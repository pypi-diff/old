# Comparing `tmp/buteo-0.8.8.tar.gz` & `tmp/buteo-0.8.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "buteo-0.8.8.tar", last modified: Fri Mar 24 10:53:42 2023, max compression
+gzip compressed data, was "buteo-0.8.9.tar", last modified: Wed Mar 29 07:28:58 2023, max compression
```

## Comparing `buteo-0.8.8.tar` & `buteo-0.8.9.tar`

### file list

```diff
@@ -1,42 +1,42 @@
--rw-r--r--   0        0        0     1089 2023-03-07 09:20:18.869934 buteo-0.8.8/LICENSE
--rw-r--r--   0        0        0     5317 2023-03-01 11:05:54.186351 buteo-0.8.8/buteo/__init__.py
--rw-r--r--   0        0        0      468 2023-03-01 11:05:54.186351 buteo-0.8.8/buteo/raster/__init__.py
--rw-r--r--   0        0        0    20205 2023-03-20 13:31:06.991294 buteo-0.8.8/buteo/raster/align.py
--rw-r--r--   0        0        0     5856 2023-03-01 11:05:54.186351 buteo-0.8.8/buteo/raster/borders.py
--rw-r--r--   0        0        0    11532 2023-03-01 14:19:56.587374 buteo-0.8.8/buteo/raster/clip.py
--rw-r--r--   0        0        0    15781 2023-03-19 10:18:25.187188 buteo-0.8.8/buteo/raster/convolution.py
--rw-r--r--   0        0        0    42190 2023-03-24 10:38:44.345747 buteo-0.8.8/buteo/raster/core_raster.py
--rw-r--r--   0        0        0    10456 2023-03-19 10:08:16.444601 buteo-0.8.8/buteo/raster/edge_detection.py
--rw-r--r--   0        0        0     5849 2023-03-01 11:05:54.186351 buteo-0.8.8/buteo/raster/grid.py
--rw-r--r--   0        0        0     3925 2023-03-01 11:05:54.186351 buteo-0.8.8/buteo/raster/morphology.py
--rw-r--r--   0        0        0    14410 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/nodata.py
--rw-r--r--   0        0        0     6657 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/patches.py
--rw-r--r--   0        0        0     6345 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/proximity.py
--rw-r--r--   0        0        0     6526 2023-03-20 12:24:41.883749 buteo-0.8.8/buteo/raster/reproject.py
--rw-r--r--   0        0        0     7297 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/resample.py
--rw-r--r--   0        0        0     4969 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/shift.py
--rw-r--r--   0        0        0    12571 2023-03-19 09:39:50.839313 buteo-0.8.8/buteo/raster/textures.py
--rw-r--r--   0        0        0     1695 2023-03-08 16:28:04.339458 buteo-0.8.8/buteo/raster/timeseries.py
--rw-r--r--   0        0        0     3270 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/vectorize.py
--rw-r--r--   0        0        0    11486 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/raster/warp.py
--rw-r--r--   0        0        0      208 2023-03-07 09:11:46.578377 buteo-0.8.8/buteo/utils/__init__.py
--rw-r--r--   0        0        0    14870 2023-03-24 08:13:00.597367 buteo-0.8.8/buteo/utils/aux_utils.py
--rw-r--r--   0        0        0    33225 2023-03-24 10:39:57.083854 buteo-0.8.8/buteo/utils/bbox_utils.py
--rw-r--r--   0        0        0    25947 2023-03-20 13:19:38.324677 buteo-0.8.8/buteo/utils/core_utils.py
--rw-r--r--   0        0        0    12683 2023-03-17 12:52:44.388017 buteo-0.8.8/buteo/utils/gdal_enums.py
--rw-r--r--   0        0        0    46247 2023-03-24 10:20:59.674911 buteo-0.8.8/buteo/utils/gdal_utils.py
--rw-r--r--   0        0        0      307 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/__init__.py
--rw-r--r--   0        0        0     4258 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/buffer.py
--rw-r--r--   0        0        0     6193 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/clip.py
--rw-r--r--   0        0        0    12800 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/convert_parts.py
--rw-r--r--   0        0        0    26159 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/core_vector.py
--rw-r--r--   0        0        0     5146 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/dissolve.py
--rw-r--r--   0        0        0      252 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/grid.py
--rw-r--r--   0        0        0     6010 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/intersect.py
--rw-r--r--   0        0        0     1777 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/merge.py
--rw-r--r--   0        0        0     6185 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/rasterize.py
--rw-r--r--   0        0        0     4388 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/reproject.py
--rw-r--r--   0        0        0    18077 2023-03-01 11:05:54.201974 buteo-0.8.8/buteo/vector/zonal_statistics.py
--rw-r--r--   0        0        0      759 2023-03-24 10:52:32.521010 buteo-0.8.8/pyproject.toml
--rw-r--r--   0        0        0     5342 2023-03-01 11:05:54.286108 buteo-0.8.8/readme.md
--rw-r--r--   0        0        0     5768 1970-01-01 00:00:00.000000 buteo-0.8.8/PKG-INFO
+-rw-r--r--   0        0        0     1089 2023-03-07 09:20:18.869934 buteo-0.8.9/LICENSE
+-rw-r--r--   0        0        0     5317 2023-03-01 11:05:54.186351 buteo-0.8.9/buteo/__init__.py
+-rw-r--r--   0        0        0      468 2023-03-01 11:05:54.186351 buteo-0.8.9/buteo/raster/__init__.py
+-rw-r--r--   0        0        0    19904 2023-03-28 08:02:37.301571 buteo-0.8.9/buteo/raster/align.py
+-rw-r--r--   0        0        0     6007 2023-03-28 08:02:37.303564 buteo-0.8.9/buteo/raster/borders.py
+-rw-r--r--   0        0        0    11138 2023-03-28 08:02:37.304561 buteo-0.8.9/buteo/raster/clip.py
+-rw-r--r--   0        0        0    18866 2023-03-28 08:02:37.306554 buteo-0.8.9/buteo/raster/convolution.py
+-rw-r--r--   0        0        0    46535 2023-03-29 07:16:39.554091 buteo-0.8.9/buteo/raster/core_raster.py
+-rw-r--r--   0        0        0    10456 2023-03-19 10:08:16.444601 buteo-0.8.9/buteo/raster/edge_detection.py
+-rw-r--r--   0        0        0     5849 2023-03-01 11:05:54.186351 buteo-0.8.9/buteo/raster/grid.py
+-rw-r--r--   0        0        0     3925 2023-03-01 11:05:54.186351 buteo-0.8.9/buteo/raster/morphology.py
+-rw-r--r--   0        0        0    14410 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/nodata.py
+-rw-r--r--   0        0        0     6657 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/patches.py
+-rw-r--r--   0        0        0     6345 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/proximity.py
+-rw-r--r--   0        0        0     6526 2023-03-20 12:24:41.883749 buteo-0.8.9/buteo/raster/reproject.py
+-rw-r--r--   0        0        0     7297 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/resample.py
+-rw-r--r--   0        0        0     4969 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/shift.py
+-rw-r--r--   0        0        0    12567 2023-03-29 07:16:39.555089 buteo-0.8.9/buteo/raster/textures.py
+-rw-r--r--   0        0        0     1695 2023-03-08 16:28:04.339458 buteo-0.8.9/buteo/raster/timeseries.py
+-rw-r--r--   0        0        0     3270 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/vectorize.py
+-rw-r--r--   0        0        0    11486 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/raster/warp.py
+-rw-r--r--   0        0        0      208 2023-03-07 09:11:46.578377 buteo-0.8.9/buteo/utils/__init__.py
+-rw-r--r--   0        0        0    14870 2023-03-29 07:24:39.870805 buteo-0.8.9/buteo/utils/aux_utils.py
+-rw-r--r--   0        0        0    33225 2023-03-24 10:39:57.083854 buteo-0.8.9/buteo/utils/bbox_utils.py
+-rw-r--r--   0        0        0    25947 2023-03-20 13:19:38.324677 buteo-0.8.9/buteo/utils/core_utils.py
+-rw-r--r--   0        0        0    12683 2023-03-17 12:52:44.388017 buteo-0.8.9/buteo/utils/gdal_enums.py
+-rw-r--r--   0        0        0    46819 2023-03-29 07:16:39.556084 buteo-0.8.9/buteo/utils/gdal_utils.py
+-rw-r--r--   0        0        0      307 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/__init__.py
+-rw-r--r--   0        0        0     4258 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/buffer.py
+-rw-r--r--   0        0        0     6193 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/clip.py
+-rw-r--r--   0        0        0    12800 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/convert_parts.py
+-rw-r--r--   0        0        0    26159 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/core_vector.py
+-rw-r--r--   0        0        0     5146 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/dissolve.py
+-rw-r--r--   0        0        0      252 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/grid.py
+-rw-r--r--   0        0        0     6010 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/intersect.py
+-rw-r--r--   0        0        0     1777 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/merge.py
+-rw-r--r--   0        0        0     6185 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/rasterize.py
+-rw-r--r--   0        0        0     4388 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/reproject.py
+-rw-r--r--   0        0        0    18077 2023-03-01 11:05:54.201974 buteo-0.8.9/buteo/vector/zonal_statistics.py
+-rw-r--r--   0        0        0      759 2023-03-29 07:25:59.882123 buteo-0.8.9/pyproject.toml
+-rw-r--r--   0        0        0     5342 2023-03-01 11:05:54.286108 buteo-0.8.9/readme.md
+-rw-r--r--   0        0        0     5768 1970-01-01 00:00:00.000000 buteo-0.8.9/PKG-INFO
```

### Comparing `buteo-0.8.8/LICENSE` & `buteo-0.8.9/LICENSE`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/__init__.py` & `buteo-0.8.9/buteo/__init__.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/align.py` & `buteo-0.8.9/buteo/raster/align.py`

 * *Files 14% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 ### Align rasters ###
 
 Functions to align a series of rasters to a master or a reference.
 """
 
 # TODO: Fix if not all a reprojected, paths/names are incorrect.
 # TODO: phase_cross_correlation
-# TODO: Ensure get_pixel_offsets works as planned.
 
 # Standard library
 import sys; sys.path.append("../../")
 
 # External
 import numpy as np
 from osgeo import gdal, ogr, osr
@@ -25,41 +24,48 @@
 
 
 def match_raster_projections(
     rasters,
     master,
     *,
     out_path=None,
-    overwrite=False,
+    overwrite=True,
     dst_nodata="infer",
     copy_if_already_correct=True,
     creation_options=None,
 ):
     """
-    Match a raster or list of rasters to a master layer. The master can be either
-    an **OGR** layer or a **GDAL** layer.
+    Match a raster or list of rasters to a master layer. The master can be
+    either an OGR layer or a GDAL layer.
 
-    ## Args:
-    `rasters` (_list_): A list of rasters to match. </br>
-    `master` (_str_/_gdal.Dataset_/_ogr.DataSource_): Path to the master raster or vector. </br>
-
-    ## Kwargs:
-    `out_path` (_str_/_list_): Paths to the output. If not provided, the output will be in-memory rasters. (Default: **None**) </br>
-    `overwrite` (_bool_): If True, existing rasters will be overwritten. (Default: **False**) </br>
-    `dst_nodata` (_str_): Value to use for no-data pixels. If not provided, the value will be transfered from the original. (Default: **"infer"**) </br>
-    `copy_if_already_correct` (_bool_): If True, the raster will be copied if it is already in the correct projection. (Default: **True**) </br>
-    `creation_options` (_list_): List of creation options to pass to the output raster. (Default: **None**) </br>
+    Args:
+        rasters (list): A list of rasters to match.
+        master (str/gdal.Dataset/ogr.DataSource): Path to the master raster
+            or vector.
+
+    Keyword Args:
+        out_path (str/list, default=None): Paths to the output. If not provided,
+            the output will be in-memory rasters.
+        overwrite (bool, default=True): If True, existing rasters will be
+            overwritten.
+        dst_nodata (str, default='infer'): Value to use for no-data pixels. If not
+            provided, the value will be transfered from the original.
+        copy_if_already_correct (bool, default=True): If True, the raster will be
+            copied if it is already in the correct projection.
+        creation_options (list, default=None): List of creation options to pass
+            to the output raster.
 
-    ## Returns:
-    (_list_): A list of reprojected input rasters with the correct projection.
+    Returns:
+        list: A list of reprojected input rasters with the correct projection.
     """
-    if isinstance(rasters, str):
-        rasters = [rasters]
+    core_utils.type_check(rasters, [str, gdal.Dataset, [str, gdal.Dataset]], "rasters")
+    core_utils.type_check(master, [str, gdal.Dataset, ogr.DataSource], "master")
+
+    rasters = core_utils.ensure_list(rasters)
 
-    assert isinstance(master, (str, gdal.Dataset, ogr.DataSource)), "master must be a string, gdal.Dataset, or ogr.DataSource."    
     assert gdal_utils.is_raster_list(rasters), "rasters must be a list of rasters."
 
     try:
         target_projection = gdal_utils.parse_projection(master)
     except Exception:
         raise ValueError(f"Unable to parse projection from master. Received: {master}") from None
 
@@ -103,37 +109,46 @@
     prefix="",
     suffix="",
     ram="auto",
 ):
     """
     Aligns a series of rasters to a master raster or specified requirements.
 
-    ## Args:
-    `rasters` (_list_): A list of rasters to align. </br>
+    Args:
+        rasters (list): A list of rasters to align.
 
-    ## Kwargs:
-    `out_path` (_str_/_list_): Paths to the output. If not provided, the output will be in-memory rasters. (Default: **None**) </br>
-    `master` (_str_/_gdal.Dataset_/_ogr.DataSource_): Path to the master raster or vector. (Default: **None**) </br>
-    `suffix` (_str_): Suffix to append to the output raster. (Default: **"_aligned"**) </br>
-    `bounding_box` (_str_): Method to use for aligning the rasters. Can be either "intersection" or "union". (Default: **"intersection"**) </br>
-    `resample_alg` (_str_): Resampling algorithm to use. (Default: **nearest**) </br>
-    `target_size` (_list_/_gdal.Dataset_/_ogr.DataSource_): Target size of the output raster. (Default: **None**) </br>
-    `target_in_pixels` (_bool_): If True, the target size will be in pixels. (Default: **False**) </br>
-    `projection` (_str_/_gdal.Dataset_/_ogr.DataSource_): Projection to use for the output raster. (Default: **None**) </br>
-    `overwrite` (_bool_): If **True**, existing rasters will be overwritten. (Default: **True**) </br>
-    `creation_options` (_list_): List of creation options to pass to the output raster. (Default: **None**) </br>
-    `src_nodata` (_str_/_int_/_float_/_None_): The source dataset of the align sets. (Default: **"infer"**) </br>
-    `dst_nodata` (_str_/_int_/_float_/_None_): The destination dataset of the align sets. (Default: **"infer"**) </br>
-    `prefix`: (_str_): Prefix to add to the output rasters. (Default: **""**) </br>
-    `suffix`: (_str_): Suffix to add to the output rasters. (Default: **""**) </br>
-    `ram`: (_int_/_str_): The ram available to **GDAL** for the processing in MB or percentage.
-    If auto 80% of available ram is allowed. (Default: **auto**) </br>
+    Keyword Args:
+        out_path (str/list, default=None): Paths to the output. If not provided,
+            the output will be in-memory rasters.
+        master (str/gdal.Dataset/ogr.DataSource, default=None): Path to the
+            master raster or vector.
+        bounding_box (str, default="intersection"): Method to use for aligning the
+            rasters. Can be either "intersection" or "union".
+        resample_alg (str, default="nearest"): Resampling algorithm to use.
+        target_size (list/gdal.Dataset/ogr.DataSource, default=None): Target size
+            of the output raster.
+        target_in_pixels (bool, default=False): If True, the target size will be
+            in pixels.
+        projection (str/gdal.Dataset/ogr.DataSource, default=None): Projection to
+            use for the output raster.
+        overwrite (bool, default=True): If True, existing rasters will be
+            overwritten.
+        creation_options (list, default=None): List of creation options to pass to
+            the output raster.
+        src_nodata (str/int/float/None, default="infer"): The source dataset of the
+            align sets.
+        dst_nodata (str/int/float/None, default="infer"): The destination dataset of
+            the align sets.
+        prefix (str, default=""): Prefix to add to the output rasters.
+        suffix (str, default=""): Suffix to append to the output raster.
+        ram (int/str, default="auto"): The ram available to GDAL for the processing
+            in MB or percentage. If auto, 80% of available ram is allowed.
 
-    ## Return:
-    (_list_): A list of paths to the aligned rasters.
+    Returns:
+        list: A list of paths to the aligned rasters.
     """
     core_utils.type_check(rasters, [str, gdal.Dataset, [str, gdal.Dataset]], "rasters")
     core_utils.type_check(out_path, [str, None, [str]], "out_path")
     core_utils.type_check(master, [str, [str], None], "master")
     core_utils.type_check(bounding_box, [str, gdal.Dataset, ogr.DataSource, list, tuple], "bounding_box")
     core_utils.type_check(resample_alg, [str], "resample_alg")
     core_utils.type_check(target_size, [tuple, list, int, float, str, gdal.Dataset, None], "target_size")
@@ -239,17 +254,16 @@
             gdal_utils.delete_if_in_memory(reprojected_target_size)
             reprojected_target_size = None
 
             # Set the target values.
             x_res = target_size_raster["width"]
             y_res = target_size_raster["height"]
         else:
-            # If a list, tuple, int or float is passed. Turn them into target values.
-            x_res, y_res, x_pixels, y_pixels = bbox_utils.get_pixel_offsets(
-                target_size, target_in_pixels
+            raise NotImplementedError(
+                "target_size must be a raster or a tuple of pixel size."
             )
 
     # If nothing has been specified, we will infer the pixel_size based on
     # the median of all input rasters.
     elif x_res is None and y_res is None and x_pixels is None and y_pixels is None:
 
         # Ready numpy arrays for insertion
@@ -400,18 +414,18 @@
             else:
                 reprojected = _reproject_raster(raster, target_projection)
                 reprojected_rasters.append(reprojected)
                 paths_to_unlink.append(gdal_utils.get_path_from_dataset(reprojected))
 
     # If any of the target values are still undefined. Throw an error!
     if target_projection is None or target_bounds is None:
-        raise Exception("Error while preparing the target projection or bounds.")
+        raise ValueError("Error while preparing the target projection or bounds.")
 
     if x_res is None and y_res is None and x_pixels is None and y_pixels is None:
-        raise Exception("Error while preparing the target pixel size.")
+        raise ValueError("Error while preparing the target pixel size.")
 
     # This is the list of rasters to return. If output is not memory, it's a list of paths.
     return_list = []
     for index, raster in enumerate(reprojected_rasters):
         raster_metadata = core_raster.raster_to_metadata(raster)
 
         out_name = path_list[index]
@@ -459,26 +473,26 @@
             resampleAlg=gdal_enums.translate_resample_method(resample_alg),
             creationOptions=gdal_utils.default_creation_options(creation_options),
             srcNodata=out_src_nodata,
             dstNodata=out_dst_nodata,
             targetAlignedPixels=False,
             cropToCutline=False,
             multithread=True,
-            # warpMemoryLimit=gdal_utils.get_gdalwarp_ram_limit(ram),
+            warpMemoryLimit=gdal_utils.get_gdalwarp_ram_limit(ram),
         )
 
         if warped is None:
-            raise Exception("Error while warping rasters.")
+            raise ValueError("Error while warping rasters.")
 
         return_list.append(out_name)
 
     # Remove the reprojected rasters if they are in memory.
     for mem_path in paths_to_unlink:
         gdal_utils.delete_if_in_memory(mem_path)
 
     if not core_raster.rasters_are_aligned(return_list, same_extent=True):
-        raise Exception("Error while aligning rasters. Output is not aligned")
+        raise ValueError("Error while aligning rasters. Output is not aligned")
 
     if isinstance(rasters, list):
         return return_list
 
     return return_list[0]
```

### Comparing `buteo-0.8.8/buteo/raster/borders.py` & `buteo-0.8.9/buteo/raster/borders.py`

 * *Files 6% similar despite different names*

```diff
@@ -121,27 +121,32 @@
     allow_lists=True,
     overwrite=True,
     creation_options=None,
 ):
     """
     Add a border to a raster.
 
-    ## Args:
-    `input_raster` (_str_/_gdal.DataSet_): The input raster.
+    Args:
+        input_raster (str/gdal.DataSet): The input raster.
 
-    ## Kwargs:
-    `out_path` (_str_/_None_): The output path. If **None** the output will be a memory raster. </br>
-    `border_size` (_int_): The size of the border. </br>
-    `border_size_unit` (_str_): The unit of the border size. </br>
-    `border_value` (_int_): The value of the border. </br>
-    `overwrite` (_bool_): If **True**, the output raster will be overwritten. </br>
-    `creation_options` (_list_/_None_): Creation options for the output raster. </br>
+    Keyword Args:
+        out_path (str/None, default=None): The output path. If None, the output
+            will be a memory raster.
+        border_size (int, default=100): The size of the border.
+        border_size_unit (str, default='px'): The unit of the border size.
+        border_value (int, default=0): The value of the border.
+        overwrite (bool, default=True): If True, the output raster will be
+            overwritten.
+        allow_lists (bool, default=True): If True, lists of rasters will be
+            allowed.
+        creation_options (list/None, default=None): Creation options for the
+            output raster.
 
-    ## Returns:
-    `out_raster` (_str_/_gdal.DataSet_): The output raster with added borders.
+    Returns:
+        str/gdal.DataSet: The output raster with added borders.
     """
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
     core_utils.type_check(out_path, [str, None], "out_path")
     core_utils.type_check(border_size, [int], "border_size")
     core_utils.type_check(border_size_unit, [str], "border_size_unit")
     core_utils.type_check(border_value, [int, float], "border_value")
     core_utils.type_check(overwrite, [bool], "overwrite")
```

### Comparing `buteo-0.8.8/buteo/raster/clip.py` & `buteo-0.8.9/buteo/raster/clip.py`

 * *Files 16% similar despite different names*

```diff
@@ -45,18 +45,18 @@
         core_utils.ensure_list(raster),
         out_path=out_path,
         prefix=prefix,
         suffix=suffix,
         add_uuid=add_uuid,
     )
 
-    if out_path is not None:
+    if out_path is not None and isinstance(out_path, str):
         if "vsimem" not in out_path:
             if not os.path.isdir(os.path.split(os.path.normpath(out_path))[0]):
-                raise ValueError(f"out_path folder does not exists: {out_path}")
+                raise ValueError(f"out_path folder does not exist: {out_path}")
 
     clip_ds = None
 
     memory_files = []
 
     # Input is a vector.
     if gdal_utils.is_vector(clip_geom):
@@ -101,15 +101,15 @@
 
     raster_metadata = core_raster._raster_to_metadata(raster)
     origin_projection = raster_metadata["projection_osr"]
 
     # Fast check: Does the extent of the two inputs overlap?
     has_inf = True in [np.isinf(val) for val in raster_metadata["bbox_latlng"]]
     if not has_inf and not bbox_utils.bboxes_intersect(raster_metadata["bbox_latlng"], clip_metadata["bbox_latlng"]):
-        raise Exception("Geometries did not intersect.")
+        raise ValueError(f"Geometries of {raster} and {clip_geom} did not intersect.")
 
     if not origin_projection.IsSame(clip_metadata["projection_osr"]):
         clip_ds = _reproject_vector(clip_ds, origin_projection)
         clip_metadata = core_vector._vector_to_metadata(clip_ds)
         memory_files.append(clip_ds)
 
     output_bounds = raster_metadata["bbox"]
@@ -130,26 +130,26 @@
     out_name = path_list[0]
     out_format = gdal_utils.path_to_driver_raster(out_name)
     out_creation_options = gdal_utils.default_creation_options(creation_options)
 
     # nodata
     if src_nodata == "infer":
         src_nodata = raster_metadata["nodata_value"]
-    elif isinstance(src_nodata, (int, float, None)):
+    elif isinstance(src_nodata, (int, float)) or src_nodata is None:
         src_nodata = float(src_nodata)
     else:
         raise ValueError(f"src_nodata must be an int, float or None: {src_nodata}")
 
     out_nodata = None
     if dst_nodata == "infer":
         if src_nodata == "infer":
             out_nodata = raster_metadata["nodata_value"]
         else:
             out_nodata = gdal_enums.get_default_nodata_value(raster_metadata["datatype_gdal_raw"])
-    elif isinstance(dst_nodata, (int, float, None)):
+    elif isinstance(dst_nodata, (int, float)) or dst_nodata is None:
         out_nodata = dst_nodata
     else:
         raise ValueError(f"Unable to parse nodata_value: {dst_nodata}")
 
     # Removes file if it exists and overwrite is True.
     core_utils.remove_if_required(out_path, overwrite)
 
@@ -177,15 +177,15 @@
 
     gdal_utils.delete_if_in_memory_list(memory_files)
 
     if verbose == 0:
         gdal.PopErrorHandler()
 
     if clipped is None:
-        raise Exception("Error while clipping raster.")
+        raise ValueError("Error while clipping raster.")
 
     return out_name
 
 
 def clip_raster(
     raster,
     clip_geom,
@@ -206,52 +206,53 @@
     verbose=0,
     add_uuid=False,
     ram="auto",
 ):
     """
     Clips a raster(s) using a vector geometry or the extents of a raster.
 
-    ## Args:
-    `raster` (_list_/_str_/_gdal.Dataset_): The raster(s) to clip. </br>
-    `clip_geom` (_str_/_ogr.DataSource_/_gdal.Dataset_): The geometry to use to clip the raster </br>
-
-    ## Kwargs:
-    `out_path` (_str_/_list_/_None_): The path(s) to save the clipped raster to. If None a memory raster is created. (Default: **None**)</br>
-    `resample_alg` (_str_): The resampling algorithm to use. (Default: **nearest**) </br>
-    &emsp; • **nearest**: Nearest neighbour. </br>
-    &emsp; • **bilinear**: Bilinear. </br>
-    &emsp; • **cubic**: Cubic. </br>
-    &emsp; • **cubicspline**: Cubic spline. </br>
-    &emsp; • **lanczos**: Lanczos. </br>
-    &emsp; • **average**: Average. </br>
-    &emsp; • **mode**: Mode. </br>
-    &emsp; • **max**: Max. </br>
-    &emsp; • **min**: Min. </br>
-    &emsp; • **median**: Median. </br>
-    &emsp; • **q1**: Quartile 1 </br>
-    &emsp; • **q3**: Quartile 3 </br>
-    &emsp; • **sum**: Sum </br>
-    &emsp; • **rms**: Root Mean Squared </br>
-    `crop_to_geom` (_bool_): If True, the output raster will be cropped to the extent of the clip geometry. (Default: **True**)</br>
-    `adjust_bbox` (_bool_): If True, the output raster have its bbox adjusted to match the clip geometry. (Default: **False**)</br>
-    `all_touch` (_bool_): If true all pixels touching the clipping geometry will be included. (Default: **False**)</br>
-    `to_extent` (_bool_): If True, the output raster will be cropped to the extent of the clip geometry. (Default: **False**)</br>
-    `prefix` (_str_): The prefix to use for the output raster. (Default: **""**)</br>
-    `suffix` (_str_): The suffix to use for the output raster. (Default: **""**)</br>
-    `overwrite` (_bool_): If True, the output raster will be overwritten if it already exists. (Default: **True**)</br>
-    `creation_options` (_list_/_None_): A list of creation options to pass to gdal. (Default: **None**)</br>
-    `dst_nodata` (_int_/_float_/_None_): The nodata value to use for the output raster. (Default: **infer**)</br>
-    `src_nodata` (_int_/_float_/_None_): The nodata value to use for the input raster. (Default: **infer**)</br>
-    `layer_to_clip` (_int_/_str_): The layer ID or name in the vector to use for clipping. (Default: **0**)</br>
-    `verbose` (_int_): The verbosity level. (Default: **0**)</br>
-    `add_uuid` (_bool_): If True, a UUID will be added to the output raster. (Default: **False**)</br>
-    `ram` (_str_): The amount of RAM to use for the operation. (Default: **auto**)</br>
-
-    ## Returns:
-    (_str_/_list_): A string or list of strings representing the path(s) to the clipped raster(s).
+    Args:
+        raster (list/str/gdal.Dataset): The raster(s) to clip.
+        clip_geom (str/ogr.DataSource/gdal.Dataset): The geometry to use to
+            clip the raster.
+
+    Keyword Args:
+        out_path (str/list/None, default=None): The path(s) to save the
+            clipped raster to. If None, a memory raster is created.
+        resample_alg (str, default="nearest"): The resampling algorithm to use.
+            Options include: nearest, bilinear, cubic, cubicspline, lanczos, average,
+                mode, max, min, median, q1, q3, sum, rms.
+        crop_to_geom (bool, default=True): If True, the output raster will be
+            cropped to the extent of the clip geometry.
+        adjust_bbox (bool, default=False): If True, the output raster will have its
+            bbox adjusted to match the clip geometry.
+        all_touch (bool, default=False): If true, all pixels touching the
+            clipping geometry will be included.
+        to_extent (bool, default=False): If True, the output raster will be
+            cropped to the extent of the clip geometry.
+        prefix (str, default=""): The prefix to use for the output raster.
+        suffix (str, default=""): The suffix to use for the output raster.
+        overwrite (bool, default=True): If True, the output raster will be
+            overwritten if it already exists.
+        creation_options (list/None, default=None): A list of creation options
+            to pass to gdal.
+        dst_nodata (int/float/None, default="infer"): The nodata value to use for
+            the output raster.
+        src_nodata (int/float/None, default="infer"): The nodata value to use for
+            the input raster.
+        layer_to_clip (int/str, default=0): The layer ID or name in the
+            vector to use for clipping.
+        verbose (int, default=0): The verbosity level.
+        add_uuid (bool, default=False): If True, a UUID will be added to the
+            output raster.
+        ram (str, default="auto"): The amount of RAM to use for the operation.
+
+    Returns:
+        str/list: A string or list of strings representing the path(s) to
+            the clipped raster(s).
     """
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
     core_utils.type_check(clip_geom, [str, ogr.DataSource, gdal.Dataset], "clip_geom")
     core_utils.type_check(out_path, [[str], str, None], "out_path")
     core_utils.type_check(resample_alg, [str], "resample_alg")
     core_utils.type_check(crop_to_geom, [bool], "crop_to_geom")
     core_utils.type_check(adjust_bbox, [bool], "adjust_bbox")
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `buteo-0.8.8/buteo/raster/core_raster.py` & `buteo-0.8.9/buteo/raster/core_raster.py`

 * *Files 7% similar despite different names*

```diff
@@ -9,15 +9,14 @@
 # Standard library
 import sys; sys.path.append("../../")
 import os
 
 # External
 import numpy as np
 from osgeo import gdal, osr, ogr
-from osgeo_utils.samples import validate_cloud_optimized_geotiff
 
 # Internal
 from buteo.utils import bbox_utils, core_utils, gdal_utils, gdal_enums
 
 
 
 def _open_raster(raster, *, writeable=True):
@@ -32,42 +31,50 @@
         gdal.PushErrorHandler("CPLQuietErrorHandler")
         opened = gdal.Open(raster, gdal.GF_Write) if writeable else gdal.Open(raster, gdal.GF_Read)
         gdal.PopErrorHandler()
 
         if not isinstance(opened, gdal.Dataset):
             raise ValueError(f"Input raster is not readable. Received: {raster}")
 
+        if opened.GetDescription() == "":
+            opened.SetDescription(raster)
+
+        if opened.GetProjectionRef() == "":
+            opened.SetProjection(gdal_utils.get_default_projection())
+            print(f"WARNING: Input raster {raster} has no projection. Setting to default: EPSG:4326.")
+
         return opened
 
     raise ValueError(f"Input raster does not exists. Received: {raster}")
 
 
 def open_raster(raster, *, writeable=True, allow_lists=True):
     """
     Opens a raster from a path to a raster. Can be in-memory or local. If a
-    gdal.Dataset is passed it is returned. Supports lists. If a list is passed
+    gdal.Dataset is passed, it is returned. Supports lists. If a list is passed,
     a list is returned with the opened raster.
 
-    ## Args:
-    `raster` (_gdal.Dataset_/_str_/_list_): A path to a raster or a GDAL dataframe. </br>
+    Args:
+        raster (gdal.Dataset/str/list): A path to a raster or a GDAL dataframe.
 
-    ## Kwargs:
-    `writeable` (_bool_): If True, the raster is opened in write mode. (Default: **True**) </br>
-    `allow_lists` (_bool_): If True, the input can be a list of rasters. Otherwise, only
-    a single raster is allowed. (Default: **True**) </br>
+    Keyword Args:
+        writeable (bool, default=True): If True, the raster is opened in write mode. Default is True.
+        allow_lists (bool, default=True): If True, the input can be a list of rasters. Otherwise,
+            only a single raster is allowed. Default is True.
 
-    ## Returns:
-    (_gdal.Dataset_/_list_): A gdal.Dataset or a list of gdal.Datasets.
+    Returns:
+        gdal.Dataset/list: A gdal.Dataset or a list of gdal.Datasets.
     """
+
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
     core_utils.type_check(writeable, [bool], "writeable")
     core_utils.type_check(allow_lists, [bool], "allow_lists")
 
-    if not allow_lists and isinstance(raster, list):
-        raise ValueError("Input raster must be a single raster.")
+    if not allow_lists and isinstance(raster, (list, tuple)):
+        raise ValueError("Input raster must be a single raster. Not a list or tuple.")
 
     if not allow_lists:
         return _open_raster(raster, writeable=writeable)
 
     list_input = core_utils.ensure_list(raster)
     list_return = []
 
@@ -80,26 +87,38 @@
     if isinstance(raster, list):
         return list_return
 
     return list_return[0]
 
 
 def get_projection(raster, wkt=True):
-    """ Gets the projection as WKT from a dataset. Path or gdal.Dataset. """
+    """
+    Gets the projection from a dataset, either as WKT or in another format.
+    The input can be a path or a gdal.Dataset.
+
+    Args:
+        raster (str/gdal.Dataset): A path to a raster or a gdal.Dataset.
+
+    Keyword Args:
+        wkt (bool, default=True): If True, returns the projection as WKT.
+
+    Returns:
+        str: The projection of the input raster in the specified format.
+    """
     dataset = open_raster(raster)
 
     if wkt:
         return dataset.GetProjectionRef()
-    else:
-        return dataset.GetProjection()
+
+    return dataset.GetProjection()
 
 
 def _raster_to_metadata(raster):
     """ Internal. """
-    assert isinstance(raster, (str, gdal.Dataset))
+    core_utils.type_check(raster, [str, gdal.Dataset], "raster")
 
     dataset = open_raster(raster)
 
     raster_driver = dataset.GetDriver()
 
     path = dataset.GetDescription()
     basename = os.path.basename(path)
@@ -118,15 +137,15 @@
     projection_osr.ImportFromWkt(projection_wkt)
 
     width = dataset.RasterXSize
     height = dataset.RasterYSize
     band_count = dataset.RasterCount
 
     size = [dataset.RasterXSize, dataset.RasterYSize]
-    shape = (width, height, band_count)
+    shape = (height, width, band_count)
 
     pixel_width = abs(transform[1])
     pixel_height = abs(transform[5])
 
     x_min = transform[0]
     y_max = transform[3]
 
@@ -164,14 +183,17 @@
         "shape": shape,
         "pixel_width": pixel_width,
         "pixel_height": pixel_height,
         "x_min": x_min,
         "y_max": y_max,
         "x_max": x_max,
         "y_min": y_min,
+        "dtype": datatype,
+        "dtype_gdal": datatype_gdal,
+        "dtype_gdal_raw": datatype_gdal_raw,
         "datatype": datatype,
         "datatype_gdal": datatype_gdal,
         "datatype_gdal_raw": datatype_gdal_raw,
         "nodata_value": nodata_value,
         "has_nodata": has_nodata,
         "is_raster": True,
         "is_vector": False,
@@ -183,41 +205,45 @@
         metadata[key] = value
 
     def get_bbox_as_vector():
         return bbox_utils.convert_bbox_to_vector(bbox_ogr, projection_osr)
 
 
     def get_bbox_as_vector_latlng():
+        latlng_wkt = gdal_utils.get_default_projection()
         projection_osr_latlng = osr.SpatialReference()
-        # projection_osr_latlng.ImportFromEPSG(4326)
-        projection_osr_latlng.ImportFromWkt('GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]')
+        projection_osr_latlng.ImportFromWkt(latlng_wkt)
 
         return bbox_utils.convert_bbox_to_vector(metadata["bbox_latlng"], projection_osr_latlng)
 
 
     metadata["get_bbox_vector"] = get_bbox_as_vector
     metadata["get_bbox_vector_latlng"] = get_bbox_as_vector_latlng
 
     return metadata
 
 
 def raster_to_metadata(raster, *, allow_lists=True):
     """
-    Reads a raster from a list of rasters, string or a dataset and returns metadata.
-
-    ## Args:
-    `raster` (_gdal.Dataset_/_str_/_list_): A GDAL dataframe or a path to a raster. </br>
-
-    ## Kwargs:
-    `allow_lists` (_bool_): If True, the input can be a list of rasters. Otherwise, only
-    a single raster is allowed. (Default: **True**) </br>
+    Reads metadata from a raster dataset or a list of raster datasets, and returns a dictionary or a list of dictionaries
+    containing metadata information for each raster.
 
-    ## Returns:
-    (_dict_/_list_): A dictionary or list of dictionaries containing metadata.
+    Args:
+        raster (str/gdal.Dataset/list): A path to a raster or a gdal.Dataset,
+            or a list of paths to rasters.
+
+    Keyword Args:
+        allow_lists (bool, default=True): If True, allows the input to be a
+            list of rasters. Otherwise, only a single raster is allowed.
+
+    Returns:
+        dict/list of dict: A dictionary or a list of dictionaries containing
+            metadata information for each raster.
     """
+
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
 
     if not allow_lists and isinstance(raster, list):
         raise ValueError("Input raster must be a single raster.")
 
     if not allow_lists:
         return _raster_to_metadata(raster)
@@ -233,34 +259,38 @@
 
     return list_return[0]
 
 
 def rasters_are_aligned(
     rasters,
     *,
-    same_extent=False,
+    same_extent=True,
     same_dtype=False,
     same_nodata=False,
     threshold=0.001,
 ):
     """
-    Verifies if a list of rasters are aligned.
-
-    ## Args:
-    `rasters` (_list_): A list of raster, either in gdal.Dataset or a string
-    refering to the dataset. </br>
+    Verifies whether a list of rasters are aligned.
 
-    ## Kwargs:
-    `same_extent` (_bool_): Should all the rasters have the same extent? (Default: **False**). </br>
-    `same_dtype` (_bool_): Should all the rasters have the same data type? (Default: **False**)
-    `same_dtype` (_bool_): Should all the rasters have the same data nodata value? (Default: **False**). </br>
-    `threshold` (_float_): The threshold for the difference between the rasters. (Default: **0.001**). </br>
+    Args:
+        rasters (list): A list of rasters, either in gdal.Dataset or a string
+            referring to the dataset.
+
+    Keyword Args:
+        same_extent (bool, default=True): If True, all the rasters should have
+            the same extent.
+        same_dtype (bool, default=False): If True, all the rasters should have
+            the same data type.
+        same_nodata (bool, default=False): If True, all the rasters should have
+            the same nodata value.
+        threshold (float, default=0.001): The threshold for the difference between
+            the rasters.
 
-    ## Returns:
-    (_bool_): **True** if rasters and aligned and optional parameters are True, **False** otherwise.
+    Returns:
+        bool: True if rasters are aligned and optional parameters are True, False otherwise.
     """
     core_utils.type_check(rasters, [[str, gdal.Dataset]], "rasters")
     core_utils.type_check(same_extent, [bool], "same_extent")
     core_utils.type_check(same_dtype, [bool], "same_dtype")
     core_utils.type_check(same_nodata, [bool], "same_nodata")
 
     if len(rasters) == 1:
@@ -285,14 +315,15 @@
     }
 
     for index, raster in enumerate(rasters):
         meta = _raster_to_metadata(raster)
         if index == 0:
             base["name"] = meta["name"]
             base["projection_wkt"] = meta["projection_wkt"]
+            base["projection_osr"] = meta["projection_osr"]
             base["pixel_width"] = meta["pixel_width"]
             base["pixel_height"] = meta["pixel_height"]
             base["x_min"] = meta["x_min"]
             base["y_max"] = meta["y_max"]
             base["transform"] = meta["transform"]
             base["width"] = meta["width"]
             base["height"] = meta["height"]
@@ -343,211 +374,343 @@
             if same_nodata:
                 if meta["nodata_value"] != base["nodata_value"]:
                     return False
 
     return True
 
 
+def raster_has_nodata(raster):
+    """
+    Verifies whether a raster has any nodata values.
+
+    Args:
+        raster (str): A raster, either in gdal.Dataset or a string
+            referring to the dataset.
+
+    Returns:
+        bool: True if raster has nodata values, False otherwise.
+    """
+    core_utils.type_check(raster, [str, gdal.Dataset], "raster")
+
+    ref = open_raster(raster)
+    band_count = ref.RasterCount
+    for band in range(1, band_count + 1):
+        band_ref = ref.GetRasterBand(band)
+        if band_ref.GetNoDataValue() is not None:
+            ref = None
+
+            return True
+
+    ref = None
+    return False
+
+
+def rasters_have_nodata(rasters):
+    """
+    Verifies whether a list of rasters have any nodata values.
+
+    Args:
+        rasters (list): A list of rasters, either in gdal.Dataset or a string
+    """
+    core_utils.type_check(rasters, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
+
+    internal_rasters = core_utils.ensure_list(rasters)
+    assert gdal_utils.is_raster_list(internal_rasters), "Invalid raster list."
+
+    has_nodata = False
+    for in_raster in internal_rasters:
+        if raster_has_nodata(in_raster):
+            has_nodata = True
+            break
+
+    return has_nodata
+
+
+def rasters_have_same_nodata(rasters):
+    """
+    Verifies whether a list of rasters have the same nodata values.
+
+    Args:
+        rasters (list): A list of rasters, either in gdal.Dataset or a string
+    """
+    core_utils.type_check(rasters, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
+
+    internal_rasters = core_utils.ensure_list(rasters)
+    assert gdal_utils.is_raster_list(internal_rasters), "Invalid raster list."
+
+    nodata_values = []
+    for in_raster in internal_rasters:
+        ref = open_raster(in_raster)
+        band_count = ref.RasterCount
+        for band in range(1, band_count + 1):
+            band_ref = ref.GetRasterBand(band)
+            nodata_values.append(band_ref.GetNoDataValue())
+
+        ref = None
+
+    return len(set(nodata_values)) == 1
+
+
+def get_first_nodata_value(raster):
+    """
+    Gets the first nodata value from a raster.
+
+    Args:
+        raster (str/gdal.Dataset): The raster to get the nodata value from.
+    """
+    core_utils.type_check(raster, [str, gdal.Dataset], "raster")
+
+    nodata = None
+
+    ref = open_raster(raster)
+    band_count = ref.RasterCount
+    for band in range(1, band_count + 1):
+        band_ref = ref.GetRasterBand(band)
+        nodata_value = band_ref.GetNoDataValue()
+        if nodata_value is not None:
+            nodata = nodata_value
+            break
+
+    ref = None
+    return nodata
+
+
 def raster_to_array(
     raster,
     *,
-    bands=-1,
+    bands='all',
+    masked="auto",
     filled=False,
+    fill_value=None,
     bbox=None,
     pixel_offsets=None,
-    stack=True,
-    split=False,
 ):
     """
-    Turns a path to a raster(s) or a GDAL.Dataset(s) into a **NumPy** array(s).
+    Converts a raster or a list of rasters into a NumPy array.
 
-    ## Args:
-    (_gdal.Dataset_/_str_/_list_): The raster(s) to convert.
+    Args:
+        raster (gdal.Dataset/str/list): Raster(s) to convert.
 
-    ## Kwargs:
-    `bands` (_list_/_str_/_int_): The bands from the raster to turn
-    into a numpy array. Can be "all", "ALL", a list of ints or a
-    single int. </br>
-    `filled` (_bool_): If the array contains nodata values. Should the
-    resulting array be a filled numpy array or a masked array? </br>
-    `bbox` (_list_): A list of `[xmin, xmax, ymin, ymax]` to use as the
-    extent of the raster. Uses coordinates and the **OGR** format. </br>
-    `pixel_offsets` (_list_): A list of [x_offset, y_offset, x_size, y_size] to use as
-    the extent of the raster. Uses pixel offsets and the **OGR** format. </br>
-    `stack` (_bool_): If True, stacks the input rasters into a single array. Only works if
-    the rasters are aligned. (Default: **True**) </br>
-    `split` (_bool_): If True, splits the bands of the input rasters into seperate arrays. (Default: **False**)
+    Keyword Args:
+        bands (list/str/int, default="all"): Bands from the raster to convert to a numpy array.
+            Can be "all", an int, or a list of integers, or a single integer.
+        masked (bool/str, default="auto"): If the array contains nodata values, determines whether
+            the resulting array should be a masked numpy array or a regular numpy array. If "auto",
+            the array will be masked only if the raster has nodata values.
+        filled (bool, default=False): If the array contains nodata values, determines whether
+            the resulting array should be a filled numpy array or a masked array.
+        fill_value (int/float, default=None): Value to fill the array with if filled is True.
+            If None, the nodata value of the raster is used.
+        bbox (list, default=None): A list of `[xmin, xmax, ymin, ymax]` to use as
+            the extent of the raster. Uses coordinates and the OGR format.
+        pixel_offsets (list, default=None): A list of
+            `[x_offset, y_offset, x_size, y_size]` to use as the extent of the
+            raster. Uses pixel offsets and the OGR format.
 
-    ## Returns:
-    (_np.ndarray_): A numpy array in the 3D channel-last format unless output_2D is
-    specified. </br>
+    Returns:
+        np.ndarray: A numpy array in the 3D channel-last format.
     """
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
-    core_utils.type_check(bands, [int, list], "bands")
+    core_utils.type_check(bands, [int, [int], str], "bands")
     core_utils.type_check(filled, [bool], "filled")
+    core_utils.type_check(fill_value, [int, float, None], "fill_value")
+    core_utils.type_check(masked, [bool, str], "masked")
     core_utils.type_check(bbox, [list, None], "bbox")
     core_utils.type_check(pixel_offsets, [list, None], "pixel_offsets")
-    core_utils.type_check(stack, [bool], "stack")
-    core_utils.type_check(split, [bool], "split")
+
+    if masked not in ["auto", True, False]:
+        raise ValueError(f"masked must be 'auto', True, or False. {masked} was provided.")
+
+    if bbox is not None and pixel_offsets is not None:
+        raise ValueError("Cannot use both bbox and pixel_offsets.")
 
     internal_rasters = core_utils.ensure_list(raster)
 
     if not gdal_utils.is_raster_list(internal_rasters):
         raise ValueError(f"An input raster is invalid. {internal_rasters}")
 
     internal_rasters = gdal_utils.get_path_from_dataset_list(internal_rasters, dataset_type="raster")
 
-    if stack and not rasters_are_aligned(internal_rasters, same_extent=True, same_dtype=False):
+    if len(internal_rasters) > 1 and not rasters_are_aligned(internal_rasters, same_extent=True, same_dtype=False):
         raise ValueError(
             "Cannot merge rasters that are not aligned, have dissimilar extent or dtype, when stack=True."
         )
 
-    layers = []
-    nodata_values = []
-    for in_raster in internal_rasters:
+    # Read metadata
+    metadata = raster_to_metadata(internal_rasters[0])
+    dtype = metadata["dtype"]
+    shape = metadata["shape"]
+
+    # Determine output shape
+    x_offset, y_offset, x_size, y_size = 0, 0, shape[1], shape[0]
+
+    if pixel_offsets is not None:
+        x_offset, y_offset, x_size, y_size = pixel_offsets
+
+        if x_offset < 0 or y_offset < 0:
+            raise ValueError("Pixel offsets cannot be negative.")
+
+        if x_offset + x_size > shape[1] or y_offset + y_size > shape[0]:
+            raise ValueError("Pixel offsets are outside of raster.")
+
+    elif bbox is not None:
+        if not bbox_utils.bboxes_intersect(metadata["bbox"], bbox):
+            raise ValueError("Extent is outside of raster.")
 
-        if not gdal_utils.is_raster(in_raster):
-            raise ValueError(f"Invalid raster: {in_raster}")
+        x_offset, y_offset, x_size, y_size = bbox_utils.get_pixel_offsets(metadata["transform"], bbox)
+
+    output_shape = (y_size, x_size, len(internal_rasters) * shape[2])
+
+    # Determine nodata and value
+    if masked == "auto":
+        has_nodata = rasters_have_nodata(internal_rasters)
+        if has_nodata:
+            masked = True
+        else:
+            masked = False
+
+    output_nodata_value = None
+    if masked or filled:
+        output_nodata_value = get_first_nodata_value(internal_rasters[0])
+
+        if output_nodata_value is None:
+            output_nodata_value = np.nan
+
+        if filled and fill_value is None:
+            fill_value = output_nodata_value
+
+    # Create output array
+    if masked:
+        output_arr = np.ma.empty(output_shape, dtype=dtype)
+        output_arr.mask = True
+
+        if filled:
+            output_arr.fill_value = fill_value
+        else:
+            output_arr.fill_value = output_nodata_value
+    else:
+        output_arr = np.empty(output_shape, dtype=dtype)
+
+
+    band_idx = 0
+    for in_raster in internal_rasters:
 
         ref = open_raster(in_raster)
 
         metadata = raster_to_metadata(ref)
         band_count = metadata["band_count"]
-        band_arrs = []
 
         if band_count == 0:
             raise ValueError("The input raster does not have any valid bands.")
 
+        if bands == "all":
+            bands = -1
+
         internal_bands = gdal_utils.to_band_list(bands, metadata["band_count"])
 
         for band in internal_bands:
             band_ref = ref.GetRasterBand(band + 1)
             band_nodata_value = band_ref.GetNoDataValue()
 
-            nodata_values.append(band_nodata_value)
-
-            if pixel_offsets is not None:
-                arr = band_ref.ReadAsArray(
-                    pixel_offsets[0], # x_offset
-                    pixel_offsets[1], # y_offset
-                    pixel_offsets[2], # x_size
-                    pixel_offsets[3], # y_size
-                )
-            elif bbox is not None:
-                if not bbox_utils.bboxes_intersect(metadata["bbox"], bbox):
-                    raise ValueError("Extent is outside of raster.")
-
-                x_offset, y_offset, x_size, y_size = bbox_utils.get_pixel_offsets(metadata["transform"], bbox)
-
+            if pixel_offsets is not None or bbox is not None:
                 arr = band_ref.ReadAsArray(x_offset, y_offset, x_size, y_size)
             else:
                 arr = band_ref.ReadAsArray()
 
-            if band_nodata_value is not None:
-                arr = np.ma.array(arr, mask=arr == band_nodata_value)
-                arr.fill_value = band_nodata_value
-
-                if filled:
-                    arr = arr.filled(band_nodata_value)
-
-            band_arrs.append(arr)
-
-        if split:
-            layers.append(band_arrs)
-        elif band_nodata_value is None:
-            layers.append(np.dstack(band_arrs))
-        else:
-            layers.append(np.ma.dstack(band_arrs))
+            if arr.shape[0] == 0 or arr.shape[1] == 0:
+                raise RuntimeWarning("The output data has no rows or columns.")
 
-        ref = None
+            if masked or filled:
+                if band_nodata_value is not None:
+                    masked_arr = np.ma.array(arr, mask=arr == band_nodata_value, copy=False)
+                    masked_arr.fill_value = output_nodata_value
+
+                    if filled:
+                        arr = np.ma.getdata(masked_arr.filled(fill_value))
+                    else:
+                        arr = masked_arr
 
-    if split:
-        if stack:
-            return layers
-
-        output = []
-        for layer in layers:
-            for band in layer:
-                output.append(band)
+            output_arr[:, :, band_idx] = arr
 
-        return output
+            band_idx += 1
 
-    if not core_utils.is_list_all_the_same(nodata_values):
-        fill_value = gdal_enums.get_default_nodata_value(layers[0].dtype)
-        for idx, layer in enumerate(layers):
-            layer[idx].fill_value = fill_value
-
-    output = layers
-
-    if stack:
-        if core_utils.is_list_all_val(nodata_values, None):
-            output = np.dstack(layers)
-        else:
-            output = np.ma.dstack(layers)
+        ref = None
 
-    return output
+    return output_arr
 
 
 def array_to_raster(
     array,
     *,
     reference,
     out_path=None,
     set_nodata="arr",
     allow_mismatches=False,
     pixel_offsets=None,
+    bbox=None,
     overwrite=True,
     creation_options=None,
 ):
     """
-    Turns a **NumPy** array into a **GDAL** dataset or exported
+    Turns a NumPy array into a GDAL dataset or exported
     as a raster using a reference raster.
 
-    ## Args:
-    `array` (_np.ndarray_): The numpy array to convert. </br>
-    `reference` (_str_/_gdal.Dataset_): The reference raster to use for the output. </br>
-
-    ## Kwargs:
-    `out_path` (_path_): The destination to save to. (Default: **None**)</br>
-    `set_nodata` (_bool_/_float_/_int_): Can be set to: (Default: **arr**)</br>
-    `allow_mismatches` (_bool_): If True, the array can have a different shape than the reference raster.
-    `overwrite` (_bool_): If the file exists, should it be overwritten? (Default: **True**) </br>
-    &emsp; • **"arr"**: The nodata value will be the same as the **NumPy** array. </br>
-    &emsp; • **"ref"**: The nodata value will be the same as the reference raster. </br>
-    &emsp; • **"value"**: The nodata value will be the value provided. </br>
-    `creation_options` (_list_): List of **GDAL** creation options. Defaults are: </br>
-    &emsp; • "TILED=YES" </br>
-    &emsp; • "NUM_THREADS=ALL_CPUS" </br>
-    &emsp; • "BIGG_TIF=YES" </br>
-    &emsp; • "COMPRESS=LZW" </br>
+    Args:
+        array (np.ndarray): The numpy array to convert.
+        reference (str/gdal.Dataset): The reference raster to use for the output.
+
+    Keyword Args:
+        out_path (path, default=None): The destination to save to.
+        set_nodata (bool/float/int, default="arr"): Can be set to
+            • "arr": The nodata value will be the same as the NumPy array.
+            • "ref": The nodata value will be the same as the reference raster.
+            • value: The nodata value will be the value provided.
+        allow_mismatches (bool, default=False): If True, the array can have a
+            different shape than the reference raster.
+        pixel_offsets (list, default=None): If provided, the array will be
+            written to the reference raster at the specified pixel offsets.
+            The list should be in the format [x_offset, y_offset, x_size, y_size].
+        bbox (list, default=None): If provided, the array will be written to
+            the reference raster at the specified bounding box.
+            The list should be in the format [min_x, min_y, max_x, max_y].
+        overwrite (bool, default=True): If the file exists, should it be
+            overwritten?
+        creation_options (list, default=["TILED=YES", "NUM_THREADS=ALL_CPUS",
+            "BIGTIFF=YES", "COMPRESS=LZW"]): List of GDAL creation options.
 
-    ## Returns:
-    (_str_): The filepath to the newly created raster(s).
+    Returns:
+        str: The filepath to the newly created raster(s).
     """
     core_utils.type_check(array, [np.ndarray, np.ma.MaskedArray], "array")
     core_utils.type_check(reference, [str, gdal.Dataset], "reference")
     core_utils.type_check(out_path, [str, None], "out_path")
     core_utils.type_check(overwrite, [bool], "overwrite")
     core_utils.type_check(pixel_offsets, [[int, float], None], "pixel_offsets")
     core_utils.type_check(allow_mismatches, [bool], "allow_mismatches")
     core_utils.type_check(set_nodata, [int, float, str, None], "set_nodata")
     core_utils.type_check(creation_options, [[str], None], "creation_options")
 
     # Verify the numpy array
     if (
-        not isinstance(array, (np.ndarray, np.ma.MaskedArray))
-        or array.size == 0
+        array.size == 0
         or array.ndim < 2
         or array.ndim > 3
     ):
         raise ValueError(f"Input array is invalid {array}")
 
-    if set_nodata != "arr" and set_nodata != "ref":
+    if set_nodata not in ["arr", "ref"]:
         core_utils.type_check(set_nodata, [int, float], "set_nodata")
 
+    if pixel_offsets is not None:
+        if len(pixel_offsets) != 4:
+            raise ValueError("pixel_offsets must be a list of 4 values.")
+
+    if pixel_offsets is not None and bbox is not None:
+        raise ValueError("pixel_offsets and bbox cannot be used together.")
+
     # Parse the driver
     driver_name = "GTiff" if out_path is None else gdal_utils.path_to_driver_raster(out_path)
     if driver_name is None:
         raise ValueError(f"Unable to parse filetype from path: {out_path}")
 
     driver = gdal.GetDriverByName(driver_name)
     if driver is None:
@@ -584,36 +747,36 @@
 
     # Weird double issue with GDAL and numpy. Cast to float or int
     if input_nodata is not None:
         input_nodata = float(input_nodata)
         if (input_nodata).is_integer() is True:
             input_nodata = int(input_nodata)
 
-
-    if (metadata["width"] != array.shape[1] or metadata["height"] != array.shape[0]) and pixel_offsets is None:
+    if (metadata["width"] != array.shape[1] or metadata["height"] != array.shape[0]) and pixel_offsets is None and bbox is None:
         if not allow_mismatches:
             raise ValueError(f"Input array and raster are not of equal size. Array: {array.shape[:2]} Raster: {metadata['width'], metadata['height']}")
 
         print("WARNING: Input array and raster are not of equal size.")
 
+    if bbox is not None:
+        pixel_offsets = bbox_utils.get_pixel_offsets(metadata["transform"], bbox)
+
     if pixel_offsets is not None:
-        if len(pixel_offsets) != 2 and len(pixel_offsets) != 4:
-            raise ValueError(f"Pixel offsets must be a list of two or four values. {pixel_offsets}")
+        x_offset, y_offset, x_size, y_size = pixel_offsets
 
-        if len(pixel_offsets) == 4:
-            if array.ndim == 3:
-                array = array[:pixel_offsets[3], :pixel_offsets[2]:, :] # numpy is col, row order
-            else:
-                array = array[:pixel_offsets[3], :pixel_offsets[2]]
+        if array.ndim == 3:
+            array = array[:y_size, :x_size:, :] # numpy is col, row order
+        else:
+            array = array[:y_size, x_size]
 
         metadata["transform"] = (
-            metadata["transform"][0] + (pixel_offsets[0] * metadata["pixel_width"]),
+            metadata["transform"][0] + (x_offset * metadata["pixel_width"]),
             metadata["transform"][1],
             metadata["transform"][2],
-            metadata["transform"][3] - (pixel_offsets[1] * metadata["pixel_height"]),
+            metadata["transform"][3] - (y_offset * metadata["pixel_height"]),
             metadata["transform"][4],
             metadata["transform"][5],
         )
 
     destination = driver.Create(
         output_name,
         array.shape[1],
@@ -687,14 +850,17 @@
     driver = gdal.GetDriverByName(driver_name)
 
     if driver is None:
         raise ValueError(f"Unable to get driver for raster: {raster}")
 
     core_utils.remove_if_required(path, overwrite)
 
+    if isinstance(dtype_str, str):
+        dtype_str = dtype_str.lower()
+
     copy = driver.Create(
         path,
         metadata["height"],
         metadata["width"],
         metadata["band_count"],
         gdal_enums.translate_str_to_gdal_dtype(dtype_str),
         gdal_utils.default_creation_options(creation_options),
@@ -726,33 +892,36 @@
     out_path=None,
     *,
     overwrite=True,
     allow_lists=True,
     creation_options=None,
 ):
     """
-    Changes the datatype of a raster.
-
-    ## Args:
-    `raster` (_str_/_gdal.Dataset_/_list_): The raster to change the datatype of. </br>
-    `dtype` (_str_): The new datatype. </br>
-
-    ## Kwargs:
-    `out_path` (_path_/_list_): The destination to save to. (Default: **None**)</br>
-    `overwrite` (_bool_): If the file exists, should it be overwritten? (Default: **True**) </br>
-    `allow_lists` (_bool_): If True, the input can be a list of rasters. Otherwise, only single rasters
-    are allowed. (Default: **True**) </br>
-    `creation_options` (_list_): List of **GDAL** creation options. Defaults are: </br>
-        * "TILED=YES"
-        * "NUM_THREADS=ALL_CPUS"
-        * "BIGG_TIF=YES"
-        * "COMPRESS=LZW"
+    Converts the datatype of a raster.
 
-    ## Returns:
-    (_str_/_list_): The filepath or list of filepaths to the newly created raster(s).
+    Args:
+        raster (str/gdal.Dataset/list): The input raster(s) for which the
+            datatype will be changed.
+        dtype (str): The target datatype for the output raster(s).
+
+    Keyword Args:
+        out_path (path/list, default=None): The output location for the
+            processed raster(s).
+        overwrite (bool, default=True): Determines whether to overwrite
+            existing files with the same name.
+        allow_lists (bool, default=True): Allows processing multiple
+            rasters as a list. If set to False, only single rasters are
+            accepted.
+        creation_options (list, default=["TILED=YES", "NUM_THREADS=ALL_CPUS",
+            "BIGTIFF=YES", "COMPRESS=LZW"]): A list of GDAL creation options
+            for the output raster(s).
+
+    Returns:
+        str/list: The filepath(s) of the newly created raster(s) with
+            the specified datatype.
     """
     core_utils.type_check(raster, [str, gdal.Dataset, [str, gdal.Dataset]], "raster")
     core_utils.type_check(dtype, [str], "dtype")
     core_utils.type_check(out_path, [list, str, None], "out_path")
     core_utils.type_check(overwrite, [bool], "overwrite")
     core_utils.type_check(allow_lists, [bool], "allow_lists")
     core_utils.type_check(creation_options, [list, None], "creation_options")
@@ -810,15 +979,15 @@
     ## Kwargs
     `out_path` (_str_/_None_): The destination to save to. (Default: **None**)</br>
     `overwrite` (_bool_): If the file exists, should it be overwritten? (Default: **True**) </br>
     `dtype` (_str_): The data type of the output raster. (Default: **None**)</br>
     `creation_options` (_list_): List of **GDAL** creation options. Defaults are: </br>
     &emsp; • "TILED=YES" </br>
     &emsp; • "NUM_THREADS=ALL_CPUS" </br>
-    &emsp; • "BIGG_TIF=YES" </br>
+    &emsp; • "BIG_TIFF=YES" </br>
     &emsp; • "COMPRESS=LZW" </br>
 
     ## Returns:
     (_str_/_list_): The filepath(s) to the newly created raster(s).
     """
     core_utils.type_check(rasters, [[str, gdal.Dataset]], "rasters")
     core_utils.type_check(out_path, [str, None], "out_path")
@@ -1066,15 +1235,24 @@
         return 0.0
 
     overlap = intersection.GetArea() / meta1.GetArea()
 
     return overlap
 
 
-def create_raster_from_array(arr, out_path=None, pixel_size=10.0, x_min=0.0, y_max=0.0, projection="EPSG:3857", creation_options=None, overwrite=True):
+def create_raster_from_array(
+    arr,
+    out_path=None,
+    pixel_size=10.0,
+    x_min=0.0,
+    y_max=0.0,
+    projection="EPSG:3857",
+    creation_options=None,
+    overwrite=True,
+):
     """ Create a raster from a numpy array. """
     core_utils.type_check(arr, [np.ndarray, np.ma.MaskedArray], "arr")
     core_utils.type_check(out_path, [str, None], "out_path")
     core_utils.type_check(pixel_size, [int, float, [int, float]], "pixel_size")
     core_utils.type_check(x_min, [int, float], "x_min")
     core_utils.type_check(y_max, [int, float], "y_max")
     core_utils.type_check(projection, [int, str, gdal.Dataset, ogr.DataSource, osr.SpatialReference], "projection")
@@ -1163,36 +1341,7 @@
     x_vals = np.linspace(start_x + x_adj, stop_x - x_adj, size_x, dtype=np.float32)
     y_vals = np.linspace(start_y - y_adj, stop_y + y_adj, size_y, dtype=np.float32)
 
     xx, yy = np.meshgrid(x_vals, y_vals)
     grid = np.dstack((xx, yy))
 
     return grid
-
-
-def is_cog(raster):
-    """Check if a raster is a Cloud Optimized GeoTIFF. """
-    core_utils.type_check(raster, [str, gdal.Dataset], "raster")
-
-    raster = _open_raster(raster)
-
-    if not validate_cloud_optimized_geotiff.validate(raster):
-        return False
-
-    return True
-
-
-# def translate_to_cog(raster, out_path):
-#     """Translate a raster to a Cloud Optimized GeoTIFF. """
-#     core_utils.type_check(raster, [str, gdal.Dataset], "raster")
-#     core_utils.type_check(out_path, [str], "out_path")
-
-#     raster = _open_raster(raster)
-
-#     if not is_cog(out_path):
-#         driver = gdal.GetDriverByName("COG")
-#         out_ds = driver.CreateCopy(out_path, raster, options=["TILED=YES", "COMPRESS=DEFLATE", "COPY_SRC_OVERVIEWS=YES"])
-#         gdal.BuildOverviews(out_path, "NEAREST", overviewlist=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
-
-#         gdal.Translate(out_path, raster, creationOptions=["TILED=YES", "COMPRESS=DEFLATE", "COPY_SRC_OVERVIEWS=YES"])
-
-#     return out_path
```

### Comparing `buteo-0.8.8/buteo/raster/edge_detection.py` & `buteo-0.8.9/buteo/raster/edge_detection.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/grid.py` & `buteo-0.8.9/buteo/raster/grid.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/morphology.py` & `buteo-0.8.9/buteo/raster/morphology.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/nodata.py` & `buteo-0.8.9/buteo/raster/nodata.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/patches.py` & `buteo-0.8.9/buteo/raster/patches.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/proximity.py` & `buteo-0.8.9/buteo/raster/proximity.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/reproject.py` & `buteo-0.8.9/buteo/raster/reproject.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/resample.py` & `buteo-0.8.9/buteo/raster/resample.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/shift.py` & `buteo-0.8.9/buteo/raster/shift.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/textures.py` & `buteo-0.8.9/buteo/raster/textures.py`

 * *Files 0% similar despite different names*

```diff
@@ -182,15 +182,15 @@
     type_check(nodata, [bool], "nodata")
     type_check(nodata_value, [int, float], "nodata_value")
     type_check(distance_weight, [str], "distance_weight")
     type_check(distance_decay, [int, float], "distance_decay")
     type_check(distance_sigma, [int, float], "distance_sigma")
 
     assert filter_size % 2 == 1, "Filter size must be odd."
-    
+
     _kernel, weights, offsets = get_kernel(
         filter_size,
         distance_weight=distance_weight,
         distance_decay=distance_decay,
         distance_sigma=distance_sigma,
         spherical=spherical,
     )
```

### Comparing `buteo-0.8.8/buteo/raster/timeseries.py` & `buteo-0.8.9/buteo/raster/timeseries.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/vectorize.py` & `buteo-0.8.9/buteo/raster/vectorize.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/raster/warp.py` & `buteo-0.8.9/buteo/raster/warp.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/utils/aux_utils.py` & `buteo-0.8.9/buteo/utils/aux_utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -217,16 +217,16 @@
             rows_grid[i, j] = range_cols[i]
 
     return rows_grid, cols_grid
 
 
 def split_into_offsets(shape, offsets_x=2, offsets_y=2, overlap_x=0, overlap_y=0):
     """ Split a shape into offsets. Usually used for splitting an image into offsets to reduce RAM needed. """
-    width = shape[0]
-    height = shape[1]
+    height = shape[0]
+    width = shape[1]
 
     x_remainder = width % offsets_x
     y_remainder = height % offsets_y
 
     x_offsets = [0]
     x_sizes = []
     for _ in range(offsets_x - 1):
```

### Comparing `buteo-0.8.8/buteo/utils/bbox_utils.py` & `buteo-0.8.9/buteo/utils/bbox_utils.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/utils/core_utils.py` & `buteo-0.8.9/buteo/utils/core_utils.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/utils/gdal_enums.py` & `buteo-0.8.9/buteo/utils/gdal_enums.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/utils/gdal_utils.py` & `buteo-0.8.9/buteo/utils/gdal_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -50,22 +50,41 @@
     if "TILED" not in opt_str:
         internal_options.append("TILED=YES")
 
     if "NUM_THREADS" not in opt_str:
         internal_options.append("NUM_THREADS=ALL_CPUS")
 
     if "BIGTIFF" not in opt_str:
-        internal_options.append("BIGTIFF=YES")
+        internal_options.append("BIGTIFF=IF_SAFER")
 
     if "COMPRESS" not in opt_str:
         internal_options.append("COMPRESS=LZW")
 
+    if "BLOCKXSIZE" not in opt_str:
+        internal_options.append("BLOCKXSIZE=256")
+
+    if "BLOCKYSIZE" not in opt_str:
+        internal_options.append("BLOCKYSIZE=256")
+
     return internal_options
 
 
+def get_default_projection():
+    """
+    Get the default projection for a new raster.
+
+    ## Returns:
+    (_str_): The default projection.
+    """
+    epsg_4326_wkt = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]'
+
+    return epsg_4326_wkt
+
+
+
 def is_valid_datatype(file_path):
     """
     Check if a file path has a valid GDAL or OGR driver.
 
     ## Args:
     `file_path` (_str_): The file path to check.
 
@@ -461,15 +480,15 @@
 
     if len(potential_path_list) == 0:
         return False
 
     for element in potential_path_list:
         if element is None and not allow_none:
             return False
-        
+
         if not core_utils.is_valid_output_path(element) and not os.path.isdir(element):
             return False
 
     return True
 
 def is_vector(potential_vector, empty_is_invalid=True):
     """
```

### Comparing `buteo-0.8.8/buteo/vector/buffer.py` & `buteo-0.8.9/buteo/vector/buffer.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/clip.py` & `buteo-0.8.9/buteo/vector/clip.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/convert_parts.py` & `buteo-0.8.9/buteo/vector/convert_parts.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/core_vector.py` & `buteo-0.8.9/buteo/vector/core_vector.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/dissolve.py` & `buteo-0.8.9/buteo/vector/dissolve.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/intersect.py` & `buteo-0.8.9/buteo/vector/intersect.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/merge.py` & `buteo-0.8.9/buteo/vector/merge.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/rasterize.py` & `buteo-0.8.9/buteo/vector/rasterize.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/reproject.py` & `buteo-0.8.9/buteo/vector/reproject.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/buteo/vector/zonal_statistics.py` & `buteo-0.8.9/buteo/vector/zonal_statistics.py`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/pyproject.toml` & `buteo-0.8.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["flit_core>=3.7.1", "numba>=0.56.2", "psutil>=5.4.8", "PyYAML>=6.0"]
 build-backend = "flit_core.buildapi"
 
 [project]
 name = "buteo"
-version = "0.8.8"
+version = "0.8.9"
 authors = [
   { name="Casper Fibaek", email="casperfibaek@gmail.com" },
 ]
 description = "Geospatial tools for raster preprocessing and EO work."
 readme = "readme.md"
 license = { file="LICENSE" }
 requires-python = ">=3.7"
```

### Comparing `buteo-0.8.8/readme.md` & `buteo-0.8.9/readme.md`

 * *Files identical despite different names*

### Comparing `buteo-0.8.8/PKG-INFO` & `buteo-0.8.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: buteo
-Version: 0.8.8
+Version: 0.8.9
 Summary: Geospatial tools for raster preprocessing and EO work.
 Author-email: Casper Fibaek <casperfibaek@gmail.com>
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

