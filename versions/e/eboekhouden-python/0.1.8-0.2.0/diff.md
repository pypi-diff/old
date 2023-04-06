# Comparing `tmp/eboekhouden_python-0.1.8.tar.gz` & `tmp/eboekhouden_python-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "eboekhouden_python-0.1.8.tar", max compression
+gzip compressed data, was "eboekhouden_python-0.2.0.tar", max compression
```

## Comparing `eboekhouden_python-0.1.8.tar` & `eboekhouden_python-0.2.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1071 2023-04-03 11:53:59.399776 eboekhouden_python-0.1.8/LICENSE
--rw-r--r--   0        0        0     1200 2023-04-03 11:41:12.021970 eboekhouden_python-0.1.8/README.md
--rw-r--r--   0        0        0      228 2023-04-06 13:32:48.446749 eboekhouden_python-0.1.8/eboekhouden_python/__init__.py
--rw-r--r--   0        0        0      399 2023-04-06 13:05:26.446485 eboekhouden_python-0.1.8/eboekhouden_python/constants/__init__.py
--rw-r--r--   0        0        0      247 2023-04-03 16:59:40.940120 eboekhouden_python-0.1.8/eboekhouden_python/constants/bedrijf_particulier.py
--rw-r--r--   0        0        0     1964 2023-04-03 14:17:12.994123 eboekhouden_python-0.1.8/eboekhouden_python/constants/btw_code.py
--rw-r--r--   0        0        0      272 2023-04-03 13:40:19.527704 eboekhouden_python-0.1.8/eboekhouden_python/constants/in_ex_btw.py
--rw-r--r--   0        0        0      623 2023-04-05 19:46:16.173697 eboekhouden_python-0.1.8/eboekhouden_python/constants/mutatie_soort.py
--rw-r--r--   0        0        0      235 2023-04-03 14:17:30.188459 eboekhouden_python-0.1.8/eboekhouden_python/constants/string_enum.py
--rw-r--r--   0        0        0     5180 2023-04-03 20:02:13.785039 eboekhouden_python-0.1.8/eboekhouden_python/eboekhouden_client.py
--rw-r--r--   0        0        0      312 2023-04-06 13:05:08.348133 eboekhouden_python-0.1.8/eboekhouden_python/models/__init__.py
--rw-r--r--   0        0        0     4432 2023-04-05 20:07:24.969738 eboekhouden_python-0.1.8/eboekhouden_python/models/mutatie.py
--rw-r--r--   0        0        0     1361 2023-04-03 17:08:37.346890 eboekhouden_python-0.1.8/eboekhouden_python/models/mutatie_filter.py
--rw-r--r--   0        0        0     2397 2023-04-04 06:03:35.645610 eboekhouden_python-0.1.8/eboekhouden_python/models/mutatie_regel.py
--rw-r--r--   0        0        0     4568 2023-04-04 06:03:35.668723 eboekhouden_python-0.1.8/eboekhouden_python/models/relatie.py
--rw-r--r--   0        0        0      735 2023-04-03 19:45:53.253119 eboekhouden_python-0.1.8/eboekhouden_python/models/relatie_filter.py
--rw-r--r--   0        0        0      954 2023-04-06 13:30:29.409900 eboekhouden_python-0.1.8/pyproject.toml
--rw-r--r--   0        0        0     2006 1970-01-01 00:00:00.000000 eboekhouden_python-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-03 11:53:59.399776 eboekhouden_python-0.2.0/LICENSE
+-rw-r--r--   0        0        0     1200 2023-04-03 11:41:12.021970 eboekhouden_python-0.2.0/README.md
+-rw-r--r--   0        0        0      228 2023-04-06 15:47:57.826745 eboekhouden_python-0.2.0/eboekhouden_python/__init__.py
+-rw-r--r--   0        0        0      399 2023-04-06 13:05:26.446485 eboekhouden_python-0.2.0/eboekhouden_python/constants/__init__.py
+-rw-r--r--   0        0        0      247 2023-04-03 16:59:40.940120 eboekhouden_python-0.2.0/eboekhouden_python/constants/bedrijf_particulier.py
+-rw-r--r--   0        0        0     1964 2023-04-03 14:17:12.994123 eboekhouden_python-0.2.0/eboekhouden_python/constants/btw_code.py
+-rw-r--r--   0        0        0      272 2023-04-03 13:40:19.527704 eboekhouden_python-0.2.0/eboekhouden_python/constants/in_ex_btw.py
+-rw-r--r--   0        0        0      623 2023-04-05 19:46:16.173697 eboekhouden_python-0.2.0/eboekhouden_python/constants/mutatie_soort.py
+-rw-r--r--   0        0        0      235 2023-04-03 14:17:30.188459 eboekhouden_python-0.2.0/eboekhouden_python/constants/string_enum.py
+-rw-r--r--   0        0        0     6020 2023-04-06 15:49:12.622768 eboekhouden_python-0.2.0/eboekhouden_python/eboekhouden_client.py
+-rw-r--r--   0        0        0      312 2023-04-06 13:05:08.348133 eboekhouden_python-0.2.0/eboekhouden_python/models/__init__.py
+-rw-r--r--   0        0        0     5934 2023-04-06 15:49:12.618138 eboekhouden_python-0.2.0/eboekhouden_python/models/mutatie.py
+-rw-r--r--   0        0        0     1367 2023-04-06 15:47:35.030825 eboekhouden_python-0.2.0/eboekhouden_python/models/mutatie_filter.py
+-rw-r--r--   0        0        0     3213 2023-04-06 15:49:12.601254 eboekhouden_python-0.2.0/eboekhouden_python/models/mutatie_regel.py
+-rw-r--r--   0        0        0     7280 2023-04-06 15:49:29.359054 eboekhouden_python-0.2.0/eboekhouden_python/models/relatie.py
+-rw-r--r--   0        0        0      741 2023-04-06 15:47:44.663894 eboekhouden_python-0.2.0/eboekhouden_python/models/relatie_filter.py
+-rw-r--r--   0        0        0      954 2023-04-06 15:48:44.271771 eboekhouden_python-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0     2006 1970-01-01 00:00:00.000000 eboekhouden_python-0.2.0/PKG-INFO
```

### Comparing `eboekhouden_python-0.1.8/LICENSE` & `eboekhouden_python-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.8/README.md` & `eboekhouden_python-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/constants/btw_code.py` & `eboekhouden_python-0.2.0/eboekhouden_python/constants/btw_code.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/constants/mutatie_soort.py` & `eboekhouden_python-0.2.0/eboekhouden_python/constants/mutatie_soort.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/eboekhouden_client.py` & `eboekhouden_python-0.2.0/eboekhouden_python/eboekhouden_client.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 """Eboekhouden client."""
-from typing import Optional
+from typing import Optional, Any
 import os
 
 from zeep import Client as ZeepClient
 
 from .models import (
     MutatieFilter,
     Mutatie,
@@ -73,16 +73,21 @@
         self,
         mutatie_nummer: Optional[str] = None,
         mutatie_nummer_van: Optional[str] = None,
         mutatie_nummer_totmet: Optional[str] = None,
         factuur_nummer: Optional[str] = None,
         datum_van: Optional[str] = None,
         datum_totmet: Optional[str] = None,
-    ) -> list[dict]:
-        """Get mutaties."""
+        return_zeep_object: bool = False,
+    ) -> list[Any]:
+        """
+        Get mutaties.
+
+        Returns a zeep.objects.cMutatieList, might want to convert to Relatie
+        """
         mutatie_filter = MutatieFilter(
             mutatie_nummer=mutatie_nummer,
             mutatie_nummer_van=mutatie_nummer_van,
             mutatie_nummer_totmet=mutatie_nummer_totmet,
             factuur_nummer=factuur_nummer,
             datum_van=datum_van,
             datum_totmet=datum_totmet,
@@ -97,15 +102,19 @@
         )
 
         self._check_response(mutaties)
 
         if mutaties["Mutaties"] is None:
             return []
 
-        return mutaties["Mutaties"]["cMutatieList"]
+        if return_zeep_object:
+            return mutaties["Mutaties"]["cMutatieList"]
+
+        mutatie_objects = [Mutatie.from_zeep(x) for x in mutaties["Mutaties"]["cMutatieList"]]
+        return mutatie_objects
 
     def add_mutatie(self, mutatie: Mutatie) -> str:
         """Add mutatie."""
         self.get_session_id()
 
         exported_mutatie = mutatie.export()
 
@@ -123,20 +132,17 @@
         return response["Mutatienummer"]
 
     def get_relaties(
         self,
         trefwoord: Optional[str] = None,
         relatie_code: Optional[str] = None,
         id: Optional[int] = None,
-    ) -> list[dict]:
-        """
-        Get relaties.
-
-        Results are capped to maximum of 100 records.
-        """
+        return_zeep_object: bool = False,
+    ) -> list[Any]:
+        """Get relaties."""
         relatie_filter = RelatieFilter(trefwoord=trefwoord, code=relatie_code, id=id)
 
         self.get_session_id()
 
         relaties = self._client.service.GetRelaties(
             SessionID=self._session_id,
             SecurityCode2=self._code2,
@@ -144,15 +150,19 @@
         )
 
         self._check_response(relaties)
 
         if relaties["Relaties"] is None:
             return []
 
-        return relaties["Relaties"]["cRelatie"]
+        if return_zeep_object:
+            return relaties["Relaties"]["cRelatie"]
+
+        relatie_objects = [Relatie.from_zeep(x) for x in relaties["Relaties"]["cRelatie"]]
+        return relatie_objects
 
     def add_relatie(self, relatie: Relatie) -> str:
         """Add mutatie."""
         self.get_session_id()
 
         response = self._client.service.AddRelatie(
             SessionID=self._session_id,
@@ -162,7 +172,16 @@
 
         self._check_response(response)
 
         if response["Rel_ID"] is None:
             raise ValueError("Error adding mutatie")
 
         return response["Rel_ID"]
+
+    def mutatie_exists(self, mutatie: Mutatie) -> bool:
+        """Check if mutatie already exists in E-boekhouden by matching the date and omschrijving."""
+        found_mutaties = self.get_mutaties(
+            datum_van=mutatie.datum,
+            datum_totmet=mutatie.datum,
+        )
+        omschrijvingen = [x.omschrijving for x in found_mutaties]
+        return mutatie.omschrijving in omschrijvingen
```

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/models/mutatie_filter.py` & `eboekhouden_python-0.2.0/eboekhouden_python/models/mutatie_filter.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """Model for GetMutaties filter in e-Boekhouden.nl."""
 from dataclasses import dataclass
 from typing import Optional
 
-from zeep.xsd import SkipValue as ZeepXsdSkipValue
+from zeep.xsd.const import SkipValue as ZeepXsdSkipValue
 
 
 @dataclass
 class MutatieFilter:
     """Filter for GetMutaties in e-Boekhouden."""
 
     mutatie_nummer: Optional[str] = None
```

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/models/mutatie_regel.py` & `eboekhouden_python-0.2.0/eboekhouden_python/models/mutatie_regel.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 """Row in a Mutatie of E-boekhouden.nl."""
 from dataclasses import dataclass
 from typing import Optional
+from collections import OrderedDict
 
-from zeep.xsd import SkipValue as ZeepXsdSkipValue
+from zeep.xsd.const import SkipValue as ZeepXsdSkipValue
 
 from ..constants import BtwCode, btw_codes_hoog, btw_codes_laag, btw_codes_geen
 
 
 @dataclass
 class MutatieRegel:
     """Row in a Mutatie of E-boekhouden.nl."""
@@ -17,14 +18,32 @@
     bedrag_inclusief_btw: str  # Decimal
     btw_code: str  # String
     btw_percentage: str  # Decimal
     tegenrekening_code: str  # String
     kostenplaats_id: Optional[str] = None  # Int
 
     @classmethod
+    def from_zeep(
+        cls,
+        zeep_mutatie_regel_object: OrderedDict,
+    ) -> "MutatieRegel":
+        """Create a MutatieRegel from a zeep object."""
+        short = zeep_mutatie_regel_object
+        return cls(
+            bedrag_invoer=f"{short.get('BedragInvoer'):.2f}",
+            bedrag_exclusief_btw=f"{short.get('BedragExclBTW'):.2f}",
+            bedrag_btw=f"{short.get('BedragBTW'):.2f}",
+            bedrag_inclusief_btw=f"{short.get('BedragInclBTW'):.2f}",
+            btw_code=f"{short.get('BTWCode')}",
+            btw_percentage=f"{int(short.get('BTWPercentage'))}",  # type: ignore
+            tegenrekening_code=short.get("TegenrekeningCode"),  # type: ignore
+            kostenplaats_id=short.get("KostenplaatsID"),
+        )
+
+    @classmethod
     def from_bedrag(
         cls,
         bedrag_invoer: float,
         btw_code: BtwCode,
         tegenrekening_code: str,
     ) -> "MutatieRegel":
         """Create a MutatieRegel from amount including vat using BtwCode."""
```

### Comparing `eboekhouden_python-0.1.8/eboekhouden_python/models/relatie_filter.py` & `eboekhouden_python-0.2.0/eboekhouden_python/models/relatie_filter.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """Model for GetMutaties filter in e-Boekhouden.nl."""
 from dataclasses import dataclass
 from typing import Optional
 
-from zeep.xsd import SkipValue as ZeepXsdSkipValue
+from zeep.xsd.const import SkipValue as ZeepXsdSkipValue
 
 
 @dataclass
 class RelatieFilter:
     """
     Filter for GetRelaties in e-Boekhouden.nl.
```

### Comparing `eboekhouden_python-0.1.8/pyproject.toml` & `eboekhouden_python-0.2.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "eboekhouden-python"
-version = "0.1.8"
+version = "0.2.0"
 description = "This is a simple API client for the E-boekhouden.nl API. It is written in Python and uses the ZEEP library."
 authors = ["Dennis Bakhuis <pypi@bakhuis.nu>"]
 readme = "README.md"
 packages = [{include = "eboekhouden_python"}]
 license = "MIT"
 homepage = "https://github.com/dennisbakhuis/eboekhouden-python"
 repository = "https://github.com/dennisbakhuis/eboekhouden-python"
```

### Comparing `eboekhouden_python-0.1.8/PKG-INFO` & `eboekhouden_python-0.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eboekhouden-python
-Version: 0.1.8
+Version: 0.2.0
 Summary: This is a simple API client for the E-boekhouden.nl API. It is written in Python and uses the ZEEP library.
 Home-page: https://github.com/dennisbakhuis/eboekhouden-python
 License: MIT
 Keywords: e-boekhouden,eboekhouden,api,zeep,soap,client,python
 Author: Dennis Bakhuis
 Author-email: pypi@bakhuis.nu
 Requires-Python: >=3.9,<4.0
```

