# Comparing `tmp/django-iris-0.2.1b1.tar.gz` & `tmp/django-iris-0.2.1b2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-iris-0.2.1b1.tar", last modified: Thu Apr  6 12:57:58 2023, max compression
+gzip compressed data, was "django-iris-0.2.1b2.tar", last modified: Thu Apr  6 13:13:58 2023, max compression
```

## Comparing `django-iris-0.2.1b1.tar` & `django-iris-0.2.1b2.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:57:57.996337 django-iris-0.2.1b1/
--rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 12:57:57.996337 django-iris-0.2.1b1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:57:57.992337 django-iris-0.2.1b1/django_iris/
--rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7038 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7738 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/compiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/creation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/features.py
--rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/introspection.py
--rw-r--r--   0 runner    (1001) docker     (123)    13175 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/operations.py
--rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/django_iris/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:57:57.992337 django-iris-0.2.1b1/django_iris.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/django_iris.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1662 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/django_iris.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/django_iris.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/django_iris.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:57:57.996337 django-iris-0.2.1b1/intersystems_iris/
--rw-rw-rw-   0 runner    (1001) docker     (123)      299 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_BufferReader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1337 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_BufferWriter.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1896 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_ConnectionInformation.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      578 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_ConnectionParameters.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1483 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_Constant.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    20104 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_DBList.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2311 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_Device.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      618 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_GatewayContext.py
--rw-rw-rw-   0 runner    (1001) docker     (123)       96 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_GatewayException.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2735 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_GatewayUtility.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    49548 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRIS.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    21467 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISConnection.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2614 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISEmbedded.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    12049 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISGlobalNode.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      797 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISGlobalNodeView.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6906 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISIterator.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    10247 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISList.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6756 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISNative.py
--rw-rw-rw-   0 runner    (1001) docker     (123)       82 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISOREF.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    14456 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISObject.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4905 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_IRISReference.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6643 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_InStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4130 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_LegacyIterator.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      354 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_ListItem.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2966 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_ListReader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     5515 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_ListWriter.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     3797 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_LogFileStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1662 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_MessageHeader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1327 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_OutStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1963 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_PrintStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    41638 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_PythonGateway.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4330 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/_SharedMemorySocket.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1773 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/__init__.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      218 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/intersystems_iris/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:57:57.996337 django-iris-0.2.1b1/irisnative/
--rw-rw-rw-   0 runner    (1001) docker     (123)      665 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/irisnative/_IRISNative.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      341 2023-04-06 12:57:57.000000 django-iris-0.2.1b1/irisnative/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      927 2023-04-06 12:57:57.996337 django-iris-0.2.1b1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      541 2023-04-06 12:57:42.000000 django-iris-0.2.1b1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.194345 django-iris-0.2.1b2/django_iris/
+-rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7093 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7738 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/creation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/cursor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/introspection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13175 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/operations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.194345 django-iris-0.2.1b2/django_iris.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1662 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/intersystems_iris/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      299 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_BufferReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1337 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_BufferWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1896 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ConnectionInformation.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      578 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ConnectionParameters.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1483 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_Constant.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    20104 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_DBList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2311 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_Device.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      618 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayContext.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       96 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayException.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2735 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayUtility.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    49548 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRIS.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    21467 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISConnection.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2614 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISEmbedded.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    12049 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNode.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      797 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNodeView.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6906 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    10247 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6756 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       82 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISOREF.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    14456 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISObject.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4905 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISReference.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6643 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_InStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4130 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_LegacyIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      354 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListItem.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2966 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5515 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     3797 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_LogFileStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1662 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_MessageHeader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1327 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_OutStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1963 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_PrintStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    41638 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_PythonGateway.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4330 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_SharedMemorySocket.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1773 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/__init__.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      218 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/irisnative/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      665 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/irisnative/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      341 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/irisnative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      927 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/setup.py
```

### Comparing `django-iris-0.2.1b1/LICENSE` & `django-iris-0.2.1b2/LICENSE`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/PKG-INFO` & `django-iris-0.2.1b2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.2.1b1
+Version: 0.2.1b2
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
```

### Comparing `django-iris-0.2.1b1/README.md` & `django-iris-0.2.1b2/README.md`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/__init__.py` & `django-iris-0.2.1b2/django_iris/__init__.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/base.py` & `django-iris-0.2.1b2/django_iris/base.py`

 * *Files 1% similar despite different names*

```diff
@@ -158,14 +158,17 @@
                 "Please supply the USER and PASSWORD"
             )
 
         conn_params['application_name'] = 'django'
         conn_params["autoCommit"] = self.autocommit
         return conn_params
 
+    def init_connection_state(self):
+        pass
+    
     @async_unsafe
     def get_new_connection(self, conn_params):
         return Database.connect(**conn_params)
 
     def _close(self):
         if self.connection is not None:
             # Automatically rollbacks anyway
```

### Comparing `django-iris-0.2.1b1/django_iris/compiler.py` & `django-iris-0.2.1b2/django_iris/compiler.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/creation.py` & `django-iris-0.2.1b2/django_iris/creation.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/cursor.py` & `django-iris-0.2.1b2/django_iris/cursor.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/features.py` & `django-iris-0.2.1b2/django_iris/features.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/introspection.py` & `django-iris-0.2.1b2/django_iris/introspection.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/operations.py` & `django-iris-0.2.1b2/django_iris/operations.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/schema.py` & `django-iris-0.2.1b2/django_iris/schema.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris/utils.py` & `django-iris-0.2.1b2/django_iris/utils.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/django_iris.egg-info/PKG-INFO` & `django-iris-0.2.1b2/django_iris.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.2.1b1
+Version: 0.2.1b2
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
```

### Comparing `django-iris-0.2.1b1/django_iris.egg-info/SOURCES.txt` & `django-iris-0.2.1b2/django_iris.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_BufferWriter.py` & `django-iris-0.2.1b2/intersystems_iris/_BufferWriter.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_ConnectionInformation.py` & `django-iris-0.2.1b2/intersystems_iris/_ConnectionInformation.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_ConnectionParameters.py` & `django-iris-0.2.1b2/intersystems_iris/_ConnectionParameters.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_Constant.py` & `django-iris-0.2.1b2/intersystems_iris/_Constant.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_DBList.py` & `django-iris-0.2.1b2/intersystems_iris/_DBList.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_Device.py` & `django-iris-0.2.1b2/intersystems_iris/_Device.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_GatewayContext.py` & `django-iris-0.2.1b2/intersystems_iris/_GatewayContext.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_GatewayUtility.py` & `django-iris-0.2.1b2/intersystems_iris/_GatewayUtility.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRIS.py` & `django-iris-0.2.1b2/intersystems_iris/_IRIS.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISConnection.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISConnection.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISEmbedded.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISEmbedded.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISGlobalNode.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNode.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISGlobalNodeView.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNodeView.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISIterator.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISIterator.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISList.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISList.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISNative.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISNative.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISObject.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISObject.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_IRISReference.py` & `django-iris-0.2.1b2/intersystems_iris/_IRISReference.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_InStream.py` & `django-iris-0.2.1b2/intersystems_iris/_InStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_LegacyIterator.py` & `django-iris-0.2.1b2/intersystems_iris/_LegacyIterator.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_ListReader.py` & `django-iris-0.2.1b2/intersystems_iris/_ListReader.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_ListWriter.py` & `django-iris-0.2.1b2/intersystems_iris/_ListWriter.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_LogFileStream.py` & `django-iris-0.2.1b2/intersystems_iris/_LogFileStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_MessageHeader.py` & `django-iris-0.2.1b2/intersystems_iris/_MessageHeader.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_OutStream.py` & `django-iris-0.2.1b2/intersystems_iris/_OutStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_PrintStream.py` & `django-iris-0.2.1b2/intersystems_iris/_PrintStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_PythonGateway.py` & `django-iris-0.2.1b2/intersystems_iris/_PythonGateway.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/_SharedMemorySocket.py` & `django-iris-0.2.1b2/intersystems_iris/_SharedMemorySocket.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/intersystems_iris/__init__.py` & `django-iris-0.2.1b2/intersystems_iris/__init__.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/irisnative/_IRISNative.py` & `django-iris-0.2.1b2/irisnative/_IRISNative.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b1/setup.cfg` & `django-iris-0.2.1b2/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = django-iris
-version = 0.2.1b1
+version = 0.2.1b2
 url = https://github.com/caretdev/django-iris
 maintainer = CaretDev
 maintainer_email = dmitry@caretdev.com
 license = MIT
 description = Django backend for InterSystems IRIS
 long_description = file: README.md
 long_description_content_type = text/markdown
```

### Comparing `django-iris-0.2.1b1/setup.py` & `django-iris-0.2.1b2/setup.py`

 * *Files identical despite different names*

