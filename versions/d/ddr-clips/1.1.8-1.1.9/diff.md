# Comparing `tmp/ddr-clips-1.1.8.tar.gz` & `tmp/ddr-clips-1.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ddr-clips-1.1.8.tar", last modified: Tue Oct 25 19:00:41 2022, max compression
+gzip compressed data, was "ddr-clips-1.1.9.tar", last modified: Thu Feb 16 14:41:45 2023, max compression
```

## Comparing `ddr-clips-1.1.8.tar` & `ddr-clips-1.1.9.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxr-x   0 petervh   (1000) petervh   (1000)        0 2022-10-25 19:00:41.193530 ddr-clips-1.1.8/
--rw-rw-r--   0 petervh   (1000) petervh   (1000)      436 2022-10-25 19:00:41.189530 ddr-clips-1.1.8/PKG-INFO
--rw-rw-r--   0 petervh   (1000) petervh   (1000)        0 2022-08-26 19:08:43.000000 ddr-clips-1.1.8/README.md
-drwxrwxr-x   0 petervh   (1000) petervh   (1000)        0 2022-10-25 19:00:41.189530 ddr-clips-1.1.8/ddr_clips.egg-info/
--rw-rw-r--   0 petervh   (1000) petervh   (1000)      436 2022-10-25 19:00:41.000000 ddr-clips-1.1.8/ddr_clips.egg-info/PKG-INFO
--rw-rw-r--   0 petervh   (1000) petervh   (1000)      205 2022-10-25 19:00:41.000000 ddr-clips-1.1.8/ddr_clips.egg-info/SOURCES.txt
--rw-rw-r--   0 petervh   (1000) petervh   (1000)        1 2022-10-25 19:00:41.000000 ddr-clips-1.1.8/ddr_clips.egg-info/dependency_links.txt
--rw-rw-r--   0 petervh   (1000) petervh   (1000)       43 2022-10-25 19:00:41.000000 ddr-clips-1.1.8/ddr_clips.egg-info/top_level.txt
--rw-rw-r--   0 petervh   (1000) petervh   (1000)   290886 2022-10-13 16:19:51.000000 ddr-clips-1.1.8/ddrclass.py
--rw-rw-r--   0 petervh   (1000) petervh   (1000)    11321 2022-10-07 19:23:31.000000 ddr-clips-1.1.8/ddrparserlib.py
--rw-rw-r--   0 petervh   (1000) petervh   (1000)     5676 2022-09-23 19:50:47.000000 ddr-clips-1.1.8/ddrrun.py
--rwxrwxr-x   0 petervh   (1000) petervh   (1000)   209450 2022-10-13 16:24:20.000000 ddr-clips-1.1.8/genie_parsers.py
--rw-rw-r--   0 petervh   (1000) petervh   (1000)       38 2022-10-25 19:00:41.193530 ddr-clips-1.1.8/setup.cfg
--rw-rw-r--   0 petervh   (1000) petervh   (1000)      784 2022-10-25 18:57:33.000000 ddr-clips-1.1.8/setup.py
+drwxrwxr-x   0 petervh   (1000) petervh   (1000)        0 2023-02-16 14:41:45.441276 ddr-clips-1.1.9/
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)     2513 2023-02-16 14:41:45.441276 ddr-clips-1.1.9/PKG-INFO
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)     2076 2023-02-16 14:19:00.000000 ddr-clips-1.1.9/README.md
+drwxrwxr-x   0 petervh   (1000) petervh   (1000)        0 2023-02-16 14:41:45.441276 ddr-clips-1.1.9/ddr_clips.egg-info/
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)     2513 2023-02-16 14:41:45.000000 ddr-clips-1.1.9/ddr_clips.egg-info/PKG-INFO
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)      205 2023-02-16 14:41:45.000000 ddr-clips-1.1.9/ddr_clips.egg-info/SOURCES.txt
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)        1 2023-02-16 14:41:45.000000 ddr-clips-1.1.9/ddr_clips.egg-info/dependency_links.txt
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)       43 2023-02-16 14:41:45.000000 ddr-clips-1.1.9/ddr_clips.egg-info/top_level.txt
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)   296783 2023-02-16 13:55:34.000000 ddr-clips-1.1.9/ddrclass.py
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)    11321 2022-12-15 14:31:02.000000 ddr-clips-1.1.9/ddrparserlib.py
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)     5676 2022-12-15 14:31:02.000000 ddr-clips-1.1.9/ddrrun.py
+-rwxrwxr-x   0 petervh   (1000) petervh   (1000)   209450 2022-12-15 14:31:02.000000 ddr-clips-1.1.9/genie_parsers.py
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)       38 2023-02-16 14:41:45.441276 ddr-clips-1.1.9/setup.cfg
+-rw-rw-r--   0 petervh   (1000) petervh   (1000)      789 2023-02-16 14:41:30.000000 ddr-clips-1.1.9/setup.py
```

### Comparing `ddr-clips-1.1.8/ddrclass.py` & `ddr-clips-1.1.9/ddrclass.py`

 * *Files 2% similar despite different names*

```diff
@@ -1357,15 +1357,15 @@
                     else:
                         self.netconf_connection = (ncclient.manager.connect_ssh(host=self.control["mgmt-device"][0], port=self.control["mgmt-device"][1],
                             username=self.control["mgmt-device"][2],
                             password=self.control["mgmt-device"][3],
                             hostkey_verify=False,
                             look_for_keys=False,
                             allow_agent=False,
-                            timeout=self.control["nc-timeout"]))
+                            timeout=5))
     #
     # If connections successful break out of the retry loop
     #
                     connect_success = True
                     break
     #
     # If connection failed, retry after waiting "retry-time" seconds
@@ -1814,16 +1814,16 @@
             device_name = fact['device']
         else:
             device_info = self.control["device-list"][int(device_index)]
             device_id = self.device[int(device_index)]
             device_name = device_info[4]
 
         get_result = device_id.get(filter=('subtree', str(fact['path'])))
-        if self.control["debug-parser"] == 1:
-            self.print_log("**** DDR Debug: get_template_multifacts_protofact NETCONF get result: \n\n" + str(get_result) + "\n")
+        if self.control["debug-fact"] == 1:
+            self.print_log("\n**** DDR Debug: get_template_multifacts_protofact NETCONF get result: \n\n" + str(get_result) + "\n")
 
         instances = xml.dom.minidom.parseString(get_result.xml).getElementsByTagName(fact["assert_fact_for_each"])
 
         # put all instances with desired fields in "filtered_instances"
         if "element_list" in fact:
             filtered_instances = []
             for each in instances:
@@ -1978,16 +1978,16 @@
                     self.env.assert_string("(" + str(assert_fact[0]) + " (" + str(assert_fact[1]) + " " + str(assert_fact[2]) + "))")
                 except: pass #ignore case where FACT already exists
     #
     # get data for multiple instances
     # instances will be a list of the objects which match the "key"
     #
             get_result = device_id.get(filter=('subtree', str(path)))
-            if self.control["debug-parser"] == 1:
-                self.print_log("**** DDR Debug: get_template_multifact NETCONF get result: " + str(get_result))
+            if self.control["debug-fact"] == 1:
+                self.print_log("\n**** DDR Debug: get_template_multifact NETCONF get result: " + str(get_result))
             instances = xml.dom.minidom.parseString(get_result.xml).getElementsByTagName(key)
             if self.control["debug-fact"] == 1:
                 self.print_log("**** DDR Debug: instances: " + str(instances))
     #
     # Filter entries in multitemplate list if a filter is specified to limit fact collection
     #
             if element_list != []:
@@ -2018,18 +2018,27 @@
                 if self.control["debug-fact"] == 1:
                     self.print_log("**** DDR Debug nodes: " + str(each.childNodes))
                 instance = []
                 for leaf in leafs:
                     if self.control["debug-fact"] == 1:
                         self.print_log("**** DDR Debug: slot: " + str(leaf))
                         self.print_log("**** DDR Debug: value: " + str(each.getElementsByTagName(leaf)))
-                    for node in each.getElementsByTagName(leaf):
+    #BUGFIX 2.7.23
+    # If no value is returned for the get request the value is []
+    # A value of 'nil' must be filled in if no value is returned from the get request
+    #
+                    if len(each.getElementsByTagName(leaf)) == 0:
+                        instance.append('nil')
                         if self.control["debug-fact"] == 1:
-                            self.print_log("**** DDR Debug get_template_fact node: " + str(node.firstChild.nodeValue))
-                        instance.append(node.firstChild.nodeValue)
+                            self.print_log("**** DDR Debug get_template_fact node: " + 'nil')
+                    else:
+                        for node in each.getElementsByTagName(leaf):
+                            if self.control["debug-fact"] == 1:
+                                self.print_log("**** DDR Debug get_template_fact node: " + str(node.firstChild.nodeValue))
+                            instance.append(node.firstChild.nodeValue)
                 if instance != []:
                     instance_list.append(instance)
                 instance = []
     #
     # For each instance in the instance_list assert the information read as facts
     # Create a python dictionary with each key:value pair where the key is the slot
     # and value is the slot value
@@ -2037,33 +2046,38 @@
     #  [["five-seconds", "int"], ["one-minute", "int"], ["five-minutes", "int"]]
     #
             for each in instance_list:
                 template = self.env.find_template(str(deftemplate))
                 fact1 = {}
                 fact1["device"] = str(device_name)
                 j = 0
-                for fact in facts:
-                    if len(fact) == 2:
-                        if fact[1] == "int":
-                            fact1[str(fact[0])] = int(each[j])
-                        elif fact[1] == "str":
-                            fact1[str(fact[0])] = str(each[j]).replace(" ", "_")
-                        elif fact[1] == "flt":
-                            fact1[str(fact[0])] = float(each[j])
-                        else:
-                            self.print_log("%%%% DDR Exception: Invalid fact type " + str(fact))
-                            break
-                        j = j + 1
+
+                try:
+                    for fact in facts:
+                        if len(fact) == 2:
+                            if fact[1] == "int":
+                                fact1[str(fact[0])] = int(each[j])
+                            elif fact[1] == "str":
+                                fact1[str(fact[0])] = str(each[j]).replace(" ", "_")
+                            elif fact[1] == "flt":
+                                fact1[str(fact[0])] = float(each[j])
+                            else:
+                                self.print_log("%%%% DDR Exception: Invalid fact type " + str(fact))
+                                break
+
+                            j = j + 1
                         
-                    else:
-                        if isinstance(each[j], int):
-                            fact1[str(fact)] = int(each[j])
                         else:
-                            fact1[str(fact)] = str(each[j]).replace(" ", "_")
-                            j = j + 1                       
+                            if isinstance(each[j], int):
+                                fact1[str(fact)] = int(each[j])
+                            else:
+                                fact1[str(fact)] = str(each[j]).replace(" ", "_")
+                                j = j + 1
+                except Exception as e:
+                    self.print_log("\n%%%% DDR Error: get_template_multifacts fact generation error: " + str(fact))                      
     #
     # Assert the FACT defined by a Python dictionary
     #
                 if self.control["debug-fact"] == 1:
                     self.print_log("**** DDR Debug: get_template_multifacts_index fact to assert: " + str(template) + " " + str(fact1))
                    
                 try:
@@ -2071,15 +2085,15 @@
                 except Exception as e:
                     if self.control["debug-fact"] == 1:
                         self.print_log("%%%% DDR Exception: get_template_multifacts_index assert_fact: " + str(e))
                     pass
 
         except Exception as e:
             self.print_log("\n%%%% DDR Error: get_template_multifacts_index error: " + str(e))
-            self.print_log("\n%%%% DDR Error: No value found in get_template_multifacts_index")
+            self.print_log("\n%%%% DDR Error: No value found in get_template_multifacts_index: " + str(fact1))
         return
 
 ##############################################################################
 #
 #
 # show_and_assert_fact -
 #            Execute a show command, parse the show command output,
@@ -2328,15 +2342,15 @@
                         fact1[slot] = str(value).replace(" ", "_")
                 except Exception as e:
                     self.print_log("\n%%%% DDR Error: Exception assert_template_fact: type error: " +  str(protofact["template"]) + " slot: "  + str(slot) + " " + str(e))
     # 
     # Append extra "slot" if there is a slot and slot_value passed in to the function
     # The added slot will always be type string
     #  
-            if add_slot != 'Fnone':
+            if add_slot != 'none':
                 fact1[add_slot] = str(slot_value)                
     #
     # Assert the FACT defined by a Python dictionary
     #
             try:
                 if self.control["debug-fact"] == 1:
                     self.print_log("**** DDR Debug: assert_template_fact: " + str(protofact["template"]) + " " + str(fact1))
@@ -4074,14 +4088,16 @@
             Invoked in the "RHS" of a triggered rule.
             This function executes NETCONF operations defined in ddr-facts nc_fact_list entries
             For example: (run_nc_fact 0 1 neighbor ?neighbor none ?neighbor)
               This example runs a NETCONF operation using index "0" in the nc_fact_list.  The 1 indicates there is one
               parameter that will provided by the rule and will substituted into the NETCONF message.
               "none" indicates that splitting the contents of variable is not required 
 
+            Two types of FACTs can be defined in ddr-facts, multitemplate and multitemplate_protofact
+            
               nc_fact_list = [
                {"fact_type": "multitemplate",
                 "data": ["multitemplate", 0, "leaf2",
                       '''<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            <router>
                              <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
                                <neighbor>
@@ -4093,15 +4109,61 @@
                              </bgp>
                            </router>
                          </native>
                 ''',
                 "nbr-hold-time", "timers",
                  ["holdtime"], 
                  ["hold-time"], [],
-                 []]}]
+                 []]},
+
+		{"fact_type": "multitemplate_protofact", 
+		        "device_index": 0,
+		        "device": 'NVE-EVPN-leaf1',
+		        "assert_fact_for_each": 'Ep-list',
+		        "hardcoded_list": ["device"],
+		"path": '''
+		      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
+		        <eps-items>
+		          <epId-items>
+	            	    <Ep-list>
+		              <epId/>
+		              <adminSt/>
+		              <primaryIp/>
+		              <peers-items>
+		                <dy_peer-items>
+		                  <DyPeer-list>
+		                    <ip/>
+		                    <state/>
+		                    <mac/>
+		                  </DyPeer-list>
+  		                </dy_peer-items>
+   		              </peers-items>
+     		              </Ep-list>
+		            </epId-items>
+		        </eps-items>
+		      </System>''',
+		"protofact": {"template": 'nve-peer-list2',
+		              "slots": {"device": 'NVE-EVPN-leaf1',
+		                        "name": 'epId',
+		                        "primary-ip": 'primaryIp',
+		                        "admin-state": 'adminSt',
+		                        "peer-ip": 'ip',
+		                        "peer-state": 'state',
+		                        "peer-mac": 'mac'
+		                       },
+		              "types": {"device": "str",
+		                        "name": "str",
+		                        "primary-ip": "str",
+		                        "admin-state": "str",
+		                        "peer-ip": "str",
+		                        "peer-state": "str",
+		                        "peer-mac": "str"
+		                        } 
+		        }
+		}                                  
             
             :param *args: Pointer to structure with passed arguments defined in function content below
                     args[0]: index = int(argval)
                     args[1]: num_params = int(argval)
                     args[2]: slot = argval is the slot name
                     args[3]: slot_value = argval is the slot value
                     args[4]: split = argval #This argument = 'split' if the next argument is an interface name
@@ -4144,17 +4206,23 @@
                             num_params = num_params + 1
                         else: sub_params.append(str(argval))
                     j = j + 1
             except Exception as e:
                 self.print_log("\n%%%% DDR Error: run_nc_fact argument error: " +str(sub_params) + " " + str(e))
                 return
 
+        #
+        # process multitemplate and multitemplate_protofact FACT types
+        #
             raw_fact = copy.deepcopy(self.control["nc-fact-list"][index])
-            fact_data = raw_fact["data"]
-            fact_msg = fact_data[3]
+            if raw_fact["fact_type"] == "multitemplate":
+                fact_data = raw_fact["data"]
+                fact_msg = fact_data[3]
+            else: #fact is multitemplate_protofact
+                fact_msg = raw_fact["path"]
 #
 # Substitute arguments from the rule function call into the Netconf operation
 #
             try:
                 if num_params == 0:
                    formatted = str(fact_msg)
                 elif num_params == 1:
@@ -4171,40 +4239,50 @@
 
             except Exception as e:
                 self.print_log("\n%%%% DDR Error: run_nc_fact format message: " + str(e))
                
             if self.control["debug-fact"] == 1:
                 self.print_log("**** DDR Debug: run_nc_facts facts: " + str(fact_msg))
 
-            fact_data[3] = formatted
-            raw_fact["data"] = fact_data
-            fact = raw_fact
+            #
+            # update FACT netconf request including any parameters provided
+            #
+            if raw_fact["fact_type"] == "multitemplate":
+                fact_data[3] = formatted
+                raw_fact["data"] = fact_data
+                fact = raw_fact
+            else: #fact is multitemplate_protofact
+                raw_fact["path"] = formatted
+                fact = raw_fact
 
+            # insert device name into get calls to insert device name into generated facts
             if fact["fact_type"] == "multitemplate":
-                status = self.get_template_multifacts_index(fact["data"], slot, slot_value, 'none')
+                status = self.get_template_multifacts_index(fact["data"], "device", fact["data"][2], 'none')
             elif fact["fact_type"] == "multitemplate_protofact":
-                status = self.get_template_multifacts_protofact_index(fact, slot, slot_value, 'none')
+                status = self.get_template_multifacts_protofact_index(fact, "device", fact["data"][2], 'none')
             else:
                 self.print_log("\n%%%% DDR Error: run_nc_facts Error in ddr-facts definition: Invalid fact type: " + str(fact))
 
         except Exception as e:
             self.print_log("\n%%%% DDR Error: Exception in run_nc_fact: " + str(e))
 
     def run_nc_fact_index(self, index, device_index, num_params, par1, par2, par3):
 
         """
-            Rule file function call: (run_nc_fact 0 ?device_index 1 neighbor ?neighbor none ?neighbor) ; use netconf to get hold-time for the bgp-neighbor
+            Rule file function call: (run_nc_fact_index 0 ?device_index 1 neighbor ?neighbor none ?neighbor) ; use netconf to get hold-time for the bgp-neighbor
             
             Invoked in the "RHS" of a triggered rule.
             This function executes NETCONF operations defined in ddr-facts nc_fact_list entries
             For example: (run_nc_fact 0 ?device_index 1 neighbor ?neighbor none ?neighbor)
               This example runs a NETCONF operation using index "0" in the nc_fact_list.  ?device_index selects which device in the 'device_list' defined in ddr-devices to perform the operation on.  The 1 indicates there is one
               parameter that will provided by the rule and will substituted into the NETCONF message.
               "none" indicates that splitting the contents of variable is not required 
-
+         
+            Two types of FACTs can be defined in ddr-facts, multitemplate and multitemplate_protofact
+            
               nc_fact_list = [
                {"fact_type": "multitemplate",
                 "data": ["multitemplate", 0, "leaf2",
                       '''<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            <router>
                              <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
                                <neighbor>
@@ -4216,36 +4294,92 @@
                              </bgp>
                            </router>
                          </native>
                 ''',
                 "nbr-hold-time", "timers",
                  ["holdtime"], 
                  ["hold-time"], [],
-                 []]}]
-            
+                 []]},
+
+		{"fact_type": "multitemplate_protofact", 
+		        "device_index": 0,
+		        "device": 'NVE-EVPN-leaf1',
+		        "assert_fact_for_each": 'Ep-list',
+		        "hardcoded_list": ["device"],
+		"path": '''
+		      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
+		        <eps-items>
+		          <epId-items>
+	            	    <Ep-list>
+		              <epId/>
+		              <adminSt/>
+		              <primaryIp/>
+		              <peers-items>
+		                <dy_peer-items>
+		                  <DyPeer-list>
+		                    <ip/>
+		                    <state/>
+		                    <mac/>
+		                  </DyPeer-list>
+  		                </dy_peer-items>
+   		              </peers-items>
+     		              </Ep-list>
+		            </epId-items>
+		        </eps-items>
+		      </System>''',
+		"protofact": {"template": 'nve-peer-list2',
+		              "slots": {"device": 'NVE-EVPN-leaf1',
+		                        "name": 'epId',
+		                        "primary-ip": 'primaryIp',
+		                        "admin-state": 'adminSt',
+		                        "peer-ip": 'ip',
+		                        "peer-state": 'state',
+		                        "peer-mac": 'mac'
+		                       },
+		              "types": {"device": "str",
+		                        "name": "str",
+		                        "primary-ip": "str",
+		                        "admin-state": "str",
+		                        "peer-ip": "str",
+		                        "peer-state": "str",
+		                        "peer-mac": "str"
+		                        } 
+		        }
+		}                                  
+
             :param index - Index into the nc_fact list id ddr-facts
             :param device_index - Index to the device_list defined in ddr-devices device_list
             :param num_params - Number of parameters to insert into NETCONF request
             :param par1 - First parameter
             :param par2 - Second parameter
             :param par3 - Third parameter
        
         Usage::
 
-              (run_nc_fact 0 0 1 GigabitEthernet0/0 none none) ;This use netconf to get hold-time for the bgp-neighbor
+              (run_nc_fact_index 0 0 1 GigabitEthernet0/0 none none) ;This use netconf to get hold-time for the bgp-neighbor
 
             :raises none:
 
         """
 
         try:
-
-            raw_fact = copy.deepcopy(self.control["nc-fact-list"][index])
-            fact_data = raw_fact["data"]
-            fact_msg = fact_data[3]
+            try:
+                raw_fact = copy.deepcopy(self.control["nc-fact-list"][index])
+        #
+        # process multitemplate and multitemplate_protofact FACT types
+        #
+                if raw_fact["fact_type"] == "multitemplate":
+                    fact_data = raw_fact["data"]
+                    fact_msg = fact_data[3]
+                else:
+                    fact_msg = raw_fact["path"]
+                    
+            except:
+                self.print_log("\n%%%% DDR Error: run_nc_fact_index missing fact in nc_fact_list in ddr-facts list index: " + str(index))
+                return
         #
         # substitute parameters in command string if included in call from rule
         #
             try:
                 
                 if num_params == 0:
                    formatted = str(fact_msg)
@@ -4262,25 +4396,36 @@
             except Exception as e:
                 self.print_log("\n%%%% DDR Error: run_nc_fact_index format message: " + str(e))
                 return
                
             if self.control["debug-fact"] == 1:
                 self.print_log("**** DDR Debug: run_nc_facts_index facts: " + str(formatted))
 
-            fact_data[3] = formatted
-            raw_fact["data"] = fact_data
-            fact = raw_fact
-
-            device_info = self.control["device-list"][int(device_index)]
-            device_id = str(device_info[4])
+            #
+            # update FACT netconf request including any parameters provided
+            #
+            if raw_fact["fact_type"] == "multitemplate":
+                fact_data[3] = formatted
+                raw_fact["data"] = fact_data
+                fact = raw_fact
+            else: # fact type is multitemplate_protofact
+                raw_fact["path"] = formatted
+                fact = raw_fact
+            
+            try:
+                device_info = self.control["device-list"][int(device_index)]
+                device_id = str(device_info[4])
+            except:
+                self.print_log("\n%%%% DDR Error: run_nc_fact_index missing device definition in  ddr-devices index value: " + str(device_index))
+                return
 
             if fact["fact_type"] == "multitemplate":
                 status = self.get_template_multifacts_index(fact["data"], "device", device_id, device_index)
             elif fact["fact_type"] == "multitemplate_protofact":
-                status = self.get_template_multifacts_protofact_index(fact, "device", device_id, device_index)
+                status = self.get_template_multifacts_protofact_index(fact, "device", device_id, fact["device_index"])
             else:
                 self.print_log("\n%%%% DDR Error: run_nc_facts_index Error in ddr-facts definition: Invalid fact type: " + str(fact))
 
         except Exception as e:
             self.print_log("\n%%%% DDR Error: Exception in run_nc_fact_index: " + str(e))
 
     def cancel_ping(self, neighbor):
```

### Comparing `ddr-clips-1.1.8/ddrparserlib.py` & `ddr-clips-1.1.9/ddrparserlib.py`

 * *Files identical despite different names*

### Comparing `ddr-clips-1.1.8/ddrrun.py` & `ddr-clips-1.1.9/ddrrun.py`

 * *Files identical despite different names*

### Comparing `ddr-clips-1.1.8/genie_parsers.py` & `ddr-clips-1.1.9/genie_parsers.py`

 * *Files identical despite different names*

### Comparing `ddr-clips-1.1.8/setup.py` & `ddr-clips-1.1.9/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="ddr-clips", # DDR-CLIPs runtime
-    version="1.1.8", # Update multiple ddr-clips usecases
+    version="1.1.9", # Update ddrclass.py for offbox execution
     author="Peter Van Horne",
     author_email="petervh@cisco.com",
     description="Distributed Device Reasoning (DDR) CLIPs runtime",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://wwwin-github.cisco.com/petervh/ddr-clips",
     classifiers=[
```

