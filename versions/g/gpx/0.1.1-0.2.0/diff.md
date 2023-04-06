# Comparing `tmp/gpx-0.1.1.tar.gz` & `tmp/gpx-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gpx-0.1.1.tar", last modified: Fri Mar 31 22:04:26 2023, max compression
+gzip compressed data, was "gpx-0.2.0.tar", last modified: Thu Apr  6 12:09:16 2023, max compression
```

## Comparing `gpx-0.1.1.tar` & `gpx-0.2.0.tar`

### file list

```diff
@@ -1,29 +1,38 @@
--rw-r--r--   0        0        0      376 2023-03-31 22:04:18.425997 gpx-0.1.1/.editorconfig
--rw-r--r--   0        0        0       66 2023-03-31 22:04:18.425997 gpx-0.1.1/.gitattributes
--rw-r--r--   0        0        0      731 2023-03-31 22:04:18.425997 gpx-0.1.1/.github/workflows/publish.yml
--rw-r--r--   0        0        0     3078 2023-03-31 22:04:18.425997 gpx-0.1.1/.gitignore
--rw-r--r--   0        0        0     1655 2023-03-31 22:04:18.425997 gpx-0.1.1/.pre-commit-config.yaml
--rw-r--r--   0        0        0      198 2023-03-31 22:04:18.425997 gpx-0.1.1/.readthedocs.yaml
--rw-r--r--   0        0        0       57 2023-03-31 22:04:18.425997 gpx-0.1.1/.vscode/extensions.json
--rw-r--r--   0        0        0    35884 2023-03-31 22:04:18.425997 gpx-0.1.1/LICENSE
--rw-r--r--   0        0        0     2117 2023-03-31 22:04:18.425997 gpx-0.1.1/README.md
--rw-r--r--   0        0        0      715 2023-03-31 22:04:18.425997 gpx-0.1.1/docs/Makefile
--rw-r--r--   0        0        0      506 2023-03-31 22:04:18.425997 gpx-0.1.1/docs/api.md
--rw-r--r--   0        0        0      781 2023-03-31 22:04:18.425997 gpx-0.1.1/docs/changelog.md
--rw-r--r--   0        0        0     1434 2023-03-31 22:04:18.425997 gpx-0.1.1/docs/conf.py
--rw-r--r--   0        0        0      322 2023-03-31 22:04:18.429997 gpx-0.1.1/docs/index.md
--rw-r--r--   0        0        0      153 2023-03-31 22:04:18.429997 gpx-0.1.1/docs/installation.md
--rw-r--r--   0        0        0      765 2023-03-31 22:04:18.429997 gpx-0.1.1/docs/make.bat
--rw-r--r--   0        0        0      132 2023-03-31 22:04:18.429997 gpx-0.1.1/docs/usage.md
--rw-r--r--   0        0        0     1561 2023-03-31 22:04:18.429997 gpx-0.1.1/pyproject.toml
--rw-r--r--   0        0        0      399 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/__init__.py
--rw-r--r--   0        0        0      674 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/_parsers.py
--rw-r--r--   0        0        0      110 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/errors.py
--rw-r--r--   0        0        0    12275 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/gpx.py
--rw-r--r--   0        0        0    25872 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/gpx.xsd
--rw-r--r--   0        0        0        0 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/py.typed
--rw-r--r--   0        0        0     4368 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/route.py
--rw-r--r--   0        0        0     5578 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/track.py
--rw-r--r--   0        0        0      370 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/utils.py
--rw-r--r--   0        0        0    11036 2023-03-31 22:04:18.429997 gpx-0.1.1/src/gpx/waypoint.py
--rw-r--r--   0        0        0     3755 1970-01-01 00:00:00.000000 gpx-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      376 2023-04-06 12:09:03.581236 gpx-0.2.0/.editorconfig
+-rw-r--r--   0        0        0       66 2023-04-06 12:09:03.581236 gpx-0.2.0/.gitattributes
+-rw-r--r--   0        0        0      731 2023-04-06 12:09:03.581236 gpx-0.2.0/.github/workflows/publish.yml
+-rw-r--r--   0        0        0     3078 2023-04-06 12:09:03.581236 gpx-0.2.0/.gitignore
+-rw-r--r--   0        0        0     1655 2023-04-06 12:09:03.581236 gpx-0.2.0/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      198 2023-04-06 12:09:03.581236 gpx-0.2.0/.readthedocs.yaml
+-rw-r--r--   0        0        0       57 2023-04-06 12:09:03.581236 gpx-0.2.0/.vscode/extensions.json
+-rw-r--r--   0        0        0    35884 2023-04-06 12:09:03.581236 gpx-0.2.0/LICENSE
+-rw-r--r--   0        0        0     2117 2023-04-06 12:09:03.581236 gpx-0.2.0/README.md
+-rw-r--r--   0        0        0      715 2023-04-06 12:09:03.581236 gpx-0.2.0/docs/Makefile
+-rw-r--r--   0        0        0     1574 2023-04-06 12:09:03.581236 gpx-0.2.0/docs/api.md
+-rw-r--r--   0        0        0     2573 2023-04-06 12:09:03.581236 gpx-0.2.0/docs/changelog.md
+-rw-r--r--   0        0        0     1528 2023-04-06 12:09:03.585236 gpx-0.2.0/docs/conf.py
+-rw-r--r--   0        0        0      322 2023-04-06 12:09:03.585236 gpx-0.2.0/docs/index.md
+-rw-r--r--   0        0        0      153 2023-04-06 12:09:03.585236 gpx-0.2.0/docs/installation.md
+-rw-r--r--   0        0        0      765 2023-04-06 12:09:03.585236 gpx-0.2.0/docs/make.bat
+-rw-r--r--   0        0        0      132 2023-04-06 12:09:03.585236 gpx-0.2.0/docs/usage.md
+-rw-r--r--   0        0        0     1561 2023-04-06 12:09:03.585236 gpx-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0      673 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/__init__.py
+-rw-r--r--   0        0        0     1773 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/bounds.py
+-rw-r--r--   0        0        0     1839 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/copyright.py
+-rw-r--r--   0        0        0     1571 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/element.py
+-rw-r--r--   0        0        0     1059 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/email.py
+-rw-r--r--   0        0        0      172 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/errors.py
+-rw-r--r--   0        0        0     8997 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/gpx.py
+-rw-r--r--   0        0        0    25872 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/gpx.xsd
+-rw-r--r--   0        0        0     1577 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/link.py
+-rw-r--r--   0        0        0     4140 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/metadata.py
+-rw-r--r--   0        0        0     2909 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/mixins.py
+-rw-r--r--   0        0        0     1716 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/person.py
+-rw-r--r--   0        0        0        0 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/py.typed
+-rw-r--r--   0        0        0     4098 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/route.py
+-rw-r--r--   0        0        0     5061 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/track.py
+-rw-r--r--   0        0        0     2471 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/track_segment.py
+-rw-r--r--   0        0        0     3419 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/types.py
+-rw-r--r--   0        0        0      379 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/utils.py
+-rw-r--r--   0        0        0    10652 2023-04-06 12:09:03.585236 gpx-0.2.0/src/gpx/waypoint.py
+-rw-r--r--   0        0        0     3733 1970-01-01 00:00:00.000000 gpx-0.2.0/PKG-INFO
```

### Comparing `gpx-0.1.1/.github/workflows/publish.yml` & `gpx-0.2.0/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/.gitignore` & `gpx-0.2.0/.gitignore`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/.pre-commit-config.yaml` & `gpx-0.2.0/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/LICENSE` & `gpx-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/README.md` & `gpx-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/docs/Makefile` & `gpx-0.2.0/docs/Makefile`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/docs/conf.py` & `gpx-0.2.0/docs/conf.py`

 * *Files 9% similar despite different names*

```diff
@@ -33,14 +33,18 @@
 myst_heading_anchors = 3
 
 intersphinx_mapping = {
     "python": ("https://docs.python.org/3", None),
 }
 
 # move type hints into the description block, instead of the signature
+autodoc_member_order = "bysource"
+autodoc_default_options = {
+    "show-inheritance": True,
+}
 autodoc_typehints = "description"
 autodoc_typehints_description_target = "documented"
 
 # -- Options for HTML output -------------------------------------------------
 # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
 
 html_theme = "furo"
```

### Comparing `gpx-0.1.1/docs/make.bat` & `gpx-0.2.0/docs/make.bat`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/pyproject.toml` & `gpx-0.2.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/src/gpx/gpx.xsd` & `gpx-0.2.0/src/gpx/gpx.xsd`

 * *Files identical despite different names*

### Comparing `gpx-0.1.1/src/gpx/track.py` & `gpx-0.2.0/src/gpx/track.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,94 +1,108 @@
-"""This module provides a Track object to contain GPX routes - an ordered list of points describing a path."""
+"""
+This module provides a Track object to contain GPX routes - an ordered list of
+points describing a path.
+"""
 from __future__ import annotations
 
+from datetime import timedelta
+from typing import Iterator
+
 from lxml import etree
 
-from ._parsers import parse_links
-from .waypoint import Waypoint
+from .element import Element
+from .link import Link
+from .track_segment import TrackSegment
+from .types import Latitude, Longitude
 
 
-class Track:
+class Track(Element):
     """A track class for the GPX data format.
 
+    A track represents an ordered list of points describing a path.
+
     Args:
-        trk: The track XML element. Defaults to `None`.
+        element: The track XML element. Defaults to `None`.
     """
 
-    def __init__(self, trk: etree._Element | None = None) -> None:
-        self._trk: etree._Element = trk
-        self._nsmap: dict[str, str] | None = None
-
-        #: GPS name of track.
-        self.name: str | None = None
-
-        #: GPS comment for track.
-        self.cmt: str | None = None
-
-        #: User description of track.
-        self.desc: str | None = None
+    #: GPS name of track.
+    name: str | None = None
 
-        #: Source of data. Included to give user some idea of reliability and
-        #: accuracy of data.
-        self.src: str | None = None
+    #: GPS comment for track.
+    cmt: str | None = None
 
-        #: Links to external information about track.
-        self.links: list[dict[str, str]] = []
+    #: User description of track.
+    desc: str | None = None
 
-        #: GPS track number.
-        self.number: int | None = None
-
-        #: Type (classification) of track.
-        self.type: str | None = None
-
-        #: A Track Segment holds a list of Track Points which are logically
-        #: connected in order. To represent a single GPS track where GPS
-        #: reception was lost, or the GPS receiver was turned off, start a new
-        #: Track Segment for each continuous span of track data.
-        self.segments: list[list[Waypoint]] = []
-
-        if self._trk is not None:
-            self._parse()
+    #: Source of data. Included to give user some idea of reliability and
+    #: accuracy of data.
+    src: str | None = None
+
+    #: Links to external information about track.
+    links: list[Link] = []
+
+    #: GPS track number.
+    number: int | None = None
+
+    #: Type (classification) of track.
+    type: str | None = None
+
+    #: A Track Segment holds a list of Track Points which are logically
+    #: connected in order. To represent a single GPS track where GPS
+    #: reception was lost, or the GPS receiver was turned off, start a new
+    #: Track Segment for each continuous span of track data.
+    trksegs: list[TrackSegment] = []
+    segments = trksegs  #: Alias of :attr:`trksegs`.
+
+    def __getitem__(self, index: int) -> TrackSegment:
+        """Returns the track segment at the given index."""
+        return self.trksegs[index]
+
+    def __len__(self) -> int:
+        """Returns the number of track segments."""
+        return len(self.trksegs)
+
+    def __iter__(self) -> Iterator[TrackSegment]:
+        """Iterates over the track segments."""
+        yield from self.trksegs
 
     def _parse(self) -> None:
-        # namespaces
-        self._nsmap = self._trk.nsmap
+        super()._parse()
+
+        # assertion to satisfy mypy
+        assert self._element is not None
 
         # name
-        if (name := self._trk.find("name", namespaces=self._nsmap)) is not None:
+        if (name := self._element.find("name", namespaces=self._nsmap)) is not None:
             self.name = name.text
         # comment
-        if (cmt := self._trk.find("cmt", namespaces=self._nsmap)) is not None:
+        if (cmt := self._element.find("cmt", namespaces=self._nsmap)) is not None:
             self.cmt = cmt.text
         # description
-        if (desc := self._trk.find("desc", namespaces=self._nsmap)) is not None:
+        if (desc := self._element.find("desc", namespaces=self._nsmap)) is not None:
             self.desc = desc.text
         # source of data
-        if (src := self._trk.find("src", namespaces=self._nsmap)) is not None:
+        if (src := self._element.find("src", namespaces=self._nsmap)) is not None:
             self.src = src.text
-        # links to additional info
-        self.links = parse_links(self._trk)
+        # links
+        for link in self._element.iterfind("link", namespaces=self._nsmap):
+            self.links.append(Link(link))
         # GPS track number
-        if (number := self._trk.find("number", namespaces=self._nsmap)) is not None:
+        if (number := self._element.find("number", namespaces=self._nsmap)) is not None:
             self.number = int(number.text)
         # track type (classification)
-        if (_type := self._trk.find("type", namespaces=self._nsmap)) is not None:
+        if (_type := self._element.find("type", namespaces=self._nsmap)) is not None:
             self.type = _type.text
 
         # segments
-        for trkseg in self._trk.iterfind("trkseg", namespaces=self._nsmap):
-            self.segments.append(
-                [
-                    Waypoint(trkpt)
-                    for trkpt in trkseg.iterfind("trkpt", namespaces=self._nsmap)
-                ]
-            )
+        for trkseg in self._element.iterfind("trkseg", namespaces=self._nsmap):
+            self.trksegs.append(TrackSegment(trkseg))
 
-    def _build(self) -> etree._Element:  # noqa: C901
-        track = etree.Element("trk", nsmap=self._nsmap)
+    def _build(self, tag: str = "trk") -> etree._Element:
+        track = super()._build(tag)
 
         if self.name is not None:
             name = etree.SubElement(track, "name", nsmap=self._nsmap)
             name.text = self.name
 
         if self.cmt is not None:
             cmt = etree.SubElement(track, "cmt", nsmap=self._nsmap)
@@ -98,59 +112,42 @@
             desc = etree.SubElement(track, "desc", nsmap=self._nsmap)
             desc.text = self.desc
 
         if self.src is not None:
             src = etree.SubElement(track, "src", nsmap=self._nsmap)
             src.text = self.src
 
-        for _link in self.links:
-            link = etree.SubElement(track, "link", nsmap=self._nsmap)
-            link.set("href", _link["href"])
-            if (tag := "text") in _link:
-                text = etree.SubElement(link, tag, nsmap=self._nsmap)
-                text.text = _link[tag]
-            if (tag := "type") in _link:
-                _type = etree.SubElement(link, tag, nsmap=self._nsmap)
-                _type.text = _link[tag]
+        for link in self.links:
+            track.append(link._build())
 
         if self.number is not None:
             number = etree.SubElement(track, "number", nsmap=self._nsmap)
             number.text = self.number
 
         if self.type is not None:
             _type = etree.SubElement(track, "type", nsmap=self._nsmap)
             _type.text = self.type
 
-        for _segment in self.segments:
-            segment = etree.SubElement(track, "trkseg", nsmap=self._nsmap)
-            for _trkpt in _segment:
-                segment.append(_trkpt._build(tag="trkpt"))
+        for segment in self.trksegs:
+            track.append(segment._build())
 
         return track
 
     @property
-    def bounds(self) -> tuple[float, float, float, float]:
-        """Returns the bounds of the track."""
+    def bounds(self) -> tuple[Latitude, Longitude, Latitude, Longitude]:
+        """The bounds of the track."""
         return (
-            min(point.lat for segment in self.segments for point in segment),
-            min(point.lon for segment in self.segments for point in segment),
-            max(point.lat for segment in self.segments for point in segment),
-            max(point.lon for segment in self.segments for point in segment),
+            min(trkpt.lat for trkseg in self.trksegs for trkpt in trkseg),
+            min(trkpt.lon for trkseg in self.trksegs for trkpt in trkseg),
+            max(trkpt.lat for trkseg in self.trksegs for trkpt in trkseg),
+            max(trkpt.lon for trkseg in self.trksegs for trkpt in trkseg),
         )
 
     @property
     def distance(self) -> float:
-        """Returns the distance of the track (in metres)."""
-        _distance = 0.0
-        for segment in self.segments:
-            for i, point in enumerate(segment[:-1]):
-                _distance += point.distance_to(segment[i + 1])
-        return round(_distance, 2)
+        """The distance of the track (in metres)."""
+        return round(sum(trkseg.distance for trkseg in self.trksegs), 2)
 
     @property
-    def duration(self) -> float:
-        """Returns the duration of the track (in seconds)."""
-        _duration = 0.0
-        for segment in self.segments:
-            for i, point in enumerate(segment[:-1]):
-                _duration += point.duration_to(segment[i + 1])
-        return _duration
+    def duration(self) -> timedelta:
+        """The duration of the track (in seconds)."""
+        return sum([trkseg.duration for trkseg in self.trksegs], timedelta())
```

### Comparing `gpx-0.1.1/src/gpx/waypoint.py` & `gpx-0.2.0/src/gpx/waypoint.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,187 +1,191 @@
 """This module provides a Waypoint object to contain GPX waypoints."""
 from __future__ import annotations
 
-import datetime
+from datetime import datetime, timedelta
+from decimal import Decimal
 from math import atan2, cos, radians, sin, sqrt
 
 from dateutil.parser import isoparse
 from lxml import etree
 
-from ._parsers import parse_links
+from .element import Element
+from .link import Link
+from .types import Degrees, DGPSStation, Fix, Latitude, Longitude
 
 
-class Waypoint:
+class Waypoint(Element):
     """A waypoint class for the GPX data format.
 
+    A waypoint represents a waypoint, point of interest, or named feature on a
+    map.
+
     Args:
-        wpt: The waypoint XML element. Defaults to `None`.
+        element: The waypoint XML element. Defaults to `None`.
     """
 
-    def __init__(self, wpt: etree._Element | None = None) -> None:
-        self._wpt: etree._Element = wpt
-        self._nsmap: dict[str, str] | None = None
-
-        #: The latitude of the point. Decimal degrees, WGS84 datum.
-        self.lat: float
+    #: The latitude of the point. Decimal degrees, WGS84 datum.
+    lat: Latitude
 
-        #: The longitude of the point. Decimal degrees, WGS84 datum.
-        self.lon: float
+    #: The longitude of the point. Decimal degrees, WGS84 datum.
+    lon: Longitude
 
-        #: Elevation (in meters) of the point.
-        self.ele: float | None = None
+    #: Elevation (in meters) of the point.
+    ele: Decimal | None = None
 
-        #: Creation/modification timestamp for element. Date and time in are in
-        #: Universal Coordinated Time (UTC), not local time! Conforms to ISO 8601
-        #: specification for date/time representation. Fractional seconds are
-        #: allowed for millisecond timing in tracklogs.
-        self.time: datetime.datetime | None = None
+    #: Creation/modification timestamp for element. Date and time in are in
+    #: Universal Coordinated Time (UTC), not local time! Conforms to ISO 8601
+    #: specification for date/time representation. Fractional seconds are
+    #: allowed for millisecond timing in tracklogs.
+    time: datetime | None = None
 
-        #: Magnetic variation (in degrees) at the point
-        self.magvar: float | None = None
+    #: Magnetic variation (in degrees) at the point
+    magvar: Degrees | None = None
 
-        #: Height (in meters) of geoid (mean sea level) above WGS84 earth
-        #: ellipsoid. As defined in NMEA GGA message.
-        self.geoidheight: float | None = None
+    #: Height (in meters) of geoid (mean sea level) above WGS84 earth
+    #: ellipsoid. As defined in NMEA GGA message.
+    geoidheight: Decimal | None = None
 
-        #: The GPS name of the waypoint. This field will be transferred to and
-        #: from the GPS. GPX does not place restrictions on the length of this
-        #: field or the characters contained in it. It is up to the receiving
-        #: application to validate the field before sending it to the GPS.
-        self.name: str | None = None
+    #: The GPS name of the waypoint. This field will be transferred to and
+    #: from the GPS. GPX does not place restrictions on the length of this
+    #: field or the characters contained in it. It is up to the receiving
+    #: application to validate the field before sending it to the GPS.
+    name: str | None = None
 
-        #: GPS waypoint comment. Sent to GPS as comment.
-        self.cmt: str | None = None
+    #: GPS waypoint comment. Sent to GPS as comment.
+    cmt: str | None = None
 
-        #: A text description of the element. Holds additional information about
-        #: the element intended for the user, not the GPS.
-        self.desc: str | None = None
+    #: A text description of the element. Holds additional information about
+    #: the element intended for the user, not the GPS.
+    desc: str | None = None
 
-        #: Source of data. Included to give user some idea of reliability and
-        #: accuracy of data. "Garmin eTrex", "USGS quad Boston North", e.g.
-        self.src: str | None = None
+    #: Source of data. Included to give user some idea of reliability and
+    #: accuracy of data. "Garmin eTrex", "USGS quad Boston North", e.g.
+    src: str | None = None
 
-        #: Link to additional information about the waypoint.
-        self.links: list[dict[str, str]] = []
+    #: Link to additional information about the waypoint.
+    links: list[Link] = []
 
-        #: Text of GPS symbol name. For interchange with other programs, use the
-        #: exact spelling of the symbol as displayed on the GPS. If the GPS
-        #: abbreviates words, spell them out.
-        self.sym: str | None = None
+    #: Text of GPS symbol name. For interchange with other programs, use the
+    #: exact spelling of the symbol as displayed on the GPS. If the GPS
+    #: abbreviates words, spell them out.
+    sym: str | None = None
 
-        #: Type (classification) of the waypoint.
-        self.type: str | None = None
+    #: Type (classification) of the waypoint.
+    type: str | None = None
 
-        #: Type of GPX fix.
-        self.fix: str | None = None
+    #: Type of GPX fix.
+    fix: Fix | None = None
 
-        #: Number of satellites used to calculate the GPX fix.
-        self.sat: int | None = None
+    #: Number of satellites used to calculate the GPX fix.
+    sat: int | None = None
 
-        #: Horizontal dilution of precision.
-        self.hdop: float | None = None
+    #: Horizontal dilution of precision.
+    hdop: Decimal | None = None
 
-        #: Vertical dilution of precision.
-        self.vdop: float | None = None
+    #: Vertical dilution of precision.
+    vdop: Decimal | None = None
 
-        #: Position dilution of precision.
-        self.pdop: float | None = None
+    #: Position dilution of precision.
+    pdop: Decimal | None = None
 
-        #: Number of seconds since last DGPS update.
-        self.ageofdgpsdata: float | None = None
+    #: Number of seconds since last DGPS update.
+    ageofdgpsdata: Decimal | None = None
 
-        #: ID of DGPS station used in differential correction.
-        self.dgpsid: int | None = None
-
-        if self._wpt is not None:
-            self._parse()
+    #: ID of DGPS station used in differential correction.
+    dgpsid: DGPSStation | None = None
 
     def _parse(self) -> None:  # noqa: C901
-        # namespaces
-        self._nsmap = self._wpt.nsmap
+        super()._parse()
+
+        # assertion to satisfy mypy
+        assert self._element is not None
 
         # required
-        self.lat = float(self._wpt.get("lat"))
-        self.lon = float(self._wpt.get("lon"))
+        self.lat = Latitude(self._element.get("lat"))
+        self.lon = Longitude(self._element.get("lon"))
 
         # position info
         # elevation
-        if (ele := self._wpt.find("ele", namespaces=self._nsmap)) is not None:
-            self.ele = float(ele.text)
+        if (ele := self._element.find("ele", namespaces=self._nsmap)) is not None:
+            self.ele = Decimal(ele.text)
         # time
-        if (time := self._wpt.find("time", namespaces=self._nsmap)) is not None:
+        if (time := self._element.find("time", namespaces=self._nsmap)) is not None:
             self.time = isoparse(time.text)
         # magnetic variation
-        if (magvar := self._wpt.find("magvar", namespaces=self._nsmap)) is not None:
-            self.magvar = float(magvar.text)
+        if (magvar := self._element.find("magvar", namespaces=self._nsmap)) is not None:
+            self.magvar = Degrees(magvar.text)
         # geoid height
         if (
-            geoidheight := self._wpt.find("geoidheight", namespaces=self._nsmap)
+            geoidheight := self._element.find("geoidheight", namespaces=self._nsmap)
         ) is not None:
-            self.geoidheight = float(geoidheight.text)
+            self.geoidheight = Decimal(geoidheight.text)
 
         # description info
         # name
-        if (name := self._wpt.find("name", namespaces=self._nsmap)) is not None:
+        if (name := self._element.find("name", namespaces=self._nsmap)) is not None:
             self.name = name.text
         # comment
-        if (cmt := self._wpt.find("cmt", namespaces=self._nsmap)) is not None:
+        if (cmt := self._element.find("cmt", namespaces=self._nsmap)) is not None:
             self.cmt = cmt.text
         # description
-        if (desc := self._wpt.find("desc", namespaces=self._nsmap)) is not None:
+        if (desc := self._element.find("desc", namespaces=self._nsmap)) is not None:
             self.desc = desc.text
         # source of data
-        if (src := self._wpt.find("src", namespaces=self._nsmap)) is not None:
+        if (src := self._element.find("src", namespaces=self._nsmap)) is not None:
             self.src = src.text
-        # links to additional info
-        self.links = parse_links(self._wpt)
+        # links
+        for link in self._element.iterfind("link", namespaces=self._nsmap):
+            self.links.append(Link(link))
         # GPS symbol name
-        if (sym := self._wpt.find("sym", namespaces=self._nsmap)) is not None:
+        if (sym := self._element.find("sym", namespaces=self._nsmap)) is not None:
             self.sym = sym.text
         # waypoint type (classification)
-        if (_type := self._wpt.find("type", namespaces=self._nsmap)) is not None:
+        if (_type := self._element.find("type", namespaces=self._nsmap)) is not None:
             self.type = _type.text
 
         # accuracy info
         # GPX fix type
-        if (fix := self._wpt.find("fix", namespaces=self._nsmap)) is not None:
-            self.fix = fix.text
+        if (fix := self._element.find("fix", namespaces=self._nsmap)) is not None:
+            self.fix = Fix(fix.text)
         # number of satellites used to calculate the GPX fix
-        if (sat := self._wpt.find("sat", namespaces=self._nsmap)) is not None:
+        if (sat := self._element.find("sat", namespaces=self._nsmap)) is not None:
             self.sat = int(sat.text)
         # horizontal dilution of precision
-        if (hdop := self._wpt.find("hdop", namespaces=self._nsmap)) is not None:
-            self.hdop = float(hdop.text)
+        if (hdop := self._element.find("hdop", namespaces=self._nsmap)) is not None:
+            self.hdop = Decimal(hdop.text)
         # vertical dilution of precision
-        if (vdop := self._wpt.find("vdop", namespaces=self._nsmap)) is not None:
-            self.vdop = float(vdop.text)
+        if (vdop := self._element.find("vdop", namespaces=self._nsmap)) is not None:
+            self.vdop = Decimal(vdop.text)
         # position dilution of precision
-        if (pdop := self._wpt.find("pdop", namespaces=self._nsmap)) is not None:
-            self.pdop = float(pdop.text)
+        if (pdop := self._element.find("pdop", namespaces=self._nsmap)) is not None:
+            self.pdop = Decimal(pdop.text)
         # number of seconds since last DGPS update
         if (
-            ageofdgpsdata := self._wpt.find("ageofdgpsdata", namespaces=self._nsmap)
+            ageofdgpsdata := self._element.find("ageofdgpsdata", namespaces=self._nsmap)
         ) is not None:
-            self.ageofdgpsdata = float(ageofdgpsdata.text)
+            self.ageofdgpsdata = Decimal(ageofdgpsdata.text)
         # DGPS station id used in differential correction
-        if (dgpsid := self._wpt.find("dgpsid", namespaces=self._nsmap)) is not None:
-            self.dgpsid = int(dgpsid.text)
+        if (dgpsid := self._element.find("dgpsid", namespaces=self._nsmap)) is not None:
+            self.dgpsid = DGPSStation(dgpsid.text)
 
-    def _build(self, tag: str | None = "wpt") -> etree._Element:  # noqa: C901
-        waypoint = etree.Element(tag, nsmap=self._nsmap)
+    def _build(self, tag: str = "wpt") -> etree._Element:  # noqa: C901
+        waypoint = super()._build(tag)
         waypoint.set("lat", str(self.lat))
         waypoint.set("lon", str(self.lon))
 
         if self.ele is not None:
             ele = etree.SubElement(waypoint, "ele", nsmap=self._nsmap)
             ele.text = str(self.ele)
 
         if self.time is not None:
             time = etree.SubElement(waypoint, "time", nsmap=self._nsmap)
-            time.text = self.time.isoformat().replace("+00:00", "Z")
+            time.text = self.time.isoformat(
+                timespec="milliseconds" if self.time.microsecond else "seconds"
+            ).replace("+00:00", "Z")
 
         if self.magvar is not None:
             magvar = etree.SubElement(waypoint, "magvar", nsmap=self._nsmap)
             magvar.text = str(self.magvar)
 
         if self.geoidheight is not None:
             geoidheight = etree.SubElement(waypoint, "geoidheight", nsmap=self._nsmap)
@@ -199,23 +203,16 @@
             desc = etree.SubElement(waypoint, "desc", nsmap=self._nsmap)
             desc.text = self.desc
 
         if self.src is not None:
             src = etree.SubElement(waypoint, "src", nsmap=self._nsmap)
             src.text = self.src
 
-        for _link in self.links:
-            link = etree.SubElement(waypoint, "link", nsmap=self._nsmap)
-            link.set("href", _link["href"])
-            if (tag := "text") in _link:
-                text = etree.SubElement(link, tag, nsmap=self._nsmap)
-                text.text = _link[tag]
-            if (tag := "type") in _link:
-                _type = etree.SubElement(link, tag, nsmap=self._nsmap)
-                _type.text = _link[tag]
+        for link in self.links:
+            waypoint.append(link._build())
 
         if self.sym is not None:
             sym = etree.SubElement(waypoint, "sym", nsmap=self._nsmap)
             sym.text = self.sym
 
         if self.type is not None:
             _type = etree.SubElement(waypoint, "type", nsmap=self._nsmap)
@@ -251,15 +248,15 @@
             dgpsid = etree.SubElement(waypoint, "dgpsid", nsmap=self._nsmap)
             dgpsid.text = str(self.dgpsid)
 
         return waypoint
 
     def distance_to(self, other: Waypoint, radius: int = 6_378_137) -> float:
         """Returns the distance to the other waypoint (in metres) using a simple
-        spherical earth model.
+        spherical earth model (haversine formula).
 
         Args:
             other: The other waypoint.
             radius: The radius of the earth (defaults to 6,378,137 metres).
 
         Returns:
             The distance to the other waypoint (in metres).
@@ -271,19 +268,19 @@
         φ2, λ2 = radians(other.lat), radians(other.lon)
         Δφ = φ2 - φ1
         Δλ = λ2 - λ1
         a = sin(Δφ / 2) * sin(Δφ / 2) + cos(φ1) * cos(φ2) * sin(Δλ / 2) * sin(Δλ / 2)
         δ = 2 * atan2(sqrt(a), sqrt(1 - a))
         return R * δ
 
-    def duration_to(self, other: Waypoint) -> float:
-        """Returns the duration to the other waypoint (in seconds).
+    def duration_to(self, other: Waypoint) -> timedelta:
+        """Returns the duration to the other waypoint.
 
         Args:
             other: The other waypoint.
 
         Returns:
-            The duration to the other waypoint (in seconds).
+            The duration to the other waypoint.
         """
         if self.time is None or other.time is None:
-            return 0
-        return (other.time - self.time).total_seconds()
+            return timedelta()
+        return other.time - self.time
```

### Comparing `gpx-0.1.1/PKG-INFO` & `gpx-0.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: gpx
-Version: 0.1.1
-Summary: PyGPX is a Python package that brings support for reading, writing and converting GPX files.
+Version: 0.2.0
+Summary: PyGPX is a Python package that brings support for reading, writing and
 Keywords: gpx,gps,xml
 Author-email: Steven van de Graaf <steven@vandegraaf.xyz>
 Requires-Python: ~=3.7
 Description-Content-Type: text/markdown
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Programming Language :: Python
```

