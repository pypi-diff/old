# Comparing `tmp/python-eigen-ingenuity-0.4.3.tar.gz` & `tmp/python-eigen-ingenuity-0.4.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python-eigen-ingenuity-0.4.3.tar", last modified: Wed Mar  8 15:23:38 2023, max compression
+gzip compressed data, was "python-eigen-ingenuity-0.4.4.tar", last modified: Thu Apr  6 15:04:00 2023, max compression
```

## Comparing `python-eigen-ingenuity-0.4.3.tar` & `python-eigen-ingenuity-0.4.4.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-03-08 15:23:38.235768 python-eigen-ingenuity-0.4.3/
--rw-r--r--   0 berhic     (501) staff       (20)      578 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.3/LICENSE
--rw-r--r--   0 berhic     (501) staff       (20)       70 2022-11-30 15:55:19.000000 python-eigen-ingenuity-0.4.3/MANIFEST.in
--rw-r--r--   0 berhic     (501) staff       (20)    11663 2023-03-08 15:23:38.235550 python-eigen-ingenuity-0.4.3/PKG-INFO
--rw-r--r--   0 berhic     (501) staff       (20)    11343 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.3/README.md
-drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-03-08 15:23:38.234020 python-eigen-ingenuity-0.4.3/eigeningenuity/
--rw-r--r--   0 berhic     (501) staff       (20)      904 2023-03-08 15:21:11.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/__init__.py
--rw-r--r--   0 berhic     (501) staff       (20)    15749 2023-01-10 11:02:17.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/assetmodel.py
-drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-03-08 15:23:38.234351 python-eigen-ingenuity-0.4.3/eigeningenuity/core/
--rw-r--r--   0 berhic     (501) staff       (20)     7714 2023-03-08 14:51:11.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/core/__init__.py
--rw-r--r--   0 berhic     (501) staff       (20)     1146 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/core/debug.py
--rw-r--r--   0 berhic     (501) staff       (20)     4783 2022-12-15 11:24:11.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/elastic.py
--rw-r--r--   0 berhic     (501) staff       (20)     3026 2022-12-15 11:42:28.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/events.py
--rw-r--r--   0 berhic     (501) staff       (20)    33990 2022-12-01 13:12:54.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/historian.py
--rw-r--r--   0 berhic     (501) staff       (20)     2829 2023-03-08 14:18:40.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/smartdash.py
--rw-r--r--   0 berhic     (501) staff       (20)     4067 2022-12-01 09:50:12.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/sql.py
--rw-r--r--   0 berhic     (501) staff       (20)    11778 2022-12-15 11:39:53.000000 python-eigen-ingenuity-0.4.3/eigeningenuity/util.py
--rw-r--r--   0 berhic     (501) staff       (20)       92 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.3/pyproject.toml
-drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-03-08 15:23:38.235347 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/
--rw-r--r--   0 berhic     (501) staff       (20)    11663 2023-03-08 15:23:38.000000 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/PKG-INFO
--rw-r--r--   0 berhic     (501) staff       (20)      551 2023-03-08 15:23:38.000000 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/SOURCES.txt
--rw-r--r--   0 berhic     (501) staff       (20)        1 2023-03-08 15:23:38.000000 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/dependency_links.txt
--rw-r--r--   0 berhic     (501) staff       (20)       24 2023-03-08 15:23:38.000000 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/requires.txt
--rw-r--r--   0 berhic     (501) staff       (20)       15 2023-03-08 15:23:38.000000 python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/top_level.txt
--rw-r--r--   0 berhic     (501) staff       (20)       38 2023-03-08 15:23:38.235813 python-eigen-ingenuity-0.4.3/setup.cfg
--rw-r--r--   0 berhic     (501) staff       (20)      689 2023-03-08 15:23:26.000000 python-eigen-ingenuity-0.4.3/setup.py
+drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-04-06 15:04:00.766403 python-eigen-ingenuity-0.4.4/
+-rw-r--r--   0 berhic     (501) staff       (20)      578 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.4/LICENSE
+-rw-r--r--   0 berhic     (501) staff       (20)       70 2022-11-30 15:55:19.000000 python-eigen-ingenuity-0.4.4/MANIFEST.in
+-rw-r--r--   0 berhic     (501) staff       (20)    11663 2023-04-06 15:04:00.766157 python-eigen-ingenuity-0.4.4/PKG-INFO
+-rw-r--r--   0 berhic     (501) staff       (20)    11343 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.4/README.md
+drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-04-06 15:04:00.763942 python-eigen-ingenuity-0.4.4/eigeningenuity/
+-rw-r--r--   0 berhic     (501) staff       (20)     1203 2023-04-06 15:03:48.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/__init__.py
+-rw-r--r--   0 berhic     (501) staff       (20)    15868 2023-04-05 14:48:43.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/assetmodel.py
+drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-04-06 15:04:00.764702 python-eigen-ingenuity-0.4.4/eigeningenuity/core/
+-rw-r--r--   0 berhic     (501) staff       (20)     7715 2023-04-06 10:18:46.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/core/__init__.py
+-rw-r--r--   0 berhic     (501) staff       (20)     1146 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/core/debug.py
+-rw-r--r--   0 berhic     (501) staff       (20)     6133 2023-04-05 13:42:19.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/elastic.py
+-rw-r--r--   0 berhic     (501) staff       (20)     3040 2023-04-06 10:18:06.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/events.py
+-rw-r--r--   0 berhic     (501) staff       (20)    36189 2023-04-06 11:02:05.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/historian.py
+-rw-r--r--   0 berhic     (501) staff       (20)     2829 2023-03-08 14:18:40.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/smartdash.py
+-rw-r--r--   0 berhic     (501) staff       (20)     4067 2022-12-01 09:50:12.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/sql.py
+-rw-r--r--   0 berhic     (501) staff       (20)    11778 2022-12-15 11:39:53.000000 python-eigen-ingenuity-0.4.4/eigeningenuity/util.py
+-rw-r--r--   0 berhic     (501) staff       (20)       92 2022-08-16 09:33:43.000000 python-eigen-ingenuity-0.4.4/pyproject.toml
+drwxr-xr-x   0 berhic     (501) staff       (20)        0 2023-04-06 15:04:00.765822 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/
+-rw-r--r--   0 berhic     (501) staff       (20)    11663 2023-04-06 15:04:00.000000 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/PKG-INFO
+-rw-r--r--   0 berhic     (501) staff       (20)      551 2023-04-06 15:04:00.000000 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/SOURCES.txt
+-rw-r--r--   0 berhic     (501) staff       (20)        1 2023-04-06 15:04:00.000000 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/dependency_links.txt
+-rw-r--r--   0 berhic     (501) staff       (20)       24 2023-04-06 15:04:00.000000 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/requires.txt
+-rw-r--r--   0 berhic     (501) staff       (20)       15 2023-04-06 15:04:00.000000 python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/top_level.txt
+-rw-r--r--   0 berhic     (501) staff       (20)       38 2023-04-06 15:04:00.766459 python-eigen-ingenuity-0.4.4/setup.cfg
+-rw-r--r--   0 berhic     (501) staff       (20)      689 2023-04-04 15:23:03.000000 python-eigen-ingenuity-0.4.4/setup.py
```

### Comparing `python-eigen-ingenuity-0.4.3/LICENSE` & `python-eigen-ingenuity-0.4.4/LICENSE`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/PKG-INFO` & `python-eigen-ingenuity-0.4.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-eigen-ingenuity
-Version: 0.4.3
+Version: 0.4.4
 Summary: A python library used to query data from the Eigen Ingenuity system
 Home-page: https://www.eigen.co/
 Author: Murray Callander
 Author-email: info@eigen.co
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `python-eigen-ingenuity-0.4.3/README.md` & `python-eigen-ingenuity-0.4.4/README.md`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/__init__.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/__init__.py`

 * *Files 21% similar despite different names*

```diff
@@ -13,13 +13,19 @@
 
 h = get_historian("instancename")
 h.listDataTags()
 """
 
 from __future__ import (absolute_import, division, print_function, unicode_literals)
 import pkg_resources
+from eigeningenuity.core import EigenServer
 from eigeningenuity.historian import get_historian, list_historians, get_default_historian_name
+from eigeningenuity.elastic import get_elastic
+from eigeningenuity.events import get_eventlog
+from eigeningenuity.assetmodel import get_assetmodel
+from eigeningenuity.smartdash import get_smartdash
+from eigeningenuity.sql import get_sql
 
 from eigeningenuity.core import *
 
-__all__ = ["get_historian", "get_assetmodel", "get_elastic", "getsql", "get_eventlog", "list_historians", "get_default_historian_name", "EigenServer"]
+__all__ = ["get_historian", "get_assetmodel", "get_elastic", "get_sql", "get_eventlog", "get_smartdash", "list_historians", "get_default_historian_name", "EigenServer"]
 __version__ = pkg_resources.require("python-eigen-ingenuity")[0].version
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/assetmodel.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/assetmodel.py`

 * *Files 3% similar despite different names*

```diff
@@ -75,15 +75,18 @@
         """
         args = {'q': query}
         response = self._doJsonCypherRequest("execute", args)
 
         if output == "raw":
             return response
         if output == "json":
-            return response
+            if type(response) == list and len(response) == 1:
+                return response[0]
+            else:
+                return response
         if output == "df":
             return pd.json_normalize(response)
 
 
 
     def getRelatedAssetsCommonMenu(self, node: str, output="json", filepath = None):
         """
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/core/__init__.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/core/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -42,15 +42,15 @@
         try:
             if name.startswith("http://") or name.startswith("https://"):
                 if name.endswith("/"):
                     baseurl = name
                 else:
                     baseurl = name + "/"
             else:
-                baseurl = "http://" + name + "/"
+                baseurl = "https://" + name + "/"
         except:
             baseurl = "http://localhost:8080/"
 
         self.__baseurl = baseurl
         self.__disablessl = disableSsl
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/core/debug.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/core/debug.py`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/elastic.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/elastic.py`

 * *Files 14% similar despite different names*

```diff
@@ -37,38 +37,88 @@
        """This is a constructor. It takes in a URL like http://infra:8080/ei-applet/search/"""
        self.baseurl = baseurl
 
     def _doJsonRequest(self,cmd,params):
         url = self.baseurl + "?cmd=" + urlquote(cmd)
         return _do_eigen_json_request(url,**params)
 
-    def _testConnection(self,instance):
+    def _testConnection(self,instance,index):
         """Preflight Request to verify connection to ingenuity"""
         try:
-            status = requests.get(self.baseurl + "?cmd=DODIRECTSEARCH&clientname=" + instance).status_code
+            status = requests.get(self.baseurl + "?cmd=DODIRECTSEARCH&clientname=" + instance + "&index=" + index + "&search=%7B%7D").status_code
             if status != 200:
                 raise ConnectionError(
                     "Invalid API Response from " + self.baseurl + "?cmd=DODIRECTSEARCH&clientname" + instance + ". Please check the base url is correct, the instance is running and has an elasticsearch database.")
         except (URLError, ConnectionError):
             raise ConnectionError ("Failed to connect to ingenuity instance at " + self.baseurl + "?cmd=DODIRECTSEARCH" + ". Please check the url is correct and the instance is up.")
+        
+        return status
+    
+    def listIndices(self,instance:str):
+        """Lists all indices in Elastic Database.
+
+        Args:
+            instance: The elasticsearch instance to query indices from.
+            
+        Returns:
+            List of all indices
+        """
+
+        args = {"clientname": instance}
+
+        mappings = self._doJsonRequest("GETMAPPINGS",args)
+
+        return mappings.keys()
+
+        
+    def checkIndices(self,instance:str,indices:str):
+        """Checks for indices in Elastic Database.
+
+        Args:
+            instance: The elasticsearch instance to query instances from.
+            indices: The elasticsearch indices to search for
+            
+        Returns:
+            Boolean indicating existence of the index, or dict of form {index: boolean}
+        """
+
+        foundIndices = self.listIndices(instance)
+        indices = force_list(indices)
+
+        result = {}
+
+        if len(indices) != 1:
+            for index in indices:
+                if index in foundIndices:
+                    result[index] = True
+                else:
+                    result[index] = False
+        else:
+            if indices[0] in foundIndices:
+                return True
+            else:
+                return False
+
+        return result
+
 
     def executeRawQuery(self,index:str, query:str, instance:str = "elasticsearch-int", output:str = "json", filepath:str = None):
         """Executes a raw cypher query against Elastic.
 
         Args:
             index: The elasticsearch index to query
             query: The body of the query
             instance: (Optional) The instance of elasticsearch to query. Defaults to elasticsearch-int
             output: (Optional) The format in which to return the data. Accepts one of: "raw" - The raw json returned by the API; "json" - A processed version of the json response; "df" - A formatted pandas dataframe object; "file" - Writes the response to a .json file in the local directory. Defaults to "json"
             filepath: (Optional) Name and path to the .json file that will be created/overwritten. If omitted, will create a file in the current directory with a generated name. Has no effect unless output is "file".
             
         Returns:
             Elasticsearch API response to the query, the format is dependent on the output parameter
         """
-        self._testConnection()
+        self._testConnection(instance,index)
         validOutputTypes = ["raw", "json", "df", "file"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args["clientname"] = instance
         args["index"] = index
         args["search"] = query
@@ -86,15 +136,14 @@
             return pd.json_normalize(response['results'])
         elif output == "file":
             if filepath is None:
                 filepath = "eigenElasticResponse-" + index + "-" + str(dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
             with open(filepath + ".json", "w") as f:
                 f.write(json.dumps(response, indent=4))
 
-
 def get_elastic(eigenserver:EigenServer = None):
     """Instantiate an elasticsearch connection for the given EigenServer.
 
     Args:
         eigenserver: (Optional) An EigenServer Object linked to the ingenuity url containing the elasticsearch. Can be omitted if environmental variable "EIGENSERVER" exists and is equal to the Ingenuity base url
 
     Returns:
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/events.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/events.py`

 * *Files 5% similar despite different names*

```diff
@@ -32,18 +32,20 @@
         """
         events = parseEvents(events)
         url = self.baseurl + "events/save-multiple"
         event_chunks = list(divide_chunks(events, 500))
         success = []
         for chunk in event_chunks:
             data = {"events": chunk}
-            success.append(requests.post(url, json=data, verify=False))
-        return all(success)
+            resp = requests.post(url, json=data, verify=False)
+            success.append(resp)
 
-    def pushTo365Events(self, events:Union[dict,list,str]) -> bool:
+        return success
+
+    def pushTo365(self, events:Union[dict,list,str]) -> bool:
         """
         Push one or more events to the office 365 connector, only accepts pre-defined event structures
 
         Args:
             events: Can only accept event structures that have been pre-defined in ingenuity. A single event as dict, many events as a list of dicts, or the string filepath of a file containing events
 
         Returns:
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/historian.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/historian.py`

 * *Files 3% similar despite different names*

```diff
@@ -14,15 +14,14 @@
   tags = h.listDataTags()
   for tag in tags:
       dp = h.getCurrentDataPoint(tag)
       print(asctime(time.gmtime(dp['timestamp'])), dp['value'])
 """
 
 import json
-import datetime
 import math
 import logging
 import csv
 import requests
 from urllib.parse import quote as urlquote
 from typing import Union
 from datetime import datetime
@@ -95,32 +94,38 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
-        ret = {}
+        response = {}
 
         for tag in force_list(tags):
             args = {}
             args['tag'] = tag
-            ret[tag] = (self._doJsonRequest("getmeta", args))
+            response[tag] = (self._doJsonRequest("getmeta", args))
+
 
         if output == "raw":
-            return ret
-        if output == "json":
-            return json.dumps(ret)
-        if output == "df":
-            return jsonToDf(ret, True)
+            return response
+        elif output == "json":
+            if len(force_list(tags)) == 1:
+                return response[tags]
+            else:
+                return response
+        elif output == "string":
+            return json.dumps(response)
+        elif output == "df":
+            return jsonToDf(response, True)
         elif output == "csv":
-            return csvWriter(ret,self.historian,filepath,multi_csv,"GetMetaData")
+            return csvWriter(response,self.historian,filepath,multi_csv,"GetMetaData")
         return None
 
 
     def getCurrentDataPoints(self, tags: Union[str, list], output: str = "json", filepath:str=None, multi_csv:bool=False):
         """
         Return most recent raw value for one or more datatags
 
@@ -133,15 +138,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args['tag'] = force_list(tags)
         response = self._doJsonRequest("getmulticurrent", args)
         items = response["items"]
 
@@ -149,14 +154,19 @@
             if items == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(response["unknown"]) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return response[tags]
+            else:
+                return response
+        elif output == "string":
             return json.dumps(items)
         elif output == "df":
             return jsonToDf(items)
         elif output == "csv":
             return csvWriter(items,self.historian,filepath,multi_csv,"GetCurrent")
         return None
 
@@ -176,15 +186,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args['tag'] = force_list(tags)
         args['timestamp'] = force_list(timestamps)
         response = self._doJsonRequest("getmulti", args)
         items = response['items']
@@ -193,14 +203,19 @@
             if items == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(response["unknown"]) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return items[tags]
+            else:
+                return items
+        elif output == "string":
             return json.dumps(items)
         elif output == "df":
             return jsonToDf(items)
         elif output == "csv":
             return csvWriter(items,self.historian,filepath,multi_csv,"GetInterpolatedPoints")
         return None
 
@@ -221,15 +236,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args['tag'] = force_list(tags)
         args['start'] = time_to_epoch_millis(start)
         args['end'] = time_to_epoch_millis(end)
         args['maxpoints'] = maxpoints
@@ -240,14 +255,19 @@
             if items == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(response["unknown"]) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return items[tags]
+            else:
+                return items
+        elif output == "string":
             return json.dumps(items)
         elif output == "df":
             return jsonToDf(items)
         elif output == "csv":
             return csvWriter(items,self.historian,filepath,multi_csv,"GetRaw")
         return None
 
@@ -269,15 +289,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args['tag'] = force_list(tags)
         args['start'] = time_to_epoch_millis(start)
         args['end'] = time_to_epoch_millis(end)
         args['count'] = count
@@ -288,14 +308,19 @@
             if items == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(response["unknown"]) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return items[tags]
+            else:
+                return items
+        elif output == "string":
             return json.dumps(items)
         elif output == "df":
             return jsonToDf(items)
         elif output == "csv":
             return csvWriter(items,self.historian,filepath,multi_csv,"GetInterpolatedRange")
         return None
 
@@ -318,15 +343,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         args = {}
         args['tag'] = force_list(tags)
         args['start'] = time_to_epoch_millis(start)
         args['end'] = time_to_epoch_millis(end)
         args['count'] = count
@@ -341,14 +366,19 @@
             if response == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(missing) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return response[tags]
+            else:
+                return response
+        elif output == "string":
             return json.dumps(response)
         elif output == "df":
             return aggToDf(response)
         elif output == "csv":
             order = ["tag","start","end","min","max","avg","var","stddev","count","numgood","numbad"]
             return csvWriter(response,self.historian,filepath,multi_csv,"GetAggregates",order,True)
         return None
@@ -373,15 +403,15 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
 
         epoch_ms_start = time_to_epoch_millis(start)
         epoch_ms_end = time_to_epoch_millis(end)
 
         if window is not None:
@@ -411,14 +441,19 @@
             if response == {}:
                 raise EigenException("None of the provided tags could be found in historian " + self.historian)
             logging.warning("Could not find tags: " + str(missing) + " in historian " + self.historian)
 
         if output == "raw":
             return response
         elif output == "json":
+            if len(force_list(tags)) == 1:
+                return response[tags]
+            else:
+                return response
+        elif output == "string":
             return json.dumps(response)
         elif output == "df":
             return aggToDf(response)
         elif output == "csv":
             order = ["tag","start","end","min","max","avg","var","stddev","count","numgood","numbad"]
             return csvWriter(response,self.historian,filepath,multi_csv,"GetAggregateIntervals",order,True)
 
@@ -438,35 +473,35 @@
 
         Raises:
             ValueError: When invalid Output Type is given
             URLError: When no Ingenuity instance could be found at given EigenServer, or no internet connection is available
             RemoteServerException: When the provided historian could not be found, or the API response contains an error
             RunTimeError/HTTPError: No response from the API
         """
-        validOutputTypes = ["raw", "json", "df", "csv"]
+        validOutputTypes = ["raw", "json", "df", "csv", "string"]
         if output not in validOutputTypes:
             raise ValueError("output must be one of %r." % validOutputTypes)
         ret = {}
         aggs = self.getAggregates(force_list(tags), start, end, "COUNT", 1, "raw")
         for tag in aggs.keys():
             ret[tag] = aggs[tag][0]["count"]
 
         response = self._matchArgumentCardinality(tags, ret)
 
-        if output == "raw":
+        if output == "raw" or output == "json":
             return response
-        elif output == "json":
+        elif output == "string":
             return json.dumps(response)
         elif output == "df":
             df = jsonToDf({"No. of Points": response})
             return df
         return None
 
 
-    def _writeDataPoints(self, data:dict) -> bool:
+    def _writeDataPoints(self, data) -> bool:
         rawdata = {}
         for tag in list(data.keys()):
             rawdps = []
             for dp in force_list(data[tag]):
                 rawdps.append([int(dp.getTimestamp() * 1000), dp.getValue(), dp.getStatus()])
             rawdata[tag] = rawdps
 
@@ -515,16 +550,37 @@
                                 badTags.append(i)
                     return ret
                 else:
                     raise KeyError
             return ret[proto]
         except KeyError:
             raise KeyError("Could not find tag(s): " + str(proto))
+        
+    def writePoints(self, tag:str, points:Union[dict,list]) -> bool:
+        """
+        Writes point data to a single existing tag.
 
+        Args:
+            tag: Id of tag to write to
+            points: The points to add to the tag (takes form [{value: ... , timestamp: ... , status: ...}, { ... }, ... ])
 
+        Returns:
+            Success: A boolean representing the successful push of data.
+        """
+        points = force_list(points)
+
+        datapoints = {tag : []}
+        for point in points:
+            if type(point["timestamp"]) is datetime:
+                point["timestamp"] = point["timestamp"].timestamp()
+            datapoints[tag].append(DataPoint(point["value"],point["timestamp"],point["status"]))
+
+        return self._writeDataPoints(datapoints)
+    
+    
     def batchCSVImport(self, filepaths: Union[str,list]) -> bool:
         """
         Writes tag data from one or more csv file to Ingenuity. Will create a tag if it does not exist.
 
         Args:
             filepaths: The paths to one or more csv files. CSV Layouts must be as follows, with one point per line: tag,value,timestamp,status,units,description
 
@@ -582,15 +638,15 @@
                         datapoints[tag] = [DataPoint(item["value"], item["timestamp"], item["status"])]
                 totalPoints += len(datapoints[tag])
 
             success.append(self._writeDataPoints(datapoints))
         return all(success)
 
 
-class DataPoint(object):
+class DataPoint(object): # LEGACY OBJECT
     """This class represents a data point which has a value and a python timestamp, and optionally a status of 'OK' or 'BAD'.
        Timestamp is stored in epochseconds. The constructor will convert datetime and tuples into floating point epoch seconds.
     """
 
     def __init__(self, value, timestamp, status = 'OK'):
         """This constructor takes in a value, a python timestamp (epoch floating point seconds or datetime or tuple)
         and an optional status.  Status is either "OK" or "BAD" and will default to "OK"
@@ -720,7 +776,10 @@
     Returns:
         The name of the default historian
     """
     if eigenserver is None:
         eigenserver = get_default_server()
 
     return eigenserver.getDefaultDataSource("historian")
+
+def createPoint(value:Union[str,int,float],timestamp:int,status:str):
+    return {"value": value, "timestamp": timestamp, "status": status}
```

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/smartdash.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/smartdash.py`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/sql.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/sql.py`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/eigeningenuity/util.py` & `python-eigen-ingenuity-0.4.4/eigeningenuity/util.py`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/PKG-INFO` & `python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-eigen-ingenuity
-Version: 0.4.3
+Version: 0.4.4
 Summary: A python library used to query data from the Eigen Ingenuity system
 Home-page: https://www.eigen.co/
 Author: Murray Callander
 Author-email: info@eigen.co
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `python-eigen-ingenuity-0.4.3/python_eigen_ingenuity.egg-info/SOURCES.txt` & `python-eigen-ingenuity-0.4.4/python_eigen_ingenuity.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `python-eigen-ingenuity-0.4.3/setup.py` & `python-eigen-ingenuity-0.4.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 README = (HERE / "README.md").read_text()
 
 pkgname = 'python-eigen-ingenuity'
 
 # Invoke setup
 setup(
     name=pkgname,
-    version='0.4.3',
+    version='0.4.4',
     author='Murray Callander',
     author_email='info@eigen.co',
     url='https://www.eigen.co/',
     description="A python library used to query data from the Eigen Ingenuity system",
     long_description=README,
     long_description_content_type="text/markdown",
     packages=find_packages("."),
```

