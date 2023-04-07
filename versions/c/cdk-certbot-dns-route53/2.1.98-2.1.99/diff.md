# Comparing `tmp/cdk-certbot-dns-route53-2.1.98.tar.gz` & `tmp/cdk-certbot-dns-route53-2.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-certbot-dns-route53-2.1.98.tar", last modified: Wed Aug  3 00:35:23 2022, max compression
+gzip compressed data, was "cdk-certbot-dns-route53-2.1.99.tar", last modified: Thu Aug  4 00:33:28 2022, max compression
```

## Comparing `cdk-certbot-dns-route53-2.1.98.tar` & `cdk-certbot-dns-route53-2.1.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-03 00:35:23.268056 cdk-certbot-dns-route53-2.1.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     4151 2022-08-03 00:35:23.268056 cdk-certbot-dns-route53-2.1.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3174 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-03 00:35:23.268056 cdk-certbot-dns-route53-2.1.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1847 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-03 00:35:23.264056 cdk-certbot-dns-route53-2.1.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-03 00:35:23.264056 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/
--rw-r--r--   0 runner    (1001) docker     (121)    19910 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-03 00:35:23.264056 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      428 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    25975 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/_jsii/cdk-certbot-dns-route53@2.1.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-03 00:35:06.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-03 00:35:23.264056 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4151 2022-08-03 00:35:22.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      504 2022-08-03 00:35:23.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-03 00:35:22.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-08-03 00:35:23.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       24 2022-08-03 00:35:23.000000 cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     4151 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3174 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1847 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 00:33:28.170920 cdk-certbot-dns-route53-2.1.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/
+-rw-r--r--   0 runner    (1001) docker     (121)    19910 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25977 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/_jsii/cdk-certbot-dns-route53@2.1.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-04 00:33:13.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 00:33:28.174920 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4151 2022-08-04 00:33:27.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      504 2022-08-04 00:33:28.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-04 00:33:27.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-08-04 00:33:27.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       24 2022-08-04 00:33:28.000000 cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/top_level.txt
```

### Comparing `cdk-certbot-dns-route53-2.1.98/LICENSE` & `cdk-certbot-dns-route53-2.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-certbot-dns-route53-2.1.98/PKG-INFO` & `cdk-certbot-dns-route53-2.1.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-certbot-dns-route53
-Version: 2.1.98
+Version: 2.1.99
 Summary: Create Cron Job Via Lambda, to update certificate and put it to S3 Bucket.
 Home-page: https://github.com/neilkuan/cdk-certbot-dns-route53.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-certbot-dns-route53.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-certbot-dns-route53-2.1.98/README.md` & `cdk-certbot-dns-route53-2.1.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-certbot-dns-route53-2.1.98/setup.py` & `cdk-certbot-dns-route53-2.1.99/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-certbot-dns-route53",
-    "version": "2.1.98",
+    "version": "2.1.99",
     "description": "Create Cron Job Via Lambda, to update certificate and put it to S3 Bucket.",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-certbot-dns-route53.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_certbot_dns_route53",
         "cdk_certbot_dns_route53._jsii"
     ],
     "package_data": {
         "cdk_certbot_dns_route53._jsii": [
-            "cdk-certbot-dns-route53@2.1.98.jsii.tgz"
+            "cdk-certbot-dns-route53@2.1.99.jsii.tgz"
         ],
         "cdk_certbot_dns_route53": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53/__init__.py` & `cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-certbot-dns-route53-2.1.98/src/cdk_certbot_dns_route53.egg-info/PKG-INFO` & `cdk-certbot-dns-route53-2.1.99/src/cdk_certbot_dns_route53.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-certbot-dns-route53
-Version: 2.1.98
+Version: 2.1.99
 Summary: Create Cron Job Via Lambda, to update certificate and put it to S3 Bucket.
 Home-page: https://github.com/neilkuan/cdk-certbot-dns-route53.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-certbot-dns-route53.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

