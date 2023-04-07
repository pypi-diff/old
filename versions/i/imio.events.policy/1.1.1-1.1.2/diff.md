# Comparing `tmp/imio.events.policy-1.1.1.tar.gz` & `tmp/imio.events.policy-1.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/imio.events.policy-1.1.1.tar", last modified: Thu Jan 12 09:06:26 2023, max compression
+gzip compressed data, was "imio.events.policy-1.1.2.tar", last modified: Fri Apr  7 14:35:22 2023, max compression
```

## Comparing `imio.events.policy-1.1.1.tar` & `imio.events.policy-1.1.2.tar`

### file list

```diff
@@ -1,74 +1,75 @@
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/docs/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7994 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/docs/conf.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       81 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/docs/index.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      520 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/DEVELOP.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     4689 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/PKG-INFO
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/CONTRIBUTORS.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2009 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/README.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      567 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/CHANGES.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       61 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/MANIFEST.in
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2618 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/setup.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      669 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/LICENSE.rst
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      518 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/setup.cfg
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        5 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/top_level.txt
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     4689 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/PKG-INFO
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/dependency_links.txt
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      373 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/requires.txt
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       17 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/namespace_packages.txt
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2197 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/SOURCES.txt
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio.events.policy.egg-info/not-zip-safe
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/__init__.py
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1494 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/testing.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      266 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/interfaces.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1039 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/setuphandlers.py
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/robot/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2003 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/robot/test_example.robot
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/__init__.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2067 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/test_setup.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      949 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/tests/test_robot.py
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/uninstall/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      199 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/uninstall/browserlayer.xml
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      216 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/News_Item.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      215 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Document.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      186 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Plone_site.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      212 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Event.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      355 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Image.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      437 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/File.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      217 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Collection.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      211 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Link.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      213 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/types/Folder.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      634 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/metadata.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      167 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/viewlets.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      179 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/browserlayer.xml
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/registry/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7956 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/registry/autopublishing.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      392 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/registry/events.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      233 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/subscribers.zcml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      198 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/utils.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      260 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/permissions.zcml
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/profiles/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/profiles/1000_to_1001/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7955 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/profiles/1000_to_1001/autopublishing.xml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/__init__.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      956 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/upgrades/configure.zcml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       46 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/__init__.py
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/static/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/static/.gitkeep
-drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/overrides/
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/overrides/.gitkeep
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/__init__.py
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      584 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/browser/configure.zcml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1862 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/events/policy/configure.zcml
--rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-01-12 09:06:26.000000 imio.events.policy-1.1.1/src/imio/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      698 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/CHANGES.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/CONTRIBUTORS.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      520 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/DEVELOP.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)    18092 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/LICENSE.GPL
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      669 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/LICENSE.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       61 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/MANIFEST.in
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     3805 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/PKG-INFO
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2009 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/README.rst
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/docs/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7994 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/docs/conf.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       81 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/docs/index.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      518 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/setup.cfg
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2656 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/setup.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       46 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/browser/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/browser/__init__.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      584 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/browser/configure.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/browser/overrides/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/browser/overrides/.gitkeep
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/browser/static/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/browser/static/.gitkeep
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1913 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/configure.zcml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      266 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/interfaces.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      260 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/permissions.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/profiles/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      179 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/browserlayer.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      706 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/metadata.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/registry/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7956 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/registry/autopublishing.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      392 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/registry/events.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      217 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Collection.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      215 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Document.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      212 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Event.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      437 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/File.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      213 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Folder.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      355 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Image.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      211 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Link.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      216 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/News_Item.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      186 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/types/Plone_site.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      167 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/viewlets.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/profiles/uninstall/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      199 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/profiles/uninstall/browserlayer.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1039 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/setuphandlers.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      233 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/subscribers.zcml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1493 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/testing.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/src/imio/events/policy/tests/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/tests/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/src/imio/events/policy/tests/robot/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2003 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/tests/robot/test_example.robot
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      949 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/tests/test_robot.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2066 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/tests/test_setup.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/__init__.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      956 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/configure.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/profiles/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.127612 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/profiles/1000_to_1001/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7955 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/upgrades/profiles/1000_to_1001/autopublishing.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      198 2023-04-07 14:35:21.000000 imio.events.policy-1.1.2/src/imio/events/policy/utils.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:35:22.123612 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     3805 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/PKG-INFO
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2209 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/SOURCES.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/dependency_links.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       17 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/namespace_packages.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/not-zip-safe
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      400 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/requires.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        5 2023-04-07 14:35:22.000000 imio.events.policy-1.1.2/src/imio.events.policy.egg-info/top_level.txt
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `imio.events.policy-1.1.1/docs/conf.py` & `imio.events.policy-1.1.2/docs/conf.py`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/DEVELOP.rst` & `imio.events.policy-1.1.2/DEVELOP.rst`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/README.rst` & `imio.events.policy-1.1.2/README.rst`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/CHANGES.rst` & `imio.events.policy-1.1.2/CHANGES.rst`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,21 @@
 Changelog
 =========
 
 
+1.1.2 (2023-04-07)
+------------------
+
+- Add module : collective.messagesviewlet
+  [boulch]
+
+- Migrate to Plone 6.0.2
+  [boulch]
+
+
 1.1.1 (2023-01-12)
 ------------------
 
 - Install and configure autopublishing (with 15 min tick subscriber)
   [boulch]
 
 - Remove obsolete TinyMCE override
```

### Comparing `imio.events.policy-1.1.1/setup.py` & `imio.events.policy-1.1.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,15 +12,15 @@
         open("CHANGES.rst").read(),
     ]
 )
 
 
 setup(
     name="imio.events.policy",
-    version="1.1.1",
+    version="1.1.2",
     description="Policies to setup imio.events",
     long_description=long_description,
     # Get more from https://pypi.org/classifiers/
     classifiers=[
         "Environment :: Web Environment",
         "Framework :: Plone",
         "Framework :: Plone :: Addon",
@@ -54,14 +54,15 @@
         "z3c.jbot",
         "plone.api>=1.8.4",
         "plone.restapi",
         "plone.app.dexterity",
         "collective.autopublishing",
         "collective.big.bang",
         "collective.js.jqueryui",  # TODO : plone6 : remove
+        "collective.messagesviewlet",
         "collective.solr",
         "collective.z3cform.select2",
         "eea.facetednavigation",
         "pas.plugins.imio",
         "imio.gdpr",
         "imio.events.core",
         "imio.smartweb.locales",
```

### Comparing `imio.events.policy-1.1.1/LICENSE.rst` & `imio.events.policy-1.1.2/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/setup.cfg` & `imio.events.policy-1.1.2/setup.cfg`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio.events.policy.egg-info/SOURCES.txt` & `imio.events.policy-1.1.2/src/imio.events.policy.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 CHANGES.rst
 CONTRIBUTORS.rst
 DEVELOP.rst
+LICENSE.GPL
 LICENSE.rst
 MANIFEST.in
 README.rst
 setup.cfg
 setup.py
 docs/conf.py
 docs/index.rst
```

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/testing.py` & `imio.events.policy-1.1.2/src/imio/events/policy/testing.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,14 @@
 )
 from plone.testing import z2
 
 import imio.events.policy
 
 
 class ImioEventsPolicyLayer(PloneSandboxLayer):
-
     defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)
 
     def setUpZope(self, app, configurationContext):
         # Load any other ZCML that is required for your tests.
         # The z3c.autoinclude feature is disabled in the Plone fixture base
         # layer.
         import plone.restapi
```

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/setuphandlers.py` & `imio.events.policy-1.1.2/src/imio/events/policy/setuphandlers.py`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/tests/robot/test_example.robot` & `imio.events.policy-1.1.2/src/imio/events/policy/tests/robot/test_example.robot`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/tests/test_setup.py` & `imio.events.policy-1.1.2/src/imio/events/policy/tests/test_setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,14 @@
         from imio.events.policy.interfaces import IImioEventsPolicyLayer
         from plone.browserlayer import utils
 
         self.assertIn(IImioEventsPolicyLayer, utils.registered_layers())
 
 
 class TestUninstall(unittest.TestCase):
-
     layer = IMIO_EVENTS_POLICY_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.installer = get_installer(self.portal, self.layer["request"])
         roles_before = api.user.get_roles(TEST_USER_ID)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
```

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/tests/test_robot.py` & `imio.events.policy-1.1.2/src/imio/events/policy/tests/test_robot.py`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/metadata.xml` & `imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/metadata.xml`

 * *Files 14% similar despite different names*

#### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/metadata.xml` & `imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/metadata.xml`

```diff
@@ -2,13 +2,14 @@
 <metadata>
   <version>1001</version>
   <dependencies>
     <dependency>profile-plone.app.contenttypes:plone-content</dependency>
     <dependency>profile-plone.restapi:default</dependency>
     <dependency>profile-pas.plugins.imio:default</dependency>
     <dependency>profile-collective.autopublishing:default</dependency>
+    <dependency>profile-collective.messagesviewlet:default</dependency>
     <dependency>profile-collective.solr:default</dependency>
     <dependency>profile-eea.facetednavigation:default</dependency>
     <dependency>profile-imio.gdpr:default</dependency>
     <dependency>profile-imio.events.core:default</dependency>
   </dependencies>
 </metadata>
```

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/profiles/default/registry/autopublishing.xml` & `imio.events.policy-1.1.2/src/imio/events/policy/profiles/default/registry/autopublishing.xml`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/upgrades/profiles/1000_to_1001/autopublishing.xml` & `imio.events.policy-1.1.2/src/imio/events/policy/upgrades/profiles/1000_to_1001/autopublishing.xml`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/upgrades/configure.zcml` & `imio.events.policy-1.1.2/src/imio/events/policy/upgrades/configure.zcml`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/browser/configure.zcml` & `imio.events.policy-1.1.2/src/imio/events/policy/browser/configure.zcml`

 * *Files identical despite different names*

### Comparing `imio.events.policy-1.1.1/src/imio/events/policy/configure.zcml` & `imio.events.policy-1.1.2/src/imio/events/policy/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -9,14 +9,15 @@
   <include package="imio.smartweb.locales" />
   <include package="imio.events.core" />
 
   <include package="plone.restapi" />
   <include package="collective.autopublishing" />
   <include package="collective.big.bang" />
   <include package="collective.js.jqueryui" />
+  <include package="collective.messagesviewlet" />
   <include package="collective.solr" />
   <include package="collective.z3cform.select2.widget" file="adapters.zcml" />
   <include package="eea.facetednavigation" />
   <include package="pas.plugins.imio" />
   <include package="imio.gdpr" />
 
   <include file="permissions.zcml" />
```

