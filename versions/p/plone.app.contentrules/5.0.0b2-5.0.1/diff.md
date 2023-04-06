# Comparing `tmp/plone.app.contentrules-5.0.0b2.tar.gz` & `tmp/plone.app.contentrules-5.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plone.app.contentrules-5.0.0b2.tar", last modified: Thu Jul 14 09:16:13 2022, max compression
+gzip compressed data, was "plone.app.contentrules-5.0.1.tar", last modified: Thu Apr  6 10:30:51 2023, max compression
```

## Comparing `plone.app.contentrules-5.0.0b2.tar` & `plone.app.contentrules-5.0.1.tar`

### file list

```diff
@@ -1,117 +1,117 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.455911 plone.app.contentrules-5.0.0b2/
--rw-r--r--   0 maurits    (501) staff       (20)    19772 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/CHANGES.rst
--rw-r--r--   0 maurits    (501) staff       (20)       70 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)      148 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)    21200 2022-07-14 09:16:13.456121 plone.app.contentrules-5.0.0b2/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)      527 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/README.rst
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.432201 plone.app.contentrules-5.0.0b2/docs/
--rw-r--r--   0 maurits    (501) staff       (20)    15220 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/docs/LICENSE.GPL
--rw-r--r--   0 maurits    (501) staff       (20)      684 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/docs/LICENSE.txt
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.432457 plone.app.contentrules-5.0.0b2/plone/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.434611 plone.app.contentrules-5.0.0b2/plone/app/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.436406 plone.app.contentrules-5.0.0b2/plone/app/contentrules/
--rw-r--r--   0 maurits    (501) staff       (20)      162 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.438953 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/
--rw-r--r--   0 maurits    (501) staff       (20)     1923 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     7256 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     4835 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/copy.py
--rw-r--r--   0 maurits    (501) staff       (20)     2197 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/delete.py
--rw-r--r--   0 maurits    (501) staff       (20)     4143 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/logger.py
--rw-r--r--   0 maurits    (501) staff       (20)     7164 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/mail.py
--rw-r--r--   0 maurits    (501) staff       (20)     5694 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/move.py
--rw-r--r--   0 maurits    (501) staff       (20)     2887 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/notify.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.439227 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/templates/
--rw-r--r--   0 maurits    (501) staff       (20)     1063 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/templates/mail.pt
--rw-r--r--   0 maurits    (501) staff       (20)     2850 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/versioning.py
--rw-r--r--   0 maurits    (501) staff       (20)     3558 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/workflow.py
--rw-r--r--   0 maurits    (501) staff       (20)     2391 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/api.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.442532 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/
--rw-r--r--   0 maurits    (501) staff       (20)        2 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3803 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/adding.py
--rw-r--r--   0 maurits    (501) staff       (20)     7175 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/assignments.py
--rw-r--r--   0 maurits    (501) staff       (20)     5896 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     5294 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/controlpanel.py
--rw-r--r--   0 maurits    (501) staff       (20)     8506 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/elements.py
--rw-r--r--   0 maurits    (501) staff       (20)     5139 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/formhelper.py
--rw-r--r--   0 maurits    (501) staff       (20)      842 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/info.py
--rw-r--r--   0 maurits    (501) staff       (20)      989 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/interfaces.py
--rw-r--r--   0 maurits    (501) staff       (20)      827 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/navigation.py
--rw-r--r--   0 maurits    (501) staff       (20)     1895 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/rule.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.443636 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/
--rw-r--r--   0 maurits    (501) staff       (20)      880 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/contentrules-pageform.pt
--rw-r--r--   0 maurits    (501) staff       (20)    10873 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/controlpanel.pt
--rw-r--r--   0 maurits    (501) staff       (20)    14097 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/manage-assignments.pt
--rw-r--r--   0 maurits    (501) staff       (20)    16953 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/manage-elements.pt
--rw-r--r--   0 maurits    (501) staff       (20)     2166 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/traversal.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.446004 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     7488 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     3435 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/fileextension.py
--rw-r--r--   0 maurits    (501) staff       (20)     3313 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/group.py
--rw-r--r--   0 maurits    (501) staff       (20)     3773 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/portaltype.py
--rw-r--r--   0 maurits    (501) staff       (20)     3170 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/role.py
--rw-r--r--   0 maurits    (501) staff       (20)     3439 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/talesexpression.py
--rw-r--r--   0 maurits    (501) staff       (20)     3201 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/wfstate.py
--rw-r--r--   0 maurits    (501) staff       (20)     3148 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/wftransition.py
--rw-r--r--   0 maurits    (501) staff       (20)     5302 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/configure.zcml
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.446977 plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      940 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)      745 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/interfaces.py
--rw-r--r--   0 maurits    (501) staff       (20)    13690 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/rules.py
--rw-r--r--   0 maurits    (501) staff       (20)     6058 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/handlers.py
--rw-r--r--   0 maurits    (501) staff       (20)      704 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/namechooser.py
--rw-r--r--   0 maurits    (501) staff       (20)     3139 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/rule.py
--rw-r--r--   0 maurits    (501) staff       (20)      963 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/testing.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.454973 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     4025 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/assignment.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1403 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/base.py
--rw-r--r--   0 maurits    (501) staff       (20)      761 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/dummy.py
--rw-r--r--   0 maurits    (501) staff       (20)     4021 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/multipublish.txt
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.429867 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.455720 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/
--rw-r--r--   0 maurits    (501) staff       (20)     3986 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/contentrules.xml
--rw-r--r--   0 maurits    (501) staff       (20)      241 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/export_steps.xml
--rw-r--r--   0 maurits    (501) staff       (20)      308 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/import_steps.xml
--rw-r--r--   0 maurits    (501) staff       (20)     3447 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/simplepublish.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4683 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_copy.py
--rw-r--r--   0 maurits    (501) staff       (20)     1984 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_delete.py
--rw-r--r--   0 maurits    (501) staff       (20)     3524 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_logger.py
--rw-r--r--   0 maurits    (501) staff       (20)     9646 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_mail.py
--rw-r--r--   0 maurits    (501) staff       (20)     1079 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_modify.py
--rw-r--r--   0 maurits    (501) staff       (20)     5419 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_move.py
--rw-r--r--   0 maurits    (501) staff       (20)     2686 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_notify.py
--rw-r--r--   0 maurits    (501) staff       (20)     2757 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_versioning.py
--rw-r--r--   0 maurits    (501) staff       (20)     3068 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_workflow.py
--rw-r--r--   0 maurits    (501) staff       (20)      663 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_browser.py
--rw-r--r--   0 maurits    (501) staff       (20)     1654 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_cascading_rule.py
--rw-r--r--   0 maurits    (501) staff       (20)     2588 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_group.py
--rw-r--r--   0 maurits    (501) staff       (20)     2809 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_portal_type.py
--rw-r--r--   0 maurits    (501) staff       (20)     2479 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_role.py
--rw-r--r--   0 maurits    (501) staff       (20)     3086 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_tales_expression.py
--rw-r--r--   0 maurits    (501) staff       (20)     2749 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_wfstate.py
--rw-r--r--   0 maurits    (501) staff       (20)     3441 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_wftransition.py
--rw-r--r--   0 maurits    (501) staff       (20)     8132 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_configuration.py
--rw-r--r--   0 maurits    (501) staff       (20)      288 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_events.py
--rw-r--r--   0 maurits    (501) staff       (20)     1652 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_handlers.py
--rw-r--r--   0 maurits    (501) staff       (20)     5781 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_rule_assignment_mapping.py
--rw-r--r--   0 maurits    (501) staff       (20)     6124 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_rule_management_views.py
--rw-r--r--   0 maurits    (501) staff       (20)      857 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_setup.py
--rw-r--r--   0 maurits    (501) staff       (20)     1926 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_traversal.py
--rw-r--r--   0 maurits    (501) staff       (20)     2743 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_ui.txt
--rw-r--r--   0 maurits    (501) staff       (20)      510 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/testing.zcml
--rw-r--r--   0 maurits    (501) staff       (20)      155 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/utils.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-07-14 09:16:13.434357 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)    21200 2022-07-14 09:16:12.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     4398 2022-07-14 09:16:13.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-07-14 09:16:12.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/dependency_links.txt
--rw-r--r--   0 maurits    (501) staff       (20)       16 2022-07-14 09:16:13.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-07-14 09:16:12.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)      472 2022-07-14 09:16:13.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        6 2022-07-14 09:16:13.000000 plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/top_level.txt
--rw-r--r--   0 maurits    (501) staff       (20)      397 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)      243 2022-07-14 09:16:13.456660 plone.app.contentrules-5.0.0b2/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)     2058 2022-07-14 09:16:11.000000 plone.app.contentrules-5.0.0b2/setup.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.045786 plone.app.contentrules-5.0.1/
+-rw-r--r--   0 maurits    (501) staff       (20)    20132 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       70 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      148 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)    21633 2023-04-06 10:30:51.045964 plone.app.contentrules-5.0.1/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)      527 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/README.rst
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.016489 plone.app.contentrules-5.0.1/docs/
+-rw-r--r--   0 maurits    (501) staff       (20)    15220 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/docs/LICENSE.GPL
+-rw-r--r--   0 maurits    (501) staff       (20)      684 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/docs/LICENSE.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.016800 plone.app.contentrules-5.0.1/plone/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.019476 plone.app.contentrules-5.0.1/plone/app/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.021894 plone.app.contentrules-5.0.1/plone/app/contentrules/
+-rw-r--r--   0 maurits    (501) staff       (20)      162 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.024976 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/
+-rw-r--r--   0 maurits    (501) staff       (20)     1923 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6880 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     4835 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/copy.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2197 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/delete.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4143 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/logger.py
+-rw-r--r--   0 maurits    (501) staff       (20)     7188 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/mail.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5694 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/move.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2887 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/notify.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.025279 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/templates/
+-rw-r--r--   0 maurits    (501) staff       (20)     1172 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/templates/mail.pt
+-rw-r--r--   0 maurits    (501) staff       (20)     2850 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/versioning.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3558 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/actions/workflow.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2391 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/api.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.028904 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/
+-rw-r--r--   0 maurits    (501) staff       (20)        2 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3799 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/adding.py
+-rw-r--r--   0 maurits    (501) staff       (20)     7174 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/assignments.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5827 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     5294 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/controlpanel.py
+-rw-r--r--   0 maurits    (501) staff       (20)     8506 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/elements.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5139 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/formhelper.py
+-rw-r--r--   0 maurits    (501) staff       (20)      842 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/info.py
+-rw-r--r--   0 maurits    (501) staff       (20)      990 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/interfaces.py
+-rw-r--r--   0 maurits    (501) staff       (20)      827 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/navigation.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1895 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/rule.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.030122 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/
+-rw-r--r--   0 maurits    (501) staff       (20)      968 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/contentrules-pageform.pt
+-rw-r--r--   0 maurits    (501) staff       (20)    14016 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/controlpanel.pt
+-rw-r--r--   0 maurits    (501) staff       (20)    14486 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/manage-assignments.pt
+-rw-r--r--   0 maurits    (501) staff       (20)    15756 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/manage-elements.pt
+-rw-r--r--   0 maurits    (501) staff       (20)     2166 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/browser/traversal.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.033037 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     7283 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     3435 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/fileextension.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3313 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/group.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3773 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/portaltype.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3170 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/role.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3439 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/talesexpression.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3201 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/wfstate.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3148 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/wftransition.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5009 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/configure.zcml
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.034212 plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      891 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      745 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/interfaces.py
+-rw-r--r--   0 maurits    (501) staff       (20)    13594 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/rules.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6057 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/handlers.py
+-rw-r--r--   0 maurits    (501) staff       (20)      704 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/namechooser.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3137 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/rule.py
+-rw-r--r--   0 maurits    (501) staff       (20)      962 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/testing.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.044383 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4025 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/assignment.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1403 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/base.py
+-rw-r--r--   0 maurits    (501) staff       (20)      761 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/dummy.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4021 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/multipublish.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.013674 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.045495 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/
+-rw-r--r--   0 maurits    (501) staff       (20)     3556 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/contentrules.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      264 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/export_steps.xml
+-rw-r--r--   0 maurits    (501) staff       (20)      346 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/import_steps.xml
+-rw-r--r--   0 maurits    (501) staff       (20)     3447 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/simplepublish.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4683 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_copy.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1821 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_delete.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3481 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_logger.py
+-rw-r--r--   0 maurits    (501) staff       (20)     9521 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_mail.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1079 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_modify.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5419 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_move.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2686 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_notify.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2757 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_versioning.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3068 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_workflow.py
+-rw-r--r--   0 maurits    (501) staff       (20)      663 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_browser.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1653 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_cascading_rule.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2588 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_group.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2809 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_portal_type.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2479 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_role.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3086 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_tales_expression.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2749 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_wfstate.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3441 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_wftransition.py
+-rw-r--r--   0 maurits    (501) staff       (20)     8131 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_configuration.py
+-rw-r--r--   0 maurits    (501) staff       (20)      288 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_events.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1652 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_handlers.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5713 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_rule_assignment_mapping.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6123 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_rule_management_views.py
+-rw-r--r--   0 maurits    (501) staff       (20)      857 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_setup.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1926 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_traversal.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2743 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_ui.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      482 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/testing.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      155 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone/app/contentrules/tests/utils.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:30:51.019145 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)    21633 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     4398 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)       16 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      485 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        6 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/top_level.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1643 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:30:51.046532 plone.app.contentrules-5.0.1/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     2204 2023-04-06 10:30:50.000000 plone.app.contentrules-5.0.1/setup.py
```

### Comparing `plone.app.contentrules-5.0.0b2/CHANGES.rst` & `plone.app.contentrules-5.0.1/CHANGES.rst`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,43 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.1 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Explicitly mark exclude_actor as not-required
+  [erral] (#77)
+- Make modal action and condition editing modal screens bigger
+  [erral] (#78)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (#47959565)
+
+
+5.0.0 (2022-11-30)
+------------------
+
+Bug fixes:
+
+
+- Final release.
+  [gforcada] (#600)
+
+
 5.0.0b2 (2022-07-14)
 --------------------
 
 Bug fixes:
 
 
 - Remove unneeded i18n:translate call
@@ -162,15 +191,15 @@
   version.
 
 Bug fixes:
 
 - Migrate all tests to use dexterity
   [pbauer]
 
-- Work around issue where new item is moved before it's completely addeed
+- Work around issue where new item is moved before it's completely added
   [davisagli]
 
 - Fix all tests with py3 and py2
   [pbauer, alert, davisagli]
 
 
 4.0.18 (2018-02-04)
@@ -380,15 +409,15 @@
 ------------------
 
 - Fixed 3.0.4 regression: add/move/remove events where not handled
   anymore on discussion items.
   [thomasdesvenain]
 
 - Fixed reordering of actions / conditions.
-  This occured when 'jq' was not defined as 'jQuery'.
+  This occurred when 'jq' was not defined as 'jQuery'.
   [thomasdesvenain]
 
 - User that manage a rule can now allow actions executed by this rule
   to recursively trigger other rules.
   For example, if you have a rule that automatically publish added content,
   and an other rule that sends an email when a content is published,
   if autopublish rule is marked as 'cascading', then send mail rule will be triggered.
@@ -523,15 +552,15 @@
 ------------------
 
 - Adding a content rule is not handled by 'added' rule...
   Fixes infinite loop on adding a content rule.
   [thomasdesvenain]
 
 - ContainerModified event is excluded from 'modified' event handling.
-  This avoids for example adding a comment to lauch 'modified' rules registered for it.
+  This avoids for example adding a comment to launch 'modified' rules registered for it.
   [thomasdesvenain]
 
 
 2.1.7 (2012-08-04)
 ------------------
 
 - Added an option in email action
```

### Comparing `plone.app.contentrules-5.0.0b2/PKG-INFO` & `plone.app.contentrules-5.0.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.contentrules
-Version: 5.0.0b2
+Version: 5.0.1
 Summary: Plone integration for plone.contentrules
 Home-page: https://pypi.org/project/plone.app.contentrules
 Author: Plone Foundation
 Author-email: plone-developers@lists.sourceforge.net
 License: GPL version 2
 Keywords: plone automatic content rules
 Classifier: Development Status :: 5 - Production/Stable
@@ -12,17 +12,19 @@
 Classifier: Framework :: Plone
 Classifier: Framework :: Plone :: 6.0
 Classifier: Framework :: Plone :: Core
 Classifier: Framework :: Zope :: 5
 Classifier: License :: OSI Approved :: GNU General Public License v2 (GPLv2)
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Python: >=3.8
 Provides-Extra: test
 
 Introduction
 ============
 
 plone.app.contentrules provides Plone-specific conditions and actions, as well
 as a user interface for plone.contentrules.
@@ -44,14 +46,43 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.1 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Explicitly mark exclude_actor as not-required
+  [erral] (#77)
+- Make modal action and condition editing modal screens bigger
+  [erral] (#78)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (#47959565)
+
+
+5.0.0 (2022-11-30)
+------------------
+
+Bug fixes:
+
+
+- Final release.
+  [gforcada] (#600)
+
+
 5.0.0b2 (2022-07-14)
 --------------------
 
 Bug fixes:
 
 
 - Remove unneeded i18n:translate call
@@ -202,15 +233,15 @@
   version.
 
 Bug fixes:
 
 - Migrate all tests to use dexterity
   [pbauer]
 
-- Work around issue where new item is moved before it's completely addeed
+- Work around issue where new item is moved before it's completely added
   [davisagli]
 
 - Fix all tests with py3 and py2
   [pbauer, alert, davisagli]
 
 
 4.0.18 (2018-02-04)
@@ -420,15 +451,15 @@
 ------------------
 
 - Fixed 3.0.4 regression: add/move/remove events where not handled
   anymore on discussion items.
   [thomasdesvenain]
 
 - Fixed reordering of actions / conditions.
-  This occured when 'jq' was not defined as 'jQuery'.
+  This occurred when 'jq' was not defined as 'jQuery'.
   [thomasdesvenain]
 
 - User that manage a rule can now allow actions executed by this rule
   to recursively trigger other rules.
   For example, if you have a rule that automatically publish added content,
   and an other rule that sends an email when a content is published,
   if autopublish rule is marked as 'cascading', then send mail rule will be triggered.
@@ -563,15 +594,15 @@
 ------------------
 
 - Adding a content rule is not handled by 'added' rule...
   Fixes infinite loop on adding a content rule.
   [thomasdesvenain]
 
 - ContainerModified event is excluded from 'modified' event handling.
-  This avoids for example adding a comment to lauch 'modified' rules registered for it.
+  This avoids for example adding a comment to launch 'modified' rules registered for it.
   [thomasdesvenain]
 
 
 2.1.7 (2012-08-04)
 ------------------
 
 - Added an option in email action
```

### Comparing `plone.app.contentrules-5.0.0b2/README.rst` & `plone.app.contentrules-5.0.1/README.rst`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/docs/LICENSE.GPL` & `plone.app.contentrules-5.0.1/docs/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/docs/LICENSE.txt` & `plone.app.contentrules-5.0.1/docs/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/__init__.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/__init__.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/configure.zcml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/configure.zcml`

 * *Files 8% similar despite different names*

```diff
@@ -1,239 +1,240 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:browser="http://namespaces.zope.org/browser"
     xmlns:plone="http://namespaces.plone.org/plone"
-    i18n_domain="plone">
+    i18n_domain="plone"
+    >
 
-    <!-- Logger action -->
+  <!-- Logger action -->
 
-    <adapter factory=".logger.LoggerActionExecutor" />
+  <adapter factory=".logger.LoggerActionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+  <browser:page
       name="plone.actions.Logger"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
       class=".logger.LoggerAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.actions.logger.ILoggerAction"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.actions.logger.ILoggerAction"
       class=".logger.LoggerEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleAction
-        name="plone.actions.Logger"
-        title="Logger"
-        description="Log a particular event"
-        for="*"
-        event="*"
-        addview="plone.actions.Logger"
-        editview="edit"
-        schema=".logger.ILoggerAction"
-        factory=".logger.LoggerAction"
-        />
-
-    <!-- Notify action -->
-
-    <adapter factory=".notify.NotifyActionExecutor" />
-
-    <browser:page
-        for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-        name="plone.actions.Notify"
-        class=".notify.NotifyAddFormView"
-        permission="plone.app.contentrules.ManageContentRules"
-      />
-
-    <browser:page
-        for="plone.app.contentrules.actions.notify.INotifyAction"
-        name="edit"
-        class=".notify.NotifyEditFormView"
-        permission="plone.app.contentrules.ManageContentRules"
-      />
-
-    <plone:ruleAction
-        name="plone.actions.Notify"
-        title="Notify user"
-        description="Return a portal message to the user"
-        for="*"
-        event="*"
-        addview="plone.actions.Notify"
-        editview="edit"
-        schema=".notify.INotifyAction"
-        factory=".notify.NotifyAction"
-        />
-
-    <!-- Copy to folder action -->
-
-     <adapter factory=".copy.CopyActionExecutor" />
-
-     <browser:page
-       for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-       name="plone.actions.Copy"
-       class=".copy.CopyAddFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <browser:page
-       for="plone.app.contentrules.actions.copy.ICopyAction"
-       name="edit"
-       class=".copy.CopyEditFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <plone:ruleAction
-         name="plone.actions.Copy"
-         title="Copy to folder"
-         description="Copy the triggering item to a specific folder"
-         for="*"
-         event="zope.interface.interfaces.IObjectEvent"
-         addview="plone.actions.Copy"
-         editview="edit"
-         schema=".copy.ICopyAction"
-         factory=".copy.CopyAction"
-         />
-
-    <!-- Move to folder action -->
-
-     <adapter factory=".move.MoveActionExecutor" />
-
-     <browser:page
-       for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-       name="plone.actions.Move"
-       class=".move.MoveAddFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <browser:page
-       for="plone.app.contentrules.actions.move.IMoveAction"
-       name="edit"
-       class=".move.MoveEditFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <plone:ruleAction
-         name="plone.actions.Move"
-         title="Move to folder"
-         description="Move the triggering item to a specific folder"
-         for="*"
-         event="zope.interface.interfaces.IObjectEvent"
-         addview="plone.actions.Move"
-         editview="edit"
-         schema=".move.IMoveAction"
-         factory=".move.MoveAction"
-         />
-
-    <!-- Delete action (no configurable options) -->
-
-     <adapter factory=".delete.DeleteActionExecutor" />
-
-     <browser:page
-       for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-       name="plone.actions.Delete"
-       class=".delete.DeleteAddForm"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <plone:ruleAction
-         name="plone.actions.Delete"
-         title="Delete object"
-         description="Delete the triggering item"
-         for="*"
-         event="zope.interface.interfaces.IObjectEvent"
-         addview="plone.actions.Delete"
-         schema=".delete.IDeleteAction"
-         factory=".delete.DeleteAction"
-         />
-
-    <!-- Transition workflow action -->
-
-     <adapter factory=".workflow.WorkflowActionExecutor" />
-
-     <browser:page
-       for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-       name="plone.actions.Workflow"
-       class=".workflow.WorkflowAddFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <browser:page
-       for="plone.app.contentrules.actions.workflow.IWorkflowAction"
-       name="edit"
-       class=".workflow.WorkflowEditFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <plone:ruleAction
-         name="plone.actions.Workflow"
-         title="Transition workflow state"
-         description="Perform a workflow transition on the triggering object"
-         for="*"
-         event="zope.interface.interfaces.IObjectEvent"
-         addview="plone.actions.Workflow"
-         editview="edit"
-         schema=".workflow.IWorkflowAction"
-         factory=".workflow.WorkflowAction"
-         />
-
-    <!-- Email action definition -->
-
-     <adapter factory=".mail.MailActionExecutor" />
-
-     <browser:page
-       for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-       name="plone.actions.Mail"
-       class=".mail.MailAddFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <browser:page
-       for="plone.app.contentrules.actions.mail.IMailAction"
-       name="edit"
-       class=".mail.MailEditFormView"
-       permission="plone.app.contentrules.ManageContentRules"
-       />
-
-     <plone:ruleAction
-         name="plone.actions.Mail"
-         title="Send email"
-         description="Send an email on the triggering object"
-         for="*"
-         event="*"
-         addview="plone.actions.Mail"
-         editview="edit"
-         schema=".mail.IMailAction"
-         factory=".mail.MailAction"
-         />
-
-    <!-- Versioning action -->
-
-    <adapter factory=".versioning.VersioningActionExecutor" />
-
-    <browser:page
-        for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
-        name="plone.actions.Versioning"
-        class=".versioning.VersioningAddFormView"
-        permission="plone.app.contentrules.ManageContentRules"
-      />
-
-    <browser:page
-        for="plone.app.contentrules.actions.versioning.IVersioningAction"
-        name="edit"
-        class=".versioning.VersioningEditFormView"
-        permission="plone.app.contentrules.ManageContentRules"
-      />
-
-    <plone:ruleAction
-        name="plone.actions.Versioning"
-        title="Version object"
-        description="Store a new version of the object"
-        for="*"
-        event="*"
-        addview="plone.actions.Versioning"
-        editview="edit"
-        schema=".versioning.IVersioningAction"
-        factory=".versioning.VersioningAction"
-        />
+  <plone:ruleAction
+      name="plone.actions.Logger"
+      title="Logger"
+      description="Log a particular event"
+      for="*"
+      event="*"
+      schema=".logger.ILoggerAction"
+      factory=".logger.LoggerAction"
+      addview="plone.actions.Logger"
+      editview="edit"
+      />
+
+  <!-- Notify action -->
+
+  <adapter factory=".notify.NotifyActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Notify"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".notify.NotifyAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.notify.INotifyAction"
+      class=".notify.NotifyEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Notify"
+      title="Notify user"
+      description="Return a portal message to the user"
+      for="*"
+      event="*"
+      schema=".notify.INotifyAction"
+      factory=".notify.NotifyAction"
+      addview="plone.actions.Notify"
+      editview="edit"
+      />
+
+  <!-- Copy to folder action -->
+
+  <adapter factory=".copy.CopyActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Copy"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".copy.CopyAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.copy.ICopyAction"
+      class=".copy.CopyEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Copy"
+      title="Copy to folder"
+      description="Copy the triggering item to a specific folder"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".copy.ICopyAction"
+      factory=".copy.CopyAction"
+      addview="plone.actions.Copy"
+      editview="edit"
+      />
+
+  <!-- Move to folder action -->
+
+  <adapter factory=".move.MoveActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Move"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".move.MoveAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.move.IMoveAction"
+      class=".move.MoveEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Move"
+      title="Move to folder"
+      description="Move the triggering item to a specific folder"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".move.IMoveAction"
+      factory=".move.MoveAction"
+      addview="plone.actions.Move"
+      editview="edit"
+      />
+
+  <!-- Delete action (no configurable options) -->
+
+  <adapter factory=".delete.DeleteActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Delete"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".delete.DeleteAddForm"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Delete"
+      title="Delete object"
+      description="Delete the triggering item"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".delete.IDeleteAction"
+      factory=".delete.DeleteAction"
+      addview="plone.actions.Delete"
+      />
+
+  <!-- Transition workflow action -->
+
+  <adapter factory=".workflow.WorkflowActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Workflow"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".workflow.WorkflowAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.workflow.IWorkflowAction"
+      class=".workflow.WorkflowEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Workflow"
+      title="Transition workflow state"
+      description="Perform a workflow transition on the triggering object"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".workflow.IWorkflowAction"
+      factory=".workflow.WorkflowAction"
+      addview="plone.actions.Workflow"
+      editview="edit"
+      />
+
+  <!-- Email action definition -->
+
+  <adapter factory=".mail.MailActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Mail"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".mail.MailAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.mail.IMailAction"
+      class=".mail.MailEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Mail"
+      title="Send email"
+      description="Send an email on the triggering object"
+      for="*"
+      event="*"
+      schema=".mail.IMailAction"
+      factory=".mail.MailAction"
+      addview="plone.actions.Mail"
+      editview="edit"
+      />
+
+  <!-- Versioning action -->
+
+  <adapter factory=".versioning.VersioningActionExecutor" />
+
+  <browser:page
+      name="plone.actions.Versioning"
+      for="plone.app.contentrules.browser.interfaces.IRuleActionAdding"
+      class=".versioning.VersioningAddFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <browser:page
+      name="edit"
+      for="plone.app.contentrules.actions.versioning.IVersioningAction"
+      class=".versioning.VersioningEditFormView"
+      permission="plone.app.contentrules.ManageContentRules"
+      />
+
+  <plone:ruleAction
+      name="plone.actions.Versioning"
+      title="Version object"
+      description="Store a new version of the object"
+      for="*"
+      event="*"
+      schema=".versioning.IVersioningAction"
+      factory=".versioning.VersioningAction"
+      addview="plone.actions.Versioning"
+      editview="edit"
+      />
 
 </configure>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/copy.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/copy.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/delete.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/delete.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/logger.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/logger.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/mail.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/mail.py`

 * *Files 0% similar despite different names*

```diff
@@ -49,14 +49,15 @@
             "different email addresses, just separate them with ,"
         ),
         required=True,
     )
     exclude_actor = schema.Bool(
         title=_("Exclude actor from recipients"),
         description=_("Do not send the email to the user that did the action."),
+        required=False,
     )
     message = schema.Text(
         title=_("Message"),
         description=_("The message that you want to mail."),
         required=True,
     )
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/move.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/move.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/notify.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/notify.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/templates/mail.pt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/templates/mail.pt`

 * *Files 22% similar despite different names*

```diff
@@ -1,29 +1,32 @@
 <metal:block use-macro="context/@@ploneform-macros/titlelessform" />
 <tal:i18n i18n:domain="plone">
-<h1 i18n:translate="title_contentrules_mailsub">Substitutions</h1>
+  <h1 i18n:translate="title_contentrules_mailsub">Substitutions</h1>
 
-<p i18n:translate="description-contentrules-mailsub">
+  <p i18n:translate="description-contentrules-mailsub">
     Some content in the subject, email source, email recipient and message
     may be replaced with "$&#123;&#125;" variables from the table below.
-</p>
+  </p>
 
-<table class="listing">
-<thead>
-    <tr>
+  <table class="listing">
+    <thead>
+      <tr>
         <th i18n:translate="category-contentrules-mailsub">Category</th>
         <th i18n:translate="variable-contentrules-mailsub">Variable</th>
         <th i18n:translate="substitution-contentrules-mailsub">Substitution</th>
-    </tr>
-</thead>
-<tbody>
-<tal:block tal:define="sublist here/@@stringinterp_info/substitutionList"
-     tal:repeat="category sublist">
-     <tr tal:repeat="item python:category['items']">
-         <td tal:content="category/category">All Content</td>
-         <td>${<span tal:replace="item/id">url</span>}</td>
-         <td tal:content="item/description">URL</td>
-     </tr>
-</tal:block>
-</tbody>
-</table>
+      </tr>
+    </thead>
+    <tbody>
+      <tal:block tal:define="
+                   sublist here/@@stringinterp_info/substitutionList;
+                 "
+                 tal:repeat="category sublist"
+      >
+        <tr tal:repeat="item python:category['items']">
+          <td tal:content="category/category">All Content</td>
+          <td>${<span tal:replace="item/id">url</span>}</td>
+          <td tal:content="item/description">URL</td>
+        </tr>
+      </tal:block>
+    </tbody>
+  </table>
 </tal:i18n>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/versioning.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/versioning.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/actions/workflow.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/actions/workflow.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/api.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/api.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/adding.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/adding.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,14 @@
 from zope.component import getUtility
 from zope.container.interfaces import INameChooser
 from zope.interface import implementer
 
 
 @implementer(IRuleAdding)
 class RuleAdding(SimpleItem, BrowserView):
-
     context = None
     request = None
     contentName = None
 
     # This is necessary so that context.absolute_url() works properly on the
     # add form, which in turn fixes the <base /> URL
     id = "+rule"
@@ -69,15 +68,14 @@
         return None
 
     def nextURL(self):
         return None
 
 
 class RuleElementAdding(SimpleItem, BrowserView):
-
     context = None
     request = None
     contentName = None
 
     def __init__(self, context, request):
         self.context = context
         self.request = request
@@ -111,28 +109,26 @@
 
     def hasCustomAddView(self):
         return None
 
 
 @implementer(IRuleConditionAdding)
 class RuleConditionAdding(RuleElementAdding):
-
     # This is necessary so that context.absolute_url() works properly on the
     # add form, which in turn fixes the <base /> URL
     id = "+condition"
 
     def add(self, content):
         """Add the rule element to the context rule"""
         rule = aq_base(aq_inner(self.context))
         rule.conditions.append(content)
 
 
 @implementer(IRuleActionAdding)
 class RuleActionAdding(RuleElementAdding):
-
     # This is necessary so that context.absolute_url() works properly on the
     # add form, which in turn fixes the <base /> URL
     id = "+action"
 
     def add(self, content):
         """Add the rule element to the context rule"""
         rule = aq_base(aq_inner(self.context))
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/assignments.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/assignments.py`

 * *Files 0% similar despite different names*

```diff
@@ -91,15 +91,14 @@
     def type_name(self):
         context = aq_inner(self.context)
         fti = context.getTypeInfo()
         return fti.Title()
 
     @memoize
     def acquired_rules(self):
-
         # Short circuit if this is the root of the portal
         if ISiteRoot.providedBy(self.context):
             return []
 
         in_use = {r["id"] for r in self.assigned_rules()}
 
         storage = getUtility(IRuleStorage)
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/configure.zcml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/configure.zcml`

 * *Files 2% similar despite different names*

```diff
@@ -1,196 +1,200 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
-    xmlns:browser="http://namespaces.zope.org/browser">
+    xmlns:browser="http://namespaces.zope.org/browser"
+    >
 
-    <!-- Site-wide information -->
-    <browser:page
-        for="*"
-        name="plone_contentrules_info"
-        class=".info.ContentRulesInfo"
-        allowed_interface=".interfaces.IContentRulesInfo"
-        permission="zope.Public"
-        />
+  <!-- Site-wide information -->
+  <browser:page
+      name="plone_contentrules_info"
+      for="*"
+      class=".info.ContentRulesInfo"
+      allowed_interface=".interfaces.IContentRulesInfo"
+      permission="zope.Public"
+      />
 
-    <!-- Adding views for rules and elements -->
-    <browser:view
-      for="Products.CMFCore.interfaces.ISiteRoot"
+  <!-- Adding views for rules and elements -->
+  <browser:view
       name="+rule"
+      for="Products.CMFCore.interfaces.ISiteRoot"
       class=".adding.RuleAdding"
       allowed_interface="plone.app.contentrules.browser.interfaces.IRuleAdding"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <class class=".adding.RuleAdding">
-      <require
+  <class class=".adding.RuleAdding">
+    <require
         permission="plone.app.contentrules.ManageContentRules"
-        interface=".interfaces.IRuleAdding" />
-    </class>
+        interface=".interfaces.IRuleAdding"
+        />
+  </class>
 
-    <browser:view
-      for="plone.contentrules.rule.interfaces.IRule"
+  <browser:view
       name="+condition"
+      for="plone.contentrules.rule.interfaces.IRule"
       class=".adding.RuleConditionAdding"
       allowed_interface=".interfaces.IRuleConditionAdding"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <class class=".adding.RuleConditionAdding">
-      <require
+  <class class=".adding.RuleConditionAdding">
+    <require
         permission="plone.app.contentrules.ManageContentRules"
-        interface=".interfaces.IRuleConditionAdding" />
-    </class>
+        interface=".interfaces.IRuleConditionAdding"
+        />
+  </class>
 
-    <browser:view
-      for="plone.contentrules.rule.interfaces.IRule"
+  <browser:view
       name="+action"
+      for="plone.contentrules.rule.interfaces.IRule"
       class=".adding.RuleActionAdding"
       allowed_interface=".interfaces.IRuleActionAdding"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <class class=".adding.RuleActionAdding">
-      <require
+  <class class=".adding.RuleActionAdding">
+    <require
         permission="plone.app.contentrules.ManageContentRules"
-        interface=".interfaces.IRuleActionAdding" />
-    </class>
+        interface=".interfaces.IRuleActionAdding"
+        />
+  </class>
 
-    <!-- Add and edit form for rules -->
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleAdding"
+  <!-- Add and edit form for rules -->
+  <browser:page
       name="plone.ContentRule"
+      for="plone.app.contentrules.browser.interfaces.IRuleAdding"
       class=".rule.RuleAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.contentrules.rule.interfaces.IRule"
+  <browser:page
       name="edit"
+      for="plone.contentrules.rule.interfaces.IRule"
       class=".rule.RuleEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <!-- Manage rules -->
+  <!-- Manage rules -->
 
-    <browser:page
-      for="Products.CMFCore.interfaces.ISiteRoot"
+  <browser:page
       name="rules-controlpanel"
+      for="Products.CMFCore.interfaces.ISiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
-      permission="plone.app.contentrules.ManageContentRules"
       allowed_attributes="template"
+      permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
+  <browser:page
       name="manage-elements"
       for="plone.contentrules.rule.interfaces.IRule"
       class=".elements.ManageElements"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.contentrules.engine.interfaces.IRuleAssignable"
+  <browser:page
       name="manage-content-rules"
+      for="plone.contentrules.engine.interfaces.IRuleAssignable"
       class=".assignments.ManageAssignments"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
+  <browser:page
       name="contentrule-enable"
+      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
       attribute="enable_rule"
       permission="plone.app.contentrules.ManageContentRules"
-    />
+      />
 
-    <browser:page
-      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
+  <browser:page
       name="contentrule-disable"
+      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
       attribute="disable_rule"
       permission="plone.app.contentrules.ManageContentRules"
-    />
+      />
 
-    <browser:page
-      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
+  <browser:page
       name="contentrule-delete"
+      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
       attribute="delete_rule"
       permission="plone.app.contentrules.ManageContentRules"
-    />
+      />
 
-    <browser:page
-      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
+  <browser:page
       name="contentrule-globally-enable"
+      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
       attribute="globally_enable"
       permission="plone.app.contentrules.ManageContentRules"
-    />
+      />
 
-    <browser:page
-      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
+  <browser:page
       name="contentrule-globally-disable"
+      for="plone.base.interfaces.siteroot.IPloneSiteRoot"
       class=".controlpanel.ContentRulesControlPanel"
       attribute="globally_disable"
       permission="plone.app.contentrules.ManageContentRules"
-    />
+      />
 
-    <!-- Namespace for rules, and for actions and conditions -->
+  <!-- Namespace for rules, and for actions and conditions -->
 
-    <adapter
-        factory=".traversal.RuleNamespace"
-        name="rule"
-        />
-    <adapter
-        factory=".traversal.RuleConditionNamespace"
-        name="condition"
-        />
-    <adapter
-        factory=".traversal.RuleActionNamespace"
-        name="action"
-        />
+  <adapter
+      factory=".traversal.RuleNamespace"
+      name="rule"
+      />
+  <adapter
+      factory=".traversal.RuleConditionNamespace"
+      name="condition"
+      />
+  <adapter
+      factory=".traversal.RuleActionNamespace"
+      name="action"
+      />
 
-    <!-- When we access rules and elements, we still want to use a CMF/Plone
+  <!-- When we access rules and elements, we still want to use a CMF/Plone
     main_template -->
 
-    <configure package="Products.CMFPlone.browser">
+  <configure package="Products.CMFPlone.browser">
 
-      <browser:page
+    <browser:page
         name="five_template"
         for="plone.app.contentrules.browser.interfaces.IRuleAdding"
         template="templates/five_template.pt"
         permission="zope2.View"
         />
 
-      <browser:page
+    <browser:page
         name="five_template"
         for="plone.app.contentrules.browser.interfaces.IRuleElementAdding"
         template="templates/five_template.pt"
         permission="zope2.View"
         />
 
-      <browser:page
+    <browser:page
         name="five_template"
         for="plone.contentrules.rule.interfaces.IRule"
         template="templates/five_template.pt"
         permission="zope2.View"
         />
 
-      <browser:page
+    <browser:page
         name="five_template"
         for="plone.contentrules.rule.interfaces.IRuleElementData"
         template="templates/five_template.pt"
         permission="zope2.View"
         />
 
-    </configure>
+  </configure>
 
-    <!-- Rule breadcrumb -->
+  <!-- Rule breadcrumb -->
 
   <browser:page
-      for="plone.contentrules.rule.interfaces.IRule"
       name="breadcrumbs_view"
+      for="plone.contentrules.rule.interfaces.IRule"
       class=".navigation.RuleBreadcrumbs"
-      permission="zope.Public"
       allowed_attributes="breadcrumbs"
+      permission="zope.Public"
       />
 
 </configure>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/controlpanel.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/controlpanel.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/elements.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/elements.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/formhelper.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/formhelper.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
     """A base add form for content rule.
 
     Use this for rule elements that require configuration before being added to
     a rule. Element types that do not should use NullAddForm instead.
 
     Sub-classes should define create() and set the form_fields class variable.
 
-    Notice the suble difference between AddForm and NullAddform in that the
+    Notice the subtle difference between AddForm and NullAddform in that the
     create template method for AddForm takes as a parameter a dict 'data':
 
         def create(self, data):
             return MyAssignment(data.get('foo'))
 
     whereas the NullAddForm has no data parameter:
 
@@ -149,9 +149,8 @@
             url,
             rule.__name__,
             focus,
         )
 
 
 class ContentRuleFormWrapper(layout.FormWrapper):
-
     index = ViewPageTemplateFile("templates/contentrules-pageform.pt")
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/info.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/info.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/interfaces.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/interfaces.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,15 +9,15 @@
         """Determine whether or not the rules tab should be shown."""
 
 
 class IContentRulesControlPanel(Interface):
     """Marker interface for rules control panel view"""
 
     def globally_disabled():
-        """Wether content rules are globally disabled or not"""
+        """Whether content rules are globally disabled or not"""
 
 
 class IRuleAdding(IAdding):
     """Marker interface for rule add views.
 
     Rules' addviews should be registered for this.
     """
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/navigation.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/navigation.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/rule.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/rule.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/contentrules-pageform.pt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/contentrules-pageform.pt`

 * *Files 24% similar despite different names*

```diff
@@ -1,32 +1,39 @@
 <html xmlns="http://www.w3.org/1999/xhtml"
-      xmlns:metal="http://xml.zope.org/namespaces/metal"
       xmlns:i18n="http://xml.zope.org/namespaces/i18n"
-      xml:lang="en" lang="en"
+      xmlns:metal="http://xml.zope.org/namespaces/metal"
+      lang="en"
       metal:use-macro="context/prefs_main_template/macros/master"
-      i18n:domain="plone">
-
-<body>
-<div metal:fill-slot="prefs_configlet_main">
-
-    <a id="setup-link" class="link-parent"
-       tal:attributes="href string:$portal_url/@@overview-controlpanel"
-       i18n:translate="">
+      xml:lang="en"
+      i18n:domain="plone"
+>
+
+  <body>
+    <div metal:fill-slot="prefs_configlet_main">
+
+      <a class="link-parent"
+         id="setup-link"
+         tal:attributes="
+           href string:$portal_url/@@overview-controlpanel;
+         "
+         i18n:translate=""
+      >
         Site Setup
-    </a>
+      </a>
 
-    <h1 class="documentFirstHeading"
-        tal:content="view/label">View Title</h1>
+      <h1 class="documentFirstHeading"
+          tal:content="view/label"
+      >View Title</h1>
 
-    <div metal:use-macro="context/global_statusmessage/macros/portal_message">
+      <div metal:use-macro="context/global_statusmessage/macros/portal_message">
       Portal status message
-    </div>
+      </div>
 
-    <div id="content-core">
+      <div id="content-core">
         <div id="layout-contents">
-            <span tal:replace="structure view/contents" />
+          <span tal:replace="structure view/contents"></span>
         </div>
-    </div>
+      </div>
 
-</div>
-</body>
+    </div>
+  </body>
 </html>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/controlpanel.pt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/controlpanel.pt`

 * *Files 26% similar despite different names*

```diff
@@ -1,223 +1,346 @@
-<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
-      lang="en"
+<html xmlns="http://www.w3.org/1999/xhtml"
+      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
       xmlns:metal="http://xml.zope.org/namespaces/metal"
       xmlns:tal="http://xml.zope.org/namespaces/tal"
-      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
+      lang="en"
       metal:use-macro="here/prefs_main_template/macros/master"
-      i18n:domain="plone">
-
-<body>
-
-<metal:main metal:fill-slot="prefs_configlet_main"
-     tal:define="rules view/registeredRules">
-
-  <header>
-    <h1 class="documentFirstHeading"
-        i18n:translate="title_manage_contentrules">Content Rules</h1>
-
-    <p i18n:translate="description-contentrules-controlpanel" class="lead">
+      xml:lang="en"
+      i18n:domain="plone"
+>
+
+  <body>
+
+    <metal:main metal:fill-slot="prefs_configlet_main"
+                tal:define="
+                  rules view/registeredRules;
+                "
+    >
+
+      <header>
+        <h1 class="documentFirstHeading"
+            i18n:translate="title_manage_contentrules"
+        >Content Rules</h1>
+
+        <p class="lead"
+           i18n:translate="description-contentrules-controlpanel"
+        >
         Use the form below to define, change or remove content rules. Rules
         will automatically perform actions on content when certain triggers
         take place. After defining rules, you may want to go to a folder
         to assign them, using the "rules" item in the actions menu.
-    </p>
+        </p>
 
-    <div id="fieldset-global">
-      <form name="ruleSettings" method="POST"
-           tal:attributes="action string:${context/absolute_url}/@@rules-controlpanel">
-          <span tal:replace="structure context/@@authenticator/authenticator"/>
-          <div class="form-check">
-              <input type="hidden" name="global_disable:boolean:default" value="" />
-              <input type="checkbox"
-                     class="form-check-input"
+        <div id="fieldset-global">
+          <form method="POST"
+                name="ruleSettings"
+                tal:attributes="
+                  action string:${context/absolute_url}/@@rules-controlpanel;
+                "
+          >
+            <span tal:replace="structure context/@@authenticator/authenticator"></span>
+            <div class="form-check">
+              <input name="global_disable:boolean:default"
+                     type="hidden"
+                     value=""
+              />
+              <input class="form-check-input"
                      id="rules_disable_globally"
                      name="global_disable:boolean"
+                     type="checkbox"
                      value="True"
-                     tal:attributes="checked python:view.globally_disabled() and 'checked' or None" />
-              <label class="form-check-label" for="rules_disable_globally" i18n:translate="">Disable globally</label>
-              <div class="form-text" i18n:translate="">
+                     tal:attributes="
+                       checked python:view.globally_disabled() and 'checked' or None;
+                     "
+              />
+              <label class="form-check-label"
+                     for="rules_disable_globally"
+                     i18n:translate=""
+              >Disable globally</label>
+              <div class="form-text"
+                   i18n:translate=""
+              >
                   Whether or not content rules should be disabled globally. If this is selected,
                   no rules will be executed anywhere in the portal.
               </div>
-          </div>
+            </div>
 
-          <noscript>
-          <!-- we'll use js to submit this normally -->
-            <div class="formControls">
-                <input type="submit"
+            <noscript>
+              <!-- we'll use js to submit this normally -->
+              <div class="formControls">
+                <input class="btn btn-primary"
                        name="form.button.SaveSettings"
-                       class="btn btn-primary"
+                       type="submit"
                        value="Save"
-                       i18n:attributes="value label_save;" />
-            </div>
-          </noscript>
-      </form>
+                       i18n:attributes="value label_save;"
+                />
+              </div>
+            </noscript>
+          </form>
 
-    </div>
+        </div>
 
 
-  </header>
+      </header>
 
-  <div id="content-core">
-    <div id="translated-text" style="display:none">
-      <span id="trns_form_error" i18n:translate="">
+      <div id="content-core">
+        <div id="translated-text"
+             style="display:none"
+        >
+          <span id="trns_form_error"
+                i18n:translate=""
+          >
         There was an error saving content rules.
-      </span>
-      <span id="trns_form_success" i18n:translate="">
+          </span>
+          <span id="trns_form_success"
+                i18n:translate=""
+          >
         Content rule settings updated.
-      </span>
-      <span id="trns_form_success_enabled" i18n:translate="">
+          </span>
+          <span id="trns_form_success_enabled"
+                i18n:translate=""
+          >
         Content rule enabled
-      </span>
-      <span id="trns_form_success_disabled" i18n:translate="">
+          </span>
+          <span id="trns_form_success_disabled"
+                i18n:translate=""
+          >
         Content rule disabled
-      </span>
-      <span id="trns_form_success_deleted" i18n:translate="">
+          </span>
+          <span id="trns_form_success_deleted"
+                i18n:translate=""
+          >
         Content rule deleted
-      </span>
-    </div>
+          </span>
+        </div>
 
 
-    <div class="card">
-      <fieldset id="fieldset-rules" class="card-body"
-                tal:define="rules rules|view/registeredRules;">
-
-          <div class="filters row row-cols-lg-auto g-3 align-items-center" tal:condition="rules">
-            <span class="type-filters">
-              <label class="col-form-label pe-3" i18n:translate="">Filter rules:</label>
-              <span class="filter-option"
-                    tal:repeat="rule view/ruleTypesToShow">
+        <div class="card">
+          <fieldset class="card-body"
+                    id="fieldset-rules"
+                    tal:define="
+                      rules rules|view/registeredRules;
+                    "
+          >
+
+            <div class="filters row row-cols-lg-auto g-3 align-items-center"
+                 tal:condition="rules"
+            >
+              <span class="type-filters">
+                <label class="col-form-label pe-3"
+                       i18n:translate=""
+                >Filter rules:</label>
+                <span class="filter-option"
+                      tal:repeat="rule view/ruleTypesToShow"
+                >
                   <div class="form-check form-check-inline">
-                    <input id="all" class="form-check-input" type="checkbox"
-                            tal:attributes="id rule/id"
-                            />
+                    <input class="form-check-input"
+                           id="all"
+                           type="checkbox"
+                           tal:attributes="
+                             id rule/id;
+                           "
+                    />
                     <label class="form-check-label"
-                            for="all"
-                            tal:attributes="for rule/id"
-                            tal:content="rule/title">
-                            All</label>
+                           for="all"
+                           tal:content="rule/title"
+                           tal:attributes="
+                             for rule/id;
+                           "
+                    >
+                      All</label>
                   </div>
+                </span>
               </span>
-            </span>
-            <span class="state-filters">
-              <span class="filter-option"
-                    tal:repeat="state view/statesToShow">
+              <span class="state-filters">
+                <span class="filter-option"
+                      tal:repeat="state view/statesToShow"
+                >
                   <div class="form-check form-check-inline">
-                    <input id="all" class="form-check-input" type="checkbox"
-                            tal:attributes="id state/id"
-                            />
+                    <input class="form-check-input"
+                           id="all"
+                           type="checkbox"
+                           tal:attributes="
+                             id state/id;
+                           "
+                    />
                     <label class="form-check-label"
-                            for="all"
-                            tal:attributes="for state/id"
-                            tal:content="state/title">
-                            All</label>
+                           for="all"
+                           tal:content="state/title"
+                           tal:attributes="
+                             for state/id;
+                           "
+                    >
+                      All</label>
                   </div>
+                </span>
               </span>
-            </span>
-          </div>
+            </div>
 
-          <div class="visualClear"><!-- --></div>
-          <div id="rules_table_form"
-                metal:define-macro="rules_table_form">
-          <table  class="listing nosort controlpanel-listing table mb-0"
-                  tal:condition="rules">
-              <thead class="">
+            <div class="visualClear"><!-- --></div>
+            <div id="rules_table_form"
+                 metal:define-macro="rules_table_form"
+            >
+              <table class="listing nosort controlpanel-listing table mb-0"
+                     tal:condition="rules"
+              >
+                <thead class="">
                   <tr>
-                      <th scope="col" i18n:translate="label_contentrules_rule_listing">Content rule</th>
-                      <th scope="col" i18n:translate="label_contentrules_rule_event">Event</th>
-                      <th scope="col"><span class="ps-2" i18n:translate="label_contentrules_rule_status">Status</span></th>
-                      <th scope="col" i18n:translate="label_contentrules_rule_actions">Actions</th>
+                    <th scope="col"
+                        i18n:translate="label_contentrules_rule_listing"
+                    >Content rule</th>
+                    <th scope="col"
+                        i18n:translate="label_contentrules_rule_event"
+                    >Event</th>
+                    <th scope="col"><span class="ps-2"
+                            i18n:translate="label_contentrules_rule_status"
+                      >Status</span></th>
+                    <th scope="col"
+                        i18n:translate="label_contentrules_rule_actions"
+                    >Actions</th>
                   </tr>
-              </thead>
-              <tbody>
+                </thead>
+                <tbody>
                   <tal:rules repeat="rule view/registeredRules">
-                  <tr tal:define="oddrow repeat/rule/odd"
-                      tal:attributes="class python:(oddrow and 'even ' or 'odd ') + rule['row_class'];">
+                    <tr tal:define="
+                          oddrow repeat/rule/odd;
+                        "
+                        tal:attributes="
+                          class python:(oddrow and 'even ' or 'odd ') + rule['row_class'];
+                        "
+                    >
                       <td>
                         <h5 class="rule-title">
-                          <span
-                              tal:replace="rule/title">Rule Title</span>
+                          <span tal:replace="rule/title">Rule Title</span>
                         </h5>
-                          <div tal:content="rule/description">
+                        <div tal:content="rule/description">
                               Rule Description.
-                          </div>
+                        </div>
                       </td>
                       <td>
-                          <span class="trigger"
-                                tal:content="rule/trigger"
-                                i18n:translate="">trigger</span>
+                        <span class="trigger"
+                              tal:content="rule/trigger"
+                              i18n:translate=""
+                        >trigger</span>
                       </td>
                       <td class="status">
 
-                        <form style="display: inline" method="POST"
-                              tal:attributes="action string:${context/absolute_url}/@@rules-controlpanel">
-                        <span tal:replace="structure context/@@authenticator/authenticator"/>
-                        <input type="hidden"
-                              name="rule-id"
-                              tal:attributes="value rule/id">
-                        <button class="context btn-rule-action btn-rule-enable btn btn-sm btn-link ${python: rule['enabled'] and 'd-none'}" type="submit" value="Enable"
-                              name="form.button.EnableRule"
-                              tal:attributes="data-value rule/id;
-                                              data-url string:$portal_url/@@contentrule-enable"
-                              i18n:attributes="value label_enable;">
-                              <tal:icon tal:replace="structure python:icons.tag('square', tag_alt='Toggle to show')" /><span class="ms-2" i18n:translate="enabled">Enabled</span>
-                        </button>
-                        <button class="standalone btn-rule-action btn-rule-disable btn btn-sm btn-link ${python: not rule['enabled'] and 'd-none'}" type="submit" value="Disable"
-                              name="form.button.DisableRule"
-                              tal:attributes="data-value rule/id;
-                                              data-url string:$portal_url/@@contentrule-disable"
-                              i18n:attributes="value label_disable;">
-                              <tal:icon tal:replace="structure python:icons.tag('check-square', tag_alt='Toggle to show')" /><span class="ms-2" i18n:translate="enabled">Enabled</span>
-                            </button>
+                        <form method="POST"
+                              style="display: inline"
+                              tal:attributes="
+                                action string:${context/absolute_url}/@@rules-controlpanel;
+                              "
+                        >
+                          <span tal:replace="structure context/@@authenticator/authenticator"></span>
+                          <input name="rule-id"
+                                 type="hidden"
+                                 tal:attributes="
+                                   value rule/id;
+                                 "
+                          />
+                          <button class="context btn-rule-action btn-rule-enable btn btn-sm btn-link ${python: rule['enabled'] and 'd-none'}"
+                                  name="form.button.EnableRule"
+                                  type="submit"
+                                  value="Enable"
+                                  tal:attributes="
+                                    data-value rule/id;
+                                    data-url string:$portal_url/@@contentrule-enable;
+                                  "
+                                  i18n:attributes="value label_enable;"
+                          >
+                            <tal:icon tal:replace="structure python:icons.tag('square', tag_alt='Toggle to show')" /><span class="ms-2"
+                                  i18n:translate="enabled"
+                            >Enabled</span>
+                          </button>
+                          <button class="standalone btn-rule-action btn-rule-disable btn btn-sm btn-link ${python: not rule['enabled'] and 'd-none'}"
+                                  name="form.button.DisableRule"
+                                  type="submit"
+                                  value="Disable"
+                                  tal:attributes="
+                                    data-value rule/id;
+                                    data-url string:$portal_url/@@contentrule-disable;
+                                  "
+                                  i18n:attributes="value label_disable;"
+                          >
+                            <tal:icon tal:replace="structure python:icons.tag('check-square', tag_alt='Toggle to show')" /><span class="ms-2"
+                                  i18n:translate="enabled"
+                            >Enabled</span>
+                          </button>
                         </form>
 
-                        <span
-                          class="badge bg-warning text-dark icon-contentrule-enabled-unassigned"
-                          alt="unassigned"
-                          title="this rule has not been assigned"
-                          tal:condition="python:not rule['assigned']"
-                          i18n:attributes="alt label_contentrules_rule_unassigned;
-                                          title title_contentrule_rule_unassigned;">
-                          <tal:icon tal:replace="structure python:icons.tag('exclamation-triangle-fill', tag_alt='not assigned')" /><span class="ms-2" i18n:translate="">not assigned</span>
-                    </span>
+                        <span class="badge bg-warning text-dark icon-contentrule-enabled-unassigned"
+                              alt="unassigned"
+                              title="this rule has not been assigned"
+                              tal:condition="python:not rule['assigned']"
+                              i18n:attributes="alt label_contentrules_rule_unassigned;
+                                          title title_contentrule_rule_unassigned;"
+                        >
+                          <tal:icon tal:replace="structure python:icons.tag('exclamation-triangle-fill', tag_alt='not assigned')" /><span class="ms-2"
+                                i18n:translate=""
+                          >not assigned</span>
+                        </span>
 
 
 
                       </td>
                       <td>
-                        <form style="display: inline" method="POST"
-                              tal:attributes="action string:${context/absolute_url}/@@rules-controlpanel">
-                        <span tal:replace="structure context/@@authenticator/authenticator"/>
-                        <input type="hidden"
-                              name="rule-id"
-                              tal:attributes="value rule/id">
-                        <a href="" class="btn btn-sm btn-primary"
-                        tal:attributes="href string:${context/absolute_url}/++rule++${rule/id}/@@manage-elements" i18n:translate="">Configure</a>
-                        <a href="" class="btn btn-sm btn-secondary"
-                              tal:attributes="href string:${context/absolute_url}/++rule++${rule/id}/@@edit" i18n:translate="">Edit</a>
-
-                        <button class="destructive btn-rule-action btn-rule-delete btn btn-sm btn-danger" type="submit" value="Delete"
-                              tal:attributes="data-value rule/id;
-                                              data-url string:$portal_url/@@contentrule-delete"
-                              name="form.button.DeleteRule"
-                              i18n:translate=""
-                              i18n:attributes="value label_delete;">Delete</button>
+                        <form method="POST"
+                              style="display: inline"
+                              tal:attributes="
+                                action string:${context/absolute_url}/@@rules-controlpanel;
+                              "
+                        >
+                          <span tal:replace="structure context/@@authenticator/authenticator"></span>
+                          <input name="rule-id"
+                                 type="hidden"
+                                 tal:attributes="
+                                   value rule/id;
+                                 "
+                          />
+                          <a class="btn btn-sm btn-primary"
+                             href=""
+                             tal:attributes="
+                               href string:${context/absolute_url}/++rule++${rule/id}/@@manage-elements;
+                             "
+                             i18n:translate=""
+                          >Configure</a>
+                          <a class="btn btn-sm btn-secondary"
+                             href=""
+                             tal:attributes="
+                               href string:${context/absolute_url}/++rule++${rule/id}/@@edit;
+                             "
+                             i18n:translate=""
+                          >Edit</a>
+
+                          <button class="destructive btn-rule-action btn-rule-delete btn btn-sm btn-danger"
+                                  name="form.button.DeleteRule"
+                                  type="submit"
+                                  value="Delete"
+                                  tal:attributes="
+                                    data-value rule/id;
+                                    data-url string:$portal_url/@@contentrule-delete;
+                                  "
+                                  i18n:attributes="value label_delete;"
+                                  i18n:translate=""
+                          >Delete</button>
                         </form>
                       </td>
-                  </tr>
+                    </tr>
                   </tal:rules>
-              </tbody>
-          </table>
-          </div>
-        </fieldset>
-      </div>
-      <div class="mt-3">
-        <a id="#addcontentrule" tal:attributes="href string:${context/absolute_url}/+rule/plone.ContentRule;"
-            class="plone-btn plone-btn-primary btn btn-success"
-            i18n:translate="label_contentrule_add">Add content rule</a>
+                </tbody>
+              </table>
+            </div>
+          </fieldset>
+        </div>
+        <div class="mt-3">
+          <a class="plone-btn plone-btn-primary btn btn-success"
+             id="#addcontentrule"
+             tal:attributes="
+               href string:${context/absolute_url}/+rule/plone.ContentRule;
+             "
+             i18n:translate="label_contentrule_add"
+          >Add content rule</a>
+        </div>
       </div>
-    </div>
-</metal:main>
-</body>
+    </metal:main>
+  </body>
 </html>
-
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/manage-assignments.pt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/manage-assignments.pt`

 * *Files 15% similar despite different names*

```diff
@@ -1,263 +1,364 @@
-<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
-      lang="en"
+<html xmlns="http://www.w3.org/1999/xhtml"
+      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
       xmlns:metal="http://xml.zope.org/namespaces/metal"
       xmlns:tal="http://xml.zope.org/namespaces/tal"
-      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
+      lang="en"
       metal:use-macro="context/main_template/macros/master"
-      i18n:domain="plone">
-
-<head>
-</head>
-
-<body>
-
-<metal:body fill-slot="body"
-    tal:define="icons python:context.restrictedTraverse('@@iconresolver')">
-
-      <link rel="stylesheet" type="text/css" media="all"
-          href="++resource++manage-contentrules.css"
-          tal:attributes="href string:${context/portal_url}/++resource++manage-contentrules.css" />
-
-    <div tal:condition="not:view/globally_enabled"
-         class="alert alert-info">
+      xml:lang="en"
+      i18n:domain="plone"
+>
+
+  <head>
+  </head>
+
+  <body>
+
+    <metal:body fill-slot="body"
+                tal:define="
+                  icons python:context.restrictedTraverse('@@iconresolver');
+                "
+    >
+
+      <link href="++resource++manage-contentrules.css"
+            media="all"
+            rel="stylesheet"
+            type="text/css"
+            tal:attributes="
+              href string:${context/portal_url}/++resource++manage-contentrules.css;
+            "
+      />
+
+      <div class="alert alert-info"
+           tal:condition="not:view/globally_enabled"
+      >
         <strong i18n:translate="">
             Info
         </strong>
         <span i18n:translate="warning_contentrules_disabled">
             Content rules are disabled globally. No assigned rules will execute
             until they are re-enabled. Use the
-            <a href=""
-               i18n:name="controlpanel_link"
-               i18n:translate="contentrules_control_panel"
-               tal:attributes="href string:${portal_url}/@@rules-controlpanel">
+          <a href=""
+             tal:attributes="
+               href string:${portal_url}/@@rules-controlpanel;
+             "
+             i18n:name="controlpanel_link"
+             i18n:translate="contentrules_control_panel"
+          >
                 content rules control panel
-            </a>to enable them again.
+          </a>to enable them again.
         </span>
-    </div>
+      </div>
 
-    <article id="content">
+      <article id="content">
         <header>
-            <h1 class="documentFirstHeading"
-                i18n:translate="title_contentrules_assigned">
-                Content rules for <q i18n:name="context" tal:content="context/Title">title</q>
-            </h1>
-
-            <div class="lead">
-
-                <span i18n:translate="description_contentrules_assigned" tal:condition="view/has_rules">
+          <h1 class="documentFirstHeading"
+              i18n:translate="title_contentrules_assigned"
+          >
+                Content rules for
+            <q tal:content="context/Title"
+               i18n:name="context"
+            >title</q>
+          </h1>
+
+          <div class="lead">
+
+            <span tal:condition="view/has_rules"
+                  i18n:translate="description_contentrules_assigned"
+            >
                     The following content rules are active in this
-                    <span i18n:name="type_name" tal:content="view/type_name" />.
-                </span>
-                <span i18n:translate="description_contentrules_assigned_norules" tal:condition="not:view/has_rules">
+              <span tal:content="view/type_name"
+                    i18n:name="type_name"
+              ></span>.
+            </span>
+            <span tal:condition="not:view/has_rules"
+                  i18n:translate="description_contentrules_assigned_norules"
+            >
                     There are currently no active content rules in this
-                    <span i18n:name="type_name" tal:content="view/type_name" />.
-                </span>
+              <span tal:content="view/type_name"
+                    i18n:name="type_name"
+              ></span>.
+            </span>
 
-                <span i18n:translate="contentrules_controlpanel_link">
+            <span i18n:translate="contentrules_controlpanel_link">
                     Use the
-                    <a i18n:name="controlpanel_link"
-                       i18n:translate="contentrules_control_panel"
-                       tal:attributes="href string:${portal_url}/@@rules-controlpanel">
+              <a tal:attributes="
+                   href string:${portal_url}/@@rules-controlpanel;
+                 "
+                 i18n:name="controlpanel_link"
+                 i18n:translate="contentrules_control_panel"
+              >
                         content rules control panel
-                    </a>
+              </a>
                     to create new rules or delete or modify existing ones.
-                </span>
+            </span>
 
 
-            </div>
+          </div>
 
 
         </header>
 
         <div id="content-core">
-            <div class="active">
-                <div tal:define="acquired_rules view/acquired_rules"
-                     tal:condition="acquired_rules">
-                    <table class="table listing nosort">
-                        <thead>
-                            <tr>
-                                <th i18n:translate="label_contentrules_from_parent">
+          <div class="active">
+            <div tal:define="
+                   acquired_rules view/acquired_rules;
+                 "
+                 tal:condition="acquired_rules"
+            >
+              <table class="table listing nosort">
+                <thead>
+                  <tr>
+                    <th i18n:translate="label_contentrules_from_parent">
                                     Content rules from parent folders
-                                </th>
-                                <th class="smallcolumn" i18n:translate="label_contentrules_active">Active</th>
-                            </tr>
-                        </thead>
-                        <tbody>
-                            <tal:rules repeat="rule acquired_rules">
-                                <tr tal:define="oddrow repeat/rule/odd"
-                                    tal:attributes="class python:oddrow and 'even' or 'odd'">
-                                    <td>
-                                        <dl>
-                                            <dt><a tal:attributes="href rule/url">
-                                                <span tal:replace="rule/title" />
-                                                (<span class="trigger"
-                                                    i18n:translate=""
-                                                    tal:content="rule/trigger">trigger</span>)</a></dt>
-                                            <dd tal:content="rule/description">
+                    </th>
+                    <th class="smallcolumn"
+                        i18n:translate="label_contentrules_active"
+                    >Active</th>
+                  </tr>
+                </thead>
+                <tbody>
+                  <tal:rules repeat="rule acquired_rules">
+                    <tr tal:define="
+                          oddrow repeat/rule/odd;
+                        "
+                        tal:attributes="
+                          class python:oddrow and 'even' or 'odd';
+                        "
+                    >
+                      <td>
+                        <dl>
+                          <dt><a tal:attributes="
+                                 href rule/url;
+                               ">
+                              <span tal:replace="rule/title"></span>
+                              (<span class="trigger"
+                                    tal:content="rule/trigger"
+                                    i18n:translate=""
+                              >trigger</span>)</a></dt>
+                          <dd tal:content="rule/description">
                                                 Rule Description.
-                                            </dd>
-                                        </dl>
-                                    </td>
-                                    <td class="checker">
-                                        <tal:icon tal:condition="rule/enabled"
-                                            i18n:attributes="alt label_contentrules_active;"
-                                            tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" />
-                                    </td>
-                                </tr>
-                            </tal:rules>
-                        </tbody>
-                    </table>
-                </div>
+                          </dd>
+                        </dl>
+                      </td>
+                      <td class="checker">
+                        <tal:icon tal:condition="rule/enabled"
+                                  tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')"
+                                  i18n:attributes="alt label_contentrules_active;"
+                        />
+                      </td>
+                    </tr>
+                  </tal:rules>
+                </tbody>
+              </table>
+            </div>
 
-                <div id="assignable-content-rules" class="mb-4"
-                    tal:define="assignable_rules view/assignable_rules"
-                    tal:condition="assignable_rules">
-                    <div class="col-form-label" i18n:translate="contentrules_available_rules">
+            <div class="mb-4"
+                 id="assignable-content-rules"
+                 tal:define="
+                   assignable_rules view/assignable_rules;
+                 "
+                 tal:condition="assignable_rules"
+            >
+              <div class="col-form-label"
+                   i18n:translate="contentrules_available_rules"
+              >
                         Available content rules:
-                    </div>
-                    <form class="row row-cols-auto g-3 align-items-center"
-                        tal:attributes="action string:${view/view_url}" method="post">
-                            <div class="col-auto">
-                                <select class="form-select" name="rule_id" size="1" id="select-rules">
-                                    <tal:options repeat="rule assignable_rules">
-                                        <option tal:attributes="value rule/id"
-                                                tal:content="rule/title">Addable rule name</option>
-                                    </tal:options>
-                                </select>
-                            </div>
-
-                            <div class="col-auto">
-                                <button class="context btn btn-primary"
-                                    type="submit"
-                                    name="form.button.AddAssignment"
-                                    value="Add"
-                                    i18n:attributes="value label_add;"
-                                    i18n:translate="label_add">Add</button>
-                            </div>
-                    </form>
+              </div>
+              <form class="row row-cols-auto g-3 align-items-center"
+                    method="post"
+                    tal:attributes="
+                      action string:${view/view_url};
+                    "
+              >
+                <div class="col-auto">
+                  <select class="form-select"
+                          id="select-rules"
+                          name="rule_id"
+                          size="1"
+                  >
+                    <tal:options repeat="rule assignable_rules">
+                      <option tal:content="rule/title"
+                              tal:attributes="
+                                value rule/id;
+                              "
+                      >Addable rule name</option>
+                    </tal:options>
+                  </select>
                 </div>
 
+                <div class="col-auto">
+                  <button class="context btn btn-primary"
+                          name="form.button.AddAssignment"
+                          type="submit"
+                          value="Add"
+                          i18n:attributes="value label_add;"
+                          i18n:translate="label_add"
+                  >Add</button>
+                </div>
+              </form>
+            </div>
 
-                <div class="clearfix"></div>
 
-                <form class="mb-3" tal:attributes="action view/view_url" method="post"
-                      tal:define="assigned_rules view/assigned_rules" tal:condition="assigned_rules">
-                    <table class="table listing nosort">
-                        <thead>
-                            <tr>
-                                <th class="smallcolumn">&nbsp;</th>
-                                <th i18n:translate="label_contentrules_active_assignments">
+            <div class="clearfix"></div>
+
+            <form class="mb-3"
+                  method="post"
+                  tal:define="
+                    assigned_rules view/assigned_rules;
+                  "
+                  tal:condition="assigned_rules"
+                  tal:attributes="
+                    action view/view_url;
+                  "
+            >
+              <table class="table listing nosort">
+                <thead>
+                  <tr>
+                    <th class="smallcolumn">&nbsp;</th>
+                    <th i18n:translate="label_contentrules_active_assignments">
                                     Active content rules in this
-                                    <span i18n:name="content_type"
-                                          tal:replace="view/type_name" />
-                                </th>
-                                <th class="smallcolumn">
+                      <span tal:replace="view/type_name"
+                            i18n:name="content_type"
+                      ></span>
+                    </th>
+                    <th class="smallcolumn">
                                     &nbsp;
-                                </th>
-                                <th class="smallcolumn" i18n:translate="label_contentrules_subfolders">
+                    </th>
+                    <th class="smallcolumn"
+                        i18n:translate="label_contentrules_subfolders"
+                    >
                                     Applies to subfolders?
-                                </th>
-                                <th class="smallcolumn" i18n:translate="label_contentrules_assignment_enabled">
+                    </th>
+                    <th class="smallcolumn"
+                        i18n:translate="label_contentrules_assignment_enabled"
+                    >
                                     Enabled here?
-                                </th>
-                                <th class="smallcolumn" i18n:translate="label_contentrules_rule_enabled_question">
+                    </th>
+                    <th class="smallcolumn"
+                        i18n:translate="label_contentrules_rule_enabled_question"
+                    >
                                     Enabled?
-                                </th>
-                            </tr>
-                        </thead>
-                        <tbody>
-                            <tal:rules repeat="rule assigned_rules">
-                            <tr tal:define="oddrow repeat/rule/odd"
-                                tal:attributes="class python:oddrow and 'even' or 'odd'">
-                                <td>
-                                    <input type="checkbox"
-                                           name="rule_ids:list"
-                                           tal:attributes="value rule/id" />
-                                </td>
-                                <td>
-                                    <dl>
-                                        <dt><a tal:attributes="href rule/url">
-                                            <span tal:replace="rule/title" />
-                                            (<span class="trigger"
-                                                i18n:translate=""
-                                                tal:content="rule/trigger">trigger</span>)</a></dt>
-                                        <dd tal:content="rule/description">
+                    </th>
+                  </tr>
+                </thead>
+                <tbody>
+                  <tal:rules repeat="rule assigned_rules">
+                    <tr tal:define="
+                          oddrow repeat/rule/odd;
+                        "
+                        tal:attributes="
+                          class python:oddrow and 'even' or 'odd';
+                        "
+                    >
+                      <td>
+                        <input name="rule_ids:list"
+                               type="checkbox"
+                               tal:attributes="
+                                 value rule/id;
+                               "
+                        />
+                      </td>
+                      <td>
+                        <dl>
+                          <dt><a tal:attributes="
+                                 href rule/url;
+                               ">
+                              <span tal:replace="rule/title"></span>
+                              (<span class="trigger"
+                                    tal:content="rule/trigger"
+                                    i18n:translate=""
+                              >trigger</span>)</a></dt>
+                          <dd tal:content="rule/description">
                                             Rule Description.
-                                        </dd>
-                                    </dl>
-                                </td>
-                                <td class="text-center">
-                                    <a tal:condition="not:repeat/rule/start"
-                                       title="Move up"
-                                       i18n:attributes="title"
-                                       tal:attributes="href string:${view/view_url}?operation=move_up&amp;rule_id=${rule/id}">
-                                        <tal:icon tal:replace="structure python:icons.tag('caret-up-fill', tag_class='', tag_alt='')" />
-                                    </a>
-                                    <a tal:condition="not:repeat/rule/end"
-                                       title="Move down"
-                                       i18n:attributes="title"
-                                       tal:attributes="href string:${view/view_url}?operation=move_down&amp;rule_id=${rule/id}">
-                                        <tal:icon tal:replace="structure python:icons.tag('caret-down-fill', tag_class='', tag_alt='')" />
-                                    </a>
-                                </td>
-                                <td class="checker listingCheckbox">
-                                    <tal:icon tal:condition="rule/bubbles"
-                                        i18n:attributes="alt label_contentrules_active;"
-                                        tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" />
-                                </td>
-                                <td class="checker listingCheckbox">
-                                    <tal:icon tal:condition="rule/enabled"
-                                        i18n:attributes="alt label_contentrules_active;"
-                                        tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" />
-                                </td>
-                                <td class="checker listingCheckbox">
-                                    <tal:icon tal:condition="rule/global_enabled"
-                                        i18n:attributes="alt label_contentrules_active;"
-                                        tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" />
-                                </td>
-                            </tr>
-                            </tal:rules>
-                        </tbody>
-                    </table>
-
-                    <div class="formControls">
-                        <button name="form.button.Enable"
-                               class="context btn btn-primary"
-                               type="submit"
-                               value="Enable"
-                               i18n:attributes="value label_enable;"
-                               i18n:translate="label_enable">Enable</button>
-                        <button name="form.button.Disable"
-                               class="standalone btn btn-primary"
-                               type="submit"
-                               value="Disable"
-                               i18n:attributes="value label_disable;"
-                               i18n:translate="label_disable">Disable</button>
-                        <button name="form.button.Bubble"
-                               class="standalone btn btn-primary"
-                               type="submit"
-                               value="Apply to subfolders"
-                               i18n:attributes="value label_apply_to_subfolders;"
-                               i18n:translate="label_apply_to_subfolders">Apply to subfolders</button>
-                        <button name="form.button.NoBubble"
-                               class="standalone btn btn-primary"
-                               type="submit"
-                               value="Disable apply to subfolders"
-                               i18n:attributes="value label_disable_apply_to_subfolders;"
-                               i18n:translate="label_disable_apply_to_subfolders">Disable apply to subfolders</button>
-                        <button name="form.button.Delete"
-                               class="destructive btn btn-danger"
-                               type="submit"
-                               value="Unassign"
-                               i18n:attributes="value label_unassign;"
-                               i18n:translate="label_unassign">Unassign</button>
-                    </div>
-                </form>
-            </div>
+                          </dd>
+                        </dl>
+                      </td>
+                      <td class="text-center">
+                        <a title="Move up"
+                           tal:condition="not:repeat/rule/start"
+                           tal:attributes="
+                             href string:${view/view_url}?operation=move_up&amp;rule_id=${rule/id};
+                           "
+                           i18n:attributes="title"
+                        >
+                          <tal:icon tal:replace="structure python:icons.tag('caret-up-fill', tag_class='', tag_alt='')" />
+                        </a>
+                        <a title="Move down"
+                           tal:condition="not:repeat/rule/end"
+                           tal:attributes="
+                             href string:${view/view_url}?operation=move_down&amp;rule_id=${rule/id};
+                           "
+                           i18n:attributes="title"
+                        >
+                          <tal:icon tal:replace="structure python:icons.tag('caret-down-fill', tag_class='', tag_alt='')" />
+                        </a>
+                      </td>
+                      <td class="checker listingCheckbox">
+                        <tal:icon tal:condition="rule/bubbles"
+                                  tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')"
+                                  i18n:attributes="alt label_contentrules_active;"
+                        />
+                      </td>
+                      <td class="checker listingCheckbox">
+                        <tal:icon tal:condition="rule/enabled"
+                                  tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')"
+                                  i18n:attributes="alt label_contentrules_active;"
+                        />
+                      </td>
+                      <td class="checker listingCheckbox">
+                        <tal:icon tal:condition="rule/global_enabled"
+                                  tal:replace="structure python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')"
+                                  i18n:attributes="alt label_contentrules_active;"
+                        />
+                      </td>
+                    </tr>
+                  </tal:rules>
+                </tbody>
+              </table>
+
+              <div class="formControls">
+                <button class="context btn btn-primary"
+                        name="form.button.Enable"
+                        type="submit"
+                        value="Enable"
+                        i18n:attributes="value label_enable;"
+                        i18n:translate="label_enable"
+                >Enable</button>
+                <button class="standalone btn btn-primary"
+                        name="form.button.Disable"
+                        type="submit"
+                        value="Disable"
+                        i18n:attributes="value label_disable;"
+                        i18n:translate="label_disable"
+                >Disable</button>
+                <button class="standalone btn btn-primary"
+                        name="form.button.Bubble"
+                        type="submit"
+                        value="Apply to subfolders"
+                        i18n:attributes="value label_apply_to_subfolders;"
+                        i18n:translate="label_apply_to_subfolders"
+                >Apply to subfolders</button>
+                <button class="standalone btn btn-primary"
+                        name="form.button.NoBubble"
+                        type="submit"
+                        value="Disable apply to subfolders"
+                        i18n:attributes="value label_disable_apply_to_subfolders;"
+                        i18n:translate="label_disable_apply_to_subfolders"
+                >Disable apply to subfolders</button>
+                <button class="destructive btn btn-danger"
+                        name="form.button.Delete"
+                        type="submit"
+                        value="Unassign"
+                        i18n:attributes="value label_unassign;"
+                        i18n:translate="label_unassign"
+                >Unassign</button>
+              </div>
+            </form>
+          </div>
         </div>
 
-    </article>
+      </article>
 
-</metal:body>
-</body>
+    </metal:body>
+  </body>
 </html>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/templates/manage-elements.pt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/templates/manage-elements.pt`

 * *Files 8% similar despite different names*

```diff
@@ -1,296 +1,400 @@
 <html xmlns="http://www.w3.org/1999/xhtml"
-    xml:lang="en"
-    lang="en"
-    xmlns:metal="http://xml.zope.org/namespaces/metal"
-    xmlns:tal="http://xml.zope.org/namespaces/tal"
-    xmlns:i18n="http://xml.zope.org/namespaces/i18n"
-    metal:use-macro="here/prefs_main_template/macros/master"
-    i18n:domain="plone">
-
-    <body>
-
-        <metal:main metal:fill-slot="prefs_configlet_main">
-
-            <header>
-                <h1 class="documentFirstHeading">
-                    <span i18n:translate="title_edit_contentrule">Edit content rule</span>:
-                    <span tal:replace="view/rule_title"></span>
-                </h1>
-
-                <p i18n:translate="contentrules_description_execution"
-                    class="lead">
+      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
+      xmlns:metal="http://xml.zope.org/namespaces/metal"
+      xmlns:tal="http://xml.zope.org/namespaces/tal"
+      lang="en"
+      metal:use-macro="here/prefs_main_template/macros/master"
+      xml:lang="en"
+      i18n:domain="plone"
+>
+
+  <body>
+
+    <metal:main metal:fill-slot="prefs_configlet_main">
+
+      <header>
+        <h1 class="documentFirstHeading">
+          <span i18n:translate="title_edit_contentrule">Edit content rule</span>:
+          <span tal:replace="view/rule_title"></span>
+        </h1>
+
+        <p class="lead"
+           i18n:translate="contentrules_description_execution"
+        >
                     Rules execute when a triggering event occurs. Rule actions will only
                     be invoked if all the rule's conditions are met. You can add new
                     actions and conditions using the buttons below.
-                </p>
-                <a href=""
-                    class="link-parent d-block"
-                    tal:attributes="href string:${portal_url}/@@rules-controlpanel"
-                    i18n:translate="go_to_contentrules_overview">
+        </p>
+        <a class="link-parent d-block"
+           href=""
+           tal:attributes="
+             href string:${portal_url}/@@rules-controlpanel;
+           "
+           i18n:translate="go_to_contentrules_overview"
+        >
                     Up to rule overview
-                </a>
-            </header>
+        </a>
+      </header>
 
-            <div id="content-core" class="pat-contentrules-elements">
-
-                <div class="row row-cols-1 row-cols-md-2">
-                    <fieldset id="configure-conditions" class="col"
-                        tal:define="conditions view/conditions">
-                        <legend i18n:translate="if_all_conditions_met" class="float-none">
+      <div class="pat-contentrules-elements"
+           id="content-core"
+      >
+
+        <div class="row row-cols-1 row-cols-md-2">
+          <fieldset class="col"
+                    id="configure-conditions"
+                    tal:define="
+                      conditions view/conditions;
+                    "
+          >
+            <legend class="float-none"
+                    i18n:translate="if_all_conditions_met"
+            >
                             If all of the following conditions are met:
-                        </legend>
+            </legend>
 
-                        <div tal:condition="not:conditions"
-                            class="alert alert-info">
-                            <strong i18n:translate="">Info</strong>
-                            <span i18n:translate="">
+            <div class="alert alert-info"
+                 tal:condition="not:conditions"
+            >
+              <strong i18n:translate="">Info</strong>
+              <span i18n:translate="">
                                 There is not any additional condition checked on this rule.
-                            </span>
-                        </div>
+              </span>
+            </div>
 
-                        <form class="mb-3"
-                            tal:attributes="action view/view_url"
-                            method="post"
-                            tal:define="auth_token context/@@authenticator/token"
-                            tal:repeat="condition conditions">
-                            <span tal:replace="structure context/@@authenticator/authenticator"></span>
-                            <a tal:attributes="name string:condition++${condition/idx}"></a>
-                            <input type="hidden"
-                                name="element_id:int"
-                                tal:attributes="value condition/idx" />
-
-                            <div class="card">
-                                <div class="card-body row">
-                                    <div class="col">
-                                        <h5 class="card-title"
-                                        tal:content="condition/title"
-                                        i18n:translate="">Transition was publish.</h5>
-                                    </div>
-                                    <div class="col-auto">
-                                        <div class="rule-operations">
-                                            <a tal:attributes="href string:${condition/editview}?_authenticator=${auth_token}"
-                                                class="pat-plone-modal btn btn-sm btn-primary"
-                                                tal:condition="condition/editview"
-                                                i18n:translate="label_edit">Edit</a>
-                                            <button type="submit"
-                                                name="form.button.DeleteCondition"
-                                                value="Remove"
-                                                class="context btn btn-sm btn-danger"
-                                                i18n:attributes="value label_remove;"
-                                                i18n:translate="label_remove">Remove</button>
-                                            <button tal:attributes="disabled python:condition['first'] and 'disabled' or None"
-                                                type="submit"
-                                                name="form.button.MoveConditionUp"
-                                                value="&uarr;"
-                                                class="context btn btn-sm btn-primary">&uarr;</button>
-                                            <button tal:attributes="disabled python:condition['last'] and 'disabled' or None"
-                                                type="submit"
-                                                name="form.button.MoveConditionDown"
-                                                value="&darr;"
-                                                class="context btn btn-sm btn-primary">&darr;</button>
-                                        </div>
-                                    </div>
-                                    <p class="card-text" tal:content="condition/summary">
+            <form class="mb-3"
+                  method="post"
+                  tal:define="
+                    auth_token context/@@authenticator/token;
+                  "
+                  tal:repeat="condition conditions"
+                  tal:attributes="
+                    action view/view_url;
+                  "
+            >
+              <span tal:replace="structure context/@@authenticator/authenticator"></span>
+              <a tal:attributes="
+                   name string:condition++${condition/idx};
+                 "></a>
+              <input name="element_id:int"
+                     type="hidden"
+                     tal:attributes="
+                       value condition/idx;
+                     "
+              />
+
+              <div class="card">
+                <div class="card-body row">
+                  <div class="col">
+                    <h5 class="card-title"
+                        tal:content="condition/title"
+                        i18n:translate=""
+                    >Transition was publish.</h5>
+                  </div>
+                  <div class="col-auto">
+                    <div class="rule-operations">
+                      <a class="pat-plone-modal btn btn-sm btn-primary"
+                         data-pat-plone-modal="modalSizeClass: modal-xl;"
+                         tal:condition="condition/editview"
+                         tal:attributes="
+                           href string:${condition/editview}?_authenticator=${auth_token};
+                         "
+                         i18n:translate="label_edit"
+                      >Edit</a>
+                      <button class="context btn btn-sm btn-danger"
+                              name="form.button.DeleteCondition"
+                              type="submit"
+                              value="Remove"
+                              i18n:attributes="value label_remove;"
+                              i18n:translate="label_remove"
+                      >Remove</button>
+                      <button class="context btn btn-sm btn-primary"
+                              name="form.button.MoveConditionUp"
+                              type="submit"
+                              value="&uarr;"
+                              tal:attributes="
+                                disabled python:condition['first'] and 'disabled' or None;
+                              "
+                      >&uarr;</button>
+                      <button class="context btn btn-sm btn-primary"
+                              name="form.button.MoveConditionDown"
+                              type="submit"
+                              value="&darr;"
+                              tal:attributes="
+                                disabled python:condition['last'] and 'disabled' or None;
+                              "
+                      >&darr;</button>
+                    </div>
+                  </div>
+                  <p class="card-text"
+                     tal:content="condition/summary"
+                  >
                                         Something happened
-                                    </p>
-                                </div>
-                            </div>
-                        </form>
-
-                        <form class="mb-3"
-                            tal:attributes="action string:${view/base_url}/+condition"
-                            method="get"
-                            id="add-condition">
-                            <span tal:replace="structure context/@@authenticator/authenticator"></span>
-                            <div class="input-group">
+                  </p>
+                </div>
+              </div>
+            </form>
 
-                                <span class="input-group-text" i18n:translate="contentrules_condition"
-                                    for="contentrules-add-condition">
+            <form class="mb-3"
+                  id="add-condition"
+                  method="get"
+                  tal:attributes="
+                    action string:${view/base_url}/+condition;
+                  "
+            >
+              <span tal:replace="structure context/@@authenticator/authenticator"></span>
+              <div class="input-group">
+
+                <span class="input-group-text"
+                      for="contentrules-add-condition"
+                      i18n:translate="contentrules_condition"
+                >
                                     Condition:
-                                </span>
+                </span>
 
-                                <select name=":action"
-                                    size="1"
-                                    id="contentrules-add-condition"
-                                    class="form-select"
-                                    aria-label="Add condition"
-                                    i18n:attributes="aria-label contentrules_add_condition">
-                                    <tal:block repeat="condition view/addable_conditions">
-                                        <option tal:attributes="value condition/addview"
-                                            i18n:translate=""
-                                            tal:content="condition/title" />
-                                    </tal:block>
-                                </select>
-                                <button class="context allowMultiSubmit btn btn-success"
-                                    type="submit"
-                                    name="form.button.AddCondition"
-                                    value="Add"
-                                    i18n:attributes="value label_add;"
-                                    i18n:translate="label_add">Add</button>
-                            </div>
-                            &nbsp; <!-- For Safari -->
-                        </form>
-                    </fieldset>
-
-                    <fieldset id="configure-actions" class="col"
-                        tal:define="actions view/actions">
-                        <legend i18n:translate="contentrules_perform_actions" class="float-none">
+                <select class="form-select"
+                        id="contentrules-add-condition"
+                        aria-label="Add condition"
+                        name=":action"
+                        size="1"
+                        i18n:attributes="aria-label contentrules_add_condition"
+                >
+                  <tal:block repeat="condition view/addable_conditions">
+                    <option tal:content="condition/title"
+                            tal:attributes="
+                              value condition/addview;
+                            "
+                            i18n:translate=""
+                    ></option>
+                  </tal:block>
+                </select>
+                <button class="context allowMultiSubmit btn btn-success"
+                        name="form.button.AddCondition"
+                        type="submit"
+                        value="Add"
+                        i18n:attributes="value label_add;"
+                        i18n:translate="label_add"
+                >Add</button>
+              </div>
+                            &nbsp;
+              <!-- For Safari -->
+            </form>
+          </fieldset>
+
+          <fieldset class="col"
+                    id="configure-actions"
+                    tal:define="
+                      actions view/actions;
+                    "
+          >
+            <legend class="float-none"
+                    i18n:translate="contentrules_perform_actions"
+            >
                             Perform the following actions:
-                        </legend>
+            </legend>
 
-                        <div tal:condition="not:actions"
-                            class="alert alert-warning">
-                            <strong i18n:translate="">Warning</strong>
-                            <span i18n:translate="">
+            <div class="alert alert-warning"
+                 tal:condition="not:actions"
+            >
+              <strong i18n:translate="">Warning</strong>
+              <span i18n:translate="">
                                 There is not any action performed by this rule.
                                 Click on Add button to setup an action.
-                            </span>
-                        </div>
-                        <form class="mb-3"
-                            tal:attributes="action view/view_url"
-                            method="post"
-                            tal:define="auth_token context/@@authenticator/token"
-                            tal:repeat="action actions">
-                            <span tal:replace="structure context/@@authenticator/authenticator"></span>
-                            <a tal:attributes="name string:action++${action/idx}"></a>
-                            <input type="hidden"
-                                name="element_id:int"
-                                tal:attributes="value action/idx" />
-
-                            <div class="card">
-                                <div class="card-body row">
-                                    <div class="col">
-                                        <h5 class="card-title"
-                                        tal:content="action/title"
-                                        i18n:translate="">Move to folder</h5>
-                                    </div>
-                                    <div class="col-auto">
-                                        <div class="rule-operations">
-                                            <a tal:attributes="href string:${action/editview}?_authenticator=${auth_token}"
-                                                class="pat-plone-modal btn btn-sm btn-primary"
-                                                tal:condition="action/editview"
-                                                i18n:translate="label_edit">Edit</a>
-                                            <button type="submit"
-                                                name="form.button.DeleteAction"
-                                                value="Remove"
-                                                class="context btn btn-sm btn-danger"
-                                                i18n:attributes="value label_remove;"
-                                                i18n:translate="label_remove">Remove</button>
-                                            <button tal:attributes="disabled python:action['first'] and 'disabled' or None"
-                                                type="submit"
-                                                name="form.button.MoveActionUp"
-                                                value="&uarr;"
-                                                class="context btn btn-sm btn-primary">&uarr;</button>
-                                            <button tal:attributes="disabled python:action['last'] and 'disabled' or None"
-                                                type="submit"
-                                                name="form.button.MoveActionDown"
-                                                value="&darr;"
-                                                class="context btn btn-sm btn-primary">&darr;</button>
-                                        </div>
-                                    </div>
-                                    <p class="card-text" tal:content="action/summary">
+              </span>
+            </div>
+            <form class="mb-3"
+                  method="post"
+                  tal:define="
+                    auth_token context/@@authenticator/token;
+                  "
+                  tal:repeat="action actions"
+                  tal:attributes="
+                    action view/view_url;
+                  "
+            >
+              <span tal:replace="structure context/@@authenticator/authenticator"></span>
+              <a tal:attributes="
+                   name string:action++${action/idx};
+                 "></a>
+              <input name="element_id:int"
+                     type="hidden"
+                     tal:attributes="
+                       value action/idx;
+                     "
+              />
+
+              <div class="card">
+                <div class="card-body row">
+                  <div class="col">
+                    <h5 class="card-title"
+                        tal:content="action/title"
+                        i18n:translate=""
+                    >Move to folder</h5>
+                  </div>
+                  <div class="col-auto">
+                    <div class="rule-operations">
+                      <a class="pat-plone-modal btn btn-sm btn-primary"
+                         data-pat-plone-modal="modalSizeClass: modal-xl;"
+                         tal:condition="action/editview"
+                         tal:attributes="
+                           href string:${action/editview}?_authenticator=${auth_token};
+                         "
+                         i18n:translate="label_edit"
+                      >Edit</a>
+                      <button class="context btn btn-sm btn-danger"
+                              name="form.button.DeleteAction"
+                              type="submit"
+                              value="Remove"
+                              i18n:attributes="value label_remove;"
+                              i18n:translate="label_remove"
+                      >Remove</button>
+                      <button class="context btn btn-sm btn-primary"
+                              name="form.button.MoveActionUp"
+                              type="submit"
+                              value="&uarr;"
+                              tal:attributes="
+                                disabled python:action['first'] and 'disabled' or None;
+                              "
+                      >&uarr;</button>
+                      <button class="context btn btn-sm btn-primary"
+                              name="form.button.MoveActionDown"
+                              type="submit"
+                              value="&darr;"
+                              tal:attributes="
+                                disabled python:action['last'] and 'disabled' or None;
+                              "
+                      >&darr;</button>
+                    </div>
+                  </div>
+                  <p class="card-text"
+                     tal:content="action/summary"
+                  >
                                         Something happened
-                                    </p>
-                                </div>
-                            </div>
-
-
-                        </form>
-
-                        <form class="mb-3"
-                            tal:attributes="action string:${view/base_url}/+action"
-                            method="get"
-                            id="add-action">
-                            <span tal:replace="structure context/@@authenticator/authenticator"></span>
-                            <div class="input-group">
-
-                                <span class="input-group-text"
-                                    i18n:translate="contentrules_action"
-                                    for="contentrules-add-action">Action:</span>
-
-                                <select name=":action"
-                                    size="1"
-                                    id="contentrules-add-action"
-                                    class="form-select"
-                                    aria-label="Add action"
-                                    i18n:attributes="aria-label contentrules_add_action">
-                                    <tal:block repeat="action view/addable_actions">
-                                        <option tal:attributes="value action/addview"
-                                            i18n:translate=""
-                                            tal:content="action/title"></option>
-                                    </tal:block>
-                                </select>
-                                <button class="context allowMultiSubmit btn btn-success"
-                                    type="submit"
-                                    name="form.button.AddAction"
-                                    value="Add"
-                                    i18n:attributes="value label_add;"
-                                    i18n:translate="label_add">Add</button>
-                            </div>
-                            &nbsp; <!-- For Safari -->
-                        </form>
-                    </fieldset>
+                  </p>
                 </div>
+              </div>
 
 
+            </form>
 
-                <tal:assignments define="assignments view/assignments">
-
-                    <fieldset id="manage-assignments" class="col">
-                        <legend i18n:translate="label_contentrules_rule_assignments" class="float-none">Assignments</legend>
-
-
-                        <tal:noassignments condition="not:assignments">
-                            <div class="alert alert-info">
-                                <strong i18n:translate="">This rule is not assigned to any location</strong>
-                                <tal:enabled condition="view/rule_enabled">
-                                    <div i18n:translate="">
+            <form class="mb-3"
+                  id="add-action"
+                  method="get"
+                  tal:attributes="
+                    action string:${view/base_url}/+action;
+                  "
+            >
+              <span tal:replace="structure context/@@authenticator/authenticator"></span>
+              <div class="input-group">
+
+                <span class="input-group-text"
+                      for="contentrules-add-action"
+                      i18n:translate="contentrules_action"
+                >Action:</span>
+
+                <select class="form-select"
+                        id="contentrules-add-action"
+                        aria-label="Add action"
+                        name=":action"
+                        size="1"
+                        i18n:attributes="aria-label contentrules_add_action"
+                >
+                  <tal:block repeat="action view/addable_actions">
+                    <option tal:content="action/title"
+                            tal:attributes="
+                              value action/addview;
+                            "
+                            i18n:translate=""
+                    ></option>
+                  </tal:block>
+                </select>
+                <button class="context allowMultiSubmit btn btn-success"
+                        name="form.button.AddAction"
+                        type="submit"
+                        value="Add"
+                        i18n:attributes="value label_add;"
+                        i18n:translate="label_add"
+                >Add</button>
+              </div>
+                            &nbsp;
+              <!-- For Safari -->
+            </form>
+          </fieldset>
+        </div>
+
+
+
+        <tal:assignments define="
+                           assignments view/assignments;
+                         ">
+
+          <fieldset class="col"
+                    id="manage-assignments"
+          >
+            <legend class="float-none"
+                    i18n:translate="label_contentrules_rule_assignments"
+            >Assignments</legend>
+
+
+            <tal:noassignments condition="not:assignments">
+              <div class="alert alert-info">
+                <strong i18n:translate="">This rule is not assigned to any location</strong>
+                <tal:enabled condition="view/rule_enabled">
+                  <div i18n:translate="">
                                         The rule is enabled but will perform nothing since it is not assigned anywhere.
-                                    </div>
-                                </tal:enabled>
-                            </div>
+                  </div>
+                </tal:enabled>
+              </div>
 
-                                <tal:enabled condition="view/rule_enabled">
-                                    <p i18n:translate="">
+              <tal:enabled condition="view/rule_enabled">
+                <p i18n:translate="">
                                         Go to the folder where you want the rule to apply, or at the site root,
                                         click on 'rule' tab, and then locally setup the rules.
-                                    </p>
+                </p>
 
-                                    <form class="mb-3"
-                                        tal:attributes="action view/view_url"
-                                        method="post">
-                                        <span tal:replace="structure context/@@authenticator/authenticator" />
-                                        <input type="submit"
-                                            class="btn btn-primary"
-                                            value="Apply rule on the whole site"
-                                            name="form.button.ApplyOnWholeSite"
-                                            i18n:attributes="value" />
-                                    </form>
-                                </tal:enabled>
-                        </tal:noassignments>
-                        <tal:assignments condition="nocall:assignments">
-                            <div class="card">
-                                <div class="card-header">
-                                    <span i18n:translate="description_contentrules_rule_assignments">
+                <form class="mb-3"
+                      method="post"
+                      tal:attributes="
+                        action view/view_url;
+                      "
+                >
+                  <span tal:replace="structure context/@@authenticator/authenticator"></span>
+                  <input class="btn btn-primary"
+                         name="form.button.ApplyOnWholeSite"
+                         type="submit"
+                         value="Apply rule on the whole site"
+                         i18n:attributes="value"
+                  />
+                </form>
+              </tal:enabled>
+            </tal:noassignments>
+            <tal:assignments condition="nocall:assignments">
+              <div class="card">
+                <div class="card-header">
+                  <span i18n:translate="description_contentrules_rule_assignments">
                                         This rule is assigned to the following locations:
-                                    </span>
-                                </div>
-                                <ul class="list-group list-group-flush">
-                                <tal:items repeat="assignment assignments">
-                                    <li class="list-group-item">
-                                        <a tal:attributes="href string:${assignment/url}/@@manage-content-rules">
-                                            <tal:icon tal:replace="structure python:icons.tag(assignment['icon'])" /><span class="ms-2" tal:content="assignment/title">title</span>
-                                        </a>&nbsp;
-                                    </li>
-                                </tal:items>
-                                </ul>
-                            </div>
-                        </tal:assignments>
-                    </fieldset>
-
-                </tal:assignments>
-
-            </div>
-        </metal:main>
-    </body>
+                  </span>
+                </div>
+                <ul class="list-group list-group-flush">
+                  <tal:items repeat="assignment assignments">
+                    <li class="list-group-item">
+                      <a tal:attributes="
+                           href string:${assignment/url}/@@manage-content-rules;
+                         ">
+                        <tal:icon tal:replace="structure python:icons.tag(assignment['icon'])" /><span class="ms-2"
+                              tal:content="assignment/title"
+                        >title</span>
+                      </a>&nbsp;
+                    </li>
+                  </tal:items>
+                </ul>
+              </div>
+            </tal:assignments>
+          </fieldset>
+
+        </tal:assignments>
+
+      </div>
+    </metal:main>
+  </body>
 </html>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/browser/traversal.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/browser/traversal.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/configure.zcml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/configure.zcml`

 * *Files 4% similar despite different names*

```diff
@@ -1,221 +1,225 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:browser="http://namespaces.zope.org/browser"
     xmlns:plone="http://namespaces.plone.org/plone"
-    i18n_domain="plone">
+    i18n_domain="plone"
+    >
 
-    <!-- needed since Plone 4.1 to use cmf permissions in ZCML declaration. -->
+  <!-- needed since Plone 4.1 to use cmf permissions in ZCML declaration. -->
 
-    <include package="Products.CMFCore" file="permissions.zcml"
-             xmlns:zcml="http://namespaces.zope.org/zcml"
-             zcml:condition="have plone-41" />
+  <include
+      xmlns:zcml="http://namespaces.zope.org/zcml"
+      package="Products.CMFCore"
+      file="permissions.zcml"
+      zcml:condition="have plone-41"
+      />
 
-    <!-- Portal type condition -->
+  <!-- Portal type condition -->
 
-    <adapter factory=".portaltype.PortalTypeConditionExecutor" />
+  <adapter factory=".portaltype.PortalTypeConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.PortalType"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".portaltype.PortalTypeAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.portaltype.IPortalTypeCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.portaltype.IPortalTypeCondition"
       class=".portaltype.PortalTypeEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.PortalType"
-        title="Content type"
-        description="Apply only when the current content object is of a particular type"
-        for="*"
-        event="zope.interface.interfaces.IObjectEvent"
-        addview="plone.conditions.PortalType"
-        editview="edit"
-        schema=".portaltype.IPortalTypeCondition"
-        factory=".portaltype.PortalTypeCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.PortalType"
+      title="Content type"
+      description="Apply only when the current content object is of a particular type"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".portaltype.IPortalTypeCondition"
+      factory=".portaltype.PortalTypeCondition"
+      addview="plone.conditions.PortalType"
+      editview="edit"
+      />
 
-    <!-- File extension condition -->
+  <!-- File extension condition -->
 
-    <adapter factory=".fileextension.FileExtensionConditionExecutor" />
+  <adapter factory=".fileextension.FileExtensionConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.FileExtension"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".fileextension.FileExtensionAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.fileextension.IFileExtensionCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.fileextension.IFileExtensionCondition"
       class=".fileextension.FileExtensionEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.FileExtension"
-        title="File Extension"
-        description="Apply only to a particular file extension"
-        for="*"
-        event="zope.interface.interfaces.IObjectEvent"
-        addview="plone.conditions.FileExtension"
-        editview="edit"
-        schema=".fileextension.IFileExtensionCondition"
-        factory=".fileextension.FileExtensionCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.FileExtension"
+      title="File Extension"
+      description="Apply only to a particular file extension"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".fileextension.IFileExtensionCondition"
+      factory=".fileextension.FileExtensionCondition"
+      addview="plone.conditions.FileExtension"
+      editview="edit"
+      />
 
-    <!-- Workflow state condition (for any object) -->
+  <!-- Workflow state condition (for any object) -->
 
-    <adapter factory=".wfstate.WorkflowStateConditionExecutor" />
+  <adapter factory=".wfstate.WorkflowStateConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.WorkflowState"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".wfstate.WorkflowStateAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.wfstate.IWorkflowStateCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.wfstate.IWorkflowStateCondition"
       class=".wfstate.WorkflowStateEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.WorkflowState"
-        title="Workflow state"
-        description="Apply only to a objects in a particular workflow state"
-        for="*"
-        event="zope.interface.interfaces.IObjectEvent"
-        addview="plone.conditions.WorkflowState"
-        editview="edit"
-        schema=".wfstate.IWorkflowStateCondition"
-        factory=".wfstate.WorkflowStateCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.WorkflowState"
+      title="Workflow state"
+      description="Apply only to a objects in a particular workflow state"
+      for="*"
+      event="zope.interface.interfaces.IObjectEvent"
+      schema=".wfstate.IWorkflowStateCondition"
+      factory=".wfstate.WorkflowStateCondition"
+      addview="plone.conditions.WorkflowState"
+      editview="edit"
+      />
 
-    <!-- Workflow transition condition (for any object) -->
+  <!-- Workflow transition condition (for any object) -->
 
-    <adapter factory=".wftransition.WorkflowTransitionConditionExecutor" />
+  <adapter factory=".wftransition.WorkflowTransitionConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.WorkflowTransition"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".wftransition.WorkflowTransitionAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.wftransition.IWorkflowTransitionCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.wftransition.IWorkflowTransitionCondition"
       class=".wftransition.WorkflowTransitionEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.WorkflowTransition"
-        title="Workflow transition"
-        description="Apply only when the executed transition was as specified"
-        for="*"
-        event="Products.CMFCore.interfaces.IActionSucceededEvent"
-        addview="plone.conditions.WorkflowTransition"
-        editview="edit"
-        schema=".wftransition.IWorkflowTransitionCondition"
-        factory=".wftransition.WorkflowTransitionCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.WorkflowTransition"
+      title="Workflow transition"
+      description="Apply only when the executed transition was as specified"
+      for="*"
+      event="Products.CMFCore.interfaces.IActionSucceededEvent"
+      schema=".wftransition.IWorkflowTransitionCondition"
+      factory=".wftransition.WorkflowTransitionCondition"
+      addview="plone.conditions.WorkflowTransition"
+      editview="edit"
+      />
 
-    <!-- Group condition -->
-    <adapter factory=".group.GroupConditionExecutor" />
+  <!-- Group condition -->
+  <adapter factory=".group.GroupConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.Group"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".group.GroupAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.group.IGroupCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.group.IGroupCondition"
       class=".group.GroupEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.Group"
-        title="User's group"
-        description="Apply only when the current user is in the given group"
-        for="*"
-        event="*"
-        addview="plone.conditions.Group"
-        editview="edit"
-        schema=".group.IGroupCondition"
-        factory=".group.GroupCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.Group"
+      title="User's group"
+      description="Apply only when the current user is in the given group"
+      for="*"
+      event="*"
+      schema=".group.IGroupCondition"
+      factory=".group.GroupCondition"
+      addview="plone.conditions.Group"
+      editview="edit"
+      />
 
-    <!-- Role condition -->
-    <adapter factory=".role.RoleConditionExecutor" />
+  <!-- Role condition -->
+  <adapter factory=".role.RoleConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.Role"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".role.RoleAddFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <browser:page
-      for="plone.app.contentrules.conditions.role.IRoleCondition"
+  <browser:page
       name="edit"
+      for="plone.app.contentrules.conditions.role.IRoleCondition"
       class=".role.RoleEditFormView"
       permission="plone.app.contentrules.ManageContentRules"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.Role"
-        title="User's role"
-        description="Apply only when the current user has the given role"
-        for="*"
-        event="*"
-        addview="plone.conditions.Role"
-        editview="edit"
-        schema=".role.IRoleCondition"
-        factory=".role.RoleCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.Role"
+      title="User's role"
+      description="Apply only when the current user has the given role"
+      for="*"
+      event="*"
+      schema=".role.IRoleCondition"
+      factory=".role.RoleCondition"
+      addview="plone.conditions.Role"
+      editview="edit"
+      />
 
-    <!-- TALES expression condition -->
+  <!-- TALES expression condition -->
 
-    <adapter factory=".talesexpression.TalesExpressionConditionExecutor" />
+  <adapter factory=".talesexpression.TalesExpressionConditionExecutor" />
 
-    <browser:page
-      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
+  <browser:page
       name="plone.conditions.TalesExpression"
+      for="plone.app.contentrules.browser.interfaces.IRuleConditionAdding"
       class=".talesexpression.TalesExpressionAddFormView"
       permission="cmf.ManagePortal"
       />
 
-    <browser:page
-      for=".talesexpression.ITalesExpressionCondition"
+  <browser:page
       name="edit"
+      for=".talesexpression.ITalesExpressionCondition"
       class=".talesexpression.TalesExpressionEditFormView"
       permission="cmf.ManagePortal"
       />
 
-    <plone:ruleCondition
-        name="plone.conditions.TalesExpression"
-        title="TALES expression"
-        description="Apply only when the result of a TALES expression is True"
-        for="*"
-        event="*"
-        addview="plone.conditions.TalesExpression"
-        editview="edit"
-        schema=".talesexpression.ITalesExpressionCondition"
-        factory=".talesexpression.TalesExpressionCondition"
-        />
+  <plone:ruleCondition
+      name="plone.conditions.TalesExpression"
+      title="TALES expression"
+      description="Apply only when the result of a TALES expression is True"
+      for="*"
+      event="*"
+      schema=".talesexpression.ITalesExpressionCondition"
+      factory=".talesexpression.TalesExpressionCondition"
+      addview="plone.conditions.TalesExpression"
+      editview="edit"
+      />
 
 </configure>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/fileextension.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/fileextension.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/group.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/group.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/portaltype.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/portaltype.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/role.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/role.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/talesexpression.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/talesexpression.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/wfstate.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/wfstate.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/conditions/wftransition.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/conditions/wftransition.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/configure.zcml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/configure.zcml`

 * *Files 4% similar despite different names*

```diff
@@ -1,163 +1,162 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:plone="http://namespaces.plone.org/plone"
     xmlns:zcml="http://namespaces.zope.org/zcml"
-    i18n_domain="plone">
+    i18n_domain="plone"
+    >
 
-    <include package="zope.annotation" />
-    <include package="plone.contentrules" />
-    <include package="plone.contentrules" file="meta.zcml" />
-    <include package="plone.stringinterp" />
+  <include package="zope.annotation" />
+  <include package="plone.contentrules" />
+  <include
+      package="plone.contentrules"
+      file="meta.zcml"
+      />
+  <include package="plone.stringinterp" />
 
-    <!-- Create permissions -->
+  <!-- Create permissions -->
 
-    <permission
-        id="plone.app.contentrules.ManageContentRules"
-        title="Content rules: Manage rules"
-       />
+  <permission
+      id="plone.app.contentrules.ManageContentRules"
+      title="Content rules: Manage rules"
+      />
 
-    <include package=".browser" />
-    <include package=".actions" />
-    <include package=".conditions" />
-    <include package=".exportimport" />
+  <include package=".browser" />
+  <include package=".actions" />
+  <include package=".conditions" />
+  <include package=".exportimport" />
 
-    <!-- Make any folder and the portal root a possible container for rules -->
+  <!-- Make any folder and the portal root a possible container for rules -->
 
-    <class class="Products.CMFPlone.Portal.PloneSite">
-        <implements interface="plone.contentrules.engine.interfaces.IRuleAssignable" />
-    </class>
+  <class class="Products.CMFPlone.Portal.PloneSite">
+    <implements interface="plone.contentrules.engine.interfaces.IRuleAssignable" />
+  </class>
 
-    <!-- Let rules be annotatable - used to keep track of rule-to-assignment mappings -->
+  <!-- Let rules be annotatable - used to keep track of rule-to-assignment mappings -->
 
-    <class class="plone.app.contentrules.rule.Rule">
-        <implements interface="zope.annotation.interfaces.IAttributeAnnotatable" />
-    </class>
+  <class class="plone.app.contentrules.rule.Rule">
+    <implements interface="zope.annotation.interfaces.IAttributeAnnotatable" />
+  </class>
 
-    <!-- Make the object related events selectable -->
+  <!-- Make the object related events selectable -->
 
-    <interface
+  <interface
       interface="zope.lifecycleevent.interfaces.IObjectAddedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="Object added to this container"
       />
 
-    <interface
+  <interface
       interface="zope.lifecycleevent.interfaces.IObjectRemovedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="Object removed from this container"
       />
 
-    <interface
+  <interface
       interface="zope.lifecycleevent.interfaces.IObjectModifiedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="Object modified"
       />
 
-    <interface
+  <interface
       interface="zope.lifecycleevent.interfaces.IObjectCopiedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="Object copied"
       />
 
-    <interface
+  <interface
       interface="Products.CMFCore.interfaces.IActionSucceededEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="Workflow state changed"
       />
 
-    <interface
+  <interface
       interface="Products.PluggableAuthService.interfaces.events.IUserLoggedInEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="User Logged in"
       />
 
-    <interface
+  <interface
       interface="Products.PluggableAuthService.interfaces.events.IUserLoggedOutEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="User Logged out"
       />
 
-    <interface
+  <interface
       interface="Products.PluggableAuthService.interfaces.events.IPrincipalCreatedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="User Created"
       />
 
-    <interface
+  <interface
       interface="Products.PluggableAuthService.interfaces.events.IPrincipalDeletedEvent"
       type="plone.contentrules.rule.interfaces.IRuleEventType"
       name="User Removed"
       />
 
-   <!-- Register handlers -->
+  <!-- Register handlers -->
 
-    <!-- Rule triggers -->
-    <subscriber
+  <!-- Rule triggers -->
+  <subscriber
       for="zope.lifecycleevent.interfaces.IObjectAddedEvent"
       handler=".handlers.added"
       />
-    <subscriber
-      zcml:condition="installed Products.Archetypes"
-      for="Products.Archetypes.interfaces.IObjectInitializedEvent"
-      handler=".handlers.archetypes_initialized"
-      />
-    <subscriber
+  <subscriber
       for="zope.lifecycleevent.interfaces.IObjectRemovedEvent"
       handler=".handlers.removed"
       />
-    <subscriber
+  <subscriber
       for="zope.lifecycleevent.interfaces.IObjectModifiedEvent"
       handler=".handlers.modified"
       />
-     <subscriber
+  <subscriber
       for="zope.lifecycleevent.interfaces.IObjectCopiedEvent"
       handler=".handlers.copied"
       />
-    <subscriber
+  <subscriber
       for="Products.CMFCore.interfaces.IActionSucceededEvent"
       handler=".handlers.workflow_action"
       />
-    <subscriber
+  <subscriber
       for="Products.PluggableAuthService.interfaces.events.IUserLoggedInEvent"
       handler=".handlers.user_logged_in"
-    />
-    <subscriber
+      />
+  <subscriber
       for="Products.PluggableAuthService.interfaces.events.IUserLoggedOutEvent"
       handler=".handlers.user_logged_out"
-    />
-    <subscriber
+      />
+  <subscriber
       for="Products.PluggableAuthService.interfaces.events.IPrincipalCreatedEvent"
       handler=".handlers.user_created"
-    />
-    <!-- Cleanup -->
-    <subscriber
-       for="zope.publisher.interfaces.IEndRequestEvent"
-       handler=".handlers.close"
-       />
-
-    <!-- Rule-to-assignment mappings -->
-    <subscriber
-        for="plone.contentrules.engine.interfaces.IRuleAssignable
-             zope.lifecycleevent.interfaces.IObjectMovedEvent"
-        handler=".rule.container_moved"
-        />
-    <subscriber
-        for="plone.contentrules.engine.interfaces.IRuleAssignable
-             zope.lifecycleevent.interfaces.IObjectRemovedEvent"
-        handler=".rule.container_removed"
-        />
-    <subscriber
-        for="plone.contentrules.rule.interfaces.IRule
-             zope.lifecycleevent.interfaces.IObjectRemovedEvent"
-        handler=".rule.rule_removed"
-        />
+      />
+  <!-- Cleanup -->
+  <subscriber
+      for="zope.publisher.interfaces.IEndRequestEvent"
+      handler=".handlers.close"
+      />
 
-    <!-- Register a name chooser explicitly -->
+  <!-- Rule-to-assignment mappings -->
+  <subscriber
+      for="plone.contentrules.engine.interfaces.IRuleAssignable
+           zope.lifecycleevent.interfaces.IObjectMovedEvent"
+      handler=".rule.container_moved"
+      />
+  <subscriber
+      for="plone.contentrules.engine.interfaces.IRuleAssignable
+           zope.lifecycleevent.interfaces.IObjectRemovedEvent"
+      handler=".rule.container_removed"
+      />
+  <subscriber
+      for="plone.contentrules.rule.interfaces.IRule
+           zope.lifecycleevent.interfaces.IObjectRemovedEvent"
+      handler=".rule.rule_removed"
+      />
 
-    <adapter
+  <!-- Register a name chooser explicitly -->
+
+  <adapter
+      factory=".namechooser.RuleNameChooser"
       provides="zope.container.interfaces.INameChooser"
       for="plone.contentrules.engine.interfaces.IRuleStorage"
-      factory=".namechooser.RuleNameChooser"
       />
 
 </configure>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/configure.zcml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/configure.zcml`

 * *Files 22% similar despite different names*

```diff
@@ -1,33 +1,33 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
-    i18n_domain="plone">
+    i18n_domain="plone"
+    >
 
-    <adapter
-        factory=".rules.RulesXMLAdapter"
-        name="plone.contentrules"
-        />
+  <adapter
+      factory=".rules.RulesXMLAdapter"
+      name="plone.contentrules"
+      />
 
-    <adapter
-        factory=".rules.PropertyRuleElementExportImportHandler"
-        />
+  <adapter factory=".rules.PropertyRuleElementExportImportHandler" />
 
-    <!-- Register import and export steps -->
-    <genericsetup:importStep
-        name="contentrules"
-        title="Content rules"
-        description="Import content rule definitions and assignments"
-        handler=".rules.importRules">
-        <depends name="componentregistry"/>
-        <depends name="content"/>
-        <depends name="workflow"/>
-    </genericsetup:importStep>
+  <!-- Register import and export steps -->
+  <genericsetup:importStep
+      name="contentrules"
+      title="Content rules"
+      description="Import content rule definitions and assignments"
+      handler=".rules.importRules"
+      >
+    <depends name="componentregistry" />
+    <depends name="content" />
+    <depends name="workflow" />
+  </genericsetup:importStep>
 
-    <genericsetup:exportStep
-        name="contentrules"
-        title="Content rules"
-        description="Export content rule definitions and assignments"
-        handler=".rules.exportRules"
-        />
+  <genericsetup:exportStep
+      name="contentrules"
+      title="Content rules"
+      description="Export content rule definitions and assignments"
+      handler=".rules.exportRules"
+      />
 
 </configure>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/interfaces.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/interfaces.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/exportimport/rules.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/exportimport/rules.py`

 * *Files 0% similar despite different names*

```diff
@@ -24,17 +24,15 @@
 from zope.component import adapter
 from zope.component import getUtility
 from zope.component import queryMultiAdapter
 from zope.component import queryUtility
 from zope.container.interfaces import INameChooser
 from zope.interface import implementer
 from zope.interface import Interface
-from zope.schema.interfaces import ICollection
 from zope.schema.interfaces import IField
-from zope.schema.interfaces import IFromUnicode
 
 
 def as_bool(string, default=False):
     if string is None or not str(string):
         return default
     return string.lower() == "true"
 
@@ -46,15 +44,14 @@
 
     def __init__(self, element):
         data = IRuleElementData(element)
         self.element = element
         self.descriptor = getUtility(IRuleElement, name=data.element)
 
     def import_element(self, node):
-
         if self.descriptor.schema is None:
             return
 
         for child in node.childNodes:
             if child.nodeName == "property":
                 self.import_node(self.descriptor.schema, child)
 
@@ -148,15 +145,14 @@
         site = self.environ.getSite()
         storage = queryUtility(IRuleStorage)
         if storage is None:
             return
 
         for child in node.childNodes:
             if child.nodeName == "rule":
-
                 rule = None
                 name = child.getAttribute("name")
                 if name:
                     rule = storage.get(name, None)
 
                 if rule is None:
                     rule = Rule()
@@ -301,15 +297,15 @@
                 handler.export_element(self._doc, action_node)
                 actions_node.appendChild(action_node)
             rule_node.appendChild(actions_node)
 
             fragment.appendChild(rule_node)
             assignment_paths.update(get_assignments(rule))
         # Export assignments last - this is necessary to ensure they
-        # are orderd properly
+        # are ordered properly
 
         site_path_length = len("/".join(site.getPhysicalPath()))
         for path in sorted(assignment_paths):
             try:
                 container = site.unrestrictedTraverse(path)
             except KeyError:
                 continue
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/handlers.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/handlers.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         return
 
     # Tell other event handlers to be equally kind
     rule_filter.in_progress = True
 
     # Prepare to break hard if a rule demanded execution be stopped
     try:
-
         # Try to execute rules in the context. It may not work if the context
         # is not a rule executor, but we may still want to bubble events
         executor = IRuleExecutor(context, None)
         if executor is not None:
             executor(event, bubbled=False, rule_filter=rule_filter)
 
         # Do not bubble beyond the site root
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/namechooser.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/namechooser.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/rule.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/rule.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 from zope.component import queryUtility
 
 
 ANNOTATION_KEY = "plone.app.contentrules.ruleassignments"
 
 
 class Rule(SimpleItem, BaseRule):
-    """A Zope 2 version of a rule, subject to acqusition, but otherwise
+    """A Zope 2 version of a rule, subject to acquisition, but otherwise
     identical.
     """
 
     __name__ = ""
 
     @property
     def id(self):
@@ -36,15 +36,14 @@
     if ANNOTATION_KEY not in annotations:
         annotations[ANNOTATION_KEY] = OOSet()
     annotations[ANNOTATION_KEY].insert(path)
 
 
 # Events that keep track of rule-to-assignment mappings
 def rule_removed(rule, event):
-
     storage = queryUtility(IRuleStorage)
     rule_name = rule.__name__
 
     if storage is None:
         return
 
     portal = getUtility(ISiteRoot)
@@ -53,15 +52,14 @@
         if container is not None:
             assignable = IRuleAssignmentManager(container, None)
             if assignable is not None and rule_name in assignable:
                 del assignable[rule_name]
 
 
 def container_moved(container, event):
-
     if event.oldParent is None or event.newParent is None or event.oldName is None:
         return
 
     assignable = IRuleAssignmentManager(container, None)
     storage = queryUtility(IRuleStorage)
 
     if assignable is None or storage is None:
@@ -83,15 +81,14 @@
             assignments = get_assignments(rule)
             if old_path in assignments:
                 assignments.remove(old_path)
                 assignments.insert(new_path)
 
 
 def container_removed(container, event):
-
     assignable = IRuleAssignmentManager(container, None)
     storage = queryUtility(IRuleStorage)
 
     if assignable is None or storage is None:
         return
 
     path = "/".join(container.getPhysicalPath())
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/testing.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/testing.py`

 * *Files 10% similar despite different names*

```diff
@@ -4,15 +4,14 @@
 from plone.app.testing import MOCK_MAILHOST_FIXTURE
 from plone.app.testing import PloneSandboxLayer
 
 import plone.app.contentrules
 
 
 class PloneAppContentrulesLayer(PloneSandboxLayer):
-
     defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)
 
     def setUpZope(self, app, configurationContext):
         self.loadZCML("testing.zcml", package=plone.app.contentrules.tests)
 
 
 PLONE_APP_CONTENTRULES_FIXTURE = PloneAppContentrulesLayer()
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/assignment.txt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/assignment.txt`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/base.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/base.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/dummy.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/dummy.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/multipublish.txt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/multipublish.txt`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/contentrules.xml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/contentrules.xml`

 * *Files 8% similar despite different names*

#### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/profiles/testing/contentrules.xml` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/profiles/testing/contentrules.xml`

```diff
@@ -1,10 +1,10 @@
 <?xml version="1.0" encoding="utf-8"?>
 <contentrules>
-  <rule name="test1" title="Test rule 1" description="A test rule" event="zope.lifecycleevent.interfaces.IObjectModifiedEvent" enabled="True" stop-after="False">
+  <rule description="A test rule" enabled="True" event="zope.lifecycleevent.interfaces.IObjectModifiedEvent" name="test1" stop-after="False" title="Test rule 1">
     <conditions>
       <condition type="plone.conditions.PortalType">
         <property name="check_types">
           <element>Document</element>
           <element>News Item</element>
         </property>
       </condition>
@@ -17,30 +17,30 @@
     <actions>
       <action type="plone.actions.Notify">
         <property name="message">A message: Hej då</property>
         <property name="message_type">info</property>
       </action>
     </actions>
   </rule>
-  <rule name="test2" title="Test rule 2" description="Another test rule" event="zope.lifecycleevent.interfaces.IObjectModifiedEvent" enabled="False" stop-after="True">
+  <rule description="Another test rule" enabled="False" event="zope.lifecycleevent.interfaces.IObjectModifiedEvent" name="test2" stop-after="True" title="Test rule 2">
     <conditions>
       <condition type="plone.conditions.PortalType">
         <property name="check_types">
           <element>Event</element>
         </property>
       </condition>
     </conditions>
     <actions>
       <action type="plone.actions.Workflow">
         <property name="transition">publish</property>
       </action>
     </actions>
   </rule>
-  <rule name="test3" title="Test rule 3" description="Third test rule" event="zope.lifecycleevent.interfaces.IObjectMovedEvent"/>
-  <rule name="test4" title="Test rule 4" description="We move published events in a folder" event="Products.CMFCore.interfaces.IActionSucceededEvent" enabled="True" stop-after="True">
+  <rule description="Third test rule" event="zope.lifecycleevent.interfaces.IObjectMovedEvent" name="test3" title="Test rule 3"/>
+  <rule description="We move published events in a folder" enabled="True" event="Products.CMFCore.interfaces.IActionSucceededEvent" name="test4" stop-after="True" title="Test rule 4">
     <conditions>
       <condition type="plone.conditions.PortalType">
         <property name="check_types">
           <element>Event</element>
         </property>
       </condition>
       <condition type="plone.conditions.WorkflowTransition">
@@ -51,27 +51,27 @@
     </conditions>
     <actions>
       <action type="plone.actions.Move">
         <property name="target_folder">/events</property>
       </action>
     </actions>
   </rule>
-  <rule name="test5" title="Test rule 5" description="Auto publish events" event="zope.lifecycleevent.interfaces.IObjectAddedEvent" enabled="True" cascading="True" stop-after="False">
+  <rule cascading="True" description="Auto publish events" enabled="True" event="zope.lifecycleevent.interfaces.IObjectAddedEvent" name="test5" stop-after="False" title="Test rule 5">
     <conditions>
       <condition type="plone.conditions.PortalType">
         <property name="check_types">
           <element>Event</element>
         </property>
       </condition>
     </conditions>
     <actions>
       <action type="plone.actions.Workflow">
         <property name="transition">publish</property>
       </action>
     </actions>
   </rule>
-  <assignment location="/news" name="test1" enabled="True" bubbles="False"/>
-  <assignment location="/news" name="test2" enabled="False" bubbles="True" insert-before="test1"/>
-  <assignment location="/news" name="test3" insert-before="*"/>
-  <assignment location="/" name="test4" insert-before="*" enabled="False"/>
-  <assignment location="/" name="test5" enabled="False"/>
+  <assignment bubbles="False" enabled="True" location="/news" name="test1"/>
+  <assignment bubbles="True" enabled="False" insert-before="test1" location="/news" name="test2"/>
+  <assignment insert-before="*" location="/news" name="test3"/>
+  <assignment enabled="False" insert-before="*" location="/" name="test4"/>
+  <assignment enabled="False" location="/" name="test5"/>
 </contentrules>
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/simplepublish.txt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/simplepublish.txt`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_copy.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_copy.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_delete.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_delete.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,14 +1,10 @@
 from plone.app.contentrules.actions.delete import DeleteAction
 from plone.app.contentrules.rule import Rule
 from plone.app.contentrules.tests.base import ContentRulesTestCase
-from plone.app.testing import login
-from plone.app.testing import setRoles
-from plone.app.testing import TEST_USER_ID
-from plone.app.testing import TEST_USER_NAME
 from plone.contentrules.engine.interfaces import IRuleStorage
 from plone.contentrules.rule.interfaces import IExecutable
 from plone.contentrules.rule.interfaces import IRuleAction
 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from zope.interface import implementer
 from zope.interface.interfaces import IObjectEvent
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_logger.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_logger.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 from plone.app.contentrules.actions.logger import LoggerAction
 from plone.app.contentrules.actions.logger import LoggerEditFormView
 from plone.app.contentrules.rule import Rule
 from plone.app.contentrules.tests.base import ContentRulesTestCase
-from plone.app.testing import TEST_USER_ID
 from plone.app.testing import TEST_USER_NAME
 from plone.contentrules.engine.interfaces import IRuleStorage
 from plone.contentrules.rule.interfaces import IExecutable
 from plone.contentrules.rule.interfaces import IRuleAction
 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from zope.interface import implementer
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_mail.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_mail.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,24 +1,21 @@
-from Acquisition import aq_base
 from email import message_from_bytes
 from plone.app.contentrules.actions.mail import MailAction
 from plone.app.contentrules.actions.mail import MailAddFormView
 from plone.app.contentrules.actions.mail import MailEditFormView
 from plone.app.contentrules.rule import Rule
 from plone.app.contentrules.tests.base import ContentRulesTestCase
 from plone.app.testing import setRoles
 from plone.app.testing import TEST_USER_ID
 from plone.base.interfaces.controlpanel import IMailSchema
 from plone.contentrules.engine.interfaces import IRuleStorage
 from plone.contentrules.rule.interfaces import IExecutable
 from plone.contentrules.rule.interfaces import IRuleAction
 from plone.registry.interfaces import IRegistry
-from Products.MailHost.interfaces import IMailHost
 from zope.component import getMultiAdapter
-from zope.component import getSiteManager
 from zope.component import getUtility
 from zope.interface import implementer
 from zope.interface.interfaces import IObjectEvent
 
 import unittest
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_modify.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_modify.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_move.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_move.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_notify.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_notify.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_versioning.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_versioning.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_action_workflow.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_action_workflow.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_browser.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_browser.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_cascading_rule.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_cascading_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 from plone.app.testing import TEST_USER_NAME
 from plone.dexterity.utils import createContentInContainer
 
 import unittest
 
 
 class TestCascadingRule(unittest.TestCase):
-
     layer = PLONE_APP_CONTENTRULES_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         login(self.portal, TEST_USER_NAME)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_group.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_group.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_portal_type.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_portal_type.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_role.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_role.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_tales_expression.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_tales_expression.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_wfstate.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_wfstate.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_condition_wftransition.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_condition_wftransition.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_configuration.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,14 @@
 from zope.lifecycleevent.interfaces import IObjectModifiedEvent
 
 import time
 import unittest
 
 
 class TestGenericSetup(unittest.TestCase):
-
     layer = PLONE_APP_CONTENTRULES_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         login(self.portal, TEST_USER_NAME)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
@@ -89,15 +88,15 @@
         assignable = IRuleAssignmentManager(self.portal.news)
         self.assertEqual({"test3", "test2", "test1"}, set(assignable.keys()))
 
     def testImportTwice(self):
         # Ensure rules, actions/conditions and assignments are not duplicated
         # if the profile is re-imported; see bug #8027.
         portal_setup = self.portal.portal_setup
-        time.sleep(1)  # avoid timestamp colission
+        time.sleep(1)  # avoid timestamp collision
         portal_setup.runAllImportStepsFromProfile(
             "profile-plone.app.contentrules:testing"
         )
 
         # We should get the same results as before
         self.testRuleInstalled()
         self.testRulesConfigured()
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_handlers.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_handlers.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_rule_assignment_mapping.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_rule_assignment_mapping.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,30 +1,28 @@
 from plone.app.contentrules import api
 from plone.app.contentrules.rule import get_assignments
 from plone.app.contentrules.rule import insert_assignment
 from plone.app.contentrules.rule import Rule
 from plone.app.contentrules.testing import (  # noqa: E501
     PLONE_APP_CONTENTRULES_FUNCTIONAL_TESTING,
 )
-from plone.app.contentrules.tests.base import ContentRulesTestCase
 from plone.app.testing import login
 from plone.app.testing import setRoles
 from plone.app.testing import TEST_USER_ID
 from plone.app.testing import TEST_USER_NAME
 from plone.contentrules.engine.assignments import RuleAssignment
 from plone.contentrules.engine.interfaces import IRuleAssignmentManager
 from plone.contentrules.engine.interfaces import IRuleStorage
 from zope.component import getUtility
 
 import transaction
 import unittest
 
 
 class TestRuleAssignmentMapping(unittest.TestCase):
-
     layer = PLONE_APP_CONTENTRULES_FUNCTIONAL_TESTING
 
     def setUp(self):
         self.portal = self.layer["portal"]
         self.request = self.layer["request"]
         login(self.portal, TEST_USER_NAME)
         setRoles(self.portal, TEST_USER_ID, ["Manager"])
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_rule_management_views.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_rule_management_views.py`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 from plone.contentrules.engine.interfaces import IRuleStorage
 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from zope.lifecycleevent.interfaces import IObjectModifiedEvent
 
 
 class DummyModifiedRule(Rule):
-
     title = "My test rule"
     description = "Test my rule"
     event = IObjectModifiedEvent
     enabled = True
 
 
 class TestRuleManagementViews(ContentRulesTestCase):
```

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_setup.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_traversal.py` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_traversal.py`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone/app/contentrules/tests/test_ui.txt` & `plone.app.contentrules-5.0.1/plone/app/contentrules/tests/test_ui.txt`

 * *Files identical despite different names*

### Comparing `plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/PKG-INFO` & `plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.contentrules
-Version: 5.0.0b2
+Version: 5.0.1
 Summary: Plone integration for plone.contentrules
 Home-page: https://pypi.org/project/plone.app.contentrules
 Author: Plone Foundation
 Author-email: plone-developers@lists.sourceforge.net
 License: GPL version 2
 Keywords: plone automatic content rules
 Classifier: Development Status :: 5 - Production/Stable
@@ -12,17 +12,19 @@
 Classifier: Framework :: Plone
 Classifier: Framework :: Plone :: 6.0
 Classifier: Framework :: Plone :: Core
 Classifier: Framework :: Zope :: 5
 Classifier: License :: OSI Approved :: GNU General Public License v2 (GPLv2)
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Python: >=3.8
 Provides-Extra: test
 
 Introduction
 ============
 
 plone.app.contentrules provides Plone-specific conditions and actions, as well
 as a user interface for plone.contentrules.
@@ -44,14 +46,43 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.1 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Explicitly mark exclude_actor as not-required
+  [erral] (#77)
+- Make modal action and condition editing modal screens bigger
+  [erral] (#78)
+
+
+Internal:
+
+
+- Update configuration files.
+  [plone devs] (#47959565)
+
+
+5.0.0 (2022-11-30)
+------------------
+
+Bug fixes:
+
+
+- Final release.
+  [gforcada] (#600)
+
+
 5.0.0b2 (2022-07-14)
 --------------------
 
 Bug fixes:
 
 
 - Remove unneeded i18n:translate call
@@ -202,15 +233,15 @@
   version.
 
 Bug fixes:
 
 - Migrate all tests to use dexterity
   [pbauer]
 
-- Work around issue where new item is moved before it's completely addeed
+- Work around issue where new item is moved before it's completely added
   [davisagli]
 
 - Fix all tests with py3 and py2
   [pbauer, alert, davisagli]
 
 
 4.0.18 (2018-02-04)
@@ -420,15 +451,15 @@
 ------------------
 
 - Fixed 3.0.4 regression: add/move/remove events where not handled
   anymore on discussion items.
   [thomasdesvenain]
 
 - Fixed reordering of actions / conditions.
-  This occured when 'jq' was not defined as 'jQuery'.
+  This occurred when 'jq' was not defined as 'jQuery'.
   [thomasdesvenain]
 
 - User that manage a rule can now allow actions executed by this rule
   to recursively trigger other rules.
   For example, if you have a rule that automatically publish added content,
   and an other rule that sends an email when a content is published,
   if autopublish rule is marked as 'cascading', then send mail rule will be triggered.
@@ -563,15 +594,15 @@
 ------------------
 
 - Adding a content rule is not handled by 'added' rule...
   Fixes infinite loop on adding a content rule.
   [thomasdesvenain]
 
 - ContainerModified event is excluded from 'modified' event handling.
-  This avoids for example adding a comment to lauch 'modified' rules registered for it.
+  This avoids for example adding a comment to launch 'modified' rules registered for it.
   [thomasdesvenain]
 
 
 2.1.7 (2012-08-04)
 ------------------
 
 - Added an option in email action
```

### Comparing `plone.app.contentrules-5.0.0b2/plone.app.contentrules.egg-info/SOURCES.txt` & `plone.app.contentrules-5.0.1/plone.app.contentrules.egg-info/SOURCES.txt`

 * *Files identical despite different names*

