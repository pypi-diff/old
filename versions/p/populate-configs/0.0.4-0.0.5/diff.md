# Comparing `tmp/populate-configs-0.0.4.tar.gz` & `tmp/populate-configs-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/populate-configs-0.0.4.tar", last modified: Tue Feb  7 21:46:26 2023, max compression
+gzip compressed data, was "/home/fable/CodeProjects/GBR/populate-configs/dist/tmp5lun2x4c/populate-configs-0.0.5.tar", last modified: Fri Apr  7 05:38:59 2023, max compression
```

## Comparing `populate-configs-0.0.4.tar` & `populate-configs-0.0.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 fable     (1000) fable     (1000)        0 2023-02-07 21:46:25.000000 populate-configs-0.0.4/
--rw-r--r--   0 fable     (1000) fable     (1000)       18 2023-02-05 20:21:07.000000 populate-configs-0.0.4/README.md
-drwxr-xr-x   0 fable     (1000) fable     (1000)        0 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_confs/
--rw-r--r--   0 fable     (1000) fable     (1000)     4772 2023-02-06 21:34:29.000000 populate-configs-0.0.4/populate_confs/__init__.py
-drwxr-xr-x   0 fable     (1000) fable     (1000)        0 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/
--rw-r--r--   0 fable     (1000) fable     (1000)       15 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/top_level.txt
--rw-r--r--   0 fable     (1000) fable     (1000)        1 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/dependency_links.txt
--rw-r--r--   0 fable     (1000) fable     (1000)        1 2023-02-07 18:49:40.000000 populate-configs-0.0.4/populate_configs.egg-info/not-zip-safe
--rw-r--r--   0 fable     (1000) fable     (1000)       58 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/entry_points.txt
--rw-r--r--   0 fable     (1000) fable     (1000)      336 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/SOURCES.txt
--rw-r--r--   0 fable     (1000) fable     (1000)       32 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/requires.txt
--rw-r--r--   0 fable     (1000) fable     (1000)      768 2023-02-07 21:46:25.000000 populate-configs-0.0.4/populate_configs.egg-info/PKG-INFO
--rw-r--r--   0 fable     (1000) fable     (1000)      966 2023-02-07 21:46:25.000000 populate-configs-0.0.4/setup.cfg
--rw-r--r--   0 fable     (1000) fable     (1000)       62 2023-02-06 21:53:59.000000 populate-configs-0.0.4/setup.py
--rw-r--r--   0 fable     (1000) fable     (1000)      768 2023-02-07 21:46:25.000000 populate-configs-0.0.4/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 05:38:59.000000 populate-configs-0.0.5/
+-rw-r--r--   0 root         (0) root         (0)       18 2023-02-05 20:21:07.000000 populate-configs-0.0.5/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_confs/
+-rw-r--r--   0 root         (0) root         (0)     5108 2023-04-07 05:25:03.000000 populate-configs-0.0.5/populate_confs/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/
+-rw-r--r--   0 root         (0) root         (0)       15 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-02-07 18:49:40.000000 populate-configs-0.0.5/populate_configs.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       58 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      336 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)       32 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)      768 2023-04-07 05:38:59.000000 populate-configs-0.0.5/populate_configs.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      966 2023-04-07 05:38:59.000000 populate-configs-0.0.5/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)       62 2023-02-06 21:53:59.000000 populate-configs-0.0.5/setup.py
+-rw-r--r--   0 root         (0) root         (0)      768 2023-04-07 05:38:59.000000 populate-configs-0.0.5/PKG-INFO
```

### Comparing `populate-configs-0.0.4/populate_confs/__init__.py` & `populate-configs-0.0.5/populate_confs/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -70,43 +70,52 @@
         )
     if not os.path.isfile(filepath):
         raise PopulateException(
             f'{filetype} filepath is not a file: {filepath}'
         )
 
 
+def update_compiled_params(update_to, update_from):
+    for k, v in update_from.items():
+        if isinstance(v, dict) and k in update_to:
+            update_to[k].update(v)
+        else:
+            update_to[k] = v
+
+
 def compile_defaults(params, section=None):
     defaults = params.get('defaults', params.get('DEFAULTS')) or {}
     if section:
         section_defaults = defaults.get(section) or {}
-        defaults.update(section_defaults)
+        update_compiled_params(defaults, section_defaults)
     return defaults
 
 
 def compile_secrets(params, section=None):
     secrets = params.get('secrets', params.get('SECRETS')) or {}
     defaults = secrets.get('defaults', secrets.get('DEFAULTS')) or {}
     if section:
         section_secrets = secrets.get(section) or {}
-        defaults.update(section_secrets)
+        update_compiled_params(defaults, section_secrets)
     secrets.update(defaults)
     return secrets
 
 
 def compile_params(params, section=None):
     defaults = compile_defaults(params, section=section)
     secrets = compile_secrets(params, section=section)
     defaults.update(secrets)
+    update_compiled_params(defaults, secrets)
     if section:
         section_params = params.get(section)
         if not section_params:
             raise PopulateException(f'{section} not a valid section name')
-        defaults.update(section_params)
+        update_compiled_params(defaults, section_params)
     else:
-        defaults.update(params)
+        update_compiled_params(defaults, params)
     return defaults
 
 
 def get_jinja_vars(template_dir, template):
     """Returns list of jinja vars in template"""
     env = Environment(loader=FileSystemLoader(template_dir))
     template_source = env.loader.get_source(env, template)
@@ -146,16 +155,16 @@
     template_path = args.filepath
     validate_filepath(template_path, 'Jinja2 Template')
     json_file = args.json
     config_file = args.yaml
     section = args.section
     if config_file:
         validate_filepath(config_file, 'Yaml Config')
-        dir, file = os.path.split(config_file)
-        config = PopulateConfig(file, dir)
+        path, file = os.path.split(config_file)
+        config = PopulateConfig(file, path)
         params = config.config
     elif json_file:
         validate_filepath(json_file, 'JSON params')
         with open(json_file, 'r') as file:
             params = json.load(file)
     else:
         params = os.environ
```

### Comparing `populate-configs-0.0.4/populate_configs.egg-info/PKG-INFO` & `populate-configs-0.0.5/populate_configs.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: populate-configs
-Version: 0.0.4
+Version: 0.0.5
 Summary: Populate Jinja2 config files from yaml or json based config params
 Home-page: https://github.com/GreenBuildingRegistry/populate-configs
 Author: Fable Turas
 Author-email: fable@rainsoftware.tech
 Maintainer: GreenBuildingRegistry
 Maintainer-email: admin@greenbuildingregistry.com
 License: UNKNOWN
```

### Comparing `populate-configs-0.0.4/setup.cfg` & `populate-configs-0.0.5/setup.cfg`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = populate-configs
-version = 0.0.4
+version = 0.0.5
 description = Populate Jinja2 config files from yaml or json based config params
 author = Fable Turas
 author_email = fable@rainsoftware.tech
 maintainer = GreenBuildingRegistry
 maintainer_email = admin@greenbuildingregistry.com
 keywords = config, yaml, jinja2
 url = https://github.com/GreenBuildingRegistry/populate-configs
```

### Comparing `populate-configs-0.0.4/PKG-INFO` & `populate-configs-0.0.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: populate-configs
-Version: 0.0.4
+Version: 0.0.5
 Summary: Populate Jinja2 config files from yaml or json based config params
 Home-page: https://github.com/GreenBuildingRegistry/populate-configs
 Author: Fable Turas
 Author-email: fable@rainsoftware.tech
 Maintainer: GreenBuildingRegistry
 Maintainer-email: admin@greenbuildingregistry.com
 License: UNKNOWN
```

