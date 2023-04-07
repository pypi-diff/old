# Comparing `tmp/morphqs-0.1.4.tar.gz` & `tmp/morphqs-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "morphqs-0.1.4.tar", last modified: Fri Apr  7 14:47:30 2023, max compression
+gzip compressed data, was "morphqs-0.1.5.tar", last modified: Fri Apr  7 14:52:51 2023, max compression
```

## Comparing `morphqs-0.1.4.tar` & `morphqs-0.1.5.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:47:30.846302 morphqs-0.1.4/
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1072 2023-03-29 01:49:10.000000 morphqs-0.1.4/LICENSE.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)      924 2023-04-07 14:47:30.844818 morphqs-0.1.4/PKG-INFO
--rw-r--r--   0 vscode    (1000) vscode    (1000)      206 2023-03-29 01:54:53.000000 morphqs-0.1.4/README.md
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:47:30.783736 morphqs-0.1.4/morphqs/
--rw-r--r--   0 vscode    (1000) vscode    (1000)      226 2023-04-07 14:46:49.000000 morphqs-0.1.4/morphqs/__init__.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:47:30.832750 morphqs-0.1.4/morphqs/components/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 02:36:46.000000 morphqs-0.1.4/morphqs/components/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1253 2023-04-07 14:03:43.000000 morphqs-0.1.4/morphqs/components/ansible.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     6189 2023-04-07 14:43:59.000000 morphqs-0.1.4/morphqs/components/integrations.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     6366 2023-04-05 12:30:10.000000 morphqs-0.1.4/morphqs/components/uchigheredmsp.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     4720 2023-04-07 14:47:22.000000 morphqs-0.1.4/morphqs/components/usecasedeployment.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:47:30.841211 morphqs-0.1.4/morphqs/logging/
--rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-28 19:26:20.000000 morphqs-0.1.4/morphqs/logging/__init__.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1959 2023-03-28 19:26:20.000000 morphqs-0.1.4/morphqs/logging/loghandler.py
--rw-r--r--   0 vscode    (1000) vscode    (1000)     3034 2023-03-28 19:51:08.000000 morphqs-0.1.4/morphqs/morphclass.py
-drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:47:30.809751 morphqs-0.1.4/morphqs.egg-info/
--rw-r--r--   0 vscode    (1000) vscode    (1000)      924 2023-04-07 14:47:30.000000 morphqs-0.1.4/morphqs.egg-info/PKG-INFO
--rw-r--r--   0 vscode    (1000) vscode    (1000)      456 2023-04-07 14:47:30.000000 morphqs-0.1.4/morphqs.egg-info/SOURCES.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        1 2023-04-07 14:47:30.000000 morphqs-0.1.4/morphqs.egg-info/dependency_links.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        9 2023-04-07 14:47:30.000000 morphqs-0.1.4/morphqs.egg-info/requires.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)        8 2023-04-07 14:47:30.000000 morphqs-0.1.4/morphqs.egg-info/top_level.txt
--rw-r--r--   0 vscode    (1000) vscode    (1000)       38 2023-04-07 14:47:30.847397 morphqs-0.1.4/setup.cfg
--rw-r--r--   0 vscode    (1000) vscode    (1000)     1024 2023-04-07 14:46:56.000000 morphqs-0.1.4/setup.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:52:51.801140 morphqs-0.1.5/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1072 2023-03-29 01:49:10.000000 morphqs-0.1.5/LICENSE.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      924 2023-04-07 14:52:51.799984 morphqs-0.1.5/PKG-INFO
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      206 2023-03-29 01:54:53.000000 morphqs-0.1.5/README.md
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:52:51.736262 morphqs-0.1.5/morphqs/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      226 2023-04-07 14:46:49.000000 morphqs-0.1.5/morphqs/__init__.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:52:51.787754 morphqs-0.1.5/morphqs/components/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-29 02:36:46.000000 morphqs-0.1.5/morphqs/components/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1253 2023-04-07 14:03:43.000000 morphqs-0.1.5/morphqs/components/ansible.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     6349 2023-04-07 14:52:40.000000 morphqs-0.1.5/morphqs/components/integrations.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     6366 2023-04-05 12:30:10.000000 morphqs-0.1.5/morphqs/components/uchigheredmsp.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     4720 2023-04-07 14:47:22.000000 morphqs-0.1.5/morphqs/components/usecasedeployment.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:52:51.796554 morphqs-0.1.5/morphqs/logging/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        0 2023-03-28 19:26:20.000000 morphqs-0.1.5/morphqs/logging/__init__.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1959 2023-03-28 19:26:20.000000 morphqs-0.1.5/morphqs/logging/loghandler.py
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     3034 2023-03-28 19:51:08.000000 morphqs-0.1.5/morphqs/morphclass.py
+drwxr-xr-x   0 vscode    (1000) vscode    (1000)        0 2023-04-07 14:52:51.764999 morphqs-0.1.5/morphqs.egg-info/
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      924 2023-04-07 14:52:51.000000 morphqs-0.1.5/morphqs.egg-info/PKG-INFO
+-rw-r--r--   0 vscode    (1000) vscode    (1000)      456 2023-04-07 14:52:51.000000 morphqs-0.1.5/morphqs.egg-info/SOURCES.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        1 2023-04-07 14:52:51.000000 morphqs-0.1.5/morphqs.egg-info/dependency_links.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        9 2023-04-07 14:52:51.000000 morphqs-0.1.5/morphqs.egg-info/requires.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)        8 2023-04-07 14:52:51.000000 morphqs-0.1.5/morphqs.egg-info/top_level.txt
+-rw-r--r--   0 vscode    (1000) vscode    (1000)       38 2023-04-07 14:52:51.802213 morphqs-0.1.5/setup.cfg
+-rw-r--r--   0 vscode    (1000) vscode    (1000)     1024 2023-04-07 14:52:49.000000 morphqs-0.1.5/setup.py
```

### Comparing `morphqs-0.1.4/LICENSE.txt` & `morphqs-0.1.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/PKG-INFO` & `morphqs-0.1.5/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: morphqs
-Version: 0.1.4
+Version: 0.1.5
 Summary: Tool utilized to deploy some basic concepts for the Morpheus Data Platform
 Home-page: https://gitlab.com/jaredlutgen/morphqs
 Author: Jared Lutgen
 Author-email: jlutgen@morpheusdata.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `morphqs-0.1.4/morphqs/components/ansible.py` & `morphqs-0.1.5/morphqs/components/ansible.py`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/morphqs/components/integrations.py` & `morphqs-0.1.5/morphqs/components/integrations.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 from ..morphclass import RequestsApi
 import morphqs.logging.loghandler as loghandler
 import json
 import urllib
+import sys
 
 def add_integration(default_branch, repo_url, integration_name):
     """
     The add_integration function is used to create a new integration in Morpheus.
         It takes three arguments: 
             1) default_branch - the branch that will be checked out by default when cloning the repo (defaults to master)
             2) repo_url - The URL of the repository you want to integrate with Morpheus. This can be any valid git url, including SSH and HTTP(S). 
@@ -54,18 +55,22 @@
         if resp["success"] == False:
             logger.error(f"Failed to create integration {integration_name}")
             logger.error(resp["errors"])
         
         coderepoId = cl.get(f"/api/options/codeRepositories?integrationId={intid}").json()
         if coderepoId["data"] != []:
             repoid = coderepoId["data"]["value"]
-        logger.debug(f"integration id: {intid}")
-        logger.debug(f"repo id {repoid}")
-        logger.debug(f"code repo response: {coderepoId}")
-        return repoid
+            logger.debug(f"integration id: {intid}")
+            logger.debug(f"repo id {repoid}")
+            logger.debug(f"code repo response: {coderepoId}")
+            return repoid
+        else: 
+            logger.error("Failed to create integration")
+            logger.error(coderepoId)
+            sys.exit(1)
        
 
 
 
 def add_integration_ansible(default_branch, repo_url, integration_name, ansibleplaybooks, ansibleroles, ansiblegroupvars, ansiblehostvars):
     """
     The add_integration_ansible function creates an Ansible integration in Morpheus.
```

### Comparing `morphqs-0.1.4/morphqs/components/uchigheredmsp.py` & `morphqs-0.1.5/morphqs/components/uchigheredmsp.py`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/morphqs/components/usecasedeployment.py` & `morphqs-0.1.5/morphqs/components/usecasedeployment.py`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/morphqs/logging/loghandler.py` & `morphqs-0.1.5/morphqs/logging/loghandler.py`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/morphqs/morphclass.py` & `morphqs-0.1.5/morphqs/morphclass.py`

 * *Files identical despite different names*

### Comparing `morphqs-0.1.4/morphqs.egg-info/PKG-INFO` & `morphqs-0.1.5/morphqs.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: morphqs
-Version: 0.1.4
+Version: 0.1.5
 Summary: Tool utilized to deploy some basic concepts for the Morpheus Data Platform
 Home-page: https://gitlab.com/jaredlutgen/morphqs
 Author: Jared Lutgen
 Author-email: jlutgen@morpheusdata.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `morphqs-0.1.4/setup.py` & `morphqs-0.1.5/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 
 setuptools.setup(
     author="Jared Lutgen",
     author_email="jlutgen@morpheusdata.com",
     name='morphqs',
     license="MIT",
     description='Tool utilized to deploy some basic concepts for the Morpheus Data Platform',
-    version='v0.1.4',
+    version='v0.1.5',
     long_description=README,
     url='https://gitlab.com/jaredlutgen/morphqs',
     packages=setuptools.find_packages(),
     python_requires=">=3.5",
     install_requires=['requests'],
     classifiers=[
         # Trove classifiers
```

