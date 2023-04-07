# Comparing `tmp/cdktf-cdktf-provider-spotinst-5.0.8.tar.gz` & `tmp/cdktf-cdktf-provider-spotinst-5.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdktf-cdktf-provider-spotinst-5.0.8.tar", last modified: Wed Feb 15 13:43:31 2023, max compression
+gzip compressed data, was "cdktf-cdktf-provider-spotinst-5.0.9.tar", last modified: Thu Mar  2 15:10:51 2023, max compression
```

## Comparing `cdktf-cdktf-provider-spotinst-5.0.8.tar` & `cdktf-cdktf-provider-spotinst-5.0.9.tar`

### file list

```diff
@@ -1,83 +1,87 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    16012 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3998 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3089 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3652 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.557391 cdktf-cdktf-provider-spotinst-5.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.557391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/
--rw-r--r--   0 runner    (1001) docker     (123)     5194 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.557391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      419 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)  1749959 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/_jsii/provider-spotinst@5.0.8.jsii.tgz
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/data_integration/
--rw-r--r--   0 runner    (1001) docker     (123)    28689 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/data_integration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/
--rw-r--r--   0 runner    (1001) docker     (123)  1442198 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/
--rw-r--r--   0 runner    (1001) docker     (123)   139090 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/
--rw-r--r--   0 runner    (1001) docker     (123)    33139 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/
--rw-r--r--   0 runner    (1001) docker     (123)   407809 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/
--rw-r--r--   0 runner    (1001) docker     (123)   202698 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/
--rw-r--r--   0 runner    (1001) docker     (123)   502883 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.561391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/
--rw-r--r--   0 runner    (1001) docker     (123)   450058 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/health_check/
--rw-r--r--   0 runner    (1001) docker     (123)    47001 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/health_check/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/
--rw-r--r--   0 runner    (1001) docker     (123)   321072 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/
--rw-r--r--   0 runner    (1001) docker     (123)   578079 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_balancer/
--rw-r--r--   0 runner    (1001) docker     (123)    49042 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_balancer/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_deployment/
--rw-r--r--   0 runner    (1001) docker     (123)    17147 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_deployment/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_listener/
--rw-r--r--   0 runner    (1001) docker     (123)    58118 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_listener/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/
--rw-r--r--   0 runner    (1001) docker     (123)    47515 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target/
--rw-r--r--   0 runner    (1001) docker     (123)    43625 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target_set/
--rw-r--r--   0 runner    (1001) docker     (123)    63947 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target_set/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks/
--rw-r--r--   0 runner    (1001) docker     (123)   311547 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/
--rw-r--r--   0 runner    (1001) docker     (123)   161601 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws/
--rw-r--r--   0 runner    (1001) docker     (123)   355576 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/
--rw-r--r--   0 runner    (1001) docker     (123)    20454 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/
--rw-r--r--   0 runner    (1001) docker     (123)   376959 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.565391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs/
--rw-r--r--   0 runner    (1001) docker     (123)   380034 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/
--rw-r--r--   0 runner    (1001) docker     (123)   221508 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/
--rw-r--r--   0 runner    (1001) docker     (123)   238602 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/
--rw-r--r--   0 runner    (1001) docker     (123)   242624 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/
--rw-r--r--   0 runner    (1001) docker     (123)    19760 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_spark/
--rw-r--r--   0 runner    (1001) docker     (123)   100729 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_spark/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/provider/
--rw-r--r--   0 runner    (1001) docker     (123)    12451 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/provider/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/
--rw-r--r--   0 runner    (1001) docker     (123)   635674 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.569391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/subscription/
--rw-r--r--   0 runner    (1001) docker     (123)    25646 2023-02-15 13:43:19.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/subscription/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-15 13:43:31.557391 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3998 2023-02-15 13:43:31.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2547 2023-02-15 13:43:31.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-15 13:43:31.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-15 13:43:31.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-02-15 13:43:31.000000 cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    16012 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3227 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.303038 cdktf-cdktf-provider-spotinst-5.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.307039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/
+-rw-r--r--   0 runner    (1001) docker     (123)     5462 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.307039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      419 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)  4784544 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/_jsii/provider-spotinst@5.0.9.jsii.tgz
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.311039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/data_integration/
+-rw-r--r--   0 runner    (1001) docker     (123)    28689 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/data_integration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.311039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/
+-rw-r--r--   0 runner    (1001) docker     (123)  1442198 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/
+-rw-r--r--   0 runner    (1001) docker     (123)   139090 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/
+-rw-r--r--   0 runner    (1001) docker     (123)    33139 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/
+-rw-r--r--   0 runner    (1001) docker     (123)   407809 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/
+-rw-r--r--   0 runner    (1001) docker     (123)   202698 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/
+-rw-r--r--   0 runner    (1001) docker     (123)   502883 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/
+-rw-r--r--   0 runner    (1001) docker     (123)   450058 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/health_check/
+-rw-r--r--   0 runner    (1001) docker     (123)    47001 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/health_check/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/
+-rw-r--r--   0 runner    (1001) docker     (123)   321072 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.315039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/
+-rw-r--r--   0 runner    (1001) docker     (123)   578079 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_balancer/
+-rw-r--r--   0 runner    (1001) docker     (123)    49042 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_balancer/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_deployment/
+-rw-r--r--   0 runner    (1001) docker     (123)    17147 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_deployment/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_listener/
+-rw-r--r--   0 runner    (1001) docker     (123)    58118 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_listener/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/
+-rw-r--r--   0 runner    (1001) docker     (123)    47515 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target/
+-rw-r--r--   0 runner    (1001) docker     (123)    43625 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target_set/
+-rw-r--r--   0 runner    (1001) docker     (123)    63947 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target_set/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks/
+-rw-r--r--   0 runner    (1001) docker     (123)   311547 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks_np/
+-rw-r--r--   0 runner    (1001) docker     (123)   130783 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks_np/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/
+-rw-r--r--   0 runner    (1001) docker     (123)   161601 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws/
+-rw-r--r--   0 runner    (1001) docker     (123)   355576 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/
+-rw-r--r--   0 runner    (1001) docker     (123)    20454 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/
+-rw-r--r--   0 runner    (1001) docker     (123)   376959 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs/
+-rw-r--r--   0 runner    (1001) docker     (123)   380034 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.319038 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/
+-rw-r--r--   0 runner    (1001) docker     (123)   221508 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/
+-rw-r--r--   0 runner    (1001) docker     (123)   238602 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/
+-rw-r--r--   0 runner    (1001) docker     (123)   242624 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/
+-rw-r--r--   0 runner    (1001) docker     (123)    19760 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_spark/
+-rw-r--r--   0 runner    (1001) docker     (123)   108960 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_spark/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_spark_virtual_node_group/
+-rw-r--r--   0 runner    (1001) docker     (123)    20505 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_spark_virtual_node_group/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/provider/
+-rw-r--r--   0 runner    (1001) docker     (123)    12451 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/provider/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/
+-rw-r--r--   0 runner    (1001) docker     (123)   635674 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.323039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/subscription/
+-rw-r--r--   0 runner    (1001) docker     (123)    25646 2023-03-02 15:10:37.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/subscription/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-02 15:10:51.307039 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-03-02 15:10:51.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2683 2023-03-02 15:10:51.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-02 15:10:51.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-02 15:10:51.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-02 15:10:51.000000 cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/top_level.txt
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/LICENSE` & `cdktf-cdktf-provider-spotinst-5.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/PKG-INFO` & `cdktf-cdktf-provider-spotinst-5.0.9/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-cdktf-provider-spotinst
-Version: 5.0.8
+Version: 5.0.9
 Summary: Prebuilt spotinst Provider for Terraform CDK (cdktf)
 Home-page: https://github.com/cdktf/cdktf-provider-spotinst.git
 Author: HashiCorp
 License: MPL-2.0
 Project-URL: Source, https://github.com/cdktf/cdktf-provider-spotinst.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
@@ -61,15 +61,22 @@
 
 The go package is generated into the [`github.com/cdktf/cdktf-provider-spotinst-go`](https://github.com/cdktf/cdktf-provider-spotinst-go) package.
 
 `go get github.com/cdktf/cdktf-provider-spotinst-go/spotinst`
 
 ## Docs
 
-Find auto-generated docs for this provider here: [./API.md](./API.md)
+Find auto-generated docs for this provider here:
+
+* [Typescript](./docs/API.typescript.md)
+* [Python](./docs/API.python.md)
+* [Java](./docs/API.java.md)
+* [C#](./docs/API.csharp.md)
+* [Go](./docs/API.go.md)
+
 You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-spotinst).
 
 ## Versioning
 
 This project is explicitly not tracking the Terraform spotinst Provider version 1:1. In fact, it always tracks `latest` of `~> 1.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).
 
 These are the upstream dependencies:
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/README.md` & `cdktf-cdktf-provider-spotinst-5.0.9/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -38,15 +38,22 @@
 
 The go package is generated into the [`github.com/cdktf/cdktf-provider-spotinst-go`](https://github.com/cdktf/cdktf-provider-spotinst-go) package.
 
 `go get github.com/cdktf/cdktf-provider-spotinst-go/spotinst`
 
 ## Docs
 
-Find auto-generated docs for this provider here: [./API.md](./API.md)
+Find auto-generated docs for this provider here:
+
+* [Typescript](./docs/API.typescript.md)
+* [Python](./docs/API.python.md)
+* [Java](./docs/API.java.md)
+* [C#](./docs/API.csharp.md)
+* [Go](./docs/API.go.md)
+
 You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-spotinst).
 
 ## Versioning
 
 This project is explicitly not tracking the Terraform spotinst Provider version 1:1. In fact, it always tracks `latest` of `~> 1.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).
 
 These are the upstream dependencies:
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/setup.py` & `cdktf-cdktf-provider-spotinst-5.0.9/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdktf-cdktf-provider-spotinst",
-    "version": "5.0.8",
+    "version": "5.0.9",
     "description": "Prebuilt spotinst Provider for Terraform CDK (cdktf)",
     "license": "MPL-2.0",
     "url": "https://github.com/cdktf/cdktf-provider-spotinst.git",
     "long_description_content_type": "text/markdown",
     "author": "HashiCorp",
     "bdist_wheel": {
         "universal": true
@@ -37,41 +37,43 @@
         "cdktf_cdktf_provider_spotinst.multai_balancer",
         "cdktf_cdktf_provider_spotinst.multai_deployment",
         "cdktf_cdktf_provider_spotinst.multai_listener",
         "cdktf_cdktf_provider_spotinst.multai_routing_rule",
         "cdktf_cdktf_provider_spotinst.multai_target",
         "cdktf_cdktf_provider_spotinst.multai_target_set",
         "cdktf_cdktf_provider_spotinst.ocean_aks",
+        "cdktf_cdktf_provider_spotinst.ocean_aks_np",
         "cdktf_cdktf_provider_spotinst.ocean_aks_virtual_node_group",
         "cdktf_cdktf_provider_spotinst.ocean_aws",
         "cdktf_cdktf_provider_spotinst.ocean_aws_extended_resource_definition",
         "cdktf_cdktf_provider_spotinst.ocean_aws_launch_spec",
         "cdktf_cdktf_provider_spotinst.ocean_ecs",
         "cdktf_cdktf_provider_spotinst.ocean_ecs_launch_spec",
         "cdktf_cdktf_provider_spotinst.ocean_gke_import",
         "cdktf_cdktf_provider_spotinst.ocean_gke_launch_spec",
         "cdktf_cdktf_provider_spotinst.ocean_gke_launch_spec_import",
         "cdktf_cdktf_provider_spotinst.ocean_spark",
+        "cdktf_cdktf_provider_spotinst.ocean_spark_virtual_node_group",
         "cdktf_cdktf_provider_spotinst.provider",
         "cdktf_cdktf_provider_spotinst.stateful_node_azure",
         "cdktf_cdktf_provider_spotinst.subscription"
     ],
     "package_data": {
         "cdktf_cdktf_provider_spotinst._jsii": [
-            "provider-spotinst@5.0.8.jsii.tgz"
+            "provider-spotinst@5.0.9.jsii.tgz"
         ],
         "cdktf_cdktf_provider_spotinst": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
         "cdktf>=0.15.0, <0.16.0",
         "constructs>=10.0.0, <11.0.0",
-        "jsii>=1.75.0, <2.0.0",
+        "jsii>=1.76.0, <2.0.0",
         "publication>=0.0.3",
         "typeguard~=2.13.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
         "Programming Language :: JavaScript",
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -39,15 +39,22 @@
 
 The go package is generated into the [`github.com/cdktf/cdktf-provider-spotinst-go`](https://github.com/cdktf/cdktf-provider-spotinst-go) package.
 
 `go get github.com/cdktf/cdktf-provider-spotinst-go/spotinst`
 
 ## Docs
 
-Find auto-generated docs for this provider here: [./API.md](./API.md)
+Find auto-generated docs for this provider here:
+
+* [Typescript](./docs/API.typescript.md)
+* [Python](./docs/API.python.md)
+* [Java](./docs/API.java.md)
+* [C#](./docs/API.csharp.md)
+* [Go](./docs/API.go.md)
+
 You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-spotinst).
 
 ## Versioning
 
 This project is explicitly not tracking the Terraform spotinst Provider version 1:1. In fact, it always tracks `latest` of `~> 1.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).
 
 These are the upstream dependencies:
@@ -112,24 +119,26 @@
     "multai_balancer",
     "multai_deployment",
     "multai_listener",
     "multai_routing_rule",
     "multai_target",
     "multai_target_set",
     "ocean_aks",
+    "ocean_aks_np",
     "ocean_aks_virtual_node_group",
     "ocean_aws",
     "ocean_aws_extended_resource_definition",
     "ocean_aws_launch_spec",
     "ocean_ecs",
     "ocean_ecs_launch_spec",
     "ocean_gke_import",
     "ocean_gke_launch_spec",
     "ocean_gke_launch_spec_import",
     "ocean_spark",
+    "ocean_spark_virtual_node_group",
     "provider",
     "stateful_node_azure",
     "subscription",
 ]
 
 publication.publish()
 
@@ -148,20 +157,22 @@
 from . import multai_balancer
 from . import multai_deployment
 from . import multai_listener
 from . import multai_routing_rule
 from . import multai_target
 from . import multai_target_set
 from . import ocean_aks
+from . import ocean_aks_np
 from . import ocean_aks_virtual_node_group
 from . import ocean_aws
 from . import ocean_aws_extended_resource_definition
 from . import ocean_aws_launch_spec
 from . import ocean_ecs
 from . import ocean_ecs_launch_spec
 from . import ocean_gke_import
 from . import ocean_gke_launch_spec
 from . import ocean_gke_launch_spec_import
 from . import ocean_spark
+from . import ocean_spark_virtual_node_group
 from . import provider
 from . import stateful_node_azure
 from . import subscription
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/data_integration/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/data_integration/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/elastigroup_gke/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/health_check/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/health_check/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/managed_instance_aws/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/mrscaler_aws/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_balancer/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_balancer/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_deployment/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_deployment/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_listener/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_listener/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_routing_rule/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/multai_target_set/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/multai_target_set/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_import/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/ocean_spark/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/ocean_spark/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -34,14 +34,15 @@
         id_: builtins.str,
         *,
         ocean_cluster_id: builtins.str,
         compute: typing.Optional[typing.Union["OceanSparkCompute", typing.Dict[builtins.str, typing.Any]]] = None,
         id: typing.Optional[builtins.str] = None,
         ingress: typing.Optional[typing.Union["OceanSparkIngress", typing.Dict[builtins.str, typing.Any]]] = None,
         log_collection: typing.Optional[typing.Union["OceanSparkLogCollection", typing.Dict[builtins.str, typing.Any]]] = None,
+        spark: typing.Optional[typing.Union["OceanSparkSpark", typing.Dict[builtins.str, typing.Any]]] = None,
         webhook: typing.Optional[typing.Union["OceanSparkWebhook", typing.Dict[builtins.str, typing.Any]]] = None,
         connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
         count: typing.Optional[jsii.Number] = None,
         depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
         for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
         lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
         provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
@@ -52,14 +53,15 @@
         :param scope: The scope in which to define this construct.
         :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
         :param ocean_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ocean_cluster_id OceanSpark#ocean_cluster_id}.
         :param compute: compute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#compute OceanSpark#compute}
         :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#id OceanSpark#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
         :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ingress OceanSpark#ingress}
         :param log_collection: log_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
+        :param spark: spark block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#spark OceanSpark#spark}
         :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
         :param connection: 
         :param count: 
         :param depends_on: 
         :param for_each: 
         :param lifecycle: 
         :param provider: 
@@ -71,14 +73,15 @@
             check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
         config = OceanSparkConfig(
             ocean_cluster_id=ocean_cluster_id,
             compute=compute,
             id=id,
             ingress=ingress,
             log_collection=log_collection,
+            spark=spark,
             webhook=webhook,
             connection=connection,
             count=count,
             depends_on=depends_on,
             for_each=for_each,
             lifecycle=lifecycle,
             provider=provider,
@@ -138,14 +141,27 @@
         '''
         :param collect_driver_logs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#collect_driver_logs OceanSpark#collect_driver_logs}.
         '''
         value = OceanSparkLogCollection(collect_driver_logs=collect_driver_logs)
 
         return typing.cast(None, jsii.invoke(self, "putLogCollection", [value]))
 
+    @jsii.member(jsii_name="putSpark")
+    def put_spark(
+        self,
+        *,
+        additional_app_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
+    ) -> None:
+        '''
+        :param additional_app_namespaces: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#additional_app_namespaces OceanSpark#additional_app_namespaces}.
+        '''
+        value = OceanSparkSpark(additional_app_namespaces=additional_app_namespaces)
+
+        return typing.cast(None, jsii.invoke(self, "putSpark", [value]))
+
     @jsii.member(jsii_name="putWebhook")
     def put_webhook(
         self,
         *,
         host_network_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
         use_host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
     ) -> None:
@@ -171,14 +187,18 @@
     def reset_ingress(self) -> None:
         return typing.cast(None, jsii.invoke(self, "resetIngress", []))
 
     @jsii.member(jsii_name="resetLogCollection")
     def reset_log_collection(self) -> None:
         return typing.cast(None, jsii.invoke(self, "resetLogCollection", []))
 
+    @jsii.member(jsii_name="resetSpark")
+    def reset_spark(self) -> None:
+        return typing.cast(None, jsii.invoke(self, "resetSpark", []))
+
     @jsii.member(jsii_name="resetWebhook")
     def reset_webhook(self) -> None:
         return typing.cast(None, jsii.invoke(self, "resetWebhook", []))
 
     @jsii.member(jsii_name="synthesizeAttributes")
     def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
         return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))
@@ -200,14 +220,19 @@
 
     @builtins.property
     @jsii.member(jsii_name="logCollection")
     def log_collection(self) -> "OceanSparkLogCollectionOutputReference":
         return typing.cast("OceanSparkLogCollectionOutputReference", jsii.get(self, "logCollection"))
 
     @builtins.property
+    @jsii.member(jsii_name="spark")
+    def spark(self) -> "OceanSparkSparkOutputReference":
+        return typing.cast("OceanSparkSparkOutputReference", jsii.get(self, "spark"))
+
+    @builtins.property
     @jsii.member(jsii_name="webhook")
     def webhook(self) -> "OceanSparkWebhookOutputReference":
         return typing.cast("OceanSparkWebhookOutputReference", jsii.get(self, "webhook"))
 
     @builtins.property
     @jsii.member(jsii_name="computeInput")
     def compute_input(self) -> typing.Optional["OceanSparkCompute"]:
@@ -230,14 +255,19 @@
 
     @builtins.property
     @jsii.member(jsii_name="oceanClusterIdInput")
     def ocean_cluster_id_input(self) -> typing.Optional[builtins.str]:
         return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oceanClusterIdInput"))
 
     @builtins.property
+    @jsii.member(jsii_name="sparkInput")
+    def spark_input(self) -> typing.Optional["OceanSparkSpark"]:
+        return typing.cast(typing.Optional["OceanSparkSpark"], jsii.get(self, "sparkInput"))
+
+    @builtins.property
     @jsii.member(jsii_name="webhookInput")
     def webhook_input(self) -> typing.Optional["OceanSparkWebhook"]:
         return typing.cast(typing.Optional["OceanSparkWebhook"], jsii.get(self, "webhookInput"))
 
     @builtins.property
     @jsii.member(jsii_name="id")
     def id(self) -> builtins.str:
@@ -414,14 +444,15 @@
         "provider": "provider",
         "provisioners": "provisioners",
         "ocean_cluster_id": "oceanClusterId",
         "compute": "compute",
         "id": "id",
         "ingress": "ingress",
         "log_collection": "logCollection",
+        "spark": "spark",
         "webhook": "webhook",
     },
 )
 class OceanSparkConfig(_cdktf_9a9027ec.TerraformMetaArguments):
     def __init__(
         self,
         *,
@@ -433,14 +464,15 @@
         provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
         provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
         ocean_cluster_id: builtins.str,
         compute: typing.Optional[typing.Union[OceanSparkCompute, typing.Dict[builtins.str, typing.Any]]] = None,
         id: typing.Optional[builtins.str] = None,
         ingress: typing.Optional[typing.Union["OceanSparkIngress", typing.Dict[builtins.str, typing.Any]]] = None,
         log_collection: typing.Optional[typing.Union["OceanSparkLogCollection", typing.Dict[builtins.str, typing.Any]]] = None,
+        spark: typing.Optional[typing.Union["OceanSparkSpark", typing.Dict[builtins.str, typing.Any]]] = None,
         webhook: typing.Optional[typing.Union["OceanSparkWebhook", typing.Dict[builtins.str, typing.Any]]] = None,
     ) -> None:
         '''
         :param connection: 
         :param count: 
         :param depends_on: 
         :param for_each: 
@@ -448,24 +480,27 @@
         :param provider: 
         :param provisioners: 
         :param ocean_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ocean_cluster_id OceanSpark#ocean_cluster_id}.
         :param compute: compute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#compute OceanSpark#compute}
         :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#id OceanSpark#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
         :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#ingress OceanSpark#ingress}
         :param log_collection: log_collection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
+        :param spark: spark block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#spark OceanSpark#spark}
         :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
         '''
         if isinstance(lifecycle, dict):
             lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
         if isinstance(compute, dict):
             compute = OceanSparkCompute(**compute)
         if isinstance(ingress, dict):
             ingress = OceanSparkIngress(**ingress)
         if isinstance(log_collection, dict):
             log_collection = OceanSparkLogCollection(**log_collection)
+        if isinstance(spark, dict):
+            spark = OceanSparkSpark(**spark)
         if isinstance(webhook, dict):
             webhook = OceanSparkWebhook(**webhook)
         if __debug__:
             type_hints = typing.get_type_hints(_typecheckingstub__286ba412bd73327f01a051d064e2c7c310afd50b3674fc79fe0a7cedf108e461)
             check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
             check_type(argname="argument count", value=count, expected_type=type_hints["count"])
             check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
@@ -474,14 +509,15 @@
             check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
             check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
             check_type(argname="argument ocean_cluster_id", value=ocean_cluster_id, expected_type=type_hints["ocean_cluster_id"])
             check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
             check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
             check_type(argname="argument log_collection", value=log_collection, expected_type=type_hints["log_collection"])
+            check_type(argname="argument spark", value=spark, expected_type=type_hints["spark"])
             check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
         self._values: typing.Dict[builtins.str, typing.Any] = {
             "ocean_cluster_id": ocean_cluster_id,
         }
         if connection is not None:
             self._values["connection"] = connection
         if count is not None:
@@ -500,14 +536,16 @@
             self._values["compute"] = compute
         if id is not None:
             self._values["id"] = id
         if ingress is not None:
             self._values["ingress"] = ingress
         if log_collection is not None:
             self._values["log_collection"] = log_collection
+        if spark is not None:
+            self._values["spark"] = spark
         if webhook is not None:
             self._values["webhook"] = webhook
 
     @builtins.property
     def connection(
         self,
     ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
@@ -610,14 +648,23 @@
 
         Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#log_collection OceanSpark#log_collection}
         '''
         result = self._values.get("log_collection")
         return typing.cast(typing.Optional["OceanSparkLogCollection"], result)
 
     @builtins.property
+    def spark(self) -> typing.Optional["OceanSparkSpark"]:
+        '''spark block.
+
+        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#spark OceanSpark#spark}
+        '''
+        result = self._values.get("spark")
+        return typing.cast(typing.Optional["OceanSparkSpark"], result)
+
+    @builtins.property
     def webhook(self) -> typing.Optional["OceanSparkWebhook"]:
         '''webhook block.
 
         Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#webhook OceanSpark#webhook}
         '''
         result = self._values.get("webhook")
         return typing.cast(typing.Optional["OceanSparkWebhook"], result)
@@ -1576,14 +1623,109 @@
         if __debug__:
             type_hints = typing.get_type_hints(_typecheckingstub__ea419c886dfcc4e29c02e6958edb55f40a9a3b4d65ffb7faa4315508de762d57)
             check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "internalValue", value)
 
 
 @jsii.data_type(
+    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkSpark",
+    jsii_struct_bases=[],
+    name_mapping={"additional_app_namespaces": "additionalAppNamespaces"},
+)
+class OceanSparkSpark:
+    def __init__(
+        self,
+        *,
+        additional_app_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
+    ) -> None:
+        '''
+        :param additional_app_namespaces: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#additional_app_namespaces OceanSpark#additional_app_namespaces}.
+        '''
+        if __debug__:
+            type_hints = typing.get_type_hints(_typecheckingstub__49dd84e45632094a51989ef27d50d1e3000a28253cf98398f4bb775073934a6e)
+            check_type(argname="argument additional_app_namespaces", value=additional_app_namespaces, expected_type=type_hints["additional_app_namespaces"])
+        self._values: typing.Dict[builtins.str, typing.Any] = {}
+        if additional_app_namespaces is not None:
+            self._values["additional_app_namespaces"] = additional_app_namespaces
+
+    @builtins.property
+    def additional_app_namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
+        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/ocean_spark#additional_app_namespaces OceanSpark#additional_app_namespaces}.'''
+        result = self._values.get("additional_app_namespaces")
+        return typing.cast(typing.Optional[typing.List[builtins.str]], result)
+
+    def __eq__(self, rhs: typing.Any) -> builtins.bool:
+        return isinstance(rhs, self.__class__) and rhs._values == self._values
+
+    def __ne__(self, rhs: typing.Any) -> builtins.bool:
+        return not (rhs == self)
+
+    def __repr__(self) -> str:
+        return "OceanSparkSpark(%s)" % ", ".join(
+            k + "=" + repr(v) for k, v in self._values.items()
+        )
+
+
+class OceanSparkSparkOutputReference(
+    _cdktf_9a9027ec.ComplexObject,
+    metaclass=jsii.JSIIMeta,
+    jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkSparkOutputReference",
+):
+    def __init__(
+        self,
+        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
+        terraform_attribute: builtins.str,
+    ) -> None:
+        '''
+        :param terraform_resource: The parent resource.
+        :param terraform_attribute: The attribute on the parent resource this class is referencing.
+        '''
+        if __debug__:
+            type_hints = typing.get_type_hints(_typecheckingstub__0b0c6c0e656cdc0e6e74ba02cc9f447fc11f59395b33daa7c5fc1c8862197c39)
+            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
+            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
+        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])
+
+    @jsii.member(jsii_name="resetAdditionalAppNamespaces")
+    def reset_additional_app_namespaces(self) -> None:
+        return typing.cast(None, jsii.invoke(self, "resetAdditionalAppNamespaces", []))
+
+    @builtins.property
+    @jsii.member(jsii_name="additionalAppNamespacesInput")
+    def additional_app_namespaces_input(
+        self,
+    ) -> typing.Optional[typing.List[builtins.str]]:
+        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalAppNamespacesInput"))
+
+    @builtins.property
+    @jsii.member(jsii_name="additionalAppNamespaces")
+    def additional_app_namespaces(self) -> typing.List[builtins.str]:
+        return typing.cast(typing.List[builtins.str], jsii.get(self, "additionalAppNamespaces"))
+
+    @additional_app_namespaces.setter
+    def additional_app_namespaces(self, value: typing.List[builtins.str]) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(_typecheckingstub__9e707824e5405ff3cd1596c4ee61db254f85eafe00a376e4312de073a2690c7c)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
+        jsii.set(self, "additionalAppNamespaces", value)
+
+    @builtins.property
+    @jsii.member(jsii_name="internalValue")
+    def internal_value(self) -> typing.Optional[OceanSparkSpark]:
+        return typing.cast(typing.Optional[OceanSparkSpark], jsii.get(self, "internalValue"))
+
+    @internal_value.setter
+    def internal_value(self, value: typing.Optional[OceanSparkSpark]) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(_typecheckingstub__f921376bdbad90f8cb0f8394698b7fb328ed043cb4c3deb339bb2dd5db1d9b7f)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
+        jsii.set(self, "internalValue", value)
+
+
+@jsii.data_type(
     jsii_type="@cdktf/provider-spotinst.oceanSpark.OceanSparkWebhook",
     jsii_struct_bases=[],
     name_mapping={
         "host_network_ports": "hostNetworkPorts",
         "use_host_network": "useHostNetwork",
     },
 )
@@ -1729,14 +1871,16 @@
     "OceanSparkIngressLoadBalancer",
     "OceanSparkIngressLoadBalancerOutputReference",
     "OceanSparkIngressOutputReference",
     "OceanSparkIngressPrivateLink",
     "OceanSparkIngressPrivateLinkOutputReference",
     "OceanSparkLogCollection",
     "OceanSparkLogCollectionOutputReference",
+    "OceanSparkSpark",
+    "OceanSparkSparkOutputReference",
     "OceanSparkWebhook",
     "OceanSparkWebhookOutputReference",
 ]
 
 publication.publish()
 
 def _typecheckingstub__e1b1c4bc9ac16a6f54df9d8f9743a0efcb7223d78fdd53130efcce6d47647516(
@@ -1744,14 +1888,15 @@
     id_: builtins.str,
     *,
     ocean_cluster_id: builtins.str,
     compute: typing.Optional[typing.Union[OceanSparkCompute, typing.Dict[builtins.str, typing.Any]]] = None,
     id: typing.Optional[builtins.str] = None,
     ingress: typing.Optional[typing.Union[OceanSparkIngress, typing.Dict[builtins.str, typing.Any]]] = None,
     log_collection: typing.Optional[typing.Union[OceanSparkLogCollection, typing.Dict[builtins.str, typing.Any]]] = None,
+    spark: typing.Optional[typing.Union[OceanSparkSpark, typing.Dict[builtins.str, typing.Any]]] = None,
     webhook: typing.Optional[typing.Union[OceanSparkWebhook, typing.Dict[builtins.str, typing.Any]]] = None,
     connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
     count: typing.Optional[jsii.Number] = None,
     depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
     for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
     lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
     provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
@@ -1815,14 +1960,15 @@
     provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
     provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
     ocean_cluster_id: builtins.str,
     compute: typing.Optional[typing.Union[OceanSparkCompute, typing.Dict[builtins.str, typing.Any]]] = None,
     id: typing.Optional[builtins.str] = None,
     ingress: typing.Optional[typing.Union[OceanSparkIngress, typing.Dict[builtins.str, typing.Any]]] = None,
     log_collection: typing.Optional[typing.Union[OceanSparkLogCollection, typing.Dict[builtins.str, typing.Any]]] = None,
+    spark: typing.Optional[typing.Union[OceanSparkSpark, typing.Dict[builtins.str, typing.Any]]] = None,
     webhook: typing.Optional[typing.Union[OceanSparkWebhook, typing.Dict[builtins.str, typing.Any]]] = None,
 ) -> None:
     """Type checking stubs"""
     pass
 
 def _typecheckingstub__6fd91c4f0dc4e99a521b8c57bef0287eccf40665d7b8ddff0bd024aa3d5bb839(
     *,
@@ -2008,14 +2154,40 @@
 
 def _typecheckingstub__ea419c886dfcc4e29c02e6958edb55f40a9a3b4d65ffb7faa4315508de762d57(
     value: typing.Optional[OceanSparkLogCollection],
 ) -> None:
     """Type checking stubs"""
     pass
 
+def _typecheckingstub__49dd84e45632094a51989ef27d50d1e3000a28253cf98398f4bb775073934a6e(
+    *,
+    additional_app_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__0b0c6c0e656cdc0e6e74ba02cc9f447fc11f59395b33daa7c5fc1c8862197c39(
+    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
+    terraform_attribute: builtins.str,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__9e707824e5405ff3cd1596c4ee61db254f85eafe00a376e4312de073a2690c7c(
+    value: typing.List[builtins.str],
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__f921376bdbad90f8cb0f8394698b7fb328ed043cb4c3deb339bb2dd5db1d9b7f(
+    value: typing.Optional[OceanSparkSpark],
+) -> None:
+    """Type checking stubs"""
+    pass
+
 def _typecheckingstub__a2b53f4137a911f81713ecd8268cd2c17403b2a0b71d0d3f7497a6d4b3cad3d3(
     *,
     host_network_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
     use_host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
 ) -> None:
     """Type checking stubs"""
     pass
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/provider/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/provider/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/stateful_node_azure/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst/subscription/__init__.py` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst/subscription/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/PKG-INFO` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-cdktf-provider-spotinst
-Version: 5.0.8
+Version: 5.0.9
 Summary: Prebuilt spotinst Provider for Terraform CDK (cdktf)
 Home-page: https://github.com/cdktf/cdktf-provider-spotinst.git
 Author: HashiCorp
 License: MPL-2.0
 Project-URL: Source, https://github.com/cdktf/cdktf-provider-spotinst.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
@@ -61,15 +61,22 @@
 
 The go package is generated into the [`github.com/cdktf/cdktf-provider-spotinst-go`](https://github.com/cdktf/cdktf-provider-spotinst-go) package.
 
 `go get github.com/cdktf/cdktf-provider-spotinst-go/spotinst`
 
 ## Docs
 
-Find auto-generated docs for this provider here: [./API.md](./API.md)
+Find auto-generated docs for this provider here:
+
+* [Typescript](./docs/API.typescript.md)
+* [Python](./docs/API.python.md)
+* [Java](./docs/API.java.md)
+* [C#](./docs/API.csharp.md)
+* [Go](./docs/API.go.md)
+
 You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-spotinst).
 
 ## Versioning
 
 This project is explicitly not tracking the Terraform spotinst Provider version 1:1. In fact, it always tracks `latest` of `~> 1.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).
 
 These are the upstream dependencies:
```

### Comparing `cdktf-cdktf-provider-spotinst-5.0.8/src/cdktf_cdktf_provider_spotinst.egg-info/SOURCES.txt` & `cdktf-cdktf-provider-spotinst-5.0.9/src/cdktf_cdktf_provider_spotinst.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 src/cdktf_cdktf_provider_spotinst/py.typed
 src/cdktf_cdktf_provider_spotinst.egg-info/PKG-INFO
 src/cdktf_cdktf_provider_spotinst.egg-info/SOURCES.txt
 src/cdktf_cdktf_provider_spotinst.egg-info/dependency_links.txt
 src/cdktf_cdktf_provider_spotinst.egg-info/requires.txt
 src/cdktf_cdktf_provider_spotinst.egg-info/top_level.txt
 src/cdktf_cdktf_provider_spotinst/_jsii/__init__.py
-src/cdktf_cdktf_provider_spotinst/_jsii/provider-spotinst@5.0.8.jsii.tgz
+src/cdktf_cdktf_provider_spotinst/_jsii/provider-spotinst@5.0.9.jsii.tgz
 src/cdktf_cdktf_provider_spotinst/data_integration/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_aws/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_aws_beanstalk/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_aws_suspension/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_azure/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_azure_v3/__init__.py
 src/cdktf_cdktf_provider_spotinst/elastigroup_gcp/__init__.py
@@ -26,20 +26,22 @@
 src/cdktf_cdktf_provider_spotinst/multai_balancer/__init__.py
 src/cdktf_cdktf_provider_spotinst/multai_deployment/__init__.py
 src/cdktf_cdktf_provider_spotinst/multai_listener/__init__.py
 src/cdktf_cdktf_provider_spotinst/multai_routing_rule/__init__.py
 src/cdktf_cdktf_provider_spotinst/multai_target/__init__.py
 src/cdktf_cdktf_provider_spotinst/multai_target_set/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_aks/__init__.py
+src/cdktf_cdktf_provider_spotinst/ocean_aks_np/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_aks_virtual_node_group/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_aws/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_aws_extended_resource_definition/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_aws_launch_spec/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_ecs/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_ecs_launch_spec/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_gke_import/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_gke_launch_spec_import/__init__.py
 src/cdktf_cdktf_provider_spotinst/ocean_spark/__init__.py
+src/cdktf_cdktf_provider_spotinst/ocean_spark_virtual_node_group/__init__.py
 src/cdktf_cdktf_provider_spotinst/provider/__init__.py
 src/cdktf_cdktf_provider_spotinst/stateful_node_azure/__init__.py
 src/cdktf_cdktf_provider_spotinst/subscription/__init__.py
```

