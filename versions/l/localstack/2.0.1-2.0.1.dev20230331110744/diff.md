# Comparing `tmp/localstack-2.0.1.tar.gz` & `tmp/localstack-2.0.1.dev20230331110744.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "localstack-2.0.1.tar", last modified: Fri Apr  7 11:08:05 2023, max compression
+gzip compressed data, was "localstack-2.0.1.dev20230331110744.tar", last modified: Fri Mar 31 11:10:55 2023, max compression
```

## Comparing `localstack-2.0.1.tar` & `localstack-2.0.1.dev20230331110744.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-04-07 11:08:05.400985 localstack-2.0.1/
--rw-rw-r--   0 runner    (1000) runner    (1001)    11400 2023-04-07 11:08:05.400985 localstack-2.0.1/PKG-INFO
-drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-04-07 11:08:05.400985 localstack-2.0.1/localstack.egg-info/
--rw-rw-r--   0 runner    (1000) runner    (1001)    11400 2023-04-07 11:08:05.000000 localstack-2.0.1/localstack.egg-info/PKG-INFO
--rw-rw-r--   0 runner    (1000) runner    (1001)      204 2023-04-07 11:08:05.000000 localstack-2.0.1/localstack.egg-info/SOURCES.txt
--rw-rw-r--   0 runner    (1000) runner    (1001)        1 2023-04-07 11:08:05.000000 localstack-2.0.1/localstack.egg-info/dependency_links.txt
--rw-rw-r--   0 runner    (1000) runner    (1001)      169 2023-04-07 11:08:05.000000 localstack-2.0.1/localstack.egg-info/requires.txt
--rw-rw-r--   0 runner    (1000) runner    (1001)       15 2023-04-07 11:08:05.000000 localstack-2.0.1/localstack.egg-info/top_level.txt
-drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-04-07 11:08:05.400985 localstack-2.0.1/localstack_cli/
--rw-rw-r--   0 runner    (1000) runner    (1001)       50 2023-04-07 11:08:04.000000 localstack-2.0.1/localstack_cli/__init__.py
--rw-rw-r--   0 runner    (1000) runner    (1001)       38 2023-04-07 11:08:05.400985 localstack-2.0.1/setup.cfg
--rw-rw-r--   0 runner    (1000) runner    (1001)     1553 2023-04-07 11:04:50.000000 localstack-2.0.1/setup.py
+drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-03-31 11:10:55.938574 localstack-2.0.1.dev20230331110744/
+-rw-rw-r--   0 runner    (1000) runner    (1001)    11439 2023-03-31 11:10:55.938574 localstack-2.0.1.dev20230331110744/PKG-INFO
+drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-03-31 11:10:55.938574 localstack-2.0.1.dev20230331110744/localstack.egg-info/
+-rw-rw-r--   0 runner    (1000) runner    (1001)    11439 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack.egg-info/PKG-INFO
+-rw-rw-r--   0 runner    (1000) runner    (1001)      204 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack.egg-info/SOURCES.txt
+-rw-rw-r--   0 runner    (1000) runner    (1001)        1 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack.egg-info/dependency_links.txt
+-rw-rw-r--   0 runner    (1000) runner    (1001)      223 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack.egg-info/requires.txt
+-rw-rw-r--   0 runner    (1000) runner    (1001)       15 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack.egg-info/top_level.txt
+drwxrwxr-x   0 runner    (1000) runner    (1001)        0 2023-03-31 11:10:55.938574 localstack-2.0.1.dev20230331110744/localstack_cli/
+-rw-rw-r--   0 runner    (1000) runner    (1001)       68 2023-03-31 11:10:55.000000 localstack-2.0.1.dev20230331110744/localstack_cli/__init__.py
+-rw-rw-r--   0 runner    (1000) runner    (1001)       38 2023-03-31 11:10:55.938574 localstack-2.0.1.dev20230331110744/setup.cfg
+-rw-rw-r--   0 runner    (1000) runner    (1001)     1553 2023-03-31 11:07:34.000000 localstack-2.0.1.dev20230331110744/setup.py
```

### Comparing `localstack-2.0.1/PKG-INFO` & `localstack-2.0.1.dev20230331110744/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: localstack
-Version: 2.0.1
+Version: 2.0.1.dev20230331110744
 Summary: LocalStack - A fully functional local Cloud stack
 Home-page: https://github.com/localstack/localstack
 Author: LocalStack Contributors
 Author-email: info@localstack.cloud
 License: Apache License 2.0
 Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: Apache Software License
@@ -47,15 +47,15 @@
   <a href="#running">Run</a> •
   <a href="#usage">Usage</a> •
   <a href="#releases">Releases</a> •
   <a href="#contributing">Contributing</a>
   <br/>
   <a href="https://docs.localstack.cloud" target="_blank">📖 Docs</a> •
   <a href="https://app.localstack.cloud" target="_blank">💻 Pro version</a> •
-  <a href="https://docs.localstack.cloud/references/coverage/" target="_blank">☑️ LocalStack coverage</a>
+  <a href="https://docs.localstack.cloud/user-guide/aws/feature-coverage/" target="_blank">☑️ Feature coverage</a>
 </p>
 
 ---
 
 # Overview
 
 [LocalStack](https://localstack.cloud) is a cloud service emulator that runs in a single container on your laptop or in your CI environment. With LocalStack, you can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider! Whether you are testing complex CDK applications or Terraform configurations, or just beginning to learn about AWS services, LocalStack helps speed up and simplify your testing and development workflow.
@@ -122,15 +122,15 @@
 ```shell
 % awslocal sqs create-queue --queue-name sample-queue
 {
     "QueueUrl": "http://localhost:4566/000000000000/sample-queue"
 }
 ```
 
-Learn more about [LocalStack AWS services](https://docs.localstack.cloud/references/coverage/) and using them with LocalStack's `awslocal` CLI.
+Learn more about [LocalStack AWS services](https://docs.localstack.cloud/user-guide/aws/feature-coverage/) and using them with LocalStack's `awslocal` CLI.
 
 ## Running
 
 You can run LocalStack through the following options:
 
 - [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
 - [Docker](https://docs.localstack.cloud/getting-started/installation/#docker)
```

#### html2text {}

```diff
@@ -1,26 +1,26 @@
-Metadata-Version: 2.1 Name: localstack Version: 2.0.1 Summary: LocalStack - A
-fully functional local Cloud stack Home-page: https://github.com/localstack/
-localstack Author: LocalStack Contributors Author-email: info@localstack.cloud
-License: Apache License 2.0 Classifier: Programming Language :: Python :: 3.10
-Classifier: License :: OSI Approved :: Apache Software License Classifier:
-Topic :: Internet Classifier: Topic :: Software Development :: Testing
-Classifier: Topic :: System :: Emulators Description-Content-Type: text/
-markdown Provides-Extra: runtime Provides-Extra: full
+Metadata-Version: 2.1 Name: localstack Version: 2.0.1.dev20230331110744
+Summary: LocalStack - A fully functional local Cloud stack Home-page: https://
+github.com/localstack/localstack Author: LocalStack Contributors Author-email:
+info@localstack.cloud License: Apache License 2.0 Classifier: Programming
+Language :: Python :: 3.10 Classifier: License :: OSI Approved :: Apache
+Software License Classifier: Topic :: Internet Classifier: Topic :: Software
+Development :: Testing Classifier: Topic :: System :: Emulators Description-
+Content-Type: text/markdown Provides-Extra: runtime Provides-Extra: full
   :zap: We are thrilled to announce LocalStack_2.0 which brings new features,
                         enhancements and bugfixes :zap:
               [LocalStack - A fully functional local cloud stack]
  [CircleCI] [Coverage_Status] [PyPI_Version] [Docker_Pulls] [PyPi_downloads]
 [Backers_on_Open_Collective] [Sponsors_on_Open_Collective] [PyPI_License] [Code
                             style:_black] [Twitter]
 LocalStack provides an easy-to-use test/mocking framework for developing cloud
                                  applications.
       Overview â¢ Install â¢ Example â¢ Run â¢ Usage â¢ Releases â¢
                                  Contributing
-         ð_Docs â¢ ð»_Pro_version â¢ âï¸_LocalStack_coverage
+          ð_Docs â¢ ð»_Pro_version â¢ âï¸_Feature_coverage
 --- # Overview [LocalStack](https://localstack.cloud) is a cloud service
 emulator that runs in a single container on your laptop or in your CI
 environment. With LocalStack, you can run your AWS applications or Lambdas
 entirely on your local machine without connecting to a remote cloud provider!
 Whether you are testing complex CDK applications or Terraform configurations,
 or just beginning to learn about AWS services, LocalStack helps speed up and
 simplify your testing and development workflow. LocalStack supports a growing
@@ -51,17 +51,17 @@
 â¡âââââââââââââââââââââââââââââââââââââââââ©
 â acm â â available â â apigateway â â available â â
 cloudformation â â available â â cloudwatch â â available â â
 config â â available â â dynamodb â â available â ... ``` To use
 SQS, a fully managed distributed message queuing service, on LocalStack, run:
 ```shell % awslocal sqs create-queue --queue-name sample-queue { "QueueUrl":
 "http://localhost:4566/000000000000/sample-queue" } ``` Learn more about
-[LocalStack AWS services](https://docs.localstack.cloud/references/coverage/
-) and using them with LocalStack's `awslocal` CLI. ## Running You can run
-LocalStack through the following options: - [LocalStack CLI](https://
+[LocalStack AWS services](https://docs.localstack.cloud/user-guide/aws/feature-
+coverage/) and using them with LocalStack's `awslocal` CLI. ## Running You can
+run LocalStack through the following options: - [LocalStack CLI](https://
 docs.localstack.cloud/getting-started/installation/#localstack-cli) - [Docker]
 (https://docs.localstack.cloud/getting-started/installation/#docker) - [Docker
 Compose](https://docs.localstack.cloud/getting-started/installation/#docker-
 compose) - [Helm](https://docs.localstack.cloud/getting-started/installation/
 #helm) ## Usage To start using LocalStack, check out our documentation at
 docs.localstack.cloud>. - [LocalStack Configuration](https://
 docs.localstack.cloud/references/configuration/) - [LocalStack in CI](https://
```

### Comparing `localstack-2.0.1/localstack.egg-info/PKG-INFO` & `localstack-2.0.1.dev20230331110744/localstack.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: localstack
-Version: 2.0.1
+Version: 2.0.1.dev20230331110744
 Summary: LocalStack - A fully functional local Cloud stack
 Home-page: https://github.com/localstack/localstack
 Author: LocalStack Contributors
 Author-email: info@localstack.cloud
 License: Apache License 2.0
 Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: Apache Software License
@@ -47,15 +47,15 @@
   <a href="#running">Run</a> •
   <a href="#usage">Usage</a> •
   <a href="#releases">Releases</a> •
   <a href="#contributing">Contributing</a>
   <br/>
   <a href="https://docs.localstack.cloud" target="_blank">📖 Docs</a> •
   <a href="https://app.localstack.cloud" target="_blank">💻 Pro version</a> •
-  <a href="https://docs.localstack.cloud/references/coverage/" target="_blank">☑️ LocalStack coverage</a>
+  <a href="https://docs.localstack.cloud/user-guide/aws/feature-coverage/" target="_blank">☑️ Feature coverage</a>
 </p>
 
 ---
 
 # Overview
 
 [LocalStack](https://localstack.cloud) is a cloud service emulator that runs in a single container on your laptop or in your CI environment. With LocalStack, you can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider! Whether you are testing complex CDK applications or Terraform configurations, or just beginning to learn about AWS services, LocalStack helps speed up and simplify your testing and development workflow.
@@ -122,15 +122,15 @@
 ```shell
 % awslocal sqs create-queue --queue-name sample-queue
 {
     "QueueUrl": "http://localhost:4566/000000000000/sample-queue"
 }
 ```
 
-Learn more about [LocalStack AWS services](https://docs.localstack.cloud/references/coverage/) and using them with LocalStack's `awslocal` CLI.
+Learn more about [LocalStack AWS services](https://docs.localstack.cloud/user-guide/aws/feature-coverage/) and using them with LocalStack's `awslocal` CLI.
 
 ## Running
 
 You can run LocalStack through the following options:
 
 - [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
 - [Docker](https://docs.localstack.cloud/getting-started/installation/#docker)
```

#### html2text {}

```diff
@@ -1,26 +1,26 @@
-Metadata-Version: 2.1 Name: localstack Version: 2.0.1 Summary: LocalStack - A
-fully functional local Cloud stack Home-page: https://github.com/localstack/
-localstack Author: LocalStack Contributors Author-email: info@localstack.cloud
-License: Apache License 2.0 Classifier: Programming Language :: Python :: 3.10
-Classifier: License :: OSI Approved :: Apache Software License Classifier:
-Topic :: Internet Classifier: Topic :: Software Development :: Testing
-Classifier: Topic :: System :: Emulators Description-Content-Type: text/
-markdown Provides-Extra: runtime Provides-Extra: full
+Metadata-Version: 2.1 Name: localstack Version: 2.0.1.dev20230331110744
+Summary: LocalStack - A fully functional local Cloud stack Home-page: https://
+github.com/localstack/localstack Author: LocalStack Contributors Author-email:
+info@localstack.cloud License: Apache License 2.0 Classifier: Programming
+Language :: Python :: 3.10 Classifier: License :: OSI Approved :: Apache
+Software License Classifier: Topic :: Internet Classifier: Topic :: Software
+Development :: Testing Classifier: Topic :: System :: Emulators Description-
+Content-Type: text/markdown Provides-Extra: runtime Provides-Extra: full
   :zap: We are thrilled to announce LocalStack_2.0 which brings new features,
                         enhancements and bugfixes :zap:
               [LocalStack - A fully functional local cloud stack]
  [CircleCI] [Coverage_Status] [PyPI_Version] [Docker_Pulls] [PyPi_downloads]
 [Backers_on_Open_Collective] [Sponsors_on_Open_Collective] [PyPI_License] [Code
                             style:_black] [Twitter]
 LocalStack provides an easy-to-use test/mocking framework for developing cloud
                                  applications.
       Overview â¢ Install â¢ Example â¢ Run â¢ Usage â¢ Releases â¢
                                  Contributing
-         ð_Docs â¢ ð»_Pro_version â¢ âï¸_LocalStack_coverage
+          ð_Docs â¢ ð»_Pro_version â¢ âï¸_Feature_coverage
 --- # Overview [LocalStack](https://localstack.cloud) is a cloud service
 emulator that runs in a single container on your laptop or in your CI
 environment. With LocalStack, you can run your AWS applications or Lambdas
 entirely on your local machine without connecting to a remote cloud provider!
 Whether you are testing complex CDK applications or Terraform configurations,
 or just beginning to learn about AWS services, LocalStack helps speed up and
 simplify your testing and development workflow. LocalStack supports a growing
@@ -51,17 +51,17 @@
 â¡âââââââââââââââââââââââââââââââââââââââââ©
 â acm â â available â â apigateway â â available â â
 cloudformation â â available â â cloudwatch â â available â â
 config â â available â â dynamodb â â available â ... ``` To use
 SQS, a fully managed distributed message queuing service, on LocalStack, run:
 ```shell % awslocal sqs create-queue --queue-name sample-queue { "QueueUrl":
 "http://localhost:4566/000000000000/sample-queue" } ``` Learn more about
-[LocalStack AWS services](https://docs.localstack.cloud/references/coverage/
-) and using them with LocalStack's `awslocal` CLI. ## Running You can run
-LocalStack through the following options: - [LocalStack CLI](https://
+[LocalStack AWS services](https://docs.localstack.cloud/user-guide/aws/feature-
+coverage/) and using them with LocalStack's `awslocal` CLI. ## Running You can
+run LocalStack through the following options: - [LocalStack CLI](https://
 docs.localstack.cloud/getting-started/installation/#localstack-cli) - [Docker]
 (https://docs.localstack.cloud/getting-started/installation/#docker) - [Docker
 Compose](https://docs.localstack.cloud/getting-started/installation/#docker-
 compose) - [Helm](https://docs.localstack.cloud/getting-started/installation/
 #helm) ## Usage To start using LocalStack, check out our documentation at
 docs.localstack.cloud>. - [LocalStack Configuration](https://
 docs.localstack.cloud/references/configuration/) - [LocalStack in CI](https://
```

### Comparing `localstack-2.0.1/setup.py` & `localstack-2.0.1.dev20230331110744/setup.py`

 * *Files identical despite different names*

