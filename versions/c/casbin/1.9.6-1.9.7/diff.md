# Comparing `tmp/casbin-1.9.6.tar.gz` & `tmp/casbin-1.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "casbin-1.9.6.tar", last modified: Fri Nov 12 15:45:33 2021, max compression
+gzip compressed data, was "casbin-1.9.7.tar", last modified: Thu Nov 18 13:58:44 2021, max compression
```

## Comparing `casbin-1.9.6.tar` & `casbin-1.9.7.tar`

### file list

```diff
@@ -1,75 +1,75 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2021-11-12 15:44:51.000000 casbin-1.9.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    15588 2021-11-12 15:45:33.397509 casbin-1.9.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    14728 2021-11-12 15:44:51.000000 casbin-1.9.6/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/casbin/
--rw-r--r--   0 runner    (1001) docker     (121)      207 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/casbin/config/
--rw-r--r--   0 runner    (1001) docker     (121)       27 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4665 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/config/config.py
--rw-r--r--   0 runner    (1001) docker     (121)    14236 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/core_enforcer.py
--rw-r--r--   0 runner    (1001) docker     (121)     5091 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/distributed_enforcer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/casbin/effect/
--rw-r--r--   0 runner    (1001) docker     (121)      954 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/effect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2219 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/effect/default_effectors.py
--rw-r--r--   0 runner    (1001) docker     (121)      408 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/effect/effector.py
--rw-r--r--   0 runner    (1001) docker     (121)     7648 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/enforcer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4749 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/internal_enforcer.py
--rw-r--r--   0 runner    (1001) docker     (121)    12801 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/management_enforcer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/casbin/model/
--rw-r--r--   0 runner    (1001) docker     (121)      119 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1762 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/assertion.py
--rw-r--r--   0 runner    (1001) docker     (121)      735 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/function.py
--rw-r--r--   0 runner    (1001) docker     (121)     2699 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/model.py
--rw-r--r--   0 runner    (1001) docker     (121)     8517 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/policy.py
--rw-r--r--   0 runner    (1001) docker     (121)       82 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/model/policy_op.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/casbin/persist/
--rw-r--r--   0 runner    (1001) docker     (121)      108 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1138 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      472 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapter_filtered.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/casbin/persist/adapters/
--rw-r--r--   0 runner    (1001) docker     (121)      126 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2637 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapters/adapter_filtered.py
--rw-r--r--   0 runner    (1001) docker     (121)     1875 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapters/file_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      501 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/adapters/update_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      416 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/batch_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      784 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/dispatcher.py
--rw-r--r--   0 runner    (1001) docker     (121)     1426 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/watcher.py
--rw-r--r--   0 runner    (1001) docker     (121)     2473 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/watcher_ex.py
--rw-r--r--   0 runner    (1001) docker     (121)     1304 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/persist/watcher_update.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/casbin/rbac/
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/rbac/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/casbin/rbac/default_role_manager/
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/rbac/default_role_manager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9625 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/rbac/default_role_manager/role_manager.py
--rw-r--r--   0 runner    (1001) docker     (121)      463 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/rbac/role_manager.py
--rw-r--r--   0 runner    (1001) docker     (121)    22768 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/synced_enforcer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/casbin/util/
--rw-r--r--   0 runner    (1001) docker     (121)       79 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4699 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/util/builtin_operators.py
--rw-r--r--   0 runner    (1001) docker     (121)      851 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/util/expression.py
--rw-r--r--   0 runner    (1001) docker     (121)     1803 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/util/rwlock.py
--rw-r--r--   0 runner    (1001) docker     (121)     2121 2021-11-12 15:44:51.000000 casbin-1.9.6/casbin/util/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/casbin.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    15588 2021-11-12 15:45:33.000000 casbin-1.9.6/casbin.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1585 2021-11-12 15:45:33.000000 casbin-1.9.6/casbin.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-12 15:45:33.000000 casbin-1.9.6/casbin.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       34 2021-11-12 15:45:33.000000 casbin-1.9.6/casbin.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2021-11-12 15:45:33.000000 casbin-1.9.6/casbin.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       66 2021-11-12 15:45:33.401510 casbin-1.9.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1551 2021-11-12 15:44:51.000000 casbin-1.9.6/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.393509 casbin-1.9.6/tests/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/tests/config/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2034 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/config/test_config.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/tests/model/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5198 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/model/test_policy.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/tests/rbac/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/rbac/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8319 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/rbac/test_role_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-12 15:45:33.397509 casbin-1.9.6/tests/util/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9455 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/util/test_builtin_operators.py
--rw-r--r--   0 runner    (1001) docker     (121)     2172 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/util/test_rwlock.py
--rw-r--r--   0 runner    (1001) docker     (121)     2868 2021-11-12 15:44:51.000000 casbin-1.9.6/tests/util/test_util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2021-11-18 13:58:04.000000 casbin-1.9.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)    15588 2021-11-18 13:58:44.716019 casbin-1.9.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    14728 2021-11-18 13:58:04.000000 casbin-1.9.7/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.708019 casbin-1.9.7/casbin/
+-rw-r--r--   0 runner    (1001) docker     (121)      207 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/config/
+-rw-r--r--   0 runner    (1001) docker     (121)       27 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4665 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/config/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14445 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/core_enforcer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5091 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/distributed_enforcer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/effect/
+-rw-r--r--   0 runner    (1001) docker     (121)      954 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/effect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2219 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/effect/default_effectors.py
+-rw-r--r--   0 runner    (1001) docker     (121)      408 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/effect/effector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7646 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/enforcer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4749 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/internal_enforcer.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12801 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/management_enforcer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/model/
+-rw-r--r--   0 runner    (1001) docker     (121)      119 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1762 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/assertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      735 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2699 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8517 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)       82 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/model/policy_op.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/persist/
+-rw-r--r--   0 runner    (1001) docker     (121)      108 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1138 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      472 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapter_filtered.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/persist/adapters/
+-rw-r--r--   0 runner    (1001) docker     (121)      126 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2637 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapters/adapter_filtered.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1875 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapters/file_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      501 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/adapters/update_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      416 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/batch_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      784 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/dispatcher.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1426 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/watcher.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2473 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/watcher_ex.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1304 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/persist/watcher_update.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.712020 casbin-1.9.7/casbin/rbac/
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/rbac/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/casbin/rbac/default_role_manager/
+-rw-r--r--   0 runner    (1001) docker     (121)       53 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/rbac/default_role_manager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10332 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/rbac/default_role_manager/role_manager.py
+-rw-r--r--   0 runner    (1001) docker     (121)      463 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/rbac/role_manager.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22768 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/synced_enforcer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/casbin/util/
+-rw-r--r--   0 runner    (1001) docker     (121)       79 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4699 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/util/builtin_operators.py
+-rw-r--r--   0 runner    (1001) docker     (121)      851 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/util/expression.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1803 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/util/rwlock.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2121 2021-11-18 13:58:04.000000 casbin-1.9.7/casbin/util/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.708019 casbin-1.9.7/casbin.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    15588 2021-11-18 13:58:44.000000 casbin-1.9.7/casbin.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1585 2021-11-18 13:58:44.000000 casbin-1.9.7/casbin.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-18 13:58:44.000000 casbin-1.9.7/casbin.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       34 2021-11-18 13:58:44.000000 casbin-1.9.7/casbin.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2021-11-18 13:58:44.000000 casbin-1.9.7/casbin.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       66 2021-11-18 13:58:44.716019 casbin-1.9.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1551 2021-11-18 13:58:04.000000 casbin-1.9.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.708019 casbin-1.9.7/tests/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/tests/config/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2034 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/config/test_config.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/tests/model/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5198 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/model/test_policy.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/tests/rbac/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/rbac/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10995 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/rbac/test_role_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:44.716019 casbin-1.9.7/tests/util/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9455 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/util/test_builtin_operators.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2172 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/util/test_rwlock.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2868 2021-11-18 13:58:04.000000 casbin-1.9.7/tests/util/test_util.py
```

### Comparing `casbin-1.9.6/LICENSE` & `casbin-1.9.7/LICENSE`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/PKG-INFO` & `casbin-1.9.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: casbin
-Version: 1.9.6
+Version: 1.9.7
 Summary: An authorization library that supports access control models like ACL, RBAC, ABAC in Python
 Home-page: https://github.com/casbin/pycasbin
 Author: TechLee
 Author-email: techlee@qq.com
 License: Apache 2.0
 Keywords: casbin,acl,rbac,abac,auth,authz,authorization,access control,permission
 Platform: UNKNOWN
```

### Comparing `casbin-1.9.6/README.md` & `casbin-1.9.7/README.md`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/config/config.py` & `casbin-1.9.7/casbin/config/config.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/core_enforcer.py` & `casbin-1.9.7/casbin/core_enforcer.py`

 * *Files 2% similar despite different names*

```diff
@@ -169,15 +169,19 @@
         """clears all policy."""
 
         self.model.clear_policy()
 
     def init_rm_map(self):
         if "g" in self.model.keys():
             for ptype in self.model["g"]:
-                self.rm_map[ptype] = default_role_manager.RoleManager(10)
+                assertion = self.model["g"][ptype]
+                if assertion.value.count("_") == 2:
+                    self.rm_map[ptype] = default_role_manager.RoleManager(10)
+                else:
+                    self.rm_map[ptype] = default_role_manager.DomainManager(10)
 
     def load_policy(self):
         """reloads the policy from file/database."""
         need_to_rebuild = False
         new_model = copy.copy(self.model)
         new_model.clear_policy()
```

### Comparing `casbin-1.9.6/casbin/distributed_enforcer.py` & `casbin-1.9.7/casbin/distributed_enforcer.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/effect/__init__.py` & `casbin-1.9.7/casbin/effect/__init__.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/effect/default_effectors.py` & `casbin-1.9.7/casbin/effect/default_effectors.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/enforcer.py` & `casbin-1.9.7/casbin/enforcer.py`

 * *Files 0% similar despite different names*

```diff
@@ -106,15 +106,15 @@
 
     def has_permission_for_user(self, user, *permission):
         """
         determines whether a user has a permission.
         """
         return self.has_policy(join_slice(user, *permission))
 
-    def get_implicit_roles_for_user(self, name, domain=None):
+    def get_implicit_roles_for_user(self, name, domain=""):
         """
         gets implicit roles that a user has.
         Compared to get_roles_for_user(), this function retrieves indirect roles besides direct roles.
         For example:
         g, alice, role:admin
         g, role:admin, role:user
```

### Comparing `casbin-1.9.6/casbin/internal_enforcer.py` & `casbin-1.9.7/casbin/internal_enforcer.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/management_enforcer.py` & `casbin-1.9.7/casbin/management_enforcer.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/model/assertion.py` & `casbin-1.9.7/casbin/model/assertion.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/model/function.py` & `casbin-1.9.7/casbin/model/function.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/model/model.py` & `casbin-1.9.7/casbin/model/model.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/model/policy.py` & `casbin-1.9.7/casbin/model/policy.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/adapter.py` & `casbin-1.9.7/casbin/persist/adapter.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/adapters/adapter_filtered.py` & `casbin-1.9.7/casbin/persist/adapters/adapter_filtered.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/adapters/file_adapter.py` & `casbin-1.9.7/casbin/persist/adapters/file_adapter.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/dispatcher.py` & `casbin-1.9.7/casbin/persist/dispatcher.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/watcher.py` & `casbin-1.9.7/casbin/persist/watcher.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/watcher_ex.py` & `casbin-1.9.7/casbin/persist/watcher_ex.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/persist/watcher_update.py` & `casbin-1.9.7/casbin/persist/watcher_update.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/rbac/default_role_manager/role_manager.py` & `casbin-1.9.7/casbin/rbac/default_role_manager/role_manager.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,326 +1,342 @@
 import logging
+from collections import namedtuple
+from enum import Enum
 
-from casbin.rbac import RoleManager
+from casbin.rbac import RoleManager as RM
 
+Link = namedtuple("Link", ["user", "role"])
 
-class RoleManager(RoleManager):
-    """provides a default implementation for the RoleManager interface"""
 
-    all_roles = dict()
-    max_hierarchy_level = 0
+class MatchOrder(Enum):
+    STR_PATTERN = 0
+    PATTERN_STR = 1
+    PATTERN_PATTERN = 2
+
+
+class Role:
+    def __init__(self, name):
+        self.name = name
+        self.roles = set()
+        self.users = set()
+
+    def add_role(self, role):
+        self.roles.add(role)
+        role._add_user(self)
+
+    def remove_role(self, role):
+        self.roles.remove(role)
+        role._remove_user(self)
+
+    def _add_user(self, user):
+        self.users.add(user)
+
+    def _remove_user(self, user):
+        self.users.remove(user)
+
+    def copy_from(self, role):
+        for r in role.roles:
+            self.add_role(r)
+        for u in role.users:
+            u.add_role(self)
+
+    def empty(self):
+        return len(self.users) + len(self.roles) == 0
+
+    def to_string(self):
+        if len(self.roles) == 0:
+            return ""
+
+        names = ", ".join(self.get_roles())
+
+        if len(self.roles) == 1:
+            return self.name + " < " + names
+        else:
+            return self.name + " < (" + names + ")"
+
+    def get_roles(self):
+        roles = []
+        for role in self.roles:
+            roles.append(role.name)
+
+        return roles
+
+
+class RoleManager(RM):
+    """provides a default implementation for the RoleManager interface"""
 
     def __init__(self, max_hierarchy_level=10):
         self.logger = logging.getLogger(__name__)
-        self.all_roles = dict()
         self.max_hierarchy_level = max_hierarchy_level
-        self.matching_func = None
-        self.domain_matching_func = None
-        self.has_pattern = False
-        self.has_domain_pattern = False
+        self.matching_func = lambda name1, name2: name1 == name2
+        self.all_links = list()
+        self.all_roles = dict()
 
-    def add_matching_func(self, fn=None):
-        self.has_pattern = True
+    def _rebuild(self):
+        self.all_roles = dict()
+        links = self.all_links
+        self.all_links = list()
+        for link in links:
+            self.add_link(link.user, link.role)
+
+    def _matching_fn(self, str1, str2, match_order=MatchOrder.STR_PATTERN):
+        if match_order == MatchOrder.PATTERN_STR:
+            return match_error_handler(self.matching_func, str2, str1)
+        elif match_order == MatchOrder.PATTERN_PATTERN:
+            return match_error_handler(
+                self.matching_func, str1, str2
+            ) or match_error_handler(self.matching_func, str2, str1)
+        else:  # match_order == MatchOrder.STR_PATTERN
+            return match_error_handler(self.matching_func, str1, str2)
+
+    def _matching_roles(self, name, match_order=MatchOrder.STR_PATTERN):
+        return [
+            role
+            for role_name, role in list(
+                self.all_roles.items()
+            )  # convert view to list to avoid RuntimeError: dictionary changed size during iteration
+            if self._matching_fn(name, role_name, match_order)
+        ]
+
+    def _get_role(self, name):
+        if name not in self.all_roles:
+            role = Role(name)
+            for pattern_role in self._matching_roles(name):
+                role.copy_from(pattern_role)
+            self.all_roles[name] = role
+        return self.all_roles[name]
+
+    def add_matching_func(self, fn):
         self.matching_func = fn
+        self._rebuild()
 
     def add_domain_matching_func(self, fn=None):
-        self.has_domain_pattern = True
         self.domain_matching_func = fn
 
-    def has_role(self, role):
+    def clear(self):
+        self.all_roles = dict()
+        self.all_links = list()
 
-        if not self.has_pattern and not self.has_domain_pattern:
-            return role in self.all_roles.values()
+    def add_link(self, name1, name2, *domain):
+        self.all_links.append(Link(name1, name2))
 
-        for known_role in list(self.all_roles.values()):
-            if self.has_pattern:
-                if not self.matching_func(role.name, known_role.name):
-                    continue
-            else:
-                if not role.name == known_role.name:
-                    continue
-
-            if self.has_domain_pattern:
-                if not self.domain_matching_func(role.domain, known_role.domain):
-                    continue
-            else:
-                if not role.domain == known_role.domain:
-                    continue
-            return True
-
-    def create_role(self, name, domain=""):
-        role = Role(name, domain)
-        if domain:
-            key = domain + "::" + name
-        else:
-            key = name
+        user = self._get_role(name1)
+        role = self._get_role(name2)
 
-        if key not in self.all_roles.keys():
-            self.all_roles[key] = role
+        user.add_role(role)
 
-        return self.all_roles[key]
+        for r in self.all_roles.values():
+            if r.name != user.name and self._matching_fn(
+                user.name, r.name, MatchOrder.PATTERN_STR
+            ):
+                r.add_role(role)
+            if r.name != role.name and self._matching_fn(
+                role.name, r.name, MatchOrder.PATTERN_STR
+            ):
+                role.add_role(r)
 
-    def clear(self):
-        self.all_roles.clear()
+    def delete_link(self, name1, name2, *domain):
+        if Link(name1, name2) not in self.all_links:
+            raise RuntimeError(
+                f"error: link between {name1} and {name2} does not exist"
+            )
+        self.all_links.remove(Link(name1, name2))
+
+        user = self._get_role(name1)
+        role = self._get_role(name2)
+        user.remove_role(role)
+
+        for r in self.all_roles.values():
+            if r.name != user.name and self._matching_fn(
+                user.name, r.name, MatchOrder.PATTERN_STR
+            ):
+                r.remove_role(role)
+            if r.name != role.name and self._matching_fn(
+                role.name, r.name, MatchOrder.PATTERN_STR
+            ):
+                role.remove_role(r)
 
-    def add_link(self, name1, name2, *domain):
-        if len(domain) > 1:
-            raise RuntimeError("error: domain should be 1 parameter")
-        elif len(domain) == 1:
-            domain = domain[0]
-        else:
-            domain = ""
+    def has_link(self, name1, name2, *domain):
+        user = self._get_role(name1)
+        role = self._get_role(name2)
 
-        role1 = self.create_role(name1, domain)
-        role2 = self.create_role(name2, domain)
-        role1.add_role(role2)
-
-        if self.has_pattern:
-            for role in self.all_roles.values():
-                if self.has_domain_pattern:
-                    if not self.domain_matching_func(domain, role.domain):
-                        continue
-                else:
-                    if domain != role.domain:
-                        continue
-
-                def duplicate_judge():
-                    return role1.name != role.name and role2.name != role.name
-
-                if (
-                    match_error_handler(self.matching_func, role.name, role1.name)
-                    or match_error_handler(self.matching_func, role1.name, role.name)
-                    and duplicate_judge()
-                ):
-                    self.all_roles[role.get_key()].add_role(role1)
-
-                if (
-                    match_error_handler(self.matching_func, role.name, role2.name)
-                    or match_error_handler(self.matching_func, role2.name, role.name)
-                    and duplicate_judge()
-                ):
-                    self.all_roles[role2.get_key()].add_role(role)
+        return self._has_link(name2, [user], self.max_hierarchy_level)
 
-    def delete_link(self, name1, name2, *domain):
-        role1, role2 = two_role_domain_wrapper(self, name1, name2, domain)
+    def _has_link(self, name, roles, level):
+        if level <= 0 or len(roles) == 0:
+            return False
 
-        if not self.has_role(role1) or not self.has_role(role2):
-            raise RuntimeError("error: name1 or name2 does not exist")
+        next_roles = set()
+        for role in roles:
+            if name == role.name:
+                return True
+            next_roles.update(set(role.roles))
 
-        role1.delete_role(role2)
+        return self._has_link(name, list(next_roles), level - 1)
 
-    def has_link(self, name1, name2, *domain):
-        if len(domain) > 1:
-            raise RuntimeError("error: domain should be 1 parameter")
-        elif len(domain) == 1:
-            domain = domain[0]
-        else:
-            domain = ""
+    def get_roles(self, name, *domain):
+        user = self._get_role(name)
+        return [r.name for r in user.roles]
 
-        role1, role2 = two_role_domain_wrapper(self, name1, name2, domain)
+    def get_users(self, name, *domain):
+        role = self._get_role(name)
+        return [u.name for u in role.users]
 
-        if role1 == role2:
-            return True
+    def to_string(self):
+        line = []
+        for role in self.all_roles.values():
+            text = role.to_string()
+            if text:
+                line.append(text)
+        return ", ".join(line)
 
-        if not self.has_role(role1) or not self.has_role(role2):
-            return False
+    def print_roles(self):
+        self.logger.info(self.to_string())
 
-        if not self.has_pattern and not self.has_domain_pattern:
-            return role1.has_role(role2, self.max_hierarchy_level, None, None)
 
-        # Here is has_pattern logic.
-        for role in self.all_roles.values():
-            if self.has_domain_pattern:
-                if not self.domain_matching_func(domain, role.domain):
-                    continue
-            else:
-                if role.domain != domain:
-                    continue
-
-            def role_judge():
-                if role.has_role(
-                    role2,
-                    self.max_hierarchy_level,
-                    self.matching_func,
-                    self.domain_matching_func,
-                ):
-                    return True
-                return False
-
-            if self.has_pattern:
-                if self.matching_func(role1.name, role.name):
-                    if role_judge():
-                        return True
-                    continue
-            else:
-                if role1.name == role.name:
-                    if role_judge():
-                        return True
-                    continue
-        return False
+class DomainManagerBase(RM):
+    def __init__(self, max_hierarchy_level=10):
+        self.logger = logging.getLogger(__name__)
+        self.all_links = dict()
+        self.max_hierarchy_level = max_hierarchy_level
+        self.domain_matching_func = lambda domain1, domain2: domain1 == domain2
+        self.matching_func = lambda name1, name2: name1 == name2
 
-    def get_roles(self, name, *domain):
-        """
-        gets the roles that a subject inherits.
-        domain is a prefix to the roles.
-        """
+    def add_matching_func(self, fn):
+        self.matching_func = fn
+
+    def add_domain_matching_func(self, fn=None):
+        self.domain_matching_func = fn
+
+    def _get_domain(self, *domain):
         if len(domain) > 1:
             raise RuntimeError("error: domain should be 1 parameter")
         elif len(domain) == 1:
             domain = domain[0]
         else:
             domain = ""
 
-        role = role_domain_wrapper(self, name, domain)
+        return domain
 
-        if not self.has_role(role):
-            return []
+    def _get_links(self, *domain):
+        domain = self._get_domain(*domain)
 
-        roles = self.create_role(name, domain).get_roles()
+        if domain not in self.all_links:
+            self.all_links[domain] = []
 
-        return roles
+        return self.all_links[domain]
 
-    def get_users(self, name, *domain):
-        """
-        gets the users that inherits a subject.
-        domain is an unreferenced parameter here, may be used in other implementations.
-        """
-        target_role = role_domain_wrapper(self, name, domain)
+    def _get_role_manager(self, *domain):
+        domain1 = self._get_domain(*domain)
+        domain_links = []
 
-        if not self.has_role(target_role):
-            return []
+        for domain2, links in self.all_links.items():
+            if match_error_handler(self.domain_matching_func, domain1, domain2):
+                domain_links = domain_links + links
 
-        roles = []
-        for role in self.all_roles.values():
-            if role.has_direct_role(target_role):
-                roles.append(role.name)
-
-        return roles
-
-    def print_roles(self):
-        line = []
-        for role in self.all_roles.values():
-            text = role.to_string()
-            if text:
-                line.append(text)
-        self.logger.info(", ".join(line))
+        rm = RoleManager(max_hierarchy_level=self.max_hierarchy_level)
+        rm.add_matching_func(self.matching_func)
+        for link in domain_links:
+            rm.add_link(link[0], link[1])
+        return rm
 
+    def clear(self):
+        self.all_links = dict()
 
-class Role:
-    """represents the data structure for a role in RBAC."""
+    def add_link(self, name1, name2, *domain):
+        links = self._get_links(*domain)
+        links.append(Link(name1, name2))
 
-    def __init__(self, name: str, domain: str = ""):
-        self.name = name
-        self.roles = []
-        self.domain = domain
+    def delete_link(self, name1, name2, *domain):
+        links = self._get_links(*domain)
+        if Link(name1, name2) not in links:
+            raise RuntimeError(
+                f"error: link between {name1} and {name2} does not exist"
+            )
+        links.remove(Link(name1, name2))
 
-    def __eq__(self, other: "Role"):
-        return (
-            type(other) == type(self)
-            and self.name == other.name
-            and self.domain == other.domain
-        )
-
-    def __hash__(self):
-        return hash(self.name + "::" + self.domain)
-
-    def get_key(self):
-        if self.domain:
-            return self.domain + "::" + self.name
-        return self.name
-
-    def add_role(self, role: "Role"):
-        if role in self.roles:
-            return
-        self.roles.append(role)
-
-    def delete_role(self, role: "Role"):
-        if role in self.roles:
-            self.roles.remove(role)
-
-    def has_role(
-        self,
-        role: "Role",
-        hierarchy_level: int,
-        matching_func=None,
-        domain_matching_func=None,
-    ):
-
-        if self.has_direct_role(role, matching_func, domain_matching_func):
-            return True
-        if hierarchy_level <= 0:
-            return False
+    def has_link(self, name1, name2, *domain):
+        rm = self._get_role_manager(*domain)
+        return rm.has_link(name1, name2)
 
-        for knownRole in self.roles:
-            if knownRole.has_role(
-                role, hierarchy_level - 1, matching_func, domain_matching_func
-            ):
-                return True
+    def get_roles(self, name, *domain):
+        rm = self._get_role_manager(*domain)
+        return rm.get_roles(name)
 
-        return False
+    def get_users(self, name, *domain):
+        rm = self._get_role_manager(*domain)
+        return rm.get_users(name)
 
-    def has_direct_role(
-        self, role: "Role", matching_func=None, domain_matching_func=None
-    ):
-        for known_role in self.roles:
-            if matching_func:
-                if not matching_func(role.name, known_role.name):
-                    continue
-            else:
-                if not role.name == known_role.name:
-                    continue
-
-            if domain_matching_func:
-                if not domain_matching_func(role.domain, known_role.domain):
-                    continue
-            else:
-                if not role.domain == known_role.domain:
-                    continue
-            return True
-        return False
+    def print_roles(self):
+        pass
 
-    def to_string(self):
-        if len(self.roles) == 0:
-            return ""
 
-        names = ", ".join(self.get_roles())
+class DomainManager(DomainManagerBase):
+    def __init__(self, max_hierarchy_level=10):
+        super().__init__(max_hierarchy_level)
+        self.rm_map = dict()  # type: dict[str, RoleManager]
 
-        if len(self.roles) == 1:
-            return self.name + " < " + names
-        else:
-            return self.name + " < (" + names + ")"
+    def _rebuild(self):
+        self.rm_map = dict()
 
-    def get_roles(self):
-        roles = []
-        for role in self.roles:
-            roles.append(role.name)
+    def _get_role_manager(self, *domain):
+        domain1 = self._get_domain(*domain)
+        if domain1 not in self.rm_map:
+            self.rm_map[domain1] = super()._get_role_manager(*domain)
+
+        return self.rm_map[domain1]
+
+    def _affected_role_managers(self, *domain):
+        domain_pattern = self._get_domain(*domain)
+        return [
+            self.rm_map[domain_str]
+            for domain_str in self.rm_map.keys()
+            if match_error_handler(
+                self.domain_matching_func, domain_str, domain_pattern
+            )
+        ]
+
+    def add_matching_func(self, fn):
+        super().add_matching_func(fn)
+        for rm in self.rm_map.values():
+            rm.add_matching_func(fn)
+
+    def add_domain_matching_func(self, fn):
+        super().add_domain_matching_func(fn)
+        for rm in self.rm_map.values():
+            rm.add_domain_matching_func(fn)
+        self._rebuild()
 
-        return roles
+    def clear(self):
+        super().clear()
+        self.rm_map = dict()
 
+    def add_link(self, name1, name2, *domain):
+        super().add_link(name1, name2, *domain)
+        for rm in self._affected_role_managers(*domain):
+            rm.add_link(name1, name2, *domain)
 
-def role_domain_wrapper(obj, name, domain):
-    if type(domain) != str:
-        if not domain or len(domain) == 0:
-            domain = ""
-        elif len(domain) == 1:
-            domain = domain[0]
-        elif len(domain) > 1:
-            raise RuntimeError("error: domain should be 1 parameter")
+    def delete_link(self, name1, name2, *domain):
+        super().delete_link(name1, name2, *domain)
+        for rm in self._affected_role_managers(*domain):
+            rm.delete_link(name1, name2, *domain)
 
-    role = Role(name, domain)
+    def has_link(self, name1, name2, *domain):
+        return super().has_link(name1, name2, *domain)
 
-    if not obj.has_role(role):
-        return role
-    return obj.create_role(name, domain)
+    def get_roles(self, name, *domain):
+        return super().get_roles(name, *domain)
 
+    def get_users(self, name, *domain):
+        return super().get_users(name, *domain)
 
-def two_role_domain_wrapper(obj, name1, name2, domain):
-    return role_domain_wrapper(obj, name1, domain), role_domain_wrapper(
-        obj, name2, domain
-    )
+    def print_roles(self):
+        for domain, rm in self.rm_map.items():
+            line = rm.to_string()
+            self.logger.info(f"{domain}: {line}")
 
 
 def match_error_handler(fn, key1, key2):
     try:
         return fn(key1, key2)
     except:
         return False
```

### Comparing `casbin-1.9.6/casbin/synced_enforcer.py` & `casbin-1.9.7/casbin/synced_enforcer.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/util/builtin_operators.py` & `casbin-1.9.7/casbin/util/builtin_operators.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/util/expression.py` & `casbin-1.9.7/casbin/util/expression.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/util/rwlock.py` & `casbin-1.9.7/casbin/util/rwlock.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin/util/util.py` & `casbin-1.9.7/casbin/util/util.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/casbin.egg-info/PKG-INFO` & `casbin-1.9.7/casbin.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: casbin
-Version: 1.9.6
+Version: 1.9.7
 Summary: An authorization library that supports access control models like ACL, RBAC, ABAC in Python
 Home-page: https://github.com/casbin/pycasbin
 Author: TechLee
 Author-email: techlee@qq.com
 License: Apache 2.0
 Keywords: casbin,acl,rbac,abac,auth,authz,authorization,access control,permission
 Platform: UNKNOWN
```

### Comparing `casbin-1.9.6/casbin.egg-info/SOURCES.txt` & `casbin-1.9.7/casbin.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/setup.py` & `casbin-1.9.7/setup.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/tests/config/test_config.py` & `casbin-1.9.7/tests/config/test_config.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/tests/model/test_policy.py` & `casbin-1.9.7/tests/model/test_policy.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/tests/rbac/test_role_manager.py` & `casbin-1.9.7/tests/rbac/test_role_manager.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,55 +1,56 @@
 from unittest import TestCase
 from casbin.rbac import default_role_manager
 from casbin.util import regex_match_func
 import time
 from concurrent.futures import ThreadPoolExecutor
+import re
 
 
-def get_role_manager():
-    return default_role_manager.RoleManager(max_hierarchy_level=10)
+class TestRoleManager(TestCase):
+    def get_role_manager(self):
+        return default_role_manager.RoleManager(max_hierarchy_level=10)
 
-
-class TestDefaultRoleManager(TestCase):
     def test_role(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_link("u1", "g1")
         rm.add_link("u2", "g1")
         rm.add_link("u3", "g2")
         rm.add_link("u4", "g2")
         rm.add_link("u4", "g3")
         rm.add_link("g1", "g3")
 
         # Current role inheritance tree:
         #             g3    g2
         #            /  \  /  \
         #          g1    u4    u3
         #         /  \
         #       u1    u2
 
+        self.assertTrue(rm.has_link("u1", "u1"))
         self.assertTrue(rm.has_link("u1", "g1"))
         self.assertFalse(rm.has_link("u1", "g2"))
         self.assertTrue(rm.has_link("u1", "g3"))
         self.assertTrue(rm.has_link("u2", "g1"))
         self.assertFalse(rm.has_link("u2", "g2"))
         self.assertTrue(rm.has_link("u2", "g3"))
         self.assertFalse(rm.has_link("u3", "g1"))
         self.assertTrue(rm.has_link("u3", "g2"))
         self.assertFalse(rm.has_link("u3", "g3"))
         self.assertFalse(rm.has_link("u4", "g1"))
         self.assertTrue(rm.has_link("u4", "g2"))
         self.assertTrue(rm.has_link("u4", "g3"))
 
-        self.assertCountEqual(rm.get_roles("u1"), ["g1"])
-        self.assertCountEqual(rm.get_roles("u2"), ["g1"])
-        self.assertCountEqual(rm.get_roles("u3"), ["g2"])
-        self.assertCountEqual(rm.get_roles("u4"), ["g2", "g3"])
-        self.assertCountEqual(rm.get_roles("g1"), ["g3"])
-        self.assertCountEqual(rm.get_roles("g2"), [])
-        self.assertCountEqual(rm.get_roles("g3"), [])
+        self.assertEqual(rm.get_roles("u1"), ["g1"])
+        self.assertEqual(rm.get_roles("u2"), ["g1"])
+        self.assertEqual(rm.get_roles("u3"), ["g2"])
+        self.assertEqual(sorted(rm.get_roles("u4")), sorted(["g2", "g3"]))
+        self.assertEqual(rm.get_roles("g1"), ["g3"])
+        self.assertEqual(rm.get_roles("g2"), [])
+        self.assertEqual(rm.get_roles("g3"), [])
 
         rm.delete_link("g1", "g3")
         rm.delete_link("u4", "g2")
 
         # Current role inheritance tree after deleting the links:
         #             g3    g2
         #               \     \
@@ -66,60 +67,78 @@
         self.assertFalse(rm.has_link("u3", "g1"))
         self.assertTrue(rm.has_link("u3", "g2"))
         self.assertFalse(rm.has_link("u3", "g3"))
         self.assertFalse(rm.has_link("u4", "g1"))
         self.assertFalse(rm.has_link("u4", "g2"))
         self.assertTrue(rm.has_link("u4", "g3"))
 
-        self.assertCountEqual(rm.get_roles("u1"), ["g1"])
-        self.assertCountEqual(rm.get_roles("u2"), ["g1"])
-        self.assertCountEqual(rm.get_roles("u3"), ["g2"])
-        self.assertCountEqual(rm.get_roles("u4"), ["g3"])
-        self.assertCountEqual(rm.get_roles("g1"), [])
-        self.assertCountEqual(rm.get_roles("g2"), [])
-        self.assertCountEqual(rm.get_roles("g3"), [])
+        self.assertEqual(rm.get_roles("u1"), ["g1"])
+        self.assertEqual(rm.get_roles("u2"), ["g1"])
+        self.assertEqual(rm.get_roles("u3"), ["g2"])
+        self.assertEqual(rm.get_roles("u4"), ["g3"])
+        self.assertEqual(rm.get_roles("g1"), [])
+        self.assertEqual(rm.get_roles("g2"), [])
+        self.assertEqual(rm.get_roles("g3"), [])
 
-    def test_domain_role(self):
-        rm = get_role_manager()
-        rm.add_link("u1", "g1", "domain1")
-        rm.add_link("u2", "g1", "domain1")
-        rm.add_link("u3", "admin", "domain2")
-        rm.add_link("u4", "admin", "domain2")
-        rm.add_link("u4", "admin", "domain1")
-        rm.add_link("g1", "admin", "domain1")
+        rm.clear()
 
-        # Current role inheritance tree:
-        #       domain1:admin    domain2:admin
-        #            /       \  /       \
-        #      domain1:g1     u4         u3
-        #         /  \
-        #       u1    u2
+        match_fn = (
+            lambda name1, name2: True if re.match("^" + name2 + "$", name1) else False
+        )
+
+        rm.add_matching_func(match_fn)
+
+        rm.add_link("u2", r"g\d+")
+        rm.add_link(r"u\d+", "any_user")
+        rm.add_link(r"g\d+", "any_group")
+        rm.add_link("u1", "g1")
 
-        self.assertTrue(rm.has_link("u1", "g1", "domain1"))
-        self.assertFalse(rm.has_link("u1", "g1", "domain2"))
-        self.assertTrue(rm.has_link("u1", "admin", "domain1"))
-        self.assertFalse(rm.has_link("u1", "admin", "domain2"))
+        self.assertTrue(rm.has_link("u1", "g1"))
+        self.assertFalse(rm.has_link("u1", "g2"))
+        self.assertTrue(rm.has_link("u1", "any_user"))
+        self.assertTrue(rm.has_link("u1", "any_group"))
 
-        self.assertTrue(rm.has_link("u2", "g1", "domain1"))
-        self.assertFalse(rm.has_link("u2", "g1", "domain2"))
-        self.assertTrue(rm.has_link("u2", "admin", "domain1"))
-        self.assertFalse(rm.has_link("u2", "admin", "domain2"))
+        self.assertTrue(rm.has_link("u2", "g1"))
+        self.assertTrue(rm.has_link("u2", "g2"))
+        self.assertTrue(rm.has_link("u2", "any_user"))
+        self.assertTrue(rm.has_link("u2", "any_group"))
 
-        self.assertFalse(rm.has_link("u3", "g1", "domain1"))
-        self.assertFalse(rm.has_link("u3", "g1", "domain2"))
-        self.assertFalse(rm.has_link("u3", "admin", "domain1"))
-        self.assertTrue(rm.has_link("u3", "admin", "domain2"))
+        self.assertFalse(rm.has_link("u3", "g1"))
+        self.assertFalse(rm.has_link("u3", "g2"))
+        self.assertTrue(rm.has_link("u3", "any_user"))
+        self.assertFalse(rm.has_link("u3", "any_group"))
 
-        self.assertFalse(rm.has_link("u4", "g1", "domain1"))
-        self.assertFalse(rm.has_link("u4", "g1", "domain2"))
-        self.assertTrue(rm.has_link("u4", "admin", "domain1"))
-        self.assertTrue(rm.has_link("u4", "admin", "domain2"))
+        self.assertTrue(rm.has_link("g1", "any_group"))
+        self.assertTrue(rm.has_link("g2", "any_group"))
+
+        self.assertEqual(sorted(rm.get_roles("u1")), sorted(["g1", "any_user"]))
+        self.assertEqual(
+            sorted(rm.get_roles("u2")), sorted(["g2", "g1", r"g\d+", "any_user"])
+        )
+        self.assertEqual(rm.get_roles(r"u\d+"), ["any_user"])
+        self.assertEqual(rm.get_roles("u3"), ["any_user"])
+        self.assertEqual(rm.get_roles("g1"), ["any_group"])
+        self.assertEqual(rm.get_roles("g2"), ["any_group"])
+
+        rm.delete_link(r"u\d+", "any_user")
+        rm.delete_link(r"g\d+", "any_group")
+        rm.delete_link("u1", "g1")
+        rm.add_link("u1", "g2")
+
+        self.assertEqual(rm.get_roles("u1"), ["g2"])
+
+        rm.clear()
+
+        rm.add_link("alice", "location_1/department_1")
+        rm.add_link("location_1/.*", "all_departments")
+
+        self.assertFalse(rm.has_link("alice", "location_1/department_2"))
 
     def test_clear(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_link("u1", "g1")
         rm.add_link("u2", "g1")
         rm.add_link("u3", "g2")
         rm.add_link("u4", "g2")
         rm.add_link("u4", "g3")
         rm.add_link("g1", "g3")
 
@@ -145,15 +164,15 @@
         self.assertFalse(rm.has_link("u3", "g2"))
         self.assertFalse(rm.has_link("u3", "g3"))
         self.assertFalse(rm.has_link("u4", "g1"))
         self.assertFalse(rm.has_link("u4", "g2"))
         self.assertFalse(rm.has_link("u4", "g3"))
 
     def test_matching_func(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_matching_func(regex_match_func)
 
         rm.add_link("u1", "g1")
         rm.add_link("u3", "g2")
         rm.add_link("u3", "g3")
         rm.add_link(r"u\d+", "g2")
 
@@ -166,35 +185,35 @@
         self.assertFalse(rm.has_link("u2", "g3"))
 
         self.assertFalse(rm.has_link("u3", "g1"))
         self.assertTrue(rm.has_link("u3", "g2"))
         self.assertTrue(rm.has_link("u3", "g3"))
 
     def test_one_to_many(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_matching_func(regex_match_func)
 
         rm.add_link("u1", r"g\d+")
         self.assertTrue(rm.has_link("u1", "g1"))
         self.assertTrue(rm.has_link("u1", "g2"))
         self.assertFalse(rm.has_link("u2", "g1"))
         self.assertFalse(rm.has_link("u2", "g2"))
 
     def test_many_to_one(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_matching_func(regex_match_func)
 
         rm.add_link(r"u\d+", "g1")
         self.assertTrue(rm.has_link("u1", "g1"))
         self.assertFalse(rm.has_link("u1", "g2"))
         self.assertTrue(rm.has_link("u2", "g1"))
         self.assertFalse(rm.has_link("u2", "g2"))
 
     def test_matching_func_order(self):
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_matching_func(regex_match_func)
 
         rm.add_link(r"g\d+", "root")
         rm.add_link("u1", "g1")
         self.assertTrue(rm.has_link("u1", "root"))
 
         rm.clear()
@@ -216,18 +235,73 @@
         self.assertTrue(rm.has_link("u1", "root"))
 
     def test_concurrent_has_link_with_matching_func(self):
         def matching_func(*args):
             time.sleep(0.01)
             return regex_match_func(*args)
 
-        rm = get_role_manager()
+        rm = self.get_role_manager()
         rm.add_matching_func(matching_func)
         rm.add_link(r"u\d+", "users")
 
         def test_has_link(role):
             return rm.has_link(role, "users")
 
         executor = ThreadPoolExecutor(10)
         futures = [executor.submit(test_has_link, "u" + str(i)) for i in range(10)]
         for future in futures:
             self.assertTrue(future.result())
+
+
+class TestDomainManager(TestRoleManager):
+    def get_role_manager(self):
+        return default_role_manager.DomainManager(max_hierarchy_level=10)
+
+    def test_domain_role(self):
+        rm = self.get_role_manager()
+        rm.add_link("u1", "g1", "domain1")
+        rm.add_link("u2", "g1", "domain1")
+        rm.add_link("u3", "admin", "domain2")
+        rm.add_link("u4", "admin", "domain2")
+        rm.add_link("u4", "admin", "domain1")
+        rm.add_link("g1", "admin", "domain1")
+
+        # Current role inheritance tree:
+        #       domain1:admin    domain2:admin
+        #            /       \  /       \
+        #      domain1:g1     u4         u3
+        #         /  \
+        #       u1    u2
+
+        self.assertTrue(rm.has_link("u1", "g1", "domain1"))
+        self.assertFalse(rm.has_link("u1", "g1", "domain2"))
+        self.assertTrue(rm.has_link("u1", "admin", "domain1"))
+        self.assertFalse(rm.has_link("u1", "admin", "domain2"))
+
+        self.assertTrue(rm.has_link("u2", "g1", "domain1"))
+        self.assertFalse(rm.has_link("u2", "g1", "domain2"))
+        self.assertTrue(rm.has_link("u2", "admin", "domain1"))
+        self.assertFalse(rm.has_link("u2", "admin", "domain2"))
+
+        self.assertFalse(rm.has_link("u3", "g1", "domain1"))
+        self.assertFalse(rm.has_link("u3", "g1", "domain2"))
+        self.assertFalse(rm.has_link("u3", "admin", "domain1"))
+        self.assertTrue(rm.has_link("u3", "admin", "domain2"))
+
+        self.assertFalse(rm.has_link("u4", "g1", "domain1"))
+        self.assertFalse(rm.has_link("u4", "g1", "domain2"))
+        self.assertTrue(rm.has_link("u4", "admin", "domain1"))
+        self.assertTrue(rm.has_link("u4", "admin", "domain2"))
+
+        rm.clear()
+        match_fn = (
+            lambda name1, name2: True if re.match("^" + name2 + "$", name1) else False
+        )
+
+        rm.add_domain_matching_func(match_fn)
+        rm.add_link("alice", "user", ".*")
+        rm.add_link("user", "users", "domain1")
+
+        self.assertTrue(rm.has_link("alice", "user", "domain1"))
+        self.assertTrue(rm.has_link("alice", "users", "domain1"))
+        self.assertTrue(rm.has_link("alice", "user", "domain2"))
+        self.assertFalse(rm.has_link("alice", "users", "domain2"))
```

### Comparing `casbin-1.9.6/tests/util/test_builtin_operators.py` & `casbin-1.9.7/tests/util/test_builtin_operators.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/tests/util/test_rwlock.py` & `casbin-1.9.7/tests/util/test_rwlock.py`

 * *Files identical despite different names*

### Comparing `casbin-1.9.6/tests/util/test_util.py` & `casbin-1.9.7/tests/util/test_util.py`

 * *Files identical despite different names*

