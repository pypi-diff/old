# Comparing `tmp/observation-0.0.4.tar.gz` & `tmp/observation-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "observation-0.0.4.tar", last modified: Wed Jan  4 21:46:54 2023, max compression
+gzip compressed data, was "observation-0.0.5.tar", last modified: Thu Apr  6 21:14:58 2023, max compression
```

## Comparing `observation-0.0.4.tar` & `observation-0.0.5.tar`

### file list

```diff
@@ -1,28 +1,38 @@
-drwxrwxrwx   0        0        0        0 2023-01-04 21:46:54.221808 observation-0.0.4/
--rw-rw-rw-   0        0        0     1090 2022-10-03 19:26:14.000000 observation-0.0.4/LICENSE.txt
--rw-rw-rw-   0        0        0     1243 2023-01-04 21:46:54.222836 observation-0.0.4/PKG-INFO
--rw-rw-rw-   0        0        0      587 2022-12-18 13:25:04.000000 observation-0.0.4/README.md
-drwxrwxrwx   0        0        0        0 2023-01-04 21:46:54.171384 observation-0.0.4/observation/
--rw-rw-rw-   0        0        0     4545 2023-01-04 20:57:04.000000 observation-0.0.4/observation/__init__.py
--rw-rw-rw-   0        0        0    20068 2023-01-04 21:07:27.000000 observation-0.0.4/observation/esconstante.py
--rw-rw-rw-   0        0        0    23446 2023-01-04 21:07:27.000000 observation-0.0.4/observation/esobservation.py
--rw-rw-rw-   0        0        0    53299 2023-01-04 21:08:22.000000 observation-0.0.4/observation/essearch.py
--rw-rw-rw-   0        0        0    25160 2023-01-04 21:07:27.000000 observation-0.0.4/observation/esvalue.py
--rw-rw-rw-   0        0        0    20836 2022-11-17 15:19:41.000000 observation-0.0.4/observation/esvalue_base.py
--rw-rw-rw-   0        0        0    17164 2023-01-04 21:07:27.000000 observation-0.0.4/observation/iindex.py
--rw-rw-rw-   0        0        0    21363 2023-01-04 21:07:27.000000 observation-0.0.4/observation/iindex_interface.py
--rw-rw-rw-   0        0        0    21793 2023-01-04 21:07:27.000000 observation-0.0.4/observation/iindex_structure.py
--rw-rw-rw-   0        0        0    27965 2023-01-04 21:07:27.000000 observation-0.0.4/observation/ilist.py
--rw-rw-rw-   0        0        0    16420 2023-01-04 21:07:27.000000 observation-0.0.4/observation/ilist_analysis.py
--rw-rw-rw-   0        0        0    25622 2023-01-04 21:07:27.000000 observation-0.0.4/observation/ilist_interface.py
--rw-rw-rw-   0        0        0    28658 2023-01-04 21:07:27.000000 observation-0.0.4/observation/ilist_structure.py
--rw-rw-rw-   0        0        0    22260 2023-01-04 21:07:27.000000 observation-0.0.4/observation/timeslot.py
--rw-rw-rw-   0        0        0    15258 2023-01-04 21:07:27.000000 observation-0.0.4/observation/util.py
-drwxrwxrwx   0        0        0        0 2023-01-04 21:46:54.218138 observation-0.0.4/observation.egg-info/
--rw-rw-rw-   0        0        0     1243 2023-01-04 21:46:53.000000 observation-0.0.4/observation.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      612 2023-01-04 21:46:53.000000 observation-0.0.4/observation.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-01-04 21:46:53.000000 observation-0.0.4/observation.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       34 2023-01-04 21:46:53.000000 observation-0.0.4/observation.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-01-04 21:46:53.000000 observation-0.0.4/observation.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       85 2023-01-04 21:46:54.225951 observation-0.0.4/setup.cfg
--rw-rw-rw-   0        0        0     1163 2023-01-04 21:46:29.000000 observation-0.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:14:58.727543 observation-0.0.5/
+-rw-rw-rw-   0        0        0     1090 2023-03-16 10:25:21.000000 observation-0.0.5/LICENSE.txt
+-rw-rw-rw-   0        0        0     1240 2023-04-06 21:14:58.728043 observation-0.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0      594 2023-03-31 12:47:59.000000 observation-0.0.5/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 21:14:58.471635 observation-0.0.5/observation/
+-rw-rw-rw-   0        0        0     5052 2023-04-06 21:09:51.000000 observation-0.0.5/observation/__init__.py
+-rw-rw-rw-   0        0        0    20150 2023-04-06 21:09:51.000000 observation-0.0.5/observation/esconstante.py
+-rw-rw-rw-   0        0        0    23564 2023-04-06 21:09:51.000000 observation-0.0.5/observation/esobservation.py
+-rw-rw-rw-   0        0        0    57400 2023-04-06 21:09:51.000000 observation-0.0.5/observation/essearch.py
+-rw-rw-rw-   0        0        0    25224 2023-04-06 21:09:51.000000 observation-0.0.5/observation/esvalue.py
+-rw-rw-rw-   0        0        0    21037 2023-04-06 21:09:51.000000 observation-0.0.5/observation/esvalue_base.py
+-rw-rw-rw-   0        0        0    17903 2023-04-06 21:09:51.000000 observation-0.0.5/observation/iindex.py
+-rw-rw-rw-   0        0        0    21922 2023-04-06 21:09:51.000000 observation-0.0.5/observation/iindex_interface.py
+-rw-rw-rw-   0        0        0    22375 2023-04-06 21:09:51.000000 observation-0.0.5/observation/iindex_structure.py
+-rw-rw-rw-   0        0        0    28550 2023-04-06 21:09:51.000000 observation-0.0.5/observation/ilist.py
+-rw-rw-rw-   0        0        0    19220 2023-04-06 21:09:51.000000 observation-0.0.5/observation/ilist_analysis.py
+-rw-rw-rw-   0        0        0    26467 2023-04-06 21:09:51.000000 observation-0.0.5/observation/ilist_interface.py
+-rw-rw-rw-   0        0        0    29277 2023-04-06 21:09:51.000000 observation-0.0.5/observation/ilist_structure.py
+-rw-rw-rw-   0        0        0    22281 2023-04-06 21:09:51.000000 observation-0.0.5/observation/timeslot.py
+-rw-rw-rw-   0        0        0    15425 2023-04-06 21:09:51.000000 observation-0.0.5/observation/util.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:14:58.489559 observation-0.0.5/observation.egg-info/
+-rw-rw-rw-   0        0        0     1240 2023-04-06 21:14:58.000000 observation-0.0.5/observation.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      794 2023-04-06 21:14:58.000000 observation-0.0.5/observation.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 21:14:58.000000 observation-0.0.5/observation.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-04-06 21:14:58.000000 observation-0.0.5/observation.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-06 21:14:58.000000 observation-0.0.5/observation.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       85 2023-04-06 21:14:58.738996 observation-0.0.5/setup.cfg
+-rw-rw-rw-   0        0        0     1204 2023-04-06 21:12:55.000000 observation-0.0.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 21:14:58.726050 observation-0.0.5/tests/
+-rw-rw-rw-   0        0        0      494 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_all.py
+-rw-rw-rw-   0        0        0    38636 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_analysis.py
+-rw-rw-rw-   0        0        0    18977 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_esvalue.py
+-rw-rw-rw-   0        0        0    22505 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_iindex.py
+-rw-rw-rw-   0        0        0    37925 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_ilist.py
+-rw-rw-rw-   0        0        0     4313 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_mongo.py
+-rw-rw-rw-   0        0        0    45172 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_obs.py
+-rw-rw-rw-   0        0        0    16130 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_search.py
+-rw-rw-rw-   0        0        0     4122 2023-03-16 10:25:21.000000 observation-0.0.5/tests/test_slot.py
```

### Comparing `observation-0.0.4/LICENSE.txt` & `observation-0.0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `observation-0.0.4/PKG-INFO` & `observation-0.0.5/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: observation
-Version: 0.0.4
-Summary: environmental data interoperability in Python
+Version: 0.0.5
+Summary: environmental data interoperability
 Home-page: https://github.com/loco-philippe/Environmental-Sensing
 Author: Philippe Thomy
 Author-email: philippe@loco-labs.io
-Keywords: observation,indexed list,development,environmental data
+Keywords: observation,tabular data,development,environmental data
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7, <4
 Description-Content-Type: text/markdown
@@ -17,15 +17,15 @@
 
 # Python package
 The Python package includes 
 - all the connectors associated with the standard ObsJson format,
 - classes Observation, Ilist, Iindex, ESValue, TimeSlot
 ## Python connectors
 The Python connectors are defined :
-- in the [documentation](https://loco-philippe.github.io/observation.html)
+- in the [documentation](https://loco-philippe.github.io/python/observation.html)
 - in the [code](./observation/README.md)  files 
 - in the [examples](./Examples/README.md)
 - in the [validation dataset](./Validation/README.md)
 
 ## Installation
 Observation itself is a pure Python package. It can be installed with pip
```

### Comparing `observation-0.0.4/README.md` & `observation-0.0.5/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Python package
 The Python package includes 
 - all the connectors associated with the standard ObsJson format,
 - classes Observation, Ilist, Iindex, ESValue, TimeSlot
 ## Python connectors
 The Python connectors are defined :
-- in the [documentation](https://loco-philippe.github.io/observation.html)
+- in the [documentation](https://loco-philippe.github.io/python/observation.html)
 - in the [code](./observation/README.md)  files 
 - in the [examples](./Examples/README.md)
 - in the [validation dataset](./Validation/README.md)
 
 ## Installation
 Observation itself is a pure Python package. It can be installed with pip
```

### Comparing `observation-0.0.4/observation/__init__.py` & `observation-0.0.5/observation/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -56,60 +56,60 @@
 
 # Documentation
 
 Documentation is available in other pages :
 
 - The concepts of 'observation', 'indexed list' and 'ES value' are describe in
 [the wiki](https://github.com/loco-philippe/Environmental-Sensing/wiki) and in
-[the presentation](https://github.com/loco-philippe/Environmental-Sensing/tree/main
-/documentation/Ilist_principles.pdf).
+[the presentation](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation/Ilist_principles.pdf).
 - The non-regression tests are at
 [this page](https://github.com/loco-philippe/Environmental-Sensing/tree/main/python/Tests)
 - Examples are
 [here](https://github.com/loco-philippe/Environmental-Sensing/tree/main/python/Examples)
-- data exchange standard for [observation](https://github.com/loco-philippe/
-Environmental-Sensing/tree/main/documentation/ObsJSON-Standard.pdf),
-[indexed list](https://github.com/loco-philippe/Environmental-Sensing/tree/main/
-documentation/IlistJSON-Standard.pdf) and
-[values](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation
-/ESJSON-Standard.pdf)
+- data exchange standard for [observation](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation/ObsJSON-Standard.pdf),
+[indexed list](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation/IlistJSON-Standard.pdf) and
+[values](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation/ESJSON-Standard.pdf)
 
 Modules contain the following classes:
 
 - Observation :
 
-    - `observation.Observation`
+    - `python.observation.esobservation`
 
 - ESValue :
 
-    - `observation.esvalue`(`observation.esvalue.DatationValue`,
-    `observation.esvalue.LocationValue`,
-    `observation.esvalue.PropertyValue`, `observation.esvalue.NamedValue`,
-    `observation.esvalue.ExternValue`, `observation.esvalue_base.ESValue`)
+    - `python.observation.esvalue`(`python.observation.esvalue.DatationValue`,
+    `python.observation.esvalue.LocationValue`,
+    `python.observation.esvalue.PropertyValue`, `python.observation.esvalue.NamedValue`,
+    `python.observation.esvalue.ExternValue`, `python.observation.esvalue_base.ESValue`)
 
 - Ilist :
 
-    - `observation.ilist`, `observation.ilist_structure`, `observation.ilist_interface`
+    - `python.observation.ilist`, `python.observation.ilist_structure`, `python.observation.ilist_interface`
 
 - Iindex :
 
-    - `observation.iindex`, `observation.iindex_structure`, `observation.iindex_interface`
+    - `python.observation.iindex`, `python.observation.iindex_structure`, `python.observation.iindex_interface`
 
 - TimeSlot :
 
-    - `observation.timeslot`
+    - `python.observation.timeslot`
 
 - ES :
 
-    - `observation.esconstante`.
+    - `python.observation.esconstante`.
 """
-from esobservation import Observation
-from esvalue import NamedValue, DatationValue, LocationValue, PropertyValue, ExternValue
-from esvalue_base import ESValue
-from ilist import Ilist
-from iindex import Iindex
-from essearch import ESSearch
-from esconstante import ES, Es, _classval
-from util import util
-from timeslot import TimeSlot
-from ilist_analysis import Analysis
+from observation.esobservation import Observation
+from observation.esvalue import NamedValue, DatationValue, LocationValue, PropertyValue, ExternValue
+from observation.esvalue_base import ESValue
+from observation.ilist import Ilist
+from observation.ilist_interface import IlistInterface, IlistError
+from observation.ilist_structure import IlistStructure
+from observation.iindex import Iindex
+from observation.iindex_structure import IindexStructure
+from observation.iindex_interface import CborDecoder, IindexError, IindexEncoder, IindexInterface
+from observation.essearch import ESSearch
+from observation.esconstante import ES, Es, _classval
+from observation.util import util
+from observation.timeslot import TimeSlot
+from observation.ilist_analysis import Analysis
 #print('package :', __package__)
```

### Comparing `observation-0.0.4/observation/esconstante.py` & `observation-0.0.5/observation/esconstante.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 """
 Created on Sun Aug  1 13:35:28 2021
 
 @author: philippe@loco-labs.io
 
-The `observation.esconstante` module describes the constants and default values used in other modules.
+The `python.observation.esconstante` module describes the constants and default values used in other modules.
 """
 import datetime
 import math
 from typing import Dict
 
 
 def _classval():
@@ -30,15 +30,15 @@
             ES.loc_classES: LocationValue,
             ES.prp_classES: PropertyValue,
             ES.res_classES: NamedValue,
             ES.ES_clsName: NamedValue}
 
 
 def _classESval():
-    from esobservation import LocationValue, DatationValue, PropertyValue, \
+    from observation.esobservation import LocationValue, DatationValue, PropertyValue, \
         NamedValue, ExternValue
     return {ES.obs_clsName: ExternValue,
             ES.dat_clsName: DatationValue,
             ES.loc_clsName: LocationValue,
             ES.prp_clsName: PropertyValue,
             ES.ext_clsName: ExternValue,
             ES.nam_clsName: NamedValue,
@@ -79,16 +79,16 @@
             "simpleval": False,  # only value in json
             "json_res_index": True,  # affiche index
             "json_prp_name": False,  # affiche name ou property
             "json_dat_name": False,  # affiche name ou instant/slot
             "json_loc_name": False,  # affiche name ou instant/slot
             "json_param": False,  # ok
             "geojson": False,  # ok
-            "json_info": False,  # si True, ok pour tous les info_
-            "json_info_detail": False,
+            #"json_info": False,  # si True, ok pour tous les info_
+            #"json_info_detail": False,
             # "json_info_type"      : False,
             # "json_info_nval"      : False,
             # "json_info_box"       : False,
             # "json_info_other"     : False,
             "unic_index": True,  # dans add
             # "add_equal"           : "full",  # sinon "value ou "name" pour les comparaisons
             "bytes_res_format": self.nullDict,  # calculé à partir de propperty si "null"
@@ -379,16 +379,18 @@
         self.complete = "complete"
         self.dimension = "dimension"
         self.num = "num"
         self.typevalue = "typevalue"
         self.lencodec = "lencodec"
         self.box = "box"
         self.cat = "cat"
-        self.typecoupl = "typecoupl"
+        #self.typecoupl = "typecoupl"
         self.pname = "pname"
+        self.parent = "parent"
+        self.root = "root"
         self.typecodec = "typecodec"
         self.linkrate = "linkrate"
         self.disttomin = "disttomin"
         self.disttomax = "disttomax"
 
         self.nul_classES = "nullClass"
         self.obs_classES = "observation"
```

### Comparing `observation-0.0.4/observation/esobservation.py` & `observation-0.0.5/observation/iindex_interface.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,588 +1,506 @@
 # -*- coding: utf-8 -*-
 """
-Created on Tue Aug  3 23:40:06 2021
+Created on Sun Oct  2 22:24:59 2022
 
 @author: philippe@loco-labs.io
 
-An `Observation` is an object representing a set of information having
-spatial and temporal characteristics associated with measurable or observable
- properties.
- 
-The `Observation` Object is built around three main bricks :
-    
-- Ilist Object which deal with indexing,
-- ESValue Object which integrate the specificities of environmental data,
-- Tools dedicated to particular domains ([Shapely](https://shapely.readthedocs.io/en/stable/manual.html) 
-for location, TimeSlot for Datation)
-
-The `observation.esobservation` module contains the `Observation` class.
-
-Documentation is available in other pages :
-
-- The concept of 'observation' is describe in 
-[this page](https://github.com/loco-philippe/Environmental-Sensing/wiki/Observation).
-- The concept of 'indexed list' is describe in 
-[this page](https://github.com/loco-philippe/Environmental-Sensing/wiki/Indexed-list).
-- The non-regression test are at 
-[this page](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Tests/test_obs.py)
-- The [examples](https://github.com/loco-philippe/Environmental-Sensing/tree/main/python/Examples/Observation)
-
-
+The `python.observation.iindex_interface` module contains the `IindexInterface` class
+(`python.observation.iindex.Iindex` methods).
 """
-import datetime
+# %% declarations
 import json
-import folium
+import datetime
+import numpy as np
+import pandas as pd
 import cbor2
-from copy import copy
-
-from ilist import Ilist
-from iindex import Iindex
-from util import util
-from iindex_interface import IindexEncoder, CborDecoder
-from esconstante import ES
-from esvalue import LocationValue, DatationValue, PropertyValue, ExternValue
-from esvalue_base import ESValue, ESValueEncoder
-from ilist_analysis import Analysis
-
-
-class Observation(Ilist):
-    """
-    An `Observation` is derived from `observation.Ilist` object.
-
-    *Additional attributes (for @property see methods)* :
-
-    - **name** : textual description
-    - **id** : textual identity 
-    - **param** : namedValue dictionnary (external data)
-
-    The methods defined in this class (included inherited) are :
-
-    *constructor (@classmethod))*
-
-    - `Observation.dic`
-    - `Observation.std`
-    - `observation.ilist.Ilist.obj`
-    - `Observation.from_obj`
-    - `observation.ilist.Ilist.from_file`
-
-    *dynamic value (getters @property)*
-
-    - `Observation.bounds`
-    - `Observation.jsonFeature`
-    - `Observation.setLocation`
-    - `Observation.setDatation`
-    - `Observation.setProperty`
-    - `Observation.setResult`
-
-    *dynamic value inherited (getters @property)*
-
-    - `observation.ilist.Ilist.extidx`
-    - `observation.ilist.Ilist.extidxext`
-    - `observation.ilist.Ilist.idxname`
-    - `observation.ilist.Ilist.idxlen`
-    - `observation.ilist.Ilist.iidx`
-    - `observation.ilist.Ilist.keys`
-    - `observation.ilist.Ilist.lenindex`
-    - `observation.ilist.Ilist.lenidx`
-    - `observation.ilist.Ilist.lidx`
-    - `observation.ilist.Ilist.lidxrow`
-    - `observation.ilist.Ilist.lvar`
-    - `observation.ilist.Ilist.lvarrow`
-    - `observation.ilist.Ilist.lname`
-    - `observation.ilist.Ilist.lunicname`
-    - `observation.ilist.Ilist.lunicrow`
-    - `observation.ilist.Ilist.setidx`
-
-    *global value (getters @property)*
-
-    - `observation.ilist.Ilist.complete`
-    - `observation.ilist.Ilist.consistent`
-    - `observation.ilist.Ilist.dimension`
-    - `observation.ilist.Ilist.lencomplete`
-    - `observation.ilist.Ilist.primary`
-    - `observation.ilist.Ilist.zip`
-
-    *selecting - infos methods*
-
-    - `observation.ilist.Ilist.couplingmatrix`
-    - `observation.ilist.Ilist.idxrecord`
-    - `observation.ilist.Ilist.indexinfos`
-    - `observation.ilist.Ilist.indicator`
-    - `observation.ilist.Ilist.iscanonorder`
-    - `observation.ilist.Ilist.isinrecord`
-    - `observation.ilist.Ilist.keytoval`
-    - `observation.ilist.Ilist.loc`
-    - `observation.ilist.Ilist.nindex`
-    - `observation.ilist.Ilist.record`
-    - `observation.ilist.Ilist.recidx`
-    - `observation.ilist.Ilist.recvar`
-    - `observation.ilist.Ilist.valtokey`
-
-    *add - update methods*
-
-    - `observation.ilist.Ilist.add`
-    - `observation.ilist.Ilist.addindex`
-    - `observation.ilist.Ilist.append`
-    - `Observation.appendObs`
-    - `observation.ilist.Ilist.delindex`
-    - `observation.ilist.Ilist.delrecord`
-    - `observation.ilist.Ilist.renameindex`
-    - `observation.ilist.Ilist.setname`
-    - `observation.ilist.Ilist.updateindex`    
-
-    *structure management - methods*
-
-    - `observation.ilist.Ilist.applyfilter`
-    - `observation.ilist.Ilist.coupling`
-    - `observation.ilist.Ilist.full`
-    - `observation.ilist.Ilist.getduplicates`
-    - `observation.ilist.Ilist.merge`
-    - `observation.ilist.Ilist.reindex`
-    - `observation.ilist.Ilist.reorder`
-    - `observation.ilist.Ilist.setfilter`
-    - `observation.ilist.Ilist.sort`
-    - `observation.ilist.Ilist.swapindex`
-    - `observation.ilist.Ilist.setcanonorder`
-    - `observation.ilist.Ilist.tostdcodec`
-
-    *exports methods*
-
-    - `Observation.choropleth`
-    - `observation.ilist.Ilist.json`
-    - `observation.ilist.Ilist.plot`
-    - `observation.ilist.Ilist.to_csv`
-    - `observation.ilist.Ilist.to_file`
-    - `Observation.to_obj`
-    - `Observation.to_xarray`
-    - `observation.ilist.Ilist.to_dataframe`
-    - `observation.ilist.Ilist.view`
-    - `observation.ilist.Ilist.vlist`
-    - `observation.ilist.Ilist.voxel`
-
-    """
-
-# %% constructor
-    def __init__(self, listidx=None, name=None, id=None, param=None, reindex=True):
-        '''Observation constructor
 
-        *Parameters*
-
-        - **listidx**  : object (default None) - list of Iindex data or Ilist or Observation
-        - **name**     : string (default None) - Obs name
-        - **id**       : string (default None) - Identification string
-        - **param**    : dict (default None) - Dict with parameter data or user's data'''
-
-        if isinstance(listidx, Observation):
-            self.lindex = [copy(idx) for idx in listidx.lindex]
-            if not listidx.param is None:
-                self.param = {k: v for k, v in listidx.param.items()}
-            else:
-                self.param = param
-            self.name = listidx.name
-            self.id = listidx.id
-            self.analysis = Analysis(self)
-            return
-        if isinstance(listidx, Ilist):
-            self.lindex = [copy(idx) for idx in listidx.lindex]
-            self.param = param
-            self.name = name
-            self.id = id
-            self.analysis = Analysis(self)
-            return
-        if not listidx:
-            Ilist.__init__(self)
-        else:
-            Ilist.__init__(self, listidx=listidx, reindex=reindex)
-        self.name = name
-        self.id = id
-        self.param = param
+from observation.esconstante import ES
+from observation.esvalue_base import ESValueEncoder, ESValue
+from observation.util import util, identity
+
+
+class CborDecoder(json.JSONDecoder):
+    ''' Cbor extension for integer keys (codification keys)'''
+
+    def __init__(self):
+        json.JSONDecoder.__init__(self, object_hook=self.codecbor)
+
+    def codecbor(self, dic):
+        dic2 = {}
+        for k, v in dic.items():
+            try:
+                k2 = int(k)
+            except:
+                k2 = k
+            dic2[k2] = v
+        return dic2
+
+
+class IindexError(Exception):
+    ''' Iindex Exception'''
+    # pass
+
+
+class IindexEncoder(json.JSONEncoder):
+    """new json encoder for Iindex and Ilist"""
+
+    def default(self, o):
+        if isinstance(o, datetime.datetime):
+            return o.isoformat()
+        option = {'encoded': False, 'encode_format': 'json'}
+        if o.__class__.__name__ in ('Ilist', 'TimeSlot'):
+            return o.json(**option)
+        if issubclass(o.__class__, ESValue):
+            return o.json(**option)
+        try:
+            return o.to_json(**option)
+        except:
+            try:
+                return o.__to_json__()
+            except:
+                return json.JSONEncoder.default(self, o)
+
+
+class IindexInterface:
+    '''this class includes Iindex methods :
+
+    - `IindexInterface.json`
+    - `IindexInterface.to_obj`
+    - `IindexInterface.to_dict_obj`
+    - `IindexInterface.to_numpy`
+    - `IindexInterface.to_pandas`
+    - `IindexInterface.vlist`
+    - `IindexInterface.vName`
+    - `IindexInterface.vSimple`
+    '''
 
-    @classmethod
-    def dic(cls, idxdic=None, typevalue=ES.def_clsName, name=None, id=None, param=None):
-        '''
-        Observation constructor (external dictionnary).
+    @staticmethod
+    def decodetype(decobj, lenparent=None):
+        '''Return the Iindex type of a decoded json value
 
         *Parameters*
 
-        - **idxdic** : dict (default None) - dict of Iindex element (Iindex name : list of Iindex values)
-        - **typevalue** : str (default ES.def_clsName) - default value class (None or NamedValue)
-        - **var** :  int (default None) - row of the variable
-        - **name**     : string (default None) - Observation name
-        - **id**       : string (default None) - Identification string
-        - **param**    : dict (default None) - Dict with parameter data or user's data'''
-        listidx = Ilist.dic(idxdic, typevalue=typevalue)
-        return cls(listidx=listidx, name=name, id=id, param=param)
-
-    @classmethod
-    def std(cls, result=None, datation=None, location=None, property=None,
-            name=None, id=None, param=None, typevalue=ES.def_clsName):
-        '''
-        Generate an Observation Object with standard indexes
+        - **decobj** : tuple with decoding data (see decodeobj method)
+        - **lenparent** : integer(default None) - parent length to compare to decoded codec length
 
-        *Parameters*
+        *Returns* 
 
-        - **datation** : compatible Iindex (default None) - index for DatationValue
-        - **location** : compatible Iindex (default None) - index for LocationValue
-        - **property** : compatible Iindex (default None) - index for PropertyValue
-        - **result  ** : compatible Iindex (default None) - index for Variable(NamedValue)
-        - **name**     : string (default None) - Observation name
-        - **id**       : string (default None) - Identification string
-        - **param**    : dict (default None) - Dict with parameter data or user's data'''
-        idxdic = {}
-        length = 0
-        std_val = (result, datation, location, property)
-        es_val = (ES.res_classES, ES.dat_classES,
-                  ES.loc_classES, ES.prp_classES)
-        for ind, (std, es) in enumerate(zip(std_val, es_val)):
-            value = []
-            if not std is None and isinstance(std, list):
-                value = std
-            elif not std is None and not isinstance(std, list):
-                value = [std]
-            length = max(length, len(value))
-            idxdic[es] = value
-        for item in idxdic.items():
-            if len(item[1]) == 1:
-                idxdic[item[0]] = item[1] * length
-        return cls.dic(idxdic=idxdic, typevalue=typevalue, name=name, id=id, param=param)
+        - **string** : name of the Iindex type'''
+        codec, parent, keys = decobj[2:5]
 
-    @classmethod
-    def from_obj(cls, bs=None, reindex=True, context=True):
-        '''
-        Generate an Observation Object from a bytes, string or dic value
+        if parent < 0 and not keys:
+            if len(codec) == 1:
+                return 'unique'
+            if lenparent and len(codec) == lenparent:
+                return 'root coupled'
+            if not lenparent:
+                raise IindexError(
+                    "lenparent is necessary to define the format")
+            return 'primary'
+        if parent >= 0 and not keys:
+            if lenparent and len(codec) == lenparent:
+                return 'coupled'
+            if not lenparent:
+                raise IindexError(
+                    "lenparent is necessary to define the format")
+            return 'periodic derived'
+        if len(keys) == lenparent and len(codec) < lenparent and parent < 0:
+            return 'root derived'
+        if len(keys) < lenparent and parent >= 0 and len(codec) < lenparent:
+            return 'derived'
+        raise IindexError("data are inconsistenty to define the format")
+        return
+
+    @staticmethod
+    def decodeobj(bs=None, classname=None, context=True):
+        '''Generate an Iindex data from a bytes, json or dict value
 
         *Parameters*
 
         - **bs** : bytes, string or dict data to convert
-        - **reindex** : boolean (default True) - if True, default codec for each Iindex
-        - **context** : boolean (default True) - if False, only codec and keys are included'''
-        if not bs:
-            bs = {}
+        - **classname** : string(default None) - classname to convert codec data
+        - **context** : boolean (default True) - if False, only codec and keys are included
+
+        *Returns* 
+
+        - **tuple** : name, dtype, codec, parent, keys, isfullindex, isparent, isvar
+            name (None or string): name of the Iindex
+            dtype (None or string): type of data
+            codec (list): lilst of Iindex codec values
+            parent (int): Iindex parent or ES.nullparent
+            keys (None or list): Iindex keys
+            isfullindex (boolean): True if Iindex is full (len(keys) = len(self))
+            isparent(boolean): True if parent is >= 0
+            isvar(boolean): not used
+            '''
+        if bs is None:
+            return (None, None, [], ES.nullparent, None, False, False, False)
         if isinstance(bs, bytes):
-            dic = cbor2.loads(bs)
-        elif isinstance(bs, str):
-            dic = json.loads(bs, object_hook=CborDecoder().codecbor)
-        elif isinstance(bs, dict):
-            dic = bs
-        else:
-            raise ObsError("the type of parameter is not available")
-        if ES.id in dic:
-            id = dic[ES.id]
-        else:
-            id = None
-        if id and not isinstance(id, str):
-            raise ObsError('id is not a str')
-        if ES.param in dic:
-            param = dic[ES.param]
-        else:
-            param = None
-        if param and not isinstance(param, dict):
-            raise ObsError('param is not a dict')
-        if ES.name in dic:
-            name = dic[ES.name]
+            lis = cbor2.loads(bs)
+        elif isinstance(bs, str) and bs[0] in ['{', '[', '"']:
+            lis = json.loads(bs, object_hook=CborDecoder().codecbor)
+        elif isinstance(bs, list):
+            lis = bs
         else:
-            name = None
-        if name and not isinstance(name, str):
-            raise ObsError('name is not a str')
-        if ES.data in dic:
-            data = dic[ES.data]
-        else:
-            data = None
-        if data and not isinstance(data, (list, dict)):
-            raise ObsError('data is not a list and not a dict')
-        return cls(listidx=Ilist.obj(data, reindex=reindex, context=context),
-                   name=name, id=id, param=param)
-
-# %% special
-    def __copy__(self):
-        ''' Copy all the data '''
-        return Observation(self)
-
-    def __str__(self):
-        '''return string format for var and lidx'''
-        if self.name:
-            stro = ES.name + ': ' + self.name + '\n'
-        else:
-            stro = ''
-        if self.id:
-            stro += ES.id + ': ' + self.id + '\n'
-        stri = Ilist.__str__(self)
-        if not stri == '':
-            stro += ES.data + ':\n' + stri
-        for idx in self.lidx:
-            stri += str(idx)
-        if self.param:
-            stro += ES.param + ':\n    ' + json.dumps(self.param) + '\n'
-        return stro
-
-    def __hash__(self):
-        '''return sum of all hash(Iindex)'''
-        return hash(json.dumps(self.param)) + hash(self.id) + hash(self.name) + \
-            Ilist.__hash__(self)
-
-# %% properties
-    @property
-    def bounds(self):
-        '''
-        **list of `observation.esvalue` (@property)** : `observation.esvalue` bounding box for each axis.'''
-        bound = [None, None, None]
-        if self.setDatation:
-            bound[0] = ESValue.boundingBox(self.setDatation).bounds
-        if self.setLocation:
-            bound[1] = ESValue.boundingBox(self.setLocation).bounds
-        if self.setProperty:
-            bound[2] = ESValue.boundingBox(self.setProperty).bounds
-        return bound
-
-    @property
-    def __geo_interface__(self):
-        '''**dict (@property)** : return the union of Location geometry (see shapely)'''
-        codecgeo = self.nindex('location').codec
-        if len(codecgeo) == 0:
-            return ""
-        if len(codecgeo) == 1:
-            return codecgeo[0].value.__geo_interface__
-        else:
-            collec = codecgeo[0].value
-            for loc in codecgeo[1:]:
-                collec = collec.union(loc.value)
-            return collec.__geo_interface__
+            lis = [bs]
+        if not isinstance(lis, list):
+            lis = [lis]
+
+        if not lis:  # format empty
+            return (None, None, [], ES.nullparent, None, False, False, False)
+        if context and (not isinstance(lis[0], (str, dict, list)) or len(lis) > 3):
+            return (None, None, IindexInterface.decodecodec(lis, classname),
+                    ES.nullparent, None, False, False, False)
+        if not context and len(lis) > 2:
+            return (None, None, IindexInterface.decodecodec(lis, classname),
+                    ES.nullparent, None, False, False, False)
+        if len(lis) == 3 and isinstance(lis[0], (str, dict)) and isinstance(lis[1], list) \
+                and isinstance(lis[2], (list, int)) and context:
+            return (*IindexInterface.decodecontext(lis[0]),
+                    IindexInterface.decodecodec(lis[1], classname),
+                    *IindexInterface.decodekeys(lis[2]))
+        if len(lis) == 2 and isinstance(lis[0], (str, dict)) and isinstance(lis[1], list) \
+                and context:
+            return (*IindexInterface.decodecontext(lis[0]),
+                    IindexInterface.decodecodec(
+                        lis[1], classname), ES.nullparent,
+                    None, False, False, False)
+        if len(lis) == 2 and isinstance(lis[0], (tuple, list)) \
+                and IindexInterface.iskeysobj(lis[1]):
+            return (None, None, IindexInterface.decodecodec(lis[0], classname),
+                    *IindexInterface.decodekeys(lis[1]))
+        return (None, None, IindexInterface.decodecodec(lis, classname), ES.nullparent,
+                None, False, False, False)
 
-    @property
-    def jsonFeature(self):
-        '''
-        **string (@property)** : "FeatureCollection" with Location geometry'''
-        if self.setLocation:
-            geo = self.__geo_interface__
-            if geo['type'][:5] == 'Multi':
-                typ = geo['type'][5:]
-                lis = [{"type":  typ, "coordinates": geo['coordinates'][i]}
-                       for i in range(len(geo['coordinates']))]
-            elif geo['type'] in ['Point', 'Polygon']:
-                lis = [geo]
-            elif geo['type'] == 'GeometryCollection':
-                lis = geo['geometries']
-            fea = [{"type": "Feature", "id": i, "geometry": lis[i]}
-                   for i in range(len(lis))]
-            return json.dumps({"type": "FeatureCollection", "features": fea},
-                              cls=ESValueEncoder)
-        return ''
+    @staticmethod
+    def decodecodec(codecobj, classname=ES.nam_clsName):
+        '''Generate a codec list from a json value'''
+        return [ESValue.from_obj(val, classname=classname) for val in codecobj]
 
-    @property
-    def setDatation(self):
-        '''**list (@property)** : list of codec values in the datation index'''
-        if self.nindex(ES.dat_classES):
-            return self.nindex(ES.dat_classES).codec
-        return None
-
-    @property
-    def setLocation(self):
-        '''**list (@property)** : list of codec values in the location index'''
-        if self.nindex(ES.loc_classES):
-            return self.nindex(ES.loc_classES).codec
-        return None
-
-    @property
-    def setProperty(self):
-        '''**list (@property)** : list of codec values in the property index'''
-        if self.nindex(ES.prp_classES):
-            return self.nindex(ES.prp_classES).codec
-        return None
+    @staticmethod
+    def decodecontext(context):
+        '''Generate a tuple (name, dtype) from a json value'''
+        if isinstance(context, dict) and len(context) == 1:
+            name, dtype = list(context.items())[0][0]
+            if isinstance(name, str) and isinstance(dtype, str) and dtype in ES.typeName.keys():
+                return (name, ES.typeName[dtype])
+            raise IindexError('name or typevalue is unconsistent')
+        if context in ES.typeName.keys():
+            return (context, ES.typeName[context])
+        if isinstance(context, str):
+            return (context, None)
+        raise IindexError('name or typevalue is unconsistent')
 
-    @property
-    def setResult(self):
-        '''
-        **list (@property)** : list of codec values in the result index'''
-        if self.nindex(ES.res_classES):
-            return self.nindex(ES.res_classES).codec
-        return None
+    @staticmethod
+    def decodekeys(keys):
+        '''Generate a tuple (parent, keys, isfullindex, isparent, isvar) from a json value'''
+        if isinstance(keys, int):
+            keys = [keys]
+        if isinstance(keys, list) and len(keys) == 0:
+            return (ES.notcrossed, keys, False, False, False)
+        if isinstance(keys, list) and len(keys) == 1 and isinstance(keys[0], int)\
+                and keys[0] < 0:
+            return (keys[0], None, False, False, True)
+        if isinstance(keys, list) and len(keys) == 1 and isinstance(keys[0], int)\
+                and keys[0] >= 0:
+            return (keys[0], None, False, True, False)
+        if isinstance(keys, list) and len(keys) == 2 and isinstance(keys[0], int)\
+                and isinstance(keys[1], list) and keys[0] < 0:
+            return (keys[0], keys[1], True, False, True)
+        if isinstance(keys, list) and len(keys) == 2 and isinstance(keys[0], int)\
+                and isinstance(keys[1], list) and keys[0] >= 0:
+            return (keys[0], keys[1], False, True, False)
+        if isinstance(keys, list) and len(keys) > 1:
+            return (ES.notcrossed, keys, True, False, False)
+        raise IindexError('parent or keys is unconsistent')
 
-# %% methods
-    def appendObs(self, obs, unique=False, fillvalue='-'):
+    @staticmethod
+    def encodeobj(codeclist, keyslist=None, name=None, simpleval=False,
+                  codecval=False, typevalue=None, parent=ES.nullparent,
+                  listunic=False, modecodec='optimize', **kwargs):
         '''
-        Add an `Observation` as a new Result `observation.esvalue` with bounding box for the Index `observation.esvalue`
+        Return a formatted object with values, keys and codec.
+        - Format can be json, bson or cbor
+        - object can be string, bytes or dict
 
         *Parameters*
+        - **modecodec** : string (default 'optimize') - json mode
+        - **codeclist** : list of codec ESValue to encode
+        - **keyslist** : list (default = None) - int keys to encode, None if no keys
+        - **name** : string (default = None) - name to encode, None if no name
+        - **typevalue** : string (default None) - type to convert values
+        - **parent** : int (default ES.nullparent) - Ilist index linked to
+        - **listunic** : boolean (default False) - if False, when len(result)=1 return value not list
+        - **codecval** : boolean (default False) - if True, only list of codec values is included
+        - **simpleval** : boolean (default False) - if True, only value (without name) is included
+
+        *Parameters (kwargs)*
 
-        - **obs** : Observation object
-        - **fillvalue** : object value used for default value
+        - **encoded** : boolean (default False) - choice for return format (string/bytes if True, dict else)
+        - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
+        - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
+        - **untyped** : boolean (default False) - include dtype in the json if True
+        - **geojson** : boolean (default False) - geojson for LocationValue if True
 
-        *Returns*
+        *Returns* : string, bytes or dict'''
+        option = {'encoded': False, 'encode_format': 'json', 'untyped': False,
+                  'codif': {}, 'typevalue': typevalue, 'geojson': False} | kwargs
+        js = []
+        if not codecval:
+            if name and typevalue:
+                js.append({name: typevalue})
+            elif name:
+                js.append(name)
+            elif typevalue:
+                js.append(typevalue)
+        codlis = [util.json(cc, encoded=False, typevalue=None, simpleval=simpleval,
+                            modecodec=modecodec, untyped=option['untyped'],
+                            geojson=option['geojson']) for cc in codeclist]
+        js.append(codlis)
+        if not codecval:
+            if parent >= 0 and keyslist:
+                js.append([parent, keyslist])
+            elif parent != ES.nullparent:
+                js.append(parent)
+            elif keyslist:
+                js.append(keyslist)
+        if len(js) == 1:
+            js = js[0]
+        if option['encoded'] and option['encode_format'] == 'json':
+            return json.dumps(js, cls=IindexEncoder)
+        if option['encoded'] and option['encode_format'] == 'cbor':
+            return cbor2.dumps(js, datetime_as_timestamp=True,
+                               timezone=datetime.timezone.utc, canonical=True)
+        return js
 
-        - **int** : last index in the `Observation`
+    @staticmethod
+    def iskeysobj(obj):
+        if isinstance(obj, int):
+            return True
+        if not isinstance(obj, list):
+            return False
+        if len(obj) == 0:
+            return True
+        if not isinstance(obj[0], int):
+            return False
+        if len(obj) == 1:
+            return True
+        if len(obj) > 2 and not isinstance(obj[1], int):
+            return False
+        if len(obj) == 2 and isinstance(obj[1], int):
+            return True
+        if len(obj) == 2 and isinstance(obj[1], list):
+            obj = obj[1]
+        if not isinstance(obj, list):
+            return False
+        for i in range(len(obj)):
+            if not isinstance(obj[i], int):
+                return False
+        return True
+
+    def json(self, keys=None, typevalue=None, modecodec='optimize', simpleval=False,
+             codecval=False, parent=ES.nullparent, **kwargs):
+        '''Return a formatted object (string, bytes or dict) for the Iindex
+
+        *Parameters*
+
+        - **keys** : list (default None) - list: List of keys to include - None:
+        no list - else: Iindex keys
+        - **typevalue** : string (default None) - type to convert values
+        - **modecodec** : string (default 'optimize') - json mode
+        - **simpleval** : boolean (default False) - if True, only codec is included
+        - **parent** : integer (default None) - index number of the parent in indexset
+
+        *Parameters (kwargs)*
+
+        - **encoded** : boolean (default False) - choice for return format
+        (string/bytes if True, dict else)
+        - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
+        - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
+        - **untyped** : boolean (default True) - include dtype in the json if True
+
+        *Returns* : string, bytes or dict'''
+        option = {'encoded': False, 'encode_format': 'json', 'untyped': True,
+                  'codif': {}} | kwargs
+        return self.to_obj(keys=keys, typevalue=typevalue, modecodec=modecodec,
+                           codecval=codecval, simpleval=simpleval, parent=parent,
+                           **option)
+
+    def to_pandas(self, func=None, codec=False, npdtype=None,
+                  series=True, index=True, numpy=False, **kwargs):
         '''
-        record = [fillvalue] * len(self.lname)
-        if ES.dat_classES in self.lname:
-            record[self.lname.index(ES.dat_classES)
-                   ] = DatationValue.Box(obs.bounds[0])
-        if ES.loc_classES in self.lname:
-            record[self.lname.index(ES.loc_classES)
-                   ] = LocationValue.Box(obs.bounds[1])
-        if ES.prp_classES in self.lname:
-            record[self.lname.index(ES.prp_classES)
-                   ] = PropertyValue.Box(obs.bounds[2])
-        if ES.res_classES in self.lname:
-            record[self.lname.index(ES.res_classES)] = ExternValue(obs)
-        return self.append(record, unique=unique)
+        Transform Iindex in a Pandas Series, Pandas DataFrame or Numpy array.
+
+        *Parameters*
 
-    def choropleth(self, name="choropleth", line=True):
+        - **func** : function (default None) - function to apply for each value of the Iindex.
+        If func is the 'index' string, values are replaced by raw values.
+        - **npdtype** : string (default None) - numpy dtype for the Array ('object' if None)
+        - **series** : boolean (default True) - if True, return a Series. 
+        If False return a DataFrame
+        - **index** : boolean (default True) - if True, index is keys.
+        - **numpy** : boolean (default False) - if True, return a Numpy array.
+        - **kwargs** : parameters to apply to the func function
+
+        *Returns* : Pandas Series, Pandas DataFrame, Numpy Array'''
+        if len(self) == 0:
+            raise IindexError("Ilist is empty")
+        if npdtype:
+            npdtype = np.dtype(npdtype)
+        else:
+            npdtype = 'object'
+        if func is None:
+            func = identity
+        if func == 'index':
+            return np.array(list(range(len(self))))
+        if not codec:
+            values = util.funclist(self.values, func, **kwargs)
+        else:
+            values = util.funclist(self._codec, func, **kwargs)
+        npdtype1 = npdtype
+        if isinstance(values[0], (datetime.datetime)):
+            npdtype1 = np.datetime64
+        # else:
+        #    npdtype=None
+        pdindex = None
+        if index:
+            pdindex = self._keys
+        try:
+            if numpy:
+                return np.array(values, dtype=npdtype1)
+            if series:
+                return pd.Series(values, dtype=npdtype1,
+                                 index=pdindex, name=self.name)
+            return pd.DataFrame(pd.Series(values, dtype=npdtype1,
+                                          index=pdindex, name=self.name))
+        except:
+            if numpy:
+                return np.array(values, dtype=npdtype)
+            if series:
+                return pd.Series(values, dtype=npdtype,
+                                 index=pdindex, name=self.name)
+            return pd.DataFrame(pd.Series(values, dtype=npdtype,
+                                          index=pdindex, name=self.name))
+
+    def to_numpy(self, func=None, codec=False, npdtype=None, **kwargs):
         '''
-        Display `Observation` on a folium.Map (only with dimension=1)
+        Transform Iindex in a Numpy array.
 
-        - **name** : String, optionnal (default 'choropleth') - Name of the choropleth
-        - **line** : Boolean, optionnal (default True) - Line between recods if True
+        *Parameters*
 
-        *Returns* : None'''
-        primary = self.primary
-        if self.dimension == 1:
-            m = folium.Map(location=self.setLocation[0].coorInv, zoom_start=6)
-            folium.Choropleth(
-                geo_data=self.jsonFeature,
-                name=self.name,
-                data=self.to_xarray(
-                    numeric=True, coord=True).to_dataframe(name='obs'),
-                key_on="feature.id",
-                columns=[self.idxname[primary[0]] + '_row', 'obs'],
-                fill_color="OrRd",
-                fill_opacity=0.7,
-                line_opacity=0.4,
-                line_weight=2,
-                legend_name=name
-            ).add_to(m)
-            if line:
-                folium.PolyLine(
-                    util.funclist(self.nindex('location'),
-                                  LocationValue.vPointInv)
-                ).add_to(m)
-            folium.LayerControl().add_to(m)
-            return m
-        return None
+        - **func** : function (default None) - function to apply for each value of the Iindex.
+        If func is the 'index' string, values are replaced by raw values.
+        - **npdtype** : string (default None) - numpy dtype for the Array ('object' if None)
+        - **kwargs** : parameters to apply to the func function
+
+        *Returns* : Numpy Array'''
+        return self.to_pandas(func=func, codec=codec, npdtype=npdtype, numpy=True, **kwargs)
+
+    def to_obj(self, keys=None, typevalue=None, simpleval=False, modecodec='optimize',
+               codecval=False, parent=ES.nullparent, name=True, listunic=False,
+               **kwargs):
+        '''Return a formatted object (string, bytes or dict) for the Iindex
 
-    def to_obj(self, **kwargs):
-        '''Return a formatted object (json string, cbor bytes or json dict). 
+        *Parameters*
+
+        - **modecodec** : string (default 'optimize') - json mode
+        - **keys** : list (default None) - list: List of keys to include - None or False:
+        no list - else: Iindex keys
+        - **typevalue** : string (default None) - type to convert values
+        - **name** : boolean (default True) - if False, name is not included
+        - **codecval** : boolean (default False) - if True, only list of codec values is included
+        - **simpleval** : boolean (default False) - if True, only value (without name) is included
+        - **listunic** : boolean (default False) - if False, when len(result)=1
+        return value not list
+        - **parent** : integer (default None) - index number of the parent in indexset
 
         *Parameters (kwargs)*
 
         - **encoded** : boolean (default False) - choice for return format
         (string/bytes if True, dict else)
         - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
         - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
-        - **modecodec** : string (default 'optimize') - if 'full', each index is with a full codec
-        if 'default' each index has keys, if 'optimize' keys are optimized, 
-        if 'dict' dict format is used, if 'nokeys' keys are absent
-        - **name** : boolean (default False) - if False, default index name are not included
-        - **fullvar** : boolean (default True) - if True and modecodec='optimize, 
-        variable index is with a full codec
+        - **untyped** : boolean (default False) - include dtype if True
         - **geojson** : boolean (default False) - geojson for LocationValue if True
 
-        - **json_param**     : Boolean - include Obs Param
-        - **json_info**      : Boolean - include all infos
-        - **json_info_detail**: Boolean - include the other infos
-
         *Returns* : string, bytes or dict'''
-        option = {'modecodec': 'optimize', 'encoded': False,
-                  'encode_format': 'json', 'codif': ES.codeb, 'name': False,
-                  'json_param': False, 'json_info': False, 'json_info_detail': False,
-                  'geojson': False, 'fullvar': True} | kwargs
-        option2 = option | {'encoded': False, 'encode_format': 'json'}
-        dic = {ES.type: ES.obs_classES}
-        if self.id:
-            dic[ES.obs_id] = self.id
-        if self.name:
-            dic[ES.obs_name] = self.name
-        if self.param:
-            dic[ES.obs_param] = self.param
-        dic[ES.obs_data] = Ilist.to_obj(self, **option2)
-        if option["json_param"] and self.param:
-            dic[ES.obs_param] = self.param
-        dic |= self._info(**option)
-        if option['codif'] and option['encode_format'] != 'cbor':
-            js2 = {}
-            for k, v in dic.items():
-                if k in option['codif']:
-                    js2[option['codif'][k]] = v
-                else:
-                    js2[k] = v
+        keyslist = None
+        if not name or self.name == ES.defaultindex:
+            idxname = None
         else:
-            js2 = dic
-        if option['encoded'] and option['encode_format'] == 'json':
-            return json.dumps(js2, cls=IindexEncoder)
-        if option['encoded'] and option['encode_format'] == 'cbor':
-            return cbor2.dumps(js2, datetime_as_timestamp=True,
-                               timezone=datetime.timezone.utc, canonical=True)
-        return dic
+            idxname = self.name
+        if modecodec == 'full':
+            codeclist = self.values
+            keyslist = None
+        elif modecodec == 'default':
+            codeclist = self._codec
+            keyslist = self._keys
+        else:
+            codeclist = self._codec
+            if keys and isinstance(keys, list):
+                keyslist = keys
+            elif keys and not isinstance(keys, list):
+                keyslist = self._keys
+        if typevalue:
+            dtype = ES.valname[typevalue]
+        else:
+            dtype = None
+        return IindexInterface.encodeobj(codeclist, keyslist, idxname, simpleval,
+                                         codecval, dtype, parent, listunic,
+                                         modecodec, **kwargs)
+
+    def to_dict_obj(self, typevalue=None, simpleval=False, modecodec='optimize', **kwargs):
+        option = {'encoded': False, 'encode_format': 'json', 'untyped': False,
+                  'codif': {}, 'geojson': False} | kwargs
+        dic = {}
+        if self.typevalue:
+            dic['type'] = self.typevalue
+        ds = pd.Series(range(len(self.keys)), index=self.keys, dtype='int64')
+        dic['value'] = [{'record': ds[i].tolist(),
+                         'codec': util.json(cod, encoded=False, typevalue=None,
+                                            simpleval=simpleval, modecodec=modecodec,
+                                            untyped=option['untyped'], datetime=False,
+                                            geojson=option['geojson'])}
+                        for i, cod in enumerate(self.codec)]
+        return {self.name: dic}
 
-    def to_xarray(self, info=False, idxname=None, varname=None, fillvalue='?',
-                  fillextern=True, lisfunc=None, numeric=False, npdtype=None,
-                  **kwargs):
+    def vlist(self, func, *args, extern=True, **kwargs):
         '''
-        Complete the Observation and generate a Xarray DataArray with the dimension define by idx.
+        Apply a function to values and return the result.
 
         *Parameters*
 
-        - **info** : boolean (default False) - if True, add _dict attributes to attrs Xarray
-        - **idxname** : list (default none) - list of idx to be completed. If None,
-        self.primary is used.
-        - **varname** : string (default none) - Name of the variable to use. If None,
-        first lvarname is used.
-        - **fillvalue** : object (default '?') - value used for the new extval
-        - **fillextern** : boolean(default True) - if True, fillvalue is converted to typevalue
-        - **lisfunc** : function (default none) - list of function to apply to indexes before export
-        - **numeric** : Boolean (default False) - Generate a numeric DataArray.Values.
-        - **npdtype** : string (default None) - numpy dtype for the DataArray ('object' if None)
-        - **kwargs** : parameter for lisfunc
-
-        *Returns* : DataArray '''
-        return Ilist.to_xarray(self, info=info, idxname=idxname, varname=varname,
-                               fillvalue=fillvalue, fillextern=fillextern,
-                               lisfunc=lisfunc, name=self.name, numeric=numeric,
-                               npdtype=npdtype, attrs=self.param, **kwargs)
-# %% internal
-
-    def _info(self, **kwargs):
-        ''' Create json dict with info datas'''
-        option = ES.mOption | kwargs
-        dcobs = {}
-        dcindex = {}
-        if not option['json_info']:
-            return dcobs
-        dcobs[ES.name] = self.name
-        dcobs[ES.length] = len(self)
-        dcobs[ES.lenindex] = self.lenindex
-        dcobs[ES.complete] = self.complete
-        dcobs[ES.dimension] = self.dimension
-        if option['json_info_detail']:
-            infos = self.indexinfos()
-        for ind, idx in enumerate(self.lidx):
-            dcidx = {}
-            dcidx[ES.num] = ind
-            dcidx[ES.typevalue] = idx.typevalue
-            dcidx[ES.lencodec] = len(idx.codec)
-            dcidx[ES.box] = Observation._info_box(idx, **option)
-            if option['json_info_detail']:
-                dcidx[ES.typecoupl] = infos[ind][ES.typecoupl]
-                dcidx[ES.cat] = infos[ind][ES.cat]
-                dcidx[ES.pname] = infos[ind][ES.pname]
-                dcidx[ES.typecodec] = idx.infos[ES.typecodec]
-                dcidx[ES.linkrate] = infos[ind][ES.linkrate]
-                dcidx[ES.disttomin] = idx.infos[ES.disttomin]
-                dcidx[ES.disttomax] = idx.infos[ES.disttomax]
-            dcindex[idx.name] = dcidx
-        return {ES.information: {ES.observation: dcobs, ES.index: dcindex}}
+        - **func** : function - function to apply to values
+        - **args, kwargs** : parameters for the function
+        - **extern** : if True, the function is apply to external values, else internal
+
+        *Returns* : list of func result'''
+        if extern:
+            return util.funclist(self.val, func, *args, **kwargs)
+        return util.funclist(self.values, func, *args, **kwargs)
 
-    @staticmethod
-    def _info_box(idx, **option):
-        ''' return box informations's'''
-        if (idx.typevalue == ES.dat_clsName):
-            return DatationValue.boundingBox(idx.codec)
-        if (idx.typevalue == ES.loc_clsName and not option["geojson"]):
-            return LocationValue.boundingBox(idx.codec)
-        if (idx.typevalue == ES.loc_clsName and option["geojson"]):
-            return LocationValue.Box(LocationValue.boundingBox(idx.codec)).__geo_interface__
-        if (idx.typevalue == ES.prp_clsName):
-            return PropertyValue.boundingBox(idx.codec)
-        return None
+    def vName(self, default=ES.nullName, maxlen=None):
+        '''
+        Return the list of name for ESValue data .
 
+        *Parameters*
+
+        - **default** : value return if no name is available
+        - **maxlen** : integer (default None) - max length of name
+
+        *Returns* : list of name founded'''
+        return [util.cast(val, dtype='name', default=default, maxlen=maxlen) for val in self.values]
+
+    def vSimple(self, string=False):
+        '''
+        Apply a vSimple function to values and return the result.
 
-class ObsError(Exception):
-    pass
+        *Parameters*
+
+        - **string** : boolean(default False) - if True the values returned are string
+
+        *Returns* : list of vSimple values (string or not)'''
+        if string:
+            return json.dumps([util.cast(val, 'simple', string=string) for val in self.values],
+                              cls=ESValueEncoder)
+        return [util.cast(val, 'simple', string=string) for val in self.values]
```

### Comparing `observation-0.0.4/observation/essearch.py` & `observation-0.0.5/observation/essearch.py`

 * *Files 12% similar despite different names*

```diff
@@ -2,23 +2,23 @@
 # How to use observation.essearch ?
 
 1. **Create the MongoDB database:**
 You can easily create an account on MongoDB. Once you have a database, follow the guidelines [here](https://www.mongodb.com/docs/atlas/tutorial/connect-to-your-cluster/#connect-to-your-atlas-cluster) to connect to it using pymongo.
 All you need in order to be able to use this module is to be able to connect to the Collection with pymongo.
 
 2. **Fill the database with your data:**
-Construct an observation or a list of observations containing your data using dedicated functions from `observation.Observation`. 
-You can then use either `insert_one_to_mongo(collection, observation)` or `insert_many_to_mongo(collection, observation_list)` to insert it in the database.
+Construct an observation or a list of observations containing your data using dedicated functions from `python.observation.Observation`. 
+You can then use `insert_mongo(collection, observation)` to insert it in the database.
 
 3. **Write a request using observation.ESSearch:**
 An `ESSearch` instance must be created with either a MongoDB Collection (passed as argument **collection**) or a list of observations (passed as argument **data**).
 Criteria for the query are then added one by one using `ESSearch.addCondition` or `ESSearch.orCondition`, or all together with `ESSearch.addConditions` or passed as argument **parameters** of ESSearch.
 
 A condition is composed of:
-- a **name** of a column or an exact **path** giving which element is concerned by the condition (name is a shortcut allowing not to enter a full path);
+- a **path** giving which element is concerned by the condition;
 - an **operand** which is the item of the comparison (if omitted, the existence of the path is tested);
 - a **comparator** which can be applied on the operand, for example '>=' or 'within' (defaults to equality in most cases);
 - optional parameters detailed in `ESSearch.addCondition` documentation, like **inverted** to add a *not*.
 
 Execute the research with `ESSearch.execute()`. Put the parameter **single** to True if you want the return to be a single observation
 instead of a list of observations.
 
@@ -54,20 +54,21 @@
 ```
 '''
 import datetime
 import shapely.geometry
 from pymongo.collection import Collection
 from pymongo.cursor import Cursor
 from pymongo.command_cursor import CommandCursor
-from esobservation import Observation
-from iindex import Iindex
-from util import util
-from timeslot import TimeSlot
 import bson
 
+from observation.esobservation import Observation
+from observation.iindex import Iindex
+from observation.util import util
+from observation.timeslot import TimeSlot
+
 dico_alias_mongo = { # dictionnary of the different names accepted for each comparator and each given type. <key>:<value> -> <accepted name>:<name in MongoDB>
     # any type other than those used as keys is considered non valid
     str : {
         None:"$eq",
         "eq":"$eq", "=":"$eq", "==":"$eq", "$eq":"$eq",
         "in":"$in", "$in":"$in",
         "regex":"$regex", "$regex":"$regex",
@@ -108,15 +109,16 @@
         "touches":"touches", "$touches":"touches",
         "overlaps":"overlaps", "$overlaps":"overlaps",
         "contains":"contains", "$contains":"contains",
         "$geoNear":"$geoNear", "$geonear":"$geoNear", "geonear":"$geoNear", "geoNear":"$geoNear",
         
         "in":"$in", "$in":"$in" # only in case where a list is not a geometry
     },
-    bson.objectid.ObjectId : {
+    #bson.objectid.ObjectId : {
+    bson.ObjectId : {
         None:"$eq",
         "eq":"$eq", "=":"$eq", "==":"$eq", "$eq":"$eq",
         "in":"$in", "$in":"$in"
     }
 }
 dico_alias_mongo[float] = dico_alias_mongo[int]
 
@@ -132,43 +134,40 @@
 _defeq    = lambda x, y: x == y
 _defsupeq = lambda x, y: x >= y
 _defsup   = lambda x, y: x > y
 _definfeq = lambda x, y: x <= y
 _definf   = lambda x, y: x < y
 _defin    = lambda x, y: x in y
 
-_timsupeq_0 = lambda x, y: x.bounds[0] >= y
-_timsup_0   = lambda x, y: x.bounds[0] > y
-_timinfeq_0 = lambda x, y: x.bounds[0] <= y
-_timinf_0   = lambda x, y: x.bounds[0] < y
-_timsupeq_1 = lambda x, y: x.bounds[1] >= y
-_timsup_1   = lambda x, y: x.bounds[1] > y
-_timinfeq_1 = lambda x, y: x.bounds[1] <= y
-_timinf_1   = lambda x, y: x.bounds[1] < y
+_timinfeq = lambda x, y: x.bounds[0] <= y # at least one element of the TimeSlot is lte y
+_timinf   = lambda x, y: x.bounds[0] < y  # at least one element of the TimeSlot is lt y
+_timsupeq = lambda x, y: x.bounds[1] >= y # at least one element of the TimeSlot is gte y
+_timsup   = lambda x, y: x.bounds[1] > y  # at least one element of the TimeSlot is gt y
+_timeq    = lambda x, y: x == TimeSlot(y)
+# To have all elements verify a comparison instead of just one, combine with parameter inverted.
+# For example : not (at least one element of the TimeSlot is lte y) <=> all elements of the TimeSlot are gt y
 
 dico_alias_python = {
     TimeSlot : { # only used in python filtering part
-        None:"equals",
-        "eq":"equals", "=":"equals", "==":"equals", "$eq":"equals", "equals":"equals", "$equals":"equals",
-        "contains":"contains", "$contains":"contains",
-        "in":"within", "$in":"within", "within":"within", "$within":"within",
-        "disjoint":"disjoint", "$disjoint":"disjoint",
-        "intersects":"intersects", "$intersects":"intersects",
-        
-        True: {
-            "$gte":_timsupeq_0, "gte":_timsupeq_0, ">=":_timsupeq_0, "=>":_timsupeq_0,
-            "$gt":_timsup_0, "gt":_timsup_0, ">":_timsup_0,
-            "$lte":_timinfeq_1, "lte":_timinfeq_1, "<=":_timinfeq_1, "=<":_timinfeq_1,
-            "$lt":_timinf_1, "lt":_timinf_1, "<":_timinf_1
+        TimeSlot : { # comparison of a TimeSlot with a timeSlot
+            None:"equals",
+            "eq":"equals", "=":"equals", "==":"equals", "$eq":"equals", "equals":"equals", "$equals":"equals",
+            "contains":"contains", "$contains":"contains",
+            "in":"within", "$in":"within", "within":"within", "$within":"within",
+            "disjoint":"disjoint", "$disjoint":"disjoint",
+            "intersects":"intersects", "$intersects":"intersects"
         },
-        False: {
-            "$gte":_timsupeq_1, "gte":_timsupeq_1, ">=":_timsupeq_1, "=>":_timsupeq_1,
-            "$gt":_timsup_1, "gt":_timsup_1, ">":_timsup_1,
-            "$lte":_timinfeq_0, "lte":_timinfeq_0, "<=":_timinfeq_0, "=<":_timinfeq_0,
-            "$lt":_timinf_0, "lt":_timinf_0, "<":_timinf_0
+            
+        datetime.datetime : { # comparison of a datetime and a TimeSlot
+            None:_timeq,
+            "eq":_timeq, "=":_timeq, "==":_timeq, "$eq":_timeq, "equals":_timeq, "$equals":_timeq,
+            "$gte":_timsupeq, "gte":_timsupeq, ">=":_timsupeq, "=>":_timsupeq,
+            "$gt":_timsup, "gt":_timsup, ">":_timsup,
+            "$lte":_timinfeq, "lte":_timinfeq, "<=":_timinfeq, "=<":_timinfeq,
+            "$lt":_timinf, "lt":_timinf, "<":_timinf
         }
     },
     'geometry' : { # lists are interpreted as geometries
         None:_geointer,
         "eq":_geoeq, "=":_geoeq, "==":_geoeq, "$eq":_geoeq, "equals":_geoeq, "$equals":_geoeq,
         "$geowithin":_geowith, "geowithin":_geowith, "$geoWithin":_geowith, "geoWithin":_geowith, "within":_geowith, "$within":_geowith,
         "disjoint":_geodis, "$disjoint":_geodis,
@@ -189,66 +188,82 @@
     }
 }
 
 def insert_from_doc(collection, document , info=True):
     '''Inserts all observations from a document into a collection, where each line of the document corresponds to an observation.'''
     with open(document, 'r') as doc:
         for line in doc:
-            try: insert_one_to_mongo(collection, line, info)
+            try: insert_to_mongo(collection, line, info)
             except: pass
 
-def insert_one_to_mongo(collection, obj, info=True):
-    '''Takes an object and inserts it into a MongoDB collection, with info by default.'''
-    if not isinstance(obj, Observation): obj = Observation.from_obj(obj)
-    dico2 = obj.json(json_info=info, modecodec='dict')
-    collection.insert_one(dico2)
-
-def insert_many_to_mongo(collection, objList, info=True):
-    '''Takes an object and inserts it into a MongoDB collection, with info by default.'''
-    for i in range(len(objList)):
-        if not isinstance(objList[i], Observation): objList[i] = Observation.from_obj(objList[i])
-        objList[i] = objList[i].json(json_info=info, modecodec='dict')
-    collection.insert_many(objList)
+def insert_to_mongo(collection, obj, info=False): # Mieux avec panda ?
+    '''Takes an observation or a list of observations and inserts them into a MongoDB collection, with info by default.'''
+    # Faire une fonction pour permettre l'ajout direct de fichiers csv.
+    inserted_list = []
+    if isinstance(obj, list):
+        pile = obj
+    elif isinstance(obj, Observation):
+        pile = [obj]
+    else:
+        pile = [Observation.from_obj(obj)]
+    for obs in pile:
+        if obs.id: obs_hash = obs.id
+        else: obs_hash = hash(obs)
+        metadata = {'id': obs_hash}
+        if obs.name : metadata['name']  = obs.name
+        if obs.param: metadata['param'] = obs.param
+        if info: metadata['information'] = Observation._info(True, True)
+        if len(obs.lname) == 1: # a special case is needed because lists with one element are replaced by the element itself so iteration doesn't work
+            for line in obs:
+                inserted_list.append({obs.lname[0]: util.json(line, encoded=False, typevalue=None, simpleval=False, geojson=True),
+                                        '_metadata': metadata})
+        elif len(obs.lname) > 1:
+            for line in obs:
+                inserted_list.append({obs.lname[i]: util.json(line[i], encoded=False, typevalue=None, simpleval=False, geojson=True) 
+                                                                for i in range(len(line))} | {'_metadata': metadata})
+    if inserted_list != []: collection.insert_many(inserted_list)
 
 def empty_request(collection):
     """
     Empty request to get an idea of what the database contains.
-    Currently returns the count of elements in the collection and the names of each column.
+    Currently returns the count of elements in the collection and the name of each column.
     """
     count = 0
     column_names = []
     cursor = collection.find()
     for doc in cursor:
         count += 1
-        for column_name in doc['data']:
+        for column_name in doc:
             if column_name not in column_names:
                 column_names.append(column_name)
-    return count, column_names
+    return {'count': count, 'column_names': column_names}
 
 class ESSearch:
     """
     An `ESSearch` is defined as an ensemble of conditions to be used to execute a MongoDB request or any iterable containing only observations.
 
     *Attributes (for @property, see methods)* :
 
     - **input** : input on which the query is done. One of or a list of these : 
         - pymongo.collection.Collection
         - pymongo.cursor.Cursor
         - pymongo.command_cursor.CommandCursor
         - Observation (can be defined from a str or a dict)
     - **parameters** : list of list of conditions for queries, to be interpreted as : parameters = [[cond_1 AND cond_2 AND cond_3] OR [cond_4 AND cond_5 AND cond_6]] where conds are criteria for queries
-    - **heavy** : boolean indicating whether the request should be simplified or not
+    - **hide** : list of paths to hide from the output
+    - **heavy** : boolean indicating whether the request should search for nested values or not. Does not work with geoJSON.
     - **sources** : attribute used to indicate the sources of the data in param
 
     The methods defined in this class are (documentations in methods definitions):
     
     *setter*
 
     - `ESSearch.addInput`
     - `ESSearch.removeInputs`
+    - `ESSearch.setHide`
     - `ESSearch.setHeavy`
     - `ESSearch.clear`
     
     *dynamic value (getter @property)*
 
     - `ESSearch.request`
     - `ESSearch.cursor`
@@ -264,58 +279,65 @@
     *query method*
 
     - `ESSearch.execute`
     """
     def __init__(self,
                     input = None,
                     parameters = None,
-                    heavy = True,
+                    hide = [],
+                    heavy = False,
                     sources = None, 
                     **kwargs
                     ):
         '''
         ESSearch constructor. Parameters can also be defined and updated using class methods.
 
         *Arguments*
 
-        - **input** : input on which the query is done. Must be one of or a list of these (can be nested): 
+        - **input** : input on which the query is done. Must be one of or a list of these (can be nested):
             - pymongo.collection.Collection
             - pymongo.cursor.Cursor
             - pymongo.command_cursor.CommandCursor
             - Observation
             - str corresponding to a json Observation
             - dict corresponding to a json Observation
         - **parameters** :  dict, list (default None) - list of list or list of dictionnaries whose keys are arguments of ESSearch.addCondition method
         ex: parameters = [
             {'name' : 'datation', 'operand' : datetime.datetime(2022, 9, 19, 1), 'comparator' : '>='},
             {'name' : 'property', 'operand' : 'PM2'}
         ]
+        - **hide** : list (default []) - List of strings where strings correspond to paths to remove from the output
         - **heavy** :  bool (default False) - Must be True when values are defined directly and inside dictionnaries simultaneously.
-        - **sources** : (default None) - Optionnal parameter indicating the sources of the data in case when a query is executed with parameter single = True.
+        - **sources** : (default None) - Optional parameter indicating the sources of the data in case when a query is executed with parameter single = True.
         - **kwargs** :  other parameters are used as arguments for ESSearch.addCondition method.
         '''
         self.parameters = [[]]                                          # self.parameters
+        if isinstance(hide, list): self.hide = hide                     # self.hide
+        else: raise TypeError("hide must be a list.")
+
         if isinstance(heavy, bool): self.heavy = heavy                  # self.heavy
         else: raise TypeError("heavy must be a bool.")
         self.sources = sources                                          # self.sources
 
-        self.input = []                                                 # self.input
+        self.input = [[], []]                                           # self.input : formatted as [[Mongo Objects], [Observations]] (list of two lists)
         if isinstance(input, list): pile = input
         else: pile = [input]
         while not len(pile) == 0:
             obj = pile.pop()
             if isinstance(obj, list):
                 pile += obj
-            elif isinstance(obj, (Collection, Cursor, CommandCursor, Observation)):
-                self.input.append(obj)
+            elif isinstance(obj, (Collection, Cursor, CommandCursor)):
+                self.input[0].append(obj)
+            elif isinstance(obj,  Observation):
+                self.input[1].append(obj)
             elif isinstance(obj, (str, dict)):
                 try:
-                    self.input.append(Observation.from_obj(obj))
+                    self.input[1].append(Observation.from_obj(obj))
                 except:
-                    raise ValueError("Cannot convert " + str(obj) + " to an Observation ")
+                    raise ValueError("Cannot convert " + str(obj) + " to an Observation.")
             elif obj is not None:
                 raise TypeError("Unsupported type for input " + str(obj))
 
         if parameters: self.addConditions(parameters)
         if kwargs: self.addCondition(**kwargs)
 
     def __repr__(self):
@@ -336,127 +358,136 @@
             raise StopIteration
 
     def __getitem__(self, key):
         return self.parameters[key]
 
     def addInput(self, input):
         """
-        Adds one or many inputs on which the query is to be executed given by argument input
+        Adds one or many inputs on which the query is to be executed given by argument input.
+        Inputs can be:
+            - pymongo.collection.Collection
+            - pymongo.cursor.Cursor
+            - pymongo.command_cursor.CommandCursor
+            - Observation
+            - str corresponding to a json Observation
+            - dict corresponding to a json Observation
+        or a list of any of these.
         """
-        added_input = []
+        added_input = [[], []]
         if isinstance(input, list): pile = input
         else: pile = [input]
-        while not len(pile) == 0:
+        while not len(pile) == 0: # using a stack (LIFO) to allow easy treatment of nested data.
             obj = pile.pop()
             if isinstance(obj, list):
                 pile += obj
-            elif isinstance(obj, (Collection, Cursor, CommandCursor, Observation)):
-                added_input.append(obj)
+            elif isinstance(obj, (Collection, Cursor, CommandCursor)):
+                added_input[0].append(obj)
+            elif isinstance(obj,  Observation):
+                added_input[1].append(obj)
             elif isinstance(obj, (str, dict)):
                 try:
-                    added_input.append(Observation.from_obj(obj))
+                    added_input[1].append(Observation.from_obj(obj))
                 except:
-                    raise ValueError("Cannot convert " + str(obj) + " to an Observation ")
+                    raise ValueError("Cannot convert " + str(obj) + " to an Observation.")
             elif obj is not None:
                 raise TypeError("Unsupported type for input " + str(obj))
-        self.input += added_input
+        self.input[0] += added_input[0] # self.input is updated with the new inputs
+        self.input[1] += added_input[1]
 
     def removeInputs(self):
         """
         Removes all inputs from self.
         """
-        self.input = []
+        self.input = [[], []]
 
+    def setHide(self, hide):
+        '''
+        Sets self.hide to a value given by argument hide.
+        '''
+        if isinstance(hide, list): self.hide = hide
+        else: raise TypeError("hide must be a list.")
+        
     def setHeavy(self, heavy):
         '''
         Sets self.heavy to a value given by argument heavy.
         '''
-        self.heavy = heavy
+        if isinstance(heavy, list): self.heavy = heavy
+        else: raise TypeError("heavy must be a bool.")
 
     def setSources(self, sources):
         '''
         Sets self.sources to a value given by argument sources.
         '''
         self.sources = sources
 
     def addConditions(self, parameters):
         '''
-        Takes multiple parameters and applyes self.addCondition() on each of them.
+        Takes multiple parameters and applies self.addCondition() on each of them.
         '''
-        if isinstance(parameters, dict):
+        if isinstance(parameters, dict): # case when one single condition is added
             self.addCondition(**parameters)
-        elif isinstance(parameters, (list, tuple)):
+        elif isinstance(parameters, (list, tuple)): # case when several conditions are added
             for parameter in parameters:
                 if isinstance(parameter, dict): self.addCondition(**parameter)
                 elif isinstance(parameters, (list, tuple)): self.addCondition(*parameter)
                 else: self.addCondition(parameter)
         else: raise TypeError("parameters must be either a dict or a list of dict.")
             
-    def addCondition(self, name = None, operand = None, comparator = None, path = None, or_position = -1, **kwargs):
+    def addCondition(self, path, operand = None, comparator = None, or_position = -1, **kwargs):
         '''
         Takes parameters and inserts corresponding query condition in self.parameters.
 
         *Parameters*
 
-        - **name** :  str (default None) - name of an IIndex, which corresponds to an Ilist column name.
+        - **path** :  str (required argument) - name of an IIndex, which corresponds to an Ilist column name, or name of a metadata element.
                     (ex: 'datation', 'location', 'property')
-                    This parameter is used to give a default value to parameters path and unwind.
 
         - **operand** :  - (default None) - Object used for the comparison.
                     (ex: if we search for observations made in Paris, operand is 'Paris')
 
         - **comparator**:  str (default None) - str giving the comparator to use. (ex: '>=', 'in')
-
-        - **path** :  str (default None) - to use to define a precise MongoDB path. When name is given, default path is data.*name*.value.codec
         
         - **or_position** :  int (default -1) - position in self.parameters in which the condition is to be inserted.
 
-        - **formatstring** :  str (default None) - str to use to automatically change str to datetime before applying condition. 
+        - **formatstring** :  str (default None) - str to use to automatically change str to datetime before applying condition.
                     Does not update the data base. If value is set to 'default', format is assumed to be Isoformat.
         
         - **inverted** :  bool (default None) - to add a "not" in the condition.
                     To use in case where every element of a MongoDB array (equivalent to python list) must verify the condition (by default, condition is verified when at least one element of the array verifies it).
         
         - **unwind** :  int (default None) - int corresponding to the number of additional {"$unwind" : "$" + path} to be added in the beginning of the query.
         
         - **regex_options** :  str (default None) - str associated to regex options (i, m, x and s). See [this link](https://www.mongodb.com/docs/manual/reference/operator/query/regex/) for more details.
 
         no comparator => default comparator associated with operand type in dico_alias_mongo is used (mainly equality)
         no operand => only the existence of something located at path is tested
         '''
-        if name is not None and not isinstance(name, str): raise TypeError("name must be a str.")
+
+        ## 1. Check if arguments given are valid.
+
+        if not isinstance(path, str): raise TypeError("name must be a str.")
         if comparator is not None and not isinstance(comparator, str): raise TypeError("comparator must be a str.")
-        if path is not None and not isinstance(path, str): raise TypeError("path must be a str.")
         if or_position is not None and not isinstance(or_position, int): raise TypeError("or_position must be an int.")
 
-        if name is None and operand is None and comparator is None and path is None:
-            raise ValueError("ESSearch.addCondition() requires at least one of these parameters : name, operand or path.")
-
-        for item in kwargs:
+        for item in kwargs: # checking if parameters in kwarg do exist
             if item not in {'formatstring', 'inverted', 'unwind', 'regex_options', 'distanceField', 'distanceMultiplier', 'includeLocs', 'key', 'maxDistance', 'minDistance', 'near', 'query', 'spherical'}:
                 raise ValueError("Unknown parameter : ", item)
 
         if isinstance(operand, datetime.datetime) and (operand.tzinfo is None or operand.tzinfo.utcoffset(operand) is None):
             operand = operand.replace(tzinfo=datetime.timezone.utc)
 
-        if path is None: # default values for path when not defined
-            if name:
-                if name in {"$year", "$month", "$dayOfMonth", "$hour", "$minute", "$second", "$millisecond", "$dayOfYear", "$dayOfWeek"}:
-                    path = "data.datation.value.codec"
-                else:
-                    path = "data." + name + ".value.codec" # there is no default case when name == "name": path is set to "data.name.value.cod" and not to "name"
-            else: path = "data"
-
-        if operand:
+        if operand: # checking if comparator can be applied on the operand
             try: comparator = dico_alias_mongo[type(operand)][comparator]
             except: raise ValueError("Incompatible values for comparator and operand. Ensure parameters are in the correct order.")
         elif comparator:
             raise ValueError("operand must be defined when comparator is used.")
+        
+        ## 2. Add the condition to self.parameters
 
-        condition = {"comparator" : comparator, "operand" : operand, "path" : path, "name" : name} | kwargs
+        condition = {"comparator" : comparator, "operand" : operand, "path" : path} | kwargs
 
         if or_position >= len(self.parameters):
             self.parameters.append([condition])
         else:
             self.parameters[or_position].append(condition)
 
     def orCondition(self, *args, **kwargs):
@@ -470,86 +501,84 @@
         Removes a condition from self.parameters. By default, last element added is removed.
         Otherwise, the removed condition is the one at self.parameters[or_position][condnum].
 
         To remove all conditions, use ESSearch.clearConditions() method.
         '''
         if self.parameters == [[]]: return
         if or_position is None:
-            if condnum is None:
+            if condnum is None: # by default : remove the very last added condition.
                 if len(self.parameters[-1]) > 1: self.parameters[-1].pop(-1)
                 else: self.parameters.pop(-1)
             else:
                 if len(self.parameters[-1]) > 1 or condnum > 1: self.parameters[-1].pop(condnum)
                 else: self.parameters.pop(-1)
         else:
-            if condnum is None or (len(self.parameters[or_position]) == 1 and condnum == 0): self.parameters.pop(or_position)
+            if condnum is None or (len(self.parameters[or_position]) == 1 and condnum == 0): self.parameters.pop(or_position) # if or_position is not None and condnum is, the whole sublist at or_position is removed.
             else: self.parameters[or_position].pop(condnum)
-        if self.parameters == []:
+        if self.parameters == []: # ensure self.parameters returns to its default value after being emptied
             self.parameters = [[]]
 
     def clearConditions(self):
         '''
         Removes all conditions from self.parameters.
         To remove all attributes, use ESSearch.clear() method.
         '''
         self.parameters = [[]]
 
     def clear(self):
         '''
-        Resets self
+        Resets self.
+        (Creating a new Observation would be smarter than using this function.)
         '''
         self = ESSearch()
 
-    def _cond(self, or_pos, operand, comparator, path, inverted = False, name = None, formatstring = None, unwind = None, regex_options = None, **kwargs):
+    def _cond(self, or_pos, operand, comparator, path, inverted = False, formatstring = None, unwind = None, regex_options = None, **kwargs):
         '''
         Takes parameters and adds corresponding MongoDB expression to self._match.
         self._unwind and self._set are updated when necessary.
         '''
-        match = '2'
-        if unwind: # unwind is applied by default when name is used and controlled precisely with parameter unwind
+        if unwind:
             if isinstance(unwind, str):
                 self._unwind.append(unwind)
             elif isinstance(unwind, int):
                 for _ in range(unwind): self._unwind.append(path)
             elif isinstance(unwind, tuple): # format : (<path>, <unwind quantity>)
                 for _ in range(unwind[1]): self._unwind.append(unwind[0])
             else: raise TypeError("unwind must be a tuple, a str or an int.")
-        elif name and operand and "data." + name + ".value" not in self._unwind: self._unwind.append("data." + name + ".value")
-        elif path[:5] != "data.": match = '1'
 
-        if self.heavy and operand is not None and path[:4] == "data":
+        if self.heavy and operand is not None:
             if path not in self._heavystages: self._heavystages.add(path) # peut-être mieux de laisser l'utilisateur choisir manuellement
             path = "_" + path + ".v"
 
-        if operand is None: # no operand => we only test if there is something located at path or at path given by name
-            if name: path = "data." + name
+        if operand is None: # no operand => we only test if there is something located at path
             comparator = "$exists"
             operand = 1
         else:
             try: comparator = dico_alias_mongo[type(operand)][comparator] #global variable
             except:
                 if formatstring:
                     try: comparator = dico_alias_mongo[datetime.datetime][comparator]
                     except: raise ValueError("Comparator not allowed.")
                 elif isinstance(operand, shapely.geometry.base.BaseGeometry):
                     operand = {"type" : operand.geom_type, "coordinates" : list(operand.exterior.coords)}
                 else: raise ValueError("Comparator not allowed.")
 
-        if name in {"$year", "$month", "$dayOfMonth", "$hour", "$minute", "$second", "$millisecond", "$dayOfYear", "$dayOfWeek"}:
-            self._set |= {name[1:]: {name : path}} #à tester
-            path = name[1:]
-            self._project |= {name[1:]:0}
+        ##if path in {"$year", "$month", "$dayOfMonth", "$hour", "$minute", "$second", "$millisecond", "$dayOfYear", "$dayOfWeek"}:
+        ##    self._set |= {path[1:]: {'datation' : path}} #à tester
+        ##    path = datation
+        ##    self._project |= {name[1:]:0}
 
         if isinstance(operand, TimeSlot): #equals->within, contains->intersects, within, disjoint, intersects
+            self._filtered = True
             if comparator == "within":
-                self._cond(or_pos, operand[0].start, "$gte", path, False, name)
-                self._cond(or_pos, operand[-1].end, "$lte", path, False, name)
+                self._cond(or_pos, operand[0].start, "$gte", path, False)
+                self._cond(or_pos, operand[-1].end, "$lte", path, False)
             elif comparator == "intersects":
-                self._cond(or_pos, operand[0].start, "$lte", path, False, name)
-                self._cond(or_pos, operand[-1].end, "$gte", path, False, name)
+                self._cond(or_pos, operand[0].start, "$lte", path, False) # pourquoi False et pas inverted ici ??
+                self._cond(or_pos, operand[-1].end, "$gte", path, False)
             return
 
         if formatstring:
             if formatstring == "default":
                 if isinstance(operand, str):
                     operand = datetime.datetime.fromisoformat(operand)
                 self._set |= {path : {"$convert": {"input" : "$" + path, "to" : "date", "onError" : "$" + path}}}
@@ -585,432 +614,457 @@
                 operand = {"$geometry" : {"type" : geom_type, "coordinates" : coordinates}}
             elif isinstance(operand, dict) and '$geometry' not in operand:
                 operand = {"$geometry" : operand}
         elif comparator == "$geoNear": # $geoNear is a MongoDB stage
             self._geonear = self._geonear | kwargs
             if 'distanceField' not in self._geonear: raise ValueError("distanceField missing in MongoDB stage $geoNear.")
             return
+        elif isinstance(operand, list): # lists are interpreted as geometries. An additional filtering is necessary for geometry-specific functions
+            self._filtered = True
+            return
         
         if comparator == "$regex" and regex_options:
             cond_0 = {"$regex" : operand, "$options" : regex_options}
         else:
             cond_0 = {comparator : operand}
         
         if inverted:
-            if path in self._match[match][or_pos]:
-                if "$nor" in self._match[match][or_pos][path]:
-                    self._match[match][or_pos][path]["$nor"].append(cond_0)
-                elif "not" in self._match[match][or_pos][path]:
-                    self._match[match][or_pos][path]["$nor"] = [self._match[match][or_pos][path]["$not"], cond_0]
-                    del self._match[match][or_pos][path]["$not"]
+            if path in self._match[or_pos]:
+                if "$nor" in self._match[or_pos][path]:
+                    self._match[or_pos][path]["$nor"].append(cond_0)
+                elif "not" in self._match[or_pos][path]:
+                    self._match[or_pos][path]["$nor"] = [self._match[or_pos][path]["$not"], cond_0]
+                    del self._match[or_pos][path]["$not"]
                 else:
-                    self._match[match][or_pos][path]["$not"] = cond_0
+                    self._match[or_pos][path]["$not"] = cond_0
             else:
-                self._match[match][or_pos][path] = {"$not" : cond_0}
+                self._match[or_pos][path] = {"$not" : cond_0}
         else:
-            if path not in self._match[match][or_pos]:
-                self._match[match][or_pos][path] = cond_0
+            if path not in self._match[or_pos]:
+                self._match[or_pos][path] = cond_0
             else:
-                self._match[match][or_pos][path] |= cond_0
+                self._match[or_pos][path] |= cond_0
 
     def _fullSearchMongo(self):
         """
         Takes self.parameters and returns a MongoDB Aggregation query.
         """
+        ## ESSearch._fullSearchMongo() 1: Declare private variables
+
         request = []
-        self._match = {}
-        self._match['1'] = [] #[{"type" : "observation"}] # first match stage benefits from the use of MongoDB indexes, second does not.
+        self._match = []
         self._unwind = []
-        self._heavystages = set() # two additional set stages when format is too unknown
+        self._heavystages = set() # two additional set stages to treat nested objects
         self._set = {}
         self._geonear = {}
-        self._match['2'] = [] # second match stage contains conditions which require to be after unwind and/or set stages.
-        self._project = {"_data" : 0} #{"_id" : 0, "_data" : 0, "information" : 0}
+        self._match = []
+        self._project = {"_id" : 0}
+        for el in self.hide: self._project |= {el : 0}
         
+        ## ESSearch._fullSearchMongo() 2: Update private variables for each condition
+
         for i in range(len(self.parameters)): # rewriting conditions in MongoDB format
-            self._match['1'].append({})
-            self._match['2'].append({})
+            self._match.append({})
             for cond in self.parameters[i]:
                 self._cond(or_pos = i, **cond)
 
-        if self._match['1']:                                                # Mongo $match stage (first one)
-            j = 0
-            for i in range(len(self._match['1'])):
-                if self._match['1'][i] and j != i:
-                    self._match['1'][j] = self._match['1'][i]
-                    j += 1
-            if j == 0: # when there is no $or
-                if self._match['1'][0]: request.append({"$match" : self._match['1'][0]})
-            else: # when there is a $or
-                request.append({"$match" : {"$or": self._match['1'][:j]}})
-        if self._unwind:                                                    # Mongo $unwind stage
-            for unwind in self._unwind:
-                request.append({"$unwind" : "$" + unwind})
-        if self._heavystages:                                               # additional Mongo $set stage # à tester
-            heavy = {}
-            for path in self._heavystages:
-                heavy |= {"_"+path:{"$cond":{"if":{"$eq":[{"$type":"$"+path},"object"]},"then":{"$objectToArray":"$"+path},"else": {"v":"$"+path}}}}
-            request.append({"$set" : heavy})
-        if self._set: request.append({"$set" : self._set})                  # Mongo $set stage
-        if self._geonear: request.append({"$geoNear" : self._geonear})      # Mongo $geoNear stage
-        if self._match['2']:                                                # Mongo $match stage (second one)
-            j = 0
-            for i in range(len(self._match['2'])):
-                if self._match['2'][i] and j != i:
-                    self._match['2'][j] = self._match['2'][i]
-                    j += 1
-            if j == 0: # when there is no $or
-                if self._match['2'][0]: request.append({"$match" : self._match['2'][0]})
-            else: # when there is a $or
-                request.append({"$match" : {"$or": self._match['2'][:j]}})
-        if self._unwind:
-            dico = {}
-            for unwind in self._unwind:
-                dico |= {unwind: ["$" + unwind]} # A FAIRE CORRECTEMENT ! (tel quel, ajoute toujours un seul array de chaque type...)
-            request.append({"$set" : dico})
-        if self._project: request.append({"$project" : self._project})      # Mongo stage $project
-        return request
+        ## ESSearch._fullSearchMongo() 3: Case 1 : find request
+
+        if not self._unwind and not self.heavy and not self._set and not self._geonear: # collection.find() request
+            if self._match:
+                j = 0
+                for i in range(len(self._match)):
+                    if self._match[i] and j != i: # removing empty elements in place
+                        self._match[j] = self._match[i]
+                        j += 1
+                if j == 0: # when there is no $or
+                    if self._match[0]: match = self._match[0]
+                else: # when there is a $or
+                    match = {"$or": self._match[:j]}
+            return 'find', match
+
+        ## ESSearch._fullSearchMongo() 4: Case 2 : aggregate request
+
+        else:
+            if self._unwind:                                                    # Mongo $unwind stage
+                for unwind in self._unwind:
+                    request.append({"$unwind" : "$" + unwind})
+            if self._heavystages:                                               # Additional Mongo $set stage if self.heavy is True
+                heavy = {}
+                for path in self._heavystages:
+                    heavy |= {"_"+path:{"$cond":{"if":{"$eq":[{"$type":"$"+path},"object"]},"then":{"$objectToArray":"$"+path},"else": {"v":"$"+path}}}}
+                    self._project |= {'_' + path: 0}
+                request.append({"$set" : heavy})
+            if self._set: request.append({"$set" : self._set})                  # Mongo $set stage
+            if self._geonear: request.append({"$geoNear" : self._geonear})      # Mongo $geoNear stage
+            if self._match:                                                     # Mongo $match stage
+                j = 0
+                for i in range(len(self._match)):
+                    if self._match[i] and j != i:
+                        self._match[j] = self._match[i]
+                        j += 1
+                if j == 0: # when there is no $or
+                    if self._match[0]: request.append({"$match" : self._match[0]})
+                else: # when there is a $or
+                    request.append({"$match" : {"$or": self._match[:j]}})
+            if self._unwind:                                                    # Second Mongo $set stage when unwind not empty
+                dico = {}
+                for unwind in self._unwind:
+                    if not unwind in dico: dico[unwind] = ["$" + unwind]
+                    else: dico[unwind] = [dico[unwind]]
+                request.append({"$set" : dico})
+            if self._project: request.append({"$project" : self._project})      # Mongo $project stage
+            return 'aggregation', request
 
     @property
     def request(self):
         '''
-        Getter returning the content of the aggregation query to be executed with ESSearch.execute().
+        Getter returning the content of the query or aggregation query to be executed with ESSearch.execute().
         '''
-        return self._fullSearchMongo()
+        request_type, request_content = self._fullSearchMongo()
+
+        if request_type == 'find':
+            return 'collection.find(' + str(request_content) + ', ' + str(self._project) + ')'
+        else:
+            return 'collection.aggregate(' + str(request_content) + ')'
 
     @property
-    def cursor(self, input):
+    def cursor(self):
         '''
-        Getter returning the coursors of the aggregation query result on all collections and cursors contained in self.input
-        or on the argument input if given.
+        Getter returning the cursors of the query or aggregation query result on all collections and cursors contained in self.input.
         '''
-        if input: return input.aggregate(self._fullSearchMongo())
+        request_type, request_content = self._fullSearchMongo()
+        
         cursor_list = []
-        for item in self.input:
+        for item in self.input[0]: # Determine the result cursor for each element of the input on which a Mongo query makes sense
             if isinstance(item, (Collection, Cursor, CommandCursor)):
-                cursor_list.append(item.aggregate(self._fullSearchMongo()))
+                if request_type == 'find':
+                    cursor_list.append(item.find(request_content, self._project))
+                else:
+                    cursor_list.append(item.aggregate(request_content))
         if len(cursor_list) == 1:
             return cursor_list[0]
         else:
             return cursor_list
 
-    def execute(self, filtered = False, namefused = False, single = False, fillvalue = None):
+
+    def execute(self, returnmode = 'observation', fillvalue = None, name = None, param = None):
         '''
         Executes the request and returns its result, either in one or many Observations.
 
         *Parameter*
 
-        - **fitered** :  bool (default False) - parameter to force filtering on Mongo out.
-        - **namefused** :  bool (default False) - Put to True to merge observations whose names are the same together.
-        - **single** :  bool (default True) - Must be put to False in order to return a list of Observation instead of a single Observation.
-        - **fillvalue** :  (default None) - Value to use to fill gaps when observations are fused together.
-        '''
+        - **returnmode** : str (default None) - Parameter giving the format of the output:
+            - 'unchanged' : output is returned as it is in the database, some operations like operations sepcific to TimeSlot object are not performed;
+            - 'observation': Each element is returned as an observation, but original observations aren't recreated;
+            - 'idfused': observations whose ids are the same are merged together; 
+            - 'single': return a single observation merging all observations together.
+        - **fillvalue** :  (default None) - Value to use to fill gaps when observations are merged together.
+        - **name** : str (default None) - name of the output observation when returnmode is 'single'.
+        - **param** : dict (default None) - param of the output observation when returnmode is 'single'.
+        '''
+        if returnmode not in {'unchanged', 'observation', 'idfused', 'single'}: raise ValueError("returnmode must have one of these values: 'unchanged', 'observation', 'idfused', 'single'.")
+        if returnmode == 'single':
+            if name  is not None and not isinstance(name, str)  : raise TypeError("name should be a string.")
+            if param is not None and not isinstance(param, dict): raise TypeError("param should be a dictionnary.")
+        self._filtered = False # Boolean put to True inside of self._cond() if an additional filtering specific to TimeSlot and shapely geometries is necessary.
+        
+        ## Construction of a result list where data are in the format given by returnmode
+        
+        ## ESSearch.execute() 1: Query is executed on each Mongo Collection or Cursor of self.input
+
         result = []
-        if self.parameters == [[]]: # à voir, car ne prend pas en compte un potentiel self.project ou similaire déclaré 
-                                    # autrement qu'au sein d'une condition. (ce qui, après tout, ne fait pas vraiment sens)
-            for data in self.input:
-                if isinstance(data, Observation):
-                    result.append(data)
-                else:
-                    for item in data.find(): result.append(Observation.from_obj(item))
-        else:
-            for data in self.input:
-                if isinstance(data, Observation):
-                    result.append(self._filtered_observation(item))
+        for data in self.input[0]:
+            request_type, request_content = self._fullSearchMongo()
+            if request_type == 'find':
+                cursor = data.find(request_content, self._project)
+            else:
+                cursor = data.aggregate(request_content)
+
+            if returnmode == 'observation': # Only in this case is an observation created directly.
+                for item in cursor:
+                    if self._filtered: # Additional filtering for objects like TimeSlot who need it
+                        for conds in self.parameters:
+                            checks_parameters, checks_conds = True, True
+                            for cond in conds:
+                                if cond['path'] in item:
+                                    try: checks_conds = checks_conds and self._condcheck(item[cond['path']], cond) # checking for each condition if it is satisfied
+                                    except: checks_conds = False
+                                else:
+                                    checks_conds = False
+                            checks_parameters = checks_parameters or checks_conds
+                    dic = {}
+                    if '_metadata' in item:
+                        if 'name'  in item['_metadata']: dic['name']  = item['_metadata']['name']
+                        if 'param' in item['_metadata']: dic['param'] = item['_metadata']['param']
+                        del item['_metadata']
+                    dic['idxdic'] = {key: [item[key]] for key in item}
+                    if not self._filtered or (self._filtered and checks_parameters): result.append(Observation.dic(**dic))
+
+            elif returnmode == 'single':
+                for item in cursor:
+                    if '_metadata' in item : del item['_metadata']
+                    result.append(item)
+
+            else: # returnmode == 'unchanged' or returnmode == 'idfused'
+                for item in cursor:
+                    if item:
+                        result.append(item)
+
+        ## ESSearch.execute() 2: Operations for cases 'idfused' and 'single' are performed on output objects.
+        # (more efficient to do it like this than after a conversion to Observation)
+
+        if returnmode == 'single':
+            arg = {} # argument to be given to Observation.dic() merging all observations together
+            for i in range(len(result)):
+                for column_name in arg: # for columns already in the new Observation
+                    if column_name not in result[i]:
+                        arg[column_name].append(fillvalue)
+                for column_name in result[i]: # for columns missing in the new Observation
+                    if column_name not in arg:
+                        arg[column_name] = [fillvalue] * i + [result[i][column_name]] # an empty column filled with fillvalue is added if a new column name is encountered
+                    else:
+                        arg[column_name].append(result[i][column_name])
+            if self._filtered: result = [self._filtered_observation(Observation.dic(arg))]
+            else: result = [Observation.dic(arg)]
+
+        elif returnmode == 'idfused':
+            hashs_dic = {}
+            for item in result:
+                id = str(item['_metadata']['id']) # will throw an error if item has no id. Should items with no id be let as is or merged together?
+                if id in hashs_dic: # one line is added to hashs_dic[id] for each element of result having this id
+                    del item['_metadata'] # Two items with the same id should have the same metadata.
+                    for column_name in hashs_dic[id]['idxdic']:
+                        if column_name not in item:
+                            hashs_dic[id]['idxdic'][column_name].append(fillvalue)
+                    for column_name in item:
+                        if column_name not in hashs_dic[id]['idxdic']:
+                            hashs_dic[id]['idxdic'][column_name] = [fillvalue] * i + [item[column_name]] # a filled column is added if a new column name is encountered
+                        else:
+                            hashs_dic[id]['idxdic'][column_name].append(item[column_name])
                 else:
-                    if filtered:
-                        for item in data.aggregate(self._fullSearchMongo()): 
-                            obs_out = self._mongo_out_to_obs(item)
-                            if obs_out:
-                                result.append(self._filtered_observation(obs_out))
+                    dic = {}
+                    if 'name'  in item['_metadata']: dic['name']  = item['_metadata']['name']
+                    if 'param' in item['_metadata']: dic['param'] = item['_metadata']['param']
+                    del item['_metadata']
+                    dic['idxdic'] = {key: [item[key]] for key in item}
+                    hashs_dic[id] = dic
+            result = []
+            for id in hashs_dic: # an Observation is added to result for each id
+                obs_out = Observation.dic(**hashs_dic[id])
+                if obs_out:
+                    if self._filtered: result.append(self._filtered_observation(obs_out)) # finalement, semble plus pertinent de faire ce filtrage directemt sur la sortie Mongo, car même si un à un les tests de condition sont faits à de nombreuses reprises, au global ce ne sont jamais les mêmes combinaisons de test
+                    else: result.append(obs_out)
+        # At this point, result is a list of observations.
+
+        ## ESSearch.execute() 3: Other inputs (pure observations) are treated purely in python with the self._filtered_observation() method
+
+        for data in self.input[1]: # data which are not taken from a Mongo database and already are observations are treated here.
+            result.append(self._filtered_observation(data, False))
+
+        ## ESSearch.execute() 4: Operations for cases 'idfused' and 'single' are performed again with the added observations
+
+        if len(result) >= 1:
+            if returnmode == 'single':
+                result = self._fusion(result, fillvalue)
+                if name is None: name = "ESSearch query result on " + str(datetime.datetime.now()) # default value for name
+                if param is None: # default value for param
+                    if self.sources is not None:
+                        sources = self.sources
                     else:
-                        for item in data.aggregate(self._fullSearchMongo()):
-                            obs_out = self._mongo_out_to_obs(item)
-                            if obs_out:
-                                result.append(obs_out)
-        if single:
-            return self._fusion(result, fillvalue=fillvalue)
-        elif namefused: return self._fusion(result, namefused, fillvalue)
-        else: return result
-
-    def _mongo_out_to_obs(self, dico):
-        '''
-        Takes a dictionnary output by the Mongo request and filters it to return an Observation which contains only valid measures.
-        '''
-        valid_records = set()
-        first_column = True
-        for column_key in dico['data']:
-            if first_column:
-                for i in range(len(dico['data'][column_key]['value'])):
-                    if isinstance(dico['data'][column_key]['value'][i]['record'], int):
-                        valid_records.add(dico['data'][column_key]['value'][i]['record'])
-                    elif isinstance(dico['data'][column_key]['value'][i]['record'], list):
-                        for k in dico['data'][column_key]['value'][i]['record']:
-                            valid_records.add(k)
-                first_column = False
-            else:
-                next_valid_records = set()
-                for i in range(len(dico['data'][column_key]['value'])):
-                    if isinstance(dico['data'][column_key]['value'][i]['record'], int) and \
-                            dico['data'][column_key]['value'][i]['record'] in valid_records:
-                        next_valid_records.add(dico['data'][column_key]['value'][i]['record'])
-                    elif isinstance(dico['data'][column_key]['value'][i]['record'], list):
-                        for k in dico['data'][column_key]['value'][i]['record']:
-                            if k in valid_records:
-                                next_valid_records.add(k)
-                valid_records = next_valid_records
-            if len(valid_records) == 0: return None
-        for column_key in dico['data']:
-            for i in range(len(dico['data'][column_key]['value'])-1, -1, -1):
-                if isinstance(dico['data'][column_key]['value'][i]['record'], int) and \
-                        dico['data'][column_key]['value'][i]['record'] not in valid_records:
-                    del dico['data'][column_key]['value'][i] # optimisation : reconstruire la liste au fur et à mesure plutôt que déplacer à chaque del
-                elif isinstance(dico['data'][column_key]['value'][i]['record'], list):
-                    for j in range(len(dico['data'][column_key]['value'][i]['record'])-1, -1, -1):
-                        if dico['data'][column_key]['value'][i]['record'][j] not in valid_records:
-                            del dico['data'][column_key]['value'][i]['record'][j]
-                    if len(dico['data'][column_key]['value'][i]['record']) == 0:
-                        del dico['data'][column_key]['value'][i]
-                    elif len(dico['data'][column_key]['value'][i]['record']) == 1:
-                        dico['data'][column_key]['value'][i]['record'] = dico['data'][column_key]['value'][i]['record'][0]
-        return Observation.from_obj(dico)
+                        sources = []
+                        for item in self.input: # informations about the inputs are added to param
+                            if isinstance(item, Observation):
+                                if item.name is not None:
+                                    sources.append('Observation: ' + item.name)
+                                else:
+                                    sources.append('data')
+                            elif isinstance(item, Collection):
+                                sources.append('MongoDB collection: ' + item.name + ' from database: ' + item.database.name)
+                            elif isinstance(item, Cursor):
+                                sources.append('Pymongo cursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
+                                                ' from database: ' + item.collection.database.name)
+                            elif isinstance(item, CommandCursor):
+                                sources.append('Pymongo commandcursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
+                                                ' from database: ' + item.collection.database.name)
+                            else: # should not happen
+                                sources.append('data')
+                    param = {'date': str(datetime.datetime.now()), 'project': 'essearch', 'type': 'dim3', 
+                            'context': {'origin': 'ESSearch query', 'sources ': sources, 
+                            'ESSearch_parameters': str(self.parameters)}}
+                result.param = param
+
+            elif returnmode == 'idfused' and len(result) != 1:
+                hashs_dic = {} # This dictionnary is in the format {id: [observations]}
+                for item in result:
+                    if item.id in hashs_dic:
+                        hashs_dic[item.id].append(item)
+                    else:
+                        hashs_dic[item.id] = [item]
+                result = []
+                for id in hashs_dic:
+                    obs_out = self._fusion(hashs_dic[id], fillvalue)
+                    if hashs_dic[id][0].name : obs_out.name = hashs_dic[id][0].name # name and param associated to the id are put back
+                    if hashs_dic[id][0].param: obs_out.name = hashs_dic[id][0].param
+                    if obs_out: result.append(obs_out)
+
+        ## ESSearch.execute() 5: Return result
 
-    def _filtered_observation(self, obs):
+        return result
+
+    def _filtered_observation(self, obs, is_from_mongo = True): # Vérifier que cette fonction n'est pas moins efficace que de tout déplier / filtrer / tout replier
+        # Regarder si on ne peut pas faire la même chose en mieux avec des fonctions de numpy ou panda.
         '''
         Takes an Observation and returns a filtered Observation with self.parameters as a filter.
         '''
         # self.parameters = [[cond1 AND cond 2 AND cond 3] OR [cond4 AND cond5 AND cond6]]
-        # dico = {"data": [["datation", [date1, date2, date3], [0,1,0,2,2,1]], ["location", [loc1, loc2, loc3], [0,1,2,0]]]}
-        if len(obs) == 0: return obs
-        
-        if not(isinstance(obs, Observation)):
-            try: Observation(obs)   # pas parfait puisque Observation.from_obj(obs) ne sera pas fait implicitement.
-            except: raise TypeError("Could not convert argument to an Observation.")
+        # dico = {"data": [["datation", [date1, date2, date3], [0,1,0,2,2,1]], ["location", [loc1, loc2, loc3], [0,1,2,0,1,1]]]} # dico n'est plus utilisé
+        if len(obs) == 0 or self.parameters == [[]]: return obs
+
+        ## ESSearch._filtered_observation() 0: This function is done with an iteration over self.parameters 
 
-        for i in range(len(self.parameters)):
+        final_filter = [False] * obs.lencomplete
+        for i in range(len(self.parameters)): # for each group of conditions separated by a or
             if self.parameters[i] != []:
-                conds, next_relevant = self._newconds(obs, self.parameters[i])
-                filter = util.funclist(obs.lindex[0].cod, self._condcheck, conds[0])
-                if not isinstance(filter, list): filter = [filter]
-                full_filter = util.tovalues(obs.lindex[0].keys, filter)
-                for j in range(1, obs.lenidx):
-                    next_filter = util.funclist(obs.lindex[j].cod, self._condcheck, conds[j])
-                    if not isinstance(next_filter, list): next_filter = [next_filter]
-                    next_filter_full = util.tovalues(obs.lindex[j].keys, next_filter)
-                    full_filter = [full_filter[k] and next_filter_full[k] for k in range(len(full_filter))]
-                if i == 0:
-                    final_filter = full_filter
-                    relevant = next_relevant
-                else:
-                    final_filter = [full_filter[j] or final_filter[j] for j in range(len(full_filter))]
+
+        ## ESSearch._filtered_observation() 1: Checking if no column is missing and if conditions on metadata are verified
+
+                conds = {} # conds is a dict which associates columns to the condition which concern them (inside of [cond1 AND cond 2 AND cond 3] : only AND)
+                relevant = True # no column given by cond["path"] is missing from obs
+                for cond in self.parameters[i]:
+                    next_relevant = False
+                    for j in range(len(obs.lindex)):
+                        if cond["path"] == obs.lindex[j].name:
+                            if j in conds: conds[j].append(cond)
+                            else: conds[j] = [cond]
+                            next_relevant = True
+                        elif cond["path"][:9] == "_metadata": # metadata are id, name and param
+                            if not is_from_mongo: # This step is considered to be done already for data taken out of Mongo
+                                if cond["path"][10:] == 'name' : next_relevant = next_relevant and self._condcheck(obs.name, cond)
+                                if cond["path"][10:] == 'id'   : next_relevant = next_relevant and self._condcheck(obs.id, cond)
+                                if cond["path"][10:] == 'param': next_relevant = next_relevant and self._condcheck(obs.param, cond)
+                            else:
+                                next_relevant = True
                     relevant = relevant and next_relevant
-        if relevant:
-            obs.setfilter(final_filter)
-            obs.applyfilter()
-            return obs
-        else:
-            return Observation()
+                if not relevant: continue # if a column on which a condition is applied is missing, the set of conditions given by the element of self.parameters is considered not verified.
 
-    def _newconds(self, obs, parameter):
-        '''
-        Takes parameters and returns a list of bool.
-        Allows to only test conditions on relevant elements. ex: 'cat' > 3 does not make sense.
-        '''
-        # parameter = [cond1 AND cond 2 AND cond 3]
-        new_conds = []
-        relevant =  False
-        for i in range(len(obs.lindex)):
-            new_conds.append([])
-            for cond in parameter:
-                if ("name" not in cond and ("path" not in cond or ("path" in cond and cond["path"] == "data." + obs.lindex[i].name) ) \
-                        or ("name" in cond and cond["name"] == obs.lindex[i].name)) \
-                        and ("operand" not in cond or ("operand" in cond and self._compatibletypes(obs.lindex[i].cod[0], cond))):
-                    new_conds[i].append(cond)
-                    relevant = True
-                elif "name" not in cond and "path" in cond and cond["path"][:11] == "information" : #Les vérifications sur les path commençant par information ne se font que dans MongoDB
-                    relevant = True
-        return new_conds, relevant
-
-    def _condcheck(self, item, parameter = None):
-        '''
-        Takes an item corresponding to an element of a column in an Observation and returns a Boolean if it verifies criteria given by parameter.
-        '''
-        # parameters = [cond_1 AND cond_2 AND cond_3]
-        if not parameter: return True
-        boolean = True
-        for cond in parameter:
-            boolean = boolean and self._condcheck_0(item, cond)
-        return boolean
+        ## ESSearch._filtered_observation() 2: Condition is applied on all elements of the Observation to create a boolean filter
+
+                full_filter = [True] * obs.lencomplete
+                for j in range(obs.lenidx): # iteration over the columns
+                    filter = []
+                    for item in obs.lindex[j].cod:
+                        boolean = True
+                        for cond in conds[j]:
+                            try: boolean = boolean and self._condcheck(item, cond)
+                            except: pass #boolean = False # pose problème pour les regex et autres opérations non implémentées...
+                        filter.append(boolean) # condition is rewritten as a boolean filter for the incoming data
+                    next_full_filter = util.tovalues(obs.lindex[j].keys, filter) # filter changed from filter on optimize codec to filter on full codec. (filter on optimize codec was the just how we calculated it, this isn't an actual method of the module)
+                    full_filter = [full_filter[k] and next_full_filter[k] for k in range(len(full_filter))] # full filter is updated each time
+
+        ## ESSearch._filtered_observation() 3: or_position is taken into account
+
+                final_filter = [final_filter[j] or full_filter[j] for j in range(len(full_filter))]
+
+        ## ESSearch._filtered_observation() 4: Application of the final filter on the incoming Observation
+
+        obs.setfilter(final_filter)
+        obs.applyfilter()
+        return obs
 
-    def _condcheck_0(self, item, cond = None):
+    def _condcheck(self, item, cond = None): # ajouter la gestion des regex
         '''
-        Takes an item and returns a Boolean.
-        Subfonction executed by _condcheck for each condition in parameter.
+        Takes an item and returns a Boolean if it verifies criteria given by parameter.
         '''
-        #cond = {"comparator" : comparator, "operand" : operand, "path" : path, "name" : name} and sometimes can contain "inverted" or "formatstring"
+        #cond = {"comparator" : comparator, "operand" : operand, "path" : path} and sometimes can contain other things
+
+        # 0. Basic cases
+
         if cond is None: return True
+        if 'inverted' in cond and cond['inverted']: return not self._condcheck(item, cond | {'inverted' : False})
         if cond["comparator"] is None and cond["operand"] is None: return True
 
+        # 1. formatstring applied if formatstring there is
+
         if "formatstring" in cond:
-            if not isinstance(item, datetime.datetime):
+            if not isinstance(item, (datetime.datetime, TimeSlot)):
                 item = datetime.datetime.strptime(item, cond["formatstring"])
-            if not isinstance(cond["operand"], datetime.datetime):
+            if not isinstance(cond["operand"], (datetime.datetime, TimeSlot)):
                 cond["operand"] = datetime.datetime.strptime(cond["operand"], cond["formatstring"])
-        elif isinstance(item, TimeSlot):
-            if cond["comparator"] in dico_alias_python[TimeSlot]:
-                cond["comparator"] = dico_alias_python[TimeSlot][cond["comparator"]]
+
+        # 2. Cases TimeSlot, geometry and nested property need specific treatment
+
+        if isinstance(item, TimeSlot):
+            if isinstance(cond["operand"], TimeSlot): # if comparator is one of the specific operators for TimeSlot
+                cond["comparator"] = dico_alias_python[TimeSlot][TimeSlot][cond["comparator"]]
                 return item.link(cond["operand"])[0] == cond["comparator"]
-            else:
-                if not 'inverted' in cond and cond['inverted']: inverted = False
-                else: inverted = True
-                try: return dico_alias_python[TimeSlot][inverted](item, cond["operand"])
+            else: # if operand is a datetime
+                try: return dico_alias_python[TimeSlot][datetime.datetime][cond["comparator"]](item, cond["operand"])
                 except: raise ValueError("Comparator not supported for TimeSlot.")
 
         elif isinstance(item, list) or isinstance(item, shapely.geometry.base.BaseGeometry):
-            if isinstance(item, list):
+            if isinstance(item, list): # lists are interpreted as geometries
                 if len(item) == 1: item = shapely.geometry.Point(item[0])
                 elif (len(item) > 1 and not isinstance(item[0], list)): item = shapely.geometry.Point(item)
                 elif len(item) == 2: item = shapely.geometry.LineString(item)
                 elif len(item) > 2:
                     if not item[-1] == item[0]:
                         item.append(item[0])
                     item = shapely.geometry.Polygon([item])
-            if isinstance(cond["operand"], list):
+            if isinstance(cond["operand"], list): # lists are interpreted as geometries
                 if len(cond["operand"]) == 1: cond["operand"] = shapely.geometry.Point(cond["operand"][0])
                 elif (len(cond["operand"]) > 1 and not isinstance(cond["operand"][0], list)):
                     cond["operand"] = shapely.geometry.Point(cond["operand"])
                 elif len(cond["operand"]) == 2: cond["operand"] = shapely.geometry.LineString(cond["operand"])
                 elif len(cond["operand"]) > 2:
                     if not item[-1] == item[0]:
                         item.append(item[0])
                     item = shapely.geometry.Polygon([item])
             return dico_alias_mongo['geometry'][cond["comparator"]](item, cond["operand"])
-            
-        elif cond["name"] == "property": # assuming that property contains dicts and that the query targets one of its values
+
+        elif cond["path"] == "property" and isinstance(item, dict): # assuming that property contains dicts and that the query targets one of its values
             for val in item.values():
-                if self._condcheck_0(val, cond | {"name" : None}):
+                if self._condcheck(val, cond | {"path" : None}):
                     return True
             return False
 
+        # 3. General comparison for remaining cases
+
         try: return dico_alias_mongo['default'][cond["comparator"]](item, cond["operand"])
         except:
             #raise ValueError("Comparator not supported.")
             return True
 
-    def _compatibletypes(self, item, cond):
-        '''
-        Takes an item and a condition and returns True if the condition can be applied on the item.
-        ex: 3 > 1 makes sense (returns True), but 'cat' > 1 does not (returns False).
-        (In this example, item = 3 or 'cat', cond = {'operand': 1, 'comparator': '>'})
-        '''
-        if type(item) == type(cond["operand"]): return True
-        elif cond["comparator"] == "$in":
-            if isinstance(cond["operand"], list) and len(cond["operand"]) > 0:
-                return self._compatibletypes(item, cond | {"operand" : cond["operand"][0], "comparator" : None})
-            elif len(cond["operand"]) == 0: return True
-            else: return False
-        elif "formatstring" in cond:
-            if isinstance(item, str):
-                return type(cond["operand"]) in {str, datetime.datetime, TimeSlot}
-            elif isinstance(cond["operand"], str):
-                return type(item) in {datetime.datetime, TimeSlot}
-        elif isinstance(item, dict):
-            for val in item.values():
-                if self._compatibletypes(val, cond):
-                    return True
-            return False
-        else:
-            return False
-
-    def _fusion(self, obsList, namefused = False, fillvalue = None, name = None):
+    def _fusion(self, obsList, fillvalue = None): # Idéalement, utiliser une méthode fusion de Observation.
         '''
-        Takes a list of observations and returns one observation merging them together in one single observation
-        or a list of observations where all observations sharing the same name are fused together.
+        Takes a list of observations and returns one observation merging them together in one single observation.
         '''
-# NE FONCTIONNE PAS S'IL NE S'AGIT PAS D'UNE LISTE D'OBSERVATIONS
-# parce que la conversion en observation est faite au sein d'execute et donc que les données entrées par le champ data ne sont pas converties
-# à voir pour modifier fusion / l'intégrer comme méthode de Ilist/Observation / modifier execute.
-# -> dans tous les cas, fait sens d'insérer fusion comme méthode d'Observation.
-        print(obsList)
-        if len(obsList) == 1:
-            return obsList[0]
-        elif len(obsList) > 1:
-            if not namefused:
-                lidx = []
-                new_lname = set()
-                for obs in obsList:
-                    new_lname |= set(obs.lname)
-                new_lname = list(new_lname)
-                
-                for i in range(len(new_lname)): # for each column of the new Observation
-                    values = []
-                    for obs in obsList: # for each Observation in the list
-                        if new_lname[i] in obs.lname: values += obs.lindex[obs.lname.index(new_lname[i])].values # values of the column are added to the new column
-                        else: values += [fillvalue] * len(obs) # when there is no value, filled with fillvalue
-                    codec = util.tocodec(values)
-                    lidx.append(Iindex(codec, new_lname[i], util.tokeys(values, codec)))
-
-                if name is None: name = "ESSearch query result on " + str(datetime.datetime.now())
-                if self.sources:
-                    sources = self.sources
-                else:
-                    sources = []
-                    for item in self.input:
-                        if isinstance(item, Observation):
-                            if item.name is not None:
-                                sources.append('Observation: ' + item.name)
-                            else:
-                                sources.append('data')
-                        elif isinstance(item, Collection):
-                            sources.append('MongoDB collection: ' + item.name + ' from database: ' + item.database.name)
-                        elif isinstance(item, Cursor):
-                            sources.append('Pymongo cursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
-                                            ' from database: ' + item.collection.database.name)
-                        elif isinstance(item, CommandCursor):
-                            sources.append('Pymongo commandcursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
-                                            ' from database: ' + item.collection.database.name)
-                        else: # should not happen
-                            sources.append('data')
-                param = {'date': str(datetime.datetime.now()), 'project': 'essearch', 'type': 'dim3', 
-                        'context': {'origin': 'ESSearch query', 'sources ': sources, 
-                        'ESSearch_parameters': str(self.parameters)}}
-                new_obs = Observation(lidx, name, param=param)
-                return new_obs
-            else:                   # à tester
-                new_obsList = []
-                dict_names = {}
-                for item in obsList:
-                    if item.name in dict_names:
-                        new_obsList[dict_names[item.name]].append(item)
-                    else:
-                        new_obsList.append([item])
-                        dict_names[item.name] = len(new_obsList) - 1
-                for i in range(len(new_obsList)):
-                    new_obsList[i] = self._fusion(new_obsList[i], False, fillvalue, new_obsList[i][0].name)
-                return new_obsList
-        else:
-            if not namefused:
-                if self.sources:
-                    sources = self.sources
-                else:
-                    sources = []
-                    for item in self.input:
-                        if isinstance(item, Observation):
-                            if item.name is not None:
-                                sources.append('Observation: ' + item.name)
-                            else:
-                                sources.append('data')
-                        elif isinstance(item, Collection):
-                            sources.append('MongoDB collection: ' + item.name + ' from database: ' + item.database.name)
-                        elif isinstance(item, Cursor):
-                            sources.append('Pymongo cursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
-                                            ' from database: ' + item.collection.database.name)
-                        elif isinstance(item, CommandCursor):
-                            sources.append('Pymongo commandcursor: ' + item.cursor_id + ' from collection ' + item.collection.name + 
-                                            ' from database: ' + item.collection.database.name)
-                        else: # should not happen
-                            sources.append('data')
-                param = {'date': str(datetime.datetime.now()), 'project': 'essearch', 'type': 'dim3', 
-                        'context': {'origin': 'ESSearch query', 'sources ': sources, 
-                        'ESSearch_parameters': str(self.parameters)}}               
-                return Observation(param=param)
-            else: return []
+        ## ESSearch._fusion() 0: Basic cases
+
+        if   len(obsList) == 0: return Observation()
+        elif len(obsList) == 1: return Observation(obsList[0])
+        else: # Fusion of a list with more than one element
+            lidx = []
+
+        ## ESSearch._fusion() 1: Determination of the names of the columns
+
+            new_lname = set()
+            for obs in obsList:
+                new_lname |= set(obs.lname)
+            new_lname = list(new_lname)
+            
+        ## ESSearch._fusion() 2: Fill the columns with the values of the observations to merge
+
+            for i in range(len(new_lname)): # for each column of the new Observation
+                values = []
+                for obs in obsList: # for each Observation in the list
+                    if new_lname[i] in obs.lname: values += obs.lindex[obs.lname.index(new_lname[i])].values # values of the column are added to the new column
+                    else: values += [fillvalue] * len(obs) # when there is no value, filled with fillvalue
+                codec = util.tocodec(values)
+                lidx.append(Iindex(codec, new_lname[i], util.tokeys(values, codec)))
+
+        ## ESSearch._fusion() 3: Build the actual Observation
+
+            return Observation(lidx)
+            # Il y aurait peut-être moyen d'optimiser un peu en remplaçant Iindex, util.tokeys et l'appel final d'Observation par des manipulations directes sur les objets.
+            # faire la fusion directement sur les keys au lieu de la faire sur les codec ?
+            # Avec la méthode actuelle, certaines opérations sont faites plusieurs fois.
```

### Comparing `observation-0.0.4/observation/esvalue.py` & `observation-0.0.5/observation/esvalue.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,39 +1,39 @@
 # -*- coding: utf-8 -*-
 """
 Created on Mon Aug  2 14:51:23 2021
 
 @author: philippe@loco-labs.io
 
-The `observation.esvalue` module contains the `observation.esvalue_base.ESValue` subclasses
+The `python.observation.esvalue` module contains the `python.observation.esvalue_base.ESValue` subclasses
 
 ESValue is build around two attributes :
 
 - 'name' which is a simple String
 - 'value' which corresponds to a more or less complex object :
 
     - 'DatationValue' : value is a TimeSlot Object which represent a set of time intervals
     - 'LocationValue' : value is a Shapely Geometry which represent a set of polygons
     - 'PropertyValue' : value is a simple dictionary which specifies all the characteristics of a property
     - 'NamedValue'    : value can be any simple object
     - 'ExternValue'   : value can be any other object
 
 <img src="https://loco-philippe.github.io/ES/ESValue_class.png" width="800">
 
-This module groups the classes of the objects used in the `observation.esobservation` module :
+This module groups the classes of the objects used in the `python.observation.esobservation` module :
 
 - `DatationValue`,
 - `LocationValue`,
 - `PropertyValue`,
 - `NamedValue`
 - `ExternValue`
 
 and the parent class :
 
-- `observation.esvalue_base.ESValue`
+- `python.observation.esvalue_base.ESValue`
 
 Documentation is available in other pages :
     
 - The concepts of 'ES value' are describe in 
 [this page](https://github.com/loco-philippe/Environmental-Sensing/wiki/ESValue).
 - The non-regression tests are at 
 [this page](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Tests/test_esvalue.py)
@@ -49,17 +49,17 @@
 import geojson
 import shapely.geometry
 import datetime
 from geopy import distance
 from copy import copy
 from openlocationcode import openlocationcode
 
-from esconstante import ES, _classval
-from esvalue_base import ESValueEncoder, ESValue
-from timeslot import TimeSlot
+from observation.esconstante import ES, _classval
+from observation.esvalue_base import ESValueEncoder, ESValue
+from observation.timeslot import TimeSlot
 
 
 class DatationValue(ESValue):   # !!! début ESValue
     # %% dat
     """
     This class represent Time (instant, interval or set of intervals).
 
@@ -292,15 +292,15 @@
 
     @property
     def coords(self):
         ''' return geoJson coordinates (list)'''
         if isinstance(self.value, shapely.geometry.polygon.Polygon):
             coords = [list(self.value.exterior.coords)]
         elif isinstance(self.value, shapely.geometry.point.Point):
-            coords = list(self.value.coords)[0]
+            coords = list(self.value.coords[0])
         elif isinstance(self.value, shapely.geometry.linestring.LineString):
             coords = list(self.value.coords)
         else:
             coords = ES.nullCoor
         return json.loads(json.dumps(coords, cls=ESValueEncoder))
 
     @property
```

### Comparing `observation-0.0.4/observation/esvalue_base.py` & `observation-0.0.5/observation/esvalue_base.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 """
 Created on Mon Aug  2 14:51:23 2021
 
 @author: philippe@loco-labs.io
 
-The `observation.esvalue_base` is a module dedicated to structured data (such as dates,
+The `python.observation.esvalue_base` is a module dedicated to structured data (such as dates,
 location or measurable properties) and groups common properties and concepts.
 
 ESValue is build around two attributes :
 
 - 'name' which is a simple String
 - 'value' which corresponds to a more or less complex object :
 
@@ -16,21 +16,21 @@
     - LocationValue : value is a Shapely Geometry which represent a set of polygons
     - PropertyValue : value is a simple dictionary which specifies all the characteristics of a property
     - NamedValue    : value can be any simple object
     - ExternValue   : value can be any other object
 
 <img src="https://loco-philippe.github.io/ES/ESValue_class.png" width="800">
 
-This module groups the classes of the objects used in the `observation.esobservation` module :
+This module groups the classes of the objects used in the `python.observation.esobservation` module :
 
-- `DatationValue`,
-- `LocationValue`,
-- `PropertyValue`,
-- `NamedValue`
-- `ExternValue`
+- `python.observation.esvalue.DatationValue`,
+- `python.observation.esvalue.LocationValue`,
+- `python.observation.esvalue.PropertyValue`,
+- `python.observation.esvalue.NamedValue`
+- `python.observation.esvalue.ExternValue`
 
 and the parent class :
 
 - `ESValue`
 
 Documentation is available in other pages :
     
@@ -49,16 +49,16 @@
 import json
 import re
 import datetime
 from json import JSONDecodeError
 import cbor2
 from copy import copy
 
-from esconstante import ES, _classval
-from timeslot import TimeInterval
+from observation.esconstante import ES, _classval
+from observation.timeslot import TimeInterval
 
 ListESValue = ['LocationValue', 'DatationValue',
                'PropertyValue', 'NamedValue', 'ExternValue']
 ListESValueSlot = ListESValue + ['TimeSlot']
 
 
 class ESValueEncoder(json.JSONEncoder):
@@ -493,23 +493,23 @@
             try:
                 return TimeInterval._dattz(datetime.datetime.fromisoformat(val))
             except ValueError:
                 return val
         return val
 
     @staticmethod
-    def uncastsimple(val):
+    def uncastsimple(val, datetime=True):
         ''' convert val in hashable val'''
         typeval = val.__class__.__name__
         if typeval == 'tuple':
             return ESValue._listed(val)
         # if typeval == 'tuple': return list(val)
         if typeval == 'str' and len(val) > 0 and val[0] == '{':
             return json.loads(val)
-        if typeval == 'datetime':
+        if datetime and typeval == 'datetime':
             return val.isoformat()
         return val
 
     @staticmethod
     def _tupled(idx):
         '''transform a list of list in a tuple of tuple'''
         return tuple([val if not isinstance(val, list) else ESValue._tupled(val) for val in idx])
```

### Comparing `observation-0.0.4/observation/iindex.py` & `observation-0.0.5/observation/iindex.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 """
 Created on Thu May 26 20:30:00 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.iindex` module contains the `Iindex` class.
+The `python.observation.iindex` module contains the `Iindex` class.
 
 Documentation is available in other pages :
 
 - The Json Standard for Iindex is defined [here](https://github.com/loco-philippe/
 Environmental-Sensing/tree/main/documentation/IlistJSON-Standard.pdf)
 - The concept of 'indexed list' is described in
 [this page](https://github.com/loco-philippe/Environmental-Sensing/wiki/Indexed-list).
@@ -28,19 +28,19 @@
     blob/main/python/Examples/Iindex/Iindex_structure-analysis.ipynb)
 
 ---
 """
 # %% declarations
 from copy import copy, deepcopy
 
-from esconstante import ES
-from esvalue_base import ESValue
-from iindex_interface import IindexInterface, IindexError
-from iindex_structure import IindexStructure
-from util import util
+from observation.esconstante import ES
+from observation.esvalue_base import ESValue
+from observation.iindex_interface import IindexInterface, IindexError
+from observation.iindex_structure import IindexStructure
+from observation.util import util
 
 
 class Iindex(IindexStructure, IindexInterface):
     # %% intro
     '''
     An `Iindex` is a representation of an index list .
 
@@ -50,14 +50,15 @@
     - **codec** : list of values for each key
     - **keys** : list of code values
 
     The methods defined in this class are :
 
     *constructor (@classmethod)*
 
+    - `Iindex.bol`
     - `Iindex.dic`
     - `Iindex.ext`
     - `Iindex.obj`
     - `Iindex.from_parent`
     - `Iindex.from_obj`
     - `Iindex.merging`
 
@@ -164,14 +165,31 @@
         self._keys = keys
         self._codec = codec
         self.name = name
         if reindex:
             self.reindex()
 
     @classmethod
+    def bol(cls, leng, notdef=None, name=None, default=True):
+        '''
+        Iindex constructor (boolean value).
+
+        *Parameters*
+
+        - **leng** : integer - length of the Iindex
+        - **notdef** : list (default None) - list of records without default value
+        - **default** : boolean (default True) - default value
+        - **name** : string (default None) - name of Iindex'''
+        values = [default] * leng
+        if notdef:
+            for item in notdef:
+                values[item] = not default        
+        return cls.ext(name=name, values=values)
+        
+    @classmethod
     def dic(cls, dicvalues=None, typevalue=ES.def_clsName, fullcodec=False):
         '''
         Iindex constructor (external dictionnary).
 
         *Parameters*
 
         - **dicvalues** : {name : values}  (see data model)
@@ -350,29 +368,30 @@
         ''' item of values'''
         return item in self.values
 
     def __getitem__(self, ind):
         ''' return value item (value conversion)'''
         if isinstance(ind, tuple):
             return [copy(self.values[i]) for i in ind]
+        #return self.values[ind]
         return copy(self.values[ind])
 
     def __setitem__(self, ind, value):
         ''' modify values item'''
         if ind < 0 or ind >= len(self):
             raise IindexError("out of bounds")
         self.setvalue(ind, value, extern=True)
 
     def __delitem__(self, ind):
         '''remove a record (value and key).'''
         self._keys.pop(ind)
         self.reindex()
 
     def __hash__(self):
-        '''return hash(codec) + hash(keys)'''
+        '''return hash(values)'''
         return hash(tuple(self.values))
 
     def _hashe(self):
         '''return hash(values)'''
         return hash(tuple(self.values))
 
     def _hashi(self):
```

### Comparing `observation-0.0.4/observation/iindex_interface.py` & `observation-0.0.5/observation/iindex_structure.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,496 +1,620 @@
 # -*- coding: utf-8 -*-
 """
 Created on Sun Oct  2 22:24:59 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.iindex_interface` module contains the `IindexInterface` class
-(`observation.iindex.Iindex` methods).
+The `python.observation.iindex_structure` module contains the `IindexStructure` class
+(`python.observation.iindex.Iindex` methods).
 """
-# %% declarations
-import json
-import datetime
-import numpy as np
-import pandas as pd
-import cbor2
-
-from esconstante import ES
-from esvalue_base import ESValueEncoder, ESValue
-from util import util, identity
-
-
-class CborDecoder(json.JSONDecoder):
-    ''' Cbor extension for integer keys (codification keys)'''
-
-    def __init__(self):
-        json.JSONDecoder.__init__(self, object_hook=self.codecbor)
-
-    def codecbor(self, dic):
-        dic2 = {}
-        for k, v in dic.items():
-            try:
-                k2 = int(k)
-            except:
-                k2 = k
-            dic2[k2] = v
-        return dic2
-
-
-class IindexError(Exception):
-    ''' Iindex Exception'''
-    # pass
-
-
-class IindexEncoder(json.JSONEncoder):
-    """new json encoder for Iindex and Ilist"""
-
-    def default(self, o):
-        if isinstance(o, datetime.datetime):
-            return o.isoformat()
-        option = {'encoded': False, 'encode_format': 'json'}
-        if o.__class__.__name__ in ('Ilist', 'TimeSlot'):
-            return o.json(**option)
-        if issubclass(o.__class__, ESValue):
-            return o.json(**option)
-        try:
-            return o.to_json(**option)
-        except:
-            try:
-                return o.__to_json__()
-            except:
-                return json.JSONEncoder.default(self, o)
+from collections import defaultdict, Counter
 
+from observation.esvalue_base import ESValue
+from observation.util import util
+from observation.esconstante import ES
+from observation.iindex_interface import IindexError
 
-class IindexInterface:
+
+class IindexStructure:
     '''this class includes Iindex methods :
 
-    - `IindexInterface.json`
-    - `IindexInterface.to_obj`
-    - `IindexInterface.to_dict_obj`
-    - `IindexInterface.to_numpy`
-    - `IindexInterface.to_pandas`
-    - `IindexInterface.vlist`
-    - `IindexInterface.vName`
-    - `IindexInterface.vSimple`
-    '''
+    *add - update methods*
 
-    @staticmethod
-    def decodetype(decobj, lenparent=None):
-        '''Return the Iindex type of a decoded json value
+    - `IindexStructure.append`
+    - `IindexStructure.setcodecvalue`
+    - `IindexStructure.setcodeclist`
+    - `IindexStructure.setname`
+    - `IindexStructure.setkeys`
+    - `IindexStructure.setlistvalue`
+    - `IindexStructure.setvalue`
+
+    *transform methods*
+
+    - `IindexStructure.coupling`
+    - `IindexStructure.extendkeys`
+    - `IindexStructure.full`
+    - `IindexStructure.reindex`
+    - `IindexStructure.reorder`
+    - `IindexStructure.sort`
+    - `IindexStructure.tocoupled`
+    - `IindexStructure.tostdcodec`
+
+    *getters methods*
+
+    - `IindexStructure.couplinginfos`
+    - `IindexStructure.derkeys`
+    - `IindexStructure.getduplicates`
+    - `IindexStructure.iscrossed`
+    - `IindexStructure.iscoupled`
+    - `IindexStructure.isderived`
+    - `IindexStructure.islinked`
+    - `IindexStructure.isvalue`
+    - `IindexStructure.iskeysfromderkeys`
+    - `IindexStructure.keysfromderkeys`
+    - `IindexStructure.keytoval`
+    - `IindexStructure.loc`
+    - `IindexStructure.recordfromkeys`
+    - `IindexStructure.recordfromvalue`
+    - `IindexStructure.valtokey`  '''
+
+    def append(self, value,  typevalue=ES.def_clsName, unique=True):
+        '''add a new value
 
         *Parameters*
 
-        - **decobj** : tuple with decoding data (see decodeobj method)
-        - **lenparent** : integer(default None) - parent length to compare to decoded codec length
+        - **value** : new object value
+        - **typevalue** : string (default ES.def_clsName) - typevalue to apply to value
+        - **unique** :  boolean (default True) - If False, duplication codec if value is present
+
+        *Returns* : key of value '''
+        value = util.castval(value, util.typename(self.name, typevalue))
+        if value in self._codec and unique:
+            key = self._codec.index(value)
+        else:
+            key = len(self._codec)
+            self._codec.append(value)
+        self._keys.append(key)
+        return key
+
+    def coupling(self, idx, derived=True, duplicate=True, reindex=False):
+        '''
+        Transform indexes in coupled or derived indexes (codec extension).
+        If derived option is True, self._codec is extended and idx codec not,
+        else, both are coupled and both codec are extended.
+
+        *Parameters*
 
-        *Returns* 
-
-        - **string** : name of the Iindex type'''
-        codec, parent, keys = decobj[2:5]
-
-        if parent < 0 and not keys:
-            if len(codec) == 1:
-                return 'unique'
-            if lenparent and len(codec) == lenparent:
-                return 'root coupled'
-            if not lenparent:
-                raise IindexError(
-                    "lenparent is necessary to define the format")
-            return 'primary'
-        if parent >= 0 and not keys:
-            if lenparent and len(codec) == lenparent:
-                return 'coupled'
-            if not lenparent:
-                raise IindexError(
-                    "lenparent is necessary to define the format")
-            return 'periodic derived'
-        if len(keys) == lenparent and len(codec) < lenparent and parent < 0:
-            return 'root derived'
-        if len(keys) < lenparent and parent >= 0 and len(codec) < lenparent:
-            return 'derived'
-        raise IindexError("data are inconsistenty to define the format")
+        - **idx** : single Iindex or list of Iindex to be coupled or derived.
+        - **derived** : boolean (default : True) - if True result is derived,
+        if False coupled
+        - **duplicate** : boolean (default: True) - if True, return duplicate records 
+        (only for self index)
+        - **reindex** : boolean (default : False). If True self.index is reindexed 
+        with default codec. But if not derived, idx indexes MUST to be reindexed.
+
+        *Returns* : tuple with duplicate records (errors) if 'duplicate', None else'''
+        if not isinstance(idx, list):
+            index = [idx]
+        else:
+            index = idx
+        idxzip = self.__class__.ext(list(zip(*([self._keys] + [ix._keys for ix in index]))),
+                                    typevalue=None)
+        self.tocoupled(idxzip)
+        if not derived:
+            for ind in index:
+                ind.tocoupled(idxzip)
+        if duplicate:
+            return self.getduplicates(reindex)
+        if reindex:
+            self.reindex()
         return
 
-    @staticmethod
-    def decodeobj(bs=None, classname=None, context=True):
-        '''Generate an Iindex data from a bytes, json or dict value
+    def couplinginfos(self, other, default=False):
+        '''return a dict with the coupling info between other (distance, rate,
+        dist, disttomin, disttomax, distmin, distmax, diff, typecoupl)
 
         *Parameters*
 
-        - **bs** : bytes, string or dict data to convert
-        - **classname** : string(default None) - classname to convert codec data
-        - **context** : boolean (default True) - if False, only codec and keys are included
-
-        *Returns* 
-
-        - **tuple** : name, typevaluedec, codec, parent, keys, isfullindex, isparent, isvar'''
-        if bs is None:
-            return (None, None, [], ES.nullparent, None, False, False, False)
-        if isinstance(bs, bytes):
-            lis = cbor2.loads(bs)
-        elif isinstance(bs, str) and bs[0] in ['{', '[', '"']:
-            lis = json.loads(bs, object_hook=CborDecoder().codecbor)
-        elif isinstance(bs, list):
-            lis = bs
+        - **other** : other index to compare
+        - **default** : comparison with default codec
+
+        *Returns* : dict'''
+        if default:
+            return util.couplinginfos(self.values, other.values)
+        if min(len(self), len(other)) == 0:
+            return {'dist': 0, 'distrate': 0, 'disttomin': 0, 'disttomax': 0,
+                    'distmin': 0, 'distmax': 0, 'diff': 0, 'typecoupl': 'null',
+                    'distance': 0, 'rate': 0}
+        lens = len(self._codec)
+        leno = len(other._codec)
+        xmin = max(lens, leno)
+        xmax = lens * leno
+        diff = abs(lens - leno)
+        if min(lens, leno) == 1:
+            rate = 0
+            if xmax - xmin + diff != 0:
+                rate = diff / (xmax - xmin + diff)
+            if lens == 1:
+                typec = 'derived'
+            else:
+                typec = 'derive'
+            return {'dist': xmin, 'distrate': 0, 'disttomin': 0, 'disttomax': 0,
+                    'distmin': xmin, 'distmax': xmax, 'diff': diff,
+                    'typecoupl': typec, 'distance': diff, 'rate': rate}
+        xso = len(util.tocodec([tuple((v1, v2))
+                  for v1, v2 in zip(self._keys, other._keys)]))
+        dic = {'dist': xso, 'distrate': (xso - xmin) / (xmax - xmin),
+               'disttomin': xso - xmin,  'disttomax': xmax - xso,
+               'distmin': xmin, 'distmax': xmax, 'diff': diff,
+               'distance': xso - xmin + diff,
+               'rate': (xso - xmin + diff) / (xmax - xmin + diff)}
+        if dic['distrate'] == 0 and dic['diff'] == 0:
+            dic['typecoupl'] = 'coupled'
+        elif dic['distrate'] == 0 and lens < leno:
+            dic['typecoupl'] = 'derived'
+        elif dic['distrate'] == 0 and lens > leno:
+            dic['typecoupl'] = 'derive'
+        elif dic['distrate'] == 1:
+            dic['typecoupl'] = 'crossed'
+        elif lens < leno:
+            dic['typecoupl'] = 'linked'
         else:
-            lis = [bs]
-        if not isinstance(lis, list):
-            lis = [lis]
-
-        if not lis:  # format empty
-            return (None, None, [], ES.nullparent, None, False, False, False)
-        if context and (not isinstance(lis[0], (str, dict, list)) or len(lis) > 3):
-            return (None, None, IindexInterface.decodecodec(lis, classname),
-                    ES.nullparent, None, False, False, False)
-        if not context and len(lis) > 2:
-            return (None, None, IindexInterface.decodecodec(lis, classname),
-                    ES.nullparent, None, False, False, False)
-        if len(lis) == 3 and isinstance(lis[0], (str, dict)) and isinstance(lis[1], list) \
-                and isinstance(lis[2], (list, int)) and context:
-            return (*IindexInterface.decodecontext(lis[0]),
-                    IindexInterface.decodecodec(lis[1], classname),
-                    *IindexInterface.decodekeys(lis[2]))
-        if len(lis) == 2 and isinstance(lis[0], (str, dict)) and isinstance(lis[1], list) \
-                and context:
-            return (*IindexInterface.decodecontext(lis[0]),
-                    IindexInterface.decodecodec(
-                        lis[1], classname), ES.nullparent,
-                    None, False, False, False)
-        if len(lis) == 2 and isinstance(lis[0], (tuple, list)) \
-                and IindexInterface.iskeysobj(lis[1]):
-            return (None, None, IindexInterface.decodecodec(lis[0], classname),
-                    *IindexInterface.decodekeys(lis[1]))
-        return (None, None, IindexInterface.decodecodec(lis, classname), ES.nullparent,
-                None, False, False, False)
+            dic['typecoupl'] = 'link'
+        return dic
 
-    @staticmethod
-    def decodecodec(codecobj, classname=ES.nam_clsName):
-        '''Generate a codec list from a json value'''
-        return [ESValue.from_obj(val, classname=classname) for val in codecobj]
+    def derkeys(self, parent):
+        '''return keys derived from parent keys
 
-    @staticmethod
-    def decodecontext(context):
-        '''Generate a tuple (name, dtype) from a json value'''
-        if isinstance(context, dict) and len(context) == 1:
-            name, dtype = list(context.items())[0][0]
-            if isinstance(name, str) and isinstance(dtype, str) and dtype in ES.typeName.keys():
-                return (name, ES.typeName[dtype])
-            raise IindexError('name or typevalue is unconsistent')
-        if context in ES.typeName.keys():
-            return (context, ES.typeName[context])
-        if isinstance(context, str):
-            return (context, None)
-        raise IindexError('name or typevalue is unconsistent')
+        *Parameters*
 
-    @staticmethod
-    def decodekeys(keys):
-        '''Generate a tuple (parent, keys, isfullindex, isparent, isvar) from a json value'''
-        if isinstance(keys, int):
-            keys = [keys]
-        if isinstance(keys, list) and len(keys) == 0:
-            return (ES.notcrossed, keys, False, False, False)
-        if isinstance(keys, list) and len(keys) == 1 and isinstance(keys[0], int)\
-                and keys[0] < 0:
-            return (keys[0], None, False, False, True)
-        if isinstance(keys, list) and len(keys) == 1 and isinstance(keys[0], int)\
-                and keys[0] >= 0:
-            return (keys[0], None, False, True, False)
-        if isinstance(keys, list) and len(keys) == 2 and isinstance(keys[0], int)\
-                and isinstance(keys[1], list) and keys[0] < 0:
-            return (keys[0], keys[1], True, False, True)
-        if isinstance(keys, list) and len(keys) == 2 and isinstance(keys[0], int)\
-                and isinstance(keys[1], list) and keys[0] >= 0:
-            return (keys[0], keys[1], False, True, False)
-        if isinstance(keys, list) and len(keys) > 1:
-            return (ES.notcrossed, keys, True, False, False)
-        raise IindexError('parent or keys is unconsistent')
+        - **parent** : Iindex - parent
 
-    @staticmethod
-    def encodeobj(codeclist, keyslist=None, name=None, simpleval=False,
-                  codecval=False, typevalue=None, parent=ES.nullparent,
-                  listunic=False, modecodec='optimize', **kwargs):
-        '''
-        Return a formatted object with values, keys and codec.
-        - Format can be json, bson or cbor
-        - object can be string, bytes or dict
-
-        *Parameters*
-        - **modecodec** : string (default 'optimize') - json mode
-        - **codeclist** : list of codec ESValue to encode
-        - **keyslist** : list (default = None) - int keys to encode, None if no keys
-        - **name** : string (default = None) - name to encode, None if no name
-        - **typevalue** : string (default None) - type to convert values
-        - **parent** : int (default ES.nullparent) - Ilist index linked to
-        - **listunic** : boolean (default False) - if False, when len(result)=1 return value not list
-        - **codecval** : boolean (default False) - if True, only list of codec values is included
-        - **simpleval** : boolean (default False) - if True, only value (without name) is included
-
-        *Parameters (kwargs)*
-
-        - **encoded** : boolean (default False) - choice for return format (string/bytes if True, dict else)
-        - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
-        - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
-        - **untyped** : boolean (default False) - include dtype in the json if True
-        - **geojson** : boolean (default False) - geojson for LocationValue if True
-
-        *Returns* : string, bytes or dict'''
-        option = {'encoded': False, 'encode_format': 'json', 'untyped': False,
-                  'codif': {}, 'typevalue': typevalue, 'geojson': False} | kwargs
-        js = []
-        if not codecval:
-            if name and typevalue:
-                js.append({name: typevalue})
-            elif name:
-                js.append(name)
-            elif typevalue:
-                js.append(typevalue)
-        codlis = [util.json(cc, encoded=False, typevalue=None, simpleval=simpleval,
-                            modecodec=modecodec, untyped=option['untyped'],
-                            geojson=option['geojson']) for cc in codeclist]
-        js.append(codlis)
-        if not codecval:
-            if parent >= 0 and keyslist:
-                js.append([parent, keyslist])
-            elif parent != ES.nullparent:
-                js.append(parent)
-            elif keyslist:
-                js.append(keyslist)
-        if len(js) == 1:
-            js = js[0]
-        if option['encoded'] and option['encode_format'] == 'json':
-            return json.dumps(js, cls=IindexEncoder)
-        if option['encoded'] and option['encode_format'] == 'cbor':
-            return cbor2.dumps(js, datetime_as_timestamp=True,
-                               timezone=datetime.timezone.utc, canonical=True)
-        return js
+        *Returns* : list of keys'''
+        derkey = [ES.nullparent] * len(parent._codec)
+        for i in range(len(self)):
+            derkey[parent._keys[i]] = self._keys[i]
+        if min(derkey) < 0:
+            raise IindexError("parent is not a derive Iindex")
+        return derkey
+
+    def extendkeys(self, keys):
+        '''add keys to the Iindex
+
+        *Parameters*
+
+        - **keys** : list of int (value lower or equal than actual keys)
+
+        *Returns* : None '''
+        if min(keys) < 0 or max(keys) > len(self._codec) - 1:
+            raise IindexError('keys not consistent with codec')
+        self._keys += keys
 
     @staticmethod
-    def iskeysobj(obj):
-        if isinstance(obj, int):
-            return True
-        if not isinstance(obj, list):
-            return False
-        if len(obj) == 0:
-            return True
-        if not isinstance(obj[0], int):
-            return False
-        if len(obj) == 1:
-            return True
-        if len(obj) > 2 and not isinstance(obj[1], int):
-            return False
-        if len(obj) == 2 and isinstance(obj[1], int):
-            return True
-        if len(obj) == 2 and isinstance(obj[1], list):
-            obj = obj[1]
-        if not isinstance(obj, list):
+    def full(listidx):
+        '''tranform a list of indexes in crossed indexes (value extension).
+
+        *Parameters*
+
+        - **listidx** : list of Iindex to transform
+
+        *Returns* : tuple of records added '''
+        idx1 = listidx[0]
+        for idx in listidx:
+            if len(idx) != len(idx):
+                return None
+        leninit = len(idx1)
+        keysadd = util.idxfull(listidx)
+        for idx, keys in zip(listidx, keysadd):
+            idx._keys += keys
+        return tuple(range(leninit, len(idx1)))
+
+    def getduplicates(self, reindex=False):
+        ''' calculate items with duplicate codec
+
+        *Parameters*
+
+        - **reindex** : boolean (default : False). If True index is reindexed with default codec
+        
+        *Returns* : tuple of items with duplicate codec'''
+        count = Counter(self._codec)
+        defcodec = list(count - Counter(list(count)))
+        dkeys = defaultdict(list)
+        for key, ind in zip(self._keys, range(len(self))):
+            dkeys[key].append(ind)
+        dcodec = defaultdict(list)
+        for key, ind in zip(self._codec, range(len(self._codec))):
+            dcodec[key].append(ind)
+        duplicates = []
+        for item in defcodec:
+            for codecitem in dcodec[item]:
+                duplicates += dkeys[codecitem]
+        if reindex:
+            self.reindex()
+        return tuple(duplicates)
+
+    def iscrossed(self, other):
+        '''return True if self is crossed to other'''
+        return self.couplinginfos(other)['distrate'] == 1.0
+
+    def iscoupled(self, other):
+        '''return True if self is coupled to other'''
+        info = self.couplinginfos(other)
+        return info['diff'] == 0 and info['distrate'] == 0
+
+    def isderived(self, other):
+        '''return True if self is derived from other'''
+        info = self.couplinginfos(other)
+        return info['diff'] != 0 and info['distrate'] == 0.0
+
+    def iskeysfromderkeys(self, other):
+        '''return True if self._keys is relative from other._keys'''
+        leng = len(other._codec)
+        if leng % len(self._codec) != 0:
             return False
-        for i in range(len(obj)):
-            if not isinstance(obj[i], int):
-                return False
-        return True
-
-    def json(self, keys=None, typevalue=None, modecodec='optimize', simpleval=False,
-             codecval=False, parent=ES.nullparent, **kwargs):
-        '''Return a formatted object (string, bytes or dict) for the Iindex
+        keys = [(i*len(self._codec))//leng for i in range(leng)]
+        return self.__class__.keysfromderkeys(other._keys, keys) == self._keys
+
+    def islinked(self, other):
+        '''return True if self is linked to other'''
+        rate = self.couplinginfos(other)['distrate']
+        return 0.0 < rate < 1.0
+
+    def isvalue(self, value, extern=True):
+        ''' return True if value is in index values
 
         *Parameters*
 
-        - **keys** : list (default None) - list: List of keys to include - None:
-        no list - else: Iindex keys
-        - **typevalue** : string (default None) - type to convert values
-        - **modecodec** : string (default 'optimize') - json mode
-        - **simpleval** : boolean (default False) - if True, only codec is included
-        - **parent** : integer (default None) - index number of the parent in indexset
-
-        *Parameters (kwargs)*
-
-        - **encoded** : boolean (default False) - choice for return format
-        (string/bytes if True, dict else)
-        - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
-        - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
-        - **untyped** : boolean (default True) - include dtype in the json if True
-
-        *Returns* : string, bytes or dict'''
-        option = {'encoded': False, 'encode_format': 'json', 'untyped': True,
-                  'codif': {}} | kwargs
-        return self.to_obj(keys=keys, typevalue=typevalue, modecodec=modecodec,
-                           codecval=codecval, simpleval=simpleval, parent=parent,
-                           **option)
+        - **value** : value to check
+        - **extern** : if True, compare value to external representation of self.value,
+        else, internal'''
+        if extern:
+            return value in self.val
+        return value in self.values
 
-    def to_pandas(self, func=None, codec=False, npdtype=None,
-                  series=True, index=True, numpy=False, **kwargs):
-        '''
-        Transform Iindex in a Pandas Series, Pandas DataFrame or Numpy array.
+    def keytoval(self, key, extern=True):
+        ''' return the value of a key
 
         *Parameters*
 
-        - **func** : function (default None) - function to apply for each value of the Iindex.
-        If func is the 'index' string, values are replaced by raw values.
-        - **npdtype** : string (default None) - numpy dtype for the Array ('object' if None)
-        - **series** : boolean (default True) - if True, return a Series. 
-        If False return a DataFrame
-        - **index** : boolean (default True) - if True, index is keys.
-        - **numpy** : boolean (default False) - if True, return a Numpy array.
-        - **kwargs** : parameters to apply to the func function
-
-        *Returns* : Pandas Series, Pandas DataFrame, Numpy Array'''
-        if len(self) == 0:
-            raise IindexError("Ilist is empty")
-        if npdtype:
-            npdtype = np.dtype(npdtype)
-        else:
-            npdtype = 'object'
-        if func is None:
-            func = identity
-        if func == 'index':
-            return np.array(list(range(len(self))))
+        - **key** : key to convert into values
+        - **extern** : if True, return string representation else, internal value
+
+        *Returns*
+
+        - **int** : first key finded (None else)'''
+        if key < 0 or key >= len(self._codec):
+            return None
+        if extern:
+            return self.cod[key]
+        return self._codec[key]
+
+    @staticmethod
+    def keysfromderkeys(parentkeys, derkeys):
+        '''return keys from parent keys and derkeys
+
+        *Parameters*
+
+        - **parentkeys** : list of keys from parent
+        - **derkeys** : list of derived keys
+
+        *Returns* : list of keys'''
+        return [derkeys[parentkeys[i]] for i in range(len(parentkeys))]
+
+    def loc(self, value, extern=True):
+        '''return a list of record number with value
+
+        *Parameters*
+
+        - **value** : value to check
+        - **extern** : if True, compare value to external representation of self.value,
+        else, internal
+
+        *Returns*
+
+        - **list of int** : list of record number finded (None else)'''
+        return self.recordfromvalue(value, extern=extern)
+
+    def recordfromvalue(self, value, extern=True):
+        '''return a list of record number with value
+
+        *Parameters*
+
+        - **value** : value to check
+        - **extern** : if True, compare value to external representation of self.value,
+        else, internal
+
+        *Returns*
+
+        - **list of int** : list of record number finded (None else)'''
+
+        if extern:
+            value = util.castval(
+                value, util.typename(self.name, ES.def_clsName))
+        if not value in self._codec:
+            return None
+        listkeys = [cod for cod, val in zip(
+            range(len(self._codec)), self._codec) if val == value]
+        return self.recordfromkeys(listkeys)
+
+    def recordfromkeys(self, listkeys):
+        '''return a list of record number with key in listkeys
+
+        *Parameters*
+
+        - **listkeys** : list of keys to check
+
+        *Returns*
+
+        - **list of int** : list of record number finded (None else)'''
+
+        return [rec for rec, key in zip(range(len(self)), self._keys) if key in listkeys]
+
+    def reindex(self, codec=None):
+        '''apply a reordered codec. If None, a new default codec is apply.
+
+        *Parameters*
+
+        - **codec** : list (default None) - reordered codec to apply.
+
+        *Returns* : self'''
+
         if not codec:
-            values = util.funclist(self.values, func, **kwargs)
-        else:
-            values = util.funclist(self._codec, func, **kwargs)
-        npdtype1 = npdtype
-        if isinstance(values[0], (datetime.datetime)):
-            npdtype1 = np.datetime64
-        # else:
-        #    npdtype=None
-        pdindex = None
-        if index:
-            pdindex = self._keys
-        try:
-            if numpy:
-                return np.array(values, dtype=npdtype1)
-            if series:
-                return pd.Series(values, dtype=npdtype1,
-                                 index=pdindex, name=self.name)
-            return pd.DataFrame(pd.Series(values, dtype=npdtype1,
-                                          index=pdindex, name=self.name))
-        except:
-            if numpy:
-                return np.array(values, dtype=npdtype)
-            if series:
-                return pd.Series(values, dtype=npdtype,
-                                 index=pdindex, name=self.name)
-            return pd.DataFrame(pd.Series(values, dtype=npdtype,
-                                          index=pdindex, name=self.name))
+            codec = util.tocodec(self.values)
+        self._keys = util.reindex(self._keys, self._codec, codec)
+        self._codec = codec
+        return self
 
-    def to_numpy(self, func=None, codec=False, npdtype=None, **kwargs):
-        '''
-        Transform Iindex in a Numpy array.
+    def reorder(self, sort=None, inplace=True):
+        '''Change the Iindex order with a new order define by sort and reset the codec.
 
         *Parameters*
 
-        - **func** : function (default None) - function to apply for each value of the Iindex.
-        If func is the 'index' string, values are replaced by raw values.
-        - **npdtype** : string (default None) - numpy dtype for the Array ('object' if None)
-        - **kwargs** : parameters to apply to the func function
+        - **sort** : int list (default None)- new record order to apply. If None, no change.
+        - **inplace** : boolean (default True) - if True, new order is apply to self,
+        if False a new Iindex is created.
+
+        *Returns*
+
+        - **Iindex** : self if inplace, new Iindex if not inplace'''
+        values = util.reorder(self.values, sort)
+        codec, keys = util.resetidx(values)
+        if inplace:
+            self._keys = keys
+            self._codec = codec
+            return None
+        return self.__class__(name=self.name, codec=codec, keys=keys)
+
+    def setcodecvalue(self, oldvalue, newvalue, extern=True, typevalue=None,
+                      nameonly=False, valueonly=False):
+        '''update all the oldvalue by newvalue
 
-        *Returns* : Numpy Array'''
-        return self.to_pandas(func=func, codec=codec, npdtype=npdtype, numpy=True, **kwargs)
+        *Parameters*
+
+        - **oldvalue** : list of values to replace
+        - **newvalue** : list of new value to apply
+        - **typevalue** : str (default None) - cast to apply to the new value
+        - **extern** : if True, the newvalue has external representation, else internal
+        - **nameonly** : if True, only the name of ESValue is changed
+        - **valueonly** : if True, only the value of ESValue is changed
+
+        *Returns* : int - last codec rank updated (-1 if None)'''
+        typevalue = util.typename(self.name, typevalue)
+        if extern:
+            newvalue = util.castval(newvalue, typevalue)
+            oldvalue = util.castval(oldvalue, typevalue)
+        rank = -1
+        for i in range(len(self._codec)):
+            if self._codec[i] == oldvalue:
+                if typevalue in ES.ESclassName and nameonly:
+                    self._codec[i].setName(newvalue.name)
+                elif typevalue in ES.ESclassName and valueonly:
+                    self._codec[i].setValue(newvalue.value)
+                self._codec[i] = newvalue
+                rank = i
+        return rank
 
-    def to_obj(self, keys=None, typevalue=None, simpleval=False, modecodec='optimize',
-               codecval=False, parent=ES.nullparent, name=True, listunic=False,
-               **kwargs):
-        '''Return a formatted object (string, bytes or dict) for the Iindex
+    def setcodeclist(self, listcodec, extern=True, typevalue=None, nameonly=False, valueonly=False):
+        '''update codec with listcodec values
 
         *Parameters*
 
-        - **modecodec** : string (default 'optimize') - json mode
-        - **keys** : list (default None) - list: List of keys to include - None or False:
-        no list - else: Iindex keys
-        - **typevalue** : string (default None) - type to convert values
-        - **name** : boolean (default True) - if False, name is not included
-        - **codecval** : boolean (default False) - if True, only list of codec values is included
-        - **simpleval** : boolean (default False) - if True, only value (without name) is included
-        - **listunic** : boolean (default False) - if False, when len(result)=1
-        return value not list
-        - **parent** : integer (default None) - index number of the parent in indexset
+        - **listcodec** : list of new codec values to apply
+        - **typevalue** : str (default None) - cast to apply to the new value
+        - **extern** : if True, the newvalue has external representation, else internal
+        - **nameonly** : if True, only the name of ESValue is changed
+        - **valueonly** : if True, only the value of ESValue is changed
 
-        *Parameters (kwargs)*
+        *Returns* : int - last codec rank updated (-1 if None)'''
+        typevalue = util.typename(self.name, typevalue)
+        if extern:
+            listcodec = util.castobj(listcodec, typevalue)
+        for i in range(len(self._codec)):
+            if typevalue in ES.ESclassName and nameonly:
+                self._codec[i].setName(listcodec[i].name)
+            elif typevalue in ES.ESclassName and valueonly:
+                self._codec[i].setValue(listcodec[i].value)
+            else:
+                self._codec[i] = listcodec[i]
+
+    def set_keys(self, keys):
+        ''' _keys setters '''
+        self._keys = keys
+
+    def set_codec(self, codec):
+        ''' _codec setters '''
+        self._codec = codec
 
-        - **encoded** : boolean (default False) - choice for return format
-        (string/bytes if True, dict else)
-        - **encode_format**  : string (default 'json')- choice for return format (json, cbor)
-        - **codif** : dict (default ES.codeb). Numerical value for string in CBOR encoder
-        - **untyped** : boolean (default False) - include dtype if True
-        - **geojson** : boolean (default False) - geojson for LocationValue if True
+    def setkeys(self, keys, inplace=True):
+        '''apply new keys (replace codec with extended codec from parent keys)
 
-        *Returns* : string, bytes or dict'''
-        keyslist = None
-        if not name or self.name == ES.defaultindex:
-            idxname = None
-        else:
-            idxname = self.name
-        if modecodec == 'full':
-            codeclist = self.values
-            keyslist = None
-        elif modecodec == 'default':
-            codeclist = self._codec
-            keyslist = self._keys
-        else:
-            codeclist = self._codec
-            if keys and isinstance(keys, list):
-                keyslist = keys
-            elif keys and not isinstance(keys, list):
-                keyslist = self._keys
-        if typevalue:
-            dtype = ES.valname[typevalue]
+        *Parameters*
+
+        - **keys** : list of keys to apply
+        - **inplace** : if True, update self data, else create a new Iindex
+
+        *Returns* : self or new Iindex'''
+        codec = util.tocodec(self.values, keys)
+        if inplace:
+            self._codec = codec
+            self._keys = keys
+            return self
+        return self.__class__(codec=codec, name=self.name, keys=keys)
+
+    def setname(self, name):
+        '''update the Iindex name
+
+        *Parameters*
+
+        - **name** : str to set into name
+
+        *Returns* : boolean - True if update'''
+        if isinstance(name, str):
+            self.name = name
+            return True
+        return False
+
+    def setvalue(self, ind, value, extern=True, typevalue=None, nameonly=False, valueonly=False):
+        '''update a value at the rank ind (and update codec and keys)
+
+        *Parameters*
+
+        - **ind** : rank of the value
+        - **value** : new value
+        - **extern** : if True, the value has external representation, else internal
+        - **typevalue** : str (default None) - cast to apply to the new value
+        - **nameonly** : if True, only the name of ESValue is changed
+        - **valueonly** : if True, only the value of ESValue is changed
+
+        *Returns* : None'''
+        typevalue = util.typename(self.name, typevalue)
+        if extern:
+            value = util.castval(value, typevalue)
+        values = self.values
+        if typevalue in ES.ESclassName and nameonly:
+            values[ind].setName(values.name)
+        elif typevalue in ES.ESclassName and valueonly:
+            values[ind].setValue(values.value)
         else:
-            dtype = None
-        return IindexInterface.encodeobj(codeclist, keyslist, idxname, simpleval,
-                                         codecval, dtype, parent, listunic,
-                                         modecodec, **kwargs)
-
-    def to_dict_obj(self, typevalue=None, simpleval=False, modecodec='optimize', **kwargs):
-        option = {'encoded': False, 'encode_format': 'json', 'untyped': False,
-                  'codif': {}, 'geojson': False} | kwargs
-        dic = {}
-        if self.typevalue:
-            dic['type'] = self.typevalue
-        ds = pd.Series(range(len(self.keys)), index=self.keys, dtype='int64')
-        dic['value'] = [{'record': ds[i].tolist(),
-                         'codec': util.json(cod, encoded=False, typevalue=None,
-                                            simpleval=simpleval, modecodec=modecodec,
-                                            untyped=option['untyped'], geojson=option['geojson'])}
-                        for i, cod in enumerate(self.codec)]
-        return {self.name: dic}
+            values[ind] = value
+        self._codec, self._keys = util.resetidx(values)
 
-    def vlist(self, func, *args, extern=True, **kwargs):
-        '''
-        Apply a function to values and return the result.
+    def setlistvalue(self, listvalue, extern=True, typevalue=None, nameonly=False, valueonly=False):
+        '''update the values (and update codec and keys)
 
         *Parameters*
 
-        - **func** : function - function to apply to values
-        - **args, kwargs** : parameters for the function
-        - **extern** : if True, the function is apply to external values, else internal
+        - **listvalue** : list - list of new values
+        - **typevalue** : str (default None) - class to apply to the new value
+        - **extern** : if True, the value has external representation, else internal
+        - **nameonly** : if True, only the name of ESValue is changed
+        - **valueonly** : if True, only the value of ESValue is changed
 
-        *Returns* : list of func result'''
+        *Returns* : None'''
+        typevalue = util.typename(self.name, typevalue)
         if extern:
-            return util.funclist(self.val, func, *args, **kwargs)
-        return util.funclist(self.values, func, *args, **kwargs)
+            listvalue = util.castobj(listvalue, typevalue)
+        values = self.values
+        for i, value_i in enumerate(listvalue):
+            if typevalue in ES.ESclassName and nameonly:
+                values[i].setName(value_i.name)
+            elif typevalue in ES.ESclassName and valueonly:
+                values[i].setValue(value_i.value)
+            else:
+                values[i] = value_i
+        self._codec, self._keys = util.resetidx(values)
+
+    def sort(self, reverse=False, inplace=True, func=str):
+        '''Define sorted index with ordered codec.
+
+        *Parameters*
 
-    def vName(self, default=ES.nullName, maxlen=None):
+        - **reverse** : boolean (defaut False) - codec is sorted with reverse order
+        - **inplace** : boolean (default True) - if True, new order is apply to self,
+        if False a new Iindex is created.
+        - **func**    : function (default str) - key used in the sorted function
+
+        *Return*
+
+        - **Iindex** : self if inplace, new Iindex if not inplace'''
+        if inplace:
+            self.reindex(codec=sorted(self._codec, reverse=reverse, key=func))
+            self._keys.sort()
+            return self
+        oldcodec = self._codec
+        codec = sorted(oldcodec, reverse=reverse, key=str)
+        return self.__class__(name=self.name, codec=codec,
+                              keys=sorted(util.reindex(self._keys, oldcodec, codec)))
+
+    def tocoupled(self, other, coupling=True):
         '''
-        Return the list of name for ESValue data .
+        Transform a derived index in a coupled index (keys extension) and add
+        new values to have the same length as other.
 
         *Parameters*
 
-        - **default** : value return if no name is available
-        - **maxlen** : integer (default None) - max length of name
+        - **other** : index to be coupled.
+        - **coupling** : boolean (default True) - reindex if False
 
-        *Returns* : list of name founded'''
-        return [util.cast(val, dtype='name', default=default, maxlen=maxlen) for val in self.values]
+        *Returns* : None'''
+        dic = util.idxlink(other._keys, self._keys)
+        if not dic:
+            raise IindexError("Iindex is not coupled or derived from other")
+        self._codec = [self._codec[dic[i]] for i in range(len(dic))]
+        self._keys = other._keys
+        if not coupling:
+            self.reindex()
 
-    def vSimple(self, string=False):
+    def tostdcodec(self, inplace=False, full=True):
         '''
-        Apply a vSimple function to values and return the result.
+        Transform codec in full or in default codec.
+
+        *Parameters*
+
+        - **inplace** : boolean (default True) - if True, new order is apply to self,
+        - **full** : boolean (default True) - if True reindex with full codec
+
+        *Return*
+
+        - **Iindex** : self if inplace, new Iindex if not inplace'''
+        if full:
+            codec = self.values
+            keys = list(range(len(codec)))
+        else:
+            codec = util.tocodec(self.values)
+            keys = util.reindex(self._keys, self._codec, codec)
+        if inplace:
+            self._codec = codec
+            self._keys = keys
+            return self
+        return self.__class__(codec=codec, name=self.name, keys=keys, castobj=False)
+
+    def valrow(self, row):
+        ''' return json val for a record
 
         *Parameters*
 
-        - **string** : boolean(default False) - if True the values returned are string
+        - **row** : record to obtain val
 
-        *Returns* : list of vSimple values (string or not)'''
-        if string:
-            return json.dumps([util.cast(val, 'simple', string=string) for val in self.values],
-                              cls=ESValueEncoder)
-        return [util.cast(val, 'simple', string=string) for val in self.values]
+        *Returns* : val[row]'''
+        val = ESValue.uncastsimple(self._codec[self._keys[row]])
+        if isinstance(val, (str, int, float, bool, list, dict, type(None), bytes)):
+            return val
+        return val.json(encoded=False)
+
+    def valtokey(self, value, extern=True):
+        '''convert a value to a key
+
+        *Parameters*
+
+        - **value** : value to convert
+        - **extern** : if True, the value has external representation, else internal
+
+        *Returns*
+
+        - **int** : first key finded (None else)'''
+        if extern:
+            value = util.castval(
+                value, util.typename(self.name, ES.def_clsName))
+        if value in self._codec:
+            return self._codec.index(value)
+        return None
```

### Comparing `observation-0.0.4/observation/iindex_structure.py` & `observation-0.0.5/observation/timeslot.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,607 +1,647 @@
 # -*- coding: utf-8 -*-
 """
-Created on Sun Oct  2 22:24:59 2022
+Created on Sun Jan  2 18:30:14 2022
 
-@author: philippe@loco-labs.io
+@author: Philippe@loco-labs.io
 
-The `observation.iindex_structure` module contains the `IindexStructure` class
-(`observation.iindex.Iindex` methods).
-"""
-from collections import defaultdict, Counter
-
-from esvalue_base import ESValue
-from util import util
-from esconstante import ES
-from iindex_interface import IindexError
-
-
-class IindexStructure:
-    '''this class includes Iindex methods :
-
-    *add - update methods*
-
-    - `IindexStructure.append`
-    - `IindexStructure.setcodecvalue`
-    - `IindexStructure.setcodeclist`
-    - `IindexStructure.setname`
-    - `IindexStructure.setkeys`
-    - `IindexStructure.setlistvalue`
-    - `IindexStructure.setvalue`
-
-    *transform methods*
-
-    - `IindexStructure.coupling`
-    - `IindexStructure.extendkeys`
-    - `IindexStructure.full`
-    - `IindexStructure.reindex`
-    - `IindexStructure.reorder`
-    - `IindexStructure.sort`
-    - `IindexStructure.tocoupled`
-    - `IindexStructure.tostdcodec`
-
-    *getters methods*
-
-    - `IindexStructure.couplinginfos`
-    - `IindexStructure.derkeys`
-    - `IindexStructure.getduplicates`
-    - `IindexStructure.iscrossed`
-    - `IindexStructure.iscoupled`
-    - `IindexStructure.isderived`
-    - `IindexStructure.islinked`
-    - `IindexStructure.isvalue`
-    - `IindexStructure.iskeysfromderkeys`
-    - `IindexStructure.keysfromderkeys`
-    - `IindexStructure.keytoval`
-    - `IindexStructure.loc`
-    - `IindexStructure.recordfromkeys`
-    - `IindexStructure.recordfromvalue`
-    - `IindexStructure.valtokey`  '''
-
-    def append(self, value,  typevalue=ES.def_clsName, unique=True):
-        '''add a new value
-
-        *Parameters*
-
-        - **value** : new object value
-        - **typevalue** : string (default ES.def_clsName) - typevalue to apply to value
-        - **unique** :  boolean (default True) - If False, duplication codec if value is present
-
-        *Returns* : key of value '''
-        value = util.castval(value, util.typename(self.name, typevalue))
-        if value in self._codec and unique:
-            key = self._codec.index(value)
-        else:
-            key = len(self._codec)
-            self._codec.append(value)
-        self._keys.append(key)
-        return key
+The `python.observation.timeslot` module contains the `TimeSlot` and the `TimeInterval` classes.
 
-    def coupling(self, idx, derived=True, duplicate=True):
-        '''
-        Transform indexes in coupled or derived indexes (codec extension).
-        If derived option is True, self._codec is extended and idx codec not,
-        else, both are coupled and both codec are extended.
+# What is the TimeSlot Object ?
 
-        *Parameters*
+The TimeSlot Object is a representation of time intervals data and properties. For example,
+ I can represent the working day of 2022-march-15 by a TimeSlot which includes the following intervals:
+- from 9 a.m. to 12 p.m.
+- from 2 p.m. to 4:30 p.m.
+- from 5 p.m. to 7:30 p.m.
+i.e. a duration of 8 hours centered around 3 p.m. with bounds at 9 a.m. and 7:30 p.m.
 
-        - **idx** : single Iindex or list of Iindex to be coupled or derived.
-        - **derived** : boolean (default : True) - if True result is derived,
-        if False coupled
-        - **duplicate** : boolean (default: True) - if True, return duplicate records
-
-        *Returns* : tuple with duplicate records (errors) if 'duplicate', None else'''
-        if not isinstance(idx, list):
-            index = [idx]
-        else:
-            index = idx
-        idxzip = self.__class__.ext(list(zip(*([self._keys] + [ix._keys for ix in index]))),
-                                    typevalue=None)
-        self.tocoupled(idxzip)
-        if not derived:
-            for ind in index:
-                ind.tocoupled(idxzip)
-        if duplicate:
-            return self.getduplicates()
-        return
-
-    def couplinginfos(self, other, default=False):
-        '''return a dict with the coupling info between other (distance, rate,
-        dist, disttomin, disttomax, distmin, distmax, diff, typecoupl)
+# Main principles
 
-        *Parameters*
+The main principles are as follows :
 
-        - **other** : other index to compare
-        - **default** : comparison with default codec
+<img src="./timeslot_data_structure.png" width="800">
+    
+## Data structure
 
-        *Returns* : dict'''
-        if default:
-            return util.couplinginfos(self.values, other.values)
-        if min(len(self), len(other)) == 0:
-            return {'dist': 0, 'distrate': 0, 'disttomin': 0, 'disttomax': 0,
-                    'distmin': 0, 'distmax': 0, 'diff': 0, 'typecoupl': 'null',
-                    'distance': 0, 'rate': 0}
-        lens = len(self._codec)
-        leno = len(other._codec)
-        xmin = max(lens, leno)
-        xmax = lens * leno
-        diff = abs(lens - leno)
-        if min(lens, leno) == 1:
-            rate = 0
-            if xmax - xmin + diff != 0:
-                rate = diff / (xmax - xmin + diff)
-            if lens == 1:
-                typec = 'derived'
-            else:
-                typec = 'derive'
-            return {'dist': xmin, 'distrate': 0, 'disttomin': 0, 'disttomax': 0,
-                    'distmin': xmin, 'distmax': xmax, 'diff': diff,
-                    'typecoupl': typec, 'distance': diff, 'rate': rate}
-        xso = len(util.tocodec([tuple((v1, v2))
-                  for v1, v2 in zip(self._keys, other._keys)]))
-        dic = {'dist': xso, 'distrate': (xso - xmin) / (xmax - xmin),
-               'disttomin': xso - xmin,  'disttomax': xmax - xso,
-               'distmin': xmin, 'distmax': xmax, 'diff': diff,
-               'distance': xso - xmin + diff,
-               'rate': (xso - xmin + diff) / (xmax - xmin + diff)}
-        if dic['distrate'] == 0 and dic['diff'] == 0:
-            dic['typecoupl'] = 'coupled'
-        elif dic['distrate'] == 0 and lens < leno:
-            dic['typecoupl'] = 'derived'
-        elif dic['distrate'] == 0 and lens > leno:
-            dic['typecoupl'] = 'derive'
-        elif dic['distrate'] == 1:
-            dic['typecoupl'] = 'crossed'
-        elif lens < leno:
-            dic['typecoupl'] = 'linked'
-        else:
-            dic['typecoupl'] = 'link'
-        return dic
+A `TimeSlot` is a list of `TimeInterval`.
 
-    def derkeys(self, parent):
-        '''return keys derived from parent keys
+A `TimeInterval` is defined by two `datetime` objects (start and end)
 
-        *Parameters*
+Multiple properties are associated with the data :
+    
+- duration : sum of the lenght of each TimeInterval
+- centroïd : instant assicited to the middle of the duration
+- bounds : minimum, maximum and middle
+- type : instant, interval or slot
 
-        - **parent** : Iindex - parent
+## Relationships and assembly
 
-        *Returns* : list of keys'''
-        derkey = [ES.nullparent] * len(parent._codec)
-        for i in range(len(self)):
-            derkey[parent._keys[i]] = self._keys[i]
-        if min(derkey) < 0:
-            raise IindexError("parent is not a derive Iindex")
-        return derkey
+Two `TimeSlot` can be compared with five statuses (equals, contains, within, disjoint, intersects).
 
-    def extendkeys(self, keys):
-        '''add keys to the Iindex
+Multiple operations between two objects can be performed :
+    
+- union between two `TimeSlot`
+- intersection between two `TimeSlot`
+- complementing a `TimeSlot` in an interval
 
-        *Parameters*
+"""
+import datetime
+import json
+import numpy
+import pandas
+import bson
 
-        - **keys** : list of int (value lower or equal than actual keys)
+from observation.esconstante import ES  # , _identity
 
-        *Returns* : None '''
-        if min(keys) < 0 or max(keys) > len(self._codec) - 1:
-            raise IindexError('keys not consistent with codec')
-        self._keys += keys
 
-    @staticmethod
-    def full(listidx):
-        '''tranform a list of indexes in crossed indexes (value extension).
+class TimeSlotEncoder(json.JSONEncoder):
+    """add a new json encoder for TimeSlot"""
 
-        *Parameters*
+    def default(self, o):
+        if isinstance(o, datetime.datetime):
+            return o.isoformat()
+        return json.JSONEncoder.default(self, o)
 
-        - **listidx** : list of Iindex to transform
 
-        *Returns* : tuple of records added '''
-        idx1 = listidx[0]
-        for idx in listidx:
-            if len(idx) != len(idx):
-                return None
-        leninit = len(idx1)
-        keysadd = util.idxfull(listidx)
-        for idx, keys in zip(listidx, keysadd):
-            idx._keys += keys
-        return tuple(range(leninit, len(idx1)))
-
-    def getduplicates(self):
-        ''' return tuple of items with duplicate codec'''
-        count = Counter(self._codec)
-        defcodec = list(count - Counter(list(count)))
-        dkeys = defaultdict(list)
-        for key, ind in zip(self._keys, range(len(self))):
-            dkeys[key].append(ind)
-        dcodec = defaultdict(list)
-        for key, ind in zip(self._codec, range(len(self._codec))):
-            dcodec[key].append(ind)
-        duplicates = []
-        for item in defcodec:
-            for codecitem in dcodec[item]:
-                duplicates += dkeys[codecitem]
-        return tuple(duplicates)
-
-    def iscrossed(self, other):
-        '''return True if self is crossed to other'''
-        return self.couplinginfos(other)['distrate'] == 1.0
-
-    def iscoupled(self, other):
-        '''return True if self is coupled to other'''
-        info = self.couplinginfos(other)
-        return info['diff'] == 0 and info['distrate'] == 0
-
-    def isderived(self, other):
-        '''return True if self is derived from other'''
-        info = self.couplinginfos(other)
-        return info['diff'] != 0 and info['distrate'] == 0.0
-
-    def iskeysfromderkeys(self, other):
-        '''return True if self._keys is relative from other._keys'''
-        leng = len(other._codec)
-        if leng % len(self._codec) != 0:
-            return False
-        keys = [(i*len(self._codec))//leng for i in range(leng)]
-        return self.__class__.keysfromderkeys(other._keys, keys) == self._keys
+class TimeSlot:
+    '''        
+    *Attributes (for @property see methods)* :
 
-    def islinked(self, other):
-        '''return True if self is linked to other'''
-        rate = self.couplinginfos(other)['distrate']
-        return 0.0 < rate < 1.0
+    - **slot** : list of `TimeInterval`
 
-    def isvalue(self, value, extern=True):
-        ''' return True if value is in index values
+    The methods defined in this class are : 
 
-        *Parameters*
+    *dynamic value property (getters)*
 
-        - **value** : value to check
-        - **extern** : if True, compare value to external representation of self.value,
-        else, internal'''
-        if extern:
-            return value in self.val
-        return value in self.values
+    - `TimeSlot.Bounds`
+    - `TimeSlot.bounds`
+    - `TimeSlot.Centroid`
+    - `TimeSlot.duration`
+    - `TimeSlot.instant`
+    - `TimeSlot.middle`
+    - `TimeSlot.interval`
+    - `TimeSlot.stype`
 
-    def keytoval(self, key, extern=True):
-        ''' return the value of a key
-
-        *Parameters*
-
-        - **key** : key to convert into values
-        - **extern** : if True, return string representation else, internal value
-
-        *Returns*
+    *instance methods*
 
-        - **int** : first key finded (None else)'''
-        if key < 0 or key >= len(self._codec):
-            return None
-        if extern:
-            return self.cod[key]
-        return self._codec[key]
+    - `TimeSlot.json`
+    - `TimeSlot.link`
+    - `TimeSlot.timetuple`
+    - `TimeSlot.union`
+    '''
 
-    @staticmethod
-    def keysfromderkeys(parentkeys, derkeys):
-        '''return keys from parent keys and derkeys
+    def __init__(self, val=None):
+        '''
+        TimeSlot constructor.
 
         *Parameters*
 
-        - **parentkeys** : list of keys from parent
-        - **derkeys** : list of derived keys
-
-        *Returns* : list of keys'''
-        return [derkeys[parentkeys[i]] for i in range(len(parentkeys))]
-
-    def loc(self, value, extern=True):
-        '''return a list of record number with value
-
-        *Parameters*
+        - **val** : date, interval, list of interval (default None) - with several formats 
+        (tuple, list, string, datetime, TimeSlot, TimeInterval, numpy datetime64, pandas timestamp)
 
-        - **value** : value to check
-        - **extern** : if True, compare value to external representation of self.value,
-        else, internal
+        *Returns* : None'''
+        slot = []
+        if isinstance(val, str):
+            try:
+                val = json.loads(val)
+            except:
+                val = TimeInterval._dattz(datetime.datetime.fromisoformat(val))
+                # try:    val = TimeInterval._dattz(datetime.datetime.fromisoformat(val))
+                # except: val = None
+        if val == None:
+            self.slot = slot
+            return
+        val = TimeSlot._listed(val)
+        #if isinstance(val, tuple): val = list(val)
+        if isinstance(val, list) and len(val) == 2 and not isinstance(val[0], TimeInterval):
+            try:
+                slot.append(TimeInterval(val))
+            except:
+                for interv in val:
+                    slot.append(TimeInterval(interv))
+        elif isinstance(val, list):
+            try:
+                for interv in val:
+                    slot.append(TimeInterval(interv))
+            except:
+                slot.append(TimeInterval(val))
+        elif isinstance(val, datetime.datetime):
+            slot.append(TimeInterval(val))
+        elif isinstance(val, TimeSlot):
+            slot = val.slot
+        elif isinstance(val, TimeInterval):
+            slot.append(val)
+        else:
+            slot.append(TimeInterval(val))
+        self.slot = TimeSlot._reduced(slot)
 
-        *Returns*
+    def __add__(self, other):
+        ''' Add other's values to self's values in a new TimeSlot'''
+        return TimeSlot(TimeSlot._reduced(self.slot + other.slot))
+
+    def __iadd__(self, other):
+        ''' Add other's values to self's values'''
+        self.slot = self._reduced(self.slot + other.slot)
+
+    def __contains__(self, item):
+        ''' item of extval'''
+        return item in self.slot
+
+    def __getitem__(self, index):
+        ''' return interval item'''
+        return self.slot[index]
+
+    def __setitem__(self, index, interv):
+        ''' modify interval item'''
+        if index < 0 or index >= len(self):
+            raise TimeSlotError("out of bounds")
+        self.slot[index] = TimeInterval(interv)
+        self.slot = TimeSlot._reduced(self.slot)
+
+    def __len__(self):
+        '''return the number of intervals included'''
+        return len(self.slot)
+
+    # def __repr__(self):
+    def __str__(self):
+        ''' return the type of slot and the json representation'''
+        return self.stype + '\n' + self.json(encoded=True, encode_format='json')
+
+    def __repr__(self):
+        # return self.__class__.__name__ + f'({self.slot})'
+        return self.__class__.__name__ + '(' + self.json(encoded=True, encode_format='json') + ')'
+
+    def __eq__(self, other):
+        '''equal if the slots are equals'''
+        try:
+            return self.slot == other.slot
+        except:
+            return False
 
-        - **list of int** : list of record number finded (None else)'''
-        return self.recordfromvalue(value, extern=extern)
+    def __lt__(self, other):
+        '''compare the earliest dates'''
+        return self.slot[0] < other.slot[0]
+
+    def __hash__(self):
+        return sum(hash(interv) for interv in self.slot)
+        # return hash(self.json(True))
+
+    @property
+    def Bounds(self):
+        '''return an interval TimeSlot with the bounds of the TimeSlot object'''
+        return TimeSlot(self.bounds)
+
+    @property
+    def bounds(self):
+        '''return a tuple with the start and end dates with isoformat string'''
+        return (TimeSlot.form(self.slot[0].start), TimeSlot.form(self.slot[len(self) - 1].end))
 
-    def recordfromvalue(self, value, extern=True):
-        '''return a list of record number with value
+    @classmethod
+    def cast(cls, value):
+        '''
+        tranform a value (unique or list) in a list of `TimeSlot`
 
         *Parameters*
 
-        - **value** : value to check
-        - **extern** : if True, compare value to external representation of self.value,
-        else, internal
+        - **value** : value to transform
 
         *Returns*
 
-        - **list of int** : list of record number finded (None else)'''
-
-        if extern:
-            value = util.castval(
-                value, util.typename(self.name, ES.def_clsName))
-        if not value in self._codec:
-            return None
-        listkeys = [cod for cod, val in zip(
-            range(len(self._codec)), self._codec) if val == value]
-        return self.recordfromkeys(listkeys)
-
-    def recordfromkeys(self, listkeys):
-        '''return a list of record number with key in listkeys
-
-        *Parameters*
-
-        - **listkeys** : list of keys to check
+        - **list** : list of `TimeSlot`
+        '''
+        if isinstance(value, list):
+            try:
+                return [cls(val) for val in value]
+            except:
+                return [cls(value)]
+        else:
+            return [cls(value)]
 
-        *Returns*
+    @property
+    def Centroid(self):
+        '''return a TimeSlot with the date corresponding to the middle of the duration'''
+        return TimeSlot(self.instant)
+
+    @property
+    def duration(self):
+        '''cumulative duration of each interval (timedelta format)'''
+        duration = datetime.timedelta()
+        for interv in self.slot:
+            duration += interv.duration
+        return duration
 
-        - **list of int** : list of record number finded (None else)'''
+    @staticmethod
+    def form(dtime):
+        if dtime.timetuple()[3:6] == (0, 0, 0):
+            return dtime.date().isoformat()
+        return dtime.isoformat()
+
+    @property
+    def instant(self):
+        '''return the date corresponding to the middle of the duration (datetime format)'''
+        duration = self.duration / 2
+        for interv in self.slot:
+            if duration > interv.duration:
+                duration -= interv.duration
+            else:
+                return interv.start + duration
 
-        return [rec for rec, key in zip(range(len(self)), self._keys) if key in listkeys]
+    @property
+    def middle(self):
+        '''return the date corresponding to the middle of the bounds (datetime format)'''
+        return self.bounds.instant
+
+    @property
+    def name(self):
+        ''' class name'''
+        return self.__class__.__name__
+
+    @property
+    def interval(self):
+        '''return a list with the start and end dates (datetime format)'''
+        return [self.slot[0].start, self.slot[len(self) - 1].end]
+
+    @property
+    def stype(self):
+        '''return a string with the type of TimeSlot (instant, interval, slot)'''
+        if len(self.slot) == 1:
+            return self.slot[0].stype
+        else:
+            return 'slot'
 
-    def reindex(self, codec=None):
-        '''apply a reordered codec. If None, a new default codec is apply.
+    def json(self, **kwargs):
+        '''
+        Return json/bson structure with the list of TimeInterval.
 
         *Parameters*
 
-        - **codec** : list (default None) - reordered codec to apply.
-
-        *Returns* : self'''
+        - **encoded** : defaut False - if False return dict, else return json string/bson bytes
+        - **encode_format** : defaut 'json' - return json, bson or cbor format
 
-        if not codec:
-            codec = util.tocodec(self.values)
-        self._keys = util.reindex(self._keys, self._codec, codec)
-        self._codec = codec
-        return self
+        *Returns* : string or dict'''
+        option = {'encoded': False, 'encode_format': 'json'} | kwargs
+        if len(self) == 1:
+            js = self.slot[0].json(
+                encoded=False, encode_format=option['encode_format'])
+        else:
+            js = [interv.json(
+                encoded=False, encode_format=option['encode_format']) for interv in self.slot]
+        if option['encoded'] and option['encode_format'] == 'json':
+            return json.dumps(js, cls=TimeSlotEncoder)
+        if option['encoded'] and option['encode_format'] == 'bson':
+            return bson.encode(js)
+        return js
 
-    def reorder(self, sort=None, inplace=True):
-        '''Change the Iindex order with a new order define by sort and reset the codec.
+    def link(self, other):
+        '''
+        Return the status (string) of the link between two TimeSlot (self and other).
+        - equals     : if self and other are the same
+        - disjoint   : if self's intervals and other's intervals are all disjoint
+        - within     : if all self's intervals are included in other's intervals
+        - contains   : if all other's intervals are included in self's intervals
+        - intersects : in the others cases
 
         *Parameters*
 
-        - **sort** : int list (default None)- new record order to apply. If None, no change.
-        - **inplace** : boolean (default True) - if True, new order is apply to self,
-        if False a new Iindex is created.
+        - **other** : TimeSlot to be compared
 
-        *Returns*
+        *Returns* 
 
-        - **Iindex** : self if inplace, new Iindex if not inplace'''
-        values = util.reorder(self.values, sort)
-        codec, keys = util.resetidx(values)
-        if inplace:
-            self._keys = keys
-            self._codec = codec
-            return None
-        return self.__class__(name=self.name, codec=codec, keys=keys)
+        - **tuple** : (string(status), boolean(full or not))'''
+        if self.stype == 'instant':
+            point, oslot = self[0], other
+        elif other.stype == 'instant':
+            point, oslot = other[0], self
+        else:
+            point = None
+        if point is not None:
+            contains = equals = False
+            for interv in oslot:
+                contains = contains or interv.link(point) == 'contains'
+                equals = equals or interv.link(point) == 'equals'
+            if equals and not contains:
+                return ('equals', True)
+            if contains and point == other[0]:
+                return ('contains', True)
+            if contains and point == self[0]:
+                return ('within', True)
+            return ('disjoint', True)
+        else:
+            union = self + other
+            link = 'intersects'
+            full = True
+            if union.duration == self.duration == other.duration:
+                full = len(union) == len(self) == len(other)
+                link = 'equals'
+            elif union.duration == self.duration:
+                full = len(union) == len(self)
+                link = 'contains'
+            elif union.duration == other.duration:
+                full = len(union) == len(other)
+                link = 'within'
+            elif union.duration == self.duration + other.duration:
+                full = len(union) == len(self) + len(other)
+                link = 'disjoint'
+            return (link, full)
 
-    def setcodecvalue(self, oldvalue, newvalue, extern=True, typevalue=None,
-                      nameonly=False, valueonly=False):
-        '''update all the oldvalue by newvalue
+    def timetuple(self, index=0, encoded=False):
+        '''
+        Return json structure with the list of TimeInterval (timetuple filter).
 
         *Parameters*
 
-        - **oldvalue** : list of values to replace
-        - **newvalue** : list of new value to apply
-        - **typevalue** : str (default None) - cast to apply to the new value
-        - **extern** : if True, the newvalue has external representation, else internal
-        - **nameonly** : if True, only the name of ESValue is changed
-        - **valueonly** : if True, only the value of ESValue is changed
-
-        *Returns* : int - last codec rank updated (-1 if None)'''
-        typevalue = util.typename(self.name, typevalue)
-        if extern:
-            newvalue = util.castval(newvalue, typevalue)
-            oldvalue = util.castval(oldvalue, typevalue)
-        rank = -1
-        for i in range(len(self._codec)):
-            if self._codec[i] == oldvalue:
-                if typevalue in ES.ESclassName and nameonly:
-                    self._codec[i].setName(newvalue.name)
-                elif typevalue in ES.ESclassName and valueonly:
-                    self._codec[i].setValue(newvalue.value)
-                self._codec[i] = newvalue
-                rank = i
-        return rank
-
-    def setcodeclist(self, listcodec, extern=True, typevalue=None, nameonly=False, valueonly=False):
-        '''update codec with listcodec values
+        - **index** : integer, defaut 0 - timetuple format to apply :
+            - 0 : year
+            - 1 : month
+            - 2 : day
+            - 3 : hour
+            - 4 : minute
+            - 5 : seconds
+            - 6 : weekday
+            - 7 : yearday
+            - 8 : isdst (1 when daylight savings time is in effect, 0 when is not)
+        - **encoded** : defaut False - if True return string, else return dict
+
+        *Returns* : string or dict'''
+        if len(self) == 1:
+            js = self.slot[0].timetuple(index, False)
+        else:
+            js = [interv.timetuple(index, False) for interv in self.slot]
+        if encoded:
+            return json.dumps(js, cls=TimeSlotEncoder)
+        else:
+            return js
 
-        *Parameters*
+    def union(self, other):
+        ''' Add other's values to self's values in a new TimeSlot (same as __add__)'''
+        return self.__add__(other)
 
-        - **listcodec** : list of new codec values to apply
-        - **typevalue** : str (default None) - cast to apply to the new value
-        - **extern** : if True, the newvalue has external representation, else internal
-        - **nameonly** : if True, only the name of ESValue is changed
-        - **valueonly** : if True, only the value of ESValue is changed
-
-        *Returns* : int - last codec rank updated (-1 if None)'''
-        typevalue = util.typename(self.name, typevalue)
-        if extern:
-            listcodec = util.castobj(listcodec, typevalue)
-        for i in range(len(self._codec)):
-            if typevalue in ES.ESclassName and nameonly:
-                self._codec[i].setName(listcodec[i].name)
-            elif typevalue in ES.ESclassName and valueonly:
-                self._codec[i].setValue(listcodec[i].value)
-            else:
-                self._codec[i] = listcodec[i]
+    @staticmethod
+    def _reduced(listinterv):
+        ''' return an ordered and non-overlapping list of TimeInterval from any TimeInterval list'''
+        if not isinstance(listinterv, list) or len(listinterv) == 0:
+            return []
+        union = []
+        slot = sorted(listinterv)
+        interv = slot[0]
+        i = j = 0
+        while i < len(slot):
+            for j in range(i + 1, len(slot)):
+                if interv.link(slot[j]) == 'within':
+                    interv = slot[j]
+                elif interv.link(slot[j]) == 'intersects':
+                    interv = interv.union(slot[j])
+                elif interv.link(slot[j]) == 'disjoint':
+                    union.append(interv)
+                    interv = slot[j]
+                    i = j
+                    break
+            if j >= len(slot) - 1:
+                union.append(interv)
+                break
+        return union
 
-    def set_keys(self, keys):
-        ''' _keys setters '''
-        self._keys = keys
-
-    def set_codec(self, codec):
-        ''' _codec setters '''
-        self._codec = codec
+    @staticmethod
+    def _listed(idx):
+        '''transform a tuple of tuple in a list of list'''
+        if not isinstance(idx, str) and hasattr(idx, '__iter__'):
+            return [val if not isinstance(val, tuple) else TimeSlot._listed(val) for val in idx]
+        return idx
 
-    def setkeys(self, keys, inplace=True):
-        '''apply new keys (replace codec with extended codec from parent keys)
 
-        *Parameters*
+class TimeInterval:    # !!! interval
+    '''        
+    *Attributes (for @property see methods)* :
 
-        - **keys** : list of keys to apply
-        - **inplace** : if True, update self data, else create a new Iindex
+    - **start** : datetime Object - start of `TimeInterval`
+    - **end**   : datetime Object - end of `TimeInterval`
 
-        *Returns* : self or new Iindex'''
-        codec = util.tocodec(self.values, keys)
-        if inplace:
-            self._codec = codec
-            self._keys = keys
-            return self
-        return self.__class__(codec=codec, name=self.name, keys=keys)
+    The methods defined in this class are : 
 
-    def setname(self, name):
-        '''update the Iindex name
+    *dynamic value property (getters)*
 
-        *Parameters*
+    - `TimeInterval.Bounds`
+    - `TimeInterval.bounds`
+    - `TimeInterval.Centroid`
+    - `TimeInterval.duration`
+    - `TimeInterval.instant`
+    - `TimeInterval.stype`
 
-        - **name** : str to set into name
+    *instance methods*
 
-        *Returns* : boolean - True if update'''
-        if isinstance(name, str):
-            self.name = name
-            return True
-        return False
+    - `TimeInterval.json`
+    - `TimeInterval.link`
+    - `TimeInterval.timetuple`
+    - `TimeInterval.union`
+    '''
 
-    def setvalue(self, ind, value, extern=True, typevalue=None, nameonly=False, valueonly=False):
-        '''update a value at the rank ind (and update codec and keys)
+    def __init__(self, val=ES.nullDate):
+        '''
+        TimeInterval constructor.
 
         *Parameters*
 
-        - **ind** : rank of the value
-        - **value** : new value
-        - **extern** : if True, the value has external representation, else internal
-        - **typevalue** : str (default None) - cast to apply to the new value
-        - **nameonly** : if True, only the name of ESValue is changed
-        - **valueonly** : if True, only the value of ESValue is changed
+        - **val** : date, interval (default ES.nullDate) - with several formats 
+        (list, string, datetime, TimeInterval, numpy datetime64, pandas timestamp)
 
         *Returns* : None'''
-        typevalue = util.typename(self.name, typevalue)
-        if extern:
-            value = util.castval(value, typevalue)
-        values = self.values
-        if typevalue in ES.ESclassName and nameonly:
-            values[ind].setName(values.name)
-        elif typevalue in ES.ESclassName and valueonly:
-            values[ind].setValue(values.value)
+        self.start = self.end = ES.nullDate
+        if isinstance(val, str):
+            try:
+                sl = TimeInterval._dattz(datetime.datetime.fromisoformat(val))
+                if sl != None:
+                    self.start = self.end = sl
+                return
+            except:
+                try:
+                    val = json.loads(val)
+                except:
+                    val = ES.nullDate
+        if isinstance(val, list):
+            self._initInterval(val)
+        elif isinstance(val, TimeInterval):
+            self.start, self.end = val.start, val.end
         else:
-            values[ind] = value
-        self._codec, self._keys = util.resetidx(values)
-
-    def setlistvalue(self, listvalue, extern=True, typevalue=None, nameonly=False, valueonly=False):
-        '''update the values (and update codec and keys)
-
-        *Parameters*
+            dat = self._initDat(val)
+            if dat != None:
+                self.start = self.end = dat
+
+    # def __repr__(self):
+    def __str__(self):
+        ''' return the type of interval and the json representation'''
+        return self.stype + '\n' + self.json(encoded=True, encode_format='json')
+
+    def __repr__(self):
+        # if self.stype == 'instant' : return self.__class__.__name__ + f'("{self.start}")'
+        # return self.__class__.__name__ + f'(["{self.start}","{self.end}"])'
+        return self.__class__.__name__ + '(' + self.json(encoded=True, encode_format='json') + ')'
+
+    def __eq__(self, other):
+        '''equal if the 'start' and 'end' dates are equals'''
+        return self.start == other.start and self.end == other.end
+
+    def __lt__(self, other):
+        '''compare the earliest dates (start)'''
+        return self.start < other.start
+
+    def __hash__(self):
+        return hash(self.start) + hash(self.end)
+        # return hash(self.json(True))
+
+    @property
+    def bounds(self):
+        '''return a tuple with the start and end dates with isoformat string'''
+        return (TimeSlot.form(self.start), TimeSlot.form(self.end))
+
+    @property
+    def Centroid(self):
+        '''return a TimeInterval with the date corresponding to the middle of the interval'''
+        return TimeInterval(self.instant)
+
+    @property
+    def duration(self):
+        '''duration between 'end' and 'start' date (timedelta format)'''
+        return self.end - self.start
+
+    @property
+    def instant(self):
+        '''return the date corresponding to the middle of the duration (datetime format)'''
+        return self.start + (self.end - self.start) / 2
+
+    @property
+    def stype(self):
+        '''return a string with the type of TimeInterval (instant, interval)'''
+        if self.start == self.end:
+            return 'instant'
+        return 'interval'
 
-        - **listvalue** : list - list of new values
-        - **typevalue** : str (default None) - class to apply to the new value
-        - **extern** : if True, the value has external representation, else internal
-        - **nameonly** : if True, only the name of ESValue is changed
-        - **valueonly** : if True, only the value of ESValue is changed
-
-        *Returns* : None'''
-        typevalue = util.typename(self.name, typevalue)
-        if extern:
-            listvalue = util.castobj(listvalue, typevalue)
-        values = self.values
-        for i, value_i in enumerate(listvalue):
-            if typevalue in ES.ESclassName and nameonly:
-                values[i].setName(value_i.name)
-            elif typevalue in ES.ESclassName and valueonly:
-                values[i].setValue(value_i.value)
-            else:
-                values[i] = value_i
-        self._codec, self._keys = util.resetidx(values)
-
-    def sort(self, reverse=False, inplace=True, func=str):
-        '''Define sorted index with ordered codec.
-
-        *Parameters*
-
-        - **reverse** : boolean (defaut False) - codec is sorted with reverse order
-        - **inplace** : boolean (default True) - if True, new order is apply to self,
-        if False a new Iindex is created.
-        - **func**    : function (default str) - key used in the sorted function
-
-        *Return*
-
-        - **Iindex** : self if inplace, new Iindex if not inplace'''
-        if inplace:
-            self.reindex(codec=sorted(self._codec, reverse=reverse, key=func))
-            self._keys.sort()
-            return self
-        oldcodec = self._codec
-        codec = sorted(oldcodec, reverse=reverse, key=str)
-        return self.__class__(name=self.name, codec=codec,
-                              keys=sorted(util.reindex(self._keys, oldcodec, codec)))
-
-    def tocoupled(self, other, coupling=True):
+    def json(self, encoded=False, encode_format='json'):
         '''
-        Transform a derived index in a coupled index (keys extension) and add
-        new values to have the same length as other.
+        Return json/bson structure (date if 'instant' or [start, end] if 'interval') 
+        with datetime or datetime.isoformat for dates.
 
         *Parameters*
 
-        - **other** : index to be coupled.
-        - **coupling** : boolean (default True) - reindex if False
+        - **encoded** : defaut False - if True return dict, else return json string/bson bytes
+        - **encode_format**   : defaut 'json' - return json, bson or cbor format
 
-        *Returns* : None'''
-        dic = util.idxlink(other._keys, self._keys)
-        if not dic:
-            raise IindexError("Iindex is not coupled or derived from other")
-        self._codec = [self._codec[dic[i]] for i in range(len(dic))]
-        self._keys = other._keys
-        if not coupling:
-            self.reindex()
+        *Returns* : string or dict'''
+        if self.stype == 'instant':
+            js = self.start
+        else:
+            js = [self.start, self.end]
+        '''if   self.stype == 'instant' : 
+            if encode_format == 'bson':  js = self.start
+            else:           
+                js = TimeSlot.form(self.start)
+        elif self.stype == 'interval' : 
+            if encode_format == 'bson':  js = [self.start, self.end]
+            else:           js = [TimeSlot.form(self.start), TimeSlot.form(self.end)]'''
+        if encoded and encode_format == 'json':
+            return json.dumps(js, cls=TimeSlotEncoder)
+        if encoded and encode_format == 'bson':
+            return bson.encode(js)
+        return js
 
-    def tostdcodec(self, inplace=False, full=True):
+    def link(self, other):
         '''
-        Transform codec in full or in default codec.
+        Return the status (string) of the link between two TimeIntervals (self and other).
+        - equals     : if self and other are the same
+        - disjoint   : if self's interval and other's interval are disjoint
+        - within     : if other's interval is included in self's interval
+        - contains   : if self's interval is included in other's interval
+        - intersects : in the others cases
 
         *Parameters*
 
-        - **inplace** : boolean (default True) - if True, new order is apply to self,
-        - **full** : boolean (default True) - if True reindex with full codec
-
-        *Return*
+        - **other** : TimeInterval to be compared
+
+        *Returns* : string'''
+        if self.start == other.start and self.end == other.end:
+            return 'equals'
+        if self.start <= other.start and self.end >= other.end:
+            return 'contains'
+        if self.start >= other.start and self.end <= other.end:
+            return 'within'
+        if self.start <= other.end and self.end >= other.start:
+            return 'intersects'
+        return 'disjoint'
 
-        - **Iindex** : self if inplace, new Iindex if not inplace'''
-        if full:
-            codec = self.values
-            keys = list(range(len(codec)))
-        else:
-            codec = util.tocodec(self.values)
-            keys = util.reindex(self._keys, self._codec, codec)
-        if inplace:
-            self._codec = codec
-            self._keys = keys
-            return self
-        return self.__class__(codec=codec, name=self.name, keys=keys, castobj=False)
-
-    def valrow(self, row):
-        ''' return json val for a record
+    def timetuple(self, index=0, encoded=False):
+        '''
+        Return json structure (timetuple filter).
 
         *Parameters*
 
-        - **row** : record to obtain val
+        - **index** : integer, defaut 0 - timetuple format to apply :
+            - 0 : year
+            - 1 : month
+            - 2 : day
+            - 3 : hour
+            - 4 : minute
+            - 5 : seconds
+            - 6 : weekday
+            - 7 : yearday
+            - 8 : isdst (1 when daylight savings time is in effect, 0 when is not)
+        - **encoded** : defaut False - if True return string, else return dict
 
-        *Returns* : val[row]'''
-        val = ESValue.uncastsimple(self._codec[self._keys[row]])
-        if isinstance(val, (str, int, float, bool, list, dict, type(None), bytes)):
-            return val
-        return val.json(encoded=False)
+        *Returns* : string or dict'''
+        if index not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
+            return None
+        if self.stype == 'instant':
+            js = self.start.timetuple()[index]
+        elif self.stype == 'interval':
+            js = [self.start.timetuple()[index], self.end.timetuple()[index]]
+        if encoded:
+            return json.dumps(js, cls=TimeSlotEncoder)
+        else:
+            return js
 
-    def valtokey(self, value, extern=True):
-        '''convert a value to a key
+    def union(self, other):
+        ''' Add other's values to self's values in a new TimeInterval 
+        if self and other are not disjoint'''
+        if self.link(other) != 'disjoint':
+            return TimeInterval([min(self.start, other.start), max(self.end, other.end)])
+        else:
+            return None
 
-        *Parameters*
+    def _initInterval(self, val):
+        '''initialization of start and end dates from a list'''
+        self.start = self.end = self._initDat(val[0])
+        if len(val) > 1:
+            self.end = self._initDat(val[1])
+        else:
+            self.start = self.end = self._initDat(val)
+        if self.end < self.start:
+            self.start, self.end = self.end, self.start
+
+    def _initDat(self, val):
+        '''initialization of start and end dates from a unique value 
+        (datetime, string, numpy.datetime64, pandas Timestamp)'''
+        if isinstance(val, datetime.datetime):
+            res = val
+            '''if val.tzinfo is None or val.tzinfo.utcoffset(val) is None:
+                res = val.astimezone(datetime.timezone.utc)
+            else: res = val'''
+        elif isinstance(val, str):
+            try:
+                res = datetime.datetime.fromisoformat(val)
+            except:
+                res = ES.nullDate
+        elif isinstance(val, numpy.datetime64):
+            res = pandas.Timestamp(val).to_pydatetime()
+        elif isinstance(val, pandas._libs.tslibs.timestamps.Timestamp):
+            res = val.to_pydatetime()
+        else:
+            raise TimeSlotError("impossible to convert in a date")
+        return TimeInterval._dattz(res)
 
-        - **value** : value to convert
-        - **extern** : if True, the value has external representation, else internal
+    @staticmethod
+    def _dattz(val):
+        if val.tzinfo is None or val.tzinfo.utcoffset(val) is None:
+            return val.replace(tzinfo=datetime.timezone.utc)
+        return val
 
-        *Returns*
 
-        - **int** : first key finded (None else)'''
-        if extern:
-            value = util.castval(
-                value, util.typename(self.name, ES.def_clsName))
-        if value in self._codec:
-            return self._codec.index(value)
-        return None
+class TimeSlotError(Exception):
+    pass
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `observation-0.0.4/observation/ilist.py` & `observation-0.0.5/observation/ilist.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,56 +1,50 @@
 # -*- coding: utf-8 -*-
 """
 Created on Thu May 26 20:30:00 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.ilist` module contains the `Ilist` class.
+The `python.observation.ilist` module contains the `Ilist` class.
 
 Documentation is available in other pages :
 
 - The Json Standard for Ilist is define
-[here](https://github.com/loco-philippe/Environmental-Sensing/tree/main/
-documentation/IlistJSON-Standard.pdf)
+[here](https://github.com/loco-philippe/Environmental-Sensing/tree/main/documentation/IlistJSON-Standard.pdf)
 - The concept of 'indexed list' is describe in
 [this page](https://github.com/loco-philippe/Environmental-Sensing/wiki/Indexed-list).
 - The non-regression test are at
-[this page](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/
-Tests/test_ilist.py)
-- The [examples](https://github.com/loco-philippe/Environmental-Sensing/tree/main/
-python/Examples/Ilist)
+[this page](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Tests/test_ilist.py)
+- The [examples](https://github.com/loco-philippe/Environmental-Sensing/tree/main/python/Examples/Ilist)
  are :
-    - [creation](https://github.com/loco-philippe/Environmental-Sensing/blob/main/
-      python/Examples/Ilist/Ilist_creation.ipynb)
-    - [variable](https://github.com/loco-philippe/Environmental-Sensing/blob/main/
-      python/Examples/Ilist/Ilist_variable.ipynb)
-    - [update](https://github.com/loco-philippe/Environmental-Sensing/blob/main/
-      python/Examples/Ilist/Ilist_update.ipynb)
-    - [structure](https://github.com/loco-philippe/Environmental-Sensing/blob/main/
-      python/Examples/Ilist/Ilist_structure.ipynb)
-    - [structure-analysis](https://github.com/loco-philippe/Environmental-Sensing/
-      blob/main/python/Examples/Ilist/Ilist_structure-analysis.ipynb)
+    - [creation](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Examples/Ilist/Ilist_creation.ipynb)
+    - [variable](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Examples/Ilist/Ilist_variable.ipynb)
+    - [update](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Examples/Ilist/Ilist_update.ipynb)
+    - [structure](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Examples/Ilist/Ilist_structure.ipynb)
+    - [structure-analysis](https://github.com/loco-philippe/Environmental-Sensing/blob/main/python/Examples/Ilist/Ilist_structure-analysis.ipynb)
 
 ---
 """
 # %% declarations
 from collections import Counter
 from copy import copy
 import math
 import json
 import csv
+import datetime
 import cbor2
+import pandas
 
-from esconstante import ES
-from iindex import Iindex
-from iindex_interface import IindexInterface, CborDecoder
-from util import util
-from ilist_interface import IlistInterface, IlistError
-from ilist_structure import IlistStructure
-from ilist_analysis import Analysis
+from observation.esconstante import ES
+from observation.iindex import Iindex
+from observation.iindex_interface import IindexInterface, CborDecoder
+from observation.util import util
+from observation.ilist_interface import IlistInterface, IlistError
+from observation.ilist_structure import IlistStructure
+from observation.ilist_analysis import Analysis
 
 
 class Ilist(IlistStructure, IlistInterface):
     # %% intro
     '''
     An `Ilist` is a representation of an indexed list.
 
@@ -71,14 +65,15 @@
     - `Ilist.from_file`
     - `Ilist.merge`
 
     *dynamic value - module analysis (getters @property)*
 
     - `Ilist.extidx`
     - `Ilist.extidxext`
+    - `Ilist.groups`
     - `Ilist.idxname`
     - `Ilist.idxlen`
     - `Ilist.iidx`
     - `Ilist.lenidx`
     - `Ilist.lidx`
     - `Ilist.lidxrow`
     - `Ilist.lisvar`
@@ -167,15 +162,15 @@
     - `Ilist.to_xarray`
     - `Ilist.to_dataframe`
     - `Ilist.view`
     - `Ilist.vlist`
     - `Ilist.voxel`
     '''
 
-    def __init__(self, listidx=None, lvarname=None, reindex=True):
+    def __init__(self, listidx=None, reindex=True):
         '''
         Ilist constructor.
 
         *Parameters*
 
         - **listidx** :  list (default None) - list of Iindex data
         - **reindex** : boolean (default True) - if True, default codec for each Iindex'''
@@ -242,15 +237,16 @@
         if idxname is None:
             idxname = [None] * len(val)
         for ind, name in enumerate(idxname):
             if name is None or name == ES.defaultindex:
                 idxname[ind] = 'i'+str(ind)
         lidx = [list(IindexInterface.decodeobj(
             idx, typevalue, context=False)) for idx in val]
-        lindex = [Iindex(idx[2], name, list(range(length)), idx[1], lendefault=length, reindex=reindex)
+        lindex = [Iindex(idx[2], name, list(range(length)), idx[1],
+                         lendefault=length, reindex=reindex)
                   for idx, name in zip(lidx, idxname)]
         return cls(lindex, reindex=False)
 
     @classmethod
     def from_csv(cls, filename='ilist.csv', header=True, nrow=None,
                  optcsv={'quoting': csv.QUOTE_NONNUMERIC}, dtype=ES.def_dtype):
         '''
@@ -330,33 +326,34 @@
         Generate an Ilist Object from a bytes, string or list value
 
         *Parameters*
 
         - **bsd** : bytes, string, DataFrame or list data to convert
         - **reindex** : boolean (default True) - if True, default codec for each Iindex
         - **context** : boolean (default True) - if False, only codec and keys are included'''
+        if isinstance(bsd, cls):
+            return bsd
         if bsd is None:
             bsd = []
         if isinstance(bsd, bytes):
             lis = cbor2.loads(bsd)
         elif isinstance(bsd, str):
             lis = json.loads(bsd, object_hook=CborDecoder().codecbor)
         elif isinstance(bsd, (list, dict)) or bsd.__class__.__name__ == 'DataFrame':
             lis = bsd
         else:
             raise IlistError("the type of parameter is not available")
         return cls._init_obj(lis, reindex=reindex, context=context)
 
-    def merge(self, name=None, fillvalue=math.nan, reindex=False, simplename=False):
+    def merge(self, fillvalue=math.nan, reindex=False, simplename=False):
         '''
         Merge method replaces Ilist objects included into its constituents.
 
         *Parameters*
 
-        - **name** : str (default None) - name of the new Ilist object
         - **fillvalue** : object (default nan) - value used for the additional data
         - **reindex** : boolean (default False) - if True, set default codec after transformation
         - **simplename** : boolean (default False) - if True, new Iindex name are
         the same as merged Iindex name else it is a composed name.
 
         *Returns*: merged Ilist '''
         ilc = copy(self)
@@ -404,17 +401,22 @@
 
         - **listidx** :  list (default None) - list of compatible Iindex data
         - **reindex** : boolean (default True) - if True, default codec for each Iindex
         - **typevalue** : str (default ES.def_clsName) - default value class (None or NamedValue)
         '''
         lindex = []
         if listidx.__class__.__name__ == 'DataFrame':
-            lindex = [Iindex(list(idx.cat.categories), name, list(idx.cat.codes),
-                             lendefault=len(listidx), castobj=False)
-                      for name, idx in listidx.astype('category').items()]
+            lindex = []
+            for name, idx in listidx.astype('category').items():
+                lis = list(idx.cat.categories)
+                if lis and isinstance(lis[0], pandas._libs.tslibs.timestamps.Timestamp):
+                    lis = [ts.to_pydatetime().astimezone(datetime.timezone.utc)
+                           for ts in lis]
+                lindex.append(Iindex(lis, name, list(idx.cat.codes),
+                                     lendefault=len(listidx), castobj=False))
             return cls(lindex, reindex=reindex)
 
         if isinstance(listidx, dict):
             for idxname in listidx:
                 var, idx = Iindex.from_dict_obj({idxname: listidx[idxname]},
                                                 typevalue=typevalue, reindex=reindex)
                 lindex.append(idx)
@@ -431,90 +433,99 @@
                 lidx[ind][0] = 'i'+str(ind)
             if lidx[ind][1] is None:
                 lidx[ind][1] = util.typename(lidx[ind][0], typevalue)
         name, typevaluedec, codec, parent, keys, isfullkeys, isparent, isvar =\
             tuple(zip(*lidx))
 
         leng = [len(cod) for cod in codec]
-        fullmode = not max(isfullkeys) and max(
-            leng) == min(leng)  # mode full : tous False
+        # mode full : tous False et même longueur
+        fullmode = not max(isfullkeys) and max(leng) == min(leng)
         # mode default : tous True (idem all(isfullkeys))
         defmode = min(isfullkeys)
 
         # not max(isparent) : tous isparent = False
-        # if not max(isparent) and ((fullmode and max(leng) == min(leng)) or defmode): # mode full ou mode default
         if not max(isparent) and (fullmode or defmode):  # mode full ou mode default
             lindex = [Iindex(idx[2], idx[0], idx[4], idx[1],
                              reindex=reindex) for idx in lidx]
             return cls(lindex, reindex=reindex)
 
-        crossed = []
-        # crossed : pas d'index (isfullindex false), pas de parent(isparent false)
-        if fullmode:  # au moins un fullkeys ou une longueur différente
-            length = max(leng)
-        else:  # au moins un fullkeys ou une longueur différente
-            if max(isfullkeys):
-                length = len(keys[isfullkeys.index(True)])
-                crossed = [i for i, (isfullk, ispar, lengt) in
-                           enumerate(zip(isfullkeys, isparent, leng))
-                           if not ispar and not isfullk and 1 < lengt < length]
-            else:  # max(leng) != min(leng)
-                # sinon pas de fullindex => matrice et dérivés
-                crossed = [i for i, (isfullk, ispar, lengt) in
-                           enumerate(zip(isfullkeys, isparent, leng))
-                           if not ispar and not isfullk and 1 < lengt]
-                lencrossed = [leng[ind] for ind in crossed]
-                if max(lencrossed) == min(lencrossed):
-                    length = lencrossed[0]
-                    crossed = []
-                else:
-                    length = math.prod([leng[i] for i in crossed])
-                    if length / max(lencrossed) == max(lencrossed):
-                        length = max(lencrossed)
-                        crossed = [i for i, (isfullk, ispar, lengt) in
-                                   enumerate(zip(isfullkeys, isparent, leng))
-                                   if not ispar and not isfullk and 1 < lengt < length]
+        length, crossed = Ilist._init_len_cros(
+            fullmode, leng, isfullkeys, keys, isparent)
         keyscross = util.canonorder([leng[i] for i in crossed])
+        # name: 0, typevaluedec: 1, codec: 2, parent: 3, keys: 4
         for ind in range(len(crossed)):
             lidx[crossed[ind]][4] = keyscross[ind]  # keys
-
         for ind in range(len(lidx)):
             Ilist._init_keys(ind, lidx, length)
-        # name: 0, typevaluedec: 1, codec: 2, parent: 3, keys: 4
         lindex = [Iindex(idx[2], idx[0], idx[4], idx[1],
                          reindex=reindex) for idx in lidx]
         return cls(lindex, reindex=False)
 
     @staticmethod
+    def _init_len_cros(fullmode, leng, isfullkeys, keys, isparent):
+        ''' initialization of length and crossed data'''
+        # crossed : pas d'index (isfullindex false), pas de parent(isparent false)
+        crossed = []
+        if fullmode:  # au moins un fullkeys ou une longueur différente
+            length = max(leng)
+            return length, crossed
+
+        # au moins un fullkeys ou une longueur différente
+        if max(isfullkeys):
+            length = len(keys[isfullkeys.index(True)])
+            crossed = [i for i, (isfullk, ispar, lengt) in
+                       enumerate(zip(isfullkeys, isparent, leng))
+                       if not ispar and not isfullk and 1 < lengt < length]
+            return length, crossed
+
+        # max(leng) != min(leng) pas de fullindex => matrice et dérivés
+        crossed = [i for i, (isfullk, ispar, lengt) in
+                   enumerate(zip(isfullkeys, isparent, leng))
+                   if not ispar and not isfullk and 1 < lengt]
+        lencrossed = [leng[ind] for ind in crossed]
+
+        if max(lencrossed) == min(lencrossed):
+            length = lencrossed[0]
+            crossed = []
+            return length, crossed
+
+        length = math.prod([leng[i] for i in crossed])
+        if length / max(lencrossed) == max(lencrossed):
+            length = max(lencrossed)
+            crossed = [i for i, (isfullk, ispar, lengt) in
+                       enumerate(zip(isfullkeys, isparent, leng))
+                       if not ispar and not isfullk and 1 < lengt < length]
+        return length, crossed
+
+    @staticmethod
     def _init_keys(ind, lidx, leng):
         ''' initialization of keys data'''
+        # name: 0, typevaluedec: 1, codec: 2, parent: 3, keys: 4
         if lidx[ind][4] and (lidx[ind][3] is None or lidx[ind][3] < 0):
             return
         if lidx[ind][4] and len(lidx[ind][4]) == leng:
             return
         if len(lidx[ind][2]) == 1:
             lidx[ind][4] = [0] * leng
             return
         if lidx[ind][3] is None:
             raise IlistError('keys not referenced')
         if lidx[ind][3] < 0:
             lidx[ind][4] = list(range(leng))
             return
         if not lidx[lidx[ind][3]][4] or len(lidx[lidx[ind][3]][4]) != leng:
             Ilist._init_keys(lidx[ind][3], lidx, leng)
-        if not lidx[ind][4]:
-            if len(lidx[ind][2]) == len(lidx[lidx[ind][3]][2]):    # coupled format
-                lidx[ind][4] = lidx[lidx[ind][3]][4]
-                return
-            # derived format without keys
-            lencodp = len(lidx[lidx[ind][3]][2])  # len codec parent
-            lidx[ind][4] = [(i*len(lidx[ind][2])) //
-                            lencodp for i in range(lencodp)]
+        if not lidx[ind][4] and len(lidx[ind][2]) == len(lidx[lidx[ind][3]][2]):
+            # coupled format
+            lidx[ind][4] = lidx[lidx[ind][3]][4]
             return
         # derived keys
+        if not lidx[ind][4]:  # derived format without keys
+            lenp = len(lidx[lidx[ind][3]][2])  # len codec parent
+            lidx[ind][4] = [(i*len(lidx[ind][2])) // lenp for i in range(lenp)]
         lidx[ind][4] = Iindex.keysfromderkeys(
             lidx[lidx[ind][3]][4], lidx[ind][4])
         return
 
     @staticmethod
     def _mergerecord(rec, mergeidx=True, updateidx=True, simplename=False):
         row = rec[0]
@@ -657,14 +668,19 @@
 
     @property
     def extidxext(self):
         '''idx val (see data model)'''
         return [idx.val for idx in self.lidx]
 
     @property
+    def groups(self):
+        ''' list with crossed Iindex groups'''
+        return self.analysis.getgroups()
+
+    @property
     def idxname(self):
         ''' list of idx name'''
         return [idx.name for idx in self.lidx]
 
     @property
     def idxlen(self):
         ''' list of idx codec length'''
```

### Comparing `observation-0.0.4/observation/ilist_analysis.py` & `observation-0.0.5/observation/ilist_analysis.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 # -*- coding: utf-8 -*-
 """
 Created on Sun Oct  2 22:24:59 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.ilist_analysis` module contains the `Analysis` class.
+The `python.observation.ilist_analysis` module contains the `Analysis` class.
 
 """
 
 # %% declarations
 from copy import copy
 import pprint
 from collections import Counter
 
-from util import util
+from observation.util import util
 
 
 class Analysis:
     '''This class analyses relationships included in a tabular object 
     (Pandas DataFrame, Ilist, Observation, list of list).
 
     The Analysis class includes the following functions:
@@ -34,15 +34,16 @@
     - **primary** : list of 'primary' fields row 
     - **secondary** : list of 'secondary' fields row 
     - **lvarname** : list of 'variable' fields name 
 
     The methods defined in this class are :
 
     - `Analysis.actualize`
-    - `Analysis.getinfos`
+    - `Analysis.actualize`
+    - `Analysis.check_relationship`
     - `Analysis.getmatrix`
     - `Analysis.getvarname`
     - `Analysis.getsecondary`
     - `Analysis.getprimary`
     - `Analysis.getpartition`
     - `Analysis.tree`
     '''
@@ -67,24 +68,26 @@
         self.hashi = None
         self.matrix = None
         self.infos = None
         self.primary = None
         self.secondary = None
         self.lvarname = None
         self.partition = []
+        self.groups = []
 
     def actualize(self, partition=None):
         ''' update all data with new values of iobj
 
          *Parameters*
 
         - **partition** : list of int (default None) - partition to be used '''
         self.matrix = self._setmatrix()
         self._setinfos()
         self._setparent()
+        self._setgroups()
         self._setpartition()
         self._setinfospartition(partition)
         infosidx = [idx for idx in self.infos if idx['cat'] != 'variable']
         self.primary = [infosidx.index(idx)
                         for idx in infosidx if idx['cat'] == 'primary']
         self.hashi = self.iobj._hashi()
         self.lvarname = [idx['name']
@@ -94,14 +97,48 @@
         self.lvarname += coupledvar
         self.secondary = [idx['num']
                           for idx in self.infos if idx['cat'] == 'secondary']
         coupledsec = [idx['num'] for idx in self.infos if idx['cat'] == 'coupled'
                       and self.infos[idx['parent']]['cat'] in ('primary', 'secondary')]
         self.secondary += coupledsec
 
+    def check_relationship(self, relations):
+        '''get the list of inconsistent records for each relationship defined in relations
+
+         *Parameters*
+
+        - **relations** : list of dict - list of fields with relationship property
+        
+        *Returns* : dict with for each relationship: key = pair of name, 
+        and value = list of inconsistent records'''
+        if not isinstance(relations, (list, dict)):
+            raise AnalysisError("relations is not correct")
+        if isinstance(relations, dict):
+            relations = [relations]
+        dic_res = {}
+        for field in relations:
+            if not 'relationship' in field or not 'name' in field:
+                continue
+            if not 'parent' in field['relationship'] or not 'link' in field['relationship']:
+                raise AnalysisError("relationship is not correct")
+            rel = field['relationship']['link']
+            f_parent = self.iobj.nindex(field['relationship']['parent'])
+            f_field = self.iobj.nindex(field['name'])
+            name_rel = field['name'] + ' - ' + field['relationship']['parent']
+            if f_parent is None or f_field is None:
+                raise AnalysisError("field's name are  not present in data")
+            match rel:
+                case 'derived':
+                    dic_res[name_rel] = f_parent.coupling(f_field, reindex=True)                
+                case 'coupled':
+                    dic_res[name_rel] = f_parent.coupling(f_field, derived=False, reindex=True)    
+                case _:
+                    raise AnalysisError(rel + "is not a valid relationship")
+        return dic_res          
+    
     def getinfos(self, keys=None):
         '''return attribute infos
 
          *Parameters*
 
         - **keys** : string, list or tuple (default None) - list of attributes to returned
         if 'all' or None, all attributes are returned
@@ -122,20 +159,20 @@
 
         - **name** : list or tuple (default None) - list of two fields names        
         '''
         if self.hashi != self.iobj._hashi():
             self.actualize()
         if not name or not isinstance(name, list):
             return self.matrix
-        if name[0] in self.iobj.indexname:
-            ind0 = self.iobj.indexname.index(name[0])
+        if name[0] in self.iobj.lname:
+            ind0 = self.iobj.lname.index(name[0])
             if len(name) == 1:
                 return self.matrix[ind0]
-            if len(name) > 1 and name[1] in self.iobj.indexname:
-                return self.matrix[ind0][self.iobj.indexname.index(name[1])]
+            if len(name) > 1 and name[1] in self.iobj.lname:
+                return self.matrix[ind0][self.iobj.lname.index(name[1])]
         return None
 
     def getvarname(self):
         '''return variable Iindex name'''
         if self.hashi != self.iobj._hashi():
             self.actualize()
         return self.lvarname
@@ -154,14 +191,20 @@
 
     def getpartition(self):
         '''return attribute partition'''
         if self.hashi != self.iobj._hashi():
             self.actualize()
         return self.partition
 
+    def getgroups(self):
+        '''return attribute groups'''
+        if self.hashi != self.iobj._hashi():
+            self.actualize()
+        return self.groups
+
     def tree(self, mode='derived', width=5, lname=20, string=True):
         '''return a string with a tree of derived Iindex.
 
          *Parameters*
 
         - **lname** : integer (default 20) - length of the names        
         - **width** : integer (default 5) - length of the lines        
@@ -280,16 +323,16 @@
         for i in range(lenindex):
             if infosp[i]['cat'] == 'coupled':
                 infosp[i]['pparent'] = infosp[infosp[i]['parent']]['pparent']
 
     def _setparent(self):
         '''set parent (Iindex with minimal diff) for each Iindex'''
         # parent : min(diff) -> child
-        # distparent : min(distrate) -> diffdistparent, linkrate
-        # minparent : min(distance) -> rate, distance
+        # distparent : min(distrate) -> diffdistparent, linkrate(rateA)
+        # minparent : min(distance) -> rate(rateB), distance
         lenindex = self.iobj.lenindex
         leniobj = len(self.iobj)
         for i in range(lenindex):
             mindiff = leniobj
             distratemin = 1
             distancemin = leniobj * leniobj
             distparent = None
@@ -358,14 +401,34 @@
             lis = [name.replace(' ', '*').replace("'", '*')]
         if child[n+1]:
             for ch in child[n+1]:
                 if ch != n:
                     lis.append(self._dic_noeud(ch, child, lname, mode))
         return {str(n).ljust(2, '*'): lis}
 
+    def _setgroups(self):
+        '''set groups (list of crossed Iindex groups)'''
+        self.groups = []
+        crossed = {info['num'] for info in self.infos if info['crossed']}
+        remove = set()
+        for num in crossed:
+            for num2 in crossed:
+                if num != num2 and self.infos[num]['parent'] in crossed:
+                    remove.add(num)
+        crossed -= remove     
+        setcrossed = set()
+        for num in crossed:
+            info = self.infos[num]
+            if not info['name'] in setcrossed:
+                setname = {self.infos[cros]['name'] for cros in info['crossed']
+                           if cros in crossed} | {info['name']}
+                self.groups.append(setname)
+                setcrossed |= setname
+        return None
+
     def _setpartition(self):
         '''set partition (list of Iindex partitions)'''
         brother = {idx['num']: idx['crossed']
                    for idx in self.infos if idx['crossed']}
         self.partition = []
         chemin = []
         for cros in brother:
```

### Comparing `observation-0.0.4/observation/ilist_interface.py` & `observation-0.0.5/observation/ilist_interface.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,32 +1,32 @@
 # -*- coding: utf-8 -*-
 """
 Created on Sun Oct  2 22:24:59 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.ilist_interface` module contains the `IlistInterface` class
-(`observation.ilist.Ilist` methods).
+The `python.observation.ilist_interface` module contains the `IlistInterface` class
+(`python.observation.ilist.Ilist` methods).
 """
 
 # %% declarations
 import datetime
 import json
 import csv
 import math
 import xarray
 import numpy as np
 import matplotlib.pyplot as plt
 from tabulate import tabulate
 import cbor2
 
-from esconstante import ES
-from iindex import Iindex
-from iindex_interface import IindexEncoder
-from util import util
+from observation.esconstante import ES
+from observation.iindex import Iindex
+from observation.iindex_interface import IindexEncoder
+from observation.util import util
 
 #import sys
 #print("In module ilist_interface sys.path[0], __package__ ==", sys.path[0], __package__)
 #print("In module ilist_interface __package__, __name__ ==", __package__, __name__)
 
 
 class IlistError(Exception):
@@ -209,29 +209,41 @@
         - **modecodec** : string (default 'optimize') - if 'full', each index is with a full codec
         if 'default' each index has keys, if 'optimize' keys are optimized, 
         if 'dict' dict format is used, if 'nokeys' keys are absent
         - **name** : boolean (default False) - if False, default index name are not included
         - **fullvar** : boolean (default True) - if True and modecodec='optimize, 
         variable index is with a full codec
         - **geojson** : boolean (default False) - geojson for LocationValue if True
+        - **id** : integer (default None) - Observation.id if Ilist is attached to an Observation
 
         *Returns* : string, bytes or dict'''
         option = {'modecodec': 'optimize', 'encoded': False,
                   'encode_format': 'json', 'codif': ES.codeb, 'name': False,
-                  'geojson': False, 'fullvar': True} | kwargs
+                  'geojson': False, 'fullvar': True, 'id': None} | kwargs
         option2 = {'encoded': False, 'encode_format': 'json',
                    'codif': option['codif'], 'geojson': option['geojson'],
                    'modecodec': option['modecodec'], 'fullvar': option['fullvar']}
         if option['modecodec'] == 'dict':
             lis = {}
             for idx in self.lindex:
                 name, dicval = list(idx.to_dict_obj(**option2).items())[0]
                 if name in self.lvarname:
                     dicval['var'] = True
                 lis[name] = dicval
+        elif option['modecodec'] == 'ndjson':
+            if not option['id']:
+                raise IlistError("an  id is necessary for 'ndjson'")                
+            lis = []
+            for rec in self:
+                lis.append({ES.id: option[ES.id]} | 
+                           {name: util.json(val, encoded=False, typevalue=None,
+                                           simpleval=False, modecodec='ndjson',
+                                           untyped=False, datetime=False,
+                                           geojson=False) 
+                            for name, val in zip(self.lname, rec)})              
         else:
             indexname = [option['name'] or name != 'i' + str(i)
                          for i, name in enumerate(self.lname)]
             if option['modecodec'] != 'optimize':
                 lis = [idx.to_obj(name=iname, **option2)
                        for idx, iname in zip(self.lindex, indexname)]
             else:
@@ -439,15 +451,15 @@
                     lis.append(idx.to_obj(keys=True, name=iname, **option2))
             else:  # derived
                 if len(self.lindex[inf['parent']].codec) == len(self):
                     lis.append(idx.to_obj(keys=True, name=iname, **option2))
                 elif idx.iskeysfromderkeys(self.lindex[inf['parent']]):
                     lis.append(idx.to_obj(parent=inf['parent'],
                                           name=iname, **option2))
-                else:
+                else: # periodic derived
                     keys = idx.derkeys(self.lindex[inf['parent']])
                     lis.append(idx.to_obj(keys=keys, parent=inf['parent'],
                                           name=iname, **option2))
         return lis
 
     def _to_tab(self, **kwargs):
         ''' data preparation (dict of dict) for view or csv export.
```

### Comparing `observation-0.0.4/observation/ilist_structure.py` & `observation-0.0.5/observation/ilist_structure.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 # -*- coding: utf-8 -*-
 """
 Created on Sun Oct  2 22:24:59 2022
 
 @author: philippe@loco-labs.io
 
-The `observation.ilist_structure` module contains the `IlistStructure` class
-(`observation.ilist.Ilist` methods).
+The `python.observation.ilist_structure` module contains the `IlistStructure` class
+(`python.observation.ilist.Ilist` methods).
 """
 
 # %% declarations
 from copy import copy
 
-from esconstante import ES
-from iindex import Iindex
-from util import util
-from ilist_interface import IlistError
+from observation.esconstante import ES
+from observation.iindex import Iindex
+from observation.util import util
+from observation.ilist_interface import IlistError
 
 
 class IlistStructure:
     '''this class includes Ilist methods :
 
     *selecting - infos methods*
 
@@ -249,25 +249,34 @@
         if None in reckeys:
             return None
         row = self.tiindex.index(reckeys)
         for idx in self:
             del idx[row]
         return row
 
-    def delindex(self, indexname):
+    def delindex(self, delname=None, savename=None):
         '''remove an Iindex or a list of Iindex.
 
         *Parameters*
 
-        - **indexname** : string or list of string - name of index to remove
+        - **delname** : string or list of string - name of index to remove
+        - **savename** : string or list of string - name of index to keep
 
         *Returns* : none '''
-        if isinstance(indexname, str):
-            indexname = [indexname]
-        for idxname in indexname:
+        if not delname and not savename :
+            return
+        if isinstance(delname, str):
+            delname = [delname]
+        if isinstance(savename, str):
+            savename = [savename]
+        if delname and savename:
+            delname = [name for name in delname if not name in savename]
+        if not delname:
+            delname = [name for name in self.lname if not name in savename]
+        for idxname in delname:
             if idxname in self.lname:
                 self.lindex.pop(self.lname.index(idxname))
 
     def _fullindex(self, ind, keysadd, indexname, varname, leng, fillvalue, fillextern):
         if not varname:
             varname = []
         idx = self.lindex[ind]
@@ -337,15 +346,17 @@
         '''check duplicate cod in a list of indexes. Result is add in a new 
         index or returned.
 
         *Parameters*
 
         - **indexname** : list of string (default none) - name of indexes to check 
         (if None, all Iindex)
-        - **resindex** : string (default None) - Add a new index with check result
+        - **resindex** : string (default None) - Add a new index named resindex 
+        with check result (False if duplicate)
+        - **indexview** : list of str (default None) - list of fields to return
 
         *Returns* : list of int - list of rows with duplicate cod '''
         if not indexname:
             indexname = self.lname
         duplicates = []
         for name in indexname:
             duplicates += self.nindex(name).getduplicates()
```

### Comparing `observation-0.0.4/observation/util.py` & `observation-0.0.5/observation/util.py`

 * *Files 2% similar despite different names*

```diff
@@ -8,17 +8,17 @@
 from collections import Counter
 from itertools import product
 import datetime
 import re
 import numpy as np
 import math
 
-from timeslot import TimeInterval
-from esconstante import ES, _classval
-from esvalue_base import ESValue
+from observation.timeslot import TimeInterval
+from observation.esconstante import ES, _classval
+from observation.esvalue_base import ESValue
 
 
 def identity(*args, **kwargs):
     '''return the same value as args or kwargs'''
     if len(args) > 0:
         return args[0]
     if len(kwargs) > 0:
@@ -250,16 +250,19 @@
         #lis = set(util.tuple(util.transpose([ref, l2])))
         # if not len(lis) == len(set(ref)):
         #    return {}
         # return dict(lis)
 
     @staticmethod
     def json(val, **option):
-        val = ESValue.uncastsimple(val)
-        if isinstance(val, (str, int, float, bool, list, dict, type(None), bytes)):
+        datecast = True
+        if 'datetime' in option:
+            datecast = option['datetime']
+        val = ESValue.uncastsimple(val, datecast)
+        if isinstance(val, (str, int, float, bool, list, dict, type(None), bytes, datetime.datetime)):
             return val
         if option['simpleval']:
             return val.json(**option)
         if val.__class__.__name__ in ES.ESclassName:  # ESValue
             if not option['typevalue']:
                 return val.json(**option)
             else:
```

### Comparing `observation-0.0.4/observation.egg-info/PKG-INFO` & `observation-0.0.5/observation.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: observation
-Version: 0.0.4
-Summary: environmental data interoperability in Python
+Version: 0.0.5
+Summary: environmental data interoperability
 Home-page: https://github.com/loco-philippe/Environmental-Sensing
 Author: Philippe Thomy
 Author-email: philippe@loco-labs.io
-Keywords: observation,indexed list,development,environmental data
+Keywords: observation,tabular data,development,environmental data
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7, <4
 Description-Content-Type: text/markdown
@@ -17,15 +17,15 @@
 
 # Python package
 The Python package includes 
 - all the connectors associated with the standard ObsJson format,
 - classes Observation, Ilist, Iindex, ESValue, TimeSlot
 ## Python connectors
 The Python connectors are defined :
-- in the [documentation](https://loco-philippe.github.io/observation.html)
+- in the [documentation](https://loco-philippe.github.io/python/observation.html)
 - in the [code](./observation/README.md)  files 
 - in the [examples](./Examples/README.md)
 - in the [validation dataset](./Validation/README.md)
 
 ## Installation
 Observation itself is a pure Python package. It can be installed with pip
```

### Comparing `observation-0.0.4/setup.py` & `observation-0.0.5/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -9,25 +9,26 @@
 from setuptools import setup, find_packages
 
 here = pathlib.Path(__file__).parent.resolve()
 long_description = (here / "README.md").read_text(encoding="utf-8")
 
 setup(
     name="observation",
-    version="0.0.4",
-    description="environmental data interoperability in Python",
+    version="0.0.5",
+    description="environmental data interoperability",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/loco-philippe/Environmental-Sensing",
     author="Philippe Thomy",
     author_email="philippe@loco-labs.io",
     classifiers=[
         "Development Status :: 3 - Alpha",
         "Intended Audience :: Developers",
         "Topic :: Software Development :: Build Tools",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3"],
-    keywords="observation, indexed list, development, environmental data",
+    keywords="observation, tabular data, development, environmental data",
     packages=find_packages(include=['observation', 'observation.*']),
     python_requires=">=3.7, <4",
-    install_requires=['numpy', 'shapely', 'cbor2', 'xarray', 'pandas']
+    install_requires=['numpy', 'shapely', 'cbor2', 'xarray', 'pandas', 'folium',
+                      'bson', 'xarray']
 )
```

