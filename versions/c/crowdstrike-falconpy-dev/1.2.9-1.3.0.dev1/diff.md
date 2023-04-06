# Comparing `tmp/crowdstrike-falconpy-dev-1.2.9.tar.gz` & `tmp/crowdstrike-falconpy-dev-1.3.0.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "crowdstrike-falconpy-dev-1.2.9.tar", last modified: Tue Jan  3 18:46:31 2023, max compression
+gzip compressed data, was "crowdstrike-falconpy-dev-1.3.0.dev1.tar", last modified: Tue Feb  7 05:49:30 2023, max compression
```

## Comparing `crowdstrike-falconpy-dev-1.2.9.tar` & `crowdstrike-falconpy-dev-1.3.0.dev1.tar`

### file list

```diff
@@ -1,173 +1,215 @@
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.266827 crowdstrike-falconpy-dev-1.2.9/
--rw-r--r--   0 jhiller    (501) staff       (20)     4805 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/AUTHORS.md
--rw-r--r--   0 jhiller    (501) staff       (20)     1211 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/LICENSE
--rw-r--r--   0 jhiller    (501) staff       (20)    33367 2023-01-03 18:46:31.266517 crowdstrike-falconpy-dev-1.2.9/PKG-INFO
--rw-r--r--   0 jhiller    (501) staff       (20)    30050 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/README.md
--rw-r--r--   0 jhiller    (501) staff       (20)     7201 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/dev_setup.py
--rw-r--r--   0 jhiller    (501) staff       (20)       38 2023-01-03 18:46:31.266981 crowdstrike-falconpy-dev-1.2.9/setup.cfg
--rw-r--r--   0 jhiller    (501) staff       (20)     4482 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/setup.py
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.120151 crowdstrike-falconpy-dev-1.2.9/src/
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.145366 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/
--rw-r--r--   0 jhiller    (501) staff       (20)    33367 2023-01-03 18:46:31.000000 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/PKG-INFO
--rw-r--r--   0 jhiller    (501) staff       (20)     6580 2023-01-03 18:46:31.000000 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/SOURCES.txt
--rw-r--r--   0 jhiller    (501) staff       (20)        1 2023-01-03 18:46:31.000000 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/dependency_links.txt
--rw-r--r--   0 jhiller    (501) staff       (20)       83 2023-01-03 18:46:31.000000 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/requires.txt
--rw-r--r--   0 jhiller    (501) staff       (20)       12 2023-01-03 18:46:31.000000 crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/top_level.txt
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.207685 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/
--rw-r--r--   0 jhiller    (501) staff       (20)     9947 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/__init__.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2124 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_base_url.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2063 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_container_base_url.py
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.248993 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/
--rw-r--r--   0 jhiller    (501) staff       (20)     8697 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/__init__.py
--rw-r--r--   0 jhiller    (501) staff       (20)     7042 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_alerts.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6876 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_cloud_connect_aws.py
--rw-r--r--   0 jhiller    (501) staff       (20)    24875 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_cspm_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13488 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_custom_ioa.py
--rw-r--r--   0 jhiller    (501) staff       (20)    11664 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_d4c_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6446 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_detects.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10079 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_device_control_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8177 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_discover.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3167 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_event_streams.py
--rw-r--r--   0 jhiller    (501) staff       (20)    12391 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falcon_complete_dashboard.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3662 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falcon_container.py
--rw-r--r--   0 jhiller    (501) staff       (20)    12780 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falconx_sandbox.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3694 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_filevantage.py
--rw-r--r--   0 jhiller    (501) staff       (20)    23292 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_firewall_management.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10008 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_firewall_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9015 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_host_group.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10176 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_hosts.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2273 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_identity_protection.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6722 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_incidents.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6237 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_installation_tokens.py
--rw-r--r--   0 jhiller    (501) staff       (20)    20988 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_intel.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4594 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ioa_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)    11562 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ioc.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13556 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_iocs.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10743 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_kubernetes_protection.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5803 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_malquery.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6806 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_message_center.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4457 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ml_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2377 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_mobile_enrollment.py
--rw-r--r--   0 jhiller    (501) staff       (20)    17802 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_mssp.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3435 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_oauth2.py
--rw-r--r--   0 jhiller    (501) staff       (20)    12911 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ods.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3569 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_overwatch_dashboard.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9960 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_prevention_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4808 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_quarantine.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4165 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_quick_scan.py
--rw-r--r--   0 jhiller    (501) staff       (20)    24729 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_real_time_response.py
--rw-r--r--   0 jhiller    (501) staff       (20)    16057 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_real_time_response_admin.py
--rw-r--r--   0 jhiller    (501) staff       (20)    17745 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_recon.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4094 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_report_executions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9918 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_response_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)    11813 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sample_uploads.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3816 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_scheduled_reports.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5275 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_download.py
--rw-r--r--   0 jhiller    (501) staff       (20)    15516 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_update_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4678 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_visibility_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4667 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_spotlight_evaluation_logic.py
--rw-r--r--   0 jhiller    (501) staff       (20)     7134 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_spotlight_vulnerabilities.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4885 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_tailored_intelligence.py
--rw-r--r--   0 jhiller    (501) staff       (20)    15659 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_user_management.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2516 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_zero_trust_assessment.py
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.255662 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/
--rw-r--r--   0 jhiller    (501) staff       (20)     4289 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/__init__.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13207 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_custom_ioa.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8177 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_discover.py
--rw-r--r--   0 jhiller    (501) staff       (20)    17702 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_firewall_management.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3316 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_hosts.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2273 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_identity_protection.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5947 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_installation_tokens.py
--rw-r--r--   0 jhiller    (501) staff       (20)    11312 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_ioc.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2177 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_iocs.py
--rw-r--r--   0 jhiller    (501) staff       (20)    12911 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_ods.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13678 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_real_time_response.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13342 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_real_time_response_admin.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4094 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_report_executions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3816 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_scheduled_reports.py
-drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-01-03 18:46:31.265934 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/
--rw-r--r--   0 jhiller    (501) staff       (20)     5368 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/__init__.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2691 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_alerts.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3503 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_cloud_connect_aws.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2574 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_container.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4593 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_cspm_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3303 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_d4c_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2621 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_detects.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3776 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_device_control_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3666 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_falconx.py
--rw-r--r--   0 jhiller    (501) staff       (20)    16024 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_firewall.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8462 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_generic.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4140 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_host_group.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4511 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_incidents.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5480 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ioa.py
--rw-r--r--   0 jhiller    (501) staff       (20)     7302 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ioc.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5565 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_malquery.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3737 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_message_center.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2866 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_mssp.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4340 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ods.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3118 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_prevention_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4309 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_real_time_response.py
--rw-r--r--   0 jhiller    (501) staff       (20)     7745 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_recon.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2528 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_reports.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3112 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_response_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2433 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_sample_uploads.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3408 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_sensor_update_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)     3032 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_result.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8997 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_service_class.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2218 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_token_fail_reason.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2152 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_uber_default_preference.py
--rw-r--r--   0 jhiller    (501) staff       (20)    22936 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_util.py
--rw-r--r--   0 jhiller    (501) staff       (20)     2115 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_version.py
--rw-r--r--   0 jhiller    (501) staff       (20)    16200 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/alerts.py
--rw-r--r--   0 jhiller    (501) staff       (20)    18028 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/api_complete.py
--rw-r--r--   0 jhiller    (501) staff       (20)    15709 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/cloud_connect_aws.py
--rw-r--r--   0 jhiller    (501) staff       (20)    39156 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/cspm_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)    33740 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/custom_ioa.py
--rw-r--r--   0 jhiller    (501) staff       (20)    22512 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/d4c_registration.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8090 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/debug.py
--rw-r--r--   0 jhiller    (501) staff       (20)    14670 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/detects.py
--rw-r--r--   0 jhiller    (501) staff       (20)    23575 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/device_control_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)    14382 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/discover.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5896 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/event_streams.py
--rw-r--r--   0 jhiller    (501) staff       (20)    34729 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falcon_complete_dashboard.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8524 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falcon_container.py
--rw-r--r--   0 jhiller    (501) staff       (20)    23759 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falconx_sandbox.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5307 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/filevantage.py
--rw-r--r--   0 jhiller    (501) staff       (20)    76935 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/firewall_management.py
--rw-r--r--   0 jhiller    (501) staff       (20)    19971 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/firewall_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)    18631 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/host_group.py
--rw-r--r--   0 jhiller    (501) staff       (20)    27079 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/hosts.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4332 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/identity_protection.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13139 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/incidents.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13423 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/installation_tokens.py
--rw-r--r--   0 jhiller    (501) staff       (20)    30717 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/intel.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10491 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ioa_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)    34282 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ioc.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13794 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/iocs.py
--rw-r--r--   0 jhiller    (501) staff       (20)    19105 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/kubernetes_protection.py
--rw-r--r--   0 jhiller    (501) staff       (20)    16167 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/malquery.py
--rw-r--r--   0 jhiller    (501) staff       (20)    20985 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/message_center.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9946 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ml_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     5112 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/mobile_enrollment.py
--rw-r--r--   0 jhiller    (501) staff       (20)    42732 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/mssp.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9018 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/oauth2.py
--rw-r--r--   0 jhiller    (501) staff       (20)    30144 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ods.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13021 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/overwatch_dashboard.py
--rw-r--r--   0 jhiller    (501) staff       (20)    20457 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/prevention_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)    13564 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/quarantine.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9370 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/quick_scan.py
--rw-r--r--   0 jhiller    (501) staff       (20)    42242 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/real_time_response.py
--rw-r--r--   0 jhiller    (501) staff       (20)    24897 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/real_time_response_admin.py
--rw-r--r--   0 jhiller    (501) staff       (20)    42718 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/recon.py
--rw-r--r--   0 jhiller    (501) staff       (20)     7564 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/report_executions.py
--rw-r--r--   0 jhiller    (501) staff       (20)    19630 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/response_policies.py
--rw-r--r--   0 jhiller    (501) staff       (20)    21814 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sample_uploads.py
--rw-r--r--   0 jhiller    (501) staff       (20)     6664 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/scheduled_reports.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10069 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_download.py
--rw-r--r--   0 jhiller    (501) staff       (20)    34534 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_update_policy.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9753 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_visibility_exclusions.py
--rw-r--r--   0 jhiller    (501) staff       (20)     8233 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/spotlight_evaluation_logic.py
--rw-r--r--   0 jhiller    (501) staff       (20)    10505 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/spotlight_vulnerabilities.py
--rw-r--r--   0 jhiller    (501) staff       (20)     9645 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/tailored_intelligence.py
--rw-r--r--   0 jhiller    (501) staff       (20)    38033 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/user_management.py
--rw-r--r--   0 jhiller    (501) staff       (20)     4712 2023-01-03 18:46:30.000000 crowdstrike-falconpy-dev-1.2.9/src/falconpydev/zero_trust_assessment.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.261430 crowdstrike-falconpy-dev-1.3.0.dev1/
+-rw-r--r--   0 jhiller    (501) staff       (20)     4830 2023-02-07 05:49:28.000000 crowdstrike-falconpy-dev-1.3.0.dev1/AUTHORS.md
+-rw-r--r--   0 jhiller    (501) staff       (20)     1211 2023-02-07 05:49:28.000000 crowdstrike-falconpy-dev-1.3.0.dev1/LICENSE
+-rw-r--r--   0 jhiller    (501) staff       (20)    33335 2023-02-07 05:49:30.261139 crowdstrike-falconpy-dev-1.3.0.dev1/PKG-INFO
+-rw-r--r--   0 jhiller    (501) staff       (20)    30050 2023-02-07 05:49:28.000000 crowdstrike-falconpy-dev-1.3.0.dev1/README.md
+-rw-r--r--   0 jhiller    (501) staff       (20)     7201 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/dev_setup.py
+-rw-r--r--   0 jhiller    (501) staff       (20)       38 2023-02-07 05:49:30.261506 crowdstrike-falconpy-dev-1.3.0.dev1/setup.cfg
+-rw-r--r--   0 jhiller    (501) staff       (20)     4482 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/setup.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.159634 crowdstrike-falconpy-dev-1.3.0.dev1/src/
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.178715 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/
+-rw-r--r--   0 jhiller    (501) staff       (20)    33335 2023-02-07 05:49:30.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/PKG-INFO
+-rw-r--r--   0 jhiller    (501) staff       (20)     8001 2023-02-07 05:49:30.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/SOURCES.txt
+-rw-r--r--   0 jhiller    (501) staff       (20)        1 2023-02-07 05:49:30.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/dependency_links.txt
+-rw-r--r--   0 jhiller    (501) staff       (20)       83 2023-02-07 05:49:30.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/requires.txt
+-rw-r--r--   0 jhiller    (501) staff       (20)       12 2023-02-07 05:49:30.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/top_level.txt
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.209379 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/
+-rw-r--r--   0 jhiller    (501) staff       (20)    11969 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/__init__.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.211510 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/
+-rw-r--r--   0 jhiller    (501) staff       (20)     2095 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11250 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5561 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request_behavior.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5022 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request_connection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3788 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request_meta.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5358 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request_payloads.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3827 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_api_request/_request_validator.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.214269 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/
+-rw-r--r--   0 jhiller    (501) staff       (20)     2047 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4234 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_base_falcon_auth.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5998 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_bearer_token.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    19770 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_falcon_interface.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4806 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_interface_config.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     8624 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_uber_interface.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.214778 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_constant/
+-rw-r--r--   0 jhiller    (501) staff       (20)     2856 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_constant/__init__.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.233242 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/
+-rw-r--r--   0 jhiller    (501) staff       (20)     8737 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     7042 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_alerts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6876 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_cloud_connect_aws.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    24875 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_cspm_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13488 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_custom_ioa.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11664 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_d4c_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6446 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_detects.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10608 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_device_control_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10099 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_discover.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3167 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_event_streams.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    12391 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falcon_complete_dashboard.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3662 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falcon_container.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    12780 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falconx_sandbox.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3694 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_filevantage.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    23292 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_firewall_management.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10008 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_firewall_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9015 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_host_group.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10176 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_hosts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2273 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_identity_protection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6722 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_incidents.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6237 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_installation_tokens.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    22179 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_intel.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4594 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ioa_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11562 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ioc.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13556 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_iocs.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10743 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_kubernetes_protection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5803 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_malquery.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6806 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_message_center.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4457 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ml_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2377 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_mobile_enrollment.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    17802 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_mssp.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3435 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_oauth2.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    12680 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ods.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3569 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_overwatch_dashboard.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9960 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_prevention_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4808 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_quarantine.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4165 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_quick_scan.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    24729 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_real_time_response.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    16057 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_real_time_response_admin.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    17745 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_recon.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4094 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_report_executions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9918 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_response_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11813 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sample_uploads.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3816 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_scheduled_reports.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5275 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_download.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    15516 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_update_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4678 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_visibility_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4667 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_spotlight_evaluation_logic.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     7134 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_spotlight_vulnerabilities.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4885 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_tailored_intelligence.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    15659 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_user_management.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2516 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_zero_trust_assessment.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.237502 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/
+-rw-r--r--   0 jhiller    (501) staff       (20)     4289 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13207 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_custom_ioa.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10099 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_discover.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    17702 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_firewall_management.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3316 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_hosts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2273 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_identity_protection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5947 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_installation_tokens.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11312 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_ioc.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2177 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_iocs.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    12911 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_ods.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13678 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_real_time_response.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13342 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_real_time_response_admin.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4094 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_report_executions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3816 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_scheduled_reports.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.238601 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/
+-rw-r--r--   0 jhiller    (501) staff       (20)     1871 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2124 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_base_url.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2063 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_container_base_url.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2218 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_token_fail_reason.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.239388 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_error/
+-rw-r--r--   0 jhiller    (501) staff       (20)     2561 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_error/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5684 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_error/_exceptions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3573 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_error/_warnings.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.239920 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_log/
+-rw-r--r--   0 jhiller    (501) staff       (20)     1744 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_log/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3809 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_log/_facility.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.256021 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/
+-rw-r--r--   0 jhiller    (501) staff       (20)     5400 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2691 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_alerts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3624 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_cloud_connect_aws.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2574 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_container.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4858 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_cspm_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3563 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_d4c_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2621 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_detects.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5478 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_device_control_policy.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3666 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_falconx.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    16024 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_firewall.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     8462 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_generic.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4290 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_host_group.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4511 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_incidents.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5480 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ioa.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     7302 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ioc.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5577 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_malquery.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3737 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_message_center.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2866 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_mssp.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4426 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ods.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3118 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_prevention_policy.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4309 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_real_time_response.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     7727 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_recon.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2615 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_reports.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3112 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_response_policy.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2433 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_sample_uploads.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3408 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_sensor_update_policy.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.258812 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/
+-rw-r--r--   0 jhiller    (501) staff       (20)     4540 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/__base_resource.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2186 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4581 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_base_dictionary.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     1825 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_errors.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2684 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_expanded_result.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3112 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_headers.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     3298 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_meta.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2489 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_resources.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4340 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_response_component.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    15675 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_result.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.259621 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_service_class/
+-rw-r--r--   0 jhiller    (501) staff       (20)     1827 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_service_class/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    12272 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_service_class/_base_service_class.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    11024 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_service_class/_service_class.py
+drwxr-xr-x   0 jhiller    (501) staff       (20)        0 2023-02-07 05:49:30.260729 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/
+-rw-r--r--   0 jhiller    (501) staff       (20)     3087 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/__init__.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2997 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/_auth.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    33605 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/_functions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6161 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/_uber.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     2120 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_version.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    16709 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/alerts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9970 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/api_complete.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    15947 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/cloud_connect_aws.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    39693 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/cspm_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    34208 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/custom_ioa.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    22911 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/d4c_registration.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10750 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/debug.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    14793 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/detects.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    27402 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/device_control_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    17344 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/discover.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5973 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/event_streams.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    35245 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falcon_complete_dashboard.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     8670 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falcon_container.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    24004 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falconx_sandbox.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5384 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/filevantage.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    77667 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/firewall_management.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    20232 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/firewall_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    18869 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/host_group.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    27363 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/hosts.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4578 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/identity_protection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13308 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/incidents.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13613 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/installation_tokens.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    34693 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/intel.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10663 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ioa_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    34704 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ioc.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    14032 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/iocs.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    19435 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/kubernetes_protection.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    16359 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/malquery.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    21223 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/message_center.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10052 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ml_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     5166 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/mobile_enrollment.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    43246 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/mssp.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     8811 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/oauth2.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    30233 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ods.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13167 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/overwatch_dashboard.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    20718 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/prevention_policy.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    13733 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/quarantine.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9493 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/quick_scan.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    42802 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/real_time_response.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    25250 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/real_time_response_admin.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    43186 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/recon.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     7687 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/report_executions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    19891 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/response_policies.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    21891 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sample_uploads.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     6764 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/scheduled_reports.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10169 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_download.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    35068 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_update_policy.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9899 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_visibility_exclusions.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     8333 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/spotlight_evaluation_logic.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    10651 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/spotlight_vulnerabilities.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     9791 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/tailored_intelligence.py
+-rw-r--r--   0 jhiller    (501) staff       (20)    38570 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/user_management.py
+-rw-r--r--   0 jhiller    (501) staff       (20)     4789 2023-02-07 05:49:29.000000 crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/zero_trust_assessment.py
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/AUTHORS.md` & `crowdstrike-falconpy-dev-1.3.0.dev1/AUTHORS.md`

 * *Files 3% similar despite different names*

```diff
@@ -78,14 +78,15 @@
 + Arifur, `@arahman63`
 + `@areino`
 + `@kmccb`
 + Carlos Matos, `@carlosmmatos`
 + `@ffalor`
 + `@jmillerca`
 + `@davidt99`
++ `@CommonVulnerability`
 
 
 ## Sponsors
 Without the support of these executives, the FalconPy project would not have happened.
 
 | Name | Role |
 | :-- | :-- |
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/LICENSE` & `crowdstrike-falconpy-dev-1.3.0.dev1/LICENSE`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/PKG-INFO` & `crowdstrike-falconpy-dev-1.3.0.dev1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,20 @@
 Metadata-Version: 2.1
 Name: crowdstrike-falconpy-dev
-Version: 1.2.9
+Version: 1.3.0.dev1
 Summary: The CrowdStrike Falcon SDK for Python 3
 Home-page: https://github.com/CrowdStrike/falconpy
 Author: CrowdStrike
 Author-email: falconpy@crowdstrike.com
 Maintainer: Joshua Hiller
 Maintainer-email: falconpy@crowdstrike.com
-License: UNKNOWN
 Project-URL: Documentation, https://www.falconpy.io
 Project-URL: Source, https://github.com/CrowdStrike/falconpy/tree/dev/src/falconpy
 Project-URL: Tracker, https://github.com/CrowdStrike/falconpy/issues
 Keywords: crowdstrike,falcon,api,sdk,oauth2,devsecops,crowdstrike-falcon
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: Operating System :: Unix
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Operating System :: MacOS
@@ -323,9 +321,7 @@
 
 
 ---
 
 
 <p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="250px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-red-eyes.png"></P>
 <h3><P align="center">WE STOP BREACHES</P></h3>
-
-
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/README.md` & `crowdstrike-falconpy-dev-1.3.0.dev1/README.md`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/dev_setup.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/dev_setup.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/setup.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/setup.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/PKG-INFO` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,20 @@
 Metadata-Version: 2.1
 Name: crowdstrike-falconpy-dev
-Version: 1.2.9
+Version: 1.3.0.dev1
 Summary: The CrowdStrike Falcon SDK for Python 3
 Home-page: https://github.com/CrowdStrike/falconpy
 Author: CrowdStrike
 Author-email: falconpy@crowdstrike.com
 Maintainer: Joshua Hiller
 Maintainer-email: falconpy@crowdstrike.com
-License: UNKNOWN
 Project-URL: Documentation, https://www.falconpy.io
 Project-URL: Source, https://github.com/CrowdStrike/falconpy/tree/dev/src/falconpy
 Project-URL: Tracker, https://github.com/CrowdStrike/falconpy/issues
 Keywords: crowdstrike,falcon,api,sdk,oauth2,devsecops,crowdstrike-falcon
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: Operating System :: Unix
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Operating System :: MacOS
@@ -323,9 +321,7 @@
 
 
 ---
 
 
 <p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="250px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-red-eyes.png"></P>
 <h3><P align="center">WE STOP BREACHES</P></h3>
-
-
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/crowdstrike_falconpy_dev.egg-info/SOURCES.txt` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/crowdstrike_falconpy_dev.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -5,21 +5,14 @@
 setup.py
 src/crowdstrike_falconpy_dev.egg-info/PKG-INFO
 src/crowdstrike_falconpy_dev.egg-info/SOURCES.txt
 src/crowdstrike_falconpy_dev.egg-info/dependency_links.txt
 src/crowdstrike_falconpy_dev.egg-info/requires.txt
 src/crowdstrike_falconpy_dev.egg-info/top_level.txt
 src/falconpydev/__init__.py
-src/falconpydev/_base_url.py
-src/falconpydev/_container_base_url.py
-src/falconpydev/_result.py
-src/falconpydev/_service_class.py
-src/falconpydev/_token_fail_reason.py
-src/falconpydev/_uber_default_preference.py
-src/falconpydev/_util.py
 src/falconpydev/_version.py
 src/falconpydev/alerts.py
 src/falconpydev/api_complete.py
 src/falconpydev/cloud_connect_aws.py
 src/falconpydev/cspm_registration.py
 src/falconpydev/custom_ioa.py
 src/falconpydev/d4c_registration.py
@@ -66,14 +59,28 @@
 src/falconpydev/sensor_update_policy.py
 src/falconpydev/sensor_visibility_exclusions.py
 src/falconpydev/spotlight_evaluation_logic.py
 src/falconpydev/spotlight_vulnerabilities.py
 src/falconpydev/tailored_intelligence.py
 src/falconpydev/user_management.py
 src/falconpydev/zero_trust_assessment.py
+src/falconpydev/_api_request/__init__.py
+src/falconpydev/_api_request/_request.py
+src/falconpydev/_api_request/_request_behavior.py
+src/falconpydev/_api_request/_request_connection.py
+src/falconpydev/_api_request/_request_meta.py
+src/falconpydev/_api_request/_request_payloads.py
+src/falconpydev/_api_request/_request_validator.py
+src/falconpydev/_auth_object/__init__.py
+src/falconpydev/_auth_object/_base_falcon_auth.py
+src/falconpydev/_auth_object/_bearer_token.py
+src/falconpydev/_auth_object/_falcon_interface.py
+src/falconpydev/_auth_object/_interface_config.py
+src/falconpydev/_auth_object/_uber_interface.py
+src/falconpydev/_constant/__init__.py
 src/falconpydev/_endpoint/__init__.py
 src/falconpydev/_endpoint/_alerts.py
 src/falconpydev/_endpoint/_cloud_connect_aws.py
 src/falconpydev/_endpoint/_cspm_registration.py
 src/falconpydev/_endpoint/_custom_ioa.py
 src/falconpydev/_endpoint/_d4c_registration.py
 src/falconpydev/_endpoint/_detects.py
@@ -132,14 +139,23 @@
 src/falconpydev/_endpoint/deprecated/_ioc.py
 src/falconpydev/_endpoint/deprecated/_iocs.py
 src/falconpydev/_endpoint/deprecated/_ods.py
 src/falconpydev/_endpoint/deprecated/_real_time_response.py
 src/falconpydev/_endpoint/deprecated/_real_time_response_admin.py
 src/falconpydev/_endpoint/deprecated/_report_executions.py
 src/falconpydev/_endpoint/deprecated/_scheduled_reports.py
+src/falconpydev/_enum/__init__.py
+src/falconpydev/_enum/_base_url.py
+src/falconpydev/_enum/_container_base_url.py
+src/falconpydev/_enum/_token_fail_reason.py
+src/falconpydev/_error/__init__.py
+src/falconpydev/_error/_exceptions.py
+src/falconpydev/_error/_warnings.py
+src/falconpydev/_log/__init__.py
+src/falconpydev/_log/_facility.py
 src/falconpydev/_payload/__init__.py
 src/falconpydev/_payload/_alerts.py
 src/falconpydev/_payload/_cloud_connect_aws.py
 src/falconpydev/_payload/_container.py
 src/falconpydev/_payload/_cspm_registration.py
 src/falconpydev/_payload/_d4c_registration.py
 src/falconpydev/_payload/_detects.py
@@ -157,8 +173,25 @@
 src/falconpydev/_payload/_ods.py
 src/falconpydev/_payload/_prevention_policy.py
 src/falconpydev/_payload/_real_time_response.py
 src/falconpydev/_payload/_recon.py
 src/falconpydev/_payload/_reports.py
 src/falconpydev/_payload/_response_policy.py
 src/falconpydev/_payload/_sample_uploads.py
-src/falconpydev/_payload/_sensor_update_policy.py
+src/falconpydev/_payload/_sensor_update_policy.py
+src/falconpydev/_result/__base_resource.py
+src/falconpydev/_result/__init__.py
+src/falconpydev/_result/_base_dictionary.py
+src/falconpydev/_result/_errors.py
+src/falconpydev/_result/_expanded_result.py
+src/falconpydev/_result/_headers.py
+src/falconpydev/_result/_meta.py
+src/falconpydev/_result/_resources.py
+src/falconpydev/_result/_response_component.py
+src/falconpydev/_result/_result.py
+src/falconpydev/_service_class/__init__.py
+src/falconpydev/_service_class/_base_service_class.py
+src/falconpydev/_service_class/_service_class.py
+src/falconpydev/_util/__init__.py
+src/falconpydev/_util/_auth.py
+src/falconpydev/_util/_functions.py
+src/falconpydev/_util/_uber.py
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/__init__.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/__init__.py`

 * *Files 22% similar despite different names*

```diff
@@ -18,18 +18,73 @@
                                                         |:  |                             |:  |   |_____|
                                                         |::.|     CrowdStrike Falcon      |::.|
                                                         `---' OAuth2 API SDK for Python 3 `---'
 """
 from ._version import _VERSION, _MAINTAINER, _AUTHOR, _AUTHOR_EMAIL
 from ._version import _CREDITS, _DESCRIPTION, _TITLE, _PROJECT_URL
 from ._version import _DOCS_URL, _KEYWORDS
-from ._service_class import ServiceClass
+from ._auth_object import (
+    BaseFalconAuth,
+    BearerToken,
+    FalconInterface,
+    UberInterface,
+    InterfaceConfiguration
+    )
+from ._service_class import BaseServiceClass, ServiceClass
 from ._util import confirm_base_region, confirm_base_url
-from ._base_url import BaseURL
-from ._container_base_url import ContainerBaseURL
+from ._constant import (
+    MAX_DEBUG_RECORDS,
+    ALLOWED_METHODS,
+    USER_AGENT,
+    MIN_TOKEN_RENEW_WINDOW,
+    MAX_TOKEN_RENEW_WINDOW,
+    GLOBAL_API_MAX_RETURN,
+    MOCK_OPERATIONS
+    )
+from ._enum import BaseURL, ContainerBaseURL, TokenFailReason
+from ._log import LogFacility
+from ._error import (
+    APIError,
+    SDKError,
+    SDKWarning,
+    NoContentWarning,
+    SSLDisabledWarning,
+    RegionSelectError,
+    InvalidCredentials,
+    InvalidMethod,
+    InvalidOperation,
+    TokenNotSpecified,
+    KeywordsOnly,
+    CannotRevokeToken,
+    FunctionalityNotImplemented,
+    InvalidBaseURL,
+    PayloadValidationError,
+    NoAuthenticationMechanism
+    )
+from ._result import (
+    Result,
+    ExpandedResult,
+    BaseDictionary,
+    BaseResource,
+    Resources,
+    ResponseComponent,
+    Meta,
+    Headers,
+    Errors,
+    RawBody,
+    BinaryFile
+    )
+from ._api_request import (
+    APIRequest,
+    RequestBehavior,
+    RequestConnection,
+    RequestMeta,
+    RequestPayloads,
+    RequestValidator
+    )
 from .alerts import Alerts
 from .api_complete import APIHarness
 from .cloud_connect_aws import CloudConnectAWS
 from .cspm_registration import CSPMRegistration
 from .custom_ioa import CustomIOA
 from .d4c_registration import D4CRegistration
 from .detects import Detects
@@ -87,26 +142,37 @@
 __description__ = _DESCRIPTION
 __title__ = _TITLE
 __project_url__ = _PROJECT_URL
 __docs_url__ = _DOCS_URL
 __keywords__ = _KEYWORDS
 __all__ = [
     "confirm_base_url", "confirm_base_region", "BaseURL", "ServiceClass", "Alerts",
+    "BaseServiceClass", "BaseFalconAuth", "FalconInterface", "UberInterface", "TokenFailReason",
     "APIHarness", "CloudConnectAWS", "CSPMRegistration", "CustomIOA", "D4CRegistration",
     "Detects", "DeviceControlPolicies", "Discover", "EventStreams", "CompleteDashboard",
     "FalconContainer", "FalconXSandbox", "FirewallManagement", "FirewallPolicies", "HostGroup",
     "Hosts", "IdentityProtection", "Incidents", "InstallationTokens", "Intel", "IOAExclusions",
     "IOC", "Iocs", "KubernetesProtection", "MalQuery", "MLExclusions", "FlightControl", "OAuth2",
     "OverwatchDashboard", "PreventionPolicy", "Quarantine", "QuickScan", "RealTimeResponseAdmin",
     "RealTimeResponse", "Recon", "ReportExecutions", "ResponsePolicies", "SampleUploads",
     "ScheduledReports", "SensorDownload", "SensorUpdatePolicy", "SensorVisibilityExclusions",
-    "SpotlightVulnerabilities", "SpotlightEvaluationLogic", "UserManagement", "ODS",
+    "SpotlightVulnerabilities", "SpotlightEvaluationLogic", "UserManagement", "MAX_DEBUG_RECORDS",
     "ZeroTrustAssessment", "PreventionPolicies", "SensorUpdatePolicies", "MessageCenter",
-    "FileVantage", "MobileEnrollment", "ContainerBaseURL", "TailoredIntelligence"
-]
+    "FileVantage", "MobileEnrollment", "ContainerBaseURL", "TailoredIntelligence", "ODS", "Result",
+    "APIError", "SDKError", "SDKWarning", "NoContentWarning", "SSLDisabledWarning",
+    "RegionSelectError", "InvalidCredentials", "InvalidMethod", "InvalidOperation",
+    "TokenNotSpecified", "KeywordsOnly", "ALLOWED_METHODS", "USER_AGENT", "APIRequest",
+    "ExpandedResult", "CannotRevokeToken", "Headers", "Meta", "Resources",
+    "ResponseComponent", "BaseDictionary", "Errors", "BaseResource", "RawBody", "BinaryFile",
+    "FunctionalityNotImplemented", "BearerToken", "LogFacility", "InvalidBaseURL",
+    "InterfaceConfiguration", "RequestBehavior", "RequestConnection", "RequestMeta",
+    "RequestPayloads", "RequestValidator", "PayloadValidationError", "MIN_TOKEN_RENEW_WINDOW",
+    "MAX_TOKEN_RENEW_WINDOW", "GLOBAL_API_MAX_RETURN", "MOCK_OPERATIONS",
+    "NoAuthenticationMechanism"
+    ]
 """
 This is free and unencumbered software released into the public domain.
 
 Anyone is free to copy, modify, publish, use, compile, sell, or
 distribute this software, either in source code form or as a compiled
 binary, for any purpose, commercial or non-commercial, and by any
 means.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_base_url.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_base_url.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_container_base_url.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_container_base_url.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/__init__.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,14 +15,15 @@
                                                         |   _   .---.-|  .----.-----.-----|   _   .--.--.
                                                         |.  1___|  _  |  |  __|  _  |     |.  1   |  |  |
                                                         |.  __) |___._|__|____|_____|__|__|.  ____|___  |
                                                         |:  |                             |:  |   |_____|
                                                         |::.|     CrowdStrike Falcon      |::.|
                                                         `---' OAuth2 API SDK for Python 3 `---'
 """
+from typing import List, Any
 from .deprecated import _custom_ioa_deprecated
 from .deprecated import _discover_deprecated
 from .deprecated import _firewall_management_deprecated
 from .deprecated import _hosts_deprecated
 from .deprecated import _identity_protection_deprecated
 from .deprecated import _installation_tokens_deprecated
 from .deprecated import _ioc_deprecated
@@ -81,15 +82,15 @@
 from ._sensor_visibility_exclusions import _sensor_visibility_exclusions_endpoints
 from ._spotlight_evaluation_logic import _spotlight_evaluation_logic_endpoints
 from ._spotlight_vulnerabilities import _spotlight_vulnerabilities_endpoints
 from ._tailored_intelligence import _tailored_intelligence_endpoints
 from ._user_management import _user_management_endpoints
 from ._zero_trust_assessment import _zero_trust_assessment_endpoints
 
-api_endpoints = []
+api_endpoints: List[Any] = []
 api_endpoints.extend(_alerts_endpoints)
 api_endpoints.extend(_cloud_connect_aws_endpoints)
 api_endpoints.extend(_cspm_registration_endpoints)
 api_endpoints.extend(_custom_ioa_endpoints)
 api_endpoints.extend(_d4c_registration_endpoints)
 api_endpoints.extend(_detects_endpoints)
 api_endpoints.extend(_device_control_policies_endpoints)
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_alerts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_alerts.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_cloud_connect_aws.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_cloud_connect_aws.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_cspm_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_cspm_registration.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_custom_ioa.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_custom_ioa.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_d4c_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_d4c_registration.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_detects.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_detects.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_device_control_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_device_control_policies.py`

 * *Files 4% similar despite different names*

```diff
@@ -132,14 +132,36 @@
         "description": "The property to sort by",
         "name": "sort",
         "in": "query"
       }
     ]
   ],
   [
+    "getDefaultDeviceControlPolicies",
+    "GET",
+    "/policy/entities/default-device-control/v1",
+    "Retrieve the configuration for a Default Device Control Policy",
+    "device_control_policies",
+    []
+  ],
+  [
+    "updateDefaultDeviceControlPolicies",
+    "PATCH",
+    "/policy/entities/default-device-control/v1",
+    "Update the configuration for a Default Device Control Policy",
+    "device_control_policies",
+    [
+      {
+        "name": "body",
+        "in": "body",
+        "required": True
+      }
+    ]
+  ],
+  [
     "performDeviceControlPoliciesAction",
     "POST",
     "/policy/entities/device-control-actions/v1",
     "Perform the specified action on the Device Control Policies specified in the request",
     "device_control_policies",
     [
       {
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_discover.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_discover.py`

 * *Files 15% similar despite different names*

```diff
@@ -54,14 +54,34 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
+    "get_applications",
+    "GET",
+    "/discover/entities/applications/v1",
+    "Get details on applications by providing one or more IDs.",
+    "discover",
+    [
+      {
+        "type": "array",
+        "items": {
+          "type": "string"
+        },
+        "collectionFormat": "multi",
+        "description": "The IDs of applications to retrieve. (Min: 1, Max: 100)",
+        "name": "ids",
+        "in": "query",
+        "required": True
+      }
+    ]
+  ],
+  [
     "get_hosts",
     "GET",
     "/discover/entities/hosts/v1",
     "Get details on assets by providing one or more IDs.",
     "discover",
     [
       {
@@ -114,14 +134,55 @@
         "name": "offset",
         "in": "query"
       },
       {
         "maximum": 100,
         "minimum": 1,
         "type": "integer",
+        "description": "The number of account IDs to return in this response (min: 1, max: 100, default: 100). "
+        "Use with the `offset` parameter to manage pagination of results.",
+        "name": "limit",
+        "in": "query"
+      },
+      {
+        "type": "string",
+        "description": "Sort accounts by their properties. A single sort field is allowed. "
+        "Common sort options include:\n\n<ul><li>username|asc</li><li>last_failed_login_timestamp|desc</li></ul>",
+        "name": "sort",
+        "in": "query"
+      },
+      {
+        "type": "string",
+        "description": "Filter accounts using an FQL query. Common filter options include:\n\n<ul>"
+        "<li>account_type:'Local'</li><li>admin_privileges:'Yes'</li><li>first_seen_timestamp:<'now-7d'</li>"
+        "<li>last_successful_login_type:'Terminal server'</li></ul>",
+        "name": "filter",
+        "in": "query"
+      }
+    ]
+  ],
+  [
+    "query_applications",
+    "GET",
+    "/discover/queries/applications/v1",
+    "Search for applications in your environment by providing an FQL filter and paging details. "
+    "returns a set of application IDs which match the filter criteria.",
+    "discover",
+    [
+      {
+        "minimum": 0,
+        "type": "integer",
+        "description": "The index of the starting resource.",
+        "name": "offset",
+        "in": "query"
+      },
+      {
+        "maximum": 100,
+        "minimum": 1,
+        "type": "integer",
         "description": "The number of account IDs to return in this response (min: 1, max: 100, default: 100). "
         "Use with the `offset` parameter to manage pagination of results.",
         "name": "limit",
         "in": "query"
       },
       {
         "type": "string",
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_event_streams.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_event_streams.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falcon_complete_dashboard.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falcon_complete_dashboard.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falcon_container.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falcon_container.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_falconx_sandbox.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_falconx_sandbox.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_filevantage.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_filevantage.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_firewall_management.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_firewall_management.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_firewall_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_firewall_policies.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_host_group.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_host_group.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_hosts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_hosts.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_identity_protection.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_identity_protection.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_incidents.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_incidents.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_installation_tokens.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_installation_tokens.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_intel.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_intel.py`

 * *Files 2% similar despite different names*

```diff
@@ -250,14 +250,51 @@
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
+    "GetMitreReport",
+    "GET",
+    "/intel/entities/mitre-reports/v1",
+    "Export Mitre ATT&CK information for a given actor.",
+    "intel",
+    [
+      {
+        "type": "string",
+        "description": "Actor ID(derived from the actor's name)",
+        "name": "actor_id",
+        "in": "query",
+        "required": True
+      },
+      {
+        "type": "string",
+        "description": "Supported report formats: CSV or JSON",
+        "name": "format",
+        "in": "query",
+        "required": True
+      }
+    ]
+  ],
+  [
+    "PostMitreAttacks",
+    "POST",
+    "/intel/entities/mitre/v1",
+    "Retrieves report and observable IDs associated with the given actor and attacks",
+    "intel",
+    [
+      {
+        "name": "body",
+        "in": "body",
+        "required": True
+      }
+    ]
+  ],
+  [
     "GetIntelReportPDF",
     "GET",
     "/intel/entities/report-files/v1",
     "Return a Report PDF attachment",
     "intel",
     [
       {
@@ -489,14 +526,30 @@
         "description": "If true, include related indicators in the response. Defaults to true.",
         "name": "include_relations",
         "in": "query"
       }
     ]
   ],
   [
+    "QueryMitreAttacks",
+    "GET",
+    "/intel/queries/mitre/v1",
+    "Gets MITRE tactics and techniques for the given actor",
+    "intel",
+    [
+      {
+        "type": "string",
+        "description": "The actor ID(derived from the actor's name) for which to retrieve a list of attacks.",
+        "name": "id",
+        "in": "query",
+        "required": True
+      }
+    ]
+  ],
+  [
     "QueryIntelReportIds",
     "GET",
     "/intel/queries/reports/v1",
     "Get report IDs that match provided FQL filters.",
     "intel",
     [
       {
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ioa_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ioa_exclusions.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ioc.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ioc.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_iocs.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_iocs.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_kubernetes_protection.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_kubernetes_protection.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_malquery.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_malquery.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_message_center.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_message_center.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ml_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ml_exclusions.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_mobile_enrollment.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_mobile_enrollment.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_mssp.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_mssp.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_oauth2.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_oauth2.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_ods.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_ods.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,43 +34,43 @@
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 
 _ods_endpoints = [
   [
-    "aggregate_scans",
+    "aggregate-scans",
     "POST",
     "/ods/aggregates/scans/v1",
     "Get aggregates on ODS scan data.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "aggregate_scheduled_scans",
+    "aggregate-scheduled-scans",
     "POST",
     "/ods/aggregates/scheduled-scans/v1",
     "Get aggregates on ODS scheduled-scan data.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get_malicious_files_by_ids",
+    "get-malicious-files-by-ids",
     "GET",
     "/ods/entities/malicious-files/v1",
     "Get malicious files by ids.",
     "ods",
     [
       {
         "type": "array",
@@ -82,29 +82,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "cancel_scans",
+    "cancel-scans",
     "POST",
     "/ods/entities/scan-control-actions/cancel/v1",
     "Cancel ODS scans for the given scan ids.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get_scan_host_metadata_by_ids",
+    "get-scan-host-metadata-by-ids",
     "GET",
     "/ods/entities/scan-hosts/v1",
     "Get scan hosts by ids.",
     "ods",
     [
       {
         "type": "array",
@@ -116,29 +116,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "scans_report",
+    "scans-report",
     "POST",
     "/ods/entities/scans-reports/v1",
     "Launch a scans report creation job",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get_scans_by_scan_ids",
+    "get-scans-by-scan-ids",
     "GET",
     "/ods/entities/scans/v1",
     "Get Scans by IDs.",
     "ods",
     [
       {
         "type": "array",
@@ -150,29 +150,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "create_scan",
+    "create-scan",
     "POST",
     "/ods/entities/scans/v1",
     "Create ODS scan and start or schedule scan for the given scan request.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get_scheduled_scans_by_scan_ids",
+    "get-scheduled-scans-by-scan-ids",
     "GET",
     "/ods/entities/scheduled-scans/v1",
     "Get ScheduledScans by IDs.",
     "ods",
     [
       {
         "type": "array",
@@ -184,29 +184,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "schedule_scan",
+    "schedule-scan",
     "POST",
     "/ods/entities/scheduled-scans/v1",
     "Create ODS scan and start or schedule scan for the given scan request.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "delete_scheduled_scans",
+    "delete-scheduled-scans",
     "DELETE",
     "/ods/entities/scheduled-scans/v1",
     "Delete ODS scheduled-scans for the given scheduled-scan ids.",
     "ods",
     [
       {
         "type": "array",
@@ -224,15 +224,15 @@
         "description": "A FQL compatible query string.",
         "name": "filter",
         "in": "query"
       }
     ]
   ],
   [
-    "query_malicious_files",
+    "query-malicious-files",
     "GET",
     "/ods/queries/malicious-files/v1",
     "Query malicious files.",
     "ods",
     [
       {
         "type": "string",
@@ -284,15 +284,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query_scan_host_metadata",
+    "query-scan-host-metadata",
     "GET",
     "/ods/queries/scan-hosts/v1",
     "Query scan hosts.",
     "ods",
     [
       {
         "type": "string",
@@ -352,15 +352,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query_scans",
+    "query-scans",
     "GET",
     "/ods/queries/scans/v1",
     "Query Scans.",
     "ods",
     [
       {
         "type": "string",
@@ -426,15 +426,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query_scheduled_scans",
+    "query-scheduled-scans",
     "GET",
     "/ods/queries/scheduled-scans/v1",
     "Query ScheduledScans.",
     "ods",
     [
       {
         "type": "string",
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_overwatch_dashboard.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_overwatch_dashboard.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_prevention_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_prevention_policies.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_quarantine.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_quarantine.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_quick_scan.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_quick_scan.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_real_time_response.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_real_time_response.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_real_time_response_admin.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_real_time_response_admin.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_recon.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_recon.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_report_executions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_report_executions.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_response_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_response_policies.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sample_uploads.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sample_uploads.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_scheduled_reports.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_scheduled_reports.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_download.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_download.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_update_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_update_policies.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_sensor_visibility_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_sensor_visibility_exclusions.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_spotlight_evaluation_logic.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_spotlight_evaluation_logic.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_spotlight_vulnerabilities.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_spotlight_vulnerabilities.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_tailored_intelligence.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_tailored_intelligence.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_user_management.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_user_management.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/_zero_trust_assessment.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_zero_trust_assessment.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/__init__.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/__init__.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_custom_ioa.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_custom_ioa.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_discover.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_discover.py`

 * *Files 17% similar despite different names*

```diff
@@ -54,14 +54,34 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
+    "get-applications",
+    "GET",
+    "/discover/entities/applications/v1",
+    "Get details on applications by providing one or more IDs.",
+    "discover",
+    [
+      {
+        "type": "array",
+        "items": {
+          "type": "string"
+        },
+        "collectionFormat": "multi",
+        "description": "The IDs of applications to retrieve. (Min: 1, Max: 100)",
+        "name": "ids",
+        "in": "query",
+        "required": True
+      }
+    ]
+  ],
+  [
     "get-hosts",
     "GET",
     "/discover/entities/hosts/v1",
     "Get details on assets by providing one or more IDs.",
     "discover",
     [
       {
@@ -104,17 +124,58 @@
     "Search for accounts in your environment by providing an FQL (Falcon Query Language) filter and paging details. "
     "Returns a set of account IDs which match the filter criteria.",
     "discover",
     [
       {
         "minimum": 0,
         "type": "integer",
-        "description": "An offset used with the `limit` parameter to manage pagination of results. "
-        "On your first request, don’t provide an `offset`. On subsequent requests, provide the `offset` "
-        "from the previous response to continue from that place in the results.",
+        "description": "An offset used with the `limit` parameter to manage pagination of results. On your first request, "
+        "don’t provide an `offset`. On subsequent requests, provide the `offset` from the previous response to continue "
+        "from that place in the results.",
+        "name": "offset",
+        "in": "query"
+      },
+      {
+        "maximum": 100,
+        "minimum": 1,
+        "type": "integer",
+        "description": "The number of account IDs to return in this response (min: 1, max: 100, default: 100). "
+        "Use with the `offset` parameter to manage pagination of results.",
+        "name": "limit",
+        "in": "query"
+      },
+      {
+        "type": "string",
+        "description": "Sort accounts by their properties. A single sort field is allowed. Common sort options include:"
+        "\n\n<ul><li>username|asc</li><li>last_failed_login_timestamp|desc</li></ul>",
+        "name": "sort",
+        "in": "query"
+      },
+      {
+        "type": "string",
+        "description": "Filter accounts using an FQL query. Common filter options include:\n\n<ul><li>"
+        "account_type:'Local'</li><li>admin_privileges:'Yes'</li><li>first_seen_timestamp:<'now-7d'</li>"
+        "<li>last_successful_login_type:'Terminal server'</li></ul>",
+        "name": "filter",
+        "in": "query"
+      }
+    ]
+  ],
+  [
+    "query-applications",
+    "GET",
+    "/discover/queries/applications/v1",
+    "Search for applications in your environment by providing an FQL filter and paging details. "
+    "returns a set of application IDs which match the filter criteria.",
+    "discover",
+    [
+      {
+        "minimum": 0,
+        "type": "integer",
+        "description": "The index of the starting resource.",
         "name": "offset",
         "in": "query"
       },
       {
         "maximum": 100,
         "minimum": 1,
         "type": "integer",
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_firewall_management.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_firewall_management.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_hosts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_hosts.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_identity_protection.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_identity_protection.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_installation_tokens.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_installation_tokens.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_ioc.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_ioc.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_iocs.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_iocs.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_ods.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/_ods.py`

 * *Files 3% similar despite different names*

```diff
@@ -34,43 +34,43 @@
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 
 _ods_endpoints = [
   [
-    "aggregate-scans",
+    "aggregate_scans",
     "POST",
     "/ods/aggregates/scans/v1",
     "Get aggregates on ODS scan data.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "aggregate-scheduled-scans",
+    "aggregate_scheduled_scans",
     "POST",
     "/ods/aggregates/scheduled-scans/v1",
     "Get aggregates on ODS scheduled-scan data.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get-malicious-files-by-ids",
+    "get_malicious_files_by_ids",
     "GET",
     "/ods/entities/malicious-files/v1",
     "Get malicious files by ids.",
     "ods",
     [
       {
         "type": "array",
@@ -82,29 +82,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "cancel-scans",
+    "cancel_scans",
     "POST",
     "/ods/entities/scan-control-actions/cancel/v1",
     "Cancel ODS scans for the given scan ids.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get-scan-host-metadata-by-ids",
+    "get_scan_host_metadata_by_ids",
     "GET",
     "/ods/entities/scan-hosts/v1",
     "Get scan hosts by ids.",
     "ods",
     [
       {
         "type": "array",
@@ -116,29 +116,15 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "scans-report",
-    "POST",
-    "/ods/entities/scans-reports/v1",
-    "Launch a scans report creation job",
-    "ods",
-    [
-      {
-        "name": "body",
-        "in": "body",
-        "required": True
-      }
-    ]
-  ],
-  [
-    "get-scans-by-scan-ids",
+    "get_scans_by_scan_ids",
     "GET",
     "/ods/entities/scans/v1",
     "Get Scans by IDs.",
     "ods",
     [
       {
         "type": "array",
@@ -150,29 +136,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "create-scan",
+    "create_scan",
     "POST",
     "/ods/entities/scans/v1",
     "Create ODS scan and start or schedule scan for the given scan request.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "get-scheduled-scans-by-scan-ids",
+    "get_scheduled_scans_by_scan_ids",
     "GET",
     "/ods/entities/scheduled-scans/v1",
     "Get ScheduledScans by IDs.",
     "ods",
     [
       {
         "type": "array",
@@ -184,29 +170,29 @@
         "name": "ids",
         "in": "query",
         "required": True
       }
     ]
   ],
   [
-    "schedule-scan",
+    "schedule_scan",
     "POST",
     "/ods/entities/scheduled-scans/v1",
     "Create ODS scan and start or schedule scan for the given scan request.",
     "ods",
     [
       {
         "name": "body",
         "in": "body",
         "required": True
       }
     ]
   ],
   [
-    "delete-scheduled-scans",
+    "delete_scheduled_scans",
     "DELETE",
     "/ods/entities/scheduled-scans/v1",
     "Delete ODS scheduled-scans for the given scheduled-scan ids.",
     "ods",
     [
       {
         "type": "array",
@@ -224,15 +210,15 @@
         "description": "A FQL compatible query string.",
         "name": "filter",
         "in": "query"
       }
     ]
   ],
   [
-    "query-malicious-files",
+    "query_malicious_files",
     "GET",
     "/ods/queries/malicious-files/v1",
     "Query malicious files.",
     "ods",
     [
       {
         "type": "string",
@@ -284,15 +270,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query-scan-host-metadata",
+    "query_scan_host_metadata",
     "GET",
     "/ods/queries/scan-hosts/v1",
     "Query scan hosts.",
     "ods",
     [
       {
         "type": "string",
@@ -352,15 +338,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query-scans",
+    "query_scans",
     "GET",
     "/ods/queries/scans/v1",
     "Query Scans.",
     "ods",
     [
       {
         "type": "string",
@@ -426,15 +412,15 @@
         "name": "sort",
         "in": "query",
         "allowEmptyValue": True
       }
     ]
   ],
   [
-    "query-scheduled-scans",
+    "query_scheduled_scans",
     "GET",
     "/ods/queries/scheduled-scans/v1",
     "Query ScheduledScans.",
     "ods",
     [
       {
         "type": "string",
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_real_time_response.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_real_time_response.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_real_time_response_admin.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_real_time_response_admin.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_report_executions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_report_executions.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_endpoint/deprecated/_scheduled_reports.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_endpoint/deprecated/_scheduled_reports.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/__init__.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,15 +45,15 @@
 from ._sensor_update_policy import sensor_policy_payload
 from ._response_policy import response_policy_payload
 from ._real_time_response import command_payload, data_payload
 from ._cloud_connect_aws import aws_registration_payload
 from ._ioc import indicator_payload, indicator_update_payload, indicator_report_payload
 from ._d4c_registration import azure_registration_payload, aws_d4c_registration_payload
 from ._cspm_registration import cspm_registration_payload, cspm_policy_payload, cspm_scan_payload
-from ._device_control_policy import device_policy_payload
+from ._device_control_policy import device_policy_payload, default_device_policy_config_payload
 from ._falconx import falconx_payload
 from ._mssp import mssp_payload
 from ._firewall import (
     firewall_policy_payload,
     firewall_container_payload,
     firewall_rule_group_validation_payload,
     firewall_rule_group_payload,
@@ -62,15 +62,15 @@
     network_locations_metadata_payload,
     network_locations_create_payload
     )
 from ._reports import reports_payload
 from ._message_center import activity_payload, case_payload
 from ._alerts import update_alerts_payload
 from ._sample_uploads import extraction_payload
-from ._ods import scheduled_scan_payload, scans_report_payload
+from ._ods import scheduled_scan_payload
 
 
 __all__ = [
     "generic_payload_list", "aggregate_payload", "recon_action_payload", "recon_rules_payload",
     "recon_action_update_payload", "recon_notifications_payload", "recon_rule_preview_payload",
     "malquery_exact_search_payload", "malquery_hunt_payload", "malquery_fuzzy_payload",
     "update_detects_payload", "exclusion_payload", "ioa_exclusion_payload",
@@ -81,10 +81,10 @@
     "cspm_policy_payload", "cspm_scan_payload", "device_policy_payload", "falconx_payload",
     "mssp_payload", "ioa_custom_payload", "firewall_policy_payload", "firewall_container_payload",
     "firewall_rule_group_payload", "firewall_rule_group_update_payload", "reports_payload",
     "activity_payload", "case_payload", "incident_action_parameters", "update_alerts_payload",
     "firewall_rule_group_validation_payload", "firewall_filepattern_payload",
     "aws_d4c_registration_payload", "image_payload", "indicator_report_payload",
     "extraction_payload", "simple_action_parameter", "network_locations_metadata_payload",
-    "network_locations_create_payload", "scheduled_scan_payload", "scans_report_payload",
-    "token_settings_payload", "recon_export_job_payload"
+    "network_locations_create_payload", "scheduled_scan_payload", "token_settings_payload",
+    "recon_export_job_payload", "default_device_policy_config_payload"
 ]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_alerts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_alerts.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_cloud_connect_aws.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_cloud_connect_aws.py`

 * *Files 7% similar despite different names*

```diff
@@ -31,17 +31,18 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, List, Union
 
 
-def aws_registration_payload(passed_keywords: dict) -> dict:
+def aws_registration_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int]]]]:
     """Create a properly formatted payload for RTR command.
 
     {
         "resources": [
             {
                 "cloudtrail_bucket_owner_id": "string",
                 "cloudtrail_bucket_region": "string",
@@ -51,15 +52,15 @@
                 "rate_limit_reqs": integer,
                 "rate_limit_time": integer,
                 "static_external_id": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, Union[str, int]]]] = {}
     returned_payload["resources"] = []
     item = {}
     if passed_keywords.get("cloudtrail_bucket_owner_id", None):
         item["cloudtrail_bucket_owner_id"] = passed_keywords.get("cloudtrail_bucket_owner_id", None)
     if passed_keywords.get("cloudtrail_bucket_region", None):
         item["cloudtrail_bucket_region"] = passed_keywords.get("cloudtrail_bucket_region", None)
     if passed_keywords.get("external_id", None):
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_container.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_container.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_cspm_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_cspm_registration.py`

 * *Files 11% similar despite different names*

```diff
@@ -31,45 +31,46 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, List, Union
 
 
-def cspm_registration_payload(passed_keywords: dict) -> dict:
+def cspm_registration_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
     """Create a properly formatted CSPM registration payload.
 
     {
         "resources": [
             {
                 "account_id": "string",
                 "cloudtrail_region": "string",
                 "organization_id": "string",
                 "tenant_id": "string",
                 "subscription_id": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, str]]] = {}
     returned_payload["resources"] = []
     item = {}
     keys = ["account_id", "cloudtrail_region", "organization_id", "tenant_id", "subscription_id"]
     for key in keys:
         if passed_keywords.get(key, None):
             item[key] = passed_keywords.get(key, None)
 
     returned_payload["resources"].append(item)
 
     return returned_payload
 
 
-def cspm_policy_payload(passed_keywords: dict) -> dict:
+def cspm_policy_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, bool, List[str]]]]]:
     """Create a properly formatted CSPM policy update payload.
 
     {
     "resources": [
         {
             "account_id": "string",
             "enabled": boolean,
@@ -79,15 +80,15 @@
             ],
             "severity": "string",
             "tag_excluded": boolean
         }
     ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, Union[str, bool, List[str]]]]] = {}
     returned_payload["resources"] = []
     item = {}
     if passed_keywords.get("account_id", None):
         item["account_id"] = passed_keywords.get("account_id", None)
     if passed_keywords.get("enabled", None) is not None:
         item["enabled"] = passed_keywords.get("enabled", None)
     if passed_keywords.get("policy_id", -1) > 0:
@@ -103,28 +104,28 @@
         item["regions"] = region_list
 
     returned_payload["resources"].append(item)
 
     return returned_payload
 
 
-def cspm_scan_payload(passed_keywords: dict) -> dict:
+def cspm_scan_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
     """Create a properly formmatted CSPM scan schedule payload.
 
     {
         "resources": [
             {
                 "cloud_platform": "string",
                 "next_scan_timestamp": "2021-10-25T05:22:27.365Z",
                 "scan_schedule": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, str]]] = {}
     returned_payload["resources"] = []
     item = {}
     for key in ["cloud_platform", "next_scan_timestamp", "scan_schedule"]:
         if passed_keywords.get(key, None):
             item[key] = passed_keywords.get(key, None)
 
     returned_payload["resources"].append(item)
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_d4c_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_d4c_registration.py`

 * *Files 12% similar despite different names*

```diff
@@ -31,61 +31,63 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, List, Union, Any
 
 
-def aws_d4c_registration_payload(passed_keywords: dict) -> dict:
+def aws_d4c_registration_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, bool]]]]:
     """Create a properly formatted AWS registration payload.
 
     {
         "resources": [
             {
                 "account_id": "string",
                 "account_type": "string",
                 "cloudtrail_region": "string",
                 "is_master": true,
                 "organization_id": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, Union[str, bool]]]] = {}
     returned_payload["resources"] = []
     keys = ["account_id", "account_type", "cloudtrail_region", "organization_id"]
-    item = {}
+    item: Dict[str, Any] = {}
     for key in keys:
-        if passed_keywords.get(key, None):
+        if isinstance(passed_keywords.get(key, None), str):
             item[key] = passed_keywords.get(key)
-    if passed_keywords.get("is_master", None) is not None:
+    if isinstance(passed_keywords.get("is_master", None), bool):
         item["is_master"] = passed_keywords.get("is_master")
 
-    returned_payload["resources"].append(item)
+    if item:
+        returned_payload["resources"].append(item)
 
     return returned_payload
 
 
-def azure_registration_payload(passed_keywords: dict) -> dict:
+def azure_registration_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
     """Create a properly formatted Azure registration payload.
 
     {
         "resources": [
             {
                 "subscription_id": "string",
                 "tenant_id": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, str]]] = {}
     returned_payload["resources"] = []
-    item = {}
+    item: Dict[str, str] = {}
     if passed_keywords.get("subscription_id", None):
         item["subscription_id"] = passed_keywords.get("subscription_id", None)
     if passed_keywords.get("tenant_id", None):
         item["tenant_id"] = passed_keywords.get("tenant_id", None)
     returned_payload["resources"].append(item)
 
     return returned_payload
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_detects.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_detects.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_device_control_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_falconx.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-"""Internal payload handling library - Device Control Policy Payloads.
+"""Internal payload handling library - Falcon X Sandbox.
 
  _______                        __ _______ __        __ __
 |   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
 |.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
 |.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
 |:  1   |                         |:  1   |
 |::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
@@ -33,65 +33,63 @@
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 
 
-def device_policy_payload(passed_keywords: dict) -> dict:
-    """Create a properly formatted prevention policy payload.
+def falconx_payload(passed_keywords: dict) -> dict:
+    """Create a properly formatting submit payload.
 
-    Supports create and update operations. Single policy only.
     {
-        "resources": [
+        "sandbox": [
             {
-                "clone_id": "string",
-                "description": "string",
-                "name": "string",
-                "platform_name": "Windows",
-                "settings": {
-                    "classes": [
-                    {
-                        "action": "FULL_ACCESS",
-                        "exceptions": [
-                        {
-                            "action": "string",
-                            "class": "string",
-                            "combined_id": "string",
-                            "id": "string",
-                            "match_method": "string",
-                            "product_id": "string",
-                            "product_id_decimal": "string",
-                            "product_name": "string",
-                            "serial_number": "string",
-                            "vendor_id": "string",
-                            "vendor_id_decimal": "string",
-                            "vendor_name": "string"
-                        }
-                        ],
-                        "id": "string"
-                    }
-                    ],
-                    "end_user_notification": "TRUE",
-                    "enforcement_mode": "string",
-                    "id": "string"
-                }
+                "action_script": "string",
+                "command_line": "string",
+                "document_password": "string",
+                "enable_tor": true,
+                "environment_id": 0,
+                "network_settings": "string",
+                "sha256": "string",
+                "submit_name": "string",
+                "system_date": "string",
+                "system_time": "string",
+                "url": "string"
             }
+        ],
+        "send_email_notification": true,
+        "user_tags": [
+            "string"
         ]
     }
     """
     returned_payload = {}
-    resources = []
-    item = {}
-    keys = ["clone_id", "description", "name", "platform_name"]
+    sandbox = []
+    sandbox_item = {}
+    keys = [
+        "action_script", "command_line", "document_password", "network_settings", "sha256",
+        "submit_name", "system_date", "system_time", "url"
+        ]
     for key in keys:
         if passed_keywords.get(key, None):
-            item[key] = passed_keywords.get(key, None)
-
-    # Settings classes not currently abstracted
-    if passed_keywords.get("settings", None):
-        item["settings"] = passed_keywords.get("settings", None)
+            sandbox_item[key] = passed_keywords.get(key, None)
+    if passed_keywords.get("enable_tor", None) is not None:
+        sandbox_item["enable_tor"] = passed_keywords.get("enable_tor", None)
+    if passed_keywords.get("environment_id", 0) > 0:
+        sandbox_item["environment_id"] = passed_keywords.get("environment_id", None)
+    if sandbox_item:
+        sandbox.append(sandbox_item)
+
+    if passed_keywords.get("send_email_notifications", None) is not None:
+        email_notify = passed_keywords.get("send_email_notifications", None)
+        returned_payload["send_email_notifications"] = email_notify
+
+    passed_tags = passed_keywords.get("user_tags", None)
+    if passed_tags:
+        if isinstance(passed_tags, str):
+            passed_tags = passed_tags.split(",")
+        returned_payload["user_tags"] = passed_tags
 
-    resources.append(item)
-    returned_payload["resources"] = resources
+    if sandbox:
+        returned_payload["sandbox"] = sandbox
 
     return returned_payload
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_falconx.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_real_time_response.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-"""Internal payload handling library - Falcon X Sandbox.
+"""Internal payload handling library - Real Time Response.
 
  _______                        __ _______ __        __ __
 |   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
 |.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
 |.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
 |:  1   |                         |:  1   |
 |::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
@@ -33,63 +33,88 @@
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 
 
-def falconx_payload(passed_keywords: dict) -> dict:
-    """Create a properly formatting submit payload.
+def command_payload(passed_keywords: dict) -> dict:  # pylint: disable=R0912  # noqa: C901
+    """Create a properly formatted payload for RTR command.
 
     {
-        "sandbox": [
-            {
-                "action_script": "string",
-                "command_line": "string",
-                "document_password": "string",
-                "enable_tor": true,
-                "environment_id": 0,
-                "network_settings": "string",
-                "sha256": "string",
-                "submit_name": "string",
-                "system_date": "string",
-                "system_time": "string",
-                "url": "string"
-            }
+        "base_command": "string",
+        "batch_id": "string",
+        "command_string": "string",
+        "optional_hosts": [
+            "string"
+        ],
+        "file_path": "string",
+        "persist_all": true,
+        "existing_batch_id": "string",
+        "host_ids": [
+            "string"
         ],
-        "send_email_notification": true,
-        "user_tags": [
+        "queue_offline": true,
+        "hosts_to_remove": [
             "string"
         ]
+        "device_id": "string",
+        "id": integer,
+        "persist": boolean,
+        "session_id": "string",
+        "origin": "string"
     }
     """
+    # flake8 / pylint both complain about complexity due to the number of if statements.
+    # Ignoring the complaint as this is just running through the potential passed keywords.
     returned_payload = {}
-    sandbox = []
-    sandbox_item = {}
+
     keys = [
-        "action_script", "command_line", "document_password", "network_settings", "sha256",
-        "submit_name", "system_date", "system_time", "url"
+        "base_command", "batch_id", "command_string", "file_path",
+        "existing_batch_id", "device_id", "session_id", "origin"
         ]
     for key in keys:
         if passed_keywords.get(key, None):
-            sandbox_item[key] = passed_keywords.get(key, None)
-    if passed_keywords.get("enable_tor", None) is not None:
-        sandbox_item["enable_tor"] = passed_keywords.get("enable_tor", None)
-    if passed_keywords.get("environment_id", 0) > 0:
-        sandbox_item["environment_id"] = passed_keywords.get("environment_id", None)
-    if sandbox_item:
-        sandbox.append(sandbox_item)
-
-    if passed_keywords.get("send_email_notifications", None) is not None:
-        email_notify = passed_keywords.get("send_email_notifications", None)
-        returned_payload["send_email_notifications"] = email_notify
-
-    passed_tags = passed_keywords.get("user_tags", None)
-    if passed_tags:
-        if isinstance(passed_tags, str):
-            passed_tags = passed_tags.split(",")
-        returned_payload["user_tags"] = passed_tags
+            returned_payload[key] = passed_keywords.get(key, None)
+
+    bool_keys = ["persist_all", "queue_offline", "persist"]
+    for boolean in bool_keys:
+        if passed_keywords.get(boolean, None) is not None:
+            returned_payload[boolean] = passed_keywords.get(boolean, None)
+
+    if passed_keywords.get("id", -1) > -1:
+        returned_payload["id"] = passed_keywords.get("id", None)
+
+    list_keys = ["optional_hosts", "host_ids", "hosts_to_remove"]
+    for list_key in list_keys:
+        passed_list = passed_keywords.get(list_key, None)
+        if passed_list:
+            if isinstance(passed_list, str):
+                passed_list = passed_list.split(",")
+            returned_payload[list_key] = passed_list
+
+    return returned_payload
+
+
+def data_payload(passed_keywords: dict) -> dict:
+    """Create a properly formatted formData payload for RTR file uploads.
 
-    if sandbox:
-        returned_payload["sandbox"] = sandbox
+    {
+        "id": "string",
+        "description": "string",
+        "name": "string",
+        "comments_for_audit_log": "string",
+        "content": "string",
+        "platform": "string",
+        "permission_type": "string"
+    }
+    """
+    returned_payload = {}
+    keys = [
+        "id", "description", "name", "comments_for_audit_log",
+        "content", "platform", "permission_type"
+        ]
+    for key in keys:
+        if passed_keywords.get(key, None):
+            returned_payload[key] = passed_keywords.get(key, None)
 
     return returned_payload
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_firewall.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_firewall.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_generic.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_generic.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_host_group.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_host_group.py`

 * *Files 11% similar despite different names*

```diff
@@ -31,33 +31,34 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, List
 
 
-def host_group_create_payload(passed_keywords: dict) -> dict:
+def host_group_create_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
     """Create a properly formatted payload for host group operations.
 
     Create operations are supported. `id` and `group_type`
     values should be added by the calling method after creating this payload.
     {
         "resources": [
             {
                 "assignment_rule": "string",
                 "description": "string",
-                "group_type": "static",
+                "group_type": "string",
                 "name": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, str]]] = {}
     returned_payload["resources"] = []
     host_group_item = {}
     if passed_keywords.get("assignment_rule", None):
         host_group_item["assignment_rule"] = passed_keywords.get("assignment_rule", None)
     if passed_keywords.get("description", None):
         host_group_item["description"] = passed_keywords.get("description", None)
     if passed_keywords.get("group_type", None):
@@ -66,15 +67,15 @@
         host_group_item["name"] = passed_keywords.get("name", None)
     if host_group_item:
         returned_payload["resources"].append(host_group_item)
 
     return returned_payload
 
 
-def host_group_update_payload(passed_keywords: dict) -> dict:
+def host_group_update_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
     """Create a properly formatted payload for host group operations.
 
     Update operations are supported. `id` and `group_type`
     values should be added by the calling method after creating this payload.
     {
         "resources": [
             {
@@ -82,15 +83,15 @@
                 "description": "string",
                 "id": "string",
                 "name": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: Dict[str, List[Dict[str, str]]] = {}
     returned_payload["resources"] = []
     host_group_item = {}
     if passed_keywords.get("assignment_rule", None):
         host_group_item["assignment_rule"] = passed_keywords.get("assignment_rule", None)
     if passed_keywords.get("description", None):
         host_group_item["description"] = passed_keywords.get("description", None)
     if passed_keywords.get("id", None):
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_incidents.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_incidents.py`

 * *Files 1% similar despite different names*

```diff
@@ -33,15 +33,15 @@
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 
 
-def incident_action_parameters(passed_keywords: dict) -> dict:
+def incident_action_parameters(passed_keywords: dict) -> list:
     """Create a properly formatted action_parameters branch for incident action payload operations.
 
     Available keywords
     add_tag - Adds the associated value as a new tag on all the incidents of the ids list.
               Multiple tags may be provided as a list or comma delimited string.
     delete_tag - Deletes tags matching the value from all the incidents in the ids list.
                  Multiple tags may be provided as a list or a comma delimited string.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ioa.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ioa.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ioc.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ioc.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_malquery.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_malquery.py`

 * *Files 1% similar despite different names*

```diff
@@ -51,15 +51,15 @@
             {
             "type": "string",
             "value": "string"
             }
         ]
     }
     """
-    returned_payload = {}
+    returned_payload: dict = {}
     filters = passed_keywords.get("filter_meta", None)
     limit = passed_keywords.get("limit", 0)
     if filters or limit:
         returned_payload["options"] = {}
     if filters:
         if isinstance(filters, str):
             filters = filters.split(",")
@@ -71,15 +71,15 @@
         returned_payload["patterns"] = patterns
 
     return returned_payload
 
 
 def handle_malquery_search_params(passed_params: dict) -> dict:
     """Create the base payload used by exact_search and hunt."""
-    returned_base = {}
+    returned_base: dict = {}
     filters = passed_params.get("filter_filetypes", None)
     filter_meta = passed_params.get("filter_meta", None)
     limit = passed_params.get("limit", 0)
     max_date = passed_params.get("max_date", None)
     max_size = passed_params.get("max_size", None)
     min_date = passed_params.get("min_date", None)
     min_size = passed_params.get("min_size", None)
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_message_center.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_message_center.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_mssp.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_mssp.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_ods.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_ods.py`

 * *Files 3% similar despite different names*

```diff
@@ -88,33 +88,34 @@
     for key in schedule_keys:
         if passed_keywords.get(key, None) is not None:
             returned_payload["schedule"][key] = passed_keywords.get(key)
 
     return returned_payload
 
 
-def scans_report_payload(passed_keywords: dict) -> dict:
-    """Craft a properly formatted scans report creation payload.
+# This operation is no longer supported
+# def scans_report_payload(passed_keywords: dict) -> dict:
+#     """Craft a properly formatted scans report creation payload.
+
+#     {
+#         "is_schedule": true,
+#         "report_format": "string",
+#         "search": {
+#             "filter": "string",
+#             "sort": "string"
+#         }
+#     }
+#     """
+#     returned_payload = {}
+#     keys = ["is_schedule", "report_format", "search"]
+#     for key in keys:
+#         if passed_keywords.get(key, None) is not None:
+#             returned_payload[key] = passed_keywords.get(key)
+
+#     if "search" not in returned_payload:
+#         returned_payload["search"] = {}
+#     search_keys = ["filter", "sort"]
+#     for key in search_keys:
+#         if passed_keywords.get(key, None):
+#             returned_payload["search"][key] = passed_keywords.get(key)
 
-    {
-        "is_schedule": true,
-        "report_format": "string",
-        "search": {
-            "filter": "string",
-            "sort": "string"
-        }
-    }
-    """
-    returned_payload = {}
-    keys = ["is_schedule", "report_format", "search"]
-    for key in keys:
-        if passed_keywords.get(key, None) is not None:
-            returned_payload[key] = passed_keywords.get(key)
-
-    if "search" not in returned_payload:
-        returned_payload["search"] = {}
-    search_keys = ["filter", "sort"]
-    for key in search_keys:
-        if passed_keywords.get(key, None):
-            returned_payload["search"][key] = passed_keywords.get(key)
-
-    return returned_payload
+#     return returned_payload
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_prevention_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_prevention_policy.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_recon.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_recon.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import List, Dict
 
 
 def handle_recon_rule_params(inbound: dict) -> dict:
     """Handle the payload formatting for a single rule object."""
     returned_dict = {}
     if inbound.get("filter", None):
         returned_dict["filter"] = inbound.get("filter", None)
@@ -52,28 +53,28 @@
         returned_dict["priority"] = inbound.get("priority", None)
     if inbound.get("topic", None):
         returned_dict["topic"] = inbound.get("topic", None)
 
     return returned_dict
 
 
-def recon_rules_payload(passed_keywords: dict) -> dict:
+def recon_rules_payload(passed_keywords: dict) -> List[Dict[str, str]]:
     """Create a properly formatted payload for recon rule handling.
 
     Creates a list of dictionaries.
-            [
-                {
-                    "filter": "string",
-                    "id": "string",
-                    "name": "string",
-                    "permissions": "string",
-                    "priority": "string",
-                    "topic": "string"
-                }
-            ]
+    [
+        {
+            "filter": "string",
+            "id": "string",
+            "name": "string",
+            "permissions": "string",
+            "priority": "string",
+            "topic": "string"
+        }
+    ]
     """
     returned_rules = []
     provided_rules = passed_keywords.get("rules", None)
     if provided_rules:
         # Not entirely sure why you wouldn't just pass the body
         if isinstance(provided_rules, list):
             for rule in passed_keywords.get("rules", None):
@@ -84,15 +85,15 @@
     else:
         # Only one rule was provided, use the keywords
         returned_rules.append(handle_recon_rule_params(passed_keywords))
 
     return returned_rules
 
 
-def recon_notifications_payload(passed_keywords: dict) -> dict:
+def recon_notifications_payload(passed_keywords: dict) -> List[Dict[str, str]]:
     """Recon notification payload handler.
 
     Creates a properly formatted payload for a recon notification
     payload. Generates a list of dictionaries, but is designed to handle
     just one notification. (For multiple notifications use the body
     payload keyword.)
     [
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_reports.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_reports.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,29 +31,30 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Union, List, Optional
 
 
-def reports_payload(passed_keywords: dict = None, passed_arguments: list = None) -> dict:
+def reports_payload(passed_keywords: dict, passed_arguments: Optional[tuple] = None) -> List[dict]:
     """Create a properly formatted payload for report execution / scheduling.
 
     [
         {
             "id": "string"
         }
     ]
     """
     returned_payload = []
-    submitted = ""
+    submitted: Union[str, list] = ""
     if passed_keywords.get("ids", None):
-        key = passed_keywords.get("ids", None)
+        key: Union[str, list] = passed_keywords.get("ids", None)
         if isinstance(key, list):
             submitted = key
         else:
             submitted = key.split(",")
     elif passed_arguments:
         key = passed_arguments[0]
         if isinstance(key, list):
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_response_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_response_policy.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_sample_uploads.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_sample_uploads.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_payload/_sensor_update_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_payload/_sensor_update_policy.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_result.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_result/_expanded_result.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-"""API Response formatting classes.
+"""API Response formatting class.
 
  _______                        __ _______ __        __ __
 |   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
 |.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
 |.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
 |:  1   |                         |:  1   |
 |::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
@@ -31,43 +31,35 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
-# pylint: disable=R0903  # Using a class so that the data structure is callable
-
-
-class Result:
-    """Callable subclass to handle parsing of result client output."""
-
-    def __init__(self: object) -> dict:
-        """Instantiate the subclass and initializes the result object."""
-        self.result_obj = {}
-
-    def __call__(self: object, status_code: int, headers, body: dict) -> dict:
-        """Format values into a properly formatted result object."""
-        self.result_obj['status_code'] = status_code
-        # force standard dictionary to prevent json issues
-        self.result_obj['headers'] = dict(headers)
-        self.result_obj['body'] = body
-
-        return self.result_obj
+# pylint: disable=R0903
+from typing import Tuple, Dict, Union
 
 
 class ExpandedResult:
-    """Callable subsclass to handle parsing of expanded result client output."""
-
-    def __init__(self: object) -> tuple:
-        """Instantiate the subclass and intialize the expanded result object."""
-        self.result_tuple = ()
+    """Callable subsclass to handle parsing of expanded result client output.
 
-    def __call__(self: object, status_code: int, headers, content) -> tuple:
+    DEPRECATED
+    ---
+    This class is deprecated and maintained for backwards compatibility purposes only.
+
+    Please move all code over to use Result.tupled.
+
+    Examples: tupled_response: Result = falcon.query_detects(pythonic=True).tupled
+              tupled_response: Result = Result(full=falcon.query_detects()).tupled
+    """
+
+    def __call__(self,
+                 status_code: int,
+                 headers: Dict[str, str],
+                 content: Union[str, bytes, Dict[str, Dict]]
+                 ) -> Tuple[str, Dict[str, str], Dict[str, Dict]]:
         """Format ingested values into a properly formatted expanded result object."""
         content_result = content
         if isinstance(content, dict):
             content_result = content["body"]
 
-        self.result_tuple = (status_code, dict(headers), content_result)
-
-        return self.result_tuple
+        return (status_code, dict(headers), content_result)
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_token_fail_reason.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_enum/_token_fail_reason.py`

 * *Files identical despite different names*

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_uber_default_preference.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_service_class/__init__.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-"""Internal constant library.
+"""FalconPy Service Class module.
 
  _______                        __ _______ __        __ __
 |   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
 |.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
 |.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
 |:  1   |                         |:  1   |
 |::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
@@ -31,19 +31,11 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
-PREFER_NONETYPE = [
-    "report_executions_download_get", "report_executions_download.get",
-    "RTR_ListFiles", "RTR_ListFilesV2", "RTR_GetExtractedFileContents",
-    "RTR_DeleteSession"
-]
-PREFER_IDS_IN_BODY = [
-    "GetDeviceDetails", "PostDeviceDetailsV2", "GetVulnerabilities", "GetIntelIndicatorEntities",
-    "getChildrenV2", "cancel-scans", "GetDetectSummaries"
-]
-MOCK_OPERATIONS = [
-    "GetImageAssessmentReport", "DeleteImageDetails", "ImageMatchesPolicy"
-]
+from ._base_service_class import BaseServiceClass
+from ._service_class import ServiceClass
+
+__all__ = ["BaseServiceClass", "ServiceClass"]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_util.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_util/_functions.py`

 * *Files 22% similar despite different names*

```diff
@@ -33,104 +33,130 @@
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import base64
 import functools
+from warnings import warn
+from json import loads
 from json.decoder import JSONDecodeError
+from typing import Dict, Any, Union, Optional, List, Type
+from copy import deepcopy
+from logging import Logger
 import requests
 import urllib3
 from urllib3.exceptions import InsecureRequestWarning
-from ._version import _TITLE, _VERSION
-from ._result import Result, ExpandedResult
-from ._base_url import BaseURL
-from ._container_base_url import ContainerBaseURL
-from ._uber_default_preference import PREFER_NONETYPE, MOCK_OPERATIONS
+from .._api_request import APIRequest
+from .._enum import BaseURL, ContainerBaseURL
+from .._constant import (
+    PREFER_NONETYPE,
+    MOCK_OPERATIONS,
+    ALLOWED_METHODS as _ALLOWED_METHODS,
+    USER_AGENT as _USER_AGENT,
+    MAX_DEBUG_RECORDS,
+    GLOBAL_API_MAX_RETURN
+)
+from .._error import (
+    RegionSelectError,
+    SDKError,
+    InvalidMethod,
+    KeywordsOnly,
+    APIError,
+    NoContentWarning,
+    PayloadValidationError,
+    InvalidBaseURL,
+    SSLDisabledWarning
+    )
+from .._result import Result
 urllib3.disable_warnings(InsecureRequestWarning)
 
-# Restrict requests to only allowed HTTP methods
-_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'UPDATE']
-# Default user-agent string
-_USER_AGENT = f"{_TITLE}/{str(_VERSION)}"
 
-
-def validate_payload(validator: dict, params: dict, required: list = None) -> bool:
+def validate_payload(validator: Dict[str, Type],
+                     payload: Dict[str, Union[str, int, dict, list, bytes]],
+                     required: Optional[List[str]] = None
+                     ) -> bool:
     """Validate parameters and body payloads sent to the API."""
     # Repurposed with permission from
     # https://github.com/yaleman/crowdstrike_api
     #         __
     #        ( (\
     #         \ =\
     #        __\_ `--\
-    #       (____))(  \----
+    #       (____))(  \-----
     #       (____)) _     Thanks
     #       (____))       James!
     #       (____))____/----
     #
     if required:
         for key in required:
-            if key not in params:
-                raise ValueError(f"Argument {key} must be specified.")
+            if key not in payload:
+                raise PayloadValidationError(code=400, msg=f"Argument {key} must be specified.")
 
-    for key in params:
+    for key in payload:
         if key not in validator:
-            raise ValueError(f"{key} is not a valid argument.")
-        if not isinstance(params[key], validator[key]):
+            raise PayloadValidationError(code=400, msg=f"{key} is not a valid argument.")
+        if not isinstance(payload[key], validator[key]):
             should = validator[key]
-            was = type(params[key])
-            raise TypeError(f"{key} is not the valid type. Should be: {should}, was {was}")
+            was = type(payload[key])
+            raise PayloadValidationError(code=400, msg=f"{key} is not the valid type. Should be: {should}, was {was}")
 
     return True
 
 
 def generate_b64cred(client_id: str, client_secret: str) -> str:
     """base64 encodes passed client_id and client_secret for authorization headers."""
     cred = f"{client_id}:{client_secret}"
     b64_byt = base64.b64encode(cred.encode("ascii"))
     encoded = b64_byt.decode("ascii")
 
     return encoded
 
 
-def handle_single_argument(passed_arguments: list, passed_keywords: dict, search_key: str) -> dict:
+def handle_single_argument(passed_arguments: tuple,
+                           passed_keywords: Optional[dict] = None,
+                           search_key: Optional[str] = None
+                           ) -> dict:
     """Handle a single argument that is provided without keywords.
 
     Reviews arguments passed to a method and injects them into the keyword dictionary if they
     match the search string.
     """
-    if len(passed_arguments) > 0:
+    if not passed_keywords:
+        passed_keywords: dict = {}
+    if len(passed_arguments) > 0 and search_key:
         passed_keywords[search_key] = passed_arguments[0]
 
     return passed_keywords
 
 
-def force_default(defaults: list, default_types: list = None):
+def force_default(defaults: List[str], default_types: List[str] = None):
     """Force default values.
 
     Intended to decorate other functions.
 
     Keyword arguments:
     defaults = list of values to default
     default_types = list of types to default the values to
 
-    Example: @force_default(defaults=["parameters], default_types=["dict"])
+    Example: @force_default(defaults=["parameters"], default_types=["dict"])
     """
     if not default_types:
         default_types = []
 
     def wrapper(func):
         """Inner wrapper."""
         @functools.wraps(func)
         def factory(*args, **kwargs):
             """Parameter factory.
 
             This method is a factory and runs through keywords passed to the called function,
             setting defaults on values within the **kwargs dictionary when necessary
             as specified in our "defaults" list that is passed to the parent wrapper.
+            It also wraps the protected method with an error handler.
             """
             element_count = 0   # Tracker so we can retrieve matching data types
             # Loop through every element specified in our defaults list
             for element in defaults:
                 if element in kwargs:
                     # It exists but it's a NoneType
                     if kwargs.get(element) is None:
@@ -138,65 +164,156 @@
                 else:
                     # Not present whatsoever
                     kwargs[element] = get_default(default_types, element_count)
                 # Increment our tracker for our sibling default_types list
                 element_count += 1
 
             try:
-                created = func(*args, **kwargs)
-            except TypeError:
-                # They passed us an argument but did not specify what it was (non-keyword) [Issue #263]
-                created = generate_error_result("Keyword arguments must be used for this method.")
-
+                # created = func(*args, **kwargs)
+                try:
+                    created = func(*args, **kwargs)
+                except TypeError as keywords_only:
+                    # They passed us an argument but did not specify
+                    # what it was (non-keyword) [Issue #263]
+                    raise KeywordsOnly from keywords_only
+            except KeywordsOnly as bad_keywords:
+                created = bad_keywords.result
+            except NoContentWarning as no_content_received:
+                created = no_content_received.result
+            except APIError as api_error:
+                # Should only receive this in pythonic mode
+                raise api_error
+            except (SDKError, InvalidMethod) as bad_sdk_command:
+                created = bad_sdk_command.result
             return created
         return factory
     return wrapper
 
 
-def service_request(caller: object = None, **kwargs) -> object:  # May return dict or object datatypes
-    """Check for token expiration, refresh if possible and then perform the request."""
-    if caller:
-        try:
-            if caller.auth_object:
-                if caller.auth_object.token_expired():
-                    auth_response = caller.auth_object.token()
-                    if auth_response["status_code"] == 201:
-                        caller.headers['Authorization'] = f"Bearer {auth_response['body']['access_token']}"
-                    else:
-                        caller.headers['Authorization'] = "Bearer "
-                else:
-                    caller.headers['Authorization'] = f"Bearer {caller.auth_object.token_value}"
-        except AttributeError:
-            pass
+# Caller is a derivitive of ServiceClass below, but we cannot type it until after
+# support for Python 3.6 is dropped due to the circular reference it would cause.
+def service_request(caller=None, **kwargs) -> Union[Dict[str, Union[int, dict, list]], bytes]:
+    """Prepare and then perform the request (Service Classes only).
 
+    Inbound caller argument should be a ServiceClass class or derivative.
+    """
+    if caller:
+        # EAFP
         try:
-            proxy = caller.proxy
+            proxy: Optional[Dict[str, str]] = caller.proxy
         except AttributeError:
             proxy = None
 
         try:
-            timeout = caller.timeout
+            timeout: Optional[int] = caller.timeout
         except AttributeError:
             timeout = None
 
         try:
-            user_agent = caller.user_agent
+            user_agent: Optional[str] = caller.user_agent
         except AttributeError:
             user_agent = None
 
-    returned = perform_request(proxy=proxy, timeout=timeout, user_agent=user_agent, **kwargs)
+        try:
+            log_utility: Optional[Logger] = caller.log
+        except AttributeError:
+            log_utility = None
 
-    return returned
+        try:
+            debug_count: Optional[int] = caller.debug_record_count
+        except AttributeError:
+            debug_count = None
+        try:
+            do_sanitize: Optional[bool] = caller.sanitize_log
+        except AttributeError:
+            do_sanitize = None
+        try:
+            # Allow pythonic behaviors to be enabled / disabled per request
+            do_pythonic: Optional[bool] = kwargs.get("pythonic", None)
+            if not isinstance(do_pythonic, bool):
+                kwargs["pythonic"] = caller.pythonic
+            # do_pythonic: Optional[bool] = caller.pythonic
+        except AttributeError:
+            kwargs["pythonic"] = None
+
+    return perform_request(proxy=proxy,
+                           timeout=timeout,
+                           user_agent=user_agent,
+                           log_util=log_utility,
+                           debug_record_count=debug_count,
+                           sanitize=do_sanitize,
+                           **kwargs
+                           )
+
+
+# pylint: disable=R0912  # I don't disagree, but this will work for now.
+def calc_content_return(resp: requests.Response,
+                        contain: bool,
+                        auth: bool,
+                        log: Logger,
+                        pythonic_mode: bool,
+                        ) -> Union[dict, bytes]:
+    """Calculate the returned content based upon the results from the call to requests."""
+    returned = {}
+    returned_content_type = resp.headers.get('content-type', "Binary")
+    if log:
+        log.debug("RECEIVED: Content returned in %s format", returned_content_type)
+    if returned_content_type.startswith("application/json"):  # Issue 708
+        json_resp: Union[dict, Result] = {}
+        try:
+            json_resp = resp.json()
+        except JSONDecodeError:
+            # It says JSON in the headers but it came back to us as a binary string.
+            json_resp = loads(resp.content.decode("ascii"))
+        finally:
+            # Default behavior is to return results as a standardized dictionary.
+            returned = Result(status_code=resp.status_code,
+                              headers=resp.headers,
+                              body=json_resp
+                              ).full_return
+    elif contain:
+        returned = Result(resp.status_code, resp.headers, resp.json()).full_return
+    else:
+        # Binary response
+        if not resp.content:
+            if auth:
+                # Issue 433 - GovCloud autodiscovery is not supported
+                raise RegionSelectError(headers=resp.headers)
+
+            # Nothing was returned, so give them back the blank binary object
+            # Emulates < v1.3 functionality
+            returned = resp.content
+        else:
+            # returned = resp.content
+            returned = Result(resp.status_code, resp.headers, resp.content).full_return
+
+    # Catch and log API response errors
+    try:
+        if resp.status_code >= 400:
+            _message = None
+            _errors = returned.get("body", {}).get("errors", [])
+            if _errors:
+                _message = f"ERROR: {_errors[0]['message']}"
+            raise APIError(code=resp.status_code, message=_message, headers=resp.headers)
+    except APIError as api_error:
+        # Still return the payload unless we're in pythonic mode
+        if log:
+            log.error(api_error.message)
+        if pythonic_mode:
+            raise api_error
 
+    return returned, returned_content_type
 
+
+# pylint: disable=R0915
 @force_default(defaults=["headers"], default_types=["dict"])
-def perform_request(endpoint: str = "",  # pylint: disable=R0912
+def perform_request(endpoint: str = "",
                     headers: dict = None,
-                    **kwargs
-                    ) -> object:  # May return dict or object data types
+                    **kwargs      # May return dict or binary data types
+                    ) -> Union[Dict[str, Union[int, Dict[str, str], Dict[str, Dict]]], bytes]:
     """Leverage the requests library to perform the requested CrowdStrike OAuth2 API operation.
 
     Keyword arguments:
     method: str - HTTP method to use when communicating with the API
         - Example: GET, POST, PATCH, DELETE or UPDATE
     endpoint: str - API endpoint, including the URL base
         - Example: https://api.crowdstrike.com/oauth2/revoke
@@ -224,78 +341,144 @@
         - Example: (5.05, 25)
     user_agent: string
         - Example: companyname-integrationname/version
     expand_result: bool - Enable expanded results output
         - Example: True
     container: bool - Is this request being sent to a Falcon Container registry endpoint
         - Example: False
+    log_util: Logger - Logging utility
+    debug_record_count: int - Maximum number of records to log in debug logs
+    authenticating: bool - This request is driving a token request
     """
-    method = kwargs.get("method", "GET")
-    body = kwargs.get("body", None)
-    body_validator = kwargs.get("body_validator", None)
-    user_agent = kwargs.get("user_agent", None)
-    expand_result = kwargs.get("expand_result", False)
-    perform = True
-    if method.upper() in _ALLOWED_METHODS:
-        # Validate parameters
-        # 05.21.21/JSH - Param validation is now handled by the updated args_to_params method
+    # Shortcut for now
+    pythonic = kwargs.get("pythonic", False)
+    api: APIRequest = APIRequest(endpoint, kwargs)
+    if not api.verify:
+        ssl_disabled = SSLDisabledWarning()
+        if pythonic:
+            warn(ssl_disabled.message, SSLDisabledWarning, stacklevel=2)
+        else:
+            api.log_warning(msg=ssl_disabled.message)
 
+    if api.method.upper() in _ALLOWED_METHODS:
         # Validate body payload
-        if body_validator:
+        if api.body_validator:
             try:
-                validate_payload(body_validator, body, kwargs.get("body_required", None))
-            except ValueError as err:
-                returned = generate_error_result(message=f"{str(err)}")
-                perform = False
-            except TypeError as err:
-                returned = generate_error_result(message=f"{str(err)}")
-                perform = False
+                validate_payload(api.body_validator, api.body_payload, api.body_required)
+            except PayloadValidationError as err:
+                api.log_error(400, err.message, err.result)
+                returned = err.result
+                api.perform = False
 
         # Perform the request
-        if perform:
-            if user_agent:
-                headers["User-Agent"] = user_agent
+        if api.perform:
+            if api.user_agent:
+                headers["User-Agent"] = api.user_agent
             else:
-                headers["User-Agent"] = _USER_AGENT  # Force all requests to pass the User-Agent identifier
+                # Force all requests to pass the User-Agent identifier
+                headers["User-Agent"] = _USER_AGENT
             headers["CrowdStrike-SDK"] = _USER_AGENT
             try:
-                response = requests.request(method.upper(), endpoint, params=kwargs.get("params", None),
-                                            headers=headers, json=kwargs.get("body", None), data=kwargs.get("data", None),
-                                            files=kwargs.get("files", []), verify=kwargs.get("verify", True),
-                                            proxies=kwargs.get("proxy", None), timeout=kwargs.get("timeout", None)
+                # Log our payloads if debugging is enabled
+                log_api_payloads(api, headers)
+                response = requests.request(api.method.upper(), endpoint, params=api.param_payload,
+                                            headers=headers, json=api.body_payload, data=api.data_payload,
+                                            files=api.files, verify=api.verify,
+                                            proxies=api.proxy, timeout=api.timeout
                                             )
-                # Force binary when content-type is not provided
-                returning_content_type = response.headers.get('content-type', "Binary")
-                if returning_content_type.startswith("application/json"):  # Issue 708
-                    content_return = Result()(response.status_code, response.headers, response.json())
-                elif kwargs.get("container", False):
-                    content_return = Result()(response.status_code, response.headers, response.json())
-                else:
-                    content_return = response.content
-                # Expanded results allow for status code and header checks on binary returns
-                if expand_result:
-                    returned = ExpandedResult()(response.status_code, response.headers, content_return)
+                api.debug_headers = response.headers
+                content_return, returning_content_type = calc_content_return(response,
+                                                                             api.container,
+                                                                             api.authenticating,
+                                                                             api.log_util,
+                                                                             pythonic
+                                                                             )
+                # Expanded results allow for status code and
+                # header checks on binary returns.
+                # Maintained for < v1.3 syntax compatibility
+                if api.expand_result:
+                    returned = Result(response.status_code, response.headers, content_return).tupled
                 else:
                     returned = content_return
 
-            except JSONDecodeError:  # pragma: no cover
+                # Log our response if debugging is enabled
+                log_api_activity(content_return, returning_content_type, api)
+
+                # !!! EXPERIMENTAL !!!
+                # This functionality is new in v1.3.0 and still experimental, mileage may vary.
+                if pythonic:
+                    if isinstance(returned, bytes):
+                        returned = Result(response.status_code, response.headers, returned)
+                    else:
+                        returned = Result(full=returned)
+
+            except RegionSelectError as bad_region:
+                # More than likely they tried to autoselect to GovCloud
+                returned = bad_region.result
+                api.log_error(returned.get("status_code"), bad_region.message, returned)
+
+            except JSONDecodeError as json_decode_error:
                 # No response content, but a successful request was made
-                returned = generate_ok_result(
-                    message="No content returned",
-                    code=response.status_code,
-                    headers=response.headers
-                    )
-            except Exception as err:  # pylint: disable=W0703  # General catch-all for anything coming out of requests
-                returned = generate_error_result(message=f"{str(err)}")
+                api.log_warning("WARNING: No content was received for this request.")
+                raise NoContentWarning(headers=response.headers) from json_decode_error
+
+            except Exception as havoc:  # pylint: disable=W0703
+                # General catch-all for anything coming          ____ ____ _ _      \\       o   o
+                # out of requests or the library itself.         |___ |--<  Y        ||      |\O/|
+                # Pass this error up to the parent try/catch                          \\      \Y/
+                # block residing within our decorator        _  _ ____ _  _ ____ ____         /W\
+                # (force_default) for handling.              |--| |--|  \/  [__] |___  !!   _|WWW|_
+                if pythonic:
+                    # Oh wait, we're pythonic, lets generate
+                    # a regular python error condition instead.
+                    raise havoc
+
+                raise SDKError(message=f"{str(havoc)}", headers=api.debug_headers) from havoc
     else:
-        returned = generate_error_result(message="Invalid API operation specified.", code=405)
+        raise InvalidMethod
 
     return returned
 
 
+def log_api_payloads(api: APIRequest, headers: dict):
+    """Log the payloads and API response to the debug log."""
+    if api.log_util:
+        _headers = headers
+        _param_payload = api.param_payload
+        _body_payload = api.body_payload
+        _data_payload = api.data_payload
+        if api.sanitize_log:
+            _headers = sanitize_dictionary(deepcopy(headers))
+            _param_payload = sanitize_dictionary(deepcopy(api.param_payload))
+            _body_payload = sanitize_dictionary(deepcopy(api.body_payload))
+            _data_payload = sanitize_dictionary(deepcopy(api.data_payload))
+        api.log_util.debug("ENDPOINT: %s (%s)", api.endpoint, api.method)
+        api.log_util.debug("HEADERS: %s", _headers)
+        api.log_util.debug("PARAMETERS: %s", _param_payload)
+        api.log_util.debug("BODY: %s", _body_payload)
+        api.log_util.debug("DATA: %s", _data_payload)
+
+
+def log_api_activity(content_return: Union[dict, bytes], content_type: str, api: APIRequest):
+    """Log the payloads and API response to the debug log."""
+    if api.log_util:
+        if isinstance(content_return, dict):
+            _status_code = content_return.get("status_code", None)
+            if _status_code:
+                api.log_util.debug("STATUS CODE: %i", _status_code)
+
+        if content_type.startswith("application/json"):
+            if api.sanitize_log:
+                api.log_util.debug("RESULT: %s", sanitize_dictionary(deepcopy(content_return), api.max_debug))
+            else:
+                api.log_util.debug("RESULT: %s", content_return)
+        else:
+            api.log_util.debug("RESULT: binary response received from API")
+
+
 def generate_error_result(
         message: str = "An error has occurred. Check your payloads and try again.",
         code: int = 500,
         **kwargs
         ) -> dict:
     """Normalize error messages."""
     return_headers = kwargs.get("headers", {})
@@ -304,15 +487,15 @@
 
 def generate_ok_result(message: str = "Request returned with success", code: int = 200, **kwargs) -> dict:
     """Normalize OK messages."""
     return_headers = kwargs.get("headers", {})
     return Result()(status_code=code, headers=return_headers, body={"message": message, "resources": []})
 
 
-def get_default(types: list, position: int):
+def get_default(types: list, position: int) -> Union[list, str, int, dict, bool]:
     """I determine the requested default data type and return it."""
     default_value_names = ["list", "str", "int", "dict", "bool"]
     default_value_types = [[], "", 0, {}, False]
     value_count = 0
     retval = {}  # Default to dictionary data type as that is our most often used
     for type_ in default_value_names:
         try:
@@ -374,22 +557,22 @@
                 returned_payload[element.__name__] = payload[element]
             else:
                 returned_payload[element] = payload[element]
 
     return returned_payload
 
 
-def process_service_request(calling_object: object,  # pylint: disable=R0914 # (19/15)
+def process_service_request(calling_object,  # pylint: disable=R0914 # (19/15)
                             endpoints: list,
                             operation_id: str,
                             **kwargs
                             ) -> dict:
     """Perform a request originating from a service class module.
 
-    Calculates the target_url based upon the provided operation ID and endpoint list.
+    Calculate the target_url based upon the provided operation ID and endpoint list.
 
     Keyword arguments:
     endpoints -- list - List of service class endpoints, defined as Endpoints in a service class. [required]
     operation_id -- The name of the operation ID. Normally this is also the function name from the service class. [required]
     method -- HTTP method to execute. GET, POST, PATCH, DELETE, PUT accepted. Defaults to GET.
     keywords -- Dictionary of kwargs that were passed to the function within the service class.
     params -- Dictionary of parameters passed to the service class function.
@@ -399,15 +582,19 @@
     files -- List of files to be uploaded.
     partition -- ID of the partition to open (Event Streams API)
     distinct_field -- Field name to retrieve distinct values for (Sensor Update Policies API)
     image_id -- Image ID to be deleted (Falcon Container API)
     body_validator -- Dictionary containing details regarding body payload validation
     body_required -- List of required body payload parameters
     expand_result -- Request expanded results output
+    pythonic -- Pythonic responses
     """
+    # Log the operation ID if we have logging enabled.
+    if calling_object.log:
+        calling_object.log.debug("OPERATION: %s", operation_id)
     target_endpoint = [ep for ep in endpoints if operation_id == ep[0]][0]
     base_url = calling_object.base_url
     container = False
     if operation_id in MOCK_OPERATIONS:
         for base in [burl for burl in dir(BaseURL) if "__" not in burl]:
             if BaseURL[base].value == calling_object.base_url.replace("https://", ""):
                 base_url = f"https://{ContainerBaseURL[base].value}"
@@ -425,56 +612,65 @@
         target_url = target_url.format(str(passed_image_id))
     # Retrieve our keyword arguments
     passed_keywords = kwargs.get("keywords", None)
     passed_params = kwargs.get("params", None)
     parameter_payload = None
     if passed_keywords or passed_params:
         parameter_payload = args_to_params(passed_params, passed_keywords, endpoints, operation_id)
-    passed_headers = kwargs.get("headers", None) if kwargs.get("headers", None) else calling_object.headers
+    passed_headers = kwargs.get("headers", None) if kwargs.get("headers", None) else {}
+    joined_headers = {
+        ** calling_object.headers,
+        ** passed_headers
+    }
     expand_result = passed_keywords.get("expand_result", False) if passed_keywords else kwargs.get("expand_result", False)
     new_keywords = {
         "caller": calling_object,
         "method": target_method,
         "endpoint": target_url,
         "verify": calling_object.ssl_verify,
-        "headers": passed_headers,
+        "headers": joined_headers,
         "params": parameter_payload,
         "body": kwargs.get("body", None),
         "data": kwargs.get("data", None),
         "files": kwargs.get("files", None),
         "body_validator": kwargs.get("body_validator", None),
         "body_required": kwargs.get("body_required", None),
         "expand_result": expand_result,
-        "container": container
+        "container": container,
+        "pythonic": kwargs.get("pythonic", None),
+        "perform": True
     }
 
     return service_request(**new_keywords)
 
 
-def confirm_base_url(provided_base: str = "https://api.crowdstrike.com") -> str:
+def confirm_base_url(provided_base: Optional[str] = "https://api.crowdstrike.com") -> str:
     """Confirm the passed base_url value matches URL syntax.
 
     If it does not, it is looked up in the BaseURL enum. If the value is not found
     within the enum, https:// is prepended to the value and then it is used for API requests.
     """
     # Assume they passed a full URL
     returned_base = provided_base
-    if "://" not in provided_base:
-        # They're passing the name instead of the URL
-        dashed_bases = ["US-1", "US-2", "EU-1", "US-GOV-1"]
-        if provided_base.upper() in dashed_bases:
-            provided_base = provided_base.replace("-", "")  # Strip the dash
-        try:
-            returned_base = f"https://{BaseURL[provided_base.upper()].value}"
-        except KeyError:
-            # Invalid base URL name, fall back to assuming they didn't give us https
-            returned_base = f"https://{provided_base}"
-
-    if returned_base[-1] == "/":  # Issue 558
-        returned_base = returned_base[:-1]
+    try:
+        if "://" not in provided_base:
+            # They're passing the name instead of the URL
+            dashed_bases = ["US-1", "US-2", "EU-1", "US-GOV-1"]
+            if provided_base.upper() in dashed_bases:
+                provided_base = provided_base.replace("-", "")  # Strip the dash
+            try:
+                returned_base = f"https://{BaseURL[provided_base.upper()].value}"
+            except KeyError:
+                # Invalid base URL name, fall back to assuming they didn't give us https
+                returned_base = f"https://{provided_base}"
+
+        if returned_base[-1] == "/":  # Issue 558
+            returned_base = returned_base[:-1]
+    except (AttributeError, TypeError) as bad_base_url:
+        raise InvalidBaseURL from bad_base_url
 
     return returned_base
 
 
 def confirm_base_region(provided_base_url: str = "https://api.crowdstrike.com") -> str:
     """Retrieve the base url shortname based upon the provided base url value."""
     try:
@@ -514,7 +710,55 @@
         token_region = auth_result["headers"]["X-Cs-Region"].replace("-", "")
     if token_region.upper() in base_url_regions():
         requested_region = confirm_base_region(confirm_base_url(provided_base_url))
         if token_region != requested_region:
             new_base_url = confirm_base_url(token_region.upper())
 
     return new_base_url
+
+
+def sanitize_dictionary(dirty: Any, record_max: int = MAX_DEBUG_RECORDS) -> dict:
+    """Strip confidential data from logged dictionaries."""
+    cleaned = dirty
+    if isinstance(dirty, dict):
+        # cleaned = deepcopy(dict(dirty))
+        redacted = ["access_token", "client_id", "client_secret", "member_cid", "token"]
+        for redact in redacted:
+            if redact in cleaned:
+                cleaned[redact] = "REDACTED"
+            if "body" in cleaned:
+                if redact in cleaned["body"]:
+                    cleaned["body"][redact] = "REDACTED"
+                if "resources" in cleaned["body"]:
+                    # Log results are limited to MAX_DEBUG_RECORDS
+                    # number of items within the resources list
+                    if cleaned["body"]["resources"]:
+                        del cleaned["body"]["resources"][max(1, min(record_max,
+                                                                    GLOBAL_API_MAX_RETURN
+                                                                    )):]
+        if "Authorization" in cleaned:
+            cleaned["Authorization"] = "Bearer REDACTED"
+
+    return cleaned
+
+
+# Python 3.6 compatibility warning: Cannot properly type the interface.
+def log_class_startup(interface, log_device: Logger):
+    """Log the startup of one of our interface or Service Classes."""
+    log_device.debug("CREATED: %s interface class", interface.__class__.__name__)
+    log_device.debug("CONFIG: Base URL set to %s", interface.base_url)
+    log_device.debug("CONFIG: SSL verification is set to %s", str(interface.ssl_verify))
+    log_device.debug("CONFIG: Timeout set to %s seconds", str(interface.timeout))
+    log_device.debug("CONFIG: Proxy dictionary: %s", str(interface.proxy))
+    log_device.debug("CONFIG: User-Agent string set to: %s", interface.user_agent)
+    log_device.debug("CONFIG: Token renewal window set to %s seconds",
+                     str(interface.renew_window)
+                     )
+    log_device.debug("CONFIG: Maximum number of records to log: %s",
+                     interface.debug_record_count
+                     )
+    log_device.debug(
+        "CONFIG: Log sanitization is %s", "enabled" if interface.sanitize_log else "disabled"
+        )
+    log_device.debug(
+        "CONFIG: Pythonic responses are %s", "enabled" if interface.pythonic else "disabled"
+        )
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/_version.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_version.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
-_VERSION = '1.2.9'
+_VERSION = '1.3.0.dev1'
 _MAINTAINER = 'Joshua Hiller'
 _AUTHOR = 'CrowdStrike'
 _AUTHOR_EMAIL = 'falconpy@crowdstrike.com'
 _CREDITS = 'CrowdStrike'
 _DESCRIPTION = "The CrowdStrike Falcon SDK for Python 3"
 _TITLE = "crowdstrike-falconpy"
 _PROJECT_URL = "https://github.com/CrowdStrike/falconpy"
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/alerts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/alerts.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union, Optional, List
 from ._util import force_default, process_service_request
 from ._payload import (
     aggregate_payload, generic_payload_list, update_alerts_payload
     )
 from ._service_class import ServiceClass
 from ._endpoint._alerts import _alerts_endpoints as Endpoints
 
@@ -53,15 +54,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def get_aggregate_alerts(self: object, body: list = None, **kwargs) -> dict:
+    def get_aggregate_alerts(self, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregates for Alerts across all CIDs.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "date_ranges": [
@@ -126,15 +127,15 @@
             operation_id="PostAggregatesAlertsV1",
             body=body
             )
 
     # PatchEntitiesAlertsV1 has been **DECOMISSIONED**
 
     # @force_default(defaults=["body"], default_types=["dict"])
-    # def update_alerts(self: object, *args, body: dict = None, **kwargs) -> dict:
+    # def update_alerts(self, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
     #     """Perform actions on alerts identified by detection ID(s) in request.
 
     #     Keyword arguments:
     #     action_parameters -- List of dictionaries containing action specific parameter settings.
     #     add_tag -- add a tag to 1 or more alert(s). String. Overridden by action_parameters.
     #     append_comment -- appends new comment to existing comments. String.
     #                       Overridden by action_parameters.
@@ -199,15 +200,19 @@
     #         calling_object=self,
     #         endpoints=Endpoints,
     #         operation_id="PatchEntitiesAlertsV1",
     #         body=body
     #         )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_alerts(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def update_alerts(self,
+                      *args,
+                      body: Optional[Dict[str, List[Union[str, Dict[str, str]]]]] = None,
+                      **kwargs
+                      ) -> Dict[str, Union[int, dict]]:
         """Perform actions on alerts identified by detection ID(s) in request.
 
         Keyword arguments:
         action_parameters -- List of dictionaries containing action specific parameter settings.
         add_tag -- add a tag to 1 or more alert(s). String. Overridden by action_parameters.
         append_comment -- appends new comment to existing comments. String.
                           Overridden by action_parameters.
@@ -259,26 +264,29 @@
                                                      submitted_keywords=kwargs,
                                                      payload_value="ids"
                                                      ),
                 passed_keywords=kwargs
                 )
 
         # Passing action_parameters overrides other keywords
-        if kwargs.get("action_parameters", None):
-            body["action_parameters"] = kwargs.get("action_parameters", None)
-
+        _action_params: Optional[List[Union[str, Dict[str, str]]]] = kwargs.get("action_parameters", None)
+        if _action_params:
+            body["action_parameters"] = _action_params
+        # Getting this from mypy:
+        # src/falconpy/alerts.py:269: error:
+        # Unsupported target for indexed assignment ("Optional[Dict[str, List[Union[str, Dict[str, str]]]]]")
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PatchEntitiesAlertsV2",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_alerts(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_alerts(self, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve all Alerts given their IDs.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "ids": [
                         "string"
@@ -308,15 +316,15 @@
             operation_id="PostEntitiesAlertsV1",
             body=body,
             body_validator={"ids": list} if self.validate_payloads else None,
             body_required=["ids"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_alerts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_alerts(self, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for detection IDs that match a given query.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
 
         For more detail regarding filtering options, please review:
         https://falcon.crowdstrike.com/documentation/86/detections-monitoring-apis#find-detections
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/api_complete.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/_auth_object/_falcon_interface.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,8 +1,11 @@
-"""All-in-one CrowdStrike Falcon OAuth2 API harness.
+"""API Interface base class.
+
+This file contains the definition of the standard base class that provides
+necessary functionality to authenticate to the CrowdStrike Falcon OAuth2 API.
 
  _______                        __ _______ __        __ __
 |   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
 |.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
 |.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
 |:  1   |                         |:  1   |
 |::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
@@ -32,343 +35,438 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import time
-from ._util import _ALLOWED_METHODS
-from ._util import (
-    perform_request,
-    generate_b64cred,
-    generate_error_result,
-    confirm_base_url,
-    args_to_params,
-    return_preferred_default,
+import warnings
+from logging import Logger, getLogger
+from typing import Dict, Optional, Union
+from ._base_falcon_auth import BaseFalconAuth
+from ._bearer_token import BearerToken
+from .._log import LogFacility
+from .._constant import MIN_TOKEN_RENEW_WINDOW, MAX_TOKEN_RENEW_WINDOW
+from ._interface_config import InterfaceConfiguration
+from .._enum import TokenFailReason
+from .._util import (
     autodiscover_region,
+    perform_request,
+    log_class_startup,
+    login_payloads,
+    logout_payloads
     )
-from ._base_url import BaseURL
-from ._container_base_url import ContainerBaseURL
-from ._uber_default_preference import PREFER_IDS_IN_BODY, MOCK_OPERATIONS
-from ._token_fail_reason import TokenFailReason
-from ._endpoint import api_endpoints
-
-
-class APIHarness:
-    """This one does it all. It's like the One Ring with significantly fewer orcs."""
-
-    # pylint: disable=too-many-instance-attributes
-    _token_fail_headers = {}  # Issue #578
-
-    def __init__(self: object,  # pylint: disable=R0913
-                 base_url: str = "https://api.crowdstrike.com",
-                 creds: dict = None,
-                 client_id: str = None,
-                 client_secret: str = None,
-                 member_cid: str = None,
-                 ssl_verify: bool = True,
-                 proxy: dict = None,
-                 timeout: float or tuple = None,
-                 user_agent: str = None,
-                 renew_window: int = 120
-                 ) -> object:
-        """Uber class constructor.
-
-        Instantiates an instance of the class, ingests credentials,
-        the base URL and the SSL verification boolean.
-        Afterwards class attributes are initialized.
-
-        Keyword arguments:
-        base_url: CrowdStrike API URL to use for requests. [Default: US-1]
-        ssl_verify: Boolean specifying if SSL verification should be used. [Default: True]
-        proxy: Dictionary of proxies to be used for requests.
-        timeout: Float or tuple specifying timeouts to use for requests.
-        creds: Dictionary containing CrowdStrike API credentials.
-               Mutually exclusive to client_id / client_secret.
-               {
-                   "client_id": "CLIENT_ID_HERE",
-                   "client_secret": "CLIENT_SECRET_HERE",
-                   "member_cid": "CHILD_CID_MSSP_ONLY"
-               }
-        client_id: Client ID for the CrowdStrike API. Mutually exclusive to creds.
-        client_secret: Client Secret for the CrowdStrike API. Mutually exclusive to creds.
-        member_cid: Child CID to connect to. (MSSP only) Mutually exclusive to creds.
-        user_agent: User-Agent string to use for all requests made to the CrowdStrike API.
-                    String. Defaults to crowdstrike-falconpy/VERSION.
-        renew_window: Amount of time (in seconds) between now and the token expiration before
-                      a refresh of the token is performed. Default: 120, Max: 1200
-                      Values over 1200 will be reset to the maximum.
+from .._error import InvalidCredentials, NoAuthenticationMechanism
 
-        This method only accepts keywords to specify arguments.
-        """
+
+class FalconInterface(BaseFalconAuth):
+    """Standard Falcon API interface used by Service Classes."""
+
+    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
+    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
+    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
+    #
+    # These attributes are present in all FalconInterface objects, regardless if we are referring
+    # to APIHarness, OAuth2 or custom inheriting classes.
+    #
+    # The default credential dictionary, where the client_id and client_secret are stored.
+    _creds: Dict[str, str] = {}
+    # Starting with v1.3.0 minimal python native logging is available. In order to reduce
+    # potential impacts to developer configurations, this facility is extremely limited
+    # and not implemented by default. (Meaning logs are not generated.)
+    # To enable logging, pass the keyword "debug" with a value of True to the constructor.
+    _log: LogFacility = LogFacility()
+    # Our token is stored within a BearerToken object.
+    _token: BearerToken = BearerToken()
+    # Configuration detail for this interface.
+    _config: InterfaceConfiguration = None
+    # Pythonic behavior.
+    _pythonic: bool = False
+
+    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
+    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
+    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
+    #
+    # The default constructor for all authentication objects. Ingests provided credentials
+    # and sets the necessary class attributes based upon the authentication detail received.
+    # pylint: disable=R0913,R0914
+    def __init__(self,
+                 access_token: Optional[Union[str, bool]] = False,
+                 base_url: Optional[str] = "https://api.crowdstrike.com",
+                 creds: Optional[Dict[str, str]] = None,
+                 client_id: Optional[str] = None,
+                 client_secret: Optional[str] = None,
+                 member_cid: Optional[str] = None,
+                 ssl_verify: Optional[bool] = True,
+                 proxy: Optional[Dict[str, str]] = None,
+                 timeout: Optional[Union[float, tuple]] = None,
+                 user_agent: Optional[str] = None,
+                 renew_window: Optional[int] = 120,
+                 debug: Optional[bool] = False,
+                 debug_record_count: Optional[int] = None,
+                 sanitize_log: Optional[bool] = None,
+                 pythonic: Optional[bool] = None
+                 ) -> "FalconInterface":
+        """Construct an instance of the FalconInterface class."""
+        # Set the pythonic behavior mode.
+        if isinstance(pythonic, bool):
+            self._pythonic = pythonic
+        # Setup our configuration object using the provided keywords.
+        self.config: InterfaceConfiguration = InterfaceConfiguration(base_url=base_url,
+                                                                     proxy=proxy,
+                                                                     timeout=timeout,
+                                                                     user_agent=user_agent,
+                                                                     ssl_verify=ssl_verify
+                                                                     )            # \ o /
+        # ____ _  _ ___ _  _ ____ _  _ ___ _ ____ ____ ___ _ ____ _  _                |
+        # |__| |  |  |  |__| |___ |\ |  |  | |    |__|  |  | |  | |\ |               / \
+        # |  | |__|  |  |  | |___ | \|  |  | |___ |  |  |  | |__| | \|
+        # Direct Authentication
         if client_id and client_secret and not creds:
             creds = {
                 "client_id": client_id,
                 "client_secret": client_secret
             }
-            # Have to pass member_cid the same way you pass client_id / secret
-            # If you use a creds dictionary, pass the member_cid there instead
+            # You must pass member_cid the same way you pass client_id / secret.
+            # If you use a creds dictionary, pass the member_cid there instead.
             if member_cid:
                 creds["member_cid"] = member_cid
         elif not creds:
             creds = {}
-        self.creds = creds
-        self.base_url = confirm_base_url(base_url)
-        self.ssl_verify = ssl_verify
-        self.proxy = proxy
-        self.timeout = timeout
-        self.token = False
-        self.token_expiration = 0
-        self.token_time = time.time()
-        self.authenticated = False
-        self.token_fail_reason = None
-        self.token_status = None
-        self.headers = lambda: {"Authorization": f"Bearer {self.token}"} if self.token else {}
-        self.commands = api_endpoints
-        self.user_agent = user_agent  # Issue #365
-        # Maximum renewal window is 20 minutes, Minimum is 2 minutes
-        self.token_renew_window = max(min(renew_window, 1200), 120)  # in seconds
+        # Credential Authentication (also powers Direct Authentication).
+        self.creds: Dict[str, str] = creds
+        # Set the token renewal window, ignored when using Legacy Authentication.
+        self.renew_window: int = max(min(renew_window, MAX_TOKEN_RENEW_WINDOW),
+                                     MIN_TOKEN_RENEW_WINDOW
+                                     )
+        # Legacy (Token) Authentication (fallback)
+        if access_token:
+            # Store this non-refreshable token, assuming it was just generated.
+            self._token: BearerToken = BearerToken(access_token, 1799)
+
+        # Log the creation of this object if debugging is enabled.
+        if debug:
+            # Ignored when debugging is disabled.
+            _debug_record_count: int = debug_record_count if debug_record_count else None
+            # Allow log sanitization to be overridden.
+            _sanitize = sanitize_log if isinstance(sanitize_log, bool) else None
+            # Logging facility for all classes using this interface, defaults to disabled.
+            self._log: LogFacility = LogFacility(getLogger(__name__),
+                                                 _debug_record_count,
+                                                 _sanitize
+                                                 )
+            # Log the startup of this class.
+            log_class_startup(self, self.log)
 
-    def valid_cred_format(self: object) -> bool:
-        """Confirm credential dictionary format.
+        try:
+            if not self.cred_format_valid and not self.token_value:
+                raise NoAuthenticationMechanism
+        except NoAuthenticationMechanism as no_auth_mechanism:
+            if pythonic:
+                warnings.warn(no_auth_mechanism.message, NoAuthenticationMechanism, stacklevel=2)
+            if self.log:
+                self.log.warning(no_auth_mechanism.message)
+
+    # _  _ ____ ___ _  _ ____ ___  ____
+    # |\/| |___  |  |__| |  | |  \ [__
+    # |  | |___  |  |  | |__| |__/ ___]
+    #
+    # The generic login and logout handlers are provided here and leverage private methods
+    # to perform the operation. These private methods can be overridden to provide individual
+    # login and logout functionality to different inheriting class types.
+    def login(self) -> dict or bool:
+        """Login to the Falcon API by requesting a new token."""
+        return self._login_handler()
+
+    def logout(self) -> dict or bool:
+        """Log out of the Falcon API by revoking the current token."""
+        return self._logout_handler()
+
+    # The default behavior for both the login and logout handlers is to return
+    # the entire dictionary created by the token API response.
+    def _login_handler(self, stateful: bool = True) -> dict:
+        """Login by requesting a new token.
 
-        Returns a boolean indicating if the client_id and
-        client_secret are present in the creds dictionary.
+        This method can also be leveraged to generate tokens without impacting authorization state.
         """
-        retval = False
-        if "client_id" in self.creds and "client_secret" in self.creds:
-            retval = True
-
-        return retval
-
-    def token_expired(self: object) -> bool:
-        """Return a boolean based upon the token expiration status."""
-        retval = False
-        if (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window):
-            retval = True
-
-        return retval
-
-    def authenticate(self: object) -> bool:
-        """Generate an authorization token."""
-        target = self.base_url+'/oauth2/token'
-        data_payload = {}
-        if self.valid_cred_format():
-            data_payload = {
-                'client_id': self.creds['client_id'],
-                'client_secret': self.creds['client_secret']
-            }
-        if "member_cid" in self.creds:
-            data_payload["member_cid"] = self.creds["member_cid"]
-
-        result = perform_request(method="POST",
-                                 endpoint=target,
-                                 data=data_payload,
-                                 headers={},
-                                 verify=self.ssl_verify,
-                                 proxy=self.proxy,
-                                 timeout=self.timeout,
-                                 user_agent=self.user_agent
-                                 )
-        if isinstance(result, dict):  # Issue #433
-            self.token_status = result["status_code"]
-            if self.token_status == 201:
-                self.token = result["body"]["access_token"]
-                self.token_expiration = result["body"]["expires_in"]
-                self.token_time = time.time()
-                self.authenticated = True
-                self.token_fail_reason = None
-                self.base_url = autodiscover_region(self.base_url, result)
+        _returned_headers = {}
+        try:
+            if self.cred_format_valid:
+                operation, target_url, data_payload = login_payloads(self.creds, self.base_url)
+                # Log the call to this operation if debugging is enabled.
+                if self.log:
+                    self.log.debug("OPERATION: %s", operation)
+                returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
+                                           headers={}, verify=self.ssl_verify, proxy=self.proxy,
+                                           timeout=self.timeout, user_agent=self.user_agent,
+                                           log_util=self.log, authenticating=True,
+                                           sanitize=self.sanitize_log
+                                           )
+                _returned_headers = returned["headers"]
+                if stateful:
+                    self.token_status = returned["status_code"]
+                    if self.token_status == 201:
+                        # Token generation was successful.
+                        self._token = BearerToken(token_value=returned["body"]["access_token"],
+                                                  expiration=returned["body"]["expires_in"],
+                                                  status=201
+                                                  )
+                        # Cloud Region auto discovery.
+                        self.base_url = autodiscover_region(self.base_url, returned)
+                    else:
+                        # Token generation failure, reset the current token and check for an error response.
+                        self._token = BearerToken(status=returned["status_code"])
+                        # Retrieve the list of errors, there should only be one item in the list.
+                        error_list = returned["body"].get("errors", [])
+                        if error_list:
+                            self.bearer_token.fail_token(returned["status_code"],
+                                                         error_list[0]["message"]
+                                                         )
             else:
-                self.authenticated = False
-                self._token_fail_headers = result["headers"]
-                if "errors" in result["body"]:
-                    if result["body"]["errors"]:
-                        self.token_fail_reason = result["body"]["errors"][0]["message"]
-        else:
-            self.authenticated = False
-            self.token_fail_reason = TokenFailReason["UNEXPECTED"].value
-            self.token_status = 403
-
-        return self.authenticated
-
-    def deauthenticate(self: object) -> bool:
-        """Revoke the current authorization token."""
-        target = str(self.base_url)+'/oauth2/revoke'
-        b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
-        header_payload = {"Authorization": f"basic {b64cred}"}
-        data_payload = {"token": f"{self.token}"}
-        revoked = False
-        if perform_request(method="POST", endpoint=target, data=data_payload,
-                           headers=header_payload, verify=self.ssl_verify,
-                           proxy=self.proxy, timeout=self.timeout, user_agent=self.user_agent
-                           )["status_code"] == 200:
-            self.authenticated = False
-            self.token = False
-            revoked = True
-        else:
-            revoked = False
-
-        return revoked
+                if stateful:
+                    self.bearer_token.fail_token(403, TokenFailReason["INVALID"])
+                raise InvalidCredentials(headers=_returned_headers)
+
+        except InvalidCredentials as bad_creds:
+            returned = bad_creds.result
+            if self.log:
+                self.log.error(bad_creds.message)
 
-    def _create_header_payload(self: object, passed_arguments: dict) -> dict:
-        """Create the HTTP header payload.
-
-        Creates the HTTP header payload based upon the existing class headers and passed arguments.
-        """
-        payload = self.headers()
-        if "headers" in passed_arguments:
-            for item in passed_arguments["headers"]:
-                payload[item] = passed_arguments["headers"][item]
-        if "content_type" in passed_arguments:
-            payload["Content-Type"] = str(passed_arguments["content_type"])
-
-        return payload
-
-    @staticmethod
-    def _handle_partition(tgt: str, kwa: dict):
-        if kwa.get("partition", None) is not None:
-            # Partition needs to be embedded into the endpoint URL
-            tgt = tgt.format(str(kwa.get("partition", None)))
-        return tgt
-
-    @staticmethod
-    def _handle_distinct_field(tgt: str, kwa: dict):
-        if kwa.get("distinct_field", None) is not None:
-            # distinct_field also needs to be embedded into the endpoint URL
-            tgt = tgt.format(str(kwa.get("distinct_field", None)))
-        return tgt
-
-    @staticmethod
-    def _handle_container_image_id(tgt: str, kwa: dict):
-        if kwa.get("image_id", None) is not None:
-            # container image ID also needs to be embedded into the endpoint URL
-            tgt = tgt.format(str(kwa.get("image_id", None)))
-        return tgt
-
-    @staticmethod
-    def _handle_body_payload_ids(kwa: dict):
-        if kwa.get("action", None) in PREFER_IDS_IN_BODY:
-            if kwa.get("ids", None):
-                # Handle the GET to POST method redirection for passed IDs
-                if not kwa.get("body", {}).get("ids", None):
-                    if "body" not in kwa:
-                        kwa["body"] = {}
-                    kwa["body"]["ids"] = kwa["ids"]
-            # Handle any body payload ID lists that are still strings
-            if isinstance(kwa.get("body", {}).get("ids", {}), str):
-                kwa["body"]["ids"] = kwa["body"]["ids"].split(",")
-        return kwa
-
-    def _handle_container_operations(self, kwa: dict, base_string: str):
-        """Handle Base URLs and keyword arguments for container registry operations."""
-        # Default to non-container registry operations
-        do_container = False
-        if kwa.get("action", None) in MOCK_OPERATIONS:
-            for base in [burl for burl in dir(BaseURL) if "__" not in burl]:
-                if BaseURL[base].value == self.base_url.replace("https://", ""):
-                    base_string = f"https://{ContainerBaseURL[base].value}"
-                    do_container = True
-            if kwa.get("action", None) == "ImageMatchesPolicy":
-                if "parameters" not in kwa:
-                    kwa["parameters"] = {}
-                kwa["parameters"]["policy_type"] = "image-prevention-policy"
-        return kwa, base_string, do_container
-
-    def command(self: object, *args, **kwargs) -> dict or bytes:
-        """Uber Class API command method.
-
-        Checks token expiration, renewing when necessary, then performs the request.
-
-        Keyword arguments:
-        action: str = ""                                    - API Operation ID to perform
-        parameters: dict = {}                               - Parameter payload (Query string)
-        body: dict = {}                                     - Body payload (Body)
-        data: dict = {}                                     - Data payload (Data)
-        headers: dict = {}                                  - Headers dictionary (HTTP Headers)
-        ids: list or str = None                             - ID list (IDs to handle)
-        partition: int or str = None                        - Partition number
-        distinct_field: str = None                          - Distinct Field
-        override: str = None   (format: 'METHOD,ENDPOINT')  - Override method and endpoint
-        action_name: str = None                             - Action to perform (API specific)
-        files: list = []                                    - List of files to upload
-        file_name: str = None                               - Name of the file to upload
-        content_type: str = None                            - Content_Type HTTP header
-        expand_result: bool = False                         - Request expanded results (Tuple)
-        image_id: str = None                                - Container image ID (Falcon Container only)
+        return returned
 
-        The first argument passed to this method is assumed to be 'action'. All others are ignored.
+    def _logout_handler(self, token_value: str = None, stateful: bool = True) -> dict:
+        """Log out by revoking the current token.
 
-        Returns: dict object containing API response or binary object depending on operation ID.
+        This method can also be leveraged to revoke other tokens.
         """
-        if self.token_expired():
-            # Authenticate them if we can
-            self.authenticate()
-
         try:
-            if not kwargs.get("action", None):
-                # Assume they're passing it in as the first param
-                kwargs["action"] = args[0]
-        except IndexError:
-            pass  # They didn't specify an action, use the default and try for an override instead
-
-        uber_command = [a for a in self.commands if a[0] == kwargs.get("action", None)]
-        if kwargs.get("override", None):
-            uber_command = [["Manual"] + kwargs["override"].split(",")]
-        if uber_command:
-            # Retrieve our default base URL
-            url_base = self.base_url
-            # Alter keywords and base URL if we are performing a container registry operation
-            kwargs, url_base, container = self._handle_container_operations(kwargs, url_base)
-            # Retrieve the endpoint URL from the command list and append to our base URL
-            target = f"{url_base}{uber_command[0][2]}"
-            # Container image ID
-            target = self._handle_container_image_id(target, kwargs)
-            # Partition
-            target = self._handle_partition(target, kwargs)
-            # Distinct field
-            target = self._handle_distinct_field(target, kwargs)
-            # Handle any IDs that are in the wrong payload
-            kwargs = self._handle_body_payload_ids(kwargs)
-            # Check for authentication
-            if self.authenticated:
-                # Which HTTP method to execute
-                selected_method = uber_command[0][1].upper()
-                selected_operation = uber_command[0][0]
-                # Only accept allowed HTTP methods
-                if selected_method in _ALLOWED_METHODS:
-                    returned = perform_request(method=selected_method,
-                                               endpoint=target,
-                                               body=kwargs.get("body", return_preferred_default(selected_operation)),
-                                               data=kwargs.get("data", return_preferred_default(selected_operation)),
-                                               params=args_to_params(kwargs.get("parameters", {}),
-                                                                     kwargs,
-                                                                     self.commands,
-                                                                     selected_operation
-                                                                     ),
-                                               headers=self._create_header_payload(kwargs),
-                                               files=kwargs.get("files",
-                                                                return_preferred_default(selected_operation, "list")
-                                                                ),
-                                               verify=self.ssl_verify,
-                                               proxy=self.proxy,
-                                               timeout=self.timeout,
-                                               user_agent=self.user_agent,
-                                               expand_result=kwargs.get("expand_result", False),
-                                               container=container
-                                               )
-                else:
-                    # Bad HTTP method
-                    returned = generate_error_result(message="Invalid HTTP method specified.",
-                                                     code=405
-                                                     )
+            if self.cred_format_valid:
+                if not token_value:
+                    token_value = self.token_value
+                operation, target_url, data_payload, header_payload = logout_payloads(
+                    creds=self.creds,
+                    base=self.base_url,
+                    token_val=token_value
+                    )
+                # Log the call to this operation if debugging is enabled.
+                if self.log:
+                    self.log.debug("OPERATION: %s", operation)
+                returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
+                                           headers=header_payload, verify=self.ssl_verify,
+                                           proxy=self.proxy, timeout=self.timeout,
+                                           user_agent=self.user_agent, log_util=self.log,
+                                           sanitize=self.sanitize_log
+                                           )
+                if stateful:
+                    self._token: BearerToken = BearerToken()
             else:
-                # Invalid token / Bad creds
-                returned = generate_error_result(message="Failed to issue token.",
-                                                 code=401,
-                                                 headers=self._token_fail_headers
-                                                 )
-        else:
-            # That command doesn't exist, have a cup of tea instead
-            returned = generate_error_result(message="Invalid API operation specified.", code=418)
+                raise InvalidCredentials
+        except InvalidCredentials as bad_creds:
+            returned = bad_creds.result
+            if self.log:
+                self.log.error(bad_creds.message)
 
         return returned
+
+    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
+    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
+    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
+    #
+    # These properties are present in all FalconInterface derivatives.
+    @property
+    def creds(self) -> Dict[str, str]:
+        """Return the current credential dictionary."""
+        return self._creds
+
+    @creds.setter
+    def creds(self, value: Dict[str, str]):
+        self._creds = value
+
+    @property
+    def config(self) -> InterfaceConfiguration:
+        """Return the interface configuration object for this interface."""
+        return self._config
+
+    @config.setter
+    def config(self, value: InterfaceConfiguration):
+        if not isinstance(value, InterfaceConfiguration):
+            raise ValueError
+        self._config = value
+
+    @property
+    def base_url(self) -> str:
+        """Return the base URL for this interface from the configuration object."""
+        return self._config.base_url
+
+    @base_url.setter
+    def base_url(self, value):
+        self._config.base_url = value
+
+    @property
+    def ssl_verify(self) -> bool:
+        """Return the SSL verification setting from the configuration object."""
+        return self._config.ssl_verify
+
+    @ssl_verify.setter
+    def ssl_verify(self, value: bool):
+        self._config.ssl_verify = value
+
+    @property
+    def proxy(self) -> Dict[str, str]:
+        """Return the current proxy setting."""
+        return self._config.proxy
+
+    @proxy.setter
+    def proxy(self, value: Dict[str, str]):
+        self._config.proxy = value
+
+    @property
+    def user_agent(self) -> str:
+        """Return the current user agent setting."""
+        return self._config.user_agent
+
+    @user_agent.setter
+    def user_agent(self, value: str):
+        self._config.user_agent = value
+
+    @property
+    def timeout(self) -> Union[int, tuple]:
+        """Return the current timeout setting."""
+        return self._config.timeout
+
+    @timeout.setter
+    def timeout(self, value: Union[int, tuple]):
+        self._config.timeout = value
+
+    @property
+    def debug_record_count(self) -> int:
+        """Return the current debug record count setting."""
+        return self.log_facility.debug_record_count
+
+    @debug_record_count.setter
+    def debug_record_count(self, value: int):
+        self.log_facility.debug_record_count = value
+
+    @property
+    def sanitize_log(self) -> bool:
+        """Return the current log sanitization."""
+        return self.log_facility.sanitize_log
+
+    @sanitize_log.setter
+    def sanitize_log(self, value):
+        self.log_facility.sanitize_log = value
+
+    # These properties provide reflection into the token object
+    @property
+    def bearer_token(self) -> BearerToken:
+        """Return the bearer token object for this configuration."""
+        return self._token
+
+    @property
+    def renew_window(self) -> int:
+        """Return the current token renew window setting."""
+        return self.bearer_token.renew_window
+
+    @renew_window.setter
+    def renew_window(self, value: int):
+        self.bearer_token.renew_window = value
+
+    @property
+    def token_expiration(self) -> int:
+        """Return the current expiration setting."""
+        return self.bearer_token.expiration
+
+    @token_expiration.setter
+    def token_expiration(self, value: int):
+        self.bearer_token.expiration = value
+
+    @property
+    def token_time(self) -> float:
+        """Return the current token_time setting."""
+        return self.bearer_token.token_time
+
+    @token_time.setter
+    def token_time(self, value: float):
+        self.bearer_token.token_time = value
+
+    @property
+    def token_fail_reason(self) -> str:
+        """Return the current fail_reason setting."""
+        return self.bearer_token.fail_reason
+
+    @token_fail_reason.setter
+    def token_fail_reason(self, value: str):
+        self.bearer_token.fail_reason = value
+
+    @property
+    def token_status(self) -> int:
+        """Return the current status setting."""
+        return self.bearer_token.status
+
+    @token_status.setter
+    def token_status(self, value: int):
+        self.bearer_token.status = value
+
+    @property
+    def token_value(self) -> str:
+        """Return the current value setting."""
+        return self.bearer_token.value
+
+    @token_value.setter
+    def token_value(self, value: str):
+        self.bearer_token.value = value
+
+    # All properties defined here are by design IMMUTABLE.
+    @property
+    def refreshable(self) -> bool:
+        """Return a boolean if this interface can automatically refresh tokens when they expire."""
+        return self.cred_format_valid
+
+    @property
+    def token_expired(self) -> bool:
+        """Return whether the token is ready to be renewed."""
+        return (time.time() - self.token_time) >= (self.token_expiration - self.renew_window)
+
+    @property
+    def authenticated(self) -> bool:
+        """Return if we are authenticated by retrieving the inverse of token_expired."""
+        return not self.token_expired
+
+    @property
+    def cred_format_valid(self) -> bool:
+        """Return a boolean that the creds dictionary is valid."""
+        return bool("client_id" in self.creds and "client_secret" in self.creds)
+
+    @property
+    def log(self) -> Logger:
+        """Return the logger from our log facility."""
+        return self.log_facility.log
+
+    @property
+    def log_facility(self) -> LogFacility:
+        """Return the entire log facility."""
+        return self._log
+
+    # The default functionality of a FalconInterface object performs a token refresh
+    # whenever a request is made for the auth_headers property and the token is stale.
+    @property
+    def auth_headers(self) -> Dict[str, str]:
+        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
+        if self.token_expired and self.refreshable:
+            self.login()
+
+        return {"Authorization": f"Bearer {self.token_value}"}
+
+    @property
+    def debug(self) -> bool:
+        """Return a boolean if we are in a debug mode."""
+        return bool(self.log)
+
+    @property
+    def pythonic(self) -> bool:
+        """Return a boolean if we are in a pythonic mode."""
+        return self._pythonic
+
+    @pythonic.setter
+    def pythonic(self, value: bool):
+        """Enable or disable pythonic mode."""
+        self._pythonic = value
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/cloud_connect_aws.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/cloud_connect_aws.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import aws_registration_payload
 from ._service_class import ServiceClass
 from ._endpoint._cloud_connect_aws import _cloud_connect_aws_endpoints as Endpoints
 
 
 class CloudConnectAWS(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_aws_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_aws_accounts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for provisioned AWS Accounts by providing an FQL filter and paging details.
 
         Returns a set of AWS accounts which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum records to return. [1-500]. Defaults to 100.
@@ -82,15 +83,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="QueryAWSAccounts",
             keywords=kwargs,
             params=parameters
             )
 
-    def get_aws_settings(self: object) -> dict:
+    def get_aws_settings(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts.
 
         This method does not accept arguments or keywords.
 
         Returns: dict object containing API response.
 
         HTTP Method: GET
@@ -101,15 +102,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetAWSSettings"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of AWS Accounts by specifying their IDs.
 
         Keyword arguments:
         ids -- List of AWS Account IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -127,15 +128,15 @@
             endpoints=Endpoints,
             operation_id="GetAWSAccounts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def provision_aws_accounts(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
+    def provision_aws_accounts(self: object, body: dict, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provision AWS Accounts by specifying details about the accounts to provision.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
                 {
                     "resources": [
                             {
@@ -178,15 +179,15 @@
             operation_id="ProvisionAWSAccounts",
             keywords=kwargs,
             params=parameters,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of AWS Accounts by specifying their IDs.
 
         Keyword arguments:
         ids -- List of AWS Account IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -204,15 +205,15 @@
             endpoints=Endpoints,
             operation_id="DeleteAWSAccounts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_aws_accounts(self: object, body: dict = None, **kwargs) -> dict:
+    def update_aws_accounts(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update AWS Accounts by specifying the ID of the account and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
                 {
                     "resources": [
                             {
@@ -250,15 +251,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateAWSAccounts",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_or_update_aws_settings(self: object, body: dict = None, **kwargs) -> dict:
+    def create_or_update_aws_settings(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create or update Global Settings which are applicable to all provisioned AWS accounts.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
                 {
                     "resources": [
                         {
@@ -291,15 +292,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict"])
     def verify_aws_account_access(self: object,
                                   *args,
                                   body: dict = None,
                                   parameters: dict = None,
                                   **kwargs
-                                  ) -> dict:
+                                  ) -> Dict[str, Union[int, dict]]:
         """Perform an Access Verification check on the specified AWS Account IDs.
 
         Keyword arguments:
         body -- full body payload, ignored by API.
         ids -- List of AWS Account IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -319,15 +320,15 @@
             operation_id="VerifyAWSAccountAccess",
             keywords=kwargs,
             body=body,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_aws_accounts_for_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_aws_accounts_for_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for provisioned AWS Accounts by providing an FQL filter and paging details.
 
         Returns a set of AWS account IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum records to return. [1-500]. Defaults to 100.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/cspm_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/cspm_registration.py`

 * *Files 3% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=R0904  # Matching API operation counts
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import cspm_registration_payload, cspm_policy_payload, cspm_scan_payload
 from ._service_class import ServiceClass
 from ._endpoint._cspm_registration import _cspm_registration_endpoints as Endpoints
 
 
 class CSPMRegistration(ServiceClass):
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about the current status of an AWS account.
 
         Keyword arguments:
         scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts
         ids -- AWS account IDs. String or list of strings.
         organization_ids -- AWS organization IDs. String or list of strings.
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
@@ -91,15 +92,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMAwsAccount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_aws_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_aws_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Register a new AWS account.
 
         Creates a new account in our system for a customer and generates a script
         to run in their AWS cloud environment to grant CrowdStrike Horizon access.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
@@ -132,15 +133,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateCSPMAwsAccount",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
+    def delete_aws_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an existing AWS Account or Organization by specifying their IDs.
 
         Keyword arguments:
         ids -- AWS Account IDs to remove. String or list of strings.
         organization_ids -- AWS Organization IDs to be removed. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -161,15 +162,15 @@
             endpoints=Endpoints,
             operation_id="DeleteCSPMAwsAccount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_aws_account(self: object, body: dict = None, **kwargs) -> dict:
+    def update_aws_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Patches a existing account in our system for a customer.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "resources": [
                         {
@@ -196,15 +197,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PatchCSPMAwsAccount",
             body=body
             )
 
-    def get_aws_console_setup_urls(self: object) -> dict:
+    def get_aws_console_setup_urls(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve setup URLs for the AWS console.
 
         Returns a URL for customers to visit in their cloud environment
         to grant access to CrowdStrike.
 
         This method does not accept arguments or keywords.
 
@@ -217,15 +218,15 @@
         """
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMAwsConsoleSetupURLs"
             )
 
-    def get_aws_account_scripts_attachment(self: object) -> dict:
+    def get_aws_account_scripts_attachment(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve AWS account scripts.
 
         Return a script for customers to run in their cloud environment
         to grant access to CrowdStrike for their AWS environment.
 
         This method does not accept arguments or keywords.
 
@@ -239,15 +240,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMAwsAccountScriptsAttachment"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about Azure account registration.
 
         Keyword arguments:
         scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts
         ids -- Azure account IDs. String or list of strings.
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Defaults to 100.
@@ -273,15 +274,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMAzureAccount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_azure_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_azure_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Register new Azure account.
 
         Creates a new account in our system for a customer and generates a script
         to run in their cloud environment to grant CrowdStrike Horizon access.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
@@ -312,15 +313,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateCSPMAzureAccount",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an existing Azure Subscription by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Azure Subscription IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -342,15 +343,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def update_azure_account_client_id(self: object,
                                        body: dict = None,
                                        parameters: dict = None,
                                        **kwargs
-                                       ) -> dict:
+                                       ) -> Dict[str, Union[int, dict]]:
         """Update Azure account Client ID.
 
         Update an Azure service account in our system with the
         user-created client_id created with the public key we've provided.
 
         Keyword arguments:
         body -- There are no body payload parameters. This field is not used. Ignore.
@@ -381,15 +382,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def update_azure_tenant_default_subscription_id(self: object,
                                                     body: dict = None,
                                                     parameters: dict = None,
                                                     **kwargs
-                                                    ) -> dict:
+                                                    ) -> Dict[str, Union[int, dict]]:
         """Update default subscription ID.
 
         Update an Azure service account in our system with the
         user-created client_id created with the public key we've provided.
 
         Keyword arguments:
         body -- There are no body payload parameters. This field is not used. Ignore.
@@ -422,15 +423,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def azure_download_certificate(self: object,
                                    *args,
                                    parameters: dict = None,
                                    **kwargs
-                                   ) -> dict:
+                                   ) -> Dict[str, Union[int, dict]]:
         """Retrieve Azure certificate.
 
         Returns JSON object(s) that contain the base64 encoded certificate for a service principal.
 
         Keyword arguments:
         tenant_id -- Azure Tenant ID to generate script for.
                      Defaults to the most recently registered tenant.
@@ -456,15 +457,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_azure_user_scripts_attachment(self: object,
                                           *args,
                                           parameters: dict = None,
                                           **kwargs
-                                          ) -> dict:
+                                          ) -> Dict[str, Union[int, dict]]:
         """
         Retrieve Azure user script.
 
         Return a script for customers to run in their cloud environment
         to grant access to CrowdStrike for their Azure environment.
 
         Keyword arguments:
@@ -490,15 +491,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMAzureUserScriptsAttachment",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "tenant-id")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_behavior_detections(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_behavior_detections(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve list of detected behaviors.
 
         Keyword arguments:
         account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
         aws_account_id -- AWS account ID. String.
         azure_subscription_id -- Azure subscription ID. String.
         azure_tenant_id -- Azure tenant ID. String.
@@ -555,15 +556,15 @@
             endpoints=Endpoints,
             operation_id="GetBehaviorDetections",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_configuration_detections(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_configuration_detections(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve list of active misconfigurations.
 
         Keyword arguments:
         account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
         aws_account_id -- AWS account ID. String.
         azure_subscription_id -- Azure subscription ID. String.
         azure_tenant_id -- Azure tenant ID. String.
@@ -619,15 +620,15 @@
             endpoints=Endpoints,
             operation_id="GetConfigurationDetections",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_ioa_events(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_ioa_events(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """For CSPM IOA events, gets list of IOA events.
 
         Keyword arguments:
         policy_id -- Policy ID. String.
         cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
         account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
         aws_account_id -- AWS account ID. String.
@@ -655,15 +656,15 @@
             endpoints=Endpoints,
             operation_id="GetIOAEvents",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_ioa_users(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_ioa_users(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """For CSPM IOA users, gets list of IOA users.
 
         Keyword arguments:
         policy_id -- Policy ID. String.
         cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
         account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
         aws_account_id -- AWS account ID. String.
@@ -686,15 +687,15 @@
             endpoints=Endpoints,
             operation_id="GetIOAUsers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policy(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policy(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Given a policy ID, returns detailed policy information.
 
         Keyword arguments:
         ids -- Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -712,15 +713,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMPolicy",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policy_settings(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_policy_settings(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about current policy settings.
 
         Keyword arguments:
         policy_id -- Policy ID. String.
         cloud_platform -- Cloud platform. Allowed values: `azure`, `aws`, `gcp`. String.
         service -- Service type to filter policy settings by.
                    Available values:
@@ -768,15 +769,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMPolicySettings",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policy_settings(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policy_settings(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update a policy setting.
 
         Can be used to override policy severity or to disable a policy entirely.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
@@ -816,15 +817,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateCSPMPolicySettings",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_scan_schedule(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_scan_schedule(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return scan schedule configuration for one or more cloud platforms.
 
         Keyword arguments:
         cloud_platform -- Cloud Platform. String. Allowed Values: `azure`, `aws`, `gcp`
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -845,15 +846,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMScanSchedule",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cloud-platform")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_scan_schedule(self: object, body: dict = None, **kwargs) -> dict:
+    def update_scan_schedule(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update scan schedule configuration for one or more cloud platforms.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "resources": [
                         {
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/custom_ioa.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/custom_ioa.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import ioa_custom_payload, generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._custom_ioa import _custom_ioa_endpoints as Endpoints
 
 
 class CustomIOA(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_patterns(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_patterns(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get pattern severities by ID.
 
         Keyword arguments:
         ids -- Pattern IDs. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -77,15 +78,15 @@
             endpoints=Endpoints,
             operation_id="get_patterns",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get platforms by ID.
 
         Keyword arguments:
         ids -- Platform IDs. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -103,15 +104,15 @@
             endpoints=Endpoints,
             operation_id="get_platformsMixin0",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rule groups by ID.
 
         Keyword arguments:
         ids -- Rule group IDs. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -133,15 +134,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def create_rule_group(self: object,
                           body: dict = None,
                           cs_username: str = None,  # pylint: disable=W0613  # deprecated
                           **kwargs
-                          ) -> dict:
+                          ) -> Dict[str, Union[int, dict]]:
         """Create a rule group for a platform with a name and an optional description.
 
         Returns the rule group.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
         comment -- Comment for the rule group. String.
@@ -170,15 +171,15 @@
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def delete_rule_groups(self: object,
                            *args,
                            cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                            parameters: dict = None,
                            **kwargs
-                           ) -> dict:
+                           ) -> Dict[str, Union[int, dict]]:
         """Delete rule groups by ID.
 
         Keyword arguments:
         comment -- Explains why the rule group is being deleted. String.
         ids -- Rule group IDs to be deleted. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
 
@@ -201,15 +202,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def update_rule_group(self: object,
                           body: dict = None,
                           cs_username: str = None,  # pylint: disable=W0613  # deprecated
                           **kwargs
-                          ) -> dict:
+                          ) -> Dict[str, Union[int, dict]]:
         """Update a rule group.
 
         The following properties can be modified: `name`, `description`, `enabled`.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
                 {
@@ -243,15 +244,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="update_rule_groupMixin0",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rule_types(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rule_types(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rule types by ID.
 
         Keyword arguments:
         ids -- Rule type IDs. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -269,15 +270,15 @@
             endpoints=Endpoints,
             operation_id="get_rule_types",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_rules_get(self: object, body: dict = None, **kwargs) -> dict:
+    def get_rules_get(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rules by ID and optionally version in the following format: ID[:version].
 
         Keyword arguments:
         body -- full body payload in JSON format, not required if using `ids` keyword is used.
         ids -- Rule IDs to retrieve. String or list of strings.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -297,15 +298,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="get_rules_get",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rules by ID and optionally version in the following format: ID[:version].
 
         The max number of IDs is constrained by URL size.
 
         Keyword arguments:
         ids -- Rule IDs. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
@@ -329,15 +330,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def create_rule(self: object,
                     body: dict = None,
                     cs_username: str = None,  # pylint: disable=W0613  # deprecated
                     **kwargs
-                    ) -> dict:
+                    ) -> Dict[str, Union[int, dict]]:
         """Create a rule within a rule group. Returns the rule.
 
         Keyword arguments:
         body -- full body payload in JSON format, not required if using other keywords.
                 {
                     "comment": "string",
                     "description": "string",
@@ -404,15 +405,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def delete_rules(self: object,
                      cs_username: str = None,  # pylint: disable=W0613  # deprecated
                      parameters: dict = None,
                      **kwargs
-                     ) -> dict:
+                     ) -> Dict[str, Union[int, dict]]:
         """Delete rules from a rule group by ID.
 
         Keyword arguments:
         comment -- Explains why the entity is being deleted. String.
         ids -- Rule IDs to be deleted. String or list of strings.
         parameters -- full parameters payload, not required if using `ids` keyword.
         rule_group_id -- The parent rule group. String.
@@ -435,15 +436,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def update_rules(self: object,
                      body: dict = None,
                      cs_username: str = None,  # pylint: disable=W0613  # deprecated
                      **kwargs
-                     ) -> dict:
+                     ) -> Dict[str, Union[int, dict]]:
         """Update rules within a rule group. Return the updated rules.
 
         Keyword arguments:
         body -- full body payload in JSON format, not required if using other keywords.
                 {
                     "comment": "string",
                     "rule_updates": [
@@ -522,15 +523,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="update_rules",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def validate(self: object, body: dict = None, **kwargs) -> dict:
+    def validate(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Validate field values and check for matches if a test string is provided.
 
         Keyword arguments:
         body -- full body payload in JSON format, not required if using other keywords.
                 {
                     "fields": [
                         {
@@ -576,15 +577,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="validate",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_patterns(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_patterns(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get all pattern severity IDs.
 
         Keyword arguments:
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
                   Use with the limit parameter to manage pagination of results.
@@ -604,15 +605,15 @@
             endpoints=Endpoints,
             operation_id="query_patterns",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_platforms(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get all platform IDs.
 
         Keyword arguments:
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
                   Use with the limit parameter to manage pagination of results.
@@ -632,15 +633,15 @@
             endpoints=Endpoints,
             operation_id="query_platformsMixin0",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rule_groups_full(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rule_groups_full(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all rule groups matching the query with optional filter.
 
         Keyword arguments:
         filter -- FQL query specifying the filter parameters. String.
                   Filter term criteria:
                   enabled                   rules.name
                   platform                  rules.description
@@ -678,15 +679,15 @@
             endpoints=Endpoints,
             operation_id="query_rule_groups_full",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all rule group IDs matching the query with optional filter.
 
         Keyword arguments:
         filter -- FQL query specifying the filter parameters. String.
                   Filter term criteria:
                   enabled                   rules.name
                   platform                  rules.description
@@ -724,15 +725,15 @@
             endpoints=Endpoints,
             operation_id="query_rule_groupsMixin0",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rule_types(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rule_types(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get all rule type IDs.
 
         Keyword arguments:
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
                   Use with the limit parameter to manage pagination of results.
@@ -752,15 +753,15 @@
             endpoints=Endpoints,
             operation_id="query_rule_types",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all rule IDs matching the query with optional filter.
 
         Keyword arguments:
         filter -- FQL query specifying the filter parameters. String.
                   Filter term criteria:
                   enabled                   rules.name
                   platform                  rules.description
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/d4c_registration.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/d4c_registration.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import azure_registration_payload, aws_d4c_registration_payload
 from ._service_class import ServiceClass
 from ._endpoint._d4c_registration import _d4c_registration_endpoints as Endpoints
 
 
 class D4CRegistration(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about the current status of an AWS account.
 
         Keyword arguments:
         ids -- List of AWS Account IDs to retrieve. String or list of strings.
         limit -- The maximum records to return. Defaults to 100. Integer.
         migrated -- Only return migrated D4C accounts. Boolean.
         offset -- The offset to start retrieving records from. Integer.
@@ -86,15 +87,15 @@
             endpoints=Endpoints,
             operation_id="GetD4CAwsAccount",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_aws_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_aws_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Register a new AWS account.
 
         Creates a new account in our system for a customer and generates a
         script for them to run in their AWS cloud environment to grant us access.
 
         Keyword arguments:
         account_id -- AWS account ID. String.
@@ -131,15 +132,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateD4CAwsAccount",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an existing AWS account or organization from the tenant.
 
         Keyword arguments:
         ids -- List of AWS Account IDs to retrieve. String or list of strings.
         organization_ids -- List of AWS Organization IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -158,15 +159,15 @@
             endpoints=Endpoints,
             operation_id="DeleteD4CAwsAccount",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_console_setup(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_console_setup(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return a URL for customer to visit in their cloud environment to grant CrowdStrike access.
 
         Keyword arguments:
         region -- AWS region to generate the URL for. String.
         parameters -- full parameters payload, not required if region is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'region'.
@@ -184,15 +185,15 @@
             endpoints=Endpoints,
             operation_id="GetD4CAwsConsoleSetupURLs",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "region")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_account_scripts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_account_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return a script for customer to run in their cloud environment to grant CrowdStrike access.
 
         Keyword arguments:
         ids -- List of AWS Account IDs to retrieve the script for. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -210,15 +211,15 @@
             endpoints=Endpoints,
             operation_id="GetD4CAWSAccountScriptsAttachment",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about Azure account registration.
 
         Keyword arguments:
         ids -- List of Azure Account IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
         scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts.
 
@@ -240,15 +241,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMAzureAccount",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_azure_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_azure_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Register a new Azure account.
 
         Creates a new account in our system for a customer and generates a
         script for them to run in their cloud environment to grant us access.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
@@ -283,15 +284,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def update_azure_account_client_id(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs
-                                       ) -> dict:
+                                       ) -> Dict[str, Union[int, dict]]:
         """Update Azure account client ID.
 
         Update an Azure service account in our system by with the
         user-created client_id created with the public key we've provided.
 
         Keyword arguments:
         id -- ClientID to use for the Service Principal associated
@@ -312,15 +313,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateCSPMAzureAccountClientID",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "id")
             )
 
-    def get_azure_user_scripts_attachment(self: object) -> dict:
+    def get_azure_user_scripts_attachment(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve Azure user script attachment.
 
         Return a script for customer to run in their cloud environment to
         grant us access to their Azure environment as a downloadable attachment.
 
         This method does not accept arguments or keywords.
 
@@ -333,15 +334,15 @@
         """
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMAzureUserScriptsAttachment"
             )
 
-    def get_azure_user_scripts(self: object) -> dict:
+    def get_azure_user_scripts(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve Azure user script.
 
         Return a script for customer to run in their cloud
         environment to grant us access to their Azure environment.
 
         This method does not accept arguments or keywords.
 
@@ -355,15 +356,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMAzureUserScripts"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return information about the current status of an GCP account.
 
         Keyword arguments:
         ids -- List of Response Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
         scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts.
 
@@ -382,15 +383,15 @@
             endpoints=Endpoints,
             operation_id="GetCSPMCGPAccount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_gcp_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_gcp_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Register new GCP account.
 
         Creates a new account in our system for a customer and generates a new service
         account for them to add access to in their GCP environment to grant us access.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
@@ -421,15 +422,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateCSPMGCPAccount",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def azure_download_certificate(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def azure_download_certificate(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Download Azure Certificate.
 
         Returns JSON object(s) that contain the base64 encoded certificate for a service principal.
 
         Keyword arguments:
         tenant_id -- Azure Tenant ID to generate script for.
                      Defaults to the most recently registered tenant.
@@ -450,15 +451,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="DiscoverCloudAzureDownloadCertificate",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "tenant_id")
             )
 
-    def get_gcp_user_scripts_attachment(self: object) -> dict:
+    def get_gcp_user_scripts_attachment(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve GCP user script attachment.
 
         Return a script for customer to run in their cloud environment to
         grant us access to their GCP environment as a downloadable attachment.
 
         This method does not accept arguments or keywords.
 
@@ -471,15 +472,15 @@
         """
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMGCPUserScriptsAttachment"
             )
 
-    def get_gcp_user_scripts(self: object) -> dict:
+    def get_gcp_user_scripts(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve GCP user script.
 
         Return a script for customer to run in their cloud
         environment to grant us access to their GCP environment.
 
         This method does not accept arguments or keywords.
 
@@ -493,15 +494,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCSPMGCPUserScripts"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_horizon_scripts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_horizon_scripts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return a script for customer to run in their cloud environment to grant CrowdStrike access.
 
         Keyword arguments:
         account_type -- Account type (commercial, gov). Only applicable when registering AWS
                         commercial accounts in a Gov environment. String.
         delete -- Generate a delete script. Boolean.
         organization_id -- AWS organization ID. String.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/debug.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/debug.py`

 * *Files 23% similar despite different names*

```diff
@@ -35,16 +35,17 @@
 
 For more information, please refer to <https://unlicense.org>
 """
 import os
 import sys
 import importlib
 import atexit
-from os.path import dirname, join
-import glob
+from logging import Logger, basicConfig, getLogger, DEBUG
+# from os.path import dirname, join
+# import glob
 from . import oauth2 as FalconAuth
 
 
 def help(item=None):  # pylint: disable=W0622
     """Debugger help function. Overrides the built in python function."""
     text = """
     This is an interactive Python shell. Python help is available under python_help().
@@ -53,28 +54,27 @@
     If you have FALCON_CLIENT_ID and FALCON_CLIENT_SECRET environment variables set,
     this shell will authenticate you at start up. You can also call the init()
     function passing the values dbg_falcon_client_id and dbg_falcon_client_secret, or
     you can pass a credential dictionary containing them.
 
     AVAILABLE VARIABLES
         'DEBUG_TOKEN' - your OAuth2 token.
-        'AUTH_OBJECT' - an instance of the OAuth2 authorization class (authenticated).
+        'AUTH' - an instance of the OAuth2 authorization object (authenticated).
 
-    LISTING AVAILABLE SERVICE CLASSES
-    Use list_modules() to retrieve a list of all available service classes.
+    LISTING AVAILABLE CLASSES
+    Use list_modules() to retrieve a list of all available classes.
 
-    IMPORTING MODULES
-    Use import_module("MODULE_NAME") to import any of the available service classes.
+    ALL CLASSES ARE IMPORTED AND AVAILABLE FOR TESTING.
 
-    Import hosts module and query for a specific host:
-    In [1]: hosts = import_module("hosts")
-    In [2]: hosts.QueryDevicesByFilter(filter="hostname:'whatever'")
+    Create an instance of the Hosts Service Class and query for devices:
+    In [1]: hosts = Hosts(auth_object=AUTH)
+    In [2]: hosts.query_devices_by_filter_scroll(filter="hostname:'whatever'")
 
-    Importing the detects module and querying for all available detections with one command:
-    In [1]: import_module("detects").QueryDetects()
+    Using the Detects Service Class to query for all available detections with one command:
+    In [1]: Detects(auth_object=AUTH).query_detects()
 
     EXIT THE DEBUGGER
     Use exit / quit / CTRL-D to exit the debugger.
     """
     if item is None:
         print(text)
     elif callable(getattr(item, 'help', None)):
@@ -87,37 +87,80 @@
     """Embed the IPython interactive shell."""
     _ = importlib.import_module("IPython.terminal.embed")
     ipshell = _.InteractiveShellEmbed(banner1=BANNER)
     ipshell.confirm_exit = False
     ipshell()
 
 
+def setup_logging() -> Logger:
+    """Configure simple logging."""
+    log_util = getLogger("log_testing")
+    basicConfig(level=DEBUG, format="%(asctime)s %(levelname)-8s %(name)s %(funcName)s %(message)s")
+
+    return log_util
+
+
 def list_modules():
     """List all available Service Classes."""
-    modules = glob.glob(join(dirname(__file__), "*.py"))
-    result = []
-    for key in modules:
-        branched = key.split("/")
-        position = len(branched)-1
-        module_name = branched[position].replace(".py", "")
-        if "_" not in module_name[0] and module_name not in ["debug", "api_complete"]:
-            result.append(module_name)
+    # modules = glob.glob(join(dirname(__file__), "*.py"))
+    # Only importing within this method to load the classes for the debugger not-package code.
+    # pylint: disable=C0415,E0401
+    import src.falconpy
+    result = [x for x in dir(src.falconpy) if ("_" not in x and not x.islower())]
+    # result = []
+    # for key in modules:
+    #     branched = key.split("/")
+    #     position = len(branched)-1
+    #     module_name = branched[position].replace(".py", "")
+    #     if "_" not in module_name[0] and module_name not in ["debug", "api_complete"]:
+    #         result.append(module_name)
     result.sort()
-    print("Available modules")
+    print("\nAvailable FalconPy classes")
+    print(f"{'=' * 65}")
     msg = ""
     for idx, val in enumerate(result):
         msg = f"{msg}%-35s" % val
         cnt = idx + 1
         if cnt % 2 == 0:
             print(msg)
             msg = ""
     print(msg)
     print("\nLoad modules with import_module('MODULE_NAME')")
 
 
+def import_all():
+    """Inspect the package folder and import all available classes from all modules."""
+    # Only importing within this method to load the classes for the debugger not-package code.
+    # pylint: disable=C0415,E0401,R1702
+    try:
+        import src.falconpy as sdk
+    except ImportError:
+        # We're running via the package prolly
+        import falconpy as sdk
+    import inspect
+    loaded = []
+    for name, obj in inspect.getmembers(sdk, inspect.isclass):
+        # This is uh... interesting.
+        mod_name = f"{obj}".replace("<class", "").replace(">", "").replace("'", "").strip().replace(f".{name}", "")
+        if "enum" not in mod_name:
+            try:
+                module = importlib.import_module(mod_name)
+                for attribute_name in [x for x in dir(module) if "__" not in x]:
+                    attribute = getattr(module, attribute_name)
+                    if inspect.isclass(attribute):
+                        if attribute_name not in loaded:
+                            globals()[attribute_name] = attribute
+                            log.debug("Loaded %s class", attribute_name)
+                            loaded.append(attribute_name)
+
+            except ImportError:
+                # Probably one of the aliases
+                log.debug("Skipped %s alias", name)
+
+
 def import_module(module: str = None):
     """Dynamically imports the module requested and returns an authenticated instance of the Service Class."""
     returned_object = False
     found = False
     if module:
         module = module.lower()
         import_location = "src.falconpy"
@@ -134,36 +177,36 @@
             except ImportError:
                 print("Unable to import requested service class")
         if found:
             current_module = sys.modules[f"{import_location}.{module}"]
             for key in dir(current_module):
                 if isinstance(getattr(current_module, key), type) and not key == "ServiceClass" and "_" not in key:
                     _.append(getattr(_[0], key))
-                    returned_object = _[1](auth_object=AUTH_OBJECT)
+                    returned_object = _[1](auth_object=AUTH)
                     print(f"Service Class {key} imported successfully.")
     else:
         print("No module specified.")
 
     return returned_object
 
 
 def exit_handler():
     """Revoke the DEBUG_TOKEN and gracefully quit the debugger. Overrides the built in python function."""
-    if AUTH_OBJECT:
+    if AUTH:
         print("Discarding token")
-        AUTH_OBJECT.revoke(token=DEBUG_TOKEN)
+        AUTH.revoke(token=DEBUG_TOKEN)
     sys.exit(0)
 
 
 def startup(dbg_falcon_client_id: str, dbg_falcon_client_secret: str):
     """Authenticate using the credentials provided and return the token / authentication object."""
-    auth_object = FalconAuth.OAuth2(creds={
-        'client_id': dbg_falcon_client_id,
-        'client_secret': dbg_falcon_client_secret
-    })
+    auth_object = FalconAuth.OAuth2(client_id=dbg_falcon_client_id,
+                                    client_secret=dbg_falcon_client_secret,
+                                    debug=True
+                                    )
 
     try:
         debug_token = auth_object.token()["body"]["access_token"]
     except KeyError:
         debug_token = False
         auth_object = False
 
@@ -176,45 +219,70 @@
         dbg_falcon_client_id = creds["falcon_client_id"]
         dbg_falcon_client_secret = creds["falcon_client_secret"]
 
     if "FALCON_CLIENT_ID" in os.environ and "FALCON_CLIENT_SECRET" in os.environ:
         dbg_falcon_client_id = os.environ["FALCON_CLIENT_ID"]
         dbg_falcon_client_secret = os.environ["FALCON_CLIENT_SECRET"]
 
-    global DEBUG_TOKEN, AUTH_OBJECT  # pylint: disable=W0603
-    DEBUG_TOKEN, AUTH_OBJECT = startup(dbg_falcon_client_id, dbg_falcon_client_secret)
+    global DEBUG_TOKEN, AUTH  # pylint: disable=W0603
+    DEBUG_TOKEN, AUTH = startup(dbg_falcon_client_id, dbg_falcon_client_secret)
     embed()
 
 
 # Move the internal python help() function to python_help()
 python_help = help
 
 # Configure our banner
-BANNER = """
+BANNER = r"""
 ,---.     |                   ,--.      |
 |__. ,---.|    ,---.,---.,---.|   |,---.|---..   .,---.
 |    ,---||    |    |   ||   ||   ||---'|   ||   ||   |
 `    `---^`---'`---'`---'`   '`--' `---'`---'`---'`---|
                                                   `---'
             CrowdStrike Python 3 Debug Interface
 
-This shell-like interface allows for quick learning,
-demoing, and prototyping of API operations using
-the CrowdStrike FalconPy SDK and Python 3.
-
-Please type help() to learn more.
-                         |
-     _____________   __ -+- _____________
-     \\_____     /   /_ \\ |   \\     _____/
-       \\_____   \\____/  \\____/    _____/
-         \\_____    FalconPy      _____/
-           \\___________  ___________/
-                     /____\\
+This shell-like interface allows for quick demoing and prototyping
+of API operations using the CrowdStrike FalconPy SDK and Python 3.
+
+                             |
+         _____________   __ -+- _____________
+         \_____     /   /_ \ |   \     _____/
+           \_____   \____/  \____/    _____/
+             \_____    FalconPy      _____/
+               \___________  ___________/
+                         /____\
+
+           Please type help() to learn more.
 """
 
 # Default our debug token and auth object to False
 DEBUG_TOKEN = False
-AUTH_OBJECT = False
+AUTH = False
 
 atexit.register(exit_handler)
-
+log = setup_logging()
+import_all()
 init()
+
+#              .-.
+#             o   \     .-.
+#                .----.'   \
+#              .'o)  / `.   o
+#             /         |
+#             \_)       /-.
+#               '_.`    \  \
+#                `.      |  \
+#                 |       \ |
+#             .--/`-.     / /
+#           .'.-/`-. `.  .\|
+#          /.' /`._ `-    '-.
+#     ____(|__/`-..`-   '-._ \
+#    |`------.'-._ `      ||\ \
+#    || #   /-.   `   /   || \|
+#    ||   #/   `--'  /  /_::_|)__
+#    `|____|-._.-`  /  ||`--------`
+#          \-.___.` | / || #      |
+#           \       | | ||   #  # |
+#           /`.___.'\ |.`|________|
+#           | /`.__.'|'.`
+#         __/ \    __/ \
+#        /__.-.)  /__.-.) LGB
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/detects.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/detects.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request
 from ._payload import generic_payload_list, update_detects_payload
 from ._payload import aggregate_payload
 from ._service_class import ServiceClass
 from ._endpoint._detects import _detects_endpoints as Endpoints
 
 
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def get_aggregate_detects(self: object, body: list = None, **kwargs) -> dict:
+    def get_aggregate_detects(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get detect aggregates as specified via json in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "date_ranges": [
@@ -123,15 +124,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetAggregateDetects",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_detects_by_ids(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def update_detects_by_ids(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Modify the state, assignee, and visibility of detections.
 
         Keyword arguments:
         assigned_to_uuid -- A user ID to assign the detection to.
         body -- full body payload, not required when using other keywords.
                 {
                     "assigned_to_uuid": "string",
@@ -189,15 +190,15 @@
                     "show_in_ui": bool,
                     "status": str
                     } if self.validate_payloads else None,
             body_required=["ids"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_detect_summaries(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_detect_summaries(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """View information about detections.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "ids": [
                         "string"
@@ -227,15 +228,15 @@
             operation_id="GetDetectSummaries",
             body=body,
             body_validator={"ids": list} if self.validate_payloads else None,
             body_required=["ids"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_detects(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_detects(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for detection IDs that match a given query.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
 
                   AVAILABLE FILTERS
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/device_control_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/device_control_policies.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,17 +31,18 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import generate_error_result, force_default, args_to_params
 from ._util import process_service_request, handle_single_argument
-from ._payload import generic_payload_list, device_policy_payload
+from ._payload import generic_payload_list, device_policy_payload, default_device_policy_config_payload
 from ._service_class import ServiceClass
 from ._endpoint._device_control_policies import _device_control_policies_endpoints as Endpoints
 
 
 class DeviceControlPolicies(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
 
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for a Device Control Policy members and return full detail.
 
         Search for members of a Device Control Policy in your environment by
         providing an FQL filter and paging details. Returns a set of host details
         which match the filter criteria.
 
         Keyword arguments:
@@ -88,15 +89,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedDeviceControlPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for a Device Control Policies and return full detail.
 
         Search for Device Control Policies in your environment by providing an FQL filter and
         paging details. Returns a set of Device Control Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -125,16 +126,95 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="queryCombinedDeviceControlPolicies",
             keywords=kwargs,
             params=parameters
             )
 
+    def get_default_policies(self: object) -> dict:
+        """Retrieve the configuration for a Default Device Control Policy.
+
+        Keyword arguments:
+        This method does not accept keyword arguments.
+
+        Arguments: This method does not accept arguments.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: GET
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
+                    /device-control-policies/getDefaultDeviceControlPolicies
+        """
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="getDefaultDeviceControlPolicies"
+            )
+
+    @force_default(defaults=["body"], default_types=["dict"])
+    def update_default_policies(self: object, body: dict = None, **kwargs) -> dict:
+        """Update Device Control Policies by specifying the ID of the policy and details to update.
+
+        Keyword arguments:
+        blocked_notification -- dictionary containing the custom message and enablement status
+                                for the blocked notification. Dictionary.
+                                {
+                                    "custom_message": "string",
+                                    "use_custom": true
+                                }
+        blocked_custom_message -- Message to use for blocked notifications. Using this keyword will
+                                  automatically generate the necessary blocked_notification dictionary.
+                                  String.
+        body -- full body payload, not required if using other keywords.
+                {
+                    "custom_notifications": {
+                        "blocked_notification": {
+                            "custom_message": "string",
+                            "use_custom": true
+                        },
+                        "restricted_notification": {
+                            "custom_message": "string",
+                            "use_custom": true
+                        }
+                    }
+                }
+        restricted_custom_message -- message to use for restricted notifications. Using this keyword will
+                                  automatically generate the necessary restricted_notification dictionary.
+                                  String.
+        restricted_notification -- dictionary containing the custom message and enablement status
+                                   for the restricted notification. Dictionary.
+                                   {
+                                       "custom_message": "string",
+                                       "use_custom": true
+                                   }
+
+        This method only supports keywords for providing arguments.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: PATCH
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
+                    /device-control-policies/updateDefaultDeviceControlPolicies
+        """
+        if not body:
+            body = default_device_policy_config_payload(passed_keywords=kwargs)
+
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="updateDefaultDeviceControlPolicies",
+            body=body
+            )
+
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Perform a Device Control Policy action.
 
         Keyword arguments:
         action_name -- action to perform: 'add-host-group', 'disable', 'enable',
                        or 'remove-host-group'.
         action_parameters -- Action specific parameter options. List of dictionaries.
                              {
@@ -194,15 +274,15 @@
                             )
         else:
             returned = generate_error_result("Invalid value specified for action_name parameter.")
 
         return returned
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def set_precedence(self: object, body: dict = None, **kwargs) -> dict:
+    def set_precedence(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Set Device Control Policy precedence.
 
         Sets the precedence of Device Control Policies based on the order of IDs specified in
         the request. The first ID specified will have the highest precedence and the last ID
         specified will have the lowest. You must specify all non-Default Policies for a platform
         when updating precedence.
 
@@ -236,15 +316,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="setDeviceControlPoliciesPrecedence",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Device Control Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Device Control Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -263,15 +343,15 @@
             endpoints=Endpoints,
             operation_id="getDeviceControlPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def create_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Device Control Policies by specifying details about the policy to create.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                 "resources": [
                     {
@@ -333,15 +413,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createDeviceControlPolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Device Control Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Device Control Policy IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -360,15 +440,15 @@
             endpoints=Endpoints,
             operation_id="deleteDeviceControlPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Device Control Policies by specifying the ID of the policy and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                 "resources": [
                     {
@@ -429,15 +509,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateDeviceControlPolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for a Device Control Policy members and return their IDs.
 
         Search for members of a Device Control Policy in your environment by providing
         an FQL filter and paging details. Returns a set of Agent IDs which match the filter
         criteria.
 
         Keyword arguments:
@@ -465,15 +545,15 @@
             endpoints=Endpoints,
             operation_id="queryDeviceControlPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for a Device Control Policies and return their IDs.
 
         Search for Device Control Policies in your environment by providing an
         FQL filter and paging details. Returns a set of Device Control Policy IDs
         which match the filter criteria.
 
         Keyword arguments:
@@ -508,14 +588,16 @@
             )
 
     # These method names align to the operation IDs in the API but
     # do not conform to snake_case / PEP8 and are defined here for
     # backwards compatibility / ease of use purposes
     queryCombinedDeviceControlPolicyMembers = query_combined_policy_members
     queryCombinedDeviceControlPolicies = query_combined_policies
+    getDefaultDeviceControlPolicies = get_default_policies
+    updateDefaultDeviceControlPolicies = update_default_policies
     performDeviceControlPoliciesAction = perform_action
     setDeviceControlPoliciesPrecedence = set_precedence
     getDeviceControlPolicies = get_policies
     createDeviceControlPolicies = create_policies
     deleteDeviceControlPolicies = delete_policies
     updateDeviceControlPolicies = update_policies
     queryDeviceControlPolicyMembers = query_policy_members
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/discover.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/discover.py`

 * *Files 12% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._service_class import ServiceClass
 from ._endpoint._discover import _discover_endpoints as Endpoints
 
 
 class Discover(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -50,15 +51,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_accounts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on accounts by providing one or more IDs.
 
         Find account IDs with `query_accounts`.
 
         Keyword arguments:
         ids -- One or more account IDs (max: 100). String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -78,15 +79,43 @@
             endpoints=Endpoints,
             operation_id="get_accounts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_hosts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_applications(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
+        """Get details on applications by providing one or more IDs.
+
+        Find application IDs with `query_applications`.
+
+        Keyword arguments:
+        ids -- One or more application IDs (max: 100). String or list of strings.
+        parameters - full parameters payload, not required if ids is provided as a keyword.
+
+        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
+                   All others are ignored.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: GET
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/get-applications
+        """
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="get_applications",
+            keywords=kwargs,
+            params=handle_single_argument(args, parameters, "ids")
+            )
+
+    @force_default(defaults=["parameters"], default_types=["dict"])
+    def get_hosts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on assets by providing one or more IDs.
 
         Find asset IDs with `query_hosts`.
 
         Keyword arguments:
         ids -- One or more asset IDs (max: 100). String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -106,15 +135,15 @@
             endpoints=Endpoints,
             operation_id="get_hosts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_logins(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_logins(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on logins by providing one or more IDs.
 
         Find login IDs with `query_logins`.
 
         Keyword arguments:
         ids -- One or more login IDs (max: 100). String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -134,15 +163,15 @@
             endpoints=Endpoints,
             operation_id="get_logins",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_accounts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for accounts in your environment.
 
         Supports providing a FQL (Falcon Query Language) filter and paging details.
         Returns a set of account IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -188,15 +217,50 @@
             endpoints=Endpoints,
             operation_id="query_accounts",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_hosts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_applications(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
+        """Search for applications in your environment.
+
+        Supports providing a FQL (Falcon Query Language) filter and paging details.
+        Returns a set of account IDs which match the filter criteria.
+
+        Keyword arguments:
+        filter -- The filter expression that should be used to limit the results. FQL syntax.
+        limit -- The number of account IDs to return in this response. (Max: 100, default: 100)
+                 Use with the offset parameter to manage pagination of results.
+        offset -- An offset used with the limit parameter to manage pagination of results.
+                  On your first request, don’t provide an offset. On subsequent requests,
+                  provide the offset from the previous response to continue from that place
+                  in the results.
+        parameters - full parameters payload, not required if using other keywords.
+        sort -- Sort assets by their properties. A single sort field is allowed.
+
+        This method only supports keywords for providing arguments.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: GET
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/query-applications
+        """
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="query_applications",
+            keywords=kwargs,
+            params=parameters
+            )
+
+    @force_default(defaults=["parameters"], default_types=["dict"])
+    def query_hosts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for assets in your environment.
 
         Supports providing a FQL (Falcon Query Language) filter and paging details.
         Returns a set of asset IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -249,15 +313,15 @@
             endpoints=Endpoints,
             operation_id="query_hosts",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_logins(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_logins(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for logins in your environment.
 
         Supports providing a FQL (Falcon Query Language) filter and paging details.
         Returns a set of asset IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/event_streams.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/event_streams.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request
 from ._service_class import ServiceClass
 from ._endpoint._event_streams import _event_streams_endpoints as Endpoints
 
 
 class EventStreams(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -55,15 +56,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def refresh_active_stream(self: object,
                               partition: int = 0,
                               parameters: dict = None,
                               body: dict = None,
                               **kwargs
-                              ) -> dict:
+                              ) -> Dict[str, Union[int, dict]]:
         """Refresh an active event stream.
 
         Use the URL shown in a listAvailableStreamsOAuth2 response.
 
         Keyword arguments:
         action_name -- Action to perform. Only allowed value is "refresh_active_stream_session".
         app_id -- Label that identifies your connection. Will also accept `appId`.
@@ -93,15 +94,15 @@
             body=body,  # Issue 247 - BODY is passed here even though it is empty
             keywords=kwargs,
             params=parameters,
             partition=partition
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_available_streams(self: object, parameters: dict = None, **kwargs) -> dict:
+    def list_available_streams(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Discover all event streams in your environment.
 
         Keyword arguments:
         app_id -- Label that identifies your connection. Will also accept `appId`.
                   32 character alphanumeric.
         format -- format for streaming events. Either 'json' or 'flatjson'.
         parameters -- full parameters payload, not required if using other keywords.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falcon_complete_dashboard.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falcon_complete_dashboard.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default
 from ._payload import aggregate_payload
 from ._service_class import ServiceClass
 from ._endpoint._falcon_complete_dashboard import _falcon_complete_dashboard_endpoints as Endpoints
 
 
 class CompleteDashboard(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_allow_list(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_allow_list(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate allowlist ticket values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -127,15 +128,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateAllowList",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_block_list(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_block_list(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate blocklist ticket values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -203,15 +204,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateBlockList",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_detections(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_detections(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate detection values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -279,15 +280,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateDetections",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_device_count_collection(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_device_count_collection(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate host/devices count based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -357,15 +358,15 @@
             endpoints=Endpoints,
             methods="POST",
             operation_id="AggregateDeviceCountCollection",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_escalations(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_escalations(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate escalation ticket values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -433,15 +434,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateEscalations",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_fc_incidents(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_fc_incidents(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate incident values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -509,15 +510,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateFCIncidents",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_remediations(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_remediations(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate remediation ticket values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -585,15 +586,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateRemediations",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_allow_list_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_allow_list_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -615,15 +616,15 @@
             endpoints=Endpoints,
             operation_id="QueryAllowListFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_block_list_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_block_list_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve block listtickets that match the provided filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -645,15 +646,15 @@
             endpoints=Endpoints,
             operation_id="QueryBlockListFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_detection_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_detection_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve DetectionsIds that match the provided FQL filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -676,15 +677,18 @@
             endpoints=Endpoints,
             operation_id="QueryDetectionIdsByFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_device_count_collection_queries_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_device_count_collection_queries_by_filter(self: object,
+                                                      parameters: dict = None,
+                                                      **kwargs
+                                                      ) -> Dict[str, Union[int, dict]]:
         """Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -707,15 +711,15 @@
             endpoints=Endpoints,
             operation_id="GetDeviceCountCollectionQueriesByFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_escalations_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_escalations_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve escalation tickets that match the provided filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -738,15 +742,15 @@
             endpoints=Endpoints,
             operation_id="QueryEscalationsFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_incident_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_incident_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve incidents that match the provided filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -769,15 +773,15 @@
             endpoints=Endpoints,
             operation_id="QueryIncidentIdsByFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_remediations_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_remediations_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve remediation tickets that match the provided filter criteria with scrolling enabled.
 
         Keyword arguments:
         filter -- Optional filter and sort criteria in the form of an FQL query. String.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falcon_container.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falcon_container.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default
 from ._payload import image_payload
 from ._service_class import ServiceClass
 from ._endpoint._falcon_container import _falcon_container_endpoints as Endpoints
 
 
 class FalconContainer(ServiceClass):
@@ -50,15 +51,15 @@
           "client_id": "CLIENT_ID_HERE",
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
-    def get_credentials(self: object) -> dict:
+    def get_credentials(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve the registry credentials.
 
         HTTP Method: GET
 
         Swagger URL
         ----
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container/GetCredentials
@@ -79,15 +80,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetCredentials"
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def read_image_vulnerabilities(self: object, body: dict = None, **kwargs) -> dict:
+    def read_image_vulnerabilities(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve an assessment report for an image by specifying repository and tag.
 
         HTTP Method: POST
 
         Swagger URL
         ----
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-cli/ReadImageVulnerabilities
@@ -133,15 +134,15 @@
             endpoints=Endpoints,
             operation_id="ReadImageVulnerabilities",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_assessment(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_assessment(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve an assessment report for an image by specifying repository and tag.
 
         HTTP Method: GET
 
         Swagger URL
         ----
         This operation does not exist in swagger.
@@ -166,15 +167,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetImageAssessmentReport",
             keywords=kwargs,
             params=parameters
             )
 
-    def delete_image_details(self: object, *args, image_id: str = None) -> dict:
+    def delete_image_details(self: object, *args, image_id: str = None) -> Dict[str, Union[int, dict]]:
         """Delete image details from the CrowdStrike registry.
 
         HTTP Method: DELETE
 
         Swagger URL
         ----
         This operation does not exist in swagger.
@@ -201,15 +202,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="DeleteImageDetails",
             image_id=image_id
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def image_matches_policy(self: object, parameters: dict = None, **kwargs) -> dict:
+    def image_matches_policy(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Check if an image matches a policy by specifying repository and tag.
 
         HTTP Method: GET
 
         Swagger URL
         ----
         This operation does not exist in swagger.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/falconx_sandbox.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/falconx_sandbox.py`

 * *Files 4% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import json
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list, falconx_payload
 from ._service_class import ServiceClass
 from ._endpoint._falconx_sandbox import _falconx_sandbox_endpoints as Endpoints
 
 
 class FalconXSandbox(ServiceClass):
@@ -86,15 +87,15 @@
             operation_id="GetArtifacts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "id"),
             headers=header_payload
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_summary_reports(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_summary_reports(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a short summary version of a sandbox report.
 
         Keyword arguments:
         ids -- List of Summary IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -112,15 +113,15 @@
             endpoints=Endpoints,
             operation_id="GetSummaryReports",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_submissions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_submissions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Check the status of a sandbox analysis.
 
         Time required for analysis varies but is usually less than 15 minutes.
 
         Keyword arguments:
         ids -- ID(s) of submitted malware samples. Find a submission ID from the response when
                submitting a malware sample or search with `query_submissions`.
@@ -142,15 +143,15 @@
             endpoints=Endpoints,
             operation_id="GetSubmissions",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def submit(self: object, body: dict = None, **kwargs) -> dict:
+    def submit(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Submit an uploaded file or a URL for sandbox analysis.
 
         The sample file must have been previously uploaded through `upload_sample`.
         Time required for analysis varies but is usually less than 15 minutes.
 
         Keyword arguments:
         action_script -- Runtime script for sandbox analysis.
@@ -228,15 +229,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="Submit",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_reports(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_reports(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find sandbox reports by providing an FQL filter and paging details.
 
         Returns a set of report IDs that match your criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -260,15 +261,15 @@
             endpoints=Endpoints,
             operation_id="QueryReports",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_submissions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_submissions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find submission IDs for uploaded files by providing an FQL filter and paging details.
 
         Returns a set of submission IDs that match your criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -293,19 +294,19 @@
             operation_id="QuerySubmissions",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def upload_sample(self: object,
-                      file_data: object,
+                      file_data: object = None,
                       body: dict = None,
                       parameters: dict = None,
                       **kwargs
-                      ) -> dict:
+                      ) -> Dict[str, Union[int, dict]]:
         """Upload a file for sandbox analysis.
 
         After uploading, use `submit` to start analyzing the file.
 
         Keyword arguments:
         comment -- A descriptive comment to identify the file for other users. String.
         file_data -- Content of the uploaded sample in binary format. Max file size is 256 MB.
@@ -396,15 +397,15 @@
             endpoints=Endpoints,
             operation_id="GetReports",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_report(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_report(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a report based on the report ID.
 
         Operation can be checked for success by polling for the report ID on the get_summary_reports endpoint.
 
         Keyword arguments:
         ids -- ID(s) of report to delete. Find a report ID from the response when
                submitting a malware sample or search with `query_reports`.
@@ -459,15 +460,15 @@
             endpoints=Endpoints,
             operation_id="GetSampleV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_sample(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_sample(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Remove a sample, including file, meta and submissions from the collection.
 
         Keyword arguments:
         ids -- SHA256 of the file to delete. Find the SHA256 from the response when
                submitting a malware sample or search with `query_sample`.
                String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -487,15 +488,15 @@
             endpoints=Endpoints,
             operation_id="DeleteSampleV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def query_sample(self: object, body: dict = None, **kwargs) -> dict:
+    def query_sample(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a list with sha256 of samples that exist and customer has rights to access.
 
         Maximum number of accepted items is 200.
 
         Keyword arguments:
         sha256s -- List of SHA256s to confirm existence for. You will be returned a list of
                existing hashes. String or list of strings.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/filevantage.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/filevantage.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._service_class import ServiceClass
 from ._endpoint._filevantage import _filevantage_endpoints as Endpoints
 
 
 class FileVantage(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -50,15 +51,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_changes(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_changes(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve information on changes.
 
         Keyword arguments:
         ids -- Change IDs to retrieve. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -76,15 +77,15 @@
             endpoints=Endpoints,
             operation_id="getChanges",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_changes(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_changes(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for changes within your environment. Returns one or more change IDs.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filters
                   action_timestamp      ingestion_timestamp
                   host.name
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/firewall_management.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/firewall_management.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=C0302,R0904
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import (
     aggregate_payload,
     firewall_container_payload,
     firewall_rule_group_validation_payload,
     firewall_rule_group_payload,
     firewall_rule_group_update_payload,
@@ -61,15 +62,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_events(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_events(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Aggregate events for customer.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -137,15 +138,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="aggregate_events",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_policy_rules(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_policy_rules(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Aggregate rules within a policy for customer.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -213,15 +214,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="aggregate_policy_rules",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_rule_groups(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_rule_groups(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Aggregate rule groups for customer.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -289,15 +290,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="aggregate_rule_groups",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_rules(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_rules(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Aggregate rules for customer.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -365,15 +366,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="aggregate_rules",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_events(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_events(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get events entities by ID and optionally version.
 
         Keyword arguments:
         ids -- The IDs of the events to retrieve. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -391,15 +392,15 @@
             endpoints=Endpoints,
             operation_id="get_events",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_firewall_fields(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_firewall_fields(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the firewall field specifications by ID.
 
         Keyword arguments:
         ids -- The IDs of the rule types to retrieve. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -864,15 +865,15 @@
             endpoints=Endpoints,
             operation_id="delete_network_locations",
             params=handle_single_argument(args, parameters, "ids"),
             keywords=kwargs
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get platforms by ID, e.g., windows or mac or droid.
 
         Keyword arguments:
         ids -- The IDs of the platforms to retrieve. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -890,15 +891,15 @@
             endpoints=Endpoints,
             operation_id="get_platforms",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policy_containers(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policy_containers(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get policy container entities by policy ID.
 
         Keyword arguments:
         ids -- The IDs of the policy container(s) to retrieve. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -920,15 +921,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def update_policy_container_v1(self: object,
                                    body: dict = None,
                                    cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                    **kwargs
-                                   ) -> dict:
+                                   ) -> Dict[str, Union[int, dict]]:
         """Update an identified policy container.
 
         **DEPRECATED**
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
                 {
@@ -974,15 +975,15 @@
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
     def update_policy_container(self: object,
                                 body: dict,
                                 cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                 **kwargs
-                                ) -> dict:
+                                ) -> Dict[str, Union[int, dict]]:
         """Update an identified policy container.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
                 {
                     "default_inbound": "string",
                     "default_outbound": "string",
@@ -1024,15 +1025,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="update_policy_container",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rule group entities by ID.
 
         These groups do not contain their rule entites, just the rule IDs in precedence order.
 
         Keyword arguments:
         ids -- The IDs of the rule group(s) to retrieve. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
@@ -1057,15 +1058,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def create_rule_group(self: object,
                           body: dict = None,
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs
-                          ) -> dict:
+                          ) -> Dict[str, Union[int, dict]]:
         """Create new rule group on a platform for a customer with a name and description.
 
         Returns the ID.
 
         Keyword arguments:
         action -- Rule action to perform. String. Overridden if 'rules' keyword is provided.
         address_family -- Address type, String. Either 'IP4', 'IP6' or 'NONE'.
@@ -1254,15 +1255,15 @@
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def delete_rule_groups(self: object,
                            *args,
                            cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                            parameters: dict = None,
                            **kwargs
-                           ) -> dict:
+                           ) -> Dict[str, Union[int, dict]]:
         """Delete rule group entities by ID.
 
         Keyword arguments:
         ids -- The IDs of the rule group(s) to delete. String or list of strings.
         parameters - full parameters payload, not required if `ids` keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -1285,15 +1286,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def update_rule_group(self: object,
                           body: dict = None,
                           cs_username: str = None,  # pylint: disable=W0613  # deprecated
                           parameters: dict = None,
                           **kwargs
-                          ) -> dict:
+                          ) -> Dict[str, Union[int, dict]]:
         """Update name, description, or enabled status of a rule group and underlying rules.
 
         Can also create, edit, delete, or reorder rules.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
                 {
@@ -1345,15 +1346,19 @@
             operation_id="update_rule_group",
             body=body,
             params=parameters,
             keywords=kwargs
             )
 
     @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
-    def create_rule_group_validation(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def create_rule_group_validation(self: object,
+                                     body: dict = None,
+                                     parameters: dict = None,
+                                     **kwargs
+                                     ) -> Dict[str, Union[int, dict]]:
         """Validate the request for creating a new rule group on a platform for a customer with a name and description.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
                 {
                     "description": "string",
                     "enabled": true,
@@ -1452,15 +1457,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def update_rule_group_validation(self: object,
                                      body: dict = None,
                                      cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                      parameters: dict = None,
                                      **kwargs
-                                     ) -> dict:
+                                     ) -> Dict[str, Union[int, dict]]:
         """Validate the request.
 
         Validates the request of updating name, description, or enabled status
         of a rule group, or create, edit, delete, or reorder rules.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if other keywords are provided.
@@ -1513,15 +1518,15 @@
             operation_id="update_rule_group_validation",
             body=body,
             params=parameters,
             keywords=kwargs
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rule entities by ID or Family ID.
 
         ID = 64-bit unsigned int as decimal string
         Family ID = 32-character hexadecimal string
 
         Keyword arguments:
         ids -- The IDs of the rule(s) to retrieve. String or list of strings.
@@ -1542,15 +1547,15 @@
             endpoints=Endpoints,
             operation_id="get_rules",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def validate_filepath_pattern(self: object, body: dict = None, **kwargs) -> dict:
+    def validate_filepath_pattern(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Validate that the test pattern matches the executable filepath glob pattern.
 
         Keyword arguments:
         body -- Full body payload in JSON format. Not required if using other keywords. Dictionary.
                 {
                     "filepath_pattern": "string",
                     "filepath_test_string": "string"
@@ -1575,15 +1580,15 @@
             endpoints=Endpoints,
             operation_id="validate_filepath_pattern",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_events(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_events(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all event IDs matching the query with filter.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination
                  of results. On your first request, don't provide an after token. On
                  subsequent requests, provide the after token from the previous response
                  to continue from that place in the results.
@@ -1617,15 +1622,15 @@
             endpoints=Endpoints,
             operation_id="query_events",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_firewall_fields(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_firewall_fields(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the firewall field specification IDs for the provided platform.
 
         Keyword arguments:
         platform_id -- Get fields configuration for this platform. String.
         limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
         offset -- The integer offset to start retrieving records from. Defaults to 0.
         parameters - full parameters payload, not required if using other keywords.
@@ -1677,15 +1682,15 @@
             endpoints=Endpoints,
             operation_id="query_network_locations",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_platforms(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the list of platform names.
 
         Keyword arguments:
         limit -- The maximum number of rule IDs to return. [integer, 1-100]
         offset -- The integer offset to start retrieving records from. Defaults to 0.
         parameters - full parameters payload, not required if using other keywords.
 
@@ -1703,15 +1708,15 @@
             endpoints=Endpoints,
             operation_id="query_platforms",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_rules(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all firewall rule IDs matching the query with filter.
 
         Results are returned in precedence order.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination
                  of results. On your first request, don't provide an after token. On
@@ -1747,15 +1752,15 @@
             endpoints=Endpoints,
             operation_id="query_policy_rules",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all rule group IDs matching the query with filter.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination
                  of results. On your first request, don't provide an after token. On
                  subsequent requests, provide the after token from the previous response
                  to continue from that place in the results.
@@ -1789,15 +1794,15 @@
             endpoints=Endpoints,
             operation_id="query_rule_groups",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all rule IDs matching the query with filter.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination
                  of results. On your first request, don't provide an after token. On
                  subsequent requests, provide the after token from the previous response
                  to continue from that place in the results.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/firewall_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/firewall_policies.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, generate_error_result, force_default
 from ._util import args_to_params, handle_single_argument
 from ._payload import generic_payload_list, firewall_policy_payload
 from ._service_class import ServiceClass
 from ._endpoint._firewall_policies import _firewall_policies_endpoints as Endpoints
 
 
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details.
 
         Returns a set of host details which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Firewall Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -85,15 +86,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedFirewallPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Firewall Policies in your environment by providing an FQL filter and paging details.
 
         Returns a set of Firewall Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -122,15 +123,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedFirewallPolicies",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Perform the specified action on the Firewall Policies specified in the request.
 
         Keyword arguments:
         action_name -- action to perform: 'add-host-group', 'disable', 'enable',
                        or 'remove-host-group'.
         action_parameters -- Action specific parameter options. List of dictionaries.
                              {
@@ -189,15 +190,15 @@
                             )
         else:
             returned = generate_error_result("Invalid value specified for action_name parameter.")
 
         return returned
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def set_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def set_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Set the precedence of Firewall Policies based on the order of IDs specified in the request.
 
         The first ID specified will have the highest precedence and the last ID specified
         will have the lowest. You must specify all non-Default Policies for a platform when
         updating precedence.
 
         Keyword arguments:
@@ -229,15 +230,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="setFirewallPoliciesPrecedence",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Firewall Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Firewall Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -255,15 +256,15 @@
             endpoints=Endpoints,
             operation_id="getFirewallPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def create_policies(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def create_policies(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Firewall Policies by specifying details about the policy to create.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -297,15 +298,15 @@
             operation_id="createFirewallPolicies",
             keywords=kwargs,
             params=parameters,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Firewall Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Firewall Policy IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -323,15 +324,15 @@
             endpoints=Endpoints,
             operation_id="deleteFirewallPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Firewall Policies by specifying the ID of the policy and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                 "resources": [
                     {
@@ -362,15 +363,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateFirewallPolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details.
 
         Returns a set of Agent IDs which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Device Control Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -395,15 +396,15 @@
             endpoints=Endpoints,
             operation_id="queryFirewallPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Firewall Policies in your environment by providing an FQL filter and paging details.
 
         Returns a set of Firewall Policy IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/host_group.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/host_group.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import generate_error_result, force_default, args_to_params
 from ._util import handle_single_argument, process_service_request
 from ._payload import host_group_create_payload, host_group_update_payload
 from ._payload import generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._host_group import _host_group_endpoints as Endpoints
 
@@ -53,15 +54,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_group_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Host Group in your environment.
 
         Provide a FQL filter and paging details.
 
         Returns a set of host details which match the filter criteria.
 
         Keyword arguments:
@@ -90,15 +91,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedGroupMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_host_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_host_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Host Groups in your environment by providing an FQL filter and paging details.
 
         Returns a set of Host Groups which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
@@ -135,15 +136,15 @@
             )
 
     @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
     def perform_group_action(self: object,
                              body: dict = None,
                              parameters: dict = None,
                              **kwargs
-                             ) -> dict:
+                             ) -> Dict[str, Union[int, dict]]:
         """Perform the specified action on the Host Groups specified in the request.
 
         Keyword arguments:
         action_name -- Action to perform on the host group. String.
                        Allowed values: 'add-hosts' or 'remove-hosts'.
         action_parameters - List of dictionaries containing action specific parameter settings.
         body -- full body payload, not required when using other keywords.
@@ -199,15 +200,15 @@
                             )
         else:
             returned = generate_error_result("Invalid value specified for action_name parameter.")
 
         return returned
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Host Groups by specifying their IDs.
 
         Keyword arguments:
         ids -- List of host group IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -225,15 +226,15 @@
             endpoints=Endpoints,
             operation_id="getHostGroups",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_host_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def create_host_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Host Groups by specifying details about the group to create.
 
         Keyword arguments:
         assignment_rule -- Assignment rule to apply. String.
         body -- full body payload, not required when using other keywords.
                 {
                     "resources": [
@@ -265,15 +266,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createHostGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Host Groups by specifying their IDs.
 
         Keyword arguments:
         ids -- List of host group IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -291,15 +292,15 @@
             endpoints=Endpoints,
             operation_id="deleteHostGroups",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_host_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def update_host_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Host Groups by specifying the ID of the group and details to update.
 
         Keyword arguments:
         assignment_rule -- Assignment rule to apply. String.
         body -- full body payload, not required when using other keywords.
                 {
                     "resources": [
@@ -331,15 +332,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateHostGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_group_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Host Group in your environment.
 
         Provide a FQL filter and paging details.
 
         Returns a set of Agent IDs which match the filter criteria.
 
         Keyword arguments:
@@ -367,15 +368,15 @@
             endpoints=Endpoints,
             operation_id="queryGroupMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_host_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_host_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Host Groups in your environment by providing an FQL filter and paging details.
 
         Returns a set of Host Group IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/hosts.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/hosts.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import generate_error_result, force_default, args_to_params
 from ._util import process_service_request, handle_single_argument
 from ._payload import generic_payload_list, simple_action_parameter
 from ._service_class import ServiceClass
 from ._endpoint._hosts import _hosts_endpoints as Endpoints
 
 
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters", "body"], default_types=["dict"])
-    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Take various actions on the hosts in your environment.
 
         Contain or lift containment on a host. Delete or restore a host.
 
         Keyword arguments:
         action_name -- action to perform, 'contain', 'lift_containment',
                        'hide_host', 'unhide_host', 'detection_suppress', or
@@ -169,15 +170,15 @@
 
         return returned
 
     def update_device_tags(self: object,
                            action_name: str,
                            ids: list or str,
                            tags: list or str
-                           ) -> dict:
+                           ) -> Dict[str, Union[int, dict]]:
         """Append or remove one or more Falcon Grouping Tags on one or more hosts.
 
         Keyword arguments:
         action_name -- action to perform, 'add' or 'remove'.
         ids -- AID(s) of the hosts to update. String or list of strings.
         tags -- Tag(s) to update. String or list of strings.
 
@@ -230,15 +231,15 @@
                 body=body_payload,
                 )
         else:
             returned = generate_error_result("Invalid value specified for action_name parameter.")
         return returned
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_device_details_v1(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_device_details_v1(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on one or more hosts by providing agent IDs (AID).
 
         You can get a host's agent IDs (AIDs) from query_devices_by_filter,
         the Falcon console or the Streaming API.
 
         Keyword arguments:
         ids -- AID(s) of the hosts to retrieve. String or list of strings.
@@ -259,15 +260,15 @@
             endpoints=Endpoints,
             operation_id="GetDeviceDetailsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_device_details_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_device_details_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on one or more hosts by providing agent IDs (AID).
 
         You can get a host's agent IDs (AIDs) from query_devices_by_filter,
         the Falcon console or the Streaming API. Supports up to a maximum of 100 IDs.
 
         For most scenarios, developers should leverage the 'get_device_details' method
         (PostDeviceDetailsV2 operation) instead of this method.
@@ -296,15 +297,15 @@
 
     @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
     def get_device_details(self: object,
                            *args,
                            body: dict = None,
                            parameters: dict = None,
                            **kwargs
-                           ) -> dict:
+                           ) -> Dict[str, Union[int, dict]]:
         """Get details on one or more hosts by providing agent IDs (AID).
 
         You can get a host's agent IDs (AIDs) from query_devices_by_filter,
         the Falcon console or the Streaming API. Supports up to a maximum of 5000 IDs.
 
         FOR DEVELOPERS: This Operation ID is `PostDeviceDetailsV2`, and is the preferred method
         for retrieving device details from the API. In order to assist developers leveraging the
@@ -348,15 +349,15 @@
             endpoints=Endpoints,
             operation_id="PostDeviceDetailsV2",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_online_state(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_online_state(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the online status for one or more hosts by specifying each host’s unique ID.
 
         Successful requests return an HTTP 200 response and the status for each host identified
         by a `state` of `online`, `offline`, or `unknown` for each host, identified by host `id`.
         Make a `GET` request to `QueryDevicesByFilter` or `QueryDevicesByFilterScroll` to get a
         list of host IDs.
 
@@ -379,15 +380,15 @@
             endpoints=Endpoints,
             operation_id="GetOnlineState_V1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_hidden_devices(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_hidden_devices(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve hidden hosts that match the provided filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return. [integer, 1-5000]
         offset -- The integer offset to start retrieving records from.
         parameters - full parameters payload, not required if using other keywords.
@@ -425,15 +426,15 @@
             endpoints=Endpoints,
             operation_id="QueryHiddenDevices",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_devices_by_filter_scroll(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_devices_by_filter_scroll(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for hosts in your environment by platform, hostname, IP, and other criteria.
 
         Provides continuous pagination capability (based on offset pointer which expires after
         2 minutes with no maximum limit)
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -474,15 +475,15 @@
             endpoints=Endpoints,
             operation_id="QueryDevicesByFilterScroll",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_devices_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_devices_by_filter(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for hosts in your environment by platform, hostname, IP, and other criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return. [integer, 1-5000]
         offset -- The integer offset to start retrieving records from.
         parameters - full parameters payload, not required if using other keywords.
@@ -520,15 +521,15 @@
             endpoints=Endpoints,
             operation_id="QueryDevicesByFilter",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def query_device_login_history(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def query_device_login_history(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve details about recent login sessions for a set of devices.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "ids": [
                         "string"
@@ -558,15 +559,15 @@
             operation_id="QueryDeviceLoginHistory",
             body=body,
             body_validator={"ids": list} if self.validate_payloads else None,
             body_required=["ids"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def query_network_address_history(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def query_network_address_history(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve history of IP and MAC addresses of devices.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "ids": [
                         "string"
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/identity_protection.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/identity_protection.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default
 from ._service_class import ServiceClass
 from ._endpoint._identity_protection import _identity_protection_endpoints as Endpoints
 
 
 class IdentityProtection(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -50,26 +51,27 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def graphql(self: object, body: dict = None, **kwargs) -> dict:
+    def graphql(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         r"""Identity Protection GraphQL API.
 
         Allows to retrieve entities, timeline activities, identity-based incidents and
         security assessment. Allows to perform actions on entities and identity-based incidents.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "query": "string"
                 }
-        query -- JSON-similar string.
+        query -- JSON-similar string. (GraphQL syntax)
+        variables -- variables to use for interpolation. Dictionary.
 
         This method only supports keywords for providing arguments.
         Currently using a non-standard body payload format.
         Example payload:
         {
             "query": "{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"
         }
@@ -81,14 +83,16 @@
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html
                    /identity-protection/api.preempt.proxy.post.graphql
         """
         if not body:
             body = {}
             body["query"] = kwargs.get("query", "{}")
+            if kwargs.get("variables", None):
+                body["variables"] = kwargs.get("variables")
 
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="api_preempt_proxy_post_graphql",
             body=body
             )
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/incidents.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/incidents.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request
 from ._payload import generic_payload_list, incident_action_parameters
 from ._service_class import ServiceClass
 from ._endpoint._incidents import _incidents_endpoints as Endpoints
 
 
 class Incidents(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def crowdscore(self: object, parameters: dict = None, **kwargs) -> dict:
+    def crowdscore(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query environment wide CrowdScore and return the entity data.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-2500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. Integer.
@@ -81,15 +82,15 @@
             endpoints=Endpoints,
             operation_id="CrowdScore",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_behaviors(self: object, body: dict = None, **kwargs) -> dict:
+    def get_behaviors(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on behaviors by providing behavior IDs.
 
         Keyword arguments:
         body -- full body payload, not required if ids are provided as keyword.
                 {
                     "ids": [
                         "string"
@@ -113,15 +114,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetBehaviors",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def perform_incident_action(self: object, body: dict = None, **kwargs) -> dict:
+    def perform_incident_action(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Perform a set of actions on one or more incidents.
 
         Such as: adding tags or updating the incident name or description.
 
         A maximum of 5000 incidents may be updated per request.
 
         Keyword arguments:
@@ -186,15 +187,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PerformIncidentAction",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_incidents(self: object, body: dict = None, **kwargs) -> dict:
+    def get_incidents(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on incidents by providing incident IDs.
 
         Keyword arguments:
         body -- full body payload, not required if ids are provided as keyword.
                 {
                     "ids": [
                         "string"
@@ -218,15 +219,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetIncidents",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_behaviors(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_behaviors(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for behaviors by providing an FQL filter, sorting, and paging details.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. Integer.
@@ -248,15 +249,15 @@
             endpoints=Endpoints,
             operation_id="QueryBehaviors",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_incidents(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_incidents(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for incidents by providing an FQL filter, sorting, and paging details.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. Integer.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/installation_tokens.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/installation_tokens.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import installation_token_payload, token_settings_payload
 from ._service_class import ServiceClass
 from ._endpoint._installation_tokens import _installation_tokens_endpoints as Endpoints
 
 
 class InstallationTokens(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def audit_events_read(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def audit_events_read(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the details of one or more audit events by id.
 
         Keyword arguments:
         ids -- List of audit event IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -76,15 +77,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="audit_events_read",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
-    def customer_settings_read(self: object) -> dict:
+    def customer_settings_read(self: object) -> Dict[str, Union[int, dict]]:
         """Check current installation token settings.
 
         This method does not accept arguments or keywords.
 
         Returns: dict object containing API response.
 
         HTTP Method: GET
@@ -95,15 +96,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="customer_settings_read"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def tokens_read(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def tokens_read(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the details of one or more tokens by id.
 
         Keyword arguments:
         ids -- List of installation token IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -121,15 +122,15 @@
             endpoints=Endpoints,
             operation_id="tokens_read",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def tokens_create(self: object, body: dict = None, **kwargs) -> dict:
+    def tokens_create(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a token.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "expires_timestamp": "2021-09-22T02:28:11.762Z",
                     "label": "string",
@@ -157,15 +158,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="tokens_create",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def tokens_delete(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def tokens_delete(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a token immediately. To revoke a token, use PATCH tokens_update instead.
 
         Keyword arguments:
         ids -- List of installation token IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -183,15 +184,15 @@
             endpoints=Endpoints,
             operation_id="tokens_delete",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def tokens_update(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
+    def tokens_update(self: object, body: dict, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update one or more tokens.
 
         Use this endpoint to edit labels, change expiration, revoke, or restore.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
@@ -224,15 +225,15 @@
             operation_id="tokens_update",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def audit_events_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def audit_events_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for audit events by providing an FQL filter and paging details.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Example: action:'token_create'
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Defaults to 50.
@@ -255,15 +256,15 @@
             endpoints=Endpoints,
             operation_id="audit_events_query",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def tokens_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def tokens_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for tokens by providing an FQL filter and paging details.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Example: status:'valid'
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Defaults to 50.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/intel.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/intel.py`

 * *Files 12% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._intel import _intel_endpoints as Endpoints
 
 
 class Intel(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_actor_entities(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_actor_entities(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get info about actors that match provided FQL filters.
 
         Keyword arguments:
         fields -- The fields to return, or a predefined set of fields in the form of the collection
                   name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                   Defaults to __basic__.
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -103,15 +104,15 @@
             endpoints=Endpoints,
             operation_id="QueryIntelActorEntities",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_indicator_entities(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_indicator_entities(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get info about indicators that match provided FQL filters.
 
         Keyword arguments:
         fields -- The fields to return, or a predefined set of fields in the form of the collection
                   name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                   Defaults to __basic__.
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -150,15 +151,15 @@
             endpoints=Endpoints,
             operation_id="QueryIntelIndicatorEntities",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_report_entities(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_report_entities(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get info about reports that match provided FQL filters.
 
         Keyword arguments:
         fields -- The fields to return, or a predefined set of fields in the form of the collection
                   name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                   Defaults to __basic__.
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -202,15 +203,15 @@
             endpoints=Endpoints,
             operation_id="QueryIntelReportEntities",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_actor_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_actor_entities(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve specific actors using their actor IDs.
 
         Keyword arguments:
         fields -- The fields to return, or a predefined set of fields in the form of the collection
                   name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                   Defaults to __basic__.
         ids -- One or more actor IDs. String or list of strings.
@@ -231,15 +232,15 @@
             endpoints=Endpoints,
             operation_id="GetIntelActorEntities",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_indicator_entities(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_indicator_entities(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve specific indicators using their indicator IDs.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "ids": [
                         "string"
@@ -269,14 +270,78 @@
             operation_id="GetIntelIndicatorEntities",
             body=body,
             body_validator={"ids": list} if self.validate_payloads else None,
             body_required=["ids"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
+    def get_mitre_report(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], bytes]:
+        """Export Mitre ATT&CK information for a given actor.
+
+        Keyword arguments:
+        actor_id -- Actor ID, derived from the actor name. String.
+        format -- Report format. Accepted options: 'CSV' or 'JSON'. String
+        parameters - full parameters payload, not required if using other keywords.
+
+        This method only supports keywords for providing arguments.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: GET
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetMitreReport
+        """
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="GetMitreReport",
+            keywords=kwargs,
+            params=parameters
+            )
+
+    @force_default(defaults=["body"], default_types=["dict"])
+    def mitre_attacks(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
+        """Retrieve reports and observable IDs associated with the given actor and attacks.
+
+        Keyword arguments:
+        body -- full body payload, not required when ids keyword is provided.
+                {
+                    "ids": [
+                        "string"
+                    ]
+                }
+        ids -- ID(s) of the indicator entities to retrieve. String or list of strings.
+
+        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
+                   All others are ignored.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: POST
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/PostMitreAttacks
+        """
+        if not body:
+            body = generic_payload_list(submitted_arguments=args,
+                                        submitted_keywords=kwargs,
+                                        payload_value="ids"
+                                        )
+
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="PostMitreAttacks",
+            body=body,
+            body_validator={"ids": list} if self.validate_payloads else None,
+            body_required=["ids"] if self.validate_payloads else None
+            )
+
+    @force_default(defaults=["parameters"], default_types=["dict"])
     def get_report_pdf(self: object, *args, parameters: dict = None, **kwargs) -> object:
         """Return a Report PDF attachment.
 
         Keyword arguments:
         id -- One or more actor IDs. String or list of strings.
         parameters - full parameters payload, not required if id is provided as a keyword.
 
@@ -295,15 +360,15 @@
             endpoints=Endpoints,
             operation_id="GetIntelReportPDF",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "id")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_report_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_report_entities(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve specific reports using their report IDs.
 
         Keyword arguments:
         fields -- The fields to return, or a predefined set of fields in the form of the collection
                   name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                   Defaults to __basic__.
         ids -- One or more actor IDs. String or list of strings.
@@ -382,15 +447,15 @@
             endpoints=Endpoints,
             operation_id="GetLatestIntelRuleFile",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "type")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rule_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rule_entities(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve details for rule sets for the specified ids.
 
         Keyword arguments:
         ids -- One or more actor IDs. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -408,15 +473,15 @@
             endpoints=Endpoints,
             operation_id="GetIntelRuleEntities",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_actor_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_actor_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get actor IDs that match provided FQL filters.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filter parameters:
                   actors                sub_type.name
                   actors.id             sub_type.slug
@@ -457,15 +522,15 @@
             endpoints=Endpoints,
             operation_id="QueryIntelActorIds",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_indicator_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_indicator_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get indicators IDs that match provided FQL filters.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filter parameters:
                   _marker               labels.name
                   actors                last_updated
@@ -501,15 +566,41 @@
             endpoints=Endpoints,
             operation_id="QueryIntelIndicatorIds",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_report_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_mitre_attacks(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
+        """Get MITRE tactics and techniques for the given actor.
+
+        Keyword arguments:
+        id -- Actor ID, derived from the actor name. (Example: fancy-bear) String.
+        parameters - full parameters payload, not required if using `id` keyword.
+
+        Arguments: When not specified, the first argument to this method is assumed to be 'id'.
+                   All others are ignored.
+
+        Returns: dict object containing API response.
+
+        HTTP Method: GET
+
+        Swagger URL
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryMitreAttacks
+        """
+        return process_service_request(
+            calling_object=self,
+            endpoints=Endpoints,
+            operation_id="QueryMitreAttacks",
+            keywords=kwargs,
+            params=handle_single_argument(args, parameters, "id")
+            )
+
+    @force_default(defaults=["parameters"], default_types=["dict"])
+    def query_report_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get report IDs that match provided FQL filters.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filter parameters:
                   actors                sub_type.name
                   actors.id             sub_type.slug
@@ -550,15 +641,15 @@
             endpoints=Endpoints,
             operation_id="QueryIntelReportIds",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rule_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rule_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for rule IDs that match provided filter criteria.
 
         Keyword arguments:
         description -- substring match on the description field. List of strings.
         limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
         max_created_date -- Filter results to those created on or before a certain date. String.
         min_created_date -- Filter results to those created on or after a certain date. String.
@@ -666,16 +757,19 @@
     QueryIntelActorEntities = query_actor_entities
     QueryIntelIndicatorEntities = query_indicator_entities
     QueryIntelReportEntities = query_report_entities
     QueryVulnerabilities = query_vulnerabilities
     GetVulnerabilities = get_vulnerabilities
     GetIntelActorEntities = get_actor_entities
     GetIntelIndicatorEntities = get_indicator_entities
+    GetMitreReport = get_mitre_report
+    PostMitreAttacks = mitre_attacks
     GetIntelReportPDF = get_report_pdf
     GetIntelReportEntities = get_report_entities
     GetIntelRuleFile = get_rule_file
     GetLatestIntelRuleFile = get_latest_rule_file
     GetIntelRuleEntities = get_rule_entities
+    QueryMitreAttacks = query_mitre_attacks
     QueryIntelActorIds = query_actor_ids
     QueryIntelIndicatorIds = query_indicator_ids
     QueryIntelReportIds = query_report_ids
     QueryIntelRuleIds = query_rule_ids
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ioa_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ioa_exclusions.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, handle_single_argument, process_service_request
 from ._service_class import ServiceClass
 from ._endpoint._ioa_exclusions import _ioa_exclusions_endpoints as Endpoints
 from ._payload import ioa_exclusion_payload
 
 
 class IOAExclusions(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a set of IOA Exclusions by specifying their IDs.
 
         Keyword arguments:
         ids -- List of exclusion IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -77,15 +78,15 @@
             endpoints=Endpoints,
             operation_id="getIOAExclusionsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def create_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create the IOA exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
             {
                 "cl_regex": "string",
                 "comment": "string",
@@ -125,15 +126,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createIOAExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
+    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete the IOA Exclusions by ID.
 
         Keyword arguments:
         comment -- Explains why this exclusions was deleted. String.
         ids -- List of exclusion IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -152,15 +153,15 @@
             endpoints=Endpoints,
             operation_id="deleteIOAExclusionsV1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def update_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update the IOA Exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
             {
                 "cl_regex": "string",
                 "comment": "string",
@@ -205,15 +206,18 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateIOAExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
+    def query_exclusions(self: object,
+                         parameters: dict = None,
+                         **kwargs
+                         ) -> Dict[str, Union[int, dict]]:
         """Search for IOA Exclusions.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
                   AVAILABLE FILTERS
                   applied_globally            last_modified
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ioc.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ioc.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import (
     aggregate_payload,
     indicator_payload,
     indicator_update_payload,
     indicator_report_payload
     )
@@ -57,15 +58,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
-    def indicator_aggregate(self: object, parameters: dict = None, body: dict = None, **kwargs) -> dict:
+    def indicator_aggregate(self: object, parameters: dict = None, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get indicator aggregates as specified via json in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "date_ranges": [
                     {
@@ -129,15 +130,15 @@
             endpoints=Endpoints,
             operation_id="indicator_aggregate_v1",
             body=body,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def indicator_combined(self: object, parameters: dict = None, **kwargs) -> dict:
+    def indicator_combined(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get Combined for Indicators.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an `after` token. On subsequent requests,
                  provide the `after` token from the previous response to continue from that place
                  in the results. To access more than 10k indicators, use the `after` parameter
@@ -179,15 +180,15 @@
             endpoints=Endpoints,
             operation_id="indicator_combined_v1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def action_get(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def action_get(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get Actions by IDs.
 
         Keyword arguments:
         ids -- List of Indicator ID(s) you wish to lookup. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -205,15 +206,15 @@
             endpoints=Endpoints,
             operation_id="action_get_v1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_indicators_report(self: object, body: dict = None, **kwargs) -> dict:
+    def get_indicators_report(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Launch an indicators report creation job.
 
         Keyword arguments:
         body -- full parameters payload, not required if using other keywords.
                 {
                     "report_format": "string",
                     "search": {
@@ -253,15 +254,15 @@
             endpoints=Endpoints,
             operation_id="GetIndicatorsReport",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def indicator_get(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def indicator_get(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get Indicators by IDs.
 
         Keyword arguments:
         ids -- List of Indicator ID(s) you wish to lookup. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -283,15 +284,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def indicator_create(self: object,
                          body: dict = None,
                          parameters: dict = None,
                          **kwargs
-                         ) -> dict:
+                         ) -> Dict[str, Union[int, dict]]:
         """Create Indicators.
 
         Keyword arguments:
         action -- Default action for the IOC. String.
         applied_globally -- Is this IOC applied globally? Boolean.
         body -- full body payload, not required if keywords are used.
                 {
@@ -362,15 +363,15 @@
             operation_id="indicator_create_v1",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def indicator_delete(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def indicator_delete(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete Indicators by IDs.
 
         Keyword arguments:
         ids -- List of Indicator ID(s) you wish to delete. String or list of strings.
         from_parent -- Limit action to IOCs originating from the MSSP parent.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -389,15 +390,15 @@
             endpoints=Endpoints,
             operation_id="indicator_delete_v1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def indicator_update(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
+    def indicator_update(self: object, body: dict, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Indicators.
 
         Keyword arguments:
         action -- Default action for the IOC. String.
         applied_globally -- Is this IOC applied globally? Boolean.
         body -- full body payload, not required if keywords are used.
                 {
@@ -489,15 +490,15 @@
             operation_id="indicator_update_v1",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def action_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def action_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query Actions.
 
         Keyword arguments:
         limit -- Number of IDs to return. Integer.
         offset -- Starting index of overall result set from which to return IDs. String.
         parameters -- full parameters payload, not required if using other keywords.
 
@@ -515,15 +516,15 @@
             endpoints=Endpoints,
             operation_id="action_query_v1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def indicator_search(self: object, parameters: dict = None, **kwargs) -> dict:
+    def indicator_search(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Indicators.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an `after` token. On subsequent requests,
                  provide the `after` token from the previous response to continue from that place
                  in the results. To access more than 10k indicators, use the `after` parameter
@@ -563,15 +564,15 @@
             endpoints=Endpoints,
             operation_id="indicator_search_v1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def ioc_type_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def ioc_type_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query IOC types.
 
         Keyword arguments:
         limit -- Number of IDs to return. Integer.
         offset -- Starting index of overall result set from which to return IDs. String.
         parameters -- full parameters payload, not required if using other keywords.
 
@@ -589,15 +590,15 @@
             endpoints=Endpoints,
             operation_id="ioc_type_query_v1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def platform_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def platform_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query platforms.
 
         Keyword arguments:
         limit -- Number of IDs to return. Integer.
         offset -- Starting index of overall result set from which to return IDs. String.
         parameters -- full parameters payload, not required if using other keywords.
 
@@ -615,15 +616,15 @@
             endpoints=Endpoints,
             operation_id="platform_query_v1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def severity_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def severity_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query severities.
 
         Keyword arguments:
         limit -- Number of IDs to return. Integer.
         offset -- Starting index of overall result set from which to return IDs. String.
         parameters -- full parameters payload, not required if using other keywords.
 
@@ -642,15 +643,15 @@
             operation_id="severity_query_v1",
             keywords=kwargs,
             params=parameters
             )
 
     # These methods are ported from the legacy IOCS Service Class, as they have not been deprecated
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def devices_count(self: object, parameters: dict = None, **kwargs) -> dict:
+    def devices_count(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return the number of hosts in your customer account that have observed a given custom IOC.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
                 `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
                 `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
@@ -674,15 +675,15 @@
             endpoints=LegacyEndpoints,
             operation_id="DevicesCount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
+    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find hosts that have observed a given custom IOC.
 
         For details about those hosts, use the hosts API interface.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
@@ -712,15 +713,15 @@
             endpoints=LegacyEndpoints,
             operation_id="DevicesRanOn",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
+    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for processes associated with a custom IOC.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
                 `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
                 `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
@@ -751,15 +752,15 @@
             endpoints=LegacyEndpoints,
             operation_id="ProcessesRanOn",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """For the provided ProcessID retrieve the process details.
 
         Keyword arguments:
         ids -- List of Process ID(s) for the running process you want to lookup.
                String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/iocs.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/iocs.py`

 * *Files 6% similar despite different names*

```diff
@@ -37,14 +37,15 @@
 """
 # The bulk of the methods within this class have been deprecated. Those
 # that are not, have been ported into the new IOC Service Class. Developers
 # should move all code over to use this new class (ioc.py) as support for
 # this class will eventually be dropped.
 # Allowing unused params and kwargs to prevent breaking change, no self use is ok
 # pylint: disable=W0613
+from typing import Dict, Union
 from ._util import force_default, handle_single_argument
 from ._util import process_service_request, generate_error_result
 from ._service_class import ServiceClass
 from ._endpoint._iocs import _iocs_endpoints as Endpoints
 
 
 class Iocs(ServiceClass):
@@ -57,15 +58,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def devices_count(self: object, parameters: dict = None, **kwargs) -> dict:
+    def devices_count(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the number of hosts in your customer account that have observed a given custom IOC.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
                 `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
                 `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
@@ -89,15 +90,15 @@
             endpoints=Endpoints,
             operation_id="DevicesCount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_ioc(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_ioc(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get an IOC by providing a type and value.
 
         * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
         This API endpoint is no longer available. Please use the new IOC.indicator_get
         method defined in the new IOC service class in order to perform this operation.
 
         This method performs no actions, ignoring all consumed arguments or keywords.
@@ -108,15 +109,15 @@
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/GetIOC
         """
         return generate_error_result(
             "This method has been deprecated. Please use the new IOC Service Class method "
             "IOC.indicator_get to perform this operation."
             )
 
-    def create_ioc(self: object, body: dict) -> dict:
+    def create_ioc(self: object, body: dict) -> Dict[str, Union[int, dict]]:
         """Create a new IOC.
 
         * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
         This API endpoint is no longer available. Please use the new IOC.indicator_create
         method defined in the new IOC service class in order to perform this operation.
 
         This method performs no actions, ignoring all consumed arguments or keywords.
@@ -128,15 +129,15 @@
         """
         return generate_error_result(
             "This method has been deprecated. Please use the new IOC Service Class method "
             "IOC.indicator_create to perform this operation."
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_ioc(self: object, parameters: dict = None, **kwargs) -> dict:
+    def delete_ioc(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an IOC by providing a type and value.
 
         * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
         This API endpoint is no longer available. Please use the new IOC.indicator_delete
         method defined in the new IOC service class in order to perform this operation.
 
         This method performs no actions, ignoring all consumed arguments or keywords.
@@ -148,15 +149,15 @@
         """
         return generate_error_result(
             "This method has been deprecated. Please use the new IOC Service Class method "
             "IOC.indicator_delete to perform this operation."
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def update_ioc(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
+    def update_ioc(self: object, body: dict, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update an IOC by providing a type and value.
 
         * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
         This API endpoint is no longer available. Please use the new IOC.indicator_update
         method defined in the new IOC service class in order to perform this operation.
 
         This method performs no actions, ignoring all consumed arguments or keywords.
@@ -168,15 +169,15 @@
         """
         return generate_error_result(
             "This method has been deprecated. Please use the new IOC Service Class method "
             "IOC.indicator_update to perform this operation."
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
+    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find hosts that have observed a given custom IOC.
 
         For details about those hosts, use the hosts API interface.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
@@ -206,15 +207,15 @@
             endpoints=Endpoints,
             operation_id="DevicesRanOn",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_iocs(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_iocs(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search the custom IOCs in your customer account.
 
         * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * * DEPRECATED METHOD * * *
         This API endpoint is no longer available. Please use the new IOC.indicator_search
         method defined in the new IOC service class in order to perform this operation.
 
         This method performs no actions, ignoring all consumed arguments or keywords.
@@ -226,15 +227,15 @@
         """
         return generate_error_result(
             "This method has been deprecated. Please use the new IOC Service Class method "
             "IOC.indicator_search to perform this operation."
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
+    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for processes associated with a custom IOC.
 
         Keyword arguments:
         type -- The type of indicator. String. Required.
                 Valid types include:
                 `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
                 `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
@@ -265,15 +266,15 @@
             endpoints=Endpoints,
             operation_id="ProcessesRanOn",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """For the provided ProcessID retrieve the process details.
 
         Keyword arguments:
         ids -- List of Process ID(s) for the running process you want to lookup.
                String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/kubernetes_protection.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/kubernetes_protection.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._service_class import ServiceClass
 from ._endpoint._kubernetes_protection import _kubernetes_protection_endpoints as Endpoints
 
 
 class KubernetesProtection(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -50,15 +51,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_aws_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_aws_accounts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provide a list of AWS accounts.
 
         Keyword arguments:
         ids -- AWS Account IDs. String or list of strings.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. String.
@@ -80,15 +81,15 @@
             endpoints=Endpoints,
             operation_id="GetAWSAccountsMixin0",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_aws_account(self: object, body: dict = None, **kwargs) -> dict:
+    def create_aws_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a new AWS customer account in our system and generates the installation script.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
                 {
                     "resources": [
                         {
@@ -121,15 +122,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateAWSAccount",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete AWS accounts.
 
         Keyword arguments:
         ids -- ID(s) of AWS accounts to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -147,15 +148,15 @@
             endpoints=Endpoints,
             operation_id="DeleteAWSAccountsMixin0",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def update_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
+    def update_aws_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update the AWS account per the query parameters provided.
 
         Keyword arguments:
         ids -- ID(s) of AWS accounts to update. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
         region -- Default region for Account Automation.
 
@@ -173,15 +174,15 @@
             endpoints=Endpoints,
             operation_id="UpdateAWSAccount",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_azure_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def list_azure_accounts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provide a list of registered Azure subscriptions.
 
         Keyword arguments:
         ids -- Azure tenant IDs. String or list of strings.
         is_horizon_acct -- Filter by whether an account originates from Horizon. Boolean.
         subscription_id -- Azure subscription IDs. String or list of strings.
         limit -- The maximum number of records to return in this response. [Integer, 1-500]
@@ -205,15 +206,15 @@
             endpoints=Endpoints,
             operation_id="ListAzureAccounts",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_azure_subscription(self: object, body: dict = None, **kwargs) -> dict:
+    def create_azure_subscription(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a new Azure subscription.
 
         Keyword arguments:
         body -- full body payload, not required if using other keywords.
                 {
                     "resources": [
                         {
@@ -246,15 +247,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateAzureSubscription",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_azure_subscription(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_azure_subscription(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an Azure subscription.
 
         Keyword arguments:
         ids -- Azure subscription IDs. String or list of strings.
         parameters - full parameters payload, not required if using other keywords.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -272,15 +273,15 @@
             endpoints=Endpoints,
             operation_id="DeleteAzureSubscription",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_locations(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_locations(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provide the cloud locations acknowledged by the Kubernetes Protection service.
 
         Keyword arguments:
         clouds -- Cloud provider. String or list of strings.
         parameters - full parameters payload, not required if using other keywords.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'clouds'.
@@ -298,15 +299,15 @@
             endpoints=Endpoints,
             operation_id="GetLocations",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "clouds")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_helm_values_yaml(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_helm_values_yaml(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provide a sample Helm values.yaml file to install alongside the agent Helm chart.
 
         Keyword arguments:
         cluster_name -- Cloud provider. String.
         parameters - full parameters payload, not required if using other keywords.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -324,15 +325,15 @@
             endpoints=Endpoints,
             operation_id="GetHelmValuesYaml",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cluster_name")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def regenerate(self: object, body: dict = None) -> dict:
+    def regenerate(self: object, body: dict = None) -> Dict[str, Union[int, dict]]:
         """Regenerate API key for docker registry integrations.
 
         Keyword arguments:
         body -- Body payload is accepted but is not used.
 
         This method has no default argument or keywords.
 
@@ -347,15 +348,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RegenerateAPIKey",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_clusters(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_clusters(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Provide the clusters acknowledged by the Kubernetes Protection service.
 
         Keyword arguments:
         account_ids -- Cluster Account IDs. For EKS, this would be the AWS Account ID.
                        String or list of strings.
         cluster_names -- Cluster name. For EKS it will be cluster ARN. String or list of strings.
         cluster_service -- Cluster Service. Available values: `eks`
@@ -385,15 +386,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def trigger_scan(self: object,
                      *args,
                      body: dict = None,
                      parameters: dict = None,
                      **kwargs
-                     ) -> dict:
+                     ) -> Dict[str, Union[int, dict]]:
         """Trigger a dry run or a full scan of a customer's kubernetes footprint.
 
         Keyword arguments:
         body -- Body payload is accepted but is not used.
         scan_type -- Type of scan to perform. String.  Default value: `dry-run`.
                      Available Values: `cluster-refresh`, `dry-run`, or `full`.
         parameters - full parameters payload, not required if using other keywords.
@@ -414,15 +415,15 @@
             operation_id="TriggerScan",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "scan_type"),
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def update_azure_service_principal(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def update_azure_service_principal(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Add the client ID for a given tenant ID to the subscription.
 
         Keyword arguments:
         id -- Azure tentant ID. String. Required.
         client_id -- Azure client ID. String. Required.
         parameters - full parameters payload, not required if using other keywords.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/malquery.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/malquery.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._payload import malquery_fuzzy_payload, generic_payload_list
 from ._payload import malquery_exact_search_payload, malquery_hunt_payload
 from ._service_class import ServiceClass
 from ._endpoint._malquery import _malquery_endpoints as Endpoints
 
 
@@ -51,15 +52,15 @@
           "client_id": "CLIENT_ID_HERE",
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
-    def get_quotas(self: object) -> dict:
+    def get_quotas(self: object) -> Dict[str, Union[int, dict]]:
         """Get information about search and download quotas in your environment.
 
         This method does not accept arguments or keywords.
 
         Returns: dict object containing API response.
 
         HTTP Method: GET
@@ -70,15 +71,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetMalQueryQuotasV1"
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def fuzzy_search(self: object, body: dict = None, **kwargs) -> dict:
+    def fuzzy_search(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search Falcon MalQuery quickly, but with more potential for false positives.
 
         Search for a combination of hex patterns and strings in order to identify
         samples based upon file content at byte level granularity.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
@@ -149,15 +150,15 @@
             endpoints=Endpoints,
             operation_id="GetMalQueryDownloadV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_metadata(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_metadata(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve indexed files metadata by their hash.
 
         Keyword arguments:
         ids -- List of SHA256s to retrieve metadata for. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -175,15 +176,15 @@
             endpoints=Endpoints,
             operation_id="GetMalQueryMetadataV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_request(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_request(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Check the status and results of an asynchronous request, such as hunt or exact-search.
 
         Supports a single request id at this time.
 
         Keyword arguments:
         ids -- List of MalQuery identifiers to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -231,15 +232,15 @@
             endpoints=Endpoints,
             operation_id="GetMalQueryEntitiesSamplesFetchV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def samples_multidownload(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def samples_multidownload(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Schedule samples for download.
 
         Use the result id with the /request endpoint to check if the download is ready
         after which you can call get_samples to get the zip.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
@@ -270,15 +271,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PostMalQueryEntitiesSamplesMultidownloadV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def exact_search(self: object, body: dict = None, **kwargs) -> dict:
+    def exact_search(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Perform a MalQuery Exact Search.
 
         Search Falcon MalQuery for a combination of hex patterns
         and strings in order to identify samples based upon file content
         at byte level granularity. You can filter results on criteria such
         as file type, file size and first seen date.
 
@@ -336,15 +337,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PostMalQueryExactSearchV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def hunt(self: object, body: dict = None, **kwargs) -> dict:
+    def hunt(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Schedule a YARA-based search for execution.
 
         Returns a request id which can be used with the /request endpoint.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/message_center.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/message_center.py`

 * *Files 4% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import json
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list, aggregate_payload, activity_payload, case_payload
 from ._service_class import ServiceClass
 from ._endpoint._message_center import _message_center_endpoints as Endpoints
 
 
 class MessageCenter(ServiceClass):
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_cases(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_cases(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve aggregate case values based on the matched filter.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [{
                     "date_ranges": [
                         {
@@ -123,15 +124,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateCases",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_case_activity(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_case_activity(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve activities for given case IDs.
 
         Keyword arguments:
         body -- full body payload, not required if ids is provided as a keyword.
                 {
                     "ids": [
                         "string"
@@ -159,15 +160,15 @@
             endpoints=Endpoints,
             operation_id="GetCaseActivityByIds",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def add_case_activity(self: object, body: dict = None, **kwargs) -> dict:
+    def add_case_activity(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Add an activity to case. Only activities of type comment are allowed via API.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 NOTICE: This particular body payload contains a field named `body`, which
                         impacts body payload abstraction functionality. This field can be
                         set using the keyword `content` if you do not wish to specify a
@@ -232,15 +233,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def add_case_attachment(self: object,
                             file_data: object = None,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
-                            ) -> dict:
+                            ) -> Dict[str, Union[int, dict]]:
         """Upload an attachment for the case.
 
         Keyword arguments:
         case_id -- Case ID to attach to. String.
         file_data -- Content of the attachment in binary format. Max file size is 15 MB.
                      'sample' and 'upfile' are also accepted as this parameter.
                      Filename must start with [a-zA-Z0-9_-] and has a maximum of 255 characters.
@@ -280,15 +281,15 @@
             body=body,
             data=file_data,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_case(self: object, body: dict = None, **kwargs) -> dict:
+    def create_case(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a new case.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 NOTICE: This particular body payload contains a field named `body`, which
                         impacts body payload abstraction functionality. This field can be
                         set using the keyword `content` if you do not wish to specify a
@@ -335,15 +336,15 @@
             endpoints=Endpoints,
             operation_id="CreateCase",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_case(self: object, body: dict = None, **kwargs) -> dict:
+    def update_case(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update an existing case.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 NOTICE: This particular body payload contains a field named `body`, which
                         impacts body payload abstraction functionality. This field can be
                         set using the keyword `content` if you do not wish to specify a
@@ -386,15 +387,15 @@
             endpoints=Endpoints,
             operation_id="UpdateCase",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_cases(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_cases(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve message center cases.
 
         Keyword arguments:
         body -- full body payload, not required if ids is provided as a keyword.
                 {
                     "ids": [
                         "string"
@@ -423,15 +424,15 @@
             endpoints=Endpoints,
             operation_id="GetCaseEntitiesByIDs",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_activities(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_activities(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve activities IDs for a case.
 
         Keyword arguments:
         case_id -- Case ID to search for activities. String.
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   String.
         limit -- The maximum number of records to return. [integer, 1-500]
@@ -456,15 +457,15 @@
             endpoints=Endpoints,
             operation_id="QueryActivityByCaseID",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_cases(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_cases(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve case IDs that match the provided filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   String.
         limit -- The maximum number of records to return. [integer, 1-500]
         offset -- The integer offset to start retrieving records from. String.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ml_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ml_exclusions.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import exclusion_payload
 from ._service_class import ServiceClass
 from ._endpoint._ml_exclusions import _ml_exclusions_endpoints as Endpoints
 
 
 class MLExclusions(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a set of ML Exclusions by specifying their IDs.
 
         Keyword arguments:
         ids -- List of exclusion IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -77,15 +78,15 @@
             endpoints=Endpoints,
             operation_id="getMLExclusionsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def create_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def create_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create the ML exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "comment": "string",
                     "excluded_from": [
@@ -119,15 +120,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createMLExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103 # Matching API
+    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete the ML Exclusions by ID.
 
         Keyword arguments:
         comment -- Explains why this exclusions was deleted. String.
         ids -- List of exclusion IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -146,15 +147,15 @@
             endpoints=Endpoints,
             operation_id="deleteMLExclusionsV1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def update_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def update_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update the ML Exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "comment": "string",
                     "groups": [
@@ -186,15 +187,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateMLExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for ML Exclusions.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
                   AVAILABLE FILTERS
                   applied_globally            last_modified
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/mobile_enrollment.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/mobile_enrollment.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default
 from ._service_class import ServiceClass
 from ._endpoint._mobile_enrollment import _mobile_enrollment_endpoints as Endpoints
 
 
 class MobileEnrollment(ServiceClass):
     """This class represents the CrowdStrike Falcon Mobile Enrollment service collection.
@@ -52,15 +53,15 @@
               "client_secret": "CLIENT_SECRET_HERE"
           }
     - an `auth_object` containing a valid instance of the authentication service class (OAuth2)
     - a valid token provided by the token method of the authentication service class (OAuth2.token)
     """
 
     @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
-    def device_enroll(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def device_enroll(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Trigger on-boarding process for a mobile device.
 
         HTTP Method: POST
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mobile-enrollment/RequestDeviceEnrollmentV3
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/mssp.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/mssp.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=C0302,R0904  # Matching API operation counts
+from typing import Dict, Union
 from ._util import force_default, handle_single_argument, process_service_request
 from ._payload import generic_payload_list, mssp_payload
 from ._service_class import ServiceClass
 from ._endpoint._mssp import _mssp_endpoints as Endpoints
 
 
 class FlightControl(ServiceClass):
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_children(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_children(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get link to child customer by child CID(s).
 
         Keyword arguments:
         ids -- CID of a child customer. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -174,15 +175,15 @@
             endpoints=Endpoints,
             operation_id="getCIDGroupMembersBy",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def add_cid_group_members(self: object, body: dict = None, **kwargs) -> dict:
+    def add_cid_group_members(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Add new CID Group member.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -215,15 +216,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="addCIDGroupMembers",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def delete_cid_group_members(self: object, body: dict = None, **kwargs) -> dict:
+    def delete_cid_group_members(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete CID Group members entry.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -316,15 +317,15 @@
             endpoints=Endpoints,
             operation_id="getCIDGroupById",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_cid_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def create_cid_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create new CID Group(s). Maximum 500 CID Group(s) allowed.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -356,15 +357,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createCIDGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_cid_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_cid_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete CID Group(s) by ID(s).
 
         Keyword arguments:
         cid_group_ids -- CID group IDs to search for. String or list of strings.
         parameters -- full parameters payload, not required if `cid_group_ids` is provided
                       as a keyword.
 
@@ -383,15 +384,15 @@
             endpoints=Endpoints,
             operation_id="deleteCIDGroups",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cid_group_ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_cid_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def update_cid_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update existing CID Group(s).
 
         CID Group ID is expected for each CID Group definition provided in request body.
 
         CID Group member(s) remain unaffected.
 
         Keyword arguments:
@@ -427,15 +428,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateCIDGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_roles_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_roles_by_id(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get MSSP Role assignment(s).
 
         MSSP Role assignment is of the format <user_group_id>:<cid_group_id>.
 
         Keyword arguments:
         ids -- MSSP Role assignment is of the format <user_group_id>:<cid_group_id>.
                String or list of strings.
@@ -456,15 +457,15 @@
             endpoints=Endpoints,
             operation_id="getRolesByID",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def add_role(self: object, body: dict = None, **kwargs) -> dict:
+    def add_role(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Assign new MSSP Role(s) between User Group and CID Group.
 
         It does not revoke existing role(s) between User Group and CID Group.
         User Group ID and CID Group ID have to be specified in request.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
@@ -501,15 +502,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="addRole",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def delete_roles(self: object, body: dict = None, **kwargs) -> dict:
+    def delete_roles(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete MSSP Role assignment(s) between User Group and CID Group.
 
         User Group ID and CID Group ID have to be specified in request.
         Only specified roles are removed if specified in request payload,
         else association between User Group and CID Group is dissolved completely
         (if there are no roles specified).
 
@@ -585,15 +586,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_user_group_members_by_id(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
-                                     ) -> dict:
+                                     ) -> Dict[str, Union[int, dict]]:
         """Get User Group members by User Group ID(s).
 
         Keyword arguments:
         ids -- User group IDs to search for. String or list of strings.
                The keyword `user_group_ids` will also be accepted for this argument.
         parameters -- full parameters payload, not required if `user_group_ids` is provided
                       as a keyword.
@@ -616,15 +617,15 @@
             endpoints=Endpoints,
             operation_id="getUserGroupMembersByID",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def add_user_group_members(self: object, body: dict = None, **kwargs) -> dict:
+    def add_user_group_members(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Add new User Group member. Maximum 500 members allowed per User Group.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -654,15 +655,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="addUserGroupMembers",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def delete_user_group_members(self: object, body: dict = None, **kwargs) -> dict:
+    def delete_user_group_members(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete User Group members entry.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -752,15 +753,15 @@
             endpoints=Endpoints,
             operation_id="getUserGroupsByID",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_user_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def create_user_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create new User Group(s). Maximum 500 User Group(s) allowed per customer.
 
         Keyword arguments:
         body -- full body payload, not required if sha256 is provided as a keyword.
                 {
                     "resources": [
                         {
@@ -792,15 +793,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createUserGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_user_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_user_groups(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete User Group(s) by ID(s).
 
         Keyword arguments:
         user_group_ids -- User group IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if `user_group_ids` is provided
                       as a keyword.
 
@@ -819,15 +820,15 @@
             endpoints=Endpoints,
             operation_id="deleteUserGroups",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_group_ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_user_groups(self: object, body: dict = None, **kwargs) -> dict:
+    def update_user_groups(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update existing User Group(s).
 
         User Group ID is expected for each User Group definition provided in request body.
 
         User Group member(s) remain unaffected.
 
         Keyword arguments:
@@ -863,15 +864,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateUserGroups",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_children(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_children(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query for customers linked as children.
 
         Keyword arguments:
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Default: 10
         offset -- The offset to start retrieving records from. String.
                   Use with the limit parameter to manage pagination of results.
@@ -892,15 +893,15 @@
             endpoints=Endpoints,
             operation_id="queryChildren",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_cid_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_cid_group_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query a CID Groups members by associated CID.
 
         Keyword arguments:
         cid -- CID to lookup associated CID group ID
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Default: 10
         offset -- The offset to start retrieving records from. String.
@@ -922,15 +923,15 @@
             endpoints=Endpoints,
             operation_id="queryCIDGroupMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_cid_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_cid_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query a CID Groups.
 
         Keyword arguments:
         name -- Name to lookup groups for
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Default: 10
         offset -- The offset to start retrieving records from. String.
@@ -952,15 +953,15 @@
             endpoints=Endpoints,
             operation_id="queryCIDGroups",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_roles(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_roles(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query links between user groups and CID groups.
 
         At least one of CID Group ID or User Group ID should also be provided. Role ID is optional.
 
         Keyword arguments:
         user_group_id -- User group ID to fetch MSSP role for
         cid_group_id -- CID group ID to fetch MSSP role for
@@ -986,15 +987,15 @@
             endpoints=Endpoints,
             operation_id="queryRoles",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_user_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_user_group_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query User Group member by User UUID.
 
         Keyword arguments:
         user_uuid -- User UUID to lookup associated user group ID
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Default: 10
         offset -- The offset to start retrieving records from. String.
@@ -1016,15 +1017,15 @@
             endpoints=Endpoints,
             operation_id="queryUserGroupMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_user_groups(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_user_groups(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query User Groups.
 
         Keyword arguments:
         name -- Name to lookup groups for
         limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                  Use with the offset parameter to manage pagination of results. Default: 10
         offset -- The offset to start retrieving records from. String.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/oauth2.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/oauth2.py`

 * *Files 21% similar despite different names*

```diff
@@ -31,166 +31,199 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
-import time
+# pylint: disable=R0902,R0913
+from typing import Dict, Optional, Union
+from ._auth_object import FalconInterface
+from ._error import CannotRevokeToken
 from ._util import (
-    perform_request,
-    generate_b64cred,
     confirm_base_url,
-    generate_error_result,
-    autodiscover_region,
+    generate_ok_result,
     )
-from ._token_fail_reason import TokenFailReason
-from ._endpoint._oauth2 import _oauth2_endpoints as Endpoints
 
 
-class OAuth2:
-    """To create an instance of this class, you must pass your client_id and client_secret.
+class OAuth2(FalconInterface):
+    """OAuth2 Service Class.
 
-    OR a properly formatted dictionary containing your client_id and client_secret
-    for the key you wish to use to connect to the API.
+    To create an instance of this class you must provide either:
+        - your client_id and client_secret.
+        - a properly formatted dictionary containing your client_id and client_secret
+          Example:
+          {
+              "client_id": FALCON_CLIENT_ID,
+              "client_secret": FALCON_CLIENT_SECRET,
+              "member_cid": OPTIONAL_CHILD_CID
+          }
+        - a valid access_token
 
-    Credential dictionary example:
-    {
-        "client_id": FALCON_CLIENT_ID,
-        "client_secret": FALCON_CLIENT_SECRET
-    }
+    All other class constructor arguments are optional.
+
+    OAuth2 is the only Service Class that inherits directly from the FalconAuth object.
+    This means the OAuth2 class does not maintain an auth_object, as it is one.
     """
 
-    # pylint: disable=too-many-instance-attributes,too-many-arguments
-    def __init__(self: object, base_url: str = "https://api.crowdstrike.com",
-                 ssl_verify: bool = True, proxy: dict = None, timeout: float or tuple = None,
-                 creds: dict = None, client_id: str = None, client_secret: str = None,
-                 user_agent: str = None, member_cid: str = None, renew_window: int = 120):
-        """Class constructor.
+    def __init__(self,
+                 access_token: Optional[Union[str, bool]] = False,
+                 base_url: Optional[str] = "https://api.crowdstrike.com",
+                 ssl_verify: Optional[bool] = True,
+                 proxy: Optional[Dict[str, str]] = None,
+                 timeout: Optional[Union[float, tuple]] = None,
+                 creds: Optional[Dict[str, str]] = None,
+                 client_id: Optional[str] = None,
+                 client_secret: Optional[str] = None,
+                 user_agent: Optional[str] = None,
+                 member_cid: Optional[str] = None,
+                 renew_window: Optional[int] = 120,
+                 debug: Optional[bool] = False,
+                 debug_record_count: Optional[int] = None,
+                 sanitize_log: Optional[bool] = None,
+                 pythonic: Optional[bool] = None
+                 ):
+        """Construct an instance of the class.
 
         Initializes the base class by ingesting credentials,
-        the proxies dictionary and specifications
-        for the base URL, SSL verification, and timeouts.
+        the proxy dictionary and specifications for other attributes
+        such as the base URL, SSL verification, and timeout.
 
-        Keyword arguments:
-        base_url: CrowdStrike API URL to use for requests. [Default: US-1]
-        ssl_verify: Boolean specifying if SSL verification should be used. [Default: True]
-        proxy: Dictionary of proxies to be used for requests.
-        timeout: Float or tuple specifying timeouts to use for requests.
-        creds: Dictionary containing CrowdStrike API credentials.
-               Mutually exclusive to client_id / client_secret.
-        client_id: Client ID for the CrowdStrike API. Mutually exclusive to creds.
-        client_secret: Client Secret for the CrowdStrike API. Mutually exclusive to creds.
-        member_cid: Child CID to connect to. Mutually exclusive to creds.
-        renew_window: Amount of time (in seconds) between now and the token expiration before
-                      a refresh of the token is performed. Default: 120, Max: 1200
-                      Values over 1200 will be reset to the maximum.
+        Keyword arguments
+        ----
+        base_url : str
+            CrowdStrike API URL to use for requests. [Default: US-1]
+        ssl_verify : bool
+            Flag specifying if SSL verification should be used. [Default: True]
+        proxy : dict
+            Dictionary of proxies to be used for requests.
+        timeout : float or tuple
+            Value specifying timeouts to use for requests.
+        creds : dict
+            Dictionary containing CrowdStrike API credentials.
+            Mutually exclusive to client_id / client_secret.
+        client_id : str
+            Client ID for the CrowdStrike API. Mutually exclusive to creds.
+        client_secret : str
+            Client Secret for the CrowdStrike API. Mutually exclusive to creds.
+        member_cid : str
+            Child CID to connect to. Mutually exclusive to creds.
+        renew_window : int
+            Amount of time (in seconds) between now and the token expiration before
+            a refresh of the token is performed. Default: 120, Max: 1200
+            Values over 1200 will be reset to the maximum.
 
+        Arguments
+        ----
         This method only supports keywords to specify arguments.
-        """
-        if client_id and client_secret and not creds:
-            creds = {
-                "client_id": client_id,
-                "client_secret": client_secret
-            }
-            # Have to pass member_cid the same way you pass client_id / secret
-            # If you use a creds dictionary, pass the member_cid there instead
-            if member_cid:
-                creds["member_cid"] = member_cid
-        elif not creds:
-            creds = {}
-
-        self.creds = creds
-        self.base_url = confirm_base_url(base_url)
-        self.ssl_verify = ssl_verify
-        self.timeout = timeout
-        self.proxy = proxy
-        self.user_agent = user_agent
-        self.token_expiration = 0
-        # Maximum renewal window is 20 minutes, Minimum is 2 minutes
-        self.token_renew_window = max(min(renew_window, 1200), 120)
-        self.token_time = time.time()
-        self.token_value = False
-        self.token_expired = lambda: bool(
-            (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)
-            )
-        self.token_fail_reason = None
-        self.token_status = None
-        self.authenticated = lambda: not bool(self.token_expired())
-
-    def token(self: object) -> dict:
-        """Generate an authorization token.
-
-        This method does not accept arguments or keywords.
 
-        Returns: dict object containing API response.
+        Returns
+        ----
+        class (OAuth2)
+            A constructed instance of the OAuth2 Service Class.
+        """
+        super().__init__(base_url=confirm_base_url(base_url),
+                         ssl_verify=ssl_verify,
+                         timeout=timeout,
+                         proxy=proxy,
+                         user_agent=user_agent,
+                         access_token=access_token,
+                         creds=creds,
+                         client_id=client_id,
+                         client_secret=client_secret,
+                         member_cid=member_cid,             # |
+                         renew_window=renew_window,         # /\
+                         debug=debug,                      # |o
+                         debug_record_count=debug_record_count,
+                         sanitize_log=sanitize_log,
+                         pythonic=pythonic
+                         )
+
+    def logout(self) -> Dict[str, Union[int, dict]]:
+        """Revoke the current token.
+
+        Keyword arguments
+        ----
+        This method does not accept keyword arguments.
+
+        Arguments
+        ----
+        This method does not accept arguments.
+
+        Returns
+        ----
+        dict
+            Dictionary object containing API response.
         """
-        operation_id = "oauth2AccessToken"
-        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
-        header_payload = {}
-        if "client_id" in self.creds and "client_secret" in self.creds:
-            data_payload = {
-                'client_id': self.creds['client_id'],
-                'client_secret': self.creds['client_secret']
-            }
-            if "member_cid" in self.creds:
-                data_payload["member_cid"] = self.creds["member_cid"]
-            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
-                                       headers=header_payload, verify=self.ssl_verify,
-                                       proxy=self.proxy, timeout=self.timeout,
-                                       user_agent=self.user_agent)
-            if isinstance(returned, dict):  # Issue #433
-                self.token_status = returned["status_code"]
-                if self.token_status == 201:
-                    self.token_expiration = returned["body"]["expires_in"]
-                    self.token_time = time.time()
-                    self.token_value = returned["body"]["access_token"]
-                    self.token_fail_reason = None
-                    self.base_url = autodiscover_region(self.base_url, returned)
-                else:
-                    if "errors" in returned["body"]:
-                        if returned["body"]["errors"]:
-                            self.token_fail_reason = returned["body"]["errors"][0]["message"]
+        try:
+            returned: dict = super().logout()
+            if returned["status_code"] == 200:
+                returned = generate_ok_result(message="Current token successfully revoked.",
+                                              headers=returned["headers"]
+                                              )
             else:
-                returned = generate_error_result("Unexpected API response received", 403)
-                self.token_fail_reason = TokenFailReason["UNEXPECTED"].value
-                self.token_status = 403
-        else:
-            returned = generate_error_result("Invalid credentials specified", 403)
-            self.token_fail_reason = TokenFailReason["INVALID"].value
-            self.token_status = 403
+                raise CannotRevokeToken(returned["status_code"], returned["body"]["errors"][0]["message"], returned["headers"])
+        except CannotRevokeToken as unable_to_revoke:
+            if self.log:
+                self.log.warning("Token revocation operation failed.")
+            returned = unable_to_revoke.result
 
         return returned
 
-    def revoke(self: object, token: str) -> dict:
+    def revoke(self, token: str, alter_state: bool = False) -> Dict[str, Union[int, dict]]:
         """Revoke the specified authorization token.
 
-        Keyword arguments:
-        token: Token string to be revoked.
+        HTTP Method: POST
 
+        Swagger URL
+        ----
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2/oauth2RevokeToken
+
+        Keyword arguments
+        ----
+        token : str
+            Token string to be revoked.
+        alter_state : bool
+            Flag indicating if the underlying authentication state is changed by this request.
+
+        Arguments
+        ----
         When not specified as a keyword, token is assumed as the only accepted argument.
 
-        Returns: dict object containing API response.
+        Returns
+        ----
+        dict
+            Dictionary containing API response.
         """
-        operation_id = "oauth2RevokeToken"
-        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
-        if "client_id" in self.creds and "client_secret" in self.creds:
-            b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
-            header_payload = {"Authorization": f"basic {b64cred}"}
-            data_payload = {"token": f"{token}"}
-            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
-                                       headers=header_payload, verify=self.ssl_verify,
-                                       proxy=self.proxy, timeout=self.timeout,
-                                       user_agent=self.user_agent)
-            self.token_expiration = 0
-            self.token_value = False
-        else:
-            returned = generate_error_result("Invalid credentials specified", 403)
+        return self._logout_handler(token, not alter_state)
 
-        return returned
+    def token(self, alter_state: bool = False) -> Dict[str, Union[int, dict]]:
+        """Generate an authorization token.
+
+        HTTP Method: POST
+
+        Swagger URL
+        ----
+        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2/oauth2AccessToken
+
+        Keyword arguments
+        ----
+        alter_state : bool
+            Flag indicating if the underlying authentication state is changed by this request.
+
+        Arguments
+        ----
+        When not specified as a keyword, alter_state is assumed as the only accepted argument.
+
+        Returns
+        ----
+        dict
+            Dictionary object containing API response.
+        """
+        return self._login_handler(not alter_state)
 
     # These method names align to the operation IDs in the API but
     # do not conform to snake_case / PEP8 and are defined here for
     # backwards compatibility / ease of use purposes
     oauth2AccessToken = token
     oAuth2AccessToken = token
     oauth2RevokeToken = revoke
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/ods.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/ods.py`

 * *Files 1% similar despite different names*

```diff
@@ -36,15 +36,14 @@
 For more information, please refer to <https://unlicense.org>
 """
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import (
     generic_payload_list,
     aggregate_payload,
     scheduled_scan_payload,
-    scans_report_payload
     )
 from ._service_class import ServiceClass
 from ._endpoint._ods import _ods_endpoints as Endpoints
 
 
 class ODS(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -278,55 +277,56 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="get_scan_host_metadata_by_ids",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
-    @force_default(defaults=["body"], default_types=["dict"])
-    def scans_report(self: object, body: dict = None, **kwargs) -> dict:
-        """Launch a scans report creation job.
-
-        Keyword arguments:
-        body -- full body payload, not required if ids is provided as a keyword.
-                {
-                    "is_schedule": true,
-                    "report_format": "string",
-                    "search": {
-                        "filter": "string",
-                        "sort": "string"
-                    }
-                }
-        is_schedule -- Flag indicating if this report is scheduled. Boolean.
-        filter -- FQL filter to filter the report. String. Overrides the value within
-                  the search dictionary if provided. String.
-        report_format -- Format for the report. String.
-        search -- Filter the report results. Dictionary.
-        sort -- FQL sort string to use within the report. Overrides the value within
-                the search dictionary if provided. String.
-
-        This method only supports keywords for providing arguments.
-
-        Returns: dict object containing API response.
-
-        HTTP Method: POST
-
-        Swagger URL
-        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/scans-report
-        """
-        if not body:
-            body = scans_report_payload(passed_keywords=kwargs)
-
-        return process_service_request(
-            calling_object=self,
-            endpoints=Endpoints,
-            operation_id="scans_report",
-            keywords=kwargs,
-            body=body
-            )
+    # This operation is no longer available
+    # @force_default(defaults=["body"], default_types=["dict"])
+    # def scans_report(self: object, body: dict = None, **kwargs) -> dict:
+    #     """Launch a scans report creation job.
+
+    #     Keyword arguments:
+    #     body -- full body payload, not required if ids is provided as a keyword.
+    #             {
+    #                 "is_schedule": true,
+    #                 "report_format": "string",
+    #                 "search": {
+    #                     "filter": "string",
+    #                     "sort": "string"
+    #                 }
+    #             }
+    #     is_schedule -- Flag indicating if this report is scheduled. Boolean.
+    #     filter -- FQL filter to filter the report. String. Overrides the value within
+    #               the search dictionary if provided. String.
+    #     report_format -- Format for the report. String.
+    #     search -- Filter the report results. Dictionary.
+    #     sort -- FQL sort string to use within the report. Overrides the value within
+    #             the search dictionary if provided. String.
+
+    #     This method only supports keywords for providing arguments.
+
+    #     Returns: dict object containing API response.
+
+    #     HTTP Method: POST
+
+    #     Swagger URL
+    #     https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/scans-report
+    #     """
+    #     if not body:
+    #         body = scans_report_payload(passed_keywords=kwargs)
+
+    #     return process_service_request(
+    #         calling_object=self,
+    #         endpoints=Endpoints,
+    #         operation_id="scans_report",
+    #         keywords=kwargs,
+    #         body=body
+    #         )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_scans(self: object, *args, parameters: dict = None, **kwargs) -> dict:
         """Get scans by IDs.
 
         Keyword arguments:
         ids -- The scan IDs to retrieve. String or list of strings.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/overwatch_dashboard.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/overwatch_dashboard.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, handle_single_argument, process_service_request
 from ._payload import aggregate_payload
 from ._service_class import ServiceClass
 from ._endpoint._overwatch_dashboard import _overwatch_dashboard_endpoints as Endpoints
 
 
 class OverwatchDashboard(ServiceClass):
@@ -55,15 +56,15 @@
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def aggregates_detections_global_counts(self: object,
                                             *args,
                                             parameters: dict = None,
                                             **kwargs
-                                            ) -> dict:
+                                            ) -> Dict[str, Union[int, dict]]:
         """Get the total number of detections pushed across all customers.
 
         Keyword arguments:
         filter -- FQL filter to limit the results. String.
         parameters -- full parameters payload, not required if filter is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -81,15 +82,15 @@
             endpoints=Endpoints,
             operation_id="AggregatesDetectionsGlobalCounts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "filter")
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregates_events_collections(self: object, body: list = None, **kwargs) -> dict:
+    def aggregates_events_collections(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get OverWatch detection event collection info by providing an aggregate query.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -157,15 +158,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregatesEventsCollections",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregates_events(self: object, body: list = None, **kwargs) -> dict:
+    def aggregates_events(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get aggregate OverWatch detection event info by providing an aggregate query.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 List of dictionaries.
                 [{
                     "date_ranges": [
@@ -237,15 +238,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def aggregates_incidents_global_counts(self: object,
                                            *args,
                                            parameters: dict = None,
                                            **kwargs
-                                           ) -> dict:
+                                           ) -> Dict[str, Union[int, dict]]:
         """Get the total number of incidents pushed across all customers.
 
         Keyword arguments:
         filter -- FQL filter to limit the results. String.
         parameters -- full parameters payload, not required if filter is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -267,15 +268,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def aggregates_events_global_counts(self: object,
                                         *args,
                                         parameters: dict = None,
                                         **kwargs
-                                        ) -> dict:
+                                        ) -> Dict[str, Union[int, dict]]:
         """Get the total number of incidents pushed across all customers.
 
         Keyword arguments:
         filter -- FQL filter to limit the results. String.
         parameters -- full parameters payload, not required if filter is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/prevention_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/prevention_policy.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, handle_single_argument, process_service_request
 from ._payload import generic_payload_list, prevention_policy_payload
 from ._service_class import ServiceClass
 from ._endpoint._prevention_policies import _prevention_policies_endpoints as Endpoints
 
 
 class PreventionPolicy(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Prevention Policy by providing an FQL filter and paging details.
 
         Returns a set of host details which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Prevention Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -85,15 +86,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedPreventionPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Prevention Policies by providing an FQL filter and paging details.
 
         Returns a set of Prevention Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -126,15 +127,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def perform_policies_action(self: object,
                                 body: dict = None,
                                 parameters: dict = None,
                                 **kwargs
-                                ) -> dict:
+                                ) -> Dict[str, Union[int, dict]]:
         """Perform the specified action on the Prevention Policies specified in the request.
 
         Keyword arguments:
         action_name -- action to perform: 'add-host-group', 'add-rule-group', 'disable',
                        'enable', 'remove-host-group', or 'remove-rule-group'.
         action_parameters -- Action specific parameter options. List of dictionaries.
                              {
@@ -185,15 +186,15 @@
             operation_id="performPreventionPoliciesAction",
             keywords=kwargs,
             params=parameters,
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> dict:
+    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Set the precedence of Prevention Policies based on the order of IDs in the request.
 
         The first ID specified will have the highest precedence and the last ID specified will
         have the lowest. You must specify all non-Default Policies for a platform when updating
         precedence.
 
         Keyword arguments:
@@ -226,15 +227,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="setPreventionPoliciesPrecedence",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Prevention Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Prevention Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -252,15 +253,15 @@
             endpoints=Endpoints,
             operation_id="getPreventionPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def create_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Prevention Policies by specifying details about the policy to create.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -304,15 +305,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createPreventionPolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Prevention Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Prevention Policy IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -330,15 +331,15 @@
             endpoints=Endpoints,
             operation_id="deletePreventionPolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Prevention Policies by specifying the ID of the policy and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -379,15 +380,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updatePreventionPolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Prevention Policy by providing a FQL filter and paging details.
 
         Returns a set of Agent IDs which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Prevention Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -413,15 +414,15 @@
             endpoints=Endpoints,
             operation_id="queryPreventionPolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Prevention Policies by providing an FQL filter and paging details.
 
         Returns a set of Prevention Policy IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/quarantine.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/quarantine.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list, aggregate_payload
 from ._service_class import ServiceClass
 from ._endpoint._quarantine import _quarantine_endpoints as Endpoints
 
 
 class Quarantine(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def action_update_count(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def action_update_count(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Return the count of potentially affected quarantined files for each action.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
         parameters - full parameters payload, not required if using other keywords.
 
@@ -78,15 +79,15 @@
             endpoints=Endpoints,
             operation_id="ActionUpdateCount",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "filter")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_aggregate_files(self: object, body: dict = None, **kwargs) -> dict:
+    def get_aggregate_files(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get quarantine file aggregates as specified via json in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "date_ranges": [
@@ -148,15 +149,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetAggregateFiles",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_quarantine_files(self: object, body: dict = None, **kwargs) -> dict:
+    def get_quarantine_files(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get quarantine file metadata for specified ids.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "ids": [
                         "string"
@@ -183,15 +184,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetQuarantineFiles",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_quarantined_detects_by_id(self: object, body: dict = None, **kwargs) -> dict:
+    def update_quarantined_detects_by_id(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Apply action by quarantine file ids.
 
         Keyword arguments:
         action -- Action to perform against the quarantined file. String.
                   Allowed values: 'release', 'unrelease', 'delete'
         comment -- Comment to list along with action taken. String.
         body -- full body payload, not required when using other keywords.
@@ -226,15 +227,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateQuarantinedDetectsByIds",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_quarantine_files(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_quarantine_files(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get quarantine file ids that match the provided filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Special value '*' means to not filter on anything.
                   Available filters
                   adversary_id                  behaviors.username
@@ -282,15 +283,15 @@
             endpoints=Endpoints,
             operation_id="QueryQuarantineFiles",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def update_quarantined_detects_by_query(self: object, body: dict = None, **kwargs) -> dict:
+    def update_quarantined_detects_by_query(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Apply quarantine file actions by query.
 
         Keyword arguments:
         action -- Action to perform against the quarantined file. String.
                   Allowed values: 'release', 'unrelease', 'delete'
         comment -- Comment to list along with action taken. String.
         body -- full body payload, not required when using other keywords.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/quick_scan.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/quick_scan.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list, aggregate_payload
 from ._service_class import ServiceClass
 from ._endpoint._quick_scan import _quick_scan_endpoints as Endpoints
 
 
 class QuickScan(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_scans_aggregates(self: object, body: dict = None, **kwargs) -> dict:
+    def get_scans_aggregates(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get scans aggregations as specified via json in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "date_ranges": [
                         {
@@ -121,15 +122,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetScansAggregates",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_scans(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_scans(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Check the status of a volume scan.
 
         Time required for analysis increases with the number of samples in a volume
         but usually it should take less than 1 minute.
 
         Keyword arguments:
         ids -- One or more remediation IDs. String or list of strings.
@@ -150,15 +151,15 @@
             endpoints=Endpoints,
             operation_id="GetScans",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def scan_samples(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def scan_samples(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get scans aggregations as specified via json in request body.
 
         Keyword arguments:
         body -- full body payload, not required when samples keyword is provided.
                 {
                     "samples": [
                         "string"
@@ -189,15 +190,15 @@
             operation_id="ScanSamples",
             body=body,
             body_validator={"samples": list} if self.validate_payloads else None,
             body_required=["samples"] if self.validate_payloads else None
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_submissions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_submissions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find IDs for submitted scans by providing an FQL filter and paging details.
 
         Returns a set of volume IDs that match your criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return. [integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/real_time_response.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/real_time_response.py`

 * *Files 6% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=R0904  # Aligning method count to API service collection operation count
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import aggregate_payload, command_payload, generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._real_time_response import _real_time_response_endpoints as Endpoints
 
 
 class RealTimeResponse(ServiceClass):
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_sessions(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_sessions(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get aggregates on session data.
 
         Supported aggregations:
             date_range
             term
 
         Keyword arguments:
@@ -136,15 +137,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def batch_active_responder_command(self: object,
                                        body: dict = None,
                                        parameters: dict = None,
                                        **kwargs
-                                       ) -> dict:
+                                       ) -> Dict[str, Union[int, dict]]:
         """Batch executes a RTR active-responder command across hosts mapped to a given batch ID.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "batch_id": "string",
@@ -191,15 +192,15 @@
             operation_id="BatchActiveResponderCmd",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def batch_command(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def batch_command(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Batch executes a RTR read-only command across the hosts mapped to the given batch ID.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "batch_id": "string",
@@ -246,15 +247,15 @@
             operation_id="BatchCmd",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def batch_get_command_status(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def batch_get_command_status(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve the status of the specified batch get command.
 
         Will return successful files when they are finished processing.
 
         Keyword arguments:
         timeout -- Timeout for how long to wait for the request in seconds.
                    Default timeout: 30 seconds  Max timeout: 10 minutes
@@ -283,15 +284,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def batch_get_command(self: object,
                           body: dict = None,
                           parameters: dict = None,
                           **kwargs
-                          ) -> dict:
+                          ) -> Dict[str, Union[int, dict]]:
         """Batch executes `get` command across hosts to retrieve files.
 
         After this call is made batch_get_command_status is used to query for the results.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
@@ -339,15 +340,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def batch_init_sessions(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
-                            ) -> dict:
+                            ) -> Dict[str, Union[int, dict]]:
         """Batch initialize a RTR session on multiple hosts.
 
         Before any RTR commands can be used, an active session is needed on the host.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
@@ -396,15 +397,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def batch_refresh_sessions(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
-                               ) -> dict:
+                               ) -> Dict[str, Union[int, dict]]:
         """Batch refresh a RTR session on multiple hosts.
 
         RTR sessions will expire after 10 minutes unless refreshed.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
@@ -445,15 +446,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def check_active_responder_command_status(self: object,
                                               *args,
                                               parameters: dict = None,
                                               **kwargs
-                                              ) -> dict:
+                                              ) -> Dict[str, Union[int, dict]]:
         """Get status of an executed active-responder command on a single host.
 
         Keyword arguments:
         cloud_request_id -- Cloud Request ID of the executed command to query.
         sequence_id -- Sequence ID that we want to retrieve. Command responses are
                        chunked across sequences. Default value: 0
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -477,15 +478,15 @@
             endpoints=Endpoints,
             operation_id="RTR_CheckActiveResponderCommandStatus",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cloud_request_id")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def execute_active_responder_command(self: object, body: dict = None, **kwargs) -> dict:
+    def execute_active_responder_command(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Execute an active responder command on a single host.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "command_string": "string",
@@ -519,15 +520,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_ExecuteActiveResponderCommand",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def check_command_status(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def check_command_status(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get status of an executed command on a single host.
 
         Keyword arguments:
         cloud_request_id -- Cloud Request ID of the executed command to query.
         sequence_id -- Sequence ID that we want to retrieve. Command responses are
                        chunked across sequences. Default value: 0
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -550,15 +551,15 @@
             endpoints=Endpoints,
             operation_id="RTR_CheckCommandStatus",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cloud_request_id")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def execute_command(self: object, body: dict = None, **kwargs) -> dict:
+    def execute_command(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Execute a command on a single host.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "command_string": "string",
@@ -592,15 +593,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_ExecuteCommand",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_extracted_file_contents(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_extracted_file_contents(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get RTR extracted file contents for specified session and sha256.
 
         Keyword arguments:
         session_id -- RTR Session ID. String.
         sha256 -- Extracted SHA256 value. String.
         filename -- Filename to use for the archive name and the file within the archive. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -620,15 +621,15 @@
             endpoints=Endpoints,
             operation_id="RTR_GetExtractedFileContents",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_files(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def list_files(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a list of files for the specified RTR session.
 
         Keyword arguments:
         session_id -- RTR Session ID. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -646,15 +647,15 @@
             endpoints=Endpoints,
             operation_id="RTR_ListFiles",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "session_id")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_files_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def list_files_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a list of files for the specified RTR session.
 
         Keyword arguments:
         session_id -- RTR Session ID. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -672,15 +673,15 @@
             endpoints=Endpoints,
             operation_id="RTR_ListFilesV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "session_id")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_file(self: object, parameters: dict = None, **kwargs) -> dict:
+    def delete_file(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a RTR session file.
 
         Keyword arguments:
         ids -- RTR Session file ID. String.
         session_id -- RTR Session ID. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -698,15 +699,15 @@
             endpoints=Endpoints,
             operation_id="RTR_DeleteFile",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_file_v2(self: object, parameters: dict = None, **kwargs) -> dict:
+    def delete_file_v2(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a RTR session file.
 
         Keyword arguments:
         ids -- RTR Session file ID. String.
         session_id -- RTR Session ID. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -724,15 +725,15 @@
             endpoints=Endpoints,
             operation_id="RTR_DeleteFileV2",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def pulse_session(self: object, body: dict = None, **kwargs) -> dict:
+    def pulse_session(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Refresh a session timeout on a single host.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "device_id": "string",
                     "origin": "string",
@@ -759,15 +760,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_PulseSession",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def list_sessions(self: object, body: dict = None, **kwargs) -> dict:
+    def list_sessions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get session metadata by session id.
 
         Keyword arguments:
         body -- full body payload, not required if ids are provided as keyword.
                 {
                     "ids": [
                         "string"
@@ -793,15 +794,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_ListSessions",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def list_queued_sessions(self: object, body: dict = None, **kwargs) -> dict:
+    def list_queued_sessions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get session metadata by session id.
 
         Keyword arguments:
         body -- full body payload, not required if ids are provided as keyword.
                 {
                     "ids": [
                         "string"
@@ -827,15 +828,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_ListQueuedSessions",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def init_session(self: object, body: dict = None, **kwargs) -> dict:
+    def init_session(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Initialize a new session with the RTR cloud.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "device_id": "string",
                     "origin": "string",
@@ -867,15 +868,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_InitSession",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_session(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_session(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a session.
 
         Keyword arguments:
         session_id -- RTR Session ID to delete. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be
@@ -894,15 +895,15 @@
             operation_id="RTR_DeleteSession",
 
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "session_id")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_queued_session(self: object, parameters: dict = None, **kwargs) -> dict:
+    def delete_queued_session(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a queued session.
 
         Keyword arguments:
         cloud_request_id -- Cloud Request ID of the executed command to query. String.
         session_id -- RTR Session ID to delete. String.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -920,15 +921,15 @@
             endpoints=Endpoints,
             operation_id="RTR_DeleteQueuedSession",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_all_sessions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def list_all_sessions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a list of session_ids.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   “user_id” can accept a special value `@me` which will restrict results to
                   records with current user’s ID.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/real_time_response_admin.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/real_time_response_admin.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import command_payload, data_payload
 from ._service_class import ServiceClass
 from ._endpoint._real_time_response_admin import _real_time_response_admin_endpoints as Endpoints
 
 
 class RealTimeResponseAdmin(ServiceClass):
@@ -55,15 +56,15 @@
     """
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def batch_admin_command(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
-                            ) -> dict:
+                            ) -> Dict[str, Union[int, dict]]:
         """Batch executes a RTR administrator command across the hosts mapped to a given batch ID.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "batch_id": "string",
@@ -110,15 +111,15 @@
             operation_id="BatchAdminCmd",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def check_admin_command_status(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def check_admin_command_status(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get status of an executed RTR administrator command on a single host.
 
         Keyword arguments:
         cloud_request_id -- Cloud Request ID of the executed command to query.
         sequence_id -- Sequence ID that we want to retrieve. Command responses are
                        chunked across sequences. Default value: 0
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -142,15 +143,15 @@
             endpoints=Endpoints,
             operation_id="RTR_CheckAdminCommandStatus",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "cloud_request_id")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def execute_admin_command(self: object, body: dict = None, **kwargs) -> dict:
+    def execute_admin_command(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Execute a RTR administrator command on a single host.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "base_command": "string",
                     "command_string": "string",
@@ -185,15 +186,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RTR_ExecuteAdminCommand",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_put_files(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_put_files(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get put-files based on the ID's given. These are used for the RTR `put` command.
 
         Keyword arguments:
         ids -- List of File IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -211,15 +212,15 @@
             endpoints=Endpoints,
             operation_id="RTR_GetPut_Files",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_put_files_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_put_files_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get put-files based on the ID's given. These are used for the RTR `put` command.
 
         Keyword arguments:
         ids -- List of File IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -237,15 +238,15 @@
             endpoints=Endpoints,
             operation_id="RTR_GetPut_FilesV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["data"], default_types=["dict"])
-    def create_put_files(self: object, files: list, data: dict = None, **kwargs) -> dict:
+    def create_put_files(self: object, files: list, data: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Upload a new put-file to use for the RTR `put` command.
 
         Keyword arguments:
         data -- full formData payload, not required if other keywords are used.
                 {
                     "description": "string",
                     "name": "string",
@@ -274,15 +275,15 @@
             endpoints=Endpoints,
             operation_id="RTR_CreatePut_Files",
             data=data,
             files=files
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_put_files(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_put_files(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a put-file based on the ID given. Can only delete one file at a time.
 
         Keyword arguments:
         ids -- File ID to delete. String. Only one file can be deleted per request.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -300,15 +301,15 @@
             endpoints=Endpoints,
             operation_id="RTR_DeletePut_Files",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_scripts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get custom-scripts based on the ID's given.
 
         These are used for the RTR `runscript` command.
 
         Keyword arguments:
         ids -- List of Script IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -328,15 +329,15 @@
             endpoints=Endpoints,
             operation_id="RTR_GetScripts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_scripts_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_scripts_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get custom-scripts based on the ID's given.
 
         These are used for the RTR `runscript` command.
 
         Keyword arguments:
         ids -- List of Script IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -356,15 +357,15 @@
             endpoints=Endpoints,
             operation_id="RTR_GetScriptsV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["data", "files"], default_types=["dict", "list"])
-    def create_scripts(self: object, data: dict = None, files: list = None, **kwargs) -> dict:
+    def create_scripts(self: object, data: dict = None, files: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Upload a new custom-script to use for the RTR `runscript` command.
 
         Keyword arguments:
         data -- full formData payload, not required if other keywords are used.
                 {
                     "description": "string",
                     "name": "string",
@@ -404,15 +405,15 @@
             endpoints=Endpoints,
             operation_id="RTR_CreateScripts",
             data=data,
             files=files
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_scripts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a custom-script based on the ID given. Can only delete one script at a time.
 
         Keyword arguments:
         ids -- Script ID to delete. String. Only one file can be deleted per request.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -430,15 +431,15 @@
             endpoints=Endpoints,
             operation_id="RTR_DeleteScripts",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["data", "files"], default_types=["dict", "list"])
-    def update_scripts(self: object, data: dict = None, files: list = None, **kwargs) -> dict:
+    def update_scripts(self: object, data: dict = None, files: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Upload a new scripts to replace an existing one.
 
         Keyword arguments:
         data -- full formData payload, not required if other keywords are used.
                 {
                     "id": "string",
                     "description": "string",
@@ -480,15 +481,15 @@
             endpoints=Endpoints,
             operation_id="RTR_UpdateScripts",
             data=data,
             files=files
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_put_files(self: object, parameters: dict = None, **kwargs) -> dict:
+    def list_put_files(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a list of put-file ID's that are available to the user for the `put` command.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. Integer.
@@ -510,15 +511,15 @@
             endpoints=Endpoints,
             operation_id="RTR_ListPut_Files",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def list_scripts(self: object, parameters: dict = None, **kwargs) -> dict:
+    def list_scripts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a list of custom-script ID's that are available for the `runscript` command.
 
         Only displays scripts the user has permissions to access.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/recon.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/recon.py`

 * *Files 3% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=C0302,R0904
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._payload import (
     recon_rules_payload,
     recon_notifications_payload,
     recon_action_payload,
     recon_action_update_payload,
     recon_rule_preview_payload,
@@ -131,15 +132,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateNotificationsExposedDataRecordsV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def aggregate_notifications(self: object, body: list = None, **kwargs) -> dict:
+    def aggregate_notifications(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get notification aggregates as specified via JSON in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "date_ranges": [
@@ -202,15 +203,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="AggregateNotificationsV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def preview_rule(self: object, body: dict = None, **kwargs) -> dict:
+    def preview_rule(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get notification aggregates as specified via JSON in request body.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "filter": "string",
                     "topic": "string"
@@ -234,15 +235,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="PreviewRuleV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_actions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_actions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get actions based on their IDs. IDs can be retrieved using the GET query_actions.
 
         Keyword arguments:
         ids -- List of action IDs to retrieve details for. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -260,15 +261,15 @@
             endpoints=Endpoints,
             operation_id="GetActionsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_actions(self: object, body: dict = None, **kwargs) -> dict:
+    def create_actions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create actions for a monitoring rule.
 
         Accepts a list of actions that will be attached to the monitoring rule.
 
         Keyword arguments:
         actions -- List of actions to attach to the monitoring rule.
                    When provided, actions overrides other passed keywords excluding body.
@@ -316,15 +317,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateActionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_action(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_action(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete an action from a monitoring rule based on the action ID.
 
         Keyword arguments:
         ids -- List of action IDs to delete. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -342,15 +343,15 @@
             endpoints=Endpoints,
             operation_id="DeleteActionV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_action(self: object, body: dict = None, **kwargs) -> dict:
+    def update_action(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update an action for a monitoring rule.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 {
                     "frequency": "string",
                     "id": "string",
@@ -514,15 +515,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_notifications_detailed_translated(self: object,
                                               *args,
                                               parameters: dict = None,
                                               **kwargs
-                                              ) -> dict:
+                                              ) -> Dict[str, Union[int, dict]]:
         """Get detailed notifications based on their IDs.
 
         These include the raw intelligence content that generated the match.
         This endpoint will return translated notification content.
         The only target language available is English.
         A single notification can be translated per request
 
@@ -545,15 +546,15 @@
             endpoints=Endpoints,
             operation_id="GetNotificationsDetailedTranslatedV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_notifications_detailed(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_notifications_detailed(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get detailed notifications based on their IDs.
 
         These include the raw intelligence content that generated the match.
 
         Keyword arguments:
         ids -- List of notification IDs to retrieve details for. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -603,15 +604,15 @@
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_notifications_translated(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
-                                     ) -> dict:
+                                     ) -> Dict[str, Union[int, dict]]:
         """Get notifications based on their IDs.
 
         IDs can be retrieved using query_notifications.
         This endpoint will return translated notification content.
         The only target language available is English.
 
         Keyword arguments:
@@ -633,15 +634,15 @@
             endpoints=Endpoints,
             operation_id="GetNotificationsTranslatedV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_notifications(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get notifications based on their IDs.
 
         IDs can be retrieved using get_notifications.
 
         Keyword arguments:
         ids -- List of notification IDs to retrieve details for. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -661,15 +662,15 @@
             endpoints=Endpoints,
             operation_id="GetNotificationsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_notifications(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete notifications based on IDs.
 
         Notifications cannot be recovered after they are deleted.
 
         Keyword arguments:
         ids -- List of notification IDs to retrieve details for. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
@@ -689,15 +690,15 @@
             endpoints=Endpoints,
             operation_id="DeleteNotificationsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def update_notifications(self: object, body: list = None, **kwargs) -> dict:
+    def update_notifications(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update notification status or assignee. Accepts bulk requests.
 
         Keyword arguments:
         assigned_to_uuid - UUID of the assigned user. String.
         body -- full body payload, not required when using other keywords.
                 [
                     {
@@ -727,15 +728,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateNotificationsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get monitoring rules rules by provided IDs.
 
         Keyword arguments:
         ids -- List of rule IDs to retrieve details for. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -753,15 +754,15 @@
             endpoints=Endpoints,
             operation_id="GetRulesV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["list"])
-    def create_rules(self: object, body: list = None, **kwargs) -> dict:
+    def create_rules(self: object, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create monitoring rules.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "filter": "string",
@@ -795,15 +796,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateRulesV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_rules(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete monitoring rules.
 
         Keyword arguments:
         ids -- List of rule IDs to delete. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -821,15 +822,15 @@
             endpoints=Endpoints,
             operation_id="DeleteRulesV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_rules(self: object, body: dict = None, **kwargs) -> dict:
+    def update_rules(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update monitoring rules.
 
         Keyword arguments:
         body -- full body payload, not required when using other keywords.
                 [
                     {
                         "filter": "string",
@@ -863,15 +864,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="UpdateRulesV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_actions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_actions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query actions based on provided criteria.
 
         Use the IDs from this response to get the action entities with get_actions.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filters
@@ -962,15 +963,15 @@
             endpoints=Endpoints,
             operation_id="QueryNotificationsExposedDataRecordsV1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_notifications(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_notifications(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query notifications based on provided criteria.
 
         Use the IDs from this response to get the notification
         entities with get_notifications or get_notifications detailed.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -1002,15 +1003,15 @@
             endpoints=Endpoints,
             operation_id="QueryNotificationsV1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query monitoring rules based on provided criteria.
 
         Use the IDs from this response to fetch the rules with get_rules.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Available filters
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/report_executions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/report_executions.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import reports_payload
 from ._service_class import ServiceClass
 from ._endpoint._report_executions import _report_executions_endpoints as Endpoints
 
 
 class ReportExecutions(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_download(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_download(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get report entity download.
 
         Keyword arguments:
         ids -- ID of the report entity to retrieve.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -76,16 +77,16 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="report_executions_download_get",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
-    @force_default(defaults=["body"], default_types=["dict"])
-    def retry_reports(self: object, *args, body: dict = None, **kwargs) -> dict:
+    @force_default(defaults=["body"], default_types=["list"])
+    def retry_reports(self: object, *args, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retries a report execution.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 [
                     {
                         "id": "string"
@@ -110,15 +111,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="report_executions_retry",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_reports(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_reports(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve report details for the provided report IDs.
 
         Keyword arguments:
         ids -- ID(s) of the reports to retrieve. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -136,15 +137,15 @@
             endpoints=Endpoints,
             operation_id="report_executions_get",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_reports(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_reports(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all report execution IDs matching the query with filter.
 
         Keyword arguments:
         filter -- FQL query specifying the filter parameters.
                   Filter term criteria: type, scheduled_report_id, status.
                   Filter range criteria: created_on, last_updated_on, expiration_on;
                     use any common date format, such as '2010-05-15T14:55:21.892315096Z'.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/response_policies.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/response_policies.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._payload import generic_payload_list, response_policy_payload
 from ._service_class import ServiceClass
 from ._endpoint._response_policies import _response_policies_endpoints as Endpoints
 
 
 class ResponsePolicies(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Response policy by providing an FQL filter and paging details.
 
         Returns a set of host details which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Response Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -84,15 +85,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedRTResponsePolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Response Policies by providing an FQL filter and paging details.
 
         Returns a set of Response Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -120,15 +121,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def perform_policies_action(self: object,
                                 body: dict = None,
                                 parameters: dict = None,
                                 **kwargs
-                                ) -> dict:
+                                ) -> Dict[str, Union[int, dict]]:
         """Perform the specified action on the Response Policies specified in the request.
 
         Keyword arguments:
         action_name -- action to perform: 'add-host-group', 'add-rule-group', 'disable',
                        'enable', 'remove-host-group', or 'remove-rule-group'.
         action_parameters -- Action specific parameter options. List of dictionaries.
                              {
@@ -178,15 +179,15 @@
             operation_id="performRTResponsePoliciesAction",
             keywords=kwargs,
             params=parameters,
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> dict:
+    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Set the precedence of Response Policies based on the order of IDs in the request.
 
         The first ID specified will have the highest precedence and the last ID specified will
         have the lowest. You must specify all non-Default Policies for a platform when updating
         precedence.
 
         Keyword arguments:
@@ -218,15 +219,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="setRTResponsePoliciesPrecedence",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Response Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Response Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -244,15 +245,15 @@
             endpoints=Endpoints,
             operation_id="getRTResponsePolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def create_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Response Policies by specifying details about the policy to create.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -295,15 +296,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createRTResponsePolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Response Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Response Policy IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -321,15 +322,15 @@
             endpoints=Endpoints,
             operation_id="deleteRTResponsePolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Response Policies by specifying the ID of the policy and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -370,15 +371,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateRTResponsePolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Response policy by providing an FQL filter and paging details.
 
         Returns a set of Agent IDs which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Response Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -403,15 +404,15 @@
             endpoints=Endpoints,
             operation_id="queryRTResponsePolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Response Policies by providing an FQL filter with sort and/or paging details.
 
         This returns a set of Response Policy IDs that match the given criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sample_uploads.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sample_uploads.py`

 * *Files 1% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import json
+from typing import Dict, Union
 from ._util import (
     force_default,
     process_service_request,
     handle_single_argument,
     generate_error_result
     )
 from ._payload import extraction_payload
@@ -399,15 +400,15 @@
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def upload_sample(self: object,
                       file_data: object = None,
                       body: dict = None,
                       parameters: dict = None,
                       **kwargs
-                      ) -> dict:
+                      ) -> Dict[str, Union[int, dict]]:
         """Upload a file for further cloud analysis.
 
         After uploading, call the specific analysis API endpoint.
 
         Keyword arguments:
         comment -- A descriptive comment to identify the file for other users. String.
         file_data -- Content of the uploaded sample in binary format. Max file size is 256 MB.
@@ -469,15 +470,15 @@
             body=body,
             data=file_data,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_sample(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_sample(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Remove a sample, including file, meta and submissions from the collection.
 
         Keyword arguments:
         ids -- List of SHA256s to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/scheduled_reports.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/scheduled_reports.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import reports_payload
 from ._service_class import ServiceClass
 from ._endpoint._scheduled_reports import _scheduled_reports_endpoints as Endpoints
 
 
 class ScheduledReports(ServiceClass):
@@ -50,16 +51,16 @@
           "client_id": "CLIENT_ID_HERE",
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
-    @force_default(defaults=["body"], default_types=["dict"])
-    def launch(self: object, *args, body: dict = None, **kwargs) -> dict:
+    @force_default(defaults=["body"], default_types=["list"])
+    def launch(self: object, *args, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Launch scheduled report executions for the provided ID(s).
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 [
                     {
                         "id": "string"
@@ -84,15 +85,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="scheduled_reports_launch",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_reports(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_reports(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve scheduled reports for the provided report IDs.
 
         Keyword arguments:
         ids -- ID(s) of the reports to retrieve. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -110,15 +111,15 @@
             endpoints=Endpoints,
             operation_id="scheduled_reports_get",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_reports(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_reports(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Find all report IDs matching the query with filter.
 
         Keyword arguments:
         filter -- FQL query specifying the filter parameters.
                   Filter term criteria: type, trigger_reference, recipients, user_uuid,
                                         cid, trigger_params.metadata.
                   Filter range criteria: created_on, modified_on;
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_download.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_download.py`

 * *Files 3% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 import os
+from typing import Dict, Union
 from ._util import generate_ok_result, force_default
 from ._util import handle_single_argument, process_service_request
 from ._service_class import ServiceClass
 from ._endpoint._sensor_download import _sensor_download_endpoints as Endpoints
 
 
 class SensorDownload(ServiceClass):
@@ -55,15 +56,15 @@
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
     def get_combined_sensor_installers_by_query(self: object,
                                                 parameters: dict = None,
                                                 **kwargs
-                                                ) -> dict:
+                                                ) -> Dict[str, Union[int, dict]]:
         """Retrieve all metadata for installers from provided query.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return. [integer, 1-5000]
         offset -- The first item to return, where 0 is the latest item. (Integer)
                   Use with the limit parameter to manage pagination of results.
@@ -160,15 +161,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetSensorInstallersEntities",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
-    def get_sensor_installer_ccid(self: object) -> dict:
+    def get_sensor_installer_ccid(self: object) -> Dict[str, Union[int, dict]]:
         """Retrieve the CID for the current oauth environment.
 
         This method does not accept arguments.
 
         Returns: dict object containing API response.
 
         HTTP Method: GET
@@ -179,15 +180,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetSensorInstallersCCIDByQuery"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_sensor_installers_by_query(self: object, parameters: dict = None, **kwargs) -> dict:
+    def get_sensor_installers_by_query(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a list of SHA256 for installers based on the filter.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return. [integer, 1-500]
         offset -- The first item to return, where 0 is the latest item. (Integer)
                   Use with the limit parameter to manage pagination of results.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_update_policy.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_update_policy.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import generate_error_result, args_to_params, force_default
 from ._util import handle_single_argument, process_service_request
 from ._payload import generic_payload_list, sensor_policy_payload
 from ._service_class import ServiceClass
 from ._endpoint._sensor_update_policies import _sensor_update_policies_endpoints as Endpoints
 
 
@@ -52,15 +53,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def reveal_uninstall_token(self: object, body: dict = None, **kwargs) -> dict:
+    def reveal_uninstall_token(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Reveals an uninstall token for a specific device.
 
         To retrieve the bulk maintenance token pass the value
         'MAINTENANCE' as the value for 'device_id'.
 
         Keyword arguments:
         audit_message -- Message to list in the audit log for this action. String.
@@ -90,15 +91,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="revealUninstallToken",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_builds(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_builds(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve available builds for use with Sensor Update Policies.
 
         Keyword arguments:
         platform -- The platform to return builds for. String.
                     Allowed values: "linux", "mac", "windows"
         parameters -- full parameters payload, not required if platform is provided as a keyword.
 
@@ -118,15 +119,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedSensorUpdateBuilds",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "platform")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_kernels(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_kernels(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve kernel compatibility info for Sensor Update Builds.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                  Use with the offset parameter to manage pagination of results.
         offset -- The offset to start retrieving records from. Integer.
@@ -148,15 +149,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedSensorUpdateKernels",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Sensor Update Policy by providing a FQL filter and paging detail.
 
         Returns a set of host details which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Sensor Update Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -182,15 +183,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedSensorUpdatePolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Sensor Update Policies by providing an FQL filter and paging details.
 
         Returns a set of Sensor Update Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -219,15 +220,15 @@
             endpoints=Endpoints,
             operation_id="queryCombinedSensorUpdatePolicies",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_combined_policies_v2(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_combined_policies_v2(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Sensor Update Policies by providing an FQL filter and paging details.
 
         Provides additional support for uninstall protection.
         Returns a set of Sensor Update Policies which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -261,15 +262,15 @@
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
     def perform_policies_action(self: object,
                                 body: dict = None,
                                 parameters: dict = None,
                                 **kwargs
-                                ) -> dict:
+                                ) -> Dict[str, Union[int, dict]]:
         """Perform the specified action on the Sensor Update Policies specified in the request.
 
         Keyword arguments:
         action_name -- action to perform: 'add-host-group', 'disable', 'enable',
                        or 'remove-host-group'.
         action_parameters -- Action specific parameter options. List of dictionaries.
                              {
@@ -329,15 +330,15 @@
                             )
         else:
             returned = generate_error_result("Invalid value specified for action_name parameter.")
 
         return returned
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> dict:
+    def set_policies_precedence(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Set the precedence of Sensor Update Policies based on the order of IDs in the request.
 
         The first ID specified will have the highest precedence and the last ID specified will have
         the lowest. You must specify all non-Default Policies for a platform when updating
         precedence.
 
         Keyword arguments:
@@ -370,15 +371,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="setSensorUpdatePoliciesPrecedence",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Sensor Update Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Sensor Update Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -396,15 +397,15 @@
             endpoints=Endpoints,
             operation_id="getSensorUpdatePolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def create_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Sensor Update Policies by specifying details about the policy to create.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -444,15 +445,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createSensorUpdatePolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a set of Sensor Update Policies by specifying their IDs.
 
         Keyword arguments:
         ids -- List of Sensor Update Policy IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -471,15 +472,15 @@
             endpoints=Endpoints,
             operation_id="deleteSensorUpdatePolicies",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Sensor Update Policies by specifying the ID of the policy and details to update.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
                         {
@@ -519,15 +520,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateSensorUpdatePolicies",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_policies_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_policies_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Retrieve a set of Sensor Update Policies by specifying their IDs.
 
         Provides additional support for uninstall protection.
 
         Keyword arguments:
         ids -- List of Sensor Update Policy IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
@@ -548,15 +549,15 @@
             endpoints=Endpoints,
             operation_id="getSensorUpdatePoliciesV2",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_policies_v2(self: object, body: dict = None, **kwargs) -> dict:
+    def create_policies_v2(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create Sensor Update Policies by specifying details about the policy.
 
         Provides additional support for uninstall protection.
 
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
@@ -603,15 +604,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createSensorUpdatePoliciesV2",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_policies_v2(self: object, body: dict = None, **kwargs) -> dict:
+    def update_policies_v2(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update Sensor Update Policies by specifying the ID of the policy and update details.
 
         Provides additional support for uninstall protection.
         Keyword arguments:
         body -- full body payload, not required if keywords are used.
                 {
                     "resources": [
@@ -656,15 +657,19 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="updateSensorUpdatePoliciesV2",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_kernels(self: object, distinct_field: str = "id", parameters: dict = None, **kwargs) -> dict:
+    def query_kernels(self: object,
+                      distinct_field: str = "id",
+                      parameters: dict = None,
+                      **kwargs
+                      ) -> Dict[str, Union[int, dict]]:
         """Retrieve kernel compatibility info for Sensor Update Builds.
 
         Keyword arguments:
         distinct_field -- The field name to get distinct values for. If you do not
                           specify a value for this field it will default to `id`.
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
@@ -689,15 +694,15 @@
             operation_id="querySensorUpdateKernelsDistinct",
             keywords=kwargs,
             params=parameters,
             distinct_field=distinct_field
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for members of a Sensor Update Policy by providing a FQL filter and paging detail.
 
         Returns a set of Agent IDs which match the filter criteria.
 
         Keyword arguments:
         id -- The ID of the Sensor Update Policy to search for members of
         filter -- The filter expression that should be used to limit the results. FQL syntax.
@@ -723,15 +728,15 @@
             endpoints=Endpoints,
             operation_id="querySensorUpdatePolicyMembers",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Sensor Update Policies by providing a FQL filter and paging details.
 
         Returns a set of Sensor Update Policy IDs which match the filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
         limit -- The maximum number of records to return in this response. [Integer, 1-5000]
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/sensor_visibility_exclusions.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/sensor_visibility_exclusions.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import exclusion_payload
 from ._service_class import ServiceClass
 from ._endpoint._sensor_visibility_exclusions import _sensor_visibility_exclusions_endpoints as EPS
 
 
 class SensorVisibilityExclusions(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (OAuth2.token())
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a set of Sensor Visibility Exclusions by specifying their IDs.
 
         Keyword arguments:
         ids -- List of exclusion IDs to retrieve. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -77,15 +78,15 @@
             endpoints=EPS,
             operation_id="getSensorVisibilityExclusionsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def create_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create the Sensor Visibility exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "comment": "string",
                     "groups": [
@@ -113,15 +114,15 @@
             calling_object=self,
             endpoints=EPS,
             operation_id="createSVExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete the Sensor Visibility exclusions by ID.
 
         Keyword arguments:
         comment -- Explains why this exclusions was deleted. String.
         ids -- List of exclusion IDs to delete. String or list of strings.
         parameters -- full parameters payload, not required if ids is provided as a keyword.
 
@@ -140,15 +141,15 @@
             endpoints=EPS,
             operation_id="deleteSensorVisibilityExclusionsV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def update_exclusions(self: object, body: dict = None, **kwargs) -> dict:
+    def update_exclusions(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Update the Sensor Visibility Exclusions.
 
         Keyword arguments:
         body -- full body payload, not required when ids keyword is provided.
                 {
                     "comment": "string",
                     "groups": [
@@ -180,15 +181,15 @@
             calling_object=self,
             endpoints=EPS,
             operation_id="updateSensorVisibilityExclusionsV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Sensor Visibility Exclusions.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   An asterisk wildcard '*' includes all results.
                   AVAILABLE FILTERS
                   applied_globally            last_modified
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/spotlight_evaluation_logic.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/spotlight_evaluation_logic.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request
 from ._util import handle_single_argument, generate_error_result
 from ._service_class import ServiceClass
 from ._endpoint._spotlight_evaluation_logic import _spotlight_evaluation_logic_endpoints as Endpoints
 
 
 class SpotlightEvaluationLogic(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_evaluation_logic_combined(self: object, parameters: dict = None,  **kwargs) -> dict:
+    def query_evaluation_logic_combined(self: object, parameters: dict = None,  **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for evaluation logic in your environment by providing a FQL filter and paging details.
 
         Returns a set of evaluation logic entities which match the filter criteria.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an after token. On subsequent requests,
@@ -100,15 +101,15 @@
                 keywords=kwargs,
                 params=parameters
                 )
 
         return returned
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_evaluation_logic(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_evaluation_logic(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on evaluation logic items by providing one or more IDs.
 
         Keyword arguments:
         ids -- One or more evaluation logic IDs (max: 400). String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -126,15 +127,15 @@
             endpoints=Endpoints,
             operation_id="getEvaluationLogic",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_evaluation_logic(self: object, parameters: dict = None,  **kwargs) -> dict:
+    def query_evaluation_logic(self: object, parameters: dict = None,  **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for evaluation logic in your environment by providing a FQL filter and paging details.
 
         Returns a set of evaluation logic IDs which match the filter criteria.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an after token. On subsequent requests,
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/spotlight_vulnerabilities.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/spotlight_vulnerabilities.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request
 from ._util import handle_single_argument, generate_error_result
 from ._service_class import ServiceClass
 from ._endpoint._spotlight_vulnerabilities import _spotlight_vulnerabilities_endpoints as Endpoints
 
 
 class SpotlightVulnerabilities(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_vulnerabilities_combined(self: object, parameters: dict = None,  **kwargs) -> dict:
+    def query_vulnerabilities_combined(self: object, parameters: dict = None,  **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Vulnerabilities by providing an FQL filter and paging details.
 
         Returns a set of Vulnerability IDs which match the filter criteria.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an after token. On subsequent requests,
@@ -104,15 +105,15 @@
                 keywords=kwargs,
                 params=parameters
                 )
 
         return returned
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_vulnerabilities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_vulnerabilities(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on vulnerabilities by providing one or more IDs.
 
         Keyword arguments:
         ids -- One or more vulnerability IDs (max: 400). String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -130,15 +131,15 @@
             endpoints=Endpoints,
             operation_id="getVulnerabilities",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_vulnerabilities(self: object, parameters: dict = None,  **kwargs) -> dict:
+    def query_vulnerabilities(self: object, parameters: dict = None,  **kwargs) -> Dict[str, Union[int, dict]]:
         """Search for Vulnerabilities by providing an FQL filter and paging details.
 
         Returns a set of Vulnerability IDs which match the filter criteria.
 
         Keyword arguments:
         after -- A pagination token used with the limit parameter to manage pagination of results.
                  On your first request, don't provide an after token. On subsequent requests,
@@ -166,15 +167,15 @@
             endpoints=Endpoints,
             operation_id="queryVulnerabilities",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_remediations(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_remediations(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on remediations by providing one or more IDs.
 
         Keyword arguments:
         ids -- One or more remediation IDs. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -192,15 +193,15 @@
             endpoints=Endpoints,
             operation_id="getRemediations",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_remediations_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_remediations_v2(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get details on remediations by providing one or more IDs.
 
         Keyword arguments:
         ids -- One or more remediation IDs. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/tailored_intelligence.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/tailored_intelligence.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import process_service_request, force_default, handle_single_argument
 from ._payload import generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._tailored_intelligence import _tailored_intelligence_endpoints as Endpoints
 
 
 class TailoredIntelligence(ServiceClass):
@@ -51,15 +52,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_event_body(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_event_body(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get the event body for the provided event ID.
 
         Keyword arguments:
         id -- Event ID to retrieve the body for. String. Required.
         parameters - full parameters payload, not required if 'id' keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'id'.
@@ -77,15 +78,15 @@
             endpoints=Endpoints,
             operation_id="GetEventsBody",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "id")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_event_entities(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_event_entities(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get events entities for specified IDs.
 
         Keyword arguments:
         ids -- Event ID to retrieve. String or list of strings.
         parameters - full parameters payload, not required if 'id' keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -113,15 +114,15 @@
             endpoints=Endpoints,
             operation_id="GetEventsEntities",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_events(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_events(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query for event IDs that match the provided filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Providing just a wildcard will return all results.
         limit -- The maximum number of records to return. [integer]
         offset -- Starting index of overall result set from which to return IDs. String.
@@ -144,15 +145,15 @@
             endpoints=Endpoints,
             operation_id="QueryEvents",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def get_rule_entities(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def get_rule_entities(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get rule entities for specified IDs.
 
         Keyword arguments:
         ids -- Rule ID to retrieve. String or list of strings.
         parameters - full parameters payload, not required if 'id' keyword is provided.
 
         Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
@@ -180,15 +181,15 @@
             endpoints=Endpoints,
             operation_id="GetRulesEntities",
             keywords=kwargs,
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Query for rule IDs that match the provided filter criteria.
 
         Keyword arguments:
         filter -- The filter expression that should be used to limit the results. FQL syntax.
                   Providing just a wildcard will return all results.
         limit -- The maximum number of records to return. [integer]
         offset -- Starting index of overall result set from which to return IDs. String.
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/user_management.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/user_management.py`

 * *Files 3% similar despite different names*

```diff
@@ -32,14 +32,15 @@
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
 # pylint: disable=R0904,C0302
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._payload import generic_payload_list
 from ._service_class import ServiceClass
 from ._endpoint._user_management import _user_management_endpoints as Endpoints
 
 
 class UserManagement(ServiceClass):
@@ -54,15 +55,15 @@
               "client_secret": "CLIENT_SECRET_HERE"
           }
     - an `auth_object` containing a valid instance of the authentication service class (OAuth2)
     - a valid token provided by the token method of the authentication service class (OAuth2.token)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_user_grants(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_user_grants(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get User Grant(s).
 
         This operation lists both direct as well as flight control grants
         between a User and a Customer.
 
         HTTP Method: GET
 
@@ -108,15 +109,15 @@
             endpoints=Endpoints,
             operation_id="combinedUserRolesV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_uuid")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_roles_mssp(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_roles_mssp(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get information about a role, supports Flight Control.
 
         HTTP Method: GET
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/entitiesRolesV1
 
@@ -146,15 +147,15 @@
             endpoints=Endpoints,
             operation_id="entitiesRolesV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def user_action(self: object, body: dict = None, **kwargs) -> dict:
+    def user_action(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Apply actions to one or more users.
 
         HTTP Method: POST
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/userActionV1
 
@@ -204,15 +205,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="userActionV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def user_roles_action(self: object, body: dict = None, **kwargs) -> dict:
+    def user_roles_action(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Grant or Revoke one or more role(s) to a user against a CID.
 
         HTTP Method: POST
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/userRolesActionV1
 
@@ -262,15 +263,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="userRolesActionV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def retrieve_users(self: object, *args, body: dict = None, **kwargs) -> dict:
+    def retrieve_users(self: object, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get info about users including their name, UID and CID by providing user UUIDs.
 
         HTTP Method: POST
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/retrieveUsersGETV1
 
@@ -310,15 +311,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="retrieveUsersGETV1",
             body=body
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_user_mssp(self: object, body: dict = None, **kwargs) -> dict:
+    def create_user_mssp(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a new user. Supports Flight Control.
 
         After creating a user, assign one or more roles with `user_roles_action`.
 
         HTTP Method: POST
 
         Swagger URL
@@ -376,15 +377,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="createUserV1",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_user_mssp(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_user_mssp(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a user permanently. Supports Flight Control.
 
         HTTP Method: DELETE
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/deleteUserV1
 
@@ -411,15 +412,15 @@
             endpoints=Endpoints,
             operation_id="deleteUserV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_uuid")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def update_user_mssp(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def update_user_mssp(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Modify an existing user's first or last name. Supports Flight Control.
 
         HTTP Method: PATCH
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/updateUserV1
 
@@ -463,15 +464,15 @@
             operation_id="updateUserV1",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_roles(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def query_roles(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Show role IDs for all roles available in your customer account. Supports Flight Control.
 
         For more information on each role, provide the role ID to `get_roles_mssp`.
 
         HTTP Method: GET
 
         Swagger URL
@@ -503,15 +504,15 @@
             endpoints=Endpoints,
             operation_id="queriesRolesV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_uuid")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def query_users(self: object, parameters: dict = None, **kwargs) -> dict:
+    def query_users(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """List user IDs for all users in your customer account.
 
         For more information on each user, provide the user ID to `retrieve_users`.
 
         HTTP Method: GET
 
         Swagger URL
@@ -547,15 +548,15 @@
             endpoints=Endpoints,
             operation_id="queryUserV1",
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_roles(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_roles(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get information about a role.
 
         HTTP Method: GET
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetRoles
 
@@ -582,15 +583,15 @@
             endpoints=Endpoints,
             operation_id="GetRoles",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def grant_user_role_ids(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
+    def grant_user_role_ids(self: object, body: dict, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Assign one or more roles to a user.
 
         HTTP Method: POST
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GrantUserRoleIds
 
@@ -635,15 +636,15 @@
             operation_id="GrantUserRoleIds",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def revoke_user_role_ids(self: object, parameters: dict = None, **kwargs) -> dict:
+    def revoke_user_role_ids(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Revoke one or more roles from a user.
 
         HTTP Method: DELETE
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RevokeUserRoleIds
 
@@ -670,15 +671,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RevokeUserRoleIds",
             keywords=kwargs,
             params=parameters
             )
 
-    def get_available_role_ids(self: object) -> dict:
+    def get_available_role_ids(self: object) -> Dict[str, Union[int, dict]]:
         """Show role IDs for all roles available in your customer account.
 
         For more information on each role, provide the role ID to get_roles.
 
         HTTP Method: GET
 
         Swagger URL
@@ -700,15 +701,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="GetAvailableRoleIds"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_user_role_ids(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_user_role_ids(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Show role IDs of roles assigned to a user.
 
         For more information on each role, provide the role ID to `get_role`.
 
         HTTP Method: GET
 
         Swagger URL
@@ -737,15 +738,15 @@
             endpoints=Endpoints,
             operation_id="GetUserRoleIds",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_uuid")
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def retrieve_user(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def retrieve_user(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get information about a user.
 
         HTTP Method: GET
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUser
 
@@ -772,15 +773,15 @@
             endpoints=Endpoints,
             operation_id="RetrieveUser",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
     @force_default(defaults=["body"], default_types=["dict"])
-    def create_user(self: object, body: dict = None, **kwargs) -> dict:
+    def create_user(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Create a new user.
 
         After creating a user, assign one or more roles with `grant_user_role_ids`.
 
         HTTP Method: POST
 
         Swagger URL
@@ -832,15 +833,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="CreateUser",
             body=body
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def delete_user(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def delete_user(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Delete a user permanently.
 
         HTTP Method: DELETE
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/DeleteUser
 
@@ -867,15 +868,15 @@
             endpoints=Endpoints,
             operation_id="DeleteUser",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "user_uuid")
             )
 
     @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
-    def update_user(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
+    def update_user(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Modify an existing user.
 
         HTTP Method: PATCH
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/UpdateUser
 
@@ -918,15 +919,15 @@
             endpoints=Endpoints,
             operation_id="UpdateUser",
             body=body,
             keywords=kwargs,
             params=parameters
             )
 
-    def retrieve_emails_by_cid(self: object) -> dict:
+    def retrieve_emails_by_cid(self: object) -> Dict[str, Union[int, dict]]:
         """List the usernames (usually an email address) for all users in your customer account.
 
         HTTP Method: GET
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveEmailsByCID
 
@@ -945,15 +946,15 @@
         """
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RetrieveEmailsByCID"
             )
 
-    def retrieve_user_uuids_by_cid(self: object) -> dict:
+    def retrieve_user_uuids_by_cid(self: object) -> Dict[str, Union[int, dict]]:
         """List user IDs for all users in your customer account.
 
         For more information on each user, provide the user ID to `retrieve_user`.
 
         HTTP Method: GET
 
         Swagger URL
@@ -975,15 +976,15 @@
         return process_service_request(
             calling_object=self,
             endpoints=Endpoints,
             operation_id="RetrieveUserUUIDsByCID"
             )
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def retrieve_user_uuid(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def retrieve_user_uuid(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get a user's ID by providing a username (usually an email address).
 
         HTTP Method: GET
 
         Swagger URL
         https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUID
```

### Comparing `crowdstrike-falconpy-dev-1.2.9/src/falconpydev/zero_trust_assessment.py` & `crowdstrike-falconpy-dev-1.3.0.dev1/src/falconpydev/zero_trust_assessment.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 For more information, please refer to <https://unlicense.org>
 """
+from typing import Dict, Union
 from ._util import force_default, process_service_request, handle_single_argument
 from ._service_class import ServiceClass
 from ._endpoint._zero_trust_assessment import _zero_trust_assessment_endpoints as Endpoints
 
 
 class ZeroTrustAssessment(ServiceClass):
     """The only requirement to instantiate an instance of this class is one of the following.
@@ -50,15 +51,15 @@
           "client_secret": "CLIENT_SECRET_HERE"
       }
     - a previously-authenticated instance of the authentication service class (oauth2.py)
     - a valid token provided by the authentication service class (oauth2.py)
     """
 
     @force_default(defaults=["parameters"], default_types=["dict"])
-    def get_assessment(self: object, *args, parameters: dict = None, **kwargs) -> dict:
+    def get_assessment(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
         """Get Zero Trust Assessment data for one or more hosts by providing agent IDs (AID).
 
         Keyword arguments:
         ids -- One or more agent IDs, which you can find in the data.zta file,
                or the Falcon console. String or list of strings.
         parameters - full parameters payload, not required if ids is provided as a keyword.
 
@@ -76,15 +77,15 @@
             calling_object=self,
             endpoints=Endpoints,
             operation_id="getAssessmentV1",
             keywords=kwargs,
             params=handle_single_argument(args, parameters, "ids")
             )
 
-    def get_compliance(self: object) -> dict:
+    def get_compliance(self: object) -> Dict[str, Union[int, dict]]:
         """Get the Zero Trust Assessment compliance report for one customer ID (CID).
 
         This method does not accept arguments.
 
         Returns: dict object containing API response.
 
         HTTP Method: GET
```

