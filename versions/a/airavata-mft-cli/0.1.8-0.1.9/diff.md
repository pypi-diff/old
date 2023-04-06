# Comparing `tmp/airavata_mft_cli-0.1.8.tar.gz` & `tmp/airavata_mft_cli-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "airavata_mft_cli-0.1.8.tar", max compression
+gzip compressed data, was "airavata_mft_cli-0.1.9.tar", max compression
```

## Comparing `airavata_mft_cli-0.1.8.tar` & `airavata_mft_cli-0.1.9.tar`

### file list

```diff
@@ -1,15 +1,17 @@
--rw-r--r--   0        0        0      799 2023-01-28 08:18:42.145208 airavata_mft_cli-0.1.8/README.md
--rw-r--r--   0        0        0      788 2023-01-28 08:18:42.145596 airavata_mft_cli-0.1.8/airavata_mft_cli/__init__.py
--rw-r--r--   0        0        0     1207 2023-01-28 08:18:42.146370 airavata_mft_cli-0.1.8/airavata_mft_cli/base.py
--rw-r--r--   0        0        0     4754 2023-01-28 08:18:49.965387 airavata_mft_cli-0.1.8/airavata_mft_cli/bootstrap.py
--rw-r--r--   0        0        0      994 2023-01-28 08:18:42.147168 airavata_mft_cli-0.1.8/airavata_mft_cli/main.py
--rw-r--r--   0        0        0     8971 2023-02-21 17:11:35.685811 airavata_mft_cli-0.1.8/airavata_mft_cli/operations.py
--rw-r--r--   0        0        0     2960 2023-02-21 17:11:35.686360 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/__init__.py
--rw-r--r--   0        0        0     3844 2023-01-28 08:18:42.148875 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/azure.py
--rw-r--r--   0        0        0    11743 2023-01-20 09:58:42.388129 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/gcs.py
--rw-r--r--   0        0        0     1765 2023-02-21 17:11:35.686503 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/local.py
--rw-r--r--   0        0        0     6021 2023-01-28 08:18:42.149618 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/s3.py
--rw-r--r--   0        0        0     3770 2023-02-21 17:08:37.157751 airavata_mft_cli-0.1.8/airavata_mft_cli/storage/swift.py
--rw-r--r--   0        0        0     1576 2023-02-21 20:33:24.548839 airavata_mft_cli-0.1.8/pyproject.toml
--rw-r--r--   0        0        0     1933 1970-01-01 00:00:00.000000 airavata_mft_cli-0.1.8/setup.py
--rw-r--r--   0        0        0     1604 1970-01-01 00:00:00.000000 airavata_mft_cli-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0      799 2023-02-19 15:26:06.342141 airavata_mft_cli-0.1.9/README.md
+-rw-r--r--   0        0        0      788 2023-02-19 15:26:06.342265 airavata_mft_cli-0.1.9/airavata_mft_cli/__init__.py
+-rw-r--r--   0        0        0     1333 2023-03-21 13:11:54.895411 airavata_mft_cli-0.1.9/airavata_mft_cli/base.py
+-rw-r--r--   0        0        0     5501 2023-03-21 13:14:57.357983 airavata_mft_cli-0.1.9/airavata_mft_cli/bootstrap.py
+-rw-r--r--   0        0        0      212 2023-03-20 18:22:11.402284 airavata_mft_cli-0.1.9/airavata_mft_cli/config.py
+-rw-r--r--   0        0        0      994 2023-02-19 15:26:06.342495 airavata_mft_cli-0.1.9/airavata_mft_cli/main.py
+-rw-r--r--   0        0        0     9540 2023-03-19 14:22:04.115496 airavata_mft_cli-0.1.9/airavata_mft_cli/operations.py
+-rw-r--r--   0        0        0     3328 2023-03-21 01:12:16.167674 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/__init__.py
+-rw-r--r--   0        0        0     4110 2023-03-19 14:22:04.116407 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/azure.py
+-rw-r--r--   0        0        0    12009 2023-03-19 14:22:04.116657 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/gcs.py
+-rw-r--r--   0        0        0     2031 2023-03-19 14:22:04.116857 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/local.py
+-rw-r--r--   0        0        0     6287 2023-03-19 14:22:04.117057 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/s3.py
+-rw-r--r--   0        0        0     3361 2023-03-21 01:17:52.358939 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/scp.py
+-rw-r--r--   0        0        0     4036 2023-03-19 14:22:04.117241 airavata_mft_cli-0.1.9/airavata_mft_cli/storage/swift.py
+-rw-r--r--   0        0        0     1576 2023-03-21 13:15:23.317158 airavata_mft_cli-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0     1933 1970-01-01 00:00:00.000000 airavata_mft_cli-0.1.9/setup.py
+-rw-r--r--   0        0        0     1604 1970-01-01 00:00:00.000000 airavata_mft_cli-0.1.9/PKG-INFO
```

### Comparing `airavata_mft_cli-0.1.8/README.md` & `airavata_mft_cli-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/__init__.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/__init__.py`

 * *Files identical despite different names*

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/base.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/base.py`

 * *Files 22% similar despite different names*

```diff
@@ -32,8 +32,16 @@
 
 @app.command("init")
 def init_mft():
   bootstrap.start_mft()
 
 @app.command("stop")
 def init_mft():
-  bootstrap.stop_mft()
+  bootstrap.stop_mft()
+
+@app.command("update")
+def init_mft():
+  bootstrap.update_mft()
+
+@app.command("log")
+def init_mft():
+  bootstrap.print_log()
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/bootstrap.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/bootstrap.py`

 * *Files 8% similar despite different names*

```diff
@@ -20,14 +20,16 @@
 import requests
 import os
 import zipfile
 from subprocess import call
 from subprocess import Popen
 from pathlib import Path
 from sys import platform
+import shutil
+import time
 
 def download_and_unarchive(url, download_path, extract_dir = os.path.join(os.path.expanduser('~'), ".mft/")):
 
   response = requests.get(url, stream=True)
   file_size = int(response.headers['Content-Length'])
   with typer.progressbar(length=file_size) as progress:
     with open(download_path, "wb") as handle:
@@ -113,15 +115,15 @@
 
   restart_service(path + "/bin", "standalone-service-daemon.sh")
 
   print("MFT Started")
 
 
 def stop_mft():
-  print("Stopping up MFT Services")
+  print("Stopping MFT Services")
 
   path = os.path.join(os.path.expanduser('~'), ".mft/consul")
   if os.path.exists(path):
     current_dir =  os.getcwd()
     try:
       os.chdir(os.path.join(os.path.expanduser('~'), ".mft"))
       os.chmod("consul", 0o744)
@@ -134,10 +136,39 @@
 
   path = os.path.join(os.path.expanduser('~'), ".mft/Standalone-Service-0.01")
   if os.path.exists(path):
     stop_service(path + "/bin", "standalone-service-daemon.sh")
 
   print("MFT Stopped....")
 
+def update_mft():
+  stop_mft()
 
+  mft_dir = os.path.join(os.path.expanduser('~'), ".mft")
+  if os.path.exists(mft_dir):
+    print("Removing .mft directory")
+    shutil.rmtree(mft_dir)
+
+  database = os.path.join(os.path.expanduser('~'), "mft_db.mv.db")
+  if os.path.exists(database):
+    os.remove(database)
+  start_mft()
+
+def print_log():
+  log_file_path = os.path.join(os.path.expanduser('~'), ".mft", "Standalone-Service-0.01", "logs", "airavata.log")
+  log_file = open(log_file_path,"r")
+  lines = follow_file(log_file)
+  for line in lines:
+    print(line)
+
+def follow_file(file):
+  #file.seek(0, os.SEEK_END)
+
+  while True:
+    line = file.readline()
+    if not line:
+      time.sleep(0.1)
+      continue
+
+    yield line
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/main.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/main.py`

 * *Files identical despite different names*

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/operations.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/operations.py`

 * *Files 11% similar despite different names*

```diff
@@ -19,23 +19,26 @@
 import typer
 from airavata_mft_sdk import mft_client
 from airavata_mft_sdk.common import StorageCommon_pb2
 from airavata_mft_sdk import MFTTransferApi_pb2
 from rich.console import Console
 from rich.table import Table
 import time
+import sys
+sys.path.append('.')
+from . import config as configcli
 
 def fetch_storage_and_secret_ids(storage_name):
-  client = mft_client.MFTClient(transfer_api_port = 7003,
-                                transfer_api_secured = False,
-                                resource_service_host = "localhost",
-                                resource_service_port = 7003,
-                                resource_service_secured = False,
-                                secret_service_host = "localhost",
-                                secret_service_port = 7003)
+  client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                transfer_api_secured = configcli.transfer_api_secured,
+                                resource_service_host = configcli.resource_service_host,
+                                resource_service_port = configcli.resource_service_port,
+                                resource_service_secured = configcli.resource_service_secured,
+                                secret_service_host = configcli.secret_service_host,
+                                secret_service_port = configcli.secret_service_port)
   search_req = StorageCommon_pb2.StorageSearchRequest(storageName=storage_name)
   storages = client.common_api.searchStorages(search_req)
 
   if len(storages.storageList) == 0:
     search_req = StorageCommon_pb2.StorageSearchRequest(storageId=storage_name)
     storages = client.common_api.searchStorages(search_req)
 
@@ -64,21 +67,21 @@
   storage_id, secret_id = fetch_storage_and_secret_ids(storage_name)
 
   id_req = MFTTransferApi_pb2.GetResourceMetadataFromIDsRequest(storageId = storage_id,
                                                                 secretId = secret_id,
                                                                 resourcePath = resource_path)
   resource_medata_req = MFTTransferApi_pb2.FetchResourceMetadataRequest(idRequest = id_req)
 
-  client = mft_client.MFTClient(transfer_api_port = 7003,
-                                transfer_api_secured = False,
-                                resource_service_host = "localhost",
-                                resource_service_port = 7003,
-                                resource_service_secured = False,
-                                secret_service_host = "localhost",
-                                secret_service_port = 7003)
+  client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                transfer_api_secured = configcli.transfer_api_secured,
+                                resource_service_host = configcli.resource_service_host,
+                                resource_service_port = configcli.resource_service_port,
+                                resource_service_secured = configcli.resource_service_secured,
+                                secret_service_host = configcli.secret_service_host,
+                                secret_service_port = configcli.secret_service_port)
 
   metadata_resp = client.transfer_api.resourceMetadata(resource_medata_req)
   return metadata_resp
 
 def list(storage_path):
 
   metadata_resp = get_resource_metadata(storage_path)
@@ -163,26 +166,26 @@
 
   transfer_request.endpointPaths.extend(endpoint_paths)
 
   confirm = typer.confirm("Total number of " + str(len(endpoint_paths)) +
                           " files to be transferred. Total volume is " + str(total_volume)
                           + " bytes. Do you want to start the transfer? ", True)
 
-  client = mft_client.MFTClient(transfer_api_port = 7003,
-                                transfer_api_secured = False,
-                                resource_service_host = "localhost",
-                                resource_service_port = 7003,
-                                resource_service_secured = False,
-                                secret_service_host = "localhost",
-                                secret_service_port = 7003)
+  if not confirm:
+      raise typer.Abort()
 
-  transfer_resp = client.transfer_api.submitTransfer(transfer_request)
+  client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                transfer_api_secured = configcli.transfer_api_secured,
+                                resource_service_host = configcli.resource_service_host,
+                                resource_service_port = configcli.resource_service_port,
+                                resource_service_secured = configcli.resource_service_secured,
+                                secret_service_host = configcli.secret_service_host,
+                                secret_service_port = configcli.secret_service_port)
 
-  if not confirm:
-    raise typer.Abort()
+  transfer_resp = client.transfer_api.submitTransfer(transfer_request)
 
   transfer_id = transfer_resp.transferId
 
   state_request = MFTTransferApi_pb2.TransferStateApiRequest(transferId=transfer_id)
 
   ## TODO: This has to be optimized and avoid frequent polling of all transfer ids in each iteration
   ## Possible fix is to introduce a parent batch transfer id at the API level and fetch child trnasfer id
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/storage/__init__.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/storage/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -15,22 +15,26 @@
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 #
 import typer
 from pick import pick
 import airavata_mft_cli.storage.s3 as s3
+import airavata_mft_cli.storage.scp as scp
 import airavata_mft_cli.storage.azure as azure
 import airavata_mft_cli.storage.gcs as gcs
 import airavata_mft_cli.storage.local as local
 import airavata_mft_cli.storage.swift as swift
 from airavata_mft_sdk import mft_client
 from airavata_mft_sdk.common import StorageCommon_pb2
 from rich.console import Console
 from rich.table import Table
+import sys
+sys.path.append('../airavata_mft_cli')
+from airavata_mft_cli import config as configcli
 
 app = typer.Typer()
 
 @app.command("add")
 def add_storage():
     title = "Select storage type: "
     options = ["S3", "Google Cloud Storage (GCS)", "Azure Storage", "Openstack SWIFT", "SCP", "FTP", "Box", "DropBox", "OData", "Agent" ]
@@ -41,25 +45,27 @@
         azure.handle_add_storage()
     elif option == "Google Cloud Storage (GCS)":
         gcs.handle_add_storage()
     elif option == "Agent":
         local.handle_add_storage()
     elif option == "Openstack SWIFT":
         swift.handle_add_storage()
+    elif option == "SCP":
+        scp.handle_add_storage()
 
 
 @app.command("list")
 def list_storage():
-    client = mft_client.MFTClient(transfer_api_port = 7003,
-                                  transfer_api_secured = False,
-                                  resource_service_host = "localhost",
-                                  resource_service_port = 7003,
-                                  resource_service_secured = False,
-                                  secret_service_host = "localhost",
-                                  secret_service_port = 7003)
+    client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                  transfer_api_secured = configcli.transfer_api_secured,
+                                  resource_service_host = configcli.resource_service_host,
+                                  resource_service_port = configcli.resource_service_port,
+                                  resource_service_secured = configcli.resource_service_secured,
+                                  secret_service_host = configcli.secret_service_host,
+                                  secret_service_port = configcli.secret_service_port)
     list_req = StorageCommon_pb2.StorageListRequest()
     list_response = client.common_api.listStorages(list_req)
 
     console = Console()
     table = Table(show_header=True, header_style='bold #2070b2')
 
     table.add_column('Storage Name', justify='left')
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/storage/azure.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/storage/azure.py`

 * *Files 14% similar despite different names*

```diff
@@ -21,30 +21,33 @@
 import typer
 from airavata_mft_sdk import mft_client
 from airavata_mft_sdk.azure import AzureCredential_pb2
 from airavata_mft_sdk.azure import AzureStorage_pb2
 from airavata_mft_sdk import MFTTransferApi_pb2
 from airavata_mft_sdk import MFTAgentStubs_pb2
 from airavata_mft_sdk.common import StorageCommon_pb2
+import sys
+sys.path.append('../airavata_mft_cli')
+from airavata_mft_cli import config as configcli
 
 def handle_add_storage():
 
     options = ["Through Azure Cli config file", "Enter manually" ]
     option, index = pick(options, "How do you want to load credentials", indicator="=>")
 
     if index == 1: # Manual configuration
         connection_string = typer.prompt("Connection String")
 
-    client = mft_client.MFTClient(transfer_api_port = 7003,
-                                  transfer_api_secured = False,
-                                  resource_service_host = "localhost",
-                                  resource_service_port = 7003,
-                                  resource_service_secured = False,
-                                  secret_service_host = "localhost",
-                                  secret_service_port = 7003)
+    client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                  transfer_api_secured = configcli.transfer_api_secured,
+                                  resource_service_host = configcli.resource_service_host,
+                                  resource_service_port = configcli.resource_service_port,
+                                  resource_service_secured = configcli.resource_service_secured,
+                                  secret_service_host = configcli.secret_service_host,
+                                  secret_service_port = configcli.secret_service_port)
 
     azure_secret = AzureCredential_pb2.AzureSecret(connectionString = connection_string)
     secret_wrapper = MFTAgentStubs_pb2.SecretWrapper(azure=azure_secret)
 
     azure_storage = AzureStorage_pb2.AzureStorage()
     storage_wrapper = MFTAgentStubs_pb2.StorageWrapper(azure=azure_storage)
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/storage/gcs.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/storage/gcs.py`

 * *Files 5% similar despite different names*

```diff
@@ -26,14 +26,17 @@
 from airavata_mft_sdk.common import StorageCommon_pb2
 import json
 import configparser
 import os
 import base64
 import google.auth
 import googleapiclient.discovery
+import sys
+sys.path.append('../airavata_mft_cli')
+from airavata_mft_cli import config as configcli
 
 gcs_key_path = '.mft/keys/gcs/service_account_key.json'
 
 
 def handle_add_storage():
 
     options = ["Through Google Cloud SDK config file", "Enter manually"]
@@ -111,21 +114,21 @@
                 client_email = config_data['client_email']
                 project_id = config_data['project_id']
                 client_secret = config_data['private_key']
             else:
                 print("No credential found in ~/" + gcs_key_path + " file")
                 exit()
 
-    client = mft_client.MFTClient(transfer_api_port = 7003,
-                                  transfer_api_secured = False,
-                                  resource_service_host = "localhost",
-                                  resource_service_port = 7003,
-                                  resource_service_secured = False,
-                                  secret_service_host = "localhost",
-                                  secret_service_port = 7003)
+    client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                  transfer_api_secured = configcli.transfer_api_secured,
+                                  resource_service_host = configcli.resource_service_host,
+                                  resource_service_port = configcli.resource_service_port,
+                                  resource_service_secured = configcli.resource_service_secured,
+                                  secret_service_host = configcli.secret_service_host,
+                                  secret_service_port = configcli.secret_service_port)
 
     gcs_secret = GCSCredential_pb2.GCSSecret(clientEmail=client_email, privateKey=client_secret, projectId=project_id)
     secret_wrapper = MFTAgentStubs_pb2.SecretWrapper(gcs=gcs_secret)
 
     gcs_storage = GCSStorage_pb2.GCSStorage()
     storage_wrapper = MFTAgentStubs_pb2.StorageWrapper(gcs=gcs_storage)
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/storage/s3.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/storage/s3.py`

 * *Files 10% similar despite different names*

```diff
@@ -23,14 +23,17 @@
 from airavata_mft_sdk.s3 import S3Credential_pb2
 from airavata_mft_sdk.s3 import S3Storage_pb2
 from airavata_mft_sdk import MFTTransferApi_pb2
 from airavata_mft_sdk import MFTAgentStubs_pb2
 from airavata_mft_sdk.common import StorageCommon_pb2
 import configparser
 import os
+import sys
+sys.path.append('../airavata_mft_cli')
+from airavata_mft_cli import config as configcli
 
 def handle_add_storage():
 
     session_token = ""
     aws_regions = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-east-1",
                    "ap-southeast-3", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1",
                    "ap-southeast-2", "ap-northeast-1", "ca-central-1", "cn-north-1", "cn-northwest-1", "eu-central-1",
@@ -75,21 +78,21 @@
         client_secret = config.get(section, 'aws_secret_access_key')
         if config.has_option(section, 'aws_session_token'):
             session_token =  config.get(section, 'aws_session_token')
 
         region, index = pick(aws_regions, "Select the AWS Region", indicator="=>")
         endpoint = "https://s3." + region + ".amazonaws.com"
 
-    client = mft_client.MFTClient(transfer_api_port = 7003,
-                                  transfer_api_secured = False,
-                                  resource_service_host = "localhost",
-                                  resource_service_port = 7003,
-                                  resource_service_secured = False,
-                                  secret_service_host = "localhost",
-                                  secret_service_port = 7003)
+    client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                  transfer_api_secured = configcli.transfer_api_secured,
+                                  resource_service_host = configcli.resource_service_host,
+                                  resource_service_port = configcli.resource_service_port,
+                                  resource_service_secured = configcli.resource_service_secured,
+                                  secret_service_host = configcli.secret_service_host,
+                                  secret_service_port = configcli.secret_service_port)
 
     s3_secret = S3Credential_pb2.S3Secret(accessKey=client_id, secretKey=client_secret, sessionToken = session_token)
     secret_wrapper = MFTAgentStubs_pb2.SecretWrapper(s3=s3_secret)
 
     s3_storage = S3Storage_pb2.S3Storage(endpoint=endpoint, region=region)
     storage_wrapper = MFTAgentStubs_pb2.StorageWrapper(s3=s3_storage)
```

### Comparing `airavata_mft_cli-0.1.8/airavata_mft_cli/storage/swift.py` & `airavata_mft_cli-0.1.9/airavata_mft_cli/storage/swift.py`

 * *Files 8% similar despite different names*

```diff
@@ -19,14 +19,17 @@
 from rich import print
 from pick import pick
 import typer
 from airavata_mft_sdk import mft_client
 from airavata_mft_sdk.swift import SwiftCredential_pb2
 from airavata_mft_sdk.swift import SwiftStorage_pb2
 from airavata_mft_sdk.common import StorageCommon_pb2
+import sys
+sys.path.append('../airavata_mft_cli')
+from airavata_mft_cli import config as configcli
 
 def handle_add_storage():
 
     options = ["v3", "v2" ]
     option, index = pick(options, "Select Keystone Auth Version", indicator="=>")
 
     secret_create_req= SwiftCredential_pb2.SwiftSecretCreateRequest()
@@ -52,21 +55,21 @@
     secret_create_req.endpoint = auth_url
 
     region_name = typer.prompt("Region Name")
     container = typer.prompt("Container")
 
     storage_name = typer.prompt("Name of the storage ", container)
 
-    client = mft_client.MFTClient(transfer_api_port = 7003,
-                                  transfer_api_secured = False,
-                                  resource_service_host = "localhost",
-                                  resource_service_port = 7003,
-                                  resource_service_secured = False,
-                                  secret_service_host = "localhost",
-                                  secret_service_port = 7003)
+    client = mft_client.MFTClient(transfer_api_port = configcli.transfer_api_port,
+                                  transfer_api_secured = configcli.transfer_api_secured,
+                                  resource_service_host = configcli.resource_service_host,
+                                  resource_service_port = configcli.resource_service_port,
+                                  resource_service_secured = configcli.resource_service_secured,
+                                  secret_service_host = configcli.secret_service_host,
+                                  secret_service_port = configcli.secret_service_port)
 
 
     swift_storage_create_req = SwiftStorage_pb2.SwiftStorageCreateRequest(region=region_name,
                                                                           container=container,
                                                                           name=storage_name)
 
     created_storage = client.swift_storage_api.createSwiftStorage(swift_storage_create_req)
```

### Comparing `airavata_mft_cli-0.1.8/pyproject.toml` & `airavata_mft_cli-0.1.9/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -14,26 +14,26 @@
 # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 [tool.poetry]
 name = "airavata-mft-cli"
-version = "0.1.8"
+version = "0.1.9"
 description = "Command Line Client for Airavata MFT data transfer software"
 authors = ["Apache Airavata <dev@apache.airavata.org>"]
 readme = "README.md"
 
 [tool.poetry.scripts]
 mft = "airavata_mft_cli.main:app"
 
 [tool.poetry.dependencies]
 python = "^3.10"
 typer = {extras = ["all"], version = "^0.7.0"}
 pick = {version= "2.2.0"}
 grpcio= [{version="1.46.3", markers = "platform_machine != 'arm64'"},{version="1.47.0rc1", markers = "platform_machine == 'arm64'"}]
 grpcio-tools = [{version="1.46.3", markers = "platform_machine != 'arm64'"},{version="1.47.0rc1", markers = "platform_machine == 'arm64'"}]
-airavata_mft_sdk= {version="0.0.1-alpha26"}
+airavata_mft_sdk= {version="0.0.1-alpha27"}
 
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `airavata_mft_cli-0.1.8/setup.py` & `airavata_mft_cli-0.1.9/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -4,27 +4,27 @@
 packages = \
 ['airavata_mft_cli', 'airavata_mft_cli.storage']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['airavata_mft_sdk==0.0.1-alpha26', 'pick==2.2.0', 'typer[all]>=0.7.0,<0.8.0']
+['airavata_mft_sdk==0.0.1-alpha27', 'pick==2.2.0', 'typer[all]>=0.7.0,<0.8.0']
 
 extras_require = \
 {':platform_machine != "arm64"': ['grpcio==1.46.3', 'grpcio-tools==1.46.3'],
  ':platform_machine == "arm64"': ['grpcio==1.47.0rc1',
                                   'grpcio-tools==1.47.0rc1']}
 
 entry_points = \
 {'console_scripts': ['mft = airavata_mft_cli.main:app']}
 
 setup_kwargs = {
     'name': 'airavata-mft-cli',
-    'version': '0.1.8',
+    'version': '0.1.9',
     'description': 'Command Line Client for Airavata MFT data transfer software',
     'long_description': '<!--\nLicensed to the Apache Software Foundation (ASF) under one\nor more contributor license agreements.  See the NOTICE file\ndistributed with this work for additional information\nregarding copyright ownership.  The ASF licenses this file\nto you under the Apache License, Version 2.0 (the\n"License"); you may not use this file except in compliance\nwith the License.  You may obtain a copy of the License at\n\n  http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing,\nsoftware distributed under the License is distributed on an\n"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\nKIND, either express or implied.  See the License for the\nspecific language governing permissions and limitations\nunder the License.\n-->\n\n# Airavata MFT Command Line Client',
     'author': 'Apache Airavata',
     'author_email': 'dev@apache.airavata.org',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `airavata_mft_cli-0.1.8/PKG-INFO` & `airavata_mft_cli-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: airavata-mft-cli
-Version: 0.1.8
+Version: 0.1.9
 Summary: Command Line Client for Airavata MFT data transfer software
 Author: Apache Airavata
 Author-email: dev@apache.airavata.org
 Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
-Requires-Dist: airavata_mft_sdk (==0.0.1-alpha26)
+Requires-Dist: airavata_mft_sdk (==0.0.1-alpha27)
 Requires-Dist: grpcio (==1.46.3) ; platform_machine != "arm64"
 Requires-Dist: grpcio (==1.47.0rc1) ; platform_machine == "arm64"
 Requires-Dist: grpcio-tools (==1.46.3) ; platform_machine != "arm64"
 Requires-Dist: grpcio-tools (==1.47.0rc1) ; platform_machine == "arm64"
 Requires-Dist: pick (==2.2.0)
 Requires-Dist: typer[all] (>=0.7.0,<0.8.0)
 Description-Content-Type: text/markdown
```

