# Comparing `tmp/botocore-a-la-carte-cloudwatch-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-cloudwatch-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-cloudwatch-1.29.98.tar", last modified: Fri Mar 24 01:24:04 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-cloudwatch-1.29.99.tar", last modified: Sat Mar 25 01:22:22 2023, max compression
```

## Comparing `botocore-a-la-carte-cloudwatch-1.29.98.tar` & `botocore-a-la-carte-cloudwatch-1.29.99.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.673806 botocore-a-la-carte-cloudwatch-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-24 01:24:04.673806 botocore-a-la-carte-cloudwatch-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.669806 botocore-a-la-carte-cloudwatch-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.669806 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.669806 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.669806 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14395 2023-03-24 01:23:57.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-24 01:23:57.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-24 01:23:57.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   216298 2023-03-24 01:23:57.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)      644 2023-03-24 01:23:57.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:04.673806 botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      505 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:04.673806 botocore-a-la-carte-cloudwatch-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-03-24 01:24:04.000000 botocore-a-la-carte-cloudwatch-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.050354 botocore-a-la-carte-cloudwatch-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:22:21.000000 botocore-a-la-carte-cloudwatch-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-25 01:22:22.050354 botocore-a-la-carte-cloudwatch-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.046354 botocore-a-la-carte-cloudwatch-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.046354 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.046354 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.050354 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    19610 2023-03-25 01:22:12.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-25 01:22:12.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-25 01:22:12.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   219046 2023-03-25 01:22:12.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)      644 2023-03-25 01:22:12.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:22.050354 botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-25 01:22:22.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      505 2023-03-25 01:22:22.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:22:22.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:22:22.000000 botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:22:22.050354 botocore-a-la-carte-cloudwatch-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-03-25 01:22:21.000000 botocore-a-la-carte-cloudwatch-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/LICENSE.txt` & `botocore-a-la-carte-cloudwatch-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/PKG-INFO` & `botocore-a-la-carte-cloudwatch-1.29.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-cloudwatch
-Version: 1.29.98
+Version: 1.29.99
 Summary: cloudwatch data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/endpoint-rule-set-1.json`

 * *Files 18% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8951340663580246%*

 * *Differences: {"'parameters'": "{'Region': {'required': False}}",*

 * * "'rules'": "{0: {'conditions': {0: {'fn': 'isSet', 'argv': {0: {'ref': 'Endpoint'}}, delete: "*

 * *            "['assign']}}, 'rules': {0: {'type': 'error', 'error': 'Invalid Configuration: FIPS "*

 * *            "and custom endpoint are not supported', delete: ['rules']}, 1: {'conditions': [], "*

 * *            "'rules': {0: {'conditions': {0: {'argv': {insert: [(0, OrderedDict([('ref', "*

 * *            "'UseDualStack')]))], delete: [1]}}}, 'type': 'error', 'error': 'I […]*

```diff
@@ -5,15 +5,15 @@
             "documentation": "Override the endpoint used to send this request",
             "required": false,
             "type": "String"
         },
         "Region": {
             "builtIn": "AWS::Region",
             "documentation": "The AWS region used to dispatch the request.",
-            "required": true,
+            "required": false,
             "type": "String"
         },
         "UseDualStack": {
             "builtIn": "AWS::UseDualStack",
             "default": false,
             "documentation": "When true, use the dual-stack endpoint. If the configured endpoint does not support dual-stack, dispatching the request MAY return an error.",
             "required": true,
@@ -29,303 +29,347 @@
     },
     "rules": [
         {
             "conditions": [
                 {
                     "argv": [
                         {
-                            "ref": "Region"
+                            "ref": "Endpoint"
                         }
                     ],
-                    "assign": "PartitionResult",
-                    "fn": "aws.partition"
+                    "fn": "isSet"
                 }
             ],
             "rules": [
                 {
                     "conditions": [
                         {
                             "argv": [
                                 {
-                                    "ref": "Endpoint"
-                                }
+                                    "ref": "UseFIPS"
+                                },
+                                true
                             ],
-                            "fn": "isSet"
+                            "fn": "booleanEquals"
                         }
                     ],
+                    "error": "Invalid Configuration: FIPS and custom endpoint are not supported",
+                    "type": "error"
+                },
+                {
+                    "conditions": [],
                     "rules": [
                         {
                             "conditions": [
                                 {
                                     "argv": [
                                         {
-                                            "ref": "UseFIPS"
+                                            "ref": "UseDualStack"
                                         },
                                         true
                                     ],
                                     "fn": "booleanEquals"
                                 }
                             ],
-                            "error": "Invalid Configuration: FIPS and custom endpoint are not supported",
+                            "error": "Invalid Configuration: Dualstack and custom endpoint are not supported",
                             "type": "error"
                         },
                         {
                             "conditions": [],
-                            "rules": [
-                                {
-                                    "conditions": [
-                                        {
-                                            "argv": [
-                                                {
-                                                    "ref": "UseDualStack"
-                                                },
-                                                true
-                                            ],
-                                            "fn": "booleanEquals"
-                                        }
-                                    ],
-                                    "error": "Invalid Configuration: Dualstack and custom endpoint are not supported",
-                                    "type": "error"
-                                },
-                                {
-                                    "conditions": [],
-                                    "endpoint": {
-                                        "headers": {},
-                                        "properties": {},
-                                        "url": {
-                                            "ref": "Endpoint"
-                                        }
-                                    },
-                                    "type": "endpoint"
+                            "endpoint": {
+                                "headers": {},
+                                "properties": {},
+                                "url": {
+                                    "ref": "Endpoint"
                                 }
-                            ],
-                            "type": "tree"
+                            },
+                            "type": "endpoint"
                         }
                     ],
                     "type": "tree"
-                },
+                }
+            ],
+            "type": "tree"
+        },
+        {
+            "conditions": [],
+            "rules": [
                 {
                     "conditions": [
                         {
                             "argv": [
                                 {
-                                    "ref": "UseFIPS"
-                                },
-                                true
-                            ],
-                            "fn": "booleanEquals"
-                        },
-                        {
-                            "argv": [
-                                {
-                                    "ref": "UseDualStack"
-                                },
-                                true
+                                    "ref": "Region"
+                                }
                             ],
-                            "fn": "booleanEquals"
+                            "fn": "isSet"
                         }
                     ],
                     "rules": [
                         {
                             "conditions": [
                                 {
                                     "argv": [
-                                        true,
+                                        {
+                                            "ref": "Region"
+                                        }
+                                    ],
+                                    "assign": "PartitionResult",
+                                    "fn": "aws.partition"
+                                }
+                            ],
+                            "rules": [
+                                {
+                                    "conditions": [
                                         {
                                             "argv": [
                                                 {
-                                                    "ref": "PartitionResult"
+                                                    "ref": "UseFIPS"
                                                 },
-                                                "supportsFIPS"
+                                                true
                                             ],
-                                            "fn": "getAttr"
+                                            "fn": "booleanEquals"
+                                        },
+                                        {
+                                            "argv": [
+                                                {
+                                                    "ref": "UseDualStack"
+                                                },
+                                                true
+                                            ],
+                                            "fn": "booleanEquals"
                                         }
                                     ],
-                                    "fn": "booleanEquals"
-                                },
-                                {
-                                    "argv": [
-                                        true,
+                                    "rules": [
                                         {
-                                            "argv": [
+                                            "conditions": [
                                                 {
-                                                    "ref": "PartitionResult"
+                                                    "argv": [
+                                                        true,
+                                                        {
+                                                            "argv": [
+                                                                {
+                                                                    "ref": "PartitionResult"
+                                                                },
+                                                                "supportsFIPS"
+                                                            ],
+                                                            "fn": "getAttr"
+                                                        }
+                                                    ],
+                                                    "fn": "booleanEquals"
                                                 },
-                                                "supportsDualStack"
+                                                {
+                                                    "argv": [
+                                                        true,
+                                                        {
+                                                            "argv": [
+                                                                {
+                                                                    "ref": "PartitionResult"
+                                                                },
+                                                                "supportsDualStack"
+                                                            ],
+                                                            "fn": "getAttr"
+                                                        }
+                                                    ],
+                                                    "fn": "booleanEquals"
+                                                }
+                                            ],
+                                            "rules": [
+                                                {
+                                                    "conditions": [],
+                                                    "rules": [
+                                                        {
+                                                            "conditions": [],
+                                                            "endpoint": {
+                                                                "headers": {},
+                                                                "properties": {},
+                                                                "url": "https://monitoring-fips.{Region}.{PartitionResult#dualStackDnsSuffix}"
+                                                            },
+                                                            "type": "endpoint"
+                                                        }
+                                                    ],
+                                                    "type": "tree"
+                                                }
                                             ],
-                                            "fn": "getAttr"
+                                            "type": "tree"
+                                        },
+                                        {
+                                            "conditions": [],
+                                            "error": "FIPS and DualStack are enabled, but this partition does not support one or both",
+                                            "type": "error"
                                         }
                                     ],
-                                    "fn": "booleanEquals"
-                                }
-                            ],
-                            "rules": [
-                                {
-                                    "conditions": [],
-                                    "endpoint": {
-                                        "headers": {},
-                                        "properties": {},
-                                        "url": "https://monitoring-fips.{Region}.{PartitionResult#dualStackDnsSuffix}"
-                                    },
-                                    "type": "endpoint"
-                                }
-                            ],
-                            "type": "tree"
-                        },
-                        {
-                            "conditions": [],
-                            "error": "FIPS and DualStack are enabled, but this partition does not support one or both",
-                            "type": "error"
-                        }
-                    ],
-                    "type": "tree"
-                },
-                {
-                    "conditions": [
-                        {
-                            "argv": [
-                                {
-                                    "ref": "UseFIPS"
+                                    "type": "tree"
                                 },
-                                true
-                            ],
-                            "fn": "booleanEquals"
-                        }
-                    ],
-                    "rules": [
-                        {
-                            "conditions": [
                                 {
-                                    "argv": [
-                                        true,
+                                    "conditions": [
                                         {
                                             "argv": [
                                                 {
-                                                    "ref": "PartitionResult"
+                                                    "ref": "UseFIPS"
                                                 },
-                                                "supportsFIPS"
+                                                true
                                             ],
-                                            "fn": "getAttr"
+                                            "fn": "booleanEquals"
                                         }
                                     ],
-                                    "fn": "booleanEquals"
-                                }
-                            ],
-                            "rules": [
-                                {
-                                    "conditions": [],
                                     "rules": [
                                         {
                                             "conditions": [
                                                 {
                                                     "argv": [
-                                                        "aws-us-gov",
+                                                        true,
                                                         {
                                                             "argv": [
                                                                 {
                                                                     "ref": "PartitionResult"
                                                                 },
-                                                                "name"
+                                                                "supportsFIPS"
                                                             ],
                                                             "fn": "getAttr"
                                                         }
                                                     ],
-                                                    "fn": "stringEquals"
+                                                    "fn": "booleanEquals"
                                                 }
                                             ],
-                                            "endpoint": {
-                                                "headers": {},
-                                                "properties": {},
-                                                "url": "https://monitoring.{Region}.{PartitionResult#dnsSuffix}"
-                                            },
-                                            "type": "endpoint"
+                                            "rules": [
+                                                {
+                                                    "conditions": [],
+                                                    "rules": [
+                                                        {
+                                                            "conditions": [
+                                                                {
+                                                                    "argv": [
+                                                                        "aws-us-gov",
+                                                                        {
+                                                                            "argv": [
+                                                                                {
+                                                                                    "ref": "PartitionResult"
+                                                                                },
+                                                                                "name"
+                                                                            ],
+                                                                            "fn": "getAttr"
+                                                                        }
+                                                                    ],
+                                                                    "fn": "stringEquals"
+                                                                }
+                                                            ],
+                                                            "endpoint": {
+                                                                "headers": {},
+                                                                "properties": {},
+                                                                "url": "https://monitoring.{Region}.amazonaws.com"
+                                                            },
+                                                            "type": "endpoint"
+                                                        },
+                                                        {
+                                                            "conditions": [],
+                                                            "endpoint": {
+                                                                "headers": {},
+                                                                "properties": {},
+                                                                "url": "https://monitoring-fips.{Region}.{PartitionResult#dnsSuffix}"
+                                                            },
+                                                            "type": "endpoint"
+                                                        }
+                                                    ],
+                                                    "type": "tree"
+                                                }
+                                            ],
+                                            "type": "tree"
                                         },
                                         {
                                             "conditions": [],
-                                            "endpoint": {
-                                                "headers": {},
-                                                "properties": {},
-                                                "url": "https://monitoring-fips.{Region}.{PartitionResult#dnsSuffix}"
-                                            },
-                                            "type": "endpoint"
+                                            "error": "FIPS is enabled but this partition does not support FIPS",
+                                            "type": "error"
                                         }
                                     ],
                                     "type": "tree"
-                                }
-                            ],
-                            "type": "tree"
-                        },
-                        {
-                            "conditions": [],
-                            "error": "FIPS is enabled but this partition does not support FIPS",
-                            "type": "error"
-                        }
-                    ],
-                    "type": "tree"
-                },
-                {
-                    "conditions": [
-                        {
-                            "argv": [
-                                {
-                                    "ref": "UseDualStack"
                                 },
-                                true
-                            ],
-                            "fn": "booleanEquals"
-                        }
-                    ],
-                    "rules": [
-                        {
-                            "conditions": [
                                 {
-                                    "argv": [
-                                        true,
+                                    "conditions": [
                                         {
                                             "argv": [
                                                 {
-                                                    "ref": "PartitionResult"
+                                                    "ref": "UseDualStack"
                                                 },
-                                                "supportsDualStack"
+                                                true
                                             ],
-                                            "fn": "getAttr"
+                                            "fn": "booleanEquals"
                                         }
                                     ],
-                                    "fn": "booleanEquals"
-                                }
-                            ],
-                            "rules": [
+                                    "rules": [
+                                        {
+                                            "conditions": [
+                                                {
+                                                    "argv": [
+                                                        true,
+                                                        {
+                                                            "argv": [
+                                                                {
+                                                                    "ref": "PartitionResult"
+                                                                },
+                                                                "supportsDualStack"
+                                                            ],
+                                                            "fn": "getAttr"
+                                                        }
+                                                    ],
+                                                    "fn": "booleanEquals"
+                                                }
+                                            ],
+                                            "rules": [
+                                                {
+                                                    "conditions": [],
+                                                    "rules": [
+                                                        {
+                                                            "conditions": [],
+                                                            "endpoint": {
+                                                                "headers": {},
+                                                                "properties": {},
+                                                                "url": "https://monitoring.{Region}.{PartitionResult#dualStackDnsSuffix}"
+                                                            },
+                                                            "type": "endpoint"
+                                                        }
+                                                    ],
+                                                    "type": "tree"
+                                                }
+                                            ],
+                                            "type": "tree"
+                                        },
+                                        {
+                                            "conditions": [],
+                                            "error": "DualStack is enabled but this partition does not support DualStack",
+                                            "type": "error"
+                                        }
+                                    ],
+                                    "type": "tree"
+                                },
                                 {
                                     "conditions": [],
-                                    "endpoint": {
-                                        "headers": {},
-                                        "properties": {},
-                                        "url": "https://monitoring.{Region}.{PartitionResult#dualStackDnsSuffix}"
-                                    },
-                                    "type": "endpoint"
+                                    "rules": [
+                                        {
+                                            "conditions": [],
+                                            "endpoint": {
+                                                "headers": {},
+                                                "properties": {},
+                                                "url": "https://monitoring.{Region}.{PartitionResult#dnsSuffix}"
+                                            },
+                                            "type": "endpoint"
+                                        }
+                                    ],
+                                    "type": "tree"
                                 }
                             ],
                             "type": "tree"
-                        },
-                        {
-                            "conditions": [],
-                            "error": "DualStack is enabled but this partition does not support DualStack",
-                            "type": "error"
                         }
                     ],
                     "type": "tree"
                 },
                 {
                     "conditions": [],
-                    "endpoint": {
-                        "headers": {},
-                        "properties": {},
-                        "url": "https://monitoring.{Region}.{PartitionResult#dnsSuffix}"
-                    },
-                    "type": "endpoint"
+                    "error": "Invalid Configuration: Missing Region",
+                    "type": "error"
                 }
             ],
             "type": "tree"
         }
     ],
     "version": "1.0"
 }
```

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/paginators-1.json` & `botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/service-2.json` & `botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/service-2.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9996960985851565%*

 * *Differences: {"'operations'": "{'DeleteAlarms': {'documentation': '<p>Deletes the specified alarms. You can "*

 * *                 'delete up to 100 alarms in one operation. However, this total can include no '*

 * *                 'more than one composite alarm. For example, you could delete 99 metric alarms '*

 * *                 "and one composite alarms with one operation, but you can\\'t delete two "*

 * *                 'composite alarms with one operation.</p> <p> If you specify an incorrect alarm '*

 * *                 'name or mak […]*

```diff
@@ -9,15 +9,15 @@
         "serviceId": "CloudWatch",
         "signatureVersion": "v4",
         "uid": "monitoring-2010-08-01",
         "xmlNamespace": "http://monitoring.amazonaws.com/doc/2010-08-01/"
     },
     "operations": {
         "DeleteAlarms": {
-            "documentation": "<p>Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can't delete two composite alarms with one operation.</p> <p> In the event of an error, no alarms are deleted.</p> <note> <p>It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can't delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.</p> <p>To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the <code>AlarmRule</code> of one of the alarms to <code>false</code>. </p> <p>Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. </p> </note>",
+            "documentation": "<p>Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can't delete two composite alarms with one operation.</p> <p> If you specify an incorrect alarm name or make any other error in the operation, no alarms are deleted. To confirm that alarms were deleted successfully, you can use the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html\">DescribeAlarms</a> operation after using <code>DeleteAlarms</code>.</p> <note> <p>It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can't delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.</p> <p>To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the <code>AlarmRule</code> of one of the alarms to <code>false</code>. </p> <p>Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. </p> </note>",
             "errors": [
                 {
                     "shape": "ResourceNotFound"
                 }
             ],
             "http": {
                 "method": "POST",
@@ -702,15 +702,15 @@
             "name": "PutManagedInsightRules",
             "output": {
                 "resultWrapper": "PutManagedInsightRulesResult",
                 "shape": "PutManagedInsightRulesOutput"
             }
         },
         "PutMetricAlarm": {
-            "documentation": "<p>Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query. For more information about using a Metrics Insights query for an alarm, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html\">Create alarms on Metrics Insights queries</a>.</p> <p>Alarms based on anomaly detection models cannot have Auto Scaling actions.</p> <p>When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.</p> <p>When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</p> <p>If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:</p> <ul> <li> <p>The <code>iam:CreateServiceLinkedRole</code> for all alarms with EC2 actions</p> </li> <li> <p>The <code>iam:CreateServiceLinkedRole</code> to create an alarm with Systems Manager OpsItem actions.</p> </li> </ul> <p>The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called <code>AWSServiceRoleForCloudWatchEvents</code> and <code>AWSServiceRoleForCloudWatchAlarms_ActionSSM</code>. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role\">Amazon Web Services service-linked role</a>.</p> <p> <b>Cross-account alarms</b> </p> <p>You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:</p> <ul> <li> <p>The account where the metrics are located (the <i>sharing account</i>) must already have a sharing role named <b>CloudWatch-CrossAccountSharingRole</b>. If it does not already have this role, you must create it using the instructions in <b>Set up a sharing account</b> in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\"> Cross-account cross-Region CloudWatch console</a>. The policy for that role must grant access to the ID of the account where you are creating the alarm. </p> </li> <li> <p>The account where you are creating the alarm (the <i>monitoring account</i>) must already have a service-linked role named <b>AWSServiceRoleForCloudWatchCrossAccount</b> to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in <b>Set up a monitoring account</b> in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\"> Cross-account cross-Region CloudWatch console</a>.</p> </li> </ul>",
+            "documentation": "<p>Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query. For more information about using a Metrics Insights query for an alarm, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html\">Create alarms on Metrics Insights queries</a>.</p> <p>Alarms based on anomaly detection models cannot have Auto Scaling actions.</p> <p>When this operation creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.</p> <p>When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.</p> <p>If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:</p> <ul> <li> <p>The <code>iam:CreateServiceLinkedRole</code> permission for all alarms with EC2 actions</p> </li> <li> <p>The <code>iam:CreateServiceLinkedRole</code> permissions to create an alarm with Systems Manager OpsItem or response plan actions.</p> </li> </ul> <p>The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called <code>AWSServiceRoleForCloudWatchEvents</code> and <code>AWSServiceRoleForCloudWatchAlarms_ActionSSM</code>. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role\">Amazon Web Services service-linked role</a>.</p> <p> <b>Cross-account alarms</b> </p> <p>You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:</p> <ul> <li> <p>The account where the metrics are located (the <i>sharing account</i>) must already have a sharing role named <b>CloudWatch-CrossAccountSharingRole</b>. If it does not already have this role, you must create it using the instructions in <b>Set up a sharing account</b> in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\"> Cross-account cross-Region CloudWatch console</a>. The policy for that role must grant access to the ID of the account where you are creating the alarm. </p> </li> <li> <p>The account where you are creating the alarm (the <i>monitoring account</i>) must already have a service-linked role named <b>AWSServiceRoleForCloudWatchCrossAccount</b> to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in <b>Set up a monitoring account</b> in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\"> Cross-account cross-Region CloudWatch console</a>.</p> </li> </ul>",
             "errors": [
                 {
                     "shape": "LimitExceededFault"
                 }
             ],
             "http": {
                 "method": "POST",
@@ -1452,15 +1452,15 @@
         "DatapointsToAlarm": {
             "min": 1,
             "type": "integer"
         },
         "DeleteAlarmsInput": {
             "members": {
                 "AlarmNames": {
-                    "documentation": "<p>The alarms to be deleted.</p>",
+                    "documentation": "<p>The alarms to be deleted. Do not enclose the alarm names in quote marks.</p>",
                     "shape": "AlarmNames"
                 }
             },
             "required": [
                 "AlarmNames"
             ],
             "type": "structure"
@@ -1781,19 +1781,19 @@
             },
             "type": "structure"
         },
         "Dimension": {
             "documentation": "<p>A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish <code>InstanceId</code> as a dimension name, and the actual instance ID as the value for that dimension.</p> <p>You can assign up to 30 dimensions to a metric.</p>",
             "members": {
                 "Name": {
-                    "documentation": "<p>The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (<code>:</code>).</p>",
+                    "documentation": "<p>The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (<code>:</code>). ASCII control characters are not supported as part of dimension names.</p>",
                     "shape": "DimensionName"
                 },
                 "Value": {
-                    "documentation": "<p>The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character.</p>",
+                    "documentation": "<p>The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.</p>",
                     "shape": "DimensionValue"
                 }
             },
             "required": [
                 "Name",
                 "Value"
             ],
@@ -3179,15 +3179,15 @@
             "documentation": "<p>Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.</p>",
             "members": {
                 "Counts": {
                     "documentation": "<p>Array of numbers that is used along with the <code>Values</code> array. Each number in the <code>Count</code> array is the number of times the corresponding value in the <code>Values</code> array occurred during the period. </p> <p>If you omit the <code>Counts</code> array, the default of 1 is used as the value for each count. If you include a <code>Counts</code> array, it must include the same amount of values as the <code>Values</code> array.</p>",
                     "shape": "Counts"
                 },
                 "Dimensions": {
-                    "documentation": "<p>The dimensions associated with the metric.</p>",
+                    "documentation": "<p>The dimensions associated with the metric. </p>",
                     "shape": "Dimensions"
                 },
                 "MetricName": {
                     "documentation": "<p>The name of the metric.</p>",
                     "shape": "MetricName"
                 },
                 "StatisticValues": {
@@ -3312,15 +3312,15 @@
                     "documentation": "<p>The current state of this stream. Valid values are <code>running</code> and <code>stopped</code>.</p>",
                     "shape": "MetricStreamState"
                 }
             },
             "type": "structure"
         },
         "MetricStreamFilter": {
-            "documentation": "<p>This structure contains the name of one of the metric namespaces that is listed in a filter of a metric stream.</p>",
+            "documentation": "<p>This structure contains the name of one of the metric namespaces that is listed in a filter of a metric stream.</p> <p>The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.</p>",
             "members": {
                 "Namespace": {
                     "documentation": "<p>The name of the metric namespace in the filter.</p>",
                     "shape": "Namespace"
                 }
             },
             "type": "structure"
@@ -3661,23 +3661,23 @@
         "PutMetricAlarmInput": {
             "members": {
                 "ActionsEnabled": {
                     "documentation": "<p>Indicates whether actions should be executed during any changes to the alarm state. The default is <code>TRUE</code>.</p>",
                     "shape": "ActionsEnabled"
                 },
                 "AlarmActions": {
-                    "documentation": "<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: <code>arn:aws:automate:<i>region</i>:ec2:stop</code> | <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> | <code>arn:aws:automate:<i>region</i>:ec2:recover</code> | <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> | <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> | <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> | <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i> </code> | <code>arn:aws:ssm-incidents::<i>account-id</i>:response-plan:<i>response-plan-name</i> </code> </p> <p>Valid Values (for use with IAM roles): <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p>",
+                    "documentation": "<p>The actions to execute when this alarm transitions to the <code>ALARM</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSN notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>",
                     "shape": "ResourceList"
                 },
                 "AlarmDescription": {
                     "documentation": "<p>The description for the alarm.</p>",
                     "shape": "AlarmDescription"
                 },
                 "AlarmName": {
-                    "documentation": "<p>The name for the alarm. This name must be unique within the Region.</p>",
+                    "documentation": "<p>The name for the alarm. This name must be unique within the Region.</p> <p>The name must contain only UTF-8 characters, and can't contain ASCII control characters</p>",
                     "shape": "AlarmName"
                 },
                 "ComparisonOperator": {
                     "documentation": "<p> The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.</p> <p>The values <code>LessThanLowerOrGreaterThanUpperThreshold</code>, <code>LessThanLowerThreshold</code>, and <code>GreaterThanUpperThreshold</code> are used only for alarms based on anomaly detection models.</p>",
                     "shape": "ComparisonOperator"
                 },
                 "DatapointsToAlarm": {
@@ -3697,15 +3697,15 @@
                     "shape": "EvaluationPeriods"
                 },
                 "ExtendedStatistic": {
                     "documentation": "<p>The percentile statistic for the metric specified in <code>MetricName</code>. Specify a value between p0.0 and p100. When you call <code>PutMetricAlarm</code> and specify a <code>MetricName</code>, you must specify either <code>Statistic</code> or <code>ExtendedStatistic,</code> but not both.</p>",
                     "shape": "ExtendedStatistic"
                 },
                 "InsufficientDataActions": {
-                    "documentation": "<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: <code>arn:aws:automate:<i>region</i>:ec2:stop</code> | <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> | <code>arn:aws:automate:<i>region</i>:ec2:recover</code> | <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> | <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> | <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> <p>Valid Values (for use with IAM roles): <code>&gt;arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p>",
+                    "documentation": "<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSN notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>",
                     "shape": "ResourceList"
                 },
                 "MetricName": {
                     "documentation": "<p>The name for the metric associated with the alarm. For each <code>PutMetricAlarm</code> operation, you must specify either <code>MetricName</code> or a <code>Metrics</code> array.</p> <p>If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the <code>Dimensions</code>, <code>Period</code>, <code>Namespace</code>, <code>Statistic</code>, or <code>ExtendedStatistic</code> parameters. Instead, you specify all this information in the <code>Metrics</code> array.</p>",
                     "shape": "MetricName"
                 },
                 "Metrics": {
@@ -3713,15 +3713,15 @@
                     "shape": "MetricDataQueries"
                 },
                 "Namespace": {
                     "documentation": "<p>The namespace for the metric associated specified in <code>MetricName</code>.</p>",
                     "shape": "Namespace"
                 },
                 "OKActions": {
-                    "documentation": "<p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p> <p>Valid Values: <code>arn:aws:automate:<i>region</i>:ec2:stop</code> | <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> | <code>arn:aws:automate:<i>region</i>:ec2:recover</code> | <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> | <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i> </code> | <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> <p>Valid Values (for use with IAM roles): <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> | <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p>",
+                    "documentation": "<p>The actions to execute when this alarm transitions to an <code>OK</code> state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:</p> <p> <b>EC2 actions:</b> </p> <ul> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:stop</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:terminate</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:reboot</code> </p> </li> <li> <p> <code>arn:aws:automate:<i>region</i>:ec2:recover</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Stop/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Terminate/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Reboot/1.0</code> </p> </li> <li> <p> <code>arn:aws:swf:<i>region</i>:<i>account-id</i>:action/actions/AWS_EC2.InstanceId.Recover/1.0</code> </p> </li> </ul> <p> <b>Autoscaling action:</b> </p> <ul> <li> <p> <code>arn:aws:autoscaling:<i>region</i>:<i>account-id</i>:scalingPolicy:<i>policy-id</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSN notification action:</b> </p> <ul> <li> <p> <code>arn:aws:sns:<i>region</i>:<i>account-id</i>:<i>sns-topic-name</i>:autoScalingGroupName/<i>group-friendly-name</i>:policyName/<i>policy-friendly-name</i> </code> </p> </li> </ul> <p> <b>SSM integration actions:</b> </p> <ul> <li> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:opsitem:<i>severity</i>#CATEGORY=<i>category-name</i> </code> </p> </li> <li> <p> <code>arn:aws:ssm-incidents::<i>account-id</i>:responseplan/<i>response-plan-name</i> </code> </p> </li> </ul>",
                     "shape": "ResourceList"
                 },
                 "Period": {
                     "documentation": "<p>The length, in seconds, used each time the metric specified in <code>MetricName</code> is evaluated. Valid values are 10, 30, and any multiple of 60.</p> <p> <code>Period</code> is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the <code>Metrics</code> array.</p> <p>Be sure to specify 10 or 30 only for metrics that are stored by a <code>PutMetricData</code> call with a <code>StorageResolution</code> of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm might often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see <a href=\"https://aws.amazon.com/cloudwatch/pricing/\">Amazon CloudWatch Pricing</a>.</p> <p>An alarm's total current evaluation period can be no longer than one day, so <code>Period</code> multiplied by <code>EvaluationPeriods</code> cannot be more than 86,400 seconds.</p>",
                     "shape": "Period"
                 },
                 "Statistic": {
@@ -3759,15 +3759,15 @@
         "PutMetricDataInput": {
             "members": {
                 "MetricData": {
                     "documentation": "<p>The data for the metric. The array can include no more than 1000 metrics per call.</p>",
                     "shape": "MetricData"
                 },
                 "Namespace": {
-                    "documentation": "<p>The namespace for the metric data.</p> <p>To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with <code>AWS/</code> </p>",
+                    "documentation": "<p>The namespace for the metric data. You can use ASCII characters for the namespace, except for control characters which are not supported.</p> <p>To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with <code>AWS/</code> </p>",
                     "shape": "Namespace"
                 }
             },
             "required": [
                 "Namespace",
                 "MetricData"
             ],
```

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/botocore/data/cloudwatch/2010-08-01/waiters-2.json` & `botocore-a-la-carte-cloudwatch-1.29.99/botocore/data/cloudwatch/2010-08-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/botocore_a_la_carte_cloudwatch.egg-info/PKG-INFO` & `botocore-a-la-carte-cloudwatch-1.29.99/botocore_a_la_carte_cloudwatch.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-cloudwatch
-Version: 1.29.98
+Version: 1.29.99
 Summary: cloudwatch data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-cloudwatch-1.29.98/setup.py` & `botocore-a-la-carte-cloudwatch-1.29.99/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-cloudwatch',
-    version="1.29.98",
+    version="1.29.99",
     description='cloudwatch data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/cloudwatch/*/*.json'],
```

