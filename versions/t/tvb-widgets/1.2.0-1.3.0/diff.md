# Comparing `tmp/tvb-widgets-1.2.0.tar.gz` & `tmp/tvb-widgets-1.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tvb-widgets-1.2.0.tar", last modified: Fri Feb 24 13:58:53 2023, max compression
+gzip compressed data, was "tvb-widgets-1.3.0.tar", last modified: Thu Apr  6 20:28:51 2023, max compression
```

## Comparing `tvb-widgets-1.2.0.tar` & `tvb-widgets-1.3.0.tar`

### file list

```diff
@@ -1,51 +1,56 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.603795 tvb-widgets-1.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)    35796 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3021 2023-02-24 13:58:53.603795 tvb-widgets-1.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-24 13:58:53.603795 tvb-widgets-1.2.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1666 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvb_widgets.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3021 2023-02-24 13:58:53.000000 tvb-widgets-1.2.0/tvb_widgets.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1257 2023-02-24 13:58:53.000000 tvb-widgets-1.2.0/tvb_widgets.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-24 13:58:53.000000 tvb-widgets-1.2.0/tvb_widgets.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-02-24 13:58:53.000000 tvb-widgets-1.2.0/tvb_widgets.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-02-24 13:58:53.000000 tvb-widgets-1.2.0/tvb_widgets.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/
--rw-r--r--   0 runner    (1001) docker     (123)     1270 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      369 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/core/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      813 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/ini_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/core/logger/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/logger/builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1405 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/logger/logging.conf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/core/simulator/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/simulator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7788 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/simulator/model_exporters.py
--rw-r--r--   0 runner    (1001) docker     (123)      553 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/core/simulator/tvb_integrators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      481 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      944 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3633 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_drive_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)     6077 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_exporters.py
--rw-r--r--   0 runner    (1001) docker     (123)     4612 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_head_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)     4598 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_phase_plane_export.py
--rw-r--r--   0 runner    (1001) docker     (123)     6513 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_ts_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)      306 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/test_tvb_integrators.py
--rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/tests/ts_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:53.599795 tvb-widgets-1.2.0/tvbwidgets/ui/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/base_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)     5645 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/drive_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)    12507 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/head_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)    36149 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/phase_plane_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)     5039 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/pse_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)      989 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/storage_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)    23948 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/ts_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)      940 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/ts_widget_help.ini
--rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-02-24 13:58:47.000000 tvb-widgets-1.2.0/tvbwidgets/ui/widget_with_browser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.422724 tvb-widgets-1.3.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    35796 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3587 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3099 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:28:51.422724 tvb-widgets-1.3.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvb_widgets.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3587 2023-04-06 20:28:51.000000 tvb-widgets-1.3.0/tvb_widgets.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-04-06 20:28:51.000000 tvb-widgets-1.3.0/tvb_widgets.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:28:51.000000 tvb-widgets-1.3.0/tvb_widgets.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-04-06 20:28:51.000000 tvb-widgets-1.3.0/tvb_widgets.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 20:28:51.000000 tvb-widgets-1.3.0/tvb_widgets.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/
+-rw-r--r--   0 runner    (1001) docker     (123)     1270 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/core/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      813 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/ini_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/core/logger/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/logger/builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1405 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/logger/logging.conf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/core/pse/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/pse/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11553 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/pse/parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      850 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/pse/pse_data.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/core/simulator/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/simulator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7788 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/simulator/model_exporters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      553 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/core/simulator/tvb_integrators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      481 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      944 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3633 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_drive_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6077 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_exporters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4612 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_head_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4598 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_phase_plane_export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6513 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_ts_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)      306 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/test_tvb_integrators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/tests/ts_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:51.418723 tvb-widgets-1.3.0/tvbwidgets/ui/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/base_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5645 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/drive_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12507 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/head_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36149 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/phase_plane_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10786 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/pse_launcher_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5304 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/pse_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)      989 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/storage_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23948 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/ts_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)      940 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/ts_widget_help.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-04-06 20:28:45.000000 tvb-widgets-1.3.0/tvbwidgets/ui/widget_with_browser.py
```

### Comparing `tvb-widgets-1.2.0/LICENSE` & `tvb-widgets-1.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/PKG-INFO` & `tvb-widgets-1.3.0/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tvb-widgets
-Version: 1.2.0
+Version: 1.3.0
 Summary: GUI widgets for EBRAINS showcases
 Home-page: https://github.com/the-virtual-brain/tvb-widgets
 Author: TVB Widgets Team (Juelich SDL Neuroscience, INS - Marseille, Codemart)
 Author-email: tvb.admin@thevirtualbrain.org
 License: GPL-3.0-or-later
 Keywords: tvb widgets jupyterlab ebrains showcases
 Platform: UNKNOWN
@@ -31,22 +31,39 @@
 can be easily deployed in the EBRAINS Collaboratory within the JupyterLab. 
 
 This module is also documented in EBRAINS here: https://wiki.ebrains.eu/bin/view/Collabs/tvb-widgets
 
 These graphic user interface components enable:
  1. Easy setup of models and region specific or cohort simulations. This includes single simulations as well as parameter explorations.
  2. Selection of Data sources and their links to models. This will exploit the backend data access functionality to be developed new in TVB.
- 3. Previews of queried data from Siibra and the KG.
- 4. Deployment of jobs to HPC resources.
- 5. Integration of a subset of TVB analysis and visualisation tools.
- 6. The GUIs must be designed to be integrated into cells in the notebooks and Jupyter notebook extension for HPC resource usage and job tracking will be also developed as independent panels.
+ 3. Integration of a subset of TVB analysis and visualisation tools.
+ 4. The GUIs must be designed to be integrated into cells in the notebooks and Jupyter notebook extension for HPC resource usage and job tracking will be also developed as independent panels.
 
-Installation:
+## Installation
+
+This module is already available in EBRAINS lab,
+but you can also make use of it locally, in which case, execute:
 
     jupyter labextension install @jupyter-widgets/jupyterlab-manager
     jupyter labextension install jupyter-matplotlib
     pip install tvb-widgets
 
+In order to install tvb-widgets from the local repo clone, directly in a notebook, run (in the first cell): 
+
+    %pip install --quiet --upgrade pip
+    %pip install --quiet -e ..
+    %pip install tvb-data
+
+For some of our widgets, where connection to EBRAINS storage is necessary, 
+you should setup as environment variable before launching the local Jupyter Lab instance:
+
+    export CLB_AUTH = "{Your TokenString copied from EBRAINS Collab}"
+
+To retrieve the token string, execute in https://lab.ch.ebrains.eu/:
+
+    clb_oauth.get_token()
+
 #  Acknowledgments
 This project has received funding from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).
 
 
+
```

### Comparing `tvb-widgets-1.2.0/README.md` & `tvb-widgets-1.3.0/tvb_widgets.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,7 +1,22 @@
+Metadata-Version: 2.1
+Name: tvb-widgets
+Version: 1.3.0
+Summary: GUI widgets for EBRAINS showcases
+Home-page: https://github.com/the-virtual-brain/tvb-widgets
+Author: TVB Widgets Team (Juelich SDL Neuroscience, INS - Marseille, Codemart)
+Author-email: tvb.admin@thevirtualbrain.org
+License: GPL-3.0-or-later
+Keywords: tvb widgets jupyterlab ebrains showcases
+Platform: UNKNOWN
+Description-Content-Type: text/markdown
+Provides-Extra: examples
+Provides-Extra: tests
+License-File: LICENSE
+
 # tvb-widgets
 ![Github Actions Status](https://sonarcloud.io/api/project_badges/measure?project=the-virtual-brain_tvb-widgets&metric=alert_status) 
 [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=the-virtual-brain_tvb-widgets&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=the-virtual-brain_tvb-widgets)
 [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=the-virtual-brain_tvb-widgets&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=the-virtual-brain_tvb-widgets) 
 [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=the-virtual-brain_tvb-widgets&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=the-virtual-brain_tvb-widgets)
 
 
@@ -16,20 +31,39 @@
 can be easily deployed in the EBRAINS Collaboratory within the JupyterLab. 
 
 This module is also documented in EBRAINS here: https://wiki.ebrains.eu/bin/view/Collabs/tvb-widgets
 
 These graphic user interface components enable:
  1. Easy setup of models and region specific or cohort simulations. This includes single simulations as well as parameter explorations.
  2. Selection of Data sources and their links to models. This will exploit the backend data access functionality to be developed new in TVB.
- 3. Previews of queried data from Siibra and the KG.
- 4. Deployment of jobs to HPC resources.
- 5. Integration of a subset of TVB analysis and visualisation tools.
- 6. The GUIs must be designed to be integrated into cells in the notebooks and Jupyter notebook extension for HPC resource usage and job tracking will be also developed as independent panels.
+ 3. Integration of a subset of TVB analysis and visualisation tools.
+ 4. The GUIs must be designed to be integrated into cells in the notebooks and Jupyter notebook extension for HPC resource usage and job tracking will be also developed as independent panels.
+
+## Installation
 
-Installation:
+This module is already available in EBRAINS lab,
+but you can also make use of it locally, in which case, execute:
 
     jupyter labextension install @jupyter-widgets/jupyterlab-manager
     jupyter labextension install jupyter-matplotlib
     pip install tvb-widgets
 
+In order to install tvb-widgets from the local repo clone, directly in a notebook, run (in the first cell): 
+
+    %pip install --quiet --upgrade pip
+    %pip install --quiet -e ..
+    %pip install tvb-data
+
+For some of our widgets, where connection to EBRAINS storage is necessary, 
+you should setup as environment variable before launching the local Jupyter Lab instance:
+
+    export CLB_AUTH = "{Your TokenString copied from EBRAINS Collab}"
+
+To retrieve the token string, execute in https://lab.ch.ebrains.eu/:
+
+    clb_oauth.get_token()
+
 #  Acknowledgments
 This project has received funding from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).
+
+
+
```

### Comparing `tvb-widgets-1.2.0/tvb_widgets.egg-info/SOURCES.txt` & `tvb-widgets-1.3.0/tvb_widgets.egg-info/SOURCES.txt`

 * *Files 9% similar despite different names*

```diff
@@ -12,14 +12,17 @@
 tvbwidgets/core/__init__.py
 tvbwidgets/core/auth.py
 tvbwidgets/core/exceptions.py
 tvbwidgets/core/ini_parser.py
 tvbwidgets/core/logger/__init__.py
 tvbwidgets/core/logger/builder.py
 tvbwidgets/core/logger/logging.conf
+tvbwidgets/core/pse/__init__.py
+tvbwidgets/core/pse/parameters.py
+tvbwidgets/core/pse/pse_data.py
 tvbwidgets/core/simulator/__init__.py
 tvbwidgets/core/simulator/model_exporters.py
 tvbwidgets/core/simulator/tvb_integrators.py
 tvbwidgets/tests/__init__.py
 tvbwidgets/tests/constants.py
 tvbwidgets/tests/test_base.py
 tvbwidgets/tests/test_drive_widget.py
@@ -30,12 +33,13 @@
 tvbwidgets/tests/test_tvb_integrators.py
 tvbwidgets/tests/ts_generator.py
 tvbwidgets/ui/__init__.py
 tvbwidgets/ui/base_widget.py
 tvbwidgets/ui/drive_widget.py
 tvbwidgets/ui/head_widget.py
 tvbwidgets/ui/phase_plane_widget.py
+tvbwidgets/ui/pse_launcher_widget.py
 tvbwidgets/ui/pse_widget.py
 tvbwidgets/ui/storage_widget.py
 tvbwidgets/ui/ts_widget.py
 tvbwidgets/ui/ts_widget_help.ini
 tvbwidgets/ui/widget_with_browser.py
```

### Comparing `tvb-widgets-1.2.0/tvbwidgets/__init__.py` & `tvb-widgets-1.3.0/tvbwidgets/__init__.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/auth.py` & `tvb-widgets-1.3.0/tvbwidgets/core/auth.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/exceptions.py` & `tvb-widgets-1.3.0/tvbwidgets/core/exceptions.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/ini_parser.py` & `tvb-widgets-1.3.0/tvbwidgets/core/ini_parser.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/logger/builder.py` & `tvb-widgets-1.3.0/tvbwidgets/core/logger/builder.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/logger/logging.conf` & `tvb-widgets-1.3.0/tvbwidgets/core/logger/logging.conf`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/simulator/model_exporters.py` & `tvb-widgets-1.3.0/tvbwidgets/core/simulator/model_exporters.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/core/simulator/tvb_integrators.py` & `tvb-widgets-1.3.0/tvbwidgets/core/simulator/tvb_integrators.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_base.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_base.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_drive_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_drive_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_exporters.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_exporters.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_head_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_head_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_phase_plane_export.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_phase_plane_export.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/test_ts_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/test_ts_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/tests/ts_generator.py` & `tvb-widgets-1.3.0/tvbwidgets/tests/ts_generator.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/base_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/base_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/drive_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/drive_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/head_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/head_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/phase_plane_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/phase_plane_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/pse_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/pse_widget.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,69 +1,79 @@
 # -*- coding: utf-8 -*-
 #
 # "TheVirtualBrain - Widgets" package
 #
 # (c) 2022-2023, TVB Widgets Team
 #
 
+import os.path
 import plotly.graph_objects as go
 import ipywidgets as widgets
-import numpy as np
 from IPython.core.display_functions import display
+from tvbwidgets.core.exceptions import InvalidInputException
+from tvbwidgets.core.pse.pse_data import PSEData, PSEStorage
 from tvbwidgets.ui.base_widget import TVBWidget
 
 
 class PSEWidget(TVBWidget):
     """Visualize PSE results"""
 
-    def __init__(self, data, x_title, y_title, x_value, y_value, metrics_names, **kwargs):
-        # type: (np.ndarray, str, str, list, list, list, dict) -> None
+    def __init__(self, file_name, **kwargs):
+        # type: (str, dict) -> None
         """
-        :param data: Numpy array with metrics data
-        :param x_title: Title of X axis
-        :param y_title: Title of Y axis
-        :param x_value: List consists of X axis range(min, max) and a step, ex: [0, 30, 2]
-        :param y_value: List consists of Y axis range(min, max) and a step
-        :param metrics_names: Representative names for each metrics
+        :param file_name: path to the file_name that contains the data necessary for the visualization
         """
         super().__init__(**kwargs)
-        self.x_title = x_title
-        self.y_title = y_title
-        self.x_value = x_value
-        self.y_value = y_value
-        self.data = data
-        self.metrics_names = metrics_names
+        if not os.path.exists(file_name):
+            raise InvalidInputException(f"File {file_name} was not found!")
+        self.file_name = file_name
+        self.param1_title = None
+        self.param2_title = None
+        self.param1_value = None
+        self.param2_value = None
+        self.data = None
+        self.metrics_names = []
         self.dict_metrics = {}
         self.figure = None
         self.smooth_effect_cb = None
         self.change_color_dd = None
         self.metrics_change_dd = None
+        self.read_h5_file()
         self._map_names_to_metrics()
         self._create_visualizer()
 
+    def read_h5_file(self):
+        pse_result = PSEData()
+        PSEStorage(self.file_name).load_into(pse_result)
+        self.param1_title = pse_result.x_title
+        self.param2_title = pse_result.y_title
+        self.param1_value = pse_result.x_value
+        self.param2_value = pse_result.y_value
+        self.metrics_names = pse_result.metrics_names
+        self.data = pse_result.results
+
     def _map_names_to_metrics(self):
         for index in range(self.metrics_names.__len__()):
             self.dict_metrics[self.metrics_names[index]] = self.data[index]
 
     def _create_visualizer(self):
+        self.param1_value = [str(elem) for elem in self.param1_value]
+        self.param2_value = [str(elem) for elem in self.param2_value]
         pse_layout = go.Layout(width=1000, height=500,
-                               xaxis=go.layout.XAxis(linecolor='black', linewidth=1, mirror=True, title=self.x_title,
-                                                     range=[self.x_value[0], self.x_value[1]], dtick=self.x_value[2]),
-                               yaxis=go.layout.YAxis(linecolor='black', linewidth=1, mirror=True, title=self.y_title,
-                                                     range=[self.y_value[0], self.y_value[1]], dtick=self.y_value[2]),
-                               margin=go.layout.Margin(
-                                   l=100,
-                                   r=50,
-                                   b=100,
-                                   t=100,
-                                   pad=4), title="PSE Visualizer", titlefont=dict(size=20, family='Arial, sans-serif'),
-                               )
+                               xaxis=go.layout.XAxis(linecolor='black', linewidth=1, mirror=True,
+                                                     title=self.param2_title),
+                               yaxis=go.layout.YAxis(linecolor='black', linewidth=1, mirror=True,
+                                                     title=self.param1_title),
+                               margin=go.layout.Margin(l=100, r=50, b=100, t=100, pad=4), title="PSE Visualizer",
+                               titlefont=dict(size=20, family='Arial, sans-serif'), )
         self.figure = go.FigureWidget(layout=pse_layout)
-        self.figure.add_trace(go.Heatmap(z=list(self.dict_metrics.values())[0], colorscale='RdBu', showscale=True,
-                                         zsmooth='best'))
+
+        self.figure.add_trace(go.Heatmap(z=list(self.dict_metrics.values())[0], x=self.param2_value, y=self.param1_value
+                                         , colorscale='RdBu', connectgaps=False, showscale=True, zsmooth='best'))
+
         self._populate_features()
 
     def _populate_features(self):
         self._smooth_effect()
         self._colors_options()
         self._metrics_options()
         features_vbox = widgets.VBox(children=[self.smooth_effect_cb, self.change_color_dd,
@@ -71,15 +81,15 @@
         features_accordion = widgets.Accordion(children=[features_vbox], selected_index=None,
                                                layout=widgets.Layout(width='25%', marginTop='100px'))
         features_accordion.set_title(0, 'Features')
         table = widgets.HBox([features_accordion, self.figure], layout=self.DEFAULT_BORDER)
         display(table)
 
     def _smooth_effect(self):
-        self.smooth_effect_cb = widgets.Checkbox(True, description='Smooth visualizer',
+        self.smooth_effect_cb = widgets.Checkbox(value=True, description='Smooth visualizer',
                                                  layout=widgets.Layout(margin='10px 0px 10px 0px'))
 
         def smooth_effect_changed(change):
             if change['type'] != 'change' or change['name'] != 'value':
                 return
 
             if change['new']:
```

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/storage_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/storage_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/ts_widget.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/ts_widget.py`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/ts_widget_help.ini` & `tvb-widgets-1.3.0/tvbwidgets/ui/ts_widget_help.ini`

 * *Files identical despite different names*

### Comparing `tvb-widgets-1.2.0/tvbwidgets/ui/widget_with_browser.py` & `tvb-widgets-1.3.0/tvbwidgets/ui/widget_with_browser.py`

 * *Files identical despite different names*

