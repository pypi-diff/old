# Comparing `tmp/morphcp-0.0.6.tar.gz` & `tmp/morphcp-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "morphcp-0.0.6.tar", last modified: Wed Apr  5 19:56:52 2023, max compression
+gzip compressed data, was "morphcp-0.0.9.tar", last modified: Fri Apr  7 13:40:35 2023, max compression
```

## Comparing `morphcp-0.0.6.tar` & `morphcp-0.0.9.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.645002 morphcp-0.0.6/
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1068 2023-03-29 11:57:39.000000 morphcp-0.0.6/LICENSE.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)      805 2023-04-05 19:56:52.643224 morphcp-0.0.6/PKG-INFO
--rw-r--r--   0 vscode    (1000) vscode    (1000)      104 2023-03-29 12:04:55.000000 morphcp-0.0.6/README.md
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.531018 morphcp-0.0.6/morphcp/
--rw-r--r--   0 vscode    (1000) vscode    (1000)      170 2023-04-05 12:33:44.000000 morphcp-0.0.6/morphcp/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     3406 2023-04-05 12:34:17.000000 morphcp-0.0.6/morphcp/create_env.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.570196 morphcp-0.0.6/morphcp/inject/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/inject/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)    19532 2023-04-05 12:26:26.000000 morphcp-0.0.6/morphcp/inject/components.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.578853 morphcp-0.0.6/morphcp/logging/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/logging/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1959 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/logging/loghandler.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     3229 2023-04-05 19:55:50.000000 morphcp-0.0.6/morphcp/morphclass.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.600296 morphcp-0.0.6/morphcp/tenants/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/tenants/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     3709 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/tenants/manage_tenant.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.637873 morphcp-0.0.6/morphcp/utils/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/utils/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     3205 2023-03-29 11:57:39.000000 morphcp-0.0.6/morphcp/utils/helpers.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     2328 2023-04-05 12:23:01.000000 morphcp-0.0.6/morphcp/vars.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-05 19:56:52.560856 morphcp-0.0.6/morphcp.egg-info/
--rw-r--r--   0 vscode    (1000) vscode    (1000)      805 2023-04-05 19:56:52.000000 morphcp-0.0.6/morphcp.egg-info/PKG-INFO
--rw-r--r--   0 vscode    (1000) vscode    (1000)      490 2023-04-05 19:56:52.000000 morphcp-0.0.6/morphcp.egg-info/SOURCES.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        1 2023-04-05 19:56:52.000000 morphcp-0.0.6/morphcp.egg-info/dependency_links.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        9 2023-04-05 19:56:52.000000 morphcp-0.0.6/morphcp.egg-info/requires.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        8 2023-04-05 19:56:52.000000 morphcp-0.0.6/morphcp.egg-info/top_level.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)       38 2023-04-05 19:56:52.645984 morphcp-0.0.6/setup.cfg
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1007 2023-04-05 19:56:50.000000 morphcp-0.0.6/setup.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.536199 morphcp-0.0.9/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1068 2023-03-29 11:57:39.000000 morphcp-0.0.9/LICENSE.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      805 2023-04-07 13:40:35.534840 morphcp-0.0.9/PKG-INFO
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      104 2023-03-29 12:04:55.000000 morphcp-0.0.9/README.md
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.461439 morphcp-0.0.9/morphcp/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      170 2023-04-05 12:33:44.000000 morphcp-0.0.9/morphcp/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     3407 2023-04-07 13:33:32.000000 morphcp-0.0.9/morphcp/create_env.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.496285 morphcp-0.0.9/morphcp/inject/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/inject/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)    21658 2023-04-07 13:40:23.000000 morphcp-0.0.9/morphcp/inject/components.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.504068 morphcp-0.0.9/morphcp/logging/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/logging/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1959 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/logging/loghandler.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     3229 2023-04-05 19:55:50.000000 morphcp-0.0.9/morphcp/morphclass.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.515231 morphcp-0.0.9/morphcp/tenants/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/tenants/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     3709 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/tenants/manage_tenant.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.529684 morphcp-0.0.9/morphcp/utils/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/utils/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     3205 2023-03-29 11:57:39.000000 morphcp-0.0.9/morphcp/utils/helpers.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     2328 2023-04-05 12:23:01.000000 morphcp-0.0.9/morphcp/vars.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 13:40:35.487279 morphcp-0.0.9/morphcp.egg-info/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      805 2023-04-07 13:40:35.000000 morphcp-0.0.9/morphcp.egg-info/PKG-INFO
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      490 2023-04-07 13:40:35.000000 morphcp-0.0.9/morphcp.egg-info/SOURCES.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        1 2023-04-07 13:40:35.000000 morphcp-0.0.9/morphcp.egg-info/dependency_links.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        9 2023-04-07 13:40:35.000000 morphcp-0.0.9/morphcp.egg-info/requires.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        8 2023-04-07 13:40:35.000000 morphcp-0.0.9/morphcp.egg-info/top_level.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)       38 2023-04-07 13:40:35.536880 morphcp-0.0.9/setup.cfg
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1007 2023-04-07 13:40:33.000000 morphcp-0.0.9/setup.py
```

### Comparing `morphcp-0.0.6/LICENSE.txt` & `morphcp-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/PKG-INFO` & `morphcp-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: morphcp
-Version: 0.0.6
+Version: 0.0.9
 Summary: Tool utilized to deploy content into a morpheus appliance
 Home-page: https://gitlab.com/jaredlutgen/morphcp
 Author: Jared Lutgen
 Author-email: jlutgen@morpheusdata.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `morphcp-0.0.6/morphcp/create_env.py` & `morphcp-0.0.9/morphcp/create_env.py`

 * *Files 1% similar despite different names*

```diff
@@ -19,19 +19,20 @@
 def content_pack_processing():
     cl = RequestsApi()
     logger = loghandler.get_logger(__name__)
     injector.inject_groups()
     injector.inject_roles()
     injector.inject_optionlist()
     injector.inject_inputs()
+    injector.inject_integrations()
     injector.inject_tasks()
     # BUG Troubleshoot workflows they are not finding the correct task id. 
     #injector.inject_workflow()
     injector.inject_whitelabel()
-    injector.inject_integrations()
+
 
 def process_content_pack_higher_ed(x):
     """
     The process_content_pack function is the main function that will be called by the content pack.
     It will call all of the other functions in this file to inject all of your content into a tenant.
```

### Comparing `morphcp-0.0.6/morphcp/inject/components.py` & `morphcp-0.0.9/morphcp/inject/components.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,14 +9,23 @@
 from morphcp.morphclass import RequestsApi
 #import morph_util.utils.helpers as morph_util
 import morphcp.utils.helpers as morph_util
 #import morph_util.logging.loghandler as loghandler
 import morphcp.logging.loghandler as loghandler
 #from morph_util.vars import * 
 from morphcp.vars import *
+
+def success_status(json_response):
+    logger = loghandler.get_logger(__name__)
+    if json_response['success'] is True:
+        logger.info("Integration successfully created")
+    if json_response['success'] is False:
+        logger.error(f"Integration creation failed: {json_response['errors']}")
+
+
 def inject_groups():
     """
     The inject_groups function is used to create groups in the mo-laptop.
     It takes a directory as an argument and looks for files that match the pattern:
     groups_inject_filter_pattern = &quot;*.json&quot;
     The function then opens each file, loads it into memory, and iterates over each group object.  Each group object is then sent to /api/groups using a POST request.
     
@@ -203,23 +212,59 @@
         
     
     :return: The response of the post request to the tasks endpoint
     :doc-author: Trelent
     """
     logger = loghandler.get_logger(__name__)
     cl = RequestsApi()
-    cp_tasks_dir = os.path.join(contentpack_base_folder,os.environ.get("contentpack"),task_payload_folder,task_inject_filter_pattern)
-    files = glob.glob(cp_tasks_dir)
+    repos = cl.get(f"/api/options/codeRepositories").json()
+    cp_dir = os.path.join(contentpack_base_folder,os.environ.get("contentpack"),task_payload_folder,f"*{task_extract_filename}*")
+    files = glob.glob(cp_dir)
+    logger.debug(f"CP DIR: {cp_dir}")
+    logger.debug(f"Files for tasks: {files}")
+    # for file in files:
+    #     with open(file,'r') as f:
+    #         data = json.load(f)
+    #     f.close()
+    # if os.path.isdir(inputdir) is True:
+    #     logger.debug(f'{inputdir}/{task_payload_folder}/{task_extract_filename}')
+    #     files = glob.glob(f'{inputdir}/{task_payload_folder}/*{task_extract_filename}*')
     for file in files:
         with open(file,'r') as f:
             data = json.load(f)
         f.close()
-        payload = json.dumps(data)
-        resp = cl.post("/api/tasks", data = payload)
-        logger.debug(resp.json())
+        logger.debug(files)
+        if "ansibleGitId" in data['task']['taskOptions']:
+            if data['task']['taskOptions']['ansibleGitId'] != None:
+                resp = cl.get(f"/api/integrations?name={urllib.parse.quote(data['task']['taskOptions']['ansibleGitId'])}").json()
+                if resp['integrations'] == []:
+                    logger.warning("Ansible Git ID not found")
+                    logger.warning("Please create the integration first")
+                    logger.info("Skipping task creation")
+                else:
+                    data['task']['taskOptions']['ansibleGitId'] = resp['integrations'][0]['id']
+        elif data['task']['file'] != None:
+            if data['task']['file']['sourceType'] == "repository":
+                for repo in repos['data']:
+                    if data['task']['file']['repository']['name'] in repo['name']:
+                        data['task']['file']['repository']['id'] = repo['value']
+                    else:
+                        logger.debug("No match found")
+                        logger.debug(f"Task: {data['task']['file']['repository']['name']}")
+                        logger.debug(f"Repo: {repos}")
+        payload = json.dumps(data, indent=4)
+        logger.debug(f"Payload: {payload}")
+        resp = cl.post("/api/tasks", data = payload).json()
+        # if resp['success'] is True:
+        #     logger.info(f"Task {data['task']['name']} created")
+        # elif resp['success'] is False:
+        #     logger.warning(f"Task {data['task']['name']} failed to create")
+        #     logger.warning(json.dumps(resp))
+        success_status(resp)
+        
         
 def inject_optionlist():
     """
     The inject_optionlist function is used to inject optionlist payloads into the Morph API.
         The function takes no arguments and returns nothing.
     
     
@@ -401,27 +446,24 @@
                         {
                             "id": cloudid
                         }
                         ]
                     }
             }
             payload = json.dumps(payload)
-            response = cl.put(f"/api/groups/{group_id}/update-zones", data = payload).json()
-            logger.debug(response)
+            resp = cl.put(f"/api/groups/{group_id}/update-zones", data = payload).json()
+            logger.debug(resp)
+            success_status(resp)
 
 def inject_integrations():
     logger = loghandler.get_logger(__name__)
     cl = RequestsApi()
     cp_dir = os.path.join(contentpack_base_folder,os.environ.get("contentpack"),integration_payload_folder,integration_pattern)
     files = glob.glob(cp_dir)
     for file in files:
         with open(file,'r') as f:
             data = json.load(f)
         f.close()
         payload = json.dumps(data)
         resp = cl.post("/api/integrations", data = payload).json()
         logger.debug(resp)
-        if resp['success'] is True:
-            logger.info("Integration successfully created")
-        if resp['success'] is False:
-            logger.error("Integration creation failed")
-            logger.error(resp)
+        success_status(resp)
```

### Comparing `morphcp-0.0.6/morphcp/logging/loghandler.py` & `morphcp-0.0.9/morphcp/logging/loghandler.py`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/morphcp/morphclass.py` & `morphcp-0.0.9/morphcp/morphclass.py`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/morphcp/tenants/manage_tenant.py` & `morphcp-0.0.9/morphcp/tenants/manage_tenant.py`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/morphcp/utils/helpers.py` & `morphcp-0.0.9/morphcp/utils/helpers.py`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/morphcp/vars.py` & `morphcp-0.0.9/morphcp/vars.py`

 * *Files identical despite different names*

### Comparing `morphcp-0.0.6/morphcp.egg-info/PKG-INFO` & `morphcp-0.0.9/morphcp.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: morphcp
-Version: 0.0.6
+Version: 0.0.9
 Summary: Tool utilized to deploy content into a morpheus appliance
 Home-page: https://gitlab.com/jaredlutgen/morphcp
 Author: Jared Lutgen
 Author-email: jlutgen@morpheusdata.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `morphcp-0.0.6/setup.py` & `morphcp-0.0.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 
 setuptools.setup(
     author="Jared Lutgen",
     author_email="jlutgen@morpheusdata.com",
     name='morphcp',
     license="MIT",
     description='Tool utilized to deploy content into a morpheus appliance',
-    version='v0.0.6',
+    version='v0.0.9',
     long_description=README,
     url='https://gitlab.com/jaredlutgen/morphcp',
     packages=setuptools.find_packages(),
     python_requires=">=3.5",
     install_requires=['requests'],
     classifiers=[
         # Trove classifiers
```

