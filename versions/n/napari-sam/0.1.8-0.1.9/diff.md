# Comparing `tmp/napari-sam-0.1.8.tar.gz` & `tmp/napari-sam-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "napari-sam-0.1.8.tar", last modified: Thu Apr  6 12:27:33 2023, max compression
+gzip compressed data, was "napari-sam-0.1.9.tar", last modified: Thu Apr  6 13:26:58 2023, max compression
```

## Comparing `napari-sam-0.1.8.tar` & `napari-sam-0.1.9.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 12:27:18.000000 napari-sam-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 12:27:18.000000 napari-sam-0.1.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 12:27:33.978078 napari-sam-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 12:27:18.000000 napari-sam-0.1.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 12:27:18.000000 napari-sam-0.1.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-04-06 12:27:33.982078 napari-sam-0.1.8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/napari_sam/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14451 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)      274 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/napari.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/napari_sam.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:26:58.601552 napari-sam-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 13:26:36.000000 napari-sam-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 13:26:36.000000 napari-sam-0.1.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 13:26:58.601552 napari-sam-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 13:26:36.000000 napari-sam-0.1.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 13:26:36.000000 napari-sam-0.1.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-04-06 13:26:58.601552 napari-sam-0.1.9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:26:58.597552 napari-sam-0.1.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:26:58.601552 napari-sam-0.1.9/src/napari_sam/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 13:26:36.000000 napari-sam-0.1.9/src/napari_sam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15306 2023-04-06 13:26:36.000000 napari-sam-0.1.9/src/napari_sam/_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)      274 2023-04-06 13:26:36.000000 napari-sam-0.1.9/src/napari_sam/napari.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-04-06 13:26:36.000000 napari-sam-0.1.9/src/napari_sam/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:26:58.601552 napari-sam-0.1.9/src/napari_sam.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 13:26:58.000000 napari-sam-0.1.9/src/napari_sam.egg-info/top_level.txt
```

### Comparing `napari-sam-0.1.8/LICENSE` & `napari-sam-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `napari-sam-0.1.8/PKG-INFO` & `napari-sam-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: napari-sam
-Version: 0.1.8
+Version: 0.1.9
 Summary: Segment anything with Meta AI's new SAM model!
 Home-page: https://github.com/MIC-DKFZ/napari-sam
 Author: Karol Gotkowski
 Author-email: karol.gotkowski@dkfz.de
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/MIC-DKFZ/napari-sam/issues
 Project-URL: Documentation, https://github.com/MIC-DKFZ/napari-sam#README.md
```

### Comparing `napari-sam-0.1.8/README.md` & `napari-sam-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `napari-sam-0.1.8/setup.cfg` & `napari-sam-0.1.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `napari-sam-0.1.8/src/napari_sam/_widget.py` & `napari-sam-0.1.9/src/napari_sam/_widget.py`

 * *Files 6% similar despite different names*

```diff
@@ -84,24 +84,27 @@
         self.layout().addWidget(self.l_info)
         self.layout().addWidget(self.l_info_positive)
         self.layout().addWidget(self.l_info_negative)
 
         self.image_name = None
         self.image_layer = None
         self.label_layer = None
+        self.points_layer = None
 
         self.init_comboboxes()
 
         self.sam_model = None
         self.sam_predictor = None
         self.sam_logits = None
 
         self.point_coords = []
         self.point_labels = []
 
+        self.viewer.window.qt_viewer.layers.model().filterAcceptsRow = self._myfilter
+
     def init_model_type_combobox(self):
         model_types = list(sam_model_registry.keys())
         cached_weight_types = get_cached_weight_types(model_types)
         entries = []
         for name, is_cached in cached_weight_types.items():
             if is_cached:
                 entries.append("{} (Cached)".format(name))
@@ -216,14 +219,19 @@
             self._history_limit = self.label_layer._history_limit
             self._reset_history()
 
             self.viewer.mouse_drag_callbacks.append(self.callback_click)
 
             self.set_image()
 
+            selected_layer = self.viewer.layers.selection.active
+            self.points_layer = self.viewer.add_points(name="Ignore this layer <hidden>")
+            self.points_layer.editable = False
+            self.viewer.layers.selection.active = selected_layer
+
             @self.label_layer.bind_key('Control-Z')
             def on_undo(layer):
                 """Undo the last paint or fill action since the view slice has changed."""
                 self.undo()
                 layer.undo()
 
             @self.label_layer.bind_key('Control-Shift-Z')
@@ -244,14 +252,15 @@
         self.btn_activate.setText("Activate")
         self.remove_all_widget_callbacks()
         if self.label_layer is not None:
             self.label_layer.keymap = {}
         self.image_name = None
         self.image_layer = None
         self.label_layer = None
+        self.points_layer = None
         self.annotator_mode = AnnotatorMode.NONE
         self.point_coords = []
         self.point_labels = []
 
     def callback_click(self, layer, event):
         if self.annotator_mode == AnnotatorMode.CLICK:
             data_coordinates = self.image_layer.world_to_data(event.position)
@@ -273,14 +282,26 @@
             image = image[..., :3]  # Remove a potential alpha channel
             self.sam_predictor.set_image(image)
 
     def do_click(self, coords, is_positive):
         self.point_coords.append(coords)
         self.point_labels.append(is_positive)
 
+        colors = []
+        for point_label in self.point_labels:
+            if point_label:
+                colors.append("green")
+            else:
+                colors.append("red")
+
+        selected_layer = self.viewer.layers.selection.active
+        self.viewer.layers.remove(self.points_layer)
+        self.points_layer = self.viewer.add_points(name="Ignore this layer <hidden>", data=np.asarray(self.point_coords), face_color=colors)
+        self.viewer.layers.selection.active = selected_layer
+
         prediction, _, self.sam_logits = self.sam_predictor.predict(
             point_coords=np.flip(self.point_coords, axis=-1),
             point_labels=np.asarray(self.point_labels),
             mask_input=self.sam_logits,
             multimask_output=False,
         )
         self.label_layer.data = prediction
@@ -352,17 +373,16 @@
             values = prev_props if undoing else next_props
             self.props.update(values)
 
     def undo(self):
         self._load_history(
             self._undo_history, self._redo_history, undoing=True
         )
-        if self.current_label > 0:
-            self.current_label -= 1
-            del self.bubbles[-1]
 
     def redo(self):
         self._load_history(
             self._redo_history, self._undo_history, undoing=False
         )
-        self.current_label += 1
-        raise RuntimeError("Redo currently not supported as bubble history is not implemented.")
+        raise RuntimeError("Redo currently not supported.")
+
+    def _myfilter(self, row, parent):
+        return "<hidden>" not in self.viewer.layers[row].name
```

### Comparing `napari-sam-0.1.8/src/napari_sam/utils.py` & `napari-sam-0.1.9/src/napari_sam/utils.py`

 * *Files identical despite different names*

### Comparing `napari-sam-0.1.8/src/napari_sam.egg-info/PKG-INFO` & `napari-sam-0.1.9/src/napari_sam.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: napari-sam
-Version: 0.1.8
+Version: 0.1.9
 Summary: Segment anything with Meta AI's new SAM model!
 Home-page: https://github.com/MIC-DKFZ/napari-sam
 Author: Karol Gotkowski
 Author-email: karol.gotkowski@dkfz.de
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/MIC-DKFZ/napari-sam/issues
 Project-URL: Documentation, https://github.com/MIC-DKFZ/napari-sam#README.md
```

