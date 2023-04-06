# Comparing `tmp/app_model-0.1.3.tar.gz` & `tmp/app_model-0.1.4.tar.gz`

## Comparing `app_model-0.1.3.tar` & `app_model-0.1.4.tar`

### file list

```diff
@@ -1,85 +1,85 @@
--rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 app_model-0.1.3/.github_changelog_generator
--rw-r--r--   0        0        0     1279 2020-02-02 00:00:00.000000 app_model-0.1.3/.pre-commit-config.yaml
--rw-r--r--   0        0        0      296 2020-02-02 00:00:00.000000 app_model-0.1.3/.readthedocs.yaml
--rw-r--r--   0        0        0    10845 2020-02-02 00:00:00.000000 app_model-0.1.3/CHANGELOG.md
--rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 app_model-0.1.3/codecov.yml
--rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 app_model-0.1.3/mkdocs.yml
--rw-r--r--   0        0        0      666 2020-02-02 00:00:00.000000 app_model-0.1.3/setup.py
--rw-r--r--   0        0        0      320 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/ISSUE_TEMPLATE.md
--rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/TEST_FAIL_TEMPLATE.md
--rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/dependabot.yml
--rw-r--r--   0        0        0     4196 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/workflows/ci.yml
--rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 app_model-0.1.3/.github/workflows/cron.yml
--rw-r--r--   0        0        0      253 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/keybinding_helper.py
--rw-r--r--   0        0        0     8203 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/model_app.py
--rw-r--r--   0        0        0     8316 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/qapplication.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/__init__.py
--rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/__main__.py
--rw-r--r--   0        0        0     2110 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/actions.py
--rw-r--r--   0        0        0      641 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/app.py
--rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/constants.py
--rw-r--r--   0        0        0      380 2020-02-02 00:00:00.000000 app_model-0.1.3/demo/multi_file/functions.py
--rw-r--r--   0        0        0     1589 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/_macros.py
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/application.md
--rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/expressions.md
--rw-r--r--   0        0        0     4479 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/index.md
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/keybindings.md
--rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/registries.md
--rw-r--r--   0        0        0      576 2020-02-02 00:00:00.000000 app_model-0.1.3/docs/types.md
--rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/__init__.py
--rw-r--r--   0        0        0     6589 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/_app.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/py.typed
--rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/__init__.py
--rw-r--r--   0        0        0      821 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/__init__.py
--rw-r--r--   0        0        0     6171 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qaction.py
--rw-r--r--   0        0        0      686 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qkeybindingedit.py
--rw-r--r--   0        0        0    16388 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qkeymap.py
--rw-r--r--   0        0        0     1212 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qmainwindow.py
--rw-r--r--   0        0        0    12288 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_qmenu.py
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/backends/qt/_util.py
--rw-r--r--   0        0        0      652 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/__init__.py
--rw-r--r--   0        0        0     4839 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_context.py
--rw-r--r--   0        0        0     7164 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_context_keys.py
--rw-r--r--   0        0        0    19026 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/expressions/_expressions.py
--rw-r--r--   0        0        0      347 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/__init__.py
--rw-r--r--   0        0        0     6697 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_commands_reg.py
--rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_keybindings_reg.py
--rw-r--r--   0        0        0     4831 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_menus_reg.py
--rw-r--r--   0        0        0     8730 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/registries/_register.py
--rw-r--r--   0        0        0      924 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/__init__.py
--rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_action.py
--rw-r--r--   0        0        0      309 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_base.py
--rw-r--r--   0        0        0     3027 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_command_rule.py
--rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_constants.py
--rw-r--r--   0        0        0     1277 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_icon.py
--rw-r--r--   0        0        0     2391 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keybinding_rule.py
--rw-r--r--   0        0        0     4000 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_menu_rule.py
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_utils.py
--rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/__init__.py
--rw-r--r--   0        0        0    33529 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_key_codes.py
--rw-r--r--   0        0        0     8891 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_keybindings.py
--rw-r--r--   0        0        0     7804 2020-02-02 00:00:00.000000 app_model-0.1.3/src/app_model/types/_keys/_standard_bindings.py
--rw-r--r--   0        0        0     7135 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/conftest.py
--rw-r--r--   0        0        0     3736 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_actions.py
--rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_app.py
--rw-r--r--   0        0        0     1262 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_command_registry.py
--rw-r--r--   0        0        0     1264 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_key_codes.py
--rw-r--r--   0        0        0     3323 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_keybindings.py
--rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_registries.py
--rw-r--r--   0        0        0      664 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_types.py
--rw-r--r--   0        0        0      149 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/fixtures/fake_module.py
--rw-r--r--   0        0        0     2387 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_context.py
--rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_context_keys.py
--rw-r--r--   0        0        0     6992 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_context/test_expressions.py
--rw-r--r--   0        0        0      122 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/__init__.py
--rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_demos.py
--rw-r--r--   0        0        0     1409 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qactions.py
--rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qkeybindingedit.py
--rw-r--r--   0        0        0     7005 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qkeymap.py
--rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qmainwindow.py
--rw-r--r--   0        0        0     5506 2020-02-02 00:00:00.000000 app_model-0.1.3/tests/test_qt/test_qmenu.py
--rw-r--r--   0        0        0     1246 2020-02-02 00:00:00.000000 app_model-0.1.3/.gitignore
--rw-r--r--   0        0        0     1513 2020-02-02 00:00:00.000000 app_model-0.1.3/LICENSE
--rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 app_model-0.1.3/README.md
--rw-r--r--   0        0        0     4534 2020-02-02 00:00:00.000000 app_model-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     3299 2020-02-02 00:00:00.000000 app_model-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 app_model-0.1.4/.github_changelog_generator
+-rw-r--r--   0        0        0     1279 2020-02-02 00:00:00.000000 app_model-0.1.4/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      296 2020-02-02 00:00:00.000000 app_model-0.1.4/.readthedocs.yaml
+-rw-r--r--   0        0        0    10999 2020-02-02 00:00:00.000000 app_model-0.1.4/CHANGELOG.md
+-rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 app_model-0.1.4/codecov.yml
+-rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 app_model-0.1.4/mkdocs.yml
+-rw-r--r--   0        0        0      666 2020-02-02 00:00:00.000000 app_model-0.1.4/setup.py
+-rw-r--r--   0        0        0      320 2020-02-02 00:00:00.000000 app_model-0.1.4/.github/ISSUE_TEMPLATE.md
+-rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 app_model-0.1.4/.github/TEST_FAIL_TEMPLATE.md
+-rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 app_model-0.1.4/.github/dependabot.yml
+-rw-r--r--   0        0        0     4196 2020-02-02 00:00:00.000000 app_model-0.1.4/.github/workflows/ci.yml
+-rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 app_model-0.1.4/.github/workflows/cron.yml
+-rw-r--r--   0        0        0      253 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/keybinding_helper.py
+-rw-r--r--   0        0        0     8203 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/model_app.py
+-rw-r--r--   0        0        0     8316 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/qapplication.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/__init__.py
+-rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/__main__.py
+-rw-r--r--   0        0        0     2110 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/actions.py
+-rw-r--r--   0        0        0      641 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/app.py
+-rw-r--r--   0        0        0      460 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/constants.py
+-rw-r--r--   0        0        0      380 2020-02-02 00:00:00.000000 app_model-0.1.4/demo/multi_file/functions.py
+-rw-r--r--   0        0        0     1589 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/_macros.py
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/application.md
+-rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/expressions.md
+-rw-r--r--   0        0        0     4479 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/index.md
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/keybindings.md
+-rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/registries.md
+-rw-r--r--   0        0        0      576 2020-02-02 00:00:00.000000 app_model-0.1.4/docs/types.md
+-rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/__init__.py
+-rw-r--r--   0        0        0     6589 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/_app.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/py.typed
+-rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/__init__.py
+-rw-r--r--   0        0        0      821 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/__init__.py
+-rw-r--r--   0        0        0     6171 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_qaction.py
+-rw-r--r--   0        0        0      686 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_qkeybindingedit.py
+-rw-r--r--   0        0        0    16388 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_qkeymap.py
+-rw-r--r--   0        0        0     1212 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_qmainwindow.py
+-rw-r--r--   0        0        0    12288 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_qmenu.py
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/backends/qt/_util.py
+-rw-r--r--   0        0        0      652 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/expressions/__init__.py
+-rw-r--r--   0        0        0     4839 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/expressions/_context.py
+-rw-r--r--   0        0        0     7164 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/expressions/_context_keys.py
+-rw-r--r--   0        0        0    19026 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/expressions/_expressions.py
+-rw-r--r--   0        0        0      347 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/registries/__init__.py
+-rw-r--r--   0        0        0     6697 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/registries/_commands_reg.py
+-rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/registries/_keybindings_reg.py
+-rw-r--r--   0        0        0     4831 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/registries/_menus_reg.py
+-rw-r--r--   0        0        0     8730 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/registries/_register.py
+-rw-r--r--   0        0        0      924 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/__init__.py
+-rw-r--r--   0        0        0     2319 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_action.py
+-rw-r--r--   0        0        0      309 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_base.py
+-rw-r--r--   0        0        0     3027 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_command_rule.py
+-rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_constants.py
+-rw-r--r--   0        0        0     1277 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_icon.py
+-rw-r--r--   0        0        0     2391 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_keybinding_rule.py
+-rw-r--r--   0        0        0     4000 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_menu_rule.py
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_utils.py
+-rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_keys/__init__.py
+-rw-r--r--   0        0        0    33529 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_keys/_key_codes.py
+-rw-r--r--   0        0        0     8891 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_keys/_keybindings.py
+-rw-r--r--   0        0        0     7804 2020-02-02 00:00:00.000000 app_model-0.1.4/src/app_model/types/_keys/_standard_bindings.py
+-rw-r--r--   0        0        0     7135 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/conftest.py
+-rw-r--r--   0        0        0     3736 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_actions.py
+-rw-r--r--   0        0        0     3247 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_app.py
+-rw-r--r--   0        0        0     1262 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_command_registry.py
+-rw-r--r--   0        0        0     1264 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_key_codes.py
+-rw-r--r--   0        0        0     3323 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_keybindings.py
+-rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_registries.py
+-rw-r--r--   0        0        0      664 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_types.py
+-rw-r--r--   0        0        0      149 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/fixtures/fake_module.py
+-rw-r--r--   0        0        0     2387 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_context/test_context.py
+-rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_context/test_context_keys.py
+-rw-r--r--   0        0        0     6992 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_context/test_expressions.py
+-rw-r--r--   0        0        0      122 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/__init__.py
+-rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_demos.py
+-rw-r--r--   0        0        0     1409 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_qactions.py
+-rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_qkeybindingedit.py
+-rw-r--r--   0        0        0     7005 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_qkeymap.py
+-rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_qmainwindow.py
+-rw-r--r--   0        0        0     5506 2020-02-02 00:00:00.000000 app_model-0.1.4/tests/test_qt/test_qmenu.py
+-rw-r--r--   0        0        0     1246 2020-02-02 00:00:00.000000 app_model-0.1.4/.gitignore
+-rw-r--r--   0        0        0     1513 2020-02-02 00:00:00.000000 app_model-0.1.4/LICENSE
+-rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 app_model-0.1.4/README.md
+-rw-r--r--   0        0        0     4537 2020-02-02 00:00:00.000000 app_model-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     3302 2020-02-02 00:00:00.000000 app_model-0.1.4/PKG-INFO
```

### Comparing `app_model-0.1.3/.pre-commit-config.yaml` & `app_model-0.1.4/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/CHANGELOG.md` & `app_model-0.1.4/CHANGELOG.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,24 @@
 # Changelog
 
-## [0.1.3](https://github.com/pyapp-kit/app-model/tree/0.1.3) (2023-04-06)
+## [0.1.4](https://github.com/pyapp-kit/app-model/tree/0.1.4) (2023-04-06)
 
-[Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.2...0.1.3)
+[Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.3...0.1.4)
 
 **Merged pull requests:**
 
+- build: pin pydantic \< 2 [\#96](https://github.com/pyapp-kit/app-model/pull/96) ([tlambert03](https://github.com/tlambert03))
+
+## [v0.1.3](https://github.com/pyapp-kit/app-model/tree/v0.1.3) (2023-04-06)
+
+[Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.2...v0.1.3)
+
+**Fixed bugs:**
+
 - fix: don't use mixin for menus [\#95](https://github.com/pyapp-kit/app-model/pull/95) ([tlambert03](https://github.com/tlambert03))
-- ci: \[pre-commit.ci\] autoupdate [\#92](https://github.com/pyapp-kit/app-model/pull/92) ([pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci))
 
 ## [v0.1.2](https://github.com/pyapp-kit/app-model/tree/v0.1.2) (2023-03-07)
 
 [Full Changelog](https://github.com/pyapp-kit/app-model/compare/v0.1.1...v0.1.2)
 
 **Fixed bugs:**
```

### Comparing `app_model-0.1.3/mkdocs.yml` & `app_model-0.1.4/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/setup.py` & `app_model-0.1.4/setup.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/.github/workflows/ci.yml` & `app_model-0.1.4/.github/workflows/ci.yml`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/.github/workflows/cron.yml` & `app_model-0.1.4/.github/workflows/cron.yml`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/demo/model_app.py` & `app_model-0.1.4/demo/model_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/demo/qapplication.py` & `app_model-0.1.4/demo/qapplication.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/demo/multi_file/actions.py` & `app_model-0.1.4/demo/multi_file/actions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/demo/multi_file/app.py` & `app_model-0.1.4/demo/multi_file/app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/docs/_macros.py` & `app_model-0.1.4/docs/_macros.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/docs/index.md` & `app_model-0.1.4/docs/index.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/docs/types.md` & `app_model-0.1.4/docs/types.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/_app.py` & `app_model-0.1.4/src/app_model/_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/__init__.py` & `app_model-0.1.4/src/app_model/backends/qt/__init__.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/_qaction.py` & `app_model-0.1.4/src/app_model/backends/qt/_qaction.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/_qkeybindingedit.py` & `app_model-0.1.4/src/app_model/backends/qt/_qkeybindingedit.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/_qkeymap.py` & `app_model-0.1.4/src/app_model/backends/qt/_qkeymap.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/_qmainwindow.py` & `app_model-0.1.4/src/app_model/backends/qt/_qmainwindow.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/backends/qt/_qmenu.py` & `app_model-0.1.4/src/app_model/backends/qt/_qmenu.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/expressions/__init__.py` & `app_model-0.1.4/src/app_model/expressions/__init__.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/expressions/_context.py` & `app_model-0.1.4/src/app_model/expressions/_context.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/expressions/_context_keys.py` & `app_model-0.1.4/src/app_model/expressions/_context_keys.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/expressions/_expressions.py` & `app_model-0.1.4/src/app_model/expressions/_expressions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/registries/_commands_reg.py` & `app_model-0.1.4/src/app_model/registries/_commands_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/registries/_keybindings_reg.py` & `app_model-0.1.4/src/app_model/registries/_keybindings_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/registries/_menus_reg.py` & `app_model-0.1.4/src/app_model/registries/_menus_reg.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/registries/_register.py` & `app_model-0.1.4/src/app_model/registries/_register.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/__init__.py` & `app_model-0.1.4/src/app_model/types/__init__.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_action.py` & `app_model-0.1.4/src/app_model/types/_action.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_command_rule.py` & `app_model-0.1.4/src/app_model/types/_command_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_constants.py` & `app_model-0.1.4/src/app_model/types/_constants.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_icon.py` & `app_model-0.1.4/src/app_model/types/_icon.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_keybinding_rule.py` & `app_model-0.1.4/src/app_model/types/_keybinding_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_menu_rule.py` & `app_model-0.1.4/src/app_model/types/_menu_rule.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_utils.py` & `app_model-0.1.4/src/app_model/types/_utils.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_keys/_key_codes.py` & `app_model-0.1.4/src/app_model/types/_keys/_key_codes.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_keys/_keybindings.py` & `app_model-0.1.4/src/app_model/types/_keys/_keybindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/src/app_model/types/_keys/_standard_bindings.py` & `app_model-0.1.4/src/app_model/types/_keys/_standard_bindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/conftest.py` & `app_model-0.1.4/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_actions.py` & `app_model-0.1.4/tests/test_actions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_app.py` & `app_model-0.1.4/tests/test_app.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_command_registry.py` & `app_model-0.1.4/tests/test_command_registry.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_key_codes.py` & `app_model-0.1.4/tests/test_key_codes.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_keybindings.py` & `app_model-0.1.4/tests/test_keybindings.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_registries.py` & `app_model-0.1.4/tests/test_registries.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_types.py` & `app_model-0.1.4/tests/test_types.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_context/test_context.py` & `app_model-0.1.4/tests/test_context/test_context.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_context/test_context_keys.py` & `app_model-0.1.4/tests/test_context/test_context_keys.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_context/test_expressions.py` & `app_model-0.1.4/tests/test_context/test_expressions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_qt/test_qactions.py` & `app_model-0.1.4/tests/test_qt/test_qactions.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_qt/test_qkeymap.py` & `app_model-0.1.4/tests/test_qt/test_qkeymap.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/tests/test_qt/test_qmenu.py` & `app_model-0.1.4/tests/test_qt/test_qmenu.py`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/.gitignore` & `app_model-0.1.4/.gitignore`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/LICENSE` & `app_model-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/README.md` & `app_model-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `app_model-0.1.3/pyproject.toml` & `app_model-0.1.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -23,15 +23,15 @@
     "Topic :: Desktop Environment",
     "Topic :: Software Development",
     "Topic :: Software Development :: User Interfaces",
 ]
 dynamic = ["version"]
 dependencies = [
     "psygnal>=0.3.4",
-    "pydantic>=1.8",
+    "pydantic>=1.8,<2",
     "in-n-out>=0.1.5",
     "typing_extensions",
 ]
 
 # extras
 # https://peps.python.org/pep-0621/#dependencies-optional-dependencies
 [project.optional-dependencies]
```

### Comparing `app_model-0.1.3/PKG-INFO` & `app_model-0.1.4/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: app-model
-Version: 0.1.3
+Version: 0.1.4
 Summary: Generic application schema implemented in python
 Project-URL: homepage, https://github.com/pyapp-kit/app-model
 Project-URL: repository, https://github.com/pyapp-kit/app-model
 Author: Talley Lambert
 Author-email: talley.lambert@gmail.com
 License: BSD 3-Clause License
 License-File: LICENSE
@@ -18,15 +18,15 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Desktop Environment
 Classifier: Topic :: Software Development
 Classifier: Topic :: Software Development :: User Interfaces
 Requires-Python: >=3.8
 Requires-Dist: in-n-out>=0.1.5
 Requires-Dist: psygnal>=0.3.4
-Requires-Dist: pydantic>=1.8
+Requires-Dist: pydantic<2,>=1.8
 Requires-Dist: typing-extensions
 Provides-Extra: dev
 Requires-Dist: black; extra == 'dev'
 Requires-Dist: ipython; extra == 'dev'
 Requires-Dist: isort; extra == 'dev'
 Requires-Dist: mypy; extra == 'dev'
 Requires-Dist: pdbpp; extra == 'dev'
```

