# Comparing `tmp/umnet-pyncs-0.1.6.tar.gz` & `tmp/umnet-pyncs-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "umnet-pyncs-0.1.6.tar", max compression
+gzip compressed data, was "umnet-pyncs-0.1.9.tar", max compression
```

## Comparing `umnet-pyncs-0.1.6.tar` & `umnet-pyncs-0.1.9.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0     1500 2022-08-31 16:02:31.678143 umnet-pyncs-0.1.6/README.md
--rw-r--r--   0        0        0      404 2022-09-01 18:13:41.967203 umnet-pyncs-0.1.6/pyproject.toml
--rw-r--r--   0        0        0       22 2022-08-31 16:02:31.679153 umnet-pyncs-0.1.6/umnet_pyncs/__init__.py
--rw-r--r--   0        0        0       40 2022-08-31 16:02:31.679383 umnet-pyncs-0.1.6/umnet_pyncs/state/__init__.py
--rw-r--r--   0        0        0        0 2022-08-31 16:02:31.679499 umnet-pyncs-0.1.6/umnet_pyncs/state/models/__init__.py
--rw-r--r--   0        0        0     1106 2022-08-31 16:02:31.679628 umnet-pyncs-0.1.6/umnet_pyncs/state/models/base.py
--rw-r--r--   0        0        0     4701 2022-08-31 16:02:31.679768 umnet-pyncs-0.1.6/umnet_pyncs/state/models/ios.py
--rw-r--r--   0        0        0     5301 2022-08-31 16:02:31.679917 umnet-pyncs-0.1.6/umnet_pyncs/state/models/junos.py
--rw-r--r--   0        0        0     5591 2022-09-01 18:13:19.324866 umnet-pyncs-0.1.6/umnet_pyncs/state/models/nxos.py
--rw-r--r--   0        0        0      636 2022-08-31 16:02:31.680187 umnet-pyncs-0.1.6/umnet_pyncs/state/models/utils.py
--rw-r--r--   0        0        0     5252 2022-08-31 21:33:48.140168 umnet-pyncs-0.1.6/umnet_pyncs/state/state_manager.py
--rw-r--r--   0        0        0     2257 2022-09-01 18:16:06.234000 umnet-pyncs-0.1.6/setup.py
--rw-r--r--   0        0        0     2026 2022-09-01 18:16:06.234333 umnet-pyncs-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     3090 2022-10-16 21:41:38.854568 umnet-pyncs-0.1.9/README.md
+-rw-r--r--   0        0        0      423 2022-10-16 21:04:25.448730 umnet-pyncs-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0       22 2022-08-31 16:02:31.679153 umnet-pyncs-0.1.9/umnet_pyncs/__init__.py
+-rw-r--r--   0        0        0       40 2022-08-31 16:02:31.679383 umnet-pyncs-0.1.9/umnet_pyncs/state/__init__.py
+-rw-r--r--   0        0        0        0 2022-08-31 16:02:31.679499 umnet-pyncs-0.1.9/umnet_pyncs/state/models/__init__.py
+-rw-r--r--   0        0        0     2498 2022-10-16 21:04:25.449437 umnet-pyncs-0.1.9/umnet_pyncs/state/models/base.py
+-rw-r--r--   0        0        0     8529 2022-10-16 21:04:25.450140 umnet-pyncs-0.1.9/umnet_pyncs/state/models/ios.py
+-rw-r--r--   0        0        0     7177 2022-10-16 21:04:25.450943 umnet-pyncs-0.1.9/umnet_pyncs/state/models/junos.py
+-rw-r--r--   0        0        0    12607 2022-10-16 21:04:25.451502 umnet-pyncs-0.1.9/umnet_pyncs/state/models/nxos.py
+-rw-r--r--   0        0        0      636 2022-08-31 16:02:31.680187 umnet-pyncs-0.1.9/umnet_pyncs/state/models/utils.py
+-rw-r--r--   0        0        0     5252 2022-08-31 21:33:48.140168 umnet-pyncs-0.1.9/umnet_pyncs/state/state_manager.py
+-rw-r--r--   0        0        0     3904 2022-10-16 21:43:25.619167 umnet-pyncs-0.1.9/setup.py
+-rw-r--r--   0        0        0     3656 2022-10-16 21:43:25.619581 umnet-pyncs-0.1.9/PKG-INFO
```

### Comparing `umnet-pyncs-0.1.6/umnet_pyncs/state/models/utils.py` & `umnet-pyncs-0.1.9/umnet_pyncs/state/models/utils.py`

 * *Files identical despite different names*

### Comparing `umnet-pyncs-0.1.6/umnet_pyncs/state/state_manager.py` & `umnet-pyncs-0.1.9/umnet_pyncs/state/state_manager.py`

 * *Files identical despite different names*

### Comparing `umnet-pyncs-0.1.6/PKG-INFO` & `umnet-pyncs-0.1.9/PKG-INFO`

 * *Files 25% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: umnet-pyncs
-Version: 0.1.6
+Version: 0.1.9
 Summary: custom python module for NCS helpers
 Author: Nick Grundler
 Author-email: grundler@umich.edu
 Requires-Python: >=3.7,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: multiprocessing-logging (>=0.3.3,<0.4.0)
+Requires-Dist: netaddr (>=0.8.0,<0.9.0)
 Requires-Dist: ntc-templates (>=3.0.0,<4.0.0)
 Description-Content-Type: text/markdown
 
 ## Overview
 
 This module is intended to be installed on the production NCS nodes and imported in other services/actions that need to gather state from the network.  It uses the NCS device manager and the standard python `multiprocessing` library to connect to devices in-parallel and issue commands, returning results as structured data.
 
@@ -34,18 +35,48 @@
             interfaces = m.get_state(al_devices, ["get-interface-details"])
             arp = m.get_state(dl_devices, ["get-arp-table"])
             ...
 ```
 
 ## Supported commands
 
-We attempt to normalize the output of each command based on how it is implemented.  For example, we might default to just directly returning the data as-parsed by the `ntc_templates` module, or try and emulate for e.g. junos devices where we might have direct access to NETCONF RPCs via the NCS device manager.
-
 Currently supported commands are:
 - `get-mac-table`
 - `get-arp-table`
 - `get-interface-details`
 - `get-transciever-details`
+- `get-lldp-neighbors`
+- `get-bfd-neighbors`
+- `get-ospf-neighbors`
+
+For any given command, the various platform-specific models are responsible for implementing how the data is fetched and parsed from the remote device.  Each command corresponds to a method that can be invoked to retrieve the data, e.g. `get-interface-details` maps to the `get_interface_details()` instance method of the model(s).
+
+For Cisco IOS and NXOS devices (which use CLI-based NEDs), the built-in NCS `live-status` action(s) are used to send raw CLI commands to the device.  For example, the `get_mac_address()` method will send a `show mac address-table` CLI command.  For both IOS and NXOS we use [ntc_templates](https://github.com/networktocode/ntc-templates) to parse the raw text output into structured data.
+
+For Juniper devices, since the NED uses NETCONF for all device communications, we instead call the `<get-ethernet-switching-table-information>` RPC directly.  Since this RPC is modelled in YANG, we can then parse the results directly using the maagic API.
+
+All the nitty-gritty details of parsing the data retrieved directly from the remote device is handled by the platform-specific model implementation for that device.  Each model normalizes the data using the dataclasses defined in [base.py](./umnet_pyncs/state/models/base.py).  The intention is to makes it simpler for NCS actions/services to use this module, as well as making it easier to develop/maintain.
+
+**NB**: this implementation currently relies on an additional template for NXOS that handles parsing `show ip arp detail vrf all` -- see [PR# 1204](https://github.com/networktocode/ntc-templates/pull/1204).
+
+## Developer testing
+
+Install the [ipython-superuser](https://github.com/NSO-developer/ipython-superuser) package into your local NSO development environment.  Use the REPL e.g:
 
-## TODO
-The models are mostly taken verbatim from the `netsplash` NCS package, and additional methods were added on top to support the [stats.py](https://gitlab.umich.edu/its-inf-net/umnet-ncs-dev/-/blob/master/packages/umnet-backbone/python/fabric/stats.py) module.
+``` python
+import logging
+from umnet_pyncs.state import StateManager
+
+logging.basicConfig(level=logging.DEBUG)
+
+devices = [d for d in root.devices.device]
+
+m = StateManager()
+
+# NB: m.get_state() expects a list of devices
+interfaces = m.get_state(devices, ["get-interface-details"])
+    
+print(interfaces)
+
+m.__exit__()
+```
```

