# Comparing `tmp/cloudsnorkel.cdk-github-runners-0.9.1.tar.gz` & `tmp/cloudsnorkel.cdk-github-runners-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cloudsnorkel.cdk-github-runners-0.9.1.tar", last modified: Thu Apr  6 18:23:34 2023, max compression
+gzip compressed data, was "cloudsnorkel.cdk-github-runners-0.9.2.tar", last modified: Thu Apr  6 21:57:29 2023, max compression
```

## Comparing `cloudsnorkel.cdk-github-runners-0.9.1.tar` & `cloudsnorkel.cdk-github-runners-0.9.2.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.348339 cloudsnorkel.cdk-github-runners-0.9.1/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    12603 2023-04-06 18:23:34.348339 cloudsnorkel.cdk-github-runners-0.9.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    11544 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:23:34.348339 cloudsnorkel.cdk-github-runners-0.9.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1974 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.344339 cloudsnorkel.cdk-github-runners-0.9.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.344339 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.344339 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/
--rw-r--r--   0 runner    (1001) docker     (123)   495846 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.344339 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      430 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)  1964979 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/_jsii/cdk-github-runners@0.9.1.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:23:22.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:23:34.344339 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12603 2023-04-06 18:23:34.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      570 2023-04-06 18:23:34.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:23:34.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-04-06 18:23:34.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 18:23:34.000000 cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.175478 cloudsnorkel.cdk-github-runners-0.9.2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    12603 2023-04-06 21:57:29.175478 cloudsnorkel.cdk-github-runners-0.9.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    11544 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 21:57:29.175478 cloudsnorkel.cdk-github-runners-0.9.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1974 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.171478 cloudsnorkel.cdk-github-runners-0.9.2/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.171478 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.171478 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/
+-rw-r--r--   0 runner    (1001) docker     (123)   510356 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.171478 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      430 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)  1977087 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/_jsii/cdk-github-runners@0.9.2.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:57:17.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:57:29.171478 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12603 2023-04-06 21:57:29.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      570 2023-04-06 21:57:29.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:57:29.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-04-06 21:57:29.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 21:57:29.000000 cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/top_level.txt
```

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/LICENSE` & `cloudsnorkel.cdk-github-runners-0.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/PKG-INFO` & `cloudsnorkel.cdk-github-runners-0.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cloudsnorkel.cdk-github-runners
-Version: 0.9.1
+Version: 0.9.2
 Summary: CDK construct to create GitHub Actions self-hosted runners. A webhook listens to events and creates ephemeral runners on the fly.
 Home-page: https://github.com/CloudSnorkel/cdk-github-runners.git
 Author: Amir Szekely<amir@cloudsnorkel.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/CloudSnorkel/cdk-github-runners.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/README.md` & `cloudsnorkel.cdk-github-runners-0.9.2/README.md`

 * *Files identical despite different names*

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/setup.py` & `cloudsnorkel.cdk-github-runners-0.9.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cloudsnorkel.cdk-github-runners",
-    "version": "0.9.1",
+    "version": "0.9.2",
     "description": "CDK construct to create GitHub Actions self-hosted runners. A webhook listens to events and creates ephemeral runners on the fly.",
     "license": "Apache-2.0",
     "url": "https://github.com/CloudSnorkel/cdk-github-runners.git",
     "long_description_content_type": "text/markdown",
     "author": "Amir Szekely<amir@cloudsnorkel.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cloudsnorkel.cdk_github_runners",
         "cloudsnorkel.cdk_github_runners._jsii"
     ],
     "package_data": {
         "cloudsnorkel.cdk_github_runners._jsii": [
-            "cdk-github-runners@0.9.1.jsii.tgz"
+            "cdk-github-runners@0.9.2.jsii.tgz"
         ],
         "cloudsnorkel.cdk_github_runners": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel/cdk_github_runners/__init__.py` & `cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel/cdk_github_runners/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -526,14 +526,98 @@
 
     def __repr__(self) -> str:
         return "AmiBuilderProps(%s)" % ", ".join(
             k + "=" + repr(v) for k, v in self._values.items()
         )
 
 
+@jsii.data_type(
+    jsii_type="@cloudsnorkel/cdk-github-runners.ApiGatewayAccessProps",
+    jsii_struct_bases=[],
+    name_mapping={
+        "allowed_ips": "allowedIps",
+        "allowed_security_groups": "allowedSecurityGroups",
+        "allowed_vpc": "allowedVpc",
+    },
+)
+class ApiGatewayAccessProps:
+    def __init__(
+        self,
+        *,
+        allowed_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
+        allowed_security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
+        allowed_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
+    ) -> None:
+        '''
+        :param allowed_ips: (experimental) List of IP addresses in CIDR notation that are allowed to access the API Gateway. If not specified on public API Gateway, all IP addresses are allowed. If not specified on private API Gateway, no IP addresses are allowed (but specified security groups are).
+        :param allowed_security_groups: (experimental) List of security groups that are allowed to access the API Gateway. Only works for private API Gateways with {@link allowedVpc}.
+        :param allowed_vpc: (experimental) Creates a private API Gateway and allows access from the specified VPC.
+
+        :stability: experimental
+        '''
+        if __debug__:
+            type_hints = typing.get_type_hints(_typecheckingstub__0230281aea2f0096e32af8e4f02c3c351aada0957c217590514bfc5f6f656b0e)
+            check_type(argname="argument allowed_ips", value=allowed_ips, expected_type=type_hints["allowed_ips"])
+            check_type(argname="argument allowed_security_groups", value=allowed_security_groups, expected_type=type_hints["allowed_security_groups"])
+            check_type(argname="argument allowed_vpc", value=allowed_vpc, expected_type=type_hints["allowed_vpc"])
+        self._values: typing.Dict[builtins.str, typing.Any] = {}
+        if allowed_ips is not None:
+            self._values["allowed_ips"] = allowed_ips
+        if allowed_security_groups is not None:
+            self._values["allowed_security_groups"] = allowed_security_groups
+        if allowed_vpc is not None:
+            self._values["allowed_vpc"] = allowed_vpc
+
+    @builtins.property
+    def allowed_ips(self) -> typing.Optional[typing.List[builtins.str]]:
+        '''(experimental) List of IP addresses in CIDR notation that are allowed to access the API Gateway.
+
+        If not specified on public API Gateway, all IP addresses are allowed.
+
+        If not specified on private API Gateway, no IP addresses are allowed (but specified security groups are).
+
+        :stability: experimental
+        '''
+        result = self._values.get("allowed_ips")
+        return typing.cast(typing.Optional[typing.List[builtins.str]], result)
+
+    @builtins.property
+    def allowed_security_groups(
+        self,
+    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]]:
+        '''(experimental) List of security groups that are allowed to access the API Gateway.
+
+        Only works for private API Gateways with {@link allowedVpc}.
+
+        :stability: experimental
+        '''
+        result = self._values.get("allowed_security_groups")
+        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]], result)
+
+    @builtins.property
+    def allowed_vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
+        '''(experimental) Creates a private API Gateway and allows access from the specified VPC.
+
+        :stability: experimental
+        '''
+        result = self._values.get("allowed_vpc")
+        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)
+
+    def __eq__(self, rhs: typing.Any) -> builtins.bool:
+        return isinstance(rhs, self.__class__) and rhs._values == self._values
+
+    def __ne__(self, rhs: typing.Any) -> builtins.bool:
+        return not (rhs == self)
+
+    def __repr__(self) -> str:
+        return "ApiGatewayAccessProps(%s)" % ", ".join(
+            k + "=" + repr(v) for k, v in self._values.items()
+        )
+
+
 class Architecture(
     metaclass=jsii.JSIIMeta,
     jsii_type="@cloudsnorkel/cdk-github-runners.Architecture",
 ):
     '''(experimental) CPU architecture enum for an image.
 
     :stability: experimental
@@ -1350,44 +1434,53 @@
         *,
         allow_public_subnet: typing.Optional[builtins.bool] = None,
         extra_certificates: typing.Optional[builtins.str] = None,
         idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         log_options: typing.Optional[typing.Union["LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
         providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
         security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
+        setup_access: typing.Optional["LambdaAccess"] = None,
+        status_access: typing.Optional["LambdaAccess"] = None,
         vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
         vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
+        webhook_access: typing.Optional["LambdaAccess"] = None,
     ) -> None:
         '''
         :param scope: -
         :param id: -
         :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
         :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates }:: const imageBuilder = CodeBuildRunnerProvider.imageBuilder(this, 'Image Builder with Certs'); imageBuilder.addComponent(RunnerImageComponent.extraCertificates('path-to-my-extra-certs-folder/certs.pem', 'private-ca'); const provider = new CodeBuildRunnerProvider(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
         :param idle_timeout: (experimental) Time to wait before stopping a runner that remains idle. If the user cancelled the job, or if another runner stole it, this stops the runner to avoid wasting resources. Default: 10 minutes
         :param log_options: (experimental) Logging options for the state machine that manages the runners. Default: no logs
         :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
         :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
+        :param setup_access: (experimental) Access configuration for the setup function. Once you finish the setup process, you can set this to ``LambdaAccess.noAccess()`` to remove access to the setup function. You can also use ``LambdaAccess.apiGateway({ allowedIps: ['my-ip/0']})`` to limit access to your IP only. Default: LambdaAccess.lambdaUrl()
+        :param status_access: (experimental) Access configuration for the status function. This function returns a lot of sensitive information about the runner, so you should only allow access to it from trusted IPs, if at all. Default: LambdaAccess.noAccess()
         :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
         :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
+        :param webhook_access: (experimental) Access configuration for the webhook function. This function is called by GitHub when a new workflow job is scheduled. For an extra layer of security, you can set this to ``LambdaAccess.apiGateway({ allowedIps: LambdaAccess.githubWebhookIps() })``. You can also set this to ``LambdaAccess.privateApiGateway()`` if your GitHub Enterprise Server is hosted in a VPC. This will create an API Gateway endpoint that's only accessible from within the VPC. *WARNING*: changing access type may change the URL. When the URL changes, you must update GitHub as well. Default: LambdaAccess.lambdaUrl()
 
         :stability: experimental
         '''
         if __debug__:
             type_hints = typing.get_type_hints(_typecheckingstub__c1a45de07d09ed9f4fd0b9051aeff4571ceda633f49c0b30a5058ad6d72fad18)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = GitHubRunnersProps(
             allow_public_subnet=allow_public_subnet,
             extra_certificates=extra_certificates,
             idle_timeout=idle_timeout,
             log_options=log_options,
             providers=providers,
             security_group=security_group,
+            setup_access=setup_access,
+            status_access=status_access,
             vpc=vpc,
             vpc_subnets=vpc_subnets,
+            webhook_access=webhook_access,
         )
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="metricFailed")
     def metric_failed(
         self,
@@ -1613,41 +1706,50 @@
     name_mapping={
         "allow_public_subnet": "allowPublicSubnet",
         "extra_certificates": "extraCertificates",
         "idle_timeout": "idleTimeout",
         "log_options": "logOptions",
         "providers": "providers",
         "security_group": "securityGroup",
+        "setup_access": "setupAccess",
+        "status_access": "statusAccess",
         "vpc": "vpc",
         "vpc_subnets": "vpcSubnets",
+        "webhook_access": "webhookAccess",
     },
 )
 class GitHubRunnersProps:
     def __init__(
         self,
         *,
         allow_public_subnet: typing.Optional[builtins.bool] = None,
         extra_certificates: typing.Optional[builtins.str] = None,
         idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         log_options: typing.Optional[typing.Union["LogOptions", typing.Dict[builtins.str, typing.Any]]] = None,
         providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
         security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
+        setup_access: typing.Optional["LambdaAccess"] = None,
+        status_access: typing.Optional["LambdaAccess"] = None,
         vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
         vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
+        webhook_access: typing.Optional["LambdaAccess"] = None,
     ) -> None:
         '''(experimental) Properties for GitHubRunners.
 
         :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
         :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates }:: const imageBuilder = CodeBuildRunnerProvider.imageBuilder(this, 'Image Builder with Certs'); imageBuilder.addComponent(RunnerImageComponent.extraCertificates('path-to-my-extra-certs-folder/certs.pem', 'private-ca'); const provider = new CodeBuildRunnerProvider(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
         :param idle_timeout: (experimental) Time to wait before stopping a runner that remains idle. If the user cancelled the job, or if another runner stole it, this stops the runner to avoid wasting resources. Default: 10 minutes
         :param log_options: (experimental) Logging options for the state machine that manages the runners. Default: no logs
         :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
         :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
+        :param setup_access: (experimental) Access configuration for the setup function. Once you finish the setup process, you can set this to ``LambdaAccess.noAccess()`` to remove access to the setup function. You can also use ``LambdaAccess.apiGateway({ allowedIps: ['my-ip/0']})`` to limit access to your IP only. Default: LambdaAccess.lambdaUrl()
+        :param status_access: (experimental) Access configuration for the status function. This function returns a lot of sensitive information about the runner, so you should only allow access to it from trusted IPs, if at all. Default: LambdaAccess.noAccess()
         :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
         :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
+        :param webhook_access: (experimental) Access configuration for the webhook function. This function is called by GitHub when a new workflow job is scheduled. For an extra layer of security, you can set this to ``LambdaAccess.apiGateway({ allowedIps: LambdaAccess.githubWebhookIps() })``. You can also set this to ``LambdaAccess.privateApiGateway()`` if your GitHub Enterprise Server is hosted in a VPC. This will create an API Gateway endpoint that's only accessible from within the VPC. *WARNING*: changing access type may change the URL. When the URL changes, you must update GitHub as well. Default: LambdaAccess.lambdaUrl()
 
         :stability: experimental
         '''
         if isinstance(log_options, dict):
             log_options = LogOptions(**log_options)
         if isinstance(vpc_subnets, dict):
             vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
@@ -1655,33 +1757,42 @@
             type_hints = typing.get_type_hints(_typecheckingstub__4db12e50ec9bf1582f493963c13640e2d81a3a4afae3df834ecce0bf88f4706c)
             check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
             check_type(argname="argument extra_certificates", value=extra_certificates, expected_type=type_hints["extra_certificates"])
             check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
             check_type(argname="argument log_options", value=log_options, expected_type=type_hints["log_options"])
             check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
             check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
+            check_type(argname="argument setup_access", value=setup_access, expected_type=type_hints["setup_access"])
+            check_type(argname="argument status_access", value=status_access, expected_type=type_hints["status_access"])
             check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
             check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
+            check_type(argname="argument webhook_access", value=webhook_access, expected_type=type_hints["webhook_access"])
         self._values: typing.Dict[builtins.str, typing.Any] = {}
         if allow_public_subnet is not None:
             self._values["allow_public_subnet"] = allow_public_subnet
         if extra_certificates is not None:
             self._values["extra_certificates"] = extra_certificates
         if idle_timeout is not None:
             self._values["idle_timeout"] = idle_timeout
         if log_options is not None:
             self._values["log_options"] = log_options
         if providers is not None:
             self._values["providers"] = providers
         if security_group is not None:
             self._values["security_group"] = security_group
+        if setup_access is not None:
+            self._values["setup_access"] = setup_access
+        if status_access is not None:
+            self._values["status_access"] = status_access
         if vpc is not None:
             self._values["vpc"] = vpc
         if vpc_subnets is not None:
             self._values["vpc_subnets"] = vpc_subnets
+        if webhook_access is not None:
+            self._values["webhook_access"] = webhook_access
 
     @builtins.property
     def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Allow management functions to run in public subnets.
 
         Lambda Functions in a public subnet can NOT access the internet.
 
@@ -1766,14 +1877,40 @@
 
         :stability: experimental
         '''
         result = self._values.get("security_group")
         return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup], result)
 
     @builtins.property
+    def setup_access(self) -> typing.Optional["LambdaAccess"]:
+        '''(experimental) Access configuration for the setup function.
+
+        Once you finish the setup process, you can set this to ``LambdaAccess.noAccess()`` to remove access to the setup function. You can also use ``LambdaAccess.apiGateway({ allowedIps: ['my-ip/0']})`` to limit access to your IP only.
+
+        :default: LambdaAccess.lambdaUrl()
+
+        :stability: experimental
+        '''
+        result = self._values.get("setup_access")
+        return typing.cast(typing.Optional["LambdaAccess"], result)
+
+    @builtins.property
+    def status_access(self) -> typing.Optional["LambdaAccess"]:
+        '''(experimental) Access configuration for the status function.
+
+        This function returns a lot of sensitive information about the runner, so you should only allow access to it from trusted IPs, if at all.
+
+        :default: LambdaAccess.noAccess()
+
+        :stability: experimental
+        '''
+        result = self._values.get("status_access")
+        return typing.cast(typing.Optional["LambdaAccess"], result)
+
+    @builtins.property
     def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
         '''(experimental) VPC used for all management functions.
 
         Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
 
         :stability: experimental
         '''
@@ -1787,14 +1924,31 @@
         Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
 
         :stability: experimental
         '''
         result = self._values.get("vpc_subnets")
         return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)
 
+    @builtins.property
+    def webhook_access(self) -> typing.Optional["LambdaAccess"]:
+        '''(experimental) Access configuration for the webhook function.
+
+        This function is called by GitHub when a new workflow job is scheduled. For an extra layer of security, you can set this to ``LambdaAccess.apiGateway({ allowedIps: LambdaAccess.githubWebhookIps() })``.
+
+        You can also set this to ``LambdaAccess.privateApiGateway()`` if your GitHub Enterprise Server is hosted in a VPC. This will create an API Gateway endpoint that's only accessible from within the VPC.
+
+        *WARNING*: changing access type may change the URL. When the URL changes, you must update GitHub as well.
+
+        :default: LambdaAccess.lambdaUrl()
+
+        :stability: experimental
+        '''
+        result = self._values.get("webhook_access")
+        return typing.cast(typing.Optional["LambdaAccess"], result)
+
     def __eq__(self, rhs: typing.Any) -> builtins.bool:
         return isinstance(rhs, self.__class__) and rhs._values == self._values
 
     def __ne__(self, rhs: typing.Any) -> builtins.bool:
         return not (rhs == self)
 
     def __repr__(self) -> str:
@@ -2679,14 +2833,109 @@
 
     def __repr__(self) -> str:
         return "ImageBuilderComponentProperties(%s)" % ", ".join(
             k + "=" + repr(v) for k, v in self._values.items()
         )
 
 
+class LambdaAccess(
+    metaclass=jsii.JSIIAbstractClass,
+    jsii_type="@cloudsnorkel/cdk-github-runners.LambdaAccess",
+):
+    '''(experimental) Access configuration options for Lambda functions like setup and webhook function.
+
+    Use this to limit access to these functions.
+
+    :stability: experimental
+    '''
+
+    def __init__(self) -> None:
+        '''
+        :stability: experimental
+        '''
+        jsii.create(self.__class__, self, [])
+
+    @jsii.member(jsii_name="apiGateway")
+    @builtins.classmethod
+    def api_gateway(
+        cls,
+        *,
+        allowed_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
+        allowed_security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
+        allowed_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
+    ) -> "LambdaAccess":
+        '''(experimental) Provide access using API Gateway.
+
+        This is the most secure option, but requires additional configuration. It allows you to limit access to specific IP addresses and even to a specific VPC.
+
+        To limit access to GitHub.com use::
+
+           LambdaAccess.apiGateway({
+             allowedIps: LambdaAccess.githubWebhookIps(),
+           });
+
+        Alternatively, get and manually update the list manually with::
+
+           curl https://api.github.com/meta | jq .hooks
+
+        :param allowed_ips: (experimental) List of IP addresses in CIDR notation that are allowed to access the API Gateway. If not specified on public API Gateway, all IP addresses are allowed. If not specified on private API Gateway, no IP addresses are allowed (but specified security groups are).
+        :param allowed_security_groups: (experimental) List of security groups that are allowed to access the API Gateway. Only works for private API Gateways with {@link allowedVpc}.
+        :param allowed_vpc: (experimental) Creates a private API Gateway and allows access from the specified VPC.
+
+        :stability: experimental
+        '''
+        props = ApiGatewayAccessProps(
+            allowed_ips=allowed_ips,
+            allowed_security_groups=allowed_security_groups,
+            allowed_vpc=allowed_vpc,
+        )
+
+        return typing.cast("LambdaAccess", jsii.sinvoke(cls, "apiGateway", [props]))
+
+    @jsii.member(jsii_name="githubWebhookIps")
+    @builtins.classmethod
+    def github_webhook_ips(cls) -> typing.List[builtins.str]:
+        '''(experimental) Downloads the list of IP addresses used by GitHub.com for webhooks.
+
+        Note that downloading dynamic data during deployment is not recommended in CDK. This is a workaround for the lack of a better solution.
+
+        :stability: experimental
+        '''
+        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "githubWebhookIps", []))
+
+    @jsii.member(jsii_name="lambdaUrl")
+    @builtins.classmethod
+    def lambda_url(cls) -> "LambdaAccess":
+        '''(experimental) Provide access using Lambda URL.
+
+        This is the default and simplest option. It puts no limits on the requester, but the Lambda functions themselves authenticate every request.
+
+        :stability: experimental
+        '''
+        return typing.cast("LambdaAccess", jsii.sinvoke(cls, "lambdaUrl", []))
+
+    @jsii.member(jsii_name="noAccess")
+    @builtins.classmethod
+    def no_access(cls) -> "LambdaAccess":
+        '''(experimental) Disables access to the configured Lambda function.
+
+        This is useful for the setup function after setup is done.
+
+        :stability: experimental
+        '''
+        return typing.cast("LambdaAccess", jsii.sinvoke(cls, "noAccess", []))
+
+
+class _LambdaAccessProxy(LambdaAccess):
+    pass
+
+# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
+typing.cast(typing.Any, LambdaAccess).__jsii_proxy_class__ = lambda : _LambdaAccessProxy
+
+
 @jsii.implements(IRunnerProvider)
 class LambdaRunnerProvider(
     _constructs_77d1e7e8.Construct,
     metaclass=jsii.JSIIMeta,
     jsii_type="@cloudsnorkel/cdk-github-runners.LambdaRunnerProvider",
 ):
     '''(experimental) GitHub Actions runner provider using Lambda to execute jobs.
@@ -8770,14 +9019,15 @@
 
         jsii.create(self.__class__, self, [scope, id, props])
 
 
 __all__ = [
     "AmiBuilder",
     "AmiBuilderProps",
+    "ApiGatewayAccessProps",
     "Architecture",
     "AwsImageBuilderRunnerImageBuilderProps",
     "CodeBuildImageBuilder",
     "CodeBuildImageBuilderProps",
     "CodeBuildRunner",
     "CodeBuildRunnerImageBuilderProps",
     "CodeBuildRunnerProvider",
@@ -8796,14 +9046,15 @@
     "IRunnerImageBuilder",
     "IRunnerImageStatus",
     "IRunnerProvider",
     "IRunnerProviderStatus",
     "ImageBuilderAsset",
     "ImageBuilderComponent",
     "ImageBuilderComponentProperties",
+    "LambdaAccess",
     "LambdaRunner",
     "LambdaRunnerProvider",
     "LambdaRunnerProviderProps",
     "LinuxUbuntuComponents",
     "LogOptions",
     "Os",
     "ProviderRetryOptions",
@@ -8839,14 +9090,23 @@
     security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
     subnet_selection: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
     vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
 ) -> None:
     """Type checking stubs"""
     pass
 
+def _typecheckingstub__0230281aea2f0096e32af8e4f02c3c351aada0957c217590514bfc5f6f656b0e(
+    *,
+    allowed_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
+    allowed_security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
+    allowed_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
 def _typecheckingstub__197fbc91031fbef228119c4ea4b7d54d7ee7ae2efdfedf7354f2313378ee5db9(
     instance_type: _aws_cdk_aws_ec2_ceddda9d.InstanceType,
 ) -> None:
     """Type checking stubs"""
     pass
 
 def _typecheckingstub__8c78353047f5b727c68147df5fbcc6c4d5381f43b731bacf43f3e3ec823bc835(
@@ -8920,30 +9180,36 @@
     *,
     allow_public_subnet: typing.Optional[builtins.bool] = None,
     extra_certificates: typing.Optional[builtins.str] = None,
     idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
     log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
     providers: typing.Optional[typing.Sequence[IRunnerProvider]] = None,
     security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
+    setup_access: typing.Optional[LambdaAccess] = None,
+    status_access: typing.Optional[LambdaAccess] = None,
     vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
     vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
+    webhook_access: typing.Optional[LambdaAccess] = None,
 ) -> None:
     """Type checking stubs"""
     pass
 
 def _typecheckingstub__4db12e50ec9bf1582f493963c13640e2d81a3a4afae3df834ecce0bf88f4706c(
     *,
     allow_public_subnet: typing.Optional[builtins.bool] = None,
     extra_certificates: typing.Optional[builtins.str] = None,
     idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
     log_options: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
     providers: typing.Optional[typing.Sequence[IRunnerProvider]] = None,
     security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
+    setup_access: typing.Optional[LambdaAccess] = None,
+    status_access: typing.Optional[LambdaAccess] = None,
     vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
     vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
+    webhook_access: typing.Optional[LambdaAccess] = None,
 ) -> None:
     """Type checking stubs"""
     pass
 
 def _typecheckingstub__d777163bee0bc9ca3b1de75cfdc0b96318f78ad3295795250df400a5f5846942(
     state_machine_role: _aws_cdk_aws_iam_ceddda9d.IGrantable,
 ) -> None:
```

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/PKG-INFO` & `cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cloudsnorkel.cdk-github-runners
-Version: 0.9.1
+Version: 0.9.2
 Summary: CDK construct to create GitHub Actions self-hosted runners. A webhook listens to events and creates ephemeral runners on the fly.
 Home-page: https://github.com/CloudSnorkel/cdk-github-runners.git
 Author: Amir Szekely<amir@cloudsnorkel.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/CloudSnorkel/cdk-github-runners.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cloudsnorkel.cdk-github-runners-0.9.1/src/cloudsnorkel.cdk_github_runners.egg-info/SOURCES.txt` & `cloudsnorkel.cdk-github-runners-0.9.2/src/cloudsnorkel.cdk_github_runners.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cloudsnorkel.cdk_github_runners.egg-info/SOURCES.txt
 src/cloudsnorkel.cdk_github_runners.egg-info/dependency_links.txt
 src/cloudsnorkel.cdk_github_runners.egg-info/requires.txt
 src/cloudsnorkel.cdk_github_runners.egg-info/top_level.txt
 src/cloudsnorkel/cdk_github_runners/__init__.py
 src/cloudsnorkel/cdk_github_runners/py.typed
 src/cloudsnorkel/cdk_github_runners/_jsii/__init__.py
-src/cloudsnorkel/cdk_github_runners/_jsii/cdk-github-runners@0.9.1.jsii.tgz
+src/cloudsnorkel/cdk_github_runners/_jsii/cdk-github-runners@0.9.2.jsii.tgz
```

