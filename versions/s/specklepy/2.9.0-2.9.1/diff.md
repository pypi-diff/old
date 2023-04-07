# Comparing `tmp/specklepy-2.9.0.tar.gz` & `tmp/specklepy-2.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "specklepy-2.9.0.tar", max compression
+gzip compressed data, was "specklepy-2.9.1.tar", max compression
```

## Comparing `specklepy-2.9.0.tar` & `specklepy-2.9.1.tar`

### file list

```diff
@@ -1,50 +1,52 @@
--rw-r--r--   0        0        0    11341 2022-10-12 13:28:58.013000 specklepy-2.9.0/LICENSE
--rw-r--r--   0        0        0     6177 2022-10-12 13:28:58.013000 specklepy-2.9.0/README.md
--rw-r--r--   0        0        0     1071 2022-10-12 13:28:58.137000 specklepy-2.9.0/pyproject.toml
--rw-r--r--   0        0        0        0 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/__init__.py
--rw-r--r--   0        0        0     7509 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/client.py
--rw-r--r--   0        0        0     4313 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/credentials.py
--rw-r--r--   0        0        0     3361 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/host_applications.py
--rw-r--r--   0        0        0     4621 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/models.py
--rw-r--r--   0        0        0     4806 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/operations.py
--rw-r--r--   0        0        0     4556 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resource.py
--rw-r--r--   0        0        0      316 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/__init__.py
--rw-r--r--   0        0        0     7101 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/branch.py
--rw-r--r--   0        0        0     7586 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/commit.py
--rw-r--r--   0        0        0     2683 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/object.py
--rw-r--r--   0        0        0     5224 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/server.py
--rw-r--r--   0        0        0    26190 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/stream.py
--rw-r--r--   0        0        0     4262 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/subscriptions.py
--rw-r--r--   0        0        0     9400 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/resources/user.py
--rw-r--r--   0        0        0     6265 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/api/wrapper.py
--rw-r--r--   0        0        0        0 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/logging/__init__.py
--rw-r--r--   0        0        0     1654 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/logging/exceptions.py
--rw-r--r--   0        0        0     4251 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/logging/metrics.py
--rw-r--r--   0        0        0       95 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/__init__.py
--rw-r--r--   0        0        0    14339 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/base.py
--rw-r--r--   0        0        0     3830 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/encoding.py
--rw-r--r--   0        0        0     1247 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/fakemesh.py
--rw-r--r--   0        0        0    25172 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/geometry.py
--rw-r--r--   0        0        0     6588 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/other.py
--rw-r--r--   0        0        0      857 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/__init__.py
--rw-r--r--   0        0        0     1301 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/analysis.py
--rw-r--r--   0        0        0      192 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/axis.py
--rw-r--r--   0        0        0     2449 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/geometry.py
--rw-r--r--   0        0        0     2757 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/loading.py
--rw-r--r--   0        0        0     1399 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/material.py
--rw-r--r--   0        0        0     4406 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/properties.py
--rw-r--r--   0        0        0     4517 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/structural/results.py
--rw-r--r--   0        0        0     1913 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/objects/units.py
--rw-r--r--   0        0        0      841 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/paths.py
--rw-r--r--   0        0        0        0 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/serialization/__init__.py
--rw-r--r--   0        0        0    15119 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/serialization/base_object_serializer.py
--rw-r--r--   0        0        0        0 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/__init__.py
--rw-r--r--   0        0        0     2729 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/abstract_transport.py
--rw-r--r--   0        0        0     1263 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/memory.py
--rw-r--r--   0        0        0       36 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/server/__init__.py
--rw-r--r--   0        0        0     5205 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/server/batch_sender.py
--rw-r--r--   0        0        0     5806 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/server/server.py
--rw-r--r--   0        0        0     6780 2022-10-12 13:28:58.017001 specklepy-2.9.0/specklepy/transports/sqlite.py
--rw-r--r--   0        0        0     7254 1970-01-01 00:00:00.000000 specklepy-2.9.0/setup.py
--rw-r--r--   0        0        0     7082 1970-01-01 00:00:00.000000 specklepy-2.9.0/PKG-INFO
+-rw-r--r--   0        0        0    11341 2022-11-02 11:36:38.984993 specklepy-2.9.1/LICENSE
+-rw-r--r--   0        0        0     6177 2022-11-02 11:36:38.984993 specklepy-2.9.1/README.md
+-rw-r--r--   0        0        0     1134 2022-11-02 11:36:39.296993 specklepy-2.9.1/pyproject.toml
+-rw-r--r--   0        0        0        0 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/__init__.py
+-rw-r--r--   0        0        0     7901 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/client.py
+-rw-r--r--   0        0        0     4664 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/credentials.py
+-rw-r--r--   0        0        0     3358 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/host_applications.py
+-rw-r--r--   0        0        0     4950 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/models.py
+-rw-r--r--   0        0        0     4806 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/operations.py
+-rw-r--r--   0        0        0     4556 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resource.py
+-rw-r--r--   0        0        0      316 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/__init__.py
+-rw-r--r--   0        0        0     8144 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/active_user.py
+-rw-r--r--   0        0        0     7101 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/branch.py
+-rw-r--r--   0        0        0     7586 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/commit.py
+-rw-r--r--   0        0        0     2683 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/object.py
+-rw-r--r--   0        0        0     5384 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/other_user.py
+-rw-r--r--   0        0        0     5224 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/server.py
+-rw-r--r--   0        0        0    26190 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/stream.py
+-rw-r--r--   0        0        0     4262 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/subscriptions.py
+-rw-r--r--   0        0        0    10159 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/resources/user.py
+-rw-r--r--   0        0        0     6265 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/api/wrapper.py
+-rw-r--r--   0        0        0        0 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/logging/__init__.py
+-rw-r--r--   0        0        0     1654 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/logging/exceptions.py
+-rw-r--r--   0        0        0     4332 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/logging/metrics.py
+-rw-r--r--   0        0        0       95 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/__init__.py
+-rw-r--r--   0        0        0    14339 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/base.py
+-rw-r--r--   0        0        0     3830 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/encoding.py
+-rw-r--r--   0        0        0     1247 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/fakemesh.py
+-rw-r--r--   0        0        0    25172 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/geometry.py
+-rw-r--r--   0        0        0     6588 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/other.py
+-rw-r--r--   0        0        0      857 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/__init__.py
+-rw-r--r--   0        0        0     1301 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/analysis.py
+-rw-r--r--   0        0        0      192 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/axis.py
+-rw-r--r--   0        0        0     2449 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/geometry.py
+-rw-r--r--   0        0        0     2757 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/loading.py
+-rw-r--r--   0        0        0     1399 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/material.py
+-rw-r--r--   0        0        0     4406 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/properties.py
+-rw-r--r--   0        0        0     4517 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/structural/results.py
+-rw-r--r--   0        0        0     1913 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/objects/units.py
+-rw-r--r--   0        0        0      841 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/paths.py
+-rw-r--r--   0        0        0        0 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/serialization/__init__.py
+-rw-r--r--   0        0        0    15119 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/serialization/base_object_serializer.py
+-rw-r--r--   0        0        0        0 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/__init__.py
+-rw-r--r--   0        0        0     2731 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/abstract_transport.py
+-rw-r--r--   0        0        0     1263 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/memory.py
+-rw-r--r--   0        0        0       36 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/server/__init__.py
+-rw-r--r--   0        0        0     5205 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/server/batch_sender.py
+-rw-r--r--   0        0        0     5806 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/server/server.py
+-rw-r--r--   0        0        0     6740 2022-11-02 11:36:38.988993 specklepy-2.9.1/src/specklepy/transports/sqlite.py
+-rw-r--r--   0        0        0     7315 1970-01-01 00:00:00.000000 specklepy-2.9.1/setup.py
+-rw-r--r--   0        0        0     7133 1970-01-01 00:00:00.000000 specklepy-2.9.1/PKG-INFO
```

### Comparing `specklepy-2.9.0/LICENSE` & `specklepy-2.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/README.md` & `specklepy-2.9.1/README.md`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/pyproject.toml` & `specklepy-2.9.1/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,37 +1,39 @@
 [tool.poetry]
 name = "specklepy"
-version = "2.9.0"
+version = "2.9.1"
 description = "The Python SDK for Speckle 2.0"
 readme = "README.md"
 authors = ["Speckle Systems <devops@speckle.systems>"]
 license = "Apache-2.0"
 repository = "https://github.com/specklesystems/speckle-py"
 documentation = "https://speckle.guide/dev/py-examples.html"
 homepage = "https://speckle.systems/"
+packages = [
+  { include = "specklepy", from = "src" },
+]
 
 
 [tool.poetry.dependencies]
 python = ">=3.7.2, <4.0"
 pydantic = "^1.8.2"
 appdirs = "^1.4.4"
 gql = {extras = ["requests", "websockets"], version = "^3.3.0"}
 ujson = "^5.3.0"
 Deprecated = "^1.2.13"
 
-[tool.poetry.dev-dependencies]
+[tool.poetry.group.dev.dependencies]
 black = "^22.8.0"
 isort = "^5.7.0"
-pytest = "^6.2.2"
+pytest = "^7.1.3"
 pytest-ordering = "^0.6"
 pytest-cov = "^3.0.0"
 devtools = "^0.8.0"
 pylint = "^2.14.4"
-mypy = "^0.971"
-
+mypy = "^0.982"
 
 [tool.black]
 exclude = '''
 /(
     \.eggs
   | \.git
   | \.hg
```

### Comparing `specklepy-2.9.0/specklepy/api/client.py` & `specklepy-2.9.1/src/specklepy/api/client.py`

 * *Files 12% similar despite different names*

```diff
@@ -14,16 +14,17 @@
     branch,
     commit,
     stream,
     object,
     server,
     user,
     subscriptions,
+    other_user,
+    active_user
 )
-from specklepy.api.models import ServerInfo
 from gql import Client
 from gql.transport.requests import RequestsHTTPTransport
 from gql.transport.websockets import WebsocketsTransport
 
 
 class SpeckleClient:
     """
@@ -172,14 +173,26 @@
             pass
         self.user = user.Resource(
             account=self.account,
             basepath=self.url,
             client=self.httpclient,
             server_version=server_version,
         )
+        self.other_user = other_user.Resource(
+            account=self.account,
+            basepath=self.url,
+            client=self.httpclient,
+            server_version=server_version,
+        )
+        self.active_user = active_user.Resource(
+            account=self.account,
+            basepath=self.url,
+            client=self.httpclient,
+            server_version=server_version,
+        )
         self.stream = stream.Resource(
             account=self.account,
             basepath=self.url,
             client=self.httpclient,
             server_version=server_version,
         )
         self.commit = commit.Resource(
```

### Comparing `specklepy-2.9.0/specklepy/api/credentials.py` & `specklepy-2.9.1/src/specklepy/api/credentials.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 import os
 from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module
 from typing import List, Optional
 from specklepy.logging import metrics
 from specklepy.api.models import ServerInfo
 from specklepy.transports.sqlite import SQLiteTransport
 from specklepy.logging.exceptions import SpeckleException
+from specklepy import paths
 
 
 class UserInfo(BaseModel):
-    name: Optional[str]
-    email: Optional[str]
-    company: Optional[str]
-    id: Optional[str]
+    name: Optional[str] = None
+    email: Optional[str] = None
+    company: Optional[str] = None
+    id: Optional[str] = None
 
 
 class Account(BaseModel):
     isDefault: bool = False
     token: Optional[str] = None
     refreshToken: Optional[str] = None
     serverInfo: ServerInfo = Field(default_factory=ServerInfo)
@@ -31,35 +32,47 @@
     @classmethod
     def from_token(cls, token: str, server_url: str = None):
         acct = cls(token=token)
         acct.serverInfo.url = server_url
         return acct
 
 
-def get_local_accounts(base_path: str = None) -> List[Account]:
+def get_local_accounts(base_path: Optional[str] = None) -> List[Account]:
     """Gets all the accounts present in this environment
 
     Arguments:
         base_path {str} -- custom base path if you are not using the system default
 
     Returns:
         List[Account] -- list of all local accounts or an empty list if no accounts were found
     """
-    account_storage = SQLiteTransport(scope="Accounts", base_path=base_path)
-    # pylint: disable=protected-access
-    json_path = os.path.join(account_storage._base_path, "Accounts")
-    os.makedirs(json_path, exist_ok=True)
-    json_acct_files = [file for file in os.listdir(json_path) if file.endswith(".json")]
-
     accounts: List[Account] = []
-    res = account_storage.get_all_objects()
-    account_storage.close()
+    try:
+        account_storage = SQLiteTransport(scope="Accounts", base_path=base_path)
+        res = account_storage.get_all_objects()
+        account_storage.close()
+        if res:
+            accounts.extend(Account.parse_raw(r[1]) for r in res)
+    except SpeckleException:
+        # cannot open SQLiteTransport, probably because of the lack
+        # of disk write permissions
+        pass
+
+    json_acct_files = []
+    json_path = paths.accounts_path()
+    try:
+        os.makedirs(json_path, exist_ok=True)
+        json_acct_files.extend(
+            file for file in os.listdir(json_path) if file.endswith(".json")
+        )
+    
+    except Exception:
+        # cannot find or get the json account paths
+        pass
 
-    if res:
-        accounts.extend(Account.parse_raw(r[1]) for r in res)
     if json_acct_files:
         try:
             accounts.extend(
                 Account.parse_file(os.path.join(json_path, json_file))
                 for json_file in json_acct_files
             )
         except Exception as ex:
@@ -75,15 +88,15 @@
             accounts[0] if accounts else None,
         ),
     )
 
     return accounts
 
 
-def get_default_account(base_path: str = None) -> Account:
+def get_default_account(base_path: Optional[str] = None) -> Optional[Account]:
     """Gets this environment's default account if any. If there is no default, the first found will be returned and set as default.
     Arguments:
         base_path {str} -- custom base path if you are not using the system default
 
     Returns:
         Account -- the default account or None if no local accounts were found
     """
```

### Comparing `specklepy-2.9.0/specklepy/api/host_applications.py` & `specklepy-2.9.1/src/specklepy/api/host_applications.py`

 * *Files 1% similar despite different names*

```diff
@@ -35,14 +35,15 @@
 class HostApplication:
     name: str
     slug: str
 
     def get_version(self, version: HostAppVersion) -> str:
         return f"{name.replace(' ', '')}{str(version).strip('v')}"
 
+
 RHINO = HostApplication("Rhino", "rhino")
 GRASSHOPPER = HostApplication("Grasshopper", "grasshopper")
 REVIT = HostApplication("Revit", "revit")
 DYNAMO = HostApplication("Dynamo", "dynamo")
 UNITY = HostApplication("Unity", "unity")
 GSA = HostApplication("GSA", "gsa")
 CIVIL = HostApplication("Civil 3D", "civil3d")
@@ -95,20 +96,21 @@
     "blender": BLENDER,
     "qgis": QGIS,
     "arcgis": ARCGIS,
     "sketchup": SKETCHUP,
     "archicad": ARCHICAD,
     "topsolid": TOPSOLID,
     "python": PYTHON,
-    "net": NET
+    "net": NET,
 }
 
+
 def get_host_app_from_string(app_name: str) -> HostApplication:
     app_name = app_name.lower().replace(" ", "")
     for partial_app_name, host_app in _app_name_host_app_mapping.items():
-        if (partial_app_name in app_name):
+        if partial_app_name in app_name:
             return host_app
     return HostApplication(app_name, app_name)
-    
+
 
 if __name__ == "__main__":
     print(HostAppVersion.v)
```

### Comparing `specklepy-2.9.0/specklepy/api/models.py` & `specklepy-2.9.1/src/specklepy/api/models.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,12 @@
-# generated by datamodel-codegen:
-#   filename:  stream_schema.json
-#   timestamp: 2020-11-17T14:33:13+00:00
-
 from datetime import datetime
 from typing import List, Optional
 
 
-from pydantic import BaseModel  # pylint: disable=no-name-in-module
+from pydantic import BaseModel, Field
 
 
 class Collaborator(BaseModel):
     id: Optional[str]
     name: Optional[str]
     role: Optional[str]
     avatar: Optional[str]
@@ -60,28 +56,28 @@
 class Branches(BaseModel):
     totalCount: Optional[int]
     cursor: Optional[datetime]
     items: List[Branch] = []
 
 
 class Stream(BaseModel):
-    id: Optional[str]
+    id: Optional[str] = None 
     name: Optional[str]
-    role: Optional[str]
-    isPublic: Optional[bool]
-    description: Optional[str]
-    createdAt: Optional[datetime]
-    updatedAt: Optional[datetime]
-    collaborators: List[Collaborator] = []
-    branches: Optional[Branches]
-    commit: Optional[Commit]
-    object: Optional[Object]
-    commentCount: Optional[int]
-    favoritedDate: Optional[datetime]
-    favoritesCount: Optional[int]
+    role: Optional[str] = None
+    isPublic: Optional[bool] = None
+    description: Optional[str] = None
+    createdAt: Optional[datetime] = None 
+    updatedAt: Optional[datetime] = None 
+    collaborators: List[Collaborator] = Field(default_factory=list)
+    branches: Optional[Branches] = None 
+    commit: Optional[Commit] = None 
+    object: Optional[Object] = None 
+    commentCount: Optional[int] = None 
+    favoritedDate: Optional[datetime] = None 
+    favoritesCount: Optional[int] = None 
 
     def __repr__(self):
         return f"Stream( id: {self.id}, name: {self.name}, description: {self.description}, isPublic: {self.isPublic})"
 
     def __str__(self) -> str:
         return self.__repr__()
 
@@ -106,14 +102,26 @@
     def __repr__(self):
         return f"User( id: {self.id}, name: {self.name}, email: {self.email}, company: {self.company} )"
 
     def __str__(self) -> str:
         return self.__repr__()
 
 
+class LimitedUser(BaseModel):
+    """Limited user type, for showing public info about a user to another user."""
+
+    id: str
+    name: Optional[str]
+    bio: Optional[str]
+    company: Optional[str]
+    avatar: Optional[str]
+    verified: Optional[bool]
+    role: Optional[str]
+
+
 class PendingStreamCollaborator(BaseModel):
     id: Optional[str]
     inviteId: Optional[str]
     streamId: Optional[str]
     streamName: Optional[str]
     title: Optional[str]
     role: Optional[str]
@@ -154,17 +162,17 @@
         return f"ActivityCollection( totalCount: {self.totalCount}, items: {len(self.items) if self.items else 0}, cursor: {self.cursor.isoformat() if self.cursor else None} )"
 
     def __str__(self) -> str:
         return self.__repr__()
 
 
 class ServerInfo(BaseModel):
-    name: Optional[str]
-    company: Optional[str]
-    url: Optional[str]
-    description: Optional[str]
-    adminContact: Optional[str]
-    canonicalUrl: Optional[str]
-    roles: Optional[List[dict]]
-    scopes: Optional[List[dict]]
-    authStrategies: Optional[List[dict]]
-    version: Optional[str]
+    name: Optional[str] = None
+    company: Optional[str] = None
+    url: Optional[str] = None
+    description: Optional[str] = None
+    adminContact: Optional[str] = None
+    canonicalUrl: Optional[str] = None
+    roles: Optional[List[dict]] = None
+    scopes: Optional[List[dict]] = None
+    authStrategies: Optional[List[dict]] = None
+    version: Optional[str] = None
```

### Comparing `specklepy-2.9.0/specklepy/api/operations.py` & `specklepy-2.9.1/src/specklepy/api/operations.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resource.py` & `specklepy-2.9.1/src/specklepy/api/resource.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/branch.py` & `specklepy-2.9.1/src/specklepy/api/resources/branch.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/commit.py` & `specklepy-2.9.1/src/specklepy/api/resources/commit.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/object.py` & `specklepy-2.9.1/src/specklepy/api/resources/object.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/server.py` & `specklepy-2.9.1/src/specklepy/api/resources/server.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/stream.py` & `specklepy-2.9.1/src/specklepy/api/resources/stream.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/subscriptions.py` & `specklepy-2.9.1/src/specklepy/api/resources/subscriptions.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/api/resources/user.py` & `specklepy-2.9.1/src/specklepy/api/resources/user.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,33 +1,42 @@
 from typing import List, Optional, Union
 from datetime import datetime, timezone
 from gql import gql
 from specklepy.logging import metrics
 from specklepy.logging.exceptions import SpeckleException
 from specklepy.api.resource import ResourceBase
 from specklepy.api.models import ActivityCollection, PendingStreamCollaborator, User
+from deprecated import deprecated
+
 
 NAME = "user"
 
+DEPRECATION_VERSION = "2.9.0"
+DEPRECATION_TEXT = "The user resource is deprecated, please use the active_user or other_user resources"
+
 
 class Resource(ResourceBase):
     """API Access class for users"""
 
     def __init__(self, account, basepath, client, server_version) -> None:
         super().__init__(
             account=account,
             basepath=basepath,
             client=client,
             name=NAME,
             server_version=server_version,
         )
         self.schema = User
 
-    def get(self, id: str = None) -> User:
-        """Gets the profile of a user. If no id argument is provided, will return the current authenticated user's profile (as extracted from the authorization header).
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
+    def get(self, id: Optional[str] = None) -> User:
+        """
+        Gets the profile of a user.
+        If no id argument is provided, will return the current authenticated
+        user's profile (as extracted from the authorization header).
 
         Arguments:
             id {str} -- the user id
 
         Returns:
             User -- the retrieved user
         """
@@ -50,14 +59,15 @@
           """
         )
 
         params = {"id": id}
 
         return self.make_request(query=query, params=params, return_type="user")
 
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
     def search(
         self, search_query: str, limit: int = 25
     ) -> Union[List[User], SpeckleException]:
         """Searches for user by name or email. The search query must be at least 3 characters long
 
         Arguments:
             search_query {str} -- a string to search for
@@ -89,16 +99,21 @@
         )
         params = {"search_query": search_query, "limit": limit}
 
         return self.make_request(
             query=query, params=params, return_type=["userSearch", "items"]
         )
 
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
     def update(
-        self, name: str = None, company: str = None, bio: str = None, avatar: str = None
+        self,
+        name: Optional[str] = None,
+        company: Optional[str] = None,
+        bio: Optional[str] = None,
+        avatar: Optional[str] = None,
     ):
         """Updates your user profile. All arguments are optional.
 
         Arguments:
             name {str} -- your name
             company {str} -- the company you may or may not work for
             bio {str} -- tell us about yourself
@@ -124,22 +139,23 @@
                 message="You must provide at least one field to update your user profile"
             )
 
         return self.make_request(
             query=query, params=params, return_type="userUpdate", parse_response=False
         )
 
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
     def activity(
         self,
-        user_id: str = None,
+        user_id: Optional[str] = None,
         limit: int = 20,
-        action_type: str = None,
-        before: datetime = None,
-        after: datetime = None,
-        cursor: datetime = None,
+        action_type: Optional[str] = None,
+        before: Optional[datetime] = None,
+        after: Optional[datetime] = None,
+        cursor: Optional[datetime] = None,
     ):
         """
         Get the activity from a given stream in an Activity collection. Step into the activity `items` for the list of activity.
         If no id argument is provided, will return the current authenticated user's activity (as extracted from the authorization header).
 
         Note: all timestamps arguments should be `datetime` of any tz as they will be converted to UTC ISO format strings
 
@@ -186,14 +202,15 @@
         return self.make_request(
             query=query,
             params=params,
             return_type=["user", "activity"],
             schema=ActivityCollection,
         )
 
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
     def get_all_pending_invites(self) -> List[PendingStreamCollaborator]:
         """Get all of the active user's pending stream invites
 
         Requires Speckle Server version >= 2.6.4
 
         Returns:
             List[PendingStreamCollaborator] -- a list of pending invites for the current user
@@ -225,16 +242,17 @@
 
         return self.make_request(
             query=query,
             return_type="streamInvites",
             schema=PendingStreamCollaborator,
         )
 
+    @deprecated(version=DEPRECATION_VERSION, reason=DEPRECATION_TEXT)
     def get_pending_invite(
-        self, stream_id: str, token: str = None
+        self, stream_id: str, token: Optional[str] = None
     ) -> Optional[PendingStreamCollaborator]:
         """Get a particular pending invite for the active user on a given stream.
         If no invite_id is provided, any valid invite will be returned.
 
         Requires Speckle Server version >= 2.6.4
 
         Arguments:
```

### Comparing `specklepy-2.9.0/specklepy/api/wrapper.py` & `specklepy-2.9.1/src/specklepy/api/wrapper.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/logging/exceptions.py` & `specklepy-2.9.1/src/specklepy/logging/exceptions.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/logging/metrics.py` & `specklepy-2.9.1/src/specklepy/logging/metrics.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import sys
 import queue
 import hashlib
 import getpass
 import logging
+from typing import Optional
 import requests
 import threading
 import platform
 import contextlib
 
 
 """
@@ -26,14 +27,15 @@
 SEND = "Send"
 STREAM = "Stream Action"
 PERMISSION = "Permission Action"
 INVITE = "Invite Action"
 COMMIT = "Commit Action"
 BRANCH = "Branch Action"
 USER = "User Action"
+OTHER_USER = "Other User Action"
 SERVER = "Server Action"
 CLIENT = "Speckle Client"
 STREAM_WRAPPER = "Stream Wrapper"
 
 ACCOUNTS = "Get Local Accounts"
 
 SERIALIZE = "serialization/serialize"
@@ -46,21 +48,21 @@
 
 
 def enable():
     global TRACK
     TRACK = True
 
 
-def set_host_app(host_app: str, host_app_version: str = None):
+def set_host_app(host_app: str, host_app_version: Optional[str] = None):
     global HOST_APP, HOST_APP_VERSION
     HOST_APP = host_app
     HOST_APP_VERSION = host_app_version or HOST_APP_VERSION
 
 
-def track(action: str, account: "Account" = None, custom_props: dict = None):
+def track(action: str, account: "Account" = None, custom_props: Optional[dict] = None):
     if not TRACK:
         return
     try:
         initialise_tracker(account)
         event_params = {
             "event": action,
             "properties": {
```

### Comparing `specklepy-2.9.0/specklepy/objects/base.py` & `specklepy-2.9.1/src/specklepy/objects/base.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/encoding.py` & `specklepy-2.9.1/src/specklepy/objects/encoding.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/fakemesh.py` & `specklepy-2.9.1/src/specklepy/objects/fakemesh.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/geometry.py` & `specklepy-2.9.1/src/specklepy/objects/geometry.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/other.py` & `specklepy-2.9.1/src/specklepy/objects/other.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/__init__.py` & `specklepy-2.9.1/src/specklepy/objects/structural/__init__.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/analysis.py` & `specklepy-2.9.1/src/specklepy/objects/structural/analysis.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/geometry.py` & `specklepy-2.9.1/src/specklepy/objects/structural/geometry.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/loading.py` & `specklepy-2.9.1/src/specklepy/objects/structural/loading.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/material.py` & `specklepy-2.9.1/src/specklepy/objects/structural/material.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/properties.py` & `specklepy-2.9.1/src/specklepy/objects/structural/properties.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/structural/results.py` & `specklepy-2.9.1/src/specklepy/objects/structural/results.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/objects/units.py` & `specklepy-2.9.1/src/specklepy/objects/units.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/paths.py` & `specklepy-2.9.1/src/specklepy/paths.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/serialization/base_object_serializer.py` & `specklepy-2.9.1/src/specklepy/serialization/base_object_serializer.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/transports/abstract_transport.py` & `specklepy-2.9.1/src/specklepy/transports/abstract_transport.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from abc import ABC, abstractmethod
 from typing import Optional, List, Dict
 from pydantic import BaseModel
-from pydantic.main import Extra
+from pydantic.config import Extra
 
 #  __________________
 # |                  |
 # |  this is v wip   |
 # |  pls be careful  |
 # |__________________|
 # (\__/) ||
```

### Comparing `specklepy-2.9.0/specklepy/transports/memory.py` & `specklepy-2.9.1/src/specklepy/transports/memory.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/transports/server/batch_sender.py` & `specklepy-2.9.1/src/specklepy/transports/server/batch_sender.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/transports/server/server.py` & `specklepy-2.9.1/src/specklepy/transports/server/server.py`

 * *Files identical despite different names*

### Comparing `specklepy-2.9.0/specklepy/transports/sqlite.py` & `specklepy-2.9.1/src/specklepy/transports/sqlite.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,10 @@
 import os
-import sys
-import time
-import sched
 import sqlite3
-from typing import Any, List, Dict, Tuple
-from appdirs import user_data_dir
+from typing import Any, List, Dict, Optional, Tuple
 from contextlib import closing
 from specklepy.transports.abstract_transport import AbstractTransport
 from specklepy.logging.exceptions import SpeckleException
 from specklepy.paths import base_path
 
 
 class SQLiteTransport(AbstractTransport):
@@ -21,16 +17,16 @@
     saved_obj_count: int = 0
     max_size: int = None
     _current_batch: List[Tuple[str, str]] = None
     _current_batch_size: int = None
 
     def __init__(
         self,
-        base_path: str = None,
-        app_name: str = None,
+        base_path: Optional[str] = None,
+        app_name: Optional[str] = None,
         scope: str = None,
         max_batch_size_mb: float = 10.0,
         **data: Any,
     ) -> None:
         super().__init__(**data)
         self.app_name = app_name or "Speckle"
         self.scope = scope or "Objects"
```

### Comparing `specklepy-2.9.0/setup.py` & `specklepy-2.9.1/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,13 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
+package_dir = \
+{'': 'src'}
+
 packages = \
 ['specklepy',
  'specklepy.api',
  'specklepy.api.resources',
  'specklepy.logging',
  'specklepy.objects',
  'specklepy.objects.structural',
@@ -20,22 +23,23 @@
  'appdirs>=1.4.4,<2.0.0',
  'gql[requests,websockets]>=3.3.0,<4.0.0',
  'pydantic>=1.8.2,<2.0.0',
  'ujson>=5.3.0,<6.0.0']
 
 setup_kwargs = {
     'name': 'specklepy',
-    'version': '2.9.0',
+    'version': '2.9.1',
     'description': 'The Python SDK for Speckle 2.0',
     'long_description': '<h1 align="center">\n  <img src="https://user-images.githubusercontent.com/2679513/131189167-18ea5fe1-c578-47f6-9785-3748178e4312.png" width="150px"/><br/>\n  Speckle | specklepy 🐍\n</h1>\n<h3 align="center">\n    The Python SDK\n</h3>\n<p align="center"><b>Speckle</b> is the data infrastructure for the AEC industry.</p><br/>\n\n<p align="center"><a href="https://twitter.com/SpeckleSystems"><img src="https://img.shields.io/twitter/follow/SpeckleSystems?style=social" alt="Twitter Follow"></a> <a href="https://speckle.community"><img src="https://img.shields.io/discourse/users?server=https%3A%2F%2Fspeckle.community&amp;style=flat-square&amp;logo=discourse&amp;logoColor=white" alt="Community forum users"></a> <a href="https://speckle.systems"><img src="https://img.shields.io/badge/https://-speckle.systems-royalblue?style=flat-square" alt="website"></a> <a href="https://speckle.guide/dev/"><img src="https://img.shields.io/badge/docs-speckle.guide-orange?style=flat-square&amp;logo=read-the-docs&amp;logoColor=white" alt="docs"></a></p>\n<p align="center"><a href="https://github.com/specklesystems/specklepy/"><img src="https://circleci.com/gh/specklesystems/specklepy.svg?style=svg&amp;circle-token=76eabd350ea243575cbb258b746ed3f471f7ac29" alt="Speckle-Next"></a><a href="https://codecov.io/gh/specklesystems/specklepy">\n  <img src="https://codecov.io/gh/specklesystems/specklepy/branch/main/graph/badge.svg?token=8KQFL5N0YF"/>\n</a> </p>\n\n# About Speckle\n\nWhat is Speckle? Check our ![YouTube Video Views](https://img.shields.io/youtube/views/B9humiSpHzM?label=Speckle%20in%201%20minute%20video&style=social)\n\n### Features\n\n- **Object-based:** say goodbye to files! Speckle is the first object based platform for the AEC industry\n- **Version control:** Speckle is the Git & Hub for geometry and BIM data\n- **Collaboration:** share your designs collaborate with others\n- **3D Viewer:** see your CAD and BIM models online, share and embed them anywhere\n- **Interoperability:** get your CAD and BIM models into other software without exporting or importing\n- **Real time:** get real time updates and notifications and changes\n- **GraphQL API:** get what you need anywhere you want it\n- **Webhooks:** the base for a automation and next-gen pipelines\n- **Built for developers:** we are building Speckle with developers in mind and got tools for every stack\n- **Built for the AEC industry:** Speckle connectors are plugins for the most common software used in the industry such as Revit, Rhino, Grasshopper, AutoCAD, Civil 3D, Excel, Unreal Engine, Unity, QGIS, Blender and more!\n\n### Try Speckle now!\n\nGive Speckle a try in no time by:\n\n- [![speckle XYZ](https://img.shields.io/badge/https://-speckle.xyz-0069ff?style=flat-square&logo=hackthebox&logoColor=white)](https://speckle.xyz) ⇒ creating an account at our public server\n- [![create a droplet](https://img.shields.io/badge/Create%20a%20Droplet-0069ff?style=flat-square&logo=digitalocean&logoColor=white)](https://marketplace.digitalocean.com/apps/speckle-server?refcode=947a2b5d7dc1) ⇒ deploying an instance in 1 click \n\n### Resources\n\n- [![Community forum users](https://img.shields.io/badge/community-forum-green?style=for-the-badge&logo=discourse&logoColor=white)](https://speckle.community) for help, feature requests or just to hang with other speckle enthusiasts, check out our community forum!\n- [![website](https://img.shields.io/badge/tutorials-speckle.systems-royalblue?style=for-the-badge&logo=youtube)](https://speckle.systems) our tutorials portal is full of resources to get you started using Speckle\n- [![docs](https://img.shields.io/badge/docs-speckle.guide-orange?style=for-the-badge&logo=read-the-docs&logoColor=white)](https://speckle.guide/dev/) reference on almost any end-user and developer functionality\n\n\n# Repo structure\n\n## Usage\n\nSend and receive data from a Speckle Server with `operations`, interact with the Speckle API with the `SpeckleClient`, create and extend your own custom Speckle Objects with `Base`, and more! \n\nHead to the [**📚 specklepy docs**](https://speckle.guide/dev/python.html) for more information and usage examples.\n\n## Developing & Debugging\n\n### Installation\n\nThis project uses python-poetry for dependency management, make sure you follow the official [docs](https://python-poetry.org/docs/#installation) to get poetry.\n\nTo bootstrap the project environment run `$ poetry install`. This will create a new virtual-env for the project and install both the package and dev dependencies.\n\nIf this is your first time using poetry and you\'re used to creating your venvs within the project directory, run `poetry config virtualenvs.in-project true` to configure poetry to do the same.\n\nTo execute any python script run `$ poetry run python my_script.py`\n\n> Alternatively you may roll your own virtual-env with either venv, virtualenv, pyenv-virtualenv etc. Poetry will play along an recognize if it is invoked from inside a virtual environment.\n\n### Local Data Paths\n\nIt may be helpful to know where the local accounts and object cache dbs are stored. Depending on on your OS, you can find the dbs at:\n- Windows: `APPDATA` or `<USER>\\AppData\\Roaming\\Speckle`\n- Linux: `$XDG_DATA_HOME` or by default `~/.local/share/Speckle`\n- Mac: `~/.config/Speckle`\n\n## Contributing\n\nPlease make sure you read the [contribution guidelines](.github/CONTRIBUTING.md) and [code of conduct](.github/CODE_OF_CONDUCT.md) for an overview of the practices we try to follow.\n\n## Community\n\nThe Speckle Community hangs out on [the forum](https://discourse.speckle.works), do join and introduce yourself & feel free to ask us questions!\n\n## Security\n\nFor any security vulnerabilities or concerns, please contact us directly at security[at]speckle.systems. \n\n## License\n\nUnless otherwise described, the code in this repository is licensed under the Apache-2.0 License. Please note that some modules, extensions or code herein might be otherwise licensed. This is indicated either in the root of the containing folder under a different license file, or in the respective file\'s header. If you have any questions, don\'t hesitate to get in touch with us via [email](mailto:hello@speckle.systems).\n',
     'author': 'Speckle Systems',
     'author_email': 'devops@speckle.systems',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://speckle.systems/',
+    'package_dir': package_dir,
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
     'python_requires': '>=3.7.2,<4.0',
 }
```

#### html2text {}

```diff
@@ -1,16 +1,16 @@
-# -*- coding: utf-8 -*- from setuptools import setup packages = \ ['specklepy',
-'specklepy.api', 'specklepy.api.resources', 'specklepy.logging',
-'specklepy.objects', 'specklepy.objects.structural', 'specklepy.serialization',
-'specklepy.transports', 'specklepy.transports.server'] package_data = \ {'':
-['*']} install_requires = \ ['Deprecated>=1.2.13,<2.0.0',
-'appdirs>=1.4.4,<2.0.0', 'gql[requests,websockets]>=3.3.0,<4.0.0',
-'pydantic>=1.8.2,<2.0.0', 'ujson>=5.3.0,<6.0.0'] setup_kwargs = { 'name':
-'specklepy', 'version': '2.9.0', 'description': 'The Python SDK for Speckle
-2.0', 'long_description': '
+# -*- coding: utf-8 -*- from setuptools import setup package_dir = \ {'':
+'src'} packages = \ ['specklepy', 'specklepy.api', 'specklepy.api.resources',
+'specklepy.logging', 'specklepy.objects', 'specklepy.objects.structural',
+'specklepy.serialization', 'specklepy.transports',
+'specklepy.transports.server'] package_data = \ {'': ['*']} install_requires =
+\ ['Deprecated>=1.2.13,<2.0.0', 'appdirs>=1.4.4,<2.0.0', 'gql
+[requests,websockets]>=3.3.0,<4.0.0', 'pydantic>=1.8.2,<2.0.0',
+'ujson>=5.3.0,<6.0.0'] setup_kwargs = { 'name': 'specklepy', 'version':
+'2.9.1', 'description': 'The Python SDK for Speckle 2.0', 'long_description': '
     ****** \n [https://user-images.githubusercontent.com/2679513/131189167-
                    18ea5fe1-c578-47f6-9785-3748178e4312.png]
                      \n Speckle | specklepy ð\n ******
 \n
                          **** \n The Python SDK\n ****
 \n
            Speckle is the data infrastructure for the AEC industry.
@@ -82,10 +82,10 @@
 code in this repository is licensed under the Apache-2.0 License. Please note
 that some modules, extensions or code herein might be otherwise licensed. This
 is indicated either in the root of the containing folder under a different
 license file, or in the respective file\'s header. If you have any questions,
 don\'t hesitate to get in touch with us via [email](mailto:
 hello@speckle.systems).\n', 'author': 'Speckle Systems', 'author_email':
 'devops@speckle.systems', 'maintainer': 'None', 'maintainer_email': 'None',
-'url': 'https://speckle.systems/', 'packages': packages, 'package_data':
-package_data, 'install_requires': install_requires, 'python_requires':
-'>=3.7.2,<4.0', } setup(**setup_kwargs)
+'url': 'https://speckle.systems/', 'package_dir': package_dir, 'packages':
+packages, 'package_data': package_data, 'install_requires': install_requires,
+'python_requires': '>=3.7.2,<4.0', } setup(**setup_kwargs)
```

### Comparing `specklepy-2.9.0/PKG-INFO` & `specklepy-2.9.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 Metadata-Version: 2.1
 Name: specklepy
-Version: 2.9.0
+Version: 2.9.1
 Summary: The Python SDK for Speckle 2.0
 Home-page: https://speckle.systems/
 License: Apache-2.0
 Author: Speckle Systems
 Author-email: devops@speckle.systems
 Requires-Python: >=3.7.2,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: Deprecated (>=1.2.13,<2.0.0)
 Requires-Dist: appdirs (>=1.4.4,<2.0.0)
 Requires-Dist: gql[requests,websockets] (>=3.3.0,<4.0.0)
 Requires-Dist: pydantic (>=1.8.2,<2.0.0)
 Requires-Dist: ujson (>=5.3.0,<6.0.0)
 Project-URL: Documentation, https://speckle.guide/dev/py-examples.html
 Project-URL: Repository, https://github.com/specklesystems/speckle-py
```

#### html2text {}

```diff
@@ -1,19 +1,20 @@
-Metadata-Version: 2.1 Name: specklepy Version: 2.9.0 Summary: The Python SDK
+Metadata-Version: 2.1 Name: specklepy Version: 2.9.1 Summary: The Python SDK
 for Speckle 2.0 Home-page: https://speckle.systems/ License: Apache-2.0 Author:
 Speckle Systems Author-email: devops@speckle.systems Requires-Python:
 >=3.7.2,<4.0 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10 Requires-Dist: Deprecated
-(>=1.2.13,<2.0.0) Requires-Dist: appdirs (>=1.4.4,<2.0.0) Requires-Dist: gql
-[requests,websockets] (>=3.3.0,<4.0.0) Requires-Dist: pydantic (>=1.8.2,<2.0.0)
-Requires-Dist: ujson (>=5.3.0,<6.0.0) Project-URL: Documentation, https://
-speckle.guide/dev/py-examples.html Project-URL: Repository, https://github.com/
-specklesystems/speckle-py Description-Content-Type: text/markdown
+Classifier: Programming Language :: Python :: 3.10 Classifier: Programming
+Language :: Python :: 3.11 Requires-Dist: Deprecated (>=1.2.13,<2.0.0)
+Requires-Dist: appdirs (>=1.4.4,<2.0.0) Requires-Dist: gql[requests,websockets]
+(>=3.3.0,<4.0.0) Requires-Dist: pydantic (>=1.8.2,<2.0.0) Requires-Dist: ujson
+(>=5.3.0,<6.0.0) Project-URL: Documentation, https://speckle.guide/dev/py-
+examples.html Project-URL: Repository, https://github.com/specklesystems/
+speckle-py Description-Content-Type: text/markdown
  ****** [https://user-images.githubusercontent.com/2679513/131189167-18ea5fe1-
                        c578-47f6-9785-3748178e4312.png]
                         Speckle | specklepy ð ******
                            **** The Python SDK ****
            Speckle is the data infrastructure for the AEC industry.
 
            [Twitter_Follow] [Community_forum_users] [website] [docs]
```

