# Comparing `tmp/click-reviewers-tools-0.77.tar.gz` & `tmp/click-reviewers-tools-0.78.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "click-reviewers-tools-0.77.tar", last modified: Tue Feb 21 14:46:16 2023, max compression
+gzip compressed data, was "click-reviewers-tools-0.78.tar", last modified: Thu Apr  6 13:27:58 2023, max compression
```

## Comparing `click-reviewers-tools-0.77.tar` & `click-reviewers-tools-0.78.tar`

### file list

```diff
@@ -1,86 +1,86 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.575311 click-reviewers-tools-0.77/
--rw-rw-rw-   0 root         (0) root         (0)    35147 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/COPYING
--rw-rw-rw-   0 root         (0) root         (0)      261 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)       86 2023-02-21 14:46:16.575311 click-reviewers-tools-0.77/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     2089 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.554309 click-reviewers-tools-0.77/bin/
--rwxrwxrwx   0 root         (0) root         (0)      913 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-bin-path
--rwxrwxrwx   0 root         (0) root         (0)      931 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-content-hub
--rwxrwxrwx   0 root         (0) root         (0)      894 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-desktop
--rwxrwxrwx   0 root         (0) root         (0)      920 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-framework
--rwxrwxrwx   0 root         (0) root         (0)      938 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-functional
--rwxrwxrwx   0 root         (0) root         (0)      885 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-lint
--rwxrwxrwx   0 root         (0) root         (0)      949 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-online-accounts
--rwxrwxrwx   0 root         (0) root         (0)      931 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-push-helper
--rwxrwxrwx   0 root         (0) root         (0)      896 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-scope
--rwxrwxrwx   0 root         (0) root         (0)      909 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-security
--rwxrwxrwx   0 root         (0) root         (0)      914 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-skeleton
--rwxrwxrwx   0 root         (0) root         (0)      908 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-systemd
--rwxrwxrwx   0 root         (0) root         (0)      949 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-check-url-dispatcher
--rwxrwxrwx   0 root         (0) root         (0)     6760 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-review
--rwxrwxrwx   0 root         (0) root         (0)     1282 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-run-checks
--rwxrwxrwx   0 root         (0) root         (0)     6884 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/click-show-files
--rwxrwxrwx   0 root         (0) root         (0)      288 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/detect-package
--rwxrwxrwx   0 root         (0) root         (0)     1546 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/empty-click
--rwxrwxrwx   0 root         (0) root         (0)     2113 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/repack-click
--rwxrwxrwx   0 root         (0) root         (0)      332 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/bin/unpack-package
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.555309 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/
--rw-r--r--   0 root         (0) root         (0)       86 2023-02-21 14:46:16.000000 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2159 2023-02-21 14:46:16.000000 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-02-21 14:46:16.000000 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       56 2023-02-21 14:46:16.000000 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       13 2023-02-21 14:46:16.000000 click-reviewers-tools-0.77/click_reviewers_tools.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.565310 click-reviewers-tools-0.77/clickreviews/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    14827 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/apparmor.py
--rw-rw-rw-   0 root         (0) root         (0)    21755 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/common.py
--rw-rw-rw-   0 root         (0) root         (0)     7743 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_bin_path.py
--rw-rw-rw-   0 root         (0) root         (0)    21600 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_common.py
--rw-rw-rw-   0 root         (0) root         (0)     4841 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_content_hub.py
--rw-rw-rw-   0 root         (0) root         (0)    36013 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_desktop.py
--rw-rw-rw-   0 root         (0) root         (0)    10104 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_framework.py
--rw-rw-rw-   0 root         (0) root         (0)    16205 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_functional.py
--rw-rw-rw-   0 root         (0) root         (0)     3594 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_language_packs.py
--rw-rw-rw-   0 root         (0) root         (0)    49990 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_lint.py
--rw-rw-rw-   0 root         (0) root         (0)    15922 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_online_accounts.py
--rw-rw-rw-   0 root         (0) root         (0)     5596 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_push_helper.py
--rw-rw-rw-   0 root         (0) root         (0)     7237 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_scope.py
--rw-rw-rw-   0 root         (0) root         (0)    62507 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_security.py
--rw-rw-rw-   0 root         (0) root         (0)     2678 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_skeleton.py
--rw-rw-rw-   0 root         (0) root         (0)    26054 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_systemd.py
--rw-rw-rw-   0 root         (0) root         (0)    43114 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_tests.py
--rw-rw-rw-   0 root         (0) root         (0)     6662 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/cr_url_dispatcher.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.565310 click-reviewers-tools-0.77/clickreviews/data/
--rw-rw-rw-   0 root         (0) root         (0)     2870 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/data/icon.png
--rw-rw-rw-   0 root         (0) root         (0)     5429 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/frameworks.py
--rw-rw-rw-   0 root         (0) root         (0)     2442 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/modules.py
--rw-rw-rw-   0 root         (0) root         (0)     6931 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/overrides.py
--rw-rw-rw-   0 root         (0) root         (0)     3435 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/remote.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.572311 click-reviewers-tools-0.77/clickreviews/tests/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4850 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_aaa_example_cr_skeleton.py
--rw-rw-rw-   0 root         (0) root         (0)     6934 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_bin_path.py
--rw-rw-rw-   0 root         (0) root         (0)     5766 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_common.py
--rw-rw-rw-   0 root         (0) root         (0)     7203 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_content_hub.py
--rw-rw-rw-   0 root         (0) root         (0)    43426 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_desktop.py
--rw-rw-rw-   0 root         (0) root         (0)     8757 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_framework.py
--rw-rw-rw-   0 root         (0) root         (0)    83423 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_lint.py
--rw-rw-rw-   0 root         (0) root         (0)    27032 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_online_accounts.py
--rw-rw-rw-   0 root         (0) root         (0)     8157 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_push_helper.py
--rw-rw-rw-   0 root         (0) root         (0)    10592 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_scope.py
--rw-rw-rw-   0 root         (0) root         (0)   113985 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_security.py
--rw-rw-rw-   0 root         (0) root         (0)    39587 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_systemd.py
--rw-rw-rw-   0 root         (0) root         (0)    11869 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_cr_url_dispatcher.py
--rw-rw-rw-   0 root         (0) root         (0)     1076 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_modules.py
--rw-rw-rw-   0 root         (0) root         (0)     1101 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/test_remote.py
--rw-rw-rw-   0 root         (0) root         (0)     9488 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/clickreviews/tests/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-21 14:46:16.575311 click-reviewers-tools-0.77/debian/
--rw-rw-rw-   0 root         (0) root         (0)    43401 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/changelog
--rw-rw-rw-   0 root         (0) root         (0)        2 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/compat
--rw-rw-rw-   0 root         (0) root         (0)     1094 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/control
--rw-rw-rw-   0 root         (0) root         (0)      924 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/copyright
--rw-rw-rw-   0 root         (0) root         (0)       10 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/docs
--rw-rw-rw-   0 root         (0) root         (0)       41 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/links
--rwxrwxrwx   0 root         (0) root         (0)     1503 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/debian/rules
--rw-rw-rw-   0 root         (0) root         (0)       69 2023-02-21 14:46:16.576311 click-reviewers-tools-0.77/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)      755 2023-02-21 14:46:15.000000 click-reviewers-tools-0.77/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.744434 click-reviewers-tools-0.78/
+-rw-rw-rw-   0 root         (0) root         (0)    35147 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/COPYING
+-rw-rw-rw-   0 root         (0) root         (0)      261 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)       86 2023-04-06 13:27:58.744434 click-reviewers-tools-0.78/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     2089 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.723433 click-reviewers-tools-0.78/bin/
+-rwxrwxrwx   0 root         (0) root         (0)      913 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-bin-path
+-rwxrwxrwx   0 root         (0) root         (0)      931 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-content-hub
+-rwxrwxrwx   0 root         (0) root         (0)      894 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-desktop
+-rwxrwxrwx   0 root         (0) root         (0)      920 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-framework
+-rwxrwxrwx   0 root         (0) root         (0)      938 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-functional
+-rwxrwxrwx   0 root         (0) root         (0)      885 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-lint
+-rwxrwxrwx   0 root         (0) root         (0)      949 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-online-accounts
+-rwxrwxrwx   0 root         (0) root         (0)      931 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-push-helper
+-rwxrwxrwx   0 root         (0) root         (0)      896 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-scope
+-rwxrwxrwx   0 root         (0) root         (0)      909 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-security
+-rwxrwxrwx   0 root         (0) root         (0)      914 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-skeleton
+-rwxrwxrwx   0 root         (0) root         (0)      908 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-systemd
+-rwxrwxrwx   0 root         (0) root         (0)      949 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-check-url-dispatcher
+-rwxrwxrwx   0 root         (0) root         (0)     6760 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-review
+-rwxrwxrwx   0 root         (0) root         (0)     1282 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-run-checks
+-rwxrwxrwx   0 root         (0) root         (0)     6884 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/click-show-files
+-rwxrwxrwx   0 root         (0) root         (0)      288 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/detect-package
+-rwxrwxrwx   0 root         (0) root         (0)     1546 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/empty-click
+-rwxrwxrwx   0 root         (0) root         (0)     2113 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/repack-click
+-rwxrwxrwx   0 root         (0) root         (0)      332 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/bin/unpack-package
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.725433 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/
+-rw-r--r--   0 root         (0) root         (0)       86 2023-04-06 13:27:58.000000 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2159 2023-04-06 13:27:58.000000 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:27:58.000000 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       56 2023-04-06 13:27:58.000000 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-06 13:27:58.000000 click-reviewers-tools-0.78/click_reviewers_tools.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.734434 click-reviewers-tools-0.78/clickreviews/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    14827 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/apparmor.py
+-rw-rw-rw-   0 root         (0) root         (0)    21755 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/common.py
+-rw-rw-rw-   0 root         (0) root         (0)     7743 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_bin_path.py
+-rw-rw-rw-   0 root         (0) root         (0)    21600 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_common.py
+-rw-rw-rw-   0 root         (0) root         (0)     4841 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_content_hub.py
+-rw-rw-rw-   0 root         (0) root         (0)    36327 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_desktop.py
+-rw-rw-rw-   0 root         (0) root         (0)    10104 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_framework.py
+-rw-rw-rw-   0 root         (0) root         (0)    17291 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_functional.py
+-rw-rw-rw-   0 root         (0) root         (0)     3594 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_language_packs.py
+-rw-rw-rw-   0 root         (0) root         (0)    49990 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_lint.py
+-rw-rw-rw-   0 root         (0) root         (0)    15922 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_online_accounts.py
+-rw-rw-rw-   0 root         (0) root         (0)     5596 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_push_helper.py
+-rw-rw-rw-   0 root         (0) root         (0)     7237 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_scope.py
+-rw-rw-rw-   0 root         (0) root         (0)    62507 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_security.py
+-rw-rw-rw-   0 root         (0) root         (0)     2678 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_skeleton.py
+-rw-rw-rw-   0 root         (0) root         (0)    26054 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_systemd.py
+-rw-rw-rw-   0 root         (0) root         (0)    43114 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_tests.py
+-rw-rw-rw-   0 root         (0) root         (0)     6662 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/cr_url_dispatcher.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.734434 click-reviewers-tools-0.78/clickreviews/data/
+-rw-rw-rw-   0 root         (0) root         (0)     2870 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/data/icon.png
+-rw-rw-rw-   0 root         (0) root         (0)     5429 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/frameworks.py
+-rw-rw-rw-   0 root         (0) root         (0)     2442 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/modules.py
+-rw-rw-rw-   0 root         (0) root         (0)     6931 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/overrides.py
+-rw-rw-rw-   0 root         (0) root         (0)     3435 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/remote.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.742434 click-reviewers-tools-0.78/clickreviews/tests/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4850 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_aaa_example_cr_skeleton.py
+-rw-rw-rw-   0 root         (0) root         (0)     6934 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_bin_path.py
+-rw-rw-rw-   0 root         (0) root         (0)     5766 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_common.py
+-rw-rw-rw-   0 root         (0) root         (0)     7203 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_content_hub.py
+-rw-rw-rw-   0 root         (0) root         (0)    44349 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_desktop.py
+-rw-rw-rw-   0 root         (0) root         (0)     8757 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_framework.py
+-rw-rw-rw-   0 root         (0) root         (0)    83423 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_lint.py
+-rw-rw-rw-   0 root         (0) root         (0)    27032 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_online_accounts.py
+-rw-rw-rw-   0 root         (0) root         (0)     8157 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_push_helper.py
+-rw-rw-rw-   0 root         (0) root         (0)    10592 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_scope.py
+-rw-rw-rw-   0 root         (0) root         (0)   113985 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_security.py
+-rw-rw-rw-   0 root         (0) root         (0)    39587 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_systemd.py
+-rw-rw-rw-   0 root         (0) root         (0)    11869 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_cr_url_dispatcher.py
+-rw-rw-rw-   0 root         (0) root         (0)     1076 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_modules.py
+-rw-rw-rw-   0 root         (0) root         (0)     1101 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/test_remote.py
+-rw-rw-rw-   0 root         (0) root         (0)     9488 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/clickreviews/tests/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:27:58.744434 click-reviewers-tools-0.78/debian/
+-rw-rw-rw-   0 root         (0) root         (0)    43595 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/changelog
+-rw-rw-rw-   0 root         (0) root         (0)        2 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/compat
+-rw-rw-rw-   0 root         (0) root         (0)     1094 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/control
+-rw-rw-rw-   0 root         (0) root         (0)      924 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/copyright
+-rw-rw-rw-   0 root         (0) root         (0)       10 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/docs
+-rw-rw-rw-   0 root         (0) root         (0)       41 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/links
+-rwxrwxrwx   0 root         (0) root         (0)     1503 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/debian/rules
+-rw-rw-rw-   0 root         (0) root         (0)       69 2023-04-06 13:27:58.745435 click-reviewers-tools-0.78/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)      755 2023-04-06 13:27:57.000000 click-reviewers-tools-0.78/setup.py
```

### Comparing `click-reviewers-tools-0.77/COPYING` & `click-reviewers-tools-0.78/COPYING`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/README.md` & `click-reviewers-tools-0.78/README.md`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-bin-path` & `click-reviewers-tools-0.78/bin/click-check-bin-path`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-content-hub` & `click-reviewers-tools-0.78/bin/click-check-content-hub`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-desktop` & `click-reviewers-tools-0.78/bin/click-check-desktop`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-framework` & `click-reviewers-tools-0.78/bin/click-check-framework`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-functional` & `click-reviewers-tools-0.78/bin/click-check-functional`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-lint` & `click-reviewers-tools-0.78/bin/click-check-lint`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-online-accounts` & `click-reviewers-tools-0.78/bin/click-check-online-accounts`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-push-helper` & `click-reviewers-tools-0.78/bin/click-check-push-helper`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-scope` & `click-reviewers-tools-0.78/bin/click-check-scope`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-security` & `click-reviewers-tools-0.78/bin/click-check-security`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-skeleton` & `click-reviewers-tools-0.78/bin/click-check-skeleton`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-systemd` & `click-reviewers-tools-0.78/bin/click-check-systemd`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-check-url-dispatcher` & `click-reviewers-tools-0.78/bin/click-check-url-dispatcher`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-review` & `click-reviewers-tools-0.78/bin/click-review`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-run-checks` & `click-reviewers-tools-0.78/bin/click-run-checks`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/click-show-files` & `click-reviewers-tools-0.78/bin/click-show-files`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/empty-click` & `click-reviewers-tools-0.78/bin/empty-click`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/bin/repack-click` & `click-reviewers-tools-0.78/bin/repack-click`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/click_reviewers_tools.egg-info/SOURCES.txt` & `click-reviewers-tools-0.78/click_reviewers_tools.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/apparmor.py` & `click-reviewers-tools-0.78/clickreviews/apparmor.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/common.py` & `click-reviewers-tools-0.78/clickreviews/common.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_bin_path.py` & `click-reviewers-tools-0.78/clickreviews/cr_bin_path.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_common.py` & `click-reviewers-tools-0.78/clickreviews/cr_common.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_content_hub.py` & `click-reviewers-tools-0.78/clickreviews/cr_content_hub.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_desktop.py` & `click-reviewers-tools-0.78/clickreviews/cr_desktop.py`

 * *Files 1% similar despite different names*

```diff
@@ -68,16 +68,17 @@
                               ]
         self.key_alt = {'X-Lomiri-Touch': 'X-Ubuntu-Touch'}
         self.expected_execs = ['qmlscene',
                                'webbrowser-app',
                                'webapp-container',
                                'ubuntu-html5-app-launcher',
                                ]
-        self.deprecated_execs = ['cordova-ubuntu-2.8',
-                                 ]
+        self.deprecated_execs = ['cordova-ubuntu-2.8']
+        self.allowed_extension_execs = ['.py']
+
         # TODO: the desktop hook will actually handle this correctly
         self.blacklisted_keys = ['Path']
 
     def _extract_desktop_entry(self, app):
         '''Get DesktopEntry for desktop file and verify it'''
         d = self.manifest['hooks'][app]['desktop']
         fn = os.path.join(self.unpack_dir, d)
@@ -221,22 +222,28 @@
                 t = 'error'
                 s = "absolute path '%s' for Exec given in .desktop file." % \
                     de.getExec()
                 link = ('http://askubuntu.com/questions/417381/'
                         'what-does-desktop-exec-mean/417382')
             elif de.getExec().split()[0] not in self.expected_execs:
                 if self.pkg_arch[0] == "all":  # interpreted file
-                    template = "found %s Exec with architecture '%s': %s"
-                    if de.getExec().split()[0] not in self.deprecated_execs:
-                        verb = 'unexpected'
+                    check = os.path.splitext(de.getExec().split()[0])
+
+                    if check[1] in self.allowed_extension_execs:
+                        s = 'ALlowed exec with %s extension' % check[1]
+                        t = 'info'
                     else:
-                        verb = 'deprecated'
-                    s = template % \
-                        (verb, self.pkg_arch[0], de.getExec().split()[0])
-                    t = 'warn'
+                        template = "found %s Exec with architecture '%s': %s"
+                        if de.getExec().split()[0] not in self.deprecated_execs:
+                            verb = 'unexpected'
+                        else:
+                            verb = 'deprecated'
+                        s = template % \
+                            (verb, self.pkg_arch[0], de.getExec().split()[0])
+                        t = 'warn'
                 else:                        # compiled
                     # TODO: this can be a lot smarter
                     s = "Non-standard Exec with architecture " + \
                         "'%s': %s (ok for compiled code)" % \
                         (self.pkg_arch[0], de.getExec().split()[0])
                     t = 'info'
             self._add_result(t, n, s, link)
```

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_framework.py` & `click-reviewers-tools-0.78/clickreviews/cr_framework.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_functional.py` & `click-reviewers-tools-0.78/clickreviews/cr_functional.py`

 * *Files 2% similar despite different names*

```diff
@@ -348,14 +348,44 @@
                     "Ubuntu.Components.Extras.Browser >= 0.2 or " + \
                     "Oxide instead): %s" % " ,".join(qmls)
                 link = ("http://askubuntu.com/questions/417342/what-does-"
                         "functional-qml-application-uses-qtwebkit-mean/417343")
 
         self._add_result(t, n, s, link)
 
+    def check_lomiri(self):
+        '''Check that QML applications don't use Lomiri types with old framework'''
+        if not self.is_click and not self.is_snap1:
+            return
+
+        t = 'info'
+        n = self._get_check_name('qml_application_uses_lomiri')
+        s = "OK"
+        link = None
+
+        frameworks = self.manifest['framework'].split(',')
+
+        qmls = []
+        pat_imp = re.compile(r'^\s*import\s+Lomiri', flags=re.MULTILINE)
+        for i in self.qml_files:
+            qml = open_file_read(i).read()
+            if pat_imp.search(str(qml)):
+                qmls.append(os.path.relpath(i, self.unpack_dir))
+
+        old_fw = [fw for fw in frameworks
+                  if apt_pkg.version_compare(fw, 'ubuntu-sdk-20.04') < 0]
+
+        if len(qmls) > 0 and old_fw:
+            t = 'error'
+            s = "Framework(s) %s do not support Lomiri types, used in QML files: %s" % \
+                (" ,".join(old_fw), " ,".join(qmls))
+            link = ("https://gitlab.com/clickable/click-reviewers-tools/-/issues/6")
+
+        self._add_result(t, n, s, link)
+
     def check_friends(self):
         '''Check that QML applications don't use deprecated Friends API'''
         if not self.is_click and not self.is_snap1:
             return
 
         t = 'info'
         n = self._get_check_name('qml_application_uses_friends')
```

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_language_packs.py` & `click-reviewers-tools-0.78/clickreviews/cr_language_packs.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_lint.py` & `click-reviewers-tools-0.78/clickreviews/cr_lint.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_online_accounts.py` & `click-reviewers-tools-0.78/clickreviews/cr_online_accounts.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_push_helper.py` & `click-reviewers-tools-0.78/clickreviews/cr_push_helper.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_scope.py` & `click-reviewers-tools-0.78/clickreviews/cr_scope.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_security.py` & `click-reviewers-tools-0.78/clickreviews/cr_security.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_skeleton.py` & `click-reviewers-tools-0.78/clickreviews/cr_skeleton.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_systemd.py` & `click-reviewers-tools-0.78/clickreviews/cr_systemd.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_tests.py` & `click-reviewers-tools-0.78/clickreviews/cr_tests.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/cr_url_dispatcher.py` & `click-reviewers-tools-0.78/clickreviews/cr_url_dispatcher.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/data/icon.png` & `click-reviewers-tools-0.78/clickreviews/data/icon.png`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/frameworks.py` & `click-reviewers-tools-0.78/clickreviews/frameworks.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/modules.py` & `click-reviewers-tools-0.78/clickreviews/modules.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/overrides.py` & `click-reviewers-tools-0.78/clickreviews/overrides.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/remote.py` & `click-reviewers-tools-0.78/clickreviews/remote.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_aaa_example_cr_skeleton.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_aaa_example_cr_skeleton.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_bin_path.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_bin_path.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_common.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_common.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_content_hub.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_content_hub.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_desktop.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_desktop.py`

 * *Files 0% similar despite different names*

```diff
@@ -73,14 +73,34 @@
         self.set_test_desktop(self.default_appname,
                               "Exec", "qmlscene   $@ myApp.qml")
         c.check_desktop_exec()
         r = c.click_report
         expected_counts = {'info': 1, 'warn': 0, 'error': 0}
         self.check_results(r, expected_counts)
 
+    def test_check_desktop_file_has_allowed_extension(self):
+        '''Test check_desktop_exec() - Exec has allowed extension'''
+        c = ClickReviewDesktop(self.test_name)
+        self.set_test_desktop(self.default_appname,
+                              "Exec", "some-script.py")
+        c.check_desktop_exec()
+        r = c.click_report
+        expected_counts = {'info': 1, 'warn': 0, 'error': 0}
+        self.check_results(r, expected_counts)
+
+    def test_check_desktop_file_does_not_has_allowed_extension(self):
+        '''Test check_desktop_exec() - Exec does not have allowed extension'''
+        c = ClickReviewDesktop(self.test_name)
+        self.set_test_desktop(self.default_appname,
+                              "Exec", "some-script.js")
+        c.check_desktop_exec()
+        r = c.click_report
+        expected_counts = {'info': 0, 'warn': 1, 'error': 0}
+        self.check_results(r, expected_counts)
+
     def test_check_desktop_latest_version(self):
         '''Test check_desktop_version()'''
         c = ClickReviewDesktop(self.test_name)
         self.set_test_desktop(self.default_appname,
                               "Version", "1.5")
         c.check_desktop_version()
         r = c.click_report
```

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_framework.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_framework.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_lint.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_lint.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_online_accounts.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_online_accounts.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_push_helper.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_push_helper.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_scope.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_scope.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_security.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_security.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_systemd.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_systemd.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_cr_url_dispatcher.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_cr_url_dispatcher.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_modules.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_modules.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/test_remote.py` & `click-reviewers-tools-0.78/clickreviews/tests/test_remote.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/clickreviews/tests/utils.py` & `click-reviewers-tools-0.78/clickreviews/tests/utils.py`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/debian/changelog` & `click-reviewers-tools-0.78/debian/changelog`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,13 @@
+click-reviewers-tools (0.78) unstable; urgency=medium
+
+  * Python scripts are now allowed in desktop file Execs
+
+ -- Clickable <bhdouglass+clickable@gmail.com>  Thu, 06 Apr 2023 09:23:00 -0500
+
 click-reviewers-tools (0.77) unstable; urgency=medium
 
   * Added support for click migrations
 
  -- Clickable <bhdouglass+clickable@gmail.com>  Tue, 21 Feb 2023 09:42:00 -0500
 
 click-reviewers-tools (0.76) unstable; urgency=medium
```

### Comparing `click-reviewers-tools-0.77/debian/control` & `click-reviewers-tools-0.78/debian/control`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/debian/copyright` & `click-reviewers-tools-0.78/debian/copyright`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/debian/rules` & `click-reviewers-tools-0.78/debian/rules`

 * *Files identical despite different names*

### Comparing `click-reviewers-tools-0.77/setup.py` & `click-reviewers-tools-0.78/setup.py`

 * *Files identical despite different names*

