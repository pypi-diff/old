# Comparing `tmp/antelope_interface-0.1.8.tar.gz` & `tmp/antelope_interface-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "antelope_interface-0.1.8.tar", last modified: Fri Apr  8 19:13:36 2022, max compression
+gzip compressed data, was "antelope_interface-0.2.0.tar", last modified: Fri Apr  7 05:30:14 2023, max compression
```

## Comparing `antelope_interface-0.1.8.tar` & `antelope_interface-0.2.0.tar`

### file list

```diff
@@ -1,36 +1,42 @@
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.121758 antelope_interface-0.1.8/
--rw-r--r--   0 b          (500) b          (506)     1520 2020-05-28 23:57:28.000000 antelope_interface-0.1.8/LICENSE
--rw-r--r--   0 b          (500) b          (506)     1787 2022-04-08 19:13:36.121758 antelope_interface-0.1.8/PKG-INFO
--rw-r--r--   0 b          (500) b          (506)     1013 2020-12-30 20:52:39.000000 antelope_interface-0.1.8/README.md
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.115091 antelope_interface-0.1.8/antelope/
--rw-r--r--   0 b          (500) b          (506)     6366 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/__init__.py
--rw-r--r--   0 b          (500) b          (506)     6484 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/exchanges_from_spreadsheet.py
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.115091 antelope_interface-0.1.8/antelope/flows/
--rw-r--r--   0 b          (500) b          (506)       77 2020-09-30 08:29:11.000000 antelope_interface-0.1.8/antelope/flows/__init__.py
--rw-r--r--   0 b          (500) b          (506)     4052 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/flows/flow.py
--rw-r--r--   0 b          (500) b          (506)     2698 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/flows/flow_interface.py
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.118425 antelope_interface-0.1.8/antelope/interfaces/
--rw-r--r--   0 b          (500) b          (506)      111 2020-09-25 19:28:16.000000 antelope_interface-0.1.8/antelope/interfaces/__init__.py
--rw-r--r--   0 b          (500) b          (506)     3645 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/interfaces/abstract_query.py
--rw-r--r--   0 b          (500) b          (506)     9673 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/interfaces/ibackground.py
--rw-r--r--   0 b          (500) b          (506)     4333 2020-09-24 22:08:18.000000 antelope_interface-0.1.8/antelope/interfaces/iconfigure.py
--rw-r--r--   0 b          (500) b          (506)     5641 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/interfaces/iexchange.py
--rw-r--r--   0 b          (500) b          (506)     2449 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/interfaces/iforeground.py
--rw-r--r--   0 b          (500) b          (506)     7077 2021-10-30 03:46:20.000000 antelope_interface-0.1.8/antelope/interfaces/iindex.py
--rw-r--r--   0 b          (500) b          (506)    10335 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/interfaces/iquantity.py
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.118425 antelope_interface-0.1.8/antelope/refs/
--rw-r--r--   0 b          (500) b          (506)       74 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/__init__.py
--rw-r--r--   0 b          (500) b          (506)    11625 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/base.py
--rw-r--r--   0 b          (500) b          (506)     4326 2022-01-22 08:03:17.000000 antelope_interface-0.1.8/antelope/refs/catalog_ref.py
--rw-r--r--   0 b          (500) b          (506)     5295 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/exchange_ref.py
--rw-r--r--   0 b          (500) b          (506)     4137 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/flow_ref.py
--rw-r--r--   0 b          (500) b          (506)    10433 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/process_ref.py
--rw-r--r--   0 b          (500) b          (506)     5696 2022-04-08 18:42:59.000000 antelope_interface-0.1.8/antelope/refs/quantity_ref.py
-drwxr-xr-x   0 b          (500) b          (506)        0 2022-04-08 19:13:36.121758 antelope_interface-0.1.8/antelope_interface.egg-info/
--rw-r--r--   0 b          (500) b          (506)     1787 2022-04-08 19:13:35.000000 antelope_interface-0.1.8/antelope_interface.egg-info/PKG-INFO
--rw-r--r--   0 b          (500) b          (506)      840 2022-04-08 19:13:35.000000 antelope_interface-0.1.8/antelope_interface.egg-info/SOURCES.txt
--rw-r--r--   0 b          (500) b          (506)        1 2022-04-08 19:13:35.000000 antelope_interface-0.1.8/antelope_interface.egg-info/dependency_links.txt
--rw-r--r--   0 b          (500) b          (506)       20 2022-04-08 19:13:35.000000 antelope_interface-0.1.8/antelope_interface.egg-info/requires.txt
--rw-r--r--   0 b          (500) b          (506)        9 2022-04-08 19:13:35.000000 antelope_interface-0.1.8/antelope_interface.egg-info/top_level.txt
--rw-r--r--   0 b          (500) b          (506)       38 2022-04-08 19:13:36.121758 antelope_interface-0.1.8/setup.cfg
--rw-r--r--   0 b          (500) b          (506)     2232 2022-04-08 19:13:12.000000 antelope_interface-0.1.8/setup.py
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/
+-rw-r--r--   0 b          (500) b          (506)     1520 2020-05-28 23:57:28.000000 antelope_interface-0.2.0/LICENSE
+-rw-r--r--   0 b          (500) b          (506)       44 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/MANIFEST.in
+-rw-r--r--   0 b          (500) b          (506)     1617 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/PKG-INFO
+-rw-r--r--   0 b          (500) b          (506)     1013 2020-12-30 20:52:39.000000 antelope_interface-0.2.0/README.md
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.606182 antelope_interface-0.2.0/antelope/
+-rw-r--r--   0 b          (500) b          (506)     7381 2023-02-06 20:32:15.000000 antelope_interface-0.2.0/antelope/__init__.py
+-rw-r--r--   0 b          (500) b          (506)     7128 2022-06-11 08:41:11.000000 antelope_interface-0.2.0/antelope/exchanges_from_spreadsheet.py
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.606182 antelope_interface-0.2.0/antelope/flows/
+-rw-r--r--   0 b          (500) b          (506)       89 2022-12-31 00:07:14.000000 antelope_interface-0.2.0/antelope/flows/__init__.py
+-rw-r--r--   0 b          (500) b          (506)     8689 2023-03-29 01:31:42.000000 antelope_interface-0.2.0/antelope/flows/flow.py
+-rw-r--r--   0 b          (500) b          (506)     3751 2022-12-31 00:07:14.000000 antelope_interface-0.2.0/antelope/flows/flow_interface.py
+-rw-r--r--   0 b          (500) b          (506)    13903 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/flows/openlca_locales.json
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.606182 antelope_interface-0.2.0/antelope/interfaces/
+-rw-r--r--   0 b          (500) b          (506)      111 2020-09-25 19:28:16.000000 antelope_interface-0.2.0/antelope/interfaces/__init__.py
+-rw-r--r--   0 b          (500) b          (506)     3307 2023-03-30 22:44:53.000000 antelope_interface-0.2.0/antelope/interfaces/abstract_query.py
+-rw-r--r--   0 b          (500) b          (506)    10849 2023-04-05 15:49:48.000000 antelope_interface-0.2.0/antelope/interfaces/ibackground.py
+-rw-r--r--   0 b          (500) b          (506)     4333 2020-09-24 22:08:18.000000 antelope_interface-0.2.0/antelope/interfaces/iconfigure.py
+-rw-r--r--   0 b          (500) b          (506)     5947 2022-12-31 00:07:14.000000 antelope_interface-0.2.0/antelope/interfaces/iexchange.py
+-rw-r--r--   0 b          (500) b          (506)     6797 2022-12-31 00:07:14.000000 antelope_interface-0.2.0/antelope/interfaces/iforeground.py
+-rw-r--r--   0 b          (500) b          (506)     7077 2021-10-30 03:46:20.000000 antelope_interface-0.2.0/antelope/interfaces/iindex.py
+-rw-r--r--   0 b          (500) b          (506)    15250 2023-01-12 06:14:41.000000 antelope_interface-0.2.0/antelope/interfaces/iquantity.py
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/antelope/refs/
+-rw-r--r--   0 b          (500) b          (506)       81 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/refs/__init__.py
+-rw-r--r--   0 b          (500) b          (506)    13561 2023-01-07 00:12:58.000000 antelope_interface-0.2.0/antelope/refs/base.py
+-rw-r--r--   0 b          (500) b          (506)     4326 2022-01-22 08:03:17.000000 antelope_interface-0.2.0/antelope/refs/catalog_ref.py
+-rw-r--r--   0 b          (500) b          (506)     8254 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/refs/exchange_ref.py
+-rw-r--r--   0 b          (500) b          (506)     4753 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/refs/flow_ref.py
+-rw-r--r--   0 b          (500) b          (506)    11560 2023-04-05 08:50:18.000000 antelope_interface-0.2.0/antelope/refs/process_ref.py
+-rw-r--r--   0 b          (500) b          (506)     8662 2023-02-06 20:32:15.000000 antelope_interface-0.2.0/antelope/refs/quantity_ref.py
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/antelope/refs/tests/
+-rw-r--r--   0 b          (500) b          (506)        0 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/refs/tests/__init__.py
+-rw-r--r--   0 b          (500) b          (506)     1150 2022-04-09 17:53:58.000000 antelope_interface-0.2.0/antelope/refs/tests/test_flows.py
+-rw-r--r--   0 b          (500) b          (506)     4605 2023-01-11 06:29:16.000000 antelope_interface-0.2.0/antelope/xdb_tokens.py
+drwxr-xr-x   0 b          (500) b          (506)        0 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/antelope_interface.egg-info/
+-rw-r--r--   0 b          (500) b          (506)     1617 2023-04-07 05:30:14.000000 antelope_interface-0.2.0/antelope_interface.egg-info/PKG-INFO
+-rw-r--r--   0 b          (500) b          (506)      977 2023-04-07 05:30:14.000000 antelope_interface-0.2.0/antelope_interface.egg-info/SOURCES.txt
+-rw-r--r--   0 b          (500) b          (506)        1 2023-04-07 05:30:14.000000 antelope_interface-0.2.0/antelope_interface.egg-info/dependency_links.txt
+-rw-r--r--   0 b          (500) b          (506)       36 2023-04-07 05:30:14.000000 antelope_interface-0.2.0/antelope_interface.egg-info/requires.txt
+-rw-r--r--   0 b          (500) b          (506)        9 2023-04-07 05:30:14.000000 antelope_interface-0.2.0/antelope_interface.egg-info/top_level.txt
+-rw-r--r--   0 b          (500) b          (506)       38 2023-04-07 05:30:14.609516 antelope_interface-0.2.0/setup.cfg
+-rw-r--r--   0 b          (500) b          (506)     2437 2023-04-06 23:21:36.000000 antelope_interface-0.2.0/setup.py
```

### Comparing `antelope_interface-0.1.8/LICENSE` & `antelope_interface-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `antelope_interface-0.1.8/PKG-INFO` & `antelope_interface-0.2.0/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,37 +1,36 @@
 Metadata-Version: 2.1
 Name: antelope_interface
-Version: 0.1.8
-Summary: UNKNOWN
+Version: 0.2.0
 Home-page: https://github.com/AntelopeLCA/antelope
 Author: Brandon Kuczenski
 Author-email: bkuczenski@ucsb.edu
 License: BSD 3-Clause
-Description: # antelope
-        Standard Interface and reference framework for LCA
-        
-        The `antelope` package is an interface specification for accessing LCA data resources, as described in [JIE submitted].  It should be subclassed by implementations that wish to expose data using this uniform interface.  A reference implementation, including a stand-alone LCA computing tool, exists...
-        
-        ## Documentation
-        
-        See the following articles:
-        
-         * [Antelope Design Principles](principles.md) for documentation of this repository.
-         * [Entity Specification](entities.md) and nomenclature.
-         * [Return Types](types.md) which are *references* to entities.
-        
-        ### See Also
-        
-         * [antelope_core](https://github.com/AntelopeLCA/core) The reference implementation including local data source management.
-         * [antelope_background](https://github.com/AntelopeLCA/background) Used for partial ordering of databases and construction and inversion of matrices
-         * [antelope_foreground](https://github.com/AntelopeLCA/foreground) Used for building foreground models
-        
-Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Natural Language :: English
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Topic :: Scientific/Engineering
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# antelope
+Standard Interface and reference framework for LCA
+
+The `antelope` package is an interface specification for accessing LCA data resources, as described in [JIE submitted].  It should be subclassed by implementations that wish to expose data using this uniform interface.  A reference implementation, including a stand-alone LCA computing tool, exists...
+
+## Documentation
+
+See the following articles:
+
+ * [Antelope Design Principles](principles.md) for documentation of this repository.
+ * [Entity Specification](entities.md) and nomenclature.
+ * [Return Types](types.md) which are *references* to entities.
+
+### See Also
+
+ * [antelope_core](https://github.com/AntelopeLCA/core) The reference implementation including local data source management.
+ * [antelope_background](https://github.com/AntelopeLCA/background) Used for partial ordering of databases and construction and inversion of matrices
+ * [antelope_foreground](https://github.com/AntelopeLCA/foreground) Used for building foreground models
```

### Comparing `antelope_interface-0.1.8/README.md` & `antelope_interface-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `antelope_interface-0.1.8/antelope/__init__.py` & `antelope_interface-0.2.0/antelope/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -10,38 +10,59 @@
 from .interfaces.iconfigure import ConfigureInterface
 from .interfaces.iexchange import ExchangeInterface, ExchangeRequired
 from .interfaces.iindex import IndexInterface, IndexRequired, directions, comp_dir, num_dir, check_direction, valid_sense, comp_sense
 from .interfaces.ibackground import BackgroundInterface, BackgroundRequired
 from .interfaces.iquantity import QuantityInterface, QuantityRequired, NoFactorsFound, ConversionReferenceMismatch, FlowableMismatch
 from .interfaces.iforeground import ForegroundInterface
 
-from .flows import BaseEntity, FlowInterface, Flow
+from .flows import BaseEntity, NullEntity, FlowInterface, Flow
 
 from .refs.process_ref import MultipleReferences, NoReference
 from .refs.catalog_ref import CatalogRef, QuantityRef, UnknownOrigin
-from .refs.quantity_ref import convert, NoUnitConversionTable
-from .refs.base import NoCatalog, EntityRefMergeError, InvalidQuery
-from .refs.exchange_ref import ExchangeRef, RxRef
+from .refs.quantity_ref import convert, NoUnitConversionTable, RefQuantityRequired
+
+from .refs.base import NoCatalog, EntityRefMergeError, InvalidQuery, PropertyExists
+from .refs.exchange_ref import ExchangeRef, RxRef, EXCHANGE_TYPES
+
 
 import re
 
 from os.path import splitext
 
 from collections import namedtuple
 
 
-class PropertyExists(Exception):
+class ValuesAccessRequired(Exception):
+    """
+    The requested route requires a grant that has values=True
+    """
+    pass
+
+
+class UpdateAccessRequired(Exception):
+    """
+    The requested route requires a grant that has updates=True
+    """
     pass
 
 
 '''
 Query classes
 '''
 
+
 class BasicQuery(IndexInterface, ExchangeInterface, QuantityInterface):
+    """
+    A basic query depends on an archive-- which is not yet well-defined, but which has the following API:
+    archive.make_interface(interface): returns an implementation of the designated interface
+    archive.ref: returns the archive's semantic reference
+    archive.source: returns the physical source for the archive's content
+
+    Note that an alternative abstract query implementation could be imagined
+    """
     def __init__(self, archive, debug=False):
         self._archive = archive
         self._dbg = debug
 
     def _perform_query(self, itype, attrname, exc, *args, strict=False, **kwargs):
         if itype is None:
             itype = 'basic'
@@ -64,14 +85,22 @@
         if entity is None:
             return None
         if entity.is_entity:
             return entity.make_ref(self)
         else:
             return entity  # already a ref
 
+    def __str__(self):
+        return '%s(%s:%s:%s)' % (self.__class__.__name__, self.origin,
+                                 self._archive.__class__.__name__,
+                                 self._archive.source)
+
+    def __repr__(self):
+        return self.__str__()
+
     '''
     I think that's all I need to do!
     '''
 
 
 class LcQuery(BasicQuery, BackgroundInterface, ConfigureInterface):
     pass
@@ -159,17 +188,17 @@
 still technically debugging the CalRecycle project. So we introduce this flag CONTEXT_STATUS_ to express to client code 
 which one to do. It should take either of the two values: 'compat' means "old style" (flows have Compartments) and 
 'new' means use the new data model (exchange terminations are contexts) 
 """
 CONTEXT_STATUS_ = 'new'  # 'compat': context = flow['Compartment']; 'new': context = exch.termination
 
 
-# Containers of information about linked exchanges.  Direction is given with respect to the termination.
+# Exterior exchanges- with contexts outside the db.  Direction is given with respect to the Interior (e.g. "Output" "to air")
+# LciaResults should negate values when an exchange direction and a context are not complementary (i.e. "Input" "to air")
 ExteriorFlow = namedtuple('ExteriorFlow', ('origin', 'flow', 'direction', 'termination'))
-# ProductFlow = namedtuple('ProductFlow', ('origin', 'flow', 'direction', 'termination', 'component_id'))
 
 EntitySpec = namedtuple('EntitySpec', ('link', 'ref', 'name', 'group'))
 
 # packages that contain 'providers'
 antelope_herd = [
     'antelope_background',
     'antelope_foreground'
```

### Comparing `antelope_interface-0.1.8/antelope/exchanges_from_spreadsheet.py` & `antelope_interface-0.2.0/antelope/exchanges_from_spreadsheet.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,18 @@
 """
 This module provides a routine that generates a list of exchange refs from a properly formatted spreadsheet
 """
 from .refs import CatalogRef, ExchangeRef
 from .interfaces import check_direction
 
 
+class ValueIsBalance(Exception):
+    pass
+
+
 class TermDictDeprecated(Exception):
     """
     Exchanges are allowed to specify terminations, including context, compartment, defaultprovider, activitylinkid,
     or target. However, the exchanges-from-spreadsheet code is not allowed to apply any interpretation or mapping
     between the specified terminations and the targets in the foreground.  Instead, that mapping should be applied
     when the exchanges are used to create fragments.  The main reason for this is that the signature of the
     exchange interface does not support term_flow, descend, or other fragment-specific aspects.
@@ -19,15 +23,15 @@
 def _row_dict(sheetlike, row):
     """
     Creates a dictionary from the named row of the 'sheetlike' input.
     :param sheetlike: has row() method returns a list of strings
     :param row: int
     :return: dict k: v where k are entry.value.lower() for entry in row(0) and v are entry.value for entry in row(row)
     """
-    headers = [k.value.lower() for k in sheetlike.row(0)]
+    headers = [str(k.value).lower() for k in sheetlike.row(0)]
     return {headers[i]: k.value for i, k in enumerate(sheetlike.row(row)) if i < len(headers)}
 
 
 def _popanykey(dct, *keys, strict=False):
     """
     Returns the first of the listed keys to be found in the dict
     :param dct: a dict
@@ -50,23 +54,31 @@
     :param rowdict:
     :return:
     """
     rowdict.pop('process', None)
     flow_ref = _popanykey(rowdict, 'flow', 'flowref', 'flow_ref', 'external_ref', strict=True)
     flow = CatalogRef(origin, flow_ref, entity_type='flow')
     dirn = check_direction(_popanykey(rowdict, 'direction', 'flowdir', strict=True))
-    try:
-        value = float(_popanykey(rowdict, 'value', 'amount', strict=True))
-    except (ValueError, TypeError):
-        value = 0.0
+    val = _popanykey(rowdict, 'value', 'amount', strict=True)
+    if str(val).lower() == 'balance':
+        value = ValueIsBalance
+    else:
+        try:
+            value = float(val)
+        except (ValueError, TypeError):
+            value = 0.0
     unit = _popanykey(rowdict, 'unit', 'units')
-    term = _popanykey(rowdict, 'context', 'compartment', 'defaultprovider', 'activitylinkid', 'target')
+    term = _popanykey(rowdict, 'context', 'compartment', 'target',
+                      'defaultprovider', 'activitylinkid', 'term', 'termination')
     if term == '':
         term = None
-    print('%s %s %g %s [%s]' % (flow, dirn, value, unit, term))
+    if value is ValueIsBalance:
+        print('%s %s (balance) %s [%s]' % (flow, dirn, unit, term))
+    else:
+        print('%s %s %g %s [%s]' % (flow, dirn, value, unit, term))
     return flow, dirn, value, unit, term
 
 
 def exchanges_from_spreadsheet(sheetlike, term_dict=None, node=None, origin=None):
     """
     A routine to create a list of flat exchanges (all having the same parent node) from an excel table.
 
@@ -89,25 +101,30 @@
         0=empty, 1=text, 2=number, 3=date, 4=boolean, 5=error, 6=blank
         (not clear what the difference is between empty and blank)
 
     Columns are interpreted as follows (case-insensitive):
     Required:
     'flow', 'flowref', 'flow_ref', 'external_ref' - in that order, used to specify flow
     'direction', 'flowdir' - in that order, used to specify direction w.r.t. parent node
-    'value', 'amount' - in that order
+    'value', 'amount' - in that order.
     This method returns unresolved catalog refs- in order for client code to use them, the flow refs must resolve (bc
     reference quantity must be known and is not required to be specified)
 
     Optional
     'unit', 'units' - unit of measure for the flow
     'context', 'compartment', 'defaultprovider', 'activitylinkid', 'target' - used to determine the termination of the exchange, default to None
 
     Ignored:
     'process' - ignored
 
+    Any remaining fields are passed to the exchange ref as initialization arguments.
+
+    A 'value' whose string is lowercase-equivalent to 'balance' will add balance=True to the initialization dict and
+    set the value to 0.
+
     :param sheetlike: an Xlrd-like object with name, nrows, and row() 
     :param term_dict: DEPRECATED.  Terminations should be handled in foreground code.
     :param node: [None] if present, use as exchange parent node for all exchanges
     :param origin: ['local.spreadsheet'] Should be provided by caller if 'node' is omitted, to give identifying 
       information to the created process
     :return:
     """
@@ -137,8 +154,12 @@
         c_flow = _row_dict(sheetlike, row)
         try:
             flow_ref, dirn, value, units, term = _exchange_params(origin, c_flow)
         except KeyError:
             print('Skipping poorly defined row %d\n%s' % (row, c_flow))
             continue
 
+        if value is ValueIsBalance:
+            c_flow['balance'] = True
+            value = 0.0
+
         yield ExchangeRef(proc_ref, flow_ref, dirn, value=value, unit=units, termination=term, **c_flow)
```

### Comparing `antelope_interface-0.1.8/antelope/interfaces/abstract_query.py` & `antelope_interface-0.2.0/antelope/interfaces/abstract_query.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 """
 Root-level catalog interface
 """
 
+
 class ValidationError(Exception):
     pass
 
 
 class PrivateArchive(Exception):
     pass
 
@@ -19,15 +20,15 @@
     Used when the actual entity is not accessible, i.e. when a ref cannot dereference itself
     """
     pass
 
 
 class AbstractQuery(object):
     """
-    Not-qute-abstract base class for executing queries
+    Not-quite-abstract base class for executing queries
 
     Query implementation must provide:
      - origin (property)
      - _iface (generator: itype)
      - _tm (property) a TermManager
     """
     _validated = None
@@ -76,15 +77,15 @@
 
     def validate(self):
         if self._validated is None:
             try:
                 self._perform_query('basic', 'validate', ValidationError)
                 self._validated = True
             except ValidationError:
-                self._validated = False
+                return False
         return self._validated
 
     def get(self, eid, **kwargs):
         """
         Basic entity retrieval-- should be supported by all implementations
         :param eid:
         :param kwargs:
@@ -121,16 +122,7 @@
     def get_uuid(self, external_ref):
         return self._perform_query('basic', 'get_uuid', EntityNotFound,
                                    external_ref)
 
     def get_reference(self, external_ref):
         return self._perform_query('basic', 'get_reference', EntityNotFound,
                                    external_ref)
-
-    def synonyms(self, item, **kwargs):
-        """
-        Return a list of synonyms for the object -- quantity, flowable, or compartment
-        :param item:
-        :return: list of strings
-        """
-        return self._perform_query('basic', 'synonyms', EntityNotFound, item,
-                                   **kwargs)
```

### Comparing `antelope_interface-0.1.8/antelope/interfaces/ibackground.py` & `antelope_interface-0.2.0/antelope/interfaces/ibackground.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,22 +15,25 @@
 The (as yet hypothetical) antelope_brightway2 plugin can provide index, inventory, and background data for a bw2
 database.
 
 More plugins are yet imagined.
 """
 
 from .abstract_query import AbstractQuery
+from itertools import chain
 
 
 class BackgroundRequired(Exception):
     pass
 
 
 _interface = 'background'
 
+BACKGROUND_VALUES_REQUIRED = {'dependencies', 'emissions', 'cutoffs', 'lci', 'sys_lci', 'foreground', 'ad', 'bf'}
+
 
 class BackgroundInterface(AbstractQuery):
     """
     BackgroundInterface core methods
     """
     def check_bg(self, reset=False, **kwargs):
         """
@@ -39,14 +42,22 @@
         :param reset: [False] whether to re-create the matrix
         :param kwargs:
         :return:
         """
         return self._perform_query(_interface, 'check_bg', BackgroundRequired,
                                    reset=reset, **kwargs)
 
+    def setup_bm(self, query):
+        """
+        Utility hook for configuring a background from an index + exchange query
+        :param query:
+        :return:
+        """
+        return False
+
     def exterior_flows(self, direction=None, search=None, **kwargs):
         """
         Yield a list of ExteriorFlows or cutoff flows, which serialize to flow, direction
         Ultimately this will be origin, flow ref, direction, context. Context=None are cutoffs.
 
         :param direction:
         :param search:
@@ -65,15 +76,16 @@
         :return:
         """
         return self._perform_query(_interface, 'consumers', BackgroundRequired,
                                    process, ref_flow=ref_flow, **kwargs)
 
     def emitters(self, flow, direction=None, context=None, **kwargs):
         """
-        Processes with a given elementary flow
+        Generate Reference exchanges which include the designated exterior flow in their inventories, optionally
+        filtering by context
         :param flow:
         :param direction:
         :param context:
         :param kwargs:
         :return:
         """
         return self._perform_query(_interface, 'emitters', BackgroundRequired,
@@ -118,46 +130,60 @@
         :param process:
         :param ref_flow:
         :return:
         """
         return self._perform_query(_interface, 'lci', BackgroundRequired,
                                    process, ref_flow=ref_flow, **kwargs)
 
-    def sys_lci(self, node, demand, **kwargs):
+    def sys_lci(self, demand, **kwargs):
         """
         Perform LCI on an arbitrary demand vector, which should be supplied as an iterable of exchanges whose
         terminations can be found in the background database.
 
         Terminations to foreground, background, and exterior flows are allowed.
 
         sys_lci(process_ref.dependencies()) + process_ref.emissions() should equal process_ref.lci()
-        (although the sum of iterables would not be straightforward to compute)
+        although the sum of iterables would not be straightforward to compute... the correct approach is:
+        sys_lci(itertools.chain(process_ref.dependencies(), process_ref.emissions(), process_ref.cutoffs()))
 
-        sys_lci(process_ref.inventory()) should equal process_ref.lci() directly, up to a normalization.
-        :param node: the node that should appear as the parent/process of the returned exchanges- not used in
-         computation
+        sys_lci(process_ref.inventory()) should equal process_ref.lci() directly, up to a normalization, assuming
+        the individual exchanges are properly terminated.
         :param demand: an iterable of exchanges with terminations that can be found in the background database.
         :param kwargs:
         :return:
         """
         return self._perform_query(_interface, 'sys_lci', BackgroundRequired,
-                                   node, demand, **kwargs)
+                                   demand, **kwargs)
 
-    def bg_lcia(self, process, query_qty, ref_flow=None, **kwargs):
+    def bg_lcia(self, process, query_qty, observed=None, ref_flow=None, **kwargs):
         """
         returns an LciaResult object, aggregated as appropriate depending on the interface's privacy level.
+        This is an ensemble function that stitches together bg functions with quantity access.
+
         :param process:
-        :param query_qty: if this is a catalog ref, the Qdb will auto-load characterization factors.  If the
-        characterization factors are already loaded, a string reference will suffice.
+        :param query_qty: must be an operable quantity_ref. the process must have exchange access
+        :param observed: iterable of DirectedFlows (flow: FlowSpec, direction: str)
         :param ref_flow:
         :param kwargs:
         :return:
         """
-        return self._perform_query(_interface, 'bg_lcia', BackgroundRequired,
-                                   process, query_qty, ref_flow=ref_flow, **kwargs)
+        p_ref = self.make_ref(self.get(process))  # a ref
+        if observed is None:
+            observed = ()
+        obs = set((x.flow.external_ref, x.direction) for x in observed)
+        if len(obs) > 0:
+            inventory = chain(p_ref.dependencies(ref_flow=ref_flow),
+                              p_ref.emissions(ref_flow=ref_flow),
+                              p_ref.cutoffs(ref_flow=ref_flow))
+            incl = (k for k in inventory if (k.flow.external_ref, k.direction) not in obs)
+            lci = self.sys_lci(incl)
+        else:
+            lci = p_ref.lci(ref_flow=ref_flow)
+        # aggregation
+        return query_qty.do_lcia(lci, **kwargs)
 
     '''
     Methods requiring a partial ordering (implemented by antelope_background)
     '''
     def foreground_flows(self, search=None, **kwargs):
         """
         Yield a list of Reference Exchanges that make up the foreground (e.g. rows/columns of Af).
@@ -181,14 +207,16 @@
                                    search=search, **kwargs)
 
     def foreground(self, process, ref_flow=None, **kwargs):
         """
         Returns an ordered list of exchanges for the foreground matrix Af for the given process and reference flow-
         the first being the named process + reference flow, and every successive one having a named termination, so
         that the exchanges could be linked into a fragment tree.
+
+        This technically should require exchange interface as well as values
         :param process:
         :param ref_flow:
         :return:
         """
         return self._perform_query(_interface, 'foreground', BackgroundRequired,
                                    process, ref_flow=ref_flow, **kwargs)
```

### Comparing `antelope_interface-0.1.8/antelope/interfaces/iconfigure.py` & `antelope_interface-0.2.0/antelope/interfaces/iconfigure.py`

 * *Files identical despite different names*

### Comparing `antelope_interface-0.1.8/antelope/interfaces/iexchange.py` & `antelope_interface-0.2.0/antelope/interfaces/iexchange.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,14 +4,16 @@
 
 class ExchangeRequired(Exception):
     pass
 
 
 _interface = 'exchange'
 
+EXCHANGE_VALUES_REQUIRED = {'ev', 'exchange_values', 'inventory', 'exchange_relation'}
+
 
 class ExchangeInterface(AbstractQuery):
     """
     InventoryInterface core methods: individual processes, quantitative data.
 
     Need to do some thinking here-- the list of methods is very short. In particular there is no way to do any of
     the following:
@@ -36,26 +38,29 @@
 
     def ev(self, process, flow, direction=None, termination=None, ref_flow=None, **kwargs):
         """
         Return a float.  Symmetric to quantity.cf
         :param process:
         :param flow:
         :param direction: [None] if none, if flows exist with both directions, raise an error
-        :param termination: [None] if none, return sum of cutoff flows
+        :param termination: [None] if none, return sum of flows across all terminations
         :param ref_flow: [None] if none, return unallocated value. Otherwise, return value allocated to a unit of the
          specified reference
         :return: a float
         """
-        return self._perform_query(_interface, 'exchange_values', ExchangeRequired,
+        return self._perform_query(_interface, 'ev', ExchangeRequired,
                                    process, flow, direction=direction, termination=termination, ref_flow=ref_flow,
                                    **kwargs)
 
     def exchange_values(self, process, flow, direction=None, termination=None, reference=None, **kwargs):
         """
         Leftover from earlier implementation; deprecated.
+        2022-12-27: is this really deprecated? it's used in computing reference_value and I don't see any other way...
+        perhaps we should add reference_value() to the API but for now let's keep this around
+
         Return a list of exchanges with values matching the specification
         :param process:
         :param flow:
         :param direction: [None] if none,
         :param termination: [None] if none, return all terminations
         :param reference: [None] if True, only find reference exchanges. If false- maybe omit reference exchanges?
         :return: list of exchanges with values matching the specification
```

### Comparing `antelope_interface-0.1.8/antelope/interfaces/iindex.py` & `antelope_interface-0.2.0/antelope/interfaces/iindex.py`

 * *Files identical despite different names*

### Comparing `antelope_interface-0.1.8/antelope/interfaces/iquantity.py` & `antelope_interface-0.2.0/antelope/interfaces/iquantity.py`

 * *Files 18% similar despite different names*

```diff
@@ -68,39 +68,44 @@
 _interface = 'quantity'
 
 
 class QuantityInterface(AbstractQuery):
     """
     QuantityInterface
     """
-    def get_canonical(self, quantity, **kwargs):
+    '''
+    qdb- and native-level queries
+    '''
+
+    def synonyms(self, item, **kwargs):
         """
-        Retrieve a canonical quantity based on a synonym or other distinguishable term.  Canonical quantities
-        include standard concepts like "mass" that have a semantic scope that is broader than LCA, and also reference
-        versions of LCIA methods such as CML2001 / GWP-100. It is up to the implementation to canonicalize these.
-        :param quantity: external_id of quantity
-        :return: QuantityRef
+        Return a list of synonyms for the object -- quantity, flowable, or compartment
+        :param item:
+        :return: list of strings
         """
-        return self.make_ref(self._perform_query(_interface, 'get_canonical',
-                                                 QuantityRequired,
-                                                 quantity, **kwargs))
+        return self._perform_query(_interface, 'synonyms', QuantityRequired, item,
+                                   **kwargs)
 
     def profile(self, flow, **kwargs):
         """
         Generate characterizations for the named flow or flowable, with the reference quantity noted in each case
         :param flow:
         :return: list of characterizations
         """
         return self._perform_query(_interface, 'profile', QuantityRequired,
                                    flow, **kwargs)
 
     def characterize(self, flowable, ref_quantity, query_quantity, value, context=None, location='GLO', **kwargs):
         """
         Add Characterization data for a flowable, reporting the amount of a query quantity that is equal to a unit
-        amount of a reference quantity, for a given context and location
+        amount of a reference quantity, for a given context and location.
+
+        At the native level, this is only used internally. At the qdb level there is basically no reason to use it--
+        characterizations should only get added via import_cfs() which is part of get_canonical()
+
         :param flowable: string or flow external ref
         :param ref_quantity: string or external ref
         :param query_quantity: string or external ref
         :param value: float or dict of locations to floats
         :param context: string
         :param location: string, ignored if value is dict
         :param kwargs: overwrite=False, origin=query_quantity.origin, others?
@@ -168,40 +173,153 @@
                                    quantity, inventory, locale=locale, **kwargs)
 
     def lcia(self, process, ref_flow, quantity_ref, **kwargs):
         """
         Perform process foreground LCIA for the given quantity reference.  Included for compatibility with antelope v1.
         In this query, the inventory is computed remotely; whereas with quantity.do_lcia() inventory knowledge is
         required
+
+        The way we imagine this working in the days of future XDB/QDB:
+         - it's not foreground LCIA at all, it's encapsulated LCIA
+         - it's not part of the quantity interface, it's part of the basic interface
+         - it requires background data implemented at the server, even if the client is denied background authorization
+           (hence the basic interface)
+         - either the quantity ref must be known locally or resolvable to a do_lcia operation by the catalog
+         - there is also the implied need for sys_lcia which is a POST operation that uses sys_lci
+        It needs to be rewritten.
+
         :param process:
         :param ref_flow:
         :param quantity_ref:
         :param kwargs:
         :return: an LciaResult whose components are flows
         """
         return self._perform_query(_interface, 'lcia', QuantityRequired,
                                    process, ref_flow, quantity_ref, **kwargs)
 
+    '''
     def fragment_lcia(self, fragment, quantity_ref, scenario=None, **kwargs):
         """
         Perform fragment LCIA by first traversing the fragment to determine node weights, and then combining with
         unit scores.
         Not sure whether this belongs in Quantity or Foreground. but probably foreground.
         :param fragment:
         :param quantity_ref:
         :param scenario:
         :param kwargs:
         :return: an LciaResult whose components are FragmentFlows
         """
         return self._perform_query(_interface, 'fragment_lcia', QuantityRequired,
                                    fragment, quantity_ref, scenario, **kwargs)
+    '''
 
     def norm(self, quantity_ref, region=None, **kwargs):
         """
         Return a normalization factor for the named quantity ref, as a single number.
         :param quantity_ref:
         :param region: not well supported
         :param kwargs:
         :return: a floating-point number, which is 0.0 if no normalisationFactors (OpenLCA spec) are available.
         """
         return self._perform_query(_interface, 'norm', QuantityRequired,
                                    quantity_ref, region=region, **kwargs)
+
+    '''
+    core required functionality
+    NOTE: a foreground interface must have access to a qdb to run get_canonical
+    '''
+    def new_quantity(self, name, ref_unit=None, **kwargs):
+        """
+        Creates a new quantity entity and adds it to the foreground
+        :param name:
+        :param ref_unit:
+        :param kwargs:
+        :return:
+        """
+        return self._perform_query(_interface, 'new_quantity', QuantityRequired,
+                                   name, ref_unit=ref_unit, **kwargs)
+
+    def new_flow(self, name, ref_quantity=None, context=None, **kwargs):
+        """
+        Creates a new flow entity and adds it to the foreground
+        :param name: required flow name
+        :param ref_quantity: [None] implementation must handle None / specify a default
+        :param context: [None] Required if flow is strictly elementary. Should be a tuple
+        :param kwargs:
+        :return:
+        """
+        return self._perform_query(_interface, 'new_flow', QuantityRequired,
+                                   name, ref_quantity=ref_quantity, context=context,
+                                   **kwargs)
+
+    '''
+    qdb-only queries
+    '''
+
+    def is_lcia_engine(self, **kwargs):
+        """
+        A key question in the quantity interface is the way terms are managed.  There are two main footings:
+         - the terms specified by the source are authentic / canonical and should be reproduced
+         - terms from different data sources refer to the same concept.
+        An archive's Term Manager determines how input terms are interpreted and how characterizations are looked up.
+
+        if the term manager is an LciaEngine, it uses a standard set of contexts and flowables, and provides routes
+        to add new synonyms for flowables/contexts and to report new flowables or contexts.  Ultimately the objective
+        is to manage characterization + knowledge of intermediate flows.
+
+        This routine reports whether an interface implements the LciaEngine [protocol?] for dealing with flows.
+
+        :param kwargs:
+        :return: True/False - could also provide more structured information as needed.
+        """
+
+        try:
+            return self._perform_query(_interface, 'is_lcia_engine', QuantityRequired, **kwargs)
+        except QuantityRequired:
+            return False
+
+    def get_canonical(self, quantity, **kwargs):
+        """
+        This is not really qdb-specific as trivial for non-qdbs.
+        Retrieve a canonical quantity based on a synonym or other distinguishable term.  Canonical quantities
+        include standard concepts like "mass" that have a semantic scope that is broader than LCA, and also reference
+        versions of LCIA methods such as CML2001 / GWP-100. It is up to the implementation to canonicalize these.
+        :param quantity: external_id of quantity
+        :return: QuantityRef
+        """
+        return self.make_ref(self._perform_query(_interface, 'get_canonical',
+                                                 QuantityRequired,
+                                                 quantity, **kwargs))
+
+    def get_factors(self, quantity, flows, **kwargs):
+        """
+        Accept an iterable of flow specifications (either a flow UUID which is known(?) and/or (flowable, ref_quantity,
+        context, locale)). Return a list of
+        :param quantity: a query quantity
+        :param flows: an iterable of flow specifications (flowable, ref_quantity, context, locale)
+        :param kwargs:
+        :return:
+        """
+        return self._perform_query(_interface, 'get_factors', QuantityRequired,
+                                   quantity, flows, **kwargs)
+
+    def flows_with_origin(self, origin, flowable=None, context=None, locale=None, **kwargs):
+        """
+        Return a list of flows matching the supplied characteristics
+        :param origin:
+        :param flowable:
+        :param context:
+        :param locale:
+        :param kwargs:
+        :return:
+        """
+        return self._perform_query(_interface, 'flows_with_origin', QuantityRequired,
+                                   origin, flowable=flowable, context=context, locale=locale, **kwargs)
+
+    def post_flows(self, flows):
+        """
+        flows_with_origin as POST/PUT/PATCH
+        :param flows: iterable of inputs to f_w_o
+        :return:
+        """
+        pass
+
```

### Comparing `antelope_interface-0.1.8/antelope/refs/base.py` & `antelope_interface-0.2.0/antelope/refs/base.py`

 * *Files 11% similar despite different names*

```diff
@@ -29,97 +29,117 @@
 
 The CatalogRef can instantiate a grounded reference if supplied with a query object that implements the interface.
 
 """
 from synonym_dict import LowerDict
 
 from ..flows import BaseEntity
-from ..interfaces.abstract_query import NoAccessToEntity
+from ..interfaces.abstract_query import NoAccessToEntity, EntityNotFound
+
+import re
+
+uuid_regex = re.compile('([0-9a-f]{8}-?([0-9a-f]{4}-?){3}[0-9a-f]{12})', flags=re.IGNORECASE)
 
 
 class NoCatalog(Exception):
     pass
 
 
 class InvalidQuery(Exception):
     pass
 
 
 class EntityRefMergeError(Exception):
     pass
 
 
+class PropertyExists(Exception):
+    pass
+
+
 class BaseRef(BaseEntity):
     """
     A base class for defining entity references.  The base class can also store information, such as properties
     """
     _etype = None
+    _uuid = None
 
     def __init__(self, origin, external_ref, uuid=None, **kwargs):
         """
 
         :param origin:
         :param external_ref:
         :param kwargs:
         """
         self._origin = origin
         self._ref = external_ref
-        self._uuid = uuid
+        self.uuid = uuid
 
         self._d = LowerDict()
-        self._d.update({k: v for k, v in filter(lambda x: x[1] is not None, kwargs.items())})
+        for k, v in kwargs.items():
+            if v is not None:
+                self.__setitem__(k, v)
+
+        if self._uuid is None:
+            self.uuid = str(external_ref)  # regex check happens inside; NOP if fails
 
     @property
     def origin(self):
         return self._origin
 
     @property
     def external_ref(self):
-        return self._ref
+        return str(self._ref)
 
     @property
     def uuid(self):
-        return self._uuid or self._ref
+        return self._uuid
+
+    @uuid.setter
+    def uuid(self, value):
+        if self._uuid is not None:
+            raise PropertyExists(self.link, self._uuid)
+        if uuid_regex.match(str(value)):
+            self._uuid = str(value)
+            # do nothing if regex does not match
 
     @property
     def entity_type(self):
         if self._etype is None:
             return 'unknown'
         return self._etype
 
-    def _localitem(self, item):
-        if item in self._d:
-            return self._d[item]
-        if 'local_%s' % item in self._d:
-            return self._d['local_%s' % item]
-
     def __getitem__(self, item):
         """
         should be overridden
         :param item:
         :return:
         """
-        return self._localitem(item)
+        return self._d.__getitem__(item)
 
     def properties(self):
         for k in self._d.keys():
             yield k
 
     def get(self, item, default=None):
+        """
+        get() is local only. subclasses should implement get_item() to access items via a query
+        :param item:
+        :param default:
+        :return:
+        """
         try:
-            return self.__getitem__(item)
+            return self._d.__getitem__(item)
         except KeyError:
             return default
 
     def has_property(self, item):
-        return self._localitem(item) is not None
+        return item in self._d
 
     def __setitem__(self, key, value):
-        if not key.lower().startswith('local_'):
-            key = 'local_%s' % key
         self._d[key] = value
 
     @property
     def _name(self):
         """
         This should be the same as .name for entities; whereas str(ref) prepends origin
         :return:
@@ -141,15 +161,15 @@
         Catalog refs are equal if their external_refs are equal and their origins start with each other
         :param other:
         :return:
         """
         if other is None:
             return False
         try:
-            return (#(other.entity_type == 'unknown' or self.entity_type == other.entity_type) and
+            return (  # (other.entity_type == 'unknown' or self.entity_type == other.entity_type) and
                     self.external_ref == other.external_ref and
                     (self.origin.startswith(other.origin) or other.origin.startswith(self.origin)))
         except AttributeError:
             return False
 
     def __str__(self):
         return '[%s] %s' % (self.origin, self._name)
@@ -218,14 +238,21 @@
             j['entityType'] = self._etype
         # j.update(self._d)  ## don't want this
         if 'Name' in self._d:
             j['Name'] = self._d['Name']
         return j
 
 
+class _MissingItem(Exception):
+    """
+    Used to prevent repeated upstream queries for a missing item
+    """
+    pass
+
+
 class EntityRef(BaseRef):
     """
     An EntityRef is a CatalogRef that has been provided a valid catalog query.  the EntityRef is still semi-abstract
     since there is no meaningful reference to an entity that is not typed.
     """
     _ref_field = 'referenceEntity'
 
@@ -255,19 +282,30 @@
             raise InvalidQuery('Query failed validation')
         return self._the_query
 
     @property
     def uuid(self):
         if self._uuid is None:
             try:
-                self._uuid = self._query.get_uuid(self.external_ref)
+                _uuid = self._query.get_uuid(self.external_ref)
+                if _uuid:  # implementation should return a valid UUID, or False [cannot return None]
+                    self._uuid = _uuid
             except InvalidQuery:
                 pass  # a None uuid is fine, but next time we ask, it will check again
         return self._uuid
 
+    @uuid.setter
+    def uuid(self, value):
+        # need to repeat this because uuid is overridden
+        if self._uuid is not None:
+            raise PropertyExists(self.link, self._uuid)
+        if uuid_regex.match(str(value)):
+            self._uuid = str(value)
+            # do nothing if regex does not match
+
     def query_synonyms(self, term):
         """
         Provide access to root archive's synonyms
         :param term:
         :return:
         """
         return self._query.synonyms(term)
@@ -285,44 +323,49 @@
         return self._reference_entity
 
     @property
     def resolved(self):
         return True
 
     def signature_fields(self):
-        yield self._ref_field
+        # this seems problematic
+        # just let a ref yield everything it knows
+        for k in self._d.keys():
+            yield k
 
     def _show_ref(self):
-        print('reference: %s' % self.reference_entity)
+        print('%s: %s' % (self.reference_field, self.reference_entity))
 
     def _show_hook(self):
         if self._uuid:
-            print('UUID: %s' % self.uuid)
+            print('   UUID: %s' % self.uuid)
         for i in ('Name', 'Comment'):
             try:
                 print('%7s: %s' % (i, self.get_item(i)))
             except NoAccessToEntity:
                 print('%7s: NoAccessToEntity' % i)
             except KeyError:
-                pass
+                self[i] = ''
+        if self._reference_entity is not None:
+            self._show_ref()
 
     def validate(self):
         """
         This is required by certain implementations to be added to archives (born legacy...)
         There should be no way to get through the instantiation without a valid query, so this should probably just
         return True (or be made more useful)
         :return:
         """
         if self._query is None:
             return False
         return True
 
     def properties(self):
         try:
-            for k in self._query.properties(self.external_ref):
+            for k in self._query.properties(self):
                 yield k
         except NoAccessToEntity:
             for k in self._d.keys():
                 yield k
 
     def get_item(self, item, force_query=True):
         """
@@ -334,44 +377,58 @@
            -- which causes recursion error if the query actually gets the entity_ref
            --- attempted solution with NoAccessToEntity exception in BasicImplementation
          - fine. So when do we raise a key error?
         :param item:
         :param force_query:
         :return:
         """
+        if item == self._ref_field:
+            return self.reference_entity
         # check local first.  return Localitem if present.
-        loc = self._localitem(item)
-        if loc is not None:
+        loc = self.get(item)
+        if loc is _MissingItem:
+            raise KeyError(item)
+        elif loc is not None:
             return loc
-        if force_query:
+        else:
             # self._check_query('getitem %s' % item)
-            val = self._query.get_item(self, item)
-            if val is not None and val != '':
+            try:
+                val = self._query.get_item(self, item)
+            except NoAccessToEntity:
+                try:  # this works in masquerade: the local.qdb query retrieves the authentic ref from the qdb
+                    lit = self._query.get(self.link)
+                except EntityNotFound:
+                    self._d[item] = _MissingItem
+                    raise KeyError(item)
+                if lit is self:
+                    raise
+                val = lit.get_item(item)
+            except KeyError:
+                self._d[item] = _MissingItem
+                raise
+            # we used to catch '' too but this is ng- remote will think it's a property but local will raise MissingItem
+            if val is not None:  # and val != ''
                 self._d[item] = val
                 return val
+        self._d[item] = _MissingItem
         raise KeyError(item)
 
     def __getitem__(self, item):
-        if item == self._ref_field:
-            return self.reference_entity
-        val = self.get_item(item)
-        if val is None:
-            raise KeyError(item)
-        return val
+        return self.get_item(item)
 
     def has_property(self, item):
         """
         let's deal with the recursion issue head-on
         :param item:
         :return:
         """
         try:
             self.get_item(item)
+            return True
         except (KeyError, NoAccessToEntity, InvalidQuery):
             return False
-        return True
 
     def serialize(self, **kwargs):
         j = super(EntityRef, self).serialize(**kwargs)
         if self._uuid:
             j['uuid'] = self.uuid
         return j
```

### Comparing `antelope_interface-0.1.8/antelope/refs/catalog_ref.py` & `antelope_interface-0.2.0/antelope/refs/catalog_ref.py`

 * *Files identical despite different names*

### Comparing `antelope_interface-0.1.8/antelope/refs/flow_ref.py` & `antelope_interface-0.2.0/antelope/refs/flow_ref.py`

 * *Files 10% similar despite different names*

```diff
@@ -15,27 +15,41 @@
     Flows can lookup:
     """
     _etype = 'flow'
     _ref_field = 'referenceQuantity'
 
     def __init__(self, *args, **kwargs):
         super(FlowRef, self).__init__(*args, **kwargs)
+        '''
         try:
             self._add_synonym(self._localitem('name'), set_name=True)
         except (KeyError, AttributeError):
             pass
-        if self.has_property('casnumber'):
+        if self._localitem('casnumber'):
             self._add_synonym(self._localitem('casnumber'))
+        '''
         self._flowable.add_term(self.link)
-        self._chars_seen = dict()
+
+    @property
+    def context(self):
+        return self._query.get_context(self._context)
+
+    @context.setter
+    def context(self, value):
+        self._catch_context('Context', value)
 
     @property
     def _addl(self):
         return self.unit
 
+    def _show_hook(self):
+        print('Context: %s' % (self.context, ))
+        print(' Locale: %s' % self.locale)
+        super(FlowRef, self)._show_hook()
+
     '''
     def has_characterization(self, quantity, location='GLO'):
         """
         A flow ref keeps track of characterizations by link
         :param quantity:
         :param location:
         :return:
@@ -86,21 +100,26 @@
         return j
 
     '''
     Interface methods
     '''
     def get_context(self):
         try:
-            return self._query.get_context(self.context)
+            return self._query.get_context(self._context)
         except InvalidQuery:
-            return self._the_query.get_context(self.context)  # this one can bypass -- by talking directly to the catalog
+            return self._the_query.get_context(self._context)  # this one can bypass -- by talking directly to the catalog
 
     def targets(self, direction=None, **kwargs):
         return self._query.targets(self.external_ref, direction, **kwargs)
 
+    def emitters(self, direction=None, context=None, **kwargs):
+        if context is None:
+            context = self.context
+        return self._query.emitters(self.external_ref, direction=direction, context=context, **kwargs)
+
     def terminate(self, **kwargs):
         return self.targets(**kwargs)
 
     def originate(self, direction=None, **kwargs):
         return self._query.originate(self.external_ref, direction, **kwargs)
 
     def profile(self, **kwargs):
@@ -115,16 +134,17 @@
                                         origin=self.origin, location=location, **kwargs)
 
     def cf(self, quantity, **kwargs):
         return quantity.cf(self, **kwargs)
 
     '''
     Characterization caching
-    '''
+    this is now builtin to the flow interface
     def see_char(self, qq, cx, loc, qrr):
         self._chars_seen[qq, cx, loc] = qrr
 
     def chk_char(self, qq, cx, loc):
         return self._chars_seen[qq, cx, loc]
 
     def pop_char(self, qq, cx, loc):
         return self._chars_seen.pop((qq, cx, loc), None)
+    '''
```

### Comparing `antelope_interface-0.1.8/antelope/refs/process_ref.py` & `antelope_interface-0.2.0/antelope/refs/process_ref.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from .base import EntityRef
 from .exchange_ref import ExchangeRef
+from itertools import chain
 
 
 class MultipleReferences(Exception):
     pass
 
 
 class NoReference(Exception):
@@ -15,15 +16,15 @@
     Processes can lookup:
     """
     _etype = 'process'
     _ref_field = 'referenceExchange'
 
     @property
     def _addl(self):
-        return self._localitem('SpatialScope') or ''
+        return self.get('SpatialScope', default='')
 
     def __init__(self, external_ref, query, **kwargs):
         self._default_rx = None
         self._lci = dict()
         super(ProcessRef, self).__init__(external_ref, query, **kwargs)
 
     @property
@@ -124,45 +125,47 @@
                 return ref_flow.external_ref
             raise TypeError('Invalid reference exchange: %s' % ref_flow)
         return ref_flow
 
     '''
     Inventory queries
     '''
+    def _to_exch_ref(self, x, value):
+        return ExchangeRef(self, self._query.make_ref(x.flow), x.direction, value=value, termination=x.termination,
+                           comment=x.comment, is_reference=x.is_reference)
+
     def exchanges(self, **kwargs):
         for x in self._query.exchanges(self.external_ref, **kwargs):
-            yield ExchangeRef(self, self._query.make_ref(x.flow), x.direction, value=None, termination=x.termination,
-                              comment=x.comment)
+            yield self._to_exch_ref(x, value=None)
 
     def exchange_values(self, flow, direction=None, termination=None, reference=None, **kwargs):
         """
-        This should get replaced by ev()
+        oooh kay...
         :param flow:
         :param direction:
         :param termination:
         :param reference:
         :param kwargs:
         :return:
         """
         if hasattr(flow, 'entity_type'):
             if flow.entity_type == 'exchange':
                 flow = flow.flow.external_ref
             elif flow.entity_type == 'flow':
                 flow = flow.external_ref
-        for x in  self._query.exchange_values(self.external_ref, flow, direction,
-                                              termination=termination, reference=reference, **kwargs):
-            yield ExchangeRef(self, self._query.make_ref(x.flow), x.direction, value=x.value, termination=x.termination,
-                              comment=x.comment)
+        for x in self._query.exchange_values(self.external_ref, flow, direction,
+                                             termination=termination, reference=reference, **kwargs):
+            yield self._to_exch_ref(x, value=x.values)
 
     def inventory(self, ref_flow=None, **kwargs):
         # ref_flow = self._use_ref_exch(ref_flow)  # ref_flow=None returns unallocated inventory
-        for x in sorted(self._query.inventory(self.external_ref, ref_flow=ref_flow, **kwargs),
-                        key=lambda t: (not t.is_reference, t.type == 'elementary', t.type == 'context', t.type == 'cutoff', t.direction)):
-            yield ExchangeRef(self, self._query.make_ref(x.flow), x.direction, value=x.value, termination=x.termination,
-                              comment=x.comment, is_reference=x.is_reference)
+        inv = [ExchangeRef(self, self._query.make_ref(x.flow), x.direction, value=x.value, termination=x.termination,
+                           comment=x.comment, is_reference=x.is_reference)
+               for x in self._query.inventory(self.external_ref, ref_flow=ref_flow, **kwargs)]
+        return sorted(inv, key=lambda t: (not t.is_reference, t.direction, t.type == 'context', t.type == 'cutoff'))
 
     def exchange_relation(self, ref_flow, exch_flow, direction, termination=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
         if hasattr(exch_flow, 'external_ref'):
             exch_flow = exch_flow.external_ref
         return self._query.exchange_relation(self.external_ref, ref_flow,
                                              exch_flow, direction,
@@ -172,17 +175,27 @@
         ref_flow = self._use_ref_exch(ref_flow)
         return self._query.lcia(self.external_ref, ref_flow, lcia_qty, **kwargs)
 
     '''
     support process
     '''
     def reference_value(self, flow=None):
-        if flow is None:
-            flow = self.reference().flow
-        return sum(x.value for x in self.exchange_values(flow, reference=True))
+        """
+        Attempts to return the un-allocated exchange value for the designated reference exchange
+        :param flow:
+        :return:
+        """
+        flow = self.reference(flow).flow
+        rx = list(self.exchange_values(flow, reference=True))
+        if len(rx) < 1:
+            raise NoReference(flow)
+        elif len(rx) > 1:
+            raise MultipleReferences(flow)
+        else:
+            return rx[0].values[None]
 
     def get_exchange(self, key):
         try:
             return next(x for x in self.reference_entity if x.key == key)
         except StopIteration:
             raise KeyError
 
@@ -192,14 +205,17 @@
         This is hugely kludgely. What should be the expected behavior of a process ref asked to perform allocation?
         :return:
         """
         return None
 
     '''
     Background queries
+    
+    BIG question here: should the ProcessRef convert ALL these to ExchangeRefs?  
+    and the answer is yes: that way client code knows it was constructed properly
     '''
     def foreground(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
         return self._query.foreground(self.external_ref, ref_flow=ref_flow, **kwargs)
 
     def consumers(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
@@ -213,19 +229,17 @@
         ref_flow = self._use_ref_exch(ref_flow)
         return self._query.emissions(self.external_ref, ref_flow=ref_flow, **kwargs)
 
     def cutoffs(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
         return self._query.cutoffs(self.external_ref, ref_flow=ref_flow, **kwargs)
 
-    def is_in_background(self, termination=None, ref_flow=None, **kwargs):
-        if termination is None:
-            termination = self.external_ref
+    def is_in_background(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
-        return self._query.is_in_background(termination, ref_flow=ref_flow, **kwargs)
+        return self._query.is_in_background(self.external_ref, ref_flow=ref_flow, **kwargs)
 
     def ad(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
         return self._query.ad(self.external_ref, ref_flow, **kwargs)
 
     def bf(self, ref_flow=None, **kwargs):
         ref_flow = self._use_ref_exch(ref_flow)
@@ -240,37 +254,49 @@
         :return:
         """
         ref_flow = self._use_ref_exch(ref_flow)
         if refresh:
             self._lci.pop(ref_flow, None)
         if ref_flow not in self._lci:
 
-            self._lci[ref_flow] = list(self._query.lci(self.external_ref, ref_flow, **kwargs))
+            self._lci[ref_flow] = [self._to_exch_ref(i, i.value)
+                                   for i in self._query.lci(self.external_ref, ref_flow, **kwargs)]
         for i in self._lci[ref_flow]:
             yield i
 
     def unobserved_lci(self, observed, ref_flow=None, **kwargs):
         """
         Performs a sys_lci of the process's unobserved exchanges. derived by excluding observed exchanges from the
         process's inventory and passing the result to sys_lci.  Note that terminations are ignored-- if a process
-        has an observed Electricity flow, all the process's electricity exchanges are assumed to be accounted for
-        by the observation.  (flow.external_ref, direction) is the filter.
+        has an observed (e.g.) Electricity flow, all the process's electricity exchanges are assumed to be accounted
+        for by the observation.  (flow.external_ref, direction) is the filter.
+
+        Problem with this implementation: if the exchanges do not contain termination info, then the resulting
+        inclusion inventory will be non-operable in the background.  Because it is a background method, it may be
+        more appropriate to use the combined dependencies and emissions rather than inventory.
 
         :param observed: iterable of exchanges or child flows, having a flow (with external_ref) and direction
         :param ref_flow:
         :param kwargs:
         :return:
         """
         excl = set((k.flow.external_ref, k.direction) for k in observed)
+        if len(excl) == 0:
+            return self.lci(ref_flow=ref_flow, **kwargs)
         ref_flow = self._use_ref_exch(ref_flow)
-        incl = (k for k in self.inventory(ref_flow) if (k.flow.external_ref, k.direction) not in excl)
-        return self._query.sys_lci(self, incl, **kwargs)
+        inventory = chain(self.dependencies(ref_flow=ref_flow),
+                          self.emissions(ref_flow=ref_flow),
+                          self.cutoffs(ref_flow=ref_flow))
+        incl = (k for k in inventory if (k.flow.external_ref, k.direction) not in excl)
+        for i in self._query.sys_lci(incl, **kwargs):
+            yield self._to_exch_ref(i, i.value)
 
-    def bg_lcia(self, lcia_qty, ref_flow=None, **kwargs):
+    def bg_lcia(self, lcia_qty, observed=None, ref_flow=None, **kwargs):
         """
         :param lcia_qty: should be a quantity ref (or qty), not an external ID
+        :param observed: see unobserved_lci
         :param ref_flow:
         :param kwargs:
         :return:
         """
         ref_flow = self._use_ref_exch(ref_flow)
-        return self._query.bg_lcia(self.external_ref, lcia_qty, ref_flow=ref_flow, **kwargs)
+        return self._query.bg_lcia(self.external_ref, lcia_qty, observed=observed, ref_flow=ref_flow, **kwargs)
```

### Comparing `antelope_interface-0.1.8/antelope_interface.egg-info/PKG-INFO` & `antelope_interface-0.2.0/antelope_interface.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,37 +1,36 @@
 Metadata-Version: 2.1
 Name: antelope-interface
-Version: 0.1.8
-Summary: UNKNOWN
+Version: 0.2.0
 Home-page: https://github.com/AntelopeLCA/antelope
 Author: Brandon Kuczenski
 Author-email: bkuczenski@ucsb.edu
 License: BSD 3-Clause
-Description: # antelope
-        Standard Interface and reference framework for LCA
-        
-        The `antelope` package is an interface specification for accessing LCA data resources, as described in [JIE submitted].  It should be subclassed by implementations that wish to expose data using this uniform interface.  A reference implementation, including a stand-alone LCA computing tool, exists...
-        
-        ## Documentation
-        
-        See the following articles:
-        
-         * [Antelope Design Principles](principles.md) for documentation of this repository.
-         * [Entity Specification](entities.md) and nomenclature.
-         * [Return Types](types.md) which are *references* to entities.
-        
-        ### See Also
-        
-         * [antelope_core](https://github.com/AntelopeLCA/core) The reference implementation including local data source management.
-         * [antelope_background](https://github.com/AntelopeLCA/background) Used for partial ordering of databases and construction and inversion of matrices
-         * [antelope_foreground](https://github.com/AntelopeLCA/foreground) Used for building foreground models
-        
-Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Natural Language :: English
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Topic :: Scientific/Engineering
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# antelope
+Standard Interface and reference framework for LCA
+
+The `antelope` package is an interface specification for accessing LCA data resources, as described in [JIE submitted].  It should be subclassed by implementations that wish to expose data using this uniform interface.  A reference implementation, including a stand-alone LCA computing tool, exists...
+
+## Documentation
+
+See the following articles:
+
+ * [Antelope Design Principles](principles.md) for documentation of this repository.
+ * [Entity Specification](entities.md) and nomenclature.
+ * [Return Types](types.md) which are *references* to entities.
+
+### See Also
+
+ * [antelope_core](https://github.com/AntelopeLCA/core) The reference implementation including local data source management.
+ * [antelope_background](https://github.com/AntelopeLCA/background) Used for partial ordering of databases and construction and inversion of matrices
+ * [antelope_foreground](https://github.com/AntelopeLCA/foreground) Used for building foreground models
```

### Comparing `antelope_interface-0.1.8/antelope_interface.egg-info/SOURCES.txt` & `antelope_interface-0.2.0/antelope_interface.egg-info/SOURCES.txt`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,18 @@
 LICENSE
+MANIFEST.in
 README.md
 setup.py
 antelope/__init__.py
 antelope/exchanges_from_spreadsheet.py
+antelope/xdb_tokens.py
 antelope/flows/__init__.py
 antelope/flows/flow.py
 antelope/flows/flow_interface.py
+antelope/flows/openlca_locales.json
 antelope/interfaces/__init__.py
 antelope/interfaces/abstract_query.py
 antelope/interfaces/ibackground.py
 antelope/interfaces/iconfigure.py
 antelope/interfaces/iexchange.py
 antelope/interfaces/iforeground.py
 antelope/interfaces/iindex.py
@@ -17,12 +20,14 @@
 antelope/refs/__init__.py
 antelope/refs/base.py
 antelope/refs/catalog_ref.py
 antelope/refs/exchange_ref.py
 antelope/refs/flow_ref.py
 antelope/refs/process_ref.py
 antelope/refs/quantity_ref.py
+antelope/refs/tests/__init__.py
+antelope/refs/tests/test_flows.py
 antelope_interface.egg-info/PKG-INFO
 antelope_interface.egg-info/SOURCES.txt
 antelope_interface.egg-info/dependency_links.txt
 antelope_interface.egg-info/requires.txt
 antelope_interface.egg-info/top_level.txt
```

### Comparing `antelope_interface-0.1.8/setup.py` & `antelope_interface-0.2.0/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,17 +1,22 @@
 from setuptools import setup, find_packages
 
-ANTELOPE_VERSION = '0.1.8'
+ANTELOPE_VERSION = '0.2.0'
 
 requires = [
-    "synonym_dict>=0.2.0"
+    "synonym_dict>=0.2.0",
+    "pydantic>=1.8.2"
 ]
 
 """
 Version History:
+0.2.0-virtualize - in progress, with xdb
+                   minimal complete foreground spec
+                   add xdb token spec
+                   
 0.1.8 2022/04/08 - Minor changes, to go along with 0.1.8 core release
  - support None in exchanges_from_spreadsheet (this will still not work until xls_tools is out)
  - add comp_sense function to relate Sink-Output and Source-Input
  - add emitters() function
  - add positional search argument for flowables()
  - allow refs to operate with invalid queries
 
@@ -45,14 +50,15 @@
     author_email="bkuczenski@ucsb.edu",
     license="BSD 3-Clause",
     install_requires=requires,
     url="https://github.com/AntelopeLCA/antelope",
     summary="An interface specification for accessing LCA data",
     long_description_content_type='text/markdown',
     long_description=open('README.md').read(),
+    include_package_data=True,
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Science/Research",
         "License :: OSI Approved :: BSD License",
         "Natural Language :: English",
         "Operating System :: OS Independent",
         "Programming Language :: Python :: 3",
```

