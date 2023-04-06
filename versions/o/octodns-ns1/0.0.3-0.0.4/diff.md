# Comparing `tmp/octodns-ns1-0.0.3.tar.gz` & `tmp/octodns-ns1-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "octodns-ns1-0.0.3.tar", last modified: Tue Jan 24 18:11:41 2023, max compression
+gzip compressed data, was "octodns-ns1-0.0.4.tar", last modified: Thu Apr  6 23:32:51 2023, max compression
```

## Comparing `octodns-ns1-0.0.3.tar` & `octodns-ns1-0.0.4.tar`

### file list

```diff
@@ -1,13 +1,16 @@
-drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-01-24 18:11:41.764200 octodns-ns1-0.0.3/
--rw-r--r--   0 ross       (501) staff       (20)     4428 2023-01-24 18:11:41.763389 octodns-ns1-0.0.3/PKG-INFO
--rw-r--r--   0 ross       (501) staff       (20)     4115 2023-01-20 20:44:12.000000 octodns-ns1-0.0.3/README.md
-drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-01-24 18:11:41.759846 octodns-ns1-0.0.3/octodns_ns1/
--rw-r--r--   0 ross       (501) staff       (20)    59019 2023-01-24 18:11:28.000000 octodns-ns1-0.0.3/octodns_ns1/__init__.py
-drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-01-24 18:11:41.762889 octodns-ns1-0.0.3/octodns_ns1.egg-info/
--rw-r--r--   0 ross       (501) staff       (20)     4428 2023-01-24 18:11:41.000000 octodns-ns1-0.0.3/octodns_ns1.egg-info/PKG-INFO
--rw-r--r--   0 ross       (501) staff       (20)      216 2023-01-24 18:11:41.000000 octodns-ns1-0.0.3/octodns_ns1.egg-info/SOURCES.txt
--rw-r--r--   0 ross       (501) staff       (20)        1 2023-01-24 18:11:41.000000 octodns-ns1-0.0.3/octodns_ns1.egg-info/dependency_links.txt
--rw-r--r--   0 ross       (501) staff       (20)      240 2023-01-24 18:11:41.000000 octodns-ns1-0.0.3/octodns_ns1.egg-info/requires.txt
--rw-r--r--   0 ross       (501) staff       (20)       12 2023-01-24 18:11:41.000000 octodns-ns1-0.0.3/octodns_ns1.egg-info/top_level.txt
--rw-r--r--   0 ross       (501) staff       (20)       38 2023-01-24 18:11:41.764419 octodns-ns1-0.0.3/setup.cfg
--rw-r--r--   0 ross       (501) staff       (20)     1784 2023-01-24 18:07:27.000000 octodns-ns1-0.0.3/setup.py
+drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-04-06 23:32:51.501676 octodns-ns1-0.0.4/
+-rw-r--r--   0 ross       (501) staff       (20)     4428 2023-04-06 23:32:51.501403 octodns-ns1-0.0.4/PKG-INFO
+-rw-r--r--   0 ross       (501) staff       (20)     4115 2023-04-06 18:12:34.000000 octodns-ns1-0.0.4/README.md
+drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-04-06 23:32:51.498350 octodns-ns1-0.0.4/octodns_ns1/
+-rw-r--r--   0 ross       (501) staff       (20)    58598 2023-04-06 23:32:37.000000 octodns-ns1-0.0.4/octodns_ns1/__init__.py
+drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-04-06 23:32:51.500595 octodns-ns1-0.0.4/octodns_ns1.egg-info/
+-rw-r--r--   0 ross       (501) staff       (20)     4428 2023-04-06 23:32:51.000000 octodns-ns1-0.0.4/octodns_ns1.egg-info/PKG-INFO
+-rw-r--r--   0 ross       (501) staff       (20)      258 2023-04-06 23:32:51.000000 octodns-ns1-0.0.4/octodns_ns1.egg-info/SOURCES.txt
+-rw-r--r--   0 ross       (501) staff       (20)        1 2023-04-06 23:32:51.000000 octodns-ns1-0.0.4/octodns_ns1.egg-info/dependency_links.txt
+-rw-r--r--   0 ross       (501) staff       (20)      254 2023-04-06 23:32:51.000000 octodns-ns1-0.0.4/octodns_ns1.egg-info/requires.txt
+-rw-r--r--   0 ross       (501) staff       (20)       12 2023-04-06 23:32:51.000000 octodns-ns1-0.0.4/octodns_ns1.egg-info/top_level.txt
+-rw-r--r--   0 ross       (501) staff       (20)      304 2023-02-04 19:09:21.000000 octodns-ns1-0.0.4/pyproject.toml
+-rw-r--r--   0 ross       (501) staff       (20)       38 2023-04-06 23:32:51.501763 octodns-ns1-0.0.4/setup.cfg
+-rw-r--r--   0 ross       (501) staff       (20)     1814 2023-02-04 19:09:21.000000 octodns-ns1-0.0.4/setup.py
+drwxr-xr-x   0 ross       (501) staff       (20)        0 2023-04-06 23:32:51.500899 octodns-ns1-0.0.4/tests/
+-rw-r--r--   0 ross       (501) staff       (20)   105009 2023-04-06 18:41:05.000000 octodns-ns1-0.0.4/tests/test_provider_ns1.py
```

### Comparing `octodns-ns1-0.0.3/PKG-INFO` & `octodns-ns1-0.0.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: octodns-ns1
-Version: 0.0.3
+Version: 0.0.4
 Summary:  NS1 provider for octoDNS
 Home-page: https://github.com/octodns/octodns-ns1
 Author: Ross McFarland
 Author-email: rwmcfa1@gmail.com
 License: MIT
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `octodns-ns1-0.0.3/README.md` & `octodns-ns1-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `octodns-ns1-0.0.3/octodns_ns1/__init__.py` & `octodns-ns1-0.0.4/octodns_ns1/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,26 +2,27 @@
 #
 #
 
 from collections import OrderedDict, defaultdict
 from collections.abc import Mapping
 from itertools import chain
 from logging import getLogger
+from time import sleep
+from uuid import uuid4
+
 from ns1 import NS1
 from ns1.rest.errors import RateLimitException, ResourceException
 from pycountry_convert import country_alpha2_to_continent_code
-from time import sleep
-from uuid import uuid4
 
 from octodns.provider import ProviderException
 from octodns.provider.base import BaseProvider
 from octodns.record import Record, Update
+from octodns.record.geo_data import geo_data
 
-
-__VERSION__ = '0.0.3'
+__VERSION__ = '0.0.4'
 
 
 def _ensure_endswith_dot(string):
     return string if string.endswith('.') else f'{string}.'
 
 
 class Ns1Exception(ProviderException):
@@ -375,16 +376,16 @@
             self._SELECT_FIRST_N_FILTER,
         ]
 
     @property
     def _FILTER_CHAIN_WITH_REGION_AND_COUNTRY(self):
         return [
             self._UP_FILTER,
-            self._REGION_FILTER,
             self._COUNTRY_FILTER,
+            self._REGION_FILTER,
             self._SELECT_FIRST_REGION_FILTER,
             self._PRIORITY_FILTER,
             self._WEIGHTED_SHUFFLE_FILTER,
             self._SELECT_FIRST_N_FILTER,
         ]
 
     _REGION_TO_CONTINENT = {
@@ -397,92 +398,23 @@
         # exist here so it doesn't break the ugrade path
         'US-CENTRAL': 'NA',
         'US-EAST': 'NA',
         'US-WEST': 'NA',
     }
     _CONTINENT_TO_REGIONS = {
         'AF': ('AFRICA',),
-        'AS': ('ASIAPAC',),
         'EU': ('EUROPE',),
         'SA': ('SOUTH-AMERICA',),
     }
 
     # Necessary for handling unsupported continents in _CONTINENT_TO_REGIONS
     _CONTINENT_TO_LIST_OF_COUNTRIES = {
-        'OC': {
-            'FJ',
-            'NC',
-            'PG',
-            'SB',
-            'VU',
-            'AU',
-            'NF',
-            'NZ',
-            'FM',
-            'GU',
-            'KI',
-            'MH',
-            'MP',
-            'NR',
-            'PW',
-            'AS',
-            'CK',
-            'NU',
-            'PF',
-            'PN',
-            'TK',
-            'TO',
-            'TV',
-            'WF',
-            'WS',
-        },
-        'NA': {
-            'DO',
-            'DM',
-            'BB',
-            'BL',
-            'BM',
-            'HT',
-            'KN',
-            'JM',
-            'VC',
-            'HN',
-            'BS',
-            'BZ',
-            'PR',
-            'NI',
-            'LC',
-            'TT',
-            'VG',
-            'PA',
-            'TC',
-            'PM',
-            'GT',
-            'AG',
-            'GP',
-            'AI',
-            'VI',
-            'CA',
-            'GD',
-            'AW',
-            'CR',
-            'GL',
-            'CU',
-            'MF',
-            'SV',
-            'US',
-            'MQ',
-            'MS',
-            'KY',
-            'MX',
-            'CW',
-            'BQ',
-            'SX',
-            'UM',
-        },
+        'AS': set(geo_data['AS'].keys()),
+        'OC': set(geo_data['OC'].keys()),
+        'NA': set(geo_data['NA'].keys()),
     }
 
     def __init__(
         self,
         id,
         api_key,
         retry_count=4,
@@ -546,17 +478,21 @@
 
     def _parse_notes(self, note):
         data = {}
         if note:
             for piece in note.split(' '):
                 try:
                     k, v = piece.split(':', 1)
-                    data[k] = v if v != '' else None
+                except ValueError:
+                    continue
+                try:
+                    v = int(v)
                 except ValueError:
                     pass
+                data[k] = v if v != '' else None
         return data
 
     def _data_for_geo_A(self, _type, record):
         # record meta (which would include geo information is only
         # returned when getting a record's detail, not from zone detail
         geo = defaultdict(list)
         data = {'ttl': record['ttl'], 'type': _type}
@@ -680,18 +616,20 @@
         continents_from_notes = set(notes.get('continents', '').split(','))
 
         special_continents = dict()
         for country in meta.get('country', []):
             # country_alpha2_to_continent_code fails for Pitcairn ('PN'),
             # United States Minor Outlying Islands ('UM') and
             # Sint Maarten ('SX')
-            if country == 'PN':
-                con = 'OC'
-            elif country in ['SX', 'UM']:
+            if country == 'TL':
+                con = 'AS'
+            elif country == 'SX':
                 con = 'NA'
+            elif country in ('PN', 'UM'):
+                con = 'OC'
             else:
                 con = country_alpha2_to_continent_code(country)
 
             if con in self._CONTINENT_TO_LIST_OF_COUNTRIES:
                 special_continents.setdefault(con, set()).add(country)
             else:
                 geos.add(f'{con}-{country}')
@@ -1193,15 +1131,22 @@
 
         return ret
 
     def _monitor_is_match(self, expected, have):
         # Make sure what we have matches what's in expected exactly. Anything
         # else in have will be ignored.
         for k, v in expected.items():
-            if have.get(k, '--missing--') != v:
+            if k == 'config':
+                # config is a nested dict and we need to only consider keys in
+                # expected for it as well
+                have_config = have.get(k, {})
+                for k, v in v.items():
+                    if have_config.get(k, '--missing--') != v:
+                        return False
+            elif have.get(k, '--missing--') != v:
                 return False
 
         return True
 
     def _monitor_sync(self, record, value, existing):
         self.log.debug('_monitor_sync: record=%s, value=%s', record.fqdn, value)
         expected = self._monitor_gen(record, value)
@@ -1495,18 +1440,23 @@
             'regions': regions,
             'ttl': record.ttl,
         }, active_monitors
 
     def _params_for_A(self, record):
         if getattr(record, 'dynamic', False):
             return self._params_for_dynamic(record)
-        elif hasattr(record, 'geo'):
+        elif getattr(record, 'geo', False):
             return self._params_for_geo_A(record)
 
-        return {'answers': record.values, 'ttl': record.ttl}, None
+        return {
+            'answers': record.values,
+            'ttl': record.ttl,
+            'filters': [],
+            'regions': {},
+        }, None
 
     _params_for_AAAA = _params_for_A
     _params_for_NS = _params_for_A
 
     def _params_for_SPF(self, record):
         # NS1 seems to be the only provider that doesn't want things
         # escaped in values so we have to strip them here and add
@@ -1520,15 +1470,20 @@
         values = [(v.flags, v.tag, v.value) for v in record.values]
         return {'answers': values, 'ttl': record.ttl}, None
 
     def _params_for_CNAME(self, record):
         if getattr(record, 'dynamic', False):
             return self._params_for_dynamic(record)
 
-        return {'answers': [record.value], 'ttl': record.ttl}, None
+        return {
+            'answers': [record.value],
+            'ttl': record.ttl,
+            'filters': [],
+            'regions': {},
+        }, None
 
     _params_for_ALIAS = _params_for_CNAME
 
     def _params_for_MX(self, record):
         values = [(v.preference, v.exchange) for v in record.values]
         return {'answers': values, 'ttl': record.ttl}, None
```

### Comparing `octodns-ns1-0.0.3/octodns_ns1.egg-info/PKG-INFO` & `octodns-ns1-0.0.4/octodns_ns1.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: octodns-ns1
-Version: 0.0.3
+Version: 0.0.4
 Summary:  NS1 provider for octoDNS
 Home-page: https://github.com/octodns/octodns-ns1
 Author: Ross McFarland
 Author-email: rwmcfa1@gmail.com
 License: MIT
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `octodns-ns1-0.0.3/setup.py` & `octodns-ns1-0.0.4/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 from os import environ
-from setuptools import find_packages, setup
 from subprocess import CalledProcessError, check_output
 
+from setuptools import find_packages, setup
+
 
 def descriptions():
     with open('README.md') as fh:
         ret = fh.read()
         first = ret.split('\n', 1)[0].replace('#', '')
         return first, ret
 
@@ -39,14 +40,15 @@
     author_email='rwmcfa1@gmail.com',
     description=description,
     extras_require={
         'dev': tests_require
         + (
             'black>=22.3.0',
             'build>=0.7.0',
+            'isort>=5.11.4',
             'pyflakes>=2.2.0',
             'readme_renderer[md]>=26.0',
             'twine>=3.4.2',
         ),
         'test': tests_require,
     },
     install_requires=(
```

