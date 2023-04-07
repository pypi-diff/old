# Comparing `tmp/osism-0.9.7.tar.gz` & `tmp/osism-0.9.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "osism-0.9.7.tar", last modified: Sun Feb 26 18:42:02 2023, max compression
+gzip compressed data, was "osism-0.9.8.tar", last modified: Sun Feb 26 20:18:16 2023, max compression
```

## Comparing `osism-0.9.7.tar` & `osism-0.9.8.tar`

### file list

```diff
@@ -1,106 +1,106 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-26 18:41:46.000000 osism-0.9.7/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.207758 osism-0.9.7/.github/
--rw-r--r--   0 runner    (1001) docker     (123)      214 2023-02-26 18:41:46.000000 osism-0.9.7/.github/renovate.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.207758 osism-0.9.7/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-02-26 18:41:46.000000 osism-0.9.7/.github/workflows/build-container-image.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-02-26 18:41:46.000000 osism-0.9.7/.github/workflows/publish.yml
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-02-26 18:41:46.000000 osism-0.9.7/.github/workflows/test-python-setup.yml
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-02-26 18:41:46.000000 osism-0.9.7/.zuul.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-02-26 18:42:02.000000 osism-0.9.7/AUTHORS
--rw-r--r--   0 runner    (1001) docker     (123)       79 2023-02-26 18:42:02.000000 osism-0.9.7/ChangeLog
--rw-r--r--   0 runner    (1001) docker     (123)     3900 2023-02-26 18:41:46.000000 osism-0.9.7/Containerfile
--rw-r--r--   0 runner    (1001) docker     (123)     3900 2023-02-26 18:41:46.000000 osism-0.9.7/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-02-26 18:41:46.000000 osism-0.9.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-02-26 18:42:02.219758 osism-0.9.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      673 2023-02-26 18:41:46.000000 osism-0.9.7/Pipfile
--rw-r--r--   0 runner    (1001) docker     (123)    98794 2023-02-26 18:41:46.000000 osism-0.9.7/Pipfile.lock
--rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-02-26 18:41:46.000000 osism-0.9.7/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.211758 osism-0.9.7/contrib/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.211758 osism-0.9.7/contrib/logs/
--rw-r--r--   0 runner    (1001) docker     (123)     9999 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/logs/baremetal-cleaning.log
--rw-r--r--   0 runner    (1001) docker     (123)     3862 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/logs/baremetal-delete.log
--rw-r--r--   0 runner    (1001) docker     (123)    27343 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/logs/baremetal-inspect.log
--rw-r--r--   0 runner    (1001) docker     (123)      630 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/netbox-state-machine.dot
--rw-r--r--   0 runner    (1001) docker     (123)    80581 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/netbox-state-machine.png
--rw-r--r--   0 runner    (1001) docker     (123)     3105 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/osism.drawio
--rw-r--r--   0 runner    (1001) docker     (123)   101525 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/osism.drawio.png
--rw-r--r--   0 runner    (1001) docker     (123)     1913 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/python-osism.drawio
--rw-r--r--   0 runner    (1001) docker     (123)    53162 2023-02-26 18:41:46.000000 osism-0.9.7/contrib/python-osism.drawio.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.211758 osism-0.9.7/files/
--rwxr-xr-x   0 runner    (1001) docker     (123)      299 2023-02-26 18:41:46.000000 osism-0.9.7/files/change.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      805 2023-02-26 18:41:46.000000 osism-0.9.7/files/cleanup-ansible-collections.sh
--rw-r--r--   0 runner    (1001) docker     (123)      304 2023-02-26 18:41:46.000000 osism-0.9.7/files/clush.conf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.211758 osism-0.9.7/files/import/
--rw-r--r--   0 runner    (1001) docker     (123)    14661 2023-02-26 18:41:46.000000 osism-0.9.7/files/import/main.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      682 2023-02-26 18:41:46.000000 osism-0.9.7/files/run-ansible-console.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.215758 osism-0.9.7/osism/
--rw-r--r--   0 runner    (1001) docker     (123)      302 2023-02-26 18:41:46.000000 osism-0.9.7/osism/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-02-26 18:41:46.000000 osism-0.9.7/osism/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.215758 osism-0.9.7/osism/actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/check_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/deploy_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/diff_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/generate_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)    37048 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/manage_device.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-26 18:41:46.000000 osism-0.9.7/osism/actions/manage_interface.py
--rw-r--r--   0 runner    (1001) docker     (123)     3760 2023-02-26 18:41:46.000000 osism-0.9.7/osism/api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/commands/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7918 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/apply.py
--rw-r--r--   0 runner    (1001) docker     (123)     1632 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/bifrost.py
--rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/compose.py
--rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/console.py
--rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/container.py
--rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/dump.py
--rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/log.py
--rw-r--r--   0 runner    (1001) docker     (123)     1861 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/manage.py
--rw-r--r--   0 runner    (1001) docker     (123)    13386 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/netbox.py
--rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/reconciler.py
--rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/service.py
--rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/status.py
--rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/task.py
--rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3929 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/wait.py
--rw-r--r--   0 runner    (1001) docker     (123)      955 2023-02-26 18:41:46.000000 osism-0.9.7/osism/commands/worker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/core/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 18:41:46.000000 osism-0.9.7/osism/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4696 2023-02-26 18:41:46.000000 osism-0.9.7/osism/core/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-02-26 18:41:46.000000 osism-0.9.7/osism/core/playbooks.py
--rw-r--r--   0 runner    (1001) docker     (123)      547 2023-02-26 18:41:46.000000 osism-0.9.7/osism/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 18:41:46.000000 osism-0.9.7/osism/plugins/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/services/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 18:41:46.000000 osism-0.9.7/osism/services/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6951 2023-02-26 18:41:46.000000 osism-0.9.7/osism/services/listener.py
--rw-r--r--   0 runner    (1001) docker     (123)      553 2023-02-26 18:41:46.000000 osism-0.9.7/osism/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)     6770 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/ansible.py
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/ceph.py
--rw-r--r--   0 runner    (1001) docker     (123)     3701 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/conductor.py
--rw-r--r--   0 runner    (1001) docker     (123)      472 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/kolla.py
--rw-r--r--   0 runner    (1001) docker     (123)     6905 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/netbox.py
--rw-r--r--   0 runner    (1001) docker     (123)     8335 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/openstack.py
--rw-r--r--   0 runner    (1001) docker     (123)     1721 2023-02-26 18:41:46.000000 osism-0.9.7/osism/tasks/reconciler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/osism/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-02-26 18:41:46.000000 osism-0.9.7/osism/utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.215758 osism-0.9.7/osism.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2123 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/pbr.json
--rw-r--r--   0 runner    (1001) docker     (123)      537 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-02-26 18:42:02.000000 osism-0.9.7/osism.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-26 18:41:46.000000 osism-0.9.7/requirements.ansible.txt
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-02-26 18:41:46.000000 osism-0.9.7/requirements.openstack-image-manager.txt
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-26 18:41:46.000000 osism-0.9.7/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      753 2023-02-26 18:41:46.000000 osism-0.9.7/requirements.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 18:42:02.219758 osism-0.9.7/scripts/
--rwxr-xr-x   0 runner    (1001) docker     (123)     1117 2023-02-26 18:41:46.000000 osism-0.9.7/scripts/build.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      594 2023-02-26 18:41:46.000000 osism-0.9.7/scripts/push.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-02-26 18:42:02.223759 osism-0.9.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-02-26 18:41:46.000000 osism-0.9.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.492905 osism-0.9.8/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-26 20:18:06.000000 osism-0.9.8/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/.github/
+-rw-r--r--   0 runner    (1001) docker     (123)      214 2023-02-26 20:18:06.000000 osism-0.9.8/.github/renovate.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-02-26 20:18:06.000000 osism-0.9.8/.github/workflows/build-container-image.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-02-26 20:18:06.000000 osism-0.9.8/.github/workflows/publish.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-02-26 20:18:06.000000 osism-0.9.8/.github/workflows/test-python-setup.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-02-26 20:18:06.000000 osism-0.9.8/.zuul.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-02-26 20:18:16.000000 osism-0.9.8/AUTHORS
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-02-26 20:18:16.000000 osism-0.9.8/ChangeLog
+-rw-r--r--   0 runner    (1001) docker     (123)     3900 2023-02-26 20:18:06.000000 osism-0.9.8/Containerfile
+-rw-r--r--   0 runner    (1001) docker     (123)     3900 2023-02-26 20:18:06.000000 osism-0.9.8/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-02-26 20:18:06.000000 osism-0.9.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-02-26 20:18:16.492905 osism-0.9.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      673 2023-02-26 20:18:06.000000 osism-0.9.8/Pipfile
+-rw-r--r--   0 runner    (1001) docker     (123)    98794 2023-02-26 20:18:06.000000 osism-0.9.8/Pipfile.lock
+-rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-02-26 20:18:06.000000 osism-0.9.8/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/contrib/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/contrib/logs/
+-rw-r--r--   0 runner    (1001) docker     (123)     9999 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/logs/baremetal-cleaning.log
+-rw-r--r--   0 runner    (1001) docker     (123)     3862 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/logs/baremetal-delete.log
+-rw-r--r--   0 runner    (1001) docker     (123)    27343 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/logs/baremetal-inspect.log
+-rw-r--r--   0 runner    (1001) docker     (123)      630 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/netbox-state-machine.dot
+-rw-r--r--   0 runner    (1001) docker     (123)    80581 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/netbox-state-machine.png
+-rw-r--r--   0 runner    (1001) docker     (123)     3105 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/osism.drawio
+-rw-r--r--   0 runner    (1001) docker     (123)   101525 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/osism.drawio.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1913 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/python-osism.drawio
+-rw-r--r--   0 runner    (1001) docker     (123)    53162 2023-02-26 20:18:06.000000 osism-0.9.8/contrib/python-osism.drawio.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/files/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      299 2023-02-26 20:18:06.000000 osism-0.9.8/files/change.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      805 2023-02-26 20:18:06.000000 osism-0.9.8/files/cleanup-ansible-collections.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      304 2023-02-26 20:18:06.000000 osism-0.9.8/files/clush.conf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/files/import/
+-rw-r--r--   0 runner    (1001) docker     (123)    14661 2023-02-26 20:18:06.000000 osism-0.9.8/files/import/main.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      682 2023-02-26 20:18:06.000000 osism-0.9.8/files/run-ansible-console.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.484906 osism-0.9.8/osism/
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-02-26 20:18:06.000000 osism-0.9.8/osism/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-02-26 20:18:06.000000 osism-0.9.8/osism/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism/actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/check_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/deploy_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/diff_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/generate_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37048 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/manage_device.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-26 20:18:06.000000 osism-0.9.8/osism/actions/manage_interface.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3760 2023-02-26 20:18:06.000000 osism-0.9.8/osism/api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism/commands/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7918 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/apply.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1632 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/bifrost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/compose.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/console.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/container.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/dump.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1861 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/manage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13386 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/netbox.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/reconciler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3547 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3929 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/wait.py
+-rw-r--r--   0 runner    (1001) docker     (123)      955 2023-02-26 20:18:06.000000 osism-0.9.8/osism/commands/worker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism/core/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:06.000000 osism-0.9.8/osism/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4696 2023-02-26 20:18:06.000000 osism-0.9.8/osism/core/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-02-26 20:18:06.000000 osism-0.9.8/osism/core/playbooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      547 2023-02-26 20:18:06.000000 osism-0.9.8/osism/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:06.000000 osism-0.9.8/osism/plugins/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism/services/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:06.000000 osism-0.9.8/osism/services/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6951 2023-02-26 20:18:06.000000 osism-0.9.8/osism/services/listener.py
+-rw-r--r--   0 runner    (1001) docker     (123)      553 2023-02-26 20:18:06.000000 osism-0.9.8/osism/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.492905 osism-0.9.8/osism/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)     7088 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/ansible.py
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/ceph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3701 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/conductor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      472 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/kolla.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6905 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/netbox.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8335 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/openstack.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1721 2023-02-26 20:18:06.000000 osism-0.9.8/osism/tasks/reconciler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.492905 osism-0.9.8/osism/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-02-26 20:18:06.000000 osism-0.9.8/osism/utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.488906 osism-0.9.8/osism.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2123 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/pbr.json
+-rw-r--r--   0 runner    (1001) docker     (123)      537 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-02-26 20:18:16.000000 osism-0.9.8/osism.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-26 20:18:06.000000 osism-0.9.8/requirements.ansible.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-02-26 20:18:06.000000 osism-0.9.8/requirements.openstack-image-manager.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-26 20:18:06.000000 osism-0.9.8/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      753 2023-02-26 20:18:06.000000 osism-0.9.8/requirements.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 20:18:16.492905 osism-0.9.8/scripts/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1117 2023-02-26 20:18:06.000000 osism-0.9.8/scripts/build.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      594 2023-02-26 20:18:06.000000 osism-0.9.8/scripts/push.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-02-26 20:18:16.492905 osism-0.9.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-02-26 20:18:06.000000 osism-0.9.8/setup.py
```

### Comparing `osism-0.9.7/.github/workflows/build-container-image.yml` & `osism-0.9.8/.github/workflows/build-container-image.yml`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/.github/workflows/publish.yml` & `osism-0.9.8/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/.github/workflows/test-python-setup.yml` & `osism-0.9.8/.github/workflows/test-python-setup.yml`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/Containerfile` & `osism-0.9.8/Containerfile`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/Dockerfile` & `osism-0.9.8/Dockerfile`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/LICENSE` & `osism-0.9.8/LICENSE`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/PKG-INFO` & `osism-0.9.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: osism
-Version: 0.9.7
+Version: 0.9.8
 Summary: OSISM manager interface
 Home-page: https://github.com/osism/python-osism
 Author: OSISM GmbH
 Author-email: info@osism.tech
 Classifier: Development Status :: 3 - Alpha
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
```

### Comparing `osism-0.9.7/Pipfile` & `osism-0.9.8/Pipfile`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/Pipfile.lock` & `osism-0.9.8/Pipfile.lock`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/README.md` & `osism-0.9.8/README.md`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/logs/baremetal-cleaning.log` & `osism-0.9.8/contrib/logs/baremetal-cleaning.log`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/logs/baremetal-delete.log` & `osism-0.9.8/contrib/logs/baremetal-delete.log`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/logs/baremetal-inspect.log` & `osism-0.9.8/contrib/logs/baremetal-inspect.log`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/netbox-state-machine.dot` & `osism-0.9.8/contrib/netbox-state-machine.dot`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/netbox-state-machine.png` & `osism-0.9.8/contrib/netbox-state-machine.png`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/osism.drawio` & `osism-0.9.8/contrib/osism.drawio`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/osism.drawio.png` & `osism-0.9.8/contrib/osism.drawio.png`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/python-osism.drawio` & `osism-0.9.8/contrib/python-osism.drawio`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/contrib/python-osism.drawio.png` & `osism-0.9.8/contrib/python-osism.drawio.png`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/files/cleanup-ansible-collections.sh` & `osism-0.9.8/files/cleanup-ansible-collections.sh`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/files/import/main.py` & `osism-0.9.8/files/import/main.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/files/run-ansible-console.sh` & `osism-0.9.8/files/run-ansible-console.sh`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/actions/check_configuration.py` & `osism-0.9.8/osism/actions/check_configuration.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/actions/deploy_configuration.py` & `osism-0.9.8/osism/actions/deploy_configuration.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/actions/diff_configuration.py` & `osism-0.9.8/osism/actions/diff_configuration.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/actions/generate_configuration.py` & `osism-0.9.8/osism/actions/generate_configuration.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/actions/manage_device.py` & `osism-0.9.8/osism/actions/manage_device.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/api.py` & `osism-0.9.8/osism/api.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/apply.py` & `osism-0.9.8/osism/commands/apply.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/bifrost.py` & `osism-0.9.8/osism/commands/bifrost.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/compose.py` & `osism-0.9.8/osism/commands/compose.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/console.py` & `osism-0.9.8/osism/commands/console.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/container.py` & `osism-0.9.8/osism/commands/container.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/dump.py` & `osism-0.9.8/osism/commands/dump.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/log.py` & `osism-0.9.8/osism/commands/log.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/manage.py` & `osism-0.9.8/osism/commands/manage.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/netbox.py` & `osism-0.9.8/osism/commands/netbox.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/reconciler.py` & `osism-0.9.8/osism/commands/reconciler.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/service.py` & `osism-0.9.8/osism/commands/service.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/status.py` & `osism-0.9.8/osism/commands/status.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/task.py` & `osism-0.9.8/osism/commands/task.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/validate.py` & `osism-0.9.8/osism/commands/validate.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/wait.py` & `osism-0.9.8/osism/commands/wait.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/commands/worker.py` & `osism-0.9.8/osism/commands/worker.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/core/enums.py` & `osism-0.9.8/osism/core/enums.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/main.py` & `osism-0.9.8/osism/main.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/services/listener.py` & `osism-0.9.8/osism/services/listener.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/settings.py` & `osism-0.9.8/osism/settings.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/tasks/__init__.py` & `osism-0.9.8/osism/tasks/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -39,23 +39,35 @@
 
     redis = Redis(host="redis", port="6379")
 
 
 def run_ansible_in_environment(
     request_id, worker, environment, role, arguments, publish=True
 ):
-    logger.info(f"worker = {worker}, environment = {environment}, role = {role}")
     result = ""
 
     if type(arguments) == list:
         joined_arguments = " ".join(arguments)
     else:
         joined_arguments = arguments
 
-    env = {"ENVIRONMENT": environment}
+    env = {}
+
+    # handle sub environments
+    if "." in environment:
+        sub = environment.split(".")[1]
+        environment = environment.split(".")[0]
+        env["SUB"] = sub
+        logger.info(
+            f"worker = {worker}, environment = {environment}, sub = {sub}, role = {role}"
+        )
+    else:
+        logger.info(f"worker = {worker}, environment = {environment}, role = {role}")
+
+    env["ENVIRONMENT"] = environment
 
     # NOTE: Consider arguments in the future
     lock = Redlock(
         key=f"lock-ansible-{environment}-{role}",
         masters={redis},
         auto_release_time=3600,
     )
```

### Comparing `osism-0.9.7/osism/tasks/ansible.py` & `osism-0.9.8/osism/tasks/ansible.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/tasks/conductor.py` & `osism-0.9.8/osism/tasks/conductor.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/tasks/netbox.py` & `osism-0.9.8/osism/tasks/netbox.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/tasks/openstack.py` & `osism-0.9.8/osism/tasks/openstack.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/tasks/reconciler.py` & `osism-0.9.8/osism/tasks/reconciler.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism/utils/__init__.py` & `osism-0.9.8/osism/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism.egg-info/PKG-INFO` & `osism-0.9.8/osism.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: osism
-Version: 0.9.7
+Version: 0.9.8
 Summary: OSISM manager interface
 Home-page: https://github.com/osism/python-osism
 Author: OSISM GmbH
 Author-email: info@osism.tech
 Classifier: Development Status :: 3 - Alpha
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
```

### Comparing `osism-0.9.7/osism.egg-info/SOURCES.txt` & `osism-0.9.8/osism.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism.egg-info/entry_points.txt` & `osism-0.9.8/osism.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/osism.egg-info/requires.txt` & `osism-0.9.8/osism.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/requirements.yml` & `osism-0.9.8/requirements.yml`

 * *Files 0% similar despite different names*

```diff
@@ -5,15 +5,15 @@
   - name: ansible.posix
     version: 1.5.1
   - name: ansible.utils
     version: 2.9.0
   - name: cloud.common
     version: 2.1.2
   - name: community.crypto
-    version: 2.10.0
+    version: 2.11.0
   - name: community.docker
     version: 3.4.2
   - name: community.general
     version: 6.3.0
   - name: community.grafana
     version: 1.5.4
   - name: community.hashi_vault
```

### Comparing `osism-0.9.7/scripts/build.sh` & `osism-0.9.8/scripts/build.sh`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/scripts/push.sh` & `osism-0.9.8/scripts/push.sh`

 * *Files identical despite different names*

### Comparing `osism-0.9.7/setup.cfg` & `osism-0.9.8/setup.cfg`

 * *Files identical despite different names*

