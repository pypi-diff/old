# Comparing `tmp/sett-4.1.0.tar.gz` & `tmp/sett-4.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sett-4.1.0.tar", last modified: Thu Nov 24 16:49:56 2022, max compression
+gzip compressed data, was "sett-4.2.0.tar", last modified: Thu Apr  6 14:02:37 2023, max compression
```

## Comparing `sett-4.1.0.tar` & `sett-4.2.0.tar`

### file list

```diff
@@ -1,78 +1,78 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.287923 sett-4.1.0/
--rw-rw-rw-   0 root         (0) root         (0)    35149 2022-11-24 16:49:43.000000 sett-4.1.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     2988 2022-11-24 16:49:56.287923 sett-4.1.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     1844 2022-11-24 16:49:43.000000 sett-4.1.0/README.md
--rw-rw-rw-   0 root         (0) root         (0)     1992 2022-11-24 16:49:43.000000 sett-4.1.0/pyproject.toml
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.268922 sett-4.1.0/sett/
--rw-rw-rw-   0 root         (0) root         (0)     2444 2022-11-24 16:49:43.000000 sett-4.1.0/sett/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.271922 sett-4.1.0/sett/cli/
--rw-rw-rw-   0 root         (0) root         (0)    12683 2022-11-24 16:49:43.000000 sett-4.1.0/sett/cli/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    18797 2022-11-24 16:49:43.000000 sett-4.1.0/sett/cli/cli_builder.py
--rw-rw-rw-   0 root         (0) root         (0)     3394 2022-11-24 16:49:43.000000 sett-4.1.0/sett/cli/progress.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.274922 sett-4.1.0/sett/core/
--rw-rw-rw-   0 root         (0) root         (0)       49 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     9765 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/archive.py
--rw-rw-rw-   0 root         (0) root         (0)     6613 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/checksum.py
--rw-rw-rw-   0 root         (0) root         (0)    14811 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/crypt.py
--rw-rw-rw-   0 root         (0) root         (0)      442 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/error.py
--rw-rw-rw-   0 root         (0) root         (0)     6635 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/filesystem.py
--rw-rw-rw-   0 root         (0) root         (0)      651 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/metadata.py
--rw-rw-rw-   0 root         (0) root         (0)     2046 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/request.py
--rw-rw-rw-   0 root         (0) root         (0)     1448 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/secret.py
--rw-rw-rw-   0 root         (0) root         (0)     2232 2022-11-24 16:49:43.000000 sett-4.1.0/sett/core/versioncheck.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.279923 sett-4.1.0/sett/gui/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2451 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/__main__.py
--rw-rw-rw-   0 root         (0) root         (0)    15962 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/component.py
--rw-rw-rw-   0 root         (0) root         (0)     3509 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/decrypt_tab.py
--rw-rw-rw-   0 root         (0) root         (0)    14093 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/encrypt_tab.py
--rw-rw-rw-   0 root         (0) root         (0)     6495 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/file_selection_widget.py
--rw-rw-rw-   0 root         (0) root         (0)     6594 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/key_generation_dialog.py
--rw-rw-rw-   0 root         (0) root         (0)     3316 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/keys_download_dialog.py
--rw-rw-rw-   0 root         (0) root         (0)    18692 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/keys_tab.py
--rw-rw-rw-   0 root         (0) root         (0)     2252 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/listener.py
--rw-rw-rw-   0 root         (0) root         (0)     9104 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/main_window.py
--rw-rw-rw-   0 root         (0) root         (0)     9776 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/model.py
--rw-rw-rw-   0 root         (0) root         (0)     5864 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/parallel.py
--rw-rw-rw-   0 root         (0) root         (0)     1555 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/pyside.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.280923 sett-4.1.0/sett/gui/resources/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/resources/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   401906 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/resources/rc_icons.py
--rw-rw-rw-   0 root         (0) root         (0)    17360 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/settings_tab.py
--rw-rw-rw-   0 root         (0) root         (0)     2422 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/theme.py
--rw-rw-rw-   0 root         (0) root         (0)    17459 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/transfer_tab.py
--rw-rw-rw-   0 root         (0) root         (0)     6827 2022-11-24 16:49:43.000000 sett-4.1.0/sett/gui/ui_model_bind.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.283923 sett-4.1.0/sett/protocols/
--rw-rw-rw-   0 root         (0) root         (0)      669 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)       38 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/defs.py
--rw-rw-rw-   0 root         (0) root         (0)     4261 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/liquid_files.py
--rw-rw-rw-   0 root         (0) root         (0)     1243 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/multipart.py
--rw-rw-rw-   0 root         (0) root         (0)      441 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/protocol.py
--rw-rw-rw-   0 root         (0) root         (0)     1921 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/s3.py
--rw-rw-rw-   0 root         (0) root         (0)    11403 2022-11-24 16:49:43.000000 sett-4.1.0/sett/protocols/sftp.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-24 16:49:43.000000 sett-4.1.0/sett/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.285923 sett-4.1.0/sett/utils/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    18393 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/config.py
--rw-rw-rw-   0 root         (0) root         (0)     5875 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/error_handling.py
--rw-rw-rw-   0 root         (0) root         (0)     1430 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/get_config_path.py
--rw-rw-rw-   0 root         (0) root         (0)     9691 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/log.py
--rw-rw-rw-   0 root         (0) root         (0)    16450 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/progress.py
--rw-rw-rw-   0 root         (0) root         (0)      445 2022-11-24 16:49:43.000000 sett-4.1.0/sett/utils/validation.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2022-11-24 16:49:43.000000 sett-4.1.0/sett/version.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.287923 sett-4.1.0/sett/workflows/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      559 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/config.py
--rw-rw-rw-   0 root         (0) root         (0)     7627 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/decrypt.py
--rw-rw-rw-   0 root         (0) root         (0)    19851 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/encrypt.py
--rw-rw-rw-   0 root         (0) root         (0)     8138 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/transfer.py
--rw-rw-rw-   0 root         (0) root         (0)     2634 2022-11-24 16:49:43.000000 sett-4.1.0/sett/workflows/upload_keys.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-24 16:49:56.270922 sett-4.1.0/sett.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2988 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1571 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       86 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-11-24 16:49:54.000000 sett-4.1.0/sett.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      340 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        5 2022-11-24 16:49:56.000000 sett-4.1.0/sett.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)     1690 2022-11-24 16:49:56.288923 sett-4.1.0/setup.cfg
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.100698 sett-4.2.0/
+-rw-rw-rw-   0 root         (0) root         (0)    35149 2023-04-06 14:02:23.000000 sett-4.2.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     3072 2023-04-06 14:02:37.100698 sett-4.2.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1852 2023-04-06 14:02:23.000000 sett-4.2.0/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     1992 2023-04-06 14:02:23.000000 sett-4.2.0/pyproject.toml
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.081696 sett-4.2.0/sett/
+-rw-rw-rw-   0 root         (0) root         (0)     2444 2023-04-06 14:02:23.000000 sett-4.2.0/sett/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.084697 sett-4.2.0/sett/cli/
+-rw-rw-rw-   0 root         (0) root         (0)    12781 2023-04-06 14:02:23.000000 sett-4.2.0/sett/cli/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18796 2023-04-06 14:02:23.000000 sett-4.2.0/sett/cli/cli_builder.py
+-rw-rw-rw-   0 root         (0) root         (0)     3394 2023-04-06 14:02:23.000000 sett-4.2.0/sett/cli/progress.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.087697 sett-4.2.0/sett/core/
+-rw-rw-rw-   0 root         (0) root         (0)       49 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     9765 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/archive.py
+-rw-rw-rw-   0 root         (0) root         (0)     6613 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/checksum.py
+-rw-rw-rw-   0 root         (0) root         (0)    15030 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/crypt.py
+-rw-rw-rw-   0 root         (0) root         (0)      442 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/error.py
+-rw-rw-rw-   0 root         (0) root         (0)     6635 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/filesystem.py
+-rw-rw-rw-   0 root         (0) root         (0)      651 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/metadata.py
+-rw-rw-rw-   0 root         (0) root         (0)     2046 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/request.py
+-rw-rw-rw-   0 root         (0) root         (0)     1448 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/secret.py
+-rw-rw-rw-   0 root         (0) root         (0)     2147 2023-04-06 14:02:23.000000 sett-4.2.0/sett/core/versioncheck.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.092697 sett-4.2.0/sett/gui/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2451 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/__main__.py
+-rw-rw-rw-   0 root         (0) root         (0)    15705 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/component.py
+-rw-rw-rw-   0 root         (0) root         (0)     3494 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/decrypt_tab.py
+-rw-rw-rw-   0 root         (0) root         (0)    14189 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/encrypt_tab.py
+-rw-rw-rw-   0 root         (0) root         (0)     6383 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/file_selection_widget.py
+-rw-rw-rw-   0 root         (0) root         (0)     6588 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/key_generation_dialog.py
+-rw-rw-rw-   0 root         (0) root         (0)     3272 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/keys_download_dialog.py
+-rw-rw-rw-   0 root         (0) root         (0)    18587 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/keys_tab.py
+-rw-rw-rw-   0 root         (0) root         (0)     2252 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/listener.py
+-rw-rw-rw-   0 root         (0) root         (0)     9076 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/main_window.py
+-rw-rw-rw-   0 root         (0) root         (0)    10030 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/model.py
+-rw-rw-rw-   0 root         (0) root         (0)     5864 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/parallel.py
+-rw-rw-rw-   0 root         (0) root         (0)     1555 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/pyside.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.093697 sett-4.2.0/sett/gui/resources/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/resources/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   401906 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/resources/rc_icons.py
+-rw-rw-rw-   0 root         (0) root         (0)    17134 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/settings_tab.py
+-rw-rw-rw-   0 root         (0) root         (0)     2422 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/theme.py
+-rw-rw-rw-   0 root         (0) root         (0)    21237 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/transfer_tab.py
+-rw-rw-rw-   0 root         (0) root         (0)     6827 2023-04-06 14:02:23.000000 sett-4.2.0/sett/gui/ui_model_bind.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.096697 sett-4.2.0/sett/protocols/
+-rw-rw-rw-   0 root         (0) root         (0)      669 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)       38 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/defs.py
+-rw-rw-rw-   0 root         (0) root         (0)     4261 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/liquid_files.py
+-rw-rw-rw-   0 root         (0) root         (0)     1243 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/multipart.py
+-rw-rw-rw-   0 root         (0) root         (0)      441 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/protocol.py
+-rw-rw-rw-   0 root         (0) root         (0)     2149 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/s3.py
+-rw-rw-rw-   0 root         (0) root         (0)    11403 2023-04-06 14:02:23.000000 sett-4.2.0/sett/protocols/sftp.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 14:02:23.000000 sett-4.2.0/sett/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.098698 sett-4.2.0/sett/utils/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18470 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/config.py
+-rw-rw-rw-   0 root         (0) root         (0)     5875 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/error_handling.py
+-rw-rw-rw-   0 root         (0) root         (0)     1430 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/get_config_path.py
+-rw-rw-rw-   0 root         (0) root         (0)     9691 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/log.py
+-rw-rw-rw-   0 root         (0) root         (0)    16450 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/progress.py
+-rw-rw-rw-   0 root         (0) root         (0)      445 2023-04-06 14:02:23.000000 sett-4.2.0/sett/utils/validation.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2023-04-06 14:02:23.000000 sett-4.2.0/sett/version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.100698 sett-4.2.0/sett/workflows/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      559 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/config.py
+-rw-rw-rw-   0 root         (0) root         (0)     7625 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/decrypt.py
+-rw-rw-rw-   0 root         (0) root         (0)    20009 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/encrypt.py
+-rw-rw-rw-   0 root         (0) root         (0)     8137 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/transfer.py
+-rw-rw-rw-   0 root         (0) root         (0)     2634 2023-04-06 14:02:23.000000 sett-4.2.0/sett/workflows/upload_keys.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 14:02:37.083697 sett-4.2.0/sett.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     3072 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1571 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       86 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 14:02:35.000000 sett-4.2.0/sett.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      471 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        5 2023-04-06 14:02:37.000000 sett-4.2.0/sett.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)     1908 2023-04-06 14:02:37.101698 sett-4.2.0/setup.cfg
```

### Comparing `sett-4.1.0/LICENSE` & `sett-4.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/PKG-INFO` & `sett-4.2.0/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: sett
-Version: 4.1.0
+Version: 4.2.0
 Summary: Secure Encryption and Transfer Tool
 Home-page: https://gitlab.com/biomedit/sett
-Author: Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin
-Author-email: robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com
+Author: Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin, Simone Guzzi, Swen Vermeul
+Author-email: robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com, simone.guzzi@sib.swiss, swen@ethz.ch
 License: GPL3v3
-Project-URL: Documentation, https://sett.rtfd.io
+Project-URL: Documentation, https://sett.rtfd.io/en/stable
 Project-URL: Source, https://gitlab.com/biomedit/sett
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
@@ -30,22 +30,24 @@
 [![license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 [![python version](https://img.shields.io/pypi/pyversions/sett.svg?logo=python&logoColor=white)](https://pypi.org/project/sett)
 [![latest version](https://img.shields.io/pypi/v/sett.svg)](https://pypi.org/project/sett)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
 # SETT - Secure Encryption and Transfer Tool
 
-_sett_ enables packaging, encryption, and transfer of data to preconfigured locations.
+_sett_ enables packaging, encryption, and transfer of data to pre-configured
+locations.
 
 ## Documentation
 
 Detailed documentation as well as a quick-start guide can be found in the
-[sett documentation](https://sett.readthedocs.io).
+[sett documentation](https://sett.readthedocs.io/en/stable).
 
-For the latest, non-stable, version of the docs, see [here](<https://sett.readthedocs.io/en/latest/>).
+For the latest, non-stable, version of the docs, see
+[here](https://sett.readthedocs.io/en/latest).
 
 ### Documentation quick-links
 
 * [Requirements and installation](https://sett.readthedocs.io/en/stable/installation.html).
 * [Quick-start guide](https://sett.readthedocs.io/en/stable/quick_start.html).
 * [Creating and managing GnuPG keys with sett](https://sett.readthedocs.io/en/stable/key_management.html).
 * [Using sett to encrypt, transfer and decrypt data](https://sett.readthedocs.io/en/stable/usage.html)
```

### Comparing `sett-4.1.0/README.md` & `sett-4.2.0/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -4,22 +4,24 @@
 [![license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 [![python version](https://img.shields.io/pypi/pyversions/sett.svg?logo=python&logoColor=white)](https://pypi.org/project/sett)
 [![latest version](https://img.shields.io/pypi/v/sett.svg)](https://pypi.org/project/sett)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
 # SETT - Secure Encryption and Transfer Tool
 
-_sett_ enables packaging, encryption, and transfer of data to preconfigured locations.
+_sett_ enables packaging, encryption, and transfer of data to pre-configured
+locations.
 
 ## Documentation
 
 Detailed documentation as well as a quick-start guide can be found in the
-[sett documentation](https://sett.readthedocs.io).
+[sett documentation](https://sett.readthedocs.io/en/stable).
 
-For the latest, non-stable, version of the docs, see [here](<https://sett.readthedocs.io/en/latest/>).
+For the latest, non-stable, version of the docs, see
+[here](https://sett.readthedocs.io/en/latest).
 
 ### Documentation quick-links
 
 * [Requirements and installation](https://sett.readthedocs.io/en/stable/installation.html).
 * [Quick-start guide](https://sett.readthedocs.io/en/stable/quick_start.html).
 * [Creating and managing GnuPG keys with sett](https://sett.readthedocs.io/en/stable/key_management.html).
 * [Using sett to encrypt, transfer and decrypt data](https://sett.readthedocs.io/en/stable/usage.html)
```

### Comparing `sett-4.1.0/pyproject.toml` & `sett-4.2.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/__init__.py` & `sett-4.2.0/sett/__init__.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/cli/__init__.py` & `sett-4.2.0/sett/cli/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -120,20 +120,24 @@
     dry_run: bool,
     passphrase_cmd: Optional[str],
     dtr_id: Optional[int] = None,
     **kwargs: Any,
 ) -> Optional[str]:
     """Wrapper for the main function of the encrypt workflow."""
 
-    if config.sign_encrypted_data and not dry_run:
-        kwargs["passphrase"] = get_passphrase_from_cmd_or_prompt(
-            "Please enter your gpg private key password:", passphrase_cmd
+    # Retrieve the user's PGP key password (needed to sign the data).
+    kwargs["passphrase"] = (
+        None
+        if dry_run
+        else get_passphrase_from_cmd_or_prompt(
+            "Please enter your PGP private key password:", passphrase_cmd
         )
-    else:
-        kwargs["passphrase"] = None
+    )
+
+    # Run the encrypt workflow.
     try:
         return workflows_encrypt(
             *files,
             dtr_id=dtr_id,
             config=config,
             dry_run=dry_run,
             **kwargs,
@@ -216,134 +220,135 @@
     return cfg
 
 
 class Cli(CliWithSubcommands):
     description = __doc__.format(URL_READTHEDOCS, URL_GITLAB_ISSUES)
     version = VERSION_WITH_DEPS
     config = load_config_and_check_app_is_up_to_date()
-    passphrase_override = dict(
-        help="Instead of asking for passphrase, get it from an external command "
+    passphrase_override = {
+        "help": "Instead of asking for passphrase, get it from an external command "
         "(passphrase must be returned to the standard output).",
-        name="passphrase-cmd",
-        dest="passphrase_cmd",
-        type=str,
-    )
-    dry_run_override = dict(
-        help="Perform checks on the input data, without running the actual command."
-    )
+        "name": "passphrase-cmd",
+        "dest": "passphrase_cmd",
+        "type": str,
+    }
+    dry_run_override = {
+        "help": "Perform checks on the input data, without running the actual command."
+    }
     subcommands = (
         Subcommand(
             decorate(
                 encrypt,
                 partial(config=config),
                 lazy_partial(progress=CliProgress),
             ),
             overrides={
-                "files": dict(help="Input file(s) or directories."),
-                "sender": dict(
-                    help="Fingerprint, key ID or email associated "
+                "files": {"help": "Input file(s) or directories."},
+                "sender": {
+                    "help": "Fingerprint, key ID or email associated "
                     "with GPG key of data sender.",
-                    alias="-s",
-                ),
-                "recipient": dict(
-                    help="Fingerprint, key ID or email associated with "
+                    "alias": "-s",
+                },
+                "recipient": {
+                    "help": "Fingerprint, key ID or email associated with "
                     "GPG key of data recipient(s).",
-                    alias="-r",
-                ),
-                "dtr_id": dict(
-                    help="Data Transfer Request (DTR) ID (optional if "
+                    "alias": "-r",
+                },
+                "dtr_id": {
+                    "help": "Data Transfer Request (DTR) ID (optional if "
                     "`verify_dtr` is disabled in settings).",
-                    alias="-t",
-                ),
-                "purpose": dict(
-                    help="Purpose of the DTR (PRODUCTION, TEST). "
+                    "alias": "-t",
+                },
+                "purpose": {
+                    "help": "Purpose of the DTR (PRODUCTION, TEST). "
                     "Mandatory only if `transfer_id` is specified."
-                ),
-                "force": dict(
-                    help="Ignore errors about missing disk space", alias="-f"
-                ),
-                "output": dict(
-                    help="Output path (directory path and/or file name) of "
+                },
+                "force": {
+                    "help": "Ignore errors about missing disk space",
+                    "alias": "-f",
+                },
+                "output": {
+                    "help": "Output path (directory path and/or file name) of "
                     "the encrypted package. If no directory path is specified, "
                     "the output package is saved in the current working "
                     "directory. If this argument is missing or the path is a "
                     "directory, the file name is generated based on the "
                     "current date and an optional suffix.",
-                    default=None,
-                    alias="-o",
-                ),
-                "output_suffix": dict(help="Output file name suffix (optional)"),
+                    "default": None,
+                    "alias": "-o",
+                },
+                "output_suffix": {"help": "Output file name suffix (optional)"},
                 "dry_run": dry_run_override,
-                "compression_level": dict(
-                    help="Compression level for inner tarball in the range "
+                "compression_level": {
+                    "help": "Compression level for inner tarball in the range "
                     "0 (no compression) to 9 (highest compression). "
                     "Higher compression levels require more computing "
                     "time."
-                ),
+                },
                 "passphrase": passphrase_override,
             },
         ),
         Subcommand(
             decorate(
                 transfer,
                 partial(config=config, two_factor_callback=two_factor_cli_prompt),
                 lazy_partial(progress=CliProgress),
             ),
             overrides={
-                "files": dict(help="Path(s) to encrypted package(s)"),
-                "protocol": dict(
-                    help=f"The protocol for the file transfer."
+                "files": {"help": "Path(s) to encrypted package(s)"},
+                "protocol": {
+                    "help": f"The protocol for the file transfer."
                     f"Currently available: {', '.join(available_protocols)}",
-                    type=parse_protocol,
-                    alias="-p",
-                ),
-                "protocol_args": dict(
-                    help="Protocol specific arguments. "
+                    "type": parse_protocol,
+                    "alias": "-p",
+                },
+                "protocol_args": {
+                    "help": "Protocol specific arguments. "
                     "Must be passed as a json string",
-                    type=parse_protocol_args,
-                ),
-                "connection": dict(
-                    help="Instead of the option 'protocol', load a connection "
+                    "type": parse_protocol_args,
+                },
+                "connection": {
+                    "help": "Instead of the option 'protocol', load a connection "
                     "named by the argument of this option to use the "
                     "protocol and protocol args from the config. The "
                     "protocol args can be overwritten by the "
                     "protocol_args option"
-                ),
-                "passphrase_cmd": dict(help=passphrase_override["help"]),
+                },
+                "passphrase_cmd": {"help": passphrase_override["help"]},
                 "dry_run": dry_run_override,
             },
         ),
         Subcommand(
             decorate(
                 decrypt, partial(config=config), lazy_partial(progress=CliProgress)
             ),
             overrides={
-                "files": dict(help="Path(s) to encrypted package(s)"),
-                "output_dir": dict(
-                    help="Path to the directory where package content is saved after decryption. "
+                "files": {"help": "Path(s) to encrypted package(s)"},
+                "output_dir": {
+                    "help": "Path to the directory where package content is saved after decryption. "
                     "If no path is specified, current working directory is taken.",
-                    default=os.getcwd(),
-                    alias="-o",
-                ),
-                "decrypt_only": dict(help="Skip extraction."),
+                    "default": os.getcwd(),
+                    "alias": "-o",
+                },
+                "decrypt_only": {"help": "Skip extraction."},
                 "dry_run": dry_run_override,
                 "passphrase": passphrase_override,
             },
         ),
         SubcommandGroup(
             "config",
             decorate(
                 config_to_dict, rename("show"), return_to_stdout, partial(config=config)
             ),
             create_config,
             help="Commands related to config file",
         ),
         Subcommand(
             decorate(verify_keylengths_and_upload_keys, partial(config=config)),
-            overrides={"fingerprints": dict(help="Fingerprints to upload")},
+            overrides={"fingerprints": {"help": "Fingerprints to upload"}},
         ),
     )
 
 
 # F is used as generic type for functions (Callable).
 F = TypeVar("F", bound=Callable[..., Any])
```

### Comparing `sett-4.1.0/sett/cli/cli_builder.py` & `sett-4.2.0/sett/cli/cli_builder.py`

 * *Files 1% similar despite different names*

```diff
@@ -345,15 +345,15 @@
         p_overrides = overrides.get(p_name, {})
         arg_names = make_arg_names(
             p_overrides.get("name", kebab_case(p_name) if not positional else p_name),
             p_overrides.get("alias", ()),
             positional,
         )
         default = p_overrides.get("default", p.default)
-        args = dict(help=p_overrides.get("help"))
+        args = {"help": p_overrides.get("help")}
         t = p_overrides.get("type", p.annotation)
         if t is inspect.Signature.empty:
             raise ValueError(f"Argument {arg_names[0]} has no type hint")
         try:
             t = unwrap_opt(t, default)
         except ValueError as e:
             raise ValueError(f"{f.__name__}: {p_name}: {e}") from None
```

### Comparing `sett-4.1.0/sett/cli/progress.py` & `sett-4.2.0/sett/cli/progress.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/archive.py` & `sett-4.2.0/sett/core/archive.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/checksum.py` & `sett-4.2.0/sett/core/checksum.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/crypt.py` & `sett-4.2.0/sett/core/crypt.py`

 * *Files 3% similar despite different names*

```diff
@@ -306,16 +306,16 @@
 
 
 def encrypt_and_sign(
     source: gpg.cmd.ISource,
     output: gpg.cmd.OSource,
     gpg_store: GPGStore,
     recipients_fingerprint: List[str],
-    signature_fingerprint: Optional[str] = None,
-    passphrase: Optional[Secret[str]] = None,
+    signature_fingerprint: str,
+    passphrase: Secret[str],
     always_trust: bool = True,
 ) -> None:
     """Encrypt input data with a PGP public key and sign it with a private key.
 
     In this function, the compression level of the "encrypt()" method is set
     to 0 as we are only encrypting data that has already been compressed, or
     has explicitly been requested by the user not to be compressed.
@@ -324,40 +324,46 @@
     is assumed that this is already done earlier.
 
     :param source: callable writing data to encrypt.
     :param output: callable reading encrypted data.
     :param gpg_store: directory containing GnuPG keyrings as gnupg object.
     :param recipients_fingerprint: fingerprint of public key(s) with which
         the data should be encrypted.
-    :param signature_fingerprint: fingerprint of private key with which the
-        data should be signed. If the parameter value is set to None the
-        encrypted file is not signed.
-    :param passphrase: password associated to 'signature_fingerprint'. This
-        parameter value can be set to None if the encrypted file should not be
-        signed.
+    :param signature_fingerprint: fingerprint of private PGP key with which to
+        sign the data.
+    :param passphrase: password of private PGP key. Needed to sign the data.
     :param always_trust: if False, the encryption key must be signed by the
         local user.
     :raises UserError:
     """
     try:
         # Note: gpg.CompressAlgo.NONE evaluates to "uncompressed", which
         # tells GnuPG to not compress the input data.
         gpg_store.encrypt(
             source=source,
             recipients=recipients_fingerprint,
             output=output,
+            sign=signature_fingerprint,
             passphrase=reveal(passphrase),
             trust_model=gpg.TrustModel.always if always_trust else gpg.TrustModel.pgp,
-            sign=signature_fingerprint,
             compress_algo=gpg.CompressAlgo.NONE,
         )
-    except gpg.GPGError:
-        raise UserError(
-            "Encryption failed. Maybe you entered a wrong passphrase."
-        ) from None
+    except gpg.GPGError as e:
+        # Note: this function is only called from the encryption workflow after
+        # checking that the password of the sender's key is correct.
+        # As a result, the GPG error should never be triggered by a wrong password.
+        msg = ["Encryption failed."]
+        if not always_trust:
+            msg.append(
+                "If the recipient key is not 'Trusted', you need to either "
+                "sign it with an external tool (e.g. GnuPG) or enable "
+                "'Always trust recipient key' in the settings."
+            )
+        msg.append(f"Original error: {e}")
+        raise UserError(" ".join(msg)) from e
 
 
 def get_recipient_email(key: gpg.Key) -> str:
     """Retrieve the email address associated with a PGP key, and generate a
     an error if the email address is missing or could not be retrieved.
     """
     try:
@@ -380,17 +386,15 @@
     passphrase: Optional[Secret[str]],
 ) -> List[str]:
     """Decrypt data.
 
     :param source: data to decrypt.
     :param output: file where the decrypted data should be written to.
     :param gpg_store: directory containing GnuPG keyrings as gnupg object.
-    :param passphrase: password associated to 'signature_fingerprint'. This
-        parameter value can be set to None if the encrypted file should not be
-        signed.
+    :param passphrase: password of the PGP decryption key (recipient key).
     :return: fingerprint or keyid of the signee's key.
     :raises UserError: if the data could not be decrypted.
     """
     try:
         if isinstance(output, str):
             with open(output, "wb") as output_file:
                 sender_fingerprints = gpg_store.decrypt(
```

### Comparing `sett-4.1.0/sett/core/filesystem.py` & `sett-4.2.0/sett/core/filesystem.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/metadata.py` & `sett-4.2.0/sett/core/metadata.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/request.py` & `sett-4.2.0/sett/core/request.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/secret.py` & `sett-4.2.0/sett/core/secret.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/core/versioncheck.py` & `sett-4.2.0/sett/core/versioncheck.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,31 +12,28 @@
     latest = get_latest_version(repo_url)
     if (
         not __version__.startswith("0.0.0.dev")
         and __version__ != latest
         and latest is not None
     ):
         line_break = "\n"
-        update_doc_url = (
-            f"{URL_READTHEDOCS}/en/stable/" "sett_installation.html#updating-sett"
-        )
+        update_doc_url = f"{URL_READTHEDOCS}/installation.html#updating-sett"
         if gui_formatting:
             line_break = "<br>"
-            update_doc_url = f"<a href='{update_doc_url}'>{update_doc_url}</a>"
+            update_doc_url = f"<a href='{update_doc_url}'>here</a>"
         warnings.warn(
             f"Your {APP_NAME_SHORT} version ({__version__}) is "
             f"outdated and no longer supported.{line_break}"
             f"Please upgrade to the latest version ({latest}) as "
             f"soon as possible.{line_break * 2}"
             f"In most cases, {APP_NAME_SHORT} can be upgraded with "
-            f"the following commmand:{line_break}"
+            f"the following command:{line_break}"
             f"pip install --upgrade --user sett{line_break * 2}"
             f"Documentation on how to upgrade your {APP_NAME_SHORT} "
-            f"installation can also be found at:{line_break}"
-            f"{update_doc_url}{line_break}"
+            f"installation can also be found {update_doc_url}.{line_break}"
         )
 
 
 def get_latest_version(repo_url: str) -> Optional[str]:
     try:
         url = repo_url + "/simple/" + __project_name__ + "/"
         with urlopen(url) as response:
@@ -50,11 +47,11 @@
             "Could not connect to pypi repository to query the latest version. "
             "You might have an outdated version. Please check yourself!"
         )
         return None
     except IndexError:
         warnings.warn(
             "No releases found on the pypi repository! "
-            "Please contact the developers!"
+            "Please contact the developers."
         )
         return None
     return ".".join(map(str, version))
```

### Comparing `sett-4.1.0/sett/gui/__main__.py` & `sett-4.2.0/sett/gui/__main__.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/component.py` & `sett-4.2.0/sett/gui/component.py`

 * *Files 8% similar despite different names*

```diff
@@ -82,15 +82,15 @@
     at least, one selected row.
     """
 
     def __init__(self, label: str, selection_model: QtCore.QItemSelectionModel):
         super().__init__(label)
         self.setEnabled(False)
         self._selection_model = selection_model
-        selection_model.selectionChanged.connect(self.selection_changed)  # type: ignore
+        selection_model.selectionChanged.connect(self.selection_changed)
 
     def selection_changed(self) -> None:
         # Following works better than using 'QItemSelection', especially in
         # cases where multiple selection is possible
         self.setEnabled(bool(len(self._selection_model.selectedRows())))
 
 
@@ -102,15 +102,15 @@
     """
 
     def __init__(self, *args: Any, selection_model: QtCore.QItemSelectionModel):
         super().__init__(*args)
         self.setEnabled(False)
         self._selection_enabled = True
         self._selection_model = selection_model
-        self._selection_model.selectionChanged.connect(self.selection_changed)  # type: ignore
+        self._selection_model.selectionChanged.connect(self.selection_changed)
 
     def enable_selection(self, enabled: bool) -> None:
         self._selection_enabled = enabled
         self.selection_changed()
 
     def selection_changed(self) -> None:
         # Following works better than using 'QItemSelection', especially in
@@ -143,15 +143,15 @@
 class ConsoleWidget(QtWidgets.QGroupBox, IconRepainterWidget):
     def __init__(self, title: str, parent: QtWidgets.QWidget):
         super().__init__(title, parent)
         self.textbox = QtWidgets.QTextEdit()
         self.textbox.setReadOnly(True)
         btn_clear_console = PushButton(":icon/feather/slash.png", "", self)
         btn_clear_console.setToolTip("Clear console")
-        btn_clear_console.clicked.connect(self.clear)  # type: ignore
+        btn_clear_console.clicked.connect(self.clear)
         layout = QtWidgets.QHBoxLayout(self)
         layout.addWidget(self.textbox)
         layout.addWidget(btn_clear_console, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
 
     def clear(self) -> None:
         self.textbox.clear()
 
@@ -175,26 +175,26 @@
         self.parent = parent
         self.text = LineEdit(parent)
         self.text.setReadOnly(True)
         self.btn = PushButton(
             f":icon/feather/{'folder' if directory else 'file'}.png", "", parent
         )
         self.btn.setToolTip("Change location")
-        self.btn.clicked.connect(partial(self._update_location, directory))  # type: ignore
+        self.btn.clicked.connect(partial(self._update_location, directory))
         if btn_clear:
             # Add additional button to allow clearing the selected path.
             self.btn_clear = PushButton(":icon/feather/slash.png", "", parent)
             self.btn_clear.setToolTip("Clear location")
-            self.btn_clear.clicked.connect(self._clear_location)  # type: ignore
+            self.btn_clear.clicked.connect(self._clear_location)
         self.update_path(path)
 
     def update_path(self, path: Optional[Path]) -> None:
         self.path = path
         self.text.setText("" if path is None else str(path))
-        self.text.editingFinished.emit()  # type: ignore
+        self.text.editingFinished.emit()
 
     def _update_location(self, directory: bool) -> None:
         if self.path and self.path.exists():
             location = self.path if self.path.is_dir() else self.path.parent
         else:
             location = Path.home()
         if directory:
@@ -214,15 +214,15 @@
         self.update_path(None)
 
     def setStatusTip(self, msg: str) -> None:
         self.text.setStatusTip(msg)
 
     def on_path_change(self, fn: Callable[[Optional[Path]], None]) -> None:
         """Run callback when path changes."""
-        self.text.editingFinished.connect(lambda: fn(self.path))  # type: ignore
+        self.text.editingFinished.connect(lambda: fn(self.path))
 
 
 class BaseTab(IconRepainterWidget):
     """Adds two boxes to the layout of a QWidget (a Tab from the application):
     - Box with buttons to run and test run a workflow.
     - Box with a console.
     """
@@ -251,23 +251,23 @@
         # pylint:disable=attribute-defined-outside-init
         self.run_panel = QtWidgets.QGroupBox(panel_name)
         # pylint:disable=attribute-defined-outside-init
         self.btn_test = BaseTab._create_disabled_button("Test")
 
         # On pressed button, make sure that the focus switches to that
         # button (Mac specific issue)
-        self.btn_test.pressed.connect(self.btn_test.setFocus)  # type: ignore
-        self.btn_test.clicked.connect(partial(action, dry_run=True))  # type: ignore
+        self.btn_test.pressed.connect(self.btn_test.setFocus)
+        self.btn_test.clicked.connect(partial(action, dry_run=True))
         # pylint:disable=attribute-defined-outside-init
         self.btn_run = BaseTab._create_disabled_button(action_name)
 
         # On pressed button, make sure that the focus switches to that
         # button (Mac specific issue)
-        self.btn_run.pressed.connect(self.btn_run.setFocus)  # type: ignore
-        self.btn_run.clicked.connect(action)  # type: ignore
+        self.btn_run.pressed.connect(self.btn_run.setFocus)
+        self.btn_run.clicked.connect(action)
         hbox_layout(self.btn_test, self.btn_run, parent=self.run_panel)
 
     def run_workflow_thread(
         self,
         f: Callable[..., Any],
         signals: Optional[Dict[str, Callable[..., Any]]] = None,
         **kwargs: Any,
@@ -288,18 +288,18 @@
     dialog = QtWidgets.QDialog(parent)
     dialog.setWindowTitle(APP_NAME_SHORT)
     buttons = QtWidgets.QDialogButtonBox(
         QtWidgets.QDialogButtonBox.StandardButton.Cancel
     )
     ok_btn = buttons.addButton(QtWidgets.QDialogButtonBox.StandardButton.Ok)
     ok_btn.setEnabled(False)
-    buttons.accepted.connect(dialog.accept)  # type: ignore
-    buttons.rejected.connect(dialog.reject)  # type: ignore
+    buttons.accepted.connect(dialog.accept)
+    buttons.rejected.connect(dialog.reject)
     user_input = LineEdit()
-    user_input.textChanged.connect(lambda t: ok_btn.setEnabled(bool(t)))  # type: ignore
+    user_input.textChanged.connect(lambda t: ok_btn.setEnabled(bool(t)))
     if password:
         user_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
     vbox_layout(QtWidgets.QLabel(msg), user_input, buttons, parent=dialog)
     if open_window(dialog) != QtWidgets.QDialog.DialogCode.Accepted:
         return None
     return user_input.text()
 
@@ -363,17 +363,17 @@
         slider.setStatusTip(status_tip)
     if show_ticks:
         slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
 
     def update_text(value: int) -> None:
         widget_value.setText(str(value))
 
-    slider.valueChanged.connect(update_text)  # type: ignore
+    slider.valueChanged.connect(update_text)
     if on_change is not None:
-        slider.valueChanged.connect(on_change)  # type: ignore
+        slider.valueChanged.connect(on_change)
 
     return slider, widget_value
 
 
 WIDGET_OR_LAYOUT = Union[QtWidgets.QWidget, QtWidgets.QBoxLayout]
 
 
@@ -400,15 +400,15 @@
         layout.addLayout
         if isinstance(child, (QtWidgets.QVBoxLayout, QtWidgets.QHBoxLayout))
         else layout.addWidget
     )
 
 
 def grid_layout(
-    *widgets: Sequence[Union[QtWidgets.QWidget, GridLayoutCell, None]],
+    *widgets: Sequence[Union[WIDGET_OR_LAYOUT, GridLayoutCell, None]],
     parent: Optional[QtWidgets.QWidget] = None,
     min_col_width: Optional[Sequence[int]] = None,
 ) -> QtWidgets.QGridLayout:
     parent_args = () if parent is None else (parent,)
     layout = QtWidgets.QGridLayout(*parent_args)
     if min_col_width is not None:
         layout.setColumnMinimumWidth(*min_col_width)
```

### Comparing `sett-4.1.0/sett/gui/decrypt_tab.py` & `sett-4.2.0/sett/gui/decrypt_tab.py`

 * *Files 10% similar despite different names*

```diff
@@ -37,26 +37,26 @@
         )
 
     def _enable_buttons(self) -> None:
         self.set_buttons_enabled(len(self.app_data.decrypt_files) > 0)
 
     def create_files_panel(self) -> QtWidgets.QGroupBox:
         box = ArchiveOnlyFileSelectionWidget(title="Files to decrypt", parent=self)
-        box.file_list_model.layoutChanged.connect(  # type: ignore
+        box.file_list_model.layoutChanged.connect(
             lambda: setattr(self.app_data, "decrypt_files", box.get_list())
         )
         return box
 
     def create_decrypt_options_panel(self) -> QtWidgets.QGroupBox:
         box = QtWidgets.QGroupBox("Output")
 
         decompress = QtWidgets.QCheckBox("Decompress", box)
         decompress.setStatusTip("Decompress data after decryption")
         decompress.setChecked(not self.app_data.decrypt_decrypt_only)
-        decompress.stateChanged.connect(  # type: ignore
+        decompress.stateChanged.connect(
             lambda state: setattr(
                 self.app_data,
                 "decrypt_decrypt_only",
                 QtCore.Qt.CheckState(state) == QtCore.Qt.CheckState.Unchecked,
             )
         )
 
@@ -79,20 +79,20 @@
             pw = get_pass_input(self, "Enter password for your GPG key")
             if pw is None:
                 return
         else:
             pw = None
         self.run_workflow_thread(
             decrypt.decrypt,
-            f_kwargs=dict(
-                files=self.app_data.decrypt_files,
-                output_dir=str(self.app_data.decrypt_output_location),
-                config=self.app_data.config,
-                decrypt_only=self.app_data.decrypt_decrypt_only,
-                passphrase=pw,
-                dry_run=dry_run,
-                progress=GuiProgress(self.progress_bar.setValue),
-            ),
+            f_kwargs={
+                "files": self.app_data.decrypt_files,
+                "output_dir": str(self.app_data.decrypt_output_location),
+                "config": self.app_data.config,
+                "decrypt_only": self.app_data.decrypt_decrypt_only,
+                "passphrase": pw,
+                "dry_run": dry_run,
+                "progress": GuiProgress(self.progress_bar.setValue),
+            },
             capture_loggers=(decrypt.logger,),
             ignore_exceptions=True,
             report_config=self.app_data.config,
         )
```

### Comparing `sett-4.1.0/sett/gui/encrypt_tab.py` & `sett-4.2.0/sett/gui/encrypt_tab.py`

 * *Files 16% similar despite different names*

```diff
@@ -84,15 +84,15 @@
                 self.app_data.encrypt_transfer_id is None
                 or self.app_data.encrypt_purpose is not None
             )
         )
 
     def create_files_panel(self) -> QtWidgets.QGroupBox:
         box = DirectoryAndFileSelectionWidget(title="Data to encrypt", parent=self)
-        box.file_list_model.layoutChanged.connect(  # type: ignore
+        box.file_list_model.layoutChanged.connect(
             lambda: setattr(self.app_data, "encrypt_files", box.get_list())
         )
         return box
 
     def create_user_panel(self) -> QtWidgets.QGroupBox:
         group_box = QtWidgets.QGroupBox("Data sender and recipients")
         sender_widget = QtWidgets.QComboBox()
@@ -157,18 +157,18 @@
         def remove_recipient() -> None:
             recipients_output_view.model().removeRows(
                 recipients_output_view.currentIndex().row(), 1
             )
             recipients_output_view.clearSelection()
 
         # Connect actions.
-        recipients_btn_add.clicked.connect(add_recipient)  # type: ignore
-        recipients_btn_remove.clicked.connect(remove_recipient)  # type: ignore
-        recipients_output_model.dataChanged.connect(update_recipients)  # type: ignore
-        sender_widget.currentIndexChanged.connect(update_sender)  # type: ignore
+        recipients_btn_add.clicked.connect(add_recipient)
+        recipients_btn_remove.clicked.connect(remove_recipient)
+        recipients_output_model.dataChanged.connect(update_recipients)
+        sender_widget.currentIndexChanged.connect(update_sender)
         # Set the default value for the sender
         update_sender(sender_widget.currentIndex())
         grid_layout(
             (
                 GridLayoutCell(
                     QtWidgets.QLabel(
                         "Select data sender and add at least one recipient:"
@@ -216,15 +216,15 @@
         )
         output_location = PathInput(
             path=self.app_data.encrypt_output_location, parent=self, btn_clear=False
         )
         output_location.setStatusTip("Destination folder for the encrypted package")
 
         # Add actions
-        output_suffix.editingFinished.connect(  # type: ignore
+        output_suffix.editingFinished.connect(
             lambda: setattr(
                 self.app_data, "encrypt_package_name_suffix", output_suffix.text()
             )
         )
         output_location.on_path_change(
             partial(setattr, self.app_data, "encrypt_output_location")
         )
@@ -245,15 +245,15 @@
         )
         ignore_disk_space_error.setStatusTip(
             "Write to disk, even if there is less space available than the input data occupies."
         )
         ignore_disk_space_error.setChecked(
             self.app_data.encrypt_ignore_disk_space_error
         )
-        ignore_disk_space_error.stateChanged.connect(  # type: ignore
+        ignore_disk_space_error.stateChanged.connect(
             lambda state: setattr(
                 self.app_data,
                 "encrypt_ignore_disk_space_error",
                 QtCore.Qt.CheckState(state) == QtCore.Qt.CheckState.Checked,
             )
         )
         grid_layout(
@@ -298,58 +298,62 @@
             if text:
                 self.app_data.encrypt_transfer_id = int(text)
                 purpose_label.setText(f"Purpose{required_suffix}")
             else:
                 self.app_data.encrypt_transfer_id = None
                 purpose_label.setText("Purpose")
 
-        transfer_id.textChanged.connect(on_transfer_id_changed)  # type: ignore
-        purpose.currentTextChanged.connect(  # type: ignore
+        transfer_id.textChanged.connect(on_transfer_id_changed)
+        purpose.currentTextChanged.connect(
             lambda text: setattr(
                 self.app_data, "encrypt_purpose", None if text == "" else Purpose(text)
             )
         )
         grid_layout(
             (transfer_id_label, transfer_id),
             (purpose_label, purpose),
             parent=group_box,
         )
         return group_box
 
     def encrypt(self, dry_run: bool = False) -> None:
-        if not dry_run and self.app_data.config.sign_encrypted_data:
-            pw = get_pass_input(self, "Enter password for your GPG key")
-            if pw is None:
-                return
-        else:
-            pw = None
+        """Run the encrypt workflow in a separate thread."""
 
-        def update_transfer_files(path: Optional[str]) -> None:
+        def update_files_to_transfer_in_transfer_tab(path: Optional[str]) -> None:
             if path is not None:
                 self.app_data.transfer_files.setStringList([path])
-                self.app_data.transfer_files.layoutChanged.emit()  # type: ignore
+                self.app_data.transfer_files.layoutChanged.emit()
                 self.console.append(
                     "<strong>Added the newly created package to the 'Transfer' tab.</strong>"
                 )
 
+        # Retrieve the user's PGP key password (needed to sign the data).
+        if not dry_run:
+            passphrase = get_pass_input(self, "Please enter your PGP key password")
+            if passphrase is None:
+                return
+        else:
+            passphrase = None
+
+        # Run the encrypt workflow in a separate thread.
         self.run_workflow_thread(
             encrypt_workflow,
-            f_kwargs=dict(
-                files=self.app_data.encrypt_files,
-                capture_loggers=(encrypt.logger,),
-                sender=self.app_data.encrypt_sender,
-                recipient=self.app_data.encrypt_recipients,
-                dtr_id=self.app_data.encrypt_transfer_id,
-                config=self.app_data.config,
-                passphrase=pw,
-                output=self.app_data.encrypt_output_location,
-                output_suffix=self.app_data.encrypt_package_name_suffix,
-                dry_run=dry_run,
-                compression_level=self.app_data.encrypt_compression_level,
-                purpose=self.app_data.encrypt_purpose,
-                progress=GuiProgress(self.progress_bar.setValue),
-            ),
-            signals={"result": update_transfer_files},
+            f_kwargs={
+                "files": self.app_data.encrypt_files,
+                "capture_loggers": (encrypt.logger,),
+                "sender": self.app_data.encrypt_sender,
+                "recipient": self.app_data.encrypt_recipients,
+                "dtr_id": self.app_data.encrypt_transfer_id,
+                "config": self.app_data.config,
+                "passphrase": passphrase,
+                "output": self.app_data.encrypt_output_location,
+                "output_suffix": self.app_data.encrypt_package_name_suffix,
+                "dry_run": dry_run,
+                "compression_level": self.app_data.encrypt_compression_level,
+                "purpose": self.app_data.encrypt_purpose,
+                "progress": GuiProgress(self.progress_bar.setValue),
+            },
+            signals={"result": update_files_to_transfer_in_transfer_tab},
             ignore_exceptions=True,
             report_config=self.app_data.config,
             force=self.app_data.encrypt_ignore_disk_space_error,
         )
```

### Comparing `sett-4.1.0/sett/gui/file_selection_widget.py` & `sett-4.2.0/sett/gui/file_selection_widget.py`

 * *Files 3% similar despite different names*

```diff
@@ -71,51 +71,51 @@
             self._create_add_files_action(),
             self._create_remove_selected_action(),
             self._create_clear_list_action(),
         ]
 
     def _create_add_files_action(self) -> QAction:
         action = Action(":icon/feather/file-plus.png", "Add file", self)
-        action.triggered.connect(self._add_files)  # type: ignore
+        action.triggered.connect(self._add_files)
         return action
 
     def _create_remove_selected_action(self) -> QAction:
         def clear_selected() -> None:
             for index in self.file_list_view.selectedIndexes():
                 self.file_list_model.removeRows(index.row(), 1)
-            self.file_list_model.layoutChanged.emit()  # type: ignore
+            self.file_list_model.layoutChanged.emit()
 
         action = SelectionAction(
             ":icon/feather/file-minus.png",
             "Remove selected",
             self,
             selection_model=self.file_list_view.selectionModel(),
         )
-        action.triggered.connect(clear_selected)  # type: ignore
+        action.triggered.connect(clear_selected)
         return action
 
     def _create_clear_list_action(self) -> QAction:
         def clear_list() -> None:
             # Clear the selection BEFORE resetting the model
             self.file_list_view.selectionModel().clearSelection()
             self.file_list_model.setStringList([])
-            self.file_list_model.layoutChanged.emit()  # type: ignore
+            self.file_list_model.layoutChanged.emit()
 
         action = Action(":icon/feather/trash-2.png", "Clear list", self)
-        action.triggered.connect(clear_list)  # type: ignore
+        action.triggered.connect(clear_list)
         return action
 
     def _update_paths(self, paths: Iterable[str]) -> None:
         paths = set(filter(None, paths))
         if paths:
             self.path = str(Path(next(iter(paths))).parent)
         self.file_list_model.setStringList(
             sorted(set(self.file_list_model.stringList()) | paths)
         )
-        self.file_list_model.layoutChanged.emit()  # type: ignore
+        self.file_list_model.layoutChanged.emit()
 
     def _add_files(self) -> None:
         dialog = QtWidgets.QFileDialog(self)
         dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
         dialog.setDirectory(str(self.path))
         if self.name_filter:
             dialog.setNameFilter(self.name_filter)
@@ -147,15 +147,15 @@
         def add_directory() -> None:
             directory = QtWidgets.QFileDialog.getExistingDirectory(
                 self, "Select directory", str(self.path)
             )
             self._update_paths((directory,))
 
         action = Action(":icon/feather/folder-plus.png", "Add directory", self)
-        action.triggered.connect(add_directory)  # type: ignore
+        action.triggered.connect(add_directory)
         return action
 
 
 class ArchiveOnlyFileSelectionWidget(FileSelectionWidget):
     """File selection widget extension for selecting ZIP and TAR archives only."""
 
     def __init__(
```

### Comparing `sett-4.1.0/sett/gui/key_generation_dialog.py` & `sett-4.2.0/sett/gui/key_generation_dialog.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from libbiomedit.lib.secret import Secret
 
+from sett import URL_READTHEDOCS
 from .model import AppData, ConfigProxy
 from ..core import gpg, crypt
 from ..core.error import UserError
 from .component import (
     LineEdit,
     grid_layout,
     GridLayoutCell,
@@ -33,20 +34,20 @@
         self.toggle_password_visibility(False)
 
         re_email = QtCore.QRegularExpression(r"[^@]+@[^@]+\.[^@]+")
         self.text_email.setValidator(QtGui.QRegularExpressionValidator(re_email))
 
         self.btn_run = QtWidgets.QPushButton("Generate key")
         self.btn_run.setDefault(True)
-        self.btn_run.clicked.connect(self.create_private_key)  # type: ignore
+        self.btn_run.clicked.connect(self.create_private_key)
         btn_cancel = QtWidgets.QPushButton("Close")
-        btn_cancel.clicked.connect(self.close)  # type: ignore
+        btn_cancel.clicked.connect(self.close)
         btn_show_pass = QtWidgets.QPushButton("Show")
         btn_show_pass.setCheckable(True)
-        btn_show_pass.clicked.connect(self.toggle_password_visibility)  # type: ignore
+        btn_show_pass.clicked.connect(self.toggle_password_visibility)
 
         self.setLayout(
             grid_layout(
                 (QtWidgets.QLabel("Full name"), self.text_name_full),
                 (
                     QtWidgets.QLabel("(optional) institution/project"),
                     self.text_name_extra,
@@ -136,26 +137,26 @@
                 self,
             )
             self.btn_run.setEnabled(True)
             return
 
         run_thread(
             crypt.create_key,
-            f_kwargs=dict(
-                full_name=name_full,
-                email=self.text_email.text(),
-                pwd=Secret(self.text_pass.text()),
-                gpg_store=self.config.gpg_store,
-            ),
+            f_kwargs={
+                "full_name": name_full,
+                "email": self.text_email.text(),
+                "pwd": Secret(self.text_pass.text()),
+                "gpg_store": self.config.gpg_store,
+            },
             forward_errors=warning_callback("GPG Key Generation Error"),
             report_config=self.config,
-            signals=dict(
-                result=self.post_key_creation,
-                finished=lambda: self.btn_run.setEnabled(True),
-            ),
+            signals={
+                "result": self.post_key_creation,
+                "finished": lambda: self.btn_run.setEnabled(True),
+            },
         )
 
 
 def click_show_details(msgbox: QtWidgets.QMessageBox) -> None:
     for button in msgbox.buttons():
         if msgbox.buttonRole(button) is QtWidgets.QMessageBox.ButtonRole.ActionRole:
             button.click()
@@ -166,18 +167,18 @@
 Upload your public key to the keyserver by selecting it in the Public keys list and clicking on the upload button.
 
 To get your key approved, please [connect to the portal]({0}/keys).
 
 """
 
 revocation_cert_creation_successful_text = (
-    post_key_creation_text
-    + """Additionally, a [revocation certificate](https://sett.rtfd.io/en/stable/key_management.html?#revocation-certificates)
-has been issued. Please store the revocation certificate below in a safe location.
-"""
+    post_key_creation_text + "Additionally, a "
+    f"[revocation certificate]({URL_READTHEDOCS}/key_management.html#revocation-certificates) "
+    "has been issued. Please store the revocation certificate below in a safe "
+    "location."
 )
 
 revocation_cert_creation_failed_text = (
     post_key_creation_text
     + """However, it was not possible to create a revocation certificate for it.
 Please execute the following command to create the certificate:
 ```
```

### Comparing `sett-4.1.0/sett/gui/keys_download_dialog.py` & `sett-4.2.0/sett/gui/keys_download_dialog.py`

 * *Files 6% similar despite different names*

```diff
@@ -15,25 +15,25 @@
         self.setWindowTitle("Download public keys from keyserver")
         self.setWindowFlags(
             self.windowFlags() & ~QtCore.Qt.WindowType.WindowContextHelpButtonHint
         )
 
         self.key_identifier = LineEdit()
         self.btn_download = QtWidgets.QPushButton("Download")
-        self.btn_download.clicked.connect(self.download)  # type: ignore
+        self.btn_download.clicked.connect(self.download)
         self.btn_download.setEnabled(False)
 
-        self.key_identifier.textChanged.connect(  # type: ignore
+        self.key_identifier.textChanged.connect(
             lambda text: self.btn_download.setEnabled(bool(text))
         )
 
         btn_box = QtWidgets.QDialogButtonBox(
             QtWidgets.QDialogButtonBox.StandardButton.Close
         )
-        btn_box.rejected.connect(self.reject)  # type: ignore
+        btn_box.rejected.connect(self.reject)
 
         self.setLayout(
             grid_layout(
                 (
                     QtWidgets.QLabel(
                         "Enter an identifier (fingerprint, key ID or email)"
                     ),
@@ -76,18 +76,18 @@
                 pass
             self.btn_download.setEnabled(True)
             self.close()
 
         self.btn_download.setEnabled(False)
         run_thread(
             crypt.download_keys,
-            f_kwargs=dict(
-                key_identifiers=[self.key_identifier.text()],
-                keyserver=self.config.keyserver_url,
-                gpg_store=self.config.gpg_store,
-            ),
+            f_kwargs={
+                "key_identifiers": [self.key_identifier.text()],
+                "keyserver": self.config.keyserver_url,
+                "gpg_store": self.config.gpg_store,
+            },
             report_config=self.config,
             forward_errors=warning_callback("GPG key search error"),
-            signals=dict(
-                result=on_result,
-            ),
+            signals={
+                "result": on_result,
+            },
         )
```

### Comparing `sett-4.1.0/sett/gui/keys_tab.py` & `sett-4.2.0/sett/gui/keys_tab.py`

 * *Files 2% similar despite different names*

```diff
@@ -72,40 +72,40 @@
         self.app_data = app_data
 
         self.text_panel = QtWidgets.QTextEdit()
         self.text_panel.setReadOnly(True)
 
         self.priv_keys_view = QtWidgets.QListView()
         self.priv_keys_view.setModel(self.app_data.priv_keys_model)
-        self.priv_keys_view.selectionModel().currentChanged.connect(  # type: ignore
+        self.priv_keys_view.selectionModel().currentChanged.connect(
             self._update_display
         )
 
         self.pub_keys_view = QtWidgets.QListView()
         self.pub_keys_view.setModel(self.app_data.pub_keys_model)
-        self.pub_keys_view.selectionModel().currentChanged.connect(self._update_display)  # type: ignore
+        self.pub_keys_view.selectionModel().currentChanged.connect(self._update_display)
         self.pub_keys_view.setSelectionMode(
             QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection
         )
 
         # When item is selected in the public/private key list, clear
         # the selection in the other list.
-        self.priv_keys_view.selectionModel().currentChanged.connect(  # type: ignore
+        self.priv_keys_view.selectionModel().currentChanged.connect(
             lambda: self.pub_keys_view.selectionModel().clear()
         )
-        self.pub_keys_view.selectionModel().currentChanged.connect(  # type: ignore
+        self.pub_keys_view.selectionModel().currentChanged.connect(
             lambda: self.priv_keys_view.selectionModel().clear()
         )
 
         action_generate_key = Action(
             ":icon/feather/plus-square.png",
             "Generate new private/public key",
             self,
         )
-        action_generate_key.triggered.connect(  # type: ignore
+        action_generate_key.triggered.connect(
             lambda: KeyGenDialog(parent=self, app_data=app_data).show()
         )
         action_refresh_keys = Action(
             ":icon/feather/refresh-cw.png",
             "Refresh keys from the local keyring",
             self,
         )
@@ -120,18 +120,18 @@
                 f_kwargs={},
                 report_config=self.app_data.config,
                 forward_errors=warning_callback(
                     title="Key approval status retrieval failure",
                     msg_prefix="Approval status of PGP keys could not be "
                     f"retrieved from \n'{self.app_data.config.dcc_portal_url}'.",
                 ),
-                signals=dict(result=self.update_display_selected_pub_key),
+                signals={"result": self.update_display_selected_pub_key},
             )
 
-        action_refresh_keys.triggered.connect(refresh_keys)  # type: ignore
+        action_refresh_keys.triggered.connect(refresh_keys)
 
         toolbar = ToolBar("Key management", self)
         toolbar.addAction(action_generate_key)
         toolbar.addSeparator()
         for action in self.create_public_keys_actions():
             toolbar.addAction(action)
         toolbar.addSeparator()
@@ -256,15 +256,15 @@
                     "Import key from file",
                     self,
                 ),
                 self.import_key,
             ),
         )
         for action, fn in functions_by_action:
-            action.triggered.connect(fn)  # type: ignore
+            action.triggered.connect(fn)
             yield action
 
     def get_selected_keys(self) -> Tuple[gpg.Key, ...]:
         """Returns the gpg.Key objects corresponding to the keys currently
         selected in the GUI.
         """
         # Note: it's probably possible to get rid of the cast() here.
@@ -286,22 +286,22 @@
                     "Keys have been successfully updated.",
                     title="Updated PGP keys",
                     parent=self.parentWidget(),
                 )
 
             run_thread(
                 crypt.download_keys,
-                f_kwargs=dict(
-                    key_identifiers=[key.fingerprint for key in keys_to_update],
-                    keyserver=self.app_data.config.keyserver_url,
-                    gpg_store=self.app_data.config.gpg_store,
-                ),
+                f_kwargs={
+                    "key_identifiers": [key.fingerprint for key in keys_to_update],
+                    "keyserver": self.app_data.config.keyserver_url,
+                    "gpg_store": self.app_data.config.gpg_store,
+                },
                 report_config=self.app_data.config,
                 forward_errors=warning_callback("GPG key update error"),
-                signals=dict(result=on_result),
+                signals={"result": on_result},
             )
 
     def import_key(self) -> None:
         """Import a PGP key from a local file."""
         path = QtWidgets.QFileDialog.getOpenFileName(
             self, "Select PGP key file", str(Path.home())
         )[0]
@@ -401,29 +401,29 @@
             for key in keys_to_upload:
                 if (
                     verify_key_length(self.parentWidget(), key)
                     == QtWidgets.QMessageBox.StandardButton.Ok
                 ):
                     run_thread(
                         upload_keys_workflow.upload_keys,
-                        f_kwargs=dict(
-                            fingerprints=[key.fingerprint],
-                            verify_key=cb.isChecked(),
-                            config=self.app_data.config,
-                        ),
+                        f_kwargs={
+                            "fingerprints": [key.fingerprint],
+                            "verify_key": cb.isChecked(),
+                            "config": self.app_data.config,
+                        },
                         capture_loggers=(upload_keys_workflow.logger,),
                         report_config=self.app_data.config,
                         forward_errors=warning_callback("GPG key upload error"),
-                        signals=dict(
-                            result=lambda _: open_info_msgbox(
+                        signals={
+                            "result": lambda _: open_info_msgbox(
                                 "Key has been successfully uploaded to keyserver.",
                                 title="Sent PGP keys",
                                 parent=self.parentWidget(),
                             )
-                        ),
+                        },
                     )
 
     def _update_display(self, index: QtCore.QModelIndex) -> None:
         """Display key info summary in GUI text panel."""
         style = (
             "<style>"
             "th {text-align: left; padding: 0 20px 5px 0;}"
```

### Comparing `sett-4.1.0/sett/gui/listener.py` & `sett-4.2.0/sett/gui/listener.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/main_window.py` & `sett-4.2.0/sett/gui/main_window.py`

 * *Files 4% similar despite different names*

```diff
@@ -93,50 +93,51 @@
         self.status = QtWidgets.QStatusBar()
         self.setStatusBar(self.status)
 
     def add_menu(self) -> None:
         action_exit = Action(":icon/feather/log-out.png", "&Exit", self)
         action_exit.setShortcut(QtGui.QKeySequence("Ctrl+Q"))
         action_exit.setStatusTip("Exit application")
-        action_exit.triggered.connect(self.close)  # type: ignore
+        action_exit.triggered.connect(self.close)
 
         menu = self.menuBar()
         menu.setNativeMenuBar(not is_macos())
         menu_file = menu.addMenu("&File")
         menu_file.addAction(action_exit)
 
         action_help = Action(":icon/feather/book-open.png", "&Documentation", self)
         action_help.setStatusTip("Open online documentation")
         action_help.setShortcut(
             QtGui.QKeySequence(QtGui.QKeySequence.StandardKey.HelpContents)
         )
-        action_help.triggered.connect(open_url(URL_READTHEDOCS))  # type: ignore
+        action_help.triggered.connect(open_url(URL_READTHEDOCS))
 
         action_bug_report = Action(
             ":icon/feather/alert-triangle.png", "&Report an Issue", self
         )
         action_bug_report.setStatusTip("Open online bug report form")
-        action_bug_report.triggered.connect(open_url(URL_GITLAB_ISSUES))  # type: ignore
+        action_bug_report.triggered.connect(open_url(URL_GITLAB_ISSUES))
 
         action_about = Action(":icon/feather/info.png", "&About", self)
         action_about.setStatusTip("Show info about application")
-        action_about.triggered.connect(self.show_about)  # type: ignore
+        action_about.triggered.connect(self.show_about)
 
         menu_help = menu.addMenu("&Help")
         menu_help.addAction(action_help)
         menu_help.addAction(action_bug_report)
         menu_help.addAction(action_about)
 
     def closeEvent(self, event: QtGui.QCloseEvent) -> None:
         """Code that is run when the application is closed by the user."""
 
         # Clear focus on the currently selected widget. This is only needed
         # for the case where a user exits the app while still having the
-        # focus on field in the Settings Tab.
-        self.focusWidget().clearFocus()
+        # focus on a field in the Settings Tab.
+        if self.focusWidget():
+            self.focusWidget().clearFocus()
 
         # Compare the current in-memory config values to those present on disk
         # (in the user's config file). If they differ, ask the user whether
         # they want to save their config value modifications to disk.
         if self.app_data.config != self.load_config_from_disk():
             msg = NormalMessageBox(self, "Persist changed settings?")
             msg.set_text_list(
@@ -183,17 +184,17 @@
                 check_version(self.app_data.config.repo_url, gui_formatting=True)
                 return "\n".join(format(warning.message) for warning in w)
 
         run_thread(
             get_warnings,
             f_kwargs={},
             report_config=self.app_data.config,
-            signals=dict(
-                result=lambda x: show_warning("Version check", x, self) if x else x
-            ),
+            signals={
+                "result": lambda x: show_warning("Version check", x, self) if x else x
+            },
         )
 
     def show_about(self) -> None:
         msg = QtWidgets.QMessageBox(parent=self)
         msg.setWindowTitle("About")
         msg.setIconPixmap(QtGui.QPixmap(":icon/biomedit_logo.png"))
         msg.setTextFormat(QtCore.Qt.TextFormat.RichText)
```

### Comparing `sett-4.1.0/sett/gui/model.py` & `sett-4.2.0/sett/gui/model.py`

 * *Files 4% similar despite different names*

```diff
@@ -51,16 +51,16 @@
         self._columns = tuple(values)
 
     def get_data(self) -> Tuple[Sequence[Any], ...]:
         return self._data
 
     def set_data(self, data: Sequence[Sequence[Any]]) -> None:
         self._data = tuple(sorted(tuple(x) for x in data))
-        self.layoutChanged.emit()  # type: ignore
-        self.dataChanged.emit(  # type: ignore
+        self.layoutChanged.emit()
+        self.dataChanged.emit(
             self.createIndex(0, 0),
             self.createIndex(self.rowCount(), self.columnCount()),
         )
 
     def rowCount(self, _parent: INDEX_UNION_TYPE = QtCore.QModelIndex()) -> int:
         return len(self._data)
 
@@ -114,15 +114,15 @@
     ):
         super().__init__(*args, **kwargs)
         self.set_data(data or [])
 
     def set_data(self, data: Iterable[Tuple[Hashable, Any]]) -> None:
         self._keyvalues = dict(data)
         self._keys = list(self._keyvalues.keys())
-        self.layoutChanged.emit()  # type: ignore
+        self.layoutChanged.emit()
 
     # Default value Qt.DisplayRole for index is not an int (upstream issue):
     def data(self, index, role) -> Optional[Hashable]:  # type: ignore
         if role == QtCore.Qt.ItemDataRole.DisplayRole:
             key: Hashable = self._keys[index.row()]
             return key
         return None
@@ -147,15 +147,22 @@
 
 
 def new_sftp_connection() -> Protocol:
     return sftp.Protocol(host="", username="", destination_dir="")
 
 
 def new_s3_connection() -> Protocol:
-    return s3.Protocol(host="", bucket="", access_key="", secret_key=Secret(""))
+    return s3.Protocol(  # nosec
+        host="",
+        secure=True,
+        bucket="",
+        access_key="",
+        secret_key=Secret(""),
+        session_token="",
+    )
 
 
 def new_liquid_files_connection() -> Protocol:
     return liquid_files.Protocol(host="", api_key=Secret(""))
 
 
 # Trick the type-checker into thinking that ConfigProxy is a Config object, so
@@ -248,18 +255,23 @@
         keys_public = self.config.gpg_store.list_pub_keys(sigs=True)
         self.pub_keys_model.set_data(data=keys_as_tuple(keys=keys_public))
 
     def update_key_approval_status(self) -> None:
         """Check whether public keys from the user's local keyring are approved
         in the portal and store/update this information in the application's
         memory.
+        If no keys are present in the user's local PGP keyring, the request to
+        the Portal's API is skipped.
         """
-        self.pub_key_status = self.config.portal_api.get_key_status(
+        fingerprints = tuple(
             k.fingerprint for k in self.config.gpg_store.list_pub_keys()
         )
+        self.pub_key_status = (
+            self.config.portal_api.get_key_status(fingerprints) if fingerprints else {}
+        )
 
     def __post_init__(self) -> None:
         super().__init__()
         if self.config.output_dir:
             self.encrypt_output_location = Path(self.config.output_dir)
             self.decrypt_output_location = Path(self.config.output_dir)
         if self.config.compression_level is not None:
```

### Comparing `sett-4.1.0/sett/gui/parallel.py` & `sett-4.2.0/sett/gui/parallel.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/pyside.py` & `sett-4.2.0/sett/gui/pyside.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/resources/rc_icons.py` & `sett-4.2.0/sett/gui/resources/rc_icons.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/settings_tab.py` & `sett-4.2.0/sett/gui/settings_tab.py`

 * *Files 2% similar despite different names*

```diff
@@ -102,18 +102,15 @@
                         ((label_field("Data encryption / decryption"),), ()),
                         (cfg_field("compression_level"), cfg_field("max_cpu")),
                         (cfg_field("verify_dtr"), cfg_field("default_sender")),
                         (
                             cfg_field("always_trust_recipient_key"),
                             cfg_field("output_dir"),
                         ),
-                        (
-                            cfg_field("sign_encrypted_data"),
-                            cfg_field("package_name_suffix"),
-                        ),
+                        ((), cfg_field("package_name_suffix")),
                         ((label_field("PGP keys"),), ()),
                         (cfg_field("gpg_key_autodownload"), cfg_field("keyserver_url")),
                         (cfg_field("verify_key_approval"), cfg_field("gpg_home_dir")),
                         ((label_field("Data transfer"),), ()),
                         (cfg_field("dcc_portal_url"), cfg_field("sftp_buffer_size")),
                         (
                             cfg_field("verify_package_name"),
@@ -139,15 +136,15 @@
         self.checkbox_gpg_key_autodownload = cast(
             QtWidgets.QCheckBox, widget_register["gpg_key_autodownload"]
         )
         self.field_keyserver_url = cast(
             QtWidgets.QLineEdit, widget_register["keyserver_url"]
         )
         self._enable_checkbox_key_autodownload()
-        self.field_keyserver_url.textChanged.connect(  # type: ignore
+        self.field_keyserver_url.textChanged.connect(
             self._enable_checkbox_key_autodownload
         )
         self.config_proxy.refresh()
         self.icon_repainter().register(self.refresh_icon)
 
     def _save_config_to_disk(self) -> None:
         """Write the current in-app config values to a config file on disk."""
@@ -164,21 +161,21 @@
             "Changes you make are applied instantly during the current session.\n"
             f"To persist changes across restarts, make sure to click the "
             f"'{self.persist_btn_text}' button at the bottom of the app."
         )
         top_label.setWordWrap(True)
         reset_btn = QtWidgets.QPushButton("Reset", self)
         reset_btn.setStatusTip("Resets to your last persisted settings")
-        reset_btn.clicked.connect(  # type: ignore
+        reset_btn.clicked.connect(
             lambda: self.config_proxy.set_config(config.load_config())
         )
 
         defaults_btn = QtWidgets.QPushButton("Restore defaults", self)
         defaults_btn.setStatusTip("Reset all settings to their default values")
-        defaults_btn.clicked.connect(  # type: ignore
+        defaults_btn.clicked.connect(
             lambda: self.config_proxy.set_config(config.default_config())
         )
         layout = QtWidgets.QGridLayout()
         layout.addWidget(top_label, 0, 0, 1, 2)
         layout.addWidget(reset_btn, 0, 2)
         layout.addWidget(defaults_btn, 0, 3)
         return layout
@@ -186,15 +183,15 @@
     def _footer(self) -> PushButton:
         self.persist_btn = PushButton(
             self.persist_btn_icon_file_name,
             f'{self.persist_btn_text} "{get_config_file()}"',
             self,
         )
         self.persist_btn.setStatusTip("Saves your current settings to the config file")
-        self.persist_btn.clicked.connect(self._save_config_to_disk)  # type: ignore
+        self.persist_btn.clicked.connect(self._save_config_to_disk)
         return self.persist_btn
 
     def _enable_checkbox_key_autodownload(self) -> None:
         self.checkbox_gpg_key_autodownload.setEnabled(
             len(self.field_keyserver_url.text().strip()) > 0
         )
 
@@ -258,20 +255,19 @@
     and if so, fill the widget with the default value of the setting that it
     holds.
     Additionally, warn the user that the setting has been reset via a pop-up.
 
     :param widget: text widget whose text is to be reset.
     """
     if not widget.text().strip():
-
         # Reset the in-memory value (AppData) and widget text to the default
         # value of the setting.
         config_key = widget.objectName()
         widget.setText(Config.get_default_value(config_key))
-        widget.editingFinished.emit()  # type: ignore
+        widget.editingFinished.emit()
 
         # Generate a pop-up that warns the user that the field has been
         # reset to its default value.
         msg = NormalMessageBox(
             parent=widget.parent(), window_title="Mandatory field warning"  # type: ignore
         )
         msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
@@ -305,25 +301,25 @@
     bind(config_proxy, config_key, widget, TextControl)
     widget.setObjectName(config_key)
 
     # If the setting is mandatory (i.e. `None` is not allowed as a value), a
     # check for resetting empty values to their default value is added to the
     # actions to perform after a field was edited by the user.
     if Config.is_mandatory_argument(config_key):
-        widget.editingFinished.connect(lambda: reset_to_default_if_empty(widget))  # type: ignore
+        widget.editingFinished.connect(lambda: reset_to_default_if_empty(widget))
 
     # Add regexp-based validation rules to the field. These rules are either
     # added via a post-edit check (i.e. when the user leaves the field, see
     # Case 1 below), or via a "Validator" (checks the value at every keystroke
     # from the user, see Case 2 below).
     # Case 1: the field uses REGEX_FQDN as validator regexp, meaning that
     #         it contains a URL (FQDN = fully qualified domain name).
     if regex == REGEX_FQDN:
         # A check for the validity of the specified domain name is added.
-        widget.editingFinished.connect(  # type: ignore
+        widget.editingFinished.connect(
             lambda: check_hostname(regex, widget, status_tip)
         )
     # Case 2: the field is not a URL, but it has some specific validation
     #         rules given as a regexp.
     elif regex is not None:
         widget.setValidator(
             QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(regex))
```

### Comparing `sett-4.1.0/sett/gui/theme.py` & `sett-4.2.0/sett/gui/theme.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/gui/transfer_tab.py` & `sett-4.2.0/sett/gui/transfer_tab.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import enum
+import json
 import time
 from functools import partial
 from typing import Iterator, Optional, Sequence
 
 from .component import (
     BaseTab,
     PathInput,
@@ -10,25 +11,28 @@
     get_text_input,
     MandatoryLabel,
     ToolBar,
     LineEdit,
     grid_layout,
     vbox_layout,
     hbox_layout,
+    GridLayoutCell,
+    NormalMessageBox,
 )
 from .file_selection_widget import ArchiveOnlyFileSelectionWidget
 from .model import new_sftp_connection, AppData
 from .pyside import QtCore, QtGui, QtWidgets, QAction, open_window
 from .theme import Action, IconRepainterWidget
 from .ui_model_bind import (
     bind,
     TextControl,
     OptionalTextControl,
     OptionalPasswordControl,
     OptionalPathControl,
+    BoolControl,
 )
 from .. import protocols
 from ..core.error import UserError
 from ..protocols.liquid_files import Protocol as LiquidFiles
 from ..protocols.s3 import Protocol as S3
 from ..protocols.sftp import Protocol as Sftp
 from ..utils.config import ConnectionStore
@@ -117,33 +121,121 @@
         )
         return box
 
     def _create_s3_options_panel(self, data: AppData) -> QtWidgets.QGroupBox:
         args = data.transfer_protocol_args[S3]
 
         text_host = LineEdit()
+        text_host.setStatusTip("Host name of the S3-compatible server.")
+        text_host.setPlaceholderText("minioserver.example.net:9000")
         bind(args, "host", text_host, TextControl)
 
+        bool_secure = QtWidgets.QCheckBox()
+        bool_secure.setStatusTip("Whether to use a secure (TLS) connection or not.")
+        bool_secure.setChecked(True)
+        bind(args, "secure", bool_secure, BoolControl)
+        secure_layout = QtWidgets.QHBoxLayout()
+        secure_layout.addWidget(QtWidgets.QLabel("Use secure TLS connection"))
+        secure_layout.addWidget(bool_secure)
+
         text_bucket = LineEdit()
+        text_bucket.setStatusTip(
+            "Location (bucket) of the S3-compatible server to which the "
+            "file(s) should be uploaded."
+        )
         bind(args, "bucket", text_bucket, TextControl)
 
         text_access_key = LineEdit()
+        text_access_key.setStatusTip(
+            "Credentials for logging-in to the S3-compatible server: user access key."
+        )
         bind(args, "access_key", text_access_key, TextControl)
 
         text_secret_key = LineEdit()
         text_secret_key.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
+        text_secret_key.setStatusTip(
+            "Credentials for logging-in to the S3-compatible server: user secret key."
+        )
+        # To make left and right panels the same width.
+        text_secret_key.setMinimumWidth(400)
         bind(args, "secret_key", text_secret_key, OptionalPasswordControl)
 
+        text_session_token = LineEdit()
+        text_session_token.setStatusTip(
+            "Credentials for logging-in to the S3-compatible server: "
+            "temporary STS (Security Token Service) token."
+        )
+        bind(args, "session_token", text_session_token, OptionalTextControl)
+
+        # Function to copy/paste s3 access credentials from the portal.
+        def read_clipboard() -> None:
+            clipboard = QtGui.QGuiApplication.clipboard()
+            try:
+                credentials_with_opts = json.loads(clipboard.text())
+                for field, key in (
+                    (text_access_key, "accessKeyId"),
+                    (text_secret_key, "secretAccessKey"),
+                    (text_session_token, "sessionToken"),
+                    (text_host, "endpoint"),
+                    (text_bucket, "bucket"),
+                ):
+                    # Make sure that the value change is really registered (important for `bind`)
+                    field.setFocus()
+                    field.setText(credentials_with_opts[key])
+                    field.clearFocus()
+            except (json.JSONDecodeError, KeyError):
+                msg = NormalMessageBox(
+                    parent=box, window_title="Paste from clipboard failure"
+                )
+                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
+                msg.setText(
+                    "This credential pasting is intended to be used with "
+                    "credentials copied from the portal.\n\n"
+                    "For the credentials pasting to work, the content of "
+                    "the clipboard must be a JSON string with the following "
+                    "format:\n\n"
+                    "{"
+                    '"accessKeyId": "value of access key ID", '
+                    '"secretAccessKey": "value of secret key", '
+                    '"sessionToken": "value of STS token", '
+                    '"endpoint": "S3 server endpoint", '
+                    '"bucket": "bucket name"'
+                    "}"
+                )
+                open_window(msg)
+
+        button = QtWidgets.QPushButton("Paste credentials from clipboard")
+        button.clicked.connect(read_clipboard)
+        button_layout = QtWidgets.QHBoxLayout()
+        button_layout.addStretch()
+        button_layout.addWidget(button)
+
         box = QtWidgets.QGroupBox()
         box.setFlat(True)
         grid_layout(
-            (MandatoryLabel("Host URL"), text_host),
-            (MandatoryLabel("Bucket"), text_bucket),
-            (MandatoryLabel("Access Key"), text_access_key),
-            (MandatoryLabel("Secret Key"), text_secret_key),
+            (
+                MandatoryLabel("Host"),
+                text_host,
+                secure_layout,
+            ),
+            (
+                MandatoryLabel("Bucket"),
+                text_bucket,
+            ),
+            (
+                MandatoryLabel("Access Key"),
+                GridLayoutCell(text_access_key, span=2),
+                MandatoryLabel("Secret Key"),
+                text_secret_key,
+            ),
+            (
+                QtWidgets.QLabel("Session Token"),
+                GridLayoutCell(text_session_token, span=4),
+            ),
+            (None, None, None, None, button_layout),
             parent=box,
         )
         return box
 
     def _create_lf_options_panel(self, data: AppData) -> QtWidgets.QGroupBox:
         args = data.transfer_protocol_args[LiquidFiles]
 
@@ -186,15 +278,15 @@
 
     def create_files_panel(self) -> QtWidgets.QGroupBox:
         box = ArchiveOnlyFileSelectionWidget(
             title="Encrypted files to transfer",
             parent=self,
             model=self.app_data.transfer_files,
         )
-        self.app_data.transfer_files.layoutChanged.connect(  # type: ignore
+        self.app_data.transfer_files.layoutChanged.connect(
             lambda: self.set_buttons_enabled(
                 self.app_data.transfer_files.rowCount() > 0
             )
         )
         return box
 
     def create_conn_actions(
@@ -279,17 +371,17 @@
         for tip, fn, needs_selection, icon in (
             ("Create a new connection profile", add, False, "plus-square"),
             ("Rename the current connection profile", rename, True, "edit"),
             ("Delete the current connection profile", delete, True, "trash-2"),
             ("Save the current connection profile", save, True, "save"),
         ):
             action = Action(f":icon/feather/{icon}.png", tip, self)
-            action.triggered.connect(fn)  # type: ignore
+            action.triggered.connect(fn)
             if needs_selection:
-                connections_selection.currentTextChanged.connect(  # type: ignore
+                connections_selection.currentTextChanged.connect(
                     partial(set_btn_enabled, action)
                 )
                 if not connections_selection.currentText():
                     action.setEnabled(False)
             yield action
 
     def create_options_panel(self) -> QtWidgets.QGroupBox:
@@ -329,25 +421,25 @@
             get_btn_from_group(
                 protocol_btn_grp, TransferProtocol[protocol].value
             ).click()
             self.app_data.transfer_protocol_args[
                 self.app_data.transfer_protocol_type
             ].target = connection
 
-        connections_selection.currentTextChanged.connect(load_connection)  # type: ignore
+        connections_selection.currentTextChanged.connect(load_connection)
 
         def toggle_protocol(btn: QtWidgets.QRadioButton, state: bool) -> None:
             protocol_name = TransferProtocol(btn.text()).name
             if state:
                 self.app_data.transfer_protocol_type = protocols.parse_protocol(
                     protocol_name
                 )
             protocol_boxes[protocol_name].setVisible(state)
 
-        protocol_btn_grp.buttonToggled.connect(toggle_protocol)  # type: ignore
+        protocol_btn_grp.buttonToggled.connect(toggle_protocol)
 
         toolbar = ToolBar("Options", self)
         for action in self.create_conn_actions(connections_selection):
             toolbar.addAction(action)
         layout_connection = hbox_layout(connections_selection, toolbar)
         layout_protocol_buttons = hbox_layout(*protocol_btn_grp.buttons())
 
@@ -390,23 +482,23 @@
         protocol = self.app_data.transfer_protocol_args[
             self.app_data.transfer_protocol_type
         ].target
 
         msg_signal.msg.connect(show_second_factor_dialog)
         self.run_workflow_thread(
             transfer.transfer,
-            f_kwargs=dict(
-                files=self.app_data.transfer_files.stringList(),
-                protocol=protocol,
-                config=self.app_data.config,
-                dry_run=dry_run,
-                pkg_name_suffix=self.app_data.encrypt_package_name_suffix,
-                progress=GuiProgress(self.progress_bar.setValue),
-                two_factor_callback=second_factor_callback,
-            ),
+            f_kwargs={
+                "files": self.app_data.transfer_files.stringList(),
+                "protocol": protocol,
+                "config": self.app_data.config,
+                "dry_run": dry_run,
+                "pkg_name_suffix": self.app_data.encrypt_package_name_suffix,
+                "progress": GuiProgress(self.progress_bar.setValue),
+                "two_factor_callback": second_factor_callback,
+            },
             capture_loggers=(
                 transfer.logger,
                 protocols.sftp.logger,
                 protocols.s3.logger,
             ),
             ignore_exceptions=True,
             report_config=self.app_data.config,
@@ -427,30 +519,30 @@
             self.windowFlags() & ~QtCore.Qt.WindowType.WindowContextHelpButtonHint
         )
 
         btn_box = QtWidgets.QDialogButtonBox(
             QtWidgets.QDialogButtonBox.StandardButton.Ok
             | QtWidgets.QDialogButtonBox.StandardButton.Cancel
         )
-        btn_box.accepted.connect(self.accept)  # type: ignore
-        btn_box.rejected.connect(self.reject)  # type: ignore
+        btn_box.accepted.connect(self.accept)
+        btn_box.rejected.connect(self.reject)
 
         self.text_field = LineEdit()
         self.text_field.setValidator(
             QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"[\w\-@]+"))
         )
         self.text_field.setText(default_input)
 
         def set_ok_enabled(text: str) -> None:
             btn_box.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(
                 len(text) > 0 and text not in forbidden
             )
 
         set_ok_enabled(self.text_field.text())
-        self.text_field.textChanged.connect(set_ok_enabled)  # type: ignore
+        self.text_field.textChanged.connect(set_ok_enabled)
 
         self.setLayout(vbox_layout(QtWidgets.QLabel(label), self.text_field, btn_box))
 
 
 def get_btn_from_group(
     btn_grp: QtWidgets.QButtonGroup, text: str
 ) -> QtWidgets.QAbstractButton:
```

### Comparing `sett-4.1.0/sett/gui/ui_model_bind.py` & `sett-4.2.0/sett/gui/ui_model_bind.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/protocols/__init__.py` & `sett-4.2.0/sett/protocols/__init__.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/protocols/liquid_files.py` & `sett-4.2.0/sett/protocols/liquid_files.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/protocols/multipart.py` & `sett-4.2.0/sett/protocols/multipart.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/protocols/s3.py` & `sett-4.2.0/sett/protocols/s3.py`

 * *Files 19% similar despite different names*

```diff
@@ -16,15 +16,18 @@
 
 
 @dataclass
 class Protocol(protocol.Protocol):
     host: str
     bucket: str
     access_key: str
+    secure: bool = True
     secret_key: Optional[Secret[str]] = None
+    # Session tokens are STS (Security Token Service) specific and temporary.
+    session_token: Optional[str] = None
 
     def required_password_args(self) -> Sequence[str]:
         return ("secret_key",)
 
     def upload(
         self,
         files: Sequence[str],
@@ -40,14 +43,16 @@
                 url_components[0],
             )
         try:
             client = Minio(
                 url_components[-1],  # ignore scheme if present
                 access_key=self.access_key,
                 secret_key=self.secret_key.reveal(),
+                session_token=self.session_token,
+                secure=self.secure,
             )
             for f in files:
                 p = Path(f)
                 size = p.stat().st_size
                 with open(p, "rb") as f_obj:
                     client.put_object(
                         self.bucket, p.name, with_progress(f_obj, progress), size
```

### Comparing `sett-4.1.0/sett/protocols/sftp.py` & `sett-4.2.0/sett/protocols/sftp.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/utils/config.py` & `sett-4.2.0/sett/utils/config.py`

 * *Files 2% similar despite different names*

```diff
@@ -139,19 +139,14 @@
         deserialize=abspath_expanduser,
         default=gpg.get_default_gnupg_home_dir(),
         label="GPG home directory",
         description="Path of the directory where GnuPG stores its keyrings and "
         "configuration files.",
         file_type=FileType.directory,
     )
-    sign_encrypted_data: bool = field_ext(
-        default=True,
-        label="Sign encrypted data",
-        description="Whether encrypted data should be signed with sender's key.",
-    )
     always_trust_recipient_key: bool = field_ext(
         default=True,
         label="Always trust recipient key",
         description="If unchecked, the encryption key must be signed by the local user.",
     )
     repo_url: str = field_ext(
         default="https://pypi.org",
@@ -338,15 +333,15 @@
 
     @classmethod
     def get_label(cls, arg: str) -> str:
         return str(cls.get_field(arg).metadata["metadata"].label)
 
 
 class ConnectionStore:
-    """Sftp/LiquidFiles connection configuration storage manager."""
+    """SFTP/S3/LiquidFiles connection configuration storage manager."""
 
     config_field_name = "connections"
 
     def __init__(self, config_path: Optional[str] = None):
         self.path = get_config_file() if config_path is None else config_path
 
     def _read(self) -> Dict[str, Any]:
@@ -492,14 +487,20 @@
     config_needs_update = False
 
     try:
         config_dict = load_config_dict(config_file)
     except UserError:
         return
 
+    # Migration to remove `sign_encrypted_data` from config.
+    # Migration added in December 2022, can be removed after about a year.
+    if "sign_encrypted_data" in config_dict:
+        del config_dict["sign_encrypted_data"]
+        config_needs_update = True
+
     # Migration to remove `offline` from config.
     # Migration added in October 2022, can be removed after about a year.
     if "offline" in config_dict:
         del config_dict["offline"]
         config_needs_update = True
 
     # Migration to remove `key_authority_fingerprint` from config.
```

### Comparing `sett-4.1.0/sett/utils/error_handling.py` & `sett-4.2.0/sett/utils/error_handling.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/utils/get_config_path.py` & `sett-4.2.0/sett/utils/get_config_path.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/utils/log.py` & `sett-4.2.0/sett/utils/log.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/utils/progress.py` & `sett-4.2.0/sett/utils/progress.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/workflows/config.py` & `sett-4.2.0/sett/workflows/config.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett/workflows/decrypt.py` & `sett-4.2.0/sett/workflows/decrypt.py`

 * *Files 1% similar despite different names*

```diff
@@ -52,15 +52,14 @@
     """Main function of the decrypt workflow. Decrypts and decompresses the
     input archive files.
     """
 
     with logger.log_task(
         f"Input data verification{' (dry_run)' if dry_run else ''}..."
     ):
-
         # Verify input data packages extension and content.
         logger.info("Files to decrypt: %s", ", ".join(files))
         logger.info("Output directory: %s", output_dir)
         for archive_path in files:
             logger.info("Verifying: %s", archive_path)
             check_package(archive_path)
 
@@ -69,15 +68,14 @@
 
     if dry_run:
         logger.info("Dry run completed successfully.")
         return
 
     for archive_file in files:
         with logger.log_task(f"Processing file: {archive_file}..."):
-
             # Reset progress bar for each archive file.
             if progress is not None:
                 progress.update(0.0)
 
             decrypt_archive(
                 archive_file,
                 passphrase=passphrase,
```

### Comparing `sett-4.1.0/sett/workflows/encrypt.py` & `sett-4.2.0/sett/workflows/encrypt.py`

 * *Files 2% similar despite different names*

```diff
@@ -136,15 +136,14 @@
 
     The function returns the file name of the created data package.
     """
 
     with logger.log_task(
         f"Input data verification{' (dry_run)' if dry_run else ''}..."
     ):
-
         # Verify user has specified at least 1 file to encrypt and that the
         # file(s) have read permission for the user.
         logger.info("Verify files to encrypt")
         if not files:
             raise UserError("Empty file list.")
         files_to_encrypt = list(search_files_recursively(files))
         if not files_to_encrypt:
@@ -205,14 +204,15 @@
                 dtr_id, purpose, config, sender_pub_key, recipients_pub_key
             )
             logger.info("DTR ID '%s' is valid for project '%s'", dtr_id, project_code)
         else:
             project_code = None
 
         logger.info("Verify available disk space")
+
         # The default value for the output name is based on date and time
         # when the script is being run.
         # Example output name: "20191011T145012.zip".
         timestamp = datetime.now().astimezone()
         output_name = generate_output_archive_name(
             prefix=project_code,
             timestamp=timestamp,
@@ -230,28 +230,31 @@
         )
         archive_paths = [
             os.path.join(CONTENT_FOLDER, os.path.relpath(f, start=root_dir))
             for f in files_to_encrypt
         ]
         check_paths_on_posix(archive_paths)
 
-        # If the user asked to sign the data, check that the GPG key password
-        # is correct.
-        if config.sign_encrypted_data and not dry_run:
-            logger.info("Verify data sender GPG password")
-            check_password(
-                password=enforce_passphrase(passphrase),
-                key_fingerprint=sender_pub_key.fingerprint,
-                gpg_store=config.gpg_store,
-            )
-
     if dry_run:
         logger.info("Dry run completed successfully")
         return None
 
+    # Verify the user's PGP key passphrase. The passphrase is needed to unlock
+    # the private PGP key used to sign the data.
+    # Note: the password is checked before starting to compress data, because
+    # that step can take a long time, and we don't want the workflow to fail
+    # at a later stage just because the user gave a wrong password.
+    logger.info("Verify data sender PGP key passphrase")
+    passphrase = enforce_passphrase(passphrase)
+    check_password(
+        password=passphrase,
+        key_fingerprint=sender_pub_key.fingerprint,
+        gpg_store=config.gpg_store,
+    )
+
     with logger.log_task("Compute sha256 checksum on input files..."):
         # Write input file checksums to a file that will be added to the
         # encrypted .tar.gz archive. This information must be encrypted as
         # file names sometimes contain information about their content.
         checksums = generate_checksums_file_content(
             zip(archive_paths, files_to_encrypt),
             # `max_workers` accepts only None and positive integers. Make
@@ -260,15 +263,15 @@
         )
         if progress is not None:
             progress.update(0.1)
 
     with logger.log_task("Compress and encrypt input data [this can take a while]..."):
         # Encryption is done with the recipient's public key and the optional
         # signing with the user's (i.e sender) private key. The user's private
-        # key passphrase is needed to sign the encrypted file.
+        # PGP key passphrase is needed to sign the encrypted file.
         encrypted_checksum_buf = io.StringIO()
         with delete_file_on_error(output_name), ZipFile(
             output_name, mode="w", compression=ZIP_STORED
         ) as zip_obj:
             with subprogress(progress, step_completion_increase=0.9) as scaled_progress:
                 # Create a tar archive containing all input files
                 archive_content: Tuple[ArchiveFileBase, ...] = (
@@ -299,20 +302,16 @@
                             output_file=output_file,
                             checksum_buffer=encrypted_checksum_buf,
                         ),
                         gpg_store=config.gpg_store,
                         recipients_fingerprint=[
                             key.fingerprint for key in recipients_pub_key
                         ],
-                        signature_fingerprint=sender_pub_key.fingerprint
-                        if config.sign_encrypted_data
-                        else None,
-                        passphrase=enforce_passphrase(passphrase)
-                        if config.sign_encrypted_data
-                        else None,
+                        signature_fingerprint=sender_pub_key.fingerprint,
+                        passphrase=passphrase,
                         always_trust=config.always_trust_recipient_key,
                     )
                 encrypted_checksum = encrypted_checksum_buf.read()
 
             logger.info("Generating metadata")
             # Create a dictionary with all the info we want to store in the
             # .json file, then pass this dictionary to json.dump that will
@@ -323,20 +322,19 @@
                 sender=HexStr1024(sender_pub_key.fingerprint),
                 recipients=[HexStr1024(key.fingerprint) for key in recipients_pub_key],
                 purpose=purpose,
                 checksum=HexStr256(encrypted_checksum),
                 compression_algorithm="gzip" if compression_level > 0 else "",
             )
             metadata_bytes, metadata_signature_bytes = byte_encode_metadata(
-                metadata,
-                config.gpg_store,
-                passphrase,
-                sender_pub_key if config.sign_encrypted_data else None,
+                metadata=metadata,
+                gpg_store=config.gpg_store,
+                passphrase=passphrase,
+                sender_pub_key=sender_pub_key,
             )
-
             in_memory_files = (
                 (METADATA_FILE, metadata_bytes),
                 (METADATA_FILE_SIG, metadata_signature_bytes),
             )
             for name, contents in in_memory_files:
                 zip_obj.writestr(
                     ZipInfo(name, date_time=datetime.utcnow().timetuple()[:6]),
@@ -355,17 +353,20 @@
 
 
 def check_arg_value(
     arg_value: T,
     arg_name: str,
     arg_type_checker: Callable[[T], Any],
 ) -> None:
-    """Verify that the value of variable arg_value that is named arg_name is
-    following type arg_type. arg_type_checker is a function that does a check
-    of the type of the variable.
+    """Verify that the arg_value of variable arg_name is of type arg_type.
+
+    :param arg_value: value of the variable/argument - the object to check.
+    :param arg_name: name of the variable/argument to check.
+    :param arg_type_checker: function that does a check of the type of the variable.
+    :raises UserError: if value is of the wrong type.
     """
     try:
         arg_type_checker(arg_value)
     except ValueError as e:
         raise UserError(f"Invalid value for argument '{arg_name}': {e}.") from e
```

### Comparing `sett-4.1.0/sett/workflows/transfer.py` & `sett-4.2.0/sett/workflows/transfer.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,15 +53,14 @@
         transfer task.
     :raises UserError:
     """
 
     with logger.log_task(
         f"Input data verification{' (dry_run)' if dry_run else ''}..."
     ):
-
         logger.info("Files to transfer: %s", ", ".join(files))
         files_by_recipient: Dict[Tuple[gpg.Key, ...], List[str]] = {}
 
         # Loop through all files to transfer and verify their content.
         for archive_path in files:
             logger.info("Verifying: %s", archive_path)
```

### Comparing `sett-4.1.0/sett/workflows/upload_keys.py` & `sett-4.2.0/sett/workflows/upload_keys.py`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/sett.egg-info/PKG-INFO` & `sett-4.2.0/sett.egg-info/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: sett
-Version: 4.1.0
+Version: 4.2.0
 Summary: Secure Encryption and Transfer Tool
 Home-page: https://gitlab.com/biomedit/sett
-Author: Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin
-Author-email: robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com
+Author: Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin, Simone Guzzi, Swen Vermeul
+Author-email: robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com, simone.guzzi@sib.swiss, swen@ethz.ch
 License: GPL3v3
-Project-URL: Documentation, https://sett.rtfd.io
+Project-URL: Documentation, https://sett.rtfd.io/en/stable
 Project-URL: Source, https://gitlab.com/biomedit/sett
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
@@ -30,22 +30,24 @@
 [![license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 [![python version](https://img.shields.io/pypi/pyversions/sett.svg?logo=python&logoColor=white)](https://pypi.org/project/sett)
 [![latest version](https://img.shields.io/pypi/v/sett.svg)](https://pypi.org/project/sett)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
 # SETT - Secure Encryption and Transfer Tool
 
-_sett_ enables packaging, encryption, and transfer of data to preconfigured locations.
+_sett_ enables packaging, encryption, and transfer of data to pre-configured
+locations.
 
 ## Documentation
 
 Detailed documentation as well as a quick-start guide can be found in the
-[sett documentation](https://sett.readthedocs.io).
+[sett documentation](https://sett.readthedocs.io/en/stable).
 
-For the latest, non-stable, version of the docs, see [here](<https://sett.readthedocs.io/en/latest/>).
+For the latest, non-stable, version of the docs, see
+[here](https://sett.readthedocs.io/en/latest).
 
 ### Documentation quick-links
 
 * [Requirements and installation](https://sett.readthedocs.io/en/stable/installation.html).
 * [Quick-start guide](https://sett.readthedocs.io/en/stable/quick_start.html).
 * [Creating and managing GnuPG keys with sett](https://sett.readthedocs.io/en/stable/key_management.html).
 * [Using sett to encrypt, transfer and decrypt data](https://sett.readthedocs.io/en/stable/usage.html)
```

### Comparing `sett-4.1.0/sett.egg-info/SOURCES.txt` & `sett-4.2.0/sett.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sett-4.1.0/setup.cfg` & `sett-4.2.0/setup.cfg`

 * *Files 18% similar despite different names*

```diff
@@ -1,33 +1,33 @@
 [metadata]
 name = sett
 version = attr: sett.__version__
 license = GPL3v3
 description = Secure Encryption and Transfer Tool
 long_description = file: README.md
 long_description_content_type = text/markdown
-author = Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin
-author_email = robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com
+author = Robin Engler, Jarosław Surkont, Gerhard Bräunlich, Kevin Sayers, Christian Ribeaud, François Martin, Simone Guzzi, Swen Vermeul
+author_email = robin.engler@sib.swiss, jaroslaw.surkont@unibas.ch, gerhard.braeunlich@id.ethz.ch, sayerskt@gmail.com, christian.ribeaud@karakun.com, francois.martin@karakun.com, simone.guzzi@sib.swiss, swen@ethz.ch
 url = https://gitlab.com/biomedit/sett
 classifiers = 
 	Programming Language :: Python :: 3
 	Programming Language :: Python :: 3.7
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
 	Programming Language :: Python :: 3.11
 	License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 	Operating System :: OS Independent
 project_urls = 
-	Documentation = https://sett.rtfd.io
+	Documentation = https://sett.rtfd.io/en/stable
 	Source = https://gitlab.com/biomedit/sett
 
 [options]
 install_requires = 
-	PySide6>=6.4.0
+	PySide6>=6.4.0, <6.5.0
 	colorama>=0.4.5 ; platform_system=='Windows'
 	gpg-lite>=0.12.3, <0.13.0
 	libbiomedit>=0.6.2, <0.7.0
 	paramiko>=2.12.0
 	sett-rs>=0.2.2, <0.3.0
 	typing_extensions ; python_version<'3.8'
 	minio>=7.1.12
@@ -45,15 +45,24 @@
 [options.package_data]
 sett = py.typed
 
 [options.extras_require]
 socks = PySocks
 legacy = PySide2>=5.15.2.1
 benchmark = pandas; matplotlib; seaborn
-dev = pytest-factoryboy
+dev = 
+	pylint==2.17.1
+	mypy==1.1.1
+	black==23.1.0
+	pytest==7.2.1
+	pytest-factoryboy==2.5.1
+	bandit==1.7.5
+	types-pkg_resources
+	types-paramiko
+	pandas-stubs
 
 [options.packages.find]
 exclude = 
 	test
 	test.*
 	benchmark
```

