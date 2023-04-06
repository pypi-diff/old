# Comparing `tmp/tksheet-5.6.7.tar.gz` & `tmp/tksheet-5.6.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tksheet-5.6.7.tar", last modified: Mon Apr  3 13:46:43 2023, max compression
+gzip compressed data, was "tksheet-5.6.8.tar", last modified: Thu Apr  6 11:14:57 2023, max compression
```

## Comparing `tksheet-5.6.7.tar` & `tksheet-5.6.8.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 13:46:43.061579 tksheet-5.6.7/
--rw-rw-rw-   0        0        0     1087 2023-03-26 15:09:51.000000 tksheet-5.6.7/LICENSE.txt
--rw-rw-rw-   0        0        0     2172 2023-04-03 13:46:43.061579 tksheet-5.6.7/PKG-INFO
--rw-rw-rw-   0        0        0     1522 2023-04-02 17:10:11.000000 tksheet-5.6.7/README.md
--rw-rw-rw-   0        0        0       86 2023-04-03 13:46:43.061579 tksheet-5.6.7/setup.cfg
--rw-rw-rw-   0        0        0     1025 2023-04-02 18:04:36.000000 tksheet-5.6.7/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:46:43.061579 tksheet-5.6.7/tksheet/
--rw-rw-rw-   0        0        0      317 2023-03-17 16:46:08.000000 tksheet-5.6.7/tksheet/__init__.py
--rw-rw-rw-   0        0        0   146851 2023-04-02 17:31:44.000000 tksheet-5.6.7/tksheet/_tksheet.py
--rw-rw-rw-   0        0        0    96335 2023-04-03 13:40:11.000000 tksheet-5.6.7/tksheet/_tksheet_column_headers.py
--rw-rw-rw-   0        0        0   314367 2023-04-03 13:40:33.000000 tksheet-5.6.7/tksheet/_tksheet_main_table.py
--rw-rw-rw-   0        0        0    11761 2023-04-02 06:42:13.000000 tksheet-5.6.7/tksheet/_tksheet_other_classes.py
--rw-rw-rw-   0        0        0    96198 2023-04-03 13:23:16.000000 tksheet-5.6.7/tksheet/_tksheet_row_index.py
--rw-rw-rw-   0        0        0     5666 2023-03-29 15:00:20.000000 tksheet-5.6.7/tksheet/_tksheet_top_left_rectangle.py
--rw-rw-rw-   0        0        0    50305 2023-04-02 16:47:04.000000 tksheet-5.6.7/tksheet/_tksheet_vars.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:46:43.061579 tksheet-5.6.7/tksheet.egg-info/
--rw-rw-rw-   0        0        0     2172 2023-04-03 13:46:43.000000 tksheet-5.6.7/tksheet.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      398 2023-04-03 13:46:43.000000 tksheet-5.6.7/tksheet.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 13:46:43.000000 tksheet-5.6.7/tksheet.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        8 2023-04-03 13:46:43.000000 tksheet-5.6.7/tksheet.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 11:14:57.345203 tksheet-5.6.8/
+-rw-rw-rw-   0        0        0     1087 2023-03-26 15:09:51.000000 tksheet-5.6.8/LICENSE.txt
+-rw-rw-rw-   0        0        0     2172 2023-04-06 11:14:57.345203 tksheet-5.6.8/PKG-INFO
+-rw-rw-rw-   0        0        0     1522 2023-04-02 17:10:11.000000 tksheet-5.6.8/README.md
+-rw-rw-rw-   0        0        0       86 2023-04-06 11:14:57.345203 tksheet-5.6.8/setup.cfg
+-rw-rw-rw-   0        0        0     1025 2023-04-03 13:47:11.000000 tksheet-5.6.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:14:57.329577 tksheet-5.6.8/tksheet/
+-rw-rw-rw-   0        0        0      317 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/__init__.py
+-rw-rw-rw-   0        0        0   146851 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet.py
+-rw-rw-rw-   0        0        0    96382 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_column_headers.py
+-rw-rw-rw-   0        0        0   314198 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_main_table.py
+-rw-rw-rw-   0        0        0    11669 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_other_classes.py
+-rw-rw-rw-   0        0        0    96245 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_row_index.py
+-rw-rw-rw-   0        0        0     5666 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_top_left_rectangle.py
+-rw-rw-rw-   0        0        0    51924 2023-04-06 07:31:37.000000 tksheet-5.6.8/tksheet/_tksheet_vars.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:14:57.345203 tksheet-5.6.8/tksheet.egg-info/
+-rw-rw-rw-   0        0        0     2172 2023-04-06 11:14:57.000000 tksheet-5.6.8/tksheet.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      398 2023-04-06 11:14:57.000000 tksheet-5.6.8/tksheet.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 11:14:57.000000 tksheet-5.6.8/tksheet.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 11:14:57.000000 tksheet-5.6.8/tksheet.egg-info/top_level.txt
```

### Comparing `tksheet-5.6.7/LICENSE.txt` & `tksheet-5.6.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `tksheet-5.6.7/PKG-INFO` & `tksheet-5.6.8/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: tksheet
-Version: 5.6.7
+Version: 5.6.8
 Summary: Tkinter table / sheet widget
 Home-page: https://github.com/ragardner/tksheet
-Download-URL: https://github.com/ragardner/tksheet/archive/5.6.7.tar.gz
+Download-URL: https://github.com/ragardner/tksheet/archive/5.6.8.tar.gz
 Author: ragardner
 Author-email: github@ragardner.simplelogin.com
 License: MIT
 Keywords: tkinter,table,widget,sheet,grid,tk
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
```

### Comparing `tksheet-5.6.7/README.md` & `tksheet-5.6.8/README.md`

 * *Files identical despite different names*

### Comparing `tksheet-5.6.7/setup.py` & `tksheet-5.6.8/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,24 +4,24 @@
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, 'README.md'), encoding = 'utf-8') as f:
     long_description = f.read()
 
 setup(
   name = 'tksheet',
   packages = ['tksheet'],
-  version = '5.6.7',
+  version = '5.6.8',
   python_requires = '>=3.6',
   license = 'MIT',
   description = 'Tkinter table / sheet widget',
   long_description = long_description,
   long_description_content_type = 'text/markdown',
   author = 'ragardner',
   author_email = 'github@ragardner.simplelogin.com',
   url = 'https://github.com/ragardner/tksheet',
-  download_url = 'https://github.com/ragardner/tksheet/archive/5.6.7.tar.gz',
+  download_url = 'https://github.com/ragardner/tksheet/archive/5.6.8.tar.gz',
   keywords = ['tkinter', 'table', 'widget', 'sheet', 'grid', 'tk'],
   install_requires = [],
   classifiers = [
     'Development Status :: 5 - Production/Stable',
     'Intended Audience :: Developers',
     'Topic :: Software Development :: Build Tools',
     'License :: OSI Approved :: MIT License'
```

### Comparing `tksheet-5.6.7/tksheet/_tksheet.py` & `tksheet-5.6.8/tksheet/_tksheet.py`

 * *Files identical despite different names*

### Comparing `tksheet-5.6.7/tksheet/_tksheet_column_headers.py` & `tksheet-5.6.8/tksheet/_tksheet_column_headers.py`

 * *Files 0% similar despite different names*

```diff
@@ -371,15 +371,15 @@
             self.extra_b1_press_func(event)
     
     def b1_motion(self, event):
         x1, y1, x2, y2 = self.MT.get_canvas_visible_area()
         if self.width_resizing_enabled and self.rsz_w is not None and self.currently_resizing_width:
             x = self.canvasx(event.x)
             size = x - self.MT.col_positions[self.rsz_w - 1]
-            if not size < self.MT.min_cw and size < self.max_cw:
+            if size >= self.MT.min_cw and size < self.max_cw:
                 self.delete_resize_lines()
                 self.MT.delete_resize_lines()
                 line2x = self.MT.col_positions[self.rsz_w - 1]
                 self.create_resize_line(x, 0, x, self.current_height, width = 1, fill = self.resizing_line_fg, tag = "rwl")
                 self.MT.create_resize_line(x, y1, x, y2, width = 1, fill = self.resizing_line_fg, tag = "rwl")
                 self.create_resize_line(line2x, 0, line2x, self.current_height,width = 1, fill = self.resizing_line_fg, tag = "rwl2")
                 self.MT.create_resize_line(line2x, y1, line2x, y2, width = 1, fill = self.resizing_line_fg, tag = "rwl2")
@@ -491,15 +491,15 @@
         if self.being_drawn_rect is not None:
             to_sel = tuple(self.being_drawn_rect)
             self.being_drawn_rect = None
             self.MT.create_selected(*to_sel)
         self.MT.bind("<MouseWheel>", self.MT.mousewheel)
         if self.width_resizing_enabled and self.rsz_w is not None and self.currently_resizing_width:
             self.currently_resizing_width = False
-            new_col_pos = self.coords("rwl")[0]
+            new_col_pos = int(self.coords("rwl")[0])
             self.delete_resize_lines()
             self.MT.delete_resize_lines()
             old_width = self.MT.col_positions[self.rsz_w] - self.MT.col_positions[self.rsz_w - 1]
             size = new_col_pos - self.MT.col_positions[self.rsz_w - 1]
             if size < self.MT.min_cw:
                 new_col_pos = ceil(self.MT.col_positions[self.rsz_w - 1] + self.MT.min_cw)
             elif size > self.max_cw:
@@ -1320,20 +1320,21 @@
                                       popup_menu_bg = self.MT.popup_menu_bg,
                                       popup_menu_highlight_bg = self.MT.popup_menu_highlight_bg,
                                       popup_menu_highlight_fg = self.MT.popup_menu_highlight_fg,
                                       binding = binding,
                                       align = self.get_cell_align(c),
                                       c = c,
                                       newline_binding = self.text_editor_has_wrapped)
+        self.text_editor.update_idletasks()
         self.text_editor_id = self.create_window((x, y), window = self.text_editor, anchor = "nw")
         if not dropdown:
             self.text_editor.textedit.focus_set()
             self.text_editor.scroll_to_bottom()
         self.text_editor.textedit.bind("<Alt-Return>", lambda x: self.text_editor_newline_binding(c = c))
-        if USER_OS == 'Darwin':
+        if USER_OS == 'darwin':
             self.text_editor.textedit.bind("<Option-Return>", lambda x: self.text_editor_newline_binding(c = c))
         for key, func in self.MT.text_editor_user_bound_keys.items():
             self.text_editor.textedit.bind(key, func)
         if binding is not None:
             self.text_editor.textedit.bind("<Tab>", lambda x: binding((c, "Tab")))
             self.text_editor.textedit.bind("<Return>", lambda x: binding((c, "Return")))
             self.text_editor.textedit.bind("<FocusOut>", lambda x: binding((c, "FocusOut")))
```

### Comparing `tksheet-5.6.7/tksheet/_tksheet_main_table.py` & `tksheet-5.6.8/tksheet/_tksheet_main_table.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,16 +8,14 @@
 import bisect
 import csv as csv_module
 import io
 import pickle
 import tkinter as tk
 import zlib
 
-import datetime
-
 
 class MainTable(tk.Canvas):
     def __init__(self,
                  *args,
                  **kwargs):
         tk.Canvas.__init__(self,
                            kwargs['parentframe'],
@@ -265,15 +263,15 @@
             self.bind("<Configure>", self.refresh)
             self.bind("<Motion>", self.mouse_motion)
             self.bind("<ButtonPress-1>", self.b1_press)
             self.bind("<B1-Motion>", self.b1_motion)
             self.bind("<ButtonRelease-1>", self.b1_release)
             self.bind("<Double-Button-1>", self.double_b1)
             self.bind("<MouseWheel>", self.mousewheel)
-            if USER_OS == "Linux":
+            if USER_OS == "linux":
                 for canvas in (self, self.RI):
                     canvas.bind("<Button-4>", self.mousewheel)
                     canvas.bind("<Button-5>", self.mousewheel)
                 for canvas in (self, self.CH):
                     canvas.bind("<Shift-Button-4>", self.shift_mousewheel)
                     canvas.bind("<Shift-Button-5>", self.shift_mousewheel)
             self.bind("<Shift-MouseWheel>", self.shift_mousewheel)
@@ -287,15 +285,15 @@
             self.unbind("<Configure>")
             self.unbind("<Motion>")
             self.unbind("<ButtonPress-1>")
             self.unbind("<B1-Motion>")
             self.unbind("<ButtonRelease-1>")
             self.unbind("<Double-Button-1>")
             self.unbind("<MouseWheel>")
-            if USER_OS == "Linux":
+            if USER_OS == "linux":
                 for canvas in (self, self.RI):
                     canvas.unbind("<Button-4>")
                     canvas.unbind("<Button-5>")
                 for canvas in (self, self.CH):
                     canvas.unbind("<Shift-Button-4>")
                     canvas.unbind("<Shift-Button-5>")
             self.unbind("<Shift-ButtonPress-1>")
@@ -1787,51 +1785,51 @@
                     self.see(r, c - 1, keep_yscroll = True, check_cell_visibility = False)
 
     def edit_bindings(self, enable = True, key = None):
         if key is None or key == "copy":
             if enable:
                 for s2 in ("c", "C"):
                     for widget in (self, self.RI, self.CH, self.TL):
-                        widget.bind(f"<{'Command' if USER_OS == 'Darwin' else 'Control'}-{s2}>", self.ctrl_c)
+                        widget.bind(f"<{ctrl_key}-{s2}>", self.ctrl_c)
                 self.copy_enabled = True
             else:
                 for s1 in ("Control", "Command"):
                     for s2 in ("c", "C"):
                         for widget in (self, self.RI, self.CH, self.TL):
                             widget.unbind(f"<{s1}-{s2}>")
                 self.copy_enabled = False
         if key is None or key == "cut":
             if enable:
                 for s2 in ("x", "X"):
                     for widget in (self, self.RI, self.CH, self.TL):
-                        widget.bind(f"<{'Command' if USER_OS == 'Darwin' else 'Control'}-{s2}>", self.ctrl_x)
+                        widget.bind(f"<{ctrl_key}-{s2}>", self.ctrl_x)
                 self.cut_enabled = True
             else:
                 for s1 in ("Control", "Command"):
                     for s2 in ("x", "X"):
                         for widget in (self, self.RI, self.CH, self.TL):
                             widget.unbind(f"<{s1}-{s2}>")
                 self.cut_enabled = False
         if key is None or key == "paste":
             if enable:
                 for s2 in ("v", "V"):
                     for widget in (self, self.RI, self.CH, self.TL):
-                        widget.bind(f"<{'Command' if USER_OS == 'Darwin' else 'Control'}-{s2}>", self.ctrl_v)
+                        widget.bind(f"<{ctrl_key}-{s2}>", self.ctrl_v)
                 self.paste_enabled = True
             else:
                 for s1 in ("Control", "Command"):
                     for s2 in ("v", "V"):
                         for widget in (self, self.RI, self.CH, self.TL):
                             widget.unbind(f"<{s1}-{s2}>")
                 self.paste_enabled = False
         if key is None or key == "undo":
             if enable:
                 for s2 in ("z", "Z"):
                     for widget in (self, self.RI, self.CH, self.TL):
-                        widget.bind(f"<{'Command' if USER_OS == 'Darwin' else 'Control'}-{s2}>", self.ctrl_z)
+                        widget.bind(f"<{ctrl_key}-{s2}>", self.ctrl_z)
                 self.undo_enabled = True
             else:
                 for s1 in ("Control", "Command"):
                     for s2 in ("z", "Z"):
                         for widget in (self, self.RI, self.CH, self.TL):
                             widget.unbind(f"<{s1}-{s2}>")
                 self.undo_enabled = False
@@ -2177,15 +2175,15 @@
                     self.disable_bindings_internal(binding.lower())
         elif isinstance(bindings, str):
             self.disable_bindings_internal(bindings)
 
     def enable_disable_select_all(self, enable = True):
         self.select_all_enabled = bool(enable)
         for s in ("A", "a"):
-            binding = f"<{'Command' if USER_OS == 'Darwin' else 'Control'}-{s}>"
+            binding = f"<{ctrl_key}-{s}>"
             for widget in (self, self.RI, self.CH, self.TL):
                 if enable:
                     widget.bind(binding, self.select_all)
                 else:
                     widget.unbind(binding)
 
     def enable_bindings_internal(self, binding):
@@ -5165,20 +5163,21 @@
                                       popup_menu_highlight_bg = self.popup_menu_highlight_bg,
                                       popup_menu_highlight_fg = self.popup_menu_highlight_fg,
                                       binding = binding,
                                       align = self.get_cell_align(r, c),
                                       r = r,
                                       c = c,
                                       newline_binding = self.text_editor_newline_binding)
+        self.text_editor.update_idletasks()
         self.text_editor_id = self.create_window((x, y), window = self.text_editor, anchor = "nw")
         if not dropdown:
             self.text_editor.textedit.focus_set()
             self.text_editor.scroll_to_bottom()
         self.text_editor.textedit.bind("<Alt-Return>", lambda x: self.text_editor_newline_binding(r, c))
-        if USER_OS == 'Darwin':
+        if USER_OS == 'darwin':
             self.text_editor.textedit.bind("<Option-Return>", lambda x: self.text_editor_newline_binding(r, c))
         for key, func in self.text_editor_user_bound_keys.items():
             self.text_editor.textedit.bind(key, func)
         if binding is not None:
             self.text_editor.textedit.bind("<Tab>", lambda x: binding((r, c, "Tab")))
             self.text_editor.textedit.bind("<Return>", lambda x: binding((r, c, "Return")))
             self.text_editor.textedit.bind("<FocusOut>", lambda x: binding((r, c, "FocusOut")))
```

### Comparing `tksheet-5.6.7/tksheet/_tksheet_other_classes.py` & `tksheet-5.6.8/tksheet/_tksheet_other_classes.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,11 @@
 from ._tksheet_vars import *
 from collections import namedtuple
 from itertools import islice
 import tkinter as tk
-# for mac bindings
-from platform import system as get_os
-USER_OS = f"{get_os()}"
 
 
 CurrentlySelectedClass = namedtuple("CurrentlySelectedClass", "row column type_")
 CtrlKeyEvent = namedtuple("CtrlKeyEvent", "eventname selectionboxes currentlyselected rows")
 PasteEvent = namedtuple("PasteEvent", "eventname currentlyselected rows")
 UndoEvent = namedtuple("UndoEvent", "eventname type storeddata")
 SelectCellEvent = namedtuple("SelectCellEvent", "eventname row column")
@@ -63,18 +60,18 @@
         if align == "w":
             self.align = "left"
         elif align == "center":
             self.align = "center"
         elif align == "e":
             self.align = "right"
         self.tag_configure("align", justify = self.align)
-        if text is not None:
+        if text:
             self.insert(1.0, text)
+            self.yview_moveto(1)
         self.tag_add("align", 1.0, "end")
-        self.yview_moveto(1)
         self.rc_popup_menu = tk.Menu(self, tearoff = 0)
         self.rc_popup_menu.add_command(label = "Select all",
                                        accelerator = "Ctrl+A",
                                        font = popup_menu_font,
                                        foreground = popup_menu_fg,
                                        background = popup_menu_bg,
                                        activebackground = popup_menu_highlight_bg,
@@ -109,15 +106,15 @@
                                        font = popup_menu_font,
                                        foreground = popup_menu_fg,
                                        background = popup_menu_bg,
                                        activebackground = popup_menu_highlight_bg,
                                        activeforeground = popup_menu_highlight_fg,
                                        command = self.undo)
         self.bind("<1>", lambda event: self.focus_set())
-        if USER_OS == "Darwin":
+        if USER_OS == "darwin":
             self.bind("<2>", self.rc)
         else:
             self.bind("<3>", self.rc)
         self._orig = self._w + "_orig"
         self.tk.call("rename", self._w, self._orig)
         self.tk.createcommand(self._w, self._proxy)
 
@@ -259,18 +256,18 @@
     for idx, n in zip(range(start, -1, -1), reversed(seq[:start])):
         if n != prevn - 1:
             return idx
         prevn = n
     return None
 
 def is_mac():
-    if USER_OS == "Darwin":
+    if USER_OS == "darwin":
         return True
     else:
         return False
 
 def get_rc_binding():
-    if USER_OS == "Darwin":
+    if USER_OS == "darwin":
         return "<2>"
     else:
         return "<3>"
```

### Comparing `tksheet-5.6.7/tksheet/_tksheet_row_index.py` & `tksheet-5.6.8/tksheet/_tksheet_row_index.py`

 * *Files 0% similar despite different names*

```diff
@@ -360,15 +360,15 @@
             self.extra_b1_press_func(event)
     
     def b1_motion(self, event):
         x1,y1,x2,y2 = self.MT.get_canvas_visible_area()
         if self.height_resizing_enabled and self.rsz_h is not None and self.currently_resizing_height:
             y = self.canvasy(event.y)
             size = y - self.MT.row_positions[self.rsz_h - 1]
-            if not size < self.MT.min_rh and size < self.max_rh:
+            if size >= self.MT.min_rh and size < self.max_rh:
                 self.delete_resize_lines()
                 self.MT.delete_resize_lines()
                 line2y = self.MT.row_positions[self.rsz_h - 1]
                 self.create_resize_line(0, y, self.current_width, y, width = 1, fill = self.resizing_line_fg, tag = "rhl")
                 self.MT.create_resize_line(x1, y, x2, y, width = 1, fill = self.resizing_line_fg, tag = "rhl")
                 self.create_resize_line(0, line2y, self.current_width, line2y, width = 1, fill = self.resizing_line_fg, tag = "rhl2")
                 self.MT.create_resize_line(x1, line2y, x2, line2y, width = 1, fill = self.resizing_line_fg, tag = "rhl2")
@@ -480,15 +480,15 @@
         if self.being_drawn_rect is not None:
             to_sel = tuple(self.being_drawn_rect)
             self.being_drawn_rect = None
             self.MT.create_selected(*to_sel)
         self.MT.bind("<MouseWheel>", self.MT.mousewheel)
         if self.height_resizing_enabled and self.rsz_h is not None and self.currently_resizing_height:
             self.currently_resizing_height = False
-            new_row_pos = self.coords("rhl")[1]
+            new_row_pos = int(self.coords("rhl")[1])
             self.delete_resize_lines()
             self.MT.delete_resize_lines()
             old_height = self.MT.row_positions[self.rsz_h] - self.MT.row_positions[self.rsz_h - 1]
             size = new_row_pos - self.MT.row_positions[self.rsz_h - 1]
             if size < self.MT.min_rh:
                 new_row_pos = ceil(self.MT.row_positions[self.rsz_h - 1] + self.MT.min_rh)
             elif size > self.max_rh:
@@ -1376,20 +1376,21 @@
                                       popup_menu_bg = self.MT.popup_menu_bg,
                                       popup_menu_highlight_bg = self.MT.popup_menu_highlight_bg,
                                       popup_menu_highlight_fg = self.MT.popup_menu_highlight_fg,
                                       binding = binding,
                                       align = self.get_cell_align(r),
                                       r = r,
                                       newline_binding = self.text_editor_newline_binding)
+        self.text_editor.update_idletasks()
         self.text_editor_id = self.create_window((x, y), window = self.text_editor, anchor = "nw")
         if not dropdown:
             self.text_editor.textedit.focus_set()
             self.text_editor.scroll_to_bottom()
         self.text_editor.textedit.bind("<Alt-Return>", lambda x: self.text_editor_newline_binding(r = r))
-        if USER_OS == 'Darwin':
+        if USER_OS == 'darwin':
             self.text_editor.textedit.bind("<Option-Return>", lambda x: self.text_editor_newline_binding(r = r))
         for key, func in self.MT.text_editor_user_bound_keys.items():
             self.text_editor.textedit.bind(key, func)
         if binding is not None:
             self.text_editor.textedit.bind("<Tab>", lambda x: binding((r, "Tab")))
             self.text_editor.textedit.bind("<Return>", lambda x: binding((r, "Return")))
             self.text_editor.textedit.bind("<FocusOut>", lambda x: binding((r, "FocusOut")))
```

### Comparing `tksheet-5.6.7/tksheet/_tksheet_top_left_rectangle.py` & `tksheet-5.6.8/tksheet/_tksheet_top_left_rectangle.py`

 * *Files identical despite different names*

### Comparing `tksheet-5.6.7/tksheet/_tksheet_vars.py` & `tksheet-5.6.8/tksheet/_tksheet_vars.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,22 @@
+# for mac bindings
+from platform import system as get_os
+USER_OS = f"{get_os()}".lower()
+
+ctrl_key = "Command" if USER_OS == "darwin" else "Control"
 symbols_set = set("""!#\$%&'()*+,-./:;"@[]^_`{|}~>?= """)
 
 def get_font():
-    return ("Calibri", 11, "normal")
+    return ("Calibri", 13 if USER_OS == "darwin" else 11, "normal")
 
 def get_index_font():
-    return ('Calibri', 11, "normal")
+    return ('Calibri', 13 if USER_OS == "darwin" else 11, "normal")
 
 def get_heading_font():
-    return ("Calibri", 11, "normal")
+    return ("Calibri", 13 if USER_OS == "darwin" else 11, "normal")
 
 def is_iterable(o):
     try:
         for e in o:
             break
         return True
     except:
@@ -142,15 +147,57 @@
 'table_selected_rows_bg': "#333333",
 'table_selected_rows_fg': "#FFFFFF",
 'table_selected_columns_border_fg': "#FBB86C",
 'table_selected_columns_bg': "#333333",
 'table_selected_columns_fg': "#FFFFFF"
 }
 
-theme_dark = theme_black.copy()
+theme_dark = {
+'popup_menu_fg': "white",
+'popup_menu_bg': "gray15",
+'popup_menu_highlight_bg': "gray35",
+'popup_menu_highlight_fg': "white",
+'index_hidden_rows_expander_bg': "gray30",
+'header_hidden_columns_expander_bg': "gray30",
+'header_bg': "#141414",
+'header_border_fg': "#505054",
+'header_grid_fg': "#8C8C8C",
+'header_fg': "gray70",
+'header_selected_cells_bg': "#545454",
+'header_selected_cells_fg': "#6aa2fc",
+'index_bg': "#141414",
+'index_border_fg': "#505054",
+'index_grid_fg': "#8C8C8C",
+'index_fg': "gray70",
+'index_selected_cells_bg': "#545454",
+'index_selected_cells_fg': "#6aa2fc",
+'top_left_bg': "#323232",
+'top_left_fg': "#505054",
+'top_left_fg_highlight': "white",
+'table_bg': "#323232",
+'table_grid_fg': "#505054",
+'table_fg': "#F2F2F2",
+'table_selected_cells_border_fg': "#6aa2fc",
+'table_selected_cells_bg': "#141414",
+'table_selected_cells_fg': "#fafafa",
+'resizing_line_fg': "white",
+'drag_and_drop_bg': "#ecf0f2",
+'outline_color': "gray95",
+'header_selected_columns_bg': "#4489F7",
+'header_selected_columns_fg': "white",
+'index_selected_rows_bg': "#4489F7",
+'index_selected_rows_fg': "white",
+'table_selected_rows_border_fg': "#4489F7",
+'table_selected_rows_bg': "#141414",
+'table_selected_rows_fg': "#fafafa",
+'table_selected_columns_border_fg': "#4489F7",
+'table_selected_columns_bg': "#141414",
+'table_selected_columns_fg': "#fafafa"
+}
+
 theme_dark_blue = theme_black.copy()
 theme_dark_blue['header_fg'] = "#6ACAD8"
 theme_dark_blue['header_selected_cells_fg'] = "#6ACAD8"
 theme_dark_blue['index_fg'] = "#6ACAD8"
 theme_dark_blue['index_selected_cells_fg'] = "#6ACAD8"
 theme_dark_blue['top_left_fg_highlight'] = "#6ACAD8"
 theme_dark_blue['table_selected_cells_border_fg'] = "#6ACAD8"
```

### Comparing `tksheet-5.6.7/tksheet.egg-info/PKG-INFO` & `tksheet-5.6.8/tksheet.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: tksheet
-Version: 5.6.7
+Version: 5.6.8
 Summary: Tkinter table / sheet widget
 Home-page: https://github.com/ragardner/tksheet
-Download-URL: https://github.com/ragardner/tksheet/archive/5.6.7.tar.gz
+Download-URL: https://github.com/ragardner/tksheet/archive/5.6.8.tar.gz
 Author: ragardner
 Author-email: github@ragardner.simplelogin.com
 License: MIT
 Keywords: tkinter,table,widget,sheet,grid,tk
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
```

