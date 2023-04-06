# Comparing `tmp/sbcoyote-1.3.6.tar.gz` & `tmp/sbcoyote-1.3.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sbcoyote-1.3.6.tar", max compression
+gzip compressed data, was "sbcoyote-1.3.7.tar", max compression
```

## Comparing `sbcoyote-1.3.6.tar` & `sbcoyote-1.3.7.tar`

### file list

```diff
@@ -1,51 +1,52 @@
--rw-r--r--   0        0        0     1090 2023-01-10 20:04:27.423064 sbcoyote-1.3.6/LICENSE
--rw-r--r--   0        0        0     1812 2023-02-15 17:19:59.916533 sbcoyote-1.3.6/pyproject.toml
--rw-r--r--   0        0        0    10243 2023-02-10 19:16:23.214334 sbcoyote-1.3.6/README.md
--rw-r--r--   0        0        0       23 2021-09-10 21:55:36.689271 sbcoyote-1.3.6/rkviewer/__init__.py
--rw-r--r--   0        0        0        0 2021-09-10 21:55:36.690269 sbcoyote-1.3.6/rkviewer/canvas/__init__.py
--rw-r--r--   0        0        0    91517 2023-02-16 03:57:51.511834 sbcoyote-1.3.6/rkviewer/canvas/canvas.py
--rw-r--r--   0        0        0    32207 2021-09-10 21:55:36.692264 sbcoyote-1.3.6/rkviewer/canvas/data.py
--rw-r--r--   0        0        0    59253 2023-02-16 03:57:51.512804 sbcoyote-1.3.6/rkviewer/canvas/elements.py
--rw-r--r--   0        0        0    17929 2023-02-16 03:57:51.514828 sbcoyote-1.3.6/rkviewer/canvas/geometry.py
--rw-r--r--   0        0        0     8408 2021-09-10 21:55:36.694258 sbcoyote-1.3.6/rkviewer/canvas/overlays.py
--rw-r--r--   0        0        0     1731 2021-09-10 21:55:36.695255 sbcoyote-1.3.6/rkviewer/canvas/state.py
--rw-r--r--   0        0        0     6751 2022-12-13 22:58:03.646205 sbcoyote-1.3.6/rkviewer/canvas/utils.py
--rw-r--r--   0        0        0    18996 2023-02-16 03:57:51.515820 sbcoyote-1.3.6/rkviewer/config.py
--rw-r--r--   0        0        0    22652 2023-02-15 22:07:24.703283 sbcoyote-1.3.6/rkviewer/controller.py
--rw-r--r--   0        0        0    13105 2021-09-10 21:55:36.697250 sbcoyote-1.3.6/rkviewer/events.py
--rw-r--r--   0        0        0    89825 2023-02-16 00:48:24.752107 sbcoyote-1.3.6/rkviewer/forms.py
--rw-r--r--   0        0        0    92469 2023-02-15 22:06:13.144995 sbcoyote-1.3.6/rkviewer/iodine.py
--rw-r--r--   0        0        0     1817 2021-09-10 21:55:36.655349 sbcoyote-1.3.6/rkviewer/json/dark-settings.json
--rw-r--r--   0        0        0     3329 2023-02-06 19:51:01.343848 sbcoyote-1.3.6/rkviewer/json/default-settings.json
--rw-r--r--   0        0        0      727 2021-09-10 21:55:36.653177 sbcoyote-1.3.6/rkviewer/json/settings.json
--rw-r--r--   0        0        0     3399 2023-02-10 23:42:55.235161 sbcoyote-1.3.6/rkviewer/main.py
--rw-r--r--   0        0        0    12295 2021-09-10 21:55:36.701263 sbcoyote-1.3.6/rkviewer/mvc.py
--rw-r--r--   0        0        0        0 2021-09-10 21:55:36.701263 sbcoyote-1.3.6/rkviewer/plugin/__init__.py
--rw-r--r--   0        0        0    56863 2021-10-25 20:51:11.812462 sbcoyote-1.3.6/rkviewer/plugin/api.py
--rw-r--r--   0        0        0      513 2021-09-10 21:55:36.703235 sbcoyote-1.3.6/rkviewer/plugin/canvas.py
--rw-r--r--   0        0        0     9684 2021-09-10 21:55:36.703235 sbcoyote-1.3.6/rkviewer/plugin/classes.py
--rw-r--r--   0        0        0      154 2021-09-10 21:55:36.704231 sbcoyote-1.3.6/rkviewer/plugin/events.py
--rw-r--r--   0        0        0    18945 2023-01-26 22:34:13.868916 sbcoyote-1.3.6/rkviewer/plugin_manage.py
--rw-r--r--   0        0        0        0 2021-09-10 21:55:36.706226 sbcoyote-1.3.6/rkviewer/resources/__init__.py
--rw-r--r--   0        0        0      335 2021-09-10 21:55:36.705228 sbcoyote-1.3.6/rkviewer/resources/AlignBottom_XP.png
--rw-r--r--   0        0        0      312 2021-09-10 21:55:36.706226 sbcoyote-1.3.6/rkviewer/resources/alignHorizCenter_XP.png
--rw-r--r--   0        0        0      298 2021-09-10 21:55:36.707254 sbcoyote-1.3.6/rkviewer/resources/alignHorizEqually_XP.png
--rw-r--r--   0        0        0      379 2021-09-10 21:55:36.707254 sbcoyote-1.3.6/rkviewer/resources/alignLeft_XP.png
--rw-r--r--   0        0        0      238 2021-09-10 21:55:36.708254 sbcoyote-1.3.6/rkviewer/resources/alignOnGrid_XP.png
--rw-r--r--   0        0        0      602 2021-09-10 21:55:36.709251 sbcoyote-1.3.6/rkviewer/resources/alignRight_XP.png
--rw-r--r--   0        0        0      366 2021-09-10 21:55:36.709251 sbcoyote-1.3.6/rkviewer/resources/alignTop_XP.png
--rw-r--r--   0        0        0      280 2021-09-10 21:55:36.709251 sbcoyote-1.3.6/rkviewer/resources/alignVertCenter_XP.png
--rw-r--r--   0        0        0      308 2021-09-10 21:55:36.710248 sbcoyote-1.3.6/rkviewer/resources/alignVertEqually_XP.png
--rw-r--r--   0        0        0      389 2021-09-10 21:55:36.710248 sbcoyote-1.3.6/rkviewer/resources/info-2-16.png
--rw-r--r--   0        0        0     8227 2023-01-23 21:52:33.720240 sbcoyote-1.3.6/rkviewer/utils.py
--rw-r--r--   0        0        0    43651 2023-02-16 16:08:31.070653 sbcoyote-1.3.6/rkviewer/view.py
--rw-r--r--   0        0        0     8420 2023-02-16 16:08:43.075683 sbcoyote-1.3.6/rkviewer_plugins/addReaction.py
--rw-r--r--   0        0        0     7696 2023-01-30 22:21:57.346994 sbcoyote-1.3.6/rkviewer_plugins/align_circle.py
--rw-r--r--   0        0        0    10023 2023-01-24 01:05:59.812128 sbcoyote-1.3.6/rkviewer_plugins/arrow_designer.py
--rw-r--r--   0        0        0     7912 2022-12-12 22:28:29.173608 sbcoyote-1.3.6/rkviewer_plugins/exportAntimony.py
--rw-r--r--   0        0        0    66991 2023-02-10 16:59:19.704579 sbcoyote-1.3.6/rkviewer_plugins/exportSBML.py
--rw-r--r--   0        0        0   149420 2023-02-15 19:41:11.915051 sbcoyote-1.3.6/rkviewer_plugins/importSBML.py
--rw-r--r--   0        0        0    16758 2023-02-16 16:09:48.612041 sbcoyote-1.3.6/rkviewer_plugins/networkX.py
--rw-r--r--   0        0        0    17557 2023-02-16 16:09:03.307322 sbcoyote-1.3.6/rkviewer_plugins/randomNetwork.py
--rw-r--r--   0        0        0    12839 2022-12-27 23:53:49.202279 sbcoyote-1.3.6/rkviewer_plugins/structuralAnalysis.py
--rw-r--r--   0        0        0    11801 1970-01-01 00:00:00.000000 sbcoyote-1.3.6/PKG-INFO
+-rw-r--r--   0        0        0     1090 2023-01-10 20:04:27.423064 sbcoyote-1.3.7/LICENSE
+-rw-r--r--   0        0        0     1812 2023-04-06 23:40:48.980565 sbcoyote-1.3.7/pyproject.toml
+-rw-r--r--   0        0        0    10355 2023-02-23 20:29:46.172339 sbcoyote-1.3.7/README.md
+-rw-r--r--   0        0        0       23 2021-09-10 21:55:36.689271 sbcoyote-1.3.7/rkviewer/__init__.py
+-rw-r--r--   0        0        0        0 2021-09-10 21:55:36.690269 sbcoyote-1.3.7/rkviewer/canvas/__init__.py
+-rw-r--r--   0        0        0    91711 2023-04-05 20:30:56.859645 sbcoyote-1.3.7/rkviewer/canvas/canvas.py
+-rw-r--r--   0        0        0    32394 2023-03-29 18:22:43.731567 sbcoyote-1.3.7/rkviewer/canvas/data.py
+-rw-r--r--   0        0        0    59253 2023-02-16 03:57:51.512804 sbcoyote-1.3.7/rkviewer/canvas/elements.py
+-rw-r--r--   0        0        0    17929 2023-02-16 03:57:51.514828 sbcoyote-1.3.7/rkviewer/canvas/geometry.py
+-rw-r--r--   0        0        0     8408 2021-09-10 21:55:36.694258 sbcoyote-1.3.7/rkviewer/canvas/overlays.py
+-rw-r--r--   0        0        0     1731 2021-09-10 21:55:36.695255 sbcoyote-1.3.7/rkviewer/canvas/state.py
+-rw-r--r--   0        0        0     6751 2022-12-13 22:58:03.646205 sbcoyote-1.3.7/rkviewer/canvas/utils.py
+-rw-r--r--   0        0        0    18996 2023-02-16 03:57:51.515820 sbcoyote-1.3.7/rkviewer/config.py
+-rw-r--r--   0        0        0    23001 2023-03-29 18:22:41.234242 sbcoyote-1.3.7/rkviewer/controller.py
+-rw-r--r--   0        0        0    13105 2021-09-10 21:55:36.697250 sbcoyote-1.3.7/rkviewer/events.py
+-rw-r--r--   0        0        0    97893 2023-04-06 00:05:27.465051 sbcoyote-1.3.7/rkviewer/forms.py
+-rw-r--r--   0        0        0    94813 2023-03-29 18:22:11.285164 sbcoyote-1.3.7/rkviewer/iodine.py
+-rw-r--r--   0        0        0     1817 2021-09-10 21:55:36.655349 sbcoyote-1.3.7/rkviewer/json/dark-settings.json
+-rw-r--r--   0        0        0     3329 2023-02-06 19:51:01.343848 sbcoyote-1.3.7/rkviewer/json/default-settings.json
+-rw-r--r--   0        0        0      727 2021-09-10 21:55:36.653177 sbcoyote-1.3.7/rkviewer/json/settings.json
+-rw-r--r--   0        0        0     3399 2023-02-10 23:42:55.235161 sbcoyote-1.3.7/rkviewer/main.py
+-rw-r--r--   0        0        0    12295 2021-09-10 21:55:36.701263 sbcoyote-1.3.7/rkviewer/mvc.py
+-rw-r--r--   0        0        0        0 2021-09-10 21:55:36.701263 sbcoyote-1.3.7/rkviewer/plugin/__init__.py
+-rw-r--r--   0        0        0    57933 2023-03-29 18:22:16.274177 sbcoyote-1.3.7/rkviewer/plugin/api.py
+-rw-r--r--   0        0        0      513 2021-09-10 21:55:36.703235 sbcoyote-1.3.7/rkviewer/plugin/canvas.py
+-rw-r--r--   0        0        0     9684 2023-03-27 18:05:44.898125 sbcoyote-1.3.7/rkviewer/plugin/classes.py
+-rw-r--r--   0        0        0      154 2021-09-10 21:55:36.704231 sbcoyote-1.3.7/rkviewer/plugin/events.py
+-rw-r--r--   0        0        0    18945 2023-01-26 22:34:13.868916 sbcoyote-1.3.7/rkviewer/plugin_manage.py
+-rw-r--r--   0        0        0        0 2021-09-10 21:55:36.706226 sbcoyote-1.3.7/rkviewer/resources/__init__.py
+-rw-r--r--   0        0        0      335 2021-09-10 21:55:36.705228 sbcoyote-1.3.7/rkviewer/resources/AlignBottom_XP.png
+-rw-r--r--   0        0        0      312 2021-09-10 21:55:36.706226 sbcoyote-1.3.7/rkviewer/resources/alignHorizCenter_XP.png
+-rw-r--r--   0        0        0      298 2021-09-10 21:55:36.707254 sbcoyote-1.3.7/rkviewer/resources/alignHorizEqually_XP.png
+-rw-r--r--   0        0        0      379 2021-09-10 21:55:36.707254 sbcoyote-1.3.7/rkviewer/resources/alignLeft_XP.png
+-rw-r--r--   0        0        0      238 2021-09-10 21:55:36.708254 sbcoyote-1.3.7/rkviewer/resources/alignOnGrid_XP.png
+-rw-r--r--   0        0        0      602 2021-09-10 21:55:36.709251 sbcoyote-1.3.7/rkviewer/resources/alignRight_XP.png
+-rw-r--r--   0        0        0      366 2021-09-10 21:55:36.709251 sbcoyote-1.3.7/rkviewer/resources/alignTop_XP.png
+-rw-r--r--   0        0        0      280 2021-09-10 21:55:36.709251 sbcoyote-1.3.7/rkviewer/resources/alignVertCenter_XP.png
+-rw-r--r--   0        0        0      308 2021-09-10 21:55:36.710248 sbcoyote-1.3.7/rkviewer/resources/alignVertEqually_XP.png
+-rw-r--r--   0        0        0      389 2021-09-10 21:55:36.710248 sbcoyote-1.3.7/rkviewer/resources/info-2-16.png
+-rw-r--r--   0        0        0     8227 2023-01-23 21:52:33.720240 sbcoyote-1.3.7/rkviewer/utils.py
+-rw-r--r--   0        0        0    47494 2023-04-06 23:40:44.717960 sbcoyote-1.3.7/rkviewer/view.py
+-rw-r--r--   0        0        0     8861 2023-04-05 18:55:40.926273 sbcoyote-1.3.7/rkviewer_plugins/addReaction.py
+-rw-r--r--   0        0        0     7700 2023-03-27 21:04:32.885475 sbcoyote-1.3.7/rkviewer_plugins/align_circle.py
+-rw-r--r--   0        0        0    10023 2023-01-24 01:05:59.812128 sbcoyote-1.3.7/rkviewer_plugins/arrow_designer.py
+-rw-r--r--   0        0        0     7910 2023-03-27 23:00:15.322399 sbcoyote-1.3.7/rkviewer_plugins/exportAntimony.py
+-rw-r--r--   0        0        0    67466 2023-03-30 18:47:20.839876 sbcoyote-1.3.7/rkviewer_plugins/exportSBML.py
+-rw-r--r--   0        0        0   152356 2023-03-30 18:44:02.927726 sbcoyote-1.3.7/rkviewer_plugins/importSBML.py
+-rw-r--r--   0        0        0     1152 2023-04-05 18:58:00.989843 sbcoyote-1.3.7/rkviewer_plugins/modelMetrics.py
+-rw-r--r--   0        0        0    16762 2023-03-27 21:03:50.201865 sbcoyote-1.3.7/rkviewer_plugins/networkX.py
+-rw-r--r--   0        0        0    17554 2023-03-27 21:03:22.666400 sbcoyote-1.3.7/rkviewer_plugins/randomNetwork.py
+-rw-r--r--   0        0        0    12839 2023-03-27 21:03:31.309823 sbcoyote-1.3.7/rkviewer_plugins/structuralAnalysis.py
+-rw-r--r--   0        0        0    11910 1970-01-01 00:00:00.000000 sbcoyote-1.3.7/PKG-INFO
```

### Comparing `sbcoyote-1.3.6/LICENSE` & `sbcoyote-1.3.7/LICENSE`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/pyproject.toml` & `sbcoyote-1.3.7/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "SBcoyote"
-version = "1.3.6"
+version = "1.3.7"
 description = "SBcoyote: An Extensible Python Based Reaction Editor and Viewer."
 readme = "README.md"
 authors = ["Jin Xu and Gary Geng et al <jxu2019@uw.edu>"]
 packages = [
     { include = "rkviewer" },
     { include = "rkviewer_plugins"},
 ]
```

### Comparing `sbcoyote-1.3.6/README.md` & `sbcoyote-1.3.7/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -5,33 +5,36 @@
 
 SBcoyote, initially called PyRKViewer or Coyote, is a cross-platform visualization tool for drawing reaction networks written with the
 [wxPython](https://www.wxpython.org/) framework. It can draw reactants, products, reactions, and compartments, and its features include but are not limited to:
 * Support for floating and boundary species.
 * Reactions can be displayed using Bezier curves and straight lines.
 * Plugin support, with some plugin examples: arrow designer, random network, auto layout, etc.
 
-## Installment for Users
+## Citing
 
-* Install Python 3.7, 3.8, 3.9 or 3.10 if not ready in the system.
+If you are using any of the code, please cite the article (https://arxiv.org/abs/2302.09151). 
+
+## Installing SBcoyote
+
+* Install Python 3.7, 3.8, 3.9 or 3.10 if not already in the system.
 * Go to the command line and type `pip install SBcoyote`.
-* If wxPython won't get installed automatically, please try to install wxPython 4.1.1 or 4.2.0 manually referring to https://wxpython.org/pages/downloads/index.html. Note wxPython 4.1.1 does not apply to Python 3.10. 
+* If wxPython doesn't get installed automatically, please try to install wxPython 4.1.1 or 4.2.0 manually referring to https://wxpython.org/pages/downloads/index.html. Note wxPython 4.1.1 does not work with Python 3.10. 
 * To run the application, simply type in the command line `SBcoyote`.
 
 ## Documentation
 
 The full documentation can be found at: https://sys-bio.github.io/SBcoyote/
 
 ## Visualization Example
 
 Here is a visualization example by SBcoyote for the large-scale Escherichia coli core 
 metabolism network (King et al., 2015; Orth et al., 2010).
 
 <img src="https://raw.githubusercontent.com/sys-bio/SBcoyote/main/examples/ecoli.png" width="500" height="400">
 
-
 ## Installment options for Developers
 
 ### Installing with Poetry
 1. If you do not have poetry installed on your computer, follow the quick steps shown [here](https://python-poetry.org/docs/).
 2. Once you have poetry installed, you will download SBcoyote. Click the green button at the top of this page that says “Code” and choose “Download ZIP”. You want to make sure you know where you have downloaded this. Unzip the folder to your desired directory.
 3. Next, open your terminal and navigate to the directory containing SBcoyote.
 4. Once inside the main folder of the application you can install the dependencies. To install the base dependencies simply run `poetry install`. To install the optional ones as well, run `poetry install -E simulation`. Note that this step may take a while. To learn more about which set of dependencies is right for you, refer to the [Dependencies](#Dependencies) section below.
```

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/canvas.py` & `sbcoyote-1.3.7/rkviewer/canvas/canvas.py`

 * *Files 0% similar despite different names*

```diff
@@ -1928,14 +1928,19 @@
         self.FullRedraw()
 
     def SelectAllReactions(self):
         with self._SelectGroupEvent():
             self.sel_reactions_idx.set_item({r.index for r in self._reactions})
         self.FullRedraw()
 
+    def SelectAllCompartments(self):
+        with self._SelectGroupEvent():
+            self.sel_compartments_idx.set_item({c.index for c in self._compartments})
+        self.FullRedraw()
+
     def ClearCurrentSelection(self):
         """Clear the current highest level of selection.
 
         If there are reactants or products marked, clear those. OTherwise clear selected nodes and
         reactions.
         """
         if len(self._reactant_idx) + len(self._product_idx) != 0:
```

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/data.py` & `sbcoyote-1.3.7/rkviewer/canvas/data.py`

 * *Files 1% similar despite different names*

```diff
@@ -247,14 +247,16 @@
         net_index: The network index of the node.
     """
     id: str
     # fill_color: wx.Colour
     # border_color: wx.Colour
     # border_width: float
     concentration: float
+    node_name: str
+    node_SBO: str
     position: Vec2
     size: Vec2
     comp_idx: int
     index: int
     net_index: int
     floatingNode: bool
     lockNode: bool  # Prevent users from moving the node
@@ -268,15 +270,17 @@
     def __init__(self, id: str, net_index: int, *, pos: Vec2, size: Vec2, comp_idx: int = -1,
                  floatingNode: bool = True,
                  lockNode: bool = False,
                  shape_index: int = 0,
                  composite_shape: Optional[CompositeShape] = None,
                  index: int = -1,
                  original_index: int = -1,
-                 concentration: float = 0.0):
+                 concentration: float = 0.0, 
+                 node_name: str = '',
+                 node_SBO: str = ''):
         self.index = index
         self.net_index = net_index
         self.id = id
         self.position = pos
         self.size = size
         # self.fill_color = fill_color
         # self.border_color = border_color
@@ -284,14 +288,16 @@
         self.comp_idx = comp_idx
         self.floatingNode = floatingNode
         self.lockNode = lockNode
         self.shape_index = shape_index
         self.composite_shape = composite_shape
         self.original_index = original_index
         self.concentration = concentration
+        self.node_name = node_name
+        self.node_SBO = node_SBO
 
     def _get_prim_field(self, field):
         for prim, _ in self.composite_shape.items:
             if hasattr(prim, field):
                 return getattr(prim, field)
         return None
```

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/elements.py` & `sbcoyote-1.3.7/rkviewer/canvas/elements.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/geometry.py` & `sbcoyote-1.3.7/rkviewer/canvas/geometry.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/overlays.py` & `sbcoyote-1.3.7/rkviewer/canvas/overlays.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/state.py` & `sbcoyote-1.3.7/rkviewer/canvas/state.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/canvas/utils.py` & `sbcoyote-1.3.7/rkviewer/canvas/utils.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/config.py` & `sbcoyote-1.3.7/rkviewer/config.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/controller.py` & `sbcoyote-1.3.7/rkviewer/controller.py`

 * *Files 1% similar despite different names*

```diff
@@ -116,15 +116,15 @@
     def add_node_g(self, neti: int, node: Node) -> int:
         '''
         Add node represented by the given Node variable.
 
         The 'g' suffix indicates that this operation creates its own group
         '''
         with self.group_action():
-            iod.addNode(neti, node.id, node.position.x, node.position.y, node.size.x, node.size.y, True) # True = floating species
+            iod.addNode(neti, node.id, node.position.x, node.position.y, node.size.x, node.size.y, True) 
             nodei = iod.getNodeIndex(neti, node.id)
             # iod.setNodeFillColorAlpha(neti, nodei, node.fill_color.Alpha() / 255)
             # iod.setNodeFillColorRGB(neti, nodei, node.fill_color.Red(),
             #                         node.fill_color.Green(), node.fill_color.Blue())
             # iod.setNodeBorderColorAlpha(neti, nodei, node.border_color.Alpha() / 255)
             # iod.setNodeBorderColorRGB(neti, nodei, node.border_color.Red(),
             #                            node.border_color.Green(), node.border_color.Blue())
@@ -199,14 +199,22 @@
         iod.setNodeSize(neti, nodei, size.x, size.y)
 
     @iod_setter
     def rename_node(self, neti: int, nodei: int, new_id: str):
         iod.setNodeID(neti, nodei, new_id)
 
     @iod_setter
+    def set_node_name(self, neti: int, nodei: int, new_name: str):
+        iod.setNodeName(neti, nodei, new_name)
+
+    @iod_setter
+    def set_node_SBO(self, neti: int, nodei: int, new_SBO: str):
+        iod.setNodeSBO(neti, nodei, new_SBO)
+
+    @iod_setter
     def set_node_concentration(self, neti: int, nodei: int, new_conc: float):
         iod.setNodeConcentration(neti, nodei, new_conc)
 
     @iod_setter
     def set_node_floating_status(self, neti: int, nodei: int, floatingStatus: bool):
         iod.setNodeFloatingStatus (neti, nodei, floatingStatus)
 
@@ -464,14 +472,16 @@
         return Node(
             id,
             neti,
             index=nodei,
             pos=Vec2(x, y),
             size=Vec2(w, h),
             concentration=iod.getNodeConcentration(neti, nodei),
+            node_name = iod.getNodeName(neti, nodei),
+            node_SBO = iod.getNodeSBO(neti, nodei),
             # fill_color=fill_color,
             # border_color=border_color,
             # border_width=iod.getNodeBorderWidth(neti, nodei),
             comp_idx=iod.getCompartmentOfNode(neti, nodei),
             floatingNode=iod.IsFloatingNode(neti, nodei),
             lockNode=iod.IsNodeLocked(neti, nodei),
             shape_index=iod.getNodeShapeIndex(neti, nodei),
```

### Comparing `sbcoyote-1.3.6/rkviewer/events.py` & `sbcoyote-1.3.7/rkviewer/events.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/forms.py` & `sbcoyote-1.3.7/rkviewer/forms.py`

 * *Files 1% similar despite different names*

```diff
@@ -861,40 +861,56 @@
 
             id_text = 'identifier' if len(self._selected_idx) == 1 else 'identifiers'
             self.main_section.labels[self.id_ctrl.GetId()].SetLabel(id_text)
 
             comp_text = 'compartment' if len(self._selected_idx) == 1 else 'compartment'
             self.main_section.labels[self.comp_ctrl.GetId()].SetLabel(comp_text)
 
+            name_text = 'name' if len(self._selected_idx) == 1 else 'name'
+            self.main_section.labels[self.name_ctrl.GetId()].SetLabel(name_text)
+
+            SBO_text = 'SBO' if len(self._selected_idx) == 1 else 'SBO'
+            self.main_section.labels[self.SBO_ctrl.GetId()].SetLabel(SBO_text)
+
             concentration_text = 'concentration' if len(self._selected_idx) == 1 else 'concentrations'
             self.main_section.labels[self.conc_ctrl.GetId()].SetLabel(concentration_text)
 
-            size_text = 'size' if len(self._selected_idx) == 1 else 'total span'
+            size_text = 'size' if len(self._selected_idx) == 1 else 'size'
             self.main_section.labels[self.size_ctrl.GetId()].SetLabel(size_text)
+
         self.ExternalUpdate()
 
     def CreateControls(self):
         self.id_ctrl = self.main_section.CreateTextCtrl()
         self.id_ctrl.Bind(wx.EVT_TEXT, self._OnIdText)
         self.main_section.AppendControl('identifier', self.id_ctrl)
 
         self.comp_ctrl = self.main_section.CreateTextCtrl()
         #self.comp_ctrl.Bind(wx.EVT_TEXT, self._OnCompText)
         self.main_section.AppendControl('compartment', self.comp_ctrl)
+
+        self.name_ctrl = self.main_section.CreateTextCtrl()
+        self.name_ctrl.Bind(wx.EVT_TEXT, self._OnNameText)
+        self.main_section.AppendControl('name', self.name_ctrl)
+
+        self.SBO_ctrl = self.main_section.CreateTextCtrl()
+        self.SBO_ctrl.Bind(wx.EVT_TEXT, self._OnSBOText)
+        self.main_section.AppendControl('SBO', self.SBO_ctrl)
         
         self.conc_ctrl = self.main_section.CreateTextCtrl()
         self.conc_ctrl.Bind(wx.EVT_TEXT, self._OnConcText)
         self.main_section.AppendControl('concentration', self.conc_ctrl)
 
         self.pos_ctrl = self.main_section.CreateTextCtrl()
         self.pos_ctrl.Bind(wx.EVT_TEXT, self._OnPosText)
         self.main_section.AppendControl('position', self.pos_ctrl)
 
         self.size_ctrl = self.main_section.CreateTextCtrl()
-        self.size_ctrl.Bind(wx.EVT_TEXT, self._OnSizeText)
+        #self.size_ctrl.Bind(wx.EVT_TEXT, self._OnSizeText)
+        self.size_ctrl.Bind(wx.EVT_TEXT, self._OnNodeSizeText)
         self.main_section.AppendControl('size', self.size_ctrl)
 
         self.nodeStates = ['Floating Node', 'Boundary Node']
         self.nodeStatusDropDown = wx.Choice(self.main_section, choices=self.nodeStates)
         self.main_section.AppendControl('node status', self.nodeStatusDropDown)
         self.nodeStatusDropDown.Bind(wx.EVT_CHOICE, self.OnNodeStatusChoice)
 
@@ -926,14 +942,47 @@
                 # loop terminated fine. There is no duplicate ID
                 self.self_changes = True
                 with self.controller.group_action():
                     self.controller.rename_node(self.net_index, nodei, new_id)
                     post_event(DidModifyNodesEvent([nodei]))
         self.main_section.SetValidationState(True, self.id_ctrl.GetId())
 
+    def _OnNameText(self, evt):
+        """Callback for the name control."""
+        new_name = evt.GetString()
+        assert len(self._selected_idx) == 1
+        [nodei] = self._selected_idx
+        ctrl_name = self.name_ctrl.GetId()
+
+        if len(new_name) != 0:
+            self.self_changes = True
+            with self.controller.group_action():
+                self.controller.set_node_name(self.net_index, nodei, new_name)
+                post_event(DidModifyNodesEvent([nodei]))
+        self.main_section.SetValidationState(True, self.id_ctrl.GetId())
+
+    def _OnSBOText(self, evt):
+        """Callback for the SBO control."""
+        new_SBO = evt.GetString()
+        assert len(self._selected_idx) == 1
+        [nodei] = self._selected_idx
+        ctrl_SBO = self.SBO_ctrl.GetId()
+
+        if len(new_SBO) != 0:
+            if new_SBO[:8] == "SBO:0000" and new_SBO[8:11].isdigit():
+                self.self_changes = True
+                with self.controller.group_action():
+                    self.controller.set_node_SBO(self.net_index, nodei, new_SBO)
+                    post_event(DidModifyNodesEvent([nodei]))
+            else:
+                self.main_section.SetValidationState(False, ctrl_SBO, "Not saved: Invalid SBO Term ID (Example: SBO:0000247)")
+                return
+         
+        self.main_section.SetValidationState(True, self.SBO_ctrl.GetId())
+
     # def _OnCompText(self, evt):
     #     """Callback for the compartment control."""
     #     #needs to double check especially comp_idx vs comp_id
     #     new_comp = evt.GetString()
     #     assert len(self._selected_idx) == 1
     #     [nodei] = self._selected_idx
     #     ctrl_comp = self.comp_ctrl.GetId()
@@ -1086,14 +1135,112 @@
                 post_event(DidMoveNodesEvent(idx_list, offsets, dragged=False))
                 post_event(DidResizeNodesEvent(idx_list, ratio=ratio, dragged=False))
                 for node in nodes:
                     self.controller.move_node(self.net_index, node.index, node.position)
                     self.controller.set_node_size(self.net_index, node.index, node.size)
         self.main_section.SetValidationState(True, self.size_ctrl.GetId())
 
+    def _OnNodeSizeText(self, evt):
+        """Callback for the node size control."""
+        # new_SBO = evt.GetString()
+        # assert len(self._selected_idx) == 1
+        # [nodei] = self._selected_idx
+        # ctrl_SBO = self.SBO_ctrl.GetId()
+
+        # if len(new_SBO) != 0:
+        #     if new_SBO[:8] == "SBO:0000" and new_SBO[8:11].isdigit():
+        #         self.self_changes = True
+        #         with self.controller.group_action():
+        #             self.controller.set_node_SBO(self.net_index, nodei, new_SBO)
+        #             post_event(DidModifyNodesEvent([nodei]))
+        #     else:
+        #         self.main_section.SetValidationState(False, ctrl_SBO, "Not saved: Invalid SBO Term ID (Example: SBO:0000247)")
+        #         return
+         
+        # self.main_section.SetValidationState(True, self.SBO_ctrl.GetId())
+
+        assert self.contiguous
+        ctrl_id = self.size_ctrl.GetId()
+        text = evt.GetString()
+        wh = parse_num_pair(text)
+
+        if wh is not None: #single node selected
+            nodes = get_nodes_by_idx(self.all_nodes, self._selected_idx)
+            min_width = get_setting('min_node_width')
+            min_height = get_setting('min_node_height')
+            size = Vec2(wh)
+            # limit size to be smaller than the compartment
+            compi = nodes[0].comp_idx
+            bounds: Rect
+            if compi == -1:
+                bounds = Rect(Vec2(), self.canvas.realsize)
+            else:
+                comp = self.canvas.comp_idx_map[compi]
+                bounds = comp.rect
+
+            min_nw = min(n.size.x for n in nodes)
+            min_nh = min(n.size.y for n in nodes)
+            min_ratio = Vec2(min_width / min_nw, min_height / min_nh)
+            min_size = self._bounding_rect.size.elem_mul(min_ratio)
+
+            if size.x < min_size.x or size.y < min_size.y:
+                message = 'The size of {} needs to be at least ({}, {})'.format(
+                    'bounding box' if len(nodes) > 1 else 'node',
+                    no_rzeros(min_size.x, 2), no_rzeros(min_size.y, 2))
+                self.main_section.SetValidationState(False, ctrl_id, message)
+                return
+
+            # if size.x > max_size.x or size.y > max_size.y:
+            #     message = 'The size of bounding box cannot exceed ({}, {})'.format(
+            #         no_rzeros(max_size.x, 2), no_rzeros(max_size.y, 2))
+            #     self.main_section.SetValidationState(False, ctrl_id, message)
+            #     return
+
+            # NOTE clamp max size automatically rather than show error
+            clamped = size.reduce2(min, bounds.size)
+            if self._bounding_rect.size != clamped or size != clamped:
+                ratio = clamped.elem_div(self._bounding_rect.size)
+                self.self_changes = True
+                with self.controller.group_action():
+                    offsets = list()
+                    for node in nodes:
+                        rel_pos = node.position - self._bounding_rect.position
+                        new_pos = self._bounding_rect.position + rel_pos.elem_mul(ratio)
+                        offsets.append(new_pos - node.position)
+                        node.position = new_pos
+                        node.size = node.size.elem_mul(ratio)
+                        # clamp so that nodes are always within compartment/bounds
+                        node.position = clamp_rect_pos(node.rect, bounds)
+
+                    idx_list = list(self._selected_idx)
+                    post_event(DidMoveNodesEvent(idx_list, offsets, dragged=False))
+                    post_event(DidResizeNodesEvent(idx_list, ratio=ratio, dragged=False))
+                    for node in nodes:
+                        self.controller.move_node(self.net_index, node.index, node.position)
+                        self.controller.set_node_size(self.net_index, node.index, node.size)
+        else: #hw is none
+            nodes = get_nodes_by_idx(self.all_nodes, self._selected_idx)
+            self.self_changes = True
+            with self.controller.group_action():
+                hws = text.split("; ")
+                for i in range(len(hws)):
+                    hw = hws[i][1:-1].split(", ")
+                    if len(hw) != 2: #not in the format of "(w1, h1);(w2, h2)" either
+                        self.main_section.SetValidationState(
+                        False, ctrl_id, 'Should be in the form of "width, height" or "(w1, h1); (w2, h2)"')   
+                        return
+                    try:
+                        self.controller.set_node_size(self.net_index, i, Vec2(float(hw[0]), float(hw[1])))
+                    except:
+                        self.main_section.SetValidationState(
+                        False, ctrl_id, 'Should be in the form of "width, height" or "(w1, h1); (w2, h2)"')   
+                        return
+
+        self.main_section.SetValidationState(True, self.size_ctrl.GetId())
+
     def OnNodeStatusChoice(self, evt):
         """Callback for the change node status, floating or boundary."""
         selected = self.nodeStatusDropDown.GetSelection()
         if selected == 0:
             floatingStatus = True
         else:
             floatingStatus = False
@@ -1130,15 +1277,15 @@
                     self.controller.set_node_shape_index(self.net_index, node.index, shapei)
 
             post_event(DidModifyNodesEvent(list(self._selected_idx)))
 
         self._UpdatePrimitiveFields()
 
     def OnNodeLockCheckBox(self, evt):
-        """Callback for the change node status, floating or boundary."""
+        """Callback for the change node lock or not."""
         cb = evt.GetEventObject()
         if cb.GetValue():
             nodeLocked = True
         else:
             nodeLocked = False
 
         nodes = get_nodes_by_idx(self.all_nodes, self._selected_idx)
@@ -1197,33 +1344,42 @@
         conc_text: str
         floatingNode: bool
         lockNode: bool
         shape_name: str
 
         if not self.contiguous:
             self.pos_ctrl.ChangeValue('?')
-            self.size_ctrl.ChangeValue('?')
+            #self.size_ctrl.ChangeValue('?')
         else:
             ChangePairValue(self.pos_ctrl, self._bounding_rect.position, prec)
-            ChangePairValue(self.size_ctrl, self._bounding_rect.size, prec)
+            #ChangePairValue(self.size_ctrl, self._bounding_rect.size, prec)
+
+        if not self.contiguous:
+            self.size_ctrl.ChangeValue('?')
 
         if len(self._selected_idx) == 1:
             [node] = nodes
             self.id_ctrl.Enable(True)
             id_text = node.id
             self.comp_ctrl.Enable(False)
             #comp_text = str(node.comp_idx)
             allCompartments = api.get_compartments(self.net_index)
             comp_id = ''
             for comp in allCompartments:
                 if comp.index == node.comp_idx:
                     comp_id = comp.id
             comp_text = str(comp_id)
+            self.name_ctrl.Enable(True)
+            name_text = str(node.node_name)
+            self.SBO_ctrl.Enable(True)
+            SBO_text = str(node.node_SBO)
             self.conc_ctrl.Enable(True)
             conc_text = str(node.concentration)
+            self.size_ctrl.Enable(True)
+            size_text = str(node.size[0]) + ", " + str(node.size[1])
             floatingNode = node.floatingNode
             lockNode = node.lockNode
             assert node.composite_shape is not None
             shape_name = node.composite_shape.name
         else:
             self.id_ctrl.Enable(False)
             id_text = '; '.join(sorted(list(n.id for n in nodes)))
@@ -1233,31 +1389,40 @@
             for n in nodes:
                 comp_id = ''
                 for comp in allCompartments:
                     if comp.index == n.comp_idx:
                         comp_id = comp.id
                 comp_list.append(str(comp_id))
             comp_text = '; '.join(sorted(comp_list))
+            self.name_ctrl.Enable(False)
+            name_text = '; '.join(sorted(list(str(n.node_name) for n in nodes)))
+            self.SBO_ctrl.Enable(False)
+            SBO_text = '; '.join(sorted(list(str(n.node_SBO) for n in nodes)))
             self.conc_ctrl.Enable(False)
             conc_text = '; '.join(sorted(list(str(n.concentration) for n in nodes)))
+            self.size_ctrl.Enable(True)
+            size_text = '; '.join(sorted(list(str(n.size) for n in nodes)))
             floatingNode = all(n.floatingNode for n in nodes)
             lockNode = all(n.lockNode for n in nodes)
             shape_name_set = set(n.composite_shape.name for n in nodes)
             if len(shape_name_set) == 1:
                 shape_name = next(iter(shape_name_set))
             else:
                 shape_name = ''
 
         self._UpdatePrimitiveFields()
         self.pos_ctrl.Enable(self.contiguous)
         self.size_ctrl.Enable(self.contiguous)
 
         self.id_ctrl.ChangeValue(id_text)
         self.comp_ctrl.ChangeValue(comp_text)
+        self.name_ctrl.ChangeValue(name_text)
+        self.SBO_ctrl.ChangeValue(SBO_text)
         self.conc_ctrl.ChangeValue(conc_text)
+        self.size_ctrl.ChangeValue(size_text)
 
         if floatingNode:
             self.nodeStatusDropDown.SetSelection(0)
         else:
             self.nodeStatusDropDown.SetSelection(1)
 
         if lockNode:
```

### Comparing `sbcoyote-1.3.6/rkviewer/iodine.py` & `sbcoyote-1.3.7/rkviewer/iodine.py`

 * *Files 1% similar despite different names*

```diff
@@ -93,15 +93,16 @@
     rectSize: Vec2
     floating : bool  # If false it means the node is a boundary node
     nodeLocked: bool #if false it means the node can be moved
     compi: int = -1
     shapei: int = 0
     shape: CompositeShape = field(default_factory=lambda: shapeFactories[0].produce())
     concentration: float = 0.0
-
+    node_name: str = ''
+    node_SBO: str = ''
 
 @dataclass
 class TAliasNode(TAbstractNode):
     index: int
     position: Vec2
     rectSize: Vec2
     originalIdx: int
@@ -582,15 +583,17 @@
 def _pushUndoStack():
     global stackFlag, errCode, networkDict, undoStack, redoStack
     if stackFlag:
         redoStack = TStack()
         undoStack.push(networkDict)
 
 
-def addNode(neti: int, nodeID: str, x: float, y: float, w: float, h: float, floatingNode: bool = True, nodeLocked: bool = False) -> int:
+def addNode(neti: int, nodeID: str, x: float, y: float, w: float, h: float, 
+            floatingNode: bool = True, nodeLocked: bool = False, 
+            nodeName: str = '', nodeSBO: str = '') -> int:
     """
     AddNode adds a node to the network
     errCode - 3: id repeat, 0: ok
     -5: net index out of range
     -12: Variable out of range
     """
     global stackFlag, errCode, networkDict, undoStack, redoStack
@@ -600,15 +603,16 @@
         if isinstance(node, TNode) and node.id == nodeID:
             _raiseError(-3)
 
     if x < 0 or y < 0 or w <= 0 or h <= 0:
         _raiseError(-12)
 
     _pushUndoStack()
-    newNode = TNode(n.lastNodeIdx, nodeID, Vec2(x, y), Vec2(w, h), floatingNode, nodeLocked)
+    newNode = TNode(n.lastNodeIdx, nodeID, Vec2(x, y), Vec2(w, h), 
+                    floatingNode, nodeLocked, nodeName, nodeSBO)
     return n.addNode(newNode)
 
 
 def addAliasNode(neti: int, originalIdx: int, x: float, y: float, w: float, h: float) -> int:
     net = _getNetwork(neti)
 
     # make sure we can get it
@@ -832,28 +836,61 @@
             return (X, Y)
 
     raise ExceptionDict[errCode](errorDict[errCode])
 
 
 def getNodeID(neti: int, nodei: int):
     """
-    GetNodeID Get the id of the node
+    GetNodeID: Get the id of the node
     errCode: -7: node index out of range
     -5: net index out of range
     """
     global stackFlag, errCode, networkDict, undoStack, redoStack
     errCode = 0
     if neti not in networkDict:
         errCode = -5
     else:
         node = _getConcreteNode(neti, nodei)
         return node.id
 
     raise ExceptionDict[errCode](errorDict[errCode])
 
+def getNodeName(neti: int, nodei: int):
+    """
+    GetNodeName: Get the name of the node
+    errCode: -7: node index out of range
+    -5: net index out of range
+    """
+    global stackFlag, errCode, networkDict, undoStack, redoStack
+    errCode = 0
+    if neti not in networkDict:
+        errCode = -5
+    else:
+        node = _getConcreteNode(neti, nodei)
+        return node.node_name
+
+    raise ExceptionDict[errCode](errorDict[errCode])
+
+
+def getNodeSBO(neti: int, nodei: int):
+    """
+    GetNodeSBO: Get the SBO of the node
+    errCode: -7: node index out of range
+    -5: net index out of range
+    """
+    global stackFlag, errCode, networkDict, undoStack, redoStack
+    errCode = 0
+    if neti not in networkDict:
+        errCode = -5
+    else:
+        node = _getConcreteNode(neti, nodei)
+        return node.node_SBO
+
+    raise ExceptionDict[errCode](errorDict[errCode])
+
 def getNodeConcentration(neti: int, nodei: int):
     """
     GetNodeConcentration - get the concentration of the node
     errcode:
         -7: node index out of range
         -5: net index out of range
     """
@@ -1064,14 +1101,54 @@
                 errCode = -3
             else:
                 _pushUndoStack()
                 _getConcreteNode(neti, nodei).id = newID
                 return
     raise ExceptionDict[errCode](errorDict[errCode])
 
+def setNodeName(neti: int, nodei: int, newName: str):
+    """
+    setNodeName set the name of a node
+    -5: net index out of range
+    -7: node index out of range
+    """
+    global stackFlag, errCode, networkDict, undoStack, redoStack
+    errCode = 0
+    if neti not in networkDict:
+        errCode = -5
+    else:
+        net = networkDict[neti]
+        if nodei not in net.nodes.keys():
+            errCode = -7
+        else:
+            _pushUndoStack()
+            _getConcreteNode(neti, nodei).node_name = newName
+            return
+    raise ExceptionDict[errCode](errorDict[errCode])
+
+def setNodeSBO(neti: int, nodei: int, newSBO: str):
+    """
+    setNodeSBO set the name of a node
+    -5: net index out of range
+    -7: node index out of range
+    """
+    global stackFlag, errCode, networkDict, undoStack, redoStack
+    errCode = 0
+    if neti not in networkDict:
+        errCode = -5
+    else:
+        net = networkDict[neti]
+        if nodei not in net.nodes.keys():
+            errCode = -7
+        else:
+            _pushUndoStack()
+            _getConcreteNode(neti, nodei).node_SBO = newSBO
+            return
+    raise ExceptionDict[errCode](errorDict[errCode])
+
 def setNodeConcentration(neti: int, nodei: int, newConc: float):
     """
     setNodeConcentration - sets the concentration of a node
     errCode -5: net index out of range
             -7: node index out of range
             -12: variable out of range
     """
@@ -2243,16 +2320,17 @@
     """Return the compartment index that the given node is in, or -1 if it is not in any."""
     return _getNodeOrAlias(neti, nodei).compi
 
 
 def setCompartmentOfNode(neti: int, nodei: int, compi: int):
     """Set the compartment of the node, or remove it from any compartment if -1 is given."""
     net = _getNetwork(neti)
-
     node = _getNodeOrAlias(neti, nodei)
+    if node.compi == '':
+        node.compi = -1
     _pushUndoStack()
     if node.compi != -1:
         net.compartments[node.compi].node_indices.remove(nodei)
     else:
         net.baseNodes.remove(nodei)
 
     if compi != -1:
```

### Comparing `sbcoyote-1.3.6/rkviewer/json/dark-settings.json` & `sbcoyote-1.3.7/rkviewer/json/dark-settings.json`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/json/default-settings.json` & `sbcoyote-1.3.7/rkviewer/json/default-settings.json`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/json/settings.json` & `sbcoyote-1.3.7/rkviewer/json/settings.json`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/main.py` & `sbcoyote-1.3.7/rkviewer/main.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/mvc.py` & `sbcoyote-1.3.7/rkviewer/mvc.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/plugin/api.py` & `sbcoyote-1.3.7/rkviewer/plugin/api.py`

 * *Files 2% similar despite different names*

```diff
@@ -67,39 +67,43 @@
                             means that this Node is not currently part of a network.
         id:             Node ID. Note: NOT constant; see `index` for constant identifiers.
         net_index:      The index of the network that this node is in.
         position:       The top-left position of the node bounding box as (x, y).
         size:           The size of the node bounding box as (w, h).
         comp_idx:       The index of the compartment that this node is in, or -1 if it is in the base
                             compartment.
-        floating_node:   Set true if you want the node to have floating status or false for boundary
+        floating_node:  Set true if you want the node to have floating status or false for boundary
                             status (default is floating)
-        lock_node:       Set false if you want the node to move or true for block (default is false)
+        lock_node:      Set false if you want the node to move or true for block (default is false)
         original_index: If this is an alias node, this is the index of the original node. Otherwise
                             this is -1.
         shape_index:    The composite shape index of the node. 0 for rectangle, 1 for circle, and
                             so on. For the full list of shapes, view iodine.py
         shape:          The CompositeShape object of the node. This is guaranteed to match the shape
                             as indicated by shape_index. This field is present for convenient access
                             of the shape's properties, including the primitives contained within and
                             the properties of the primitive.
-        concentration: The concentration of the node. Default to zero, must not be negative
+        concentration:  The concentration of the node. Default to zero, must not be negative.
+        node_name:      The name of the node.
+        node_SBO:       The SBO of the node.
     """
     net_index: int = field()
     id: str = field()
     position: Vec2 = field(default=Vec2())
     size: Vec2 = field(default=Vec2())
     comp_idx: int = field(default=-1)
     index: int = field(default=-1)
     floating_node: bool = field(default=True)
     lock_node: bool = field(default=False)
     original_index: int = field(default=-1)
     shape_index: int = field(default=0)
     shape: CompositeShape = field(default_factory=DEFAULT_SHAPE_FACTORY.produce)
     concentration: float = field(default=0.0)
+    node_name: str = field(default='')
+    node_SBO: str = field(default='')
 
     @property
     def bounding_rect(self) -> Rect:
         return Rect(self.position, self.size)
 
 
 # @require_kwargs_on_init
@@ -301,15 +305,17 @@
         comp_idx=node.comp_idx,
         index=node.index,
         floating_node=node.floatingNode,
         lock_node=node.lockNode,
         original_index=node.original_index,
         shape_index=node.shape_index,
         shape=copy.copy(node.composite_shape),
-        concentration=node.concentration
+        concentration=node.concentration,
+        node_name = node.node_name,
+        node_SBO = node.node_SBO
     )
 
 
 def _translate_reaction(reaction: Reaction) -> ReactionData:
     """Translate Reaction (internal data structure for rkviewer) to ReactionData (for API)"""
     return ReactionData(
         id=reaction.id,
@@ -631,31 +637,34 @@
         border_width=border_width,
         index=-1
     )
     return _controller.add_compartment_g(net_index, compartment)
 
 
 def add_node(net_index: int, id: str, fill_color: Color = None, border_color: Color = None,
-             border_width: float = None, position: Vec2 = None, size: Vec2 = None,
+             border_width: float = None, position: Vec2 = None, size: Vec2 = None, comp_idx: int = -1,
              floating_node: bool = True, lock_node: bool = False, shape_index: int = 0,
-             concentration: float = 0.0) -> int:
+             concentration: float = 0.0, node_name: str = '', node_SBO: str = '') -> int:
     """Adds a node to the given network.
 
     The node indices are assigned in increasing order, regardless of deletion.
 
     Args:
         net_index: The network index.
         id: The ID of the node.
         fill_color: The fill color of the node, or leave as None to use current theme.
         border_color: The border color of the node, or leave as None to use current theme.
         border_width: The border width of the node, or leave as None to use current theme.
         position: The position of the node, or leave as None to use default, (0, 0).
         size: The size of the node, or leave as None to use default, (0, 0).
+        comp_idx: The index of the compartment that the node is in, default as -1.
         shape_index: The index of the CompositeShape of the node. 0 (rectangle) by default.
         concentration: The concentration of the node, or leave as None to use default, 0.0.
+        node_name: The name of the node.
+        node_SBO: The SBO of the node.
 
     Returns:
         The index of the node that was added.
     """
     if fill_color is None:
         fill_color = _to_color(get_theme('node_fill'))
 
@@ -675,24 +684,29 @@
         id,
         net_index,
         pos=position,
         size=size,
         floatingNode=floating_node,
         lockNode=lock_node,
         shape_index=shape_index,
-        concentration=concentration
+        concentration=concentration,
+        node_name = node_name,
+        node_SBO = node_SBO,
+        comp_idx = comp_idx
     )
     with group_action():
         nodei = _controller.add_node_g(net_index, node)
         _controller.set_node_fill_rgb(net_index, nodei, _to_wxcolour(fill_color))
         _controller.set_node_fill_alpha(net_index, nodei, fill_color.a)
         _controller.set_node_border_rgb(net_index, nodei, _to_wxcolour(border_color))
         _controller.set_node_border_alpha(net_index, nodei, border_color.a)
         _controller.set_node_border_width(net_index, nodei, border_width)
         _controller.set_node_concentration(net_index, nodei, concentration)
+        _controller.set_node_name(net_index, nodei, node_name)
+        _controller.set_node_SBO(net_index, nodei, node_SBO)
     return nodei
 
 
 def add_alias(net_index: int, original_index: int, position: Vec2 = None, size: Vec2 = None):
     """Adds an alias node to the network.
 
     The node indices are assigned in increasing order, regardless of deletion.
@@ -733,15 +747,16 @@
 # TODO add "cosmetic" versions of these functions, where changes made to _controller are not added
 # to the history stack. This requires _controller to have "programmatic group" feature, i.e. actions
 # performed inside such groups are not recorded. programmatic groups nested within group operations
 # should be ignored.
 def update_node(net_index: int, node_index: int, id: str = None, fill_color: Color = None,
                 border_color: Color = None, border_width: float = None, position: Vec2 = None,
                 size: Vec2 = None, floating_node: bool = True, lock_node: bool = False,
-                shape_index: int = None, concentration: float = None):
+                shape_index: int = None, concentration: float = None, node_name: str = None,
+                node_SBO: str = None):
     """
     Update one or multiple properties of a node.
 
     Args:
         net_index: The network index.
         node_index: The node index of the node to modify.
         id: If specified, the new ID of the node.
@@ -750,14 +765,16 @@
         border_width: If specified, the new border width of the node.
         position: If specified, the new position of the node.
         size: If specified, the new size of the node.
         floating_node: If specified, the floating status of the node.
         lock_node: If specified, whether the node is locked.
         shape_index: If specified, the new shape of the node.
         concentration: If specified, the new concentration of the node.
+        node_name: If specified, the new node name.
+        node_SBO: If specified, the new node SBO.
 
     Note:
         This is *not* an atomic function, meaning if we failed to set one specific property, the
         previous changes to model in this function will not be undone, even after the exception
         is caught. To go around that, make one calls to update_node() for each property instead.
 
         Also note the behavior if the given node_index refers to an alias node.
@@ -825,14 +842,19 @@
 
         if concentration is not None:
             if concentration < 0.0:
                 raise ValueError('Invalid concentration value. Concentration must not be negative.')
             else:
                 _controller.set_node_concentration(net_index, node_index, concentration)
 
+        if node_name is not None:
+            _controller.set_node_name(net_index, node_index, node_name)
+        if node_SBO is not None:
+            _controller.set_node_SBO(net_index, node_index, node_SBO)
+
 
 def set_node_shape_property(net_index: int, node_index: int, primitive_index: int,
                             prop_name: str, prop_value: Any):
     '''Set a property of the node's composite shape, e.g. fill color.
 
     NOTE specify -1 for `primitive_index` to modify the text primitive of the node.
```

### Comparing `sbcoyote-1.3.6/rkviewer/plugin/canvas.py` & `sbcoyote-1.3.7/rkviewer/plugin/canvas.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/plugin/classes.py` & `sbcoyote-1.3.7/rkviewer/plugin/classes.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/plugin_manage.py` & `sbcoyote-1.3.7/rkviewer/plugin_manage.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/resources/alignRight_XP.png` & `sbcoyote-1.3.7/rkviewer/resources/alignRight_XP.png`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/utils.py` & `sbcoyote-1.3.7/rkviewer/utils.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer/view.py` & `sbcoyote-1.3.7/rkviewer/view.py`

 * *Files 5% similar despite different names*

```diff
@@ -29,14 +29,18 @@
                      DidResizeNodesEvent, SelectionDidUpdateEvent,
                      bind_handler)
 from .forms import CompartmentForm, NodeForm, ReactionForm
 from .mvc import IController, IView
 from .utils import ButtonGroup, on_msw, resource_path, start_file
 from rkviewer.config import AppSettings
 
+from rkviewer_plugins import importSBML
+from rkviewer_plugins import exportSBML
+
+from rkviewer_plugins import addReaction
 
 class EditPanel(fnb.FlatNotebook):
     """Panel that displays and allows editing of the details of a node.
 
     Attributes
         node_form: The actual form widget. This is at the same level as null_message. TODO
         null_message: The widget displayed in place of the form,  when nothing is selected.
@@ -247,16 +251,17 @@
         file_tb.AppendTool('Details', edit_panel_callback,
                            wx.ArtProvider.GetBitmap(wx.ART_HELP_SIDE_PANEL, wx.ART_MENU))
         self.AddPage(file_tb, text='Main')
 
     def AddPluginPages(self):
         categories = self.manager.get_plugins_by_category()
         for cat in PluginCategory:
-            if len(categories[cat]) == 0:
-                continue
+            # do not show the plugin categories if no valid plugin example available
+            # if len(categories[cat]) == 0:
+            #     continue
 
             tb = Toolbar(self)
             for name, callback, bitmap in categories[cat]:
                 if bitmap is None:
                     #bitmap = wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE, wx.ART_MENU)
                     bitmap = wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_MENU)
                 tb.AppendTool(name, callback, bitmap)
@@ -290,14 +295,17 @@
         self.AppendNormalButton('Reactants', canvas.MarkSelectedAsReactants,
                                 sizer, tooltip='Mark selected nodes as reactants')
         self.AppendNormalButton('Products', canvas.MarkSelectedAsProducts,
                                 sizer, tooltip='Mark selected nodes as products')
         self.AppendNormalButton('Create Rxn', canvas.CreateReactionFromMarked,
                                 sizer, tooltip='Create reaction from marked reactants and products')
 
+        # self.AppendSeparator(sizer)
+        # self.AppendToggleButtonUniUni('UniUni', sizer, tooltip='Add a UniUni reaction')
+
         self.SetSizer(sizer)
 
     def AppendModeButton(self, label: str, mode: InputMode, sizer: wx.Sizer):
         if get_theme ('btn_border'):
             btn = wx.ToggleButton(self, label=label)
         else:
             btn = wx.ToggleButton(self, label=label, style=wx.BORDER_NONE)
@@ -330,16 +338,31 @@
         btn.SetBackgroundColour(get_theme ('btn_bg'))
         btn.SetForegroundColour(get_theme ('btn_fg'))
         if tooltip is not None:
             btn.SetToolTip(tooltip)
         btn.Bind(wx.EVT_BUTTON, lambda _: callback())
         sizer.Add(btn, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.TOP, 10))
 
+    def AppendToggleButtonUniUni(self, label: str, sizer: wx.Sizer, tooltip: str = None):
+
+        if get_theme ('btn_border'):
+           btn = wx.ToggleButton(self, label=label)
+        else:
+           btn = wx.ToggleButton(self, label=label, style=wx.BORDER_NONE)
+
+        btn.SetBackgroundColour(get_theme ('btn_bg'))
+        btn.SetForegroundColour(get_theme ('btn_fg'))
+        if tooltip is not None:
+            btn.SetToolTip(tooltip)
+        btn.Bind(wx.EVT_TOGGLEBUTTON, addReaction.AddReaction._UniUni(self))
+        sizer.Add(btn, wx.SizerFlags().Align(wx.ALIGN_CENTER).Border(wx.TOP, 10))
+
     def AppendSeparator(self, sizer: wx.Sizer):
         sizer.Add((0, 10))
+    
 
 
 class BottomBar(wx.Panel):
     def __init__(self, parent):
         super().__init__(parent)
         self.SetForegroundColour(get_theme('toolbar_fg'))
         self.SetBackgroundColour(get_theme('toolbar_bg'))
@@ -512,14 +535,21 @@
         # TODO Load Recent...
         file_menu.AppendSeparator()
         self.save_item = self.AddMenuItem(file_menu, '&Save', 'Save current network as a JSON file',
                                           lambda _: self.SaveJson(), entries, key=(wx.ACCEL_CTRL, ord('S')))
         self.save_item.Enable(False)
         self.AddMenuItem(file_menu, '&Save As...', 'Save current network as a JSON file',
                          lambda _: self.SaveAsJson(), entries, key=(wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('N')))
+        #Import SBML
+        file_menu.AppendSeparator()
+        self.AddMenuItem(file_menu, '&Import SBML', 'Import SBML',
+                         lambda _: self.ImportSBML(),  entries, key=(wx.ACCEL_CTRL, ord('I')))
+        #Emport SBML
+        self.AddMenuItem(file_menu, '&Export SBML', 'Export SBML',
+                         lambda _: self.ExportSBML(),  entries, key=(wx.ACCEL_CTRL, ord('E')))
         file_menu.AppendSeparator()
         self.AddMenuItem(file_menu, '&Edit Settings', 'Edit settings',
                          lambda _: self.EditSettings(),  entries)
         self.AddMenuItem(file_menu, '&Reload Settings', 'Reload settings',
                          lambda _: self.ReloadSettings(),  entries)
         file_menu.AppendSeparator()
         align_menu = wx.Menu()
@@ -557,14 +587,16 @@
         select_menu = wx.Menu()
         self.AddMenuItem(select_menu, 'Select &All', 'Select all',
                          lambda _: canvas.SelectAll(), entries, key=(wx.ACCEL_CTRL, ord('A')))
         self.AddMenuItem(select_menu, 'Select All &Nodes', 'Select all nodes',
                          lambda _: canvas.SelectAllNodes(), entries, key=(wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('N')))
         self.AddMenuItem(select_menu, 'Select All &Reactions', 'Select all reactions',
                          lambda _: canvas.SelectAllReactions(), entries, key=(wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('R')))
+        self.AddMenuItem(select_menu, 'Select All &Compartments', 'Select all compartments',
+                         lambda _: canvas.SelectAllCompartments(), entries, key=(wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('C')))
         self.AddMenuItem(select_menu, 'Clear Selection', 'Clear the current selection',
                          lambda _: canvas.ClearCurrentSelection(), entries,
                          key=(wx.ACCEL_NORMAL, wx.WXK_ESCAPE))
 
         view_menu = wx.Menu()
         self.AddMenuItem(view_menu, 'Zoom &In', 'Zoom in canvas', lambda _: canvas.ZoomCenter(True),
                          entries, key=(wx.ACCEL_CTRL, ord('+')))
@@ -664,25 +696,66 @@
         self.Bind(wx.EVT_MENU, callback, item)
         self.menu_events.append((callback, item))
         return item
 
     def onAboutDlg(self, event):
         info = wx.adv.AboutDialogInfo()
         info.SetName("SBcoyote")
-        info.SetVersion("1.3.6")
+        info.SetVersion("1.3.7")
         info.SetCopyright("(c) 2023 UW Sauro Lab")
         info.SetDescription("An Extensible Python-Based Reaction Editor and Viewer.")
         info.SetWebSite("https://github.com/sys-bio/SBcoyote",
                         "Home Page")  # TODO update home page?
         info.SetDevelopers(["Jin Xu", "Gary Geng", "Nhan D. Nguyen", "Carmen Perena-Corte","Claire Samuels", "Herbert M. Sauro"])# TODO update authors
         info.SetLicense("MIT")
 
         # Show the wx.AboutBox
         wx.adv.AboutBox(info)
 
+    def ImportSBML(self):
+        """Import SBML files."""
+        
+        self.dirname=""  #set directory name to blank
+        dlg = wx.FileDialog(self, "Choose a file to open", self.dirname, wildcard="SBML files (*.xml)|*.xml", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) #open the dialog boxto open file
+        if dlg.ShowModal() == wx.ID_OK:  #if positive button selected....
+            self.filename = dlg.GetFilename()  #get the filename of the file
+            self.dirname = dlg.GetDirectory()  #get the directory of where file is located
+            f = open(os.path.join(self.dirname, self.filename), 'r')  #traverse the file directory and find filename in the OS
+            self.sbmlStr = f.read()
+            with wx.BusyCursor():
+            #with wx.BusyInfo("Please wait, working..."):
+                importSBML.IMPORTSBML.DisplayModel(self, self.sbmlStr, True, False)
+                f.close
+        dlg.Destroy()
+
+    def ExportSBML(self):
+        """Export SBML files."""
+        sbmlStr_layout_render = exportSBML.ExportSBML.NetworkToSBML(self)
+        if sbmlStr_layout_render is None:
+            wx.MessageBox("No valid SBML string to export or save!", "Error")
+        else:
+            try:
+                #save to local
+                self.dirname=""  #set directory name to blank 
+                dlg = wx.FileDialog(self, "Save As", self.dirname, wildcard="SBML files (*.xml)|*.xml", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
+                if dlg.ShowModal() == wx.ID_OK:
+                    # Grab the content to be saved
+                    #itcontains = self.SBMLText.GetValue()
+                    itcontains = sbmlStr_layout_render
+                    # Open the file for write, write, close
+                    self.filename=dlg.GetFilename()
+                    self.dirname=dlg.GetDirectory()
+                    filehandle=open(os.path.join(self.dirname, self.filename),'w')
+                    filehandle.write(itcontains)
+                    filehandle.close()
+                # Get rid of the dialog to keep things tidy
+                dlg.Destroy()
+            except:
+                wx.MessageBox("No valid SBML string to export or save!", "Error")
+
     def ReloadSettings(self):
         load_theme_settings()
         err = pop_settings_err()
         if err is None:
             # msg = NotificationMessage('Settings reloaded', 'Some changes may not be applied until the application is restarted.')
             # msg.Show()
             pass
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/addReaction.py` & `sbcoyote-1.3.7/rkviewer_plugins/addReaction.py`

 * *Files 2% similar despite different names*

```diff
@@ -193,14 +193,30 @@
          self.bibiState = False
          self.BiUni_btn.SetValue (False)
          self.UniBi_btn.SetValue (False)
          self.BiBi_btn.SetValue (False)            
       else:
          self.uniuniState = False
 
+   def _UniUni(self, state = True):
+      """
+      Handler for the "UniUni" button in view.py.
+      """
+
+      if state == True:  
+         self.src = []
+         self.dest = []
+         # This code is to make the buttons work as a radionbutton
+         self.uniuniState = True
+         self.biuniState = False
+         self.unibiState = False
+         self.bibiState = False
+      else:
+         self.uniuniState = False
+
    def BiUni(self, evt):
       """
       Handler for the "BiUni" button. add a BiUni reaction.
       """
       state = evt.GetEventObject().GetValue()
       if state == True:  
          self.src = []
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/align_circle.py` & `sbcoyote-1.3.7/rkviewer_plugins/align_circle.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 class AlignCircle(WindowedPlugin):
     metadata = PluginMetadata(
         name='AlignCircle',
         author='Evan Yip and Jin Xu',
         version='1.0.0',
         short_desc='Align Circle',
         long_desc='Aligns the nodes into a circle',
-        category=PluginCategory.UTILITIES
+        category=PluginCategory.VISUALIZATION
     )
 
     def __init__(self):
         """
         Initialize the AlignCircle
 
         Args:
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/arrow_designer.py` & `sbcoyote-1.3.7/rkviewer_plugins/arrow_designer.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/exportAntimony.py` & `sbcoyote-1.3.7/rkviewer_plugins/exportAntimony.py`

 * *Files 0% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 class ExportAntimony(WindowedPlugin):
     metadata = PluginMetadata(
         name='ExportAntimony',
         author='Jin Xu',
         version='1.0.0',
         short_desc='Export Antimony.',
         long_desc='Export the Antimony String from the network on canvas.',
-        category=PluginCategory.ANALYSIS
+        category=PluginCategory.MODELS
     )
 
     def create_window(self, dialog):
         """
         Create a window to do the antimony export.
         Args:
             self
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/exportSBML.py` & `sbcoyote-1.3.7/rkviewer_plugins/exportSBML.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 """
 Export the network on canvas to an SBML string as save it as a file.
-Version 1.0.4: Author: Jin Xu (2023)
+Version 1.0.6: Author: Jin Xu (2023)
 """
 
 
 # pylint: disable=maybe-no-member
 
 from inspect import Parameter
 import wx
@@ -16,18 +16,18 @@
 from libsbml import * # does not have to import in the main.py too
 import re # to process kinetic_law string
 
 class ExportSBML(WindowedPlugin):
     metadata = PluginMetadata(
         name='ExportSBML',
         author='Jin Xu',
-        version='1.0.4',
+        version='1.0.6',
         short_desc='Export SBML.',
         long_desc='Export the SBML String from the network on canvas and save it to a file.',
-        category=PluginCategory.ANALYSIS
+        category=PluginCategory.MODELS
     )
 
 
     def create_window(self, dialog):
         """
         Create a window to export the SBML.
         Args:
@@ -85,15 +85,15 @@
                 self.dirname=dlg.GetDirectory()
                 filehandle=open(os.path.join(self.dirname, self.filename),'w')
                 filehandle.write(itcontains)
                 filehandle.close()
             # Get rid of the dialog to keep things tidy
             dlg.Destroy()
         except:
-            wx.MessageBox("No valid SBML string to save!", "Error")
+            wx.MessageBox("No valid SBML string to export or save!", "Error")
 
 
     def NetworkToSBML(self):
         """
         Get the network on canvas and change it to an SBML string
         """
 
@@ -178,15 +178,16 @@
 
         isReversible = True
         netIn = 0
         numNodes = api.node_count(netIn)
         numReactions = api.reaction_count(netIn)
         
         if numNodes == 0:
-           wx.MessageBox("Please import a network with at least one node on canvas", "Message", wx.OK | wx.ICON_INFORMATION)
+            pass
+            #wx.MessageBox("There are no nodes on canvas to export.", "Message", wx.OK | wx.ICON_INFORMATION)
         else:
             allNodes = api.get_nodes(netIn)
             
             allReactions = api.get_reactions(netIn)
             allcompartments = api.get_compartments(netIn)
             #print("allNodes:", allNodes)
             #print("allReactions:", allReactions)
@@ -236,20 +237,24 @@
                     compartment.setConstant(True)
                     compartment.setVolume(1.)
                 spec_id_list = []
                 for i in range(numNodes):
                     original_index = allNodes[i].original_index
                     if original_index == -1:
                         spec_id = allNodes[i].id
+                        spec_name = allNodes[i].node_name
+                        spec_SBO = allNodes[i].node_SBO
                         if ' ' in spec_id:
                             spec_id = spec_id.replace(' ', '_')
                         if spec_id not in spec_id_list:
                             spec_id_list.append(spec_id)
                         species = model.createSpecies()
                         species.setId(spec_id)
+                        species.setName(spec_name)
+                        species.setSBOTerm(spec_SBO)
                         comp_idx = allNodes[i].comp_idx
                         if comp_idx != -1:
                             comp_id = allcompartments[comp_idx].id 
                             species.setCompartment(comp_id)  
                         else:
                             species.setCompartment("_compartment_default_") 
                         species.setInitialConcentration(allNodes[i].concentration)	
@@ -266,20 +271,24 @@
                 compartment.setConstant(True)
                 compartment.setVolume(1.)
                 spec_id_list = []
                 for i in range(numNodes):
                     original_index = allNodes[i].original_index
                     if original_index == -1:
                         spec_id = allNodes[i].id
+                        spec_name = allNodes[i].node_name
+                        spec_SBO = allNodes[i].node_SBO
                         if ' ' in spec_id:
                             spec_id = spec_id.replace(' ', '_')
                         if spec_id not in spec_id_list:
                             spec_id_list.append(spec_id)
                         species = model.createSpecies()
                         species.setId(spec_id)
+                        species.setName(spec_name)
+                        species.setSBOTerm(spec_SBO)
                         species.setCompartment(comp_id)
                         species.setInitialConcentration(allNodes[i].concentration)	
                         species.setHasOnlySubstanceUnits(False)
                         species.setBoundaryCondition(False)
                         species.setConstant(False)             
                         if allNodes[i].floating_node == False:
                             species.setBoundaryCondition(True)
@@ -405,16 +414,16 @@
 
 
             #
             # Creates a Layout object via LayoutModelPlugin object.
             #
             layout = mplugin.createLayout()
             layout.setId("COYOTO_layout")
-            layout_width = 9900
-            layout_height = 6100
+            layout_width = 10000 - 20
+            layout_height = 6200 - 20
             layout.setDimensions(Dimensions(layoutns, layout_width, layout_height))
             # random network (40+800x, 40+800y)
 
             #create the CompartmentGlyph and SpeciesGlyphs
             if numCompartments != 0:
                 for i in range(numCompartments):   
                     comp_id=allcompartments[i].id
@@ -1120,15 +1129,15 @@
                     color.setColorValue(border_color_str)
                     lineEnding.getGroup().setStroke('lineEnding_border_color' + '_' + lineEnding_id)
 
 
                     for j in range(rct_num):
                         specsRefG_id = "SpecRefG_" + rxn_id + "_rct" + str(j)
                         style = rInfo.createStyle("specRefGlyphStyle" + rxn_id + "_rct" + str(j))
-                        style.getGroup().setEndHead('_line_ending_default_NONE_')
+                        style.getGroup().setEndHead('_line_ending_default_NONE_' + rxn_id)
                         style.getGroup().setStroke("lineEnding_border_color" + "_" + lineEnding_id)
                         style.getGroup().setFill("lineEnding_fill_color" + "_" + lineEnding_id)
                         style.getGroup().setStrokeWidth(reaction_line_thickness)
                         style.addType('SPECIESREFERENCEGLYPH')
                         style.addId(specsRefG_id)
                     
                     ##
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/importSBML.py` & `sbcoyote-1.3.7/rkviewer_plugins/importSBML.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 """
 Import an SBML string from a file and visualize it to a network on canvas.
-Version 1.1.5: Author: Jin Xu (2023)
+Version 1.1.6: Author: Jin Xu (2023)
 """
 
 
 # pylint: disable=maybe-no-member
 
 from ast import Num
 from inspect import Parameter
@@ -23,18 +23,18 @@
 import random as _random
 import pandas as pd
 
 class IMPORTSBML(WindowedPlugin):
     metadata = PluginMetadata(
         name='ImportSBML',
         author='Jin Xu',
-        version='1.1.5',
+        version='1.1.6',
         short_desc='Import SBML.',
         long_desc='Import an SBML String from a file and visualize it as a network on canvas.',
-        category=PluginCategory.ANALYSIS
+        category=PluginCategory.MODELS
     )
 
     def create_window(self, dialog):
         """
         Create a window to import SBML.
         Args:
             self
@@ -135,14 +135,16 @@
             net_index = 0
             api.clear_network(net_index)
             comp_id_list = []
             compGlyph_id_list = []
             comp_dimension_list = []
             comp_position_list = []
             spec_id_list = []
+            spec_name_list = []
+            spec_SBO_list = []
             specGlyph_id_list = []
             spec_specGlyph_id_list = []
             spec_dimension_list = []
             spec_position_list = []
             spec_text_alignment_list = []
             spec_text_position_list = []
             spec_concentration_list = []
@@ -291,14 +293,15 @@
                                         center_pt = []
                                     else:
                                         center_pt = [pos_x+.5*width, pos_y+.5*height]
                                 center_sz = [width, height]
                             except:
                                 pass
 
+                            
                             reaction_center_list.append(center_pt)
                             #reaction_size_list.append(center_sz)
                             
                             reaction_id = reactionGlyph.getReactionId()
                            
                             reaction_id_list.append(reaction_id)
                             reactionGlyph_id_list.append(reactionGlyph_id)
@@ -373,55 +376,90 @@
                                     dist_start_center = math.sqrt((line_start_pt[0]-center_pt[0])*(line_start_pt[0]-center_pt[0])+(line_start_pt[1]-center_pt[1])*(line_start_pt[1]-center_pt[1]))
                                     dist_end_center = math.sqrt((line_end_pt[0]-center_pt[0])*(line_end_pt[0]-center_pt[0])+(line_end_pt[1]-center_pt[1])*(line_end_pt[1]-center_pt[1]))
                                     #if math.sqrt(line_start_pt, center_pt) <= math.dist(line_end_pt, center_pt):
                                     if dist_start_center <= dist_end_center:
                                         #line starts from center
                                         spec_lineend_pos = line_end_pt
                                         modifier_lineend_pos = line_start_pt
-                                        try: #bezier
-                                            if num_curve == 1:
+                                        
+                                        if num_curve == 1:
+                                            try: #bezier
                                                 center_handle_candidate = [segment.getBasePoint1().getXOffset(), 
                                                                 segment.getBasePoint1().getYOffset()]                                
                                                 spec_handle = [segment.getBasePoint2().getXOffset(),
-                                                            segment.getBasePoint2().getYOffset()]
-                                            else:        
+                                                            segment.getBasePoint2().getYOffset()] 
+                                            except: #straight
+                                                spec_handle = [.5*(center_pt[0]+line_end_pt[0]),
+                                                .5*(center_pt[1]+line_end_pt[1])]
+                                                center_handle_candidate = center_pt
+                                                #spec_handle = center_pt         
+                                        else:  
+                                            try: #bezier
+                                                center_handle_candidate = []  
+                                                flag_bezier = 0  
+                                                for segment in curve.getListOfCurveSegments():
+                                                    if segment.getTypeCode() == 102:
+                                                        flag_bezier = 1
                                                 for segment in curve.getListOfCurveSegments():
-                                                    if segment.getTypeCode() == 102: 
+                                                    if flag_bezier == 1: 
                                                         #102 CubicBezier #107LineSegment
-                                                        center_handle_candidate = center_pt                              
-                                                        spec_handle = [segment.getBasePoint2().getXOffset(),
-                                                                segment.getBasePoint2().getYOffset()]
-                                        except: #straight
-                                            spec_handle = [.5*(center_pt[0]+line_end_pt[0]),
-                                            .5*(center_pt[1]+line_end_pt[1])]
-                                            center_handle_candidate = center_pt
-                                            #spec_handle = center_pt
+                                                        if segment.getTypeCode() == 102:
+                                                            spec_handle = [segment.getBasePoint1().getXOffset(), 
+                                                                        segment.getBasePoint1().getYOffset()]                                
+                                                            center_handle_candidate = center_pt
+                                                    else:
+                                                        spec_handle = [.5*(center_pt[0]+line_start_pt[0]),
+                                                        .5*(center_pt[1]+line_start_pt[1])]
+                                                        center_handle_candidate = center_pt
+                                                        #spec_handle = center_pt
+                                            except: #straight
+                                                spec_handle = [.5*(center_pt[0]+line_end_pt[0]),
+                                                .5*(center_pt[1]+line_end_pt[1])]
+                                                center_handle_candidate = center_pt
+                                                #spec_handle = center_pt 
                                     else:
                                         #line starts from species
                                         spec_lineend_pos = line_start_pt
                                         modifier_lineend_pos = line_end_pt
-                                        try: #bezier
-                                            if num_curve == 1:
+                                        
+                                        if num_curve == 1:
+                                            try: #bezier
                                                 spec_handle = [segment.getBasePoint1().getXOffset(), 
                                                                     segment.getBasePoint1().getYOffset()]                                
                                                 center_handle_candidate = [segment.getBasePoint2().getXOffset(),
                                                                 segment.getBasePoint2().getYOffset()]
-                                            else:
+                                            except: #straight
+                                                spec_handle = [.5*(center_pt[0]+line_start_pt[0]),
+                                                .5*(center_pt[1]+line_start_pt[1])]
+                                                center_handle_candidate = center_pt
+                                                #spec_handle = center_pt
+                                        else:
+                                            try: #bezier
+                                                center_handle_candidate = [] 
+                                                flag_bezier = 0  
+                                                for segment in curve.getListOfCurveSegments():
+                                                    if segment.getTypeCode() == 102:
+                                                        flag_bezier = 1
                                                 for segment in curve.getListOfCurveSegments():
-                                                    if segment.getTypeCode() == 102: 
+                                                    if flag_bezier == 1: 
                                                         #102 CubicBezier #107LineSegment
-                                                        spec_handle = [segment.getBasePoint1().getXOffset(), 
-                                                                    segment.getBasePoint1().getYOffset()]                                
+                                                        if segment.getTypeCode() == 102:
+                                                            spec_handle = [segment.getBasePoint1().getXOffset(), 
+                                                                        segment.getBasePoint1().getYOffset()]                                
+                                                            center_handle_candidate = center_pt
+                                                    else:
+                                                        spec_handle = [.5*(center_pt[0]+line_start_pt[0]),
+                                                        .5*(center_pt[1]+line_start_pt[1])]
                                                         center_handle_candidate = center_pt
-                                        except: #straight
-                                            spec_handle = [.5*(center_pt[0]+line_start_pt[0]),
-                                            .5*(center_pt[1]+line_start_pt[1])]
-                                            # center_handle_candidate = center_pt
-                                            center_handle_candidate = center_pt
-                                            #spec_handle = center_pt
+                                                        #spec_handle = center_pt
+                                            except: #straight
+                                                spec_handle = [.5*(center_pt[0]+line_start_pt[0]),
+                                                .5*(center_pt[1]+line_start_pt[1])]
+                                                center_handle_candidate = center_pt
+                                                #spec_handle = center_pt
 
                                 except:
                                     center_handle_candidate = []
                                     spec_handle = []
 
                                 role = specRefGlyph.getRoleString()
                                 specGlyph_id = specRefGlyph.getSpeciesGlyphId()
@@ -444,17 +482,18 @@
                                         textGlyph = textGlyph_temp
                                         text_content = textGlyph.getText()
                                         temp_id = textGlyph.getId()
                                         textGlyph_spec_id_list.append([specGlyph_id, temp_id])
 
 
                                 spec_id = specGlyph.getSpeciesId()
-                                
                                 spec = model_layout.getSpecies(spec_id)
                                 spec_name = spec.getName()
+                                spec_SBO = spec.getSBOTermID()
+                                #print(spec_SBO)
                                 
                                 try:
                                     concentration = spec.getInitialConcentration()
                                     if math.nan(concentration):
                                         concentration = 1
                                 except:
                                     concentration = 1.
@@ -493,14 +532,16 @@
                                    
                                 except:
                                     pass  
                     
 
                                 if specGlyph_id not in specGlyph_id_list:
                                     spec_id_list.append(spec_id)
+                                    spec_name_list.append(spec_name)
+                                    spec_SBO_list.append(spec_SBO)
                                     specGlyph_id_list.append(specGlyph_id)
                                     spec_specGlyph_id_list.append([spec_id,specGlyph_id])
                                     spec_dimension_list.append([width,height])
                                     spec_position_list.append([pos_x,pos_y])
                                     if text_content == '':
                                         if spec_name != '':
                                             text_content = spec_name
@@ -510,18 +551,15 @@
                                     spec_text_alignment_list.append(alignment_name)
                                     spec_text_position_list.append(position_name)
                                     spec_concentration_list.append(concentration)
                                 
                                 if center_handle == []:
                                     center_handle.append(center_handle_candidate)
 
-                                # if reaction_id == "EX_h_e":
-                                #     print(center_pt)
-                                #     print(center_handle_candidate)
-                                #     print(spec_handle)
+                              
                                 if role == "substrate" or role == "sidesubstrate": #it is a rct
                                     #rct_specGlyph_temp_list.append(specGlyph_id)
                                     rct_specGlyph_handles_temp_list.append([specGlyph_id,spec_handle,specRefGlyph_id,spec_lineend_pos])
                                 elif role == "product" or role == "sideproduct": #it is a prd
                                     #prd_specGlyph_temp_list.append(specGlyph_id)
                                     prd_specGlyph_handles_temp_list.append([specGlyph_id,spec_handle,specRefGlyph_id,spec_lineend_pos])
                                 elif role == "modifier" or role == 'activator': #it is a modifier
@@ -540,15 +578,20 @@
                         #orphan nodes
                         for i in range(numSpecGlyphs):
                             specGlyph = layout.getSpeciesGlyph(i)
                             specGlyph_id = specGlyph.getId()
                             if specGlyph_id not in specGlyph_id_list:
                                 specGlyph_id_list.append(specGlyph_id)
                                 spec_id = specGlyph.getSpeciesId()
+                                spec = model_layout.getSpecies(spec_id)
+                                spec_name = spec.getName()
+                                spec_SBO = spec.getSBOTermID()
                                 spec_id_list.append(spec_id)
+                                spec_name_list.append(spec_name)
+                                spec_SBO_list.append(spec_SBO)
                                 spec_specGlyph_id_list.append([spec_id,specGlyph_id])
                                 boundingbox = specGlyph.getBoundingBox()
                                 height = boundingbox.getHeight()
                                 width = boundingbox.getWidth()
                                 pos_x = boundingbox.getX()
                                 pos_y = boundingbox.getY()
                                 spec_dimension_list.append([width,height])
@@ -1228,14 +1271,16 @@
                     nodeIdx_list = [] #get_nodes idx do not follow the same order of add_node
                     nodeIdx_specGlyph_list = []
                     nodeIdx_specGlyph_alias_list = []
                     numSpec_in_reaction = len(spec_specGlyph_id_list) 
                     # orphan nodes have been considered, so numSpec_in_reaction should equals to numSpecGlyphs
                     for i in range (numSpec_in_reaction):
                         temp_id = spec_specGlyph_id_list[i][0]
+                        temp_name = spec_name_list[i]
+                        temp_SBO = spec_SBO_list[i]
                         temp_concentration = spec_concentration_list[i]
                         tempGlyph_id = spec_specGlyph_id_list[i][1]
                         dimension = spec_dimension_list[i]
                         position = spec_position_list[i]
                         text_content = spec_text_content_list[i]
                         # position_abs = [abs(y) for y in position]
                         # position = position_abs
@@ -1297,15 +1342,16 @@
                                     #print(shapeIdx)
                                     
                                     
                                     nodeIdx_temp = api.add_node(net_index, id=temp_id, floating_node = True,
                                     size=Vec2(dimension[0],dimension[1]), position=Vec2(position[0],position[1]),
                                     fill_color=api.Color(spec_fill_color[0],spec_fill_color[1],spec_fill_color[2],spec_fill_color[3]),
                                     border_color=api.Color(spec_border_color[0],spec_border_color[1],spec_border_color[2],spec_border_color[3]),
-                                    border_width=spec_border_width, shape_index=shapeIdx, concentration = temp_concentration)
+                                    border_width=spec_border_width, shape_index=shapeIdx, concentration = temp_concentration,
+                                    node_name = temp_name, node_SBO = temp_SBO)
                                     
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "alignment", text_alignment)
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "position", text_position)
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "font_color", 
                                     api.Color(text_line_color[0], text_line_color[1], text_line_color[2], text_line_color[3]))
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "font_size", int(text_font_size))
                                     id_list.append(temp_id)
@@ -1382,15 +1428,16 @@
                                     if len(text_line_color) == 3:
                                         text_line_color.append(255)
                                     
                                     nodeIdx_temp = api.add_node(net_index, id=temp_id, floating_node = False,
                                     size=Vec2(dimension[0],dimension[1]), position=Vec2(position[0],position[1]),
                                     fill_color=api.Color(spec_fill_color[0],spec_fill_color[1],spec_fill_color[2],spec_fill_color[3]),
                                     border_color=api.Color(spec_border_color[0],spec_border_color[1],spec_border_color[2],spec_border_color[3]),
-                                    border_width=spec_border_width, shape_index=shapeIdx, concentration = temp_concentration)
+                                    border_width=spec_border_width, shape_index=shapeIdx, concentration = temp_concentration,
+                                    node_name = temp_name, node_SBO = temp_SBO)
                                                                             
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "alignment", text_alignment)
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "position", text_position)
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "font_color", 
                                     api.Color(text_line_color[0], text_line_color[1], text_line_color[2], text_line_color[3]))
                                     api.set_node_shape_property(net_index, nodeIdx_temp, -1, "font_size", int(text_font_size))
                                     id_list.append(temp_id)
@@ -1485,20 +1532,15 @@
                                 temp_specGlyph_id = rct_specGlyph_handle_list[i][j][0]
                                 for k in range(numSpec_in_reaction):
                                     if temp_specGlyph_id == nodeIdx_specGlyph_whole_list[k][1]:
                                         rct_idx = nodeIdx_specGlyph_whole_list[k][0]
                                 src.append(rct_idx)
                                 src_handle.append(rct_specGlyph_handle_list[i][j][1])
                                 src_lineend_pos.append(rct_specGlyph_handle_list[i][j][3])
-                            # if temp_id == "EX_h_e":
-                            #     center_position = reaction_center_list[i]
-                            #     center_handle = reaction_center_handle_list[i]
-                                # print(center_position)
-                                # print(center_handle)
-                                # print(src_handle)
+                           
                             
                             for j in range(prd_num):
                                 temp_specGlyph_id = prd_specGlyph_handle_list[i][j][0]
                                 for k in range(numSpec_in_reaction):
                                     if temp_specGlyph_id == nodeIdx_specGlyph_whole_list[k][1]:
                                         prd_idx = nodeIdx_specGlyph_whole_list[k][0]
                                 dst.append(prd_idx)
@@ -1574,32 +1616,30 @@
                             [src_corr.append(x) for x in src if x not in src_corr]
                             dst_corr = []
                             [dst_corr.append(x) for x in dst if x not in dst_corr]
 
                             
                             center_position = reaction_center_list[i] 
                             center_handle = reaction_center_handle_list[i]
-                         
+                        
                             center_position = [center_position[0]-TopLeft[0]-shift[0], center_position[1]-TopLeft[1]-shift[1]]
                             center_handle = [center_handle[0]-TopLeft[0]-shift[0], center_handle[1]-TopLeft[1]-shift[1]]
-                      
+                        
                             if center_handle != []:
                                 handles = [center_handle]
                             else:
                                 handles = [center_position]
+                            
                             src_handle_shift = []
                             dst_handle_shift = []
                             for a in range(len(src_handle)):
                                 src_handle_shift.append([src_handle[a][0]-TopLeft[0]-shift[0], src_handle[a][1]-TopLeft[1]-shift[1]])
                             for a in range(len(dst_handle)):
                                 dst_handle_shift.append([dst_handle[a][0]-TopLeft[0]-shift[0], dst_handle[a][1]-TopLeft[1]-shift[1]])
-                            # if temp_id == "EX_h_e":
-                            #     print(center_position)
-                            #     print(center_handle)
-                            #     print(src_handle_shift)
+                            
                             if len(src_corr) == 0:
                                 temp_node_id = "dummy" + str(dummy_node_id_index)                   
                                 comp_node_id = allNodes[dst_corr[0]].id 
                                 dst_node_id = comp_node_id #pick a product node
                                 # assume the dummy node is in the same compartment as the first src/dst node
                                 comp_id = model.getCompartmentIdSpeciesIsIn(comp_node_id)
                                 for m in range(len(allCompartments)):
@@ -1612,15 +1652,15 @@
                                         spec_border_color = comp_fill_color
                                         text_line_color = comp_fill_color
                                 for m in range(len(allNodes)):
                                     if dst_node_id == allNodes[m].id:
                                         dst_node_pos = allNodes[m].position
                                         dst_node_size = allNodes[m].size
                                         dst_node_c_pos = [dst_node_pos[0]+0.5*dst_node_size[0],
-                                                          dst_node_pos[1]+0.5*dst_node_size[1]]
+                                                            dst_node_pos[1]+0.5*dst_node_size[1]]
                                 if spec_border_width == 0.:
                                     spec_border_width = 0.001
                                     spec_border_color = spec_fill_color
 
 
                                 #node_position = [comp_position[0] + math.trunc (_random.random()*(comp_size[0] - 60.)), 
                                 #                comp_position[1] + math.trunc (_random.random()*(comp_size[1] - 40.))]
@@ -1666,27 +1706,27 @@
                                             src_node_Glyph_id = nodeIdx_specGlyph_whole_list[m][1]
                                     for m in range(len(spec_specGlyph_id_list)):
                                         if src_node_Glyph_id == spec_specGlyph_id_list[m][1]:
                                             #print(spec_specGlyph_id_list[m][0])
                                             src_node_size = spec_dimension_list[m]
                                             src_node_pos = spec_position_list[m]
                                             src_node_c_pos = [src_node_pos[0]+0.5*src_node_size[0],
-                                                              src_node_pos[1]+0.5*src_node_size[1]]
+                                                                src_node_pos[1]+0.5*src_node_size[1]]
                                     
                                 # try:#in case the dummy node has an alias node as src node
                                 #     src_node_c_pos = src_lineend_pos[0]
                                 # except:#in case there is no lineending available
                                 #     src_node_id = comp_node_id #pick a rct node
                                 #     for m in range(len(allNodes)):
                                 #         if src_node_id == allNodes[m].id:
                                 #             src_node_pos = allNodes[m].position
                                 #             src_node_size = allNodes[m].size
                                 #             src_node_c_pos = [src_node_pos[0]+0.5*src_node_size[0],
                                 #                               src_node_pos[1]+0.5*src_node_size[1]]
-                           
+                            
                                 comp_id = model.getCompartmentIdSpeciesIsIn(comp_node_id)
                                 for m in range(len(allCompartments)):
                                     if comp_id == allCompartments[m].id:
                                         comp_position = allCompartments[m].position
                                         comp_size = allCompartments[m].size
                                         compColor = allCompartments[m].fill_color
                                         comp_fill_color = [compColor.r, compColor.g, compColor.b, compColor.a]
@@ -1711,15 +1751,15 @@
                                     api.Color(text_line_color[0], text_line_color[1], text_line_color[2], text_line_color[3]))
                                 
                                 dst_corr.append(nodeIdx_temp)
                                 dummy_node_id_index += 1
 
                                 #dummy_handle_position = [0.5*(node_position[0] + center_position[0]), 
                                 #                            0.5*(node_position[1] + center_position[1])]
-                               
+                                
                                 dummy_handle_position = [0.5*(src_node_c_pos[0] + center_position[0]), 
                                                             0.5*(src_node_c_pos[1] + center_position[1])]
                                 #dummy_handle_position = center_position
                                 center_position = dummy_handle_position
                                 dst_handle_shift.append(dummy_handle_position)
 
                                 for xx in range(numComps):
@@ -1734,18 +1774,15 @@
 
 
                             handles.extend(src_handle_shift)
                             handles.extend(dst_handle_shift)
                             
                             if len(reaction_line_color) == 3:
                                 reaction_line_color.append(255)
-                            # if temp_id == "Diffusion_of_ammonia":
-                            #     print(temp_id)  
-                            #     print(center_position)  
-                            #     print(handles)                         
+                            
                             idx = api.add_reaction(net_index, id=temp_id, reactants=src_corr, products=dst_corr,
                             fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]),
                             line_thickness=reaction_line_width, modifiers = mod)
                             api.update_reaction(net_index, idx, ratelaw = kinetics)
                             handles_Vec2 = []  
                             if [] not in handles:      
                                 for i in range(len(handles)):
@@ -1905,52 +1942,56 @@
                                 dst_handles.append(dummy_handle_position)
 
                                 for xx in range(numComps):
                                     if comp_id == Comps_ids[xx]:
                                         api.set_compartment_of_node(net_index=net_index, node_index=nodeIdx_temp, comp_index=xx)
 
 
-                            handles.extend(src_handles)
-                            handles.extend(dst_handles)
 
+                            src_handles = [x for _,x in sorted(zip(src_corr, src_handles))]
+                            dst_handles = [x for _,x in sorted(zip(dst_corr, dst_handles))]
                             src_corr.sort()
                             dst_corr.sort()
 
+                            handles.extend(src_handles)
+                            handles.extend(dst_handles)
+
                             if len(reaction_line_color)==3:
                                 reaction_line_color.append(255)
 
-                            # try: 
-                            #     idx = api.add_reaction(net_index, id=temp_id, reactants=src_corr, products=dst_corr,
-                            #     fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]),
-                            #     line_thickness=reaction_line_width, modifiers = mod)
-                            #     api.update_reaction(net_index, idx, ratelaw = kinetics,
-                            #     fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
-                            # except:
-                            #     #rxn_id_duplicated
-                            #     idx = api.add_reaction(net_index, id=temp_id + "_duplicate", reactants=src_corr, products=dst_corr,
-                            #     fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]),
-                            #     line_thickness=reaction_line_width, modifiers = mod)
-                            #     api.update_reaction(net_index, idx, ratelaw = kinetics,
-                            #     fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
+                            try: 
+                                idx = api.add_reaction(net_index, id=temp_id, reactants=src_corr, products=dst_corr,
+                                fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]),
+                                line_thickness=reaction_line_width, modifiers = mod)
+                                api.update_reaction(net_index, idx, ratelaw = kinetics,
+                                fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
+                            except:
+                                #rxn_id_duplicated
+                                idx = api.add_reaction(net_index, id=temp_id + "_duplicate", reactants=src_corr, products=dst_corr,
+                                fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]),
+                                line_thickness=reaction_line_width, modifiers = mod)
+                                api.update_reaction(net_index, idx, ratelaw = kinetics,
+                                fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
                                                              
-                            # api.update_reaction(net_index, idx, 
-                            #      center_pos = Vec2(center_position[0],center_position[1]),  
-                            #      fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
-
-                            # handles_Vec2 = []  
-                            # if [] not in handles:      
-                            #     for i in range(len(handles)):
-                            #         handles_Vec2.append(Vec2(handles[i][0],handles[i][1]))
-                            #     api.update_reaction(net_index, idx, 
-                            #     center_pos = Vec2(center_position[0],center_position[1]), 
-                            #     handle_positions=handles_Vec2, 
-                            #     fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
+                            api.update_reaction(net_index, idx, 
+                                 center_pos = Vec2(center_position[0],center_position[1]),  
+                                 fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
+
+                            handles_Vec2 = []  
+                            if [] not in handles:      
+                                for i in range(len(handles)):
+                                    handles_Vec2.append(Vec2(handles[i][0],handles[i][1]))
+                                api.update_reaction(net_index, idx, 
+                                center_pos = Vec2(center_position[0],center_position[1]), 
+                                handle_positions=handles_Vec2, 
+                                fill_color=api.Color(reaction_line_color[0],reaction_line_color[1],reaction_line_color[2],reaction_line_color[3]))
 
 
                 else: # there is no layout information, assign position randomly and size as default
+                
                     comp_id_list = Comps_ids
 
                     for i in range(numComps):
                         temp_id = Comps_ids[i]
                         vol= model.getCompartmentVolume(i)
                         if math.isnan(vol):
                             vol = 1.
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/networkX.py` & `sbcoyote-1.3.7/rkviewer_plugins/networkX.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 class LayoutNetworkX(WindowedPlugin):
     metadata = PluginMetadata(
         name='AutoLayout',
         author='Carmen Perena Cortes, Herbert M. Sauro and Jin Xu',
         version='1.0.3',
         short_desc='Auto Layout using networkX.',
         long_desc='Rearrange a random network into a neat auto layout',
-        category=PluginCategory.UTILITIES,
+        category=PluginCategory.VISUALIZATION,
     )
 
     def create_window(self, dialog):
         '''
         Create a window with several inputs and buttons.
         Args:
             self
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/randomNetwork.py` & `sbcoyote-1.3.7/rkviewer_plugins/randomNetwork.py`

 * *Files 0% similar despite different names*

```diff
@@ -33,15 +33,15 @@
 class RandomNetwork(WindowedPlugin):
     metadata = PluginMetadata(
         name='RandomNetwork',
         author='Jin Xu, Herbert M. Sauro',
         version='1.0.1',
         short_desc='Random network.',
         long_desc='Display a random network with certain number of species and reactions as input.',
-        category=PluginCategory.UTILITIES
+        category=PluginCategory.MODELS
     )
     def __init__(self):
         """
         Initialize the RandomNetwork.
 
         Args:
             self
```

### Comparing `sbcoyote-1.3.6/rkviewer_plugins/structuralAnalysis.py` & `sbcoyote-1.3.7/rkviewer_plugins/structuralAnalysis.py`

 * *Files identical despite different names*

### Comparing `sbcoyote-1.3.6/PKG-INFO` & `sbcoyote-1.3.7/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sbcoyote
-Version: 1.3.6
+Version: 1.3.7
 Summary: SBcoyote: An Extensible Python Based Reaction Editor and Viewer.
 Author: Jin Xu and Gary Geng et al
 Author-email: jxu2019@uw.edu
 Requires-Python: >=3.7.1,<3.11
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Science/Research
@@ -45,33 +45,36 @@
 
 SBcoyote, initially called PyRKViewer or Coyote, is a cross-platform visualization tool for drawing reaction networks written with the
 [wxPython](https://www.wxpython.org/) framework. It can draw reactants, products, reactions, and compartments, and its features include but are not limited to:
 * Support for floating and boundary species.
 * Reactions can be displayed using Bezier curves and straight lines.
 * Plugin support, with some plugin examples: arrow designer, random network, auto layout, etc.
 
-## Installment for Users
+## Citing
 
-* Install Python 3.7, 3.8, 3.9 or 3.10 if not ready in the system.
+If you are using any of the code, please cite the article (https://arxiv.org/abs/2302.09151). 
+
+## Installing SBcoyote
+
+* Install Python 3.7, 3.8, 3.9 or 3.10 if not already in the system.
 * Go to the command line and type `pip install SBcoyote`.
-* If wxPython won't get installed automatically, please try to install wxPython 4.1.1 or 4.2.0 manually referring to https://wxpython.org/pages/downloads/index.html. Note wxPython 4.1.1 does not apply to Python 3.10. 
+* If wxPython doesn't get installed automatically, please try to install wxPython 4.1.1 or 4.2.0 manually referring to https://wxpython.org/pages/downloads/index.html. Note wxPython 4.1.1 does not work with Python 3.10. 
 * To run the application, simply type in the command line `SBcoyote`.
 
 ## Documentation
 
 The full documentation can be found at: https://sys-bio.github.io/SBcoyote/
 
 ## Visualization Example
 
 Here is a visualization example by SBcoyote for the large-scale Escherichia coli core 
 metabolism network (King et al., 2015; Orth et al., 2010).
 
 <img src="https://raw.githubusercontent.com/sys-bio/SBcoyote/main/examples/ecoli.png" width="500" height="400">
 
-
 ## Installment options for Developers
 
 ### Installing with Poetry
 1. If you do not have poetry installed on your computer, follow the quick steps shown [here](https://python-poetry.org/docs/).
 2. Once you have poetry installed, you will download SBcoyote. Click the green button at the top of this page that says “Code” and choose “Download ZIP”. You want to make sure you know where you have downloaded this. Unzip the folder to your desired directory.
 3. Next, open your terminal and navigate to the directory containing SBcoyote.
 4. Once inside the main folder of the application you can install the dependencies. To install the base dependencies simply run `poetry install`. To install the optional ones as well, run `poetry install -E simulation`. Note that this step may take a while. To learn more about which set of dependencies is right for you, refer to the [Dependencies](#Dependencies) section below.
```

