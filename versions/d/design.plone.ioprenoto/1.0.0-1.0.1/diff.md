# Comparing `tmp/design.plone.ioprenoto-1.0.0.tar.gz` & `tmp/design.plone.ioprenoto-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "design.plone.ioprenoto-1.0.0.tar", last modified: Thu Apr  6 13:00:51 2023, max compression
+gzip compressed data, was "design.plone.ioprenoto-1.0.1.tar", last modified: Thu Apr  6 15:54:42 2023, max compression
```

## Comparing `design.plone.ioprenoto-1.0.0.tar` & `design.plone.ioprenoto-1.0.1.tar`

### file list

```diff
@@ -1,89 +1,89 @@
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.830374 design.plone.ioprenoto-1.0.0/
--rw-r--r--   0 roman      (502) staff       (20)       94 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/CHANGES.rst
--rw-r--r--   0 roman      (502) staff       (20)       58 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/CONTRIBUTORS.rst
--rw-r--r--   0 roman      (502) staff       (20)     1338 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/DEVELOP.rst
--rw-r--r--   0 roman      (502) staff       (20)    18092 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/LICENSE.GPL
--rw-r--r--   0 roman      (502) staff       (20)      662 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/LICENSE.rst
--rw-r--r--   0 roman      (502) staff       (20)      116 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/MANIFEST.in
--rw-r--r--   0 roman      (502) staff       (20)     5138 2023-04-06 13:00:51.830510 design.plone.ioprenoto-1.0.0/PKG-INFO
--rw-r--r--   0 roman      (502) staff       (20)     2849 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/README.rst
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.817599 design.plone.ioprenoto-1.0.0/docs/
--rw-r--r--   0 roman      (502) staff       (20)     7986 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/docs/conf.py
--rw-r--r--   0 roman      (502) staff       (20)       89 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/docs/index.rst
--rw-r--r--   0 roman      (502) staff       (20)      340 2023-04-06 13:00:51.830957 design.plone.ioprenoto-1.0.0/setup.cfg
--rw-r--r--   0 roman      (502) staff       (20)     2736 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/setup.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.812508 design.plone.ioprenoto-1.0.0/src/
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.817852 design.plone.ioprenoto-1.0.0/src/design/
--rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/__init__.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.820301 design.plone.ioprenoto-1.0.0/src/design/plone/
--rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/__init__.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.822084 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/
--rw-r--r--   0 roman      (502) staff       (20)      139 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/__init__.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.823302 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)     1145 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/configure.zcml
--rw-r--r--   0 roman      (502) staff       (20)      471 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/orario_di_apertura.py
--rw-r--r--   0 roman      (502) staff       (20)     1128 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/punto_di_contatto.py
--rw-r--r--   0 roman      (502) staff       (20)     1123 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/uffici_correlati.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.823672 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)      628 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/configure.zcml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.823884 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/overrides/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/overrides/.gitkeep
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.824106 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/static/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/static/.gitkeep
--rw-r--r--   0 roman      (502) staff       (20)     1464 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/configure.zcml
--rw-r--r--   0 roman      (502) staff       (20)      270 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/interfaces.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.825179 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/
--rw-r--r--   0 roman      (502) staff       (20)      611 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/README.rst
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/design.plone.ioprenoto.pot
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.813635 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/en/
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.825406 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/en/LC_MESSAGES/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/en/LC_MESSAGES/design.plone.ioprenoto.po
--rw-r--r--   0 roman      (502) staff       (20)     1760 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/update.py
--rwxr-xr-x   0 roman      (502) staff       (20)      503 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/update.sh
--rw-r--r--   0 roman      (502) staff       (20)      414 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/permissions.zcml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.814222 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.826315 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/
--rw-r--r--   0 roman      (502) staff       (20)      191 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/browserlayer.xml
--rw-r--r--   0 roman      (502) staff       (20)      105 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/catalog.xml
--rw-r--r--   0 roman      (502) staff       (20)      191 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/metadata.xml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.826547 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/registry/
--rw-r--r--   0 roman      (502) staff       (20)      180 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/registry/main.xml
--rw-r--r--   0 roman      (502) staff       (20)      339 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/rolemap.xml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.826769 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/types/
--rw-r--r--   0 roman      (502) staff       (20)      476 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/default/types/PrenotazioniFolder.xml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.826985 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/uninstall/
--rw-r--r--   0 roman      (502) staff       (20)      132 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/profiles/uninstall/browserlayer.xml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.827418 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)      246 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/configure.zcml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.827798 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)      166 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/configure.zcml
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.828662 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/__init__.py
--rw-r--r--   0 roman      (502) staff       (20)      414 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/configure.zcml
--rw-r--r--   0 roman      (502) staff       (20)     1745 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/prenotazioniFolder.py
--rw-r--r--   0 roman      (502) staff       (20)     3329 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/servizio.py
--rw-r--r--   0 roman      (502) staff       (20)      794 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/setuphandlers.py
--rw-r--r--   0 roman      (502) staff       (20)     4058 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/testing.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.829968 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/
--rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/__init__.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.830185 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/robot/
--rw-r--r--   0 roman      (502) staff       (20)     2019 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/robot/test_example.robot
--rw-r--r--   0 roman      (502) staff       (20)      923 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_PrenotazioniFolder_ct.py
--rw-r--r--   0 roman      (502) staff       (20)     2230 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_prenotazioni_folder.py
--rw-r--r--   0 roman      (502) staff       (20)     2809 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_serzvizio.py
--rw-r--r--   0 roman      (502) staff       (20)      961 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_robot.py
--rw-r--r--   0 roman      (502) staff       (20)     2509 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_setup.py
-drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 13:00:51.820025 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/
--rw-r--r--   0 roman      (502) staff       (20)     5138 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/PKG-INFO
--rw-r--r--   0 roman      (502) staff       (20)     3015 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/SOURCES.txt
--rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/dependency_links.txt
--rw-r--r--   0 roman      (502) staff       (20)      147 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/entry_points.txt
--rw-r--r--   0 roman      (502) staff       (20)       20 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/namespace_packages.txt
--rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/not-zip-safe
--rw-r--r--   0 roman      (502) staff       (20)      281 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/requires.txt
--rw-r--r--   0 roman      (502) staff       (20)        7 2023-04-06 13:00:51.000000 design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/top_level.txt
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.736051 design.plone.ioprenoto-1.0.1/
+-rw-r--r--   0 roman      (502) staff       (20)      180 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/CHANGES.rst
+-rw-r--r--   0 roman      (502) staff       (20)       58 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/CONTRIBUTORS.rst
+-rw-r--r--   0 roman      (502) staff       (20)     1338 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/DEVELOP.rst
+-rw-r--r--   0 roman      (502) staff       (20)    18092 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/LICENSE.GPL
+-rw-r--r--   0 roman      (502) staff       (20)      662 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/LICENSE.rst
+-rw-r--r--   0 roman      (502) staff       (20)      116 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/MANIFEST.in
+-rw-r--r--   0 roman      (502) staff       (20)     5182 2023-04-06 15:54:42.736219 design.plone.ioprenoto-1.0.1/PKG-INFO
+-rw-r--r--   0 roman      (502) staff       (20)     2759 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/README.rst
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.721346 design.plone.ioprenoto-1.0.1/docs/
+-rw-r--r--   0 roman      (502) staff       (20)     7986 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/docs/conf.py
+-rw-r--r--   0 roman      (502) staff       (20)       89 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/docs/index.rst
+-rw-r--r--   0 roman      (502) staff       (20)      340 2023-04-06 15:54:42.736756 design.plone.ioprenoto-1.0.1/setup.cfg
+-rw-r--r--   0 roman      (502) staff       (20)     2736 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/setup.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.715663 design.plone.ioprenoto-1.0.1/src/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.721612 design.plone.ioprenoto-1.0.1/src/design/
+-rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.724110 design.plone.ioprenoto-1.0.1/src/design/plone/
+-rw-r--r--   0 roman      (502) staff       (20)       80 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.725775 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/
+-rw-r--r--   0 roman      (502) staff       (20)      139 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.727124 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)     1145 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      471 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/orario_di_apertura.py
+-rw-r--r--   0 roman      (502) staff       (20)     1128 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/punto_di_contatto.py
+-rw-r--r--   0 roman      (502) staff       (20)     1123 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/uffici_correlati.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.727586 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      628 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.727848 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/overrides/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/overrides/.gitkeep
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.728043 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/static/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/static/.gitkeep
+-rw-r--r--   0 roman      (502) staff       (20)     1464 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)      270 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/interfaces.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.729544 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/
+-rw-r--r--   0 roman      (502) staff       (20)      611 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/README.rst
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/design.plone.ioprenoto.pot
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.716891 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/en/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.729877 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/en/LC_MESSAGES/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/en/LC_MESSAGES/design.plone.ioprenoto.po
+-rw-r--r--   0 roman      (502) staff       (20)     1760 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/update.py
+-rwxr-xr-x   0 roman      (502) staff       (20)      503 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/update.sh
+-rw-r--r--   0 roman      (502) staff       (20)      414 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/permissions.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.717558 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.730981 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/
+-rw-r--r--   0 roman      (502) staff       (20)      191 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/browserlayer.xml
+-rw-r--r--   0 roman      (502) staff       (20)      105 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/catalog.xml
+-rw-r--r--   0 roman      (502) staff       (20)      191 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/metadata.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.731252 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/registry/
+-rw-r--r--   0 roman      (502) staff       (20)      180 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/registry/main.xml
+-rw-r--r--   0 roman      (502) staff       (20)      339 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/rolemap.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.731525 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/types/
+-rw-r--r--   0 roman      (502) staff       (20)      476 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/default/types/PrenotazioniFolder.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.731796 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/uninstall/
+-rw-r--r--   0 roman      (502) staff       (20)      132 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/profiles/uninstall/browserlayer.xml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.732280 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      246 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.732760 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      166 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/configure.zcml
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.733829 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/__init__.py
+-rw-r--r--   0 roman      (502) staff       (20)      414 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/configure.zcml
+-rw-r--r--   0 roman      (502) staff       (20)     1745 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/prenotazioniFolder.py
+-rw-r--r--   0 roman      (502) staff       (20)     3329 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/servizio.py
+-rw-r--r--   0 roman      (502) staff       (20)      794 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/setuphandlers.py
+-rw-r--r--   0 roman      (502) staff       (20)     4058 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/testing.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.735467 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/
+-rw-r--r--   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/__init__.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.735805 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/robot/
+-rw-r--r--   0 roman      (502) staff       (20)     2019 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/robot/test_example.robot
+-rw-r--r--   0 roman      (502) staff       (20)      923 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_PrenotazioniFolder_ct.py
+-rw-r--r--   0 roman      (502) staff       (20)     2230 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_prenotazioni_folder.py
+-rw-r--r--   0 roman      (502) staff       (20)     2809 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_serzvizio.py
+-rw-r--r--   0 roman      (502) staff       (20)      961 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_robot.py
+-rw-r--r--   0 roman      (502) staff       (20)     2509 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_setup.py
+drwxr-xr-x   0 roman      (502) staff       (20)        0 2023-04-06 15:54:42.723855 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/
+-rw-r--r--   0 roman      (502) staff       (20)     5182 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/PKG-INFO
+-rw-r--r--   0 roman      (502) staff       (20)     3015 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/SOURCES.txt
+-rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/dependency_links.txt
+-rw-r--r--   0 roman      (502) staff       (20)      147 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/entry_points.txt
+-rw-r--r--   0 roman      (502) staff       (20)       20 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/namespace_packages.txt
+-rw-r--r--   0 roman      (502) staff       (20)        1 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/not-zip-safe
+-rw-r--r--   0 roman      (502) staff       (20)      281 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/requires.txt
+-rw-r--r--   0 roman      (502) staff       (20)        7 2023-04-06 15:54:42.000000 design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/top_level.txt
```

### Comparing `design.plone.ioprenoto-1.0.0/DEVELOP.rst` & `design.plone.ioprenoto-1.0.1/DEVELOP.rst`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/LICENSE.GPL` & `design.plone.ioprenoto-1.0.1/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/LICENSE.rst` & `design.plone.ioprenoto-1.0.1/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/PKG-INFO` & `design.plone.ioprenoto-1.0.1/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,46 +1,45 @@
 Metadata-Version: 2.1
 Name: design.plone.ioprenoto
-Version: 1.0.0
+Version: 1.0.1
 Summary: An add-on for Plone
 Home-page: https://github.com/collective/design.plone.ioprenoto
 Author: RedTurtle
 Author-email: info@redturtle.it
 License: GPL version 2
 Project-URL: PyPI, https://pypi.org/project/design.plone.ioprenoto/
 Project-URL: Source, https://github.com/collective/design.plone.ioprenoto
 Project-URL: Tracker, https://github.com/collective/design.plone.ioprenoto/issues
 Description: .. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
            If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
            This text does not appear on PyPI or github. It is a comment.
         
-        .. image:: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml/badge.svg
-            :target: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml
-        
-        .. image:: https://coveralls.io/repos/github/collective/design.plone.ioprenoto/badge.svg?branch=main
-            :target: https://coveralls.io/github/collective/design.plone.ioprenoto?branch=main
-            :alt: Coveralls
-        
-        .. image:: https://codecov.io/gh/collective/design.plone.ioprenoto/branch/master/graph/badge.svg
-            :target: https://codecov.io/gh/collective/design.plone.ioprenoto
-        
         .. image:: https://img.shields.io/pypi/v/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-            :alt: Latest Version
-        
-        .. image:: https://img.shields.io/pypi/status/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto
-            :alt: Egg Status
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Latest Version
         
-        .. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic   :alt: Supported - Python Versions
+        .. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Supported - Python Versions
+        
+        .. image:: https://img.shields.io/pypi/dm/design.plone.ioprenoto.svg
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Number of PyPI downloads
         
         .. image:: https://img.shields.io/pypi/l/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-            :alt: License
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: License
         
+        .. image:: https://github.com/RedTurtle/design.plone.ioprenoto/actions/workflows/tests.yml/badge.svg
+               :target: https://github.com/RedTurtle/design.plone.ioprenoto/actions
+               :alt: Tests
+        
+        .. image:: https://coveralls.io/repos/github/RedTurtle/design.plone.ioprenoto/badge.svg?branch=master
+               :target: https://coveralls.io/github/RedTurtle/design.plone.ioprenoto?branch=master
+               :alt: Coverage
         
         ======================
         design.plone.ioprenoto
         ======================
         
         This product is designed to integrate `redturtle.prenotazioni` package with `design.plone.ioprenoto`
         
@@ -128,14 +127,21 @@
         - RedTurtle, info@redturtle.it
         
         
         Changelog
         =========
         
         
+        1.0.1 (2023-04-06)
+        ------------------
+        
+        - Fix CI struments configs.
+          [foxtrot-dfm1]
+        
+        
         1.0.0 (2023-04-06)
         ------------------
         
         - Initial release.
           [RedTurtle]
         
 Keywords: Python Plone CMS
```

### Comparing `design.plone.ioprenoto-1.0.0/README.rst` & `design.plone.ioprenoto-1.0.1/README.rst`

 * *Files 14% similar despite different names*

```diff
@@ -1,35 +1,34 @@
 .. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
    If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
    This text does not appear on PyPI or github. It is a comment.
 
-.. image:: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml/badge.svg
-    :target: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml
-
-.. image:: https://coveralls.io/repos/github/collective/design.plone.ioprenoto/badge.svg?branch=main
-    :target: https://coveralls.io/github/collective/design.plone.ioprenoto?branch=main
-    :alt: Coveralls
-
-.. image:: https://codecov.io/gh/collective/design.plone.ioprenoto/branch/master/graph/badge.svg
-    :target: https://codecov.io/gh/collective/design.plone.ioprenoto
-
 .. image:: https://img.shields.io/pypi/v/design.plone.ioprenoto.svg
-    :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-    :alt: Latest Version
-
-.. image:: https://img.shields.io/pypi/status/design.plone.ioprenoto.svg
-    :target: https://pypi.python.org/pypi/design.plone.ioprenoto
-    :alt: Egg Status
+       :target: https://pypi.org/project/design.plone.ioprenoto/
+       :alt: Latest Version
 
-.. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic   :alt: Supported - Python Versions
+.. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic
+       :target: https://pypi.org/project/design.plone.ioprenoto/
+       :alt: Supported - Python Versions
+
+.. image:: https://img.shields.io/pypi/dm/design.plone.ioprenoto.svg
+       :target: https://pypi.org/project/design.plone.ioprenoto/
+       :alt: Number of PyPI downloads
 
 .. image:: https://img.shields.io/pypi/l/design.plone.ioprenoto.svg
-    :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-    :alt: License
+       :target: https://pypi.org/project/design.plone.ioprenoto/
+       :alt: License
 
+.. image:: https://github.com/RedTurtle/design.plone.ioprenoto/actions/workflows/tests.yml/badge.svg
+       :target: https://github.com/RedTurtle/design.plone.ioprenoto/actions
+       :alt: Tests
+
+.. image:: https://coveralls.io/repos/github/RedTurtle/design.plone.ioprenoto/badge.svg?branch=master
+       :target: https://coveralls.io/github/RedTurtle/design.plone.ioprenoto?branch=master
+       :alt: Coverage
 
 ======================
 design.plone.ioprenoto
 ======================
 
 This product is designed to integrate `redturtle.prenotazioni` package with `design.plone.ioprenoto`
```

### Comparing `design.plone.ioprenoto-1.0.0/docs/conf.py` & `design.plone.ioprenoto-1.0.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/setup.py` & `design.plone.ioprenoto-1.0.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,15 +12,15 @@
         open("CHANGES.rst").read(),
     ]
 )
 
 
 setup(
     name="design.plone.ioprenoto",
-    version="1.0.0",
+    version="1.0.1",
     description="An add-on for Plone",
     long_description=long_description,
     # Get more from https://pypi.org/classifiers/
     classifiers=[
         "Environment :: Web Environment",
         "Framework :: Plone",
         "Framework :: Plone :: Addon",
```

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/configure.zcml` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/punto_di_contatto.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/punto_di_contatto.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/behaviors/uffici_correlati.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/behaviors/uffici_correlati.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/browser/configure.zcml` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/browser/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/configure.zcml` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/configure.zcml`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/README.rst` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/README.rst`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/locales/update.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/locales/update.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/prenotazioniFolder.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/prenotazioniFolder.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/restapi/serializers/ovverrides/servizio.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/restapi/serializers/ovverrides/servizio.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/setuphandlers.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/setuphandlers.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/testing.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/testing.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/robot/test_example.robot` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/robot/test_example.robot`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_PrenotazioniFolder_ct.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_PrenotazioniFolder_ct.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_prenotazioni_folder.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_prenotazioni_folder.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_serzvizio.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_restapi_serializers_ovverrides_serzvizio.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_robot.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_robot.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design/plone/ioprenoto/tests/test_setup.py` & `design.plone.ioprenoto-1.0.1/src/design/plone/ioprenoto/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/PKG-INFO` & `design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,46 +1,45 @@
 Metadata-Version: 2.1
 Name: design.plone.ioprenoto
-Version: 1.0.0
+Version: 1.0.1
 Summary: An add-on for Plone
 Home-page: https://github.com/collective/design.plone.ioprenoto
 Author: RedTurtle
 Author-email: info@redturtle.it
 License: GPL version 2
 Project-URL: PyPI, https://pypi.org/project/design.plone.ioprenoto/
 Project-URL: Source, https://github.com/collective/design.plone.ioprenoto
 Project-URL: Tracker, https://github.com/collective/design.plone.ioprenoto/issues
 Description: .. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
            If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
            This text does not appear on PyPI or github. It is a comment.
         
-        .. image:: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml/badge.svg
-            :target: https://github.com/collective/design.plone.ioprenoto/actions/workflows/plone-package.yml
-        
-        .. image:: https://coveralls.io/repos/github/collective/design.plone.ioprenoto/badge.svg?branch=main
-            :target: https://coveralls.io/github/collective/design.plone.ioprenoto?branch=main
-            :alt: Coveralls
-        
-        .. image:: https://codecov.io/gh/collective/design.plone.ioprenoto/branch/master/graph/badge.svg
-            :target: https://codecov.io/gh/collective/design.plone.ioprenoto
-        
         .. image:: https://img.shields.io/pypi/v/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-            :alt: Latest Version
-        
-        .. image:: https://img.shields.io/pypi/status/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto
-            :alt: Egg Status
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Latest Version
         
-        .. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic   :alt: Supported - Python Versions
+        .. image:: https://img.shields.io/pypi/pyversions/design.plone.ioprenoto.svg?style=plastic
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Supported - Python Versions
+        
+        .. image:: https://img.shields.io/pypi/dm/design.plone.ioprenoto.svg
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: Number of PyPI downloads
         
         .. image:: https://img.shields.io/pypi/l/design.plone.ioprenoto.svg
-            :target: https://pypi.python.org/pypi/design.plone.ioprenoto/
-            :alt: License
+               :target: https://pypi.org/project/design.plone.ioprenoto/
+               :alt: License
         
+        .. image:: https://github.com/RedTurtle/design.plone.ioprenoto/actions/workflows/tests.yml/badge.svg
+               :target: https://github.com/RedTurtle/design.plone.ioprenoto/actions
+               :alt: Tests
+        
+        .. image:: https://coveralls.io/repos/github/RedTurtle/design.plone.ioprenoto/badge.svg?branch=master
+               :target: https://coveralls.io/github/RedTurtle/design.plone.ioprenoto?branch=master
+               :alt: Coverage
         
         ======================
         design.plone.ioprenoto
         ======================
         
         This product is designed to integrate `redturtle.prenotazioni` package with `design.plone.ioprenoto`
         
@@ -128,14 +127,21 @@
         - RedTurtle, info@redturtle.it
         
         
         Changelog
         =========
         
         
+        1.0.1 (2023-04-06)
+        ------------------
+        
+        - Fix CI struments configs.
+          [foxtrot-dfm1]
+        
+        
         1.0.0 (2023-04-06)
         ------------------
         
         - Initial release.
           [RedTurtle]
         
 Keywords: Python Plone CMS
```

### Comparing `design.plone.ioprenoto-1.0.0/src/design.plone.ioprenoto.egg-info/SOURCES.txt` & `design.plone.ioprenoto-1.0.1/src/design.plone.ioprenoto.egg-info/SOURCES.txt`

 * *Files identical despite different names*

