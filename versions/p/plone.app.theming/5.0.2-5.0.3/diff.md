# Comparing `tmp/plone.app.theming-5.0.2.tar.gz` & `tmp/plone.app.theming-5.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plone.app.theming-5.0.2.tar", last modified: Tue Mar 21 23:13:29 2023, max compression
+gzip compressed data, was "plone.app.theming-5.0.3.tar", last modified: Thu Apr  6 10:34:46 2023, max compression
```

## Comparing `plone.app.theming-5.0.2.tar` & `plone.app.theming-5.0.3.tar`

### file list

```diff
@@ -1,151 +1,151 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.793269 plone.app.theming-5.0.2/
--rw-r--r--   0 maurits    (501) staff       (20)     1019 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/.editorconfig
--rw-r--r--   0 maurits    (501) staff       (20)      199 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/.gitignore
--rw-r--r--   0 maurits    (501) staff       (20)      128 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/.meta.toml
--rw-r--r--   0 maurits    (501) staff       (20)      973 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/.pre-commit-config.yaml
--rw-r--r--   0 maurits    (501) staff       (20)    21163 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/CHANGES.rst
--rw-r--r--   0 maurits    (501) staff       (20)       70 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)      674 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/LICENSE
--rw-r--r--   0 maurits    (501) staff       (20)      172 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)    63287 2023-03-21 23:13:29.793413 plone.app.theming-5.0.2/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)      286 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/README.rst
--rw-r--r--   0 maurits    (501) staff       (20)      536 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/TODO.txt
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.758255 plone.app.theming-5.0.2/docs/
--rw-r--r--   0 maurits    (501) staff       (20)    41101 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/docs/index.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1643 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/pyproject.toml
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.749830 plone.app.theming-5.0.2/resources/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.749924 plone.app.theming-5.0.2/resources/theme/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.760179 plone.app.theming-5.0.2/resources/theme/theme1/
--rw-r--r--   0 maurits    (501) staff       (20)      191 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/manifest.cfg
--rw-r--r--   0 maurits    (501) staff       (20)      153 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/othertheme.html
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.760504 plone.app.theming-5.0.2/resources/theme/theme1/overrides/
--rw-r--r--   0 maurits    (501) staff       (20)      557 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/overrides/plone.app.layout.viewlets.colophon.pt
--rw-r--r--   0 maurits    (501) staff       (20)      885 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/rules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      211 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/theme.html
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.762989 plone.app.theming-5.0.2/resources/theme/theme1/views/
--rw-r--r--   0 maurits    (501) staff       (20)     3947 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/class-view.pt
--rw-r--r--   0 maurits    (501) staff       (20)      124 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/context-view.pt
--rw-r--r--   0 maurits    (501) staff       (20)      121 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/name-view.pt
--rw-r--r--   0 maurits    (501) staff       (20)      127 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/permission-view.pt
--rw-r--r--   0 maurits    (501) staff       (20)      121 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/test-view.pt
--rw-r--r--   0 maurits    (501) staff       (20)      217 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/resources/theme/theme1/views/views.cfg
--rw-r--r--   0 maurits    (501) staff       (20)      217 2023-03-21 23:13:29.793900 plone.app.theming-5.0.2/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)     2360 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/setup.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.750579 plone.app.theming-5.0.2/src/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.763371 plone.app.theming-5.0.2/src/plone/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.767177 plone.app.theming-5.0.2/src/plone/app/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.771667 plone.app.theming-5.0.2/src/plone/app/theming/
--rw-r--r--   0 maurits    (501) staff       (20)      152 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.774301 plone.app.theming-5.0.2/src/plone/app/theming/browser/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     1194 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)    38834 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/controlpanel.pt
--rw-r--r--   0 maurits    (501) staff       (20)    16099 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/controlpanel.py
--rw-r--r--   0 maurits    (501) staff       (20)     1060 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/custom_css.py
--rw-r--r--   0 maurits    (501) staff       (20)      470 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/help.py
--rw-r--r--   0 maurits    (501) staff       (20)      939 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/icon.gif
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.775534 plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/
--rw-r--r--   0 maurits    (501) staff       (20)     1644 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/controlpanel.css
--rw-r--r--   0 maurits    (501) staff       (20)     5536 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/defaultPreview.png
--rwxr-xr-x   0 maurits    (501) staff       (20)     1495 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/preview.png
--rw-r--r--   0 maurits    (501) staff       (20)    40897 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/userguide.rst
--rw-r--r--   0 maurits    (501) staff       (20)      488 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/theme-error.pt
--rw-r--r--   0 maurits    (501) staff       (20)      772 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/browser/themefile.py
--rw-r--r--   0 maurits    (501) staff       (20)     2747 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)      217 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/events.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.776500 plone.app.theming-5.0.2/src/plone/app/theming/exportimport/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/exportimport/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      412 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/exportimport/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     1832 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/exportimport/handler.py
--rw-r--r--   0 maurits    (501) staff       (20)      381 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/header.py
--rw-r--r--   0 maurits    (501) staff       (20)     9484 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/interfaces.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.777884 plone.app.theming-5.0.2/src/plone/app/theming/plugins/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/plugins/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      476 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/plugins/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     1391 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/plugins/hooks.py
--rw-r--r--   0 maurits    (501) staff       (20)     2689 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/plugins/utils.py
--rw-r--r--   0 maurits    (501) staff       (20)     6244 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/policy.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.751841 plone.app.theming-5.0.2/src/plone/app/theming/profiles/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.779112 plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/
--rw-r--r--   0 maurits    (501) staff       (20)      161 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/browserlayer.xml
--rw-r--r--   0 maurits    (501) staff       (20)     1043 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/controlpanel.xml
--rw-r--r--   0 maurits    (501) staff       (20)      187 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/metadata.xml
--rw-r--r--   0 maurits    (501) staff       (20)      132 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/registry.xml
--rw-r--r--   0 maurits    (501) staff       (20)     1136 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/testing.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.785266 plone.app.theming-5.0.2/src/plone/app/theming/tests/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.785843 plone.app.theming-5.0.2/src/plone/app/theming/tests/another-theme/
--rw-r--r--   0 maurits    (501) staff       (20)      608 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/another-theme/manifest.cfg
--rw-r--r--   0 maurits    (501) staff       (20)      213 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/another-theme/rules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      636 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)      242 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/french.html
--rw-r--r--   0 maurits    (501) staff       (20)      156 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/includes.html
--rw-r--r--   0 maurits    (501) staff       (20)      456 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/includes.xml
--rw-r--r--   0 maurits    (501) staff       (20)      438 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/localrules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      119 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/nonascii.html
--rw-r--r--   0 maurits    (501) staff       (20)      342 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/nonascii.xml
--rw-r--r--   0 maurits    (501) staff       (20)      199 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/notheme.pt
--rw-r--r--   0 maurits    (501) staff       (20)      116 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/one.html
--rw-r--r--   0 maurits    (501) staff       (20)      442 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/otherrules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      153 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/othertheme.html
--rw-r--r--   0 maurits    (501) staff       (20)       53 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/package_theme.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1095 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/paramrules.xml
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.788856 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/
--rw-r--r--   0 maurits    (501) staff       (20)      471 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/css-js.xml
--rw-r--r--   0 maurits    (501) staff       (20)      139 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/manifest.cfg
--rw-r--r--   0 maurits    (501) staff       (20)       46 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/nonascii.html
--rw-r--r--   0 maurits    (501) staff       (20)      340 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/nonascii.xml
--rw-r--r--   0 maurits    (501) staff       (20)      153 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/othertheme.html
--rw-r--r--   0 maurits    (501) staff       (20)      632 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/overridesrules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      217 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/overridestheme.html
--rw-r--r--   0 maurits    (501) staff       (20)       17 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/resource.css
--rw-r--r--   0 maurits    (501) staff       (20)       16 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/resource.js
--rw-r--r--   0 maurits    (501) staff       (20)      643 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/rules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      177 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/theme.html
--rw-r--r--   0 maurits    (501) staff       (20)      709 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/rules.xml
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.789422 plone.app.theming-5.0.2/src/plone/app/theming/tests/secondary-theme/
--rw-r--r--   0 maurits    (501) staff       (20)      636 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/secondary-theme/manifest.cfg
--rw-r--r--   0 maurits    (501) staff       (20)      213 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/secondary-theme/rules.xml
--rw-r--r--   0 maurits    (501) staff       (20)     3357 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/test_controlpanel.py
--rw-r--r--   0 maurits    (501) staff       (20)     4183 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/test_exportimport.py
--rw-r--r--   0 maurits    (501) staff       (20)     4937 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/test_policy.py
--rw-r--r--   0 maurits    (501) staff       (20)    29670 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/test_transform.py
--rw-r--r--   0 maurits    (501) staff       (20)    23127 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/test_utils.py
--rw-r--r--   0 maurits    (501) staff       (20)      177 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/theme.html
--rw-r--r--   0 maurits    (501) staff       (20)      116 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/two.html
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.792176 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/
--rw-r--r--   0 maurits    (501) staff       (20)      752 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/default_rules.zip
--rw-r--r--   0 maurits    (501) staff       (20)     1330 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/ignores_dotfiles_resource_forks.zip
--rw-r--r--   0 maurits    (501) staff       (20)     1029 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_default_rules.zip
--rw-r--r--   0 maurits    (501) staff       (20)     1437 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_default_rules_override.zip
--rw-r--r--   0 maurits    (501) staff       (20)      985 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_prefix.zip
--rw-r--r--   0 maurits    (501) staff       (20)     8584 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_preview.zip
--rw-r--r--   0 maurits    (501) staff       (20)      980 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_rules.zip
--rw-r--r--   0 maurits    (501) staff       (20)      890 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/multiple_dir.zip
--rw-r--r--   0 maurits    (501) staff       (20)      540 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/nodir.zip
--rw-r--r--   0 maurits    (501) staff       (20)     2395 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/subdirectories.zip
--rw-r--r--   0 maurits    (501) staff       (20)     1403 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/theme.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.752871 plone.app.theming-5.0.2/src/plone/app/theming/themes/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.793062 plone.app.theming-5.0.2/src/plone/app/theming/themes/template/
--rw-r--r--   0 maurits    (501) staff       (20)      158 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/themes/template/index.html
--rw-r--r--   0 maurits    (501) staff       (20)       29 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/themes/template/manifest.cfg
--rw-r--r--   0 maurits    (501) staff       (20)     1174 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/themes/template/rules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      228 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/themes.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     6679 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/transform.py
--rw-r--r--   0 maurits    (501) staff       (20)     1020 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/traversal.py
--rw-r--r--   0 maurits    (501) staff       (20)      524 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/upgrade.py
--rw-r--r--   0 maurits    (501) staff       (20)    24470 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/utils.py
--rw-r--r--   0 maurits    (501) staff       (20)     1169 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone/app/theming/zmi.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:13:29.766726 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)    63287 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     5142 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/dependency_links.txt
--rw-r--r--   0 maurits    (501) staff       (20)       40 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/entry_points.txt
--rw-r--r--   0 maurits    (501) staff       (20)       16 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)      411 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        6 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/src/plone.app.theming.egg-info/top_level.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1185 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/tox.ini
--rw-r--r--   0 maurits    (501) staff       (20)      264 2023-03-21 23:13:29.000000 plone.app.theming-5.0.2/versions.cfg
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.096963 plone.app.theming-5.0.3/
+-rw-r--r--   0 maurits    (501) staff       (20)     1019 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/.editorconfig
+-rw-r--r--   0 maurits    (501) staff       (20)      199 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/.gitignore
+-rw-r--r--   0 maurits    (501) staff       (20)      128 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/.meta.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      973 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/.pre-commit-config.yaml
+-rw-r--r--   0 maurits    (501) staff       (20)    21272 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       70 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      674 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/LICENSE
+-rw-r--r--   0 maurits    (501) staff       (20)      172 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)    63396 2023-04-06 10:34:46.097101 plone.app.theming-5.0.3/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)      286 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/README.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      536 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/TODO.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.062472 plone.app.theming-5.0.3/docs/
+-rw-r--r--   0 maurits    (501) staff       (20)    41101 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/docs/index.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     1643 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/pyproject.toml
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.054306 plone.app.theming-5.0.3/resources/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.054401 plone.app.theming-5.0.3/resources/theme/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.063532 plone.app.theming-5.0.3/resources/theme/theme1/
+-rw-r--r--   0 maurits    (501) staff       (20)      191 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/manifest.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)      153 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/othertheme.html
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.063879 plone.app.theming-5.0.3/resources/theme/theme1/overrides/
+-rw-r--r--   0 maurits    (501) staff       (20)      557 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/overrides/plone.app.layout.viewlets.colophon.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      885 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/rules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      211 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/theme.html
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.065883 plone.app.theming-5.0.3/resources/theme/theme1/views/
+-rw-r--r--   0 maurits    (501) staff       (20)     3947 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/class-view.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      124 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/context-view.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      121 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/name-view.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      127 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/permission-view.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      121 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/test-view.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/resources/theme/theme1/views/views.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:34:46.097681 plone.app.theming-5.0.3/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     2360 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/setup.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.055051 plone.app.theming-5.0.3/src/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.066306 plone.app.theming-5.0.3/src/plone/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.069259 plone.app.theming-5.0.3/src/plone/app/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.073736 plone.app.theming-5.0.3/src/plone/app/theming/
+-rw-r--r--   0 maurits    (501) staff       (20)      152 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.077596 plone.app.theming-5.0.3/src/plone/app/theming/browser/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1194 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)    38831 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/controlpanel.pt
+-rw-r--r--   0 maurits    (501) staff       (20)    16099 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/controlpanel.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1060 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/custom_css.py
+-rw-r--r--   0 maurits    (501) staff       (20)      470 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/help.py
+-rw-r--r--   0 maurits    (501) staff       (20)      939 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/icon.gif
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.079047 plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/
+-rw-r--r--   0 maurits    (501) staff       (20)     1644 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/controlpanel.css
+-rw-r--r--   0 maurits    (501) staff       (20)     5536 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/defaultPreview.png
+-rwxr-xr-x   0 maurits    (501) staff       (20)     1495 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/preview.png
+-rw-r--r--   0 maurits    (501) staff       (20)    40897 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/userguide.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      488 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/theme-error.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      772 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/browser/themefile.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2747 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/events.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.080145 plone.app.theming-5.0.3/src/plone/app/theming/exportimport/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/exportimport/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      412 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/exportimport/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     1832 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/exportimport/handler.py
+-rw-r--r--   0 maurits    (501) staff       (20)      381 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/header.py
+-rw-r--r--   0 maurits    (501) staff       (20)     9484 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/interfaces.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.081251 plone.app.theming-5.0.3/src/plone/app/theming/plugins/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/plugins/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      476 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/plugins/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     1391 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/plugins/hooks.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2689 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/plugins/utils.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6244 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/policy.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.056140 plone.app.theming-5.0.3/src/plone/app/theming/profiles/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.082852 plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/
+-rw-r--r--   0 maurits    (501) staff       (20)      161 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/browserlayer.xml
+-rw-r--r--   0 maurits    (501) staff       (20)     1043 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/controlpanel.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      187 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/metadata.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      132 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/registry.xml
+-rw-r--r--   0 maurits    (501) staff       (20)     1136 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/testing.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.089463 plone.app.theming-5.0.3/src/plone/app/theming/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.090082 plone.app.theming-5.0.3/src/plone/app/theming/tests/another-theme/
+-rw-r--r--   0 maurits    (501) staff       (20)      608 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/another-theme/manifest.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)      213 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/another-theme/rules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      636 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      242 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/french.html
+-rw-r--r--   0 maurits    (501) staff       (20)      156 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/includes.html
+-rw-r--r--   0 maurits    (501) staff       (20)      456 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/includes.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      438 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/localrules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      119 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/nonascii.html
+-rw-r--r--   0 maurits    (501) staff       (20)      342 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/nonascii.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      199 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/notheme.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      116 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/one.html
+-rw-r--r--   0 maurits    (501) staff       (20)      442 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/otherrules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      153 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/othertheme.html
+-rw-r--r--   0 maurits    (501) staff       (20)       53 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/package_theme.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1095 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/paramrules.xml
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.093037 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/
+-rw-r--r--   0 maurits    (501) staff       (20)      471 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/css-js.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      139 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/manifest.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)       46 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/nonascii.html
+-rw-r--r--   0 maurits    (501) staff       (20)      340 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/nonascii.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      153 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/othertheme.html
+-rw-r--r--   0 maurits    (501) staff       (20)      632 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/overridesrules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/overridestheme.html
+-rw-r--r--   0 maurits    (501) staff       (20)       17 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/resource.css
+-rw-r--r--   0 maurits    (501) staff       (20)       16 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/resource.js
+-rw-r--r--   0 maurits    (501) staff       (20)      643 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/rules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      177 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/theme.html
+-rw-r--r--   0 maurits    (501) staff       (20)      709 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/rules.xml
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.093567 plone.app.theming-5.0.3/src/plone/app/theming/tests/secondary-theme/
+-rw-r--r--   0 maurits    (501) staff       (20)      636 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/secondary-theme/manifest.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)      213 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/secondary-theme/rules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)     3357 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/test_controlpanel.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4183 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/test_exportimport.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4937 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/test_policy.py
+-rw-r--r--   0 maurits    (501) staff       (20)    29670 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/test_transform.py
+-rw-r--r--   0 maurits    (501) staff       (20)    23127 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/test_utils.py
+-rw-r--r--   0 maurits    (501) staff       (20)      177 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/theme.html
+-rw-r--r--   0 maurits    (501) staff       (20)      116 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/two.html
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.096029 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/
+-rw-r--r--   0 maurits    (501) staff       (20)      752 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/default_rules.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     1330 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/ignores_dotfiles_resource_forks.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     1029 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_default_rules.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     1437 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_default_rules_override.zip
+-rw-r--r--   0 maurits    (501) staff       (20)      985 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_prefix.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     8584 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_preview.zip
+-rw-r--r--   0 maurits    (501) staff       (20)      980 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_rules.zip
+-rw-r--r--   0 maurits    (501) staff       (20)      890 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/multiple_dir.zip
+-rw-r--r--   0 maurits    (501) staff       (20)      540 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/nodir.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     2395 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/subdirectories.zip
+-rw-r--r--   0 maurits    (501) staff       (20)     1403 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/theme.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.057354 plone.app.theming-5.0.3/src/plone/app/theming/themes/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.096763 plone.app.theming-5.0.3/src/plone/app/theming/themes/template/
+-rw-r--r--   0 maurits    (501) staff       (20)      158 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/themes/template/index.html
+-rw-r--r--   0 maurits    (501) staff       (20)       29 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/themes/template/manifest.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     1174 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/themes/template/rules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      228 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/themes.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     6679 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/transform.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1020 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/traversal.py
+-rw-r--r--   0 maurits    (501) staff       (20)      524 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/upgrade.py
+-rw-r--r--   0 maurits    (501) staff       (20)    24470 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/utils.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1169 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone/app/theming/zmi.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:34:46.068961 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)    63396 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     5142 2023-04-06 10:34:46.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)       40 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/entry_points.txt
+-rw-r--r--   0 maurits    (501) staff       (20)       16 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      411 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        6 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/src/plone.app.theming.egg-info/top_level.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1279 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/tox.ini
+-rw-r--r--   0 maurits    (501) staff       (20)      264 2023-04-06 10:34:45.000000 plone.app.theming-5.0.3/versions.cfg
```

### Comparing `plone.app.theming-5.0.2/.editorconfig` & `plone.app.theming-5.0.3/.editorconfig`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/.pre-commit-config.yaml` & `plone.app.theming-5.0.3/.pre-commit-config.yaml`

 * *Files 1% similar despite different names*

```diff
@@ -11,27 +11,27 @@
     -   id: pyupgrade
         args: [--py38-plus]
 -   repo: https://github.com/pycqa/isort
     rev: 5.12.0
     hooks:
     -   id: isort
 -   repo: https://github.com/psf/black
-    rev: 23.1.0
+    rev: 23.3.0
     hooks:
     -   id: black
 -   repo: https://github.com/collective/zpretty
-    rev: 3.0.2
+    rev: 3.0.3
     hooks:
     -   id: zpretty
 -   repo: https://github.com/PyCQA/flake8
     rev: 6.0.0
     hooks:
     -   id: flake8
 -   repo: https://github.com/codespell-project/codespell
-    rev: v2.2.2
+    rev: v2.2.4
     hooks:
     -   id: codespell
         additional_dependencies:
           - tomli
 -   repo: https://github.com/mgedmin/check-manifest
     rev: "0.49"
     hooks:
```

### Comparing `plone.app.theming-5.0.2/CHANGES.rst` & `plone.app.theming-5.0.3/CHANGES.rst`

 * *Files 1% similar despite different names*

```diff
@@ -5,14 +5,24 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.3 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Fix theme for `pat-code-editor`.
+  [petschki] (#219)
+
+
 5.0.2 (2023-03-22)
 ------------------
 
 Bug fixes:
 
 
 - Fixes circular dependency on ZCML level to `Products.CMFPlone`:
```

### Comparing `plone.app.theming-5.0.2/LICENSE` & `plone.app.theming-5.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/PKG-INFO` & `plone.app.theming-5.0.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.theming
-Version: 5.0.2
+Version: 5.0.3
 Summary: Integrates the Diazo theming engine with Plone
 Home-page: https://pypi.org/project/plone.app.theming
 Author: Martin Aspeli and Laurence Rowe
 Author-email: optilude@gmail.com
 License: GPL
 Keywords: plone diazo xdv deliverance theme transform xslt
 Classifier: Development Status :: 5 - Production/Stable
@@ -1071,14 +1071,24 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.3 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Fix theme for `pat-code-editor`.
+  [petschki] (#219)
+
+
 5.0.2 (2023-03-22)
 ------------------
 
 Bug fixes:
 
 
 - Fixes circular dependency on ZCML level to `Products.CMFPlone`:
```

### Comparing `plone.app.theming-5.0.2/TODO.txt` & `plone.app.theming-5.0.3/TODO.txt`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/docs/index.rst` & `plone.app.theming-5.0.3/docs/index.rst`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/pyproject.toml` & `plone.app.theming-5.0.3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/resources/theme/theme1/overrides/plone.app.layout.viewlets.colophon.pt` & `plone.app.theming-5.0.3/resources/theme/theme1/overrides/plone.app.layout.viewlets.colophon.pt`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/resources/theme/theme1/rules.xml` & `plone.app.theming-5.0.3/resources/theme/theme1/rules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/resources/theme/theme1/views/class-view.pt` & `plone.app.theming-5.0.3/resources/theme/theme1/views/class-view.pt`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/setup.py` & `plone.app.theming-5.0.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from setuptools import find_packages
 from setuptools import setup
 
 import os
 
 
-version = "5.0.2"
+version = "5.0.3"
 
 longdescription = open("README.rst").read()
 longdescription += "\n\n"
 longdescription += open(
     os.path.join(
         "src", "plone", "app", "theming", "browser", "resources", "userguide.rst"
     )
```

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/configure.zcml` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/configure.zcml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/controlpanel.pt` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/controlpanel.pt`

 * *Files 0% similar despite different names*

```diff
@@ -738,15 +738,15 @@
 
                         <textarea class="pat-code-editor"
                                   id="custom_css"
                                   cols="160"
                                   name="custom_css"
                                   placeholder="Put your plain css..."
                                   rows="40"
-                                  data-pat-code-editor="language: css; theme: tomorrow"
+                                  data-pat-code-editor="language: css; theme: light"
                                   tal:content="custom_css"
                                   i18n:attributes="placeholder"
                         ></textarea>
 
                       </div>
                     </fieldset>
                   </div>
```

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/controlpanel.py` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/controlpanel.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/custom_css.py` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/custom_css.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/icon.gif` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/icon.gif`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/controlpanel.css` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/controlpanel.css`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/defaultPreview.png` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/defaultPreview.png`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/preview.png` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/preview.png`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/resources/userguide.rst` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/resources/userguide.rst`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/browser/themefile.py` & `plone.app.theming-5.0.3/src/plone/app/theming/browser/themefile.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/configure.zcml` & `plone.app.theming-5.0.3/src/plone/app/theming/configure.zcml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/exportimport/handler.py` & `plone.app.theming-5.0.3/src/plone/app/theming/exportimport/handler.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/interfaces.py` & `plone.app.theming-5.0.3/src/plone/app/theming/interfaces.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/plugins/hooks.py` & `plone.app.theming-5.0.3/src/plone/app/theming/plugins/hooks.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/plugins/utils.py` & `plone.app.theming-5.0.3/src/plone/app/theming/plugins/utils.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/policy.py` & `plone.app.theming-5.0.3/src/plone/app/theming/policy.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/profiles/default/controlpanel.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/profiles/default/controlpanel.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/testing.py` & `plone.app.theming-5.0.3/src/plone/app/theming/testing.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/another-theme/manifest.cfg` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/another-theme/manifest.cfg`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/configure.zcml` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/configure.zcml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/paramrules.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/paramrules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/overridesrules.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/overridesrules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/resources/rules.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/resources/rules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/rules.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/rules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/secondary-theme/manifest.cfg` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/secondary-theme/manifest.cfg`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/test_controlpanel.py` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/test_controlpanel.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/test_exportimport.py` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/test_exportimport.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/test_policy.py` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/test_policy.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/test_transform.py` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/test_transform.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/test_utils.py` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/default_rules.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/default_rules.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/ignores_dotfiles_resource_forks.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/ignores_dotfiles_resource_forks.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_default_rules.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_default_rules.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_default_rules_override.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_default_rules_override.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_prefix.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_prefix.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_preview.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_preview.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/manifest_rules.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/manifest_rules.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/multiple_dir.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/multiple_dir.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/nodir.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/nodir.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/tests/zipfiles/subdirectories.zip` & `plone.app.theming-5.0.3/src/plone/app/theming/tests/zipfiles/subdirectories.zip`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/theme.py` & `plone.app.theming-5.0.3/src/plone/app/theming/theme.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/themes/template/rules.xml` & `plone.app.theming-5.0.3/src/plone/app/theming/themes/template/rules.xml`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/transform.py` & `plone.app.theming-5.0.3/src/plone/app/theming/transform.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/traversal.py` & `plone.app.theming-5.0.3/src/plone/app/theming/traversal.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/upgrade.py` & `plone.app.theming-5.0.3/src/plone/app/theming/upgrade.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/utils.py` & `plone.app.theming-5.0.3/src/plone/app/theming/utils.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone/app/theming/zmi.py` & `plone.app.theming-5.0.3/src/plone/app/theming/zmi.py`

 * *Files identical despite different names*

### Comparing `plone.app.theming-5.0.2/src/plone.app.theming.egg-info/PKG-INFO` & `plone.app.theming-5.0.3/src/plone.app.theming.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.theming
-Version: 5.0.2
+Version: 5.0.3
 Summary: Integrates the Diazo theming engine with Plone
 Home-page: https://pypi.org/project/plone.app.theming
 Author: Martin Aspeli and Laurence Rowe
 Author-email: optilude@gmail.com
 License: GPL
 Keywords: plone diazo xdv deliverance theme transform xslt
 Classifier: Development Status :: 5 - Production/Stable
@@ -1071,14 +1071,24 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.3 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Fix theme for `pat-code-editor`.
+  [petschki] (#219)
+
+
 5.0.2 (2023-03-22)
 ------------------
 
 Bug fixes:
 
 
 - Fixes circular dependency on ZCML level to `Products.CMFPlone`:
```

### Comparing `plone.app.theming-5.0.2/src/plone.app.theming.egg-info/SOURCES.txt` & `plone.app.theming-5.0.3/src/plone.app.theming.egg-info/SOURCES.txt`

 * *Files identical despite different names*

