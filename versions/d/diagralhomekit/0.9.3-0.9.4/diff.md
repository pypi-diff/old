# Comparing `tmp/diagralhomekit-0.9.3.tar.gz` & `tmp/diagralhomekit-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "diagralhomekit-0.9.3.tar", max compression
+gzip compressed data, was "diagralhomekit-0.9.4.tar", max compression
```

## Comparing `diagralhomekit-0.9.3.tar` & `diagralhomekit-0.9.4.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0    21393 2023-04-03 19:32:16.506454 diagralhomekit-0.9.3/LICENSE
--rw-r--r--   0        0        0     3336 2023-04-06 16:01:35.043604 diagralhomekit-0.9.3/README.md
--rw-r--r--   0        0        0      455 2023-04-05 18:45:00.080586 diagralhomekit-0.9.3/diagralhomekit/__init__.py
--rw-r--r--   0        0        0      584 2023-04-06 08:43:32.341564 diagralhomekit-0.9.3/diagralhomekit/__main__.py
--rw-r--r--   0        0        0     2352 2023-04-06 12:46:44.557883 diagralhomekit-0.9.3/diagralhomekit/alarm_system.py
--rw-r--r--   0        0        0     2456 2023-04-06 15:42:16.478616 diagralhomekit-0.9.3/diagralhomekit/config.py
--rw-r--r--   0        0        0    26784 2023-04-06 13:39:56.573598 diagralhomekit-0.9.3/diagralhomekit/diagral.py
--rw-r--r--   0        0        0     6674 2023-04-06 12:23:10.592110 diagralhomekit-0.9.3/diagralhomekit/homekit_alarm.py
--rw-r--r--   0        0        0     4243 2023-04-06 14:01:59.443690 diagralhomekit-0.9.3/diagralhomekit/http_plugin.py
--rw-r--r--   0        0        0     4534 2023-04-06 15:49:37.721542 diagralhomekit-0.9.3/diagralhomekit/main.py
--rw-r--r--   0        0        0     7518 2023-04-06 15:59:40.754133 diagralhomekit-0.9.3/diagralhomekit/meteofrance.py
--rw-r--r--   0        0        0     4452 2023-04-06 15:48:02.383331 diagralhomekit-0.9.3/diagralhomekit/nut.py
--rw-r--r--   0        0        0     8497 2023-04-06 13:39:39.849006 diagralhomekit-0.9.3/diagralhomekit/plex.py
--rw-r--r--   0        0        0     1044 2023-04-06 13:50:15.159321 diagralhomekit-0.9.3/diagralhomekit/plugin.py
--rw-r--r--   0        0        0     2524 2023-04-06 13:38:00.533738 diagralhomekit-0.9.3/diagralhomekit/utils.py
--rw-r--r--   0        0        0      586 2023-04-06 16:10:07.809492 diagralhomekit-0.9.3/pyproject.toml
--rw-r--r--   0        0        0     4423 1970-01-01 00:00:00.000000 diagralhomekit-0.9.3/setup.py
--rw-r--r--   0        0        0     4215 1970-01-01 00:00:00.000000 diagralhomekit-0.9.3/PKG-INFO
+-rw-r--r--   0        0        0    21393 2023-04-03 19:32:16.506454 diagralhomekit-0.9.4/LICENSE
+-rw-r--r--   0        0        0     3336 2023-04-06 16:01:35.043604 diagralhomekit-0.9.4/README.md
+-rw-r--r--   0        0        0      455 2023-04-05 18:45:00.080586 diagralhomekit-0.9.4/diagralhomekit/__init__.py
+-rw-r--r--   0        0        0      584 2023-04-06 08:43:32.341564 diagralhomekit-0.9.4/diagralhomekit/__main__.py
+-rw-r--r--   0        0        0     2352 2023-04-06 12:46:44.557883 diagralhomekit-0.9.4/diagralhomekit/alarm_system.py
+-rw-r--r--   0        0        0     2456 2023-04-06 15:42:16.478616 diagralhomekit-0.9.4/diagralhomekit/config.py
+-rw-r--r--   0        0        0    26793 2023-04-06 16:34:03.553032 diagralhomekit-0.9.4/diagralhomekit/diagral.py
+-rw-r--r--   0        0        0     6674 2023-04-06 12:23:10.592110 diagralhomekit-0.9.4/diagralhomekit/homekit_alarm.py
+-rw-r--r--   0        0        0     4243 2023-04-06 14:01:59.443690 diagralhomekit-0.9.4/diagralhomekit/http_plugin.py
+-rw-r--r--   0        0        0     4530 2023-04-06 16:35:35.719387 diagralhomekit-0.9.4/diagralhomekit/main.py
+-rw-r--r--   0        0        0     7518 2023-04-06 15:59:40.754133 diagralhomekit-0.9.4/diagralhomekit/meteofrance.py
+-rw-r--r--   0        0        0     4452 2023-04-06 15:48:02.383331 diagralhomekit-0.9.4/diagralhomekit/nut.py
+-rw-r--r--   0        0        0     8497 2023-04-06 13:39:39.849006 diagralhomekit-0.9.4/diagralhomekit/plex.py
+-rw-r--r--   0        0        0     1044 2023-04-06 13:50:15.159321 diagralhomekit-0.9.4/diagralhomekit/plugin.py
+-rw-r--r--   0        0        0     2524 2023-04-06 13:38:00.533738 diagralhomekit-0.9.4/diagralhomekit/utils.py
+-rw-r--r--   0        0        0      586 2023-04-06 16:36:40.140629 diagralhomekit-0.9.4/pyproject.toml
+-rw-r--r--   0        0        0     4423 1970-01-01 00:00:00.000000 diagralhomekit-0.9.4/setup.py
+-rw-r--r--   0        0        0     4215 1970-01-01 00:00:00.000000 diagralhomekit-0.9.4/PKG-INFO
```

### Comparing `diagralhomekit-0.9.3/LICENSE` & `diagralhomekit-0.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/README.md` & `diagralhomekit-0.9.4/README.md`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/__main__.py` & `diagralhomekit-0.9.4/diagralhomekit/__main__.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/alarm_system.py` & `diagralhomekit-0.9.4/diagralhomekit/alarm_system.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/config.py` & `diagralhomekit-0.9.4/diagralhomekit/config.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/diagral.py` & `diagralhomekit-0.9.4/diagralhomekit/diagral.py`

 * *Files 0% similar despite different names*

```diff
@@ -512,15 +512,15 @@
         for system in self.alarm_systems.values():
             if line.endswith(system.internal_name + " : Alarme"):
                 logger.debug(
                     f"Alarm triggered for {system.name}.",
                     extra=self.extra_log_data(action="imap", detail="alarm"),
                 )
                 system.is_triggered = True
-                system.trigger_date = datetime.datetime.now(tz=datetime.UTC)
+                system.trigger_date = datetime.datetime.now(tz=datetime.timezone.utc)
 
     def update_all_systems(self):
         """Update all system with a few requests."""
         with self.request_lock:
             self.do_login()
             for system in self.alarm_systems.values():
                 try:
```

### Comparing `diagralhomekit-0.9.3/diagralhomekit/homekit_alarm.py` & `diagralhomekit-0.9.4/diagralhomekit/homekit_alarm.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/http_plugin.py` & `diagralhomekit-0.9.4/diagralhomekit/http_plugin.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/main.py` & `diagralhomekit-0.9.4/diagralhomekit/main.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,26 +1,28 @@
 # ##############################################################################
 #  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
 #  This file main.py is part of DiagralHomekit.                                #
 #  Please check the LICENSE file for sharing or distribution permissions.      #
 # ##############################################################################
 """All the main functions."""
-from multiprocessing import Queue
-
 import argparse
 import logging
 import os
 import pathlib
-import sentry_sdk
 import signal
 import sys
 import urllib.parse
+from multiprocessing import Queue
+
+import sentry_sdk
 from logging_loki import LokiQueueHandler, emitter
+
 # noinspection PyPackageRequirements
 from pyhap.accessory import Bridge
+
 # noinspection PyPackageRequirements
 from pyhap.accessory_driver import AccessoryDriver
 
 from diagralhomekit.config import HomekitConfig
 from diagralhomekit.diagral import DiagralHomekitPlugin
 
 logger = logging.getLogger("diagralhomekit")
@@ -98,17 +100,15 @@
     run_daemons(
         config_dir,
         listen_port,
         log_requests=args.verbosity >= 3,
     )
 
 
-def run_daemons(
-    config_dir, listen_port, log_requests: bool = False
-):
+def run_daemons(config_dir, listen_port, log_requests: bool = False):
     """launch all processes: Homekit and Diagral checker."""
     persist_file = config_dir / "persist.json"
     config_file = config_dir / "config.ini"
     logger.info(f"configuration file: {config_file}")
     logger.info(f"persistence file: {persist_file}")
     logger.info(f"listen port: {listen_port}")
```

### Comparing `diagralhomekit-0.9.3/diagralhomekit/meteofrance.py` & `diagralhomekit-0.9.4/diagralhomekit/meteofrance.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/nut.py` & `diagralhomekit-0.9.4/diagralhomekit/nut.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/plex.py` & `diagralhomekit-0.9.4/diagralhomekit/plex.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/plugin.py` & `diagralhomekit-0.9.4/diagralhomekit/plugin.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/diagralhomekit/utils.py` & `diagralhomekit-0.9.4/diagralhomekit/utils.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.9.3/pyproject.toml` & `diagralhomekit-0.9.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 [tool.poetry]
 authors = ["d9pouces <github@19pouces.net>"]
 description = "Apple HomeKit integration for Diagral alarm systems"
 license = "CeCILL-B"
 name = "diagralhomekit"
 readme = "README.md"
-version = "0.9.3"
+version = "0.9.4"
 
 [tool.poetry.dependencies]
 HAP-python = "^4.6.0"
 base36 = "^0.1.1"
 meteofrance-api = "^1.2.0"
 nut2 = "^2.1.1"
 pyqrcode = "^1.2.1"
```

### Comparing `diagralhomekit-0.9.3/setup.py` & `diagralhomekit-0.9.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,15 +18,15 @@
  'sentry-sdk>=1.18.0,<2.0.0']
 
 entry_points = \
 {'console_scripts': ['diagral-homekit = diagralhomekit.main:main']}
 
 setup_kwargs = {
     'name': 'diagralhomekit',
-    'version': '0.9.3',
+    'version': '0.9.4',
     'description': 'Apple HomeKit integration for Diagral alarm systems',
     'long_description': "DiagralHomekit\n==============\n\n[![PyPI version](https://badge.fury.io/py/diagralhomekit.svg)](https://badge.fury.io/py/diagralhomekit)\n\nAllow to control your Diagral alarm systems through Apple Homekit.\n\n\nFirst, you need to create a configuration file `~/.diagralhomekit/config.ini` with connection details for all Diagral systems.\n\n```ini\n[diagral:Home]\nname=[an explicit name for this system]\nlogin=[email address of the Diagral account]\npassword=[password for the Diagral account]\nimap_login=[IMAP login for the email address receiving alarm alerts]\nimap_password=[IMAP password]\nimap_hostname=[IMAP server]\nimap_port=[IMAP port]\nimap_use_tls=[true/1/on if you use SSL for the IMAP connection]\nmaster_code=[a Diagral master code, able to arm or disarm the alarm]\nsystem_id=[system id — see below]\ntransmitter_id=[transmitter id — see below]\ncentral_id=[central id — see below]\n\n```\n`system_id`, `transmitter_id` and `central_id` can be retrieved with the following command, that prepares a configuration file:\n\n```bash\npython3 -m diagralhomekit --config-dir ~/.diagralhomekit --create-config 'diagral@account.com:password'\n```\n\nThen you can run the script:\n\n```bash\npython3 -m diagralhomekit --port 6666 --config-dir ~/.diagralhomekit -v 2\n```\nOn the first launch, a QR code is displayed and can be scanned in Homekit, like any Homekit-compatible device.\n\n\nYou can send logs to [Loki](https://grafana.com/oss/loki/) with `--loki-url=https://username:password@my.loki.server/loki/api/v1/push`.\nYou can also send alerts to [Sentry](https://sentry.io/) with `--sentry-dsn=my_sentry_dsn`.\n\nEverything can be configured by environment variables instead of arguments:\n\n```bash\nDIAGRAL_PORT=6666\nDIAGRAL_CONFIG=/etc/diagralhomekit\nDIAGRAL_SENTRY_DSN=https://sentry_dsn@sentry.io/42\nDIAGRAL_LOKI_URL=https://username:password@my.loki.server/loki/api/v1/push\nDIAGRAL_VERBOSITY=1\n```\n\n\n**As many sensitive data must be stored in this configuration file, so you should create a dedicated email address and Diagral account.**\n\n\nPlex sensor\n-----------\n\nA presence can be detected when a specified Plex player is playing something:\n```ini\n[plex:appletv_web]\nserver_token=[authentication token]\nserver_url=[url of your Plex server]\nplayer_name=[Displayed name for the player]\nplayer_device=None,\nplayer_product=[Product name of the targeted player]\nplayer_title=[Title of the targeted player]\nplayer_address=[IP address of the targeted player]\n```\nOnly one of the last four properties is required to match with the targeted player.\nTo get actual property values, you can use `curl`:\n\n```bash\ncurl -H Accept:application/json -H X-Plex-Token:[authentication token] [url of your Plex server]/status/sessions\n```\n\nHTTP monitoring\n---------------\n\nYou can monitor some websites, as air purifier sensors (no Homekit sensor is available for HTTP monitoring…):\n```ini\n[internet:website]\nurl=[url to check]\nname=[Displayed name]\n```\n\nWeather monitoring\n------------------\n\nYou can monitor weather, and emulate a presence when it will rain in the next 10 minutes:\n\n```ini\n[meteofrance:paris]\nname=Paris\nlatitude=48.866667\nlongitude=2.333333\ncountry=FR\nregion=Île-de-France\n```\n\nUPS monitoring\n--------------\n\nUPS can also be monitoring, as soon as NUT is locally installed (standard UPS monitoring server on Linux.\n```\n[ups:home]\nname=eaton650\n```\n",
     'author': 'd9pouces',
     'author_email': 'github@19pouces.net',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `diagralhomekit-0.9.3/PKG-INFO` & `diagralhomekit-0.9.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: diagralhomekit
-Version: 0.9.3
+Version: 0.9.4
 Summary: Apple HomeKit integration for Diagral alarm systems
 License: CECILL-B
 Author: d9pouces
 Author-email: github@19pouces.net
 Requires-Python: >=3.9,<4.0
 Classifier: License :: CeCILL-B Free Software License Agreement (CECILL-B)
 Classifier: Programming Language :: Python :: 3
```

