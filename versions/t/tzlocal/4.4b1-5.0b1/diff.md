# Comparing `tmp/tzlocal-4.4b1.tar.gz` & `tmp/tzlocal-5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tzlocal-4.4b1.tar", last modified: Mon Mar 20 11:22:46 2023, max compression
+gzip compressed data, was "tzlocal-5.0b1.tar", last modified: Fri Apr  7 10:20:33 2023, max compression
```

## Comparing `tzlocal-4.4b1.tar` & `tzlocal-5.0b1.tar`

### file list

```diff
@@ -1,99 +1,99 @@
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     8018 2023-03-20 11:22:46.000000 tzlocal-4.4b1/CHANGES.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1060 2023-03-20 11:22:46.000000 tzlocal-4.4b1/LICENSE.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       96 2023-03-20 11:22:46.000000 tzlocal-4.4b1/MANIFEST.in
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    14754 2023-03-20 11:22:46.438709 tzlocal-4.4b1/PKG-INFO
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     5705 2023-03-20 11:22:46.000000 tzlocal-4.4b1/README.rst
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      143 2023-03-20 11:22:46.000000 tzlocal-4.4b1/pyproject.toml
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1339 2023-03-20 11:22:46.438709 tzlocal-4.4b1/setup.cfg
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       38 2023-03-20 11:22:46.000000 tzlocal-4.4b1/setup.py
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/Africa/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/Africa/Harare
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/UTC
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/etc/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/etc/conf.d/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       33 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/etc/conf.d/clock
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/etc/localtime
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/etc/sysconfig/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/etc/sysconfig/clock
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       64 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/usr/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/usr/share/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/usr/share/zoneinfo/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/usr/share/zoneinfo/Africa/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/usr/share/zoneinfo/Africa/Harare
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/var/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/conflicting/var/db/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       83 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/conflicting/var/db/zoneinfo
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/localtime/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/localtime/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/localtime/etc/localtime
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/etc/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/etc/conf.d/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/etc/conf.d/clock
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/etc/localtime
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/etc/sysconfig/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       12 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/etc/sysconfig/clock
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       59 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/usr/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/UCT
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/UTC
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/UTC
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/noconflict/usr/share/zoneinfo/Zulu
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/symlink_localtime/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/symlink_localtime/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/symlink_localtime/etc/localtime
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/symlink_localtime/usr/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/symlink_localtime/usr/share/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/Africa/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/Africa/Harare
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/termux/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/termux/system/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/termux/system/bin/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       68 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/termux/system/bin/getprop
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/timezone/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/timezone/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       65 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/timezone/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/timezone_setting/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/timezone_setting/etc/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/timezone_setting/etc/conf.d/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       27 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/timezone_setting/etc/conf.d/clock
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/top_line_comment/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/top_line_comment/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       38 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/top_line_comment/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/ubuntu_docker_bug/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/ubuntu_docker_bug/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        5 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/ubuntu_docker_bug/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/etc/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/etc/timezone
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/var/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/var/db/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       80 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/vardbzoneinfo/var/db/zoneinfo
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/zone_setting/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.434709 tzlocal-4.4b1/tests/test_data/zone_setting/etc/
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tests/test_data/zone_setting/etc/sysconfig/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_data/zone_setting/etc/sysconfig/clock
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    10948 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tests/test_tzlocal.py
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tzlocal/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      334 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal/__init__.py
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     8132 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal/unix.py
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     4193 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal/utils.py
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     4556 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal/win32.py
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    32071 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal/windows_tz.py
-drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-03-20 11:22:46.438709 tzlocal-4.4b1/tzlocal.egg-info/
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    14754 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/PKG-INFO
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1629 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/SOURCES.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/dependency_links.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      207 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/requires.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        8 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/top_level.txt
--rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-03-20 11:22:46.000000 tzlocal-4.4b1/tzlocal.egg-info/zip-safe
--rwxrwxr-x   0 lregebro  (1000) lregebro  (1000)     3318 2023-03-20 11:22:46.000000 tzlocal-4.4b1/update_windows_mappings.py
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.781944 tzlocal-5.0b1/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     8092 2023-04-07 10:20:33.000000 tzlocal-5.0b1/CHANGES.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1060 2023-04-07 10:20:33.000000 tzlocal-5.0b1/LICENSE.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      113 2023-04-07 10:20:33.000000 tzlocal-5.0b1/MANIFEST.in
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    15084 2023-04-07 10:20:33.781944 tzlocal-5.0b1/PKG-INFO
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     5961 2023-04-07 10:20:33.000000 tzlocal-5.0b1/README.rst
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      143 2023-04-07 10:20:33.000000 tzlocal-5.0b1/pyproject.toml
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1316 2023-04-07 10:20:33.781944 tzlocal-5.0b1/setup.cfg
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       38 2023-04-07 10:20:33.000000 tzlocal-5.0b1/setup.py
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/Africa/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/Africa/Harare
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/UTC
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/conflicting/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/conflicting/etc/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/conflicting/etc/conf.d/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       33 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/etc/conf.d/clock
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/etc/localtime
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/conflicting/etc/sysconfig/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/etc/sysconfig/clock
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       64 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/conflicting/usr/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/conflicting/usr/share/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/conflicting/usr/share/zoneinfo/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/conflicting/usr/share/zoneinfo/Africa/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/usr/share/zoneinfo/Africa/Harare
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/conflicting/var/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/conflicting/var/db/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       83 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/conflicting/var/db/zoneinfo
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/localtime/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/localtime/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/localtime/etc/localtime
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/noconflict/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/noconflict/etc/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/noconflict/etc/conf.d/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/etc/conf.d/clock
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/etc/localtime
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/noconflict/etc/sysconfig/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       12 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/etc/sysconfig/clock
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       59 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/noconflict/usr/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/UCT
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/Etc/UTC
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/UTC
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      118 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/noconflict/usr/share/zoneinfo/Zulu
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/symlink_localtime/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/symlink_localtime/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/symlink_localtime/etc/localtime
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/symlink_localtime/usr/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/symlink_localtime/usr/share/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.773944 tzlocal-5.0b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/Africa/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      157 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/symlink_localtime/usr/share/zoneinfo/Africa/Harare
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/termux/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/termux/system/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/termux/system/bin/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       68 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/termux/system/bin/getprop
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/timezone/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/timezone/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       65 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/timezone/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/timezone_setting/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/timezone_setting/etc/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/timezone_setting/etc/conf.d/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       27 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/timezone_setting/etc/conf.d/clock
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/top_line_comment/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/top_line_comment/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       38 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/top_line_comment/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/ubuntu_docker_bug/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/ubuntu_docker_bug/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        5 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/ubuntu_docker_bug/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/etc/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/etc/timezone
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/var/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.781944 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/var/db/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       80 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/vardbzoneinfo/var/db/zoneinfo
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/zone_setting/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.777944 tzlocal-5.0b1/tests/test_data/zone_setting/etc/
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.781944 tzlocal-5.0b1/tests/test_data/zone_setting/etc/sysconfig/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)       21 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_data/zone_setting/etc/sysconfig/clock
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    10284 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tests/test_tzlocal.py
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.781944 tzlocal-5.0b1/tzlocal/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      334 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal/__init__.py
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     8098 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal/unix.py
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     3880 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal/utils.py
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     4665 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal/win32.py
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    34203 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal/windows_tz.py
+drwxrwxr-x   0 lregebro  (1000) lregebro  (1000)        0 2023-04-07 10:20:33.781944 tzlocal-5.0b1/tzlocal.egg-info/
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)    15084 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/PKG-INFO
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)     1629 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/SOURCES.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/dependency_links.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)      185 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/requires.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        8 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/top_level.txt
+-rw-rw-r--   0 lregebro  (1000) lregebro  (1000)        1 2023-04-07 10:20:33.000000 tzlocal-5.0b1/tzlocal.egg-info/zip-safe
+-rwxrwxr-x   0 lregebro  (1000) lregebro  (1000)     3318 2023-04-07 10:20:33.000000 tzlocal-5.0b1/update_windows_mappings.py
```

### Comparing `tzlocal-4.4b1/CHANGES.txt` & `tzlocal-5.0b1/CHANGES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,16 @@
 Changes
 =======
 
+5.0b1 (2023-04-07)
+------------------
+
+- Removed the deprecation shim. 
+
+
 4.4b1 (2023-03-20)
 ------------------
 
 - Added debug logging
 
 
 4.3 (2023-03-18)
```

### Comparing `tzlocal-4.4b1/LICENSE.txt` & `tzlocal-5.0b1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `tzlocal-4.4b1/PKG-INFO` & `tzlocal-5.0b1/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tzlocal
-Version: 4.4b1
+Version: 5.0b1
 Summary: tzinfo object for the local timezone
 Home-page: UNKNOWN
 Author: Lennart Regebro
 Author-email: regebro@gmail.com
 License: MIT
 Project-URL: Source code, https://github.com/regebro/tzlocal
 Project-URL: Issue tracker, https://github.com/regebro/tzlocal/issues
@@ -41,14 +41,19 @@
 the timezone name, instead of a timezone object. On unix, it can raise an
 error if you don't have a timezone name configured, where `get_localzone()`
 will succeed, so only use that if you need the timezone name.
 
 4.0 also adds way more information on what is going wrong in your
 configuration when the configuration files are unclear or contradictory.
 
+Version 5.0 removes the `pytz_deprecation_shim`, and now only returns
+`zoneinfo` objects, like verion 3.0 did. If you need `pytz` objects, you have
+to stay on version 4.0. If there are bugs in version 4.0, I will rekease
+updates, but there will be no further functional changes on the 4.x branch.
+
 
 Info
 ----
 
 This Python module returns a ``tzinfo`` object (with a pytz_deprecation_shim,
 for pytz compatibility) with the local timezone information, under Unix and
 Windows.
@@ -161,30 +166,33 @@
 
     DEBUG:root:/etc/timezone found, contents:
      Europe/Warsaw
 
     DEBUG:root:/etc/localtime found
     DEBUG:root:2 found:
      {'/etc/timezone': 'Europe/Warsaw', '/etc/localtime is a symlink to': 'Europe/Warsaw'}
-    _PytzShimTimezone(zoneinfo.ZoneInfo(key='Europe/Warsaw'), 'Europe/Warsaw')
+    zoneinfo.ZoneInfo(key='Europe/Warsaw')
 
 
 Development
 -----------
 
-To create a development environment, create a virtualenv and make a development installation::
+For ease of development, there is a Makefile that will help you with basic tasks,
+like creating a development environment with all the necessary tools (although
+you need a supported Python version installed first)::
+
+    $ make devenv
 
-    $ virtualenv ve
-    $ source ve/bin/activation (Win32: .\ve\Scripts\activate)
-    (ve) $ pip install -e .[test,devenv]
+To run tests::
 
-To run tests, just use pytest, coverage is nice as well::
+    $ make test
 
-    (ve) $ pytest --cov=tzlocal
+Check the syntax::
 
+    $ make check
 
 
 Maintainer
 ----------
 
 * Lennart Regebro, regebro@gmail.com
 
@@ -223,14 +231,20 @@
 -------
 
 * MIT https://opensource.org/licenses/MIT
 
 Changes
 =======
 
+5.0b1 (2023-04-07)
+------------------
+
+- Removed the deprecation shim. 
+
+
 4.4b1 (2023-03-20)
 ------------------
 
 - Added debug logging
 
 
 4.3 (2023-03-18)
```

### Comparing `tzlocal-4.4b1/README.rst` & `tzlocal-5.0b1/README.rst`

 * *Files 6% similar despite different names*

```diff
@@ -13,14 +13,19 @@
 the timezone name, instead of a timezone object. On unix, it can raise an
 error if you don't have a timezone name configured, where `get_localzone()`
 will succeed, so only use that if you need the timezone name.
 
 4.0 also adds way more information on what is going wrong in your
 configuration when the configuration files are unclear or contradictory.
 
+Version 5.0 removes the `pytz_deprecation_shim`, and now only returns
+`zoneinfo` objects, like verion 3.0 did. If you need `pytz` objects, you have
+to stay on version 4.0. If there are bugs in version 4.0, I will rekease
+updates, but there will be no further functional changes on the 4.x branch.
+
 
 Info
 ----
 
 This Python module returns a ``tzinfo`` object (with a pytz_deprecation_shim,
 for pytz compatibility) with the local timezone information, under Unix and
 Windows.
@@ -133,30 +138,33 @@
 
     DEBUG:root:/etc/timezone found, contents:
      Europe/Warsaw
 
     DEBUG:root:/etc/localtime found
     DEBUG:root:2 found:
      {'/etc/timezone': 'Europe/Warsaw', '/etc/localtime is a symlink to': 'Europe/Warsaw'}
-    _PytzShimTimezone(zoneinfo.ZoneInfo(key='Europe/Warsaw'), 'Europe/Warsaw')
+    zoneinfo.ZoneInfo(key='Europe/Warsaw')
 
 
 Development
 -----------
 
-To create a development environment, create a virtualenv and make a development installation::
+For ease of development, there is a Makefile that will help you with basic tasks,
+like creating a development environment with all the necessary tools (although
+you need a supported Python version installed first)::
+
+    $ make devenv
 
-    $ virtualenv ve
-    $ source ve/bin/activation (Win32: .\ve\Scripts\activate)
-    (ve) $ pip install -e .[test,devenv]
+To run tests::
 
-To run tests, just use pytest, coverage is nice as well::
+    $ make test
 
-    (ve) $ pytest --cov=tzlocal
+Check the syntax::
 
+    $ make check
 
 
 Maintainer
 ----------
 
 * Lennart Regebro, regebro@gmail.com
```

### Comparing `tzlocal-4.4b1/setup.cfg` & `tzlocal-5.0b1/setup.cfg`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 [metadata]
 name = tzlocal
 description = tzinfo object for the local timezone
 long_description = file: README.rst, CHANGES.txt
-version = 4.4b1
+version = 5.0b1
 author = Lennart Regebro
 author_email = regebro@gmail.com
 project_urls = 
 	Source code = https://github.com/regebro/tzlocal
 	Issue tracker = https://github.com/regebro/tzlocal/issues
 license = MIT
 keywords = timezone
@@ -25,15 +25,14 @@
 	Programming Language :: Python :: 3.11
 
 [options]
 packages = find:
 python_requires = >= 3.7
 zip_safe = True
 install_requires = 
-	pytz_deprecation_shim
 	backports.zoneinfo; python_version < "3.9"
 	tzdata; platform_system == "Windows"
 
 [options.packages.find]
 include = tzlocal
 
 [options.extras_require]
```

### Comparing `tzlocal-4.4b1/tests/test_tzlocal.py` & `tzlocal-5.0b1/tests/test_tzlocal.py`

 * *Files 12% similar despite different names*

```diff
@@ -12,16 +12,18 @@
 
 if sys.version_info >= (3, 9):
     from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
 else:
     from backports.zoneinfo import ZoneInfo, ZoneInfoNotFoundError
 
 import logging
+
 logging.basicConfig(level=logging.DEBUG)
 
+
 @pytest.fixture(scope="session", autouse=True)
 def clear_tz_env_variable():
     os.environ.pop("TZ", None)
 
 
 def tz_path(zonefile: str = None) -> str:
     path = Path(__file__).parent.joinpath("test_data")
@@ -282,34 +284,14 @@
     platform.system() == "Windows", reason="Symbolic links are not available on Windows"
 )
 def test_noconflict():
     tz = tzlocal.unix._get_localzone(_root=tz_path("noconflict"))
     assert str(tz) == "Etc/UTC"
 
 
-def test_pytz_compatibility():
-    os.environ["TZ"] = "Africa/Harare"
-    tzlocal.unix.reload_localzone()
-    tz_harare = tzlocal.unix.get_localzone()
-    os.environ["TZ"] = "America/New_York"
-    tzlocal.unix.reload_localzone()
-    tz_newyork = tzlocal.unix.get_localzone()
-
-    dt = datetime(2021, 10, 1, 12, 00)
-    dt = tz_harare.localize(dt)
-    tz_harare.normalize(dt)
-    assert dt.tzinfo.zone == "Africa/Harare"
-    assert dt.utcoffset().total_seconds() == 7200
-    dt = dt.astimezone(tz_newyork)
-    dt = tz_newyork.normalize(dt)
-    assert dt.tzinfo.zone == "America/New_York"
-    assert dt.utcoffset().total_seconds() == -14400
-    del os.environ["TZ"]
-
-
 def test_zoneinfo_compatibility():
     os.environ["TZ"] = "Africa/Harare"
     tzlocal.unix.reload_localzone()
     tz_harare = tzlocal.unix.get_localzone()
     assert str(tz_harare) == "Africa/Harare"
 
     os.environ["TZ"] = "America/New_York"
```

### Comparing `tzlocal-4.4b1/tzlocal/unix.py` & `tzlocal-5.0b1/tzlocal/unix.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,20 @@
 import logging
 import os
 import re
 import sys
 import warnings
 from datetime import timezone
-import pytz_deprecation_shim as pds
 
 from tzlocal import utils
 
 if sys.version_info >= (3, 9):
-    from zoneinfo import ZoneInfo  # pragma: no cover
+    import zoneinfo  # pragma: no cover
 else:
-    from backports.zoneinfo import ZoneInfo  # pragma: no cover
+    from backports import zoneinfo  # pragma: no cover
 
 _cache_tz = None
 _cache_tz_name = None
 
 
 def _get_localzone_name(_root="/"):
     """Tries to find the local timezone configuration.
@@ -121,45 +120,45 @@
     if os.path.exists(tzpath) and os.path.islink(tzpath):
         logging.debug(f"{tzpath} found")
         etctz = os.path.realpath(tzpath)
         start = etctz.find("/") + 1
         while start != 0:
             etctz = etctz[start:]
             try:
-                pds.timezone(etctz)
+                zoneinfo.ZoneInfo(etctz)
                 tzinfo = f"{tzpath} is a symlink to"
                 found_configs[tzinfo] = etctz.replace(" ", "_")
                 # Only need first valid relative path in simlink.
                 break
-            except pds.UnknownTimeZoneError:
+            except zoneinfo.ZoneInfoNotFoundError:
                 pass
             start = etctz.find("/") + 1
 
     if len(found_configs) > 0:
         logging.debug(f"{len(found_configs)} found:\n {found_configs}")
         # We found some explicit config of some sort!
         if len(found_configs) > 1:
             # Uh-oh, multiple configs. See if they match:
             unique_tzs = set()
-            zoneinfo = os.path.join(_root, "usr", "share", "zoneinfo")
-            directory_depth = len(zoneinfo.split(os.path.sep))
+            zoneinfopath = os.path.join(_root, "usr", "share", "zoneinfo")
+            directory_depth = len(zoneinfopath.split(os.path.sep))
 
             for tzname in found_configs.values():
                 # Look them up in /usr/share/zoneinfo, and find what they
                 # really point to:
-                path = os.path.realpath(os.path.join(zoneinfo, *tzname.split("/")))
+                path = os.path.realpath(os.path.join(zoneinfopath, *tzname.split("/")))
                 real_zone_name = "/".join(path.split(os.path.sep)[directory_depth:])
                 unique_tzs.add(real_zone_name)
 
             if len(unique_tzs) != 1:
                 message = "Multiple conflicting time zone configurations found:\n"
                 for key, value in found_configs.items():
                     message += f"{key}: {value}\n"
                 message += "Fix the configuration, or set the time zone in a TZ environment variable.\n"
-                raise utils.ZoneInfoNotFoundError(message)
+                raise zoneinfo.ZoneInfoNotFoundError(message)
 
         # We found exactly one config! Use it.
         return list(found_configs.values())[0]
 
 
 def _get_localzone(_root="/"):
     """Creates a timezone object from the timezone name.
@@ -182,21 +181,21 @@
         logging.debug("No explicit setting existed. Use localtime")
         for filename in ("etc/localtime", "usr/local/etc/localtime"):
             tzpath = os.path.join(_root, filename)
 
             if not os.path.exists(tzpath):
                 continue
             with open(tzpath, "rb") as tzfile:
-                tz = pds.wrap_zone(ZoneInfo.from_file(tzfile, key="local"))
+                tz = zoneinfo.ZoneInfo.from_file(tzfile, key="local")
                 break
         else:
             warnings.warn("Can not find any timezone configuration, defaulting to UTC.")
             tz = timezone.utc
     else:
-        tz = pds.timezone(tzname)
+        tz = zoneinfo.ZoneInfo(tzname)
 
     if _root == "/":
         # We are using a file in etc to name the timezone.
         # Verify that the timezone specified there is actually used:
         utils.assert_tz_offset(tz)
     return tz
```

### Comparing `tzlocal-4.4b1/tzlocal/utils.py` & `tzlocal-5.0b1/tzlocal/utils.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,30 +1,21 @@
 import logging
 import os
 import time
 import datetime
 import calendar
-import pytz_deprecation_shim as pds
 
 try:
     import zoneinfo  # pragma: no cover
 except ImportError:
     from backports import zoneinfo  # pragma: no cover
 
 from tzlocal import windows_tz
 
 
-class ZoneInfoNotFoundError(pds.UnknownTimeZoneError, zoneinfo.ZoneInfoNotFoundError):
-    """An exception derived from both pytz and zoneinfo
-
-    This exception will be trappable both by pytz expecting clients and
-    zoneinfo expecting clients.
-    """
-
-
 def get_system_offset():
     """Get system's timezone offset using built-in library time.
 
     For the Timezone constants (altzone, daylight, timezone, and tzname), the
     value is determined by the timezone rules in effect at module load time or
     the last time tzset() is called and may be incorrect for times in the past.
 
@@ -113,21 +104,20 @@
     if os.path.isabs(tzenv) and os.path.exists(tzenv):
         # Try to see if we can figure out the name
         tzname = _tz_name_from_env(tzenv)
         if not tzname:
             # Nope, not a standard timezone name, just take the filename
             tzname = tzenv.split(os.sep)[-1]
         with open(tzenv, "rb") as tzfile:
-            zone = zoneinfo.ZoneInfo.from_file(tzfile, key=tzname)
-            return pds.wrap_zone(zone)
+            return zoneinfo.ZoneInfo.from_file(tzfile, key=tzname)
 
     # TZ must specify a zoneinfo zone.
     try:
-        tz = pds.timezone(tzenv)
+        tz = zoneinfo.ZoneInfo(tzenv)
         # That worked, so we return this:
         return tz
-    except pds.UnknownTimeZoneError:
+    except zoneinfo.ZoneInfoNotFoundError:
         # Nope, it's something like "PST4DST" etc, we can't handle that.
-        raise ZoneInfoNotFoundError(
+        raise zoneinfo.ZoneInfoNotFoundError(
             "tzlocal() does not support non-zoneinfo timezones like %s. \n"
             "Please use a timezone in the form of Continent/City" % tzenv
         ) from None
```

### Comparing `tzlocal-4.4b1/tzlocal/win32.py` & `tzlocal-5.0b1/tzlocal/win32.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,16 +1,20 @@
 import logging
 from datetime import datetime
-import pytz_deprecation_shim as pds
 
 try:
     import _winreg as winreg
 except ImportError:
     import winreg
 
+try:
+    import zoneinfo  # pragma: no cover
+except ImportError:
+    from backports import zoneinfo  # pragma: no cover
+
 from tzlocal.windows_tz import win_tz
 from tzlocal import utils
 
 _cache_tz = None
 _cache_tz_name = None
 
 
@@ -72,35 +76,35 @@
     if timezone is None:
         # Nope, that didn't work. Try adding "Standard Time",
         # it seems to work a lot of times:
         timezone = win_tz.get(tzkeyname + " Standard Time")
 
     # Return what we have.
     if timezone is None:
-        raise utils.ZoneInfoNotFoundError(tzkeyname)
+        raise zoneinfo.ZoneInfoNotFoundError(tzkeyname)
 
     if keyvalues.get("DynamicDaylightTimeDisabled", 0) == 1:
         # DST is disabled, so don't return the timezone name,
         # instead return Etc/GMT+offset
 
-        tz = pds.timezone(timezone)
+        tz = zoneinfo.ZoneInfo(timezone)
         has_dst, std_offset, dst_offset = _get_dst_info(tz)
         if not has_dst:
             # The DST is turned off in the windows configuration,
             # but this timezone doesn't have DST so it doesn't matter
             return timezone
 
         if std_offset is None:
-            raise utils.ZoneInfoNotFoundError(
+            raise zoneinfo.ZoneInfoNotFoundError(
                 f"{tzkeyname} claims to not have a non-DST time!?"
             )
 
         if std_offset % 3600:
             # I can't convert this to an hourly offset
-            raise utils.ZoneInfoNotFoundError(
+            raise zoneinfo.ZoneInfoNotFoundError(
                 f"tzlocal can't support disabling DST in the {timezone} zone."
             )
 
         # This has whole hours as offset, return it as Etc/GMT
         return f"Etc/GMT{-std_offset//3600:+.0f}"
 
     return timezone
@@ -116,15 +120,15 @@
 
 
 def get_localzone():
     """Returns the zoneinfo-based tzinfo object that matches the Windows-configured timezone."""
 
     global _cache_tz
     if _cache_tz is None:
-        _cache_tz = pds.timezone(get_localzone_name())
+        _cache_tz = zoneinfo.ZoneInfo(get_localzone_name())
 
     if not utils._tz_name_from_env():
         # If the timezone does NOT come from a TZ environment variable,
         # verify that it's correct. If it's from the environment,
         # we accept it, this is so you can run tests with different timezones.
         utils.assert_tz_offset(_cache_tz)
 
@@ -132,10 +136,10 @@
 
 
 def reload_localzone():
     """Reload the cached localzone. You need to call this if the timezone has changed."""
     global _cache_tz
     global _cache_tz_name
     _cache_tz_name = _get_localzone_name()
-    _cache_tz = pds.timezone(_cache_tz_name)
+    _cache_tz = zoneinfo.ZoneInfo(_cache_tz_name)
     utils.assert_tz_offset(_cache_tz)
     return _cache_tz
```

### Comparing `tzlocal-4.4b1/tzlocal.egg-info/PKG-INFO` & `tzlocal-5.0b1/tzlocal.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tzlocal
-Version: 4.4b1
+Version: 5.0b1
 Summary: tzinfo object for the local timezone
 Home-page: UNKNOWN
 Author: Lennart Regebro
 Author-email: regebro@gmail.com
 License: MIT
 Project-URL: Source code, https://github.com/regebro/tzlocal
 Project-URL: Issue tracker, https://github.com/regebro/tzlocal/issues
@@ -41,14 +41,19 @@
 the timezone name, instead of a timezone object. On unix, it can raise an
 error if you don't have a timezone name configured, where `get_localzone()`
 will succeed, so only use that if you need the timezone name.
 
 4.0 also adds way more information on what is going wrong in your
 configuration when the configuration files are unclear or contradictory.
 
+Version 5.0 removes the `pytz_deprecation_shim`, and now only returns
+`zoneinfo` objects, like verion 3.0 did. If you need `pytz` objects, you have
+to stay on version 4.0. If there are bugs in version 4.0, I will rekease
+updates, but there will be no further functional changes on the 4.x branch.
+
 
 Info
 ----
 
 This Python module returns a ``tzinfo`` object (with a pytz_deprecation_shim,
 for pytz compatibility) with the local timezone information, under Unix and
 Windows.
@@ -161,30 +166,33 @@
 
     DEBUG:root:/etc/timezone found, contents:
      Europe/Warsaw
 
     DEBUG:root:/etc/localtime found
     DEBUG:root:2 found:
      {'/etc/timezone': 'Europe/Warsaw', '/etc/localtime is a symlink to': 'Europe/Warsaw'}
-    _PytzShimTimezone(zoneinfo.ZoneInfo(key='Europe/Warsaw'), 'Europe/Warsaw')
+    zoneinfo.ZoneInfo(key='Europe/Warsaw')
 
 
 Development
 -----------
 
-To create a development environment, create a virtualenv and make a development installation::
+For ease of development, there is a Makefile that will help you with basic tasks,
+like creating a development environment with all the necessary tools (although
+you need a supported Python version installed first)::
+
+    $ make devenv
 
-    $ virtualenv ve
-    $ source ve/bin/activation (Win32: .\ve\Scripts\activate)
-    (ve) $ pip install -e .[test,devenv]
+To run tests::
 
-To run tests, just use pytest, coverage is nice as well::
+    $ make test
 
-    (ve) $ pytest --cov=tzlocal
+Check the syntax::
 
+    $ make check
 
 
 Maintainer
 ----------
 
 * Lennart Regebro, regebro@gmail.com
 
@@ -223,14 +231,20 @@
 -------
 
 * MIT https://opensource.org/licenses/MIT
 
 Changes
 =======
 
+5.0b1 (2023-04-07)
+------------------
+
+- Removed the deprecation shim. 
+
+
 4.4b1 (2023-03-20)
 ------------------
 
 - Added debug logging
 
 
 4.3 (2023-03-18)
```

### Comparing `tzlocal-4.4b1/tzlocal.egg-info/SOURCES.txt` & `tzlocal-5.0b1/tzlocal.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tzlocal-4.4b1/update_windows_mappings.py` & `tzlocal-5.0b1/update_windows_mappings.py`

 * *Files identical despite different names*

