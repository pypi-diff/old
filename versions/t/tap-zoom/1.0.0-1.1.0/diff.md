# Comparing `tmp/tap-zoom-1.0.0.tar.gz` & `tmp/tap-zoom-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tap-zoom-1.0.0.tar", last modified: Mon Mar 15 19:06:29 2021, max compression
+gzip compressed data, was "tap-zoom-1.1.0.tar", last modified: Thu Apr  6 12:57:11 2023, max compression
```

## Comparing `tap-zoom-1.0.0.tar` & `tap-zoom-1.1.0.tar`

### file list

```diff
@@ -1,40 +1,41 @@
-drwxr-xr-x   0 aerlich    (503) staff       (20)        0 2021-03-15 19:06:29.422365 tap-zoom-1.0.0/
--rw-r--r--   0 aerlich    (503) staff       (20)      282 2021-03-15 19:06:29.421522 tap-zoom-1.0.0/PKG-INFO
--rw-r--r--   0 aerlich    (503) staff       (20)     3858 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/README.md
--rw-r--r--   0 aerlich    (503) staff       (20)       38 2021-03-15 19:06:29.422537 tap-zoom-1.0.0/setup.cfg
--rw-r--r--   0 aerlich    (503) staff       (20)      616 2021-03-15 19:06:14.000000 tap-zoom-1.0.0/setup.py
-drwxr-xr-x   0 aerlich    (503) staff       (20)        0 2021-03-15 19:06:29.401863 tap-zoom-1.0.0/tap_zoom/
--rw-r--r--   0 aerlich    (503) staff       (20)      987 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/__init__.py
--rw-r--r--   0 aerlich    (503) staff       (20)     4339 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/client.py
--rw-r--r--   0 aerlich    (503) staff       (20)     2191 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/discover.py
--rw-r--r--   0 aerlich    (503) staff       (20)     6581 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/endpoints.py
-drwxr-xr-x   0 aerlich    (503) staff       (20)        0 2021-03-15 19:06:29.420190 tap-zoom-1.0.0/tap_zoom/schemas/
--rw-r--r--   0 aerlich    (503) staff       (20)      400 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meeting_files.json
--rw-r--r--   0 aerlich    (503) staff       (20)      757 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meeting_poll_results.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1039 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meeting_polls.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1414 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meeting_questions.json
--rw-r--r--   0 aerlich    (503) staff       (20)     2272 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meeting_registrants.json
--rw-r--r--   0 aerlich    (503) staff       (20)     7940 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/meetings.json
--rw-r--r--   0 aerlich    (503) staff       (20)      739 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/report_meeting_participants.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1623 2021-03-15 18:03:44.000000 tap-zoom-1.0.0/tap_zoom/schemas/report_meetings.json
--rw-r--r--   0 aerlich    (503) staff       (20)      832 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/report_webinar_participants.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1785 2021-03-15 18:03:44.000000 tap-zoom-1.0.0/tap_zoom/schemas/report_webinars.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1500 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/users.json
--rw-r--r--   0 aerlich    (503) staff       (20)     2274 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_absentees.json
--rw-r--r--   0 aerlich    (503) staff       (20)      400 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_files.json
--rw-r--r--   0 aerlich    (503) staff       (20)      444 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_panelists.json
--rw-r--r--   0 aerlich    (503) staff       (20)      757 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_poll_results.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1039 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_polls.json
--rw-r--r--   0 aerlich    (503) staff       (20)      757 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_qna_results.json
--rw-r--r--   0 aerlich    (503) staff       (20)     1414 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_questions.json
--rw-r--r--   0 aerlich    (503) staff       (20)     2272 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_registrants.json
--rw-r--r--   0 aerlich    (503) staff       (20)      557 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinar_tracking_sources.json
--rw-r--r--   0 aerlich    (503) staff       (20)     6714 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/schemas/webinars.json
--rw-r--r--   0 aerlich    (503) staff       (20)     5340 2021-03-09 20:02:24.000000 tap-zoom-1.0.0/tap_zoom/sync.py
-drwxr-xr-x   0 aerlich    (503) staff       (20)        0 2021-03-15 19:06:29.404850 tap-zoom-1.0.0/tap_zoom.egg-info/
--rw-r--r--   0 aerlich    (503) staff       (20)      282 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/PKG-INFO
--rw-r--r--   0 aerlich    (503) staff       (20)     1141 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/SOURCES.txt
--rw-r--r--   0 aerlich    (503) staff       (20)        1 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/dependency_links.txt
--rw-r--r--   0 aerlich    (503) staff       (20)       68 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/entry_points.txt
--rw-r--r--   0 aerlich    (503) staff       (20)       70 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/requires.txt
--rw-r--r--   0 aerlich    (503) staff       (20)        9 2021-03-15 19:06:29.000000 tap-zoom-1.0.0/tap_zoom.egg-info/top_level.txt
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 12:57:11.545752 tap-zoom-1.1.0/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    34522 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/LICENSE
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      282 2023-04-06 12:57:11.545752 tap-zoom-1.1.0/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3858 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/README.md
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-04-06 12:57:11.545752 tap-zoom-1.1.0/setup.cfg
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      617 2023-04-06 12:56:04.000000 tap-zoom-1.1.0/setup.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 12:57:11.541752 tap-zoom-1.1.0/tap_zoom/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      987 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4339 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/client.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2531 2023-04-06 12:56:04.000000 tap-zoom-1.1.0/tap_zoom/discover.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8021 2023-04-06 12:56:04.000000 tap-zoom-1.1.0/tap_zoom/endpoints.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 12:57:11.545752 tap-zoom-1.1.0/tap_zoom/schemas/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      400 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meeting_files.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      757 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meeting_poll_results.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1039 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meeting_polls.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1414 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meeting_questions.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2272 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meeting_registrants.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7940 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/meetings.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      739 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/report_meeting_participants.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1623 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/report_meetings.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      832 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/report_webinar_participants.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1785 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/report_webinars.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1500 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/users.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2274 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_absentees.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      400 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_files.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      444 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_panelists.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      757 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_poll_results.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1039 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_polls.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      757 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_qna_results.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1414 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_questions.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2272 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_registrants.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      557 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinar_tracking_sources.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6714 2023-03-17 17:28:32.000000 tap-zoom-1.1.0/tap_zoom/schemas/webinars.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5406 2023-04-06 12:56:04.000000 tap-zoom-1.1.0/tap_zoom/sync.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 12:57:11.541752 tap-zoom-1.1.0/tap_zoom.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      282 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1149 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       68 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/entry_points.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       71 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        9 2023-04-06 12:57:11.000000 tap-zoom-1.1.0/tap_zoom.egg-info/top_level.txt
```

### Comparing `tap-zoom-1.0.0/README.md` & `tap-zoom-1.1.0/README.md`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/setup.py` & `tap-zoom-1.1.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 #!/usr/bin/env python
 
 from setuptools import setup
 
 setup(name='tap-zoom',
-      version='1.0.0',
+      version='1.1.0',
       description='Singer.io tap for extracting data from the Zoom API',
       classifiers=['Programming Language :: Python :: 3 :: Only'],
       py_modules=['tap_zoom'],
       install_requires=[
         'backoff==1.8.0',
         'ratelimit==2.2.1',
         'requests==2.23.0',
-        'singer-python==5.9.0'
+        'singer-python==5.13.0'
       ],
       entry_points='''
           [console_scripts]
           tap-zoom=tap_zoom:main
       ''',
       packages=['tap_zoom'],
       package_data = {
```

### Comparing `tap-zoom-1.0.0/tap_zoom/__init__.py` & `tap-zoom-1.1.0/tap_zoom/__init__.py`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/client.py` & `tap-zoom-1.1.0/tap_zoom/client.py`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/discover.py` & `tap-zoom-1.1.0/tap_zoom/discover.py`

 * *Files 16% similar despite different names*

```diff
@@ -4,24 +4,24 @@
 from singer.catalog import Catalog, CatalogEntry, Schema
 
 from tap_zoom.endpoints import ENDPOINTS_CONFIG
 
 SCHEMAS = {}
 FIELD_METADATA = {}
 
-def get_pk(stream_name, endpoints=None):
+def get_field_value(stream_name, field_name, endpoints=None):
     if not endpoints:
         endpoints = ENDPOINTS_CONFIG
 
     for endpoint_stream_name, endpoint in endpoints.items():
         if stream_name == endpoint_stream_name:
-            return endpoint['pk']
+            return endpoint[field_name]
 
         if 'children' in endpoint:
-            pk = get_pk(stream_name, endpoints=endpoint['children'])
+            pk = get_field_value(stream_name, field_name, endpoints=endpoint['children'])
             if pk:
                 return pk
 
 def get_abs_path(path):
     return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
 
 def get_schemas():
@@ -38,17 +38,21 @@
     for file_name in file_names:
         stream_name = file_name[:-5]
         with open(os.path.join(schemas_path, file_name)) as data_file:
             schema = json.load(data_file)
             
         SCHEMAS[stream_name] = schema
 
-        pk = get_pk(stream_name)
+        pk = get_field_value(stream_name, 'pk')
+        repl_method = get_field_value(stream_name, 'forced-replication-method')
 
-        metadata = []
+        mdata = {"table-key-properties": pk,
+                "forced-replication-method": repl_method,
+                "inclusion": "available"}
+        metadata = [{"breadcrumb": [], "metadata": mdata}]
         for prop, json_schema in schema['properties'].items():
             if prop in pk:
                 inclusion = 'automatic'
             else:
                 inclusion = 'available'
             metadata.append({
                 'metadata': {
@@ -62,15 +66,15 @@
 
 def discover():
     schemas, field_metadata = get_schemas()
     catalog = Catalog([])
 
     for stream_name, schema_dict in schemas.items():
         schema = Schema.from_dict(schema_dict)
-        pk = get_pk(stream_name)
+        pk = get_field_value(stream_name, 'pk')
         metadata = field_metadata[stream_name]
 
         catalog.streams.append(CatalogEntry(
             stream=stream_name,
             tap_stream_id=stream_name,
             key_properties=pk,
             schema=schema,
```

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/meeting_poll_results.json` & `tap-zoom-1.1.0/tap_zoom/schemas/meeting_poll_results.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/meeting_polls.json` & `tap-zoom-1.1.0/tap_zoom/schemas/meeting_polls.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/meeting_questions.json` & `tap-zoom-1.1.0/tap_zoom/schemas/meeting_questions.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/meeting_registrants.json` & `tap-zoom-1.1.0/tap_zoom/schemas/meeting_registrants.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/meetings.json` & `tap-zoom-1.1.0/tap_zoom/schemas/meetings.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/report_meeting_participants.json` & `tap-zoom-1.1.0/tap_zoom/schemas/report_meeting_participants.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/report_meetings.json` & `tap-zoom-1.1.0/tap_zoom/schemas/report_meetings.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/report_webinar_participants.json` & `tap-zoom-1.1.0/tap_zoom/schemas/report_webinar_participants.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/report_webinars.json` & `tap-zoom-1.1.0/tap_zoom/schemas/report_webinars.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/users.json` & `tap-zoom-1.1.0/tap_zoom/schemas/users.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_absentees.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_absentees.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_poll_results.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_poll_results.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_polls.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_polls.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_qna_results.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_qna_results.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_questions.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_questions.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_registrants.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_registrants.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinar_tracking_sources.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinar_tracking_sources.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/schemas/webinars.json` & `tap-zoom-1.1.0/tap_zoom/schemas/webinars.json`

 * *Files identical despite different names*

### Comparing `tap-zoom-1.0.0/tap_zoom/sync.py` & `tap-zoom-1.1.0/tap_zoom/sync.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,15 +32,14 @@
                   key_bag):
     persist = endpoint.get('persist', True)
 
     if persist:
         stream = catalog.get_stream(stream_name)
         schema = stream.schema.to_dict()
         mdata = metadata.to_map(stream.metadata)
-        write_schema(stream)
 
     path = endpoint['path'].format(**key_bag)
 
     page_size = 1000
     page_number = 1
     while True:
         params = {
@@ -118,15 +117,16 @@
         selected_streams = catalog.streams
     else:
         selected_streams = catalog.get_selected_streams(state)
 
     selected_stream_names = []
     for selected_stream in selected_streams:
         selected_stream_names.append(selected_stream.tap_stream_id)
-
+        stream = catalog.get_stream(selected_stream.tap_stream_id)
+        write_schema(stream)
     required_streams = get_required_streams(ENDPOINTS_CONFIG, selected_stream_names)
 
     for stream_name, endpoint in ENDPOINTS_CONFIG.items():
         if stream_name in required_streams:
             update_current_stream(state, stream_name)
             sync_endpoint(client,
                           catalog,
```

### Comparing `tap-zoom-1.0.0/tap_zoom.egg-info/SOURCES.txt` & `tap-zoom-1.1.0/tap_zoom.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+LICENSE
 README.md
 setup.py
 tap_zoom/__init__.py
 tap_zoom/client.py
 tap_zoom/discover.py
 tap_zoom/endpoints.py
 tap_zoom/sync.py
```

