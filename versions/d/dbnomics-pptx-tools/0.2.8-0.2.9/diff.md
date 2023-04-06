# Comparing `tmp/dbnomics-pptx-tools-0.2.8.tar.gz` & `tmp/dbnomics-pptx-tools-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbnomics-pptx-tools-0.2.8.tar", last modified: Tue Mar  7 09:53:25 2023, max compression
+gzip compressed data, was "dbnomics-pptx-tools-0.2.9.tar", last modified: Thu Mar  9 15:44:40 2023, max compression
```

## Comparing `dbnomics-pptx-tools-0.2.8.tar` & `dbnomics-pptx-tools-0.2.9.tar`

### file list

```diff
@@ -1,32 +1,35 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.736374 dbnomics-pptx-tools-0.2.8/
--rw-r--r--   0 root         (0) root         (0)     4473 2023-03-07 09:53:25.736374 dbnomics-pptx-tools-0.2.8/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     3866 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/README.md
--rw-rw-rw-   0 root         (0) root         (0)     1560 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/pyproject.toml
--rw-rw-rw-   0 root         (0) root         (0)      322 2023-03-07 09:53:25.736374 dbnomics-pptx-tools-0.2.8/setup.cfg
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.732374 dbnomics-pptx-tools-0.2.8/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.732374 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1335 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cache.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.736374 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/
--rw-rw-rw-   0 root         (0) root         (0)     1967 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1846 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/chart_data.py
--rw-rw-rw-   0 root         (0) root         (0)     7559 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/data_labels.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.736374 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/
--rw-rw-rw-   0 root         (0) root         (0)     6185 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/app.py
--rw-rw-rw-   0 root         (0) root         (0)     1896 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/cli_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     1815 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/slide_expr.py
--rw-rw-rw-   0 root         (0) root         (0)      342 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/formatters.py
--rw-rw-rw-   0 root         (0) root         (0)     4914 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/metadata.py
--rw-rw-rw-   0 root         (0) root         (0)      713 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/module_utils.py
--rw-rw-rw-   0 root         (0) root         (0)    10590 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/pptx_copy.py
--rw-rw-rw-   0 root         (0) root         (0)     2180 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/repo.py
--rw-rw-rw-   0 root         (0) root         (0)     6632 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/slides.py
--rw-rw-rw-   0 root         (0) root         (0)    10751 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/tables.py
--rw-rw-rw-   0 root         (0) root         (0)      121 2023-03-07 09:42:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/xml_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-07 09:53:25.732374 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4473 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      927 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       66 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)      414 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       20 2023-03-07 09:53:25.000000 dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/
+-rw-r--r--   0 root         (0) root         (0)     4473 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     3866 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     1714 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/pyproject.toml
+-rw-rw-rw-   0 root         (0) root         (0)      365 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/setup.cfg
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.064689 dbnomics-pptx-tools-0.2.9/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.064689 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/
+-rw-rw-rw-   0 root         (0) root         (0)       55 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1321 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cache.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/
+-rw-rw-rw-   0 root         (0) root         (0)     2146 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1213 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/chart_data.py
+-rw-rw-rw-   0 root         (0) root         (0)     7737 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/data_labels.py
+-rw-rw-rw-   0 root         (0) root         (0)     1116 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/series.py
+-rw-rw-rw-   0 root         (0) root         (0)      814 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/
+-rw-rw-rw-   0 root         (0) root         (0)     6146 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/app.py
+-rw-rw-rw-   0 root         (0) root         (0)     1625 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/cli_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     1836 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/slide_expr.py
+-rw-rw-rw-   0 root         (0) root         (0)     5278 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/data_loader.py
+-rw-rw-rw-   0 root         (0) root         (0)      357 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/formatters.py
+-rw-rw-rw-   0 root         (0) root         (0)     5059 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/metadata.py
+-rw-rw-rw-   0 root         (0) root         (0)      738 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/module_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)    10328 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/pptx_copy.py
+-rw-rw-rw-   0 root         (0) root         (0)     2191 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/repo.py
+-rw-rw-rw-   0 root         (0) root         (0)     6632 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/slides.py
+-rw-rw-rw-   0 root         (0) root         (0)    11193 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/tables.py
+-rw-rw-rw-   0 root         (0) root         (0)      121 2023-03-09 15:44:01.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/xml_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-09 15:44:40.068688 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4473 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1047 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       66 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      437 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       20 2023-03-09 15:44:40.000000 dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/top_level.txt
```

### Comparing `dbnomics-pptx-tools-0.2.8/PKG-INFO` & `dbnomics-pptx-tools-0.2.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbnomics-pptx-tools
-Version: 0.2.8
+Version: 0.2.9
 Summary: DBnomics PowerPoint (pptx) tools
 Author-email: Christophe Benz <christophe.benz@nomics.world>
 Project-URL: Homepage, https://git.nomics.world/dbnomics/dbnomics-pptx-tools
 Project-URL: Bug Tracker, https://git.nomics.world/dbnomics/dbnomics-pptx-tools/-/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `dbnomics-pptx-tools-0.2.8/README.md` & `dbnomics-pptx-tools-0.2.9/README.md`

 * *Files identical despite different names*

### Comparing `dbnomics-pptx-tools-0.2.8/pyproject.toml` & `dbnomics-pptx-tools-0.2.9/pyproject.toml`

 * *Files 17% similar despite different names*

```diff
@@ -1,13 +1,11 @@
 [project]
 name = "dbnomics-pptx-tools"
-version = "0.2.8"
-authors = [
-  { name="Christophe Benz", email="christophe.benz@nomics.world" },
-]
+version = "0.2.9"
+authors = [{ name = "Christophe Benz", email = "christophe.benz@nomics.world" }]
 description = "DBnomics PowerPoint (pptx) tools"
 readme = "README.md"
 requires-python = ">=3.10"
 classifiers = [
   "Programming Language :: Python :: 3",
   "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
   "Operating System :: OS Independent",
@@ -21,14 +19,15 @@
   "parsy",
   "pydantic",
   "python-pptx",
   "python-slugify",
   "PyYAML",
   "tabulate",
   "typer[all]",
+  "webcolors",
 ]
 
 [project.optional-dependencies]
 dev = [
   "black",
   "flake8",
   "flake8-blind-except",
@@ -42,14 +41,15 @@
   "flake8-logging-format",
   "flake8-mutable",
   "flake8-print",
   "flake8-quotes",
   "ipykernel",
   "isort",
   "mypy",
+  "pandas-stubs",
   "types-python-slugify",
   "types-PyYAML",
   "types-tabulate",
 ]
 
 [project.scripts]
 dbnomics-pptx = "dbnomics_pptx_tools.cli.app:app"
@@ -61,12 +61,16 @@
 [tool.black]
 line-length = 120
 
 # From https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#isort
 [tool.isort]
 line_length = 120
 profile = "black"
-src_paths = ["dbnomics_pptx_tools"]
 
 [tool.mypy]
 packages = ["dbnomics_pptx_tools"]
+plugins = ["pydantic.mypy"]
 strict = true
+
+[[tool.mypy.overrides]]
+module = ["dbnomics", "isodate", "lxml.*", "parsy", "pptx.*", "webcolors"]
+ignore_missing_imports = true
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cache.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cache.py`

 * *Files 7% similar despite different names*

```diff
@@ -3,31 +3,29 @@
 
 import pandas as pd
 from pandas import DataFrame
 from slugify import slugify
 
 
 class SeriesCache:
-    def __init__(self, *, auto_create_dir=True, cache_dir: Path):
+    def __init__(self, *, auto_create_dir: bool = True, cache_dir: Path) -> None:
         self._auto_create_dir = auto_create_dir
         self._cache_dir = cache_dir
 
     def get(self, series_id: str) -> Optional[DataFrame]:
         file_path = self._get_series_json_file_path(series_id)
         if not file_path.is_file():
             return None
-        return pd.read_json(
-            file_path, convert_dates=["period"], dtype={"original_period": str}, orient="records"  # type: ignore
-        )
+        return pd.read_json(file_path, convert_dates=["period"], dtype={"original_period": str}, orient="records")
 
     def has(self, series_id: str) -> bool:
         file_path = self._get_series_json_file_path(series_id)
         return file_path.is_file()
 
-    def set(self, series_id: str, series_df: DataFrame):
+    def set(self, series_id: str, series_df: DataFrame) -> None:
         file_path = self._get_series_json_file_path(series_id)
         if self._auto_create_dir:
             file_path.parent.mkdir(parents=True, exist_ok=True)
         series_df.to_json(file_path, date_format="iso", indent=2, orient="records")
 
     def _get_series_json_file_name(self, series_id: str) -> str:
         return slugify(series_id) + ".json"
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/__init__.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -4,52 +4,53 @@
 from pptx.chart.axis import DateAxis
 from pptx.chart.chart import Chart
 from pptx.chart.data import CategoryChartData
 from pptx.shapes.graphfrm import GraphicFrame
 from pptx.shapes.shapetree import SlideShapes
 from pptx.slide import Slide
 
+from dbnomics_pptx_tools.charts.series import update_series
+from dbnomics_pptx_tools.data_loader import ShapeDataLoader
 from dbnomics_pptx_tools.metadata import ChartSpec
 from dbnomics_pptx_tools.pptx_copy import copy_shape_properties
 from dbnomics_pptx_tools.repo import SeriesRepo
 from dbnomics_pptx_tools.xml_utils import remove_element
 
-from .chart_data import build_category_chart_data, load_chart_df
+from .chart_data import build_category_chart_data
 from .data_labels import update_data_labels
 
-__all__ = ["update_chart"]
-
 logger = daiquiri.getLogger(__name__)
 
 
-def recreate_chart(chart_shape: GraphicFrame, *, chart_data: CategoryChartData, slide: Slide):
+def recreate_chart(chart_shape: GraphicFrame, *, chart_data: CategoryChartData, slide: Slide) -> Chart:
     chart = cast(Chart, chart_shape.chart)
     remove_element(chart_shape.element)
     new_chart_shape = cast(
         GraphicFrame,
         cast(SlideShapes, slide.shapes).add_chart(
             chart.chart_type, chart_shape.left, chart_shape.top, chart_shape.width, chart_shape.height, chart_data
         ),
     )
     copy_shape_properties(chart_shape, new_chart_shape)
     logger.debug("The chart was recreated")
     return cast(Chart, new_chart_shape.chart)
 
 
-def update_chart(chart_shape: GraphicFrame, *, chart_spec: ChartSpec, repo: SeriesRepo, slide: Slide):
+def update_chart(chart_shape: GraphicFrame, *, chart_spec: ChartSpec, repo: SeriesRepo, slide: Slide) -> None:
     chart = cast(Chart, chart_shape.chart)
     if not isinstance(chart.category_axis, DateAxis):
         raise NotImplementedError()
 
-    df = load_chart_df(chart_spec, repo=repo)
-    pivoted_df = df.pivot(index="period", columns="series_id", values="value")
+    chart_series_df = ShapeDataLoader(repo).load_shape_df(chart_spec)
+    pivoted_df = chart_series_df.pivot(index="period", columns="series_id", values="value")
 
     chart_data = build_category_chart_data(chart_spec, pivoted_df=pivoted_df)
 
     try:
         chart.replace_data(chart_data)
     except ValueError:
         chart = recreate_chart(chart_shape, chart_data=chart_data, slide=slide)
     else:
         logger.debug("Chart data was replaced")
 
     update_data_labels(chart, chart_spec=chart_spec, pivoted_df=pivoted_df)
+    update_series(chart, chart_spec=chart_spec)
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/charts/data_labels.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/charts/data_labels.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,24 +9,25 @@
 from pptx.chart.datalabel import DataLabel
 from pptx.chart.plot import _BasePlot
 from pptx.chart.point import Point
 from pptx.chart.series import _BaseCategorySeries
 from pptx.dml.line import LineFormat
 from pptx.oxml.ns import nsdecls
 
+from dbnomics_pptx_tools.charts.utils import iter_chart_series_with_spec
 from dbnomics_pptx_tools.metadata import ChartSpec, DataLabelPosition, DataLabelSpec
 from dbnomics_pptx_tools.pptx_copy import copy_color_format_properties, copy_font_properties
 from dbnomics_pptx_tools.xml_utils import remove_element
 
 logger = daiquiri.getLogger(__name__)
 
 
 @dataclass
 class DataLabelRenderData:
-    series: _BaseCategorySeries
+    chart_series: _BaseCategorySeries
     point: Point
     ratio: float
     new_ratio: float | None
 
     @property
     def ratio_distance(self) -> float | None:
         if self.new_ratio is None:
@@ -37,29 +38,31 @@
 def add_data_label_to_last_point_of_each_series(
     chart: Chart,
     *,
     chart_spec: ChartSpec,
     data_label_spec: DataLabelSpec,
     pivoted_df: DataFrame,
     points_by_series_name: dict[str, list[Point]],
-):
+) -> None:
     logger.debug("Adding a data label to the last point of each series of the chart...")
 
     render_data_list = compute_data_label_positions(
         chart, chart_spec=chart_spec, pivoted_df=pivoted_df, points_by_series_name=points_by_series_name
     )
 
     for render_data in render_data_list:
         apply_render_data_to_chart(render_data, chart=chart, data_label_spec=data_label_spec)
 
 
-def apply_render_data_to_chart(render_data: DataLabelRenderData, *, chart: Chart, data_label_spec: DataLabelSpec):
+def apply_render_data_to_chart(
+    render_data: DataLabelRenderData, *, chart: Chart, data_label_spec: DataLabelSpec
+) -> None:
     logger.debug(
         "Adding data label to chart for series %r (using number format %r)...",
-        render_data.series.name,
+        render_data.chart_series.name,
         data_label_spec.number_format,
     )
     value_axis_font = chart.value_axis.tick_labels.font
 
     data_label = cast(DataLabel, render_data.point.data_label)
     copy_font_properties(value_axis_font, data_label.font)
     dLbl_element = data_label._get_or_add_dLbl()
@@ -68,21 +71,21 @@
     if numFmt_element is None:
         numFmt_element = etree.fromstring(f"""<c:numFmt {nsdecls("c")} />""")
         dLbl_element.append(numFmt_element)
     numFmt_element.attrib["formatCode"] = data_label_spec.number_format
     numFmt_element.attrib["sourceLinked"] = "0"
     dLbl_element.find("./{*}showVal").attrib["val"] = "1"
     line = LineFormat(data_label._dLbl.get_or_add_spPr())
-    copy_color_format_properties(render_data.series.format.line.color, line.color)
+    copy_color_format_properties(render_data.chart_series.format.line.color, line.color)
 
     ratio_distance = render_data.ratio_distance
     if ratio_distance is not None:
         logger.debug(
             "Moving the data label of the series %r because if is too close to the previous one",
-            render_data.series.name,
+            render_data.chart_series.name,
         )
         layout_element = etree.fromstring(
             f"""
                 <c:layout {nsdecls("c")}>
                     <c:manualLayout>
                         <c:x val="0"/>
                         <c:y val="{-ratio_distance}"/>
@@ -95,26 +98,30 @@
 
 def compute_data_label_positions(
     chart: Chart, *, chart_spec: ChartSpec, pivoted_df: DataFrame, points_by_series_name: dict[str, list[Point]]
 ) -> list[DataLabelRenderData]:
     logger.debug("Computing data label positions...")
     render_data_list: list[DataLabelRenderData] = []
 
-    for chart_series in cast(Iterable[_BaseCategorySeries], chart.series):
-        series_id = chart_spec.find_series_id_by_name(chart_series.name)
+    for chart_series, series_spec in iter_chart_series_with_spec(chart, chart_spec):
+        series_id = series_spec.id
+        series_name = series_spec.name
+
         series = pivoted_df.reset_index()[series_id]
-        last_value_index = series.last_valid_index()
+        last_value_index = cast(int, series.last_valid_index())
         if last_value_index is None:
-            logger.warning("The series %r (%r) only has NA values, skipping", chart_series.name, series_id)
+            logger.warning("The series named %r with ID %r has only NA values, skipping", series_name, series_id)
             continue
 
         last_value = series[last_value_index]
         ratio = compute_data_label_ratio(last_value, chart=chart, pivoted_df=pivoted_df)
-        last_point = points_by_series_name[chart_series.name][last_value_index]
-        render_data_list.append(DataLabelRenderData(series=chart_series, point=last_point, ratio=ratio, new_ratio=None))
+        last_point = points_by_series_name[series_name][last_value_index]
+        render_data_list.append(
+            DataLabelRenderData(chart_series=chart_series, point=last_point, ratio=ratio, new_ratio=None)
+        )
 
     render_data_list = sorted(render_data_list, key=lambda render_data: render_data.ratio)
     return list(iter_spaced_data_labels(render_data_list))
 
 
 def compute_data_label_ratio(value: float, *, chart: Chart, pivoted_df: DataFrame) -> float:
     chart_min_value, chart_max_value = compute_value_axis_bounds(pivoted_df, chart=chart)
@@ -168,15 +175,15 @@
                         point_position,
                         len(series_points),
                         series.name,
                     )
                     remove_element(data_label._dLbl)
 
 
-def update_data_labels(chart: Chart, *, chart_spec: ChartSpec, pivoted_df: DataFrame):
+def update_data_labels(chart: Chart, *, chart_spec: ChartSpec, pivoted_df: DataFrame) -> None:
     points_by_series_name = {series.name: list(series.points) for series in chart.series}
     remove_data_labels(chart, points_by_series_name=points_by_series_name)
     for data_label_spec in chart_spec.iter_data_label_specs():
         if data_label_spec.type == DataLabelPosition.LAST_POINT.value:
             add_data_label_to_last_point_of_each_series(
                 chart,
                 chart_spec=chart_spec,
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/app.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/app.py`

 * *Files 7% similar despite different names*

```diff
@@ -30,38 +30,38 @@
 logger = daiquiri.getLogger(__name__)
 
 
 DBNOMICS_API_CACHE_DIR_NAME = "dbnomics_api_cache"
 
 
 @app.callback(context_settings={"help_option_names": ["-h", "--help"]})
-def main(verbose: bool = typer.Option(False, "-v", help="Show debug log messages")):
+def main(verbose: bool = typer.Option(False, "-v", help="Show debug log messages")) -> None:
     """
     DBnomics PowerPoint (pptx) tools.
     """
     daiquiri.setup()
     if verbose:
         daiquiri.set_default_log_levels([("dbnomics_pptx_tools", logging.DEBUG)])
 
 
 @app.command()
 def extract_table_zones(
     input_pptx_file: FileBinaryRead,
     slide_expr: str = typer.Argument(..., help="Slide ID or number"),
     table_name: str = typer.Argument(...),
-    metadata_file: Optional[Path] = typer.Option(None, exists=True, readable=True),
-):
+    metadata_file: Path = typer.Option(..., exists=True, readable=True),
+) -> None:
     prs = open_presentation(input_pptx_file)
     prs_slide_ids = [extract_slide_id_from_slide_notes(slide) for slide in cast(Iterable[Slide], prs.slides)]
     slide_number = parse_slide_option(slide_expr, slide_ids=prs_slide_ids)
     slide_id = prs_slide_ids[slide_number - 1]
     if slide_id is None:
         raise typer.BadParameter(f"Slide number {slide_number} does not have an ID defined in the slide notes")
 
-    presentation_metadata = load_presentation_metadata(metadata_file, pptx_file=input_pptx_file)
+    presentation_metadata = load_presentation_metadata(metadata_file)
     slide_metadata = presentation_metadata.slides.get(slide_id)
     table_spec = None if slide_metadata is None else slide_metadata.tables.get(table_name)
 
     slide = find_slide_by_id(prs, slide_id=slide_id)
     if slide is None:
         typer.echo(f"Could not find slide wiht ID {slide_id!r}")
         raise typer.Exit(1)
@@ -85,17 +85,17 @@
 
 
 @app.command()
 def fetch(
     metadata_file: Path = typer.Argument(..., exists=True, readable=True),
     dbnomics_api_cache_dir: Path = typer.Option(DBNOMICS_API_CACHE_DIR_NAME),
     skip_existing: bool = typer.Option(False, help="Do not fetch the series that are already stored in the cache."),
-):
+) -> None:
     presentation_metadata = load_presentation_metadata(metadata_file)
-    series_ids = sorted(presentation_metadata.get_slide_series_ids())
+    series_ids = sorted(presentation_metadata.find_fetchable_series_ids())
 
     cache = SeriesCache(cache_dir=dbnomics_api_cache_dir)
     repo = SeriesRepo(auto_fetch=True, cache=cache, force=not skip_existing)
 
     logger.debug("Fetching all the series needed for the presentation: %r...", series_ids)
 
     fetched_series_ids = []
@@ -120,33 +120,33 @@
     input_pptx_file: FileBinaryRead,
     output_pptx_file: FileBinaryWrite,
     auto_fetch: bool = typer.Option(
         True, help="Fetch series when it is not found in the cache, then add it to the cache."
     ),
     dbnomics_api_cache_dir: Path = typer.Option(DBNOMICS_API_CACHE_DIR_NAME),
     force: bool = typer.Option(False, help="Fetch a series even if it is already stored in the cache."),
-    metadata_file: Optional[Path] = typer.Option(None, exists=True, readable=True),
+    metadata_file: Path = typer.Option(..., exists=True, readable=True),
     only_slides_expr: Optional[str] = typer.Option(None, "--slides"),
     save_processed_slides_only: bool = False,
-):
+) -> None:
     """
     Update DBnomics data in a PowerPoint (pptx) presentation.
     """
     prs = open_presentation(input_pptx_file)
 
     only_slides = None
     if only_slides_expr is not None:
         logger.debug("Will process slides %s", only_slides_expr)
         prs_slide_ids = [extract_slide_id_from_slide_notes(slide) for slide in cast(Iterable[Slide], prs.slides)]
         only_slides = parse_slides_option(only_slides_expr, slide_ids=prs_slide_ids)
 
     if save_processed_slides_only and only_slides is None:
         raise typer.BadParameter("--save-processed-slides-only must be used with --slides")
 
-    presentation_metadata = load_presentation_metadata(metadata_file, pptx_file=input_pptx_file)
+    presentation_metadata = load_presentation_metadata(metadata_file)
 
     cache = SeriesCache(cache_dir=dbnomics_api_cache_dir)
     repo = SeriesRepo(auto_fetch=auto_fetch, cache=cache, force=force)
 
     try:
         update_slides(prs, only_slides=only_slides, presentation_metadata=presentation_metadata, repo=repo)
     except SeriesLoadError as exc:
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/cli_utils.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/cli_utils.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,51 +1,46 @@
 from pathlib import Path
 
 import daiquiri
 import typer
-import yaml  # type: ignore
+import yaml
 from pptx import Presentation as _open_presentation
 from pptx.presentation import Presentation
 from typer import FileBinaryRead
 
 from dbnomics_pptx_tools.cli.slide_expr import parse_slide_expr, parse_slides_expr, slide_to_number
 from dbnomics_pptx_tools.metadata import PresentationMetadata
 
 logger = daiquiri.getLogger(__name__)
 
 
-def load_presentation_metadata(metadata_file: Path | None, *, pptx_file: Path) -> PresentationMetadata:
-    if metadata_file is None:
-        metadata_file = Path(pptx_file.name).with_suffix(".yaml")
-        logger.debug(
-            "Metadata file not passed as an option, using file named after the presentation, with '.yaml' suffix"
-        )
+def load_presentation_metadata(metadata_file: Path) -> PresentationMetadata:
     logger.debug("Loading presentation metadata from %r...", str(metadata_file))
     presentation_metadata_data = yaml.safe_load(metadata_file.read_text())
     return PresentationMetadata.parse_obj(presentation_metadata_data)
 
 
 def open_presentation(input_pptx_file: FileBinaryRead) -> Presentation:
     logger.debug("Loading presentation from %r...", str(input_pptx_file.name))
     prs: Presentation = _open_presentation(input_pptx_file)
     return prs
 
 
-def parse_slide_option(expr: str, *, slide_ids: list[str]) -> int:
+def parse_slide_option(expr: str, *, slide_ids: list[str | None]) -> int:
     try:
         slide = parse_slide_expr(expr)
     except Exception:
         raise typer.BadParameter(f"Could not parse {expr!r}")
 
     try:
         return slide_to_number(slide, slide_ids=slide_ids)
     except ValueError as exc:
         raise typer.BadParameter(f"Invalid slide expression {expr!r}: {exc}") from exc
 
 
-def parse_slides_option(expr: str, *, slide_ids: list[str]) -> list[int]:
+def parse_slides_option(expr: str, *, slide_ids: list[str | None]) -> list[int]:
     try:
         slides = list(parse_slides_expr(expr))
     except Exception:
         raise typer.BadParameter(f"Could not parse {expr!r}")
 
     return [slide_to_number(slide, slide_ids=slide_ids) for slide in slides]
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/cli/slide_expr.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/cli/slide_expr.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from typing import Iterator
 
 
-def check_slide_number(slide_number: int, *, slide_ids: list[str]) -> None:
+def check_slide_number(slide_number: int, *, slide_ids: list[str | None]) -> None:
     if slide_number > len(slide_ids):
         raise ValueError(
             f"Invalid slide number: {slide_number} (there are only {len(slide_ids)} slide in the presentation)"
         )
 
 
 def parse_range_expr(value: str) -> Iterator[int | str]:
@@ -41,19 +41,19 @@
     for part in value.split(","):
         if "-" in value:
             yield from parse_range_expr(part)
         else:
             yield parse_slide_expr(part)
 
 
-def slide_id_to_number(slide_id: str, *, slide_ids: list[str]) -> int:
+def slide_id_to_number(slide_id: str, *, slide_ids: list[str | None]) -> int:
     if slide_id not in slide_ids:
         raise ValueError(f"Invalid slide ID: {slide_id!r}")
 
     slide_number = slide_ids.index(slide_id) + 1
     return slide_number
 
 
-def slide_to_number(slide: str | int, *, slide_ids: list[str]) -> int:
+def slide_to_number(slide: str | int, *, slide_ids: list[str | None]) -> int:
     slide_number = slide_id_to_number(slide, slide_ids=slide_ids) if isinstance(slide, str) else slide
     check_slide_number(slide_number, slide_ids=slide_ids)
     return slide_number
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/metadata.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/data_loader.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,150 +1,126 @@
-from collections import Counter, defaultdict
-from enum import Enum
-from typing import Callable, Iterator, Literal, TypeAlias
+from typing import Iterable, Iterator
 
 import daiquiri
-import isodate
 import pandas as pd
-from isodate import Duration
-from pydantic import BaseModel, Field, StrictStr, validator
-
-from dbnomics_pptx_tools.module_utils import parse_callable
-
-__all__ = ["DataLabelPosition", "PresentationMetadata", "SlideMetadata"]
+from more_itertools import partition
+from pandas import DataFrame, Series
 
+from dbnomics_pptx_tools.metadata import SeriesId, SeriesSpec, ShapeSpec
+from dbnomics_pptx_tools.repo import SeriesRepo
 
 logger = daiquiri.getLogger(__name__)
 
 
-class DataLabelPosition(Enum):
-    LAST_POINT = "last_point"
-
-
-ChartName: TypeAlias = str
-DataLabelType: TypeAlias = Literal["last_point"]
-Frequency: TypeAlias = Literal["annual", "monthly", "quarterly"]
-SeriesId: TypeAlias = str
-SeriesTransformer: TypeAlias = Callable[["SeriesSpec", pd.Series], pd.Series]
-TableLocation: TypeAlias = str
-
-
-class SeriesSpec(BaseModel):
-    id: str
-    name: str
-    tag: str | None = None
-    transformers: list[SeriesTransformer] = Field(default_factory=list)
-
-    @validator("transformers", pre=True, each_item=True)
-    def parse_transformers(cls, value: str):
-        if not isinstance(value, str):
-            raise ValueError(f"str expected, got {type(value)}")
-        function = parse_callable(value)
-        if function is None:
-            raise ValueError(f"The function referenced by {value!r} does not exist")
-        return function
-
-    def apply_transformers(self, series: pd.Series, *, series_id: str) -> pd.Series:
-        for transformer in self.transformers:
+class ShapeDataLoader:
+    def __init__(self, repo: SeriesRepo) -> None:
+        self._repo = repo
+
+    def load_dbnomics_series_spec_df(self, series_spec: SeriesSpec) -> DataFrame:
+        series_id = series_spec.id
+        df = self.load_series_df(series_id)
+        self._apply_transformers(df, series_spec=series_spec)
+        df["__display_name"] = series_spec.name
+        return df
+
+    def load_factory_series_spec_df(self, series_spec: SeriesSpec, *, series_so_far_df: DataFrame) -> DataFrame:
+        series_id = series_spec.id
+        factory = series_spec.factory
+        assert factory is not None
+
+        series = factory.function(series_so_far_df, **factory.parameters)
+        if isinstance(series, Series):
+            logger.debug(
+                "Factory function %r with parameters %r for series ID %r returned:\n%r",
+                factory.function.__qualname__,
+                factory.parameters,
+                series_id,
+                series,
+            )
+        else:
+            raise ValueError(
+                f"Factory function {factory.function.__qualname__!r} for series ID {series_id!r} "
+                f"did not return a Series, got {series!r}"
+            )
+
+        df: DataFrame = series.rename("value").reset_index()
+        df["series_id"] = series_id
+        self._apply_transformers(df, series_spec=series_spec)
+        df["__display_name"] = series_spec.name
+        return df
+
+    def load_series_df(self, series_id: SeriesId) -> DataFrame:
+        df = self._repo.load(series_id)
+        if df.empty:
+            raise ValueError(f"Series {series_id!r} is empty")
+        return df
+
+    def load_shape_df(self, shape_spec: ShapeSpec) -> DataFrame:
+        factory_series_specs, dbnomics_series_specs = partition(
+            lambda series_spec: series_spec.factory is None, shape_spec.series
+        )
+
+        data_source_series_dfs = list(self._iter_data_source_dfs(shape_spec.data_sources))
+        dbnomics_series_dfs = list(self._iter_dbnomics_dfs(dbnomics_series_specs))
+
+        loaded_series_dfs = data_source_series_dfs + dbnomics_series_dfs
+        loaded_series_df = pd.concat(loaded_series_dfs) if loaded_series_dfs else DataFrame()
+        factory_series_dfs = list(self._iter_factory_dfs(factory_series_specs, loaded_series_df))
+
+        shape_series_dfs = dbnomics_series_dfs + factory_series_dfs
+        shape_series_df = pd.concat(shape_series_dfs) if shape_series_dfs else DataFrame()
+        return shape_series_df
+
+    def _apply_transformers(self, df: pd.DataFrame, *, series_spec: SeriesSpec) -> None:
+        transformers = series_spec.transformers
+        if not transformers:
+            return
+
+        series_id = series_spec.id
+        series = df["value"]
+        df["__value_before_transformers"] = series
+        for transformer in transformers:
             logger.debug("Applying transformer %r to series %r", transformer.__qualname__, series_id)
-            series = transformer(self, series)
-        return series
-
-    def has_tag(self, tag: str | None) -> bool:
-        return tag == self.tag
-
-
-class ShapeSpec(BaseModel):
-    series: list[SeriesSpec]
-
-    def find_series_id_by_name(self, series_name: str, *, tag: str | None = None) -> str | None:
-        """Find series ID by its name.
-
-        When tag is None, return the series without a tag (and not any tag).
-        """
-        for series_spec in self.series:
-            if series_spec.name == series_name and series_spec.has_tag(tag):
-                return series_spec.id
-        return None
-
-    def find_series_spec(self, series_id: str) -> SeriesSpec | None:
-        for series_spec in self.series:
-            if series_spec.id == series_id:
-                return series_spec
-        return None
-
-    def get_series_ids(self) -> list[str]:
-        return [series_id_or_spec.id for series_id_or_spec in self.series]
-
-    @validator("series")
-    def validate_series_name_is_unique(cls, value: list[SeriesSpec]):
-        names_by_tag = defaultdict(list)
-        for series_spec in value:
-            names_by_tag[series_spec.tag].append(series_spec.name)
-        for tag, names in names_by_tag.items():
-            counts = Counter(names)
-            duplicates = {name for name, count in counts.items() if count > 1}
-            if duplicates:
-                message = f"Series names must be unique, found those duplicates: {sorted(duplicates)!r}"
-                if tag is not None:
-                    message += f" (for tag {tag})"
-                raise ValueError(message)
-        return value
-
-
-class DataLabelSpec(BaseModel):
-    type: DataLabelType
-    number_format: StrictStr = "0.0"
-
-
-class ChartSpec(ShapeSpec):
-    data_labels: list[DataLabelType | DataLabelSpec] = Field(default_factory=list)
-
-    def iter_data_label_specs(self) -> Iterator[DataLabelSpec]:
-        for data_label in self.data_labels:
-            if isinstance(data_label, str):
-                yield DataLabelSpec(type=data_label)
+            series = transformer(series)
+            if not isinstance(series, Series):
+                raise ValueError(
+                    f"Transformer function {transformer.__qualname__!r} did not return a Series, got {series!r}"
+                )
+
+        df["value"] = series
+
+    def _iter_data_source_dfs(self, series_ids_to_load: Iterable[SeriesId]) -> Iterator[DataFrame]:
+        for series_id in series_ids_to_load:
+            try:
+                yield self.load_series_df(series_id)
+            except ValueError as exc:
+                logger.warning(  # noqa: G200
+                    "Could not load DataFrame for data source series ID %r: %s", series_id, exc
+                )
+
+    def _iter_dbnomics_dfs(self, dbnomics_series_specs: Iterable[SeriesSpec]) -> Iterator[DataFrame]:
+        for dbnomics_series_spec in dbnomics_series_specs:
+            try:
+                yield self.load_dbnomics_series_spec_df(dbnomics_series_spec)
+            except ValueError as exc:
+                logger.warning(  # noqa: G200
+                    "Could not load DataFrame for DBnomics series ID %r: %s", dbnomics_series_spec.id, exc
+                )
+
+    def _iter_factory_dfs(
+        self, factory_series_specs: Iterable[SeriesSpec], loaded_series_df: DataFrame
+    ) -> Iterator[DataFrame]:
+        series_so_far_df = loaded_series_df
+        for factory_series_spec in factory_series_specs:
+            factory = factory_series_spec.factory
+            assert factory is not None
+            try:
+                factory_df = self.load_factory_series_spec_df(factory_series_spec, series_so_far_df=series_so_far_df)
+            except Exception:
+                logger.exception(
+                    "Could not load series from factory function %r with parameters %r, ignoring",
+                    factory.function.__qualname__,
+                    factory.parameters,
+                )
             else:
-                yield data_label
-
-
-class ColumnsSpec(BaseModel):
-    end_period_offset: Duration | None
-    frequency: Frequency
-    period_format: str
-
-    class Config:
-        arbitrary_types_allowed = True
-
-    @validator("end_period_offset", pre=True)
-    def parse_end_period_offset(cls, value: str):
-        if not isinstance(value, str):
-            raise ValueError(f"str expected, got {type(value)}")
-        return isodate.parse_duration(value)
-
-
-class TableSpec(ShapeSpec):
-    columns: ColumnsSpec | None
-    header_first_cell: str = "Country"
-
-
-class SlideMetadata(BaseModel):
-    charts: dict[ChartName, ChartSpec] = Field(default_factory=dict)
-    tables: dict[TableLocation, TableSpec] = Field(default_factory=dict)
-
-    def get_series_ids(self) -> set[str]:
-        series_ids = set()
-        for chart_spec in self.charts.values():
-            series_ids |= set(chart_spec.get_series_ids())
-        for table_spec in self.tables.values():
-            series_ids |= set(table_spec.get_series_ids())
-        return series_ids
-
-
-class PresentationMetadata(BaseModel):
-    slides: dict[str, SlideMetadata]
-
-    def get_slide_series_ids(self) -> set[str]:
-        result = set()
-        for slide in self.slides.values():
-            result |= slide.get_series_ids()
-        return result
+                yield factory_df
+                series_so_far_df = pd.concat([series_so_far_df, factory_df])
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/module_utils.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/module_utils.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 from importlib import import_module
-from typing import Callable
+from typing import Any, Callable
 
 import daiquiri
 from parsy import regex, seq, string
 
 logger = daiquiri.getLogger(__name__)
 
 
-def load_function_from_module(function_name: str, *, module_name: str) -> Callable | None:
+def load_function_from_module(function_name: str, *, module_name: str) -> Callable[..., Any] | None:
     module = import_module(module_name)
     return getattr(module, function_name, None)
 
 
-def parse_callable(callable_ref: str) -> Callable | None:
+def parse_callable(callable_ref: str) -> Callable[..., Any] | None:
     module_name = regex(r"(\w|\.)+").desc("module name")
     function_name = regex(r"(\w|\.)+").desc("function name")
     parser = seq(module_name << string(":"), function_name)
     module_name, function_name = parser.parse(callable_ref)
     return load_function_from_module(function_name, module_name=module_name)
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/pptx_copy.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/pptx_copy.py`

 * *Files 6% similar despite different names*

```diff
@@ -7,23 +7,21 @@
 from pptx.chart.plot import _BasePlot
 from pptx.chart.point import Point
 from pptx.chart.series import SeriesCollection, _BaseCategorySeries
 from pptx.dml.chtfmt import ChartFormat
 from pptx.dml.color import ColorFormat
 from pptx.dml.fill import FillFormat
 from pptx.dml.line import LineFormat
-from pptx.enum.dml import MSO_COLOR_TYPE, MSO_FILL  # type: ignore
+from pptx.enum.dml import MSO_COLOR_TYPE, MSO_FILL
 from pptx.shapes.autoshape import BaseShape
 from pptx.shapes.graphfrm import GraphicFrame
 from pptx.text.text import Font, TextFrame
 
-__all__ = ["copy_shape_properties"]
 
-
-def copy_axis_properties(source: _BaseAxis, target: _BaseAxis):
+def copy_axis_properties(source: _BaseAxis, target: _BaseAxis) -> None:
     assert type(source) == type(source)
     copy_scalar_attributes(
         source,
         target,
         attribute_names={
             "maximum_scale",
             "minimum_scale",
@@ -50,97 +48,92 @@
     elif isinstance(source, ValueAxis):
         assert isinstance(target, ValueAxis)
         copy_value_axis_properties(source, target)
     else:
         raise NotImplementedError()
 
 
-def copy_axis_title_properties(source: AxisTitle, target: AxisTitle):
+def copy_axis_title_properties(source: AxisTitle, target: AxisTitle) -> None:
     copy_scalar_attributes(source, target, attribute_names={"has_text_frame"})
     copy_chart_format_properties(cast(ChartFormat, source.format), cast(ChartFormat, target.format))
     if source.has_text_frame:
         copy_text_frame_properties(source.text_frame, target.text_frame)
 
 
-def copy_base_category_series_properties(source: _BaseCategorySeries, target: _BaseCategorySeries):
+def copy_base_category_series_properties(source: _BaseCategorySeries, target: _BaseCategorySeries) -> None:
     # Ignore data_labels because they will be generated automatically
     copy_scalar_attributes(source, target, attribute_names={"smooth"})
     copy_chart_format_properties(cast(ChartFormat, source.format), cast(ChartFormat, target.format))
-    # for source_point, target_point in zip(cast(Iterable[Point], source.points), cast(Iterable[Point], target.points)):
-    #     copy_point_properties(source_point, target_point)
-    # TODO marker?
 
 
-def copy_chart_format_properties(source: ChartFormat, target: ChartFormat):
+def copy_chart_format_properties(source: ChartFormat, target: ChartFormat) -> None:
     copy_fill_format_properties(cast(FillFormat, source.fill), cast(FillFormat, target.fill))
     copy_line_format_properties(cast(LineFormat, source.line), cast(LineFormat, target.line))
 
 
-def copy_chart_properties(source: Chart, target: Chart):
+def copy_chart_properties(source: Chart, target: Chart) -> None:
     """Copy chart properties.
 
     Plots are ignored because they are set by chart data when calling add_chart.
     """
-    # TODO remove line drawing rectangle around chart
     assert source.chart_type == target.chart_type  # Set by add_chart
     copy_axis_properties(source.category_axis, target.category_axis)
     copy_axis_properties(source.value_axis, target.value_axis)
     copy_font_properties(cast(Font, source.font), cast(Font, target.font))
     if source.chart_style is not None:
         target.chart_style = source.chart_style
     if source.has_legend:
         copy_legend_properties(cast(Legend, source.legend), cast(Legend, target.legend))
     if source.has_title:
         copy_chart_title_properties(source.chart_title, target.chart_title)
     copy_series_collection_properties(cast(SeriesCollection, source.series), cast(SeriesCollection, target.series))
     copy_plots_properties(cast(_Plots, source.plots), cast(_Plots, target.plots))
 
 
-def copy_chart_title_properties(source: ChartTitle, target: ChartTitle):
+def copy_chart_title_properties(source: ChartTitle, target: ChartTitle) -> None:
     copy_axis_title_properties(cast(AxisTitle, source), cast(AxisTitle, target))
 
 
-def copy_color_format_properties(source: ColorFormat, target: ColorFormat):
+def copy_color_format_properties(source: ColorFormat, target: ColorFormat) -> None:
     match source.type:
         case None:
             pass
-        case MSO_COLOR_TYPE.RGB:  # type: ignore
+        case MSO_COLOR_TYPE.RGB:
             copy_scalar_attributes(source, target, attribute_names=["rgb", "brightness"])
-        case MSO_COLOR_TYPE.SCHEME:  # type: ignore
+        case MSO_COLOR_TYPE.SCHEME:
             copy_scalar_attributes(source, target, attribute_names=["theme_color", "brightness"])
         case _:
             raise NotImplementedError(source.type)
 
 
-def copy_data_label_properties(source: DataLabel, target: DataLabel):
+def copy_data_label_properties(source: DataLabel, target: DataLabel) -> None:
     copy_scalar_attributes(source, target, attribute_names={"has_text_frame", "position"})
     if source.has_text_frame:
         copy_font_properties(cast(Font, source.font), cast(Font, target.font))
         copy_text_frame_properties(source.text_frame, target.text_frame)
 
 
-def copy_data_labels_properties(source: DataLabels, target: DataLabels):
+def copy_data_labels_properties(source: DataLabels, target: DataLabels) -> None:
     copy_scalar_attributes(
         source,
         target,
         attribute_names={
             "number_format_is_linked",
             "number_format",
             "show_category_name",
             "show_legend_key",
             "show_percentage",
             "show_series_name",
             "show_value",
         },
     )
     copy_font_properties(cast(Font, source.font), cast(Font, target.font))
-    # TODO position
 
 
-def copy_fill_format_properties(source: FillFormat, target: FillFormat):
+def copy_fill_format_properties(source: FillFormat, target: FillFormat) -> None:
     if source.type != target.type:
         match source.type:
             case MSO_FILL.BACKGROUND:
                 target.background()
             case MSO_FILL.SOLID:
                 target.solid()
             case _:
@@ -152,103 +145,99 @@
             copy_color_format_properties(cast(ColorFormat, source.fore_color), cast(ColorFormat, target.fore_color))
         case MSO_FILL.BACKGROUND:
             pass  # BACKGROUND means transparent
         case _:
             raise NotImplementedError(source.type)
 
 
-def copy_font_properties(source: Font, target: Font):
+def copy_font_properties(source: Font, target: Font) -> None:
     copy_scalar_attributes(
         source, target, attribute_names={"bold", "italic", "language_id", "name", "size", "underline"}
     )
     copy_color_format_properties(cast(ColorFormat, source.color), cast(ColorFormat, target.color))
     copy_fill_format_properties(cast(FillFormat, source.fill), cast(FillFormat, target.fill))
 
 
-def copy_legend_properties(source: Legend, target: Legend):
+def copy_legend_properties(source: Legend, target: Legend) -> None:
     copy_scalar_attributes(source, target, attribute_names={"horz_offset", "include_in_layout", "position"})
     copy_font_properties(cast(Font, source.font), cast(Font, target.font))
 
 
-def copy_line_format_properties(source: LineFormat, target: LineFormat):
+def copy_line_format_properties(source: LineFormat, target: LineFormat) -> None:
     copy_scalar_attributes(source, target, attribute_names={"dash_style", "width"})
     copy_color_format_properties(cast(ColorFormat, source.color), cast(ColorFormat, target.color))
     copy_fill_format_properties(cast(FillFormat, source.fill), cast(FillFormat, target.fill))
 
 
-def copy_major_gridlines_properties(source: MajorGridlines, target: MajorGridlines):
+def copy_major_gridlines_properties(source: MajorGridlines, target: MajorGridlines) -> None:
     copy_chart_format_properties(cast(ChartFormat, source.format), cast(ChartFormat, target.format))
 
 
-def copy_plots_properties(source: _Plots, target: _Plots):
+def copy_plots_properties(source: _Plots, target: _Plots) -> None:
     for source_plot, target_plot in zip(cast(Iterable[_BasePlot], source), cast(Iterable[_BasePlot], target)):
         copy_plot_properties(source_plot, target_plot)
 
 
-def copy_plot_properties(source: _BasePlot, target: _BasePlot):
+def copy_plot_properties(source: _BasePlot, target: _BasePlot) -> None:
     copy_scalar_attributes(source, target, attribute_names={"has_data_labels", "vary_by_categories"})
-    # TODO categories?
     if source.has_data_labels:
         copy_data_labels_properties(source.data_labels, target.data_labels)
 
 
-def copy_point_properties(source: Point, target: Point):
+def copy_point_properties(source: Point, target: Point) -> None:
     copy_data_label_properties(cast(DataLabel, source.data_label), cast(DataLabel, target.data_label))
     copy_chart_format_properties(cast(ChartFormat, source.format), cast(ChartFormat, target.format))
-    # TODO marker?
 
 
-def copy_scalar_attributes(source: object, target: object, *, attribute_names: Iterable[str]):
+def copy_scalar_attributes(source: object, target: object, *, attribute_names: Iterable[str]) -> None:
     for attribute_name in attribute_names:
         source_attribute_value = getattr(source, attribute_name)
         setattr(target, attribute_name, source_attribute_value)
 
 
-def copy_series_collection_properties(source: SeriesCollection, target: SeriesCollection):
+def copy_series_collection_properties(source: SeriesCollection, target: SeriesCollection) -> None:
     for source_series, target_series in zip(source, target):
         if isinstance(source_series, _BaseCategorySeries) and isinstance(target_series, _BaseCategorySeries):
             copy_base_category_series_properties(source_series, target_series)
         else:
             raise NotImplementedError()
 
 
-def copy_shape_properties(source: BaseShape, target: BaseShape):
+def copy_shape_properties(source: BaseShape, target: BaseShape) -> None:
     copy_scalar_attributes(source, target, attribute_names={"name", "rotation"})
     if source.has_chart and target.has_chart:
         assert isinstance(source, GraphicFrame)
         assert isinstance(target, GraphicFrame)
         copy_chart_properties(source.chart, target.chart)
 
 
-def copy_text_frame_properties(source: TextFrame, target: TextFrame):
+def copy_text_frame_properties(source: TextFrame, target: TextFrame) -> None:
     copy_scalar_attributes(
         source,
         target,
         attribute_names={
             "margin_bottom",
             "margin_left",
             "margin_right",
             "margin_top",
             "text",
             "vertical_anchor",
             "word_wrap",
         },
     )
-    # TODO paragraphs?
-    # TODO auto_size?
 
 
-def copy_tick_labels_properties(source: TickLabels, target: TickLabels, *, axis: _BaseAxis):
+def copy_tick_labels_properties(source: TickLabels, target: TickLabels, *, axis: _BaseAxis) -> None:
     copy_scalar_attributes(source, target, attribute_names={"number_format", "number_format_is_linked"})
     copy_font_properties(cast(Font, source.font), cast(Font, target.font))
     if isinstance(axis, CategoryAxis):
         copy_scalar_attributes(source, target, attribute_names={"offset"})
 
 
-def copy_value_axis_properties(source: ValueAxis, target: ValueAxis):
+def copy_value_axis_properties(source: ValueAxis, target: ValueAxis) -> None:
     """Copy only the properties that are specific to ValueAxis.
 
     Cf copy_axis_properties.
     """
     copy_scalar_attributes(
         source,
         target,
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/repo.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/repo.py`

 * *Files 4% similar despite different names*

```diff
@@ -29,15 +29,15 @@
         return pd.concat([self.load(series_id) for series_id in series_ids])
 
     def _add_series_id_column(self, df: DataFrame) -> DataFrame:
         return df.assign(series_id=lambda row: row.provider_code + "/" + row.dataset_code + "/" + row.series_code)
 
     def _fetch_series_df(self, series_id: str) -> DataFrame:
         logger.debug("Fetching series %r from DBnomics API...", series_id)
-        df = fetch_series(series_ids=[series_id])
+        df: DataFrame = fetch_series(series_ids=[series_id])
         df = self._remove_dimension_columns(df)
         df = self._add_series_id_column(df)
         return df
 
     def _remove_dimension_columns(self, df: DataFrame) -> DataFrame:
         columns_to_keep = [
             "@frequency",
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/slides.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/slides.py`

 * *Files 3% similar despite different names*

```diff
@@ -11,27 +11,25 @@
 
 from dbnomics_pptx_tools.charts import update_chart
 from dbnomics_pptx_tools.repo import SeriesRepo
 from dbnomics_pptx_tools.tables import extract_table_zones, format_table, update_table
 
 from .metadata import PresentationMetadata, SlideMetadata
 
-__all__ = ["delete_other_slides", "update_slides"]
-
 logger = daiquiri.getLogger(__name__)
 
 
-def delete_other_slides(prs: Presentation, *, only_slides: Container[int]):
+def delete_other_slides(prs: Presentation, *, only_slides: Container[int]) -> None:
     for slide_pos, slide in enumerate(cast(Iterable[Slide], prs.slides), start=1):
         if slide_pos not in only_slides:
             delete_slide(prs, slide)
 
 
 # Cf https://github.com/scanny/python-pptx/issues/67#issuecomment-296135015
-def delete_slide(prs: Presentation, slide: Slide):
+def delete_slide(prs: Presentation, slide: Slide) -> None:
     slides = cast(Slides, prs.slides)
     id_dict = {slide.id: [i, slide.rId] for i, slide in enumerate(slides._sldIdLst)}
     slide_id = slide.slide_id
     prs.part.drop_rel(id_dict[slide_id][1])
     del slides._sldIdLst[id_dict[slide_id][0]]
 
 
@@ -43,15 +41,15 @@
         >> whitespace.optional()
         >> string(":")
         >> whitespace.optional()
         >> regex(r"[\w_-]+")
         << any_char.many().optional()
     )
     try:
-        return parser.parse(slide_notes)
+        return cast(str, parser.parse(slide_notes))
     except ParseError:
         return None
 
 
 def find_slide_by_id(prs: Presentation, *, slide_id: str) -> Slide | None:
     for slide in cast(Iterable[Slide], prs.slides):
         current_slide_id = extract_slide_id_from_slide_notes(slide)
@@ -61,15 +59,15 @@
     return None
 
 
 def find_table_shape(slide: Slide, table_name: str) -> GraphicFrame | None:
     return first_true(
         iter_table_shapes(slide),
         default=None,
-        pred=lambda table_shape: table_shape.name == table_name,  # type:ignore
+        pred=lambda table_shape: table_shape.name == table_name,  # type: ignore
     )
 
 
 def iter_chart_shapes(slide: Slide) -> Iterator[GraphicFrame]:
     for shape in cast(list[GraphicFrame], slide.shapes):
         if shape.has_chart:
             yield shape
@@ -87,15 +85,15 @@
             if strict:
                 raise ValueError(f"Only LineSeries are expected in {series_collection!r}")
             else:
                 continue
         yield series
 
 
-def update_slide_charts(slide: Slide, *, repo: SeriesRepo, slide_metadata: SlideMetadata):
+def update_slide_charts(slide: Slide, *, repo: SeriesRepo, slide_metadata: SlideMetadata) -> None:
     slide_shapes = list(iter_chart_shapes(slide))
     for chart_pos, chart_shape in enumerate(slide_shapes, start=1):
         chart_name = chart_shape.name
         chart_full_name = f"{chart_name} ({chart_pos}/{len(slide_shapes)})"
 
         chart_spec = slide_metadata.charts.get(chart_name)
         if chart_spec is None:
@@ -115,15 +113,15 @@
                 repo=repo,
                 slide=slide,
             )
         except Exception:
             logger.exception("Error updating chart %s, skipping", chart_full_name)
 
 
-def update_slide_tables(slide: Slide, *, repo: SeriesRepo, slide_metadata: SlideMetadata):
+def update_slide_tables(slide: Slide, *, repo: SeriesRepo, slide_metadata: SlideMetadata) -> None:
     table_shapes = list(iter_table_shapes(slide))
     for table_pos, table_shape in enumerate(table_shapes, start=1):
         table: Table = table_shape.table
         table_name = table_shape.name
         table_full_name = f"{table_name} ({table_pos}/{len(table_shapes)})"
 
         table_spec = slide_metadata.tables.get(table_name)
@@ -155,15 +153,15 @@
 
 def update_slides(
     prs: Presentation,
     *,
     only_slides: Container[int] | None = None,
     presentation_metadata: PresentationMetadata,
     repo: SeriesRepo,
-):
+) -> None:
     for slide_pos, slide in enumerate(cast(Iterable[Slide], prs.slides), start=1):
         if only_slides is not None and slide_pos not in only_slides:
             continue
 
         slide_title: str = slide.shapes.title.text
 
         slide_id = extract_slide_id_from_slide_notes(slide)
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools/tables.py` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools/tables.py`

 * *Files 5% similar despite different names*

```diff
@@ -4,22 +4,21 @@
 
 import daiquiri
 import pandas as pd
 from isodate import Duration
 from pandas import DataFrame
 from parsy import ParseError, any_char, char_from, regex, seq, string
 from pptx.table import Table, _Cell, _Row, _RowCollection
-from tabulate import tabulate  # type: ignore
+from tabulate import tabulate
 
+from dbnomics_pptx_tools.data_loader import ShapeDataLoader
 from dbnomics_pptx_tools.formatters import format_number
-from dbnomics_pptx_tools.metadata import ColumnsSpec, TableSpec
+from dbnomics_pptx_tools.metadata import ColumnsSpec, SeriesSpec, TableSpec
 from dbnomics_pptx_tools.repo import SeriesRepo
 
-__all__ = ["extract_table_zones", "format_table", "replace_cell_text", "update_table"]
-
 logger = daiquiri.getLogger(__name__)
 
 
 @dataclass
 class AnnualPeriod:
     year: int
 
@@ -116,30 +115,34 @@
                 continue
             raise NotImplementedError()
         if table_spec is not None and row.cells[0].text == table_spec.header_first_cell:
             return row_index
     return None
 
 
-def find_latest_column_period(series_df: DataFrame) -> pd.Period:
+def find_latest_column_period(table_series_df: DataFrame) -> pd.Period:
     logger.debug("Finding the period of the latest column from table series")
-    return pd.Period(max(sub_df["original_period"].iloc[-1] for _, sub_df in series_df.dropna().groupby("series_id")))
+    return pd.Period(
+        max(sub_df["original_period"].iloc[-1] for _, sub_df in table_series_df.dropna().groupby("series_id"))
+    )
 
 
 def format_table(table: Table) -> str:
     rows = cast(Iterable[_Row], table.rows)
     tabular_data = [[cell.text for cell in row.cells] for row in rows]
     return tabulate(tabular_data)
 
 
-def generate_periods(columns_spec: ColumnsSpec, *, series_df: DataFrame, table_zones: TableZones) -> Sequence[Period]:
+def generate_periods(
+    columns_spec: ColumnsSpec, *, table_series_df: DataFrame, table_zones: TableZones
+) -> Sequence[Period]:
     frequency = columns_spec.frequency
 
     end_period = (
-        find_latest_column_period(series_df)
+        find_latest_column_period(table_series_df)
         if columns_spec.end_period_offset is None
         else get_end_period_with_offset(columns_spec.end_period_offset)
     )
     logger.debug("The period of the latest column is %r", end_period)
 
     if frequency == "annual":
         return generate_annual_periods(end_period=end_period, table_zones=table_zones)
@@ -169,14 +172,27 @@
 def get_end_period_with_offset(end_period_offset: Duration) -> pd.Period:
     logger.debug(
         "Using the date of today with an offset of %r to determine the period of the latest column", end_period_offset
     )
     return pd.Period(date.today() + end_period_offset)
 
 
+def iter_table_data_row_index_with_series_spec(
+    table: Table, *, table_spec: TableSpec, table_zones: TableZones
+) -> Iterator[tuple[int, SeriesSpec]]:
+    row_index_by_label = {v: k for k, v in iter_table_data_rows(table, table_zones=table_zones)}
+    for series_spec in table_spec.series:
+        series_name = series_spec.name
+        row_index = row_index_by_label.get(series_name)
+        if row_index is None:
+            logger.warning("Could not find the row corresponding to the series name %r, ignoring", series_name)
+            continue
+        yield row_index, series_spec
+
+
 def iter_table_data_rows(table: Table, *, table_zones: TableZones) -> Iterator[tuple[int, str]]:
     rows = list(cast(Iterable[_Row], table.rows))
     first_data_row_index = table_zones.first_data_row_index
 
     for row_index, row in enumerate(rows[first_data_row_index:], start=first_data_row_index):
         row_label = row.cells[0].text.strip()
         yield row_index, row_label
@@ -189,82 +205,78 @@
     full_year = regex(r"[0-9]{4}").desc("4 digit year")
     short_year = regex(r"[0-9]{2}").desc("2 digit year")
     annual_period = full_year.map(int)
     quarterly_period = seq(year=short_year.map(to_full_year), quarter=(string("Q") >> char_from("1234").map(int)))
     period = annual_period.map(AnnualPeriod) | quarterly_period.combine_dict(QuarterlyPeriod)
     attribute = string("(") >> any_char << string(")")
     period_header = period << attribute.optional()
-    return period_header.parse(text)
+    return cast(Period, period_header.parse(text))
 
 
 def parse_header_periods(period_cells: list[_Cell]) -> list[Period] | None:
     period_cells_text = [cell.text for cell in period_cells]
     logger.debug("Parsing period cells: %r", period_cells_text)
 
     has_errors = False
 
-    def iter_parsed():
+    def iter_parsed() -> Iterator[Period]:
         nonlocal has_errors
         for text_pos, text in enumerate(period_cells_text):
             try:
                 yield parse_header_period(text)
             except ParseError:
                 logger.exception("Could not parse period at index %d from text %r", text_pos, text)
                 has_errors = True
 
     return None if has_errors else list(iter_parsed())
 
 
-def replace_cell_text(cell: _Cell, text: str):
+def replace_cell_text(cell: _Cell, text: str) -> None:
     runs = cell.text_frame.paragraphs[0].runs
     if not runs:
         raise ValueError("No text in cell, do not know which format (font, alignment, etc.) to use")
     runs[0].text = text
 
 
-def update_table(table: Table, *, repo: SeriesRepo, table_spec: TableSpec, table_zones: TableZones):
+def update_table(table: Table, *, repo: SeriesRepo, table_spec: TableSpec, table_zones: TableZones) -> None:
+    table_series_df = ShapeDataLoader(repo).load_shape_df(table_spec)
+
     columns_spec = table_spec.columns
     if columns_spec is None:
         assert table_zones.periods is not None
         periods = table_zones.periods
     else:
-        series_df = repo.load_many([series.id for series in table_spec.series])
-        periods = list(generate_periods(columns_spec, series_df=series_df, table_zones=table_zones))
+        periods = list(generate_periods(columns_spec, table_series_df=table_series_df, table_zones=table_zones))
         update_table_header(table, columns_spec=columns_spec, periods=periods, table_zones=table_zones)
 
-    for row_index, row_label in iter_table_data_rows(table, table_zones=table_zones):
-        series_id = table_spec.find_series_id_by_name(row_label)
-        if series_id is None:
-            logger.warning("Could not find the series ID from the row label %r, ignoring row", row_label)
-            continue
-
-        logger.debug("Processing table row %d named %r related to series %r", row_index, row_label, series_id)
-
-        series_spec = table_spec.find_series_spec(series_id)
-        assert series_spec is not None
+    for row_index, series_spec in iter_table_data_row_index_with_series_spec(
+        table, table_spec=table_spec, table_zones=table_zones
+    ):
+        series_id = series_spec.id
+        series_name = series_spec.name
+        logger.debug("Processing table row %d named %r related to series %r", row_index, series_name, series_id)
 
-        series_df = repo.load(series_id)
-        series_df["value"] = series_spec.apply_transformers(series_df["value"], series_id=series_id)
+        row_series_df = table_series_df.query("series_id == @series_id")
 
         for column_index, period in enumerate(periods, start=1):
             update_table_cell(
                 table,
                 column_index=column_index,
                 period=str(period),
                 row_index=row_index,
                 series_id=series_id,
-                series_df=series_df,
+                row_series_df=row_series_df,
             )
 
 
 def update_table_cell(
-    table: Table, *, column_index: int, period: str, row_index: int, series_df: DataFrame, series_id: str
-):
+    table: Table, *, column_index: int, period: str, row_index: int, row_series_df: DataFrame, series_id: str
+) -> None:
     cell = table.cell(row_index, column_index)
-    observations = series_df[series_df["original_period"] == period].value
+    observations = row_series_df[row_series_df["original_period"] == period].value
 
     if observations.empty:
         logger.debug(
             "Period %r requested for table, but not found in series %r, keeping current value (%r)",
             period,
             series_id,
             cell.text,
@@ -272,15 +284,17 @@
     elif len(observations) > 1:
         logger.warning("Many observations found for period %r in series %r, ignoring period", period, series_id)
     else:
         observation = cast(float, observations.values[0])
         replace_cell_text(cell, format_number(observation))
 
 
-def update_table_header(table: Table, *, columns_spec: ColumnsSpec, periods: list[Period], table_zones: TableZones):
+def update_table_header(
+    table: Table, *, columns_spec: ColumnsSpec, periods: list[Period], table_zones: TableZones
+) -> None:
     row_index = table_zones.header_row_index
     logger.debug("Updating the table header (row %d) with periods %r", row_index, [str(p) for p in periods])
     for column_index, period in enumerate(periods, start=1):
         cell = table.cell(row_index, column_index)
         pd_period = period.to_pandas_period()
         period_str = pd_period.strftime(columns_spec.period_format)
         replace_cell_text(cell, period_str)
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/PKG-INFO` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbnomics-pptx-tools
-Version: 0.2.8
+Version: 0.2.9
 Summary: DBnomics PowerPoint (pptx) tools
 Author-email: Christophe Benz <christophe.benz@nomics.world>
 Project-URL: Homepage, https://git.nomics.world/dbnomics/dbnomics-pptx-tools
 Project-URL: Bug Tracker, https://git.nomics.world/dbnomics/dbnomics-pptx-tools/-/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `dbnomics-pptx-tools-0.2.8/src/dbnomics_pptx_tools.egg-info/SOURCES.txt` & `dbnomics-pptx-tools-0.2.9/src/dbnomics_pptx_tools.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 README.md
 pyproject.toml
 setup.cfg
 src/dbnomics_pptx_tools/__init__.py
 src/dbnomics_pptx_tools/cache.py
+src/dbnomics_pptx_tools/data_loader.py
 src/dbnomics_pptx_tools/formatters.py
 src/dbnomics_pptx_tools/metadata.py
 src/dbnomics_pptx_tools/module_utils.py
 src/dbnomics_pptx_tools/pptx_copy.py
 src/dbnomics_pptx_tools/repo.py
 src/dbnomics_pptx_tools/slides.py
 src/dbnomics_pptx_tools/tables.py
@@ -16,10 +17,12 @@
 src/dbnomics_pptx_tools.egg-info/dependency_links.txt
 src/dbnomics_pptx_tools.egg-info/entry_points.txt
 src/dbnomics_pptx_tools.egg-info/requires.txt
 src/dbnomics_pptx_tools.egg-info/top_level.txt
 src/dbnomics_pptx_tools/charts/__init__.py
 src/dbnomics_pptx_tools/charts/chart_data.py
 src/dbnomics_pptx_tools/charts/data_labels.py
+src/dbnomics_pptx_tools/charts/series.py
+src/dbnomics_pptx_tools/charts/utils.py
 src/dbnomics_pptx_tools/cli/app.py
 src/dbnomics_pptx_tools/cli/cli_utils.py
 src/dbnomics_pptx_tools/cli/slide_expr.py
```

