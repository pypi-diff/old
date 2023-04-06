# Comparing `tmp/rasa-model-report-1.3.2.tar.gz` & `tmp/rasa-model-report-1.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rasa-model-report-1.3.2.tar", last modified: Mon Feb 27 00:37:59 2023, max compression
+gzip compressed data, was "rasa-model-report-1.3.3.tar", last modified: Thu Apr  6 16:03:09 2023, max compression
```

## Comparing `rasa-model-report-1.3.2.tar` & `rasa-model-report-1.3.3.tar`

### file list

```diff
@@ -1,39 +1,40 @@
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.223918 rasa-model-report-1.3.2/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    11357 2022-11-12 01:01:09.000000 rasa-model-report-1.3.2/LICENSE
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8416 2023-02-27 00:37:59.223918 rasa-model-report-1.3.2/PKG-INFO
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8022 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/README.md
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.203918 rasa-model-report-1.3.2/rasa_model_report/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/rasa_model_report/__init__.py
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.215918 rasa-model-report-1.3.2/rasa_model_report/controllers/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/__init__.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1157 2023-02-24 17:23:06.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1380 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/csv_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     7804 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/e2e_coverage_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    12049 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/json_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    22934 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/markdown_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     4616 2023-02-24 17:23:06.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/model_report.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     9043 2023-02-24 17:23:06.000000 rasa-model-report-1.3.2/rasa_model_report/controllers/nlu_controller.py
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.219918 rasa-model-report-1.3.2/rasa_model_report/helpers/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/rasa_model_report/helpers/__init__.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      246 2023-02-24 17:23:06.000000 rasa-model-report-1.3.2/rasa_model_report/helpers/type_aliases.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     5324 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/rasa_model_report/helpers/utils.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     2741 2023-02-21 20:14:38.000000 rasa-model-report-1.3.2/rasa_model_report/main.py
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.207918 rasa-model-report-1.3.2/rasa_model_report.egg-info/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8416 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/PKG-INFO
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1093 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/SOURCES.txt
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        1 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/dependency_links.txt
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       66 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/entry_points.txt
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       35 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/requires.txt
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       18 2023-02-27 00:37:59.000000 rasa-model-report-1.3.2/rasa_model_report.egg-info/top_level.txt
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      518 2023-02-27 00:37:59.223918 rasa-model-report-1.3.2/setup.cfg
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      983 2023-02-27 00:35:46.000000 rasa-model-report-1.3.2/setup.py
-drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-02-27 00:37:59.223918 rasa-model-report-1.3.2/tests/
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      467 2023-02-26 23:52:26.000000 rasa-model-report-1.3.2/tests/test_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1611 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/tests/test_csv_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     5900 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/tests/test_e2e_coverage_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     9033 2023-02-26 03:56:52.000000 rasa-model-report-1.3.2/tests/test_json_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1294 2023-02-24 16:02:52.000000 rasa-model-report-1.3.2/tests/test_main.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    13586 2023-02-21 20:14:38.000000 rasa-model-report-1.3.2/tests/test_markdown_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     2383 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/tests/test_model_report.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8143 2022-12-31 15:38:47.000000 rasa-model-report-1.3.2/tests/test_nlu_controller.py
--rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     6339 2023-02-27 00:24:02.000000 rasa-model-report-1.3.2/tests/test_utils.py
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.029863 rasa-model-report-1.3.3/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    11357 2022-11-12 01:01:09.000000 rasa-model-report-1.3.3/LICENSE
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8523 2023-04-06 16:03:09.029863 rasa-model-report-1.3.3/PKG-INFO
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8129 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/README.md
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.009863 rasa-model-report-1.3.3/rasa_model_report/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/rasa_model_report/__init__.py
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.021864 rasa-model-report-1.3.3/rasa_model_report/controllers/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/__init__.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1157 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1380 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/csv_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     7804 2023-02-27 00:24:02.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/e2e_coverage_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    12196 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/json_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    23220 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/markdown_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     4616 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/model_report.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     9116 2023-04-06 16:01:46.000000 rasa-model-report-1.3.3/rasa_model_report/controllers/nlu_controller.py
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.025864 rasa-model-report-1.3.3/rasa_model_report/helpers/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        0 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/rasa_model_report/helpers/__init__.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      204 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/rasa_model_report/helpers/constants.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      247 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/rasa_model_report/helpers/type_aliases.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     5885 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/rasa_model_report/helpers/utils.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     3241 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/rasa_model_report/main.py
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.013863 rasa-model-report-1.3.3/rasa_model_report.egg-info/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8523 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/PKG-INFO
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1132 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/SOURCES.txt
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)        1 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/dependency_links.txt
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       66 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/entry_points.txt
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       35 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/requires.txt
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)       18 2023-04-06 16:03:08.000000 rasa-model-report-1.3.3/rasa_model_report.egg-info/top_level.txt
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      518 2023-04-06 16:03:09.029863 rasa-model-report-1.3.3/setup.cfg
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      983 2023-04-06 16:02:52.000000 rasa-model-report-1.3.3/setup.py
+drwxrwxr-x   0 bruno.justo  (1001) bruno.justo  (1001)        0 2023-04-06 16:03:09.029863 rasa-model-report-1.3.3/tests/
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)      467 2023-02-26 23:52:26.000000 rasa-model-report-1.3.3/tests/test_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1611 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/tests/test_csv_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     5900 2023-02-27 00:24:02.000000 rasa-model-report-1.3.3/tests/test_e2e_coverage_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     9082 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/tests/test_json_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     1294 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/tests/test_main.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)    13462 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/tests/test_markdown_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     2383 2023-04-06 15:47:57.000000 rasa-model-report-1.3.3/tests/test_model_report.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     8143 2022-12-31 15:38:47.000000 rasa-model-report-1.3.3/tests/test_nlu_controller.py
+-rw-rw-r--   0 bruno.justo  (1001) bruno.justo  (1001)     7652 2023-03-24 23:06:15.000000 rasa-model-report-1.3.3/tests/test_utils.py
```

### Comparing `rasa-model-report-1.3.2/LICENSE` & `rasa-model-report-1.3.3/LICENSE`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/PKG-INFO` & `rasa-model-report-1.3.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rasa-model-report
-Version: 1.3.2
+Version: 1.3.3
 Summary: Simple open-source Rasa command-line add-on that generates training model health reports for your projects.
 Home-page: https://github.com/brunohjs/rasa-model-report
 Author: Bruno Justo
 Author-email: brunohjs@gmail.com
 License: Apache 2.0
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
@@ -101,22 +101,23 @@
 There are parameters that can be used. Available options are below:
 
 ```
 --actions-path TEXT     Actions path. (default: actions/ inside Rasa project
                         path)
 --disable-nlu           Disable processing NLU sentences. NLU section will
                         not be generated in the report. Required Rasa API.
-                        (default: false)
 -h, --help              Show this help message.
 --model-link TEXT       Model download link. It's only displayed in the
                         report to model download.
---no-images             Generate model report without images. (default:
-                        false)
+--no-images             Generate model report without images.
 --output-path TEXT      Report output path. (default: ./)
 -p, --path TEXT         Rasa project path. (default: ./)
+--precision INTEGER     Grade precision. Used to change precision of the
+                        model report overview grades. Can vary between 0 and
+                        5 (default: 1)
 --project-name TEXT     Rasa project name. It's only displayed in the
                         report. (default: My project)
 --project-version TEXT  Project version. It's only displayed in the report
                         for project documentation.
 --rasa-api TEXT         Rasa API URL. Is needed to create NLU section of
                         report. (default: http://localhost:5005)
 --rasa-version TEXT     Rasa version. It's only displayed in the report for
```

### Comparing `rasa-model-report-1.3.2/README.md` & `rasa-model-report-1.3.3/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -89,22 +89,23 @@
 There are parameters that can be used. Available options are below:
 
 ```
 --actions-path TEXT     Actions path. (default: actions/ inside Rasa project
                         path)
 --disable-nlu           Disable processing NLU sentences. NLU section will
                         not be generated in the report. Required Rasa API.
-                        (default: false)
 -h, --help              Show this help message.
 --model-link TEXT       Model download link. It's only displayed in the
                         report to model download.
---no-images             Generate model report without images. (default:
-                        false)
+--no-images             Generate model report without images.
 --output-path TEXT      Report output path. (default: ./)
 -p, --path TEXT         Rasa project path. (default: ./)
+--precision INTEGER     Grade precision. Used to change precision of the
+                        model report overview grades. Can vary between 0 and
+                        5 (default: 1)
 --project-name TEXT     Rasa project name. It's only displayed in the
                         report. (default: My project)
 --project-version TEXT  Project version. It's only displayed in the report
                         for project documentation.
 --rasa-api TEXT         Rasa API URL. Is needed to create NLU section of
                         report. (default: http://localhost:5005)
 --rasa-version TEXT     Rasa version. It's only displayed in the report for
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/controller.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/csv_controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/csv_controller.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/e2e_coverage_controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/e2e_coverage_controller.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/json_controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/json_controller.py`

 * *Files 2% similar despite different names*

```diff
@@ -212,31 +212,35 @@
         """
         logging.info(f"{self.overview_report_path} file successfully saved.")
         file = open(self.overview_report_path, "w", encoding="utf-8")
         json.dump(self._overview, file, indent=4)
         file.write("\n")
         file.close()
 
+    @staticmethod
+    def weight_function(x: float) -> float:
+        return 1 - x**3
+
     def _calculate_overall(self) -> None:
         """
         Calculate report overall.
         """
         weights = {
             "intent": 2,
             "entity": 1,
             "core": 1,
-            "nlu": 3,
-            "e2e_coverage": 3
+            "nlu": 8,
+            "e2e_coverage": 8
         }
         overview_sum = sum(
-            self._overview[item] * w for item, w in weights.items()
+            self._overview[item] * self.weight_function(self._overview[item]) for item in weights
             if isinstance(self._overview[item], (int, float)) and self._overview[item] >= 0
         )
         weight_sum = sum(
-            w for item, w in weights.items()
+            self.weight_function(self._overview[item]) for item in weights
             if isinstance(self._overview[item], (int, float)) and self._overview[item] >= 0
         )
         overview_rate = overview_sum / weight_sum if weight_sum else 0
         self._overview.update({
             "overall": overview_rate
         })
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/markdown_controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/markdown_controller.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 from typing import Union
 
 from rasa_model_report.controllers.controller import Controller
 from rasa_model_report.controllers.csv_controller import CsvController
 from rasa_model_report.controllers.e2e_coverage_controller import E2ECoverageController
 from rasa_model_report.controllers.json_controller import JsonController
 from rasa_model_report.controllers.nlu_controller import NluController
+from rasa_model_report.helpers import constants
 from rasa_model_report.helpers import type_aliases
 from rasa_model_report.helpers import utils
 
 
 class MarkdownController(Controller):
     """
     Controller responsible for markdown files.
@@ -40,24 +41,25 @@
 
         self.result: str = ""
         self.title: str = "# Model health report"
         self.rasa_version: str = rasa_version
         self.output_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.md")
         self.readme_path: str = "README.md"
         self.model_link: str = kwargs.get("model_link")
-        self.no_images: bool = kwargs.get("no_images", False)
+        self.no_images: bool = kwargs.get("no_images", constants.NO_IMAGES)
+        self.precision: int = kwargs.get("precision", constants.GRADE_PRECISION)
         self.json: JsonController = JsonController(rasa_path, output_path, project_name, project_version)
         self.csv: CsvController = CsvController(rasa_path, output_path, project_name, project_version)
         self.nlu: NluController = NluController(
             rasa_path,
             output_path,
             project_name,
             project_version,
-            url=kwargs.get("rasa_api_url"),
-            disable_nlu=kwargs.get("disable_nlu")
+            url=kwargs.get("rasa_api_url", constants.RASA_API_URL),
+            disable_nlu=kwargs.get("disable_nlu", constants.DISABLE_NLU)
         )
         self.e2e_coverage: E2ECoverageController = E2ECoverageController(
             rasa_path,
             output_path,
             kwargs.get("actions_path"),
             project_name,
             project_version
@@ -178,20 +180,20 @@
             data.append(["Model", f"[Download]({self.model_link})"])
         text += "|" + "|".join([item[0] for item in data]) + "|\n"
         text += "|" + "|".join([":-:" for i in range(len(data))]) + "|\n"
         text += "|" + "|".join([f"<span {style}>{item[1]}</span>" for item in data]) + "|\n\n"
         style = "style='font-size:20px'"
         text += f"|Intent|Entity|NLU|Core|E2E Coverage|<span {style}>General</span>|\n"
         text += "|:-:|:-:|:-:|:-:|:-:|:-:|\n"
-        text += f"|{utils.change_scale(overview['intent'], 10)}\
-            |{utils.change_scale(overview['entity'], 10)}\
-            |{utils.change_scale(overview['nlu'], 10)}\
-            |{utils.change_scale(overview['core'], 10)}\
-            |{utils.change_scale(overview['e2e_coverage'], 10)}\
-            |<span {style}>**{utils.change_scale(overview['overall'], 10)}**</span>|\n"
+        text += f"|{utils.change_scale(overview['intent'], 10, self.precision)}\
+            |{utils.change_scale(overview['entity'], 10, self.precision)}\
+            |{utils.change_scale(overview['nlu'], 10, self.precision)}\
+            |{utils.change_scale(overview['core'], 10, self.precision)}\
+            |{utils.change_scale(overview['e2e_coverage'], 10, self.precision)}\
+            |<span {style}>**{utils.change_scale(overview['overall'], 10, self.precision)}**</span>|\n"
         text += f"{utils.get_color(overview['intent'])}\
             |{utils.get_color(overview['entity'])}\
             |{utils.get_color(overview['nlu'])}\
             |{utils.get_color(overview['core'])}\
             |{utils.get_color(overview['e2e_coverage'])}\
             |<span {style}>{utils.get_color(overview['overall'])}</span>|"
         return text
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/model_report.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/model_report.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/rasa_model_report/controllers/nlu_controller.py` & `rasa-model-report-1.3.3/rasa_model_report/controllers/nlu_controller.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 from typing import List
 from typing import Optional
 from typing import Union
 
 import requests.exceptions
 
 from rasa_model_report.controllers.controller import Controller
+from rasa_model_report.helpers import constants
 from rasa_model_report.helpers import type_aliases
 from rasa_model_report.helpers import utils
 
 
 class NluController(Controller):
     """
     Controller responsible for Rasa NLU.
@@ -37,15 +38,15 @@
         :param url: Rasa API URL (default: "http://localhost:5005")
         """
         super().__init__(rasa_path, output_path, project_name, project_version)
         self._data: List[type_aliases.nlu_payload] = []
         self._problem_sentences: List[type_aliases.nlu_payload] = []
         self._general_grade: Optional[float] = None
         self._connected: bool = False
-        self._disable_nlu: bool = kwargs.get("disable_nlu")
+        self._disable_nlu: bool = kwargs.get("disable_nlu", constants.DISABLE_NLU)
         self.url: str = url
 
         if not self._disable_nlu and self.health_check_rasa_api():
             self._load_nlu()
             self._generate_data()
             self._load_problem_sentences()
             self._calculate_general_grade()
@@ -81,15 +82,15 @@
         :return: A dictionary that contains the sentences separeted by intent.
         """
         logging.info("Looking for Rasa's NLU files.")
         files = glob.glob(f"{self.nlu_path}/**/*.yml") + glob.glob(f"{self.nlu_path}/*.yml")
         nlu = {}
         for filename in files:
             file = utils.load_yaml_file(filename)
-            if file.get("nlu"):
+            if file and file.get("nlu"):
                 data = {i["intent"]: i["examples"] for i in file["nlu"] if i.get("intent")}
                 if data:
                     logging.info(f"Found sentences in {filename} file.")
                     for intent, text in data.items():
                         data[intent] = self._extract_sentences(text)
                         logging.info(f" - Intent {intent}: {len(data[intent])} sentence(s).")
                     nlu.update(data)
@@ -104,15 +105,15 @@
         """
         logging.info("Formatting extracted data.")
         data = []
         index = 1
         for intent, examples in self._data.items():
             progress = index / len(self._data) * 100
             index += 1
-            logging.info(f" - Analyzing NLU of the {intent} intent ({progress:<5.1f}%).")
+            logging.info(f" - ({progress:<5.1f}%) analyzing NLU intent: {intent}")
             for text in examples:
                 text = self.remove_entities_from_text(text)
                 nlu_requested = self.request_nlu(text)
                 predicted_intent = self.select_intent(nlu_requested)
                 item = {
                     "intent": intent,
                     "text": text,
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report/helpers/utils.py` & `rasa-model-report-1.3.3/rasa_model_report/helpers/utils.py`

 * *Files 13% similar despite different names*

```diff
@@ -7,14 +7,16 @@
 from typing import Union
 
 import requests.exceptions
 from requests.adapters import HTTPAdapter
 from requests.adapters import Retry
 from yaml import safe_load
 
+from rasa_model_report.helpers import constants
+
 
 def format_date() -> str:
     """
     Format the current date to the format DD/MM/YY hh:mm:ss.
 
     :return: Date string.
     """
@@ -60,24 +62,36 @@
         elif value >= 0.4:
             return "🟠"
         elif value >= 0.001:
             return "🔴"
     return "❌"
 
 
-def change_scale(value: float, scale: int = 1) -> str:
+def change_scale(value: float, scale: int = 1, precision: int = 1) -> str:
     """
     Change the value scale and rounds it to display in string format.
 
     :param value: Value that will be changed to scale and rounds it.
     :param scale: Scale that will be applied.
-    :return: Value on the new scale.
+    :param precision: Value precision.
+    :return: Value on the new scale and precision.
     """
-    if isinstance(value, (float, int)):
-        return f"{int(value * scale)}"
+    precision = precision if isinstance(precision, int) and 5 >= precision >= 0 else constants.GRADE_PRECISION
+    if (
+        isinstance(value, (float, int)) and
+        isinstance(scale, (float, int)) and
+        scale != 0
+    ):
+        new_value = value * scale
+        if new_value >= 1 and new_value % int(new_value) == 0:
+            return str(int(new_value))
+        elif re.search(r"\.0$", f"{new_value:.{precision}f}"):
+            return "0"
+        else:
+            return f"{new_value:.{precision}f}"
     return value
 
 
 def get_project_name(path: Optional[str] = None) -> str:
     """
     Returns the project folder's name.
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report/main.py` & `rasa-model-report-1.3.3/rasa_model_report/main.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,29 +1,30 @@
 import logging
 
 import click
 
 from rasa_model_report.controllers.model_report import ModelReport
+from rasa_model_report.helpers import constants
 
 logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
 
 
 @click.command()
 @click.option(
     "--actions-path",
     required=False,
     help="Actions path. (default: actions/ inside Rasa project path)"
 )
 @click.option(
     "--disable-nlu",
     is_flag=True,
     required=False,
-    default=False,
+    default=constants.DISABLE_NLU,
     help="Disable processing NLU sentences. NLU section will not be generated "
-    "in the report. Required Rasa API. (default: false)"
+    "in the report. Required Rasa API."
 )
 @click.help_option(
     "--help",
     "-h",
     help="Show this help message."
 )
 @click.option(
@@ -32,58 +33,66 @@
     required=False,
     help="Model download link. It's only displayed in the report to model download."
 )
 @click.option(
     "--no-images",
     is_flag=True,
     required=False,
-    default=False,
-    help="Generate model report without images. (default: false)"
+    default=constants.NO_IMAGES,
+    help="Generate model report without images."
 )
 @click.option(
     "--output-path",
     type=str,
     required=False,
-    default="./",
-    help="Report output path. (default: ./)"
+    default=constants.OUTPUT_PATH,
+    help=f"Report output path. (default: {constants.OUTPUT_PATH})"
 )
 @click.option(
     "--path",
     "-p",
     type=str,
     required=False,
-    default="./",
-    help="Rasa project path. (default: ./)"
+    default=constants.RASA_PATH,
+    help=f"Rasa project path. (default: {constants.RASA_PATH})"
+)
+@click.option(
+    "--precision",
+    type=int,
+    required=False,
+    default=constants.GRADE_PRECISION,
+    help="Grade precision. Used to change precision of the model report overview grades. "
+    f"Can vary between 0 and 5 (default: {constants.GRADE_PRECISION})"
 )
 @click.option(
     "--project-name",
     type=str,
     required=False,
-    default="My Project",
-    help="Rasa project name. It's only displayed in the report. (default: My project)"
+    default=constants.PROJECT_NAME,
+    help=f"Rasa project name. It's only displayed in the report. (default: {constants.PROJECT_NAME})"
 )
 @click.option(
     "--project-version",
     type=str,
     required=False,
-    default=None,
+    default=constants.PROJECT_VERSION,
     help="Project version. It's only displayed in the report for project documentation."
 )
 @click.option(
     "--rasa-api",
     type=str,
     required=False,
-    default="http://localhost:5005",
-    help="Rasa API URL. Is needed to create NLU section of report. (default: http://localhost:5005)"
+    default=constants.RASA_API_URL,
+    help=f"Rasa API URL. Is needed to create NLU section of report. (default: {constants.RASA_API_URL})"
 )
 @click.option(
     "--rasa-version",
     type=str,
     required=False,
-    default=None,
+    default=constants.RASA_VERSION,
     help="Rasa version. It's only displayed in the report for project documentation."
 )
 @click.version_option(
     None,
     "--version",
     "-v",
     message="v%(version)s",
@@ -91,14 +100,15 @@
 )
 def main(
     actions_path,
     disable_nlu,
     model_link,
     no_images,
     output_path, path,
+    precision,
     project_name,
     project_version,
     rasa_api,
     rasa_version
 ):
     """
     Simple add-on that generates training model health reports for your Rasa projects. 📈🔍🧾🤖🧠
@@ -109,10 +119,11 @@
         project_name,
         rasa_version,
         project_version,
         disable_nlu=disable_nlu,
         rasa_api_url=rasa_api,
         model_link=model_link,
         actions_path=actions_path,
-        no_images=no_images
+        no_images=no_images,
+        precision=precision
     )
     return report
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report.egg-info/PKG-INFO` & `rasa-model-report-1.3.3/rasa_model_report.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rasa-model-report
-Version: 1.3.2
+Version: 1.3.3
 Summary: Simple open-source Rasa command-line add-on that generates training model health reports for your projects.
 Home-page: https://github.com/brunohjs/rasa-model-report
 Author: Bruno Justo
 Author-email: brunohjs@gmail.com
 License: Apache 2.0
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
@@ -101,22 +101,23 @@
 There are parameters that can be used. Available options are below:
 
 ```
 --actions-path TEXT     Actions path. (default: actions/ inside Rasa project
                         path)
 --disable-nlu           Disable processing NLU sentences. NLU section will
                         not be generated in the report. Required Rasa API.
-                        (default: false)
 -h, --help              Show this help message.
 --model-link TEXT       Model download link. It's only displayed in the
                         report to model download.
---no-images             Generate model report without images. (default:
-                        false)
+--no-images             Generate model report without images.
 --output-path TEXT      Report output path. (default: ./)
 -p, --path TEXT         Rasa project path. (default: ./)
+--precision INTEGER     Grade precision. Used to change precision of the
+                        model report overview grades. Can vary between 0 and
+                        5 (default: 1)
 --project-name TEXT     Rasa project name. It's only displayed in the
                         report. (default: My project)
 --project-version TEXT  Project version. It's only displayed in the report
                         for project documentation.
 --rasa-api TEXT         Rasa API URL. Is needed to create NLU section of
                         report. (default: http://localhost:5005)
 --rasa-version TEXT     Rasa version. It's only displayed in the report for
```

### Comparing `rasa-model-report-1.3.2/rasa_model_report.egg-info/SOURCES.txt` & `rasa-model-report-1.3.3/rasa_model_report.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 rasa_model_report/controllers/csv_controller.py
 rasa_model_report/controllers/e2e_coverage_controller.py
 rasa_model_report/controllers/json_controller.py
 rasa_model_report/controllers/markdown_controller.py
 rasa_model_report/controllers/model_report.py
 rasa_model_report/controllers/nlu_controller.py
 rasa_model_report/helpers/__init__.py
+rasa_model_report/helpers/constants.py
 rasa_model_report/helpers/type_aliases.py
 rasa_model_report/helpers/utils.py
 tests/test_controller.py
 tests/test_csv_controller.py
 tests/test_e2e_coverage_controller.py
 tests/test_json_controller.py
 tests/test_main.py
```

### Comparing `rasa-model-report-1.3.2/setup.cfg` & `rasa-model-report-1.3.3/setup.cfg`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/setup.py` & `rasa-model-report-1.3.3/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text(encoding="utf-8")
 
 setup(
     name="rasa-model-report",
-    version="1.3.2",
+    version="1.3.3",
     author="Bruno Justo",
     author_email="brunohjs@gmail.com",
     license="Apache 2.0",
     description="Simple open-source Rasa command-line add-on that "
                 "generates training model health reports for your projects.",
     long_description=long_description,
     long_description_content_type="text/markdown",
```

### Comparing `rasa-model-report-1.3.2/tests/test_csv_controller.py` & `rasa-model-report-1.3.3/tests/test_csv_controller.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/tests/test_e2e_coverage_controller.py` & `rasa-model-report-1.3.3/tests/test_e2e_coverage_controller.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/tests/test_json_controller.py` & `rasa-model-report-1.3.3/tests/test_json_controller.py`

 * *Files 5% similar despite different names*

```diff
@@ -80,20 +80,20 @@
     json_controller = pytest.json_controller
     json_controller._load_overview()
     overview = json_controller.overview
     assert isinstance(overview, dict)
     assert isinstance(overview.get("project"), str)
     assert isinstance(overview.get("version"), str)
     assert isinstance(overview.get("updated_at"), str)
-    assert isinstance(overview.get("intent"), float)
-    assert isinstance(overview.get("entity"), float)
-    assert isinstance(overview.get("core"), float)
-    assert isinstance(overview.get("nlu"), float) or overview.get("nlu") is None
-    assert isinstance(overview.get("e2e_coverage"), float) or overview.get("e2e_coverage") is None
-    assert isinstance(overview.get("overall"), float)
+    assert isinstance(overview.get("intent"), (float, int))
+    assert isinstance(overview.get("entity"), (float, int))
+    assert isinstance(overview.get("core"), (float, int))
+    assert isinstance(overview.get("nlu"), (float, int)) or overview.get("nlu") is None
+    assert isinstance(overview.get("e2e_coverage"), (float, int)) or overview.get("e2e_coverage") is None
+    assert isinstance(overview.get("overall"), (float, int))
     assert isinstance(overview.get("created_at"), str)
 
 
 def test_load_overview_if_exists():
     json_controller = pytest.json_controller
     json_controller._load_overview()
     json_controller.save_overview()
@@ -106,15 +106,15 @@
     json_controller.save_overview()
     assert os.path.isfile(json_controller.overview_report_path)
 
 
 def test_calculate_overall():
     json_controller = pytest.json_controller
     json_controller._calculate_overall()
-    assert isinstance(json_controller.overview.get("overall"), float)
+    assert isinstance(json_controller.overview.get("overall"), (float, int))
 
 
 def test_update_overview():
     json_controller = pytest.json_controller
     random_number = random.randint(0, 100)
     json_controller.update_overview({
         "nlu": random_number
```

### Comparing `rasa-model-report-1.3.2/tests/test_main.py` & `rasa-model-report-1.3.3/tests/test_main.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/tests/test_markdown_controller.py` & `rasa-model-report-1.3.3/tests/test_markdown_controller.py`

 * *Files 1% similar despite different names*

```diff
@@ -82,14 +82,15 @@
     assert isinstance(text, str)
     assert markdown_controller.nlu.is_connected() is True
     assert "#nlu" in text
 
 
 def test_build_summary_without_nlu_section():
     markdown_controller = pytest.markdown_controller
+    markdown_controller.nlu._connected = False
     text = markdown_controller.build_summary()
     assert isinstance(text, str)
     assert markdown_controller.nlu.is_connected() is False
     assert "#nlu" not in text
 
 
 def test_build_summary_without_config_section():
@@ -253,16 +254,15 @@
     text = markdown_controller.build_nlu_table()
     assert isinstance(text, str)
     assert os.path.isfile(f"{markdown_controller.results_path}/nlu_report.csv")
 
 
 def test_build_nlu_table_if_len_less_than_2():
     markdown_controller = pytest.markdown_controller
-    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
-    markdown_controller.json = json_controller
+    markdown_controller.nlu._data = {}
     text = markdown_controller.build_nlu_table()
     assert isinstance(text, str)
     assert "No example sentences were found in this template" in text
     assert not os.path.isfile(f"{markdown_controller.results_path}/nlu_report.csv")
 
 
 def test_build_nlu_errors_table():
@@ -276,16 +276,15 @@
     })
     text = markdown_controller.build_nlu_errors_table()
     assert isinstance(text, str)
 
 
 def test_build_nlu_errors_table_if_len_less_than_2():
     markdown_controller = pytest.markdown_controller
-    json_controller = JsonController("invalid/path", "./", "test-project", "0.0.0")
-    markdown_controller.json = json_controller
+    markdown_controller.nlu._problem_sentences = {}
     text = markdown_controller.build_nlu_errors_table()
     assert isinstance(text, str)
     assert "There are no sentences that were not understood in this model" in text
 
 
 def test_build_config_report():
     markdown_controller = pytest.markdown_controller
```

### Comparing `rasa-model-report-1.3.2/tests/test_model_report.py` & `rasa-model-report-1.3.3/tests/test_model_report.py`

 * *Files identical despite different names*

### Comparing `rasa-model-report-1.3.2/tests/test_nlu_controller.py` & `rasa-model-report-1.3.3/tests/test_nlu_controller.py`

 * *Files identical despite different names*

