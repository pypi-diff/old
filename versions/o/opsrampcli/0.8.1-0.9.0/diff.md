# Comparing `tmp/opsrampcli-0.8.1.tar.gz` & `tmp/opsrampcli-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "opsrampcli-0.8.1.tar", max compression
+gzip compressed data, was "opsrampcli-0.9.0.tar", max compression
```

## Comparing `opsrampcli-0.8.1.tar` & `opsrampcli-0.9.0.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    35848 2022-10-04 14:47:11.226935 opsrampcli-0.8.1/README.md
--rw-r--r--   0        0        0        0 2022-09-07 21:17:27.706613 opsrampcli-0.8.1/opsrampcli/__init.py__
--rw-r--r--   0        0        0     3540 2022-09-24 03:17:44.657708 opsrampcli-0.8.1/opsrampcli/alerts.py
--rw-r--r--   0        0        0    20577 2022-11-11 00:26:02.367366 opsrampcli-0.8.1/opsrampcli/argparsing.py
--rw-r--r--   0        0        0    11027 2022-11-11 03:46:23.396107 opsrampcli-0.8.1/opsrampcli/customattrs.py
--rw-r--r--   0        0        0      139 2022-09-09 16:13:15.713881 opsrampcli-0.8.1/opsrampcli/discovery.py
--rw-r--r--   0        0        0    12040 2022-09-11 16:05:49.016343 opsrampcli-0.8.1/opsrampcli/escalationpolicies.py
--rw-r--r--   0        0        0      625 2022-09-09 15:05:38.177711 opsrampcli-0.8.1/opsrampcli/incidents.py
--rw-r--r--   0        0        0     2185 2022-10-28 21:23:02.886157 opsrampcli-0.8.1/opsrampcli/integrations.py
--rw-r--r--   0        0        0     1566 2022-10-19 01:58:44.171208 opsrampcli-0.8.1/opsrampcli/monitoring.py
--rw-r--r--   0        0        0     6209 2022-11-11 00:26:34.377060 opsrampcli-0.8.1/opsrampcli/opsrampcli.py
--rw-r--r--   0        0        0    27943 2022-11-11 03:35:41.899990 opsrampcli-0.8.1/opsrampcli/opsrampenv.py
--rw-r--r--   0        0        0     1780 2022-09-09 14:51:18.045918 opsrampcli-0.8.1/opsrampcli/resources.py
--rw-r--r--   0        0        0     4998 2022-09-11 04:00:10.796357 opsrampcli-0.8.1/opsrampcli/servicemaps.py
--rw-r--r--   0        0        0      568 2022-11-11 03:48:02.246123 opsrampcli-0.8.1/pyproject.toml
--rw-r--r--   0        0        0    37340 2022-11-11 03:48:17.981620 opsrampcli-0.8.1/setup.py
--rw-r--r--   0        0        0    36632 2022-11-11 03:48:17.984233 opsrampcli-0.8.1/PKG-INFO
+-rw-r--r--   0        0        0    35848 2022-10-04 14:47:11.226935 opsrampcli-0.9.0/README.md
+-rw-r--r--   0        0        0        0 2022-09-07 21:17:27.706613 opsrampcli-0.9.0/opsrampcli/__init.py__
+-rw-r--r--   0        0        0     3540 2022-09-24 03:17:44.657708 opsrampcli-0.9.0/opsrampcli/alerts.py
+-rw-r--r--   0        0        0    22745 2023-04-05 21:39:44.608984 opsrampcli-0.9.0/opsrampcli/argparsing.py
+-rw-r--r--   0        0        0    11027 2022-11-11 03:46:23.396107 opsrampcli-0.9.0/opsrampcli/customattrs.py
+-rw-r--r--   0        0        0      139 2022-09-09 16:13:15.713881 opsrampcli-0.9.0/opsrampcli/discovery.py
+-rw-r--r--   0        0        0    12040 2022-09-11 16:05:49.016343 opsrampcli-0.9.0/opsrampcli/escalationpolicies.py
+-rw-r--r--   0        0        0      632 2022-12-15 14:20:53.238049 opsrampcli-0.9.0/opsrampcli/incidents.py
+-rw-r--r--   0        0        0     3439 2022-12-07 18:44:00.338142 opsrampcli-0.9.0/opsrampcli/integrations.py
+-rw-r--r--   0        0        0     1566 2022-10-19 01:58:44.171208 opsrampcli-0.9.0/opsrampcli/monitoring.py
+-rw-r--r--   0        0        0     6425 2023-03-29 19:31:15.306879 opsrampcli-0.9.0/opsrampcli/opsrampcli.py
+-rw-r--r--   0        0        0    29838 2023-04-05 21:35:53.744693 opsrampcli-0.9.0/opsrampcli/opsrampenv.py
+-rw-r--r--   0        0        0    12963 2023-04-05 21:30:40.172669 opsrampcli-0.9.0/opsrampcli/resources.py
+-rw-r--r--   0        0        0     4998 2022-09-11 04:00:10.796357 opsrampcli-0.9.0/opsrampcli/servicemaps.py
+-rw-r--r--   0        0        0      568 2023-04-05 21:41:31.947752 opsrampcli-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0    37340 2023-04-05 21:42:14.239674 opsrampcli-0.9.0/setup.py
+-rw-r--r--   0        0        0    36632 2023-04-05 21:42:14.242034 opsrampcli-0.9.0/PKG-INFO
```

### Comparing `opsrampcli-0.8.1/README.md` & `opsrampcli-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/opsrampcli/alerts.py` & `opsrampcli-0.9.0/opsrampcli/alerts.py`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/opsrampcli/argparsing.py` & `opsrampcli-0.9.0/opsrampcli/argparsing.py`

 * *Files 3% similar despite different names*

```diff
@@ -65,27 +65,36 @@
     parser_webhookalerts.add_argument('--secure', default=True, help='Whether or not to verify SSL cert')
 
 
     # Incidents
     parser_getincidents = subparsers.add_parser('getincidents', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Search and take action on Incidents")
     parser_getincidents.add_argument('--query', required=True, help='Query String to filter incidents')
     parser_getincidents.add_argument('--brief', action='store_true', help='Include only key fields in output')
+    parser_getincidents.add_argument('--details', action='store_true', help='Get the full details for all matched incidents - this will include custom field values')
     parser_getincidents.add_argument('--count', action='store_true', help='Only show the count of matching incidents')
     parser_getincidents.add_argument('--filter', required=False, help='Post-query filter on incidents.  Python expression that will evaluate to True or False such as incident["resource"]["name"].startswith("prod")')
     parser_getincidents.add_argument('--resolve', action='store_true', help='Resolve the matching incidents')
 
     # Resources/Devices
     parser_getresources = subparsers.add_parser('getresources', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Search for and take action on resources/devices")
     parser_getresources.add_argument('--query', required=False, help='Query String to filter resources as per https://develop.opsramp.com/resource-management/tenants-tenantid-resources-search')
     parser_getresources.add_argument('--search', required=False, help='Search String to filter resources as it would be entered under Resources -> Search')
     parser_getresources.add_argument('--count', action='store_true', help='Only show the count of matching resources')
     parser_getresources.add_argument('--delete', action='store_true', help='Delete the matching resources')
     parser_getresources.add_argument('--manage', action='store_true', help='Manage the matching resources')
     parser_getresources.add_argument('--filter', required=False, help='Post-query filter on resources.  Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod")')
 
+    parser_importresources = subparsers.add_parser('importresources', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Import resources from a spreadsheet.  Custom attr field names should be prefixed with .tag and the custom attribute names should be created in advance via the UI.  Any resource with an Action Processing column value of Delete will deleted.")
+    parser_importresources.add_argument('--commit', action='store_true', help='Make the actual updates on the platform.  If not specified, only error checking and import simulation will occur.')
+    parser_importresources.add_argument('--addvalues', action='store_true', help='If new values are found in the spreadsheet, add the value definitions on the fly.  Otherwise new values will be considered an error.')
+    parser_importresources.add_argument('--writeblanks', action='store_true', help='When no value is provided in the spreadsheet for a resource, remove any existing value for that resource on the platform.  If not specified then no action is taken for empty values.')
+    parser_importresources.add_argument('--filename', required=False, help='Name of excel file to import (.xlsx extension will be added if not specified.)')
+
+
+
     # Service Maps
     parser_exportservicemaps = subparsers.add_parser('exportservicemaps', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Export one or more full Service Map definitions to a file which can be manipulated and re-imported")
     parser_exportservicemaps.add_argument("--name", required=False, help='Name of the root level Service Map/Group (export all if not specified)')
     parser_exportservicemaps.add_argument("--outdir", default=".", help='Directory path where export will be saved')
     parser_exportservicemaps.add_argument('--clobber', action='store_true', help='Remove/overwrite prior exports of same maps')
     parser_exportservicemaps.add_argument('--timestamp', action='store_true', help='Include a timestamp in the Service Map dir name')
 
@@ -167,20 +176,26 @@
     parser_clonetemplates_target = parser_clonetemplates.add_mutually_exclusive_group(required=True)
     parser_clonetemplates_target.add_argument('--prefix', help="New template name will be same as original name but with this text prepended")
     parser_clonetemplates_target.add_argument('--copyname', help="New template will have this as its name")
 
     # Integrations
     parser_getintegrations = subparsers.add_parser('getintegrations', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Get installed Integration definitions")
     parser_getintegrations.add_argument('--query', required=False, help='Query String to filter integrations')
+    parser_getintegrations.add_argument('--filter', required=False, help='Post-query filter.  Python expression that will evaluate to True or False such as record["integration"]["name"] == "JIRA"')
+
+    parser_importintegrations = subparsers.add_parser('importintegrations', parents=[env_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Import integration definitions from a json file")
+    parser_importintegrations.add_argument('--file', required=True, help='JSON file containing integration definition or array of definitions')
 
+    # Discovery schedule options for cloud integrations
     discp_parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
     discp = discp_parser.add_argument_group(title="Specify discovery schedule")
     discp.add_argument('--recurrence', default='WEEKLY', choices=('WEEKLY','DAILY','NONE'), help='Recurrence type for discovery schedule')
     discp.add_argument('--daysofweek', default='sunday,', help='Comma-separated list of days of week used for WEEKLY recurrence')
     discp.add_argument('--starthour', default=2, help='Hour of day to start discovery')
+    discp.add_argument('--rules', default="ANY_CLOUD_RESOURCE", help='Comma-delimited list of rules to filter what object types are discovered and managed')
 
     # Azure Integrations
     parser_addazurearmintegration = subparsers.add_parser('addazurearmintegration', parents=[env_parser,discp_parser], formatter_class=argparse.ArgumentDefaultsHelpFormatter, help="Install a new Azure ARM integration")
     parser_addazurearmintegration.add_argument('--azname', required=True, help='displayName for the integration')
     parser_addazurearmintegration.add_argument('--azsub', required=True, help='Azure Subscription ID')
     parser_addazurearmintegration.add_argument('--aztenant', required=True, help='Azure Tenant ID')
     parser_addazurearmintegration.add_argument('--azclient', required=True, help='Azure Client ID')
```

### Comparing `opsrampcli-0.8.1/opsrampcli/customattrs.py` & `opsrampcli-0.9.0/opsrampcli/customattrs.py`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/opsrampcli/escalationpolicies.py` & `opsrampcli-0.9.0/opsrampcli/escalationpolicies.py`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/opsrampcli/incidents.py` & `opsrampcli-0.9.0/opsrampcli/incidents.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import requests
 import json
 
 def do_cmd_getincidents(ops, args):
     if args.count:
             print("Matched %i incidents." % (ops.get_incidents_count(args.query)))
     else:
-        incidents = ops.get_incidents(args.query, 1, args.brief, False, args.filter)
+        incidents = ops.get_incidents(args.query, 1, args.brief, args.details, args.filter)
         print(json.dumps(incidents, indent=2, sort_keys=False))
         if args.resolve:
             update = {"status": "Resolved"}
             for incident in incidents:
                 try:
                     print(ops.post_incident_update(incident['id'], update))
                 except requests.exceptions.RequestException as e:
```

### Comparing `opsrampcli-0.8.1/opsrampcli/monitoring.py` & `opsrampcli-0.9.0/opsrampcli/monitoring.py`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/opsrampcli/opsrampcli.py` & `opsrampcli-0.9.0/opsrampcli/opsrampcli.py`

 * *Files 2% similar despite different names*

```diff
@@ -122,14 +122,16 @@
         escalationpolicies.do_cmd_getalertescalations(ops, args)
     elif args.command == "migratealertesc":
         escalationpolicies.do_cmd_migratealertescalations(ops, args)
     elif args.command == "getcustomattrs":
         customattrs.do_cmd_get_custom_attributes(ops, args)
     elif args.command == "getresources":
         resources.do_cmd_get_resources(ops, args)
+    elif args.command == "importresources":
+        resources.do_cmd_import_resources(ops, args)
     elif args.command == "exportcustattrfile":
         customattrs.do_cmd_make_custom_attr_file(ops, args)
     elif args.command == "importcustattrfile":
         customattrs.do_cmd_import_custom_attr_file(ops, args)
     elif args.command == "getservicemaps":
         print(json.dumps(ops.get_service_maps(), indent=2, sort_keys=False));
     elif args.command == "getchildsvcgroups":
@@ -145,14 +147,16 @@
     elif args.command == "cloneservicemaps":
         servicemaps.do_cmd_clone_service_maps(ops, args)
     elif args.command == "gettemplates":
         monitoring.do_cmd_get_templates(ops, args)
     elif args.command == "clonetemplates":
         monitoring.do_cmd_clone_templates(ops, args)
     elif args.command == "getintegrations":
-        print(json.dumps(ops.get_integrations(args.query), indent=2, sort_keys=False));
+        print(json.dumps(ops.get_integrations(args.query, filter=args.filter), indent=2, sort_keys=False))
+    elif args.command == "importintegrations":
+        integrations.do_import_integrations(ops, args)
     elif args.command == "addazurearmintegration":
-        print(json.dumps(integrations.do_add_azure_arm(ops, args), indent=2, sort_keys=False));
+        print(json.dumps(integrations.do_add_azure_arm(ops, args), indent=2, sort_keys=False))
     elif args.command == "addazureasmintegration":
-        print(json.dumps(integrations.do_add_azure_asm(ops, args), indent=2, sort_keys=False));
+        print(json.dumps(integrations.do_add_azure_asm(ops, args), indent=2, sort_keys=False))
 if __name__ == "__main__":
     main()
```

### Comparing `opsrampcli-0.8.1/opsrampcli/opsrampenv.py` & `opsrampcli-0.9.0/opsrampcli/opsrampenv.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,20 +31,114 @@
     ]
     def __init__(self, env, isSecure=True):
         self.env = env
         self.isSecure = True
         if isinstance(isSecure, str) and (isSecure.lower() == 'false' or isSecure.lower() == 'no' or isSecure == '0'):
             self.isSecure = False
 
-    def get_integrations(self, queryString=None):
-        return self.get_objects("integrations", queryString=queryString)
+    def post_object(self, path, obj):
+        token = self.get_token()
+        url = self.env['url'] + path
+        headers = {
+            'Content-Type': 'application/json',
+            'Accept': 'application/json',
+            'Authorization': 'Bearer ' + token
+        }
+        response = requests.request("POST", url, headers=headers, data=json.dumps(obj), verify=self.isSecure)
+        if int(response.headers['x-ratelimit-remaining']) < 2 :
+            sleeptime = int(response.headers['x-ratelimit-reset']) - int(datetime.now().timestamp()) + 3
+            print(f'Sleeping for {str(sleeptime)} sec to wait for API throttling limit to reset..')
+            time.sleep(sleeptime)
+        try:    
+            return response.json()
+        except Exception as e:
+            return {'success': response.ok, 'text': response.text}
+
+    def get_objects(self, obtype, page=1, queryString=None, searchQuery=None,countonly=False, itemId=None, filter=None):
+
+        endpoints = {
+            "clients": self.env['partner'] + "/clients/" + self.env['tenant'],
+            "incidentCustomFields": self.env['tenant'] + "/customFields/INCIDENT",
+            "deviceGroups": self.env['tenant'] + "/deviceGroups/minimal",
+            "userGroups": self.env['tenant'] + "/userGroups",
+            "urgencies": self.env['tenant'] + "/incidents/urgencies",
+            "customAttributes": self.env['tenant'] + "/customAttributes/search",
+            "resources": self.env['tenant'] + "/resources/search",
+            "resourcesNewSearch": self.env['tenant'] + "/query/execute",
+            "assignedAttributeEntities": self.env['tenant'] + "/customAttributes/" + str(itemId) + "/assignedEntities/search",
+            "serviceMaps": self.env['tenant'] + "/serviceGroups/search",
+            "childServiceGroups": self.env['tenant'] + "/serviceGroups/" + str(itemId) + "/childs/search",
+            "serviceGroup": self.env['tenant'] + "/serviceGroups/" + str(itemId),
+            "templates": self.env['tenant'] + "/monitoring/templates/search",
+            "integration": self.env['tenant'] + "/integrations/installed/" + str(itemId),
+            "integrations": self.env['tenant'] + "/integrations/installed/search",
+            "incident": f'{self.env["tenant"]}/incidents/{itemId}'
+        }
+
+        url = self.env['url'] + "/api/v2/tenants/" + endpoints[obtype]
+        token = self.get_token()
+ 
+        headers = {
+            'Content-Type': 'application/json',
+            'Accept': 'application/json',
+            'Authorization': 'Bearer ' + token
+        }
+
+        params = {
+            'pageSize': 500,
+            'pageNo': page
+        }
+
+        if countonly:
+            params['pageSize'] = 1
+
+        if queryString:
+            params['queryString'] = queryString
+
+        if searchQuery:
+            params['searchQuery'] = searchQuery
+            params['type'] = "resources"
+
+        if obtype in ['userGroups', 'serviceMaps', 'integrations']:
+            params['pageSize'] = 100
+
+        response = requests.request("GET", url, headers=headers, verify=self.isSecure, params=params)
+        if int(response.headers['x-ratelimit-remaining']) < 2 :
+            sleeptime = int(response.headers['x-ratelimit-reset']) - int(datetime.now().timestamp()) + 3
+            print(f'Sleeping for {str(sleeptime)} sec to wait for API throttling limit to reset..')
+            time.sleep(sleeptime)
+        try:
+            responseobj = response.json()
+        except Exception as e:
+            print(repr(response))
+            sys.exit(1)
+
+        if countonly:
+            return int(responseobj['totalResults'])
+
+        if "results" in responseobj:
+            results = responseobj['results']
+        else:
+            results = responseobj
+ 
+        if filter and (type(results) == list):
+            results[:] = [record for record in results if (eval(filter))]
+
+        if "nextPage" in responseobj and responseobj['nextPage']:
+            #print("Got %i %s from %s, proceeding to page %i" % (len(results), obtype, self.env['name'], responseobj['nextPageNo']))
+            return results + self.get_objects(obtype=obtype, page=responseobj['nextPageNo'],queryString=queryString, searchQuery=searchQuery, itemId=itemId, filter=filter)
+        else:
+            return results
+
+    def get_integrations(self, queryString=None, filter=None):
+        return self.get_objects("integrations", queryString=queryString, filter=filter)
 
     def add_integration(self, intname, obj):
         path = f'/api/v2/tenants/{self.env["tenant"]}/integrations/install/{intname}'
-        return self.post_object(path, obj);
+        return self.post_object(path, obj)
 
 
     def get_templates(self, queryString=None):
         return self.get_objects("templates", queryString=queryString)
 
     def clone_template(self, templateobj, newname, newdesc):
         token = self.get_token()
@@ -234,17 +328,18 @@
         alerts = []
         if brief:
             for result in results:
                 alerts.append({
                     'uniqueId': result['uniqueId'],
                     'createdDate': result['createdDate'],
                     'updatedTime': result['updatedTime'],
+                    'app': result['app'],
                     'device': { 
                         'name': result['device']['name'],
-                        'id': result['device']['id']
+                        'id': result['device'].get('id','NO_ID_FOUND')
                     },
                     'component': result['component'],
                     'metric': result['metric'],
                     'problemArea': result['problemArea'],
                     'subject': result['subject'],
                     'status': result['status'],
                     'eventType': result['eventType'],
@@ -296,14 +391,17 @@
             'pageSize': 1
         }
 
         response = requests.request("GET", url, headers=headers, params=params, verify=self.isSecure)
         responseobj = response.json()
         return responseobj['totalResults']
 
+    def get_incident(self, incidentId):
+        return self.get_objects("incident", itemId=incidentId)
+
     def get_incidents(self, query, page=1, brief=False, details=False, filter=""):
         token = self.get_token()
         url = self.env['url'] + "/api/v2/tenants/" + self.env['tenant'] + "/incidents/search"
         headers = {
             'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Bearer ' + token
@@ -338,16 +436,17 @@
                     'currentState': result['currentState'],
                     'repeatCount': result['repeatCount']
                 })
         else:
             incidents = results
         if details:
             for incident in incidents:
-                details = self.get_incident(incident['uniqueId'])
+                details = self.get_incident(incident['id'])
                 incident['description'] = details['description']
+                incident['customFields'] = details['customFields']
 
         if filter:
             for idx, incident in enumerate(incidents):
                 if not eval(filter):
                    del incidents[idx] 
 
         if responseobj['nextPage']:
@@ -481,15 +580,15 @@
     def add_custom_attr_value(self, attributeId, values, description=""):
         if type(values) == str:
             values = [values]
         if type(description) == str:
             description = [description]
         if len(values) > len(description):
             for i in range(len(description), len(values)):
-                description[i] = ""
+                description.append("")
 
         path = f'/api/v2/tenants/{self.env["tenant"]}/customAttributes/{attributeId}'
         obj = {}
         customAttributeValues = []
         for i,val in enumerate(values):
             customAttributeValues.append({
                     "value": val,
@@ -532,24 +631,17 @@
         else:
             raise TypeError("device_ids must be an array or a string") 
 
         payload = []
         for device in devices:
             payload.append({"id": device})
 
-        token = self.get_token()
-        url = self.env['url'] + "/api/v2/tenants/" + self.env['tenant'] + "/customAttributes/" + str(attr_id) + "/values/" + str(value_id) + "/devices"
-        headers = {
-            'Content-Type': 'application/json',
-            'Accept': 'application/json',
-            'Authorization': 'Bearer ' + token
-        }
-
-        response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=self.isSecure)
-        return response.json()     
+        path = "/api/v2/tenants/" + self.env['tenant'] + "/customAttributes/" + str(attr_id) + "/values/" + str(value_id) + "/devices"
+        return self.post_object(path, payload)
+   
 
     def remove_custom_attr_from_devices(self, attr_id, value_id, device_ids):
         devices = []
         if isinstance(device_ids, list):
             devices = device_ids
         elif isinstance(device_ids, str):
             devices.append(device_ids)
@@ -567,115 +659,61 @@
             'Accept': 'application/json',
             'Authorization': 'Bearer ' + token
         }
 
         response = requests.request("DELETE", url, headers=headers, data=json.dumps(payload), verify=self.isSecure)
         return response.json() 
 
-    def post_object(self, path, obj):
-        token = self.get_token()
-        url = self.env['url'] + path
-        headers = {
-            'Content-Type': 'application/json',
-            'Accept': 'application/json',
-            'Authorization': 'Bearer ' + token
-        }
-        response = requests.request("POST", url, headers=headers, data=json.dumps(obj), verify=self.isSecure)
-        return response.json() 
-
-    def get_objects(self, obtype, page=1, queryString=None, searchQuery=None,countonly=False, itemId=None):
-
-        endpoints = {
-            "clients": self.env['partner'] + "/clients/" + self.env['tenant'],
-            "incidentCustomFields": self.env['tenant'] + "/customFields/INCIDENT",
-            "deviceGroups": self.env['tenant'] + "/deviceGroups/minimal",
-            "userGroups": self.env['tenant'] + "/userGroups",
-            "urgencies": self.env['tenant'] + "/incidents/urgencies",
-            "customAttributes": self.env['tenant'] + "/customAttributes/search",
-            "resources": self.env['tenant'] + "/resources/search",
-            "resourcesNewSearch": self.env['tenant'] + "/query/execute",
-            "assignedAttributeEntities": self.env['tenant'] + "/customAttributes/" + str(itemId) + "/assignedEntities/search",
-            "serviceMaps": self.env['tenant'] + "/serviceGroups/search",
-            "childServiceGroups": self.env['tenant'] + "/serviceGroups/" + str(itemId) + "/childs/search",
-            "serviceGroup": self.env['tenant'] + "/serviceGroups/" + str(itemId),
-            "templates": self.env['tenant'] + "/monitoring/templates/search",
-            "integration": self.env['tenant'] + "/integrations/installed/" + str(itemId),
-            "integrations": self.env['tenant'] + "/integrations/installed/search"
-        }
-
-        url = self.env['url'] + "/api/v2/tenants/" + endpoints[obtype]
+        
+    def do_resource_action(self, action, resourceId):
+        # Action is manage or unmanage
         token = self.get_token()
- 
+        url = f'{self.env["url"]}/api/v2/tenants/{self.env["tenant"]}/devices/{resourceId}/{action}'
         headers = {
             'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Bearer ' + token
         }
 
-        params = {
-            'pageSize': 500,
-            'pageNo': page
-        }
-
-        if countonly:
-            params['pageSize'] = 1
-
-        if queryString:
-            params['queryString'] = queryString
-
-        if searchQuery:
-            params['searchQuery'] = searchQuery
-            params['type'] = "resources"
-
-        if obtype in ['userGroups', 'serviceMaps', 'integrations']:
-            params['pageSize'] = 100
-
-        response = requests.request("GET", url, headers=headers, verify=self.isSecure, params=params)
-        try:
+        response = requests.request("POST", url, headers=headers, verify=self.isSecure)
+        responseobj = { "status_code": 200}
+        if response.status_code != 200:
             responseobj = response.json()
-        except Exception as e:
-            print(repr(response))
-            sys.exit(1)
 
-        if countonly:
-            return int(responseobj['totalResults'])
 
-        if "results" in responseobj:
-            results = responseobj['results']
-        else:
-            results = responseobj
- 
-        if "nextPage" in responseobj and responseobj['nextPage']:
-            #print("Got %i %s from %s, proceeding to page %i" % (len(results), obtype, self.env['name'], responseobj['nextPageNo']))
-            return results + self.get_objects(obtype=obtype, page=responseobj['nextPageNo'],queryString=queryString, searchQuery=searchQuery, itemId=itemId)
-        else:
-            return results
-        
-    def do_resource_action(self, action, resourceId):
-        # Action is manage or unmanage
+        if int(response.headers['x-ratelimit-remaining']) < 2 :
+            sleeptime = int(response.headers['x-ratelimit-reset']) - int(datetime.now().timestamp()) + 3
+            print(f'Sleeping for {str(sleeptime)} sec..')
+            time.sleep(sleeptime)
+        return responseobj
+
+    def create_resource(self, resource_dict:dict):
         token = self.get_token()
-        url = f'{self.env["url"]}/api/v2/tenants/{self.env["tenant"]}/devices/{resourceId}/{action}'
+        url = f'{self.env["url"]}/api/v2/tenants/{self.env["tenant"]}/resources'
         headers = {
             'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Bearer ' + token
         }
 
-        response = requests.request("POST", url, headers=headers, verify=self.isSecure)
-        responseobj = { "status_code": 200}
-        if response.status_code != 200:
-            responseobj = response.json()
+        response = requests.request("POST", url, headers=headers, verify=self.isSecure, data=json.dumps(resource_dict))
+        responseobj = response.json()
 
 
         if int(response.headers['x-ratelimit-remaining']) < 2 :
             sleeptime = int(response.headers['x-ratelimit-reset']) - int(datetime.now().timestamp()) + 3
             print(f'Sleeping for {str(sleeptime)} sec..')
             time.sleep(sleeptime)
         return responseobj
 
+    def update_resource(self, resourceId:str, resource_dict:dict):
+        token = self.get_token()
+        path = f'/api/v2/tenants/{self.env["tenant"]}/resources/{resourceId}'
+        return self.post_object(path, resource_dict)
+
     def delete_resource(self, resourceId):
         token = self.get_token()
         url = f'{self.env["url"]}/api/v2/tenants/{self.env["tenant"]}/resources/{resourceId}'
         headers = {
             'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Bearer ' + token
```

### Comparing `opsrampcli-0.8.1/opsrampcli/servicemaps.py` & `opsrampcli-0.9.0/opsrampcli/servicemaps.py`

 * *Files identical despite different names*

### Comparing `opsrampcli-0.8.1/pyproject.toml` & `opsrampcli-0.9.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "opsrampcli"
-version = "0.8.1"
+version = "0.9.0"
 description = "A command line interface for OpsRamp"
 authors = ["Michael Friedhoff <michael.friedhoff@opsramp.com>"]
 license = "MIT"
 
 readme = "README.md"
 
 [tool.poetry.scripts]
```

### Comparing `opsrampcli-0.8.1/setup.py` & `opsrampcli-0.9.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -17,15 +17,15 @@
  'requests>=2.28.0,<3.0.0']
 
 entry_points = \
 {'console_scripts': ['opcli = opsrampcli.opsrampcli:main']}
 
 setup_kwargs = {
     'name': 'opsrampcli',
-    'version': '0.8.1',
+    'version': '0.9.0',
     'description': 'A command line interface for OpsRamp',
     'long_description': '# OpsRamp Command Line Interface\n\nThis is a utility script that allows easy searching and manipulation of various OpsRamp items and configurations.  You can specify connection credentials via command line, or you can [set up an environments file](#credentials) to contain the credentials you need to use, which makes it easier if you need to manage multiple credentials.\n\n\n# <a id="Available"></a>Available Commands\nThe available commands are:\n\n\n| opcli Command                               | Description                                                                                                               |\n|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|\n| [getalerts](#getalerts)                     | Search for and take action on alerts                                                                                      |\n| [postalerts](#postalerts)                   | Post alerts using the API (using OAuth creds)                                                                             |\n| [webhookalerts](#webhookalerts)             | Post alerts to a Webhook integration                                                                                      |\n| [getincidents](#getincidents)               | Search and take action on Incidents                                                                                       |\n| [getresources](#getresources)               | Search for and take action on resources/devices                                                                           |\n| [exportservicemaps](#exportservicemaps)     | Export one or more full Service Map definitions to a file which can be manipulated and re-imported                        |\n| [importservicemaps](#importservicemaps)     | Import (and optionally transform while doing so) from a Service Map export file                                           |\n| [cloneservicemaps](#cloneservicemaps)       | Copy an existing Service Map, with transformations/replacements (useful when you have a template Service Map to re-use)   |\n| [transformsvcmap](#transformsvcmap)         | Apply regex replacements to an exported Service Map and create a new transformed export file with the changes             |\n| [getservicemaps](#getservicemaps)           | Get Service Map definitions                                                                                               |\n| [getchildsvcgroups](#getchildsvcgroups)     | Get child Service Groups of a parent Service                                                                              |\n| [getservicegroup](#getservicegroup)         | Get the full definition of a Service Group                                                                                |\n| [exportcustattrfile](#exportcustattrfile)   | Generate an Excel or csv file from existing custom attribute values                                                       |\n| [importcustattrfile](#importcustattrfile)   | Import an Excel file containing custom attribute values                                                                   |\n| [getcustomattrs](#getcustomattrs)           | Get custom attribute definitions                                                                                          |\n| [getdiscoprofile](#getdiscoprofile)         | Get discovery profile definition                                                                                          |\n| [getalertesc](#getalertesc)                 | Search and get Escalation Policy definitions                                                                              |\n| [migratealertesc](#migratealertesc)         | Migrate/copy Escalation Policies within same tenant or from one tenant to another                                         |\n| [clonetemplates](#clonetemplates)           | Clone monitoring templates                                                                                                |\n\n&nbsp;\n&nbsp;\n\nFor more detailed help on a specific command use the -h option with the command, for example to get help on the cloneservicemaps command:\n\n```shell\n% opcli cloneservicemaps -h\nusage: opcli cloneservicemaps [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --name NAME --replace REGEX REPLACEWITH [--parentlink] [--clobber]\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n  --name NAME           Name of Service Map to transform and clone (default: None)\n  --replace REGEX REPLACEWITH\n                        Transforming regex pattern and replacement string (option can be repeated) (default: None)\n  --parentlink          If root Service has a link to a parent, link the imported Service Map (default: False)\n  --clobber             Overwrite Service Map (i.e. with same name) if it already exists (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="credentials"></a>Credentials\n\nopcli requires credentials for most operations, either via command line arguments or an *environments.yml* file to be located in the directory where you running it.  Optionally you can specify an explicit environments file path & name using the --envfile option.  The file must follow the following format, where the name is the value you will specify to the --env option to define the URL and credentials you will use:\n\n```yaml\n- name: example1\n  url:  https://customer2name.api.opsramp.com\n  partner: msp_nnnnn\n  tenant: client_nnnnn\n  client_id: abcdefg1234567\n  client_secret: abcdefg1234567\n\n- name: example2\n  url:  https://customer2name.api.opsramp.com\n  partner: msp_nnnnn\n  tenant: client_nnnnn\n  client_id: abcdefg1234567\n  client_secret: abcdefg1234567\n```\nIf providing credentials directly on the command line, use the following options:\n\n```shell\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n  --vtoken VTOKEN       OpsRamp webhook token (only used for webhookalerts command) (default: None)\n```\nNote that you only need to provide the attributes needed for the kind of API calls you are making.  Therefore:\n* If you are making an API call that does not require a partner id (which is not needed  in most cases) you do not need to provide a *partner* value.\n* If you are not doing webhook alert posts, you would not need to specify the *vtoken* value.\n* If you are doing only webhook alert posts then you would not need *client_id* and *client_secret*.\n* If you are using the environment for a bunch of different scenarios, there is no harm in having the extra values there for the cases where they are not needed.\n\n&nbsp;\n&nbsp;\n# Commands\n\n## <a id="getalerts"></a>getalerts\nSearch for and take action on alerts\n\n```shell\nusage: opcli getalerts [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --query QUERY [--brief] [--descr] [--count] [--filter FILTER] [--action ACTION] [--heal]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --query QUERY      Query String to filter alerts as per https://develop.opsramp.com/resource-management/tenants-tenantid-resources-search (default: None)\n  --brief            Include only key fields in output (default: False)\n  --descr            Include the description field in results (runs *much* slower as it requires a separate api call per alert) (default: False)\n  --count            Only show the count of matching alerts (default: False)\n  --filter FILTER    Post-query filter on alerts. Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod") (default: None)\n  --action ACTION    Perform an action on matching alerts (Heal, acknowledge, suppress, close, unsuppress, unAcknowledge) (default: None)\n  --heal             Heal the matching alerts (i.e. send a matching Ok) (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n### Alert search criteria\nAlert search --query option uses the syntax documented [here](https://web.archive.org/web/20211024221749/https://docs.opsramp.com/api/alerts/tenants-tenantid-alerts-search/)\n\n*Note: Above link is to an Internet Archive capture of an old doc page, as the latest doc no longer lists query variables* \n### Examples\n\nSearch for all alerts with matching resource/device numeric id and metric\n\n    % opcli getalerts --env myenvname --query \'resourceIds:9798408+metrics:testmetric\' --brief\n\n\nSearch for all alerts last updated during given time range, and heal & close them\n\n    % opcli getalerts --env myenvname --query \'startDate:2000-01-01T00:00:00 0000+endDate:2020-12-01T00:00:00 0000+alertTimeBase:updated+states:Critical,Warning,Info\' --heal --action close\n\n# <a id="postalerts"></a>postalerts\nPost alerts directly to the API (using OAuth creds)\n```shell\nusage: opcli postalerts [-h] [--env ENV] [--envfile ENVFILE] [--url URL] [--client_id KEY] [--client_secret SCRT] [--tenant TENANT] [--partner PARTNER] [--secure SECURE] [--infile INFILE] [--range RANGE] [--subject SUBJECT] [--state {Critical,Warning,Info,Ok}] [--metric METRIC] [--resource RESOURCE] [--source SOURCE] [--comp COMP] [--desc DESC] [--prob PROB] [--client CLIENT]\n                        [--custom NAME VALUE]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n\nPost alerts using alert content from a json file:\n  --infile INFILE       File containing a json array of alert payloads (default: None)\n  --range RANGE         An integer or range identifying which alert in the file to send (default: None)\n\nPost an alert using alert content from the command line:\n  --subject SUBJECT     Alert Subject (default: None)\n  --state {Critical,Warning,Info,Ok}\n                        Alert Current State (default: None)\n  --metric METRIC       Alert metric (default: None)\n  --resource RESOURCE   Alert Resource name (default: None)\n  --source SOURCE       Alert Source name (default: None)\n  --comp COMP           Alert Component name (default: None)\n  --desc DESC           Alert Description (default: None)\n  --prob PROB           Alert Problem Area (default: None)\n  --client CLIENT       Alert Client ID (only required if posting with a partner-level tenant (default: None)\n  --custom NAME VALUE   Alert custom attribute name and value (can repeat this option for multiple custom attributes) (default: None)\n```\n### Example\n\n    % opcli postalerts --env myenv --subject \'test alert\' --state Warning --metric testmetric --resource testhost  --comp c1 --desc mydesc --prob p1 --custom attr1 val1 --custom attr2 val2\n# <a id="webhookalerts"></a>webhookalerts\nPost alerts to a Webhook integration\n```shell\nusage: opcli webhookalerts [-h] [--url URL] [--vtoken VTOKEN] --infile INFILE [--range RANGE]\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --infile INFILE       File containing an array of json alert payloads (default: None)\n  --range RANGE         An integer or range identifying which alert in the file to send (default: all)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --vtoken VTOKEN       OpsRamp webhook token (default: None)\n```\n### Example\nPost alert #5 from the specified json file (expected to contain an array of alerts), using vtoken authentication\n\n    % opcli webhookalerts --vtoken mytoken --infile myalertsamples.json --range 5\n\n# <a id="getincidents"></a>getincidents\nSearch and take action on Incidents\n```shell\nusage: opcli getincidents [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --query QUERY [--brief] [--count] [--filter FILTER] [--resolve]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --query QUERY      Query String to filter incidents (default: None)\n  --brief            Include only key fields in output (default: False)\n  --count            Only show the count of matching incidents (default: False)\n  --filter FILTER    Post-query filter on incidents. Python expression that will evaluate to True or False such as incident["resource"]["name"].startswith("prod") (default: None)\n  --resolve          Resolve the matching incidents (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getresources"></a>getresources\nSearch for and take action on resources/devices\n```shell\nusage: opcli getresources [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--query QUERY] [--search SEARCH] [--count] [--delete] [--manage] [--filter FILTER]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --query QUERY      Query String to filter resources as per https://develop.opsramp.com/resource-management/tenants-tenantid-resources-search (default: None)\n  --search SEARCH    Search String to filter resources as it would be entered under Resources -> Search (default: None)\n  --count            Only show the count of matching resources (default: False)\n  --delete           Delete the matching resources (default: False)\n  --manage           Manage the matching resources (default: False)\n  --filter FILTER    Post-query filter on resources. Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod") (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="exportservicemaps"></a>exportservicemaps    \nExport one or more full Service Map definitions to a file which can be manipulated and re-imported\n```shell\nusage: opcli exportservicemaps [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--name NAME] [--outdir OUTDIR] [--clobber] [--timestamp]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --name NAME        Name of the root level Service Map/Group (export all if not specified) (default: None)\n  --outdir OUTDIR    Directory path where export will be saved (default: .)\n  --clobber          Remove/overwrite prior exports of same maps (default: False)\n  --timestamp        Include a timestamp in the Service Map dir name (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="importservicemaps"></a>importservicemaps    \nImport (and optionally transform while doing so) from a Service Map export file\n```shell\nusage: opcli importservicemaps [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --src SRC [--replace REGEX REPLACEWITH] [--parentlink] [--clobber]\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n  --src SRC             Source: Path to the export file of a Service Map (default: None)\n  --replace REGEX REPLACEWITH\n                        Transforming regex pattern and replacement string (option can be repeated) (default: None)\n  --parentlink          If root Service has a link to a parent, link the imported Service Map (default: False)\n  --clobber             Overwrite Service Map (i.e. with same name) if it already exists (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="cloneservicemaps"></a>cloneservicemaps     \nCopy an existing Service Map, with transformations/replacements (useful when you have a template Service Map to re-use)\n```shell\nusage: opcli cloneservicemaps [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --name NAME --replace REGEX REPLACEWITH [--parentlink] [--clobber]\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n  --name NAME           Name of Service Map to transform and clone (default: None)\n  --replace REGEX REPLACEWITH\n                        Transforming regex pattern and replacement string (option can be repeated) (default: None)\n  --parentlink          If root Service has a link to a parent, link the imported Service Map (default: False)\n  --clobber             Overwrite Service Map (i.e. with same name) if it already exists (default: False)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n### Example\n\n```shell\n% opcli cloneservicemaps --env myenv --name HUB --replace HUB HUBCOPY --parentlink\n```\n# <a id="transformsvcmap"></a>transformsvcmap      \nApply regex replacements to an exported Service Map and create a new transformed export file with the changes.  Note that no credentials are required for this command since it is just operating on local export files.\n```shell\nusage: opcli transformsvcmap [-h] src dest --replace REGEX REPLACEWITH [--clobber]\n\npositional arguments:\n  src                   Source: File path where a Service Map was previously exported\n  dest                  Destination: File path where the transformed export will be saved\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --replace REGEX REPLACEWITH\n                        Transforming regex pattern and replacement string (option can be repeated) (default: None)\n  --clobber             Overwrite dest file if it already exists (default: False)\n```\n# <a id="getservicemaps"></a>getservicemaps       \nGet Service Map definitions\n```shell\nusage: opcli getservicemaps [-h] --env ENV [--secure SECURE] [--envfile ENVFILE]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getchildsvcgroups"></a>getchildsvcgroups    \nGet child Service Groups of a parent Service\n```shell\nusage: opcli getchildsvcgroups [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --parent PARENT\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --parent PARENT    ID of the parent Service Map/Group (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getservicegroup"></a>getservicegroup      \nGet the full definition of a Service Group\n```shell\nusage: opcli getservicegroup [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --id ID\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --id ID            ID of the Service Map/Group (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="exportcustattrfile"></a>exportcustattrfile   \nGenerate an Excel or csv file from existing custom attribute values\n```shell\nusage: opcli exportcustattrfile [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--query QUERY] [--search SEARCH] [--filter FILTER] [--filename FILENAME]\n\nCommand-specific arguments:\n  -h, --help           show this help message and exit\n  --secure SECURE      Whether or not to verify SSL cert (default: True)\n  --query QUERY        Query String to filter resources as per https://develop.opsramp.com/resource-management/tenants-tenantid-resources-search (default: None)\n  --search SEARCH      Search String to filter resources as it would be entered under Resources -> Search (default: None)\n  --filter FILTER      Post-query filter on resources. Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod") (default: None)\n  --filename FILENAME  Name of excel file to generate (.xlsx extension will be added) (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="importcustattrfile"></a>importcustattrfile   \nImport an Excel file containing custom attribute values\n```shell\nusage: opcli importcustattrfile [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--commit] [--writeblanks] [--filename FILENAME]\n\nCommand-specific arguments:\n  -h, --help           show this help message and exit\n  --secure SECURE      Whether or not to verify SSL cert (default: True)\n  --commit             Make the actual updates on the platform. If not specified, only error checking and import simulation will occur. (default: False)\n  --writeblanks        When no value is provided in the spreadsheet for a resource, remove any existing value for that resource on the platform. If not specified then no action is taken for empty values. (default: False)\n  --filename FILENAME  Name of excel file to import (.xlsx extension will be added if not specified.) (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getcustomattrs"></a>getcustomattrs       \nGet custom attribute definitions\n```shell\nusage: opcli getcustomattrs [-h] --env ENV [--secure SECURE] [--envfile ENVFILE]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getdiscoprofile"></a>getdiscoprofile      \nGet discovery profile definition\n```shell\nusage: opcli getdiscoprofile [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] --id ID --tenantId TENANTID\n\nCommand-specific arguments:\n  -h, --help           show this help message and exit\n  --secure SECURE      Whether or not to verify SSL cert (default: True)\n  --id ID              Discovery profile ID (default: None)\n  --tenantId TENANTID  Client ID or MSP ID of the tenant (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="getalertesc"></a>getalertesc          \nSearch and get Escalation Policy definitions\n```shell\nusage: opcli getalertesc [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--query QUERY] [--details] [--count] [--filter FILTER]\n\nCommand-specific arguments:\n  -h, --help         show this help message and exit\n  --secure SECURE    Whether or not to verify SSL cert (default: True)\n  --query QUERY      Query String to filter alerts (default: None)\n  --details          Get the full details for all matched policies (default: False)\n  --count            Only show the count of matching alerts (default: False)\n  --filter FILTER    Post-query filter on alerts. Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod") (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="migratealertesc"></a>migratealertesc      \nMigrate/copy Escalation Policies within same tenant or from one tenant to another\n```shell\nusage: opcli migratealertesc [-h] --env ENV [--secure SECURE] [--envfile ENVFILE] [--query QUERY] [--filter FILTER] [--preexec PREEXEC] [--postexec POSTEXEC] --to_env TO_ENV [--test] [--update] [--setactive SETACTIVE]\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n  --query QUERY         Query string to filter policies from source/from instance (default: None)\n  --filter FILTER       Filter for which policies to migrate. Python expression that will evaluate to True or False such as alert["resource"]["name"].startswith("prod") (default: None)\n  --preexec PREEXEC     Pre-mapped exec command (default: None)\n  --postexec POSTEXEC   Post-mapped exec command (default: None)\n  --to_env TO_ENV       Target environment to which policy definitions will be migrated. (--env option defines the source/from environment) (default: None)\n  --test                Test run only. Will check object mappings for missing items and not actually change the target instance. (default: False)\n  --update              Used for bulk updates, will only work if --env and --to_env are the same. Try to update existing policies instead of creating new ones. (default: False)\n  --setactive SETACTIVE\n                        Specify ON or OFF. Will force all policies created on the target to be ON or OFF. Otherwise will be set the same as the source. (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n```\n# <a id="clonetemplates"></a>clonetemplates\nClone monitoring templates\n```shell\n usage: opcli clonetemplates [-h] [--env ENV] [--envfile ENVFILE] [--url URL] [--client_id KEY] [--client_secret SCRT] [--tenant TENANT] [--partner PARTNER] [--secure SECURE] (--name NAME | --infile INFILE)\n                            (--prefix PREFIX | --copyname COPYNAME)\n\nCommand-specific arguments:\n  -h, --help            show this help message and exit\n  --secure SECURE       Whether or not to verify SSL cert (default: True)\n  --name NAME           Name of the Monitoring Template to clone (default: None)\n  --infile INFILE       File containing list of templates to clone (requires use of --prefix option) (default: None)\n  --prefix PREFIX       New template name will be same as original name but with this text prepended (default: None)\n  --copyname COPYNAME   New template will have this as its name (default: None)\n\nSpecify credentials via YAML file:\n  --env ENV             Name of environment to use, as defined in your environments.yml file (default: None)\n  --envfile ENVFILE     Location of environments YAML file (default: environments.yml)\n\nSpecify credentials via command line:\n  --url URL             OpsRamp API URL (default: None)\n  --client_id KEY       OpsRamp API Key (default: None)\n  --client_secret SCRT  OpsRamp API Secret (default: None)\n  --tenant TENANT       OpsRamp tenant ID (default: None)\n  --partner PARTNER     OpsRamp partner ID (usually unnecessary - only needed for partner-level API calls) (default: None)\n  ```\n\n\n',
     'author': 'Michael Friedhoff',
     'author_email': 'michael.friedhoff@opsramp.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `opsrampcli-0.8.1/PKG-INFO` & `opsrampcli-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: opsrampcli
-Version: 0.8.1
+Version: 0.9.0
 Summary: A command line interface for OpsRamp
 License: MIT
 Author: Michael Friedhoff
 Author-email: michael.friedhoff@opsramp.com
 Requires-Python: >=3.7.1,<4.0.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

