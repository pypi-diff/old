# Comparing `tmp/boto3-1.9.98.tar.gz` & `tmp/boto3-1.9.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/boto3-1.9.98.tar", last modified: Tue Feb 19 19:05:47 2019, max compression
+gzip compressed data, was "dist/boto3-1.9.99.tar", last modified: Wed Feb 20 19:05:53 2019, max compression
```

## Comparing `boto3-1.9.98.tar` & `boto3-1.9.99.tar`

### file list

```diff
@@ -1,101 +1,101 @@
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/ec2/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1163 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/ec2/deletetags.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1576 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/ec2/createtags.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/ec2/__init__.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/docs/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2625 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/docstring.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2768 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/method.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10988 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/resource.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6170 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/action.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2217 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/attr.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4620 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/subresource.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4046 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/waiter.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9721 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/collection.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5710 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5479 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/service.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1529 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1330 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/base.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1064 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/docs/client.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/resources/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    20675 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/model.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9500 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/action.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    22401 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/factory.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19049 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/collection.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11569 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/response.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6132 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/params.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5054 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/resources/base.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/dynamodb/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12332 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/dynamodb/transform.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6293 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/dynamodb/table.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9640 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/dynamodb/types.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14875 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/dynamodb/conditions.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/dynamodb/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3993 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/exceptions.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/s3/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26176 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/s3/inject.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12812 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/s3/transfer.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/s3/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3095 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/utils.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19614 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/session.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2015-03-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2015-03-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2016-11-15/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76922 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2016-11-15/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2015-10-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2015-10-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2016-09-15/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2016-09-15/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2016-04-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2016-04-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2015-04-15/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2015-04-15/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/ec2/2014-10-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/ec2/2014-10-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/cloudformation/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/cloudformation/2010-05-15/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5110 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/cloudformation/2010-05-15/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/cloudwatch/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/cloudwatch/2010-08-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11690 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/cloudwatch/2010-08-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/dynamodb/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/dynamodb/2012-08-10/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3849 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/dynamodb/2012-08-10/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/s3/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/s3/2006-03-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    37204 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/s3/2006-03-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/opsworks/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/opsworks/2013-02-18/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4136 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/opsworks/2013-02-18/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/glacier/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/glacier/2012-06-01/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19940 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/glacier/2012-06-01/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/sns/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/sns/2010-03-31/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9091 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/sns/2010-03-31/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/iam/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/iam/2010-05-08/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    50357 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/iam/2010-05-08/resources-1.json
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/sqs/
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/data/sqs/2012-11-05/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6545 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/data/sqs/2012-11-05/resources-1.json
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1490 2019-02-19 19:05:46.000000 boto3-1.9.98/boto3/compat.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3339 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3/__init__.py
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1637 2019-02-19 19:05:47.000000 boto3-1.9.98/setup.py
-drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)       74 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/requires.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5646 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/PKG-INFO
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        1 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/dependency_links.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1794 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/SOURCES.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        6 2019-02-19 19:05:47.000000 boto3-1.9.98/boto3.egg-info/top_level.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      549 2019-02-19 19:05:46.000000 boto3-1.9.98/LICENSE
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      261 2019-02-19 19:05:46.000000 boto3-1.9.98/requirements.txt
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      121 2019-02-19 19:05:46.000000 boto3-1.9.98/MANIFEST.in
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5646 2019-02-19 19:05:47.000000 boto3-1.9.98/PKG-INFO
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      173 2019-02-19 19:05:47.000000 boto3-1.9.98/setup.cfg
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3769 2019-02-19 19:05:46.000000 boto3-1.9.98/README.rst
--rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1360 2019-02-19 19:05:46.000000 boto3-1.9.98/CONTRIBUTING.rst
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/ec2/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1163 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/ec2/deletetags.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1576 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/ec2/createtags.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/ec2/__init__.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/docs/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2625 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/docstring.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2768 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/method.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    10988 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/resource.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6170 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/action.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     2217 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/attr.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4620 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/subresource.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4046 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/waiter.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9721 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/collection.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5710 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5479 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/service.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1529 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1330 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/base.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1064 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/docs/client.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/resources/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    20675 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/model.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9500 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/action.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    22401 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/factory.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19049 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/collection.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11569 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/response.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6132 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/params.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5054 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/resources/base.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/dynamodb/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12332 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/dynamodb/transform.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6293 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/dynamodb/table.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9640 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/dynamodb/types.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    14875 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/dynamodb/conditions.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/dynamodb/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3993 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/exceptions.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/s3/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    26176 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/s3/inject.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    12812 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/s3/transfer.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      561 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/s3/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3095 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/utils.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19614 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/session.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2015-03-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2015-03-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2016-11-15/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76922 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2016-11-15/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2015-10-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2015-10-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2016-09-15/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2016-09-15/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2016-04-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    76564 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2016-04-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2015-04-15/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2015-04-15/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/ec2/2014-10-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    68469 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/ec2/2014-10-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/cloudformation/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/cloudformation/2010-05-15/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5110 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/cloudformation/2010-05-15/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/cloudwatch/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/cloudwatch/2010-08-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    11690 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/cloudwatch/2010-08-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/dynamodb/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/dynamodb/2012-08-10/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3849 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/dynamodb/2012-08-10/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/s3/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/s3/2006-03-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    37204 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/s3/2006-03-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/opsworks/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/opsworks/2013-02-18/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     4136 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/opsworks/2013-02-18/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/glacier/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/glacier/2012-06-01/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    19940 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/glacier/2012-06-01/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/sns/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/sns/2010-03-31/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     9091 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/sns/2010-03-31/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/iam/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/iam/2010-05-08/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)    50357 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/iam/2010-05-08/resources-1.json
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/sqs/
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/data/sqs/2012-11-05/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     6545 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/data/sqs/2012-11-05/resources-1.json
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1490 2019-02-20 19:05:52.000000 boto3-1.9.99/boto3/compat.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3339 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3/__init__.py
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1637 2019-02-20 19:05:53.000000 boto3-1.9.99/setup.py
+drwxrwxrwx   0 pysdk-ci (1230230) amazon     (100)        0 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)       74 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/requires.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5646 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/PKG-INFO
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        1 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/dependency_links.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1794 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/SOURCES.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)        6 2019-02-20 19:05:53.000000 boto3-1.9.99/boto3.egg-info/top_level.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      549 2019-02-20 19:05:52.000000 boto3-1.9.99/LICENSE
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      261 2019-02-20 19:05:52.000000 boto3-1.9.99/requirements.txt
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      121 2019-02-20 19:05:52.000000 boto3-1.9.99/MANIFEST.in
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     5646 2019-02-20 19:05:53.000000 boto3-1.9.99/PKG-INFO
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)      173 2019-02-20 19:05:53.000000 boto3-1.9.99/setup.cfg
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     3769 2019-02-20 19:05:52.000000 boto3-1.9.99/README.rst
+-rw-rw-rw-   0 pysdk-ci (1230230) amazon     (100)     1360 2019-02-20 19:05:52.000000 boto3-1.9.99/CONTRIBUTING.rst
```

### Comparing `boto3-1.9.98/boto3/ec2/deletetags.py` & `boto3-1.9.99/boto3/ec2/deletetags.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/ec2/createtags.py` & `boto3-1.9.99/boto3/ec2/createtags.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/ec2/__init__.py` & `boto3-1.9.99/boto3/ec2/__init__.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/docstring.py` & `boto3-1.9.99/boto3/docs/docstring.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/method.py` & `boto3-1.9.99/boto3/docs/method.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/resource.py` & `boto3-1.9.99/boto3/docs/resource.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/action.py` & `boto3-1.9.99/boto3/docs/action.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/attr.py` & `boto3-1.9.99/boto3/docs/attr.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/subresource.py` & `boto3-1.9.99/boto3/docs/subresource.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/waiter.py` & `boto3-1.9.99/boto3/docs/waiter.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/collection.py` & `boto3-1.9.99/boto3/docs/collection.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/utils.py` & `boto3-1.9.99/boto3/docs/utils.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/service.py` & `boto3-1.9.99/boto3/docs/service.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/__init__.py` & `boto3-1.9.99/boto3/docs/__init__.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/base.py` & `boto3-1.9.99/boto3/docs/base.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/docs/client.py` & `boto3-1.9.99/boto3/docs/client.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/model.py` & `boto3-1.9.99/boto3/resources/model.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/action.py` & `boto3-1.9.99/boto3/resources/action.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/factory.py` & `boto3-1.9.99/boto3/resources/factory.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/collection.py` & `boto3-1.9.99/boto3/resources/collection.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/response.py` & `boto3-1.9.99/boto3/resources/response.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/params.py` & `boto3-1.9.99/boto3/resources/params.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/resources/base.py` & `boto3-1.9.99/boto3/resources/base.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/dynamodb/transform.py` & `boto3-1.9.99/boto3/dynamodb/transform.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/dynamodb/table.py` & `boto3-1.9.99/boto3/dynamodb/table.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/dynamodb/types.py` & `boto3-1.9.99/boto3/dynamodb/types.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/dynamodb/conditions.py` & `boto3-1.9.99/boto3/dynamodb/conditions.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/dynamodb/__init__.py` & `boto3-1.9.99/boto3/dynamodb/__init__.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/exceptions.py` & `boto3-1.9.99/boto3/exceptions.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/s3/inject.py` & `boto3-1.9.99/boto3/s3/inject.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/s3/transfer.py` & `boto3-1.9.99/boto3/s3/transfer.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/s3/__init__.py` & `boto3-1.9.99/boto3/s3/__init__.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/utils.py` & `boto3-1.9.99/boto3/utils.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/session.py` & `boto3-1.9.99/boto3/session.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2015-03-01/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2015-03-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2016-11-15/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2016-11-15/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2015-10-01/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2015-10-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2016-09-15/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2016-09-15/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2016-04-01/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2016-04-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2015-04-15/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2015-04-15/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/ec2/2014-10-01/resources-1.json` & `boto3-1.9.99/boto3/data/ec2/2014-10-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/cloudformation/2010-05-15/resources-1.json` & `boto3-1.9.99/boto3/data/cloudformation/2010-05-15/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/cloudwatch/2010-08-01/resources-1.json` & `boto3-1.9.99/boto3/data/cloudwatch/2010-08-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/dynamodb/2012-08-10/resources-1.json` & `boto3-1.9.99/boto3/data/dynamodb/2012-08-10/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/s3/2006-03-01/resources-1.json` & `boto3-1.9.99/boto3/data/s3/2006-03-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/opsworks/2013-02-18/resources-1.json` & `boto3-1.9.99/boto3/data/opsworks/2013-02-18/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/glacier/2012-06-01/resources-1.json` & `boto3-1.9.99/boto3/data/glacier/2012-06-01/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/sns/2010-03-31/resources-1.json` & `boto3-1.9.99/boto3/data/sns/2010-03-31/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/iam/2010-05-08/resources-1.json` & `boto3-1.9.99/boto3/data/iam/2010-05-08/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/data/sqs/2012-11-05/resources-1.json` & `boto3-1.9.99/boto3/data/sqs/2012-11-05/resources-1.json`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/compat.py` & `boto3-1.9.99/boto3/compat.py`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/boto3/__init__.py` & `boto3-1.9.99/boto3/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 
 import logging
 
 from boto3.session import Session
 
 
 __author__ = 'Amazon Web Services'
-__version__ = '1.9.98'
+__version__ = '1.9.99'
 
 
 # The default Boto3 session; autoloaded when needed.
 DEFAULT_SESSION = None
 
 
 def setup_default_session(**kwargs):
```

### Comparing `boto3-1.9.98/setup.py` & `boto3-1.9.99/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 
 
 ROOT = os.path.dirname(__file__)
 VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
 
 
 requires = [
-    'botocore>=1.12.98,<1.13.0',
+    'botocore>=1.12.99,<1.13.0',
     'jmespath>=0.7.1,<1.0.0',
     's3transfer>=0.2.0,<0.3.0'
 ]
 
 
 def get_version():
     init = open(os.path.join(ROOT, 'boto3', '__init__.py')).read()
```

### Comparing `boto3-1.9.98/boto3.egg-info/PKG-INFO` & `boto3-1.9.99/boto3.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: boto3
-Version: 1.9.98
+Version: 1.9.99
 Summary: The AWS SDK for Python
 Home-page: https://github.com/boto/boto3
 Author: Amazon Web Services
 Author-email: UNKNOWN
 License: Apache License 2.0
 Description: ===============================
         Boto 3 - The AWS SDK for Python
```

### Comparing `boto3-1.9.98/boto3.egg-info/SOURCES.txt` & `boto3-1.9.99/boto3.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/LICENSE` & `boto3-1.9.99/LICENSE`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/PKG-INFO` & `boto3-1.9.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: boto3
-Version: 1.9.98
+Version: 1.9.99
 Summary: The AWS SDK for Python
 Home-page: https://github.com/boto/boto3
 Author: Amazon Web Services
 Author-email: UNKNOWN
 License: Apache License 2.0
 Description: ===============================
         Boto 3 - The AWS SDK for Python
```

### Comparing `boto3-1.9.98/README.rst` & `boto3-1.9.99/README.rst`

 * *Files identical despite different names*

### Comparing `boto3-1.9.98/CONTRIBUTING.rst` & `boto3-1.9.99/CONTRIBUTING.rst`

 * *Files identical despite different names*

