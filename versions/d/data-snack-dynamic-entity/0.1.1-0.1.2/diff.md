# Comparing `tmp/data_snack_dynamic_entity-0.1.1.tar.gz` & `tmp/data_snack_dynamic_entity-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_snack_dynamic_entity-0.1.1.tar", last modified: Mon Jan 30 16:25:17 2023, max compression
+gzip compressed data, was "data_snack_dynamic_entity-0.1.2.tar", last modified: Fri Apr  7 08:27:42 2023, max compression
```

## Comparing `data_snack_dynamic_entity-0.1.1.tar` & `data_snack_dynamic_entity-0.1.2.tar`

### file list

```diff
@@ -1,25 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      129 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1685 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      739 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      596 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2148 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/entityTemplates.schema.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/factory/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/factory/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1807 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/factory/entity_creation.py
--rw-r--r--   0 runner    (1001) docker     (123)      778 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/factory/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/types.py
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-01-30 16:25:07.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 16:25:17.448385 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-01-30 16:25:17.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      680 2023-01-30 16:25:17.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 16:25:17.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-01-30 16:25:17.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-01-30 16:25:17.000000 data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:27:42.567129 data_snack_dynamic_entity-0.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      129 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-04-07 08:27:42.567129 data_snack_dynamic_entity-0.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1685 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      739 2023-04-07 08:27:42.567129 data_snack_dynamic_entity-0.1.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      596 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:27:42.563129 data_snack_dynamic_entity-0.1.2/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:27:42.567129 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2148 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/entityTemplates.schema.json
+-rw-r--r--   0 runner    (1001) docker     (123)     3513 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      728 2023-04-07 08:27:25.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:27:42.567129 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2265 2023-04-07 08:27:42.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-07 08:27:42.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:27:42.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-07 08:27:42.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-07 08:27:42.000000 data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/top_level.txt
```

### Comparing `data_snack_dynamic_entity-0.1.1/LICENSE` & `data_snack_dynamic_entity-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `data_snack_dynamic_entity-0.1.1/PKG-INFO` & `data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: data_snack_dynamic_entity
-Version: 0.1.1
+Name: data-snack-dynamic-entity
+Version: 0.1.2
 Home-page: https://github.com/webinterpret-ds/data-snack-dynamic-entity
 Author: webinterpret-datascience
 Author-email: data-science@webinterpret.com
 Project-URL: Bug Tracker, https://github.com/webinterpret-ds/data-snack-dynamic-entity/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `data_snack_dynamic_entity-0.1.1/README.md` & `data_snack_dynamic_entity-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `data_snack_dynamic_entity-0.1.1/setup.cfg` & `data_snack_dynamic_entity-0.1.2/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = data-snack-dynamic-entity
-version = 0.1.1
+version = 0.1.2
 author = webinterpret-datascience
 author_email = data-science@webinterpret.com
 description = 
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/webinterpret-ds/data-snack-dynamic-entity
 project_urls =
```

### Comparing `data_snack_dynamic_entity-0.1.1/setup.py` & `data_snack_dynamic_entity-0.1.2/setup.py`

 * *Files identical despite different names*

### Comparing `data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/entityTemplates.schema.json` & `data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/entityTemplates.schema.json`

 * *Files identical despite different names*

### Comparing `data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity/validate.py` & `data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity/validate.py`

 * *Files identical despite different names*

### Comparing `data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/PKG-INFO` & `data_snack_dynamic_entity-0.1.2/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: data-snack-dynamic-entity
-Version: 0.1.1
+Name: data_snack_dynamic_entity
+Version: 0.1.2
 Home-page: https://github.com/webinterpret-ds/data-snack-dynamic-entity
 Author: webinterpret-datascience
 Author-email: data-science@webinterpret.com
 Project-URL: Bug Tracker, https://github.com/webinterpret-ds/data-snack-dynamic-entity/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `data_snack_dynamic_entity-0.1.1/src/data_snack_dynamic_entity.egg-info/SOURCES.txt` & `data_snack_dynamic_entity-0.1.2/src/data_snack_dynamic_entity.egg-info/SOURCES.txt`

 * *Files 16% similar despite different names*

```diff
@@ -3,17 +3,15 @@
 README.md
 pyproject.toml
 requirements.txt
 setup.cfg
 setup.py
 src/data_snack_dynamic_entity/__init__.py
 src/data_snack_dynamic_entity/entityTemplates.schema.json
+src/data_snack_dynamic_entity/factory.py
 src/data_snack_dynamic_entity/types.py
 src/data_snack_dynamic_entity/validate.py
 src/data_snack_dynamic_entity.egg-info/PKG-INFO
 src/data_snack_dynamic_entity.egg-info/SOURCES.txt
 src/data_snack_dynamic_entity.egg-info/dependency_links.txt
 src/data_snack_dynamic_entity.egg-info/requires.txt
-src/data_snack_dynamic_entity.egg-info/top_level.txt
-src/data_snack_dynamic_entity/factory/__init__.py
-src/data_snack_dynamic_entity/factory/entity_creation.py
-src/data_snack_dynamic_entity/factory/loader.py
+src/data_snack_dynamic_entity.egg-info/top_level.txt
```

