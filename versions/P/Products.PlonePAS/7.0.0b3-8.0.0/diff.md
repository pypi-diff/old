# Comparing `tmp/Products.PlonePAS-7.0.0b3.tar.gz` & `tmp/Products.PlonePAS-8.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Products.PlonePAS-7.0.0b3.tar", last modified: Tue Oct 11 21:00:29 2022, max compression
+gzip compressed data, was "Products.PlonePAS-8.0.0.tar", last modified: Thu Apr  6 10:28:06 2023, max compression
```

## Comparing `Products.PlonePAS-7.0.0b3.tar` & `Products.PlonePAS-8.0.0.tar`

### file list

```diff
@@ -1,120 +1,123 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.172064 Products.PlonePAS-7.0.0b3/
--rw-r--r--   0 maurits    (501) staff       (20)      176 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/.gitignore
--rw-r--r--   0 maurits    (501) staff       (20)    31464 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/CHANGES.rst
--rw-r--r--   0 maurits    (501) staff       (20)       70 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)      141 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)    35741 2022-10-11 21:00:29.172227 Products.PlonePAS-7.0.0b3/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     3432 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/README.rst
--rw-r--r--   0 maurits    (501) staff       (20)      438 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/buildout.cfg
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.148523 Products.PlonePAS-7.0.0b3/docs/
--rw-r--r--   0 maurits    (501) staff       (20)     2160 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/LICENSE.ZPL
--rw-r--r--   0 maurits    (501) staff       (20)      886 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/STATUS.txt
--rw-r--r--   0 maurits    (501) staff       (20)     5720 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/TODO.txt
--rw-r--r--   0 maurits    (501) staff       (20)      337 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/copyright-and-license.txt
--rw-r--r--   0 maurits    (501) staff       (20)      891 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/pas-dev.txt
--rw-r--r--   0 maurits    (501) staff       (20)      452 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/docs/scratchpad.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1248 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/mypy.ini
--rw-r--r--   0 maurits    (501) staff       (20)      471 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)      259 2022-10-11 21:00:29.172763 Products.PlonePAS-7.0.0b3/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)     1699 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/setup.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.142688 Products.PlonePAS-7.0.0b3/src/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.148787 Products.PlonePAS-7.0.0b3/src/Products/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.155113 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/
--rw-r--r--   0 maurits    (501) staff       (20)     4656 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.156348 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      889 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     1371 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/info.py
--rw-r--r--   0 maurits    (501) staff       (20)      977 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/member.py
--rw-r--r--   0 maurits    (501) staff       (20)     2619 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/search.py
--rw-r--r--   0 maurits    (501) staff       (20)      584 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/config.py
--rw-r--r--   0 maurits    (501) staff       (20)      507 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)      795 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/events.py
--rw-r--r--   0 maurits    (501) staff       (20)     1168 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/exportimport.zcml
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.158626 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3247 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/browser.py
--rw-r--r--   0 maurits    (501) staff       (20)     2384 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/capabilities.py
--rw-r--r--   0 maurits    (501) staff       (20)      192 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/events.py
--rw-r--r--   0 maurits    (501) staff       (20)     3634 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/group.py
--rw-r--r--   0 maurits    (501) staff       (20)      185 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/memberdata.py
--rw-r--r--   0 maurits    (501) staff       (20)      272 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/membership.py
--rw-r--r--   0 maurits    (501) staff       (20)     3424 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/plugins.py
--rw-r--r--   0 maurits    (501) staff       (20)      402 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/propertysheets.py
--rw-r--r--   0 maurits    (501) staff       (20)     1945 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/ldapmp.py
--rw-r--r--   0 maurits    (501) staff       (20)    20812 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/pas.py
--rw-r--r--   0 maurits    (501) staff       (20)     2222 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/patch.py
--rw-r--r--   0 maurits    (501) staff       (20)      519 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/permissions.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.161429 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3907 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/autogroup.py
--rw-r--r--   0 maurits    (501) staff       (20)     4011 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/cookie_handler.py
--rw-r--r--   0 maurits    (501) staff       (20)     2007 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/crumbler.py
--rw-r--r--   0 maurits    (501) staff       (20)     9253 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/group.py
--rw-r--r--   0 maurits    (501) staff       (20)     5317 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/local_role.py
--rw-r--r--   0 maurits    (501) staff       (20)     2509 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/passwordpolicy.py
--rw-r--r--   0 maurits    (501) staff       (20)    10610 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/property.py
--rw-r--r--   0 maurits    (501) staff       (20)     5529 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/role.py
--rw-r--r--   0 maurits    (501) staff       (20)     7113 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/ufactory.py
--rw-r--r--   0 maurits    (501) staff       (20)     4464 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/user.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.143658 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.161960 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/default/
--rw-r--r--   0 maurits    (501) staff       (20)       68 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/default/metadata.xml
--rw-r--r--   0 maurits    (501) staff       (20)       65 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/default/plone-pas.txt
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.162479 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/root-cookie/
--rw-r--r--   0 maurits    (501) staff       (20)       68 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/root-cookie/metadata.xml
--rw-r--r--   0 maurits    (501) staff       (20)      116 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles/root-cookie/plone-pas-zope-root-cookie.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1363 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles.zcml
--rw-r--r--   0 maurits    (501) staff       (20)    19293 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/setuphandlers.py
--rw-r--r--   0 maurits    (501) staff       (20)     3764 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/sheet.py
--rw-r--r--   0 maurits    (501) staff       (20)     1778 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/testing.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.166059 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     2803 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/cookie_auth.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1392 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/dummy.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.166957 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/
--rw-r--r--   0 maurits    (501) staff       (20)     5714 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/test.gif
--rw-r--r--   0 maurits    (501) staff       (20)     1898 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/test.jpg
--rw-r--r--   0 maurits    (501) staff       (20)      315 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/test.png
--rw-r--r--   0 maurits    (501) staff       (20)     6139 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_basic_ops.py
--rw-r--r--   0 maurits    (501) staff       (20)      656 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_doctests.py
--rw-r--r--   0 maurits    (501) staff       (20)     6944 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_groupdatatool.py
--rw-r--r--   0 maurits    (501) staff       (20)    10188 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_groupstool.py
--rw-r--r--   0 maurits    (501) staff       (20)     5740 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_memberdatatool.py
--rw-r--r--   0 maurits    (501) staff       (20)    42534 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_membershiptool.py
--rw-r--r--   0 maurits    (501) staff       (20)    10528 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_properties.py
--rw-r--r--   0 maurits    (501) staff       (20)     3273 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_role_plugin.py
--rw-r--r--   0 maurits    (501) staff       (20)     5335 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_setup.py
--rw-r--r--   0 maurits    (501) staff       (20)     1008 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_views.py
--rw-r--r--   0 maurits    (501) staff       (20)      954 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tool.gif
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.168531 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      179 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)    18194 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/groupdata.py
--rw-r--r--   0 maurits    (501) staff       (20)    14411 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/groups.py
--rw-r--r--   0 maurits    (501) staff       (20)    17325 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/memberdata.py
--rw-r--r--   0 maurits    (501) staff       (20)    29154 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/membership.py
--rw-r--r--   0 maurits    (501) staff       (20)     2101 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/upgrades.py
--rw-r--r--   0 maurits    (501) staff       (20)     6505 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/utils.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.171833 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/
--rw-r--r--   0 maurits    (501) staff       (20)     1543 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/AutoGroupForm.zpt
--rw-r--r--   0 maurits    (501) staff       (20)      847 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/CookieCrumblingPluginForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      512 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/ExtendedCookieAuthHelperForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      730 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/GroupAwareRoleManagerForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      679 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/GroupManagerForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      666 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/LocalRolesManagerForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      703 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/MutablePropertyProviderForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)     1147 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/PasswordPolicyForm.zpt
--rw-r--r--   0 maurits    (501) staff       (20)      687 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/PloneUserFactoryForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)      659 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/UserManagerForm.dtml
--rw-r--r--   0 maurits    (501) staff       (20)     3569 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/membershipRolemapping.dtml
--rw-r--r--   0 maurits    (501) staff       (20)     1874 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/portrait_fix.dtml
--rw-r--r--   0 maurits    (501) staff       (20)       56 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-10-11 21:00:29.150734 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)    35741 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     4028 2022-10-11 21:00:29.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/dependency_links.txt
--rw-r--r--   0 maurits    (501) staff       (20)        9 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)      211 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        9 2022-10-11 21:00:28.000000 Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/top_level.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.967130 Products.PlonePAS-8.0.0/
+-rw-r--r--   0 maurits    (501) staff       (20)     1019 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/.editorconfig
+-rw-r--r--   0 maurits    (501) staff       (20)      176 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/.gitignore
+-rw-r--r--   0 maurits    (501) staff       (20)      128 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/.meta.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      973 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/.pre-commit-config.yaml
+-rw-r--r--   0 maurits    (501) staff       (20)    31855 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       70 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      141 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)    36204 2023-04-06 10:28:06.967280 Products.PlonePAS-8.0.0/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     3432 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/README.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      438 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/buildout.cfg
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.941007 Products.PlonePAS-8.0.0/docs/
+-rw-r--r--   0 maurits    (501) staff       (20)     2160 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/LICENSE.ZPL
+-rw-r--r--   0 maurits    (501) staff       (20)      888 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/STATUS.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     5720 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/TODO.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      337 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/copyright-and-license.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      891 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/pas-dev.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      452 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/docs/scratchpad.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1248 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/mypy.ini
+-rw-r--r--   0 maurits    (501) staff       (20)     1769 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:28:06.967771 Products.PlonePAS-8.0.0/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     1870 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/setup.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.933668 Products.PlonePAS-8.0.0/src/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.941319 Products.PlonePAS-8.0.0/src/Products/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.948629 Products.PlonePAS-8.0.0/src/Products/PlonePAS/
+-rw-r--r--   0 maurits    (501) staff       (20)     4655 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.950193 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      910 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     1371 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/info.py
+-rw-r--r--   0 maurits    (501) staff       (20)      977 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/member.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2617 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/search.py
+-rw-r--r--   0 maurits    (501) staff       (20)      584 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/config.py
+-rw-r--r--   0 maurits    (501) staff       (20)      512 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      795 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/events.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1184 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/exportimport.zcml
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.952827 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3247 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/browser.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2384 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/capabilities.py
+-rw-r--r--   0 maurits    (501) staff       (20)      192 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/events.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3635 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/group.py
+-rw-r--r--   0 maurits    (501) staff       (20)      185 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/memberdata.py
+-rw-r--r--   0 maurits    (501) staff       (20)      272 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/membership.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3424 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/plugins.py
+-rw-r--r--   0 maurits    (501) staff       (20)      402 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/propertysheets.py
+-rw-r--r--   0 maurits    (501) staff       (20)    20812 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/pas.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2222 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/patch.py
+-rw-r--r--   0 maurits    (501) staff       (20)      519 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/permissions.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.955922 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3907 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/autogroup.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4011 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/cookie_handler.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2007 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/crumbler.py
+-rw-r--r--   0 maurits    (501) staff       (20)     9251 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/group.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5314 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/local_role.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2509 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/passwordpolicy.py
+-rw-r--r--   0 maurits    (501) staff       (20)    10608 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/property.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5528 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/role.py
+-rw-r--r--   0 maurits    (501) staff       (20)     7109 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/ufactory.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4465 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/user.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.934666 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.956429 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/default/
+-rw-r--r--   0 maurits    (501) staff       (20)       85 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/default/metadata.xml
+-rw-r--r--   0 maurits    (501) staff       (20)       65 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/default/plone-pas.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.957229 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/root-cookie/
+-rw-r--r--   0 maurits    (501) staff       (20)       85 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/root-cookie/metadata.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      116 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles/root-cookie/plone-pas-zope-root-cookie.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1387 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)    19253 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/setuphandlers.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3771 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/sheet.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1806 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/testing.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.960676 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2803 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/cookie_auth.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     1393 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/dummy.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.961472 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/
+-rw-r--r--   0 maurits    (501) staff       (20)     5714 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/test.gif
+-rw-r--r--   0 maurits    (501) staff       (20)     1898 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/test.jpg
+-rw-r--r--   0 maurits    (501) staff       (20)      315 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/test.png
+-rw-r--r--   0 maurits    (501) staff       (20)     6138 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_basic_ops.py
+-rw-r--r--   0 maurits    (501) staff       (20)      646 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_doctests.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6968 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_groupdatatool.py
+-rw-r--r--   0 maurits    (501) staff       (20)    10213 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_groupstool.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5739 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_memberdatatool.py
+-rw-r--r--   0 maurits    (501) staff       (20)    42530 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_membershiptool.py
+-rw-r--r--   0 maurits    (501) staff       (20)    10526 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_properties.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3272 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_role_plugin.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5335 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_setup.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1007 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_views.py
+-rw-r--r--   0 maurits    (501) staff       (20)      954 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tool.gif
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.963059 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      179 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)    18192 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/groupdata.py
+-rw-r--r--   0 maurits    (501) staff       (20)    14413 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/groups.py
+-rw-r--r--   0 maurits    (501) staff       (20)    17323 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/memberdata.py
+-rw-r--r--   0 maurits    (501) staff       (20)    29163 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/membership.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2101 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/upgrades.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6500 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/utils.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.966763 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/
+-rw-r--r--   0 maurits    (501) staff       (20)     2089 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/AutoGroupForm.zpt
+-rw-r--r--   0 maurits    (501) staff       (20)      847 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/CookieCrumblingPluginForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      512 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/ExtendedCookieAuthHelperForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      730 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/GroupAwareRoleManagerForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      679 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/GroupManagerForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      666 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/LocalRolesManagerForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      703 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/MutablePropertyProviderForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)     1501 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/PasswordPolicyForm.zpt
+-rw-r--r--   0 maurits    (501) staff       (20)      687 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/PloneUserFactoryForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)      659 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/UserManagerForm.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)     3569 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/membershipRolemapping.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)     1874 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/portrait_fix.dtml
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:28:06.943612 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)    36204 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     4053 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        9 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      274 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        9 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/top_level.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1279 2023-04-06 10:28:06.000000 Products.PlonePAS-8.0.0/tox.ini
```

### Comparing `Products.PlonePAS-7.0.0b3/CHANGES.rst` & `Products.PlonePAS-8.0.0/CHANGES.rst`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,41 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+8.0.0 (2023-04-06)
+------------------
+
+Breaking changes:
+
+
+- Remove `ldapmp` module. It is not being tested in Plone 6.
+  See https://github.com/plone/Products.PlonePAS/pull/71#pullrequestreview-1351349950
+  [gforcada] (#1)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (80cf330f)
+
+
+7.0.0 (2022-12-02)
+------------------
+
+Bug fixes:
+
+
+- Final release for Plone 6.0.0 (#600)
+
+
 7.0.0b3 (2022-10-11)
 --------------------
 
 Bug fixes:
 
 
 - Fix admin password used in tests. [davisagli] (#70)
@@ -332,22 +359,22 @@
 ------------------
 
 - Add a integrated test setup with codeanalysis and travis. For this moved
   ``Products`` folder to a ``src`` folder in order to follow the package
   structure expected by ``buildout.plonetest``'s ``qa.cfg``.
   [jensens]
 
-- Make patching of LDAPMultiPlugin explizit. Code using those must call
+- Make patching of LDAPMultiPlugin explicit. Code using those must call
   ``Products.PlonePAS.ldapmp.patch_ldapmp`` with no parameters in order
   to activate the patches.
   [jensens]
 
 - Removed (optional) Archetypes Storage (used in past with CMFMember, which
-  itself was long time ago superseeded by Membrane). Probably dead code. If
-  theres someone out there needing it in Plone 5 please copy the code from
+  itself was long time ago superseded by Membrane). Probably dead code. If
+  there's someone out there needing it in Plone 5 please copy the code from
   git/Plone4 in your addon/project.
   [jensens]
 
 - Moved ``Extensions/Install.py`` functions to setuphandlers, kept BBB import
   for ``activatePluginInterfaces`` since this is imported by ``borg.localrole``.
   [jensens]
 
@@ -594,15 +621,15 @@
 
 - Made last_login_time logic compatible with DateTime 2.12.5.
   [hannosch]
 
 4.0.1 - 2010-07-31
 ------------------
 
-- Clean up some unused imports and variable assigments.
+- Clean up some unused imports and variable assignments.
   [esteele]
 
 - Stop looking to GRUF to check if group properties can be edited.
   [esteele]
 
 4.0 - 2010-07-18
 ----------------
@@ -1217,15 +1244,15 @@
   as GRUF itself uses.
   [mj]
 
 - Fix migration to handle properties of selection or multiple selection
   types.
   [reinout]
 
-- Correct creation of groups wich default group managers.
+- Correct creation of groups which default group managers.
   [dreamcatcher]
 
 - Fix migration from GRUF sites: also include the member properties in the
   migration.
   [tesdal]
 
 - Correct the test for creation of groups with the same id as users: search
```

### Comparing `Products.PlonePAS-7.0.0b3/PKG-INFO` & `Products.PlonePAS-8.0.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Products.PlonePAS
-Version: 7.0.0b3
+Version: 8.0.0
 Summary: PlonePAS modifies the PluggableAuthService for use by Plone.
 Home-page: https://github.com/plone/Products.PlonePAS
 Author: Kapil Thangavelu, Wichert Akkerman
 Author-email: plone-developers@lists.sourceforge.net
 License: ZPL
 Keywords: Zope CMF Plone PAS authentication
 Classifier: Development Status :: 5 - Production/Stable
@@ -14,14 +14,16 @@
 Classifier: Framework :: Zope
 Classifier: Framework :: Zope :: 5
 Classifier: License :: OSI Approved :: Zope Public License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Python: >=3.8
 Provides-Extra: test
 
 Overview
 ========
 
 This product extends `PluggableAuthService <https://github.com/zopefoundation/Products.PluggableAuthService>`_ (PAS) for use in Plone.
 
@@ -75,27 +77,27 @@
 
 Initial creation: The PAS CIGNEX Sprint Team [ Anders, Bob, Ben,
 Chad, Gautham, Joel, Kapil, Michel, Micheal ]
 
 Post-sprint work: J Cameron Cooper, Leo, Sidnei, Mark at `Enfold
 Systems <http://enfoldsystems.com>`_
 
-Basic setAuthCookie support (to mimick CookieCrumbler):
+Basic setAuthCookie support (to mimic CookieCrumbler):
 Rocky Burt at `ServerZen Software <http://www.serverzen.com>`_
 
 Synced login process with Plone:
 Dorneles Tremea at `PloneSolutions <http://plonesolutions.com>`_
 
 Bugfixes, various development and merging with Plone:
 Wichert Akkerman at Simplon
 
 Bugfixes, improvements to membership and property lookups:
 Eric Steele and Erik Rose
 
-Review, cleanup, modernize code, adressing Plone 5:
+Review, cleanup, modernize code, addressing Plone 5:
 Jens Klein, BlueDynamics Alliance - `Klein & Partner KG <http://kleinundpartner.at>`_
 
 Source Code
 -----------
 
 Contributors please read the document `Process for Plone core's development <https://docs.plone.org/develop/coredev/docs/index.html>`_
 
@@ -107,14 +109,41 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+8.0.0 (2023-04-06)
+------------------
+
+Breaking changes:
+
+
+- Remove `ldapmp` module. It is not being tested in Plone 6.
+  See https://github.com/plone/Products.PlonePAS/pull/71#pullrequestreview-1351349950
+  [gforcada] (#1)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (80cf330f)
+
+
+7.0.0 (2022-12-02)
+------------------
+
+Bug fixes:
+
+
+- Final release for Plone 6.0.0 (#600)
+
+
 7.0.0b3 (2022-10-11)
 --------------------
 
 Bug fixes:
 
 
 - Fix admin password used in tests. [davisagli] (#70)
@@ -435,22 +464,22 @@
 ------------------
 
 - Add a integrated test setup with codeanalysis and travis. For this moved
   ``Products`` folder to a ``src`` folder in order to follow the package
   structure expected by ``buildout.plonetest``'s ``qa.cfg``.
   [jensens]
 
-- Make patching of LDAPMultiPlugin explizit. Code using those must call
+- Make patching of LDAPMultiPlugin explicit. Code using those must call
   ``Products.PlonePAS.ldapmp.patch_ldapmp`` with no parameters in order
   to activate the patches.
   [jensens]
 
 - Removed (optional) Archetypes Storage (used in past with CMFMember, which
-  itself was long time ago superseeded by Membrane). Probably dead code. If
-  theres someone out there needing it in Plone 5 please copy the code from
+  itself was long time ago superseded by Membrane). Probably dead code. If
+  there's someone out there needing it in Plone 5 please copy the code from
   git/Plone4 in your addon/project.
   [jensens]
 
 - Moved ``Extensions/Install.py`` functions to setuphandlers, kept BBB import
   for ``activatePluginInterfaces`` since this is imported by ``borg.localrole``.
   [jensens]
 
@@ -697,15 +726,15 @@
 
 - Made last_login_time logic compatible with DateTime 2.12.5.
   [hannosch]
 
 4.0.1 - 2010-07-31
 ------------------
 
-- Clean up some unused imports and variable assigments.
+- Clean up some unused imports and variable assignments.
   [esteele]
 
 - Stop looking to GRUF to check if group properties can be edited.
   [esteele]
 
 4.0 - 2010-07-18
 ----------------
@@ -1320,15 +1349,15 @@
   as GRUF itself uses.
   [mj]
 
 - Fix migration to handle properties of selection or multiple selection
   types.
   [reinout]
 
-- Correct creation of groups wich default group managers.
+- Correct creation of groups which default group managers.
   [dreamcatcher]
 
 - Fix migration from GRUF sites: also include the member properties in the
   migration.
   [tesdal]
 
 - Correct the test for creation of groups with the same id as users: search
```

### Comparing `Products.PlonePAS-7.0.0b3/README.rst` & `Products.PlonePAS-8.0.0/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -53,27 +53,27 @@
 
 Initial creation: The PAS CIGNEX Sprint Team [ Anders, Bob, Ben,
 Chad, Gautham, Joel, Kapil, Michel, Micheal ]
 
 Post-sprint work: J Cameron Cooper, Leo, Sidnei, Mark at `Enfold
 Systems <http://enfoldsystems.com>`_
 
-Basic setAuthCookie support (to mimick CookieCrumbler):
+Basic setAuthCookie support (to mimic CookieCrumbler):
 Rocky Burt at `ServerZen Software <http://www.serverzen.com>`_
 
 Synced login process with Plone:
 Dorneles Tremea at `PloneSolutions <http://plonesolutions.com>`_
 
 Bugfixes, various development and merging with Plone:
 Wichert Akkerman at Simplon
 
 Bugfixes, improvements to membership and property lookups:
 Eric Steele and Erik Rose
 
-Review, cleanup, modernize code, adressing Plone 5:
+Review, cleanup, modernize code, addressing Plone 5:
 Jens Klein, BlueDynamics Alliance - `Klein & Partner KG <http://kleinundpartner.at>`_
 
 Source Code
 -----------
 
 Contributors please read the document `Process for Plone core's development <https://docs.plone.org/develop/coredev/docs/index.html>`_
```

### Comparing `Products.PlonePAS-7.0.0b3/docs/LICENSE.ZPL` & `Products.PlonePAS-8.0.0/docs/LICENSE.ZPL`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/docs/STATUS.txt` & `Products.PlonePAS-8.0.0/docs/STATUS.txt`

 * *Files 12% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Some Plone UI functionality will not work with all plugins.
 many plugins cannot modify users/properties/groups/etc. There is some
 capabilities checking now, so that things that cannot be changed will not
-appear changable.
+appear changeable.
 
 PlonePAS implements a good deal of the API expected of a UserFolder
 and of GRUF. However, no systematic determination of interface
 fulfillment has been made, beyond that used by the Plone UI. Over time
-GRUF compatibilty will be removed in favour of a new interface on top
+GRUF compatibility will be removed in favour of a new interface on top
 of PAS.
 
 PlonePAS will currently migrate the users and groups of a default
 Plone setup. Other setups may work. Please see the README.
 
 Using GRUF as a multi-source may work, but hasn't been looked at
 recently.
```

### Comparing `Products.PlonePAS-7.0.0b3/docs/TODO.txt` & `Products.PlonePAS-8.0.0/docs/TODO.txt`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/docs/pas-dev.txt` & `Products.PlonePAS-8.0.0/docs/pas-dev.txt`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/mypy.ini` & `Products.PlonePAS-8.0.0/mypy.ini`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/setup.py` & `Products.PlonePAS-8.0.0/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,28 +1,30 @@
 from setuptools import find_packages
 from setuptools import setup
 
-import sys
 
-
-version = "7.0.0b3"
+version = "8.0.0"
 
 
 longdescription = open("README.rst").read()
 longdescription += "\n"
 longdescription += open("CHANGES.rst").read()
 
 install_requires = [
+    "AuthEncoding",
+    "BTrees",
+    "Pillow",
     "plone.base",
     "plone.i18n",
     "plone.memoize",
     "plone.protect>=2.0.3",
+    "plone.registry",
     "plone.session",
     "Products.GenericSetup",
-    "Products.PluggableAuthService>=2.0b2.dev0",
+    "Products.PluggableAuthService>=2.0",
     "setuptools",
 ]
 
 setup(
     name="Products.PlonePAS",
     version=version,
     description="PlonePAS modifies the PluggableAuthService for use by Plone.",
@@ -35,27 +37,30 @@
         "Framework :: Zope",
         "Framework :: Zope :: 5",
         "License :: OSI Approved :: Zope Public License",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
     ],
     keywords="Zope CMF Plone PAS authentication",
     author="Kapil Thangavelu, Wichert Akkerman",
     author_email="plone-developers@lists.sourceforge.net",
     url="https://github.com/plone/Products.PlonePAS",
     license="ZPL",
     packages=find_packages("src"),
     package_dir={"": "src"},
     namespace_packages=["Products"],
     include_package_data=True,
     zip_safe=False,
+    python_requires=">=3.8",
     install_requires=install_requires,
     extras_require=dict(
         test=[
             "plone.app.testing",
+            "plone.app.contenttypes[test]",
             "plone.testing",
-            "plone.app.robotframework",
+            "Products.PluginRegistry",
         ],
     ),
 )
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/__init__.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -40,15 +40,14 @@
     registerMultiPlugin(passwordpolicy.PasswordPolicyPlugin.meta_type)
 except RuntimeError:
     # make refresh users happy
     pass
 
 
 def initialize(context):
-
     tools = (GroupsTool, GroupDataTool, MembershipTool, MemberDataTool)
 
     ToolInit(
         "PlonePAS Tool",
         tools=tools,
         icon="tool.gif",
     ).initialize(context)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/configure.zcml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -1,36 +1,37 @@
 <configure
-    i18n_domain="Five"
     xmlns="http://namespaces.zope.org/zope"
     xmlns:browser="http://namespaces.zope.org/browser"
-    xmlns:five="http://namespaces.zope.org/five">
+    xmlns:five="http://namespaces.zope.org/five"
+    i18n_domain="Five"
+    >
 
   <permission
       id="PAS.SearchPrincipals"
       title="Search for principals"
-  />
+      />
 
   <browser:page
-      allowed_interface="Products.PlonePAS.interfaces.browser.IPASInfoView"
-      class=".info.PASInfoView"
-      for="*"
       name="pas_info"
+      for="*"
+      class=".info.PASInfoView"
+      allowed_interface="Products.PlonePAS.interfaces.browser.IPASInfoView"
       permission="zope2.View"
-  />
+      />
 
   <browser:page
-      allowed_interface="Products.PlonePAS.interfaces.browser.IPASMemberView"
-      class=".member.PASMemberView"
-      for="*"
       name="pas_member"
+      for="*"
+      class=".member.PASMemberView"
+      allowed_interface="Products.PlonePAS.interfaces.browser.IPASMemberView"
       permission="zope2.View"
-  />
+      />
 
   <browser:page
-      allowed_interface="Products.PlonePAS.interfaces.browser.IPASSearchView"
-      class=".search.PASSearchView"
-      for="*"
       name="pas_search"
+      for="*"
+      class=".search.PASSearchView"
+      allowed_interface="Products.PlonePAS.interfaces.browser.IPASSearchView"
       permission="zope2.View"
-  />
+      />
 
 </configure>
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/info.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/info.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/member.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/member.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/browser/search.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/browser/search.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
     def extractCriteriaFromRequest(request):
         criteria = request.form.copy()
 
         for key in ["form.submitted", "submit", "b_start", "b_size"]:
             if key in criteria:
                 del criteria[key]
 
-        for (key, value) in criteria.items():
+        for key, value in criteria.items():
             if not value:
                 del criteria[key]
 
         return criteria
 
     @staticmethod
     def merge(results, key):
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/config.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/config.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/events.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/events.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/exportimport.zcml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/exportimport.zcml`

 * *Files 8% similar despite different names*

```diff
@@ -1,26 +1,26 @@
 <configure xmlns="http://namespaces.zope.org/zope">
 
   <adapter
       factory="Products.PluggableAuthService.plugins.exportimport.TitleOnlyExportImport"
-      for="Products.PluggableAuthService.interfaces.plugins.IUserFactoryPlugin"
       provides="Products.GenericSetup.interfaces.IFilesystemExporter"
-  />
+      for="Products.PluggableAuthService.interfaces.plugins.IUserFactoryPlugin"
+      />
   <adapter
       factory="Products.PluggableAuthService.plugins.exportimport.TitleOnlyExportImport"
-      for="Products.PluggableAuthService.interfaces.plugins.IUserFactoryPlugin"
       provides="Products.GenericSetup.interfaces.IFilesystemImporter"
-  />
+      for="Products.PluggableAuthService.interfaces.plugins.IUserFactoryPlugin"
+      />
 
   <!-- XXX This should point to an own export/import class! TitleOnly is far not enough -->
   <adapter
       factory="Products.PluggableAuthService.plugins.exportimport.TitleOnlyExportImport"
-      for="Products.PlonePAS.interfaces.plugins.IMutablePropertiesPlugin"
       provides="Products.GenericSetup.interfaces.IFilesystemExporter"
-  />
+      for="Products.PlonePAS.interfaces.plugins.IMutablePropertiesPlugin"
+      />
   <adapter
       factory="Products.PluggableAuthService.plugins.exportimport.TitleOnlyExportImport"
-      for="Products.PlonePAS.interfaces.plugins.IMutablePropertiesPlugin"
       provides="Products.GenericSetup.interfaces.IFilesystemImporter"
-  />
+      for="Products.PlonePAS.interfaces.plugins.IMutablePropertiesPlugin"
+      />
 
 </configure>
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/browser.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/browser.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/capabilities.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/capabilities.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/group.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/group.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from zope.interface import Interface
 
 
 class IGroupManagement(Interface):
     def addGroup(id, **kw):
         """
         Create a group with the supplied id, roles, and groups.
-        return True if the operation suceeded
+        return True if the operation succeeded
         """
 
     def addPrincipalToGroup(principal_id, group_id):
         """
         Add a given principal to the group.
         return True on success
         """
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/interfaces/plugins.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/interfaces/plugins.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/pas.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/pas.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# pas alterations and monkies
+# pas alterations and monkeys
 from AccessControl import getSecurityManager
 from AccessControl import Unauthorized
 from AccessControl.PermissionRole import PermissionRole
 from AccessControl.Permissions import change_permissions
 from AccessControl.Permissions import manage_properties
 from AccessControl.Permissions import manage_users as ManageUsers
 from AccessControl.requestmethod import postonly
@@ -37,15 +37,15 @@
 
 
 #################################
 # helper functions
 
 
 def _userSetGroups(pas, user_id, groupnames):
-    """method was used at GRUF level, but is used inside this monkies at several
+    """method was used at GRUF level, but is used inside this monkeys at several
     places too.
 
     We no longer provide it on PAS to clean up patches
 
     """
     plugins = pas.plugins
     gtool = getToolByName(pas, "portal_groups")
@@ -79,15 +79,15 @@
             except _SWALLOWABLE_PLUGIN_EXCEPTIONS:
                 logger.info(
                     "PluggableAuthService: GroupManagement %s error", gm_id, exc_info=1
                 )
 
 
 #################################
-# pas folder monkies - standard zope user folder api or GRUF
+# pas folder monkeys - standard zope user folder api or GRUF
 
 
 def _doAddUser(self, login, password, roles, domains, groups=None, **kw):
     """Masking of PAS._doAddUser to add groups param."""
     _old_doAddUser = getattr(self, getattr(_doAddUser, ORIG_NAME))
     retval = _old_doAddUser(login, password, roles, domains)
     if groups is not None:
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/patch.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/patch.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/permissions.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/permissions.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/autogroup.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/autogroup.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/cookie_handler.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/cookie_handler.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/crumbler.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/crumbler.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/group.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/group.py`

 * *Files 0% similar despite different names*

```diff
@@ -40,15 +40,14 @@
 
     if RESPONSE is not None:
         return RESPONSE.redirect("manage_workspace")
 
 
 @implementer(IGroupManagement, IGroupIntrospection, IGroupCapability, IDeleteCapability)
 class GroupManager(ZODBGroupManager):
-
     meta_type = "Group Manager"
     security = ClassSecurityInfo()
 
     def __init__(self, *args, **kw):
         ZODBGroupManager.__init__(self, *args, **kw)
         # reverse index of groups->principal
         self._group_principal_map = OOBTree()
@@ -105,15 +104,15 @@
     def getGroupIds(self):
         return self.listGroupIds()
 
     def getGroupMembers(self, group_id):
         return tuple(self._group_principal_map.get(group_id, ()))
 
     #################################
-    # capabilties interface impls.
+    # capabilities interface impls.
 
     @security.public
     def allowDeletePrincipal(self, principal_id):
         """True iff this plugin can delete a certain group.
         This is true if this plugin manages the group.
         """
         if self._groups.get(principal_id) is not None:
@@ -166,15 +165,14 @@
         """group_id -> decorated_group
         This method based on PluggableAuthService._findGroup
         """
         group = self._createGroup(plugins, group_id, title)
 
         propfinders = plugins.listPlugins(IPropertiesPlugin)
         for propfinder_id, propfinder in propfinders:
-
             data = propfinder.getPropertiesForUser(group, request)
             if data:
                 group.addPropertysheet(propfinder_id, data)
 
         groups = self._getPAS()._getGroupsForPrincipal(group, request, plugins=plugins)
         group._addGroups(groups)
 
@@ -187,15 +185,14 @@
 
         group._addRoles(["Authenticated"])
 
         return group.__of__(self)
 
     @security.private
     def _verifyGroup(self, plugins, group_id=None, title=None):
-
         """group_id -> boolean
         This method based on PluggableAuthService._verifyUser
         """
         criteria = {}
 
         if group_id is not None:
             criteria["id"] = group_id
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/local_role.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/local_role.py`

 * *Files 0% similar despite different names*

```diff
@@ -95,15 +95,14 @@
         user_id = user.getId()
         group_ids = user.getGroups()
 
         principal_ids = list(group_ids)
         principal_ids.insert(0, user_id)
 
         while 1:
-
             local_roles = getattr(inner_obj, "__ac_local_roles__", None)
 
             if local_roles and callable(local_roles):
                 local_roles = local_roles()
 
             if local_roles:
                 dict = local_roles
@@ -143,22 +142,20 @@
         return None
 
     def getAllLocalRolesInContext(self, context):
         roles = {}
         object = aq_inner(context)
 
         while True:
-
             local_roles = getattr(object, "__ac_local_roles__", None)
 
             if local_roles and callable(local_roles):
                 local_roles = local_roles()
 
             if local_roles:
-
                 dict = local_roles
 
                 for principal, localroles in dict.items():
                     if principal not in roles:
                         roles[principal] = set()
 
                     roles[principal].update(localroles)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/passwordpolicy.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/passwordpolicy.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/property.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/property.py`

 * *Files 0% similar despite different names*

```diff
@@ -208,15 +208,15 @@
             del self._storage[user_id]
         except KeyError:
             pass
 
     @security.private
     def testMemberData(self, memberdata, criteria, exact_match=False):
         """Test if a memberdata matches the search criteria."""
-        for (key, value) in criteria.items():
+        for key, value in criteria.items():
             testvalue = memberdata.get(key, None)
             if testvalue is None:
                 return False
 
             if isStringType(testvalue):
                 testvalue = safe_unicode(testvalue.lower())
             if isStringType(value):
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/role.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/role.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,15 +32,14 @@
 manage_addGroupAwareRoleManagerForm = DTMLFile(
     "../zmi/GroupAwareRoleManagerForm", globals()
 )
 
 
 @implementer(IAssignRoleCapability)
 class GroupAwareRoleManager(ZODBRoleManager):
-
     meta_type = "Group Aware Role Manager"
     security = ClassSecurityInfo()
 
     def updateRolesList(self):
         role_holder = aq_parent(aq_inner(self._getPAS()))
         for role in getattr(role_holder, "__ac_roles__", ()):
             if role not in ("Anonymous", "Authenticated") and role not in self._roles:
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/ufactory.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/ufactory.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,14 @@
 
     if RESPONSE is not None:
         return RESPONSE.redirect("manage_workspace")
 
 
 @implementer(IUserFactoryPlugin)
 class PloneUserFactory(BasePlugin):
-
     security = ClassSecurityInfo()
     meta_type = "Plone User Factory"
 
     def __init__(self, id, title=""):
         self.id = id
         self.title = title or self.meta_type
 
@@ -46,15 +45,14 @@
         return PloneUser(user_id, name)
 
 
 InitializeClass(PloneUserFactory)
 
 
 class PloneUser(PropertiedUser):
-
     security = ClassSecurityInfo()
 
     #################################
     # GRUF API
     _isGroup = False
 
     def __init__(self, id, login=None):
@@ -201,15 +199,15 @@
             properties = kw
 
         for sheet in self.getOrderedPropertySheets():
             if not IMutablePropertySheet.providedBy(sheet):
                 continue
 
             update = {}
-            for (key, value) in list(properties.items()):
+            for key, value in list(properties.items()):
                 if sheet.hasProperty(key):
                     update[key] = value
                     del properties[key]
 
             if update:
                 sheet.setProperties(self, update)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/plugins/user.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/plugins/user.py`

 * *Files 0% similar despite different names*

```diff
@@ -44,15 +44,15 @@
 
     meta_type = "User Manager"
     security = ClassSecurityInfo()
 
     @security.protected(ManageUsers)
     def addUser(self, user_id, login_name, password):
         """Original ZODBUserManager.addUser, modified to check if
-        incoming password is already encypted.
+        incoming password is already encrypted.
 
         This support clean migration from default user source.
         Should go into PAS.
         """
         if self._user_passwords.get(user_id) is not None:
             raise KeyError("Duplicate user ID: %s" % user_id)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/profiles.zcml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/profiles.zcml`

 * *Files 3% similar despite different names*

```diff
@@ -1,38 +1,41 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
-    i18n_domain="plonepas">
+    i18n_domain="plonepas"
+    >
 
   <genericsetup:registerProfile
       name="PlonePAS"
       title="PlonePAS"
-      directory="profiles/default"
       description="Extension profile for default PlonePAS setup."
       provides="Products.GenericSetup.interfaces.EXTENSION"
+      directory="profiles/default"
       />
   <genericsetup:importStep
+      name="plonepas"
+      title="PlonePAS setup"
       description="Configure PlonePas"
       handler="Products.PlonePAS.setuphandlers.setupPlonePAS"
-      name="plonepas"
-      title="PlonePAS setup">
+      >
     <depends name="componentregistry" />
     <depends name="controlpanel" />
     <depends name="memberdata-properties" />
     <depends name="rolemap" />
   </genericsetup:importStep>
   <genericsetup:upgradeStep
       title="Fix existing broken Zope root `/acl_users` plugins"
       profile="Products.PlonePAS:PlonePAS"
       source="4"
       destination="5"
-      handler=".upgrades.from4to5_fix_zope_root" />
+      handler=".upgrades.from4to5_fix_zope_root"
+      />
 
   <genericsetup:registerProfile
       name="root-cookie"
       title="Zope Root Cookie Login"
-      description="Change the Zope root `/acl_users` to use a simple cookie login form
-		   instead of HTTP `Basic ...` for authentication."
+      description="Change the Zope root `/acl_users` to use a simple cookie login form      instead of HTTP `Basic ...` for authentication."
       provides="Products.GenericSetup.interfaces.EXTENSION"
-      post_handler=".setuphandlers.set_up_zope_root_cookie_auth" />
+      post_handler=".setuphandlers.set_up_zope_root_cookie_auth"
+      />
 
 </configure>
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/setuphandlers.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/setuphandlers.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,31 +1,30 @@
 """
 Custom GenericSetup import steps for PAS in Plone.
 """
 
 from Acquisition import aq_base
 from Acquisition import aq_parent
+from plone.base.interfaces.siteroot import IPloneSiteRoot
 from plone.session.plugins.session import manage_addSessionPlugin
 from Products.CMFCore.utils import getToolByName
-from Products.CMFPlone import interfaces as plone_ifaces
 from Products.PlonePAS import config
 from Products.PlonePAS.interfaces import group as igroup
 from Products.PlonePAS.interfaces.plugins import ILocalRolesPlugin
 from Products.PlonePAS.interfaces.plugins import IUserIntrospection
 from Products.PlonePAS.interfaces.plugins import IUserManagement
 from Products.PlonePAS.plugins import cookie_handler
 from Products.PluggableAuthService.Extensions.upgrade import replace_acl_users
 from Products.PluggableAuthService.interfaces.authservice import IPluggableAuthService
 from Products.PluggableAuthService.interfaces.plugins import IChallengePlugin
 from Products.PluggableAuthService.interfaces.plugins import ICredentialsResetPlugin
 from Products.PluggableAuthService.plugins import CookieAuthHelper
 from Products.PluggableAuthService.plugins.RecursiveGroupsPlugin import (
     addRecursiveGroupsPlugin,
 )
-from zope import component
 
 import logging
 
 
 logger = logging.getLogger("PlonePAS setup")
 
 
@@ -71,15 +70,14 @@
     pas.plugins._plugin_types = plugin_types
 
     # It's safe to assign over a existing key here.
     pas.plugins._plugin_type_info[plugin_type] = plugin_info
 
 
 def registerPluginTypes(pas):
-
     PluginInfo = {
         "id": "IUserManagement",
         "title": "user_management",
         "description": (
             "The User Management plugins allow the "
             "Pluggable Auth Service to add/delete/modify users"
         ),
@@ -215,15 +213,15 @@
     cookie_name = "__ac"
 
     crumbler = getToolByName(portal, "cookie_authentication", None)
     if crumbler is not None:
         login_path = crumbler.auto_login_page
         cookie_name = crumbler.auth_cookie
 
-    is_plone_site = plone_ifaces.IPloneSiteRoot.providedBy(portal)
+    is_plone_site = IPloneSiteRoot.providedBy(portal)
     if is_plone_site:
         cookie_meta_type = cookie_handler.ExtendedCookieAuthHelper.meta_type
         add_cookie_plugin = plone_pas.manage_addExtendedCookieAuthHelper
     else:
         # Can't use the `ExtendedCookieAuthHelper` outside of a Plone portal.
         cookie_meta_type = CookieAuthHelper.CookieAuthHelper.meta_type
         add_cookie_plugin = pas.addCookieAuthHelper
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/sheet.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/sheet.py`

 * *Files 1% similar despite different names*

```diff
@@ -40,15 +40,17 @@
 
 
 PropertySchema = PropertySchemaTypeMap()
 PropertySchema.addType("string", lambda x: x is None or isinstance(x, str))
 PropertySchema.addType("text", lambda x: x is None or isinstance(x, str))
 PropertySchema.addType("boolean", lambda x: 1)  # anything can be boolean
 PropertySchema.addType("int", lambda x: x is None or isinstance(x, int))
-PropertySchema.addType("long", lambda x: x is None or isinstance(x, int))  # theres is no long in Python 3
+PropertySchema.addType(
+    "long", lambda x: x is None or isinstance(x, int)
+)  # there's is no long in Python 3
 PropertySchema.addType("float", lambda x: x is None or isinstance(x, float))
 PropertySchema.addType("lines", lambda x: x is None or isinstance(x, (tuple, list)))
 PropertySchema.addType("selection", lambda x: x is None or isinstance(x, str))
 PropertySchema.addType(
     "multiple selection", lambda x: x is None or isinstance(x, (tuple, list))
 )
 PropertySchema.addType("date", lambda x: 1)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/testing.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/testing.py`

 * *Files 7% similar despite different names*

```diff
@@ -6,38 +6,37 @@
 from plone.app.testing import TEST_USER_ID
 from plone.testing import zope as zope_testing
 
 import Products.PlonePAS
 
 
 class ProductsPlonepasLayer(PloneSandboxLayer):
-
     defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)
 
     def setUpZope(self, app, configurationContext):
         # Load any other ZCML that is required for your tests.
         # The z3c.autoinclude feature is disabled in the Plone fixture base
         # layer.
         self.loadZCML(package=Products.PlonePAS)
         zope_testing.installProduct(app, "Products.PlonePAS")
 
     def setUpPloneSite(self, portal):
         applyProfile(portal, "Products.PlonePAS:PlonePAS")
         # setRoles(portal, TEST_USER_ID, ['Manager'])
-        from Products.CMFPlone.utils import _createObjectByType
+        from plone.base.utils import unrestricted_construct_instance
 
-        _createObjectByType("Folder", portal, id="Members")
+        unrestricted_construct_instance("Folder", portal, id="Members")
         mtool = portal.portal_membership
         if not mtool.getMemberareaCreationFlag():
             mtool.setMemberareaCreationFlag()
         mtool.createMemberArea(TEST_USER_ID)
         if mtool.getMemberareaCreationFlag():
             mtool.setMemberareaCreationFlag()
 
-        _createObjectByType("Folder", portal, id="folder")
+        unrestricted_construct_instance("Folder", portal, id="folder")
 
 
 PRODUCTS_PLONEPAS_FIXTURE = ProductsPlonepasLayer()
 
 
 PRODUCTS_PLONEPAS_INTEGRATION_TESTING = IntegrationTesting(
     bases=(PRODUCTS_PLONEPAS_FIXTURE,),
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/cookie_auth.rst` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/cookie_auth.rst`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/dummy.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/dummy.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from io import BytesIO
 from OFS.SimpleItem import SimpleItem
 from ZPublisher.HTTPRequest import FileUpload
 
 import typing
 
+
 TEXT = b"file data"
 
 
 class FieldStorage:
     def __init__(self, file, filename="testfile", headers=None):
         self.file = file
         if headers is None:
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/test.gif` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/test.gif`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/images/test.jpg` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/images/test.jpg`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_basic_ops.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_basic_ops.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 from zope.component import adapter
 from zope.component import getGlobalSiteManager
 
 import unittest
 
 
 class BasicOpsTestCase(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
         self.acl_users = self.portal.acl_users
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_groupdatatool.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_groupdatatool.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,22 +5,21 @@
 from plone.app.testing import TEST_USER_ID
 from plone.app.testing import TEST_USER_NAME
 from Products.PlonePAS.testing import PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
 import unittest
 
 
-def sortTuple(t):
-    l = list(t)
-    l.sort()
-    return tuple(l)
+def sortTuple(a_tuple):
+    a_list = list(a_tuple)
+    a_list.sort()
+    return tuple(a_list)
 
 
 class TestGroupDataTool(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.acl_users = self.portal.acl_users
         self.groups = self.portal.portal_groups
         self.groupdata = self.portal.portal_groupdata
@@ -36,15 +35,14 @@
         g = self.groupdata.wrapGroup(g)
         self.assertEqual(g.__class__.__name__, "GroupData")
         self.assertEqual(aq_parent(g).__class__.__name__, "PloneGroup")
         self.assertEqual(aq_parent(aq_parent(g)).__class__.__name__, "GroupManager")
 
 
 class TestGroupData(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.memberdata = self.portal.portal_memberdata
         self.acl_users = self.portal.acl_users
@@ -149,15 +147,14 @@
         g = self.groups.getGroupById("foo")
         self.groups.editGroup(g.getId(), roles=["Member"])
         g = self.groups.getGroupById("foo")
         self.assertTrue(g.has_role("Member"))
 
 
 class TestMethodProtection(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.groups = self.portal.portal_groups
         self.groups.addGroup("foo")
         self.groupdata = self.groups.getGroupById("foo")
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_groupstool.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_groupstool.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,22 +12,21 @@
 from Products.PluggableAuthService.interfaces.events import IGroupDeletedEvent
 from zope.component import adapter
 from zope.component import getGlobalSiteManager
 
 import unittest
 
 
-def sortTuple(t):
-    l = list(t)
-    l.sort()
-    return tuple(l)
+def sortTuple(a_tuple):
+    a_list = list(a_tuple)
+    a_list.sort()
+    return tuple(a_list)
 
 
 class TestGroupsTool(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.gt = getToolByName(self.portal, "portal_groups")
         self.gd = getToolByName(self.portal, "portal_groupdata")
 
@@ -115,15 +114,14 @@
     def testManagerRemoveMember(self):
         self.portal.manage_role("Member", [Permissions.manage_users])
         self.groupdata.addMember(TEST_USER_ID)
         self.groupdata.removeMember(TEST_USER_ID)
 
 
 class TestGroupsToolIntegration(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.acl_users = self.portal.acl_users
         self.groups = self.portal.portal_groups
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_memberdatatool.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_memberdatatool.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,14 @@
 from zope.component import getGlobalSiteManager
 from zope.component import getMultiAdapter
 
 import unittest
 
 
 class TestMemberDataTool(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.memberdata = self.portal.portal_memberdata
         self.membership = self.portal.portal_membership
         self.membership.memberareaCreationFlag = 0
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_membershiptool.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_membershiptool.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,14 @@
 from zope.component import getGlobalSiteManager
 
 import os
 import unittest
 
 
 class MembershipToolTest(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.mt = getToolByName(self.portal, "portal_membership")
         self.md = getToolByName(self.portal, "portal_memberdata")
 
@@ -131,15 +130,14 @@
             self.assertTrue(aa == cc)
         cleaned = cleanId("abc")
         self.assertEqual(cleaned, "abc")
         self.assertTrue(isinstance(cleaned, str))
 
 
 class MemberAreaTest(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.mt = getToolByName(self.portal, "portal_membership")
         self.md = getToolByName(self.portal, "portal_memberdata")
         # Enable member-area creation
@@ -178,15 +176,14 @@
 
         self.mt.memberareaCreationFlag = 0
         self.mt.createMemberArea("bar")
         self.assertFalse("bar" in self.portal.Members)
 
 
 class TestMembershipTool(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.groups = self.portal.portal_groups
         self.folder = self.portal["folder"]
@@ -683,24 +680,23 @@
         def got_credentials_updated_event(event):
             events_fired.append(event)
 
         gsm = getGlobalSiteManager()
         gsm.registerHandler(got_credentials_updated_event)
 
         self.assertTrue(self.membership.testCurrentPassword(TEST_USER_PASSWORD))
-        self.assertFalse(self.membership.testCurrentPassword("whoknows"))
+        self.assertFalse(self.membership.testCurrentPassword("who-knows"))
         login(self.portal, TEST_USER_NAME)  # Back to normal
-        self.membership.setPassword("guessagain")
+        self.membership.setPassword("guess-again")
         self.assertEqual(len(events_fired), 1)
         self.assertEqual(events_fired[0].principal.getId(), TEST_USER_ID)
-        self.assertEqual(events_fired[0].password, "guessagain")
+        self.assertEqual(events_fired[0].password, "guess-again")
 
 
 class TestCreateMemberarea(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.membership.addMember("user2", "secret", ["Member"], [])
 
@@ -775,15 +771,14 @@
         memberfolder = self.membership.getHomeFolder("user2")
         self.assertFalse(
             memberfolder, "createMemberarea created memberarea despite flag"
         )
 
 
 class TestMemberareaSetup(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.membership.addMember("user2", "secret", ["Member"], [])
         self.membership.createMemberarea("user2")
@@ -819,15 +814,14 @@
     def testHomePageNotExists(self):
         if self.membership.memberareaCreationFlag is True:
             # Should not have an index_html document anymore
             self.assertFalse("index_html" in self.home)
 
 
 class TestSearchForMembers(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.memberdata = self.portal.portal_memberdata
         self.membership = self.portal.portal_membership
         # Don't let default_user disturb results
@@ -963,15 +957,14 @@
         exec(
             "def testMemberAccessible_%s(self):"
             "    self.membership.restrictedTraverse('%s')" % (method, method)
         )
 
 
 class TestMemberInfoView(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.membership = self.portal.portal_membership
         self.view = PASMemberView(self.portal, self.portal.REQUEST)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_properties.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_properties.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 from Products.PlonePAS.testing import PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 from Products.PluggableAuthService.interfaces.plugins import IUserEnumerationPlugin
 
 import unittest
 
 
 class PropertiesTest(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
 
     def test_user_properties(self):
         mt = getToolByName(self.portal, "portal_membership")
@@ -200,15 +199,14 @@
         self.assertEqual(
             sheet.propertyInfo("city"), {"type": "str", "id": "city", "mode": ""}
         )
         self.assertEqual(sheet.getProperty("addresses"), ("Here", "There"))
 
 
 class PropertySearchTest(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.mt = getToolByName(self.portal, "portal_membership")
         self.md = getToolByName(self.portal, "portal_memberdata")
         self.gt = getToolByName(self.portal, "portal_groups")
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_role_plugin.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_role_plugin.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,26 +17,24 @@
 @implementer(IGroupsPlugin)
 class FauxGroupsPlugin(BasePlugin):
     def getGroupsForPrincipal(self, principal, request=None):
         return principal._groups
 
 
 class GroupAwareRoleManagerTests(unittest.TestCase):
-    """Roles manager that takes care of goup of principal"""
+    """Roles manager that takes care of group of principal"""
 
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def _getTargetClass(self):
-
         from Products.PlonePAS.plugins.role import GroupAwareRoleManager
 
         return GroupAwareRoleManager
 
     def _makeOne(self, id="test", *args, **kw):
-
         plugin = self._getTargetClass()(id=id, *args, **kw)
         # We need to bind a fake request to this plugin
         request, dummy_response = makeRequestAndResponse()
         setattr(plugin, "REQUEST", request)
         return plugin
 
     def test_roles_for_control_panel(self):
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_setup.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tests/test_views.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tests/test_views.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 from Products.PlonePAS.testing import PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
 import unittest
 
 
 class TestPASSearchView(unittest.TestCase):
-
     layer = PRODUCTS_PLONEPAS_INTEGRATION_TESTING
 
     def test_sort(self):
         self.portal = self.layer["portal"]
         pas_search = self.portal.restrictedTraverse("@@pas_search")
         values = [
             {"title": "Sociologie"},
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tool.gif` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tool.gif`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/groupdata.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/groupdata.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,15 +98,14 @@
 
 InitializeClass(GroupDataTool)
 registerToolInterface("portal_groupdata", IGroupDataTool)
 
 
 @implementer(IGroupData, IManageCapabilities)
 class GroupData(SimpleItem):
-
     security = ClassSecurityInfo()
 
     id = None
     _tool = None
 
     def __init__(self, tool, id):
         self.id = id
@@ -225,15 +224,15 @@
             return True
 
         # Is explicitly mentioned as a group administrator?
         managers = self.getProperty("delegated_group_member_managers", ())
         if user.getId() in managers:
             return True
 
-        # Belongs to a group which is explicitly mentionned as a group
+        # Belongs to a group which is explicitly mentioned as a group
         # administrator
         meth = getattr(user, "getAllGroupNames", None)
         if meth:
             groups = meth()
         else:
             groups = ()
         for v in groups:
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/groups.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/groups.py`

 * *Files 0% similar despite different names*

```diff
@@ -396,15 +396,15 @@
     def setGroupOwnership(self, group, object, REQUEST=None):
         """Make the object  'object' owned by group 'group'
         (a portal_groupdata-ish object).
 
         For GRUF this is easy. Others may have to re-implement."""
         user = group.getGroup()
         if user is None:
-            raise ValueError("Invalid group: '{}'.".format(group))
+            raise ValueError(f"Invalid group: '{group}'.")
         object.changeOwnership(user)
         object.manage_setLocalRoles(user.getId(), ["Owner"])
 
     @security.private
     def wrapGroup(self, g, wrap_anon=0):
         """Sets up the correct acquisition wrappers for a group
         object and provides an opportunity for a portal_memberdata
@@ -428,15 +428,15 @@
             # Get portal_groupdata to do the wrapping.
             gd = getToolByName(parent, "portal_groupdata")
             try:
                 portal_group = gd.wrapGroup(g)
                 return portal_group
             except ConflictError:
                 raise
-            except:
+            except Exception:
                 logger.exception("Error during wrapGroup")
         # Failed.
         return g
 
 
 InitializeClass(GroupsTool)
 registerToolInterface("portal_groups", igroup.IGroupTool)
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/memberdata.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/memberdata.py`

 * *Files 0% similar despite different names*

```diff
@@ -141,15 +141,14 @@
 
             if user_wrapper is not None:
                 memberProperty = user_wrapper.getProperty
                 searched = memberProperty(search_param, None)
 
                 if searched is not None:
                     if searched.strip().lower().find(search_term) != -1:
-
                         res.append(
                             {
                                 "username": memberProperty("id"),
                                 "email": memberProperty("email", ""),
                             }
                         )
         return res
@@ -223,15 +222,14 @@
 
 InitializeClass(MemberDataTool)
 
 
 @implementer(IManageCapabilities, IMember)
 @adapter(IUser, IMemberDataTool)
 class MemberData(BaseMemberAdapter):
-
     security = ClassSecurityInfo()
 
     def __init__(self, user, tool):
         BaseMemberAdapter.__init__(self, user, tool)
         self.id = user.getId()
 
     # setProperties uses setMemberProperties. no need to override.
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/tools/membership.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/tools/membership.py`

 * *Files 1% similar despite different names*

```diff
@@ -472,15 +472,15 @@
         personal = None
         if home:
             personal = getattr(home, self.personal_id, None)
         return personal
 
     @security.public
     def getPersonalPortrait(self, id=None, verifyPermission=0):
-        """Return a members personal portait.
+        """Return a members personal portrait.
 
         Modified from CMFPlone version to URL-quote the member id.
         """
         if not id:
             id = self.getAuthenticatedMember().getId()
         safe_id = self._getSafeMemberId(id)
         membertool = getToolByName(self, "portal_memberdata")
@@ -495,28 +495,28 @@
             portal = getToolByName(self, "portal_url").getPortalObject()
             portrait = getattr(portal, default_portrait, None)
 
         return portrait
 
     @security.protected(SetOwnProperties)
     def deletePersonalPortrait(self, id=None):
-        """deletes the Portait of a member."""
+        """deletes the Portrait of a member."""
         authenticated_id = self.getAuthenticatedMember().getId()
         if not id:
             id = authenticated_id
         safe_id = self._getSafeMemberId(id)
         if id != authenticated_id and not _checkPermission(ManageUsers, self):
             raise Unauthorized
 
         membertool = getToolByName(self, "portal_memberdata")
         return membertool._deletePortrait(safe_id)
 
     @security.protected(SetOwnProperties)
     def changeMemberPortrait(self, portrait, id=None):
-        """update the portait of a member.
+        """update the portrait of a member.
 
         We URL-quote the member id if needed.
 
         Note that this method might be called by an anonymous user who
         is getting registered.  This method will then be called from
         plone.app.users and this is fine.  When called from restricted
         python code or with a curl command by a hacker, the
@@ -594,15 +594,15 @@
                 failMessage = registration.testPasswordValidity(password)
                 if failMessage is not None:
                     raise BadRequest(failMessage)
 
             if domains is None:
                 domains = []
             user = acl_users.getUserById(member.getUserId(), None)
-            # we must change the users password trough grufs changepassword
+            # we must change the users password through grufs changepassword
             # to keep her  group settings
             if hasattr(user, "changePassword"):
                 user.changePassword(password)
             else:
                 acl_users._doChangeUser(
                     member.getUserId(), password, member.getRoles(), domains
                 )
@@ -703,15 +703,15 @@
 
         if REQUEST is None:
             REQUEST = getattr(self, "REQUEST", None)
         if REQUEST is not None:
             pas = getToolByName(self, "acl_users")
             try:
                 pas.logout(REQUEST)
-            except Exception as e:
+            except Exception:
                 logger.error("Error in PAS logout()", exc_info=True)
 
             # Expire the skin cookie if it is not configured to persist
             st = getToolByName(self, "portal_skins")
             skinvar = st.getRequestVarname()
             if skinvar in REQUEST and not st.getCookiePersistence():
                 portal = getToolByName(self, "portal_url").getPortalObject()
@@ -764,15 +764,15 @@
             portrait_data = portrait.data
             if not portrait_data:
                 continue
             try:
                 PIL.Image.open(BytesIO(portrait_data))
             except ConflictError:
                 pass
-            except:
+            except Exception:
                 # Anything else we have a bad bad image and we destroy it
                 # and ask questions later.
                 portraits._delObject(member_id)
                 bad_member_ids.append(member_id)
             if not counter % TXN_THRESHOLD:
                 transaction.savepoint(optimistic=True)
             counter = counter + 1
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/upgrades.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/upgrades.py`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/utils.py` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -43,15 +43,15 @@
         >>> from Products.PlonePAS import config
         >>> import os
         >>> from io import BytesIO
         >>> from Products.PlonePAS.utils import scale_image
         >>> from PIL import Image
 
     Let's make a couple test images and see how it works (all are
-    100x100), the gif is palletted mode::
+    100x100), the gif is paletted mode::
 
         >>> pas_path = os.path.dirname(config.__file__)
         >>> pjoin = os.path.join
         >>> path = pjoin(pas_path, 'tests', 'images')
         >>> orig_jpg = open(pjoin(path, 'test.jpg'), 'rb')
         >>> orig_png = open(pjoin(path, 'test.png'), 'rb')
         >>> orig_gif = open(pjoin(path, 'test.gif'), 'rb')
@@ -145,26 +145,26 @@
     format = image.format
     mimetype = "image/%s" % format.lower()
 
     # from Archetypes ImageField
     # consider image mode when scaling
     # source images can be mode '1','L,','P','RGB(A)'
     # convert to greyscale or RGBA before scaling
-    # preserve palletted mode (but not pallette)
-    # for palletted-only image formats, e.g. GIF
+    # preserve paletted mode (but not palette)
+    # for paletted-only image formats, e.g. GIF
     # PNG compression is OK for RGBA thumbnails
     original_mode = image.mode
     if original_mode == "1":
         image = image.convert("L")
     elif original_mode == "P":
         image = image.convert("RGBA")
     # Rescale in place with an method that will not alter the aspect ratio
     # and will only shrink the image not enlarge it.
     image.thumbnail(size, resample=IMAGE_SCALE_PARAMS["algorithm"])
-    # preserve palletted mode for GIF and PNG
+    # preserve paletted mode for GIF and PNG
     if original_mode == "P" and format in ("GIF", "PNG"):
         image = image.convert("P")
     # Save
     new_file = BytesIO()
     image.save(new_file, format, quality=IMAGE_SCALE_PARAMS["quality"])
     new_file.seek(0)
     # Return the file data and the new mimetype
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/AutoGroupForm.zpt` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/PasswordPolicyForm.zpt`

 * *Files 25% similar despite different names*

```diff
@@ -1,66 +1,74 @@
 <h1 tal:replace="structure here/manage_page_header">Header</h1>
 
-<h2 tal:define="form_title string:Add Auto Group plugin"
-    tal:replace="structure here/manage_form_title">Form Title</h2>
+<h2 tal:define="
+      form_title string:Add Default Plone Password Policy plugin;
+    "
+    tal:replace="structure here/manage_form_title"
+>Form Title</h2>
 
 <p class="form-help">
-The Auto Group plugin automatically puts all authenticated users in a virtual
-group.
+The Default Plone Password Policy validates passwords to be at least 5 chars long
 </p>
 
-<form action="manage_addAutoGroup" method="post">
-<table cellspacing="0" cellpadding="2" border="0">
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-label">
+<form action="manage_addPasswordPolicyPlugin"
+      method="post"
+>
+  <table border="0"
+         cellpadding="2"
+         cellspacing="0"
+  >
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-label">
     Id
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="id" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-optional">
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="id"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-optional">
     Title
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="title" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-label">
-    Group id
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="group" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-label">
-    Description
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="description" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    </td>
-    <td align="left" valign="top">
-    <div class="form-element">
-    <input class="form-element" type="submit" name="submit"
-     value=" Add " />
-    </div>
-    </td>
-  </tr>
-</table>
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="title"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-element">
+          <input class="form-element"
+                 name="submit"
+                 type="submit"
+                 value=" Add "
+          />
+        </div>
+      </td>
+    </tr>
+  </table>
 </form>
 
 <h1 tal:replace="structure here/manage_page_footer">Footer</h1>
```

#### html2text {}

```diff
@@ -1,10 +1,8 @@
 ****** Header ******
 ***** Form Title *****
-The Auto Group plugin automatically puts all authenticated users in a virtual
-group.
-Id          [id                                      ]
-Title       [title                                   ]
-Group id    [group                                   ]
-Description [description                             ]
-            [ Add ]
+The Default Plone Password Policy validates passwords to be at least 5 chars
+long
+Id    [id                                      ]
+Title [title                                   ]
+      [ Add ]
 ****** Footer ******
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/CookieCrumblingPluginForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/CookieCrumblingPluginForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/ExtendedCookieAuthHelperForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/ExtendedCookieAuthHelperForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/GroupAwareRoleManagerForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/GroupAwareRoleManagerForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/GroupManagerForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/GroupManagerForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/LocalRolesManagerForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/LocalRolesManagerForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/MutablePropertyProviderForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/MutablePropertyProviderForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/PasswordPolicyForm.zpt` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/AutoGroupForm.zpt`

 * *Files 22% similar despite different names*

```diff
@@ -1,45 +1,109 @@
 <h1 tal:replace="structure here/manage_page_header">Header</h1>
 
-<h2 tal:define="form_title string:Add Default Plone Password Policy plugin"
-    tal:replace="structure here/manage_form_title">Form Title</h2>
+<h2 tal:define="
+      form_title string:Add Auto Group plugin;
+    "
+    tal:replace="structure here/manage_form_title"
+>Form Title</h2>
 
 <p class="form-help">
-The Default Plone Password Policy validates passwords to be at least 5 chars long
+The Auto Group plugin automatically puts all authenticated users in a virtual
+group.
 </p>
 
-<form action="manage_addPasswordPolicyPlugin" method="post">
-<table cellspacing="0" cellpadding="2" border="0">
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-label">
+<form action="manage_addAutoGroup"
+      method="post"
+>
+  <table border="0"
+         cellpadding="2"
+         cellspacing="0"
+  >
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-label">
     Id
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="id" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    <div class="form-optional">
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="id"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-optional">
     Title
-    </div>
-    </td>
-    <td align="left" valign="top">
-    <input type="text" name="title" size="40" />
-    </td>
-  </tr>
-  <tr>
-    <td align="left" valign="top">
-    </td>
-    <td align="left" valign="top">
-    <div class="form-element">
-    <input class="form-element" type="submit" name="submit"
-     value=" Add " />
-    </div>
-    </td>
-  </tr>
-</table>
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="title"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-label">
+    Group id
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="group"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-label">
+    Description
+        </div>
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <input name="description"
+               size="40"
+               type="text"
+        />
+      </td>
+    </tr>
+    <tr>
+      <td align="left"
+          valign="top"
+      >
+      </td>
+      <td align="left"
+          valign="top"
+      >
+        <div class="form-element">
+          <input class="form-element"
+                 name="submit"
+                 type="submit"
+                 value=" Add "
+          />
+        </div>
+      </td>
+    </tr>
+  </table>
 </form>
 
 <h1 tal:replace="structure here/manage_page_footer">Footer</h1>
```

#### html2text {}

```diff
@@ -1,8 +1,10 @@
 ****** Header ******
 ***** Form Title *****
-The Default Plone Password Policy validates passwords to be at least 5 chars
-long
-Id    [id                                      ]
-Title [title                                   ]
-      [ Add ]
+The Auto Group plugin automatically puts all authenticated users in a virtual
+group.
+Id          [id                                      ]
+Title       [title                                   ]
+Group id    [group                                   ]
+Description [description                             ]
+            [ Add ]
 ****** Footer ******
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/PloneUserFactoryForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/PloneUserFactoryForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/UserManagerForm.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/UserManagerForm.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/membershipRolemapping.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/membershipRolemapping.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products/PlonePAS/zmi/portrait_fix.dtml` & `Products.PlonePAS-8.0.0/src/Products/PlonePAS/zmi/portrait_fix.dtml`

 * *Files identical despite different names*

### Comparing `Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/PKG-INFO` & `Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Products.PlonePAS
-Version: 7.0.0b3
+Version: 8.0.0
 Summary: PlonePAS modifies the PluggableAuthService for use by Plone.
 Home-page: https://github.com/plone/Products.PlonePAS
 Author: Kapil Thangavelu, Wichert Akkerman
 Author-email: plone-developers@lists.sourceforge.net
 License: ZPL
 Keywords: Zope CMF Plone PAS authentication
 Classifier: Development Status :: 5 - Production/Stable
@@ -14,14 +14,16 @@
 Classifier: Framework :: Zope
 Classifier: Framework :: Zope :: 5
 Classifier: License :: OSI Approved :: Zope Public License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Python: >=3.8
 Provides-Extra: test
 
 Overview
 ========
 
 This product extends `PluggableAuthService <https://github.com/zopefoundation/Products.PluggableAuthService>`_ (PAS) for use in Plone.
 
@@ -75,27 +77,27 @@
 
 Initial creation: The PAS CIGNEX Sprint Team [ Anders, Bob, Ben,
 Chad, Gautham, Joel, Kapil, Michel, Micheal ]
 
 Post-sprint work: J Cameron Cooper, Leo, Sidnei, Mark at `Enfold
 Systems <http://enfoldsystems.com>`_
 
-Basic setAuthCookie support (to mimick CookieCrumbler):
+Basic setAuthCookie support (to mimic CookieCrumbler):
 Rocky Burt at `ServerZen Software <http://www.serverzen.com>`_
 
 Synced login process with Plone:
 Dorneles Tremea at `PloneSolutions <http://plonesolutions.com>`_
 
 Bugfixes, various development and merging with Plone:
 Wichert Akkerman at Simplon
 
 Bugfixes, improvements to membership and property lookups:
 Eric Steele and Erik Rose
 
-Review, cleanup, modernize code, adressing Plone 5:
+Review, cleanup, modernize code, addressing Plone 5:
 Jens Klein, BlueDynamics Alliance - `Klein & Partner KG <http://kleinundpartner.at>`_
 
 Source Code
 -----------
 
 Contributors please read the document `Process for Plone core's development <https://docs.plone.org/develop/coredev/docs/index.html>`_
 
@@ -107,14 +109,41 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+8.0.0 (2023-04-06)
+------------------
+
+Breaking changes:
+
+
+- Remove `ldapmp` module. It is not being tested in Plone 6.
+  See https://github.com/plone/Products.PlonePAS/pull/71#pullrequestreview-1351349950
+  [gforcada] (#1)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (80cf330f)
+
+
+7.0.0 (2022-12-02)
+------------------
+
+Bug fixes:
+
+
+- Final release for Plone 6.0.0 (#600)
+
+
 7.0.0b3 (2022-10-11)
 --------------------
 
 Bug fixes:
 
 
 - Fix admin password used in tests. [davisagli] (#70)
@@ -435,22 +464,22 @@
 ------------------
 
 - Add a integrated test setup with codeanalysis and travis. For this moved
   ``Products`` folder to a ``src`` folder in order to follow the package
   structure expected by ``buildout.plonetest``'s ``qa.cfg``.
   [jensens]
 
-- Make patching of LDAPMultiPlugin explizit. Code using those must call
+- Make patching of LDAPMultiPlugin explicit. Code using those must call
   ``Products.PlonePAS.ldapmp.patch_ldapmp`` with no parameters in order
   to activate the patches.
   [jensens]
 
 - Removed (optional) Archetypes Storage (used in past with CMFMember, which
-  itself was long time ago superseeded by Membrane). Probably dead code. If
-  theres someone out there needing it in Plone 5 please copy the code from
+  itself was long time ago superseded by Membrane). Probably dead code. If
+  there's someone out there needing it in Plone 5 please copy the code from
   git/Plone4 in your addon/project.
   [jensens]
 
 - Moved ``Extensions/Install.py`` functions to setuphandlers, kept BBB import
   for ``activatePluginInterfaces`` since this is imported by ``borg.localrole``.
   [jensens]
 
@@ -697,15 +726,15 @@
 
 - Made last_login_time logic compatible with DateTime 2.12.5.
   [hannosch]
 
 4.0.1 - 2010-07-31
 ------------------
 
-- Clean up some unused imports and variable assigments.
+- Clean up some unused imports and variable assignments.
   [esteele]
 
 - Stop looking to GRUF to check if group properties can be edited.
   [esteele]
 
 4.0 - 2010-07-18
 ----------------
@@ -1320,15 +1349,15 @@
   as GRUF itself uses.
   [mj]
 
 - Fix migration to handle properties of selection or multiple selection
   types.
   [reinout]
 
-- Correct creation of groups wich default group managers.
+- Correct creation of groups which default group managers.
   [dreamcatcher]
 
 - Fix migration from GRUF sites: also include the member properties in the
   migration.
   [tesdal]
 
 - Correct the test for creation of groups with the same id as users: search
```

### Comparing `Products.PlonePAS-7.0.0b3/src/Products.PlonePAS.egg-info/SOURCES.txt` & `Products.PlonePAS-8.0.0/src/Products.PlonePAS.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,21 @@
+.editorconfig
 .gitignore
+.meta.toml
+.pre-commit-config.yaml
 CHANGES.rst
 CONTRIBUTING.rst
 MANIFEST.in
 README.rst
 buildout.cfg
 mypy.ini
 pyproject.toml
 setup.cfg
 setup.py
+tox.ini
 docs/LICENSE.ZPL
 docs/STATUS.txt
 docs/TODO.txt
 docs/copyright-and-license.txt
 docs/pas-dev.txt
 docs/scratchpad.txt
 src/Products/__init__.py
@@ -23,15 +27,14 @@
 src/Products.PlonePAS.egg-info/requires.txt
 src/Products.PlonePAS.egg-info/top_level.txt
 src/Products/PlonePAS/__init__.py
 src/Products/PlonePAS/config.py
 src/Products/PlonePAS/configure.zcml
 src/Products/PlonePAS/events.py
 src/Products/PlonePAS/exportimport.zcml
-src/Products/PlonePAS/ldapmp.py
 src/Products/PlonePAS/pas.py
 src/Products/PlonePAS/patch.py
 src/Products/PlonePAS/permissions.py
 src/Products/PlonePAS/profiles.zcml
 src/Products/PlonePAS/setuphandlers.py
 src/Products/PlonePAS/sheet.py
 src/Products/PlonePAS/testing.py
```

