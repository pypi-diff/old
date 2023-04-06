# Comparing `tmp/DyaGram-0.0.98.tar.gz` & `tmp/DyaGram-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "DyaGram-0.0.98.tar", last modified: Thu Mar 30 19:59:40 2023, max compression
+gzip compressed data, was "DyaGram-0.0.99.tar", last modified: Thu Mar 30 20:10:04 2023, max compression
```

## Comparing `DyaGram-0.0.98.tar` & `DyaGram-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-03-30 19:59:40.012034 DyaGram-0.0.98/
-drwxrwxrwx   0        0        0        0 2023-03-30 19:59:39.995992 DyaGram-0.0.98/DyaGram.egg-info/
--rw-rw-rw-   0        0        0      238 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      348 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       50 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      239 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-03-30 19:59:39.000000 DyaGram-0.0.98/DyaGram.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      238 2023-03-30 19:59:40.011636 DyaGram-0.0.98/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-03-30 19:59:39.999420 DyaGram-0.0.98/dyagram/
--rw-rw-rw-   0        0        0        0 2023-03-16 01:50:39.000000 DyaGram-0.0.98/dyagram/__init__.py
--rw-rw-rw-   0        0        0    35103 2023-03-30 19:59:32.000000 DyaGram-0.0.98/dyagram/dyagram.py
-drwxrwxrwx   0        0        0        0 2023-03-30 19:59:40.004821 DyaGram-0.0.98/dyagram/initialize/
--rw-rw-rw-   0        0        0        0 2023-03-16 01:50:39.000000 DyaGram-0.0.98/dyagram/initialize/__init__.py
--rw-rw-rw-   0        0        0     2132 2023-03-23 23:04:02.000000 DyaGram-0.0.98/dyagram/initialize/initialize.py
-drwxrwxrwx   0        0        0        0 2023-03-30 19:59:40.008998 DyaGram-0.0.98/dyagram/sites/
--rw-rw-rw-   0        0        0        4 2023-03-16 04:29:28.000000 DyaGram-0.0.98/dyagram/sites/__init__.py
--rw-rw-rw-   0        0        0     1427 2023-03-24 02:37:09.000000 DyaGram-0.0.98/dyagram/sites/sites.py
--rw-rw-rw-   0        0        0       42 2023-03-30 19:59:40.013065 DyaGram-0.0.98/setup.cfg
--rw-rw-rw-   0        0        0      718 2023-03-30 19:59:32.000000 DyaGram-0.0.98/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-30 20:10:04.180565 DyaGram-0.0.99/
+drwxrwxrwx   0        0        0        0 2023-03-30 20:10:04.161236 DyaGram-0.0.99/DyaGram.egg-info/
+-rw-rw-rw-   0        0        0      238 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      348 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       50 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      239 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-03-30 20:10:04.000000 DyaGram-0.0.99/DyaGram.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      238 2023-03-30 20:10:04.179371 DyaGram-0.0.99/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-03-30 20:10:04.165289 DyaGram-0.0.99/dyagram/
+-rw-rw-rw-   0        0        0        0 2023-03-16 01:50:39.000000 DyaGram-0.0.99/dyagram/__init__.py
+-rw-rw-rw-   0        0        0    35565 2023-03-30 20:09:58.000000 DyaGram-0.0.99/dyagram/dyagram.py
+drwxrwxrwx   0        0        0        0 2023-03-30 20:10:04.170975 DyaGram-0.0.99/dyagram/initialize/
+-rw-rw-rw-   0        0        0        0 2023-03-16 01:50:39.000000 DyaGram-0.0.99/dyagram/initialize/__init__.py
+-rw-rw-rw-   0        0        0     2132 2023-03-23 23:04:02.000000 DyaGram-0.0.99/dyagram/initialize/initialize.py
+drwxrwxrwx   0        0        0        0 2023-03-30 20:10:04.175462 DyaGram-0.0.99/dyagram/sites/
+-rw-rw-rw-   0        0        0        4 2023-03-16 04:29:28.000000 DyaGram-0.0.99/dyagram/sites/__init__.py
+-rw-rw-rw-   0        0        0     1427 2023-03-24 02:37:09.000000 DyaGram-0.0.99/dyagram/sites/sites.py
+-rw-rw-rw-   0        0        0       42 2023-03-30 20:10:04.181243 DyaGram-0.0.99/setup.cfg
+-rw-rw-rw-   0        0        0      718 2023-03-30 20:09:58.000000 DyaGram-0.0.99/setup.py
```

### Comparing `DyaGram-0.0.98/dyagram/dyagram.py` & `DyaGram-0.0.99/dyagram/dyagram.py`

 * *Files 1% similar despite different names*

```diff
@@ -426,14 +426,18 @@
                 nm_args = self.netmiko_args_template.copy()
                 nm_args['host'] = device
                 nm_args['device_type'] = os
                 print(f"NETMIKO ARGS FROM COPY TEMPLATE: {nm_args}")
 
             else:
                 os = "cisco_ios"
+                nm_args = self.netmiko_args_template.copy()
+                nm_args['host'] = device
+                nm_args['device_type'] = os
+                print(f"NETMIKO ARGS FROM COPY TEMPLATE: {nm_args}")
                 #raise Exception("Unable to determine OS.")
             self.log.info("GOT DEVICE TYPE")
 
             print("BEFORE SETTING CH")
             dev = ConnectHandler(**nm_args)
             print("AFTER SETTING CH")
             dev.enable()
@@ -556,15 +560,15 @@
                     raise ValueError("LLDP NEIGHBORS ARE STRs. Try without textfsm")
             except ValueError as e:
                 try:
                     lldp_nei_json = self._get_lldp_neighbors_ssh_regex(dev)
                 except:
                     tb = self.get_traceback()
                     self.log.info(f"DEVICE: {device} EXCEPTION22 IN _discover_lldp_neighbors_by_ssh: {tb}")
-            except Exception:
+            except:
                 tb = self.get_traceback()
                 self.log.info(f"DEVICE: {device} - SSH : ERROR DISCOVER LLDP NEIGHBORS - {tb}")
 
             for i in self.topology["devices"]:
                 if i['inventory_ip'] == device:
                     i['hostname'] = lldp_nei_json['hostname']
                     lldp_nei_json.pop("hostname")
@@ -586,15 +590,15 @@
     def _get_chassis_ids(self, netmiko_session=None, os=None, restconf_session=None):
 
 
         if not netmiko_session and restconf_session:
 
             try:
                 resp = restconf_session.get(f"{restconf_session.base_url}/openconfig-interfaces:interfaces")
-            except Exception:
+            except:
                 tb = self.get_traceback()
                 self.log.info(f"DEVICE: {restconf_session.base_url} EXCEPTION01 THROWN IN _get_chassis_ids : {tb}")
                 #print(tb) LOG THIS
 
             if resp.status_code == 200:
                 return  [i['ethernet']['state']['hw-mac-address']
              for i in resp.json()['interfaces']['interface']
@@ -668,15 +672,15 @@
                     neighbor_info = self.lldp_neighbor_template.copy()
                     neighbor_info['hostname'] = intf['neighbors']['neighbor'][0]['state']['system-name']
                     neighbor_info['local_port'] = intf['name']
                     neighbor_info['neighbor_port'] = intf['neighbors']['neighbor'][0]['state']['port-id']
                     neighbor_info['chassis_id'] = intf['neighbors']['neighbor'][0]['state']['chassis-id']
                     lldp_info_json['neighbors'].append(neighbor_info)
 
-        except Exception:
+        except:
             tb = self.get_traceback()
             self.log.info(f"DEVICE: {device} EXCEPTION01 THROWN IN _get_lldp_neighbors_restconf : {tb}")
 
             #print(tb)
 
         if oc_yang_resp.status_code == 200:
             return lldp_info_json
@@ -775,56 +779,60 @@
         #     cdp_info_json['neighbors'][counter]["mgmt_ip_address"] = i
         #     counter += 1
 
         return cdp_info_json
 
     def _get_hostname(self, netmiko_session=None, restconf_session=None):
 
+        try:
+            if not netmiko_session and restconf_session:
+                try:
+                    device = re.search('\d+\.\d+\.\d+\.\d+', restconf_session.base_url).group(1)
+                except:
+                    device = restconf_session.base_url
 
-        if not netmiko_session and restconf_session:
-            try:
-                device = re.search('\d+\.\d+\.\d+\.\d+', restconf_session.base_url).group(1)
-            except:
-                device = restconf_session.base_url
-
-            try:
-                self.log.info(f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying for hostname - START")
-                resp = restconf_session.get(f"{device}/openconfig-system:system/config/name")
-                if resp.status_code == 200:
-                    self.log.info(f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying hostname - SUCCESSFUL")
-                    return resp.json()['hostname']
-                if resp.status_code != 200:
-                    self.log.info(
-                        f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying hostname - FAILURE")
-                    # try nexus TEMPORARY
-                    self.log.info(
-                        f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - START")
-                    resp = restconf_session.get(f"{device}/Cisco-NX-OS-device:System/name")
-
+                try:
+                    self.log.info(f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying for hostname - START")
+                    resp = restconf_session.get(f"{device}/openconfig-system:system/config/name")
                     if resp.status_code == 200:
+                        self.log.info(f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying hostname - SUCCESSFUL")
+                        return resp.json()['hostname']
+                    if resp.status_code != 200:
                         self.log.info(
-                            f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - SUCCESSFUL")
-                        return resp.json()['name']
-                    self.log.info(
-                        f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - FAILURE")
+                            f"DEVICE: {device} - RESTCONF_OPENCONFIG : Querying hostname - FAILURE")
+                        # try nexus TEMPORARY
+                        self.log.info(
+                            f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - START")
+                        resp = restconf_session.get(f"{device}/Cisco-NX-OS-device:System/name")
 
-            except Exception:
+                        if resp.status_code == 200:
+                            self.log.info(
+                                f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - SUCCESSFUL")
+                            return resp.json()['name']
+                        self.log.info(
+                            f"DEVICE: {device} - RESTCONF_NXOS_OS_DEVICE_YANG : Querying hostname - FAILURE")
 
-                tb = self.get_traceback()
-                self.log.info(
-                    f"DEVICE: {device} - RESTCONF_OPENCONFIG_AND_NXOS_OS_DEVICE_YANG_CATCHALL : Querying hostname - FAILURE - TB: {tb}")
+                except:
 
-        else:
-            self.log.info(f"DEVICE: {netmiko_session.host} - SSH : Querying for hostname - START")
-            sh_run_output = netmiko_session.send_command("sh run | inc hostname")
-            hostname = re.search("hostname\s+(.*)", sh_run_output).group(1)
-            self.log.info(f"DEVICE: {netmiko_session.host} - SSH : Querying for hostname - SUCCESSFUL")
+                    tb = self.get_traceback()
+                    self.log.info(
+                        f"DEVICE: {device} - RESTCONF_OPENCONFIG_AND_NXOS_OS_DEVICE_YANG_CATCHALL : Querying hostname - FAILURE - TB: {tb}")
+
+            else:
+                self.log.info(f"DEVICE: {netmiko_session.host} - SSH : Querying for hostname - START")
+                sh_run_output = netmiko_session.send_command("sh run | inc hostname")
+                hostname = re.search("hostname\s+(.*)", sh_run_output).group(1)
+                self.log.info(f"DEVICE: {netmiko_session.host} - SSH : Querying for hostname - SUCCESSFUL")
+
+                return hostname
+            return None
+        except:
+            tb = self.get_traceback()
+            self.log.info(f"DEVICE: {device} EXCEPTION THROWN IN _get_hostname : {tb}")
 
-            return hostname
-        return None
 
     def _get_os_version(self, netmiko_session):
 
         sh_version_output = netmiko_session.send_command("show version")
         if "IOS-XE" in sh_version_output:
             return "ios_xe"
         elif "NX-OS" in sh_version_output:
@@ -891,15 +899,15 @@
             s = sites()
             if len(args.dyagram_args) == 1:
                 s.list_sites_in_cli()
             elif len(args.dyagram_args) > 1:
                 if args.dyagram_args[1].lower() == "new":
                     try:
                         s.make_new_site(args.dyagram_args[2])
-                    except Exception as e:
+                    except:
                         print("Missing argument : <site>")
                 if args.dyagram_args[1].lower() == "switch":
                     try:
                         s.switch_site(args.dyagram_args[2].lower())
                     except:
                         print(f"Site {args.dyagram_args[2]} doesn't exist")
     except:
```

### Comparing `DyaGram-0.0.98/dyagram/initialize/initialize.py` & `DyaGram-0.0.99/dyagram/initialize/initialize.py`

 * *Files identical despite different names*

### Comparing `DyaGram-0.0.98/dyagram/sites/sites.py` & `DyaGram-0.0.99/dyagram/sites/sites.py`

 * *Files identical despite different names*

### Comparing `DyaGram-0.0.98/setup.py` & `DyaGram-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 req = ['bcrypt==4.0.1','cffi==1.15.1','cryptography==39.0.1','future==0.18.3',
        'netmiko==4.1.2','ntc-templates==3.2.0','paramiko==3.0.0','pycparser==2.21',
        'PyNaCl==1.5.0','pyserial==3.5','pywin32==305','PyYAML==6.0',
        'scp==0.14.5','six==1.16.0','tenacity==8.2.1', 'textfsm==1.1.2']
 
 setup(
     name="DyaGram",
-    version="0.0.98",
+    version="0.0.99",
     author="Chris Moses",
     author_email="chrismoses121@gmail.com",
     description="IaC Tool to map out a diagram of a network",
     packages=find_packages(),
     install_requires=req,
     entry_points={
         'console_scripts': ['dyagram=dyagram.dyagram:main']
```

