# Comparing `tmp/edx-repo-tools-0.7.1.tar.gz` & `tmp/edx-repo-tools-0.7.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "edx-repo-tools-0.7.1.tar", last modified: Fri May 13 10:28:39 2022, max compression
+gzip compressed data, was "edx-repo-tools-0.7.2.tar", last modified: Thu Apr  6 12:45:53 2023, max compression
```

## Comparing `edx-repo-tools-0.7.1.tar` & `edx-repo-tools-0.7.2.tar`

### file list

```diff
@@ -1,93 +1,100 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.707144 edx-repo-tools-0.7.1/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)      187 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2930 2022-05-13 10:28:39.707144 edx-repo-tools-0.7.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1955 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.695144 edx-repo-tools-0.7.1/edx_repo_tools/
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3022 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/add_common_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     6986 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/auth.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/codemods/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1049 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/auth_anonymous_update.py
--rw-r--r--   0 runner    (1001) docker     (121)     1718 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/foreignkey_on_delete_mod.py
--rw-r--r--   0 runner    (1001) docker     (121)     1498 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/widget_add_renderer_mod.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/
--rw-r--r--   0 runner    (1001) docker     (121)      304 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3125 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/add_new_django32_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     2001 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/github_actions_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     3830 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/github_actions_modernizer_django.py
--rw-r--r--   0 runner    (1001) docker     (121)     1067 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/remove_python2_unicode_compatible.py
--rw-r--r--   0 runner    (1001) docker     (121)     1372 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/replace_render_to_response.py
--rw-r--r--   0 runner    (1001) docker     (121)      500 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/replace_static.py
--rw-r--r--   0 runner    (1001) docker     (121)      814 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/replace_unicode_with_str.py
--rw-r--r--   0 runner    (1001) docker     (121)     2254 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/setup_file_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4132 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/tox_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4613 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/travis_modernizer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/
--rw-r--r--   0 runner    (1001) docker     (121)      135 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2913 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/gha_ci_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     2735 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/gha_release_workflow_modernizer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/conventional_commits/
--rw-r--r--   0 runner    (1001) docker     (121)     6773 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/conventional_commits/commitstats.py
--rw-r--r--   0 runner    (1001) docker     (121)     6716 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/data.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/dev/
--rw-r--r--   0 runner    (1001) docker     (121)       32 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/dev/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2162 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/dev/clone_org.py
--rw-r--r--   0 runner    (1001) docker     (121)     1459 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/dev/get_org_repo_urls.py
--rw-r--r--   0 runner    (1001) docker     (121)     1152 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/dev/show_hooks.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.699144 edx-repo-tools-0.7.1/edx_repo_tools/drip_survey/
--rw-r--r--   0 runner    (1001) docker     (121)      474 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/drip_survey/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1990 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/drip_survey/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/gitgraft/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/gitgraft/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22365 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/gitgraft/gitgraft.py
--rw-r--r--   0 runner    (1001) docker     (121)      977 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/modernize_openedx_yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/oep2/
--rw-r--r--   0 runner    (1001) docker     (121)      386 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      631 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_explicit.py
--rw-r--r--   0 runner    (1001) docker     (121)     6240 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_oep10.py
--rw-r--r--   0 runner    (1001) docker     (121)     1510 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_oep2.py
--rw-r--r--   0 runner    (1001) docker     (121)      915 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/explode_repos_yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1087 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)       78 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/oep2-report.ini
--rw-r--r--   0 runner    (1001) docker     (121)    10463 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/ospr/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/ospr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1549 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/ospr/no_yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/edx_repo_tools/release/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/release/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    27877 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/release/tag_release.py
--rw-r--r--   0 runner    (1001) docker     (121)     2430 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/edx_repo_tools/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.695144 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2930 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2877 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)     1600 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)       69 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-05-13 10:28:39.000000 edx-repo-tools-0.7.1/edx_repo_tools.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.703144 edx-repo-tools-0.7.1/requirements/
--rw-r--r--   0 runner    (1001) docker     (121)      429 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/requirements/base.in
--rw-r--r--   0 runner    (1001) docker     (121)       82 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/requirements/constraints.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-13 10:28:39.707144 edx-repo-tools-0.7.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     3493 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:39.707144 edx-repo-tools-0.7.1/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2367 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_actions_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     2765 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_actions_modernizer_django.py
--rw-r--r--   0 runner    (1001) docker     (121)     3229 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_add_new_django32_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     2447 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_gha_release_workflow_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)      904 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_modernize_openedx_yaml.py
--rw-r--r--   0 runner    (1001) docker     (121)     2153 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_node_ci_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     1249 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_remove_python2_unicode_compatible.py
--rw-r--r--   0 runner    (1001) docker     (121)     2073 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_replace_render_to_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     1505 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_setup_file_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)    16510 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_tag_release.py
--rw-r--r--   0 runner    (1001) docker     (121)     4131 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_tox_modernizer.py
--rw-r--r--   0 runner    (1001) docker     (121)     3517 2022-05-13 10:28:28.000000 edx-repo-tools-0.7.1/tests/test_travis_modernizer.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/
+-rw-r--r--   0 runner    (1001) docker     (122)    11358 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      187 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)      550 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/NOTICE.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     3151 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     2545 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.854612 edx-repo-tools-0.7.2/edx_repo_tools/
+-rw-r--r--   0 runner    (1001) docker     (122)       23 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3022 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/add_common_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7051 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/auth.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.854612 edx-repo-tools-0.7.2/edx_repo_tools/codemods/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1049 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/auth_anonymous_update.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1718 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/foreignkey_on_delete_mod.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1498 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/widget_add_renderer_mod.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/
+-rw-r--r--   0 runner    (1001) docker     (122)      304 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3125 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/add_new_django32_settings.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2001 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/github_actions_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3830 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/github_actions_modernizer_django.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1067 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/remove_python2_unicode_compatible.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1372 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/replace_render_to_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)      500 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/replace_static.py
+-rw-r--r--   0 runner    (1001) docker     (122)      814 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/replace_unicode_with_str.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2254 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/setup_file_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4132 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/tox_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4613 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/travis_modernizer.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/
+-rw-r--r--   0 runner    (1001) docker     (122)      135 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2913 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/gha_ci_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2735 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/gha_release_workflow_modernizer.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/conventional_commits/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/conventional_commits/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6830 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/conventional_commits/commitstats.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2134 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/data.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1709 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/dependabot_yml.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/dev/
+-rw-r--r--   0 runner    (1001) docker     (122)       32 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/dev/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2162 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/dev/clone_org.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1459 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/dev/get_org_repo_urls.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1167 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/dev/show_hooks.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/find_dependencies/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/find_dependencies/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10833 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/find_dependencies/find_dependencies.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/gitgraft/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/gitgraft/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    22365 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/gitgraft/gitgraft.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3902 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)      977 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/modernize_openedx_yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/oep2/
+-rw-r--r--   0 runner    (1001) docker     (122)      386 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      631 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_explicit.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6240 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_oep10.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1510 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_oep2.py
+-rw-r--r--   0 runner    (1001) docker     (122)      915 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/explode_repos_yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.858612 edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1087 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/cli.py
+-rw-r--r--   0 runner    (1001) docker     (122)       78 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/oep2-report.ini
+-rw-r--r--   0 runner    (1001) docker     (122)    10463 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/edx_repo_tools/ospr/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/ospr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1487 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/ospr/no_yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/edx_repo_tools/release/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/release/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    28778 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/release/tag_release.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/edx_repo_tools/repo_access_scraper/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/repo_access_scraper/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6613 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/repo_access_scraper/repo_access_scraper.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2479 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/edx_repo_tools/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.854612 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     3151 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     3123 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     1720 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     2186 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-06 12:45:53.000000 edx-repo-tools-0.7.2/edx_repo_tools.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/requirements/
+-rw-r--r--   0 runner    (1001) docker     (122)      429 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/requirements/base.in
+-rw-r--r--   0 runner    (1001) docker     (122)       26 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/requirements/constraints.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     4597 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:53.862612 edx-repo-tools-0.7.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2367 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_actions_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2765 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_actions_modernizer_django.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3229 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_add_new_django32_settings.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2447 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_gha_release_workflow_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)      904 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_modernize_openedx_yaml.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2153 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_node_ci_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1249 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_remove_python2_unicode_compatible.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2073 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_replace_render_to_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1505 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_setup_file_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16510 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_tag_release.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4131 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_tox_modernizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3517 2023-04-06 12:45:42.000000 edx-repo-tools-0.7.2/tests/test_travis_modernizer.py
```

### Comparing `edx-repo-tools-0.7.1/LICENSE.txt` & `edx-repo-tools-0.7.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/PKG-INFO` & `edx-repo-tools-0.7.2/README.rst`

 * *Files 26% similar despite different names*

```diff
@@ -1,79 +1,81 @@
-Metadata-Version: 1.1
-Name: edx-repo-tools
-Version: 0.7.1
-Summary: This repo contains a number of tools Open edX uses for working with GitHub repositories.
-Home-page: https://github.com/edx/repo-tools
-Author: edX
-Author-email: oscm@edx.org
-License: Apache
-Description: ###################
-        Open EdX Repo Tools
-        ###################
-        
-        This repo contains a number of tools Open edX uses for working with GitHub
-        repositories.
-        
-        * oep2: Report on `OEP-2`_ compliance across repositories.
-        * tag_release: Tags multiple repos as part of the release process.
-        
-        .. _OEP-2: https://open-edx-proposals.readthedocs.io/en/latest/oep-0002-bp-repo-metadata.html
-        
-        Setting up GitHub authentication
-        ================================
-        
-        Most of these make GitHub API calls, and so will need GitHub credentials in
-        order to not be severely rate-limited.  Edit (or create) `~/.netrc` so that it
-        has an entry like this::
-        
-            machine api.github.com
-              login your_user_name
-              password ddf9079e12042ac022c101c61c0235965851e209
-        
-        Change the login to your GitHub user name.  You'll get the password value from
-        https://github.com/settings/applications.  Visit that page, click on Developer
-        Settings and in the section called "Personal access tokens," click "Generate new token."  
-        It will prompt you for your password, then you'll see a scary list of scopes. Check 
-        the "repo" option and click "Generate token." Copy the password that
-        appears. Paste it into your ~/.netrc.
-        
-        
-        Working in the repo
-        ===================
-        
-        To work on these tools:
-        
-        1. Use a virtualenv.
-        
-        2. Install dependencies::
-           
-            make dev-install
-        
-        3. Run tests::
-           
-            make test
-        
-        4. Older tools were Python files run from the root of the repo.  Now we are
-           being more disciplined and putting code into importable modules with entry
-           points in setup.py.
-        
-        
-        Older Tools
-        ===========
-        
-        There are many programs in this repo in various stages of disrepair.  A few
-        of them are described in this repo's `older README.md`_ file.  Others are not
-        described at all, but may be useful, or have useful tidbits in the code.
-        
-        .. _older README.md: https://github.com/edx/repo-tools/blob/7aa8bda466d1925c56d4ad6e3b2bdd87b1f83148/README.md
-        
-        
-        Feedback
-        ========
-        
-        Please send any feedback to oscm@edx.org.
-        
-Keywords: edx repo tools
-Platform: UNKNOWN
-Classifier: Environment :: Console
-Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: Apache Software License
+###################
+Open edX Repo Tools
+###################
+
+This repo contains a number of tools Open edX engineers use for working with
+GitHub repositories.
+
+The set of tools has grown over the years. Some are old and in current use,
+some have fallen out of use, some are quite new.
+
+Setting up GitHub authentication
+================================
+
+Most of these make GitHub API calls, and so will need GitHub credentials in
+order to not be severely rate-limited.  Edit (or create) `~/.netrc` so that it
+has an entry like this::
+
+    machine api.github.com
+      login your_user_name
+      password ghp_XyzzyfGXFooBar8nBqQuuxY9brgXYz4Xyzzy
+
+Change the login to your GitHub user name.  The password is a Personal Access
+Token you get from https://github.com/settings/tokens.  Visit that page, click
+"Generate new token." It will prompt you for your password, then you'll see a
+scary list of scopes. Check the "repo" option and click "Generate token." Copy
+the token that appears. Paste it into your ~/.netrc in the "password" entry.
+
+
+Working in the repo
+===================
+
+To work on these tools:
+
+1. Use a virtualenv.
+
+2. Install dependencies::
+
+    make dev-install
+
+3. Run tests::
+
+    make test
+
+4. Older tools were Python files run from the root of the repo.  Now we are
+   being more disciplined and putting code into importable modules with entry
+   points in setup.py.
+
+5. Simple tools can go into an existing subdirectory of edx_repo_tools.  Follow
+   the structure of existing tools you find here.  More complex tools, or ones
+   that need unusual third-party requirements, should go into a new
+   subdirectory of edx_repo_tools.
+
+6. Add a new `entry_point` in setup.py for your command:
+
+   .. code::
+
+        entry_points={
+            'console_scripts': [
+                ...
+                'new_tool = edx_repo_tools.new_tool_dir.new_tool:main',
+                ...
+
+7. If your tool is in its own directory, you can create an `extra.in` file
+   there with third-party requirements intended just for your tool.  This will
+   automatically create an installable "extra" for your requirements.
+
+
+Older Tools
+===========
+
+There are many programs in this repo in various stages of disrepair.  A few
+of them are described in this repo's `older README.md`_ file.  Others are not
+described at all, but may be useful, or have useful tidbits in the code.
+
+.. _older README.md: https://github.com/openedx/repo-tools/blob/7aa8bda466d1925c56d4ad6e3b2bdd87b1f83148/README.md
+
+
+Feedback
+========
+
+Please send any feedback to oscm@edx.org.
```

### Comparing `edx-repo-tools-0.7.1/README.rst` & `edx-repo-tools-0.7.2/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,65 +1,102 @@
+Metadata-Version: 2.1
+Name: edx-repo-tools
+Version: 0.7.2
+Summary: This repo contains a number of tools Open edX uses for working with GitHub repositories.
+Home-page: https://github.com/openedx/repo-tools
+Author: edX
+Author-email: oscm@edx.org
+License: Apache
+Keywords: edx repo tools
+Platform: UNKNOWN
+Classifier: Environment :: Console
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: Apache Software License
+Provides-Extra: repo_access_scraper
+Provides-Extra: find_dependencies
+Provides-Extra: conventional_commits
+License-File: LICENSE.txt
+License-File: NOTICE.txt
+
 ###################
-Open EdX Repo Tools
+Open edX Repo Tools
 ###################
 
-This repo contains a number of tools Open edX uses for working with GitHub
-repositories.
-
-* oep2: Report on `OEP-2`_ compliance across repositories.
-* tag_release: Tags multiple repos as part of the release process.
+This repo contains a number of tools Open edX engineers use for working with
+GitHub repositories.
 
-.. _OEP-2: https://open-edx-proposals.readthedocs.io/en/latest/oep-0002-bp-repo-metadata.html
+The set of tools has grown over the years. Some are old and in current use,
+some have fallen out of use, some are quite new.
 
 Setting up GitHub authentication
 ================================
 
 Most of these make GitHub API calls, and so will need GitHub credentials in
 order to not be severely rate-limited.  Edit (or create) `~/.netrc` so that it
 has an entry like this::
 
     machine api.github.com
       login your_user_name
-      password ddf9079e12042ac022c101c61c0235965851e209
+      password ghp_XyzzyfGXFooBar8nBqQuuxY9brgXYz4Xyzzy
 
-Change the login to your GitHub user name.  You'll get the password value from
-https://github.com/settings/applications.  Visit that page, click on Developer
-Settings and in the section called "Personal access tokens," click "Generate new token."  
-It will prompt you for your password, then you'll see a scary list of scopes. Check 
-the "repo" option and click "Generate token." Copy the password that
-appears. Paste it into your ~/.netrc.
+Change the login to your GitHub user name.  The password is a Personal Access
+Token you get from https://github.com/settings/tokens.  Visit that page, click
+"Generate new token." It will prompt you for your password, then you'll see a
+scary list of scopes. Check the "repo" option and click "Generate token." Copy
+the token that appears. Paste it into your ~/.netrc in the "password" entry.
 
 
 Working in the repo
 ===================
 
 To work on these tools:
 
 1. Use a virtualenv.
 
 2. Install dependencies::
-   
+
     make dev-install
 
 3. Run tests::
-   
+
     make test
 
 4. Older tools were Python files run from the root of the repo.  Now we are
    being more disciplined and putting code into importable modules with entry
    points in setup.py.
 
+5. Simple tools can go into an existing subdirectory of edx_repo_tools.  Follow
+   the structure of existing tools you find here.  More complex tools, or ones
+   that need unusual third-party requirements, should go into a new
+   subdirectory of edx_repo_tools.
+
+6. Add a new `entry_point` in setup.py for your command:
+
+   .. code::
+
+        entry_points={
+            'console_scripts': [
+                ...
+                'new_tool = edx_repo_tools.new_tool_dir.new_tool:main',
+                ...
+
+7. If your tool is in its own directory, you can create an `extra.in` file
+   there with third-party requirements intended just for your tool.  This will
+   automatically create an installable "extra" for your requirements.
+
 
 Older Tools
 ===========
 
 There are many programs in this repo in various stages of disrepair.  A few
 of them are described in this repo's `older README.md`_ file.  Others are not
 described at all, but may be useful, or have useful tidbits in the code.
 
-.. _older README.md: https://github.com/edx/repo-tools/blob/7aa8bda466d1925c56d4ad6e3b2bdd87b1f83148/README.md
+.. _older README.md: https://github.com/openedx/repo-tools/blob/7aa8bda466d1925c56d4ad6e3b2bdd87b1f83148/README.md
 
 
 Feedback
 ========
 
 Please send any feedback to oscm@edx.org.
+
+
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/add_common_constraint.py` & `edx-repo-tools-0.7.2/edx_repo_tools/add_common_constraint.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/auth.py` & `edx-repo-tools-0.7.2/edx_repo_tools/auth.py`

 * *Files 3% similar despite different names*

```diff
@@ -191,19 +191,21 @@
         return f
     f._pass_github_applied = True
 
     # pylint: disable=missing-docstring
     @click.option(
         '--username',
         help='Specify the user to log in to GitHub with',
+        envvar="GITHUB_USERNAME",
     )
     @click.option('--password', help='Password to log in to GitHub with')
     @click.option(
         '--token',
         help='Personal access token to log in to GitHub with',
+        envvar="GITHUB_TOKEN",
     )
     @click.option(
         '--token-file',
         help='File containing personal access token to log in to GitHub with',
     )
     @click.option(
         '--debug/--no-debug',
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/auth_anonymous_update.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/auth_anonymous_update.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/foreignkey_on_delete_mod.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/foreignkey_on_delete_mod.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django2/widget_add_renderer_mod.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django2/widget_add_renderer_mod.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/add_new_django32_settings.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/add_new_django32_settings.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/github_actions_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/github_actions_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/github_actions_modernizer_django.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/github_actions_modernizer_django.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/remove_python2_unicode_compatible.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/remove_python2_unicode_compatible.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/replace_render_to_response.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/replace_render_to_response.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/replace_unicode_with_str.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/replace_unicode_with_str.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/setup_file_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/setup_file_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/tox_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/tox_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/django3/travis_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/django3/travis_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/gha_ci_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/gha_ci_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/codemods/node16/gha_release_workflow_modernizer.py` & `edx-repo-tools-0.7.2/edx_repo_tools/codemods/node16/gha_release_workflow_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/conventional_commits/commitstats.py` & `edx-repo-tools-0.7.2/edx_repo_tools/conventional_commits/commitstats.py`

 * *Files 1% similar despite different names*

```diff
@@ -115,14 +115,16 @@
 @click.option("--db", "dbfile", default="commits.db", help="SQLite database file to write to")
 @click.option("--ignore", multiple=True, help="Repos to ignore")
 @click.option("--require", help="A file that must exist to process the repo")
 @click.argument("repos", nargs=-1)
 def collect(dbfile, ignore, require, repos):
     db = dataset.connect("sqlite:///" + dbfile, sqlite_wal_mode=False)
     for repo in repos:
+        if not os.path.isdir(repo):
+            continue
         if any(fnmatch.fnmatch(repo, pat) for pat in ignore):
             print(f"Ignoring {repo}")
             continue
         if require is not None:
             if not os.path.exists(os.path.join(repo, require)):
                 print(f"Skipping {repo}")
                 continue
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/dev/clone_org.py` & `edx-repo-tools-0.7.2/edx_repo_tools/dev/clone_org.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/dev/get_org_repo_urls.py` & `edx-repo-tools-0.7.2/edx_repo_tools/dev/get_org_repo_urls.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/dev/show_hooks.py` & `edx-repo-tools-0.7.2/edx_repo_tools/dev/show_hooks.py`

 * *Files 10% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 import os.path
 import re
 
 import click
 from git.repo.base import Repo
 
 from edx_repo_tools.auth import pass_github
-from helpers import paginated_get
+from edx_repo_tools.helpers import paginated_get
 
 @click.command()
 @click.argument('org')
 @click.argument('pattern', required=False)
 @pass_github
 def main(hub, org, pattern=None):
     for repo in hub.organization(org).repositories():
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/gitgraft/gitgraft.py` & `edx-repo-tools-0.7.2/edx_repo_tools/gitgraft/gitgraft.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/modernize_openedx_yaml.py` & `edx-repo-tools-0.7.2/edx_repo_tools/modernize_openedx_yaml.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_explicit.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_explicit.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_oep10.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_oep10.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/checks/check_oep2.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/checks/check_oep2.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/explode_repos_yaml.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/explode_repos_yaml.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/cli.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/cli.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/oep2/report/plugin.py` & `edx-repo-tools-0.7.2/edx_repo_tools/oep2/report/plugin.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/ospr/no_yaml.py` & `edx-repo-tools-0.7.2/edx_repo_tools/ospr/no_yaml.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,27 +1,25 @@
 #!/usr/bin/env python
 """Find repos with no openedx.yaml file."""
 
-
 import itertools
 
 import click
 from github3.exceptions import NotFoundError
 
 from edx_repo_tools.auth import pass_github
-from edx_repo_tools.data import pass_repo_tools_data, iter_nonforks
+from edx_repo_tools.data import iter_nonforks
 from edx_repo_tools.utils import dry_echo, dry
 
 
 @click.command()
 @pass_github
-@pass_repo_tools_data
 @click.option('--org', multiple=True, default=['edx', 'edx-ops'])
 @dry
-def no_yaml(hub, repo_tools_data, org, dry):
+def no_yaml(hub, org, dry):
     """Find public repos with no openedx.yaml file."""
     repos = iter_nonforks(hub, org)
     repos = sorted(repos, reverse=True, key=lambda r: r.pushed_at)
     for repo in repos:
         if repo.private:
             continue
         if repo.archived:
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/release/tag_release.py` & `edx-repo-tools-0.7.2/edx_repo_tools/release/tag_release.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,17 +31,15 @@
 
 log = logging.getLogger(__name__)
 
 
 # Name used for fetching/storing GitHub OAuth tokens on disk
 TOKEN_NAME = "openedx-release"
 
-# We are in the process of migrating repos; in the future, we will have to
-# remove "edx" from the list of organizations.
-OPENEDX_ORGS = ['edx', 'openedx']
+OPENEDX_ORGS = ['openedx']
 
 
 # An object to act like a response (with a .text attribute) in the case that
 # create_ref uselessly returns us None on failure.
 FakeResponse = collections.namedtuple("FakeResponse", "text")
 
 
@@ -708,15 +706,39 @@
          "May be specified multiple times.",
 )
 @dry
 @pass_github
 def main(hub, ref, use_tag, override_ref, overrides, interactive, quiet,
          reverse, skip_invalid, input_repos, output_repos, included_repos,
          skip_repos, dry, orgs, branches):
-    """Create/remove tags & branches on GitHub repos for Open edX releases."""
+    """
+    Create/remove tags & branches on GitHub repos for Open edX releases.
+
+    Search GitHub repositories belonging to the Open edX organizations (`--org`)
+    that include an "openedx.yaml" file. For reference, see:
+
+    \b
+    https://open-edx-proposals.readthedocs.io/en/latest/processes/oep-0010-proc-openedx-releases.html#involving-repos-in-the-open-edx-build-process
+
+    The "openedx.yaml" file will be searched for in the branch indicated by
+    `--search-branch`, or in the default repo branch (typically "main" or
+    "master"). Once found, the chosen reference (`--tag` or `--branch`) will be
+    created in the branch indicated by `--override-ref/--override`, if present,
+    or the "ref" attribute from the "openedx.yaml" file.
+
+    For instance, to create a new release branch, run (in dry mode):
+
+        \b
+        tag_release --dry --branch open-release/zebulon.master
+
+    To create a new release tag in this branch, run:
+
+        \b
+        tag_release --dry --tag --search-branch=open-release/zebulon.master --override-ref=open-release/zebulon.master open-release/zebulon.1
+    """
     if input_repos:
         with open(input_repos) as f:
             repos = {
                 ShortRepository.from_dict(r["repo"], hub): r["data"]
                 for r in json.load(f)
             }
     else:
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools/utils.py` & `edx-repo-tools-0.7.2/edx_repo_tools/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -41,14 +41,15 @@
     )(f)
 
 
 class YamlLoader:
     def __init__(self, file_path):
         self.file_path = file_path
         self.yml_instance = YAML()
+        self.yml_instance.preserve_quotes = True
         self.yml_instance.default_flow_style = None
         self.yml_instance.indent(mapping=2, sequence=2, offset=0)
         self._load_file()
 
     def _load_file(self):
         with open(self.file_path) as file_stream:
             self.elements = self.yml_instance.load(file_stream)
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools.egg-info/SOURCES.txt` & `edx-repo-tools-0.7.2/edx_repo_tools.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -1,15 +1,18 @@
 LICENSE.txt
 MANIFEST.in
+NOTICE.txt
 README.rst
 setup.py
 edx_repo_tools/__init__.py
 edx_repo_tools/add_common_constraint.py
 edx_repo_tools/auth.py
 edx_repo_tools/data.py
+edx_repo_tools/dependabot_yml.py
+edx_repo_tools/helpers.py
 edx_repo_tools/modernize_openedx_yaml.py
 edx_repo_tools/utils.py
 edx_repo_tools.egg-info/PKG-INFO
 edx_repo_tools.egg-info/SOURCES.txt
 edx_repo_tools.egg-info/dependency_links.txt
 edx_repo_tools.egg-info/entry_points.txt
 edx_repo_tools.egg-info/requires.txt
@@ -29,21 +32,22 @@
 edx_repo_tools/codemods/django3/replace_unicode_with_str.py
 edx_repo_tools/codemods/django3/setup_file_modernizer.py
 edx_repo_tools/codemods/django3/tox_modernizer.py
 edx_repo_tools/codemods/django3/travis_modernizer.py
 edx_repo_tools/codemods/node16/__init__.py
 edx_repo_tools/codemods/node16/gha_ci_modernizer.py
 edx_repo_tools/codemods/node16/gha_release_workflow_modernizer.py
+edx_repo_tools/conventional_commits/__init__.py
 edx_repo_tools/conventional_commits/commitstats.py
 edx_repo_tools/dev/__init__.py
 edx_repo_tools/dev/clone_org.py
 edx_repo_tools/dev/get_org_repo_urls.py
 edx_repo_tools/dev/show_hooks.py
-edx_repo_tools/drip_survey/__init__.py
-edx_repo_tools/drip_survey/upload.py
+edx_repo_tools/find_dependencies/__init__.py
+edx_repo_tools/find_dependencies/find_dependencies.py
 edx_repo_tools/gitgraft/__init__.py
 edx_repo_tools/gitgraft/gitgraft.py
 edx_repo_tools/oep2/__init__.py
 edx_repo_tools/oep2/explode_repos_yaml.py
 edx_repo_tools/oep2/checks/__init__.py
 edx_repo_tools/oep2/checks/check_explicit.py
 edx_repo_tools/oep2/checks/check_oep10.py
@@ -52,14 +56,16 @@
 edx_repo_tools/oep2/report/cli.py
 edx_repo_tools/oep2/report/oep2-report.ini
 edx_repo_tools/oep2/report/plugin.py
 edx_repo_tools/ospr/__init__.py
 edx_repo_tools/ospr/no_yaml.py
 edx_repo_tools/release/__init__.py
 edx_repo_tools/release/tag_release.py
+edx_repo_tools/repo_access_scraper/__init__.py
+edx_repo_tools/repo_access_scraper/repo_access_scraper.py
 requirements/base.in
 requirements/constraints.txt
 tests/__init__.py
 tests/test_actions_modernizer.py
 tests/test_actions_modernizer_django.py
 tests/test_add_new_django32_settings.py
 tests/test_gha_release_workflow_modernizer.py
```

### Comparing `edx-repo-tools-0.7.1/edx_repo_tools.egg-info/entry_points.txt` & `edx-repo-tools-0.7.2/edx_repo_tools.egg-info/entry_points.txt`

 * *Files 23% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [console_scripts]
 add_common_constraint = edx_repo_tools.add_common_constraint:main
 add_django32_settings = edx_repo_tools.codemods.django3.add_new_django32_settings:main
 clone_org = edx_repo_tools.dev.clone_org:main
 conventional_commits = edx_repo_tools.conventional_commits.commitstats:main
-drip = edx_repo_tools.drip_survey:cli
+find_dependencies = edx_repo_tools.find_dependencies.find_dependencies:main
 get_org_repo_urls = edx_repo_tools.dev.get_org_repo_urls:main
 modernize_github_actions = edx_repo_tools.codemods.django3.github_actions_modernizer:main
 modernize_github_actions_django = edx_repo_tools.codemods.django3.github_actions_modernizer_django:main
 modernize_node_release_workflow = edx_repo_tools.codemods.node16.gha_release_workflow_modernizer:main
 modernize_node_workflow = edx_repo_tools.codemods.node16.gha_ci_modernizer:main
 modernize_openedx_yaml = edx_repo_tools.modernize_openedx_yaml:main
 modernize_setup_file = edx_repo_tools.codemods.django3.setup_file_modernizer:main
@@ -15,10 +15,11 @@
 modernize_travis = edx_repo_tools.codemods.django3.travis_modernizer:main
 no_yaml = edx_repo_tools.ospr.no_yaml:no_yaml
 oep2 = edx_repo_tools.oep2:_cli
 remove_python2_unicode_compatible = edx_repo_tools.codemods.django3.remove_python2_unicode_compatible:main
 replace_render_to_response = edx_repo_tools.codemods.django3.replace_render_to_response:main
 replace_static = edx_repo_tools.codemods.django3.replace_static:main
 replace_unicode_with_str = edx_repo_tools.codemods.django3.replace_unicode_with_str:main
+repo_access_scraper = edx_repo_tools.repo_access_scraper.repo_access_scraper:main
 show_hooks = edx_repo_tools.dev.show_hooks:main
 tag_release = edx_repo_tools.release.tag_release:main
```

### Comparing `edx-repo-tools-0.7.1/tests/test_actions_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_actions_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_actions_modernizer_django.py` & `edx-repo-tools-0.7.2/tests/test_actions_modernizer_django.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_add_new_django32_settings.py` & `edx-repo-tools-0.7.2/tests/test_add_new_django32_settings.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_gha_release_workflow_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_gha_release_workflow_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_modernize_openedx_yaml.py` & `edx-repo-tools-0.7.2/tests/test_modernize_openedx_yaml.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_node_ci_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_node_ci_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_remove_python2_unicode_compatible.py` & `edx-repo-tools-0.7.2/tests/test_remove_python2_unicode_compatible.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_replace_render_to_response.py` & `edx-repo-tools-0.7.2/tests/test_replace_render_to_response.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_setup_file_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_setup_file_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_tag_release.py` & `edx-repo-tools-0.7.2/tests/test_tag_release.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_tox_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_tox_modernizer.py`

 * *Files identical despite different names*

### Comparing `edx-repo-tools-0.7.1/tests/test_travis_modernizer.py` & `edx-repo-tools-0.7.2/tests/test_travis_modernizer.py`

 * *Files identical despite different names*

