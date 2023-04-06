# Comparing `tmp/pyplotbrookings-0.1.1.tar.gz` & `tmp/pyplotbrookings-0.1.2.tar.gz`

## Comparing `pyplotbrookings-0.1.1.tar` & `pyplotbrookings-0.1.2.tar`

### file list

```diff
@@ -1,52 +1,52 @@
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/.DS_Store
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/examples/.DS_Store
--rw-r--r--   0        0        0   544308 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/examples/Examples.ipynb
--rw-r--r--   0        0        0   556797 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/examples/.ipynb_checkpoints/Examples-checkpoint.ipynb
--rw-r--r--   0        0        0    50649 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/figures/Figure1A.png
--rw-r--r--   0        0        0   110676 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/figures/Figure2.png
--rw-r--r--   0        0        0    41346 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/figures/Figure3.png
--rw-r--r--   0        0        0    30774 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/figures/logo.png
--rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/.DS_Store
--rw-r--r--   0        0        0     8196 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/.DS_Store
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/__init__.py
--rw-r--r--   0        0        0    18369 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/pyplotbrookings.py
--rw-r--r--   0        0        0   931903 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/.ipynb_checkpoints/Examples-checkpoint.ipynb
--rw-r--r--   0        0        0    11560 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/LICENSE.txt
--rw-r--r--   0        0        0   168060 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Black.ttf
--rw-r--r--   0        0        0   174108 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-BlackItalic.ttf
--rw-r--r--   0        0        0   167336 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Bold.ttf
--rw-r--r--   0        0        0   171508 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-BoldItalic.ttf
--rw-r--r--   0        0        0   170504 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Italic.ttf
--rw-r--r--   0        0        0   167000 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Light.ttf
--rw-r--r--   0        0        0   173172 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-LightItalic.ttf
--rw-r--r--   0        0        0   168644 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Medium.ttf
--rw-r--r--   0        0        0   173416 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-MediumItalic.ttf
--rw-r--r--   0        0        0   168260 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Regular.ttf
--rw-r--r--   0        0        0   168488 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Thin.ttf
--rw-r--r--   0        0        0   172860 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-ThinItalic.ttf
--rw-r--r--   0        0        0     7706 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/b_logo.png
--rw-r--r--   0        0        0    21136 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/bc.png
--rw-r--r--   0        0        0    12097 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/bi.png
--rw-r--r--   0        0        0    17913 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/brookings.png
--rw-r--r--   0        0        0    18458 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cc.png
--rw-r--r--   0        0        0    20676 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/ccf.png
--rw-r--r--   0        0        0   101943 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/ceaps.png
--rw-r--r--   0        0        0    26494 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cepm.png
--rw-r--r--   0        0        0    56387 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/chp.png
--rw-r--r--   0        0        0   107876 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cmep.png
--rw-r--r--   0        0        0   107158 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/crm.png
--rw-r--r--   0        0        0    22586 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/csd.png
--rw-r--r--   0        0        0    93053 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cti.png
--rw-r--r--   0        0        0    20197 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cue.png
--rw-r--r--   0        0        0    96557 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cuse.png
--rw-r--r--   0        0        0    14692 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/es.png
--rw-r--r--   0        0        0    13597 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/fp.png
--rw-r--r--   0        0        0    21605 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/global.png
--rw-r--r--   0        0        0    16084 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/gs.png
--rw-r--r--   0        0        0    47345 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/hc.png
--rw-r--r--   0        0        0    20101 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/metro.png
--rw-r--r--   0        0        0     8222 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/src/pyplotbrookings/logos/thp.png
--rw-r--r--   0        0        0     1094 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/LICENSE
--rw-r--r--   0        0        0     4795 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/README.md
--rw-r--r--   0        0        0      548 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/pyproject.toml
--rw-r--r--   0        0        0     5274 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/.DS_Store
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/examples/.DS_Store
+-rw-r--r--   0        0        0   544308 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/examples/Examples.ipynb
+-rw-r--r--   0        0        0   556797 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/examples/.ipynb_checkpoints/Examples-checkpoint.ipynb
+-rw-r--r--   0        0        0    50649 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/figures/Figure1A.png
+-rw-r--r--   0        0        0   110676 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/figures/Figure2.png
+-rw-r--r--   0        0        0    41346 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/figures/Figure3.png
+-rw-r--r--   0        0        0    30774 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/figures/logo.png
+-rw-r--r--   0        0        0     6148 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/.DS_Store
+-rw-r--r--   0        0        0     8196 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/.DS_Store
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/__init__.py
+-rw-r--r--   0        0        0    18369 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/pyplotbrookings.py
+-rw-r--r--   0        0        0   931903 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/.ipynb_checkpoints/Examples-checkpoint.ipynb
+-rw-r--r--   0        0        0    11560 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/LICENSE.txt
+-rw-r--r--   0        0        0   168060 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Black.ttf
+-rw-r--r--   0        0        0   174108 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-BlackItalic.ttf
+-rw-r--r--   0        0        0   167336 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Bold.ttf
+-rw-r--r--   0        0        0   171508 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-BoldItalic.ttf
+-rw-r--r--   0        0        0   170504 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Italic.ttf
+-rw-r--r--   0        0        0   167000 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Light.ttf
+-rw-r--r--   0        0        0   173172 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-LightItalic.ttf
+-rw-r--r--   0        0        0   168644 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Medium.ttf
+-rw-r--r--   0        0        0   173416 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-MediumItalic.ttf
+-rw-r--r--   0        0        0   168260 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Regular.ttf
+-rw-r--r--   0        0        0   168488 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Thin.ttf
+-rw-r--r--   0        0        0   172860 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-ThinItalic.ttf
+-rw-r--r--   0        0        0     7706 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/b_logo.png
+-rw-r--r--   0        0        0    21136 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/bc.png
+-rw-r--r--   0        0        0    12097 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/bi.png
+-rw-r--r--   0        0        0    17913 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/brookings.png
+-rw-r--r--   0        0        0    18458 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cc.png
+-rw-r--r--   0        0        0    20676 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/ccf.png
+-rw-r--r--   0        0        0   101943 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/ceaps.png
+-rw-r--r--   0        0        0    26494 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cepm.png
+-rw-r--r--   0        0        0    56387 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/chp.png
+-rw-r--r--   0        0        0   107876 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cmep.png
+-rw-r--r--   0        0        0   107158 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/crm.png
+-rw-r--r--   0        0        0    22586 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/csd.png
+-rw-r--r--   0        0        0    93053 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cti.png
+-rw-r--r--   0        0        0    20197 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cue.png
+-rw-r--r--   0        0        0    96557 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cuse.png
+-rw-r--r--   0        0        0    14692 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/es.png
+-rw-r--r--   0        0        0    13597 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/fp.png
+-rw-r--r--   0        0        0    21605 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/global.png
+-rw-r--r--   0        0        0    16084 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/gs.png
+-rw-r--r--   0        0        0    47345 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/hc.png
+-rw-r--r--   0        0        0    20101 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/metro.png
+-rw-r--r--   0        0        0     8222 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/src/pyplotbrookings/logos/thp.png
+-rw-r--r--   0        0        0     1094 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/LICENSE
+-rw-r--r--   0        0        0     6323 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/README.md
+-rw-r--r--   0        0        0      548 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     6802 2020-02-02 00:00:00.000000 pyplotbrookings-0.1.2/PKG-INFO
```

### Comparing `pyplotbrookings-0.1.1/.DS_Store` & `pyplotbrookings-0.1.2/.DS_Store`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/examples/.DS_Store` & `pyplotbrookings-0.1.2/examples/.DS_Store`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/examples/Examples.ipynb` & `pyplotbrookings-0.1.2/examples/Examples.ipynb`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/examples/.ipynb_checkpoints/Examples-checkpoint.ipynb` & `pyplotbrookings-0.1.2/examples/.ipynb_checkpoints/Examples-checkpoint.ipynb`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/figures/Figure1A.png` & `pyplotbrookings-0.1.2/figures/Figure1A.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/figures/Figure2.png` & `pyplotbrookings-0.1.2/figures/Figure2.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/figures/Figure3.png` & `pyplotbrookings-0.1.2/figures/Figure3.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/figures/logo.png` & `pyplotbrookings-0.1.2/figures/logo.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/.DS_Store` & `pyplotbrookings-0.1.2/src/.DS_Store`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/.DS_Store` & `pyplotbrookings-0.1.2/src/pyplotbrookings/.DS_Store`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/pyplotbrookings.py` & `pyplotbrookings-0.1.2/src/pyplotbrookings/pyplotbrookings.py`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/.ipynb_checkpoints/Examples-checkpoint.ipynb` & `pyplotbrookings-0.1.2/src/pyplotbrookings/.ipynb_checkpoints/Examples-checkpoint.ipynb`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/LICENSE.txt` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Black.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Black.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-BlackItalic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-BlackItalic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Bold.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Bold.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-BoldItalic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Italic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Italic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Light.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Light.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-LightItalic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-LightItalic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Medium.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Medium.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-MediumItalic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-MediumItalic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Regular.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Regular.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-Thin.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-Thin.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/fonts/Roboto-ThinItalic.ttf` & `pyplotbrookings-0.1.2/src/pyplotbrookings/fonts/Roboto-ThinItalic.ttf`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/b_logo.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/b_logo.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/bc.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/bc.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/bi.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/bi.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/brookings.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/brookings.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cc.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cc.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/ccf.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/ccf.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/ceaps.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/ceaps.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cepm.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cepm.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/chp.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/chp.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cmep.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cmep.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/crm.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/crm.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/csd.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/csd.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cti.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cti.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cue.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cue.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/cuse.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/cuse.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/es.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/es.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/fp.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/fp.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/global.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/global.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/gs.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/gs.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/hc.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/hc.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/metro.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/metro.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/src/pyplotbrookings/logos/thp.png` & `pyplotbrookings-0.1.2/src/pyplotbrookings/logos/thp.png`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/LICENSE` & `pyplotbrookings-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pyplotbrookings-0.1.1/pyproject.toml` & `pyplotbrookings-0.1.2/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyplotbrookings"
-version = "0.1.1"
+version = "0.1.2"
 authors = [
   { name="Adam Sedlak", email="asedlak@brookings.edu" },
 ]
 description = "A plotting package for the Brookings Institution"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyplotbrookings-0.1.1/PKG-INFO` & `pyplotbrookings-0.1.2/README.md`

 * *Files 17% similar despite different names*

```diff
@@ -1,34 +1,21 @@
-Metadata-Version: 2.1
-Name: pyplotbrookings
-Version: 0.1.1
-Summary: A plotting package for the Brookings Institution
-Project-URL: Homepage, https://github.com/Adam-Sedlak-Brookings/pyplotbrookings
-Author-email: Adam Sedlak <asedlak@brookings.edu>
-License-File: LICENSE
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Classifier: Programming Language :: Python :: 3
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-
 # pyplotbrookings <img src="figures/logo.png" align="right" width="120"/>
 
 ## Overview
 
 `pyplotbrookings` is a `matplotlib` extension which implements the Brookings
 Institution style guide. It offers several color palettes, a custom theme, and a few
 helper functions. `pyplotbrookings` is a python implementation of `ggbrookings`, 
 an R extension for `ggplot`.
 
 ## Installation
 
-`pyplotbrookings` is now a python package! It downloaded from PyPI with `pip` (https://pypi.org/project/pyplotbrookings/0.1.0/)!
+`pyplotbrookings` is now a python package! It downloaded from PyPI with `pip` (https://pypi.org/project/pyplotbrookings/)!
 ```
-pip install pyplotbrookings==0.1.0
+pip install pyplotbrookings
 ```
 
 The accepted alias for `pyplotbrookings` is `ppb`. For example,
 ```python
 import pyplotbrookings.pyplotbrookings as ppb
 ```
 
@@ -40,14 +27,15 @@
     custom one which adheres to the Brookings style guide.
 
 -   `get_palette()` returns the colors for a valid Brookings brand 
     palettes.
 
 -   `set_palette()` sets the `matplotlib` color cycler to one of
     the Brookings brand palettes.
+    - Valid color palettes are: `default`, `brand1`, `brand2`, `analogous1`, `analogous2`, `contrasting1`, `contrasting2`, `semantic1`, `semantic2`, `semantic3`, `pos_neg1`, `pos_neg2`, `political1`, `political2` `political3`, `political4`, `categorical`, `sequential1`, `sequential2`, `diverging`, `misc`, `brand blue`, `vivid blue`, `teal`, `green`, `yellow`, `orange`, `red`, `magenta`, `purple`
 
 -   `get_cmap()` returns a continuous palette (or color map) using one of
     the color Brookings color palettes.
 
 -   `view_palette()` helper function that previews a color palette
     showing the color, order, and the appropriate text color 
     that can be applied on top of each color.
@@ -55,22 +43,27 @@
 -   `add_title()` adds titles and subtitles to a figure that are consistent 
     with Brookings brand guidelines. 
 
 -   `add_notes()` adds notes to the bottom of a figure also consistent 
     with Brookings brand guidelines.
 
 -   `add_logo()` adds a program/center logo to a figure.
+    - You can add a logo using a local path or use one of the logos that comes with `pyplotbrookings`.
+    - The following logos are included with pyplotbrookings: `bc` (Brown Center), `bi` (Bass Initiative on Innovation and Placemaking), `brookings` (Brookings Institution), `cc` (China Center), `ccf` (Center on Children and Families), `ceaps` (Center for East Asia Policy Studies), `cepm` (Center for Effective Policy Management), `chp` (Center for Health Policy), `cmep` (Center for Middle Eastern Policy), `crm` (Center on Regulation and Markets), `csd` (Center for Sustainable Development), `cti` (Center for Technology Innovation), `cue` (Center for Universal Education), `cuse` (Center on United States and Europe), `es` (Economic Studies), `fp` (Foreign Policy), `global` (Global Studies), `gs` (Governance Studies), `hc` (Hutchins Center), `metro` (Metropolitan Policy Studies), `thp` (The Hamilton Project).
 
 -   `figure()` creates a `matplotlib` figure in one of the standard 
     Brookings sizes.
 
 -   `save()` saves a figure in the Brookings advised dpi values depending
      on content type.
 
 
+## Contact
+To report any bugs or discuss contributing to this package please contact Adam Sedlak or Valerie Wirtschafter.
+
 ## Examples
 Let's create a figure plot using `pyplotbrookings`. First we'll need some data
 
 ```python
 import matplotlib.pyplot as plt
 import pyplotbrookings.pyplotbrookings as ppb
 import seaborn as sns
@@ -104,14 +97,16 @@
 # Adding notes
 ppb.add_notes('Source: Palmer Station Antarctica LTER', 
               'Notes: Figure made using matplotlib')
 
 ppb.add_logo('hc')
 ```
 
+![alt text](figures/Figure1A.png)
+
 `pyplotbrookings` is designed to work with many different plots. Let's try creating a scatter plot that uses a colormap
 
 ```python
 # Getting the Brookings sequential2 color map
 cmap = ppb.get_cmap('sequential2', reverse=True)
 # Creating a scatter plot
 plt.scatter(data=penguins, x='bill_length_mm', y='bill_depth_mm', c='flipper_length_mm', cmap=cmap)
@@ -134,14 +129,15 @@
 ppb.add_notes('Source: Palmer Station Antarctica LTER',
               'Example: Here is some extra long text that\ngoes on and on and needs a linefeed.',
               'Notes: Figure made using matplotlib')
 
 # Adding a CRM logo
 ppb.add_logo('crm', scale=0.35, offsets=(-0.1, 0))
 ```
+![alt text](figures/Figure2.png)
 
 We could also create a box plot. Note that titles and notes auto-align to the left margin of the figure.
 ```python
 # Creating a boxplot
 sns.boxplot(data=penguins, x='bill_depth_mm', y='island', palette=ppb.get_palette('misc'))
 
 
@@ -157,7 +153,8 @@
 
 # Adding matplotlib legend/labels
 plt.xlabel('Bill Depth (mm)')
 plt.ylabel('Island')
 
 ppb.add_logo('crm', scale=0.35, offsets=(-0.1, 0))
 ```
+![alt text](figures/Figure3.png)
```

