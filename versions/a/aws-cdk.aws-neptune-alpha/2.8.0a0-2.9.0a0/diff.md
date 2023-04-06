# Comparing `tmp/aws-cdk.aws-neptune-alpha-2.8.0a0.tar.gz` & `tmp/aws-cdk.aws-neptune-alpha-2.9.0a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/individual-packages/aws-neptune/dist/python/aws-cdk.aws-neptune-alpha-2.8.0a0.tar", last modified: Thu Jan 13 18:05:53 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/individual-packages/aws-neptune/dist/python/aws-cdk.aws-neptune-alpha-2.9.0a0.tar", last modified: Wed Jan 26 11:22:06 2022, max compression
```

## Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0.tar` & `aws-cdk.aws-neptune-alpha-2.9.0a0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      113 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     5295 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     4327 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1795 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/
--rw-r--r--   0 root         (0) root         (0)   110096 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/
--rw-r--r--   0 root         (0) root         (0)      405 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)    54504 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/aws-neptune-alpha@2.8.0-alpha.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:47.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/
--rw-r--r--   0 root         (0) root         (0)     5295 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      530 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       92 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 18:05:53.000000 aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      113 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     5750 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     4782 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1795 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/
+-rw-r--r--   0 root         (0) root         (0)   111643 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      405 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    55214 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/_jsii/aws-neptune-alpha@2.9.0-alpha.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:01.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     5750 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      530 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       92 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 11:22:06.000000 aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/top_level.txt
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/LICENSE` & `aws-cdk.aws-neptune-alpha-2.9.0a0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/PKG-INFO` & `aws-cdk.aws-neptune-alpha-2.9.0a0/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-neptune-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: The CDK Construct Library for AWS::Neptune
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
@@ -142,8 +142,23 @@
 ```python
 replica1 = neptune.DatabaseInstance(self, "Instance",
     cluster=cluster,
     instance_type=neptune.InstanceType.R5_LARGE
 )
 ```
 
+## Automatic minor version upgrades
+
+By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
+the engine of the entire cluster to the latest minor version after a stabilization
+window of 2 to 3 weeks.
+
+```python
+# Example automatically generated from non-compiling source. May contain errors.
+neptune.DatabaseCluster(stack, "Cluster",
+    vpc=vpc,
+    instance_type=InstanceType.R5_LARGE,
+    auto_minor_version_upgrade=True
+)
+```
+
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/README.md` & `aws-cdk.aws-neptune-alpha-2.9.0a0/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -114,7 +114,22 @@
 
 ```python
 replica1 = neptune.DatabaseInstance(self, "Instance",
     cluster=cluster,
     instance_type=neptune.InstanceType.R5_LARGE
 )
 ```
+
+## Automatic minor version upgrades
+
+By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
+the engine of the entire cluster to the latest minor version after a stabilization
+window of 2 to 3 weeks.
+
+```python
+# Example automatically generated from non-compiling source. May contain errors.
+neptune.DatabaseCluster(stack, "Cluster",
+    vpc=vpc,
+    instance_type=InstanceType.R5_LARGE,
+    auto_minor_version_upgrade=True
+)
+```
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/setup.py` & `aws-cdk.aws-neptune-alpha-2.9.0a0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.aws-neptune-alpha",
-    "version": "2.8.0.a0",
+    "version": "2.9.0.a0",
     "description": "The CDK Construct Library for AWS::Neptune",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,23 +22,23 @@
     },
     "packages": [
         "aws_cdk.aws_neptune_alpha",
         "aws_cdk.aws_neptune_alpha._jsii"
     ],
     "package_data": {
         "aws_cdk.aws_neptune_alpha._jsii": [
-            "aws-neptune-alpha@2.8.0-alpha.0.jsii.tgz"
+            "aws-neptune-alpha@2.9.0-alpha.0.jsii.tgz"
         ],
         "aws_cdk.aws_neptune_alpha": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "aws-cdk-lib>=2.8.0, <3.0.0",
+        "aws-cdk-lib>=2.9.0, <3.0.0",
         "constructs>=10.0.0, <11.0.0",
         "jsii>=1.52.1, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk/aws_neptune_alpha/__init__.py` & `aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk/aws_neptune_alpha/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -115,14 +115,29 @@
 
 ```python
 replica1 = neptune.DatabaseInstance(self, "Instance",
     cluster=cluster,
     instance_type=neptune.InstanceType.R5_LARGE
 )
 ```
+
+## Automatic minor version upgrades
+
+By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
+the engine of the entire cluster to the latest minor version after a stabilization
+window of 2 to 3 weeks.
+
+```python
+# Example automatically generated from non-compiling source. May contain errors.
+neptune.DatabaseCluster(stack, "Cluster",
+    vpc=vpc,
+    instance_type=InstanceType.R5_LARGE,
+    auto_minor_version_upgrade=True
+)
+```
 '''
 import abc
 import builtins
 import datetime
 import enum
 import typing
 
@@ -377,14 +392,15 @@
 @jsii.data_type(
     jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseClusterProps",
     jsii_struct_bases=[],
     name_mapping={
         "instance_type": "instanceType",
         "vpc": "vpc",
         "associated_roles": "associatedRoles",
+        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
         "backup_retention": "backupRetention",
         "cluster_parameter_group": "clusterParameterGroup",
         "db_cluster_name": "dbClusterName",
         "deletion_protection": "deletionProtection",
         "engine_version": "engineVersion",
         "iam_authentication": "iamAuthentication",
         "instance_identifier_base": "instanceIdentifierBase",
@@ -404,14 +420,15 @@
 class DatabaseClusterProps:
     def __init__(
         self,
         *,
         instance_type: "InstanceType",
         vpc: aws_cdk.aws_ec2.IVpc,
         associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
+        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
         backup_retention: typing.Optional[aws_cdk.Duration] = None,
         cluster_parameter_group: typing.Optional["IClusterParameterGroup"] = None,
         db_cluster_name: typing.Optional[builtins.str] = None,
         deletion_protection: typing.Optional[builtins.bool] = None,
         engine_version: typing.Optional["EngineVersion"] = None,
         iam_authentication: typing.Optional[builtins.bool] = None,
         instance_identifier_base: typing.Optional[builtins.str] = None,
@@ -428,14 +445,15 @@
         vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
     ) -> None:
         '''(experimental) Properties for a new database cluster.
 
         :param instance_type: (experimental) What type of instance to start for the replicas.
         :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
         :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
+        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
         :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
         :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
         :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
         :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
         :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
         :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
         :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
@@ -452,30 +470,30 @@
         :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets
 
         :stability: experimental
         :exampleMetadata: infused
 
         Example::
 
-            cluster = neptune.DatabaseCluster(self, "Cluster",
+            cluster = neptune.DatabaseCluster(self, "Database",
                 vpc=vpc,
                 instance_type=neptune.InstanceType.R5_LARGE,
-                iam_authentication=True
+                instances=2
             )
-            role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
-            cluster.grant_connect(role)
         '''
         if isinstance(vpc_subnets, dict):
             vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
         self._values: typing.Dict[str, typing.Any] = {
             "instance_type": instance_type,
             "vpc": vpc,
         }
         if associated_roles is not None:
             self._values["associated_roles"] = associated_roles
+        if auto_minor_version_upgrade is not None:
+            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
         if backup_retention is not None:
             self._values["backup_retention"] = backup_retention
         if cluster_parameter_group is not None:
             self._values["cluster_parameter_group"] = cluster_parameter_group
         if db_cluster_name is not None:
             self._values["db_cluster_name"] = db_cluster_name
         if deletion_protection is not None:
@@ -539,14 +557,25 @@
 
         :stability: experimental
         '''
         result = self._values.get("associated_roles")
         return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.IRole]], result)
 
     @builtins.property
+    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.bool]:
+        '''(experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks.
+
+        :default: - false
+
+        :stability: experimental
+        '''
+        result = self._values.get("auto_minor_version_upgrade")
+        return typing.cast(typing.Optional[builtins.bool], result)
+
+    @builtins.property
     def backup_retention(self) -> typing.Optional[aws_cdk.Duration]:
         '''(experimental) How many days to retain the backup.
 
         :default: - cdk.Duration.days(1)
 
         :stability: experimental
         '''
@@ -2656,31 +2685,30 @@
 
     :stability: experimental
     :exampleMetadata: infused
     :resource: AWS::Neptune::DBCluster
 
     Example::
 
-        cluster = neptune.DatabaseCluster(self, "Cluster",
+        cluster = neptune.DatabaseCluster(self, "Database",
             vpc=vpc,
             instance_type=neptune.InstanceType.R5_LARGE,
-            iam_authentication=True
+            instances=2
         )
-        role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
-        cluster.grant_connect(role)
     '''
 
     def __init__(
         self,
         scope: constructs.Construct,
         id: builtins.str,
         *,
         instance_type: InstanceType,
         vpc: aws_cdk.aws_ec2.IVpc,
         associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
+        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
         backup_retention: typing.Optional[aws_cdk.Duration] = None,
         cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
         db_cluster_name: typing.Optional[builtins.str] = None,
         deletion_protection: typing.Optional[builtins.bool] = None,
         engine_version: typing.Optional[EngineVersion] = None,
         iam_authentication: typing.Optional[builtins.bool] = None,
         instance_identifier_base: typing.Optional[builtins.str] = None,
@@ -2698,14 +2726,15 @@
     ) -> None:
         '''
         :param scope: -
         :param id: -
         :param instance_type: (experimental) What type of instance to start for the replicas.
         :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
         :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
+        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
         :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
         :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
         :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
         :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
         :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
         :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
         :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
@@ -2723,14 +2752,15 @@
 
         :stability: experimental
         '''
         props = DatabaseClusterProps(
             instance_type=instance_type,
             vpc=vpc,
             associated_roles=associated_roles,
+            auto_minor_version_upgrade=auto_minor_version_upgrade,
             backup_retention=backup_retention,
             cluster_parameter_group=cluster_parameter_group,
             db_cluster_name=db_cluster_name,
             deletion_protection=deletion_protection,
             engine_version=engine_version,
             iam_authentication=iam_authentication,
             instance_identifier_base=instance_identifier_base,
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/PKG-INFO` & `aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-neptune-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: The CDK Construct Library for AWS::Neptune
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
@@ -142,8 +142,23 @@
 ```python
 replica1 = neptune.DatabaseInstance(self, "Instance",
     cluster=cluster,
     instance_type=neptune.InstanceType.R5_LARGE
 )
 ```
 
+## Automatic minor version upgrades
+
+By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
+the engine of the entire cluster to the latest minor version after a stabilization
+window of 2 to 3 weeks.
+
+```python
+# Example automatically generated from non-compiling source. May contain errors.
+neptune.DatabaseCluster(stack, "Cluster",
+    vpc=vpc,
+    instance_type=InstanceType.R5_LARGE,
+    auto_minor_version_upgrade=True
+)
+```
+
```

### Comparing `aws-cdk.aws-neptune-alpha-2.8.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/SOURCES.txt` & `aws-cdk.aws-neptune-alpha-2.9.0a0/src/aws_cdk.aws_neptune_alpha.egg-info/SOURCES.txt`

 * *Files 16% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/aws_cdk.aws_neptune_alpha.egg-info/SOURCES.txt
 src/aws_cdk.aws_neptune_alpha.egg-info/dependency_links.txt
 src/aws_cdk.aws_neptune_alpha.egg-info/requires.txt
 src/aws_cdk.aws_neptune_alpha.egg-info/top_level.txt
 src/aws_cdk/aws_neptune_alpha/__init__.py
 src/aws_cdk/aws_neptune_alpha/py.typed
 src/aws_cdk/aws_neptune_alpha/_jsii/__init__.py
-src/aws_cdk/aws_neptune_alpha/_jsii/aws-neptune-alpha@2.8.0-alpha.0.jsii.tgz
+src/aws_cdk/aws_neptune_alpha/_jsii/aws-neptune-alpha@2.9.0-alpha.0.jsii.tgz
```

