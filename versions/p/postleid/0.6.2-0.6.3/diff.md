# Comparing `tmp/postleid-0.6.2.tar.gz` & `tmp/postleid-0.6.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "postleid-0.6.2.tar", last modified: Wed Apr  5 16:06:02 2023, max compression
+gzip compressed data, was "postleid-0.6.3.tar", last modified: Thu Apr  6 15:57:27 2023, max compression
```

## Comparing `postleid-0.6.2.tar` & `postleid-0.6.3.tar`

### file list

```diff
@@ -1,31 +1,32 @@
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/
--rw-r--r--   0 rainer    (1000) rainer    (1000)     1075 2023-04-05 15:58:25.000000 postleid-0.6.2/LICENSE
--rw-r--r--   0 rainer    (1000) rainer    (1000)     4323 2023-04-05 16:06:02.168146 postleid-0.6.2/PKG-INFO
--rw-r--r--   0 rainer    (1000) rainer    (1000)     1786 2023-04-05 16:02:03.000000 postleid-0.6.2/README.md
--rw-r--r--   0 rainer    (1000) rainer    (1000)     1625 2023-04-05 15:58:25.000000 postleid-0.6.2/pyproject.toml
--rw-r--r--   0 rainer    (1000) rainer    (1000)       38 2023-04-05 16:06:02.168146 postleid-0.6.2/setup.cfg
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid/
--rw-r--r--   0 rainer    (1000) rainer    (1000)      580 2023-04-05 15:58:25.000000 postleid-0.6.2/src/postleid/__init__.py
--rwxr-xr-x   0 rainer    (1000) rainer    (1000)     7796 2023-04-05 15:58:25.000000 postleid-0.6.2/src/postleid/__main__.py
--rw-r--r--   0 rainer    (1000) rainer    (1000)     4921 2023-04-05 15:58:25.000000 postleid-0.6.2/src/postleid/commons.py
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid/data/
--rw-r--r--   0 rainer    (1000) rainer    (1000)     1487 2023-04-05 15:58:25.000000 postleid-0.6.2/src/postleid/data/country_names_by_cc.yaml
--rw-r--r--   0 rainer    (1000) rainer    (1000)     9074 2023-04-05 15:58:25.000000 postleid-0.6.2/src/postleid/data/postal_code_rules_by_cc.yaml
--rw-r--r--   0 rainer    (1000) rainer    (1000)     7557 2023-04-05 16:00:51.000000 postleid-0.6.2/src/postleid/fix_excel_files.py
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid/locale/
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid/locale/de/
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid/locale/de/LC_MESSAGES/
--rw-r--r--   0 rainer    (1000) rainer    (1000)     3749 2023-04-05 15:58:26.000000 postleid-0.6.2/src/postleid/locale/de/LC_MESSAGES/argparse.mo
--rw-r--r--   0 rainer    (1000) rainer    (1000)     1192 2023-04-05 15:58:26.000000 postleid-0.6.2/src/postleid/presets.py
--rw-r--r--   0 rainer    (1000) rainer    (1000)    13925 2023-04-05 15:58:26.000000 postleid-0.6.2/src/postleid/rule_checks.py
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/src/postleid.egg-info/
--rw-r--r--   0 rainer    (1000) rainer    (1000)     4323 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/PKG-INFO
--rw-r--r--   0 rainer    (1000) rainer    (1000)      593 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/SOURCES.txt
--rw-r--r--   0 rainer    (1000) rainer    (1000)        1 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/dependency_links.txt
--rw-r--r--   0 rainer    (1000) rainer    (1000)       52 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/entry_points.txt
--rw-r--r--   0 rainer    (1000) rainer    (1000)       54 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/requires.txt
--rw-r--r--   0 rainer    (1000) rainer    (1000)        9 2023-04-05 16:06:02.000000 postleid-0.6.2/src/postleid.egg-info/top_level.txt
-drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-05 16:06:02.168146 postleid-0.6.2/tests/
--rw-r--r--   0 rainer    (1000) rainer    (1000)    13336 2023-04-05 15:58:26.000000 postleid-0.6.2/tests/test_commons.py
--rw-r--r--   0 rainer    (1000) rainer    (1000)     3630 2023-04-05 15:58:26.000000 postleid-0.6.2/tests/test_rule_checks.py
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     1075 2023-04-05 15:58:25.000000 postleid-0.6.3/LICENSE
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     2906 2023-04-06 15:57:27.876777 postleid-0.6.3/PKG-INFO
+-rw-r--r--   0 rainer    (1000) rainer    (1000)      270 2023-04-06 15:51:50.000000 postleid-0.6.3/README.md
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     1716 2023-04-06 15:52:37.000000 postleid-0.6.3/pyproject.toml
+-rw-r--r--   0 rainer    (1000) rainer    (1000)       38 2023-04-06 15:57:27.876777 postleid-0.6.3/setup.cfg
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)      580 2023-04-05 18:53:34.000000 postleid-0.6.3/src/postleid/__init__.py
+-rwxr-xr-x   0 rainer    (1000) rainer    (1000)     7090 2023-04-06 08:55:53.000000 postleid-0.6.3/src/postleid/__main__.py
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     5605 2023-04-06 08:25:49.000000 postleid-0.6.3/src/postleid/commons.py
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid/data/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     1487 2023-04-05 15:58:25.000000 postleid-0.6.3/src/postleid/data/country_names_by_cc.yaml
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     1476 2023-04-06 06:34:58.000000 postleid-0.6.3/src/postleid/data/default_user_settings.yaml
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     9074 2023-04-05 15:58:25.000000 postleid-0.6.3/src/postleid/data/postal_code_rules_by_cc.yaml
+-rw-r--r--   0 rainer    (1000) rainer    (1000)    10379 2023-04-06 08:40:47.000000 postleid-0.6.3/src/postleid/fix_excel_files.py
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid/locale/
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid/locale/de/
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid/locale/de/LC_MESSAGES/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     3749 2023-04-05 15:58:26.000000 postleid-0.6.3/src/postleid/locale/de/LC_MESSAGES/argparse.mo
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     1194 2023-04-06 08:11:50.000000 postleid-0.6.3/src/postleid/presets.py
+-rw-r--r--   0 rainer    (1000) rainer    (1000)    13925 2023-04-05 15:58:26.000000 postleid-0.6.3/src/postleid/rule_checks.py
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/src/postleid.egg-info/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     2906 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/PKG-INFO
+-rw-r--r--   0 rainer    (1000) rainer    (1000)      638 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/SOURCES.txt
+-rw-r--r--   0 rainer    (1000) rainer    (1000)        1 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/dependency_links.txt
+-rw-r--r--   0 rainer    (1000) rainer    (1000)       52 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/entry_points.txt
+-rw-r--r--   0 rainer    (1000) rainer    (1000)       54 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/requires.txt
+-rw-r--r--   0 rainer    (1000) rainer    (1000)        9 2023-04-06 15:57:27.000000 postleid-0.6.3/src/postleid.egg-info/top_level.txt
+drwxr-xr-x   0 rainer    (1000) rainer    (1000)        0 2023-04-06 15:57:27.876777 postleid-0.6.3/tests/
+-rw-r--r--   0 rainer    (1000) rainer    (1000)    13336 2023-04-05 15:58:26.000000 postleid-0.6.3/tests/test_commons.py
+-rw-r--r--   0 rainer    (1000) rainer    (1000)     3630 2023-04-05 15:58:26.000000 postleid-0.6.3/tests/test_rule_checks.py
```

### Comparing `postleid-0.6.2/LICENSE` & `postleid-0.6.3/LICENSE`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/pyproject.toml` & `postleid-0.6.3/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -36,15 +36,16 @@
   "pandas==2.0.0",
   "PyYAML>=6.0",
   "xlrd>=2.0.1",
 ]
 
 [project.urls]
 "Homepage" = "https://codeberg.org/blackstream-x/postleid"
-"Documentation" = "https://codeberg.org/blackstream-x/postleid"
+"Changelog" = "https://codeberg.org/blackstream-x/postleid/src/branch/main/CHANGELOG.md"
+"Documentation" = "https://blackstream-x.codeberg.page/postleid/"
 "Repository" = "https://codeberg.org/blackstream-x/postleid.git"
 "Bug Tracker" = "https://codeberg.org/blackstream-x/postleid/issues"
 
 [project.scripts]
 postleid = "postleid.__main__:main"
 
 [tool.setuptools.dynamic]
```

### Comparing `postleid-0.6.2/src/postleid/__init__.py` & `postleid-0.6.3/src/postleid/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,11 +17,11 @@
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the LICENSE file for more details.
 
 """
 
 
-__version__ = "0.6.2"
+__version__ = "0.6.3"
 
 
 # vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
```

### Comparing `postleid-0.6.2/src/postleid/__main__.py` & `postleid-0.6.3/src/postleid/__main__.py`

 * *Files 10% similar despite different names*

```diff
@@ -22,48 +22,43 @@
 """
 
 
 import argparse
 import gettext
 import logging
 import pathlib
+import shutil
 import sys
 
 from typing import List, Optional
 
-import pandas
-
 # local imports
 from postleid import __version__
 from postleid import commons
 from postleid import fix_excel_files
 from postleid import presets
 
 
 # Absolute script path
 SCRIPT_PATH = pathlib.Path(sys.argv[0]).resolve()
 
-# Return codes
-RETURNCODE_OK = 0
-RETURNCODE_ERROR = 1
-
 
 def list_supported_countries() -> int:
     """List supported countries and exit with the matching returncode"""
     try:
         country_names = commons.load_country_names_from_file()
     except OSError as error:
         commons.LogWrapper.error(f"{error}")
-        return RETURNCODE_ERROR
+        return commons.RETURNCODE_ERROR
     #
     try:
         rules = commons.load_rules_from_file()
     except OSError as error:
         commons.LogWrapper.error(f"{error}")
-        return RETURNCODE_ERROR
+        return commons.RETURNCODE_ERROR
     #
     without_rules: List[str] = []
     commons.LogWrapper.info("Supported countries:", commons.separator_line())
     for iso_cc, names in country_names.items():
         line = f"[{iso_cc}] {' / '.join(names)}"
         if iso_cc in rules:
             print(line)
@@ -88,15 +83,15 @@
         commons.LogWrapper.debug(
             commons.separator_line(),
             "Countries with rules but missing cleartext name(s):",
             commons.separator_line(),
             *without_cleartext,
         )
     #
-    return RETURNCODE_OK
+    return commons.RETURNCODE_OK
 
 
 def _parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
     """Parse command line arguments using argparse
     and return the arguments namespace.
 
     :param args: a list of command line arguments,
@@ -118,14 +113,15 @@
     # ------------------------------------------------------------------
     main_parser = argparse.ArgumentParser(
         prog="postleid",
         description="Postleitzahlen in Excel-Dateien korrigieren",
     )
     main_parser.set_defaults(
         loglevel=logging.INFO,
+        settings_file=pathlib.Path(presets.DEFAULT_USER_SETTINGS_FILE_NAME),
     )
     main_parser.add_argument(
         "--version",
         action="version",
         version=f"%(prog)s {__version__}",
         help="Version ausgeben und beenden",
     )
@@ -147,22 +143,14 @@
         "--quiet",
         action="store_const",
         const=logging.WARNING,
         dest="loglevel",
         help="nur Warnungen und Fehler ausgeben (Loglevel WARNING)",
     )
     main_parser.add_argument(
-        "-g",
-        "--guess-1000s",
-        action="store_true",
-        help="Postleitzahlen unter 1000 mit 1000 multiplizieren"
-        " (Achtung, für PLZs aus Bahrain liefert diese Option"
-        " falsche Ergebnisse!)",
-    )
-    main_parser.add_argument(
         "-l",
         "--list-supported-countries",
         action="store_true",
         help="Unterstützte Länder anzeigen"
         " (der Dateiname muss in diesem Fall zwar auch angegeben werden,"
         " wird jedoch ignoriert)",
     )
@@ -171,14 +159,22 @@
         "--output-file",
         metavar="AUSGABEDATEI",
         type=pathlib.Path,
         help="die Ausgabedatei (Standardwert: Name der Original-Exceldatei"
         f" mit vorangestelltem {presets.DEFAULT_FIXED_FILE_PREFIX!r})",
     )
     main_parser.add_argument(
+        "-s",
+        "--settings-file",
+        metavar="EINSTELLUNGSDATEI",
+        type=pathlib.Path,
+        help="die Datei mit Benutzereinstellungen"
+        " (Standardwert: %(default)s im aktuellen Verzeichnis)",
+    )
+    main_parser.add_argument(
         "excel_file",
         metavar="EXCELDATEI",
         type=pathlib.Path,
         help="die Original-Exceldatei",
     )
     return main_parser.parse_args(args)
 
@@ -189,68 +185,47 @@
     """
     arguments = _parse_args(args)
     commons.LogWrapper(arguments.loglevel)
     if arguments.list_supported_countries:
         return list_supported_countries()
     #
     source_path = arguments.excel_file.resolve()
-    commons.LogWrapper.info(f"Lade Datei {source_path} …")
-    dataframe = pandas.read_excel(source_path)
-    data_fixer = fix_excel_files.DataFixer(
-        dataframe, guess_1000s=arguments.guess_1000s
-    )
-    statistics = data_fixer.fix_all_zip_codes()
-    everything_is_fine, data_changed = commons.evaluate_results(statistics)
-    commons.LogWrapper.info(commons.separator_line())
-    if data_changed:
-        if everything_is_fine:
-            try:
-                data_fixer.sort_rows()
-            except NotImplementedError:
-                commons.LogWrapper.info(
-                    "Die Daten werden noch nicht nach Postleitzahlen"
-                    " sortiert.",
-                    "Das muss in Excel/LibreOffice Calc/… durchgeführt"
-                    " werden.",
-                )
-            #
-        else:
-            commons.LogWrapper.warning(
-                "Da die Orignaldaten nicht fehlerfrei waren,"
-                " wurden sie nicht nach Land und Postleitzahl sortiert."
-            )
-        #
-        target_path = arguments.output_file
-        if target_path:
-            target_path = target_path.resolve()
-        else:
-            target_path = (
-                source_path.parent
-                / f"{presets.DEFAULT_FIXED_FILE_PREFIX}{source_path.name}"
-            )
-        #
-        commons.LogWrapper.info(f"Schreibe Ausgabedatei {target_path} …")
-        try:
-            data_fixer.save(target_path)
-        except OSError as error:
-            commons.LogWrapper.error(str(error))
-            return RETURNCODE_ERROR
-        #
+    target_path = arguments.output_file
+    if target_path:
+        target_path = target_path.resolve()
     else:
-        if everything_is_fine:
-            no_errors = "keine Fehler"
-        else:
-            no_errors = "keine automatisiert behebbaren Fehler"
-        #
+        target_path = (
+            source_path.parent
+            / f"{presets.DEFAULT_FIXED_FILE_PREFIX}{source_path.name}"
+        )
+    #
+    if not arguments.settings_file.exists():
+        default_settings_path = commons.build_data_file_path(
+            "default_user_settings.yaml"
+        )
         commons.LogWrapper.info(
-            "Es wird keine Ausgabedatei geschrieben,",
-            f"weil die Daten {no_errors} enthalten.",
+            f"Einstellungsdatei {arguments.settings_file}"
+            " noch nicht vorhanden",
+            f" → erzeuge eine neue aus {default_settings_path} …",
         )
+        shutil.copy2(default_settings_path, arguments.settings_file)
+        commons.LogWrapper.info("… ok")
     #
-    return RETURNCODE_OK
+    commons.LogWrapper.info(
+        f"Lade Einstellungen aus {arguments.settings_file} …"
+    )
+    loaded_settings = commons.load_yaml_from_path(arguments.settings_file)
+    user_settings = commons.UserSettings(**loaded_settings)
+    commons.LogWrapper.info("… ok")
+    commons.LogWrapper.info(commons.separator_line())
+    return fix_excel_files.process_file(
+        source_path,
+        target_path,
+        user_settings=user_settings,
+    )
 
 
 if __name__ == "__main__":
     sys.exit(main())
 
 
 # vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
```

### Comparing `postleid-0.6.2/src/postleid/commons.py` & `postleid-0.6.3/src/postleid/commons.py`

 * *Files 12% similar despite different names*

```diff
@@ -18,22 +18,22 @@
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the LICENSE file for more details.
 
 """
 
 
 import bisect
+import dataclasses
 import logging
 import pathlib
-import sys
 import textwrap
 
 from collections import Counter
 
-from typing import Any, List, Tuple
+from typing import Any, List, Tuple, Union
 
 import yaml
 
 # local imports
 from postleid import presets
 
 
@@ -44,17 +44,14 @@
 S_WRONG_FORMAT = "(✘) falsches Format"
 S_WRONG_DATA_TYPE = "(✘) falscher Datentyp"
 S_OUT_OF_RANGE = "(✘) außerhalb des Bereichs"
 
 STATES_OK = (S_UNCHANGED, S_FIXED)
 STATES_ERROR = (S_WRONG_DATA_TYPE, S_WRONG_FORMAT, S_OUT_OF_RANGE)
 
-# Absolute script path
-SCRIPT_PATH = pathlib.Path(sys.argv[0]).resolve()
-
 # Return codes
 RETURNCODE_OK = 0
 RETURNCODE_ERROR = 1
 
 
 class LogWrapper:
 
@@ -100,14 +97,29 @@
 
     @classmethod
     def warning(cls, *messages: str) -> None:
         """Log with WARNING level"""
         cls.log_formatted(logging.WARNING, *messages)
 
 
+@dataclasses.dataclass
+class UserSettings:
+
+    """Container object for keeping user settings"""
+
+    default_country_code: str = presets.DEFAULT_CC
+    guess_1000s: bool = presets.GUESS_1000S
+    country_headings: Union[
+        List[str], Tuple[str, ...]
+    ] = presets.COUNTRY_HEADINGS
+    postal_code_heading_parts: Union[
+        List[str], Tuple[str, ...]
+    ] = presets.POSTAL_CODE_HEADING_PARTS
+
+
 def separator_line(
     element: str = "–", width: int = presets.LOG_MESSAGE_MAX_WIDTH
 ) -> str:
     """Return a separator line"""
     return element * width
 
 
@@ -147,23 +159,32 @@
                 f" {f'{keyword}:':<{max_kw_width + 1}} {frequency}",
             )
         #
     #
     return everything_is_fine, data_changed
 
 
-def load_yaml_data_file(file_name: str) -> Any:
-    """Load a YAML file from the provided file
+def build_data_file_path(file_name: Union[str, pathlib.Path]) -> pathlib.Path:
+    """Build a data file path from the provided file name"""
+    return pathlib.Path(__file__).resolve().parent / "data" / file_name
+
+
+def load_yaml_from_path(path: pathlib.Path) -> Any:
+    """Load a YAML file from the provided path
+    and return its deserialized contents
+    """
+    return yaml.safe_load(path.read_text(encoding="utf-8"))
+
+
+def load_yaml_data_file(file_name: Union[str, pathlib.Path]) -> Any:
+    """Load YAML from the provided file
     located in the data subdirectory
     and return its deserialized contents
     """
-    settings_path = (
-        pathlib.Path(__file__).resolve().parent / "data" / file_name
-    )
-    return yaml.safe_load(settings_path.read_text(encoding="utf-8"))
+    return load_yaml_from_path(build_data_file_path(file_name))
 
 
 def load_rules_from_file() -> Any:
     """Load the postal code rules by country code
     from the appropriate file
     """
     return load_yaml_data_file("postal_code_rules_by_cc.yaml")
```

### Comparing `postleid-0.6.2/src/postleid/data/country_names_by_cc.yaml` & `postleid-0.6.3/src/postleid/data/country_names_by_cc.yaml`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/src/postleid/data/postal_code_rules_by_cc.yaml` & `postleid-0.6.3/src/postleid/data/postal_code_rules_by_cc.yaml`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/src/postleid/locale/de/LC_MESSAGES/argparse.mo` & `postleid-0.6.3/src/postleid/locale/de/LC_MESSAGES/argparse.mo`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/src/postleid/presets.py` & `postleid-0.6.3/src/postleid/presets.py`

 * *Files 23% similar despite different names*

```diff
@@ -17,31 +17,35 @@
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the LICENSE file for more details.
 
 """
 
 
-# Heading parts in lower case indicating a zip code column
-ZIP_CODE_HEADING_PARTS = ("plz", "postleit", "zip code")
-
-# Headings in lower case indicating a country column
-COUNTRY_HEADINGS = ("land", "staat", "country")
-
 # Prefix for the fixed file name
 DEFAULT_FIXED_FILE_PREFIX = "fixed-"
 
-# Append 000 to integer values between 1 and 99?
-# (in a future release, this controls whether
-#  the --guess-1000s or the --no-guess-1000s flag
-#  will be provided as options)
-DEFAULT_GUESS_1000S_SHORTENED = False
-
-# Default country code
-DEFAULT_CC = "de"
+# User settings default file name
+DEFAULT_USER_SETTINGS_FILE_NAME = "postleid-settings.yaml"
 
 # Logging options
 LOG_MESSAGE_FORMAT = "%(levelname)-8s | %(message)s"
 LOG_MESSAGE_MAX_WIDTH = 68
 
+#
+# Defaults for the commons.UserSettings class
+#
+
+# Default country code
+DEFAULT_CC = "de"
+
+# Multiply values by 1000 if lower than 1000?
+GUESS_1000S = False
+
+# Headings in lower case indicating a country column
+COUNTRY_HEADINGS = ("Land", "Staat", "Country")
+
+# Heading parts in lower case indicating a postal code column
+POSTAL_CODE_HEADING_PARTS = ("PLZ", "Postleit", "Zip Code")
+
 
 # vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
```

### Comparing `postleid-0.6.2/src/postleid/rule_checks.py` & `postleid-0.6.3/src/postleid/rule_checks.py`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/src/postleid.egg-info/SOURCES.txt` & `postleid-0.6.3/src/postleid.egg-info/SOURCES.txt`

 * *Files 26% similar despite different names*

```diff
@@ -10,11 +10,12 @@
 src/postleid.egg-info/PKG-INFO
 src/postleid.egg-info/SOURCES.txt
 src/postleid.egg-info/dependency_links.txt
 src/postleid.egg-info/entry_points.txt
 src/postleid.egg-info/requires.txt
 src/postleid.egg-info/top_level.txt
 src/postleid/data/country_names_by_cc.yaml
+src/postleid/data/default_user_settings.yaml
 src/postleid/data/postal_code_rules_by_cc.yaml
 src/postleid/locale/de/LC_MESSAGES/argparse.mo
 tests/test_commons.py
 tests/test_rule_checks.py
```

### Comparing `postleid-0.6.2/tests/test_commons.py` & `postleid-0.6.3/tests/test_commons.py`

 * *Files identical despite different names*

### Comparing `postleid-0.6.2/tests/test_rule_checks.py` & `postleid-0.6.3/tests/test_rule_checks.py`

 * *Files identical despite different names*

