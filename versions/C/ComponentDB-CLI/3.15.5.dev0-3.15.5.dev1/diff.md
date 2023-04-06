# Comparing `tmp/ComponentDB-CLI-3.15.5.dev0.tar.gz` & `tmp/ComponentDB-CLI-3.15.5.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ComponentDB-CLI-3.15.5.dev0.tar", last modified: Tue Mar 21 18:00:36 2023, max compression
+gzip compressed data, was "ComponentDB-CLI-3.15.5.dev1.tar", last modified: Thu Apr  6 20:52:47 2023, max compression
```

## Comparing `ComponentDB-CLI-3.15.5.dev0.tar` & `ComponentDB-CLI-3.15.5.dev1.tar`

### file list

```diff
@@ -1,48 +1,48 @@
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.054754 ComponentDB-CLI-3.15.5.dev0/
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/
--rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-03-21 18:00:35.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/PKG-INFO
--rw-rw-r--   0 darek     (1000) darek     (1000)     1545 2023-03-21 18:00:36.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/SOURCES.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)        1 2023-03-21 18:00:35.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/dependency_links.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)      227 2023-03-21 18:00:35.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/entry_points.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)       96 2023-03-21 18:00:35.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/requires.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)        7 2023-03-21 18:00:35.000000 ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/top_level.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-03-21 18:00:36.054754 ComponentDB-CLI-3.15.5.dev0/PKG-INFO
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/__init__.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/__init__.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/cli/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/cli/__init__.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     9142 2022-12-28 01:44:25.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/cli/cliBase.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/utility/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/utility/__init__.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     6047 2022-04-26 16:43:26.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/common/utility/configurationManager.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/__init__.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.050754 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/__init__.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:36.054754 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/
--rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-04-11 21:33:56.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/__init__.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3868 2022-05-03 20:30:22.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addDocumentFile.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     5926 2022-05-03 21:00:56.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addDocumentProperty.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     5892 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addProperty.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     9549 2022-05-03 16:01:28.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/cdb_log_to_mqtt.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3496 2022-05-03 20:31:36.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/createLocation.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)    11672 2022-05-03 19:10:24.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getCatalogItemsByName.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     2852 2022-05-03 19:11:18.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getLocationIdByName.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7772 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getProperties.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     1544 2022-10-31 18:46:48.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/help.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)    18237 2022-12-07 18:49:59.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/info.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)    12151 2022-10-31 18:02:35.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/search.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     6777 2022-05-03 20:32:40.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemDetails.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     5451 2022-05-03 20:33:43.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemLocation.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3459 2022-05-03 20:35:02.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemLogById.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3889 2022-05-03 20:35:27.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemStatusById.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5371 2022-05-03 21:02:51.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setMachineInstallState.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3666 2022-05-03 20:54:55.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setParentLocation.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     4419 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setPropertiesAndMetadata.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3599 2022-05-03 20:42:12.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setQrIdById.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     5213 2022-05-03 20:58:42.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/updateHierarchy.py
--rwxrwxr-x   0 darek     (1000) darek     (1000)     3214 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cli.py
--rw-rw-r--   0 darek     (1000) darek     (1000)       38 2023-03-21 18:00:36.054754 ComponentDB-CLI-3.15.5.dev0/setup.cfg
--rw-rw-r--   0 darek     (1000) darek     (1000)     1618 2023-03-21 17:53:20.000000 ComponentDB-CLI-3.15.5.dev0/setup.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.587502 ComponentDB-CLI-3.15.5.dev1/
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/
+-rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-04-06 20:52:46.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/PKG-INFO
+-rw-rw-r--   0 darek     (1000) darek     (1000)     1545 2023-04-06 20:52:47.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/SOURCES.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)        1 2023-04-06 20:52:47.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/dependency_links.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)      227 2023-04-06 20:52:47.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/entry_points.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)       96 2023-04-06 20:52:47.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/requires.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)        7 2023-04-06 20:52:47.000000 ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/top_level.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-04-06 20:52:47.587502 ComponentDB-CLI-3.15.5.dev1/PKG-INFO
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/__init__.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/__init__.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/cli/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/cli/__init__.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     9142 2022-12-28 01:44:25.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/cli/cliBase.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/utility/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/utility/__init__.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     6047 2022-04-26 16:43:26.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/common/utility/configurationManager.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/__init__.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.583502 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-03-24 21:01:53.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/__init__.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:47.587502 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/
+-rw-rw-r--   0 darek     (1000) darek     (1000)        0 2022-04-11 21:33:56.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/__init__.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3868 2022-05-03 20:30:22.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addDocumentFile.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     5926 2022-05-03 21:00:56.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addDocumentProperty.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     5892 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addProperty.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     9549 2022-05-03 16:01:28.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/cdb_log_to_mqtt.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3496 2022-05-03 20:31:36.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/createLocation.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)    11672 2022-05-03 19:10:24.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getCatalogItemsByName.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     2852 2022-05-03 19:11:18.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getLocationIdByName.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7772 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getProperties.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     1544 2022-10-31 18:46:48.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/help.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)    18237 2022-12-07 18:49:59.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/info.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)    12151 2022-10-31 18:02:35.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/search.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     6777 2022-05-03 20:32:40.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemDetails.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     5451 2022-05-03 20:33:43.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemLocation.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3459 2022-05-03 20:35:02.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemLogById.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3889 2022-05-03 20:35:27.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemStatusById.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5371 2022-05-03 21:02:51.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setMachineInstallState.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3666 2022-05-03 20:54:55.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setParentLocation.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     4419 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setPropertiesAndMetadata.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3599 2022-05-03 20:42:12.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setQrIdById.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     5213 2022-05-03 20:58:42.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/updateHierarchy.py
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     3214 2023-03-21 16:56:29.000000 ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cli.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)       38 2023-04-06 20:52:47.587502 ComponentDB-CLI-3.15.5.dev1/setup.cfg
+-rw-rw-r--   0 darek     (1000) darek     (1000)     1618 2023-04-06 20:50:05.000000 ComponentDB-CLI-3.15.5.dev1/setup.py
```

### Comparing `ComponentDB-CLI-3.15.5.dev0/ComponentDB_CLI.egg-info/SOURCES.txt` & `ComponentDB-CLI-3.15.5.dev1/ComponentDB_CLI.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/common/cli/cliBase.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/common/cli/cliBase.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/common/utility/configurationManager.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/common/utility/configurationManager.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addDocumentFile.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addDocumentFile.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addDocumentProperty.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addDocumentProperty.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/addProperty.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/addProperty.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/cdb_log_to_mqtt.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/cdb_log_to_mqtt.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/createLocation.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/createLocation.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getCatalogItemsByName.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getCatalogItemsByName.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getLocationIdByName.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getLocationIdByName.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/getProperties.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/getProperties.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/help.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/help.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/info.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/info.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/search.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/search.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemDetails.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemDetails.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemLocation.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemLocation.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemLogById.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemLogById.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setItemStatusById.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setItemStatusById.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setMachineInstallState.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setMachineInstallState.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setParentLocation.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setParentLocation.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setPropertiesAndMetadata.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setPropertiesAndMetadata.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/setQrIdById.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/setQrIdById.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cdbCliCmnds/updateHierarchy.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cdbCliCmnds/updateHierarchy.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/cdbCli/service/cli/cli.py` & `ComponentDB-CLI-3.15.5.dev1/cdbCli/service/cli/cli.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-CLI-3.15.5.dev0/setup.py` & `ComponentDB-CLI-3.15.5.dev1/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 twine upload dist/(specific version file)
 """
 
 from setuptools import setup
 from setuptools import find_packages
 
 setup(name='ComponentDB-CLI',
-      version='3.15.5.dev0',
+      version='3.15.5.dev1',
       packages=['cdbCli',
                 'cdbCli.common',
                 'cdbCli.common.cli',
                 'cdbCli.common.utility',
                 'cdbCli.service',
                 'cdbCli.service.cli',
                 'cdbCli.service.cli.cdbCliCmnds',],
@@ -28,15 +28,15 @@
                         'urllib3',
                         'six',
                         'paho-mqtt',
                         'click',
                         'pandas',
                         'rich',
                         'InquirerPy',
-                        'ComponentDB-API==3.15.5.dev0'],
+                        'ComponentDB-API==3.15.5.dev1'],
       license='Copyright (c) UChicago Argonne, LLC. All rights reserved.',
       description='Python APIs used to communicate with java hosted ComponentDB API.',
       maintainer='Dariusz Jarosz',
       maintainer_email='djarosz@aps.anl.gov',
       url='https://github.com/AdvancedPhotonSource/ComponentDB',      
       entry_points={
         'console_scripts': [
```

