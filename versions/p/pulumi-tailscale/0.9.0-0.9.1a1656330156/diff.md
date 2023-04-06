# Comparing `tmp/pulumi_tailscale-0.9.0.tar.gz` & `tmp/pulumi_tailscale-0.9.1a1656330156.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pulumi_tailscale-0.9.0.tar", last modified: Mon Jun 13 10:50:17 2022, max compression
+gzip compressed data, was "dist/pulumi_tailscale-0.9.1a1656330156.tar", last modified: Mon Jun 27 11:45:39 2022, max compression
```

## Comparing `pulumi_tailscale-0.9.0.tar` & `pulumi_tailscale-0.9.1a1656330156.tar`

### file list

```diff
@@ -1,33 +1,33 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/
--rw-r--r--   0 runner    (1001) docker     (121)     3219 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2406 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/
--rw-r--r--   0 runner    (1001) docker     (121)     2588 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7667 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/_utilities.py
--rw-r--r--   0 runner    (1001) docker     (121)     6543 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/acl.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/config/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1170 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/config/vars.py
--rw-r--r--   0 runner    (1001) docker     (121)     8632 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/device_authorization.py
--rw-r--r--   0 runner    (1001) docker     (121)     8707 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/device_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     9108 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/device_subnet_routes.py
--rw-r--r--   0 runner    (1001) docker     (121)     8351 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/device_tags.py
--rw-r--r--   0 runner    (1001) docker     (121)     7317 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/dns_nameservers.py
--rw-r--r--   0 runner    (1001) docker     (121)     6361 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/dns_preferences.py
--rw-r--r--   0 runner    (1001) docker     (121)     7098 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/dns_search_paths.py
--rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/get_device.py
--rw-r--r--   0 runner    (1001) docker     (121)     3296 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/get_devices.py
--rw-r--r--   0 runner    (1001) docker     (121)     1381 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/outputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     7607 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/provider.py
--rw-r--r--   0 runner    (1001) docker     (121)       46 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/pulumi-plugin.json
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/py.typed
--rw-r--r--   0 runner    (1001) docker     (121)    13737 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale/tailnet_key.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3219 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      876 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2108 2022-06-13 10:50:17.000000 pulumi_tailscale-0.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/
+-rw-r--r--   0 runner    (1001) docker     (121)     3230 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2406 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/
+-rw-r--r--   0 runner    (1001) docker     (121)     2588 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7667 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6543 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/acl.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/config/
+-rw-r--r--   0 runner    (1001) docker     (121)      285 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1170 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/config/vars.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8632 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_authorization.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8707 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9108 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_subnet_routes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8351 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_tags.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7317 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_nameservers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6361 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_preferences.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7098 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_search_paths.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/get_device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3296 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/get_devices.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1381 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7607 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/provider.py
+-rw-r--r--   0 runner    (1001) docker     (121)       46 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/pulumi-plugin.json
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/py.typed
+-rw-r--r--   0 runner    (1001) docker     (121)    13737 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/tailnet_key.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3230 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      876 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       17 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2145 2022-06-27 11:45:39.000000 pulumi_tailscale-0.9.1a1656330156/setup.py
```

### Comparing `pulumi_tailscale-0.9.0/PKG-INFO` & `pulumi_tailscale-0.9.1a1656330156/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_tailscale
-Version: 0.9.0
+Version: 0.9.1a1656330156
 Summary: A Pulumi package for creating and managing xyz cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-tailscale
 Description: [![Actions Status](https://github.com/pulumi/pulumi-tailscale/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-tailscale/actions)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Ftailscale.svg)](https://www.npmjs.com/package/@pulumi/tailscale)
```

### Comparing `pulumi_tailscale-0.9.0/README.md` & `pulumi_tailscale-0.9.1a1656330156/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/__init__.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/__init__.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/_utilities.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/_utilities.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/acl.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/acl.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/config/vars.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/config/vars.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/device_authorization.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_authorization.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/device_key.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/device_subnet_routes.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_subnet_routes.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/device_tags.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/device_tags.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/dns_nameservers.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_nameservers.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/dns_preferences.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_preferences.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/dns_search_paths.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/dns_search_paths.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/get_device.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/get_device.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/get_devices.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/get_devices.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/outputs.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/provider.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale/tailnet_key.py` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale/tailnet_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/PKG-INFO` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-tailscale
-Version: 0.9.0
+Version: 0.9.1a1656330156
 Summary: A Pulumi package for creating and managing xyz cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-tailscale
 Description: [![Actions Status](https://github.com/pulumi/pulumi-tailscale/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-tailscale/actions)
         [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
         [![NPM version](https://badge.fury.io/js/%40pulumi%2Ftailscale.svg)](https://www.npmjs.com/package/@pulumi/tailscale)
```

### Comparing `pulumi_tailscale-0.9.0/pulumi_tailscale.egg-info/SOURCES.txt` & `pulumi_tailscale-0.9.1a1656330156/pulumi_tailscale.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pulumi_tailscale-0.9.0/setup.py` & `pulumi_tailscale-0.9.1a1656330156/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "0.9.0"
-PLUGIN_VERSION = "0.9.0"
+VERSION = "0.9.1a1656330156"
+PLUGIN_VERSION = "0.9.1-alpha.1656330156+1b781cf6"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'tailscale', PLUGIN_VERSION])
         except OSError as error:
```

