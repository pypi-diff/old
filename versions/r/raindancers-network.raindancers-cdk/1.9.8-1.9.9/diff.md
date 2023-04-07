# Comparing `tmp/raindancers-network.raindancers-cdk-1.9.8.tar.gz` & `tmp/raindancers-network.raindancers-cdk-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "raindancers-network.raindancers-cdk-1.9.8.tar", last modified: Wed Jan 11 15:28:10 2023, max compression
+gzip compressed data, was "raindancers-network.raindancers-cdk-1.9.9.tar", last modified: Wed Jan 11 16:00:48 2023, max compression
```

## Comparing `raindancers-network.raindancers-cdk-1.9.8.tar` & `raindancers-network.raindancers-cdk-1.9.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 15:28:10.299244 raindancers-network.raindancers-cdk-1.9.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     6265 2023-01-11 15:28:10.299244 raindancers-network.raindancers-cdk-1.9.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5291 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-11 15:28:10.299244 raindancers-network.raindancers-cdk-1.9.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1763 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 15:28:10.295244 raindancers-network.raindancers-cdk-1.9.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 15:28:10.295244 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/
--rw-r--r--   0 runner    (1001) docker     (123)   234479 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 15:28:10.295244 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      418 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   502837 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/_jsii/raindancers-network@1.9.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-11 15:27:55.000000 raindancers-network.raindancers-cdk-1.9.8/src/Evpc/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 15:28:10.299244 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6265 2023-01-11 15:28:09.000000 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-11 15:28:10.000000 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-11 15:28:09.000000 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-11 15:28:10.000000 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-11 15:28:10.000000 raindancers-network.raindancers-cdk-1.9.8/src/raindancers_network.raindancers_cdk.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2094 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1763 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/
+-rw-r--r--   0 runner    (1001) docker     (123)   230308 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      418 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   501286 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/_jsii/raindancers-network@1.9.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-11 16:00:34.000000 raindancers-network.raindancers-cdk-1.9.9/src/Evpc/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-11 16:00:48.415703 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2094 2023-01-11 16:00:47.000000 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-11 16:00:48.000000 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-11 16:00:47.000000 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-11 16:00:48.000000 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-11 16:00:48.000000 raindancers-network.raindancers-cdk-1.9.9/src/raindancers_network.raindancers_cdk.egg-info/top_level.txt
```

### Comparing `raindancers-network.raindancers-cdk-1.9.8/LICENSE` & `raindancers-network.raindancers-cdk-1.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `raindancers-network.raindancers-cdk-1.9.8/setup.py` & `raindancers-network.raindancers-cdk-1.9.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "raindancers-network.raindancers-cdk",
-    "version": "1.9.8",
+    "version": "1.9.9",
     "description": "Extensions to the ec2.Vpc Constructs",
     "license": "Apache-2.0",
     "url": "https://github.com/raindancers/raindancers-network.raindancers-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Andrew Frazer<andrew.frazer@raindancers.co.nz>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "Evpc",
         "Evpc._jsii"
     ],
     "package_data": {
         "Evpc._jsii": [
-            "raindancers-network@1.9.8.jsii.tgz"
+            "raindancers-network@1.9.9.jsii.tgz"
         ],
         "Evpc": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `raindancers-network.raindancers-cdk-1.9.8/src/Evpc/__init__.py` & `raindancers-network.raindancers-cdk-1.9.9/src/Evpc/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,149 +1,23 @@
 '''
 # Raindancers Network Construct Library...
 
-The raindancers network package contains  constructs that construct to provide easy to use abstractions, particually for using in an enterprise network, with Transit Gateways, Cloudwan, Network Firewalls, and DNS.
+The raindancers network package contains  constructs that construct to provide easy to use abstractions, particually for using in an enterprise network, with Transit Gateways, Cloudwan, Network Firewalls.
 
-All of the methods that work with ec2.Vpc, work with Evpc.   Refer to [the ec2.Vpc Documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2-readme.html)
+Note: This Construct Library is functional, but there is no promise thate that breaking changes could occur.    While this construct is highly opinionated, it seeks to solve a wide set of scenerios that its author has faced, and problems that others have described.   The author of this construct encourages and welcome PR's.  Please raise an issue to start
 
-Note: This Construct Library is functional, but it is possible that breaking changes could occur.   This construct is highly opinionated, but seeks to solve a wide set of scenerios that its author has faced.   The authors of this construct encourage and welcome PR's.  Please raise an issue to start
+The EnterpriseVPC provides addtional methods from the standard ec2.Vpc construct, while maintaining compatiblity, so it can be used with other constructs that use the ec2.Vpc
 
-```
-import { EnterpriseVPC } from 'raindancers-cdk.raindancers-network';
-```
+A getting started example provides guidence in using the constructs.
 
-## EnterpriseVPC
+* [Getting Started](./docs/gettingstarted.md)
+* [Deploying VPC with Cloudwan](./docs/deployVpcts.md)
+* [Create A shared Egress VPC](./docs/egress.md)
 
-Many projects need a Virtual Private Cloud network.  This can be provided by creating an instance of `EVpc` :
-
-```
-const shineyEvpc = new Evpc(this, 'EnterpriseVPC');
-```
-
-### Using IPAM address Pool for Addressing in Cidr
-
-Creating a vpc that gets its Ip Address allocation from an IPAM pool, requires providing a netmask and ipamPoolId.  Only one of ipamPoolId or cidr is allowed.    The underlying resource that creates a VPC natively consumes IPAM.
-
-```
-const shineyEpvc = new Evpc(this, 'EnterpriseVPC', {
-	ipamPoolId: 'pool-00000122344',
-	netmaskLength: 24
-})
-```
-
-### Centralised Flow Logs and Athena Querys.
-
-This construct will create a flow log, that is written to a centralised flow log bucket. The construct expects to find the bucket name in they key `flowlogbucket` in cdk.json. (This typically is in the log-archive acount, set up by Control Tower). This requires that the buckets policy allows access. To DISABLE this feature, set the disableFLowLog to `false`.  By default the flow log will aggregate flow logs at a 10minute internal.  To enable aggregation on a 1 minute interval, set the oneMinuteFlowLogs property to true.
-
-The construct will also create a set of Athena querys and glue jobs that will provide an easy way to query the flow logs from within the account that the vpc is created.
-
-```
-const shineyEpvc = new Evpc(this, 'EnterpriseVPC', {
-	disableFlowlog: false,
-	oneMinuteFlowLogs: true
-})
-```
-
-### Subnets
-
-The construct creates subnets in the same way that the ec2.Vpc construct does.   in order to connect the VPC to a cloudWAN, the construct requires that a subnet group called 'linknets' is created.  This is where the attachments for cloudwan will be created.
-
-```
-const shiney = new Evpc(this, 'Shineyvpc', {
-	r53InternalZoneName: 'thing.domain.com'
-	ipamPoolId: 'ip-pool-id',
-	subnetConfiguration: [
-		{
-			name: 'linknet',
-			subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
-			cidrMask: 28
-		},
-	]
-	}
-)
-```
-
-### Attaching a VPC to cloud wan.
-
-To attach a vpc to a cloudwan, use the attachToCloudWan method, for example to connect to a core network 'AcmeCore' and segment 'AppsProd';  The attachments to cloudwan will be made in the linknets subnets
-
-```
-const shineyVpc = new Evpc: Evpc;
-shineyVpc.attachToCloudWan('AcmeCore', 'AppsProd')
-```
-
-This method returns the attachmentId, which is used in the routing methods.
-
-## Attaching a VPC to a TransitGateway in Appliance Mode.
-
-(very beta and potentially buggy)
-TODO: Write doc's
-
-### Adding Routes to Cloudwan attached VPC's
-
-A number of convience methods are provided to add routes to the cloudwan; For example to add a default route (0/0) in all privatesubnets
-
-```
-shineyVpc.addRouteForPrivateSubnetstoCloudwan('0.0.0.0/0', attachmentId)
-```
-
-Similar method exisits for PublicSubnets, TransitGateways Instances and Firewalls.
-
-### Internal Route53 Zones
-
-A internal Route53 Zone can be created and associated with the Vpc, by specifying the r53InternalZoneName property
-
-```
-const shineyEpvc = new Evpc(this, 'EnterpriseVPC', {
-	r53InternalZoneName: 'internal.somedomain.cloud',
-})
-```
-
-## DNS Methods
-
-To do.
-associateVPCZonewithCentralVPC
-associateSharedRoute53ResolverRules
-
-# IPAM
-
-This package contains constructs for integrating with **Amazon IP Address Manager**.  While the IPAM Service is GA and provides a very useful service, only a handful of services natively support ingesting a IPAM allocated address ( ie, VPC ).
-
-For futher infomation on Amazon IPAM, see the [IPAM Documentation](https://docs.aws.amazon.com/vpc/latest/ipam/getting-started-ipam.html)
-
-### Using IPAM for IPsec VPN tunnel addresses
-
-The Cidr ranges for IPSec VPN Tunnels must comply to several constraints.
-
-* they must be a /30
-* they must be subnets of 169.254.0.0/16
-* they must not conflict with the reserved subnets ( see docs above )
-
-The following example demonstrates how the constructs can be used to create an address Pool and suitable allocations, that met these criteria
-
-```
-
-const tunnelIPAMPool = new kapua_ipam.IpsecTunnelPool(this, 'ipampool', {
-	ipamScopeId: 'ipam-scope-00112233445566778',
-	cidr: '169.254.100.0/27',
-	description: 'Addressing for IPSec Tunnels between ap-southeast-2 and on prem',
-	name: 'ToOnPremVPNTunnels'
-})
-
-
-var assignedCidrs: string[] = []
-
-const tunnelAllocation = new GetTunnelAddressPair(this, `${name}tunneladdress`,{
-	ipamPoolId: tunnelIPAMPool.attrIpamPoolId,
-	name: name
-})
-
-assignedCidrs = tunnelAllocation.assignedCidrPair
-
-```
+Slack:  A good way to to get help with this construct, is to join the [cdk.dev] (https://cdk.dev/) slack channel.
 '''
 import abc
 import builtins
 import datetime
 import enum
 import typing
```

