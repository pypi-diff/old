# Comparing `tmp/cjdb-1.0.0.tar.gz` & `tmp/cjdb-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cjdb-1.0.0.tar", max compression
+gzip compressed data, was "cjdb-1.1.0.tar", max compression
```

## Comparing `cjdb-1.0.0.tar` & `cjdb-1.1.0.tar`

### file list

```diff
@@ -1,28 +1,22 @@
--rw-r--r--   0        0        0     1065 2023-03-24 08:47:24.943711 cjdb-1.0.0/LICENSE
--rw-r--r--   0        0        0     2491 2023-03-27 09:25:00.078680 cjdb-1.0.0/README.md
--rw-r--r--   0        0        0     8165 2023-03-24 10:32:51.758607 cjdb-1.0.0/cjdb/README.md
--rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944366 cjdb-1.0.0/cjdb/__init__.py
--rw-r--r--   0        0        0      572 2023-03-24 08:47:24.944434 cjdb-1.0.0/cjdb/main.py
--rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944484 cjdb-1.0.0/cjdb/modules/__init__.py
--rw-r--r--   0        0        0     3189 2023-03-24 08:47:24.944557 cjdb-1.0.0/cjdb/modules/arg_parser.py
--rw-r--r--   0        0        0     1981 2023-03-24 08:47:24.944614 cjdb-1.0.0/cjdb/modules/checks.py
--rw-r--r--   0        0        0     1925 2023-03-24 08:47:24.944674 cjdb-1.0.0/cjdb/modules/extensions.py
--rw-r--r--   0        0        0     6834 2023-03-24 08:47:24.944744 cjdb-1.0.0/cjdb/modules/geometric.py
--rw-r--r--   0        0        0    15043 2023-03-24 08:47:24.944834 cjdb-1.0.0/cjdb/modules/importer.py
--rw-r--r--   0        0        0     1377 2023-03-24 08:47:24.944898 cjdb-1.0.0/cjdb/modules/utils.py
--rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944949 cjdb-1.0.0/cjdb/resources/__init__.py
--rw-r--r--   0        0        0      783 2023-03-24 08:47:24.945006 cjdb-1.0.0/cjdb/resources/object_types.py
--rw-r--r--   0        0        0      798 2023-03-24 08:47:24.945052 cjdb-1.0.0/cjdb/resources/post_import.sql
--rw-r--r--   0        0        0     2079 2023-03-24 08:47:24.945116 cjdb-1.0.0/cjdb/resources/strings.py
--rw-r--r--   0        0        0        0 2023-03-24 08:47:24.945171 cjdb-1.0.0/cjdb/test/__init__.py
--rw-r--r--   0        0        0      324 2023-03-24 08:47:24.945230 cjdb-1.0.0/cjdb/test/cli_test.py
--rw-r--r--   0        0        0     1043 2023-03-24 08:47:24.945310 cjdb-1.0.0/cjdb/test/conftest.py
--rw-r--r--   0        0        0   349901 2023-03-24 08:47:24.946336 cjdb-1.0.0/cjdb/test/files/cjfiles/5870_ext.jsonl
--rw-r--r--   0        0        0   279635 2023-03-24 08:47:24.947026 cjdb-1.0.0/cjdb/test/files/cjfiles/tile_901_trimmed.jsonl
--rw-r--r--   0        0        0  1795334 2023-03-24 08:47:24.973978 cjdb-1.0.0/cjdb/test/files/extension2.jsonl
--rw-r--r--   0        0        0      797 2023-03-24 08:47:24.974248 cjdb-1.0.0/cjdb/test/files/geomtemplate.city.jsonl
--rw-r--r--   0        0        0  2188315 2023-03-24 08:47:24.979779 cjdb-1.0.0/cjdb/test/files/vienna.jsonl
--rw-r--r--   0        0        0      515 2023-03-24 08:47:24.979972 cjdb-1.0.0/cjdb/test/inputs/arguments
--rw-r--r--   0        0        0      515 2023-04-05 08:26:55.836404 cjdb-1.0.0/pyproject.toml
--rw-r--r--   0        0        0     3437 1970-01-01 00:00:00.000000 cjdb-1.0.0/setup.py
--rw-r--r--   0        0        0     3089 1970-01-01 00:00:00.000000 cjdb-1.0.0/PKG-INFO
+-rw-r--r--   0        0        0     1065 2023-03-24 08:47:24.943711 cjdb-1.1.0/LICENSE
+-rw-r--r--   0        0        0     1820 2023-04-06 14:32:49.893157 cjdb-1.1.0/README.md
+-rw-r--r--   0        0        0     9397 2023-04-06 15:36:36.056059 cjdb-1.1.0/cjdb/README.md
+-rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944366 cjdb-1.1.0/cjdb/__init__.py
+-rw-r--r--   0        0        0      564 2023-04-05 10:23:47.428044 cjdb-1.1.0/cjdb/main.py
+-rw-r--r--   0        0        0     5008 2023-04-06 08:58:50.702731 cjdb-1.1.0/cjdb/model/README.md
+-rw-r--r--   0        0        0        0 2023-03-24 08:47:24.987486 cjdb-1.1.0/cjdb/model/__init__.py
+-rw-r--r--   0        0        0     4778 2023-04-06 11:09:51.718769 cjdb-1.1.0/cjdb/model/sqlalchemy_models/__init__.py
+-rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944484 cjdb-1.1.0/cjdb/modules/__init__.py
+-rw-r--r--   0        0        0     3199 2023-04-05 14:27:23.970495 cjdb-1.1.0/cjdb/modules/arg_parser.py
+-rw-r--r--   0        0        0     2162 2023-04-05 12:24:10.108456 cjdb-1.1.0/cjdb/modules/checks.py
+-rw-r--r--   0        0        0     1926 2023-04-05 12:24:10.110402 cjdb-1.1.0/cjdb/modules/extensions.py
+-rw-r--r--   0        0        0     6836 2023-04-05 12:24:10.103852 cjdb-1.1.0/cjdb/modules/geometric.py
+-rw-r--r--   0        0        0    15976 2023-04-06 12:46:29.824095 cjdb-1.1.0/cjdb/modules/importer.py
+-rw-r--r--   0        0        0     1375 2023-04-05 12:24:10.114393 cjdb-1.1.0/cjdb/modules/utils.py
+-rw-r--r--   0        0        0        0 2023-03-24 08:47:24.944949 cjdb-1.1.0/cjdb/resources/__init__.py
+-rw-r--r--   0        0        0      783 2023-03-24 08:47:24.945006 cjdb-1.1.0/cjdb/resources/object_types.py
+-rw-r--r--   0        0        0      798 2023-03-24 08:47:24.945052 cjdb-1.1.0/cjdb/resources/post_import.sql
+-rw-r--r--   0        0        0     2079 2023-03-24 08:47:24.945116 cjdb-1.1.0/cjdb/resources/strings.py
+-rw-r--r--   0        0        0      862 2023-04-06 15:13:09.211742 cjdb-1.1.0/pyproject.toml
+-rw-r--r--   0        0        0     2930 1970-01-01 00:00:00.000000 cjdb-1.1.0/setup.py
+-rw-r--r--   0        0        0     2669 1970-01-01 00:00:00.000000 cjdb-1.1.0/PKG-INFO
```

### Comparing `cjdb-1.0.0/LICENSE` & `cjdb-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `cjdb-1.0.0/cjdb/README.md` & `cjdb-1.1.0/cjdb/README.md`

 * *Files 27% similar despite different names*

```diff
@@ -1,77 +1,146 @@
-# cj2pgsql
+# cjdb
 
 [![MIT badge](https://img.shields.io/pypi/l/cjdb)](../LICENSE) &nbsp; [![PyPI](https://img.shields.io/pypi/v/cjdb)](https://pypi.org/project/cjdb)
 
-`cj2pgsql` is a Python based importer of CityJSONL files to a PostgreSQL database. It requires [PostGIS](https://postgis.net/) extension for geometry types.
+`cjdb` is a Python based importer of CityJSONL files to a PostgreSQL database. It requires [PostGIS](https://postgis.net/) extension for geometry types.
 
 ## Table of Contents  
 ### [1. CLI Usage](#usage)
 - [CLI instructions](#instructions)
 - [Quickstart example](#quickstart)
 
-### [2. cj2pgsql explanations](#explanation)
+### [2. cjdb explanations](#explanation)
  - [Model assumptions](#model)
  - [What is a City Model?](#citymodel)
  - [Types of input](#input)
  - [Coordinate Reference Systems](#crs)
  - [3D reprojections](#3d)
  - [CityJSON Extensions](#extensions)
  - [CityJSON GeometryTemplate](#geomtemplate)
  - [Data validation](#validation)
  - [Repeated object IDs](#repeated)
 
-### [3. Running with local code](#local)
-
-### [4. Running tests](#tests)
 ---------------------------------
 
 ## 1. CLI usage <a name="usage"></a>
 ---
 ### CLI instructions: <a name="instructions"></a>
-https://leoleonsio.github.io/cjdb/#cj2pgsql-cli-usage
+
+usage: 
+
+```bash
+cj2pgsql [-h] [-H DB_HOST] [-p DB_PORT] -U DB_USER [-W DB_PASSWORD] -d DB_NAME [-s DB_SCHEMA] [-I TARGET_SRID][-x INDEXED_ATTRIBUTES] [-px PARTIAL_INDEXED_ATTRIBUTES] [-g] [-a | -o] [-e | -u] [file_or_directory]
+```
+#### Positional Arguments
+file_or_directory
+Source CityJSONL file or a directory with CityJSONL files. STDIN if not specified. If specifying a directory, all the *.jsonl files inside of it will be imported.
+
+Default: “stdin”
+
+#### Named Arguments
+-I, --srid
+Target coordinate system SRID. All 3D and 2D geometries will be reprojected.
+
+-x, --attr-index
+CityObject attribute to be indexed using a btree index. Can be specified multiple times, for each attribute once.
+
+Default: []
+
+-px, --partial-attr-index
+CityObject attribute to be indexed using a btree partial index. Can be specified multiple times, for each attribute once. This index indexes on a condition ‘where {
+                {ATTR_NAME
+                }
+        } is not null’. This means that it saves space and improves query performance when the attribute is not present for all imported CityObjects.
+
+Default: []
+
+-g, --ignore-repeated-file
+Ignore repeated file names warning when importing. By default, the importer will send out warnings if a specific file has already been imported.
+
+Default: False
+
+-a, --append
+Run in append mode (as opposed to default create mode). This assumes the database structure exists already and new data is to be appended.
+
+Default: False
+
+-o, --overwrite
+Overwrite the data that is currently in the database schema. Warning: this causes the loss of what was imported before to the database schema.
+
+Default: False
+
+-u, --update-existing
+Check if the object with given ID exists before inserting, and update it if it does. The old object will be updated with the new object’s properties.
+
+Default: False
+
+#### Database connection arguments
+-H, --host
+PostgreSQL database host
+
+Default: “localhost”
+
+-p, --port
+PostgreSQL database port
+
+Default: 5432
+
+-U, --user
+PostgreSQL database user name
+
+-W, --password
+PostgreSQL database user password
+
+-d, --database
+PostgreSQL database name
+
+-s, --schema
+Target database schema
+
+Default: “public”
 
 ### Quickstart example <a name="quickstart"></a>
 Sample CityJSON data can be downloaded from [3DBAG download service](https://3dbag.nl/nl/download?tid=901).
 
-Then, having the CityJSON file, a combination of [cjio](https://github.com/cityjson/cjio) (external CityJSON processing library) and cj2pgsql is needed to import it to a specified schema in a database.
+Then, having the CityJSON file, a combination of [cjio](https://github.com/cityjson/cjio) (external CityJSON processing library) and cjdb is needed to import it to a specified schema in a database.
 
 1. Convert CityJSON to CityJSONL
 
 ```
 cjio --suppress_msg tile_901.json export jsonl stdout > tile_901.jsonl 
 ```
 
 2. Import CityJSONL to the database
 ```
-PGPASSWORD=postgres cj2pgsql -H localhost -U postgres -d postgres -s cjdb -o tile_901.jsonl   
+PGPASSWORD=postgres cjdb -H localhost -U postgres -d postgres -s cjdb -o tile_901.jsonl   
 ```
 
 **Alternatively steps 1 and 2 in a single command:**
 
 ```
-cjio --suppress_msg tile_901.json export jsonl stdout | cj2pgsql -H localhost -U postgres -d postgres -s cjdb -o
+cjio --suppress_msg tile_901.json export jsonl stdout | cjdb -H localhost -U postgres -d postgres -s cjdb -o
 ```
 
 The metadata and the objects can then be found in the tables in the specified schema (`cjdb` in this example).
 
 
 Password can be specified in the `PGPASSWORD` environment variable. If not specified, the app will prompt for the password.
 
 
-## 2. cj2pgsql explanations <a name="explanation"></a>
+## 2. cjdb explanations <a name="explanation"></a>
 ---
 ### Model assumptions <a name="model"></a>
-The `cj2pgsql` importer loads the data in accordance with a specific data model.
+The `cjdb` importer loads the data in accordance with a specific data model.
 
 Model documentation:
- [model/README](../model/README.md)
+ [model/README](model/README.md)
 
 #### Indexes
-Some indexes are created by default (refer to [model/README](../model/README.md)).
+Some indexes are created by default (refer to [model/README](model/README.md)).
 
 Additionally, the user can specify which CityObject attributes are to be indexed with the `-x/--attr-index` or `-px/--partial-attr-index` flag. The second option uses a partial index with a `not null` condition on the attribute. This saves disk space when indexing an attribute that is not present among all the imported CityObjects. This is often the case with CityJSON, because in a single dataset there can be different object types, with different attributes.
 
 ### What is a City Model? How to organize CityJSON data from various sources? <a name="citymodel"></a>
 
 The definition and scope of the City Model are for the user to decide. It is recommended to group together semantically coherent objects, by importing them to the same database schema.
 
@@ -83,19 +152,19 @@
 
 
 The importer supports 3 kinds of input:
 - a single CityJSONL file
 - a directory of CityJSONL files (all files with *jsonl* extensions are located and imported)
 - STDIN using the pipe operator:
 ```
-cat file.jsonl | cj2pgsql ...
+cat file.jsonl | cjdb ...
 ```
 
 ### Coordinate Reference Systems <a name="crs"></a>
-The `cj2pgsql` importer does not allow inconsistent CRS (coordinate reference systems) within the same database schema. For storing data in separate CRS using multiple schemas is required.
+The `cjdb` importer does not allow inconsistent CRS (coordinate reference systems) within the same database schema. For storing data in separate CRS using multiple schemas is required.
 
 The data needs to be either harmonized beforehand, or the `-I/--srid` flag can be used upon import, to reproject all the geometries to the one specified CRS. Specifying a 2D CRS (instead of a 3D one) will cause the Z-coordinates to remain unchanged.
 
 **Note:** reprojections slow down the import significantly.
 
 **Note:** Source data with missing `"metadata"/"referenceSystem"` cannot be reprojected due to unknown source reference system.
 
@@ -109,15 +178,15 @@
 
 If that fails, the user will have to download the required grids and put them in the printed `{pyproj_directory}` themselves. 
 
 
 ### CityJSON Extensions <a name="extensions"></a>
 If [CityJSON Extensions](https://www.cityjson.org/extensions/) were present in the imported file, they can be found listed in the `extensions` column in the `import_meta` table.
 
-The [CityJSON specifications](https://www.cityjson.org/specs/1.1.2/#extensions) mention 3 different extendable features, and the `cj2pgsql` importer deals with them as follows:
+The [CityJSON specifications](https://www.cityjson.org/specs/1.1.2/#extensions) mention 3 different extendable features, and the `cjdb` importer deals with them as follows:
 
 1. Complex attributes
 
 No action is taken. These attributes end up in the `attributes` JSONB column.
 
 2. Additional root properties
 
@@ -139,47 +208,9 @@
 - the source dataset does not have a CRS defined at all
 
 ### Repeated object IDs <a name="repeated"></a>
 By default, the importer does not check if an object with a given ID exists already in the database. This is because such an operation for every inserted object results in a performance penalty.
 
 The user can choose to run the import with either the `-e/--skip-existing` option to skip existing objects or `-u, --update-existing` to update existing objects. This will slow down the import, but it will also ensure that repeated object cases are handled.
 
-## 3. Running with local code <a name="local"></a>
-Create `pipenv` environment in repository root:
-```
-pipenv install
-```
-
-Run the importer:
-```
-PYTHONPATH=$PWD pipenv run python cj2pgsql/main.py --help
-```
-
-
-## 4. Running tests <a name="tests"></a>
----
-Test cases for Pytest are generated based on the CityJSONL files in:
-- cj2pgsql/test/files
-
-And the argument sets defined in the file:
-- cj2pgsql/test/inputs/arguments
-
-Where each line is a separate argument set.
-
-The tests are run for each combination of a file and argument set. To run them locally, the cj2pgsql/test/inputs/arguments file has to be modified.
-
-Install pytest first.
-```
-pip3 install pytest
-```
-
-Then, in repository root:
-```
-pytest cj2pgsql -v
-```
-
-or, to see the importer output:
-```
-pytest cj2pgsql -s
-```
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `cjdb-1.0.0/cjdb/main.py` & `cjdb-1.1.0/cjdb/main.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from cj2pgsql.modules.arg_parser import Parser, validate_args
-from cj2pgsql.modules.importer import Importer
+from cjdb.modules.arg_parser import Parser, validate_args
+from cjdb.modules.importer import Importer
 
 
 def get_args():
     parser = Parser()
     args = parser.parse_args()
     validation_result, validation_msg = validate_args(args)
```

### Comparing `cjdb-1.0.0/cjdb/modules/checks.py` & `cjdb-1.1.0/cjdb/modules/checks.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,48 +1,59 @@
-from pyproj import datadir, CRS
+from pyproj import CRS, datadir
 from pyproj.transformer import TransformerGroup
 
 
 def check_root_properties(found_extra_properties, defined_extra_properties):
     if found_extra_properties:
-        base_msg = "Warning: An extended CityJSON root property: '{}' was not defined by any of the extensions."
+        base_msg = """Warning: An extended CityJSON root property: '{}'\
+                      was not defined by any of the extensions."""
         for prop_name in found_extra_properties:
-            if not prop_name in defined_extra_properties:
+            if prop_name not in defined_extra_properties:
                 print(base_msg.format(prop_name))
 
 
 def check_object_type(checked_type, allowed_types, extended_types):
     check_result = True
     message = ""
     all_types = allowed_types + extended_types
     if checked_type not in all_types:
         check_result = False
-        message = f"Warning: CityJSON object type '{checked_type}' not allowed by main schema nor extensions."
+        message = f"""Warning: CityJSON object type '{checked_type}'\
+                      not allowed by main schema nor extensions."""
 
     return check_result, message
 
 
 # check if reprojection possible
 # prints warnings, but doesn't stop the import
 def check_reprojection(source_srid, target_srid):
     source_proj = CRS.from_epsg(source_srid)
     target_proj = CRS.from_epsg(target_srid)
 
     if len(target_proj.axis_info) < 3:
-        print(f"Warning: The specified target SRID({target_srid}) " + \
-                "lacks information about the Z-axis. The Z vertex values will remain unchanged.")
+        print(
+            f"Warning: The specified target SRID({target_srid}) "
+            + "lacks information about the Z-axis."
+            + " The Z vertex values will remain unchanged."
+        )
 
     group = TransformerGroup(source_proj, target_proj)
-    # this prints a warning if there are some grids missing for the reprojection
-    # more about this https://pyproj4.github.io/pyproj/stable/transformation_grids.html
+    # this prints a warning if there are some grids missing for the reprojection # noqa
+    # more about this https://pyproj4.github.io/pyproj/stable/transformation_grids.html # noqa
 
     # attempt to download missing grids
     if not group.best_available:
-        print("Attempting to download additional grids required for CRS transformation.")
-        print(f"This can also be done manually, and the grid should be put in this folder:\n\t{datadir.get_data_dir()}")
-        
+        print(
+            """Attempting to download additional grids\
+               required for CRS transformation."""
+        )
+        print(
+            f"""This can also be done manually, and the grid\
+            should be put in this folder:\n\t{datadir.get_data_dir()}"""
+        )
+
         try:
             group.download_grids(datadir.get_data_dir())
-        except:
+        except (...):
             print("Failed to download the missing grids.")
         else:
-            print("Download successful.")
+            print("Download successful.")
```

### Comparing `cjdb-1.0.0/cjdb/modules/extensions.py` & `cjdb-1.1.0/cjdb/modules/extensions.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
-import requests
 import json
 
+import requests
+
 
 class ExtensionHandler:
     def __init__(self, extensions):
         self.full_definitions = {}
         self.extra_root_properties = []
         self.extra_attributes = {}
         self.extra_city_objects = []
```

### Comparing `cjdb-1.0.0/cjdb/modules/geometric.py` & `cjdb-1.1.0/cjdb/modules/geometric.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import copy
-from shapely.geometry import box, MultiPolygon, Point, Polygon
-from shapely.validation import explain_validity,make_valid
+from collections import OrderedDict
+
+import numpy as np
 from pyproj import CRS, Transformer
 from pyproj.transformer import TransformerGroup
-import numpy as np
-from collections import OrderedDict
+from shapely.geometry import MultiPolygon, Point, Polygon, box
+from shapely.validation import explain_validity, make_valid
 
 
 # get srid from a CRS string definition
 def get_srid(crs):
     if crs:
         proj = CRS.from_string(crs)
         srid = proj.to_epsg()
```

### Comparing `cjdb-1.0.0/cjdb/modules/importer.py` & `cjdb-1.1.0/cjdb/modules/importer.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,72 +1,99 @@
-from cj2pgsql.modules.checks import check_object_type, check_root_properties, check_reprojection
-from cj2pgsql.modules.extensions import ExtensionHandler
-from cj2pgsql.modules.geometric import get_ground_geometry, get_srid, \
-    reproject_vertex_list, resolve_geometry_vertices, transform_vertex
-from cj2pgsql.modules.utils import find_extra_properties, get_cj_object_types, get_db_engine, to_dict
-from model.sqlalchemy_models import BaseModel, FamilyModel, ImportMetaModel, CjObjectModel
-import os
 import json
+import os
 import sys
-from sqlalchemy.orm import Session
-from sqlalchemy import func, insert
 from pathlib import Path
-from pyproj import CRS
+
+from sqlalchemy import func, text
+from sqlalchemy.dialects.postgresql import insert
+from sqlalchemy.orm import Session
+
+from cjdb.modules.checks import (
+    check_object_type,
+    check_reprojection,
+    check_root_properties,
+)
+from cjdb.modules.extensions import ExtensionHandler
+from cjdb.modules.geometric import (
+    get_ground_geometry,
+    get_srid,
+    reproject_vertex_list,
+    resolve_geometry_vertices,
+    transform_vertex,
+)
+from cjdb.modules.utils import (
+    find_extra_properties,
+    get_cj_object_types,
+    get_db_engine,
+    to_dict,
+)
+from cjdb.model.sqlalchemy_models import (
+    BaseModel,
+    CjObjectModel,
+    FamilyModel,
+    ImportMetaModel,
+)
+
 
 # class to store variables per file import - for clarity
 class SingleFileImport:
     def __init__(self, file="stdin"):
         self.file = file
         self.target_srid = None
-        self.import_meta = None # meta read from the file
+        self.import_meta = None  # meta read from the file
         self.source_srid = None
-        self.extension_handler = None # data about extensions - extra properties, root attributes...
+        self.extension_handler = (
+            None  # data about extensions - extra properties, root attributes
+        )
         self.cj_objects = []
         self.families = []
 
+
 # importer class called once per whole import
 class Importer:
     def __init__(self, args):
         self.args = args
         # get allowed types for validation
         self.cj_object_types = get_cj_object_types()
         self.current = SingleFileImport()
 
         for table in BaseModel.metadata.tables.values():
             table.schema = self.args.db_schema
 
-
     def __enter__(self):
         self.engine = get_db_engine(self.args)
         self.session = Session(self.engine)
         return self
 
     def __exit__(self, exc_type, exc_value, traceback):
         self.session.close()
 
     def run_import(self):
         # create model if in create mode, else append data
         if not self.args.append_mode:
             self.prepare_database()
-
         self.parse_cityjson()
         self.session.commit()
-
         # post import operations like clustering, indexing...
         if not self.args.append_mode:
             self.post_import()
-
         self.current.import_meta.finished_at = func.now()
         self.session.commit()
         print(f"Imported from {self.args.filepath} successfully")
 
     def prepare_database(self):
-        if self.args.overwrite:
-            self.engine.execute(f"drop schema if exists {self.args.db_schema} cascade")
-        self.engine.execute(f"create schema if not exists {self.args.db_schema}")
+        with self.engine.connect() as conn:
+            if self.args.overwrite:
+                conn.execute(
+                    text(f"""DROP SCHEMA
+                             IF EXISTS {self.args.db_schema}
+                             CASCADE""")
+                )
+            conn.execute(text(f"""CREATE SCHEMA IF NOT EXISTS
+                                  {self.args.db_schema}"""))
 
         # create all tables defined as SqlAlchemy models
         for table in BaseModel.metadata.tables.values():
             table.create(self.engine, checkfirst=True)
 
     def parse_cityjson(self):
         source_path = self.args.filepath
@@ -84,266 +111,322 @@
         # post import operations like clustering, indexing...
 
         cur_path = Path(__file__).parent
         sql_path = os.path.join(cur_path.parent, "resources/post_import.sql")
 
         with open(sql_path) as f:
             cmd = f.read().format(schema=self.args.db_schema)
-        self.engine.execute(cmd)
+        with self.engine.connect() as conn:
+            conn.execute(text(cmd))
         self.index_attributes()
-        
+
     def process_line(self, line):
         line_json = json.loads(line)
         if "metadata" in line_json:
             extra_root_properties = find_extra_properties(line_json)
-            self.current.source_srid = get_srid(line_json["metadata"].get("referenceSystem"))
+            self.current.source_srid = get_srid(
+                line_json["metadata"].get("referenceSystem")
+            )
             if not self.current.source_srid:
-                print("Warning: No Coordinate Reference System specified for the dataset.")
+                print(
+                    """Warning: No Coordinate Reference System
+                       specified for the dataset."""
+                )
 
             # use specified target SRID for all the geometries
             # If not specified use same as source.
             if self.args.target_srid and self.current.source_srid:
-                self.current.target_srid = self.args.target_srid                
-                check_reprojection(self.current.source_srid, self.current.target_srid)
+                self.current.target_srid = self.args.target_srid
+                check_reprojection(self.current.source_srid, self.current.target_srid) # noqa
+            elif self.args.target_srid:
+                self.current.target_srid = self.args.target_srid
             else:
                 self.current.target_srid = self.current.source_srid
 
             # calculate dataset bbox based on geographicalExtent
             bbox = None
             if "geographicalExtent" in line_json["metadata"]:
                 bbox_coords = line_json["metadata"]["geographicalExtent"]
                 bbox_vertices = [bbox_coords[:3], bbox_coords[3:]]
-    
-                if self.current.source_srid \
-                    and self.current.target_srid != self.current.source_srid:
-
-                    bbox_vertices = reproject_vertex_list(bbox_vertices,
-                                                        self.current.source_srid,
-                                                        self.current.target_srid)
-            
-                bbox = func.st_makeenvelope(bbox_vertices[0][0], bbox_vertices[0][1],
-                                            bbox_vertices[1][0], bbox_vertices[1][1],
-                                            self.current.target_srid)
 
-            # store extensions data - extra root properties, extra city objects...
-            self.current.extension_handler = ExtensionHandler(line_json.get("extensions"))
+                if (
+                    self.current.source_srid
+                    and self.current.target_srid != self.current.source_srid
+                ):
+                    bbox_vertices = reproject_vertex_list(
+                        bbox_vertices,
+                        self.current.source_srid,
+                        self.current.target_srid,
+                    )
+
+                bbox = func.st_makeenvelope(
+                    bbox_vertices[0][0],
+                    bbox_vertices[0][1],
+                    bbox_vertices[1][0],
+                    bbox_vertices[1][1],
+                    self.current.target_srid,
+                )
+
+            # store extensions data - extra root properties, extra city objects
+            self.current.extension_handler = ExtensionHandler(
+                line_json.get("extensions")
+            )
 
             # prepare extra properties coming from extensions
             # they will be placed in the extra_properties jsonb column
             extra_properties_obj = {}
             for prop_name in extra_root_properties:
                 extra_properties_obj[prop_name] = line_json[prop_name]
 
-            # check the occurring properties against the extension defined extra properties
-            check_root_properties(extra_root_properties,
-                                    self.current.extension_handler.extra_root_properties)
-                
+            # check the occurring properties against
+            # the extension defined extra properties
+            check_root_properties(
+                extra_root_properties,
+                self.current.extension_handler.extra_root_properties,
+            )
+
             # "or None" is added to change empty json "{}" to database null
             import_meta = ImportMetaModel(
                 source_file=os.path.basename(self.current.file),
                 version=line_json["version"],
                 meta=line_json.get("metadata") or None,
                 transform=line_json.get("transform") or None,
                 geometry_templates=line_json.get("geometry-templates") or None,
                 srid=self.current.target_srid,
                 extensions=line_json.get("extensions") or None,
                 extra_properties=extra_properties_obj or None,
-                bbox=bbox
+                bbox=bbox,
             )
 
             # compare to existing import metas
             # for example to detect inconsistent CRS from different files
-            result_ok = import_meta.compare_existing(self.session, 
-                                                    self.args.ignore_repeated_file)
+            result_ok = import_meta.compare_existing(
+                self.session, self.args.ignore_repeated_file
+            )
             if not result_ok:
                 print("Cancelling import")
-                sys.exit()
+                sys.exit(1)
 
             # add metadata to the database
             import_meta.__table__.schema = self.args.db_schema
             self.current.import_meta = import_meta
             self.session.add(import_meta)
             self.session.commit()
 
         else:
-            # unpack vertices for the cityobjects based on the CityJSON transform
+            # unpack vertices for the cityobjects based on
+            # the CityJSON transform
             # this is done once for the CityJSONFeature
-            vertices = [transform_vertex(v, self.current.import_meta.transform) 
-                                        for v in line_json["vertices"]]
+            vertices = [
+                transform_vertex(v, self.current.import_meta.transform)
+                for v in line_json["vertices"]
+            ]
 
             # reproject if needed
             source_target_srid = None
-            if self.current.source_srid and self.current.target_srid != self.current.source_srid:
-                source_target_srid = (self.current.source_srid, self.current.target_srid)
+            if (
+                self.current.source_srid
+                and self.current.target_srid != self.current.source_srid
+            ):
+                source_target_srid = (
+                    self.current.source_srid,
+                    self.current.target_srid,
+                )
                 vertices = reproject_vertex_list(vertices, *source_target_srid)
 
             # list of relationships for the CityJSONFeature
             family_ties = []
             # objects for the CityJSONFeature
             cj_feature_objects = {}
 
             # create CityJSONObjects
             for obj_id, cityobj in line_json["CityObjects"].items():
                 obj_to_update = None
 
-                # optionally check if the object exists - to skip it or update it
-                if self.args.skip_existing or self.args.update_existing:
-                    existing = self.session.query(CjObjectModel).filter_by(object_id=obj_id).first()
+                # optionally check if the object exists - 
+                # to skip it or update it
+                if self.args.update_existing:
+                    existing = (
+                        self.session.query(CjObjectModel)
+                        .filter_by(object_id=obj_id)
+                        .first()
+                    )
 
                     if existing:
-                        if self.args.skip_existing:
-                            print(f"CityObject (id:{obj_id}) already exists. Skipping.")
-                            continue
-                        
-                        elif self.args.update_existing:
-                            print(f"CityObject (id:{obj_id}) already exists. Updating.")
-                            obj_to_update = existing
+                        # TODO: proper logging
+                        print(f"CityObject (id:{obj_id}) already exists. Updating.") # noqa
+                        obj_to_update = existing
 
                 # get 3D geom, ground geom and bbox
-                geometry, ground_geometry = self.get_geometries(obj_id, cityobj, vertices,
-                                                                        source_target_srid)
-                    
-                # check if the object type is allowed by the official spec or extension
-                check_result, message = check_object_type(cityobj.get("type"), 
-                                    self.cj_object_types, 
-                                    self.current.extension_handler.extra_city_objects)
+                geometry, ground_geometry = self.get_geometries(
+                    obj_id, cityobj, vertices, source_target_srid
+                )
+
+                # check if the object type is allowed by the official
+                # spec or extension
+                check_result, message = check_object_type(
+                    cityobj.get("type"),
+                    self.cj_object_types,
+                    self.current.extension_handler.extra_city_objects,
+                )
                 if not check_result:
                     print(message)
 
                 # update or insert the object
-                # 'or None' is added to change empty json "{}" to database null                
+                # 'or None' is added to change empty json "{}" to database null
                 if obj_to_update:
                     cj_object = obj_to_update
                     cj_object.type = cityobj.get("type")
                     cj_object.attributes = cityobj.get("attributes") or None
-                    cj_object.geometry=geometry
-                    cj_object.ground_geometry=ground_geometry
+                    cj_object.geometry = geometry
+                    cj_object.ground_geometry = ground_geometry
                     cj_object.import_meta = self.current.import_meta
                 else:
                     cj_object = CjObjectModel(
                         object_id=obj_id,
                         type=cityobj.get("type"),
                         attributes=cityobj.get("attributes") or None,
                         geometry=geometry,
-                        ground_geometry=ground_geometry
+                        ground_geometry=ground_geometry,
                     )
 
                     # add CityJson object to the database
                     cj_object.__table__.schema = self.args.db_schema
                     cj_object.import_meta_id = self.current.import_meta.id
                     self.current.cj_objects.append(to_dict(cj_object))
-            
+
                 cj_feature_objects[obj_id] = cj_object
 
                 # save children-parent links
                 for child_id in cityobj.get("children", []):
                     family_ties.append((obj_id, child_id))
 
                     # delete previous ties if updating object
                     if obj_to_update:
-                        children = self.session.query(FamilyModel).filter_by(child_id=child_id)
+                        children = self.session.query(FamilyModel).filter_by(
+                            child_id=child_id
+                        )
                         children.delete()
 
-
-            # create children-parent links after all objects from the CityJSONFeature already exist
+            # create children-parent links after all objects
+            # from the CityJSONFeature already exist
             for parent_id, child_id in family_ties:
-                self.current.families.append({"parent_id": parent_id, "child_id": child_id})
-
+                self.current.families.append(
+                    {"parent_id": parent_id, "child_id": child_id}
+                )
 
     def process_file(self, filepath):
         self.current = SingleFileImport(filepath)
         print("Running import for file: ", filepath)
 
         if filepath.lower() == "stdin":
             for line in sys.stdin:
                 self.process_line(line.rstrip("\n"))
         else:
             with open(filepath) as f:
                 for line in f.readlines():
                     self.process_line(line)
 
         if self.current.cj_objects:
-            obj_insert = insert(CjObjectModel).values(self.current.cj_objects)
+            obj_insert = (
+                insert(CjObjectModel)
+                .values(self.current.cj_objects)
+                .on_conflict_do_nothing()
+            )  # noqa
             self.session.execute(obj_insert)
 
         if self.current.families:
-            family_insert = insert(FamilyModel).values(self.current.families)
+            family_insert = (
+                insert(FamilyModel)
+                .values(self.current.families)
+                .on_conflict_do_nothing()
+            )  # noqa
             self.session.execute(family_insert)
-
         self.current.import_meta.finished_at = func.now()
         self.session.commit()
 
     def process_directory(self, dir_path):
         print("Running import for directory: ", dir_path)
-        ext = (".jsonl")
+        ext = ".jsonl"
         for f in os.scandir(dir_path):
             if f.path.endswith(ext):
                 self.process_file(f.path)
 
     def index_attributes(self):
         # postgres types to be used in type casted index
         postgres_type_mapping = {
             float: "float",
             str: "text",
             int: "int",
-            bool: "boolean"
+            bool: "boolean",
         }
 
         # python type mapping for the attributes based on sampled values
         type_mapping = CjObjectModel.get_attributes_and_types(self.session)
 
         # sql index command
-        cmd_base = "create index if not exists {table}_{attr_name}_idx " + \
-                "on {schema}.{table} using btree(((attributes->>'{attr_name}')::{attr_type}))"
+        cmd_base = (
+            "create index if not exists {table}_{attr_name}_idx "
+            + "on {schema}.{table} using "
+            + "btree(((attributes->>'{attr_name}')::{attr_type}))"
+        )
 
         # prepare partial and non partial indexes in one list
-        attributes = [(a, True) for a in self.args.partial_indexed_attributes] + \
-                    [(a, False) for a in self.args.indexed_attributes]
+        attributes = [(a, True) for a in self.args.partial_indexed_attributes] + [ #noqa
+            (a, False) for a in self.args.indexed_attributes
+        ]
 
         # for each attribute to be indexed
         for attr_name, is_partial in attributes:
             msg = f"Indexing CityObject attribute: '{attr_name}'"
             if is_partial:
                 msg += " with partial index"
             print(msg)
 
             # get proper postgres type
             if attr_name in type_mapping:
                 postgres_type = postgres_type_mapping[type_mapping[attr_name]]
 
                 # prepare and run sql command
                 if is_partial:
-                    cmd = cmd_base + " WHERE attributes->>'{attr_name}' IS NOT NULL"
+                    cmd = cmd_base
+                    + " WHERE attributes->>'{attr_name}' IS NOT NULL"
                 else:
                     cmd = cmd_base
 
                 cmd = cmd.format(
                     table=CjObjectModel.__table__.name,
                     schema=CjObjectModel.__table__.schema,
                     attr_name=attr_name,
-                    attr_type=postgres_type
+                    attr_type=postgres_type,
                 )
-                self.engine.execute(cmd)
+                with self.engine.connect() as conn:
+                    conn.execute(text(cmd))
 
             else:
-                print(f"Specified attribute to be indexed: '{attr_name}' does not exist")
+                print(
+                    f"Specified attribute to be indexed: '{attr_name}' does not exist" # noqa
+                )
 
     def get_geometries(self, obj_id, cityobj, vertices, source_target_srid):
         if "geometry" not in cityobj:
             return None, None
-        
+
         # returned geometry is already in the required projection
-        geometry = resolve_geometry_vertices(cityobj["geometry"], 
-                                            vertices,
-                                            self.current.import_meta.geometry_templates,
-                                            source_target_srid)
+        geometry = resolve_geometry_vertices(
+            cityobj["geometry"],
+            vertices,
+            self.current.import_meta.geometry_templates,
+            source_target_srid,
+        )
 
         ground_geometry = get_ground_geometry(geometry, obj_id)
 
-        if ((ground_geometry is None) is False):
-            if (not self.current.target_srid):
+        if (ground_geometry is None) is False:
+            if not self.current.target_srid:
                 ground_geometry = func.st_geomfromtext(ground_geometry.wkt)
             else:
-                ground_geometry = func.st_geomfromtext(ground_geometry.wkt, self.current.target_srid)
-                
+                ground_geometry = func.st_geomfromtext(
+                    ground_geometry.wkt, self.current.target_srid
+                )
 
         return geometry, ground_geometry
```

### Comparing `cjdb-1.0.0/cjdb/modules/utils.py` & `cjdb-1.1.0/cjdb/modules/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,15 @@
+import os
+from pathlib import Path
+
 import psycopg2
 from psycopg2.extras import RealDictCursor
 from sqlalchemy import create_engine
-import os
-from pathlib import Path
-from cj2pgsql.resources import object_types
+
+from cjdb.resources import object_types
 
 
 def get_db_engine(args, echo=False):
     conn_string = f"postgresql://{args.db_user}:{args.db_password}"\
         f"@{args.db_host}:{args.db_port}/{args.db_name}"
 
     engine = create_engine(conn_string, echo=echo)
```

### Comparing `cjdb-1.0.0/cjdb/resources/object_types.py` & `cjdb-1.1.0/cjdb/resources/object_types.py`

 * *Files identical despite different names*

### Comparing `cjdb-1.0.0/cjdb/resources/post_import.sql` & `cjdb-1.1.0/cjdb/resources/post_import.sql`

 * *Files identical despite different names*

### Comparing `cjdb-1.0.0/cjdb/resources/strings.py` & `cjdb-1.1.0/cjdb/resources/strings.py`

 * *Files identical despite different names*

### Comparing `cjdb-1.0.0/setup.py` & `cjdb-1.1.0/setup.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,34 +1,43 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
-['cjdb', 'cjdb.modules', 'cjdb.resources', 'cjdb.test']
+['cjdb',
+ 'cjdb.model',
+ 'cjdb.model.sqlalchemy_models',
+ 'cjdb.modules',
+ 'cjdb.resources']
 
 package_data = \
-{'': ['*'], 'cjdb.test': ['files/*', 'files/cjfiles/*', 'inputs/*']}
+{'': ['*']}
 
 install_requires = \
-['GeoAlchemy>=0.7.2,<0.8.0',
+['geoalchemy2>=0.13.1,<0.14.0',
  'numpy>=1.24.2,<2.0.0',
+ 'psycopg2-binary>=2.9.6,<3.0.0',
  'pyproj>=3.5.0,<4.0.0',
  'requests>=2.28.2,<3.0.0',
  'shapely>=2.0.1,<3.0.0']
 
+entry_points = \
+{'console_scripts': ['cjdb = cjdb.main:main']}
+
 setup_kwargs = {
     'name': 'cjdb',
-    'version': '1.0.0',
-    'description': 'Import city.json files to postgreSQL',
-    'long_description': '# cjdb\n[![MIT badge](https://img.shields.io/pypi/l/cjdb)](LICENSE) &nbsp; [![PyPI](https://img.shields.io/pypi/v/cjdb)](https://pypi.org/project/cjdb)\n\nCJDB is a tool for enabling CityJSON integration with a PostgreSQL database.\n\nAuthors: Cynthia Cai, Lan Yan, Yitong Xia, Chris Poon, Siebren Meines, Leon Powalka\n\n## Table of Contents  \n### [1. Data model](#model)\n### [2. Installation & running](#install)\n### [3. Local development](#local)\n### [4. Local CLI development](#cli)\n---\n## 1. Data model <a name="model"></a>\nFor the underlying data model see [model/README.md](model/README.md)\n\nBased on this model, there are 2 software components available:\n\n### cj2pgsql\nSee [cj2pgsql/README.md](cj2pgsql/README.md)\n\n## 2. Installation & running <a name="install"></a>\n### Using pip\n\nIt is recommended to install it in an isolated environment, because of fragile external library dependencies for CQL filter parsing.\n\n```\npip install cjdb\n```\n\n\n### Using the repository code\nAnother option is to clone the repository and build the CLI from the code.\nFrom repository root, run:\n```\npip3 install build wheel\npython3 -m build\n```\n\nThen install the .whl file with pip:\n```\npip3 install dist/*.whl --force-reinstall\n```\n\n### Using docker\nBuild:\n```\ndocker build -t cjdb:latest .\n```\n\nRun: **cj2pgsql**\n```\ndocker run --rm -it cjdb cj2pgsql --help\n```\n\nTo import some files, the `-v` option is needed to mount our local file directory in the container.\n```\ndocker run -v {MYDIRECTORY}:/data --rm -it --network=host cjdb cj2pgsql -H localhost -U postgres -d postgres -W postgres /data/5870_ext.jsonl \n```\n\nFor instructions on running the software check specific READMEs.\n\n\n## 3. Local development <a name="local"></a>\nMake sure pipenv is installed:\n```\npip install pipenv\n```\nCreate the environment:\n```\npipenv install\n```\n\n## 4. Local CLI development <a name="cli"></a>\n---\nTo build the CLI app (so that it can be called as a command line tool from anywhere):\n\n\n1. Sync the pipenv requirements with the setup.py file:\n```\npipenv run pipenv-setup sync\n```\n\n2. Create a venv just for testing the CLI build.\n\n**Note**: This is not the pipenv/development environment.\n```\nvirtualenv venv\n```\n3. Activate environment (note: this is not the pipenv environment. This is a separate environment just to test the CLI build)\n```\n. venv/bin/activate\n\n```\n\n4. Build the CLI:\n```\npython setup.py develop\n```\n\n5. The cj2pgsql importer should now work as a command inside this environment:\n```\ncj2pgsql --help\n```\n',
-    'author': 'Gina Stavropoulou',
-    'author_email': 'ginastavropoulou@gmail.com',
-    'maintainer': 'None',
-    'maintainer_email': 'None',
-    'url': 'None',
+    'version': '1.1.0',
+    'description': 'CJDB is a tool that enables CityJSON integration with a PostgreSQL database',
+    'long_description': '# cjdb\n[![MIT badge](https://img.shields.io/pypi/l/cjdb)](LICENSE) &nbsp; [![PyPI](https://img.shields.io/pypi/v/cjdb)](https://pypi.org/project/cjdb)\n\nCJDB is a tool for enabling CityJSON integration with a PostgreSQL database.\n\nAuthors: Cynthia Cai, Lan Yan, Yitong Xia, Chris Poon, Siebren Meines, Leon Powalka\n\nMaintainer: Gina Stavropoulou\n\n## Table of Contents  \n### [1. Data model](#model)\n### [2. Installation & running](#install)\n### [3. Local development](#local)\n### [4. Running tests](#tests)\n---\n## 1. Data model <a name="model"></a>\nFor the underlying data model see [cjdb/model/README.md](cjdb/model/README.md)\n\n\n## 2. Installation & running <a name="install"></a>\n### Using pip\n\n```bash\npip install cjdb\n```\nIt is recommended to install it in an isolated environment, because of fragile external library dependencies for CQL filter parsing.\n\n### Using docker\nBuild:\n```bash\ndocker build -t cjdb:latest .\n```\n\nRun:\n```bash\ndocker run --rm -it cjdb cjdb --help\n```\n\nTo import some files, the `-v` option is needed to mount our local file directory in the container:\n```bash\ndocker run -v {MYDIRECTORY}:/data --rm -it --network=host cjdb cjdb -H localhost -U postgres -d postgres -W postgres /data/5870_ext.jsonl \n```\n\n## 3. Local development <a name="local"></a>\nMake sure `poetry` is installed. Then, to create a local environment with all the necessary dependencies, run from the repository root:\n```bash\npoetry install\n```\n\nTo build the wheel run:\n```bash\npoetry build\n```\n\nThen install the .whl file with pip:\n```bash\npip3 install dist/*.whl --force-reinstall\n```\n\nThen you can run the CLI command:\n```bash\ncjdb --help\n```\n\n## 4. Running tests <a name="tests"></a>\n---\nModify the arguments for the database connection to your own settings in:\n- /tests/cli_test.py\n\nThen run:\n```bash\npytest -v\n```\n\n\n\n\n\n',
+    'author': 'Cynthia Cai',
+    'author_email': 'None',
+    'maintainer': 'Gina Stavropoulou',
+    'maintainer_email': 'g.stavropoulou@tudelft.nl',
+    'url': 'https://github.com/tudelft3d/cjdb',
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
+    'entry_points': entry_points,
     'python_requires': '>=3.11,<4.0',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `cjdb-1.0.0/PKG-INFO` & `cjdb-1.1.0/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,123 +1,102 @@
 Metadata-Version: 2.1
 Name: cjdb
-Version: 1.0.0
-Summary: Import city.json files to postgreSQL
+Version: 1.1.0
+Summary: CJDB is a tool that enables CityJSON integration with a PostgreSQL database
+Home-page: https://github.com/tudelft3d/cjdb
 License: MIT
-Author: Gina Stavropoulou
-Author-email: ginastavropoulou@gmail.com
+Keywords: CityJSON,PostgreSQL
+Author: Cynthia Cai
+Maintainer: Gina Stavropoulou
+Maintainer-email: g.stavropoulou@tudelft.nl
 Requires-Python: >=3.11,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.11
-Requires-Dist: GeoAlchemy (>=0.7.2,<0.8.0)
+Requires-Dist: geoalchemy2 (>=0.13.1,<0.14.0)
 Requires-Dist: numpy (>=1.24.2,<2.0.0)
+Requires-Dist: psycopg2-binary (>=2.9.6,<3.0.0)
 Requires-Dist: pyproj (>=3.5.0,<4.0.0)
 Requires-Dist: requests (>=2.28.2,<3.0.0)
 Requires-Dist: shapely (>=2.0.1,<3.0.0)
+Project-URL: Repository, https://github.com/tudelft3d/cjdb
 Description-Content-Type: text/markdown
 
 # cjdb
 [![MIT badge](https://img.shields.io/pypi/l/cjdb)](LICENSE) &nbsp; [![PyPI](https://img.shields.io/pypi/v/cjdb)](https://pypi.org/project/cjdb)
 
 CJDB is a tool for enabling CityJSON integration with a PostgreSQL database.
 
 Authors: Cynthia Cai, Lan Yan, Yitong Xia, Chris Poon, Siebren Meines, Leon Powalka
 
+Maintainer: Gina Stavropoulou
+
 ## Table of Contents  
 ### [1. Data model](#model)
 ### [2. Installation & running](#install)
 ### [3. Local development](#local)
-### [4. Local CLI development](#cli)
+### [4. Running tests](#tests)
 ---
 ## 1. Data model <a name="model"></a>
-For the underlying data model see [model/README.md](model/README.md)
-
-Based on this model, there are 2 software components available:
+For the underlying data model see [cjdb/model/README.md](cjdb/model/README.md)
 
-### cj2pgsql
-See [cj2pgsql/README.md](cj2pgsql/README.md)
 
 ## 2. Installation & running <a name="install"></a>
 ### Using pip
 
-It is recommended to install it in an isolated environment, because of fragile external library dependencies for CQL filter parsing.
-
-```
+```bash
 pip install cjdb
 ```
-
-
-### Using the repository code
-Another option is to clone the repository and build the CLI from the code.
-From repository root, run:
-```
-pip3 install build wheel
-python3 -m build
-```
-
-Then install the .whl file with pip:
-```
-pip3 install dist/*.whl --force-reinstall
-```
+It is recommended to install it in an isolated environment, because of fragile external library dependencies for CQL filter parsing.
 
 ### Using docker
 Build:
-```
+```bash
 docker build -t cjdb:latest .
 ```
 
-Run: **cj2pgsql**
-```
-docker run --rm -it cjdb cj2pgsql --help
+Run:
+```bash
+docker run --rm -it cjdb cjdb --help
 ```
 
-To import some files, the `-v` option is needed to mount our local file directory in the container.
-```
-docker run -v {MYDIRECTORY}:/data --rm -it --network=host cjdb cj2pgsql -H localhost -U postgres -d postgres -W postgres /data/5870_ext.jsonl 
+To import some files, the `-v` option is needed to mount our local file directory in the container:
+```bash
+docker run -v {MYDIRECTORY}:/data --rm -it --network=host cjdb cjdb -H localhost -U postgres -d postgres -W postgres /data/5870_ext.jsonl 
 ```
 
-For instructions on running the software check specific READMEs.
-
-
 ## 3. Local development <a name="local"></a>
-Make sure pipenv is installed:
+Make sure `poetry` is installed. Then, to create a local environment with all the necessary dependencies, run from the repository root:
+```bash
+poetry install
 ```
-pip install pipenv
+
+To build the wheel run:
+```bash
+poetry build
 ```
-Create the environment:
+
+Then install the .whl file with pip:
+```bash
+pip3 install dist/*.whl --force-reinstall
 ```
-pipenv install
+
+Then you can run the CLI command:
+```bash
+cjdb --help
 ```
 
-## 4. Local CLI development <a name="cli"></a>
+## 4. Running tests <a name="tests"></a>
 ---
-To build the CLI app (so that it can be called as a command line tool from anywhere):
+Modify the arguments for the database connection to your own settings in:
+- /tests/cli_test.py
 
-
-1. Sync the pipenv requirements with the setup.py file:
-```
-pipenv run pipenv-setup sync
+Then run:
+```bash
+pytest -v
 ```
 
-2. Create a venv just for testing the CLI build.
 
-**Note**: This is not the pipenv/development environment.
-```
-virtualenv venv
-```
-3. Activate environment (note: this is not the pipenv environment. This is a separate environment just to test the CLI build)
-```
-. venv/bin/activate
 
-```
 
-4. Build the CLI:
-```
-python setup.py develop
-```
 
-5. The cj2pgsql importer should now work as a command inside this environment:
-```
-cj2pgsql --help
-```
```

