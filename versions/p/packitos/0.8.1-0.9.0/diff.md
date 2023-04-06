# Comparing `tmp/packitos-0.8.1.tar.gz` & `tmp/packitos-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/packitos-0.8.1.tar", last modified: Mon Jan 20 16:00:40 2020, max compression
+gzip compressed data, was "dist/packitos-0.9.0.tar", last modified: Wed Mar 25 14:57:50 2020, max compression
```

## Comparing `packitos-0.8.1.tar` & `packitos-0.9.0.tar`

### file list

```diff
@@ -1,314 +1,306 @@
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/.fmf/
--rw-r--r--   0 default  (1005350000) root         (0)        2 2020-01-16 12:08:42.000000 packitos-0.8.1/.fmf/version
--rw-r--r--   0 default  (1005350000) root         (0)       23 2020-01-16 12:08:42.000000 packitos-0.8.1/.git_archival.txt
--rw-r--r--   0 default  (1005350000) root         (0)       72 2020-01-16 12:08:42.000000 packitos-0.8.1/.gitattributes
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/.github/
--rw-r--r--   0 default  (1005350000) root         (0)      915 2020-01-16 12:08:42.000000 packitos-0.8.1/.github/stale.yml
--rw-r--r--   0 default  (1005350000) root         (0)       14 2020-01-16 12:08:42.000000 packitos-0.8.1/.gitignore
--rw-r--r--   0 default  (1005350000) root         (0)      835 2020-01-16 12:08:42.000000 packitos-0.8.1/.packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      991 2020-01-16 12:08:42.000000 packitos-0.8.1/.pre-commit-config.yaml
--rw-r--r--   0 default  (1005350000) root         (0)     2618 2020-01-16 12:08:42.000000 packitos-0.8.1/.zuul.yaml
--rw-r--r--   0 default  (1005350000) root         (0)    13235 2020-01-20 16:00:20.000000 packitos-0.8.1/CHANGELOG.md
--rw-r--r--   0 default  (1005350000) root         (0)     7276 2020-01-16 12:08:42.000000 packitos-0.8.1/CONTRIBUTING.md
--rw-r--r--   0 default  (1005350000) root         (0)     1421 2020-01-16 12:08:42.000000 packitos-0.8.1/DCO
--rw-r--r--   0 default  (1005350000) root         (0)      566 2020-01-16 12:08:42.000000 packitos-0.8.1/Dockerfile
--rw-r--r--   0 default  (1005350000) root         (0)      446 2020-01-16 12:08:42.000000 packitos-0.8.1/Dockerfile.tests
--rw-r--r--   0 default  (1005350000) root         (0)     1099 2020-01-16 12:08:42.000000 packitos-0.8.1/LICENSE
--rw-r--r--   0 default  (1005350000) root         (0)      842 2020-01-16 12:08:42.000000 packitos-0.8.1/Makefile
--rw-r--r--   0 default  (1005350000) root         (0)     6649 2020-01-20 16:00:40.000000 packitos-0.8.1/PKG-INFO
--rw-r--r--   0 default  (1005350000) root         (0)     4644 2020-01-16 12:08:42.000000 packitos-0.8.1/README.md
--rw-r--r--   0 default  (1005350000) root         (0)      695 2020-01-16 12:08:42.000000 packitos-0.8.1/Vagrantfile
--rw-r--r--   0 default  (1005350000) root         (0)       86 2020-01-16 12:08:42.000000 packitos-0.8.1/ansible.cfg
--rw-r--r--   0 default  (1005350000) root         (0)      751 2020-01-16 12:08:42.000000 packitos-0.8.1/ci.fmf
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/design/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/design/export/
--rw-r--r--   0 default  (1005350000) root         (0)     6148 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/.DS_Store
--rw-r--r--   0 default  (1005350000) root         (0)   132230 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-dark.png
--rw-r--r--   0 default  (1005350000) root         (0)    75002 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-extended.jpg
--rw-r--r--   0 default  (1005350000) root         (0)    48468 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-extended.png
--rw-r--r--   0 default  (1005350000) root         (0)    24881 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-extended.svg
--rw-r--r--   0 default  (1005350000) root         (0)   106567 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-guideline.pdf
--rw-r--r--   0 default  (1005350000) root         (0)    66141 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-no-borders.jpg
--rw-r--r--   0 default  (1005350000) root         (0)   143587 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-no-borders.png
--rw-r--r--   0 default  (1005350000) root         (0)    70268 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-square-small-borders.jpg
--rw-r--r--   0 default  (1005350000) root         (0)   150044 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-square-small-borders.png
--rw-r--r--   0 default  (1005350000) root         (0)    18005 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-text.jpg
--rw-r--r--   0 default  (1005350000) root         (0)    14198 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-text.png
--rw-r--r--   0 default  (1005350000) root         (0)    10016 2020-01-16 12:08:42.000000 packitos-0.8.1/design/export/logo-text.svg
--rw-r--r--   0 default  (1005350000) root         (0)   144552 2020-01-16 12:08:43.000000 packitos-0.8.1/design/export/logo-white.png
--rw-r--r--   0 default  (1005350000) root         (0)   158074 2020-01-16 12:08:43.000000 packitos-0.8.1/design/export/logo.png
--rw-r--r--   0 default  (1005350000) root         (0)    14697 2020-01-16 12:08:43.000000 packitos-0.8.1/design/export/logo.svg
--rw-r--r--   0 default  (1005350000) root         (0)  1843517 2020-01-16 12:08:43.000000 packitos-0.8.1/design/logo-packit.sketch
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/docs/
--rw-r--r--   0 default  (1005350000) root         (0)       92 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/01.md
--rw-r--r--   0 default  (1005350000) root         (0)       92 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/02.md
--rw-r--r--   0 default  (1005350000) root         (0)       93 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/ARCHITECTURE.md
--rw-r--r--   0 default  (1005350000) root         (0)       88 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/actions.md
--rw-r--r--   0 default  (1005350000) root         (0)       90 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/build.md
--rw-r--r--   0 default  (1005350000) root         (0)       94 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/configuration.md
--rw-r--r--   0 default  (1005350000) root         (0)      104 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/create_bodhi_update.md
--rw-r--r--   0 default  (1005350000) root         (0)       98 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/how-to-source-git.md
--rw-r--r--   0 default  (1005350000) root         (0)     4477 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/packit.dia
--rw-r--r--   0 default  (1005350000) root         (0)    55228 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/packit.png
--rw-r--r--   0 default  (1005350000) root         (0)       99 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/propose_update.md
--rw-r--r--   0 default  (1005350000) root         (0)    59456 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/source-git-best-practices.svg.png
--rw-r--r--   0 default  (1005350000) root         (0)       86 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/source-git.md
--rw-r--r--   0 default  (1005350000) root         (0)       89 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/srpm.md
--rw-r--r--   0 default  (1005350000) root         (0)      105 2020-01-16 12:08:43.000000 packitos-0.8.1/docs/sync-from-downstream.md
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/fedora-tests/
--rwxr-xr-x   0 default  (1005350000) root         (0)      157 2020-01-16 12:08:43.000000 packitos-0.8.1/fedora-tests/simple.py
--rw-r--r--   0 default  (1005350000) root         (0)      401 2020-01-16 12:08:43.000000 packitos-0.8.1/fedora-tests/tests.yml
--rwxr-xr-x   0 default  (1005350000) root         (0)      485 2020-01-16 12:08:43.000000 packitos-0.8.1/fedora-tests/upstream.sh
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/files/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/files/bash-completion/
--rwxr-xr-x   0 default  (1005350000) root         (0)      240 2020-01-20 15:55:16.000000 packitos-0.8.1/files/bash-completion/packit
--rw-r--r--   0 default  (1005350000) root         (0)      266 2020-01-16 12:08:43.000000 packitos-0.8.1/files/install-requirements.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      369 2020-01-16 12:08:43.000000 packitos-0.8.1/files/install-tests-requirements.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      313 2020-01-16 12:08:43.000000 packitos-0.8.1/files/packit-testing-farm-prepare-session-recording.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      269 2020-01-16 12:08:43.000000 packitos-0.8.1/files/packit-testing-farm-prepare.yaml
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/files/tasks/
--rw-r--r--   0 default  (1005350000) root         (0)      136 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/build-rpm-deps.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      179 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/configure-git.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      211 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/generic-dnf-requirements.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      102 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/install-packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      114 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/ogr-from-master.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      148 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/python-compile-deps.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      120 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/requre-master.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      232 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/rpm-test-deps.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      172 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/sandcastle-master.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      374 2020-01-16 12:08:43.000000 packitos-0.8.1/files/tasks/zuul-project-setup.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      262 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-install-requirements-git-master.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      366 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-install-requirements-pip.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      264 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-install-requirements-rpms.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      549 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-pre-commit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      442 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-tests-session-recording.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      429 2020-01-16 12:08:43.000000 packitos-0.8.1/files/zuul-tests.yaml
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/packit/
--rw-r--r--   0 default  (1005350000) root         (0)     1306 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     2338 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/actions.py
--rw-r--r--   0 default  (1005350000) root         (0)    27319 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/api.py
--rw-r--r--   0 default  (1005350000) root         (0)    17748 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/base_git.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/packit/cli/
--rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     4041 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/cli/build.py
--rw-r--r--   0 default  (1005350000) root         (0)     3260 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/copr_build.py
--rw-r--r--   0 default  (1005350000) root         (0)     3208 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/create_update.py
--rw-r--r--   0 default  (1005350000) root         (0)     3745 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/generate.py
--rw-r--r--   0 default  (1005350000) root         (0)     3347 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/packit_base.py
--rw-r--r--   0 default  (1005350000) root         (0)     2032 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/push_updates.py
--rw-r--r--   0 default  (1005350000) root         (0)     2671 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/srpm.py
--rw-r--r--   0 default  (1005350000) root         (0)     1973 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/status.py
--rw-r--r--   0 default  (1005350000) root         (0)     3642 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/sync_from_downstream.py
--rw-r--r--   0 default  (1005350000) root         (0)     3470 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/types.py
--rw-r--r--   0 default  (1005350000) root         (0)     4267 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/update.py
--rw-r--r--   0 default  (1005350000) root         (0)     6082 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/cli/utils.py
--rw-r--r--   0 default  (1005350000) root         (0)     3585 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/command_handler.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/packit/config/
--rw-r--r--   0 default  (1005350000) root         (0)      910 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/config/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     5382 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/config/aliases.py
--rw-r--r--   0 default  (1005350000) root         (0)     7997 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/config/config.py
--rw-r--r--   0 default  (1005350000) root         (0)     3295 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/config/job_config.py
--rw-r--r--   0 default  (1005350000) root         (0)    11373 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/config/package_config.py
--rw-r--r--   0 default  (1005350000) root         (0)     2531 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/config/sync_files_config.py
--rw-r--r--   0 default  (1005350000) root         (0)     3537 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/constants.py
--rw-r--r--   0 default  (1005350000) root         (0)     6803 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/copr_helper.py
--rw-r--r--   0 default  (1005350000) root         (0)    15137 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/distgit.py
--rw-r--r--   0 default  (1005350000) root         (0)     2732 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/downstream_checks.py
--rw-r--r--   0 default  (1005350000) root         (0)     2647 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/exceptions.py
--rw-r--r--   0 default  (1005350000) root         (0)     2176 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/fed_mes_consume.py
--rw-r--r--   0 default  (1005350000) root         (0)     4405 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/fedpkg.py
--rw-r--r--   0 default  (1005350000) root         (0)    15667 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/local_project.py
--rw-r--r--   0 default  (1005350000) root         (0)     9190 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/schema.py
--rw-r--r--   0 default  (1005350000) root         (0)     6834 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/security.py
--rw-r--r--   0 default  (1005350000) root         (0)     3726 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/specfile.py
--rw-r--r--   0 default  (1005350000) root         (0)     6806 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/status.py
--rw-r--r--   0 default  (1005350000) root         (0)     4472 2020-01-16 12:08:43.000000 packitos-0.8.1/packit/sync.py
--rw-r--r--   0 default  (1005350000) root         (0)    30180 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/upstream.py
--rw-r--r--   0 default  (1005350000) root         (0)    12276 2020-01-20 15:55:16.000000 packitos-0.8.1/packit/utils.py
--rw-r--r--   0 default  (1005350000) root         (0)     3859 2020-01-20 15:55:16.000000 packitos-0.8.1/packit.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/packitos.egg-info/
--rw-r--r--   0 default  (1005350000) root         (0)     6649 2020-01-20 16:00:35.000000 packitos-0.8.1/packitos.egg-info/PKG-INFO
--rw-r--r--   0 default  (1005350000) root         (0)     7951 2020-01-20 16:00:36.000000 packitos-0.8.1/packitos.egg-info/SOURCES.txt
--rw-r--r--   0 default  (1005350000) root         (0)        1 2020-01-20 16:00:35.000000 packitos-0.8.1/packitos.egg-info/dependency_links.txt
--rw-r--r--   0 default  (1005350000) root         (0)       63 2020-01-20 16:00:35.000000 packitos-0.8.1/packitos.egg-info/entry_points.txt
--rw-r--r--   0 default  (1005350000) root         (0)      197 2020-01-20 16:00:35.000000 packitos-0.8.1/packitos.egg-info/requires.txt
--rw-r--r--   0 default  (1005350000) root         (0)        7 2020-01-20 16:00:35.000000 packitos-0.8.1/packitos.egg-info/top_level.txt
--rw-r--r--   0 default  (1005350000) root         (0)       53 2020-01-16 12:08:43.000000 packitos-0.8.1/pytest.ini
--rw-r--r--   0 default  (1005350000) root         (0)      684 2020-01-16 12:08:43.000000 packitos-0.8.1/recipe-tests.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      158 2020-01-16 12:08:43.000000 packitos-0.8.1/release-conf.yaml
--rw-r--r--   0 default  (1005350000) root         (0)     1404 2020-01-20 16:00:40.000000 packitos-0.8.1/setup.cfg
--rw-r--r--   0 default  (1005350000) root         (0)     1191 2020-01-16 12:08:43.000000 packitos-0.8.1/setup.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/
--rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     4316 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/conftest.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/cockpit-ostree/
--rw-r--r--   0 default  (1005350000) root         (0)      948 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/cockpit-ostree/Makefile
--rw-r--r--   0 default  (1005350000) root         (0)      796 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/cockpit-ostree/cockpit-ostree.spec.dg
--rw-r--r--   0 default  (1005350000) root         (0)      804 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/cockpit-ostree/cockpit-ostree.spec.in
--rw-r--r--   0 default  (1005350000) root         (0)      315 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/cockpit-ostree/packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)      146 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/copr_config
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/dg-ogr/
--rw-r--r--   0 default  (1005350000) root         (0)      913 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dg-ogr/.packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)       37 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dg-ogr/README.md
--rw-r--r--   0 default  (1005350000) root         (0)       61 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dg-ogr/README.packit
--rw-r--r--   0 default  (1005350000) root         (0)     2295 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dg-ogr/python-ogr.spec
--rw-r--r--   0 default  (1005350000) root         (0)      157 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dg-ogr/sources
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/dist_git/
--rw-r--r--   0 default  (1005350000) root         (0)      222 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dist_git/.packit.json
--rw-r--r--   0 default  (1005350000) root         (0)      334 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/dist_git/beer.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/edd/
--rw-r--r--   0 default  (1005350000) root         (0)      167 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/.packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/LICENSE
--rw-r--r--   0 default  (1005350000) root         (0)     1348 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/Makefile
--rw-r--r--   0 default  (1005350000) root         (0)      192 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/README.rst
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/edd/docs/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/docs/man.rst
--rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/edd
--rw-r--r--   0 default  (1005350000) root         (0)     1422 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/edd/edd.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/empty_changelog/
--rw-r--r--   0 default  (1005350000) root         (0)      175 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/empty_changelog/.packit.json
--rw-r--r--   0 default  (1005350000) root         (0)      327 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/empty_changelog/beer.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/osbuild/
--rw-r--r--   0 default  (1005350000) root         (0)      233 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/osbuild/.packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)       10 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/osbuild/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     1462 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/osbuild/osbuild.spec
--rw-r--r--   0 default  (1005350000) root         (0)       65 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/osbuild/setup.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/osbuild/sources/
--rw-r--r--   0 default  (1005350000) root         (0)        5 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/osbuild/sources/test
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/snapd/
--rw-r--r--   0 default  (1005350000) root         (0)      395 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/.packit.yaml
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/tests/data/snapd/packaging/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/snapd/packaging/fedora/
--rwxr-xr-x   0 default  (1005350000) root         (0)      456 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/packaging/fedora/fix-spec
--rwxr-xr-x   0 default  (1005350000) root         (0)     1840 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/packaging/fedora/pack-source
--rw-r--r--   0 default  (1005350000) root         (0)    18386 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/packaging/fedora/snapd.spec
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/packaging/fedora/some-file-to-add
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/snapd/vendor/
--rw-r--r--   0 default  (1005350000) root         (0)     7279 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/snapd/vendor/vendor.json
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/tests/data/sourcegit/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/sourcegit/source_git/
--rw-r--r--   0 default  (1005350000) root         (0)      482 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/data/sourcegit/source_git/.packit.yaml
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/sourcegit/source_git/fedora/
--rw-r--r--   0 default  (1005350000) root         (0)      339 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sourcegit/source_git/fedora/beer.spec
--rw-r--r--   0 default  (1005350000) root         (0)       20 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/data/sourcegit/source_git/ignored_file.txt
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/sourcegit/upstream/
--rw-r--r--   0 default  (1005350000) root         (0)       45 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sourcegit/upstream/big-source-file.txt
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/tests/data/spec_not_in_root/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/spec_not_in_root/upstream/
--rw-r--r--   0 default  (1005350000) root         (0)      189 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/spec_not_in_root/upstream/.packit.json
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/spec_not_in_root/upstream/dir_with_spec/
--rw-r--r--   0 default  (1005350000) root         (0)      421 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/spec_not_in_root/upstream/dir_with_spec/beer.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/sync_files/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/a.md
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/b.md
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/c.txt
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/sync_files/example_dir/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/example_dir/d.md
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/example_dir/e.md
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/sync_files/example_dir/f.txt
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/upstream_git/
--rw-r--r--   0 default  (1005350000) root         (0)      175 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/upstream_git/.packit.json
--rw-r--r--   0 default  (1005350000) root         (0)      421 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/upstream_git/beer.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:39.000000 packitos-0.8.1/tests/data/upstream_git_with_multiple_sources/
--rw-r--r--   0 default  (1005350000) root         (0)      175 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/upstream_git_with_multiple_sources/.packit.json
--rw-r--r--   0 default  (1005350000) root         (0)      513 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/data/upstream_git_with_multiple_sources/beer.spec
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/data/vsftpd/
--rw-r--r--   0 default  (1005350000) root         (0)      218 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/.packit.yaml
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/AUDIT
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/BENCHMARKS
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/BUGS
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/COPYING
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Changelog
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/data/vsftpd/EXAMPLE/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/EXAMPLE/example
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/FAQ
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/
--rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd-generator
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.ftpusers
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.pam
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.service
--rw-r--r--   0 default  (1005350000) root         (0)    27817 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.spec
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.target
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.user_list
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.xinetd
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd@.service
--rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd_conf_migrate.sh
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/INSTALL
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/LICENSE
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/README
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/README.security
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/REWARD
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/data/vsftpd/RedHat/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/RedHat/vsftpd.log
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/data/vsftpd/SECURITY/
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/SECURITY/security
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/SIZE
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/SPEED
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/TODO
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/TUNING
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/vsftpd.8
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/vsftpd.conf
--rw-r--r--   0 default  (1005350000) root         (0)        0 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/data/vsftpd/vsftpd.conf.5
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/functional/
--rw-r--r--   0 default  (1005350000) root         (0)       19 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/functional/README.md
--rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/functional/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)      509 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/functional/spellbook.py
--rw-r--r--   0 default  (1005350000) root         (0)     3977 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/functional/test_srpm.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/integration/
--rw-r--r--   0 default  (1005350000) root         (0)       38 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/README.md
--rw-r--r--   0 default  (1005350000) root         (0)       99 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     2433 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/bodhi_latest_builds.py
--rw-r--r--   0 default  (1005350000) root         (0)    43175 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/bodhi_status_updates.py
--rw-r--r--   0 default  (1005350000) root         (0)    11604 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/integration/conftest.py
--rw-r--r--   0 default  (1005350000) root         (0)     3023 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_actions.py
--rw-r--r--   0 default  (1005350000) root         (0)     1605 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_api.py
--rw-r--r--   0 default  (1005350000) root         (0)     3567 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_base_git.py
--rw-r--r--   0 default  (1005350000) root         (0)     2689 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/integration/test_build.py
--rw-r--r--   0 default  (1005350000) root         (0)     4104 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_copr_build.py
--rw-r--r--   0 default  (1005350000) root         (0)    12447 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_create_update.py
--rw-r--r--   0 default  (1005350000) root         (0)     1479 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_distgit.py
--rw-r--r--   0 default  (1005350000) root         (0)      682 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_generate.py
--rw-r--r--   0 default  (1005350000) root         (0)     4832 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_get_api.py
--rw-r--r--   0 default  (1005350000) root         (0)     2472 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_pagure.py
--rw-r--r--   0 default  (1005350000) root         (0)    18568 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_push_updates.py
--rw-r--r--   0 default  (1005350000) root         (0)     3186 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_security.py
--rw-r--r--   0 default  (1005350000) root         (0)     6188 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/integration/test_source_git.py
--rw-r--r--   0 default  (1005350000) root         (0)     1646 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_spec.py
--rw-r--r--   0 default  (1005350000) root         (0)     3829 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_sync_files.py
--rw-r--r--   0 default  (1005350000) root         (0)     5177 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/integration/test_update.py
--rw-r--r--   0 default  (1005350000) root         (0)     6875 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_upstream.py
--rw-r--r--   0 default  (1005350000) root         (0)     3603 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_using_cockpit.py
--rw-r--r--   0 default  (1005350000) root         (0)     2352 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/test_using_examples.py
--rw-r--r--   0 default  (1005350000) root         (0)     1323 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/integration/utils.py
--rw-r--r--   0 default  (1005350000) root         (0)     5191 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/spellbook.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests/unit/
--rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     2085 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_actions.py
--rw-r--r--   0 default  (1005350000) root         (0)     2476 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_api.py
--rw-r--r--   0 default  (1005350000) root         (0)     6848 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_base_git.py
--rw-r--r--   0 default  (1005350000) root         (0)     2309 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_cli.py
--rw-r--r--   0 default  (1005350000) root         (0)     4306 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_cli_utils.py
--rw-r--r--   0 default  (1005350000) root         (0)    23178 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/unit/test_config.py
--rw-r--r--   0 default  (1005350000) root         (0)     3799 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_config_aliases.py
--rw-r--r--   0 default  (1005350000) root         (0)    12716 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_local_project.py
--rw-r--r--   0 default  (1005350000) root         (0)     6342 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_security.py
--rw-r--r--   0 default  (1005350000) root         (0)     2534 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_sync.py
--rw-r--r--   0 default  (1005350000) root         (0)      706 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_unicodez.py
--rw-r--r--   0 default  (1005350000) root         (0)     2957 2020-01-16 12:08:43.000000 packitos-0.8.1/tests/unit/test_upstream.py
--rw-r--r--   0 default  (1005350000) root         (0)     3455 2020-01-20 15:55:16.000000 packitos-0.8.1/tests/unit/test_utils.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests_recording/
--rw-r--r--   0 default  (1005350000) root         (0)     1401 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/README.md
--rw-r--r--   0 default  (1005350000) root         (0)     1740 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/__init__.py
--rw-r--r--   0 default  (1005350000) root         (0)     3739 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_api.py
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:38.000000 packitos-0.8.1/tests_recording/test_data/
-drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-01-20 16:00:40.000000 packitos-0.8.1/tests_recording/test_data/test_status/
--rw-r--r--   0 default  (1005350000) root         (0)   142537 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_builds.yaml
--rw-r--r--   0 default  (1005350000) root         (0)    92011 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_distgen_versions.yaml
--rw-r--r--   0 default  (1005350000) root         (0)    92439 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_dowstream_pr.yaml
--rw-r--r--   0 default  (1005350000) root         (0)    18453 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_status.yaml
--rw-r--r--   0 default  (1005350000) root         (0)    27782 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_up_releases.yaml
--rw-r--r--   0 default  (1005350000) root         (0)   250710 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_updates.yaml
--rw-r--r--   0 default  (1005350000) root         (0)     2798 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/test_status.py
--rw-r--r--   0 default  (1005350000) root         (0)     2612 2020-01-16 12:08:43.000000 packitos-0.8.1/tests_recording/testbase.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:50.000000 packitos-0.9.0/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/.fmf/
+-rw-r--r--   0 default  (1005350000) root         (0)        2 2020-03-22 10:01:19.000000 packitos-0.9.0/.fmf/version
+-rw-r--r--   0 default  (1005350000) root         (0)       23 2020-03-22 10:01:19.000000 packitos-0.9.0/.git_archival.txt
+-rw-r--r--   0 default  (1005350000) root         (0)       72 2020-03-22 10:01:19.000000 packitos-0.9.0/.gitattributes
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/.github/
+-rw-r--r--   0 default  (1005350000) root         (0)      915 2020-03-22 10:01:19.000000 packitos-0.9.0/.github/stale.yml
+-rw-r--r--   0 default  (1005350000) root         (0)       14 2020-03-22 10:01:19.000000 packitos-0.9.0/.gitignore
+-rw-r--r--   0 default  (1005350000) root         (0)      784 2020-03-25 14:52:32.000000 packitos-0.9.0/.packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)     1228 2020-03-25 14:52:32.000000 packitos-0.9.0/.pre-commit-config.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)     3212 2020-03-25 14:52:32.000000 packitos-0.9.0/.zuul.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)    14668 2020-03-25 14:57:35.000000 packitos-0.9.0/CHANGELOG.md
+-rw-r--r--   0 default  (1005350000) root         (0)     7628 2020-03-25 14:52:32.000000 packitos-0.9.0/CONTRIBUTING.md
+-rw-r--r--   0 default  (1005350000) root         (0)     1421 2020-03-22 10:01:19.000000 packitos-0.9.0/DCO
+-rw-r--r--   0 default  (1005350000) root         (0)      759 2020-03-25 14:52:32.000000 packitos-0.9.0/Dockerfile
+-rw-r--r--   0 default  (1005350000) root         (0)      496 2020-03-25 14:52:32.000000 packitos-0.9.0/Dockerfile.tests
+-rw-r--r--   0 default  (1005350000) root         (0)     1099 2020-03-22 10:01:19.000000 packitos-0.9.0/LICENSE
+-rw-r--r--   0 default  (1005350000) root         (0)      963 2020-03-25 14:52:32.000000 packitos-0.9.0/Makefile
+-rw-r--r--   0 default  (1005350000) root         (0)     6938 2020-03-25 14:57:50.000000 packitos-0.9.0/PKG-INFO
+-rw-r--r--   0 default  (1005350000) root         (0)     4787 2020-03-25 14:52:32.000000 packitos-0.9.0/README.md
+-rw-r--r--   0 default  (1005350000) root         (0)      695 2020-03-22 10:01:19.000000 packitos-0.9.0/Vagrantfile
+-rw-r--r--   0 default  (1005350000) root         (0)       86 2020-03-22 10:01:19.000000 packitos-0.9.0/ansible.cfg
+-rw-r--r--   0 default  (1005350000) root         (0)      751 2020-03-22 10:01:19.000000 packitos-0.9.0/ci.fmf
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/design/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/design/export/
+-rw-r--r--   0 default  (1005350000) root         (0)     6148 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/.DS_Store
+-rw-r--r--   0 default  (1005350000) root         (0)   132230 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-dark.png
+-rw-r--r--   0 default  (1005350000) root         (0)    75002 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-extended.jpg
+-rw-r--r--   0 default  (1005350000) root         (0)    48468 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-extended.png
+-rw-r--r--   0 default  (1005350000) root         (0)    24881 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-extended.svg
+-rw-r--r--   0 default  (1005350000) root         (0)   106567 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-guideline.pdf
+-rw-r--r--   0 default  (1005350000) root         (0)    66141 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-no-borders.jpg
+-rw-r--r--   0 default  (1005350000) root         (0)   143587 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-no-borders.png
+-rw-r--r--   0 default  (1005350000) root         (0)    70268 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-square-small-borders.jpg
+-rw-r--r--   0 default  (1005350000) root         (0)   150044 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-square-small-borders.png
+-rw-r--r--   0 default  (1005350000) root         (0)    18005 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-text.jpg
+-rw-r--r--   0 default  (1005350000) root         (0)    14198 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-text.png
+-rw-r--r--   0 default  (1005350000) root         (0)    10016 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-text.svg
+-rw-r--r--   0 default  (1005350000) root         (0)   144552 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo-white.png
+-rw-r--r--   0 default  (1005350000) root         (0)   158074 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo.png
+-rw-r--r--   0 default  (1005350000) root         (0)    14697 2020-03-22 10:01:19.000000 packitos-0.9.0/design/export/logo.svg
+-rw-r--r--   0 default  (1005350000) root         (0)  1843517 2020-03-22 10:01:19.000000 packitos-0.9.0/design/logo-packit.sketch
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/fedora-tests/
+-rwxr-xr-x   0 default  (1005350000) root         (0)      157 2020-03-22 10:01:19.000000 packitos-0.9.0/fedora-tests/simple.py
+-rw-r--r--   0 default  (1005350000) root         (0)      473 2020-03-25 14:52:32.000000 packitos-0.9.0/fedora-tests/tests.yml
+-rwxr-xr-x   0 default  (1005350000) root         (0)      485 2020-03-22 10:01:19.000000 packitos-0.9.0/fedora-tests/upstream.sh
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/files/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/files/bash-completion/
+-rwxr-xr-x   0 default  (1005350000) root         (0)      240 2020-03-22 10:01:19.000000 packitos-0.9.0/files/bash-completion/packit
+-rw-r--r--   0 default  (1005350000) root         (0)      272 2020-03-25 14:52:32.000000 packitos-0.9.0/files/install-requirements.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      383 2020-03-25 14:52:32.000000 packitos-0.9.0/files/install-tests-requirements.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      321 2020-03-25 14:52:32.000000 packitos-0.9.0/files/packit-testing-farm-prepare-session-recording.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      275 2020-03-25 14:52:32.000000 packitos-0.9.0/files/packit-testing-farm-prepare.yaml
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/files/tasks/
+-rw-r--r--   0 default  (1005350000) root         (0)      136 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/build-rpm-deps.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      179 2020-03-22 10:01:19.000000 packitos-0.9.0/files/tasks/configure-git.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      227 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/generic-dnf-requirements.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)       95 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/install-ansible.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)       87 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/install-packit-service.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      102 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/install-packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      114 2020-03-22 10:01:19.000000 packitos-0.9.0/files/tasks/ogr-from-master.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      791 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/packit-service-requirements.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      154 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/python-compile-deps.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      120 2020-03-22 10:01:19.000000 packitos-0.9.0/files/tasks/requre-master.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      242 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/rpm-test-deps.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      172 2020-03-22 10:01:19.000000 packitos-0.9.0/files/tasks/sandcastle-master.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      378 2020-03-25 14:52:32.000000 packitos-0.9.0/files/tasks/zuul-project-setup.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      270 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-install-requirements-git-master.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      394 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-install-requirements-pip.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      272 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-install-requirements-rpms.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      599 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-pre-commit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      586 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-reverse-dep-packit-service.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      460 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-tests-session-recording.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      447 2020-03-25 14:52:32.000000 packitos-0.9.0/files/zuul-tests.yaml
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/packit/
+-rw-r--r--   0 default  (1005350000) root         (0)     1306 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2338 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/actions.py
+-rw-r--r--   0 default  (1005350000) root         (0)    29344 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/api.py
+-rw-r--r--   0 default  (1005350000) root         (0)    16367 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/base_git.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/packit/cli/
+-rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4041 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/build.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3751 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/cli/copr_build.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3208 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/create_update.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3734 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/cli/init.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2507 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/cli/local_build.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3894 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/cli/packit_base.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2032 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/push_updates.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2671 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/srpm.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1973 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/status.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3642 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/sync_from_downstream.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3470 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/types.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4267 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/update.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6082 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/cli/utils.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3585 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/command_handler.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/packit/config/
+-rw-r--r--   0 default  (1005350000) root         (0)      939 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/config/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     5408 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/config/aliases.py
+-rw-r--r--   0 default  (1005350000) root         (0)     8483 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/config/config.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3203 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/config/job_config.py
+-rw-r--r--   0 default  (1005350000) root         (0)    14710 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/config/package_config.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2531 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/config/sync_files_config.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3537 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/constants.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6560 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/copr_helper.py
+-rw-r--r--   0 default  (1005350000) root         (0)    15226 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/distgit.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2732 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/downstream_checks.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2914 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/exceptions.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2176 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/fed_mes_consume.py
+-rw-r--r--   0 default  (1005350000) root         (0)     5106 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/fedpkg.py
+-rw-r--r--   0 default  (1005350000) root         (0)    15667 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/local_project.py
+-rw-r--r--   0 default  (1005350000) root         (0)    10927 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/schema.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6461 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/security.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6972 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/specfile.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6853 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/status.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4472 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/sync.py
+-rw-r--r--   0 default  (1005350000) root         (0)    34805 2020-03-25 14:52:32.000000 packitos-0.9.0/packit/upstream.py
+-rw-r--r--   0 default  (1005350000) root         (0)    12276 2020-03-22 10:01:19.000000 packitos-0.9.0/packit/utils.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3978 2020-03-25 14:57:35.000000 packitos-0.9.0/packit.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/packitos.egg-info/
+-rw-r--r--   0 default  (1005350000) root         (0)     6938 2020-03-25 14:57:46.000000 packitos-0.9.0/packitos.egg-info/PKG-INFO
+-rw-r--r--   0 default  (1005350000) root         (0)     7940 2020-03-25 14:57:48.000000 packitos-0.9.0/packitos.egg-info/SOURCES.txt
+-rw-r--r--   0 default  (1005350000) root         (0)        1 2020-03-25 14:57:46.000000 packitos-0.9.0/packitos.egg-info/dependency_links.txt
+-rw-r--r--   0 default  (1005350000) root         (0)       63 2020-03-25 14:57:46.000000 packitos-0.9.0/packitos.egg-info/entry_points.txt
+-rw-r--r--   0 default  (1005350000) root         (0)      190 2020-03-25 14:57:46.000000 packitos-0.9.0/packitos.egg-info/requires.txt
+-rw-r--r--   0 default  (1005350000) root         (0)        7 2020-03-25 14:57:46.000000 packitos-0.9.0/packitos.egg-info/top_level.txt
+-rw-r--r--   0 default  (1005350000) root         (0)       53 2020-03-22 10:01:19.000000 packitos-0.9.0/pytest.ini
+-rw-r--r--   0 default  (1005350000) root         (0)      720 2020-03-25 14:52:32.000000 packitos-0.9.0/recipe-tests.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      158 2020-03-22 10:01:19.000000 packitos-0.9.0/release-conf.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)     1518 2020-03-25 14:57:50.000000 packitos-0.9.0/setup.cfg
+-rw-r--r--   0 default  (1005350000) root         (0)     1191 2020-03-22 10:01:19.000000 packitos-0.9.0/setup.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/
+-rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4316 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/conftest.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/cockpit-ostree/
+-rw-r--r--   0 default  (1005350000) root         (0)      948 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/cockpit-ostree/Makefile
+-rw-r--r--   0 default  (1005350000) root         (0)      796 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/cockpit-ostree/cockpit-ostree.spec.dg
+-rw-r--r--   0 default  (1005350000) root         (0)      804 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/cockpit-ostree/cockpit-ostree.spec.in
+-rw-r--r--   0 default  (1005350000) root         (0)      315 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/cockpit-ostree/packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)      146 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/copr_config
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/dg-ogr/
+-rw-r--r--   0 default  (1005350000) root         (0)      961 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/dg-ogr/.packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)       37 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/dg-ogr/README.md
+-rw-r--r--   0 default  (1005350000) root         (0)       61 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/dg-ogr/README.packit
+-rw-r--r--   0 default  (1005350000) root         (0)     2295 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/dg-ogr/python-ogr.spec
+-rw-r--r--   0 default  (1005350000) root         (0)      157 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/dg-ogr/sources
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/dist_git/
+-rw-r--r--   0 default  (1005350000) root         (0)      214 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/dist_git/.packit.json
+-rw-r--r--   0 default  (1005350000) root         (0)      451 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/dist_git/beer.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/edd/
+-rw-r--r--   0 default  (1005350000) root         (0)      181 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/edd/.packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/LICENSE
+-rw-r--r--   0 default  (1005350000) root         (0)     1348 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/Makefile
+-rw-r--r--   0 default  (1005350000) root         (0)      192 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/README.rst
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/edd/docs/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/docs/man.rst
+-rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/edd
+-rw-r--r--   0 default  (1005350000) root         (0)     1422 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/edd/edd.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/empty_changelog/
+-rw-r--r--   0 default  (1005350000) root         (0)      166 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/empty_changelog/.packit.json
+-rw-r--r--   0 default  (1005350000) root         (0)      327 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/empty_changelog/beer.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/osbuild/
+-rw-r--r--   0 default  (1005350000) root         (0)      233 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/osbuild/.packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)       10 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/osbuild/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1462 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/osbuild/osbuild.spec
+-rw-r--r--   0 default  (1005350000) root         (0)       65 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/osbuild/setup.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/osbuild/sources/
+-rw-r--r--   0 default  (1005350000) root         (0)        5 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/osbuild/sources/test
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/snapd/
+-rw-r--r--   0 default  (1005350000) root         (0)      395 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/snapd/.packit.yaml
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/snapd/packaging/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/snapd/packaging/fedora/
+-rwxr-xr-x   0 default  (1005350000) root         (0)      456 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/snapd/packaging/fedora/fix-spec
+-rwxr-xr-x   0 default  (1005350000) root         (0)     1840 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/snapd/packaging/fedora/pack-source
+-rw-r--r--   0 default  (1005350000) root         (0)    18386 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/snapd/packaging/fedora/snapd.spec
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/snapd/packaging/fedora/some-file-to-add
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/snapd/vendor/
+-rw-r--r--   0 default  (1005350000) root         (0)     7844 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/snapd/vendor/vendor.json
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sourcegit/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sourcegit/source_git/
+-rw-r--r--   0 default  (1005350000) root         (0)      506 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/sourcegit/source_git/.packit.yaml
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sourcegit/source_git/fedora/
+-rw-r--r--   0 default  (1005350000) root         (0)      450 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/sourcegit/source_git/fedora/beer.spec
+-rw-r--r--   0 default  (1005350000) root         (0)       20 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sourcegit/source_git/ignored_file.txt
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sourcegit/upstream/
+-rw-r--r--   0 default  (1005350000) root         (0)       45 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sourcegit/upstream/big-source-file.txt
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/spec_not_in_root/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/spec_not_in_root/upstream/
+-rw-r--r--   0 default  (1005350000) root         (0)      180 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/spec_not_in_root/upstream/.packit.json
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/spec_not_in_root/upstream/dir_with_spec/
+-rw-r--r--   0 default  (1005350000) root         (0)      421 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/spec_not_in_root/upstream/dir_with_spec/beer.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sync_files/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/a.md
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/b.md
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/c.txt
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/sync_files/example_dir/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/example_dir/d.md
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/example_dir/e.md
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/sync_files/example_dir/f.txt
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/upstream_git/
+-rw-r--r--   0 default  (1005350000) root         (0)      166 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/upstream_git/.packit.json
+-rw-r--r--   0 default  (1005350000) root         (0)      421 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/upstream_git/beer.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/upstream_git_with_multiple_sources/
+-rw-r--r--   0 default  (1005350000) root         (0)      166 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/upstream_git_with_multiple_sources/.packit.json
+-rw-r--r--   0 default  (1005350000) root         (0)      513 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/upstream_git_with_multiple_sources/beer.spec
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/vsftpd/
+-rw-r--r--   0 default  (1005350000) root         (0)      234 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/data/vsftpd/.packit.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/AUDIT
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/BENCHMARKS
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/BUGS
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/COPYING
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/Changelog
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/vsftpd/EXAMPLE/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/EXAMPLE/example
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:19.000000 packitos-0.9.0/tests/data/vsftpd/FAQ
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/
+-rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd-generator
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.ftpusers
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.pam
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.service
+-rw-r--r--   0 default  (1005350000) root         (0)    27817 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.spec
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.target
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.user_list
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.xinetd
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd@.service
+-rwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd_conf_migrate.sh
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/INSTALL
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/LICENSE
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/README
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/README.security
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/REWARD
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/vsftpd/RedHat/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/RedHat/vsftpd.log
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/data/vsftpd/SECURITY/
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/SECURITY/security
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/SIZE
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/SPEED
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/TODO
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/TUNING
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/vsftpd.8
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/vsftpd.conf
+-rw-r--r--   0 default  (1005350000) root         (0)        0 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/data/vsftpd/vsftpd.conf.5
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/functional/
+-rw-r--r--   0 default  (1005350000) root         (0)       19 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/functional/README.md
+-rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/functional/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)      509 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/functional/spellbook.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1796 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/functional/test_local_build.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3977 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/functional/test_srpm.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests/integration/
+-rw-r--r--   0 default  (1005350000) root         (0)       38 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/README.md
+-rw-r--r--   0 default  (1005350000) root         (0)       99 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2433 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/bodhi_latest_builds.py
+-rw-r--r--   0 default  (1005350000) root         (0)    43175 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/bodhi_status_updates.py
+-rw-r--r--   0 default  (1005350000) root         (0)    11615 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/integration/conftest.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3023 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_actions.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1605 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_api.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3567 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_base_git.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2689 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_build.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4104 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_copr_build.py
+-rw-r--r--   0 default  (1005350000) root         (0)    12447 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_create_update.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1479 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_distgit.py
+-rw-r--r--   0 default  (1005350000) root         (0)      682 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_generate.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4832 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_get_api.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2472 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_pagure.py
+-rw-r--r--   0 default  (1005350000) root         (0)    18568 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_push_updates.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3186 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_security.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6697 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/integration/test_source_git.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2163 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/integration/test_spec.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3829 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_sync_files.py
+-rw-r--r--   0 default  (1005350000) root         (0)     5157 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/integration/test_update.py
+-rw-r--r--   0 default  (1005350000) root         (0)     7770 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/integration/test_upstream.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3603 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_using_cockpit.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2352 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/test_using_examples.py
+-rw-r--r--   0 default  (1005350000) root         (0)     1323 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/integration/utils.py
+-rw-r--r--   0 default  (1005350000) root         (0)     5943 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/spellbook.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:50.000000 packitos-0.9.0/tests/unit/
+-rw-r--r--   0 default  (1005350000) root         (0)     1112 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2085 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_actions.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2476 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_api.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6848 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_base_git.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2309 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_cli.py
+-rw-r--r--   0 default  (1005350000) root         (0)     4306 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_cli_utils.py
+-rw-r--r--   0 default  (1005350000) root         (0)    25562 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_config.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3979 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_config_aliases.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2253 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_load_authentication.py
+-rw-r--r--   0 default  (1005350000) root         (0)    12716 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_local_project.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2307 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_package_config.py
+-rw-r--r--   0 default  (1005350000) root         (0)     6732 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_security.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2534 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_sync.py
+-rw-r--r--   0 default  (1005350000) root         (0)      706 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_unicodez.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2957 2020-03-22 10:01:20.000000 packitos-0.9.0/tests/unit/test_upstream.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3661 2020-03-25 14:52:32.000000 packitos-0.9.0/tests/unit/test_utils.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:50.000000 packitos-0.9.0/tests_recording/
+-rw-r--r--   0 default  (1005350000) root         (0)     1366 2020-03-25 14:52:32.000000 packitos-0.9.0/tests_recording/README.md
+-rw-r--r--   0 default  (1005350000) root         (0)     1740 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/__init__.py
+-rw-r--r--   0 default  (1005350000) root         (0)     3739 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_api.py
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:49.000000 packitos-0.9.0/tests_recording/test_data/
+drwxr-xr-x   0 default  (1005350000) root         (0)        0 2020-03-25 14:57:50.000000 packitos-0.9.0/tests_recording/test_data/test_status/
+-rw-r--r--   0 default  (1005350000) root         (0)   142537 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_builds.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)    92011 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_distgen_versions.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)    92439 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_dowstream_pr.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)    18453 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_status.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)    27782 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_up_releases.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)   250710 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_updates.yaml
+-rw-r--r--   0 default  (1005350000) root         (0)     2798 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/test_status.py
+-rw-r--r--   0 default  (1005350000) root         (0)     2612 2020-03-22 10:01:20.000000 packitos-0.9.0/tests_recording/testbase.py
```

### Comparing `packitos-0.8.1/.github/stale.yml` & `packitos-0.9.0/.github/stale.yml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/.packit.yaml` & `packitos-0.9.0/.packit.yaml`

 * *Files 25% similar despite different names*

```diff
@@ -1,37 +1,32 @@
 ---
-specfile_path: packit.spec
 synced_files:
-  - packit.spec
-  - .packit.yaml
   - src: fedora-tests/
     dest: tests/
 # packit was already taken on PyPI
 upstream_package_name: packitos
-downstream_package_name: packit
 upstream_project_url: https://github.com/packit-service/packit
 
 actions:
   create-archive:
-  - "python3 setup.py sdist --dist-dir ."
-  - "sh -c 'echo packitos-$(python3 setup.py --version).tar.gz'"
+    - "python3 setup.py sdist --dist-dir ."
+    - "sh -c 'echo packitos-$(python3 setup.py --version).tar.gz'"
   get-current-version:
-  - "python3 setup.py --version"
-
+    - "python3 setup.py --version"
 
 jobs:
-- job: propose_downstream
-  trigger: release
-  metadata:
-    dist-git-branch: fedora-all
-- job: sync_from_downstream
-  trigger: commit
-- job: copr_build
-  trigger: pull_request
-  metadata:
-    targets:
-    - fedora-all
-- job: tests
-  trigger: pull_request
-  metadata:
-    targets:
-    - fedora-stable # on rawhide we have problems with the new marshmallow
+  - job: propose_downstream
+    trigger: release
+    metadata:
+      dist-git-branch: fedora-all
+  - job: sync_from_downstream
+    trigger: commit
+  - job: copr_build
+    trigger: pull_request
+    metadata:
+      targets:
+        - fedora-all
+  - job: tests
+    trigger: pull_request
+    metadata:
+      targets:
+        - fedora-stable # on rawhide we have problems with the new marshmallow
```

### Comparing `packitos-0.8.1/.pre-commit-config.yaml` & `packitos-0.9.0/.pre-commit-config.yaml`

 * *Files 12% similar despite different names*

```diff
@@ -1,36 +1,44 @@
 # HOWTO: https://pre-commit.com/#usage
 # pip3 install pre-commit
 # pre-commit install
 
 repos:
--   repo: https://github.com/ambv/black
-    rev: 19.3b0
+  - repo: https://github.com/psf/black
+    rev: stable
     hooks:
-    - id: black
-      language_version: python3.6
--   repo: https://github.com/pre-commit/pre-commit-hooks
-    rev: v2.2.3
-    hooks:
-    - id: check-added-large-files
-    - id: check-ast
-    - id: check-merge-conflict
-    - id: check-yaml
-    - id: detect-private-key
-      exclude: tests/integration/conftest.py
-    - id: end-of-file-fixer
-    - id: trailing-whitespace
-    - id: flake8
-      args:
-        - --max-line-length=100
-        - --per-file-ignores=files/packit.wsgi:F401,E402
--   repo: https://github.com/pre-commit/mirrors-mypy
-    rev: v0.711
+      - id: black
+        language_version: python3.6
+  - repo: https://github.com/prettier/prettier
+    rev: 1.19.1
     hooks:
-    -   id: mypy
+      - id: prettier
+        exclude: tests_recording/test_data/*
+  - repo: https://github.com/pre-commit/pre-commit-hooks
+    rev: v2.5.0
+    hooks:
+      - id: check-added-large-files
+      - id: check-ast
+      - id: check-merge-conflict
+      - id: check-yaml
+      - id: detect-private-key
+        exclude: tests/integration/conftest.py
+      - id: end-of-file-fixer
+      - id: trailing-whitespace
+  - repo: https://gitlab.com/pycqa/flake8
+    rev: 3.7.9
+    hooks:
+      - id: flake8
+        args:
+          - --max-line-length=100
+          - --per-file-ignores=files/packit.wsgi:F401,E402
+  - repo: https://github.com/pre-commit/mirrors-mypy
+    rev: v0.761
+    hooks:
+      - id: mypy
         args: [--no-strict-optional, --ignore-missing-imports]
--   repo: https://github.com/packit-service/pre-commit-hooks
+  - repo: https://github.com/packit-service/pre-commit-hooks
     rev: master
     hooks:
-    -   id: check-rebase
+      - id: check-rebase
         args:
-        - git://github.com/packit-service/packit.git
+          - git://github.com/packit-service/packit.git
```

### Comparing `packitos-0.8.1/.zuul.yaml` & `packitos-0.9.0/.zuul.yaml`

 * *Files 25% similar despite different names*

```diff
@@ -6,77 +6,79 @@
         - packit-pre-commit
         - packit-tests-rpm
         - packit-tests-pip-deps
         - packit-tests-git-master
         - packit-tests-rpm-sess-rec
         - packit-tests-pip-deps-sess-rec
         - packit-tests-git-master-sess-rec
+        - reverse-dep-packit-service-tests
     gate:
       jobs:
         - packit-pre-commit
         - packit-tests-rpm
         - packit-tests-pip-deps
         - packit-tests-git-master
         - packit-tests-rpm-sess-rec
         - packit-tests-pip-deps-sess-rec
         - packit-tests-git-master-sess-rec
+        - reverse-dep-packit-service-tests
 
 - job:
     name: packit-pre-commit
     parent: base
     description: Check precommit
     run: files/zuul-pre-commit.yaml
     extra-vars:
       ansible_python_interpreter: /usr/bin/python3
     nodeset:
       nodes:
         - name: test-node
-          label: cloud-fedora-30
+          label: cloud-fedora-31
 
 - job:
     name: packit-tests-rpm
     parent: base
     description: Run tests of packit via rpms
     pre-run: files/zuul-install-requirements-rpms.yaml
     run: files/zuul-tests.yaml
     extra-vars:
       with_testing: true
       ansible_python_interpreter: /usr/bin/python3
     nodeset:
       nodes:
         - name: test-node
-          label: cloud-fedora-30
+          label: cloud-fedora-31
 
 - job:
     name: packit-tests-pip-deps
     parent: base
     description: Run tests of packit via pip installed dependencies
     pre-run: files/zuul-install-requirements-pip.yaml
     run: files/zuul-tests.yaml
     extra-vars:
       with_testing: true
       ansible_python_interpreter: /usr/bin/python3
     nodeset:
       nodes:
         - name: test-node
-          label: cloud-fedora-30
+          label: cloud-fedora-31
 
 - job:
     name: packit-tests-git-master
     parent: base
     description: Run tests of packit via pip installed dependencies
     pre-run: files/zuul-install-requirements-git-master.yaml
     run: files/zuul-tests.yaml
     extra-vars:
       with_testing: true
       ansible_python_interpreter: /usr/bin/python3
     nodeset:
       nodes:
         - name: test-node
-          label: cloud-fedora-30
+          label: cloud-fedora-31
 
 - job:
     name: packit-tests-rpm-sess-rec
     parent: packit-tests-rpm
     description: Run session recording tests of packit via rpms
     run: files/zuul-tests-session-recording.yaml
 
@@ -87,7 +89,23 @@
     run: files/zuul-tests-session-recording.yaml
 
 - job:
     name: packit-tests-git-master-sess-rec
     parent: packit-tests-git-master
     description: Run session recording tests of packit via pip installed dependencies
     run: files/zuul-tests-session-recording.yaml
+
+- job:
+    name: reverse-dep-packit-service-tests
+    parent: base
+    description: Run packit-service tests to check if we do not break packit-service
+    required-projects:
+      - github.com/packit-service/packit-service
+    pre-run: files/zuul-install-requirements-pip.yaml
+    run: files/zuul-reverse-dep-packit-service.yaml
+    extra-vars:
+      with_testing: true
+      ansible_python_interpreter: /usr/bin/python3
+    nodeset:
+      nodes:
+        - name: test-node
+          label: cloud-fedora-31
```

### Comparing `packitos-0.8.1/CHANGELOG.md` & `packitos-0.9.0/CHANGELOG.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,21 +1,42 @@
+# 0.9.0
+
+## Features
+
+- CLI has a new `local-build` command.
+- Packit learned how to look for RPM spec files on its own, so specifying `specfile_path` in the configuration is not mandatory anymore.
+- Default configuration has `tests` job enabled from now on. You still need to use `fmf` to create some tests, otherwise testing-farm only tests the success of the installation.
+- We don't touch `Version` in spec files and change `Release` only by default.
+
+## Minor changes and fixes
+
+- Improved documentation (README & CONTRIBUTING).
+- `copr-build` CLI command has new `--upstrem-ref` option.
+- As a result of `keys.fedoraproject.org` being turned off, Packit now tries a list of GPG keyservers when downloading keys to check commit signatures.
+- `generate` CLI command is now deprecated in favor of the `init` command.
+- When executing `copr-build` command, you don't need to set project name if this value is defined in `copr_build` job in configuration file.
+- When loading authentication in the config file - users are warned only if deprecated keys are used, no more confusing messages when you do not have authentication key in the configuration.
+- Several `source-git` related fixes & improvements are applied.
+- A bug which was causing SRPM-build failures in Packit Service for projects which had their spec files stored in a subdirectory is fixed.
+- We handle `git-describe` output better: it should help when tags contain dashes.
+
 # 0.8.1
 
 ## Features:
 
 - Packit is able to build in [Koji](https://koji.fedoraproject.org) from upstream/source-git.
 - CLI has bash-completion.
 - Configuration can use a new option (`patch_generation_ignore_paths`) to exclude paths from patching.
 
-
 # 0.8.0
 
 Packit has a [new logo](https://github.com/packit-service/packit/blob/master/design/export/logo.svg)!
 
 ## Features:
+
 - Marshmallow object schema was implemented.
 - `config file` and `spec file` are synced by default.
 - We use testing farm for sanity tests.
 - `packit status` command shows latest copr builds.
 - Target aliases (currently fedora-development, fedora-stable, fedora-all) can now be used in the packit config file.
 - `upstream_package_name` and `downstream_package_name` are no longer required in package config. github repository name is the default value both.
 - If no jobs are defined in .packit.yaml, packit by default runs build job on fedora-stable targets and propose_downstream on fedora-all branches.
@@ -29,292 +50,286 @@
 - Specfile is refreshed after each run of the propose-update.
 - When there is no copr project owner, exception is raised
 - While building specfile from custom specfile, the archive is linked from the spec-directory.
 - Setting cwd in command handlers is allowed.
 - SRPM build is run from the folder containing specfile.
 
 ## Fixes:
+
 - Consecutive API call for status works.
 - rebase-helper breaking changes in new version is fixed.
 - fixed updating version on srpm build
 
 ## Minor:
+
 - pre-commit check requires rebased branch.
 - fedora version in .packit.yaml config is updated.
 - Code related to copr id now extracted to dedicated class.
-- There is a warning in logs when there is  no packit config in repository.
+- There is a warning in logs when there is no packit config in repository.
 - Tests are now restructured and use new structure or `requre`, also containing tests for copr.
 - The stale bot is now set with up-to-date config.
 - The imports of packit are simplier.
 - The preparation of SRPM build has been refactored including new exceptions.
 
 # 0.7.1
 
 ## Minor
 
-* The "Developer Certificate of Origin" was added to the git repository.
+- The "Developer Certificate of Origin" was added to the git repository.
 
 ## Fixes
 
-* Packit will determine `upstream_project_url` from git remote if not specified in the config.
-
+- Packit will determine `upstream_project_url` from git remote if not specified in the config.
 
 # 0.7.0
 
 See our [website](https://packit.dev) for up-to-date documentation on how to
 use the new features described below.
 
 ## Deprecation changes
 
-* Rename `upstream_project_name` option to `upstream_package_name`.
-  * The old one is now deprecated and will be ignored in the future.
+- Rename `upstream_project_name` option to `upstream_package_name`.
+  - The old one is now deprecated and will be ignored in the future.
 
 ## Features
 
-* Packit is now able to be used from a distgit repository.
-  * You need to specify `upstream_project_url` to make it work.
-* New option (`upstream_tag_template`) was added to the configuration file to
+- Packit is now able to be used from a distgit repository.
+  - You need to specify `upstream_project_url` to make it work.
+- New option (`upstream_tag_template`) was added to the configuration file to
   support more versioning schemes.
-* You can now use `Source` and `Source0` macros to define upstream sources.
-* The configuration of the authentication was reworked: it nested under
+- You can now use `Source` and `Source0` macros to define upstream sources.
+- The configuration of the authentication was reworked: it nested under
   `authentication` key.
-  * The scheme now supports multiple git services.
+  - The scheme now supports multiple git services.
 
 ## Fixes
 
-* Packit now verifies the output of the `create-archive` action.
-
+- Packit now verifies the output of the `create-archive` action.
 
 # 0.6.1
 
 This patch release contains only few bug-fixes on top of 0.6.0.
 
 # 0.6.0
 
 We keep our documentation up to date: https://packit.dev/docs - you can learn
 how to use all the latest features.
 
 ## Breaking changes
 
-* `pagure_fork_token` is no longer needed given a change which happened in
+- `pagure_fork_token` is no longer needed given a change which happened in
   pagure (src.fedoraproject.org); [Pierre](https://pagure.io/user/pingou)
   rocks!
-* New COPR projects created by packit are no longer listed in the COPR
+- New COPR projects created by packit are no longer listed in the COPR
   dashboard and are set to be deleted after 180 days upon being created.
 
 ## Features
 
-* There is a new command `push-updates` to mark bodhi updates for stable.
-* Packit now sets description and instructions for newly created COPR projects.
-* There is a new config option to set ID of a spec file Source which packit
+- There is a new command `push-updates` to mark bodhi updates for stable.
+- Packit now sets description and instructions for newly created COPR projects.
+- There is a new config option to set ID of a spec file Source which packit
   should operate on (defaults to 0). Packit now also updates the `%[auto]setup`
   macro in `%prep` so that the generated archive is correctly unpacked - this
   behavior matches what tito does.
-* There is a new action `fix-spec` which by default sets Source0, %version and
+- There is a new action `fix-spec` which by default sets Source0, %version and
   %setup macros in spec file - you can override it with your own
   implementation. [Documentation](https://packit.dev/docs/actions)
-* Packit now sets certain environment variables during `fix-spec` and
+- Packit now sets certain environment variables during `fix-spec` and
   `create-archive` actions. You can read more about this in the documentation
   for actions.
 
 ## Fixes
 
-* Packit can be again installed as an RPM: it correctly depends on koji client
+- Packit can be again installed as an RPM: it correctly depends on koji client
   library now.
-* If an error happens in a section while doing `status`, the section is now
+- If an error happens in a section while doing `status`, the section is now
   skipped and rest of the information is printed.
-* Packit is able to handle URLs to git repo if they end with a slash.
-
+- Packit is able to handle URLs to git repo if they end with a slash.
 
 # 0.5.1
 
 ## Breaking changes
 
-* Command `version` no longer exists and is now replaced with a `--version`
+- Command `version` no longer exists and is now replaced with a `--version`
   option. (thanks to @FrNecas)
 
 ## Fixes
 
-* Fix creation of SRPMs - they can be rebuilt now properly.
-* Don't update %changelog if it's not present in the spec file.
-* Koji builds are now obtained using koji, not bodhi, in `status` command which
+- Fix creation of SRPMs - they can be rebuilt now properly.
+- Don't update %changelog if it's not present in the spec file.
+- Koji builds are now obtained using koji, not bodhi, in `status` command which
   should yield more consistent results.
-* Comments in generated .packit.yaml (using `generate` command) should be now
+- Comments in generated .packit.yaml (using `generate` command) should be now
   more accurate.
-* Command `sync-from-downstream` no longer creates a branch when using option
+- Command `sync-from-downstream` no longer creates a branch when using option
   `--no-pr`.
-* Building in copr now yields an URL to frontend instead of a link to log files.
-* `status` command now displays one update per stable Fedora release.
+- Building in copr now yields an URL to frontend instead of a link to log files.
+- `status` command now displays one update per stable Fedora release.
 
 ## Minor
 
-* We are using softwarefactory.io Zuul now instead of Centos CI jenkins.
-* CONTRIBUTING.md file is now fully up to date when it comes to CI testing.
-* Updates to our testing scripts.
-
+- We are using softwarefactory.io Zuul now instead of Centos CI jenkins.
+- CONTRIBUTING.md file is now fully up to date when it comes to CI testing.
+- Updates to our testing scripts.
 
 # 0.5.0
 
 All the documentation was moved to our site: https://packit.dev/docs
 
 ## Features
 
-* If you set up `fas_username` in your config, packit will perform kinit before
+- If you set up `fas_username` in your config, packit will perform kinit before
   doing an authenticated dist-git clone.
-* You can now specify a koji target when building in koji using the `build`
+- You can now specify a koji target when building in koji using the `build`
   command.
-* There is a new command `copr-build` which enables you to submit builds into
+- There is a new command `copr-build` which enables you to submit builds into
   Fedora COPR build system.
-* The config file now has a new attribute called `create_pr` which tells packit
+- The config file now has a new attribute called `create_pr` which tells packit
   whether it should create pull requests in dist-git or push directly.
-* `build` command now waits for the build to finish and has a `--nowait`.
-* Packit now supports the most popular archive formats, not just .tar.gz
+- `build` command now waits for the build to finish and has a `--nowait`.
+- Packit now supports the most popular archive formats, not just .tar.gz
   (thanks to @FrNecas for contributing this feature)
-* Command `propose-update` can now push directly to dist-git. This can be
+- Command `propose-update` can now push directly to dist-git. This can be
   controlled via a CLI option `--nopr` or in a config using `create_pr` value.
-* When doing a `propose-update`, packit no longer does a 1:1 copy, instead it
+- When doing a `propose-update`, packit no longer does a 1:1 copy, instead it
   copies everything from the upstream spec except for %changelog and then
   performs `rpmdev-bumpspec`.
 
 ## Fixes
 
-* SRPMs are now being correctly created from source-git repos.
-* Packit is now able to clone a dist-git repo using authentication (`fedpkg
-  clone`) and push to it afterwards.
-* `packit status` now displays also a latest rawhide koji build.
-* The command `propose-update` does no longer fail when looking for an upstream
+- SRPMs are now being correctly created from source-git repos.
+- Packit is now able to clone a dist-git repo using authentication (`fedpkg clone`) and push to it afterwards.
+- `packit status` now displays also a latest rawhide koji build.
+- The command `propose-update` does no longer fail when looking for an upstream
   archive.
-* Packit no longer discards changes in the local git repo if it's dirty.
+- Packit no longer discards changes in the local git repo if it's dirty.
 
 ## Minor
 
-* Several improvements to text printed by packit.
-* We are now using Zuul for testing and have multiple jobs set up to verify
+- Several improvements to text printed by packit.
+- We are now using Zuul for testing and have multiple jobs set up to verify
   packit works against different versions of dependant software.
 
-
 # 0.4.2
 
-* Packit now uses [Sandcastle](https://github.com/packit-service/sandcastle) to run untrusted commands in a sandbox.
-* Service code has been moved to separate [repo](https://github.com/packit-service/packit-service).
-* [Actions](https://github.com/packit-service/packit/blob/master/docs/actions.md) [now support](https://github.com/packit-service/packit/pull/363) more commands per action.
-* Lots of code, documentation and tests fixes.
+- Packit now uses [Sandcastle](https://github.com/packit-service/sandcastle) to run untrusted commands in a sandbox.
+- Service code has been moved to separate [repo](https://github.com/packit-service/packit-service).
+- [Actions](https://github.com/packit-service/packit/blob/master/docs/actions.md) [now support](https://github.com/packit-service/packit/pull/363) more commands per action.
+- Lots of code, documentation and tests fixes.
 
 # 0.4.1
 
-* Patch release with few fixes/minor changes.
+- Patch release with few fixes/minor changes.
 
 # 0.4.0
 
 ## Features
-* Packit service now submits builds in [copr](https://copr.fedorainfracloud.org) and once they're done it adds a GitHub status and comment with instructions how to install the builds.
-* Packit service is now configurable via [jobs](https://packit.dev/docs/configuration/#packit-service-jobs) defined in configuration file.
-* Packit is now able to check GPG signatures of the upstream commits against configured fingerprints.
-* [CLI] `srpm` command now works also with [Source-git](https://packit.dev/source-git/).
-* Fedmsg parsing has been unified into a single `listen-to-fedmsg` command.
-* Packit service: Github webhook now reacts to ping event and validates payload signature.
+
+- Packit service now submits builds in [copr](https://copr.fedorainfracloud.org) and once they're done it adds a GitHub status and comment with instructions how to install the builds.
+- Packit service is now configurable via [jobs](https://packit.dev/docs/configuration/#packit-service-jobs) defined in configuration file.
+- Packit is now able to check GPG signatures of the upstream commits against configured fingerprints.
+- [CLI] `srpm` command now works also with [Source-git](https://packit.dev/source-git/).
+- Fedmsg parsing has been unified into a single `listen-to-fedmsg` command.
+- Packit service: Github webhook now reacts to ping event and validates payload signature.
 
 ## Fixes
-* More source-git related changes have been applied.
-* Few tracebacks when using CLI have been fixed.
-* RPM package now really contains generated man pages.
+
+- More source-git related changes have been applied.
+- Few tracebacks when using CLI have been fixed.
+- RPM package now really contains generated man pages.
 
 ## Minor
-* Packit service runs on httpd server.
-* [CLI] `status` command now access remote APIs asynchronously in parallel, which should speed up the execution.
-* CLI now has `--dry-run` option to not perform any remote changes (pull requests or comments).
-* Repository now includes Dockerfile and we by default use Docker instead of ansible-bender to build container image.
-* Repository now includes Vagranfile.
-* List of on-boarded projects has been moved to [README.md](https://github.com/packit-service/packit/blob/master/README.md#already-on-boarded)
 
+- Packit service runs on httpd server.
+- [CLI] `status` command now access remote APIs asynchronously in parallel, which should speed up the execution.
+- CLI now has `--dry-run` option to not perform any remote changes (pull requests or comments).
+- Repository now includes Dockerfile and we by default use Docker instead of ansible-bender to build container image.
+- Repository now includes Vagranfile.
+- List of on-boarded projects has been moved to [README.md](https://github.com/packit-service/packit/blob/master/README.md#already-on-boarded)
 
 # 0.3.0
 
 We have a brand new website: https://packit.dev/!
 [packit.dev repo](https://github.com/packit-service/packit.dev) contains source content for [Hugo website engine](https://gohugo.io).
 
 ## Features
 
-* Packit supports [Source-git](https://packit.dev/source-git/).
-* You can now specify your own actions to replace default packit behavior.
-* Packit supports pagure.io-based upstream projects.
-* Packit {propose-update, sync-from-downstream} supports copying directories.
-* A new `status` command to display useful upstream/downstream info.
-* You can now have a config file for packit in your home directory(`~/.config/packit.yaml`).
-* Packit installed from an RPM now has manpages.
+- Packit supports [Source-git](https://packit.dev/source-git/).
+- You can now specify your own actions to replace default packit behavior.
+- Packit supports pagure.io-based upstream projects.
+- Packit {propose-update, sync-from-downstream} supports copying directories.
+- A new `status` command to display useful upstream/downstream info.
+- You can now have a config file for packit in your home directory(`~/.config/packit.yaml`).
+- Packit installed from an RPM now has manpages.
 
 ## Fixes
 
-* Downstream pull requests titles now have correct version numbers.
-* `sync-from-downstream` command constructs a PR correctly when origin is a fork.
+- Downstream pull requests titles now have correct version numbers.
+- `sync-from-downstream` command constructs a PR correctly when origin is a fork.
 
 ## Minor
 
-* Improved documentation.
-* Code refactoring.
-* Added MIT license notice into python files.
-* CI shows code coverage and runs linters/checkers defined in pre-commit config file.
-* We've started work on packit service by implementing a handler for a Github
+- Improved documentation.
+- Code refactoring.
+- Added MIT license notice into python files.
+- CI shows code coverage and runs linters/checkers defined in pre-commit config file.
+- We've started work on packit service by implementing a handler for a Github
   webhook. More to come in the next cycle!
-* Packit is able to authenticate as a GitHub App.
-
+- Packit is able to authenticate as a GitHub App.
 
 # 0.2.0
 
-
 ## Breaking Changes
 
-* We have renamed two variables in our configuration file:
-  * `package_name` → `downstream_package_name`
-  * `upstream_name` → `upstream_project_name`
+- We have renamed two variables in our configuration file:
+  - `package_name` → `downstream_package_name`
+  - `upstream_name` → `upstream_project_name`
 
 ## Features
 
-* You can now use packit to sync files from your dist-git repo into upstream
+- You can now use packit to sync files from your dist-git repo into upstream
   (mainly to keep spec files in sync). `sync-from-downstream` is the command.
-* An SRPM can be created out of the current content in your upstream repository
+- An SRPM can be created out of the current content in your upstream repository
   — please check out the `srpm` command.
-* Packit is able to create bodhi updates using the `create-update` command.
-* You can ask packit to build the latest content of your dist-git
+- Packit is able to create bodhi updates using the `create-update` command.
+- You can ask packit to build the latest content of your dist-git
   repository in koji: the command is `build`.
-* We have added `--force-new-sources` option to propose-update update command
+- We have added `--force-new-sources` option to propose-update update command
   to bypass our caching optimization.
-* `propose-update` command now has option `--local-content` which disables
+- `propose-update` command now has option `--local-content` which disables
   checking out the tag with the upstream release. This is useful if you forget
   to bump your spec file when doing a release.
-* You are now able to pick a specific upstream release version in
+- You are now able to pick a specific upstream release version in
   `propose-update` command.
 
 ## Fixes
 
-* Packit checks if the upstream tarball is already present in the lookaside
+- Packit checks if the upstream tarball is already present in the lookaside
   cache so it's not uploaded twice. We have fixed a behavior when the upload
   part was skipped while having old tarball specified in dist-git. Packit now
   does the right thing - checks if sources file has the correct tarball
   referenced.
-* We have updated several error messages which were coming from GitPython and
+- We have updated several error messages which were coming from GitPython and
   it was not clear what's wrong.
 
 ## Minor
 
-* We have added CONTRIBUTING.md to ease contribution to packit. All your
+- We have added CONTRIBUTING.md to ease contribution to packit. All your
   patches are welcome!
-* We are now using black, flake8 and mypy to improve code quality.
-* We have moved some info from README to dedicated doc. Also, all the
+- We are now using black, flake8 and mypy to improve code quality.
+- We have moved some info from README to dedicated doc. Also, all the
   documentation should be up to date.
 
-
 # 0.1.0
 
 The first official release of packit!
 
-
 ## Features
 
-* `packit propose-update` brings a new upstream release into Fedora rawhide.
+- `packit propose-update` brings a new upstream release into Fedora rawhide.
   For more info, please [check out the documentation](https://packit.dev/docs/cli/propose-update/).
 
-* `packit watch-releases` listens to github events for new upstream releases.
+- `packit watch-releases` listens to github events for new upstream releases.
   If an upstream project uses packit, it would bring the upstream release into
   Fedora, the same way as `packit propose-update`. Please make sure that your
   upstream project is set up using
   [github2fedmsg](https://apps.fedoraproject.org/github2fedmsg/).
```

### Comparing `packitos-0.8.1/CONTRIBUTING.md` & `packitos-0.9.0/CONTRIBUTING.md`

 * *Files 8% similar despite different names*

```diff
@@ -4,21 +4,23 @@
 
 The following is a set of guidelines for contributing to `packit`.
 Use your best judgement, and feel free to propose changes to this document in a pull request.
 
 By contributing to this project you agree to the Developer Certificate of Origin (DCO). This document is a simple statement that you, as a contributor, have the legal right to submit the contribution. See the [DCO](DCO) file for details.
 
 ## Reporting Bugs
+
 Before creating bug reports, please check a [list of known issues](https://github.com/packit-service/packit/issues) to see
 if the problem has already been reported (or fixed in a master branch).
 
 If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/packit-service/packit/issues/new).
 Be sure to include a **descriptive title and a clear description**. Ideally, please provide:
- * version of packit you are using (`rpm -q packit` or `pip3 freeze | grep packitos`)
- * the command you executed and a debug output (using option `--debug`)
+
+- version of packit you are using (`rpm -q packit` or `pip3 freeze | grep packitos`)
+- the command you executed and a debug output (using option `--debug`)
 
 If possible, add a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.
 
 **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.
 You can also comment on the closed issue to indicate that upstream should provide a new release with a fix.
 
 ### Suggesting Enhancements
@@ -34,57 +36,57 @@
 
 Please take a few minutes to read GitHub's guide on [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).
 It's a quick read, and it's a great way to introduce yourself to how things work behind the scenes in open-source projects.
 
 ### Dependencies
 
 If you are introducing a new dependency, please make sure it's added to:
- * [setup.cfg](setup.cfg)
+
+- [setup.cfg](setup.cfg)
 
 ### Documentation
 
-If you want to update documentation, find corresponding file in [docs](/docs) folder.
+If you want to update documentation, create a PR against [packit.dev](https://github.com/packit-service/packit.dev).
 
 #### Changelog
 
 When you are contributing to changelog, please follow these suggestions:
 
-* The changelog is meant to be read by everyone. Imagine that an average user
+- The changelog is meant to be read by everyone. Imagine that an average user
   will read it and should understand the changes.
-* Every line should be a complete sentence. Either tell what is the change that
+- Every line should be a complete sentence. Either tell what is the change that
   the tool is doing or describe it precisely:
-  * Bad: `Use search method in label regex`
-  * Good: `Packit now uses search method when...`
-* And finally, with the changelogs we are essentially selling our projects:
+  - Bad: `Use search method in label regex`
+  - Good: `Packit now uses search method when...`
+- And finally, with the changelogs we are essentially selling our projects:
   think about a situation that you met someone at a conference and you are
   trying to convince the person to use the project and that the changelog
   should help with that.
 
 ### Testing
 
 Tests are stored in [tests](/tests) directory:
 
 - `tests/unit`
-    - testing small units/parts of the code
-    - strictly offline
+  - testing small units/parts of the code
+  - strictly offline
 - `tests/integration`
-    - testing bigger parts of codebase (integration between multiple units, packit python API)
-    - mocking with [flexmock](https://github.com/bkabrda/flexmock/) instead of using [requre](https://github.com/packit-service/requre)
+  - testing bigger parts of codebase (integration between multiple units, packit python API)
+  - mocking with [flexmock](https://github.com/bkabrda/flexmock/) instead of using [requre](https://github.com/packit-service/requre)
 - `tests/functional`
-    - testing packit as a CLI
-    - be careful what you run -- no requre, no mocking
+  - testing packit as a CLI
+  - be careful what you run -- no requre, no mocking
 - `tests_recording`
-    - testing bigger parts of codebase (integration between multiple units, packit python API)
-    - use [requre](https://github.com/packit-service/requre)
-      for remote communication => offline in the CI
-    - prefer [requre](https://github.com/packit-service/requre) instead of mocking
-
-We use [Tox](https://pypi.org/project/tox) with configuration in [tox.ini](tox.ini).
+  - testing bigger parts of codebase (integration between multiple units, packit python API)
+  - use [requre](https://github.com/packit-service/requre)
+    for remote communication => offline in the CI
+  - prefer [requre](https://github.com/packit-service/requre) instead of mocking
 
 Running tests locally:
+
 ```
 make check_in_container
 ```
 
 As a CI we use [Zuul](https://softwarefactory-project.io/zuul/t/local/builds?project=packit-service/packit) with a configuration in [.zuul.yaml](.zuul.yaml).
 If you want to re-run CI/tests in a pull request, just include `recheck` in a comment.
 
@@ -106,14 +108,15 @@
 
 ### Additional configuration for development purposes
 
 #### Copr build
 
 For cases you'd like to trigger copr build in your copr project, you can configure it in
 packit configuration of your chosen package:
+
 ```
 jobs:
 - job: copr_build
   trigger: pull_request
   metadata:
     targets:
       - some_targets
@@ -121,34 +124,41 @@
     owner: <your_fedora_username>
     # (Optional) Defaults to <github_namespace>-<github_repo>
     project: some_project_name
 ```
 
 ### How to contribute code to packit
 
-1. Create a fork of the `packit` repository.
+1. Create a fork of this repository.
 2. Create a new branch just for the bug/feature you are working on.
 3. Once you have completed your work, create a Pull Request, ensuring that it meets the requirements listed below.
 
-### Requirements for Pull Requests
+### Requirements for Pull Requests (PR)
 
-* Please create Pull Requests against the `master` branch.
-* Please make sure that your code complies with [PEP8](https://www.python.org/dev/peps/pep-0008/).
-* One line should not contain more than 100 characters.
-* Make sure that new code is covered by a test case (new or existing one).
-* We don't like [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code).
-* The tests have to pass.
+- Use `pre-commit` (see [below](#checkerslintersformatters--pre-commit)).
+- Use common sense when creating commits, not too big, not too small. You can also squash them at the end of review. See [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).
+- Cover new code with a test case (new or existing one).
+- All tests have to pass.
+- Rebase against updated `master` branch before creating a PR to have linear git history.
+- Create a PR against the `master` branch.
+- The `mergit` label:
+  - Add it to instruct CI and/or reviewer that you're really done with the PR.
+  - Anyone else can add it too if they think the PR is ready to be merged.
+- Status checks SHOULD all be green.
+  - Reviewer(s) have final word and HAVE TO run tests locally if they merge a PR with a red CI.
 
 ### Checkers/linters/formatters & pre-commit
 
-To make sure our code is compliant with the above requirements, we use:
-* [black code formatter](https://github.com/ambv/black)
-* [Flake8 code linter](http://flake8.pycqa.org)
-* [mypy static type checker](http://mypy-lang.org)
+To make sure our code is [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant, we use:
+
+- [black code formatter](https://github.com/psf/black)
+- [Flake8 code linter](http://flake8.pycqa.org)
+- [mypy static type checker](http://mypy-lang.org)
 
 There's a [pre-commit](https://pre-commit.com) config file in [.pre-commit-config.yaml](.pre-commit-config.yaml).
-To [utilize pre-commit](https://pre-commit.com/#usage), install pre-commit with `pip3 install pre-commit` and then either
-* `pre-commit install` - to install pre-commit into your [git hooks](https://githooks.com). pre-commit will from now on run all the checkers/linters/formatters on every commit. If you later want to commit without running it, just run `git commit` with `-n/--no-verify`.
-* Or if you want to manually run all the checkers/linters/formatters, run `pre-commit run --all-files`.
+To [utilize pre-commit](https://pre-commit.com/#usage), install pre-commit with `pip3 install pre-commit` and then either:
+
+- `pre-commit install` - to install pre-commit into your [git hooks](https://githooks.com). pre-commit will from now on run all the checkers/linters/formatters on every commit. If you later want to commit without running it, just run `git commit` with `-n/--no-verify`.
+- Or if you want to manually run all the checkers/linters/formatters, run `pre-commit run --all-files`.
 
 Thank you for your interest!
-packit team.
+Packit team.
```

### Comparing `packitos-0.8.1/DCO` & `packitos-0.9.0/DCO`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/LICENSE` & `packitos-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/Makefile` & `packitos-0.9.0/Makefile`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,17 @@
+IMAGE=docker.io/usercont/packit
 TESTS_IMAGE=packit-tests
 TESTS_RECORDING_PATH=tests_recording
 TESTS_CONTAINER_RUN=podman run --rm -ti -v $(CURDIR):/src --security-opt label=disable $(TESTS_IMAGE)
 TESTS_TARGET := ./tests/unit ./tests/integration ./tests/functional
 
+# To build base image for packit-service-worker
+image:
+	docker build --rm -t $(IMAGE) .
+
 tests_image:
 	podman build --tag $(TESTS_IMAGE) -f Dockerfile.tests .
 	sleep 2
 
 tests_image_remove:
 	podman rmi $(TESTS_IMAGE)
```

### Comparing `packitos-0.8.1/PKG-INFO` & `packitos-0.9.0/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: packitos
-Version: 0.8.1
+Version: 0.9.0
 Summary: A set of tools to integrate upstream open source projects into Fedora operating system.
 Home-page: https://github.com/packit-service/packit
 Author: Red Hat
 Author-email: user-cont-team@redhat.com
 License: MIT
 Description: [![Build Status](https://zuul-ci.org/gated.svg)](https://softwarefactory-project.io/zuul/t/local/builds?project=packit-service/packit)
         
@@ -17,56 +17,54 @@
         You can use packit to continously build your upstream project in Fedora.
         With packit you can create SRPMs, open pull requests in dist-git, submit koji builds and even
         create bodhi updates, effectively replacing the whole Fedora packaging workflow.
         
         ## Plan and current status
         
         We are working on two things now:
-         1. Packit as a tool - a standalone CLI tool which you can install from Fedora
+        
+        1.  Packit as a tool - a standalone CLI tool which you can install from Fedora
             repositories and use easily.
-         2. Packit service - A service offering built on top of packit tool. Our
+        2.  Packit service - A service offering built on top of packit tool. Our
             expectation is that you would add packit service into your Github
             repository and it would start handling things automatically: opening pull
             requests on dist-git, building packages, creating updates, ...
         
         For the run-down of the planned work, please see the task-list below.
         
-        
-        * [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
-          * [x] Bring new upstream releases into Fedora rawhide as dist-git pull
+        - [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
+          - [x] Bring new upstream releases into Fedora rawhide as dist-git pull
                 requests. ([propose-update](https://packit.dev/docs/cli/propose-update/) command included in 0.1.0 release)
-          * [x] Build the change once it's merged. #137
-          * [x] Send new downstream changes back to upstream. (so the spec files are in
+          - [x] Build the change once it's merged. #137
+          - [x] Send new downstream changes back to upstream. (so the spec files are in
                 sync) #145
-          * [x] Packit can create bodhi updates. #139
-          * [x] Ability to propose updates also to stable releases of Fedora.
-          * [x] Create SRPMs from the upstream repository
-          * [x] Build RPMs in COPR and integrate the results into Github.
-        * [ ] source-git
-          * [x] Packit can create a SRPM from a source-git repo.
-          * [ ] You can release to rawhide from source-git using packit.
-          * [ ] Packit can create a source-git repository.
-          * [ ] Packit helps developers with their source-git repositories.
-        * [ ] Packit as a service
-          * [x] Packit reacts to Github webhooks.
-          * [x] Have a Github app for packit.
-            * [ ] Github app is on Marketplace.
-          * [ ] Packit service is deployed and usable by anyone.
-        
+          - [x] Packit can create bodhi updates. #139
+          - [x] Ability to propose updates also to stable releases of Fedora.
+          - [x] Create SRPMs from the upstream repository
+          - [x] Build RPMs in COPR and integrate the results into Github.
+        - [ ] source-git
+          - [x] Packit can create a SRPM from a source-git repo.
+          - [ ] You can release to rawhide from source-git using packit.
+          - [ ] Packit can create a source-git repository.
+          - [ ] Packit helps developers with their source-git repositories.
+        - [x] Packit as a service
+          - [x] Packit reacts to Github webhooks.
+          - [x] Have a Github app for packit.
+            - [x] Github app is on Marketplace.
+          - [x] Packit service is deployed and usable by anyone.
         
         ## Workflows covered by packit
         
         This list contains workflows covered by packit tool and links to the documentation.
         
-        * [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
-        * [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
-        * [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
-        * [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
-        * [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
-        
+        - [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
+        - [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
+        - [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
+        - [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
+        - [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
         
         ## Configuration
         
         Configuration file for packit is described [here](http://packit.dev/docs/configuration/).
         
         TL;DR
         
@@ -74,14 +72,17 @@
         specfile_path: packit.spec
         synced_files:
           - packit.spec
         upstream_package_name: packitos
         downstream_package_name: packit
         ```
         
+        ## User configuration file
+        
+        User configuration file for packit is described [here](http://packit.dev/docs/configuration/#user-configuration-file).
         
         ## Requirements
         
         Packit is written in python 3 and is supported only on 3.6 and later.
         
         When packit interacts with dist-git, it uses `fedpkg`, we suggest installing it:
         
@@ -107,15 +108,14 @@
         
         You can also install packit from master branch, if you are brave enough:
         
         ```
         $ pip3 install --user git+https://github.com/packit-service/packit.git
         ```
         
-        
         ### Run from git directly:
         
         You don't need need to install packit to try it out. You can run it directly
         from git (if you have all the dependencies installed):
         
         ```
         $ python3 -m packit.cli.packit_base --help
@@ -123,29 +123,28 @@
         
         Options:
           -d, --debug
           -h, --help         Show this message and exit.
         ...
         ```
         
-        
         ## Who is interested
         
-        * Identity team (@pvoborni)
-        * Plumbers - Source Git (@msekletar @lnykryn)
-        * shells (@siteshwar)
-        * python-operator-courier (Ralph Bean)
-        * @thrix
-        * youtube-dl (Till Mass)
-        * [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
-        * ABRT
-        * OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
-        * CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
-        * cockpit (@martinpitt)
-        * iptables (@jsynacek)
+        - Identity team (@pvoborni)
+        - Plumbers - Source Git (@msekletar @lnykryn)
+        - shells (@siteshwar)
+        - python-operator-courier (Ralph Bean)
+        - @thrix
+        - youtube-dl (Till Mass)
+        - [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
+        - ABRT
+        - OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
+        - CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
+        - cockpit (@martinpitt)
+        - iptables (@jsynacek)
         
         For the up to date list of projects which are using packit, [click here](https://github.com/packit-service/research/blob/master/onboard/status.md).
         
         ## Logo design
         
         Created by `Marián Mrva` - [@surfer19](https://github.com/surfer19)
         
@@ -153,14 +152,17 @@
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
 Classifier: Topic :: Software Development
 Classifier: Topic :: Utilities
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 Provides-Extra: testing
```

### Comparing `packitos-0.8.1/README.md` & `packitos-0.9.0/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -9,56 +9,54 @@
 You can use packit to continously build your upstream project in Fedora.
 With packit you can create SRPMs, open pull requests in dist-git, submit koji builds and even
 create bodhi updates, effectively replacing the whole Fedora packaging workflow.
 
 ## Plan and current status
 
 We are working on two things now:
- 1. Packit as a tool - a standalone CLI tool which you can install from Fedora
+
+1.  Packit as a tool - a standalone CLI tool which you can install from Fedora
     repositories and use easily.
- 2. Packit service - A service offering built on top of packit tool. Our
+2.  Packit service - A service offering built on top of packit tool. Our
     expectation is that you would add packit service into your Github
     repository and it would start handling things automatically: opening pull
     requests on dist-git, building packages, creating updates, ...
 
 For the run-down of the planned work, please see the task-list below.
 
-
-* [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
-  * [x] Bring new upstream releases into Fedora rawhide as dist-git pull
+- [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
+  - [x] Bring new upstream releases into Fedora rawhide as dist-git pull
         requests. ([propose-update](https://packit.dev/docs/cli/propose-update/) command included in 0.1.0 release)
-  * [x] Build the change once it's merged. #137
-  * [x] Send new downstream changes back to upstream. (so the spec files are in
+  - [x] Build the change once it's merged. #137
+  - [x] Send new downstream changes back to upstream. (so the spec files are in
         sync) #145
-  * [x] Packit can create bodhi updates. #139
-  * [x] Ability to propose updates also to stable releases of Fedora.
-  * [x] Create SRPMs from the upstream repository
-  * [x] Build RPMs in COPR and integrate the results into Github.
-* [ ] source-git
-  * [x] Packit can create a SRPM from a source-git repo.
-  * [ ] You can release to rawhide from source-git using packit.
-  * [ ] Packit can create a source-git repository.
-  * [ ] Packit helps developers with their source-git repositories.
-* [ ] Packit as a service
-  * [x] Packit reacts to Github webhooks.
-  * [x] Have a Github app for packit.
-    * [ ] Github app is on Marketplace.
-  * [ ] Packit service is deployed and usable by anyone.
-
+  - [x] Packit can create bodhi updates. #139
+  - [x] Ability to propose updates also to stable releases of Fedora.
+  - [x] Create SRPMs from the upstream repository
+  - [x] Build RPMs in COPR and integrate the results into Github.
+- [ ] source-git
+  - [x] Packit can create a SRPM from a source-git repo.
+  - [ ] You can release to rawhide from source-git using packit.
+  - [ ] Packit can create a source-git repository.
+  - [ ] Packit helps developers with their source-git repositories.
+- [x] Packit as a service
+  - [x] Packit reacts to Github webhooks.
+  - [x] Have a Github app for packit.
+    - [x] Github app is on Marketplace.
+  - [x] Packit service is deployed and usable by anyone.
 
 ## Workflows covered by packit
 
 This list contains workflows covered by packit tool and links to the documentation.
 
-* [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
-* [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
-* [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
-* [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
-* [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
-
+- [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
+- [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
+- [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
+- [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
+- [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
 
 ## Configuration
 
 Configuration file for packit is described [here](http://packit.dev/docs/configuration/).
 
 TL;DR
 
@@ -66,14 +64,17 @@
 specfile_path: packit.spec
 synced_files:
   - packit.spec
 upstream_package_name: packitos
 downstream_package_name: packit
 ```
 
+## User configuration file
+
+User configuration file for packit is described [here](http://packit.dev/docs/configuration/#user-configuration-file).
 
 ## Requirements
 
 Packit is written in python 3 and is supported only on 3.6 and later.
 
 When packit interacts with dist-git, it uses `fedpkg`, we suggest installing it:
 
@@ -99,15 +100,14 @@
 
 You can also install packit from master branch, if you are brave enough:
 
 ```
 $ pip3 install --user git+https://github.com/packit-service/packit.git
 ```
 
-
 ### Run from git directly:
 
 You don't need need to install packit to try it out. You can run it directly
 from git (if you have all the dependencies installed):
 
 ```
 $ python3 -m packit.cli.packit_base --help
@@ -115,28 +115,27 @@
 
 Options:
   -d, --debug
   -h, --help         Show this message and exit.
 ...
 ```
 
-
 ## Who is interested
 
-* Identity team (@pvoborni)
-* Plumbers - Source Git (@msekletar @lnykryn)
-* shells (@siteshwar)
-* python-operator-courier (Ralph Bean)
-* @thrix
-* youtube-dl (Till Mass)
-* [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
-* ABRT
-* OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
-* CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
-* cockpit (@martinpitt)
-* iptables (@jsynacek)
+- Identity team (@pvoborni)
+- Plumbers - Source Git (@msekletar @lnykryn)
+- shells (@siteshwar)
+- python-operator-courier (Ralph Bean)
+- @thrix
+- youtube-dl (Till Mass)
+- [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
+- ABRT
+- OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
+- CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
+- cockpit (@martinpitt)
+- iptables (@jsynacek)
 
 For the up to date list of projects which are using packit, [click here](https://github.com/packit-service/research/blob/master/onboard/status.md).
 
 ## Logo design
 
 Created by `Marián Mrva` - [@surfer19](https://github.com/surfer19)
```

### Comparing `packitos-0.8.1/Vagrantfile` & `packitos-0.9.0/Vagrantfile`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/ci.fmf` & `packitos-0.9.0/ci.fmf`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/.DS_Store` & `packitos-0.9.0/design/export/.DS_Store`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-dark.png` & `packitos-0.9.0/design/export/logo-dark.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-extended.jpg` & `packitos-0.9.0/design/export/logo-extended.jpg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-extended.png` & `packitos-0.9.0/design/export/logo-extended.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-extended.svg` & `packitos-0.9.0/design/export/logo-extended.svg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-guideline.pdf` & `packitos-0.9.0/design/export/logo-guideline.pdf`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-no-borders.jpg` & `packitos-0.9.0/design/export/logo-no-borders.jpg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-no-borders.png` & `packitos-0.9.0/design/export/logo-no-borders.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-square-small-borders.jpg` & `packitos-0.9.0/design/export/logo-square-small-borders.jpg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-square-small-borders.png` & `packitos-0.9.0/design/export/logo-square-small-borders.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-text.jpg` & `packitos-0.9.0/design/export/logo-text.jpg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-text.png` & `packitos-0.9.0/design/export/logo-text.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-text.svg` & `packitos-0.9.0/design/export/logo-text.svg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo-white.png` & `packitos-0.9.0/design/export/logo-white.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo.png` & `packitos-0.9.0/design/export/logo.png`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/export/logo.svg` & `packitos-0.9.0/design/export/logo.svg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/design/logo-packit.sketch` & `packitos-0.9.0/design/logo-packit.sketch`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/files/zuul-pre-commit.yaml` & `packitos-0.9.0/files/zuul-pre-commit.yaml`

 * *Files 2% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 ---
 - name: Run pre-commit
   hosts: all
   tasks:
-  - include_tasks: tasks/zuul-project-setup.yaml
-  - name: Install git
-    dnf:
-      name:
-      - git-core
-      - python36
-    become: true
-  - name: Install pre-commit PyPI package
-    pip:
-      name: pre-commit
-    become: true
-    tags:
-    - stop-layering
+    - include_tasks: tasks/zuul-project-setup.yaml
+    - name: Install git
+      dnf:
+        name:
+          - git-core
+          - python36
+      become: true
+    - name: Install pre-commit PyPI package
+      pip:
+        name: pre-commit
+      become: true
+      tags:
+        - stop-layering
 
-  - name: Install pre-commit for the repo
-    command: pre-commit install
-    args:
-      chdir: "{{ project_dir }}"
-    become: true
+    - name: Install pre-commit for the repo
+      command: pre-commit install
+      args:
+        chdir: "{{ project_dir }}"
+      become: true
 
-  - name: Run it
-    command: pre-commit run --all-files
-    args:
-      chdir: "{{ project_dir }}"
+    - name: Run it
+      command: pre-commit run --all-files
+      args:
+        chdir: "{{ project_dir }}"
```

### Comparing `packitos-0.8.1/packit/__init__.py` & `packitos-0.9.0/packit/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/actions.py` & `packitos-0.9.0/packit/actions.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/api.py` & `packitos-0.9.0/packit/api.py`

 * *Files 2% similar despite different names*

```diff
@@ -28,25 +28,29 @@
 import logging
 import os
 import sys
 from datetime import datetime
 from pathlib import Path
 from typing import Sequence, Callable, List, Tuple, Dict, Iterable, Optional
 
+from ogr.abstract import PullRequest
 from tabulate import tabulate
 
 from packit.actions import ActionName
 from packit.config import Config, PackageConfig
 from packit.constants import SYNCING_NOTE
 from packit.copr_helper import CoprHelper
 from packit.distgit import DistGit
 from packit.exceptions import (
     PackitException,
     PackitSRPMException,
     PackitSRPMNotFoundException,
+    PackitRPMException,
+    PackitRPMNotFoundException,
+    PackitCoprException,
 )
 from packit.local_project import LocalProject
 from packit.status import Status
 from packit.sync import sync_files
 from packit.upstream import Upstream
 from packit.utils import assert_existence, get_packit_version
 
@@ -101,15 +105,15 @@
     def sync_pr(self, pr_id, dist_git_branch: str, upstream_version: str = None):
         assert_existence(self.dg.local_project)
         # do not add anything between distgit clone and saving gpg keys!
         self.up.allowed_gpg_keys = self.dg.get_allowed_gpg_keys_from_downstream_config()
 
         self.up.run_action(actions=ActionName.pre_sync)
 
-        self.up.checkout_pr(pr_id=pr_id)
+        self.up.local_project.checkout_pr(pr_id=pr_id)
         self.dg.check_last_commit()
 
         local_pr_branch = f"pull-request-{pr_id}-sync"
         # fetch and reset --hard upstream/$branch?
         self.dg.create_branch(
             dist_git_branch,
             base=f"remotes/origin/{dist_git_branch}",
@@ -123,15 +127,15 @@
         self.dg.checkout_branch(local_pr_branch)
 
         if self.up.with_action(action=ActionName.create_patches):
             patches = self.up.create_patches(
                 upstream=upstream_version,
                 destination=str(self.dg.absolute_specfile_dir),
             )
-            self.dg.add_patches_to_specfile(patches)
+            self.dg.specfile_add_patches(patches)
 
         description = (
             f"Upstream pr: {pr_id}\n"
             f"Upstream commit: {self.up.local_project.commit_hexsha}\n"
         )
 
         self._handle_sources(add_new_sources=True, force_new_sources=False)
@@ -155,28 +159,35 @@
         dist_git_branch: str,
         use_local_content=False,
         version: str = None,
         force_new_sources=False,
         upstream_ref: str = None,
         create_pr: bool = True,
         force: bool = False,
-    ):
+    ) -> Optional[PullRequest]:
         """
         Update given package in Fedora
 
         :param dist_git_branch: branch in dist-git
         :param use_local_content: don't check out anything
         :param version: upstream version to update in Fedora
         :param force_new_sources: don't check the lookaside cache and perform new-sources
         :param upstream_ref: for a source-git repo, use this ref as the latest upstream commit
         :param create_pr: create a pull request if set to True
         :param force: ignore changes in the git index
+
+        :return created PullRequest if create_pr is True, else None
         """
         assert_existence(self.up.local_project)
         assert_existence(self.dg.local_project)
+        if self.dg.is_dirty():
+            raise PackitException(
+                f"The distgit repository {self.dg.local_project.working_dir} is dirty."
+                f"This is not supported."
+            )
         if not force and self.up.is_dirty() and not use_local_content:
             raise PackitException(
                 "The repository is dirty, will not discard the changes. Use --force to bypass."
             )
         # do not add anything between distgit clone and saving gpg keys!
         self.up.allowed_gpg_keys = self.dg.get_allowed_gpg_keys_from_downstream_config()
 
@@ -246,15 +257,15 @@
                 sync_files(raw_sync_files)
                 if upstream_ref:
                     if self.up.with_action(action=ActionName.create_patches):
                         patches = self.up.create_patches(
                             upstream=upstream_ref,
                             destination=str(self.dg.absolute_specfile_dir),
                         )
-                        self.dg.add_patches_to_specfile(patches)
+                        self.dg.specfile_add_patches(patches)
 
                 self._handle_sources(
                     add_new_sources=True, force_new_sources=force_new_sources
                 )
 
             # when the action is defined, we still need to copy the files
             if self.up.has_action(action=ActionName.prepare_files):
@@ -262,27 +273,30 @@
                     Path(self.up.local_project.working_dir),
                     Path(self.dg.local_project.working_dir),
                 )
                 sync_files(raw_sync_files)
 
             self.dg.commit(title=f"{full_version} upstream release", msg=description)
 
+            new_pr = None
             if create_pr:
-                self.push_and_create_pr(
+                new_pr = self.push_and_create_pr(
                     pr_title=f"Update to upstream release {full_version}",
                     pr_description=description,
                     dist_git_branch=dist_git_branch,
                 )
             else:
                 self.dg.push(refspec=f"HEAD:{dist_git_branch}")
         finally:
             if not use_local_content:
                 self.up.local_project.git_repo.git.checkout(current_up_branch)
             self.dg.refresh_specfile()
 
+        return new_pr
+
     def sync_from_downstream(
         self,
         dist_git_branch: str,
         upstream_branch: str,
         no_pr: bool = False,
         fork: bool = True,
         remote_name: str = None,
@@ -356,18 +370,18 @@
                 source_branch=source_branch,
                 target_branch=upstream_branch,
                 fork_username=fork_username,
             )
 
     def push_and_create_pr(
         self, pr_title: str, pr_description: str, dist_git_branch: str
-    ):
+    ) -> PullRequest:
         # the branch may already be up, let's push forcefully
         self.dg.push_to_fork(self.dg.local_project.ref, force=True)
-        self.dg.create_pull(
+        return self.dg.create_pull(
             pr_title,
             pr_description,
             source_branch=self.dg.local_project.ref,
             target_branch=dist_git_branch,
         )
 
     def _handle_sources(self, add_new_sources, force_new_sources):
@@ -486,14 +500,47 @@
 
         if not srpm_path.exists():
             raise PackitSRPMNotFoundException(
                 f"SRPM was created successfully, but can't be found at {srpm_path}"
             )
         return srpm_path
 
+    def create_rpms(self, upstream_ref: str = None, rpm_dir: str = None) -> List[Path]:
+        """
+        Create rpms from the upstream repo
+
+        :param upstream_ref: git ref to upstream commit
+        :param rpm_dir: path to the directory where the rpm is meant to be placed
+        :return: a path to the rpm
+        """
+        self.up.run_action(actions=ActionName.post_upstream_clone)
+
+        try:
+            self.up.prepare_upstream_for_srpm_creation(upstream_ref=upstream_ref)
+        except Exception as ex:
+            raise PackitRPMException(
+                f"Preparing of the upstream to the RPM build failed: {ex}"
+            ) from ex
+
+        try:
+            rpm_paths = self.up.create_rpms(rpm_dir=rpm_dir)
+        except PackitRPMException:
+            raise
+        except Exception as ex:
+            raise PackitRPMException(
+                f"An unexpected error occurred when creating the RPMs: {ex}"
+            ) from ex
+
+        for rpm_path in rpm_paths:
+            if not rpm_path.exists():
+                raise PackitRPMNotFoundException(
+                    f"RPM was created successfully, but can't be found at {rpm_path}"
+                )
+        return rpm_paths
+
     @staticmethod
     async def status_get_downstream_prs(status) -> List[Tuple[int, str, str]]:
         try:
             await asyncio.sleep(0)
             return status.get_downstream_prs()
         except Exception as exc:
             # https://github.com/packit-service/ogr/issues/67 work-around
@@ -542,15 +589,15 @@
             await asyncio.sleep(0)
             return status.get_updates()
         except Exception as exc:
             logger.error(f"Failed when getting Bodhi updates: {exc}")
             return []
 
     @staticmethod
-    async def status_main(status: Status) -> Tuple:
+    async def status_main(status: Status) -> List:
         """
         Schedule repository data retrieval calls concurrently.
         :param status: status of the package
         :return: awaitable tasks
         """
         res = await asyncio.gather(
             PackitAPI.status_get_downstream_prs(status),
@@ -633,41 +680,49 @@
     def run_copr_build(
         self,
         project: str,
         chroots: List[str],
         owner: str = None,
         description: str = None,
         instructions: str = None,
+        upstream_ref: str = None,
     ) -> Tuple[int, str]:
         """
         Submit a build to copr build system using an SRPM using the current checkout.
 
         :param project: name of the copr project to build
                         inside (defaults to something long and ugly)
         :param chroots: a list of COPR chroots (targets) e.g. fedora-rawhide-x86_64
         :param owner: defaults to username from copr config file
         :param description: description of the project
         :param instructions: installation instructions for the project
+        :param upstream_ref: git ref to upstream commit
         :return: id of the created build and url to the build web page
         """
-        srpm_path = self.create_srpm(srpm_dir=self.up.local_project.working_dir)
+        srpm_path = self.create_srpm(
+            upstream_ref=upstream_ref, srpm_dir=self.up.local_project.working_dir
+        )
+
+        owner = owner or self.copr_helper.configured_owner
+        if not owner:
+            raise PackitCoprException(
+                f"Copr owner not set. Use Copr config file or `--owner` when calling packit CLI."
+            )
 
         self.copr_helper.create_copr_project_if_not_exists(
             project=project,
             chroots=chroots,
             owner=owner,
             description=description,
             instructions=instructions,
         )
-        logger.debug(
-            f"owner={owner if owner else 'value from the config file will be used'}, "
-            f"project={project}, path={srpm_path}"
-        )
+        logger.debug(f"owner={owner}, project={project}, path={srpm_path}")
+
         build = self.copr_helper.copr_client.build_proxy.create_from_file(
-            owner, project, srpm_path
+            ownername=owner, projectname=project, path=srpm_path
         )
         return build.id, self.copr_helper.copr_web_build_url(build)
 
     def watch_copr_build(
         self, build_id: int, timeout: int, report_func: Callable = None
     ) -> str:
         """ returns copr build state """
```

### Comparing `packitos-0.8.1/packit/base_git.py` & `packitos-0.9.0/packit/base_git.py`

 * *Files 13% similar despite different names*

```diff
@@ -15,16 +15,17 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-import logging
+
 import shlex
+from logging import getLogger
 from pathlib import Path
 from typing import Optional, Callable, List, Tuple, Iterable, Dict
 
 import git
 from git import PushInfo
 
 from packit.actions import ActionName
@@ -32,15 +33,15 @@
 from packit.config import Config, PackageConfig, RunCommandType
 from packit.exceptions import PackitException
 from packit.local_project import LocalProject
 from packit.security import CommitVerifier
 from packit.specfile import Specfile
 from packit.utils import cwd
 
-logger = logging.getLogger(__name__)
+logger = getLogger(__name__)
 
 
 class PackitRepositoryBase:
     # mypy complains when this is a property
     local_project: LocalProject
 
     def __init__(self, config: Config, package_config: PackageConfig) -> None:
@@ -309,58 +310,27 @@
         for cmd in commands_to_run:
             outputs.append(
                 self.command_handler.run_command(cmd, return_output=True, env=env)
             )
         logger.debug(f"Action command output: {outputs}")
         return outputs
 
-    def add_patches_to_specfile(self, patch_list: List[Tuple[str, str]]) -> None:
+    def specfile_add_patches(self, patch_list: List[Tuple[Path, str]]) -> None:
         """
         Add the given list of (patch_name, msg) to the specfile.
 
-        :param patch_list: [(patch_name, msg)] if None, the patches will be generated
+        :param patch_list: [(patch_name, msg)]
         """
-        logger.debug(f"About to add patches {patch_list} to specfile")
         if not patch_list:
             return
 
-        with open(file=str(self.absolute_specfile_path), mode="r+") as spec_file:
-            last_source_position = None
-            line = spec_file.readline()
-            while line:
-                if line.startswith("Patch"):
-                    raise PackitException(
-                        "This specfile already contains patches, please remove them."
-                    )
-                if line.startswith("Source"):
-                    last_source_position = spec_file.tell()
-                line = spec_file.readline()
-
-            if not last_source_position:
-                raise PackitException(
-                    "Cannot find a place to put patches in the specfile."
-                )
+        self.specfile.remove_applied_patches()
+        self.specfile.add_patches(patch_list)
+        self.specfile.ensure_pnum()
 
-            spec_file.seek(last_source_position)
-            rest_of_the_file = spec_file.read()
-            spec_file.seek(last_source_position)
-
-            spec_file.write("\n\n# PATCHES FROM SOURCE GIT:\n")
-            for i, (patch, msg) in enumerate(patch_list):
-                commented_msg = "\n# " + "\n# ".join(msg.split("\n")) + "\n"
-                spec_file.write(commented_msg)
-                spec_file.write(f"Patch{i + 1:04d}: {patch}\n")
-
-            spec_file.write("\n\n")
-            spec_file.write(rest_of_the_file)
-
-        logger.info(
-            f"Patches ({len(patch_list)}) added to the specfile ({self.absolute_specfile_path})"
-        )
-        self.refresh_specfile()
         self.local_project.git_repo.index.write()
 
     def get_project_url_from_distgit_spec(self) -> Optional[str]:
         """
         Parse spec file and return value of URL
         """
         # consider using rebase-helper for this: SpecFile.download_remote_sources
```

### Comparing `packitos-0.8.1/packit/cli/__init__.py` & `packitos-0.9.0/packit/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/build.py` & `packitos-0.9.0/packit/cli/build.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/copr_build.py` & `packitos-0.9.0/packit/cli/copr_build.py`

 * *Files 9% similar despite different names*

```diff
@@ -36,51 +36,71 @@
 @click.option(
     "--owner",
     help="Copr user, owner of the project. (defaults to username from copr config)",
 )
 @click.option(
     "--project",
     help="Project name to build in. Will be created if does not exist. "
-    "(defaults to 'packit-cli-{repo_name}-{branch/commit}')",
+    "(defaults to the first found project value in the config file or "
+    "'packit-cli-{repo_name}-{branch/commit}')",
 )
 @click.option(
     "--targets",
     help="Comma separated list of chroots to build in. (defaults to 'fedora-rawhide-x86_64')",
     default="fedora-rawhide-x86_64",
 )
 @click.option(
     "--description", help="Description of the project to build in.", default=None
 )
 @click.option(
     "--instructions",
     help="Installation instructions for the project to build in.",
     default=None,
 )
+@click.option(
+    "--upstream-ref",
+    default=None,
+    help="Git ref of the last upstream commit in the current branch "
+    "from which packit should generate patches "
+    "(this option implies the repository is source-git).",
+)
 @click.argument("path_or_url", type=LocalProjectParameter(), default=os.path.curdir)
 @pass_config
 @cover_packit_exception
 def copr_build(
-    config, nowait, owner, project, targets, path_or_url, description, instructions
+    config,
+    nowait,
+    owner,
+    project,
+    targets,
+    description,
+    instructions,
+    upstream_ref,
+    path_or_url,
 ):
     """
     Build selected upstream project in COPR.
 
     PATH_OR_URL argument is a local path or a URL to the upstream git repository,
     it defaults to the current working directory.
     """
     api = get_packit_api(config=config, local_project=path_or_url)
-    default_project_name = f"packit-cli-{path_or_url.repo_name}-{path_or_url.ref}"
+    default_project_name = api.package_config.get_copr_build_project_value()
+
+    if not default_project_name:
+        default_project_name = f"packit-cli-{path_or_url.repo_name}-{path_or_url.ref}"
 
     targets_to_build = get_build_targets(
         *targets.split(","), default="fedora-rawhide-x86_64"
     )
 
     build_id, repo_url = api.run_copr_build(
         project=project or default_project_name,
         chroots=list(targets_to_build),
         owner=owner,
         description=description,
         instructions=instructions,
+        upstream_ref=upstream_ref,
     )
     click.echo(f"Build id: {build_id}, repo url: {repo_url}")
     if not nowait:
         api.watch_copr_build(build_id=build_id, timeout=60 * 60 * 2)
```

### Comparing `packitos-0.8.1/packit/cli/create_update.py` & `packitos-0.9.0/packit/cli/create_update.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/generate.py` & `packitos-0.9.0/packit/cli/init.py`

 * *Files 4% similar despite different names*

```diff
@@ -36,31 +36,32 @@
 from packit.config import get_context_settings
 from packit.constants import CONFIG_FILE_NAMES, PACKIT_CONFIG_TEMPLATE
 from packit.exceptions import PackitException
 
 logger = logging.getLogger(__name__)
 
 
-@click.command("generate", context_settings=get_context_settings())
+@click.command("init", context_settings=get_context_settings())
 @click.argument("path_or_url", type=LocalProjectParameter(), default=os.path.curdir)
 @click.option(
     "-f", "--force", is_flag=True, help="Reset config to default if already exists."
 )
 @cover_packit_exception
-def generate(path_or_url, force):
+def init(path_or_url, force):
     """
     Generate new packit config.
     """
+
     working_dir = Path(path_or_url.working_dir)
     config_path = get_existing_config(working_dir)
     if config_path:
         if not force:
             raise PackitException(
                 f"Packit config {config_path} already exists."
-                " If you want to regenerate it use `packit generate --force`"
+                " If you want to regenerate it use `packit init --force`"
             )
     else:
         # Use default name
         config_path = working_dir / ".packit.yaml"
 
     template_data = {
         "upstream_package_name": path_or_url.repo_name,
```

### Comparing `packitos-0.8.1/packit/cli/packit_base.py` & `packitos-0.9.0/packit/cli/packit_base.py`

 * *Files 15% similar despite different names*

```diff
@@ -24,27 +24,41 @@
 
 import click
 from pkg_resources import get_distribution
 
 from packit.cli.build import build
 from packit.cli.copr_build import copr_build
 from packit.cli.create_update import create_update
-from packit.cli.generate import generate
+from packit.cli.init import init
+from packit.cli.local_build import local_build
 from packit.cli.push_updates import push_updates
 from packit.cli.srpm import srpm
 from packit.cli.status import status
 from packit.cli.sync_from_downstream import sync_from_downstream
 from packit.cli.update import update
 from packit.config import Config, get_context_settings
 from packit.utils import set_logging
 
 logger = logging.getLogger("packit")
 
 
-@click.group("packit", context_settings=get_context_settings())
+class AliasedGroup(click.Group):
+    def get_command(self, ctx, cmd_name):
+        if cmd_name == "generate":
+            click.secho(
+                "WARNING: 'packit generate' is deprecated and it "
+                "is going to be removed. Use 'packit init' instead.",
+                fg="yellow",
+            )
+            return click.Group.get_command(self, ctx, "init")
+        else:
+            return click.Group.get_command(self, ctx, cmd_name)
+
+
+@click.group("packit", cls=AliasedGroup, context_settings=get_context_settings())
 @click.option("-d", "--debug", is_flag=True, help="Enable debug logs.")
 @click.option("--fas-user", help="Fedora Account System username.")
 @click.option("-k", "--keytab", help="Path to FAS keytab file.")
 @click.option(
     "--dry-run",
     is_flag=True,
     help="Do not perform any remote changes (pull requests or comments).",
@@ -80,11 +94,12 @@
 packit_base.add_command(sync_from_downstream)
 packit_base.add_command(build)
 packit_base.add_command(copr_build)
 packit_base.add_command(create_update)
 packit_base.add_command(push_updates)
 packit_base.add_command(srpm)
 packit_base.add_command(status)
-packit_base.add_command(generate)
+packit_base.add_command(init)
+packit_base.add_command(local_build)
 
 if __name__ == "__main__":
     packit_base()
```

### Comparing `packitos-0.8.1/packit/cli/push_updates.py` & `packitos-0.9.0/packit/cli/push_updates.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/srpm.py` & `packitos-0.9.0/packit/cli/srpm.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/status.py` & `packitos-0.9.0/packit/cli/status.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/sync_from_downstream.py` & `packitos-0.9.0/packit/cli/sync_from_downstream.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/types.py` & `packitos-0.9.0/packit/cli/types.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/update.py` & `packitos-0.9.0/packit/cli/update.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/cli/utils.py` & `packitos-0.9.0/packit/cli/utils.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/command_handler.py` & `packitos-0.9.0/packit/command_handler.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/config/__init__.py` & `packitos-0.9.0/packit/config/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,15 +1,19 @@
 from packit.config.config import (
     Config,
     RunCommandType,
     get_context_settings,
     get_default_map_from_file,
     pass_config,
 )
-from packit.config.job_config import JobConfig, JobTriggerType, JobType
+from packit.config.job_config import (
+    JobConfig,
+    JobConfigTriggerType,
+    JobType,
+)
 from packit.config.package_config import (
     PackageConfig,
     get_package_config_from_repo,
     get_local_package_config,
     parse_loaded_config,
 )
 from packit.config.sync_files_config import (
@@ -17,15 +21,15 @@
     SyncFilesItem,
     RawSyncFilesItem,
 )
 
 __all__ = [
     Config.__name__,
     JobConfig.__name__,
-    JobTriggerType.__name__,
+    JobConfigTriggerType.__name__,
     JobType.__name__,
     PackageConfig.__name__,
     RawSyncFilesItem.__name__,
     RunCommandType.__name__,
     SyncFilesConfig.__name__,
     SyncFilesItem.__name__,
     "get_context_settings",
```

### Comparing `packitos-0.8.1/packit/config/aliases.py` & `packitos-0.9.0/packit/config/aliases.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,17 +20,17 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 from typing import Dict, List, Set
 
 from packit.exceptions import PackitException
 
 ALIASES: Dict[str, List[str]] = {
-    "fedora-development": ["fedora-rawhide"],
+    "fedora-development": ["fedora-rawhide", "fedora-32"],
     "fedora-stable": ["fedora-30", "fedora-31"],
-    "fedora-all": ["fedora-rawhide", "fedora-30", "fedora-31"],
+    "fedora-all": ["fedora-rawhide", "fedora-30", "fedora-31", "fedora-32"],
 }
 ARCHITECTURE_LIST: List[str] = [
     "aarch64",
     "armhfp",
     "i386",
     "ppc64le",
     "s390x",
```

### Comparing `packitos-0.8.1/packit/config/config.py` & `packitos-0.9.0/packit/config/config.py`

 * *Files 4% similar despite different names*

```diff
@@ -127,51 +127,61 @@
         config = UserConfigSchema(strict=True).load(raw_dict).data
 
         return config
 
     @staticmethod
     def load_authentication(raw_dict):
         services = set()
+        deprecated_keys = [
+            "github_app_id",
+            "github_app_cert_path",
+            "github_token",
+            "pagure_user_token",
+            "pagure_instance_url",
+            "pagure_fork_token",
+        ]
         if "authentication" in raw_dict:
             services = get_instances_from_dict(instances=raw_dict["authentication"])
-        else:
+        elif any(key in raw_dict for key in deprecated_keys):
             logger.warning(
                 "Please, "
                 "use 'authentication' key in the user configuration "
                 "to set tokens for GitHub and Pagure. "
                 "New method supports more services and direct keys will be removed in the future.\n"
                 "Example:\n"
                 "authentication:\n"
                 "    github.com:\n"
                 "        token: GITHUB_TOKEN\n"
                 "    pagure:\n"
                 "        token: PAGURE_TOKEN\n"
                 '        instance_url: "https://src.fedoraproject.org"\n'
+                "See our documentation for more information "
+                "http://packit.dev/docs/configuration/#user-configuration-file. "
             )
             github_app_id = raw_dict.get("github_app_id")
             github_app_cert_path = raw_dict.get("github_app_cert_path")
             github_token = raw_dict.get("github_token")
             services.add(
                 GithubService(
                     token=github_token,
                     github_app_id=github_app_id,
                     github_app_private_key_path=github_app_cert_path,
                 )
             )
             pagure_user_token = raw_dict.get("pagure_user_token")
+            pagure_instance_url = raw_dict.get(
+                "pagure_instance_url", "https://src.fedoraproject.org"
+            )
             if raw_dict.get("pagure_fork_token"):
                 warnings.warn(
                     "packit no longer accepts 'pagure_fork_token'"
                     " value (https://github.com/packit-service/packit/issues/495)"
                 )
             services.add(
-                PagureService(
-                    token=pagure_user_token,
-                    instance_url="https://src.fedoraproject.org",
-                )
+                PagureService(token=pagure_user_token, instance_url=pagure_instance_url)
             )
 
         return services
 
     def _get_project(self, url: str) -> GitProject:
         try:
             project = get_project(url=url, custom_instances=self.services)
```

### Comparing `packitos-0.8.1/packit/config/job_config.py` & `packitos-0.9.0/packit/config/job_config.py`

 * *Files 10% similar despite different names*

```diff
@@ -19,78 +19,75 @@
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
 import logging
 from enum import Enum
 
-from packit.config.aliases import get_build_targets, get_branches
 from packit.exceptions import PackitConfigException
 
 logger = logging.getLogger(__name__)
 
 
 class JobType(Enum):
     """ Type of the job to execute: pick the correct handler """
 
     propose_downstream = "propose_downstream"
     check_downstream = "check_downstream"
     build = "build"
     sync_from_downstream = "sync_from_downstream"
     copr_build = "copr_build"
+    production_build = "production_build"  # koji build
     add_to_whitelist = "add_to_whitelist"
     tests = "tests"
     report_test_results = "report_test_results"
     pull_request_action = "pull_request_action"
     copr_build_finished = "copr_build_finished"
     copr_build_started = "copr_build_started"
 
 
-class JobTriggerType(Enum):
+class JobConfigTriggerType(Enum):
     release = "release"
     pull_request = "pull_request"
     commit = "commit"
-    installation = "installation"
-    testing_farm_results = "testing_farm_results"
-    comment = "comment"
 
 
 class JobConfig:
-    def __init__(self, job: JobType, trigger: JobTriggerType, metadata: dict):
-        self.job = job
-        self.trigger = trigger
-        self.metadata = metadata
+    def __init__(self, type: JobType, trigger: JobConfigTriggerType, metadata: dict):
+        self.type = type
+        self.trigger: JobConfigTriggerType = trigger
+        self.metadata: dict = metadata
 
     def __repr__(self):
         return (
-            f"JobConfig(job={self.job}, trigger={self.trigger}, meta={self.metadata})"
+            f"JobConfig(job={self.type}, trigger={self.trigger}, meta={self.metadata})"
         )
 
     @classmethod
     def get_from_dict(cls, raw_dict: dict) -> "JobConfig":
         # required to avoid cyclical imports
         from packit.schema import JobConfigSchema
 
         return JobConfigSchema(strict=True).load(raw_dict).data
 
     def __eq__(self, other: object):
         if not isinstance(other, JobConfig):
             raise PackitConfigException("Provided object is not a JobConfig instance.")
         return (
-            self.job == other.job
+            self.type == other.type
             and self.trigger == other.trigger
             and self.metadata == other.metadata
         )
 
 
 default_jobs = [
     JobConfig(
-        job=JobType.copr_build,
-        trigger=JobTriggerType.pull_request,
-        metadata={"targets": get_build_targets("fedora-stable")},
+        type=JobType.tests,
+        trigger=JobConfigTriggerType.pull_request,
+        metadata={"targets": ["fedora-stable"]},
     ),
     JobConfig(
-        job=JobType.propose_downstream,
-        trigger=JobTriggerType.release,
-        metadata={"dist-git-branch": get_branches("fedora-all")},
+        type=JobType.propose_downstream,
+        trigger=JobConfigTriggerType.release,
+        metadata={"dist-git-branch": ["fedora-all"]},
     ),
 ]
```

### Comparing `packitos-0.8.1/packit/config/package_config.py` & `packitos-0.9.0/packit/config/package_config.py`

 * *Files 20% similar despite different names*

```diff
@@ -25,22 +25,36 @@
 from pathlib import Path
 from typing import Optional, List, Dict, Union
 
 from yaml import safe_load
 
 from ogr.abstract import GitProject
 from packit.actions import ActionName
-from packit.constants import CONFIG_FILE_NAMES, PROD_DISTGIT_URL
-from packit.config.job_config import JobConfig, default_jobs
+from packit.config.job_config import JobConfig, default_jobs, JobType
 from packit.config.sync_files_config import SyncFilesConfig, SyncFilesItem
+from packit.constants import CONFIG_FILE_NAMES, PROD_DISTGIT_URL
 from packit.exceptions import PackitConfigException
 
 logger = logging.getLogger(__name__)
 
 
+class PullRequestNotificationsConfig:
+    """ Configuration of commenting on pull requests. """
+
+    def __init__(self, successful_build: bool = True):
+        self.successful_build = successful_build
+
+
+class NotificationsConfig:
+    """ Configuration of notifications. """
+
+    def __init__(self, pull_request: PullRequestNotificationsConfig):
+        self.pull_request = pull_request
+
+
 class PackageConfig:
     """
     Config class for upstream/downstream packages;
     this is the config people put in their repos
     """
 
     def __init__(
@@ -60,14 +74,15 @@
         actions: Dict[ActionName, Union[str, List[str]]] = None,
         upstream_ref: Optional[str] = None,
         allowed_gpg_keys: Optional[List[str]] = None,
         create_pr: bool = True,
         spec_source_id: str = "Source0",
         upstream_tag_template: str = "{version}",
         patch_generation_ignore_paths: List[str] = None,
+        notifications: Optional[NotificationsConfig] = None,
         **kwargs,
     ):
         self.config_file_path: Optional[str] = config_file_path
         self.specfile_path: Optional[str] = specfile_path
         self.synced_files: SyncFilesConfig = synced_files or SyncFilesConfig([])
         self.patch_generation_ignore_paths = patch_generation_ignore_paths or []
         self.jobs: List[JobConfig] = jobs or []
@@ -81,22 +96,26 @@
         # path to a local git clone of the dist-git repo; None means to clone in a tmpdir
         self.dist_git_clone_path: Optional[str] = None
         self.actions = actions or {}
         self.upstream_ref: Optional[str] = upstream_ref
         self.allowed_gpg_keys = allowed_gpg_keys
         self.create_pr: bool = create_pr
         self.spec_source_id: str = spec_source_id
+        self.notifications = notifications or NotificationsConfig(
+            pull_request=PullRequestNotificationsConfig()
+        )
 
         # command to generate a tarball from the upstream repo
         # uncommitted changes will not be present in the archive
         self.create_tarball_command: List[str] = create_tarball_command
         # command to get current version of the project
         self.current_version_command: List[str] = current_version_command or [
             "git",
             "describe",
+            "--abbrev=0",
             "--tags",
             "--match",
             "*",
         ]
         # template to create an upstream tag name (upstream may use different tagging scheme)
         self.upstream_tag_template = upstream_tag_template
 
@@ -114,24 +133,34 @@
         return (
             f"{self.dist_git_base_url}{self.dist_git_namespace}/"
             f"{self.downstream_package_name}.git"
         )
 
     @classmethod
     def get_from_dict(
-        cls, raw_dict: dict, config_file_path: str = None, repo_name: str = None
+        cls,
+        raw_dict: dict,
+        config_file_path: str = None,
+        repo_name: str = None,
+        spec_file_path: str = None,
     ) -> "PackageConfig":
         # required to avoid cyclical imports
         from packit.schema import PackageConfigSchema
 
         if config_file_path and not raw_dict.get("config_file_path", None):
             raw_dict.update(config_file_path=config_file_path)
 
         package_config = PackageConfigSchema(strict=True).load(raw_dict).data
 
+        if not getattr(package_config, "specfile_path", None):
+            if spec_file_path:
+                package_config.specfile_path = spec_file_path
+            else:
+                raise PackitConfigException("Spec file was not found!")
+
         if not getattr(package_config, "upstream_package_name", None) and repo_name:
             package_config.upstream_package_name = repo_name
 
         if not getattr(package_config, "downstream_package_name", None) and repo_name:
             package_config.downstream_package_name = repo_name
 
         if "jobs" not in raw_dict:
@@ -154,14 +183,31 @@
         ):
             files.append(
                 SyncFilesItem(src=self.config_file_path, dest=self.config_file_path)
             )
 
         return SyncFilesConfig(files)
 
+    def get_copr_build_project_value(self) -> Optional[str]:
+        projects_list = [
+            job.metadata.get("project")
+            for job in self.jobs
+            if job.type == JobType.copr_build and job.metadata.get("project")
+        ]
+        if not projects_list:
+            return None
+
+        if len(set(projects_list)) > 1:
+            logger.warning(
+                f"You have defined multiple copr projects to build in, we are going "
+                f"to pick the first one: {projects_list[0]}, reorder the job definitions"
+                f" if this is not the one you want."
+            )
+        return projects_list[0]
+
     def __eq__(self, other: object):
         if not isinstance(other, self.__class__):
             return NotImplemented
         logger.debug(f"our configuration:\n{self.__dict__}")
         logger.debug(f"the other configuration:\n{other.__dict__}")
         return (
             self.specfile_path == other.specfile_path
@@ -189,20 +235,28 @@
     try_local_dir_first=False,
     try_local_dir_last=False,
 ) -> PackageConfig:
     """
     :return: local PackageConfig if present
     """
     directories = [Path(config_dir) for config_dir in directory]
+    cwd = Path.cwd()
+
+    if try_local_dir_first and try_local_dir_last:
+        logger.error("Ambiguous usage of try_local_dir_first and try_local_dir_last")
 
     if try_local_dir_first:
-        directories.insert(0, Path.cwd())
+        if cwd in directories:
+            directories.remove(cwd)
+        directories.insert(0, cwd)
 
     if try_local_dir_last:
-        directories.append(Path.cwd())
+        if cwd in directories:
+            directories.remove(cwd)
+        directories.append(cwd)
 
     for config_dir in directories:
         for config_file_name in CONFIG_FILE_NAMES:
             config_file_name_full = config_dir / config_file_name
             if config_file_name_full.is_file():
                 logger.debug(f"Local package config found: {config_file_name_full}")
                 try:
@@ -212,69 +266,113 @@
                         f"Cannot load package config '{config_file_name_full}'."
                     )
                     raise PackitConfigException(f"Cannot load package config: {ex}.")
                 return parse_loaded_config(
                     loaded_config=loaded_config,
                     config_file_path=str(config_file_name),
                     repo_name=repo_name,
+                    spec_file_path=str(get_local_specfile_path(config_dir)),
                 )
 
             logger.debug(f"The local config file '{config_file_name_full}' not found.")
     raise PackitConfigException("No packit config found.")
 
 
 def get_package_config_from_repo(
     sourcegit_project: GitProject, ref: str
 ) -> Optional[PackageConfig]:
     for config_file_name in CONFIG_FILE_NAMES:
         try:
             config_file_content = sourcegit_project.get_file_content(
                 path=config_file_name, ref=ref
             )
+        except FileNotFoundError:
+            # do nothing
+            pass
+        else:
             logger.debug(
                 f"Found a config file '{config_file_name}' "
                 f"on ref '{ref}' "
                 f"of the {sourcegit_project.full_repo_name} repository."
             )
-        except FileNotFoundError as ex:
-            logger.debug(
-                f"The config file '{config_file_name}' "
-                f"not found on ref '{ref}' "
-                f"of the {sourcegit_project.full_repo_name} repository."
-                f"{ex!r}"
-            )
-            continue
-
-        try:
-            loaded_config = safe_load(config_file_content)
-        except Exception as ex:
-            logger.error(f"Cannot load package config '{config_file_name}'.")
-            raise PackitConfigException(f"Cannot load package config: {ex}.")
-        return parse_loaded_config(
-            loaded_config=loaded_config,
-            config_file_path=config_file_name,
-            repo_name=sourcegit_project.repo,
+            break
+    else:
+        logger.warning(
+            f"No config file ({CONFIG_FILE_NAMES}) found on ref '{ref}' "
+            f"of the {sourcegit_project.full_repo_name} repository."
         )
+        return None
 
-    logger.warning(
-        f"No config file found on ref '{ref}' "
-        f"of the {sourcegit_project.full_repo_name} repository."
+    try:
+        loaded_config = safe_load(config_file_content)
+    except Exception as ex:
+        logger.error(f"Cannot load package config {config_file_name!r}. {ex}")
+        raise PackitConfigException(
+            f"Cannot load package config {config_file_name!r}. {ex}"
+        )
+    return parse_loaded_config(
+        loaded_config=loaded_config,
+        config_file_path=config_file_name,
+        repo_name=sourcegit_project.repo,
+        spec_file_path=get_specfile_path_from_repo(sourcegit_project, ref),
     )
-    return None
 
 
 def parse_loaded_config(
-    loaded_config: dict, config_file_path: str = None, repo_name: str = None
+    loaded_config: dict,
+    config_file_path: str = None,
+    repo_name: str = None,
+    spec_file_path: str = None,
 ) -> PackageConfig:
     """Tries to parse the config to PackageConfig."""
     logger.debug(f"Package config:\n{json.dumps(loaded_config, indent=4)}")
 
     try:
         package_config = PackageConfig.get_from_dict(
             raw_dict=loaded_config,
             config_file_path=config_file_path,
             repo_name=repo_name,
+            spec_file_path=spec_file_path,
         )
         return package_config
     except Exception as ex:
         logger.error(f"Cannot parse package config. {ex}.")
         raise PackitConfigException(f"Cannot parse package config: {ex}.")
+
+
+def get_local_specfile_path(dir: Path, exclude: List[str] = None) -> Optional[Path]:
+    """
+    Get the path (relative to dir) of the local spec file if present.
+    If the spec is not found in dir directly, try to search it recursively (rglob)
+    :param dir: to find the spec file in
+    :param exclude: don't include files found in these dirs (default "tests")
+    :return: path (relative to dir) of the first found spec file
+    """
+    files = [path.relative_to(dir) for path in dir.glob("*.spec")] or [
+        path.relative_to(dir) for path in dir.rglob("*.spec")
+    ]
+
+    if len(files) > 0:
+        # Don't take files found in exclude
+        sexclude = set(exclude) if exclude else {"tests"}
+        files = [f for f in files if f.parts[0] not in sexclude]
+
+        logger.debug(f"Local spec files found: {files}. Taking: {files[0]}")
+        return files[0]
+
+    return None
+
+
+def get_specfile_path_from_repo(
+    project: GitProject, ref: str = "master"
+) -> Optional[str]:
+    """
+    Get the path of the spec file in the given repo if present.
+    :param project: GitProject
+    :param ref: git ref
+    :return: str path of the spec file or None
+    """
+    spec_files = project.get_files(ref=ref, filter_regex=r".+\.spec$")
+    if not spec_files:
+        logger.debug(f"No spec file found in {project.full_repo_name}")
+        return None
+    return spec_files[0]
```

### Comparing `packitos-0.8.1/packit/config/sync_files_config.py` & `packitos-0.9.0/packit/config/sync_files_config.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/constants.py` & `packitos-0.9.0/packit/constants.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/copr_helper.py` & `packitos-0.9.0/packit/copr_helper.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from typing import Callable, List
 
 from copr.v3 import Client as CoprClient
 from copr.v3.exceptions import CoprNoResultException, CoprException
 from munch import Munch
 
 from packit.constants import COPR2GITHUB_STATE
-from packit.exceptions import PackitCoprProjectException, PackitCoprException
+from packit.exceptions import PackitCoprProjectException
 from packit.local_project import LocalProject
 
 logger = logging.getLogger(__name__)
 
 
 class CoprHelper:
     def __init__(self, upstream_local_project: LocalProject) -> None:
@@ -50,21 +50,14 @@
         instructions: str = None,
     ) -> None:
         """
         Create a project in copr if it does not exists.
 
         Raises PackitCoprException on any problems.
         """
-        owner = owner or self.configured_owner
-
-        if not owner:
-            raise PackitCoprException(
-                f"Copr owner not set. Use Copr config file or `--owner` when calling packit CLI."
-            )
-
         try:
             copr_proj = self.copr_client.project_proxy.get(
                 ownername=owner, projectname=project
             )
             # make sure or project has chroots set correctly
             if set(copr_proj.chroot_repos.keys()) != set(chroots):
                 logger.info(f"Updating targets on project {owner}/{project}")
```

### Comparing `packitos-0.8.1/packit/distgit.py` & `packitos-0.9.0/packit/distgit.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,14 +24,15 @@
 import tempfile
 from pathlib import Path
 from typing import Optional, Sequence, List
 
 import cccolutils
 import git
 import requests
+from ogr.abstract import PullRequest
 
 from packit.base_git import PackitRepositoryBase
 from packit.config import (
     Config,
     PackageConfig,
     SyncFilesConfig,
     get_local_package_config,
@@ -164,16 +165,16 @@
         push changes to a fork of the dist-git repo; they need to be committed!
 
         :param branch_name: the branch where we push
         :param fork_remote_name: local name of the remote where we push to
         :param force: push forcefully?
         """
         logger.debug(
-            f"About to {'force ' if force else ''}push changes to branch {branch_name} "
-            f"of a fork {fork_remote_name} of the dist-git repo"
+            f"About to {'force ' if force else ''}push changes to branch {branch_name!r} "
+            f"of a fork {fork_remote_name!r} of the dist-git repo."
         )
         if fork_remote_name not in [
             remote.name for remote in self.local_project.git_repo.remotes
         ]:
             fork = self.local_project.git_project.get_fork()
             if not fork:
                 self.local_project.git_project.fork_create()
@@ -188,22 +189,22 @@
                 name=fork_remote_name, url=fork_urls["ssh"]
             )
 
         try:
             self.push(refspec=branch_name, remote_name=fork_remote_name, force=force)
         except git.GitError as ex:
             msg = (
-                f"Unable to push to remote {fork_remote_name} using branch {branch_name}, "
+                f"Unable to push to remote fork {fork_remote_name!r} using branch {branch_name!r}, "
                 f"the error is:\n{ex}"
             )
             raise PackitException(msg)
 
     def create_pull(
         self, pr_title: str, pr_description: str, source_branch: str, target_branch: str
-    ) -> None:
+    ) -> PullRequest:
         """
         Create dist-git pull request using the requested branches
         """
         logger.debug(
             "About to create dist-git pull request "
             f"from {source_branch} to {target_branch}"
         )
@@ -224,14 +225,15 @@
         except Exception as ex:
             logger.error(f"There was an error while creating the PR: {ex!r}")
             if "Pull-Request have been deactivated" in str(ex):
                 logger.info("See https://github.com/packit-service/packit/issues/328")
             raise
         else:
             logger.info(f"PR created: {dist_git_pr.url}")
+            return dist_git_pr
 
     @property
     def upstream_archive_name(self) -> str:
         """
         :return: name of the archive, e.g. sen-0.6.1.tar.gz
         """
         archive_name = self.specfile.get_archive()
```

### Comparing `packitos-0.8.1/packit/downstream_checks.py` & `packitos-0.9.0/packit/downstream_checks.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/exceptions.py` & `packitos-0.9.0/packit/exceptions.py`

 * *Files 15% similar despite different names*

```diff
@@ -77,7 +77,19 @@
 
 class PackitSRPMNotFoundException(PackitSRPMException):
     """ SRPM created but not found """
 
 
 class PackitFailedToCreateSRPMException(PackitSRPMException):
     """ Failed to create SRPM """
+
+
+class PackitRPMException(PackitException):
+    """ Problem with the RPM """
+
+
+class PackitRPMNotFoundException(PackitRPMException):
+    """ RPM created but not found """
+
+
+class PackitFailedToCreateRPMException(PackitRPMException):
+    """ Failed to create RPM """
```

### Comparing `packitos-0.8.1/packit/fed_mes_consume.py` & `packitos-0.9.0/packit/fed_mes_consume.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/fedpkg.py` & `packitos-0.9.0/packit/fedpkg.py`

 * *Files 23% similar despite different names*

```diff
@@ -19,14 +19,16 @@
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
 from pathlib import Path
 from typing import Optional
 
+from packit.exceptions import PackitCommandFailedError
+
 from packit import utils  # so we can mock utils
 from packit.utils import logger
 
 
 class FedPKG:
     """
     Part of the code is from release-bot:
@@ -77,47 +79,66 @@
             cmd.append("--scratch")
         if nowait:
             cmd.append("--nowait")
         if koji_target:
             cmd += ["--target", koji_target]
         if srpm_path:
             cmd += ["--srpm", str(srpm_path)]
-        utils.run_command_remote(
-            cmd=cmd,
-            cwd=self.directory,
-            error_message="Submission of build to koji failed.",
-            fail=True,
-        )
+
+        try:
+            utils.run_command_remote(
+                cmd=cmd,
+                cwd=self.directory,
+                error_message="Submission of build to koji failed.",
+                fail=True,
+            )
+
+        except PackitCommandFailedError as ex:
+            # fail on the fedpkg side, the build is triggered
+            if (
+                "watch_tasks() got an unexpected keyword argument 'ki_handler'"
+                in ex.stderr_output
+            ):
+                logger.info(
+                    "fedpkg build command crashed which is a known issue: "
+                    "the build is submitted in koji anyway"
+                )
+                logger.debug(ex.stdout_output)
+
+            else:
+                raise
 
     def clone(self, package_name: str, target_path: str, anonymous: bool = False):
         """
         clone a dist-git repo; this has to be done in current env
         b/c we don't have the keytab in sandbox
         """
         cmd = [self.fedpkg_exec]
         if self.fas_username:
             cmd += ["--user", self.fas_username]
         cmd += ["-q", "clone"]
         if anonymous:
             cmd += ["-a"]
         cmd += [package_name, target_path]
-        utils.run_command(cmd=cmd)
+
+        error_msg = (
+            f"Packit failed to clone the repository {package_name}; please make sure that you"
+            f"authorized to clone repositories from fedora dist-git - this may require"
+            f"SSH keys set up or Kerberos ticket being active."
+        )
+        utils.run_command(cmd=cmd, error_message=error_msg)
 
     def init_ticket(self, keytab: str = None):
         # TODO: this method has nothing to do with fedpkg, pull it out
-        if not keytab and not self.fas_username:
+        if not self.fas_username or not keytab or not Path(keytab).is_file():
             logger.info("won't be doing kinit, no credentials provided")
             return
-        if keytab and Path(keytab).is_file():
-            cmd = [
-                "kinit",
-                f"{self.fas_username}@FEDORAPROJECT.ORG",
-                "-k",
-                "-t",
-                keytab,
-            ]
-        else:
-            # there is no keytab, but user still might have active ticket - try to renew it
-            cmd = ["kinit", "-R", f"{self.fas_username}@FEDORAPROJECT.ORG"]
+        cmd = [
+            "kinit",
+            f"{self.fas_username}@FEDORAPROJECT.ORG",
+            "-k",
+            "-t",
+            keytab,
+        ]
         return utils.run_command_remote(
             cmd=cmd, error_message="Failed to init kerberos ticket:", fail=True
         )
```

### Comparing `packitos-0.8.1/packit/local_project.py` & `packitos-0.9.0/packit/local_project.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/schema.py` & `packitos-0.9.0/packit/schema.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,35 +1,66 @@
-import logging
-import typing
+# MIT License
+#
+# Copyright (c) 2018-2019 Red Hat, Inc.
+
+# Permission is hereby granted, free of charge, to any person obtaining a copy
+# of this software and associated documentation files (the "Software"), to deal
+# in the Software without restriction, including without limitation the rights
+# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
+# copies of the Software, and to permit persons to whom the Software is
+# furnished to do so, subject to the following conditions:
+#
+# The above copyright notice and this permission notice shall be included in all
+# copies or substantial portions of the Software.
+#
+# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
+# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
+# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
+# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
+# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
+# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
+# SOFTWARE.
+
+from logging import getLogger
+from typing import Dict, Any, Optional, Mapping
 
 from marshmallow import Schema, fields, post_load, pre_load, ValidationError
 from marshmallow_enum import EnumField
 
 from packit.actions import ActionName
 from packit.config import PackageConfig, Config, SyncFilesConfig
-from packit.config.job_config import JobType, JobTriggerType, JobConfig, default_jobs
+from packit.config.job_config import (
+    JobType,
+    JobConfig,
+    default_jobs,
+    JobConfigTriggerType,
+)
+from packit.config.package_config import (
+    NotificationsConfig,
+    PullRequestNotificationsConfig,
+)
 from packit.sync import SyncFilesItem
 
-logger = logging.getLogger(__name__)
+logger = getLogger(__name__)
 
 
 class FilesToSyncField(fields.Field):
     """
     Field class representing SyncFilesItem.
     Accepts str or dict  {'src': str, 'dest':str}
     """
 
-    def _serialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
+    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
         raise NotImplementedError
 
     def _deserialize(
         self,
-        value: typing.Any,
-        attr: typing.Optional[str],
-        data: typing.Optional[typing.Mapping[str, typing.Any]],
+        value: Any,
+        attr: Optional[str],
+        data: Optional[Mapping[str, Any]],
         **kwargs,
     ) -> SyncFilesItem:
         if isinstance(value, dict):
             try:
                 if not isinstance(value["src"], str):
                     raise ValidationError("src have to be str")
                 if not isinstance(value["dest"], str):
@@ -48,24 +79,24 @@
 
 
 class ActionField(fields.Field):
     """
     Field class representing Action.
     """
 
-    def _serialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
+    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
         raise NotImplementedError
 
     def _deserialize(
         self,
-        value: typing.Any,
-        attr: typing.Optional[str],
-        data: typing.Optional[typing.Mapping[ActionName, typing.Any]],
+        value: Any,
+        attr: Optional[str],
+        data: Optional[Mapping[ActionName, Any]],
         **kwargs,
-    ) -> typing.Dict:
+    ) -> Dict:
         if not isinstance(value, dict):
             raise ValidationError("Invalid data provided. dict required")
 
         self.validate_all_actions(actions=list(value))
         data = {ActionName(key): val for key, val in value.items()}
         return data
 
@@ -85,22 +116,22 @@
     """
     Field class to mark fields which wil not be processed, only generates warning.
     Can be passed additional message via additional_message parameter.
 
     :param str additional_message: additional warning message to be displayed
     """
 
-    def _serialize(self, value: typing.Any, attr: str, obj: typing.Any, **kwargs):
+    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
         raise NotImplementedError
 
     def _deserialize(
         self,
-        value: typing.Any,
-        attr: typing.Optional[str],
-        data: typing.Optional[typing.Mapping[str, typing.Any]],
+        value: Any,
+        attr: Optional[str],
+        data: Optional[Mapping[str, Any]],
         **kwargs,
     ):
         logger.warning(f"{self.name} is no longer being processed.")
         additional_message = self.metadata.get("additional_message")
         if additional_message:
             logger.warning(f"{additional_message}")
 
@@ -134,29 +165,50 @@
 
 class JobConfigSchema(Schema):
     """
     Schema for processing JobConfig config data.
     """
 
     job = EnumField(JobType, required=True)
-    trigger = EnumField(JobTriggerType, required=True)
+    trigger = EnumField(JobConfigTriggerType, required=True)
     metadata = fields.Dict(missing={})
 
     @post_load
+    def make_instance(self, data, **_):
+        type = data.pop("job")
+        return JobConfig(type=type, **data)
+
+
+class PullRequestNotificationsSchema(Schema):
+    """ Configuration of commenting on pull requests. """
+
+    successful_build = fields.Bool(default=True)
+
+    @post_load
     def make_instance(self, data, **kwargs):
-        return JobConfig(**data)
+        return PullRequestNotificationsConfig(**data)
+
+
+class NotificationsSchema(Schema):
+    """ Configuration of notifications. """
+
+    pull_request = fields.Nested(PullRequestNotificationsSchema)
+
+    @post_load
+    def make_instance(self, data, **kwargs):
+        return NotificationsConfig(**data)
 
 
 class PackageConfigSchema(Schema):
     """
     Schema for processing PackageConfig config data.
     """
 
     config_file_path = fields.String()
-    specfile_path = fields.String(required=True)
+    specfile_path = fields.String()
     downstream_package_name = fields.String()
     upstream_project_url = fields.String(missing=None)
     upstream_package_name = fields.String()
     upstream_ref = fields.String()
     upstream_tag_template = fields.String()
     dist_git_url = NotProcessedField(
         additional_message="it is generated from dist_git_base_url and downstream_package_name"
@@ -168,14 +220,15 @@
     allowed_gpg_keys = fields.List(fields.String())
     spec_source_id = fields.Method(deserialize="spec_source_id_fm")
     synced_files = fields.Nested(SyncFilesConfigSchema)
     jobs = fields.Nested(JobConfigSchema, many=True, default=default_jobs)
     actions = ActionField(default={})
     create_pr = fields.Bool(default=True)
     patch_generation_ignore_paths = fields.List(fields.String())
+    notifications = fields.Nested(NotificationsSchema)
 
     # list of deprecated keys and their replacement (new,old)
     deprecated_keys = (("upstream_package_name", "upstream_project_name"),)
 
     @pre_load
     def ordered_preprocess(self, data, **kwargs):
         data = self.rename_deprecated_keys(data, **kwargs)
@@ -200,32 +253,32 @@
                 new_key_value = data.get(new_key_name, None)
                 if not new_key_value:
                     # prio: new > old
                     data[new_key_name] = old_key_value
                 del data[old_key_name]
         return data
 
-    def specfile_path_pre(self, data, **kwargs):
+    def specfile_path_pre(self, data: Dict, **kwargs):
         """
-        Method for pre-processing specfile_path value. If is None, will try to generate from,
-        donwstream_package_name, else will keep None and generate warning.
+        Method for pre-processing specfile_path value.
+        Set it to downstream_package_name if specified, else leave unset.
 
         :param data: conf dictionary to process
         :return: processed dictionary
         """
 
         specfile_path = data.get("specfile_path", None)
         if not specfile_path:
             downstream_package_name = data.get("downstream_package_name", None)
             if downstream_package_name:
                 data["specfile_path"] = f"{downstream_package_name}.spec"
-                logger.info(f"We guess that spec file is at {specfile_path}")
+                logger.info(f"Setting specfile_path to {downstream_package_name}.spec")
             else:
                 # guess it?
-                logger.warning("Path to spec file is not set.")
+                logger.info("Neither specfile_path nor downstream_package_name set.")
         return data
 
     @post_load
     def make_instance(self, data, **kwargs):
         return PackageConfig(**data)
 
     def spec_source_id_fm(self, value):
@@ -270,9 +323,8 @@
     command_handler_work_dir = fields.String()
     command_handler_pvc_env_var = fields.String()
     command_handler_image_reference = fields.String()
     command_handler_k8s_namespace = fields.String()
 
     @post_load
     def make_instance(self, data, **kwargs):
-
         return Config(**data)
```

### Comparing `packitos-0.8.1/packit/security.py` & `packitos-0.9.0/packit/security.py`

 * *Files 5% similar despite different names*

```diff
@@ -34,81 +34,73 @@
 
 logger = logging.getLogger(__name__)
 
 
 class CommitVerifier:
     """
     Class used for verifying git commits. Uses python-gnupg for accessing the GPG binary.
-
-    Uses `gpg2` instead of the `gpg` if it exists.
     """
 
     def __init__(self, key_server: str = None) -> None:
         """
-        :param key_server: GPG key server to be used, defaults to keys.fedoraproject.org
+        :param key_server: GPG key server to be used
         """
         self._gpg: Optional[GPG] = None
-        self.key_server = key_server or "keys.fedoraproject.org"
+        if key_server:
+            self.key_servers = [key_server]
+        else:
+            self.key_servers = [
+                "keys.openpgp.org",
+                "pgp.mit.edu",
+                "keyserver.ubuntu.com",
+            ]
 
     @property
     def gpg(self) -> GPG:
         """
         gnupg.GPG instance from python-gnupg
-
-        Uses `gpg2` instead of the `gpg` if it exists.
         """
         if not self._gpg:
-            for gpg_location in ["gpg2", "gpg"]:
-                try:
-                    self._gpg = GPG(gpgbinary=gpg_location)
-                    break
-                except FileNotFoundError:
-                    continue
-            else:
-                raise PackitException("GPG binary not found.")
+            self._gpg = GPG()
         return self._gpg
 
     @property
     def _gpg_keys(self) -> ListKeys:
         """
         List of installed gpg keys
 
         (do not cache this value)
         """
         return self.gpg.list_keys()
 
     @property
-    def _gpg_fingerprints(self) -> str:
+    def _gpg_fingerprints(self) -> List[str]:
         """List of fingerprints of the saved keys"""
         return self._gpg_keys.fingerprints
 
-    def download_gpg_key_if_needed(self, key_fingerprint: str) -> None:
+    def download_gpg_key_if_needed(self, key_fingerprint: str) -> str:
         """
-        Download the gpg key from the self.key_server
-        if it is not present.
+        Download the gpg key from the self.key_servers if it is not present.
 
-        :param key_fingerprint: str (fingerprint of the gpg key)
+        :param key_fingerprint: fingerprint of the gpg key
         """
         if key_fingerprint in self._gpg_fingerprints:
-            return
+            return key_fingerprint
 
         try:
-            result = self.gpg.recv_keys(self.key_server, key_fingerprint)
-            if not result.fingerprints:
-                raise PackitException(f"Cannot receive a gpg key: {key_fingerprint}")
-
-        except ValueError as error:
-            # python-gnupg do not recognise KEY_CONSIDERED response from gpg2
-            if "KEY_CONSIDERED" not in str(error):
-                raise PackitException(
-                    f"Cannot receive a gpg key: {key_fingerprint}", error
-                )
+            for keyserver in self.key_servers:
+                logger.debug(f"Downloading {key_fingerprint} from {keyserver}")
+                result = self.gpg.recv_keys(keyserver, key_fingerprint)
+                if result.fingerprints:
+                    return result.fingerprints[0]
         except Exception as ex:
             raise PackitException(f"Cannot receive a gpg key: {key_fingerprint}", ex)
 
+        raise PackitException(f"Cannot receive a gpg key: {key_fingerprint}")
+
     def check_signature_of_commit(
         self, commit: git.Commit, possible_key_fingerprints: List[str]
     ) -> bool:
         """
         Check the validity of the commit signature
         and test if the signer is present in the provided list.
         (Commit without signature returns False.)
```

### Comparing `packitos-0.8.1/packit/status.py` & `packitos-0.9.0/packit/status.py`

 * *Files 1% similar despite different names*

```diff
@@ -80,14 +80,15 @@
         logger.debug("Dist-git branches fetched.")
         for branch in branches:
             try:
                 self.dg.create_branch(
                     branch, base=f"remotes/origin/{branch}", setup_tracking=False
                 )
                 self.dg.checkout_branch(branch)
+                self.dg.specfile.update_spec()
             except Exception as ex:
                 logger.debug(f"Branch {branch} is not present: {ex}")
                 continue
             try:
                 dg_versions[branch] = self.dg.specfile.get_version()
             except PackitException:
                 logger.debug(f"Can't figure out the version of branch: {branch}")
```

### Comparing `packitos-0.8.1/packit/sync.py` & `packitos-0.9.0/packit/sync.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit/upstream.py` & `packitos-0.9.0/packit/upstream.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,34 +15,38 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
+import datetime
 import logging
 import os
 import re
 import shutil
+from math import log10, floor
 from pathlib import Path
-from typing import Optional, List, Tuple
+from typing import Optional, List, Tuple, Union
 
 import git
 from packaging import version
 
 from packit import utils
 from packit.actions import ActionName
 from packit.base_git import PackitRepositoryBase
 from packit.config import Config, PackageConfig, SyncFilesConfig
 from packit.constants import COMMON_ARCHIVE_EXTENSIONS
 from packit.exceptions import (
     PackitException,
     PackitSRPMNotFoundException,
     PackitFailedToCreateSRPMException,
     PackitCommandFailedError,
+    PackitFailedToCreateRPMException,
+    PackitRPMNotFoundException,
 )
 from packit.local_project import LocalProject
 from packit.specfile import Specfile
 from packit.utils import is_a_git_ref, run_command, git_remote_url_to_https_url
 
 logger = logging.getLogger(__name__)
 
@@ -85,24 +89,24 @@
         return self._local_project
 
     @property
     def active_branch(self) -> str:
         return self.local_project.ref
 
     def get_commits_to_upstream(
-        self, upstream: str, add_upstream_head_commit=False
+        self, upstream: str, add_upstream_head_commit: bool = True
     ) -> List[git.Commit]:
         """
         Return the list of different commits between current branch and upstream rev/tag.
 
         Always choosing the first-parent, so we have a line/path of the commits.
         It contains merge-commits from the master and commits on top of the master.
         (e.g. commits from PR)
 
-        :param add_upstream_head_commit: bool
+        :param add_upstream_head_commit: add also upstream rev/tag commit as a first value
         :param upstream: str -- git branch or tag
         :return: list of commits (last commit on the current branch.).
         """
 
         if is_a_git_ref(repo=self.local_project.git_repo, ref=upstream):
             upstream_ref = upstream
         else:
@@ -212,29 +216,27 @@
             logger.error("there was an error while create a PR: %r", ex)
             raise
         else:
             logger.info(f"PR created: {upstream_pr.url}")
 
     def create_patches(
         self, upstream: str = None, destination: str = None
-    ) -> List[Tuple[str, str]]:
+    ) -> List[Tuple[Path, str]]:
         """
         Create patches from downstream commits.
 
         :param destination: str
         :param upstream: str -- git branch or tag
-        :return: [(patch_name, msg)] list of created patches (tuple of the file name and commit msg)
+        :return: [(patch_path, msg)] list of created patches (tuple of the file path and commit msg)
         """
 
         upstream = upstream or self.get_specfile_version()
-        commits = self.get_commits_to_upstream(upstream, add_upstream_head_commit=True)
-
         destination = destination or self.local_project.working_dir
 
-        patches_to_create = []
+        commits = self.get_commits_to_upstream(upstream, add_upstream_head_commit=True)
 
         sync_files_to_ignore = [
             str(sf.src.relative_to(self.local_project.working_dir))
             for sf in self.package_config.get_all_files_to_sync().get_raw_files_to_sync(
                 Path(self.local_project.working_dir),
                 Path(
                     # dest (downstream) is not important, we only care about src (upstream)
@@ -242,49 +244,56 @@
                 ),
             )
         ]
         files_to_ignore = (
             self.package_config.patch_generation_ignore_paths + sync_files_to_ignore
         )
 
+        patch_list = []
+        # we need to prefix patches so we can order them properly
+        # this is needed for merge commits - git orders every instance of `format-patch` call
+        commits_count = len(commits)
+        # how many digits does commits_count have?
+        order = floor(log10(commits_count)) + 1
+        patch_counter = 0  # prefix for patches so they are nicely ordered
+        # first value is upstream ref, i.e parent for the first commit we want to create patch from
         for i, commit in enumerate(commits[1:]):
-            parent = commits[i]
-
+            parent_commit = commits[i]
             git_diff_cmd = [
                 "git",
-                "diff",
-                "--patch",
-                parent.hexsha,
-                commit.hexsha,
+                "format-patch",
+                "--output-directory",
+                f"{destination}",
+                f"{parent_commit.hexsha}..{commit.hexsha}",
                 "--",
                 ".",
             ] + [f":(exclude){file_to_ignore}" for file_to_ignore in files_to_ignore]
-            diff = run_command(
+            git_format_patch_out = run_command(
                 cmd=git_diff_cmd,
                 cwd=self.local_project.working_dir,
                 output=True,
-                decode=False,
+                decode=True,
             )
 
-            if not diff:
+            # there can be multiple patches in a merge request
+            # so `git format-patch` can contain multiple files in the output
+            if git_format_patch_out:
+                for patch_file_str in git_format_patch_out.split("\n"):
+                    if not patch_file_str:
+                        continue
+                    prefix = format(patch_counter, f"0{order}")
+                    patch_file = Path(patch_file_str)
+                    patch_name = f"{prefix}-{patch_file.name}"
+                    patch_target_path = Path(destination).joinpath(patch_name)
+                    patch_file.replace(patch_target_path)
+                    msg = f"{commit.summary}\nAuthor: {commit.author.name} <{commit.author.email}>"
+                    patch_list.append((patch_target_path, msg))
+                    patch_counter += 1
+            else:
                 logger.info(f"No patch for commit: {commit.summary} ({commit.hexsha})")
-                continue
-
-            patches_to_create.append((commit, diff))
-
-        patch_list = []
-        for i, (commit, diff) in enumerate(patches_to_create):
-            patch_name = f"{i + 1:04d}-{commit.hexsha}.patch"
-            patch_path = os.path.join(destination, patch_name)
-            patch_msg = f"{commit.summary}\nAuthor: {commit.author.name} <{commit.author.email}>"
-
-            logger.debug(f"Saving patch: {patch_name}\n{patch_msg}")
-            with open(patch_path, mode="wb") as patch_file:
-                patch_file.write(diff)
-            patch_list.append((patch_name, patch_msg))
 
         return patch_list
 
     def get_latest_released_version(self) -> str:
         """
         Return version of the upstream project for the latest official release
 
@@ -307,25 +316,22 @@
 
     def get_version(self) -> str:
         """
         Return version of the latest release available: prioritize bigger from upstream
         package repositories or the version in spec
         """
         ups_ver = version.parse(self.get_latest_released_version() or "")
-        logger.debug(f"Version in upstream package repositories: {ups_ver}")
         spec_ver = version.parse(self.get_specfile_version())
-        logger.debug(f"Version in spec file: {spec_ver}")
 
         if ups_ver > spec_ver:
-            logger.warning("Version in spec file is outdated")
-            logger.info(
-                "Picking version of the latest release from the upstream registry."
-            )
+            logger.warning(f"Version '{spec_ver}' in spec file is outdated")
+            logger.info(f"Picking version '{ups_ver}' from upstream registry.")
             return str(ups_ver)
-        logger.info("Picking version found in spec file.")
+
+        logger.info(f"Picking version '{spec_ver}' found in spec file.")
         return str(spec_ver)
 
     def get_current_version(self) -> str:
         """
         Get version of the project in current state (hint `git describe`)
 
         :return: e.g. 0.1.1.dev86+ga17a559.d20190315 or 0.6.1.1.gce4d84e
@@ -335,18 +341,21 @@
         )
         if action_output:
             return action_output[-1].strip()
 
         ver = self.command_handler.run_command(
             self.package_config.current_version_command, return_output=True
         ).strip()
-        logger.debug("version = %s", ver)
-        # RPM refuses dashes in version/release
-        ver = ver.replace("-", ".")
-        logger.debug("sanitized version = %s", ver)
+        logger.debug(f"version: {ver}")
+
+        if "-" in ver:
+            # RPM refuses dashes in version/release
+            ver = ver.replace("-", ".")
+            logger.debug(f"sanitized version: {ver}")
+
         return ver
 
     def get_archive_extension(self, archive_basename: str, version: str) -> str:
         """
         Obtains archive extension from SpecFile based on basename of the archive.
         Defaults to .tar.gz if no Source corresponds to the basename.
         """
@@ -416,15 +425,15 @@
         )
         if self.package_config.create_tarball_command:
             archive_cmd = self.package_config.create_tarball_command
         else:
             archive_cmd = [
                 "git",
                 "archive",
-                "-o",
+                "--output",
                 str(relative_archive_path),
                 "--prefix",
                 f"{dir_name}/",
                 "HEAD",
             ]
         self.command_handler.run_command(archive_cmd, return_output=True, env=env)
         return archive_name
@@ -475,16 +484,47 @@
         :param archive: relative path to the archive: used as Source0
         :param version: version to set in the spec
         :param commit: commit to set in the changelog
         """
         self._fix_spec_source(archive)
         self._fix_spec_prep(version)
 
-        msg = f"Development snapshot ({commit})"
-        self.specfile.set_spec_version(version=f"{version}", changelog_entry=msg)
+        # we only care about the first number in the release
+        # so that we can re-run `packit srpm`
+        git_des_command = [
+            "git",
+            "describe",
+            "--tags",
+            "--long",
+            "--match",
+            "*",
+        ]
+        try:
+            git_des_out = run_command(git_des_command, output=True).strip()
+        except PackitCommandFailedError as ex:
+            logger.info(f"Exception while describing the repository: {ex}")
+            # probably no tags in the git repo
+            git_desc_suffix = ""
+        else:
+            # git adds various info in the output separated by -
+            # so let's just drop version and reuse everything else
+            g_desc_raw = git_des_out.rsplit("-", 2)[1:]
+            # release components are meant to be separated by ".", not "-"
+            git_desc_suffix = "." + ".".join(g_desc_raw)
+        original_release_number = self.specfile.get_release_number().split(".", 1)[0]
+        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
+        release = f"{original_release_number}.{current_time}{git_desc_suffix}"
+
+        msg = f"- Development snapshot ({commit})"
+        logger.debug(f"Setting Release in spec to {release!r}")
+        # instead of changing version, we change Release field
+        # upstream projects should take care of versions
+        self.specfile.set_spec_version(
+            version=version, release=release, changelog_entry=msg,
+        )
 
     def _fix_spec_prep(self, version):
         prep = self.specfile.spec_content.section("%prep")
         if not prep:
             logger.warning("this package doesn't have a %prep section")
             return
 
@@ -553,51 +593,50 @@
         """
         Create SRPM from the actual content of the repo
 
         :param srpm_path: path to the srpm
         :param srpm_dir: path to the directory where the srpm is meant to be placed
         :return: path to the srpm
         """
+
         if self.running_in_service():
             srpm_dir = "."
-            rpmbuild_dir = "."
-            src_dir = str(
-                self.absolute_specfile_dir.relative_to(self.local_project.working_dir)
+            rpmbuild_dir = os.path.relpath(
+                str(self.absolute_specfile_dir), self.local_project.working_dir
             )
         else:
             srpm_dir = srpm_dir or os.getcwd()
-            src_dir = rpmbuild_dir = str(self.absolute_specfile_dir)
+            rpmbuild_dir = str(self.absolute_specfile_dir)
 
         cmd = [
             "rpmbuild",
             "-bs",
             "--define",
             f"_sourcedir {rpmbuild_dir}",
             f"--define",
-            f"_srcdir {src_dir}",
+            f"_srcdir {rpmbuild_dir}",
             "--define",
             f"_specdir {rpmbuild_dir}",
             "--define",
             f"_srcrpmdir {srpm_dir}",
-            # no idea about this one, but tests were failing in tox w/o it
             "--define",
             f"_topdir {rpmbuild_dir}",
             # we also need these 3 so that rpmbuild won't create them
             "--define",
             f"_builddir {rpmbuild_dir}",
             "--define",
             f"_rpmdir {rpmbuild_dir}",
             "--define",
             f"_buildrootdir {rpmbuild_dir}",
             self.package_config.specfile_path,
         ]
         escaped_command = " ".join([f'"{cmd_part}"' for cmd_part in cmd])
         logger.debug(f"SRPM build command: {escaped_command}")
         present_srpms = set(Path(srpm_dir).glob("*.src.rpm"))
-        logger.debug("present srpms = %s", present_srpms)
+        logger.debug(f"present srpms: {present_srpms}")
         try:
             out = self.command_handler.run_command(cmd, return_output=True).strip()
         except PackitCommandFailedError as ex:
             logger.error(f"The `rpmbuild` command failed: {ex!r}")
             raise PackitFailedToCreateSRPMException(
                 f"reason:\n"
                 f"{ex}\n"
@@ -721,15 +760,15 @@
 
         :param upstream_ref: the base git ref for the source git
         """
         if self.with_action(action=ActionName.create_patches):
             patches = self.create_patches(
                 upstream=upstream_ref, destination=str(self.absolute_specfile_dir)
             )
-            self.add_patches_to_specfile(patches)
+            self.specfile_add_patches(patches)
 
     def koji_build(
         self,
         scratch: bool = False,
         nowait: bool = False,
         koji_target: Optional[str] = None,
         srpm_path: Optional[Path] = None,
@@ -762,7 +801,80 @@
             cmd,
             cwd=self.local_project.working_dir,
             output=True,
             decode=True,
             print_live=True,
         )
         return out
+
+    def create_rpms(self, rpm_dir: Union[str, Path] = None) -> List[Path]:
+        """
+        Create RPMs from the actual content of the repo.
+        :param rpm_dir: path to the directory where the rpms are meant to be placed
+        :return: paths to the RPMs
+        """
+        rpm_dir = rpm_dir or os.getcwd()
+        src_dir = rpmbuild_dir = str(self.absolute_specfile_dir)
+
+        cmd = [
+            "rpmbuild",
+            "-bb",
+            "--define",
+            f"_sourcedir {rpmbuild_dir}",
+            f"--define",
+            f"_srcdir {src_dir}",
+            "--define",
+            f"_specdir {rpmbuild_dir}",
+            "--define",
+            f"_topdir {rpmbuild_dir}",
+            "--define",
+            f"_builddir {rpmbuild_dir}",
+            "--define",
+            f"_rpmdir {rpm_dir}",
+            "--define",
+            f"_buildrootdir {rpmbuild_dir}",
+            self.package_config.specfile_path,
+        ]
+
+        escaped_command = " ".join([f'"{cmd_part}"' for cmd_part in cmd])
+        logger.debug(f"RPM build command: {escaped_command}")
+        try:
+            out = self.command_handler.run_command(cmd, return_output=True).strip()
+        except PackitCommandFailedError as ex:
+            logger.error(f"The `rpmbuild` command failed: {ex!r}")
+            raise PackitFailedToCreateRPMException(
+                f"reason:\n"
+                f"{ex}\n"
+                f"command:\n"
+                f"{escaped_command}\n"
+                f"stdout:\n"
+                f"{ex.stdout_output}\n"
+                f"stderr:\n"
+                f"{ex.stderr_output}"
+            ) from ex
+        except PackitException as ex:
+            logger.error(f"The `rpmbuild` command failed: {ex!r}")
+            raise PackitFailedToCreateRPMException(
+                f"The `rpmbuild` command failed:\n{ex}"
+            ) from ex
+
+        rpms = self._get_rpms_from_rpmbuild_output(out)
+        return [Path(rpm) for rpm in rpms]
+
+    def _get_rpms_from_rpmbuild_output(self, output: str) -> List[str]:
+        """
+        Try to find the rpm files in the `rpmbuild -bb` command output.
+
+        :param output: output of the `rpmbuild -bb` command
+        :return: the names of the RPM files
+        """
+        logger.debug(f"{output}")
+        reg = r": (.+\.rpm)"
+        logger.debug(re.findall(reg, output))
+        rpms = re.findall(reg, output)
+
+        if not rpms:
+            raise PackitRPMNotFoundException(
+                "RPMs cannot be found, something is wrong."
+            )
+
+        return rpms
```

### Comparing `packitos-0.8.1/packit/utils.py` & `packitos-0.9.0/packit/utils.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/packit.spec` & `packitos-0.9.0/packit.spec`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 %global pypi_name packitos
 %global real_name packit
 
 Name:           %{real_name}
-Version:        0.8.0
+Version:        0.9.0
 Release:        1%{?dist}
 Summary:        A tool for integrating upstream projects with Fedora operating system
 
 License:        MIT
 URL:            https://github.com/packit-service/packit
 Source0:        %pypi_source
 BuildArch:      noarch
@@ -17,14 +17,15 @@
 BuildRequires:  python3-fedmsg
 BuildRequires:  python3-jsonschema
 BuildRequires:  python3-ogr
 BuildRequires:  python3-packaging
 BuildRequires:  python3-pyyaml
 BuildRequires:  python3-tabulate
 BuildRequires:  python3-cccolutils
+BuildRequires:  python3-copr
 BuildRequires:  python3-koji
 BuildRequires:  python3-lazy-object-proxy
 BuildRequires:  rebase-helper
 BuildRequires:  python3dist(setuptools)
 BuildRequires:  python3dist(setuptools-scm)
 BuildRequires:  python3dist(setuptools-scm-git-archive)
 # new-sources
@@ -32,16 +33,14 @@
 # bumpspec
 Requires:       rpmdevtools
 # doesn't have the python3dist provide
 Requires:       python3-koji
 Requires:       python3-bodhi-client
 Requires:       python3-%{real_name} = %{version}-%{release}
 
-%?python_enable_dependency_generator
-
 %description
 This project provides tooling and automation to integrate upstream open source
 projects into Fedora operating system.
 
 %package -n     python3-%{real_name}
 Summary:        %{summary}
 %{?python_provide:%python_provide python3-%{real_name}}
@@ -57,37 +56,39 @@
 rm -rf %{pypi_name}.egg-info
 
 %build
 %py3_build
 
 %install
 %py3_install
-%if 0%{?fedora} >= 30
 python3 setup.py --command-packages=click_man.commands man_pages --target %{buildroot}%{_mandir}/man1
-%endif
 
 # FIXME: workaround for setuptools installing it into bash_completion/ instead of bash-completion/
 install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
 mv %{buildroot}%{_datadir}/bash_completion/completions/packit %{buildroot}%{_datadir}/bash-completion/completions/packit
 
 %files
 %license LICENSE
 %{_bindir}/packit
-%if 0%{?fedora} >= 30
 %{_mandir}/man1/packit*.1*
-%endif
 %dir %{_datadir}/bash-completion/completions
 %{_datadir}/bash-completion/completions/%{real_name}
 
 %files -n python3-%{real_name}
 %license LICENSE
 %doc README.md
 %{python3_sitelib}/*
 
 %changelog
+* Wed Mar 25 2020 Jiri Popelka <jpopelka@redhat.com> - 0.9.0-1
+- new upstream release 0.9.0
+
+* Mon Jan 20 2020 Jiri Popelka <jpopelka@redhat.com> - 0.8.1-1
+- new upstream release 0.8.1
+
 * Fri Oct 18 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.1-1
 - new upstream release 0.7.1
 
 * Fri Oct 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.0-1
 - new upstream release 0.7.0
 
 * Thu Sep 12 2019 Jiri Popelka <jpopelka@redhat.com> - 0.6.1-1
```

### Comparing `packitos-0.8.1/packitos.egg-info/PKG-INFO` & `packitos-0.9.0/packitos.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: packitos
-Version: 0.8.1
+Version: 0.9.0
 Summary: A set of tools to integrate upstream open source projects into Fedora operating system.
 Home-page: https://github.com/packit-service/packit
 Author: Red Hat
 Author-email: user-cont-team@redhat.com
 License: MIT
 Description: [![Build Status](https://zuul-ci.org/gated.svg)](https://softwarefactory-project.io/zuul/t/local/builds?project=packit-service/packit)
         
@@ -17,56 +17,54 @@
         You can use packit to continously build your upstream project in Fedora.
         With packit you can create SRPMs, open pull requests in dist-git, submit koji builds and even
         create bodhi updates, effectively replacing the whole Fedora packaging workflow.
         
         ## Plan and current status
         
         We are working on two things now:
-         1. Packit as a tool - a standalone CLI tool which you can install from Fedora
+        
+        1.  Packit as a tool - a standalone CLI tool which you can install from Fedora
             repositories and use easily.
-         2. Packit service - A service offering built on top of packit tool. Our
+        2.  Packit service - A service offering built on top of packit tool. Our
             expectation is that you would add packit service into your Github
             repository and it would start handling things automatically: opening pull
             requests on dist-git, building packages, creating updates, ...
         
         For the run-down of the planned work, please see the task-list below.
         
-        
-        * [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
-          * [x] Bring new upstream releases into Fedora rawhide as dist-git pull
+        - [ ] E2E workflow for getting upstream releases into Fedora using packit CLI.
+          - [x] Bring new upstream releases into Fedora rawhide as dist-git pull
                 requests. ([propose-update](https://packit.dev/docs/cli/propose-update/) command included in 0.1.0 release)
-          * [x] Build the change once it's merged. #137
-          * [x] Send new downstream changes back to upstream. (so the spec files are in
+          - [x] Build the change once it's merged. #137
+          - [x] Send new downstream changes back to upstream. (so the spec files are in
                 sync) #145
-          * [x] Packit can create bodhi updates. #139
-          * [x] Ability to propose updates also to stable releases of Fedora.
-          * [x] Create SRPMs from the upstream repository
-          * [x] Build RPMs in COPR and integrate the results into Github.
-        * [ ] source-git
-          * [x] Packit can create a SRPM from a source-git repo.
-          * [ ] You can release to rawhide from source-git using packit.
-          * [ ] Packit can create a source-git repository.
-          * [ ] Packit helps developers with their source-git repositories.
-        * [ ] Packit as a service
-          * [x] Packit reacts to Github webhooks.
-          * [x] Have a Github app for packit.
-            * [ ] Github app is on Marketplace.
-          * [ ] Packit service is deployed and usable by anyone.
-        
+          - [x] Packit can create bodhi updates. #139
+          - [x] Ability to propose updates also to stable releases of Fedora.
+          - [x] Create SRPMs from the upstream repository
+          - [x] Build RPMs in COPR and integrate the results into Github.
+        - [ ] source-git
+          - [x] Packit can create a SRPM from a source-git repo.
+          - [ ] You can release to rawhide from source-git using packit.
+          - [ ] Packit can create a source-git repository.
+          - [ ] Packit helps developers with their source-git repositories.
+        - [x] Packit as a service
+          - [x] Packit reacts to Github webhooks.
+          - [x] Have a Github app for packit.
+            - [x] Github app is on Marketplace.
+          - [x] Packit service is deployed and usable by anyone.
         
         ## Workflows covered by packit
         
         This list contains workflows covered by packit tool and links to the documentation.
         
-        * [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
-        * [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
-        * [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
-        * [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
-        * [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
-        
+        - [Update Fedora dist-git with an upstream release.](https://packit.dev/docs/cli/propose-update/)
+        - [Build content of a Fedora dist-git branch in koji.](https://packit.dev/docs/cli/build/)
+        - [Create a bodhi update.](https://packit.dev/docs/cli/create-bodhi-update/)
+        - [Create a SRPM from the current content in the upstream repository.](https://packit.dev/docs/cli/srpm/)
+        - [Sync content of the Fedora dist-git repo into the upstream repository.](https://packit.dev/docs/cli/sync-from-downstream/)
         
         ## Configuration
         
         Configuration file for packit is described [here](http://packit.dev/docs/configuration/).
         
         TL;DR
         
@@ -74,14 +72,17 @@
         specfile_path: packit.spec
         synced_files:
           - packit.spec
         upstream_package_name: packitos
         downstream_package_name: packit
         ```
         
+        ## User configuration file
+        
+        User configuration file for packit is described [here](http://packit.dev/docs/configuration/#user-configuration-file).
         
         ## Requirements
         
         Packit is written in python 3 and is supported only on 3.6 and later.
         
         When packit interacts with dist-git, it uses `fedpkg`, we suggest installing it:
         
@@ -107,15 +108,14 @@
         
         You can also install packit from master branch, if you are brave enough:
         
         ```
         $ pip3 install --user git+https://github.com/packit-service/packit.git
         ```
         
-        
         ### Run from git directly:
         
         You don't need need to install packit to try it out. You can run it directly
         from git (if you have all the dependencies installed):
         
         ```
         $ python3 -m packit.cli.packit_base --help
@@ -123,29 +123,28 @@
         
         Options:
           -d, --debug
           -h, --help         Show this message and exit.
         ...
         ```
         
-        
         ## Who is interested
         
-        * Identity team (@pvoborni)
-        * Plumbers - Source Git (@msekletar @lnykryn)
-        * shells (@siteshwar)
-        * python-operator-courier (Ralph Bean)
-        * @thrix
-        * youtube-dl (Till Mass)
-        * [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
-        * ABRT
-        * OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
-        * CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
-        * cockpit (@martinpitt)
-        * iptables (@jsynacek)
+        - Identity team (@pvoborni)
+        - Plumbers - Source Git (@msekletar @lnykryn)
+        - shells (@siteshwar)
+        - python-operator-courier (Ralph Bean)
+        - @thrix
+        - youtube-dl (Till Mass)
+        - [greenboot](https://github.com/LorbusChris/greenboot/) (@LorbusChris)
+        - ABRT
+        - OSBS (atomic-reactor, osbs-client, koji-containerbuild) (@cverna)
+        - CoreOS (starting with rpm-ostree, ignition, and ostree) (@jlebon)
+        - cockpit (@martinpitt)
+        - iptables (@jsynacek)
         
         For the up to date list of projects which are using packit, [click here](https://github.com/packit-service/research/blob/master/onboard/status.md).
         
         ## Logo design
         
         Created by `Marián Mrva` - [@surfer19](https://github.com/surfer19)
         
@@ -153,14 +152,17 @@
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
 Classifier: Topic :: Software Development
 Classifier: Topic :: Utilities
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 Provides-Extra: testing
```

### Comparing `packitos-0.8.1/packitos.egg-info/SOURCES.txt` & `packitos-0.9.0/packitos.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -36,48 +36,37 @@
 design/export/logo-square-small-borders.png
 design/export/logo-text.jpg
 design/export/logo-text.png
 design/export/logo-text.svg
 design/export/logo-white.png
 design/export/logo.png
 design/export/logo.svg
-docs/01.md
-docs/02.md
-docs/ARCHITECTURE.md
-docs/actions.md
-docs/build.md
-docs/configuration.md
-docs/create_bodhi_update.md
-docs/how-to-source-git.md
-docs/packit.dia
-docs/packit.png
-docs/propose_update.md
-docs/source-git-best-practices.svg.png
-docs/source-git.md
-docs/srpm.md
-docs/sync-from-downstream.md
 fedora-tests/simple.py
 fedora-tests/tests.yml
 fedora-tests/upstream.sh
 files/install-requirements.yaml
 files/install-tests-requirements.yaml
 files/packit-testing-farm-prepare-session-recording.yaml
 files/packit-testing-farm-prepare.yaml
 files/zuul-install-requirements-git-master.yaml
 files/zuul-install-requirements-pip.yaml
 files/zuul-install-requirements-rpms.yaml
 files/zuul-pre-commit.yaml
+files/zuul-reverse-dep-packit-service.yaml
 files/zuul-tests-session-recording.yaml
 files/zuul-tests.yaml
 files/bash-completion/packit
 files/tasks/build-rpm-deps.yaml
 files/tasks/configure-git.yaml
 files/tasks/generic-dnf-requirements.yaml
+files/tasks/install-ansible.yaml
+files/tasks/install-packit-service.yaml
 files/tasks/install-packit.yaml
 files/tasks/ogr-from-master.yaml
+files/tasks/packit-service-requirements.yaml
 files/tasks/python-compile-deps.yaml
 files/tasks/requre-master.yaml
 files/tasks/rpm-test-deps.yaml
 files/tasks/sandcastle-master.yaml
 files/tasks/zuul-project-setup.yaml
 packit/__init__.py
 packit/actions.py
@@ -99,15 +88,16 @@
 packit/sync.py
 packit/upstream.py
 packit/utils.py
 packit/cli/__init__.py
 packit/cli/build.py
 packit/cli/copr_build.py
 packit/cli/create_update.py
-packit/cli/generate.py
+packit/cli/init.py
+packit/cli/local_build.py
 packit/cli/packit_base.py
 packit/cli/push_updates.py
 packit/cli/srpm.py
 packit/cli/status.py
 packit/cli/sync_from_downstream.py
 packit/cli/types.py
 packit/cli/update.py
@@ -206,14 +196,15 @@
 tests/data/vsftpd/Fedora/vsftpd@.service
 tests/data/vsftpd/Fedora/vsftpd_conf_migrate.sh
 tests/data/vsftpd/RedHat/vsftpd.log
 tests/data/vsftpd/SECURITY/security
 tests/functional/README.md
 tests/functional/__init__.py
 tests/functional/spellbook.py
+tests/functional/test_local_build.py
 tests/functional/test_srpm.py
 tests/integration/README.md
 tests/integration/__init__.py
 tests/integration/bodhi_latest_builds.py
 tests/integration/bodhi_status_updates.py
 tests/integration/conftest.py
 tests/integration/test_actions.py
@@ -240,15 +231,17 @@
 tests/unit/test_actions.py
 tests/unit/test_api.py
 tests/unit/test_base_git.py
 tests/unit/test_cli.py
 tests/unit/test_cli_utils.py
 tests/unit/test_config.py
 tests/unit/test_config_aliases.py
+tests/unit/test_load_authentication.py
 tests/unit/test_local_project.py
+tests/unit/test_package_config.py
 tests/unit/test_security.py
 tests/unit/test_sync.py
 tests/unit/test_unicodez.py
 tests/unit/test_upstream.py
 tests/unit/test_utils.py
 tests_recording/README.md
 tests_recording/__init__.py
```

### Comparing `packitos-0.8.1/recipe-tests.yaml` & `packitos-0.9.0/recipe-tests.yaml`

 * *Files 0% similar despite different names*

```diff
@@ -7,20 +7,20 @@
         environment:
           LD_PRELOAD: ""
           NSS_WRAPPER_PASSWD: ""
           NSS_WRAPPER_GROUP: /etc/group
           USER: ""
           HOME: ""
   tasks:
-  - name: Install all packages needed to run tests
-    dnf:
-      name:
-      - python3-tox
-      - python36
-      - krb5-devel
-      - rpm-libs
-      - redhat-rpm-config
-      # when running the tests in a rootless podman container, tox environment
-      # needed gcc and rpm-devel to compile the rpm-libs python bindings
-      # - gcc
-      # - rpm-devel
-      state: present
+    - name: Install all packages needed to run tests
+      dnf:
+        name:
+          - python3-tox
+          - python36
+          - krb5-devel
+          - rpm-libs
+          - redhat-rpm-config
+        # when running the tests in a rootless podman container, tox environment
+        # needed gcc and rpm-devel to compile the rpm-libs python bindings
+        # - gcc
+        # - rpm-devel
+        state: present
```

### Comparing `packitos-0.8.1/setup.cfg` & `packitos-0.9.0/setup.cfg`

 * *Files 18% similar despite different names*

```diff
@@ -1,72 +1,75 @@
 [metadata]
 name = packitos
-url = https://github.com/packit-service/packit
 description = A set of tools to integrate upstream open source projects into Fedora operating system.
 long_description = file: README.md
 long_description_content_type = text/markdown
+url = https://github.com/packit-service/packit
 author = Red Hat
 author_email = user-cont-team@redhat.com
 license = MIT
 license_file = LICENSE
 classifiers = 
 	Development Status :: 4 - Beta
 	Environment :: Console
 	Intended Audience :: Developers
 	License :: OSI Approved :: MIT License
 	Operating System :: POSIX :: Linux
 	Programming Language :: Python
+	Programming Language :: Python :: 3
+	Programming Language :: Python :: 3 :: Only
 	Programming Language :: Python :: 3.6
 	Programming Language :: Python :: 3.7
+	Programming Language :: Python :: 3.8
 	Topic :: Software Development
 	Topic :: Utilities
 keywords = 
 	git
 	packaging
 	fedora
 	rpm
 	dist-git
 
 [options]
 packages = find:
-python_requires = >=3.6
-include_package_data = True
-setup_requires = 
-	setuptools_scm
-	setuptools_scm_git_archive
 install_requires = 
 	GitPython
 	PyGithub
-	click
 	PyYAML
-	jsonschema
-	ogr>=0.7.0
-	rebasehelper
-	munch
-	tabulate
-	packaging
-	requests
-	copr
-	python-gnupg
 	cccolutils
+	click
+	copr
+	jsonschema
 	lazy_object_proxy
 	marshmallow<3
 	marshmallow-enum
+	munch
+	ogr
+	packaging
+	python-gnupg
+	rebasehelper
+	requests
+	tabulate
+python_requires = >=3.6
+include_package_data = True
+setup_requires = 
+	setuptools_scm
+	setuptools_scm_git_archive
 
-[options.packages.find]
-exclude = 
-	tests*
+[options.entry_points]
+console_scripts = 
+	packit=packit.cli.packit_base:packit_base
 
 [options.extras_require]
 testing = 
 	pytest
 
-[options.entry_points]
-console_scripts = 
-	packit=packit.cli.packit_base:packit_base
+[options.packages.find]
+exclude = 
+	tests*
 
 [options.data_files]
 share/bash-completion/completions/ = files/bash-completion/packit
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `packitos-0.8.1/setup.py` & `packitos-0.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/__init__.py` & `packitos-0.9.0/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/conftest.py` & `packitos-0.9.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/cockpit-ostree/Makefile` & `packitos-0.9.0/tests/data/cockpit-ostree/Makefile`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/cockpit-ostree/cockpit-ostree.spec.dg` & `packitos-0.9.0/tests/data/cockpit-ostree/cockpit-ostree.spec.dg`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/cockpit-ostree/cockpit-ostree.spec.in` & `packitos-0.9.0/tests/data/cockpit-ostree/cockpit-ostree.spec.in`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/dg-ogr/.packit.yaml` & `packitos-0.9.0/tests/data/dg-ogr/.packit.yaml`

 * *Files 11% similar despite different names*

```diff
@@ -6,28 +6,28 @@
 upstream_package_name: ogr
 downstream_package_name: python-ogr
 upstream_project_url: "https://github.com/packit-service/ogr"
 # the version is different than with basic git describe
 create_tarball_command: ["python3", "setup.py", "sdist", "--dist-dir", "."]
 current_version_command: ["python3", "setup.py", "--version"]
 jobs:
-- job: sync_from_downstream
-  trigger: commit
-- job: propose_downstream
-  trigger: release
-  metadata:
-    dist-git-branch: master
-- job: propose_downstream
-  trigger: release
-  metadata:
-    dist-git-branch: f30
-- job: propose_downstream
-  trigger: release
-  metadata:
-    dist-git-branch: f29
-- job: copr_build
-  trigger: pull_request
-  metadata:
-    targets:
-    - fedora-29-x86_64
-    - fedora-rawhide-x86_64
-    - fedora-30-x86_64
+  - job: sync_from_downstream
+    trigger: commit
+  - job: propose_downstream
+    trigger: release
+    metadata:
+      dist-git-branch: master
+  - job: propose_downstream
+    trigger: release
+    metadata:
+      dist-git-branch: f30
+  - job: propose_downstream
+    trigger: release
+    metadata:
+      dist-git-branch: f29
+  - job: copr_build
+    trigger: pull_request
+    metadata:
+      targets:
+        - fedora-29-x86_64
+        - fedora-rawhide-x86_64
+        - fedora-30-x86_64
```

### Comparing `packitos-0.8.1/tests/data/dg-ogr/python-ogr.spec` & `packitos-0.9.0/tests/data/dg-ogr/python-ogr.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/edd/Makefile` & `packitos-0.9.0/tests/data/edd/Makefile`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/edd/edd.spec` & `packitos-0.9.0/tests/data/edd/edd.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/osbuild/osbuild.spec` & `packitos-0.9.0/tests/data/osbuild/osbuild.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/snapd/packaging/fedora/pack-source` & `packitos-0.9.0/tests/data/snapd/packaging/fedora/pack-source`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/snapd/packaging/fedora/snapd.spec` & `packitos-0.9.0/tests/data/snapd/packaging/fedora/snapd.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/upstream_git_with_multiple_sources/beer.spec` & `packitos-0.9.0/tests/data/upstream_git_with_multiple_sources/beer.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/data/vsftpd/Fedora/vsftpd.spec` & `packitos-0.9.0/tests/data/vsftpd/Fedora/vsftpd.spec`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/functional/__init__.py` & `packitos-0.9.0/tests/functional/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/functional/test_srpm.py` & `packitos-0.9.0/tests/functional/test_srpm.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/bodhi_latest_builds.py` & `packitos-0.9.0/tests/integration/bodhi_latest_builds.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/bodhi_status_updates.py` & `packitos-0.9.0/tests/integration/bodhi_status_updates.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/conftest.py` & `packitos-0.9.0/tests/integration/conftest.py`

 * *Files 4% similar despite different names*

```diff
@@ -48,14 +48,15 @@
     SOURCEGIT_UPSTREAM,
     SOURCEGIT_SOURCEGIT,
     git_add_and_commit,
     TARBALL_NAME,
     UPSTREAM,
     initiate_git_repo,
     DISTGIT,
+    NAME_VERSION,
 )
 
 DOWNSTREAM_PROJECT_URL = "https://src.fedoraproject.org/not/set.git"
 UPSTREAM_PROJECT_URL = "https://github.com/also-not/set.git"
 
 
 @pytest.fixture()
@@ -91,20 +92,19 @@
     distgit, _ = distgit_and_remote
     return mock_remote_functionality(upstream=sourcegit, distgit=distgit)
 
 
 def mock_spec_download_remote_s(path: Path):
     def mock_download_remote_sources():
         """ mock download of the remote archive and place it into dist-git repo """
-        tarball_path = path / TARBALL_NAME
-        hops_filename = "hops"
-        hops_path = path / hops_filename
-        hops_path.write_text("Cascade\n")
+        beerware_dir = path / NAME_VERSION
+        beerware_dir.mkdir(exist_ok=True)
+        beerware_dir.joinpath("hops").write_text("Cascade\n")
         subprocess.check_call(
-            ["tar", "-cf", str(tarball_path), hops_filename], cwd=path
+            ["tar", "-cf", str(path / TARBALL_NAME), NAME_VERSION], cwd=path
         )
 
     flexmock(Specfile, download_remote_sources=mock_download_remote_sources)
 
 
 def mock_remote_functionality(distgit: Path, upstream: Path):
     def mocked_pr_create(*args, **kwargs):
@@ -165,15 +165,15 @@
     pc.upstream_project_url = str(upstream)
     return upstream, distgit
 
 
 @pytest.fixture()
 def mock_patching():
     flexmock(Upstream).should_receive("create_patches").and_return(["patches"])
-    flexmock(DistGit).should_receive("add_patches_to_specfile").with_args(["patches"])
+    flexmock(DistGit).should_receive("specfile_add_patches").with_args(["patches"])
 
 
 @pytest.fixture()
 def cwd_upstream(upstream_and_remote) -> Iterator[Path]:
     upstream, _ = upstream_and_remote
     with cwd(upstream):
         yield upstream
```

### Comparing `packitos-0.8.1/tests/integration/test_actions.py` & `packitos-0.9.0/tests/integration/test_actions.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_api.py` & `packitos-0.9.0/tests/integration/test_api.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_base_git.py` & `packitos-0.9.0/tests/integration/test_base_git.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_build.py` & `packitos-0.9.0/tests/integration/test_build.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_copr_build.py` & `packitos-0.9.0/tests/integration/test_copr_build.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_create_update.py` & `packitos-0.9.0/tests/integration/test_create_update.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_distgit.py` & `packitos-0.9.0/tests/integration/test_distgit.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_generate.py` & `packitos-0.9.0/tests/integration/test_generate.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_get_api.py` & `packitos-0.9.0/tests/integration/test_get_api.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_pagure.py` & `packitos-0.9.0/tests/integration/test_pagure.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_push_updates.py` & `packitos-0.9.0/tests/integration/test_push_updates.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_security.py` & `packitos-0.9.0/tests/integration/test_security.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_source_git.py` & `packitos-0.9.0/tests/integration/test_source_git.py`

 * *Files 9% similar despite different names*

```diff
@@ -21,15 +21,20 @@
 # SOFTWARE.
 import subprocess
 from pathlib import Path
 
 from packit.utils import cwd
 from packit.specfile import Specfile
 from tests.integration.conftest import mock_spec_download_remote_s
-from tests.spellbook import TARBALL_NAME, git_add_and_commit, build_srpm
+from tests.spellbook import (
+    TARBALL_NAME,
+    git_add_and_commit,
+    build_srpm,
+    create_merge_commit_in_source_git,
+)
 
 
 def test_basic_local_update_without_patching(
     sourcegit_and_remote,
     distgit_and_remote,
     mock_patching,
     mock_remote_functionality_sourcegit,
@@ -40,29 +45,29 @@
     sourcegit, _ = sourcegit_and_remote
     distgit, _ = distgit_and_remote
     mock_spec_download_remote_s(distgit)
 
     api_instance_source_git.sync_release("master", "0.1.0", upstream_ref="0.1.0")
 
     assert (distgit / TARBALL_NAME).is_file()
-    spec = Specfile(str(distgit / "beer.spec"))
+    spec = Specfile(distgit / "beer.spec")
     assert spec.get_version() == "0.1.0"
 
 
 def test_basic_local_update_empty_patch(
     distgit_and_remote, mock_remote_functionality_sourcegit, api_instance_source_git
 ):
     """ propose-update for sourcegit test: mock remote API, use local upstream and dist-git """
 
     distgit, _ = distgit_and_remote
     mock_spec_download_remote_s(distgit)
     api_instance_source_git.sync_release("master", "0.1.0", upstream_ref="0.1.0")
 
     assert (distgit / TARBALL_NAME).is_file()
-    spec = Specfile(str(distgit / "beer.spec"))
+    spec = Specfile(distgit / "beer.spec")
     assert spec.get_version() == "0.1.0"
 
     spec_package_section = ""
     for section in spec.spec_content.sections:
         if "%package" in section[0]:
             spec_package_section += "\n".join(section[1])
     assert "# PATCHES FROM SOURCE GIT" not in spec_package_section
@@ -78,91 +83,148 @@
 ):
     """ propose-update for sourcegit test: mock remote API, use local upstream and dist-git """
 
     sourcegit, _ = sourcegit_and_remote
     distgit, _ = distgit_and_remote
     mock_spec_download_remote_s(distgit)
 
+    create_merge_commit_in_source_git(sourcegit)
+
     source_file = sourcegit / "big-source-file.txt"
     source_file.write_text("new changes")
     git_add_and_commit(directory=sourcegit, message="source change")
 
     source_file = sourcegit / "ignored_file.txt"
     source_file.write_text(" And I am sad.")
     git_add_and_commit(directory=sourcegit, message="make a file sad")
 
     api_instance_source_git.sync_release("master", "0.1.0", upstream_ref="0.1.0")
 
-    spec = Specfile(str(distgit / "beer.spec"))
-
-    spec_package_section = ""
-    for section in spec.spec_content.sections:
-        if "%package" in section[0]:
-            spec_package_section += "\n".join(section[1])
-    assert "Patch0001: 0001" in spec_package_section
-    assert "Patch0002: 0002" not in spec_package_section  # no empty patches
-
     git_diff = subprocess.check_output(
         ["git", "diff", "HEAD~", "HEAD"], cwd=distgit
     ).decode()
 
-    assert "-Version:        0.0.0\n+Version:        0.1.0" in git_diff
-    assert "+# PATCHES FROM SOURCE GIT:" in git_diff
     assert (
-        " - 0.1.0-1\n"
-        "+- new upstream release: 0.1.0\n"
-        "+\n"
-        " * Sun Feb 24 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.0.0-1\n"
-        " - No brewing, yet.\n" in git_diff
+        """
+-Version:        0.0.0
++Version:        0.1.0"""
+        in git_diff
+    )
+
+    assert (
+        """
++# PATCHES FROM SOURCE GIT:
++
++# MERGE COMMIT!
++# Author: Packit Test Suite <test@example.com>
++Patch0001: 0-0001-switching-to-amarillo-hops.patch
++
++# MERGE COMMIT!
++# Author: Packit Test Suite <test@example.com>
++Patch0002: 1-0002-actually-let-s-do-citra.patch
++
++# source change
++# Author: Packit Test Suite <test@example.com>
++Patch0003: 2-0001-source-change.patch
++
++
+ %description
+"""
+        in git_diff
+    )
+    assert "Patch0004:" not in git_diff
+
+    assert (
+        """ %prep
+-%autosetup -n %{upstream_name}-%{version}
++%autosetup -p1 -n %{upstream_name}-%{version}"""
+        in git_diff
+    )
+
+    assert (
+        """ - 0.1.0-1
++- new upstream release: 0.1.0
++
+ * Sun Feb 24 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.0.0-1
+ - No brewing, yet."""
+        in git_diff
     )
 
     # direct diff in the synced file
     assert (
-        "diff --git a/.packit.yaml b/.packit.yaml\n" "new file mode 100644" in git_diff
+        """diff --git a/.packit.yaml b/.packit.yaml
+new file mode 100644"""
+        in git_diff
+    )
+
+    assert (
+        """
+--- /dev/null
++++ b/.packit.yaml"""
+        in git_diff
     )
-    assert "--- /dev/null\n" "+++ b/.packit.yaml" in git_diff
 
     # diff of the synced file should not be in the patch
     assert (
-        "+diff --git a/.packit.yaml b/.packit.yaml\n"
-        "+new file mode 100644\n" not in git_diff
+        """
++diff --git a/.packit.yaml b/.packit.yaml
++new file mode 100644"""
+        not in git_diff
     )
 
     # diff of the source file (not synced) has to be in the patch
     assert (
-        "patch\n"
-        "@@ -0,0 +1,9 @@\n"
-        "+diff --git a/big-source-file.txt b/big-source-file.txt\n" in git_diff
+        """
++Subject: [PATCH] source change
++
++---
++ big-source-file.txt | 3 +--
++ 1 file changed, 1 insertion(+), 2 deletions(-)
++
++diff --git a/big-source-file.txt b/big-source-file.txt"""
+        in git_diff
     )
 
     assert (
-        "+--- a/big-source-file.txt\n"
-        "++++ b/big-source-file.txt\n"
-        "+@@ -1,2 +1 @@\n"
-        "+-This is a testing file\n"
-        "+-containing some text.\n"
-        "++new changes\n" in git_diff
+        "+Subject: [PATCH 2/2] actually, let's do citra\n"
+        "+\n"
+        "+---\n"
+        "+ hops | 2 +-\n"
+        "+ 1 file changed, 1 insertion(+), 1 deletion(-)\n"
+    ) in git_diff
+
+    assert (
+        """
++--- a/big-source-file.txt
+++++ b/big-source-file.txt
++@@ -1,2 +1 @@
++-This is a testing file
++-containing some text.
+++new changes"""
+        in git_diff
     )
 
     # diff of the source files (not synced) should not be directly in the git diff
     assert (
-        "--- a/big-source-file.txt\n"
-        "+++ b/big-source-file.txt\n"
-        "@@ -1,2 +1 @@\n"
-        "-This is a testing file\n"
-        "-containing some text.\n"
-        "+new changes\n" not in git_diff
+        """
+--- a/big-source-file.txt
++++ b/big-source-file.txt
+@@ -1,2 +1 @@
+-This is a testing file
+-containing some text.
++new changes"""
+        not in git_diff
     )
 
     # ignored file should not be in the diff
     assert "--- a/ignored_file.txt\n" not in git_diff
 
 
 def test_srpm(mock_remote_functionality_sourcegit, api_instance_source_git):
-    # TODO: we need a better test case here which will mimic the systemd use case
     sg_path = Path(api_instance_source_git.upstream_local_project.working_dir)
     mock_spec_download_remote_s(sg_path / "fedora")
+    create_merge_commit_in_source_git(sg_path)
     with cwd(sg_path):
         api_instance_source_git.create_srpm(upstream_ref="0.1.0")
     srpm_path = list(sg_path.glob("beer-0.1.0-2.*.src.rpm"))[0]
     assert srpm_path.is_file()
     build_srpm(srpm_path)
```

### Comparing `packitos-0.8.1/tests/integration/test_spec.py` & `packitos-0.9.0/tests/integration/test_spec.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,26 +15,47 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
+from pathlib import Path
+from shutil import copy
 
-from tests.spellbook import SPECFILE
-from packit.specfile import Specfile
+import pytest
 from rebasehelper.specfile import SpecContent
 
+from packit.specfile import Specfile
+from tests.spellbook import SPECFILE, UP_OSBUILD, UP_EDD, UP_VSFTPD
+
 
 def test_write_spec_content():
     with open(SPECFILE) as spec:
         content = spec.read()
 
     data = "new line 1\n"
     spec = Specfile(SPECFILE)
     spec.spec_content.replace_section("%description", [data])
     spec.write_spec_content()
 
     with open(SPECFILE) as specfile:
         assert "new line 1" in specfile.read()
         spec.spec_content = SpecContent(content)
         spec.write_spec_content()
+
+
+@pytest.mark.parametrize(
+    "input_spec",
+    [
+        UP_VSFTPD / "Fedora" / "vsftpd.spec",
+        UP_OSBUILD / "osbuild.spec",
+        UP_EDD / "edd.spec",
+    ],
+)
+def test_ensure_pnum(tmp_path, input_spec):
+    spec = Path(copy(input_spec, tmp_path))
+    Specfile(spec).ensure_pnum()
+    text = spec.read_text()
+    assert "%autosetup -p1" in text
+    # %autosetup does not accept -q
+    assert "-q" not in text
```

### Comparing `packitos-0.8.1/tests/integration/test_sync_files.py` & `packitos-0.9.0/tests/integration/test_sync_files.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_update.py` & `packitos-0.9.0/tests/integration/test_update.py`

 * *Files 2% similar despite different names*

```diff
@@ -61,15 +61,15 @@
     """ basic propose-update test: mock remote API, use local upstream and dist-git """
     u, d, api = api_instance
     mock_spec_download_remote_s(d)
 
     api.sync_release("master", "0.1.0")
 
     assert (d / TARBALL_NAME).is_file()
-    spec = Specfile(str(d / "beer.spec"))
+    spec = Specfile(d / "beer.spec")
     assert spec.get_version() == "0.1.0"
     assert (d / "README.packit").is_file()
     # assert that we have changelog entries for both versions
     changelog = "\n".join(spec.spec_content.section("%changelog"))
     assert "0.0.0" in changelog
     assert "0.1.0" in changelog
 
@@ -80,15 +80,15 @@
     """ basic propose-update test: mock remote API, use local upstream and dist-git """
     u, d, api = api_instance
     mock_spec_download_remote_s(d)
 
     api.sync_release("master", "0.1.0")
 
     assert (d / TARBALL_NAME).is_file()
-    spec = Specfile(str(d / "beer.spec"))
+    spec = Specfile(d / "beer.spec")
     assert spec.get_version() == "0.1.0"
     assert (d / "README.packit").is_file()
     # assert that we have changelog entries for both versions
     changelog = "\n".join(spec.spec_content.section("%changelog"))
     assert "0.0.0" in changelog
     assert "0.1.0" in changelog
 
@@ -105,30 +105,30 @@
 
     remote_dir_clone = Path(f"{distgit_remote}-clone")
     subprocess.check_call(
         ["git", "clone", distgit_remote, str(remote_dir_clone)],
         cwd=str(remote_dir_clone.parent),
     )
 
-    spec = Specfile(str(remote_dir_clone / "beer.spec"))
+    spec = Specfile(remote_dir_clone / "beer.spec")
     assert spec.get_version() == "0.1.0"
     assert (remote_dir_clone / "README.packit").is_file()
 
 
 def test_basic_local_update_from_downstream(
     cwd_upstream, api_instance, mock_remote_functionality_upstream
 ):
     flexmock(LocalProject, _parse_namespace_from_git_url=lambda: None)
     u, d, api = api_instance
 
     api.sync_from_downstream("master", "master", True)
 
     new_upstream = Path(api.up.local_project.working_dir)
     assert (new_upstream / "beer.spec").is_file()
-    spec = Specfile(str(new_upstream / "beer.spec"))
+    spec = Specfile(new_upstream / "beer.spec")
     assert spec.get_version() == "0.0.0"
 
 
 def test_local_update_with_specified_tag_template():
     c = Config()
     pc = parse_loaded_config(
         {
```

### Comparing `packitos-0.8.1/tests/integration/test_upstream.py` & `packitos-0.9.0/tests/integration/test_upstream.py`

 * *Files 4% similar despite different names*

```diff
@@ -73,16 +73,15 @@
 
     assert ups.get_version() == exp
 
     u.joinpath("README").write_text("\nEven better now!\n")
     subprocess.check_call(["git", "add", "."], cwd=u)
     subprocess.check_call(["git", "commit", "-m", "More awesome changes"], cwd=u)
 
-    # 0.1.0.1.ge98cee1
-    assert re.match(r"0\.1\.0\.1\.\w{8}", ups.get_current_version())
+    assert ups.get_current_version() == "0.1.0"
 
 
 def test_get_version_macro(upstream_instance):
     u, ups = upstream_instance
 
     data = "import setuptools \nsetuptools.setup(version='1')"
     setup_path = u.joinpath("setup.py")
@@ -159,15 +158,17 @@
 
     u.joinpath("README").write_text("\nEven better now!\n")
     subprocess.check_call(["git", "add", "."], cwd=u)
     subprocess.check_call(["git", "commit", "-m", "More awesome changes"], cwd=u)
 
     ups.create_archive()
 
-    assert len(list(u.glob(f"*{extension}"))) == 2
+    # there is still only one archive - we no longer use --long git-describe
+    # by default, upstreams should handle versions themselves
+    assert len(list(u.glob(f"*{extension}"))) == 1
 
 
 def test_create_uncommon_archive(upstream_instance):
     u, ups = upstream_instance
     change_source_ext(ups, ".cpio")
 
     with pytest.raises(PackitException):
@@ -193,17 +194,39 @@
 
     ups.create_archive()
     srpm = ups.create_srpm()
 
     assert srpm.exists()
 
     srpm_path = Path(tmpdir).joinpath("custom.src.rpm")
+
+    ups.prepare_upstream_for_srpm_creation()
     srpm = ups.create_srpm(srpm_path=srpm_path)
+    r = re.compile(r"^- Development snapshot \(\w{8}\)$")
+    for l in ups.specfile.spec_content.section("%changelog"):
+        if r.match(l):
+            break
+    else:
+        assert False, "Didn't find the correct line in the spec file."
+    assert srpm.exists()
+    build_srpm(srpm)
+
+
+def test_create_srpm_git_desc_release(upstream_instance, tmpdir):
+    u, ups = upstream_instance
+    u.joinpath("README").write_text("\nEven better now!\n")
+    subprocess.check_call(["git", "add", "."], cwd=u)
+    subprocess.check_call(["git", "commit", "-m", "More awesome changes"], cwd=u)
+
+    ups.create_archive()
+    ups.prepare_upstream_for_srpm_creation()
+    srpm = ups.create_srpm()
     assert srpm.exists()
     build_srpm(srpm)
+    assert re.match(r".+beer-0.1.0-1.\d+.fc\d{2}.src.rpm$", str(srpm))
 
 
 def test_github_app(upstream_instance, tmpdir):
     u, ups = upstream_instance
     t = Path(tmpdir)
 
     fake_cert_path = t / "fake-cert.pem"
```

### Comparing `packitos-0.8.1/tests/integration/test_using_cockpit.py` & `packitos-0.9.0/tests/integration/test_using_cockpit.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/test_using_examples.py` & `packitos-0.9.0/tests/integration/test_using_examples.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/integration/utils.py` & `packitos-0.9.0/tests/integration/utils.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/spellbook.py` & `packitos-0.9.0/tests/spellbook.py`

 * *Files 6% similar despite different names*

```diff
@@ -41,20 +41,22 @@
 EMPTY_CHANGELOG = DATA_DIR / "empty_changelog"
 DISTGIT = DATA_DIR / "dist_git"
 UP_COCKPIT_OSTREE = DATA_DIR / "cockpit-ostree"
 UP_OSBUILD = DATA_DIR / "osbuild"
 UP_SNAPD = DATA_DIR / "snapd"
 UP_EDD = DATA_DIR / "edd"
 UP_VSFTPD = DATA_DIR / "vsftpd"
-TARBALL_NAME = "beerware-0.1.0.tar.gz"
+NAME_VERSION = "beerware-0.1.0"
+TARBALL_NAME = f"{NAME_VERSION}.tar.gz"
 SOURCEGIT_UPSTREAM = DATA_DIR / "sourcegit" / "upstream"
 SOURCEGIT_SOURCEGIT = DATA_DIR / "sourcegit" / "source_git"
 DG_OGR = DATA_DIR / "dg-ogr"
 SPECFILE = DATA_DIR / "upstream_git/beer.spec"
 UPSTREAM_SPEC_NOT_IN_ROOT = DATA_DIR / "spec_not_in_root/upstream"
+SYNC_FILES = DATA_DIR / "sync_files"
 
 
 def git_set_user_email(directory):
     subprocess.check_call(
         ["git", "config", "user.email", "test@example.com"], cwd=directory
     )
     subprocess.check_call(
@@ -94,15 +96,18 @@
     """
     if remotes is None:
         remotes = [("origin", upstream_remote)]
 
     if copy_from:
         shutil.copytree(copy_from, directory)
     subprocess.check_call(["git", "init", "."], cwd=directory)
-    Path(directory).joinpath("README").write_text("Best upstream project ever!")
+    directory_path = Path(directory)
+    directory_path.joinpath("README").write_text("Best upstream project ever!")
+    # this file is in the tarball
+    directory_path.joinpath("hops").write_text("Cascade\n")
     git_set_user_email(directory)
     subprocess.check_call(["git", "add", "."], cwd=directory)
     subprocess.check_call(["git", "commit", "-m", "initial commit"], cwd=directory)
     if tag:
         subprocess.check_call(
             ["git", "tag", "-a", "-m", f"tag {tag}, tests", tag], cwd=directory
         )
@@ -115,14 +120,27 @@
         # tox strips some env vars so your user gitconfig is not picked up
         # hence we need to be very explicit with git commands here
         subprocess.check_call(
             ["git", "push", "--tags", "-u", "origin", "master:master"], cwd=directory
         )
 
 
+def create_merge_commit_in_source_git(sg: Path):
+    hops = sg.joinpath("hops")
+    subprocess.check_call(["git", "checkout", "-B", "new-changes"], cwd=sg)
+    hops.write_text("Amarillo\n")
+    git_add_and_commit(directory=sg, message="switching to amarillo hops")
+    hops.write_text("Citra\n")
+    git_add_and_commit(directory=sg, message="actually, let's do citra")
+    subprocess.check_call(["git", "checkout", "master"], cwd=sg)
+    subprocess.check_call(
+        ["git", "merge", "--no-ff", "-m", "MERGE COMMIT!", "new-changes"], cwd=sg,
+    )
+
+
 def prepare_dist_git_repo(directory, push=True):
     subprocess.check_call(["git", "branch", "f30"], cwd=directory)
     if push:
         subprocess.check_call(["git", "push", "-u", "origin", "f30:f30"], cwd=directory)
 
 
 def call_packit(fnc=None, parameters=None, envs=None, working_dir=None):
```

### Comparing `packitos-0.8.1/tests/unit/__init__.py` & `packitos-0.9.0/tests/unit/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_actions.py` & `packitos-0.9.0/tests/unit/test_actions.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_api.py` & `packitos-0.9.0/tests/unit/test_api.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_base_git.py` & `packitos-0.9.0/tests/unit/test_base_git.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_cli.py` & `packitos-0.9.0/tests/unit/test_cli.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_cli_utils.py` & `packitos-0.9.0/tests/unit/test_cli_utils.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_config.py` & `packitos-0.9.0/tests/unit/test_config.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,31 +20,32 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
 import os
 from pathlib import Path
 
 import pytest
-from flexmock import flexmock
 from marshmallow import ValidationError
 
+from flexmock import flexmock
 from ogr import GithubService, PagureService
 from ogr.abstract import GitProject, GitService
 from packit.actions import ActionName
 from packit.config import (
     Config,
     JobConfig,
-    JobTriggerType,
     JobType,
     PackageConfig,
     get_package_config_from_repo,
     SyncFilesConfig,
     SyncFilesItem,
+    JobConfigTriggerType,
 )
-from packit.config.aliases import get_build_targets, get_branches
+from packit.config.package_config import get_local_specfile_path
+from tests.spellbook import UP_OSBUILD, SYNC_FILES
 
 
 def get_job_config_dict_simple():
     return {"job": "build", "trigger": "release"}
 
 
 def get_job_config_dict_full():
@@ -52,36 +53,38 @@
         "job": "propose_downstream",
         "trigger": "pull_request",
         "metadata": {"a": "b"},
     }
 
 
 def get_job_config_simple():
-    return JobConfig(job=JobType.build, trigger=JobTriggerType.release, metadata={})
+    return JobConfig(
+        type=JobType.build, trigger=JobConfigTriggerType.release, metadata={}
+    )
 
 
 def get_job_config_full():
     return JobConfig(
-        job=JobType.propose_downstream,
-        trigger=JobTriggerType.pull_request,
+        type=JobType.propose_downstream,
+        trigger=JobConfigTriggerType.pull_request,
         metadata={"a": "b"},
     )
 
 
 def get_default_job_config():
     return [
         JobConfig(
-            job=JobType.copr_build,
-            trigger=JobTriggerType.pull_request,
-            metadata={"targets": get_build_targets("fedora-stable")},
+            type=JobType.tests,
+            trigger=JobConfigTriggerType.pull_request,
+            metadata={"targets": ["fedora-stable"]},
         ),
         JobConfig(
-            job=JobType.propose_downstream,
-            trigger=JobTriggerType.release,
-            metadata={"dist-git-branch": get_branches("fedora-all")},
+            type=JobType.propose_downstream,
+            trigger=JobConfigTriggerType.release,
+            metadata={"dist-git-branch": ["fedora-all"]},
         ),
     ]
 
 
 @pytest.fixture()
 def job_config_simple():
     return get_job_config_simple()
@@ -230,23 +233,21 @@
         == not_equal_package_config
     )
 
 
 @pytest.mark.parametrize(
     "raw,is_valid",
     [
-        ({}, False),
         (
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": "fedora/foobar.spec",
             },
             False,
         ),
-        ({"jobs": [{"trigger": "release", "job": "propose_downstream"}]}, False),
         (
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/foobar.spec"],
             },
             True,
         ),
@@ -284,44 +285,64 @@
             {
                 "specfile_path": "fedora/package.spec",
                 "actions": ["actions" "has", "to", "be", "key", "value"],
                 "jobs": [{"job": "asd", "trigger": "qwe"}],
             },
             False,
         ),
+        (
+            {
+                "specfile_path": "fedora/package.spec",
+                "notifications": {"pull_request": {"successful_build": False}},
+            },
+            True,
+        ),
+        (
+            {
+                "specfile_path": "fedora/package.spec",
+                "notifications": {"pull_request": {"successful_build": "nie"}},
+            },
+            False,
+        ),
+        (
+            {
+                "specfile_path": "fedora/package.spec",
+                "notifications": {"pull_request": False},
+            },
+            False,
+        ),
     ],
 )
 def test_package_config_validate(raw, is_valid):
     if not is_valid:
         with pytest.raises((ValidationError, ValueError)):
             PackageConfig.get_from_dict(raw)
     else:
         PackageConfig.get_from_dict(raw)
 
 
 @pytest.mark.parametrize(
     "raw",
     [
-        {},
         # {"specfile_path": "test/spec/file/path", "something": "different"},
         {
             "specfile_path": "test/spec/file/path",
             "jobs": [{"trigger": "release", "release_to": ["f28"]}],
-        },
+        }
     ],
 )
 def test_package_config_parse_error(raw):
     with pytest.raises(Exception):
         PackageConfig.get_from_dict(raw_dict=raw)
 
 
 @pytest.mark.parametrize(
     "raw,expected",
     [
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/package.spec"],
                 "jobs": [get_job_config_dict_full()],
                 "downstream_package_name": "package",
                 "create_pr": False,
             },
@@ -334,16 +355,17 @@
                         )
                     ]
                 ),
                 jobs=[get_job_config_full()],
                 downstream_package_name="package",
                 create_pr=False,
             ),
+            id="specfile_path+synced_files+job_config_full+downstream_package_name+create_pr",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": [
                     "fedora/package.spec",
                     "somefile",
                     "other",
                     "directory/files",
@@ -362,16 +384,17 @@
                         SyncFilesItem(src="other", dest="other"),
                         SyncFilesItem(src="directory/files", dest="directory/files"),
                     ]
                 ),
                 jobs=[get_job_config_simple()],
                 downstream_package_name="package",
             ),
+            id="specfile_path+synced_files+job_config_dict_simple+downstream_package_name",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/package.spec"],
                 "jobs": [get_job_config_dict_full()],
                 "downstream_package_name": "package",
             },
             PackageConfig(
@@ -382,16 +405,17 @@
                             src="fedora/package.spec", dest="fedora/package.spec"
                         )
                     ]
                 ),
                 jobs=[get_job_config_full()],
                 downstream_package_name="package",
             ),
+            id="specfile_path+synced_files(spec_only)+job_config_full+downstream_package_name",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/package.spec", "somefile"],
                 "jobs": [get_job_config_dict_full()],
                 "downstream_package_name": "package",
             },
             PackageConfig(
@@ -403,16 +427,17 @@
                         ),
                         SyncFilesItem(src="somefile", dest="somefile"),
                     ]
                 ),
                 jobs=[get_job_config_full()],
                 downstream_package_name="package",
             ),
+            id="specfile_path+synced_files+job_config_full+downstream_package_name",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/package.spec"],
                 "jobs": [get_job_config_dict_full()],
                 "upstream_project_url": "https://github.com/asd/qwe",
                 "upstream_package_name": "qwe",
                 "dist_git_base_url": "https://something.wicked",
@@ -429,16 +454,18 @@
                 ),
                 jobs=[get_job_config_full()],
                 upstream_project_url="https://github.com/asd/qwe",
                 upstream_package_name="qwe",
                 dist_git_base_url="https://something.wicked",
                 downstream_package_name="package",
             ),
+            id="specfile_path+synced_files+job_config_dict_full+upstream_project_url"
+            "+upstream_package_name+dist_git_base_url+downstream_package_name",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "actions": {
                     "pre-sync": "some/pre-sync/command --option",
                     "get-current-version": "get-me-version",
                 },
                 "jobs": [],
@@ -455,16 +482,18 @@
                 },
                 jobs=[],
                 upstream_project_url="https://github.com/asd/qwe",
                 upstream_package_name="qwe",
                 dist_git_base_url="https://something.wicked",
                 downstream_package_name="package",
             ),
+            id="specfile_path+actions+empty_jobs+upstream_project_url"
+            "+upstream_package_name+dist_git_base_url+downstream_package_name",
         ),
-        (
+        pytest.param(
             {
                 "specfile_path": "fedora/package.spec",
                 "synced_files": ["fedora/package.spec"],
                 "downstream_package_name": "package",
             },
             PackageConfig(
                 specfile_path="fedora/package.spec",
@@ -474,24 +503,25 @@
                             src="fedora/package.spec", dest="fedora/package.spec"
                         )
                     ]
                 ),
                 jobs=get_default_job_config(),
                 downstream_package_name="package",
             ),
+            id="specfile_path+synced_files+downstream_package_name",
         ),
     ],
 )
 def test_package_config_parse(raw, expected):
     package_config = PackageConfig.get_from_dict(raw_dict=raw)
     assert package_config
     # tests for https://github.com/packit-service/packit-service/pull/342
     if expected.jobs:
         for j in package_config.jobs:
-            assert j.job
+            assert j.type
     assert package_config == expected
 
 
 @pytest.mark.parametrize(
     "raw,expected",
     [
         (
@@ -564,27 +594,41 @@
         '{"src": ".packit.yaml", "dest": ".packit2.yaml"}]}',
     ],
 )
 def test_get_package_config_from_repo(content):
     gp = flexmock(GitProject)
     gp.should_receive("full_repo_name").and_return("a/b")
     gp.should_receive("get_file_content").and_return(content)
+    gp.should_receive("get_files").and_return(["packit.spec"])
     git_project = GitProject(repo="", service=GitService(), namespace="")
     config = get_package_config_from_repo(sourcegit_project=git_project, ref="")
     assert isinstance(config, PackageConfig)
     assert Path(config.specfile_path).name == "packit.spec"
     assert config.synced_files == SyncFilesConfig(
         files_to_sync=[
             SyncFilesItem(src="packit.spec", dest="packit.spec"),
             SyncFilesItem(src=".packit.yaml", dest=".packit2.yaml"),
         ]
     )
     assert config.create_pr
 
 
+@pytest.mark.parametrize("content", ["{}"])
+def test_get_package_config_from_repo_spec_file_not_defined(content):
+    gp = flexmock(GitProject)
+    gp.should_receive("full_repo_name").and_return("a/b")
+    gp.should_receive("get_file_content").and_return(content)
+    gp.should_receive("get_files").and_return(["packit.spec"])
+    git_project = GitProject(repo="", service=GitService(), namespace="")
+    config = get_package_config_from_repo(sourcegit_project=git_project, ref="")
+    assert isinstance(config, PackageConfig)
+    assert Path(config.specfile_path).name == "packit.spec"
+    assert config.create_pr
+
+
 def test_get_user_config(tmpdir):
     user_config_file_path = Path(tmpdir) / ".packit.yaml"
     user_config_file_path.write_text(
         "---\n"
         "debug: true\n"
         "fas_user: rambo\n"
         "keytab_path: './rambo.keytab'\n"
@@ -692,7 +736,17 @@
                 ]
             ),
         ),
     ],
 )
 def test_get_all_files_to_sync(package_config, all_synced_files):
     assert package_config.get_all_files_to_sync() == all_synced_files
+
+
+def test_get_local_specfile_path():
+    assert str(get_local_specfile_path(UP_OSBUILD)) == "osbuild.spec"
+    assert not get_local_specfile_path(SYNC_FILES)
+
+
+def test_notifications_section():
+    pc = PackageConfig.get_from_dict({"specfile_path": "package.spec"})
+    assert pc.notifications.pull_request.successful_build
```

### Comparing `packitos-0.8.1/tests/unit/test_config_aliases.py` & `packitos-0.9.0/tests/unit/test_config_aliases.py`

 * *Files 11% similar despite different names*

```diff
@@ -9,16 +9,16 @@
     [
         ("fedora-29", {"fedora-29"}),
         ("epel-8", {"epel-8"}),
         ("fedora-rawhide", {"fedora-rawhide"}),
         ("openmandriva-rolling", {"openmandriva-rolling"}),
         ("opensuse-leap-15.0", {"opensuse-leap-15.0"}),
         ("fedora-stable", {"fedora-30", "fedora-31"}),
-        ("fedora-development", {"fedora-rawhide"}),
-        ("fedora-all", {"fedora-rawhide", "fedora-30", "fedora-31"}),
+        ("fedora-development", {"fedora-rawhide", "fedora-32"}),
+        ("fedora-all", {"fedora-rawhide", "fedora-30", "fedora-31", "fedora-32"}),
         ("centos-stream", {"centos-stream"}),
     ],
 )
 def test_get_versions(name, versions):
     assert get_versions(name) == versions
 
 
@@ -41,23 +41,28 @@
         ("epel-8", {"epel-8-x86_64"}),
         ("fedora-rawhide", {"fedora-rawhide-x86_64"}),
         ("openmandriva-rolling", {"openmandriva-rolling-x86_64"}),
         ("opensuse-leap-15.0", {"opensuse-leap-15.0-x86_64"}),
         ("centos-stream", {"centos-stream-x86_64"}),
         ("centos-stream-x86_64", {"centos-stream-x86_64"}),
         ("fedora-stable", {"fedora-30-x86_64", "fedora-31-x86_64"}),
-        ("fedora-development", {"fedora-rawhide-x86_64"}),
+        ("fedora-development", {"fedora-rawhide-x86_64", "fedora-32-x86_64"}),
         ("fedora-29-x86_64", {"fedora-29-x86_64"}),
         ("fedora-29-aarch64", {"fedora-29-aarch64"}),
         ("fedora-29-i386", {"fedora-29-i386"}),
         ("fedora-stable-aarch64", {"fedora-30-aarch64", "fedora-31-aarch64"}),
-        ("fedora-development-aarch64", {"fedora-rawhide-aarch64"}),
+        ("fedora-development-aarch64", {"fedora-rawhide-aarch64", "fedora-32-aarch64"}),
         (
             "fedora-all",
-            {"fedora-rawhide-x86_64", "fedora-30-x86_64", "fedora-31-x86_64"},
+            {
+                "fedora-rawhide-x86_64",
+                "fedora-30-x86_64",
+                "fedora-31-x86_64",
+                "fedora-32-x86_64",
+            },
         ),
     ],
 )
 def test_get_build_targets(name, targets):
     assert get_build_targets(name) == targets
 
 
@@ -90,21 +95,21 @@
     "name,branches",
     [
         ("fedora-29", {"f29"}),
         ("fedora-rawhide", {"master"}),
         ("rawhide", {"master"}),
         ("master", {"master"}),
         ("f30", {"f30"}),
-        ("fedora-development", {"master"}),
+        ("fedora-development", {"master", "f32"}),
         ("fedora-stable", {"f30", "f31"}),
         ("epel-7", {"epel7"}),
         ("epel7", {"epel7"}),
         ("el6", {"el6"}),
         ("epel-6", {"el6"}),
-        ("fedora-all", {"master", "f30", "f31"}),
+        ("fedora-all", {"master", "f30", "f31", "f32"}),
     ],
 )
 def test_get_branches(name, branches):
     assert get_branches(name) == branches
 
 
 @pytest.mark.parametrize(
```

### Comparing `packitos-0.8.1/tests/unit/test_local_project.py` & `packitos-0.9.0/tests/unit/test_local_project.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_security.py` & `packitos-0.9.0/tests/unit/test_security.py`

 * *Files 6% similar despite different names*

```diff
@@ -97,15 +97,15 @@
     key, sign, allowed_keys, local_keys, valid, download_times
 ):
     gpg_flexmock = flexmock(GPG)
     gpg_flexmock.should_receive("list_keys").and_return(
         flexmock(fingerprints=local_keys)
     )
     gpg_flexmock.should_receive("recv_keys").and_return(
-        flexmock(fingerprints=flexmock())
+        flexmock(fingerprints=["fingerprint"])
     ).times(download_times)
 
     repo_mock = flexmock(
         git=flexmock()
         .should_receive("show")
         .and_return(sign)
         .and_return(key)
@@ -150,18 +150,18 @@
     local_keys_after_download,
     valid,
     download_times,
 ):
     gpg_flexmock = flexmock(GPG)
     gpg_flexmock.should_receive("list_keys").and_return(
         flexmock(fingerprints=local_keys)
-    ).and_return(flexmock(fingerprints=local_keys))
+    )
 
     gpg_flexmock.should_receive("recv_keys").and_return(
-        flexmock(fingerprints=flexmock())
+        flexmock(fingerprints=["fingerprint"])
     ).times(download_times)
 
     repo_mock = flexmock(
         git=flexmock()
         .should_receive("show")
         .and_return(first_sign)
         .and_return(key)
@@ -180,21 +180,33 @@
 def test_check_signature_of_commit_key_not_found():
     gpg_flexmock = flexmock(GPG)
 
     # No key present
     gpg_flexmock.should_receive("list_keys").and_return(flexmock(fingerprints=[]))
 
     # No key received
-    gpg_flexmock.should_receive("recv_keys").and_return(
-        flexmock(fingerprints=[])
-    ).once()
+    gpg_flexmock.should_receive("recv_keys").and_return(flexmock(fingerprints=[]))
 
     # Signature cannot be checked
     repo_mock = flexmock(git=flexmock().should_receive("show").and_return("E").mock())
 
     verifier = CommitVerifier()
     with pytest.raises(PackitException) as ex:
         verifier.check_signature_of_commit(
             commit=flexmock(hexsha="abcd", repo=repo_mock),
             possible_key_fingerprints=["a"],
         )
     assert "Cannot receive" in str(ex)
+
+
+# This could possibly but unlikely fail if all the default key servers are down.
+@pytest.mark.parametrize(
+    "keyid, ok",
+    [("A3E9A812AAB73DA7", True,), ("NOTEXISTING", False,)],  # Jirka's key id
+)
+def test_download_gpg_key_if_needed(keyid, ok):
+    cf = CommitVerifier()
+    if ok:
+        assert cf.download_gpg_key_if_needed(keyid)
+    else:
+        with pytest.raises(PackitException):
+            cf.download_gpg_key_if_needed(keyid)
```

### Comparing `packitos-0.8.1/tests/unit/test_sync.py` & `packitos-0.9.0/tests/unit/test_sync.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_unicodez.py` & `packitos-0.9.0/tests/unit/test_unicodez.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_upstream.py` & `packitos-0.9.0/tests/unit/test_upstream.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests/unit/test_utils.py` & `packitos-0.9.0/tests/unit/test_utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -17,26 +17,28 @@
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
-import pytest
+import os
 import sys
+import pytest
+
 from flexmock import flexmock
+from pkg_resources import DistributionNotFound, Distribution
 
 from packit.exceptions import PackitException, ensure_str
 from packit.utils import (
     get_namespace_and_repo_name,
     git_remote_url_to_https_url,
     run_command,
     get_packit_version,
 )
-from pkg_resources import DistributionNotFound, Distribution
 
 
 @pytest.mark.parametrize(
     "url,namespace,repo_name",
     [
         ("https://github.com/org/name", "org", "name"),
         ("https://github.com/org/name/", "org", "name"),
@@ -96,7 +98,14 @@
 @pytest.mark.parametrize(
     "inp,exp",
     (("asd", "asd"), (b"asd", "asd"), ("🍺", "🍺"), (b"\xf0\x9f\x8d\xba", "🍺")),
     ids=("asd", "bytes-asd", "beer-str", "beer-bytes"),
 )
 def test_ensure_str(inp, exp):
     assert ensure_str(inp) == exp
+
+
+@pytest.mark.parametrize(
+    "to,from_,exp", (("/", "/", "."), ("/a", "/a/b", ".."), ("/a", "/c", "../a"))
+)
+def test_relative_to(to, from_, exp):
+    assert os.path.relpath(to, from_) == exp
```

### Comparing `packitos-0.8.1/tests_recording/__init__.py` & `packitos-0.9.0/tests_recording/__init__.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_api.py` & `packitos-0.9.0/tests_recording/test_api.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_builds.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_builds.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_distgen_versions.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_distgen_versions.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_dowstream_pr.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_dowstream_pr.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_status.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_status.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_up_releases.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_up_releases.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_updates.yaml` & `packitos-0.9.0/tests_recording/test_data/test_status/tests_recording.test_status.TestStatus.test_updates.yaml`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/test_status.py` & `packitos-0.9.0/tests_recording/test_status.py`

 * *Files identical despite different names*

### Comparing `packitos-0.8.1/tests_recording/testbase.py` & `packitos-0.9.0/tests_recording/testbase.py`

 * *Files identical despite different names*

