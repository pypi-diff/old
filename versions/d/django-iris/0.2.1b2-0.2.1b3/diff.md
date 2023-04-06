# Comparing `tmp/django-iris-0.2.1b2.tar.gz` & `tmp/django-iris-0.2.1b3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-iris-0.2.1b2.tar", last modified: Thu Apr  6 13:13:58 2023, max compression
+gzip compressed data, was "django-iris-0.2.1b3.tar", last modified: Thu Apr  6 13:29:44 2023, max compression
```

## Comparing `django-iris-0.2.1b2.tar` & `django-iris-0.2.1b3.tar`

### file list

```diff
@@ -1,61 +1,93 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/
--rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.194345 django-iris-0.2.1b2/django_iris/
--rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7093 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7738 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/compiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/creation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/features.py
--rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/introspection.py
--rw-r--r--   0 runner    (1001) docker     (123)    13175 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/operations.py
--rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/django_iris/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.194345 django-iris-0.2.1b2/django_iris.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1662 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 13:13:58.000000 django-iris-0.2.1b2/django_iris.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/intersystems_iris/
--rw-rw-rw-   0 runner    (1001) docker     (123)      299 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_BufferReader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1337 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_BufferWriter.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1896 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ConnectionInformation.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      578 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ConnectionParameters.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1483 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_Constant.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    20104 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_DBList.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2311 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_Device.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      618 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayContext.py
--rw-rw-rw-   0 runner    (1001) docker     (123)       96 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayException.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2735 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_GatewayUtility.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    49548 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRIS.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    21467 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISConnection.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2614 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISEmbedded.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    12049 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNode.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      797 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNodeView.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6906 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISIterator.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    10247 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISList.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6756 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISNative.py
--rw-rw-rw-   0 runner    (1001) docker     (123)       82 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISOREF.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    14456 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISObject.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4905 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_IRISReference.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     6643 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_InStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4130 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_LegacyIterator.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      354 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListItem.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     2966 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListReader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     5515 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_ListWriter.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     3797 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_LogFileStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1662 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_MessageHeader.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1327 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_OutStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1963 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_PrintStream.py
--rw-rw-rw-   0 runner    (1001) docker     (123)    41638 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_PythonGateway.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     4330 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/_SharedMemorySocket.py
--rw-rw-rw-   0 runner    (1001) docker     (123)     1773 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/__init__.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      218 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/intersystems_iris/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/irisnative/
--rw-rw-rw-   0 runner    (1001) docker     (123)      665 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/irisnative/_IRISNative.py
--rw-rw-rw-   0 runner    (1001) docker     (123)      341 2023-04-06 13:13:57.000000 django-iris-0.2.1b2/irisnative/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      927 2023-04-06 13:13:58.202345 django-iris-0.2.1b2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      541 2023-04-06 13:13:39.000000 django-iris-0.2.1b2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.993900 django-iris-0.2.1b3/django_iris/
+-rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7093 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7738 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/creation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/cursor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/introspection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13175 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/operations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/django_iris/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.993900 django-iris-0.2.1b3/django_iris.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/django_iris.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2847 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/django_iris.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/django_iris.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/django_iris.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.997900 django-iris-0.2.1b3/intersystems_iris/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      299 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_BufferReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1337 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_BufferWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1896 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_ConnectionInformation.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      578 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_ConnectionParameters.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1483 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_Constant.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    20104 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_DBList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2311 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_Device.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      618 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_GatewayContext.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       96 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_GatewayException.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2735 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_GatewayUtility.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    49548 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRIS.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    21467 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISConnection.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2614 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISEmbedded.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    12049 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISGlobalNode.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      797 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISGlobalNodeView.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6906 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    10247 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6756 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       82 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISOREF.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    14456 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISObject.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4905 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_IRISReference.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6643 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_InStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4130 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_LegacyIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      354 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_ListItem.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2966 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_ListReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5515 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_ListWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     3797 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_LogFileStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1662 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_MessageHeader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1327 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_OutStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1963 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_PrintStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    41638 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_PythonGateway.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4330 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/_SharedMemorySocket.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1773 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/__init__.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      218 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.997900 django-iris-0.2.1b3/intersystems_iris/dbapi/
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2535 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_Column.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    94963 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_DBAPI.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1391 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_Descriptor.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2113 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_IRISStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4076 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_Message.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4776 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_Parameter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5151 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_ParameterCollection.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    12810 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_ResultSetRow.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      557 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/_SQLType.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/
+-rw-rw-rw-   0 runner    (1001) docker     (123)    78588 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/_PreParser.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    16163 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/_Scanner.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2304 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/_Token.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6770 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/_TokenList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/dbapi/preparser/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/intersystems_iris/pex/
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4370 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_BusinessHost.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5241 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_BusinessOperation.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    10774 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_BusinessProcess.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5441 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_BusinessService.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    10509 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_Common.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1203 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_Director.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      172 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_IRISBusinessOperation.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      585 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_IRISBusinessService.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      171 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_IRISInboundAdapter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      522 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_IRISOutboundAdapter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2296 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_InboundAdapter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      320 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_Message.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1628 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/_OutboundAdapter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1379 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/intersystems_iris/pex/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/irisnative/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      665 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/irisnative/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      341 2023-04-06 13:29:43.000000 django-iris-0.2.1b3/irisnative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-04-06 13:29:44.001900 django-iris-0.2.1b3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-04-06 13:29:26.000000 django-iris-0.2.1b3/setup.py
```

### Comparing `django-iris-0.2.1b2/LICENSE` & `django-iris-0.2.1b3/LICENSE`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/PKG-INFO` & `django-iris-0.2.1b3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.2.1b2
+Version: 0.2.1b3
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
```

### Comparing `django-iris-0.2.1b2/README.md` & `django-iris-0.2.1b3/README.md`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/__init__.py` & `django-iris-0.2.1b3/django_iris/__init__.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/base.py` & `django-iris-0.2.1b3/django_iris/base.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/compiler.py` & `django-iris-0.2.1b3/django_iris/compiler.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/creation.py` & `django-iris-0.2.1b3/django_iris/creation.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/cursor.py` & `django-iris-0.2.1b3/django_iris/cursor.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/features.py` & `django-iris-0.2.1b3/django_iris/features.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/introspection.py` & `django-iris-0.2.1b3/django_iris/introspection.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/operations.py` & `django-iris-0.2.1b3/django_iris/operations.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/schema.py` & `django-iris-0.2.1b3/django_iris/schema.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris/utils.py` & `django-iris-0.2.1b3/django_iris/utils.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/django_iris.egg-info/PKG-INFO` & `django-iris-0.2.1b3/django_iris.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.2.1b2
+Version: 0.2.1b3
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
```

### Comparing `django-iris-0.2.1b2/intersystems_iris/_BufferWriter.py` & `django-iris-0.2.1b3/intersystems_iris/_BufferWriter.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_ConnectionInformation.py` & `django-iris-0.2.1b3/intersystems_iris/_ConnectionInformation.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_ConnectionParameters.py` & `django-iris-0.2.1b3/intersystems_iris/_ConnectionParameters.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_Constant.py` & `django-iris-0.2.1b3/intersystems_iris/_Constant.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_DBList.py` & `django-iris-0.2.1b3/intersystems_iris/_DBList.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_Device.py` & `django-iris-0.2.1b3/intersystems_iris/_Device.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_GatewayContext.py` & `django-iris-0.2.1b3/intersystems_iris/_GatewayContext.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_GatewayUtility.py` & `django-iris-0.2.1b3/intersystems_iris/_GatewayUtility.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRIS.py` & `django-iris-0.2.1b3/intersystems_iris/_IRIS.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISConnection.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISConnection.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISEmbedded.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISEmbedded.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNode.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISGlobalNode.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISGlobalNodeView.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISGlobalNodeView.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISIterator.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISIterator.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISList.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISList.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISNative.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISNative.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISObject.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISObject.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_IRISReference.py` & `django-iris-0.2.1b3/intersystems_iris/_IRISReference.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_InStream.py` & `django-iris-0.2.1b3/intersystems_iris/_InStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_LegacyIterator.py` & `django-iris-0.2.1b3/intersystems_iris/_LegacyIterator.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_ListReader.py` & `django-iris-0.2.1b3/intersystems_iris/_ListReader.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_ListWriter.py` & `django-iris-0.2.1b3/intersystems_iris/_ListWriter.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_LogFileStream.py` & `django-iris-0.2.1b3/intersystems_iris/_LogFileStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_MessageHeader.py` & `django-iris-0.2.1b3/intersystems_iris/_MessageHeader.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_OutStream.py` & `django-iris-0.2.1b3/intersystems_iris/_OutStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_PrintStream.py` & `django-iris-0.2.1b3/intersystems_iris/_PrintStream.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_PythonGateway.py` & `django-iris-0.2.1b3/intersystems_iris/_PythonGateway.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/_SharedMemorySocket.py` & `django-iris-0.2.1b3/intersystems_iris/_SharedMemorySocket.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/intersystems_iris/__init__.py` & `django-iris-0.2.1b3/intersystems_iris/__init__.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/irisnative/_IRISNative.py` & `django-iris-0.2.1b3/irisnative/_IRISNative.py`

 * *Files identical despite different names*

### Comparing `django-iris-0.2.1b2/setup.cfg` & `django-iris-0.2.1b3/setup.cfg`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = django-iris
-version = 0.2.1b2
+version = 0.2.1b3
 url = https://github.com/caretdev/django-iris
 maintainer = CaretDev
 maintainer_email = dmitry@caretdev.com
 license = MIT
 description = Django backend for InterSystems IRIS
 long_description = file: README.md
 long_description_content_type = text/markdown
@@ -20,17 +20,14 @@
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
 project_urls = 
 	Source = https://github.com/caretdev/django-iris
 	Tracker = https://github.com/caretdev/django-iris/issues
 
 [options]
-packages = 
-	django_iris
-	intersystems_iris
-	irisnative
+packages = find:
 python_requires = >=3.8
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `django-iris-0.2.1b2/setup.py` & `django-iris-0.2.1b3/setup.py`

 * *Files identical despite different names*

