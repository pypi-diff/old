# Comparing `tmp/osmrx-0.0.5.tar.gz` & `tmp/osmrx-0.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "osmrx-0.0.5.tar", max compression
+gzip compressed data, was "osmrx-0.0.6.tar", max compression
```

## Comparing `osmrx-0.0.5.tar` & `osmrx-0.0.6.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0    35149 2023-04-06 20:28:50.789620 osmrx-0.0.5/LICENSE
--rw-r--r--   0        0        0     1269 2023-04-06 20:28:50.789620 osmrx-0.0.5/README.md
--rw-r--r--   0        0        0      211 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/__init__.py
--rw-r--r--   0        0        0        0 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/__init__.py
--rw-r--r--   0        0        0     1346 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/core.py
--rw-r--r--   0        0        0     2564 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/models.py
--rw-r--r--   0        0        0     1768 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/nominatim.py
--rw-r--r--   0        0        0      570 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/overpass.py
--rw-r--r--   0        0        0     1499 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/apis_handler/query_builder.py
--rw-r--r--   0        0        0        0 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/data_processing/__init__.py
--rw-r--r--   0        0        0     2528 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/data_processing/overpass_data_builder.py
--rw-r--r--   0        0        0     3074 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/globals/queries.py
--rw-r--r--   0        0        0        0 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/graph_manager/__init__.py
--rw-r--r--   0        0        0     2875 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/graph_manager/arc_feature.py
--rw-r--r--   0        0        0     5369 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/graph_manager/graph_manager.py
--rw-r--r--   0        0        0     2313 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/graph_manager/isochrones_feature.py
--rw-r--r--   0        0        0     1074 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/graph_manager/path_feature.py
--rw-r--r--   0        0        0        0 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/helpers/__init__.py
--rw-r--r--   0        0        0     2551 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/helpers/logger.py
--rw-r--r--   0        0        0     1451 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/helpers/misc.py
--rw-r--r--   0        0        0     2543 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/main/core.py
--rw-r--r--   0        0        0     1108 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/main/pois.py
--rw-r--r--   0        0        0     4437 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/main/roads.py
--rw-r--r--   0        0        0        0 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/topology/__init__.py
--rw-r--r--   0        0        0     1943 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/topology/checker.py
--rw-r--r--   0        0        0    15360 2023-04-06 20:28:50.789620 osmrx-0.0.5/osmrx/topology/cleaner.py
--rw-r--r--   0        0        0      595 2023-04-06 20:28:50.793620 osmrx-0.0.5/pyproject.toml
--rw-r--r--   0        0        0     2268 1970-01-01 00:00:00.000000 osmrx-0.0.5/setup.py
--rw-r--r--   0        0        0     1847 1970-01-01 00:00:00.000000 osmrx-0.0.5/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-04-06 21:41:00.119394 osmrx-0.0.6/LICENSE
+-rw-r--r--   0        0        0     4150 2023-04-06 21:41:00.119394 osmrx-0.0.6/README.md
+-rw-r--r--   0        0        0      211 2023-04-06 21:41:00.119394 osmrx-0.0.6/osmrx/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 21:41:00.119394 osmrx-0.0.6/osmrx/apis_handler/__init__.py
+-rw-r--r--   0        0        0     1346 2023-04-06 21:41:00.119394 osmrx-0.0.6/osmrx/apis_handler/core.py
+-rw-r--r--   0        0        0     2564 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/apis_handler/models.py
+-rw-r--r--   0        0        0     1768 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/apis_handler/nominatim.py
+-rw-r--r--   0        0        0      570 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/apis_handler/overpass.py
+-rw-r--r--   0        0        0     1499 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/apis_handler/query_builder.py
+-rw-r--r--   0        0        0        0 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/data_processing/__init__.py
+-rw-r--r--   0        0        0     2528 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/data_processing/overpass_data_builder.py
+-rw-r--r--   0        0        0     3074 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/globals/queries.py
+-rw-r--r--   0        0        0        0 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/graph_manager/__init__.py
+-rw-r--r--   0        0        0     2875 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/graph_manager/arc_feature.py
+-rw-r--r--   0        0        0     5369 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/graph_manager/graph_manager.py
+-rw-r--r--   0        0        0     2313 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/graph_manager/isochrones_feature.py
+-rw-r--r--   0        0        0     1074 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/graph_manager/path_feature.py
+-rw-r--r--   0        0        0        0 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/helpers/__init__.py
+-rw-r--r--   0        0        0     2551 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/helpers/logger.py
+-rw-r--r--   0        0        0     1451 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/helpers/misc.py
+-rw-r--r--   0        0        0     2543 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/main/core.py
+-rw-r--r--   0        0        0     1108 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/main/pois.py
+-rw-r--r--   0        0        0     4618 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/main/roads.py
+-rw-r--r--   0        0        0        0 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/topology/__init__.py
+-rw-r--r--   0        0        0     1943 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/topology/checker.py
+-rw-r--r--   0        0        0    15360 2023-04-06 21:41:00.123394 osmrx-0.0.6/osmrx/topology/cleaner.py
+-rw-r--r--   0        0        0      595 2023-04-06 21:41:00.123394 osmrx-0.0.6/pyproject.toml
+-rw-r--r--   0        0        0     5205 1970-01-01 00:00:00.000000 osmrx-0.0.6/setup.py
+-rw-r--r--   0        0        0     4728 1970-01-01 00:00:00.000000 osmrx-0.0.6/PKG-INFO
```

### Comparing `osmrx-0.0.5/LICENSE` & `osmrx-0.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/apis_handler/core.py` & `osmrx-0.0.6/osmrx/apis_handler/core.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/apis_handler/models.py` & `osmrx-0.0.6/osmrx/apis_handler/models.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/apis_handler/nominatim.py` & `osmrx-0.0.6/osmrx/apis_handler/nominatim.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/apis_handler/overpass.py` & `osmrx-0.0.6/osmrx/apis_handler/overpass.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/apis_handler/query_builder.py` & `osmrx-0.0.6/osmrx/apis_handler/query_builder.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/data_processing/overpass_data_builder.py` & `osmrx-0.0.6/osmrx/data_processing/overpass_data_builder.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/globals/queries.py` & `osmrx-0.0.6/osmrx/globals/queries.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/graph_manager/arc_feature.py` & `osmrx-0.0.6/osmrx/graph_manager/arc_feature.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/graph_manager/graph_manager.py` & `osmrx-0.0.6/osmrx/graph_manager/graph_manager.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/graph_manager/isochrones_feature.py` & `osmrx-0.0.6/osmrx/graph_manager/isochrones_feature.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/graph_manager/path_feature.py` & `osmrx-0.0.6/osmrx/graph_manager/path_feature.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/helpers/logger.py` & `osmrx-0.0.6/osmrx/helpers/logger.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/helpers/misc.py` & `osmrx-0.0.6/osmrx/helpers/misc.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/main/core.py` & `osmrx-0.0.6/osmrx/main/core.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/main/pois.py` & `osmrx-0.0.6/osmrx/main/pois.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/main/roads.py` & `osmrx-0.0.6/osmrx/main/roads.py`

 * *Files 7% similar despite different names*

```diff
@@ -41,14 +41,15 @@
 
     @property
     def data(self) -> List[Dict] | None:
         """Return the data"""
         if self._graph_manager.features is not None:
             return [feature.to_dict(with_attr=True) for feature in self._graph_manager.features]
 
+    @property
     def graph(self) -> rx.PyGraph | rx.PyDiGraph:
         return self._graph_manager.graph
 
     def _execute(self):
         """Continue the execution by building the graph"""
         super()._execute()
         self._build_graph()
@@ -68,32 +69,37 @@
     def from_location(self, location: str):
         """Find roads from location"""
         self.geo_filter = Location(location, logger=self.logger)
         self._execute()
 
 
 class GraphAnalysis(Roads):
+    # TODO improvements needed
+
     def __init__(self, mode: str, nodes_to_connect: List[Point]):
         # must be ordered
         nodes_to_connect = [{"topo_uuid": 999999 + enum, "geometry": node}
                             for enum, node in enumerate(nodes_to_connect)]
         super().__init__(mode=mode, nodes_to_connect=nodes_to_connect)
 
     def get_shortest_path(self) -> Generator[PathFeature, Any, None]:
-        """Compute a shortest path from a node to an other node"""
-        assert len(self.additional_nodes) > 1, "You need 2 points at least to compute a path"
-        nodes = [node["geometry"] for node in self.additional_nodes]
-
-        for from_point, to_point in zip(nodes, nodes[1:]):
-            area = MultiPoint([from_point, to_point]).buffer(from_point.distance(to_point) / 2).bounds
-            self.from_bbox(tuple([area[1], area[0], area[3], area[2]]))
-            paths = self._graph_manager.compute_shortest_path(from_point, to_point)
-            for path in paths:
-                yield path
-            self.logger.info(f"Shortest path(s) built from {from_point.wkt} to {to_point.wkt}.")
+        # TODO improve: code is ugly
+        """Compute a shortest path from a source node to a target node"""
+        assert len(self.additional_nodes) == 2, "You need 2 points to compute a path"
+        assert not self.additional_nodes[0]["geometry"].equals(self.additional_nodes[-1]["geometry"]), "Your points must be different"
+
+        from_point = self.additional_nodes[0]["geometry"]
+        to_point = self.additional_nodes[-1]["geometry"]
+
+        area = MultiPoint([from_point, to_point]).buffer(from_point.distance(to_point) / 2).bounds
+        self.from_bbox(tuple([area[1], area[0], area[3], area[2]]))
+        paths = self._graph_manager.compute_shortest_path(from_point, to_point)
+        for path in paths:
+            yield path
+        self.logger.info(f"Shortest path(s) built from {from_point.wkt} to {to_point.wkt}.")
 
     def isochrones_from_distance(self, intervals: List[int], precision: float = 1.0) -> IsochronesFeature:
         """Compute isochrones from a node based on distances"""
         assert len(self.additional_nodes) == 1, "You need 1 point to compute an isochrone"
         nodes = [node["geometry"] for node in self.additional_nodes]
 
         for node in nodes:
```

### Comparing `osmrx-0.0.5/osmrx/topology/checker.py` & `osmrx-0.0.6/osmrx/topology/checker.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/osmrx/topology/cleaner.py` & `osmrx-0.0.6/osmrx/topology/cleaner.py`

 * *Files identical despite different names*

### Comparing `osmrx-0.0.5/pyproject.toml` & `osmrx-0.0.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "osmrx"
-version = "0.0.5"
+version = "0.0.6"
 description = ""
 authors = ["amauryval <amauryval@gmail.com>"]
 license = ""
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "3.11.0"
```

