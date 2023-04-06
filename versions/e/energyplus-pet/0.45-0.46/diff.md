# Comparing `tmp/energyplus_pet-0.45.tar.gz` & `tmp/energyplus_pet-0.46.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "energyplus_pet-0.45.tar", last modified: Thu Apr  6 19:01:34 2023, max compression
+gzip compressed data, was "energyplus_pet-0.46.tar", last modified: Thu Apr  6 19:05:59 2023, max compression
```

## Comparing `energyplus_pet-0.45.tar` & `energyplus_pet-0.46.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:34.136310 energyplus_pet-0.45/
--rw-r--r--   0 runner    (1001) docker     (122)     2133 2023-04-06 19:01:34.136310 energyplus_pet-0.45/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-06 19:01:04.000000 energyplus_pet-0.45/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:34.132310 energyplus_pet-0.45/energyplus_pet/
--rw-r--r--   0 runner    (1001) docker     (122)       49 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)       56 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/__main__.py
--rw-r--r--   0 runner    (1001) docker     (122)      318 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/configure.py
--rw-r--r--   0 runner    (1001) docker     (122)     7858 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/correction_factor.py
--rw-r--r--   0 runner    (1001) docker     (122)     5776 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/data_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:34.132310 energyplus_pet-0.45/energyplus_pet/equipment/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    13066 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/base.py
--rw-r--r--   0 runner    (1001) docker     (122)     2486 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/column_header.py
--rw-r--r--   0 runner    (1001) docker     (122)     2291 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/common_curves.py
--rw-r--r--   0 runner    (1001) docker     (122)     1908 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/equip_types.py
--rw-r--r--   0 runner    (1001) docker     (122)     1709 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/manager.py
--rw-r--r--   0 runner    (1001) docker     (122)    20165 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/wahp_cooling_curve.py
--rw-r--r--   0 runner    (1001) docker     (122)    15424 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/wahp_heating_curve.py
--rw-r--r--   0 runner    (1001) docker     (122)    15053 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/wwhp_cooling_curve.py
--rw-r--r--   0 runner    (1001) docker     (122)    15053 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/equipment/wwhp_heating_curve.py
--rw-r--r--   0 runner    (1001) docker     (122)      137 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:34.136310 energyplus_pet-0.45/energyplus_pet/forms/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    16776 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/base_data_form.py
--rw-r--r--   0 runner    (1001) docker     (122)     1045 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/basic_message_form.py
--rw-r--r--   0 runner    (1001) docker     (122)     4170 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/catalog_plot.py
--rw-r--r--   0 runner    (1001) docker     (122)     4268 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/comparison_plot.py
--rw-r--r--   0 runner    (1001) docker     (122)     8198 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/constant_parameters.py
--rw-r--r--   0 runner    (1001) docker     (122)    22194 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/correction_detail_form.py
--rw-r--r--   0 runner    (1001) docker     (122)     9698 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/correction_summary_form.py
--rw-r--r--   0 runner    (1001) docker     (122)     6408 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/correction_summary_widget.py
--rw-r--r--   0 runner    (1001) docker     (122)     3421 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/header_preview.py
--rw-r--r--   0 runner    (1001) docker     (122)    31743 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/forms/main.py
--rw-r--r--   0 runner    (1001) docker     (122)      152 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/runner.py
--rw-r--r--   0 runner    (1001) docker     (122)    12745 2023-04-06 19:01:04.000000 energyplus_pet-0.45/energyplus_pet/units.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:01:34.132310 energyplus_pet-0.45/energyplus_pet.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     2133 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1352 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)      152 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)       41 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       15 2023-04-06 19:01:34.000000 energyplus_pet-0.45/energyplus_pet.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      174 2023-04-06 19:01:34.136310 energyplus_pet-0.45/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1209 2023-04-06 19:01:04.000000 energyplus_pet-0.45/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:59.429499 energyplus_pet-0.46/
+-rw-r--r--   0 runner    (1001) docker     (122)     2133 2023-04-06 19:05:59.429499 energyplus_pet-0.46/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-06 19:05:35.000000 energyplus_pet-0.46/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:59.429499 energyplus_pet-0.46/energyplus_pet/
+-rw-r--r--   0 runner    (1001) docker     (122)       49 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)       56 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      318 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/configure.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7858 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/correction_factor.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5776 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/data_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:59.429499 energyplus_pet-0.46/energyplus_pet/equipment/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13066 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/base.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2486 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/column_header.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2291 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/common_curves.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1908 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/equip_types.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1709 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/manager.py
+-rw-r--r--   0 runner    (1001) docker     (122)    20165 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/wahp_cooling_curve.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15424 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/wahp_heating_curve.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15053 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/wwhp_cooling_curve.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15053 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/equipment/wwhp_heating_curve.py
+-rw-r--r--   0 runner    (1001) docker     (122)      137 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:59.429499 energyplus_pet-0.46/energyplus_pet/forms/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16776 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/base_data_form.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1045 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/basic_message_form.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4170 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/catalog_plot.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4268 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/comparison_plot.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8198 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/constant_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (122)    22194 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/correction_detail_form.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9698 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/correction_summary_form.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6408 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/correction_summary_widget.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3421 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/header_preview.py
+-rw-r--r--   0 runner    (1001) docker     (122)    31600 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/forms/main.py
+-rw-r--r--   0 runner    (1001) docker     (122)      152 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/runner.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12745 2023-04-06 19:05:35.000000 energyplus_pet-0.46/energyplus_pet/units.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 19:05:59.429499 energyplus_pet-0.46/energyplus_pet.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     2133 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1352 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      152 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       41 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       15 2023-04-06 19:05:59.000000 energyplus_pet-0.46/energyplus_pet.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      174 2023-04-06 19:05:59.433499 energyplus_pet-0.46/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1209 2023-04-06 19:05:35.000000 energyplus_pet-0.46/setup.py
```

### Comparing `energyplus_pet-0.45/PKG-INFO` & `energyplus_pet-0.46/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: energyplus_pet
-Version: 0.45
+Version: 0.46
 Summary: Parameter Estimation Tools for Generating EnergyPlus Inputs from Raw Performance Data
 Home-page: https://github.com/Myoldmopar/EnergyPlusPet
 Author: Edwin Lee
 Author-email: a@a.a
 License: UnlicensedForNow
 Description: # EnergyPlus "PET"
```

### Comparing `energyplus_pet-0.45/README.md` & `energyplus_pet-0.46/README.md`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/correction_factor.py` & `energyplus_pet-0.46/energyplus_pet/correction_factor.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/data_manager.py` & `energyplus_pet-0.46/energyplus_pet/data_manager.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/base.py` & `energyplus_pet-0.46/energyplus_pet/equipment/base.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/column_header.py` & `energyplus_pet-0.46/energyplus_pet/equipment/column_header.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/common_curves.py` & `energyplus_pet-0.46/energyplus_pet/equipment/common_curves.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/equip_types.py` & `energyplus_pet-0.46/energyplus_pet/equipment/equip_types.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/manager.py` & `energyplus_pet-0.46/energyplus_pet/equipment/manager.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/wahp_cooling_curve.py` & `energyplus_pet-0.46/energyplus_pet/equipment/wahp_cooling_curve.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/wahp_heating_curve.py` & `energyplus_pet-0.46/energyplus_pet/equipment/wahp_heating_curve.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/wwhp_cooling_curve.py` & `energyplus_pet-0.46/energyplus_pet/equipment/wwhp_cooling_curve.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/equipment/wwhp_heating_curve.py` & `energyplus_pet-0.46/energyplus_pet/equipment/wwhp_heating_curve.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/base_data_form.py` & `energyplus_pet-0.46/energyplus_pet/forms/base_data_form.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/basic_message_form.py` & `energyplus_pet-0.46/energyplus_pet/forms/basic_message_form.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/catalog_plot.py` & `energyplus_pet-0.46/energyplus_pet/forms/catalog_plot.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/comparison_plot.py` & `energyplus_pet-0.46/energyplus_pet/forms/comparison_plot.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/constant_parameters.py` & `energyplus_pet-0.46/energyplus_pet/forms/constant_parameters.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/correction_detail_form.py` & `energyplus_pet-0.46/energyplus_pet/forms/correction_detail_form.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/correction_summary_form.py` & `energyplus_pet-0.46/energyplus_pet/forms/correction_summary_form.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/correction_summary_widget.py` & `energyplus_pet-0.46/energyplus_pet/forms/correction_summary_widget.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/header_preview.py` & `energyplus_pet-0.46/energyplus_pet/forms/header_preview.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet/forms/main.py` & `energyplus_pet-0.46/energyplus_pet/forms/main.py`

 * *Files 0% similar despite different names*

```diff
@@ -63,18 +63,14 @@
             img = PhotoImage(file=str(self.icon_path))
             if self.icon_path.exists():
                 self.iconphoto(False, img)
             else:
                 print(f"Could not set icon for Windows, expecting to find it at {self.icon_path}")
         fixup_taskbar_icon_on_windows(NICE_NAME)
 
-        icon_path = Path(__file__).parent / 'favicon.png'
-        image = PhotoImage(file=str(icon_path))
-        self.iconphoto(True, image)
-
         # setup event listeners
         self._gui_queue = Queue()
         self._check_queue()
 
         # define the Tk.Variable instances that will be used to communicate with the GUI widgets
         self._define_tk_variables()
```

### Comparing `energyplus_pet-0.45/energyplus_pet/units.py` & `energyplus_pet-0.46/energyplus_pet/units.py`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/energyplus_pet.egg-info/PKG-INFO` & `energyplus_pet-0.46/energyplus_pet.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: energyplus-pet
-Version: 0.45
+Version: 0.46
 Summary: Parameter Estimation Tools for Generating EnergyPlus Inputs from Raw Performance Data
 Home-page: https://github.com/Myoldmopar/EnergyPlusPet
 Author: Edwin Lee
 Author-email: a@a.a
 License: UnlicensedForNow
 Description: # EnergyPlus "PET"
```

### Comparing `energyplus_pet-0.45/energyplus_pet.egg-info/SOURCES.txt` & `energyplus_pet-0.46/energyplus_pet.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `energyplus_pet-0.45/setup.py` & `energyplus_pet-0.46/setup.py`

 * *Files identical despite different names*

