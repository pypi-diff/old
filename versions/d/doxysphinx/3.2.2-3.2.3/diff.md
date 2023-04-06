# Comparing `tmp/doxysphinx-3.2.2.tar.gz` & `tmp/doxysphinx-3.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "doxysphinx-3.2.2.tar", max compression
+gzip compressed data, was "doxysphinx-3.2.3.tar", max compression
```

## Comparing `doxysphinx-3.2.2.tar` & `doxysphinx-3.2.3.tar`

### file list

```diff
@@ -1,23 +1,23 @@
--rw-r--r--   0        0        0     1068 2023-04-06 08:03:27.314633 doxysphinx-3.2.2/LICENSE
--rw-r--r--   0        0        0     1078 2023-04-06 08:03:27.314633 doxysphinx-3.2.2/LICENSE.md
--rw-r--r--   0        0        0     2602 2023-04-06 08:03:27.314633 doxysphinx-3.2.2/README.md
--rw-r--r--   0        0        0      926 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/__init__.py
--rw-r--r--   0        0        0      608 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/__main__.py
--rw-r--r--   0        0        0     7300 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/cli.py
--rw-r--r--   0        0        0    12357 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/doxygen.py
--rw-r--r--   0        0        0    19836 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/html_parser.py
--rw-r--r--   0        0        0     7740 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/process.py
--rw-r--r--   0        0        0     5859 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/resources/custom.scss
--rw-r--r--   0        0        0        0 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/resources/toc_template.html.j2
--rw-r--r--   0        0        0     9683 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/resources.py
--rw-r--r--   0        0        0     2943 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/sphinx.py
--rw-r--r--   0        0        0    10875 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/toc.py
--rw-r--r--   0        0        0      527 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/__init__.py
--rw-r--r--   0        0        0     2282 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/contexts.py
--rw-r--r--   0        0        0     1156 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/exceptions.py
--rw-r--r--   0        0        0     4967 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/files.py
--rw-r--r--   0        0        0     1757 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/iterators.py
--rw-r--r--   0        0        0     1431 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/utils/pathlib_fix.py
--rw-r--r--   0        0        0    12216 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/doxysphinx/writer.py
--rw-r--r--   0        0        0     4630 2023-04-06 08:03:27.330633 doxysphinx-3.2.2/pyproject.toml
--rw-r--r--   0        0        0     4122 1970-01-01 00:00:00.000000 doxysphinx-3.2.2/PKG-INFO
+-rw-r--r--   0        0        0     1068 2023-04-06 14:29:01.979708 doxysphinx-3.2.3/LICENSE
+-rw-r--r--   0        0        0     1078 2023-04-06 14:29:01.979708 doxysphinx-3.2.3/LICENSE.md
+-rw-r--r--   0        0        0     2602 2023-04-06 14:29:01.979708 doxysphinx-3.2.3/README.md
+-rw-r--r--   0        0        0      926 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/__init__.py
+-rw-r--r--   0        0        0      608 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/__main__.py
+-rw-r--r--   0        0        0     7409 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/cli.py
+-rw-r--r--   0        0        0    12640 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/doxygen.py
+-rw-r--r--   0        0        0    19836 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/html_parser.py
+-rw-r--r--   0        0        0     7740 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/process.py
+-rw-r--r--   0        0        0     5859 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/resources/custom.scss
+-rw-r--r--   0        0        0        0 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/resources/toc_template.html.j2
+-rw-r--r--   0        0        0     9683 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/resources.py
+-rw-r--r--   0        0        0     2943 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/sphinx.py
+-rw-r--r--   0        0        0    10875 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/toc.py
+-rw-r--r--   0        0        0      527 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/__init__.py
+-rw-r--r--   0        0        0     2282 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/contexts.py
+-rw-r--r--   0        0        0     1156 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/exceptions.py
+-rw-r--r--   0        0        0     4967 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/files.py
+-rw-r--r--   0        0        0     1757 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/iterators.py
+-rw-r--r--   0        0        0     1431 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/utils/pathlib_fix.py
+-rw-r--r--   0        0        0    12216 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/doxysphinx/writer.py
+-rw-r--r--   0        0        0     4630 2023-04-06 14:29:01.995709 doxysphinx-3.2.3/pyproject.toml
+-rw-r--r--   0        0        0     4122 1970-01-01 00:00:00.000000 doxysphinx-3.2.3/PKG-INFO
```

### Comparing `doxysphinx-3.2.2/LICENSE` & `doxysphinx-3.2.3/LICENSE`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/LICENSE.md` & `doxysphinx-3.2.3/LICENSE.md`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/README.md` & `doxysphinx-3.2.3/README.md`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/__init__.py` & `doxysphinx-3.2.3/doxysphinx/__init__.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/__main__.py` & `doxysphinx-3.2.3/doxysphinx/__main__.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/cli.py` & `doxysphinx-3.2.3/doxysphinx/cli.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 #  C O P Y R I G H T
 # -------------------------------------------------------------------------------------
 #  Copyright (c) 2023 by Robert Bosch GmbH. All rights reserved.
 #
 #  Author(s):
 #  - Markus Braun, :em engineering methods AG (contracted by Robert Bosch GmbH)
 #  - Celina Adelhardt, :em engineering methods AG (contracted by Robert Bosch GmbH)
+#  - Gergely Meszaros, Stream HPC B.V. (contracted by Advanced Micro Devices Inc.)
 # =====================================================================================
 
 # noqa: D301
 """
 Entry module for the doxysphinx cli.
 
 Defines click main command (:func:`cli`) and subcommands (:func:`build`), (:func:`clean`)
@@ -157,15 +158,15 @@
             yield _get_outdir_via_doxyfile(i, sphinx_source, doxy_context)
 
 
 def _get_outdir_via_doxyfile(doxyfile: Path, sphinx_source: Path, doxy_context: DoxygenContext) -> Path:
     config = read_doxyconfig(doxyfile, doxy_context.doxygen_exe, doxy_context.doxygen_cwd)
 
     validator = DoxygenSettingsValidator()
-    if not validator.validate(config, sphinx_source):
+    if not validator.validate(config, sphinx_source, doxy_context.doxygen_cwd):
         if any(item for item in validator.validation_errors if not item.startswith("Hint:")):
             message = validator.validation_msg
             raise click.UsageError(
                 f'The doxygen settings defined in "{doxyfile}"'
                 f"do not match the mandatory settings necessary for doxysphinx:\n"
                 f"{message}"
             )
```

### Comparing `doxysphinx-3.2.2/doxysphinx/doxygen.py` & `doxysphinx-3.2.3/doxysphinx/doxygen.py`

 * *Files 4% similar despite different names*

```diff
@@ -166,52 +166,54 @@
     validation_errors: List[str] = []
     """List of the validation errors including the doxyflag with its used and the correct value."""
     absolute_out: Path
     """Absolute path of the output directory."""
     validation_msg = ""
     """Validation errors merged in one string."""
 
-    def validate(self, config: ConfigDict, sphinx_source_dir: Path) -> bool:
+    def validate(self, config: ConfigDict, sphinx_source_dir: Path, doxygen_cwd: Path) -> bool:
         """Validate the doxygen configuration regarding the output directory, mandatory and optional settings.
 
         :param config: the imported doxyfile.
         :param sphinx_source_dir: the sphinx directory (necessary for output directory validation).
+        :param doxygen_cwd the directory for doxygen, paths from doxyfile are relative from here
         :return: False, if there is a deviation to the defined mandatory or optional settings.
         """
         if "WARNINGS" in config:
             self.validation_errors.extend(config["WARNINGS"])
 
-        out_dir_validated = self._validate_doxygen_out_dirs(config, sphinx_source_dir)
+        out_dir_validated = self._validate_doxygen_out_dirs(config, sphinx_source_dir, doxygen_cwd)
         recommended_settings_validated = self._validate_doxygen_recommended_settings(config)
         optional_settings_validated = self._validate_doxygen_optional_settings(config)
         if out_dir_validated and recommended_settings_validated and optional_settings_validated:
             self.validation_msg = "All doxygen settings are set correctly."
             return True
         else:
             for error in self.validation_errors:
                 self.validation_msg += error + "\n"
             return False
 
-    def _validate_doxygen_out_dirs(self, config: ConfigDict, sphinx_source_dir: Path) -> bool:
+    def _validate_doxygen_out_dirs(self, config: ConfigDict, sphinx_source_dir: Path, doxygen_cwd: Path) -> bool:
         """
         Validate the output directory given from doxyfile and set the required values in mandatory settings.
 
         :param out_dir: output directory value in doxyfile.
         :param sphinx_source_dir: sphinx docs source-directory.
+        :param doxygen_cwd the directory for doxygen, paths from doxyfile are relative from here
         :return: True if doxygen output directory is located inside the sphinx docs root,
         False if not and doxysphinx should exit.
         """
-        out = Path(str(config["OUTPUT_DIRECTORY"])) / "html"  # config["HTML_OUTPUT"]
+        out = Path(doxygen_cwd) / str(config["OUTPUT_DIRECTORY"]) / "html"  # config["HTML_OUTPUT"]
         self.absolute_out = path_resolve(out)
         stringified_out = str(out) if out.is_absolute() else f'"{out}" (resolved to "{self.absolute_out}")'
 
         self.mandatory_settings["OUTPUT_DIRECTORY"] = str(config["OUTPUT_DIRECTORY"])
 
         if path_is_relative_to(out, sphinx_source_dir):
-            self.optional_settings["GENERATE_TAGFILE"] = str(out) + "/tagfile.xml"
+            self.optional_settings["GENERATE_TAGFILE"] = os.path.relpath(out / "tagfile.xml", doxygen_cwd)
             return True
         else:
             self.optional_settings["GENERATE_TAGFILE"] = "docs/doxygen/demo/html/tagfile.xml"  # default value
             self.validation_errors.append(
                 f'The doxygen OUTPUT_DIR of "{stringified_out}" defined in the doxyfile'
                 f' is not in a sub-path of the sphinx source directory "{sphinx_source_dir}".'
             )
```

### Comparing `doxysphinx-3.2.2/doxysphinx/html_parser.py` & `doxysphinx-3.2.3/doxysphinx/html_parser.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/process.py` & `doxysphinx-3.2.3/doxysphinx/process.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/resources/custom.scss` & `doxysphinx-3.2.3/doxysphinx/resources/custom.scss`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/resources.py` & `doxysphinx-3.2.3/doxysphinx/resources.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/sphinx.py` & `doxysphinx-3.2.3/doxysphinx/sphinx.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/toc.py` & `doxysphinx-3.2.3/doxysphinx/toc.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/__init__.py` & `doxysphinx-3.2.3/doxysphinx/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/contexts.py` & `doxysphinx-3.2.3/doxysphinx/utils/contexts.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/exceptions.py` & `doxysphinx-3.2.3/doxysphinx/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/files.py` & `doxysphinx-3.2.3/doxysphinx/utils/files.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/iterators.py` & `doxysphinx-3.2.3/doxysphinx/utils/iterators.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/utils/pathlib_fix.py` & `doxysphinx-3.2.3/doxysphinx/utils/pathlib_fix.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/doxysphinx/writer.py` & `doxysphinx-3.2.3/doxysphinx/writer.py`

 * *Files identical despite different names*

### Comparing `doxysphinx-3.2.2/pyproject.toml` & `doxysphinx-3.2.3/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 ##
 ##  Author(s):
 ##  - Markus Braun, :em engineering methods AG (contracted by Robert Bosch GmbH)
 ## =====================================================================================
 
 [tool.poetry]
 name = "doxysphinx"
-version = "3.2.2"
+version = "3.2.3"
 description = "Integrates doxygen html documentation with sphinx."
 authors = [
     "Nirmal Sasidharan <nirmal.sasidharan@de.bosch.com>",
     "Markus Braun <markus.braun@em.ag>",
     "Aniket Salve <aniketdilip.salve@bosch.com>",
 ]
 maintainers = ["Nirmal Sasidharan <nirmal.sasidharan@de.bosch.com>"]
@@ -84,15 +84,15 @@
 sphinx-autoapi = "^2.0.0"
 
 [tool.poetry.scripts]
 doxysphinx = "doxysphinx.cli:cli"
 
 [tool.commitizen]
 name = "cz_conventional_commits"
-version = "3.2.2"
+version = "3.2.3"
 tag_format = "v$version"
 version_files = ["pyproject.toml:^version"]
 bump_message = """chore(release): release $current_version → $new_version by commitizen [skip-ci]
 
 Signed-off-by: github-actions <actions@github.com>
 """
```

### Comparing `doxysphinx-3.2.2/PKG-INFO` & `doxysphinx-3.2.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: doxysphinx
-Version: 3.2.2
+Version: 3.2.3
 Summary: Integrates doxygen html documentation with sphinx.
 Home-page: https://github.com/boschglobal/doxysphinx
 License: MIT
 Keywords: DaC,docs-as-code,doxygen,sphinx
 Author: Nirmal Sasidharan
 Author-email: nirmal.sasidharan@de.bosch.com
 Maintainer: Nirmal Sasidharan
```

