# Comparing `tmp/mkdocs-placeholder-plugin-0.2.5.tar.gz` & `tmp/mkdocs-placeholder-plugin-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mkdocs-placeholder-plugin-0.2.5.tar", last modified: Sun Mar  5 16:38:50 2023, max compression
+gzip compressed data, was "mkdocs-placeholder-plugin-0.3.0.tar", last modified: Fri Apr  7 11:56:56 2023, max compression
```

## Comparing `mkdocs-placeholder-plugin-0.2.5.tar` & `mkdocs-placeholder-plugin-0.3.0.tar`

### file list

```diff
@@ -1,41 +1,34 @@
-drwxr-xr-x   0 user       (501) staff       (20)        0 2023-03-05 16:38:50.096840 mkdocs-placeholder-plugin-0.2.5/
--rw-r--r--   0 user       (501) staff       (20)     1063 2022-07-29 16:34:40.000000 mkdocs-placeholder-plugin-0.2.5/LICENSE
--rw-r--r--   0 user       (501) staff       (20)       69 2023-02-08 16:55:48.000000 mkdocs-placeholder-plugin-0.2.5/MANIFEST.in
--rw-r--r--   0 user       (501) staff       (20)     5821 2023-03-05 16:38:50.096916 mkdocs-placeholder-plugin-0.2.5/PKG-INFO
--rw-r--r--   0 user       (501) staff       (20)     5183 2023-03-05 16:35:43.000000 mkdocs-placeholder-plugin-0.2.5/README.md
--rw-r--r--   0 user       (501) staff       (20)       85 2022-07-29 16:34:40.000000 mkdocs-placeholder-plugin-0.2.5/pyproject.toml
--rw-r--r--   0 user       (501) staff       (20)      943 2023-03-05 16:38:50.097174 mkdocs-placeholder-plugin-0.2.5/setup.cfg
-drwxr-xr-x   0 user       (501) staff       (20)        0 2023-03-05 16:38:50.089525 mkdocs-placeholder-plugin-0.2.5/src/
--rwxr-xr-x   0 user       (501) staff       (20)     1467 2022-12-31 08:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs-placeholder-replace-static.py
-drwxr-xr-x   0 user       (501) staff       (20)        0 2023-03-05 16:38:50.092905 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/
--rw-r--r--   0 user       (501) staff       (20)      626 2022-09-10 08:23:28.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/__init__.py
--rw-r--r--   0 user       (501) staff       (20)     4816 2023-02-25 18:44:15.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/assets.py
--rw-r--r--   0 user       (501) staff       (20)     3275 2023-03-05 14:38:09.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/auto_input_table.py
--rw-r--r--   0 user       (501) staff       (20)     1315 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/html_tag_parser.py
--rw-r--r--   0 user       (501) staff       (20)     8119 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/input_table.py
--rw-r--r--   0 user       (501) staff       (20)     4122 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/input_tag_handler.py
-drwxr-xr-x   0 user       (501) staff       (20)        0 2023-03-05 16:38:50.096601 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/
--rw-r--r--   0 user       (501) staff       (20)       96 2023-02-18 14:42:01.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/00_init.js
--rw-r--r--   0 user       (501) staff       (20)     4589 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/10_parse_data.js
--rw-r--r--   0 user       (501) staff       (20)     1373 2023-02-12 13:15:54.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/15_debug.js
--rw-r--r--   0 user       (501) staff       (20)     5332 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/20_placeholder_state.js
--rw-r--r--   0 user       (501) staff       (20)     6379 2023-03-05 14:53:27.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/30_input.js
--rw-r--r--   0 user       (501) staff       (20)     7886 2023-03-04 17:38:53.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/35_input_validators.js
--rw-r--r--   0 user       (501) staff       (20)     2701 2023-03-04 18:15:38.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/40_replace.js
--rw-r--r--   0 user       (501) staff       (20)     6146 2023-03-05 15:36:07.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/60_auto_tables.js
--rw-r--r--   0 user       (501) staff       (20)      456 2023-03-04 18:16:11.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/80_style.js
--rw-r--r--   0 user       (501) staff       (20)      992 2023-02-18 14:41:48.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/javascript/90_trigger_actions.js
--rw-r--r--   0 user       (501) staff       (20)    13727 2023-03-05 16:18:13.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/placeholder_data.py
--rw-r--r--   0 user       (501) staff       (20)     5303 2023-02-12 12:18:01.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/plugin.py
--rw-r--r--   0 user       (501) staff       (20)     2039 2023-02-19 09:31:34.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/plugin_config.py
--rw-r--r--   0 user       (501) staff       (20)     5202 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/static_replacer.py
--rw-r--r--   0 user       (501) staff       (20)     1807 2023-03-05 15:36:07.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/style.py
--rw-r--r--   0 user       (501) staff       (20)     4999 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/validators.py
--rw-r--r--   0 user       (501) staff       (20)     8540 2023-03-04 11:11:53.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/validators_predefined.py
-drwxr-xr-x   0 user       (501) staff       (20)        0 2023-03-05 16:38:50.093751 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/
--rw-r--r--   0 user       (501) staff       (20)     5821 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/PKG-INFO
--rw-r--r--   0 user       (501) staff       (20)     1591 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/SOURCES.txt
--rw-r--r--   0 user       (501) staff       (20)        1 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/dependency_links.txt
--rw-r--r--   0 user       (501) staff       (20)       75 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/entry_points.txt
--rw-r--r--   0 user       (501) staff       (20)       14 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/requires.txt
--rw-r--r--   0 user       (501) staff       (20)       26 2023-03-05 16:38:50.000000 mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/top_level.txt
+drwxr-xr-x   0 user       (501) staff       (20)        0 2023-04-07 11:56:56.600991 mkdocs-placeholder-plugin-0.3.0/
+-rw-r--r--   0 user       (501) staff       (20)     1063 2022-07-29 16:34:40.000000 mkdocs-placeholder-plugin-0.3.0/LICENSE
+-rw-r--r--   0 user       (501) staff       (20)       65 2023-03-27 05:22:55.000000 mkdocs-placeholder-plugin-0.3.0/MANIFEST.in
+-rw-r--r--   0 user       (501) staff       (20)     7156 2023-04-07 11:56:56.601042 mkdocs-placeholder-plugin-0.3.0/PKG-INFO
+-rw-r--r--   0 user       (501) staff       (20)     6518 2023-04-07 11:55:42.000000 mkdocs-placeholder-plugin-0.3.0/README.md
+-rw-r--r--   0 user       (501) staff       (20)       85 2022-07-29 16:34:40.000000 mkdocs-placeholder-plugin-0.3.0/pyproject.toml
+-rw-r--r--   0 user       (501) staff       (20)      943 2023-04-07 11:56:56.601284 mkdocs-placeholder-plugin-0.3.0/setup.cfg
+drwxr-xr-x   0 user       (501) staff       (20)        0 2023-04-07 11:56:56.596497 mkdocs-placeholder-plugin-0.3.0/src/
+-rwxr-xr-x   0 user       (501) staff       (20)     1467 2022-12-31 08:17:05.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs-placeholder-replace-static.py
+drwxr-xr-x   0 user       (501) staff       (20)        0 2023-04-07 11:56:56.599514 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/
+-rw-r--r--   0 user       (501) staff       (20)      626 2022-09-10 08:23:28.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/__init__.py
+drwxr-xr-x   0 user       (501) staff       (20)        0 2023-04-07 11:56:56.600844 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets/
+-rw-r--r--   0 user       (501) staff       (20)      312 2023-03-27 05:34:32.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets/placeholder-data.js
+-rw-------   0 user       (501) staff       (20)    21736 2023-04-07 11:52:41.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets/placeholder.min.js
+-rw-------   0 user       (501) staff       (20)    91944 2023-04-07 11:52:41.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets/placeholder.min.js.map
+-rw-r--r--   0 user       (501) staff       (20)     5288 2023-04-02 08:07:34.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets.py
+-rw-r--r--   0 user       (501) staff       (20)     3275 2023-03-05 14:38:09.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/auto_input_table.py
+-rw-r--r--   0 user       (501) staff       (20)     1315 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/html_tag_parser.py
+-rw-r--r--   0 user       (501) staff       (20)     8119 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/input_table.py
+-rw-r--r--   0 user       (501) staff       (20)     4122 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/input_tag_handler.py
+-rw-r--r--   0 user       (501) staff       (20)    13905 2023-03-28 17:35:35.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/placeholder_data.py
+-rw-r--r--   0 user       (501) staff       (20)     5699 2023-03-31 17:41:46.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/plugin.py
+-rw-r--r--   0 user       (501) staff       (20)     2239 2023-03-31 17:42:43.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/plugin_config.py
+-rw-r--r--   0 user       (501) staff       (20)     5202 2023-03-04 18:17:05.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/static_replacer.py
+-rw-r--r--   0 user       (501) staff       (20)     2196 2023-04-01 12:57:06.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/style.py
+-rw-r--r--   0 user       (501) staff       (20)     5043 2023-03-28 17:34:25.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/validators.py
+-rw-r--r--   0 user       (501) staff       (20)     8885 2023-03-28 17:25:38.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/validators_predefined.py
+drwxr-xr-x   0 user       (501) staff       (20)        0 2023-04-07 11:56:56.600334 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/
+-rw-r--r--   0 user       (501) staff       (20)     7156 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/PKG-INFO
+-rw-r--r--   0 user       (501) staff       (20)     1189 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/SOURCES.txt
+-rw-r--r--   0 user       (501) staff       (20)        1 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/dependency_links.txt
+-rw-r--r--   0 user       (501) staff       (20)       75 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/entry_points.txt
+-rw-r--r--   0 user       (501) staff       (20)       14 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/requires.txt
+-rw-r--r--   0 user       (501) staff       (20)       26 2023-04-07 11:56:56.000000 mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/top_level.txt
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/LICENSE` & `mkdocs-placeholder-plugin-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/PKG-INFO` & `mkdocs-placeholder-plugin-0.3.0/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkdocs-placeholder-plugin
-Version: 0.2.5
+Version: 0.3.0
 Summary: Add dynamic placeholders to your mkdocs page
 Home-page: https://github.com/six-two/mkdocs-placeholder-plugin
 Author: six-two
 Author-email: pip@six-two.dev
 License: MIT License
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
@@ -38,16 +38,34 @@
 python3 -m pip install git+https://github.com/six-two/mkdocs-placeholder-plugin
 ```
 
 The corresponding documentation is hosted at <https://dev.mkdocs-placeholder-plugin.six-two.dev>.
 
 ## Notable changes
 
+### TODOs
+
+- Rewrite python code and decouple it from MkDocs (to be able to use it with other projects).
+- Implement propper exception handling for TypeScript code to recover from / compartmentalize non-critical errors.
+- Update the documentation.
+
 ### HEAD
 
+### Version 0.3.0
+
+This release may be a bit buggy due to the rewrite and the documentation is not entirely accurate yet.
+I will update the docs after I also clean up / rewrite the python code (planed for v0.4.0).
+
+- Rewrote the JavaScript code in TypeScript:
+    - Packed and minified using Webpack, so the file is a bit smaller
+    - Should find stupid errors I make in code paths that I do not test (often)
+    - Sophisticated update logic: Instead of always reloading the page it tries to update the DOM in-place (if possible), which should improve user experience a bit and is much faster
+    - Recursive placeholders (placeholders that contain placeholders that contain placeholder...) no longer need to be specified in a speific order in the configuration file.
+    - A placeholder's `default-function` and a validator rule's `match_function` are now evaluated using [`new Function(...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) instead of `eval(...)`, so you need to add a return statement.
+
 ### Version 0.2.5
 
 - When an JavaScript generated `auto-input-table` is empty, now a info box is shown (instead of nothing / an empty table).
 - Bugfixes:
     - `auto_placeholder_tables_javascript` had no effect.
     - Pressing `Enter` on text fields without validators did not try to reload the page,
 
@@ -127,8 +145,9 @@
 2. Update the changelog in this README file.
 3. Update version number in `setup.cfg`.
 4. Build and update package.
 5. Create a commit for the release (`Version 0.X.Y`) and push it.
 6. Update the `latest-release` branch, so that the documentation website gets updated:
     ```
     git branch --force latest-release HEAD
+    git push origin latest-release
     ```
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/README.md` & `mkdocs-placeholder-plugin-0.3.0/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -20,16 +20,34 @@
 python3 -m pip install git+https://github.com/six-two/mkdocs-placeholder-plugin
 ```
 
 The corresponding documentation is hosted at <https://dev.mkdocs-placeholder-plugin.six-two.dev>.
 
 ## Notable changes
 
+### TODOs
+
+- Rewrite python code and decouple it from MkDocs (to be able to use it with other projects).
+- Implement propper exception handling for TypeScript code to recover from / compartmentalize non-critical errors.
+- Update the documentation.
+
 ### HEAD
 
+### Version 0.3.0
+
+This release may be a bit buggy due to the rewrite and the documentation is not entirely accurate yet.
+I will update the docs after I also clean up / rewrite the python code (planed for v0.4.0).
+
+- Rewrote the JavaScript code in TypeScript:
+    - Packed and minified using Webpack, so the file is a bit smaller
+    - Should find stupid errors I make in code paths that I do not test (often)
+    - Sophisticated update logic: Instead of always reloading the page it tries to update the DOM in-place (if possible), which should improve user experience a bit and is much faster
+    - Recursive placeholders (placeholders that contain placeholders that contain placeholder...) no longer need to be specified in a speific order in the configuration file.
+    - A placeholder's `default-function` and a validator rule's `match_function` are now evaluated using [`new Function(...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) instead of `eval(...)`, so you need to add a return statement.
+
 ### Version 0.2.5
 
 - When an JavaScript generated `auto-input-table` is empty, now a info box is shown (instead of nothing / an empty table).
 - Bugfixes:
     - `auto_placeholder_tables_javascript` had no effect.
     - Pressing `Enter` on text fields without validators did not try to reload the page,
 
@@ -109,8 +127,9 @@
 2. Update the changelog in this README file.
 3. Update version number in `setup.cfg`.
 4. Build and update package.
 5. Create a commit for the release (`Version 0.X.Y`) and push it.
 6. Update the `latest-release` branch, so that the documentation website gets updated:
     ```
     git branch --force latest-release HEAD
+    git push origin latest-release
     ```
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/setup.cfg` & `mkdocs-placeholder-plugin-0.3.0/setup.cfg`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = mkdocs-placeholder-plugin
-version = 0.2.5
+version = 0.3.0
 author = six-two
 author_email = pip@six-two.dev
 description = Add dynamic placeholders to your mkdocs page
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/six-two/mkdocs-placeholder-plugin
 license = MIT License
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs-placeholder-replace-static.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs-placeholder-replace-static.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/__init__.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/__init__.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/assets.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/assets.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,118 +1,127 @@
 import json
 import os
+import shutil
 from typing import Any
 # local
 from mkdocs.config.defaults import MkDocsConfig
 from .plugin_config import PlaceholderPluginConfig
 from .placeholder_data import Placeholder, InputType
 from .style import generate_style_sheet
 from .validators import validator_to_dict
 
 
+def _write_to_file(config: MkDocsConfig, relative_path: str, contents: str, open_mode: str) -> None:
+    file_path = os.path.join(config.site_dir, relative_path)
+    parent_dir = os.path.dirname(file_path)
+    os.makedirs(parent_dir, exist_ok=True)
+    with open(file_path, open_mode) as f:
+        f.write(contents)
+
 def copy_assets_to_mkdocs_site_directory(config: MkDocsConfig, plugin_config: PlaceholderPluginConfig, placeholders: dict[str, Placeholder]):
     """
     Copy the JavaScript file to the site (if necessary) and replace the placeholder string with the actual data
     """
+    # @TODO: merge everything into a single file if debug==false
     custom_js_path = os.path.join(config.site_dir, plugin_config.placeholder_js)
     if os.path.exists(custom_js_path):
         # use the file that is already in the site directory
         with open(custom_js_path, "r") as f:
             text = f.read()
     else:
         # use the default file supplied by the plugin
-        text = ""
-        current_dir = os.path.dirname(__file__)
-        js_dir = os.path.join(current_dir, "javascript")
-        for file_name in sorted(os.listdir(js_dir)):
-            with open(os.path.join(js_dir, file_name), "r") as f:
-                text += f.read()
-        # input_file = get_resource_path("../javascript/placeholder-plugin.js")
+        input_file = get_resource_path("assets/placeholder-data.js")
+        with open(input_file, "r") as f:
+            text = f.read()
+
+    if plugin_config.placeholder_css:
+        theme_name = config.theme.name or "mkdocs"
+        css_text = generate_style_sheet(theme_name, plugin_config.debug_javascript)
+        _write_to_file(config, plugin_config.placeholder_css, css_text, "a")
 
     # Add extra JS
     if (plugin_config.placeholder_extra_js):
         with open(plugin_config.placeholder_extra_js, "r") as f:
             extra_js = f.read()
 
         text = "///// Custom extra JS code /////\n" + extra_js + "\n///// Normal JS code /////\n" + text
 
     # Generate placeholder data and inject them in the JavaScript file
-    theme_name = config.theme.name or "mkdocs"
-    placeholder_data_json = generate_placeholder_json(theme_name, placeholders, plugin_config)
-    text = text.replace("__MKDOCS_PLACEHOLDER_PLUGIN_JSON__", placeholder_data_json)
+    text = text.replace("__MKDOCS_PLACEHOLDER_PLUGIN_NEW_JSON__", generate_new_placeholder_json(placeholders, plugin_config))
+    _write_to_file(config, plugin_config.placeholder_js, text, "w")
 
-    # write back the results
     parent_dir = os.path.dirname(custom_js_path)
-    os.makedirs(parent_dir, exist_ok=True)
-    with open(custom_js_path, "w") as f:
-        f.write(text)
+    shutil.copy(get_resource_path("assets/placeholder.min.js"), parent_dir)
+    shutil.copy(get_resource_path("assets/placeholder.min.js.map"), parent_dir)
 
 
 def get_resource_path(name: str) -> str:
     """
     Gets the path to a file in the same directory as this file
     """
     current_dir = os.path.dirname(__file__)
     return os.path.join(current_dir, name)
 
 
-def generate_placeholder_json(theme_name: str, placeholders: dict[str, Placeholder], plugin_config: PlaceholderPluginConfig) -> str:
+def generate_new_placeholder_json(placeholders: dict[str, Placeholder], plugin_config: PlaceholderPluginConfig) -> str:
     """
     Generate the JSON string, that will replace the placeholder in the JavaScript file
     """
-    checkbox_data = {}
-    dropdown_data = {}
-    textbox_data = {}
-    common_data = {}
+    placeholder_data_list = []
+    validator_map = {}
 
     for placeholder in placeholders.values():
+        placeholder_data = {
+            "name": placeholder.name,
+            "description": placeholder.description,
+            "read_only": placeholder.read_only,
+            "allow_inner_html": placeholder.replace_everywhere,
+        }
         if placeholder.input_type == InputType.Checkbox:
-            checkbox_data[placeholder.name] = {
-                "default_value": bool(placeholder.default_value == "checked"),
-                "checked": placeholder.values["checked"],
-                "unchecked": placeholder.values["unchecked"],
-            }
+            placeholder_data.update({
+                "type": "checkbox",
+                "value_checked": placeholder.values["checked"],
+                "value_unchecked": placeholder.values["unchecked"],
+                "checked_by_default": bool(placeholder.default_value == "checked"),
+            })
         elif placeholder.input_type == InputType.Dropdown:
             # Figure out the index of the item selected by default
             default_index = 0
             for index, value in enumerate(placeholder.values.keys()):
                 if placeholder.default_value == value:
                     default_index = index
 
-            dropdown_data[placeholder.name] = {
+            placeholder_data.update({
+                "type": "dropdown",
                 "default_index": default_index,
-                "options": [[key, value] for key, value in placeholder.values.items()],
-            }
+                "options": [{"display_name": key, "value": value} for key, value in placeholder.values.items()],
+            })
         elif placeholder.input_type == InputType.Field:
-            td: dict[str, Any] = {}
+            placeholder_data.update({
+                "type": "textbox",
+                "allow_recursive": True, # @TODO: read from config
+                "validators": [v.id for v in placeholder.validator_list],
+            })
+
             if placeholder.default_function:
-                td["value_function"] = placeholder.default_function
+                placeholder_data["default_function"] = placeholder.default_function
             else:
-                td["value"] = placeholder.default_value
+                placeholder_data["default_value"] = placeholder.default_value
 
-            if placeholder.validator_list:
-                td["validators"] = [validator_to_dict(v) for v in placeholder.validator_list]
-            textbox_data[placeholder.name] = td
         else:
             raise Exception(f"Unexpected input type: {placeholder.input_type}")
 
-        common_data[placeholder.name] = {
-            "description": placeholder.description,
-            "read_only": placeholder.read_only,
-            "replace_everywhere": placeholder.replace_everywhere,
-        }
+        placeholder_data_list.append(placeholder_data)
 
-    custom_css = generate_style_sheet(theme_name)
+        for validator in placeholder.validator_list:
+            # deduplicate validators
+            validator_map[validator.id] = validator_to_dict(validator)
 
     result_object = {
-        "checkbox": checkbox_data,
-        "custom_css": custom_css,
-        "dropdown": dropdown_data,
-        "common": common_data,
-        "textbox": textbox_data,
-        "delay_millis": plugin_config.replace_delay_millis,
-        "auto_table_apply_button": plugin_config.add_apply_table_column,
-        "auto_table_hide_read_only": not plugin_config.table_default_show_readonly,
-        "reload": plugin_config.reload_on_change,
-        "debug": plugin_config.debug_javascript,
+        "placeholder_list": placeholder_data_list,
+        "settings": {
+            "debug": plugin_config.debug_javascript,
+            "delay_millis": plugin_config.replace_delay_millis,
+        },
+        "validators": list(validator_map.values()),
     }
     return json.dumps(result_object, indent=None, sort_keys=False)
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/auto_input_table.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/auto_input_table.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/html_tag_parser.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/html_tag_parser.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/input_table.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/input_table.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/input_tag_handler.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/input_tag_handler.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/placeholder_data.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/placeholder_data.py`

 * *Files 2% similar despite different names*

```diff
@@ -237,27 +237,32 @@
             warning(f"Placeholder {placeholder_name} has field 'validators', but is not a text field. Any validators for it will be ignored.")
 
     return validator_list
 
 
 def parse_validator_object(data: dict[str,Any]) -> Validator:
     try:
+        id = data["id"]
+        if type(id) != str:
+            raise PluginError(f"Wrong type for key 'name': Expected 'string', got '{type(id).__name__}'")
+
         name = data["name"]
         if type(name) != str:
             raise PluginError(f"Wrong type for key 'name': Expected 'string', got '{type(name).__name__}'")
 
         rules_data = data["rules"]
         if type(rules_data) != list:
             raise PluginError(f"Wrong type for key 'rules_data': Expected 'list', got '{type(rules_data).__name__}'")
 
         if not rules_data:
             raise PluginError("Validators neet to have at least a rule, but received an empty list")
 
         rules = [parse_validator_rule(x) for x in rules_data]
         return Validator(
+            id=id,
             name=name,
             rules=rules,
         )
     except Exception as ex:
         message = f"Missing key {ex}" if type(ex) == KeyError else str(ex)
         raise PluginError(f"{message}\n\nCaused by validator: {json.dumps(data, indent=4)}")
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/plugin.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/plugin.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 from functools import wraps
+import os
 import traceback
 from typing import Callable
 # pip dependency
 from mkdocs.config.defaults import MkDocsConfig
 from mkdocs.plugins import BasePlugin
 from mkdocs.config.base import Config
 from mkdocs.exceptions import PluginError
@@ -78,18 +79,26 @@
         if self.config.enabled:
             self.after_build_action(config)
 
     def initialize_plugin(self, config: MkDocsConfig) -> None:
         set_warnings_enabled(self.config.show_warnings)
 
         # Make sure that the custom JS is included on every page
-        custom_js_path = self.config.placeholder_js
-        extra_js = config.extra_javascript
-        if custom_js_path not in extra_js:
-            extra_js.append(custom_js_path)
+        if self.config.placeholder_js not in config.extra_javascript:
+            config.extra_javascript.append(self.config.placeholder_js)
+
+        # Make sure that the custom CSS is included on every page
+        if self.config.placeholder_css:
+            if self.config.placeholder_css not in config.extra_css:
+                config.extra_css.append(self.config.placeholder_css)
+
+        # @TODO: fix later
+        relative_site_dir = os.path.dirname(self.config.placeholder_js)
+        config.extra_javascript.append(f"{relative_site_dir}/placeholder.min.js")
+
 
         # Immediatley parse the placeholder file, so that all following methods can use the information
         placeholder_file = self.config.placeholder_file
         self.placeholders = load_placeholder_data(placeholder_file)
 
         # Instanciate a table generator
         self.table_generator = InputTableGenerator(self.placeholders,
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/plugin_config.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/plugin_config.py`

 * *Files 11% similar despite different names*

```diff
@@ -28,10 +28,12 @@
     placeholder_file = Type(str, default="placeholder-plugin.yaml")
     # Output loaction for the custom JS file. This overwrites the javascript code provided by the plugin
     placeholder_js = Type(str, default="assets/javascripts/placeholder-plugin.js")
     # Provide additional javascript for example for hooks, providing functions, etc
     placeholder_extra_js = Type(str, default="")
     # Replace delay millis
     replace_delay_millis = Type(int, default=0)
+    # CSS file. If it exists, the contents will be appended to. add empty string to not include the default styles
+    placeholder_css = Type(str, default="assets/javascripts/placeholder-plugin.css")
     # Default values for place4holder input tables
     table_default_show_readonly = Type(bool, default=False)
     table_default_type = Type(str, default="simple")
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/static_replacer.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/static_replacer.py`

 * *Files identical despite different names*

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/style.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/style.py`

 * *Files 9% similar despite different names*

```diff
@@ -16,15 +16,16 @@
     background-color: #f7dd67;
     color: black;
 }
 
 table tr td button.placeholder-input-apply-button,
 table tr td input.input-for-variable,
 table tr td select.placeholder-dropdown {
-    min-width: max(200px, 100%);
+    min-width: min(30vw, 200px);
+    max-width: initial;
 }
 
 table tr td input.input-for-variable[type="checkbox"] {
     min-width: initial;
 }
 
 .auto-input-table .info-message {
@@ -47,15 +48,33 @@
 
 .input-for-variable:focus {
     border: 4px solid var(--md-primary-fg-color);
     padding: 3px;
 }
 """
 
-def generate_style_sheet(theme_name: str):
+HIGHLIGHT_STYLE = """
+.placeholder-value {
+    background-color: #aaa;
+    padding: 3px;
+    border-radius: 3px;
+}
+"""
+
+def generate_style_sheet(theme_name: str, debug: bool):
+    theme = _generate_theme_style_sheet(theme_name)
+    
+    if debug:
+        # For highlighting stuff, useful during debugging
+        theme += HIGHLIGHT_STYLE
+
+    return theme
+
+
+def _generate_theme_style_sheet(theme_name: str):
     if theme_name == "material":
         # MkDocs for Material screws up the look of imput elements (makes them look really bad)
         # So I implemented some rough fixes that should fit in with the users color choices
         return BASIC_STYLE + MATERIAL_STYLE
     elif theme_name in ["mkdocs", "readthedocs"]:
         # These themes have been tested (at some point in the past) and should work ok.
         # No specific tweaks were needed
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/validators.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/validators.py`

 * *Files 4% similar despite different names*

```diff
@@ -46,22 +46,24 @@
         match_function="",
         should_match=False,
         error_message=error_message,
     )
 
 
 class Validator(NamedTuple):
+    id: str
     name: str
     rules: list[ValidatorRule]
 
 
 def validator_to_dict(v: Validator) -> dict:
     try:
         return {
-            "name": v.name,
+            "id": v.id,
+            "display_name": v.name,
             "rules": [validator_rule_to_dict(r) for r in v.rules],
         }
     except Exception as ex:
         raise PluginError(f"Error while converting validator '{v.name}' to dictionary: {ex}")
 
 def validator_rule_to_dict(r: ValidatorRule) -> dict:
     data = {
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin/validators_predefined.py` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin/validators_predefined.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,100 +13,109 @@
 # Source: https://ihateregex.io/expr/ipv6/
 # Not great, does not match that well
 MEDIOCRE_IPV6_REGEX = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
 
 def generate_url_http_validator() -> Validator:
     # source: https://urlregex.com. Modified to handle the fragment part (what comes after #)
     return Validator(
+        id="url_http",
         name="URL (HTTP / HTTPS)",
         rules=[
             must_match("^https?://", "Needs to start with 'http://' or 'https://'"),
             RULE_URL_NO_WHITESPACE,
             should_match(f"^{URL_REGEX}$", "Expected an value like https://example.com/some/page.php?x=1&y=some%20value"),
         ]
     )
 
 def generate_file_name_linux_validator() -> Validator:
     return Validator(
+        id="file_name_linux",
         name="File name",
         rules=[
             RULE_NOT_EMPTY,
             must_not_match("/", "Can not contain path separators (slash)"),
             RULE_WARN_WHITESPACE,
         ]
     )
 
 def generate_file_name_windows_validator() -> Validator:
     return Validator(
+        id="file_name_windows",
         name="File name",
         rules=[
             RULE_NOT_EMPTY,
             must_not_match(r"[/\\]", "Can not contain path separators (slash or backslash)"),
             must_not_match('[<>:"|?*]', 'Can not contain prohibited characters: \'<>:"|?*\''),
             RULE_WARN_WHITESPACE,
         ]
     )
 
 
 def generate_path_linux_validator() -> Validator:
     return Validator(
+        id="path_linux",
         name="File path (Linux)",
         rules=[
             RULE_NOT_EMPTY,
             RULE_WARN_WHITESPACE,
         ]
     )
 
 def generate_path_windows_validator() -> Validator:
     return Validator(
+        id="path_windows",
         name="File path (Windows)",
         rules=[
             RULE_NOT_EMPTY,
             # Colon may be in 'C:\...' (and maybe for a port number in an UNC path?)
             should_not_match('[<>"|?*]', 'Can not contain prohibited characters: \'<>"|?*\''),
             RULE_WARN_WHITESPACE,
         ]
     )
 
 
 def generate_url_validator() -> Validator:
     # source: https://urlregex.com. Modified to handle the fragment part (what comes after #)
     return Validator(
+        id="url_any",
         name="URL (any protocol)",
         rules=[
             RULE_URL_NO_WHITESPACE,
             should_match(f"^{URL_REGEX}$", "Expected an value like smb://example.com:10445/share/some-file.txt"),
         ]
     )
 
 def generate_ipv6_validator() -> Validator:
     return Validator(
+        id="ipv6_address",
         name="IPv6 address",
         rules=[
             must_match("^[0-9a-fA-F:.\\[\\]]+$", "Only numbers, the letters A-F, colons, dots, and square brackets are allowed"),
             should_match(f"^{MEDIOCRE_IPV6_REGEX}$", "Should probably look like '2001:0db8:85a3:0000:0000:8a2e:0370:7334' or '::1'"),
             should_not_match(f"^{IPV4_ADDRESS}$", "Should not be an IPv4 address. If you want a IPv4-mapped IPv6 address, prefix it with '::FFFF:' like this: '::FFFF:123.4.56.78'"),
 
         ]
     )
 
 
 def generate_ipv4_validator() -> Validator:
     return Validator(
+        id="ipv4_address",
         name="IPv4 address",
         rules=[
             must_match("^[0-9.]+$", "Only numbers and dots are allowed"),
             # There are other ways of specifying IP addresses, that not all software understands. For example: 2130706433, 017700000001, and 127.1 are alternative representations of 127.0.0.1
             # So we just filter for expected characters, but not for the pattern
             should_match(f"^{IPV4_ADDRESS}$", "Expected an value like 123.4.56.78"),
         ]
     )
 
 def generate_ipv4_range_cidr_validator() -> Validator:
     return Validator(
+        id="ipv4_range_cidr",
         name="IPv4 adress range (CIDR notation)",
         rules=[
             must_match("^[0-9./]+$", "Only numbers, dots and a slash are allowed"),
             must_not_match("/.*/", "May only contain one slash"),
             must_match(f"{CIDR_SUFFIX}$", "The number after that slash needs to be between 0 and 32 (inclusive)"),
             # There are other ways of specifying IP addresses, that not all software understands. For example: 2130706433, 017700000001, and 127.1 are alternative representations of 127.0.0.1
             # So we just filter for expected characters, but not for the pattern
@@ -115,14 +124,15 @@
     )
 
 
 def generate_ipv4_range_dash_validator() -> Validator:
     IPV4_SEGMENT_DASH = f"{IPV4_SEGMENT}(-{IPV4_SEGMENT})?"
     IPV4_ADDRESS_DASHES = f"{IPV4_SEGMENT_DASH}(?:\\.{IPV4_SEGMENT_DASH}){{3}}"
     return Validator(
+        id="ipv4_range_dashes",
         name="IPv4 adress range (dash)",
         rules=[
             must_match("^[0-9-.]+$", "Only numbers, dots and minuses are allowed"),
             must_not_match("(-\.|\.-)", "Number should be on both sites of the dash"),
             must_not_match("--", "Consecutive dashes are not allowed"),
             # There are other ways of specifying IP addresses, that not all software understands. For example: 2130706433, 017700000001, and 127.1 are alternative representations of 127.0.0.1
             # So we just filter for expected characters, but not for the pattern
@@ -130,37 +140,40 @@
         ]
     )
 
 
 def generate_port_validator() -> Validator:
     port_regex="^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$"
     return Validator(
+        id="port_number",
         name="TCP/UDP port",
         rules=[
             must_match("^[0-9]+$", "Only numbers are allowed"),
             should_match(port_regex, "Expected an number between 0 and 65535 (inclusive)"),
         ]
     )
 
 RULE_DOMAIN_CHARS = must_match("^[a-zA-Z0-9-.]+$", "Only letters, numbers, dashes (minus signs), and dots are allowed")
 RULE_DOMAIN_START = must_match("^[^.-]", "Can not begin with a dot or dash (minus sign)")
 RULE_DOMAIN_END = must_match("[^.-]$", "Can not end with a dot or dash (minus sign)")
 RULE_DOMAIN_LENGTH = should_not_match("[a-zA-Z0-9-]{64}", "Subdomains should not be longer than 63 characters")
 
 def generate_domain_name_validator() -> Validator:
     return Validator(
+        id="domain",
         name="Domain name",
         rules=[
             RULE_DOMAIN_CHARS, RULE_DOMAIN_START, RULE_DOMAIN_END, RULE_DOMAIN_LENGTH,
             should_match("\\.", "Should contain multiple elements (for example domain.com or my.domain.com)"),
         ]
     )
 
 def generate_hostname_validator() -> Validator:
     return Validator(
+        id="hostname",
         name="Hostname",
         rules=[
             RULE_DOMAIN_CHARS, RULE_DOMAIN_START, RULE_DOMAIN_END, RULE_DOMAIN_LENGTH
         ]
     )
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/PKG-INFO` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkdocs-placeholder-plugin
-Version: 0.2.5
+Version: 0.3.0
 Summary: Add dynamic placeholders to your mkdocs page
 Home-page: https://github.com/six-two/mkdocs-placeholder-plugin
 Author: six-two
 Author-email: pip@six-two.dev
 License: MIT License
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
@@ -38,16 +38,34 @@
 python3 -m pip install git+https://github.com/six-two/mkdocs-placeholder-plugin
 ```
 
 The corresponding documentation is hosted at <https://dev.mkdocs-placeholder-plugin.six-two.dev>.
 
 ## Notable changes
 
+### TODOs
+
+- Rewrite python code and decouple it from MkDocs (to be able to use it with other projects).
+- Implement propper exception handling for TypeScript code to recover from / compartmentalize non-critical errors.
+- Update the documentation.
+
 ### HEAD
 
+### Version 0.3.0
+
+This release may be a bit buggy due to the rewrite and the documentation is not entirely accurate yet.
+I will update the docs after I also clean up / rewrite the python code (planed for v0.4.0).
+
+- Rewrote the JavaScript code in TypeScript:
+    - Packed and minified using Webpack, so the file is a bit smaller
+    - Should find stupid errors I make in code paths that I do not test (often)
+    - Sophisticated update logic: Instead of always reloading the page it tries to update the DOM in-place (if possible), which should improve user experience a bit and is much faster
+    - Recursive placeholders (placeholders that contain placeholders that contain placeholder...) no longer need to be specified in a speific order in the configuration file.
+    - A placeholder's `default-function` and a validator rule's `match_function` are now evaluated using [`new Function(...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) instead of `eval(...)`, so you need to add a return statement.
+
 ### Version 0.2.5
 
 - When an JavaScript generated `auto-input-table` is empty, now a info box is shown (instead of nothing / an empty table).
 - Bugfixes:
     - `auto_placeholder_tables_javascript` had no effect.
     - Pressing `Enter` on text fields without validators did not try to reload the page,
 
@@ -127,8 +145,9 @@
 2. Update the changelog in this README file.
 3. Update version number in `setup.cfg`.
 4. Build and update package.
 5. Create a commit for the release (`Version 0.X.Y`) and push it.
 6. Update the `latest-release` branch, so that the documentation website gets updated:
     ```
     git branch --force latest-release HEAD
+    git push origin latest-release
     ```
```

### Comparing `mkdocs-placeholder-plugin-0.2.5/src/mkdocs_placeholder_plugin.egg-info/SOURCES.txt` & `mkdocs-placeholder-plugin-0.3.0/src/mkdocs_placeholder_plugin.egg-info/SOURCES.txt`

 * *Files 23% similar despite different names*

```diff
@@ -19,17 +19,10 @@
 src/mkdocs_placeholder_plugin/validators_predefined.py
 src/mkdocs_placeholder_plugin.egg-info/PKG-INFO
 src/mkdocs_placeholder_plugin.egg-info/SOURCES.txt
 src/mkdocs_placeholder_plugin.egg-info/dependency_links.txt
 src/mkdocs_placeholder_plugin.egg-info/entry_points.txt
 src/mkdocs_placeholder_plugin.egg-info/requires.txt
 src/mkdocs_placeholder_plugin.egg-info/top_level.txt
-src/mkdocs_placeholder_plugin/javascript/00_init.js
-src/mkdocs_placeholder_plugin/javascript/10_parse_data.js
-src/mkdocs_placeholder_plugin/javascript/15_debug.js
-src/mkdocs_placeholder_plugin/javascript/20_placeholder_state.js
-src/mkdocs_placeholder_plugin/javascript/30_input.js
-src/mkdocs_placeholder_plugin/javascript/35_input_validators.js
-src/mkdocs_placeholder_plugin/javascript/40_replace.js
-src/mkdocs_placeholder_plugin/javascript/60_auto_tables.js
-src/mkdocs_placeholder_plugin/javascript/80_style.js
-src/mkdocs_placeholder_plugin/javascript/90_trigger_actions.js
+src/mkdocs_placeholder_plugin/assets/placeholder-data.js
+src/mkdocs_placeholder_plugin/assets/placeholder.min.js
+src/mkdocs_placeholder_plugin/assets/placeholder.min.js.map
```

