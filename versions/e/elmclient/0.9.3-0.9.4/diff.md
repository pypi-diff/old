# Comparing `tmp/elmclient-0.9.3.tar.gz` & `tmp/elmclient-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "elmclient-0.9.3.tar", last modified: Tue Sep  6 08:48:58 2022, max compression
+gzip compressed data, was "elmclient-0.9.4.tar", last modified: Tue Sep 20 11:57:35 2022, max compression
```

## Comparing `elmclient-0.9.3.tar` & `elmclient-0.9.4.tar`

### file list

```diff
@@ -1,52 +1,52 @@
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.420744 elmclient-0.9.3/
--rw-rw-rw-   0        0        0     1224 2022-07-06 10:21:20.000000 elmclient-0.9.3/LICENSE
--rw-rw-rw-   0        0        0      124 2022-07-06 10:21:20.000000 elmclient-0.9.3/MANIFEST.in
--rw-rw-rw-   0        0        0     9514 2022-09-06 08:48:58.420744 elmclient-0.9.3/PKG-INFO
--rw-rw-rw-   0        0        0     9021 2022-09-06 08:48:46.000000 elmclient-0.9.3/README.md
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.177785 elmclient-0.9.3/elmclient/
--rw-rw-rw-   0        0        0      543 2022-08-01 15:47:09.000000 elmclient-0.9.3/elmclient/__init__.py
--rw-rw-rw-   0        0        0      471 2022-09-06 08:48:46.000000 elmclient-0.9.3/elmclient/__meta__.py
--rw-rw-rw-   0        0        0    15843 2022-08-01 15:45:00.000000 elmclient-0.9.3/elmclient/_app.py
--rw-rw-rw-   0        0        0    21863 2022-03-16 13:15:17.000000 elmclient-0.9.3/elmclient/_ccm.py
--rw-rw-rw-   0        0        0     1914 2022-07-13 09:23:29.000000 elmclient-0.9.3/elmclient/_config.py
--rw-rw-rw-   0        0        0    35937 2022-07-07 16:17:09.000000 elmclient-0.9.3/elmclient/_gcm.py
--rw-rw-rw-   0        0        0    24154 2022-08-01 16:07:00.000000 elmclient-0.9.3/elmclient/_project.py
--rw-rw-rw-   0        0        0    31381 2022-03-16 13:12:56.000000 elmclient-0.9.3/elmclient/_qm.py
--rw-rw-rw-   0        0        0    25997 2022-08-01 14:31:06.000000 elmclient-0.9.3/elmclient/_queryparser.py
--rw-rw-rw-   0        0        0     2483 2022-05-13 16:26:50.000000 elmclient-0.9.3/elmclient/_relm.py
--rw-rw-rw-   0        0        0    59257 2022-07-13 09:23:18.000000 elmclient-0.9.3/elmclient/_rm.py
--rw-rw-rw-   0        0        0    57900 2022-02-22 08:42:55.000000 elmclient-0.9.3/elmclient/_rm1.py
--rw-rw-rw-   0        0        0    13288 2022-06-07 09:30:08.000000 elmclient-0.9.3/elmclient/_typesystem.py
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.384745 elmclient-0.9.3/elmclient/examples/
--rw-rw-rw-   0        0        0     1531 2021-12-01 09:35:01.000000 elmclient-0.9.3/elmclient/examples/DN_SIMPLE_MODULESTRUCTURE.md
--rw-rw-rw-   0        0        0    56862 2022-09-06 07:52:57.000000 elmclient-0.9.3/elmclient/examples/OSLCQUERY.md
--rw-rw-rw-   0        0        0    17003 2021-11-18 12:16:32.000000 elmclient-0.9.3/elmclient/examples/REPREST.md
--rw-rw-rw-   0        0        0    13982 2022-06-20 11:39:40.000000 elmclient-0.9.3/elmclient/examples/REQIF_IO.md
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.392799 elmclient-0.9.3/elmclient/examples/basic/
--rw-rw-rw-   0        0        0     9082 2021-10-06 07:58:47.000000 elmclient-0.9.3/elmclient/examples/basic/dn_basic_oslcquery.py
--rw-rw-rw-   0        0        0    10656 2022-07-13 11:30:56.000000 elmclient-0.9.3/elmclient/examples/batchquery.py
--rw-rw-rw-   0        0        0     3193 2022-03-16 13:32:33.000000 elmclient-0.9.3/elmclient/examples/ccm_simple_attachmentdownload.py
--rw-rw-rw-   0        0        0    25342 2022-04-27 11:33:14.000000 elmclient-0.9.3/elmclient/examples/dn_simple_modulestructure.py
--rw-rw-rw-   0        0        0     3776 2022-03-16 13:41:16.000000 elmclient-0.9.3/elmclient/examples/dn_simple_represt.py
--rw-rw-rw-   0        0        0     4842 2022-09-01 09:19:09.000000 elmclient-0.9.3/elmclient/examples/dn_simple_typesystemimport.py
--rw-rw-rw-   0        0        0    12338 2022-06-20 14:33:22.000000 elmclient-0.9.3/elmclient/examples/log2seq.py
--rw-rw-rw-   0        0        0    38850 2022-09-06 07:20:57.000000 elmclient-0.9.3/elmclient/examples/oslcquery.py
--rw-rw-rw-   0        0        0    21712 2022-03-17 08:33:13.000000 elmclient-0.9.3/elmclient/examples/represt.py
--rw-rw-rw-   0        0        0    47549 2022-09-01 12:25:04.000000 elmclient-0.9.3/elmclient/examples/reqif_io.py
--rw-rw-rw-   0        0        0    35712 2022-09-01 09:15:14.000000 elmclient-0.9.3/elmclient/httpops.py
--rw-rw-rw-   0        0        0    46832 2022-09-06 07:25:56.000000 elmclient-0.9.3/elmclient/oslcqueryapi.py
--rw-rw-rw-   0        0        0    14037 2022-06-16 13:20:54.000000 elmclient-0.9.3/elmclient/rdfxml.py
--rw-rw-rw-   0        0        0    14368 2022-08-23 14:41:18.000000 elmclient-0.9.3/elmclient/server.py
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.416804 elmclient-0.9.3/elmclient/tests/
--rw-rw-rw-   0        0        0    22052 2022-07-13 12:01:40.000000 elmclient-0.9.3/elmclient/tests/tests_6061.xlsx
--rw-rw-rw-   0        0        0    22070 2022-09-02 07:50:09.000000 elmclient-0.9.3/elmclient/tests/tests_702.xlsx
--rw-rw-rw-   0        0        0    11615 2022-06-21 07:28:03.000000 elmclient-0.9.3/elmclient/utils.py
-drwxrwxrwx   0        0        0        0 2022-09-06 08:48:58.226489 elmclient-0.9.3/elmclient.egg-info/
--rw-rw-rw-   0        0        0     9514 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1203 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      241 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      269 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2022-09-06 08:48:57.000000 elmclient-0.9.3/elmclient.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2022-09-06 08:48:58.420744 elmclient-0.9.3/setup.cfg
--rw-rw-rw-   0        0        0     1755 2022-09-06 08:48:46.000000 elmclient-0.9.3/setup.py
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.259662 elmclient-0.9.4/
+-rw-rw-rw-   0        0        0     1224 2022-07-06 10:21:20.000000 elmclient-0.9.4/LICENSE
+-rw-rw-rw-   0        0        0      124 2022-07-06 10:21:20.000000 elmclient-0.9.4/MANIFEST.in
+-rw-rw-rw-   0        0        0     9514 2022-09-20 11:57:35.258646 elmclient-0.9.4/PKG-INFO
+-rw-rw-rw-   0        0        0     9021 2022-09-20 11:54:12.000000 elmclient-0.9.4/README.md
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.114683 elmclient-0.9.4/elmclient/
+-rw-rw-rw-   0        0        0      543 2022-08-01 15:47:09.000000 elmclient-0.9.4/elmclient/__init__.py
+-rw-rw-rw-   0        0        0      471 2022-09-20 11:54:12.000000 elmclient-0.9.4/elmclient/__meta__.py
+-rw-rw-rw-   0        0        0    15843 2022-08-01 15:45:00.000000 elmclient-0.9.4/elmclient/_app.py
+-rw-rw-rw-   0        0        0    21863 2022-03-16 13:15:17.000000 elmclient-0.9.4/elmclient/_ccm.py
+-rw-rw-rw-   0        0        0     1914 2022-07-13 09:23:29.000000 elmclient-0.9.4/elmclient/_config.py
+-rw-rw-rw-   0        0        0    35937 2022-07-07 16:17:09.000000 elmclient-0.9.4/elmclient/_gcm.py
+-rw-rw-rw-   0        0        0    24154 2022-08-01 16:07:00.000000 elmclient-0.9.4/elmclient/_project.py
+-rw-rw-rw-   0        0        0    29806 2022-09-08 14:59:07.000000 elmclient-0.9.4/elmclient/_qm.py
+-rw-rw-rw-   0        0        0    25997 2022-08-01 14:31:06.000000 elmclient-0.9.4/elmclient/_queryparser.py
+-rw-rw-rw-   0        0        0     2483 2022-05-13 16:26:50.000000 elmclient-0.9.4/elmclient/_relm.py
+-rw-rw-rw-   0        0        0    59257 2022-07-13 09:23:18.000000 elmclient-0.9.4/elmclient/_rm.py
+-rw-rw-rw-   0        0        0    57900 2022-02-22 08:42:55.000000 elmclient-0.9.4/elmclient/_rm1.py
+-rw-rw-rw-   0        0        0    13288 2022-06-07 09:30:08.000000 elmclient-0.9.4/elmclient/_typesystem.py
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.233647 elmclient-0.9.4/elmclient/examples/
+-rw-rw-rw-   0        0        0     1531 2021-12-01 09:35:01.000000 elmclient-0.9.4/elmclient/examples/DN_SIMPLE_MODULESTRUCTURE.md
+-rw-rw-rw-   0        0        0    56862 2022-09-06 07:52:57.000000 elmclient-0.9.4/elmclient/examples/OSLCQUERY.md
+-rw-rw-rw-   0        0        0    17003 2021-11-18 12:16:32.000000 elmclient-0.9.4/elmclient/examples/REPREST.md
+-rw-rw-rw-   0        0        0    14764 2022-09-09 15:33:11.000000 elmclient-0.9.4/elmclient/examples/REQIF_IO.md
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.242645 elmclient-0.9.4/elmclient/examples/basic/
+-rw-rw-rw-   0        0        0     9082 2021-10-06 07:58:47.000000 elmclient-0.9.4/elmclient/examples/basic/dn_basic_oslcquery.py
+-rw-rw-rw-   0        0        0    10656 2022-07-13 11:30:56.000000 elmclient-0.9.4/elmclient/examples/batchquery.py
+-rw-rw-rw-   0        0        0     3193 2022-03-16 13:32:33.000000 elmclient-0.9.4/elmclient/examples/ccm_simple_attachmentdownload.py
+-rw-rw-rw-   0        0        0    25342 2022-04-27 11:33:14.000000 elmclient-0.9.4/elmclient/examples/dn_simple_modulestructure.py
+-rw-rw-rw-   0        0        0     3776 2022-03-16 13:41:16.000000 elmclient-0.9.4/elmclient/examples/dn_simple_represt.py
+-rw-rw-rw-   0        0        0     4842 2022-09-01 09:19:09.000000 elmclient-0.9.4/elmclient/examples/dn_simple_typesystemimport.py
+-rw-rw-rw-   0        0        0    12338 2022-06-20 14:33:22.000000 elmclient-0.9.4/elmclient/examples/log2seq.py
+-rw-rw-rw-   0        0        0    40913 2022-09-09 09:24:12.000000 elmclient-0.9.4/elmclient/examples/oslcquery.py
+-rw-rw-rw-   0        0        0    21712 2022-03-17 08:33:13.000000 elmclient-0.9.4/elmclient/examples/represt.py
+-rw-rw-rw-   0        0        0    47561 2022-09-09 15:38:05.000000 elmclient-0.9.4/elmclient/examples/reqif_io.py
+-rw-rw-rw-   0        0        0    35712 2022-09-01 09:15:14.000000 elmclient-0.9.4/elmclient/httpops.py
+-rw-rw-rw-   0        0        0    48086 2022-09-09 15:26:40.000000 elmclient-0.9.4/elmclient/oslcqueryapi.py
+-rw-rw-rw-   0        0        0    14037 2022-06-16 13:20:54.000000 elmclient-0.9.4/elmclient/rdfxml.py
+-rw-rw-rw-   0        0        0    14368 2022-08-23 14:41:18.000000 elmclient-0.9.4/elmclient/server.py
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.256657 elmclient-0.9.4/elmclient/tests/
+-rw-rw-rw-   0        0        0    22052 2022-07-13 12:01:40.000000 elmclient-0.9.4/elmclient/tests/tests_6061.xlsx
+-rw-rw-rw-   0        0        0    22070 2022-09-02 07:50:09.000000 elmclient-0.9.4/elmclient/tests/tests_702.xlsx
+-rw-rw-rw-   0        0        0    11615 2022-06-21 07:28:03.000000 elmclient-0.9.4/elmclient/utils.py
+drwxrwxrwx   0        0        0        0 2022-09-20 11:57:35.135679 elmclient-0.9.4/elmclient.egg-info/
+-rw-rw-rw-   0        0        0     9514 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1203 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      241 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      269 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2022-09-20 11:57:34.000000 elmclient-0.9.4/elmclient.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2022-09-20 11:57:35.259662 elmclient-0.9.4/setup.cfg
+-rw-rw-rw-   0        0        0     1755 2022-09-20 11:56:30.000000 elmclient-0.9.4/setup.py
```

### Comparing `elmclient-0.9.3/LICENSE` & `elmclient-0.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/PKG-INFO` & `elmclient-0.9.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: elmclient
-Version: 0.9.3
+Version: 0.9.4
 Summary: Python client for ELM with examples of OSLC Query, ReqIF import/export, Reportable REST, and more
 Home-page: https://github.com/IBM/ELM-Python-Client
 Author: Ian Barnard
 License: MIT
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -18,15 +18,15 @@
  Python client for IBM Enterprise Lifecycle Management applications
 
 
  (c) Copyright 2021- IBM Inc. All rights reserved
  
  SPDX-License-Identifier: MIT
 
- version="0.9.3"
+ version="0.9.4"
 
 
 Introduction
 ============
 
 The aim of this code is to provide a Python client for the IBM Enterprise Lifecycle Management (ELM) applications.
```

### Comparing `elmclient-0.9.3/README.md` & `elmclient-0.9.4/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
  Python client for IBM Enterprise Lifecycle Management applications
 
 
  (c) Copyright 2021- IBM Inc. All rights reserved
  
  SPDX-License-Identifier: MIT
 
- version="0.9.3"
+ version="0.9.4"
 
 
 Introduction
 ============
 
 The aim of this code is to provide a Python client for the IBM Enterprise Lifecycle Management (ELM) applications.
```

### Comparing `elmclient-0.9.3/elmclient/__init__.py` & `elmclient-0.9.4/elmclient/__init__.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_app.py` & `elmclient-0.9.4/elmclient/_app.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_ccm.py` & `elmclient-0.9.4/elmclient/_ccm.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_config.py` & `elmclient-0.9.4/elmclient/_config.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_gcm.py` & `elmclient-0.9.4/elmclient/_gcm.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_project.py` & `elmclient-0.9.4/elmclient/_project.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_qm.py` & `elmclient-0.9.4/elmclient/_qm.py`

 * *Files 7% similar despite different names*

```diff
@@ -46,39 +46,16 @@
             return
         self._components = {}
         self._configurations = {}
         ncomps = 0
         nconfs = 0
         # retrieve components and configurations for this project
         if not self.is_optin:
-            logger.debug( f"{self.is_optin=}" )
-            # get the default configuration
-            projx = self.execute_get_xml( self.reluri( 'rm-projects/' + self.iid ), intent="Retrieve the project definition (opt-out)" )
-            compsu = rdfxml.xmlrdf_get_resource_text( projx, './/jp06:components' )
-            compsx = self.execute_get_xml(compsu, intent="Retrieve the component definition (opt-out)" )
-            defaultcompu = rdfxml.xmlrdf_get_resource_uri( compsx, './/oslc_config:component' )
-            
-            # register the only component
-            ncomps += 1
-            self._components[defaultcompu] = {'name': self.name, 'configurations': {}}
-            thisconfu = defaultcompu+"/configurations"
-            configs = self.execute_get_json( thisconfu, intent="Retrieve all configurations (opt-out)" )
-            configdetails = configs[defaultcompu+"/configurations"]
-            if type(configs[thisconfu]["http://www.w3.org/2000/01/rdf-schema#member"])==dict:
-                confs = [configs[thisconfu]["http://www.w3.org/2000/01/rdf-schema#member"]]
-            else:
-                confs = configs[thisconfu]["http://www.w3.org/2000/01/rdf-schema#member"]
-            for aconf in confs:
-                confu = aconf['value']
-                confx = self.execute_get_xml( confu, intent="Retrieve configuration definition (opt-out)" )
-                conftitle = rdfxml.xmlrdf_get_resource_text(confx,'.//dcterms:title')
-                conftype = 'Stream' if 'stream' in confu else 'Baseline'
-                self._components[defaultcompu]['configurations'][confu] = {'name': conftitle, 'conftype': conftype, 'confXml': confx}
-                self._configurations[defaultcompu] = self._components[defaultcompu]['configurations'][confu]
-                nconfs += 1
+            # for QM, no configs to load!
+            return
         elif self.singlemode:
             logger.debug( f"{self.singlemode=}" )
             #get the single component from a QueryCapability
             # <oslc:QueryCapability>
             #    <oslc_config:component rdf:resource="https://mb02-calm.rtp.raleigh.ibm.com:9443/rm/cm/component/_ln_roBIOEeumc4tx0skHCA"/>
             #    <oslc:resourceType rdf:resource="http://jazz.net/ns/rm/dng/view#View"/>
             #    <oslc:queryBase rdf:resource="https://mb02-calm.rtp.raleigh.ibm.com:9443/rm/views_oslc/query?componentURI=https%3A%2F%2Fmb02-calm.rtp.raleigh.ibm.com%3A9443%2Frm%2Fcm%2Fcomponent%2F_ln_roBIOEeumc4tx0skHCA"/>
@@ -119,17 +96,19 @@
 #    <oslc:resourceShape rdf:resource="https://jazz.ibm.com:9443/qm/oslc_config/resourceShapes/com.ibm.team.vvc.Component"/>
 #    <dcterms:title rdf:parseType="Literal">Default query capability for Component</dcterms:title>
 #    <rdf:type rdf:resource="http://open-services.net/ns/core#QueryCapability"/>
 #  </rdf:Description>
 
             components_uri = rdfxml.xmlrdf_get_resource_uri(cmsp_xml, './/rdf:Description/rdf:type[@rdf:resource="http://open-services.net/ns/core#QueryCapability"]/../oslc:resourceType[@rdf:resource="http://open-services.net/ns/config#Component"]/../oslc:queryBase')
             logger.info( f"{components_uri=}" )
+            print( f"{components_uri=}" )
             # get all components
             crx = self.execute_get_xml( components_uri, intent="Retrieve component definition" )
-
+            logger.info( f"{crx=}" )
+            print( f"{crx=}" )
 #      <oslc_config:Component rdf:about="https://jazz.ibm.com:9443/qm/oslc_config/resources/com.ibm.team.vvc.Component/_iw4s4EB3Eeus6Zk4qsm_Cw">
 #        <dcterms:title rdf:parseType="Literal">SGC Agile</dcterms:title>
 #        <oslc:instanceShape rdf:resource="https://jazz.ibm.com:9443/qm/oslc_config/resourceShapes/com.ibm.team.vvc.Component"/>
 #        <dcterms:identifier>_iw4s4EB3Eeus6Zk4qsm_Cw</dcterms:identifier>
 #        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2020-12-17T14:52:54.318Z</dcterms:modified>
 #        <oslc_config:configurations rdf:resource="https://jazz.ibm.com:9443/qm/oslc_config/resources/com.ibm.team.vvc.Component/_iw4s4EB3Eeus6Zk4qsm_Cw/configurations"/>
 #        <acc:accessContext rdf:resource="https://jazz.ibm.com:9443/qm/acclist#_rikP0EB1Eeus6Zk4qsm_Cw"/>
@@ -222,19 +201,22 @@
     def get_local_component_details(self):
         results = {}
         for compuri, compdetail in self._components.items():
             results[compuri] = compdetail['name']
         return results
 
     def find_local_component(self, name_or_uri):
-        self.load_components_and_configurations()
-        for compuri, compdetail in self._components.items():
-            logger.info( f"Checking {name_or_uri} {compdetail}" )
-            if compuri == name_or_uri or compdetail['name'] == name_or_uri:
-                return compdetail['component']
+        if self.is_optin:
+            self.load_components_and_configurations()
+            for compuri, compdetail in self._components.items():
+                logger.info( f"Checking {name_or_uri} {compdetail}" )
+                if compuri == name_or_uri or compdetail['name'] == name_or_uri:
+                    return compdetail['component']
+        else:
+            return self
         return None
 
     def _create_component_api(self, component_prj_url, component_name):
         logger.info( f"CREATE QM COMPONENT {self=} {component_prj_url=} {component_name=} {self.app=} {self.is_optin=} {self.singlemode=}" )
         result = _QMComponent(component_name, component_prj_url, self.app, self.is_optin, self.singlemode, defaultinit=False, project=self)
         return result
```

### Comparing `elmclient-0.9.3/elmclient/_queryparser.py` & `elmclient-0.9.4/elmclient/_queryparser.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_relm.py` & `elmclient-0.9.4/elmclient/_relm.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_rm.py` & `elmclient-0.9.4/elmclient/_rm.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_rm1.py` & `elmclient-0.9.4/elmclient/_rm1.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/_typesystem.py` & `elmclient-0.9.4/elmclient/_typesystem.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/DN_SIMPLE_MODULESTRUCTURE.md` & `elmclient-0.9.4/elmclient/examples/DN_SIMPLE_MODULESTRUCTURE.md`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/OSLCQUERY.md` & `elmclient-0.9.4/elmclient/examples/OSLCQUERY.md`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/REPREST.md` & `elmclient-0.9.4/elmclient/examples/REPREST.md`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/REQIF_IO.md` & `elmclient-0.9.4/elmclient/examples/REQIF_IO.md`

 * *Files 3% similar despite different names*

```diff
@@ -22,14 +22,32 @@
 **IMPORTANT NOTE** ReqIF import and export are expensive operations on your server - you are responsible to manage the load these place on your server so as not to adversely affect the experience of other users or to jeopardise the server itself due to excessive load.
 
 Installation
 ============
 
 The `reqif_io` command is installed in your Python scripts folder when installing `elmclient`
 
+TLDR;
+=====
+
+Here's a sequence which lists definitions, creates a new definition for a specific module, exports it to reqifz, reimports the reqifz, and then deletes the definition
+
+NOTE this is so brief because it's using the defaults for server URL and context roots, username and password - see below these sections for how to set these up for your environment.
+NOTE this works when project `rm_optout_p1` was created using the `Systems Requirement Sample`, which has a module `AMR Stakeholder Specification`.
+
+
+```
+reqif_io rm_optout_p1 list
+reqif_io rm_optout_p1 create stk -m "AMR Stakeholder Requirements Specification"
+reqif_io rm_optout_p1 list
+reqif_io rm_optout_p1 export stk
+reqif_io rm_optout_p1 import stk.reqifz
+reqif_io rm_optout_p1 delete stk
+```
+
 
 Usage
 =====
 
 
 To get all the usage options use `reqif_io -h` or `reqif_io --help`:
```

### Comparing `elmclient-0.9.3/elmclient/examples/basic/dn_basic_oslcquery.py` & `elmclient-0.9.4/elmclient/examples/basic/dn_basic_oslcquery.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/batchquery.py` & `elmclient-0.9.4/elmclient/examples/batchquery.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/ccm_simple_attachmentdownload.py` & `elmclient-0.9.4/elmclient/examples/ccm_simple_attachmentdownload.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/dn_simple_modulestructure.py` & `elmclient-0.9.4/elmclient/examples/dn_simple_modulestructure.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/dn_simple_represt.py` & `elmclient-0.9.4/elmclient/examples/dn_simple_represt.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/dn_simple_typesystemimport.py` & `elmclient-0.9.4/elmclient/examples/dn_simple_typesystemimport.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/log2seq.py` & `elmclient-0.9.4/elmclient/examples/log2seq.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/oslcquery.py` & `elmclient-0.9.4/elmclient/examples/oslcquery.py`

 * *Files 4% similar despite different names*

```diff
@@ -101,14 +101,16 @@
 
     # various options
     parser.add_argument('--nresults', default=-1, type=int, help="Number of results expected - used for regression testing - use `--nresults -1` to disable checking")
     parser.add_argument('--compareresults', default=None, help="TESTING UNFINISHED: saved CSV file to compare results with")
     parser.add_argument('--pagesize', default=200, type=int, help="Page size for OSLC query (default 200)")
     parser.add_argument('--typesystemreport', default=None, help="Load the specified project/configuration and then produce a simple HTML type system report of resource shapes/properties/enumerations to this file" )
     parser.add_argument('--cachedays', default=1,type=int, help="The number of days for caching received data, default 1. To disable caching use -WW. To keep using a non-default cache period you must specify this value every time" )
+    parser.add_argument('--saverawresults', default=None, help="Save the raw results as XML to this path/file prefix - pages are numbered starting from 0000" )
+    parser.add_argument('--saveprocessedresults', default=None, help="Save the processed results as JSON to this path/file" )
 
     # saved credentials
     parser.add_argument('-0', '--savecreds', default=None, help="Save obfuscated credentials file for use with readcreds, then exit - this stores jazzurl, jts, appstring, username and password")
     parser.add_argument('-1', '--readcreds', default=None, help="Read obfuscated credentials from file - completely overrides commandline/environment values for jazzurl, jts, appstring, username and password" )
     parser.add_argument('-2', '--erasecreds', default=None, help="Wipe and delete obfuscated credentials file" )
     parser.add_argument('-3', '--secret', default="N0tSeCret-", help="SECRET used to encrypt and decrypt the obfuscated credentials (make this longer for greater security) - required if using -0 or -1" )
     parser.add_argument('-4', '--credspassword', action="store_true", help="Prompt user for a password to save/read obfuscated credentials (make this longer for greater security)" )
@@ -452,14 +454,15 @@
                     ,show_progress=args.noprogressbar
                     ,verbose=args.verbose
                     ,maxresults=args.maxresults
                     ,delaybetweenpages=args.delaybetweenpages
                     ,pagesize=args.pagesize
                     ,resolvenames = args.resolvenames
                     ,totalize=args.totalize
+                    ,saverawresults=args.saverawresults
                     )
 
     if args.debugprint:
         pp.pprint(results)
 
     # try to get a key as an integers - no exception if the string isn't an integer
     def safeint(s,nonereturns=0):
@@ -505,43 +508,68 @@
             if todelete in results.keys():
                 del results[todelete]
             else:
                 pass
 
     resultsentries = "entries" if len(results.keys())!=1 else "entry"
 
+    if args.saveprocessedresults:
+        open(args.saveprocessedresults+"_before.json","wt").write(json.dumps(results))
+        
     print( f"Query result has {len(results.keys())} {resultsentries}" )
 
-    # THIS IS UNTESTED!
+    # COMPARE IS UNTESTED!
     if args.outputfile or args.compareresults:
         # write to CSV and/or compare with CSV
+        # FIRST merge columns with same name - this merges types across components based on name
+        # which is only need for queries in a GC. NOTE this doesn't attempt to use RDF URIs which it probably should :-o
+        # but having different (as in totally different) types with same name is not exactly human-friendly!
         # build a list of all properties - these will be column headings for the CSV
         headings = []
+        rawheadings = [] # this is used so headings are only resolved once - the raw headings are remembered in this list
+        actualheadings = {}
         for k, v in list(results.items()):
             # add the URI to the value so it will be exported (first char is $ so the uri will always be in first column after the column titles are sorted)
             v["$uri"] = k
             for sk in list(v.keys()):
-                sk1 = queryon.resolve_uri_to_name(sk)
-                if sk1 is not None:
+                sk1 = queryon.resolve_uri_to_name(sk) if args.resolvenames else sk
+                if sk not in rawheadings:
+                    rawheadings.append(sk)
+                    if sk1 == sk: # if heading name hasn't been resolved before
+                        sk1 = queryon.resolve_uri_to_name(sk) # always resolve - only for headings
+                    if sk1 not in headings:
+                        headings.append(sk1)
+                    actualheadings[sk] = sk1
+#                    # also store the reverse actual->raw
+#                    actualheadings[sk1] = sk
+                    logger.info( f"Mapping {sk} to {sk1}" )
+                else:
+                    sk1 = actualheadings[sk]
+                if sk!=sk1:
                     logger.debug(f"renaming {sk=} {sk1=}" )
+                    # if ernaming need to merge column content!
                     existing = v[sk]
+                    otherexisting = v.get(sk1)
                     del v[sk]
-                    v[sk1] = existing
-                else:
-                    sk1 = sk
-                if sk1 not in headings:
-                    headings.append(sk1)
+                    if existing and otherexisting:
+                        if existing != otherexisting:
+                            logger.info( f"MERGE {existing=} {otherexisting=}" )
+                            burp
+                    v[sk1] = otherexisting if otherexisting else existing
 
         fieldnames = sorted(headings)
         if args.outputfile:
             with open(args.outputfile, 'w', newline='', encoding='utf-8-sig') as csvfile:
                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='')
                 writer.writeheader()
                 for k, v in results.items():
                     writer.writerow(v)
+                    
+        if args.saveprocessedresults:
+            open(args.saveprocessedresults+"_after.json","wt").write(json.dumps(results))
 
         if args.compareresults:
             # a simple test by comparing the received results with a saved CSV from a previous run
             # load the saved CSV
             with open(args.compareresults, newline='', encoding='utf-8-sig') as csvfile:
                 reader = csv.DictReader(csvfile)
                 savedheadings = list(reader.fieldnames)
@@ -596,15 +624,15 @@
         if len(results.keys()) != args.nresults:
 #            print( f"There are {len(results.keys())} results but {args.nresults} expected - Failed :-(" )
             raise Exception( f"There are {len(results.keys())} results but {args.nresults} expected - Failed :-(" )
         else:
             print( f"{len(results.keys())} results and {args.nresults} expected - Passed :-)" )
 
     if args.xmloutputfile is not None:
-    
+        # retrieve all resources in the results to XML
         # ensure output folder exists
         args.xmloutputfile = os.path.abspath(args.xmloutputfile)
         outputpath = os.path.split(args.xmloutputfile)[0]
 #        print( f"{outputpath=}" )
         if not os.path.isdir( outputpath ):
 #            print( f"creating {outputpath=}" )
             os.makedirs( outputpath, exist_ok=True)
```

### Comparing `elmclient-0.9.3/elmclient/examples/represt.py` & `elmclient-0.9.4/elmclient/examples/represt.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/examples/reqif_io.py` & `elmclient-0.9.4/elmclient/examples/reqif_io.py`

 * *Files 0% similar despite different names*

```diff
@@ -104,16 +104,16 @@
     parser_create.add_argument('-i', '--identifiers', nargs='*', default=[], help='Use * for all core artifacts or comma-separated list of requirement IDs to add - can specify this option more than once')
     parser_create.add_argument('-l', '--links', action="store_false", help="Don't include links in the reqif (defaults to including) - if you need this off, specify it on the last update or on the create")
     parser_create.add_argument('-m', '--modules', nargs='*', default=[], help='Use * or comma-separated list of module IDs or names of the module to add - for name you can use a regex - can specify this option more than once')
     parser_create.add_argument('-r', '--removeallartifacts', action="store_true", help="When updating, first remove all artifacts/modules/views")
     parser_create.add_argument('-s', '--description', default="-", help="Description for the definition")
     parser_create.add_argument('-t', '--tags', action="store_false", help="Don't include tags in the reqif (defaults to including) - if you need this off, specify it on the last update or on the create")
     parser_create.add_argument('-u', '--update', action="store_true", help="Update the named definition by adding things - it must already exist!")
-# NIY    parser_create.add_argument('-p', '--publicviews', nargs='*', default=[], help='* or CSL of public view names')
-# NIY    parser_create.add_argument('-v', '--moduleviews', nargs='*', default=[], help='* or CSL of module view names')
+# TODO: NIY    parser_create.add_argument('-p', '--publicviews', nargs='*', default=[], help='* or CSL of public view names')
+# TODO: NIY    parser_create.add_argument('-v', '--moduleviews', nargs='*', default=[], help='* or CSL of module view names')
 
     parser_delete.add_argument('definitionnames',nargs='*',default=[],help='One or more names of export definitions to delete - this can be a regex where . matches any character, etc. If you want the regex to match a complete name put ^ at the start and $ at the end')
     parser_delete.add_argument('-n', '--noconfirm', action='store_true', help="Don't prompt to confirm each delete (DANGEROUS!)")
     parser_delete.add_argument('-x', '--exception', action='store_true', help="Don't raise an exception if definition doesn't exist")
     
 
     args = parser.parse_args()
```

### Comparing `elmclient-0.9.3/elmclient/httpops.py` & `elmclient-0.9.4/elmclient/httpops.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/oslcqueryapi.py` & `elmclient-0.9.4/elmclient/oslcqueryapi.py`

 * *Files 2% similar despite different names*

```diff
@@ -90,14 +90,15 @@
     # sortorder default is + for ascending alphabetic sort, use'-' to get descending alphabetic sorting - use '>' to get increasing numeric sorting of the first item in sortby, or < to get decreasing numeric sort (if any value doesn't convert to integer it is assumed to be 0 so will sort first/last)
     def do_complex_query(self,queryresource, *, querystring='', searchterms=None, select='', orderby='', properties=None, isnulls=None
                         ,isnotnulls=None, enhanced=True, show_progress=True
                         ,show_info=False, verbose=False, maxresults=None, delaybetweenpages=0.0
                         , pagesize=200
                         ,resolvenames=True
                         ,totalize=False
+                        ,saverawresults=None
                      ):
         if searchterms and querystring:
             logger.info( f"{searchterms=}" )
             logger.info( f"{querystring=}" )
             raise Exception( "Can't use query and search terms together!" )
         if querystring is None:
             querystring=''
@@ -158,15 +159,15 @@
 
         if verbose:
             print( "Starting query - to terminate with current retrieved results press Esc and wait for the current query page to complete and then for processing to complete" )
         # now evaluate the queries
         resultstack = self._evaluate_steps(querycapabilityuri,querysteps, select=parsedselect, prefixes=prefixes
                                             , orderbys=parsedorderby, searchterms=searchterms, show_progress=show_progress
                                             , verbose=verbose, maxresults=maxresults,delaybetweenpages=delaybetweenpages
-                                            , pagesize=pagesize)
+                                            , pagesize=pagesize, saverawresults=saverawresults)
 
         if len(resultstack) != 1:
             raise Exception(f"Something went horribly wrong and there isn't exactly one result left on the query stack! {len(resultstack)} {resultstack}")
 
         # Now tidy up the results
         # in particular make sure type uris as column headers and values are turned into their more meaningful names
         # go through the results, mapping attribute uris back to names
@@ -289,15 +290,15 @@
     ########################################################################################
     ########################################################################################
     # Below here is private implementation
     #
 
     # for a query which has been parsed to steps, execute the steps, recursing if there is more than one compount_term
     # a query with two logicalor terms looks like: [[['dcterms:identifier', 'in', [3949]]], [['dcterms:identifier', 'in', [3950]]], 'logicalor']
-    def _evaluate_steps(self, querycapabilityuri,querysteps,*,resultstack=None, select=None, prefixes=None, orderbys=None, searchterms=None, show_progress=False, verbose=False, maxresults=None, delaybetweenpages=0.0, pagesize=200):
+    def _evaluate_steps(self, querycapabilityuri,querysteps,*,resultstack=None, select=None, prefixes=None, orderbys=None, searchterms=None, show_progress=False, verbose=False, maxresults=None, delaybetweenpages=0.0, pagesize=200, saverawresults=None):
         logger.info( f"_evaluate_steps {querysteps}" )
         resultstack = resultstack if resultstack is not None else []
         orderbys = orderbys or []
         select = select or []
         prefixes = prefixes or {}
         searchterms = searchterms or []
 
@@ -311,15 +312,15 @@
                 if len(step)>0 and isinstance(step[0],list):
                     # handle anded terms
                     # iterate, recursing
                     resultstack = self._evaluate_steps( querycapabilityuri,step,resultstack=resultstack, select=select, prefixes=prefixes, orderbys=orderbys, searchterms=searchterms, show_progress=show_progress, verbose=verbose, maxresults=maxresults, delaybetweenpages=delaybetweenpages)
 #                    raise Exception( f"Very strange parse result! {step}" )
                 else:
                     # do an actual query
-                    results = self.execute_oslc_query(querycapabilityuri,whereterms=[step], select=select, prefixes=prefixes, orderbys=orderbys, searchterms=searchterms, show_progress=show_progress, maxresults=maxresults, delaybetweenpages=delaybetweenpages, pagesize=pagesize, verbose=verbose)
+                    results = self.execute_oslc_query(querycapabilityuri,whereterms=[step], select=select, prefixes=prefixes, orderbys=orderbys, searchterms=searchterms, show_progress=show_progress, maxresults=maxresults, delaybetweenpages=delaybetweenpages, pagesize=pagesize, verbose=verbose, saverawresults=saverawresults)
                     if isinstance(results, list):
                         resultlist = {}
                         for result in results:
                             resultlist[result] = {}
                         resultstack.append(resultlist)
                     else:
                         # put results onto resultstack
@@ -390,15 +391,15 @@
         
 
     # lower-level OSLC query with prepared arguments
     # by default returns a list of uris as result, but if you provide a select list of attributes, returns a dictionary with as key the artifact uri, each result containing a dictionary with the selected values
     # the whereterms can be created using create_query_operator_string
     # NOTE that prefixes is reversed from what you might expect, i.e. keyed by URL and the value is the prefix!
     # NOTE that whereterms should be a list of lists (the oslc terms) - each of these nested lists is ['attribute',operator',value'] - if more than one and'd term, the first entry must be 'and'!
-    def execute_oslc_query(self, querycapabilityuri, *, whereterms=None, select=None, prefixes=None, orderbys=None, searchterms=None, show_progress=False, verbose=False, maxresults=None, delaybetweenpages=0.0, pagesize=200, intent=None):
+    def execute_oslc_query(self, querycapabilityuri, *, whereterms=None, select=None, prefixes=None, orderbys=None, searchterms=None, show_progress=False, verbose=False, maxresults=None, delaybetweenpages=0.0, pagesize=200, intent=None, saverawresults=None):
         if select is None:
             select = []
         prefixes = prefixes or {}
         if orderbys is None:
             orderbys = []
         if searchterms is None:
             searchterms = []
@@ -408,15 +409,15 @@
         query_params = self._create_query_params(whereterms, select=select, prefixes=prefixes, orderbys=orderbys, searchterms=searchterms)
 
         if self.hooks:
             query_params1 = self.hooks[0](query_params)
         else:
              query_params1 = query_params
 
-        results = self._execute_vanilla_oslc_query(querycapabilityuri,query_params1, select=select, prefixes=prefixes, show_progress=show_progress, verbose=verbose, maxresults=maxresults, delaybetweenpages=delaybetweenpages, pagesize=pagesize, intent=intent)
+        results = self._execute_vanilla_oslc_query(querycapabilityuri,query_params1, select=select, prefixes=prefixes, show_progress=show_progress, verbose=verbose, maxresults=maxresults, delaybetweenpages=delaybetweenpages, pagesize=pagesize, intent=intent, saverawresults=saverawresults)
         return results
 
     # convert whereterms (which is a list of OSLC and terms) into a corresponding oslc.where string
     # replacing property references with prefixed tags
     # updates map with all prefixes used
     def _get_query_clauses(self, whereterms, prefixmap):
         clauses = []
@@ -515,15 +516,15 @@
     #
     # This executes a single vanilla OSLC query (the enhanced stuff is handled by the caller)
     # Returns a dictionary with artifact uri as key containing a (possibly empty) dictionary with the selected values
     # NOTE the select contents must also be already encoded into query_params!
     # select is used to build the returned dictionary containing only the selected values
     #
 
-    def _execute_vanilla_oslc_query(self, querycapabilityuri, query_params, orderby=None, searchterms=None, select=None, prefixes=None, show_progress=False, pagesize=200, verbose=False, maxresults=None, delaybetweenpages=0.0, intent=None):
+    def _execute_vanilla_oslc_query(self, querycapabilityuri, query_params, orderby=None, searchterms=None, select=None, prefixes=None, show_progress=False, pagesize=200, verbose=False, maxresults=None, delaybetweenpages=0.0, intent=None,saverawresults=None):
         select = select or []
         orderby = orderby or []
         searchterms = searchterms or []
         prefixes = prefixes or {}
         logger.debug( f"{prefixes=}" )
         headers = {}
 
@@ -581,14 +582,18 @@
             # let the intent from entry be used for first page only, after that number the page being retrieved
             if page>1:
                 intent = f"Retrieve {utils.nth(page)} page of OSLC query results"
 
             # request this page
             this_result_xml = self.execute_get_rdf_xml(query_url, params=params, headers=headers, cacheable=False, intent=intent)
             queryurls.append(query_url)
+            
+            if saverawresults:
+                open( f"{saverawresults}{page:04d}" ,'wb').write(ET.tostring(this_result_xml))
+
             # accumulate the results
             result_xmls.append(this_result_xml)
             # check for maxresults exceeded - rough calculation!
             if maxresults is not None and len(result_xmls)*pagesize>=maxresults:
                 break
             # check for next page link
             if rdfxml.xml_find_element( this_result_xml, ".//oslc:nextPage") is None:
@@ -714,15 +719,15 @@
             else:
                 # only CM has rdfs:member with no sub-tags
                 cmmode = True
         else:
             # only RM returns rdfs:member with sub-tags
             rmmode = True
         logger.info(f"cmmode={cmmode} rmmode={rmmode} gcmode={gcmode} {qmmode=}")
-#        print(f"cmmode={cmmode} rmmode={rmmode} gcmode={gcmode} {qmmode=}")
+        # print(f"cmmode={cmmode} rmmode={rmmode} gcmode={gcmode} {qmmode=}")
         logger.debug( f"{prefixes=}" )
         revprefixes = { v:k for k,v in prefixes.items()}
         # with select - build a dictionary
         allprops = True if "*" in select else False
         # have to convert the select terms to complete URIs to be able to compare with tags  from the results xml also converted to complete URIs.
         # (the other way to do this would perhaps be to convert the selects to tags)
         if not allprops:
@@ -746,14 +751,15 @@
                     rdfs_member_es = rdfxml.xml_find_elements( result_xml, './/rdf:Description[@rdf:about]/dcterms:title/..')
 #                    print( f"2 {rdfs_member_es=}" )
 
 
             # process them
             if len(rdfs_member_es) > 0:
                 for rdfs_member in rdfs_member_es:
+                    # print( f"{rdfs_member.tag=}" )
                     # about is the uri of the resource
                     if cmmode or gcmode:
                         about = rdfs_member.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
                         # CM-style results
                         desc = result_xml.find(".//rdf:Description[@rdf:about='%s']" % (about), rdfxml.RDF_DEFAULT_PREFIX)
                     elif rmmode or qmmode:
                         # RM/QM-style results
@@ -763,85 +769,99 @@
                         if qmmode and len(rdfxml.xml_find_elements( rdfs_member, './/oslc:totalCount'))>0:
                             continue
                     else:
                         raise Exception("Query result extraction mode not set to anything!")
                     # is this a 'duplicate' result? AFAIK only reason this would happen is if oslc.select is e.g. oslc_rm:uses{dcterms:identifier}
                     if about not in result:
                         result[about] = {}
-                        dup = False
+#                        dup = False
                     else:
-                        dup = True
+#                        dup = True
+                        pass
                     if desc is not None:
                         # for an entry with no children, if dup and value is same then ignore it
                         #   if dup and value is different, exception
                         #
                         # for entry with children
                         #  always: store first value as list or append value to list
                         #
 
                         themembers = list(desc)
+                        # print( f"{len(themembers)=}" )
                         # now scan its children - these are the select results
                         for ent in themembers:
-                            # place is the column heading
-#                            place = None
+                            # first make sure this level is stored in the results, if it has a URI
+                            # print( f"no subs {len(ent)} {ent.tag=} {ent.text=}")
+                            # no children, just use the text if not empty or the resource URL
+                            if len(ent)>0 and rdfxml.xmlrdf_get_resource_uri(ent,attrib="rdf:parseType") == "Literal":
+                                # get the XML literal value by converting the whole ent to a string and then strip off the start/end tags!
+                                # (shouldn't there be a less hacky way of doing this?)
+                                literal = ET.tostring(ent).decode()
+                                value = literal[literal.index('>')+1:literal.rindex('<')]
+                                logger.info( f"0 {value=}" )
+                            elif ent.text is None or not ent.text.strip():
+                                # no text, try the resource URI
+                                value = ent.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
+                                if value is None:
+                                    # no resource URI, use an empty string
+                                    value = ""
+                                logger.info( f"1 {value=}" )
+                                # print( f"1 {value=}" )
+                            else:
+                                value = ent.text
+                                logger.info( f"2 {value=}" )
+                                # print( f"2 {value=}" )
+                            place = rdfxml.uri_to_default_prefixed_tag(rdfxml.tag_to_uri(ent.tag))
+                            # print( f"{place=} {value=} {result.get(about)=}" )
+#                                if dup and place in result[about]:
+                            if place and place in result[about]:
+                                # possibly extend as a list
+                                if result[about][place] is None or type(result[about][place])!=list:
+                                    # only extend the list if this value is different
+                                    if result[about][place] is not None and result[about][place] != value:
+                                        # already got one entry that's different - make it a list
+                                        result[about][place] = [result[about][place]]
+                                        result[about][place].append(value)
+                                        logger.debug( f"Saving4 {about} {place} {value}" )
+                                        logger.debug( f"{result[about][place]=}" )
+                                    else:
+                                        # repeat entry, cna be ignored
+                                        logger.debug( f"Saving5 {about} {place} {value}" )
+                                else:
+                                    # list already present - extend it
+                                    result[about][place].append(value)
+                                    logger.debug( f"Saving3 {about} {place} {value}" )
+                                    logger.debug( f"{result[about][place]=}" )
+
+                            else:
+                                # first time seen
+                                result[about][place] = value
+                                logger.debug( f"Saving2 {about} {place} {value}" )
+#                                    dup = True
+
+                            # now look at itse children
                             if len(ent)>0 and rdfxml.xmlrdf_get_resource_uri(ent,attrib="rdf:parseType") != "Literal":
+                                # this has children and isn't literal text
+                                # print( "has subs")
                                 # this entity has children; it's like using oslc.selct=oslc_rm:uses{dcterms:identifier}
                                 # work out a heading for this column by concatenating the ent tag with its child's tags
                                 for subent in ent[0]:
-                                    # these are the real values - they always result in lists
+                                    # these are the child values - they always result in lists
                                     place = rdfxml.remove_tag(ent.tag)+"/"+rdfxml.remove_tag(subent.tag)
 #                                    place = f"{rdfxml.tag_to_prefix(ent.tag)}/{rdfxml.tag_to_prefix(subent.tag)}"
                                     value = subent.text
-                                    if value is None:
+                                    if not value or not value.strip():
+                                        # no text, or text is emtpy - try getting resource URI instead
                                         value = rdfxml.xmlrdf_get_resource_uri(subent)
                                     if place in result[about]:
                                         result[about][place].append(value)
                                         logger.debug( f"Saving{about} {place} {value}" )
                                     else:
                                         result[about][place] = [value]
                                         logger.debug( f"Saving1 {about} {place} {value}" )
-                            else:
-                                # no children, just use the text if not empty or the resource URL
-                                if len(ent)>0 and rdfxml.xmlrdf_get_resource_uri(ent,attrib="rdf:parseType") == "Literal":
-                                    # get the XML literal value by converting the whole ent to a string and then strip off the start/end tags!
-                                    # (shouldn't there be a less hacky way of doing this?)
-                                    literal = ET.tostring(ent).decode()
-                                    value = literal[literal.index('>')+1:literal.rindex('<')]
-                                    logger.info( f"0 {value=}" )
-                                elif ent.text is None or not ent.text.strip():
-                                    # no text, try the resource URI
-                                    value = ent.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
-                                    if value is None:
-                                        # no resource URI, use an empty string
-                                        value = ""
-                                    logger.info( f"1 {value=}" )
-                                else:
-                                    value = ent.text
-                                    logger.info( f"2 {value=}" )
-                                place = rdfxml.uri_to_default_prefixed_tag(rdfxml.tag_to_uri(ent.tag))
-                                if dup and place in result[about]:
-                                    # possibly extend as a list
-                                    if result[about][place] is None or type(result[about][place])!=list:
-                                        # only extend the list if this value is different
-                                        if result[about][place] is not None and result[about][place] != value:
-                                            # make it a list
-                                            result[about][place] = [result[about][place]]
-                                            result[about][place].append(value)
-                                            logger.debug( f"Saving4 {about} {place} {value}" )
-                                            logger.debug( f"{result[about][place]=}" )
-                                        else:
-                                            logger.debug( f"Saving5 {about} {place} {value}" )
-                                    else:
-                                        result[about][place].append(value)
-                                        logger.debug( f"Saving3 {about} {place} {value}" )
-                                        logger.debug( f"{result[about][place]=}" )
-
-                                else:
-                                    result[about][place] = value
-                                    logger.debug( f"Saving2 {about} {place} {value}" )
 
         return result
 
     #
     # refer to OSLC Query 3.0 https://tools.oasis-open.org/version-control/svn/oslc-core/trunk/specs/oslc-query.html
     #
     # parse the query and return list of steps - each step is a single vanilla OSLC query, and for enhanced query syntax there will be a step per real OSLC query
```

### Comparing `elmclient-0.9.3/elmclient/rdfxml.py` & `elmclient-0.9.4/elmclient/rdfxml.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/server.py` & `elmclient-0.9.4/elmclient/server.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/tests/tests_6061.xlsx` & `elmclient-0.9.4/elmclient/tests/tests_6061.xlsx`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/tests/tests_702.xlsx` & `elmclient-0.9.4/elmclient/tests/tests_702.xlsx`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient/utils.py` & `elmclient-0.9.4/elmclient/utils.py`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/elmclient.egg-info/PKG-INFO` & `elmclient-0.9.4/elmclient.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: elmclient
-Version: 0.9.3
+Version: 0.9.4
 Summary: Python client for ELM with examples of OSLC Query, ReqIF import/export, Reportable REST, and more
 Home-page: https://github.com/IBM/ELM-Python-Client
 Author: Ian Barnard
 License: MIT
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -18,15 +18,15 @@
  Python client for IBM Enterprise Lifecycle Management applications
 
 
  (c) Copyright 2021- IBM Inc. All rights reserved
  
  SPDX-License-Identifier: MIT
 
- version="0.9.3"
+ version="0.9.4"
 
 
 Introduction
 ============
 
 The aim of this code is to provide a Python client for the IBM Enterprise Lifecycle Management (ELM) applications.
```

### Comparing `elmclient-0.9.3/elmclient.egg-info/SOURCES.txt` & `elmclient-0.9.4/elmclient.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `elmclient-0.9.3/setup.py` & `elmclient-0.9.4/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,30 +12,30 @@
 
 # The text of the README file
 README = (HERE / "README.md").read_text()
 
 # This call to setup() does all the work
 setup(
     name="elmclient",
-    version="0.9.3",
+    version="0.9.4",
     description="Python client for ELM with examples of OSLC Query, ReqIF import/export, Reportable REST, and more",
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://github.com/IBM/ELM-Python-Client",
     author="Ian Barnard",
 #    author_email="ian.barnard@uk.ibm.com",
     license="MIT",
     classifiers=[
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.9",
     ],
     packages=["elmclient", "elmclient.examples", "elmclient.examples.basic","elmclient.tests"],
     include_package_data=True,
-    install_requires=['CacheControl==0.12.6','anytree==2.8.0',"colorama==0.4.4","cryptography==3.4.4",'lark_parser==0.12.0','lockfile==0.12.2','lxml==4.7.1',"openpyxl == 3.0.9","python-dateutil==2.8.2", "pytz==2021.3", "requests>=2.24.0","requests_toolbelt>=0.9.3",'tqdm==4.56.2','urllib3==1.25.11',"twin", "bump2version", "twine"],
+    install_requires=['CacheControl==0.12.6','anytree==2.8.0',"colorama==0.4.4","cryptography==3.4.4",'lark_parser==0.12.0','lockfile==0.12.2','lxml==4.7.1',"openpyxl == 3.0.9","python-dateutil==2.8.2", "pytz==2021.3", "requests>=2.24.0","requests_toolbelt>=0.9.1",'tqdm==4.56.2','urllib3==1.25.11',"twin", "bump2version", "twine"],
     entry_points={
         "console_scripts": [
             "oslcquery=elmclient.examples.oslcquery:main",
             "batchquery=elmclient.examples.batchquery:main",
             "represt=elmclient.examples.represt:main",
             "reqif_io=elmclient.examples.reqif_io:main",
             "log2seq=elmclient.examples.log2seq:main",
```

