# Comparing `tmp/tmuxp-1.9.3.tar.gz` & `tmp/tmuxp-1.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tmuxp-1.9.3.tar", last modified: Sat Oct 30 19:15:51 2021, max compression
+gzip compressed data, was "tmuxp-1.9.4.tar", max compression
```

## Comparing `tmuxp-1.9.3.tar` & `tmuxp-1.9.4.tar`

### file list

```diff
@@ -1,200 +1,188 @@
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/
--rw-r--r--   0 t         (1000) t         (1000)      600 2021-10-17 14:15:51.000000 tmuxp-1.9.3/.tmuxp.yaml
--rw-r--r--   0 t         (1000) t         (1000)    38777 2021-10-30 19:14:16.000000 tmuxp-1.9.3/CHANGES
--rw-r--r--   0 t         (1000) t         (1000)     1076 2021-10-17 14:15:51.000000 tmuxp-1.9.3/LICENSE
--rw-r--r--   0 t         (1000) t         (1000)      206 2021-10-17 14:15:51.000000 tmuxp-1.9.3/MANIFEST.in
--rw-r--r--   0 t         (1000) t         (1000)     7936 2021-10-30 19:15:51.000000 tmuxp-1.9.3/PKG-INFO
--rw-r--r--   0 t         (1000) t         (1000)     6753 2021-10-30 11:54:32.000000 tmuxp-1.9.3/README.md
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/docs/
--rw-r--r--   0 t         (1000) t         (1000)     3727 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/about.md
--rw-r--r--   0 t         (1000) t         (1000)    21424 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/about_tmux.md
--rw-r--r--   0 t         (1000) t         (1000)     2135 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/api.md
--rw-r--r--   0 t         (1000) t         (1000)     5739 2021-10-30 11:54:32.000000 tmuxp-1.9.3/docs/cli.md
--rw-r--r--   0 t         (1000) t         (1000)     5843 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/developing.md
--rw-r--r--   0 t         (1000) t         (1000)    10345 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/examples.md
--rw-r--r--   0 t         (1000) t         (1000)     1676 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/glossary.md
--rw-r--r--   0 t         (1000) t         (1000)       65 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/history.md
--rw-r--r--   0 t         (1000) t         (1000)      384 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/index.md
--rw-r--r--   0 t         (1000) t         (1000)     3521 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/plugin_system.md
--rw-r--r--   0 t         (1000) t         (1000)     2888 2021-10-17 14:15:51.000000 tmuxp-1.9.3/docs/quickstart.md
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/examples/
--rw-r--r--   0 t         (1000) t         (1000)      260 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/2-pane-synchronized.json
--rw-r--r--   0 t         (1000) t         (1000)      177 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/2-pane-synchronized.yaml
--rw-r--r--   0 t         (1000) t         (1000)      181 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/2-pane-vertical.json
--rw-r--r--   0 t         (1000) t         (1000)      120 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/2-pane-vertical.yaml
--rw-r--r--   0 t         (1000) t         (1000)      386 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/3-pane.json
--rw-r--r--   0 t         (1000) t         (1000)      233 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/3-pane.yaml
--rw-r--r--   0 t         (1000) t         (1000)      406 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/4-pane.json
--rw-r--r--   0 t         (1000) t         (1000)      247 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/4-pane.yaml
--rw-r--r--   0 t         (1000) t         (1000)      823 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/blank-panes.json
--rw-r--r--   0 t         (1000) t         (1000)      640 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/blank-panes.yaml
--rw-r--r--   0 t         (1000) t         (1000)      659 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/env-variables.json
--rw-r--r--   0 t         (1000) t         (1000)      398 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/env-variables.yaml
--rw-r--r--   0 t         (1000) t         (1000)      814 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/focus-window-and-panes.json
--rw-r--r--   0 t         (1000) t         (1000)      479 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/focus-window-and-panes.yaml
--rw-r--r--   0 t         (1000) t         (1000)      548 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/main-pane-height.json
--rw-r--r--   0 t         (1000) t         (1000)      288 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/main-pane-height.yaml
--rw-r--r--   0 t         (1000) t         (1000)      686 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/options.json
--rw-r--r--   0 t         (1000) t         (1000)      411 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/options.yaml
--rw-r--r--   0 t         (1000) t         (1000)      442 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/plugin-system.json
--rw-r--r--   0 t         (1000) t         (1000)      285 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/plugin-system.yaml
--rw-r--r--   0 t         (1000) t         (1000)      337 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/session-environment.json
--rw-r--r--   0 t         (1000) t         (1000)      250 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/session-environment.yaml
--rw-r--r--   0 t         (1000) t         (1000)      363 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/shorthands.json
--rw-r--r--   0 t         (1000) t         (1000)      218 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/shorthands.yaml
--rw-r--r--   0 t         (1000) t         (1000)     1738 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/start-directory.json
--rw-r--r--   0 t         (1000) t         (1000)     1201 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/start-directory.yaml
--rw-r--r--   0 t         (1000) t         (1000)      872 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/suppress-history.json
--rw-r--r--   0 t         (1000) t         (1000)      612 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/suppress-history.yaml
--rw-r--r--   0 t         (1000) t         (1000)      444 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/window-index.json
--rw-r--r--   0 t         (1000) t         (1000)      305 2021-10-17 14:15:51.000000 tmuxp-1.9.3/examples/window-index.yaml
--rw-r--r--   0 t         (1000) t         (1000)     2030 2021-10-30 19:15:14.000000 tmuxp-1.9.3/pyproject.toml
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/requirements/
--rw-r--r--   0 t         (1000) t         (1000)       67 2021-10-30 19:13:47.000000 tmuxp-1.9.3/requirements/base.txt
--rw-r--r--   0 t         (1000) t         (1000)       19 2021-10-17 14:15:51.000000 tmuxp-1.9.3/requirements/dev.txt
--rw-r--r--   0 t         (1000) t         (1000)      108 2021-10-17 14:15:51.000000 tmuxp-1.9.3/requirements/doc.txt
--rw-r--r--   0 t         (1000) t         (1000)       56 2021-10-17 14:15:51.000000 tmuxp-1.9.3/requirements/test.txt
--rw-r--r--   0 t         (1000) t         (1000)      697 2021-10-30 19:15:51.000000 tmuxp-1.9.3/setup.cfg
--rw-r--r--   0 t         (1000) t         (1000)     2017 2021-10-17 14:15:51.000000 tmuxp-1.9.3/setup.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/
--rw-r--r--   0 t         (1000) t         (1000)      264 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)     2757 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/conftest.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/
--rw-r--r--   0 t         (1000) t         (1000)       28 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      252 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/_util.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/
--rw-r--r--   0 t         (1000) t         (1000)      161 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)     2273 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/expand1.py
--rw-r--r--   0 t         (1000) t         (1000)      548 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/expand2-expanded.yaml
--rw-r--r--   0 t         (1000) t         (1000)      514 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/expand2-unexpanded.yaml
--rw-r--r--   0 t         (1000) t         (1000)      211 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/expand2.py
--rw-r--r--   0 t         (1000) t         (1000)      985 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/expand_blank.py
--rw-r--r--   0 t         (1000) t         (1000)      706 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/sampleconfig.py
--rw-r--r--   0 t         (1000) t         (1000)     4125 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/shell_command_before.py
--rw-r--r--   0 t         (1000) t         (1000)      372 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/shell_command_before_session-expected.yaml
--rw-r--r--   0 t         (1000) t         (1000)      174 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/shell_command_before_session.py
--rw-r--r--   0 t         (1000) t         (1000)      257 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/shell_command_before_session.yaml
--rw-r--r--   0 t         (1000) t         (1000)     1230 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config/trickle.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/
--rw-r--r--   0 t         (1000) t         (1000)       58 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)     5026 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/layouts.py
--rw-r--r--   0 t         (1000) t         (1000)     1848 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/layouts.yaml
--rw-r--r--   0 t         (1000) t         (1000)      745 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test1.py
--rw-r--r--   0 t         (1000) t         (1000)      166 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test1.yaml
--rw-r--r--   0 t         (1000) t         (1000)      777 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test2.py
--rw-r--r--   0 t         (1000) t         (1000)      158 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test2.yaml
--rw-r--r--   0 t         (1000) t         (1000)     1433 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test3.py
--rw-r--r--   0 t         (1000) t         (1000)      374 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test3.yaml
--rw-r--r--   0 t         (1000) t         (1000)      523 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test4.py
--rw-r--r--   0 t         (1000) t         (1000)       95 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_teamocil/test4.yaml
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/
--rw-r--r--   0 t         (1000) t         (1000)       42 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      609 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test1.py
--rw-r--r--   0 t         (1000) t         (1000)      153 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test1.yaml
--rw-r--r--   0 t         (1000) t         (1000)     2508 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test2.py
--rw-r--r--   0 t         (1000) t         (1000)      818 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test2.yaml
--rw-r--r--   0 t         (1000) t         (1000)     2654 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test3.py
--rw-r--r--   0 t         (1000) t         (1000)      971 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test3.yaml
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/__init__.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      746 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/all_pass.py
--rw-r--r--   0 t         (1000) t         (1000)      967 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/libtmux_version_fail.py
--rw-r--r--   0 t         (1000) t         (1000)      729 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/test_plugin_helpers.py
--rw-r--r--   0 t         (1000) t         (1000)      924 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/tmux_version_fail.py
--rw-r--r--   0 t         (1000) t         (1000)      945 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/tmuxp_version_fail.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      624 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/plugin.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/tmuxp_test_plugin_bs/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/tmuxp_test_plugin_bs/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      249 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/tmuxp_test_plugin_bs/plugin.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/tmuxp_test_plugin_bwb/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/tmuxp_test_plugin_bwb/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      271 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/tmuxp_test_plugin_bwb/plugin.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/tmuxp_test_plugin_fail/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/tmuxp_test_plugin_fail/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      273 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/tmuxp_test_plugin_fail/plugin.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      610 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/plugin.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/tmuxp_test_plugin_r/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/tmuxp_test_plugin_r/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      239 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/tmuxp_test_plugin_r/plugin.py
--rwxr-xr-x   0 t         (1000) t         (1000)       97 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/script_complete.sh
--rwxr-xr-x   0 t         (1000) t         (1000)      180 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/script_failed.sh
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/
--rw-r--r--   0 t         (1000) t         (1000)       87 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/config_script_completes.yaml
--rw-r--r--   0 t         (1000) t         (1000)       95 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/config_script_fails.yaml
--rw-r--r--   0 t         (1000) t         (1000)       89 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/config_script_not_exists.yaml
--rw-r--r--   0 t         (1000) t         (1000)      266 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/env_var_options.yaml
--rw-r--r--   0 t         (1000) t         (1000)      135 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/environment_vars.yaml
--rw-r--r--   0 t         (1000) t         (1000)      487 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/focus_and_pane.yaml
--rw-r--r--   0 t         (1000) t         (1000)      179 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/global_options.yaml
--rw-r--r--   0 t         (1000) t         (1000)      180 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/pane_ordering.yaml
--rw-r--r--   0 t         (1000) t         (1000)      314 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_awf.yaml
--rw-r--r--   0 t         (1000) t         (1000)      377 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_awf_multiple_windows.yaml
--rw-r--r--   0 t         (1000) t         (1000)      305 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_bs.yaml
--rw-r--r--   0 t         (1000) t         (1000)      317 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_bwb.yaml
--rw-r--r--   0 t         (1000) t         (1000)      134 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_missing_fail.yaml
--rw-r--r--   0 t         (1000) t         (1000)      392 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_multiple_plugins.yaml
--rw-r--r--   0 t         (1000) t         (1000)      309 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_owc.yaml
--rw-r--r--   0 t         (1000) t         (1000)      356 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_owc_multiple_windows.yaml
--rw-r--r--   0 t         (1000) t         (1000)      299 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_r.yaml
--rw-r--r--   0 t         (1000) t         (1000)      134 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/plugin_versions_fail.yaml
--rw-r--r--   0 t         (1000) t         (1000)      173 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/regression_00132_dots.yaml
--rw-r--r--   0 t         (1000) t         (1000)      181 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/session_options.yaml
--rw-r--r--   0 t         (1000) t         (1000)     1049 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/start_directory.yaml
--rw-r--r--   0 t         (1000) t         (1000)      974 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/start_directory_relative.yaml
--rw-r--r--   0 t         (1000) t         (1000)      212 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/suppress_history.yaml
--rw-r--r--   0 t         (1000) t         (1000)      213 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/three_pane.yaml
--rw-r--r--   0 t         (1000) t         (1000)      283 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/three_windows.yaml
--rw-r--r--   0 t         (1000) t         (1000)      310 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/two_pane.yaml
--rw-r--r--   0 t         (1000) t         (1000)      202 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/two_windows.yaml
--rw-r--r--   0 t         (1000) t         (1000)      260 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/window_automatic_rename.yaml
--rw-r--r--   0 t         (1000) t         (1000)      187 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/window_index.yaml
--rw-r--r--   0 t         (1000) t         (1000)      183 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/window_options.yaml
--rw-r--r--   0 t         (1000) t         (1000)      225 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/window_options_after.yaml
--rw-r--r--   0 t         (1000) t         (1000)      203 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacebuilder/window_shell.yaml
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacefreezer/
--rw-r--r--   0 t         (1000) t         (1000)      365 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/fixtures/workspacefreezer/sampleconfig.yaml
--rw-r--r--   0 t         (1000) t         (1000)    36948 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_cli.py
--rw-r--r--   0 t         (1000) t         (1000)    11356 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_config.py
--rw-r--r--   0 t         (1000) t         (1000)     2590 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_config_teamocil.py
--rw-r--r--   0 t         (1000) t         (1000)     1252 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_config_tmuxinator.py
--rw-r--r--   0 t         (1000) t         (1000)     2850 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_plugin.py
--rw-r--r--   0 t         (1000) t         (1000)      356 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_shell.py
--rw-r--r--   0 t         (1000) t         (1000)     1443 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_util.py
--rw-r--r--   0 t         (1000) t         (1000)    28675 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_workspacebuilder.py
--rw-r--r--   0 t         (1000) t         (1000)      857 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/test_workspacefreezer.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tests/tests/
--rw-r--r--   0 t         (1000) t         (1000)        0 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/tests/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      975 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tests/tests/test_helpers.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tmuxp/
--rw-r--r--   0 t         (1000) t         (1000)      434 2021-10-30 19:15:09.000000 tmuxp-1.9.3/tmuxp/__about__.py
--rw-r--r--   0 t         (1000) t         (1000)      341 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)      562 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/_compat.py
--rw-r--r--   0 t         (1000) t         (1000)    39746 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/cli.py
--rw-r--r--   0 t         (1000) t         (1000)    16717 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/config.py
--rw-r--r--   0 t         (1000) t         (1000)     1347 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/exc.py
--rw-r--r--   0 t         (1000) t         (1000)     3937 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/log.py
--rw-r--r--   0 t         (1000) t         (1000)     7241 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/plugin.py
--rw-r--r--   0 t         (1000) t         (1000)     6874 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/shell.py
--rw-r--r--   0 t         (1000) t         (1000)     4224 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/util.py
--rw-r--r--   0 t         (1000) t         (1000)    14331 2021-10-17 14:15:51.000000 tmuxp-1.9.3/tmuxp/workspacebuilder.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-10-30 19:15:51.000000 tmuxp-1.9.3/tmuxp.egg-info/
--rw-r--r--   0 t         (1000) t         (1000)     7936 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/PKG-INFO
--rw-r--r--   0 t         (1000) t         (1000)     6533 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/SOURCES.txt
--rw-r--r--   0 t         (1000) t         (1000)        1 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/dependency_links.txt
--rw-r--r--   0 t         (1000) t         (1000)       41 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/entry_points.txt
--rw-r--r--   0 t         (1000) t         (1000)        1 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/not-zip-safe
--rw-r--r--   0 t         (1000) t         (1000)       67 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/requires.txt
--rw-r--r--   0 t         (1000) t         (1000)        6 2021-10-30 19:15:50.000000 tmuxp-1.9.3/tmuxp.egg-info/top_level.txt
+-rwxr-xr-x   0        0        0      120 2021-10-17 14:15:51.559594 tmuxp-1.9.4/.tmuxp-before-script.sh
+-rw-r--r--   0        0        0      600 2021-10-17 14:15:51.559594 tmuxp-1.9.4/.tmuxp.yaml
+-rw-r--r--   0        0        0    39811 2022-01-11 03:59:26.646439 tmuxp-1.9.4/CHANGES
+-rw-r--r--   0        0        0     1076 2021-10-17 14:15:51.559594 tmuxp-1.9.4/LICENSE
+-rw-r--r--   0        0        0     6753 2022-01-08 13:28:09.871937 tmuxp-1.9.4/README.md
+-rw-r--r--   0        0        0     6269 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/Makefile
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_ext/__init__.py
+-rw-r--r--   0        0        0     6569 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_ext/aafig.py
+-rw-r--r--   0        0        0     1150 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/favicon.ico
+-rw-r--r--   0        0        0    17641 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/books/amazon-logo.png
+-rw-r--r--   0        0        0    52958 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/books/ibooks-logo.png
+-rw-r--r--   0        0        0     1681 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-128x128.png
+-rw-r--r--   0        0        0     1847 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-144x144.png
+-rw-r--r--   0        0        0     1885 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-152x152.png
+-rw-r--r--   0        0        0     2462 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-192x192.png
+-rw-r--r--   0        0        0     4795 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-384x384.png
+-rw-r--r--   0        0        0     7521 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-512x512.png
+-rw-r--r--   0        0        0     1084 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-72x72.png
+-rw-r--r--   0        0        0     1316 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/icons/icon-96x96.png
+-rw-r--r--   0        0        0      639 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/img/tmuxp.svg
+-rw-r--r--   0        0        0    38232 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/tao-tmux-screenshot.png
+-rw-r--r--   0        0        0   457272 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/tmuxp-demo.gif
+-rw-r--r--   0        0        0    13869 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/tmuxp-dev-screenshot.png
+-rw-r--r--   0        0        0   153463 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_static/tmuxp-shell.gif
+-rw-r--r--   0        0        0      636 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_templates/book.html
+-rw-r--r--   0        0        0     2261 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/_templates/layout.html
+-rw-r--r--   0        0        0     3727 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/about.md
+-rw-r--r--   0        0        0    21424 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/about_tmux.md
+-rw-r--r--   0        0        0     2135 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/api.md
+-rw-r--r--   0        0        0     5739 2022-01-08 12:45:19.791937 tmuxp-1.9.4/docs/cli.md
+-rw-r--r--   0        0        0     4839 2022-01-08 17:00:58.861937 tmuxp-1.9.4/docs/conf.py
+-rw-r--r--   0        0        0     5843 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/developing.md
+-rw-r--r--   0        0        0    10343 2022-01-08 13:28:09.881937 tmuxp-1.9.4/docs/examples.md
+-rw-r--r--   0        0        0     1676 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/glossary.md
+-rw-r--r--   0        0        0       65 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/history.md
+-rw-r--r--   0        0        0      384 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/index.md
+-rw-r--r--   0        0        0     1219 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/manifest.json
+-rw-r--r--   0        0        0     3521 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/plugin_system.md
+-rw-r--r--   0        0        0     2888 2021-10-17 14:15:51.569594 tmuxp-1.9.4/docs/quickstart.md
+-rw-r--r--   0        0        0      260 2021-10-17 14:15:51.569594 tmuxp-1.9.4/examples/2-pane-synchronized.json
+-rw-r--r--   0        0        0      177 2021-10-17 14:15:51.569594 tmuxp-1.9.4/examples/2-pane-synchronized.yaml
+-rw-r--r--   0        0        0      181 2021-10-17 14:15:51.569594 tmuxp-1.9.4/examples/2-pane-vertical.json
+-rw-r--r--   0        0        0      120 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/2-pane-vertical.yaml
+-rw-r--r--   0        0        0      386 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/3-pane.json
+-rw-r--r--   0        0        0      233 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/3-pane.yaml
+-rw-r--r--   0        0        0      406 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/4-pane.json
+-rw-r--r--   0        0        0      247 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/4-pane.yaml
+-rw-r--r--   0        0        0      823 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/blank-panes.json
+-rw-r--r--   0        0        0      640 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/blank-panes.yaml
+-rw-r--r--   0        0        0      659 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/env-variables.json
+-rw-r--r--   0        0        0      398 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/env-variables.yaml
+-rw-r--r--   0        0        0      814 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/focus-window-and-panes.json
+-rw-r--r--   0        0        0      479 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/focus-window-and-panes.yaml
+-rw-r--r--   0        0        0      548 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/main-pane-height.json
+-rw-r--r--   0        0        0      288 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/main-pane-height.yaml
+-rw-r--r--   0        0        0      686 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/options.json
+-rw-r--r--   0        0        0      411 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/options.yaml
+-rw-r--r--   0        0        0      442 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/plugin-system.json
+-rw-r--r--   0        0        0      285 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/plugin-system.yaml
+-rw-r--r--   0        0        0      337 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/session-environment.json
+-rw-r--r--   0        0        0      250 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/session-environment.yaml
+-rw-r--r--   0        0        0      363 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/shorthands.json
+-rw-r--r--   0        0        0      218 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/shorthands.yaml
+-rw-r--r--   0        0        0     1738 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/start-directory.json
+-rw-r--r--   0        0        0     1201 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/start-directory.yaml
+-rw-r--r--   0        0        0      872 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/suppress-history.json
+-rw-r--r--   0        0        0      612 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/suppress-history.yaml
+-rw-r--r--   0        0        0      444 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/window-index.json
+-rw-r--r--   0        0        0      305 2021-10-17 14:15:51.579594 tmuxp-1.9.4/examples/window-index.yaml
+-rw-r--r--   0        0        0     2597 2022-01-11 03:59:45.966439 tmuxp-1.9.4/pyproject.toml
+-rw-r--r--   0        0        0      264 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/__init__.py
+-rw-r--r--   0        0        0     2757 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/conftest.py
+-rw-r--r--   0        0        0       28 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/__init__.py
+-rw-r--r--   0        0        0      252 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/_util.py
+-rw-r--r--   0        0        0      161 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/__init__.py
+-rw-r--r--   0        0        0     2273 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/expand1.py
+-rw-r--r--   0        0        0      548 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/expand2-expanded.yaml
+-rw-r--r--   0        0        0      514 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/expand2-unexpanded.yaml
+-rw-r--r--   0        0        0      211 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/expand2.py
+-rw-r--r--   0        0        0      985 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/expand_blank.py
+-rw-r--r--   0        0        0      706 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/sampleconfig.py
+-rw-r--r--   0        0        0     4125 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/shell_command_before.py
+-rw-r--r--   0        0        0      372 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/shell_command_before_session-expected.yaml
+-rw-r--r--   0        0        0      174 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/shell_command_before_session.py
+-rw-r--r--   0        0        0      257 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/shell_command_before_session.yaml
+-rw-r--r--   0        0        0     1230 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config/trickle.py
+-rw-r--r--   0        0        0       58 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/__init__.py
+-rw-r--r--   0        0        0     5026 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/layouts.py
+-rw-r--r--   0        0        0     1848 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/layouts.yaml
+-rw-r--r--   0        0        0      745 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test1.py
+-rw-r--r--   0        0        0      166 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test1.yaml
+-rw-r--r--   0        0        0      777 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test2.py
+-rw-r--r--   0        0        0      158 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test2.yaml
+-rw-r--r--   0        0        0     1433 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test3.py
+-rw-r--r--   0        0        0      374 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test3.yaml
+-rw-r--r--   0        0        0      523 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test4.py
+-rw-r--r--   0        0        0       95 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_teamocil/test4.yaml
+-rw-r--r--   0        0        0       42 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/__init__.py
+-rw-r--r--   0        0        0      609 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test1.py
+-rw-r--r--   0        0        0      153 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test1.yaml
+-rw-r--r--   0        0        0     2508 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test2.py
+-rw-r--r--   0        0        0      818 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test2.yaml
+-rw-r--r--   0        0        0     2654 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test3.py
+-rw-r--r--   0        0        0      971 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test3.yaml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/__init__.py
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/__init__.py
+-rw-r--r--   0        0        0      746 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/all_pass.py
+-rw-r--r--   0        0        0      967 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/libtmux_version_fail.py
+-rw-r--r--   0        0        0      729 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/test_plugin_helpers.py
+-rw-r--r--   0        0        0      924 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/tmux_version_fail.py
+-rw-r--r--   0        0        0      945 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/tmuxp_version_fail.py
+-rw-r--r--   0        0        0      384 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/__init__.py
+-rw-r--r--   0        0        0      624 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/plugin.py
+-rw-r--r--   0        0        0      376 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/tmuxp_test_plugin_bs/__init__.py
+-rw-r--r--   0        0        0      249 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/tmuxp_test_plugin_bs/plugin.py
+-rw-r--r--   0        0        0      385 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/tmuxp_test_plugin_bwb/__init__.py
+-rw-r--r--   0        0        0      271 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/tmuxp_test_plugin_bwb/plugin.py
+-rw-r--r--   0        0        0      355 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/tmuxp_test_plugin_fail/__init__.py
+-rw-r--r--   0        0        0      273 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/tmuxp_test_plugin_fail/plugin.py
+-rw-r--r--   0        0        0      379 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/__init__.py
+-rw-r--r--   0        0        0      610 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/plugin.py
+-rw-r--r--   0        0        0      369 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/tmuxp_test_plugin_r/__init__.py
+-rw-r--r--   0        0        0      239 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/tmuxp_test_plugin_r/plugin.py
+-rwxr-xr-x   0        0        0       97 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/script_complete.sh
+-rwxr-xr-x   0        0        0      180 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/script_failed.sh
+-rw-r--r--   0        0        0       87 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/config_script_completes.yaml
+-rw-r--r--   0        0        0       95 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/config_script_fails.yaml
+-rw-r--r--   0        0        0       89 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/config_script_not_exists.yaml
+-rw-r--r--   0        0        0      266 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/env_var_options.yaml
+-rw-r--r--   0        0        0      135 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/environment_vars.yaml
+-rw-r--r--   0        0        0      487 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/focus_and_pane.yaml
+-rw-r--r--   0        0        0      179 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/global_options.yaml
+-rw-r--r--   0        0        0      180 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/pane_ordering.yaml
+-rw-r--r--   0        0        0      314 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_awf.yaml
+-rw-r--r--   0        0        0      377 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_awf_multiple_windows.yaml
+-rw-r--r--   0        0        0      305 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_bs.yaml
+-rw-r--r--   0        0        0      317 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_bwb.yaml
+-rw-r--r--   0        0        0      134 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_missing_fail.yaml
+-rw-r--r--   0        0        0      392 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_multiple_plugins.yaml
+-rw-r--r--   0        0        0      309 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_owc.yaml
+-rw-r--r--   0        0        0      356 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_owc_multiple_windows.yaml
+-rw-r--r--   0        0        0      299 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_r.yaml
+-rw-r--r--   0        0        0      134 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/plugin_versions_fail.yaml
+-rw-r--r--   0        0        0      173 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/regression_00132_dots.yaml
+-rw-r--r--   0        0        0      181 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/session_options.yaml
+-rw-r--r--   0        0        0     1049 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/start_directory.yaml
+-rw-r--r--   0        0        0      974 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/start_directory_relative.yaml
+-rw-r--r--   0        0        0      212 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/suppress_history.yaml
+-rw-r--r--   0        0        0      213 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/three_pane.yaml
+-rw-r--r--   0        0        0      283 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/three_windows.yaml
+-rw-r--r--   0        0        0      310 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/two_pane.yaml
+-rw-r--r--   0        0        0      202 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/two_windows.yaml
+-rw-r--r--   0        0        0      260 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/window_automatic_rename.yaml
+-rw-r--r--   0        0        0      187 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/window_index.yaml
+-rw-r--r--   0        0        0      183 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/window_options.yaml
+-rw-r--r--   0        0        0      225 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/window_options_after.yaml
+-rw-r--r--   0        0        0      203 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacebuilder/window_shell.yaml
+-rw-r--r--   0        0        0      365 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/fixtures/workspacefreezer/sampleconfig.yaml
+-rw-r--r--   0        0        0    36950 2022-01-11 02:57:44.446439 tmuxp-1.9.4/tests/test_cli.py
+-rw-r--r--   0        0        0    11356 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_config.py
+-rw-r--r--   0        0        0     2590 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_config_teamocil.py
+-rw-r--r--   0        0        0     1252 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_config_tmuxinator.py
+-rw-r--r--   0        0        0     2850 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_plugin.py
+-rw-r--r--   0        0        0      356 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_shell.py
+-rw-r--r--   0        0        0     1443 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_util.py
+-rw-r--r--   0        0        0    28675 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_workspacebuilder.py
+-rw-r--r--   0        0        0      857 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/test_workspacefreezer.py
+-rw-r--r--   0        0        0        0 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/tests/__init__.py
+-rw-r--r--   0        0        0      975 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tests/tests/test_helpers.py
+-rw-r--r--   0        0        0      507 2022-01-11 03:59:42.076439 tmuxp-1.9.4/tmuxp/__about__.py
+-rw-r--r--   0        0        0      341 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/__init__.py
+-rw-r--r--   0        0        0      562 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/_compat.py
+-rw-r--r--   0        0        0    40052 2022-01-08 13:28:09.881937 tmuxp-1.9.4/tmuxp/cli.py
+-rw-r--r--   0        0        0    16717 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/config.py
+-rw-r--r--   0        0        0     1347 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/exc.py
+-rw-r--r--   0        0        0     3937 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/log.py
+-rw-r--r--   0        0        0     7241 2022-01-08 21:36:59.911937 tmuxp-1.9.4/tmuxp/plugin.py
+-rw-r--r--   0        0        0     6874 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/shell.py
+-rw-r--r--   0        0        0     4224 2021-10-17 14:15:51.579594 tmuxp-1.9.4/tmuxp/util.py
+-rw-r--r--   0        0        0    14331 2022-01-08 12:41:26.511937 tmuxp-1.9.4/tmuxp/workspacebuilder.py
+-rw-r--r--   0        0        0     7800 2022-01-11 04:01:24.121249 tmuxp-1.9.4/setup.py
+-rw-r--r--   0        0        0     8292 2022-01-11 04:01:24.121739 tmuxp-1.9.4/PKG-INFO
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `tmuxp-1.9.3/.tmuxp.yaml` & `tmuxp-1.9.4/.tmuxp.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/CHANGES` & `tmuxp-1.9.4/CHANGES`

 * *Files 3% similar despite different names*

```diff
@@ -1,30 +1,70 @@
 # Changelog
 
 ## current
 
 - _Insert changes/features/fixes for next release here_
 
+## tmuxp 1.9.4 (2022-01-10)
+
+#### Packaging
+
+- `poetry build` used to package in place of `python setup.py build` (#729)
+
+  Package maintainers: If you run into any issues at
+  [#625](https://github.com/tmux-python/tmuxp/issues/625).
+
+  Additionally, `libtmux` has been pinned to a similar release at
+  [0.10.3](https://pypi.org/project/libtmux/0.10.3/) which has used the new
+  build process.
+
+- `poetry publish` instead of `twine upload dist/*` (#729)
+
+  Similar to the above, reach out to the #625 issue if you bump into problems.
+
+#### What's new
+
+- `tmuxp edit` for configuration changes (#707, @GlebPoljakov)
+
+  Inside of configuration directory: `tmuxp edit yourconfig`
+
+  Inside a project: `tmuxp edit .`
+
+### Removed support
+
+- Python 3.6 support has been removed (#726)
+
+### Development
+
+- We are trying `.pre-commit-config.yaml` in pull requests to automate
+  black, isort and flake8 for those who forget (#726)
+- Poetry update 1.1.7 -> 1.1.12 and use new installer URL (#726)
+- Black updated 21.9b0 -> 21.12b0 (#726)
+
 ## tmuxp 1.9.3 (2021-10-30)
+
 - #700: Add `-h` / `--help` option, thanks @GHPS
 - #689: Update poetry to 1.1
   - CI: Use poetry 1.1.7 and `install-poetry.py` installer
   - Relock poetry.lock at 1.1 (w/ 1.1.7's fix)
 - #696: Typo fix, thanks @inkch
 
 ## tmuxp 1.9.2 (2021-06-17)
+
 - #686: Allow click 8.0.x
 - Remove `manual/`, move to https://github.com/tmux-python/tmux-manuals
 
 ## tmuxp 1.9.1 (2021-06-16)
+
 - libtmux: Update to 0.10.1+ to include `Window.select_window()` fix
 
   https://github.com/tmux-python/libtmux/pull/271
 
 ## tmuxp 1.9.0 (2021-06-16)
+
 - libtmux: Update to 0.10.x
 
 ## tmuxp 1.8.2 (2021-06-15)
 
 - {issue}`474` Re-release with `python setup.py sdist bdist_wheel` to
   fix missing test files
```

### Comparing `tmuxp-1.9.3/LICENSE` & `tmuxp-1.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/PKG-INFO` & `tmuxp-1.9.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,37 +1,46 @@
 Metadata-Version: 2.1
 Name: tmuxp
-Version: 1.9.3
+Version: 1.9.4
 Summary: tmux session manager
-Home-page: https://github.com/tmux-python/tmuxp
+Home-page: http://github.com/tmux-python/tmuxp/
+License: MIT
+Keywords: tmux,session manager,terminal,ncurses
 Author: Tony Narlock
 Author-email: tony@git-pull.com
-License: MIT
-Download-URL: https://pypi.org/project/tmuxp/
-Project-URL: Documentation, https://tmuxp.git-pull.com
-Project-URL: Code, https://github.com/tmux-python/tmuxp
-Project-URL: Issue tracker, https://github.com/tmux-python/tmuxp/issues
-Keywords: tmuxp
-Platform: UNKNOWN
+Requires-Python: >=3.7,<4.0
 Classifier: Development Status :: 5 - Production/Stable
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: POSIX
-Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: MacOS :: MacOS X
+Classifier: Operating System :: POSIX
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: Implementation :: PyPy
-Classifier: Topic :: Utilities
 Classifier: Topic :: System :: Shells
+Classifier: Topic :: Utilities
+Provides-Extra: coverage
+Provides-Extra: docs
+Provides-Extra: format
+Provides-Extra: lint
+Provides-Extra: test
+Requires-Dist: click (>7,<8.1)
+Requires-Dist: colorama (>=0.3.9)
+Requires-Dist: kaptan (>=0.5.10)
+Requires-Dist: libtmux (>=0.10.3,<0.11.0)
+Project-URL: Bug Tracker, https://github.com/tmux-python/tmuxp/issues
+Project-URL: Changes, https://github.com/tmux-python/tmuxp/blob/master/CHANGES
+Project-URL: Documentation, https://tmuxp.git-pull.com
+Project-URL: Repository, https://github.com/tmux-python/tmuxp
 Description-Content-Type: text/markdown
-License-File: LICENSE
 
 tmuxp, tmux session manager. built on
 [libtmux](https://github.com/tmux-python/libtmux).
 
 [![Python Package](https://img.shields.io/pypi/v/tmuxp.svg)](http://badge.fury.io/py/tmuxp)
 [![Docs](https://github.com/tmux-python/tmuxp/workflows/Publish%20Docs/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22Publish+Docs%22)
 [![Build status](https://github.com/tmux-python/tmuxp/workflows/tests/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22tests%22)
@@ -266,19 +275,18 @@
 right for the value you get out of the project.
 
 See donation options at <https://git-pull.com/support.html>.
 
 # Project details
 
 - tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-- python support: >= 3.6, pypy, pypy3
+- python support: >= 3.7, pypy, pypy3
 - Source: <https://github.com/tmux-python/tmuxp>
 - Docs: <https://tmuxp.git-pull.com>
 - API: <https://tmuxp.git-pull.com/api.html>
 - Changelog: <https://tmuxp.git-pull.com/history.html>
 - Issues: <https://github.com/tmux-python/tmuxp/issues>
 - Test Coverage: <https://codecov.io/gh/tmux-python/tmuxp>
 - pypi: <https://pypi.python.org/pypi/tmuxp>
 - Open Hub: <https://www.openhub.net/p/tmuxp-python>
 - License: [MIT](http://opensource.org/licenses/MIT).
 
-
```

### Comparing `tmuxp-1.9.3/README.md` & `tmuxp-1.9.4/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -235,15 +235,15 @@
 right for the value you get out of the project.
 
 See donation options at <https://git-pull.com/support.html>.
 
 # Project details
 
 - tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-- python support: >= 3.6, pypy, pypy3
+- python support: >= 3.7, pypy, pypy3
 - Source: <https://github.com/tmux-python/tmuxp>
 - Docs: <https://tmuxp.git-pull.com>
 - API: <https://tmuxp.git-pull.com/api.html>
 - Changelog: <https://tmuxp.git-pull.com/history.html>
 - Issues: <https://github.com/tmux-python/tmuxp/issues>
 - Test Coverage: <https://codecov.io/gh/tmux-python/tmuxp>
 - pypi: <https://pypi.python.org/pypi/tmuxp>
```

### Comparing `tmuxp-1.9.3/docs/about.md` & `tmuxp-1.9.4/docs/about.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/about_tmux.md` & `tmuxp-1.9.4/docs/about_tmux.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/api.md` & `tmuxp-1.9.4/docs/api.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/cli.md` & `tmuxp-1.9.4/docs/cli.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/developing.md` & `tmuxp-1.9.4/docs/developing.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/examples.md` & `tmuxp-1.9.4/docs/examples.md`

 * *Files 0% similar despite different names*

```diff
@@ -383,24 +383,23 @@
 ### JSON
 
 ```{literalinclude} ../.tmuxp.json
 :language: json
 
 ```
 
-
 ## Multi-line commands
 
 You can use YAML's multiline syntax to easily split multiple
 commands into the same shell command: https://stackoverflow.com/a/21699210
 
 ```{code-block} yaml
 
 session_name: my project
-shell_command_before: 
+shell_command_before:
 - >
   [ -d `.venv/bin/activate` ] &&
   source .venv/bin/activate &&
   reset
 - sleep 1
 windows:
 - window_name: first window
```

### Comparing `tmuxp-1.9.3/docs/glossary.md` & `tmuxp-1.9.4/docs/glossary.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/plugin_system.md` & `tmuxp-1.9.4/docs/plugin_system.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/docs/quickstart.md` & `tmuxp-1.9.4/docs/quickstart.md`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/blank-panes.json` & `tmuxp-1.9.4/examples/blank-panes.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/blank-panes.yaml` & `tmuxp-1.9.4/examples/blank-panes.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/env-variables.json` & `tmuxp-1.9.4/examples/env-variables.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/focus-window-and-panes.json` & `tmuxp-1.9.4/examples/focus-window-and-panes.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/main-pane-height.json` & `tmuxp-1.9.4/examples/main-pane-height.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/options.json` & `tmuxp-1.9.4/examples/options.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/start-directory.json` & `tmuxp-1.9.4/examples/start-directory.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/start-directory.yaml` & `tmuxp-1.9.4/examples/start-directory.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/suppress-history.json` & `tmuxp-1.9.4/examples/suppress-history.json`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/examples/suppress-history.yaml` & `tmuxp-1.9.4/examples/suppress-history.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/pyproject.toml` & `tmuxp-1.9.4/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,81 +1,95 @@
 [tool.black]
 skip-string-normalization = true
 
 [tool.poetry]
 name = "tmuxp"
-version = "1.9.3"
+version = "1.9.4"
 description = "tmux session manager"
 license = "MIT"
 authors = ["Tony Narlock <tony@git-pull.com>"]
 classifiers = [
   "Development Status :: 5 - Production/Stable",
   "License :: OSI Approved :: MIT License",
   "Operating System :: POSIX",
   "Operating System :: MacOS :: MacOS X",
   "Environment :: Web Environment",
   "Intended Audience :: Developers",
   "Programming Language :: Python",
-  "Programming Language :: Python :: 3.6",
   "Programming Language :: Python :: 3.7",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: 3.9",
+  "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: Implementation :: PyPy",
   "Topic :: Utilities",
   "Topic :: System :: Shells"
 ]
 keywords = ["tmux", "session manager", "terminal", "ncurses"]
 homepage = "http://github.com/tmux-python/tmuxp/"
 readme = "README.md"
+packages = [
+    { include = "tmuxp" }
+]
+include = [
+    { path = "CHANGES", format = "sdist" },
+    { path = ".tmuxp.yaml", format = "sdist" },
+    { path = ".tmuxp-before-script.sh", format = "sdist" },
+    { path = "tests", format = "sdist" },
+    { path = "examples", format = "sdist" },
+    { path = "docs", format = "sdist" },
+]
 
 [tool.poetry.urls]
 "Bug Tracker" = "https://github.com/tmux-python/tmuxp/issues"
 Documentation = "https://tmuxp.git-pull.com"
 Repository = "https://github.com/tmux-python/tmuxp"
+Changes = "https://github.com/tmux-python/tmuxp/blob/master/CHANGES"
 
 [tool.poetry.scripts]
 tmuxp = 'tmuxp:cli.cli'
 
 [tool.poetry.dependencies]
-python = "^3.6"
+python = "^3.7"
 click = ">7,<8.1"
 kaptan = ">=0.5.10"
-libtmux = "~0.10.2"
+libtmux = "~0.10.3"
 colorama = ">=0.3.9"
 
 [tool.poetry.dev-dependencies]
 ### Docs ###
 sphinx = "*"
 alagitpull = "~0.1.0"
 sphinx-issues = "^1.2.0"
 aafigure = ">=0.6"
 pillow = "*"
-sphinx-autodoc-typehints = "^1.12.0"
-myst_parser = "^0.15.0"
+sphinx-autodoc-typehints = "~1.14.1"
+myst_parser = "~0.16.1"
 
 ### Testing ###
 pytest = "*"
 pytest-rerunfailures = "*"
 pytest-mock = "*"
 pytest-cov = "*"
+tox = {version = "^3.24.5", extras = ["test"]}
+tox-poetry-installer = {extras = ["poetry"], version = "^0.8.3"}
 
 ### Coverage ###
 codecov = "*"
 coverage = "*"
 
 ### Format ###
-black = {version="==21.9b0", python="^3.6.2"}
+black = "==21.12b0"
 isort = "*"
 
 ### Lint ###
 flake8 = "*"
 
-### Deploy ###
-twine = "*"
-
 [tool.poetry.extras]
 docs = ["sphinx", "myst_parser", "sphinx-issues", "alagitpull", "sphinx-autodoc-typehints", "aafigure", "pillow"]
-test = ["pytest", "pytest-rerunfailures", "pytest-mock"]
+test = ["pytest", "pytest-rerunfailures", "pytest-mock", "tox", "tox-poetry-installer"]
 coverage = ["codecov", "coverage", "pytest-cov"]
 format = ["black", "isort"]
 lint = ["flake8"]
-deploy = ["twine"]
+
+[build-system]
+requires = ["poetry_core>=1.0.0"]
+build-backend = "poetry.core.masonry.api"
```

### Comparing `tmuxp-1.9.3/tests/conftest.py` & `tmuxp-1.9.4/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/expand1.py` & `tmuxp-1.9.4/tests/fixtures/config/expand1.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/expand2-expanded.yaml` & `tmuxp-1.9.4/tests/fixtures/config/expand2-expanded.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/expand2-unexpanded.yaml` & `tmuxp-1.9.4/tests/fixtures/config/expand2-unexpanded.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/expand_blank.py` & `tmuxp-1.9.4/tests/fixtures/config/expand_blank.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/sampleconfig.py` & `tmuxp-1.9.4/tests/fixtures/config/sampleconfig.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/shell_command_before.py` & `tmuxp-1.9.4/tests/fixtures/config/shell_command_before.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config/trickle.py` & `tmuxp-1.9.4/tests/fixtures/config/trickle.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/layouts.py` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/layouts.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/layouts.yaml` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/layouts.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/test1.py` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/test1.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/test2.py` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/test2.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/test3.py` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/test3.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_teamocil/test4.py` & `tmuxp-1.9.4/tests/fixtures/config_teamocil/test4.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test1.py` & `tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test1.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test2.py` & `tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test2.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test2.yaml` & `tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test2.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test3.py` & `tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test3.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/config_tmuxinator/test3.yaml` & `tmuxp-1.9.4/tests/fixtures/config_tmuxinator/test3.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/all_pass.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/all_pass.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/libtmux_version_fail.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/libtmux_version_fail.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/test_plugin_helpers.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/test_plugin_helpers.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/tmux_version_fail.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/tmux_version_fail.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/partials/tmuxp_version_fail.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/partials/tmuxp_version_fail.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/plugin.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/tmuxp_test_plugin_awf/plugin.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/plugin.py` & `tmuxp-1.9.4/tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/tmuxp_test_plugin_owc/plugin.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/workspacebuilder/start_directory.yaml` & `tmuxp-1.9.4/tests/fixtures/workspacebuilder/start_directory.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/fixtures/workspacebuilder/start_directory_relative.yaml` & `tmuxp-1.9.4/tests/fixtures/workspacebuilder/start_directory_relative.yaml`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_cli.py` & `tmuxp-1.9.4/tests/test_cli.py`

 * *Files 0% similar despite different names*

```diff
@@ -757,27 +757,29 @@
 def test_import(cli_args, monkeypatch):
     runner = CliRunner()
 
     result = runner.invoke(cli.cli, cli_args)
     assert 'tmuxinator' in result.output
     assert 'teamocil' in result.output
 
+
 @pytest.mark.parametrize(
     "cli_args",
     [
         (['--help']),
         (['-h']),
     ],
 )
 def test_help(cli_args, monkeypatch):
     runner = CliRunner()
 
     result = runner.invoke(cli.cli, cli_args)
     assert 'Usage: cli [OPTIONS] COMMAND [ARGS]...' in result.output
 
+
 @pytest.mark.parametrize(
     "cli_args,inputs",
     [
         (
             ['import', 'teamocil', './.teamocil/config.yaml'],
             ['\n', 'y\n', './la.yaml\n', 'y\n'],
         ),
```

### Comparing `tmuxp-1.9.3/tests/test_config.py` & `tmuxp-1.9.4/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_config_teamocil.py` & `tmuxp-1.9.4/tests/test_config_teamocil.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_config_tmuxinator.py` & `tmuxp-1.9.4/tests/test_config_tmuxinator.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_plugin.py` & `tmuxp-1.9.4/tests/test_plugin.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_util.py` & `tmuxp-1.9.4/tests/test_util.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_workspacebuilder.py` & `tmuxp-1.9.4/tests/test_workspacebuilder.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/test_workspacefreezer.py` & `tmuxp-1.9.4/tests/test_workspacefreezer.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tests/tests/test_helpers.py` & `tmuxp-1.9.4/tests/tests/test_helpers.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/_compat.py` & `tmuxp-1.9.4/tmuxp/_compat.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/cli.py` & `tmuxp-1.9.4/tmuxp/cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 
 """
 import importlib
 import logging
 import os
 import platform
 import sys
+from subprocess import call
 
 import click
 import kaptan
 from click.exceptions import FileError
 
 from libtmux import __version__ as libtmux_version
 from libtmux.common import (
@@ -745,15 +746,15 @@
             _reattach(builder)
         else:
             sys.exit()
 
     return _setup_plugins(builder)
 
 
-@click.group(context_settings={'obj': {}, 'help_option_names':['-h', '--help']})
+@click.group(context_settings={'obj': {}, 'help_option_names': ['-h', '--help']})
 @click.version_option(__version__, '-V', '--version', message='%(prog)s %(version)s')
 @click.option(
     '--log-level',
     default='INFO',
     help='Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)',
 )
 def cli(log_level):
@@ -1205,14 +1206,23 @@
     if confirmed:
         buf = open(newfile, 'w')
         buf.write(newconfig)
         buf.close()
         print('New config saved to <%s>.' % newfile)
 
 
+@cli.command(name='edit', short_help='Run $EDITOR on config.')
+@click.argument('config', type=ConfigPath(exists=True), nargs=1)
+def command_edit_config(config):
+    config = scan_config(config)
+
+    sys_editor = os.environ.get('EDITOR', 'vim')
+    call([sys_editor, config])
+
+
 @cli.command(
     name='ls', short_help='List configured sessions in {}.'.format(get_config_dir())
 )
 def command_ls():
     tmuxp_dir = get_config_dir()
     if os.path.exists(tmuxp_dir) and os.path.isdir(tmuxp_dir):
         for f in sorted(os.listdir(tmuxp_dir)):
```

### Comparing `tmuxp-1.9.3/tmuxp/config.py` & `tmuxp-1.9.4/tmuxp/config.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/exc.py` & `tmuxp-1.9.4/tmuxp/exc.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/log.py` & `tmuxp-1.9.4/tmuxp/log.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/plugin.py` & `tmuxp-1.9.4/tmuxp/plugin.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/shell.py` & `tmuxp-1.9.4/tmuxp/shell.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/util.py` & `tmuxp-1.9.4/tmuxp/util.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp/workspacebuilder.py` & `tmuxp-1.9.4/tmuxp/workspacebuilder.py`

 * *Files identical despite different names*

### Comparing `tmuxp-1.9.3/tmuxp.egg-info/PKG-INFO` & `tmuxp-1.9.4/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,284 +1,34 @@
-Metadata-Version: 2.1
-Name: tmuxp
-Version: 1.9.3
-Summary: tmux session manager
-Home-page: https://github.com/tmux-python/tmuxp
-Author: Tony Narlock
-Author-email: tony@git-pull.com
-License: MIT
-Download-URL: https://pypi.org/project/tmuxp/
-Project-URL: Documentation, https://tmuxp.git-pull.com
-Project-URL: Code, https://github.com/tmux-python/tmuxp
-Project-URL: Issue tracker, https://github.com/tmux-python/tmuxp/issues
-Keywords: tmuxp
-Platform: UNKNOWN
-Classifier: Development Status :: 5 - Production/Stable
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: POSIX
-Classifier: Operating System :: MacOS :: MacOS X
-Classifier: Environment :: Web Environment
-Classifier: Intended Audience :: Developers
-Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3.6
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: Implementation :: PyPy
-Classifier: Topic :: Utilities
-Classifier: Topic :: System :: Shells
-Description-Content-Type: text/markdown
-License-File: LICENSE
+# -*- coding: utf-8 -*-
+from setuptools import setup
 
-tmuxp, tmux session manager. built on
-[libtmux](https://github.com/tmux-python/libtmux).
+packages = \
+['tmuxp']
 
-[![Python Package](https://img.shields.io/pypi/v/tmuxp.svg)](http://badge.fury.io/py/tmuxp)
-[![Docs](https://github.com/tmux-python/tmuxp/workflows/Publish%20Docs/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22Publish+Docs%22)
-[![Build status](https://github.com/tmux-python/tmuxp/workflows/tests/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22tests%22)
-[![Code Coverage](https://codecov.io/gh/tmux-python/tmuxp/branch/master/graph/badge.svg)](https://codecov.io/gh/tmux-python/tmuxp)
-![License](https://img.shields.io/github/license/tmux-python/tmuxp.svg)
+package_data = \
+{'': ['*']}
 
-**We need help!** tmuxp is a trusted session manager for tmux. If you
-could lend your time to helping answer issues and QA pull requests,
-please do! See [issue
-#290](https://github.com/tmux-python/tmuxp/issues/290)!
-
-**New to tmux?** [The Tao of tmux](https://leanpub.com/the-tao-of-tmux)
-is available on Leanpub and [Amazon Kindle](http://amzn.to/2gPfRhC).
-Read and browse the book for free [on the
-web](https://leanpub.com/the-tao-of-tmux/read).
-
-# Installation
-
-## Pip
-
-```shell
-$ pip install --user tmuxp
-```
-
-## Homebrew
-
-```shell
-$ brew install tmuxp
-```
-
-# Load a tmux session
-
-Load tmux sessions via json and YAML,
-[tmuxinator](https://github.com/aziz/tmuxinator) and
-[teamocil](https://github.com/remiprev/teamocil) style.
-
-```yaml
-session_name: 4-pane-split
-windows:
-  - window_name: dev window
-    layout: tiled
-    shell_command_before:
-      - cd ~/ # run as a first command in all panes
-    panes:
-      - shell_command: # pane no. 1
-          - cd /var/log # run multiple commands in this pane
-          - ls -al | grep \.log
-      - echo second pane # pane no. 2
-      - echo third pane # pane no. 3
-      - echo forth pane # pane no. 4
-```
-
-Save as _mysession.yaml_, and load:
-
-```sh
-$ tmuxp load ./mysession.yaml
-```
-
-Projects with _.tmuxp.yaml_ or _.tmuxp.json_ load via directory:
-
-```sh
-$ tmuxp load path/to/my/project/
-```
-
-Load multiple at once (in bg, offer to attach last):
-
-```sh
-$ tmuxp load mysession ./another/project/
-```
-
-Name a session:
-
-```bash
-$ tmuxp load -s session_name ./mysession.yaml
-```
-
-[simple](http://tmuxp.git-pull.com/examples.html#short-hand-inline) and
-[very
-elaborate](http://tmuxp.git-pull.com/examples.html#super-advanced-dev-environment)
-config examples
-
-# User-level configurations
-
-tmuxp checks for configs in user directories:
-
-- `$TMUXP_CONFIGDIR`, if set
-- `$XDG_CONFIG_HOME`, usually _$HOME/.config/tmuxp/_
-- `$HOME/.tmuxp/`
-
-Load your tmuxp config from anywhere by using the filename, assuming
-_\~/.config/tmuxp/mysession.yaml_ (or _.json_):
-
-```sh
-$ tmuxp load mysession
-```
-
-See [author's tmuxp configs](https://github.com/tony/tmuxp-config) and
-the projects'
-[tmuxp.yaml](https://github.com/tmux-python/tmuxp/blob/master/.tmuxp.yaml).
-
-# Shell
-
-_New in 1.6.0_:
-
-`tmuxp shell` launches into a python console preloaded with the attached
-server, session, and window in
-[libtmux](https://github.com/tmux-python/libtmux) objects.
-
-```shell
-$ tmuxp shell
-
-(Pdb) server
-<libtmux.server.Server object at 0x7f7dc8e69d10>
-(Pdb) server.sessions
-[Session($1 your_project)]
-(Pdb) session
-Session($1 your_project)
-(Pdb) session.name
-'your_project'
-(Pdb) window
-Window(@3 1:your_window, Session($1 your_project))
-(Pdb) window.name
-'your_window'
-(Pdb) window.panes
-[Pane(%6 Window(@3 1:your_window, Session($1 your_project)))
-(Pdb) pane
-Pane(%6 Window(@3 1:your_window, Session($1 your_project))
-```
-
-Python 3.7+ supports [PEP
-553](https://www.python.org/dev/peps/pep-0553/) `breakpoint()`
-(including `PYTHONBREAKPOINT`). Also supports direct commands via `-c`:
-
-```shell
-$ tmuxp shell -c 'print(window.name)'
-my_window
-
-$ tmuxp shell -c 'print(window.name.upper())'
-MY_WINDOW
-```
-
-Read more on [tmuxp shell](https://tmuxp.git-pull.com/cli.html#shell) in
-the CLI docs.
-
-# Pre-load hook
-
-Run custom startup scripts (such as installing project dependencies
-before loading tmux. See the
-[bootstrap_env.py](https://github.com/tmux-python/tmuxp/blob/master/bootstrap_env.py)
-and
-[before_script](http://tmuxp.git-pull.com/examples.html#bootstrap-project-before-launch)
-example
-
-# Load in detached state
-
-You can also load sessions in the background by passing `-d` flag
-
-# Screenshot
-
-<img src="https://raw.githubusercontent.com/tmux-python/tmuxp/master/docs/_static/tmuxp-demo.gif" class="align-center" style="width:45.0%" alt="image" />
-
-# Freeze a tmux session
-
-Snapshot your tmux layout, pane paths, and window/session names.
-
-```sh
-$ tmuxp freeze session-name
-```
-
-See more about [freezing
-tmux](http://tmuxp.git-pull.com/cli.html#freeze-sessions) sessions.
-
-# Convert a session file
-
-Convert a session file from yaml to json and vice versa.
-
-```sh
-$ tmuxp convert filename
-```
-
-This will prompt you for confirmation and shows you the new file that is
-going to be written.
-
-You can auto confirm the prompt. In this case no preview will be shown.
-
-```sh
-$ tmuxp convert -y filename
-$ tmuxp convert --yes filename
-```
-
-# Plugin System
-
-tmuxp has a plugin system to allow for custom behavior. See more about
-the [Plugin System](http://tmuxp.git-pull.com/plugin_system.html).
-
-# Debugging Helpers
-
-The `load` command provides a way to log output to a log file for
-debugging purposes.
-
-```sh
-$ tmuxp load --log-file <log-file-name> .
-```
-
-Collect system info to submit with a Github issue:
-
-```sh
-$ tmuxp debug-info
-------------------
-environment:
-    system: Linux
-    arch: x86_64
-
-# ... so on
-```
-
-# Docs / Reading material
-
-See the [Quickstart](http://tmuxp.git-pull.com/quickstart.html).
-
-[Documentation](http://tmuxp.git-pull.com) homepage (also in
-[中文](http://tmuxp-zh.rtfd.org/))
-
-Want to learn more about tmux itself? [Read The Tao of Tmux
-online](http://tmuxp.git-pull.com/about_tmux.html).
-
-# Donations
-
-Your donations fund development of new features, testing and support.
-Your money will go directly to maintenance and development of the
-project. If you are an individual, feel free to give whatever feels
-right for the value you get out of the project.
-
-See donation options at <https://git-pull.com/support.html>.
-
-# Project details
-
-- tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-- python support: >= 3.6, pypy, pypy3
-- Source: <https://github.com/tmux-python/tmuxp>
-- Docs: <https://tmuxp.git-pull.com>
-- API: <https://tmuxp.git-pull.com/api.html>
-- Changelog: <https://tmuxp.git-pull.com/history.html>
-- Issues: <https://github.com/tmux-python/tmuxp/issues>
-- Test Coverage: <https://codecov.io/gh/tmux-python/tmuxp>
-- pypi: <https://pypi.python.org/pypi/tmuxp>
-- Open Hub: <https://www.openhub.net/p/tmuxp-python>
-- License: [MIT](http://opensource.org/licenses/MIT).
+install_requires = \
+['click>7,<8.1', 'colorama>=0.3.9', 'kaptan>=0.5.10', 'libtmux>=0.10.3,<0.11.0']
+
+entry_points = \
+{'console_scripts': ['tmuxp = tmuxp:cli.cli']}
+
+setup_kwargs = {
+    'name': 'tmuxp',
+    'version': '1.9.4',
+    'description': 'tmux session manager',
+    'long_description': 'tmuxp, tmux session manager. built on\n[libtmux](https://github.com/tmux-python/libtmux).\n\n[![Python Package](https://img.shields.io/pypi/v/tmuxp.svg)](http://badge.fury.io/py/tmuxp)\n[![Docs](https://github.com/tmux-python/tmuxp/workflows/Publish%20Docs/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22Publish+Docs%22)\n[![Build status](https://github.com/tmux-python/tmuxp/workflows/tests/badge.svg)](https://github.com/tmux-python/tmuxp/actions?query=workflow%3A%22tests%22)\n[![Code Coverage](https://codecov.io/gh/tmux-python/tmuxp/branch/master/graph/badge.svg)](https://codecov.io/gh/tmux-python/tmuxp)\n![License](https://img.shields.io/github/license/tmux-python/tmuxp.svg)\n\n**We need help!** tmuxp is a trusted session manager for tmux. If you\ncould lend your time to helping answer issues and QA pull requests,\nplease do! See [issue\n#290](https://github.com/tmux-python/tmuxp/issues/290)!\n\n**New to tmux?** [The Tao of tmux](https://leanpub.com/the-tao-of-tmux)\nis available on Leanpub and [Amazon Kindle](http://amzn.to/2gPfRhC).\nRead and browse the book for free [on the\nweb](https://leanpub.com/the-tao-of-tmux/read).\n\n# Installation\n\n## Pip\n\n```shell\n$ pip install --user tmuxp\n```\n\n## Homebrew\n\n```shell\n$ brew install tmuxp\n```\n\n# Load a tmux session\n\nLoad tmux sessions via json and YAML,\n[tmuxinator](https://github.com/aziz/tmuxinator) and\n[teamocil](https://github.com/remiprev/teamocil) style.\n\n```yaml\nsession_name: 4-pane-split\nwindows:\n  - window_name: dev window\n    layout: tiled\n    shell_command_before:\n      - cd ~/ # run as a first command in all panes\n    panes:\n      - shell_command: # pane no. 1\n          - cd /var/log # run multiple commands in this pane\n          - ls -al | grep \\.log\n      - echo second pane # pane no. 2\n      - echo third pane # pane no. 3\n      - echo forth pane # pane no. 4\n```\n\nSave as _mysession.yaml_, and load:\n\n```sh\n$ tmuxp load ./mysession.yaml\n```\n\nProjects with _.tmuxp.yaml_ or _.tmuxp.json_ load via directory:\n\n```sh\n$ tmuxp load path/to/my/project/\n```\n\nLoad multiple at once (in bg, offer to attach last):\n\n```sh\n$ tmuxp load mysession ./another/project/\n```\n\nName a session:\n\n```bash\n$ tmuxp load -s session_name ./mysession.yaml\n```\n\n[simple](http://tmuxp.git-pull.com/examples.html#short-hand-inline) and\n[very\nelaborate](http://tmuxp.git-pull.com/examples.html#super-advanced-dev-environment)\nconfig examples\n\n# User-level configurations\n\ntmuxp checks for configs in user directories:\n\n- `$TMUXP_CONFIGDIR`, if set\n- `$XDG_CONFIG_HOME`, usually _$HOME/.config/tmuxp/_\n- `$HOME/.tmuxp/`\n\nLoad your tmuxp config from anywhere by using the filename, assuming\n_\\~/.config/tmuxp/mysession.yaml_ (or _.json_):\n\n```sh\n$ tmuxp load mysession\n```\n\nSee [author\'s tmuxp configs](https://github.com/tony/tmuxp-config) and\nthe projects\'\n[tmuxp.yaml](https://github.com/tmux-python/tmuxp/blob/master/.tmuxp.yaml).\n\n# Shell\n\n_New in 1.6.0_:\n\n`tmuxp shell` launches into a python console preloaded with the attached\nserver, session, and window in\n[libtmux](https://github.com/tmux-python/libtmux) objects.\n\n```shell\n$ tmuxp shell\n\n(Pdb) server\n<libtmux.server.Server object at 0x7f7dc8e69d10>\n(Pdb) server.sessions\n[Session($1 your_project)]\n(Pdb) session\nSession($1 your_project)\n(Pdb) session.name\n\'your_project\'\n(Pdb) window\nWindow(@3 1:your_window, Session($1 your_project))\n(Pdb) window.name\n\'your_window\'\n(Pdb) window.panes\n[Pane(%6 Window(@3 1:your_window, Session($1 your_project)))\n(Pdb) pane\nPane(%6 Window(@3 1:your_window, Session($1 your_project))\n```\n\nPython 3.7+ supports [PEP\n553](https://www.python.org/dev/peps/pep-0553/) `breakpoint()`\n(including `PYTHONBREAKPOINT`). Also supports direct commands via `-c`:\n\n```shell\n$ tmuxp shell -c \'print(window.name)\'\nmy_window\n\n$ tmuxp shell -c \'print(window.name.upper())\'\nMY_WINDOW\n```\n\nRead more on [tmuxp shell](https://tmuxp.git-pull.com/cli.html#shell) in\nthe CLI docs.\n\n# Pre-load hook\n\nRun custom startup scripts (such as installing project dependencies\nbefore loading tmux. See the\n[bootstrap_env.py](https://github.com/tmux-python/tmuxp/blob/master/bootstrap_env.py)\nand\n[before_script](http://tmuxp.git-pull.com/examples.html#bootstrap-project-before-launch)\nexample\n\n# Load in detached state\n\nYou can also load sessions in the background by passing `-d` flag\n\n# Screenshot\n\n<img src="https://raw.githubusercontent.com/tmux-python/tmuxp/master/docs/_static/tmuxp-demo.gif" class="align-center" style="width:45.0%" alt="image" />\n\n# Freeze a tmux session\n\nSnapshot your tmux layout, pane paths, and window/session names.\n\n```sh\n$ tmuxp freeze session-name\n```\n\nSee more about [freezing\ntmux](http://tmuxp.git-pull.com/cli.html#freeze-sessions) sessions.\n\n# Convert a session file\n\nConvert a session file from yaml to json and vice versa.\n\n```sh\n$ tmuxp convert filename\n```\n\nThis will prompt you for confirmation and shows you the new file that is\ngoing to be written.\n\nYou can auto confirm the prompt. In this case no preview will be shown.\n\n```sh\n$ tmuxp convert -y filename\n$ tmuxp convert --yes filename\n```\n\n# Plugin System\n\ntmuxp has a plugin system to allow for custom behavior. See more about\nthe [Plugin System](http://tmuxp.git-pull.com/plugin_system.html).\n\n# Debugging Helpers\n\nThe `load` command provides a way to log output to a log file for\ndebugging purposes.\n\n```sh\n$ tmuxp load --log-file <log-file-name> .\n```\n\nCollect system info to submit with a Github issue:\n\n```sh\n$ tmuxp debug-info\n------------------\nenvironment:\n    system: Linux\n    arch: x86_64\n\n# ... so on\n```\n\n# Docs / Reading material\n\nSee the [Quickstart](http://tmuxp.git-pull.com/quickstart.html).\n\n[Documentation](http://tmuxp.git-pull.com) homepage (also in\n[中文](http://tmuxp-zh.rtfd.org/))\n\nWant to learn more about tmux itself? [Read The Tao of Tmux\nonline](http://tmuxp.git-pull.com/about_tmux.html).\n\n# Donations\n\nYour donations fund development of new features, testing and support.\nYour money will go directly to maintenance and development of the\nproject. If you are an individual, feel free to give whatever feels\nright for the value you get out of the project.\n\nSee donation options at <https://git-pull.com/support.html>.\n\n# Project details\n\n- tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6\n- python support: >= 3.7, pypy, pypy3\n- Source: <https://github.com/tmux-python/tmuxp>\n- Docs: <https://tmuxp.git-pull.com>\n- API: <https://tmuxp.git-pull.com/api.html>\n- Changelog: <https://tmuxp.git-pull.com/history.html>\n- Issues: <https://github.com/tmux-python/tmuxp/issues>\n- Test Coverage: <https://codecov.io/gh/tmux-python/tmuxp>\n- pypi: <https://pypi.python.org/pypi/tmuxp>\n- Open Hub: <https://www.openhub.net/p/tmuxp-python>\n- License: [MIT](http://opensource.org/licenses/MIT).\n',
+    'author': 'Tony Narlock',
+    'author_email': 'tony@git-pull.com',
+    'maintainer': None,
+    'maintainer_email': None,
+    'url': 'http://github.com/tmux-python/tmuxp/',
+    'packages': packages,
+    'package_data': package_data,
+    'install_requires': install_requires,
+    'entry_points': entry_points,
+    'python_requires': '>=3.7,<4.0',
+}
 
 
+setup(**setup_kwargs)
```

