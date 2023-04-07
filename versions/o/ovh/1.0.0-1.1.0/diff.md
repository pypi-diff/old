# Comparing `tmp/ovh-1.0.0.tar.gz` & `tmp/ovh-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ovh-1.0.0.tar", last modified: Tue Mar 15 12:13:26 2022, max compression
+gzip compressed data, was "ovh-1.1.0.tar", last modified: Fri Apr  7 09:48:14 2023, max compression
```

## Comparing `ovh-1.0.0.tar` & `ovh-1.1.0.tar`

### file list

```diff
@@ -1,39 +1,40 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.621223 ovh-1.0.0/
--rw-r--r--   0 root         (0) root         (0)     3525 2022-03-15 12:13:08.000000 ovh-1.0.0/CONTRIBUTING.rst
--rw-r--r--   0 root         (0) root         (0)     1468 2022-03-15 12:13:08.000000 ovh-1.0.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)      174 2022-03-15 12:13:08.000000 ovh-1.0.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     4031 2022-03-15 12:13:08.000000 ovh-1.0.0/MIGRATION.rst
--rw-r--r--   0 root         (0) root         (0)    20362 2022-03-15 12:13:26.621223 ovh-1.0.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    19348 2022-03-15 12:13:08.000000 ovh-1.0.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.617223 ovh-1.0.0/docs/
--rw-r--r--   0 root         (0) root         (0)     6778 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/Makefile
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.613222 ovh-1.0.0/docs/api/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.617223 ovh-1.0.0/docs/api/ovh/
--rw-r--r--   0 root         (0) root         (0)     1800 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/api/ovh/client.rst
--rw-r--r--   0 root         (0) root         (0)      411 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/api/ovh/config.rst
--rw-r--r--   0 root         (0) root         (0)      508 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/api/ovh/consumer_key.rst
--rw-r--r--   0 root         (0) root         (0)      595 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/api/ovh/exceptions.rst
--rw-r--r--   0 root         (0) root         (0)     8279 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/conf.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.617223 ovh-1.0.0/docs/img/
--rw-r--r--   0 root         (0) root         (0)    73002 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/img/logo.png
--rw-r--r--   0 root         (0) root         (0)    13434 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/index.rst
--rw-r--r--   0 root         (0) root         (0)     6709 2022-03-15 12:13:08.000000 ovh-1.0.0/docs/make.bat
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.617223 ovh-1.0.0/ovh/
--rw-r--r--   0 root         (0) root         (0)     1942 2022-03-15 12:13:08.000000 ovh-1.0.0/ovh/__init__.py
--rw-r--r--   0 root         (0) root         (0)    21154 2022-03-15 12:13:08.000000 ovh-1.0.0/ovh/client.py
--rw-r--r--   0 root         (0) root         (0)     4570 2022-03-15 12:13:08.000000 ovh-1.0.0/ovh/config.py
--rw-r--r--   0 root         (0) root         (0)     4767 2022-03-15 12:13:08.000000 ovh-1.0.0/ovh/consumer_key.py
--rw-r--r--   0 root         (0) root         (0)     3571 2022-03-15 12:13:08.000000 ovh-1.0.0/ovh/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.621223 ovh-1.0.0/ovh.egg-info/
--rw-r--r--   0 root         (0) root         (0)    20362 2022-03-15 12:13:26.000000 ovh-1.0.0/ovh.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      563 2022-03-15 12:13:26.000000 ovh-1.0.0/ovh.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-03-15 12:13:26.000000 ovh-1.0.0/ovh.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      188 2022-03-15 12:13:26.000000 ovh-1.0.0/ovh.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2022-03-15 12:13:26.000000 ovh-1.0.0/ovh.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1457 2022-03-15 12:13:26.621223 ovh-1.0.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      217 2022-03-15 12:13:08.000000 ovh-1.0.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-15 12:13:26.621223 ovh-1.0.0/tests/
--rw-r--r--   0 root         (0) root         (0)     1535 2022-03-15 12:13:08.000000 ovh-1.0.0/tests/__init__.py
--rw-r--r--   0 root         (0) root         (0)    19189 2022-03-15 12:13:08.000000 ovh-1.0.0/tests/test_client.py
--rw-r--r--   0 root         (0) root         (0)     4873 2022-03-15 12:13:08.000000 ovh-1.0.0/tests/test_config.py
--rw-r--r--   0 root         (0) root         (0)     3683 2022-03-15 12:13:08.000000 ovh-1.0.0/tests/test_consumer_key.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.526301 ovh-1.1.0/
+-rw-r--r--   0 root         (0) root         (0)     3525 2023-04-07 09:47:55.000000 ovh-1.1.0/CONTRIBUTING.rst
+-rw-r--r--   0 root         (0) root         (0)     1468 2023-04-07 09:47:55.000000 ovh-1.1.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)      174 2023-04-07 09:47:55.000000 ovh-1.1.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     4031 2023-04-07 09:47:55.000000 ovh-1.1.0/MIGRATION.rst
+-rw-r--r--   0 root         (0) root         (0)    20912 2023-04-07 09:48:14.526301 ovh-1.1.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    19938 2023-04-07 09:47:55.000000 ovh-1.1.0/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.522301 ovh-1.1.0/docs/
+-rw-r--r--   0 root         (0) root         (0)     6778 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/Makefile
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.518301 ovh-1.1.0/docs/api/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.522301 ovh-1.1.0/docs/api/ovh/
+-rw-r--r--   0 root         (0) root         (0)     1800 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/api/ovh/client.rst
+-rw-r--r--   0 root         (0) root         (0)      411 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/api/ovh/config.rst
+-rw-r--r--   0 root         (0) root         (0)      508 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/api/ovh/consumer_key.rst
+-rw-r--r--   0 root         (0) root         (0)      595 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/api/ovh/exceptions.rst
+-rw-r--r--   0 root         (0) root         (0)     8363 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/conf.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.522301 ovh-1.1.0/docs/img/
+-rw-r--r--   0 root         (0) root         (0)    73002 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/img/logo.png
+-rw-r--r--   0 root         (0) root         (0)    13217 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/index.rst
+-rw-r--r--   0 root         (0) root         (0)     6709 2023-04-07 09:47:55.000000 ovh-1.1.0/docs/make.bat
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.522301 ovh-1.1.0/ovh/
+-rw-r--r--   0 root         (0) root         (0)     1952 2023-04-07 09:47:55.000000 ovh-1.1.0/ovh/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    21281 2023-04-07 09:47:55.000000 ovh-1.1.0/ovh/client.py
+-rw-r--r--   0 root         (0) root         (0)     4399 2023-04-07 09:47:55.000000 ovh-1.1.0/ovh/config.py
+-rw-r--r--   0 root         (0) root         (0)     4736 2023-04-07 09:47:55.000000 ovh-1.1.0/ovh/consumer_key.py
+-rw-r--r--   0 root         (0) root         (0)     3561 2023-04-07 09:47:55.000000 ovh-1.1.0/ovh/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.526301 ovh-1.1.0/ovh.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    20912 2023-04-07 09:48:14.000000 ovh-1.1.0/ovh.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      578 2023-04-07 09:48:14.000000 ovh-1.1.0/ovh.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 09:48:14.000000 ovh-1.1.0/ovh.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      130 2023-04-07 09:48:14.000000 ovh-1.1.0/ovh.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2023-04-07 09:48:14.000000 ovh-1.1.0/ovh.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      356 2023-04-07 09:47:55.000000 ovh-1.1.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     1251 2023-04-07 09:48:14.526301 ovh-1.1.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      218 2023-04-07 09:47:55.000000 ovh-1.1.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 09:48:14.526301 ovh-1.1.0/tests/
+-rw-r--r--   0 root         (0) root         (0)     1507 2023-04-07 09:47:55.000000 ovh-1.1.0/tests/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    13351 2023-04-07 09:47:55.000000 ovh-1.1.0/tests/test_client.py
+-rw-r--r--   0 root         (0) root         (0)     5067 2023-04-07 09:47:55.000000 ovh-1.1.0/tests/test_config.py
+-rw-r--r--   0 root         (0) root         (0)     3695 2023-04-07 09:47:55.000000 ovh-1.1.0/tests/test_consumer_key.py
```

### Comparing `ovh-1.0.0/CONTRIBUTING.rst` & `ovh-1.1.0/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/LICENSE` & `ovh-1.1.0/LICENSE`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-Copyright (c) 2013-2022, OVH SAS.
+Copyright (c) 2013-2023, OVH SAS.
 All rights reserved.
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:
 
   * Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
```

### Comparing `ovh-1.0.0/MIGRATION.rst` & `ovh-1.1.0/MIGRATION.rst`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/PKG-INFO` & `ovh-1.1.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,32 +1,30 @@
 Metadata-Version: 2.1
 Name: ovh
-Version: 1.0.0
+Version: 1.1.0
 Summary: "Official module to perform HTTP requests to the OVHcloud APIs"
 Home-page: https://api.ovh.com
 Author: OVHcloud team - Romain Beuque
 Author-email: api@ml.ovh.net
 License: BSD
 Keywords: ovh,sdk,rest,ovhcloud
-Platform: UNKNOWN
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: Topic :: System :: Archiving :: Packaging
 Provides-Extra: dev
-Provides-Extra: test
 License-File: LICENSE
 
 .. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
            :alt: Python & OVH APIs
            :target: https://pypi.python.org/pypi/ovh
 
 Lightweight wrapper around OVHcloud's APIs. Handles all the hard work including
@@ -40,25 +38,23 @@
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/pyversions/ovh.svg
            :alt: PyPi supported Python versions
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/wheel/ovh.svg
            :alt: PyPi Wheel status
            :target: https://pypi.python.org/pypi/ovh
-.. image:: https://travis-ci.org/ovh/python-ovh.svg?branch=master
+.. image:: https://github.com/ovh/python-ovh/actions/workflows/test.yaml/badge.svg?branch=master
            :alt: Build Status
-           :target: https://travis-ci.org/ovh/python-ovh
+           :target: https://github.com/ovh/python-ovh/actions/workflows/test.yaml
 .. image:: https://coveralls.io/repos/github/ovh/python-ovh/badge.svg
            :alt: Coverage Status
            :target: https://coveralls.io/github/ovh/python-ovh
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
     # to get your credentials
     client = ovh.Client(
         endpoint='ovh-eu',
         application_key='<application key>',
@@ -156,15 +152,14 @@
 behalf, you need a **consumer key (CK)**.
 
 Here is a sample code you can use to allow your application to access a
 customer's information:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
 
     # create a client using configuration
     client = ovh.Client()
 
     # Request RO, /me API access
     ck = client.new_consumer_key_request()
@@ -176,15 +171,14 @@
     print("Please visit %s to authenticate" % validation['validationUrl'])
     input("and press Enter to continue...")
 
     # Print nice welcome message
     print("Welcome", client.get('/me')['firstname'])
     print("Btw, your 'consumerKey' is '%s'" % validation['consumerKey'])
 
-
 Returned ``consumerKey`` should then be kept to avoid re-authenticating your
 end-user on each use.
 
 .. note:: To request full and unlimited access to the API, you may use ``add_recursive_rules``:
 
 .. code:: python
 
@@ -202,16 +196,14 @@
 ``from`` keyword. Which is a problem as this is also a reserved Python keyword.
 In this case, simply prefix it with a '_', the wrapper will automatically detect
 it as being a prefixed reserved keyword and will substitute it. Such aliasing
 is only supported with reserved keywords.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     DOMAIN = "example.com"
     SOURCE = "sales@example.com"
     DESTINATION = "contact@example.com"
 
     # create a client
@@ -233,16 +225,14 @@
 of each bill lines using ``/me/bill/{billId}/details/{billDetailId}``.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # Grab bill list
     bills = client.get('/me/bill')
@@ -263,16 +253,14 @@
 manually for each servers. You could take advantage of a code like this.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # get list of all server names
     servers = client.get('/dedicated/server/')
@@ -294,16 +282,14 @@
 manage revocation too.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
     from tabulate import tabulate
 
     # create a client
     client = ovh.Client()
 
     credentials = client.get('/me/api/credential', status='validated')
@@ -341,15 +327,14 @@
 particularly useful to tweak the BIOS or troubleshoot boot issues.
 
 Hopefully, this can easily be automated using a simple script. It assumes Java Web Start is
 fully installed on the machine and a consumer key allowed on the server exists.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
     import sys
     import time
     import tempfile
     import subprocess
 
     # check arguments
@@ -449,41 +434,63 @@
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client()
 
+Use v1 and v2 API versions
+--------------------------
+
+When using OVHcloud APIs (not So you Start or Kimsufi ones), you are given the
+opportunity to aim for two API versions. For the European API, for example:
+
+- the v1 is reachable through https://eu.api.ovh.com/v1
+- the v2 is reachable through https://eu.api.ovh.com/v2
+- the legacy URL is https://eu.api.ovh.com/1.0
+
+ Calling ``client.get``, you can target the API version you want:
+
+.. code:: python
+
+    client = ovh.Client(endpoint="ovh-eu")
+
+    # Call to https://eu.api.ovh.com/v1/xdsl/xdsl-yourservice
+    client.get("/v1/xdsl/xdsl-yourservice")
+
+    # Call to https://eu.api.ovh.com/v2/xdsl/xdsl-yourservice
+    client.get("/v2/xdsl/xdsl-yourservice")
+
+    # Legacy call to https://eu.api.ovh.com/1.0/xdsl/xdsl-yourservice
+    client.get("/xdsl/xdsl-yourservice")
+
 Custom configuration file
 -------------------------
 
 You can also specify a custom configuration file. With this method, you won't be able to inherit values from environment.
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client(config_file='/my/config.conf')
 
-
 Passing parameters
 ==================
 
 You can call all the methods of the API with the necessary arguments.
 
 If an API needs an argument colliding with a Python reserved keyword, it
 can be prefixed with an underscore. For example, ``from`` argument of
 ``POST /email/domain/{domain}/redirection`` may be replaced by ``_from``.
 
 With characters invalid in python argument name like a dot, you can:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     params = {}
     params['date.from'] = '2014-01-01'
     params['date.to'] = '2015-01-01'
 
     # create a client
@@ -532,29 +539,28 @@
 
 .. code:: bash
 
     git clone https://github.com/ovh/python-ovh.git
     cd python-ovh
     python setup.py develop
 
-You've developed a new cool feature ? Fixed an annoying bug ? We'd be happy
-to hear from you !
+You've developed a new cool feature? Fixed an annoying bug? We'd be happy
+to hear from you!
 
 Run the tests
 -------------
 
-Simply run ``nosetests``. It will automatically load its configuration from
+Simply run ``pytest``. It will automatically load its configuration from
 ``setup.cfg`` and output full coverage status. Since we all love quality, please
 note that we do not accept contributions with test coverage under 100%.
 
 .. code:: bash
 
     pip install -e .[dev]
-    nosetests # 100% coverage is a hard minimum
-
+    pytest
 
 Build the documentation
 -----------------------
 
 Documentation is managed using the excellent ``Sphinx`` system. For example, to
 build HTML documentation:
 
@@ -635,9 +641,7 @@
 - **Report bugs**: https://github.com/ovh/python-ovh/issues
 - **Download**: http://pypi.python.org/pypi/ovh
 
 License
 =======
 
 3-Clause BSD
-
-
```

### Comparing `ovh-1.0.0/README.rst` & `ovh-1.1.0/README.rst`

 * *Files 4% similar despite different names*

```diff
@@ -13,25 +13,23 @@
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/pyversions/ovh.svg
            :alt: PyPi supported Python versions
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/wheel/ovh.svg
            :alt: PyPi Wheel status
            :target: https://pypi.python.org/pypi/ovh
-.. image:: https://travis-ci.org/ovh/python-ovh.svg?branch=master
+.. image:: https://github.com/ovh/python-ovh/actions/workflows/test.yaml/badge.svg?branch=master
            :alt: Build Status
-           :target: https://travis-ci.org/ovh/python-ovh
+           :target: https://github.com/ovh/python-ovh/actions/workflows/test.yaml
 .. image:: https://coveralls.io/repos/github/ovh/python-ovh/badge.svg
            :alt: Coverage Status
            :target: https://coveralls.io/github/ovh/python-ovh
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
     # to get your credentials
     client = ovh.Client(
         endpoint='ovh-eu',
         application_key='<application key>',
@@ -129,15 +127,14 @@
 behalf, you need a **consumer key (CK)**.
 
 Here is a sample code you can use to allow your application to access a
 customer's information:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
 
     # create a client using configuration
     client = ovh.Client()
 
     # Request RO, /me API access
     ck = client.new_consumer_key_request()
@@ -149,15 +146,14 @@
     print("Please visit %s to authenticate" % validation['validationUrl'])
     input("and press Enter to continue...")
 
     # Print nice welcome message
     print("Welcome", client.get('/me')['firstname'])
     print("Btw, your 'consumerKey' is '%s'" % validation['consumerKey'])
 
-
 Returned ``consumerKey`` should then be kept to avoid re-authenticating your
 end-user on each use.
 
 .. note:: To request full and unlimited access to the API, you may use ``add_recursive_rules``:
 
 .. code:: python
 
@@ -175,16 +171,14 @@
 ``from`` keyword. Which is a problem as this is also a reserved Python keyword.
 In this case, simply prefix it with a '_', the wrapper will automatically detect
 it as being a prefixed reserved keyword and will substitute it. Such aliasing
 is only supported with reserved keywords.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     DOMAIN = "example.com"
     SOURCE = "sales@example.com"
     DESTINATION = "contact@example.com"
 
     # create a client
@@ -206,16 +200,14 @@
 of each bill lines using ``/me/bill/{billId}/details/{billDetailId}``.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # Grab bill list
     bills = client.get('/me/bill')
@@ -236,16 +228,14 @@
 manually for each servers. You could take advantage of a code like this.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # get list of all server names
     servers = client.get('/dedicated/server/')
@@ -267,16 +257,14 @@
 manage revocation too.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
     from tabulate import tabulate
 
     # create a client
     client = ovh.Client()
 
     credentials = client.get('/me/api/credential', status='validated')
@@ -314,15 +302,14 @@
 particularly useful to tweak the BIOS or troubleshoot boot issues.
 
 Hopefully, this can easily be automated using a simple script. It assumes Java Web Start is
 fully installed on the machine and a consumer key allowed on the server exists.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
     import sys
     import time
     import tempfile
     import subprocess
 
     # check arguments
@@ -422,41 +409,63 @@
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client()
 
+Use v1 and v2 API versions
+--------------------------
+
+When using OVHcloud APIs (not So you Start or Kimsufi ones), you are given the
+opportunity to aim for two API versions. For the European API, for example:
+
+- the v1 is reachable through https://eu.api.ovh.com/v1
+- the v2 is reachable through https://eu.api.ovh.com/v2
+- the legacy URL is https://eu.api.ovh.com/1.0
+
+ Calling ``client.get``, you can target the API version you want:
+
+.. code:: python
+
+    client = ovh.Client(endpoint="ovh-eu")
+
+    # Call to https://eu.api.ovh.com/v1/xdsl/xdsl-yourservice
+    client.get("/v1/xdsl/xdsl-yourservice")
+
+    # Call to https://eu.api.ovh.com/v2/xdsl/xdsl-yourservice
+    client.get("/v2/xdsl/xdsl-yourservice")
+
+    # Legacy call to https://eu.api.ovh.com/1.0/xdsl/xdsl-yourservice
+    client.get("/xdsl/xdsl-yourservice")
+
 Custom configuration file
 -------------------------
 
 You can also specify a custom configuration file. With this method, you won't be able to inherit values from environment.
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client(config_file='/my/config.conf')
 
-
 Passing parameters
 ==================
 
 You can call all the methods of the API with the necessary arguments.
 
 If an API needs an argument colliding with a Python reserved keyword, it
 can be prefixed with an underscore. For example, ``from`` argument of
 ``POST /email/domain/{domain}/redirection`` may be replaced by ``_from``.
 
 With characters invalid in python argument name like a dot, you can:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     params = {}
     params['date.from'] = '2014-01-01'
     params['date.to'] = '2015-01-01'
 
     # create a client
@@ -505,29 +514,28 @@
 
 .. code:: bash
 
     git clone https://github.com/ovh/python-ovh.git
     cd python-ovh
     python setup.py develop
 
-You've developed a new cool feature ? Fixed an annoying bug ? We'd be happy
-to hear from you !
+You've developed a new cool feature? Fixed an annoying bug? We'd be happy
+to hear from you!
 
 Run the tests
 -------------
 
-Simply run ``nosetests``. It will automatically load its configuration from
+Simply run ``pytest``. It will automatically load its configuration from
 ``setup.cfg`` and output full coverage status. Since we all love quality, please
 note that we do not accept contributions with test coverage under 100%.
 
 .. code:: bash
 
     pip install -e .[dev]
-    nosetests # 100% coverage is a hard minimum
-
+    pytest
 
 Build the documentation
 -----------------------
 
 Documentation is managed using the excellent ``Sphinx`` system. For example, to
 build HTML documentation:
```

### Comparing `ovh-1.0.0/docs/Makefile` & `ovh-1.1.0/docs/Makefile`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/docs/api/ovh/client.rst` & `ovh-1.1.0/docs/api/ovh/client.rst`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/docs/api/ovh/exceptions.rst` & `ovh-1.1.0/docs/api/ovh/exceptions.rst`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/docs/conf.py` & `ovh-1.1.0/docs/conf.py`

 * *Files 14% similar despite different names*

```diff
@@ -8,256 +8,253 @@
 #
 # Note that not all possible configuration values are present in this
 # autogenerated file.
 #
 # All configuration values have a default; values that are commented out
 # serve to show the default.
 
-import sys
-import os
-
 # If extensions (or modules to document with autodoc) are in another directory,
 # add these directories to sys.path here. If the directory is relative to the
 # documentation root, use os.path.abspath to make it absolute, like shown here.
-#sys.path.insert(0, os.path.abspath('.'))
+# sys.path.insert(0, os.path.abspath('.'))
 
 # -- General configuration ------------------------------------------------
 
 # If your documentation needs a minimal Sphinx version, state it here.
-#needs_sphinx = '1.0'
+# needs_sphinx = '1.0'
 
 # Add any Sphinx extension module names here, as strings. They can be
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
 # ones.
 extensions = [
-    'sphinx.ext.autodoc',
-    'sphinx.ext.doctest',
-    'sphinx.ext.coverage',
-    'sphinx.ext.viewcode',
+    "sphinx.ext.autodoc",
+    "sphinx.ext.doctest",
+    "sphinx.ext.coverage",
+    "sphinx.ext.viewcode",
 ]
 
 # Add any paths that contain templates here, relative to this directory.
-templates_path = ['_templates']
+templates_path = ["_templates"]
 
 # The suffix of source filenames.
-source_suffix = '.rst'
+source_suffix = ".rst"
 
 # The encoding of source files.
-#source_encoding = 'utf-8-sig'
+# source_encoding = 'utf-8-sig'
 
 # The master toctree document.
-master_doc = 'index'
+master_doc = "index"
 
 # General information about the project.
-project = u'Python-OVH'
-copyright = u'2013-2014, OVH SAS'
+project = "Python-OVH"
+copyright = "2013-2014, OVH SAS"
 
 # The version info for the project you're documenting, acts as replacement for
 # |version| and |release|, also used in various other places throughout the
 # built documents.
 #
 # The short X.Y version.
-version = '0.3'
+version = "0.3"
 # The full version, including alpha/beta/rc tags.
-release = '0.5.0'
+release = "0.5.0"
 
 # The language for content autogenerated by Sphinx. Refer to documentation
 # for a list of supported languages.
-#language = None
+# language = None
 
 # There are two options for replacing |today|: either, you set today to some
 # non-false value, then it is used:
-#today = ''
+# today = ''
 # Else, today_fmt is used as the format for a strftime call.
-#today_fmt = '%B %d, %Y'
+# today_fmt = '%B %d, %Y'
 
 # List of patterns, relative to source directory, that match files and
 # directories to ignore when looking for source files.
-exclude_patterns = ['_build']
+exclude_patterns = ["_build"]
 
 # The reST default role (used for this markup: `text`) to use for all
 # documents.
-#default_role = None
+# default_role = None
 
 # If true, '()' will be appended to :func: etc. cross-reference text.
-#add_function_parentheses = True
+# add_function_parentheses = True
 
 # If true, the current module name will be prepended to all description
 # unit titles (such as .. function::).
-#add_module_names = True
+# add_module_names = True
 
 # If true, sectionauthor and moduleauthor directives will be shown in the
 # output. They are ignored by default.
-#show_authors = False
+# show_authors = False
 
 # The name of the Pygments (syntax highlighting) style to use.
-pygments_style = 'sphinx'
+pygments_style = "sphinx"
 
 # A list of ignored prefixes for module index sorting.
-#modindex_common_prefix = []
+# modindex_common_prefix = []
 
 # If true, keep warnings as "system message" paragraphs in the built documents.
-#keep_warnings = False
+# keep_warnings = False
 
 
 # -- Options for HTML output ----------------------------------------------
 
 # The theme to use for HTML and HTML Help pages.  See the documentation for
 # a list of builtin themes.
-html_theme = 'default'
+html_theme = "default"
 
 # Theme options are theme-specific and customize the look and feel of a theme
 # further.  For a list of options available for each theme, see the
 # documentation.
-#html_theme_options = {}
+# html_theme_options = {}
 
 # Add any paths that contain custom themes here, relative to this directory.
-#html_theme_path = []
+# html_theme_path = []
 
 # The name for this set of Sphinx documents.  If None, it defaults to
 # "<project> v<release> documentation".
-#html_title = None
+# html_title = None
 
 # A shorter title for the navigation bar.  Default is the same as html_title.
-#html_short_title = None
+# html_short_title = None
 
 # The name of an image file (relative to this directory) to place at the top
 # of the sidebar.
-#html_logo = None
+# html_logo = None
 
 # The name of an image file (within the static path) to use as favicon of the
 # docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
 # pixels large.
-#html_favicon = None
+# html_favicon = None
 
 # Add any paths that contain custom static files (such as style sheets) here,
 # relative to this directory. They are copied after the builtin static files,
 # so a file named "default.css" will overwrite the builtin "default.css".
-html_static_path = ['_static']
+html_static_path = ["_static"]
 
 # Add any extra paths that contain custom files (such as robots.txt or
 # .htaccess) here, relative to this directory. These files are copied
 # directly to the root of the documentation.
-#html_extra_path = []
+# html_extra_path = []
 
 # If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
 # using the given strftime format.
-#html_last_updated_fmt = '%b %d, %Y'
+# html_last_updated_fmt = '%b %d, %Y'
 
 # If true, SmartyPants will be used to convert quotes and dashes to
 # typographically correct entities.
-#html_use_smartypants = True
+# html_use_smartypants = True
 
 # Custom sidebar templates, maps document names to template names.
-#html_sidebars = {}
+# html_sidebars = {}
 
 # Additional templates that should be rendered to pages, maps page names to
 # template names.
-#html_additional_pages = {}
+# html_additional_pages = {}
 
 # If false, no module index is generated.
-#html_domain_indices = True
+# html_domain_indices = True
 
 # If false, no index is generated.
-#html_use_index = True
+# html_use_index = True
 
 # If true, the index is split into individual pages for each letter.
-#html_split_index = False
+# html_split_index = False
 
 # If true, links to the reST sources are added to the pages.
-#html_show_sourcelink = True
+# html_show_sourcelink = True
 
 # If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
-#html_show_sphinx = True
+# html_show_sphinx = True
 
 # If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
-#html_show_copyright = True
+# html_show_copyright = True
 
 # If true, an OpenSearch description file will be output, and all pages will
 # contain a <link> tag referring to it.  The value of this option must be the
 # base URL from which the finished HTML is served.
-#html_use_opensearch = ''
+# html_use_opensearch = ''
 
 # This is the file name suffix for HTML files (e.g. ".xhtml").
-#html_file_suffix = None
+# html_file_suffix = None
 
 # Output file base name for HTML help builder.
-htmlhelp_basename = 'python-ovh-doc'
+htmlhelp_basename = "python-ovh-doc"
 
 
 # -- Options for LaTeX output ---------------------------------------------
 
 latex_elements = {
-# The paper size ('letterpaper' or 'a4paper').
-#'papersize': 'letterpaper',
-
-# The font size ('10pt', '11pt' or '12pt').
-#'pointsize': '10pt',
-
-# Additional stuff for the LaTeX preamble.
-#'preamble': '',
+    # The paper size ('letterpaper' or 'a4paper').
+    # 'papersize': 'letterpaper',
+    # The font size ('10pt', '11pt' or '12pt').
+    # 'pointsize': '10pt',
+    # Additional stuff for the LaTeX preamble.
+    # 'preamble': '',
 }
 
 # Grouping the document tree into LaTeX files. List of tuples
 # (source start file, target name, title,
 #  author, documentclass [howto, manual, or own class]).
 latex_documents = [
-  ('index', 'Python-OVH.tex', u'Python-OVH Documentation',
-   u'Jean-Tiare Le Bigot', 'manual'),
+    ("index", "Python-OVH.tex", "Python-OVH Documentation", "Jean-Tiare Le Bigot", "manual"),
 ]
 
 # The name of an image file (relative to this directory) to place at the top of
 # the title page.
-#latex_logo = None
+# latex_logo = None
 
 # For "manual" documents, if this is true, then toplevel headings are parts,
 # not chapters.
-#latex_use_parts = False
+# latex_use_parts = False
 
 # If true, show page references after internal links.
-#latex_show_pagerefs = False
+# latex_show_pagerefs = False
 
 # If true, show URL addresses after external links.
-#latex_show_urls = False
+# latex_show_urls = False
 
 # Documents to append as an appendix to all manuals.
-#latex_appendices = []
+# latex_appendices = []
 
 # If false, no module index is generated.
-#latex_domain_indices = True
+# latex_domain_indices = True
 
 
 # -- Options for manual page output ---------------------------------------
 
 # One entry per manual page. List of tuples
 # (source start file, name, description, authors, manual section).
-man_pages = [
-    ('index', 'python-ovh', u'Python-OVH Documentation',
-     [u'Jean-Tiare Le Bigot'], 1)
-]
+man_pages = [("index", "python-ovh", "Python-OVH Documentation", ["Jean-Tiare Le Bigot"], 1)]
 
 # If true, show URL addresses after external links.
-#man_show_urls = False
+# man_show_urls = False
 
 
 # -- Options for Texinfo output -------------------------------------------
 
 # Grouping the document tree into Texinfo files. List of tuples
 # (source start file, target name, title, author,
 #  dir menu entry, description, category)
 texinfo_documents = [
-  ('index', 'Python-OVH', u'Python-OVH Documentation',
-   u'Jean-Tiare Le Bigot', 'Python-OVH', 'OVH Rest API wrapper.',
-   'API'),
+    (
+        "index",
+        "Python-OVH",
+        "Python-OVH Documentation",
+        "Jean-Tiare Le Bigot",
+        "Python-OVH",
+        "OVH Rest API wrapper.",
+        "API",
+    ),
 ]
 
 # Documents to append as an appendix to all manuals.
-#texinfo_appendices = []
+# texinfo_appendices = []
 
 # If false, no module index is generated.
-#texinfo_domain_indices = True
+# texinfo_domain_indices = True
 
 # How to display URL addresses: 'footnote', 'no', or 'inline'.
-#texinfo_show_urls = 'footnote'
+# texinfo_show_urls = 'footnote'
 
 # If true, do not generate a @detailmenu in the "Top" node's menu.
-#texinfo_no_detailmenu = False
+# texinfo_no_detailmenu = False
```

### Comparing `ovh-1.0.0/docs/img/logo.png` & `ovh-1.1.0/docs/img/logo.png`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/docs/index.rst` & `ovh-1.1.0/docs/index.rst`

 * *Files 2% similar despite different names*

```diff
@@ -7,16 +7,14 @@
 =================================================
 
 Thin wrapper around OVH's APIs. Handles all the hard work including credential
 creation and requests signing.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # Instantiate. Visit https://api.ovh.com/createToken/index.cgi?GET=/me
     # to get your credentials
     client = ovh.Client(
         endpoint='ovh-eu',
         application_key='<application key>',
@@ -106,16 +104,14 @@
 **********************************************************
 
 To allow your application to access a customer account using the API on your
 behalf, you need a **consumer key (CK)**.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     try:
         input = raw_input
     except NameError:
         pass
 
     import ovh
 
@@ -163,16 +159,14 @@
 ``from`` keyword. Which is a problem as this is also a reserved Python keyword.
 In this case, simply prefix it with a '_', the wrapper will automatically detect
 it as being a prefixed reserved keyword and will substitute it. Such aliasing
 is only supported with reserved keywords.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     DOMAIN = "example.com"
     SOURCE = "sales@example.com"
     DESTINATION = "contact@example.com"
 
     # create a client
@@ -194,16 +188,14 @@
 of each bill lines using ``/me/bill/{billId}/details/{billDetailId}``.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client without a consumerKey
     client = ovh.Client()
 
     # Grab bill list
     bills = client.get('/me/bill')
@@ -224,16 +216,14 @@
 manually for each servers. You could take advantage of a code like this.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # get list of all server names
     servers = client.get('/dedicated/server/')
@@ -255,16 +245,14 @@
 manage revocation too.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
     from tabulate import tabulate
 
     # create a client
     client = ovh.Client()
 
     credentials = client.get('/me/api/credential', status='validated')
@@ -339,16 +327,14 @@
 can be prefixed with an underscore. For example, ``from`` argument of
 ``POST /email/domain/{domain}/redirection`` may be replaced by ``_from``.
 
 With characters invalid in python argument name like a dot, you can:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     params = {}
     params['date.from'] = '2014-01-01'
     params['date.to'] = '2015-01-01'
 
     # create a client
```

### Comparing `ovh-1.0.0/docs/make.bat` & `ovh-1.1.0/docs/make.bat`

 * *Files identical despite different names*

### Comparing `ovh-1.0.0/ovh/__init__.py` & `ovh-1.1.0/tests/__init__.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -21,20 +19,7 @@
 # DISCLAIMED. IN NO EVENT SHALL OVH SAS AND CONTRIBUTORS BE LIABLE FOR ANY
 # DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 # (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 # LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 # ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 # SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
-
-from .client import Client
-from .exceptions import (
-    APIError, NetworkError, InvalidResponse, InvalidRegion, ReadOnlyError,
-    ResourceNotFoundError, BadParametersError, ResourceConflictError, HTTPError,
-    InvalidKey, InvalidCredential, NotGrantedCall, NotCredential, Forbidden,
-)
-from .consumer_key import (
-    ConsumerKeyRequest,
-    API_READ_ONLY,
-    API_READ_WRITE,
-    API_READ_WRITE_SAFE,
-)
```

### Comparing `ovh-1.0.0/ovh/client.py` & `ovh-1.1.0/ovh/client.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -31,54 +29,57 @@
 It handles requesting credential, signing queries...
 
  - To get your API keys: https://eu.api.ovh.com/createApp/
  - To get started with API: https://api.ovh.com/g934.first_step_with_api
 """
 
 import hashlib
-import urllib
+import json
 import keyword
 import time
-import json
+from urllib.parse import urlencode
 
-try:
-    from urllib import urlencode
-except ImportError: # pragma: no cover
-    # Python 3
-    from urllib.parse import urlencode
-
-from requests import request, Session
-from requests.packages import urllib3
+from requests import Session
 from requests.exceptions import RequestException
 
-from .config import config
+from . import config
 from .consumer_key import ConsumerKeyRequest
 from .exceptions import (
-    APIError, NetworkError, InvalidResponse, InvalidRegion, InvalidKey,
-    ResourceNotFoundError, BadParametersError, ResourceConflictError, HTTPError,
-    NotGrantedCall, NotCredential, Forbidden, InvalidCredential,
+    APIError,
+    BadParametersError,
+    Forbidden,
+    HTTPError,
+    InvalidCredential,
+    InvalidKey,
+    InvalidRegion,
+    InvalidResponse,
+    NetworkError,
+    NotCredential,
+    NotGrantedCall,
+    ResourceConflictError,
     ResourceExpiredError,
+    ResourceNotFoundError,
 )
 
 #: Mapping between OVH API region names and corresponding endpoints
 ENDPOINTS = {
-    'ovh-eu': 'https://eu.api.ovh.com/1.0',
-    'ovh-us': 'https://api.us.ovhcloud.com/1.0',
-    'ovh-ca': 'https://ca.api.ovh.com/1.0',
-    'kimsufi-eu': 'https://eu.api.kimsufi.com/1.0',
-    'kimsufi-ca': 'https://ca.api.kimsufi.com/1.0',
-    'soyoustart-eu': 'https://eu.api.soyoustart.com/1.0',
-    'soyoustart-ca': 'https://ca.api.soyoustart.com/1.0',
+    "ovh-eu": "https://eu.api.ovh.com/1.0",
+    "ovh-us": "https://api.us.ovhcloud.com/1.0",
+    "ovh-ca": "https://ca.api.ovh.com/1.0",
+    "kimsufi-eu": "https://eu.api.kimsufi.com/1.0",
+    "kimsufi-ca": "https://ca.api.kimsufi.com/1.0",
+    "soyoustart-eu": "https://eu.api.soyoustart.com/1.0",
+    "soyoustart-ca": "https://ca.api.soyoustart.com/1.0",
 }
 
 #: Default timeout for each request. 180 seconds connect, 180 seconds read.
 TIMEOUT = 180
 
 
-class Client(object):
+class Client:
     """
     Low level OVH Client. It abstracts all the authentication and request
     signing logic along with some nice tools helping with key generation.
 
     All low level request logic including signing and error handling takes place
     in :py:func:`Client.call` function. Convenient wrappers
     :py:func:`Client.get` :py:func:`Client.post`, :py:func:`Client.put`,
@@ -102,17 +103,23 @@
         try:
             print(client.get('/me'))
         except APIError as e:
             print("Ooops, failed to get my info:", e.msg)
 
     """
 
-    def __init__(self, endpoint=None, application_key=None,
-                 application_secret=None, consumer_key=None, timeout=TIMEOUT,
-                 config_file=None):
+    def __init__(
+        self,
+        endpoint=None,
+        application_key=None,
+        application_secret=None,
+        consumer_key=None,
+        timeout=TIMEOUT,
+        config_file=None,
+    ):
         """
         Creates a new Client. No credential check is done at this point.
 
         The ``application_key`` identifies your application while
         ``application_secret`` authenticates it. On the other hand, the
         ``consumer_key`` uniquely identifies your application's end user without
         requiring his personal password.
@@ -134,51 +141,53 @@
         :param str application_key: Application key as provided by OVH
         :param str application_secret: Application secret key as provided by OVH
         :param str consumer_key: uniquely identifies
         :param tuple timeout: Connection and read timeout for each request
         :param float timeout: Same timeout for both connection and read
         :raises InvalidRegion: if ``endpoint`` can't be found in ``ENDPOINTS``.
         """
+
+        configuration = config.ConfigurationManager()
+
         # Load a custom config file if requested
         if config_file is not None:
-            config.read(config_file)
+            configuration.read(config_file)
 
         # load endpoint
         if endpoint is None:
-            endpoint = config.get('default', 'endpoint')
+            endpoint = configuration.get("default", "endpoint")
 
         try:
             self._endpoint = ENDPOINTS[endpoint]
         except KeyError:
-            raise InvalidRegion("Unknown endpoint %s. Valid endpoints: %s",
-                                endpoint, ENDPOINTS.keys())
+            raise InvalidRegion("Unknown endpoint %s. Valid endpoints: %s", endpoint, ENDPOINTS.keys())
 
         # load keys
         if application_key is None:
-            application_key = config.get(endpoint, 'application_key')
+            application_key = configuration.get(endpoint, "application_key")
         self._application_key = application_key
 
         if application_secret is None:
-            application_secret = config.get(endpoint, 'application_secret')
+            application_secret = configuration.get(endpoint, "application_secret")
         self._application_secret = application_secret
 
         if consumer_key is None:
-            consumer_key = config.get(endpoint, 'consumer_key')
+            consumer_key = configuration.get(endpoint, "consumer_key")
         self._consumer_key = consumer_key
 
         # lazy load time delta
         self._time_delta = None
 
         # use a requests session to reuse HTTPS connections between requests
         self._session = Session()
 
         # Override default timeout
         self._timeout = timeout
 
-    ## high level API
+    # high level API
 
     @property
     def time_delta(self):
         """
         Request signatures are valid only for a short amount of time to mitigate
         risk of attack replay scenarii which requires to use a common time
         reference. This function queries endpoint's time and computes the delta.
@@ -189,15 +198,15 @@
 
         .. note:: You should not need to use this property directly
 
         :returns: time distance between local and server time in seconds.
         :rtype: int
         """
         if self._time_delta is None:
-            server_time = self.get('/auth/time', _need_auth=False)
+            server_time = self.get("/auth/time", _need_auth=False)
             self._time_delta = server_time - int(time.time())
         return self._time_delta
 
     def new_consumer_key_request(self):
         """
         Create a new consumer key request. This is the recommended way to create
         a new consumer key request.
@@ -211,15 +220,15 @@
         >>> ck.add_recursive_rules(ovh.API_READ_WRITE, "/sms")
         >>> ck.request()
         {
             'state': 'pendingValidation',
             'consumerKey': 'TnpZAd5pYNqxk4RhlPiSRfJ4WrkmII2i',
             'validationUrl': 'https://eu.api.ovh.com/auth/?credentialToken=now2OOAVO4Wp6t7bemyN9DMWIobhGjFNZSHmixtVJM4S7mzjkN2L5VBfG96Iy1i0'
         }
-        """
+        """  # noqa:E501
         return ConsumerKeyRequest(self)
 
     def request_consumerkey(self, access_rules, redirect_url=None):
         """
         Create a new "consumer key" identifying this application's end user. API
         will return a ``consumerKey`` and a ``validationUrl``. The end user must
         visit the ``validationUrl``, authenticate and validate the requested
@@ -271,34 +280,33 @@
 
         :param list access_rules: Mapping specifying requested privileges.
         :param str redirect_url: Where to redirect end user upon validation.
         :raises APIError: When ``self.call`` fails.
         :returns: dict with ``consumerKey`` and ``validationUrl`` keys
         :rtype: dict
         """
-        res = self.post('/auth/credential', _need_auth=False,
-                        accessRules=access_rules, redirection=redirect_url)
-        self._consumer_key = res['consumerKey']
+        res = self.post("/auth/credential", _need_auth=False, accessRules=access_rules, redirection=redirect_url)
+        self._consumer_key = res["consumerKey"]
         return res
 
-    ## API shortcuts
+    # API shortcuts
 
     def _canonicalize_kwargs(self, kwargs):
         """
         If an API needs an argument colliding with a Python reserved keyword, it
         can be prefixed with an underscore. For example, ``from`` argument of
         ``POST /email/domain/{domain}/redirection`` may be replaced by ``_from``
 
         :param dict kwargs: input kwargs
         :return dict: filtered kawrgs
         """
         arguments = {}
 
         for k, v in kwargs.items():
-            if k[0] == '_' and k[1:] in keyword.kwlist:
+            if k[0] == "_" and k[1:] in keyword.kwlist:
                 k = k[1:]
             arguments[k] = v
 
         return arguments
 
     def _prepare_query_string(self, kwargs):
         """
@@ -331,20 +339,20 @@
         :param string _need_auth: If True, send authentication headers. This is
             the default
         """
         if kwargs:
             kwargs = self._canonicalize_kwargs(kwargs)
             query_string = self._prepare_query_string(kwargs)
             if query_string != "":
-                if '?' in _target:
-                    _target = '%s&%s' % (_target, query_string)
+                if "?" in _target:
+                    _target = "%s&%s" % (_target, query_string)
                 else:
-                    _target = '%s?%s' % (_target, query_string)
+                    _target = "%s?%s" % (_target, query_string)
 
-        return self.call('GET', _target, None, _need_auth)
+        return self.call("GET", _target, None, _need_auth)
 
     def put(self, _target, _need_auth=True, **kwargs):
         """
         'PUT' :py:func:`Client.call` wrapper
 
         Body parameters can be set either directly in ``_target`` or as keyword
         arguments. If an argument collides with a Python reserved keyword,
@@ -353,15 +361,15 @@
         :param string _target: API method to call
         :param string _need_auth: If True, send authentication headers. This is
             the default
         """
         kwargs = self._canonicalize_kwargs(kwargs)
         if not kwargs:
             kwargs = None
-        return self.call('PUT', _target, kwargs, _need_auth)
+        return self.call("PUT", _target, kwargs, _need_auth)
 
     def post(self, _target, _need_auth=True, **kwargs):
         """
         'POST' :py:func:`Client.call` wrapper
 
         Body parameters can be set either directly in ``_target`` or as keyword
         arguments. If an argument collides with a Python reserved keyword,
@@ -370,15 +378,15 @@
         :param string _target: API method to call
         :param string _need_auth: If True, send authentication headers. This is
             the default
         """
         kwargs = self._canonicalize_kwargs(kwargs)
         if not kwargs:
             kwargs = None
-        return self.call('POST', _target, kwargs, _need_auth)
+        return self.call("POST", _target, kwargs, _need_auth)
 
     def delete(self, _target, _need_auth=True, **kwargs):
         """
         'DELETE' :py:func:`Client.call` wrapper
 
         Query string parameters can be set either directly in ``_target`` or as
         keyword arguments. If an argument collides with a Python reserved
@@ -388,22 +396,22 @@
         :param string _need_auth: If True, send authentication headers. This is
             the default
         """
         if kwargs:
             kwargs = self._canonicalize_kwargs(kwargs)
             query_string = self._prepare_query_string(kwargs)
             if query_string != "":
-                if '?' in _target:
-                    _target = '%s&%s' % (_target, query_string)
+                if "?" in _target:
+                    _target = "%s&%s" % (_target, query_string)
                 else:
-                    _target = '%s?%s' % (_target, query_string)
+                    _target = "%s?%s" % (_target, query_string)
 
-        return self.call('DELETE', _target, None, _need_auth)
+        return self.call("DELETE", _target, None, _need_auth)
 
-    ## low level helpers
+    # low level helpers
 
     def call(self, method, path, data=None, need_auth=True):
         """
         Low level call helper. If ``consumer_key`` is not ``None``, inject
         authentication headers and sign the request.
 
         Request signature is a sha1 hash on following fields, joined by '+'
@@ -437,43 +445,50 @@
                 json_result = None
         except ValueError as error:
             raise InvalidResponse("Failed to decode API response", error)
 
         # error check
         if status >= 100 and status < 300:
             return json_result
-        elif status == 403 and json_result.get('errorCode') == 'NOT_GRANTED_CALL':
-                raise NotGrantedCall(json_result.get('message'),
-                                     response=result)
-        elif status == 403 and json_result.get('errorCode') == 'NOT_CREDENTIAL':
-                raise NotCredential(json_result.get('message'),
-                                    response=result)
-        elif status == 403 and json_result.get('errorCode') == 'INVALID_KEY':
-                raise InvalidKey(json_result.get('message'), response=result)
-        elif status == 403 and json_result.get('errorCode') == 'INVALID_CREDENTIAL':
-                raise InvalidCredential(json_result.get('message'),
-                                        response=result)
-        elif status == 403 and json_result.get('errorCode') == 'FORBIDDEN':
-                raise Forbidden(json_result.get('message'), response=result)
+        elif status == 403 and json_result.get("errorCode") == "NOT_GRANTED_CALL":
+            raise NotGrantedCall(json_result.get("message"), response=result)
+        elif status == 403 and json_result.get("errorCode") == "NOT_CREDENTIAL":
+            raise NotCredential(json_result.get("message"), response=result)
+        elif status == 403 and json_result.get("errorCode") == "INVALID_KEY":
+            raise InvalidKey(json_result.get("message"), response=result)
+        elif status == 403 and json_result.get("errorCode") == "INVALID_CREDENTIAL":
+            raise InvalidCredential(json_result.get("message"), response=result)
+        elif status == 403 and json_result.get("errorCode") == "FORBIDDEN":
+            raise Forbidden(json_result.get("message"), response=result)
         elif status == 404:
-            raise ResourceNotFoundError(json_result.get('message'),
-                                        response=result)
+            raise ResourceNotFoundError(json_result.get("message"), response=result)
         elif status == 400:
-            raise BadParametersError(json_result.get('message'),
-                                     response=result)
+            raise BadParametersError(json_result.get("message"), response=result)
         elif status == 409:
-            raise ResourceConflictError(json_result.get('message'),
-                                        response=result)
+            raise ResourceConflictError(json_result.get("message"), response=result)
         elif status == 460:
-            raise ResourceExpiredError(json_result.get('message'),
-                                       response=result)
+            raise ResourceExpiredError(json_result.get("message"), response=result)
         elif status == 0:
             raise NetworkError()
         else:
-            raise APIError(json_result.get('message'), response=result)
+            raise APIError(json_result.get("message"), response=result)
+
+    def _get_target(self, path):
+        """
+        _get_target returns the URL to target given an endpoint and a path.
+        If the path starts with `/v1` or `/v2`, then remove the trailing `/1.0` from the endpoint.
+
+        :param str path: path to use prefix from
+        :returns: target with one of /1.0 and /v1|2 path segment
+        :rtype: str
+        """
+        endpoint = self._endpoint
+        if endpoint.endswith("/1.0") and path.startswith(("/v1", "/v2")):
+            endpoint = endpoint[:-4]
+        return endpoint + path
 
     def raw_call(self, method, path, data=None, need_auth=True, headers=None):
         """
         Lowest level call helper. If ``consumer_key`` is not ``None``, inject
         authentication headers and sign the request.
         Will return ``requests.Response`` object or let any
         ``requests`` exception pass through.
@@ -491,44 +506,40 @@
         :param data: any json serializable data to send as request's body
         :param boolean need_auth: if False, bypass signature
         :param dict headers: A dict containing the headers that should be sent to
                              the OVH API. ``raw_call`` will override the
                              OVH API authentication headers, as well as
                              the Content-Type header.
         """
-        body = ''
-        target = self._endpoint + path
+        body = ""
+        target = self._get_target(path)
 
         if headers is None:
             headers = {}
-        headers['X-Ovh-Application'] = self._application_key
+        headers["X-Ovh-Application"] = self._application_key
 
         # include payload
         if data is not None:
-            headers['Content-type'] = 'application/json'
-            body = json.dumps(data)
+            headers["Content-type"] = "application/json"
+            body = json.dumps(data, separators=(",", ":"))  # Separators to prevent adding useless spaces
 
         # sign request. Never sign 'time' or will recurse infinitely
         if need_auth:
             if not self._application_secret:
-                raise InvalidKey("Invalid ApplicationSecret '%s'" %
-                                 self._application_secret)
+                raise InvalidKey("Invalid ApplicationSecret '%s'" % self._application_secret)
 
             if not self._consumer_key:
-                raise InvalidKey("Invalid ConsumerKey '%s'" %
-                                 self._consumer_key)
+                raise InvalidKey("Invalid ConsumerKey '%s'" % self._consumer_key)
 
             now = str(int(time.time()) + self.time_delta)
             signature = hashlib.sha1()
-            signature.update("+".join([
-                self._application_secret, self._consumer_key,
-                method.upper(), target,
-                body,
-                now
-            ]).encode('utf-8'))
-
-            headers['X-Ovh-Consumer'] = self._consumer_key
-            headers['X-Ovh-Timestamp'] = now
-            headers['X-Ovh-Signature'] = "$1$" + signature.hexdigest()
+            signature.update(
+                "+".join([self._application_secret, self._consumer_key, method.upper(), target, body, now]).encode(
+                    "utf-8"
+                )
+            )
+
+            headers["X-Ovh-Consumer"] = self._consumer_key
+            headers["X-Ovh-Timestamp"] = now
+            headers["X-Ovh-Signature"] = "$1$" + signature.hexdigest()
 
-        return self._session.request(method, target, headers=headers,
-                                     data=body, timeout=self._timeout)
+        return self._session.request(method, target, headers=headers, data=body, timeout=self._timeout)
```

### Comparing `ovh-1.0.0/ovh/config.py` & `ovh-1.1.0/ovh/config.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -58,57 +56,54 @@
 2. Current user's home directory ``~/.ovh.conf``
 3. System wide configuration ``/etc/ovh.conf``
 
 This lookup mechanism makes it easy to overload credentials for a specific
 project or user.
 """
 
+from configparser import NoOptionError, NoSectionError, RawConfigParser
 import os
 
-try:
-    from ConfigParser import RawConfigParser, NoSectionError, NoOptionError
-except ImportError: # pragma: no cover
-    # Python 3
-    from configparser import RawConfigParser, NoSectionError, NoOptionError
-
-__all__ = ['config']
+__all__ = ["config"]
 
 #: Locations where to look for configuration file by *increasing* priority
 CONFIG_PATH = [
-    '/etc/ovh.conf',
-    os.path.expanduser('~/.ovh.conf'),
-    os.path.realpath('./ovh.conf'),
+    "/etc/ovh.conf",
+    os.path.expanduser("~/.ovh.conf"),
+    os.path.realpath("./ovh.conf"),
 ]
 
-class ConfigurationManager(object):
-    '''
+
+class ConfigurationManager:
+    """
     Application wide configuration manager
-    '''
+    """
+
     def __init__(self):
-        '''
+        """
         Create a config parser and load config from environment.
-        '''
+        """
         # create config parser
         self.config = RawConfigParser()
         self.config.read(CONFIG_PATH)
 
     def get(self, section, name):
-        '''
+        """
         Load parameter ``name`` from configuration, respecting priority order.
         Most of the time, ``section`` will correspond to the current api
         ``endpoint``. ``default`` section only contains ``endpoint`` and general
         configuration.
 
         :param str section: configuration section or region name. Ignored when
             looking in environment
         :param str name: configuration parameter to lookup
-        '''
+        """
         # 1/ try env
         try:
-            return os.environ['OVH_'+name.upper()]
+            return os.environ["OVH_" + name.upper()]
         except KeyError:
             pass
 
         # 2/ try from specified section/endpoint
         try:
             return self.config.get(section, name)
         except (NoSectionError, NoOptionError):
@@ -117,9 +112,10 @@
         # not found, sorry
         return None
 
     def read(self, config_file):
         # Read an other config file
         self.config.read(config_file)
 
+
 #: System wide instance :py:class:`ConfigurationManager` instance
 config = ConfigurationManager()
```

### Comparing `ovh-1.0.0/ovh/consumer_key.py` & `ovh-1.1.0/ovh/consumer_key.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -36,78 +34,78 @@
 powerful and flexible as it may apply on only a very specific subset of the API
 but it's also trickier to get right on simple scenarios.
 
 Hence this module
 """
 
 # Common authorization patterns
-API_READ_ONLY       = ["GET"]
-API_READ_WRITE      = ["GET", "POST", "PUT", "DELETE"]
+API_READ_ONLY = ["GET"]
+API_READ_WRITE = ["GET", "POST", "PUT", "DELETE"]
 API_READ_WRITE_SAFE = ["GET", "POST", "PUT"]
 
+
 class ConsumerKeyRequest(object):
-    '''
+    """
     ConsumerKey request. The generated consumer key will be linked to the
     client's ``application_key``. When performing the request, the
     ``consumer_key`` will automatically be registered in the client.
 
     It is recommended to save the generated key as soon as it validated to avoid
     requesting a new one on each API access.
-    '''
+    """
 
     def __init__(self, client):
-        '''
+        """
         Create a new consumer key helper on API ``client``. The keys will be
         tied to the ``application_key`` defined in the client.
-        '''
+        """
         self._client = client
         self._access_rules = []
 
     def request(self, redirect_url=None):
-        '''
+        """
         Create the consumer key with the configures autorizations. The user will
         need to validate it before it can be used with the API
 
         >>> ck.request()
         {
             'state': 'pendingValidation',
             'consumerKey': 'TnpZAd5pYNqxk4RhlPiSRfJ4WrkmII2i',
             'validationUrl': 'https://eu.api.ovh.com/auth/?credentialToken=now2OOAVO4Wp6t7bemyN9DMWIobhGjFNZSHmixtVJM4S7mzjkN2L5VBfG96Iy1i0'
         }
-        '''
+        """  # noqa: E501
         return self._client.request_consumerkey(self._access_rules, redirect_url)
 
     def add_rule(self, method, path):
-        '''
+        """
         Add a new rule to the request. Will grant the ``(method, path)`` tuple.
         Path can be any API route pattern like ``/sms/*`` or ``/me``. For example,
         to grant RO access on personal data:
 
         >>> ck.add_rule("GET", "/me")
-        '''
-        self._access_rules.append({'method': method.upper(), 'path': path})
+        """
+        self._access_rules.append({"method": method.upper(), "path": path})
 
     def add_rules(self, methods, path):
-        '''
+        """
         Add rules for ``path`` pattern, for each methods in ``methods``. This is
         a convenient helper over ``add_rule``. For example, this could be used
         to grant all access on the API at once:
-        
+
         >>> ck.add_rules(["GET", "POST", "PUT", "DELETE"], "/*")
-        '''
+        """
         for method in methods:
             self.add_rule(method, path)
 
     def add_recursive_rules(self, methods, path):
-        '''
+        """
         Use this method to grant access on a full API tree. This is the
         recommended way to grant access in the API. It will take care of granted
         the root call *AND* sub-calls for you. Which is commonly forgotten...
         For example, to grant a full access on ``/sms``:
 
         >>> ck.add_recursive_rules(["GET", "POST", "PUT", "DELETE"], "/sms")
-        '''
-        path = path.rstrip('*/ ')
+        """
+        path = path.rstrip("*/ ")
         if path:
             self.add_rules(methods, path)
-        self.add_rules(methods, path+'/*')
-
+        self.add_rules(methods, path + "/*")
```

### Comparing `ovh-1.0.0/ovh/exceptions.py` & `ovh-1.1.0/ovh/exceptions.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -26,64 +24,80 @@
 # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 # SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
 """
 All exceptions used in OVH SDK derives from `APIError`
 """
 
+
 class APIError(Exception):
     """Base OVH API exception, all specific exceptions inherits from it."""
+
     def __init__(self, *args, **kwargs):
-        self.response = kwargs.pop('response', None)
+        self.response = kwargs.pop("response", None)
         if self.response is not None:
             self.query_id = self.response.headers.get("X-OVH-QUERYID")
         else:
             self.query_id = None
         super(APIError, self).__init__(*args, **kwargs)
 
     def __str__(self):
-        if self.query_id: # pragma: no cover
+        if self.query_id:  # pragma: no cover
             return "{} \nOVH-Query-ID: {}".format(super(APIError, self).__str__(), self.query_id)
-        else: # pragma: no cover
+        else:  # pragma: no cover
             return super(APIError, self).__str__()
 
+
 class HTTPError(APIError):
     """Raised when the request fails at a low level (DNS, network, ...)"""
 
+
 class InvalidKey(APIError):
     """Raised when trying to sign request with invalid key"""
 
+
 class InvalidCredential(APIError):
     """Raised when trying to sign request with invalid consumer key"""
 
+
 class InvalidResponse(APIError):
     """Raised when api response is not valid json"""
 
+
 class InvalidRegion(APIError):
     """Raised when region is not in `REGIONS`."""
 
+
 class ReadOnlyError(APIError):
     """Raised when attempting to modify readonly data."""
 
+
 class ResourceNotFoundError(APIError):
     """Raised when requested resource does not exist."""
 
+
 class BadParametersError(APIError):
     """Raised when request contains bad parameters."""
 
+
 class ResourceConflictError(APIError):
     """Raised when trying to create an already existing resource."""
 
+
 class NetworkError(APIError):
     """Raised when there is an error from network layer."""
 
+
 class NotGrantedCall(APIError):
     """Raised when there is an error from network layer."""
 
+
 class NotCredential(APIError):
     """Raised when there is an error from network layer."""
 
+
 class Forbidden(APIError):
     """Raised when there is an error from network layer."""
 
+
 class ResourceExpiredError(APIError):
     """Raised when requested resource expired."""
```

### Comparing `ovh-1.0.0/ovh.egg-info/PKG-INFO` & `ovh-1.1.0/ovh.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,32 +1,30 @@
 Metadata-Version: 2.1
 Name: ovh
-Version: 1.0.0
+Version: 1.1.0
 Summary: "Official module to perform HTTP requests to the OVHcloud APIs"
 Home-page: https://api.ovh.com
 Author: OVHcloud team - Romain Beuque
 Author-email: api@ml.ovh.net
 License: BSD
 Keywords: ovh,sdk,rest,ovhcloud
-Platform: UNKNOWN
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: Topic :: System :: Archiving :: Packaging
 Provides-Extra: dev
-Provides-Extra: test
 License-File: LICENSE
 
 .. image:: https://github.com/ovh/python-ovh/raw/master/docs/img/logo.png
            :alt: Python & OVH APIs
            :target: https://pypi.python.org/pypi/ovh
 
 Lightweight wrapper around OVHcloud's APIs. Handles all the hard work including
@@ -40,25 +38,23 @@
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/pyversions/ovh.svg
            :alt: PyPi supported Python versions
            :target: https://pypi.python.org/pypi/ovh
 .. image:: https://img.shields.io/pypi/wheel/ovh.svg
            :alt: PyPi Wheel status
            :target: https://pypi.python.org/pypi/ovh
-.. image:: https://travis-ci.org/ovh/python-ovh.svg?branch=master
+.. image:: https://github.com/ovh/python-ovh/actions/workflows/test.yaml/badge.svg?branch=master
            :alt: Build Status
-           :target: https://travis-ci.org/ovh/python-ovh
+           :target: https://github.com/ovh/python-ovh/actions/workflows/test.yaml
 .. image:: https://coveralls.io/repos/github/ovh/python-ovh/badge.svg
            :alt: Coverage Status
            :target: https://coveralls.io/github/ovh/python-ovh
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
     # to get your credentials
     client = ovh.Client(
         endpoint='ovh-eu',
         application_key='<application key>',
@@ -156,15 +152,14 @@
 behalf, you need a **consumer key (CK)**.
 
 Here is a sample code you can use to allow your application to access a
 customer's information:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
 
     # create a client using configuration
     client = ovh.Client()
 
     # Request RO, /me API access
     ck = client.new_consumer_key_request()
@@ -176,15 +171,14 @@
     print("Please visit %s to authenticate" % validation['validationUrl'])
     input("and press Enter to continue...")
 
     # Print nice welcome message
     print("Welcome", client.get('/me')['firstname'])
     print("Btw, your 'consumerKey' is '%s'" % validation['consumerKey'])
 
-
 Returned ``consumerKey`` should then be kept to avoid re-authenticating your
 end-user on each use.
 
 .. note:: To request full and unlimited access to the API, you may use ``add_recursive_rules``:
 
 .. code:: python
 
@@ -202,16 +196,14 @@
 ``from`` keyword. Which is a problem as this is also a reserved Python keyword.
 In this case, simply prefix it with a '_', the wrapper will automatically detect
 it as being a prefixed reserved keyword and will substitute it. Such aliasing
 is only supported with reserved keywords.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     DOMAIN = "example.com"
     SOURCE = "sales@example.com"
     DESTINATION = "contact@example.com"
 
     # create a client
@@ -233,16 +225,14 @@
 of each bill lines using ``/me/bill/{billId}/details/{billDetailId}``.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # Grab bill list
     bills = client.get('/me/bill')
@@ -263,16 +253,14 @@
 manually for each servers. You could take advantage of a code like this.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     # create a client
     client = ovh.Client()
 
     # get list of all server names
     servers = client.get('/dedicated/server/')
@@ -294,16 +282,14 @@
 manage revocation too.
 
 This example assumes an existing Configuration_ with valid ``application_key``,
 ``application_secret`` and ``consumer_key``.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
     from tabulate import tabulate
 
     # create a client
     client = ovh.Client()
 
     credentials = client.get('/me/api/credential', status='validated')
@@ -341,15 +327,14 @@
 particularly useful to tweak the BIOS or troubleshoot boot issues.
 
 Hopefully, this can easily be automated using a simple script. It assumes Java Web Start is
 fully installed on the machine and a consumer key allowed on the server exists.
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
     import ovh
     import sys
     import time
     import tempfile
     import subprocess
 
     # check arguments
@@ -449,41 +434,63 @@
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client()
 
+Use v1 and v2 API versions
+--------------------------
+
+When using OVHcloud APIs (not So you Start or Kimsufi ones), you are given the
+opportunity to aim for two API versions. For the European API, for example:
+
+- the v1 is reachable through https://eu.api.ovh.com/v1
+- the v2 is reachable through https://eu.api.ovh.com/v2
+- the legacy URL is https://eu.api.ovh.com/1.0
+
+ Calling ``client.get``, you can target the API version you want:
+
+.. code:: python
+
+    client = ovh.Client(endpoint="ovh-eu")
+
+    # Call to https://eu.api.ovh.com/v1/xdsl/xdsl-yourservice
+    client.get("/v1/xdsl/xdsl-yourservice")
+
+    # Call to https://eu.api.ovh.com/v2/xdsl/xdsl-yourservice
+    client.get("/v2/xdsl/xdsl-yourservice")
+
+    # Legacy call to https://eu.api.ovh.com/1.0/xdsl/xdsl-yourservice
+    client.get("/xdsl/xdsl-yourservice")
+
 Custom configuration file
 -------------------------
 
 You can also specify a custom configuration file. With this method, you won't be able to inherit values from environment.
 
 Example usage:
 
 .. code:: python
 
     client = ovh.Client(config_file='/my/config.conf')
 
-
 Passing parameters
 ==================
 
 You can call all the methods of the API with the necessary arguments.
 
 If an API needs an argument colliding with a Python reserved keyword, it
 can be prefixed with an underscore. For example, ``from`` argument of
 ``POST /email/domain/{domain}/redirection`` may be replaced by ``_from``.
 
 With characters invalid in python argument name like a dot, you can:
 
 .. code:: python
 
-    # -*- encoding: utf-8 -*-
-
     import ovh
 
     params = {}
     params['date.from'] = '2014-01-01'
     params['date.to'] = '2015-01-01'
 
     # create a client
@@ -532,29 +539,28 @@
 
 .. code:: bash
 
     git clone https://github.com/ovh/python-ovh.git
     cd python-ovh
     python setup.py develop
 
-You've developed a new cool feature ? Fixed an annoying bug ? We'd be happy
-to hear from you !
+You've developed a new cool feature? Fixed an annoying bug? We'd be happy
+to hear from you!
 
 Run the tests
 -------------
 
-Simply run ``nosetests``. It will automatically load its configuration from
+Simply run ``pytest``. It will automatically load its configuration from
 ``setup.cfg`` and output full coverage status. Since we all love quality, please
 note that we do not accept contributions with test coverage under 100%.
 
 .. code:: bash
 
     pip install -e .[dev]
-    nosetests # 100% coverage is a hard minimum
-
+    pytest
 
 Build the documentation
 -----------------------
 
 Documentation is managed using the excellent ``Sphinx`` system. For example, to
 build HTML documentation:
 
@@ -635,9 +641,7 @@
 - **Report bugs**: https://github.com/ovh/python-ovh/issues
 - **Download**: http://pypi.python.org/pypi/ovh
 
 License
 =======
 
 3-Clause BSD
-
-
```

### Comparing `ovh-1.0.0/ovh.egg-info/SOURCES.txt` & `ovh-1.1.0/ovh.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 CONTRIBUTING.rst
 LICENSE
 MANIFEST.in
 MIGRATION.rst
 README.rst
+pyproject.toml
 setup.cfg
 setup.py
 docs/Makefile
 docs/conf.py
 docs/index.rst
 docs/make.bat
 docs/api/ovh/client.rst
```

### Comparing `ovh-1.0.0/setup.cfg` & `ovh-1.1.0/setup.cfg`

 * *Files 15% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 [metadata]
 name = ovh
 description = "Official module to perform HTTP requests to the OVHcloud APIs"
 long_description = file: README.rst
-version = 1.0.0
+version = 1.1.0
 author = OVHcloud team - Romain Beuque
 author_email = api@ml.ovh.net
 url = https://api.ovh.com
 license = BSD
 license_file = LICENSE
 keywords = ovh, sdk, rest, ovhcloud
 classifiers = 
 	License :: OSI Approved :: BSD License
 	Development Status :: 5 - Production/Stable
 	Intended Audience :: Developers
 	Operating System :: OS Independent
 	Programming Language :: Python
 	Programming Language :: Python :: 3
-	Programming Language :: Python :: 3.6
 	Programming Language :: Python :: 3.7
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
+	Programming Language :: Python :: 3.11
 	Topic :: Software Development :: Libraries :: Python Modules
 	Topic :: System :: Archiving :: Packaging
 
 [options]
 packages = find:
 setup_requires = 
 	setuptools>=30.3.0
@@ -34,38 +34,23 @@
 
 [options.packages.find]
 exclude = 
 	tests
 
 [options.extras_require]
 dev = 
-	coverage==5.5
-	mock==1.0.1
-	nose==1.3.3
-	yanc==0.2.4
 	Sphinx==1.2.2
-	coveralls==3.2.0
+	black
+	coverage~=7.2.2
+	flake8
+	isort
+	pytest~=7.2.2
+	pytest-cov==4.0.0
 	setuptools>=30.3.0
 	wheel
-test = 
-	coverage==5.5
-	mock==1.0.1
-	nose==1.3.3
-	yanc==0.2.4
-
-[test]
-test-suite = nose.collector
-
-[nosetests]
-verbosity = 2
-where = tests/
-with-yanc = 1
-with-coverage = 1
-cover-package = ovh
-cover-erase = 1
 
 [bdist_wheel]
 universal = 1
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `ovh-1.0.0/tests/__init__.py` & `ovh-1.1.0/ovh/__init__.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-# -*- encoding: utf-8 -*-
-#
-# Copyright (c) 2013-2018, OVH SAS.
+# Copyright (c) 2013-2023, OVH SAS.
 # All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions are met:
 #
 #  * Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
@@ -21,7 +19,27 @@
 # DISCLAIMED. IN NO EVENT SHALL OVH SAS AND CONTRIBUTORS BE LIABLE FOR ANY
 # DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 # (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 # LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 # ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 # SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
+
+# flake8: noqa
+from .client import Client
+from .consumer_key import API_READ_ONLY, API_READ_WRITE, API_READ_WRITE_SAFE, ConsumerKeyRequest
+from .exceptions import (
+    APIError,
+    BadParametersError,
+    Forbidden,
+    HTTPError,
+    InvalidCredential,
+    InvalidKey,
+    InvalidRegion,
+    InvalidResponse,
+    NetworkError,
+    NotCredential,
+    NotGrantedCall,
+    ReadOnlyError,
+    ResourceConflictError,
+    ResourceNotFoundError,
+)
```

