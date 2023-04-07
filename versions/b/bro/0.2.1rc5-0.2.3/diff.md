# Comparing `tmp/bro-0.2.1rc5.tar.gz` & `tmp/bro-0.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bro-0.2.1rc5.tar", last modified: Fri Mar 31 12:38:02 2023, max compression
+gzip compressed data, was "bro-0.2.3.tar", last modified: Fri Apr  7 10:20:36 2023, max compression
```

## Comparing `bro-0.2.1rc5.tar` & `bro-0.2.3.tar`

### file list

```diff
@@ -1,24 +1,25 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 12:38:02.729526 bro-0.2.1rc5/
--rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-31 12:37:38.000000 bro-0.2.1rc5/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3441 2023-03-31 12:38:02.729526 bro-0.2.1rc5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1608 2023-03-31 12:37:38.000000 bro-0.2.1rc5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 12:38:02.729526 bro-0.2.1rc5/bro/
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-31 12:37:38.000000 bro-0.2.1rc5/bro/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-31 12:37:38.000000 bro-0.2.1rc5/bro/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10764 2023-03-31 12:37:38.000000 bro-0.2.1rc5/bro/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     1003 2023-03-31 12:37:38.000000 bro-0.2.1rc5/bro/helper_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1736 2023-03-31 12:37:38.000000 bro-0.2.1rc5/bro/objects.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 12:38:02.729526 bro-0.2.1rc5/bro.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3441 2023-03-31 12:38:02.000000 bro-0.2.1rc5/bro.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      331 2023-03-31 12:38:02.000000 bro-0.2.1rc5/bro.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 12:38:02.000000 bro-0.2.1rc5/bro.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-03-31 12:38:02.000000 bro-0.2.1rc5/bro.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-03-31 12:38:02.000000 bro-0.2.1rc5/bro.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 12:38:02.729526 bro-0.2.1rc5/examples/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-31 12:37:38.000000 bro-0.2.1rc5/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      982 2023-03-31 12:37:38.000000 bro-0.2.1rc5/examples/examples.py
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 12:38:02.729526 bro-0.2.1rc5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-03-31 12:37:38.000000 bro-0.2.1rc5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 12:38:02.729526 bro-0.2.1rc5/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     5577 2023-03-31 12:37:38.000000 bro-0.2.1rc5/tests/test_api.py
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-31 12:37:38.000000 bro-0.2.1rc5/tests/test_objects.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:36.456128 bro-0.2.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-04-07 10:20:07.000000 bro-0.2.3/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-07 10:20:36.456128 bro-0.2.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1608 2023-04-07 10:20:07.000000 bro-0.2.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:36.452128 bro-0.2.3/bro/
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-07 10:20:07.000000 bro-0.2.3/bro/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-07 10:20:07.000000 bro-0.2.3/bro/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12303 2023-04-07 10:20:07.000000 bro-0.2.3/bro/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      942 2023-04-07 10:20:07.000000 bro-0.2.3/bro/helper_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1717 2023-04-07 10:20:07.000000 bro-0.2.3/bro/objects.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:36.456128 bro-0.2.3/bro.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-07 10:20:36.000000 bro-0.2.3/bro.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-04-07 10:20:36.000000 bro-0.2.3/bro.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:20:36.000000 bro-0.2.3/bro.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-07 10:20:36.000000 bro-0.2.3/bro.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-07 10:20:36.000000 bro-0.2.3/bro.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:36.456128 bro-0.2.3/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:07.000000 bro-0.2.3/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      982 2023-04-07 10:20:07.000000 bro-0.2.3/examples/examples.py
+-rw-r--r--   0 runner    (1001) docker     (123)      523 2023-04-07 10:20:07.000000 bro-0.2.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 10:20:36.456128 bro-0.2.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1797 2023-04-07 10:20:07.000000 bro-0.2.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:20:36.456128 bro-0.2.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     5556 2023-04-07 10:20:07.000000 bro-0.2.3/tests/test_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-04-07 10:20:07.000000 bro-0.2.3/tests/test_objects.py
```

### Comparing `bro-0.2.1rc5/LICENSE.txt` & `bro-0.2.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `bro-0.2.1rc5/PKG-INFO` & `bro-0.2.3/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 Metadata-Version: 2.1
 Name: bro
-Version: 0.2.1rc5
+Version: 0.2.3
 Summary: Open source python library for accessing BRO API
 Home-page: https://github.com/viktor-platform/bro
 Author: VIKTOR
 Author-email: support@viktor.ai
 License: see LICENSE.txt
+Project-URL: Example VIKTOR application, https://demo.viktor.ai/public/bro-app
+Project-URL: Source code VIKTOR application, https://github.com/viktor-platform/bro-app
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: License :: Free To Use But Restricted
 Classifier: Operating System :: Microsoft :: Windows
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
-![](https://img.shields.io/badge/release-v0.2.1rc5-green)
+![](https://img.shields.io/badge/release-v0.2.3-green)
 
 # BRO
 This package can access the REST API from the [BRO](https://www.broloket.nl/ondergrondgegevens). Currently, this package provides
 functionality to request CPTs from the BRO when you provide a region of interest. The format is based on the REST API of the BRO, which is described [here](https://publiek.broservices.nl/sr/cpt/v1/swagger-ui/#/default/) for CPTs.
 
 Current options include retrieval of the following objects: 
 1. CPTs (format: bytes, dict)
```

### Comparing `bro-0.2.1rc5/README.md` & `bro-0.2.3/README.md`

 * *Files identical despite different names*

### Comparing `bro-0.2.1rc5/bro/api.py` & `bro-0.2.3/bro/api.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,28 +1,35 @@
 from dataclasses import dataclass
 from pathlib import Path
-
-from pyproj import Transformer
-from typing import Union, List
+from typing import List
+from typing import Optional
+from typing import Union
 
 import requests
 import xmltodict
+from pyproj import Transformer
 
 from .helper_functions import _str2bool
 from .objects import IMBROFile
 
+# pylint: disable=exec-used
 about = {}
-with open(Path(__file__).parent / '__version__.py', 'r') as f:
+with open(Path(__file__).parent / "__version__.py", "r") as f:
     exec(f.read(), about)
+# pylint: enable=exec-used
+
 
 REQUEST_REFERENCE = f"Requested-with-bro-v{about['__version__']}"
 CPT_OBJECT_URL = "https://publiek.broservices.nl/sr/cpt/v1/objects/"
-CPT_CHARACTERISTICS_URL = f"https://publiek.broservices.nl/sr/cpt/v1/characteristics/searches?requestReference={REQUEST_REFERENCE}"
+CPT_CHARACTERISTICS_URL = (
+    f"https://publiek.broservices.nl/sr/cpt/v1/characteristics/searches?requestReference={REQUEST_REFERENCE}"
+)
 
 
+# pylint: disable=unpacking-non-sequence
 @dataclass
 class RDPoint:
     x: float
     y: float
 
     def from_rd_to_wgs84(self) -> "Point":
         """Converts RD coordinates (EPSG:28992) in m  to lat/lon coordinates (EPSG: 4326) in degrees
@@ -51,14 +58,15 @@
         :param lat: float latitude in degree (WGS84 / EPSG:4326)
         :param lon: float longitude in degree (WGS84 / EPSG:4326)
         :return:
         """
         transformer = Transformer.from_crs(4326, 28992)
         rd_y, rd_x = transformer.transform(self.lat, self.lon)
         return RDPoint(rd_y, rd_x)
+# pylint: enable=unpacking-non-sequence
 
 
 @dataclass
 class Circle:
     center: Point
     radius: float
     """
@@ -66,34 +74,29 @@
     radius: circle radius in km
     """
 
     @property
     def bro_json(self):
         return {
             "enclosingCircle": {
-                "center": {
-                    "lat": self.center.lat,
-                    "lon": self.center.lon
-                },
-                "radius": self.radius
+                "center": {"lat": self.center.lat, "lon": self.center.lon},
+                "radius": self.radius,
             }
         }
 
     @property
     def to_geojson_feature(self):
         return {
-                "type": "Feature",
-                "geometry": {
-                    "type": "Point",
-                    "coordinates": [self.center.lon, self.center.lat]
-                },
-                "properties": {
-                    "description": f"Requested centroid"
-                }
-            }
+            "type": "Feature",
+            "geometry": {
+                "type": "Point",
+                "coordinates": [self.center.lon, self.center.lat],
+            },
+            "properties": {"description": "Requested centroid"},
+        }
 
 
 @dataclass
 class Envelope:
     lower_corner: Point
     upper_corner: Point
 
@@ -114,67 +117,107 @@
 
     @property
     def to_geojson_feature(self) -> dict:
         return {
             "type": "Feature",
             "geometry": {
                 "type": "Polygon",
-                "coordinates": [[
-                    [self.lower_corner.lon, self.lower_corner.lat],
-                    [self.upper_corner.lon, self.lower_corner.lat],
-                    [self.upper_corner.lon, self.upper_corner.lat],
-                    [self.lower_corner.lon, self.upper_corner.lat],
-                    [self.lower_corner.lon, self.lower_corner.lat],
-                ]
-                ]
+                "coordinates": [
+                    [
+                        [self.lower_corner.lon, self.lower_corner.lat],
+                        [self.upper_corner.lon, self.lower_corner.lat],
+                        [self.upper_corner.lon, self.upper_corner.lat],
+                        [self.lower_corner.lon, self.upper_corner.lat],
+                        [self.lower_corner.lon, self.lower_corner.lat],
+                    ]
+                ],
             },
-            "properties": {
-                "description": f"Requested area"
-            }
+            "properties": {"description": "Requested area"},
         }
 
 
 class CPTCharacteristics:
     """
     Class to save all Characteristics of a CPT object, resulting from a characteristics search on the API
     """
+
     def __init__(self, parsed_dispatch_document: dict):
         self.gml_id: str = parsed_dispatch_document["gml:id"]
         self.bro_id: str = parsed_dispatch_document["brocom:broId"]
         self.deregistered: bool = _str2bool(parsed_dispatch_document["brocom:deregistered"])
         self.accountable_party: int = parsed_dispatch_document["brocom:deliveryAccountableParty"]
         self.quality_regime: str = parsed_dispatch_document["brocom:qualityRegime"]
         self.object_registration_time: str = parsed_dispatch_document["brocom:objectRegistrationTime"]
         self.under_review: bool = _str2bool(parsed_dispatch_document["brocom:underReview"])
-        self.standardized_location: Point = Point(*tuple(elem for elem in parsed_dispatch_document["brocom:standardizedLocation"]["gml:pos"].split(' ')))
-        self.delivered_location: RDPoint = RDPoint(*tuple(elem for elem in parsed_dispatch_document["brocom:deliveredLocation"]["gml:pos"].split(' ')))
-        self.local_vertical_reference_point: str = parsed_dispatch_document["localVerticalReferencePoint"]["value"]
-        self.vertical_datum: str = parsed_dispatch_document["verticalDatum"]["value"]
-        self.cpt_standard: str = parsed_dispatch_document["cptStandard"]["value"]
-        self.offset: float = float(parsed_dispatch_document["offset"]["value"])
-        self.quality_class: str = parsed_dispatch_document["qualityClass"]
-        self.research_report_date: str = parsed_dispatch_document["researchReportDate"]["brocom:date"]
-        self.start_time: str = parsed_dispatch_document["startTime"]
-        self.predrilled_depth: float = float(parsed_dispatch_document["predrilledDepth"]["value"]) if parsed_dispatch_document.get("predrilledDepth") else None
-        self.final_depth: float = float(parsed_dispatch_document["finalDepth"]["value"])
-        self.survey_purpose: str = parsed_dispatch_document["surveyPurpose"]["value"]
-        self.dissipation_test_performed: bool = _str2bool(parsed_dispatch_document["dissipationTestPerformed"])
-        self.stop_criterion: str = parsed_dispatch_document["stopCriterion"]["value"]
+        self.standardized_location: Point = Point(
+            *tuple(elem for elem in parsed_dispatch_document["brocom:standardizedLocation"]["gml:pos"].split(" "))
+        )
+        self.delivered_location: RDPoint = RDPoint(
+            *tuple(elem for elem in parsed_dispatch_document["brocom:deliveredLocation"]["gml:pos"].split(" "))
+        )
+        self.local_vertical_reference_point: Optional[str] = (
+            parsed_dispatch_document["localVerticalReferencePoint"]["value"]
+            if parsed_dispatch_document.get("localVerticalReferencePoint")
+            else None
+        )
+        self.vertical_datum: Optional[str] = (
+            parsed_dispatch_document["verticalDatum"]["value"]
+            if parsed_dispatch_document.get("verticalDatum")
+            else None
+        )
+        self.cpt_standard: Optional[str] = (
+            parsed_dispatch_document["cptStandard"]["value"] if parsed_dispatch_document.get("cptStandard") else None
+        )
+        self.offset: Optional[float] = (
+            float(parsed_dispatch_document["offset"]["value"]) if parsed_dispatch_document.get("offset") else None
+        )
+        self.quality_class: Optional[str] = (
+            parsed_dispatch_document["qualityClass"] if parsed_dispatch_document.get("offset") else None
+        )
+        self.research_report_date: Optional[str] = (
+            parsed_dispatch_document["researchReportDate"]["brocom:date"]
+            if parsed_dispatch_document.get("researchReportDate")
+            else None
+        )
+        self.start_time: Optional[str] = parsed_dispatch_document.get("startTime")
+        self.predrilled_depth: Optional[float] = (
+            float(parsed_dispatch_document["predrilledDepth"]["value"])
+            if parsed_dispatch_document.get("predrilledDepth")
+            else None
+        )
+        self.final_depth: Optional[float] = (
+            float(parsed_dispatch_document["finalDepth"]["value"])
+            if parsed_dispatch_document.get("finalDepth")
+            else None
+        )
+        self.survey_purpose: Optional[str] = (
+            parsed_dispatch_document["surveyPurpose"]["value"]
+            if parsed_dispatch_document.get("surveyPurpose")
+            else None
+        )
+        self.dissipation_test_performed: Optional[bool] = (
+            _str2bool(parsed_dispatch_document["dissipationTestPerformed"])
+            if parsed_dispatch_document.get("dissipationTestPerformed")
+            else None
+        )
+        self.stop_criterion: Optional[str] = (
+            parsed_dispatch_document["stopCriterion"]["value"]
+            if parsed_dispatch_document.get("stopCriterion")
+            else None
+        )
 
     @property
     def to_geojson_feature(self) -> dict:
         return {
             "type": "Feature",
             "geometry": {
                 "type": "Point",
-                "coordinates": [self.wgs84_coordinate.lon, self.wgs84_coordinate.lat]
+                "coordinates": [self.wgs84_coordinate.lon, self.wgs84_coordinate.lat],
             },
-            "properties": {
-                "bro_id": f"{self.bro_id}"
-            }
+            "properties": {"bro_id": f"{self.bro_id}"},
         }
 
     @property
     def rd_coordinate(self) -> RDPoint:
         return self.delivered_location
 
     @property
@@ -200,20 +243,16 @@
     # TODO: Add logging for amount of cpts to be retrieved
 
     # Retrieve the objects in series
     bro_cpt_objects = [get_cpt_object(available_cpt.bro_id, as_dict=as_dict) for available_cpt in available_cpts]
     return bro_cpt_objects
 
 
-def get_cpt_characteristics(
-    begin_date: str,
-    end_date: str,
-    area: Union[Circle, Envelope]
-) -> list:
-    """ Retrieves available CPT Objects from the BRO in given date / area range.
+def get_cpt_characteristics(begin_date: str, end_date: str, area: Union[Circle, Envelope]) -> list:
+    """Retrieves available CPT Objects from the BRO in given date / area range.
 
     :param begin_date: str date in format YYYY-mm-dd (.strftime("%Y-%m-%d")) and should be > 2015-01-01
     :param end_date: str date in format YYYY-mm-dd (.strftime("%Y-%m-%d"))
     :param area: Union[Circle, Envelope] definition of area in which to look for CPT objects
     :return: A list of objects containing metadata of available CPT objects, WITHOUT actual measurements
     """
 
@@ -223,57 +262,57 @@
     }
 
     json = {
         "registrationPeriod": {
             "beginDate": begin_date,
             "endDate": end_date,
         },
-        "area": area.bro_json
+        "area": area.bro_json,
     }
 
-    response = requests.post(
-        CPT_CHARACTERISTICS_URL,
-        headers=headers,
-        json=json,
-    )
+    response = requests.post(CPT_CHARACTERISTICS_URL, headers=headers, json=json, timeout=10)
 
     available_cpt_objects = []
-    # Check status codes, if 200 return, if 400 get json with description
+    # TODO: Check status codes in BRO REST API documentation.
     if response.status_code == 200:
         parsed = xmltodict.parse(response.content, attr_prefix="", cdata_key="value")
-        if parsed['dispatchCharacteristicsResponse']["numberOfDocuments"] == 0:
-            raise ValueError("No available objects have been found in given date + area range. Retry with different parameters.")
 
-        for document in parsed['dispatchCharacteristicsResponse']['dispatchDocument']:
+        rejection_reason = parsed["dispatchCharacteristicsResponse"].get("brocom:rejectionReason")
+        if rejection_reason:
+            raise ValueError(f"{rejection_reason}")
+
+        nr_of_documents = parsed["dispatchCharacteristicsResponse"].get("numberOfDocuments")
+        if nr_of_documents == 0:
+            raise ValueError(
+                "No available objects have been found in given date + area range. Retry with different parameters."
+            )
+
+        for document in parsed["dispatchCharacteristicsResponse"]["dispatchDocument"]:
             # TODO: Hard skip, this is likely to happen when it's deregistered. document will have key ["BRO_DO"]["brocom:deregistered"] = "ja"
             # TODO: Add this information to logger
             if "CPT_C" not in document.keys():
                 continue
             available_cpt_objects.append(CPTCharacteristics(document["CPT_C"]))
         return available_cpt_objects
     response.raise_for_status()
 
 
-def get_cpt_object(
-    bro_cpt_id: str,
-    as_dict: bool = False
-) -> Union[bytes, dict]:
-    """ Performs GET request on BRO API to retrieve a CPT object.
+def get_cpt_object(bro_cpt_id: str, as_dict: bool = False) -> Union[bytes, dict]:
+    """Performs GET request on BRO API to retrieve a CPT object.
 
     :param bro_cpt_id: BRO CPT ID in str format, retrievable from CPTCharacteristics
     :param as_dict: bool indicating whether the returned xml in bytes format needs to be parsed to dict.
     :return: XML bytes CPT file directly from BRO REST API or dict of given XML file
     """
     headers = {
         "accept": "application/xml",
     }
 
     response = requests.get(
-        f"{CPT_OBJECT_URL}{bro_cpt_id}?requestReference={REQUEST_REFERENCE}",
-        headers=headers,
+        f"{CPT_OBJECT_URL}{bro_cpt_id}?requestReference={REQUEST_REFERENCE}", headers=headers, timeout=10
     )
-    # Check status code, 200 -> xml, 400 -> json
+    # TODO: Check status codes in BRO REST API documentation.
     if response.status_code == 200:
         if as_dict:
             return IMBROFile(response.content).parse()
         return response.content
     response.raise_for_status()
```

### Comparing `bro-0.2.1rc5/bro/helper_functions.py` & `bro-0.2.3/bro/helper_functions.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,27 +8,22 @@
     :param s: int, str, float
     :return: bool
     """
     return str(s).lower() in ("ja", "yes", "true", "t", "1")
 
 
 def construct_geojson_from_characteristics(
-        characteristics: List,
-        area=None,
+    characteristics: List,
+    area=None,
 ) -> str:
     """Generates a str containing a valid geojson structure from separate objects.
 
     :param characteristics: List of CPTCharacteristics objects
     :param area: Envelope. Circle are not yet supported
     :return: str in geojson format that contains of requested area + available objects in that area
     """
     # TODO: Add Circle area as polygon, Circle with shapely?
 
     features = [characteristic.to_geojson_feature for characteristic in characteristics]
     features += [area.to_geojson_feature]
 
-    return json.dumps(
-        {
-            "type": "FeatureCollection",
-            "features": features
-        }
-    )
+    return json.dumps({"type": "FeatureCollection", "features": features})
```

### Comparing `bro-0.2.1rc5/bro/objects.py` & `bro-0.2.3/bro/objects.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 from lxml import etree
 
 
 class IMBROFile:
     """
     Class to handle paring of BRO XML files, currently working for the CPT API.
     """
+
     def __init__(self, file_content: bytes):
         self.file_content = file_content
 
     @classmethod
     def from_file(cls, file_path: Union[str, Path]) -> "IMBROFile":
         """Instantiates the IMBROFile class from a file_path to an IMBRO xml file."""
         with Path(file_path).open("rb") as xml_file:
@@ -35,13 +36,12 @@
             return node.text
 
         grand_children = {}
         for child in node.getchildren():
             tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
             if tag == "parameters":
                 grand_children["parameters"] = [
-                    (sub_child.tag.split("}")[-1], sub_child.text in {"ja", 1})
-                    for sub_child in child
+                    (sub_child.tag.split("}")[-1], sub_child.text in {"ja", 1}) for sub_child in child
                 ]
             else:
                 grand_children[tag] = cls._parse_xml_to_dict_recursively(child)
         return grand_children
```

### Comparing `bro-0.2.1rc5/bro.egg-info/PKG-INFO` & `bro-0.2.3/bro.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 Metadata-Version: 2.1
 Name: bro
-Version: 0.2.1rc5
+Version: 0.2.3
 Summary: Open source python library for accessing BRO API
 Home-page: https://github.com/viktor-platform/bro
 Author: VIKTOR
 Author-email: support@viktor.ai
 License: see LICENSE.txt
+Project-URL: Example VIKTOR application, https://demo.viktor.ai/public/bro-app
+Project-URL: Source code VIKTOR application, https://github.com/viktor-platform/bro-app
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: License :: Free To Use But Restricted
 Classifier: Operating System :: Microsoft :: Windows
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
-![](https://img.shields.io/badge/release-v0.2.1rc5-green)
+![](https://img.shields.io/badge/release-v0.2.3-green)
 
 # BRO
 This package can access the REST API from the [BRO](https://www.broloket.nl/ondergrondgegevens). Currently, this package provides
 functionality to request CPTs from the BRO when you provide a region of interest. The format is based on the REST API of the BRO, which is described [here](https://publiek.broservices.nl/sr/cpt/v1/swagger-ui/#/default/) for CPTs.
 
 Current options include retrieval of the following objects: 
 1. CPTs (format: bytes, dict)
```

### Comparing `bro-0.2.1rc5/examples/examples.py` & `bro-0.2.3/examples/examples.py`

 * *Files identical despite different names*

### Comparing `bro-0.2.1rc5/setup.py` & `bro-0.2.3/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,48 +1,50 @@
-from setuptools import setup, find_packages
 from pathlib import Path
 
+from setuptools import find_packages
+from setuptools import setup
+
 about = {}
-with open(Path(__file__).parent / 'bro' / '__version__.py', 'r') as f:
+with open(Path(__file__).parent / "bro" / "__version__.py", "r") as f:
     exec(f.read(), about)
 
-license_content = (Path(__file__).parent / 'LICENSE.txt').read_text()
-long_description = (Path(__file__).parent / 'README.md').read_text()
-long_description = long_description.replace('X.Y.Z', about['__version__'])
-long_description = long_description.replace('LICENSE-PLACEHOLDER', license_content)
+license_content = (Path(__file__).parent / "LICENSE.txt").read_text()
+long_description = (Path(__file__).parent / "README.md").read_text()
+long_description = long_description.replace("X.Y.Z", about["__version__"])
+long_description = long_description.replace("LICENSE-PLACEHOLDER", license_content)
 
 setup(
-    name='bro',
-    version=about['__version__'],
-    description='Open source python library for accessing BRO API',
+    name="bro",
+    version=about["__version__"],
+    description="Open source python library for accessing BRO API",
     long_description=long_description,
     long_description_content_type="text/markdown",
-    url='https://github.com/viktor-platform/bro',
-    author='VIKTOR',
-    author_email='support@viktor.ai',
-    license='see LICENSE.txt',
-    license_files=('LICENSE.txt',),
-    packages=find_packages(exclude=['tests']),
+    url="https://github.com/viktor-platform/bro",
+    author="VIKTOR",
+    author_email="support@viktor.ai",
+    license="see LICENSE.txt",
+    license_files=("LICENSE.txt",),
+    packages=find_packages(exclude=["tests"]),
     install_requires=[
         "xmltodict==0.13.0",
         "requests==2.28.2",
         "lxml==4.9.2",
-        "pyproj==3.4.1"
+        "pyproj==3.4.1",
     ],
     classifiers=[
-        'Environment :: Web Environment',
-        'Intended Audience :: Developers',
-        'License :: Free To Use But Restricted',
-        'Operating System :: Microsoft :: Windows',
-        'Operating System :: POSIX :: Linux',
-        'Programming Language :: Python :: 3.7',
-        'Programming Language :: Python :: 3.8',
-        'Programming Language :: Python :: 3.9',
-        'Programming Language :: Python :: 3.10',
-        'Programming Language :: Python :: 3.11',
+        "Environment :: Web Environment",
+        "Intended Audience :: Developers",
+        "License :: Free To Use But Restricted",
+        "Operating System :: Microsoft :: Windows",
+        "Operating System :: POSIX :: Linux",
+        "Programming Language :: Python :: 3.7",
+        "Programming Language :: Python :: 3.8",
+        "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
     ],
-    test_suite='tests',
-    # project_urls={
-    #     'Example VIKTOR application': '',  # TODO: update
-    #     'Source code example VIKTOR application': '',  # TODO: update
-    # }
+    test_suite="tests",
+    project_urls={
+        "Example VIKTOR application": "https://demo.viktor.ai/public/bro-app",
+        "Source code VIKTOR application": "https://github.com/viktor-platform/bro-app",
+    },
 )
```

### Comparing `bro-0.2.1rc5/tests/test_api.py` & `bro-0.2.3/tests/test_api.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,19 @@
 import json
 import unittest
 from datetime import datetime
-
 from pathlib import Path
 
-from bro import Point, RDPoint, Circle, Envelope, get_cpt_object, get_cpt_characteristics, \
-    get_cpt_characteristics_and_return_cpt_objects
+from bro import Circle
+from bro import Envelope
+from bro import Point
+from bro import RDPoint
+from bro import get_cpt_characteristics
+from bro import get_cpt_characteristics_and_return_cpt_objects
+from bro import get_cpt_object
 
 
 class TestPoint(unittest.TestCase):
     def setUp(self):
         self.wgs = Point(lat=51.998929, lon=4.375587)
         self.rd = RDPoint(x=85530.20712412785, y=446100.1761217844)
 
@@ -33,37 +37,29 @@
         self.circle = Circle(Point(lat=52.038297852, lon=5.31447958948), radius=0.5)
 
     def test_bro_json_property_has_correct_format(self):
         bro_json_actual = self.circle.bro_json
 
         bro_json_expected = {
             "enclosingCircle": {
-                "center": {
-                    "lat": 52.038297852,
-                    "lon": 5.31447958948
-                },
-                "radius": 0.5
+                "center": {"lat": 52.038297852, "lon": 5.31447958948},
+                "radius": 0.5,
             }
         }
 
         self.assertEqual(bro_json_actual, bro_json_expected)
 
     def test_to_geojson_feature_returns_correct_format(self):
         actual_geojson_feature = self.circle.to_geojson_feature
 
         expected_geojson_feature = {
-                "type": "Feature",
-                "geometry": {
-                    "type": "Point",
-                    "coordinates": [5.31447958948, 52.038297852]
-                },
-                "properties": {
-                    "description": f"Requested centroid"
-                }
-            }
+            "type": "Feature",
+            "geometry": {"type": "Point", "coordinates": [5.31447958948, 52.038297852]},
+            "properties": {"description": f"Requested centroid"},
+        }
 
         self.assertEqual(actual_geojson_feature, expected_geojson_feature)
 
 
 class TestEnvelope(unittest.TestCase):
     def setUp(self):
         self.envelope = Envelope(
@@ -92,41 +88,42 @@
     def test_to_geojson_feature_returns_correct_format(self):
         actual_geojson_feature = self.envelope.to_geojson_feature
 
         expected_geojson_feature = {
             "type": "Feature",
             "geometry": {
                 "type": "Polygon",
-                "coordinates": [[
-                    [4.469594207611851, 51.92269686635185],
-                    [4.470094707426648, 51.92269686635185],
-                    [4.470094707426648, 51.923034432171065],
-                    [4.469594207611851, 51.923034432171065],
-                    [4.469594207611851, 51.92269686635185],
-                ]
-                ]
+                "coordinates": [
+                    [
+                        [4.469594207611851, 51.92269686635185],
+                        [4.470094707426648, 51.92269686635185],
+                        [4.470094707426648, 51.923034432171065],
+                        [4.469594207611851, 51.923034432171065],
+                        [4.469594207611851, 51.92269686635185],
+                    ]
+                ],
             },
-            "properties": {
-                "description": f"Requested area"
-            }
+            "properties": {"description": f"Requested area"},
         }
 
         self.assertEqual(actual_geojson_feature, expected_geojson_feature)
 
 
 class TestAPI(unittest.TestCase):
-
     def test_get_cpt_object(self):
         bro_cpt_id = "CPT000000053405"
-        response = get_cpt_object(bro_cpt_id,  as_dict=True)
+        response = get_cpt_object(bro_cpt_id, as_dict=True)
 
         with open(Path(__file__).parent / "response_CPT000000053405.json", "r") as f:
             expected_response = json.load(f)
 
-        self.assertEqual(json.dumps(response["dispatchDocument"]), json.dumps(expected_response["dispatchDocument"]))
+        self.assertEqual(
+            json.dumps(response["dispatchDocument"]),
+            json.dumps(expected_response["dispatchDocument"]),
+        )
 
     def test_get_cpt_characteristics_returns_correct_amount_of_results(self):
         # If the BRO gets updated the amount of available cpts in this area may change. As of 17/03/2023 this is valid.
 
         # Arrange
         begin_date = datetime(2015, 1, 1).strftime("%Y-%m-%d")
         end_date = datetime(2023, 3, 3).strftime("%Y-%m-%d")
@@ -138,15 +135,17 @@
         # Act
         response = get_cpt_characteristics(begin_date, end_date, area=envelope)
         amount_of_available_cpts = 5
 
         # Assert
         self.assertEqual(len(response), amount_of_available_cpts)
 
-    def test_get_cpt_characteristics_and_return_cpt_objects_returns_correct_result_type(self):
+    def test_get_cpt_characteristics_and_return_cpt_objects_returns_correct_result_type(
+        self,
+    ):
         # Arrange
         begin_date = datetime(2015, 1, 1).strftime("%Y-%m-%d")
         end_date = datetime(2023, 3, 3).strftime("%Y-%m-%d")
 
         lower_corner = Point(51.92269686635185, 4.469594207611851)
         upper_corner = Point(51.923034432171065, 4.470094707426648)
         envelope = Envelope(lower_corner, upper_corner)
```

