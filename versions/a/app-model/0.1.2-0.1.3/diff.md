# Comparing `tmp/app_model-0.1.2.tar.gz` & `tmp/app_model-0.1.3.tar.gz`

## Comparing `app_model-0.1.2.tar` & `app_model-0.1.3.tar`

### file list

```diff
@@ -1,85 +1,85 @@
--rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 app_model-0.1.2/.github_changelog_generator
--rw-r--r--   0        0        0     1279 2020-02-02 00:00:00.000000 app_model-0.1.2/.pre-commit-config.yaml
--rw-r--r--   0        0        0      296 2020-02-02 00:00:00.000000 app_model-0.1.2/.readthedocs.yaml
--rw-r--r--   0        0        0    10374 2020-02-02 00:00:00.000000 app_model-0.1.2/CHANGELOG.md
--rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 app_model-0.1.2/codecov.yml
--rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 app_model-0.1.2/mkdocs.yml
--rw-r--r--   0        0        0      666 2020-02-02 00:00:00.000000 app_model-0.1.2/setup.py
--rw-r--r--   0        0        0      320 2020-02-02 00:00:00.000000 app_model-0.1.2/.github/ISSUE_TEMPLATE.md
--rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 app_model-0.1.2/.github/TEST_FAIL_TEMPLATE.md
--rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 app_model-0.1.2/.github/dependabot.yml
--rw-r--r--   0        0        0     4194 2020-02-02 00:00:00.000000 app_model-0.1.2/.github/workflows/ci.yml
--rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 app_model-0.1.2/.github/workflows/cron.yml
--rw-r--r--   0        0        0      253 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/keybinding_helper.py
--rw-r--r--   0        0        0     8203 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/model_app.py
--rw-r--r--   0        0        0     8316 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/qapplication.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/__init__.py
--rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/__main__.py
--rw-r--r--   0        0        0     2110 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/actions.py
--rw-r--r--   0        0        0      641 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/app.py
--rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/constants.py
--rw-r--r--   0        0        0      380 2020-02-02 00:00:00.000000 app_model-0.1.2/demo/multi_file/functions.py
--rw-r--r--   0        0        0     1589 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/_macros.py
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/application.md
--rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/expressions.md
--rw-r--r--   0        0        0     4479 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/index.md
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/keybindings.md
--rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/registries.md
--rw-r--r--   0        0        0      576 2020-02-02 00:00:00.000000 app_model-0.1.2/docs/types.md
--rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/__init__.py
--rw-r--r--   0        0        0     6589 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/_app.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/py.typed
--rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/__init__.py
--rw-r--r--   0        0        0      785 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/__init__.py
--rw-r--r--   0        0        0     6171 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_qaction.py
--rw-r--r--   0        0        0      686 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_qkeybindingedit.py
--rw-r--r--   0        0        0    16388 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_qkeymap.py
--rw-r--r--   0        0        0     1212 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_qmainwindow.py
--rw-r--r--   0        0        0     9755 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_qmenu.py
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/backends/qt/_util.py
--rw-r--r--   0        0        0      652 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/expressions/__init__.py
--rw-r--r--   0        0        0     4839 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/expressions/_context.py
--rw-r--r--   0        0        0     7164 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/expressions/_context_keys.py
--rw-r--r--   0        0        0    19026 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/expressions/_expressions.py
--rw-r--r--   0        0        0      347 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/registries/__init__.py
--rw-r--r--   0        0        0     6697 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/registries/_commands_reg.py
--rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/registries/_keybindings_reg.py
--rw-r--r--   0        0        0     4831 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/registries/_menus_reg.py
--rw-r--r--   0        0        0     8730 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/registries/_register.py
--rw-r--r--   0        0        0      924 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/__init__.py
--rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_action.py
--rw-r--r--   0        0        0      309 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_base.py
--rw-r--r--   0        0        0     3027 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_command_rule.py
--rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_constants.py
--rw-r--r--   0        0        0     1277 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_icon.py
--rw-r--r--   0        0        0     2391 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_keybinding_rule.py
--rw-r--r--   0        0        0     4000 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_menu_rule.py
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_utils.py
--rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_keys/__init__.py
--rw-r--r--   0        0        0    33529 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_keys/_key_codes.py
--rw-r--r--   0        0        0     8891 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_keys/_keybindings.py
--rw-r--r--   0        0        0     7804 2020-02-02 00:00:00.000000 app_model-0.1.2/src/app_model/types/_keys/_standard_bindings.py
--rw-r--r--   0        0        0     7135 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/conftest.py
--rw-r--r--   0        0        0     3736 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_actions.py
--rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_app.py
--rw-r--r--   0        0        0     1262 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_command_registry.py
--rw-r--r--   0        0        0     1264 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_key_codes.py
--rw-r--r--   0        0        0     3323 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_keybindings.py
--rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_registries.py
--rw-r--r--   0        0        0      664 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_types.py
--rw-r--r--   0        0        0      149 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/fixtures/fake_module.py
--rw-r--r--   0        0        0     2387 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_context/test_context.py
--rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_context/test_context_keys.py
--rw-r--r--   0        0        0     6992 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_context/test_expressions.py
--rw-r--r--   0        0        0      122 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/__init__.py
--rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_demos.py
--rw-r--r--   0        0        0     1409 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_qactions.py
--rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_qkeybindingedit.py
--rw-r--r--   0        0        0     7005 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_qkeymap.py
--rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_qmainwindow.py
--rw-r--r--   0        0        0     4312 2020-02-02 00:00:00.000000 app_model-0.1.2/tests/test_qt/test_qmenu.py
--rw-r--r--   0        0        0     1246 2020-02-02 00:00:00.000000 app_model-0.1.2/.gitignore
--rw-r--r--   0        0        0     1513 2020-02-02 00:00:00.000000 app_model-0.1.2/LICENSE
--rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 app_model-0.1.2/README.md
--rw-r--r--   0        0        0     4524 2020-02-02 00:00:00.000000 app_model-0.1.2/pyproject.toml
--rw-r--r--   0        0        0     3299 2020-02-02 00:00:00.000000 app_model-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 app_model-0.1.3/.github_changelog_generator
+-rw-r--r--   0        0        0     1279 2020-02-02 00:00:00.000000 app_model-0.1.3/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      296 2020-02-02 00:00:00.000000 app_model-0.1.3/.readthedocs.yaml
+-rw-r--r--   0        0        0    10845 2020-02-02 00:00:00.000000 app_model-0.1.3/CHANGELOG.md
+-rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 app_model-0.1.3/codecov.yml
+-rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 app_model-0.1.3/mkdocs.yml
+-rw-r--r--   0        0        0      666 2020-02-02 00:00:00.000000 app_model-0.1.3/setup.py
+-rw-r--r--   0        0        0      320 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/ISSUE_TEMPLATE.md
+-rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/TEST_FAIL_TEMPLATE.md
+-rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/dependabot.yml
+-rw-r--r--   0        0        0     4196 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/workflows/ci.yml
+-rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/workflows/cron.yml
+-rw-r--r--   0        0        0      253 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/keybinding_helper.py
+-rw-r--r--   0        0        0     8203 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/model_app.py
+-rw-r--r--   0        0        0     8316 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/qapplication.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/__init__.py
+-rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/__main__.py
+-rw-r--r--   0        0        0     2110 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/actions.py
+-rw-r--r--   0        0        0      641 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/app.py
+-rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/constants.py
+-rw-r--r--   0        0        0      380 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/functions.py
+-rw-r--r--   0        0        0     1589 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/_macros.py
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/application.md
+-rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/expressions.md
+-rw-r--r--   0        0        0     4479 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/index.md
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/keybindings.md
+-rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/registries.md
+-rw-r--r--   0        0        0      576 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/types.md
+-rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/__init__.py
+-rw-r--r--   0        0        0     6589 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/_app.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/py.typed
+-rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/__init__.py
+-rw-r--r--   0        0        0      821 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/__init__.py
+-rw-r--r--   0        0        0     6171 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qaction.py
+-rw-r--r--   0        0        0      686 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qkeybindingedit.py
+-rw-r--r--   0        0        0    16388 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qkeymap.py
+-rw-r--r--   0        0        0     1212 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qmainwindow.py
+-rw-r--r--   0        0        0    12288 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qmenu.py
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_util.py
+-rw-r--r--   0        0        0      652 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/__init__.py
+-rw-r--r--   0        0        0     4839 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_context.py
+-rw-r--r--   0        0        0     7164 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_context_keys.py
+-rw-r--r--   0        0        0    19026 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_expressions.py
+-rw-r--r--   0        0        0      347 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/__init__.py
+-rw-r--r--   0        0        0     6697 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_commands_reg.py
+-rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_keybindings_reg.py
+-rw-r--r--   0        0        0     4831 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_menus_reg.py
+-rw-r--r--   0        0        0     8730 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_register.py
+-rw-r--r--   0        0        0      924 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/__init__.py
+-rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_action.py
+-rw-r--r--   0        0        0      309 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_base.py
+-rw-r--r--   0        0        0     3027 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_command_rule.py
+-rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_constants.py
+-rw-r--r--   0        0        0     1277 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_icon.py
+-rw-r--r--   0        0        0     2391 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keybinding_rule.py
+-rw-r--r--   0        0        0     4000 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_menu_rule.py
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_utils.py
+-rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/__init__.py
+-rw-r--r--   0        0        0    33529 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_key_codes.py
+-rw-r--r--   0        0        0     8891 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_keybindings.py
+-rw-r--r--   0        0        0     7804 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_standard_bindings.py
+-rw-r--r--   0        0        0     7135 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/conftest.py
+-rw-r--r--   0        0        0     3736 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_actions.py
+-rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_app.py
+-rw-r--r--   0        0        0     1262 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_command_registry.py
+-rw-r--r--   0        0        0     1264 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_key_codes.py
+-rw-r--r--   0        0        0     3323 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_keybindings.py
+-rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_registries.py
+-rw-r--r--   0        0        0      664 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_types.py
+-rw-r--r--   0        0        0      149 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/fixtures/fake_module.py
+-rw-r--r--   0        0        0     2387 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_context.py
+-rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_context_keys.py
+-rw-r--r--   0        0        0     6992 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_expressions.py
+-rw-r--r--   0        0        0      122 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/__init__.py
+-rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_demos.py
+-rw-r--r--   0        0        0     1409 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qactions.py
+-rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qkeybindingedit.py
+-rw-r--r--   0        0        0     7005 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qkeymap.py
+-rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qmainwindow.py
+-rw-r--r--   0        0        0     5506 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qmenu.py
+-rw-r--r--   0        0        0     1246 2020-02-02 00:00:00.000000 app_model-0.1.3/.gitignore
+-rw-r--r--   0        0        0     1513 2020-02-02 00:00:00.000000 app_model-0.1.3/LICENSE
+-rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 app_model-0.1.3/README.md
+-rw-r--r--   0        0        0     4534 2020-02-02 00:00:00.000000 app_model-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0     3299 2020-02-02 00:00:00.000000 app_model-0.1.3/PKG-INFO
```

### Comparing `app_model-0.1.2/.pre-commit-config.yaml` & `app_model-0.1.3/.pre-commit-config.yaml`

 * *Files 3% similar despite different names*

```diff
@@ -16,40 +16,40 @@
     rev: v4.4.0
     hooks:
       - id: check-docstring-first
       - id: end-of-file-fixer
       - id: trailing-whitespace
 
   - repo: https://github.com/psf/black
-    rev: 23.1.0
+    rev: 23.3.0
     hooks:
       - id: black
 
   - repo: https://github.com/charliermarsh/ruff-pre-commit
-    rev: v0.0.254
+    rev: v0.0.260
     hooks:
       - id: ruff
         args: ["--fix"]
 
   - repo: https://github.com/abravalheri/validate-pyproject
-    rev: v0.12.1
+    rev: v0.12.2
     hooks:
       - id: validate-pyproject
 
   - repo: https://github.com/pre-commit/mirrors-mypy
-    rev: v1.0.1
+    rev: v1.1.1
     hooks:
       - id: mypy
         files: "^src/"
         additional_dependencies:
           - pydantic
           - in-n-out
 
   # manual hooks
 
   - repo: https://github.com/codespell-project/codespell
-    rev: v2.2.2
+    rev: v2.2.4
     hooks:
       - id: codespell
         exclude: CHANGELOG.md
         stages:
           - "manual"
```

### Comparing `app_model-0.1.2/CHANGELOG.md` & `app_model-0.1.3/CHANGELOG.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,18 @@
 # Changelog
 
+## [0.1.3](https://github.com/pyapp-kit/app-model/tree/0.1.3) (2023-04-06)
+
+[Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.2...0.1.3)
+
+**Merged pull requests:**
+
+- fix: don't use mixin for menus [\#95](https://github.com/pyapp-kit/app-model/pull/95) ([tlambert03](https://github.com/tlambert03))
+- ci: \[pre-commit.ci\] autoupdate [\#92](https://github.com/pyapp-kit/app-model/pull/92) ([pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci))
+
 ## [v0.1.2](https://github.com/pyapp-kit/app-model/tree/v0.1.2) (2023-03-07)
 
 [Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.1...v0.1.2)
 
 **Fixed bugs:**
 
 - fix: Fix typo in execute\_command method [\#86](https://github.com/pyapp-kit/app-model/pull/86) ([davidbrochart](https://github.com/davidbrochart))
```

### Comparing `app_model-0.1.2/mkdocs.yml` & `app_model-0.1.3/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/setup.py` & `app_model-0.1.3/setup.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/.github/workflows/ci.yml` & `app_model-0.1.3/.github/workflows/ci.yml`

 * *Files 2% similar despite different names*

```diff
@@ -77,15 +77,15 @@
       - name: Install dependencies
         run: |
           python -m pip install -U pip
           python -m pip install -e .[qt,test,test-qt]
           python -m pip install ${{ matrix.qt-backend }}
 
       - name: Test
-        uses: coactions/setup-xvfb@v1
+        uses: aganders3/headless-gui@v1
         with:
           run: python -m pytest -s --cov=app_model --cov-report=xml --cov-report=term-missing --color=yes
 
       - name: Coverage
         uses: codecov/codecov-action@v3
 
   test_napari:
```

### Comparing `app_model-0.1.2/.github/workflows/cron.yml` & `app_model-0.1.3/.github/workflows/cron.yml`

 * *Files 8% similar despite different names*

```diff
@@ -37,15 +37,15 @@
       - name: Install dependencies
         run: |
           python -m pip install -U pip
           python -m pip install --pre -e .[qt,test,test-qt]
           python -m pip install --pre ${{ matrix.qt-backend }}
 
       - name: Test
-        uses: GabrielBB/xvfb-action@v1
+        uses: aganders3/headless-gui@v1
         with:
           run: python -m pytest -s --color=yes
 
       # If something goes wrong, we can open an issue in the repo
       - name: Report Failures
         if: ${{ failure() }}
         uses: JasonEtco/create-an-issue@v2
```

### Comparing `app_model-0.1.2/demo/model_app.py` & `app_model-0.1.3/demo/model_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/demo/qapplication.py` & `app_model-0.1.3/demo/qapplication.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/demo/multi_file/actions.py` & `app_model-0.1.3/demo/multi_file/actions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/demo/multi_file/app.py` & `app_model-0.1.3/demo/multi_file/app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/docs/_macros.py` & `app_model-0.1.3/docs/_macros.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/docs/index.md` & `app_model-0.1.3/docs/index.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/docs/types.md` & `app_model-0.1.3/docs/types.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/_app.py` & `app_model-0.1.3/src/app_model/_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/backends/qt/__init__.py` & `app_model-0.1.3/src/app_model/backends/qt/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,15 +5,15 @@
     QKeyBindingSequence,
     qkey2modelkey,
     qkeycombo2modelkey,
     qkeysequence2modelkeybinding,
     qmods2modelmods,
 )
 from ._qmainwindow import QModelMainWindow
-from ._qmenu import QModelMenu, QModelMenuBar, QModelSubmenu
+from ._qmenu import QModelMenu, QModelMenuBar, QModelSubmenu, QModelToolBar
 from ._util import to_qicon
 
 __all__ = [
     "QCommandAction",
     "QCommandRuleAction",
     "qkey2modelkey",
     "QKeyBindingSequence",
@@ -21,10 +21,11 @@
     "qkeysequence2modelkeybinding",
     "QMenuItemAction",
     "QModelKeyBindingEdit",
     "QModelMainWindow",
     "QModelMenu",
     "QModelMenuBar",
     "QModelSubmenu",
+    "QModelToolBar",
     "qmods2modelmods",
     "to_qicon",
 ]
```

### Comparing `app_model-0.1.2/src/app_model/backends/qt/_qaction.py` & `app_model-0.1.3/src/app_model/backends/qt/_qaction.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/backends/qt/_qkeybindingedit.py` & `app_model-0.1.3/src/app_model/backends/qt/_qkeybindingedit.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/backends/qt/_qkeymap.py` & `app_model-0.1.3/src/app_model/backends/qt/_qkeymap.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/backends/qt/_qmainwindow.py` & `app_model-0.1.3/src/app_model/backends/qt/_qmainwindow.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/backends/qt/_qmenu.py` & `app_model-0.1.3/src/app_model/backends/qt/_qmenu.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 from __future__ import annotations
 
 from typing import (
     TYPE_CHECKING,
     Collection,
+    Iterable,
     List,
     Mapping,
     Optional,
-    Protocol,
     Set,
     Union,
+    cast,
 )
 
-from qtpy.QtCore import QObject
 from qtpy.QtWidgets import QMenu, QMenuBar, QToolBar
 
 from app_model import Application
 from app_model.types import SubmenuItem
 
 from ._qaction import QCommandRuleAction, QMenuItemAction
 from ._util import to_qicon
@@ -25,72 +25,63 @@
 except ImportError:
     QT6 = False
 
 if TYPE_CHECKING:
     from qtpy.QtWidgets import QAction, QWidget
 
 
-# fmt: off
-class _AcceptsMenus(Protocol):
-    _app: Application
-    def clear(self) -> None: ...
-    def addMenu(self, menu: QMenu) -> None: ...
-    def addAction(self, menu: QAction) -> None: ...
-    def addSeparator(self) -> None: ...
-
-# fmt: on
-
+class QModelMenu(QMenu):
+    """QMenu for a menu_id in an `app_model` MenusRegistry.
 
-class _MenuMixin(QObject):
-    _app: Application
-    _menu_id: str
+    Parameters
+    ----------
+    menu_id : str
+        Menu ID to look up in the registry.
+    app : Union[str, Application]
+        Application instance or name of application instance.
+    title : Optional[str]
+        Optional title for the menu, by default None
+    parent : Optional[QWidget]
+        Optional parent widget, by default None
+    """
 
     def __init__(
         self,
         menu_id: str,
         app: Union[str, Application],
+        title: Optional[str] = None,
+        parent: Optional[QWidget] = None,
     ):
+        QMenu.__init__(self, parent)
+
+        # NOTE: code duplication with QModelToolBar, but Qt mixins and multiple
+        # inheritance are problematic for some versions of Qt, and for typing
         assert isinstance(menu_id, str), f"Expected str, got {type(menu_id)!r}"
         self._menu_id = menu_id
         self._app = Application.get_or_create(app) if isinstance(app, str) else app
         self.setObjectName(menu_id)
         self.rebuild()
         self._app.menus.menus_changed.connect(self._on_registry_changed)
         self.destroyed.connect(self._disconnect)
+        # ----------------------
 
-    def _disconnect(self) -> None:
-        self._app.menus.menus_changed.disconnect(self._on_registry_changed)
-
-    def _on_registry_changed(self, changed_ids: Set[str]) -> None:
-        if self._menu_id in changed_ids:
-            self.rebuild()
+        if title is not None:
+            self.setTitle(title)
+        self.aboutToShow.connect(self._on_about_to_show)
 
-    def rebuild(
-        self: _MenuMixin,
-        include_submenus: bool = True,
-        exclude: Optional[Collection[str]] = None,
-    ) -> None:
-        """Rebuild menu by looking up self._menu_id in menu_registry."""
-        self.clear()
-        _exclude = exclude or set()
+    def findAction(self, object_name: str) -> Union[QAction, QModelMenu, None]:
+        """Find an action by its ObjectName.
 
-        groups = list(self._app.menus.iter_menu_groups(self._menu_id))
-        n_groups = len(groups)
-        for n, group in enumerate(groups):
-            for item in group:
-                if isinstance(item, SubmenuItem) and include_submenus:
-                    submenu = QModelSubmenu(item, self._app, parent=self)
-                    self.addMenu(submenu)
-                elif item.command.id not in _exclude:  # type: ignore
-                    action = QMenuItemAction(
-                        item, app=self._app, parent=self  # type: ignore
-                    )
-                    self.addAction(action)
-            if n < n_groups - 1:
-                self.addSeparator()
+        Parameters
+        ----------
+        object_name : str
+            Action ID to find. Note that `QCommandAction` have `ObjectName` set
+            to their `command.id`
+        """
+        return _find_action(self.actions(), object_name)
 
     def update_from_context(
         self, ctx: Mapping[str, object], _recurse: bool = True
     ) -> None:
         """Update the enabled/visible state of each menu item with `ctx`.
 
         See `app_model.expressions` for details on expressions.
@@ -101,73 +92,41 @@
             A namespace that will be used to `eval()` the `'enablement'` and
             `'when'` expressions provided for each action in the menu.
             *ALL variables used in these expressions must either be present in
             the `ctx` dict, or be builtins*.
         _recurse : bool
             recursion check, internal use only
         """
-        for action in self.actions():
-            if isinstance(action, QMenuItemAction):
-                action.update_from_context(ctx)
-            elif not QT6 and isinstance(menu := action.menu(), QModelMenu):
-                menu.update_from_context(ctx)
-            elif isinstance(parent := action.parent(), QModelMenu):
-                # FIXME: this is a hack for Qt6 that I don't entirely understand.
-                # QAction has lost the `.menu()` method, and it's a bit hard to find
-                # how to get to the parent menu now. Checking parent() seems to work,
-                # but I'm not sure if it's the right thing to do, and it leads to a
-                # recursion error.  I stop it with the _recurse flag here, but I wonder
-                # whether that will cause other problems.
-                if _recurse:
-                    parent.update_from_context(ctx, _recurse=False)
-
+        _update_from_context(self.actions(), ctx, _recurse=_recurse)
 
-class QModelMenu(QMenu, _MenuMixin):
-    """QMenu for a menu_id in an `app_model` MenusRegistry.
-
-    Parameters
-    ----------
-    menu_id : str
-        Menu ID to look up in the registry.
-    app : Union[str, Application]
-        Application instance or name of application instance.
-    parent : Optional[QWidget]
-        Optional parent widget, by default None
-    """
-
-    def __init__(
-        self,
-        menu_id: str,
-        app: Union[str, Application],
-        title: Optional[str] = None,
-        parent: Optional[QWidget] = None,
-    ):
-        QMenu.__init__(self, parent)
-        _MenuMixin.__init__(self, menu_id, app)
-        if title is not None:
-            self.setTitle(title)
-        self.aboutToShow.connect(self._on_about_to_show)
-
-    def findAction(self, object_name: str) -> Union[QAction, QModelMenu, None]:
-        """Find an action by its ObjectName.
-
-        Parameters
-        ----------
-        object_name : str
-            Action ID to find. Note that `QCommandAction` have `ObjectName` set
-            to their `command.id`
-        """
-        return next((a for a in self.actions() if a.objectName() == object_name), None)
+    def rebuild(
+        self, include_submenus: bool = True, exclude: Optional[Collection[str]] = None
+    ) -> None:
+        """Rebuild menu by looking up self._menu_id in menu_registry."""
+        _rebuild(
+            menu=self,
+            app=self._app,
+            menu_id=self._menu_id,
+            include_submenus=include_submenus,
+            exclude=exclude,
+        )
 
     def _on_about_to_show(self) -> None:
         # this would also be a reasonable place to call
         for action in self.actions():
             if isinstance(action, QCommandRuleAction):
                 action._refresh()
 
+    def _disconnect(self) -> None:
+        self._app.menus.menus_changed.disconnect(self._on_registry_changed)
+
+    def _on_registry_changed(self, changed_ids: Set[str]) -> None:
+        if self._menu_id in changed_ids:
+            self.rebuild()
+
 
 class QModelSubmenu(QModelMenu):
     """QMenu for a menu_id in an `app_model` MenusRegistry.
 
     Parameters
     ----------
     submenu : SubmenuItem
@@ -199,40 +158,108 @@
         super().update_from_context(ctx)
         self.setEnabled(expr.eval(ctx) if (expr := self._submenu.enablement) else True)
         # TODO: ... visibility needs to be controlled at the level of placement
         # in the submenu.  consider only using the `when` expression
         # self.setVisible(expr.eval(ctx) if (expr := self._submenu.when) else True)
 
 
-class QModelToolBar(QToolBar, _MenuMixin):
-    """QToolBar that is built from a list of model menu ids."""
+class QModelToolBar(QToolBar):
+    """QToolBar that is built from a list of model menu ids.
+
+    Parameters
+    ----------
+    menu_id : str
+        Menu ID to look up in the registry.
+    app : Union[str, Application]
+        Application instance or name of application instance.
+    exclude : Optional[Collection[str]]
+        Optional list of menu ids to exclude from the toolbar, by default None
+    title : Optional[str]
+        Optional title for the menu, by default None
+    parent : Optional[QWidget]
+        Optional parent widget, by default None
+    """
 
     def __init__(
         self,
         menu_id: str,
         app: Union[str, Application],
         *,
         exclude: Optional[Collection[str]] = None,
         title: Optional[str] = None,
         parent: Optional[QWidget] = None,
     ) -> None:
         self._exclude = exclude
         QToolBar.__init__(self, parent)
-        _MenuMixin.__init__(self, menu_id, app)
+
+        # NOTE: code duplication with QModelMenu, but Qt mixins and multiple
+        # inheritance are problematic for some versions of Qt, and for typing
+        assert isinstance(menu_id, str), f"Expected str, got {type(menu_id)!r}"
+        self._menu_id = menu_id
+        self._app = Application.get_or_create(app) if isinstance(app, str) else app
+        self.setObjectName(menu_id)
+        self.rebuild()
+        self._app.menus.menus_changed.connect(self._on_registry_changed)
+        self.destroyed.connect(self._disconnect)
+        # ----------------------
+
         if title is not None:
             self.setWindowTitle(title)
 
+    def addMenu(self, menu: QMenu) -> None:
+        """No-op for toolbar."""
+
+    def findAction(self, object_name: str) -> Union[QAction, QModelMenu, None]:
+        """Find an action by its ObjectName.
+
+        Parameters
+        ----------
+        object_name : str
+            Action ID to find. Note that `QCommandAction` have `ObjectName` set
+            to their `command.id`
+        """
+        return _find_action(self.actions(), object_name)
+
+    def update_from_context(
+        self, ctx: Mapping[str, object], _recurse: bool = True
+    ) -> None:
+        """Update the enabled/visible state of each menu item with `ctx`.
+
+        See `app_model.expressions` for details on expressions.
+
+        Parameters
+        ----------
+        ctx : Mapping
+            A namespace that will be used to `eval()` the `'enablement'` and
+            `'when'` expressions provided for each action in the menu.
+            *ALL variables used in these expressions must either be present in
+            the `ctx` dict, or be builtins*.
+        _recurse : bool
+            recursion check, internal use only
+        """
+        _update_from_context(self.actions(), ctx, _recurse=_recurse)
+
     def rebuild(
         self, include_submenus: bool = True, exclude: Optional[Collection[str]] = None
     ) -> None:
         """Rebuild toolbar by looking up self._menu_id in menu_registry."""
-        super().rebuild(include_submenus=include_submenus, exclude=self._exclude)
+        _rebuild(
+            menu=self,
+            app=self._app,
+            menu_id=self._menu_id,
+            include_submenus=include_submenus,
+            exclude=self._exclude if exclude is None else exclude,
+        )
 
-    def addMenu(self, menu: QMenu) -> None:
-        """No-op for toolbar."""
+    def _disconnect(self) -> None:
+        self._app.menus.menus_changed.disconnect(self._on_registry_changed)
+
+    def _on_registry_changed(self, changed_ids: Set[str]) -> None:
+        if self._menu_id in changed_ids:
+            self.rebuild()
 
 
 class QModelMenuBar(QMenuBar):
     """QMenuBar that is built from a list of model menu ids."""
 
     def __init__(
         self,
@@ -258,21 +285,73 @@
             A namespace that will be used to `eval()` the `'enablement'` and
             `'when'` expressions provided for each action in the menu.
             *ALL variables used in these expressions must either be present in
             the `ctx` dict, or be builtins*.
         _recurse : bool
             recursion check, internal use only
         """
-        for action in self.actions():
-            if isinstance(action, QMenuItemAction):
-                action.update_from_context(ctx)
-            elif not QT6 and isinstance(menu := action.menu(), QModelMenu):
-                menu.update_from_context(ctx)
-            elif isinstance(parent := action.parent(), QModelMenu):
-                # FIXME: this is a hack for Qt6 that I don't entirely understand.
-                # QAction has lost the `.menu()` method, and it's a bit hard to find
-                # how to get to the parent menu now. Checking parent() seems to work,
-                # but I'm not sure if it's the right thing to do, and it leads to a
-                # recursion error.  I stop it with the _recurse flag here, but I wonder
-                # whether that will cause other problems.
-                if _recurse:
-                    parent.update_from_context(ctx, _recurse=False)
+        _update_from_context(self.actions(), ctx, _recurse=_recurse)
+
+
+def _rebuild(
+    menu: QMenu | QToolBar,
+    app: Application,
+    menu_id: str,
+    include_submenus: bool = True,
+    exclude: Optional[Collection[str]] = None,
+) -> None:
+    """Rebuild menu by looking up `menu` in `Application`'s menu_registry."""
+    menu.clear()
+    _exclude = exclude or set()
+
+    groups = list(app.menus.iter_menu_groups(menu_id))
+    n_groups = len(groups)
+    for n, group in enumerate(groups):
+        for item in group:
+            if isinstance(item, SubmenuItem):
+                if include_submenus:
+                    submenu = QModelSubmenu(item, app, parent=menu)
+                    cast("QMenu", menu).addMenu(submenu)
+            elif item.command.id not in _exclude:
+                action = QMenuItemAction(item, app=app, parent=menu)
+                menu.addAction(action)
+        if n < n_groups - 1:
+            menu.addSeparator()
+
+
+def _update_from_context(
+    actions: Iterable[QAction], ctx: Mapping[str, object], _recurse: bool = True
+) -> None:
+    """Update the enabled/visible state of each menu item with `ctx`.
+
+    See `app_model.expressions` for details on expressions.
+
+    Parameters
+    ----------
+    actions : Iterable[QAction]
+        Actions to update.
+    ctx : Mapping
+        A namespace that will be used to `eval()` the `'enablement'` and
+        `'when'` expressions provided for each action in the menu.
+        *ALL variables used in these expressions must either be present in
+        the `ctx` dict, or be builtins*.
+    _recurse : bool
+        recursion check, internal use only
+    """
+    for action in actions:
+        if isinstance(action, QMenuItemAction):
+            action.update_from_context(ctx)
+        elif not QT6 and isinstance(menu := action.menu(), QModelMenu):
+            menu.update_from_context(ctx)
+        elif isinstance(parent := action.parent(), QModelMenu):
+            # FIXME: this is a hack for Qt6 that I don't entirely understand.
+            # QAction has lost the `.menu()` method, and it's a bit hard to find
+            # how to get to the parent menu now. Checking parent() seems to work,
+            # but I'm not sure if it's the right thing to do, and it leads to a
+            # recursion error.  I stop it with the _recurse flag here, but I wonder
+            # whether that will cause other problems.
+            if _recurse:
+                parent.update_from_context(ctx, _recurse=False)
+
+
+def _find_action(actions: Iterable[QAction], object_name: str) -> Union[QAction, None]:
+    return next((a for a in actions if a.objectName() == object_name), None)
```

### Comparing `app_model-0.1.2/src/app_model/expressions/__init__.py` & `app_model-0.1.3/src/app_model/expressions/__init__.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/expressions/_context.py` & `app_model-0.1.3/src/app_model/expressions/_context.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/expressions/_context_keys.py` & `app_model-0.1.3/src/app_model/expressions/_context_keys.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/expressions/_expressions.py` & `app_model-0.1.3/src/app_model/expressions/_expressions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/registries/_commands_reg.py` & `app_model-0.1.3/src/app_model/registries/_commands_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/registries/_keybindings_reg.py` & `app_model-0.1.3/src/app_model/registries/_keybindings_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/registries/_menus_reg.py` & `app_model-0.1.3/src/app_model/registries/_menus_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/registries/_register.py` & `app_model-0.1.3/src/app_model/registries/_register.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/__init__.py` & `app_model-0.1.3/src/app_model/types/__init__.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_action.py` & `app_model-0.1.3/src/app_model/types/_action.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_command_rule.py` & `app_model-0.1.3/src/app_model/types/_command_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_constants.py` & `app_model-0.1.3/src/app_model/types/_constants.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_icon.py` & `app_model-0.1.3/src/app_model/types/_icon.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_keybinding_rule.py` & `app_model-0.1.3/src/app_model/types/_keybinding_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_menu_rule.py` & `app_model-0.1.3/src/app_model/types/_menu_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_utils.py` & `app_model-0.1.3/src/app_model/types/_utils.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_keys/_key_codes.py` & `app_model-0.1.3/src/app_model/types/_keys/_key_codes.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_keys/_keybindings.py` & `app_model-0.1.3/src/app_model/types/_keys/_keybindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/src/app_model/types/_keys/_standard_bindings.py` & `app_model-0.1.3/src/app_model/types/_keys/_standard_bindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/conftest.py` & `app_model-0.1.3/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_actions.py` & `app_model-0.1.3/tests/test_actions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_app.py` & `app_model-0.1.3/tests/test_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_command_registry.py` & `app_model-0.1.3/tests/test_command_registry.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_key_codes.py` & `app_model-0.1.3/tests/test_key_codes.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_keybindings.py` & `app_model-0.1.3/tests/test_keybindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_registries.py` & `app_model-0.1.3/tests/test_registries.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_types.py` & `app_model-0.1.3/tests/test_types.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_context/test_context.py` & `app_model-0.1.3/tests/test_context/test_context.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_context/test_context_keys.py` & `app_model-0.1.3/tests/test_context/test_context_keys.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_context/test_expressions.py` & `app_model-0.1.3/tests/test_context/test_expressions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_qt/test_qactions.py` & `app_model-0.1.3/tests/test_qt/test_qactions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_qt/test_qkeymap.py` & `app_model-0.1.3/tests/test_qt/test_qkeymap.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/tests/test_qt/test_qmenu.py` & `app_model-0.1.3/tests/test_qt/test_qmenu.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,43 +1,48 @@
+from __future__ import annotations
+
 import sys
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, cast
 
 import pytest
 from qtpy.QtCore import Qt
 from qtpy.QtWidgets import QAction, QMainWindow
 
-from app_model.backends.qt import QModelMenu
+from app_model.backends.qt import QModelMenu, QModelToolBar
 
 if TYPE_CHECKING:
     from pytestqt.plugin import QtBot
 
     from conftest import FullApp
 
 SEP = ""
 LINUX = sys.platform.startswith("linux")
 
 
-def test_menu(qtbot: "QtBot", full_app: "FullApp") -> None:
+@pytest.mark.parametrize("MenuCls", [QModelMenu, QModelToolBar])
+def test_menu(
+    MenuCls: type[QModelMenu] | type[QModelToolBar], qtbot: QtBot, full_app: FullApp
+) -> None:
     app = full_app
 
-    menu = QModelMenu(app.Menus.EDIT, app)
+    menu = MenuCls(app.Menus.EDIT, app)
     qtbot.addWidget(menu)
 
     # The "" are separators, according to our group settings in full_app
     menu_texts = [a.text() for a in menu.actions()]
     assert menu_texts == ["AtTop", SEP, "Undo", "Redo", SEP, "Copy", "Paste"]
 
     # check that triggering the actions calls the associated commands
     for cmd in (app.Commands.UNDO, app.Commands.REDO):
-        action: QAction = menu.findAction(cmd)
+        action = cast(QAction, menu.findAction(cmd))
         with qtbot.waitSignal(action.triggered):
             action.trigger()
             getattr(app.mocks, cmd).assert_called_once()
 
-    redo_action: QAction = menu.findAction(app.Commands.REDO)
+    redo_action = cast(QAction, menu.findAction(app.Commands.REDO))
 
     assert redo_action.isVisible()
     assert redo_action.isEnabled()
 
     # change that visibility and enablement follows the context
     menu.update_from_context({"allow_undo_redo": True, "something_to_undo": False})
     assert redo_action.isVisible()
@@ -55,16 +60,18 @@
     assert redo_action.isVisible()
     assert redo_action.isEnabled()
 
     # useful error when we forget a required name
     with pytest.raises(NameError, match="Names required to eval this expression"):
         menu.update_from_context({})
 
+    menu._disconnect()
+
 
-def test_submenu(qtbot: "QtBot", full_app: "FullApp") -> None:
+def test_submenu(qtbot: QtBot, full_app: FullApp) -> None:
     app = full_app
 
     menu = QModelMenu(app.Menus.FILE, app)
     qtbot.addWidget(menu)
 
     menu_texts = [a.text() for a in menu.actions()]
     assert menu_texts == ["Open From...", "Open..."]
@@ -93,40 +100,66 @@
     menu.update_from_context({"something_open": True, "friday": True})
     # assert not submenu.isVisible()
     assert submenu.isEnabled()
 
 
 @pytest.mark.filterwarnings("ignore:QPixmapCache.find:")
 @pytest.mark.skipif(LINUX, reason="Linux keytest not working")
-def test_shortcuts(qtbot: "QtBot", full_app: "FullApp") -> None:
+def test_shortcuts(qtbot: QtBot, full_app: FullApp) -> None:
     app = full_app
 
     win = QMainWindow()
     menu = QModelMenu(app.Menus.EDIT, app=app, title="Edit", parent=win)
     win.menuBar().addMenu(menu)
     qtbot.addWidget(win)
     qtbot.addWidget(menu)
 
     with qtbot.waitExposed(win):
         win.show()
 
     copy_action = menu.findAction(app.Commands.COPY)
 
-    with qtbot.waitSignal(copy_action.triggered, timeout=1000):
+    with qtbot.waitSignal(copy_action.triggered, timeout=2000):
         qtbot.keyClicks(win, "C", Qt.KeyboardModifier.ControlModifier)
 
     paste_action = menu.findAction(app.Commands.PASTE)
     with qtbot.waitSignal(paste_action.triggered, timeout=1000):
         qtbot.keyClicks(win, "V", Qt.KeyboardModifier.ControlModifier)
 
 
-def test_toggled_menu_item(qtbot: "QtBot", full_app: "FullApp") -> None:
+def test_toggled_menu_item(qtbot: QtBot, full_app: FullApp) -> None:
     app = full_app
     menu = QModelMenu(app.Menus.HELP, app)
     qtbot.addWidget(menu)
 
     menu.update_from_context({"thing_toggled": True})
     action = menu.findAction(app.Commands.TOGGLE_THING)
     assert action.isChecked()
 
     menu.update_from_context({"thing_toggled": False})
     assert not action.isChecked()
+
+
+@pytest.mark.parametrize("MenuCls", [QModelMenu, QModelToolBar])
+def test_menu_events(
+    MenuCls: type[QModelMenu] | type[QModelToolBar], qtbot: QtBot, full_app: FullApp
+) -> None:
+    app = full_app
+    menu = MenuCls(app.Menus.EDIT, app)
+
+    qtbot.addWidget(menu)
+
+    # The "" are separators, according to our group settings in full_app
+    menu_texts = [a.text() for a in menu.actions()]
+    assert menu_texts == ["AtTop", SEP, "Undo", "Redo", SEP, "Copy", "Paste"]
+
+    # simulate something changing the edit menu... normally this would be
+    # triggered by a dispose() call, but that's a bit hard to do currently with the
+    # test app fixture.
+    copy_item = next(
+        x for x in full_app.menus._menu_items["edit"] if x.command.title == "Copy"
+    )
+    full_app.menus._menu_items["edit"].pop(copy_item)
+    full_app.menus.menus_changed.emit(app.Menus.EDIT)
+
+    menu_texts = [a.text() for a in menu.actions()]
+    assert menu_texts == ["AtTop", SEP, "Undo", "Redo", SEP, "Paste"]
```

### Comparing `app_model-0.1.2/.gitignore` & `app_model-0.1.3/.gitignore`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/LICENSE` & `app_model-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/README.md` & `app_model-0.1.3/README.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.2/pyproject.toml` & `app_model-0.1.3/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -80,28 +80,27 @@
 src_paths = ["src/app_model", "tests"]
 
 # https://github.com/charliermarsh/ruff
 [tool.ruff]
 line-length = 88
 src = ["src", "tests"]
 target-version = "py38"
-extend-select = [
+select = [
     "E",    # style errors
+    "W",    # style warnings
     "F",    # flakes
     "D",    # pydocstyle
-    "I", # isort
-    "U",    # pyupgrade
-    # "N",  # pep8-naming
-    # "S",  # bandit
-    "C",    # flake8-comprehensions
+    "I",    # isort
+    "UP",   # pyupgrade
+    "C4",   # flake8-comprehensions
     "B",    # flake8-bugbear
     "A001", # flake8-builtins
     "RUF",  # ruff-specific rules
 ]
-extend-ignore = [
+ignore = [
     "D100", # Missing docstring in public module
     "D107", # Missing docstring in __init__
     "D203", # 1 blank line required before class docstring
     "D212", # Multi-line docstring summary should start at the first line
     "D213", # Multi-line docstring summary should start at the second line
     "D413", # Missing blank line after last section
     "D416", # Section name should end with a colon
@@ -119,24 +118,28 @@
 "src/app_model/context/_expressions.py" = ["D10"]
 "src/app_model/types/_keys/*" = ["E501"]
 "setup.py" = ["F821"]
 
 # https://docs.pytest.org/en/6.2.x/customize.html
 [tool.pytest.ini_options]
 minversion = "6.0"
-filterwarnings = ["error", "ignore:QPixmapCache.find:DeprecationWarning:"]
+filterwarnings = [
+    "error",
+    "ignore:Enum value:DeprecationWarning:superqt",
+]
 
 # https://mypy.readthedocs.io/en/stable/config_file.html
 [tool.mypy]
 files = "src/**/*.py"
 strict = true
 disallow_any_generics = false
 disallow_subclassing_any = false
 show_error_codes = true
 pretty = true
+plugins = ["pydantic.mypy"]
 
 [[tool.mypy.overrides]]
 module = ["tests.*"]
 disallow_untyped_defs = false
 
 [[tool.mypy.overrides]]
 module = ["qtpy.*"]
```

### Comparing `app_model-0.1.2/PKG-INFO` & `app_model-0.1.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: app-model
-Version: 0.1.2
+Version: 0.1.3
 Summary: Generic application schema implemented in python
 Project-URL: homepage, https://github.com/pyapp-kit/app-model
 Project-URL: repository, https://github.com/pyapp-kit/app-model
 Author: Talley Lambert
 Author-email: talley.lambert@gmail.com
 License: BSD 3-Clause License
 License-File: LICENSE
```

