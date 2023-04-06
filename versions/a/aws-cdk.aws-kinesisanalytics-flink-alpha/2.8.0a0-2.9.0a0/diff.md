# Comparing `tmp/aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0.tar.gz` & `tmp/aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/individual-packages/aws-kinesisanalytics-flink/dist/python/aws-cdk.aws-kinesisanaly", last modified: Thu Jan 13 18:05:51 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/individual-packages/aws-kinesisanalytics-flink/dist/python/aws-cdk.aws-kinesisanaly", last modified: Wed Jan 26 11:22:06 2022, max compression
```

## Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0.tar` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      113 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     4679 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3674 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1907 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/
--rw-r--r--   0 root         (0) root         (0)    53164 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/
--rw-r--r--   0 root         (0) root         (0)      435 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)    45905 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.8.0-alpha.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:47.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4679 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      680 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       92 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 18:05:51.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      113 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     4679 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3674 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1907 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/
+-rw-r--r--   0 root         (0) root         (0)    53164 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      435 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    45998 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.9.0-alpha.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:01.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4679 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      680 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       92 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 11:22:06.000000 aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/top_level.txt
```

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/LICENSE` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/PKG-INFO` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-kinesisanalytics-flink-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: A CDK Construct Library for Kinesis Analytics Flink applications
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/README.md` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/README.md`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/setup.py` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.aws-kinesisanalytics-flink-alpha",
-    "version": "2.8.0.a0",
+    "version": "2.9.0.a0",
     "description": "A CDK Construct Library for Kinesis Analytics Flink applications",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,23 +22,23 @@
     },
     "packages": [
         "aws_cdk.aws_kinesisanalytics_flink_alpha",
         "aws_cdk.aws_kinesisanalytics_flink_alpha._jsii"
     ],
     "package_data": {
         "aws_cdk.aws_kinesisanalytics_flink_alpha._jsii": [
-            "aws-kinesisanalytics-flink-alpha@2.8.0-alpha.0.jsii.tgz"
+            "aws-kinesisanalytics-flink-alpha@2.9.0-alpha.0.jsii.tgz"
         ],
         "aws_cdk.aws_kinesisanalytics_flink_alpha": [
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

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/__init__.py` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.8.0-alpha.0.jsii.tgz` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.9.0-alpha.0.jsii.tgz`

 * *Files 27% similar despite different names*

#### Comparing `aws-kinesisanalytics-flink-alpha@2.8.0-alpha.0.jsii.tgz-content` & `aws-kinesisanalytics-flink-alpha@2.9.0-alpha.0.jsii.tgz-content`

##### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0   127273 1985-10-26 08:15:00.000000 package/.jsii
+-rw-r--r--   0        0        0   128805 1985-10-26 08:15:00.000000 package/.jsii
 -rw-rw-r--   0        0        0    11391 1985-10-26 08:15:00.000000 package/LICENSE
 -rw-rw-r--   0        0        0      113 1985-10-26 08:15:00.000000 package/NOTICE
 -rw-r--r--   0        0        0     2513 1985-10-26 08:15:00.000000 package/.warnings.jsii.js
 -rw-r--r--   0        0        0    10998 1985-10-26 08:15:00.000000 package/lib/application-code.js
 -rw-r--r--   0        0        0    27117 1985-10-26 08:15:00.000000 package/lib/application.js
 -rw-r--r--   0        0        0     1913 1985-10-26 08:15:00.000000 package/lib/private/environment-properties.js
 -rw-r--r--   0        0        0     6254 1985-10-26 08:15:00.000000 package/lib/private/flink-application-configuration.js
```

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.965246067985794%*

 * *Differences: {"'dependencies'": "{'aws-cdk-lib': '^2.9.0'}",*

 * * "'dependencyClosure'": "{'aws-cdk-lib': {'submodules': {'aws-cdk-lib.aws_forecast': "*

 * *                        "OrderedDict([('targets', OrderedDict([('dotnet', "*

 * *                        "OrderedDict([('namespace', 'Amazon.CDK.AWS.Forecast')])), ('java', "*

 * *                        "OrderedDict([('package', 'software.amazon.awscdk.services.forecast')])), "*

 * *                        "('python', OrderedDict([('module', 'aws_cdk.aws_forecast')]))]))]), "*

 * *             […]*

```diff
@@ -4,15 +4,15 @@
         "organization": true,
         "roles": [
             "author"
         ],
         "url": "https://aws.amazon.com"
     },
     "dependencies": {
-        "aws-cdk-lib": "^2.8.0",
+        "aws-cdk-lib": "^2.9.0",
         "constructs": "^10.0.0"
     },
     "dependencyClosure": {
         "aws-cdk-lib": {
             "submodules": {
                 "aws-cdk-lib.alexa_ask": {
                     "targets": {
@@ -1181,14 +1181,27 @@
                             "package": "software.amazon.awscdk.services.fms"
                         },
                         "python": {
                             "module": "aws_cdk.aws_fms"
                         }
                     }
                 },
+                "aws-cdk-lib.aws_forecast": {
+                    "targets": {
+                        "dotnet": {
+                            "namespace": "Amazon.CDK.AWS.Forecast"
+                        },
+                        "java": {
+                            "package": "software.amazon.awscdk.services.forecast"
+                        },
+                        "python": {
+                            "module": "aws_cdk.aws_forecast"
+                        }
+                    }
+                },
                 "aws-cdk-lib.aws_frauddetector": {
                     "targets": {
                         "dotnet": {
                             "namespace": "Amazon.CDK.AWS.FraudDetector"
                         },
                         "java": {
                             "package": "software.amazon.awscdk.services.frauddetector"
@@ -1363,14 +1376,27 @@
                             "package": "software.amazon.awscdk.services.inspector"
                         },
                         "python": {
                             "module": "aws_cdk.aws_inspector"
                         }
                     }
                 },
+                "aws-cdk-lib.aws_inspectorv2": {
+                    "targets": {
+                        "dotnet": {
+                            "namespace": "Amazon.CDK.AWS.InspectorV2"
+                        },
+                        "java": {
+                            "package": "software.amazon.awscdk.services.inspectorv2"
+                        },
+                        "python": {
+                            "module": "aws_cdk.aws_inspectorv2"
+                        }
+                    }
+                },
                 "aws-cdk-lib.aws_iot": {
                     "targets": {
                         "dotnet": {
                             "namespace": "Amazon.CDK.AWS.IoT"
                         },
                         "java": {
                             "package": "software.amazon.awscdk.services.iot"
@@ -1532,27 +1558,53 @@
                             "package": "software.amazon.awscdk.services.kinesisanalytics"
                         },
                         "python": {
                             "module": "aws_cdk.aws_kinesisanalytics"
                         }
                     }
                 },
+                "aws-cdk-lib.aws_kinesisanalyticsv2": {
+                    "targets": {
+                        "dotnet": {
+                            "namespace": "Amazon.CDK.AWS.KinesisAnalyticsV2"
+                        },
+                        "java": {
+                            "package": "software.amazon.awscdk.services.kinesisanalyticsv2"
+                        },
+                        "python": {
+                            "module": "aws_cdk.aws_kinesisanalyticsv2"
+                        }
+                    }
+                },
                 "aws-cdk-lib.aws_kinesisfirehose": {
                     "targets": {
                         "dotnet": {
                             "namespace": "Amazon.CDK.AWS.KinesisFirehose"
                         },
                         "java": {
                             "package": "software.amazon.awscdk.services.kinesisfirehose"
                         },
                         "python": {
                             "module": "aws_cdk.aws_kinesisfirehose"
                         }
                     }
                 },
+                "aws-cdk-lib.aws_kinesisvideo": {
+                    "targets": {
+                        "dotnet": {
+                            "namespace": "Amazon.CDK.AWS.KinesisVideo"
+                        },
+                        "java": {
+                            "package": "software.amazon.awscdk.services.kinesisvideo"
+                        },
+                        "python": {
+                            "module": "aws_cdk.aws_kinesisvideo"
+                        }
+                    }
+                },
                 "aws-cdk-lib.aws_kms": {
                     "targets": {
                         "dotnet": {
                             "namespace": "Amazon.CDK.AWS.KMS"
                         },
                         "java": {
                             "package": "software.amazon.awscdk.services.kms"
@@ -3988,9 +4040,9 @@
                         "primitive": "string"
                     }
                 }
             ],
             "symbolId": "lib/types:Runtime"
         }
     },
-    "version": "2.8.0-alpha.0"
+    "version": "2.9.0-alpha.0"
 }
```

##### package/lib/application-code.js

###### js-beautify {}

```diff
@@ -38,15 +38,15 @@
         return new AssetApplicationCode(path, options);
     }
 }
 exports.ApplicationCode = ApplicationCode;
 _a = JSII_RTTI_SYMBOL_1;
 ApplicationCode[_a] = {
     fqn: "@aws-cdk/aws-kinesisanalytics-flink-alpha.ApplicationCode",
-    version: "2.8.0-alpha.0"
+    version: "2.9.0-alpha.0"
 };
 class BucketApplicationCode extends ApplicationCode {
     constructor(props) {
         super();
         this.bucket = props.bucket;
         this.fileKey = props.fileKey;
         this.objectVersion = props.objectVersion;
```

##### package/lib/application.js

###### js-beautify {}

```diff
@@ -162,15 +162,15 @@
         });
     }
 }
 exports.Application = Application;
 _a = JSII_RTTI_SYMBOL_1;
 Application[_a] = {
     fqn: "@aws-cdk/aws-kinesisanalytics-flink-alpha.Application",
-    version: "2.8.0-alpha.0"
+    version: "2.9.0-alpha.0"
 };
 
 function applicationArnComponents(resourceName) {
     return {
         service: 'kinesisanalytics',
         resource: 'application',
         resourceName,
```

##### package/lib/types.js

###### js-beautify {}

```diff
@@ -47,15 +47,15 @@
         return new Runtime(value);
     }
 }
 exports.Runtime = Runtime;
 _a = JSII_RTTI_SYMBOL_1;
 Runtime[_a] = {
     fqn: "@aws-cdk/aws-kinesisanalytics-flink-alpha.Runtime",
-    version: "2.8.0-alpha.0"
+    version: "2.9.0-alpha.0"
 };
 /**
  * (experimental) Flink Version 1.6.
  *
  * @experimental
  */
 Runtime.FLINK_1_6 = Runtime.of('FLINK-1_6');
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9680059523809524%*

 * *Differences: {"'devDependencies'": "{'@aws-cdk/cdk-build-tools': '2.9.0', '@aws-cdk/cdk-integ-tools': '2.9.0', "*

 * *                      "'@aws-cdk/pkglint': '2.9.0', 'aws-cdk-lib': '2.9.0'}",*

 * * "'peerDependencies'": "{'aws-cdk-lib': '^2.9.0'}",*

 * * "'version'": "'2.9.0-alpha.0'"}*

```diff
@@ -16,19 +16,19 @@
         "env": {
             "AWSLINT_BASE_CONSTRUCT": true
         }
     },
     "dependencies": {},
     "description": "A CDK Construct Library for Kinesis Analytics Flink applications",
     "devDependencies": {
-        "@aws-cdk/cdk-build-tools": "2.8.0",
-        "@aws-cdk/cdk-integ-tools": "2.8.0",
-        "@aws-cdk/pkglint": "2.8.0",
+        "@aws-cdk/cdk-build-tools": "2.9.0",
+        "@aws-cdk/cdk-integ-tools": "2.9.0",
+        "@aws-cdk/pkglint": "2.9.0",
         "@types/jest": "^27.4.0",
-        "aws-cdk-lib": "2.8.0",
+        "aws-cdk-lib": "2.9.0",
         "constructs": "^10.0.0",
         "jest": "^27.4.7"
     },
     "engines": {
         "node": ">= 14.15.0"
     },
     "homepage": "https://github.com/aws/aws-cdk",
@@ -78,15 +78,15 @@
         "flink"
     ],
     "license": "Apache-2.0",
     "main": "lib/index.js",
     "maturity": "experimental",
     "name": "@aws-cdk/aws-kinesisanalytics-flink-alpha",
     "peerDependencies": {
-        "aws-cdk-lib": "^2.8.0",
+        "aws-cdk-lib": "^2.9.0",
         "constructs": "^10.0.0"
     },
     "pkglint": {
         "exclude": [
             "naming/package-matches-directory",
             "assert/assert-dependency"
         ]
@@ -114,9 +114,9 @@
         "pkglint": "pkglint -f",
         "rosetta:extract": "yarn --silent jsii-rosetta extract",
         "test": "cdk-test",
         "watch": "cdk-watch"
     },
     "stability": "experimental",
     "types": "lib/index.d.ts",
-    "version": "2.8.0-alpha.0"
+    "version": "2.9.0-alpha.0"
 }
```

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/PKG-INFO` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-kinesisanalytics-flink-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: A CDK Construct Library for Kinesis Analytics Flink applications
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.aws-kinesisanalytics-flink-alpha-2.8.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/SOURCES.txt` & `aws-cdk.aws-kinesisanalytics-flink-alpha-2.9.0a0/src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/SOURCES.txt
 src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/dependency_links.txt
 src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/requires.txt
 src/aws_cdk.aws_kinesisanalytics_flink_alpha.egg-info/top_level.txt
 src/aws_cdk/aws_kinesisanalytics_flink_alpha/__init__.py
 src/aws_cdk/aws_kinesisanalytics_flink_alpha/py.typed
 src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/__init__.py
-src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.8.0-alpha.0.jsii.tgz
+src/aws_cdk/aws_kinesisanalytics_flink_alpha/_jsii/aws-kinesisanalytics-flink-alpha@2.9.0-alpha.0.jsii.tgz
```

