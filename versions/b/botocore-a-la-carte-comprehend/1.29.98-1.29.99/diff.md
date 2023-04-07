# Comparing `tmp/botocore-a-la-carte-comprehend-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-comprehend-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-comprehend-1.29.98.tar", last modified: Fri Mar 24 01:24:08 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-comprehend-1.29.99.tar", last modified: Sat Mar 25 01:22:27 2023, max compression
```

## Comparing `botocore-a-la-carte-comprehend-1.29.98.tar` & `botocore-a-la-carte-comprehend-1.29.99.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/
--rw-r--r--   0 runner    (1001) docker     (123)    17640 2023-03-24 01:23:57.000000 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-24 01:23:57.000000 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-03-24 01:23:57.000000 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   360614 2023-03-24 01:23:57.000000 botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/service-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      454 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:08.693842 botocore-a-la-carte-comprehend-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-03-24 01:24:08.000000 botocore-a-la-carte-comprehend-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.150591 botocore-a-la-carte-comprehend-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:22:26.000000 botocore-a-la-carte-comprehend-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-25 01:22:27.150591 botocore-a-la-carte-comprehend-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.146591 botocore-a-la-carte-comprehend-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.146591 botocore-a-la-carte-comprehend-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.146591 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.146591 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/
+-rw-r--r--   0 runner    (1001) docker     (123)    17640 2023-03-25 01:22:12.000000 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-25 01:22:12.000000 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-03-25 01:22:12.000000 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   360107 2023-03-25 01:22:12.000000 botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/service-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:27.146591 botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-25 01:22:27.000000 botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      454 2023-03-25 01:22:27.000000 botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:22:27.000000 botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:22:27.000000 botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:22:27.150591 botocore-a-la-carte-comprehend-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-03-25 01:22:26.000000 botocore-a-la-carte-comprehend-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-comprehend-1.29.98/LICENSE.txt` & `botocore-a-la-carte-comprehend-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-comprehend-1.29.98/PKG-INFO` & `botocore-a-la-carte-comprehend-1.29.99/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-comprehend
-Version: 1.29.98
+Version: 1.29.99
 Summary: comprehend data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/endpoint-rule-set-1.json` & `botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/paginators-1.json` & `botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-comprehend-1.29.98/botocore/data/comprehend/2017-11-27/service-2.json` & `botocore-a-la-carte-comprehend-1.29.99/botocore/data/comprehend/2017-11-27/service-2.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8997498519609681%*

 * *Differences: {"'documentation'": "'<p>Amazon Comprehend is an Amazon Web Services service for gaining insight "*

 * *                    'into the content of documents. Use these actions to determine the topics '*

 * *                    'contained in your documents, the topics they discuss, the predominant '*

 * *                    "sentiment expressed in them, the predominant language used, and more.</p>'",*

 * * "'operations'": "{'CreateFlywheel': {'documentation': '<p>A flywheel is an Amazon Web Services "*

 * *                 'resource t […]*

```diff
@@ -1,9 +1,9 @@
 {
-    "documentation": "<p>Amazon Comprehend is an AWS service for gaining insight into the content of documents. Use these actions to determine the topics contained in your documents, the topics they discuss, the predominant sentiment expressed in them, the predominant language used, and more.</p>",
+    "documentation": "<p>Amazon Comprehend is an Amazon Web Services service for gaining insight into the content of documents. Use these actions to determine the topics contained in your documents, the topics they discuss, the predominant sentiment expressed in them, the predominant language used, and more.</p>",
     "metadata": {
         "apiVersion": "2017-11-27",
         "endpointPrefix": "comprehend",
         "jsonVersion": "1.1",
         "protocol": "json",
         "serviceFullName": "Amazon Comprehend",
         "serviceId": "Comprehend",
@@ -406,15 +406,15 @@
             },
             "name": "CreateEntityRecognizer",
             "output": {
                 "shape": "CreateEntityRecognizerResponse"
             }
         },
         "CreateFlywheel": {
-            "documentation": "<p>A flywheel is an AWS resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.</p> <p>When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.</p> <p>To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.</p> <p>To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.</p> <p>For more information about flywheels, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html\"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>",
+            "documentation": "<p>A flywheel is an Amazon Web Services resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.</p> <p>When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.</p> <p>To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.</p> <p>To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.</p> <p>For more information about flywheels, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html\"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>",
             "errors": [
                 {
                     "shape": "InvalidRequestException"
                 },
                 {
                     "shape": "ResourceInUseException"
                 },
@@ -1251,15 +1251,15 @@
             },
             "name": "DetectTargetedSentiment",
             "output": {
                 "shape": "DetectTargetedSentimentResponse"
             }
         },
         "ImportModel": {
-            "documentation": "<p>Creates a new custom model that replicates a source custom model that you import. The source model can be in your AWS account or another one.</p> <p>If the source model is in another AWS account, then it must have a resource-based policy that authorizes you to import it.</p> <p>The source model must be in the same AWS region that you're using when you import. You can't import a model that's in a different region.</p>",
+            "documentation": "<p>Creates a new custom model that replicates a source custom model that you import. The source model can be in your Amazon Web Services account or another one.</p> <p>If the source model is in another Amazon Web Services account, then it must have a resource-based policy that authorizes you to import it.</p> <p>The source model must be in the same Amazon Web Services Region that you're using when you import. You can't import a model that's in a different Region.</p>",
             "errors": [
                 {
                     "shape": "InvalidRequestException"
                 },
                 {
                     "shape": "ResourceNotFoundException"
                 },
@@ -1294,15 +1294,15 @@
             },
             "name": "ImportModel",
             "output": {
                 "shape": "ImportModelResponse"
             }
         },
         "ListDatasets": {
-            "documentation": "<p>List the datasets that you have configured in this region. For more information about datasets, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html\"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>",
+            "documentation": "<p>List the datasets that you have configured in this Region. For more information about datasets, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html\"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>",
             "errors": [
                 {
                     "shape": "InvalidRequestException"
                 },
                 {
                     "shape": "TooManyRequestsException"
                 },
@@ -1792,15 +1792,15 @@
             },
             "name": "ListTopicsDetectionJobs",
             "output": {
                 "shape": "ListTopicsDetectionJobsResponse"
             }
         },
         "PutResourcePolicy": {
-            "documentation": "<p>Attaches a resource-based policy to a custom model. You can use this policy to authorize an entity in another AWS account to import the custom model, which replicates it in Amazon Comprehend in their account.</p>",
+            "documentation": "<p>Attaches a resource-based policy to a custom model. You can use this policy to authorize an entity in another Amazon Web Services account to import the custom model, which replicates it in Amazon Comprehend in their account.</p>",
             "errors": [
                 {
                     "shape": "InvalidRequestException"
                 },
                 {
                     "shape": "ResourceNotFoundException"
                 },
@@ -2724,15 +2724,15 @@
         "BatchDetectSentimentRequest": {
             "members": {
                 "LanguageCode": {
                     "documentation": "<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>",
                     "shape": "LanguageCode"
                 },
                 "TextList": {
-                    "documentation": "<p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB. </p> <note> <p>Amazon Comprehend performs real-time sentiment analysis on the first 500 characters of the input text and ignores any additional text in the input.</p> </note>",
+                    "documentation": "<p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB. </p>",
                     "shape": "CustomerInputStringList"
                 }
             },
             "required": [
                 "TextList",
                 "LanguageCode"
             ],
@@ -3227,15 +3227,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DocumentClassifierName": {
                     "documentation": "<p>The name of the document classifier.</p>",
                     "shape": "ComprehendArnName"
                 },
                 "InputDataConfig": {
@@ -3247,35 +3247,35 @@
                     "shape": "LanguageCode"
                 },
                 "Mode": {
                     "documentation": "<p>Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class mode, which identifies one and only one class for each document, or multi-label mode, which identifies one or more labels for each document. In multi-label mode, multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).</p>",
                     "shape": "DocumentClassifierMode"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "ModelPolicy": {
-                    "documentation": "<p>The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another AWS account to import your custom model.</p> <p>Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\\"attribute\\\": \\\"value\\\", \\\"attribute\\\": [\\\"value\\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>",
+                    "documentation": "<p>The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\\"attribute\\\": \\\"value\\\", \\\"attribute\\\": [\\\"value\\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>",
                     "shape": "Policy"
                 },
                 "OutputDataConfig": {
                     "documentation": "<p>Enables the addition of output results configuration parameters for custom classifier jobs.</p>",
                     "shape": "DocumentClassifierOutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department. </p>",
                     "shape": "TagList"
                 },
                 "VersionName": {
-                    "documentation": "<p>The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the account/AWS Region.</p>",
+                    "documentation": "<p>The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the Amazon Web Services account/Amazon Web Services Region.</p>",
                     "shape": "VersionName"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -3300,15 +3300,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>An idempotency token provided by the customer. If this token matches a previous endpoint creation request, Amazon Comprehend will not return a <code>ResourceInUseException</code>. </p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>",
                     "shape": "IamRoleArn"
                 },
                 "DesiredInferenceUnits": {
                     "documentation": "<p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>",
                     "shape": "InferenceUnitsInteger"
                 },
                 "EndpointName": {
@@ -3351,47 +3351,47 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p> A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
-                    "documentation": "<p>Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same region as the entity recognizer being created. </p>",
+                    "documentation": "<p>Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same Region as the entity recognizer being created. </p>",
                     "shape": "EntityRecognizerInputDataConfig"
                 },
                 "LanguageCode": {
                     "documentation": "<p> You can specify any of the following languages: English (\"en\"), Spanish (\"es\"), French (\"fr\"), Italian (\"it\"), German (\"de\"), or Portuguese (\"pt\"). If you plan to use this entity recognizer with PDF, Word, or image input files, you must specify English as the language. All training documents must be in the same language.</p>",
                     "shape": "LanguageCode"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "ModelPolicy": {
-                    "documentation": "<p>The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another AWS account to import your custom model.</p> <p>Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\\"attribute\\\": \\\"value\\\", \\\"attribute\\\": [\\\"value\\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>",
+                    "documentation": "<p>The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>\"{\\\"attribute\\\": \\\"value\\\", \\\"attribute\\\": [\\\"value\\\"]}\"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{\"attribute\": \"value\", \"attribute\": [\"value\"]}'</code> </p>",
                     "shape": "Policy"
                 },
                 "RecognizerName": {
-                    "documentation": "<p>The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/region.</p>",
+                    "documentation": "<p>The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/Region.</p>",
                     "shape": "ComprehendArnName"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the entity recognizer. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department. </p>",
                     "shape": "TagList"
                 },
                 "VersionName": {
-                    "documentation": "<p>The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/ AWS Region.</p>",
+                    "documentation": "<p>The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/Region.</p>",
                     "shape": "VersionName"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -3420,15 +3420,15 @@
                 },
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DataLakeS3Uri": {
                     "documentation": "<p>Enter the S3 location for the data lake. You can specify a new S3 bucket or a new folder of an existing S3 bucket. The flywheel creates the data lake at this location.</p>",
                     "shape": "FlywheelS3Uri"
                 },
                 "DataSecurityConfig": {
@@ -3489,15 +3489,15 @@
             "documentation": "<p>Data security configuration.</p>",
             "members": {
                 "DataLakeKmsKeyId": {
                     "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt the data in the data lake.</p>",
                     "shape": "KmsKeyId"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VolumeKmsKeyId": {
                     "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt the volume.</p>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
@@ -3553,28 +3553,28 @@
             "documentation": "<p>Describes the dataset input data configuration for a document classifier model.</p> <p>For more information on how the input file is formatted, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html\">Preparing training data</a> in the Comprehend Developer Guide. </p>",
             "members": {
                 "LabelDelimiter": {
                     "documentation": "<p>Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.</p>",
                     "shape": "LabelDelimiter"
                 },
                 "S3Uri": {
-                    "documentation": "<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>",
+                    "documentation": "<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
         },
         "DatasetEntityRecognizerAnnotations": {
             "documentation": "<p>Describes the annotations associated with a entity recognizer.</p>",
             "members": {
                 "S3Uri": {
-                    "documentation": "<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -4193,15 +4193,15 @@
                 "Text"
             ],
             "type": "structure"
         },
         "DetectDominantLanguageResponse": {
             "members": {
                 "Languages": {
-                    "documentation": "<p>The languages that Amazon Comprehend detected in the input text. For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see <a href=\"https://tools.ietf.org/html/rfc5646\">Tags for Identifying Languages</a> on the <i>IETF Tools</i> web site.</p>",
+                    "documentation": "<p>Array of languages that Amazon Comprehend detected in the input text. The array is sorted in descending order of the score (the dominant language is always the first element in the array).</p> <p>For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see <a href=\"https://tools.ietf.org/html/rfc5646\">Tags for Identifying Languages</a> on the <i>IETF Tools</i> web site.</p>",
                     "shape": "ListOfDominantLanguages"
                 }
             },
             "sensitive": true,
             "type": "structure"
         },
         "DetectEntitiesRequest": {
@@ -4311,15 +4311,15 @@
         "DetectSentimentRequest": {
             "members": {
                 "LanguageCode": {
                     "documentation": "<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>",
                     "shape": "LanguageCode"
                 },
                 "Text": {
-                    "documentation": "<p>A UTF-8 text string. The maximum string size is 5 KB.</p> <note> <p>Amazon Comprehend performs real-time sentiment analysis on the first 500 characters of the input text and ignores any additional text in the input.</p> </note>",
+                    "documentation": "<p>A UTF-8 text string. The maximum string size is 5 KB.</p>",
                     "shape": "CustomerInputString"
                 }
             },
             "required": [
                 "Text",
                 "LanguageCode"
             ],
@@ -4450,15 +4450,15 @@
             },
             "type": "structure"
         },
         "DocumentClassificationJobProperties": {
             "documentation": "<p>Provides information about a document classification job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DocumentClassifierArn": {
                     "documentation": "<p>The Amazon Resource Name (ARN) that identifies the document classifier. </p>",
                     "shape": "DocumentClassifierArn"
                 },
                 "EndTime": {
@@ -4470,15 +4470,15 @@
                     "shape": "ComprehendFlywheelArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the document classification job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the document classification job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:document-classification-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the document classification job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:document-classification-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the document classification job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -4498,15 +4498,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the document classification job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your document classification job. For more information, see <a href=\"https://docs.aws.amazon.com/vppc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -4575,19 +4575,19 @@
                     "shape": "DocumentClassifierDataFormat"
                 },
                 "LabelDelimiter": {
                     "documentation": "<p>Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.</p>",
                     "shape": "LabelDelimiter"
                 },
                 "S3Uri": {
-                    "documentation": "<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>",
+                    "documentation": "<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>",
                     "shape": "S3Uri"
                 },
                 "TestS3Uri": {
-                    "documentation": "<p>This specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same AWS Region as the API endpoint that you are calling. </p>",
+                    "documentation": "<p>This specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same Amazon Web Services Region as the API endpoint that you are calling. </p>",
                     "shape": "S3Uri"
                 }
             },
             "type": "structure"
         },
         "DocumentClassifierMode": {
             "enum": [
@@ -4600,33 +4600,33 @@
             "documentation": "<p>Provides output results configuration parameters for custom classifier jobs. </p>",
             "members": {
                 "FlywheelStatsS3Prefix": {
                     "documentation": "<p>The Amazon S3 prefix for the data lake location of the flywheel statistics.</p>",
                     "shape": "S3Uri"
                 },
                 "KmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>KMS Key Alias: <code>\"alias/ExampleAlias\"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>KMS Key Alias: <code>\"alias/ExampleAlias\"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "S3Uri": {
-                    "documentation": "<p>When you use the <code>OutputDataConfig</code> object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.</p> <p>When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the confusion matrix.</p>",
+                    "documentation": "<p>When you use the <code>OutputDataConfig</code> object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.</p> <p>When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the confusion matrix.</p>",
                     "shape": "S3Uri"
                 }
             },
             "type": "structure"
         },
         "DocumentClassifierProperties": {
             "documentation": "<p>Provides information about a document classifier.</p>",
             "members": {
                 "ClassifierMetadata": {
                     "documentation": "<p>Information about the document classifier, including the number of documents used for training the classifier, the number of documents used for test the classifier, and an accuracy rating.</p>",
                     "shape": "ClassifierMetadata"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DocumentClassifierArn": {
                     "documentation": "<p>The Amazon Resource Name (ARN) that identifies the document classifier.</p>",
                     "shape": "DocumentClassifierArn"
                 },
                 "EndTime": {
@@ -4650,23 +4650,23 @@
                     "shape": "AnyLengthString"
                 },
                 "Mode": {
                     "documentation": "<p>Indicates the mode in which the specific classifier was trained. This also indicates the format of input documents and the format of the confusion matrix. Each classifier can only be trained in one mode and this cannot be changed once the classifier is trained.</p>",
                     "shape": "DocumentClassifierMode"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "OutputDataConfig": {
                     "documentation": "<p> Provides output results configuration parameters for custom classifier jobs.</p>",
                     "shape": "DocumentClassifierOutputDataConfig"
                 },
                 "SourceModelArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different AWS account to create the document classifier model in your AWS account.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different Amazon Web Services account to create the document classifier model in your Amazon Web Services account.</p>",
                     "shape": "DocumentClassifierArn"
                 },
                 "Status": {
                     "documentation": "<p>The status of the document classifier. If the status is <code>TRAINED</code> the classifier is ready to use. If the status is <code>FAILED</code> you can see additional information about why the classifier wasn't trained in the <code>Message</code> field.</p>",
                     "shape": "ModelStatus"
                 },
                 "SubmitTime": {
@@ -4682,15 +4682,15 @@
                     "shape": "Timestamp"
                 },
                 "VersionName": {
                     "documentation": "<p>The version name that you assigned to the document classifier.</p>",
                     "shape": "VersionName"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see <a href=\"https://docs.aws.amazon.com/vppc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -4871,27 +4871,27 @@
             },
             "type": "structure"
         },
         "DominantLanguageDetectionJobProperties": {
             "documentation": "<p>Provides information about a dominant language detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the dominant language detection job completed.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the dominant language detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the dominant language detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:dominant-language-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the dominant language detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:dominant-language-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the dominant language detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -4911,15 +4911,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the dominant language detection job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your dominant language detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -4964,15 +4964,15 @@
                     "shape": "Timestamp"
                 },
                 "CurrentInferenceUnits": {
                     "documentation": "<p>The number of inference units currently used by the model using this endpoint.</p>",
                     "shape": "InferenceUnitsInteger"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>",
                     "shape": "IamRoleArn"
                 },
                 "DesiredDataAccessRoleArn": {
                     "documentation": "<p>Data access role ARN to use in case the new model is encrypted with a customer KMS key.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DesiredInferenceUnits": {
@@ -5048,31 +5048,35 @@
             },
             "type": "structure"
         },
         "EntitiesDetectionJobProperties": {
             "documentation": "<p>Provides information about an entities detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the entities detection job completed</p>",
                     "shape": "Timestamp"
                 },
                 "EntityRecognizerArn": {
                     "documentation": "<p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>",
                     "shape": "EntityRecognizerArn"
                 },
+                "FlywheelArn": {
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the flywheel associated with this job.</p>",
+                    "shape": "ComprehendFlywheelArn"
+                },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the entities detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the entities detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the entities detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -5096,15 +5100,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the entities detection job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your entity detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -5173,19 +5177,19 @@
             ],
             "type": "structure"
         },
         "EntityRecognizerAnnotations": {
             "documentation": "<p>Describes the annotations associated with a entity recognizer.</p>",
             "members": {
                 "S3Uri": {
-                    "documentation": "<p> Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p> Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 },
                 "TestS3Uri": {
-                    "documentation": "<p> Specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p> Specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -5212,19 +5216,19 @@
             "documentation": "<p>Describes the training documents submitted with an entity recognizer.</p>",
             "members": {
                 "InputFormat": {
                     "documentation": "<p> Specifies how the text in an input file should be processed. This is optional, and the default is ONE_DOC_PER_LINE. ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.</p>",
                     "shape": "InputFormat"
                 },
                 "S3Uri": {
-                    "documentation": "<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 },
                 "TestS3Uri": {
-                    "documentation": "<p> Specifies the Amazon S3 location where the test documents for an entity recognizer are located. The URI must be in the same AWS Region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p> Specifies the Amazon S3 location where the test documents for an entity recognizer are located. The URI must be in the same Amazon Web Services Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -5234,15 +5238,15 @@
             "pattern": "arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer-endpoint/[a-zA-Z0-9](-*[a-zA-Z0-9])*",
             "type": "string"
         },
         "EntityRecognizerEntityList": {
             "documentation": "<p>Describes the entity list submitted with an entity recognizer.</p>",
             "members": {
                 "S3Uri": {
-                    "documentation": "<p>Specifies the Amazon S3 location where the entity list is located. The URI must be in the same region as the API endpoint that you are calling.</p>",
+                    "documentation": "<p>Specifies the Amazon S3 location where the entity list is located. The URI must be in the same Region as the API endpoint that you are calling.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -5377,15 +5381,15 @@
             },
             "type": "structure"
         },
         "EntityRecognizerProperties": {
             "documentation": "<p>Describes information about an entity recognizer.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p> The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p> The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the recognizer creation completed.</p>",
                     "shape": "Timestamp"
                 },
                 "EntityRecognizerArn": {
@@ -5405,27 +5409,27 @@
                     "shape": "LanguageCode"
                 },
                 "Message": {
                     "documentation": "<p> A description of the status of the recognizer.</p>",
                     "shape": "AnyLengthString"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "OutputDataConfig": {
                     "documentation": "<p>Output data configuration.</p>",
                     "shape": "EntityRecognizerOutputDataConfig"
                 },
                 "RecognizerMetadata": {
                     "documentation": "<p> Provides information about an entity recognizer.</p>",
                     "shape": "EntityRecognizerMetadata"
                 },
                 "SourceModelArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different AWS account to create the entity recognizer model in your AWS account.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different Amazon Web Services account to create the entity recognizer model in your Amazon Web Services account.</p>",
                     "shape": "EntityRecognizerArn"
                 },
                 "Status": {
                     "documentation": "<p>Provides the status of the entity recognizer.</p>",
                     "shape": "ModelStatus"
                 },
                 "SubmitTime": {
@@ -5441,15 +5445,15 @@
                     "shape": "Timestamp"
                 },
                 "VersionName": {
                     "documentation": "<p>The version name you assigned to the entity recognizer.</p>",
                     "shape": "VersionName"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -5595,27 +5599,27 @@
             },
             "type": "structure"
         },
         "EventsDetectionJobProperties": {
             "documentation": "<p>Provides information about an events detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the events detection job completed.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the events detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the events detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:events-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:events-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the events detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:events-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:events-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the events detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -5805,15 +5809,15 @@
                     "shape": "ComprehendModelArn"
                 },
                 "CreationTime": {
                     "documentation": "<p>Creation time of the flywheel.</p>",
                     "shape": "Timestamp"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend permission to access the flywheel data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DataLakeS3Uri": {
                     "documentation": "<p>Amazon S3 URI of the data lake location. </p>",
                     "shape": "S3Uri"
                 },
                 "DataSecurityConfig": {
@@ -5933,19 +5937,19 @@
             "min": 20,
             "pattern": "arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+",
             "type": "string"
         },
         "ImportModelRequest": {
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend permission to use Amazon Key Management Service (KMS) to encrypt or decrypt the custom model.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to use Amazon Key Management Service (KMS) to encrypt or decrypt the custom model.</p>",
                     "shape": "IamRoleArn"
                 },
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "ModelName": {
                     "documentation": "<p>The name to assign to the custom model that is created in Amazon Comprehend by this import.</p>",
                     "shape": "ComprehendArnName"
                 },
                 "SourceModelArn": {
@@ -5953,15 +5957,15 @@
                     "shape": "ComprehendModelArn"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the custom model that is created by this import. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VersionName": {
-                    "documentation": "<p>The version name given to the custom model that is created by this import. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the account/AWS Region.</p>",
+                    "documentation": "<p>The version name given to the custom model that is created by this import. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the account/Region.</p>",
                     "shape": "VersionName"
                 }
             },
             "required": [
                 "SourceModelArn"
             ],
             "type": "structure"
@@ -5987,15 +5991,15 @@
                     "shape": "DocumentReaderConfig"
                 },
                 "InputFormat": {
                     "documentation": "<p>Specifies how the text in an input file should be processed:</p> <ul> <li> <p> <code>ONE_DOC_PER_FILE</code> - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.</p> </li> <li> <p> <code>ONE_DOC_PER_LINE</code> - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.</p> </li> </ul>",
                     "shape": "InputFormat"
                 },
                 "S3Uri": {
-                    "documentation": "<p>The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. </p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p>",
+                    "documentation": "<p>The Amazon S3 URI for the input data. The URI must be in same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. </p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -6149,27 +6153,27 @@
             },
             "type": "structure"
         },
         "KeyPhrasesDetectionJobProperties": {
             "documentation": "<p>Provides information about a key phrases detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the key phrases detection job completed.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the key phrases detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the key phrases detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:key-phrases-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the key phrases detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:key-phrases-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the key phrases detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -6193,15 +6197,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the key phrases detection job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your key phrases detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -6987,15 +6991,16 @@
             "enum": [
                 "SUBMITTED",
                 "TRAINING",
                 "DELETING",
                 "STOP_REQUESTED",
                 "STOPPED",
                 "IN_ERROR",
-                "TRAINED"
+                "TRAINED",
+                "TRAINED_WITH_WARNING"
             ],
             "type": "string"
         },
         "ModelType": {
             "enum": [
                 "DOCUMENT_CLASSIFIER",
                 "ENTITY_RECOGNIZER"
@@ -7010,19 +7015,19 @@
             "min": 1,
             "type": "integer"
         },
         "OutputDataConfig": {
             "documentation": "<p>Provides configuration parameters for the output of inference jobs.</p> <p/>",
             "members": {
                 "KmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>KMS Key Alias: <code>\"alias/ExampleAlias\"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>KMS Key Alias: <code>\"alias/ExampleAlias\"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "S3Uri": {
-                    "documentation": "<p>When you use the <code>OutputDataConfig</code> object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.</p> <p>When the topic detection job is finished, the service creates an output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the ouput of the operation.</p> <p> For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with <code>.out</code> appended at the end. </p>",
+                    "documentation": "<p>When you use the <code>OutputDataConfig</code> object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.</p> <p>When the topic detection job is finished, the service creates an output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the ouput of the operation.</p> <p> For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with <code>.out</code> appended at the end. </p>",
                     "shape": "S3Uri"
                 }
             },
             "required": [
                 "S3Uri"
             ],
             "type": "structure"
@@ -7096,27 +7101,27 @@
             },
             "type": "structure"
         },
         "PiiEntitiesDetectionJobProperties": {
             "documentation": "<p>Provides information about a PII entities detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the PII entities detection job completed.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input properties for a PII entities detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the PII entities detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:pii-entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the PII entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:pii-entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the PII entities detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -7238,15 +7243,15 @@
             ],
             "type": "string"
         },
         "PiiOutputDataConfig": {
             "documentation": "<p>Provides configuration parameters for the output of PII entity detection jobs.</p>",
             "members": {
                 "KmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job.</p>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job.</p>",
                     "shape": "KmsKeyId"
                 },
                 "S3Uri": {
                     "documentation": "<p>When you use the <code>PiiOutputDataConfig</code> object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. </p> <p> For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with <code>.out</code> appended at the end. </p>",
                     "shape": "S3Uri"
                 }
             },
@@ -7439,27 +7444,27 @@
             },
             "type": "structure"
         },
         "SentimentDetectionJobProperties": {
             "documentation": "<p>Provides information about a sentiment detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the sentiment detection job ended.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration that you supplied when you created the sentiment detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the sentiment detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -7483,15 +7488,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the sentiment detection job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your sentiment detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -7545,15 +7550,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DocumentClassifierArn": {
                     "documentation": "<p>The Amazon Resource Name (ARN) of the document classifier to use to process the job.</p>",
                     "shape": "DocumentClassifierArn"
                 },
                 "FlywheelArn": {
@@ -7573,15 +7578,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the document classification job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your document classification job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -7595,15 +7600,15 @@
         "StartDocumentClassificationJobResponse": {
             "members": {
                 "DocumentClassifierArn": {
                     "documentation": "<p>The ARN of the custom classification model.</p>",
                     "shape": "DocumentClassifierArn"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the document classification job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:document-classification-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the document classification job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:document-classification-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of the job, use this identifier with the <code>DescribeDocumentClassificationJob</code> operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7617,15 +7622,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>Specifies the format and location of the input data for the job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -7637,15 +7642,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the dominant language detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your dominant language detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -7655,15 +7660,15 @@
                 "DataAccessRoleArn"
             ],
             "type": "structure"
         },
         "StartDominantLanguageDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the dominant language detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:dominant-language-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the dominant language detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:dominant-language-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of a job, use this identifier with the operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7677,15 +7682,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EntityRecognizerArn": {
                     "documentation": "<p>The Amazon Resource Name (ARN) that identifies the specific entity recognizer to be used by the <code>StartEntitiesDetectionJob</code>. This ARN is optional and is only used for a custom entity recognition job.</p>",
                     "shape": "EntityRecognizerArn"
                 },
                 "FlywheelArn": {
@@ -7709,15 +7714,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the entities detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your entity detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -7732,15 +7737,15 @@
         "StartEntitiesDetectionJobResponse": {
             "members": {
                 "EntityRecognizerArn": {
                     "documentation": "<p>The ARN of the custom entity recognition model.</p>",
                     "shape": "EntityRecognizerArn"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the entities detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of job, use this identifier with the operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7754,15 +7759,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>An unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>Specifies the format and location of the input data for the job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -7794,15 +7799,15 @@
                 "TargetEventTypes"
             ],
             "type": "structure"
         },
         "StartEventsDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the events detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:events-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:events-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the events detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:events-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:events-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>An unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7845,15 +7850,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>Specifies the format and location of the input data for the job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -7869,15 +7874,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the key phrases detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p> Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your key phrases detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -7888,15 +7893,15 @@
                 "LanguageCode"
             ],
             "type": "structure"
         },
         "StartKeyPhrasesDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the key phrase detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:key-phrases-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the key phrase detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:key-phrases-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of a job, use this identifier with the operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7910,15 +7915,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input properties for a PII entities detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -7954,15 +7959,15 @@
                 "LanguageCode"
             ],
             "type": "structure"
         },
         "StartPiiEntitiesDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the PII entity detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:pii-entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the PII entity detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:pii-entities-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -7976,15 +7981,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>Specifies the format and location of the input data for the job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -8000,15 +8005,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the sentiment detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your sentiment detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -8019,15 +8024,15 @@
                 "LanguageCode"
             ],
             "type": "structure"
         },
         "StartSentimentDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of a job, use this identifier with the operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -8041,15 +8046,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">Role-based permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
                     "documentation": "<p>The identifier of the job.</p>",
@@ -8082,15 +8087,15 @@
                 "LanguageCode"
             ],
             "type": "structure"
         },
         "StartTargetedSentimentDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:targeted-sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:targeted-sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of a job, use this identifier with the <code>DescribeTargetedSentimentDetectionJob</code> operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -8104,15 +8109,15 @@
             "members": {
                 "ClientRequestToken": {
                     "documentation": "<p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>",
                     "idempotencyToken": true,
                     "shape": "ClientRequestTokenString"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions\">https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions</a>.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions\">Role-based permissions</a>.</p>",
                     "shape": "IamRoleArn"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>Specifies the format and location of the input data for the job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobName": {
@@ -8128,15 +8133,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "Tags": {
                     "documentation": "<p>Tags to associate with the topics detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department.</p>",
                     "shape": "TagList"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your topic detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -8146,15 +8151,15 @@
                 "DataAccessRoleArn"
             ],
             "type": "structure"
         },
         "StartTopicsDetectionJobResponse": {
             "members": {
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the topics detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:topics-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the topics detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:topics-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier generated for the job. To get the status of the job, use this identifier with the <code>DescribeTopicDetectionJob</code> operation.</p>",
                     "shape": "JobId"
                 },
                 "JobStatus": {
@@ -8521,26 +8526,26 @@
             },
             "type": "structure"
         },
         "TargetedSentimentDetectionJobProperties": {
             "documentation": "<p>Provides information about a targeted sentiment detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the targeted sentiment detection job ended.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:targeted-sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:targeted-sentiment-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the targeted sentiment detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -8738,27 +8743,27 @@
             },
             "type": "structure"
         },
         "TopicsDetectionJobProperties": {
             "documentation": "<p>Provides information about a topic detection job.</p>",
             "members": {
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your job data. </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your job data. </p>",
                     "shape": "IamRoleArn"
                 },
                 "EndTime": {
                     "documentation": "<p>The time that the topic detection job was completed.</p>",
                     "shape": "Timestamp"
                 },
                 "InputDataConfig": {
                     "documentation": "<p>The input data configuration supplied when you created the topic detection job.</p>",
                     "shape": "InputDataConfig"
                 },
                 "JobArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the topics detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:topics-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the topics detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:&lt;partition&gt;:comprehend:&lt;region&gt;:&lt;account-id&gt;:topics-detection-job/&lt;job-id&gt;</code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>",
                     "shape": "ComprehendArn"
                 },
                 "JobId": {
                     "documentation": "<p>The identifier assigned to the topic detection job.</p>",
                     "shape": "JobId"
                 },
                 "JobName": {
@@ -8782,15 +8787,15 @@
                     "shape": "OutputDataConfig"
                 },
                 "SubmitTime": {
                     "documentation": "<p>The time that the topic detection job was submitted for processing.</p>",
                     "shape": "Timestamp"
                 },
                 "VolumeKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
                     "documentation": "<p>Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your topic detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
                     "shape": "VpcConfig"
                 }
             },
@@ -8833,15 +8838,15 @@
             "members": {},
             "type": "structure"
         },
         "UpdateDataSecurityConfig": {
             "documentation": "<p>Data security configuration.</p>",
             "members": {
                 "ModelKmsKeyId": {
-                    "documentation": "<p>ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
+                    "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>",
                     "shape": "KmsKeyId"
                 },
                 "VolumeKmsKeyId": {
                     "documentation": "<p>ID for the KMS key that Amazon Comprehend uses to encrypt the volume.</p>",
                     "shape": "KmsKeyId"
                 },
                 "VpcConfig": {
@@ -8890,15 +8895,15 @@
         "UpdateFlywheelRequest": {
             "members": {
                 "ActiveModelArn": {
                     "documentation": "<p>The Amazon Resource Number (ARN) of the active model version.</p>",
                     "shape": "ComprehendModelArn"
                 },
                 "DataAccessRoleArn": {
-                    "documentation": "<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend permission to access the flywheel data.</p>",
+                    "documentation": "<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.</p>",
                     "shape": "IamRoleArn"
                 },
                 "DataSecurityConfig": {
                     "documentation": "<p>Flywheel data security configuration.</p>",
                     "shape": "UpdateDataSecurityConfig"
                 },
                 "FlywheelArn": {
@@ -8929,15 +8934,15 @@
             "documentation": "<p> Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>",
             "members": {
                 "SecurityGroupIds": {
                     "documentation": "<p>The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you\u2019ll be accessing on the VPC. This ID number is preceded by \"sg-\", for instance: \"sg-03b388029b0a285ea\". For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html\">Security Groups for your VPC</a>. </p>",
                     "shape": "SecurityGroupIds"
                 },
                 "Subnets": {
-                    "documentation": "<p>The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC\u2019s region. This ID number is preceded by \"subnet-\", for instance: \"subnet-04ccf456919e69055\". For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html\">VPCs and Subnets</a>. </p>",
+                    "documentation": "<p>The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC\u2019s Region. This ID number is preceded by \"subnet-\", for instance: \"subnet-04ccf456919e69055\". For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html\">VPCs and Subnets</a>. </p>",
                     "shape": "Subnets"
                 }
             },
             "required": [
                 "SecurityGroupIds",
                 "Subnets"
             ],
```

### Comparing `botocore-a-la-carte-comprehend-1.29.98/botocore_a_la_carte_comprehend.egg-info/PKG-INFO` & `botocore-a-la-carte-comprehend-1.29.99/botocore_a_la_carte_comprehend.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-comprehend
-Version: 1.29.98
+Version: 1.29.99
 Summary: comprehend data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-comprehend-1.29.98/setup.py` & `botocore-a-la-carte-comprehend-1.29.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-comprehend',
-    version="1.29.98",
+    version="1.29.99",
     description='comprehend data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/comprehend/*/*.json'],
```

