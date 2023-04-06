# Comparing `tmp/chalkpy-1.9.8.tar.gz` & `tmp/chalkpy-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chalkpy-1.9.8.tar", last modified: Wed Nov 16 22:55:43 2022, max compression
+gzip compressed data, was "chalkpy-1.9.9.tar", last modified: Tue Nov 22 03:28:53 2022, max compression
```

## Comparing `chalkpy-1.9.8.tar` & `chalkpy-1.9.9.tar`

### file list

```diff
@@ -1,950 +1,953 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.776372 chalkpy-1.9.8/.github/
--rw-r--r--   0 runner    (1001) docker     (121)      109 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/CODEOWNERS
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (121)      425 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/ISSUE_TEMPLATE/bug_report.md
--rw-r--r--   0 runner    (1001) docker     (121)      250 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/ISSUE_TEMPLATE/feature_request.md
--rw-r--r--   0 runner    (1001) docker     (121)      200 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     2362 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/workflows/integration-tests.yml
--rw-r--r--   0 runner    (1001) docker     (121)      698 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/workflows/lint.yml
--rw-r--r--   0 runner    (1001) docker     (121)      753 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (121)      868 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.github/workflows/test.yml
--rw-r--r--   0 runner    (1001) docker     (121)      794 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)     1236 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      210 2022-11-16 22:55:28.000000 chalkpy-1.9.8/.pre-commit-hooks.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     7945 2022-11-16 22:55:43.832371 chalkpy-1.9.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7084 2022-11-16 22:55:28.000000 chalkpy-1.9.8/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      495 2022-11-16 22:55:28.000000 chalkpy-1.9.8/SECURITY.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/
--rw-r--r--   0 runner    (1001) docker     (121)     8248 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     3260 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/client/
--rw-r--r--   0 runner    (1001) docker     (121)     1041 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17134 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/client/client_impl.py
--rw-r--r--   0 runner    (1001) docker     (121)    14428 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/client/client_protocol.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/clogging/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/clogging/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      574 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/clogging/chalk_logger.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/config/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1906 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/config/auth_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     1840 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/config/project_config.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/df/
--rw-r--r--   0 runner    (1001) docker     (121)      133 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/df/ChalkDataFrameImpl.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/df/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6168 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/df/ast_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/
--rw-r--r--   0 runner    (1001) docker     (121)    14204 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1425 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/codegen.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_1/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_1/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_10/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_10/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      598 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_10/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_100/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_100/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5023 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_100/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_101/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_101/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5074 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_101/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_102/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_102/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5125 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_102/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_103/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_103/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5176 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_103/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_104/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_104/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5227 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_104/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_105/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_105/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5278 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_105/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_106/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_106/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5329 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_106/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_107/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_107/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5380 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_107/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.780372 chalkpy-1.9.8/chalk/feature_n/feature_108/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_108/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5431 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_108/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_109/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_109/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5482 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_109/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_11/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_11/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      629 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_11/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_110/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_110/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5533 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_110/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_111/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_111/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5584 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_111/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_112/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_112/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5635 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_112/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_113/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_113/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5686 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_113/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_114/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_114/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5737 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_114/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_115/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_115/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5788 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_115/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_116/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_116/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5839 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_116/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_117/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_117/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5890 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_117/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_118/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_118/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5941 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_118/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_119/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_119/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5992 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_119/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_12/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_12/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      660 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_12/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_120/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_120/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6043 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_120/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_121/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_121/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6094 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_121/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_122/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_122/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6145 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_122/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_123/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_123/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6196 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_123/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_124/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_124/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6247 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_124/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_125/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_125/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6298 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_125/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_126/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_126/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6349 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_126/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_127/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_127/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6400 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_127/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_128/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_128/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6451 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_128/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_129/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_129/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6502 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_129/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.784372 chalkpy-1.9.8/chalk/feature_n/feature_13/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_13/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      691 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_13/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_130/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_130/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6553 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_130/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_131/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_131/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6604 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_131/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_132/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_132/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6655 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_132/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_133/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_133/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6706 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_133/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_134/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_134/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6757 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_134/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_135/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_135/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6808 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_135/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_136/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_136/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6859 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_136/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_137/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_137/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6910 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_137/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_138/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_138/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6961 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_138/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_139/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_139/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7012 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_139/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_14/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_14/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      722 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_14/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_140/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_140/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7063 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_140/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_141/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_141/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7114 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_141/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_142/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_142/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7165 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_142/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_143/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_143/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7216 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_143/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_144/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_144/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7267 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_144/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_145/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_145/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7318 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_145/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_146/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_146/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7369 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_146/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_147/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_147/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7420 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_147/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_148/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_148/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7471 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_148/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_149/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_149/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7522 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_149/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_15/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_15/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      753 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_15/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_150/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_150/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7573 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_150/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_151/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_151/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7624 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_151/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.788372 chalkpy-1.9.8/chalk/feature_n/feature_152/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_152/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7675 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_152/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_153/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_153/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7726 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_153/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_154/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_154/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7777 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_154/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_155/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_155/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7828 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_155/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_156/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_156/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7879 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_156/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_157/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_157/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7930 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_157/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_158/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_158/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7981 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_158/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_159/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_159/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8032 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_159/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_16/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_16/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      790 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_16/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_160/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_160/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8083 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_160/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_161/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_161/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8134 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_161/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_162/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_162/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8185 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_162/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_163/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_163/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8236 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_163/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_164/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_164/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8287 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_164/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_165/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_165/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8338 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_165/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_166/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_166/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8389 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_166/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_167/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_167/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8440 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_167/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_168/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_168/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8491 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_168/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_169/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_169/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8542 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_169/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_17/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_17/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      821 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_17/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_170/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_170/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8593 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_170/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_171/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_171/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8644 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_171/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_172/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_172/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8695 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_172/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_173/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_173/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8746 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_173/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.792372 chalkpy-1.9.8/chalk/feature_n/feature_174/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_174/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8797 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_174/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_175/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_175/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8848 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_175/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_176/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_176/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8899 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_176/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_177/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_177/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8950 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_177/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_178/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_178/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9001 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_178/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_179/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_179/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9052 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_179/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_18/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_18/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      852 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_18/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_180/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_180/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9103 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_180/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_181/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_181/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9154 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_181/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_182/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_182/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9205 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_182/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_183/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_183/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9256 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_183/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_184/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_184/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9307 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_184/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_185/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_185/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9358 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_185/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_186/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_186/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9409 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_186/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_187/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_187/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9460 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_187/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_188/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_188/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9511 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_188/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_189/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_189/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9562 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_189/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_19/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_19/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      888 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_19/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_190/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_190/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9613 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_190/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_191/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_191/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9664 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_191/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_192/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_192/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9715 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_192/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_193/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_193/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9766 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_193/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_194/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_194/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9817 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_194/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_195/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_195/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9868 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_195/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.796372 chalkpy-1.9.8/chalk/feature_n/feature_196/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_196/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9919 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_196/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_197/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_197/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9970 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_197/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_198/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_198/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10021 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_198/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_199/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_199/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10072 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_199/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_2/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      378 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_2/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_20/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_20/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      919 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_20/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_200/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_200/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10123 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_200/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_201/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_201/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10174 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_201/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_202/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_202/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10225 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_202/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_203/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_203/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10276 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_203/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_204/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_204/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10327 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_204/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_205/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_205/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10378 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_205/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_206/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_206/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10429 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_206/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_207/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_207/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10480 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_207/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_208/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_208/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10531 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_208/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_209/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_209/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10582 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_209/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_21/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_21/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      950 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_21/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_210/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_210/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10633 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_210/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_211/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_211/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10684 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_211/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_212/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_212/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10735 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_212/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_213/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_213/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10786 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_213/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_214/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_214/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10837 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_214/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_215/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_215/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10888 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_215/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_216/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_216/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10939 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_216/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.800372 chalkpy-1.9.8/chalk/feature_n/feature_217/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_217/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10990 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_217/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_218/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_218/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11041 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_218/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_219/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_219/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11092 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_219/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_22/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_22/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      987 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_22/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_220/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_220/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11143 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_220/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_221/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_221/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11194 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_221/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_222/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_222/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11245 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_222/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_223/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_223/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11296 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_223/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_224/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_224/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11347 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_224/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_225/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_225/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11398 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_225/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_226/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_226/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11449 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_226/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_227/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_227/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11500 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_227/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_228/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_228/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11551 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_228/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_229/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_229/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11602 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_229/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_23/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_23/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1018 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_23/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_230/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_230/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11653 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_230/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_231/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_231/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11704 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_231/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_232/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_232/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11755 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_232/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_233/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_233/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11806 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_233/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_234/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_234/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11857 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_234/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_235/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_235/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11908 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_235/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_236/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_236/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11959 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_236/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_237/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_237/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12010 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_237/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_238/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_238/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12061 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_238/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.804371 chalkpy-1.9.8/chalk/feature_n/feature_239/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_239/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12112 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_239/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_24/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_24/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1077 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_24/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_240/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_240/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12163 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_240/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_241/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_241/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12214 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_241/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_242/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_242/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12265 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_242/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_243/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_243/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12316 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_243/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_244/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_244/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12367 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_244/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_245/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_245/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12418 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_245/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_246/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_246/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12469 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_246/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_247/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_247/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12520 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_247/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_248/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_248/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12571 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_248/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_249/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_249/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12622 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_249/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_25/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_25/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1494 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_25/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_250/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_250/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12673 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_250/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_251/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_251/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12724 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_251/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_252/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_252/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12775 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_252/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_253/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_253/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12826 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_253/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_254/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_254/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12877 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_254/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_255/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_255/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12928 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_255/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_256/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_256/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12979 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_256/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_26/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_26/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1541 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_26/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_27/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_27/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1588 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_27/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_28/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_28/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1635 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_28/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_29/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_29/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1682 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_29/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.808371 chalkpy-1.9.8/chalk/feature_n/feature_3/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      405 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_3/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_30/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_30/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1729 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_30/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_31/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_31/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1776 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_31/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_32/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_32/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1823 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_32/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_33/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_33/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1870 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_33/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_34/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_34/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1917 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_34/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_35/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_35/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1964 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_35/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_36/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_36/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2011 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_36/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_37/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_37/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2058 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_37/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_38/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_38/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2105 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_38/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_39/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_39/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2152 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_39/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_4/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_4/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      432 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_4/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_40/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_40/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2199 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_40/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_41/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_41/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2246 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_41/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_42/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_42/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2293 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_42/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_43/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_43/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2340 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_43/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_44/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_44/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2387 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_44/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_45/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_45/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2434 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_45/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_46/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_46/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2481 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_46/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_47/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_47/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_47/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_48/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_48/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2575 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_48/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_49/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_49/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2622 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_49/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_5/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_5/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      459 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_5/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_50/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_50/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2669 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_50/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_51/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_51/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2716 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_51/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.812372 chalkpy-1.9.8/chalk/feature_n/feature_52/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_52/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2763 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_52/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_53/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_53/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2810 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_53/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_54/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_54/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2857 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_54/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_55/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_55/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2904 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_55/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_56/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_56/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2951 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_56/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_57/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_57/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2998 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_57/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_58/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_58/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3045 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_58/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_59/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_59/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3092 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_59/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_6/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_6/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      486 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_6/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_60/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_60/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3139 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_60/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_61/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_61/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3186 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_61/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_62/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_62/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_62/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_63/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_63/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3280 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_63/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_64/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_64/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3327 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_64/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_65/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_65/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3374 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_65/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_66/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_66/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3421 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_66/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_67/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_67/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3468 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_67/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_68/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_68/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3515 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_68/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_69/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_69/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3562 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_69/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_7/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_7/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      513 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_7/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_70/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_70/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3609 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_70/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_71/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_71/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3656 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_71/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_72/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_72/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3703 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_72/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_73/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_73/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3750 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_73/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_74/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_74/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3797 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_74/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.816372 chalkpy-1.9.8/chalk/feature_n/feature_75/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_75/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3844 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_75/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_76/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_76/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3891 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_76/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_77/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_77/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3938 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_77/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_78/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_78/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3985 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_78/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_79/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_79/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4032 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_79/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_8/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_8/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      540 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_8/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_80/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_80/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4079 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_80/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_81/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_81/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4126 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_81/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_82/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_82/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4173 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_82/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_83/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_83/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4220 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_83/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_84/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_84/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4267 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_84/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_85/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_85/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4314 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_85/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_86/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_86/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4361 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_86/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_87/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_87/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4408 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_87/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_88/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_88/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4455 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_88/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_89/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_89/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4502 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_89/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_9/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_9/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_9/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_90/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_90/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4549 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_90/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_91/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_91/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4596 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_91/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_92/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_92/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4643 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_92/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_93/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_93/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4690 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_93/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_94/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_94/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4737 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_94/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_95/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_95/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4784 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_95/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_96/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_96/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4831 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_96/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.820371 chalkpy-1.9.8/chalk/feature_n/feature_97/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_97/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4878 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_97/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/feature_n/feature_98/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_98/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4925 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_98/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/feature_n/feature_99/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_99/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4972 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/feature_n/feature_99/feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/features/
--rw-r--r--   0 runner    (1001) docker     (121)     3535 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    42343 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/dataframe.py
--rw-r--r--   0 runner    (1001) docker     (121)    12984 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/feature_field.py
--rw-r--r--   0 runner    (1001) docker     (121)     5452 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/feature_set.py
--rw-r--r--   0 runner    (1001) docker     (121)    18559 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/feature_set_decorator.py
--rw-r--r--   0 runner    (1001) docker     (121)     5219 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/feature_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (121)     4755 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/filter.py
--rw-r--r--   0 runner    (1001) docker     (121)     2720 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/hooks.py
--rw-r--r--   0 runner    (1001) docker     (121)      920 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/pseudofeatures.py
--rw-r--r--   0 runner    (1001) docker     (121)    21193 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/resolver.py
--rw-r--r--   0 runner    (1001) docker     (121)      801 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/features/tag.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/gitignore/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/gitignore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7297 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/gitignore/gitignore_parser.py
--rw-r--r--   0 runner    (1001) docker     (121)     3519 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/importer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/integrations/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/integrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      580 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/integrations/named.py
--rw-r--r--   0 runner    (1001) docker     (121)    15643 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/mypy_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/parsed/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/parsed/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3426 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/parsed/duplicate_input_gql.py
--rw-r--r--   0 runner    (1001) docker     (121)     7795 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/parsed/json_conversions.py
--rw-r--r--   0 runner    (1001) docker     (121)     3564 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/parsed/user_types_to_json.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/serialization/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/serialization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11142 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/serialization/codec.py
--rw-r--r--   0 runner    (1001) docker     (121)     7813 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/serialization/parsed_annotation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/sql/
--rw-r--r--   0 runner    (1001) docker     (121)     5358 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/sql/base/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/base/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10395 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/base/protocols.py
--rw-r--r--   0 runner    (1001) docker     (121)     1305 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/base/session.py
--rw-r--r--   0 runner    (1001) docker     (121)     5668 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/base/sql_source.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/sql/integrations/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1919 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (121)     7907 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/chalk_query.py
--rw-r--r--   0 runner    (1001) docker     (121)     1554 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/cloudsql.py
--rw-r--r--   0 runner    (1001) docker     (121)     1630 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/mysql.py
--rw-r--r--   0 runner    (1001) docker     (121)     1822 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/postgres.py
--rw-r--r--   0 runner    (1001) docker     (121)     1166 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/redshift.py
--rw-r--r--   0 runner    (1001) docker     (121)     2314 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (121)     1112 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/sqlite.py
--rw-r--r--   0 runner    (1001) docker     (121)     5851 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/sql/integrations/string_chalk_query.py
--rw-r--r--   0 runner    (1001) docker     (121)      732 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/state.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.824371 chalkpy-1.9.8/chalk/streams/
--rw-r--r--   0 runner    (1001) docker     (121)      399 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      251 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/_file_source.py
--rw-r--r--   0 runner    (1001) docker     (121)      554 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/_kafka_source.py
--rw-r--r--   0 runner    (1001) docker     (121)     3026 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)     1424 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/_types.py
--rw-r--r--   0 runner    (1001) docker     (121)      758 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/streams/_windows.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/chalk/testing/
--rw-r--r--   0 runner    (1001) docker     (121)      500 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/testing/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/chalk/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      126 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/collection_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     3915 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/collections.py
--rw-r--r--   0 runner    (1001) docker     (121)     1208 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/duration.py
--rw-r--r--   0 runner    (1001) docker     (121)     1641 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/enum.py
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/environment_parsing.py
--rw-r--r--   0 runner    (1001) docker     (121)     6320 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/json_log_formatter.py
--rw-r--r--   0 runner    (1001) docker     (121)     4303 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/log_with_context.py
--rw-r--r--   0 runner    (1001) docker     (121)     2116 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/metaprogramming.py
--rw-r--r--   0 runner    (1001) docker     (121)      608 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/paths.py
--rw-r--r--   0 runner    (1001) docker     (121)     3355 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/sqlalchemy.py
--rw-r--r--   0 runner    (1001) docker     (121)      493 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/string.py
--rw-r--r--   0 runner    (1001) docker     (121)    13386 2022-11-16 22:55:28.000000 chalkpy-1.9.8/chalk/utils/stubgen.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/chalkpy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     7945 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    24114 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       42 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      574 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-11-16 22:55:43.000000 chalkpy-1.9.8/chalkpy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      360 2022-11-16 22:55:28.000000 chalkpy-1.9.8/mypy.ini
--rw-r--r--   0 runner    (1001) docker     (121)     2573 2022-11-16 22:55:28.000000 chalkpy-1.9.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      126 2022-11-16 22:55:28.000000 chalkpy-1.9.8/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (121)      269 2022-11-16 22:55:28.000000 chalkpy-1.9.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-16 22:55:43.832371 chalkpy-1.9.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2590 2022-11-16 22:55:28.000000 chalkpy-1.9.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/_gitignore/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/_gitignore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4908 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/_gitignore/test_gitignore_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/client/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1649 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/client/test_client_serialization.py
--rw-r--r--   0 runner    (1001) docker     (121)     1904 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/client/test_expand_features.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/features/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      974 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_chained_feature_time.py
--rw-r--r--   0 runner    (1001) docker     (121)      724 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_chained_has_one.py
--rw-r--r--   0 runner    (1001) docker     (121)     1612 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_custom_name.py
--rw-r--r--   0 runner    (1001) docker     (121)    17918 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_df.py
--rw-r--r--   0 runner    (1001) docker     (121)     5943 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_feature_discovery.py
--rw-r--r--   0 runner    (1001) docker     (121)     4976 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_features.py
--rw-r--r--   0 runner    (1001) docker     (121)     1170 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_hooks.py
--rw-r--r--   0 runner    (1001) docker     (121)     2878 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_id_assignment.py
--rw-r--r--   0 runner    (1001) docker     (121)      700 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_iter.py
--rw-r--r--   0 runner    (1001) docker     (121)      987 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_resolver_state.py
--rw-r--r--   0 runner    (1001) docker     (121)      915 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_resolvers_callable.py
--rw-r--r--   0 runner    (1001) docker     (121)     1981 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/features/test_ts_feature.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/mypy/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/mypy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      629 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/mypy/mypy_docs_demo.py
--rw-r--r--   0 runner    (1001) docker     (121)     1282 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/mypy/mypy_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      345 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/mypy/test_mypy_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/parsed/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/parsed/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      656 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/parsed/test_user_types_to_json.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.828371 chalkpy-1.9.8/tests/serialization/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/serialization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2650 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/serialization/test_codec.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/tests/sql/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1798 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/sql/test_implicit_mappings.py
--rw-r--r--   0 runner    (1001) docker     (121)     2800 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/sql/test_sql_features.py
--rw-r--r--   0 runner    (1001) docker     (121)      554 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/sql/test_table_ingest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/tests/streams/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/streams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      753 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/streams/test_stream.py
--rw-r--r--   0 runner    (1001) docker     (121)      531 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/streams/test_window.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/tests/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      857 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/test_collections.py
--rw-r--r--   0 runner    (1001) docker     (121)      829 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/test_enum.py
--rw-r--r--   0 runner    (1001) docker     (121)     4060 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/test_log_with_context.py
--rw-r--r--   0 runner    (1001) docker     (121)      742 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/test_stubgen.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.776372 chalkpy-1.9.8/tests/utils/typings/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.776372 chalkpy-1.9.8/tests/utils/typings/chalk/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/tests/utils/typings/chalk/features/
--rw-r--r--   0 runner    (1001) docker     (121)      775 2022-11-16 22:55:28.000000 chalkpy-1.9.8/tests/utils/typings/chalk/features/feature_set_decorator.pyi
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.776372 chalkpy-1.9.8/typings/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.776372 chalkpy-1.9.8/typings/chalk/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-16 22:55:43.832371 chalkpy-1.9.8/typings/chalk/features/
--rw-r--r--   0 runner    (1001) docker     (121)    48523 2022-11-16 22:55:28.000000 chalkpy-1.9.8/typings/chalk/features/feature_set_decorator.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.642167 chalkpy-1.9.9/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/.github/
+-rw-r--r--   0 runner    (1001) docker     (122)      109 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/CODEOWNERS
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (122)      425 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-r--r--   0 runner    (1001) docker     (122)      250 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/ISSUE_TEMPLATE/feature_request.md
+-rw-r--r--   0 runner    (1001) docker     (122)      200 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (122)     2362 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/workflows/integration-tests.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      861 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/workflows/lint.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      753 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/workflows/release.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      868 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.github/workflows/test.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      794 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (122)     1236 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      210 2022-11-22 03:28:40.000000 chalkpy-1.9.9/.pre-commit-hooks.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     7945 2022-11-22 03:28:53.642167 chalkpy-1.9.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     7084 2022-11-22 03:28:40.000000 chalkpy-1.9.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)      495 2022-11-22 03:28:40.000000 chalkpy-1.9.9/SECURITY.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/
+-rw-r--r--   0 runner    (1001) docker     (122)     8611 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)       22 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/_version.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3260 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/client/
+-rw-r--r--   0 runner    (1001) docker     (122)     1041 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17134 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/client/client_impl.py
+-rw-r--r--   0 runner    (1001) docker     (122)    14428 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/client/client_protocol.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/clogging/
+-rw-r--r--   0 runner    (1001) docker     (122)       81 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/clogging/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)       81 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/clogging/chalk_logger.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/config/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1906 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/config/auth_config.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1840 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/config/project_config.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/df/
+-rw-r--r--   0 runner    (1001) docker     (122)      133 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/df/ChalkDataFrameImpl.py
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/df/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6168 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/df/ast_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/
+-rw-r--r--   0 runner    (1001) docker     (122)    14204 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1425 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/codegen.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_1/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      351 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_1/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_10/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_10/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      598 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_10/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_100/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_100/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5023 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_100/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_101/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_101/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5074 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_101/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_102/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_102/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5125 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_102/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_103/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_103/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5176 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_103/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_104/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_104/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5227 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_104/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_105/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_105/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5278 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_105/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.590167 chalkpy-1.9.9/chalk/feature_n/feature_106/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_106/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5329 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_106/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_107/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_107/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5380 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_107/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_108/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_108/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5431 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_108/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_109/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_109/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5482 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_109/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_11/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_11/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      629 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_11/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_110/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_110/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5533 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_110/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_111/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_111/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5584 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_111/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_112/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_112/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5635 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_112/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_113/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_113/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5686 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_113/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_114/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_114/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5737 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_114/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_115/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_115/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5788 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_115/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_116/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_116/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5839 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_116/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_117/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_117/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5890 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_117/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_118/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_118/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5941 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_118/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_119/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_119/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5992 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_119/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_12/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_12/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      660 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_12/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_120/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_120/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6043 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_120/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_121/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_121/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6094 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_121/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_122/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_122/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6145 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_122/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_123/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_123/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6196 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_123/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_124/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_124/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6247 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_124/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_125/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_125/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6298 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_125/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_126/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_126/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6349 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_126/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_127/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_127/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6400 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_127/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_128/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_128/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6451 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_128/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.594167 chalkpy-1.9.9/chalk/feature_n/feature_129/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_129/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6502 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_129/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_13/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_13/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      691 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_13/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_130/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_130/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6553 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_130/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_131/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_131/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6604 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_131/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_132/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_132/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6655 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_132/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_133/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_133/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6706 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_133/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_134/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_134/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6757 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_134/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_135/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_135/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6808 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_135/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_136/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_136/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6859 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_136/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_137/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_137/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6910 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_137/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_138/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_138/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6961 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_138/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_139/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_139/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7012 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_139/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_14/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_14/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      722 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_14/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_140/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_140/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7063 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_140/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_141/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_141/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7114 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_141/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_142/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_142/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7165 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_142/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_143/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_143/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7216 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_143/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_144/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_144/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7267 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_144/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_145/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_145/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7318 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_145/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_146/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_146/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7369 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_146/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_147/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_147/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7420 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_147/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_148/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_148/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7471 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_148/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_149/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_149/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7522 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_149/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_15/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_15/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      753 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_15/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_150/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_150/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7573 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_150/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.598167 chalkpy-1.9.9/chalk/feature_n/feature_151/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_151/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7624 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_151/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_152/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_152/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7675 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_152/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_153/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_153/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7726 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_153/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_154/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_154/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7777 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_154/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_155/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_155/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7828 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_155/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_156/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_156/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7879 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_156/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_157/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_157/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7930 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_157/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_158/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_158/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7981 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_158/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_159/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_159/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8032 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_159/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_16/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_16/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      790 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_16/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_160/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_160/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8083 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_160/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_161/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_161/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8134 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_161/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_162/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_162/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8185 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_162/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_163/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_163/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8236 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_163/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_164/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_164/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8287 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_164/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_165/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_165/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8338 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_165/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_166/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_166/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8389 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_166/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_167/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_167/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8440 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_167/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_168/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_168/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8491 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_168/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_169/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_169/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8542 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_169/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_17/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_17/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      821 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_17/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_170/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_170/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8593 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_170/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_171/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_171/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8644 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_171/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_172/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_172/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8695 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_172/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.602167 chalkpy-1.9.9/chalk/feature_n/feature_173/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_173/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8746 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_173/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_174/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_174/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8797 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_174/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_175/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_175/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8848 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_175/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_176/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_176/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8899 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_176/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_177/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_177/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8950 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_177/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_178/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_178/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9001 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_178/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_179/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_179/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9052 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_179/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_18/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_18/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      852 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_18/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_180/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_180/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9103 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_180/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_181/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_181/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9154 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_181/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_182/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_182/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9205 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_182/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_183/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_183/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9256 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_183/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_184/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_184/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9307 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_184/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_185/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_185/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9358 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_185/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_186/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_186/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9409 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_186/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_187/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_187/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9460 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_187/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_188/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_188/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9511 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_188/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_189/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_189/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9562 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_189/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_19/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_19/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      888 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_19/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_190/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_190/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9613 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_190/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_191/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_191/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9664 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_191/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_192/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_192/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9715 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_192/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_193/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_193/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9766 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_193/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_194/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_194/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9817 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_194/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_195/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_195/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9868 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_195/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.606167 chalkpy-1.9.9/chalk/feature_n/feature_196/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_196/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9919 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_196/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_197/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_197/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9970 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_197/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_198/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_198/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10021 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_198/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_199/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_199/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10072 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_199/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_2/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      378 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_2/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_20/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_20/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      919 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_20/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_200/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_200/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10123 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_200/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_201/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_201/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10174 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_201/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_202/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_202/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10225 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_202/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_203/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_203/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10276 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_203/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_204/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_204/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10327 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_204/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_205/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_205/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10378 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_205/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_206/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_206/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10429 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_206/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_207/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_207/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10480 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_207/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_208/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_208/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10531 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_208/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_209/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_209/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10582 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_209/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_21/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_21/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      950 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_21/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_210/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_210/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10633 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_210/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_211/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_211/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10684 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_211/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_212/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_212/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10735 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_212/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_213/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_213/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10786 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_213/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_214/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_214/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10837 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_214/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_215/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_215/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10888 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_215/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_216/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_216/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10939 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_216/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_217/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_217/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10990 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_217/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.610167 chalkpy-1.9.9/chalk/feature_n/feature_218/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_218/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11041 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_218/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_219/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_219/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11092 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_219/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_22/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_22/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      987 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_22/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_220/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_220/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11143 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_220/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_221/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_221/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11194 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_221/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_222/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_222/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11245 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_222/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_223/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_223/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11296 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_223/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_224/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_224/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11347 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_224/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_225/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_225/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11398 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_225/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_226/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_226/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11449 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_226/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_227/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_227/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11500 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_227/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_228/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_228/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11551 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_228/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_229/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_229/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11602 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_229/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_23/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_23/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1018 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_23/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_230/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_230/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11653 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_230/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_231/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_231/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11704 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_231/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_232/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_232/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11755 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_232/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_233/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_233/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11806 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_233/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_234/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_234/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11857 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_234/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_235/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_235/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11908 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_235/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_236/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_236/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11959 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_236/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_237/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_237/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12010 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_237/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_238/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_238/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12061 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_238/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.614167 chalkpy-1.9.9/chalk/feature_n/feature_239/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_239/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12112 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_239/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_24/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_24/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1077 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_24/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_240/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_240/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12163 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_240/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_241/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_241/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12214 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_241/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_242/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_242/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12265 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_242/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_243/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_243/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12316 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_243/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_244/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_244/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12367 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_244/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_245/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_245/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12418 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_245/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_246/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_246/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12469 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_246/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_247/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_247/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12520 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_247/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_248/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_248/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12571 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_248/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_249/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_249/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12622 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_249/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_25/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_25/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1494 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_25/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_250/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_250/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12673 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_250/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_251/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_251/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12724 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_251/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_252/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_252/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12775 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_252/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_253/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_253/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12826 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_253/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_254/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_254/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12877 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_254/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_255/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_255/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12928 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_255/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_256/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_256/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12979 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_256/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_26/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_26/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1541 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_26/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_27/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_27/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1588 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_27/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_28/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_28/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1635 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_28/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_29/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_29/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1682 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_29/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_3/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      405 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_3/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.618167 chalkpy-1.9.9/chalk/feature_n/feature_30/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_30/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1729 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_30/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_31/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_31/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1776 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_31/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_32/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_32/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1823 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_32/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_33/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_33/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1870 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_33/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_34/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_34/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1917 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_34/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_35/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_35/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1964 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_35/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_36/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_36/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2011 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_36/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_37/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_37/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2058 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_37/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_38/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_38/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2105 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_38/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_39/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_39/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2152 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_39/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_4/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_4/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      432 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_4/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_40/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_40/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2199 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_40/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_41/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_41/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2246 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_41/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_42/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_42/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2293 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_42/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_43/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_43/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2340 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_43/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_44/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_44/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2387 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_44/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_45/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_45/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2434 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_45/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_46/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_46/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2481 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_46/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_47/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_47/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2528 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_47/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_48/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_48/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2575 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_48/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_49/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_49/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2622 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_49/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_5/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_5/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      459 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_5/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_50/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_50/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2669 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_50/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_51/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_51/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2716 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_51/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_52/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_52/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2763 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_52/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_53/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_53/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2810 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_53/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_54/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_54/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2857 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_54/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.622167 chalkpy-1.9.9/chalk/feature_n/feature_55/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_55/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2904 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_55/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_56/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_56/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2951 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_56/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_57/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_57/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2998 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_57/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_58/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_58/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3045 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_58/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_59/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_59/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3092 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_59/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_6/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_6/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      486 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_6/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_60/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_60/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3139 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_60/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_61/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_61/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3186 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_61/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_62/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_62/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3233 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_62/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_63/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_63/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3280 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_63/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_64/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_64/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3327 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_64/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_65/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_65/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3374 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_65/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_66/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_66/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3421 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_66/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_67/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_67/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3468 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_67/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_68/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_68/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3515 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_68/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_69/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_69/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3562 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_69/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_7/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_7/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      513 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_7/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_70/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_70/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3609 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_70/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_71/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_71/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3656 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_71/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_72/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_72/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3703 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_72/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_73/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_73/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3750 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_73/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_74/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_74/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3797 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_74/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_75/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_75/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3844 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_75/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_76/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_76/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3891 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_76/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_77/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_77/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3938 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_77/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_78/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_78/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3985 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_78/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.626167 chalkpy-1.9.9/chalk/feature_n/feature_79/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_79/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4032 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_79/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_8/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_8/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      540 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_8/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_80/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_80/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4079 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_80/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_81/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_81/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4126 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_81/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_82/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_82/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4173 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_82/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_83/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_83/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4220 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_83/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_84/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_84/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4267 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_84/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_85/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_85/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4314 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_85/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_86/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_86/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4361 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_86/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_87/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_87/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4408 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_87/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_88/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_88/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4455 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_88/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_89/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_89/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4502 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_89/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_9/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_9/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      567 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_9/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_90/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_90/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4549 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_90/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_91/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_91/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4596 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_91/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_92/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_92/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4643 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_92/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_93/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_93/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4690 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_93/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_94/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_94/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4737 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_94/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_95/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_95/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4784 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_95/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_96/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_96/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4831 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_96/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_97/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_97/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4878 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_97/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_98/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_98/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4925 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_98/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.630167 chalkpy-1.9.9/chalk/feature_n/feature_99/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_99/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4972 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/feature_n/feature_99/feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/features/
+-rw-r--r--   0 runner    (1001) docker     (122)     3535 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    42343 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/dataframe.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13124 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/feature_field.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5528 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/feature_set.py
+-rw-r--r--   0 runner    (1001) docker     (122)    18782 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/feature_set_decorator.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5219 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/feature_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4755 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/filter.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2720 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (122)      920 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/pseudofeatures.py
+-rw-r--r--   0 runner    (1001) docker     (122)    22171 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/resolver.py
+-rw-r--r--   0 runner    (1001) docker     (122)      801 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/features/tag.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/gitignore/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/gitignore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7297 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/gitignore/gitignore_parser.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3519 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/importer.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/integrations/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/integrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      580 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/integrations/named.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15643 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/mypy_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/parsed/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/parsed/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3443 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/parsed/duplicate_input_gql.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7805 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/parsed/json_conversions.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3574 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/parsed/user_types_to_json.py
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/serialization/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/serialization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11142 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/serialization/codec.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7813 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/serialization/parsed_annotation.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/sql/
+-rw-r--r--   0 runner    (1001) docker     (122)     5358 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/sql/base/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/base/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10395 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/base/protocols.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1305 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/base/session.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5668 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/base/sql_source.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/sql/integrations/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1919 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7907 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/chalk_query.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1554 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/cloudsql.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1630 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1822 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1166 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2314 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1112 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/sqlite.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5851 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/sql/integrations/string_chalk_query.py
+-rw-r--r--   0 runner    (1001) docker     (122)      732 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/state.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/streams/
+-rw-r--r--   0 runner    (1001) docker     (122)      502 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      226 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_file_source.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1536 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_internal.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1358 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_kafka_source.py
+-rw-r--r--   0 runner    (1001) docker     (122)      777 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_keyed_state.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5371 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_stream.py
+-rw-r--r--   0 runner    (1001) docker     (122)       94 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_types.py
+-rw-r--r--   0 runner    (1001) docker     (122)      758 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/streams/_windows.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.634167 chalkpy-1.9.9/chalk/testing/
+-rw-r--r--   0 runner    (1001) docker     (122)      500 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/testing/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/chalk/utils/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      126 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/collection_type.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3915 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/collections.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1476 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/duration.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1641 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/enum.py
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/environment_parsing.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6320 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/json_log_formatter.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4173 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/log_with_context.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2116 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/metaprogramming.py
+-rw-r--r--   0 runner    (1001) docker     (122)      608 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/paths.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3355 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/sqlalchemy.py
+-rw-r--r--   0 runner    (1001) docker     (122)      493 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/string.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13386 2022-11-22 03:28:40.000000 chalkpy-1.9.9/chalk/utils/stubgen.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/chalkpy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     7945 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    24200 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       42 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      574 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       12 2022-11-22 03:28:53.000000 chalkpy-1.9.9/chalkpy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      360 2022-11-22 03:28:40.000000 chalkpy-1.9.9/mypy.ini
+-rw-r--r--   0 runner    (1001) docker     (122)     2573 2022-11-22 03:28:40.000000 chalkpy-1.9.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)      126 2022-11-22 03:28:40.000000 chalkpy-1.9.9/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      269 2022-11-22 03:28:40.000000 chalkpy-1.9.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2022-11-22 03:28:53.642167 chalkpy-1.9.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     2591 2022-11-22 03:28:40.000000 chalkpy-1.9.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/_gitignore/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/_gitignore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4908 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/_gitignore/test_gitignore_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/client/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1649 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/client/test_client_serialization.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1904 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/client/test_expand_features.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/features/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      974 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_chained_feature_time.py
+-rw-r--r--   0 runner    (1001) docker     (122)      724 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_chained_has_one.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1612 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_custom_name.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17918 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_df.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6373 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_feature_discovery.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4976 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_features.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1170 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_hooks.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2878 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_id_assignment.py
+-rw-r--r--   0 runner    (1001) docker     (122)      700 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_iter.py
+-rw-r--r--   0 runner    (1001) docker     (122)      987 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_resolver_state.py
+-rw-r--r--   0 runner    (1001) docker     (122)      915 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_resolvers_callable.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1981 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/features/test_ts_feature.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/mypy/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/mypy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      629 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/mypy/mypy_docs_demo.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1282 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/mypy/mypy_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)      345 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/mypy/test_mypy_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/parsed/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/parsed/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      656 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/parsed/test_user_types_to_json.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/serialization/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/serialization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2650 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/serialization/test_codec.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/sql/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1798 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/sql/test_implicit_mappings.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2800 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/sql/test_sql_features.py
+-rw-r--r--   0 runner    (1001) docker     (122)      554 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/sql/test_table_ingest.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/streams/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/streams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      767 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/streams/test_stream.py
+-rw-r--r--   0 runner    (1001) docker     (122)      513 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/streams/test_window.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/utils/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      857 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/test_collections.py
+-rw-r--r--   0 runner    (1001) docker     (122)      504 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/test_duration.py
+-rw-r--r--   0 runner    (1001) docker     (122)      829 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/test_enum.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3788 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/test_log_with_context.py
+-rw-r--r--   0 runner    (1001) docker     (122)      775 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/test_stubgen.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.586166 chalkpy-1.9.9/tests/utils/typings/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.586166 chalkpy-1.9.9/tests/utils/typings/chalk/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/tests/utils/typings/chalk/features/
+-rw-r--r--   0 runner    (1001) docker     (122)      775 2022-11-22 03:28:40.000000 chalkpy-1.9.9/tests/utils/typings/chalk/features/feature_set_decorator.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.586166 chalkpy-1.9.9/typings/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.586166 chalkpy-1.9.9/typings/chalk/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-22 03:28:53.638167 chalkpy-1.9.9/typings/chalk/features/
+-rw-r--r--   0 runner    (1001) docker     (122)    48523 2022-11-22 03:28:40.000000 chalkpy-1.9.9/typings/chalk/features/feature_set_decorator.pyi
```

### Comparing `chalkpy-1.9.8/.github/workflows/integration-tests.yml` & `chalkpy-1.9.9/.github/workflows/integration-tests.yml`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/.github/workflows/lint.yml` & `chalkpy-1.9.9/.github/workflows/lint.yml`

 * *Files 20% similar despite different names*

```diff
@@ -19,14 +19,16 @@
     - name: Install dependencies
       run: pip install -r requirements.txt -r requirements-dev.txt
 
     - name: Run pre-commit
       run: pre-commit run --all-files
 
     - name: Fix lint errors if needed
-      if: failure()
-      uses: EndBug/add-and-commit@v9.1.0
-      with:
-        author_name: Linter
-        author_email: bot@chalk.ai
-        fetch: true
-        message: 'Chalk Bot: Fix linting errors'
+      if: ${{ failure() }}
+      run: |
+        git config --global user.name 'Linter'
+        git config --global user.email 'bot@chalk.ai'
+        git remote set-url origin https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/chalk-ai/chalk
+        git fetch --all
+        git checkout $GITHUB_HEAD_REF
+        git commit -am "Fix linting"
+        git push
```

### Comparing `chalkpy-1.9.8/.github/workflows/release.yml` & `chalkpy-1.9.9/.github/workflows/release.yml`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/.github/workflows/test.yml` & `chalkpy-1.9.9/.github/workflows/test.yml`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/.gitignore` & `chalkpy-1.9.9/.gitignore`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/.pre-commit-config.yaml` & `chalkpy-1.9.9/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/PKG-INFO` & `chalkpy-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chalkpy
-Version: 1.9.8
+Version: 1.9.9
 Summary: Python SDK for Chalk
 Home-page: https://chalk.ai
 Author: Chalk AI, Inc.
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
```

### Comparing `chalkpy-1.9.8/README.md` & `chalkpy-1.9.9/README.md`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/__init__.py` & `chalkpy-1.9.9/chalk/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -94,14 +94,16 @@
     caller_globals = caller_frame.frame.f_globals
     caller_locals = caller_frame.frame.f_locals
 
     def decorator(fn: Callable, cf: str = caller_filename):
         parsed = parse_function(fn, caller_globals, caller_locals)
         if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
             raise ValueError(f"Duplicate resolver {parsed.fqn}")
+        if parsed.output is None:
+            raise ValueError(f"Realtime resolvers must return features; '{parsed.fqn}' returns None")
 
         resolver = OnlineResolver(
             filename=cf,
             function_definition=parsed.function_definition,
             fqn=parsed.fqn,
             doc=parsed.doc,
             inputs=parsed.inputs,
@@ -112,16 +114,16 @@
             max_staleness=None,
             cron=cron,
             machine_type=machine_type,
             when=when,
             state=parsed.state,
             default_args=parsed.default_args,
         )
-
         Resolver.registry.append(resolver)
+        Resolver.hook and Resolver.hook(resolver)
 
         # Return the decorated resolver, which notably implements __call__() so it acts the same as
         # the underlying function if called directly, e.g. from test code
         return resolver
 
     return decorator(fn) if fn else decorator
 
@@ -193,31 +195,33 @@
     caller_frame = inspect.stack()[1]
     caller_filename = caller_frame.filename
     caller_globals = caller_frame.frame.f_globals
     caller_locals = caller_frame.frame.f_locals
 
     def decorator(args, cf=caller_filename):
         parsed = parse_function(args, caller_globals, caller_locals)
-        if parsed.fqn in {s.fqn for s in Resolver.registry}:
+        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
             raise ValueError(f"Duplicate resolver {parsed.fqn}")
-        Resolver.registry.append(
-            OfflineResolver(
-                filename=cf,
-                function_definition=parsed.function_definition,
-                fqn=parsed.fqn,
-                doc=parsed.doc,
-                inputs=parsed.inputs,
-                output=parsed.output,
-                fn=parsed.function,
-                environment=None if environment is None else list(ensure_tuple(environment)),
-                tags=None if tags is None else list(ensure_tuple(tags)),
-                max_staleness=None,
-                cron=cron,
-                machine_type=machine_type,
-                when=when,
-                state=parsed.state,
-                default_args=parsed.default_args,
-            )
+        if parsed.output is None:
+            raise ValueError(f"Batch resolvers must return features; '{parsed.fqn}' returns None")
+        resolver = OfflineResolver(
+            filename=cf,
+            function_definition=parsed.function_definition,
+            fqn=parsed.fqn,
+            doc=parsed.doc,
+            inputs=parsed.inputs,
+            output=parsed.output,
+            fn=parsed.function,
+            environment=None if environment is None else list(ensure_tuple(environment)),
+            tags=None if tags is None else list(ensure_tuple(tags)),
+            max_staleness=None,
+            cron=cron,
+            machine_type=machine_type,
+            when=when,
+            state=parsed.state,
+            default_args=parsed.default_args,
         )
+        Resolver.registry.append(resolver)
+        Resolver.hook and Resolver.hook(resolver)
         return args
 
     return decorator(fn) if fn else decorator
```

### Comparing `chalkpy-1.9.8/chalk/cli.py` & `chalkpy-1.9.9/chalk/cli.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/client/__init__.py` & `chalkpy-1.9.9/chalk/client/__init__.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/client/client_impl.py` & `chalkpy-1.9.9/chalk/client/client_impl.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/client/client_protocol.py` & `chalkpy-1.9.9/chalk/client/client_protocol.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/config/auth_config.py` & `chalkpy-1.9.9/chalk/config/auth_config.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/config/project_config.py` & `chalkpy-1.9.9/chalk/config/project_config.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/df/ast_parser.py` & `chalkpy-1.9.9/chalk/df/ast_parser.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/__init__.py` & `chalkpy-1.9.9/chalk/feature_n/__init__.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/codegen.py` & `chalkpy-1.9.9/chalk/feature_n/codegen.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_10/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_10/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_100/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_100/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_101/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_101/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_102/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_102/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_103/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_103/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_104/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_104/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_105/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_105/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_106/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_106/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_107/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_107/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_108/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_108/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_109/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_109/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_11/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_11/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_110/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_110/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_111/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_111/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_112/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_112/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_113/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_113/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_114/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_114/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_115/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_115/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_116/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_116/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_117/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_117/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_118/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_118/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_119/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_119/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_12/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_12/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_120/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_120/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_121/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_121/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_122/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_122/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_123/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_123/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_124/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_124/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_125/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_125/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_126/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_126/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_127/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_127/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_128/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_128/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_129/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_129/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_13/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_13/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_130/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_130/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_131/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_131/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_132/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_132/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_133/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_133/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_134/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_134/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_135/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_135/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_136/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_136/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_137/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_137/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_138/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_138/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_139/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_139/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_14/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_14/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_140/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_140/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_141/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_141/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_142/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_142/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_143/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_143/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_144/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_144/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_145/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_145/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_146/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_146/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_147/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_147/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_148/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_148/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_149/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_149/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_15/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_15/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_150/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_150/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_151/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_151/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_152/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_152/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_153/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_153/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_154/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_154/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_155/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_155/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_156/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_156/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_157/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_157/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_158/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_158/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_159/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_159/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_16/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_16/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_160/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_160/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_161/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_161/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_162/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_162/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_163/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_163/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_164/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_164/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_165/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_165/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_166/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_166/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_167/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_167/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_168/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_168/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_169/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_169/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_17/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_17/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_170/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_170/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_171/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_171/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_172/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_172/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_173/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_173/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_174/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_174/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_175/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_175/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_176/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_176/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_177/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_177/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_178/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_178/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_179/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_179/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_18/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_18/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_180/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_180/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_181/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_181/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_182/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_182/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_183/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_183/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_184/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_184/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_185/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_185/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_186/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_186/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_187/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_187/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_188/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_188/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_189/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_189/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_19/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_19/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_190/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_190/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_191/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_191/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_192/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_192/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_193/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_193/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_194/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_194/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_195/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_195/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_196/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_196/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_197/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_197/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_198/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_198/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_199/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_199/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_20/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_20/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_200/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_200/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_201/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_201/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_202/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_202/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_203/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_203/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_204/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_204/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_205/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_205/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_206/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_206/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_207/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_207/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_208/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_208/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_209/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_209/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_21/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_21/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_210/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_210/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_211/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_211/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_212/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_212/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_213/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_213/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_214/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_214/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_215/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_215/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_216/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_216/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_217/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_217/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_218/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_218/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_219/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_219/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_22/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_22/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_220/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_220/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_221/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_221/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_222/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_222/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_223/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_223/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_224/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_224/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_225/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_225/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_226/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_226/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_227/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_227/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_228/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_228/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_229/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_229/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_23/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_23/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_230/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_230/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_231/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_231/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_232/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_232/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_233/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_233/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_234/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_234/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_235/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_235/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_236/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_236/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_237/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_237/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_238/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_238/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_239/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_239/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_24/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_24/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_240/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_240/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_241/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_241/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_242/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_242/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_243/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_243/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_244/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_244/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_245/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_245/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_246/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_246/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_247/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_247/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_248/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_248/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_249/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_249/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_25/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_25/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_250/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_250/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_251/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_251/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_252/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_252/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_253/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_253/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_254/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_254/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_255/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_255/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_256/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_256/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_26/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_26/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_27/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_27/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_28/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_28/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_29/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_29/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_30/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_30/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_31/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_31/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_32/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_32/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_33/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_33/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_34/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_34/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_35/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_35/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_36/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_36/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_37/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_37/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_38/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_38/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_39/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_39/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_40/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_40/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_41/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_41/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_42/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_42/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_43/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_43/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_44/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_44/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_45/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_45/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_46/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_46/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_47/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_47/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_48/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_48/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_49/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_49/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_50/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_50/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_51/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_51/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_52/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_52/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_53/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_53/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_54/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_54/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_55/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_55/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_56/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_56/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_57/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_57/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_58/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_58/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_59/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_59/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_60/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_60/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_61/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_61/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_62/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_62/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_63/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_63/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_64/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_64/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_65/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_65/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_66/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_66/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_67/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_67/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_68/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_68/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_69/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_69/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_7/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_7/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_70/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_70/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_71/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_71/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_72/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_72/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_73/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_73/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_74/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_74/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_75/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_75/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_76/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_76/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_77/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_77/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_78/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_78/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_79/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_79/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_8/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_8/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_80/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_80/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_81/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_81/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_82/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_82/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_83/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_83/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_84/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_84/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_85/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_85/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_86/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_86/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_87/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_87/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_88/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_88/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_89/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_89/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_9/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_9/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_90/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_90/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_91/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_91/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_92/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_92/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_93/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_93/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_94/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_94/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_95/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_95/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_96/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_96/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_97/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_97/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_98/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_98/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/feature_n/feature_99/feature.py` & `chalkpy-1.9.9/chalk/feature_n/feature_99/feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/__init__.py` & `chalkpy-1.9.9/chalk/features/__init__.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/dataframe.py` & `chalkpy-1.9.9/chalk/features/dataframe.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/feature_field.py` & `chalkpy-1.9.9/chalk/features/feature_field.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 from __future__ import annotations
 
 import copy
 import dataclasses
 import functools
 import itertools
-from datetime import datetime
+from datetime import datetime, timedelta
 from typing import TYPE_CHECKING, Any, Callable, List, Optional, Tuple, Type, TypeVar, Union, cast
 
 import polars as pl
 from sqlalchemy.types import TypeEngine
 
 from chalk.features.tag import Tags
 from chalk.serialization.parsed_annotation import ParsedAnnotation
 from chalk.utils.collections import ensure_tuple
-from chalk.utils.duration import Duration
+from chalk.utils.duration import Duration, timedelta_to_duration
 
 if TYPE_CHECKING:
     from chalk.features.feature_set import Features
     from chalk.features.filter import Filter
 
 T = TypeVar("T")
 U = TypeVar("U")
@@ -341,15 +341,17 @@
         Feature(
             name=name,
             version=version,
             owner=owner,
             tags=None if tags is None else list(ensure_tuple(tags)),
             description=description,
             primary=primary,
-            max_staleness=max_staleness,
+            max_staleness=timedelta_to_duration(max_staleness)
+            if isinstance(max_staleness, timedelta)
+            else max_staleness,
             etl_offline_to_online=etl_offline_to_online,
             encoder=encoder,
             decoder=decoder,
             validations=FeatureValidation(
                 min=min,
                 max=max,
                 min_length=min_length,
```

### Comparing `chalkpy-1.9.8/chalk/features/feature_set.py` & `chalkpy-1.9.9/chalk/features/feature_set.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from __future__ import annotations
 
-from typing import Any, ClassVar, Dict, Iterator, List, Optional, Tuple, Type, cast
+from typing import Any, Callable, ClassVar, Dict, Iterator, List, Optional, Tuple, Type, cast
 
 from typing_extensions import TypeAlias, TypeGuard
 
 from chalk.features.feature_field import Feature
 from chalk.features.feature_wrapper import FeatureWrapper
 from chalk.utils.collections import ensure_tuple, get_unique_item
 from chalk.utils.duration import Duration
@@ -117,14 +117,15 @@
 
 
 class FeatureSetBase:
     """Registry containing all @features classes."""
 
     registry: Dict[str, Type[Features]] = {}  # mapping of fqn to Features cls
     root_fqn_to_feature: Dict[str, Feature] = {}  # mapping of root fqn to the Feature instance
+    hook: "ClassVar[Optional[Callable[[Features], None]]]" = None
 
     def __init__(self) -> None:
         raise RuntimeError("FeatureSetBase should never be instantiated")
 
 
 def is_features_cls(maybe_features: Any) -> TypeGuard[Type[Features]]:
     return isinstance(maybe_features, type) and issubclass(maybe_features, Features)
```

### Comparing `chalkpy-1.9.8/chalk/features/feature_set_decorator.py` & `chalkpy-1.9.9/chalk/features/feature_set_decorator.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import functools
 import inspect
 import re
 import sys
 import textwrap
 import threading
 import types
-from datetime import datetime
+from datetime import datetime, timedelta
 from typing import (
     Any,
     Callable,
     Dict,
     List,
     Mapping,
     MutableMapping,
@@ -25,15 +25,15 @@
 
 from chalk.features.feature_field import Feature, feature_time
 from chalk.features.feature_set import Features, FeatureSetBase
 from chalk.features.feature_wrapper import FeatureWrapper
 from chalk.features.tag import Tags
 from chalk.serialization.parsed_annotation import ParsedAnnotation
 from chalk.utils.collections import ensure_tuple
-from chalk.utils.duration import Duration
+from chalk.utils.duration import Duration, timedelta_to_duration
 from chalk.utils.metaprogramming import MISSING, create_fn, field_assign, set_new_attribute
 from chalk.utils.string import removeprefix, to_snake_case
 
 T = TypeVar("T")
 
 __all__ = ["features"]
 
@@ -82,15 +82,17 @@
         if name is not None and len(namespace) == 0:
             raise ValueError(f"Namespace cannot be an empty string, but is for the class '{c.__name__}'.")
         updated_class = _process_class(
             cls=c,
             owner=owner,
             tags=ensure_tuple(tags),
             etl_offline_to_online=etl_offline_to_online,
-            max_staleness=max_staleness,
+            max_staleness=timedelta_to_duration(max_staleness)
+            if isinstance(max_staleness, timedelta)
+            else max_staleness,
             namespace=namespace,
         )
         set_new_attribute(
             cls=updated_class,
             name="namespace",
             value=namespace,
         )
@@ -109,14 +111,15 @@
         timestamp_feature = _discover_feature(
             updated_class,
             "feature time",
             lambda f: f.is_feature_time,
         )
         set_new_attribute(cls=updated_class, name="__chalk_primary__", value=primary_feature)
         set_new_attribute(cls=updated_class, name="__chalk_ts__", value=timestamp_feature)
+        FeatureSetBase.hook and FeatureSetBase.hook(cast(Features, updated_class))
 
         return cast(Type[T], updated_class)
 
     # See if we're being called as @features or @features().
     if cls is None:
         # We're called with parens.
         return wrap
```

### Comparing `chalkpy-1.9.8/chalk/features/feature_wrapper.py` & `chalkpy-1.9.9/chalk/features/feature_wrapper.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/filter.py` & `chalkpy-1.9.9/chalk/features/filter.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/hooks.py` & `chalkpy-1.9.9/chalk/features/hooks.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/pseudofeatures.py` & `chalkpy-1.9.9/chalk/features/pseudofeatures.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/features/resolver.py` & `chalkpy-1.9.9/chalk/features/resolver.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 import dataclasses
 import inspect
 import textwrap
 from dataclasses import dataclass
 from typing import (
     Any,
     Callable,
+    ClassVar,
     Dict,
     Generic,
     List,
     Optional,
     Protocol,
     Sequence,
     Type,
@@ -17,28 +18,30 @@
     Union,
     get_args,
     get_origin,
     get_type_hints,
     overload,
 )
 
+from pydantic import BaseModel
 from typing_extensions import ParamSpec
 
 from chalk.df.ast_parser import convert_slice, eval_converted_expr
 from chalk.features.dataframe import DataFrame
 from chalk.features.feature_field import Feature
 from chalk.features.feature_set import Features
 from chalk.features.feature_wrapper import FeatureWrapper, unwrap_feature
 from chalk.features.filter import Filter
 from chalk.features.tag import Environments, Tags
 from chalk.sql.base.protocols import BaseSQLSourceProtocol
 from chalk.state import StateWrapper
 from chalk.utils.collection_type import GenericAlias
 from chalk.utils.collections import ensure_tuple
 from chalk.utils.duration import Duration, ScheduleOptions
+from chalk.utils.environment_parsing import env_var_bool
 
 MachineType = str
 T = TypeVar("T")
 P = ParamSpec("P")
 
 
 @dataclasses.dataclass(frozen=True)
@@ -92,15 +95,16 @@
     environment: Optional[List[str]]
     tags: Optional[List[str]]
     max_staleness: Optional[Duration]
     machine_type: Optional[MachineType]
     state: Optional[StateDescriptor]
     default_args: List[Optional[ResolverArgErrorHandler]]
 
-    registry: "List[Resolver]" = []
+    registry: "ClassVar[List[Resolver]]" = []
+    hook: "ClassVar[Optional[Callable[[Resolver], None]]]" = None
 
     def __hash__(self):
         return hash(self.fqn)
 
 
 def _process_call(result, *, declared_output: Any):
     from chalk.sql import StringChalkQuery
@@ -327,14 +331,50 @@
         return eval_converted_expr(annotation, self.glbs, self.lcls)
 
 
 def get_resolver_fqn(function: Callable):
     return f"{function.__module__}.{function.__name__}"
 
 
+def get_state_default_value(
+    state_typ: Type[Any],
+    declared_default: Any,
+    parameter_name_for_errors: str,
+    resolver_fqn_for_errors: str,
+) -> Any:
+    if not issubclass(state_typ, BaseModel) and not dataclasses.is_dataclass(state_typ):
+        raise ValueError(
+            f"State value must be a pydantic model or dataclass, "
+            f"but argument '{parameter_name_for_errors}' has type '{type(state_typ).__name__}'"
+        )
+
+    default = declared_default
+    if default is inspect.Signature.empty:
+        try:
+            default = state_typ()
+        except Exception as e:
+            cls_name = state_typ.__name__
+            raise ValueError(
+                (
+                    "State parameter must have a default value, or be able to be instantiated "
+                    f"with no arguments. For resolver '{resolver_fqn_for_errors}', no default found, and default "
+                    f"construction failed with '{str(e)}'. Assign a default in the resolver's "
+                    f"signature ({parameter_name_for_errors}: {cls_name} = {cls_name}(...)), or assign a default"
+                    f" to each of the fields of '{cls_name}'."
+                )
+            )
+
+    if not isinstance(default, state_typ):
+        raise ValueError(
+            f"Expected type '{state_typ.__name__}' for '{parameter_name_for_errors}', but default has type '{type(default).__name__}'"
+        )
+
+    return default
+
+
 def parse_function(
     fn: Callable,
     glbs: Optional[Dict[str, Any]],
     lcls: Optional[Dict[str, Any]],
     ignore_return: bool = False,
 ) -> ResolverParseResult:
     fqn = get_resolver_fqn(function=fn)
@@ -377,15 +417,14 @@
         raise ValueError(f"Resolver {fqn} did not have a valid return type")
 
     inputs = [annotation_parser.parse_annotation(p) for p in sig.parameters.keys()]
 
     # Unwrap anything that is wrapped with FeatureWrapper
     inputs = [unwrap_feature(p) if isinstance(p, FeatureWrapper) else p for p in inputs]
 
-    state_index = None
     state = None
     default_args: List[Optional[ResolverArgErrorHandler]] = [None for _ in range(len(inputs))]
 
     for i, (arg_name, parameter) in enumerate(sig.parameters.items()):
         bad_input = lambda: ValueError(
             f"Resolver inputs must be Features or State. Received {str(inputs[i])} for argument '{arg_name}'."
         )
@@ -410,53 +449,37 @@
         if not isinstance(arg, (StateWrapper, Feature)):
             raise bad_input()
 
         if not isinstance(arg, StateWrapper):
             continue
 
         typ = arg.typ
-
-        if not dataclasses.is_dataclass(typ):
-            raise ValueError(f"State value must be a dataclass. Argument '{arg_name}' has type '{type(typ).__name__}'")
-
         if state is not None:
             raise ValueError(
                 f"Only one state argument is allowed. Two provided to '{fqn}': '{state.kwarg}' and '{arg_name}'"
             )
 
-        default = parameter.default
-        if default is inspect.Signature.empty:
-            try:
-                default = typ()
-            except Exception as e:
-                cls_name = typ.__name__
-                raise ValueError(
-                    (
-                        "State parameter must have a default value, or be able to be instantiated "
-                        f"with no arguments. For resolver '{fqn}', no default found, and default "
-                        f"construction failed with '{str(e)}'. Assign a default in the resolver's "
-                        f"signature ({arg_name}: {cls_name} = {cls_name}(...)), or assign a default to each "
-                        f"of the fields of '{cls_name}'."
-                    )
-                )
-
-        if not isinstance(default, typ):
-            raise ValueError(
-                f"Expected type '{typ.__name__}' for '{arg_name}', but default has type '{type(default).__name__}'"
-            )
+        arg_name = parameter.name
+        arg = inputs[i]
 
-        state_index = i
         state = StateDescriptor(
             kwarg=arg_name,
             pos=i,
-            initial=default,
+            initial=get_state_default_value(
+                state_typ=arg.typ,
+                resolver_fqn_for_errors=fqn,
+                parameter_name_for_errors=arg_name,
+                declared_default=parameter.default,
+            ),
             typ=typ,
         )
+
     assert ret_val is None or issubclass(ret_val, Features)
 
+    state_index = state.pos if state is not None else None
     return ResolverParseResult(
         fqn=fqn,
         inputs=[v for i, v in enumerate(inputs) if i != state_index],
         output=ret_val,
         function_definition=function_definition,
         function=fn,
         doc=fn.__doc__,
@@ -498,18 +521,18 @@
     caller_frame = inspect.stack()[1]
     caller_filename = caller_frame.filename
     caller_globals = caller_frame.frame.f_globals
     caller_locals = caller_frame.frame.f_locals
 
     def decorator(fn: Callable[P, T], cf: str = caller_filename):
         parsed = parse_function(fn, caller_globals, caller_locals)
-        if parsed.fqn in {s.fqn for s in Resolver.registry}:
+        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
             raise ValueError(f"Duplicate resolver {parsed.fqn}")
         if parsed.output is None:
-            raise ValueError("Online resolvers must return features")
+            raise ValueError(f"Online resolvers must return features; '{parsed.fqn}' returns None")
 
         resolver = OnlineResolver(
             filename=cf,
             function_definition=parsed.function_definition,
             fqn=parsed.fqn,
             doc=parsed.doc,
             inputs=parsed.inputs,
@@ -522,14 +545,15 @@
             machine_type=machine_type,
             when=when,
             state=parsed.state,
             default_args=parsed.default_args,
         )
 
         Resolver.registry.append(resolver)
+        Resolver.hook and resolver.hook(resolver)
 
         # Return the decorated resolver, which notably implements __call__() so it acts the same as
         # the underlying function if called directly, e.g. from test code
         return resolver
 
     return decorator(fn) if fn else decorator
 
@@ -567,37 +591,37 @@
     caller_frame = inspect.stack()[1]
     caller_filename = caller_frame.filename
     caller_globals = caller_frame.frame.f_globals
     caller_locals = caller_frame.frame.f_locals
 
     def decorator(fn: Callable[P, T], cf: str = caller_filename):
         parsed = parse_function(fn, caller_globals, caller_locals)
-        if parsed.fqn in {s.fqn for s in Resolver.registry}:
+        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
             raise ValueError(f"Duplicate resolver {parsed.fqn}")
         if parsed.output is None:
-            raise ValueError("Offline resolvers must return features")
-        Resolver.registry.append(
-            OfflineResolver(
-                filename=cf,
-                function_definition=parsed.function_definition,
-                fqn=parsed.fqn,
-                doc=parsed.doc,
-                inputs=parsed.inputs,
-                output=parsed.output,
-                fn=parsed.function,
-                environment=None if environment is None else list(ensure_tuple(environment)),
-                tags=None if tags is None else list(ensure_tuple(tags)),
-                max_staleness=None,
-                cron=cron,
-                machine_type=machine_type,
-                state=parsed.state,
-                when=when,
-                default_args=parsed.default_args,
-            )
+            raise ValueError(f"Offline resolvers must return features; '{parsed.fqn}' returns None")
+        resolver = OfflineResolver(
+            filename=cf,
+            function_definition=parsed.function_definition,
+            fqn=parsed.fqn,
+            doc=parsed.doc,
+            inputs=parsed.inputs,
+            output=parsed.output,
+            fn=parsed.function,
+            environment=None if environment is None else list(ensure_tuple(environment)),
+            tags=None if tags is None else list(ensure_tuple(tags)),
+            max_staleness=None,
+            cron=cron,
+            machine_type=machine_type,
+            state=parsed.state,
+            when=when,
+            default_args=parsed.default_args,
         )
+        Resolver.registry.append(resolver)
+        Resolver.hook and resolver.hook(resolver)
         return fn
 
     return decorator(fn) if fn else decorator
 
 
 @overload
 def sink(
```

### Comparing `chalkpy-1.9.8/chalk/features/tag.py` & `chalkpy-1.9.9/chalk/features/tag.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/gitignore/gitignore_parser.py` & `chalkpy-1.9.9/chalk/gitignore/gitignore_parser.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/importer.py` & `chalkpy-1.9.9/chalk/importer.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/integrations/named.py` & `chalkpy-1.9.9/chalk/integrations/named.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/mypy_plugin.py` & `chalkpy-1.9.9/chalk/mypy_plugin.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/parsed/duplicate_input_gql.py` & `chalkpy-1.9.9/chalk/parsed/duplicate_input_gql.py`

 * *Files 1% similar despite different names*

```diff
@@ -91,15 +91,15 @@
 
 
 @dataclass
 class UpsertStreamResolverGQL:
     fqn: str
     kind: str
     functionDefinition: str
-    sourceClassName: str
+    sourceClassName: Optional[str] = None
     sourceConfig: Optional[Any] = None
     machineType: Optional[str] = None
     environment: Optional[List[str]] = None
     doc: Optional[str] = None
 
 
 @dataclass
```

### Comparing `chalkpy-1.9.8/chalk/parsed/json_conversions.py` & `chalkpy-1.9.9/chalk/parsed/json_conversions.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,15 +19,15 @@
     UpsertReferencePathComponentGQL,
     UpsertResolverGQL,
     UpsertResolverOutputGQL,
     UpsertScalarKindGQL,
     UpsertSinkResolverGQL,
     UpsertStreamResolverGQL,
 )
-from chalk.streams import StreamResolver
+from chalk.streams._internal import StreamResolver
 from chalk.utils import paths
 
 T = TypeVar("T")
 
 
 try:
     import attrs
```

### Comparing `chalkpy-1.9.8/chalk/parsed/user_types_to_json.py` & `chalkpy-1.9.9/chalk/parsed/user_types_to_json.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 
 from chalk._version import __version__
 from chalk.config.project_config import ValidationSettings, load_project_config
 from chalk.features import FeatureSetBase
 from chalk.features.resolver import Resolver, SinkResolver
 from chalk.importer import FailedImport
 from chalk.parsed.json_conversions import convert_type_to_gql
-from chalk.streams import StreamResolver
+from chalk.streams._internal import StreamResolver
 from chalk.utils import paths
 
 
 def _is_relative_to(x: Path, other: Path) -> bool:
     try:
         x.relative_to(other)
         return True
```

### Comparing `chalkpy-1.9.8/chalk/serialization/codec.py` & `chalkpy-1.9.9/chalk/serialization/codec.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/serialization/parsed_annotation.py` & `chalkpy-1.9.9/chalk/serialization/parsed_annotation.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/__init__.py` & `chalkpy-1.9.9/chalk/sql/__init__.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/base/protocols.py` & `chalkpy-1.9.9/chalk/sql/base/protocols.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/base/session.py` & `chalkpy-1.9.9/chalk/sql/base/session.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/base/sql_source.py` & `chalkpy-1.9.9/chalk/sql/base/sql_source.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/bigquery.py` & `chalkpy-1.9.9/chalk/sql/integrations/bigquery.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/chalk_query.py` & `chalkpy-1.9.9/chalk/sql/integrations/chalk_query.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/cloudsql.py` & `chalkpy-1.9.9/chalk/sql/integrations/cloudsql.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/mysql.py` & `chalkpy-1.9.9/chalk/sql/integrations/mysql.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/postgres.py` & `chalkpy-1.9.9/chalk/sql/integrations/postgres.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/redshift.py` & `chalkpy-1.9.9/chalk/sql/integrations/redshift.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/snowflake.py` & `chalkpy-1.9.9/chalk/sql/integrations/snowflake.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/sqlite.py` & `chalkpy-1.9.9/chalk/sql/integrations/sqlite.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/sql/integrations/string_chalk_query.py` & `chalkpy-1.9.9/chalk/sql/integrations/string_chalk_query.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/state.py` & `chalkpy-1.9.9/chalk/state.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/streams/_types.py` & `chalkpy-1.9.9/chalk/streams/_internal.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,54 +1,60 @@
-from typing import Any, Callable, List, Optional, Type, Union
+from typing import Any, Callable, List, Optional, Sequence, Set, Type, Union
 
 from pydantic import BaseModel
 
 from chalk import MachineType
-from chalk.features import Features
+from chalk.streams._types import StreamSource
 
 
-class StreamSource:
-    message_model: Union[Type[Any], None] = None
+class StreamResolverParam(BaseModel):
+    name: str
 
-    def config_to_json(self) -> Any:
-        ...
+
+class StreamResolverParamMessage(StreamResolverParam):
+    typ: Union[Type[str], Type[bytes], Type[BaseModel]]
+
+
+AnyDataclass = Any
+
+
+class StreamResolverParamKeyedState(StreamResolverParam):
+    typ: Union[Type[BaseModel], Type[AnyDataclass]]
+    default_value: Any
+
+
+class StreamResolverSignature(BaseModel):
+    params: Sequence[StreamResolverParam]
+    output_feature_fqns: Set[str]
 
 
 class StreamResolver:
     registry: "List[StreamResolver]" = []
 
     def __init__(
         self,
         function_definition: str,
         fqn: str,
         filename: str,
         doc: Optional[str],
         source: StreamSource,
         fn: Callable,
-        model: Union[BaseModel, None],
-        output_features: Type[Features],
+        signature: StreamResolverSignature,
         environment: Optional[Union[List[str], str]],
         machine_type: Optional[MachineType],
     ):
         super(StreamResolver, self).__init__()
         self.function_definition = function_definition
         self.fqn = fqn
         self.filename = filename
         self.source = source
         self.fn = fn
-        self.model = model
         self.environment = environment
         self.doc = doc
         self.machine_type = machine_type
-        self.output_features = output_features
-
-    def __eq__(self, other):
-        return isinstance(other, StreamResolver) and self.fqn == other.fqn
-
-    def __hash__(self):
-        return hash(self.fqn)
+        self.signature = signature
 
     def __call__(self, *args, **kwargs):
         return self.fn(*args, **kwargs)
 
     def __repr__(self):
         return f"StreamResolver(name={self.fqn})"
```

### Comparing `chalkpy-1.9.8/chalk/streams/_windows.py` & `chalkpy-1.9.9/chalk/streams/_windows.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/collections.py` & `chalkpy-1.9.9/chalk/utils/collections.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/duration.py` & `chalkpy-1.9.9/chalk/utils/duration.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+from datetime import timedelta
 from typing import Literal, Optional, Union
 
 # Duration is used to describe time periods in
 # natural langauge. To specify using natural
 # language, write the count of the unit you would
 # like, followed by the representation of the unit.
 #
@@ -18,22 +19,33 @@
 # | Signifier   | Meaning                           |
 # | ----------- | --------------------------------- |
 # | "10h"       | 10 hours                          |
 # | "1w 2m"     | 1 week and 2 minutes              |
 # | "1h 10m 2s" | 1 hour, 10 minutes, and 2 seconds |
 #
 # Read more at https://docs.chalk.ai/docs/duration
-Duration = str
+Duration = Union[str, timedelta]
 
 # A schedule defined using the unix-cron
 # string format (* * * * *).
 # Values are given in the order below:
 #
 # | Field        | Values |
 # | ------------ | ------ |
 # | Minute       | 0-59   |
 # | Hour         | 0-23   |
 # | Day of Month | 1-31   |
 # | Month        | 1-12   |
 # | Day of Week  | 0-6    |
 CronTab = str
 ScheduleOptions = Optional[Union[CronTab, Duration, Literal[True]]]
+
+
+def timedelta_to_duration(t: timedelta) -> Duration:
+    s = ""
+    if t.days > 0:
+        s += f"{t.days}d"
+    if t.seconds > 0:
+        if len(s) > 0:
+            s += " "
+        s += f"{t.seconds}s"
+    return s
```

### Comparing `chalkpy-1.9.8/chalk/utils/enum.py` & `chalkpy-1.9.9/chalk/utils/enum.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/json_log_formatter.py` & `chalkpy-1.9.9/chalk/utils/json_log_formatter.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/log_with_context.py` & `chalkpy-1.9.9/chalk/utils/log_with_context.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,50 +1,43 @@
 """
 Adds thread-local context to a Python logger. Taken from neocrym/log-with-context
 """
-import collections
+import contextvars
 import logging
-import os
-import threading
-from typing import Any, Callable, Mapping, Optional, Union
+from typing import Any, Callable, Dict, Optional, Union
 
-_EXTRA_TYPE = Mapping[str, Any]
+_EXTRA_TYPE = Dict[str, Any]
 
-_THREAD_LOCAL = threading.local()
-
-_THREAD_LOCAL.pids = collections.defaultdict(dict)
+_LOGGING_CONTEXT: contextvars.ContextVar[_EXTRA_TYPE] = contextvars.ContextVar("_LOGGING_CONTEXT")
 
 
 def init_extra():
     """Initialize our thread-local variable for storing contexts."""
-    if not hasattr(_THREAD_LOCAL, "pids"):
-        _THREAD_LOCAL.pids = collections.defaultdict(dict)
+    if _LOGGING_CONTEXT.get(None) is None:
+        _LOGGING_CONTEXT.set({})
 
 
 def get_extra() -> _EXTRA_TYPE:
     """
     Retrieve the thread-local extra.
     This initializes the thread-local variable if necessary.
     """
     init_extra()
-    pid = os.getpid()
-    return _THREAD_LOCAL.pids[pid]
+    return _LOGGING_CONTEXT.get()
 
 
 def set_extra(extra: _EXTRA_TYPE) -> _EXTRA_TYPE:
     """
     Sets the thread-local context to a new value.
     This erases whatever the context used to be. If you would rather
     restore that old value later, you might prefer using the
     :py:class:`add_logging_context` context manager.
     """
-    init_extra()
-    pid = os.getpid()
-    _THREAD_LOCAL.pids[pid] = extra
-    return _THREAD_LOCAL.pids[pid]
+    _LOGGING_CONTEXT.set(extra)
+    return extra
 
 
 class Logger:
     """
     Wrapper for a python :py:class:`logging.Logger`.
     This wrapper reads the current local context and emits
     them for each log message.
```

### Comparing `chalkpy-1.9.8/chalk/utils/metaprogramming.py` & `chalkpy-1.9.9/chalk/utils/metaprogramming.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/paths.py` & `chalkpy-1.9.9/chalk/utils/paths.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/sqlalchemy.py` & `chalkpy-1.9.9/chalk/utils/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalk/utils/stubgen.py` & `chalkpy-1.9.9/chalk/utils/stubgen.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/chalkpy.egg-info/PKG-INFO` & `chalkpy-1.9.9/chalkpy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chalkpy
-Version: 1.9.8
+Version: 1.9.9
 Summary: Python SDK for Chalk
 Home-page: https://chalk.ai
 Author: Chalk AI, Inc.
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
```

### Comparing `chalkpy-1.9.8/chalkpy.egg-info/SOURCES.txt` & `chalkpy-1.9.9/chalkpy.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -583,15 +583,17 @@
 chalk/sql/integrations/postgres.py
 chalk/sql/integrations/redshift.py
 chalk/sql/integrations/snowflake.py
 chalk/sql/integrations/sqlite.py
 chalk/sql/integrations/string_chalk_query.py
 chalk/streams/__init__.py
 chalk/streams/_file_source.py
+chalk/streams/_internal.py
 chalk/streams/_kafka_source.py
+chalk/streams/_keyed_state.py
 chalk/streams/_stream.py
 chalk/streams/_types.py
 chalk/streams/_windows.py
 chalk/testing/__init__.py
 chalk/utils/__init__.py
 chalk/utils/collection_type.py
 chalk/utils/collections.py
@@ -643,12 +645,13 @@
 tests/sql/test_sql_features.py
 tests/sql/test_table_ingest.py
 tests/streams/__init__.py
 tests/streams/test_stream.py
 tests/streams/test_window.py
 tests/utils/__init__.py
 tests/utils/test_collections.py
+tests/utils/test_duration.py
 tests/utils/test_enum.py
 tests/utils/test_log_with_context.py
 tests/utils/test_stubgen.py
 tests/utils/typings/chalk/features/feature_set_decorator.pyi
 typings/chalk/features/feature_set_decorator.pyi
```

### Comparing `chalkpy-1.9.8/chalkpy.egg-info/requires.txt` & `chalkpy-1.9.9/chalkpy.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/pyproject.toml` & `chalkpy-1.9.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/setup.py` & `chalkpy-1.9.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 
 def get_version() -> str:
     version_file = "chalk/_version.py"
     match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", read(version_file), re.M)
     assert match is not None, f"Unable to find version string in {version_file}"
     return match.group(1)
 
+
 if __name__ == "__main__":
     setup(
         version=get_version(),
         name="chalkpy",
         author="Chalk AI, Inc.",
         description="Python SDK for Chalk",
         long_description=read("README.md"),
```

### Comparing `chalkpy-1.9.8/tests/_gitignore/test_gitignore_parser.py` & `chalkpy-1.9.9/tests/_gitignore/test_gitignore_parser.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/client/test_client_serialization.py` & `chalkpy-1.9.9/tests/client/test_client_serialization.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/client/test_expand_features.py` & `chalkpy-1.9.9/tests/client/test_expand_features.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_chained_feature_time.py` & `chalkpy-1.9.9/tests/features/test_chained_feature_time.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_chained_has_one.py` & `chalkpy-1.9.9/tests/features/test_chained_has_one.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_custom_name.py` & `chalkpy-1.9.9/tests/features/test_custom_name.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_df.py` & `chalkpy-1.9.9/tests/features/test_df.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_feature_discovery.py` & `chalkpy-1.9.9/tests/features/test_feature_discovery.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from datetime import datetime
+from datetime import datetime, timedelta
 
 import pytest
 
 from chalk import description, is_primary, owner, tags
 from chalk.features import Features, feature, feature_time, features, unwrap_feature
 
 
@@ -82,14 +82,20 @@
 
 
 @features(max_staleness="4d")
 class MaxStalenessFeatures:
     id: int
     name: str = feature(max_staleness=None)
     woohoo: str = feature(max_staleness="30d")
+    boop: str = feature(max_staleness=timedelta(seconds=5))
+
+
+@features(max_staleness=timedelta(days=3, seconds=5))
+class MaxStalenessFeatures2:
+    id: int
 
 
 @features(etl_offline_to_online=True)
 class ETLFeatures:
     id: int
     name: str = feature(etl_offline_to_online=False)
     woohoo: str = feature(etl_offline_to_online=True)
@@ -103,20 +109,24 @@
     assert ETLFeatures.__chalk_etl_offline_to_online__ is True
     assert issubclass(MaxStalenessFeatures, Features)
     assert MaxStalenessFeatures.__chalk_etl_offline_to_online__ is None
 
 
 def test_class_max_staleness():
     assert unwrap_feature(MaxStalenessFeatures.id).max_staleness == "4d"
+    assert unwrap_feature(MaxStalenessFeatures.boop).max_staleness == "5s"
     assert unwrap_feature(MaxStalenessFeatures.name).max_staleness is None
     assert unwrap_feature(MaxStalenessFeatures.woohoo).max_staleness == "30d"
     assert issubclass(MaxStalenessFeatures, Features)
     assert MaxStalenessFeatures.__chalk_max_staleness__ == "4d"
     assert issubclass(ETLFeatures, Features)
     assert ETLFeatures.__chalk_max_staleness__ is None
+    assert MaxStalenessFeatures.__chalk_max_staleness__ == "4d"
+    assert ETLFeatures.__chalk_max_staleness__ is None
+    assert MaxStalenessFeatures2.__chalk_max_staleness__ == "3d 5s"
 
 
 def test_primary():
     assert is_primary(CommentBaseOwner.id)
     assert not is_primary(CommentBaseOwner.email)
```

### Comparing `chalkpy-1.9.8/tests/features/test_features.py` & `chalkpy-1.9.9/tests/features/test_features.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_hooks.py` & `chalkpy-1.9.9/tests/features/test_hooks.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_id_assignment.py` & `chalkpy-1.9.9/tests/features/test_id_assignment.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_iter.py` & `chalkpy-1.9.9/tests/features/test_iter.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_resolver_state.py` & `chalkpy-1.9.9/tests/features/test_resolver_state.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_resolvers_callable.py` & `chalkpy-1.9.9/tests/features/test_resolvers_callable.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/features/test_ts_feature.py` & `chalkpy-1.9.9/tests/features/test_ts_feature.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/mypy/mypy_docs_demo.py` & `chalkpy-1.9.9/tests/mypy/mypy_docs_demo.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/mypy/mypy_test.py` & `chalkpy-1.9.9/tests/mypy/mypy_test.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/parsed/test_user_types_to_json.py` & `chalkpy-1.9.9/tests/parsed/test_user_types_to_json.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/serialization/test_codec.py` & `chalkpy-1.9.9/tests/serialization/test_codec.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/sql/test_implicit_mappings.py` & `chalkpy-1.9.9/tests/sql/test_implicit_mappings.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/sql/test_sql_features.py` & `chalkpy-1.9.9/tests/sql/test_sql_features.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/sql/test_table_ingest.py` & `chalkpy-1.9.9/tests/sql/test_table_ingest.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/streams/test_stream.py` & `chalkpy-1.9.9/tests/streams/test_stream.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,39 +1,39 @@
 import dataclasses
 
 from pydantic import BaseModel
 
 from chalk import State
 from chalk.features import Features, features
-from chalk.streams import KafkaSource, stream
+from chalk.streams import KafkaSource, KeyedState, stream
 
 
 @features
 class StreamFeatures:
     scalar_feature: str
 
 
 class KafkaMessage(BaseModel):
     val_a: str
 
 
-s = KafkaSource(broker=[], topic=[], message_model=KafkaMessage)
+source = KafkaSource(bootstrap_server=[], topic=[])
 
 
 @dataclasses.dataclass
 class MyState:
     a: int = 4
 
 
-@stream(source=s)
-def fn(message: KafkaMessage, s: State[MyState]) -> Features[StreamFeatures.scalar_feature]:
+@stream(source=source)
+def fn(message: KafkaMessage, s: KeyedState[MyState]) -> Features[StreamFeatures.scalar_feature]:
     return StreamFeatures(
         scalar_feature=message.val_a,
     )
 
 
 def test_callable():
     assert fn(KafkaMessage(val_a="hello"), MyState()) == StreamFeatures(scalar_feature="hello")
 
 
 def test_parsed_source():
-    assert fn.source == s
+    assert fn.source == source
```

### Comparing `chalkpy-1.9.8/tests/streams/test_window.py` & `chalkpy-1.9.9/tests/streams/test_window.py`

 * *Files 15% similar despite different names*

```diff
@@ -11,15 +11,15 @@
     uid: str
 
 
 class KafkaMessage(BaseModel):
     val_a: str
 
 
-s = KafkaSource(broker=[], topic=[], message_model=KafkaMessage)
+s = KafkaSource(bootstrap_server=[], topic=[])
 
 
 @realtime
 def fn(x: StreamFeaturesWindow.scalar_feature) -> Features[StreamFeaturesWindow.uid]:
     pass
```

### Comparing `chalkpy-1.9.8/tests/utils/test_collections.py` & `chalkpy-1.9.9/tests/utils/test_collections.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/utils/test_enum.py` & `chalkpy-1.9.9/tests/utils/test_enum.py`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/tests/utils/test_log_with_context.py` & `chalkpy-1.9.9/tests/utils/test_log_with_context.py`

 * *Files 4% similar despite different names*

```diff
@@ -93,13 +93,7 @@
             with add_logging_context(val=val):
                 self.logger.debug("2")
                 self.base_logger.debug.assert_called_with("2", extra=dict(val=val), stacklevel=3)
 
         with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exc:
             with add_logging_context(a=1):
                 list(exc.map(thread_worker, [1, 2]))
-
-    def test_process_local(self):
-        """Test how our logger works with multiple processes."""
-        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exc:
-            with add_logging_context(a=1):
-                list(exc.map(process_worker, [1, 2]))
```

### Comparing `chalkpy-1.9.8/tests/utils/test_stubgen.py` & `chalkpy-1.9.9/tests/utils/test_stubgen.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,16 @@
 import os
 import subprocess
 
+import pytest
+
 import chalk
 
 
+@pytest.mark.skip
 def test_stubgen():
     """Test that the chalkpy stubgen runs and that the generated stub file is the one that is committed."""
     stub_file_path = os.path.join(
         os.path.dirname(chalk.__file__), "..", "typings", "chalk", "features", "feature_set_decorator.pyi"
     )
     with open(stub_file_path, "r") as f:
         current_stub_file = f.read()
```

### Comparing `chalkpy-1.9.8/tests/utils/typings/chalk/features/feature_set_decorator.pyi` & `chalkpy-1.9.9/tests/utils/typings/chalk/features/feature_set_decorator.pyi`

 * *Files identical despite different names*

### Comparing `chalkpy-1.9.8/typings/chalk/features/feature_set_decorator.pyi` & `chalkpy-1.9.9/typings/chalk/features/feature_set_decorator.pyi`

 * *Files identical despite different names*

