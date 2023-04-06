# Comparing `tmp/mypy-boto3-rds-1.26.97.post1.tar.gz` & `tmp/mypy-boto3-rds-1.26.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mypy-boto3-rds-1.26.97.post1.tar", last modified: Thu Mar 23 01:30:37 2023, max compression
+gzip compressed data, was "mypy-boto3-rds-1.26.99.tar", last modified: Fri Mar 24 19:32:25 2023, max compression
```

## Comparing `mypy-boto3-rds-1.26.97.post1.tar` & `mypy-boto3-rds-1.26.99.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxrwxr-x   0 vlad      (1000) vlad      (1000)        0 2023-03-23 01:30:37.291124 mypy-boto3-rds-1.26.97.post1/
--rw-rw-r--   0 vlad      (1000) vlad      (1000)     1070 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/LICENSE
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    41334 2023-03-23 01:30:37.291124 mypy-boto3-rds-1.26.97.post1/PKG-INFO
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    39857 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/README.md
-drwxrwxr-x   0 vlad      (1000) vlad      (1000)        0 2023-03-23 01:30:37.291124 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    11325 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__init__.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    11324 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__init__.pyi
--rw-rw-r--   0 vlad      (1000) vlad      (1000)      903 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__main__.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)   143183 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/client.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)   142990 2023-03-23 01:30:16.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/client.pyi
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    17592 2023-03-23 01:30:18.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/literals.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    17590 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/literals.pyi
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    45248 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/paginator.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    45211 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/paginator.pyi
--rw-rw-r--   0 vlad      (1000) vlad      (1000)        0 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/py.typed
--rw-rw-r--   0 vlad      (1000) vlad      (1000)   190070 2023-03-23 01:30:22.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/type_defs.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)   189893 2023-03-23 01:30:20.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/type_defs.pyi
--rw-rw-r--   0 vlad      (1000) vlad      (1000)       67 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/version.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    11143 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/waiter.py
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    11134 2023-03-23 01:30:17.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/waiter.pyi
-drwxrwxr-x   0 vlad      (1000) vlad      (1000)        0 2023-03-23 01:30:37.291124 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/
--rw-rw-r--   0 vlad      (1000) vlad      (1000)    41334 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/PKG-INFO
--rw-rw-r--   0 vlad      (1000) vlad      (1000)      655 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/SOURCES.txt
--rw-rw-r--   0 vlad      (1000) vlad      (1000)        1 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/dependency_links.txt
--rw-rw-r--   0 vlad      (1000) vlad      (1000)        1 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/not-zip-safe
--rw-rw-r--   0 vlad      (1000) vlad      (1000)       52 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/requires.txt
--rw-rw-r--   0 vlad      (1000) vlad      (1000)       15 2023-03-23 01:30:37.000000 mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/top_level.txt
--rw-rw-r--   0 vlad      (1000) vlad      (1000)       38 2023-03-23 01:30:37.291124 mypy-boto3-rds-1.26.97.post1/setup.cfg
--rw-rw-r--   0 vlad      (1000) vlad      (1000)     1963 2023-03-23 01:30:15.000000 mypy-boto3-rds-1.26.97.post1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.581893 mypy-boto3-rds-1.26.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    41328 2023-03-24 19:32:25.581893 mypy-boto3-rds-1.26.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    39857 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.581893 mypy-boto3-rds-1.26.99/mypy_boto3_rds/
+-rw-r--r--   0 runner    (1001) docker     (123)    11325 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11324 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)      891 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   143243 2023-03-24 19:32:11.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)   143050 2023-03-24 19:32:11.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/client.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    17612 2023-03-24 19:32:13.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/literals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17610 2023-03-24 19:32:12.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/literals.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    45248 2023-03-24 19:32:12.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/paginator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45211 2023-03-24 19:32:12.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/paginator.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)   190070 2023-03-24 19:32:16.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/type_defs.py
+-rw-r--r--   0 runner    (1001) docker     (123)   189893 2023-03-24 19:32:15.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/type_defs.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-03-24 19:32:10.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11143 2023-03-24 19:32:12.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/waiter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11134 2023-03-24 19:32:12.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds/waiter.pyi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.581893 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    41328 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-24 19:32:25.000000 mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 19:32:25.581893 mypy-boto3-rds-1.26.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1957 2023-03-24 19:32:09.000000 mypy-boto3-rds-1.26.99/setup.py
```

### Comparing `mypy-boto3-rds-1.26.97.post1/LICENSE` & `mypy-boto3-rds-1.26.99/LICENSE`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/PKG-INFO` & `mypy-boto3-rds-1.26.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3-rds
-Version: 1.26.97.post1
-Summary: Type annotations for boto3.RDS 1.26.97 service generated with mypy-boto3-builder 7.14.1
+Version: 1.26.99
+Summary: Type annotations for boto3.RDS 1.26.99 service generated with mypy-boto3-builder 7.14.2
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,24 +38,24 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-rds.svg?color=blue)](https://pypi.org/project/mypy-boto3-rds)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-rds?color=blue)](https://pypistats.org/packages/mypy-boto3-rds)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.RDS 1.26.97](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
+[boto3.RDS 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
 
 Generated by
-[mypy-boto3-builder 7.14.1](https://github.com/youtype/mypy_boto3_builder).
+[mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
 [boto3-stubs](https://pypi.org/project/boto3-stubs/) page and in
 [mypy-boto3-rds docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/).
 
 See how it helps to find and fix potential bugs:
```

### Comparing `mypy-boto3-rds-1.26.97.post1/README.md` & `mypy-boto3-rds-1.26.99/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -6,24 +6,24 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-rds.svg?color=blue)](https://pypi.org/project/mypy-boto3-rds)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-rds?color=blue)](https://pypistats.org/packages/mypy-boto3-rds)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.RDS 1.26.97](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
+[boto3.RDS 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
 
 Generated by
-[mypy-boto3-builder 7.14.1](https://github.com/youtype/mypy_boto3_builder).
+[mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
 [boto3-stubs](https://pypi.org/project/boto3-stubs/) page and in
 [mypy-boto3-rds docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/).
 
 See how it helps to find and fix potential bugs:
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__init__.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/__init__.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__init__.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/__init__.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/__main__.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/__main__.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,28 +5,28 @@
 
 
 def print_info() -> None:
     """
     Print package info to stdout.
     """
     print(
-        "Type annotations for boto3.RDS 1.26.97\nVersion:         1.26.97.post1\nBuilder version:"
-        " 7.14.1\nDocs:           "
+        "Type annotations for boto3.RDS 1.26.99\nVersion:         1.26.99\nBuilder version:"
+        " 7.14.2\nDocs:           "
         " https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds//\nBoto3 docs:     "
         " https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS\nOther"
         " services:  https://pypi.org/project/boto3-stubs/\nChangelog:      "
         " https://github.com/youtype/mypy_boto3_builder/releases"
     )
 
 
 def print_version() -> None:
     """
     Print package version to stdout.
     """
-    print("1.26.97.post1")
+    print("1.26.99")
 
 
 def main() -> None:
     """
     Main CLI entrypoint.
     """
     if "--version" in sys.argv:
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/client.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/client.py`

 * *Files 0% similar despite different names*

```diff
@@ -236,14 +236,15 @@
     AuthorizationNotFoundFault: Type[BotocoreClientError]
     AuthorizationQuotaExceededFault: Type[BotocoreClientError]
     BackupPolicyNotFoundFault: Type[BotocoreClientError]
     BlueGreenDeploymentAlreadyExistsFault: Type[BotocoreClientError]
     BlueGreenDeploymentNotFoundFault: Type[BotocoreClientError]
     CertificateNotFoundFault: Type[BotocoreClientError]
     ClientError: Type[BotocoreClientError]
+    CreateCustomDBEngineVersionFault: Type[BotocoreClientError]
     CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
     CustomDBEngineVersionAlreadyExistsFault: Type[BotocoreClientError]
     CustomDBEngineVersionNotFoundFault: Type[BotocoreClientError]
     CustomDBEngineVersionQuotaExceededFault: Type[BotocoreClientError]
     DBClusterAlreadyExistsFault: Type[BotocoreClientError]
     DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
     DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
@@ -1154,15 +1155,15 @@
         DBProxyName: str,
         TargetGroupName: str = ...,
         DBInstanceIdentifiers: Sequence[str] = ...,
         DBClusterIdentifiers: Sequence[str] = ...
     ) -> Dict[str, Any]:
         """
         Remove the association between one or more `DBProxyTarget` data structures and a
-        `DBProxyTargetGroup` .
+        `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#deregister_db_proxy_targets)
         """
 
     def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
         """
@@ -1817,15 +1818,15 @@
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_db_cluster)
         """
 
     def failover_global_cluster(
         self, *, GlobalClusterIdentifier: str, TargetDbClusterIdentifier: str
     ) -> FailoverGlobalClusterResultTypeDef:
         """
-        Initiates the failover process for an Aurora global database (  GlobalCluster ).
+        Initiates the failover process for an Aurora global database (  GlobalCluster).
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_global_cluster)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_global_cluster)
         """
 
     def generate_db_auth_token(
         self, DBHostname: str, Port: int, DBUsername: str, Region: Optional[str] = ...
@@ -2116,15 +2117,15 @@
         *,
         TargetGroupName: str,
         DBProxyName: str,
         ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = ...,
         NewName: str = ...
     ) -> ModifyDBProxyTargetGroupResponseTypeDef:
         """
-        Modifies the properties of a `DBProxyTargetGroup` .
+        Modifies the properties of a `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_target_group)
         """
 
     def modify_db_snapshot(
         self, *, DBSnapshotIdentifier: str, EngineVersion: str = ..., OptionGroupName: str = ...
@@ -2276,15 +2277,15 @@
         DBProxyName: str,
         TargetGroupName: str = ...,
         DBInstanceIdentifiers: Sequence[str] = ...,
         DBClusterIdentifiers: Sequence[str] = ...
     ) -> RegisterDBProxyTargetsResponseTypeDef:
         """
         Associate one or more `DBProxyTarget` data structures with a
-        `DBProxyTargetGroup` .
+        `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#register_db_proxy_targets)
         """
 
     def remove_from_global_cluster(
         self, *, GlobalClusterIdentifier: str = ..., DbClusterIdentifier: str = ...
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/client.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/client.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -233,14 +233,15 @@
     AuthorizationNotFoundFault: Type[BotocoreClientError]
     AuthorizationQuotaExceededFault: Type[BotocoreClientError]
     BackupPolicyNotFoundFault: Type[BotocoreClientError]
     BlueGreenDeploymentAlreadyExistsFault: Type[BotocoreClientError]
     BlueGreenDeploymentNotFoundFault: Type[BotocoreClientError]
     CertificateNotFoundFault: Type[BotocoreClientError]
     ClientError: Type[BotocoreClientError]
+    CreateCustomDBEngineVersionFault: Type[BotocoreClientError]
     CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
     CustomDBEngineVersionAlreadyExistsFault: Type[BotocoreClientError]
     CustomDBEngineVersionNotFoundFault: Type[BotocoreClientError]
     CustomDBEngineVersionQuotaExceededFault: Type[BotocoreClientError]
     DBClusterAlreadyExistsFault: Type[BotocoreClientError]
     DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
     DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
@@ -1100,15 +1101,15 @@
         DBProxyName: str,
         TargetGroupName: str = ...,
         DBInstanceIdentifiers: Sequence[str] = ...,
         DBClusterIdentifiers: Sequence[str] = ...
     ) -> Dict[str, Any]:
         """
         Remove the association between one or more `DBProxyTarget` data structures and a
-        `DBProxyTargetGroup` .
+        `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#deregister_db_proxy_targets)
         """
     def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
         """
         Lists all of the attributes for a customer account.
@@ -1721,15 +1722,15 @@
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_db_cluster)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_db_cluster)
         """
     def failover_global_cluster(
         self, *, GlobalClusterIdentifier: str, TargetDbClusterIdentifier: str
     ) -> FailoverGlobalClusterResultTypeDef:
         """
-        Initiates the failover process for an Aurora global database (  GlobalCluster ).
+        Initiates the failover process for an Aurora global database (  GlobalCluster).
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_global_cluster)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_global_cluster)
         """
     def generate_db_auth_token(
         self, DBHostname: str, Port: int, DBUsername: str, Region: Optional[str] = ...
     ) -> str:
@@ -2004,15 +2005,15 @@
         *,
         TargetGroupName: str,
         DBProxyName: str,
         ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = ...,
         NewName: str = ...
     ) -> ModifyDBProxyTargetGroupResponseTypeDef:
         """
-        Modifies the properties of a `DBProxyTargetGroup` .
+        Modifies the properties of a `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_target_group)
         """
     def modify_db_snapshot(
         self, *, DBSnapshotIdentifier: str, EngineVersion: str = ..., OptionGroupName: str = ...
     ) -> ModifyDBSnapshotResultTypeDef:
@@ -2152,15 +2153,15 @@
         DBProxyName: str,
         TargetGroupName: str = ...,
         DBInstanceIdentifiers: Sequence[str] = ...,
         DBClusterIdentifiers: Sequence[str] = ...
     ) -> RegisterDBProxyTargetsResponseTypeDef:
         """
         Associate one or more `DBProxyTarget` data structures with a
-        `DBProxyTargetGroup` .
+        `DBProxyTargetGroup`.
 
         [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
         [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#register_db_proxy_targets)
         """
     def remove_from_global_cluster(
         self, *, GlobalClusterIdentifier: str = ..., DbClusterIdentifier: str = ...
     ) -> RemoveFromGlobalClusterResultTypeDef:
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/literals.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/literals.py`

 * *Files 0% similar despite different names*

```diff
@@ -366,14 +366,15 @@
     "iotfleetwise",
     "iotsecuretunneling",
     "iotsitewise",
     "iotthingsgraph",
     "iottwinmaker",
     "iotwireless",
     "ivs",
+    "ivs-realtime",
     "ivschat",
     "kafka",
     "kafkaconnect",
     "kendra",
     "kendra-ranking",
     "keyspaces",
     "kinesis",
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/literals.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/literals.pyi`

 * *Files 0% similar despite different names*

```diff
@@ -364,14 +364,15 @@
     "iotfleetwise",
     "iotsecuretunneling",
     "iotsitewise",
     "iotthingsgraph",
     "iottwinmaker",
     "iotwireless",
     "ivs",
+    "ivs-realtime",
     "ivschat",
     "kafka",
     "kafkaconnect",
     "kendra",
     "kendra-ranking",
     "keyspaces",
     "kinesis",
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/paginator.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/paginator.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/paginator.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/paginator.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/type_defs.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/type_defs.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/type_defs.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/type_defs.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/waiter.py` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/waiter.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds/waiter.pyi` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds/waiter.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/PKG-INFO` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3-rds
-Version: 1.26.97.post1
-Summary: Type annotations for boto3.RDS 1.26.97 service generated with mypy-boto3-builder 7.14.1
+Version: 1.26.99
+Summary: Type annotations for boto3.RDS 1.26.99 service generated with mypy-boto3-builder 7.14.2
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,24 +38,24 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-rds.svg?color=blue)](https://pypi.org/project/mypy-boto3-rds)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-rds?color=blue)](https://pypistats.org/packages/mypy-boto3-rds)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.RDS 1.26.97](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
+[boto3.RDS 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
 
 Generated by
-[mypy-boto3-builder 7.14.1](https://github.com/youtype/mypy_boto3_builder).
+[mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
 [boto3-stubs](https://pypi.org/project/boto3-stubs/) page and in
 [mypy-boto3-rds docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/).
 
 See how it helps to find and fix potential bugs:
```

### Comparing `mypy-boto3-rds-1.26.97.post1/mypy_boto3_rds.egg-info/SOURCES.txt` & `mypy-boto3-rds-1.26.99/mypy_boto3_rds.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mypy-boto3-rds-1.26.97.post1/setup.py` & `mypy-boto3-rds-1.26.99/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -6,22 +6,22 @@
 from setuptools import setup
 
 LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()
 
 
 setup(
     name="mypy-boto3-rds",
-    version="1.26.97.post1",
+    version="1.26.99",
     packages=["mypy_boto3_rds"],
     url="https://github.com/youtype/mypy_boto3_builder",
     license="MIT License",
     author="Vlad Emelianov",
     author_email="vlad.emelianov.nz@gmail.com",
     description=(
-        "Type annotations for boto3.RDS 1.26.97 service generated with mypy-boto3-builder 7.14.1"
+        "Type annotations for boto3.RDS 1.26.99 service generated with mypy-boto3-builder 7.14.2"
     ),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "Environment :: Console",
         "License :: OSI Approved :: MIT License",
         "Natural Language :: English",
```

