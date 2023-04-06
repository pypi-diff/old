# Comparing `tmp/certbot-dns-e2econfig-0.4.5.tar.gz` & `tmp/certbot-dns-e2econfig-0.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "certbot-dns-e2econfig-0.4.5.tar", last modified: Thu Apr  6 08:56:26 2023, max compression
+gzip compressed data, was "certbot-dns-e2econfig-0.4.6.tar", last modified: Thu Apr  6 09:15:14 2023, max compression
```

## Comparing `certbot-dns-e2econfig-0.4.5.tar` & `certbot-dns-e2econfig-0.4.6.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 08:56:26.432116 certbot-dns-e2econfig-0.4.5/
--rw-r--r--   0 abhaybhati   (501) staff       (20)    10786 2023-04-03 06:46:44.000000 certbot-dns-e2econfig-0.4.5/LICENSE.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)     7200 2023-04-06 08:56:26.432208 certbot-dns-e2econfig-0.4.5/PKG-INFO
--rw-r--r--   0 abhaybhati   (501) staff       (20)     4898 2023-04-03 06:46:44.000000 certbot-dns-e2econfig-0.4.5/README.rst
-drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 08:56:26.431255 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig/
--rw-r--r--   0 abhaybhati   (501) staff       (20)     3271 2023-04-05 12:55:09.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig/__init__.py
--rw-r--r--   0 abhaybhati   (501) staff       (20)     8536 2023-04-06 08:54:49.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig/dns_e2econfig.py
-drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 08:56:26.432024 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/
--rw-r--r--   0 abhaybhati   (501) staff       (20)     7200 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/PKG-INFO
--rw-r--r--   0 abhaybhati   (501) staff       (20)      386 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/SOURCES.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)        1 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/dependency_links.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)       85 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/entry_points.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)       79 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/requires.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)       22 2023-04-06 08:56:26.000000 certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/top_level.txt
--rw-r--r--   0 abhaybhati   (501) staff       (20)       67 2023-04-06 08:56:26.432420 certbot-dns-e2econfig-0.4.5/setup.cfg
--rw-r--r--   0 abhaybhati   (501) staff       (20)     1994 2023-04-06 08:55:00.000000 certbot-dns-e2econfig-0.4.5/setup.py
+drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 09:15:14.676818 certbot-dns-e2econfig-0.4.6/
+-rw-r--r--   0 abhaybhati   (501) staff       (20)    10786 2023-04-03 06:46:44.000000 certbot-dns-e2econfig-0.4.6/LICENSE.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     7200 2023-04-06 09:15:14.676916 certbot-dns-e2econfig-0.4.6/PKG-INFO
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     4898 2023-04-03 06:46:44.000000 certbot-dns-e2econfig-0.4.6/README.rst
+drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 09:15:14.675984 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig/
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     3271 2023-04-05 12:55:09.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig/__init__.py
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     8638 2023-04-06 09:14:40.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig/dns_e2econfig.py
+drwxr-xr-x   0 abhaybhati   (501) staff       (20)        0 2023-04-06 09:15:14.676697 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     7200 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/PKG-INFO
+-rw-r--r--   0 abhaybhati   (501) staff       (20)      386 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/SOURCES.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)        1 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/dependency_links.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)       85 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/entry_points.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)       79 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/requires.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)       22 2023-04-06 09:15:14.000000 certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/top_level.txt
+-rw-r--r--   0 abhaybhati   (501) staff       (20)       67 2023-04-06 09:15:14.677141 certbot-dns-e2econfig-0.4.6/setup.cfg
+-rw-r--r--   0 abhaybhati   (501) staff       (20)     1994 2023-04-06 09:14:46.000000 certbot-dns-e2econfig-0.4.6/setup.py
```

### Comparing `certbot-dns-e2econfig-0.4.5/LICENSE.txt` & `certbot-dns-e2econfig-0.4.6/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `certbot-dns-e2econfig-0.4.5/PKG-INFO` & `certbot-dns-e2econfig-0.4.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: certbot-dns-e2econfig
-Version: 0.4.5
+Version: 0.4.6
 Summary: E2E DNS Authenticator plugin for Certbot
 Home-page: UNKNOWN
 Author: Abhay Bhati
 Author-email: abhaybhati987@gmail.com
 License: Apache License 2.0
 Description: certbot-dns-ispconfig
         =====================
```

### Comparing `certbot-dns-e2econfig-0.4.5/README.rst` & `certbot-dns-e2econfig-0.4.6/README.rst`

 * *Files identical despite different names*

### Comparing `certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig/__init__.py` & `certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig/__init__.py`

 * *Files identical despite different names*

### Comparing `certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig/dns_e2econfig.py` & `certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig/dns_e2econfig.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 import json
 import logging
 import time
 import requests
 
 from e2e_client.manager import Manager
 from e2e_client.domain import Domain
+from e2e_client.exceptions import TokenException, DomainException
 from certbot import errors
 from certbot.plugins import dns_common
 
 logger = logging.getLogger(__name__)
 
 
 class Authenticator(dns_common.DNSAuthenticator):
@@ -88,30 +89,30 @@
         """
         if not domain.endswith('.'):
             domain += '.'
         record_content = '"' + record_content + '"'   
         record_name = record_name + '.' 
         try:
             Manager(api_key=self.api_key, api_token=self.api_token).check_token()
-        except:
+        except TokenException as e:
             hint = 'Did you provide a valid API token?'  
             
             logger.debug('Error finding domain using the e2e_client API')
             raise errors.PluginError('Error finding domain using the e2e_client API: {0}'
-                                     .format(hint))
+                                     .format(e))
 
         try:
             Domain(domain_name=domain, zone_name=domain, record_name=record_name, record_ttl=record_ttl, record_type='TXT', content=record_content, api_key=self.api_key, api_token=self.api_token).check_domain_valid()
             self._find_managed_zone_id(domain_name=domain, zone_name=domain, record_name=record_name, record_ttl=record_ttl, record_type='TXT', content=record_content, api_key=self.api_key, api_token=self.api_token)
-        except:
+        except DomainException as e: 
             hint = 'Did you provide a correct Domain Name?'  
             
             logger.debug('Error finding domain using the e2e_client API')
             raise errors.PluginError('Error finding domain using the e2e_client API: {0}'
-                                     .format(hint)) 
+                                     .format(e)) 
 
         try:
             result = Domain(domain_name=domain, zone_name=domain, record_name=record_name, record_ttl=record_ttl, record_type='TXT', content=f'{record_content}', api_key=self.api_key, api_token=self.api_token).add_record() 
             result_message = result['message']
             logger.debug('Successfully added TXT record with id: %s', result_message)
         except:
             logger.debug('Error adding TXT record using the e2e_client API')
```

### Comparing `certbot-dns-e2econfig-0.4.5/certbot_dns_e2econfig.egg-info/PKG-INFO` & `certbot-dns-e2econfig-0.4.6/certbot_dns_e2econfig.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: certbot-dns-e2econfig
-Version: 0.4.5
+Version: 0.4.6
 Summary: E2E DNS Authenticator plugin for Certbot
 Home-page: UNKNOWN
 Author: Abhay Bhati
 Author-email: abhaybhati987@gmail.com
 License: Apache License 2.0
 Description: certbot-dns-ispconfig
         =====================
```

### Comparing `certbot-dns-e2econfig-0.4.5/setup.py` & `certbot-dns-e2econfig-0.4.6/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from setuptools import setup
 from setuptools import find_packages
 
-version = "0.4.5"
+version = "0.4.6"
 install_requires = [
     "acme>=0.29.0",
     "certbot>=0.34.0",
     "setuptools",
     "requests",
     "mock",
     "requests-mock",
```

