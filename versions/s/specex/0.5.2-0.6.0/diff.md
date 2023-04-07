# Comparing `tmp/specex-0.5.2.tar.gz` & `tmp/specex-0.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "specex-0.5.2.tar", last modified: Mon Dec 19 11:57:52 2022, max compression
+gzip compressed data, was "specex-0.6.0.tar", last modified: Fri Apr  7 11:00:50 2023, max compression
```

## Comparing `specex-0.5.2.tar` & `specex-0.6.0.tar`

### file list

```diff
@@ -1,33 +1,33 @@
-drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2022-12-19 11:57:52.896747 specex-0.5.2/
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1525 2022-04-01 11:26:21.000000 specex-0.5.2/LICENSE
--rw-r--r--   0 daddona   (1000) daddona   (1000)     3919 2022-12-19 11:57:52.896747 specex-0.5.2/PKG-INFO
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1407 2022-12-16 07:04:36.000000 specex-0.5.2/README.md
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1590 2022-12-19 09:35:46.000000 specex-0.5.2/pyproject.toml
--rw-r--r--   0 daddona   (1000) daddona   (1000)       38 2022-12-19 11:57:52.896747 specex-0.5.2/setup.cfg
-drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2022-12-19 11:57:52.893414 specex-0.5.2/src/
-drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2022-12-19 11:57:52.896747 specex-0.5.2/src/specex/
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1920 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/__init__.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    39156 2022-12-15 19:50:51.000000 specex-0.5.2/src/specex/cube.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)     5175 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/lines.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    12951 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/plot.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    20267 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/rrspecex.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    24593 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/sources.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    42650 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/specex.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)     7542 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/stack.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)    38051 2022-12-19 11:41:40.000000 specex-0.5.2/src/specex/utils.py
--rwxr-xr-x   0 daddona   (1000) daddona   (1000)     4550 2022-12-15 19:17:38.000000 specex-0.5.2/src/specex/zeropoints.py
-drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2022-12-19 11:57:52.896747 specex-0.5.2/src/specex.egg-info/
--rw-r--r--   0 daddona   (1000) daddona   (1000)     3919 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/PKG-INFO
--rw-r--r--   0 daddona   (1000) daddona   (1000)      607 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/SOURCES.txt
--rw-r--r--   0 daddona   (1000) daddona   (1000)        1 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/dependency_links.txt
--rw-r--r--   0 daddona   (1000) daddona   (1000)      244 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/entry_points.txt
--rw-r--r--   0 daddona   (1000) daddona   (1000)       46 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/requires.txt
--rw-r--r--   0 daddona   (1000) daddona   (1000)        7 2022-12-19 11:57:52.000000 specex-0.5.2/src/specex.egg-info/top_level.txt
-drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2022-12-19 11:57:52.896747 specex-0.5.2/test/
--rw-r--r--   0 daddona   (1000) daddona   (1000)      652 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_cubestack.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1970 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_cutout.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1524 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_rrspecex.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)      583 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_sources.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)     1133 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_specex.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)      706 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_specexplot.py
--rw-r--r--   0 daddona   (1000) daddona   (1000)      756 2022-12-15 19:17:38.000000 specex-0.5.2/test/test_zeropointinfo.py
+drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2023-04-07 11:00:50.568760 specex-0.6.0/
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1525 2022-04-01 11:26:21.000000 specex-0.6.0/LICENSE
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     3919 2023-04-07 11:00:50.568760 specex-0.6.0/PKG-INFO
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1407 2022-12-16 07:04:36.000000 specex-0.6.0/README.md
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1635 2023-02-12 09:24:28.000000 specex-0.6.0/pyproject.toml
+-rw-r--r--   0 daddona   (1000) daddona   (1000)       38 2023-04-07 11:00:50.568760 specex-0.6.0/setup.cfg
+drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2023-04-07 11:00:50.565426 specex-0.6.0/src/
+drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2023-04-07 11:00:50.565426 specex-0.6.0/src/specex/
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1918 2023-03-06 07:50:03.000000 specex-0.6.0/src/specex/__init__.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    53480 2023-02-13 13:15:40.000000 specex-0.6.0/src/specex/cube.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     5175 2022-12-15 19:17:38.000000 specex-0.6.0/src/specex/lines.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    12965 2023-02-21 15:30:58.000000 specex-0.6.0/src/specex/plot.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    20267 2022-12-15 19:17:38.000000 specex-0.6.0/src/specex/rrspecex.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    24593 2022-12-15 19:17:38.000000 specex-0.6.0/src/specex/sources.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    42648 2023-03-06 07:49:53.000000 specex-0.6.0/src/specex/specex.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     8345 2023-02-14 07:35:23.000000 specex-0.6.0/src/specex/stack.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)    38123 2023-02-14 07:38:24.000000 specex-0.6.0/src/specex/utils.py
+-rwxr-xr-x   0 daddona   (1000) daddona   (1000)     4550 2022-12-15 19:17:38.000000 specex-0.6.0/src/specex/zeropoints.py
+drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2023-04-07 11:00:50.565426 specex-0.6.0/src/specex.egg-info/
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     3919 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/PKG-INFO
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      607 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/SOURCES.txt
+-rw-r--r--   0 daddona   (1000) daddona   (1000)        1 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/dependency_links.txt
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      287 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/entry_points.txt
+-rw-r--r--   0 daddona   (1000) daddona   (1000)       46 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/requires.txt
+-rw-r--r--   0 daddona   (1000) daddona   (1000)        7 2023-04-07 11:00:50.000000 specex-0.6.0/src/specex.egg-info/top_level.txt
+drwxr-xr-x   0 daddona   (1000) daddona   (1000)        0 2023-04-07 11:00:50.568760 specex-0.6.0/test/
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      652 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_cubestack.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1970 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_cutout.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1524 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_rrspecex.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      583 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_sources.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)     1133 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_specex.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      706 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_specexplot.py
+-rw-r--r--   0 daddona   (1000) daddona   (1000)      756 2022-12-15 19:17:38.000000 specex-0.6.0/test/test_zeropointinfo.py
```

### Comparing `specex-0.5.2/LICENSE` & `specex-0.6.0/LICENSE`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/PKG-INFO` & `specex-0.6.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: specex
-Version: 0.5.2
+Version: 0.6.0
 Summary: Extract spectra from fits cubes
 Author: Maurizio D'Addona
 Author-email: mauritiusdadd@gmail.com
 Maintainer: Maurizio D'Addona
 Maintainer-email: mauritiusdadd@gmail.com
 License: BSD 3-Clause License
```

### Comparing `specex-0.5.2/README.md` & `specex-0.6.0/README.md`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/pyproject.toml` & `specex-0.6.0/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "specex"
-version = "0.5.2"
+version = "0.6.0"
 description = "Extract spectra from fits cubes"
 readme = "README.md"
 requires-python = ">=3.7"
 license = {file = "LICENSE"}
 keywords = ["spectroscopy", "spectra", "spectrum", "spectral cubes"]
 authors = [
  {name = "Maurizio D'Addona"},
@@ -50,8 +50,9 @@
 
 [project.scripts]
 specex = "specex.specex:specex"
 rrspecex = "specex.rrspecex:rrspecex"
 specex-zeropointinfo = "specex.zeropoints:main"
 specex-cubestack = "specex.stack:cube_stack"
 specex-cutout = "specex.cube:cutout_main"
+specex-smooth = "specex.cube:smoothing_main"
 specex-plot = "specex.plot:plot"
```

### Comparing `specex-0.5.2/src/specex/__init__.py` & `specex-0.6.0/src/specex/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -35,14 +35,14 @@
 from pkgutil import extend_path
 
 from . import specex
 from . import utils
 from . import plot
 try:
     from . import rrspecex
-except ImportError:
+except Exception:
     HAS_RR = False
 else:
     HAS_RR = True
 
 __version__ = importlib.metadata.version("specex")
 __path__ = extend_path(__path__, __name__)
```

### Comparing `specex-0.5.2/src/specex/cube.py` & `specex-0.6.0/src/specex/cube.py`

 * *Files 19% similar despite different names*

```diff
@@ -5,31 +5,39 @@
 import re
 import sys
 import argparse
 import warnings
 from typing import Optional, Union, Callable
 
 import numpy as np
+from scipy.ndimage import gaussian_filter, gaussian_filter1d, zoom
 
 from astropy import units
 from astropy.io import fits
 from astropy.wcs import WCS
 from astropy.wcs.utils import wcs_to_celestial_frame
 from astropy.table import Table
 from astropy.coordinates import SkyCoord
 from astropy.nddata.utils import Cutout2D
 
 from .utils import get_pc_transform_params, rotate_data, get_pbar
 
+
 KNOWN_SPEC_EXT_NAMES = ['spec', 'spectrum', 'flux', 'data', 'sci', 'science']
 KNOWN_VARIANCE_EXT_NAMES = ['stat', 'stats', 'var', 'variance', 'noise', 'err']
 KNOWN_MASK_EXT_NAMES = ['mask', 'platemask', 'footprint', 'dq']
 KNOWN_RGB_EXT_NAMES = ['r', 'g', 'b', 'red', 'green', 'blue']
 
 
+def __simple_report_callback(k, total):
+    pbar = get_pbar(k / total)
+    sys.stderr.write(f"\r{pbar} {k} / {total} \r")
+    sys.stderr.flush()
+
+
 def __cutout_argshandler(options=None):
     """
     Parse the arguments given by the user.
 
     Inputs
     ------
     options: list or None
@@ -122,14 +130,121 @@
     elif not os.path.isfile(args.regionfile):
         print("The file input regionfile does not exist!")
         sys.exit(1)
 
     return args
 
 
+def __smoothing_argshandler(options=None):
+    """
+    Parse the arguments given by the user.
+
+    Inputs
+    ------
+    options: list or None
+        If none, args are parsed from the command line, otherwise the options
+        list is used as input for argument parser.
+
+    Returns
+    -------
+    args: Namespace
+        A Namespace containing the parsed arguments. For more information see
+        the python documentation of the argparse module.
+    """
+    parser = argparse.ArgumentParser(
+        description='Apply a gaussian smoothing kernel to a spectral cubes '
+                    'spatially and/or along the spectral axis.'
+    )
+
+    parser.add_argument(
+        'input_fits_files', metavar='INPUT_FIST', type=str, nargs='+',
+        help='The spectral cube (or image) from which to extract a cutout.'
+    )
+    parser.add_argument(
+        '--spatial-sigma', metavar='SIGMA', type=float, default=1.0,
+        help='Set the sigma for the spatial gaussian kernel. If %(metavar)s '
+        'is 0 then no spatial smoothing is applied. If not specified the '
+        'default value %(metavar)s=%(default)f is used.'
+    )
+    parser.add_argument(
+        '--spatial-supersample', metavar='ZOOM_FACTOR', type=int, default=0,
+        help='Set the spatial supersampling factor. If %(metavar)s <= 1 then '
+        'no supersampling is applied. %(metavar)s=2 means that the output cube'
+        ' will have a doubled width and height, and so on. The default value '
+        'is %(metavar)s=%(default)d.'
+    )
+    parser.add_argument(
+        '--wave-supersample', metavar='ZOOM_FACTOR', type=int, default=0,
+        help='Set the wavelength supersampling factor. If %(metavar)s <= 1 '
+        'then no supersampling is applied. %(metavar)s=2 means that the output'
+        'cube will have a doubled spectral resolution, and so on. '
+        'The default value is %(metavar)s=%(default)d.'
+    )
+    parser.add_argument(
+        '--wave-sigma', metavar='SIGMA', type=float, default=0,
+        help='Set the sigma for the spectral gaussian kernel. If %(metavar)s '
+        'is 0 then no spectral smoothing is applied. If not specified the '
+        'default value %(metavar)s=%(default)f is used.'
+    )
+    parser.add_argument(
+        '--info-hdu', metavar='INFO_HDU', type=int, default=0,
+        help='The HDU containing cube metadata. If this argument '
+        'Set this to -1 to automatically detect the HDU containing the info. '
+        'NOTE that this value is zero indexed (i.e. firts HDU has index 0).'
+    )
+
+    parser.add_argument(
+        '--spec-hdu', metavar='SPEC_HDU', type=int, default=-1,
+        help='The HDU containing the spectral data to use. If this argument '
+        'Set this to -1 to automatically detect the HDU containing spectra. '
+        'NOTE that this value is zero indexed (i.e. second HDU has index 1).'
+    )
+
+    parser.add_argument(
+        '--var-hdu', metavar='VAR_HDU', type=int, default=-1,
+        help='The HDU containing the variance of the spectral data. '
+        'Set this to -1 if no variance data is present in the cube. '
+        'The default value is %(metavar)s=%(default)s.'
+        'NOTE that this value is zero indexed (i.e. third HDU has index 2).'
+    )
+
+    parser.add_argument(
+        '--mask-hdu', metavar='MASK_HDU', type=int, default=-1,
+        help='The HDU containing the valid pixel mask of the spectral data. '
+        'Set this to -1 if no mask is present in the cube. '
+        'The default value is %(metavar)s=%(default)s.'
+        'NOTE that this value is zero indexed (i.e. fourth HDU has index 3).'
+    )
+
+    parser.add_argument(
+        '--verbose', action='store_true', default=False,
+        help="Print verbose outout."
+    )
+    args = None
+    if options is None:
+        args = parser.parse_args()
+    else:
+        args = parser.parse_args(options)
+
+    for inp_fits_file in args.input_fits_files:
+        if (inp_fits_file is not None) and (not os.path.isfile(inp_fits_file)):
+            print(f"The file {inp_fits_file} does not exist!")
+            sys.exit(1)
+
+    if (args.spatial_sigma == 0) and (args.wave_sigma == 0):
+        print(
+            "Spatial smoothing and spectral smooting cannot be both disabled, "
+            "please set at least one the options --wave-sigma or "
+            "--spatial-sigma."
+        )
+        sys.exit(1)
+
+    return args
+
+
 def parse_regionfile(regionfile: str, key_ra: str = 'RA', key_dec: str = 'DEC',
                      key_a: str = 'A_WORLD', key_b: str = 'B_WORLD',
                      key_theta: str = 'THETA_WORLD', key_wmin: str = 'WMIN',
                      key_wmax: str = 'WMAX'):
     """
     Parse a regionfile and return an asrtopy Table with sources information.
 
@@ -336,16 +451,15 @@
                    resample_to_wcs: bool = False):
     """
     Get a cutout from a bigger RGB.
 
     Parameters
     ----------
     data : np.ndarray or tuple or list
-        The actual image data. Should have only two dimensions (a grayscale
-        image has only X and Y corrdinates).
+        The actual image data.
     center : astropy.coordinate.SkyCoord or tuple.
         The center of the cutout. If a SkyCoord is provided then a WCS for the
         image data musto also be specified with the parameter data_wcs.
         If a tuple is provided, then the first two numbers of the tuple are
         interpreted as the X and Y coordinate of the cutout center: in this
         case, if no WCS is specified, the values are assumed to be in pixels,
         else if a WCS is provided then the values are assumed to be in degrees.
@@ -600,19 +714,19 @@
 
                 if ext.name.lower() in KNOWN_RGB_EXT_NAMES:
                     data_ext = ext
                     data_structure['data-ext'].append(k)
 
             # If cannot determine which extensions cointain data,
             # then just use the second extension
-            if data_structure['data-ext'] is None:
+            if not data_structure['data-ext']:
                 data_ext = f[1]
                 data_structure['data-ext'] = [1, ]
 
-        data_shape = data_ext.shape
+        data_shape = data_ext.data.shape
         if len(data_shape) == 2:
             # A 2D image, we should check other extensions to
             # determine if its an RGB multi-extension file
             for k, ext in enumerate(f):
                 if k in data_structure['data-ext']:
                     continue
 
@@ -729,33 +843,314 @@
             if msg_index_error:
                 print(msg_index_error.format(hdu_index), file=sys.stderr)
             if exit_on_errors:
                 sys.exit(1)
     return valid_hdu
 
 
-def cutout_main(options=None):
+def cube_tiled_func(data, func, tile_size, *args, **kwargs):
+    data_shape = data.shape[-2:]
+    if isinstance(data, np.ma.MaskedArray):
+        result = np.ma.zeros(data_shape)
+    else:
+        result = np.zeros(data_shape)
+    for j in np.arange(data_shape[0], step=tile_size):
+        for k in np.arange(data_shape[1], step=tile_size):
+            tile = data[:, j:j+tile_size, k:k+tile_size]
+            # Skip empty tiles:
+            if not np.isfinite(tile).any():
+                result[j:j+tile_size, k:k+tile_size] = np.nan
+                try:
+                    result[j:j+tile_size, k:k+tile_size].mask = True
+                except AttributeError:
+                    pass
+                continue
+
+            processed_tile = func(tile, *args, **kwargs).copy()
+            result[j:j+tile_size, k:k+tile_size] = processed_tile
+            try:
+                result[j:j+tile_size, k:k+tile_size].mask = processed_tile.mask
+            except AttributeError:
+                pass
+
+    return result
+
+
+def correlate_spaxel(cube_data: np.ndarray,
+                     spaxel_data: np.ndarray,
+                     similarity_function: Optional[str] = 'rms'):
+
+    if spaxel_data.shape[0] != cube_data.shape[0]:
+        raise ValueError(
+            "spaxel_data and cube_data must have the same first dimension."
+        )
+
+    if len(spaxel_data.shape) == 1:
+        spaxel_data = spaxel_data[:, None, None]
+
+    x = cube_data - np.nanmedian(cube_data, axis=0)
+    x = x / np.nanmax(x, axis=0)
+    y = spaxel_data - np.nanmedian(spaxel_data)
+    y = y / np.nanmax(y)
+
+    if similarity_function == 'rms':
+        res = np.sqrt(np.nanmean((x - y)**2, axis=0))
+        return 1/(1 + res)
+    elif similarity_function == 'correlation':
+        res = np.nansum(x * y, axis=0)
+        return res / (np.nansum(x**2, axis=0) * np.nansum(y**2))
+
+
+def self_correlate(data: np.ndarray,
+                   data_mask: Optional[np.ndarray] = None,
+                   similarity_sigma_threshold: Optional[float] = 5,
+                   tile_size: Optional[int] = 32,
+                   block_size: Optional[int] = 2,
+                   similarity_function: Optional[str] = 'rms',
+                   report_callback: Optional[Callable] = None) -> np.ndarray:
+    if data_mask is not None and data.shape != data_mask.shape:
+            raise ValueError("data and data_mask must have the same shape!")
+
+    hei, wid = data.shape[1:]
+
+    sim_table = np.zeros((hei, wid))
+    # Dor each spaxel in the cube
+    block_id = 0
+    for h in np.arange(hei, step=block_size):
+        for k in np.arange(wid, step=block_size):
+            block_id += 1
+            if (
+                (sim_table[h:h+block_size, k:k+block_size] != 0).any() or
+                (
+                    data_mask is not None and
+                    (data_mask[:, h:h+block_size, k:k+block_size] != 0).any()
+                )
+            ):
+                continue
+
+            if report_callback is not None:
+                report_callback(block_id + 1, int(wid*hei / (block_size**2)))
+
+            spaxel_data = np.nansum(
+                data[:, h:h+block_size, k:k+block_size],
+                axis=(1, 2)
+            )
+
+            if not np.isfinite(spaxel_data).any():
+                continue
+
+            similarity_map = cube_tiled_func(
+                data,
+                correlate_spaxel,
+                tile_size=tile_size,
+                spaxel_data=spaxel_data,
+                similarity_function=similarity_function
+            )
+
+            thresh = np.nanmean(similarity_map)
+            thresh += similarity_sigma_threshold * np.nanstd(similarity_map)
+            similarity_mask = similarity_map >= thresh
+            sim_table[similarity_mask] = block_id
+    return sim_table
+
+
+def smooth_cube(data: np.ndarray, data_mask: Optional[np.ndarray] = None,
+                spatial_sigma: Optional[float] = 1.0,
+                wave_sigma: Optional[float] = 0.0,
+                report_callback: Optional[Callable] = None) -> np.ndarray:
     """
-    Run the main program.
+    Smooth a datacube spatially and/or along the spectral axis.
+
+    Parameters
+    ----------
+    data : numpy.ndarray
+        The spectral datacube.
+    data_mask : numpy.ndarray, optional
+        The mask for the spectral datacube. The default is None.
+    spatial_sigma : float, optional
+        The sigma for the spatial smoothing gaussian kernel.
+        The default is 1.0.
+    wave_sigma : float, optional
+        The sigma fot the spectral smoothing gaussian kernel.
+        The default is 0.0.
+    report_callback : Callable or None, optional
+        A callable that will be execute every time the cutout of a single
+        slice of the cube is computed. Must accept in input two arguments:
+            - the number of slice processed so far
+            - the total number of slices.
+
+    Raises
+    ------
+    ValueError
+        If the shape of data does not match the shape of data_mask.
+
+    Returns
+    -------
+    smoothed_arr : numpy.ndarray
+        The smoothed version of the input data.
+
+    """
+    if data_mask is not None and data.shape != data_mask.shape:
+            raise ValueError("data and data_mask must have the same shape!")
+
+    smoothed_arr = data.copy()
+
+    if wave_sigma > 0:
+        for h in range(smoothed_arr.shape[1]):
+            if report_callback is not None:
+                report_callback(h, smoothed_arr.shape[1])
+            for k in range(smoothed_arr.shape[2]):
+                smoothed_spaxel = gaussian_filter1d(
+                    smoothed_arr[:, h, k],
+                    sigma=wave_sigma,
+                    mode='constant'
+                )
+                smoothed_arr[:, h, k] = smoothed_spaxel
+
+    if report_callback is not None:
+        print("")
+
+    if spatial_sigma > 0:
+        for k, data_slice in enumerate(smoothed_arr):
+            if report_callback is not None:
+                report_callback(k + 1, smoothed_arr.shape[0])
+            smoothed_slice = gaussian_filter(
+                data_slice,
+                sigma=spatial_sigma,
+                mode='constant'
+            )
+            smoothed_arr[k] = smoothed_slice
+
+    if report_callback is not None:
+        print("")
+
+    if data_mask is not None:
+        smoothed_mask = data_mask.copy().astype(bool)
+        for k, mask_slice in enumerate(smoothed_mask):
+            if report_callback is not None:
+                report_callback(k + 1, smoothed_mask.shape[0])
+                smoothed_mask[k] &= ~np.isfinite(smoothed_arr[k])
+        if report_callback is not None:
+            print("")
+        smoothed_mask = smoothed_mask.astype('int8')
+
+    return smoothed_arr, smoothed_mask
+
+
+def smoothing_main(options=None):
+    """
+    Run the main cutout program.
 
     Parameters
     ----------
     options : list or None, optional
         A list of cli input prameters. The default is None.
 
     Returns
     -------
     None.
 
     """
-    def simple_report_callback(k, total):
-        pbar = get_pbar(k / total)
-        sys.stderr.write(f"\r{pbar} {k} / {total} \r")
-        sys.stderr.flush()
+    args = __smoothing_argshandler(options)
+
+    if args.verbose:
+        report_callback = __simple_report_callback
+    else:
+        report_callback = None
+
+    for target_data_file in args.input_fits_files:
+        fits_base_name = os.path.basename(target_data_file)
+        fits_base_name = os.path.splitext(fits_base_name)[0]
+        if args.verbose:
+            print(f"\n[{fits_base_name}]")
+
+        with fits.open(target_data_file, mode='readonly') as hdul:
+                spec_hdu = get_hdu(
+                    hdul,
+                    hdu_index=args.spec_hdu,
+                    valid_names=KNOWN_SPEC_EXT_NAMES,
+                    msg_err_notfound=(
+                        "ERROR: Cannot determine which HDU contains spectral "
+                        "data, try to specify it manually!"
+                    ),
+                    msg_index_error="ERROR: Cannot open HDU {} to read specra!"
+                )
+
+                spec_wcs = WCS(spec_hdu.header)
 
+                var_hdu = get_hdu(
+                    hdul,
+                    hdu_index=args.var_hdu,
+                    valid_names=KNOWN_VARIANCE_EXT_NAMES,
+                    msg_err_notfound=(
+                        "WARNING: Cannot determine which HDU contains the "
+                        "variance data, try to specify it manually!"
+                    ),
+                    msg_index_error="WARNING: Cannot open HDU {} to read the "
+                                    "variance!",
+                    exit_on_errors=False
+                )
+
+                mask_hdu = get_hdu(
+                    hdul,
+                    hdu_index=args.mask_hdu,
+                    valid_names=KNOWN_MASK_EXT_NAMES,
+                    msg_err_notfound=(
+                        "WARNING: Cannot determine which HDU contains the "
+                        "mask data, try to specify it manually!"
+                    ),
+                    msg_index_error="WARNING: Cannot open HDU {} to read the "
+                                    "mask!",
+                    exit_on_errors=False
+                )
+
+                if mask_hdu is not None:
+                    data_mask = mask_hdu.data
+
+                if args.verbose:
+                    print(">>> applying smoothing...")
+                    print(f"  - spatial_sigma: {args.spatial_sigma}")
+                    print(f"  - wave_sigma: {args.wave_sigma}")
+
+                smoothed_spec, smoothed_mask = smooth_cube(
+                    data=spec_hdu.data,
+                    data_mask=data_mask,
+                    spatial_sigma=args.spatial_sigma,
+                    wave_sigma=args.wave_sigma,
+                    report_callback=report_callback
+                )
+
+                spec_hdu.data = smoothed_spec
+                if mask_hdu is not None:
+                    mask_hdu.data = smoothed_mask
+
+                out_fname = f"{fits_base_name}_smoothed.fits"
+                if args.verbose:
+                    print("  - saving to {out_fname}...")
+
+                hdul.writeto(
+                    out_fname,
+                    overwrite=True
+                )
+
+
+def cutout_main(options=None):
+    """
+    Run the main cutout program.
+
+    Parameters
+    ----------
+    options : list or None, optional
+        A list of cli input prameters. The default is None.
+
+    Returns
+    -------
+    None.
+
+    """
     def updated_wcs_cutout_header(orig_header, cutout_header):
         new_header = orig_header.copy()
 
         sys.stdout.flush()
         sys.stderr.flush()
 
         # Delete any existing CD card
@@ -828,15 +1223,15 @@
             f" Name: {fits_base_name}\n"
             f" Type: {data_structure['type']}\n"
             f" Data EXT: {data_structure['data-ext']}\n"
             f" Var EXT: {data_structure['variance-ext']}\n"
             f" DQ EXT: {data_structure['mask-ext']}\n",
             file=sys.stderr
         )
-        report_callback = simple_report_callback
+        report_callback = __simple_report_callback
     else:
         report_callback = None
 
     with fits.open(target_data_file) as hdul:
         for j, cutout_info in enumerate(myt):
             cutout_name = f"cutout_{fits_base_name}_{j:04}.fits"
             cc_ra = cutout_info['RA'] * units.deg
@@ -1038,11 +1433,7 @@
                 ])
                 cutout_hdul.writeto(cutout_name, overwrite=True)
             else:
                 print(
                     f"WARNING: not implemente yet [{data_structure['type']}]!",
                     file=sys.stderr
                 )
-
-
-if __name__ == '__main__':
-    cutout_main()
```

### Comparing `specex-0.5.2/src/specex/lines.py` & `specex-0.6.0/src/specex/lines.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/src/specex/plot.py` & `specex-0.6.0/src/specex/plot.py`

 * *Files 0% similar despite different names*

```diff
@@ -286,15 +286,15 @@
                     object_z = float(info_dict['Z'])
                     restframe = args.restframe
                 else:
                     object_z = None
                     restframe = False
 
             flux_data = spec_hdu.data
-            spec_wcs = wcs.WCS(spec_hdu.header)
+            spec_wcs = wcs.WCS(spec_hdu.header, fobj=hdulist)
             var_data = var_hdu.data
 
             if nan_mask_hdu is not None:
                 nan_mask = nan_mask_hdu.data == 1
             else:
                 nan_mask = None
```

### Comparing `specex-0.5.2/src/specex/rrspecex.py` & `specex-0.6.0/src/specex/rrspecex.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/src/specex/sources.py` & `specex-0.6.0/src/specex/sources.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/src/specex/specex.py` & `specex-0.6.0/src/specex/specex.py`

 * *Files 0% similar despite different names*

```diff
@@ -34,15 +34,15 @@
 from .cube import KNOWN_SPEC_EXT_NAMES
 from .cube import KNOWN_VARIANCE_EXT_NAMES
 from .cube import KNOWN_MASK_EXT_NAMES
 from .cube import get_hdu
 
 try:
     from .rrspecex import rrspecex, get_templates
-except ImportError:
+except Exception:
     HAS_RR = False
 else:
     HAS_RR = True
 
 
 def __argshandler(options=None):
     """
```

### Comparing `specex-0.5.2/src/specex/stack.py` & `specex-0.6.0/src/specex/stack.py`

 * *Files 14% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 import matplotlib.pyplot as plt
 
 from .utils import stack
 from .cube import get_hdu
 
 
 def stack_and_plot(ext, basename, suffix="", is_mask=False, override_wcs=None,
-                   dpi=150, wave_range=None):
+                   dpi=150, wave_ranges=None):
     """
     Stack and plot a spectral datacube.
 
     Stack a datacube along the spectral axis and plot the result as a
     PNG and a FITS file.
 
     Parameters
@@ -57,20 +57,23 @@
 
     """
     if ext.data is None:
         return None
 
     img_wcs = WCS(ext.header)
 
-    wave_mask = None
-    if wave_range is not None and img_wcs.has_spectral:
-        wave_index = np.aragne(ext.data.shape[0])
-        wave_angstrom = img_wcs.spectral.pixel_to_world(wave_index).Angstrom
-        wave_mask = wave_angstrom >= np.nanmax(wave_range)
-        wave_mask &= wave_angstrom <= np.nanmin(wave_range)
+    wave_mask = np.zeros(ext.data.shape[0], dtype=bool)
+    if wave_ranges and img_wcs.has_spectral:
+        for wave_range in wave_ranges:
+            wave_index = np.arange(ext.data.shape[0])
+            wave_angstrom = img_wcs.spectral.pixel_to_world(wave_index)
+            wave_angstrom = wave_angstrom.Angstrom
+            mask = wave_angstrom >= np.nanmin(wave_range)
+            mask &= wave_angstrom <= np.nanmax(wave_range)
+            wave_mask |= mask
 
     img_height, img_width = ext.data.shape[1], ext.data.shape[2]
     img_figsize = (
         img_width / dpi,
         img_height / dpi
     )
 
@@ -148,14 +151,21 @@
     parser.add_argument(
         '--outdir', metavar='DIR', type=str, default=None,
         help='Set the directory where extracted spectra will be outputed. '
         'If this parameter is not specified, then a new directory will be '
         'created based on the name of the input cube.'
     )
 
+    parser.add_argument(
+        '--wave-ranges', metavar='WAVE_RANGE', type=str, default=None,
+        help='Set the wavelength range(s) to stack, in the format '
+        'WAVE_RANGE=RANGE1_START-RANGE1_STOP,RANGE2_START-RANGE2_STOP,...'
+        ' If not specified, the whole wavelength range is used.'
+    )
+
     args = None
     if options is None:
         args = parser.parse_args()
     else:
         args = parser.parse_args(options)
 
     return args
@@ -208,36 +218,47 @@
             valid_names=['mask', 'platemask', 'footprint', 'dq'],
             msg_err_notfound="WARNING: Cannot determine which HDU contains "
                              "the mask data, try to specify it manually!",
             msg_index_error="ERROR: Cannot open HDU {} to read the mask!",
             exit_on_errors=False
         )
 
+        if args.wave_ranges is not None:
+            wave_ranges = [
+                [float(k) for k in x.split('-')]
+                for x in args.wave_ranges.split(',')
+            ]
+        else:
+            wave_ranges = None
+
         dat, dat_wcs = stack_and_plot(
             spec_hdu,
             basename,
             'data',
+            wave_ranges=wave_ranges,
             dpi=args.dpi
         )
 
         if args.var_hdu >= 0:
             var, var_wcs = stack_and_plot(
                 var_hdu,
                 basename,
                 'variance',
                 override_wcs=dat_wcs,
+                wave_ranges=wave_ranges,
                 dpi=args.dpi
             )
 
         if args.mask_hdu >= 0:
             mask, mask_wcs = stack_and_plot(
                 mask_hdu,
                 basename,
                 'mask',
                 is_mask=True,
                 override_wcs=dat_wcs,
+                wave_ranges=wave_ranges,
                 dpi=args.dpi
             )
 
 
 if __name__ == '__main__':
     cube_stack()
```

### Comparing `specex-0.5.2/src/specex/utils.py` & `specex-0.6.0/src/specex/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -591,35 +591,36 @@
 
     # If variance data are present, then make two plots on the left of the
     # figure. The top one is for the spectrum and the bottom one is for the
     # variance. Otherwise just make a bigger plot on the left only for the
     # spectrum.
     if variance is not None:
         ax0 = fig.add_subplot(gs[:4, :-1])
-        ax4 = fig.add_subplot(gs[4:, :-1], sharex=ax0)
+        ax3 = fig.add_subplot(gs[4:, :-1], sharex=ax0)
 
-        ax4.plot(
+        ax3.plot(
             wavelengths, variance,
             ls='-',
             lw=0.5,
             alpha=0.75,
             color='black',
             label='variance',
             zorder=0
         )
-        ax4.set_xlabel(x_label)
-        ax4.set_ylabel('Variance')
+        ax3.set_xlabel(x_label)
+        ax3.set_ylabel('Variance')
 
-        ax4.set_xlim(w_min, w_max)
-        ax4.set_ylim(1, var_max)
-        ax4.set_yscale('log')
+        ax3.set_xlim(w_min, w_max)
+        ax3.set_ylim(1, var_max)
+        ax3.set_yscale('log')
         ax0.label_outer()
     else:
         ax0 = fig.add_subplot(gs[:, :-1])
         ax0.set_xlabel(x_label)
+        ax3 = None
 
     ax0.set_ylabel(y_label)
     ax0.set_xlim(w_min, w_max)
 
     # Plot a cutout
     if cutout is not None:
         ax1 = fig.add_subplot(gs[:3, -1], projection=cutout_wcs)
@@ -846,22 +847,23 @@
     )
 
     cell_text = [
         [f'{key}', f"{val}"] for key, val in extra_info.items()
     ]
 
     ax2.axis("off")
-    tbl = ax2.table(
-        cellText=cell_text,
-        colWidths=[0.4, 0.6],
-        loc='upper center'
-    )
-    tbl.scale(1, 1.5)
+    if cell_text:
+        tbl = ax2.table(
+            cellText=cell_text,
+            colWidths=[0.4, 0.6],
+            loc='upper center'
+        )
+        tbl.scale(1, 1.5)
 
-    return fig, [ax0, ax1, ax2]
+    return fig, [ax0, ax1, ax2, ax3]
 
 
 def plot_zfit_check(target, zbest, plot_template=None, restframe=True,
                     wavelengt_units='Angstrom', flux_units=''):
     """
     Plot the check images for the fitted targets.
 
@@ -1015,15 +1017,15 @@
     new_data = np.zeros((img_height, img_width))
     for k, dat in enumerate(data):
         progress = (k + 1) / len(data)
         sys.stderr.write(
             f"\rstacking cube: {get_pbar(progress)} {progress:.2%}\r"
         )
         sys.stderr.flush()
-        if wave_mask is None or wave_mask[k]:
+        if wave_mask is None or wave_mask[k].any():
             new_data = np.nansum(np.array([new_data, dat]), axis=0)
     print("", file=sys.stderr)
     return new_data
 
 
 def nannmad(x, scale=1.48206, axis=None):
     """
```

### Comparing `specex-0.5.2/src/specex/zeropoints.py` & `specex-0.6.0/src/specex/zeropoints.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/src/specex.egg-info/PKG-INFO` & `specex-0.6.0/src/specex.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: specex
-Version: 0.5.2
+Version: 0.6.0
 Summary: Extract spectra from fits cubes
 Author: Maurizio D'Addona
 Author-email: mauritiusdadd@gmail.com
 Maintainer: Maurizio D'Addona
 Maintainer-email: mauritiusdadd@gmail.com
 License: BSD 3-Clause License
```

### Comparing `specex-0.5.2/src/specex.egg-info/SOURCES.txt` & `specex-0.6.0/src/specex.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_cubestack.py` & `specex-0.6.0/test/test_cubestack.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_cutout.py` & `specex-0.6.0/test/test_cutout.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_rrspecex.py` & `specex-0.6.0/test/test_rrspecex.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_sources.py` & `specex-0.6.0/test/test_sources.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_specex.py` & `specex-0.6.0/test/test_specex.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_specexplot.py` & `specex-0.6.0/test/test_specexplot.py`

 * *Files identical despite different names*

### Comparing `specex-0.5.2/test/test_zeropointinfo.py` & `specex-0.6.0/test/test_zeropointinfo.py`

 * *Files identical despite different names*

