# Comparing `tmp/fhir-cli-0.9.0.tar.gz` & `tmp/fhir-cli-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fhir-cli-0.9.0.tar", last modified: Wed Mar 30 10:25:18 2022, max compression
+gzip compressed data, was "fhir-cli-0.9.1.tar", last modified: Wed Mar 30 12:39:52 2022, max compression
```

## Comparing `fhir-cli-0.9.0.tar` & `fhir-cli-0.9.1.tar`

### file list

```diff
@@ -1,38 +1,38 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.523995 fhir-cli-0.9.0/
--rw-r--r--   0 runner    (1001) docker     (116)    11356 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (116)       32 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (116)     2829 2022-03-30 10:25:18.523995 fhir-cli-0.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     2309 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/README.md
--rw-r--r--   0 runner    (1001) docker     (116)      587 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (116)     1005 2022-03-30 10:25:18.523995 fhir-cli-0.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)       38 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.519995 fhir-cli-0.9.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.519995 fhir-cli-0.9.0/src/fhir_cli/
--rw-r--r--   0 runner    (1001) docker     (116)     1598 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     7377 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/admin.py
--rw-r--r--   0 runner    (1001) docker     (116)     7514 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/cli.py
--rw-r--r--   0 runner    (1001) docker     (116)     4630 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/dbt.py
--rw-r--r--   0 runner    (1001) docker     (116)     2212 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/fhir_resource.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.523995 fhir-cli-0.9.0/src/fhir_cli/templates/
--rw-r--r--   0 runner    (1001) docker     (116)     2740 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/01-OMOPCDM_postgresql_5.4_ddl.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)      546 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/02-OMOPCDM_postgresql_5.4_primary_keys.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)     1169 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/03-vocabulary.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)     3358 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/04-OMOPCDM_postgresql_5.4_constraints.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)     2923 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/05-OMOPCDM_postgresql_5.4_indices.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)     6009 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/init_db.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)      377 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/oracle_fdw.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)      411 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/postgres_fdw.sql.j2
--rw-r--r--   0 runner    (1001) docker     (116)      608 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/fhir_cli/templates/postgres_source_connector.json.j2
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.519995 fhir-cli-0.9.0/src/fhir_cli.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)     2829 2022-03-30 10:25:17.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)      997 2022-03-30 10:25:18.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2022-03-30 10:25:17.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       42 2022-03-30 10:25:18.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (116)      256 2022-03-30 10:25:18.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)       15 2022-03-30 10:25:18.000000 fhir-cli-0.9.0/src/fhir_cli.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:18.523995 fhir-cli-0.9.0/src/utils/
--rw-r--r--   0 runner    (1001) docker     (116)        0 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)      889 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/utils/compact.py
--rw-r--r--   0 runner    (1001) docker     (116)      713 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/utils/dotty.py
--rw-r--r--   0 runner    (1001) docker     (116)      173 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/utils/number_print.py
--rw-r--r--   0 runner    (1001) docker     (116)      301 2022-03-30 10:25:06.000000 fhir-cli-0.9.0/src/utils/prettify_json.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.257459 fhir-cli-0.9.1/
+-rw-r--r--   0 runner    (1001) docker     (116)    11356 2022-03-30 12:39:38.000000 fhir-cli-0.9.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (116)       32 2022-03-30 12:39:38.000000 fhir-cli-0.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (116)     2829 2022-03-30 12:39:52.257459 fhir-cli-0.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     2309 2022-03-30 12:39:38.000000 fhir-cli-0.9.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (116)      587 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (116)     1005 2022-03-30 12:39:52.261459 fhir-cli-0.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (116)       38 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.241459 fhir-cli-0.9.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.249459 fhir-cli-0.9.1/src/fhir_cli/
+-rw-r--r--   0 runner    (1001) docker     (116)     1598 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     7377 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/admin.py
+-rw-r--r--   0 runner    (1001) docker     (116)     7514 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/cli.py
+-rw-r--r--   0 runner    (1001) docker     (116)     4630 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/dbt.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2212 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/fhir_resource.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.257459 fhir-cli-0.9.1/src/fhir_cli/templates/
+-rw-r--r--   0 runner    (1001) docker     (116)     2740 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/01-OMOPCDM_postgresql_5.4_ddl.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)      546 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/02-OMOPCDM_postgresql_5.4_primary_keys.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)     1169 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/03-vocabulary.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)     3358 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/04-OMOPCDM_postgresql_5.4_constraints.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)     2923 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/05-OMOPCDM_postgresql_5.4_indices.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)     6009 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/init_db.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)      377 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/oracle_fdw.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)      411 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/postgres_fdw.sql.j2
+-rw-r--r--   0 runner    (1001) docker     (116)      608 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/fhir_cli/templates/postgres_source_connector.json.j2
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.253459 fhir-cli-0.9.1/src/fhir_cli.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)     2829 2022-03-30 12:39:51.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)      997 2022-03-30 12:39:52.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2022-03-30 12:39:51.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       42 2022-03-30 12:39:51.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      256 2022-03-30 12:39:52.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       15 2022-03-30 12:39:52.000000 fhir-cli-0.9.1/src/fhir_cli.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:52.257459 fhir-cli-0.9.1/src/utils/
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)      889 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/utils/compact.py
+-rw-r--r--   0 runner    (1001) docker     (116)      713 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/utils/dotty.py
+-rw-r--r--   0 runner    (1001) docker     (116)      173 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/utils/number_print.py
+-rw-r--r--   0 runner    (1001) docker     (116)      301 2022-03-30 12:39:39.000000 fhir-cli-0.9.1/src/utils/prettify_json.py
```

### Comparing `fhir-cli-0.9.0/LICENSE` & `fhir-cli-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/PKG-INFO` & `fhir-cli-0.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fhir-cli
-Version: 0.9.0
+Version: 0.9.1
 Summary: DBTonFhir cli
 Home-page: https://github.com/arkhn/dbtonfhir
 Author: Arkhn
 Author-email: engineering@arkhn.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/arkhn/dbtonfhir/issues
 Platform: UNKNOWN
```

### Comparing `fhir-cli-0.9.0/README.md` & `fhir-cli-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/pyproject.toml` & `fhir-cli-0.9.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/setup.cfg` & `fhir-cli-0.9.1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = fhir-cli
-version = 0.9.0
+version = 0.9.1
 author = Arkhn
 author_email = engineering@arkhn.com
 description = DBTonFhir cli
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/arkhn/dbtonfhir
 project_urls =
```

### Comparing `fhir-cli-0.9.0/src/fhir_cli/__init__.py` & `fhir-cli-0.9.1/src/fhir_cli/__init__.py`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/admin.py` & `fhir-cli-0.9.1/src/fhir_cli/admin.py`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/cli.py` & `fhir-cli-0.9.1/src/fhir_cli/cli.py`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/dbt.py` & `fhir-cli-0.9.1/src/fhir_cli/dbt.py`

 * *Files 0% similar despite different names*

```diff
@@ -40,15 +40,15 @@
     stmt = result.group(1)
     references = [
         reference.strip() for reference in result.group(3).split(",") if reference.strip()
     ]
     if not references:
         raise EmptyDbtReferenceWarning("no reference has been specified")
     for reference in references:
-        stmt, match = re.subn(fr"(\s+|^){reference}\b", f"\\1{{{{ref('{reference}')}}}}", stmt)
+        stmt, match = re.subn(rf"(\s+|^){reference}\b", f"\\1{{{{ref('{reference}')}}}}", stmt)
         if not match:
             raise UnknownDbtReferenceError(f"{reference} is unknown")
     return stmt
 
 
 class Dbt:
     """The dbt command manages your DBT project"""
```

### Comparing `fhir-cli-0.9.0/src/fhir_cli/fhir_resource.py` & `fhir-cli-0.9.1/src/fhir_cli/fhir_resource.py`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/01-OMOPCDM_postgresql_5.4_ddl.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/01-OMOPCDM_postgresql_5.4_ddl.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/02-OMOPCDM_postgresql_5.4_primary_keys.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/02-OMOPCDM_postgresql_5.4_primary_keys.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/03-vocabulary.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/03-vocabulary.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/04-OMOPCDM_postgresql_5.4_constraints.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/04-OMOPCDM_postgresql_5.4_constraints.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/05-OMOPCDM_postgresql_5.4_indices.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/05-OMOPCDM_postgresql_5.4_indices.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/init_db.sql.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/init_db.sql.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli/templates/postgres_source_connector.json.j2` & `fhir-cli-0.9.1/src/fhir_cli/templates/postgres_source_connector.json.j2`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/fhir_cli.egg-info/PKG-INFO` & `fhir-cli-0.9.1/src/fhir_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fhir-cli
-Version: 0.9.0
+Version: 0.9.1
 Summary: DBTonFhir cli
 Home-page: https://github.com/arkhn/dbtonfhir
 Author: Arkhn
 Author-email: engineering@arkhn.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/arkhn/dbtonfhir/issues
 Platform: UNKNOWN
```

### Comparing `fhir-cli-0.9.0/src/fhir_cli.egg-info/SOURCES.txt` & `fhir-cli-0.9.1/src/fhir_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/utils/compact.py` & `fhir-cli-0.9.1/src/utils/compact.py`

 * *Files identical despite different names*

### Comparing `fhir-cli-0.9.0/src/utils/dotty.py` & `fhir-cli-0.9.1/src/utils/dotty.py`

 * *Files identical despite different names*

