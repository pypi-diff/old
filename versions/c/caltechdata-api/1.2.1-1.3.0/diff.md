# Comparing `tmp/caltechdata_api-1.2.1.tar.gz` & `tmp/caltechdata_api-1.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "caltechdata_api-1.2.1.tar", last modified: Wed Jan 11 00:48:28 2023, max compression
+gzip compressed data, was "caltechdata_api-1.3.0.tar", last modified: Thu Apr  6 20:22:20 2023, max compression
```

## Comparing `caltechdata_api-1.2.1.tar` & `caltechdata_api-1.3.0.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-01-11 00:48:28.168473 caltechdata_api-1.2.1/
--rw-r--r--   0 tmorrell   (502) staff       (20)     1523 2017-11-22 17:15:19.000000 caltechdata_api-1.2.1/LICENSE
--rw-r--r--   0 tmorrell   (502) staff       (20)     2514 2023-01-11 00:48:28.167941 caltechdata_api-1.2.1/PKG-INFO
--rw-r--r--   0 tmorrell   (502) staff       (20)     1825 2022-12-06 00:24:56.000000 caltechdata_api-1.2.1/README.md
-drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-01-11 00:48:28.141452 caltechdata_api-1.2.1/caltechdata_api/
--rw-r--r--   0 tmorrell   (502) staff       (20)      400 2022-12-01 21:58:52.000000 caltechdata_api-1.2.1/caltechdata_api/__init__.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     6978 2023-01-05 00:14:34.000000 caltechdata_api-1.2.1/caltechdata_api/caltechdata_edit.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     7311 2023-01-05 00:14:40.000000 caltechdata_api-1.2.1/caltechdata_api/caltechdata_write.py
--rw-r--r--   0 tmorrell   (502) staff       (20)    15792 2023-01-11 00:38:52.000000 caltechdata_api-1.2.1/caltechdata_api/customize_schema.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     1983 2022-10-28 23:31:55.000000 caltechdata_api-1.2.1/caltechdata_api/download_file.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     1981 2021-09-03 16:50:58.000000 caltechdata_api-1.2.1/caltechdata_api/get_files.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     2489 2022-10-28 18:19:39.000000 caltechdata_api-1.2.1/caltechdata_api/get_metadata.py
--rw-r--r--   0 tmorrell   (502) staff       (20)     2742 2022-12-06 16:41:11.000000 caltechdata_api-1.2.1/caltechdata_api/utils.py
-drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-01-11 00:48:28.167318 caltechdata_api-1.2.1/caltechdata_api/vocabularies/
--rw-r--r--   0 tmorrell   (502) staff       (20)      794 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/date_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)      497 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/description_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)     1396 2022-12-06 16:41:11.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/identifier_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)    51301 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/licenses.csv
--rw-r--r--   0 tmorrell   (502) staff       (20)     2682 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/relation_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)    16372 2022-11-18 19:12:39.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/resource_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)     1815 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/roles.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)      332 2021-09-15 17:27:24.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies/title_types.yaml
--rw-r--r--   0 tmorrell   (502) staff       (20)      601 2021-09-21 20:43:40.000000 caltechdata_api-1.2.1/caltechdata_api/vocabularies.yaml
-drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-01-11 00:48:28.159002 caltechdata_api-1.2.1/caltechdata_api.egg-info/
--rw-r--r--   0 tmorrell   (502) staff       (20)     2514 2023-01-11 00:48:27.000000 caltechdata_api-1.2.1/caltechdata_api.egg-info/PKG-INFO
--rw-r--r--   0 tmorrell   (502) staff       (20)      884 2023-01-11 00:48:27.000000 caltechdata_api-1.2.1/caltechdata_api.egg-info/SOURCES.txt
--rw-r--r--   0 tmorrell   (502) staff       (20)        1 2023-01-11 00:48:27.000000 caltechdata_api-1.2.1/caltechdata_api.egg-info/dependency_links.txt
--rw-r--r--   0 tmorrell   (502) staff       (20)       44 2023-01-11 00:48:27.000000 caltechdata_api-1.2.1/caltechdata_api.egg-info/requires.txt
--rw-r--r--   0 tmorrell   (502) staff       (20)       16 2023-01-11 00:48:27.000000 caltechdata_api-1.2.1/caltechdata_api.egg-info/top_level.txt
--rw-r--r--   0 tmorrell   (502) staff       (20)       38 2023-01-11 00:48:28.168610 caltechdata_api-1.2.1/setup.cfg
--rw-r--r--   0 tmorrell   (502) staff       (20)     4587 2022-10-31 22:00:33.000000 caltechdata_api-1.2.1/setup.py
+drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-04-06 20:22:20.368445 caltechdata_api-1.3.0/
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1523 2017-11-22 17:15:19.000000 caltechdata_api-1.3.0/LICENSE
+-rw-r--r--   0 tmorrell   (502) staff       (20)     2514 2023-04-06 20:22:20.367644 caltechdata_api-1.3.0/PKG-INFO
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1825 2022-12-06 00:24:56.000000 caltechdata_api-1.3.0/README.md
+drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-04-06 20:22:20.308954 caltechdata_api-1.3.0/caltechdata_api/
+-rw-r--r--   0 tmorrell   (502) staff       (20)      400 2022-12-01 21:58:52.000000 caltechdata_api-1.3.0/caltechdata_api/__init__.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     7836 2023-04-06 20:14:53.000000 caltechdata_api-1.3.0/caltechdata_api/caltechdata_edit.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     8067 2023-04-06 20:14:53.000000 caltechdata_api-1.3.0/caltechdata_api/caltechdata_write.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)    15796 2023-04-06 20:14:53.000000 caltechdata_api-1.3.0/caltechdata_api/customize_schema.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1983 2022-10-28 23:31:55.000000 caltechdata_api-1.3.0/caltechdata_api/download_file.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1981 2021-09-03 16:50:58.000000 caltechdata_api-1.3.0/caltechdata_api/get_files.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     2489 2022-10-28 18:19:39.000000 caltechdata_api-1.3.0/caltechdata_api/get_metadata.py
+-rw-r--r--   0 tmorrell   (502) staff       (20)     2742 2022-12-06 16:41:11.000000 caltechdata_api-1.3.0/caltechdata_api/utils.py
+drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-04-06 20:22:20.366581 caltechdata_api-1.3.0/caltechdata_api/vocabularies/
+-rw-r--r--   0 tmorrell   (502) staff       (20)      794 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/date_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)      497 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/description_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1396 2022-12-06 16:41:11.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/identifier_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)    51301 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/licenses.csv
+-rw-r--r--   0 tmorrell   (502) staff       (20)     2682 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/relation_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)    16372 2022-11-18 19:12:39.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/resource_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)     1815 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/roles.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)      332 2021-09-15 17:27:24.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies/title_types.yaml
+-rw-r--r--   0 tmorrell   (502) staff       (20)      601 2021-09-21 20:43:40.000000 caltechdata_api-1.3.0/caltechdata_api/vocabularies.yaml
+drwxr-xr-x   0 tmorrell   (502) staff       (20)        0 2023-04-06 20:22:20.349155 caltechdata_api-1.3.0/caltechdata_api.egg-info/
+-rw-r--r--   0 tmorrell   (502) staff       (20)     2514 2023-04-06 20:22:19.000000 caltechdata_api-1.3.0/caltechdata_api.egg-info/PKG-INFO
+-rw-r--r--   0 tmorrell   (502) staff       (20)      884 2023-04-06 20:22:19.000000 caltechdata_api-1.3.0/caltechdata_api.egg-info/SOURCES.txt
+-rw-r--r--   0 tmorrell   (502) staff       (20)        1 2023-04-06 20:22:19.000000 caltechdata_api-1.3.0/caltechdata_api.egg-info/dependency_links.txt
+-rw-r--r--   0 tmorrell   (502) staff       (20)       49 2023-04-06 20:22:19.000000 caltechdata_api-1.3.0/caltechdata_api.egg-info/requires.txt
+-rw-r--r--   0 tmorrell   (502) staff       (20)       16 2023-04-06 20:22:19.000000 caltechdata_api-1.3.0/caltechdata_api.egg-info/top_level.txt
+-rw-r--r--   0 tmorrell   (502) staff       (20)       38 2023-04-06 20:22:20.368563 caltechdata_api-1.3.0/setup.cfg
+-rwxr-xr-x   0 tmorrell   (502) staff       (20)     4595 2023-04-06 20:14:24.000000 caltechdata_api-1.3.0/setup.py
```

### Comparing `caltechdata_api-1.2.1/LICENSE` & `caltechdata_api-1.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/PKG-INFO` & `caltechdata_api-1.3.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: caltechdata_api
-Version: 1.2.1
+Version: 1.3.0
 Summary: Python wrapper for CaltechDATA API.
 Home-page: https://github.com/caltechlibrary/caltechdata_api
 Author: Thomas E Morrell
 Author-email: tmorrell@caltech.edu
 License: https://data.caltech.edu/license
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python
```

### Comparing `caltechdata_api-1.2.1/README.md` & `caltechdata_api-1.3.0/README.md`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/caltechdata_edit.py` & `caltechdata_api-1.3.0/caltechdata_api/caltechdata_edit.py`

 * *Files 5% similar despite different names*

```diff
@@ -68,16 +68,35 @@
     if not token:
         token = os.environ["RDMTOK"]
 
     # If files is a string - change to single value array
     if isinstance(files, str) == True:
         files = [files]
 
+    # Check if file links were provided in the metadata
+    descriptions = []
+    for d in metadata["descriptions"]:
+        if d["description"].startswith("Files available via S3"):
+            ex_file_links = []
+            file_text = d["description"]
+            file_list = file_text.split('href="')
+            # Loop over links in description, skip header text
+            for file in file_list[1:]:
+                ex_file_links.append(file.split('"\n')[0])
+        else:
+            descriptions.append(d)
+    # We remove file link descriptions, and re-add below
+    metadata["descriptions"] = descriptions
+
+    # If user has provided file links as a cli option, we add those
     if file_links:
         metadata = add_file_links(metadata, file_links)
+    # Otherwise we add file links found in the mtadata file
+    elif ex_file_links:
+        metadata = add_file_links(metadata, ex_file_links)
 
     if production == True:
         url = "https://data.caltech.edu"
     else:
         url = "https://data.caltechlibrary.dev"
 
     headers = {
@@ -97,15 +116,15 @@
     if existing.status_code != 200:
         # Might have a draft
         existing = requests.get(
             url + "/api/records/" + idv + "/draft",
             headers=headers,
         )
         if existing.status_code != 200:
-            raise Exception(existing.text)
+            raise Exception(f"Record {idv} does not exist, cannot edit")
 
     status = existing.json()["status"]
 
     # Determine whether we need a new version
     version = False
     if status == "published" and files:
         version = True
```

### Comparing `caltechdata_api-1.2.1/caltechdata_api/caltechdata_write.py` & `caltechdata_api-1.3.0/caltechdata_api/caltechdata_write.py`

 * *Files 11% similar despite different names*

```diff
@@ -59,19 +59,16 @@
     # Currently configured for OSN S3 links
     link_string = ""
     endpoint = "https://renc.osn.xsede.org/"
     s3 = s3fs.S3FileSystem(anon=True, client_kwargs={"endpoint_url": endpoint})
     for link in file_links:
         file = link.split("/")[-1]
         path = link.split(endpoint)[1]
-        try:
-            size = s3.info(path)["Size"]
-            size = humanbytes(size)
-        except:
-            size = 0
+        size = s3.info(path)["size"]
+        size = humanbytes(size)
         if link_string == "":
             cleaned = link.strip(file)
             link_string = f"Files available via S3 at {cleaned}&lt;/p&gt;</p>"
         link_string += f"""{file} {size} 
         <p>&lt;a role="button" class="ui compact mini button" href="{link}"
         &gt; &lt;i class="download icon"&gt;&lt;/i&gt; Download &lt;/a&gt;</p>&lt;/p&gt;</p>
         """
@@ -120,14 +117,15 @@
     files=[],
     production=False,
     schema="43",
     publish=False,
     file_links=[],
     s3=None,
     community=None,
+    authors=False,
 ):
     """
     File links are links to files existing in external systems that will
     be added directly in a CaltechDATA record, instead of uploading the file.
 
     S3 is a s3sf object for directly opening files
     """
@@ -144,43 +142,67 @@
 
     # Pull out pid information
     if production == True:
         repo_prefix = "10.22002"
     else:
         repo_prefix = "10.33569"
     pids = {}
-    if "identifiers" in metadata:
-        for identifier in metadata["identifiers"]:
+    identifiers = []
+    if "metadata" in metadata:
+        # we have rdm schema
+        if "identifiers" in metadata["metadata"]:
+            identifiers = metadata["metadata"]["identifiers"]
+    elif "identifiers" in metadata:
+        identifiers = metadata["identifiers"]
+    for identifier in identifiers:
+        if "identifierType" in identifier:
             if identifier["identifierType"] == "DOI":
                 doi = identifier["identifier"]
                 prefix = doi.split("/")[0]
-
-                if prefix == repo_prefix:
-                    pids["doi"] = {
-                        "identifier": doi,
-                        "provider": "datacite",
-                        "client": "datacite",
-                    }
-                else:
-                    pids["doi"] = {
-                        "identifier": doi,
-                        "provider": "external",
-                    }
             elif identifier["identifierType"] == "oai":
                 pids["oai"] = {
                     "identifier": identifier["identifier"],
                     "provider": "oai",
                 }
+        elif "scheme" in identifier:
+            # We have RDM internal metadata
+            if identifier["scheme"] == "doi":
+                doi = identifier["identifier"]
+                prefix = doi.split("/")[0]
+            else:
+                doi = False
+        else:
+            doi = False
+        if doi != False:
+            if prefix == repo_prefix:
+                pids["doi"] = {
+                    "identifier": doi,
+                    "provider": "datacite",
+                    "client": "datacite",
+                }
+            else:
+                pids["doi"] = {
+                    "identifier": doi,
+                    "provider": "external",
+                }
+
     metadata["pids"] = pids
 
-    data = customize_schema.customize_schema(copy.deepcopy(metadata), schema=schema)
-    if production == True:
-        url = "https://data.caltech.edu/"
+    if authors == False:
+        data = customize_schema.customize_schema(copy.deepcopy(metadata), schema=schema)
+        if production == True:
+            url = "https://data.caltech.edu/"
+        else:
+            url = "https://data.caltechlibrary.dev/"
     else:
-        url = "https://data.caltechlibrary.dev/"
+        data = metadata
+        if production == True:
+            url = "https://authors.caltech.edu/"
+        else:
+            url = "https://authors.caltechlibrary.dev/"
 
     headers = {
         "Authorization": "Bearer %s" % token,
         "Content-type": "application/json",
     }
     f_headers = {
         "Authorization": "Bearer %s" % token,
@@ -190,14 +212,15 @@
     if not files:
         data["files"] = {"enabled": False}
     else:
         if "README.txt" in files:
             data["files"] = {"default_preview": "README.txt"}
 
     # Make draft and publish
+    print(data)
     result = requests.post(url + "/api/records", headers=headers, json=data)
     if result.status_code != 201:
         raise Exception(result.text)
     idv = result.json()["id"]
     publish_link = result.json()["links"]["publish"]
 
     if files:
```

### Comparing `caltechdata_api-1.2.1/caltechdata_api/customize_schema.py` & `caltechdata_api-1.3.0/caltechdata_api/customize_schema.py`

 * *Files 4% similar despite different names*

```diff
@@ -77,16 +77,16 @@
             else:
                 print(f"Name type {ntype} not known")
         else:
             # We default to organizational if not known
             cre["type"] = "personal"
         change_label(cre, "givenName", "given_name")
         change_label(cre, "familyName", "family_name")
-        if 'name' not in cre:
-            cre['name'] = cre['family_name']+','+cre['given_name']
+        if "name" not in cre:
+            cre["name"] = cre["family_name"] + "," + cre["given_name"]
         change_label(cre, "nameIdentifiers", "identifiers")
         if "identifiers" in cre:
             new_id = []
             for ide in cre["identifiers"]:
                 change_label(ide, "nameIdentifier", "identifier")
                 change_label(ide, "nameIdentifierScheme", "scheme")
                 ide["scheme"] = ide["scheme"].lower()
```

### Comparing `caltechdata_api-1.2.1/caltechdata_api/download_file.py` & `caltechdata_api-1.3.0/caltechdata_api/download_file.py`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/get_files.py` & `caltechdata_api-1.3.0/caltechdata_api/get_files.py`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/get_metadata.py` & `caltechdata_api-1.3.0/caltechdata_api/get_metadata.py`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/utils.py` & `caltechdata_api-1.3.0/caltechdata_api/utils.py`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/date_types.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/date_types.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/identifier_types.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/identifier_types.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/licenses.csv` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/licenses.csv`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/relation_types.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/relation_types.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/resource_types.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/resource_types.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies/roles.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies/roles.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api/vocabularies.yaml` & `caltechdata_api-1.3.0/caltechdata_api/vocabularies.yaml`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/caltechdata_api.egg-info/PKG-INFO` & `caltechdata_api-1.3.0/caltechdata_api.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: caltechdata-api
-Version: 1.2.1
+Version: 1.3.0
 Summary: Python wrapper for CaltechDATA API.
 Home-page: https://github.com/caltechlibrary/caltechdata_api
 Author: Thomas E Morrell
 Author-email: tmorrell@caltech.edu
 License: https://data.caltech.edu/license
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python
```

### Comparing `caltechdata_api-1.2.1/caltechdata_api.egg-info/SOURCES.txt` & `caltechdata_api-1.3.0/caltechdata_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `caltechdata_api-1.2.1/setup.py` & `caltechdata_api-1.3.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -56,15 +56,15 @@
 download = meta["downloadUrl"]
 license = meta["license"]
 name = meta["name"]
 
 REQUIRES_PYTHON = ">=3.6.0"
 
 # What packages are required for this module to be executed?
-REQUIRED = ["requests", "datacite>1.1.0", "tqdm>=4.62.3", "pyyaml"]
+REQUIRED = ["requests", "datacite>1.1.0", "tqdm>=4.62.3", "pyyaml", "s3fs"]
 
 # What packages are optional?
 EXTRAS = {
     # 'fancy feature': ['django'],
 }
 
 files = package_files("caltechdata_api", "vocabularies")
```

