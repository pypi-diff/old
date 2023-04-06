# Comparing `tmp/alibabacloud_ga20191120_py2-1.0.8.tar.gz` & `tmp/alibabacloud_ga20191120_py2-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_ga20191120_py2-1.0.8.tar", last modified: Mon Dec 20 03:05:31 2021, max compression
+gzip compressed data, was "dist/alibabacloud_ga20191120_py2-1.0.9.tar", last modified: Thu Jan  6 08:45:29 2022, max compression
```

## Comparing `alibabacloud_ga20191120_py2-1.0.8.tar` & `alibabacloud_ga20191120_py2-1.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/
--rw-r--r--   0 root         (0) root         (0)    95107 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/client.py
--rw-r--r--   0 root         (0) root         (0)   508815 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/models.py
--rw-r--r--   0 root         (0) root         (0)       21 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/__init__.py
--rw-r--r--   0 root         (0) root         (0)      588 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1113 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/README.md
--rw-r--r--   0 root         (0) root         (0)     2443 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       28 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1030 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     2915 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/
--rw-r--r--   0 root         (0) root         (0)       24 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     2443 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      432 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      175 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       94 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      374 2021-12-20 03:05:31.000000 alibabacloud_ga20191120_py2-1.0.8/ChangeLog.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/
+-rw-r--r--   0 root         (0) root         (0)   132568 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/client.py
+-rw-r--r--   0 root         (0) root         (0)   550490 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/models.py
+-rw-r--r--   0 root         (0) root         (0)       21 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      588 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1113 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/README.md
+-rw-r--r--   0 root         (0) root         (0)     2443 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)       28 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1030 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     2915 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/
+-rw-r--r--   0 root         (0) root         (0)       24 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     2443 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      432 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      175 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       94 2022-01-06 08:45:29.000000 alibabacloud_ga20191120_py2-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      534 2022-01-06 08:45:28.000000 alibabacloud_ga20191120_py2-1.0.9/ChangeLog.md
```

### Comparing `alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/client.py` & `alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/client.py`

 * *Files 26% similar despite different names*

```diff
@@ -29,19 +29,24 @@
         if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
             return endpoint_map.get(region_id)
         return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
 
     def add_entries_to_acl_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclEntries'] = request.acl_entries
-        query['AclId'] = request.acl_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_entries):
+            query['AclEntries'] = request.acl_entries
+        if not UtilClient.is_unset(request.acl_id):
+            query['AclId'] = request.acl_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='AddEntriesToAcl',
             version='2019-11-20',
             protocol='HTTPS',
@@ -60,20 +65,26 @@
     def add_entries_to_acl(self, request):
         runtime = util_models.RuntimeOptions()
         return self.add_entries_to_acl_with_options(request, runtime)
 
     def associate_acls_with_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclIds'] = request.acl_ids
-        query['AclType'] = request.acl_type
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_ids):
+            query['AclIds'] = request.acl_ids
+        if not UtilClient.is_unset(request.acl_type):
+            query['AclType'] = request.acl_type
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='AssociateAclsWithListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -92,19 +103,24 @@
     def associate_acls_with_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.associate_acls_with_listener_with_options(request, runtime)
 
     def associate_additional_certificates_with_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['Certificates'] = request.certificates
-        query['ClientToken'] = request.client_token
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.certificates):
+            query['Certificates'] = request.certificates
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='AssociateAdditionalCertificatesWithListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -123,18 +139,22 @@
     def associate_additional_certificates_with_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.associate_additional_certificates_with_listener_with_options(request, runtime)
 
     def attach_ddos_to_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['DdosId'] = request.ddos_id
-        query['DdosRegionId'] = request.ddos_region_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.ddos_id):
+            query['DdosId'] = request.ddos_id
+        if not UtilClient.is_unset(request.ddos_region_id):
+            query['DdosRegionId'] = request.ddos_region_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='AttachDdosToAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -153,22 +173,30 @@
     def attach_ddos_to_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.attach_ddos_to_accelerator_with_options(request, runtime)
 
     def attach_log_store_to_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['EndpointGroupIds'] = request.endpoint_group_ids
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
-        query['SlsLogStoreName'] = request.sls_log_store_name
-        query['SlsProjectName'] = request.sls_project_name
-        query['SlsRegionId'] = request.sls_region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.endpoint_group_ids):
+            query['EndpointGroupIds'] = request.endpoint_group_ids
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.sls_log_store_name):
+            query['SlsLogStoreName'] = request.sls_log_store_name
+        if not UtilClient.is_unset(request.sls_project_name):
+            query['SlsProjectName'] = request.sls_project_name
+        if not UtilClient.is_unset(request.sls_region_id):
+            query['SlsRegionId'] = request.sls_region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='AttachLogStoreToEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -187,17 +215,20 @@
     def attach_log_store_to_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.attach_log_store_to_endpoint_group_with_options(request, runtime)
 
     def bandwidth_package_add_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='BandwidthPackageAddAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -216,17 +247,20 @@
     def bandwidth_package_add_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.bandwidth_package_add_accelerator_with_options(request, runtime)
 
     def bandwidth_package_remove_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='BandwidthPackageRemoveAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -245,22 +279,30 @@
     def bandwidth_package_remove_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.bandwidth_package_remove_accelerator_with_options(request, runtime)
 
     def config_endpoint_probe_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['Enable'] = request.enable
-        query['Endpoint'] = request.endpoint
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['EndpointType'] = request.endpoint_type
-        query['ProbePort'] = request.probe_port
-        query['ProbeProtocol'] = request.probe_protocol
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.enable):
+            query['Enable'] = request.enable
+        if not UtilClient.is_unset(request.endpoint):
+            query['Endpoint'] = request.endpoint
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.endpoint_type):
+            query['EndpointType'] = request.endpoint_type
+        if not UtilClient.is_unset(request.probe_port):
+            query['ProbePort'] = request.probe_port
+        if not UtilClient.is_unset(request.probe_protocol):
+            query['ProbeProtocol'] = request.probe_protocol
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ConfigEndpointProbe',
             version='2019-11-20',
             protocol='HTTPS',
@@ -279,24 +321,34 @@
     def config_endpoint_probe(self, request):
         runtime = util_models.RuntimeOptions()
         return self.config_endpoint_probe_with_options(request, runtime)
 
     def create_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AutoPay'] = request.auto_pay
-        query['AutoRenew'] = request.auto_renew
-        query['AutoRenewDuration'] = request.auto_renew_duration
-        query['AutoUseCoupon'] = request.auto_use_coupon
-        query['ClientToken'] = request.client_token
-        query['Duration'] = request.duration
-        query['Name'] = request.name
-        query['PricingCycle'] = request.pricing_cycle
-        query['RegionId'] = request.region_id
-        query['Spec'] = request.spec
+        if not UtilClient.is_unset(request.auto_pay):
+            query['AutoPay'] = request.auto_pay
+        if not UtilClient.is_unset(request.auto_renew):
+            query['AutoRenew'] = request.auto_renew
+        if not UtilClient.is_unset(request.auto_renew_duration):
+            query['AutoRenewDuration'] = request.auto_renew_duration
+        if not UtilClient.is_unset(request.auto_use_coupon):
+            query['AutoUseCoupon'] = request.auto_use_coupon
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.duration):
+            query['Duration'] = request.duration
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.pricing_cycle):
+            query['PricingCycle'] = request.pricing_cycle
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.spec):
+            query['Spec'] = request.spec
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -315,20 +367,26 @@
     def create_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_accelerator_with_options(request, runtime)
 
     def create_acl_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclEntries'] = request.acl_entries
-        query['AclName'] = request.acl_name
-        query['AddressIPVersion'] = request.address_ipversion
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_entries):
+            query['AclEntries'] = request.acl_entries
+        if not UtilClient.is_unset(request.acl_name):
+            query['AclName'] = request.acl_name
+        if not UtilClient.is_unset(request.address_ipversion):
+            query['AddressIPVersion'] = request.address_ipversion
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateAcl',
             version='2019-11-20',
             protocol='HTTPS',
@@ -344,31 +402,87 @@
             self.call_api(params, req, runtime)
         )
 
     def create_acl(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_acl_with_options(request, runtime)
 
+    def create_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.address):
+            query['Address'] = request.address
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.detect_threshold):
+            query['DetectThreshold'] = request.detect_threshold
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.options_json):
+            query['OptionsJson'] = request.options_json
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_name):
+            query['TaskName'] = request.task_name
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='CreateApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.CreateApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def create_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.create_application_monitor_with_options(request, runtime)
+
     def create_bandwidth_package_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AutoPay'] = request.auto_pay
-        query['AutoUseCoupon'] = request.auto_use_coupon
-        query['Bandwidth'] = request.bandwidth
-        query['BandwidthType'] = request.bandwidth_type
-        query['BillingType'] = request.billing_type
-        query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
-        query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
-        query['ChargeType'] = request.charge_type
-        query['ClientToken'] = request.client_token
-        query['Duration'] = request.duration
-        query['PricingCycle'] = request.pricing_cycle
-        query['Ratio'] = request.ratio
-        query['RegionId'] = request.region_id
-        query['Type'] = request.type
+        if not UtilClient.is_unset(request.auto_pay):
+            query['AutoPay'] = request.auto_pay
+        if not UtilClient.is_unset(request.auto_use_coupon):
+            query['AutoUseCoupon'] = request.auto_use_coupon
+        if not UtilClient.is_unset(request.bandwidth):
+            query['Bandwidth'] = request.bandwidth
+        if not UtilClient.is_unset(request.bandwidth_type):
+            query['BandwidthType'] = request.bandwidth_type
+        if not UtilClient.is_unset(request.billing_type):
+            query['BillingType'] = request.billing_type
+        if not UtilClient.is_unset(request.cbn_geographic_region_id_a):
+            query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
+        if not UtilClient.is_unset(request.cbn_geographic_region_id_b):
+            query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
+        if not UtilClient.is_unset(request.charge_type):
+            query['ChargeType'] = request.charge_type
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.duration):
+            query['Duration'] = request.duration
+        if not UtilClient.is_unset(request.pricing_cycle):
+            query['PricingCycle'] = request.pricing_cycle
+        if not UtilClient.is_unset(request.ratio):
+            query['Ratio'] = request.ratio
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.type):
+            query['Type'] = request.type
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateBandwidthPackage',
             version='2019-11-20',
             protocol='HTTPS',
@@ -387,22 +501,30 @@
     def create_bandwidth_package(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_bandwidth_package_with_options(request, runtime)
 
     def create_basic_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AutoPay'] = request.auto_pay
-        query['AutoRenew'] = request.auto_renew
-        query['AutoRenewDuration'] = request.auto_renew_duration
-        query['AutoUseCoupon'] = request.auto_use_coupon
-        query['ClientToken'] = request.client_token
-        query['Duration'] = request.duration
-        query['PricingCycle'] = request.pricing_cycle
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.auto_pay):
+            query['AutoPay'] = request.auto_pay
+        if not UtilClient.is_unset(request.auto_renew):
+            query['AutoRenew'] = request.auto_renew
+        if not UtilClient.is_unset(request.auto_renew_duration):
+            query['AutoRenewDuration'] = request.auto_renew_duration
+        if not UtilClient.is_unset(request.auto_use_coupon):
+            query['AutoUseCoupon'] = request.auto_use_coupon
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.duration):
+            query['Duration'] = request.duration
+        if not UtilClient.is_unset(request.pricing_cycle):
+            query['PricingCycle'] = request.pricing_cycle
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateBasicAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -421,22 +543,30 @@
     def create_basic_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_basic_accelerator_with_options(request, runtime)
 
     def create_basic_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['EndpointAddress'] = request.endpoint_address
-        query['EndpointGroupRegion'] = request.endpoint_group_region
-        query['EndpointType'] = request.endpoint_type
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.endpoint_address):
+            query['EndpointAddress'] = request.endpoint_address
+        if not UtilClient.is_unset(request.endpoint_group_region):
+            query['EndpointGroupRegion'] = request.endpoint_group_region
+        if not UtilClient.is_unset(request.endpoint_type):
+            query['EndpointType'] = request.endpoint_type
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateBasicEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -455,18 +585,22 @@
     def create_basic_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_basic_endpoint_group_with_options(request, runtime)
 
     def create_basic_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AccelerateRegionId'] = request.accelerate_region_id
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerate_region_id):
+            query['AccelerateRegionId'] = request.accelerate_region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateBasicIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -485,32 +619,50 @@
     def create_basic_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_basic_ip_set_with_options(request, runtime)
 
     def create_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['EndpointConfigurations'] = request.endpoint_configurations
-        query['EndpointGroupRegion'] = request.endpoint_group_region
-        query['EndpointGroupType'] = request.endpoint_group_type
-        query['EndpointRequestProtocol'] = request.endpoint_request_protocol
-        query['HealthCheckEnabled'] = request.health_check_enabled
-        query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
-        query['HealthCheckPath'] = request.health_check_path
-        query['HealthCheckPort'] = request.health_check_port
-        query['HealthCheckProtocol'] = request.health_check_protocol
-        query['ListenerId'] = request.listener_id
-        query['Name'] = request.name
-        query['PortOverrides'] = request.port_overrides
-        query['RegionId'] = request.region_id
-        query['ThresholdCount'] = request.threshold_count
-        query['TrafficPercentage'] = request.traffic_percentage
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.endpoint_configurations):
+            query['EndpointConfigurations'] = request.endpoint_configurations
+        if not UtilClient.is_unset(request.endpoint_group_region):
+            query['EndpointGroupRegion'] = request.endpoint_group_region
+        if not UtilClient.is_unset(request.endpoint_group_type):
+            query['EndpointGroupType'] = request.endpoint_group_type
+        if not UtilClient.is_unset(request.endpoint_request_protocol):
+            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
+        if not UtilClient.is_unset(request.health_check_enabled):
+            query['HealthCheckEnabled'] = request.health_check_enabled
+        if not UtilClient.is_unset(request.health_check_interval_seconds):
+            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
+        if not UtilClient.is_unset(request.health_check_path):
+            query['HealthCheckPath'] = request.health_check_path
+        if not UtilClient.is_unset(request.health_check_port):
+            query['HealthCheckPort'] = request.health_check_port
+        if not UtilClient.is_unset(request.health_check_protocol):
+            query['HealthCheckProtocol'] = request.health_check_protocol
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.port_overrides):
+            query['PortOverrides'] = request.port_overrides
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.threshold_count):
+            query['ThresholdCount'] = request.threshold_count
+        if not UtilClient.is_unset(request.traffic_percentage):
+            query['TrafficPercentage'] = request.traffic_percentage
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -529,20 +681,26 @@
     def create_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_endpoint_group_with_options(request, runtime)
 
     def create_endpoint_groups_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.endpoint_group_configurations):
+            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateEndpointGroups',
             version='2019-11-20',
             protocol='HTTPS',
@@ -561,19 +719,24 @@
     def create_endpoint_groups(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_endpoint_groups_with_options(request, runtime)
 
     def create_forwarding_rules_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['ForwardingRules'] = request.forwarding_rules
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.forwarding_rules):
+            query['ForwardingRules'] = request.forwarding_rules
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateForwardingRules',
             version='2019-11-20',
             protocol='HTTPS',
@@ -592,18 +755,22 @@
     def create_forwarding_rules(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_forwarding_rules_with_options(request, runtime)
 
     def create_ip_sets_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AccelerateRegion'] = request.accelerate_region
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerate_region):
+            query['AccelerateRegion'] = request.accelerate_region
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateIpSets',
             version='2019-11-20',
             protocol='HTTPS',
@@ -622,26 +789,38 @@
     def create_ip_sets(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_ip_sets_with_options(request, runtime)
 
     def create_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['Certificates'] = request.certificates
-        query['ClientAffinity'] = request.client_affinity
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['Name'] = request.name
-        query['PortRanges'] = request.port_ranges
-        query['Protocol'] = request.protocol
-        query['ProxyProtocol'] = request.proxy_protocol
-        query['RegionId'] = request.region_id
-        query['SecurityPolicyId'] = request.security_policy_id
-        query['XForwardedForConfig'] = request.xforwarded_for_config
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.certificates):
+            query['Certificates'] = request.certificates
+        if not UtilClient.is_unset(request.client_affinity):
+            query['ClientAffinity'] = request.client_affinity
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.port_ranges):
+            query['PortRanges'] = request.port_ranges
+        if not UtilClient.is_unset(request.protocol):
+            query['Protocol'] = request.protocol
+        if not UtilClient.is_unset(request.proxy_protocol):
+            query['ProxyProtocol'] = request.proxy_protocol
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.security_policy_id):
+            query['SecurityPolicyId'] = request.security_policy_id
+        if not UtilClient.is_unset(request.xforwarded_for_config):
+            query['XForwardedForConfig'] = request.xforwarded_for_config
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -660,19 +839,24 @@
     def create_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_listener_with_options(request, runtime)
 
     def create_spare_ips_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
-        query['SpareIps'] = request.spare_ips
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.spare_ips):
+            query['SpareIps'] = request.spare_ips
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateSpareIps',
             version='2019-11-20',
             protocol='HTTPS',
@@ -691,16 +875,18 @@
     def create_spare_ips(self, request):
         runtime = util_models.RuntimeOptions()
         return self.create_spare_ips_with_options(request, runtime)
 
     def delete_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -719,18 +905,22 @@
     def delete_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_accelerator_with_options(request, runtime)
 
     def delete_acl_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclId'] = request.acl_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_id):
+            query['AclId'] = request.acl_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteAcl',
             version='2019-11-20',
             protocol='HTTPS',
@@ -746,20 +936,55 @@
             self.call_api(params, req, runtime)
         )
 
     def delete_acl(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_acl_with_options(request, runtime)
 
+    def delete_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='DeleteApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.DeleteApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def delete_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.delete_application_monitor_with_options(request, runtime)
+
     def delete_bandwidth_package_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['ClientToken'] = request.client_token
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteBandwidthPackage',
             version='2019-11-20',
             protocol='HTTPS',
@@ -778,16 +1003,18 @@
     def delete_bandwidth_package(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_bandwidth_package_with_options(request, runtime)
 
     def delete_basic_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteBasicAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -806,16 +1033,18 @@
     def delete_basic_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_basic_accelerator_with_options(request, runtime)
 
     def delete_basic_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteBasicEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -834,17 +1063,20 @@
     def delete_basic_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_basic_endpoint_group_with_options(request, runtime)
 
     def delete_basic_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['IpSetId'] = request.ip_set_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.ip_set_id):
+            query['IpSetId'] = request.ip_set_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteBasicIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -863,17 +1095,20 @@
     def delete_basic_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_basic_ip_set_with_options(request, runtime)
 
     def delete_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -892,18 +1127,22 @@
     def delete_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_endpoint_group_with_options(request, runtime)
 
     def delete_endpoint_groups_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['EndpointGroupIds'] = request.endpoint_group_ids
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.endpoint_group_ids):
+            query['EndpointGroupIds'] = request.endpoint_group_ids
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteEndpointGroups',
             version='2019-11-20',
             protocol='HTTPS',
@@ -922,19 +1161,24 @@
     def delete_endpoint_groups(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_endpoint_groups_with_options(request, runtime)
 
     def delete_forwarding_rules_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['ForwardingRuleIds'] = request.forwarding_rule_ids
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.forwarding_rule_ids):
+            query['ForwardingRuleIds'] = request.forwarding_rule_ids
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteForwardingRules',
             version='2019-11-20',
             protocol='HTTPS',
@@ -953,18 +1197,22 @@
     def delete_forwarding_rules(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_forwarding_rules_with_options(request, runtime)
 
     def delete_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['IpSetId'] = request.ip_set_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.ip_set_id):
+            query['IpSetId'] = request.ip_set_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -983,16 +1231,18 @@
     def delete_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_ip_set_with_options(request, runtime)
 
     def delete_ip_sets_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['IpSetIds'] = request.ip_set_ids
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.ip_set_ids):
+            query['IpSetIds'] = request.ip_set_ids
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteIpSets',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1011,17 +1261,20 @@
     def delete_ip_sets(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_ip_sets_with_options(request, runtime)
 
     def delete_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1040,19 +1293,24 @@
     def delete_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_listener_with_options(request, runtime)
 
     def delete_spare_ips_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
-        query['SpareIps'] = request.spare_ips
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.spare_ips):
+            query['SpareIps'] = request.spare_ips
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteSpareIps',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1071,16 +1329,18 @@
     def delete_spare_ips(self, request):
         runtime = util_models.RuntimeOptions()
         return self.delete_spare_ips_with_options(request, runtime)
 
     def describe_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1099,16 +1359,18 @@
     def describe_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_accelerator_with_options(request, runtime)
 
     def describe_accelerator_auto_renew_attribute_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeAcceleratorAutoRenewAttribute',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1124,19 +1386,53 @@
             self.call_api(params, req, runtime)
         )
 
     def describe_accelerator_auto_renew_attribute(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_accelerator_auto_renew_attribute_with_options(request, runtime)
 
+    def describe_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='DescribeApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.DescribeApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def describe_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.describe_application_monitor_with_options(request, runtime)
+
     def describe_bandwidth_package_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeBandwidthPackage',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1155,16 +1451,18 @@
     def describe_bandwidth_package(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_bandwidth_package_with_options(request, runtime)
 
     def describe_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1183,16 +1481,18 @@
     def describe_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_endpoint_group_with_options(request, runtime)
 
     def describe_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['IpSetId'] = request.ip_set_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.ip_set_id):
+            query['IpSetId'] = request.ip_set_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1211,16 +1511,18 @@
     def describe_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_ip_set_with_options(request, runtime)
 
     def describe_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1239,15 +1541,16 @@
     def describe_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_listener_with_options(request, runtime)
 
     def describe_regions_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DescribeRegions',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1266,16 +1569,18 @@
     def describe_regions(self, request):
         runtime = util_models.RuntimeOptions()
         return self.describe_regions_with_options(request, runtime)
 
     def detach_ddos_from_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DetachDdosFromAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1294,19 +1599,24 @@
     def detach_ddos_from_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.detach_ddos_from_accelerator_with_options(request, runtime)
 
     def detach_log_store_from_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['EndpointGroupIds'] = request.endpoint_group_ids
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.endpoint_group_ids):
+            query['EndpointGroupIds'] = request.endpoint_group_ids
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DetachLogStoreFromEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1322,22 +1632,91 @@
             self.call_api(params, req, runtime)
         )
 
     def detach_log_store_from_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.detach_log_store_from_endpoint_group_with_options(request, runtime)
 
+    def detect_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='DetectApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.DetectApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def detect_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.detect_application_monitor_with_options(request, runtime)
+
+    def disable_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='DisableApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.DisableApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def disable_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.disable_application_monitor_with_options(request, runtime)
+
     def dissociate_acls_from_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclIds'] = request.acl_ids
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_ids):
+            query['AclIds'] = request.acl_ids
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DissociateAclsFromListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1356,19 +1735,24 @@
     def dissociate_acls_from_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.dissociate_acls_from_listener_with_options(request, runtime)
 
     def dissociate_additional_certificates_from_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['Domains'] = request.domains
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.domains):
+            query['Domains'] = request.domains
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DissociateAdditionalCertificatesFromListener',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1384,19 +1768,53 @@
             self.call_api(params, req, runtime)
         )
 
     def dissociate_additional_certificates_from_listener(self, request):
         runtime = util_models.RuntimeOptions()
         return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)
 
+    def enable_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='EnableApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.EnableApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def enable_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.enable_application_monitor_with_options(request, runtime)
+
     def get_acl_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclId'] = request.acl_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_id):
+            query['AclId'] = request.acl_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetAcl',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1415,16 +1833,18 @@
     def get_acl(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_acl_with_options(request, runtime)
 
     def get_basic_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetBasicAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1443,17 +1863,20 @@
     def get_basic_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_basic_accelerator_with_options(request, runtime)
 
     def get_basic_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetBasicEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1472,17 +1895,20 @@
     def get_basic_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_basic_endpoint_group_with_options(request, runtime)
 
     def get_basic_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['IpSetId'] = request.ip_set_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.ip_set_id):
+            query['IpSetId'] = request.ip_set_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetBasicIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1501,19 +1927,24 @@
     def get_basic_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_basic_ip_set_with_options(request, runtime)
 
     def get_health_status_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetHealthStatus',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1532,19 +1963,24 @@
     def get_health_status(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_health_status_with_options(request, runtime)
 
     def get_spare_ip_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
-        query['SpareIp'] = request.spare_ip
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.spare_ip):
+            query['SpareIp'] = request.spare_ip
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetSpareIp',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1563,15 +1999,16 @@
     def get_spare_ip(self, request):
         runtime = util_models.RuntimeOptions()
         return self.get_spare_ip_with_options(request, runtime)
 
     def list_accelerate_areas_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListAccelerateAreas',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1590,19 +2027,24 @@
     def list_accelerate_areas(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_accelerate_areas_with_options(request, runtime)
 
     def list_accelerators_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
-        query['State'] = request.state
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.state):
+            query['State'] = request.state
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListAccelerators',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1621,20 +2063,26 @@
     def list_accelerators(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_accelerators_with_options(request, runtime)
 
     def list_acls_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclIds'] = request.acl_ids
-        query['AclName'] = request.acl_name
-        query['ClientToken'] = request.client_token
-        query['MaxResults'] = request.max_results
-        query['NextToken'] = request.next_token
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_ids):
+            query['AclIds'] = request.acl_ids
+        if not UtilClient.is_unset(request.acl_name):
+            query['AclName'] = request.acl_name
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.max_results):
+            query['MaxResults'] = request.max_results
+        if not UtilClient.is_unset(request.next_token):
+            query['NextToken'] = request.next_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListAcls',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1650,19 +2098,93 @@
             self.call_api(params, req, runtime)
         )
 
     def list_acls(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_acls_with_options(request, runtime)
 
+    def list_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.search_value):
+            query['SearchValue'] = request.search_value
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='ListApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.ListApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def list_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.list_application_monitor_with_options(request, runtime)
+
+    def list_application_monitor_detect_result_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.begin_time):
+            query['BeginTime'] = request.begin_time
+        if not UtilClient.is_unset(request.end_time):
+            query['EndTime'] = request.end_time
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='ListApplicationMonitorDetectResult',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.ListApplicationMonitorDetectResultResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def list_application_monitor_detect_result(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.list_application_monitor_detect_result_with_options(request, runtime)
+
     def list_available_accelerate_areas_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListAvailableAccelerateAreas',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1681,16 +2203,18 @@
     def list_available_accelerate_areas(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_available_accelerate_areas_with_options(request, runtime)
 
     def list_available_busi_regions_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListAvailableBusiRegions',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1709,20 +2233,26 @@
     def list_available_busi_regions(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_available_busi_regions_with_options(request, runtime)
 
     def list_bandwidth_packages_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
-        query['State'] = request.state
-        query['Type'] = request.type
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.state):
+            query['State'] = request.state
+        if not UtilClient.is_unset(request.type):
+            query['Type'] = request.type
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListBandwidthPackages',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1741,17 +2271,20 @@
     def list_bandwidth_packages(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_bandwidth_packages_with_options(request, runtime)
 
     def list_bandwidthackages_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListBandwidthackages',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1770,19 +2303,24 @@
     def list_bandwidthackages(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_bandwidthackages_with_options(request, runtime)
 
     def list_basic_accelerators_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
-        query['State'] = request.state
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.state):
+            query['State'] = request.state
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListBasicAccelerators',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1801,15 +2339,16 @@
     def list_basic_accelerators(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_basic_accelerators_with_options(request, runtime)
 
     def list_busi_regions_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListBusiRegions',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1828,22 +2367,30 @@
     def list_busi_regions(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_busi_regions_with_options(request, runtime)
 
     def list_endpoint_groups_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['AccessLogSwitch'] = request.access_log_switch
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['EndpointGroupType'] = request.endpoint_group_type
-        query['ListenerId'] = request.listener_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.access_log_switch):
+            query['AccessLogSwitch'] = request.access_log_switch
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.endpoint_group_type):
+            query['EndpointGroupType'] = request.endpoint_group_type
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListEndpointGroups',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1862,21 +2409,28 @@
     def list_endpoint_groups(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_endpoint_groups_with_options(request, runtime)
 
     def list_forwarding_rules_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['ForwardingRuleId'] = request.forwarding_rule_id
-        query['ListenerId'] = request.listener_id
-        query['MaxResults'] = request.max_results
-        query['NextToken'] = request.next_token
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.forwarding_rule_id):
+            query['ForwardingRuleId'] = request.forwarding_rule_id
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.max_results):
+            query['MaxResults'] = request.max_results
+        if not UtilClient.is_unset(request.next_token):
+            query['NextToken'] = request.next_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListForwardingRules',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1895,18 +2449,22 @@
     def list_forwarding_rules(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_forwarding_rules_with_options(request, runtime)
 
     def list_ip_sets_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListIpSets',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1925,20 +2483,26 @@
     def list_ip_sets(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_ip_sets_with_options(request, runtime)
 
     def list_listener_certificates_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ListenerId'] = request.listener_id
-        query['MaxResults'] = request.max_results
-        query['NextToken'] = request.next_token
-        query['RegionId'] = request.region_id
-        query['Role'] = request.role
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.max_results):
+            query['MaxResults'] = request.max_results
+        if not UtilClient.is_unset(request.next_token):
+            query['NextToken'] = request.next_token
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.role):
+            query['Role'] = request.role
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListListenerCertificates',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1957,18 +2521,22 @@
     def list_listener_certificates(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_listener_certificates_with_options(request, runtime)
 
     def list_listeners_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListListeners',
             version='2019-11-20',
             protocol='HTTPS',
@@ -1987,18 +2555,22 @@
     def list_listeners(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_listeners_with_options(request, runtime)
 
     def list_spare_ips_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListSpareIps',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2017,17 +2589,20 @@
     def list_spare_ips(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_spare_ips_with_options(request, runtime)
 
     def list_system_security_policies_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['PageNumber'] = request.page_number
-        query['PageSize'] = request.page_size
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.page_number):
+            query['PageNumber'] = request.page_number
+        if not UtilClient.is_unset(request.page_size):
+            query['PageSize'] = request.page_size
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ListSystemSecurityPolicies',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2046,19 +2621,24 @@
     def list_system_security_policies(self, request):
         runtime = util_models.RuntimeOptions()
         return self.list_system_security_policies_with_options(request, runtime)
 
     def remove_entries_from_acl_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclEntries'] = request.acl_entries
-        query['AclId'] = request.acl_id
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_entries):
+            query['AclEntries'] = request.acl_entries
+        if not UtilClient.is_unset(request.acl_id):
+            query['AclId'] = request.acl_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='RemoveEntriesFromAcl',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2077,17 +2657,20 @@
     def remove_entries_from_acl(self, request):
         runtime = util_models.RuntimeOptions()
         return self.remove_entries_from_acl_with_options(request, runtime)
 
     def replace_bandwidth_package_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['RegionId'] = request.region_id
-        query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.target_bandwidth_package_id):
+            query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='ReplaceBandwidthPackage',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2106,22 +2689,30 @@
     def replace_bandwidth_package(self, request):
         runtime = util_models.RuntimeOptions()
         return self.replace_bandwidth_package_with_options(request, runtime)
 
     def update_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['AutoPay'] = request.auto_pay
-        query['AutoUseCoupon'] = request.auto_use_coupon
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
-        query['Spec'] = request.spec
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.auto_pay):
+            query['AutoPay'] = request.auto_pay
+        if not UtilClient.is_unset(request.auto_use_coupon):
+            query['AutoUseCoupon'] = request.auto_use_coupon
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.spec):
+            query['Spec'] = request.spec
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2140,21 +2731,28 @@
     def update_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_accelerator_with_options(request, runtime)
 
     def update_accelerator_auto_renew_attribute_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['AutoRenew'] = request.auto_renew
-        query['AutoRenewDuration'] = request.auto_renew_duration
-        query['ClientToken'] = request.client_token
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
-        query['RenewalStatus'] = request.renewal_status
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.auto_renew):
+            query['AutoRenew'] = request.auto_renew
+        if not UtilClient.is_unset(request.auto_renew_duration):
+            query['AutoRenewDuration'] = request.auto_renew_duration
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.renewal_status):
+            query['RenewalStatus'] = request.renewal_status
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateAcceleratorAutoRenewAttribute',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2173,16 +2771,18 @@
     def update_accelerator_auto_renew_attribute(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_accelerator_auto_renew_attribute_with_options(request, runtime)
 
     def update_accelerator_confirm_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateAcceleratorConfirm',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2201,19 +2801,24 @@
     def update_accelerator_confirm(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_accelerator_confirm_with_options(request, runtime)
 
     def update_acl_attribute_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AclId'] = request.acl_id
-        query['AclName'] = request.acl_name
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.acl_id):
+            query['AclId'] = request.acl_id
+        if not UtilClient.is_unset(request.acl_name):
+            query['AclName'] = request.acl_name
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateAclAttribute',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2229,25 +2834,75 @@
             self.call_api(params, req, runtime)
         )
 
     def update_acl_attribute(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_acl_attribute_with_options(request, runtime)
 
+    def update_application_monitor_with_options(self, request, runtime):
+        UtilClient.validate_model(request)
+        query = {}
+        if not UtilClient.is_unset(request.address):
+            query['Address'] = request.address
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.detect_threshold):
+            query['DetectThreshold'] = request.detect_threshold
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.options_json):
+            query['OptionsJson'] = request.options_json
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.task_id):
+            query['TaskId'] = request.task_id
+        if not UtilClient.is_unset(request.task_name):
+            query['TaskName'] = request.task_name
+        req = open_api_models.OpenApiRequest(
+            query=OpenApiUtilClient.query(query)
+        )
+        params = open_api_models.Params(
+            action='UpdateApplicationMonitor',
+            version='2019-11-20',
+            protocol='HTTPS',
+            pathname='/',
+            method='POST',
+            auth_type='AK',
+            style='RPC',
+            req_body_type='formData',
+            body_type='json'
+        )
+        return TeaCore.from_map(
+            ga_20191120_models.UpdateApplicationMonitorResponse(),
+            self.call_api(params, req, runtime)
+        )
+
+    def update_application_monitor(self, request):
+        runtime = util_models.RuntimeOptions()
+        return self.update_application_monitor_with_options(request, runtime)
+
     def update_bandwidth_package_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AutoPay'] = request.auto_pay
-        query['AutoUseCoupon'] = request.auto_use_coupon
-        query['Bandwidth'] = request.bandwidth
-        query['BandwidthPackageId'] = request.bandwidth_package_id
-        query['BandwidthType'] = request.bandwidth_type
-        query['Description'] = request.description
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.auto_pay):
+            query['AutoPay'] = request.auto_pay
+        if not UtilClient.is_unset(request.auto_use_coupon):
+            query['AutoUseCoupon'] = request.auto_use_coupon
+        if not UtilClient.is_unset(request.bandwidth):
+            query['Bandwidth'] = request.bandwidth
+        if not UtilClient.is_unset(request.bandwidth_package_id):
+            query['BandwidthPackageId'] = request.bandwidth_package_id
+        if not UtilClient.is_unset(request.bandwidth_type):
+            query['BandwidthType'] = request.bandwidth_type
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateBandwidthPackage',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2266,19 +2921,24 @@
     def update_bandwidth_package(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_bandwidth_package_with_options(request, runtime)
 
     def update_basic_accelerator_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateBasicAccelerator',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2297,21 +2957,28 @@
     def update_basic_accelerator(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_basic_accelerator_with_options(request, runtime)
 
     def update_basic_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['EndpointAddress'] = request.endpoint_address
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['EndpointType'] = request.endpoint_type
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.endpoint_address):
+            query['EndpointAddress'] = request.endpoint_address
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.endpoint_type):
+            query['EndpointType'] = request.endpoint_type
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateBasicEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2330,30 +2997,46 @@
     def update_basic_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_basic_endpoint_group_with_options(request, runtime)
 
     def update_endpoint_group_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['EndpointConfigurations'] = request.endpoint_configurations
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['EndpointGroupRegion'] = request.endpoint_group_region
-        query['EndpointRequestProtocol'] = request.endpoint_request_protocol
-        query['HealthCheckEnabled'] = request.health_check_enabled
-        query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
-        query['HealthCheckPath'] = request.health_check_path
-        query['HealthCheckPort'] = request.health_check_port
-        query['HealthCheckProtocol'] = request.health_check_protocol
-        query['Name'] = request.name
-        query['PortOverrides'] = request.port_overrides
-        query['RegionId'] = request.region_id
-        query['ThresholdCount'] = request.threshold_count
-        query['TrafficPercentage'] = request.traffic_percentage
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.endpoint_configurations):
+            query['EndpointConfigurations'] = request.endpoint_configurations
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.endpoint_group_region):
+            query['EndpointGroupRegion'] = request.endpoint_group_region
+        if not UtilClient.is_unset(request.endpoint_request_protocol):
+            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
+        if not UtilClient.is_unset(request.health_check_enabled):
+            query['HealthCheckEnabled'] = request.health_check_enabled
+        if not UtilClient.is_unset(request.health_check_interval_seconds):
+            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
+        if not UtilClient.is_unset(request.health_check_path):
+            query['HealthCheckPath'] = request.health_check_path
+        if not UtilClient.is_unset(request.health_check_port):
+            query['HealthCheckPort'] = request.health_check_port
+        if not UtilClient.is_unset(request.health_check_protocol):
+            query['HealthCheckProtocol'] = request.health_check_protocol
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.port_overrides):
+            query['PortOverrides'] = request.port_overrides
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.threshold_count):
+            query['ThresholdCount'] = request.threshold_count
+        if not UtilClient.is_unset(request.traffic_percentage):
+            query['TrafficPercentage'] = request.traffic_percentage
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateEndpointGroup',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2372,19 +3055,24 @@
     def update_endpoint_group(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_endpoint_group_with_options(request, runtime)
 
     def update_endpoint_group_attribute_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['EndpointGroupId'] = request.endpoint_group_id
-        query['Name'] = request.name
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.endpoint_group_id):
+            query['EndpointGroupId'] = request.endpoint_group_id
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateEndpointGroupAttribute',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2403,19 +3091,24 @@
     def update_endpoint_group_attribute(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_endpoint_group_attribute_with_options(request, runtime)
 
     def update_endpoint_groups_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['ClientToken'] = request.client_token
-        query['DryRun'] = request.dry_run
-        query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.dry_run):
+            query['DryRun'] = request.dry_run
+        if not UtilClient.is_unset(request.endpoint_group_configurations):
+            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateEndpointGroups',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2434,19 +3127,24 @@
     def update_endpoint_groups(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_endpoint_groups_with_options(request, runtime)
 
     def update_forwarding_rules_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['AcceleratorId'] = request.accelerator_id
-        query['ClientToken'] = request.client_token
-        query['ForwardingRules'] = request.forwarding_rules
-        query['ListenerId'] = request.listener_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.accelerator_id):
+            query['AcceleratorId'] = request.accelerator_id
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.forwarding_rules):
+            query['ForwardingRules'] = request.forwarding_rules
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateForwardingRules',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2465,18 +3163,22 @@
     def update_forwarding_rules(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_forwarding_rules_with_options(request, runtime)
 
     def update_ip_set_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['Bandwidth'] = request.bandwidth
-        query['ClientToken'] = request.client_token
-        query['IpSetId'] = request.ip_set_id
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.bandwidth):
+            query['Bandwidth'] = request.bandwidth
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.ip_set_id):
+            query['IpSetId'] = request.ip_set_id
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateIpSet',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2495,16 +3197,18 @@
     def update_ip_set(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_ip_set_with_options(request, runtime)
 
     def update_ip_sets_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['IpSets'] = request.ip_sets
-        query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.ip_sets):
+            query['IpSets'] = request.ip_sets
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateIpSets',
             version='2019-11-20',
             protocol='HTTPS',
@@ -2523,27 +3227,40 @@
     def update_ip_sets(self, request):
         runtime = util_models.RuntimeOptions()
         return self.update_ip_sets_with_options(request, runtime)
 
     def update_listener_with_options(self, request, runtime):
         UtilClient.validate_model(request)
         query = {}
-        query['BackendPorts'] = request.backend_ports
-        query['Certificates'] = request.certificates
-        query['ClientAffinity'] = request.client_affinity
-        query['ClientToken'] = request.client_token
-        query['Description'] = request.description
-        query['ListenerId'] = request.listener_id
-        query['Name'] = request.name
-        query['PortRanges'] = request.port_ranges
-        query['Protocol'] = request.protocol
-        query['ProxyProtocol'] = request.proxy_protocol
-        query['RegionId'] = request.region_id
-        query['SecurityPolicyId'] = request.security_policy_id
-        query['XForwardedForConfig'] = request.xforwarded_for_config
+        if not UtilClient.is_unset(request.backend_ports):
+            query['BackendPorts'] = request.backend_ports
+        if not UtilClient.is_unset(request.certificates):
+            query['Certificates'] = request.certificates
+        if not UtilClient.is_unset(request.client_affinity):
+            query['ClientAffinity'] = request.client_affinity
+        if not UtilClient.is_unset(request.client_token):
+            query['ClientToken'] = request.client_token
+        if not UtilClient.is_unset(request.description):
+            query['Description'] = request.description
+        if not UtilClient.is_unset(request.listener_id):
+            query['ListenerId'] = request.listener_id
+        if not UtilClient.is_unset(request.name):
+            query['Name'] = request.name
+        if not UtilClient.is_unset(request.port_ranges):
+            query['PortRanges'] = request.port_ranges
+        if not UtilClient.is_unset(request.protocol):
+            query['Protocol'] = request.protocol
+        if not UtilClient.is_unset(request.proxy_protocol):
+            query['ProxyProtocol'] = request.proxy_protocol
+        if not UtilClient.is_unset(request.region_id):
+            query['RegionId'] = request.region_id
+        if not UtilClient.is_unset(request.security_policy_id):
+            query['SecurityPolicyId'] = request.security_policy_id
+        if not UtilClient.is_unset(request.xforwarded_for_config):
+            query['XForwardedForConfig'] = request.xforwarded_for_config
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='UpdateListener',
             version='2019-11-20',
             protocol='HTTPS',
```

### Comparing `alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120/models.py` & `alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -1234,14 +1234,137 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = CreateAclResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class CreateApplicationMonitorRequest(TeaModel):
+    def __init__(self, accelerator_id=None, address=None, client_token=None, detect_threshold=None,
+                 listener_id=None, options_json=None, region_id=None, task_name=None):
+        self.accelerator_id = accelerator_id  # type: str
+        self.address = address  # type: str
+        self.client_token = client_token  # type: str
+        self.detect_threshold = detect_threshold  # type: int
+        self.listener_id = listener_id  # type: str
+        self.options_json = options_json  # type: str
+        self.region_id = region_id  # type: str
+        self.task_name = task_name  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(CreateApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class CreateApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None, task_id=None):
+        # Id of the request
+        self.request_id = request_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(CreateApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class CreateApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: CreateApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(CreateApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = CreateApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class CreateBandwidthPackageRequest(TeaModel):
     def __init__(self, auto_pay=None, auto_use_coupon=None, bandwidth=None, bandwidth_type=None, billing_type=None,
                  cbn_geographic_region_id_a=None, cbn_geographic_region_id_b=None, charge_type=None, client_token=None, duration=None,
                  pricing_cycle=None, ratio=None, region_id=None, type=None):
         self.auto_pay = auto_pay  # type: bool
         self.auto_use_coupon = auto_use_coupon  # type: str
         self.bandwidth = bandwidth  # type: int
@@ -3461,14 +3584,105 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DeleteAclResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DeleteApplicationMonitorRequest(TeaModel):
+    def __init__(self, client_token=None, region_id=None, task_id=None):
+        self.client_token = client_token  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DeleteApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DeleteApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None):
+        self.request_id = request_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DeleteApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DeleteApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: DeleteApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(DeleteApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DeleteApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DeleteBandwidthPackageRequest(TeaModel):
     def __init__(self, bandwidth_package_id=None, client_token=None, region_id=None):
         self.bandwidth_package_id = bandwidth_package_id  # type: str
         self.client_token = client_token  # type: str
         self.region_id = region_id  # type: str
 
     def validate(self):
@@ -4876,14 +5090,198 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DescribeAcceleratorAutoRenewAttributeResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DescribeApplicationMonitorRequest(TeaModel):
+    def __init__(self, client_token=None, region_id=None, task_id=None):
+        self.client_token = client_token  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DescribeApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DescribeApplicationMonitorResponseBodyIspCityList(TeaModel):
+    def __init__(self, city=None, city_name=None, isp=None, isp_name=None):
+        self.city = city  # type: str
+        self.city_name = city_name  # type: str
+        self.isp = isp  # type: str
+        self.isp_name = isp_name  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DescribeApplicationMonitorResponseBodyIspCityList, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.city is not None:
+            result['City'] = self.city
+        if self.city_name is not None:
+            result['CityName'] = self.city_name
+        if self.isp is not None:
+            result['Isp'] = self.isp
+        if self.isp_name is not None:
+            result['IspName'] = self.isp_name
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('City') is not None:
+            self.city = m.get('City')
+        if m.get('CityName') is not None:
+            self.city_name = m.get('CityName')
+        if m.get('Isp') is not None:
+            self.isp = m.get('Isp')
+        if m.get('IspName') is not None:
+            self.isp_name = m.get('IspName')
+        return self
+
+
+class DescribeApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, accelerator_id=None, address=None, detect_threshold=None, isp_city_list=None,
+                 listener_id=None, options_json=None, region_id=None, request_id=None, task_id=None, task_name=None):
+        self.accelerator_id = accelerator_id  # type: str
+        self.address = address  # type: str
+        self.detect_threshold = detect_threshold  # type: str
+        self.isp_city_list = isp_city_list  # type: list[DescribeApplicationMonitorResponseBodyIspCityList]
+        self.listener_id = listener_id  # type: str
+        self.options_json = options_json  # type: str
+        self.region_id = region_id  # type: str
+        self.request_id = request_id  # type: str
+        self.task_id = task_id  # type: str
+        self.task_name = task_name  # type: str
+
+    def validate(self):
+        if self.isp_city_list:
+            for k in self.isp_city_list:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super(DescribeApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        result['IspCityList'] = []
+        if self.isp_city_list is not None:
+            for k in self.isp_city_list:
+                result['IspCityList'].append(k.to_map() if k else None)
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        self.isp_city_list = []
+        if m.get('IspCityList') is not None:
+            for k in m.get('IspCityList'):
+                temp_model = DescribeApplicationMonitorResponseBodyIspCityList()
+                self.isp_city_list.append(temp_model.from_map(k))
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class DescribeApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: DescribeApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(DescribeApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DescribeApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DescribeBandwidthPackageRequest(TeaModel):
     def __init__(self, bandwidth_package_id=None, region_id=None):
         self.bandwidth_package_id = bandwidth_package_id  # type: str
         self.region_id = region_id  # type: str
 
     def validate(self):
         pass
@@ -6175,14 +6573,196 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DetachLogStoreFromEndpointGroupResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DetectApplicationMonitorRequest(TeaModel):
+    def __init__(self, client_token=None, region_id=None, task_id=None):
+        self.client_token = client_token  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DetectApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DetectApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None):
+        self.request_id = request_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DetectApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DetectApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: DetectApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(DetectApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DetectApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
+class DisableApplicationMonitorRequest(TeaModel):
+    def __init__(self, client_token=None, region_id=None, task_id=None):
+        self.client_token = client_token  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DisableApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DisableApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None):
+        self.request_id = request_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(DisableApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DisableApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: DisableApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(DisableApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DisableApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DissociateAclsFromListenerRequest(TeaModel):
     def __init__(self, acl_ids=None, client_token=None, dry_run=None, listener_id=None, region_id=None):
         self.acl_ids = acl_ids  # type: list[str]
         self.client_token = client_token  # type: str
         self.dry_run = dry_run  # type: bool
         self.listener_id = listener_id  # type: str
         self.region_id = region_id  # type: str
@@ -6389,14 +6969,105 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class EnableApplicationMonitorRequest(TeaModel):
+    def __init__(self, client_token=None, region_id=None, task_id=None):
+        self.client_token = client_token  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(EnableApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class EnableApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None):
+        self.request_id = request_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(EnableApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class EnableApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: EnableApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(EnableApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = EnableApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class GetAclRequest(TeaModel):
     def __init__(self, acl_id=None, region_id=None):
         self.acl_id = acl_id  # type: str
         self.region_id = region_id  # type: str
 
     def validate(self):
         pass
@@ -8088,14 +8759,390 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = ListAclsResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class ListApplicationMonitorRequest(TeaModel):
+    def __init__(self, page_number=None, page_size=None, region_id=None, search_value=None):
+        self.page_number = page_number  # type: int
+        self.page_size = page_size  # type: int
+        self.region_id = region_id  # type: str
+        self.search_value = search_value  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.search_value is not None:
+            result['SearchValue'] = self.search_value
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('SearchValue') is not None:
+            self.search_value = m.get('SearchValue')
+        return self
+
+
+class ListApplicationMonitorResponseBodyApplicationMonitors(TeaModel):
+    def __init__(self, accelerator_id=None, address=None, detect_threshold=None, listener_id=None,
+                 options_json=None, state=None, task_id=None, task_name=None):
+        self.accelerator_id = accelerator_id  # type: str
+        self.address = address  # type: str
+        self.detect_threshold = detect_threshold  # type: int
+        self.listener_id = listener_id  # type: str
+        self.options_json = options_json  # type: str
+        self.state = state  # type: str
+        self.task_id = task_id  # type: str
+        self.task_name = task_name  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorResponseBodyApplicationMonitors, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.state is not None:
+            result['State'] = self.state
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('State') is not None:
+            self.state = m.get('State')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class ListApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, application_monitors=None, page_number=None, page_size=None, request_id=None,
+                 total_count=None):
+        self.application_monitors = application_monitors  # type: list[ListApplicationMonitorResponseBodyApplicationMonitors]
+        self.page_number = page_number  # type: int
+        self.page_size = page_size  # type: int
+        self.request_id = request_id  # type: str
+        self.total_count = total_count  # type: int
+
+    def validate(self):
+        if self.application_monitors:
+            for k in self.application_monitors:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        result['ApplicationMonitors'] = []
+        if self.application_monitors is not None:
+            for k in self.application_monitors:
+                result['ApplicationMonitors'].append(k.to_map() if k else None)
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.total_count is not None:
+            result['TotalCount'] = self.total_count
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        self.application_monitors = []
+        if m.get('ApplicationMonitors') is not None:
+            for k in m.get('ApplicationMonitors'):
+                temp_model = ListApplicationMonitorResponseBodyApplicationMonitors()
+                self.application_monitors.append(temp_model.from_map(k))
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TotalCount') is not None:
+            self.total_count = m.get('TotalCount')
+        return self
+
+
+class ListApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: ListApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = ListApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
+class ListApplicationMonitorDetectResultRequest(TeaModel):
+    def __init__(self, begin_time=None, end_time=None, page_number=None, page_size=None, region_id=None,
+                 task_id=None):
+        self.begin_time = begin_time  # type: long
+        self.end_time = end_time  # type: long
+        self.page_number = page_number  # type: int
+        self.page_size = page_size  # type: int
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorDetectResultRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.begin_time is not None:
+            result['BeginTime'] = self.begin_time
+        if self.end_time is not None:
+            result['EndTime'] = self.end_time
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('BeginTime') is not None:
+            self.begin_time = m.get('BeginTime')
+        if m.get('EndTime') is not None:
+            self.end_time = m.get('EndTime')
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList(TeaModel):
+    def __init__(self, accelerator_id=None, detail=None, diag_status=None, listener_id=None, port=None,
+                 protocol=None, task_id=None):
+        self.accelerator_id = accelerator_id  # type: str
+        self.detail = detail  # type: str
+        self.diag_status = diag_status  # type: str
+        self.listener_id = listener_id  # type: str
+        self.port = port  # type: str
+        self.protocol = protocol  # type: str
+        self.task_id = task_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.detail is not None:
+            result['Detail'] = self.detail
+        if self.diag_status is not None:
+            result['DiagStatus'] = self.diag_status
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.port is not None:
+            result['Port'] = self.port
+        if self.protocol is not None:
+            result['Protocol'] = self.protocol
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Detail') is not None:
+            self.detail = m.get('Detail')
+        if m.get('DiagStatus') is not None:
+            self.diag_status = m.get('DiagStatus')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('Port') is not None:
+            self.port = m.get('Port')
+        if m.get('Protocol') is not None:
+            self.protocol = m.get('Protocol')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponseBody(TeaModel):
+    def __init__(self, application_monitor_detect_result_list=None, page_number=None, page_size=None,
+                 request_id=None, total_count=None):
+        self.application_monitor_detect_result_list = application_monitor_detect_result_list  # type: list[ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList]
+        self.page_number = page_number  # type: int
+        self.page_size = page_size  # type: int
+        self.request_id = request_id  # type: str
+        self.total_count = total_count  # type: int
+
+    def validate(self):
+        if self.application_monitor_detect_result_list:
+            for k in self.application_monitor_detect_result_list:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorDetectResultResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        result['ApplicationMonitorDetectResultList'] = []
+        if self.application_monitor_detect_result_list is not None:
+            for k in self.application_monitor_detect_result_list:
+                result['ApplicationMonitorDetectResultList'].append(k.to_map() if k else None)
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.total_count is not None:
+            result['TotalCount'] = self.total_count
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        self.application_monitor_detect_result_list = []
+        if m.get('ApplicationMonitorDetectResultList') is not None:
+            for k in m.get('ApplicationMonitorDetectResultList'):
+                temp_model = ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList()
+                self.application_monitor_detect_result_list.append(temp_model.from_map(k))
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TotalCount') is not None:
+            self.total_count = m.get('TotalCount')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: ListApplicationMonitorDetectResultResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(ListApplicationMonitorDetectResultResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = ListApplicationMonitorDetectResultResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class ListAvailableAccelerateAreasRequest(TeaModel):
     def __init__(self, accelerator_id=None, region_id=None):
         self.accelerator_id = accelerator_id  # type: str
         self.region_id = region_id  # type: str
 
     def validate(self):
         pass
@@ -11685,14 +12732,131 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = UpdateAclAttributeResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class UpdateApplicationMonitorRequest(TeaModel):
+    def __init__(self, address=None, client_token=None, detect_threshold=None, listener_id=None, options_json=None,
+                 region_id=None, task_id=None, task_name=None):
+        self.address = address  # type: str
+        self.client_token = client_token  # type: str
+        self.detect_threshold = detect_threshold  # type: int
+        self.listener_id = listener_id  # type: str
+        self.options_json = options_json  # type: str
+        self.region_id = region_id  # type: str
+        self.task_id = task_id  # type: str
+        self.task_name = task_name  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(UpdateApplicationMonitorRequest, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class UpdateApplicationMonitorResponseBody(TeaModel):
+    def __init__(self, request_id=None):
+        self.request_id = request_id  # type: str
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super(UpdateApplicationMonitorResponseBody, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class UpdateApplicationMonitorResponse(TeaModel):
+    def __init__(self, headers=None, body=None):
+        self.headers = headers  # type: dict[str, str]
+        self.body = body  # type: UpdateApplicationMonitorResponseBody
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super(UpdateApplicationMonitorResponse, self).to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m=None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = UpdateApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class UpdateBandwidthPackageRequest(TeaModel):
     def __init__(self, auto_pay=None, auto_use_coupon=None, bandwidth=None, bandwidth_package_id=None,
                  bandwidth_type=None, description=None, name=None, region_id=None):
         self.auto_pay = auto_pay  # type: bool
         self.auto_use_coupon = auto_use_coupon  # type: bool
         self.bandwidth = bandwidth  # type: int
         self.bandwidth_package_id = bandwidth_package_id  # type: str
```

### Comparing `alibabacloud_ga20191120_py2-1.0.8/LICENSE` & `alibabacloud_ga20191120_py2-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120_py2-1.0.8/README.md` & `alibabacloud_ga20191120_py2-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120_py2-1.0.8/PKG-INFO` & `alibabacloud_ga20191120_py2-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: alibabacloud_ga20191120_py2
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud Global Acceleration (20191120) SDK Library for Python2
 Home-page: https://github.com/aliyun/alibabacloud-python2-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_ga20191120_py2-1.0.8/README-CN.md` & `alibabacloud_ga20191120_py2-1.0.9/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120_py2-1.0.8/setup.py` & `alibabacloud_ga20191120_py2-1.0.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,29 +21,29 @@
 import os
 import sys
 from setuptools import setup, find_packages
 
 """
 setup module for alibabacloud_ga20191120_py2.
 
-Created on 20/12/2021
+Created on 06/01/2022
 
 @author: Alibaba Cloud SDK
 """
 
 PACKAGE = "alibabacloud_ga20191120"
 NAME = "alibabacloud_ga20191120_py2" or "alibabacloud-package"
 DESCRIPTION = "Alibaba Cloud Global Acceleration (20191120) SDK Library for Python2"
 AUTHOR = "Alibaba Cloud SDK"
 AUTHOR_EMAIL = "sdk-team@alibabacloud.com"
 URL = "https://github.com/aliyun/alibabacloud-python2-sdk"
 VERSION = __import__(PACKAGE).__version__
 REQUIRES = [
     "alibabacloud_tea_util_py2>=0.0.5, <1.0.0",
-    "alibabacloud_tea_openapi_py2>=0.1.0, <1.0.0",
+    "alibabacloud_tea_openapi_py2>=0.1.1, <1.0.0",
     "alibabacloud_openapi_util_py2>=0.0.8, <1.0.0",
     "alibabacloud_endpoint_util_py2>=0.0.2, <1.0.0"
 ]
 
 LONG_DESCRIPTION = ''
 
 if os.path.exists('./README.md'):
```

### Comparing `alibabacloud_ga20191120_py2-1.0.8/alibabacloud_ga20191120_py2.egg-info/PKG-INFO` & `alibabacloud_ga20191120_py2-1.0.9/alibabacloud_ga20191120_py2.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: alibabacloud-ga20191120-py2
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud Global Acceleration (20191120) SDK Library for Python2
 Home-page: https://github.com/aliyun/alibabacloud-python2-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

