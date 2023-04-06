# Comparing `tmp/teflo-2.3.0.tar.gz` & `tmp/teflo-2.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "teflo-2.3.0.tar", last modified: Mon Feb  6 20:06:19 2023, max compression
+gzip compressed data, was "teflo-2.4.0.tar", last modified: Thu Apr  6 20:01:46 2023, max compression
```

## Comparing `teflo-2.3.0.tar` & `teflo-2.4.0.tar`

### file list

```diff
@@ -1,114 +1,114 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/
--rw-r--r--   0 runner    (1001) docker     (123)      243 2023-02-06 20:06:10.000000 teflo-2.3.0/AUTHORS
--rw-r--r--   0 runner    (1001) docker     (123)    32462 2023-02-06 20:06:10.000000 teflo-2.3.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      814 2023-02-06 20:06:10.000000 teflo-2.3.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-02-06 20:06:19.303841 teflo-2.3.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-02-06 20:06:10.000000 teflo-2.3.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-06 20:06:19.303841 teflo-2.3.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3908 2023-02-06 20:06:10.000000 teflo-2.3.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/_compat.py
--rw-r--r--   0 runner    (1001) docker     (123)    36544 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/ansible_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    15148 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     5351 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    52186 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     7898 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/executors/
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/execute_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/executors/ext/
--rw-r--r--   0 runner    (1001) docker     (123)      788 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/ext/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18089 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/ansible_executor_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/files/
--rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/files/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/files/schema.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/files/
--rw-r--r--   0 runner    (1001) docker     (123)     3173 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/files/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4505 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/files/schema.yml
--rw-r--r--   0 runner    (1001) docker     (123)    81193 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/importers/
--rw-r--r--   0 runner    (1001) docker     (123)      945 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/importers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4413 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/importers/artifact_importer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/notifiers/
--rw-r--r--   0 runner    (1001) docker     (123)      924 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/notifiers/ext/
--rw-r--r--   0 runner    (1001) docker     (123)      936 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/notifiers/ext/email/
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7896 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/email_notification_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/notifiers/ext/email/schema/
--rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/schema/email_extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)      837 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/schema/schema.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/notifiers/ext/email/templates/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/templates/email_on_start_txt_template.jinja
--rw-r--r--   0 runner    (1001) docker     (123)     1907 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/ext/email/templates/email_txt_template.jinja
--rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/notifiers/notification_emitter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/orchestrators/
--rw-r--r--   0 runner    (1001) docker     (123)      958 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2327 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/action_orchestrator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/orchestrators/ext/
--rw-r--r--   0 runner    (1001) docker     (123)      798 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/ext/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12454 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/ansible_orchestrator_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/
--rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/schema.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/providers/
--rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/providers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    34125 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/providers/aws.py
--rw-r--r--   0 runner    (1001) docker     (123)    16778 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/providers/beaker.py
--rw-r--r--   0 runner    (1001) docker     (123)    10822 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/providers/libvirt.py
--rw-r--r--   0 runner    (1001) docker     (123)     8907 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/providers/openstack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo/provisioners/
--rw-r--r--   0 runner    (1001) docker     (123)      951 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/asset_provisioner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/provisioners/ext/
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      794 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    44855 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/beaker_client_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2329 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/schema.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      804 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24546 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/openstack_libcloud_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/schema.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/resources/
--rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11188 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/actions.py
--rw-r--r--   0 runner    (1001) docker     (123)    19942 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/assets.py
--rw-r--r--   0 runner    (1001) docker     (123)     9255 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/executes.py
--rw-r--r--   0 runner    (1001) docker     (123)    11087 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/notification.py
--rw-r--r--   0 runner    (1001) docker     (123)    12348 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/reports.py
--rw-r--r--   0 runner    (1001) docker     (123)    28440 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/resources/scenario.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/static/
--rw-r--r--   0 runner    (1001) docker     (123)      897 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/static/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9653 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/static/playbooks.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3568 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/cleanup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1971 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/execute.py
--rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/notification.py
--rw-r--r--   0 runner    (1001) docker     (123)     2101 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/orchestrate.py
--rw-r--r--   0 runner    (1001) docker     (123)     2415 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/provision.py
--rw-r--r--   0 runner    (1001) docker     (123)     2571 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/report.py
--rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/tasks/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)    37764 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/teflo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.303841 teflo-2.3.0/teflo/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      894 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/utils/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    15528 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/utils/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     9297 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/utils/resource_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)    13571 2023-02-06 20:06:10.000000 teflo-2.3.0/teflo/utils/scenario_graph.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-06 20:06:19.299842 teflo-2.3.0/teflo.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      671 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      503 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-02-06 20:06:19.000000 teflo-2.3.0/teflo.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-04-06 20:01:32.000000 teflo-2.4.0/AUTHORS
+-rw-r--r--   0 runner    (1001) docker     (123)    32462 2023-04-06 20:01:32.000000 teflo-2.4.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      814 2023-04-06 20:01:32.000000 teflo-2.4.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3625 2023-04-06 20:01:46.064641 teflo-2.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2761 2023-04-06 20:01:32.000000 teflo-2.4.0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:01:46.064641 teflo-2.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3908 2023-04-06 20:01:32.000000 teflo-2.4.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo/
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/_compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36544 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/ansible_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15148 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5351 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52186 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7898 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo/executors/
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/execute_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo/executors/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)      788 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/ext/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18089 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/ansible_executor_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/files/
+-rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/files/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/files/schema.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/files/
+-rw-r--r--   0 runner    (1001) docker     (123)     2686 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/files/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4471 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/files/schema.yml
+-rw-r--r--   0 runner    (1001) docker     (123)    81189 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/importers/
+-rw-r--r--   0 runner    (1001) docker     (123)      945 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/importers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4413 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/importers/artifact_importer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/notifiers/
+-rw-r--r--   0 runner    (1001) docker     (123)      924 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/notifiers/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)      936 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/notifiers/ext/email/
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7896 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/email_notification_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/notifiers/ext/email/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/schema/email_extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      837 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/schema/schema.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/notifiers/ext/email/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/templates/email_on_start_txt_template.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)     1907 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/ext/email/templates/email_txt_template.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/notifiers/notification_emitter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/orchestrators/
+-rw-r--r--   0 runner    (1001) docker     (123)      958 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2327 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/action_orchestrator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/orchestrators/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)      798 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/ext/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12454 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/ansible_orchestrator_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/
+-rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/schema.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/providers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/providers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34125 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/providers/aws.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16778 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/providers/beaker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10822 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/providers/libvirt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8907 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/providers/openstack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/provisioners/
+-rw-r--r--   0 runner    (1001) docker     (123)      951 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/asset_provisioner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/provisioners/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.060641 teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      794 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44855 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/beaker_client_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2329 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/schema.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24546 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/openstack_libcloud_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/schema.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/teflo/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11188 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/actions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19291 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/assets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9255 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/executes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11087 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/notification.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12348 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28440 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/resources/scenario.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/teflo/static/
+-rw-r--r--   0 runner    (1001) docker     (123)      897 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/static/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9653 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/static/playbooks.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/teflo/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3568 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/cleanup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1971 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/execute.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/notification.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2101 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/orchestrate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2415 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/provision.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2571 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/tasks/validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37764 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/teflo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.064641 teflo-2.4.0/teflo/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      894 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9713 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/utils/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15528 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/utils/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9297 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/utils/resource_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13561 2023-04-06 20:01:32.000000 teflo-2.4.0/teflo/utils/scenario_graph.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:01:46.056640 teflo-2.4.0/teflo.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3625 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      671 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      503 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 20:01:46.000000 teflo-2.4.0/teflo.egg-info/top_level.txt
```

### Comparing `teflo-2.3.0/LICENSE` & `teflo-2.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/MANIFEST.in` & `teflo-2.4.0/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/PKG-INFO` & `teflo-2.4.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: teflo
-Version: 2.3.0
+Version: 2.4.0
 Summary: Test Execution Framework Libraries and Objects. It is an orchestration software that controls the flow of a set of testing scenarios.
 Author: Red Hat Inc.
 License: GPLv3
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
 Classifier: Natural Language :: English
@@ -16,14 +16,18 @@
 Provides-Extra: openstack-client-plugin
 Provides-Extra: terraform-plugin
 Provides-Extra: webhook-notification-plugin
 Provides-Extra: notify-service-plugin
 License-File: LICENSE
 License-File: AUTHORS
 
+.. warning::
+    **This project is in maintenance mode and will not have any new feature development.**
+
+
 Welcome to Teflo!
 ==================
 
 What is Teflo?
 ---------------
 
 **TEFLO** stands for (**T** est **E** xecution **F** ramework **L** ibraries and **O** bjects)
```

### Comparing `teflo-2.3.0/README.rst` & `teflo-2.4.0/README.rst`

 * *Files 12% similar despite different names*

```diff
@@ -1,7 +1,11 @@
+.. warning::
+    **This project is in maintenance mode and will not have any new feature development.**
+
+
 Welcome to Teflo!
 ==================
 
 What is Teflo?
 ---------------
 
 **TEFLO** stands for (**T** est **E** xecution **F** ramework **L** ibraries and **O** bjects)
```

### Comparing `teflo-2.3.0/setup.py` & `teflo-2.4.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -57,15 +57,15 @@
         'ipaddress',
         'Jinja2>=2.10',
         'pykwalify>=1.6.0',
         'python-cachetclient',
         'ruamel.yaml>=0.15.64',
         'paramiko>=2.4.2',
         'retry2>=0.9.4',
-        'ssh-python==0.9.0',
+        'ssh-python>=0.9.0',
         'requests>=2.20.1',
         'urllib3>=1.26',
         'termcolor>=1.1.0'
     ],
     extras_require={
                     'linchpin-wrapper': ['teflo_linchpin_plugin'],
                     'openstack-client-plugin': ['teflo_openstack_client_plugin'],
```

### Comparing `teflo-2.3.0/teflo/__init__.py` & `teflo-2.4.0/teflo/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,9 +20,9 @@
 
     A framework that cares about product interoperability quality.
 
     :copyright: (c) 2022 Red Hat, Inc.
     :license: GPLv3, see LICENSE for more details.
 """
 from .teflo import Teflo
-__version__ = '2.3.0'
+__version__ = '2.4.0'
 __author__ = 'Red Hat Inc.'
```

### Comparing `teflo-2.3.0/teflo/_compat.py` & `teflo-2.4.0/teflo/_compat.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/ansible_helpers.py` & `teflo-2.4.0/teflo/ansible_helpers.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/cli.py` & `teflo-2.4.0/teflo/cli.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/constants.py` & `teflo-2.4.0/teflo/constants.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/core.py` & `teflo-2.4.0/teflo/core.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/exceptions.py` & `teflo-2.4.0/teflo/exceptions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/__init__.py` & `teflo-2.4.0/teflo/executors/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/execute_manager.py` & `teflo-2.4.0/teflo/executors/execute_manager.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/ext/__init__.py` & `teflo-2.4.0/teflo/executors/ext/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/__init__.py` & `teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/ansible_executor_plugin.py` & `teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/ansible_executor_plugin.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/files/extensions.py` & `teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/files/extensions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/executors/ext/ansible_executor_plugin/files/schema.yml` & `teflo-2.4.0/teflo/executors/ext/ansible_executor_plugin/files/schema.yml`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/files/schema.yml` & `teflo-2.4.0/teflo/files/schema.yml`

 * *Files 1% similar despite different names*

```diff
@@ -70,29 +70,27 @@
 
   provision:
     required: False
     sequence:
       - type: map
         allowempty: True
         matching-rule: any
+        func: check_provider_present
         mapping:
           name:
             required: True
             type: str
           description:
             type: str
           ip_address:
             required: False
             type: any
           provisioner:
             type: str
-          provider:
-            allowempty: True
             required: False
-            type: map
           ansible_params:
             type: map
             allowempty: True
           labels:
             type: any
             func: type_str_list
           metadata:
```

### Comparing `teflo-2.3.0/teflo/helpers.py` & `teflo-2.4.0/teflo/helpers.py`

 * *Files 0% similar despite different names*

```diff
@@ -1679,15 +1679,15 @@
                 remote_workspace_path = os.path.join(
                         config["WORKSPACE"], config["REMOTE_WORKSPACE_DOWNLOAD_LOCATION"] + short_name_of_workspace)
                 ret[short_name_of_workspace] = remote_workspace_path
             return ret
 
         workspace_info = None
         if 'remote_workspace' in data.keys() and data['remote_workspace'] is not None \
-                and len(data['remote_workspace']) is not 0:
+                and len(data['remote_workspace']) != 0:
             remote_workspaces = data['remote_workspace']
             workspace_info = process_remote_workspace(remote_workspaces)
 
         def process_path(path: str, workspace_info: dict):
             # ex remote_workspace/sdf.yml
             if path is None or path == "":
                 return None, None
```

### Comparing `teflo-2.3.0/teflo/importers/__init__.py` & `teflo-2.4.0/teflo/importers/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/importers/artifact_importer.py` & `teflo-2.4.0/teflo/importers/artifact_importer.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/__init__.py` & `teflo-2.4.0/teflo/notifiers/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/__init__.py` & `teflo-2.4.0/teflo/notifiers/ext/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/email/__init__.py` & `teflo-2.4.0/teflo/notifiers/ext/email/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/email/email_notification_plugin.py` & `teflo-2.4.0/teflo/notifiers/ext/email/email_notification_plugin.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/email/schema/email_extensions.py` & `teflo-2.4.0/teflo/notifiers/ext/email/schema/email_extensions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/email/schema/schema.yml` & `teflo-2.4.0/teflo/notifiers/ext/email/schema/schema.yml`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/ext/email/templates/email_txt_template.jinja` & `teflo-2.4.0/teflo/notifiers/ext/email/templates/email_txt_template.jinja`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/notifiers/notification_emitter.py` & `teflo-2.4.0/teflo/notifiers/notification_emitter.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/__init__.py` & `teflo-2.4.0/teflo/orchestrators/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/action_orchestrator.py` & `teflo-2.4.0/teflo/orchestrators/action_orchestrator.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/ext/__init__.py` & `teflo-2.4.0/teflo/orchestrators/ext/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/__init__.py` & `teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/ansible_orchestrator_plugin.py` & `teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/ansible_orchestrator_plugin.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/extensions.py` & `teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/extensions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/schema.yml` & `teflo-2.4.0/teflo/orchestrators/ext/ansible_orchestrator_plugin/files/schema.yml`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/providers/__init__.py` & `teflo-2.4.0/teflo/providers/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/providers/aws.py` & `teflo-2.4.0/teflo/providers/aws.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/providers/beaker.py` & `teflo-2.4.0/teflo/providers/beaker.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/providers/libvirt.py` & `teflo-2.4.0/teflo/providers/libvirt.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/providers/openstack.py` & `teflo-2.4.0/teflo/providers/openstack.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/__init__.py` & `teflo-2.4.0/teflo/provisioners/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/asset_provisioner.py` & `teflo-2.4.0/teflo/provisioners/asset_provisioner.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/__init__.py` & `teflo-2.4.0/teflo/provisioners/ext/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/__init__.py` & `teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/beaker_client_plugin.py` & `teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/beaker_client_plugin.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/extensions.py` & `teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/extensions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/bkr_client_plugin/schema.yml` & `teflo-2.4.0/teflo/provisioners/ext/bkr_client_plugin/schema.yml`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/__init__.py` & `teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/openstack_libcloud_plugin.py` & `teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/openstack_libcloud_plugin.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/provisioners/ext/os_libcloud_plugin/schema.yml` & `teflo-2.4.0/teflo/provisioners/ext/os_libcloud_plugin/schema.yml`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/__init__.py` & `teflo-2.4.0/teflo/resources/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/actions.py` & `teflo-2.4.0/teflo/resources/actions.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/assets.py` & `teflo-2.4.0/teflo/resources/assets.py`

 * *Files 8% similar despite different names*

```diff
@@ -201,35 +201,22 @@
 
             # host needs to be provisioned, get the provider parameters
             parameters = self.__set_provider_attr_(parameters)
 
             # lets setup any feature toggles that we defined in the configuration file
             self.__set_feature_toggles_()
 
-            # TODO remove this , it is additional
-            self._provisioner = get_default_provisioner_plugin()
-
-            if provisioner_name is None and self.has_provider:
-                try:
-                    self._provisioner = get_default_provisioner_plugin(self._provider)
-                except KeyError:
-                    raise TefloResourceError('Specified provider is not supported by a provisioner.')
-            elif provisioner_name:
+            if provisioner_name:
                 found_name = False
                 for name in get_provisioners_plugins_list():
                     if name.startswith(provisioner_name):
                         found_name = True
                         break
-
                 if found_name:
-                    if self.has_provider and \
-                            is_provider_mapped_to_provisioner(self._provider, provisioner_name):
-                        self._provisioner = get_provisioner_plugin_class(provisioner_name)
-                    else:
-                        self._provisioner = get_provisioner_plugin_class(provisioner_name)
+                    self._provisioner = get_provisioner_plugin_class(provisioner_name)
                 else:
                     self.logger.error('Provisioner %s for asset %s is invalid.'
                                       % (provisioner_name, self.name))
                     raise TefloResourceError('The specified provisioner is not valid for the asset type.')
             else:
                 raise TefloResourceError('Could not find a provisioner to satisfy the asset type.')
 
@@ -260,21 +247,18 @@
         :return: updated parameters
         :rtype: dict
         """
 
         self._provider = {}
 
         if parameters.get('provider', False):
-            creds = parameters.get('provider').pop('credential', None)
-            for p, v in parameters.pop('provider').items():
-                if p == 'name':
-                    self._provider = v
-                    continue
-                setattr(self, p, v)
-            self.has_provider = True
+            raise TefloResourceError('Provider key is deprecated and is no longer supported. '
+                                     'Visit '
+                                     'https://teflo.readthedocs.io/en/latest/users/definitions/provision.html#provision'
+                                     ' to see examples for provisioning assets')
         else:
             # set no provider object
             creds = parameters.pop('credential', None)
             for p, v in parameters.items():
                 setattr(self, p, v)
             del self.provider
             self.has_provider = False
```

### Comparing `teflo-2.3.0/teflo/resources/executes.py` & `teflo-2.4.0/teflo/resources/executes.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/notification.py` & `teflo-2.4.0/teflo/resources/notification.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/reports.py` & `teflo-2.4.0/teflo/resources/reports.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/resources/scenario.py` & `teflo-2.4.0/teflo/resources/scenario.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/static/__init__.py` & `teflo-2.4.0/teflo/static/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/static/playbooks.py` & `teflo-2.4.0/teflo/static/playbooks.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/__init__.py` & `teflo-2.4.0/teflo/tasks/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/cleanup.py` & `teflo-2.4.0/teflo/tasks/cleanup.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/execute.py` & `teflo-2.4.0/teflo/tasks/execute.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/notification.py` & `teflo-2.4.0/teflo/tasks/notification.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/orchestrate.py` & `teflo-2.4.0/teflo/tasks/orchestrate.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/provision.py` & `teflo-2.4.0/teflo/tasks/provision.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/report.py` & `teflo-2.4.0/teflo/tasks/report.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/tasks/validate.py` & `teflo-2.4.0/teflo/tasks/validate.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/teflo.py` & `teflo-2.4.0/teflo/teflo.py`

 * *Files 0% similar despite different names*

```diff
@@ -606,15 +606,15 @@
                         str(self.config.get("SKIP_FAIL")).lower() != 'false' and \
                         self.config.get("SKIP_FAIL") is not None:
                     self.logger.error('The skip_fail variable can be true or false only. Running'
                                       ' as default value which is False')
                     self.config["SKIP_FAIL"] = 'False'
 
                 if str(self.config.get("SKIP_FAIL")).lower() != 'true' \
-                        and self._teflo_options.get('skip_fail') is not True and state is 'FAILED':
+                        and self._teflo_options.get('skip_fail') is not True and state == 'FAILED':
                     raise TefloScenarioFailure(
                         "Scenario `%s` failed during the Teflo run" % sc.name)
 
             exit_on_status()
 
     def notify(self, task, status=0, passed_tasks=None, failed_tasks=None, scenario: Scenario = None):
         """
```

### Comparing `teflo-2.3.0/teflo/utils/__init__.py` & `teflo-2.4.0/teflo/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/utils/config.py` & `teflo-2.4.0/teflo/utils/config.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/utils/pipeline.py` & `teflo-2.4.0/teflo/utils/pipeline.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/utils/resource_checker.py` & `teflo-2.4.0/teflo/utils/resource_checker.py`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo/utils/scenario_graph.py` & `teflo-2.4.0/teflo/utils/scenario_graph.py`

 * *Files 1% similar despite different names*

```diff
@@ -169,27 +169,27 @@
         '''
 
         if self.root is None:
             raise StopIteration
 
         if self.iterate_method == "by_depth":
 
-            while len(self.stack) is not 0:
+            while len(self.stack) != 0:
                 self.current = self.stack[-1]
                 if self.prev is None or self.current in self.prev.child_scenarios:
 
                     if self.next_unvisited_sc(self.current.child_scenarios) is not None:
                         next_sc = self.next_unvisited_sc(self.current.child_scenarios)
                         self.stack.append(next_sc)
                         self.visited[next_sc] = True
                     else:
                         self.visited[self.stack.pop()] = True
                         self.prev = self.current
                         return self.current
-                elif (self.prev in self.current.child_scenarios and self.prev is not self.current.child_scenarios[-1]):
+                elif self.prev in self.current.child_scenarios and self.prev is not self.current.child_scenarios[-1]:
                     if self.next_unvisited_sc(self.current.child_scenarios) is not None:
                         next_sc = self.next_unvisited_sc(self.current.child_scenarios)
                         self.stack.append(next_sc)
                         self.visited[next_sc] = True
                     else:
                         self.visited[self.stack.pop()] = True
                         self.prev = self.current
@@ -209,15 +209,15 @@
                 size = len(sc_list)
                 for i in range(size - 1, -1, -1):
                     sc: Scenario = sc_list[i]
                     child = sc.child_scenarios
                     if len(child) != 0:
                         self.stack.append(child)
 
-            while len(self.stack) is not 0:
+            while len(self.stack) != 0:
                 # current scenario list
                 self.current = self.stack[-1]
 
                 # From top to down
                 top_down = self.prev is not None and True in [(self.current == sc.child_scenarios) for sc in self.prev]
                 if self.prev is None or top_down:
                     # current is a list of scenario
```

### Comparing `teflo-2.3.0/teflo.egg-info/PKG-INFO` & `teflo-2.4.0/teflo.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: teflo
-Version: 2.3.0
+Version: 2.4.0
 Summary: Test Execution Framework Libraries and Objects. It is an orchestration software that controls the flow of a set of testing scenarios.
 Author: Red Hat Inc.
 License: GPLv3
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
 Classifier: Natural Language :: English
@@ -16,14 +16,18 @@
 Provides-Extra: openstack-client-plugin
 Provides-Extra: terraform-plugin
 Provides-Extra: webhook-notification-plugin
 Provides-Extra: notify-service-plugin
 License-File: LICENSE
 License-File: AUTHORS
 
+.. warning::
+    **This project is in maintenance mode and will not have any new feature development.**
+
+
 Welcome to Teflo!
 ==================
 
 What is Teflo?
 ---------------
 
 **TEFLO** stands for (**T** est **E** xecution **F** ramework **L** ibraries and **O** bjects)
```

### Comparing `teflo-2.3.0/teflo.egg-info/SOURCES.txt` & `teflo-2.4.0/teflo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `teflo-2.3.0/teflo.egg-info/entry_points.txt` & `teflo-2.4.0/teflo.egg-info/entry_points.txt`

 * *Files identical despite different names*

