# Comparing `tmp/diagralhomekit-0.1.0.tar.gz` & `tmp/diagralhomekit-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "diagralhomekit-0.1.0.tar", max compression
+gzip compressed data, was "diagralhomekit-0.9.3.tar", max compression
```

## Comparing `diagralhomekit-0.1.0.tar` & `diagralhomekit-0.9.3.tar`

### file list

```diff
@@ -1,12 +1,18 @@
--rw-r--r--   0        0        0    21393 2023-04-03 19:32:16.506454 diagralhomekit-0.1.0/LICENSE
--rw-r--r--   0        0        0     1661 2023-04-06 07:23:17.536701 diagralhomekit-0.1.0/README.md
--rw-r--r--   0        0        0      455 2023-04-05 18:45:00.080586 diagralhomekit-0.1.0/diagralhomekit/__init__.py
--rw-r--r--   0        0        0      584 2023-04-06 08:43:32.341564 diagralhomekit-0.1.0/diagralhomekit/__main__.py
--rw-r--r--   0        0        0     2353 2023-04-05 20:21:20.761710 diagralhomekit-0.1.0/diagralhomekit/alarm_system.py
--rw-r--r--   0        0        0    26378 2023-04-06 08:37:56.989496 diagralhomekit-0.1.0/diagralhomekit/diagral_config.py
--rw-r--r--   0        0        0     6674 2023-04-06 07:43:06.047521 diagralhomekit-0.1.0/diagralhomekit/homekit.py
--rw-r--r--   0        0        0     4512 2023-04-06 08:43:32.344283 diagralhomekit-0.1.0/diagralhomekit/main.py
--rw-r--r--   0        0        0     2331 2023-04-06 08:37:13.227691 diagralhomekit-0.1.0/diagralhomekit/utils.py
--rw-r--r--   0        0        0      543 2023-04-06 08:44:18.955658 diagralhomekit-0.1.0/pyproject.toml
--rw-r--r--   0        0        0     2623 1970-01-01 00:00:00.000000 diagralhomekit-0.1.0/setup.py
--rw-r--r--   0        0        0     2455 1970-01-01 00:00:00.000000 diagralhomekit-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0    21393 2023-04-03 19:32:16.506454 diagralhomekit-0.9.3/LICENSE
+-rw-r--r--   0        0        0     3336 2023-04-06 16:01:35.043604 diagralhomekit-0.9.3/README.md
+-rw-r--r--   0        0        0      455 2023-04-05 18:45:00.080586 diagralhomekit-0.9.3/diagralhomekit/__init__.py
+-rw-r--r--   0        0        0      584 2023-04-06 08:43:32.341564 diagralhomekit-0.9.3/diagralhomekit/__main__.py
+-rw-r--r--   0        0        0     2352 2023-04-06 12:46:44.557883 diagralhomekit-0.9.3/diagralhomekit/alarm_system.py
+-rw-r--r--   0        0        0     2456 2023-04-06 15:42:16.478616 diagralhomekit-0.9.3/diagralhomekit/config.py
+-rw-r--r--   0        0        0    26784 2023-04-06 13:39:56.573598 diagralhomekit-0.9.3/diagralhomekit/diagral.py
+-rw-r--r--   0        0        0     6674 2023-04-06 12:23:10.592110 diagralhomekit-0.9.3/diagralhomekit/homekit_alarm.py
+-rw-r--r--   0        0        0     4243 2023-04-06 14:01:59.443690 diagralhomekit-0.9.3/diagralhomekit/http_plugin.py
+-rw-r--r--   0        0        0     4534 2023-04-06 15:49:37.721542 diagralhomekit-0.9.3/diagralhomekit/main.py
+-rw-r--r--   0        0        0     7518 2023-04-06 15:59:40.754133 diagralhomekit-0.9.3/diagralhomekit/meteofrance.py
+-rw-r--r--   0        0        0     4452 2023-04-06 15:48:02.383331 diagralhomekit-0.9.3/diagralhomekit/nut.py
+-rw-r--r--   0        0        0     8497 2023-04-06 13:39:39.849006 diagralhomekit-0.9.3/diagralhomekit/plex.py
+-rw-r--r--   0        0        0     1044 2023-04-06 13:50:15.159321 diagralhomekit-0.9.3/diagralhomekit/plugin.py
+-rw-r--r--   0        0        0     2524 2023-04-06 13:38:00.533738 diagralhomekit-0.9.3/diagralhomekit/utils.py
+-rw-r--r--   0        0        0      586 2023-04-06 16:10:07.809492 diagralhomekit-0.9.3/pyproject.toml
+-rw-r--r--   0        0        0     4423 1970-01-01 00:00:00.000000 diagralhomekit-0.9.3/setup.py
+-rw-r--r--   0        0        0     4215 1970-01-01 00:00:00.000000 diagralhomekit-0.9.3/PKG-INFO
```

### Comparing `diagralhomekit-0.1.0/LICENSE` & `diagralhomekit-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.1.0/diagralhomekit/__main__.py` & `diagralhomekit-0.9.3/diagralhomekit/__main__.py`

 * *Files identical despite different names*

### Comparing `diagralhomekit-0.1.0/diagralhomekit/alarm_system.py` & `diagralhomekit-0.9.3/diagralhomekit/alarm_system.py`

 * *Files 0% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 
     def extra_log_data(self, **kwargs):
         """Extra data for logging events."""
         return {
             "tags": {
                 "identifier": str(self.identifier),
                 "name": self.name,
-                "type": "system",
+                "type": "alarm",
                 **kwargs,
             }
         }
 
     @property
     def identifier(self) -> int:
         """return a unique identifier."""
```

### Comparing `diagralhomekit-0.1.0/diagralhomekit/diagral_config.py` & `diagralhomekit-0.9.3/diagralhomekit/diagral.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,30 +1,32 @@
 # ##############################################################################
 #  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
-#  This file diagral_config.py is part of DiagralHomekit.                      #
+#  This file diagral.py is part of DiagralHomekit.                             #
 #  Please check the LICENSE file for sharing or distribution permissions.      #
 # ##############################################################################
 """A Diagral config."""
 import configparser
 import datetime
 import email.header
 import imaplib
 import io
 import logging
-import pathlib
 import re
 import time
 from multiprocessing.pool import ThreadPool
 from threading import Lock
 from typing import Dict, Optional, Set, Tuple
 
 import requests
 from sentry_sdk import capture_exception
 
 from diagralhomekit.alarm_system import AlarmSystem
+from diagralhomekit.config import HomekitConfig
+from diagralhomekit.homekit_alarm import HomekitAlarm
+from diagralhomekit.plugin import HomekitPlugin
 from diagralhomekit.utils import (
     RegexValidator,
     bool_validator,
     capture_some_exception,
     slugify,
 )
 
@@ -261,15 +263,15 @@
 
 
 class DiagralAccount:
     """Represent a Diagral account."""
 
     def __init__(self, config, login: str, password: str):
         """init function."""
-        self.config: DiagralConfig = config
+        self.config: HomekitConfig = config
         self.login = login
         self.password = password
         self.alarm_systems: Dict[int, DiagralAlarmSystem] = {}
         self.session_id = None
         self.diagral_id = None
 
         self.imap_login = ""
@@ -285,45 +287,23 @@
 
     def __str__(self):
         """Return a string."""
         return f"DiagralAccount('{self.login})"
 
     def extra_log_data(self, **kwargs):
         """Extra data for logging events."""
-        return {"tags": {"identifier": self.login, "type": "account", **kwargs}}
-
-    @classmethod
-    def show_basic_config(cls, login, password):
-        """Display a basic configuration."""
-        parser = configparser.RawConfigParser()
-        config = DiagralConfig()
-        account = cls(config, login, password)
-        account.do_login()
-        systems = account.initialize_systems()
-        for system_data in systems:
-            name = slugify(system_data["name"])
-            section = f"system:{name}"
-            parser.add_section(section)
-            system_config = account.get_system_configuration(system_data["id"])
-            data = {k: "" for k in config.account_requirements}
-            data |= {k: "" for k in config.imap_requirements}
-            data["login"] = login
-            data["password"] = password
-            data["name"] = system_data["name"]
-            data["login"] = login
-            data["system_id"] = str(system_data["id"])
-            data["transmitter_id"] = system_config["transmitterId"]
-            data["central_id"] = system_config["centralId"]
-            parser[section] = data
-        fd = io.StringIO()
-        parser.write(fd)
-        account.do_logout()
-        return fd.getvalue()
+        return {
+            "tags": {
+                "identifier": self.login,
+                **kwargs,
+                "type": "diagral",
+            }
+        }
 
-    def get_system_configuration(self, system_id: int, count=0):
+    def get_system_configuration(self, system_id: int):
         """Return complete configuration for a given system."""
         r = self.request(
             "/configuration/getConfiguration",
             json_data={"systemId": system_id, "role": 0},
         )
         return r.json()
 
@@ -587,18 +567,18 @@
                 )
             except Exception as e:
                 logger.exception(e, extra=extra)
                 capture_some_exception(e)
             self.sleep_while_run(check_interval_in_s)
 
 
-class DiagralConfig:
-    """Diagral configuration, with multiple accounts."""
+class DiagralHomekitPlugin(HomekitPlugin):
+    """Specific plugin for Diagral alarms."""
 
-    max_request_tries = 3
+    config_prefix = "diagral"
     account_requirements = {
         "login": RegexValidator(r".*@.*\..*"),
         "password": str,
         "system_id": int,
         "transmitter_id": RegexValidator(r"[\dA-F]*"),
         "central_id": RegexValidator(r"[\dA-F]*"),
         "master_code": int,
@@ -608,71 +588,103 @@
         "imap_login": str,
         "imap_password": str,
         "imap_hostname": str,
         "imap_port": int,
         "imap_use_tls": bool_validator,
     }
 
-    def __init__(self):
+    def __init__(self, config):
         """init function."""
-        self.accounts: [Tuple[str, str], DiagralAccount] = {}
+        super().__init__(config)
+        self.diagral_accounts: [Tuple[str, str], DiagralAccount] = {}
         self.thread_pool = None
-        self.log_requests = False
 
     def get_account(self, login: str, password: str) -> DiagralAccount:
         """Get an account identified by the login and the password."""
         key = (login, password)
-        if key not in self.accounts:
-            self.accounts[key] = DiagralAccount(self, login, password)
-        return self.accounts[key]
-
-    def load_config(self, config_file: pathlib.Path):
-        """Load the configuration."""
-        parser = configparser.ConfigParser()
-        parser.read(config_file)
+        if key not in self.diagral_accounts:
+            self.diagral_accounts[key] = DiagralAccount(self.config, *key)
+        return self.diagral_accounts[key]
+
+    def load_config(self, parser, section):
+        """Load a configuration section."""
+        logger.debug(f"loading {section}")
         config_errors = []
-        for section in parser.sections():
-            if not re.match(r"system:.*", section):
+        kwargs = {}
+        for kwarg, checker in self.account_requirements.items():
+            raw_value = parser.get(section, kwarg, fallback=None)
+            if raw_value is None:
+                msg = f"Required option {kwarg} in section {section}."
+                config_errors.append(msg)
+                logger.fatal(msg)
                 continue
-            kwargs = {}
-            for kwarg, checker in self.account_requirements.items():
-                raw_value = parser.get(section, kwarg, fallback=None)
-                if raw_value is None:
-                    msg = f"Required option {kwarg} in section {section}."
+            elif raw_value is not None:
+                try:
+                    kwargs[kwarg] = checker(raw_value)
+                except ValueError:
+                    msg = f"Invalid option {kwarg} in section {section}."
                     config_errors.append(msg)
                     logger.fatal(msg)
                     continue
-                elif raw_value is not None:
-                    try:
-                        kwargs[kwarg] = checker(raw_value)
-                    except ValueError:
-                        msg = f"Invalid option {kwarg} in section {section}."
-                        config_errors.append(msg)
-                        logger.fatal(msg)
-                        continue
-            login, password = kwargs.pop("login"), kwargs.pop("password")
-            account = self.get_account(login, password)
+        if not config_errors:
+            key = kwargs.pop("login"), kwargs.pop("password")
+            account = self.get_account(*key)
 
             # allow to connect to IMAP accounts for fetching alarm emails
             for attr, checker in self.imap_requirements.items():
                 raw_value = parser.get(section, attr, fallback=None)
                 if raw_value is not None:
                     setattr(account, attr, checker(raw_value))
 
             system = account.get_alarm_system(**kwargs)
             logger.info(
                 f"Configuration for alarm system {system} added.",
                 extra=system.extra_log_data(),
             )
-        if config_errors:
-            raise ValueError("\n".join(config_errors))
+        return config_errors
+
+    def load_accessories(self, bridge):
+        """Add accessories to the Homekit bridge."""
+        for account in self.diagral_accounts.values():
+            for system in account.alarm_systems.values():
+                accessory = HomekitAlarm(system, bridge.driver)
+                bridge.add_accessory(accessory)
 
     def run_all(self):
         """Run all daemons in separate threads."""
-        self.thread_pool = ThreadPool(1)
-        for account in self.accounts.values():
-            self.thread_pool.apply_async(account.run)
+        if self.diagral_accounts:
+            self.thread_pool = ThreadPool(len(self.diagral_accounts))
+            for account in self.diagral_accounts.values():
+                self.thread_pool.apply_async(account.run)
 
     def stop_all(self):
         """Stop all accounts."""
-        for account in self.accounts.values():
+        for account in self.diagral_accounts.values():
             account.is_running = False
+
+    @classmethod
+    def show_basic_config(cls, login, password):
+        """Display a basic configuration."""
+        parser = configparser.RawConfigParser()
+        config = HomekitConfig()
+        account = DiagralAccount(config, login, password)
+        account.do_login()
+        systems = account.initialize_systems()
+        for system_data in systems:
+            name = slugify(system_data["name"])
+            section = f"diagral:{name}"
+            parser.add_section(section)
+            system_config = account.get_system_configuration(system_data["id"])
+            data = {k: "" for k in cls.account_requirements}
+            data |= {k: "" for k in cls.imap_requirements}
+            data["login"] = login
+            data["password"] = password
+            data["name"] = system_data["name"]
+            data["login"] = login
+            data["system_id"] = str(system_data["id"])
+            data["transmitter_id"] = system_config["transmitterId"]
+            data["central_id"] = system_config["centralId"]
+            parser[section] = data
+        fd = io.StringIO()
+        parser.write(fd)
+        account.do_logout()
+        return fd.getvalue()
```

### Comparing `diagralhomekit-0.1.0/diagralhomekit/homekit.py` & `diagralhomekit-0.9.3/diagralhomekit/homekit_alarm.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # ##############################################################################
 #  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
-#  This file homekit.py is part of DiagralHomekit.                             #
+#  This file homekit_alarm.py is part of DiagralHomekit.                       #
 #  Please check the LICENSE file for sharing or distribution permissions.      #
 # ##############################################################################
 """Implements a generic Homekit accessory."""
 import logging
 
 # noinspection PyPackageRequirements
 from pyhap.accessory import Accessory
```

### Comparing `diagralhomekit-0.1.0/diagralhomekit/main.py` & `diagralhomekit-0.9.3/diagralhomekit/main.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,33 +1,31 @@
 # ##############################################################################
 #  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
 #  This file main.py is part of DiagralHomekit.                                #
 #  Please check the LICENSE file for sharing or distribution permissions.      #
 # ##############################################################################
 """All the main functions."""
+from multiprocessing import Queue
+
 import argparse
 import logging
 import os
 import pathlib
+import sentry_sdk
 import signal
 import sys
 import urllib.parse
-from multiprocessing import Queue
-
-import sentry_sdk
 from logging_loki import LokiQueueHandler, emitter
-
 # noinspection PyPackageRequirements
 from pyhap.accessory import Bridge
-
 # noinspection PyPackageRequirements
 from pyhap.accessory_driver import AccessoryDriver
 
-from diagralhomekit.diagral_config import DiagralAccount, DiagralConfig
-from diagralhomekit.homekit import HomekitAlarm
+from diagralhomekit.config import HomekitConfig
+from diagralhomekit.diagral import DiagralHomekitPlugin
 
 logger = logging.getLogger("diagralhomekit")
 
 
 def main():
     """parse arguments and run the daemons."""
     parser = argparse.ArgumentParser()
@@ -54,28 +52,29 @@
     args = parser.parse_args()
     config_dir = args.config_dir
     if args.create_config:
         login, sep, password = args.create_config.partition(":")
         if sep != ":":
             print("Usage: --create-config=login:password")
             return
-        content = DiagralAccount.show_basic_config(login, password)
+        content = DiagralHomekitPlugin.show_basic_config(login, password)
         print(f"cat << EOF > {config_dir}/config.ini")
         print(content)
         print("EOF")
         return
 
     handler = logging.StreamHandler(sys.stdout)
     if args.verbosity == 0:
         logger.setLevel(logging.WARNING)
     elif args.verbosity == 1:
         logger.setLevel(logging.INFO)
     else:
         logger.setLevel(logging.DEBUG)
     logger.addHandler(handler)
+    listen_port = args.port
 
     if args.loki_url:
         emitter.LokiEmitter.level_tag = "level"
         parsed_url = urllib.parse.urlparse(args.loki_url)
         url = f"{parsed_url.scheme}://{parsed_url.hostname}"
         if parsed_url.port:
             url += f":{parsed_url.port}"
@@ -92,34 +91,41 @@
         logger.addHandler(handler)
         logger.debug("Loki configured.")
 
     if args.sentry_dsn:
         sentry_sdk.init(args.sentry_dsn)
         logger.debug("Sentry DSN configured.")
 
-    listen_port = args.port
-
-    run_daemons(config_dir, listen_port, log_requests=args.verbosity >= 3)
+    run_daemons(
+        config_dir,
+        listen_port,
+        log_requests=args.verbosity >= 3,
+    )
 
 
-def run_daemons(config_dir, listen_port, log_requests: bool = False):
+def run_daemons(
+    config_dir, listen_port, log_requests: bool = False
+):
     """launch all processes: Homekit and Diagral checker."""
     persist_file = config_dir / "persist.json"
     config_file = config_dir / "config.ini"
-
-    driver = AccessoryDriver(port=listen_port, persist_file=persist_file)
+    logger.info(f"configuration file: {config_file}")
+    logger.info(f"persistence file: {persist_file}")
+    logger.info(f"listen port: {listen_port}")
+
+    driver = AccessoryDriver(
+        port=listen_port,
+        persist_file=persist_file,
+    )
     bridge = Bridge(driver, "Diagral e-One")
-    config = DiagralConfig()
+    config = HomekitConfig()
     config.log_requests = log_requests
     try:
         config.load_config(config_file)
-        for account in config.accounts.values():
-            for system in account.alarm_systems.values():
-                accessory = HomekitAlarm(system, bridge.driver)
-                bridge.add_accessory(accessory)
+        config.load_accessories(bridge)
         driver.add_accessory(accessory=bridge)
         signal.signal(signal.SIGTERM, driver.signal_handler)
         config.run_all()
         driver.start()
     except Exception as e:
         logger.exception(e)
         raise e
```

### Comparing `diagralhomekit-0.1.0/diagralhomekit/utils.py` & `diagralhomekit-0.9.3/diagralhomekit/utils.py`

 * *Files 8% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 #  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
 #  This file utils.py is part of DiagralHomekit.                               #
 #  Please check the LICENSE file for sharing or distribution permissions.      #
 # ##############################################################################
 """Some utility functions."""
 import re
 import unicodedata
+from typing import Optional
 
 from requests.exceptions import ConnectionError, ConnectTimeout, SSLError
 from sentry_sdk import capture_exception
 from urllib3.exceptions import NewConnectionError
 
 BASE_AID = 1_970_000_000_000
 
@@ -29,14 +30,20 @@
     value = (
         unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
     )
     value = re.sub(r"[^\w\s-]", "", value.lower())
     return re.sub(r"[-_\s]+", "_", value).strip("-_")
 
 
+def str_or_none(value: str) -> Optional[str]:
+    """Return None if the value is empty, the value otherwise."""
+    value = value.strip()
+    return value or None
+
+
 def capture_some_exception(e):
     """Silently discards some network exceptions."""
     if isinstance(
         e,
         (
             NewConnectionError,
             AssertionError,
```

### Comparing `diagralhomekit-0.1.0/pyproject.toml` & `diagralhomekit-0.9.3/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -4,19 +4,21 @@
 
 [tool.poetry]
 authors = ["d9pouces <github@19pouces.net>"]
 description = "Apple HomeKit integration for Diagral alarm systems"
 license = "CeCILL-B"
 name = "diagralhomekit"
 readme = "README.md"
-version = "0.1.0"
+version = "0.9.3"
 
 [tool.poetry.dependencies]
 HAP-python = "^4.6.0"
 base36 = "^0.1.1"
+meteofrance-api = "^1.2.0"
+nut2 = "^2.1.1"
 pyqrcode = "^1.2.1"
 python = "^3.9"
 python-logging-loki = "^0.3.1"
 requests = "^2.28.2"
 sentry-sdk = "^1.18.0"
 
 [tool.poetry.scripts]
```

