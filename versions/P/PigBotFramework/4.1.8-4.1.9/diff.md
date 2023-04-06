# Comparing `tmp/PigBotFramework-4.1.8.tar.gz` & `tmp/PigBotFramework-4.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/PigBotFramework-4.1.8.tar", last modified: Sun Apr  2 07:50:21 2023, max compression
+gzip compressed data, was "dist/PigBotFramework-4.1.9.tar", last modified: Wed Apr  5 14:11:51 2023, max compression
```

## Comparing `PigBotFramework-4.1.8.tar` & `PigBotFramework-4.1.9.tar`

### file list

```diff
@@ -1,58 +1,63 @@
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.097444 PigBotFramework-4.1.8/
--rw-rw-r--   0 root         (0) root         (0)     2385 2023-04-02 07:50:21.097444 PigBotFramework-4.1.8/PKG-INFO
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.070443 PigBotFramework-4.1.8/PigBotFramework.egg-info/
--rw-rw-r--   0 root         (0) root         (0)     2385 2023-04-02 07:50:20.000000 PigBotFramework-4.1.8/PigBotFramework.egg-info/PKG-INFO
--rw-rw-r--   0 root         (0) root         (0)     1232 2023-04-02 07:50:21.000000 PigBotFramework-4.1.8/PigBotFramework.egg-info/SOURCES.txt
--rw-rw-r--   0 root         (0) root         (0)        1 2023-04-02 07:50:20.000000 PigBotFramework-4.1.8/PigBotFramework.egg-info/dependency_links.txt
--rw-rw-r--   0 root         (0) root         (0)      485 2023-04-02 07:50:20.000000 PigBotFramework-4.1.8/PigBotFramework.egg-info/requires.txt
--rw-rw-r--   0 root         (0) root         (0)        4 2023-04-02 07:50:20.000000 PigBotFramework-4.1.8/PigBotFramework.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1507 2023-03-18 09:09:55.000000 PigBotFramework-4.1.8/README.md
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.070443 PigBotFramework-4.1.8/pbf/
--rw-rw-r--   0 root         (0) root         (0)       40 2023-04-02 07:49:52.000000 PigBotFramework-4.1.8/pbf/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.076443 PigBotFramework-4.1.8/pbf/controller/
--rw-r--r--   0 root         (0) root         (0)     2410 2023-04-01 15:32:07.000000 PigBotFramework-4.1.8/pbf/controller/Banwords.py
--rw-r--r--   0 root         (0) root         (0)     1431 2023-04-01 15:27:03.000000 PigBotFramework-4.1.8/pbf/controller/Cache.py
--rw-r--r--   0 root         (0) root         (0)     8715 2023-04-01 15:25:49.000000 PigBotFramework-4.1.8/pbf/controller/Client.py
--rw-rw-rw-   0 root         (0) root         (0)     1681 2023-04-01 15:25:24.000000 PigBotFramework-4.1.8/pbf/controller/CommandListener.py
--rw-r--r--   0 root         (0) root         (0)    20818 2023-04-02 07:50:14.000000 PigBotFramework-4.1.8/pbf/controller/Handler.py
--rw-r--r--   0 root         (0) root         (0)     1226 2023-04-02 01:46:13.000000 PigBotFramework-4.1.8/pbf/controller/Logger.py
--rw-r--r--   0 root         (0) root         (0)     3542 2023-04-01 15:24:35.000000 PigBotFramework-4.1.8/pbf/controller/Menu.py
--rw-rw-rw-   0 root         (0) root         (0)     2088 2023-04-01 15:24:10.000000 PigBotFramework-4.1.8/pbf/controller/Mysql.py
--rw-rw-r--   0 root         (0) root         (0)     6318 2023-04-01 15:31:36.000000 PigBotFramework-4.1.8/pbf/controller/PBF.py
--rw-r--r--   0 root         (0) root         (0)     1727 2023-04-01 02:31:46.000000 PigBotFramework-4.1.8/pbf/controller/PbfStruct.py
--rw-r--r--   0 root         (0) root         (0)     2755 2023-04-02 07:49:43.000000 PigBotFramework-4.1.8/pbf/controller/Regex.py
--rw-rw-r--   0 root         (0) root         (0)        0 2023-04-01 15:31:31.000000 PigBotFramework-4.1.8/pbf/controller/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.077443 PigBotFramework-4.1.8/pbf/driver/
--rw-rw-r--   0 root         (0) root         (0)    16343 2023-04-02 02:06:30.000000 PigBotFramework-4.1.8/pbf/driver/Fastapi.py
--rw-rw-r--   0 root         (0) root         (0)        0 2023-04-01 01:22:08.000000 PigBotFramework-4.1.8/pbf/driver/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.077443 PigBotFramework-4.1.8/pbf/model/
--rw-r--r--   0 root         (0) root         (0)     8862 2023-04-01 15:23:23.000000 PigBotFramework-4.1.8/pbf/model/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.081443 PigBotFramework-4.1.8/pbf/statement/
--rwxr-xr-x   0 root         (0) root         (0)      160 2023-04-01 15:28:24.000000 PigBotFramework-4.1.8/pbf/statement/AtStatement.py
--rw-r--r--   0 root         (0) root         (0)      167 2023-04-01 15:28:36.000000 PigBotFramework-4.1.8/pbf/statement/FaceStatement.py
--rwxr-xr-x   0 root         (0) root         (0)      521 2023-04-01 15:29:33.000000 PigBotFramework-4.1.8/pbf/statement/ImageStatement.py
--rw-rw-rw-   0 root         (0) root         (0)      193 2023-04-01 15:28:44.000000 PigBotFramework-4.1.8/pbf/statement/JsonStatement.py
--rw-r--r--   0 root         (0) root         (0)      718 2023-04-01 15:29:19.000000 PigBotFramework-4.1.8/pbf/statement/TextStatement.py
--rw-rw-rw-   0 root         (0) root         (0)      156 2023-04-01 15:28:58.000000 PigBotFramework-4.1.8/pbf/statement/XmlStatement.py
--rw-r--r--   0 root         (0) root         (0)      795 2023-02-15 12:05:54.000000 PigBotFramework-4.1.8/pbf/statement/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.082443 PigBotFramework-4.1.8/pbf/utils/
--rw-r--r--   0 root         (0) root         (0)     1863 2023-04-01 15:23:05.000000 PigBotFramework-4.1.8/pbf/utils/CQCode.py
--rw-r--r--   0 root         (0) root         (0)     1430 2023-04-01 15:22:56.000000 PigBotFramework-4.1.8/pbf/utils/Coin.py
--rw-r--r--   0 root         (0) root         (0)      594 2023-02-15 13:23:45.000000 PigBotFramework-4.1.8/pbf/utils/RegCmd.py
--rw-rw-rw-   0 root         (0) root         (0)     2944 2023-04-01 15:22:32.000000 PigBotFramework-4.1.8/pbf/utils/__init__.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.084443 PigBotFramework-4.1.8/pbf/utils/nsfw/
--rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:14.000000 PigBotFramework-4.1.8/pbf/utils/nsfw/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1672 2023-02-03 13:45:14.000000 PigBotFramework-4.1.8/pbf/utils/nsfw/classify_nsfw.py
--rwxrwxrwx   0 root         (0) root         (0)     4492 2023-02-03 13:45:14.000000 PigBotFramework-4.1.8/pbf/utils/nsfw/image_utils.py
--rwxrwxrwx   0 root         (0) root         (0)    10395 2023-02-03 13:45:14.000000 PigBotFramework-4.1.8/pbf/utils/nsfw/model.py
-drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-02 07:50:21.096444 PigBotFramework-4.1.8/pbf/utils/pillow/
--rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/__init__.py
--rw-r--r--   0 root         (0) root         (0)    20265 2023-02-18 08:32:47.000000 PigBotFramework-4.1.8/pbf/utils/pillow/build_image.py
--rwxrwxrwx   0 root         (0) root         (0)      611 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/config.py
--rw-r--r--   0 root         (0) root         (0)     7048 2023-02-18 05:29:52.000000 PigBotFramework-4.1.8/pbf/utils/pillow/fonts.py
--rwxr-xr-x   0 root         (0) root         (0)     3555 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/gradient.py
--rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/main.py
--rwxrwxrwx   0 root         (0) root         (0)    15847 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/text2image.py
--rwxrwxrwx   0 root         (0) root         (0)     1062 2023-02-03 13:45:26.000000 PigBotFramework-4.1.8/pbf/utils/pillow/types.py
--rw-rw-r--   0 root         (0) root         (0)       38 2023-04-02 07:50:21.097444 PigBotFramework-4.1.8/setup.cfg
--rw-rw-r--   0 root         (0) root         (0)     3809 2023-04-02 01:54:59.000000 PigBotFramework-4.1.8/setup.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.946886 PigBotFramework-4.1.9/
+-rw-rw-r--   0 root         (0) root         (0)     2385 2023-04-05 14:11:51.945886 PigBotFramework-4.1.9/PKG-INFO
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.932886 PigBotFramework-4.1.9/PigBotFramework.egg-info/
+-rw-rw-r--   0 root         (0) root         (0)     2385 2023-04-05 14:11:51.000000 PigBotFramework-4.1.9/PigBotFramework.egg-info/PKG-INFO
+-rw-rw-r--   0 root         (0) root         (0)     1378 2023-04-05 14:11:51.000000 PigBotFramework-4.1.9/PigBotFramework.egg-info/SOURCES.txt
+-rw-rw-r--   0 root         (0) root         (0)        1 2023-04-05 14:11:51.000000 PigBotFramework-4.1.9/PigBotFramework.egg-info/dependency_links.txt
+-rw-rw-r--   0 root         (0) root         (0)      485 2023-04-05 14:11:51.000000 PigBotFramework-4.1.9/PigBotFramework.egg-info/requires.txt
+-rw-rw-r--   0 root         (0) root         (0)        4 2023-04-05 14:11:51.000000 PigBotFramework-4.1.9/PigBotFramework.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     1507 2023-03-18 09:09:55.000000 PigBotFramework-4.1.9/README.md
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.932886 PigBotFramework-4.1.9/pbf/
+-rw-rw-r--   0 root         (0) root         (0)       40 2023-04-05 14:11:46.000000 PigBotFramework-4.1.9/pbf/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.936886 PigBotFramework-4.1.9/pbf/controller/
+-rw-r--r--   0 root         (0) root         (0)     2410 2023-04-01 15:32:07.000000 PigBotFramework-4.1.9/pbf/controller/Banwords.py
+-rw-r--r--   0 root         (0) root         (0)     1431 2023-04-01 15:27:03.000000 PigBotFramework-4.1.9/pbf/controller/Cache.py
+-rw-r--r--   0 root         (0) root         (0)     8763 2023-04-05 11:44:25.000000 PigBotFramework-4.1.9/pbf/controller/Client.py
+-rw-rw-rw-   0 root         (0) root         (0)     1681 2023-04-01 15:25:24.000000 PigBotFramework-4.1.9/pbf/controller/CommandListener.py
+-rw-r--r--   0 root         (0) root         (0)    16382 2023-04-05 12:27:39.000000 PigBotFramework-4.1.9/pbf/controller/Handler.py
+-rw-r--r--   0 root         (0) root         (0)     1226 2023-04-02 01:46:13.000000 PigBotFramework-4.1.9/pbf/controller/Logger.py
+-rw-r--r--   0 root         (0) root         (0)     3674 2023-04-05 12:26:58.000000 PigBotFramework-4.1.9/pbf/controller/Menu.py
+-rw-rw-rw-   0 root         (0) root         (0)     2006 2023-04-05 12:18:37.000000 PigBotFramework-4.1.9/pbf/controller/Mysql.py
+-rw-rw-r--   0 root         (0) root         (0)     6318 2023-04-01 15:31:36.000000 PigBotFramework-4.1.9/pbf/controller/PBF.py
+-rw-r--r--   0 root         (0) root         (0)     1727 2023-04-01 02:31:46.000000 PigBotFramework-4.1.9/pbf/controller/PbfStruct.py
+-rw-r--r--   0 root         (0) root         (0)     2755 2023-04-02 07:49:43.000000 PigBotFramework-4.1.9/pbf/controller/Regex.py
+-rw-rw-r--   0 root         (0) root         (0)        0 2023-04-01 15:31:31.000000 PigBotFramework-4.1.9/pbf/controller/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.936886 PigBotFramework-4.1.9/pbf/driver/
+-rw-rw-r--   0 root         (0) root         (0)    16343 2023-04-02 02:06:30.000000 PigBotFramework-4.1.9/pbf/driver/Fastapi.py
+-rw-rw-r--   0 root         (0) root         (0)        0 2023-04-01 01:22:08.000000 PigBotFramework-4.1.9/pbf/driver/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.938886 PigBotFramework-4.1.9/pbf/model/
+-rw-rw-r--   0 root         (0) root         (0)      447 2023-04-05 10:10:23.000000 PigBotFramework-4.1.9/pbf/model/BlackListModel.py
+-rw-rw-r--   0 root         (0) root         (0)      332 2023-04-05 11:45:27.000000 PigBotFramework-4.1.9/pbf/model/BotPluginsModel.py
+-rw-rw-r--   0 root         (0) root         (0)     1958 2023-04-05 10:07:45.000000 PigBotFramework-4.1.9/pbf/model/BotSettingsModel.py
+-rw-rw-r--   0 root         (0) root         (0)      497 2023-04-05 11:38:17.000000 PigBotFramework-4.1.9/pbf/model/GroupSettingsModel.py
+-rw-rw-r--   0 root         (0) root         (0)      699 2023-04-05 12:27:31.000000 PigBotFramework-4.1.9/pbf/model/UserInfoModel.py
+-rw-r--r--   0 root         (0) root         (0)     8620 2023-04-05 12:20:59.000000 PigBotFramework-4.1.9/pbf/model/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.940886 PigBotFramework-4.1.9/pbf/statement/
+-rwxr-xr-x   0 root         (0) root         (0)      160 2023-04-01 15:28:24.000000 PigBotFramework-4.1.9/pbf/statement/AtStatement.py
+-rw-r--r--   0 root         (0) root         (0)      167 2023-04-01 15:28:36.000000 PigBotFramework-4.1.9/pbf/statement/FaceStatement.py
+-rwxr-xr-x   0 root         (0) root         (0)      521 2023-04-01 15:29:33.000000 PigBotFramework-4.1.9/pbf/statement/ImageStatement.py
+-rw-rw-rw-   0 root         (0) root         (0)      193 2023-04-01 15:28:44.000000 PigBotFramework-4.1.9/pbf/statement/JsonStatement.py
+-rw-r--r--   0 root         (0) root         (0)      718 2023-04-01 15:29:19.000000 PigBotFramework-4.1.9/pbf/statement/TextStatement.py
+-rw-rw-rw-   0 root         (0) root         (0)      156 2023-04-01 15:28:58.000000 PigBotFramework-4.1.9/pbf/statement/XmlStatement.py
+-rw-r--r--   0 root         (0) root         (0)      795 2023-02-15 12:05:54.000000 PigBotFramework-4.1.9/pbf/statement/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.941886 PigBotFramework-4.1.9/pbf/utils/
+-rw-r--r--   0 root         (0) root         (0)     1863 2023-04-01 15:23:05.000000 PigBotFramework-4.1.9/pbf/utils/CQCode.py
+-rw-r--r--   0 root         (0) root         (0)     1430 2023-04-01 15:22:56.000000 PigBotFramework-4.1.9/pbf/utils/Coin.py
+-rw-r--r--   0 root         (0) root         (0)      594 2023-02-15 13:23:45.000000 PigBotFramework-4.1.9/pbf/utils/RegCmd.py
+-rw-rw-rw-   0 root         (0) root         (0)     3051 2023-04-05 10:11:07.000000 PigBotFramework-4.1.9/pbf/utils/__init__.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.942886 PigBotFramework-4.1.9/pbf/utils/nsfw/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:14.000000 PigBotFramework-4.1.9/pbf/utils/nsfw/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1672 2023-02-03 13:45:14.000000 PigBotFramework-4.1.9/pbf/utils/nsfw/classify_nsfw.py
+-rwxrwxrwx   0 root         (0) root         (0)     4492 2023-02-03 13:45:14.000000 PigBotFramework-4.1.9/pbf/utils/nsfw/image_utils.py
+-rwxrwxrwx   0 root         (0) root         (0)    10395 2023-02-03 13:45:14.000000 PigBotFramework-4.1.9/pbf/utils/nsfw/model.py
+drwxrwxr-x   0 root         (0) root         (0)        0 2023-04-05 14:11:51.945886 PigBotFramework-4.1.9/pbf/utils/pillow/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    20265 2023-02-18 08:32:47.000000 PigBotFramework-4.1.9/pbf/utils/pillow/build_image.py
+-rwxrwxrwx   0 root         (0) root         (0)      611 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/config.py
+-rw-r--r--   0 root         (0) root         (0)     7048 2023-02-18 05:29:52.000000 PigBotFramework-4.1.9/pbf/utils/pillow/fonts.py
+-rwxr-xr-x   0 root         (0) root         (0)     3555 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/gradient.py
+-rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/main.py
+-rwxrwxrwx   0 root         (0) root         (0)    15847 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/text2image.py
+-rwxrwxrwx   0 root         (0) root         (0)     1062 2023-02-03 13:45:26.000000 PigBotFramework-4.1.9/pbf/utils/pillow/types.py
+-rw-rw-r--   0 root         (0) root         (0)       38 2023-04-05 14:11:51.946886 PigBotFramework-4.1.9/setup.cfg
+-rw-rw-r--   0 root         (0) root         (0)     3809 2023-04-02 08:42:22.000000 PigBotFramework-4.1.9/setup.py
```

### Comparing `PigBotFramework-4.1.8/PKG-INFO` & `PigBotFramework-4.1.9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PigBotFramework
-Version: 4.1.8
+Version: 4.1.9
 Summary: PigBotFramework is a fast, easy-to-use, intelligent robot framework.
 Home-page: https://github.com/PigBotFramework/v4
 Author: XzyStudio
 Author-email: gingmzmzx@gmail.com
 License: MIT
 Description: 
         # 新版本预告： 
@@ -30,12 +30,12 @@
         PBFv4将采用`MSC（Model-Statement-Controller）`模式编写插件，与`MVC`不同之处在于将`View`更改为了`Statement`，不过其作用基本相同。  
         与`MVC`相同，`Model`部分主要控制数据的存取等。插件需要实现一个model类，来实现数据存取。自建的`Model`类需要继承`model.ModelBase`类，并可以轻松实现数据存取。具体详见开发文档。
         自建的`Statement`类也需要继承`statement.Statement`类，具体详见开发文档。
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
```

### Comparing `PigBotFramework-4.1.8/PigBotFramework.egg-info/PKG-INFO` & `PigBotFramework-4.1.9/PigBotFramework.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PigBotFramework
-Version: 4.1.8
+Version: 4.1.9
 Summary: PigBotFramework is a fast, easy-to-use, intelligent robot framework.
 Home-page: https://github.com/PigBotFramework/v4
 Author: XzyStudio
 Author-email: gingmzmzx@gmail.com
 License: MIT
 Description: 
         # 新版本预告： 
@@ -30,12 +30,12 @@
         PBFv4将采用`MSC（Model-Statement-Controller）`模式编写插件，与`MVC`不同之处在于将`View`更改为了`Statement`，不过其作用基本相同。  
         与`MVC`相同，`Model`部分主要控制数据的存取等。插件需要实现一个model类，来实现数据存取。自建的`Model`类需要继承`model.ModelBase`类，并可以轻松实现数据存取。具体详见开发文档。
         自建的`Statement`类也需要继承`statement.Statement`类，具体详见开发文档。
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
```

### Comparing `PigBotFramework-4.1.8/PigBotFramework.egg-info/SOURCES.txt` & `PigBotFramework-4.1.9/PigBotFramework.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -16,14 +16,19 @@
 pbf/controller/Mysql.py
 pbf/controller/PBF.py
 pbf/controller/PbfStruct.py
 pbf/controller/Regex.py
 pbf/controller/__init__.py
 pbf/driver/Fastapi.py
 pbf/driver/__init__.py
+pbf/model/BlackListModel.py
+pbf/model/BotPluginsModel.py
+pbf/model/BotSettingsModel.py
+pbf/model/GroupSettingsModel.py
+pbf/model/UserInfoModel.py
 pbf/model/__init__.py
 pbf/statement/AtStatement.py
 pbf/statement/FaceStatement.py
 pbf/statement/ImageStatement.py
 pbf/statement/JsonStatement.py
 pbf/statement/TextStatement.py
 pbf/statement/XmlStatement.py
```

### Comparing `PigBotFramework-4.1.8/README.md` & `PigBotFramework-4.1.9/README.md`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Banwords.py` & `PigBotFramework-4.1.9/pbf/controller/Banwords.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Cache.py` & `PigBotFramework-4.1.9/pbf/controller/Cache.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Client.py` & `PigBotFramework-4.1.9/pbf/controller/Client.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,29 +5,30 @@
 import random, math, requests, re
 from . import Mysql, Cache
 from urllib.request import urlopen
 from io import BytesIO
 from PIL import Image, ImageFont, ImageDraw, ImageFilter
 from ..utils import Utils
 from ..utils.pillow.build_image import BuildImage, Text2Image
+from ..model.BotSettingsModel import BotSettingsModel
 
 class Client:
     data: Struct = None
     utils: Utils = None
 
     def __init__(self, struct: Struct) -> None:
         self.data = struct
         self.utils = Utils(self.data)
     
     def CallApi(self, api, parms={}, timeout=10):
         botSettings = self.data.botSettings
         if not botSettings:
-            botSettings = Cache.get('botBotconfig').get(self.data.uuid)
+            botSettings = BotSettingsModel(uuid=self.data.uuid)
             self.data.botSettings = botSettings
-        return requests.post(url='{0}/{1}?access_token={2}'.format(botSettings.get('httpurl'), api, botSettings.get('secret')), json=parms, timeout=timeout).json()
+        return requests.post(url='{0}/{1}?access_token={2}'.format(botSettings._get('httpurl'), api, botSettings._get('secret')), json=parms, timeout=timeout).json()
     
     def msg(self, *args, coinFlag=True, insertStrFlag=False, retryFlag=True, translateFlag=True):
         return Msg(self.data, *args, coinFlag=coinFlag, insertStrFlag=insertStrFlag, retryFlag=retryFlag, translateFlag=translateFlag)
 
 class Msg(Client):
     content: list = None
     coinFlag: bool = True
```

### Comparing `PigBotFramework-4.1.8/pbf/controller/CommandListener.py` & `PigBotFramework-4.1.9/pbf/controller/CommandListener.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Handler.py` & `PigBotFramework-4.1.9/pbf/controller/Handler.py`

 * *Files 14% similar despite different names*

```diff
@@ -11,14 +11,19 @@
 from ..statement.FaceStatement import FaceStatement
 from ..statement.AtStatement import AtStatement
 from .Banwords import BanWords
 from .CommandListener import CommandListener
 from .Regex import Regex
 from .Logger import Logger
 from .Menu import Menu
+from ..model.BotPluginsModel import BotPluginsModel
+from ..model.BlackListModel import BlackListModel
+from ..model.BotSettingsModel import BotSettingsModel
+from ..model.GroupSettingsModel import GroupSettingsModel
+from ..model.UserInfoModel import UserInfoModel
 
 def reloadPlugins(flag: bool=False):
     noticeListenerList = []
     requestListenerList = []
     metaListenerList = []
     messageListenerList = []
     ChatterBotListener = [] # 已弃用 ChatterBot监听
@@ -68,24 +73,23 @@
                         requestListenerList.append(cmd)
                     elif cmd.type == 'message':
                         messageListenerList.append(cmd)
         except Exception:
             p(f'An error was made by loading plugins: {i}\n{traceback.format_exc()}')
             pluginsList.remove(i)
     
-    p('commandListenerList', commandListenerList)
-    Cache.connectSql('keywordList', 'SELECT * FROM `botKeyword` WHERE `state` = 0', mapDictToList, 'uuid')
-    Cache.connectSql('botBotconfig', 'SELECT * FROM `botBotconfig`', mapDict, 'uuid')
-    Cache.connectSql('botWeijin', "SELECT * FROM `botWeijin` WHERE `state`=0 or `state`=3;", noMap)
-    Cache.connectSql('botReplace', "SELECT * FROM `botReplace`", noMap)
-    Cache.connectSql('settingName', "SELECT * FROM `botSettingName`", noMap)
-    Cache.connectSql('groupSettings', 'SELECT * FROM `botSettings`', mapDoubleDict, 'qn uuid')
-    Cache.connectSql('userCoin', "SELECT * FROM `botCoin`", mapDict, 'qn')
-    Cache.connectSql('botPluginsList', 'SELECT * FROM `botPlugins`', mapDictToList, 'uuid')
-    Cache.connectSql('globalBanned', "SELECT * FROM `botQuanping`", mapDict, 'qn')
+    # Cache.connectSql('keywordList', 'SELECT * FROM `botKeyword` WHERE `state` = 0', mapDictToList, 'uuid')
+    # Cache.connectSql('botBotconfig', 'SELECT * FROM `botBotconfig`', mapDict, 'uuid')
+    # Cache.connectSql('botWeijin', "SELECT * FROM `botWeijin` WHERE `state`=0 or `state`=3;", noMap)
+    # Cache.connectSql('botReplace', "SELECT * FROM `botReplace`", noMap)
+    # Cache.connectSql('settingName', "SELECT * FROM `botSettingName`", noMap)
+    # Cache.connectSql('groupSettings', 'SELECT * FROM `botSettings`', mapDoubleDict, 'qn uuid')
+    # Cache.connectSql('userCoin', "SELECT * FROM `botCoin`", mapDict, 'qn')
+    # Cache.connectSql('botPluginsList', 'SELECT * FROM `botPlugins`', mapDictToList, 'uuid')
+    # Cache.connectSql('globalBanned', "SELECT * FROM `botQuanping`", mapDict, 'qn')
     loadCache(
         commandModedList = commandModedList,
         commandPluginsList = commandPluginsList,
         commandListenerList = commandListenerList,
         messageListenerList = messageListenerList, 
         metaListenerList = metaListenerList,
         requestListenerList = requestListenerList,
@@ -141,32 +145,35 @@
     if se.get('meta_event_type') == 'heartbeat':
         p('Pass heartbeat event.')
         return None
     
     # 初始化各项
     args = se.get("message").split() if se.get('message') else None # 初始化参数
     messageType = 'cid' if se.get('channel_id') else 'qn' # 消息来源（频道或群组）
-    botSettings = Cache.get('botBotconfig', {}).get(uuid) # 机器人实例设置
-    groupSettings = None if se.get('group_id') == None else Cache.get('groupSettings', {}).get(se.get('group_id'), {}).get(uuid) # 加载群聊设置
+    botSettings = BotSettingsModel(uuid=uuid) # 机器人实例设置
+    groupSettings = GroupSettingsModel(uuid=uuid, qn=se.get('group_id'))
     if se.get('user_id'):
-        userInfo = Cache.get('userCoin', {}).get(se.get('user_id'))
-        userCoin = -1 if userInfo == None else userInfo.get('value')
-        isGlobalBanned = Cache.get('globalBanned', {}).get(se.get('user_id'))
+        userInfo = UserInfoModel(qn=se.get('user_id'), uuid=uuid, value=0)
+        userCoin = userInfo._get('value', -1)
+        isGlobalBanned = BlackListModel(qn=se.get('user_id'), reason='Debug', time=114514, uuid='uuid')
+        if isGlobalBanned.exists == False:
+            isGlobalBanned._delete()
+            del isGlobalBanned
+            isGlobalBanned = None
     else:
         userInfo = None
         userCoin = -1
         isGlobalBanned = None
     
-    pluginsList = Cache.get('botPluginsList', {}).get(uuid)
+    pluginsList = BotPluginsModel(uuid=uuid)._get('data')
     
     struct = Struct(
         args = args,
         messageType = messageType,
         botSettings = botSettings,
-        groupSettings = groupSettings,
         userCoin = userCoin,
         isGlobalBanned = isGlobalBanned,
         userInfo = userInfo,
         pluginsList = pluginsList,
         se = se,
         uuid = uuid,
         message = message,
@@ -176,37 +183,32 @@
     pbf = PBF(struct)
     logger = Logger(struct)
     regex = Regex(struct)
     client = Client(struct)
     banwords = BanWords(struct)
     menu = Menu(struct)
     p('Inited all vars.')
-    
-    if not groupSettings and se.get("group_id") != None: # 初始化群聊设置
-        pbf.groupInit()
-        return 
 
     if isGlobalBanned == None and se.get('group_id') != None:
-        if not groupSettings.get("power", True):
+        if not groupSettings._get("power", True):
             if message == '开机':
-                if se.get('sender').get('role') != 'member' or se.get('user_id') == botSettings.get('owner') or se.get('user_id') == botSettings.get('second_owner'):
-                    groupSettings['power'] = 1
-                    Cache.set('groupSettings', groupSettings)
+                if se.get('sender').get('role') != 'member' or se.get('user_id') == botSettings._get('owner') or se.get('user_id') == botSettings._get('second_owner'):
+                    groupSettings._set(power=1)
                     client.msg(
-                        TextStatement(f'{botSettings.get("name")}开机成功！')
+                        TextStatement(f'{botSettings._get("name")}开机成功！')
                     ).send()
                 else:
                     client.msg(
                         FaceStatement(151),
                         TextStatement('就你？先拿到管理员再说吧！')
                     ).send()
             elif message:
-                if (f'[CQ:at,qq={botSettings.get("myselfqn")}]' in message) or (botSettings.get('name') in message) or ('机器人' in message):
+                if (f'[CQ:at,qq={botSettings._get("myselfqn")}]' in message) or (botSettings._get('name') in message) or ('机器人' in message):
                     client.msg(
-                        TextStatement(f'{botSettings.get("name")}还没有开机哦~', 1),
+                        TextStatement(f'{botSettings._get("name")}还没有开机哦~', 1),
                         TextStatement('发送 开机 可以开启机器人！')
                     ).send()
             banwords.check(False)
             p('Bot is shutdowned.')
             return 
     elif isGlobalBanned != None:
         banwords.check(True)
@@ -236,127 +238,84 @@
             pbf.checkPromiseAndRun(i)
         return 
     
     else:
         for i in Cache.get('messageListenerList', []):
             pbf.checkPromiseAndRun(i)
         
-        if se.get('channel_id') == None and gid != None:
-            # 防刷屏 TODO 该内容最好移动到查建中
-            messagelist = Cache.get('messagelist', [])
-            mlob = utils.findObject('qn', gid, messagelist)
-            mlo = mlob.get('object')
-            if mlo == 404:
-                messagelist.append({'qn':gid, 'uid':uid, 'times':1})
-            else:
-                arrnum = mlob.get('num')
-                if mlo.get('uid') == uid:
-                    if mlo.get('times') >= int(settings.get('AntiswipeScreen')):
-                        messagelist[arrnum]['times'] = 1
-                        if se.get('sender').get('role') == "member":
-                            datajson = client.CallApi('set_group_ban', {"group_id":gid,"user_id":uid,"duration":600})
-                            if datajson['status'] != 'ok':
-                                client.msg(
-                                    FaceStatement(151),
-                                    TextStatement('检测到刷屏，但禁言失败！')
-                                ).send()
-                            else:
-                                client.msg(
-                                    FaceStatement(54),
-                                    TextStatement('检测到刷屏，已禁言！')
-                                ).send()
-                    else:
-                        messagelist[arrnum]['times'] += 1
-                    # 禁言警告
-                    if mlo.get('times') == int(settings.get('AntiswipeScreen'))-1 and se.get('sender').get('role') == "member":
-                        client.msg(
-                            TextStatement('刷屏禁言警告', 1),
-                            TextStatement('请不要连续发送消息超过设定数量！')
-                        ).send()
-                else:
-                    messagelist[arrnum]['times'] = 1
-                    messagelist[arrnum]['uid'] = uid
-            Cache.set('messagelist', messagelist)
-        
         commandPluginsList = Cache.get('commandPluginsList')
         
         p('Handle events finished.')
         # 跟班模式
         only_for_uid = True
         if se.get("group_id"):
-            if botSettings.get("only_for_uid") and botSettings.get("only_for_uid") == uid:
+            if settings._get('only_for_uid') is None:
+                settings._set(only_for_uid=' ')
+            if botSettings._get("only_for_uid") and botSettings._get("only_for_uid") == uid:
                 only_for_uid = False
-            if len(settings.get("only_for_uid")) != 0 and str(uid) in settings.get("only_for_uid").split():
+            if len(settings._get("only_for_uid").split()) != 0 and str(uid) in settings._get("only_for_uid").split():
                 only_for_uid = False
-            if (not botSettings.get("only_for_uid")) and (len(settings.get("only_for_uid")) == 0):
+            if (not botSettings._get("only_for_uid")) and (len(settings._get("only_for_uid")) == 0):
                 only_for_uid = False
             if uid == yamldata.get("chat").get("owner"):
                 only_for_uid = False
         else:
             only_for_uid = False
         
-        if uid != botSettings.get('owner') and se.get('channel_id') == None and gid == None and botSettings.get("reportPrivate"):
+        if uid != botSettings._get('owner') and se.get('channel_id') == None and gid == None and botSettings._get("reportPrivate"):
             client.msg(
                 FaceStatement(151),
                 TextStatement('主人，有人跟我说话话~', 1),
                 TextStatement(f'内容为：{message}', 1),
                 TextStatement(f'回复请对我说：回复|{se.get("user_id")}|{se.get("message_id")}|<回复内容>')
-            ).custom(botSettings.get('owner'))
-            if uid != botSettings.get('second_owner'):
+            ).custom(botSettings._get('owner'))
+            if uid != botSettings._get('second_owner'):
                 client.msg(
                     FaceStatement(151),
                     TextStatement('副主人，有人跟我说话话~', 1),
                     TextStatement(f'内容为：{message}', 1),
                     TextStatement(f'回复请对我说：回复|{se.get("user_id")}|{se.get("message_id")}|<回复内容>')
-                ).custom(botSettings.get('second_owner'))
+                ).custom(botSettings._get('second_owner'))
         
-        if '[CQ:at,qq='+str(botSettings.get('owner'))+']' in message and botSettings.get("reportAt"):
+        if '[CQ:at,qq='+str(botSettings._get('owner'))+']' in message and botSettings._get("reportAt"):
             client.msg(
                 FaceStatement(151),
                 TextStatement('主人，有人艾特你~', 1),
                 TextStatement(f'消息内容：{message}', 1),
                 TextStatement(f'来自群：{gid}', 1),
                 TextStatement(f'来自用户：{uid}')
-            ).custom(botSettings.get('owner'))
+            ).custom(botSettings._get('owner'))
             
-        if '[CQ:at,qq='+str(botSettings.get('second_owner'))+']' in message and botSettings.get("reportAt"):
+        if '[CQ:at,qq='+str(botSettings._get('second_owner'))+']' in message and botSettings._get("reportAt"):
             client.msg(
                 FaceStatement(151),
                 TextStatement('副主人，有人艾特你~', 1),
                 TextStatement(f'消息内容：{message}', 1),
                 TextStatement(f'来自群：{gid}', 1),
                 TextStatement(f'来自用户：{uid}')
-            ).custom(botSettings.get('second_owner'))
+            ).custom(botSettings._get('second_owner'))
         
-        if (f'[CQ:at,qq={botSettings.get("myselfqn")}]' in message) and (userCoin == -1) and not only_for_uid:
+        if (f'[CQ:at,qq={botSettings._get("myselfqn")}]' in message) and (userCoin == -1) and not only_for_uid:
             client.msg(
                 Statement('reply', id=se.get('message_id')),
-                TextStatement(f'{botSettings.get("name")}想起来你还没有注册哦~',1),
+                TextStatement(f'{botSettings._get("name")}想起来你还没有注册哦~',1),
                 TextStatement('发送“注册”可以让机器人认识你啦QAQ')
             ).send()
         
         try:
             cq = CQCode(message).get('file', type='image')
             if len(cq) <= 0:
                 dataa = client.CallApi('ocr_image', {'image':cq[0]})
                 message = ''
                 datajson = dataa.get('data').get('texts')
                 for i in datajson:
                     message += i.get('text')
         except Exception:
             pass
         
-        try:
-            if gid != None:
-                if settings.get('increase_verify') != 0:
-                    if pbf.execPlugin('basic.getVerifyStatus()') == True and '人机验证 ' not in message:
-                        client.CallApi('delete_msg', {'message_id':se.get('message_id')})
-        except Exception:
-            pass
-        
         # 指令监听器
         commandListener = CommandListener(struct)
         if commandListener.get() != 404:
             if message == '退出':
                 commandListener.remove()
                 client.msg(TextStatement('退出！')).send()
                 return True
@@ -385,20 +344,20 @@
             # 检测
             lengthmx = len(content.lstrip().rstrip())
             if message[0:lengthmx] == content.lstrip().rstrip():
                 global noticeFlag
                 noticeFlag = True
             return False
         
-        atStr = '[CQ:at,qq='+str(botSettings.get('myselfqn'))+'] '
+        atStr = '[CQ:at,qq='+str(botSettings._get('myselfqn'))+'] '
         if message[0:len(atStr)] == atStr:
             message = message.replace(atStr, '', 1)
         
-        if settings.get("v_command"):
-            v_command_list = settings.get("v_command").split()
+        if settings._get("v_command"):
+            v_command_list = settings._get("v_command").split()
         else:
             v_command_list = []
         if (not only_for_uid) or (v_command_list):
             for l in pluginsList:
                 if commandPluginsList.get(l.get('path')) == None:
                     continue
                 for i in commandPluginsList.get(l.get('path')):
@@ -410,70 +369,20 @@
                         if (not only_for_uid) or (alia.strip() in v_command_list):
                             if runCommand(i, alia, message):
                                 return
         
         if noticeFlag and not only_for_uid:
             client.msg(TextStatement("请注意指令每一部分之间有一个空格！！！")).send()
         
-        if message[0:10] == '[CQ:reply,' and '撤回' in message:
-            if uid == botSettings.get('owner') or uid == botSettings.get('second_owner') or se.get('sender').get('role') != 'member':
-                reply_id = CQCode(message).get('id', type='reply')
-                client.CallApi('delete_msg', {'message_id':reply_id})
-                client.CallApi('delete_msg', {'message_id':se.get('message_id')})
-                return 
-            else:
-                client.msg(TextStatement('[CQ:face,id=151] 就你？先拿到管理员再说吧！')).send()
-        
-        # 违禁词检查
-        if settings != None:
-            weijinFlag = 1 if settings.get('weijinCheck') else 0
-        else:
-            weijinFlag = 1
-        if banwords.check(weijinFlag) == True and not only_for_uid:
-            return 'OK.'
-        
-        try:
-            # 关键词回复
-            if settings != None:
-                kwFlag = 1 if settings.get('keywordReply') else 0
-            else:
-                kwFlag = 1
-            if kwFlag and not only_for_uid:
-                keywordlist = Cache.get('keywordList').get(uuid, [])
-                for i in keywordlist:
-                    replyFlag = False
-                    if userCoin >= i.get('coin') and (i.get("qn") == 0 or gid == i.get("qn")):
-                        replyFlag = True
-                    if replyFlag == True:
-                        replyKey = regex.replace(i.get('key'))
-                        if regex.pair(replyKey, message):
-                            regex.send(i.get('value'))
-        except Exception:
-            logger.warn(f'{traceback.format_exc()}')
-        
         # 分类菜单
         for i in menu.getModedMenu():
             menuStr = i.replace(' ', '')
             if message[0:len(menuStr)] == menuStr:
                 p(f'Send SingleMenu: {i}')
                 menu.sendSingleMenu(i)
-        
-        # 回复
-        if not only_for_uid:
-            if gid != None or cid != None:
-                if gid != None:
-                    randnum = settings.get('replyPercent')
-                elif cid != None:
-                    randnum = 100
-                rand = random.randint(1, randnum)
-                if (rand == 1) or ('[CQ:at,qq='+str(botSettings.get('myselfqn'))+']' in message):
-                    pbf.data.message = pbf.data.se['message'] = pbf.data.message.replace('[CQ:at,qq='+str(botSettings.get('myselfqn'))+']', "")
-                    pbf.reply()
-            else:
-                pbf.reply()
 
 def loadCache(**kwargs):
     '''在对应键不存在的时候设置缓存'''
     for key, value in kwargs.items():
         if (Cache.get(key) == None):
             Cache.set(key, value)
```

### Comparing `PigBotFramework-4.1.8/pbf/controller/Logger.py` & `PigBotFramework-4.1.9/pbf/controller/Logger.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Menu.py` & `PigBotFramework-4.1.9/pbf/controller/Menu.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 from .PbfStruct import Struct
 from .Client import Client
 from . import Cache
 from ..statement.FaceStatement import FaceStatement
 from ..statement.TextStatement import TextStatement
+from ..model.BotPluginsModel import BotPluginsModel
 
 class Menu:
     data: Struct = None
     client: Client = None
 
     def __init__(self, data: Struct):
         self.data = data
         self.client = Client(data)
     
     def getModedMenu(self):
         pluginsList = Cache.get('commandPluginsList')
-        botPluginsList = Cache.get('botPluginsList').get(self.data.uuid)
+        botPluginsList = BotPluginsModel(uuid=self.data.uuid)._get('data')
+        botPluginsList = botPluginsList if botPluginsList is not None else []
         commandModedList = []
 
         for i in botPluginsList:
             cmds = pluginsList.get(i.get('path'))
             if cmds == None:
                 continue
             for cmd in cmds:
```

### Comparing `PigBotFramework-4.1.8/pbf/controller/Mysql.py` & `PigBotFramework-4.1.9/pbf/controller/Mysql.py`

 * *Files 10% similar despite different names*

```diff
@@ -8,28 +8,28 @@
 
 def selectx(sqlstr, params=(), host=yamldata.get('database').get('dbhost'), user=yamldata.get('database').get('dbuser'), password=yamldata.get('database').get('dbpassword'), database=yamldata.get('database').get('dbname')):
     conn = pymysql.connect(host=host, user=user, password=password, database=database)
     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
     try:
         cursor.execute(sqlstr, params)
     except Exception as e:
-        # self.CrashReport("selectx execute error\nsql: {}\nparams: {}\nerror: {}".format(sqlstr, params, e), "selectx", level="WARNING")
+        print("selectx execute error\nsql: {}\nparams: {}\nerror: {}".format(sqlstr, params, e))
         raise Exception(e)
     result = cursor.fetchall()
     cursor.close()
     conn.close()
     return result
 
 def commonx(sqlstr, params=(), host=yamldata.get('database').get('dbhost'), user=yamldata.get('database').get('dbuser'), password=yamldata.get('database').get('dbpassword'), database=yamldata.get('database').get('dbname')):
     connect = pymysql.connect(host=host, user=user, password=password, database=database)
     cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
     try:
         cursor.execute(sqlstr, params)
     except Exception as e:
-        # self.CrashReport("commonx execute error\nsql: {}\nparams: {}\nerror: {}".format(sqlstr, params, e), "commonx", level="WARNING")
+        print("commonx execute error\nsql: {}\nparams: {}\nerror: {}".format(sqlstr, params, e))
         raise Exception(e)
     connect.commit()
     cursor.close()
     connect.close()
 
 def getConfig(uuid, key, value, template, sql=None):
     if sql == None:
```

### Comparing `PigBotFramework-4.1.8/pbf/controller/PBF.py` & `PigBotFramework-4.1.9/pbf/controller/PBF.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/PbfStruct.py` & `PigBotFramework-4.1.9/pbf/controller/PbfStruct.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/controller/Regex.py` & `PigBotFramework-4.1.9/pbf/controller/Regex.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/driver/Fastapi.py` & `PigBotFramework-4.1.9/pbf/driver/Fastapi.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/model/__init__.py` & `PigBotFramework-4.1.9/pbf/model/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -10,45 +10,50 @@
     sql_whereCase: str = ""
     sql_whereList: list = []
     
     db_table: str = None
     db_perfix: str = "bot_"
     
     col: list = []
-    cache = None
+    cache: dict = []
     map: list = []
     args: list = []
     exists: bool = True
     delFlag: bool = False
     
     format_insert: list = []
     format_update: list = []
     format_delete: bool = False
     format_createTable: list = []
 
+    def __str__(self):
+        return f'<pbf.model.ModelBase {self.db_table}>'
+
     def _getIndexStr(self, i):
         strr: str = f"['{self._c()}']"
         listt: list = self.map
         dictOb = Cache.cacheList
         for l in listt:
-            strr += f"[{eval(str(i.get(l)))}]"
+            ob = i.get(l)
+            strr += f"[\"{ob}\"]" if isinstance(ob, str) else f"[{eval('i.get(l)')}]"
             dictOb = dictOb.get(str(i.get(l)))
             if dictOb == None:
-                exec(f"cache.cacheList{strr} = {'{}'}")
+                exec(f"Cache.cacheList{strr} = {'{}'}")
                 dictOb = {}
             
         return strr
     
     def _getTableName(self):
         return self.db_perfix + self.db_table
         
     def _c(self):
         return "db_" + self._getTableName()
     
     def _getCol(self):
+        self.col = []
         for i in dir(self):
             if i[0:1] == "_" or not callable(getattr(self, i)):
                 continue
             name = i
             i = getattr(self, i)
             desc = i.__doc__
             default = i()
@@ -57,14 +62,21 @@
                 "desc": desc,
                 "name": name,
                 "default": f"`{name}` {default}",
                 "type": _type
             })
     
     def __init__(self, **kwargs):
+        # Init class vars.
+        for i in dir(self):
+            if i[0:1] == "_" or callable(getattr(self, i)):
+                continue
+            varType = type(getattr(self, i))
+            setattr(self, i, varType(getattr(self, i)))
+
         self.args = kwargs
         
         # 初始化数据
         self._getCol()
         self._refresh(insertFlag=True, kwargs=kwargs)
         self._refreshWhereCase()
     
@@ -86,14 +98,15 @@
             self.sql_whereCase += "`{}` = %s".format(i)
             self.sql_whereList.append(self.args.get(i))
     
     def _createTable(self):
         strr: str = ""
         flag: bool = False
         listt: list = self.col + self.format_createTable
+
         for i in listt:
             if flag:
                 strr += ", "
             else:
                 flag = True
             if isinstance(i, dict):
                 strr += i.get("default")
@@ -105,31 +118,31 @@
         self.cache = {}
         Cache.set(self._c(), {})
         
         sql = self.sql_select.format(self._getTableName())
         data = Mysql.selectx(sql)
         for i in data:
             strr = self._getIndexStr(i)
-            exec(f"cache.cacheList{strr} = {eval(str(i))}")
-
+            exec(f"Cache.cacheList{strr} = {eval(str(i))}")
+        
         return self
     
     def _dropTable(self):
         Mysql.commonx(self.sql_dropTable.format(self._getTableName()))
         self.delFlag = True
         del self
         return None
 
     def _get(self, key: str, *args, **kwargs):
         return self.cache.get(key, *args, **kwargs)
     
     def _insert(self, **kwargs):
         # 在缓存中新增
         strr = self._getIndexStr(kwargs)
-        exec(f"cache.cacheList{strr} = {eval(str(kwargs))}")
+        exec(f"Cache.cacheList{strr} = {eval(str(kwargs))}")
         
         self.exists = True
         self.delFlag = False
         self.cache = kwargs
         self.args = kwargs
         self._refreshWhereCase()
         
@@ -139,15 +152,15 @@
             insertList.append(kwargs.get(i.get('name')))
         self.format_insert.append(insertList)
         return self
     
     def _delete(self):
         # 缓存删除
         strr = self._getIndexStr(self.args)
-        exec(f"del cache.cacheList{strr}")
+        exec(f"del Cache.cacheList{strr}")
         
         self.format_delete = True
         
         return self
     
     def __delete(self):
         # 数据库删除
@@ -162,15 +175,15 @@
             self.format_update.append({
                 "key": k,
                 "value": v
             })
             
             # 修改缓存
             '''
-            _cache = cache.cacheList
+            _cache = Cache.cacheList
             cacheList: list = []
             map: list = ["_db_table"]
             self.args["_db_table"] = self._c()
             map += self.map
             for i in map:
                 cacheList.append(_cache)
                 _cache = _cache.get(self.args.get(i))
@@ -182,29 +195,30 @@
             listLength = len(cacheList) - 1
             while listLength >= 0:
                 _temp = cacheList[-listLength]
                 _temp[map[-listLength]] = _cache
                 _cache = _temp
                 listLength -= 1
             
-            cache.cacheList = _cache
+            Cache.cacheList = _cache
             '''
             
             self.cache[k] = v
             
             strr: str = ""
             for i in self.map:
-                strr += f"[{eval(str(self.args.get(i)))}]"
-            exec(f"cache.cacheList{strr} = {eval(str(self.cache))}")
+                ob = self.args.get(i)
+                strr += f"[\"{ob}\"]" if isinstance(ob, str) else f"[{eval('self.args.get(i)')}]"
+            exec(f"Cache.cacheList{strr} = {eval(str(self.cache))}")
         return self
     
     def __insert(self):
         if not self.format_insert:
             return False
-        
+
         colname: str = ""
         flag: bool = False
         for i in self.col:
             name = i.get('name')
             if flag:
                 colname += ", "
             else:
@@ -258,55 +272,21 @@
         
     def _refresh(self, insertFlag: bool = False, kwargs: dict = {}):
         self.cache = Cache.get(self._c())
         
         # 初始化数据表
         if self.cache == None:
             self._createTable()
+            self.cache = Cache.get(self._c())
             
         # 获取具体cache
         iter = 0
         for i in self.map:
             _cache = self.cache
             self.cache = self.cache.get(self.args.get(i))
             if self.cache == None:
                 if insertFlag:
                     self._insert(**kwargs)
                     self.exists = False
                 else:
                     raise Exception("Key Not Found.")
             iter += 1
-
-# ============ DEBUG ============
-
-class TestModel(ModelBase):
-    db_table = "402ModReport"
-    db_perfix = "bot"
-    map = ["qn"]
-    format_createTable = ["PRIMARY KEY (`id`)"]
-    
-    def id(self):
-        return "INT(11) NOT NULL AUTO_INCREMENT"
-    
-    def qn(self):
-        return "INT(11) NOT NULL COMMENT 'UID'"
-    
-    def au(self):
-        return "VARCHAR(11) NOT NULL COMMENT 'AUID'"
-    
-    def time(self):
-        return "VARCHAR(50) COMMENT '报名时间'"
-    
-    def nickname(self):
-        return "VARCHAR(100) COMMENT '昵称'"
-
-def mapDict(ob, key: str):
-    obDict = {}
-    for i in ob:
-        obDict[i.get(key)] = i
-    
-    return obDict
-
-if __name__ == "__main__":
-    model = TestModel(qn=int(input("> ")), au="az")
-    print(Cache.cacheList)
-
```

### Comparing `PigBotFramework-4.1.8/pbf/statement/ImageStatement.py` & `PigBotFramework-4.1.9/pbf/statement/ImageStatement.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/statement/TextStatement.py` & `PigBotFramework-4.1.9/pbf/statement/TextStatement.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/statement/__init__.py` & `PigBotFramework-4.1.9/pbf/statement/__init__.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/CQCode.py` & `PigBotFramework-4.1.9/pbf/utils/CQCode.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/Coin.py` & `PigBotFramework-4.1.9/pbf/utils/Coin.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/RegCmd.py` & `PigBotFramework-4.1.9/pbf/utils/RegCmd.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/__init__.py` & `PigBotFramework-4.1.9/pbf/utils/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import hmac, random, math
 from .Coin import Coin
 from .CQCode import CQCode
 from ..controller import Mysql
 from ..controller.PbfStruct import Struct
+from ..model.BotSettingsModel import BotSettingsModel
 from googletrans import Translator as googleTranslator
 
 googleTranslatorIns = googleTranslator()
 
 from apscheduler.schedulers.background import BackgroundScheduler
 scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
 
@@ -71,19 +72,22 @@
 
     def getPswd(self, uuid):
         '''
         根据UUID获取实例通信密钥
         '''
         if not uuid:
             raise ValueError('Please give a non-empty string as a uuid.')
-        botOb = Mysql.selectx('SELECT * FROM `botBotconfig` WHERE `uuid`=%s;', (uuid))
-        if not botOb:
+        botOb = BotSettingsModel(uuid=uuid)
+        print(botOb._get('secret'))
+        if botOb.exists == False:
+            botOb._delete()
+            del botOb
             raise ValueError('Cannot find the right secret. Is the uuid right?')
         else:
-            return botOb[0].get('secret')
+            return botOb._get('secret')
 
     def encryption(self, data, secret, encode='utf-8', digestmod='sha1'):
         '''
         HMAC加密
         '''
         key = secret.encode(encode)
         obj = hmac.new(key, msg=data, digestmod=digestmod)
```

### Comparing `PigBotFramework-4.1.8/pbf/utils/nsfw/classify_nsfw.py` & `PigBotFramework-4.1.9/pbf/utils/nsfw/classify_nsfw.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/nsfw/image_utils.py` & `PigBotFramework-4.1.9/pbf/utils/nsfw/image_utils.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/nsfw/model.py` & `PigBotFramework-4.1.9/pbf/utils/nsfw/model.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/build_image.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/build_image.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/config.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/config.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/fonts.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/fonts.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/gradient.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/gradient.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/text2image.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/text2image.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/pbf/utils/pillow/types.py` & `PigBotFramework-4.1.9/pbf/utils/pillow/types.py`

 * *Files identical despite different names*

### Comparing `PigBotFramework-4.1.8/setup.py` & `PigBotFramework-4.1.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -116,15 +116,15 @@
     license='MIT',
     classifiers=[
         # Trove classifiers
         # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
         'License :: OSI Approved :: Apache Software License',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3',
-        'Programming Language :: Python :: 3.6',
+        'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: Implementation :: CPython',
         'Programming Language :: Python :: Implementation :: PyPy'
     ],
     # $ setup.py publish support.
     cmdclass={
         'upload': UploadCommand,
     },
```

