# Comparing `tmp/cpggen-0.7.0.tar.gz` & `tmp/cpggen-0.7.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cpggen-0.7.0.tar", max compression
+gzip compressed data, was "cpggen-0.7.1.tar", max compression
```

## Comparing `cpggen-0.7.0.tar` & `cpggen-0.7.1.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0    11357 2023-04-06 10:38:38.834535 cpggen-0.7.0/LICENSE
--rw-r--r--   0        0        0     4409 2023-04-06 10:38:38.834535 cpggen-0.7.0/README.md
--rw-r--r--   0        0        0        0 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/__init__.py
--rw-r--r--   0        0        0     8264 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/cli.py
--rw-r--r--   0        0        0    16008 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/executor.py
--rw-r--r--   0        0        0      732 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/logger.py
--rw-r--r--   0        0        0     9581 2023-04-06 10:38:38.834535 cpggen-0.7.0/cpggen/utils.py
--rw-r--r--   0        0        0     1245 2023-04-06 10:38:38.834535 cpggen-0.7.0/pyproject.toml
--rw-r--r--   0        0        0     5737 1970-01-01 00:00:00.000000 cpggen-0.7.0/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-06 12:19:09.022715 cpggen-0.7.1/LICENSE
+-rw-r--r--   0        0        0     4409 2023-04-06 12:19:09.022715 cpggen-0.7.1/README.md
+-rw-r--r--   0        0        0        0 2023-04-06 12:19:09.022715 cpggen-0.7.1/cpggen/__init__.py
+-rw-r--r--   0        0        0     8264 2023-04-06 12:19:09.022715 cpggen-0.7.1/cpggen/cli.py
+-rw-r--r--   0        0        0    16565 2023-04-06 12:19:09.022715 cpggen-0.7.1/cpggen/executor.py
+-rw-r--r--   0        0        0      731 2023-04-06 12:19:09.022715 cpggen-0.7.1/cpggen/logger.py
+-rw-r--r--   0        0        0     9581 2023-04-06 12:19:09.022715 cpggen-0.7.1/cpggen/utils.py
+-rw-r--r--   0        0        0     1245 2023-04-06 12:19:09.022715 cpggen-0.7.1/pyproject.toml
+-rw-r--r--   0        0        0     5737 1970-01-01 00:00:00.000000 cpggen-0.7.1/PKG-INFO
```

### Comparing `cpggen-0.7.0/LICENSE` & `cpggen-0.7.1/LICENSE`

 * *Files identical despite different names*

### Comparing `cpggen-0.7.0/README.md` & `cpggen-0.7.1/README.md`

 * *Files identical despite different names*

### Comparing `cpggen-0.7.0/cpggen/cli.py` & `cpggen-0.7.1/cpggen/cli.py`

 * *Files identical despite different names*

### Comparing `cpggen-0.7.0/cpggen/executor.py` & `cpggen-0.7.1/cpggen/executor.py`

 * *Files 2% similar despite different names*

```diff
@@ -359,17 +359,27 @@
                             cpg_out = cpg_out.replace("/github/workspace/", "")
                             sbom_out = sbom_out.replace("/github/workspace/", "")
                             amodule = amodule.replace("/github/workspace/", "")
                         language = tool_lang.split("-")[0]
                         # Override the language for jvm
                         if language in ("jar", "scala"):
                             language = "java"
+                        app_base_name = os.path.basename(amodule)
+                        # Let's improve the name for github action
+                        if app_base_name == "workspace" and os.getenv(
+                            "GITHUB_REPOSITORY"
+                        ):
+                            app_base_name = os.getenv("GITHUB_REPOSITORY").split("/")[
+                                -1
+                            ]
                         json.dump(
                             {
                                 "src": amodule,
+                                "group": app_base_name,
+                                "app": f"{app_base_name}-{language}",
                                 "cpg": cpg_out,
                                 "sbom": sbom_out,
                                 "language": language,
                                 "cpg_frontend_invocation": " ".join(cmd_list_with_args),
                                 "sbom_invocation": " ".join(sbom_cmd_list_with_args),
                             },
                             mfp,
```

### Comparing `cpggen-0.7.0/cpggen/logger.py` & `cpggen-0.7.1/cpggen/logger.py`

 * *Files 13% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 
 custom_theme = Theme({"info": "cyan", "warning": "purple4", "danger": "bold red"})
 console = Console(
     log_time=False,
     log_path=False,
     theme=custom_theme,
     width=280,
-    color_system="auto",
+    color_system="256",
     record=True,
 )
 
 logging.basicConfig(
     level=logging.INFO,
     format="%(message)s",
     datefmt="[%X]",
```

### Comparing `cpggen-0.7.0/cpggen/utils.py` & `cpggen-0.7.1/cpggen/utils.py`

 * *Files identical despite different names*

### Comparing `cpggen-0.7.0/pyproject.toml` & `cpggen-0.7.1/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "cpggen"
-version = "0.7.0"
+version = "0.7.1"
 description = "Generate CPG for multiple languages for use with joern"
 authors = ["Team AppThreat <cloud@appthreat.com>"]
 license = "Apache-2.0"
 readme = "README.md"
 packages = [{include = "cpggen"}]
 homepage = "https://github.com/AppThreat/cpggen"
 repository = "https://github.com/AppThreat/cpggen"
```

### Comparing `cpggen-0.7.0/PKG-INFO` & `cpggen-0.7.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cpggen
-Version: 0.7.0
+Version: 0.7.1
 Summary: Generate CPG for multiple languages for use with joern
 Home-page: https://github.com/AppThreat/cpggen
 License: Apache-2.0
 Keywords: joern,code analysis,static analysis,cpg,code property graph
 Author: Team AppThreat
 Author-email: cloud@appthreat.com
 Requires-Python: >=3.8,<3.12
```

