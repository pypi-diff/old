# Comparing `tmp/zcmds-1.4.8.tar.gz` & `tmp/zcmds-1.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "zcmds-1.4.8.tar", last modified: Tue Apr  4 02:38:34 2023, max compression
+gzip compressed data, was "zcmds-1.4.9.tar", last modified: Thu Apr  6 18:07:06 2023, max compression
```

## Comparing `zcmds-1.4.8.tar` & `zcmds-1.4.9.tar`

### file list

```diff
@@ -1,111 +1,111 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.210270 zcmds-1.4.8/
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.038269 zcmds-1.4.8/.github/
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.102268 zcmds-1.4.8/.github/workflows/
--rw-rw-rw-   0        0        0      899 2022-11-05 21:21:20.000000 zcmds-1.4.8/.github/workflows/lint.yml
--rw-rw-rw-   0        0        0      833 2022-11-05 21:19:03.000000 zcmds-1.4.8/.github/workflows/push_macos.yml
--rw-rw-rw-   0        0        0      803 2023-02-02 07:49:35.000000 zcmds-1.4.8/.github/workflows/push_ubuntu.yml
--rw-rw-rw-   0        0        0     1650 2023-02-02 07:49:35.000000 zcmds-1.4.8/.github/workflows/push_win.yml
--rw-rw-rw-   0        0        0     2013 2022-10-08 21:49:27.000000 zcmds-1.4.8/.gitignore
--rw-rw-rw-   0        0        0    27051 2023-02-02 07:58:31.000000 zcmds-1.4.8/.pylintrc
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.103269 zcmds-1.4.8/.vscode/
--rw-rw-rw-   0        0        0     1046 2023-04-02 08:55:51.000000 zcmds-1.4.8/.vscode/settings.json
--rw-rw-rw-   0        0        0     1085 2022-02-21 03:22:36.000000 zcmds-1.4.8/LICENSE
--rw-rw-rw-   0        0        0      205 2023-04-02 09:38:20.000000 zcmds-1.4.8/MANIFEST.in
--rw-rw-rw-   0        0        0      106 2023-04-03 23:26:07.000000 zcmds-1.4.8/NOTES.md
--rw-rw-rw-   0        0        0     7447 2023-04-04 02:38:34.210270 zcmds-1.4.8/PKG-INFO
--rw-rw-rw-   0        0        0     7063 2023-04-04 02:37:58.000000 zcmds-1.4.8/README.md
--rw-rw-rw-   0        0        0      292 2023-04-02 08:27:52.000000 zcmds-1.4.8/activate.sh
--rw-rw-rw-   0        0        0      284 2023-03-14 23:38:05.000000 zcmds-1.4.8/lint.sh
--rw-rw-rw-   0        0        0     1994 2022-07-27 00:44:21.000000 zcmds-1.4.8/make_venv.py
--rw-rw-rw-   0        0        0      571 2023-04-04 02:38:12.000000 zcmds-1.4.8/pyproject.toml
--rw-rw-rw-   0        0        0       28 2022-02-21 03:22:36.000000 zcmds-1.4.8/requirements.testing.txt
--rw-rw-rw-   0        0        0      217 2023-04-03 18:51:55.000000 zcmds-1.4.8/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-04-04 02:38:34.211267 zcmds-1.4.8/setup.cfg
--rw-rw-rw-   0        0        0     1431 2023-04-02 09:38:31.000000 zcmds-1.4.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.040267 zcmds-1.4.8/src/
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.108270 zcmds-1.4.8/src/zcmds/
--rw-rw-rw-   0        0        0       33 2022-10-15 20:55:39.000000 zcmds-1.4.8/src/zcmds/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.133268 zcmds-1.4.8/src/zcmds/assets/
--rw-rw-rw-   0        0        0    77452 2023-02-02 07:49:35.000000 zcmds-1.4.8/src/zcmds/assets/bell.mp3
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.134266 zcmds-1.4.8/src/zcmds/cmds/
--rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.8/src/zcmds/cmds/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.175267 zcmds-1.4.8/src/zcmds/cmds/common/
--rw-rw-rw-   0        0        0       83 2022-02-24 09:10:00.000000 zcmds-1.4.8/src/zcmds/cmds/common/README.md
--rw-rw-rw-   0        0        0        0 2022-02-21 10:39:02.000000 zcmds-1.4.8/src/zcmds/cmds/common/__init__.py
--rw-rw-rw-   0        0        0     5364 2023-04-03 19:00:15.000000 zcmds-1.4.8/src/zcmds/cmds/common/askai.py
--rw-rw-rw-   0        0        0     1554 2023-02-26 19:57:05.000000 zcmds-1.4.8/src/zcmds/cmds/common/audnorm.py
--rw-rw-rw-   0        0        0      311 2023-01-01 07:58:23.000000 zcmds-1.4.8/src/zcmds/cmds/common/comports.py
--rw-rw-rw-   0        0        0     4305 2022-12-03 00:29:53.000000 zcmds-1.4.8/src/zcmds/cmds/common/diskaudit.py
--rw-rw-rw-   0        0        0     1172 2023-03-29 02:40:46.000000 zcmds-1.4.8/src/zcmds/cmds/common/findfiles.py
--rw-rw-rw-   0        0        0      616 2023-02-02 08:05:19.000000 zcmds-1.4.8/src/zcmds/cmds/common/fixinternet.py
--rw-rw-rw-   0        0        0     2107 2023-04-03 03:08:28.000000 zcmds-1.4.8/src/zcmds/cmds/common/geninvoice.py
--rw-rw-rw-   0        0        0     7264 2023-04-02 23:37:24.000000 zcmds-1.4.8/src/zcmds/cmds/common/gitsummary.py
--rw-rw-rw-   0        0        0     1714 2023-02-27 00:07:25.000000 zcmds-1.4.8/src/zcmds/cmds/common/img2vid.py
--rw-rw-rw-   0        0        0     3303 2023-02-02 07:49:35.000000 zcmds-1.4.8/src/zcmds/cmds/common/imgai.py
--rw-rw-rw-   0        0        0     1785 2023-02-02 07:57:46.000000 zcmds-1.4.8/src/zcmds/cmds/common/obs_organize.py
--rw-rw-rw-   0        0        0      739 2023-01-11 08:02:51.000000 zcmds-1.4.8/src/zcmds/cmds/common/openaicfg.py
--rw-rw-rw-   0        0        0     2394 2023-02-09 20:17:45.000000 zcmds-1.4.8/src/zcmds/cmds/common/pdf2png.py
--rw-rw-rw-   0        0        0     1166 2023-03-30 01:50:51.000000 zcmds-1.4.8/src/zcmds/cmds/common/pdf2txt.py
--rw-rw-rw-   0        0        0      556 2023-03-24 04:23:48.000000 zcmds-1.4.8/src/zcmds/cmds/common/printenv.py
--rw-rw-rw-   0        0        0      756 2023-04-03 19:33:48.000000 zcmds-1.4.8/src/zcmds/cmds/common/say.py
--rw-rw-rw-   0        0        0      119 2022-02-21 05:10:16.000000 zcmds-1.4.8/src/zcmds/cmds/common/search_and_replace.py
--rw-rw-rw-   0        0        0      108 2022-02-21 05:10:10.000000 zcmds-1.4.8/src/zcmds/cmds/common/search_in_files.py
--rw-rw-rw-   0        0        0       44 2022-03-31 06:58:04.000000 zcmds-1.4.8/src/zcmds/cmds/common/sharedir.py
--rw-rw-rw-   0        0        0     1986 2023-03-23 20:09:17.000000 zcmds-1.4.8/src/zcmds/cmds/common/stereo2mono.py
--rw-rw-rw-   0        0        0     1340 2022-05-20 06:00:29.000000 zcmds-1.4.8/src/zcmds/cmds/common/vid2gif.py
--rw-rw-rw-   0        0        0     1830 2022-03-10 02:29:32.000000 zcmds-1.4.8/src/zcmds/cmds/common/vid2jpg.py
--rw-rw-rw-   0        0        0      553 2022-03-02 20:54:15.000000 zcmds-1.4.8/src/zcmds/cmds/common/vid2mp3.py
--rw-rw-rw-   0        0        0     1333 2022-11-05 02:45:38.000000 zcmds-1.4.8/src/zcmds/cmds/common/vid2mp4.py
--rw-rw-rw-   0        0        0     1080 2022-08-16 20:18:02.000000 zcmds-1.4.8/src/zcmds/cmds/common/vid2webm.py
--rw-rw-rw-   0        0        0     3377 2023-04-04 02:37:00.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidcat.py
--rw-rw-rw-   0        0        0     4891 2022-11-10 05:10:07.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidclip.py
--rw-rw-rw-   0        0        0     1984 2022-02-24 06:01:55.000000 zcmds-1.4.8/src/zcmds/cmds/common/viddur.py
--rw-rw-rw-   0        0        0     3533 2023-01-01 07:59:58.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidhero.py
--rw-rw-rw-   0        0        0     5987 2023-03-14 20:56:14.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidinfo.py
--rw-rw-rw-   0        0        0     1242 2022-09-03 19:04:52.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidlist.py
--rw-rw-rw-   0        0        0     2777 2022-09-03 19:04:52.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidmatrix.py
--rw-rw-rw-   0        0        0     1705 2022-11-09 03:22:17.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidmute.py
--rw-rw-rw-   0        0        0     1688 2023-03-23 20:09:17.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidshrink.py
--rw-rw-rw-   0        0        0     1726 2023-02-26 19:57:37.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidspeed.py
--rw-rw-rw-   0        0        0     1807 2022-07-27 02:41:03.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidvol.py
--rw-rw-rw-   0        0        0     5750 2023-04-03 19:35:12.000000 zcmds-1.4.8/src/zcmds/cmds/common/vidwebmaster.py
--rw-rw-rw-   0        0        0     3408 2023-03-24 04:25:59.000000 zcmds-1.4.8/src/zcmds/cmds/common/whichall.py
--rw-rw-rw-   0        0        0      933 2023-03-23 20:09:17.000000 zcmds-1.4.8/src/zcmds/cmds/common/zcmds_main.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.178273 zcmds-1.4.8/src/zcmds/cmds/darwin/
--rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.8/src/zcmds/cmds/darwin/__init__.py
--rw-rw-rw-   0        0        0     3505 2022-11-04 21:13:40.000000 zcmds-1.4.8/src/zcmds/cmds/darwin/test_net_connection.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.189268 zcmds-1.4.8/src/zcmds/cmds/linux/
--rw-rw-rw-   0        0        0       34 2022-02-21 09:21:39.000000 zcmds-1.4.8/src/zcmds/cmds/linux/TODO
--rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.8/src/zcmds/cmds/linux/__init__.py
--rw-rw-rw-   0        0        0      366 2023-04-02 09:48:39.000000 zcmds-1.4.8/src/zcmds/cmds.py
--rw-rw-rw-   0        0        0     1792 2023-04-04 01:35:43.000000 zcmds-1.4.8/src/zcmds/cmds.txt
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.190270 zcmds-1.4.8/src/zcmds/install/
--rw-rw-rw-   0        0        0        0 2022-02-21 03:22:36.000000 zcmds-1.4.8/src/zcmds/install/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.194270 zcmds-1.4.8/src/zcmds/install/darwin/
--rw-rw-rw-   0        0        0        0 2022-02-24 11:15:15.000000 zcmds-1.4.8/src/zcmds/install/darwin/__init__.py
--rw-rw-rw-   0        0        0     1438 2022-07-27 03:33:16.000000 zcmds-1.4.8/src/zcmds/install/darwin/darwin_update.py
--rw-rw-rw-   0        0        0      617 2022-02-21 07:57:18.000000 zcmds-1.4.8/src/zcmds/install/darwin/macOS_key_bindings.dict
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.205270 zcmds-1.4.8/src/zcmds/util/
--rw-rw-rw-   0        0        0        0 2022-02-21 05:09:08.000000 zcmds-1.4.8/src/zcmds/util/__init__.py
--rw-rw-rw-   0        0        0     1097 2023-04-02 22:01:35.000000 zcmds-1.4.8/src/zcmds/util/config.py
--rw-rw-rw-   0        0        0     1710 2023-03-31 05:34:41.000000 zcmds-1.4.8/src/zcmds/util/file_search_and_replacer.py
--rw-rw-rw-   0        0        0     1063 2023-03-31 05:28:50.000000 zcmds-1.4.8/src/zcmds/util/file_searcher.py
--rw-rw-rw-   0        0        0     4309 2023-04-02 06:56:44.000000 zcmds-1.4.8/src/zcmds/util/fileutils.py
--rw-rw-rw-   0        0        0      669 2022-02-21 05:08:59.000000 zcmds-1.4.8/src/zcmds/util/index_all_files.py
--rw-rw-rw-   0        0        0      381 2023-04-03 18:54:53.000000 zcmds-1.4.8/src/zcmds/util/prompt_input.py
--rw-rw-rw-   0        0        0      532 2023-04-03 19:36:05.000000 zcmds-1.4.8/src/zcmds/util/say.py
--rw-rw-rw-   0        0        0      249 2023-02-02 07:49:35.000000 zcmds-1.4.8/src/zcmds/util/sound.py
--rw-rw-rw-   0        0        0      147 2023-04-04 02:38:18.000000 zcmds-1.4.8/src/zcmds/version.py
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.132268 zcmds-1.4.8/src/zcmds.egg-info/
--rw-rw-rw-   0        0        0     7447 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2691 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0     1734 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      223 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/requires.txt
--rw-rw-rw-   0        0        0        6 2023-04-04 02:38:33.000000 zcmds-1.4.8/src/zcmds.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-04 02:38:34.208269 zcmds-1.4.8/tests/
--rw-rw-rw-   0        0        0      876 2022-11-05 20:55:29.000000 zcmds-1.4.8/tests/test_main.py
--rw-rw-rw-   0        0        0      260 2023-02-02 07:49:35.000000 zcmds-1.4.8/tests/test_sound.py
--rw-rw-rw-   0        0        0      746 2023-01-03 06:43:04.000000 zcmds-1.4.8/tests/test_version.py
--rw-rw-rw-   0        0        0      451 2023-02-02 07:49:35.000000 zcmds-1.4.8/tox.ini
--rw-rw-rw-   0        0        0      275 2023-01-01 07:58:23.000000 zcmds-1.4.8/upload_package.sh
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.523714 zcmds-1.4.9/
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.401713 zcmds-1.4.9/.github/
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.427716 zcmds-1.4.9/.github/workflows/
+-rw-rw-rw-   0        0        0      899 2022-11-05 21:21:20.000000 zcmds-1.4.9/.github/workflows/lint.yml
+-rw-rw-rw-   0        0        0      833 2022-11-05 21:19:03.000000 zcmds-1.4.9/.github/workflows/push_macos.yml
+-rw-rw-rw-   0        0        0      803 2023-02-02 07:49:35.000000 zcmds-1.4.9/.github/workflows/push_ubuntu.yml
+-rw-rw-rw-   0        0        0     1650 2023-02-02 07:49:35.000000 zcmds-1.4.9/.github/workflows/push_win.yml
+-rw-rw-rw-   0        0        0     2013 2022-10-08 21:49:27.000000 zcmds-1.4.9/.gitignore
+-rw-rw-rw-   0        0        0    27051 2023-02-02 07:58:31.000000 zcmds-1.4.9/.pylintrc
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.428712 zcmds-1.4.9/.vscode/
+-rw-rw-rw-   0        0        0     1046 2023-04-02 08:55:51.000000 zcmds-1.4.9/.vscode/settings.json
+-rw-rw-rw-   0        0        0     1085 2022-02-21 03:22:36.000000 zcmds-1.4.9/LICENSE
+-rw-rw-rw-   0        0        0      205 2023-04-02 09:38:20.000000 zcmds-1.4.9/MANIFEST.in
+-rw-rw-rw-   0        0        0      106 2023-04-03 23:26:07.000000 zcmds-1.4.9/NOTES.md
+-rw-rw-rw-   0        0        0     7554 2023-04-06 18:07:06.522715 zcmds-1.4.9/PKG-INFO
+-rw-rw-rw-   0        0        0     7170 2023-04-06 18:05:22.000000 zcmds-1.4.9/README.md
+-rw-rw-rw-   0        0        0      292 2023-04-02 08:27:52.000000 zcmds-1.4.9/activate.sh
+-rw-rw-rw-   0        0        0      284 2023-03-14 23:38:05.000000 zcmds-1.4.9/lint.sh
+-rw-rw-rw-   0        0        0     1994 2022-07-27 00:44:21.000000 zcmds-1.4.9/make_venv.py
+-rw-rw-rw-   0        0        0      571 2023-04-06 18:04:11.000000 zcmds-1.4.9/pyproject.toml
+-rw-rw-rw-   0        0        0       28 2022-02-21 03:22:36.000000 zcmds-1.4.9/requirements.testing.txt
+-rw-rw-rw-   0        0        0      217 2023-04-03 18:51:55.000000 zcmds-1.4.9/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 18:07:06.523714 zcmds-1.4.9/setup.cfg
+-rw-rw-rw-   0        0        0     1431 2023-04-02 09:38:31.000000 zcmds-1.4.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.402719 zcmds-1.4.9/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.433714 zcmds-1.4.9/src/zcmds/
+-rw-rw-rw-   0        0        0       33 2022-10-15 20:55:39.000000 zcmds-1.4.9/src/zcmds/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.454716 zcmds-1.4.9/src/zcmds/assets/
+-rw-rw-rw-   0        0        0    77452 2023-02-02 07:49:35.000000 zcmds-1.4.9/src/zcmds/assets/bell.mp3
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.455713 zcmds-1.4.9/src/zcmds/cmds/
+-rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.9/src/zcmds/cmds/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.499713 zcmds-1.4.9/src/zcmds/cmds/common/
+-rw-rw-rw-   0        0        0       83 2022-02-24 09:10:00.000000 zcmds-1.4.9/src/zcmds/cmds/common/README.md
+-rw-rw-rw-   0        0        0        0 2022-02-21 10:39:02.000000 zcmds-1.4.9/src/zcmds/cmds/common/__init__.py
+-rw-rw-rw-   0        0        0     5364 2023-04-03 19:00:15.000000 zcmds-1.4.9/src/zcmds/cmds/common/askai.py
+-rw-rw-rw-   0        0        0     1561 2023-04-06 17:36:45.000000 zcmds-1.4.9/src/zcmds/cmds/common/audnorm.py
+-rw-rw-rw-   0        0        0      311 2023-01-01 07:58:23.000000 zcmds-1.4.9/src/zcmds/cmds/common/comports.py
+-rw-rw-rw-   0        0        0     4305 2022-12-03 00:29:53.000000 zcmds-1.4.9/src/zcmds/cmds/common/diskaudit.py
+-rw-rw-rw-   0        0        0     1172 2023-03-29 02:40:46.000000 zcmds-1.4.9/src/zcmds/cmds/common/findfiles.py
+-rw-rw-rw-   0        0        0      616 2023-02-02 08:05:19.000000 zcmds-1.4.9/src/zcmds/cmds/common/fixinternet.py
+-rw-rw-rw-   0        0        0     2107 2023-04-03 03:08:28.000000 zcmds-1.4.9/src/zcmds/cmds/common/geninvoice.py
+-rw-rw-rw-   0        0        0     7264 2023-04-02 23:37:24.000000 zcmds-1.4.9/src/zcmds/cmds/common/gitsummary.py
+-rw-rw-rw-   0        0        0     1714 2023-02-27 00:07:25.000000 zcmds-1.4.9/src/zcmds/cmds/common/img2vid.py
+-rw-rw-rw-   0        0        0     3303 2023-02-02 07:49:35.000000 zcmds-1.4.9/src/zcmds/cmds/common/imgai.py
+-rw-rw-rw-   0        0        0     1785 2023-02-02 07:57:46.000000 zcmds-1.4.9/src/zcmds/cmds/common/obs_organize.py
+-rw-rw-rw-   0        0        0      739 2023-01-11 08:02:51.000000 zcmds-1.4.9/src/zcmds/cmds/common/openaicfg.py
+-rw-rw-rw-   0        0        0     2394 2023-02-09 20:17:45.000000 zcmds-1.4.9/src/zcmds/cmds/common/pdf2png.py
+-rw-rw-rw-   0        0        0     1166 2023-03-30 01:50:51.000000 zcmds-1.4.9/src/zcmds/cmds/common/pdf2txt.py
+-rw-rw-rw-   0        0        0      556 2023-03-24 04:23:48.000000 zcmds-1.4.9/src/zcmds/cmds/common/printenv.py
+-rw-rw-rw-   0        0        0      756 2023-04-04 04:43:30.000000 zcmds-1.4.9/src/zcmds/cmds/common/say.py
+-rw-rw-rw-   0        0        0      119 2022-02-21 05:10:16.000000 zcmds-1.4.9/src/zcmds/cmds/common/search_and_replace.py
+-rw-rw-rw-   0        0        0      108 2022-02-21 05:10:10.000000 zcmds-1.4.9/src/zcmds/cmds/common/search_in_files.py
+-rw-rw-rw-   0        0        0       44 2022-03-31 06:58:04.000000 zcmds-1.4.9/src/zcmds/cmds/common/sharedir.py
+-rw-rw-rw-   0        0        0     1986 2023-03-23 20:09:17.000000 zcmds-1.4.9/src/zcmds/cmds/common/stereo2mono.py
+-rw-rw-rw-   0        0        0     1340 2022-05-20 06:00:29.000000 zcmds-1.4.9/src/zcmds/cmds/common/vid2gif.py
+-rw-rw-rw-   0        0        0     1830 2022-03-10 02:29:32.000000 zcmds-1.4.9/src/zcmds/cmds/common/vid2jpg.py
+-rw-rw-rw-   0        0        0     1128 2023-04-06 18:03:51.000000 zcmds-1.4.9/src/zcmds/cmds/common/vid2mp3.py
+-rw-rw-rw-   0        0        0     1333 2022-11-05 02:45:38.000000 zcmds-1.4.9/src/zcmds/cmds/common/vid2mp4.py
+-rw-rw-rw-   0        0        0     1080 2022-08-16 20:18:02.000000 zcmds-1.4.9/src/zcmds/cmds/common/vid2webm.py
+-rw-rw-rw-   0        0        0     3397 2023-04-06 18:04:01.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidcat.py
+-rw-rw-rw-   0        0        0     4891 2022-11-10 05:10:07.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidclip.py
+-rw-rw-rw-   0        0        0     1984 2022-02-24 06:01:55.000000 zcmds-1.4.9/src/zcmds/cmds/common/viddur.py
+-rw-rw-rw-   0        0        0     3533 2023-01-01 07:59:58.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidhero.py
+-rw-rw-rw-   0        0        0     5987 2023-03-14 20:56:14.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidinfo.py
+-rw-rw-rw-   0        0        0     1242 2022-09-03 19:04:52.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidlist.py
+-rw-rw-rw-   0        0        0     2777 2022-09-03 19:04:52.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidmatrix.py
+-rw-rw-rw-   0        0        0     1705 2022-11-09 03:22:17.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidmute.py
+-rw-rw-rw-   0        0        0     1688 2023-03-23 20:09:17.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidshrink.py
+-rw-rw-rw-   0        0        0     1726 2023-02-26 19:57:37.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidspeed.py
+-rw-rw-rw-   0        0        0     1807 2022-07-27 02:41:03.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidvol.py
+-rw-rw-rw-   0        0        0     5750 2023-04-03 19:35:12.000000 zcmds-1.4.9/src/zcmds/cmds/common/vidwebmaster.py
+-rw-rw-rw-   0        0        0     3408 2023-03-24 04:25:59.000000 zcmds-1.4.9/src/zcmds/cmds/common/whichall.py
+-rw-rw-rw-   0        0        0      933 2023-03-23 20:09:17.000000 zcmds-1.4.9/src/zcmds/cmds/common/zcmds_main.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.501712 zcmds-1.4.9/src/zcmds/cmds/darwin/
+-rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.9/src/zcmds/cmds/darwin/__init__.py
+-rw-rw-rw-   0        0        0     3505 2022-11-04 21:13:40.000000 zcmds-1.4.9/src/zcmds/cmds/darwin/test_net_connection.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.504712 zcmds-1.4.9/src/zcmds/cmds/linux/
+-rw-rw-rw-   0        0        0       34 2022-02-21 09:21:39.000000 zcmds-1.4.9/src/zcmds/cmds/linux/TODO
+-rw-rw-rw-   0        0        0        0 2022-02-21 10:38:44.000000 zcmds-1.4.9/src/zcmds/cmds/linux/__init__.py
+-rw-rw-rw-   0        0        0      366 2023-04-02 09:48:39.000000 zcmds-1.4.9/src/zcmds/cmds.py
+-rw-rw-rw-   0        0        0     1792 2023-04-04 01:35:43.000000 zcmds-1.4.9/src/zcmds/cmds.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.505713 zcmds-1.4.9/src/zcmds/install/
+-rw-rw-rw-   0        0        0        0 2022-02-21 03:22:36.000000 zcmds-1.4.9/src/zcmds/install/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.508714 zcmds-1.4.9/src/zcmds/install/darwin/
+-rw-rw-rw-   0        0        0        0 2022-02-24 11:15:15.000000 zcmds-1.4.9/src/zcmds/install/darwin/__init__.py
+-rw-rw-rw-   0        0        0     1438 2022-07-27 03:33:16.000000 zcmds-1.4.9/src/zcmds/install/darwin/darwin_update.py
+-rw-rw-rw-   0        0        0      617 2022-02-21 07:57:18.000000 zcmds-1.4.9/src/zcmds/install/darwin/macOS_key_bindings.dict
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.518715 zcmds-1.4.9/src/zcmds/util/
+-rw-rw-rw-   0        0        0        0 2022-02-21 05:09:08.000000 zcmds-1.4.9/src/zcmds/util/__init__.py
+-rw-rw-rw-   0        0        0     1097 2023-04-02 22:01:35.000000 zcmds-1.4.9/src/zcmds/util/config.py
+-rw-rw-rw-   0        0        0     1710 2023-03-31 05:34:41.000000 zcmds-1.4.9/src/zcmds/util/file_search_and_replacer.py
+-rw-rw-rw-   0        0        0     1063 2023-03-31 05:28:50.000000 zcmds-1.4.9/src/zcmds/util/file_searcher.py
+-rw-rw-rw-   0        0        0     4309 2023-04-02 06:56:44.000000 zcmds-1.4.9/src/zcmds/util/fileutils.py
+-rw-rw-rw-   0        0        0      669 2022-02-21 05:08:59.000000 zcmds-1.4.9/src/zcmds/util/index_all_files.py
+-rw-rw-rw-   0        0        0      381 2023-04-03 18:54:53.000000 zcmds-1.4.9/src/zcmds/util/prompt_input.py
+-rw-rw-rw-   0        0        0      532 2023-04-03 19:36:05.000000 zcmds-1.4.9/src/zcmds/util/say.py
+-rw-rw-rw-   0        0        0      249 2023-02-02 07:49:35.000000 zcmds-1.4.9/src/zcmds/util/sound.py
+-rw-rw-rw-   0        0        0      147 2023-04-06 18:04:23.000000 zcmds-1.4.9/src/zcmds/version.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.453714 zcmds-1.4.9/src/zcmds.egg-info/
+-rw-rw-rw-   0        0        0     7554 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2691 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0     1734 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      223 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        6 2023-04-06 18:07:06.000000 zcmds-1.4.9/src/zcmds.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 18:07:06.521713 zcmds-1.4.9/tests/
+-rw-rw-rw-   0        0        0      876 2022-11-05 20:55:29.000000 zcmds-1.4.9/tests/test_main.py
+-rw-rw-rw-   0        0        0      260 2023-02-02 07:49:35.000000 zcmds-1.4.9/tests/test_sound.py
+-rw-rw-rw-   0        0        0      746 2023-01-03 06:43:04.000000 zcmds-1.4.9/tests/test_version.py
+-rw-rw-rw-   0        0        0      451 2023-02-02 07:49:35.000000 zcmds-1.4.9/tox.ini
+-rw-rw-rw-   0        0        0      275 2023-01-01 07:58:23.000000 zcmds-1.4.9/upload_package.sh
```

### Comparing `zcmds-1.4.8/.github/workflows/lint.yml` & `zcmds-1.4.9/.github/workflows/lint.yml`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.github/workflows/push_macos.yml` & `zcmds-1.4.9/.github/workflows/push_macos.yml`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.github/workflows/push_ubuntu.yml` & `zcmds-1.4.9/.github/workflows/push_ubuntu.yml`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.github/workflows/push_win.yml` & `zcmds-1.4.9/.github/workflows/push_win.yml`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.gitignore` & `zcmds-1.4.9/.gitignore`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.pylintrc` & `zcmds-1.4.9/.pylintrc`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/.vscode/settings.json` & `zcmds-1.4.9/.vscode/settings.json`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/LICENSE` & `zcmds-1.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/PKG-INFO` & `zcmds-1.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zcmds
-Version: 1.4.8
+Version: 1.4.9
 Summary: Cross platform(ish) productivity commands written in python.
 Home-page: https://github.com/zackees/zcmds
 Maintainer: Zachary Vorhies
 License: BSD 3-Clause License
 Keywords: zcmds
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
@@ -116,14 +116,15 @@
 # Note:
 
 Running tox will install hooks into the .tox directory. Keep this in my if you are developing.
 TODO: Add a cleanup function to undo this.
 
 # Release Notes
   
+  * 1.4.8: `audnorm` now encodes in mp3 format (improves compatibility). vid2mp3 now allows `--normalize`
   * 1.4.7: Fixes broken build.
   * 1.4.6: Adds `say` command to speak out the text you give the program
   * 1.4.5: Adds saved settings for gitsummary
   * 1.4.4: Adds `pdf2txt` command
   * 1.4.3: Adds `gitsummary` command
   * 1.4.2: Bump up zcmds_win32 to 1.0.17
   * 1.4.1: Adds 'whichall' command
```

### Comparing `zcmds-1.4.8/README.md` & `zcmds-1.4.9/src/zcmds.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,7 +1,20 @@
+Metadata-Version: 2.1
+Name: zcmds
+Version: 1.4.9
+Summary: Cross platform(ish) productivity commands written in python.
+Home-page: https://github.com/zackees/zcmds
+Maintainer: Zachary Vorhies
+License: BSD 3-Clause License
+Keywords: zcmds
+Classifier: Programming Language :: Python :: 3
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
 # zcmds
 Cross platform(ish) productivity commands written in python. Tools for doing video manipulation, searching through files and other things. On Windows ls, rm and other common unix file commands are installed.
 
 [![Actions Status](https://github.com/zackees/zcmds/workflows/MacOS_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_macos.yml)
 [![Actions Status](https://github.com/zackees/zcmds/workflows/Win_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_win.yml)
 [![Actions Status](https://github.com/zackees/zcmds/workflows/Ubuntu_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_ubuntu.yml)
 
@@ -103,14 +116,15 @@
 # Note:
 
 Running tox will install hooks into the .tox directory. Keep this in my if you are developing.
 TODO: Add a cleanup function to undo this.
 
 # Release Notes
   
+  * 1.4.8: `audnorm` now encodes in mp3 format (improves compatibility). vid2mp3 now allows `--normalize`
   * 1.4.7: Fixes broken build.
   * 1.4.6: Adds `say` command to speak out the text you give the program
   * 1.4.5: Adds saved settings for gitsummary
   * 1.4.4: Adds `pdf2txt` command
   * 1.4.3: Adds `gitsummary` command
   * 1.4.2: Bump up zcmds_win32 to 1.0.17
   * 1.4.1: Adds 'whichall' command
```

### Comparing `zcmds-1.4.8/make_venv.py` & `zcmds-1.4.9/make_venv.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/setup.py` & `zcmds-1.4.9/setup.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/assets/bell.mp3` & `zcmds-1.4.9/src/zcmds/assets/bell.mp3`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/askai.py` & `zcmds-1.4.9/src/zcmds/cmds/common/askai.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/audnorm.py` & `zcmds-1.4.9/src/zcmds/cmds/common/audnorm.py`

 * *Files 1% similar despite different names*

```diff
@@ -37,14 +37,14 @@
     args = parser.parse_args()
     path = args.vidfile or input("in vid file: ")
     out = args.out or input("out vid file: ")
     if len(os.path.dirname(out)):
         os.makedirs(os.path.dirname(out), exist_ok=True)
     assert _is_media_file(path), f"{path} is not a media file"
     add_paths(weak=True)
-    cmd = f'ffmpeg-normalize -f "{path}" -o "{out}" -c:a aac -b:a 192k'
+    cmd = f'ffmpeg-normalize -f "{path}" -o "{out}" -c:a libmp3lame -b:a 192k'
     print(f"Executing:\n  {cmd}")
     os.system(cmd)
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/diskaudit.py` & `zcmds-1.4.9/src/zcmds/cmds/common/diskaudit.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/findfiles.py` & `zcmds-1.4.9/src/zcmds/cmds/common/findfiles.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/fixinternet.py` & `zcmds-1.4.9/src/zcmds/cmds/common/fixinternet.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/geninvoice.py` & `zcmds-1.4.9/src/zcmds/cmds/common/geninvoice.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/gitsummary.py` & `zcmds-1.4.9/src/zcmds/cmds/common/gitsummary.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/img2vid.py` & `zcmds-1.4.9/src/zcmds/cmds/common/img2vid.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/imgai.py` & `zcmds-1.4.9/src/zcmds/cmds/common/imgai.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/obs_organize.py` & `zcmds-1.4.9/src/zcmds/cmds/common/obs_organize.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/openaicfg.py` & `zcmds-1.4.9/src/zcmds/cmds/common/openaicfg.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/pdf2png.py` & `zcmds-1.4.9/src/zcmds/cmds/common/pdf2png.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/pdf2txt.py` & `zcmds-1.4.9/src/zcmds/cmds/common/pdf2txt.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/printenv.py` & `zcmds-1.4.9/src/zcmds/cmds/common/printenv.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/say.py` & `zcmds-1.4.9/src/zcmds/cmds/common/say.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/stereo2mono.py` & `zcmds-1.4.9/src/zcmds/cmds/common/stereo2mono.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vid2gif.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vid2gif.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vid2jpg.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vid2jpg.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vid2mp4.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vid2mp4.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vid2webm.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vid2webm.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidcat.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidcat.py`

 * *Files 1% similar despite different names*

```diff
@@ -76,15 +76,15 @@
         cmd = f'static_ffmpeg -f concat -safe 0 -i input.txt -c copy "{os.path.abspath(outname)}"'
 
         rtn, _, _ = exec(cmd)
         if rtn != 0:
             print(f"{__file__}: WARNING: '{cmd}' returned code {rtn}")
 
 
-def main():
+def main() -> int:
     parser = argparse.ArgumentParser(
         description="Concatenates videos by encoding them to the same resolution.\n",
         formatter_class=argparse.RawDescriptionHelpFormatter,
     )
     parser.add_argument("input", help="input", nargs="+")
     parser.add_argument("--outname", help="output name of the file", required=True)
     parser.add_argument(
@@ -93,11 +93,12 @@
     parser.add_argument("--height", help="height of the output video, e.g 1080 = 1080p")
     args = parser.parse_args()
     infiles = args.input
     resolution: Resolution = get_highest_resolution(infiles)
     print(f"Highest resolution: {resolution.width}x{resolution.height}")
     concatenate_videos(infiles, args.outname, resolution, args.crf)
     print(f"Concatenated videos saved as {args.outname}")
+    return 0
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidclip.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidclip.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/viddur.py` & `zcmds-1.4.9/src/zcmds/cmds/common/viddur.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidhero.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidhero.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidinfo.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidinfo.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidlist.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidlist.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidmatrix.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidmatrix.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidmute.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidmute.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidshrink.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidshrink.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidspeed.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidspeed.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidvol.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidvol.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/vidwebmaster.py` & `zcmds-1.4.9/src/zcmds/cmds/common/vidwebmaster.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/whichall.py` & `zcmds-1.4.9/src/zcmds/cmds/common/whichall.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/common/zcmds_main.py` & `zcmds-1.4.9/src/zcmds/cmds/common/zcmds_main.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds/darwin/test_net_connection.py` & `zcmds-1.4.9/src/zcmds/cmds/darwin/test_net_connection.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/cmds.txt` & `zcmds-1.4.9/src/zcmds/cmds.txt`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/install/darwin/darwin_update.py` & `zcmds-1.4.9/src/zcmds/install/darwin/darwin_update.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/install/darwin/macOS_key_bindings.dict` & `zcmds-1.4.9/src/zcmds/install/darwin/macOS_key_bindings.dict`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/config.py` & `zcmds-1.4.9/src/zcmds/util/config.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/file_search_and_replacer.py` & `zcmds-1.4.9/src/zcmds/util/file_search_and_replacer.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/file_searcher.py` & `zcmds-1.4.9/src/zcmds/util/file_searcher.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/fileutils.py` & `zcmds-1.4.9/src/zcmds/util/fileutils.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/index_all_files.py` & `zcmds-1.4.9/src/zcmds/util/index_all_files.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds/util/say.py` & `zcmds-1.4.9/src/zcmds/util/say.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds.egg-info/PKG-INFO` & `zcmds-1.4.9/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,20 +1,7 @@
-Metadata-Version: 2.1
-Name: zcmds
-Version: 1.4.8
-Summary: Cross platform(ish) productivity commands written in python.
-Home-page: https://github.com/zackees/zcmds
-Maintainer: Zachary Vorhies
-License: BSD 3-Clause License
-Keywords: zcmds
-Classifier: Programming Language :: Python :: 3
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
 # zcmds
 Cross platform(ish) productivity commands written in python. Tools for doing video manipulation, searching through files and other things. On Windows ls, rm and other common unix file commands are installed.
 
 [![Actions Status](https://github.com/zackees/zcmds/workflows/MacOS_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_macos.yml)
 [![Actions Status](https://github.com/zackees/zcmds/workflows/Win_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_win.yml)
 [![Actions Status](https://github.com/zackees/zcmds/workflows/Ubuntu_Tests/badge.svg)](https://github.com/zackees/zcmds/actions/workflows/push_ubuntu.yml)
 
@@ -116,14 +103,15 @@
 # Note:
 
 Running tox will install hooks into the .tox directory. Keep this in my if you are developing.
 TODO: Add a cleanup function to undo this.
 
 # Release Notes
   
+  * 1.4.8: `audnorm` now encodes in mp3 format (improves compatibility). vid2mp3 now allows `--normalize`
   * 1.4.7: Fixes broken build.
   * 1.4.6: Adds `say` command to speak out the text you give the program
   * 1.4.5: Adds saved settings for gitsummary
   * 1.4.4: Adds `pdf2txt` command
   * 1.4.3: Adds `gitsummary` command
   * 1.4.2: Bump up zcmds_win32 to 1.0.17
   * 1.4.1: Adds 'whichall' command
```

### Comparing `zcmds-1.4.8/src/zcmds.egg-info/SOURCES.txt` & `zcmds-1.4.9/src/zcmds.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/src/zcmds.egg-info/entry_points.txt` & `zcmds-1.4.9/src/zcmds.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/tests/test_main.py` & `zcmds-1.4.9/tests/test_main.py`

 * *Files identical despite different names*

### Comparing `zcmds-1.4.8/tests/test_version.py` & `zcmds-1.4.9/tests/test_version.py`

 * *Files identical despite different names*

