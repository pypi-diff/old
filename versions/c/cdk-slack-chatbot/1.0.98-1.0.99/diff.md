# Comparing `tmp/cdk-slack-chatbot-1.0.98.tar.gz` & `tmp/cdk-slack-chatbot-1.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-slack-chatbot-1.0.98.tar", last modified: Fri Feb 17 00:56:18 2023, max compression
+gzip compressed data, was "cdk-slack-chatbot-1.0.99.tar", last modified: Sat Feb 18 00:53:56 2023, max compression
```

## Comparing `cdk-slack-chatbot-1.0.98.tar` & `cdk-slack-chatbot-1.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2950 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-17 00:56:18.250418 cdk-slack-chatbot-1.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/
--rw-r--r--   0 runner    (1001) docker     (123)     8168 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16977 2023-02-17 00:56:00.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/_jsii/cdk-slack-chatbot@1.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-17 00:56:01.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-17 00:56:18.254418 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2950 2023-02-17 00:56:18.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      444 2023-02-17 00:56:18.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-17 00:56:18.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-02-17 00:56:18.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-02-17 00:56:18.000000 cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2950 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/
+-rw-r--r--   0 runner    (1001) docker     (123)     8168 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17065 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/_jsii/cdk-slack-chatbot@1.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-18 00:53:44.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-18 00:53:56.406924 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2950 2023-02-18 00:53:56.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      444 2023-02-18 00:53:56.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-18 00:53:56.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-02-18 00:53:56.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-02-18 00:53:56.000000 cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/top_level.txt
```

### Comparing `cdk-slack-chatbot-1.0.98/LICENSE` & `cdk-slack-chatbot-1.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-slack-chatbot-1.0.98/PKG-INFO` & `cdk-slack-chatbot-1.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-slack-chatbot
-Version: 1.0.98
+Version: 1.0.99
 Summary: cdk-slack-chatbot
 Home-page: https://github.com/lvthillo/cdk-slack-chatbot.git
 Author: Lorenz Vanthillo<lorenz.vanthillo@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/lvthillo/cdk-slack-chatbot.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdk-slack-chatbot-1.0.98/README.md` & `cdk-slack-chatbot-1.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-slack-chatbot-1.0.98/setup.py` & `cdk-slack-chatbot-1.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-slack-chatbot",
-    "version": "1.0.98",
+    "version": "1.0.99",
     "description": "cdk-slack-chatbot",
     "license": "Apache-2.0",
     "url": "https://github.com/lvthillo/cdk-slack-chatbot.git",
     "long_description_content_type": "text/markdown",
     "author": "Lorenz Vanthillo<lorenz.vanthillo@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_slack_chatbot",
         "cdk_slack_chatbot._jsii"
     ],
     "package_data": {
         "cdk_slack_chatbot._jsii": [
-            "cdk-slack-chatbot@1.0.98.jsii.tgz"
+            "cdk-slack-chatbot@1.0.99.jsii.tgz"
         ],
         "cdk_slack_chatbot": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot/__init__.py` & `cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-slack-chatbot-1.0.98/src/cdk_slack_chatbot.egg-info/PKG-INFO` & `cdk-slack-chatbot-1.0.99/src/cdk_slack_chatbot.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-slack-chatbot
-Version: 1.0.98
+Version: 1.0.99
 Summary: cdk-slack-chatbot
 Home-page: https://github.com/lvthillo/cdk-slack-chatbot.git
 Author: Lorenz Vanthillo<lorenz.vanthillo@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/lvthillo/cdk-slack-chatbot.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

