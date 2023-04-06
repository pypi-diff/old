# Comparing `tmp/e2e_cli-0.9.8.tar.gz` & `tmp/e2e_cli-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "e2e_cli-0.9.8.tar", last modified: Thu Mar 30 12:20:44 2023, max compression
+gzip compressed data, was "e2e_cli-0.9.9.tar", last modified: Thu Apr  6 13:42:01 2023, max compression
```

## Comparing `e2e_cli-0.9.8.tar` & `e2e_cli-0.9.9.tar`

### file list

```diff
@@ -1,106 +1,106 @@
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.555973 e2e_cli-0.9.8/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/LICENSE
--rw-rw-r--   0 aman      (1000) aman      (1000)       31 2023-03-03 10:09:05.000000 e2e_cli-0.9.8/MANIFEST.in
--rw-rw-r--   0 aman      (1000) aman      (1000)      227 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/PKG-INFO
--rw-rw-r--   0 aman      (1000) aman      (1000)     6237 2023-03-03 09:45:02.000000 e2e_cli-0.9.8/README.md
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/auto_scaling/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:32.000000 e2e_cli-0.9.8/e2e_cli/auto_scaling/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3839 2023-03-24 07:07:56.000000 e2e_cli-0.9.8/e2e_cli/auto_scaling/auto_scaling.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1833 2023-03-29 12:10:32.000000 e2e_cli-0.9.8/e2e_cli/auto_scaling/autoscaling_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/bucket_store/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_actions/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-20 13:31:40.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_actions/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     8261 2023-03-24 07:11:49.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_actions/bucket_actions.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:41.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3761 2023-03-27 12:55:58.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_crud/bucket_storage.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     4935 2023-03-22 06:02:51.000000 e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/cdn/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/cdn/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/cdn/cdn_actions/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:23.000000 e2e_cli-0.9.8/e2e_cli/cdn/cdn_actions/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3123 2023-03-24 07:02:00.000000 e2e_cli-0.9.8/e2e_cli/cdn/cdn_actions/cdn_action.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/cdn/cdn_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:19.000000 e2e_cli-0.9.8/e2e_cli/cdn/cdn_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3579 2023-03-24 07:00:47.000000 e2e_cli-0.9.8/e2e_cli/cdn/cdn_crud/cdn.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3189 2023-03-21 12:29:16.000000 e2e_cli-0.9.8/e2e_cli/cdn/cdn_routing.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     5249 2023-03-30 11:36:44.000000 e2e_cli-0.9.8/e2e_cli/commands_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli/config/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/config/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     5781 2023-03-29 11:42:25.000000 e2e_cli-0.9.8/e2e_cli/config/config.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1898 2023-03-29 12:04:10.000000 e2e_cli-0.9.8/e2e_cli/config/config_routing.py
--rw-rw-r--   0 aman      (1000) aman      (1000)      372 2023-03-24 06:11:14.000000 e2e_cli-0.9.8/e2e_cli/config/config_service.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/core/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/core/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1643 2023-03-29 11:45:05.000000 e2e_cli-0.9.8/e2e_cli/core/alias_service.py
--rw-rw-r--   0 aman      (1000) aman      (1000)      494 2023-03-30 12:12:51.000000 e2e_cli-0.9.8/e2e_cli/core/constants.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3639 2023-03-10 13:20:42.000000 e2e_cli-0.9.8/e2e_cli/core/error_logs_service.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     5251 2023-03-30 11:38:57.000000 e2e_cli-0.9.8/e2e_cli/core/help_messages.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3300 2023-03-24 10:04:56.000000 e2e_cli-0.9.8/e2e_cli/core/helper_service.py
--rw-rw-r--   0 aman      (1000) aman      (1000)      648 2023-03-30 10:22:40.000000 e2e_cli-0.9.8/e2e_cli/core/py_manager.py
--rw-rw-r--   0 aman      (1000) aman      (1000)      455 2023-03-21 09:56:43.000000 e2e_cli-0.9.8/e2e_cli/core/request_service.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/dbaas/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/dbaas/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_actions/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:07.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_actions/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     8227 2023-03-24 07:03:10.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_actions/dbaas_action.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:03.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     5221 2023-03-24 06:12:26.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/dbaas.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     8922 2023-03-24 06:22:28.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/dbaas_services.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     7157 2023-03-29 12:09:20.000000 e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/docs/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/docs/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     8402 2023-03-24 16:57:39.000000 e2e_cli-0.9.8/e2e_cli/docs/e2e_cli.1
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/image/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 14:00:12.000000 e2e_cli-0.9.8/e2e_cli/image/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/image/image_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 10:56:29.000000 e2e_cli-0.9.8/e2e_cli/image/image_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3550 2023-03-24 06:10:02.000000 e2e_cli-0.9.8/e2e_cli/image/image_crud/image.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/image/image_listing/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 10:56:22.000000 e2e_cli-0.9.8/e2e_cli/image/image_listing/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1365 2023-03-24 06:10:02.000000 e2e_cli-0.9.8/e2e_cli/image/image_listing/image_list.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     2734 2023-03-22 11:04:30.000000 e2e_cli-0.9.8/e2e_cli/image/image_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/loadbalancer/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/loadbalancer/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     4406 2023-03-02 07:23:13.000000 e2e_cli-0.9.8/e2e_cli/loadbalancer/lb.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     2617 2023-03-29 11:24:45.000000 e2e_cli-0.9.8/e2e_cli/loadbalancer/lb_routing.py
--rw-rw-r--   0 aman      (1000) aman      (1000)    42484 2023-03-24 06:23:22.000000 e2e_cli-0.9.8/e2e_cli/loadbalancer/lb_services.py
--rw-rw-r--   0 aman      (1000) aman      (1000)    12444 2023-03-30 12:04:39.000000 e2e_cli-0.9.8/e2e_cli/main.py
--rw-rw-r--   0 aman      (1000) aman      (1000)      459 2023-03-30 07:20:32.000000 e2e_cli-0.9.8/e2e_cli/man_display.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/node/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/node/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/node/node_actions/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 08:09:56.000000 e2e_cli-0.9.8/e2e_cli/node/node_actions/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     7873 2023-03-24 06:24:03.000000 e2e_cli-0.9.8/e2e_cli/node/node_actions/node_action.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/node/node_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 14:01:01.000000 e2e_cli-0.9.8/e2e_cli/node/node_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     6462 2023-03-29 12:20:43.000000 e2e_cli-0.9.8/e2e_cli/node/node_crud/node.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3666 2023-03-24 06:25:30.000000 e2e_cli-0.9.8/e2e_cli/node/node_crud/node_listing_service.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     6029 2023-03-29 11:48:20.000000 e2e_cli-0.9.8/e2e_cli/node/node_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/volumes/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.8/e2e_cli/volumes/__init__.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/volumes/volumes_actions/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 09:26:32.000000 e2e_cli-0.9.8/e2e_cli/volumes/volumes_actions/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1839 2023-03-24 06:28:30.000000 e2e_cli-0.9.8/e2e_cli/volumes/volumes_actions/volumes_action.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/volumes/volumes_crud/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 09:26:32.000000 e2e_cli-0.9.8/e2e_cli/volumes/volumes_crud/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3683 2023-03-24 06:10:02.000000 e2e_cli-0.9.8/e2e_cli/volumes/volumes_crud/volumes.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     2651 2023-03-22 10:46:32.000000 e2e_cli-0.9.8/e2e_cli/volumes/volumes_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.551973 e2e_cli-0.9.8/e2e_cli/vpc/
--rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:29:40.000000 e2e_cli-0.9.8/e2e_cli/vpc/__init__.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     3472 2023-03-24 06:29:17.000000 e2e_cli-0.9.8/e2e_cli/vpc/vpc.py
--rw-rw-r--   0 aman      (1000) aman      (1000)     1703 2023-03-29 12:12:00.000000 e2e_cli-0.9.8/e2e_cli/vpc/vpc_routing.py
-drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-03-30 12:20:44.547973 e2e_cli-0.9.8/e2e_cli.egg-info/
--rw-rw-r--   0 aman      (1000) aman      (1000)      227 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/PKG-INFO
--rw-rw-r--   0 aman      (1000) aman      (1000)     2450 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/SOURCES.txt
--rw-rw-r--   0 aman      (1000) aman      (1000)        1 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/dependency_links.txt
--rw-rw-r--   0 aman      (1000) aman      (1000)       57 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/entry_points.txt
--rw-rw-r--   0 aman      (1000) aman      (1000)       40 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/requires.txt
--rw-rw-r--   0 aman      (1000) aman      (1000)        8 2023-03-30 12:20:44.000000 e2e_cli-0.9.8/e2e_cli.egg-info/top_level.txt
--rw-rw-r--   0 aman      (1000) aman      (1000)      432 2023-03-30 07:14:12.000000 e2e_cli-0.9.8/install_man.py
--rw-rw-r--   0 aman      (1000) aman      (1000)       38 2023-03-30 12:20:44.555973 e2e_cli-0.9.8/setup.cfg
--rw-rw-r--   0 aman      (1000) aman      (1000)      735 2023-03-30 12:20:39.000000 e2e_cli-0.9.8/setup.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/LICENSE
+-rw-rw-r--   0 aman      (1000) aman      (1000)       31 2023-03-03 10:09:05.000000 e2e_cli-0.9.9/MANIFEST.in
+-rw-rw-r--   0 aman      (1000) aman      (1000)      227 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/PKG-INFO
+-rw-rw-r--   0 aman      (1000) aman      (1000)     6237 2023-03-03 09:45:02.000000 e2e_cli-0.9.9/README.md
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/auto_scaling/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:32.000000 e2e_cli-0.9.9/e2e_cli/auto_scaling/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3934 2023-04-06 09:40:06.000000 e2e_cli-0.9.9/e2e_cli/auto_scaling/auto_scaling.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2000 2023-04-06 11:22:35.000000 e2e_cli-0.9.9/e2e_cli/auto_scaling/autoscaling_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/bucket_store/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_actions/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-20 13:31:40.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_actions/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     8271 2023-04-06 10:32:48.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_actions/bucket_actions.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:41.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3848 2023-04-06 10:15:21.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_crud/bucket_storage.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     4485 2023-04-06 11:22:16.000000 e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/cdn/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/cdn/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/cdn/cdn_actions/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:23.000000 e2e_cli-0.9.9/e2e_cli/cdn/cdn_actions/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3135 2023-04-06 11:06:02.000000 e2e_cli-0.9.9/e2e_cli/cdn/cdn_actions/cdn_action.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/cdn/cdn_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:19.000000 e2e_cli-0.9.9/e2e_cli/cdn/cdn_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3598 2023-04-06 10:59:59.000000 e2e_cli-0.9.9/e2e_cli/cdn/cdn_crud/cdn.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3126 2023-04-06 11:22:26.000000 e2e_cli-0.9.9/e2e_cli/cdn/cdn_routing.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     6044 2023-04-06 09:55:18.000000 e2e_cli-0.9.9/e2e_cli/commands_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/config/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/config/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     6612 2023-04-06 09:09:02.000000 e2e_cli-0.9.9/e2e_cli/config/config.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3081 2023-04-06 12:27:41.000000 e2e_cli-0.9.9/e2e_cli/config/config_routing.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)      372 2023-03-24 06:11:14.000000 e2e_cli-0.9.9/e2e_cli/config/config_service.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/core/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/core/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2192 2023-04-06 08:56:51.000000 e2e_cli-0.9.9/e2e_cli/core/alias_service.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)      494 2023-03-30 12:12:51.000000 e2e_cli-0.9.9/e2e_cli/core/constants.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3639 2023-03-10 13:20:42.000000 e2e_cli-0.9.9/e2e_cli/core/error_logs_service.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     1797 2023-04-04 13:21:23.000000 e2e_cli-0.9.9/e2e_cli/core/help_messages.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3263 2023-04-06 09:53:11.000000 e2e_cli-0.9.9/e2e_cli/core/helper_service.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)      657 2023-04-04 12:06:28.000000 e2e_cli-0.9.9/e2e_cli/core/py_manager.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)      455 2023-03-21 09:56:43.000000 e2e_cli-0.9.9/e2e_cli/core/request_service.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/dbaas/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/dbaas/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_actions/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:07.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_actions/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     8272 2023-04-06 12:16:27.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_actions/dbaas_action.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:23:03.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     5221 2023-03-24 06:12:26.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/dbaas.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     8922 2023-03-24 06:22:28.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/dbaas_services.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     5036 2023-04-06 12:18:07.000000 e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/docs/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/docs/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     8402 2023-03-24 16:57:39.000000 e2e_cli-0.9.9/e2e_cli/docs/e2e_cli.1
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/image/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 14:00:12.000000 e2e_cli-0.9.9/e2e_cli/image/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/image/image_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 10:56:29.000000 e2e_cli-0.9.9/e2e_cli/image/image_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3345 2023-04-06 12:57:23.000000 e2e_cli-0.9.9/e2e_cli/image/image_crud/image.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/image/image_listing/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 10:56:22.000000 e2e_cli-0.9.9/e2e_cli/image/image_listing/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     1365 2023-03-24 06:10:02.000000 e2e_cli-0.9.9/e2e_cli/image/image_listing/image_list.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2674 2023-04-06 12:50:42.000000 e2e_cli-0.9.9/e2e_cli/image/image_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/loadbalancer/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/loadbalancer/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     4406 2023-03-02 07:23:13.000000 e2e_cli-0.9.9/e2e_cli/loadbalancer/lb.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     1530 2023-04-06 13:10:48.000000 e2e_cli-0.9.9/e2e_cli/loadbalancer/lb_routing.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)    42484 2023-03-24 06:23:22.000000 e2e_cli-0.9.9/e2e_cli/loadbalancer/lb_services.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)    14058 2023-04-06 09:52:54.000000 e2e_cli-0.9.9/e2e_cli/main.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)      459 2023-03-31 06:51:42.000000 e2e_cli-0.9.9/e2e_cli/man_display.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/node/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/node/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/node/node_actions/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 08:09:56.000000 e2e_cli-0.9.9/e2e_cli/node/node_actions/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     8036 2023-04-04 12:12:13.000000 e2e_cli-0.9.9/e2e_cli/node/node_actions/node_action.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/node/node_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-17 14:01:01.000000 e2e_cli-0.9.9/e2e_cli/node/node_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     6414 2023-04-05 05:52:33.000000 e2e_cli-0.9.9/e2e_cli/node/node_crud/node.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3666 2023-03-24 06:25:30.000000 e2e_cli-0.9.9/e2e_cli/node/node_crud/node_listing_service.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     5378 2023-04-04 12:11:05.000000 e2e_cli-0.9.9/e2e_cli/node/node_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/volumes/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-02-17 14:04:58.000000 e2e_cli-0.9.9/e2e_cli/volumes/__init__.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/volumes/volumes_actions/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 09:26:32.000000 e2e_cli-0.9.9/e2e_cli/volumes/volumes_actions/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     1839 2023-03-24 06:28:30.000000 e2e_cli-0.9.9/e2e_cli/volumes/volumes_actions/volumes_action.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/volumes/volumes_crud/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 09:26:32.000000 e2e_cli-0.9.9/e2e_cli/volumes/volumes_crud/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3749 2023-04-06 13:35:14.000000 e2e_cli-0.9.9/e2e_cli/volumes/volumes_crud/volumes.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2809 2023-04-06 13:17:35.000000 e2e_cli-0.9.9/e2e_cli/volumes/volumes_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/e2e_cli/vpc/
+-rw-rw-r--   0 aman      (1000) aman      (1000)        0 2023-03-22 08:29:40.000000 e2e_cli-0.9.9/e2e_cli/vpc/__init__.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     3510 2023-04-06 13:38:49.000000 e2e_cli-0.9.9/e2e_cli/vpc/vpc.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2142 2023-04-06 13:34:46.000000 e2e_cli-0.9.9/e2e_cli/vpc/vpc_routing.py
+drwxrwxr-x   0 aman      (1000) aman      (1000)        0 2023-04-06 13:42:01.902504 e2e_cli-0.9.9/e2e_cli.egg-info/
+-rw-rw-r--   0 aman      (1000) aman      (1000)      227 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/PKG-INFO
+-rw-rw-r--   0 aman      (1000) aman      (1000)     2450 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/SOURCES.txt
+-rw-rw-r--   0 aman      (1000) aman      (1000)        1 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/dependency_links.txt
+-rw-rw-r--   0 aman      (1000) aman      (1000)       57 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/entry_points.txt
+-rw-rw-r--   0 aman      (1000) aman      (1000)       40 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/requires.txt
+-rw-rw-r--   0 aman      (1000) aman      (1000)        8 2023-04-06 13:42:01.000000 e2e_cli-0.9.9/e2e_cli.egg-info/top_level.txt
+-rw-rw-r--   0 aman      (1000) aman      (1000)      432 2023-03-30 07:14:12.000000 e2e_cli-0.9.9/install_man.py
+-rw-rw-r--   0 aman      (1000) aman      (1000)       38 2023-04-06 13:42:01.906504 e2e_cli-0.9.9/setup.cfg
+-rw-rw-r--   0 aman      (1000) aman      (1000)      735 2023-04-06 13:41:47.000000 e2e_cli-0.9.9/setup.py
```

### Comparing `e2e_cli-0.9.8/README.md` & `e2e_cli-0.9.9/README.md`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/auto_scaling/auto_scaling.py` & `e2e_cli-0.9.9/e2e_cli/auto_scaling/auto_scaling.py`

 * *Files 4% similar despite different names*

```diff
@@ -42,29 +42,30 @@
         #               return
                   
         # Checks.show_json(status)    
 
 
     def delete_autoscaling(self):
         my_payload={}
-        autoscaling_id=Py_version_manager.py_input("input id of the autoscaling you want to delete : ")
+        autoscaling_id=Checks.take_input(self.kwargs["inputs"], "autoscaling_id")
         while(not Checks.is_int(autoscaling_id)):
                 autoscaling_id=Py_version_manager.py_input("Only integers allowed ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/scaler/scalegroups/"+ autoscaling_id +"?apikey="+API_key
         req="DELETE"
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         if Checks.status_result(status,req):
                         Py_version_manager.py_print("autoscaling Successfully deleted")
                         Py_version_manager.py_print("use following command -> e2e_cli <alias> autoscaling list to check if autoscaling has been deleted")
         
-        Checks.show_json(status)
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
 
 
     def list_autoscaling(self):
         my_payload={}
         API_key= self.API_key  
         Auth_Token= self.Auth_Token 
         url =  BASE_URL+"myaccount/api/v1/scaler/scalegroups?apikey="+ API_key+"&location=Delhi"
@@ -79,13 +80,13 @@
                     x = PrettyTable()
                     x.field_names = ["index", "ID", "Policy", "Name", "Max_nodes", "Min_nodes"]
                     for element in list:
                         x.add_row([i, element['id'], element['policy'], element['name'], element['max_nodes'], element["min_nodes"]])
                         i = i+1
                     Py_version_manager.py_print(x)
                 except Exception as e:
-                      Checks.show_json(status, e)
-                      return
-
-        Checks.show_json(status)
+                      Py_version_manager.py_print("Errors : ", e)
+                        
+        if('json' in self.kwargs["inputs"]):
+                    Checks.show_json(status)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/auto_scaling/autoscaling_routing.py` & `e2e_cli-0.9.9/e2e_cli/vpc/vpc_routing.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,40 +1,49 @@
 import subprocess
 
 from e2e_cli.core.py_manager import Py_version_manager
-from e2e_cli.auto_scaling.auto_scaling import autoscaling_Crud
+from e2e_cli.vpc.vpc import vpc_Crud
 
-class autoscaling_Routing:
+class vpc_Routing:
     def __init__(self, arguments):
         self.arguments = arguments
         
         
-    def route(self):
-        if (self.arguments.autoscaling_commands is None):
-            subprocess.call(['e2e_cli', 'alias', 'autoscaling', '-h'])
-
-        # elif (self.arguments.autoscaling_commands is not None) and (self.arguments.action is not None):
-        #       Py_version_manager.py_print("Only one action at a time !!")
-
-        elif self.arguments.autoscaling_commands == 'create':
-            auto_scaling_operations = autoscaling_Crud(alias=self.arguments.alias )
-            if(auto_scaling_operations.possible):
-                        try:
-                            auto_scaling_operations.create_autoscaling()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-
-        elif self.arguments.autoscaling_commands == 'delete':
-            auto_scaling_operations = autoscaling_Crud(alias=self.arguments.alias)
-            if(auto_scaling_operations.possible):
-                        try:
-                            auto_scaling_operations.delete_autoscaling()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-        elif self.arguments.autoscaling_commands == 'list':
-            auto_scaling_operations = autoscaling_Crud(alias=self.arguments.alias)
-            if(auto_scaling_operations.possible):
-                        try:
-                            auto_scaling_operations.list_autoscaling()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.vpc_commands is None):
+            subprocess.call(['e2e_cli', 'alias', 'vpc', '-h'])
+
+
+        elif (self.arguments.args.vpc_commands is not None) and (self.arguments.args.action is not None):
+            Py_version_manager.py_print("Only one action at a time !!")
+
+
+        elif (self.arguments.args.vpc_commands is not None):
+            vpc_operations = vpc_Crud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+            if(vpc_operations.possible):  
+
+                if self.arguments.args.vpc_commands == 'create':
+                                try:
+                                    vpc_operations.create_vpc()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+
+                elif self.arguments.args.vpc_commands == 'delete':
+                    vpc_operations = vpc_Crud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+                    if(vpc_operations.possible):
+                                try:
+                                    vpc_operations.delete_vpc()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+                                
+                elif self.arguments.args.vpc_commands == 'list':
+                    vpc_operations = vpc_Crud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+                    if(vpc_operations.possible):
+                                try:
+                                    vpc_operations.list_vpc()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+        
+
+        else:
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_actions/bucket_actions.py` & `e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_actions/bucket_actions.py`

 * *Files 18% similar despite different names*

```diff
@@ -16,15 +16,15 @@
             self.Auth_Token=get_user_cred(kwargs['alias'])[0]
             self.possible=True
         else:
             self.possible=False
 
 
     def enable_versioning(self):
-        bucket_name=Py_version_manager.py_input("input name of the bucket : ")
+        bucket_name=Checks.take_input(self.kwargs["inputs"], "bucket_name")
         while(Checks.bucket_name_validity(bucket_name)):
                 bucket_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
         my_payload= json.dumps({
                         "bucket_name": bucket_name,
                         "new_versioning_state": "Enabled"
                 }) 
         
@@ -35,15 +35,15 @@
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         Checks.status_result(status)
         Checks.show_json(status)
 
 
     def disable_versioning(self):
-        bucket_name=Py_version_manager.py_input("input name of the bucket : ")
+        bucket_name=Checks.take_input(self.kwargs["inputs"], "bucket_name")
         while(Checks.bucket_name_validity(bucket_name)):
                 bucket_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
         my_payload= json.dumps({
                         "bucket_name": bucket_name,
                         "new_versioning_state": "Disabled"
                 }) 
         
@@ -54,15 +54,15 @@
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         Checks.status_result(status)
         Checks.show_json(status)
 
 
     def create_key(self):
-        key_name=Py_version_manager.py_input("input name of the key : ")
+        key_name=Checks.take_input(self.kwargs["inputs"], "key_name")
         while(Checks.bucket_name_validity(key_name)):
                 key_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
         my_payload= json.dumps({
                         "tag": key_name
                 }) 
         
         API_key=self.API_key
@@ -74,15 +74,15 @@
         if(Checks.status_result(status)):
               Py_version_manager.py_print("Key Created successfully")
 
         Checks.show_json(status)
     
 
     def delete_key(self):
-        access_key=Py_version_manager.py_input("input access key (Alphanumeric): ")
+        access_key=Checks.take_input(self.kwargs["inputs"], "access_key")
         my_payload= {} 
         query= dict()
         query['access_key']=access_key
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/core/users/?apikey="+API_key+"&location=Delhi"
         req="DELETE"
@@ -117,20 +117,20 @@
                       Checks.show_json(status, e)
                       return    
 
         Checks.show_json(status)
 
 
     def lock_key(self):
-        KEY_id=Py_version_manager.py_input("input id of the key : ")
-        while(not Checks.is_int(bucket_id)):
-                bucket_id=Py_version_manager.py_input("Only integer allowed ")
+        key_id=Checks.take_input(self.kwargs["inputs"], "key_id")
+        while(not Checks.is_int(key_id)):
+                key_id=Py_version_manager.py_input("Only integer allowed ")
         my_payload= json.dumps({
                 "disabled": True,
-                "id": KEY_id
+                "id": key_id
                 }) 
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/core/users/?apikey="+API_key+"&location=Delhi"
         req="PUT"
         status=Request(url, Auth_Token, my_payload, req).response.json()
@@ -138,20 +138,20 @@
         if(Checks.status_result(status)):
               Py_version_manager.py_print("Key locked")
 
         Checks.show_json(status)
 
     
     def unlock_key(self):
-        bucket_id=Py_version_manager.py_input("input id of the key : ")
-        while(not Checks.is_int(bucket_id)):
-                bucket_id=Py_version_manager.py_input("Only integer allowed ")
+        key_id=Checks.take_input(self.kwargs["inputs"], "key_id")
+        while(not Checks.is_int(key_id)):
+                key_id=Py_version_manager.py_input("Only integer allowed ")
         my_payload= json.dumps({
                 "disabled": False,
-                "id": bucket_id
+                "id": key_id
                 }) 
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/core/users/?apikey="+API_key+"&location=Delhi"
         req="PUT"
         status=Request(url, Auth_Token, my_payload, req).response.json()
@@ -159,15 +159,15 @@
         if(Checks.status_result(status)):
               Py_version_manager.py_print("Key unlocked")
 
         Checks.show_json(status)
     
 
     def add_permission(self):
-        bucket_name=Py_version_manager.py_input("input name of your new bucket : ")
+        bucket_name=Checks.take_input(self.kwargs["inputs"], "bucket_name")
         while(Checks.bucket_name_validity(bucket_name)):
                 bucket_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
         my_payload= json.dumps({
             "role_name": "Bucket Admin",
             "users": [
             {
                 "access_key": Py_version_manager.py_input("input access key (Alphanumeric): "),
@@ -188,26 +188,27 @@
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/bucket_perms/?apikey="+API_key+"&location=Delhi"
         req="PUT"
         status=Request(url, Auth_Token, my_payload, req, query=query).response.json()
 
         # if(Checks.status_result(status)):
         #       Py_version_manager.py_print("Key deleted successfully")
-
+        Checks.status_result(status)
         Checks.show_json(status)
 
 
     def remove_permission(self):
-        bucket_name=Py_version_manager.py_input("input access key (Alphanumeric): ")
+        access_key=Checks.take_input(self.kwargs["inputs"], "access_key")
         my_payload= {} 
         query= dict()
-        query['access_key']=bucket_name
+        query['access_key']=access_key
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/core/users/?apikey="+API_key+"&location=Delhi"
         req="DELETE"
         status=Request(url, Auth_Token, my_payload, req, query=query).response.json()
 
         if(Checks.status_result(status)):
               Py_version_manager.py_print("Key deleted successfully")
 
+        Checks.status_result(status)
         Checks.show_json(status)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_crud/bucket_storage.py` & `e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_crud/bucket_storage.py`

 * *Files 7% similar despite different names*

```diff
@@ -17,15 +17,15 @@
         else:
             self.possible=False
         
 
     def create_bucket(self):
         Py_version_manager.py_print("Creating")
         my_payload= {}  
-        bucket_name=Py_version_manager.py_input("input name of your new bucket : ")
+        bucket_name=Checks.take_input(self.kwargs["inputs"], "bucket_name")
         while(Checks.bucket_name_validity(bucket_name)):
                 bucket_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
 
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/buckets/"+ bucket_name +"/?apikey="+API_key+"&location=Delhi"
         req="POST"
@@ -34,37 +34,38 @@
         if Checks.status_result(status, req):
             try:
                 x = PrettyTable()
                 x.field_names = ["ID", "Name", "Created at"]
                 x.add_row([status['data']['id'], status['data']['name'], status['data']['created_at']])
                 Py_version_manager.py_print(x)
             except Exception as e:
-                      Checks.show_json(status, e)
-                      return
+                    Py_version_manager.py_print("Errors : ", e)
                   
-        Checks.show_json(status)    
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)    
 
 
     def delete_bucket(self):
         my_payload={}
-        bucket_name=Py_version_manager.py_input("input name of the bucket you want to delete : ")
+        bucket_name=Checks.take_input(self.kwargs["inputs"], "bucket_name")
         while(Checks.bucket_name_validity(bucket_name)):
                 bucket_name=Py_version_manager.py_input("Only following chars are supported: lowercase letters (a-z) or numbers(0-9)  Re-enter : ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/storage/buckets/"+ bucket_name +"/?apikey="+API_key+"&location=Delhi"
         req="DELETE"
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         if Checks.status_result(status,req):
                         Py_version_manager.py_print("Bucket Successfully deleted")
                         Py_version_manager.py_print("use following command -> e2e_cli <alias> bucket list to check if bucket has been deleted")
         
-        Checks.show_json(status)
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
 
 
     def list_bucket(self):
         my_payload={}
         API_key= self.API_key  
         Auth_Token= self.Auth_Token 
         url =  BASE_URL+"myaccount/api/v1/storage/buckets/?apikey="+ API_key+"&location=Delhi"
@@ -79,13 +80,13 @@
                     x = PrettyTable()
                     x.field_names = ["index", "ID", "Name", "Created at", "bucket size"]
                     for element in list:
                         x.add_row([i, element['id'], element['name'], element['created_at'], element['bucket_size']])
                         i = i+1
                     Py_version_manager.py_print(x)
                 except Exception as e:
-                      Checks.show_json(status, e)
-                      return
+                    Py_version_manager.py_print("Errors : ", e)
 
-        Checks.show_json(status)
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/bucket_store/bucket_routing.py` & `e2e_cli-0.9.9/e2e_cli/bucket_store/bucket_routing.py`

 * *Files 19% similar despite different names*

```diff
@@ -5,102 +5,95 @@
 from e2e_cli.bucket_store.bucket_actions.bucket_actions import BucketActions
 
 class BucketRouting:
     def __init__(self, arguments):
         self.arguments = arguments
         
         
-    def route(self):
-        if (self.arguments.bucket_commands is None) and (self.arguments.action is None):
-            subprocess.call(['e2e_cli', 'alias', 'bucket', '-h'])
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.bucket_commands is None) and (self.arguments.args.action is None):
+            subprocess.call(['e2e_cli', 'bucket', '-h'])
 
-        elif (self.arguments.bucket_commands is not None) and (self.arguments.action is not None):
+
+        elif (self.arguments.args.bucket_commands is not None) and (self.arguments.args.action is not None):
               Py_version_manager.py_print("Only one action at a time !!")
 
-        elif self.arguments.bucket_commands == 'create':
-            bucket_operations = bucketCrud(alias=self.arguments.alias )
-            if(bucket_operations.possible):
-                        try:
-                            bucket_operations.create_bucket()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
 
-        elif self.arguments.bucket_commands == 'delete':
-            bucket_operations = bucketCrud(alias=self.arguments.alias)
+        elif(self.arguments.args.bucket_commands is not None):
+            bucket_operations = bucketCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
             if(bucket_operations.possible):
-                        try:
-                            bucket_operations.delete_bucket()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-        elif self.arguments.bucket_commands == 'list':
-            bucket_operations = bucketCrud(alias=self.arguments.alias)
-            if(bucket_operations.possible):
-                        try:
-                            bucket_operations.list_bucket()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+                
+                if self.arguments.args.bucket_commands == 'create':
+                                try:
+                                    bucket_operations.create_bucket()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+
+                elif self.arguments.args.bucket_commands == 'delete':
+                                try:
+                                    bucket_operations.delete_bucket()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+                                
+                elif self.arguments.args.bucket_commands == 'list':
+                                try:
+                                    bucket_operations.list_bucket()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+
 
-        elif self.arguments.action == 'enable_versioning':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
+        elif(self.arguments.args.action is not None):
+            Bucket_operations=BucketActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs)     
             if(Bucket_operations.possible):
+
+                if self.arguments.args.action == 'enable_versioning':
                         try: 
                            Bucket_operations.enable_versioning()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
                         
-        elif self.arguments.action == 'disable_versioning':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'disable_versioning':
                         try: 
                            Bucket_operations.disable_versioning()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
                         
-
-        elif self.arguments.action == 'create_key':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'create_key':
                         try: 
                            Bucket_operations.create_key()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
 
-        elif self.arguments.action == 'delete_key':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'delete_key':
                         try: 
                            Bucket_operations.delete_key()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
         
-        elif self.arguments.action == 'list_key':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'list_key':
                         try: 
                            Bucket_operations.list_key()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
                             
-        elif self.arguments.action == 'lock_key':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'lock_key':
                         try: 
                            Bucket_operations.lock_key()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
         
-        elif self.arguments.action == 'unlock_key':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'unlock_key':
                         try: 
                            Bucket_operations.unlock_key()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
 
-        elif self.arguments.action == 'add_permission':
-            Bucket_operations=BucketActions(alias=self.arguments.alias)     
-            if(Bucket_operations.possible):
+                elif self.arguments.args.action == 'add_permission':
                         try: 
                            Bucket_operations.add_permission()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
+        
+
+        else:
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/cdn/cdn_actions/cdn_action.py` & `e2e_cli-0.9.9/e2e_cli/volumes/volumes_crud/volumes.py`

 * *Files 24% similar despite different names*

```diff
@@ -4,84 +4,94 @@
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core.request_service import Request
 from e2e_cli.core.alias_service import get_user_cred
 from e2e_cli.core.helper_service import Checks
 from e2e_cli.core.constants import BASE_URL
 
 
-class cdnActions:
+class volumes_Crud:
     def __init__(self, **kwargs):
         self.kwargs = kwargs
         if(get_user_cred(kwargs['alias'])):
             self.API_key=get_user_cred(kwargs['alias'])[1]
             self.Auth_Token=get_user_cred(kwargs['alias'])[0]
             self.possible=True
         else:
             self.possible=False
+        
 
-
-    def cdn_monitoring(self):
-        my_payload= {}
-        query=dict()
-        query['start_date']=Py_version_manager.py_input("input start date ")
-        query['end_date']=Py_version_manager.py_input("input start date ")
-        query['distribution_id']=Py_version_manager.py_input("input domain id of the cdn : ")
-        query['granularity']=Py_version_manager.py_input("daily/monthly ")
-
+    def create_volumes(self):
+        Py_version_manager.py_print("Creating")
+        iops_list=dict({
+                "250" : "5000", "500" : "10000", "1000" : "20000",  "2000" : "40000",  "4000" : "80000", "8000" : "120000", "16000" : "120000"
+        })
+        Py_version_manager.py_print("Enter size, multiple of 250GB only")
+        size=Checks.take_input(self.kwargs["inputs"], "size")
+        my_payload= json.dumps({
+            "name": Checks.take_input(self.kwargs["inputs"], "name"),
+            "size": size,
+            "iops": iops_list[size]
+        })
         API_key=self.API_key
         Auth_Token=self.Auth_Token
-        url =  BASE_URL+"myaccount/api/v1/cdn/monitoring-data/?&apikey="+API_key+"&location=Delhi"
-        req="GET"
-        status=Request(url, Auth_Token, my_payload, req, query=query).response.json()
-
-        Checks.status_result(status)
-        Checks.show_json(status)
-
-    
-    def enable_cdn(self):
-        my_payload = json.dumps({
-            "domain_id": Py_version_manager.py_input("input domain id of the cdn : "),
-            "is_enabled": True
-            }) 
+        url =  BASE_URL+"myaccount/api/v1/block_storage/?apikey="+API_key+"&location=Delhi"
+        req="POST"
+        status=Request(url, Auth_Token, my_payload, req).response.json()
+               
+        if Checks.status_result(status, req):
+            try:
+                x = PrettyTable()
+                x.field_names = ["block_storage_id", "name"]
+                x.add_row([status['data']['block_storage_id'], status['data']['image_name']])
+                Py_version_manager.py_print(x)
+            except Exception as e:
+                      Checks.show_json(status, e)
+                      return
+                  
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)     
+
+
+    def delete_volumes(self):
+        my_payload={}
+        blockstorage_id=Checks.take_input(self.kwargs["inputs"], "blockstorage_id")
         API_key=self.API_key
         Auth_Token=self.Auth_Token
-        url =  BASE_URL+"myaccount/api/v1/cdn/distributions/?apikey="+API_key
-        req="PUT"
+        url =  BASE_URL+"myaccount/api/v1/block_storage/"+blockstorage_id+"/?apikey="+API_key+"&location=Delhi"
+        req="DELETE"
         status=Request(url, Auth_Token, my_payload, req).response.json()
+
+        if Checks.status_result(status,req):
+                        Py_version_manager.py_print("volume Successfully deleted")
+                        Py_version_manager.py_print("use following command -> e2e_cli <alias> volumes list to check if volumes has been deleted")
         
-        Checks.status_result(status)
-        Checks.show_json(status)                
+        Checks.show_json(status)
 
 
-    def disable_cdn(self):
-        my_payload = json.dumps({
-            "domain_id": Py_version_manager.py_input("input domain id of the cdn : "),
-            "is_enabled": True
-            })         
-        API_key=self.API_key
-        Auth_Token=self.Auth_Token
-        url =  BASE_URL+"myaccount/api/v1/cdn/distributions/?apikey="+API_key
-        req="PUT"
+    def list_volumes(self):
+        my_payload={}
+        API_key= self.API_key  
+        Auth_Token= self.Auth_Token 
+        url =  BASE_URL+"myaccount/api/v1/block_storage/?apikey="+ API_key+"&location=Delhi"
+        req="GET"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        Checks.status_result(status)
-        Checks.show_json(status)                
+        if Checks.status_result(status, req):
+                Py_version_manager.py_print("Your volumess : ")
+                try:
+                    list=status['data']
+                    i=1
+                    x = PrettyTable()
+                    x.field_names = ["index", "name", "block_id", "status"]
+                    for element in list:
+                        x.add_row([i, element['name'], element['block_id'], element["status"]])
+                        i = i+1
+                    Py_version_manager.py_print(x)
+                except Exception as e:
+                    Py_version_manager.py_print("Errors : ", e)
+
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status) 
+    
+
 
-               
-    def cdn_bandwidth_usage(self):
-        my_payload= json.dumps({
-        "domain": "all",
-        'start_date' : Py_version_manager.py_input("input start date "),
-        'end_date' : Py_version_manager.py_input("input start date "),
-        'granularity' : Py_version_manager.py_input("daily/monthly ")
-            })
-        API_key=self.API_key
-        Auth_Token=self.Auth_Token
-        url =  BASE_URL+"myaccount/api/v1/cdn/domain-usage/?apikey="+API_key+"&location=Delhi"
-        req="POST"
-        status=Request(url, Auth_Token, my_payload, req, query=query).response.json()
 
-        Checks.status_result(status)
-        Checks.show_json(status)
-           
-        
-
```

### Comparing `e2e_cli-0.9.8/e2e_cli/cdn/cdn_crud/cdn.py` & `e2e_cli-0.9.9/e2e_cli/cdn/cdn_crud/cdn.py`

 * *Files 4% similar despite different names*

```diff
@@ -43,16 +43,15 @@
                   
         # Checks.show_json(status)    
 
 
     def delete_cdn(self):
         my_payload={}
         query=dict()
-        query['domain_id']=Py_version_manager.py_input("input domain id of the cdn you want to delete : ")
-        
+        query['domain_id']=Checks.take_input(self.kwargs["inputs"], "domain_id")
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/cdn/distributions/?apikey="+API_key
         req="DELETE"
         status=Request(url, Auth_Token, my_payload, req, query=query).response.json()
 
         if Checks.status_result(status,req):
@@ -78,13 +77,13 @@
                     x = PrettyTable()
                     x.field_names = ["index", "ID", "user_domain_name", "Created at", "domain_id"]
                     for element in list:
                         x.add_row([i, element['id'], element['user_domain_name'], element['created_at'], element['domain_id']])
                         i = i+1
                     Py_version_manager.py_print(x)
                 except Exception as e:
-                      Checks.show_json(status, e)
-                      return
-
-        Checks.show_json(status)
+                    Py_version_manager.py_print("Errors : ", e)
+                    
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/cdn/cdn_routing.py` & `e2e_cli-0.9.9/e2e_cli/image/image_routing.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,73 +1,59 @@
 import subprocess
 
 from e2e_cli.core.py_manager import Py_version_manager
-from e2e_cli.cdn.cdn_crud.cdn import cdn_Crud
-from e2e_cli.cdn.cdn_actions.cdn_action import cdnActions
+from e2e_cli.image.image_crud.image import ImageCrud
+from e2e_cli.image.image_listing.image_list import ImageListing
 
-class cdn_Routing:
+class ImageRouting:
     def __init__(self, arguments):
         self.arguments = arguments
         
-        
-    def route(self):
-        if (self.arguments.action is None) and (self.arguments.cdn_commands is None):
-            subprocess.call(['e2e_cli', 'alias', 'cdn', '-h'])
-
-        elif (self.arguments.cdn_commands is not None) and (self.arguments.action is not None):
-              Py_version_manager.py_print("Only one action at a time !!")
-
-        elif self.arguments.cdn_commands == 'create':
-            cdn_operations = cdn_Crud(alias=self.arguments.alias )
-            if(cdn_operations.possible):
-                        try:
-                            cdn_operations.create_cdn()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
 
-        elif self.arguments.cdn_commands == 'delete':
-            cdn_operations = cdn_Crud(alias=self.arguments.alias)
-            if(cdn_operations.possible):
-                        try:
-                            cdn_operations.delete_cdn()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-        elif self.arguments.cdn_commands == 'list':
-            cdn_operations = cdn_Crud(alias=self.arguments.alias)
-            if(cdn_operations.possible):
-                        try:
-                            cdn_operations.list_cdn()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.image_commands is None) and (self.arguments.args.list_by is None):
+            subprocess.call(['e2e_cli', 'image', '-h'])
 
-        elif self.arguments.action == "enable_cdn":
-            cdn_operations = cdnActions(alias=self.arguments.alias)
-            if(cdn_operations.possible):
+
+        elif (self.arguments.args.image_commands is not None) and (self.arguments.args.list_by is not None):
+            Py_version_manager.py_print("Only one action at a time !!")
+
+
+        elif(self.arguments.args.image_commands is not None):
+            image_operations = ImageCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+            if(image_operations.possible):
+
+                if self.arguments.args.image_commands == 'create' or self.arguments.args.image_commands=="save":
                         try:
-                            cdn_operations.enable_cdn()
+                           image_operations.create_image()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-
-        elif self.arguments.action == "disable_cdn":
-            cdn_operations = cdnActions(alias=self.arguments.alias)
-            if(cdn_operations.possible):
+                            Py_version_manager.py_print(" ")  
+                                    
+                elif self.arguments.args.image_commands == 'delete':
                         try:
-                            cdn_operations.disable_cdn()
+                           image_operations.delete_image()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == "cdn_monitoring":
-            cdn_operations = cdnActions(alias=self.arguments.alias)
-            if(cdn_operations.possible):
+                                
+                elif self.arguments.args.image_commands == 'rename':
                         try:
-                            cdn_operations.cdn_monitoring()
+                           image_operations.rename_image()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-
-        elif self.arguments.action == "cdn_bandwidth_usage":
-            cdn_operations = cdnActions(alias=self.arguments.alias)
-            if(cdn_operations.possible):
-                        try:
-                            cdn_operations.cdn_bandwidth_usage()
+                                                        
+                elif self.arguments.args.image_commands == 'list':
+                        try: 
+                           image_operations.list_image()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+                            Py_version_manager.py_print(" ")
+                        
+        # elif self.arguments.args.list_by == 'image_type':
+        #     image_operations=ImageListing(alias=self.arguments.args.alias)     
+        #     if(image_operations.possible):
+        #                 try: 
+        #                    image_operations.all()
+        #                 except KeyboardInterrupt:
+        #                     Py_version_manager.py_print(" ")
+
+        else:
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/commands_routing.py` & `e2e_cli-0.9.9/e2e_cli/commands_routing.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-
+import subprocess
 
 from e2e_cli.core.error_logs_service import action_on_exception
 from e2e_cli.core.helper_service import Checks
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core import help_messages
 
 from e2e_cli.config.config_routing import ConfigRouting
@@ -17,104 +17,119 @@
 from e2e_cli.volumes.volumes_routing import volumes_Routing
 from e2e_cli.man_display import man_page
 
 class CommandsRouting:
     def __init__(self, arguments):
         self.arguments = arguments
 
-    def route(self):
-        if self.arguments.alias is None:
-                help_messages.e2e_help()
+    def route(self, Parsing_Errors):
 
+        if(self.arguments.args.version):
+              help_messages.e2e_version_info()
 
-        elif self.arguments.alias == "help" or self.arguments.alias == "doc":
-                man_page()
+
+        elif(self.arguments.args.info):
+              help_messages.e2e_pakage_info()
 
 
-        elif (self.arguments.alias == "alias") :
+        elif self.arguments.args.command is None:
+                subprocess.call(['e2e_cli', "-h"])
+
+
+        elif self.arguments.args.command == "help" or self.arguments.args.command == "doc":
+                man_page()
 
-            if(self.arguments.command not in ["add", "view","add_file","delete"]):
-                help_messages.e2e_alias_help()  
 
-            elif self.arguments.command in ["add", "view", "add_file", "delete"]:
+        elif (self.arguments.args.command == "alias") :
+
+            if self.arguments.args.alias_commands in ["add", "view", "add_file", "delete", "set"]:
                 try:
-                    ConfigRouting(self.arguments).route()
+                    ConfigRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                        Checks.manage_exception(e)
-                                # action_on_exception(e, self.arguments.alias, traceback.print_exc())
+                    if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                                # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())
+            else:
 
+                Py_version_manager.py_print(*Parsing_Errors, sep="\n")
+                subprocess.call(['e2e_cli', "alias","-h"])
     
-        elif (self.arguments.alias[0]=="@"):
-
-            if (self.arguments.command is None):
-                Py_version_manager.py_print("issue in command/Wrong command given!!")
-                help_messages.e2e_service_help()
-                # subprocess.call(['e2e_cli', 'alias','-h'])
+    
+        else:
+            if(self.arguments.args.alias=="default"):
+                Py_version_manager.py_print("Using default alias")
 
-            elif self.arguments.command == "node":
+            if self.arguments.args.command == "node":
                 try:
-                    NodeRouting(self.arguments).route()
+                    NodeRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
+                    if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
 
-            elif self.arguments.command == "lb":
+            elif self.arguments.args.command == "lb":
                 try: 
-                    LBRouting(self.arguments).route()
+                    LBRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                        Checks.manage_exception(e)
-                                # action_on_exception(e, self.arguments.alias, traceback.print_exc()) 
+                        if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                                # action_on_exception(e, self.arguments.args.alias, traceback.print_exc()) 
     
-            elif self.arguments.command == "bucket":
+            elif self.arguments.args.command == "bucket":
                 try:
-                    BucketRouting(self.arguments).route()
+                    BucketRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                        Checks.manage_exception(e)
-                                # action_on_exception(e, self.arguments.alias, traceback.print_exc())
+                        if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                                # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())
             
-            elif self.arguments.command == "dbaas":
+            elif self.arguments.args.command == "dbaas":
                 try:
-                    DBaaSRouting(self.arguments).route()
+                    DBaaSRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                        Checks.manage_exception(e)
-                                # action_on_exception(e, self.arguments.alias, traceback.print_exc())
+                        if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                                # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())
 
-            elif self.arguments.command == "image":
+            elif self.arguments.args.command == "image":
                 try:
-                    ImageRouting(self.arguments).route()
+                    ImageRouting(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
-                            # action_on_exception(e, self.arguments.alias, traceback.print_exc())   
+                            if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                            # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())   
 
-            elif self.arguments.command == "autoscaling":
+            elif self.arguments.args.command == "autoscaling":
                 try:
-                    autoscaling_Routing(self.arguments).route()
+                    autoscaling_Routing(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
-                            # action_on_exception(e, self.arguments.alias, traceback.print_exc())   
+                            if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                            # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())   
         
-            elif self.arguments.command == "cdn":
+            elif self.arguments.args.command == "cdn":
                 try:
-                    cdn_Routing(self.arguments).route()
+                    cdn_Routing(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
-                            # action_on_exception(e, self.arguments.alias, traceback.print_exc()) 
+                            if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                            # action_on_exception(e, self.arguments.args.alias, traceback.print_exc()) 
 
-            elif self.arguments.command == "vpc":
+            elif self.arguments.args.command == "vpc":
                 try:
-                    vpc_Routing(self.arguments).route()
+                    vpc_Routing(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
-                            # action_on_exception(e, self.arguments.alias, traceback.print_exc())  
+                            if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                            # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())  
 
-            elif self.arguments.command == "volumes":
+            elif self.arguments.args.command == "volumes":
                 try:
-                    volumes_Routing(self.arguments).route()
+                    volumes_Routing(self.arguments).route(Parsing_Errors)
                 except Exception as e:
-                            Checks.manage_exception(e)
-                            # action_on_exception(e, self.arguments.alias, traceback.print_exc())  
-    
-                            
-        else :
-              Py_version_manager.py_print("Command not found")
-              Py_version_manager.py_print("Did you mean, e2e_cli help/doc --> for viewing man doc ??")
-              Py_version_manager.py_print("Did you mean, e2e_cli alias [command] --> for adding alias ??")
-              Py_version_manager.py_print("Did you mean, e2e_cli @<alias> [command] [sub-command] --> for accessing services ??")
+                            if("debug" in self.arguments.inputs):
+                                Checks.manage_exception(e)
+                            # action_on_exception(e, self.arguments.args.alias, traceback.print_exc())  
+
+            else:
+                Py_version_manager.py_print("Command not found!! for more help type e2e_cli help")
+                Py_version_manager.py_print(*Parsing_Errors, sep="\n")
+
```

### Comparing `e2e_cli-0.9.8/e2e_cli/config/config.py` & `e2e_cli-0.9.9/e2e_cli/config/config.py`

 * *Files 6% similar despite different names*

```diff
@@ -49,14 +49,15 @@
 
     def reserve_keyword_check(self):
         if(str(self.kwargs["alias"]).lower() in RESERVES):
                 Py_version_manager.py_print("The used alias name is a reserve keyword for cli tool")            
         else:
                 self.add_json_to_file()
 
+
     def add_json_to_file(self):
         api_access_credentials_object = {"api_key": self.kwargs["api_key"],
                                          "api_auth_token": self.kwargs["api_auth_token"]}
         if(is_valid(api_access_credentials_object["api_key"], api_access_credentials_object["api_auth_token"])):
             with open(self.file, 'r+') as file_reference:
                 read_string = file_reference.read()
                 if read_string == "":
@@ -64,21 +65,22 @@
                                                         api_access_credentials_object}))
                 else:
                     api_access_credentials = json.loads(read_string)
                     api_access_credentials.update({self.kwargs["alias"]:
                                                     api_access_credentials_object})
                     file_reference.seek(0)
                     file_reference.write(json.dumps(api_access_credentials))
-            Py_version_manager.py_print()
+            
             Py_version_manager.py_print("Alias/user_name/Token name successfully added")
         else:
-            Py_version_manager.py_print()
+            
             Py_version_manager.py_print("Invalid credentials given please enter correct Api key and Authorisation")
             return
 
+
     def add_to_config(self):
         file_exist_check_variable = self.check_if_file_exist()
         if file_exist_check_variable == -1:
             os.mkdir(self.folder)
             with open(self.file, 'w'):
                 pass
             self.reserve_keyword_check()
@@ -88,36 +90,38 @@
             self.reserve_keyword_check()
         elif file_exist_check_variable == 1:
             if (get_user_cred(self.kwargs['alias'],2)):
                 Py_version_manager.py_print("The given alias/username already exist!! Please use another name or delete the previous one")
             else:
                 self.reserve_keyword_check()
 
-    def delete_from_config(self):
+
+    def delete_from_config(self, x=0):
         file_exist_check_variable = self.check_if_file_exist()
         if file_exist_check_variable == -1 | file_exist_check_variable == 0:
             Py_version_manager.py_print("You need to add your api access credentials using the add functionality ")
-            Py_version_manager.py_print("To know more please write e2e_cli config add -h on your terminal")
+            Py_version_manager.py_print("To know more please write 'e2e_cli alias -h' on your terminal")
 
         elif file_exist_check_variable == 1:
             with open(self.file, 'r+') as file_reference:
                 file_contents_object = json.loads(file_reference.read())
                 delete_output = file_contents_object.pop(self.kwargs["alias"], 'No key found')
                 if delete_output == "No key found":
-                    Py_version_manager.py_print()
+                    
                     Py_version_manager.py_print("No such alias found. Please re-check and enter again")
                 else:
                     file_reference.seek(0)
                     file_reference.write(json.dumps(file_contents_object))
                     file_reference.truncate()
-                    Py_version_manager.py_print()
-                    Py_version_manager.py_print("Alias/name Successfully deteted")
+                    
+                    if(x!=1):
+                        Py_version_manager.py_print("Alias/name Successfully deleted")
+
 
     def adding_config_file(self, path):
-        
         # for drag and drop
         if(path[0]=="'" and path[-1]=="'"):
                     path=path.lstrip(path[0])
                     path=path.rstrip(path[-1])
 
         if((path.endswith("/config.json") or path=="config.json") and os.path.isfile(path)):
     
@@ -125,8 +129,25 @@
                 os.mkdir(self.folder)
             
             if platform.system() == "Windows":
                 os.system('copy '+ path+ ' '+ self.folder)
             elif platform.system() == "Linux" or platform.system() == "Darwin":    
                 os.system('cp '+ path+ ' '+ self.folder)
 
-            Py_version_manager.py_print("Token file successfuly added")
+            Py_version_manager.py_print("Token file successfuly added")
+
+
+    def set_default(self):
+        api_access_credentials_object = {"api_key": self.kwargs["api_key"],
+                                         "api_auth_token": self.kwargs["api_auth_token"]}
+        with open(self.file, 'r+') as file_reference:
+                read_string = file_reference.read()
+                if read_string == "":
+                    file_reference.write(json.dumps({"default":
+                                                        api_access_credentials_object}))
+                else:
+                    api_access_credentials = json.loads(read_string)
+                    api_access_credentials.update({"default":
+                                                    api_access_credentials_object})
+                    file_reference.seek(0)
+                    file_reference.truncate(0)                    
+                    file_reference.write(json.dumps(api_access_credentials))
```

### Comparing `e2e_cli-0.9.8/e2e_cli/config/config_routing.py` & `e2e_cli-0.9.9/e2e_cli/config/config_routing.py`

 * *Files 18% similar despite different names*

```diff
@@ -4,44 +4,63 @@
 from e2e_cli.config.config import AuthConfig
 from e2e_cli.core.alias_service import get_user_cred
 
 class ConfigRouting:
     def __init__(self, arguments):
         self.arguments = arguments
 
-    def route(self):
-        if self.arguments.command == 'add':
+    def route(self, Parsing_errors):
+
+        if self.arguments.args.alias_commands == 'add':
             try:
                 api_key = Py_version_manager.py_input("Enter your api key: ")
                 auth_token = Py_version_manager.py_input("Enter your auth token: ")
                 auth_config_object = AuthConfig(alias=Py_version_manager.py_input("Input name of alias you want to add : "),
                                                     api_key=api_key,
                                                     api_auth_token=auth_token)
                 auth_config_object.add_to_config()
             except KeyboardInterrupt:
                 Py_version_manager.py_print(" ")
                 pass
 
 
-        elif self.arguments.command == 'add_file':
+        elif self.arguments.args.alias_commands == 'add_file':
                 path=Py_version_manager.py_input("input the file path : ")
                 auth_config_object = AuthConfig()
                 auth_config_object.adding_config_file(path)
                 return
             
 
-        elif self.arguments.command == 'delete':            
+        elif self.arguments.args.alias_commands == 'delete':            
             confirmation =Py_version_manager.py_input("are you sure you want to delete press y for yes, else any other key : ")
             if(confirmation.lower()=='y'):
                 auth_config_object = AuthConfig(alias=Py_version_manager.py_input("Input name of alias you want to add : "))
                 try:
                     auth_config_object.delete_from_config()
                 except:
                     pass  
 
 
-        elif self.arguments.command == 'view':
-                
+        elif self.arguments.args.alias_commands == 'view':
                 for item in list(get_user_cred("all", 1)):
                     Py_version_manager.py_print(item)
             
-
+        
+        elif self.arguments.args.alias_commands == 'set':
+                default_name=Py_version_manager.py_input("Enter name of the alias you want to set as default : ")   
+                if(Py_version_manager.py_input("are you sure you want to proceed : ").lower()=="y"):
+                    try:
+                        auth_config_object = AuthConfig(alias="default",
+                                                        api_key=default_name,
+                                                        api_auth_token=default_name)
+                        if(get_user_cred("default")):
+                                AuthConfig(alias="default").delete_from_config(x=1)
+                        auth_config_object.set_default()
+                        Py_version_manager.py_print("Default alias set to ", default_name)
+                    except KeyboardInterrupt:
+                        Py_version_manager.py_print(" ")
+                        pass
+
+
+        else:
+            Py_version_manager.py_print("Command not found!!")
+            Py_version_manager.py_print(*Parsing_errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/core/alias_service.py` & `e2e_cli-0.9.9/e2e_cli/core/alias_service.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,61 +2,72 @@
 import os
 import platform
 
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core.constants import RESERVES
 
 
-def option_check(alias):
-    if(alias.startswith("@")):
-            return alias.lstrip(alias[0])
-    else:
-          return alias
+# def option_check(alias):
+#     if(alias=="default"):
+#             return get_user_cred(alias)[0]
+#     else:
+#           return alias
 
 
 class AliasServices:
     def __init__(self, alias):
-        self.alias = option_check(alias)
+        self.alias = alias
 
     def get_api_credentials(self):
         file= os.path.expanduser("~") + '/.E2E_CLI/config.json'
         file_reference = open(file, "r")
         config_file_object = json.loads(file_reference.read())
         if self.alias in config_file_object:
-            return {"api_credentials": config_file_object[self.alias],
-                    "message": "Valid alias"}
+            if(self.alias=="default"):
+                default_alias=config_file_object["default"]['api_key']
+                return {"api_credentials": config_file_object[default_alias],
+                        "message": "Valid alias"}
+            else:
+                return {"api_credentials": config_file_object[self.alias],
+                        "message": "Valid alias"}
         else:
             return {"message": "Invalid alias provided"}
 
 def system_file():
     if platform.system() == "Windows":  
                 return os.path.expanduser("~") + '\.E2E_CLI\config.json'
     elif platform.system() == "Linux" or platform.system() == "Darwin":  
                 return os.path.expanduser("~") + '/.E2E_CLI/config.json'
 
 
 def get_user_cred(name, x=0):
     
-    name=option_check(name)
     file= system_file()
 
     # try :
     # Opening JSON file
     f = open(file)
     
     # returns JSON object as a dictionary
     data = json.load(f)
 
     if(name=="all" and x==1):
+                try:
+                    Py_version_manager.py_print("default --> ", data["default"])
+                except:
+                    Py_version_manager.py_print("default --> ", "Not set")
                 return data.keys()
     
     # Closing file
     f.close()
 
 
     if(name in data):
-        return[ data[name]['api_auth_token'], data[name]['api_key'] ]
+        if(name=="default"):
+            return get_user_cred(data["default"]['api_key'])
+        else:  
+            return[ data[name]['api_auth_token'], data[name]['api_key'] ]
     elif x==2:
         return None
     else:
-        Py_version_manager.py_print("the given alias/credential doesn't exist")
+        Py_version_manager.py_print("Warning : The given alias/credential doesn't exist")
         return None
```

### Comparing `e2e_cli-0.9.8/e2e_cli/core/error_logs_service.py` & `e2e_cli-0.9.9/e2e_cli/core/error_logs_service.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/core/helper_service.py` & `e2e_cli-0.9.9/e2e_cli/core/helper_service.py`

 * *Files 4% similar despite different names*

```diff
@@ -69,19 +69,24 @@
         # data_result=status_data_check(status, req)
 
         return error_result
         
 
     @classmethod
     def manage_exception(self, e):
-                Py_version_manager.py_print("Oops!! An error occurred for more info, type : debug")
-                if(Py_version_manager.py_input("debug/exit ?? ").lower()=="debug"):
-                        Py_version_manager.py_print(e)    
-                        traceback.print_exc()                 
+                    Py_version_manager.py_print(e)    
+                    traceback.print_exc()                 
     
     @classmethod
     def show_json(self, status, e=None):
         if(e!=None):
                 Py_version_manager.py_print("Errors while reading json ",e)
+        Py_version_manager.py_print(json.dumps(status, sort_keys=True, indent=4))
 
-        if(Py_version_manager.py_input("for more info type 'json' ").lower()=="json"):
-                Py_version_manager.py_print(json.dumps(status, sort_keys=True, indent=4))
+
+    @classmethod
+    def take_input(self, inputs, value):
+        if(value in inputs):
+            # print("gfhg")
+            return inputs.__dict__[value]
+        else:
+            return Py_version_manager.py_input("Please enter "+ value+ " : ")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/core/py_manager.py` & `e2e_cli-0.9.9/e2e_cli/core/py_manager.py`

 * *Files 22% similar despite different names*

```diff
@@ -13,16 +13,16 @@
     def py_input(self, msg):
         if(int(sys.version[0:1])<3):
                 return raw_input(msg)
         else:
                 return input(msg)
     
     @classmethod
-    def py_print(self, *args):
+    def py_print(self, *args, sep=" "):
         # if(int(sys.version[0:1])<3):
         #         print(*args, sep = " ")
         # else:
-                print(*args, sep = " ")
+                print(*args, sep = sep)
                 # return print(args)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/dbaas.py` & `e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/dbaas.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_crud/dbaas_services.py` & `e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_crud/dbaas_services.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/dbaas/dbaas_routing.py` & `e2e_cli-0.9.9/e2e_cli/dbaas/dbaas_routing.py`

 * *Files 26% similar despite different names*

```diff
@@ -6,150 +6,112 @@
 
 
 
 class DBaaSRouting:
     def __init__(self, arguments):
         self.arguments = arguments
 
-    def route(self):
-        if (self.arguments.dbaas_commands is None) and (self.arguments.action is None):
-            subprocess.call(['e2e_cli', "alias",'dbaas', '-h'])
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.dbaas_commands is None) and (self.arguments.args.action is None):
+            subprocess.call(['e2e_cli','dbaas', '-h'])
 
-        elif (self.arguments.dbaas_commands is not None) and (self.arguments.action is not None):
+
+        elif (self.arguments.args.dbaas_commands is not None) and (self.arguments.args.action is not None):
               Py_version_manager.py_print("Only one action at a time !!")
 
-        elif self.arguments.dbaas_commands == 'create':
-            if "alias=" in self.arguments.alias:
-                alias_name = self.arguments.alias.split("=")[1]
-            else:
-                alias_name = self.arguments.alias
-            dbaas_class_object = DBaaSClass(alias=alias_name)
-            try:
-              dbaas_class_object.create_dbaas()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
-
-        elif self.arguments.dbaas_commands == 'list' or self.arguments.dbaas_commands == 'ls':
-            if "alias=" in self.arguments.alias:
-                alias_name = self.arguments.alias.split("=")[1]
-            else:
-                alias_name = self.arguments.alias
-            dbaas_class_object = DBaaSClass(alias=alias_name)
-            try:
-                dbaas_class_object.list_dbaas()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
-
-        elif self.arguments.dbaas_commands == 'delete':
-            if "alias=" in self.arguments.alias:
-                alias_name = self.arguments.alias.split("=")[1]
-            else:
-                alias_name = self.arguments.alias
-            dbaas_class_object = DBaaSClass(alias=alias_name)
-            try:
-                dbaas_class_object.delete_dbaas_by_name()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
+
+        elif (self.arguments.args.dbaas_commands is not None):
+            dbaas_class_object = DBaaSClass(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+
+            if self.arguments.args.dbaas_commands == 'create':
+                try:
+                    dbaas_class_object.create_dbaas()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+
+            elif self.arguments.args.dbaas_commands == 'list' or self.arguments.args.dbaas_commands == 'ls':
+                try:
+                    dbaas_class_object.list_dbaas()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+
+            elif self.arguments.args.dbaas_commands == 'delete':
+                try:
+                    dbaas_class_object.delete_dbaas_by_name()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
         
-        elif self.arguments.action == 'take_snapshot':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
+
+        elif(self.arguments.args.action is not None):
+            DBaas_operations=DBaasAction(alias=self.arguments.args.alias, inputs=self.arguments.inputs)     
             if(DBaas_operations.possible):
+            
+                if self.arguments.args.action == 'take_snapshot':
                         try: 
                            DBaas_operations.take_snapshot()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'reset_password':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'reset_password':
                         try: 
                            DBaas_operations.reset_password()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'stop_db':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'stop_db':
                         try: 
                            DBaas_operations.stop_db()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'start_db':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'start_db':
                         try: 
                            DBaas_operations.start_db()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
         
-        elif self.arguments.action == 'restart_db':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'restart_db':
                         try: 
                            DBaas_operations.restart_db()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'enable_backup':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'enable_backup':
                         try: 
                            DBaas_operations.enable_backup()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'disable_backup':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'disable_backup':
                         try: 
                            DBaas_operations.disable_backup()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
         
-        elif self.arguments.action == 'add_parameter_group':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'add_parameter_group':
                         try: 
                            DBaas_operations.add_parameter_group()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'remove_parameter_group':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'remove_parameter_group':
                         try: 
                            DBaas_operations.remove_parameter_group()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'add_vpc':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'add_vpc':
                         try: 
                            DBaas_operations.add_vpc()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
             
-        elif self.arguments.action == 'remove_vpc':
-            DBaas_operations=DBaasAction(alias=self.arguments.alias)     
-            if(DBaas_operations.possible):
+                elif self.arguments.args.action == 'remove_vpc':
                         try: 
                            DBaas_operations.remove_vpc()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-            
+        
+
+        else:
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/docs/e2e_cli.1` & `e2e_cli-0.9.9/e2e_cli/docs/e2e_cli.1`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/image/image_crud/image.py` & `e2e_cli-0.9.9/e2e_cli/image/image_crud/image.py`

 * *Files 19% similar despite different names*

```diff
@@ -3,37 +3,33 @@
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core.alias_service import get_user_cred
 from e2e_cli.core.request_service import Request
 from e2e_cli.core.helper_service import Checks
 from e2e_cli.core.constants import BASE_URL
 
 
-def response_output(status, req):
-    if Checks.status_result(status, req):
-            try:
-                Checks.show_json(status["data"])
-                return
-            except Exception as e:
-                    Checks.show_json(status, e)
-                    return
+def response_output(status, req): 
+    Checks.status_result(status, req)
+    Checks.show_json(status)
+
 
 class ImageCrud:
     def __init__(self, **kwargs):
         self.kwargs = kwargs
         if(get_user_cred(kwargs['alias'])):
             self.API_key=get_user_cred(kwargs['alias'])[1]
             self.Auth_Token=get_user_cred(kwargs['alias'])[0]
             self.possible=True
         else:
             self.possible=False
     
 
     def create_image(self):
-        node_id = Py_version_manager.py_input("please enter node id ")
-        new_image_name= Py_version_manager.py_input("please enter a name for your new image ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
+        new_image_name= Checks.take_input(self.kwargs["inputs"], "new_image_name")
         my_payload= json.dumps({
                         "name": new_image_name,
                         "type": "save_images"
                 }) 
         
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
@@ -44,15 +40,15 @@
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         response_output(status, req)                
         
 
     def delete_image(self):
-        image_id = Py_version_manager.py_input("please enter image id ")
+        image_id = Checks.take_input(self.kwargs["inputs"], "image_id")
         while(not Checks.is_int(image_id)):
               image_id = Py_version_manager.py_input("please enter image id (integer only) ")
         my_payload= json.dumps({
                         "action_type": "delete_image"
                 }) 
         
         API_key=self.API_key
@@ -62,18 +58,18 @@
         if(Py_version_manager.py_input("Are you sure you want to delete : ").lower()=="y"):
             status=Request(url, Auth_Token, my_payload, req).response.json()
 
         response_output(status, req)
 
 
     def rename_image(self):
-        image_id = Py_version_manager.py_input("please enter image id ")
+        image_id = Checks.take_input(self.kwargs["inputs"], "image_id")
         while(not Checks.is_int(image_id)):
               image_id = Py_version_manager.py_input("please enter image id (integer only) ")
-        new_name= Py_version_manager.py_input("please enter a name for your new image ")
+        new_name= Checks.take_input(self.kwargs["inputs"], "new_name")
         my_payload= json.dumps({
                         "name": new_name,
                         "action_type": "rename"
                 }) 
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
```

### Comparing `e2e_cli-0.9.8/e2e_cli/image/image_listing/image_list.py` & `e2e_cli-0.9.9/e2e_cli/image/image_listing/image_list.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/image/image_routing.py` & `e2e_cli-0.9.9/e2e_cli/auto_scaling/autoscaling_routing.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,60 +1,43 @@
 import subprocess
 
 from e2e_cli.core.py_manager import Py_version_manager
-from e2e_cli.image.image_crud.image import ImageCrud
-from e2e_cli.image.image_listing.image_list import ImageListing
+from e2e_cli.auto_scaling.auto_scaling import autoscaling_Crud
 
-class ImageRouting:
+class autoscaling_Routing:
     def __init__(self, arguments):
         self.arguments = arguments
         
-
-    def route(self):
-        if (self.arguments.image_commands is None) and (self.arguments.list_by is None):
-            subprocess.call(['e2e_cli', 'alias','image', '-h'])
-
-        elif (self.arguments.image_commands is not None) and (self.arguments.list_by is not None):
-              Py_version_manager.py_print("Only one action at a time !!")
-
-        elif self.arguments.image_commands == 'create' or self.arguments.image_commands=="save":
-            image_operations = ImageCrud(alias=self.arguments.alias)
-            if(image_operations.possible):
-                        try:
-                           image_operations.create_image()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")  
-                              
-        elif self.arguments.image_commands == 'delete':
-            image_operations = ImageCrud(alias=self.arguments.alias)
-            if(image_operations.possible):
-                        try:
-                           image_operations.delete_image()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-        elif self.arguments.image_commands == 'rename':
-            image_operations = ImageCrud(alias=self.arguments.alias)
-            if(image_operations.possible):
-                        try:
-                           image_operations.rename_image()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                                                 
-        elif self.arguments.image_commands == 'list':
-            image_operations = ImageCrud(alias=self.arguments.alias)
-            if(image_operations.possible):
-                        try: 
-                           image_operations.list_image()
-                        except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-        # elif self.arguments.list_by == 'image_type':
-        #     image_operations=ImageListing(alias=self.arguments.alias)     
-        #     if(image_operations.possible):
-        #                 try: 
-        #                    image_operations.all()
-        #                 except KeyboardInterrupt:
-        #                     Py_version_manager.py_print(" ")
-
+        
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.autoscaling_commands is None):
+            subprocess.call(['e2e_cli', 'autoscaling', '-h'])
+
+        # elif (self.arguments.args.autoscaling_commands is not None) and (self.arguments.args.action is not None):
+        #       Py_version_manager.py_print("Only one action at a time !!")
+
+        elif(self.arguments.args.autoscaling_commands is not None):
+            auto_scaling_operations = autoscaling_Crud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+            if(auto_scaling_operations.possible):
+
+                if self.arguments.args.autoscaling_commands == 'create':
+                                try:
+                                    auto_scaling_operations.create_autoscaling()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+
+                elif self.arguments.args.autoscaling_commands == 'delete':
+                                try:
+                                    auto_scaling_operations.delete_autoscaling()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+                                
+                elif self.arguments.args.autoscaling_commands == 'list':
+                                try:
+                                    auto_scaling_operations.list_autoscaling()
+                                except KeyboardInterrupt:
+                                    Py_version_manager.py_print(" ")
+           
+            
         else:
-            Py_version_manager.py_print("command not found!!")
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/loadbalancer/lb.py` & `e2e_cli-0.9.9/e2e_cli/loadbalancer/lb.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/loadbalancer/lb_routing.py` & `e2e_cli-0.9.9/e2e_cli/loadbalancer/lb_routing.py`

 * *Files 25% similar despite different names*

```diff
@@ -4,58 +4,39 @@
 from e2e_cli.loadbalancer.lb import LBClass
 
 
 class LBRouting:
     def __init__(self, arguments):
         self.arguments = arguments
 
-    def route(self):
-        if self.arguments.lb_commands is None:
-            subprocess.call(['e2e_cli', "alias", 'lb', '-h'])
-
-        elif self.arguments.lb_commands == 'create':
-            lb_class_object = LBClass(alias=self.arguments.alias)
-            try:
-               lb_class_object.create_lb()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
-
-        elif self.arguments.lb_commands == 'list' or self.arguments.lb_commands == 'ls':
-            lb_class_object = LBClass(alias=self.arguments.alias)
-            try:
-               lb_class_object.list_lb()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
-
-        elif self.arguments.lb_commands == 'delete':
-            lb_class_object = LBClass(alias=self.arguments.alias)
-            try:
-               lb_class_object.delete_lb()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
-
-        elif self.arguments.lb_commands == 'edit':
-            lb_class_object = LBClass(alias=self.arguments.alias)
-            try:
-               lb_class_object.edit_lb()
-            except KeyboardInterrupt:
-                Py_version_manager.py_print(" ")
-            except Exception as e:
-                            if(str(e)=="'data'" or str(e)=="'code'"):
-                                Py_version_manager.py_print("Oops!! Your access credentials seems to have expired")
-                            else:
-                                raise e
+    def route(self, Parsing_Errors):
+        if self.arguments.args.lb_commands is None:
+            subprocess.call(['e2e_cli', 'lb', '-h'])
+
+
+        elif(self.arguments.args.lb_commands is not None):
+            lb_class_object = LBClass(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
+            
+            if self.arguments.args.lb_commands == 'create':
+                try:
+                    lb_class_object.create_lb()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+                
+            elif self.arguments.args.lb_commands == 'list' or self.arguments.args.lb_commands == 'ls':
+                try:
+                    lb_class_object.list_lb()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+                
+            elif self.arguments.args.lb_commands == 'delete':
+                try:
+                    lb_class_object.delete_lb()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+                
+            elif self.arguments.args.lb_commands == 'edit':
+                try:
+                    lb_class_object.edit_lb()
+                except KeyboardInterrupt:
+                    Py_version_manager.py_print(" ")
+
```

### Comparing `e2e_cli-0.9.8/e2e_cli/loadbalancer/lb_services.py` & `e2e_cli-0.9.9/e2e_cli/loadbalancer/lb_services.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/main.py` & `e2e_cli-0.9.9/e2e_cli/main.py`

 * *Files 20% similar despite different names*

```diff
@@ -2,199 +2,236 @@
 # import argcomplete working on auto-complete now 
 
 from e2e_cli.commands_routing import CommandsRouting
 from e2e_cli.core.error_logs_service import ErrorLogs
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core import help_messages
 
+PARSING_ERROR_MSG=[]
 
 class Main:
     def __init__(self):
         pass
 
     def FormatUsage(self, parser, action):
-        format_string = "e2e_cli" + " alias"+ " " + action + " [-h]" + " {create,delete,list,edit/update} ... "
+        if(action=="alias"):
+            format_string = "e2e_cli" + " alias" + " [-h]" + " {create,delete,list,edit/update} ... "
+        else:
+            format_string = "e2e_cli" + " --alias"+ " " + action + " [-h]" + " {create,delete,list,edit/update} ... "
         parser.usage = format_string
 
     def FormatUsageCommand(self, parser, action, command):
         format_string = "e2e_cli" + " alias=" + "<alias_name>"+ " " + action + " [-h] " + command
         parser.usage = format_string
 
-    def config(self, parser):
-        config_sub_parser = parser.add_subparsers(title="Config Commands", dest="config_commands")
-        config_add_sub_parser = config_sub_parser.add_parser("add", help="To add api key and auth token")
-        config_delete_sub_parser = config_sub_parser.add_parser("delete", help="To delete api key and auth token")
-        config_view_sub_parser = config_sub_parser.add_parser("view", help="To view all alias and credentials")
-        self.FormatUsageCommand(config_add_sub_parser, "config", "add")
-        self.FormatUsageCommand(config_delete_sub_parser, "config", "delete")
-        self.FormatUsageCommand(config_view_sub_parser, "config", "view")
+    def alias(self, parser):
+        alias_sub_parser = parser.add_subparsers(title="Alias Commands", metavar="", dest="alias_commands")
+        alias_add_sub_parser = alias_sub_parser.add_parser("add", help="To add api key and auth token")
+        alias_file_sub_parser = alias_sub_parser.add_parser("add_file", help="To add api key and auth token via file")
+        alias_delete_sub_parser = alias_sub_parser.add_parser("delete", help="To delete api key and auth token")
+        alias_view_sub_parser = alias_sub_parser.add_parser("view", help="To view all alias and credentials")
+        alias_set_default_sub_parser = alias_sub_parser.add_parser("set", help="To set default alias for system")
+        self.FormatUsageCommand(alias_add_sub_parser, "alias", "add")
+        self.FormatUsageCommand(alias_file_sub_parser, "alias", "add_file")
+        self.FormatUsageCommand(alias_delete_sub_parser, "alias", "delete")
+        self.FormatUsageCommand(alias_view_sub_parser, "alias", "view")
+        self.FormatUsageCommand(alias_set_default_sub_parser, "alias", "set")
 
     def node(self, parser):
-        node_sub_parser = parser.add_subparsers(title="node Commands", dest="node_commands")
-        node_action=parser.add_argument('-action', '--action', help="Type of action to be performed your node")
+        node_sub_parser = parser.add_subparsers(title="Node Commands", metavar="", dest="node_commands")
+        node_action=parser.add_argument('--action', help="Type of action to be performed your node")
         node_create_sub_parser = node_sub_parser.add_parser("create", help="To create a new node", formatter_class=help_messages.cli_formatter())
         node_delete_sub_parser = node_sub_parser.add_parser("delete", help="To delete a specific node", formatter_class=help_messages.cli_formatter())
         node_list_sub_parser = node_sub_parser.add_parser("list", help="To get a list of all nodes", formatter_class=help_messages.cli_formatter())
         node_get_sub_parser = node_sub_parser.add_parser("get", help="To get a list of all nodes", formatter_class=help_messages.cli_formatter())
         self.FormatUsageCommand(node_action, "node", "actions")
         self.FormatUsageCommand(node_create_sub_parser, "node", "create")
         self.FormatUsageCommand(node_delete_sub_parser, "node", "delete")
         self.FormatUsageCommand(node_list_sub_parser, "node", "list")
         self.FormatUsageCommand(node_get_sub_parser, "node", "get")
 
     def image(self, parser):
-        image_sub_parser = parser.add_subparsers(title="image Commands", dest="image_commands")
-        image_list=parser.add_argument('-list_by', '--list_by', help="attribute/property by which you want to list images")
+        image_sub_parser = parser.add_subparsers(title="Image Commands", metavar="", dest="image_commands")
+        image_list=parser.add_argument('--list_by', help="attribute/property by which you want to list images")
         image_create_sub_parser = image_sub_parser.add_parser("create", help="To create a new image")
         image_delete_sub_parser = image_sub_parser.add_parser("delete", help="To delete a specific image")
         image_list_sub_parser = image_sub_parser.add_parser("list", help="To get a list of all image")
         image_get_sub_parser = image_sub_parser.add_parser("rename", help="To rename a specific image")
         self.FormatUsageCommand(image_list, "image", "list_by")
         self.FormatUsageCommand(image_create_sub_parser, "image", "create")
         self.FormatUsageCommand(image_delete_sub_parser, "image", "delete")
         self.FormatUsageCommand(image_list_sub_parser, "image", "list")
         self.FormatUsageCommand(image_get_sub_parser, "image", "rename")
 
     def lb(self, parser):
-        node_sub_parser = parser.add_subparsers(title="LB Commands", dest="lb_commands")
+        node_sub_parser = parser.add_subparsers(title="LB Commands", metavar="", dest="lb_commands")
         node_create_sub_parser = node_sub_parser.add_parser("create", help="To create a new node", formatter_class=help_messages.cli_formatter())
         node_delete_sub_parser = node_sub_parser.add_parser("delete", help="To delete a specific node", formatter_class=help_messages.cli_formatter())
         node_list_sub_parser = node_sub_parser.add_parser("list", help="To get a list of all nodes", formatter_class=help_messages.cli_formatter())
         node_edit_sub_parser = node_sub_parser.add_parser("edit", help="To get a list of all nodes", formatter_class=help_messages.cli_formatter())
         self.FormatUsageCommand(node_create_sub_parser, "node", "create")
         self.FormatUsageCommand(node_delete_sub_parser, "node", "delete")
         self.FormatUsageCommand(node_list_sub_parser, "node", "list")
         self.FormatUsageCommand(node_edit_sub_parser, "node", "edit")
 
     def bucket(self, parser):
-        bucket_sub_parser = parser.add_subparsers(title="bucket Commands", dest="bucket_commands")
-        bucket_action=parser.add_argument('-action', '--action', help="Type of action to be performed your bucket")
+        bucket_sub_parser = parser.add_subparsers(title="Bucket Commands", metavar="", dest="bucket_commands")
+        bucket_action=parser.add_argument('--action', help="Type of action to be performed your bucket")
         bucket_create_sub_parser = bucket_sub_parser.add_parser("create", help="To create a new bucket")
         bucket_delete_sub_parser = bucket_sub_parser.add_parser("delete", help="To delete a specific bucket")
         bucket_delete_sub_parser = bucket_sub_parser.add_parser("list", help="To get a list of all buckets")
         self.FormatUsageCommand(bucket_action, "bucket", "actions")
         self.FormatUsageCommand(bucket_create_sub_parser, "bucket", "create")
         self.FormatUsageCommand(bucket_delete_sub_parser, "bucket", "delete")
         self.FormatUsageCommand(bucket_delete_sub_parser, "bucket", "list")    
 
     def autoscaling(self, parser):
-        autoscaling_sub_parser = parser.add_subparsers(title="autoscaling Commands", dest="autoscaling_commands")
+        autoscaling_sub_parser = parser.add_subparsers(title="Autoscaling Commands", metavar="", dest="autoscaling_commands")
         autoscaling_create_sub_parser = autoscaling_sub_parser.add_parser("create", help="To create a new bucket")
         autoscaling_delete_sub_parser = autoscaling_sub_parser.add_parser("delete", help="To delete a specific bucket")
         autoscaling_delete_sub_parser = autoscaling_sub_parser.add_parser("list", help="To get a list of all buckets")
         self.FormatUsageCommand(autoscaling_create_sub_parser, "autoscaling", "create")
         self.FormatUsageCommand(autoscaling_delete_sub_parser, "autoscaling", "delete")
         self.FormatUsageCommand(autoscaling_delete_sub_parser, "autoscaling", "list")
 
     def vpc(self, parser):
-        vpc_sub_parser = parser.add_subparsers(title="vpc Commands", dest="vpc_commands")
+        vpc_sub_parser = parser.add_subparsers(title="VPC Commands", metavar="", dest="vpc_commands")
         vpc_create_sub_parser = vpc_sub_parser.add_parser("create", help="To create a new bucket")
         vpc_delete_sub_parser = vpc_sub_parser.add_parser("delete", help="To delete a specific bucket")
         vpc_delete_sub_parser = vpc_sub_parser.add_parser("list", help="To get a list of all buckets")
         self.FormatUsageCommand(vpc_create_sub_parser, "vpc", "create")
         self.FormatUsageCommand(vpc_delete_sub_parser, "vpc", "delete")
         self.FormatUsageCommand(vpc_delete_sub_parser, "vpc", "list")
 
     def cdn(self, parser):
-        cdn_sub_parser = parser.add_subparsers(title="cdn Commands", dest="cdn_commands")
-        cdn_action=parser.add_argument('-action', '--action', help="Type of action to be performed your cdn")
+        cdn_sub_parser = parser.add_subparsers(title="CDN Commands", metavar="", dest="cdn_commands")
+        cdn_action=parser.add_argument('--action', help="Type of action to be performed your cdn")
         cdn_create_sub_parser = cdn_sub_parser.add_parser("create", help="To create a new cdn")
         cdn_delete_sub_parser = cdn_sub_parser.add_parser("delete", help="To delete a specific cdn")
         cdn_delete_sub_parser = cdn_sub_parser.add_parser("list", help="To get a list of all cdn")
         self.FormatUsageCommand(cdn_action, "cdn", "actions")
         self.FormatUsageCommand(cdn_create_sub_parser, "cdn", "create")
         self.FormatUsageCommand(cdn_delete_sub_parser, "cdn", "delete")
         self.FormatUsageCommand(cdn_delete_sub_parser, "cdn", "list")
 
     def volumes(self, parser):
-        volumes_sub_parser = parser.add_subparsers(title="volumes Commands", dest="volumes_commands")
-        volumes_action=parser.add_argument('-action', '--action', help="Type of action to be performed your volumes")
+        volumes_sub_parser = parser.add_subparsers(title="Volumes Commands", metavar="", dest="volumes_commands")
+        volumes_action=parser.add_argument('--action', help="Type of action to be performed your volumes")
         volumes_create_sub_parser = volumes_sub_parser.add_parser("create", help="To create a new volumes")
         volumes_delete_sub_parser = volumes_sub_parser.add_parser("delete", help="To delete a specific volumes")
         volumes_delete_sub_parser = volumes_sub_parser.add_parser("list", help="To get a list of all volumes")
         self.FormatUsageCommand(volumes_action, "volumes", "actions")
         self.FormatUsageCommand(volumes_create_sub_parser, "volumes", "create")
         self.FormatUsageCommand(volumes_delete_sub_parser, "volumes", "delete")
         self.FormatUsageCommand(volumes_delete_sub_parser, "volumes", "list")
            
     def dbaas(self, parser):
-        dbaas_sub_parser = parser.add_subparsers(title="DBaaS Commands", dest="dbaas_commands")
-        dbaas_action=parser.add_argument('-action', '--action', help="Type of action to be performed your dbaas")
+        dbaas_sub_parser = parser.add_subparsers(title="DBaaS Commands", metavar="", dest="dbaas_commands")
+        dbaas_action=parser.add_argument('--action', help="Type of action to be performed your dbaas")
         dbaas_create_sub_parser = dbaas_sub_parser.add_parser("create", help="To launch a new dbaas")
         dbaas_delete_sub_parser = dbaas_sub_parser.add_parser("delete", help="To delete a created dbaas")
         dbaas_list_sub_parser = dbaas_sub_parser.add_parser("list", help="To list all of your dbaas")
         self.FormatUsageCommand(dbaas_action, "dbaas", "actions")
         self.FormatUsageCommand(dbaas_create_sub_parser, "dbaas", "create")
         self.FormatUsageCommand(dbaas_list_sub_parser, "dbaas", "list")
         self.FormatUsageCommand(dbaas_delete_sub_parser, "dbaas", "delete")
 
 
-class ArgPaser(argparse.ArgumentParser):
+class Namespace(argparse._AttributeHolder):
+    """Simple object for storing attributes.
+    copied and over-written/modified here for getting unrecognised commands/inputs
+    """
+
+    def __init__(self, **kwargs):
+        for name in kwargs:
+            setattr(self, name, kwargs[name])
+
+    def __eq__(self, other):
+        if not isinstance(other, Namespace):
+            return NotImplemented
+        return vars(self) == vars(other)
+
+    def __contains__(self, key):
+        return key in self.__dict__
+
 
-    def version_and_pkg_info(self, msg):
-        if("argument -v/--version: expected one argument"==msg):
-            help_messages.e2e_version_info()
-            self.exit()
-
-        if("argument --info: expected one argument"==msg):
-            help_messages.e2e_pakage_info()
-            self.exit()
+class ArgPaser(argparse.ArgumentParser):
 
+    # used to collect input values 
+    def inputs_list(self, argv):
+        inputs=Namespace()
+        for element in argv:
+            if "=" in element:
+                    x=element.split("=")
+                    setattr(inputs, x[0], x[1])
+            elif(element.startswith('-')):
+                    setattr(inputs, element.lstrip('-'), True)
+        return inputs        
+        
+    def parse_args(self, args=None, namespace=None):
+        args, argv = self.parse_known_args(args, namespace)
+        if argv:
+            msg = argparse._('unrecognized arguments: %s')
+            self.error(msg % ' '.join(argv))
+        # here args is used for routing to service and inputs as input to service
+        return Namespace(args=args, inputs=self.inputs_list(argv))
 
     def error(self, message):
         args = {'prog': self.prog, 'message': message}
-        self.version_and_pkg_info(args["message"])
-        if("unrecognized arguments: -h" not in args["message"]):
-                        Py_version_manager.py_print( args["message"])
+        if("unrecognized arguments" not in args["message"]):
+                        PARSING_ERROR_MSG.append( args["message"])
 
 
 def commanding(parser):
     sub_parsers = parser.add_subparsers(title="Commands", dest="command")
-    alias_add_parser = sub_parsers.add_parser("add" )
-    alias_add_parser = sub_parsers.add_parser("add_file" )
-    alias_add_parser = sub_parsers.add_parser("view")
-    alias_delete_parser= sub_parsers.add_parser("delete")
+    alias_parser = sub_parsers.add_parser("help", help="To view man doc")
+    alias_parser = sub_parsers.add_parser("alias", help="To add delete tokens" )
     node_parser = sub_parsers.add_parser("node", help="To apply crud operations over Nodes")
     lb_parser = sub_parsers.add_parser("lb", help="To apply operations over Load-Balancer")
     bucket_parser = sub_parsers.add_parser("bucket", help="To create/delete/list buckets of the user")
     dbaas_parser = sub_parsers.add_parser("dbaas", help="To perform operations over DBaaS service provided")
     image_parser = sub_parsers.add_parser("image", help="To perform operations over Image service provided")
     autoscaling_parser= sub_parsers.add_parser("autoscaling", help="To create/delete/list autoscaling for the user")
     vpc_parser= sub_parsers.add_parser("vpc", help="To create/delete/list vpc for the user")
     cdn_parser= sub_parsers.add_parser("cdn", help="To create/delete/list cdn for the user")
     volumes_parser= sub_parsers.add_parser("volumes", help="To create/delete/list volume for the user")
     m = Main()
-    # m.config(config_parser)
+    m.alias(alias_parser)
     m.bucket(bucket_parser)
     m.node(node_parser)
     m.dbaas(dbaas_parser)
     m.lb(lb_parser)
     m.image(image_parser)
     m.autoscaling(autoscaling_parser)
     m.vpc(vpc_parser)
     m.cdn(cdn_parser)
     m.volumes(volumes_parser)
 
-    # m.FormatUsage(config_parser, "config")
+    m.FormatUsage(alias_parser, "alias")
     m.FormatUsage(node_parser, "node")
     m.FormatUsage(lb_parser, "lb")
     m.FormatUsage(bucket_parser, "bucket")
     m.FormatUsage(dbaas_parser, "dbaas")
     m.FormatUsage(autoscaling_parser, "autoscaling")
     m.FormatUsage(vpc_parser, "vpc")
     m.FormatUsage(cdn_parser, "cdn")
     m.FormatUsage(volumes_parser, "volumes")
 
 
 def run_main_class():
-    parser = ArgPaser(description="E2E CLI", formatter_class=help_messages.cli_formatter(), add_help=False)
-    parser.add_argument("-v", "--version", default=False)
-    parser.add_argument( "--info", default=False)
-    parser.add_argument("alias", metavar="option", type=str, help="The option to be used or name of your access credentials valid option")
+    parser = ArgPaser(description="E2E CLI", formatter_class=help_messages.cli_formatter())
+
+    #version, info, and alias to be taken first else default
+    parser.add_argument("-v", "--version", action='store_true', help="To view version Info")
+    parser.add_argument( "--info", action='store_true', help="To view package Info")
+    parser.add_argument("--alias", default="default", type=str, help="The name of your access credentials valid option")
+
+    # parsing our commands for routing
     commanding(parser)
 
+    # breakpoint()
     args = parser.parse_args()
     commands_route = CommandsRouting(args)
-    commands_route.route()
+    commands_route.route(PARSING_ERROR_MSG)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/node/node_actions/node_action.py` & `e2e_cli-0.9.9/e2e_cli/node/node_actions/node_action.py`

 * *Files 17% similar despite different names*

```diff
@@ -4,212 +4,213 @@
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core.request_service import Request
 from e2e_cli.core.alias_service import get_user_cred
 from e2e_cli.core.helper_service import Checks
 from e2e_cli.core.constants import BASE_URL
 
 
-def action_table(status, req):
-    if Checks.status_result(status, req):
-            try:
-                x = PrettyTable()
-                x.field_names = ["Action_type", "Status", "Action ID"]
-                x.add_row([status['data']['action_type'],
-                          status['data']['status'], status['data']['id']])
-                Py_version_manager.py_print(x)
-            except Exception as e:
-                      Checks.show_json(status, e)
-                      return
-
-    Checks.show_json(status)
-
 class nodeActions:
     def __init__(self, **kwargs):
         self.kwargs = kwargs
         if(get_user_cred(kwargs['alias'])):
             self.API_key=get_user_cred(kwargs['alias'])[1]
             self.Auth_Token=get_user_cred(kwargs['alias'])[0]
             self.possible=True
         else:
             self.possible=False
 
 
+    def action_table(self, status, req):
+        if Checks.status_result(status, req):
+                try:
+                    x = PrettyTable()
+                    x.field_names = ["Action_type", "Status", "Action ID"]
+                    x.add_row([status['data']['action_type'],
+                            status['data']['status'], status['data']['id']])
+                    Py_version_manager.py_print(x)
+                except Exception as e:
+                        Py_version_manager.py_print("Errors while reading json ", str(e))
+                
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
+
+
     def node_monitoring(self):
         my_payload= {}
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/monitor/server-health/?&apikey="+API_key
         req="GET"
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
-        Checks.show_json(status)
+        self.action_table(status, req) 
 
 
     
     def enable_recovery(self):
         my_payload= json.dumps({
                        "type": "enable_recovery_mode"
                 }) 
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)                 
+        self.action_table(status, req)                 
 
 
     def disable_recovery(self):
         my_payload= json.dumps({
                       "type": "disable_recovery_mode"
                })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)
+        self.action_table(status, req)
                
 
 
     def reinstall(self):
         my_payload= json.dumps({
                         "type": "reinstall"
                       })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)    
+        self.action_table(status, req)    
          
 
 
     def reboot(self):
         my_payload= json.dumps({
                            "type": "reboot"
                         })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)                  
+        self.action_table(status, req)                  
 
 
 
     def power_on(self):
         my_payload= json.dumps({
                         "type": "power_on"
                   }) 
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)              
+        self.action_table(status, req)              
         
 
 
     def power_off(self):
         my_payload= json.dumps({
                          "type": "power_off"
                  })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)             
+        self.action_table(status, req)             
     
 
 
     def rename_node(self):
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         new_name=Py_version_manager.py_input("please enter new name for the node : ")
         my_payload= json.dumps({
                        "name": new_name,
                        "type": "rename"
                   })  
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)
+        self.action_table(status, req)
                
         
 
     def unlock_vm(self):
         my_payload= json.dumps({
                         "type": "unlock_vm"
                  })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)
+        self.action_table(status, req)
                
     
 
     def lock_vm(self):
         my_payload= json.dumps({
                         "type": "lock_vm"
                  })  
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/"+ node_id +"/actions/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
         
-        action_table(status, req)
+        self.action_table(status, req)
```

### Comparing `e2e_cli-0.9.8/e2e_cli/node/node_crud/node.py` & `e2e_cli-0.9.9/e2e_cli/node/node_crud/node.py`

 * *Files 26% similar despite different names*

```diff
@@ -5,35 +5,33 @@
 from e2e_cli.core.py_manager import Py_version_manager
 from e2e_cli.core.alias_service import get_user_cred
 from e2e_cli.core.request_service import Request
 from e2e_cli.core.helper_service import Checks
 from e2e_cli.core.constants import BASE_URL
 from e2e_cli.node.node_crud.node_listing_service import Nodelisting
 
-
     
 class payload:
-    def __init__(self, alias):
-        self.Option=Py_version_manager.py_input("How would u like to proceed?? For auto input type 'auto' ")
+    def __init__(self, arguments):
 
-        if(self.Option.lower()=="auto"):
-            node_specifications=Nodelisting(alias).node_listing()
+        if('auto' in arguments["inputs"]):
+            node_specifications=Nodelisting(arguments['alias']).node_listing()
             self.image = node_specifications['image']
             self.plan = node_specifications['plan']
             if(node_specifications['location']=='Delhi'):
                     self.region='ncr'
             else:
                     self.region='mumbai'
         else :
-            self.image = Py_version_manager.py_input("please enter OS you require : ")
-            self.plan = Py_version_manager.py_input("please enter system requirements/plans : ")
-            self.region= Py_version_manager.py_input("please enter region in where server is required : ")
+            self.image = Checks.take_input(arguments["inputs"], "image")
+            self.plan = Checks.take_input(arguments["inputs"], "plan")
+            self.region = Checks.take_input(arguments["inputs"], "region")
                     
-        self.security_group_id = Py_version_manager.py_input("please enter security group id : ")
-        self.name = Py_version_manager.py_input("please enter name of your node : ")
+        self.security_group_id = Checks.take_input(arguments["inputs"], "security_group_id")
+        self.name = Checks.take_input(arguments["inputs"], "name")
         self.ssh_keys = []
 
 
 class NodeCrud:
     def __init__(self, **kwargs):
         self.kwargs = kwargs
         if (get_user_cred(kwargs['alias'])):
@@ -42,85 +40,84 @@
             self.possible = True
         else:
             self.possible = False
 
 
     def create_node(self):
         Py_version_manager.py_print("Creating")
-        my_payload = payload(self.kwargs['alias'])
+        my_payload = payload(self.kwargs)
         API_key = self.API_key
         Auth_Token = self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/?apikey=" + API_key+"&location=Delhi"
         req = "POST"
-        if (my_payload.Option=="auto"):
+        if ('auto' in self.kwargs["inputs"]):
                         user_agent='cli_python'
         else:
                 user_agent='cli-e2e'
         my_payload=my_payload.__dict__
-        my_payload.pop('Option')
 
         status = Request(url, Auth_Token, json.dumps(my_payload), req, user_agent).response.json()
-        
+    
         if Checks.status_result(status,req):
             try :
                 x = PrettyTable()
                 x.field_names = ["ID", "Name", "Created at", "disk", "Status", "Plan"]
                 x.add_row([status['data']['id'], status['data']['name'],
                       status['data']['created_at'], status['data']['disk'], status['data']['status'], status['data']['plan']])
                 Py_version_manager.py_print(x)
             except Exception as e:
-                        Checks.show_json(status, e)
-                        return
+                    Py_version_manager.py_print("Errors : ", e)
 
-        Checks.show_json(status)
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
 
 
     def delete_node(self):
         my_payload = {}
         API_key = self.API_key
         Auth_Token = self.Auth_Token
-        node_id = Py_version_manager.py_input("please enter node id : ")
+        node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         url =  BASE_URL+"myaccount/api/v1/nodes/" + str(node_id) + "/?apikey="+API_key
         req = "DELETE"
 
         confirmation =Py_version_manager.py_input("are you sure you want to delete press y for yes, else any other key : ")
         if(confirmation.lower()=="y"):
             status = Request(url, Auth_Token, my_payload, req).response.json()
             if Checks.status_result(status,req):
                         Py_version_manager.py_print("Node Successfully deleted")
                         Py_version_manager.py_print("use following command -> e2e_cli <alias> node list to check if bucket has been deleted")
             
-            Checks.show_json(status)
-    
+            if('json' in self.kwargs["inputs"]):
+                Checks.show_json(status)
 
 
     def get_node_by_id(self):
         my_payload = {}
         API_key = self.API_key
         Auth_Token = self.Auth_Token
-        node_id = Py_version_manager.py_input("please enter node id ")
+        node_id = node_id = Checks.take_input(self.kwargs["inputs"], "node_id")
         while(not Checks.is_int(node_id)):
               node_id = Py_version_manager.py_input("please enter node id (integer only) ")
         url =  BASE_URL+"myaccount/api/v1/nodes/" + str(node_id) + "/?apikey="+API_key
         req = "GET"
         status = Request(url, Auth_Token, my_payload, req).response.json()
 
         if Checks.status_result(status, req):
             try:
                 x = PrettyTable()
                 x.field_names = ["VM id", "Name", "Created at", "disk", "Plan", "Public IP", "Status"]
                 x.add_row([ status['data']['vm_id'], status['data']['name'], status['data']['created_at'], status['data']['disk'],  status['data']['plan'], status['data']['public_ip_address'], status['data']['status'] ])
                 Py_version_manager.py_print(x)
             except Exception as e:
-                        Checks.show_json(status, e)
-                        return
+                        Py_version_manager.py_print("Errors : ", e)
         
-        Checks.show_json(status)
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)
 
 
     def list_node(self, parameter=0):
         my_payload = {}
         API_key = self.API_key
         Auth_Token = self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/nodes/?apikey=" + API_key+"&location=Delhi"
@@ -137,17 +134,18 @@
                     x.field_names = ["index", "ID", "Name", "Created at", "disk", "Plan", "Status"]
                     for element in list:
                         x.add_row([i, element['id'], element['name'],
                                 element['created_at'], element['disk'],  element['plan'],  element['status']])
                         i = i+1
                     Py_version_manager.py_print(x)
                 except Exception as e:
-                        Checks.show_json(status, e)
-                        return       
-                Checks.show_json(status)
+                        Py_version_manager.py_print("Errors : ", e)
+                        
+                if('json' in self.kwargs["inputs"]):
+                    Checks.show_json(status)
             
         elif parameter==1:
                     return status['data']
 
 
     def update_node(self):
         API_key = self.API_key
```

### Comparing `e2e_cli-0.9.8/e2e_cli/node/node_crud/node_listing_service.py` & `e2e_cli-0.9.9/e2e_cli/node/node_crud/node_listing_service.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/node/node_routing.py` & `e2e_cli-0.9.9/e2e_cli/node/node_routing.py`

 * *Files 21% similar despite different names*

```diff
@@ -5,132 +5,120 @@
 from e2e_cli.node.node_actions.node_action import nodeActions
 
 class NodeRouting:
     def __init__(self, arguments):
         self.arguments = arguments
         
 
-    def route(self):
-        if (self.arguments.node_commands is None) and (self.arguments.action is None):
-            subprocess.call(['e2e_cli', 'alias','node', '-h'])
+    def route(self, Parsing_Errors):
+        if (self.arguments.args.node_commands is None) and (self.arguments.args.action is None):
+            subprocess.call(['e2e_cli','node', '-h'])
 
-        elif (self.arguments.node_commands is not None) and (self.arguments.action is not None):
+
+        elif (self.arguments.args.node_commands is not None) and (self.arguments.args.action is not None):
               Py_version_manager.py_print("Only one action at a time !!")
-              
-        if self.arguments.node_commands == 'create':
-            Node_operations = NodeCrud(alias=self.arguments.alias )
+
+
+        elif(self.arguments.args.node_commands is not None):
+            Node_operations = NodeCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
             if(Node_operations.possible):
+
+                if self.arguments.args.node_commands == 'create':
                         try:
-                           Node_operations.create_node()
+                            Node_operations.create_node()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")  
-                              
+                                Py_version_manager.py_print(" ")  
+                            
 
-        elif self.arguments.node_commands == 'delete':
-            Node_operations = NodeCrud(alias=self.arguments.alias)
-            if(Node_operations.possible):
+                elif self.arguments.args.node_commands == 'delete':
                         try:
-                           Node_operations.delete_node()
+                            Node_operations.delete_node()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+                                Py_version_manager.py_print(" ")
                         
 
-        elif self.arguments.node_commands == 'get':
-            Node_operations = NodeCrud(alias=self.arguments.alias)
-            if(Node_operations.possible):
+                elif self.arguments.args.node_commands == 'get':
                         try:
-                           Node_operations.get_node_by_id()
+                            Node_operations.get_node_by_id()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
-                        
-                                    
-        elif self.arguments.node_commands == 'list':
-            Node_operations = NodeCrud(alias=self.arguments.alias)
-            if(Node_operations.possible):
+                                Py_version_manager.py_print(" ")
+                            
+                                            
+                elif self.arguments.args.node_commands == 'list':
                         try: 
-                           Node_operations.list_node()
+                            Node_operations.list_node()
                         except KeyboardInterrupt:
-                            Py_version_manager.py_print(" ")
+                                Py_version_manager.py_print(" ")
                         
 
-        elif self.arguments.action == 'enable_recovery':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
+        elif(self.arguments.args.action is not None):
+            Node_operations=nodeActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs) 
             if(Node_operations.possible):
+
+                if self.arguments.args.action == 'enable_recovery':  
                         try: 
                            Node_operations.enable_recovery()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'disable_recovery':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'disable_recovery':  
                         try: 
                            Node_operations.disable_recovery()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'reinstall':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'reinstall':  
                         try: 
                            Node_operations.reinstall()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'reboot':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'reboot':  
                         try: 
                            Node_operations.reboot()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'power_on':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'power_on':  
                         try: 
                            Node_operations.power_on()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'power_off':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'power_off':  
                         try: 
                            Node_operations.power_off()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'rename_node':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'rename_node':  
                         try: 
                            Node_operations.rename_node()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'lock_vm':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'lock_vm':  
                         try: 
                            Node_operations.lock_vm()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action == 'unlock_vm':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action == 'unlock_vm':  
                         try: 
                            Node_operations.unlock_vm()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-        
-        elif self.arguments.action =='monitor':
-            Node_operations=nodeActions(alias=self.arguments.alias)     
-            if(Node_operations.possible):
+            
+                elif self.arguments.args.action =='monitor':
                         try: 
                            Node_operations.node_monitoring()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
+                
+                else:
+                    Py_version_manager.py_print("command not found")
+                    Py_version_manager.py_print(*Parsing_Errors, sep="\n")
+
 
         else:
             Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/volumes/volumes_actions/volumes_action.py` & `e2e_cli-0.9.9/e2e_cli/volumes/volumes_actions/volumes_action.py`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/e2e_cli/volumes/volumes_routing.py` & `e2e_cli-0.9.9/e2e_cli/volumes/volumes_routing.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,55 +5,58 @@
 from e2e_cli.volumes.volumes_actions.volumes_action import volumesActions
 
 class volumes_Routing:
     def __init__(self, arguments):
         self.arguments = arguments
         
         
-    def route(self):
-        if (self.arguments.action is None) and (self.arguments.volumes_commands is None):
-            subprocess.call(['e2e_cli', 'alias', 'volumes', '-h'])
+    def route(self,  Parsing_Errors):
+        if (self.arguments.args.action is None) and (self.arguments.args.volumes_commands is None):
+            subprocess.call(['e2e_cli', 'volumes', '-h'])
 
-        elif (self.arguments.volumes_commands is not None) and (self.arguments.action is not None):
+
+        elif (self.arguments.args.volumes_commands is not None) and (self.arguments.args.action is not None):
               Py_version_manager.py_print("Only one action at a time !!")
 
-        elif self.arguments.volumes_commands == 'create':
-            volumes_operations = volumes_Crud(alias=self.arguments.alias )
+
+        elif(self.arguments.args.volumes_commands is not None):
+            volumes_operations = volumes_Crud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
             if(volumes_operations.possible):
+
+                if self.arguments.args.volumes_commands == 'create':
                         try:
                             volumes_operations.create_volumes()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
 
-        elif self.arguments.volumes_commands == 'delete':
-            volumes_operations = volumes_Crud(alias=self.arguments.alias)
-            if(volumes_operations.possible):
+                elif self.arguments.args.volumes_commands == 'delete':
                         try:
                             volumes_operations.delete_volumes()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
-                        
-        elif self.arguments.volumes_commands == 'list':
-            volumes_operations = volumes_Crud(alias=self.arguments.alias)
-            if(volumes_operations.possible):
+                                
+                elif self.arguments.args.volumes_commands == 'list':
                         try:
                             volumes_operations.list_volumes()
                         except KeyboardInterrupt:
                             Py_version_manager.py_print(" ")
 
-        # elif self.arguments.action == "attach_volume":
-        #     volumes_operations = volumesActions(alias=self.arguments.alias)
+        # elif self.arguments.args.action == "attach_volume":
+        #     volumes_operations = volumesActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
         #     if(volumes_operations.possible):
         #                 try:
         #                     volumes_operations.attach_volume()
         #                 except KeyboardInterrupt:
         #                     Py_version_manager.py_print(" ")
 
-        # elif self.arguments.action == "desable_volumes":
-        #     volumes_operations = volumesActions(alias=self.arguments.alias)
+        # elif self.arguments.args.action == "desable_volumes":
+        #     volumes_operations = volumesActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
         #     if(volumes_operations.possible):
         #                 try:
         #                     volumes_operations.disable_volumes()
         #                 except KeyboardInterrupt:
         #                     Py_version_manager.py_print(" ")
         
-        
+        
+        else:
+            Py_version_manager.py_print("command not found")
+            Py_version_manager.py_print(*Parsing_Errors, sep="\n")
```

### Comparing `e2e_cli-0.9.8/e2e_cli/vpc/vpc.py` & `e2e_cli-0.9.9/e2e_cli/vpc/vpc.py`

 * *Files 8% similar despite different names*

```diff
@@ -19,49 +19,49 @@
             self.possible=False
         
 
     def create_vpc(self):
         Py_version_manager.py_print("Creating")
         my_payload= json.dumps({
                 "network_size": 512,
-                "vpc_name": Py_version_manager.py_input("input name of your new vpc : ")
+                "vpc_name": Checks.take_input(self.kwargs["inputs"], "vpc_name")
             }) 
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"myaccount/api/v1/vpc/?apikey="+API_key+"&location=Delhi"
         req="POST"
         status=Request(url, Auth_Token, my_payload, req).response.json()
                
         if Checks.status_result(status, req):
             try:
                 x = PrettyTable()
                 x.field_names = ["ID", "Name"]
                 x.add_row([status['data']['vpc_id'], status['data']['name'] ])
                 Py_version_manager.py_print(x)
             except Exception as e:
-                      Checks.show_json(status, e)
-                      return
+                      Py_version_manager.py_print("Errors : ", e)
                   
-        Checks.show_json(status)    
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)    
 
 
     def delete_vpc(self):
         my_payload={}
-        network_id=Py_version_manager.py_input("input network_id of the vpc you want to delete : ")
+        network_id=Checks.take_input(self.kwargs["inputs"], "network_id")
         while(not Checks.is_int(network_id)):
                 network_id=Py_version_manager.py_input("Only integers allowed ")
         API_key=self.API_key
         Auth_Token=self.Auth_Token
         url =  BASE_URL+"/myaccount/api/v1/vpc/"+ network_id +"/?apikey="+API_key
         req="DELETE"
         status=Request(url, Auth_Token, my_payload, req).response.json()
 
         if Checks.status_result(status,req):
                         Py_version_manager.py_print("vpc Successfully deleted")
-                        Py_version_manager.py_print("use following command -> e2e_cli <alias> vpc list to check if vpc has been deleted")
+                        Py_version_manager.py_print("use following command -> e2e_cli --alias vpc list to check if vpc has been deleted")
         
         Checks.show_json(status)
 
 
     def list_vpc(self):
         my_payload={}
         API_key= self.API_key  
@@ -78,13 +78,13 @@
                     x = PrettyTable()
                     x.field_names = ["index", "network_id", "Name", "network_mask", "gateway_ip", "pool_size"]
                     for element in list:
                         x.add_row([i, element['network_id'], element['name'], element['network_mask'], element["gateway_ip"], element["pool_size"]])
                         i = i+1
                     Py_version_manager.py_print(x)
                 except Exception as e:
-                      Checks.show_json(status, e)
-                      return
+                      Py_version_manager.py_print("Errors : ", e)
+
+        if('json' in self.kwargs["inputs"]):
+            Checks.show_json(status)    
 
-        Checks.show_json(status)
-
```

### Comparing `e2e_cli-0.9.8/e2e_cli.egg-info/SOURCES.txt` & `e2e_cli-0.9.9/e2e_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `e2e_cli-0.9.8/setup.py` & `e2e_cli-0.9.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
   from setuptools import setup, find_packages
 except ImportError:
   subprocess.call["pip","install","setuptools"]
   from setuptools import setup, find_packages
 
 setup(
     name='e2e_cli',
-    version='0.9.8',
+    version='0.9.9',
     description="This a E2E CLI tool for myAccount",
     author="Sajal&Aman@E2E_Networks_Ltd",
     packages=find_packages(),
     install_requires=['prettytable', 'requests', 'setuptools', 'chardet'],
 
     include_package_data = True,
     package_data = {
```

