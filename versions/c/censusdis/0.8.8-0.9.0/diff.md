# Comparing `tmp/censusdis-0.8.8.tar.gz` & `tmp/censusdis-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "censusdis-0.8.8.tar", max compression
+gzip compressed data, was "censusdis-0.9.0.tar", max compression
```

## Comparing `censusdis-0.8.8.tar` & `censusdis-0.9.0.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0    19938 2022-09-04 16:09:33.581435 censusdis-0.8.8/LICENSE.md
--rw-r--r--   0        0        0     9190 2022-12-19 21:31:03.165779 censusdis-0.8.8/README.md
--rw-r--r--   0        0        0        0 2022-09-25 01:08:54.692941 censusdis-0.8.8/censusdis/__init__.py
--rw-r--r--   0        0        0    37943 2022-12-19 02:24:25.191452 censusdis-0.8.8/censusdis/data.py
--rw-r--r--   0        0        0     8901 2022-11-17 15:46:01.914512 censusdis-0.8.8/censusdis/geography.py
--rw-r--r--   0        0        0    24536 2022-12-19 02:27:21.907681 censusdis-0.8.8/censusdis/maps.py
--rw-r--r--   0        0        0     5752 2022-12-16 14:10:01.986062 censusdis-0.8.8/censusdis/states.py
--rw-r--r--   0        0        0     1599 2022-12-19 21:32:17.665453 censusdis-0.8.8/pyproject.toml
--rw-r--r--   0        0        0    10389 1970-01-01 00:00:00.000000 censusdis-0.8.8/setup.py
--rw-r--r--   0        0        0    10553 1970-01-01 00:00:00.000000 censusdis-0.8.8/PKG-INFO
+-rw-r--r--   0        0        0    19938 2022-09-04 16:09:33.581435 censusdis-0.9.0/LICENSE.md
+-rw-r--r--   0        0        0    10402 2022-12-24 18:29:27.353153 censusdis-0.9.0/README.md
+-rw-r--r--   0        0        0        0 2022-09-25 01:08:54.692941 censusdis-0.9.0/censusdis/__init__.py
+-rw-r--r--   0        0        0    41291 2022-12-24 18:08:17.969815 censusdis-0.9.0/censusdis/data.py
+-rw-r--r--   0        0        0     9053 2022-12-24 16:38:58.914431 censusdis-0.9.0/censusdis/geography.py
+-rw-r--r--   0        0        0    25245 2022-12-20 22:05:37.483144 censusdis-0.9.0/censusdis/maps.py
+-rw-r--r--   0        0        0     5752 2022-12-16 14:10:01.986062 censusdis-0.9.0/censusdis/states.py
+-rw-r--r--   0        0        0     1599 2022-12-24 13:38:15.778076 censusdis-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0    11611 1970-01-01 00:00:00.000000 censusdis-0.9.0/setup.py
+-rw-r--r--   0        0        0    11765 1970-01-01 00:00:00.000000 censusdis-0.9.0/PKG-INFO
```

### Comparing `censusdis-0.8.8/LICENSE.md` & `censusdis-0.9.0/LICENSE.md`

 * *Files identical despite different names*

### Comparing `censusdis-0.8.8/README.md` & `censusdis-0.9.0/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -21,18 +21,25 @@
 
 `censusdis` is a package for discovering, loading, analyzing, and computing
 diversity, integration, and segregation metrics
 to U.S. Census demographic data. It is designed to be intuitive and Pythonic,
 but give users access to the full collection of data and maps the US Census
 publishes via their APIs. It also avoids hard-coding metadata
 about U.S. Census variables, such as their names, types, and
-hierarchies in groups. Instead it queries this from the 
+hierarchies in groups. Instead, it queries this from the 
 U.S. Census API. This allows it to operate over a large set
 of datasets and years, likely including many that don't
-exist as of time of this writing.
+exist as of time of this writing. It also integrates
+downloading and merging the geometry of geographic 
+geometries to make plotting data and derived metrics simple
+and easy. Finally, it interacts with the `divintseg`
+package to compute diversity and integration metrics.
+
+The design goal of `censusdis` are discussed in more
+detail in [design-goals.md](./design-goals.md).
 
 > ### I'm not sure I get it. Show me what it can do.
 > 
 > The [Nationwide Diversity and Integration](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)
 > notebook demonstrates how we can download, process, and 
 > plot a large amount of US Census demographic data quickly
 > and easily to produce compelling results with just a few
@@ -58,20 +65,20 @@
 import censusdis.data as ced
 from censusdis.states import STATE_GA
 
 # This is a census variable for median household income.
 # See https://api.census.gov/data/2020/acs/acs5/variables/B19013_001E.html
 MEDIAN_HOUSEHOLD_INCOME_VARIABLE = "B19013_001E"
 
-gdf_bg = ced.download_detail(
+gdf_bg = ced.download(
     "acs/acs5",  # The American Community Survey 5-Year Data
-    2020, 
-    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE], 
-    state=STATE_GA, 
-    block_group="*", 
+    2020,
+    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE],
+    state=STATE_GA,
+    block_group="*",
     with_geometry=True
 )
 ```
 
 Similarly, we can download data and geographies, do a little
 analysis on our own using familiar [Pandas](https://pandas.pydata.org/)
 data frame operations, and plot graphs like these
@@ -97,15 +104,18 @@
 [notebook](https://github.com/vengroff/censusdis/tree/main/notebooks) 
 directory of the source code.
 
 The demo notebooks include
 
 | Notebook Name                                                                                              | Description                                                                                                                                                                          |
 |------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
-| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |
+| [ACS Comparison Profile.ipynb](./notebooks/ACS%20Comparison%20Profile.ipynb)                               | Load and plot American Community Survey (ACS) Comparison Profile data at the state level.                                                                                            |
+| [ACS Data Profile.ipynb](./notebooks/ACS%20Data%20Profile.ipynb)                                           | Load and plot American Community Survey (ACS) Data Profile data at the state level.                                                                                                  |
+| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) Detail Table data for New Jersey and plot diversity statewide at the census block group level.                                                  |
+| [ACS Subject Table.ipynb](./notebooks/ACS%20Subject%20Table.ipynb)                                         | Load and plot American Community Survey (ACS) Subject Table data at the state level.                                                                                                 |
 | [Data With Geometry.ipynb](./notebooks/Data%20With%Geometry.ipynb)                                         | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |
 | [Exploring Variables.ipynb](./notebooks/Exploring%20Variables.ipynb)                                       | Load metatdata on a group of variables, visualize the tree hierarchy of variables in the group, and load data from the leaves of the tree.                                           |
 | [Getting Started Examples.ipynb](./notebooks/Getting%20Started%20Examples.ipynb)                           | Sample code from the [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html) guide.                                                                                 |                                                         |
 | [Nationwide Diversity and Integration.ipynb](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb) | Load nationwide demographic data, compute diversity and integration, and plot.                                                                                                       |
 | [Map Demo.ipynb](./notebooks/Map%20Demo.ipynb)                                                             | Demonstrate loading at plotting maps of New Jersey at different geographic granularity.                                                                                              |
 | [Map Geographies.ipynb](./notebooks/Map%20Geographies.ipynb)                                               | Illustrates a large number of different map geogpraphies and how to load them.                                                                                                       |
 | [Population Change 2020-2021.ipynb](./notebooks/Population%20Change%202020-2021.ipynb)                     | Track the change in state population from 2020 to 2021 using ACS5 data.                                                                                                              |
```

### Comparing `censusdis-0.8.8/censusdis/data.py` & `censusdis-0.9.0/censusdis/data.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 """
 Utilities for loading census dats.
 
 This module relies on the US Census API, which
 it wraps in a pythonic manner.
 """
 
+import warnings
 from abc import ABC, abstractmethod
 from collections import defaultdict
 from typing import (
     Any,
     DefaultDict,
     Dict,
     Generator,
@@ -63,23 +64,23 @@
     if (
         isinstance(parsed_json, list)
         and len(parsed_json) >= 1
         and isinstance(parsed_json[0], list)
     ):
         return pd.DataFrame(
             parsed_json[1:],
-            columns=(
+            columns=[
                 c.upper()
                 .replace(" ", "_")
                 .replace("-", "_")
                 .replace("/", "_")
                 .replace("(", "")
                 .replace(")", "")
                 for c in parsed_json[0]
-            ),
+            ],
         )
 
     raise CensusApiException(
         f"Expected json data to be a list of lists, not a {type(parsed_json)}"
     )
 
 
@@ -95,35 +96,69 @@
         f"Census API request to {request.url} failed with status {request.status_code}. {request.text}"
     )
 
 
 _MAX_FIELDS_PER_DOWNLOAD = 50
 
 
-def _download_concat_detail(
+def _download_concat(
     dataset: str,
     year: int,
     fields: List[str],
     *,
     key: Optional[str],
     census_variables: "VariableCache",
     with_geometry: bool = False,
     **kwargs: cgeo.InSpecType,
 ) -> pd.DataFrame:
+    """
+    Download data in groups of columns and concatenate the results together.
+
+    The reason for this function is that the API will only return a maximum
+    of 50 columns per query. This function downloads wider data 50 columns
+    at a time and concatenates them.
 
+    Parameters
+    ----------
+    dataset
+        The dataset to download from. For example `acs/acs5` or
+        `dec/pl`.
+    year
+        The year to download data for.
+    download_variables
+        The census variables to download, for example `["NAME", "B01001_001E"]`.
+    with_geometry
+        If `True` a :py:class:`gpd.GeoDataFrame` will be returned and each row
+        will have a geometry that is a cartographic boundary suitable for platting
+        a map. See https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.2020.html
+        for details of the shapefiles that will be downloaded on your behalf to
+        generate these boundaries.
+    api_key
+        An optional API key. If you don't have or don't use a key, the number
+        of calls you can make will be limited.
+    variable_cache
+        A cache of metadata about variables.
+    kwargs
+        A specification of the geometry that we want data for.
+
+    Returns
+    -------
+        The full results of the query with all columns.
+
+    """
     # Divide the fields into groups.
     field_groups = [
         # black and flake8 disagree about the whitespace before ':' here...
         fields[start : start + _MAX_FIELDS_PER_DOWNLOAD]  # noqa: 203
         for start in range(0, len(fields), _MAX_FIELDS_PER_DOWNLOAD)
     ]
 
     # Get the data for each chunk.
     dfs = [
-        download_detail(
+        download(
             dataset,
             year,
             field_group,
             api_key=key,
             variable_cache=census_variables,
             with_geometry=with_geometry and (ii == 0),
             **kwargs,
@@ -154,15 +189,15 @@
 
 
 def set_shapefile_path(shapefile_path: Union[str, None]) -> None:
     """
     Set the path to the directory to cache shapefiles.
 
     This is where we will cache shapefiles downloaded when
-    `with_geometry=True` is passed to :py:func:`~download_detail`.
+    `with_geometry=True` is passed to :py:func:`~download`.
 
     Parameters
     ----------
     shapefile_path
         The path to use for caching shapefiles.
     """
     global __shapefile_root
@@ -171,15 +206,15 @@
 
 
 def get_shapefile_path() -> Union[str, None]:
     """
     Get the path to the directory to cache shapefiles.
 
     This is where we will cache shapefiles downloaded when
-    `with_geometry=True` is passed to :py:func:`~download_detail`.
+    `with_geometry=True` is passed to :py:func:`~download`.
 
     Returns
     -------
         The path to use for caching shapefiles.
     """
     global __shapefile_root
 
@@ -441,14 +476,51 @@
     *,
     with_geometry: bool = False,
     api_key: Optional[str] = None,
     variable_cache: Optional["VariableCache"] = None,
     **kwargs: cgeo.InSpecType,
 ) -> Union[pd.DataFrame, gpd.GeoDataFrame]:
     """
+    Deprecated version of :py:ref:`~download`; use `download` instead.
+
+    Same functionality but under the old name. Back in the pre-history
+    of `censusdis`, this function started life as a way to download
+    ACS detail tables. It evolved significantly since then and does much
+    more now. Hence the name change.
+
+    This function will disappear completely in a future version.
+    """
+    warnings.warn(
+        "censusdis.data.download_detail is deprecated. "
+        "Please use censusdis.data.download instead.",
+        DeprecationWarning,
+        2,
+    )
+    return download(
+        dataset,
+        year,
+        download_variables,
+        with_geometry=with_geometry,
+        api_key=api_key,
+        variable_cache=variable_cache,
+        **kwargs,
+    )
+
+
+def download(
+    dataset: str,
+    year: int,
+    download_variables: Iterable[str],
+    *,
+    with_geometry: bool = False,
+    api_key: Optional[str] = None,
+    variable_cache: Optional["VariableCache"] = None,
+    **kwargs: cgeo.InSpecType,
+) -> Union[pd.DataFrame, gpd.GeoDataFrame]:
+    """
     Download data from the US Census API.
 
     This is the main API for downloading US Census data with the
     `censusdis` package. There are many examples of how to use
     this in the demo notebooks provided with the package at
     https://github.com/vengroff/censusdis/tree/main/notebooks.
 
@@ -491,15 +563,15 @@
     }
 
     if not isinstance(download_variables, list):
         download_variables = list(download_variables)
 
     # Special case if we are trying to get too many fields.
     if len(download_variables) > _MAX_FIELDS_PER_DOWNLOAD:
-        return _download_concat_detail(
+        return _download_concat(
             dataset,
             year,
             download_variables,
             key=api_key,
             census_variables=variable_cache,
             with_geometry=with_geometry,
             **kwargs,
@@ -525,24 +597,30 @@
                 f"If not found, check {census_variables_url} for all variables in the dataset."
             )
 
     # If we were given a list, join it together into
     # a comma-separated string.
     string_kwargs = {k: _gf2s(v) for k, v in kwargs.items()}
 
-    url, params, bound_path = census_detail_table_url(
+    url, params, bound_path = census_table_url(
         dataset, year, download_variables, api_key=api_key, **string_kwargs
     )
     df_data = data_from_url(url, params)
 
     for field in download_variables:
         field_type = variable_cache.get(dataset, year, field)["predicateType"]
 
         if field_type == "int":
-            df_data[field] = df_data[field].astype(int)
+            if df_data[field].isnull().any():
+                # Some Census data sets put in null in int fields.
+                # We have to go with a float to make this a NaN.
+                # Int has no representation for NaN or None.
+                df_data[field] = df_data[field].astype(float)
+            else:
+                df_data[field] = df_data[field].astype(int)
         elif field_type == "float":
             df_data[field] = df_data[field].astype(float)
         elif field_type == "string":
             pass
         else:
             # Leave it as an object?
             pass
@@ -560,39 +638,62 @@
 
         gdf_data = _add_geography(df_data, year, shapefile_scope, geo_level)
         return gdf_data
 
     return df_data
 
 
-def census_detail_table_url(
+def census_table_url(
     dataset: str,
     year: int,
-    fields: Iterable[str],
+    download_variables: Iterable[str],
     *,
     api_key: Optional[str] = None,
     **kwargs: cgeo.InSpecType,
 ) -> Tuple[str, Mapping[str, str], cgeo.BoundGeographyPath]:
+    """
+    Construct the URL to download data from the U.S. Census API.
+
+    Parameters
+    ----------
+    dataset
+        The dataset to download from. For example `acs/acs5` or
+        `dec/pl`.
+    year
+        The year to download data for.
+    download_variables
+        The census variables to download, for example `["NAME", "B01001_001E"]`.
+    api_key
+        An optional API key. If you don't have or don't use a key, the number
+        of calls you can make will be limited.
+    kwargs
+        A specification of the geometry that we want data for.
+
+    Returns
+    -------
+        The URL, parameters and bound path.
+
+    """
     bound_path = cgeo.PathSpec.partial_prefix_match(dataset, year, **kwargs)
 
     if bound_path is None:
         raise CensusApiException(
             f"Unable to match the geography specification {kwargs}.\n"
             f"Supported geographies for dataset='{dataset}' in year={year} are:\n"
             + "\n".join(
                 f"{path_spec}"
                 for path_spec in cgeo.geo_path_snake_specs(dataset, year).values()
             )
         )
 
     query_spec = cgeo.CensusGeographyQuerySpec(
-        dataset, year, list(fields), bound_path, api_key=api_key
+        dataset, year, list(download_variables), bound_path, api_key=api_key
     )
 
-    url, params = query_spec.detail_table_url()
+    url, params = query_spec.table_url()
 
     return url, params, bound_path
 
 
 class VariableSource(ABC):
     """
     A source of variables, typically used behind a :py:class:`~VariableCache`.
```

### Comparing `censusdis-0.8.8/censusdis/geography.py` & `censusdis-0.9.0/censusdis/geography.py`

 * *Files 2% similar despite different names*

```diff
@@ -246,15 +246,22 @@
         *components, _ = self.bound_path.bindings.items()
 
         if components:
             return " ".join(f"{k}:{v}" for (k, v) in components)
 
         return None
 
-    def detail_table_url(self) -> Tuple[str, Mapping[str, str]]:
+    def table_url(self) -> Tuple[str, Mapping[str, str]]:
+        """
+        Construct the URL to query census data.
+
+        Returns
+        -------
+            The URL and the parameters to pass to it.
+        """
         url = "/".join([self._BASE_URL, f"{self.year:04}", self.dataset])
 
         params = {
             "get": ",".join(self.variables),
             "for": self.for_component,
         }
```

### Comparing `censusdis-0.8.8/censusdis/maps.py` & `censusdis-0.9.0/censusdis/maps.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,18 +10,18 @@
 import shutil
 from zipfile import ZipFile, BadZipFile
 
 import geopandas as gpd
 import requests
 import shapely.affinity
 from shapely import affinity
-from shapely.geometry import MultiPolygon, Polygon
+from shapely.geometry import MultiPolygon, Polygon, Point
 from shapely.geometry.base import BaseGeometry
 
-from typing import Optional
+from typing import Optional, Union
 
 from censusdis.states import STATE_AK, STATE_HI, TERRITORY_PR
 
 
 class MapException(Exception):
     pass
 
@@ -419,21 +419,25 @@
         .apply(
             lambda s: gpd.clip(s, gdf_state_bounds[gdf_state_bounds.STATEFP == s.name])
         )
         .droplevel("STATEFP")
     )
 
 
-def _wrap_poly(poly):
+def _wrap_poly(poly: Union[Polygon, Point]):
     """
     A helper function for moving a polygon.
 
     Used in shifting AK and HI geometries.
     """
-    x_coord, _ = poly.exterior.coords.xy
+    if isinstance(poly, Polygon):
+        x_coord, _ = poly.exterior.coords.xy
+    elif isinstance(poly, Point):
+        x_coord = [poly.x]
+
     if x_coord[0] > 0:
         poly = affinity.translate(poly, xoff=-360.0, yoff=0.0)
     return poly
 
 
 def _wrap_polys(polys):
     """
@@ -740,7 +744,32 @@
     else:
         # At least wrap the Aleutian islands.
         gdf = gdf.copy()
         gdf.geometry = gdf.geometry.map(_wrap_polys)
 
     ax = gdf.boundary.plot(*args, **kwargs)
     return ax
+
+
+def geographic_centroids(gdf: gpd.GeoDataFrame) -> gpd.GeoSeries:
+    """
+    Compute the centroid of a geography.
+
+    We do this by projecting to epsg 3857 (https://epsg.io/3857),
+    computing the centroid, and then projecting back. This gives
+    a reasonable answer for most geometries and avoids warnings from
+    `GeoPandas`.
+
+    Parameters
+    ----------
+    gdf
+
+    Returns
+    -------
+
+    """
+    crs = gdf.crs
+
+    projected_centroids = gdf.geometry.to_crs(epsg=3857).geometry.centroid
+    centroids = projected_centroids.to_crs(crs)
+
+    return centroids
```

### Comparing `censusdis-0.8.8/censusdis/states.py` & `censusdis-0.9.0/censusdis/states.py`

 * *Files identical despite different names*

### Comparing `censusdis-0.8.8/pyproject.toml` & `censusdis-0.9.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "censusdis"
-version = "0.8.8"
+version = "0.9.0"
 description = "US Census utilities for a variety of data loading and mapping purposes."
 license = "HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV"
 authors = ["Darren Vengroff"]
 readme = "README.md"
 repository = "https://github.com/vengroff/censusdis"
 keywords = ["census", "demographics"]
 classifiers = [
```

### Comparing `censusdis-0.8.8/setup.py` & `censusdis-0.9.0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,17 +20,17 @@
           'sphinx-rtd-theme==1.0.0',
           'sphinx-copybutton>=0.5.1,<0.6.0',
           'sphinxcontrib-napoleon==0.7',
           'toml>=0.10.0,<0.11.0']}
 
 setup_kwargs = {
     'name': 'censusdis',
-    'version': '0.8.8',
+    'version': '0.9.0',
     'description': 'US Census utilities for a variety of data loading and mapping purposes.',
-    'long_description': '# censusdis\n\n[![Hippocratic License HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/cl-eco-extr-ffd-law-mil-sv.html)\n[![Documentation Status](https://readthedocs.org/projects/censusdis/badge/?version=latest)](https://censusdis.readthedocs.io/en/latest/?badge=latest)\n![Tests Badge](reports/junit/tests-badge.svg)\n![Coverage Badge](reports/coverage/coverage-badge.svg)\n![Notebook Tests Badge](reports/nbmake/nbmake-badge.svg)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/censusdis)\n\nClick any of the thumbnails below to see the notebook\nthat generated it.\n\n[<img src="docs/_static/images/sample00.png" alt="Integration in SoMa Tracts" height=160>](notebooks/SoMa%20DIS%20Demo.ipynb)\n[<img src="docs/_static/images/sample01.png" alt="Diversity in New Jersey" height=160>](notebooks/Data%20With%20Geometry.ipynb)\n[<img src="docs/_static/images/sample02.png" alt="2020 Median Income by County in Georgia" height=160>](notebooks/Data%20With%20Geometry.ipynb)\n[<img src="docs/_static/images/sample05.png" alt="Nationwide Integration at the Census Tract over Block Group Level" height=160>](notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)\n[<img src="docs/_static/images/sample03.png" alt="White Alone Population as a Percent of County Population" height=160>](notebooks/Seeing%20White.ipynb)\n[<img src="docs/_static/images/sample04.png" alt="Average Age by Public Use Microdata Area in Massachusetts" height=160>](notebooks/PUMS%20Demo.ipynb)\n\n## Introduction \n\n`censusdis` is a package for discovering, loading, analyzing, and computing\ndiversity, integration, and segregation metrics\nto U.S. Census demographic data. It is designed to be intuitive and Pythonic,\nbut give users access to the full collection of data and maps the US Census\npublishes via their APIs. It also avoids hard-coding metadata\nabout U.S. Census variables, such as their names, types, and\nhierarchies in groups. Instead it queries this from the \nU.S. Census API. This allows it to operate over a large set\nof datasets and years, likely including many that don\'t\nexist as of time of this writing.\n\n> ### I\'m not sure I get it. Show me what it can do.\n> \n> The [Nationwide Diversity and Integration](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)\n> notebook demonstrates how we can download, process, and \n> plot a large amount of US Census demographic data quickly\n> and easily to produce compelling results with just a few\n> lines of code.\n\n> ### I\'m sold! I want to dive right in!\n> \n> To get straight to installing and trying out\n> code hop over to our \n> [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html)\n> guide.\n\n`censusdis` lets you quickly and easily load US Census data and make plots like \nthis one:\n\n![Median income by block group in GA](docs/_static/images/sample02.png)\n\nWe downloaded the data behind this plot, including\nthe geometry of all the block groups, with a\nsingle call:\n\n```python\nimport censusdis.data as ced\nfrom censusdis.states import STATE_GA\n\n# This is a census variable for median household income.\n# See https://api.census.gov/data/2020/acs/acs5/variables/B19013_001E.html\nMEDIAN_HOUSEHOLD_INCOME_VARIABLE = "B19013_001E"\n\ngdf_bg = ced.download_detail(\n    "acs/acs5",  # The American Community Survey 5-Year Data\n    2020, \n    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE], \n    state=STATE_GA, \n    block_group="*", \n    with_geometry=True\n)\n```\n\nSimilarly, we can download data and geographies, do a little\nanalysis on our own using familiar [Pandas](https://pandas.pydata.org/)\ndata frame operations, and plot graphs like these\n\n![Percent of population identifying as white by county](docs/_static/images/sample03.png)\n![Integration is SoMa](docs/_static/images/sample00.png)\n\n## Modules\n\nThe modules that make up the `censusdis` package are\n\n| Module                | Description                                                                                                   |\n|-----------------------|:--------------------------------------------------------------------------------------------------------------|\n| `censusdis.geography` | Code for managing geography hierarchies in which census data is organized.                                    | \n| `censusdis.data`      | Code for fetching data from the US Census API, including managing datasets, groups, and variable hierarchies. |\n| `censusdis.maps`      | Code for downloading map data from the US, caching it locally, and using it to render maps.                   |\n| `censusdis.states`    | Constants defining the US States. Used by the three other modules.                                            |\n\n## Demonstration Notebooks\n\nThere are several demonstration notebooks available to illustrate how `censusdis` can\nbe used. They are found in the \n[notebook](https://github.com/vengroff/censusdis/tree/main/notebooks) \ndirectory of the source code.\n\nThe demo notebooks include\n\n| Notebook Name                                                                                              | Description                                                                                                                                                                          |\n|------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |\n| [Data With Geometry.ipynb](./notebooks/Data%20With%Geometry.ipynb)                                         | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |\n| [Exploring Variables.ipynb](./notebooks/Exploring%20Variables.ipynb)                                       | Load metatdata on a group of variables, visualize the tree hierarchy of variables in the group, and load data from the leaves of the tree.                                           |\n| [Getting Started Examples.ipynb](./notebooks/Getting%20Started%20Examples.ipynb)                           | Sample code from the [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html) guide.                                                                                 |                                                         |\n| [Nationwide Diversity and Integration.ipynb](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb) | Load nationwide demographic data, compute diversity and integration, and plot.                                                                                                       |\n| [Map Demo.ipynb](./notebooks/Map%20Demo.ipynb)                                                             | Demonstrate loading at plotting maps of New Jersey at different geographic granularity.                                                                                              |\n| [Map Geographies.ipynb](./notebooks/Map%20Geographies.ipynb)                                               | Illustrates a large number of different map geogpraphies and how to load them.                                                                                                       |\n| [Population Change 2020-2021.ipynb](./notebooks/Population%20Change%202020-2021.ipynb)                     | Track the change in state population from 2020 to 2021 using ACS5 data.                                                                                                              |\n| [PUMS Demo.ipynb](./notebooks/PUMS%20Demo.ipynb)                                                           | Load Public-Use Microdata Samples (PUMS) data for Massachusetts and plot it.                                                                                                         |\n| [Seeing White.ipynb](./notebooks/Seeing%20White.ipynb)                                                     | Load nationwide demographic data at the county level and plot of map of the US showing the percent of the population who identify as white only (no other race) at the county level. | \n| [SoMa DIS Demo.ipynb](./notebooks/SoMa%20DIS%20Demo.ipynb)                                                 | Load race and ethnicity data for two towns in Essex County, NJ and compute diversity and integration metrics.                                                                        |\n\n\n## Diversity and Integration Metrics\n\nDiversity and integration metrics from the `divintseg` package are \ndemonstrated in some notebooks.\n\nFor more information on these metrics\nsee the [divintseg](https://github.com/vengroff/divintseg/) \nproject.\n\n',
+    'long_description': '# censusdis\n\n[![Hippocratic License HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/cl-eco-extr-ffd-law-mil-sv.html)\n[![Documentation Status](https://readthedocs.org/projects/censusdis/badge/?version=latest)](https://censusdis.readthedocs.io/en/latest/?badge=latest)\n![Tests Badge](reports/junit/tests-badge.svg)\n![Coverage Badge](reports/coverage/coverage-badge.svg)\n![Notebook Tests Badge](reports/nbmake/nbmake-badge.svg)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/censusdis)\n\nClick any of the thumbnails below to see the notebook\nthat generated it.\n\n[<img src="docs/_static/images/sample00.png" alt="Integration in SoMa Tracts" height=160>](notebooks/SoMa%20DIS%20Demo.ipynb)\n[<img src="docs/_static/images/sample01.png" alt="Diversity in New Jersey" height=160>](notebooks/Data%20With%20Geometry.ipynb)\n[<img src="docs/_static/images/sample02.png" alt="2020 Median Income by County in Georgia" height=160>](notebooks/Data%20With%20Geometry.ipynb)\n[<img src="docs/_static/images/sample05.png" alt="Nationwide Integration at the Census Tract over Block Group Level" height=160>](notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)\n[<img src="docs/_static/images/sample03.png" alt="White Alone Population as a Percent of County Population" height=160>](notebooks/Seeing%20White.ipynb)\n[<img src="docs/_static/images/sample04.png" alt="Average Age by Public Use Microdata Area in Massachusetts" height=160>](notebooks/PUMS%20Demo.ipynb)\n\n## Introduction \n\n`censusdis` is a package for discovering, loading, analyzing, and computing\ndiversity, integration, and segregation metrics\nto U.S. Census demographic data. It is designed to be intuitive and Pythonic,\nbut give users access to the full collection of data and maps the US Census\npublishes via their APIs. It also avoids hard-coding metadata\nabout U.S. Census variables, such as their names, types, and\nhierarchies in groups. Instead, it queries this from the \nU.S. Census API. This allows it to operate over a large set\nof datasets and years, likely including many that don\'t\nexist as of time of this writing. It also integrates\ndownloading and merging the geometry of geographic \ngeometries to make plotting data and derived metrics simple\nand easy. Finally, it interacts with the `divintseg`\npackage to compute diversity and integration metrics.\n\nThe design goal of `censusdis` are discussed in more\ndetail in [design-goals.md](./design-goals.md).\n\n> ### I\'m not sure I get it. Show me what it can do.\n> \n> The [Nationwide Diversity and Integration](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)\n> notebook demonstrates how we can download, process, and \n> plot a large amount of US Census demographic data quickly\n> and easily to produce compelling results with just a few\n> lines of code.\n\n> ### I\'m sold! I want to dive right in!\n> \n> To get straight to installing and trying out\n> code hop over to our \n> [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html)\n> guide.\n\n`censusdis` lets you quickly and easily load US Census data and make plots like \nthis one:\n\n![Median income by block group in GA](docs/_static/images/sample02.png)\n\nWe downloaded the data behind this plot, including\nthe geometry of all the block groups, with a\nsingle call:\n\n```python\nimport censusdis.data as ced\nfrom censusdis.states import STATE_GA\n\n# This is a census variable for median household income.\n# See https://api.census.gov/data/2020/acs/acs5/variables/B19013_001E.html\nMEDIAN_HOUSEHOLD_INCOME_VARIABLE = "B19013_001E"\n\ngdf_bg = ced.download(\n    "acs/acs5",  # The American Community Survey 5-Year Data\n    2020,\n    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE],\n    state=STATE_GA,\n    block_group="*",\n    with_geometry=True\n)\n```\n\nSimilarly, we can download data and geographies, do a little\nanalysis on our own using familiar [Pandas](https://pandas.pydata.org/)\ndata frame operations, and plot graphs like these\n\n![Percent of population identifying as white by county](docs/_static/images/sample03.png)\n![Integration is SoMa](docs/_static/images/sample00.png)\n\n## Modules\n\nThe modules that make up the `censusdis` package are\n\n| Module                | Description                                                                                                   |\n|-----------------------|:--------------------------------------------------------------------------------------------------------------|\n| `censusdis.geography` | Code for managing geography hierarchies in which census data is organized.                                    | \n| `censusdis.data`      | Code for fetching data from the US Census API, including managing datasets, groups, and variable hierarchies. |\n| `censusdis.maps`      | Code for downloading map data from the US, caching it locally, and using it to render maps.                   |\n| `censusdis.states`    | Constants defining the US States. Used by the three other modules.                                            |\n\n## Demonstration Notebooks\n\nThere are several demonstration notebooks available to illustrate how `censusdis` can\nbe used. They are found in the \n[notebook](https://github.com/vengroff/censusdis/tree/main/notebooks) \ndirectory of the source code.\n\nThe demo notebooks include\n\n| Notebook Name                                                                                              | Description                                                                                                                                                                          |\n|------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| [ACS Comparison Profile.ipynb](./notebooks/ACS%20Comparison%20Profile.ipynb)                               | Load and plot American Community Survey (ACS) Comparison Profile data at the state level.                                                                                            |\n| [ACS Data Profile.ipynb](./notebooks/ACS%20Data%20Profile.ipynb)                                           | Load and plot American Community Survey (ACS) Data Profile data at the state level.                                                                                                  |\n| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) Detail Table data for New Jersey and plot diversity statewide at the census block group level.                                                  |\n| [ACS Subject Table.ipynb](./notebooks/ACS%20Subject%20Table.ipynb)                                         | Load and plot American Community Survey (ACS) Subject Table data at the state level.                                                                                                 |\n| [Data With Geometry.ipynb](./notebooks/Data%20With%Geometry.ipynb)                                         | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |\n| [Exploring Variables.ipynb](./notebooks/Exploring%20Variables.ipynb)                                       | Load metatdata on a group of variables, visualize the tree hierarchy of variables in the group, and load data from the leaves of the tree.                                           |\n| [Getting Started Examples.ipynb](./notebooks/Getting%20Started%20Examples.ipynb)                           | Sample code from the [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html) guide.                                                                                 |                                                         |\n| [Nationwide Diversity and Integration.ipynb](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb) | Load nationwide demographic data, compute diversity and integration, and plot.                                                                                                       |\n| [Map Demo.ipynb](./notebooks/Map%20Demo.ipynb)                                                             | Demonstrate loading at plotting maps of New Jersey at different geographic granularity.                                                                                              |\n| [Map Geographies.ipynb](./notebooks/Map%20Geographies.ipynb)                                               | Illustrates a large number of different map geogpraphies and how to load them.                                                                                                       |\n| [Population Change 2020-2021.ipynb](./notebooks/Population%20Change%202020-2021.ipynb)                     | Track the change in state population from 2020 to 2021 using ACS5 data.                                                                                                              |\n| [PUMS Demo.ipynb](./notebooks/PUMS%20Demo.ipynb)                                                           | Load Public-Use Microdata Samples (PUMS) data for Massachusetts and plot it.                                                                                                         |\n| [Seeing White.ipynb](./notebooks/Seeing%20White.ipynb)                                                     | Load nationwide demographic data at the county level and plot of map of the US showing the percent of the population who identify as white only (no other race) at the county level. | \n| [SoMa DIS Demo.ipynb](./notebooks/SoMa%20DIS%20Demo.ipynb)                                                 | Load race and ethnicity data for two towns in Essex County, NJ and compute diversity and integration metrics.                                                                        |\n\n\n## Diversity and Integration Metrics\n\nDiversity and integration metrics from the `divintseg` package are \ndemonstrated in some notebooks.\n\nFor more information on these metrics\nsee the [divintseg](https://github.com/vengroff/divintseg/) \nproject.\n\n',
     'author': 'Darren Vengroff',
     'author_email': 'None',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/vengroff/censusdis',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `censusdis-0.8.8/PKG-INFO` & `censusdis-0.9.0/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: censusdis
-Version: 0.8.8
+Version: 0.9.0
 Summary: US Census utilities for a variety of data loading and mapping purposes.
 Home-page: https://github.com/vengroff/censusdis
 License: HL3-CL-ECO-EXTR-FFD-LAW-MIL-SV
 Keywords: census,demographics
 Author: Darren Vengroff
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 3 - Alpha
@@ -53,18 +53,25 @@
 
 `censusdis` is a package for discovering, loading, analyzing, and computing
 diversity, integration, and segregation metrics
 to U.S. Census demographic data. It is designed to be intuitive and Pythonic,
 but give users access to the full collection of data and maps the US Census
 publishes via their APIs. It also avoids hard-coding metadata
 about U.S. Census variables, such as their names, types, and
-hierarchies in groups. Instead it queries this from the 
+hierarchies in groups. Instead, it queries this from the 
 U.S. Census API. This allows it to operate over a large set
 of datasets and years, likely including many that don't
-exist as of time of this writing.
+exist as of time of this writing. It also integrates
+downloading and merging the geometry of geographic 
+geometries to make plotting data and derived metrics simple
+and easy. Finally, it interacts with the `divintseg`
+package to compute diversity and integration metrics.
+
+The design goal of `censusdis` are discussed in more
+detail in [design-goals.md](./design-goals.md).
 
 > ### I'm not sure I get it. Show me what it can do.
 > 
 > The [Nationwide Diversity and Integration](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb)
 > notebook demonstrates how we can download, process, and 
 > plot a large amount of US Census demographic data quickly
 > and easily to produce compelling results with just a few
@@ -90,20 +97,20 @@
 import censusdis.data as ced
 from censusdis.states import STATE_GA
 
 # This is a census variable for median household income.
 # See https://api.census.gov/data/2020/acs/acs5/variables/B19013_001E.html
 MEDIAN_HOUSEHOLD_INCOME_VARIABLE = "B19013_001E"
 
-gdf_bg = ced.download_detail(
+gdf_bg = ced.download(
     "acs/acs5",  # The American Community Survey 5-Year Data
-    2020, 
-    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE], 
-    state=STATE_GA, 
-    block_group="*", 
+    2020,
+    ["NAME", MEDIAN_HOUSEHOLD_INCOME_VARIABLE],
+    state=STATE_GA,
+    block_group="*",
     with_geometry=True
 )
 ```
 
 Similarly, we can download data and geographies, do a little
 analysis on our own using familiar [Pandas](https://pandas.pydata.org/)
 data frame operations, and plot graphs like these
@@ -129,15 +136,18 @@
 [notebook](https://github.com/vengroff/censusdis/tree/main/notebooks) 
 directory of the source code.
 
 The demo notebooks include
 
 | Notebook Name                                                                                              | Description                                                                                                                                                                          |
 |------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
-| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |
+| [ACS Comparison Profile.ipynb](./notebooks/ACS%20Comparison%20Profile.ipynb)                               | Load and plot American Community Survey (ACS) Comparison Profile data at the state level.                                                                                            |
+| [ACS Data Profile.ipynb](./notebooks/ACS%20Data%20Profile.ipynb)                                           | Load and plot American Community Survey (ACS) Data Profile data at the state level.                                                                                                  |
+| [ACS Demo.ipynb](./notebooks/ACS%20Demo.ipynb)                                                             | Load American Community Survey (ACS) Detail Table data for New Jersey and plot diversity statewide at the census block group level.                                                  |
+| [ACS Subject Table.ipynb](./notebooks/ACS%20Subject%20Table.ipynb)                                         | Load and plot American Community Survey (ACS) Subject Table data at the state level.                                                                                                 |
 | [Data With Geometry.ipynb](./notebooks/Data%20With%Geometry.ipynb)                                         | Load American Community Survey (ACS) data for New Jersey and plot diversity statewide at the census block group level.                                                               |
 | [Exploring Variables.ipynb](./notebooks/Exploring%20Variables.ipynb)                                       | Load metatdata on a group of variables, visualize the tree hierarchy of variables in the group, and load data from the leaves of the tree.                                           |
 | [Getting Started Examples.ipynb](./notebooks/Getting%20Started%20Examples.ipynb)                           | Sample code from the [Getting Started](https://censusdis.readthedocs.io/en/latest/intro.html) guide.                                                                                 |                                                         |
 | [Nationwide Diversity and Integration.ipynb](./notebooks/Nationwide%20Diversity%20and%20Integration.ipynb) | Load nationwide demographic data, compute diversity and integration, and plot.                                                                                                       |
 | [Map Demo.ipynb](./notebooks/Map%20Demo.ipynb)                                                             | Demonstrate loading at plotting maps of New Jersey at different geographic granularity.                                                                                              |
 | [Map Geographies.ipynb](./notebooks/Map%20Geographies.ipynb)                                               | Illustrates a large number of different map geogpraphies and how to load them.                                                                                                       |
 | [Population Change 2020-2021.ipynb](./notebooks/Population%20Change%202020-2021.ipynb)                     | Track the change in state population from 2020 to 2021 using ACS5 data.                                                                                                              |
```

