# Comparing `tmp/griffon-0.1.8.tar.gz` & `tmp/griffon-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "griffon-0.1.8.tar", last modified: Fri Mar 31 09:57:16 2023, max compression
+gzip compressed data, was "griffon-0.1.9.tar", last modified: Fri Mar 31 11:59:25 2023, max compression
```

## Comparing `griffon-0.1.8.tar` & `griffon-0.1.9.tar`

### file list

```diff
@@ -1,52 +1,52 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.965978 griffon-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-31 09:56:56.000000 griffon-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-03-31 09:57:16.965978 griffon-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-03-31 09:56:56.000000 griffon-0.1.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.957978 griffon-0.1.8/griffon/
--rw-r--r--   0 runner    (1001) docker     (123)     6255 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.957978 griffon-0.1.8/griffon/autocomplete/
--rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/autocomplete/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3354 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.961978 griffon-0.1.8/griffon/commands/
--rw-r--r--   0 runner    (1001) docker     (123)     1525 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/configure.py
--rw-r--r--   0 runner    (1001) docker     (123)     1576 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/docs.py
--rw-r--r--   0 runner    (1001) docker     (123)    18280 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/entities.py
--rw-r--r--   0 runner    (1001) docker     (123)     1784 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/manage.py
--rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugin_commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.961978 griffon-0.1.8/griffon/commands/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugins/cve_mitre.py
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugins/cvelib.py
--rw-r--r--   0 runner    (1001) docker     (123)      396 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugins/fcc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugins/go_vuln.py
--rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/plugins/osv.py
--rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/process.py
--rw-r--r--   0 runner    (1001) docker     (123)    22098 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/queries.py
--rw-r--r--   0 runner    (1001) docker     (123)     2815 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/commands/reports.py
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    30131 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/output.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.961978 griffon-0.1.8/griffon/services/
--rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/services/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      592 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/services/core_process.py
--rw-r--r--   0 runner    (1001) docker     (123)    37876 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/services/core_queries.py
--rw-r--r--   0 runner    (1001) docker     (123)    19336 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/services/core_reports.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.961978 griffon-0.1.8/griffon/static/
--rw-r--r--   0 runner    (1001) docker     (123)     1993 2023-03-31 09:56:56.000000 griffon-0.1.8/griffon/static/default_griffonrc
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.957978 griffon-0.1.8/griffon.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-31 09:57:16.000000 griffon-0.1.8/griffon.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-31 09:56:56.000000 griffon-0.1.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 09:57:16.965978 griffon-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-03-31 09:56:56.000000 griffon-0.1.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 09:57:16.965978 griffon-0.1.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      601 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_entities.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_manage.py
--rw-r--r--   0 runner    (1001) docker     (123)      366 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_plugins.py
--rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_process.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_queries.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_reports.py
--rw-r--r--   0 runner    (1001) docker     (123)     1450 2023-03-31 09:56:56.000000 griffon-0.1.8/tests/test_unit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-31 11:59:11.000000 griffon-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-03-31 11:59:25.885891 griffon-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-03-31 11:59:11.000000 griffon-0.1.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.881891 griffon-0.1.9/griffon/
+-rw-r--r--   0 runner    (1001) docker     (123)     6255 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.881891 griffon-0.1.9/griffon/autocomplete/
+-rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/autocomplete/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3354 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/griffon/commands/
+-rw-r--r--   0 runner    (1001) docker     (123)     1525 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/configure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1576 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/docs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18280 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/entities.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1784 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/manage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugin_commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/griffon/commands/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugins/cve_mitre.py
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugins/cvelib.py
+-rw-r--r--   0 runner    (1001) docker     (123)      396 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugins/fcc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugins/go_vuln.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/plugins/osv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/process.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22098 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/queries.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2815 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/commands/reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30001 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/output.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/griffon/services/
+-rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/services/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      592 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/services/core_process.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37876 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/services/core_queries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19336 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/services/core_reports.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/griffon/static/
+-rw-r--r--   0 runner    (1001) docker     (123)     1993 2023-03-31 11:59:11.000000 griffon-0.1.9/griffon/static/default_griffonrc
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.881891 griffon-0.1.9/griffon.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2464 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-31 11:59:25.000000 griffon-0.1.9/griffon.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-31 11:59:11.000000 griffon-0.1.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 11:59:25.885891 griffon-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-03-31 11:59:11.000000 griffon-0.1.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:59:25.885891 griffon-0.1.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      601 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_entities.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_manage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      366 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_plugins.py
+-rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_process.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_queries.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1450 2023-03-31 11:59:11.000000 griffon-0.1.9/tests/test_unit.py
```

### Comparing `griffon-0.1.8/LICENSE` & `griffon-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/PKG-INFO` & `griffon-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: griffon
-Version: 0.1.8
+Version: 0.1.9
 Summary: Red Hat Product Security CLI
 Home-page: https://github.com/RedHatProductSecurity/griffon
 Author: James Fuller, Red Hat Product Security
 License: MIT
 Classifier: Topic :: Security
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

### Comparing `griffon-0.1.8/README.md` & `griffon-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/__init__.py` & `griffon-0.1.9/griffon/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 import component_registry_bindings
 import osidb_bindings
 from pkg_resources import resource_filename  # type: ignore
 from rich.logging import RichHandler
 
 from griffon.output import console
 
-__version__ = "0.1.8"
+__version__ = "0.1.9"
 
 if "CORGI_API_URL" not in os.environ:
     print("Must set CORGI_API_URL environment variable.")
     exit(1)
 CORGI_API_URL = os.environ["CORGI_API_URL"]
 
 if "OSIDB_API_URL" not in os.environ:
```

### Comparing `griffon-0.1.8/griffon/autocomplete/__init__.py` & `griffon-0.1.9/griffon/autocomplete/__init__.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/cli.py` & `griffon-0.1.9/griffon/cli.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/configure.py` & `griffon-0.1.9/griffon/commands/configure.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/docs.py` & `griffon-0.1.9/griffon/commands/docs.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/entities.py` & `griffon-0.1.9/griffon/commands/entities.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/manage.py` & `griffon-0.1.9/griffon/commands/manage.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/plugin_commands.py` & `griffon-0.1.9/griffon/commands/plugin_commands.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/plugins/go_vuln.py` & `griffon-0.1.9/griffon/commands/plugins/go_vuln.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/plugins/osv.py` & `griffon-0.1.9/griffon/commands/plugins/osv.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/process.py` & `griffon-0.1.9/griffon/commands/process.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/queries.py` & `griffon-0.1.9/griffon/commands/queries.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/commands/reports.py` & `griffon-0.1.9/griffon/commands/reports.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/output.py` & `griffon-0.1.9/griffon/output.py`

 * *Files 2% similar despite different names*

```diff
@@ -540,44 +540,44 @@
                     if purl.type == "oci":
                         component_ns = Text("REDHAT", style="bold magenta")
                     elif not purl.namespace:
                         component_ns = Text("UPSTREAM", style="bold magenta")
                     else:
                         component_ns = Text(purl.namespace.upper(), style="bold red")
 
-                    version = output_version(ctx, purl.version)
-                    if "version" in row:
-                        version = row["version"]
-                        if purl.version:
-                            if purl.version.startswith("sha256"):
-                                version = f"{row['version']} {output_version(ctx,purl.version)}"
+                    sha256 = ""
+                    if purl.version:
+                        if purl.version.startswith("sha256"):
+                            sha256 = output_version(ctx, purl.version)
+                    nvr = None
+                    if "nvr" in row:
+                        nvr = row["nvr"]
 
-                    if "release" in row:
-                        version = f"{version}-{row['release']}"
                     if not ctx.obj["SHOW_PURL"]:
                         if ctx.obj["VERBOSE"] == 0:
                             console.print(
                                 component_ns,
                                 purl.type.upper(),
-                                Text(purl.name, style="bold white"),
-                                version,
+                                Text(nvr, style="bold white"),
+                                sha256,
                                 row["related_url"],
                                 purl.qualifiers.get("arch"),
                             )
                         if ctx.obj["VERBOSE"] == 1:
-                            component_name = purl.name
-                            if "nvr" in row:
-                                component_name = row["nvr"]
+                            download_url = ""
+                            if "download_url" in row:
+                                download_url = row["download_url"]
                             console.print(
                                 component_ns,
                                 purl.type.upper(),
-                                Text(component_name, style="bold white"),
+                                Text(nvr, style="bold white"),
+                                sha256,
                                 row["related_url"],
-                                row["download_url"],
                                 purl.qualifiers.get("arch"),
+                                download_url,
                             )
                     else:
                         console.print(
                             row["purl"],
                         )
         # handle flaw
         if "cve_id" in output["results"][0]:
```

### Comparing `griffon-0.1.8/griffon/services/__init__.py` & `griffon-0.1.9/griffon/services/__init__.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/services/core_process.py` & `griffon-0.1.9/griffon/services/core_process.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/services/core_queries.py` & `griffon-0.1.9/griffon/services/core_queries.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/services/core_reports.py` & `griffon-0.1.9/griffon/services/core_reports.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon/static/default_griffonrc` & `griffon-0.1.9/griffon/static/default_griffonrc`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/griffon.egg-info/PKG-INFO` & `griffon-0.1.9/griffon.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: griffon
-Version: 0.1.8
+Version: 0.1.9
 Summary: Red Hat Product Security CLI
 Home-page: https://github.com/RedHatProductSecurity/griffon
 Author: James Fuller, Red Hat Product Security
 License: MIT
 Classifier: Topic :: Security
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

### Comparing `griffon-0.1.8/griffon.egg-info/SOURCES.txt` & `griffon-0.1.9/griffon.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/pyproject.toml` & `griffon-0.1.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/setup.py` & `griffon-0.1.9/setup.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/tests/test_cli.py` & `griffon-0.1.9/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/tests/test_process.py` & `griffon-0.1.9/tests/test_process.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/tests/test_queries.py` & `griffon-0.1.9/tests/test_queries.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/tests/test_reports.py` & `griffon-0.1.9/tests/test_reports.py`

 * *Files identical despite different names*

### Comparing `griffon-0.1.8/tests/test_unit.py` & `griffon-0.1.9/tests/test_unit.py`

 * *Files identical despite different names*

