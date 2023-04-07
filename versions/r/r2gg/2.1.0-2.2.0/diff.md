# Comparing `tmp/r2gg-2.1.0.tar.gz` & `tmp/r2gg-2.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "r2gg-2.1.0.tar", last modified: Thu Mar  9 14:47:07 2023, max compression
+gzip compressed data, was "r2gg-2.2.0.tar", last modified: Fri Apr  7 11:12:09 2023, max compression
```

## Comparing `r2gg-2.1.0.tar` & `r2gg-2.2.0.tar`

### file list

```diff
@@ -1,33 +1,33 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:47:07.115121 r2gg-2.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-03-09 14:46:58.000000 r2gg-2.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-03-09 14:47:07.115121 r2gg-2.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3715 2023-03-09 14:46:58.000000 r2gg-2.1.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:47:07.115121 r2gg-2.1.0/r2gg/
--rw-r--r--   0 runner    (1001) docker     (123)     1343 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/__about__.py
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3914 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_configure.py
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_file_copier.py
--rw-r--r--   0 runner    (1001) docker     (123)    10308 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_lua_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)    21580 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_main.py
--rw-r--r--   0 runner    (1001) docker     (123)     4227 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_osm_building.py
--rw-r--r--   0 runner    (1001) docker     (123)     1088 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_osm_to_pbf.py
--rw-r--r--   0 runner    (1001) docker     (123)     6208 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_output_costs_from_costs_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      340 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_path_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6731 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_pivot_to_osm.py
--rw-r--r--   0 runner    (1001) docker     (123)    15518 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_pivot_to_pgr.py
--rw-r--r--   0 runner    (1001) docker     (123)      721 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_read_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_sql_building.py
--rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_subprocess_execution.py
--rw-r--r--   0 runner    (1001) docker     (123)    13816 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/_valhalla_lua_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-03-09 14:46:58.000000 r2gg-2.1.0/r2gg/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:47:07.115121 r2gg-2.1.0/r2gg.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      599 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-09 14:47:07.000000 r2gg-2.1.0/r2gg.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-09 14:47:07.115121 r2gg-2.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-03-09 14:46:58.000000 r2gg-2.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:47:07.115121 r2gg-2.1.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     4765 2023-03-09 14:46:58.000000 r2gg-2.1.0/tests/test_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:12:09.926770 r2gg-2.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-04-07 11:12:00.000000 r2gg-2.2.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-04-07 11:12:09.926770 r2gg-2.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3715 2023-04-07 11:12:00.000000 r2gg-2.2.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:12:09.922770 r2gg-2.2.0/r2gg/
+-rw-r--r--   0 runner    (1001) docker     (123)     1343 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/__about__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3914 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_configure.py
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_file_copier.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10308 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_lua_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21592 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4227 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_osm_building.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1088 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_osm_to_pbf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6208 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_output_costs_from_costs_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      340 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_path_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6731 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_pivot_to_osm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15518 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_pivot_to_pgr.py
+-rw-r--r--   0 runner    (1001) docker     (123)      721 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_read_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      840 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_sql_building.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_subprocess_execution.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13816 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/_valhalla_lua_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-04-07 11:12:00.000000 r2gg-2.2.0/r2gg/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:12:09.926770 r2gg-2.2.0/r2gg.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      599 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-07 11:12:09.000000 r2gg-2.2.0/r2gg.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-04-07 11:12:09.926770 r2gg-2.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-04-07 11:12:00.000000 r2gg-2.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:12:09.926770 r2gg-2.2.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     4765 2023-04-07 11:12:00.000000 r2gg-2.2.0/tests/test_cli.py
```

### Comparing `r2gg-2.1.0/LICENSE` & `r2gg-2.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/PKG-INFO` & `r2gg-2.2.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: r2gg
-Version: 2.1.0
+Version: 2.2.0
 Summary: Route Graph Generator (r2gg) est un script Python qui permet la génération de graphes pour des moteurs de calcul d'itinéraire
 Home-page: https://github.com/IGNF/route-graph-generator/
 Author: IGNF
 Author-email: 
 Keywords: cli, IGN, osrm, routing, pgrouting, valhalla, generation-algorithms, isochrone, road2
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
```

### Comparing `r2gg-2.1.0/README.md` & `r2gg-2.2.0/README.md`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/__about__.py` & `r2gg-2.2.0/r2gg/__about__.py`

 * *Files 5% similar despite different names*

```diff
@@ -30,15 +30,15 @@
 __title__ = "Route Graph Generator"
 __title_clean__ = "".join(e for e in __title__ if e.isalnum())
 __uri_homepage__ = "https://ignf.github.io/route-graph-generator"
 __uri_repository__ = "https://github.com/IGNF/route-graph-generator/"
 __uri_tracker__ = f"{__uri_repository__}issues/"
 __uri__ = __uri_repository__
 
-__version__ = "2.1.0"
+__version__ = "2.2.0"
 __version_info__ = tuple(
     [
         int(num) if num.isdigit() else num
         for num in __version__.replace("-", ".", 1).split(".")
     ]
 )
```

### Comparing `r2gg-2.1.0/r2gg/_configure.py` & `r2gg-2.2.0/r2gg/_configure.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_file_copier.py` & `r2gg-2.2.0/r2gg/_file_copier.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_lua_builder.py` & `r2gg-2.2.0/r2gg/_lua_builder.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_main.py` & `r2gg-2.2.0/r2gg/_main.py`

 * *Files 0% similar despite different names*

```diff
@@ -460,27 +460,27 @@
             logger.info("Smartrouting source, no need for modifications")
         elif source['type'] == 'osrm':
             source.pop("mapping", None)
             source["cost"].pop("compute", None)
         elif source['type'] == "valhalla":
             source.pop("mapping", None)
             for cost in source["costs"]:
-                cost.pop("compute")
+                cost.pop("compute", None)
         elif source['type'] == "pgr":
             source.pop("mapping", None)
             bid_tmp = source["storage"]["base"]["baseId"]
             for base in config["bases"]:
                 if base["id"] == bid_tmp:
                     db_file_out = convert_path(base["configFile"], config["outputs"]["configurations"]["databases"]["storage"]["directory"])
                     copy_file_locally(base["configFile"], db_file_out)
                     source["storage"]["base"].update({"dbConfig":db_file_out})
                     source["storage"]["base"].update({"schema":base["schema"]})
             source["storage"]["base"].pop("baseId", None)
             for cost in source["costs"]:
-                cost.pop("compute")
+                cost.pop("compute", None)
         else:
             continue
 
         # Écriture du fichier
         with open(source_file, "w") as source_file:
             json_string = json.dumps(source, indent=2)
             source_file.write(json_string)
```

### Comparing `r2gg-2.1.0/r2gg/_osm_building.py` & `r2gg-2.2.0/r2gg/_osm_building.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_osm_to_pbf.py` & `r2gg-2.2.0/r2gg/_osm_to_pbf.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_output_costs_from_costs_config.py` & `r2gg-2.2.0/r2gg/_output_costs_from_costs_config.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_pivot_to_osm.py` & `r2gg-2.2.0/r2gg/_pivot_to_osm.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_pivot_to_pgr.py` & `r2gg-2.2.0/r2gg/_pivot_to_pgr.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_read_config.py` & `r2gg-2.2.0/r2gg/_read_config.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_sql_building.py` & `r2gg-2.2.0/r2gg/_sql_building.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_subprocess_execution.py` & `r2gg-2.2.0/r2gg/_subprocess_execution.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/_valhalla_lua_builder.py` & `r2gg-2.2.0/r2gg/_valhalla_lua_builder.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg/cli.py` & `r2gg-2.2.0/r2gg/cli.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/r2gg.egg-info/PKG-INFO` & `r2gg-2.2.0/r2gg.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: r2gg
-Version: 2.1.0
+Version: 2.2.0
 Summary: Route Graph Generator (r2gg) est un script Python qui permet la génération de graphes pour des moteurs de calcul d'itinéraire
 Home-page: https://github.com/IGNF/route-graph-generator/
 Author: IGNF
 Author-email: 
 Keywords: cli, IGN, osrm, routing, pgrouting, valhalla, generation-algorithms, isochrone, road2
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
```

### Comparing `r2gg-2.1.0/r2gg.egg-info/SOURCES.txt` & `r2gg-2.2.0/r2gg.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/setup.cfg` & `r2gg-2.2.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/setup.py` & `r2gg-2.2.0/setup.py`

 * *Files identical despite different names*

### Comparing `r2gg-2.1.0/tests/test_cli.py` & `r2gg-2.2.0/tests/test_cli.py`

 * *Files identical despite different names*

