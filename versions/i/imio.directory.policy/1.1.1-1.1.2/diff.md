# Comparing `tmp/imio.directory.policy-1.1.1.tar.gz` & `tmp/imio.directory.policy-1.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/imio.directory.policy-1.1.1.tar", last modified: Thu Jan 12 09:11:47 2023, max compression
+gzip compressed data, was "imio.directory.policy-1.1.2.tar", last modified: Fri Apr  7 14:37:49 2023, max compression
```

## Comparing `imio.directory.policy-1.1.1.tar` & `imio.directory.policy-1.1.2.tar`

### file list

```diff
@@ -1,79 +1,79 @@
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/
--rw-r--r--   0 laurent    (501) staff       (20)      578 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/CHANGES.rst
--rw-r--r--   0 laurent    (501) staff       (20)       80 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/CONTRIBUTORS.rst
--rw-r--r--   0 laurent    (501) staff       (20)      520 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/DEVELOP.rst
--rw-r--r--   0 laurent    (501) staff       (20)    18092 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/LICENSE.GPL
--rw-r--r--   0 laurent    (501) staff       (20)      672 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/LICENSE.rst
--rw-r--r--   0 laurent    (501) staff       (20)       61 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/MANIFEST.in
--rw-r--r--   0 laurent    (501) staff       (20)     3754 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/PKG-INFO
--rw-r--r--   0 laurent    (501) staff       (20)     2060 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/README.rst
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/docs/
--rw-r--r--   0 laurent    (501) staff       (20)     8000 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/docs/conf.py
--rw-r--r--   0 laurent    (501) staff       (20)       84 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/docs/index.rst
--rw-r--r--   0 laurent    (501) staff       (20)      518 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/setup.cfg
--rw-r--r--   0 laurent    (501) staff       (20)     2623 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/setup.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/
--rw-r--r--   0 laurent    (501) staff       (20)       80 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/__init__.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/
--rw-r--r--   0 laurent    (501) staff       (20)       80 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/__init__.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/
--rw-r--r--   0 laurent    (501) staff       (20)       46 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/__init__.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/
--rw-r--r--   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/__init__.py
--rw-r--r--   0 laurent    (501) staff       (20)      593 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/configure.zcml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/overrides/
--rw-r--r--   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/overrides/.gitkeep
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/static/
--rw-r--r--   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/browser/static/.gitkeep
--rw-r--r--   0 laurent    (501) staff       (20)     1716 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/configure.zcml
--rw-r--r--   0 laurent    (501) staff       (20)      269 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/interfaces.py
--rw-r--r--   0 laurent    (501) staff       (20)      260 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/permissions.zcml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/
--rw-r--r--   0 laurent    (501) staff       (20)      188 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/browserlayer.xml
--rw-r--r--   0 laurent    (501) staff       (20)      637 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/metadata.xml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/registry/
--rw-r--r--   0 laurent    (501) staff       (20)     7796 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/registry/autopublishing.xml
--rw-r--r--   0 laurent    (501) staff       (20)      392 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/registry/direcotry.xml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/
--rw-r--r--   0 laurent    (501) staff       (20)      217 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Collection.xml
--rw-r--r--   0 laurent    (501) staff       (20)      215 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Document.xml
--rw-r--r--   0 laurent    (501) staff       (20)      212 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Event.xml
--rw-r--r--   0 laurent    (501) staff       (20)      437 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/File.xml
--rw-r--r--   0 laurent    (501) staff       (20)      213 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Folder.xml
--rw-r--r--   0 laurent    (501) staff       (20)      355 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Image.xml
--rw-r--r--   0 laurent    (501) staff       (20)      211 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Link.xml
--rw-r--r--   0 laurent    (501) staff       (20)      216 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/News_Item.xml
--rw-r--r--   0 laurent    (501) staff       (20)      186 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/types/Plone_Site.xml
--rw-r--r--   0 laurent    (501) staff       (20)      167 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/viewlets.xml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/uninstall/
--rw-r--r--   0 laurent    (501) staff       (20)      208 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/uninstall/browserlayer.xml
--rw-r--r--   0 laurent    (501) staff       (20)     1054 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/setuphandlers.py
--rw-r--r--   0 laurent    (501) staff       (20)      234 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/subscribers.zcml
--rw-r--r--   0 laurent    (501) staff       (20)     1539 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/testing.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/
--rw-r--r--   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/__init__.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/robot/
--rw-r--r--   0 laurent    (501) staff       (20)     2015 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/robot/test_example.robot
--rw-r--r--   0 laurent    (501) staff       (20)      958 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/test_robot.py
--rw-r--r--   0 laurent    (501) staff       (20)     2121 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/tests/test_setup.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/
--rw-r--r--   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/__init__.py
--rw-r--r--   0 laurent    (501) staff       (20)     1946 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/configure.zcml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1000_to_1001/
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1000_to_1001/registry/
--rw-r--r--   0 laurent    (501) staff       (20)      332 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1000_to_1001/registry/bundles.xml
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1002_to_1003/
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:47.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/
--rw-r--r--   0 laurent    (501) staff       (20)     7796 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/autopublishing.xml
--rw-r--r--   0 laurent    (501) staff       (20)      198 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio/directory/policy/utils.py
-drwxr-xr-x   0 laurent    (501) staff       (20)        0 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/
--rw-r--r--   0 laurent    (501) staff       (20)     3754 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/PKG-INFO
--rw-r--r--   0 laurent    (501) staff       (20)     2425 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/SOURCES.txt
--rw-r--r--   0 laurent    (501) staff       (20)        1 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/dependency_links.txt
--rw-r--r--   0 laurent    (501) staff       (20)       20 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/namespace_packages.txt
--rw-r--r--   0 laurent    (501) staff       (20)        1 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/not-zip-safe
--rw-r--r--   0 laurent    (501) staff       (20)      376 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/requires.txt
--rw-r--r--   0 laurent    (501) staff       (20)        5 2023-01-12 09:11:46.000000 imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/top_level.txt
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      709 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/CHANGES.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/CONTRIBUTORS.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      520 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/DEVELOP.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)    18092 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/LICENSE.GPL
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      672 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/LICENSE.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       61 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/MANIFEST.in
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     3885 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/PKG-INFO
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2060 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/README.rst
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.932029 imio.directory.policy-1.1.2/docs/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     8000 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/docs/conf.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       84 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/docs/index.rst
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      518 2023-04-07 14:37:49.952029 imio.directory.policy-1.1.2/setup.cfg
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2661 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/setup.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.872029 imio.directory.policy-1.1.2/src/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.932029 imio.directory.policy-1.1.2/src/imio/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.936029 imio.directory.policy-1.1.2/src/imio/directory/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       80 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       46 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/__init__.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      593 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/configure.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/overrides/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/overrides/.gitkeep
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/static/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/browser/static/.gitkeep
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1767 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/configure.zcml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      269 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/interfaces.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      260 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/permissions.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.872029 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      188 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/browserlayer.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      709 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/metadata.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.940029 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/registry/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7796 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/registry/autopublishing.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      392 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/registry/direcotry.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.944029 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      217 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Collection.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      215 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Document.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      212 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Event.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      437 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/File.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      213 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Folder.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      355 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Image.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      211 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Link.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      216 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/News_Item.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      186 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/types/Plone_Site.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      167 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/viewlets.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.944029 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/uninstall/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      208 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/uninstall/browserlayer.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1054 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/setuphandlers.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      234 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/subscribers.zcml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1538 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/testing.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.944029 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/__init__.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/robot/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2015 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/robot/test_example.robot
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      958 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/test_robot.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2120 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/tests/test_setup.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/__init__.py
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     1946 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/configure.zcml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.928029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.872029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1000_to_1001/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1000_to_1001/registry/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      332 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1000_to_1001/registry/bundles.xml
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.928029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1002_to_1003/
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.948029 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     7796 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/autopublishing.xml
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      198 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio/directory/policy/utils.py
+drwxrwxr-x   0 cboulanger  (1000) cboulanger  (1000)        0 2023-04-07 14:37:49.936029 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     3885 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/PKG-INFO
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)     2425 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/SOURCES.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/dependency_links.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)       20 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/namespace_packages.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        1 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/not-zip-safe
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)      403 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/requires.txt
+-rw-rw-r--   0 cboulanger  (1000) cboulanger  (1000)        5 2023-04-07 14:37:49.000000 imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/top_level.txt
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `imio.directory.policy-1.1.1/CHANGES.rst` & `imio.directory.policy-1.1.2/CHANGES.rst`

 * *Files 18% similar despite different names*

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

### Comparing `imio.directory.policy-1.1.1/DEVELOP.rst` & `imio.directory.policy-1.1.2/DEVELOP.rst`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/LICENSE.GPL` & `imio.directory.policy-1.1.2/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/LICENSE.rst` & `imio.directory.policy-1.1.2/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/PKG-INFO` & `imio.directory.policy-1.1.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: imio.directory.policy
-Version: 1.1.1
+Version: 1.1.2
 Summary: Policies to setup imio.directory
 Home-page: https://github.com/imio/imio.directory.policy
 Author: Christophe Boulanger
 Author-email: christophe.boulanger@imio.be
 License: GPL version 2
 Project-URL: PyPI, https://pypi.python.org/pypi/imio.directory.policy
 Project-URL: Source, https://github.com/imio/imio.directory.policy
@@ -119,14 +119,24 @@
 - Christophe Boulanger, christophe.boulanger@imio.be
 
 
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

### Comparing `imio.directory.policy-1.1.1/README.rst` & `imio.directory.policy-1.1.2/README.rst`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/docs/conf.py` & `imio.directory.policy-1.1.2/docs/conf.py`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/setup.cfg` & `imio.directory.policy-1.1.2/setup.cfg`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/setup.py` & `imio.directory.policy-1.1.2/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,15 +12,15 @@
         open("CHANGES.rst").read(),
     ]
 )
 
 
 setup(
     name="imio.directory.policy",
-    version="1.1.1",
+    version="1.1.2",
     description="Policies to setup imio.directory",
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
         "imio.directory.core",
         "imio.smartweb.locales",
```

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/browser/configure.zcml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/browser/configure.zcml`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/configure.zcml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -9,14 +9,15 @@
   <include package="imio.smartweb.locales" />
   <include package="imio.directory.core" />
 
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

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/metadata.xml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/metadata.xml`

 * *Files 23% similar despite different names*

#### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/metadata.xml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/metadata.xml`

```diff
@@ -2,13 +2,14 @@
 <metadata>
   <version>1003</version>
   <dependencies>
     <dependency>profile-plone.app.contenttypes:plone-content</dependency>
     <dependency>profile-plone.restapi:default</dependency>
     <dependency>profile-pas.plugins.imio:default</dependency>
     <dependency>profile-collective.autopublishing:default</dependency>
+    <dependency>profile-collective.messagesviewlet:default</dependency>
     <dependency>profile-collective.solr:default</dependency>
     <dependency>profile-eea.facetednavigation:default</dependency>
     <dependency>profile-imio.gdpr:default</dependency>
     <dependency>profile-imio.directory.core:default</dependency>
   </dependencies>
 </metadata>
```

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/profiles/default/registry/autopublishing.xml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/profiles/default/registry/autopublishing.xml`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/setuphandlers.py` & `imio.directory.policy-1.1.2/src/imio/directory/policy/setuphandlers.py`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/testing.py` & `imio.directory.policy-1.1.2/src/imio/directory/policy/testing.py`

 * *Files 14% similar despite different names*

```diff
@@ -9,15 +9,14 @@
 )
 from plone.testing import z2
 
 import imio.directory.policy
 
 
 class ImioDirectoryPolicyLayer(PloneSandboxLayer):
-
     defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)
 
     def setUpZope(self, app, configurationContext):
         # Load any other ZCML that is required for your tests.
         # The z3c.autoinclude feature is disabled in the Plone fixture base
         # layer.
         import plone.restapi
```

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/tests/robot/test_example.robot` & `imio.directory.policy-1.1.2/src/imio/directory/policy/tests/robot/test_example.robot`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/tests/test_robot.py` & `imio.directory.policy-1.1.2/src/imio/directory/policy/tests/test_robot.py`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/tests/test_setup.py` & `imio.directory.policy-1.1.2/src/imio/directory/policy/tests/test_setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,14 @@
         from imio.directory.policy.interfaces import IImioDirectoryPolicyLayer
         from plone.browserlayer import utils
 
         self.assertIn(IImioDirectoryPolicyLayer, utils.registered_layers())
 
 
 class TestUninstall(unittest.TestCase):
-
     layer = IMIO_DIRECTORY_POLICY_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.installer = get_installer(self.portal, self.layer["request"])
         roles_before = api.user.get_roles(TEST_USER_ID)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
```

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/configure.zcml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/configure.zcml`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/autopublishing.xml` & `imio.directory.policy-1.1.2/src/imio/directory/policy/upgrades/profiles/1002_to_1003/registry/autopublishing.xml`

 * *Files identical despite different names*

### Comparing `imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/PKG-INFO` & `imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: imio.directory.policy
-Version: 1.1.1
+Version: 1.1.2
 Summary: Policies to setup imio.directory
 Home-page: https://github.com/imio/imio.directory.policy
 Author: Christophe Boulanger
 Author-email: christophe.boulanger@imio.be
 License: GPL version 2
 Project-URL: PyPI, https://pypi.python.org/pypi/imio.directory.policy
 Project-URL: Source, https://github.com/imio/imio.directory.policy
@@ -119,14 +119,24 @@
 - Christophe Boulanger, christophe.boulanger@imio.be
 
 
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

### Comparing `imio.directory.policy-1.1.1/src/imio.directory.policy.egg-info/SOURCES.txt` & `imio.directory.policy-1.1.2/src/imio.directory.policy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

