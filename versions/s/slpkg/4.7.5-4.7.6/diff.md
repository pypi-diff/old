# Comparing `tmp/slpkg-4.7.5.tar.gz` & `tmp/slpkg-4.7.6.tar.gz`

## Comparing `slpkg-4.7.5.tar` & `slpkg-4.7.6.tar`

### file list

```diff
@@ -1,89 +1,97 @@
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:16:19.000000 slpkg-4.7.5/
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slackbuild/
--rw-r--r--   0 dslackw   (1000) users      (100)      941 2023-04-04 18:12:57.000000 slpkg-4.7.5/slackbuild/slack-desc
--rw-r--r--   0 dslackw   (1000) users      (100)      432 2023-04-04 18:12:57.000000 slpkg-4.7.5/slackbuild/doinst.sh
--rw-r--r--   0 dslackw   (1000) users      (100)      304 2023-04-04 18:12:57.000000 slpkg-4.7.5/slackbuild/README
--rwxr-xr-x   0 dslackw   (1000) users      (100)     4281 2023-04-04 18:12:57.000000 slpkg-4.7.5/slackbuild/slpkg.SlackBuild
--rwxr-xr-x   0 dslackw   (1000) users      (100)       70 2023-04-04 18:12:57.000000 slpkg-4.7.5/setup.py
--rw-r--r--   0 dslackw   (1000) users      (100)     6335 2023-04-04 18:12:57.000000 slpkg-4.7.5/README.rst
--rw-r--r--   0 dslackw   (1000) users      (100)       58 2023-04-04 18:12:57.000000 slpkg-4.7.5/requirements.txt
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/configs/
--rw-r--r--   0 dslackw   (1000) users      (100)     8502 2023-04-04 18:12:57.000000 slpkg-4.7.5/configs/repositories.toml
--rw-r--r--   0 dslackw   (1000) users      (100)      273 2023-04-04 18:12:57.000000 slpkg-4.7.5/configs/blacklist.toml
--rw-r--r--   0 dslackw   (1000) users      (100)     2450 2023-04-04 18:12:57.000000 slpkg-4.7.5/configs/slpkg.toml
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/
--rw-r--r--   0 dslackw   (1000) users      (100)     2153 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_configs.py
--rw-r--r--   0 dslackw   (1000) users      (100)      941 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_checks.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2239 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_utilities.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1251 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_sbo_queries.py
--rw-r--r--   0 dslackw   (1000) users      (100)      272 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_blacklist.py
--rw-r--r--   0 dslackw   (1000) users      (100)      588 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_colors.py
--rw-r--r--   0 dslackw   (1000) users      (100)      724 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_upgrade.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2436 2023-04-04 18:12:57.000000 slpkg-4.7.5/tests/test_bin_queries.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1076 2023-04-04 18:12:57.000000 slpkg-4.7.5/LICENSE
--rwxr-xr-x   0 dslackw   (1000) users      (100)     1773 2023-04-04 18:12:57.000000 slpkg-4.7.5/install.sh
--rw-r--r--   0 dslackw   (1000) users      (100)    44035 2023-04-04 18:12:57.000000 slpkg-4.7.5/ChangeLog.txt
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/man/
--rw-r--r--   0 dslackw   (1000) users      (100)     7252 2023-04-04 18:12:57.000000 slpkg-4.7.5/man/slpkg.1
--rw-r--r--   0 dslackw   (1000) users      (100)     8027 2023-04-04 18:12:57.000000 slpkg-4.7.5/man/slpkg-fr.1
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/completion/
--rw-r--r--   0 dslackw   (1000) users      (100)      910 2023-04-04 18:12:57.000000 slpkg-4.7.5/completion/slpkg
--rw-r--r--   0 dslackw   (1000) users      (100)       93 2023-04-04 18:12:57.000000 slpkg-4.7.5/.gitignore
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/binaries/
--rw-r--r--   0 dslackw   (1000) users      (100)     1850 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/binaries/required.py
--rw-r--r--   0 dslackw   (1000) users      (100)     6870 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/binaries/queries.py
--rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/binaries/__init__.py
--rw-r--r--   0 dslackw   (1000) users      (100)     9818 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/binaries/install.py
--rw-r--r--   0 dslackw   (1000) users      (100)    62222 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/install_data.py
--rw-r--r--   0 dslackw   (1000) users      (100)    20789 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/repositories.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2515 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/repo_info.py
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/sbos/
--rw-r--r--   0 dslackw   (1000) users      (100)     4499 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/sbos/queries.py
--rw-r--r--   0 dslackw   (1000) users      (100)    14578 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/sbos/slackbuild.py
--rw-r--r--   0 dslackw   (1000) users      (100)      958 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/sbos/dependencies.py
--rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/sbos/__init__.py
--rw-r--r--   0 dslackw   (1000) users      (100)     3983 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/form_configs.py
--rw-r--r--   0 dslackw   (1000) users      (100)    32105 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/update_repository.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1791 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/progress_bar.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2166 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/downloader.py
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/models/
--rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/models/__init__.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2630 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/models/models.py
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/
--rw-r--r--   0 dslackw   (1000) users      (100)     7147 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/view_package.py
--rw-r--r--   0 dslackw   (1000) users      (100)      629 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/version.py
--rw-r--r--   0 dslackw   (1000) users      (100)     6318 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/cli_menu.py
--rw-r--r--   0 dslackw   (1000) users      (100)     5546 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/ascii.py
--rw-r--r--   0 dslackw   (1000) users      (100)     4004 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/help_commands.py
--rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/__init__.py
--rw-r--r--   0 dslackw   (1000) users      (100)     9630 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/views/views.py
--rw-r--r--   0 dslackw   (1000) users      (100)     3357 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/checks.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1316 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/checksum.py
--rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/__init__.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2196 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/dialog_box.py
--rw-r--r--   0 dslackw   (1000) users      (100)     4853 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/configs.py
--rw-r--r--   0 dslackw   (1000) users      (100)      874 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/clean_logs.py
--rw-r--r--   0 dslackw   (1000) users      (100)     7009 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/utilities.py
--rw-r--r--   0 dslackw   (1000) users      (100)     4072 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/dependees.py
--rw-r--r--   0 dslackw   (1000) users      (100)    10204 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/check_updates.py
--rw-r--r--   0 dslackw   (1000) users      (100)     4070 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/remove_packages.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1522 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/blacklist.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2558 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/download_only.py
--rw-r--r--   0 dslackw   (1000) users      (100)     3142 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/tracking.py
--rw-r--r--   0 dslackw   (1000) users      (100)    29238 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/main.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1461 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/find_installed.py
--rw-r--r--   0 dslackw   (1000) users      (100)     2612 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/upgrade.py
--rw-r--r--   0 dslackw   (1000) users      (100)     3392 2023-04-04 18:12:57.000000 slpkg-4.7.5/slpkg/search.py
--rw-r--r--   0 dslackw   (1000) users      (100)     1311 2023-04-04 18:12:57.000000 slpkg-4.7.5/setup.cfg
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/
--rw-r--r--   0 dslackw   (1000) users      (100)        1 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/dependency_links.txt
--rw-r--r--   0 dslackw   (1000) users      (100)     1082 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/SOURCES.txt
--rw-r--r--   0 dslackw   (1000) users      (100)        6 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/top_level.txt
--rw-r--r--   0 dslackw   (1000) users      (100)       53 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/requires.txt
--rw-r--r--   0 dslackw   (1000) users      (100)     7577 2023-04-04 18:16:15.000000 slpkg-4.7.5/slpkg.egg-info/PKG-INFO
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/tools/
--rwxr-xr-x   0 dslackw   (1000) users      (100)      787 2023-04-04 18:12:57.000000 slpkg-4.7.5/tools/gen_sbo_txt.sh
-drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-04 18:12:57.000000 slpkg-4.7.5/bin/
--rwxr-xr-x   0 dslackw   (1000) users      (100)    11470 2023-04-04 18:12:57.000000 slpkg-4.7.5/bin/slpkg_new-configs
--rwxr-xr-x   0 dslackw   (1000) users      (100)      184 2023-04-04 18:12:57.000000 slpkg-4.7.5/bin/slpkg
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:54:05.000000 slpkg-4.7.6/
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/multilib/
+-rw-r--r--   0 dslackw   (1000) users      (100)    15477 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/multilib/README.ERIC
+-rw-r--r--   0 dslackw   (1000) users      (100)      250 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/multilib/glibc_packages.pkgs
+-rw-r--r--   0 dslackw   (1000) users      (100)      793 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/multilib/README
+-rw-r--r--   0 dslackw   (1000) users      (100)     4508 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/multilib/compat32.pkgs
+-rw-r--r--   0 dslackw   (1000) users      (100)       88 2023-04-06 16:45:48.000000 slpkg-4.7.6/filelists/README
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slackbuild/
+-rw-r--r--   0 dslackw   (1000) users      (100)      941 2023-04-06 16:45:48.000000 slpkg-4.7.6/slackbuild/slack-desc
+-rw-r--r--   0 dslackw   (1000) users      (100)      432 2023-04-06 16:45:48.000000 slpkg-4.7.6/slackbuild/doinst.sh
+-rw-r--r--   0 dslackw   (1000) users      (100)      304 2023-04-06 16:45:48.000000 slpkg-4.7.6/slackbuild/README
+-rwxr-xr-x   0 dslackw   (1000) users      (100)     4281 2023-04-06 16:45:48.000000 slpkg-4.7.6/slackbuild/slpkg.SlackBuild
+-rwxr-xr-x   0 dslackw   (1000) users      (100)       70 2023-04-06 16:45:48.000000 slpkg-4.7.6/setup.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     6655 2023-04-06 16:45:48.000000 slpkg-4.7.6/README.rst
+-rw-r--r--   0 dslackw   (1000) users      (100)       58 2023-04-06 16:45:48.000000 slpkg-4.7.6/requirements.txt
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/configs/
+-rw-r--r--   0 dslackw   (1000) users      (100)     8949 2023-04-06 16:45:48.000000 slpkg-4.7.6/configs/repositories.toml
+-rw-r--r--   0 dslackw   (1000) users      (100)      273 2023-04-06 16:45:48.000000 slpkg-4.7.6/configs/blacklist.toml
+-rw-r--r--   0 dslackw   (1000) users      (100)     2456 2023-04-06 16:45:48.000000 slpkg-4.7.6/configs/slpkg.toml
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/
+-rw-r--r--   0 dslackw   (1000) users      (100)     2153 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_configs.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      941 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_checks.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2269 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_utilities.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1251 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_sbo_queries.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      272 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_blacklist.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      588 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_colors.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1242 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_upgrade.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2436 2023-04-06 16:45:48.000000 slpkg-4.7.6/tests/test_bin_queries.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1076 2023-04-06 16:45:48.000000 slpkg-4.7.6/LICENSE
+-rwxr-xr-x   0 dslackw   (1000) users      (100)     1773 2023-04-06 16:45:48.000000 slpkg-4.7.6/install.sh
+-rw-r--r--   0 dslackw   (1000) users      (100)    44396 2023-04-06 16:45:48.000000 slpkg-4.7.6/ChangeLog.txt
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/man/
+-rw-r--r--   0 dslackw   (1000) users      (100)     7264 2023-04-06 16:45:48.000000 slpkg-4.7.6/man/slpkg.1
+-rw-r--r--   0 dslackw   (1000) users      (100)     8039 2023-04-06 16:45:48.000000 slpkg-4.7.6/man/slpkg-fr.1
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/completion/
+-rw-r--r--   0 dslackw   (1000) users      (100)      910 2023-04-06 16:45:48.000000 slpkg-4.7.6/completion/slpkg
+-rw-r--r--   0 dslackw   (1000) users      (100)       93 2023-04-06 16:45:48.000000 slpkg-4.7.6/.gitignore
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/binaries/
+-rw-r--r--   0 dslackw   (1000) users      (100)     1850 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/binaries/required.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     6792 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/binaries/queries.py
+-rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/binaries/__init__.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     9818 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/binaries/install.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    62222 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/install_data.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    24339 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/repositories.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2515 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/repo_info.py
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/sbos/
+-rw-r--r--   0 dslackw   (1000) users      (100)     4499 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/sbos/queries.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    14578 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/sbos/slackbuild.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      958 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/sbos/dependencies.py
+-rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/sbos/__init__.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     3983 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/form_configs.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    32105 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/update_repository.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1791 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/progress_bar.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2177 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/downloader.py
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/models/
+-rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/models/__init__.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2630 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/models/models.py
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/
+-rw-r--r--   0 dslackw   (1000) users      (100)     7147 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/view_package.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      629 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/version.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     6318 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/cli_menu.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     5546 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/ascii.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     4004 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/help_commands.py
+-rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/__init__.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     9824 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/views/views.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     3357 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/checks.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1316 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/checksum.py
+-rw-r--r--   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/__init__.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2196 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/dialog_box.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     4931 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/configs.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      874 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/clean_logs.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     7625 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/utilities.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     4072 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/dependees.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    10204 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/check_updates.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     5580 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/remove_packages.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1522 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/blacklist.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     2558 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/download_only.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     3142 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/tracking.py
+-rw-r--r--   0 dslackw   (1000) users      (100)      245 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/logging_config.py
+-rw-r--r--   0 dslackw   (1000) users      (100)    29668 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/main.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1461 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/find_installed.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     3502 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/upgrade.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     3392 2023-04-06 16:45:48.000000 slpkg-4.7.6/slpkg/search.py
+-rw-r--r--   0 dslackw   (1000) users      (100)     1311 2023-04-06 16:45:48.000000 slpkg-4.7.6/setup.cfg
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/
+-rw-r--r--   0 dslackw   (1000) users      (100)        1 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/dependency_links.txt
+-rw-r--r--   0 dslackw   (1000) users      (100)     1106 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/SOURCES.txt
+-rw-r--r--   0 dslackw   (1000) users      (100)        6 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/top_level.txt
+-rw-r--r--   0 dslackw   (1000) users      (100)       53 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/requires.txt
+-rw-r--r--   0 dslackw   (1000) users      (100)     7897 2023-04-06 16:54:00.000000 slpkg-4.7.6/slpkg.egg-info/PKG-INFO
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/tools/
+-rwxr-xr-x   0 dslackw   (1000) users      (100)      787 2023-04-06 16:45:48.000000 slpkg-4.7.6/tools/gen_sbo_txt.sh
+drwxr-xr-x   0 dslackw   (1000) users      (100)        0 2023-04-06 16:45:48.000000 slpkg-4.7.6/bin/
+-rwxr-xr-x   0 dslackw   (1000) users      (100)    11470 2023-04-06 16:45:48.000000 slpkg-4.7.6/bin/slpkg_new-configs
+-rwxr-xr-x   0 dslackw   (1000) users      (100)      184 2023-04-06 16:45:48.000000 slpkg-4.7.6/bin/slpkg
```

### Comparing `slpkg-4.7.5/slackbuild/slack-desc` & `slpkg-4.7.6/slackbuild/slack-desc`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slackbuild/slpkg.SlackBuild` & `slpkg-4.7.6/slackbuild/slpkg.SlackBuild`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/README.rst` & `slpkg-4.7.6/README.rst`

 * *Files 4% similar despite different names*

```diff
@@ -27,16 +27,16 @@
 Install
 -------
 
 Install from the official third-party `SBo repository <https://slackbuilds.org/repository/15.0/system/slpkg/>`_ or directly from source:
 
 .. code-block:: bash
 
-    $ tar xvf slpkg-4.7.4.tar.gz
-    $ cd slpkg-4.7.4
+    $ tar xvf slpkg-4.7.6.tar.gz
+    $ cd slpkg-4.7.6
     $ ./install.sh
 
 Screenshots
 -----------
 
 .. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_install.png
     :target: https://gitlab.com/dslackw/slpkg
@@ -137,14 +137,22 @@
 - `Slackonly <https://packages.slackonly.com/pub/packages/15.0-x86_64/>`_ repository.
 - `Salix OS <https://download.salixos.org/x86_64/slackware-15.0/>`_ repository.
 - `Salix OS extra <https://download.salixos.org/x86_64/slackware-15.0/extra/>`_ repository.
 - `Salix OS patches <https://download.salixos.org/x86_64/slackware-15.0/patches/>`_ repository.
 - `Slackel OS <http://www.slackel.gr/repo/x86_64/current/>`_ repository.
 - `Slint OS <https://slackware.uk/slint/x86_64/slint-15.0/>`_ repository.
 
+
+Multilib packages
+-----------------
+
+Slackware for x86_64 - multilib packages & install instructions:
+
+- Please read the file `README <https://gitlab.com/dslackw/slpkg/-/raw/master/filelists/multilib/README>`_ you will find in the folder `multlib <https://gitlab.com/dslackw/slpkg/-/tree/master/filelists/multilib>`_.
+
 Donate
 ------
 
 If you feel satisfied with this project and want to thanks me make a donation.
 
 .. image:: https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png
    :target: https://www.paypal.me/dslackw
```

### Comparing `slpkg-4.7.5/configs/repositories.toml` & `slpkg-4.7.6/configs/repositories.toml`

 * *Files 12% similar despite different names*

```diff
@@ -38,154 +38,170 @@
   # https://slackware.uk/slackware/slackware64-current/
   SLACK_REPO = false
   SLACK_REPO_NAME = "slack"
   SLACK_REPO_MIRROR = "https://slackware.uk/slackware/slackware64-15.0/"
   SLACK_REPO_PACKAGES = "PACKAGES.TXT"
   SLACK_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLACK_REPO_CHANGELOG = "ChangeLog.txt"
+  SLACK_REPO_TAG = ""
 
   # Official repository for Slackware patches x86_64 15.0 stable.
   # For Slackware patches x86_64 -current:
   # https://slackware.uk/slackware/slackware64-current/extra/
   SLACK_EXTRA_REPO = false
   SLACK_EXTRA_REPO_NAME = "slack_extra"
   SLACK_EXTRA_REPO_MIRROR = "https://slackware.uk/slackware/slackware64-15.0/"
   SLACK_EXTRA_REPO_PACKAGES_MIRROR = "https://slackware.uk/slackware/slackware64-15.0/extra/"
   SLACK_EXTRA_REPO_PACKAGES = "PACKAGES.TXT"
   SLACK_EXTRA_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLACK_EXTRA_REPO_CHANGELOG = "ChangeLog.txt"
+  SLACK_EXTRA_REPO_TAG = ""
 
   # Official repository for Slackware patches x86_64 15.0 stable.
   # For Slackware patches x86_64 -current:
   # https://slackware.uk/slackware/slackware64-current/patches/
   SLACK_PATCHES_REPO = false
   SLACK_PATCHES_REPO_NAME = "slack_patches"
   SLACK_PATCHES_REPO_MIRROR = "https://slackware.uk/slackware/slackware64-15.0/"
   SLACK_PATCHES_REPO_PACKAGES_MIRROR = "https://slackware.uk/slackware/slackware64-15.0/patches/"
   SLACK_PATCHES_REPO_PACKAGES = "PACKAGES.TXT"
   SLACK_PATCHES_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLACK_PATCHES_REPO_CHANGELOG = "ChangeLog.txt"
+  SLACK_PATCHES_REPO_TAG = ""
 
   # AlienBob Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # http://slackware.uk/people/alien/sbrepos/current/x86_64/
   ALIEN_REPO = false
   ALIEN_REPO_NAME = "alien"
   ALIEN_REPO_MIRROR = "https://slackware.nl/people/alien/sbrepos/"
   ALIEN_REPO_PACKAGES_MIRROR = "https://slackware.nl/people/alien/sbrepos/15.0/x86_64/"
   ALIEN_REPO_PACKAGES = "PACKAGES.TXT"
   ALIEN_REPO_CHECKSUMS = "CHECKSUMS.md5"
   ALIEN_REPO_CHANGELOG = "ChangeLog.txt"
+  ALIEN_REPO_TAG = "alien"
 
   # Multilib Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://slackware.nl/people/alien/multilib/current/
   MULTILIB_REPO = false
   MULTILIB_REPO_NAME = "multilib"
   MULTILIB_REPO_MIRROR = "https://slackware.nl/people/alien/multilib/"
   MULTILIB_REPO_PACKAGES_MIRROR = "https://slackware.nl/people/alien/multilib/15.0/"
   MULTILIB_REPO_PACKAGES = "PACKAGES.TXT"
   MULTILIB_REPO_CHECKSUMS = "CHECKSUMS.md5"
   MULTILIB_REPO_CHANGELOG = "ChangeLog.txt"
+  MULTILIB_REPO_TAG = "alien"
 
   # Restricted Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://slackware.nl/people/alien/restricted_sbrepos/current/x86_64/
   RESTRICTED_REPO = false
   RESTRICTED_REPO_NAME = "restricted"
   RESTRICTED_REPO_MIRROR = "https://slackware.nl/people/alien/restricted_sbrepos/"
   RESTRICTED_REPO_PACKAGES_MIRROR = "https://slackware.nl/people/alien/restricted_sbrepos/15.0/x86_64/"
   RESTRICTED_REPO_PACKAGES = "PACKAGES.TXT"
   RESTRICTED_REPO_CHECKSUMS = "CHECKSUMS.md5"
   RESTRICTED_REPO_CHANGELOG = "ChangeLog.txt"
+  RESTRICTED_REPO_TAG = "alien"
 
   # Gnome Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://reddoglinux.ddns.net/linux/gnome/43.x/x86_64/
   GNOME_REPO = false
   GNOME_REPO_NAME = "gnome"
   GNOME_REPO_MIRROR = "https://reddoglinux.ddns.net/linux/gnome/41.x/x86_64/"
   GNOME_REPO_PACKAGES = "PACKAGES.TXT"
   GNOME_REPO_CHECKSUMS = "CHECKSUMS.md5"
   GNOME_REPO_CHANGELOG = "ChangeLog.txt"
+  GNOME_REPO_TAG = "gfs"
 
   # MATE Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://slackware.uk/msb/current/1.26/x86_64/
   MSB_REPO = false
   MSB_REPO_NAME = "msb"
   MSB_REPO_MIRROR = "https://slackware.uk/msb/"
   MSB_REPO_PACKAGES_MIRROR = 'https://slackware.uk/msb/15.0/1.26/x86_64/'
   MSB_REPO_PACKAGES = "PACKAGES.TXT"
   MSB_REPO_CHECKSUMS = "CHECKSUMS.md5"
   MSB_REPO_CHANGELOG = "ChangeLog.txt"
+  MSB_REPO_TAG = "msb"
 
   # Cinnamon Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://slackware.uk/csb/current/x86_64/
   CSB_REPO = false
   CSB_REPO_NAME = "csb"
   CSB_REPO_MIRROR = "https://slackware.uk/csb/"
   CSB_REPO_PACKAGES_MIRROR = 'https://slackware.uk/csb/15.0/x86_64/'
   CSB_REPO_PACKAGES = "PACKAGES.TXT"
   CSB_REPO_CHECKSUMS = "CHECKSUMS.md5"
   CSB_REPO_CHANGELOG = "ChangeLog.txt"
+  CSB_REPO_TAG = "csb"
 
   # Conraid Repository for Slackware x86_64 -current.
   CONRAID_REPO = false
   CONRAID_REPO_NAME = "conraid"
   CONRAID_REPO_MIRROR = "https://slack.conraid.net/repository/slackware64-current/"
   CONRAID_REPO_PACKAGES = "PACKAGES.TXT"
   CONRAID_REPO_CHECKSUMS = "CHECKSUMS.md5"
   CONRAID_REPO_CHANGELOG = "ChangeLog.txt"
+  CONRAID_REPO_TAG = "cf"
 
   # Slackonly Repository for Slackware x86_64 15.0 stable.
   # For Slackware x86_64 -current:
   # https://packages.slackonly.com/pub/packages/current-x86_64/
   SLACKONLY_REPO = false
   SLACKONLY_REPO_NAME = "slackonly"
   SLACKONLY_REPO_MIRROR = "https://packages.slackonly.com/pub/packages/15.0-x86_64/"
   SLACKONLY_REPO_PACKAGES = "PACKAGES.TXT"
   SLACKONLY_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLACKONLY_REPO_CHANGELOG = "ChangeLog.txt"
+  SLACKONLY_REPO_TAG = "slonly"
 
   # Repository for Salix OS x86_64 15.0 stable.
   SALIXOS_REPO = false
   SALIXOS_REPO_NAME = "salixos"
   SALIXOS_REPO_MIRROR = "https://download.salixos.org/x86_64/slackware-15.0/"
   SALIXOS_REPO_PACKAGES = "PACKAGES.TXT"
   SALIXOS_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SALIXOS_REPO_CHANGELOG = "ChangeLog.txt"
+  SALIXOS_REPO_TAG = ""
 
   # Repository for Salix OS x86_64 15.0 stable.
   SALIXOS_EXTRA_REPO = false
   SALIXOS_EXTRA_REPO_NAME = "salixos_extra"
   SALIXOS_EXTRA_REPO_MIRROR = "https://download.salixos.org/x86_64/slackware-15.0/"
   SALIXOS_EXTRA_REPO_PACKAGES_MIRROR = 'https://download.salixos.org/x86_64/slackware-15.0/extra/'
   SALIXOS_EXTRA_REPO_PACKAGES = "PACKAGES.TXT"
   SALIXOS_EXTRA_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SALIXOS_EXTRA_REPO_CHANGELOG = "ChangeLog.txt"
+  SALIXOS_EXTRA_REPO_TAG = ""
 
   # Repository for Salix OS x86_64 15.0 stable.
   SALIXOS_PATCHES_REPO = false
   SALIXOS_PATCHES_REPO_NAME = "salixos_patches"
   SALIXOS_PATCHES_REPO_MIRROR = "https://download.salixos.org/x86_64/slackware-15.0/"
   SALIXOS_PATCHES_REPO_PACKAGES_MIRROR = 'https://download.salixos.org/x86_64/slackware-15.0/patches/'
   SALIXOS_PATCHES_REPO_PACKAGES = "PACKAGES.TXT"
   SALIXOS_PATCHES_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SALIXOS_PATCHES_REPO_CHANGELOG = "ChangeLog.txt"
+  SALIXOS_PATCHES_REPO_TAG = "_slack15.0"
 
   # Repository for Slackel OS x86_64 -current.
   SLACKEL_REPO = false
   SLACKEL_REPO_NAME = "slackel"
   SLACKEL_REPO_MIRROR = "http://www.slackel.gr/repo/x86_64/current/"
   SLACKEL_REPO_PACKAGES = "PACKAGES.TXT"
   SLACKEL_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLACKEL_REPO_CHANGELOG = "ChangeLog.txt"
+  SLACKEL_REPO_TAG = "dj"
 
   # Slint Repository for Slackware x86_64 15.0 stable.
   SLINT_REPO = false
   SLINT_REPO_NAME = "slint"
   SLINT_REPO_MIRROR = "https://slackware.uk/slint/x86_64/slint-15.0/"
   SLINT_REPO_PACKAGES = "PACKAGES.TXT"
   SLINT_REPO_CHECKSUMS = "CHECKSUMS.md5"
   SLINT_REPO_CHANGELOG = "ChangeLog.txt"
+  SLINT_REPO_TAG = "slint"
```

### Comparing `slpkg-4.7.5/configs/slpkg.toml` & `slpkg-4.7.6/configs/slpkg.toml`

 * *Files 2% similar despite different names*

```diff
@@ -39,15 +39,15 @@
   INSTALLPKG = "upgradepkg --install-new"
   # Slackware command to reinstall packages.
   REINSTALL = "upgradepkg --reinstall"
   # Slackware command to remove packages.
   REMOVEPKG = "removepkg"
 
   # You can choose a downloader among wget, curl and lftp.
-  # Default is wget. [wget/curl/lftp]
+  # Default is wget. [wget/wget2/curl/lftp]
   DOWNLOADER = "wget"
   # Wget downloader options.
   # -c, --continue: resume getting a partially-downloaded file.
   # -q, Turn off Wget's output.
   # --show-progress, Force wget to display the progress bar in any verbosity.
   WGET_OPTIONS = "-c -q --progress=bar:force:noscroll --show-progress"
   # Curl downloader options.
```

### Comparing `slpkg-4.7.5/tests/test_configs.py` & `slpkg-4.7.6/tests/test_configs.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/tests/test_checks.py` & `slpkg-4.7.6/tests/test_checks.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/tests/test_utilities.py` & `slpkg-4.7.6/tests/test_utilities.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 import unittest
 
+from pathlib import Path
 from slpkg.configs import Configs
 from slpkg.utilities import Utilities
 
 
 class TestUtilities(unittest.TestCase):
 
     def setUp(self):
@@ -47,15 +48,15 @@
         self.assertEqual('1', self.utils.read_sbo_build_tag('slpkg'))
 
     def test_is_option(self):
         self.assertTrue(True, self.utils.is_option(['-P', '--parallel'],
                                                    ['-k', '-p', '-P', '--parallel', '--bin-repo']))
 
     def test_get_file_size(self):
-        self.assertEqual('2154 KB', self.utils.get_file_size(f'/var/log/packages/{self.package}'))
+        self.assertEqual('2154 KB', self.utils.get_file_size(Path('/var/log/packages/', self.package)))
 
     def test_apply_package_pattern(self):
         self.assertGreater(len(self.utils.apply_package_pattern([], ['*'], '')), 1)
 
 
 if __name__ == '__main__':
     unittest.main()
```

### Comparing `slpkg-4.7.5/tests/test_sbo_queries.py` & `slpkg-4.7.6/tests/test_sbo_queries.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/tests/test_colors.py` & `slpkg-4.7.6/tests/test_colors.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/tests/test_upgrade.py` & `slpkg-4.7.6/tests/test_upgrade.py`

 * *Files 26% similar despite different names*

```diff
@@ -4,20 +4,35 @@
 from slpkg.upgrade import Upgrade
 
 
 class TestUtilities(unittest.TestCase):
 
     def setUp(self):
         self.utils = Utilities()
-        self.packages: list = ['git', 'wget', 'vim', 'pycharm', 'libreoffice', 'ptpython', 'ranger', 'colored']
+        self.packages: list = ['wget', 'vim', 'pycharm', 'libreoffice', 'ptpython', 'ranger', 'colored']
 
     def test_installed_is_upgradable_for_binaries(self):
         for pkg in self.packages:
             self.assertFalse(False, Upgrade(['-B', '--bin-repo='], 'slack_patches').is_package_upgradeable(pkg))
 
     def test_installed_is_upgradable_for_slackbuilds(self):
         for pkg in self.packages:
             self.assertFalse(False, Upgrade([]).is_package_upgradeable(pkg))
 
+    def test_for_sbo_repository(self):
+        upgrade = Upgrade([])
+        packages: list = list(upgrade.packages())
+        self.assertGreater(len(packages), 1)
+
+    def test_for_alien_repository(self):
+        upgrade = Upgrade(['-B'], 'alien')
+        packages: list = list(upgrade.packages())
+        self.assertGreater(len(packages), 1)
+
+    def test_for_slack_repository(self):
+        upgrade = Upgrade(['-B'], 'slack')
+        packages: list = list(upgrade.packages())
+        self.assertGreater(len(packages), 1)
+
 
 if __name__ == '__main__':
     unittest.main()
```

### Comparing `slpkg-4.7.5/tests/test_bin_queries.py` & `slpkg-4.7.6/tests/test_bin_queries.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/LICENSE` & `slpkg-4.7.6/LICENSE`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/install.sh` & `slpkg-4.7.6/install.sh`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/ChangeLog.txt` & `slpkg-4.7.6/ChangeLog.txt`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,19 @@
+4.7.6 - 04/04/2023
+Fixed:
+- Upgrade packages with build numbers greater to >= 10
+Updated:
+- Indicate colour for upgradable packages
+- Upgrade packages by repository
+Added:
+- Packages list for multilib installation
+- To detect the dependencies before removing a package (Thanks to marav)
+- The flag -y, --yes to the remove command
+- To support wget2 downloader
+
 4.7.5 - 04/04/2023
 BugFixed:
 - Upgrade packages from repositories
 
 4.7.4 - 04/04/2023
 Fixed:
 - Python typing hints
```

### Comparing `slpkg-4.7.5/man/slpkg.1` & `slpkg-4.7.6/man/slpkg.1`

 * *Files 0% similar despite different names*

```diff
@@ -110,15 +110,15 @@
 Tracking the packages dependencies.
 .RE
 .SH OPTIONS
 .P
 .B -y, --yes
 .RS
 Answer Yes to all questions. (to be used with: -u, update, -U, upgrade, -L, clean-logs, -b, build,
--i, install, -d, download,) (Not used with -R, remove, option removed for security reasons)
+-i, install, -R, remove, -d, download,) (Not used with -R, remove, option removed for security reasons)
 .RE
 .P
 .B -j, --jobs
 .RS
 Acceleration of SlackBuild scripts. When the \fB--jobs\fR flag is set, slpkg automatically detects the number
 of processors and enters it into the MAKEFLAGS variable. Some SlackBuilds fail when MAKEFLAGS is declared or
 the number of processors (-j) is greater than one. (to be used with: -U, upgrade, -b, build, -i, install)
```

### Comparing `slpkg-4.7.5/man/slpkg-fr.1` & `slpkg-4.7.6/man/slpkg-fr.1`

 * *Files 1% similar despite different names*

```diff
@@ -108,15 +108,15 @@
 Suivre les dépendances des paquets.
 .RE
 .SH OPTIONS
 .P
 .B -y, --yes
 .RS
 Répondre \fBOui\fP à toutes les questions. (à utiliser avec: \fB-u, update, -U, upgrade, -L, clean-logs, -b, build,
--i, install, -d, download\fP) (Non utilisée avec \fB-R, remove\fP, option supprimée pour des raisons de sécurité)
+-i, install, -R, remove, -d, download\fP) (Non utilisée avec \fB-R, remove\fP, option supprimée pour des raisons de sécurité)
 .RE
 .P
 .B -j, --jobs
 .RS
 Accélération des scripts SlackBuild. Lorsque l'indicateur \fB--jobs\fP est activé, slpkg détecte automatiquement le nombre de
 de processeurs et le saisit dans la variable \fBMAKEFLAGS\fP. Certains SlackBuilds échouent lorsque \fBMAKEFLAGS\fP est déclaré ou que
 le nombre de processeurs (-j) est supérieur à 1. (à utiliser avec: \fB-U, upgrade, build, -i, install\fP)
```

### Comparing `slpkg-4.7.5/completion/slpkg` & `slpkg-4.7.6/completion/slpkg`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/binaries/required.py` & `slpkg-4.7.6/slpkg/binaries/required.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/binaries/queries.py` & `slpkg-4.7.6/slpkg/binaries/queries.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,24 +1,22 @@
 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
 from typing import Union, Generator
 
-from slpkg.configs import Configs
 from slpkg.blacklist import Blacklist
 from slpkg.repositories import Repositories
 from slpkg.models.models import BinariesTable
 from slpkg.models.models import session as Session
 
 
-class BinQueries(Configs):
-    """ Queries class for the sbo repository. """
+class BinQueries:
+    """ Queries class for the binary repositories. """
 
     def __init__(self, name: str, repo: str):
-        super(Configs, self).__init__()
         self.name: str = name
         self.repo: str = repo
         self.session = Session
         self.repos = Repositories()
 
         self.black = Blacklist()
         if self.name in self.black.packages():
```

### Comparing `slpkg-4.7.5/slpkg/binaries/install.py` & `slpkg-4.7.6/slpkg/binaries/install.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/install_data.py` & `slpkg-4.7.6/slpkg/install_data.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/repositories.py` & `slpkg-4.7.6/slpkg/repositories.py`

 * *Files 18% similar despite different names*

```diff
@@ -48,143 +48,159 @@
     slack_repo: bool = False
     slack_repo_name: str = 'slack'
     slack_repo_path: Path = Path(config.lib_path, 'repositories', slack_repo_name)
     slack_repo_mirror: str = 'https://slackware.uk/slackware/slackware64-15.0/'
     slack_repo_packages: str = 'PACKAGES.TXT'
     slack_repo_checksums: str = 'CHECKSUMS.md5'
     slack_repo_changelog: str = 'ChangeLog.txt'
+    slack_repo_tag: str = ''
 
     slack_extra_repo: bool = False
     slack_extra_repo_name: str = 'slack_extra'
     slack_extra_repo_path: Path = Path(config.lib_path, 'repositories', slack_extra_repo_name)
     slack_extra_repo_mirror: str = 'https://slackware.uk/slackware/slackware64-15.0/'
     slack_extra_packages_mirror: str = 'https://slackware.uk/slackware/slackware64-15.0/extra/'
     slack_extra_repo_packages: str = 'PACKAGES.TXT'
     slack_extra_repo_checksums: str = 'CHECKSUMS.md5'
     slack_extra_repo_changelog: str = 'ChangeLog.txt'
+    slack_extra_repo_tag: str = ''
 
     slack_patches_repo: bool = False
     slack_patches_repo_name: str = 'slack_patches'
     slack_patches_repo_path: Path = Path(config.lib_path, 'repositories', slack_patches_repo_name)
     slack_patches_repo_mirror: str = 'https://slackware.uk/slackware/slackware64-15.0/'
     slack_patches_packages_mirror: str = 'https://slackware.uk/slackware/slackware64-15.0/patches/'
     slack_patches_repo_packages: str = 'PACKAGES.TXT'
     slack_patches_repo_checksums: str = 'CHECKSUMS.md5'
     slack_patches_repo_changelog: str = 'ChangeLog.txt'
+    slack_patches_repo_tag: str = '_slack15.0'
 
     alien_repo: bool = False
     alien_repo_name: str = 'alien'
     alien_repo_path: Path = Path(config.lib_path, 'repositories', alien_repo_name)
     alien_repo_mirror: str = 'https://slackware.nl/people/alien/sbrepos/'
     alien_repo_packages_mirror: str = 'https://slackware.nl/people/alien/sbrepos/15.0/x86_64/'
     alien_repo_packages: str = 'PACKAGES.TXT'
     alien_repo_checksums: str = 'CHECKSUMS.md5'
     alien_repo_changelog: str = 'ChangeLog.txt'
+    alien_repo_tag: str = 'alien'
 
     multilib_repo: bool = False
     multilib_repo_name: str = 'multilib'
     multilib_repo_path: Path = Path(config.lib_path, 'repositories', multilib_repo_name)
     multilib_repo_mirror: str = 'https://slackware.nl/people/alien/multilib/'
     multilib_repo_packages_mirror: str = 'https://slackware.nl/people/alien/multilib/15.0/'
     multilib_repo_packages: str = 'PACKAGES.TXT'
     multilib_repo_checksums: str = 'CHECKSUMS.md5'
     multilib_repo_changelog: str = 'ChangeLog.txt'
+    multilib_repo_tag: str = 'alien'
 
     restricted_repo: bool = False
     restricted_repo_name: str = 'restricted'
     restricted_repo_path: Path = Path(config.lib_path, 'repositories', restricted_repo_name)
     restricted_repo_mirror: str = 'https://slackware.nl/people/alien/restricted_sbrepos/'
     restricted_repo_packages_mirror: str = 'https://slackware.nl/people/alien/restricted_sbrepos/15.0/x86_64/'
     restricted_repo_packages: str = 'PACKAGES.TXT'
     restricted_repo_checksums: str = 'CHECKSUMS.md5'
     restricted_repo_changelog: str = 'ChangeLog.txt'
+    restricted_repo_tag: str = 'alien'
 
     gnome_repo: bool = False
     gnome_repo_name: str = 'gnome'
     gnome_repo_path: Path = Path(config.lib_path, 'repositories', gnome_repo_name)
     gnome_repo_mirror: str = 'https://reddoglinux.ddns.net/linux/gnome/43.x/x86_64/'
     gnome_repo_packages: str = 'PACKAGES.TXT'
     gnome_repo_checksums: str = 'CHECKSUMS.md5'
     gnome_repo_changelog: str = 'ChangeLog.txt'
+    gnome_repo_tag: str = 'gfs'
 
     msb_repo: bool = False
     msb_repo_name: str = 'msb'
     msb_repo_path: Path = Path(config.lib_path, 'repositories', msb_repo_name)
     msb_repo_mirror: str = 'https://slackware.uk/msb/'
     msb_repo_packages_mirror: str = 'https://slackware.uk/msb/15.0/1.26/x86_64/'
     msb_repo_packages: str = 'PACKAGES.TXT'
     msb_repo_checksums: str = 'CHECKSUMS.md5'
     msb_repo_changelog: str = 'ChangeLog.txt'
+    msb_repo_tag: str = 'msb'
 
     csb_repo: bool = False
     csb_repo_name: str = 'csb'
     csb_repo_path: Path = Path(config.lib_path, 'repositories', csb_repo_name)
     csb_repo_mirror: str = 'https://slackware.uk/csb/'
     csb_repo_packages_mirror: str = 'https://slackware.uk/csb/15.0/x86_64/'
     csb_repo_packages: str = 'PACKAGES.TXT'
     csb_repo_checksums: str = 'CHECKSUMS.md5'
     csb_repo_changelog: str = 'ChangeLog.txt'
+    csb_repo_tag: str = 'csb'
 
     conraid_repo: bool = False
     conraid_repo_name: str = 'conraid'
     conraid_repo_path: Path = Path(config.lib_path, 'repositories', conraid_repo_name)
-    conraid_repo_mirror: str = 'https://reddoglinux.ddns.net/linux/conraid_43.x/x86_64/'
+    conraid_repo_mirror: str = 'https://slack.conraid.net/repository/slackware64-current/'
     conraid_repo_packages: str = 'PACKAGES.TXT'
     conraid_repo_checksums: str = 'CHECKSUMS.md5'
     conraid_repo_changelog: str = 'ChangeLog.txt'
+    conraid_repo_tag: str = 'cf'
 
     slackonly_repo: bool = False
     slackonly_repo_name: str = 'slackonly'
     slackonly_repo_path: Path = Path(config.lib_path, 'repositories', slackonly_repo_name)
     slackonly_repo_mirror: str = 'https://packages.slackonly.com/pub/packages/15.0-x86_64/'
     slackonly_repo_packages: str = 'PACKAGES.TXT'
     slackonly_repo_checksums: str = 'CHECKSUMS.md5'
     slackonly_repo_changelog: str = 'ChangeLog.txt'
+    slackonly_repo_tag: str = 'slonly'
 
     salixos_repo: bool = False
     salixos_repo_name: str = 'salixos'
     salixos_repo_path: Path = Path(config.lib_path, 'repositories', salixos_repo_name)
     salixos_repo_mirror: str = 'https://download.salixos.org/x86_64/slackware-15.0/'
     salixos_repo_packages: str = 'PACKAGES.TXT'
     salixos_repo_checksums: str = 'CHECKSUMS.md5'
     salixos_repo_changelog: str = 'ChangeLog.txt'
+    salixos_repo_tag: str = ''
 
     salixos_extra_repo: bool = False
     salixos_extra_repo_name: str = 'salixos_extra'
     salixos_extra_repo_path: Path = Path(config.lib_path, 'repositories', salixos_extra_repo_name)
     salixos_extra_repo_mirror: str = 'https://download.salixos.org/x86_64/slackware-15.0/'
     salixos_extra_repo_packages_mirror: str = 'https://download.salixos.org/x86_64/slackware-15.0/extra/'
     salixos_extra_repo_packages: str = 'PACKAGES.TXT'
     salixos_extra_repo_checksums: str = 'CHECKSUMS.md5'
     salixos_extra_repo_changelog: str = 'ChangeLog.txt'
+    salixos_extra_repo_tag: str = ''
 
     salixos_patches_repo: bool = False
     salixos_patches_repo_name: str = 'salixos_patches'
     salixos_patches_repo_path: Path = Path(config.lib_path, 'repositories', salixos_patches_repo_name)
     salixos_patches_repo_mirror: str = 'https://download.salixos.org/x86_64/slackware-15.0/'
     salixos_patches_repo_packages_mirror: str = 'https://download.salixos.org/x86_64/slackware-15.0/patches/'
     salixos_patches_repo_packages: str = 'PACKAGES.TXT'
     salixos_patches_repo_checksums: str = 'CHECKSUMS.md5'
     salixos_patches_repo_changelog: str = 'ChangeLog.txt'
+    salixos_patches_repo_tag: str = '_slack15.0'
 
     slackel_repo: bool = False
     slackel_repo_name: str = 'slackel'
     slackel_repo_path: Path = Path(config.lib_path, 'repositories', slackel_repo_name)
     slackel_repo_mirror: str = 'http://www.slackel.gr/repo/x86_64/current/'
     slackel_repo_packages: str = 'PACKAGES.TXT'
     slackel_repo_checksums: str = 'CHECKSUMS.md5'
     slackel_repo_changelog: str = 'ChangeLog.txt'
+    slackel_repo_tag: str = 'dj'
 
     slint_repo: bool = False
     slint_repo_name: str = 'slint'
     slint_repo_path: Path = Path(config.lib_path, 'repositories', slint_repo_name)
     slint_repo_mirror: str = 'https://slackware.uk/slint/x86_64/slint-15.0/'
     slint_repo_packages: str = 'PACKAGES.TXT'
     slint_repo_checksums: str = 'CHECKSUMS.md5'
     slint_repo_changelog: str = 'ChangeLog.txt'
+    slint_repo_tag: str = 'slint'
 
     try:
         if repositories_file_toml.is_file():
             with open(repositories_file_toml, 'rb') as repo:
                 repos_config = tomli.load(repo)['REPOSITORIES']
 
             sbo_repo_name: str = repos_config['SBO_REPO_NAME']
@@ -205,128 +221,144 @@
 
             slack_repo: bool = repos_config['SLACK_REPO']
             slack_repo_name: str = repos_config['SLACK_REPO_NAME']
             slack_repo_mirror: str = repos_config['SLACK_REPO_MIRROR']
             slack_repo_packages: str = repos_config['SLACK_REPO_PACKAGES']
             slack_repo_checksums: str = repos_config['SLACK_REPO_CHECKSUMS']
             slack_repo_changelog: str = repos_config['SLACK_REPO_CHANGELOG']
+            slack_repo_tag: str = repos_config['SLACK_REPO_TAG']
 
             slack_extra_repo: bool = repos_config['SLACK_EXTRA_REPO']
             slack_extra_repo_name: str = repos_config['SLACK_EXTRA_REPO_NAME']
             slack_extra_repo_mirror: str = repos_config['SLACK_EXTRA_REPO_MIRROR']
             slack_extra_repo_packages_mirror: str = repos_config['SLACK_EXTRA_REPO_PACKAGES_MIRROR']
             slack_extra_repo_packages: str = repos_config['SLACK_EXTRA_REPO_PACKAGES']
             slack_extra_repo_checksums: str = repos_config['SLACK_EXTRA_REPO_CHECKSUMS']
             slack_extra_repo_changelog: str = repos_config['SLACK_EXTRA_REPO_CHANGELOG']
+            slack_extra_repo_tag: str = repos_config['SLACK_EXTRA_REPO_TAG']
 
             slack_patches_repo: bool = repos_config['SLACK_PATCHES_REPO']
             slack_patches_repo_name: str = repos_config['SLACK_PATCHES_REPO_NAME']
             slack_patches_repo_mirror: str = repos_config['SLACK_PATCHES_REPO_MIRROR']
             slack_patches_repo_packages_mirror: str = repos_config['SLACK_PATCHES_REPO_PACKAGES_MIRROR']
             slack_patches_repo_packages: str = repos_config['SLACK_PATCHES_REPO_PACKAGES']
             slack_patches_repo_checksums: str = repos_config['SLACK_PATCHES_REPO_CHECKSUMS']
             slack_patches_repo_changelog: str = repos_config['SLACK_PATCHES_REPO_CHANGELOG']
+            slack_patches_repo_tag: str = repos_config['SLACK_PATCHES_REPO_TAG']
 
             alien_repo: bool = repos_config['ALIEN_REPO']
             alien_repo_name: str = repos_config['ALIEN_REPO_NAME']
             alien_repo_mirror: str = repos_config['ALIEN_REPO_MIRROR']
             alien_repo_packages_mirror: str = repos_config['ALIEN_REPO_PACKAGES_MIRROR']
             alien_repo_packages: str = repos_config['ALIEN_REPO_PACKAGES']
             alien_repo_checksums: str = repos_config['ALIEN_REPO_CHECKSUMS']
             alien_repo_changelog: str = repos_config['ALIEN_REPO_CHANGELOG']
+            alien_repo_tag: str = repos_config['ALIEN_REPO_TAG']
 
             multilib_repo: bool = repos_config['MULTILIB_REPO']
             multilib_repo_name: str = repos_config['MULTILIB_REPO_NAME']
             multilib_repo_mirror: str = repos_config['MULTILIB_REPO_MIRROR']
             multilib_repo_packages_mirror: str = repos_config['MULTILIB_REPO_PACKAGES_MIRROR']
             multilib_repo_packages: str = repos_config['MULTILIB_REPO_PACKAGES']
             multilib_repo_checksums: str = repos_config['MULTILIB_REPO_CHECKSUMS']
             multilib_repo_changelog: str = repos_config['MULTILIB_REPO_CHANGELOG']
+            multilib_repo_tag: str = repos_config['MULTILIB_REPO_TAG']
 
             restricted_repo: bool = repos_config['RESTRICTED_REPO']
             restricted_repo_name: str = repos_config['RESTRICTED_REPO_NAME']
             restricted_repo_mirror: str = repos_config['RESTRICTED_REPO_MIRROR']
             restricted_repo_packages_mirror: str = repos_config['RESTRICTED_REPO_PACKAGES_MIRROR']
             restricted_repo_packages: str = repos_config['RESTRICTED_REPO_PACKAGES']
             restricted_repo_checksums: str = repos_config['RESTRICTED_REPO_CHECKSUMS']
             restricted_repo_changelog: str = repos_config['RESTRICTED_REPO_CHANGELOG']
+            restricted_repo_tag: str = repos_config['RESTRICTED_REPO_TAG']
 
             gnome_repo: bool = repos_config['GNOME_REPO']
             gnome_repo_name: str = repos_config['GNOME_REPO_NAME']
             gnome_repo_mirror: str = repos_config['GNOME_REPO_MIRROR']
             gnome_repo_packages: str = repos_config['GNOME_REPO_PACKAGES']
             gnome_repo_checksums: str = repos_config['GNOME_REPO_CHECKSUMS']
             gnome_repo_changelog: str = repos_config['GNOME_REPO_CHANGELOG']
+            gnome_repo_tag: str = repos_config['GNOME_REPO_TAG']
 
             msb_repo: bool = repos_config['MSB_REPO']
             msb_repo_name: str = repos_config['MSB_REPO_NAME']
             msb_repo_mirror: str = repos_config['MSB_REPO_MIRROR']
             msb_repo_packages_mirror: str = repos_config['MSB_REPO_PACKAGES_MIRROR']
             msb_repo_packages: str = repos_config['MSB_REPO_PACKAGES']
             msb_repo_checksums: str = repos_config['MSB_REPO_CHECKSUMS']
             msb_repo_changelog: str = repos_config['MSB_REPO_CHANGELOG']
+            msb_repo_tag: str = repos_config['MSB_REPO_TAG']
 
             csb_repo: bool = repos_config['CSB_REPO']
             csb_repo_name: str = repos_config['CSB_REPO_NAME']
             csb_repo_mirror: str = repos_config['CSB_REPO_MIRROR']
             csb_repo_packages_mirror: str = repos_config['CSB_REPO_PACKAGES_MIRROR']
             csb_repo_packages: str = repos_config['CSB_REPO_PACKAGES']
             csb_repo_checksums: str = repos_config['CSB_REPO_CHECKSUMS']
             csb_repo_changelog: str = repos_config['CSB_REPO_CHANGELOG']
+            csb_repo_tag: str = repos_config['CSB_REPO_TAG']
 
             conraid_repo: bool = repos_config['CONRAID_REPO']
             conraid_repo_name: str = repos_config['CONRAID_REPO_NAME']
             conraid_repo_mirror: str = repos_config['CONRAID_REPO_MIRROR']
             conraid_repo_packages: str = repos_config['CONRAID_REPO_PACKAGES']
             conraid_repo_checksums: str = repos_config['CONRAID_REPO_CHECKSUMS']
             conraid_repo_changelog: str = repos_config['CONRAID_REPO_CHANGELOG']
+            conraid_repo_tag: str = repos_config['CONRAID_REPO_TAG']
 
             slackonly_repo: bool = repos_config['SLACKONLY_REPO']
             slackonly_repo_name: str = repos_config['SLACKONLY_REPO_NAME']
             slackonly_repo_mirror: str = repos_config['SLACKONLY_REPO_MIRROR']
             slackonly_repo_packages: str = repos_config['SLACKONLY_REPO_PACKAGES']
             slackonly_repo_checksums: str = repos_config['SLACKONLY_REPO_CHECKSUMS']
             slackonly_repo_changelog: str = repos_config['SLACKONLY_REPO_CHANGELOG']
+            slackonly_repo_tag: str = repos_config['SLACKONLY_REPO_TAG']
 
             salixos_repo: bool = repos_config['SALIXOS_REPO']
             salixos_repo_name: str = repos_config['SALIXOS_REPO_NAME']
             salixos_repo_mirror: str = repos_config['SALIXOS_REPO_MIRROR']
             salixos_repo_packages: str = repos_config['SALIXOS_REPO_PACKAGES']
             salixos_repo_checksums: str = repos_config['SALIXOS_REPO_CHECKSUMS']
             salixos_repo_changelog: str = repos_config['SALIXOS_REPO_CHANGELOG']
+            salixos_repo_tag: str = repos_config['SALIXOS_REPO_TAG']
 
             salixos_extra_repo: bool = repos_config['SALIXOS_EXTRA_REPO']
             salixos_extra_repo_name: str = repos_config['SALIXOS_EXTRA_REPO_NAME']
             salixos_extra_repo_mirror: str = repos_config['SALIXOS_EXTRA_REPO_MIRROR']
             salixos_extra_repo_packages_mirror: str = repos_config['SALIXOS_EXTRA_REPO_PACKAGES_MIRROR']
             salixos_extra_repo_packages: str = repos_config['SALIXOS_EXTRA_REPO_PACKAGES']
             salixos_extra_repo_checksums: str = repos_config['SALIXOS_EXTRA_REPO_CHECKSUMS']
             salixos_extra_repo_changelog: str = repos_config['SALIXOS_EXTRA_REPO_CHANGELOG']
+            salixos_extra_repo_tag: str = repos_config['SALIXOS_EXTRA_REPO_TAG']
 
             salixos_patches_repo: bool = repos_config['SALIXOS_PATCHES_REPO']
             salixos_patches_repo_name: str = repos_config['SALIXOS_PATCHES_REPO_NAME']
             salixos_patches_repo_mirror: str = repos_config['SALIXOS_PATCHES_REPO_MIRROR']
             salixos_patches_repo_packages_mirror: str = repos_config['SALIXOS_PATCHES_REPO_PACKAGES_MIRROR']
             salixos_patches_repo_packages: str = repos_config['SALIXOS_PATCHES_REPO_PACKAGES']
             salixos_patches_repo_checksums: str = repos_config['SALIXOS_PATCHES_REPO_CHECKSUMS']
             salixos_patches_repo_changelog: str = repos_config['SALIXOS_PATCHES_REPO_CHANGELOG']
+            salixos_patches_repo_tag: str = repos_config['SALIXOS_PATCHES_REPO_TAG']
 
             slackel_repo: bool = repos_config['SLACKEL_REPO']
             slackel_repo_name: str = repos_config['SLACKEL_REPO_NAME']
             slackel_repo_mirror: str = repos_config['SLACKEL_REPO_MIRROR']
             slackel_repo_packages: str = repos_config['SLACKEL_REPO_PACKAGES']
             slackel_repo_checksums: str = repos_config['SLACKEL_REPO_CHECKSUMS']
             slackel_repo_changelog: str = repos_config['SLACKEL_REPO_CHANGELOG']
+            slackel_repo_tag: str = repos_config['SLACKEL_REPO_TAG']
 
             slint_repo: bool = repos_config['SLINT_REPO']
             slint_repo_name: str = repos_config['SLINT_REPO_NAME']
             slint_repo_mirror: str = repos_config['SLINT_REPO_MIRROR']
             slint_repo_packages: str = repos_config['SLINT_REPO_PACKAGES']
             slint_repo_checksums: str = repos_config['SLINT_REPO_CHECKSUMS']
             slint_repo_changelog: str = repos_config['SLINT_REPO_CHANGELOG']
+            slint_repo_tag: str = repos_config['SLINT_REPO_TAG']
 
     except (tomli.TOMLDecodeError, KeyError) as error:
         raise SystemExit(f'\n{config.prog_name} {bred}Error{endc}: {error}: in the configuration file '
                          f"'{repositories_file_toml}'.\n"
                          f"\nIf you have upgraded the '{config.prog_name}' probably you need to run:\n"
                          f"'mv {repositories_file_toml}.new {repositories_file_toml}'.\n"
                          f"or '{cyan}slpkg_new-configs{endc}' command.\n")
@@ -339,33 +371,103 @@
         sbo_enabled_repository: str = ponce_repo_name
         repo_tag: str = ponce_repo_tag
         patch_repo_tag: str = ponce_repo_patch_tag
         sbo_enabled_repo: bool = False
 
     # List of repositories.
     repositories = {
-        sbo_repo_name: [sbo_enabled_repo, sbo_repo_path, sbo_repo_changelog],
-        ponce_repo_name: [ponce_repo, ponce_repo_path, ponce_repo_changelog],
-        slack_repo_name: [slack_repo, slack_repo_path, slack_repo_changelog],
-        slack_extra_repo_name: [slack_extra_repo, slack_extra_repo_path, slack_extra_repo_changelog],
-        slack_patches_repo_name: [slack_patches_repo, slack_patches_repo_path, slack_patches_repo_changelog],
-        alien_repo_name: [alien_repo, alien_repo_path, alien_repo_changelog],
-        multilib_repo_name: [multilib_repo, multilib_repo_path, multilib_repo_changelog],
-        restricted_repo_name: [restricted_repo, restricted_repo_path, restricted_repo_changelog],
-        gnome_repo_name: [gnome_repo, gnome_repo_path, gnome_repo_changelog],
-        msb_repo_name: [msb_repo, msb_repo_path, msb_repo_changelog],
-        csb_repo_name: [csb_repo, csb_repo_path, csb_repo_changelog],
-        conraid_repo_name: [conraid_repo, conraid_repo_path, conraid_repo_changelog],
-        slackonly_repo_name: [slackonly_repo, slackonly_repo_path, slackonly_repo_changelog],
-        salixos_repo_name: [salixos_repo, salixos_repo_path, salixos_repo_changelog],
-        salixos_extra_repo_name: [salixos_extra_repo, salixos_extra_repo_path, salixos_extra_repo_changelog],
-        salixos_patches_repo_name: [salixos_patches_repo, salixos_patches_repo_path,
-                                    salixos_patches_repo_changelog],
-        slackel_repo_name: [slackel_repo, slackel_repo_path, slackel_repo_changelog],
-        slint_repo_name: [slint_repo, slint_repo_path, slint_repo_changelog]
+        sbo_repo_name: [sbo_enabled_repo,
+                        sbo_repo_path,
+                        sbo_repo_changelog,
+                        sbo_repo_tag],
+
+        ponce_repo_name: [ponce_repo,
+                          ponce_repo_path,
+                          ponce_repo_changelog,
+                          ponce_repo_tag],
+
+        slack_repo_name: [slack_repo,
+                          slack_repo_path,
+                          slack_repo_changelog,
+                          slack_repo_tag],
+
+        slack_extra_repo_name: [slack_extra_repo,
+                                slack_extra_repo_path,
+                                slack_extra_repo_changelog,
+                                slack_extra_repo_tag],
+
+        slack_patches_repo_name: [slack_patches_repo,
+                                  slack_patches_repo_path,
+                                  slack_patches_repo_changelog,
+                                  slack_patches_repo_tag],
+
+        alien_repo_name: [alien_repo,
+                          alien_repo_path,
+                          alien_repo_changelog,
+                          alien_repo_tag],
+
+        multilib_repo_name: [multilib_repo,
+                             multilib_repo_path,
+                             multilib_repo_changelog,
+                             multilib_repo_tag],
+
+        restricted_repo_name: [restricted_repo,
+                               restricted_repo_path,
+                               restricted_repo_changelog,
+                               restricted_repo_tag],
+
+        gnome_repo_name: [gnome_repo,
+                          gnome_repo_path,
+                          gnome_repo_changelog,
+                          gnome_repo_tag],
+
+        msb_repo_name: [msb_repo,
+                        msb_repo_path,
+                        msb_repo_changelog,
+                        msb_repo_tag],
+
+        csb_repo_name: [csb_repo,
+                        csb_repo_path,
+                        csb_repo_changelog,
+                        csb_repo_tag],
+
+        conraid_repo_name: [conraid_repo,
+                            conraid_repo_path,
+                            conraid_repo_changelog,
+                            conraid_repo_tag],
+
+        slackonly_repo_name: [slackonly_repo,
+                              slackonly_repo_path,
+                              slackonly_repo_changelog,
+                              slackonly_repo_tag],
+
+        salixos_repo_name: [salixos_repo,
+                            salixos_repo_path,
+                            salixos_repo_changelog,
+                            salixos_repo_tag],
+
+        salixos_extra_repo_name: [salixos_extra_repo,
+                                  salixos_extra_repo_path,
+                                  salixos_extra_repo_changelog,
+                                  slack_extra_repo_tag],
+
+        salixos_patches_repo_name: [salixos_patches_repo,
+                                    salixos_patches_repo_path,
+                                    salixos_patches_repo_changelog,
+                                    salixos_patches_repo_tag],
+
+        slackel_repo_name: [slackel_repo,
+                            slackel_repo_path,
+                            slackel_repo_changelog,
+                            slackel_repo_tag],
+
+        slint_repo_name: [slint_repo,
+                          slint_repo_path,
+                          slint_repo_changelog,
+                          slint_repo_tag]
     }
 
     # All the binary repositories names.
     bin_repos_names = list(repositories.keys())[2:]
 
     # All the enabled binary repositories names.
     for repo, enabled in repositories.items():
```

### Comparing `slpkg-4.7.5/slpkg/repo_info.py` & `slpkg-4.7.6/slpkg/repo_info.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/sbos/queries.py` & `slpkg-4.7.6/slpkg/sbos/queries.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/sbos/slackbuild.py` & `slpkg-4.7.6/slpkg/sbos/slackbuild.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/sbos/dependencies.py` & `slpkg-4.7.6/slpkg/sbos/dependencies.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/form_configs.py` & `slpkg-4.7.6/slpkg/form_configs.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/update_repository.py` & `slpkg-4.7.6/slpkg/update_repository.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/progress_bar.py` & `slpkg-4.7.6/slpkg/progress_bar.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/downloader.py` & `slpkg-4.7.6/slpkg/downloader.py`

 * *Files 5% similar despite different names*

```diff
@@ -39,15 +39,15 @@
                 self.tools(url)
 
     def tools(self, url: str) -> None:
         """ Downloader tools wget, curl and lftp. """
         command: str = ''
         filename: str = url.split('/')[-1]
 
-        if self.downloader == 'wget':
+        if self.downloader in ['wget', 'wget2']:
             command: str = f'{self.downloader} {self.wget_options} --directory-prefix={self.path} "{url}"'
 
         elif self.downloader == 'curl':
             command: str = f'{self.downloader} {self.curl_options} "{url}" --output {self.path}/{filename}'
 
         elif self.downloader == 'lftp':
             command: str = f'{self.downloader} {self.lftp_get_options} {url} -o {self.path}'
```

### Comparing `slpkg-4.7.5/slpkg/models/models.py` & `slpkg-4.7.6/slpkg/models/models.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/views/view_package.py` & `slpkg-4.7.6/slpkg/views/view_package.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/views/version.py` & `slpkg-4.7.6/slpkg/views/version.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
 class Version:
     """ Print the version. """
 
     def __init__(self):
-        self.version_info: tuple = (4, 7, 5)
+        self.version_info: tuple = (4, 7, 6)
         self.version: str = '{0}.{1}.{2}'.format(*self.version_info)
         self.license: str = 'MIT License'
         self.author: str = 'Dimitris Zlatanidis (dslackw)'
         self.homepage: str = 'https://dslackw.gitlab.io/slpkg'
 
     def view(self) -> None:
         """ Prints the version. """
```

### Comparing `slpkg-4.7.5/slpkg/views/cli_menu.py` & `slpkg-4.7.6/slpkg/views/cli_menu.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/views/ascii.py` & `slpkg-4.7.6/slpkg/views/ascii.py`

 * *Files 0% similar despite different names*

```diff
@@ -63,15 +63,15 @@
 
         print(f'{self.vertical_line}{self.endc} {message}' + ' ' * (self.columns - len(message) - 3) +
               f'{self.bgreen}{self.vertical_line}')
 
         self.draw_middle_line()
 
         print(f'{self.bgreen}{self.vertical_line}{self.endc} Package:' + ' ' * 22 + 'Version:' +
-              ' ' * (self.columns - 65) + 'Size:' + ' ' * 13 + f'Repo:{self.bgreen} {self.vertical_line}{self.endc}')
+              ' ' * (self.columns - 66) + 'Size:' + ' ' * 14 + f'Repo:{self.bgreen} {self.vertical_line}{self.endc}')
 
     def draw_view_package(self, package: str, version: str, size: str, color: str, repo: str) -> None:
         """ Draw nad print the packages. """
         if self.columns <= 80 and len(version) >= 11:
             version: str = f'{version[:10]}...'
         if self.columns <= 80 and len(package) >= 25:
             package: str = f'{package[:24]}...'
```

### Comparing `slpkg-4.7.5/slpkg/views/help_commands.py` & `slpkg-4.7.6/slpkg/views/help_commands.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/views/views.py` & `slpkg-4.7.6/slpkg/views/views.py`

 * *Files 7% similar despite different names*

```diff
@@ -68,14 +68,18 @@
         # If the package is installed and change the color to gray.
         if package in self.utils.installed_package_names and mode == 'install':
             color: str = self.grey
 
         if self.upgrade.is_package_upgradeable(package) and mode == 'install':
             color: str = self.violet
 
+        if (package in self.utils.installed_package_names and mode == 'install'
+                and self.utils.is_option(self.flag_reinstall, self.flags)):
+            color: str = self.violet
+
         self.ascii.draw_view_package(package, version, size, color, repo)
 
     def view_skipping_packages(self, package: str, version: str) -> None:
         """ Print the skipping packages. """
         print(f'[{self.yellow}Skipping{self.endc}] {package}-{version} {self.red}(already installed){self.endc}')
 
     def build_packages(self, slackbuilds: list, dependencies: list) -> None:
@@ -170,15 +174,15 @@
     def _view_removed(self, name: str) -> None:
         """ View and creates list with packages for remove. """
         installed = self.utils.is_package_installed(name)
 
         if installed:
             pkg: list = self.utils.split_binary_pkg(installed)
             self.installed_packages.append(installed)
-            size: str = self.utils.get_file_size(f'{self.log_packages}/{installed}')
+            size: str = self.utils.get_file_size(Path(self.log_packages, installed))
             self.ascii.draw_view_package(pkg[0], pkg[1], size, self.red, '')
 
     def choose_dependencies_for_remove(self, dependencies: list) -> list:
         """ Choose packages for remove using the dialog box. """
         height: int = 10
         width: int = 70
         list_height: int = 0
```

### Comparing `slpkg-4.7.5/slpkg/checks.py` & `slpkg-4.7.6/slpkg/checks.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/checksum.py` & `slpkg-4.7.6/slpkg/checksum.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/dialog_box.py` & `slpkg-4.7.6/slpkg/dialog_box.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/configs.py` & `slpkg-4.7.6/slpkg/configs.py`

 * *Files 3% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 # -*- coding: utf-8 -*-
 
 import os
 import tomli
 import platform
 from pathlib import Path
 from dataclasses import dataclass
+from slpkg.logging_config import LoggingConfig
 
 
 class Load:
 
     def __init__(self):
         bold = '\033[1m'
         red = '\x1b[91m'
@@ -109,20 +110,21 @@
                              f"{error}: in the configuration file '/etc/slpkg/slpkg.toml'.\n"
                              f"\nIf you have upgraded the '{prog_name}' probably you need to run:\n"
                              f"'mv {etc_path}/{prog_name}.toml.new {etc_path}/{prog_name}.toml'.\n"
                              f"or '{color['cyan']}slpkg_new-configs{color['endc']}' command.\n")
 
     # Creating the paths if not exists
     paths = [
-        tmp_slpkg,
-        build_path,
-        download_only_path,
+        db_path,
         lib_path,
         etc_path,
-        db_path,
+        build_path,
+        tmp_slpkg,
+        download_only_path,
+        LoggingConfig.log_path
     ]
 
     for path in paths:
         if not os.path.isdir(path):
             os.makedirs(path)
 
     @classmethod
```

### Comparing `slpkg-4.7.5/slpkg/clean_logs.py` & `slpkg-4.7.6/slpkg/clean_logs.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/utilities.py` & `slpkg-4.7.6/slpkg/utilities.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,22 +1,24 @@
 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
 import re
 import time
 import shutil
+import logging
 import subprocess
 from pathlib import Path
 from typing import Generator, Union
 
 from slpkg.configs import Configs
 from slpkg.blacklist import Blacklist
 from slpkg.sbos.queries import SBoQueries
 from slpkg.repositories import Repositories
 from slpkg.binaries.queries import BinQueries
+from slpkg.logging_config import LoggingConfig
 
 
 class Utilities:
 
     def __init__(self):
         self.configs = Configs
         self.colors = self.configs.colour
@@ -31,49 +33,59 @@
         self.endc: str = self.color['endc']
         self.bred: str = f'{self.bold}{self.red}'
         self.flag_bin_repository: list = ['-B', '--bin-repo=']
 
         self.installed_packages: list = list(self.all_installed())
         self.installed_package_names: list = list(self.all_installed_names())
 
+        logging.basicConfig(filename=LoggingConfig.log_file,
+                            filemode='w',
+                            encoding='utf-8',
+                            level=logging.INFO)
+
     def is_package_installed(self, name: str) -> str:
         """ Returns the installed package name. """
         for package in self.installed_packages:
             pkg_name: str = self.split_binary_pkg(package)[0]
 
             if pkg_name == name:
                 return package
 
         return ''
 
     def all_installed(self) -> Generator:
         """ Return all installed packages from /val/log/packages folder. """
-        var_log_packages = Path(self.configs.log_packages)
-
+        var_log_packages: Path = Path(self.configs.log_packages)
         try:
             for file in var_log_packages.glob(self.configs.file_pattern):
-                package_name = self.split_binary_pkg(file.name)[0]
+                name = self.split_binary_pkg(file.name)[0]
 
-                if package_name not in self.black.packages():
+                if not name.startswith('.') and name not in self.black.packages():
                     yield file.name
-        except ValueError:
-            pass
+        except ValueError as err:
+            logger = logging.getLogger(__name__)
+            logger.info('%s: %s: %s', self.__class__.__name__,
+                        Utilities.all_installed.__name__,
+                        err)
 
     def all_installed_names(self) -> Generator:
         """ Return all installed packages names from /val/log/packages folder. """
         var_log_packages = Path(self.configs.log_packages)
 
         try:
             for file in var_log_packages.glob(self.configs.file_pattern):
-                package_name = self.split_binary_pkg(file.name)[0]
+                name = self.split_binary_pkg(file.name)[0]
 
-                if package_name not in self.black.packages():
-                    yield package_name
-        except ValueError:
-            pass
+                if not name.startswith('.') and name not in self.black.packages():
+                    yield name
+        except ValueError as err:
+            logger = logging.getLogger(__name__)
+            logger.info('%s: %s: %s', self.__class__.__name__,
+                        Utilities.all_installed_names.__name__,
+                        err)
 
     @staticmethod
     def remove_file_if_exists(path: Path, file: str) -> None:
         """ Clean the old files. """
         archive = Path(path, file)
         if archive.is_file():
             archive.unlink()
@@ -96,17 +108,16 @@
     def split_binary_pkg(package: str) -> list:
         """ Split the package by the name, version, arch, build and tag. """
         name: str = '-'.join(package.split('-')[:-3])
         version: str = ''.join(package[len(name):].split('-')[:-2])
         arch: str = ''.join(package[len(name + version) + 2:].split('-')[:-1])
         build_tag: str = package.split('-')[-1]
         build: str = ''.join(re.findall(r'\d+', build_tag[:2]))
-        tag: str = build_tag[len(build):].replace('_', '')
 
-        return [name, version, arch, build, tag]
+        return [name, version, arch, build]
 
     def finished_time(self, elapsed_time: float) -> None:
         """ Printing the elapsed time. """
         print(f'\n{self.yellow}Finished Successfully:{self.endc}',
               time.strftime(f'[{self.cyan}%H:%M:%S{self.endc}]',
                             time.gmtime(elapsed_time)))
 
@@ -169,15 +180,15 @@
             raise SystemExit(output)
 
     def raise_error_message(self, message: str) -> None:
         """ A general method to raise an error message and exit. """
         raise SystemExit(f"\n{self.configs.prog_name}: {self.bred}Error{self.endc}: {message}.\n")
 
     @staticmethod
-    def get_file_size(file):
+    def get_file_size(file: Path) -> str:
         """ Get the file size and converted to units. """
         unit: str = 'KB'
         file_size = Path(file).stat().st_size
         mb = file_size / 1024 ** 2
         gb = file_size / 1024 ** 3
 
         if mb >= 0.1:
```

### Comparing `slpkg-4.7.5/slpkg/dependees.py` & `slpkg-4.7.6/slpkg/dependees.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/check_updates.py` & `slpkg-4.7.6/slpkg/check_updates.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/remove_packages.py` & `slpkg-4.7.6/slpkg/remove_packages.py`

 * *Files 23% similar despite different names*

```diff
@@ -21,37 +21,37 @@
         self.packages: list = packages
         self.flags: list = flags
 
         self.session = Session
         self.color = self.colour()
         self.utils = Utilities()
         self.progress = ProgressBar()
+        self.view = ViewMessage(self.flags)
 
         self.output: int = 0
         self.installed_packages: list = []
         self.dependencies: list = []
-        self.remove_pkg = None
         self.stderr = None
         self.stdout = None
         self.bold: str = self.color['bold']
+        self.cyan: str = self.color['cyan']
         self.yellow: str = self.color['yellow']
         self.red: str = self.color['red']
         self.endc: str = self.color['endc']
         self.byellow: str = f'{self.bold}{self.yellow}'
         self.bred: str = f'{self.bold}{self.red}'
         self.flag_resolve_off: list = ['-o', '--resolve-off']
         self.flag_no_silent: list = ['-n', '--no-silent']
+        self.flag_yes: list = ['-y', '--yes']
 
     def remove(self) -> None:
         """ Removes package with dependencies. """
-        view = ViewMessage(self.flags)
+        self.installed_packages, self.dependencies = self.view.remove_packages(self.packages)
 
-        self.installed_packages, self.dependencies = view.remove_packages(self.packages)
-
-        view.question()
+        self.view.question()
 
         start: float = time.time()
         self.remove_packages()
 
         if self.dependencies and not self.utils.is_option(self.flag_resolve_off, self.flags):
             self.delete_deps_logs()
 
@@ -60,17 +60,55 @@
         elapsed_time: float = time.time() - start
 
         self.utils.finished_time(elapsed_time)
 
     def remove_packages(self) -> None:
         """ Run Slackware command to remove the packages. """
         for package in self.installed_packages:
-            self.remove_pkg = package
-            command: str = f'{self.removepkg} {package}'
-            self.multi_process(command, package)
+            name: str = self.utils.split_binary_pkg(package)[0]
+
+            if self.check_in_logs_for_dependencies_to_remove(name):
+                command: str = f'{self.removepkg} {package}'
+                self.multi_process(command, package)
+
+    def check_in_logs_for_dependencies_to_remove(self, name: str) -> bool:
+        dependencies: list = []
+        logs: dict = self.query_dependencies()
+
+        for package, requires in logs.items():
+            if name in requires:
+                dependencies.append(package)
+
+        if dependencies and not self.utils.is_option(self.flag_yes, self.flags) and self.ask_question:
+            print(f"\n[{self.bred}WARNING!{self.endc}] The package '{self.red}{name}{self.endc}' "
+                  f"is a dependency for the packages:")
+
+            for dep in dependencies:
+                print(f"{self.cyan:>16}-> {dep}{self.endc}")
+
+            answer: str = input('\nDo you want to remove? [y/N] ')
+
+            if answer not in ['Y', 'y']:
+                return False
+            print()
+
+        return True
+
+    def query_dependencies(self) -> dict:
+        """ Returns a dictionary with the package name and the dependencies
+            before they are saved with the command slpkg install. """
+        logs_deps: dict = {}
+        package_requires: tuple = self.session.query(
+            LogsDependencies.name, LogsDependencies.requires).all()
+
+        for package in package_requires:
+            if package[0] not in self.packages:
+                logs_deps[package[0]] = package[1].split()
+
+        return logs_deps
 
     def delete_main_logs(self) -> None:
         """ Deletes main packages from logs. """
         for pkg in self.packages:
             self.session.query(LogsDependencies).filter(
                 LogsDependencies.name == pkg).delete()
         self.session.commit()
```

### Comparing `slpkg-4.7.5/slpkg/blacklist.py` & `slpkg-4.7.6/slpkg/blacklist.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/download_only.py` & `slpkg-4.7.6/slpkg/download_only.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/tracking.py` & `slpkg-4.7.6/slpkg/tracking.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/main.py` & `slpkg-4.7.6/slpkg/main.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
 import os
 import sys
+import logging
 from pathlib import Path
 
 from slpkg.checks import Check
 from slpkg.upgrade import Upgrade
 from slpkg.configs import Configs
 from slpkg.tracking import Tracking
 from slpkg.repo_info import RepoInfo
@@ -22,14 +23,15 @@
 from slpkg.form_configs import FormConfigs
 from slpkg.views.help_commands import Help
 from slpkg.repositories import Repositories
 from slpkg.binaries.install import Packages
 from slpkg.check_updates import CheckUpdates
 from slpkg.sbos.slackbuild import Slackbuilds
 from slpkg.binaries.queries import BinQueries
+from slpkg.logging_config import LoggingConfig
 from slpkg.find_installed import FindInstalled
 from slpkg.views.view_package import ViewPackage
 from slpkg.remove_packages import RemovePackages
 from slpkg.clean_logs import CleanLogsDependencies
 from slpkg.update_repository import UpdateRepository
 
 
@@ -203,14 +205,16 @@
                 self.flag_short_directory,
                 self.flag_bin_repository,
                 self.flag_short_bin_repository,
                 self.flag_parallel,
                 self.flag_short_parallel
             ],
             'remove': [
+                self.flag_yes,
+                self.flag_short_yes,
                 self.flag_resolve_off,
                 self.flag_short_resolve_off,
                 self.flag_search,
                 self.flag_short_search,
                 self.flag_no_silent,
                 self.flag_short_no_silent,
             ],
@@ -277,14 +281,19 @@
         self.move_options()
         self.invalid_options()
         self.check_for_bin_repositories()
 
         self.check = Check(self.flags)
         self.check.is_blacklist(self.args[1:])
 
+        logging.basicConfig(filename=LoggingConfig.log_file,
+                            filemode='w',
+                            encoding='utf-8',
+                            level=logging.INFO)
+
     def check_for_bin_repositories(self) -> None:
         """ Checks combination for binaries use repositories only and if repository exists. """
         if self.utils.is_option(self.flag_binaries, self.flags):
 
             except_options: list = [
                 '-s', 'search',
                 '-u', 'update',
@@ -804,13 +813,15 @@
         '-e': argparse.dependees,
         'tracking': argparse.tracking,
         '-t': argparse.tracking
     }
 
     try:
         arguments[args[0]]()
-    except (KeyError, IndexError):
+    except (KeyError, IndexError) as err:
+        logger = logging.getLogger(__name__)
+        logger.info('%s: %s', main.__name__, err)
         usage.help_short(1)
 
 
 if __name__ == '__main__':
     main()
```

### Comparing `slpkg-4.7.5/slpkg/find_installed.py` & `slpkg-4.7.6/slpkg/find_installed.py`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/slpkg/upgrade.py` & `slpkg-4.7.6/slpkg/search.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,64 +1,92 @@
 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
 from typing import Generator
-from packaging.version import parse
 
 from slpkg.configs import Configs
 from slpkg.utilities import Utilities
 from slpkg.sbos.queries import SBoQueries
+from slpkg.repositories import Repositories
 from slpkg.binaries.queries import BinQueries
 
 
-class Upgrade(Configs):
-    """ Upgrade the installed packages. """
+class SearchPackage(Configs):
+    """ Search packages from the repositories. """
 
-    def __init__(self, flags: list, repo=None):
+    def __init__(self, flags=None):
         super(Configs, self).__init__()
         self.flags: list = flags
-        self.repo: str = repo
+
+        self.color = self.colour()
         self.utils = Utilities()
+        self.repos = Repositories()
+
+        self.yellow: str = self.color['yellow']
+        self.cyan: str = self.color['cyan']
+        self.green: str = self.color['green']
+        self.grey: str = self.color['grey']
+        self.endc: str = self.color['endc']
 
         self.flag_bin_repository: list = ['-B', '--bin-repo=']
-        self.repo_for_binaries: bool = self.utils.is_option(self.flag_bin_repository, self.flags)
 
-        self.all_installed: list = self.utils.installed_packages
+    def package(self, packages: list, repo=None) -> None:
+        """ Searching and print the matched packages. """
+        matching: int = 0
+        repository: str = ''
+
+        print(f'The list below shows the repo '
+              f'packages that contains \'{", ".join([p for p in packages])}\':\n')
 
-    def packages(self) -> Generator[str, None, None]:
-        """ Compares version of packages and returns the maximum. """
+        # Searching for binaries.
         if self.utils.is_option(self.flag_bin_repository, self.flags):
-            repo_packages: list = list(BinQueries('', self.repo).all_package_names_by_repo())
-        else:
-            repo_packages: list = list(SBoQueries('').sbos())
+            if repo == '*':
+                pkg_repo: tuple = BinQueries('', repo).all_package_names_from_repositories()
+
+                for pkg in packages:
+                    for pr in pkg_repo:
 
-        for pkg in self.all_installed:
-            inst_package: str = self.utils.split_binary_pkg(pkg)[0]
+                        if pkg in pr[0] or pkg == '*':
+                            matching += 1
 
-            if inst_package in repo_packages:
+                            desc: str = BinQueries(pr[0], pr[1]).description()
+                            version: str = BinQueries(pr[0], pr[1]).version()
 
-                if self.is_package_upgradeable(inst_package):
-                    yield inst_package
+                            if repo == '*':
+                                repository: str = f'{pr[1]}: '
 
-    def is_package_upgradeable(self, name: str) -> bool:
-        """ Checks for installed and upgradeable packages. """
-        repo_version = repo_build = '0'
-        inst_version = inst_build = '0'
-        inst_package: str = self.utils.is_package_installed(name)
+                            print(f'{repository}{self.cyan}{pr[0]}{self.endc} {self.yellow}{version}{self.endc}'
+                                  f'{self.green}{desc}{self.endc}')
+            else:
+                pkg_repo: Generator = BinQueries('', repo).all_package_names_by_repo()
 
-        if inst_package:
-            inst_version: str = self.utils.split_binary_pkg(inst_package)[1]
-            inst_build: str = self.utils.split_binary_pkg(inst_package)[3]
+                for pkg in packages:
+                    for pr in pkg_repo:
 
-            if self.repo_for_binaries and BinQueries(name, self.repo).package_bin():
-                repo_package: str = BinQueries(name, self.repo).package_bin()
-                repo_version: str = BinQueries(name, self.repo).version()
-                repo_build: str = self.utils.split_binary_pkg(repo_package)[3]
+                        if pkg in pr or pkg == '*':
+                            matching += 1
 
-            elif not self.repo_for_binaries and SBoQueries(name).slackbuild():
-                repo_version: str = SBoQueries(name).version()
-                repo_build: str = self.utils.read_sbo_build_tag(name)
+                            desc: str = BinQueries(pr, repo).description()
+                            version: str = BinQueries(pr, repo).version()
 
-        # print(f'{name} {repo_version}{repo_build} {inst_version}{inst_build}',
-        # parse(f'{repo_version}{repo_build}') > parse(f'{inst_version}{inst_build}'))
+                            print(f'{repository}{self.cyan}{pr}{self.endc} {self.yellow}{version}{self.endc}'
+                                  f'{self.green}{desc}{self.endc}')
 
-        return parse(f'{repo_version}{repo_build}') > parse(f'{inst_version}{inst_build}')
+        else:
+            # Searching for slackbuilds.
+            names: Generator = SBoQueries('').sbos()
+            for name in names:
+                for package in packages:
+
+                    if package in name or package == '*':
+                        matching += 1
+
+                        desc: str = SBoQueries(name).description().replace(name, '')
+                        version: str = SBoQueries(name).version()
+
+                        print(f'{self.cyan}{name}{self.endc}-{self.yellow}'
+                              f'{version}{self.endc}{self.green}{desc}{self.endc}')
+
+        if not matching:
+            print('\nDoes not match any package.\n')
+        else:
+            print(f'\n{self.grey}Total found {matching} packages.{self.endc}')
```

### Comparing `slpkg-4.7.5/setup.cfg` & `slpkg-4.7.6/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = slpkg
-version = 4.7.5
+version = 4.7.6
 license_file = LICENSE
 author = Dimitris Zlatanidis
 author_email = d.zlatanidis@gmail.com
 description = Packaging tool that interacts with the SBo repository
 long_description = file:README.rst
 url = https://dslackw.gitlab.io/slpkg/
 project_urls =
```

### Comparing `slpkg-4.7.5/slpkg.egg-info/SOURCES.txt` & `slpkg-4.7.6/slpkg.egg-info/SOURCES.txt`

 * *Files 17% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 slpkg/dependees.py
 slpkg/dialog_box.py
 slpkg/download_only.py
 slpkg/downloader.py
 slpkg/find_installed.py
 slpkg/form_configs.py
 slpkg/install_data.py
+slpkg/logging_config.py
 slpkg/main.py
 slpkg/progress_bar.py
 slpkg/remove_packages.py
 slpkg/repo_info.py
 slpkg/repositories.py
 slpkg/search.py
 slpkg/tracking.py
```

### Comparing `slpkg-4.7.5/slpkg.egg-info/PKG-INFO` & `slpkg-4.7.6/slpkg.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slpkg
-Version: 4.7.5
+Version: 4.7.6
 Summary: Packaging tool that interacts with the SBo repository
 Home-page: https://dslackw.gitlab.io/slpkg/
 Author: Dimitris Zlatanidis
 Author-email: d.zlatanidis@gmail.com
 License: UNKNOWN
 Project-URL: Source, https://dslackw.gitlab.io/slpkg/
 Project-URL: Documentation, https://dslackw.gitlab.io/slpkg/
@@ -58,16 +58,16 @@
 Install
 -------
 
 Install from the official third-party `SBo repository <https://slackbuilds.org/repository/15.0/system/slpkg/>`_ or directly from source:
 
 .. code-block:: bash
 
-    $ tar xvf slpkg-4.7.4.tar.gz
-    $ cd slpkg-4.7.4
+    $ tar xvf slpkg-4.7.6.tar.gz
+    $ cd slpkg-4.7.6
     $ ./install.sh
 
 Screenshots
 -----------
 
 .. image:: https://gitlab.com/dslackw/images/raw/master/slpkg/slpkg_install.png
     :target: https://gitlab.com/dslackw/slpkg
@@ -168,14 +168,22 @@
 - `Slackonly <https://packages.slackonly.com/pub/packages/15.0-x86_64/>`_ repository.
 - `Salix OS <https://download.salixos.org/x86_64/slackware-15.0/>`_ repository.
 - `Salix OS extra <https://download.salixos.org/x86_64/slackware-15.0/extra/>`_ repository.
 - `Salix OS patches <https://download.salixos.org/x86_64/slackware-15.0/patches/>`_ repository.
 - `Slackel OS <http://www.slackel.gr/repo/x86_64/current/>`_ repository.
 - `Slint OS <https://slackware.uk/slint/x86_64/slint-15.0/>`_ repository.
 
+
+Multilib packages
+-----------------
+
+Slackware for x86_64 - multilib packages & install instructions:
+
+- Please read the file `README <https://gitlab.com/dslackw/slpkg/-/raw/master/filelists/multilib/README>`_ you will find in the folder `multlib <https://gitlab.com/dslackw/slpkg/-/tree/master/filelists/multilib>`_.
+
 Donate
 ------
 
 If you feel satisfied with this project and want to thanks me make a donation.
 
 .. image:: https://gitlab.com/dslackw/images/raw/master/donate/paypaldonate.png
    :target: https://www.paypal.me/dslackw
```

### Comparing `slpkg-4.7.5/tools/gen_sbo_txt.sh` & `slpkg-4.7.6/tools/gen_sbo_txt.sh`

 * *Files identical despite different names*

### Comparing `slpkg-4.7.5/bin/slpkg_new-configs` & `slpkg-4.7.6/bin/slpkg_new-configs`

 * *Files identical despite different names*

