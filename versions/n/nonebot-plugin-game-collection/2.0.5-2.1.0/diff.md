# Comparing `tmp/nonebot_plugin_game_collection-2.0.5.tar.gz` & `tmp/nonebot_plugin_game_collection-2.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nonebot_plugin_game_collection-2.0.5.tar", last modified: Mon Jan 30 20:08:54 2023, max compression
+gzip compressed data, was "nonebot_plugin_game_collection-2.1.0.tar", last modified: Fri Apr  7 09:56:11 2023, max compression
```

## Comparing `nonebot_plugin_game_collection-2.0.5.tar` & `nonebot_plugin_game_collection-2.1.0.tar`

### file list

```diff
@@ -1,44 +1,54 @@
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.555433 nonebot_plugin_game_collection-2.0.5/
--rw-rw-rw-   0        0        0     1065 2022-08-13 09:26:37.000000 nonebot_plugin_game_collection-2.0.5/LICENSE
--rw-rw-rw-   0        0        0      193 2022-12-20 21:13:32.000000 nonebot_plugin_game_collection-2.0.5/MANIFEST.in
--rw-rw-rw-   0        0        0      376 2023-01-30 20:08:54.554432 nonebot_plugin_game_collection-2.0.5/PKG-INFO
--rw-rw-rw-   0        0        0     8291 2022-08-13 12:03:08.000000 nonebot_plugin_game_collection-2.0.5/README.md
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.503388 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/
--rw-rw-rw-   0        0        0    43867 2023-01-30 18:29:22.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/__init__.py
--rw-rw-rw-   0        0        0      288 2023-01-19 14:18:52.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/api.py
--rw-rw-rw-   0        0        0     1006 2023-01-10 09:59:45.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/avatar.py
--rw-rw-rw-   0        0        0      455 2023-01-11 18:07:38.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/config.py
--rw-rw-rw-   0        0        0   128285 2023-01-30 20:02:12.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/data_source.py
--rw-rw-rw-   0        0        0      179 2023-01-13 09:29:56.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/element_library.json
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.477366 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.526408 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/
--rw-rw-rw-   0        0        0     5418 2022-08-06 08:52:55.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/Stand.json
--rw-rw-rw-   0        0        0     4492 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/“日常，真的很日常”.json
--rw-rw-rw-   0        0        0     1704 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/克苏鲁.json
--rw-rw-rw-   0        0        0      892 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/基础事件.json
--rw-rw-rw-   0        0        0     2668 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/复刻经典事件集合v1.json
--rw-rw-rw-   0        0        0     1237 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/崩坏集合v1.json
--rw-rw-rw-   0        0        0    22378 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/群友日常.json
--rw-rw-rw-   0        0        0     4659 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/芜湖事件合集.json
--rw-rw-rw-   0        0        0      995 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/赫尔事件集v1.json
--rw-rw-rw-   0        0        0     2223 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/赫尔的赛马场事件簿.json
--rw-rw-rw-   0        0        0    15245 2022-08-06 13:02:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events_main.py
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.527408 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/fonts/
--rw-rw-rw-   0        0        0 18214472 2019-12-07 09:08:27.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/fonts/simsun.ttc
--rw-rw-rw-   0        0        0     6188 2022-08-06 12:31:20.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/horse.py
--rw-rw-rw-   0        0        0    11416 2023-01-30 19:23:27.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/menu_data.json
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.552930 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/process/
--rw-rw-rw-   0        0        0     5257 2023-01-19 14:52:52.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/process/ohlc.py
--rw-rw-rw-   0        0        0     4590 2023-01-21 08:21:22.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/props_library.json
--rw-rw-rw-   0        0        0     4584 2022-08-06 13:03:20.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/race_group.py
--rw-rw-rw-   0        0        0      494 2022-08-06 06:56:48.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/setting.py
--rw-rw-rw-   0        0        0     9110 2022-08-09 09:44:50.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/start.py
--rw-rw-rw-   0        0        0     5852 2023-01-19 14:54:40.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/utils.py
-drwxrwxrwx   0        0        0        0 2023-01-30 20:08:54.511895 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/
--rw-rw-rw-   0        0        0      376 2023-01-30 20:08:54.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1722 2023-01-30 20:08:54.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-01-30 20:08:54.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      104 2023-01-30 20:08:54.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/requires.txt
--rw-rw-rw-   0        0        0       31 2023-01-30 20:08:54.000000 nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-01-30 20:08:54.555433 nonebot_plugin_game_collection-2.0.5/setup.cfg
--rw-rw-rw-   0        0        0      738 2023-01-30 20:08:50.000000 nonebot_plugin_game_collection-2.0.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.638506 nonebot_plugin_game_collection-2.1.0/
+-rw-rw-rw-   0        0        0     1065 2022-08-13 09:26:37.000000 nonebot_plugin_game_collection-2.1.0/LICENSE
+-rw-rw-rw-   0        0        0      193 2022-12-20 21:13:32.000000 nonebot_plugin_game_collection-2.1.0/MANIFEST.in
+-rw-rw-rw-   0        0        0      376 2023-04-07 09:56:11.635503 nonebot_plugin_game_collection-2.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0     8291 2022-08-13 12:03:08.000000 nonebot_plugin_game_collection-2.1.0/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.589964 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.599472 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/.vs/
+-rw-rw-rw-   0        0        0       37 2023-03-04 09:10:52.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/.vs/ProjectSettings.json
+-rw-rw-rw-   0        0        0      150 2023-03-04 11:54:34.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/.vs/VSWorkspaceState.json
+-rw-rw-rw-   0        0        0    17615 2023-03-04 07:33:31.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Account.py
+-rw-rw-rw-   0        0        0    41084 2023-03-04 07:28:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Game.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.606478 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/
+-rw-rw-rw-   0        0        0    15272 2023-02-28 15:49:25.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/events_main.py
+-rw-rw-rw-   0        0        0     6237 2023-02-28 15:49:25.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/horse.py
+-rw-rw-rw-   0        0        0     4999 2023-02-28 16:14:15.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/race_group.py
+-rw-rw-rw-   0        0        0     8962 2023-02-28 15:50:53.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/start.py
+-rw-rw-rw-   0        0        0    10909 2023-03-04 07:38:48.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Manager.py
+-rw-rw-rw-   0        0        0    20122 2023-03-04 11:07:21.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Market.py
+-rw-rw-rw-   0        0        0    13072 2023-03-04 08:07:35.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Prop.py
+-rw-rw-rw-   0        0        0    28660 2023-03-04 11:53:52.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/__init__.py
+-rw-rw-rw-   0        0        0     3129 2023-03-04 11:53:52.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/config.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.609481 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/data/
+-rw-rw-rw-   0        0        0      525 2023-02-24 19:49:14.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/data/api.py
+-rw-rw-rw-   0        0        0     5589 2023-03-02 18:02:43.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/data/data.py
+-rw-rw-rw-   0        0        0      102 2023-02-24 19:49:02.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/data/run.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.612984 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/
+-rw-rw-rw-   0        0        0      171 2023-02-25 14:16:58.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/element_library.json
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.629498 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/
+-rw-rw-rw-   0        0        0     5335 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/Stand.json
+-rw-rw-rw-   0        0        0     4372 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/“日常，真的很日常”.json
+-rw-rw-rw-   0        0        0     1692 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/克苏鲁.json
+-rw-rw-rw-   0        0        0      861 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/基础事件.json
+-rw-rw-rw-   0        0        0     2616 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/复刻经典事件集合v1.json
+-rw-rw-rw-   0        0        0     1208 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/崩坏集合v1.json
+-rw-rw-rw-   0        0        0    22088 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/群友日常.json
+-rw-rw-rw-   0        0        0     4569 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/芜湖事件合集.json
+-rw-rw-rw-   0        0        0      975 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/赫尔事件集v1.json
+-rw-rw-rw-   0        0        0     2199 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/赫尔的赛马场事件簿.json
+-rw-rw-rw-   0        0        0    11276 2023-02-25 14:16:59.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/menu_data.json
+-rw-rw-rw-   0        0        0     4976 2023-03-04 08:08:51.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/props_library.json
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.630999 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/subprocess/
+-rw-rw-rw-   0        0        0     2347 2023-03-04 05:27:28.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/subprocess/ohlc.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.634502 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/utils/
+-rw-rw-rw-   0        0        0     1321 2023-02-25 14:16:58.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/utils/avatar.py
+-rw-rw-rw-   0        0        0     7133 2023-02-27 17:39:47.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/utils/chart.py
+-rw-rw-rw-   0        0        0     1619 2023-02-28 15:47:33.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/utils/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:56:11.596970 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/
+-rw-rw-rw-   0        0        0      376 2023-04-07 09:56:11.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2151 2023-04-07 09:56:11.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:56:11.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      104 2023-04-07 09:56:11.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       31 2023-04-07 09:56:11.000000 nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 09:56:11.638506 nonebot_plugin_game_collection-2.1.0/setup.cfg
+-rw-rw-rw-   0        0        0      738 2023-04-07 09:56:02.000000 nonebot_plugin_game_collection-2.1.0/setup.py
```

### Comparing `nonebot_plugin_game_collection-2.0.5/LICENSE` & `nonebot_plugin_game_collection-2.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `nonebot_plugin_game_collection-2.0.5/README.md` & `nonebot_plugin_game_collection-2.1.0/README.md`

 * *Files identical despite different names*

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/__init__.py` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/Game.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,1152 +1,1153 @@
-from nonebot import on_command, on_fullmatch, on_regex, require
+﻿from typing import Tuple,Dict
+from pydantic import BaseModel
 from nonebot.adapters.onebot.v11 import (
-    GROUP,
-    GROUP_ADMIN,
-    GROUP_OWNER,
-    PRIVATE,
     Bot,
     MessageEvent,
     GroupMessageEvent,
-    PrivateMessageEvent,
     Message,
     MessageSegment
-)
-from nonebot.internal.adapter import Bot as BaseBot
-from nonebot.rule import to_me
-from nonebot.matcher import Matcher
-from nonebot.params import CommandArg, Arg
-from nonebot.log import logger
-from nonebot.permission import SUPERUSER
-
-from pathlib import Path
-import math
+    )
+import random
 import time
 import asyncio
-import random
-
-import shutil
-import os
-import io
-import re
-
-from .utils import is_number, number, get_message_at, text_to_png
-from .data_source import (
-    bot_name,
-    russian_manager,
-    market_manager,
-    max_bet_gold,
-    race_bet_gold,
-    russian_path,
-    linechart_cache,
-    candlestick_cache
-    )
-from .utils import company_info_Splicing
-
-from .start import *
-from .race_group import race_group
-from .setting import  *
-
-try:
-    import ujson as json
-except ModuleNotFoundError:
-    import json
-
-try:
-    from nonebot.plugin import PluginMetadata
-    with open(os.path.dirname(__file__) + "/menu_data.json", "r", encoding="utf8") as f:
-        menu_data = json.load(f)
-    __plugin_meta__ = PluginMetadata(
-        name = "小游戏合集",
-        description = "各种群内小游戏",
-        usage = "",
-        extra = {
-            'menu_data': menu_data,
-            'menu_template': 'default'
-            }
-        )
-except ModuleNotFoundError:
-    logger.info("当前nonebot版本无法使用插件元数据。")
-
-
-from nonebot_plugin_imageutils import text2image
-
-scheduler = require("nonebot_plugin_apscheduler").scheduler
-
-data_file = russian_path / "data" / "russian"
-if not data_file.exists():
-    data_file.mkdir(exist_ok=True, parents=True)
-
-#开场加载
-
-events_list = []
-
-driver = get_driver()
-@driver.on_startup
-async def events_read():
-    global events_list
-    events_list = await load_dlcs()
-    market_manager.reset_market_index()
-
-
-
-RaceNew = on_command("赛马创建",aliases = {"创建赛马"}, permission=GROUP, priority=5, block=True)
-RaceJoin = on_command("赛马加入",aliases = {"加入赛马"}, permission=GROUP, priority=5, block=True)
-RaceStart = on_command("赛马开始",aliases = {"开始赛马"}, permission=GROUP, priority=5, block=True)
-RaceReStart = on_command("赛马重置",aliases = {"重置赛马"}, permission=GROUP, priority=5, block=True)
-RaceStop = on_command("赛马暂停",aliases = {"暂停赛马"}, permission=SUPERUSER, priority=5, block=True)
-RaceClear = on_command("赛马清空",aliases = {"清空赛马"}, permission=SUPERUSER, priority=5, block=True)
-RaceReload = on_command("赛马事件重载", permission=SUPERUSER, priority=5, block=True)
 
-race = {}
+from .utils.utils import get_message_at
+from .utils.chart import text_to_png
+from .data.data import props_library
+from .config import bot_name, security_gold, max_bet_gold, max_player, min_player
+
+from .HorseRace.start import load_dlcs
+from .HorseRace.race_group import race_group
+
+from .Manager import data
+from . import Manager
+
+user_data = data.user
+group_data = data.group
 
-@RaceNew.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    global race
-    group = event.group_id
-    try:
-        if race[group].start == 0 and time.time() - race[group].time < 300:
-            out_msg = (
-                f'> 创建赛马比赛失败!\n'
-                f'> 原因:{bot_name}正在打扫赛马场...\n'
-                f'> 解决方案:等{bot_name}打扫完...\n'
-                f'> 可以在{str(round(setting_over_time - time.time() + race[group].time),2)}秒后输入 赛马重置'
-                )
-            await RaceNew.finish(out_msg)
-        elif race[group].start == 1:
-            await RaceNew.finish(f"一场赛马正在进行中")
-            await RaceNew.finish()
-    except KeyError:
-        pass
-
-    race[group] = race_group()
-    await RaceNew.finish(f'> 创建赛马比赛成功！\n> 输入 [赛马加入 + 名字] 即可加入赛马。')
-
-@RaceJoin.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    global race, max_player
-    msg = arg.extract_plain_text().strip()
-
-    group = event.group_id
-    uid = event.user_id
-
-    gold = russian_manager.get_user_data(event)["gold"]
 
-    player_name = event.sender.card if event.sender.card else event.sender.nickname
 
-    if gold < race_bet_gold:
-        await RaceJoin.finish(f'报名赛马需要{race_bet_gold}金币，你的金币：{gold}。', at_sender=True)
-    else:
-        pass
-
-    try:
-        race[group]
-    except KeyError:
-        await RaceJoin.finish( f"赛马活动未开始，请输入 [赛马创建] 开场")
-    try:
-        if race[group].start == 1 or race[group].start == 2:
-            await RaceJoin.finish()
-    except KeyError:
-        await RaceJoin.finish()
-    if race[group].query_of_player() >= max_player:
-        await RaceJoin.finish( f"> 加入失败\n> 原因:赛马场就那么大，满了满了！" )
-    if race[group].is_player_in(uid) == True:
-        await RaceJoin.finish( f"> 加入失败\n> 原因:您已经加入了赛马场!")
-    if msg:
-        if len(msg) > 5:
-            horse_name = msg[:2]+"酱"
+"""+++++++++++++++++
+——————————
+     赛马小游戏
+——————————
++++++++++++++++++"""
+
+def race_create_check(event:GroupMessageEvent):
+    """
+    检查是否可以创建赛马
+    """
+    global current_games
+    group_id = event.group_id
+    if group_id not in current_games:
+        return None
+    session = current_games[group_id]
+    overtime = time.time() - session.time + 180
+    if session.at == -1:
+        race:race_group = session.info["race_group"]
+        if race.start == 0:
+            if overtime < 120:
+                return "一场赛马正在报名中"
+            else:
+                return None
         else:
-            horse_name = msg
-
-        race[group].add_player(horse_name, uid, player_name)
-        
-        russian_manager._player_data[str(group)][str(uid)]["gold"] -= race_bet_gold
-        russian_manager.save()
-
-        out_msg = (
-            '\n> 加入赛马成功\n'
-            '> 赌上马儿性命的一战即将开始!\n'
-            f'> 赛马场位置:{str(race[group].query_of_player())}/{str(max_player)}'
-            )
-        await RaceJoin.finish(out_msg, at_sender=True)
+            return f"一场赛马正在进行中，遇到问题可以{f'在{t}秒后' if (t := int(180 - overtime)) > 0 else ''}输入【赛马重置】重置游戏"
     else:
-        await RaceJoin.finish(f"请输入你的马儿名字", at_sender=True)
+        return session.create_check(event)
 
-@RaceStart.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    global race
-    global events_list
-    group = event.group_id
-    try:
-        if race[group].query_of_player() == 0:
-            await RaceStart.finish()
-    except KeyError:
-        await RaceStart.finish()
-    try:
-        if race[group].start == 0 or race[group].start == 2:
-            if len(race[group].player) >= min_player:
-                race[group].start_change(1)
-            else:
-                await RaceStart.finish(
-                    f'> 开始失败\n'
-                    f'> 原因:赛马开局需要最少{str(min_player)}人参与',
-                    at_sender=True
-                    )
-        elif race[group].start == 1:
-            await RaceStart.finish()
-    except KeyError:
-        await RaceStart.finish()
-    race[group].time = time.time()
-
-    await RaceStart.send(
-        f'> 比赛开始\n'
-        f'> 当前奖金：{len(race[group].player) * race_bet_gold}金币'
+def RaceNew(event:GroupMessageEvent, gold:int ):
+    """
+    赛马创建
+    """
+    global current_games
+    if msg := race_create_check(event):
+        return msg
+    current_games[event.group_id] =  Session(
+        time = time.time() + 180,
+        player1_id = event.user_id,
+        at = -1,
+        gold = gold,
+        info = {"game":"horse race","race_group":race_group()}
         )
+    return ("\n"
+             "> 创建赛马比赛成功！\n"
+             "> 输入 【赛马加入 名字】 即可加入赛马。")
+
+def RaceJoin(event:GroupMessageEvent, horsename:str):
+    """
+    赛马加入
+    """
+    global current_games
+    group_id = event.group_id
+    if group_id not in current_games:
+        return "赛马活动未开始，请输入【赛马创建】创建赛马场"
+    session = current_games[event.group_id]
+    if session.info["game"] != "horse race":
+        return "其他对战进行中。"
+    user,group_account = Manager.locate_user(event)
+    user_id = user.user_id
+    if (gold := group_account.gold) < session.gold:
+        return f"报名赛马需要{session.gold}金币，你的金币：{gold}。"
+    race:race_group = session.info["race_group"]
+    if race.start != 0:
+        return
+    if (query_of_player := race.query_of_player()) >= max_player:
+        return "加入失败！赛马场就那么大，满了满了！"
+    if race.is_player_in(user_id) == True:
+        return "加入失败！您已经加入了赛马场!"
+    if not horsename:
+        return "请输入你的马儿名字"
+    horsename = horsename[:2]+"酱" if len(horsename) > 5 else horsename
+    race.add_player(horsename, user_id, group_account.nickname)
+    user.gold -= session.gold
+    group_account.gold -= session.gold
+    return  ("\n"
+             "> 加入赛马成功\n"
+             "> 赌上马儿性命的一战即将开始!\n"
+             f"> 赛马场位置:{query_of_player + 1}/{max_player}")
+
+events_list = load_dlcs()
+
+async def RaceStart(bot:Bot, event:GroupMessageEvent):
+    """
+    赛马开始
+    """
+    global current_games
+    group_id = event.group_id
+    if group_id not in current_games or (session := current_games[event.group_id]).info["game"] != "horse race":
+        return "赛马活动未开始，请输入【赛马创建】创建赛马场"
+    race:race_group = session.info["race_group"]
+    global events_list
+    if (player_count := race.query_of_player()) == 0:
+        return
+    if race.start == 1:
+        return
+    if race.start == 0 or race.start == 2:
+        if player_count >= min_player:
+            race.start = 1
+        else:
+            return f"开始失败！赛马开局需要最少{min_player}人参与"
+    session.time = time.time() + 180
+    await bot.send(event,(f'> 比赛开始\n'
+                          f'> 当前奖金：{session.gold * player_count}金币'))
     await asyncio.sleep(0.5)
 
-    while race[group].start == 1:
+    while race.start == 1:
         # 回合数+1
-        race[group].round_add()
+        race.round_add()
         #移除超时buff
-        race[group].del_buff_overtime()
+        race.del_buff_overtime()
         #马儿全名计算
-        race[group].fullname()
+        race.fullname()
         #回合事件计算
-        text = race[group].event_start(events_list)
+        text = race.event_start(events_list)
         #马儿移动
-        race[group].move()
+        race.move()
         #场地显示
-        display = race[group].display()
-
-        logger.info(f'事件输出:{text}\n{display}')
+        display = race.display()
         
-        output = text_to_png(display)
+        output = text_to_png(display,20)
 
         try:
-            await RaceStart.send(Message(text) + MessageSegment.image(output))
+            await bot.send(event,(Message(text) + MessageSegment.image(output)))
         except:
             text = ""
-            await RaceStart.send(MessageSegment.image(output))
+            try:
+                await bot.send(event,(MessageSegment.image(output)))
+            except:
+                pass
 
-        if text:
-            await asyncio.sleep(0.5 + int(0.06 * len(text)))
-        else:
-            await asyncio.sleep(0.5)
+        await asyncio.sleep(0.5 + int(0.06 * len(text)))
             
         #全员失败计算
-        if race[group].is_die_all():
-            for x in race[group].player:
+        if race.is_die_all():
+            for x in race.player:
                 uid = x.playeruid
-                if uid > 10:
-                    russian_manager._player_data[str(group)][str(uid)]["gold"] += race_bet_gold
-            else:
-                russian_manager.save()
-                del race[group]
+                if uid in user_data:
+                    user = user_data[uid]
+                    user.gold += session.gold
+                    user.group_accounts[group_id].gold += session.gold
+
+            del current_games[group_id]
+            return "比赛已结束，鉴定为无马生还"
 
-            await RaceStart.finish("比赛已结束，鉴定为无马生还")
         #全员胜利计算
-        winer = race[group].is_win_all()
+        winer = race.is_win_all()
         winer_list="\n"
         if winer != []:
-            await RaceStart.send(
-                f'> 比赛结束\n'
-                f'> {bot_name}正在为您生成战报...'
-                ) 
+            await bot.send(event,(f'> 比赛结束\n'
+                                  f'> {bot_name}正在为您生成战报...'))
             await asyncio.sleep(1)
-            gold = int(race_bet_gold * len(race[group].player) / len(winer))
+            gold = int(session.gold * player_count / len(winer))
             for x in winer:
                 uid = x[1]
                 winer_list += "> "+ x[0] + "\n"
-                if uid > 10:
-                    russian_manager._player_data[str(group)][str(uid)]["gold"] += gold
-            else:
-                russian_manager.save()
-                del race[group]
-
-            msg = f"> 比赛已结束，胜者为：{winer_list}> 本次奖金：{gold} 金币"
-            await RaceStart.finish(msg)
-
+                if uid in user_data:
+                    user = user_data[uid]
+                    user.gold += gold
+                    user.group_accounts[group_id].gold += gold
+            del current_games[group_id]
+            return (f"> 比赛已结束，胜者为：{winer_list}"
+                    f"> 本次奖金：{gold} 金币")
         await asyncio.sleep(1)
 
-@RaceReStart.handle()
-async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
-    global race
-    group = event.group_id
-    time_key = math.ceil(time.time() - race[group].time)
-    if time_key >= setting_over_time:
-        for x in race[group].player:
-            uid = x.playeruid
-            if uid > 10:
-                russian_manager._player_data[str(group)][str(uid)]["gold"] += race_bet_gold
-        else:
-            russian_manager.save()
-            del race[group]
-
-        await RaceReStart.finish(f'超时{str(setting_over_time)}秒，已重置赛马场')
-    await RaceReStart.finish(f'未超时{str(setting_over_time)}秒，目前为{str(time_key)}秒，未重置')
-
-@RaceStop.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    global race
-    group = event.group_id
-    race[group].start_change(2)
-
-@RaceClear.handle()
-async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
-    global race
-    group = event.group_id
-    for x in race[group].player:
+def RaceReStart(event:GroupMessageEvent):
+    """
+    赛马重置
+    """
+    global current_games
+    group_id = event.group_id
+    session = current_games[group_id]
+
+    overtime = time.time() - session.time + 180
+    if overtime < 180:
+        return f"当前赛马已创建 {int(overtime)} 秒，未超时。"
+    race:race_group = session.info["race_group"]
+    for x in race.player:
         uid = x.playeruid
-        if uid > 10:
-            russian_manager._player_data[str(group)][str(uid)]["gold"] += race_bet_gold
-    else:
-        russian_manager.save()
-        del race[group]
-
-@RaceReload.handle()
-async def _(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
-    global events_list
-    logs = f""
-    files = os.listdir(os.path.dirname(__file__) + '/events/horserace')
-    for file in files:
-        try:
-            with open(f'{os.path.dirname(__file__)}/events/horserace/{file}', "r", encoding="utf-8") as f:
-                logger.info(f'加载事件文件：{file}')
-                events = deal_events(json.load(f))
-                events_list.extend(events)
-            logger.info(f"加载 {file} 成功")
-            logs += f'加载 {file} 成功\n'
-        except:
-            logger.info(f"加载 {file} 失败！失败！失败！")
-            logs += f"加载 {file} 失败！失败！失败！\n"
-    await RaceReload.finish(logs)
-
-
-
-# 金币签到
-sign = on_command("金币签到",aliases = {"轮盘签到"}, priority = 5, block = True)
-
-@sign.handle()
-async def _(event: MessageEvent):
-    msg =  russian_manager.sign(event)
-    await sign.finish(msg, at_sender=True)
-
-# 发动革命
-revolt = on_command("发起重置", aliases={"发起revolt","发动revolt", "revolution", "Revolution"},permission=GROUP, priority=5, block=True)
+        if uid in user_data:
+            user = user_data[uid]
+            user.gold += session.gold
+            user.group_accounts[group_id].gold += session.gold
+
+    del race
+    return "赛马场已重置。"
+
+
+"""+++++++++++++++++
+——————————
+     其他小游戏
+——————————
++++++++++++++++++"""
+
+def slot(event:MessageEvent, gold:int):
+    """
+    幸运花色
+    """
+    user,group_account = Manager.locate_user(event)
+    if not group_account:
+        return "私聊未关联账户，请发送【关联账户】关联群内账户。"
+    if gold > max_bet_gold:
+        return f'幸运花色每次最多{max_bet_gold}金币。'
+    if gold > group_account.gold:
+        return f'你没有足够的金币，你的金币：{user_data["group_account.gold:"]}。'
+    suit = {1:"♤",2:"♡",3:"♧",4:"♢"}
+    x = random.randint(1,4)
+    y = random.randint(1,4)
+    z = random.randint(1,4)
+    res = f"\n| {suit[x]} | {suit[y]} | {suit[z]} |\n"
+    l = len(set([x,y,z]))
+    if l == 1:
+        gold = gold * 7
+        msg =("你抽到的花色为：" +
+              res +
+              f"恭喜你获得了{gold}金币，祝你好运~")
+    elif l == 2:
+        gold = 0
+        msg =("你抽到的花色为：" +
+              res +
+              "祝你好运~")
+    else:
+        gold = -gold
+        msg =("你抽到的花色为：" +
+              res +
+              f"你失去了{-gold}金币 ，祝你好运~")
+    user.gold += gold
+    group_account.gold += gold
+    return msg
+
+"""+++++++++++++++++
+——————————
+      对战系统
+——————————
++++++++++++++++++"""
+
+class Session(BaseModel):
+    """
+    群内进行的游戏
+    """
+    time:float = 0.0
+    player1_id:int = None
+    player2_id:int = None
+    at:int = None
+    round = 0
+    next:int = None
+    win:int = None
+    gold:int = 0
+    info:dict = {}
+    def create(self, event:GroupMessageEvent):
+        """
+        创建游戏
+        """
+        self.__init__(
+            time = time.time(),
+            player1_id = event.user_id,
+            at = int(get_message_at(event.message)[0]) if get_message_at(event.message) else None
+            )
 
-@revolt.handle()
-async def _(event: GroupMessageEvent):
-    msg = russian_manager.revlot(event.group_id)
-    if msg:
-        await revolt.finish(msg)
-    else:
-        await revolt.finish()
-# 重置签到
-revolt_sign = on_command("重置签到",aliases = {"revolt签到"}, priority = 5, block = True)
-
-@revolt_sign.handle()
-async def _(event: MessageEvent):
-    msg = russian_manager.revolt_sign(event)
-    await revolt_sign.finish(msg, at_sender=True)
-
-# 发红包
-give_gold = on_command("打钱", aliases={"发红包", "赠送金币"},permission=GROUP, priority=5, block=True)
-
-@give_gold.handle()
-async def _(bot: Bot,event: GroupMessageEvent,arg: Message = CommandArg(),):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 1:
-            msg = msg[0]
-            if is_number(msg):
-                unsettled = abs(int(msg))
-                player_id = event.user_id
-                at_player_id = get_message_at(event.json())
-                if at_player_id:
-                    at_player_id = at_player_id[0]
-                    if unsettled > russian_manager.get_user_data(event)["gold"]:
-                        await give_gold.finish("您的账户没有足够的金币", at_sender=True)
-                    else:
-                        await russian_manager._init_at_player_data(bot,event,at_player_id)
-                        msg = russian_manager.transfer_accounts(event, at_player_id, unsettled)
-                        await give_gold.finish(msg)
-
-# 送道具
-give_props = on_command("送道具", aliases={"赠送道具"},permission=GROUP, priority=5, block=True)
-
-@give_props.handle()
-async def _(bot: Bot,event: GroupMessageEvent,arg: Message = CommandArg(),):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        at_player_id = get_message_at(event.json())
-        if at_player_id:
-            at_player_id = at_player_id[0]
-            if len(msg) == 1:
-                props = msg[0]
-                count = 1
-            else:
-                props = msg[0]
-                n = number(msg[1])
-                if n and n > 1:
-                    count = int(n)
+    def create_check(self, event:GroupMessageEvent):
+        """
+        检查是否可以根据event创建游戏
+        如果不能创建则返回提示
+        如果可以创建则返回None
+        """
+        overtime = time.time() - self.time
+        if overtime > 60:
+            return None
+        user_id = event.user_id
+        if player1_id := self.player1_id:
+            if player1_id == user_id:
+                return "你已发起了一场对决"
+            if player2_id := self.player2_id:
+                if player2_id == user_id:
+                    return "你正在进行一场对决"
                 else:
-                    count = 1
-            russian_manager._init_player_data(event)
-            await russian_manager._init_at_player_data(bot,event,at_player_id)
-            msg = russian_manager.give_props(event, at_player_id, props, count)
-            await give_props.finish(msg, at_sender=True)
-
-# 使用道具
-use_props = on_command("使用道具", priority=5, block=True)
-
-@use_props.handle()
-async def _(bot:Bot, event: MessageEvent, arg:Message = CommandArg(),):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 1:
-            props = msg[0]
-            count = 1
-        else:
-            props = msg[0]
-            n = number(msg[1])
-            if n and n > 1:
-                count = int(n)
+                    player1_name = user_data[player1_id].group_accounts[event.group_id].nickname
+                    player2_name = user_data[player2_id].group_accounts[event.group_id].nickname
+                    return f"{player1_name} 与 {player2_name} 的对决还未结束！"
             else:
-                count = 1
-        msg = russian_manager.use_props.main(event,props,count)
-        await use_props.finish(msg, at_sender=True)
-
-# 状态处理
-accept = on_command("接受挑战", aliases={"接受决斗", "接受对决"}, permission=GROUP, priority=5, block=True)
-
-@accept.handle()
-async def _(event: GroupMessageEvent):
-    msg = russian_manager.accept(event)
-    if msg:
-        await accept.send(msg)       
-    else:
-        await accept.finish()
-
-refuse = on_command("拒绝挑战", aliases={"拒绝决斗", "拒绝对决"}, permission=GROUP, priority=5, block=True)
-
-@refuse.handle()
-async def _(bot: Bot, event: GroupMessageEvent):
-    msg = russian_manager.refuse(bot, event)
-    if msg:
-        await refuse.send(msg, at_sender=True)        
-    else:
-        await refuse.finish()
-
-settlement = on_command("结算", permission=GROUP, priority=5, block=True)
-
-@settlement.handle()
-async def _(bot: Bot, event: GroupMessageEvent):
-    msg = russian_manager.settlement(event)
-    if msg:
-        await settlement.send(msg, at_sender=True)
-        await russian_manager.end_game(bot, event)
-    else:
-        await settlement.finish()
-
-fold = on_command("结束", permission=GROUP, priority=5, block=True)
-
-@fold.handle()
-async def _(bot: Bot, event: GroupMessageEvent):
-    await russian_manager.fold(bot, event)
-
-# 俄罗斯轮盘
-
-russian = on_command("俄罗斯轮盘", aliases={"装弹", "俄罗斯转盘"}, permission=GROUP, priority=5, block=True)
-
-@russian.handle()
-async def _(bot: Bot,event: GroupMessageEvent, arg: Message = CommandArg()):
-    try:
-        _msg = await russian_manager.check_current_game(bot, event)
-        if _msg:
-            await russian.finish(_msg)
-    except KeyError:
-        pass
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        bullet_num = 1
-        money = 200
-        msg = msg.split()
-        if len(msg) == 1:
-            msg = msg[0]
-            if is_number(msg) and 0 < int(msg):
-                if int(msg) < 7:
-                    bullet_num = int(msg)
+                if overtime > 30:
+                    return None
                 else:
-                    money = int(msg)
+                    return f'现在是 {user_data[player1_id].group_accounts[event.group_id].nickname} 发起的对决，请等待比赛结束后再开始下一轮...'
+
+    def try_create_game(self, event:GroupMessageEvent):
+        """
+        根据event创建游戏
+        如果创建失败则返回提示
+        如果创建成功则返回None
+        """
+        if msg := self.create_check(event):
+            return msg
         else:
-            msg[0] = msg[0].strip()  
-            msg[1] = msg[1].strip()         
-            if is_number(msg[0]) and 0 < int(msg[0]) < 7:
-                bullet_num = int(msg[0])
-            if is_number(msg[1]) and 0 < int(msg[1]):
-                money = int(msg[1])
-
-        user_money = russian_manager.get_user_data(event)["gold"]
-
-        if money > max_bet_gold:
-            await russian.finish(f"单次金额不能超过{max_bet_gold}", at_sender=True)
-        if money > user_money:
-            await russian.finish("你没有足够的金币支撑这场挑战", at_sender=True)
-
-        player1_name = event.sender.card or event.sender.nickname
-        at_ = get_message_at(event.json())
-        if at_:
-            at_ = at_[0]
-            at_player_name = await bot.get_group_member_info(group_id=event.group_id, user_id=int(at_))
-            at_player_name = at_player_name["card"] or at_player_name["nickname"]
-            msg = (
-                f"{player1_name} 向 {MessageSegment.at(at_)} 发起挑战！\n"
-                f"请 {at_player_name} 回复 接受挑战 or 拒绝挑战\n"
-                "【30秒内有效】"
-                )
+            self.create(event)
+    def try_join_game(self, event:GroupMessageEvent):
+        """
+        根据event加入游戏
+        如果加入失败则返回提示
+        如果加入成功则返回None
+        """
+        if time.time() - self.time > 60:
+            return "这场对决邀请已经过时了，请重新发起决斗..."
+        user_id = event.user_id
+        if self.player1_id and self.player1_id != user_id and not self.next:
+            if not self.at or self.at == user_id: 
+                self.time = time.time()
+                self.player2_id = user_id
+            else:
+                return f'现在是 {user_data[self.player2_id].group_accounts[event.group_id].nickname} 发起的对决，请等待比赛结束后再开始下一轮...'
         else:
-            at_ = 0
-            msg = (
-                f"{player1_name} 发起挑战！\n"
-                "回复 接受挑战 即可开始对局。\n"
-                "【30秒内有效】"
-                )
-
-        info = {
-            "game":"russian",
-            "bullet_num":bullet_num
-            }
-        _msg = russian_manager.ready_game(event, msg, player1_name, at_, money, info)
-        await russian.send(_msg)
-
-shot = on_command("开枪", aliases={"咔", "嘭", "嘣"}, permission=GROUP, priority=5, block=True)
-
-@shot.handle()  
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    count = arg.extract_plain_text().strip()
-    if is_number(count):
-        count = abs(int(count))
-        if count == 0:
-            count = 7 - russian_manager.get_current_bullet_index(event)
-        if count > 7 - russian_manager.get_current_bullet_index(event):
-            await shot.finish(
-                f"你不能开{count}枪，大于剩余的子弹数量，"
-                f"剩余子弹数量：{7 - russian_manager.get_current_bullet_index(event)}"
-                )
-    else:
-        count = 1
-    await russian_manager.shot(bot, event, count)
-
-# 摇骰子
-dice = on_command("摇骰子",aliases={"摇色子", "掷骰子", "掷色子"}, permission=GROUP, priority=5, block=True)
-
-@dice.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg(),):
-    try:
-        _msg = await russian_manager.check_current_game(bot, event)
-        if _msg:
-            await dice.finish(_msg)
-    except KeyError:
-        pass
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        money = msg[0].strip()
-        if is_number(money) and 0 < int(money):
-            money = int(money)
-            money = money if money else 200
-            user_money = russian_manager.get_user_data(event)["gold"]
-            if money > max_bet_gold * 5:
-                await dice.finish(f"单次金额不能超过{max_bet_gold * 5}", at_sender=True)
-            if money > user_money:
-                await dice.finish("你没有足够的金币支撑这场挑战", at_sender=True)
-
-            player1_name = event.sender.card or event.sender.nickname
-            at_ = get_message_at(event.json())
-            if at_:
-                at_ = at_[0]
-                at_player_name = await bot.get_group_member_info(group_id=event.group_id, user_id=int(at_))
-                at_player_name = at_player_name["card"] or at_player_name["nickname"]
-                msg = (
-                    f"{player1_name} 向 {MessageSegment.at(at_)} 发起挑战！\n"
-                    f"请 {at_player_name} 回复 接受挑战 or 拒绝挑战\n"
-                    "【30秒内有效】"
-                    )
+            return " "
+    def nextround(self):
+        """
+        把session状态切换到下一回合
+        """
+        self.time = time.time()
+        self.round += 1
+        self.next = self.player1_id if self.next == self.player2_id else self.player2_id
+    def shot_check(self, event:GroupMessageEvent):
+        """
+        开枪前检查游戏是否合法
+        如果不合法则返回提示
+        如果合法则返回None
+        """
+        if time.time() - self.time > 60:
+            return "这场对决邀请已经过时了，请重新发起决斗..."
+        user_id = event.user_id
+        if not self.player1_id:
+            return " "
+        if not self.player2_id:
+            if self.player1_id == user_id:
+                return "目前无人接受挑战哦"
             else:
-                at_ = 0
-                msg = (
-                    f"{player1_name} 发起挑战！\n"
-                    "回复 接受挑战 即可开始对局。\n"
-                    "【30秒内有效】"
-                    )
-            info = {"game":"dice"}
-            _msg = russian_manager.ready_game(event, msg, player1_name, at_, money, info)
-            await dice.send(_msg)
-
-dice_open = on_command("取出", aliases={"开数", "开点"},permission=GROUP, priority=5, block=True)
-
-@dice_open.handle()
-async def _(bot: Bot, event: GroupMessageEvent):
-    await russian_manager.dice_open(bot, event)
-
-# 扑克对战
-poker = on_command("扑克对战",aliases={"扑克对决", "扑克决斗"}, permission=GROUP, priority=5, block=True)
-
-@poker.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg(),):
-    try:
-        _msg = await russian_manager.check_current_game(bot, event)
-        if _msg:
-            await poker.finish(_msg)
-    except KeyError:
-        pass
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        money = msg[0].strip()
-        if is_number(money) and 0 < int(money):
-            money = int(money)
-            money = money if money else 200
-            user_money = russian_manager.get_user_data(event)["gold"]
-            if money > max_bet_gold:
-                await poker.finish(f"单次金额不能超过{max_bet_gold}", at_sender=True)
-            if money > user_money:
-                await poker.finish("你没有足够的金币支撑这场挑战", at_sender=True)
-
-            player1_name = event.sender.card or event.sender.nickname
-            at_ = get_message_at(event.json())
-            if at_:
-                at_ = at_[0]
-                at_player_name = await bot.get_group_member_info(group_id=event.group_id, user_id=int(at_))
-                at_player_name = at_player_name["card"] or at_player_name["nickname"]
-                msg = (
-                    f"{player1_name} 向 {MessageSegment.at(at_)} 发起挑战！\n"
-                    f"请 {at_player_name} 回复 接受挑战 or 拒绝挑战\n"
-                    "【30秒内有效】"
-                    )
+                return "请这位勇士先接受挑战"
+        if user_id == self.player1_id or user_id == self.player2_id:
+            if user_id == self.next:
+                return None
             else:
-                at_ = 0
-                msg = (
-                    f"{player1_name} 发起挑战！\n"
-                    "回复 接受挑战 即可开始对局。\n"
-                    "【30秒内有效】"
-                    )
-            info = {"game":"poker"}
-            _msg = russian_manager.ready_game(event, msg, player1_name, at_, money, info)
-            await poker.send(_msg)
-
-poker_play = on_command("出牌", permission=GROUP, priority=5, block=True)
-
-@poker_play.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    card = arg.extract_plain_text().strip()
-    await russian_manager.poker_play(bot, event, card)
-
-# 随机对战
-random_game = on_command("随机对战", permission=GROUP, priority=5, block=True)
-
-@random_game.handle()
-async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
-    try:
-        _msg = await russian_manager.check_current_game(bot, event)
-        if _msg:
-            await random_game.finish(_msg)
-    except KeyError:
-        pass
-
-    user_data = russian_manager.get_user_data(event)
-    
-    if user_data["props"].get("32002",0) < 1:
-        await random_game.finish("只有持有挑战徽章的用户才可发起随机对战。", at_sender=True)
-
-    money = user_data["gold"]
-
-    if money < 200:
-        await random_game.finish("你没有足够的金币支撑这场挑战", at_sender=True)
-
-    player1_name = event.sender.card or event.sender.nickname
-    at_ = get_message_at(event.json())
-    if at_:
-        at_ = at_[0]
-        at_player_name = await bot.get_group_member_info(group_id=event.group_id, user_id=int(at_))
-        at_player_name = at_player_name["card"] or at_player_name["nickname"]
-        msg = (
-            f"{player1_name} 向 {MessageSegment.at(at_)} 发起随机对战！\n"
-            f"请 {at_player_name} 回复 接受挑战 or 拒绝挑战\n"
-            "【30秒内有效】"
-            )
-    else:
-        at_ = 0
-        msg = (
-            f"{player1_name} 发起随机对战！\n"
-            "回复 接受挑战 即可开始对局。\n"
-            "【30秒内有效】"
-            )
-    info = random.choice([{"game":"russian","bullet_num":random.randint(1,6)},{"game":"dice"},{"game":"poker"}])
-    russian_manager.ready_game(event, msg, player1_name, at_, -money, info)
-    await random_game.send(Message(msg))
-
-
-# 关联账户
-connect = on_command("连接账户", aliases = {"关联账户"}, rule = to_me(), priority = 5, block = True)
-
-@connect.handle()
-async def _(bot: Bot, event: MessageEvent, matcher: Matcher):
-    user_id = str(event.user_id)
-    if isinstance(event,GroupMessageEvent):
-        russian_manager._init_player_data(event)
-        global_data = russian_manager.get_global_data(user_id)
-        global_data["connect"] = str(event.group_id)
-        russian_manager.global_data_save()
-        await connect.finish("私聊账户已关联到本群", at_sender=True)
-    else:
-        player = russian_manager._player_data
-        msg = "你的账户\n"
-        group_list = []
-        for group_id in player.keys():
-            if user_id in player[group_id].keys():
-                msg += f'{group_id} 金币：{player[group_id][user_id]["gold"]} 枚\n'
-                group_list.append(group_id)
+                return f"现在是{user_data[self.next].group_accounts[event.group_id].nickname}的回合"
         else:
-            msg += "\n请输入你要关联的群号"
-        matcher.set_arg("group_list", group_list)
-        await asyncio.sleep(2)
-        await connect.send(msg)
-
-@connect.got("group_id")
-
-async def _(bot:Bot, event: MessageEvent, matcher: Matcher, group_id : Message = Arg()):
-    group_id = str(group_id).strip()
-    group_list = matcher.get_arg("group_list")
-    if group_id in group_list:
-        global_data = russian_manager.get_global_data(str(event.user_id))
-        global_data["connect"] = group_id
-        russian_manager.global_data_save()
-        await connect.finish(f"私聊账户已关联到{group_id}")
-    else:
-        await connect.finish(f"未关联")
-
-# 幸运花色
-slot = on_command("幸运花色", aliases={"抽花色"}, permission = PRIVATE, priority=5, block=True)
-
-@slot.handle()
-async def _(bot: Bot, event: PrivateMessageEvent,arg: Message = CommandArg()):
-    gold = 50
-    if arg:
-        arg = str(arg)
-        if is_number(arg):
-            gold = abs(int(arg))
-    else:
-        gold = 50
-
-    msg = russian_manager.slot(event,gold)
-    await slot.finish(msg, at_sender=True)
-
-# 抽卡
-gacha = on_regex("^.+连抽?卡?|单抽", rule = to_me(), priority = 5, block = True)
-
-@gacha.handle()
-async def _(bot: Bot, event: MessageEvent):
-    cmd = event.get_plaintext()
-    N = re.search(r"^(.*)连抽?卡?$",cmd)
-    if N:
-        N = N.group(1)
-        N = number(N)
-    else:
-        N = 1
-
-    if N and 0 < N <= 200:
-        msg = russian_manager.gacha(event,N)
-        await gacha.finish(msg)
-
-# 我的
-my_props = on_command("我的道具", aliases={"我的仓库"}, priority=5, block=True)
-
-@my_props.handle()
-async def _(event: MessageEvent):
-    msg = russian_manager.my_props(event)
-    await my_props.finish(msg)
-
-my_gold = on_command("我的金币", priority=5, block=True)
-
-@my_gold.handle()
-async def _(event: MessageEvent):
-    user_data = russian_manager.try_get_user_data(event)[0]
-    if user_data:
-        await my_gold.finish(f'你还有 {user_data["gold"]} 枚金币', at_sender=True)
-    else:
-        await my_gold.finish('私聊未关联账户，请发送【关联账户】关联群内账户。')
-
-my_info = on_command("我的信息", aliases={"我的资料"}, priority=5, block=True)
-
-@my_info.handle()
-async def _(event: MessageEvent):
-    info = russian_manager.my_info(event)
-    if info:
-        output = text_to_png(info[:-1], 12)
-        await my_info.finish(MessageSegment.image(output))
-    else:
-        await my_info.finish('私聊未关联账户，请发送【关联账户】关联群内账户。')
-
-# 查看排行榜
-russian_rank = on_command(
-    "金币排行",
-    aliases = {"胜场排行", "胜利排行", "败场排行", "失败排行", "欧洲人排行", "慈善家排行"},
-    permission=GROUP,
-    priority=5,
-    block=True,
-    )
-
-@russian_rank.handle()
-async def _(event: GroupMessageEvent):
-    msg = await russian_manager.rank(event.raw_message, event.group_id)
-    if msg:
-        output = text_to_png(msg)
-        await russian_rank.finish(MessageSegment.image(output))
-    else:
-        await russian_rank.finish()
+            player1_name = user_data[self.player1_id].group_accounts[event.group_id].nickname
+            player2_name = user_data[self.player2_id].group_accounts[event.group_id].nickname
+            return f"{player1_name} v.s. {player2_name}\n正在进行中..."
+
+current_games:Dict[int,Session] = {}
+
+def accept(event:GroupMessageEvent):
+    """
+    接受挑战
+    """
+    global current_games
+    session = current_games[event.group_id]
+    if msg := session.try_join_game(event):
+        return None if msg == " " else msg
+    group_account = Manager.locate_user(event)[1]
+    if session.info["game"] == "random":
+        session.gold = random.randint(0, 0 if(mingold := min(group_account.gold,session.info["gold"])) < 0 else mingold) if session.gold == -1 else session.gold
+        game = random.choice(["russian","dice","poker","lucky_number"])
+        if game == "russian":
+            session.info = russian_info(random.randint(1,6))
+        elif game == "dice":
+            session.info = dice_info(session.gold)
+        elif game == "poker":
+            session.info = poker_info()
+        elif game == "lucky_number":
+            session.info = lucky_number_info(session.gold)
+    elif group_account.gold <  session.gold:
+        return Message(MessageSegment.at(event.user_id) + f"你的金币不足以接受这场对决！\n——你还有{group_account.gold}枚金币。")
+    session.next = session.player1_id
+    return acceptmessage(session)
+
+def acceptmessage(session:Session):
+    """
+    生成接受挑战的提示信息
+    """
+    game = session.info.get("game")
+    if game == "russian":
+        gold = session.gold
+        tip1 = "本场对决为【俄罗斯轮盘】\n"
+        tip2 = "开枪！"
+    elif game == "dice":
+        gold = session.info["max_gold"]
+        tip1 = "本场对决为【掷色子】\n"
+        tip2 = "开数！"
+    elif game == "poker":
+        gold = session.gold
+        tip1 = "本场对决为【扑克对战】\n"
+        tip2 = "出牌！\n"
+        tip2 += MessageSegment.image(text_to_png(
+            "P1初始状态\n"
+            f'HP {session.info["P1"]["HP"]} SP {session.info["P1"]["SP"]} DEF {session.info["P1"]["DEF"]}\n'
+            "——————————————\n"
+            "P2初始状态\n"
+            f'HP {session.info["P2"]["HP"]} SP {session.info["P2"]["SP"]} DEF {session.info["P2"]["DEF"]}\n'
+            "——————————————\n"
+            "P1初始手牌\n" + 
+            "".join([f'【{pokerACT.suit[suit]}{pokerACT.point[point]}】' for suit, point in session.info["P1"]["hand"]])
+            ),30)
+    elif game == "lucky_number":
+        gold = session.gold
+        tip1 = "本场对决为【猜数字】\n"
+        tip2 = "发送数字"
+    else:
+        gold = session.gold
+        tip1 = ""
+    return Message(
+        f"{MessageSegment.at(session.player2_id)}接受了对决！\n" +
+        tip1 +
+        f"赌注为 {gold} 金币\n" +
+        f"请{MessageSegment.at(session.player1_id)}{tip2}"
+        )
 
-# 查看路灯挂件
-name_list = on_command("查看路灯挂件",aliases={"查看路灯","查看挂件"},permission=GROUP, priority=5, block=True)
+def refuse(event:GroupMessageEvent):
+    """
+    拒绝挑战
+    """
+    global current_games
+    group_id = event.group_id
+    session = current_games[group_id]
+    if time.time() - session.time > 60:
+        del current_games[group_id]
+        return None
+    if session.at == event.user_id:
+        if session.player2_id:
+            return "对决已开始，拒绝失败。"
+        else:
+            del current_games[group_id]
+            return "拒绝成功，对决已结束。"
 
-@name_list.handle()
-async def _(event: GroupMessageEvent):
-    group_id = str(event.group_id)
-    player_data = russian_manager._player_data
-    all_user = list(player_data[group_id].keys())
-    all_user_data = [player_data[group_id][x]["Achieve_revolution"] for x in all_user]
-    if all_user:
-        rst = ""
-        for _ in range(len(all_user)):
-            _max = max(all_user_data)
-            if _max == 0:
-                break
-            _max_id = all_user[all_user_data.index(_max)]
-            player_data[group_id][_max_id]["Achieve_revolution"]
-            name = player_data[group_id][_max_id]["nickname"]
-            rst += f"{name}：达成{_max}次\n"
-            all_user_data.remove(_max)
-            all_user.remove(_max_id)
-        if rst:
-            await name_list.finish("☆ ☆ 路灯挂件榜 ☆ ☆\n" + rst[:-1])
+async def overtime(bot:Bot, event:GroupMessageEvent):
+    """
+    超时结算
+    """
+    global current_games
+    session = current_games[event.group_id]
+    if (time.time() - session.time > 30 and
+        session.player1_id and
+        session.player2_id):
+        await end(bot, event)
+
+async def fold(bot:Bot, event:GroupMessageEvent):
+    """
+    认输
+    """
+    global current_games
+    session = current_games[event.group_id]
+    user_id = event.user_id
+    if (time.time() - session.time < 60 and
+        session.player1_id and
+        session.player2_id and
+        user_id == session.player1_id or user_id == session.player2_id):
+        session.win = session.player1_id if user_id == session.player2_id else session.player2_id
+        await end(bot, event)
+
+def start(event:GroupMessageEvent, gold:int, max_bet_gold:int = max_bet_gold) -> Tuple[bool,Message]:
+    """
+    发起游戏
+    """
+    if gold > max_bet_gold:
+        return  False, Message(MessageSegment.at(event.user_id) + f"对战金额不能超过{max_bet_gold}")
+    group_account = Manager.locate_user(event)[1]
+    if gold > group_account.gold:
+        return  False, Message(MessageSegment.at(event.user_id) + f"你没有足够的金币支撑这场对决。\n——你还有{group_account.gold}枚金币。")
+
+    global current_games
+    group_id = event.group_id
+    session = current_games.setdefault(group_id,Session())
+    if msg := session.try_create_game(event):
+        return False, msg
+
+    if at := session.at:
+        if at not in group_data[group_id].namelist:
+            del current_games[group_id]
+            return False, "没有对方的注册信息。"
+        player1_name = user_data[session.player1_id].group_accounts[event.group_id].nickname
+        player2_name = user_data[at].group_accounts[event.group_id].nickname
+        msg = (f"{player1_name} 向 {player2_name} 发起挑战！\n"
+               f"请 {player2_name} 回复 接受挑战 or 拒绝挑战\n"
+               "【30秒内有效】")
+    else:
+        player1_name = user_data[session.player1_id].group_accounts[event.group_id].nickname
+        msg = (f"{player1_name} 发起挑战！\n"
+               "回复 接受挑战 即可开始对局。\n"
+               "【30秒内有效】")
+    session.round += 1
+    return True, msg
+
+"""+++++++++++++++++
+——————————
+     俄罗斯轮盘
+——————————
++++++++++++++++++"""
+
+def random_bullet(bullet_num:int):
+    """
+    随机子弹排列
+        bullet_num:装填子弹数量
+    """
+    bullet_lst = [0, 0, 0, 0, 0, 0, 0]
+    for i in random.sample([0, 1, 2, 3, 4, 5, 6], bullet_num):
+        bullet_lst[i] = 1
+    return bullet_lst
+
+def russian_info(bullet_num):
+    """
+    生成俄罗斯轮盘游戏内容
+    """
+    return {
+        "game":"russian",
+        "bullet_num":bullet_num,
+        "bullet":random_bullet(bullet_num),
+        "index":0
+        }
+
+def russian(event:GroupMessageEvent, bullet_num:int, gold:int):
+    """
+    发起游戏：俄罗斯轮盘
+        bullet_num:装填子弹数量
+    """
+    flag, msg = start(event, gold)
+    if flag == False:
+        return msg
+    session = current_games[event.group_id]
+    session.gold = gold
+    session.info = russian_info(bullet_num)
+    return (("咔 " * bullet_num)[:-1] + "，装填完毕\n"
+            f"挑战金额：{gold}\n"
+            f"第一枪的概率为：{round(bullet_num / 7.0 * 100,2)}%\n"
+            f"{msg}")
+
+async def russian_shot(bot:Bot, event:GroupMessageEvent, count:int):
+    """
+    开枪！！！
+    """
+    global current_games
+    session = current_games[event.group_id]
+    if msg := session.shot_check(event):
+        return None if msg == " " else msg
+    index = session.info["index"]
+    MAG = session.info["bullet"][index:]
+    count = len(MAG) if count < 1 else count
+    msg = f"连开{count}枪！\n" if count > 1 else ""
+    if 1 in MAG[:count]:
+        session.win = session.player1_id if event.user_id == session.player2_id else session.player2_id
+        await bot.send(event,(
+            MessageSegment.at(event.user_id) + msg +
+            random.choice(["嘭！，你直接去世了","眼前一黑，你直接穿越到了异世界...(死亡)","终究还是你先走一步..."]) +
+            f"\n第 {index + MAG.index(1) + 1} 发子弹送走了你..."
+            ))
+        await end(bot, event)
+    else:
+        session.nextround()
+        session.info["index"] += count
+        next_name = user_data[session.next].group_accounts[event.group_id].nickname
+        await bot.send(event,msg + (
+            random.choice(["呼呼，没有爆裂的声响，你活了下来",
+                           "虽然黑洞洞的枪口很恐怖，但好在没有子弹射出来，你活下来了",
+                           f'{"咔 "*count}，看来运气不错，你活了下来']) +
+            f"\n下一枪中弹的概率：{round(session.info['bullet_num'] * 100 / (len(MAG) - count),2)}%\n"
+            f"轮到 {next_name}了"
+            ))
+
+"""+++++++++++++++++
+——————————
+       掷色子
+——————————
++++++++++++++++++"""
+
+def dice_pt(dice_array:list) -> int:
+    """
+    计算骰子排列pt
+    """
+    pt = 0
+    for i in range(1,7):
+        if dice_array.count(i) <= 1:
+            pt += i * dice_array.count(i)
+        elif dice_array.count(i) == 2:
+            pt += (100 + i) * (10 ** dice_array.count(i))
         else:
-            await name_list.finish("群内没有路灯挂件。")
+            pt += i * (10 ** (2 + dice_array.count(i)))
     else:
-        await name_list.finish()
+        return pt
 
-# 公司上市
-Market_public = on_command("市场注册",aliases={"公司注册","注册公司"},rule = to_me(),permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=5, block=True)
-
-@Market_public.handle()
-async def _(event: GroupMessageEvent,arg: Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 1:
-            msg = msg[0]
-            if is_number(msg):
-                await Market_public.finish("错误：公司名称不可以是数字。")
-            else:
-                msg = market_manager.public(event,msg)
-                await Market_public.finish(msg)
+def dice_pt_analyses(pt:int) -> str:
+    """
+    分析骰子pt
+    """
+    array_type = ""
+    if (yiman := int(pt/10000000)) > 0:
+        pt -= yiman * 10000000
+        array_type += f"役满 {yiman} + "
+    if (chuan := int(pt/1000000)) > 0:
+        pt -= chuan * 1000000
+        array_type += f"串 {chuan} + "
+    if (tiao := int(pt/100000)) > 0:
+        pt -= tiao * 100000
+        array_type += f"条 {tiao} + "
+    if (dui := int(pt/10000)) > 0:
+        if dui == 1:
+            pt -= 10000
+            dui = int(pt/100)
+            array_type += f"对 {dui} + "
         else:
-            await Market_public.finish(f"错误：公司名称格式错误\n{str(msg)}")
-    else:
-        await Market_public.finish("错误：未设置公司名称")
+            pt -= 20000
+            dui = int(pt/100)
+            array_type += f"两对 {dui} + "
+        pt -= dui * 100
+    if pt>0:
+        array_type += f"散 {pt} + "
+    return array_type[:-3]
+
+def dice_list(dice_array:list) -> str:
+    """
+    把骰子列表转成字符串
+    """
+    lst_dict = {0:"〇",1:"１",2:"２",3:"３",4:"４",5:"５",6:"６",7:"７",8:"８",9:"９"}
+    return " ".join(lst_dict[x] for x in dice_array)
+
+def dice_info(gold):
+    """
+    生成掷色子游戏内容
+    """
+    return {
+        "game":"dice",
+        "max_gold":gold,
+        "dice_array1":[random.randint(1,6) for i in range(5)],
+        "dice_array2":[random.randint(1,6) for i in range(5)],
+        }
+
+def dice(event:GroupMessageEvent, gold:int):
+    """
+    发起游戏：掷色子
+    """
+    flag, msg = start(event, gold, max_bet_gold * 10)
+    if flag == False:
+        return msg
+    session = current_games[event.group_id]
+    session.gold = int(gold/10)
+    session.info = dice_info(gold)
+    return ("哗啦哗啦~，骰子准备完毕\n"
+            f"挑战金额：{gold}\n"
+            f"{msg}")
+
+async def dice_open(bot:Bot, event:GroupMessageEvent):
+    """
+    开数！！！
+    """
+    group_id = event.group_id
+    global current_games
+    session = current_games[group_id]
+    if msg := session.shot_check(event):
+        return None if msg == " " else msg
 
-# 发行购买
-company_buy = on_command("发行购买",aliases={"发行买入"}, priority=5, block=True)
+    session.gold = int(session.info["max_gold"] * session.round/10)
 
-@company_buy.handle()
-async def _(event: MessageEvent, arg:Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 2:
-            company_name = msg[0]
-            stock = abs(int(msg[1])) if is_number(msg[1]) else 100
-            msg = market_manager.company_buy(event,company_name,stock)
-            try:
-                await company_buy.send(msg)
-            except:
-                output = text_to_png(msg)
-                await company_buy.send(MessageSegment.image(output))
-            finally:
-                await company_buy.finish()
-
-# 债务清算
-company_clear = on_command("官方结算", priority=5, block=True)
-
-@company_clear.handle()
-async def _(event:MessageEvent, arg:Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 2:
-            company_name = msg[0]            
-            stock = abs(int(msg[1])) if is_number(msg[1]) else 100
-            msg = market_manager.company_clear(event,company_name,stock)
-            try:
-                await company_clear.send(msg)
-            except:
-                output = text_to_png(msg)
-                await company_clear.send(MessageSegment.image(output))
-            finally:
-                await company_clear.finish()
-
-# 市场买入
-Market_buy = on_command("买入",aliases={"购买","购入"}, priority=5, block=True)
-
-@Market_buy.handle()
-async def _(event:MessageEvent, arg: Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 2:
-            company_name = msg[0]            
-            stock = abs(int(msg[1])) if is_number(msg[1]) else 100
-            msg = market_manager.Market_buy(event,company_name,stock)
-            try:
-                await Market_buy.send(msg)
-            except:
-                output = text_to_png(msg)
-                await Market_buy.send(MessageSegment.image(output))
-            finally:
-                await Market_buy.finish()
-
-# 市场卖出
-Market_sell = on_command("卖出",aliases={"出售","上架"}, priority=5, block=True)
-
-@Market_sell.handle()
-async def _(event:MessageEvent, arg: Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split()
-        if len(msg) == 3:
-            company_name = msg[0]
-            if is_number(msg[1]):
-                quote = abs(float(msg[1]))
-                stock = abs(int(msg[2])) if is_number(msg[2]) else 100
-                msg = market_manager.Market_sell(event,company_name,quote,stock)
-                try:
-                    await Market_sell.send(msg)
-                except:
-                    output = text_to_png(msg)
-                    await Market_sell.send(MessageSegment.image(output))
-                finally:
-                    await Market_sell.finish()
-
-# 市场信息
-Market_info = on_command("市场信息",aliases={"查看市场","市场行情","市场走势"}, priority=5, block=True)
-
-@Market_info.handle()
-async def _(bot:Bot, event: MessageEvent,arg: Message = CommandArg()):
-    cmd = event.raw_message
-    if "市场行情" in cmd or "市场走势" in cmd:
-        await Market_info.send("正在生成走势图。")
-        company_name = "pro"
-    else:
-        company_name = arg.extract_plain_text().strip()
-        if company_name:
-            company_name = company_name.split()
-            company_name = company_name[0]
-        else:
-            company_name == ""
+    player1_id = session.player1_id
+    player2_id = session.player2_id
 
-    msg = await market_manager.Market_info(event,company_name)
+    dice_array1 = (session.info["dice_array1"][:int(session.round/2+0.5)] + [0, 0, 0, 0, 0])[:5]
+    dice_array2 = (session.info["dice_array2"][:int(session.round/2)] + [0, 0, 0, 0, 0])[:5]
+    
+    dice_array1.sort(reverse=True)
+    dice_array2.sort(reverse=True)
 
-    if type(msg) == list:
-        if len(msg) == 1:
-            await Market_info.finish(msg[0]["data"]["content"])
-        else:
-            if isinstance(event, GroupMessageEvent):
-                await bot.send_group_forward_msg(group_id = event.group_id, messages = msg)
-            else:
-                await bot.send_private_forward_msg(user_id = event.user_id, messages = msg)
-        await Market_info.finish()
-    else:
-        await Market_info.finish(msg)
+    pt1 = dice_pt(dice_array1)
+    pt2 = dice_pt(dice_array2)
 
-# 公司信息
-company_info = on_command("公司信息",aliases={"公司资料"}, priority=5, block=True)
+    session.win = player1_id if pt1 > pt2 else player2_id
+    session.nextround()
 
-@company_info.handle()
-async def _(event: MessageEvent,arg: Message = CommandArg()):
-    company_name = arg.extract_plain_text().strip()
-    if company_name:
-        company_name = company_name.split()
-        company_name = company_name[0]
-        msg = market_manager.company_info(company_name)
-        if msg:
-            ohlc = [Path(linechart_cache / company_name), Path(candlestick_cache / company_name)]
-            if os.path.exists(ohlc[0]) and os.path.exists(ohlc[1]):
-                output = company_info_Splicing(msg ,ohlc)
+    next_name = "结算" if session.round > 10 else user_data[session.next].group_accounts[group_id].nickname
+    msg = (
+        f'玩家：{user_data[player1_id].group_accounts[group_id].nickname}\n'
+        f"组合：{dice_list(dice_array1)}\n"
+        f"点数：{dice_pt_analyses(pt1)}\n"
+        "———————————\n"
+        f'玩家：{user_data[player2_id].group_accounts[group_id].nickname}\n'
+        f"组合：{dice_list(dice_array2)}\n"
+        f"点数：{dice_pt_analyses(pt2)}\n"
+        "———————————\n"
+        f"结算金额：{session.gold}\n"
+        f'领先：{user_data[session.win].group_accounts[group_id].nickname}\n'
+        f'下一回合：{next_name}'
+        )
+    await bot.send(event,message = MessageSegment.image(text_to_png(msg,30)))
+    if session.round > 10:
+        await end(bot, event)
+
+"""+++++++++++++++++
+——————————
+      扑克对战
+——————————
++++++++++++++++++"""
+
+def random_poker():
+    """
+    生成随机牌库
+    """
+    poker_deck = [[i,j] for i in range(1,5) for j in range(1,14)]
+    random.shuffle(poker_deck)
+    return poker_deck
+
+def poker_info():
+    """
+    生成扑克对战游戏内容
+    """
+    deck = random_poker()
+    hand = deck[0:3].copy()
+    del deck[0:3]
+    return {
+        "game":"poker",
+        "deck":deck + [[0,0],[0,0],[0,0],[0,0]],
+        "ACT":1,
+        "P1":{"hand":hand,"HP":20,"ATK":0,"DEF":0,"SP":0},
+        "P2":{"hand":[],"HP":25,"ATK":0,"DEF":0,"SP":2}
+        }
+
+def poker(event:GroupMessageEvent, gold:int):
+    """
+    发起游戏：扑克对战
+    """
+    flag, msg = start(event, gold)
+    if flag == False:
+        return msg
+    session = current_games[event.group_id]
+    session.gold = gold
+    session.info = poker_info()
+    return ("唰唰~，随机牌库已生成\n"
+            f"挑战金额：{gold}\n"
+            f"{msg}")
+
+class pokerACT():
+    suit = {0:"结束",1:"防御",2:"恢复",3:"技能",4:"攻击"}
+    point = {0:"0",1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11",12:"12",13:"13"}
+    @classmethod
+    def action_ACE(cls, Active:dict, roll:int = 1) -> str:
+        '''
+        手牌全部作为技能牌（ACE技能）
+            Active:行动牌生效对象
+        '''
+        card_msg = "技能牌为"
+        skill_msg = "\n"
+        for card in Active["hand"]:
+            suit = card[0]
+            point = roll if card[1] == 1 else card[1]
+            card_msg += f'【{cls.suit[suit]} {cls.point[point]}】'
+            if suit == 1:
+                Active["DEF"] += point
+                skill_msg += f'♤防御力强化了 {point}\n'
+            elif suit == 2:
+                Active["HP"] += point
+                skill_msg += f'♡生命值增加了 {point}\n'
+            elif suit == 3:
+                Active["SP"] += point + point
+                skill_msg += f'♧技能点增加了 {point}\n'
+            elif suit == 4:
+                Active["ATK"] += point
+                skill_msg += f'♢发动了攻击 {point}\n'
             else:
-                output = text_to_png(msg)
-            await company_info.finish(MessageSegment.image(output))
+                return "出现未知错误"
+            Active["SP"] -= point
+            Active["SP"] = 0 if Active["SP"] < 0 else Active["SP"]
+        return card_msg + skill_msg[:-1]
+    @classmethod
+    def action(cls, index:int, Active:dict) -> str:
+        '''
+        行动牌生效
+            index:手牌序号
+            Active:行动牌生效对象
+        '''
+        card = Active["hand"][index]
+        suit = card[0]
+        point = card[1]
+        if point == 1:
+            roll = random.randint(1,6)
+            msg = f'发动ACE技能！六面骰子判定为 {roll}\n'
+            msg += cls.action_ACE(Active, roll)
         else:
-            await company_info.finish(f"【{company_name}】未注册")
-# 更新公司简介
-update_intro = on_command("更新公司简介",aliases={"添加公司简介"},permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=5, block=True)
-
-@update_intro.handle()
-async def _(event: GroupMessageEvent,arg: Message = CommandArg()):
-    intro = arg.extract_plain_text().strip()
-    group_id = str(event.group_id)
-    if intro:
-        if group_id in market_manager._market_data.keys():
-            company_name = market_manager._market_data[group_id]["company_name"]
-            market_manager.update_intro(company_name,intro)
-            await update_intro.finish("简介更新完成...")
+            if suit == 1:
+                Active["ATK"] += point
+                msg = f"♤发动了攻击{point}"
+            elif suit == 2:
+                Active["HP"] += point
+                msg = f"♡生命值增加了{point}"
+            elif suit == 3:
+                Active["SP"] += point
+                msg = f"♧技能点增加了{point}...\n"
+                roll = random.randint(1,20)
+                if Active["SP"] < roll:
+                    msg += f'二十面骰判定为{roll}点，当前技能点{Active["SP"]}\n技能发动失败...'
+                else:
+                    del Active["hand"][index]
+                    msg += f'二十面骰判定为{roll}点，当前技能点{Active["SP"]}\n技能发动成功！\n'
+                    msg += cls.action_ACE(Active)
+            elif suit == 4:
+                Active["ATK"] = point
+                msg = f"♢发动了攻击{point}"
+            else:
+                msg = "出现未知错误"
+        return msg
+    @classmethod
+    def skill(cls, card:list, Player:dict) -> str:
+        '''
+        技能牌生效
+            card:技能牌
+            Player:技能牌生效对象
+        '''
+        suit = card[0]
+        point = card[1]
+        msg = f'技能牌为【{cls.suit[suit]} {cls.point[point]}】\n'
+        if suit == 1:
+            Player["DEF"] += point
+            msg += f"♤发动了防御 {point}"
+        elif suit == 2:
+            Player["HP"] += point
+            msg += f"♡生命值增加了 {point}"
+        elif suit == 3:
+            Player["SP"] += point + point
+            msg += f"♧技能点增加了 {point}"
+        elif suit == 4:
+            Player["ATK"] += point
+            msg += f"♢发动了反击 {point}"
         else:
-            await update_intro.finish(f"群号：{group_id}未注册")
-    else:
-        await update_intro.finish()
-
-# 管理员更新简介
-update_intro_superuser = on_command("管理员更新公司简介",aliases={"管理员更新公司简介"},permission=SUPERUSER, priority=5, block=True)
-
-@update_intro_superuser.handle()
-async def _(event: GroupMessageEvent,arg: Message = CommandArg()):
-    msg = arg.extract_plain_text().strip()
-    if msg:
-        msg = msg.split(" ",1)
-        market_manager.update_intro(msg[0],msg[1])
-        await update_intro_superuser.finish("简介更新完成...")
-
-# 跨群转移金币到自己的账户
-intergroup_transfer = on_command("金币转移", permission=GROUP, priority=5, block=True)
-
-@intergroup_transfer.handle()
-async def _(event: GroupMessageEvent,arg: Message = CommandArg()):
-    msg = arg.extract_plain_text().strip().split()
-    if len(msg) == 2 and is_number(msg[1]):
-        company_name = msg[0]
-        gold = msg[1]
-        msg = market_manager.intergroup_transfer(event,company_name,gold)
-        await intergroup_transfer.finish(msg, at_sender=True)
-
-# 清理无效账户
-delist = on_command("清理无效账户", rule = to_me() , permission = SUPERUSER, priority=5, block = True)
-
-@delist.handle()
-async def _(bot:Bot, event:MessageEvent):
-    await delist.send("正在启动清理程序。")
-    msg = await market_manager.delist(bot,event)
-    await delist.finish(msg)
-
-# 我的资产
-self_survey = on_command("我的资产", priority=5, block = True)
-@self_survey.handle()
-async def _(bot:Bot, event:MessageEvent):
-    msg = await market_manager.survey(bot,event,str(event.user_id))
-    await survey.send(msg)
-
-# 资产调查
-survey = on_command("资产调查", permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=5, block = True)
-
-@survey.handle()
-async def _(bot:Bot, event:MessageEvent):
-    at = get_message_at(event.json())
-    if at:
-        await russian_manager._init_at_player_data(bot,event,at[0])
-        msg = await market_manager.survey(bot,event,str(at[0]))
-        await survey.send(msg)
+            msg += "启动结算程序"
+        Player["SP"] -= point
+        Player["SP"] = 0 if Player["SP"] < 0 else Player["SP"]
+        return msg
+
+async def poker_play(bot:Bot, event:GroupMessageEvent, index:str):
+    """
+    出牌
+    """
+    group_id = event.group_id
+    global current_games
+    session = current_games[group_id]
+    if session.info["ACT"] == 0:
+        return
+    if msg := session.shot_check(event):
+        return None if msg == " " else msg
+    if index not in ["1","2","3"]:
+        return "请发送【出牌 1/2/3】打出你的手牌。"
+
+    session.info["ACT"] = 0
+    session.nextround()
+
+    deck = session.info["deck"]
+
+    if event.user_id == session.player1_id:
+        Active = session.info["P1"]
+        Passive = session.info["P2"]
     else:
-        msg = await market_manager.survey(bot,event,None)
-        if isinstance(event, GroupMessageEvent):
-            await bot.send_group_forward_msg(group_id = event.group_id, messages = msg)
+        Active = session.info["P2"]
+        Passive = session.info["P1"]  
+        
+    # 出牌判定
+    msg = pokerACT.action(int(index) - 1,Active)
+    try:
+        await bot.send(event,message = msg,at_sender=True)
+    except:
+        await bot.send(event,message = MessageSegment.image(text_to_png(msg,30)))
+
+    await asyncio.sleep(0.03*len(msg))
+
+    # 敌方技能判定
+    next_name = user_data[session.next].group_accounts[group_id].nickname
+    if Passive["SP"] > 0:
+        roll = random.randint(1,20)
+        if  Passive["SP"] < roll:
+            msg = f'{next_name} 二十面骰判定为{roll}点，当前技能点{Passive["SP"]}\n技能发动失败...'
         else:
-            await bot.send_private_forward_msg(user_id = event.user_id, messages = msg)
+            msg = f'{next_name} 二十面骰判定为{roll}点，当前技能点{Passive["SP"]}\n技能发动成功！\n'
+            msg += pokerACT.skill(deck[0], Passive)
+            del deck[0]
 
-# 冻结个人资产
-freeze = on_command("冻结资产", permission = SUPERUSER, priority = 5, block = True)
-
-@freeze.handle()
-async def _(bot: Bot, event: MessageEvent, matcher: Matcher):
-    at = get_message_at(event.json())
-    if at:
-        at = at[0]
-        nickname = (await bot.get_group_member_info(group_id = event.group_id, user_id = at))["nickname"]
-        code = random.randint(1000,9999)
-        matcher.set_arg("freeze", [str(at),str(code)])
-        await freeze.send(f"您即将冻结 {nickname}（{at}），请输入{code}来确认。")
-    else:
-        await freeze.finish("没有选择冻结对象。")
+        try:
+            await bot.send(event,message = msg)
+        except:
+            await bot.send(event,message = MessageSegment.image(text_to_png(msg,30)))
 
-@freeze.got("code")
+    # 回合结算
+    Active["HP"] += Active["DEF"] - Active["ATK"] if Active["DEF"] < Passive["ATK"] else 0
+    Passive["HP"] += Passive["DEF"] - Active["ATK"] if Passive["DEF"] < Active["ATK"] else 0
+
+    Active["ATK"] = 0
+    Passive["ATK"] = 0
+
+    # 防御力强化保留一回合
+    Passive["DEF"] = 0 
+
+    # 下回合准备
+    hand = deck[0:3].copy()
+    Passive["hand"] = hand
+    del deck[0:3]
+
+    next_name = "游戏结束" if Active["HP"] < 1 or Passive["HP"] < 1 or Passive["HP"] >= 40 or [0,0] in hand else next_name
+
+    msg = (
+        f'玩家：{user_data[session.player1_id].group_accounts[group_id].nickname}\n'
+        "状态：\n"
+        f'HP {session.info["P1"]["HP"]} SP {session.info["P1"]["SP"]} DEF {session.info["P1"]["DEF"]}\n'
+        "——————————————\n"
+        f'玩家：{user_data[session.player2_id].group_accounts[group_id].nickname}\n'
+        "状态：\n"
+        f'HP {session.info["P2"]["HP"]} SP {session.info["P2"]["SP"]} DEF {session.info["P2"]["DEF"]}\n'
+        "——————————————\n"
+        f'当前回合：{next_name}\n'
+        "手牌：\n" + 
+        "".join([f'【{pokerACT.suit[suit]}{pokerACT.point[point]}】' for suit, point in Passive["hand"]])
+        )
+    await asyncio.sleep(0.5)
+    await bot.send(event, message = MessageSegment.image(text_to_png(msg,30)))
 
-async def _(bot:Bot, event: MessageEvent, matcher: Matcher, code : Message = Arg()):
-    confirm = matcher.get_arg("freeze")
-    if confirm[1] == str(code):
-        msg = market_manager.freeze(bot,event,confirm[0])
-        await freeze.finish(msg)
+    if next_name == "游戏结束":
+        Passive["HP"] = Passive["HP"] + 100 if Passive["HP"] >= 40 else Passive["HP"]
+        session.win = session.player1_id if session.info["P1"]["HP"] > session.info["P2"]["HP"] else session.player2_id
+        await end(bot, event)
+    else:
+        session.info["ACT"] = 1
+
+"""+++++++++++++++++
+——————————
+      猜数字
+——————————
++++++++++++++++++"""
+
+def lucky_number_info(gold):
+    """
+    生成猜数字游戏内容
+    """
+    return {
+        "game":"lucky_number",
+        "gold":gold,
+        "number":random.randint(1,100),
+        }
+
+def lucky_number(event:GroupMessageEvent, gold:int):
+    """
+    发起游戏：猜数字
+    """
+    flag, msg = start(event, gold)
+    if flag == False:
+        return msg
+    session = current_games[event.group_id]
+    session.gold = gold
+    session.info = lucky_number_info(gold)
+    return (f"随机 1-100 数字已生成。"
+            f"挑战金额：{gold}/次\n"
+            f"{msg}")
+
+async def guess_number(bot:Bot, event:GroupMessageEvent, N:int):
+    """
+    猜数字
+    """
+    group_id = event.group_id
+    global current_games
+    session = current_games[group_id]
+    if msg := session.shot_check(event):
+        return None if msg == " " else msg
+    session.info.setdefault("max",(maxgold if (maxgold := min(
+        user_data[session.player1_id].group_accounts[group_id].gold,
+        user_data[session.player2_id].group_accounts[group_id].gold)) > 0 else 0 ))
+    session.gold = min(session.info["gold"] * session.round, session.info["max"])
+    session.nextround()
+    TrueN = session.info["number"]
+    if N > TrueN:
+        return f"{N}比这个数字大\n金额：{session.gold}"
+    if N < TrueN:
+        return f"{N}比这个数字小\n金额：{session.gold}"
+    session.win = event.user_id
+    await end(bot, event)
+
+
+"""+++++++++++++++++
+——————————
+      随机对战
+——————————
++++++++++++++++++"""
+
+def random_game(event:GroupMessageEvent, gold:int):
+    """
+    发起游戏：随机对战
+    """
+    group_account = Manager.locate_user(event)[1]
+    if group_account.props.get("32002",0) < 1:
+        return f"你未持有持有【{props_library['32002']['name']}】，无法发起随机对战。"
+    flag, msg = start(event, gold)
+    if flag == False:
+        return msg
+    session = current_games[event.group_id]
+    session.gold = gold
+    session.info = {
+        "game":"random",
+        "gold":group_account.gold if gold == -1 else gold
+        }
+    return ("随机对战已生成\n"
+            f"挑战金额：{gold if gold > 0 else '随机'}\n"
+            f"{msg}")
+
+"""+++++++++++++++++
+——————————
+      游戏结束
+——————————
++++++++++++++++++"""
+
+def settle(group_id:int):
+    """
+    游戏结束结算
+        return:结算界面
+    """
+    global current_games
+    session = current_games[group_id]
+    win = session.win if session.win else session.player1_id if session.next == session.player2_id else session.player2_id
+    lose = session.player1_id if session.player2_id == win else session.player2_id
+    winner = user_data[win]
+    winner_group_account = winner.group_accounts[group_id]
+    loser = user_data[lose]
+    loser_group_account = loser.group_accounts[group_id]
+
+    gold = session.gold
+    if winner_group_account.props.get("42001",0) > 0:
+        fee = 0
+        fee_tip = f"『{props_library['42001']['name']}』免手续费"
+    else:
+        rand = random.randint(0, 5)
+        fee = int(gold * rand / 100)
+        fee_tip = f"手续费：{fee}({rand}%)"
+
+    maxgold = int(max_bet_gold/5)
+
+    if winner_group_account.props.get("52002",0) > 0:
+        extra = int(gold *0.1)
+        if extra < maxgold:
+            extra_tip = f"◆『{props_library['52002']['name']}』\n"
+        else:
+            extra = maxgold
+            extra_tip = f"◆『{props_library['52002']['name']}』最大奖励\n"
     else:
-        await freeze.finish("【冻结】已取消。")
+        extra_tip = ""
+        extra = 0
 
-# 刷新每日签到和每日补贴
-reset_sign = on_command("reset_sign", permission=SUPERUSER, priority=5, block=True) # 重置每日签到和每日补贴
+    if gold == loser_group_account.gold and loser_group_account.security < 3:
+        loser_group_account.security += 1
+        security = random.randint(security_gold[0], security_gold[1])
+        security_tip1 = "◇『金币补贴』\n"
+        security_tip2 = f"◇已领取补贴：{security}\n"
+    else:
+        security = 0
+        security_tip1 = ""
+        security_tip2 = ""
+
+    if loser_group_account.props.get("52001",0) > 0:
+        off = int(gold * 0.1)
+        if off < maxgold:
+            off_tip = f"◇『{props_library['52001']['name']}』\n"
+        else:
+            off = maxgold
+            off_tip = f"◇『{props_library['52001']['name']}』最大补贴\n"
 
-@reset_sign.handle()
-@scheduler.scheduled_job("cron", hour = 0)
-async def _():
-    russian_manager.reset_sign()
-    logger.info("今日签到重置成功...")
-    russian_manager.reset_security()
-    logger.info("今日补贴重置成功...")
-     
-# 刷新道具时间
-@scheduler.scheduled_job("cron", hour = 4)
-async def _():
-    for group_id in russian_manager._player_data.keys():
-        for user_id in russian_manager._player_data[group_id].keys():
-            for props in russian_manager._player_data[group_id][user_id]["props"].keys():
-                if russian_manager._player_data[group_id][user_id]["props"][props] > 0 and props[2] == "0":
-                    russian_manager._player_data[group_id][user_id]["props"][props] -= 1
     else:
-        logger.info("道具时间已刷新...")
-        russian_manager.save()
+        off = 0
+        off_tip = ""
 
-# 市场指数更新
-@scheduler.scheduled_job("cron", hour = "0,3,6,9,12,15,18,21")
-async def _():
-    market_manager.reset_market_index()
-
-# 股市更新
-@scheduler.scheduled_job("cron", minute = "0,5,10,15,20,25,30,35,40,45,50,55")
-async def _():
-    for group_id in russian_manager._player_data.keys():
-        for user_id in russian_manager._player_data[group_id].keys():
-            russian_manager._player_data[group_id][user_id]["stock"]["value"] = market_manager.value_update(group_id,user_id)
-
-        if group_id in market_manager._market_data.keys():
-            market_manager.company_update(group_id)
-            logger.info(f'【{market_manager._market_data[group_id]["company_name"]}】更新成功...')
-    else:
-        market_manager.ohlc_temp[1] += 1
-        russian_manager.save()
-        market_manager.market_data_save()
-        market_manager.market_history_save()
-
-# 数据备份
-
-@scheduler.scheduled_job("cron", hour = "4,10,16,22")
-async def _():
-    now = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
-    path =f"{russian_path}/data/russian"
-    if not os.path.exists(f"{path}/backup"):
-        os.makedirs(f"{path}/backup")
-    if os.path.isfile(f"{path}/market_data.json"):
-        shutil.copy(f"{path}/market_data.json",f"{path}/backup/market_data {now}.json")
-        logger.info(f'market_data.json备份成功！')
-    if os.path.isfile(f"{path}/russian_data.json"):
-        shutil.copy(f"{path}/russian_data.json",f"{path}/backup/russian_data {now}.json")
-        logger.info(f'russian_data.json备份成功！')
-    if os.path.isfile(f"{path}/Stock_Exchange.json"):
-        shutil.copy(f"{path}/Stock_Exchange.json",f"{path}/backup/Stock_Exchange {now}.json")
-        logger.info(f'Stock_Exchange.json备份成功！')
-    if os.path.isfile(f"{path}/global_data.json"):
-        shutil.copy(f"{path}/global_data.json",f"{path}/backup/global_data {now}.json")
-        logger.info(f'global_data.json备份成功！')
+    win_gold = gold - fee + extra
+    lose_gold = gold - off
+    winner.win += 1
+    winner.Achieve_win += 1
+    winner.Achieve_lose = 0
+    loser.lose += 1
+    loser.Achieve_lose += 1
+    loser.Achieve_win = 0
+    msg = (
+        f"结算：\n"
+        "——————————————\n" +
+        (tmp + "\n" if (tmp := "\n".join(x for x in Manager.Achieve_list((winner,winner_group_account)))) else "") +
+        extra_tip +
+        f"◆胜者：{winner_group_account.nickname}\n"
+        f"◆结算：{winner_group_account.gold}（+{win_gold}）\n"
+        f"◆战绩：{winner.win}:{winner.lose}\n"
+        f"◆胜率：{round(winner.win * 100 / (winner.win + winner.lose), 2) if winner.win > 0 else 0}%\n"
+        "——————————————\n" +
+        (tmp + "\n" if (tmp := "\n".join(x for x in Manager.Achieve_list((loser,loser_group_account)))) else "") +
+        security_tip1 +
+        off_tip +
+        f"◇败者：{loser_group_account.nickname}\n"
+        f"◇结算：{loser_group_account.gold}（-{lose_gold}）\n" +
+        security_tip2 +
+        f"◇战绩：{loser.win}:{loser.lose}\n"
+        f"◇胜率：{round(loser.win * 100 / (loser.win + loser.lose), 2) if loser.win > 0 else 0}%\n"
+        "——————————————\n" + 
+        fee_tip
+        )
+    winner.gold += win_gold
+    winner_group_account.gold += win_gold
+    loser.gold -= lose_gold - security
+    loser_group_account.gold -= lose_gold - security
+    res = game_str(session)
+    del current_games[group_id]
+    return f"这场对决是 {winner_group_account.nickname} 胜利了", msg, res
+
+def game_str(session:Session):
+    """
+    结束附件
+    """
+    game = session.info["game"]
+    if game == "russian":
+        return " ".join(("—" if x == 0 else "|") for x in session.info["bullet"])
+    if game == "dice":
+        return (f'玩家 1\n'
+                f'组合：{" ".join(str(x) for x in session.info["dice_array1"])}\n'
+                f'玩家 2\n'
+                f'组合：{" ".join(str(x) for x in session.info["dice_array2"])}')
+    else:
+        return ""
+
+async def end(bot:Bot, event:GroupMessageEvent):
+    """
+    输出结算界面
+    """
+    end_info = settle(event.group_id)
+    tmp = MessageSegment.image(text_to_png(end_info[1]))
+    await bot.send(event,end_info[0])
+    await bot.send(event,tmp)
+    await asyncio.sleep(0.5)
+    await bot.send(event,end_info[2])
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/avatar.py` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/utils/avatar.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,30 +1,39 @@
-import io
 import httpx
-import hashlib
 import asyncio
+from io import BytesIO
+from PIL import Image
 
-from nonebot_plugin_imageutils import BuildImage
-
-async def download_avatar(user_id: int) -> bytes:
+async def download_avatar(user_id:int) -> bytes:
     url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640"
-    data = await download_url(url)
-    if hashlib.md5(data).hexdigest() == "acef72340ac0e914090bd35799f5594e":
-        url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=100"
-        data = await download_url(url)
-    return data
+    if data := await download_url(url):
+        return BytesIO(data)
+    url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=100"
+    if data := await download_url(url):
+        return BytesIO(data)
+
+    output = BytesIO()
+    Image.new("RGBA", (300, 300),color = "gray").save(output, format = "png")
+    return output
+
+async def download_groupavatar(group_id:int) -> bytes:
+    url = f"https://p.qlogo.cn/gh/{group_id}/{group_id}/640"
+    if data := await download_url(url):
+        return BytesIO(data)
+    url = f"https://p.qlogo.cn/gh/{group_id}/{group_id}/100"
+    if data := await download_url(url):
+        return BytesIO(data)
 
-async def download_url(url: str) -> bytes:
+    output = BytesIO()
+    Image.new("RGBA", (300, 300),color = "gray").save(output, format = "png")
+    return output
+
+async def download_url(url:str) -> bytes:
     async with httpx.AsyncClient() as client:
         for i in range(3):
             try:
                 resp = await client.get(url, timeout=20)
                 resp.raise_for_status()
                 return resp.content
             except Exception:
                 await asyncio.sleep(3)
-    raise Exception(f"{url} 下载失败！")
-
-async def download_user_img(user_id: int):
-    data = await download_avatar(user_id)
-    img = BuildImage.open(io.BytesIO(data))
-    return img.save_png()
+    return None
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/Stand.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/Stand.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 20% similar despite different names*

```diff
@@ -1,339 +1,334 @@
 00000000: 5b0a 2020 2020 7b0a 2020 2020 2020 2020  [.    {.        
-00000010: 2265 7665 6e74 5f6e 616d 6522 3a20 22e7  "event_name": ".
-00000020: 99bd e987 91e4 b98b e698 9f5f 5374 6172  ..........._Star
-00000030: 2050 6c61 7469 6e75 6d22 2c0a 2020 2020   Platinum",.    
-00000040: 2020 2020 2264 6573 6372 6962 6522 3a20      "describe": 
-00000050: 223c 303e e799 bde9 8791 e4b9 8be6 989f  "<0>............
-00000060: 5f53 7461 7220 506c 6174 696e 756d efbc  _Star Platinum..
-00000070: 88e5 87bb e699 95e4 b880 e59b 9ee5 9088  ................
-00000080: e5b9 b6e5 908e e980 80e4 b880 e4be a7e7  ................
-00000090: 9a84 e9a9 ac31 30e6 ada5 efbc 8922 2c0a  .....10......",.
-000000a0: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-000000b0: 3a20 362c 0a20 2020 2020 2020 2022 7665  : 6,.        "ve
-000000c0: 7274 6967 6f22 3a20 312c 0a20 2020 2020  rtigo": 1,.     
-000000d0: 2020 2022 726f 756e 6473 223a 2031 2c0a     "rounds": 1,.
-000000e0: 2020 2020 2020 2020 226d 6f76 6522 3a20          "move": 
-000000f0: 2d31 302c 0a20 2020 2020 2020 2022 6e61  -10,.        "na
-00000100: 6d65 223a 22e5 87bb e699 9522 0a20 2020  me":"......".   
-00000110: 207d 2c0a 2020 2020 7b0a 2020 2020 2020   },.    {.      
-00000120: 2020 2265 7665 6e74 5f6e 616d 6522 3a20    "event_name": 
-00000130: 22e4 b896 e795 8c5f 5468 6520 576f 726c  "......_The Worl
-00000140: 6422 2c0a 2020 2020 2020 2020 2264 6573  d",.        "des
-00000150: 6372 6962 6522 3a20 223c 303e e4b8 96e7  cribe": "<0>....
-00000160: 958c 5f54 6865 2057 6f72 6c64 efbc 88e7  .._The World....
-00000170: 9ca9 e699 95e9 99a4 e887 aae5 b7b1 e4bb  ................
-00000180: a5e5 a496 e79a 84e6 8980 e69c 89e4 baba  ................
-00000190: 3130 e4b8 aae5 9b9e e590 88ef bc89 222c  10............",
-000001a0: 0a20 2020 2020 2020 2022 7461 7267 6574  .        "target
-000001b0: 223a 2033 2c0a 2020 2020 2020 2020 2276  ": 3,.        "v
-000001c0: 6572 7469 676f 223a 2031 2c0a 2020 2020  ertigo": 1,.    
-000001d0: 2020 2020 2272 6f75 6e64 7322 3a20 3130      "rounds": 10
-000001e0: 2c0a 2020 2020 2020 2020 226e 616d 6522  ,.        "name"
-000001f0: 3a22 e587 bbe6 9995 220a 2020 2020 7d2c  :"......".    },
-00000200: 0a20 2020 207b 0a20 2020 2020 2020 2022  .    {.        "
-00000210: 6576 656e 745f 6e61 6d65 223a 2022 e799  event_name": "..
-00000220: bde9 8791 e4b9 8be6 989f c2b7 e4b8 96e7  ................
-00000230: 958c 5f53 7461 7220 506c 6174 696e 756d  .._Star Platinum
-00000240: c2b7 5468 6520 576f 726c 6422 2c0a 2020  ..The World",.  
-00000250: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-00000260: 3a20 223c 303e e799 bde9 8791 e4b9 8be6  : "<0>..........
-00000270: 989f c2b7 e4b8 96e7 958c 28e5 87bb e699  ..........(.....
-00000280: 95e5 8d81 e59b 9ee5 9088 e5b9 b6e5 908e  ................
-00000290: e980 80e4 b880 e4be a7e7 9a84 e9a9 ac31  ...............1
-000002a0: 30e6 ada5 efbc 8922 2c0a 2020 2020 2020  0......",.      
-000002b0: 2020 2274 6172 6765 7422 3a20 362c 0a20    "target": 6,. 
-000002c0: 2020 2020 2020 2022 7665 7274 6967 6f22         "vertigo"
-000002d0: 3a20 312c 0a20 2020 2020 2020 2022 726f  : 1,.        "ro
-000002e0: 756e 6473 223a 2031 302c 0a20 2020 2020  unds": 10,.     
-000002f0: 2020 2022 6d6f 7665 223a 202d 3130 2c20     "move": -10, 
-00000300: 0a20 2020 2020 2020 2022 6e61 6d65 223a  .        "name":
-00000310: 22e5 87bb e699 95e4 b894 e590 8ee9 8080  "...............
-00000320: 220a 2020 2020 7d2c 0a20 2020 207b 0a20  ".    },.    {. 
-00000330: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00000340: 6d65 223a 2022 e9bb 84e9 8791 e4bd 93e9  me": "..........
-00000350: aa8c 5f47 6f6c 6420 4578 7065 7269 656e  .._Gold Experien
-00000360: 6365 222c 0a20 2020 2020 2020 2022 6465  ce",.        "de
-00000370: 7363 7269 6265 223a 2022 3c30 3ee9 bb84  scribe": "<0>...
-00000380: e987 91e4 bd93 e9aa 8c5f 476f 6c64 2045  ........._Gold E
-00000390: 7870 6572 6965 6e63 65ef bc88 e5a4 8de6  xperience.......
-000003a0: b4bb e5b9 b6e7 9ca9 e699 95e4 b880 e590  ................
-000003b0: 8de4 b8a4 e4b8 aae5 9b9e e590 88ef bc8c  ................
-000003c0: e4b8 94e5 908e e980 80e4 b889 e6ad a5ef  ................
-000003d0: bc89 222c 0a20 2020 2020 2020 2022 7461  ..",.        "ta
-000003e0: 7267 6574 223a 2031 2c0a 2020 2020 2020  rget": 1,.      
-000003f0: 2020 226f 7468 6572 5f62 7566 6622 3a5b    "other_buff":[
-00000400: 226c 6976 6522 2c22 7665 7274 6967 6f22  "live","vertigo"
-00000410: 5d2c 0a20 2020 2020 2020 2022 726f 756e  ],.        "roun
-00000420: 6473 223a 2032 2c0a 2020 2020 2020 2020  ds": 2,.        
-00000430: 226d 6f76 6522 3a20 2d33 2c0a 2020 2020  "move": -3,.    
-00000440: 2020 2020 226e 616d 6522 3a22 e5a4 8de6      "name":"....
-00000450: b4bb e380 81e5 87bb e699 95e4 b894 e590  ................
-00000460: 8ee9 8080 220a 2020 2020 7d2c 0a20 2020  ....".    },.   
-00000470: 207b 0a20 2020 2020 2020 2022 6576 656e   {.        "even
-00000480: 745f 6e61 6d65 223a 2022 e7b4 abe8 89b2  t_name": "......
-00000490: e99a 90e8 8085 5f48 6572 6d69 7420 5075  ......_Hermit Pu
-000004a0: 7270 6c65 222c 0a20 2020 2020 2020 2022  rple",.        "
-000004b0: 6465 7363 7269 6265 223a 2022 3c30 3ee7  describe": "<0>.
-000004c0: b4ab e889 b2e9 9a90 e880 855f 4865 726d  ..........._Herm
-000004d0: 6974 2050 7572 706c 65ef bc88 e5b0 86e8  it Purple.......
-000004e0: 87aa e5b7 b1e5 928c e4bb bbe6 848f e4b8  ................
-000004f0: 80e4 baba e4ba 92e6 8da2 e4bd 8de7 bdae  ................
-00000500: efbc 8922 2c0a 2020 2020 2020 2020 2274  ...",.        "t
-00000510: 6172 6765 7422 3a20 312c 0a20 2020 2020  arget": 1,.     
-00000520: 2020 2022 7472 6163 6b5f 2065 7863 6861     "track_ excha
-00000530: 6e67 655f 206c 6f63 6174 696f 6e22 3a20  nge_ location": 
-00000540: 310a 2020 2020 7d2c 0a20 2020 207b 0a20  1.    },.    {. 
-00000550: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00000560: 6d65 223a 2022 e79f b3e4 b98b e887 aae7  me": "..........
-00000570: 94b1 5f53 746f 6e65 2046 7265 6522 2c0a  .._Stone Free",.
-00000580: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-00000590: 6522 3a20 223c 303e e79f b3e4 b98b e887  e": "<0>........
-000005a0: aae7 94b1 5f53 746f 6e65 2046 7265 6528  ...._Stone Free(
-000005b0: e7ac ace4 b880 e590 8de8 a2ab e994 81e5  ................
-000005c0: ae9a e79a 84e4 baba efbc 8922 2c0a 2020  ...........",.  
-000005d0: 2020 2020 2020 2274 6172 6765 7422 3a20        "target": 
-000005e0: 312c 0a20 2020 2020 2020 2022 6465 6c61  1,.        "dela
-000005f0: 795f 6576 656e 7422 3a5b 332c 7b0a 2020  y_event":[3,{.  
-00000600: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-00000610: 5f6e 616d 6522 3a20 22e7 9fb3 e4b9 8be8  _name": ".......
-00000620: 87aa e794 b15f 5374 6f6e 6520 4672 6565  ....._Stone Free
-00000630: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
-00000640: 6465 7363 7269 6265 223a 2022 e79f b3e4  describe": "....
-00000650: b98b e887 aae7 94b1 5f53 746f 6e65 2046  ........_Stone F
-00000660: 7265 65ef bc88 e5b0 86e6 ada4 e79b aee6  ree.............
-00000670: a087 e59c a8e4 b889 e59b 9ee5 9088 e590  ................
-00000680: 8ee4 b88e e7ac ace4 b880 e590 8de4 ba92  ................
-00000690: e68d a2e4 bd8d e7bd aeef bc89 222c 0a20  ............",. 
-000006a0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-000006b0: 6574 223a 2031 2c0a 2020 2020 2020 2020  et": 1,.        
-000006c0: 2020 2020 2274 7261 636b 5f20 6578 6368      "track_ exch
-000006d0: 616e 6765 5f20 6c6f 6361 7469 6f6e 223a  ange_ location":
-000006e0: 2031 0a20 2020 2020 2020 207d 5d0a 2020   1.        }].  
-000006f0: 2020 7d2c 0a20 2020 207b 0a20 2020 2020    },.    {.     
-00000700: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-00000710: 2022 e796 afe7 8b82 e992 bbe7 9fb3 5f43   "............_C
-00000720: 7261 7a79 2044 6961 6d6f 6e64 222c 0a20  razy Diamond",. 
-00000730: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-00000740: 223a 2022 3c30 3ee7 96af e78b 82e9 92bb  ": "<0>.........
-00000750: e79f b35f 4372 617a 7920 4469 616d 6f6e  ..._Crazy Diamon
-00000760: 64ef bc88 e4b8 8be5 9b9e e590 88e5 a48d  d...............
-00000770: e6b4 bbe5 b9b6 e8a7 a3e9 99a4 e79c a9e6  ................
-00000780: 9995 efbc 8922 2c0a 2020 2020 2020 2020  .....",.        
-00000790: 2274 6172 6765 7422 3a20 342c 0a20 2020  "target": 4,.   
-000007a0: 2020 2020 2022 6465 6c5f 6275 6666 223a       "del_buff":
-000007b0: 2022 7665 7274 6967 6f22 2c0a 2020 2020   "vertigo",.    
-000007c0: 2020 2020 2264 656c 6179 5f65 7665 6e74      "delay_event
-000007d0: 5f73 656c 6622 3a20 5b33 2c20 7b0a 2020  _self": [3, {.  
-000007e0: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-000007f0: 5f6e 616d 6522 3a20 22e7 96af e78b 82e9  _name": ".......
-00000800: 92bb e79f b3e2 809d 5f43 7261 7a79 2044  ........_Crazy D
-00000810: 6961 6d6f 6e64 222c 0a20 2020 2020 2020  iamond",.       
-00000820: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
-00000830: 2022 e796 afe7 8b82 e992 bbe7 9fb3 5f43   "............_C
-00000840: 7261 7a79 2044 6961 6d6f 6e64 efbc 88e4  razy Diamond....
-00000850: b889 e59b 9ee5 9088 e590 8ee4 bdbf e4b8  ................
-00000860: 80e4 b8aa e99a 8fe6 9cba e79b aee6 a087  ................
-00000870: e980 80e5 908e 33e6 ada5 efbc 8922 2c0a  ......3......",.
-00000880: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
-00000890: 6765 7422 3a20 312c 0a20 2020 2020 2020  get": 1,.       
-000008a0: 2020 2020 2022 6d6f 7665 223a 202d 332c       "move": -3,
-000008b0: 0a20 2020 2020 2020 2020 2020 2022 6e61  .            "na
-000008c0: 6d65 223a 22e5 908e e980 8022 0a20 2020  me":"......".   
-000008d0: 2020 2020 207d 5d0a 2020 2020 7d2c 0a20       }].    },. 
-000008e0: 2020 207b 0a20 2020 2020 2020 2022 6576     {.        "ev
-000008f0: 656e 745f 6e61 6d65 223a 2022 e69d 80e6  ent_name": "....
-00000900: 898b e79a 87e5 908e 5f4b 696c 6c65 7220  ........_Killer 
-00000910: 5175 6565 6e5f e7ac ac31 2d33 e788 86e5  Queen_...1-3....
-00000920: bcb9 222c 0a20 2020 2020 2020 2022 7461  ..",.        "ta
-00000930: 7267 6574 223a 2031 2c0a 2020 2020 2020  rget": 1,.      
-00000940: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
-00000950: 3e3a e69d 80e6 898b e79a 87e5 908e 204b  >:............ K
-00000960: 696c 6c65 7220 5175 6565 6eef bc81 e688  iller Queen.....
-00000970: 91e7 9a84 e590 8de5 ad97 e58f ab3c 303e  .............<0>
-00000980: e280 a6e2 80a6 222c 0a20 2020 2020 2020  ......",.       
-00000990: 2022 7261 6e64 6f6d 5f65 7665 6e74 5f6f   "random_event_o
-000009a0: 6e63 6522 3a20 5b0a 2020 2020 2020 2020  nce": [.        
-000009b0: 2020 2020 5b34 302c 207b 0a20 2020 2020      [40, {.     
-000009c0: 2020 2020 2020 2020 2020 2022 6576 656e             "even
-000009d0: 745f 6e61 6d65 223a 2022 e7ac ace4 b880  t_name": "......
-000009e0: e788 86e5 bcb9 222c 0a20 2020 2020 2020  ......",.       
-000009f0: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-00000a00: 6265 223a 2022 e69d 80e6 898b e79a 87e5  be": "..........
-00000a10: 908e 204b 696c 6c65 7220 5175 6565 6ee7  .. Killer Queen.
-00000a20: acac e4b8 80e7 82b8 e5bc b9ef bc81 efbc  ................
-00000a30: 88e4 b880 e4be a7e4 baba e590 8ee9 8080  ................
-00000a40: e4b8 80e6 ada5 efbc 8922 2c0a 2020 2020  .........",.    
-00000a50: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
-00000a60: 6765 7422 3a20 362c 0a20 2020 2020 2020  get": 6,.       
-00000a70: 2020 2020 2020 2020 2022 6d6f 7665 223a           "move":
-00000a80: 202d 312c 0a20 2020 2020 2020 2020 2020   -1,.           
-00000a90: 2020 2020 2022 6e61 6d65 223a 22e5 908e       "name":"...
-00000aa0: e980 8022 0a20 2020 2020 2020 2020 2020  ...".           
-00000ab0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-00000ac0: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
-00000ad0: 2020 5b38 302c 207b 0a20 2020 2020 2020    [80, {.       
-00000ae0: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
-00000af0: 6e61 6d65 223a 2022 e7ac ace4 ba8c e788  name": "........
-00000b00: 86e5 bcb9 222c 0a20 2020 2020 2020 2020  ....",.         
-00000b10: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-00000b20: 223a 2022 e69d 80e6 898b e79a 87e5 908e  ": "............
-00000b30: 204b 696c 6c65 7220 5175 6565 6ee7 acac   Killer Queen...
-00000b40: e4ba 8ce7 82b8 e5bc b9ef bc81 e69e afe8  ................
-00000b50: 908e e7a9 bfe5 bf83 e694 bbe5 87bb efbc  ................
-00000b60: 81ef bc88 e4b8 80e4 b8aa e4ba bae5 908e  ................
-00000b70: e980 8035 e6ad a5ef bc89 222c 0a20 2020  ...5......",.   
-00000b80: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
-00000b90: 7267 6574 223a 2031 2c0a 2020 2020 2020  rget": 1,.      
-00000ba0: 2020 2020 2020 2020 2020 226d 6f76 6522            "move"
-00000bb0: 3a20 2d35 2c0a 2020 2020 2020 2020 2020  : -5,.          
-00000bc0: 2020 2020 2020 226e 616d 6522 3a22 e590        "name":"..
-00000bd0: 8ee9 8080 220a 2020 2020 2020 2020 2020  ....".          
-00000be0: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-00000bf0: 5d2c 0a20 2020 2020 2020 2020 2020 205b  ],.            [
-00000c00: 3132 302c 207b 0a20 2020 2020 2020 2020  120, {.         
-00000c10: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00000c20: 6d65 223a 2022 e7ac ace4 b889 e788 86e5  me": "..........
-00000c30: bcb9 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00000c40: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
-00000c50: 2022 e69d 80e6 898b e79a 87e5 908e 204b   "............ K
-00000c60: 696c 6c65 7220 5175 6565 6ee7 acac e4b8  iller Queen.....
-00000c70: 89e7 82b8 e5bc b9ef bc81 e8b4 a5e8 8085  ................
-00000c80: e9a3 9fe5 b098 efbc 81e5 8f91 e58a a8ef  ................
-00000c90: bc81 28e4 b880 e4ba bae6 adbb e4ba a1ef  ..(.............
-00000ca0: bc89 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00000cb0: 2020 2020 2022 7461 7267 6574 223a 2031       "target": 1
-00000cc0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00000cd0: 2020 2264 6965 223a 2031 2c0a 2020 2020    "die": 1,.    
-00000ce0: 2020 2020 2020 2020 2020 2020 226e 616d              "nam
-00000cf0: 6522 3a22 e6ad bbe4 baa1 220a 2020 2020  e":"......".    
-00000d00: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
-00000d10: 2020 2020 2020 5d0a 2020 2020 2020 2020        ].        
-00000d20: 2020 5d0a 2020 2020 2020 2020 7d2c 0a20    ].        },. 
-00000d30: 2020 2020 2020 207b 0a20 2020 2020 2020         {.       
-00000d40: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00000d50: 223a 2022 e7bb afe7 baa2 e4b9 8be7 8e8b  ": "............
-00000d60: 5f4b 696e 6720 4372 696d 736f 6e22 2c0a  _King Crimson",.
-00000d70: 2020 2020 2020 2020 2020 2020 2264 6573              "des
-00000d80: 6372 6962 6522 3a20 223c 303e 3ae3 8090  cribe": "<0>:...
-00000d90: e7bb afe7 baa2 e4b9 8be7 8e8b 204b 696e  ............ Kin
-00000da0: 6720 4372 696d 736f 6ee3 8091 efbc 81e5  g Crimson.......
-00000db0: b89d e78e 8be6 98af e688 913c 303e e593  ...........<0>..
-00000dc0: 92ef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
-00000dd0: 2020 2022 7461 7267 6574 223a 2031 2c0a     "target": 1,.
-00000de0: 2020 2020 2020 2020 2020 2020 2274 7261              "tra
-00000df0: 636b 5f20 6578 6368 616e 6765 5f20 6c6f  ck_ exchange_ lo
-00000e00: 6361 7469 6f6e 223a 312c 0a20 2020 2020  cation":1,.     
-00000e10: 2020 2020 2020 2022 6469 6522 3a20 312c         "die": 1,
-00000e20: 0a20 2020 2020 2020 2020 2020 2022 6e61  .            "na
-00000e30: 6d65 223a 22e6 adbb e4ba a122 0a20 2020  me":"......".   
-00000e40: 2020 2020 207d 2c0a 2020 2020 2020 2020       },.        
-00000e50: 7b0a 2020 2020 2020 2020 2020 2020 2265  {.            "e
-00000e60: 7665 6e74 5f6e 616d 6522 3a20 22e6 96b0  vent_name": "...
-00000e70: e69c 885f 432d 4d6f 6f6e 222c 0a20 2020  ..._C-Moon",.   
-00000e80: 2020 2020 2020 2020 2022 7461 7267 6574           "target
-00000e90: 223a 2033 2c0a 2020 2020 2020 2020 2020  ": 3,.          
-00000ea0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
-00000eb0: 3e3a e696 b0e6 9c88 5f43 2d4d 6f6f 6eef  >:......_C-Moon.
-00000ec0: bc81 e78e b0e5 9ca8 e4bd a0e4 bbac e5b7  ................
-00000ed0: b2e7 bb8f e69d 80e4 b88d e6ad bbe6 8891  ................
-00000ee0: e4ba 86ef bc81 222c 0a20 2020 2020 2020  ......",.       
-00000ef0: 2020 2020 2022 7261 6e64 6f6d 5f65 7665       "random_eve
-00000f00: 6e74 5f6f 6e63 6522 3a20 5b0a 2020 2020  nt_once": [.    
-00000f10: 2020 2020 2020 2020 2020 2020 5b35 302c              [50,
-00000f20: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-00000f30: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00000f40: 6d65 223a 2022 e6bb 9ae5 898d e99d a2e5  me": "..........
-00000f50: 8ebb efbc 8122 2c0a 2020 2020 2020 2020  .....",.        
-00000f60: 2020 2020 2020 2020 2020 2020 2264 6573              "des
-00000f70: 6372 6962 6522 3a20 22e5 be80 e589 8de6  cribe": ".......
-00000f80: 8ea8 efbc 88e9 99a4 3c30 3ee4 b98b e5a4  ........<0>.....
-00000f90: 96e7 9a84 e689 80e6 9c89 e4ba bae5 898d  ................
-00000fa0: e8bf 9b35 e6ad a5ef bc89 222c 0a20 2020  ...5......",.   
-00000fb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000fc0: 2022 7461 7267 6574 223a 2033 2c0a 2020   "target": 3,.  
+00000010: 2265 7665 6e74 5f6e 616d 6522 3a22 e799  "event_name":"..
+00000020: bde9 8791 e4b9 8be6 989f 5f53 7461 7220  .........._Star 
+00000030: 506c 6174 696e 756d 222c 0a20 2020 2020  Platinum",.     
+00000040: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00000050: 303e e799 bde9 8791 e4b9 8be6 989f 5f53  0>............_S
+00000060: 7461 7220 506c 6174 696e 756d efbc 88e5  tar Platinum....
+00000070: 87bb e699 95e4 b880 e59b 9ee5 9088 e5b9  ................
+00000080: b6e5 908e e980 80e4 b880 e4be a7e7 9a84  ................
+00000090: e9a9 ac31 30e6 ada5 efbc 8922 2c0a 2020  ...10......",.  
+000000a0: 2020 2020 2020 2274 6172 6765 7422 3a36        "target":6
+000000b0: 2c0a 2020 2020 2020 2020 2276 6572 7469  ,.        "verti
+000000c0: 676f 223a 312c 0a20 2020 2020 2020 2022  go":1,.        "
+000000d0: 726f 756e 6473 223a 312c 0a20 2020 2020  rounds":1,.     
+000000e0: 2020 2022 6d6f 7665 223a 2d31 302c 0a20     "move":-10,. 
+000000f0: 2020 2020 2020 2022 6e61 6d65 223a 22e5         "name":".
+00000100: 87bb e699 9522 0a20 2020 207d 2c0a 2020  .....".    },.  
+00000110: 2020 7b0a 2020 2020 2020 2020 2265 7665    {.        "eve
+00000120: 6e74 5f6e 616d 6522 3a22 e4b8 96e7 958c  nt_name":"......
+00000130: 5f54 6865 2057 6f72 6c64 222c 0a20 2020  _The World",.   
+00000140: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00000150: 223c 303e e4b8 96e7 958c 5f54 6865 2057  "<0>......_The W
+00000160: 6f72 6c64 efbc 88e7 9ca9 e699 95e9 99a4  orld............
+00000170: e887 aae5 b7b1 e4bb a5e5 a496 e79a 84e6  ................
+00000180: 8980 e69c 89e4 baba 3130 e4b8 aae5 9b9e  ........10......
+00000190: e590 88ef bc89 222c 0a20 2020 2020 2020  ......",.       
+000001a0: 2022 7461 7267 6574 223a 332c 0a20 2020   "target":3,.   
+000001b0: 2020 2020 2022 7665 7274 6967 6f22 3a31       "vertigo":1
+000001c0: 2c0a 2020 2020 2020 2020 2272 6f75 6e64  ,.        "round
+000001d0: 7322 3a31 302c 0a20 2020 2020 2020 2022  s":10,.        "
+000001e0: 6e61 6d65 223a 22e5 87bb e699 9522 0a20  name":"......". 
+000001f0: 2020 207d 2c0a 2020 2020 7b0a 2020 2020     },.    {.    
+00000200: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+00000210: 3a22 e799 bde9 8791 e4b9 8be6 989f c2b7  :"..............
+00000220: e4b8 96e7 958c 5f53 7461 7220 506c 6174  ......_Star Plat
+00000230: 696e 756d c2b7 5468 6520 576f 726c 6422  inum..The World"
+00000240: 2c0a 2020 2020 2020 2020 2264 6573 6372  ,.        "descr
+00000250: 6962 6522 3a22 3c30 3ee7 99bd e987 91e4  ibe":"<0>.......
+00000260: b98b e698 9fc2 b7e4 b896 e795 8c28 e587  .............(..
+00000270: bbe6 9995 e58d 81e5 9b9e e590 88e5 b9b6  ................
+00000280: e590 8ee9 8080 e4b8 80e4 bea7 e79a 84e9  ................
+00000290: a9ac 3130 e6ad a5ef bc89 222c 0a20 2020  ..10......",.   
+000002a0: 2020 2020 2022 7461 7267 6574 223a 362c       "target":6,
+000002b0: 0a20 2020 2020 2020 2022 7665 7274 6967  .        "vertig
+000002c0: 6f22 3a31 2c0a 2020 2020 2020 2020 2272  o":1,.        "r
+000002d0: 6f75 6e64 7322 3a31 302c 0a20 2020 2020  ounds":10,.     
+000002e0: 2020 2022 6d6f 7665 223a 2d31 302c 200a     "move":-10, .
+000002f0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+00000300: e587 bbe6 9995 e4b8 94e5 908e e980 8022  ..............."
+00000310: 0a20 2020 207d 2c0a 2020 2020 7b0a 2020  .    },.    {.  
+00000320: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
+00000330: 6522 3a22 e9bb 84e9 8791 e4bd 93e9 aa8c  e":"............
+00000340: 5f47 6f6c 6420 4578 7065 7269 656e 6365  _Gold Experience
+00000350: 222c 0a20 2020 2020 2020 2022 6465 7363  ",.        "desc
+00000360: 7269 6265 223a 223c 303e e9bb 84e9 8791  ribe":"<0>......
+00000370: e4bd 93e9 aa8c 5f47 6f6c 6420 4578 7065  ......_Gold Expe
+00000380: 7269 656e 6365 efbc 88e5 a48d e6b4 bbe5  rience..........
+00000390: b9b6 e79c a9e6 9995 e4b8 80e5 908d e4b8  ................
+000003a0: a4e4 b8aa e59b 9ee5 9088 efbc 8ce4 b894  ................
+000003b0: e590 8ee9 8080 e4b8 89e6 ada5 efbc 8922  ..............."
+000003c0: 2c0a 2020 2020 2020 2020 2274 6172 6765  ,.        "targe
+000003d0: 7422 3a31 2c0a 2020 2020 2020 2020 226f  t":1,.        "o
+000003e0: 7468 6572 5f62 7566 6622 3a5b 226c 6976  ther_buff":["liv
+000003f0: 6522 2c22 7665 7274 6967 6f22 5d2c 0a20  e","vertigo"],. 
+00000400: 2020 2020 2020 2022 726f 756e 6473 223a         "rounds":
+00000410: 322c 0a20 2020 2020 2020 2022 6d6f 7665  2,.        "move
+00000420: 223a 2d33 2c0a 2020 2020 2020 2020 226e  ":-3,.        "n
+00000430: 616d 6522 3a22 e5a4 8de6 b4bb e380 81e5  ame":"..........
+00000440: 87bb e699 95e4 b894 e590 8ee9 8080 220a  ..............".
+00000450: 2020 2020 7d2c 0a20 2020 207b 0a20 2020      },.    {.   
+00000460: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00000470: 223a 22e7 b4ab e889 b2e9 9a90 e880 855f  ":"............_
+00000480: 4865 726d 6974 2050 7572 706c 6522 2c0a  Hermit Purple",.
+00000490: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
+000004a0: 6522 3a22 3c30 3ee7 b4ab e889 b2e9 9a90  e":"<0>.........
+000004b0: e880 855f 4865 726d 6974 2050 7572 706c  ..._Hermit Purpl
+000004c0: 65ef bc88 e5b0 86e8 87aa e5b7 b1e5 928c  e...............
+000004d0: e4bb bbe6 848f e4b8 80e4 baba e4ba 92e6  ................
+000004e0: 8da2 e4bd 8de7 bdae efbc 8922 2c0a 2020  ...........",.  
+000004f0: 2020 2020 2020 2274 6172 6765 7422 3a31        "target":1
+00000500: 2c0a 2020 2020 2020 2020 2274 7261 636b  ,.        "track
+00000510: 5f20 6578 6368 616e 6765 5f20 6c6f 6361  _ exchange_ loca
+00000520: 7469 6f6e 223a 310a 2020 2020 7d2c 0a20  tion":1.    },. 
+00000530: 2020 207b 0a20 2020 2020 2020 2022 6576     {.        "ev
+00000540: 656e 745f 6e61 6d65 223a 22e7 9fb3 e4b9  ent_name":".....
+00000550: 8be8 87aa e794 b15f 5374 6f6e 6520 4672  ......._Stone Fr
+00000560: 6565 222c 0a20 2020 2020 2020 2022 6465  ee",.        "de
+00000570: 7363 7269 6265 223a 223c 303e e79f b3e4  scribe":"<0>....
+00000580: b98b e887 aae7 94b1 5f53 746f 6e65 2046  ........_Stone F
+00000590: 7265 6528 e7ac ace4 b880 e590 8de8 a2ab  ree(............
+000005a0: e994 81e5 ae9a e79a 84e4 baba efbc 8922  ..............."
+000005b0: 2c0a 2020 2020 2020 2020 2274 6172 6765  ,.        "targe
+000005c0: 7422 3a31 2c0a 2020 2020 2020 2020 2264  t":1,.        "d
+000005d0: 656c 6179 5f65 7665 6e74 223a 5b33 2c7b  elay_event":[3,{
+000005e0: 0a20 2020 2020 2020 2020 2020 2022 6576  .            "ev
+000005f0: 656e 745f 6e61 6d65 223a 22e7 9fb3 e4b9  ent_name":".....
+00000600: 8be8 87aa e794 b15f 5374 6f6e 6520 4672  ......._Stone Fr
+00000610: 6565 222c 0a20 2020 2020 2020 2020 2020  ee",.           
+00000620: 2022 6465 7363 7269 6265 223a 22e7 9fb3   "describe":"...
+00000630: e4b9 8be8 87aa e794 b15f 5374 6f6e 6520  ........._Stone 
+00000640: 4672 6565 efbc 88e5 b086 e6ad a4e7 9bae  Free............
+00000650: e6a0 87e5 9ca8 e4b8 89e5 9b9e e590 88e5  ................
+00000660: 908e e4b8 8ee7 acac e4b8 80e5 908d e4ba  ................
+00000670: 92e6 8da2 e4bd 8de7 bdae efbc 8922 2c0a  .............",.
+00000680: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
+00000690: 6765 7422 3a31 2c0a 2020 2020 2020 2020  get":1,.        
+000006a0: 2020 2020 2274 7261 636b 5f20 6578 6368      "track_ exch
+000006b0: 616e 6765 5f20 6c6f 6361 7469 6f6e 223a  ange_ location":
+000006c0: 310a 2020 2020 2020 2020 7d5d 0a20 2020  1.        }].   
+000006d0: 207d 2c0a 2020 2020 7b0a 2020 2020 2020   },.    {.      
+000006e0: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+000006f0: e796 afe7 8b82 e992 bbe7 9fb3 5f43 7261  ............_Cra
+00000700: 7a79 2044 6961 6d6f 6e64 222c 0a20 2020  zy Diamond",.   
+00000710: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00000720: 223c 303e e796 afe7 8b82 e992 bbe7 9fb3  "<0>............
+00000730: 5f43 7261 7a79 2044 6961 6d6f 6e64 efbc  _Crazy Diamond..
+00000740: 88e4 b88b e59b 9ee5 9088 e5a4 8de6 b4bb  ................
+00000750: e5b9 b6e8 a7a3 e999 a4e7 9ca9 e699 95ef  ................
+00000760: bc89 222c 0a20 2020 2020 2020 2022 7461  ..",.        "ta
+00000770: 7267 6574 223a 342c 0a20 2020 2020 2020  rget":4,.       
+00000780: 2022 6465 6c5f 6275 6666 223a 2276 6572   "del_buff":"ver
+00000790: 7469 676f 222c 0a20 2020 2020 2020 2022  tigo",.        "
+000007a0: 6465 6c61 795f 6576 656e 745f 7365 6c66  delay_event_self
+000007b0: 223a 5b33 2c20 7b0a 2020 2020 2020 2020  ":[3, {.        
+000007c0: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+000007d0: 3a22 e796 afe7 8b82 e992 bbe7 9fb3 e280  :"..............
+000007e0: 9d5f 4372 617a 7920 4469 616d 6f6e 6422  ._Crazy Diamond"
+000007f0: 2c0a 2020 2020 2020 2020 2020 2020 2264  ,.            "d
+00000800: 6573 6372 6962 6522 3a22 e796 afe7 8b82  escribe":"......
+00000810: e992 bbe7 9fb3 5f43 7261 7a79 2044 6961  ......_Crazy Dia
+00000820: 6d6f 6e64 efbc 88e4 b889 e59b 9ee5 9088  mond............
+00000830: e590 8ee4 bdbf e4b8 80e4 b8aa e99a 8fe6  ................
+00000840: 9cba e79b aee6 a087 e980 80e5 908e 33e6  ..............3.
+00000850: ada5 efbc 8922 2c0a 2020 2020 2020 2020  .....",.        
+00000860: 2020 2020 2274 6172 6765 7422 3a31 2c0a      "target":1,.
+00000870: 2020 2020 2020 2020 2020 2020 226d 6f76              "mov
+00000880: 6522 3a2d 332c 0a20 2020 2020 2020 2020  e":-3,.         
+00000890: 2020 2022 6e61 6d65 223a 22e5 908e e980     "name":".....
+000008a0: 8022 0a20 2020 2020 2020 207d 5d0a 2020  .".        }].  
+000008b0: 2020 7d2c 0a20 2020 207b 0a20 2020 2020    },.    {.     
+000008c0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
+000008d0: 22e6 9d80 e689 8be7 9a87 e590 8e5f 4b69  "............_Ki
+000008e0: 6c6c 6572 2051 7565 656e 5fe7 acac 312d  ller Queen_...1-
+000008f0: 33e7 8886 e5bc b922 2c0a 2020 2020 2020  3......",.      
+00000900: 2020 2274 6172 6765 7422 3a31 2c0a 2020    "target":1,.  
+00000910: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00000920: 3a22 3c30 3e3a e69d 80e6 898b e79a 87e5  :"<0>:..........
+00000930: 908e 204b 696c 6c65 7220 5175 6565 6eef  .. Killer Queen.
+00000940: bc81 e688 91e7 9a84 e590 8de5 ad97 e58f  ................
+00000950: ab3c 303e e280 a6e2 80a6 222c 0a20 2020  .<0>......",.   
+00000960: 2020 2020 2022 7261 6e64 6f6d 5f65 7665       "random_eve
+00000970: 6e74 5f6f 6e63 6522 3a5b 0a20 2020 2020  nt_once":[.     
+00000980: 2020 2020 2020 205b 3430 2c20 7b0a 2020         [40, {.  
+00000990: 2020 2020 2020 2020 2020 2020 2020 2265                "e
+000009a0: 7665 6e74 5f6e 616d 6522 3a22 e7ac ace4  vent_name":"....
+000009b0: b880 e788 86e5 bcb9 222c 0a20 2020 2020  ........",.     
+000009c0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
+000009d0: 7269 6265 223a 22e6 9d80 e689 8be7 9a87  ribe":".........
+000009e0: e590 8e20 4b69 6c6c 6572 2051 7565 656e  ... Killer Queen
+000009f0: e7ac ace4 b880 e782 b8e5 bcb9 efbc 81ef  ................
+00000a00: bc88 e4b8 80e4 bea7 e4ba bae5 908e e980  ................
+00000a10: 80e4 b880 e6ad a5ef bc89 222c 0a20 2020  ..........",.   
+00000a20: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
+00000a30: 7267 6574 223a 362c 0a20 2020 2020 2020  rget":6,.       
+00000a40: 2020 2020 2020 2020 2022 6d6f 7665 223a           "move":
+00000a50: 2d31 2c0a 2020 2020 2020 2020 2020 2020  -1,.            
+00000a60: 2020 2020 226e 616d 6522 3a22 e590 8ee9      "name":"....
+00000a70: 8080 220a 2020 2020 2020 2020 2020 2020  ..".            
+00000a80: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
+00000a90: 2020 5d2c 0a20 2020 2020 2020 2020 2020    ],.           
+00000aa0: 205b 3830 2c20 7b0a 2020 2020 2020 2020   [80, {.        
+00000ab0: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
+00000ac0: 616d 6522 3a22 e7ac ace4 ba8c e788 86e5  ame":"..........
+00000ad0: bcb9 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00000ae0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00000af0: 22e6 9d80 e689 8be7 9a87 e590 8e20 4b69  "............ Ki
+00000b00: 6c6c 6572 2051 7565 656e e7ac ace4 ba8c  ller Queen......
+00000b10: e782 b8e5 bcb9 efbc 81e6 9eaf e890 8ee7  ................
+00000b20: a9bf e5bf 83e6 94bb e587 bbef bc81 efbc  ................
+00000b30: 88e4 b880 e4b8 aae4 baba e590 8ee9 8080  ................
+00000b40: 35e6 ada5 efbc 8922 2c0a 2020 2020 2020  5......",.      
+00000b50: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+00000b60: 7422 3a31 2c0a 2020 2020 2020 2020 2020  t":1,.          
+00000b70: 2020 2020 2020 226d 6f76 6522 3a2d 352c        "move":-5,
+00000b80: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00000b90: 2022 6e61 6d65 223a 22e5 908e e980 8022   "name":"......"
+00000ba0: 0a20 2020 2020 2020 2020 2020 207d 0a20  .            }. 
+00000bb0: 2020 2020 2020 2020 2020 205d 2c0a 2020             ],.  
+00000bc0: 2020 2020 2020 2020 2020 5b31 3230 2c20            [120, 
+00000bd0: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
+00000be0: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00000bf0: e7ac ace4 b889 e788 86e5 bcb9 222c 0a20  ............",. 
+00000c00: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000c10: 6465 7363 7269 6265 223a 22e6 9d80 e689  describe":".....
+00000c20: 8be7 9a87 e590 8e20 4b69 6c6c 6572 2051  ....... Killer Q
+00000c30: 7565 656e e7ac ace4 b889 e782 b8e5 bcb9  ueen............
+00000c40: efbc 81e8 b4a5 e880 85e9 a39f e5b0 98ef  ................
+00000c50: bc81 e58f 91e5 8aa8 efbc 8128 e4b8 80e4  ...........(....
+00000c60: baba e6ad bbe4 baa1 efbc 8922 2c0a 2020  ...........",.  
+00000c70: 2020 2020 2020 2020 2020 2020 2020 2274                "t
+00000c80: 6172 6765 7422 3a31 2c0a 2020 2020 2020  arget":1,.      
+00000c90: 2020 2020 2020 2020 2020 2264 6965 223a            "die":
+00000ca0: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
+00000cb0: 2020 2022 6e61 6d65 223a 22e6 adbb e4ba     "name":".....
+00000cc0: a122 0a20 2020 2020 2020 2020 2020 207d  .".            }
+00000cd0: 0a20 2020 2020 2020 2020 2020 205d 0a20  .            ]. 
+00000ce0: 2020 2020 2020 2020 205d 0a20 2020 2020           ].     
+00000cf0: 2020 207d 2c0a 2020 2020 2020 2020 7b0a     },.        {.
+00000d00: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00000d10: 6e74 5f6e 616d 6522 3a22 e7bb afe7 baa2  nt_name":"......
+00000d20: e4b9 8be7 8e8b 5f4b 696e 6720 4372 696d  ......_King Crim
+00000d30: 736f 6e22 2c0a 2020 2020 2020 2020 2020  son",.          
+00000d40: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+00000d50: 3e3a e380 90e7 bbaf e7ba a2e4 b98b e78e  >:..............
+00000d60: 8b20 4b69 6e67 2043 7269 6d73 6f6e e380  . King Crimson..
+00000d70: 91ef bc81 e5b8 9de7 8e8b e698 afe6 8891  ................
+00000d80: 3c30 3ee5 9392 efbc 8122 2c0a 2020 2020  <0>......",.    
+00000d90: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
+00000da0: 3a31 2c0a 2020 2020 2020 2020 2020 2020  :1,.            
+00000db0: 2274 7261 636b 5f20 6578 6368 616e 6765  "track_ exchange
+00000dc0: 5f20 6c6f 6361 7469 6f6e 223a 312c 0a20  _ location":1,. 
+00000dd0: 2020 2020 2020 2020 2020 2022 6469 6522             "die"
+00000de0: 3a31 2c0a 2020 2020 2020 2020 2020 2020  :1,.            
+00000df0: 226e 616d 6522 3a22 e6ad bbe4 baa1 220a  "name":"......".
+00000e00: 2020 2020 2020 2020 7d2c 0a20 2020 2020          },.     
+00000e10: 2020 207b 0a20 2020 2020 2020 2020 2020     {.           
+00000e20: 2022 6576 656e 745f 6e61 6d65 223a 22e6   "event_name":".
+00000e30: 96b0 e69c 885f 432d 4d6f 6f6e 222c 0a20  ....._C-Moon",. 
+00000e40: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+00000e50: 6574 223a 332c 0a20 2020 2020 2020 2020  et":3,.         
+00000e60: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00000e70: 303e 3ae6 96b0 e69c 885f 432d 4d6f 6f6e  0>:......_C-Moon
+00000e80: efbc 81e7 8eb0 e59c a8e4 bda0 e4bb ace5  ................
+00000e90: b7b2 e7bb 8fe6 9d80 e4b8 8de6 adbb e688  ................
+00000ea0: 91e4 ba86 efbc 8122 2c0a 2020 2020 2020  .......",.      
+00000eb0: 2020 2020 2020 2272 616e 646f 6d5f 6576        "random_ev
+00000ec0: 656e 745f 6f6e 6365 223a 5b0a 2020 2020  ent_once":[.    
+00000ed0: 2020 2020 2020 2020 2020 2020 5b35 302c              [50,
+00000ee0: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
+00000ef0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+00000f00: 6d65 223a 22e6 bb9a e589 8de9 9da2 e58e  me":"...........
+00000f10: bbef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
+00000f20: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
+00000f30: 7269 6265 223a 22e5 be80 e589 8de6 8ea8  ribe":".........
+00000f40: efbc 88e9 99a4 3c30 3ee4 b98b e5a4 96e7  ......<0>.......
+00000f50: 9a84 e689 80e6 9c89 e4ba bae5 898d e8bf  ................
+00000f60: 9b35 e6ad a5ef bc89 222c 0a20 2020 2020  .5......",.     
+00000f70: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000f80: 7461 7267 6574 223a 332c 0a20 2020 2020  target":3,.     
+00000f90: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000fa0: 6d6f 7665 223a 352c 0a20 2020 2020 2020  move":5,.       
+00000fb0: 2020 2020 2020 2020 2020 2020 2022 6e61               "na
+00000fc0: 6d65 223a 22e5 898d e8bf 9b22 0a20 2020  me":"......".   
 00000fd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000fe0: 2020 226d 6f76 6522 3a20 352c 0a20 2020    "move": 5,.   
-00000ff0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001000: 2022 6e61 6d65 223a 22e5 898d e8bf 9b22   "name":"......"
-00001010: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001020: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-00001030: 2020 2020 2020 205d 2c0a 2020 2020 2020         ],.      
-00001040: 2020 2020 2020 2020 2020 5b31 3030 2c20            [100, 
-00001050: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-00001060: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-00001070: 6522 3a20 22e4 b88d e587 86e8 b68a e795  e": "...........
-00001080: 8cef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
-00001090: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-000010a0: 7269 6265 223a 2022 e5be 80e5 908e e980  ribe": "........
-000010b0: 80ef bc88 e999 a43c 303e e4b9 8be5 a496  .......<0>......
-000010c0: e79a 84e6 8980 e69c 89e4 baba e590 8ee9  ................
-000010d0: 8080 35e6 ada5 efbc 8922 2c0a 2020 2020  ..5......",.    
-000010e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000010f0: 2274 6172 6765 7422 3a20 332c 0a20 2020  "target": 3,.   
-00001100: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001110: 2022 6d6f 7665 223a 202d 352c 0a20 2020   "move": -5,.   
-00001120: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001130: 2022 6e61 6d65 223a 22e5 908e e980 8022   "name":"......"
-00001140: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001150: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
-00001160: 2020 205d 0a20 2020 2020 2020 2020 2020     ].           
-00001170: 2020 205d 0a20 2020 2020 2020 2020 2020     ].           
-00001180: 207d 2c0a 2020 2020 2020 2020 2020 2020   },.            
-00001190: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-000011a0: 2020 2265 7665 6e74 5f6e 616d 6522 3a20    "event_name": 
-000011b0: 22e5 a4a9 e5a0 82e5 88b6 e980 a05f 4d61  "............_Ma
-000011c0: 6465 2049 6e20 4865 6176 656e 222c 0a20  de In Heaven",. 
-000011d0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-000011e0: 7461 7267 6574 223a 2033 2c0a 2020 2020  target": 3,.    
-000011f0: 2020 2020 2020 2020 2020 2020 2264 6573              "des
-00001200: 6372 6962 6522 3a22 3c30 3e3a e5a4 a9e5  cribe":"<0>:....
-00001210: a082 e588 b6e9 80a0 5f4d 6164 6520 496e  ........_Made In
-00001220: 2048 6561 7665 6eef bc81 222c 0a20 2020   Heaven...",.   
-00001230: 2020 2020 2020 2020 2020 2020 2022 7261               "ra
-00001240: 6e64 6f6d 5f65 7665 6e74 5f6f 6e63 6522  ndom_event_once"
-00001250: 3a20 5b0a 2020 2020 2020 2020 2020 2020  : [.            
-00001260: 2020 2020 2020 2020 5b35 302c 207b 0a20          [50, {. 
-00001270: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001280: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00001290: 6d65 223a 2022 e8bf 9be5 85a5 e696 b0e5  me": "..........
-000012a0: ae87 e5ae 9922 2c0a 2020 2020 2020 2020  .....",.        
-000012b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012c0: 2264 6573 6372 6962 6522 3a20 22e8 bf9b  "describe": "...
-000012d0: e585 a5e6 96b0 e5ae 87e5 ae99 efbc 88e9  ................
-000012e0: 99a4 3c30 3ee4 b98b e5a4 96e7 9a84 e689  ..<0>...........
-000012f0: 80e6 9c89 e4ba bae5 898d e8bf 9b31 3030  .............100
-00001300: e6ad a5ef bc89 222c 0a20 2020 2020 2020  ......",.       
-00001310: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001320: 2022 7461 7267 6574 223a 2033 2c0a 2020   "target": 3,.  
+00000fe0: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
+00000ff0: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
+00001000: 2020 2020 2020 5b31 3030 2c20 7b0a 2020        [100, {.  
+00001010: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001020: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00001030: e4b8 8de5 8786 e8b6 8ae7 958c efbc 8122  ..............."
+00001040: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00001050: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00001060: 3a22 e5be 80e5 908e e980 80ef bc88 e999  :"..............
+00001070: a43c 303e e4b9 8be5 a496 e79a 84e6 8980  .<0>............
+00001080: e69c 89e4 baba e590 8ee9 8080 35e6 ada5  ............5...
+00001090: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+000010a0: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+000010b0: 7422 3a33 2c0a 2020 2020 2020 2020 2020  t":3,.          
+000010c0: 2020 2020 2020 2020 2020 226d 6f76 6522            "move"
+000010d0: 3a2d 352c 0a20 2020 2020 2020 2020 2020  :-5,.           
+000010e0: 2020 2020 2020 2020 2022 6e61 6d65 223a           "name":
+000010f0: 22e5 908e e980 8022 0a20 2020 2020 2020  "......".       
+00001100: 2020 2020 2020 2020 207d 0a20 2020 2020           }.     
+00001110: 2020 2020 2020 2020 2020 205d 0a20 2020             ].   
+00001120: 2020 2020 2020 2020 2020 205d 0a20 2020             ].   
+00001130: 2020 2020 2020 2020 207d 2c0a 2020 2020           },.    
+00001140: 2020 2020 2020 2020 7b0a 2020 2020 2020          {.      
+00001150: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
+00001160: 5f6e 616d 6522 3a22 e5a4 a9e5 a082 e588  _name":"........
+00001170: b6e9 80a0 5f4d 6164 6520 496e 2048 6561  ...._Made In Hea
+00001180: 7665 6e22 2c0a 2020 2020 2020 2020 2020  ven",.          
+00001190: 2020 2020 2020 2274 6172 6765 7422 3a33        "target":3
+000011a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000011b0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+000011c0: 3e3a e5a4 a9e5 a082 e588 b6e9 80a0 5f4d  >:............_M
+000011d0: 6164 6520 496e 2048 6561 7665 6eef bc81  ade In Heaven...
+000011e0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+000011f0: 2020 2022 7261 6e64 6f6d 5f65 7665 6e74     "random_event
+00001200: 5f6f 6e63 6522 3a5b 0a20 2020 2020 2020  _once":[.       
+00001210: 2020 2020 2020 2020 2020 2020 205b 3530               [50
+00001220: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
+00001230: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00001240: 6e74 5f6e 616d 6522 3a22 e8bf 9be5 85a5  nt_name":"......
+00001250: e696 b0e5 ae87 e5ae 9922 2c0a 2020 2020  .........",.    
+00001260: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001270: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00001280: e8bf 9be5 85a5 e696 b0e5 ae87 e5ae 99ef  ................
+00001290: bc88 e999 a43c 303e e4b9 8be5 a496 e79a  .....<0>........
+000012a0: 84e6 8980 e69c 89e4 baba e589 8de8 bf9b  ................
+000012b0: 3130 30e6 ada5 efbc 8922 2c0a 2020 2020  100......",.    
+000012c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000012d0: 2020 2020 2274 6172 6765 7422 3a33 2c0a      "target":3,.
+000012e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000012f0: 2020 2020 2020 2020 226d 6f76 6522 3a31          "move":1
+00001300: 3030 2c0a 2020 2020 2020 2020 2020 2020  00,.            
+00001310: 2020 2020 2020 2020 2020 2020 226e 616d              "nam
+00001320: 6522 3a22 e589 8de8 bf9b 220a 2020 2020  e":"......".    
 00001330: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001340: 2020 2020 2020 226d 6f76 6522 3a20 3130        "move": 10
-00001350: 302c 0a20 2020 2020 2020 2020 2020 2020  0,.             
-00001360: 2020 2020 2020 2020 2020 2022 6e61 6d65             "name
-00001370: 223a 22e5 898d e8bf 9b22 0a20 2020 2020  ":"......".     
+00001340: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
+00001350: 2020 2020 2020 2020 2020 5d2c 0a20 2020            ],.   
+00001360: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001370: 205b 3130 302c 207b 0a20 2020 2020 2020   [100, {.       
 00001380: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001390: 2020 207d 0a20 2020 2020 2020 2020 2020     }.           
-000013a0: 2020 2020 2020 2020 205d 2c0a 2020 2020           ],.    
-000013b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000013c0: 5b31 3030 2c20 7b0a 2020 2020 2020 2020  [100, {.        
-000013d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000013e0: 2265 7665 6e74 5f6e 616d 6522 3a20 22e5  "event_name": ".
-000013f0: 9b9e e5bd 92e6 9c80 e588 9de7 82b9 222c  ..............",
-00001400: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001410: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-00001420: 6265 223a 2022 e59b 9ee5 bd92 e69c 80e5  be": "..........
-00001430: 889d e782 b9ef bc88 e999 a43c 303e e4b9  ...........<0>..
-00001440: 8be5 a496 e79a 84e6 8980 e69c 89e4 baba  ................
-00001450: e590 8ee9 8080 3130 30e6 ada5 efbc 8922  ......100......"
-00001460: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00001470: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
-00001480: 7422 3a20 332c 0a20 2020 2020 2020 2020  t": 3,.         
-00001490: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-000014a0: 6d6f 7665 223a 202d 3130 302c 0a20 2020  move": -100,.   
+00001390: 2022 6576 656e 745f 6e61 6d65 223a 22e5   "event_name":".
+000013a0: 9b9e e5bd 92e6 9c80 e588 9de7 82b9 222c  ..............",
+000013b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000013c0: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
+000013d0: 6265 223a 22e5 9b9e e5bd 92e6 9c80 e588  be":"...........
+000013e0: 9de7 82b9 efbc 88e9 99a4 3c30 3ee4 b98b  ..........<0>...
+000013f0: e5a4 96e7 9a84 e689 80e6 9c89 e4ba bae5  ................
+00001400: 908e e980 8031 3030 e6ad a5ef bc89 222c  .....100......",
+00001410: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001420: 2020 2020 2020 2020 2022 7461 7267 6574           "target
+00001430: 223a 332c 0a20 2020 2020 2020 2020 2020  ":3,.           
+00001440: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
+00001450: 7665 223a 2d31 3030 2c0a 2020 2020 2020  ve":-100,.      
+00001460: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001470: 2020 226e 616d 6522 3a22 e590 8ee9 8080    "name":"......
+00001480: 220a 2020 2020 2020 2020 2020 2020 2020  ".              
+00001490: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
+000014a0: 2020 2020 2020 2020 2020 2020 5d0a 2020              ].  
 000014b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000014c0: 2020 2020 2022 6e61 6d65 223a 22e5 908e       "name":"...
-000014d0: e980 8022 0a20 2020 2020 2020 2020 2020  ...".           
-000014e0: 2020 2020 2020 2020 207d 0a20 2020 2020           }.     
-000014f0: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
-00001500: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001510: 2020 205d 0a20 2020 2020 2020 2020 2020     ].           
-00001520: 2020 2020 207d 0a0a 5d0a                      }..].
+000014c0: 5d0a 2020 2020 2020 2020 2020 2020 2020  ].              
+000014d0: 2020 7d0a 0a5d 0a                          }..].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/克苏鲁.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/克苏鲁.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 9% similar despite different names*

```diff
@@ -1,107 +1,106 @@
 00000000: 5b0a 7b0a 2022 6576 656e 745f 6e61 6d65  [.{. "event_name
-00000010: 223a 2022 e585 8be8 8b8f e9b2 81e4 ba8b  ": "............
-00000020: e4bb b631 222c 0a20 2264 6573 6372 6962  ...1",. "describ
-00000030: 6522 3a20 223c 303e e7aa 81e7 84b6 e684  e": "<0>........
-00000040: 9fe8 a789 e8a7 82e4 bc97 e5b8 ade4 b8ad  ................
-00000050: e69c 89e4 b880 e58f 8ce7 9cbc e79d 9be5  ................
-00000060: 9ca8 e79b afe7 9d80 e4bb 9622 2c0a 2022  ...........",. "
-00000070: 7461 7267 6574 223a 2030 0a7d 2c0a 7b0a  target": 0.},.{.
-00000080: 2022 6576 656e 745f 6e61 6d65 223a 22e5   "event_name":".
-00000090: 858b e88b 8fe9 b281 e4ba 8be4 bbb6 3222  ..............2"
-000000a0: 2c0a 2022 6465 7363 7269 6265 223a 223c  ,. "describe":"<
-000000b0: 303e e684 9fe8 a789 e8ba abe8 beb9 e8b2  0>..............
-000000c0: 8ce4 bcbc e999 a4e4 ba86 e8b5 9be9 a9ac  ................
-000000d0: e4bb a5e5 a496 e8bf 98e6 9c89 e4b8 80e4  ................
-000000e0: ba9b e585 b6e5 ae83 e4b8 9ce8 a5bf 222c  ..............",
-000000f0: 0a20 2274 6172 6765 7422 3a20 300a 7d2c  . "target": 0.},
-00000100: 0a7b 0a20 2265 7665 6e74 5f6e 616d 6522  .{. "event_name"
-00000110: 3a22 e585 8be8 8b8f e9b2 81e4 ba8b e4bb  :"..............
-00000120: b633 222c 0a20 2264 6573 6372 6962 6522  .3",. "describe"
-00000130: 3a22 3c30 3ee4 b88d e79b b8e4 bfa1 e4b8  :"<0>...........
-00000140: 96e7 958c e4b8 8ae6 9c89 e4bb 80e4 b988  ................
-00000150: e5a5 87e6 80aa e79a 84e4 b89c e8a5 bf22  ..............."
-00000160: 2c0a 2022 7461 7267 6574 223a 300a 7d2c  ,. "target":0.},
-00000170: 0a7b 0a20 2265 7665 6e74 5f6e 616d 6522  .{. "event_name"
-00000180: 3a22 e585 8be8 8b8f e9b2 81e4 ba8b e4bb  :"..............
-00000190: b634 222c 0a20 2264 6573 6372 6962 6522  .4",. "describe"
-000001a0: 3a22 3c30 3ee6 849f e8a7 89e4 bb8a e5a4  :"<0>...........
-000001b0: a9e5 a4aa e998 b3e5 8589 e79a 84e9 a29c  ................
-000001c0: e889 b2e6 9c89 e4ba 9be4 b88d e5af b9ef  ................
-000001d0: bc8c e4bc bce4 b98e e6af 94e5 b9b3 e5b8  ................
-000001e0: b8e6 9a97 e4ba 86e8 aeb8 e5a4 9a22 2c0a  .............",.
-000001f0: 2022 7461 7267 6574 223a 300a 7d2c 0a7b   "target":0.},.{
-00000200: 0a20 2265 7665 6e74 5f6e 616d 6522 3a22  . "event_name":"
-00000210: e585 8be8 8b8f e9b2 81e4 ba8b e4bb b635  ...............5
-00000220: 222c 0a20 2264 6573 6372 6962 6522 3a22  ",. "describe":"
-00000230: 3c30 3ee6 849f e8a7 89e6 9c89 e4bb 80e4  <0>.............
-00000240: b988 e280 9ce4 b89c e8a5 bfe2 809d e59c  ................
-00000250: a8e6 8e90 e79d 80e8 87aa e5b7 b1e7 9a84  ................
-00000260: e596 89e5 9299 222c 0a20 2274 6172 6765  ......",. "targe
-00000270: 7422 3a30 2c0a 2022 726f 756e 6473 223a  t":0,. "rounds":
-00000280: 2031 2c0a 2022 6e61 6d65 223a 2022 e7bc   1,. "name": "..
-00000290: bae6 b0a7 222c 0a20 226c 6f63 6174 655f  ....",. "locate_
-000002a0: 6c6f 636b 223a 2031 0a7d 2c0a 7b0a 2022  lock": 1.},.{. "
-000002b0: 6576 656e 745f 6e61 6d65 223a 22e5 858b  event_name":"...
-000002c0: e88b 8fe9 b281 e4ba 8be4 bbb6 3622 2c0a  ............6",.
-000002d0: 2022 6465 7363 7269 6265 223a 223c 303e   "describe":"<0>
-000002e0: e7aa 81e7 84b6 e684 9fe8 a789 e4b8 80e9  ................
-000002f0: 98b5 e6af 9be9 aaa8 e682 9ae7 84b6 efbc  ................
-00000300: 8ce6 8385 e4b8 8de8 87aa e7a6 81e7 9a84  ................
-00000310: e590 8ee9 8080 e4ba 86e4 b8a4 e6ad a522  ..............."
-00000320: 2c0a 2022 7461 7267 6574 223a 302c 0a20  ,. "target":0,. 
-00000330: 226d 6f76 6522 3a2d 320a 7d2c 0a7b 0a20  "move":-2.},.{. 
-00000340: 2265 7665 6e74 5f6e 616d 6522 3a22 e585  "event_name":"..
-00000350: 8be8 8b8f e9b2 81e4 ba8b e4bb b637 222c  .............7",
-00000360: 0a20 2264 6573 6372 6962 6522 3a22 3c30  . "describe":"<0
-00000370: 3ee5 8f91 e78e b0e7 bb88 e782 b9e5 898d  >...............
-00000380: e5a5 bde5 838f e69c 89e4 b880 e4b8 aae6  ................
-00000390: a8a1 e7b3 8ae7 9a84 e8ba abe5 bdb1 e7ab  ................
-000003a0: 99e5 9ca8 e982 a3ef bc8c e4bd 86e4 bb96  ................
-000003b0: e79c 8be4 b88d e6b8 85e9 82a3 e280 9ce4  ................
-000003c0: b89c e8a5 bfe2 809d e588 b0e5 ba95 e698  ................
-000003d0: afe4 bb80 e4b9 8822 2c0a 2022 7461 7267  .......",. "targ
-000003e0: 6574 223a 300a 7d2c 0a7b 0a20 2265 7665  et":0.},.{. "eve
-000003f0: 6e74 5f6e 616d 6522 3a22 e585 8be8 8b8f  nt_name":"......
-00000400: e9b2 81e4 ba8b e4bb b638 222c 0a20 2264  .........8",. "d
-00000410: 6573 6372 6962 6522 3a22 3c30 3ee6 849f  escribe":"<0>...
-00000420: e8a7 89e8 bf99 e4b8 aae4 b896 e795 8ce4  ................
-00000430: bcbc e4b9 8ee5 8f91 e794 9fe4 ba86 e4bb  ................
-00000440: 80e4 b988 e58f 98e5 8c96 222c 0a20 2274  ..........",. "t
-00000450: 6172 6765 7422 3a30 0a7d 2c0a 7b0a 2265  arget":0.},.{."e
-00000460: 7665 6e74 5f6e 616d 6522 3a22 e585 8be8  vent_name":"....
-00000470: 8b8f e9b2 81e4 ba8b e4bb b639 222c 0a22  ...........9",."
-00000480: 6465 7363 7269 6265 223a 223c 303e e58f  describe":"<0>..
-00000490: 91e7 8eb0 e887 aae5 b7b1 e79a 84e5 afb9  ................
-000004a0: e689 8be5 a5bd e583 8fe5 b9b6 e4b8 8de6  ................
-000004b0: 98af e280 9ce8 b59b e9a9 ace2 809d 222c  ..............",
-000004c0: 0a22 7461 7267 6574 223a 300a 7d2c 0a7b  ."target":0.},.{
-000004d0: 0a20 2265 7665 6e74 5f6e 616d 6522 3a22  . "event_name":"
-000004e0: e585 8be8 8b8f e9b2 81e4 ba8b e4bb b631  ...............1
-000004f0: 3022 2c0a 2022 6465 7363 7269 6265 223a  0",. "describe":
-00000500: 223c 303e e58f 91e7 8eb0 e589 8de6 96b9  "<0>............
-00000510: e7ab 99e7 9d80 e4b8 80e4 b8aa e296 93e2  ................
-00000520: 9693 e296 93e2 9693 e296 93e2 9693 e296  ................
-00000530: 93e2 9693 e296 93e2 9693 e296 93e2 9693  ................
-00000540: e280 a6e2 80a6 262a 252b 2d2a efbc 8ce4  ......&*%+-*....
-00000550: bda0 e8af 95e5 9bbe e980 83e8 b791 efbc  ................
-00000560: 8ce5 8faf e698 afe8 bf98 e698 afe8 a2ab  ................
-00000570: e280 9ce4 bb96 e58f 91e7 8eb0 e4ba 86e2  ................
-00000580: 809d efbc 8ce2 9885 e298 86e2 8691 e297  ................
-00000590: 8ec2 a4e2 9885 e298 86e2 978e e286 91c2  ................
-000005a0: a4e2 9885 e298 86e2 978e c2a4 e297 8ee2  ................
-000005b0: 8691 c2a4 e298 85e2 9886 e286 9122 2c0a  .............",.
-000005c0: 2022 7461 7267 6574 223a 302c 0a20 2261   "target":0,. "a
-000005d0: 7761 7922 3a20 312c 0a20 2261 7761 795f  way": 1,. "away_
-000005e0: 6e61 6d65 223a 2022 3f3f 3f22 0a7d 2c0a  name": "???".},.
-000005f0: 7b0a 2022 6576 656e 745f 6e61 6d65 223a  {. "event_name":
-00000600: 22e5 858b e88b 8fe9 b281 e4ba 8be4 bbb6  "...............
-00000610: 3131 222c 0a20 2264 6573 6372 6962 6522  11",. "describe"
-00000620: 3a20 223c 303e e6b6 88e5 a4b1 e59c a8e4  : "<0>..........
-00000630: ba86 e8b5 9be5 9cba e4b8 8aef bc8c e6b2  ................
-00000640: a1e6 9c89 e4ba bae7 9fa5 e981 93e8 bf99  ................
-00000650: e59c bae6 af94 e8b5 9be4 b8ad e58f 91e7  ................
-00000660: 949f e4ba 86e4 bb80 e4b9 88e3 8082 222c  ..............",
-00000670: 0a20 2274 6172 6765 7422 3a30 2c0a 2022  . "target":0,. "
-00000680: 6469 6522 3a20 312c 0a20 2264 6965 5f6e  die": 1,. "die_n
-00000690: 616d 6522 3a20 22c2 a4e2 9885 e298 86e2  ame": ".........
-000006a0: 8691 220a 7d0a 5d0a                      ..".}.].
+00000010: 223a 22e5 858b e88b 8fe9 b281 e4ba 8be4  ":".............
+00000020: bbb6 3122 2c0a 2022 6465 7363 7269 6265  ..1",. "describe
+00000030: 223a 223c 303e e7aa 81e7 84b6 e684 9fe8  ":"<0>..........
+00000040: a789 e8a7 82e4 bc97 e5b8 ade4 b8ad e69c  ................
+00000050: 89e4 b880 e58f 8ce7 9cbc e79d 9be5 9ca8  ................
+00000060: e79b afe7 9d80 e4bb 9622 2c0a 2022 7461  .........",. "ta
+00000070: 7267 6574 223a 300a 7d2c 0a7b 0a20 2265  rget":0.},.{. "e
+00000080: 7665 6e74 5f6e 616d 6522 3a22 e585 8be8  vent_name":"....
+00000090: 8b8f e9b2 81e4 ba8b e4bb b632 222c 0a20  ...........2",. 
+000000a0: 2264 6573 6372 6962 6522 3a22 3c30 3ee6  "describe":"<0>.
+000000b0: 849f e8a7 89e8 baab e8be b9e8 b28c e4bc  ................
+000000c0: bce9 99a4 e4ba 86e8 b59b e9a9 ace4 bba5  ................
+000000d0: e5a4 96e8 bf98 e69c 89e4 b880 e4ba 9be5  ................
+000000e0: 85b6 e5ae 83e4 b89c e8a5 bf22 2c0a 2022  ...........",. "
+000000f0: 7461 7267 6574 223a 300a 7d2c 0a7b 0a20  target":0.},.{. 
+00000100: 2265 7665 6e74 5f6e 616d 6522 3a22 e585  "event_name":"..
+00000110: 8be8 8b8f e9b2 81e4 ba8b e4bb b633 222c  .............3",
+00000120: 0a20 2264 6573 6372 6962 6522 3a22 3c30  . "describe":"<0
+00000130: 3ee4 b88d e79b b8e4 bfa1 e4b8 96e7 958c  >...............
+00000140: e4b8 8ae6 9c89 e4bb 80e4 b988 e5a5 87e6  ................
+00000150: 80aa e79a 84e4 b89c e8a5 bf22 2c0a 2022  ...........",. "
+00000160: 7461 7267 6574 223a 300a 7d2c 0a7b 0a20  target":0.},.{. 
+00000170: 2265 7665 6e74 5f6e 616d 6522 3a22 e585  "event_name":"..
+00000180: 8be8 8b8f e9b2 81e4 ba8b e4bb b634 222c  .............4",
+00000190: 0a20 2264 6573 6372 6962 6522 3a22 3c30  . "describe":"<0
+000001a0: 3ee6 849f e8a7 89e4 bb8a e5a4 a9e5 a4aa  >...............
+000001b0: e998 b3e5 8589 e79a 84e9 a29c e889 b2e6  ................
+000001c0: 9c89 e4ba 9be4 b88d e5af b9ef bc8c e4bc  ................
+000001d0: bce4 b98e e6af 94e5 b9b3 e5b8 b8e6 9a97  ................
+000001e0: e4ba 86e8 aeb8 e5a4 9a22 2c0a 2022 7461  .........",. "ta
+000001f0: 7267 6574 223a 300a 7d2c 0a7b 0a20 2265  rget":0.},.{. "e
+00000200: 7665 6e74 5f6e 616d 6522 3a22 e585 8be8  vent_name":"....
+00000210: 8b8f e9b2 81e4 ba8b e4bb b635 222c 0a20  ...........5",. 
+00000220: 2264 6573 6372 6962 6522 3a22 3c30 3ee6  "describe":"<0>.
+00000230: 849f e8a7 89e6 9c89 e4bb 80e4 b988 e280  ................
+00000240: 9ce4 b89c e8a5 bfe2 809d e59c a8e6 8e90  ................
+00000250: e79d 80e8 87aa e5b7 b1e7 9a84 e596 89e5  ................
+00000260: 9299 222c 0a20 2274 6172 6765 7422 3a30  ..",. "target":0
+00000270: 2c0a 2022 726f 756e 6473 223a 312c 0a20  ,. "rounds":1,. 
+00000280: 226e 616d 6522 3a22 e7bc bae6 b0a7 222c  "name":"......",
+00000290: 0a20 226c 6f63 6174 655f 6c6f 636b 223a  . "locate_lock":
+000002a0: 310a 7d2c 0a7b 0a20 2265 7665 6e74 5f6e  1.},.{. "event_n
+000002b0: 616d 6522 3a22 e585 8be8 8b8f e9b2 81e4  ame":"..........
+000002c0: ba8b e4bb b636 222c 0a20 2264 6573 6372  .....6",. "descr
+000002d0: 6962 6522 3a22 3c30 3ee7 aa81 e784 b6e6  ibe":"<0>.......
+000002e0: 849f e8a7 89e4 b880 e998 b5e6 af9b e9aa  ................
+000002f0: a8e6 829a e784 b6ef bc8c e683 85e4 b88d  ................
+00000300: e887 aae7 a681 e79a 84e5 908e e980 80e4  ................
+00000310: ba86 e4b8 a4e6 ada5 222c 0a20 2274 6172  ........",. "tar
+00000320: 6765 7422 3a30 2c0a 2022 6d6f 7665 223a  get":0,. "move":
+00000330: 2d32 0a7d 2c0a 7b0a 2022 6576 656e 745f  -2.},.{. "event_
+00000340: 6e61 6d65 223a 22e5 858b e88b 8fe9 b281  name":".........
+00000350: e4ba 8be4 bbb6 3722 2c0a 2022 6465 7363  ......7",. "desc
+00000360: 7269 6265 223a 223c 303e e58f 91e7 8eb0  ribe":"<0>......
+00000370: e7bb 88e7 82b9 e589 8de5 a5bd e583 8fe6  ................
+00000380: 9c89 e4b8 80e4 b8aa e6a8 a1e7 b38a e79a  ................
+00000390: 84e8 baab e5bd b1e7 ab99 e59c a8e9 82a3  ................
+000003a0: efbc 8ce4 bd86 e4bb 96e7 9c8b e4b8 8de6  ................
+000003b0: b885 e982 a3e2 809c e4b8 9ce8 a5bf e280  ................
+000003c0: 9de5 88b0 e5ba 95e6 98af e4bb 80e4 b988  ................
+000003d0: 222c 0a20 2274 6172 6765 7422 3a30 0a7d  ",. "target":0.}
+000003e0: 2c0a 7b0a 2022 6576 656e 745f 6e61 6d65  ,.{. "event_name
+000003f0: 223a 22e5 858b e88b 8fe9 b281 e4ba 8be4  ":".............
+00000400: bbb6 3822 2c0a 2022 6465 7363 7269 6265  ..8",. "describe
+00000410: 223a 223c 303e e684 9fe8 a789 e8bf 99e4  ":"<0>..........
+00000420: b8aa e4b8 96e7 958c e4bc bce4 b98e e58f  ................
+00000430: 91e7 949f e4ba 86e4 bb80 e4b9 88e5 8f98  ................
+00000440: e58c 9622 2c0a 2022 7461 7267 6574 223a  ...",. "target":
+00000450: 300a 7d2c 0a7b 0a22 6576 656e 745f 6e61  0.},.{."event_na
+00000460: 6d65 223a 22e5 858b e88b 8fe9 b281 e4ba  me":"...........
+00000470: 8be4 bbb6 3922 2c0a 2264 6573 6372 6962  ....9",."describ
+00000480: 6522 3a22 3c30 3ee5 8f91 e78e b0e8 87aa  e":"<0>.........
+00000490: e5b7 b1e7 9a84 e5af b9e6 898b e5a5 bde5  ................
+000004a0: 838f e5b9 b6e4 b88d e698 afe2 809c e8b5  ................
+000004b0: 9be9 a9ac e280 9d22 2c0a 2274 6172 6765  .......",."targe
+000004c0: 7422 3a30 0a7d 2c0a 7b0a 2022 6576 656e  t":0.},.{. "even
+000004d0: 745f 6e61 6d65 223a 22e5 858b e88b 8fe9  t_name":".......
+000004e0: b281 e4ba 8be4 bbb6 3130 222c 0a20 2264  ........10",. "d
+000004f0: 6573 6372 6962 6522 3a22 3c30 3ee5 8f91  escribe":"<0>...
+00000500: e78e b0e5 898d e696 b9e7 ab99 e79d 80e4  ................
+00000510: b880 e4b8 aae2 9693 e296 93e2 9693 e296  ................
+00000520: 93e2 9693 e296 93e2 9693 e296 93e2 9693  ................
+00000530: e296 93e2 9693 e296 93e2 80a6 e280 a626  ...............&
+00000540: 2a25 2b2d 2aef bc8c e4bd a0e8 af95 e59b  *%+-*...........
+00000550: bee9 8083 e8b7 91ef bc8c e58f afe6 98af  ................
+00000560: e8bf 98e6 98af e8a2 abe2 809c e4bb 96e5  ................
+00000570: 8f91 e78e b0e4 ba86 e280 9def bc8c e298  ................
+00000580: 85e2 9886 e286 91e2 978e c2a4 e298 85e2  ................
+00000590: 9886 e297 8ee2 8691 c2a4 e298 85e2 9886  ................
+000005a0: e297 8ec2 a4e2 978e e286 91c2 a4e2 9885  ................
+000005b0: e298 86e2 8691 222c 0a20 2274 6172 6765  ......",. "targe
+000005c0: 7422 3a30 2c0a 2022 6177 6179 223a 312c  t":0,. "away":1,
+000005d0: 0a20 2261 7761 795f 6e61 6d65 223a 223f  . "away_name":"?
+000005e0: 3f3f 220a 7d2c 0a7b 0a20 2265 7665 6e74  ??".},.{. "event
+000005f0: 5f6e 616d 6522 3a22 e585 8be8 8b8f e9b2  _name":"........
+00000600: 81e4 ba8b e4bb b631 3122 2c0a 2022 6465  .......11",. "de
+00000610: 7363 7269 6265 223a 223c 303e e6b6 88e5  scribe":"<0>....
+00000620: a4b1 e59c a8e4 ba86 e8b5 9be5 9cba e4b8  ................
+00000630: 8aef bc8c e6b2 a1e6 9c89 e4ba bae7 9fa5  ................
+00000640: e981 93e8 bf99 e59c bae6 af94 e8b5 9be4  ................
+00000650: b8ad e58f 91e7 949f e4ba 86e4 bb80 e4b9  ................
+00000660: 88e3 8082 222c 0a20 2274 6172 6765 7422  ....",. "target"
+00000670: 3a30 2c0a 2022 6469 6522 3a31 2c0a 2022  :0,. "die":1,. "
+00000680: 6469 655f 6e61 6d65 223a 22c2 a4e2 9885  die_name":".....
+00000690: e298 86e2 8691 220a 7d0a 5d0a            ......".}.].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/基础事件.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/基础事件.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 26% similar despite different names*

```diff
@@ -1,56 +1,54 @@
-00000000: 5b0a 7b0a 2264 6573 6372 6962 6522 3a20  [.{."describe": 
-00000010: 223c 303e e7ad 96e9 a9ac e5a5 94e8 85be  "<0>............
-00000020: efbc 8ce4 b88b e59b 9ee5 9088 e7a7 bbe5  ................
-00000030: 8aa8 e8b7 9de7 a6bb 2b33 222c 0a22 7461  ........+3",."ta
-00000040: 7267 6574 223a 2030 2c0a 2272 6f75 6e64  rget": 0,."round
-00000050: 7322 3a20 312c 0a22 6e61 6d65 223a 2022  s": 1,."name": "
-00000060: e5b4 a9e8 85be 222c 0a22 6d6f 7665 5f6d  ......",."move_m
-00000070: 6178 223a 2033 2c0a 226d 6f76 655f 6d69  ax": 3,."move_mi
-00000080: 6e22 3a20 330a 7d2c 0a7b 0a22 6465 7363  n": 3.},.{."desc
-00000090: 7269 6265 223a 2022 3c30 3ee8 b8a9 e588  ribe": "<0>.....
-000000a0: b0e4 ba86 e59d 91e9 878c efbc 8ce6 97a0  ................
-000000b0: e6b3 95e7 a7bb e58a a8e4 b8a4 e59b 9ee5  ................
-000000c0: 9088 222c 0a22 7461 7267 6574 223a 2030  ..",."target": 0
-000000d0: 2c0a 2272 6f75 6e64 7322 3a20 322c 0a22  ,."rounds": 2,."
-000000e0: 6e61 6d65 223a 2022 e999 b7e9 98b1 222c  name": "......",
-000000f0: 0a22 6c6f 6361 7465 5f6c 6f63 6b22 3a20  ."locate_lock": 
-00000100: 310a 7d2c 0a7b 0a22 6465 7363 7269 6265  1.},.{."describe
-00000110: 223a 2022 3c30 3ee8 8eb7 e5be 97e4 ba86  ": "<0>.........
-00000120: e694 bee6 b5aa e7a5 9ee7 9a84 e7a5 9de7  ................
-00000130: a68f efbc 8ce9 9a8f e69c bae8 8eb7 e5be  ................
-00000140: 9732 e59b 9ee5 9088 e79a 8430 7e2b 32e7  .2.........0~+2.
-00000150: 9a84 e4bd 8de7 a7bb e58a a0e6 8890 222c  ..............",
-00000160: 0a22 7461 7267 6574 223a 2030 2c0a 2272  ."target": 0,."r
-00000170: 6f75 6e64 7322 3a20 322c 0a22 6e61 6d65  ounds": 2,."name
-00000180: 223a 2022 e694 bee6 b5aa e7a5 9e22 2c0a  ": ".........",.
-00000190: 226d 6f76 655f 6d61 7822 3a20 320a 7d2c  "move_max": 2.},
-000001a0: 0a7b 0a22 6465 7363 7269 6265 223a 2022  .{."describe": "
-000001b0: 3c30 3ee6 8993 e5bc 80e4 ba86 e4b8 80e4  <0>.............
-000001c0: bbbd e58d a1e5 8c85 efbc 8ce6 98af e5b7  ................
-000001d0: a8e5 a4a7 e596 b7e6 b581 efbc 8c3c 313e  .............<1>
-000001e0: e59b 9be5 8886 e4ba 94e8 a382 e4ba 8622  ..............."
-000001f0: 2c0a 2269 6e76 696e 6369 626c 655f 6163  ,."invincible_ac
-00000200: 7469 7665 223a 2031 2c0a 2264 6573 6372  tive": 1,."descr
-00000210: 6962 655f 696e 7669 6e63 6962 6c65 223a  ibe_invincible":
-00000220: 2022 3c30 3ee6 8993 e5bc 80e4 ba86 e4b8   "<0>...........
-00000230: 80e4 bbbd e58d a1e5 8c85 efbc 8ce6 98af  ................
-00000240: e5b7 a8e5 a4a7 e596 b7e6 b581 efbc 8c3c  ...............<
-00000250: 313e e58f 97e5 88b0 e4ba 86e6 94bb e587  1>..............
-00000260: bbef bc8c e4bd 86e6 97a0 e4ba 8be5 8f91  ................
-00000270: e794 9f22 2c0a 2274 6172 6765 7422 3a20  ...",."target": 
-00000280: 312c 0a22 6e61 6d65 223a 2022 e8a3 82e5  1,."name": "....
-00000290: bc80 222c 0a22 6469 6522 3a20 310a 7d2c  ..",."die": 1.},
-000002a0: 0a7b 0a22 6465 7363 7269 6265 223a 2022  .{."describe": "
-000002b0: 3c30 3ee4 bdbf e794 a8e4 ba86 e8b5 a4e5  <0>.............
-000002c0: a4a9 e5bc 80e9 97a8 222c 0a22 7461 7267  ........",."targ
-000002d0: 6574 223a 2032 2c0a 226c 6976 6522 3a20  et": 2,."live": 
-000002e0: 310a 7d2c 0a7b 0a22 6465 7363 7269 6265  1.},.{."describe
-000002f0: 223a 2022 3c30 3ee9 99b7 e585 a5e4 ba86  ": "<0>.........
-00000300: e8bf b7e8 8cab efbc 8ce8 8eb7 e5be 9732  ...............2
-00000310: e59b 9ee5 9088 e79a 842d 32e7 9a84 e4bd  .........-2.....
-00000320: 8de7 a7bb e58a a0e6 8890 222c 0a22 7461  ..........",."ta
-00000330: 7267 6574 223a 2030 2c0a 2272 6f75 6e64  rget": 0,."round
-00000340: 7322 3a20 322c 0a22 6e61 6d65 223a 2022  s": 2,."name": "
-00000350: e8bf b7e8 8cab 222c 0a22 6d6f 7665 5f6d  ......",."move_m
-00000360: 6178 223a 202d 322c 0a22 6d6f 7665 5f6d  ax": -2,."move_m
-00000370: 696e 223a 202d 320a 7d0a 5d0a            in": -2.}.].
+00000000: 5b0a 7b0a 2264 6573 6372 6962 6522 3a22  [.{."describe":"
+00000010: 3c30 3ee7 ad96 e9a9 ace5 a594 e885 beef  <0>.............
+00000020: bc8c e4b8 8be5 9b9e e590 88e7 a7bb e58a  ................
+00000030: a8e8 b79d e7a6 bb2b 3322 2c0a 2274 6172  .......+3",."tar
+00000040: 6765 7422 3a30 2c0a 2272 6f75 6e64 7322  get":0,."rounds"
+00000050: 3a31 2c0a 226e 616d 6522 3a22 e5b4 a9e8  :1,."name":"....
+00000060: 85be 222c 0a22 6d6f 7665 5f6d 6178 223a  ..",."move_max":
+00000070: 332c 0a22 6d6f 7665 5f6d 696e 223a 330a  3,."move_min":3.
+00000080: 7d2c 0a7b 0a22 6465 7363 7269 6265 223a  },.{."describe":
+00000090: 223c 303e e8b8 a9e5 88b0 e4ba 86e5 9d91  "<0>............
+000000a0: e987 8cef bc8c e697 a0e6 b395 e7a7 bbe5  ................
+000000b0: 8aa8 e4b8 a4e5 9b9e e590 8822 2c0a 2274  ...........",."t
+000000c0: 6172 6765 7422 3a30 2c0a 2272 6f75 6e64  arget":0,."round
+000000d0: 7322 3a32 2c0a 226e 616d 6522 3a22 e999  s":2,."name":"..
+000000e0: b7e9 98b1 222c 0a22 6c6f 6361 7465 5f6c  ....",."locate_l
+000000f0: 6f63 6b22 3a31 0a7d 2c0a 7b0a 2264 6573  ock":1.},.{."des
+00000100: 6372 6962 6522 3a22 3c30 3ee8 8eb7 e5be  cribe":"<0>.....
+00000110: 97e4 ba86 e694 bee6 b5aa e7a5 9ee7 9a84  ................
+00000120: e7a5 9de7 a68f efbc 8ce9 9a8f e69c bae8  ................
+00000130: 8eb7 e5be 9732 e59b 9ee5 9088 e79a 8430  .....2.........0
+00000140: 7e2b 32e7 9a84 e4bd 8de7 a7bb e58a a0e6  ~+2.............
+00000150: 8890 222c 0a22 7461 7267 6574 223a 302c  ..",."target":0,
+00000160: 0a22 726f 756e 6473 223a 322c 0a22 6e61  ."rounds":2,."na
+00000170: 6d65 223a 22e6 94be e6b5 aae7 a59e 222c  me":".........",
+00000180: 0a22 6d6f 7665 5f6d 6178 223a 320a 7d2c  ."move_max":2.},
+00000190: 0a7b 0a22 6465 7363 7269 6265 223a 223c  .{."describe":"<
+000001a0: 303e e689 93e5 bc80 e4ba 86e4 b880 e4bb  0>..............
+000001b0: bde5 8da1 e58c 85ef bc8c e698 afe5 b7a8  ................
+000001c0: e5a4 a7e5 96b7 e6b5 81ef bc8c 3c31 3ee5  ............<1>.
+000001d0: 9b9b e588 86e4 ba94 e8a3 82e4 ba86 222c  ..............",
+000001e0: 0a22 696e 7669 6e63 6962 6c65 5f61 6374  ."invincible_act
+000001f0: 6976 6522 3a31 2c0a 2264 6573 6372 6962  ive":1,."describ
+00000200: 655f 696e 7669 6e63 6962 6c65 223a 223c  e_invincible":"<
+00000210: 303e e689 93e5 bc80 e4ba 86e4 b880 e4bb  0>..............
+00000220: bde5 8da1 e58c 85ef bc8c e698 afe5 b7a8  ................
+00000230: e5a4 a7e5 96b7 e6b5 81ef bc8c 3c31 3ee5  ............<1>.
+00000240: 8f97 e588 b0e4 ba86 e694 bbe5 87bb efbc  ................
+00000250: 8ce4 bd86 e697 a0e4 ba8b e58f 91e7 949f  ................
+00000260: 222c 0a22 7461 7267 6574 223a 312c 0a22  ",."target":1,."
+00000270: 6e61 6d65 223a 22e8 a382 e5bc 8022 2c0a  name":"......",.
+00000280: 2264 6965 223a 310a 7d2c 0a7b 0a22 6465  "die":1.},.{."de
+00000290: 7363 7269 6265 223a 223c 303e e4bd bfe7  scribe":"<0>....
+000002a0: 94a8 e4ba 86e8 b5a4 e5a4 a9e5 bc80 e997  ................
+000002b0: a822 2c0a 2274 6172 6765 7422 3a32 2c0a  .",."target":2,.
+000002c0: 226c 6976 6522 3a31 0a7d 2c0a 7b0a 2264  "live":1.},.{."d
+000002d0: 6573 6372 6962 6522 3a22 3c30 3ee9 99b7  escribe":"<0>...
+000002e0: e585 a5e4 ba86 e8bf b7e8 8cab efbc 8ce8  ................
+000002f0: 8eb7 e5be 9732 e59b 9ee5 9088 e79a 842d  .....2.........-
+00000300: 32e7 9a84 e4bd 8de7 a7bb e58a a0e6 8890  2...............
+00000310: 222c 0a22 7461 7267 6574 223a 302c 0a22  ",."target":0,."
+00000320: 726f 756e 6473 223a 322c 0a22 6e61 6d65  rounds":2,."name
+00000330: 223a 22e8 bfb7 e88c ab22 2c0a 226d 6f76  ":"......",."mov
+00000340: 655f 6d61 7822 3a2d 322c 0a22 6d6f 7665  e_max":-2,."move
+00000350: 5f6d 696e 223a 2d32 0a7d 0a5d 0a         _min":-2.}.].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/复刻经典事件集合v1.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/复刻经典事件集合v1.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 9% similar despite different names*

```diff
@@ -1,167 +1,164 @@
 00000000: 5b0a 2020 2020 7b0a 2020 2020 2265 7665  [.    {.    "eve
-00000010: 6e74 5f6e 616d 6522 3a20 22e7 a9ba e997  nt_name": ".....
-00000020: b4e8 b7b3 e8b7 835f e589 8de8 bf9b 3322  ......._......3"
-00000030: 2c0a 2020 2020 2274 6172 6765 7422 3a20  ,.    "target": 
-00000040: 302c 0a20 2020 2022 6465 7363 7269 6265  0,.    "describe
-00000050: 223a 223c 303e e88e b7e5 be97 e4ba 86e7  ":"<0>..........
-00000060: 99bd e4ba 95e9 bb91 e5ad 90e7 9a84 e58a  ................
-00000070: 9be9 878f efbc 8ce5 be80 e589 8de7 a9ba  ................
-00000080: e997 b4e8 b7b3 e8b7 83e4 ba86 33e6 a0bc  ............3...
-00000090: 2122 2c0a 2020 2020 226d 6f76 6522 3a20  !",.    "move": 
-000000a0: 330a 2020 2020 7d2c 0a20 2020 207b 0a20  3.    },.    {. 
-000000b0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-000000c0: 2022 e69b b2e7 8e87 e58a a0e9 809f 5fe5   "............_.
-000000d0: 898d e8bf 9b33 222c 0a20 2020 2022 7461  .....3",.    "ta
-000000e0: 7267 6574 223a 2030 2c0a 2020 2020 2264  rget": 0,.    "d
-000000f0: 6573 6372 6962 6522 3a22 3c30 3ee6 89be  escribe":"<0>...
-00000100: e588 b0e4 ba86 e4b8 80e4 b8aa e69b b2e7  ................
-00000110: 8e87 e58a a0e9 809f e599 a8ef bc8c e58a  ................
-00000120: a0e9 809f e589 8de8 bf9b e4ba 8633 e6a0  .............3..
-00000130: bc21 222c 0a20 2020 2022 6d6f 7665 223a  .!",.    "move":
-00000140: 2033 0a20 2020 207d 2c0a 2020 2020 7b0a   3.    },.    {.
-00000150: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-00000160: 3a20 22e7 81ab e7ae ade6 8ea8 e8bf 9be5  : ".............
-00000170: 99a8 5fe5 898d e8bf 9b33 222c 0a20 2020  .._......3",.   
-00000180: 2022 7461 7267 6574 223a 2030 2c0a 2020   "target": 0,.  
-00000190: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
-000001a0: 3ee6 89be e588 b0e4 ba86 e4b8 80e4 b8aa  >...............
-000001b0: e781 abe7 aead e68e a8e8 bf9b e599 a8ef  ................
-000001c0: bc8c e58a a0e9 809f e589 8de8 bf9b e4ba  ................
-000001d0: 8633 e6a0 bc22 2c0a 2020 2020 226d 6f76  .3...",.    "mov
-000001e0: 6522 3a20 330a 2020 2020 7d2c 0a20 2020  e": 3.    },.   
-000001f0: 207b 0a20 2020 2022 6576 656e 745f 6e61   {.    "event_na
-00000200: 6d65 223a 2022 e6b2 89e8 bfb7 5048 7562  me": "......PHub
-00000210: 5fe5 908e e980 8032 222c 0a20 2020 2022  _......2",.    "
-00000220: 7461 7267 6574 223a 2030 2c0a 2020 2020  target": 0,.    
-00000230: 2264 6573 6372 6962 6522 3a22 3c30 3ee6  "describe":"<0>.
-00000240: b289 e8bf b750 4875 62ef bc8c e590 8ee9  .....PHub.......
-00000250: 8080 e4ba 8632 e6a0 bc22 2c0a 2020 2020  .....2...",.    
-00000260: 226d 6f76 6522 3a20 2d32 0a20 2020 207d  "move": -2.    }
-00000270: 2c0a 2020 2020 7b0a 2020 2020 2265 7665  ,.    {.    "eve
-00000280: 6e74 5f6e 616d 6522 3a20 22e8 849a e889  nt_name": ".....
-00000290: bae9 a9ac 222c 0a20 2020 2022 7461 7267  ....",.    "targ
-000002a0: 6574 223a 2030 2c0a 2020 2020 2264 6573  et": 0,.    "des
-000002b0: 6372 6962 6522 3a22 3c30 3ee6 8890 e4b8  cribe":"<0>.....
-000002c0: bae4 ba86 e884 9ae8 89ba e9a9 acef bc8c  ................
-000002d0: e9a2 9de5 a496 e589 8de8 bf9b e4ba 8632  ...............2
-000002e0: e6a0 bc22 2c0a 2020 2020 226d 6f76 6522  ...",.    "move"
-000002f0: 3a20 320a 2020 2020 7d2c 0a20 2020 207b  : 2.    },.    {
-00000300: 0a20 2020 2022 6576 656e 745f 6e61 6d65  .    "event_name
-00000310: 223a 2022 e68e 89e5 85a5 e4ba 8ce6 aca1  ": "............
-00000320: e585 835f e590 8ee9 8080 3222 2c0a 2020  ..._......2",.  
-00000330: 2020 2274 6172 6765 7422 3a20 302c 0a20    "target": 0,. 
-00000340: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
-00000350: 303e e68e 89e5 85a5 e4ba 86e4 ba8c e6ac  0>..............
-00000360: a1e5 8583 efbc 8ce6 b289 e8bf b7e5 85b6  ................
-00000370: e4b8 adef bc8c e697 a0e6 b395 e887 aae6  ................
-00000380: 8b94 efbc 8ce5 908e e980 80e4 ba86 32e6  ..............2.
-00000390: a0bc 222c 0a20 2020 2022 6d6f 7665 223a  ..",.    "move":
-000003a0: 202d 320a 2020 2020 7d2c 0a20 2020 207b   -2.    },.    {
-000003b0: 0a20 2020 2022 6576 656e 745f 6e61 6d65  .    "event_name
-000003c0: 223a 2022 e9a3 9ee6 9cba e587 bbe4 b8ad  ": "............
-000003d0: 222c 0a20 2020 2022 7461 7267 6574 223a  ",.    "target":
-000003e0: 2030 2c0a 2020 2020 2264 6573 6372 6962   0,.    "describ
-000003f0: 6522 3a22 3c30 3ee8 a2ab e5a4 a9e4 b88a  e":"<0>.........
-00000400: e79a 84e9 a39e e69c bae5 87bb e4b8 ade4  ................
-00000410: ba86 efbc 8c22 2c0a 2020 2020 2272 616e  .....",.    "ran
-00000420: 646f 6d5f 6576 656e 745f 6f6e 6365 223a  dom_event_once":
-00000430: 205b 5b32 352c 207b 0a20 2020 2020 2020   [[25, {.       
-00000440: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00000450: 223a 2022 e9a3 9ee6 9cba e587 bbe4 b8ad  ": "............
-00000460: 2de5 87bb e4b8 ad22 2c0a 2020 2020 2020  -......",.      
-00000470: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-00000480: 3a20 22e4 b88d e5b9 b8e7 a6bb e5bc 80e4  : ".............
-00000490: ba86 e688 98e5 9cba 222c 0a20 2020 2020  ........",.     
-000004a0: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-000004b0: 2030 2c0a 2020 2020 2020 2020 2020 2020   0,.            
-000004c0: 2264 6965 223a 2031 0a20 2020 2020 2020  "die": 1.       
-000004d0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-000004e0: 205d 2c0a 2020 2020 2020 2020 2020 5b31   ],.          [1
-000004f0: 3030 2c20 7b0a 2020 2020 2020 2020 2020  00, {.          
-00000500: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-00000510: 3a20 22e9 a39e e69c bae5 87bb e4b8 ad2d  : "............-
-00000520: e697 a0e4 ba8b e58f 91e7 949f 222c 0a20  ............",. 
-00000530: 2020 2020 2020 2020 2020 2020 2022 6465               "de
-00000540: 7363 7269 6265 223a 2022 e5bd 93e5 b9b6  scribe": "......
-00000550: e6b2 a1e6 9c89 e58f 91e7 949f e4bb 80e4  ................
-00000560: b988 e4ba 8b22 2c0a 2020 2020 2020 2020  .....",.        
-00000570: 2020 2020 2020 2274 6172 6765 7422 3a20        "target": 
-00000580: 300a 2020 2020 2020 2020 2020 2020 7d0a  0.            }.
-00000590: 2020 2020 2020 2020 2020 5d0a 2020 2020            ].    
-000005a0: 2020 2020 5d0a 2020 2020 7d2c 0a20 2020      ].    },.   
-000005b0: 207b 0a20 2020 2022 6576 656e 745f 6e61   {.    "event_na
-000005c0: 6d65 223a 2022 e5bf 83e8 848f e797 8522  me": "........."
-000005d0: 2c0a 2020 2020 2274 6172 6765 7422 3a20  ,.    "target": 
-000005e0: 302c 0a20 2020 2022 6465 7363 7269 6265  0,.    "describe
-000005f0: 223a 223c 303e e7aa 81e5 8f91 e5bf 83e8  ":"<0>..........
-00000600: 848f e797 85ef bc8c 222c 0a20 2020 2022  ........",.    "
-00000610: 7261 6e64 6f6d 5f65 7665 6e74 5f6f 6e63  random_event_onc
-00000620: 6522 3a20 5b5b 3235 2c20 7b0a 2020 2020  e": [[25, {.    
-00000630: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00000640: 616d 6522 3a20 22e5 bf83 e884 8fe7 9785  ame": ".........
-00000650: 2de5 8f91 e4bd 9c22 2c0a 2020 2020 2020  -......",.      
-00000660: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-00000670: 3a20 22e4 b88d e5b9 b8e7 a6bb e5bc 80e4  : ".............
-00000680: ba86 e688 98e5 9cba 222c 0a20 2020 2020  ........",.     
-00000690: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-000006a0: 2030 2c0a 2020 2020 2020 2020 2020 2020   0,.            
-000006b0: 2264 6965 223a 2031 0a20 2020 2020 2020  "die": 1.       
-000006c0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-000006d0: 205d 2c0a 2020 2020 2020 2020 2020 5b31   ],.          [1
-000006e0: 3030 2c20 7b0a 2020 2020 2020 2020 2020  00, {.          
-000006f0: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-00000700: 3a20 22e5 bf83 e884 8fe7 9785 2de6 97a0  : ".........-...
-00000710: e4ba 8be5 8f91 e794 9f22 2c0a 2020 2020  .........",.    
-00000720: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
-00000730: 6962 6522 3a20 22e4 bd86 e698 afe6 89be  ibe": ".........
-00000740: e588 b0e4 ba86 e88d afe7 89a9 efbc 8ce6  ................
-00000750: b4bb e4ba 86e8 bf87 e69d a522 2c0a 2020  ...........",.  
-00000760: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
-00000770: 6765 7422 3a20 300a 2020 2020 2020 2020  get": 0.        
-00000780: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
-00000790: 5d0a 2020 2020 2020 2020 5d0a 2020 2020  ].        ].    
-000007a0: 7d2c 0a20 2020 207b 0a20 2020 2022 6576  },.    {.    "ev
-000007b0: 656e 745f 6e61 6d65 223a 2022 e688 91e5  ent_name": "....
-000007c0: 91bd e69c 89e6 8891 e4b8 8de7 94b1 e5a4  ................
-000007d0: a922 2c0a 2020 2020 2274 6172 6765 7422  .",.    "target"
-000007e0: 3a20 302c 0a20 2020 2022 6465 7363 7269  : 0,.    "descri
-000007f0: 6265 223a 223c 303e e8a7 89e5 be97 e688  be":"<0>........
-00000800: 91e5 91bd e69c 89e6 8891 e4b8 8de7 94b1  ................
-00000810: e5a4 a9ef bc8c 222c 0a20 2020 2022 7261  ......",.    "ra
-00000820: 6e64 6f6d 5f65 7665 6e74 5f6f 6e63 6522  ndom_event_once"
-00000830: 3a20 5b5b 3135 2c20 7b0a 2020 2020 2020  : [[15, {.      
-00000840: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-00000850: 6522 3a20 22e6 8891 e591 bde6 9c89 e688  e": "...........
-00000860: 91e4 b88d e794 b1e5 a4a9 2de7 bb88 e782  ..........-.....
-00000870: b922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00000880: 2264 6573 6372 6962 6522 3a20 22e5 bfab  "describe": "...
-00000890: e980 9fe5 86b2 e588 b0e4 ba86 e7bb 88e7  ................
-000008a0: 82b9 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-000008b0: 2022 7461 7267 6574 223a 2030 2c0a 2020   "target": 0,.  
-000008c0: 2020 2020 2020 2020 2020 226d 6f76 6522            "move"
-000008d0: 3a20 3130 300a 2020 2020 2020 2020 2020  : 100.          
-000008e0: 2020 7d0a 2020 2020 2020 2020 2020 5d2c    }.          ],
-000008f0: 0a20 2020 2020 2020 2020 205b 3130 302c  .          [100,
-00000900: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-00000910: 2022 6576 656e 745f 6e61 6d65 223a 2022   "event_name": "
-00000920: e688 91e5 91bd e69c 89e6 8891 e4b8 8de7  ................
-00000930: 94b1 e5a4 a92d e697 a0e4 ba8b e58f 91e7  .....-..........
-00000940: 949f 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00000950: 2020 2022 6465 7363 7269 6265 223a 2022     "describe": "
-00000960: e4bd 86e6 98af e5b9 b6e6 b2a1 e4ba bae7  ................
-00000970: 9086 e4bb 9622 2c0a 2020 2020 2020 2020  .....",.        
-00000980: 2020 2020 2020 2274 6172 6765 7422 3a20        "target": 
-00000990: 300a 2020 2020 2020 2020 2020 2020 7d0a  0.            }.
-000009a0: 2020 2020 2020 2020 2020 5d0a 2020 2020            ].    
-000009b0: 2020 2020 5d0a 2020 2020 7d2c 0a20 2020      ].    },.   
-000009c0: 207b 0a20 2020 2022 6576 656e 745f 6e61   {.    "event_na
-000009d0: 6d65 223a 2022 e8af a1e8 aea1 222c 0a20  me": "......",. 
-000009e0: 2020 2022 7461 7267 6574 223a 2033 2c0a     "target": 3,.
-000009f0: 2020 2020 2264 6573 6372 6962 6522 3a20      "describe": 
-00000a00: 223c 303e e699 bae5 9586 e5a2 9ee5 8aa0  "<0>............
-00000a10: e4ba 86ef bc8c e696 bde4 ba86 e8af a1e8  ................
-00000a20: aea1 e4bd bfe5 be97 e999 a4e4 ba86 e4bb  ................
-00000a30: 96e4 b98b e5a4 96e7 9a84 e980 89e6 898b  ................
-00000a40: e980 80e5 9b9e e4ba 86e8 b5b7 e782 b921  ...............!
-00000a50: 222c 0a20 2020 2022 6d6f 7665 223a 202d  ",.    "move": -
-00000a60: 3130 300a 2020 2020 7d0a 5d0a            100.    }.].
+00000010: 6e74 5f6e 616d 6522 3a22 e7a9 bae9 97b4  nt_name":"......
+00000020: e8b7 b3e8 b783 5fe5 898d e8bf 9b33 222c  ......_......3",
+00000030: 0a20 2020 2022 7461 7267 6574 223a 302c  .    "target":0,
+00000040: 0a20 2020 2022 6465 7363 7269 6265 223a  .    "describe":
+00000050: 223c 303e e88e b7e5 be97 e4ba 86e7 99bd  "<0>............
+00000060: e4ba 95e9 bb91 e5ad 90e7 9a84 e58a 9be9  ................
+00000070: 878f efbc 8ce5 be80 e589 8de7 a9ba e997  ................
+00000080: b4e8 b7b3 e8b7 83e4 ba86 33e6 a0bc 2122  ..........3...!"
+00000090: 2c0a 2020 2020 226d 6f76 6522 3a33 0a20  ,.    "move":3. 
+000000a0: 2020 207d 2c0a 2020 2020 7b0a 2020 2020     },.    {.    
+000000b0: 2265 7665 6e74 5f6e 616d 6522 3a22 e69b  "event_name":"..
+000000c0: b2e7 8e87 e58a a0e9 809f 5fe5 898d e8bf  .........._.....
+000000d0: 9b33 222c 0a20 2020 2022 7461 7267 6574  .3",.    "target
+000000e0: 223a 302c 0a20 2020 2022 6465 7363 7269  ":0,.    "descri
+000000f0: 6265 223a 223c 303e e689 bee5 88b0 e4ba  be":"<0>........
+00000100: 86e4 b880 e4b8 aae6 9bb2 e78e 87e5 8aa0  ................
+00000110: e980 9fe5 99a8 efbc 8ce5 8aa0 e980 9fe5  ................
+00000120: 898d e8bf 9be4 ba86 33e6 a0bc 2122 2c0a  ........3...!",.
+00000130: 2020 2020 226d 6f76 6522 3a33 0a20 2020      "move":3.   
+00000140: 207d 2c0a 2020 2020 7b0a 2020 2020 2265   },.    {.    "e
+00000150: 7665 6e74 5f6e 616d 6522 3a22 e781 abe7  vent_name":"....
+00000160: aead e68e a8e8 bf9b e599 a85f e589 8de8  ..........._....
+00000170: bf9b 3322 2c0a 2020 2020 2274 6172 6765  ..3",.    "targe
+00000180: 7422 3a30 2c0a 2020 2020 2264 6573 6372  t":0,.    "descr
+00000190: 6962 6522 3a22 3c30 3ee6 89be e588 b0e4  ibe":"<0>.......
+000001a0: ba86 e4b8 80e4 b8aa e781 abe7 aead e68e  ................
+000001b0: a8e8 bf9b e599 a8ef bc8c e58a a0e9 809f  ................
+000001c0: e589 8de8 bf9b e4ba 8633 e6a0 bc22 2c0a  .........3...",.
+000001d0: 2020 2020 226d 6f76 6522 3a33 0a20 2020      "move":3.   
+000001e0: 207d 2c0a 2020 2020 7b0a 2020 2020 2265   },.    {.    "e
+000001f0: 7665 6e74 5f6e 616d 6522 3a22 e6b2 89e8  vent_name":"....
+00000200: bfb7 5048 7562 5fe5 908e e980 8032 222c  ..PHub_......2",
+00000210: 0a20 2020 2022 7461 7267 6574 223a 302c  .    "target":0,
+00000220: 0a20 2020 2022 6465 7363 7269 6265 223a  .    "describe":
+00000230: 223c 303e e6b2 89e8 bfb7 5048 7562 efbc  "<0>......PHub..
+00000240: 8ce5 908e e980 80e4 ba86 32e6 a0bc 222c  ..........2...",
+00000250: 0a20 2020 2022 6d6f 7665 223a 2d32 0a20  .    "move":-2. 
+00000260: 2020 207d 2c0a 2020 2020 7b0a 2020 2020     },.    {.    
+00000270: 2265 7665 6e74 5f6e 616d 6522 3a22 e884  "event_name":"..
+00000280: 9ae8 89ba e9a9 ac22 2c0a 2020 2020 2274  .......",.    "t
+00000290: 6172 6765 7422 3a30 2c0a 2020 2020 2264  arget":0,.    "d
+000002a0: 6573 6372 6962 6522 3a22 3c30 3ee6 8890  escribe":"<0>...
+000002b0: e4b8 bae4 ba86 e884 9ae8 89ba e9a9 acef  ................
+000002c0: bc8c e9a2 9de5 a496 e589 8de8 bf9b e4ba  ................
+000002d0: 8632 e6a0 bc22 2c0a 2020 2020 226d 6f76  .2...",.    "mov
+000002e0: 6522 3a32 0a20 2020 207d 2c0a 2020 2020  e":2.    },.    
+000002f0: 7b0a 2020 2020 2265 7665 6e74 5f6e 616d  {.    "event_nam
+00000300: 6522 3a22 e68e 89e5 85a5 e4ba 8ce6 aca1  e":"............
+00000310: e585 835f e590 8ee9 8080 3222 2c0a 2020  ..._......2",.  
+00000320: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+00000330: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+00000340: 3ee6 8e89 e585 a5e4 ba86 e4ba 8ce6 aca1  >...............
+00000350: e585 83ef bc8c e6b2 89e8 bfb7 e585 b6e4  ................
+00000360: b8ad efbc 8ce6 97a0 e6b3 95e8 87aa e68b  ................
+00000370: 94ef bc8c e590 8ee9 8080 e4ba 8632 e6a0  .............2..
+00000380: bc22 2c0a 2020 2020 226d 6f76 6522 3a2d  .",.    "move":-
+00000390: 320a 2020 2020 7d2c 0a20 2020 207b 0a20  2.    },.    {. 
+000003a0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
+000003b0: 22e9 a39e e69c bae5 87bb e4b8 ad22 2c0a  "............",.
+000003c0: 2020 2020 2274 6172 6765 7422 3a30 2c0a      "target":0,.
+000003d0: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+000003e0: 3c30 3ee8 a2ab e5a4 a9e4 b88a e79a 84e9  <0>.............
+000003f0: a39e e69c bae5 87bb e4b8 ade4 ba86 efbc  ................
+00000400: 8c22 2c0a 2020 2020 2272 616e 646f 6d5f  .",.    "random_
+00000410: 6576 656e 745f 6f6e 6365 223a 5b5b 3235  event_once":[[25
+00000420: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
+00000430: 2265 7665 6e74 5f6e 616d 6522 3a22 e9a3  "event_name":"..
+00000440: 9ee6 9cba e587 bbe4 b8ad 2de5 87bb e4b8  ..........-.....
+00000450: ad22 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00000460: 2264 6573 6372 6962 6522 3a22 e4b8 8de5  "describe":"....
+00000470: b9b8 e7a6 bbe5 bc80 e4ba 86e6 8898 e59c  ................
+00000480: ba22 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00000490: 2274 6172 6765 7422 3a30 2c0a 2020 2020  "target":0,.    
+000004a0: 2020 2020 2020 2020 2264 6965 223a 310a          "die":1.
+000004b0: 2020 2020 2020 2020 2020 2020 7d0a 2020              }.  
+000004c0: 2020 2020 2020 2020 5d2c 0a20 2020 2020          ],.     
+000004d0: 2020 2020 205b 3130 302c 207b 0a20 2020       [100, {.   
+000004e0: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+000004f0: 745f 6e61 6d65 223a 22e9 a39e e69c bae5  t_name":".......
+00000500: 87bb e4b8 ad2d e697 a0e4 ba8b e58f 91e7  .....-..........
+00000510: 949f 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00000520: 2020 2022 6465 7363 7269 6265 223a 22e5     "describe":".
+00000530: bd93 e5b9 b6e6 b2a1 e69c 89e5 8f91 e794  ................
+00000540: 9fe4 bb80 e4b9 88e4 ba8b 222c 0a20 2020  ..........",.   
+00000550: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+00000560: 6574 223a 300a 2020 2020 2020 2020 2020  et":0.          
+00000570: 2020 7d0a 2020 2020 2020 2020 2020 5d0a    }.          ].
+00000580: 2020 2020 2020 2020 5d0a 2020 2020 7d2c          ].    },
+00000590: 0a20 2020 207b 0a20 2020 2022 6576 656e  .    {.    "even
+000005a0: 745f 6e61 6d65 223a 22e5 bf83 e884 8fe7  t_name":".......
+000005b0: 9785 222c 0a20 2020 2022 7461 7267 6574  ..",.    "target
+000005c0: 223a 302c 0a20 2020 2022 6465 7363 7269  ":0,.    "descri
+000005d0: 6265 223a 223c 303e e7aa 81e5 8f91 e5bf  be":"<0>........
+000005e0: 83e8 848f e797 85ef bc8c 222c 0a20 2020  ..........",.   
+000005f0: 2022 7261 6e64 6f6d 5f65 7665 6e74 5f6f   "random_event_o
+00000600: 6e63 6522 3a5b 5b32 352c 207b 0a20 2020  nce":[[25, {.   
+00000610: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
+00000620: 6e61 6d65 223a 22e5 bf83 e884 8fe7 9785  name":".........
+00000630: 2de5 8f91 e4bd 9c22 2c0a 2020 2020 2020  -......",.      
+00000640: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00000650: 3a22 e4b8 8de5 b9b8 e7a6 bbe5 bc80 e4ba  :"..............
+00000660: 86e6 8898 e59c ba22 2c0a 2020 2020 2020  .......",.      
+00000670: 2020 2020 2020 2274 6172 6765 7422 3a30        "target":0
+00000680: 2c0a 2020 2020 2020 2020 2020 2020 2264  ,.            "d
+00000690: 6965 223a 310a 2020 2020 2020 2020 2020  ie":1.          
+000006a0: 2020 7d0a 2020 2020 2020 2020 2020 5d2c    }.          ],
+000006b0: 0a20 2020 2020 2020 2020 205b 3130 302c  .          [100,
+000006c0: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
+000006d0: 2022 6576 656e 745f 6e61 6d65 223a 22e5   "event_name":".
+000006e0: bf83 e884 8fe7 9785 2de6 97a0 e4ba 8be5  ........-.......
+000006f0: 8f91 e794 9f22 2c0a 2020 2020 2020 2020  .....",.        
+00000700: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00000710: 3a22 e4bd 86e6 98af e689 bee5 88b0 e4ba  :"..............
+00000720: 86e8 8daf e789 a9ef bc8c e6b4 bbe4 ba86  ................
+00000730: e8bf 87e6 9da5 222c 0a20 2020 2020 2020  ......",.       
+00000740: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
+00000750: 300a 2020 2020 2020 2020 2020 2020 7d0a  0.            }.
+00000760: 2020 2020 2020 2020 2020 5d0a 2020 2020            ].    
+00000770: 2020 2020 5d0a 2020 2020 7d2c 0a20 2020      ].    },.   
+00000780: 207b 0a20 2020 2022 6576 656e 745f 6e61   {.    "event_na
+00000790: 6d65 223a 22e6 8891 e591 bde6 9c89 e688  me":"...........
+000007a0: 91e4 b88d e794 b1e5 a4a9 222c 0a20 2020  ..........",.   
+000007b0: 2022 7461 7267 6574 223a 302c 0a20 2020   "target":0,.   
+000007c0: 2022 6465 7363 7269 6265 223a 223c 303e   "describe":"<0>
+000007d0: e8a7 89e5 be97 e688 91e5 91bd e69c 89e6  ................
+000007e0: 8891 e4b8 8de7 94b1 e5a4 a9ef bc8c 222c  ..............",
+000007f0: 0a20 2020 2022 7261 6e64 6f6d 5f65 7665  .    "random_eve
+00000800: 6e74 5f6f 6e63 6522 3a5b 5b31 352c 207b  nt_once":[[15, {
+00000810: 0a20 2020 2020 2020 2020 2020 2022 6576  .            "ev
+00000820: 656e 745f 6e61 6d65 223a 22e6 8891 e591  ent_name":".....
+00000830: bde6 9c89 e688 91e4 b88d e794 b1e5 a4a9  ................
+00000840: 2de7 bb88 e782 b922 2c0a 2020 2020 2020  -......",.      
+00000850: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00000860: 3a22 e5bf abe9 809f e586 b2e5 88b0 e4ba  :"..............
+00000870: 86e7 bb88 e782 b922 2c0a 2020 2020 2020  .......",.      
+00000880: 2020 2020 2020 2274 6172 6765 7422 3a30        "target":0
+00000890: 2c0a 2020 2020 2020 2020 2020 2020 226d  ,.            "m
+000008a0: 6f76 6522 3a31 3030 0a20 2020 2020 2020  ove":100.       
+000008b0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
+000008c0: 205d 2c0a 2020 2020 2020 2020 2020 5b31   ],.          [1
+000008d0: 3030 2c20 7b0a 2020 2020 2020 2020 2020  00, {.          
+000008e0: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+000008f0: 3a22 e688 91e5 91bd e69c 89e6 8891 e4b8  :"..............
+00000900: 8de7 94b1 e5a4 a92d e697 a0e4 ba8b e58f  .......-........
+00000910: 91e7 949f 222c 0a20 2020 2020 2020 2020  ....",.         
+00000920: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00000930: 22e4 bd86 e698 afe5 b9b6 e6b2 a1e4 baba  "...............
+00000940: e790 86e4 bb96 222c 0a20 2020 2020 2020  ......",.       
+00000950: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
+00000960: 300a 2020 2020 2020 2020 2020 2020 7d0a  0.            }.
+00000970: 2020 2020 2020 2020 2020 5d0a 2020 2020            ].    
+00000980: 2020 2020 5d0a 2020 2020 7d2c 0a20 2020      ].    },.   
+00000990: 207b 0a20 2020 2022 6576 656e 745f 6e61   {.    "event_na
+000009a0: 6d65 223a 22e8 afa1 e8ae a122 2c0a 2020  me":"......",.  
+000009b0: 2020 2274 6172 6765 7422 3a33 2c0a 2020    "target":3,.  
+000009c0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+000009d0: 3ee6 99ba e595 86e5 a29e e58a a0e4 ba86  >...............
+000009e0: efbc 8ce6 96bd e4ba 86e8 afa1 e8ae a1e4  ................
+000009f0: bdbf e5be 97e9 99a4 e4ba 86e4 bb96 e4b9  ................
+00000a00: 8be5 a496 e79a 84e9 8089 e689 8be9 8080  ................
+00000a10: e59b 9ee4 ba86 e8b5 b7e7 82b9 2122 2c0a  ............!",.
+00000a20: 2020 2020 226d 6f76 6522 3a2d 3130 300a      "move":-100.
+00000a30: 2020 2020 7d0a 5d0a                          }.].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/群友日常.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/群友日常.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 11% similar despite different names*

```diff
@@ -1,1399 +1,1381 @@
 00000000: 5b0a 2020 2020 7b0a 2020 2020 2020 2020  [.    {.        
-00000010: 2265 7665 6e74 5f6e 616d 6522 3a20 22e5  "event_name": ".
-00000020: 88ab e59c a8e8 bf99 e790 86e5 8f91 e5ba  ................
-00000030: 97ef bc81 222c 0a20 2020 2020 2020 2022  ....",.        "
-00000040: 6465 7363 7269 6265 223a 2022 3c30 3ee7  describe": "<0>.
-00000050: a0b8 e7a2 8ee4 ba86 e790 86e5 8f91 e5ba  ................
-00000060: 97e7 9a84 e4b8 89e8 89b2 e69f b1ef bc88  ................
-00000070: e9a9 b1e8 b5b6 e689 80e6 9c89 e4ba bae5  ................
-00000080: 898d e8bf 9b33 e6ad a5ef bc89 222c 0a20  .....3......",. 
-00000090: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-000000a0: 2032 2c0a 2020 2020 2020 2020 226d 6f76   2,.        "mov
-000000b0: 6522 3a20 330a 2020 2020 7d2c 0a20 2020  e": 3.    },.   
-000000c0: 207b 0a20 2020 2020 2020 2022 6576 656e   {.        "even
-000000d0: 745f 6e61 6d65 223a 2022 e7a6 81e6 ada2  t_name": "......
-000000e0: e889 b2e8 89b2 efbc 8122 2c0a 2020 2020  .........",.    
-000000f0: 2020 2020 2264 6573 6372 6962 6522 3a20      "describe": 
-00000100: 223c 303e efbc 9ae9 83bd e8af b4e4 ba86  "<0>............
-00000110: e587 a0e9 818d efbc 8ce4 b88d e883 bde8  ................
-00000120: 89b2 e889 b2ef bc81 efbc 88e9 99a4 e4ba  ................
-00000130: 86e8 87aa e5b7 b1e5 85a8 e591 98e6 8892  ................
-00000140: e889 b2e7 9ca9 e699 95e4 b880 e59b 9ee5  ................
-00000150: 9088 efbc 8922 2c0a 2020 2020 2020 2020  .....",.        
-00000160: 2274 6172 6765 7422 3a20 332c 0a20 2020  "target": 3,.   
-00000170: 2020 2020 2022 7665 7274 6967 6f22 3a20       "vertigo": 
-00000180: 312c 0a20 2020 2020 2020 2022 726f 756e  1,.        "roun
-00000190: 6473 223a 2031 2c0a 2020 2020 2020 2020  ds": 1,.        
-000001a0: 226e 616d 6522 3a22 e4b8 8de5 8786 e6b6  "name":"........
-000001b0: a9e6 b6a9 220a 2020 2020 7d2c 0a20 2020  ....".    },.   
-000001c0: 207b 0a20 2020 2020 2020 2022 6576 656e   {.        "even
-000001d0: 745f 6e61 6d65 223a 2022 e7be a4e4 b8bb  t_name": "......
-000001e0: e7a7 81e5 8f91 e4ba 86e5 a5b3 e8a3 85ef  ................
-000001f0: bc81 222c 0a20 2020 2020 2020 2022 6465  ..",.        "de
-00000200: 7363 7269 6265 223a 2022 3c30 3ee6 94b6  scribe": "<0>...
-00000210: e588 b0e4 ba86 e7be a4e4 b8bb e7a7 81e5  ................
-00000220: 8f91 e79a 84e5 a5b3 e8a3 8528 e589 8de8  ...........(....
-00000230: bf9b 3130 e6ad a5e4 bd86 e586 b2e6 9995  ..10............
-00000240: e4b8 80e5 9b9e e590 88ef bc89 222c 0a20  ............",. 
-00000250: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00000260: 2030 2c0a 2020 2020 2020 2020 2276 6572   0,.        "ver
-00000270: 7469 676f 223a 2031 2c0a 2020 2020 2020  tigo": 1,.      
-00000280: 2020 2272 6f75 6e64 7322 3a20 312c 0a20    "rounds": 1,. 
-00000290: 2020 2020 2020 2022 6d6f 7665 223a 2031         "move": 1
-000002a0: 302c 0a20 2020 2020 2020 2022 6e61 6d65  0,.        "name
-000002b0: 223a 22e7 bea4 e4b8 bbe5 a5b3 e8a3 8522  ":"............"
-000002c0: 0a20 2020 207d 2c0a 2020 2020 7b0a 2020  .    },.    {.  
-000002d0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-000002e0: 6522 3a20 22e7 bea4 e4b8 bbe8 afb7 e4ba  e": "...........
-000002f0: 86e6 af8f e4b8 aae4 baba e796 afe7 8b82  ................
-00000300: e698 9fe6 9c9f e59b 9b22 2c0a 2020 2020  .........",.    
-00000310: 2020 2020 2264 6573 6372 6962 6522 3a20      "describe": 
-00000320: 223c 303e e7be a4e4 b8bb 56e4 ba86 e688  "<0>......V.....
-00000330: 9135 30ef bc88 e689 80e6 9c89 e4ba bae6  .50.............
-00000340: ada2 e6ad a5e4 b880 e59b 9ee5 9088 e58e  ................
-00000350: bbe4 ba86 4b46 43ef bc89 222c 0a20 2020  ....KFC...",.   
-00000360: 2020 2020 2022 7461 7267 6574 223a 2033       "target": 3
-00000370: 2c0a 2020 2020 2020 2020 226c 6f63 6174  ,.        "locat
-00000380: 655f 6c6f 636b 223a 312c 0a20 2020 2020  e_lock":1,.     
-00000390: 2020 2022 726f 756e 6473 223a 2031 2c0a     "rounds": 1,.
-000003a0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
-000003b0: 4372 617a 7920 5468 7572 7364 6179 2122  Crazy Thursday!"
-000003c0: 0a20 2020 207d 2c0a 2020 2020 7b0a 2020  .    },.    {.  
-000003d0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-000003e0: 6522 3a20 22e6 8891 e58f 91e4 ba86 e889  e": "...........
-000003f0: b2e5 9bbe 222c 0a20 2020 2020 2020 2022  ....",.        "
-00000400: 6465 7363 7269 6265 223a 2022 3c30 3ee5  describe": "<0>.
-00000410: 8f91 e4ba 8631 2d31 30e5 bca0 e889 b2e5  .....1-10.......
-00000420: 9bbe efbc 88e9 9a8f e69c bae7 9bae e6a0  ................
-00000430: 87e7 9ca9 e699 95e5 afb9 e5ba 94e8 89b2  ................
-00000440: e59b bee6 95b0 e79a 84e5 9b9e e590 88ef  ................
-00000450: bc8c e88b a5e4 b8ba 35e3 8081 36e3 8081  ........5...6...
-00000460: 37e5 bca0 e68f 90e9 ab98 e69c 80e5 a4a7  7...............
-00000470: e980 9fef bc89 222c 0a20 2020 2020 2020  ......",.       
-00000480: 2022 7461 7267 6574 223a 2034 2c0a 2020   "target": 4,.  
-00000490: 2020 2020 2020 2272 616e 646f 6d5f 6576        "random_ev
-000004a0: 656e 745f 6f6e 6365 223a 205b 0a20 2020  ent_once": [.   
-000004b0: 2020 2020 2020 2020 2020 2020 205b 3130               [10
-000004c0: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
-000004d0: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-000004e0: 616d 6522 3a20 22e6 8891 e58f 91e4 ba86  ame": ".........
-000004f0: 31e5 bca0 e889 b2e5 9bbe 222c 0a20 2020  1.........",.   
-00000500: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000510: 2022 6465 7363 7269 6265 223a 2022 e5a5   "describe": "..
-00000520: bde8 afb6 efbc 8131 e5bc a0e8 89b2 e59b  .......1........
-00000530: beef bc81 efbc 883c 313e e68b bfe5 88b0  .......<1>......
-00000540: e4ba 86e4 b880 e5bc a0e8 89b2 e59b beef  ................
-00000550: bc8c e4b8 94e4 bd93 e58a 9be4 b88d e694  ................
-00000560: afe6 9995 e4ba 8631 e59b 9ee5 9088 efbc  .......1........
-00000570: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00000580: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-00000590: 3a20 312c 0a20 2020 2020 2020 2020 2020  : 1,.           
-000005a0: 2020 2020 2020 2020 2022 7665 7274 6967           "vertig
-000005b0: 6f22 3a20 312c 0a20 2020 2020 2020 2020  o": 1,.         
-000005c0: 2020 2020 2020 2020 2020 2022 726f 756e             "roun
-000005d0: 6473 223a 2031 2c0a 2020 2020 2020 2020  ds": 1,.        
-000005e0: 2020 2020 2020 2020 2020 2020 226e 616d              "nam
-000005f0: 6522 3a22 e586 b2e6 9995 e4ba 8622 0a20  e":".........". 
-00000600: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000610: 2020 207d 0a20 2020 2020 2020 2020 2020     }.           
-00000620: 2020 2020 205d 2c0a 2020 2020 2020 2020       ],.        
-00000630: 2020 2020 2020 2020 5b32 302c 207b 0a20          [20, {. 
-00000640: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000650: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-00000660: 2022 e688 91e5 8f91 e4ba 8632 e5bc a0e8   ".........2....
-00000670: 89b2 e59b be22 2c0a 2020 2020 2020 2020  .....",.        
-00000680: 2020 2020 2020 2020 2020 2020 2264 6573              "des
-00000690: 6372 6962 6522 3a20 22e5 a5bd e8af b6ef  cribe": ".......
-000006a0: bc81 32e5 bca0 e889 b2e5 9bbe efbc 81ef  ..2.............
-000006b0: bc88 3c31 3ee6 8bbf e588 b0e4 ba86 32e5  ..<1>.........2.
-000006c0: bca0 e889 b2e5 9bbe efbc 8ce4 b894 e4bd  ................
-000006d0: 93e5 8a9b e4b8 8de6 94af e699 95e4 ba86  ................
-000006e0: 32e5 9b9e e590 88ef bc89 222c 0a20 2020  2.........",.   
+00000010: 2265 7665 6e74 5f6e 616d 6522 3a22 e588  "event_name":"..
+00000020: abe5 9ca8 e8bf 99e7 9086 e58f 91e5 ba97  ................
+00000030: efbc 8122 2c0a 2020 2020 2020 2020 2264  ...",.        "d
+00000040: 6573 6372 6962 6522 3a22 3c30 3ee7 a0b8  escribe":"<0>...
+00000050: e7a2 8ee4 ba86 e790 86e5 8f91 e5ba 97e7  ................
+00000060: 9a84 e4b8 89e8 89b2 e69f b1ef bc88 e9a9  ................
+00000070: b1e8 b5b6 e689 80e6 9c89 e4ba bae5 898d  ................
+00000080: e8bf 9b33 e6ad a5ef bc89 222c 0a20 2020  ...3......",.   
+00000090: 2020 2020 2022 7461 7267 6574 223a 322c       "target":2,
+000000a0: 0a20 2020 2020 2020 2022 6d6f 7665 223a  .        "move":
+000000b0: 330a 2020 2020 7d2c 0a20 2020 207b 0a20  3.    },.    {. 
+000000c0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+000000d0: 6d65 223a 22e7 a681 e6ad a2e8 89b2 e889  me":"...........
+000000e0: b2ef bc81 222c 0a20 2020 2020 2020 2022  ....",.        "
+000000f0: 6465 7363 7269 6265 223a 223c 303e efbc  describe":"<0>..
+00000100: 9ae9 83bd e8af b4e4 ba86 e587 a0e9 818d  ................
+00000110: efbc 8ce4 b88d e883 bde8 89b2 e889 b2ef  ................
+00000120: bc81 efbc 88e9 99a4 e4ba 86e8 87aa e5b7  ................
+00000130: b1e5 85a8 e591 98e6 8892 e889 b2e7 9ca9  ................
+00000140: e699 95e4 b880 e59b 9ee5 9088 efbc 8922  ..............."
+00000150: 2c0a 2020 2020 2020 2020 2274 6172 6765  ,.        "targe
+00000160: 7422 3a33 2c0a 2020 2020 2020 2020 2276  t":3,.        "v
+00000170: 6572 7469 676f 223a 312c 0a20 2020 2020  ertigo":1,.     
+00000180: 2020 2022 726f 756e 6473 223a 312c 0a20     "rounds":1,. 
+00000190: 2020 2020 2020 2022 6e61 6d65 223a 22e4         "name":".
+000001a0: b88d e587 86e6 b6a9 e6b6 a922 0a20 2020  ...........".   
+000001b0: 207d 2c0a 2020 2020 7b0a 2020 2020 2020   },.    {.      
+000001c0: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+000001d0: e7be a4e4 b8bb e7a7 81e5 8f91 e4ba 86e5  ................
+000001e0: a5b3 e8a3 85ef bc81 222c 0a20 2020 2020  ........",.     
+000001f0: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00000200: 303e e694 b6e5 88b0 e4ba 86e7 bea4 e4b8  0>..............
+00000210: bbe7 a781 e58f 91e7 9a84 e5a5 b3e8 a385  ................
+00000220: 28e5 898d e8bf 9b31 30e6 ada5 e4bd 86e5  (......10.......
+00000230: 86b2 e699 95e4 b880 e59b 9ee5 9088 efbc  ................
+00000240: 8922 2c0a 2020 2020 2020 2020 2274 6172  .",.        "tar
+00000250: 6765 7422 3a30 2c0a 2020 2020 2020 2020  get":0,.        
+00000260: 2276 6572 7469 676f 223a 312c 0a20 2020  "vertigo":1,.   
+00000270: 2020 2020 2022 726f 756e 6473 223a 312c       "rounds":1,
+00000280: 0a20 2020 2020 2020 2022 6d6f 7665 223a  .        "move":
+00000290: 3130 2c0a 2020 2020 2020 2020 226e 616d  10,.        "nam
+000002a0: 6522 3a22 e7be a4e4 b8bb e5a5 b3e8 a385  e":"............
+000002b0: 220a 2020 2020 7d2c 0a20 2020 207b 0a20  ".    },.    {. 
+000002c0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+000002d0: 6d65 223a 22e7 bea4 e4b8 bbe8 afb7 e4ba  me":"...........
+000002e0: 86e6 af8f e4b8 aae4 baba e796 afe7 8b82  ................
+000002f0: e698 9fe6 9c9f e59b 9b22 2c0a 2020 2020  .........",.    
+00000300: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00000310: 3c30 3ee7 bea4 e4b8 bb56 e4ba 86e6 8891  <0>......V......
+00000320: 3530 efbc 88e6 8980 e69c 89e4 baba e6ad  50..............
+00000330: a2e6 ada5 e4b8 80e5 9b9e e590 88e5 8ebb  ................
+00000340: e4ba 864b 4643 efbc 8922 2c0a 2020 2020  ...KFC...",.    
+00000350: 2020 2020 2274 6172 6765 7422 3a33 2c0a      "target":3,.
+00000360: 2020 2020 2020 2020 226c 6f63 6174 655f          "locate_
+00000370: 6c6f 636b 223a 312c 0a20 2020 2020 2020  lock":1,.       
+00000380: 2022 726f 756e 6473 223a 312c 0a20 2020   "rounds":1,.   
+00000390: 2020 2020 2022 6e61 6d65 223a 2243 7261       "name":"Cra
+000003a0: 7a79 2054 6875 7273 6461 7921 220a 2020  zy Thursday!".  
+000003b0: 2020 7d2c 0a20 2020 207b 0a20 2020 2020    },.    {.     
+000003c0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
+000003d0: 22e6 8891 e58f 91e4 ba86 e889 b2e5 9bbe  "...............
+000003e0: 222c 0a20 2020 2020 2020 2022 6465 7363  ",.        "desc
+000003f0: 7269 6265 223a 223c 303e e58f 91e4 ba86  ribe":"<0>......
+00000400: 312d 3130 e5bc a0e8 89b2 e59b beef bc88  1-10............
+00000410: e99a 8fe6 9cba e79b aee6 a087 e79c a9e6  ................
+00000420: 9995 e5af b9e5 ba94 e889 b2e5 9bbe e695  ................
+00000430: b0e7 9a84 e59b 9ee5 9088 efbc 8ce8 8ba5  ................
+00000440: e4b8 ba35 e380 8136 e380 8137 e5bc a0e6  ...5...6...7....
+00000450: 8f90 e9ab 98e6 9c80 e5a4 a7e9 809f efbc  ................
+00000460: 8922 2c0a 2020 2020 2020 2020 2274 6172  .",.        "tar
+00000470: 6765 7422 3a34 2c0a 2020 2020 2020 2020  get":4,.        
+00000480: 2272 616e 646f 6d5f 6576 656e 745f 6f6e  "random_event_on
+00000490: 6365 223a 5b0a 2020 2020 2020 2020 2020  ce":[.          
+000004a0: 2020 2020 2020 5b31 302c 207b 0a20 2020        [10, {.   
+000004b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000004c0: 2022 6576 656e 745f 6e61 6d65 223a 22e6   "event_name":".
+000004d0: 8891 e58f 91e4 ba86 31e5 bca0 e889 b2e5  ........1.......
+000004e0: 9bbe 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+000004f0: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
+00000500: 6265 223a 22e5 a5bd e8af b6ef bc81 31e5  be":".........1.
+00000510: bca0 e889 b2e5 9bbe efbc 81ef bc88 3c31  ..............<1
+00000520: 3ee6 8bbf e588 b0e4 ba86 e4b8 80e5 bca0  >...............
+00000530: e889 b2e5 9bbe efbc 8ce4 b894 e4bd 93e5  ................
+00000540: 8a9b e4b8 8de6 94af e699 95e4 ba86 31e5  ..............1.
+00000550: 9b9e e590 88ef bc89 222c 0a20 2020 2020  ........",.     
+00000560: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000570: 7461 7267 6574 223a 312c 0a20 2020 2020  target":1,.     
+00000580: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000590: 7665 7274 6967 6f22 3a31 2c0a 2020 2020  vertigo":1,.    
+000005a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000005b0: 2272 6f75 6e64 7322 3a31 2c0a 2020 2020  "rounds":1,.    
+000005c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000005d0: 226e 616d 6522 3a22 e586 b2e6 9995 e4ba  "name":"........
+000005e0: 8622 0a20 2020 2020 2020 2020 2020 2020  .".             
+000005f0: 2020 2020 2020 207d 0a20 2020 2020 2020         }.       
+00000600: 2020 2020 2020 2020 205d 2c0a 2020 2020           ],.    
+00000610: 2020 2020 2020 2020 2020 2020 5b32 302c              [20,
+00000620: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
+00000630: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+00000640: 6d65 223a 22e6 8891 e58f 91e4 ba86 32e5  me":".........2.
+00000650: bca0 e889 b2e5 9bbe 222c 0a20 2020 2020  ........",.     
+00000660: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000670: 6465 7363 7269 6265 223a 22e5 a5bd e8af  describe":".....
+00000680: b6ef bc81 32e5 bca0 e889 b2e5 9bbe efbc  ....2...........
+00000690: 81ef bc88 3c31 3ee6 8bbf e588 b0e4 ba86  ....<1>.........
+000006a0: 32e5 bca0 e889 b2e5 9bbe efbc 8ce4 b894  2...............
+000006b0: e4bd 93e5 8a9b e4b8 8de6 94af e699 95e4  ................
+000006c0: ba86 32e5 9b9e e590 88ef bc89 222c 0a20  ..2.........",. 
+000006d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000006e0: 2020 2022 7461 7267 6574 223a 312c 0a20     "target":1,. 
 000006f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000700: 2022 7461 7267 6574 223a 2031 2c0a 2020   "target": 1,.  
+00000700: 2020 2022 7665 7274 6967 6f22 3a31 2c0a     "vertigo":1,.
 00000710: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000720: 2020 2276 6572 7469 676f 223a 2031 2c0a    "vertigo": 1,.
+00000720: 2020 2020 2272 6f75 6e64 7322 3a32 2c0a      "rounds":2,.
 00000730: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000740: 2020 2020 2272 6f75 6e64 7322 3a20 322c      "rounds": 2,
-00000750: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000760: 2020 2020 2022 6e61 6d65 223a 22e5 86b2       "name":"...
-00000770: e699 95e4 ba86 220a 2020 2020 2020 2020  ......".        
-00000780: 2020 2020 2020 2020 2020 2020 7d0a 2020              }.  
-00000790: 2020 2020 2020 2020 2020 2020 2020 5d2c                ],
-000007a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000007b0: 205b 3330 2c20 7b0a 2020 2020 2020 2020   [30, {.        
-000007c0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
-000007d0: 6e74 5f6e 616d 6522 3a20 22e6 8891 e58f  nt_name": ".....
-000007e0: 91e4 ba86 33e5 bca0 e889 b2e5 9bbe 222c  ....3.........",
-000007f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000800: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
-00000810: 2022 e5a5 bde8 afb6 efbc 8133 e5bc a0e8   ".........3....
-00000820: 89b2 e59b beef bc81 efbc 883c 313e e68b  ...........<1>..
-00000830: bfe5 88b0 e4ba 8633 e5bc a0e8 89b2 e59b  .......3........
-00000840: beef bc8c e4b8 94e4 bd93 e58a 9be4 b88d  ................
-00000850: e694 afe6 9995 e4ba 8633 e59b 9ee5 9088  .........3......
-00000860: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
-00000870: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
-00000880: 7422 3a20 312c 0a20 2020 2020 2020 2020  t": 1,.         
-00000890: 2020 2020 2020 2020 2020 2022 7665 7274             "vert
-000008a0: 6967 6f22 3a20 312c 0a20 2020 2020 2020  igo": 1,.       
-000008b0: 2020 2020 2020 2020 2020 2020 2022 726f               "ro
-000008c0: 756e 6473 223a 2033 2c0a 2020 2020 2020  unds": 3,.      
-000008d0: 2020 2020 2020 2020 2020 2020 2020 226e                "n
-000008e0: 616d 6522 3a22 e586 b2e6 9995 e4ba 8622  ame":"........."
-000008f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000900: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-00000910: 2020 2020 2020 205d 2c0a 2020 2020 2020         ],.      
-00000920: 2020 2020 2020 2020 2020 5b34 302c 207b            [40, {
-00000930: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000940: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00000950: 223a 2022 e688 91e5 8f91 e4ba 8634 e5bc  ": ".........4..
-00000960: a0e8 89b2 e59b be22 2c0a 2020 2020 2020  .......",.      
-00000970: 2020 2020 2020 2020 2020 2020 2020 2264                "d
-00000980: 6573 6372 6962 6522 3a20 22e5 a5bd e8af  escribe": ".....
-00000990: b6ef bc81 34e5 bca0 e889 b2e5 9bbe efbc  ....4...........
-000009a0: 81ef bc88 3c31 3ee6 8bbf e588 b0e4 ba86  ....<1>.........
-000009b0: 34e5 bca0 e889 b2e5 9bbe efbc 8ce4 b894  4...............
-000009c0: e4bd 93e5 8a9b e4b8 8de6 94af e699 95e4  ................
-000009d0: ba86 34e5 9b9e e590 88ef bc89 222c 0a20  ..4.........",. 
-000009e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000009f0: 2020 2022 7461 7267 6574 223a 2031 2c0a     "target": 1,.
-00000a00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a10: 2020 2020 2276 6572 7469 676f 223a 2031      "vertigo": 1
-00000a20: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00000a30: 2020 2020 2020 2272 6f75 6e64 7322 3a20        "rounds": 
-00000a40: 342c 0a20 2020 2020 2020 2020 2020 2020  4,.             
-00000a50: 2020 2020 2020 2022 6e61 6d65 223a 22e5         "name":".
-00000a60: 86b2 e699 95e4 ba86 220a 2020 2020 2020  ........".      
-00000a70: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
+00000740: 2020 2020 226e 616d 6522 3a22 e586 b2e6      "name":"....
+00000750: 9995 e4ba 8622 0a20 2020 2020 2020 2020  .....".         
+00000760: 2020 2020 2020 2020 2020 207d 0a20 2020             }.   
+00000770: 2020 2020 2020 2020 2020 2020 205d 2c0a               ],.
+00000780: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000790: 5b33 302c 207b 0a20 2020 2020 2020 2020  [30, {.         
+000007a0: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+000007b0: 745f 6e61 6d65 223a 22e6 8891 e58f 91e4  t_name":".......
+000007c0: ba86 33e5 bca0 e889 b2e5 9bbe 222c 0a20  ..3.........",. 
+000007d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000007e0: 2020 2022 6465 7363 7269 6265 223a 22e5     "describe":".
+000007f0: a5bd e8af b6ef bc81 33e5 bca0 e889 b2e5  ........3.......
+00000800: 9bbe efbc 81ef bc88 3c31 3ee6 8bbf e588  ........<1>.....
+00000810: b0e4 ba86 33e5 bca0 e889 b2e5 9bbe efbc  ....3...........
+00000820: 8ce4 b894 e4bd 93e5 8a9b e4b8 8de6 94af  ................
+00000830: e699 95e4 ba86 33e5 9b9e e590 88ef bc89  ......3.........
+00000840: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00000850: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
+00000860: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
+00000870: 2020 2020 2020 2022 7665 7274 6967 6f22         "vertigo"
+00000880: 3a31 2c0a 2020 2020 2020 2020 2020 2020  :1,.            
+00000890: 2020 2020 2020 2020 2272 6f75 6e64 7322          "rounds"
+000008a0: 3a33 2c0a 2020 2020 2020 2020 2020 2020  :3,.            
+000008b0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+000008c0: e586 b2e6 9995 e4ba 8622 0a20 2020 2020  .........".     
+000008d0: 2020 2020 2020 2020 2020 2020 2020 207d                 }
+000008e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000008f0: 205d 2c0a 2020 2020 2020 2020 2020 2020   ],.            
+00000900: 2020 2020 5b34 302c 207b 0a20 2020 2020      [40, {.     
+00000910: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00000920: 6576 656e 745f 6e61 6d65 223a 22e6 8891  event_name":"...
+00000930: e58f 91e4 ba86 34e5 bca0 e889 b2e5 9bbe  ......4.........
+00000940: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00000950: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
+00000960: 223a 22e5 a5bd e8af b6ef bc81 34e5 bca0  ":".........4...
+00000970: e889 b2e5 9bbe efbc 81ef bc88 3c31 3ee6  ............<1>.
+00000980: 8bbf e588 b0e4 ba86 34e5 bca0 e889 b2e5  ........4.......
+00000990: 9bbe efbc 8ce4 b894 e4bd 93e5 8a9b e4b8  ................
+000009a0: 8de6 94af e699 95e4 ba86 34e5 9b9e e590  ..........4.....
+000009b0: 88ef bc89 222c 0a20 2020 2020 2020 2020  ....",.         
+000009c0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+000009d0: 6574 223a 312c 0a20 2020 2020 2020 2020  et":1,.         
+000009e0: 2020 2020 2020 2020 2020 2022 7665 7274             "vert
+000009f0: 6967 6f22 3a31 2c0a 2020 2020 2020 2020  igo":1,.        
+00000a00: 2020 2020 2020 2020 2020 2020 2272 6f75              "rou
+00000a10: 6e64 7322 3a34 2c0a 2020 2020 2020 2020  nds":4,.        
+00000a20: 2020 2020 2020 2020 2020 2020 226e 616d              "nam
+00000a30: 6522 3a22 e586 b2e6 9995 e4ba 8622 0a20  e":".........". 
+00000a40: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000a50: 2020 207d 0a20 2020 2020 2020 2020 2020     }.           
+00000a60: 2020 2020 205d 2c0a 2020 2020 2020 2020       ],.        
+00000a70: 2020 2020 2020 2020 5b35 302c 207b 0a20          [50, {. 
 00000a80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a90: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
-00000aa0: 2020 205b 3530 2c20 7b0a 2020 2020 2020     [50, {.      
-00000ab0: 2020 2020 2020 2020 2020 2020 2020 2265                "e
-00000ac0: 7665 6e74 5f6e 616d 6522 3a20 22e6 8891  vent_name": "...
-00000ad0: e58f 91e4 ba86 35e5 bca0 e889 b2e5 9bbe  ......5.........
-00000ae0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00000af0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-00000b00: 223a 2022 e5a5 bde8 afb6 efbc 8135 e5bc  ": ".........5..
-00000b10: a0e8 89b2 e59b beef bc81 efbc 883c 313e  .............<1>
-00000b20: e68b bfe5 88b0 e4ba 8635 e5bc a0e8 89b2  .........5......
-00000b30: e59b beef bc8c e4b8 94e4 bd93 e58a 9be4  ................
-00000b40: b88d e694 afe6 9995 e4ba 8635 e59b 9ee5  ...........5....
-00000b50: 9088 efbc 8ce4 bd86 e4bb 96e7 9a84 e585  ................
-00000b60: bde6 80a7 e8a2 abe5 b08f e6bf 80e5 8f91  ................
-00000b70: e4ba 86ef bc8c e980 9fe5 baa6 e69c 80e5  ................
-00000b80: a4a7 e58f 98e4 b8ba 32ef bc89 222c 0a20  ........2...",. 
-00000b90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000ba0: 2020 2022 7461 7267 6574 223a 2031 2c0a     "target": 1,.
-00000bb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000bc0: 2020 2020 2276 6572 7469 676f 223a 2031      "vertigo": 1
-00000bd0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00000be0: 2020 2020 2020 2272 6f75 6e64 7322 3a20        "rounds": 
-00000bf0: 352c 0a20 2020 2020 2020 2020 2020 2020  5,.             
-00000c00: 2020 2020 2020 2022 6d6f 7665 5f6d 6178         "move_max
-00000c10: 223a 322c 0a20 2020 2020 2020 2020 2020  ":2,.           
-00000c20: 2020 2020 2020 2020 2022 6d6f 7665 5f6d           "move_m
-00000c30: 696e 223a 322c 0a20 2020 2020 2020 2020  in":2,.         
-00000c40: 2020 2020 2020 2020 2020 2022 6e61 6d65             "name
-00000c50: 223a 22e5 86b2 e699 95e4 ba86 e4bd 86e7  ":".............
-00000c60: 88bd 220a 2020 2020 2020 2020 2020 2020  ..".            
-00000c70: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
-00000c80: 2020 2020 2020 2020 2020 5d2c 0a20 2020            ],.   
-00000c90: 2020 2020 2020 2020 2020 2020 205b 3630               [60
-00000ca0: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
-00000cb0: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00000cc0: 616d 6522 3a20 22e6 8891 e58f 91e4 ba86  ame": ".........
-00000cd0: 36e5 bca0 e889 b2e5 9bbe 222c 0a20 2020  6.........",.   
-00000ce0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000cf0: 2022 6465 7363 7269 6265 223a 2022 e5a5   "describe": "..
-00000d00: bde8 afb6 efbc 8136 e5bc a0e8 89b2 e59b  .......6........
-00000d10: beef bc81 efbc 883c 313e e68b bfe5 88b0  .......<1>......
-00000d20: e4ba 8636 e5bc a0e8 89b2 e59b beef bc8c  ...6............
-00000d30: e4b8 94e4 bd93 e58a 9be4 b88d e694 afe6  ................
-00000d40: 9995 e4ba 8636 e59b 9ee5 9088 efbc 8ce4  .....6..........
-00000d50: bd86 e4bb 96e7 9a84 e585 bde6 80a7 e8a2  ................
-00000d60: abe4 b8ad e6bf 80e5 8f91 e4ba 86ef bc8c  ................
-00000d70: e980 9fe5 baa6 e69c 80e5 a4a7 e58f 98e4  ................
-00000d80: b8ba 33ef bc89 222c 0a20 2020 2020 2020  ..3...",.       
-00000d90: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
-00000da0: 7267 6574 223a 2031 2c0a 2020 2020 2020  rget": 1,.      
-00000db0: 2020 2020 2020 2020 2020 2020 2020 2276                "v
-00000dc0: 6572 7469 676f 223a 2031 2c0a 2020 2020  ertigo": 1,.    
-00000dd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000de0: 2272 6f75 6e64 7322 3a20 362c 0a20 2020  "rounds": 6,.   
-00000df0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000e00: 2022 6d6f 7665 5f6d 6178 223a 332c 0a20   "move_max":3,. 
-00000e10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000e20: 2020 2022 6d6f 7665 5f6d 696e 223a 332c     "move_min":3,
-00000e30: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000e40: 2020 2020 2022 6e61 6d65 223a 22e5 86b2       "name":"...
-00000e50: e699 95e4 ba86 e4bd 86e7 88bd 220a 2020  ............".  
-00000e60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000e70: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-00000e80: 2020 2020 5d2c 0a20 2020 2020 2020 2020      ],.         
-00000e90: 2020 2020 2020 205b 3730 2c20 7b0a 2020         [70, {.  
-00000ea0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000eb0: 2020 2265 7665 6e74 5f6e 616d 6522 3a20    "event_name": 
-00000ec0: 22e6 8891 e58f 91e4 ba86 37e5 bca0 e889  ".........7.....
-00000ed0: b2e5 9bbe 222c 0a20 2020 2020 2020 2020  ....",.         
-00000ee0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-00000ef0: 7269 6265 223a 2022 e5a5 bde8 afb6 efbc  ribe": "........
-00000f00: 8137 e5bc a0e8 89b2 e59b beef bc81 efbc  .7..............
-00000f10: 883c 313e e68b bfe5 88b0 e4ba 8637 e5bc  .<1>.........7..
-00000f20: a0e8 89b2 e59b beef bc8c e4b8 94e4 bd93  ................
-00000f30: e58a 9be4 b88d e694 afe6 9995 e4ba 8637  ...............7
-00000f40: e59b 9ee5 9088 efbc 8ce4 bd86 e4bb 96e7  ................
-00000f50: 9a84 e585 bde6 80a7 e8a2 abe5 a4a7 e6bf  ................
-00000f60: 80e5 8f91 e4ba 86ef bc8c e980 9fe5 baa6  ................
-00000f70: e69c 80e5 a4a7 e58f 98e4 b8ba 34ef bc89  ............4...
-00000f80: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00000f90: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00000fa0: 2031 2c0a 2020 2020 2020 2020 2020 2020   1,.            
-00000fb0: 2020 2020 2020 2020 2276 6572 7469 676f          "vertigo
-00000fc0: 223a 2031 2c0a 2020 2020 2020 2020 2020  ": 1,.          
-00000fd0: 2020 2020 2020 2020 2020 2272 6f75 6e64            "round
-00000fe0: 7322 3a20 372c 0a20 2020 2020 2020 2020  s": 7,.         
-00000ff0: 2020 2020 2020 2020 2020 2022 6d6f 7665             "move
-00001000: 5f6d 6178 223a 342c 0a20 2020 2020 2020  _max":4,.       
-00001010: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
-00001020: 7665 5f6d 696e 223a 342c 0a20 2020 2020  ve_min":4,.     
-00001030: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00001040: 6e61 6d65 223a 22e5 86b2 e699 95e4 ba86  name":".........
-00001050: e4bd 86e7 88bd 220a 2020 2020 2020 2020  ......".        
-00001060: 2020 2020 2020 2020 2020 2020 7d0a 2020              }.  
-00001070: 2020 2020 2020 2020 2020 2020 2020 5d2c                ],
-00001080: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001090: 205b 3830 2c20 7b0a 2020 2020 2020 2020   [80, {.        
-000010a0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
-000010b0: 6e74 5f6e 616d 6522 3a20 22e6 8891 e58f  nt_name": ".....
-000010c0: 91e4 ba86 38e5 bca0 e889 b2e5 9bbe 222c  ....8.........",
-000010d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000010e0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
-000010f0: 2022 e5a5 bde8 afb6 efbc 8138 e5bc a0e8   ".........8....
-00001100: 89b2 e59b beef bc81 efbc 883c 313e e68b  ...........<1>..
-00001110: bfe5 88b0 e4ba 8638 e5bc a0e8 89b2 e59b  .......8........
-00001120: beef bc8c e4b8 94e5 86b2 e8bf 87e5 a4b4  ................
-00001130: e699 95e4 ba86 38e5 9b9e e590 88ef bc89  ......8.........
-00001140: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00001150: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00001160: 2031 2c0a 2020 2020 2020 2020 2020 2020   1,.            
-00001170: 2020 2020 2020 2020 2276 6572 7469 676f          "vertigo
-00001180: 223a 2031 2c0a 2020 2020 2020 2020 2020  ": 1,.          
-00001190: 2020 2020 2020 2020 2020 2272 6f75 6e64            "round
-000011a0: 7322 3a20 382c 0a20 2020 2020 2020 2020  s": 8,.         
-000011b0: 2020 2020 2020 2020 2020 2022 6e61 6d65             "name
-000011c0: 223a 22e5 86b2 e8bf 87e5 a4b4 e4ba 8622  ":"............"
-000011d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000011e0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-000011f0: 2020 2020 2020 205d 2c0a 2020 2020 2020         ],.      
-00001200: 2020 2020 2020 2020 2020 5b39 302c 207b            [90, {
-00001210: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001220: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00001230: 223a 2022 e688 91e5 8f91 e4ba 8639 e5bc  ": ".........9..
-00001240: a0e8 89b2 e59b be22 2c0a 2020 2020 2020  .......",.      
-00001250: 2020 2020 2020 2020 2020 2020 2020 2264                "d
-00001260: 6573 6372 6962 6522 3a20 22e5 a5bd e8af  escribe": ".....
-00001270: b6ef bc81 39e5 bca0 e889 b2e5 9bbe efbc  ....9...........
-00001280: 81ef bc88 3c31 3ee6 8bbf e588 b0e4 ba86  ....<1>.........
-00001290: 39e5 bca0 e889 b2e5 9bbe efbc 8ce4 b894  9...............
-000012a0: e586 b2e8 bf87 e5a4 b4e6 9995 e4ba 8639  ...............9
-000012b0: e59b 9ee5 9088 efbc 8922 2c0a 2020 2020  .........",.    
+00000a90: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
+00000aa0: 22e6 8891 e58f 91e4 ba86 35e5 bca0 e889  ".........5.....
+00000ab0: b2e5 9bbe 222c 0a20 2020 2020 2020 2020  ....",.         
+00000ac0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
+00000ad0: 7269 6265 223a 22e5 a5bd e8af b6ef bc81  ribe":".........
+00000ae0: 35e5 bca0 e889 b2e5 9bbe efbc 81ef bc88  5...............
+00000af0: 3c31 3ee6 8bbf e588 b0e4 ba86 35e5 bca0  <1>.........5...
+00000b00: e889 b2e5 9bbe efbc 8ce4 b894 e4bd 93e5  ................
+00000b10: 8a9b e4b8 8de6 94af e699 95e4 ba86 35e5  ..............5.
+00000b20: 9b9e e590 88ef bc8c e4bd 86e4 bb96 e79a  ................
+00000b30: 84e5 85bd e680 a7e8 a2ab e5b0 8fe6 bf80  ................
+00000b40: e58f 91e4 ba86 efbc 8ce9 809f e5ba a6e6  ................
+00000b50: 9c80 e5a4 a7e5 8f98 e4b8 ba32 efbc 8922  ...........2..."
+00000b60: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00000b70: 2020 2020 2020 2274 6172 6765 7422 3a31        "target":1
+00000b80: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00000b90: 2020 2020 2020 2276 6572 7469 676f 223a        "vertigo":
+00000ba0: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
+00000bb0: 2020 2020 2020 2022 726f 756e 6473 223a         "rounds":
+00000bc0: 352c 0a20 2020 2020 2020 2020 2020 2020  5,.             
+00000bd0: 2020 2020 2020 2022 6d6f 7665 5f6d 6178         "move_max
+00000be0: 223a 322c 0a20 2020 2020 2020 2020 2020  ":2,.           
+00000bf0: 2020 2020 2020 2020 2022 6d6f 7665 5f6d           "move_m
+00000c00: 696e 223a 322c 0a20 2020 2020 2020 2020  in":2,.         
+00000c10: 2020 2020 2020 2020 2020 2022 6e61 6d65             "name
+00000c20: 223a 22e5 86b2 e699 95e4 ba86 e4bd 86e7  ":".............
+00000c30: 88bd 220a 2020 2020 2020 2020 2020 2020  ..".            
+00000c40: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
+00000c50: 2020 2020 2020 2020 2020 5d2c 0a20 2020            ],.   
+00000c60: 2020 2020 2020 2020 2020 2020 205b 3630               [60
+00000c70: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
+00000c80: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
+00000c90: 616d 6522 3a22 e688 91e5 8f91 e4ba 8636  ame":".........6
+00000ca0: e5bc a0e8 89b2 e59b be22 2c0a 2020 2020  .........",.    
+00000cb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000cc0: 2264 6573 6372 6962 6522 3a22 e5a5 bde8  "describe":"....
+00000cd0: afb6 efbc 8136 e5bc a0e8 89b2 e59b beef  .....6..........
+00000ce0: bc81 efbc 883c 313e e68b bfe5 88b0 e4ba  .....<1>........
+00000cf0: 8636 e5bc a0e8 89b2 e59b beef bc8c e4b8  .6..............
+00000d00: 94e4 bd93 e58a 9be4 b88d e694 afe6 9995  ................
+00000d10: e4ba 8636 e59b 9ee5 9088 efbc 8ce4 bd86  ...6............
+00000d20: e4bb 96e7 9a84 e585 bde6 80a7 e8a2 abe4  ................
+00000d30: b8ad e6bf 80e5 8f91 e4ba 86ef bc8c e980  ................
+00000d40: 9fe5 baa6 e69c 80e5 a4a7 e58f 98e4 b8ba  ................
+00000d50: 33ef bc89 222c 0a20 2020 2020 2020 2020  3...",.         
+00000d60: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+00000d70: 6574 223a 312c 0a20 2020 2020 2020 2020  et":1,.         
+00000d80: 2020 2020 2020 2020 2020 2022 7665 7274             "vert
+00000d90: 6967 6f22 3a31 2c0a 2020 2020 2020 2020  igo":1,.        
+00000da0: 2020 2020 2020 2020 2020 2020 2272 6f75              "rou
+00000db0: 6e64 7322 3a36 2c0a 2020 2020 2020 2020  nds":6,.        
+00000dc0: 2020 2020 2020 2020 2020 2020 226d 6f76              "mov
+00000dd0: 655f 6d61 7822 3a33 2c0a 2020 2020 2020  e_max":3,.      
+00000de0: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+00000df0: 6f76 655f 6d69 6e22 3a33 2c0a 2020 2020  ove_min":3,.    
+00000e00: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000e10: 226e 616d 6522 3a22 e586 b2e6 9995 e4ba  "name":"........
+00000e20: 86e4 bd86 e788 bd22 0a20 2020 2020 2020  .......".       
+00000e30: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
+00000e40: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
+00000e50: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00000e60: 2020 5b37 302c 207b 0a20 2020 2020 2020    [70, {.       
+00000e70: 2020 2020 2020 2020 2020 2020 2022 6576               "ev
+00000e80: 656e 745f 6e61 6d65 223a 22e6 8891 e58f  ent_name":".....
+00000e90: 91e4 ba86 37e5 bca0 e889 b2e5 9bbe 222c  ....7.........",
+00000ea0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00000eb0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00000ec0: 22e5 a5bd e8af b6ef bc81 37e5 bca0 e889  ".........7.....
+00000ed0: b2e5 9bbe efbc 81ef bc88 3c31 3ee6 8bbf  ..........<1>...
+00000ee0: e588 b0e4 ba86 37e5 bca0 e889 b2e5 9bbe  ......7.........
+00000ef0: efbc 8ce4 b894 e4bd 93e5 8a9b e4b8 8de6  ................
+00000f00: 94af e699 95e4 ba86 37e5 9b9e e590 88ef  ........7.......
+00000f10: bc8c e4bd 86e4 bb96 e79a 84e5 85bd e680  ................
+00000f20: a7e8 a2ab e5a4 a7e6 bf80 e58f 91e4 ba86  ................
+00000f30: efbc 8ce9 809f e5ba a6e6 9c80 e5a4 a7e5  ................
+00000f40: 8f98 e4b8 ba34 efbc 8922 2c0a 2020 2020  .....4...",.    
+00000f50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000f60: 2274 6172 6765 7422 3a31 2c0a 2020 2020  "target":1,.    
+00000f70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000f80: 2276 6572 7469 676f 223a 312c 0a20 2020  "vertigo":1,.   
+00000f90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000fa0: 2022 726f 756e 6473 223a 372c 0a20 2020   "rounds":7,.   
+00000fb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000fc0: 2022 6d6f 7665 5f6d 6178 223a 342c 0a20   "move_max":4,. 
+00000fd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000fe0: 2020 2022 6d6f 7665 5f6d 696e 223a 342c     "move_min":4,
+00000ff0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001000: 2020 2020 2022 6e61 6d65 223a 22e5 86b2       "name":"...
+00001010: e699 95e4 ba86 e4bd 86e7 88bd 220a 2020  ............".  
+00001020: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001030: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
+00001040: 2020 2020 5d2c 0a20 2020 2020 2020 2020      ],.         
+00001050: 2020 2020 2020 205b 3830 2c20 7b0a 2020         [80, {.  
+00001060: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001070: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00001080: e688 91e5 8f91 e4ba 8638 e5bc a0e8 89b2  .........8......
+00001090: e59b be22 2c0a 2020 2020 2020 2020 2020  ...",.          
+000010a0: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
+000010b0: 6962 6522 3a22 e5a5 bde8 afb6 efbc 8138  ibe":".........8
+000010c0: e5bc a0e8 89b2 e59b beef bc81 efbc 883c  ...............<
+000010d0: 313e e68b bfe5 88b0 e4ba 8638 e5bc a0e8  1>.........8....
+000010e0: 89b2 e59b beef bc8c e4b8 94e5 86b2 e8bf  ................
+000010f0: 87e5 a4b4 e699 95e4 ba86 38e5 9b9e e590  ..........8.....
+00001100: 88ef bc89 222c 0a20 2020 2020 2020 2020  ....",.         
+00001110: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+00001120: 6574 223a 312c 0a20 2020 2020 2020 2020  et":1,.         
+00001130: 2020 2020 2020 2020 2020 2022 7665 7274             "vert
+00001140: 6967 6f22 3a31 2c0a 2020 2020 2020 2020  igo":1,.        
+00001150: 2020 2020 2020 2020 2020 2020 2272 6f75              "rou
+00001160: 6e64 7322 3a38 2c0a 2020 2020 2020 2020  nds":8,.        
+00001170: 2020 2020 2020 2020 2020 2020 226e 616d              "nam
+00001180: 6522 3a22 e586 b2e8 bf87 e5a4 b4e4 ba86  e":"............
+00001190: 220a 2020 2020 2020 2020 2020 2020 2020  ".              
+000011a0: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
+000011b0: 2020 2020 2020 2020 5d2c 0a20 2020 2020          ],.     
+000011c0: 2020 2020 2020 2020 2020 205b 3930 2c20             [90, 
+000011d0: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
+000011e0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
+000011f0: 6522 3a22 e688 91e5 8f91 e4ba 8639 e5bc  e":".........9..
+00001200: a0e8 89b2 e59b be22 2c0a 2020 2020 2020  .......",.      
+00001210: 2020 2020 2020 2020 2020 2020 2020 2264                "d
+00001220: 6573 6372 6962 6522 3a22 e5a5 bde8 afb6  escribe":"......
+00001230: efbc 8139 e5bc a0e8 89b2 e59b beef bc81  ...9............
+00001240: efbc 883c 313e e68b bfe5 88b0 e4ba 8639  ...<1>.........9
+00001250: e5bc a0e8 89b2 e59b beef bc8c e4b8 94e5  ................
+00001260: 86b2 e8bf 87e5 a4b4 e699 95e4 ba86 39e5  ..............9.
+00001270: 9b9e e590 88ef bc89 222c 0a20 2020 2020  ........",.     
+00001280: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00001290: 7461 7267 6574 223a 312c 0a20 2020 2020  target":1,.     
+000012a0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+000012b0: 7665 7274 6967 6f22 3a31 2c0a 2020 2020  vertigo":1,.    
 000012c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012d0: 2274 6172 6765 7422 3a20 312c 0a20 2020  "target": 1,.   
+000012d0: 2272 6f75 6e64 7322 3a39 2c0a 2020 2020  "rounds":9,.    
 000012e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012f0: 2022 7665 7274 6967 6f22 3a20 312c 0a20   "vertigo": 1,. 
-00001300: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001310: 2020 2022 726f 756e 6473 223a 2039 2c0a     "rounds": 9,.
-00001320: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001330: 2020 2020 226e 616d 6522 3a22 e586 b2e8      "name":"....
-00001340: bf87 e5a4 b4e4 ba86 220a 2020 2020 2020  ........".      
-00001350: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
-00001360: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001370: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
-00001380: 2020 205b 3130 302c 207b 0a20 2020 2020     [100, {.     
-00001390: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-000013a0: 6576 656e 745f 6e61 6d65 223a 2022 e688  event_name": "..
-000013b0: 91e5 8f91 e4ba 8631 30e5 bca0 e889 b2e5  .......10.......
-000013c0: 9bbe 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-000013d0: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-000013e0: 6265 223a 2022 e5a5 bde8 afb6 efbc 8131  be": ".........1
-000013f0: 30e5 bca0 e889 b2e5 9bbe efbc 81ef bc88  0...............
-00001400: 3c31 3ee6 8bbf e588 b0e4 ba86 38e5 bca0  <1>.........8...
-00001410: e889 b2e5 9bbe efbc 8ce4 bb96 e586 b2e6  ................
-00001420: adbb e4ba 86ef bc89 222c 0a20 2020 2020  ........",.     
-00001430: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00001440: 7461 7267 6574 223a 2031 2c0a 2020 2020  target": 1,.    
-00001450: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001460: 2264 6965 223a 2031 2c0a 2020 2020 2020  "die": 1,.      
-00001470: 2020 2020 2020 2020 2020 2020 2020 226e                "n
-00001480: 616d 6522 3a22 e586 b2e6 adbb e4ba 8622  ame":"........."
-00001490: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000014a0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-000014b0: 2020 2020 2020 205d 0a20 2020 2020 2020         ].       
-000014c0: 2020 2020 2020 205d 0a0a 2020 2020 7d2c         ]..    },
-000014d0: 0a20 2020 207b 0a20 2020 2020 2020 2022  .    {.        "
-000014e0: 6576 656e 745f 6e61 6d65 223a 2022 e6ad  event_name": "..
-000014f0: bbe5 ae85 e79c 9fe6 81b6 e5bf 8322 2c0a  .............",.
-00001500: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-00001510: 6522 3a20 223c 303e 3a3c 313e e4bd a0e5  e": "<0>:<1>....
-00001520: 958a efbc 8ce5 9b9b e696 8be8 92b8 e9b9  ................
-00001530: 85e5 bf83 efbc 81ef bc88 e4b8 8ee7 9bae  ................
-00001540: e6a0 87e4 ba92 e68d a2e4 bd8d e7bd aeef  ................
-00001550: bc8c e589 8de8 bf9b 33e6 ada5 e5b9 b6e5  ........3.......
-00001560: 9ca8 e4b8 89e5 9b9e e590 88e4 b98b e590  ................
-00001570: 8ee6 8f90 e9ab 98e6 9c80 e5a4 a7e9 809f  ................
-00001580: 32e5 9b9e e590 88ef bc89 222c 0a20 2020  2.........",.   
-00001590: 2020 2020 2022 7461 7267 6574 223a 2031       "target": 1
-000015a0: 2c0a 2020 2020 2020 2020 2274 7261 636b  ,.        "track
-000015b0: 5f20 6578 6368 616e 6765 5f20 6c6f 6361  _ exchange_ loca
-000015c0: 7469 6f6e 223a 2031 2c0a 2020 2020 2020  tion": 1,.      
-000015d0: 2020 226d 6f76 6522 3a20 332c 0a20 2020    "move": 3,.   
-000015e0: 2020 2020 2022 6465 6c61 795f 6576 656e       "delay_even
-000015f0: 745f 7365 6c66 223a 5b33 2c7b 0a20 2020  t_self":[3,{.   
-00001600: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
-00001610: 6e61 6d65 223a 2022 e588 abe9 9da0 e8bf  name": "........
-00001620: 91e6 8891 efbc 8ce5 a4aa e681 b6e5 bf83  ................
-00001630: e4ba 8622 2c0a 2020 2020 2020 2020 2020  ...",.          
-00001640: 2020 2264 6573 6372 6962 6522 3a20 22ef    "describe": ".
-00001650: bc88 e68f 90e9 ab98 e69c 80e5 a4a7 e980  ................
-00001660: 9fe5 88b0 32e6 8896 33ef bc89 222c 0a20  ....2...3...",. 
-00001670: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-00001680: 6574 223a 2030 2c0a 2020 2020 2020 2020  et": 0,.        
-00001690: 2020 2020 2272 616e 646f 6d5f 6576 656e      "random_even
-000016a0: 745f 6f6e 6365 223a 205b 0a20 2020 2020  t_once": [.     
-000016b0: 2020 2020 2020 2020 2020 205b 3530 2c20             [50, 
-000016c0: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-000016d0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-000016e0: 6522 3a20 22e5 8f97 e4b8 8de4 ba86 efbc  e": "...........
-000016f0: 8c62 6c6f 636b e4ba 86ef bc81 222c 0a20  .block......",. 
-00001700: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001710: 2020 2022 6465 7363 7269 6265 223a 2022     "describe": "
-00001720: e5bf 83e9 878c e7a8 8de5 beae e58f 97e4  ................
-00001730: b88d e4ba 86ef bc8c e8b7 91e7 9a84 e7a8  ................
-00001740: 8de5 beae e5bf abe4 ba86 e5bf abe4 b880  ................
-00001750: e782 b9ef bc88 3c30 3ee6 9c80 e5a4 a7e9  ......<0>.......
-00001760: 809f e588 b032 efbc 8922 2c0a 2020 2020  .....2...",.    
-00001770: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001780: 2274 6172 6765 7422 3a20 302c 0a20 2020  "target": 0,.   
-00001790: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000017a0: 2022 6d6f 7665 5f6d 6178 223a 322c 0a20   "move_max":2,. 
-000017b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000017c0: 2020 2022 6d6f 7665 5f6d 696e 223a 322c     "move_min":2,
-000017d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000017e0: 2020 2020 2022 726f 756e 6473 223a 322c       "rounds":2,
-000017f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001800: 2020 2020 2022 6e61 6d65 223a 22e7 9c9f       "name":"...
-00001810: e9b9 85e5 bf83 2122 0a20 2020 2020 2020  ......!".       
-00001820: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
-00001830: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
-00001840: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00001850: 2020 5b31 3030 2c20 7b0a 2020 2020 2020    [100, {.      
-00001860: 2020 2020 2020 2020 2020 2020 2020 2265                "e
-00001870: 7665 6e74 5f6e 616d 6522 3a20 22e4 b88d  vent_name": "...
-00001880: e58a b3e7 83a6 e682 a8e8 b5b6 e688 91ef  ................
-00001890: bc8c e688 91e9 a9ac e4b8 8ae6 ba9c efbc  ................
-000018a0: 8122 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-000018b0: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-000018c0: 6522 3a20 22e4 baba e592 8ce9 a9ac e69c  e": "...........
-000018d0: 89e4 b880 e4b8 aae8 83bd e6b6 a6e5 b0b1  ................
-000018e0: e8a1 8ce4 ba86 efbc 883c 303e e69c 80e5  .........<0>....
-000018f0: a4a7 e980 9fe5 88b0 33ef bc89 222c 0a20  ........3...",. 
-00001900: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001910: 2020 2022 7461 7267 6574 223a 2030 2c0a     "target": 0,.
-00001920: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001930: 2020 2020 226d 6f76 655f 6d61 7822 3a33      "move_max":3
-00001940: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00001950: 2020 2020 2020 226d 6f76 655f 6d69 6e22        "move_min"
-00001960: 3a33 2c0a 2020 2020 2020 2020 2020 2020  :3,.            
-00001970: 2020 2020 2020 2020 2272 6f75 6e64 7322          "rounds"
-00001980: 3a32 2c0a 2020 2020 2020 2020 2020 2020  :2,.            
-00001990: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
-000019a0: e79c 9fe9 b985 e5bf 83ef bc81 efbc 8122  ..............."
-000019b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000019c0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-000019d0: 2020 2020 2020 205d 0a20 2020 2020 2020         ].       
-000019e0: 205d 0a20 2020 207d 5d0a 0a20 2020 207d   ].    }]..    }
-000019f0: 2c0a 2020 2020 7b0a 2020 2020 2020 2020  ,.    {.        
-00001a00: 2265 7665 6e74 5f6e 616d 6522 3a20 22e5  "event_name": ".
-00001a10: a4a7 e4bd ace5 8f88 e59c a8e8 afb4 e688  ................
-00001a20: 91e5 90ac e4b8 8de6 8782 e79a 84e4 b89c  ................
-00001a30: e8a5 bfe4 ba86 222c 0a20 2020 2020 2020  ......",.       
-00001a40: 2022 6465 7363 7269 6265 223a 2022 3c30   "describe": "<0
-00001a50: 3ee5 a4a7 e4bd ace5 8f88 e59c a8e8 afb4  >...............
-00001a60: e688 91e5 90ac e4b8 8de6 8782 e79a 84e4  ................
-00001a70: b89c e8a5 bfe4 ba86 efbc 88e5 bc80 e5a7  ................
-00001a80: 8be6 bd9c e6b0 b4ef bc8c e8bf 9be5 85a5  ................
-00001a90: e99a 90e8 baab e78a b6e6 8081 efbc 8ce5  ................
-00001aa0: b9b6 e88e b7e5 be97 e4b8 80e4 ba9b e5a5  ................
-00001ab0: 87e6 80aa e79a 8462 7566 66ef bc89 222c  .......buff...",
-00001ac0: 0a20 2020 2020 2020 2022 7461 7267 6574  .        "target
-00001ad0: 223a 2030 2c0a 2020 2020 2020 2020 2268  ": 0,.        "h
-00001ae0: 6964 696e 6722 3a20 312c 0a20 2020 2020  iding": 1,.     
-00001af0: 2020 2022 6e61 6d65 223a 22e6 bd9c e6b0     "name":".....
-00001b00: b4e4 b8ad 222c 0a20 2020 2020 2020 2022  ....",.        "
-00001b10: 6465 6c61 795f 6576 656e 745f 7365 6c66  delay_event_self
-00001b20: 223a 205b 332c 207b 0a20 2020 2020 2020  ": [3, {.       
-00001b30: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00001b40: 223a 2022 e699 bae6 85a7 e4b9 8be7 9cbc  ": "............
-00001b50: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
-00001b60: 6465 7363 7269 6265 223a 2022 3c30 3ee7  describe": "<0>.
-00001b70: 9a84 e699 bae6 85a7 e4b9 8be7 9cbc efbc  ................
-00001b80: 88e9 9a8f e69c bae7 9a84 6275 6666 efbc  ..........buff..
-00001b90: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00001ba0: 2274 6172 6765 7422 3a20 302c 0a20 2020  "target": 0,.   
-00001bb0: 2020 2020 2020 2020 2022 7261 6e64 6f6d           "random
-00001bc0: 5f65 7665 6e74 5f6f 6e63 6522 3a20 5b0a  _event_once": [.
-00001bd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001be0: 5b32 352c 207b 0a20 2020 2020 2020 2020  [25, {.         
-00001bf0: 2020 2020 2020 2020 2020 2022 6576 656e             "even
-00001c00: 745f 6e61 6d65 223a 2022 e4bd a0e4 bbac  t_name": "......
-00001c10: e59c a8e8 afb4 e4bb 80e4 b988 efbc 9f22  ..............."
-00001c20: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00001c30: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-00001c40: 3a20 223c 303e 3ae4 bda0 e4bb ace5 9ca8  : "<0>:.........
-00001c50: e8af b4e4 bb80 e4b9 88ef bc9f 222c 0a20  ............",. 
+000012f0: 226e 616d 6522 3a22 e586 b2e8 bf87 e5a4  "name":"........
+00001300: b4e4 ba86 220a 2020 2020 2020 2020 2020  ....".          
+00001310: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
+00001320: 2020 2020 2020 2020 2020 2020 5d2c 0a20              ],. 
+00001330: 2020 2020 2020 2020 2020 2020 2020 205b                 [
+00001340: 3130 302c 207b 0a20 2020 2020 2020 2020  100, {.         
+00001350: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+00001360: 745f 6e61 6d65 223a 22e6 8891 e58f 91e4  t_name":".......
+00001370: ba86 3130 e5bc a0e8 89b2 e59b be22 2c0a  ..10.........",.
+00001380: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001390: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+000013a0: e5a5 bde8 afb6 efbc 8131 30e5 bca0 e889  .........10.....
+000013b0: b2e5 9bbe efbc 81ef bc88 3c31 3ee6 8bbf  ..........<1>...
+000013c0: e588 b0e4 ba86 38e5 bca0 e889 b2e5 9bbe  ......8.........
+000013d0: efbc 8ce4 bb96 e586 b2e6 adbb e4ba 86ef  ................
+000013e0: bc89 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+000013f0: 2020 2020 2020 2020 2022 7461 7267 6574           "target
+00001400: 223a 312c 0a20 2020 2020 2020 2020 2020  ":1,.           
+00001410: 2020 2020 2020 2020 2022 6469 6522 3a31           "die":1
+00001420: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00001430: 2020 2020 2020 226e 616d 6522 3a22 e586        "name":"..
+00001440: b2e6 adbb e4ba 8622 0a20 2020 2020 2020  .......".       
+00001450: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
+00001460: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
+00001470: 0a20 2020 2020 2020 2020 2020 2020 205d  .              ]
+00001480: 0a0a 2020 2020 7d2c 0a20 2020 207b 0a20  ..    },.    {. 
+00001490: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+000014a0: 6d65 223a 22e6 adbb e5ae 85e7 9c9f e681  me":"...........
+000014b0: b6e5 bf83 222c 0a20 2020 2020 2020 2022  ....",.        "
+000014c0: 6465 7363 7269 6265 223a 223c 303e 3a3c  describe":"<0>:<
+000014d0: 313e e4bd a0e5 958a efbc 8ce5 9b9b e696  1>..............
+000014e0: 8be8 92b8 e9b9 85e5 bf83 efbc 81ef bc88  ................
+000014f0: e4b8 8ee7 9bae e6a0 87e4 ba92 e68d a2e4  ................
+00001500: bd8d e7bd aeef bc8c e589 8de8 bf9b 33e6  ..............3.
+00001510: ada5 e5b9 b6e5 9ca8 e4b8 89e5 9b9e e590  ................
+00001520: 88e4 b98b e590 8ee6 8f90 e9ab 98e6 9c80  ................
+00001530: e5a4 a7e9 809f 32e5 9b9e e590 88ef bc89  ......2.........
+00001540: 222c 0a20 2020 2020 2020 2022 7461 7267  ",.        "targ
+00001550: 6574 223a 312c 0a20 2020 2020 2020 2022  et":1,.        "
+00001560: 7472 6163 6b5f 2065 7863 6861 6e67 655f  track_ exchange_
+00001570: 206c 6f63 6174 696f 6e22 3a31 2c0a 2020   location":1,.  
+00001580: 2020 2020 2020 226d 6f76 6522 3a33 2c0a        "move":3,.
+00001590: 2020 2020 2020 2020 2264 656c 6179 5f65          "delay_e
+000015a0: 7665 6e74 5f73 656c 6622 3a5b 332c 7b0a  vent_self":[3,{.
+000015b0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+000015c0: 6e74 5f6e 616d 6522 3a22 e588 abe9 9da0  nt_name":"......
+000015d0: e8bf 91e6 8891 efbc 8ce5 a4aa e681 b6e5  ................
+000015e0: bf83 e4ba 8622 2c0a 2020 2020 2020 2020  .....",.        
+000015f0: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00001600: efbc 88e6 8f90 e9ab 98e6 9c80 e5a4 a7e9  ................
+00001610: 809f e588 b032 e688 9633 efbc 8922 2c0a  .....2...3...",.
+00001620: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
+00001630: 6765 7422 3a30 2c0a 2020 2020 2020 2020  get":0,.        
+00001640: 2020 2020 2272 616e 646f 6d5f 6576 656e      "random_even
+00001650: 745f 6f6e 6365 223a 5b0a 2020 2020 2020  t_once":[.      
+00001660: 2020 2020 2020 2020 2020 5b35 302c 207b            [50, {
+00001670: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001680: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00001690: 223a 22e5 8f97 e4b8 8de4 ba86 efbc 8c62  ":"............b
+000016a0: 6c6f 636b e4ba 86ef bc81 222c 0a20 2020  lock......",.   
+000016b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000016c0: 2022 6465 7363 7269 6265 223a 22e5 bf83   "describe":"...
+000016d0: e987 8ce7 a88d e5be aee5 8f97 e4b8 8de4  ................
+000016e0: ba86 efbc 8ce8 b791 e79a 84e7 a88d e5be  ................
+000016f0: aee5 bfab e4ba 86e5 bfab e4b8 80e7 82b9  ................
+00001700: efbc 883c 303e e69c 80e5 a4a7 e980 9fe5  ...<0>..........
+00001710: 88b0 32ef bc89 222c 0a20 2020 2020 2020  ..2...",.       
+00001720: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
+00001730: 7267 6574 223a 302c 0a20 2020 2020 2020  rget":0,.       
+00001740: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
+00001750: 7665 5f6d 6178 223a 322c 0a20 2020 2020  ve_max":2,.     
+00001760: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00001770: 6d6f 7665 5f6d 696e 223a 322c 0a20 2020  move_min":2,.   
+00001780: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001790: 2022 726f 756e 6473 223a 322c 0a20 2020   "rounds":2,.   
+000017a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000017b0: 2022 6e61 6d65 223a 22e7 9c9f e9b9 85e5   "name":".......
+000017c0: bf83 2122 0a20 2020 2020 2020 2020 2020  ..!".           
+000017d0: 2020 2020 2020 2020 207d 0a20 2020 2020           }.     
+000017e0: 2020 2020 2020 2020 2020 205d 2c0a 2020             ],.  
+000017f0: 2020 2020 2020 2020 2020 2020 2020 5b31                [1
+00001800: 3030 2c20 7b0a 2020 2020 2020 2020 2020  00, {.          
+00001810: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
+00001820: 5f6e 616d 6522 3a22 e4b8 8de5 8ab3 e783  _name":"........
+00001830: a6e6 82a8 e8b5 b6e6 8891 efbc 8ce6 8891  ................
+00001840: e9a9 ace4 b88a e6ba 9cef bc81 222c 0a20  ............",. 
+00001850: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001860: 2020 2022 6465 7363 7269 6265 223a 22e4     "describe":".
+00001870: baba e592 8ce9 a9ac e69c 89e4 b880 e4b8  ................
+00001880: aae8 83bd e6b6 a6e5 b0b1 e8a1 8ce4 ba86  ................
+00001890: efbc 883c 303e e69c 80e5 a4a7 e980 9fe5  ...<0>..........
+000018a0: 88b0 33ef bc89 222c 0a20 2020 2020 2020  ..3...",.       
+000018b0: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
+000018c0: 7267 6574 223a 302c 0a20 2020 2020 2020  rget":0,.       
+000018d0: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
+000018e0: 7665 5f6d 6178 223a 332c 0a20 2020 2020  ve_max":3,.     
+000018f0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00001900: 6d6f 7665 5f6d 696e 223a 332c 0a20 2020  move_min":3,.   
+00001910: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001920: 2022 726f 756e 6473 223a 322c 0a20 2020   "rounds":2,.   
+00001930: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001940: 2022 6e61 6d65 223a 22e7 9c9f e9b9 85e5   "name":".......
+00001950: bf83 efbc 81ef bc81 220a 2020 2020 2020  ........".      
+00001960: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
+00001970: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001980: 5d0a 2020 2020 2020 2020 5d0a 2020 2020  ].        ].    
+00001990: 7d5d 0a0a 2020 2020 7d2c 0a20 2020 207b  }]..    },.    {
+000019a0: 0a20 2020 2020 2020 2022 6576 656e 745f  .        "event_
+000019b0: 6e61 6d65 223a 22e5 a4a7 e4bd ace5 8f88  name":".........
+000019c0: e59c a8e8 afb4 e688 91e5 90ac e4b8 8de6  ................
+000019d0: 8782 e79a 84e4 b89c e8a5 bfe4 ba86 222c  ..............",
+000019e0: 0a20 2020 2020 2020 2022 6465 7363 7269  .        "descri
+000019f0: 6265 223a 223c 303e e5a4 a7e4 bdac e58f  be":"<0>........
+00001a00: 88e5 9ca8 e8af b4e6 8891 e590 ace4 b88d  ................
+00001a10: e687 82e7 9a84 e4b8 9ce8 a5bf e4ba 86ef  ................
+00001a20: bc88 e5bc 80e5 a78b e6bd 9ce6 b0b4 efbc  ................
+00001a30: 8ce8 bf9b e585 a5e9 9a90 e8ba abe7 8ab6  ................
+00001a40: e680 81ef bc8c e5b9 b6e8 8eb7 e5be 97e4  ................
+00001a50: b880 e4ba 9be5 a587 e680 aae7 9a84 6275  ..............bu
+00001a60: 6666 efbc 8922 2c0a 2020 2020 2020 2020  ff...",.        
+00001a70: 2274 6172 6765 7422 3a30 2c0a 2020 2020  "target":0,.    
+00001a80: 2020 2020 2268 6964 696e 6722 3a31 2c0a      "hiding":1,.
+00001a90: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+00001aa0: e6bd 9ce6 b0b4 e4b8 ad22 2c0a 2020 2020  .........",.    
+00001ab0: 2020 2020 2264 656c 6179 5f65 7665 6e74      "delay_event
+00001ac0: 5f73 656c 6622 3a5b 332c 207b 0a20 2020  _self":[3, {.   
+00001ad0: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
+00001ae0: 6e61 6d65 223a 22e6 99ba e685 a7e4 b98b  name":".........
+00001af0: e79c bc22 2c0a 2020 2020 2020 2020 2020  ...",.          
+00001b00: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+00001b10: 3ee7 9a84 e699 bae6 85a7 e4b9 8be7 9cbc  >...............
+00001b20: efbc 88e9 9a8f e69c bae7 9a84 6275 6666  ............buff
+00001b30: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00001b40: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+00001b50: 2020 2020 2020 2020 2020 2272 616e 646f            "rando
+00001b60: 6d5f 6576 656e 745f 6f6e 6365 223a 5b0a  m_event_once":[.
+00001b70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001b80: 5b32 352c 207b 0a20 2020 2020 2020 2020  [25, {.         
+00001b90: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+00001ba0: 745f 6e61 6d65 223a 22e4 bda0 e4bb ace5  t_name":".......
+00001bb0: 9ca8 e8af b4e4 bb80 e4b9 88ef bc9f 222c  ..............",
+00001bc0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001bd0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00001be0: 223c 303e 3ae4 bda0 e4bb ace5 9ca8 e8af  "<0>:...........
+00001bf0: b4e4 bb80 e4b9 88ef bc9f 222c 0a20 2020  ..........",.   
+00001c00: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001c10: 2022 7461 7267 6574 223a 302c 0a20 2020   "target":0,.   
+00001c20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001c30: 2022 7665 7274 6967 6f22 3a31 2c0a 2020   "vertigo":1,.  
+00001c40: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001c50: 2020 2272 6f75 6e64 7322 3a35 2c0a 2020    "rounds":5,.  
 00001c60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001c70: 2020 2022 7461 7267 6574 223a 2030 2c0a     "target": 0,.
+00001c70: 2020 226e 616d 6522 3a22 3f22 0a20 2020    "name":"?".   
 00001c80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001c90: 2020 2020 2276 6572 7469 676f 223a 2031      "vertigo": 1
-00001ca0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00001cb0: 2020 2020 2020 2272 6f75 6e64 7322 3a20        "rounds": 
-00001cc0: 352c 0a20 2020 2020 2020 2020 2020 2020  5,.             
-00001cd0: 2020 2020 2020 2022 6e61 6d65 223a 223f         "name":"?
-00001ce0: 220a 2020 2020 2020 2020 2020 2020 2020  ".              
-00001cf0: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
-00001d00: 2020 2020 2020 2020 5d2c 0a20 2020 2020          ],.     
-00001d10: 2020 2020 2020 2020 2020 205b 3530 2c20             [50, 
-00001d20: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-00001d30: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-00001d40: 6522 3a20 22e6 8891 e697 a0e6 b395 e790  e": "...........
-00001d50: 86e8 a7a3 222c 0a20 2020 2020 2020 2020  ....",.         
-00001d60: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-00001d70: 7269 6265 223a 2022 3c30 3e3a e688 91e6  ribe": "<0>:....
-00001d80: 97a0 e6b3 95e7 9086 e8a7 a322 2c0a 2020  ...........",.  
-00001d90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001da0: 2020 2274 6172 6765 7422 3a20 302c 0a20    "target": 0,. 
-00001db0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001dc0: 2020 2022 6469 6522 203a 3120 2020 2020     "die" :1     
-00001dd0: 2020 2020 2020 2020 2020 2020 200a 2020               .  
-00001de0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001df0: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-00001e00: 2020 2020 5d2c 0a20 2020 2020 2020 2020      ],.         
-00001e10: 2020 2020 2020 205b 3735 2c20 7b0a 2020         [75, {.  
-00001e20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001e30: 2020 2265 7665 6e74 5f6e 616d 6522 3a20    "event_name": 
-00001e40: 22e6 8891 e592 8ce5 a4a7 e4bd ace4 b98b  "...............
-00001e50: e997 b4ef bc8c e58f aae6 9c89 e4ba bfe7  ................
-00001e60: 82b9 e8b7 9de7 a6bb 222c 0a20 2020 2020  ........",.     
-00001e70: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00001e80: 6465 7363 7269 6265 223a 2022 3c30 3e3a  describe": "<0>:
-00001e90: e688 91e5 928c e5a4 a7e4 bdac e4b9 8be9  ................
-00001ea0: 97b4 efbc 8ce5 8faa e69c 89e4 babf e782  ................
-00001eb0: b9e8 b79d e7a6 bb22 2c0a 2020 2020 2020  .......",.      
-00001ec0: 2020 2020 2020 2020 2020 2020 2020 2274                "t
-00001ed0: 6172 6765 7422 3a20 302c 0a20 2020 2020  arget": 0,.     
-00001ee0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00001ef0: 6d6f 7665 223a 2d31 3030 0a20 2020 2020  move":-100.     
-00001f00: 2020 2020 2020 2020 2020 2020 2020 207d                 }
-00001f10: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001f20: 205d 2c0a 2020 2020 2020 2020 2020 2020   ],.            
-00001f30: 2020 2020 5b31 3030 2c20 7b0a 2020 2020      [100, {.    
-00001f40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001f50: 2265 7665 6e74 5f6e 616d 6522 3a20 22e6  "event_name": ".
-00001f60: 8891 e8a7 89e5 be97 e688 91e4 bba5 e590  ................
-00001f70: 8ee4 bc9a e79c 8be5 be97 e687 8222 2c0a  .............",.
-00001f80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001f90: 2020 2020 2264 6573 6372 6962 6522 3a20      "describe": 
-00001fa0: 223c 303e 3ae6 8891 e8a7 89e5 be97 e688  "<0>:...........
-00001fb0: 91e4 bba5 e590 8ee4 bc9a e79c 8be5 be97  ................
-00001fc0: e687 8222 2c0a 2020 2020 2020 2020 2020  ...",.          
-00001fd0: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
-00001fe0: 7422 3a20 302c 0a20 2020 2020 2020 2020  t": 0,.         
-00001ff0: 2020 2020 2020 2020 2020 2022 7665 7274             "vert
-00002000: 6967 6f22 3a20 312c 0a20 2020 2020 2020  igo": 1,.       
-00002010: 2020 2020 2020 2020 2020 2020 2022 726f               "ro
-00002020: 756e 6473 223a 2032 2c0a 2020 2020 2020  unds": 2,.      
-00002030: 2020 2020 2020 2020 2020 2020 2020 226d                "m
-00002040: 6f76 6522 3a2d 3130 2c0a 2020 2020 2020  ove":-10,.      
-00002050: 2020 2020 2020 2020 2020 2020 2020 226e                "n
-00002060: 616d 6522 3a22 3f22 0a20 2020 2020 2020  ame":"?".       
-00002070: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
-00002080: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
-00002090: 0a20 2020 2020 2020 2020 2020 2020 205d  .              ]
-000020a0: 0a20 2020 2020 2020 207d 5d0a 2020 2020  .        }].    
-000020b0: 0a20 2020 2020 2020 200a 0a20 2020 207d  .        ..    }
-000020c0: 2c0a 2020 2020 2020 2020 7b0a 2020 2020  ,.        {.    
-000020d0: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-000020e0: 3a20 22e6 b182 e6b6 a9e6 b6a9 222c 0a20  : ".........",. 
-000020f0: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00002100: 2030 2c0a 2020 2020 2020 2020 2264 6573   0,.        "des
-00002110: 6372 6962 6522 3a22 3c30 3e3a e587 a0e7  cribe":"<0>:....
-00002120: 82b9 e4ba 86ef bc8c e8bf 98e4 b88d e58f  ................
-00002130: 91e8 89b2 e59b beef bc88 e6b1 82e5 8f96  ................
-00002140: 312d 33e5 bca0 e889 b2e5 9bbe efbc 8ce5  1-3.............
-00002150: b9b6 e88e b7e5 be97 e79b b8e5 ba94 e79a  ................
-00002160: 84e4 bd8d e7a7 bbef bc89 222c 0a20 2020  ..........",.   
-00002170: 2020 2020 2022 7261 6e64 6f6d 5f65 7665       "random_eve
-00002180: 6e74 5f6f 6e63 6522 3a20 5b0a 2020 2020  nt_once": [.    
-00002190: 2020 2020 2020 2020 5b33 332c 207b 0a20          [33, {. 
-000021a0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-000021b0: 6576 656e 745f 6e61 6d65 223a 2022 e4b8  event_name": "..
-000021c0: 80e5 bca0 222c 0a20 2020 2020 2020 2020  ....",.         
-000021d0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-000021e0: 223a 2022 3c30 3eef bc9a e6b1 82e6 b182  ": "<0>.........
-000021f0: e595 a6ef bc81 e69d a5e4 b880 e5bc a0e5  ................
-00002200: 90a7 efbc 81ef bc88 e586 b2e4 b880 e6ad  ................
-00002210: a5ef bc89 222c 0a20 2020 2020 2020 2020  ....",.         
-00002220: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00002230: 2030 2c0a 2020 2020 2020 2020 2020 2020   0,.            
-00002240: 2020 2020 226d 6f76 6522 3a20 312c 0a20      "move": 1,. 
-00002250: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00002260: 6e61 6d65 223a 22e5 86b2 efbc 8122 0a20  name":"......". 
-00002270: 2020 2020 2020 2020 2020 2020 2020 207d                 }
-00002280: 0a20 2020 2020 2020 2020 2020 205d 2c0a  .            ],.
-00002290: 2020 2020 2020 2020 2020 2020 5b36 372c              [67,
-000022a0: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-000022b0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-000022c0: 2022 e4b8 a4e5 bca0 222c 0a20 2020 2020   "......",.     
-000022d0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-000022e0: 7269 6265 223a 2022 3c30 3eef bc9a e6b1  ribe": "<0>.....
-000022f0: 82e6 b182 e595 a6ef bc81 e69d a5e4 b8a4  ................
-00002300: e5bc a0e5 90a7 efbc 81ef bc88 e586 b2e4  ................
-00002310: b8a4 e6ad a5ef bc89 222c 0a20 2020 2020  ........",.     
-00002320: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-00002330: 6574 223a 2030 2c0a 2020 2020 2020 2020  et": 0,.        
-00002340: 2020 2020 2020 2020 226d 6f76 6522 3a20          "move": 
-00002350: 322c 0a20 2020 2020 2020 2020 2020 2020  2,.             
-00002360: 2020 2022 6e61 6d65 223a 22e5 86b2 efbc     "name":".....
-00002370: 81ef bc81 220a 2020 2020 2020 2020 2020  ....".          
-00002380: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-00002390: 5d2c 0a20 2020 2020 2020 2020 2020 205b  ],.            [
-000023a0: 3130 302c 207b 0a20 2020 2020 2020 2020  100, {.         
-000023b0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-000023c0: 6d65 223a 2022 e4b8 89e5 bca0 222c 0a20  me": "......",. 
-000023d0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-000023e0: 6465 7363 7269 6265 223a 2022 3c30 3eef  describe": "<0>.
-000023f0: bc9a e6b1 82e6 b182 e595 a6ef bc81 e69d  ................
-00002400: a5e4 b889 e5bc a0e5 90a7 efbc 81ef bc88  ................
-00002410: e586 b2e4 b889 e6ad a5ef bc89 222c 0a20  ............",. 
-00002420: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00002430: 7461 7267 6574 223a 2030 2c0a 2020 2020  target": 0,.    
-00002440: 2020 2020 2020 2020 2020 2020 226d 6f76              "mov
-00002450: 6522 3a20 332c 0a20 2020 2020 2020 2020  e": 3,.         
-00002460: 2020 2020 2020 2022 6e61 6d65 223a 22e5         "name":".
-00002470: 86b2 efbc 81ef bc81 efbc 8122 0a20 2020  ...........".   
-00002480: 2020 2020 2020 2020 207d 0a20 2020 2020           }.     
-00002490: 2020 2020 2020 205d 0a20 2020 2020 2020         ].       
-000024a0: 2020 205d 0a20 2020 2020 2020 207d 2c0a     ].        },.
-000024b0: 2020 2020 2020 2020 7b0a 2020 2020 2020          {.      
-000024c0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-000024d0: 6522 3a20 22e5 98bf e598 bfe2 80a6 e280  e": "...........
-000024e0: a6e6 8891 e8a6 81e5 bc80 e5a7 8be5 8f91  ................
-000024f0: e799 abe4 ba86 efbc 8122 2c0a 2020 2020  .........",.    
-00002500: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-00002510: 6522 3a20 223c 303e efbc 9ae5 98bf e598  e": "<0>........
-00002520: bfe2 80a6 e280 a6e7 bea4 e4b8 bbe2 80a6  ................
-00002530: e280 a6e7 bea4 e4b8 bbe7 9a84 e5b0 8f6a  ...............j
-00002540: 696f 6a69 6fe2 80a6 e280 a6e5 98bf e598  iojio...........
-00002550: bfef bc88 e887 aae5 b7b1 e6ad a2e6 ada5  ................
-00002560: e4ba 8ee6 ada4 33e5 9b9e e590 88ef bc8c  ......3.........
-00002570: e5b9 b6e5 9ca8 e4b8 8be5 9b9e e590 88e8  ................
-00002580: b5b6 e8b7 91e5 85b6 e4bb 96e4 baba e590  ................
-00002590: 91e5 898d 34e6 ada5 efbc 8922 2c0a 2020  ....4......",.  
-000025a0: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
-000025b0: 7422 3a20 302c 0a20 2020 2020 2020 2020  t": 0,.         
-000025c0: 2020 2022 6c6f 6361 7465 5f6c 6f63 6b22     "locate_lock"
-000025d0: 3a20 312c 0a20 2020 2020 2020 2020 2020  : 1,.           
-000025e0: 2022 726f 756e 6473 223a 332c 0a20 2020   "rounds":3,.   
-000025f0: 2020 2020 2020 2020 2022 6e61 6d65 223a           "name":
-00002600: 22e5 8f91 e799 abe4 b8ad 222c 0a20 2020  ".........",.   
-00002610: 2020 2020 2020 2020 2022 6465 6c61 795f           "delay_
-00002620: 6576 656e 745f 7365 6c66 223a 205b 322c  event_self": [2,
-00002630: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-00002640: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-00002650: 2022 e598 bfe5 98bf e280 a6e2 80a6 e688   "..............
-00002660: 91e8 a681 e5bc 80e5 a78b e58f 91e7 99ab  ................
-00002670: e4ba 86ef bc81 222c 0a20 2020 2020 2020  ......",.       
-00002680: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-00002690: 6265 223a 223c 303e e5bf 8de4 b88d e4bd  be":"<0>........
-000026a0: 8fe4 ba86 efbc 81e8 a681 e58f 91e7 99ab  ................
-000026b0: e4ba 86ef bc81 efbc 81ef bc88 e8b5 b6e8  ................
-000026c0: b791 e585 b6e4 bb96 e4ba bae5 9091 e589  ................
-000026d0: 8d34 e6ad a5ef bc89 222c 0a20 2020 2020  .4......",.     
-000026e0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-000026f0: 6574 223a 2033 2c0a 2020 2020 2020 2020  et": 3,.        
-00002700: 2020 2020 2020 2020 226d 6f76 6522 3a34          "move":4
-00002710: 0a20 2020 2020 2020 2020 2020 207d 5d0a  .            }].
-00002720: 0a20 2020 2020 2020 200a 2020 2020 2020  .        .      
-00002730: 2020 2020 2020 0a20 2020 200a 2020 2020        .    .    
-00002740: 2020 2020 7d2c 0a20 2020 2020 2020 207b      },.        {
-00002750: 0a20 2020 2020 2020 2020 2020 2022 6576  .            "ev
-00002760: 656e 745f 6e61 6d65 223a 2022 e5be 88e6  ent_name": "....
-00002770: 8ab1 e6ad 89ef bc8c e8bf 99e9 878c e4b8  ................
-00002780: 8de6 aca2 e8bf 8ee4 bda0 222c 0a20 2020  ..........",.   
-00002790: 2020 2020 2020 2020 2022 7461 7267 6574           "target
-000027a0: 223a 2034 2c0a 2020 2020 2020 2020 2020  ": 4,.          
-000027b0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
-000027c0: 3e3a e5be 88e6 8ab1 e6ad 89ef bc8c e8bf  >:..............
-000027d0: 99e9 878c e4b8 8de6 aca2 e8bf 8ee4 bda0  ................
-000027e0: efbc 88e5 b086 3c31 3ee8 b8a2 e587 bae8  ......<1>.......
-000027f0: b59b e981 93ef bc89 222c 0a20 2020 2020  ........",.     
-00002800: 2020 2020 2020 2022 6177 6179 223a 2031         "away": 1
-00002810: 2c0a 2020 2020 2020 2020 2020 2020 226e  ,.            "n
-00002820: 616d 6522 3a22 e682 a8e5 b7b2 e8a2 abe8  ame":"..........
-00002830: b8a2 e587 bae7 bea4 e881 8a22 0a20 2020  ...........".   
-00002840: 2020 2020 207d 2c0a 2020 2020 2020 2020       },.        
-00002850: 7b0a 2020 2020 2020 2020 2020 2020 2265  {.            "e
-00002860: 7665 6e74 5f6e 616d 6522 3a20 22e9 82a3  vent_name": "...
-00002870: e698 afe5 9cba e8af afe4 bc9a 222c 0a20  ............",. 
-00002880: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-00002890: 6574 223a 2032 2c0a 2020 2020 2020 2020  et": 2,.        
-000028a0: 2020 2020 2274 6172 6765 745f 6973 5f62      "target_is_b
-000028b0: 7566 6622 3a20 2261 7761 7922 2c0a 2020  uff": "away",.  
-000028c0: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
-000028d0: 6962 6522 3a22 3c30 3e3a e4b9 8be5 898d  ibe":"<0>:......
-000028e0: e68a 8a3c 313e e8b8 a2e5 87ba e58e bbe6  ...<1>..........
-000028f0: 98af e59c bae8 afaf e4bc 9aef bc88 e6b6  ................
-00002900: 88e9 99a4 e7a6 bbe5 bc80 6275 6666 efbc  ..........buff..
-00002910: 8ce4 b88d e8bf 87e7 9bae e6a0 87e4 bc9a  ................
-00002920: e8b8 b9e4 b880 e4b8 aae4 baba 35e6 ada5  ............5...
-00002930: e4bb a5e7 a4ba e695 ace6 848f efbc 8922  ..............."
-00002940: 2c0a 2020 2020 2020 2020 2020 2020 2264  ,.            "d
-00002950: 656c 5f62 7566 6622 3a20 22e6 82a8 e5b7  el_buff": ".....
-00002960: b2e8 a2ab e8b8 a2e5 87ba e7be a4e8 818a  ................
-00002970: 2220 2c0a 2020 2020 2020 2020 2020 2020  " ,.            
-00002980: 2261 6e6f 7468 6572 5f65 7665 6e74 223a  "another_event":
-00002990: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-000029a0: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-000029b0: 2022 e688 91e4 b88d e8a7 89e5 be97 222c   "............",
-000029c0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000029d0: 2022 6465 7363 7269 6265 223a 223c 303e   "describe":"<0>
-000029e0: 3ae6 8891 e58f afe4 b88d e8a7 89e5 be97  :...............
-000029f0: efbc 88e8 b8b9 e4b8 80e4 b8aa e4ba ba35  ...............5
-00002a00: e6ad a5e4 bba5 e7a4 bae6 95ac e684 8fef  ................
-00002a10: bc89 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00002a20: 2020 2020 2022 7461 7267 6574 223a 2031       "target": 1
-00002a30: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00002a40: 2020 226d 6f76 6522 3a2d 350a 2020 2020    "move":-5.    
-00002a50: 2020 2020 2020 2020 7d20 0a20 2020 2020          } .     
-00002a60: 2020 207d 2c0a 2020 2020 2020 2020 7b0a     },.        {.
-00002a70: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
-00002a80: 6e74 5f6e 616d 6522 3a20 22e6 aca2 e8bf  nt_name": ".....
-00002a90: 8ee6 96b0 e688 90e5 9198 222c 0a20 2020  ..........",.   
-00002aa0: 2020 2020 2020 2020 2022 7461 7267 6574           "target
-00002ab0: 223a 2030 2c0a 2020 2020 2020 2020 2020  ": 0,.          
-00002ac0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
-00002ad0: 3e3a e6ac a2e8 bf8e e696 b0e6 8890 e591  >:..............
-00002ae0: 98e5 85a5 e7be a4ef bc8c e585 b6e5 ae9e  ................
-00002af0: e698 afe5 b08f e58f b7ef bc88 e5b0 86e4  ................
-00002b00: b880 e58c b9e6 96b0 e9a9 ace5 8aa0 e585  ................
-00002b10: a5e6 af94 e8b5 9be5 b9b6 e69b bfe6 8da2  ................
-00002b20: e58e 9fe9 a9ac efbc 8922 2c0a 2020 2020  .........",.    
-00002b30: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
-00002b40: e5b0 8fe5 8fb7 222c 0a20 2020 2020 2020  ......",.       
-00002b50: 2020 2020 2022 7261 6e64 6f6d 5f65 7665       "random_eve
-00002b60: 6e74 5f6f 6e63 6522 3a20 5b0a 2020 2020  nt_once": [.    
-00002b70: 2020 2020 2020 2020 2020 2020 5b31 302c              [10,
-00002b80: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
-00002b90: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00002ba0: 6d65 223a 2022 e4ba bae6 b4bb e79d 80e5  me": "..........
-00002bb0: b0b1 e698 afe4 b8ba e4ba 86e6 a8b1 e5b2  ................
-00002bc0: 9be9 babb e8a1 a322 2c0a 2020 2020 2020  .......",.      
-00002bd0: 2020 2020 2020 2020 2020 2020 2020 2264                "d
-00002be0: 6573 6372 6962 6522 3a20 22e4 baba e6b4  escribe": ".....
-00002bf0: bbe7 9d80 e5b0 b1e6 98af e4b8 bae4 ba86  ................
-00002c00: e6a8 b1e5 b29b e9ba bbe8 a1a3 e280 94e2  ................
-00002c10: 8094 e58a a0e5 85a5 e4ba 86e6 af94 e8b5  ................
-00002c20: 9bef bc88 e4b8 8ee4 b880 e590 8de9 9a8f  ................
-00002c30: e69c bae7 9bae e6a0 87e6 8da2 e4bd 8def  ................
-00002c40: bc8c e69c 89e5 8faf e883 bde4 bc9a e587  ................
-00002c50: bbe6 9d80 e58f a6e4 b880 e79b aee6 a087  ................
-00002c60: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
-00002c70: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
-00002c80: 7422 3a20 302c 0a20 2020 2020 2020 2020  t": 0,.         
-00002c90: 2020 2020 2020 2020 2020 2022 6164 645f             "add_
-00002ca0: 686f 7273 6522 3a20 7b22 686f 7273 656e  horse": {"horsen
-00002cb0: 616d 6522 3a20 22e4 baba e6b4 bbe7 9d80  ame": ".........
-00002cc0: e5b0 b1e6 98af e4b8 bae4 ba86 e6a8 b1e5  ................
-00002cd0: b29b e9ba bbe8 a1a3 222c 2022 7569 6422  ........", "uid"
-00002ce0: 3a20 312c 2022 6f77 6e65 7222 3a20 22e5  : 1, "owner": ".
-00002cf0: b08f e58f b722 2c20 226c 6f63 6174 696f  .....", "locatio
-00002d00: 6e22 3a20 3120 7d2c 0a20 2020 2020 2020  n": 1 },.       
-00002d10: 2020 2020 2020 2020 2020 2020 2022 616e               "an
-00002d20: 6f74 6865 725f 6576 656e 745f 7365 6c66  other_event_self
-00002d30: 223a 207b 0a20 2020 2020 2020 2020 2020  ": {.           
-00002d40: 2020 2020 2020 2020 2020 2020 2022 6576               "ev
-00002d50: 656e 745f 6e61 6d65 223a 2022 e68d a2e4  ent_name": "....
-00002d60: bd8d 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00002d70: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
-00002d80: 7267 6574 223a 2034 2c0a 2020 2020 2020  rget": 4,.      
-00002d90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002da0: 2020 2264 6573 6372 6962 6522 3a22 e4b8    "describe":"..
-00002db0: bae4 ba86 e6a8 b1e5 b29b e9ba bbe8 a1a3  ................
-00002dc0: efbc 81ef bc81 efbc 88e6 8da2 e4bd 8def  ................
-00002dd0: bc89 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00002de0: 2020 2020 2020 2020 2020 2020 2022 7472               "tr
-00002df0: 6163 6b5f 6578 6368 616e 6765 5f6c 6f63  ack_exchange_loc
-00002e00: 6174 696f 6e22 3a20 312c 0a20 2020 2020  ation": 1,.     
-00002e10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002e20: 2020 2022 7261 6e64 6f6d 5f65 7665 6e74     "random_event
-00002e30: 5f6f 6e63 6522 3a5b 0a20 2020 2020 2020  _once":[.       
-00002e40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002e50: 2020 2020 205b 3530 2c7b 0a20 2020 2020       [50,{.     
-00002e60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002e70: 2020 2020 2020 2020 2020 2022 6576 656e             "even
-00002e80: 745f 6e61 6d65 223a 2022 e587 bbe6 9d80  t_name": "......
-00002e90: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00001c90: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
+00001ca0: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
+00001cb0: 2020 2020 2020 5b35 302c 207b 0a20 2020        [50, {.   
+00001cc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001cd0: 2022 6576 656e 745f 6e61 6d65 223a 22e6   "event_name":".
+00001ce0: 8891 e697 a0e6 b395 e790 86e8 a7a3 222c  ..............",
+00001cf0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001d00: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00001d10: 223c 303e 3ae6 8891 e697 a0e6 b395 e790  "<0>:...........
+00001d20: 86e8 a7a3 222c 0a20 2020 2020 2020 2020  ....",.         
+00001d30: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
+00001d40: 6574 223a 302c 0a20 2020 2020 2020 2020  et":0,.         
+00001d50: 2020 2020 2020 2020 2020 2022 6469 6522             "die"
+00001d60: 203a 3120 2020 2020 2020 2020 2020 2020   :1             
+00001d70: 2020 2020 200a 2020 2020 2020 2020 2020       .          
+00001d80: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
+00001d90: 2020 2020 2020 2020 2020 2020 5d2c 0a20              ],. 
+00001da0: 2020 2020 2020 2020 2020 2020 2020 205b                 [
+00001db0: 3735 2c20 7b0a 2020 2020 2020 2020 2020  75, {.          
+00001dc0: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
+00001dd0: 5f6e 616d 6522 3a22 e688 91e5 928c e5a4  _name":"........
+00001de0: a7e4 bdac e4b9 8be9 97b4 efbc 8ce5 8faa  ................
+00001df0: e69c 89e4 babf e782 b9e8 b79d e7a6 bb22  ..............."
+00001e00: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00001e10: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
+00001e20: 3a22 3c30 3e3a e688 91e5 928c e5a4 a7e4  :"<0>:..........
+00001e30: bdac e4b9 8be9 97b4 efbc 8ce5 8faa e69c  ................
+00001e40: 89e4 babf e782 b9e8 b79d e7a6 bb22 2c0a  .............",.
+00001e50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001e60: 2020 2020 2274 6172 6765 7422 3a30 2c0a      "target":0,.
+00001e70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001e80: 2020 2020 226d 6f76 6522 3a2d 3130 300a      "move":-100.
+00001e90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001ea0: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
+00001eb0: 2020 2020 2020 5d2c 0a20 2020 2020 2020        ],.       
+00001ec0: 2020 2020 2020 2020 205b 3130 302c 207b           [100, {
+00001ed0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001ee0: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00001ef0: 223a 22e6 8891 e8a7 89e5 be97 e688 91e4  ":".............
+00001f00: bba5 e590 8ee4 bc9a e79c 8be5 be97 e687  ................
+00001f10: 8222 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00001f20: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
+00001f30: 6522 3a22 3c30 3e3a e688 91e8 a789 e5be  e":"<0>:........
+00001f40: 97e6 8891 e4bb a5e5 908e e4bc 9ae7 9c8b  ................
+00001f50: e5be 97e6 8782 222c 0a20 2020 2020 2020  ......",.       
+00001f60: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
+00001f70: 7267 6574 223a 302c 0a20 2020 2020 2020  rget":0,.       
+00001f80: 2020 2020 2020 2020 2020 2020 2022 7665               "ve
+00001f90: 7274 6967 6f22 3a31 2c0a 2020 2020 2020  rtigo":1,.      
+00001fa0: 2020 2020 2020 2020 2020 2020 2020 2272                "r
+00001fb0: 6f75 6e64 7322 3a32 2c0a 2020 2020 2020  ounds":2,.      
+00001fc0: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+00001fd0: 6f76 6522 3a2d 3130 2c0a 2020 2020 2020  ove":-10,.      
+00001fe0: 2020 2020 2020 2020 2020 2020 2020 226e                "n
+00001ff0: 616d 6522 3a22 3f22 0a20 2020 2020 2020  ame":"?".       
+00002000: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
+00002010: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
+00002020: 0a20 2020 2020 2020 2020 2020 2020 205d  .              ]
+00002030: 0a20 2020 2020 2020 207d 5d0a 2020 2020  .        }].    
+00002040: 0a20 2020 2020 2020 200a 0a20 2020 207d  .        ..    }
+00002050: 2c0a 2020 2020 2020 2020 7b0a 2020 2020  ,.        {.    
+00002060: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+00002070: 3a22 e6b1 82e6 b6a9 e6b6 a922 2c0a 2020  :".........",.  
+00002080: 2020 2020 2020 2274 6172 6765 7422 3a30        "target":0
+00002090: 2c0a 2020 2020 2020 2020 2264 6573 6372  ,.        "descr
+000020a0: 6962 6522 3a22 3c30 3e3a e587 a0e7 82b9  ibe":"<0>:......
+000020b0: e4ba 86ef bc8c e8bf 98e4 b88d e58f 91e8  ................
+000020c0: 89b2 e59b beef bc88 e6b1 82e5 8f96 312d  ..............1-
+000020d0: 33e5 bca0 e889 b2e5 9bbe efbc 8ce5 b9b6  3...............
+000020e0: e88e b7e5 be97 e79b b8e5 ba94 e79a 84e4  ................
+000020f0: bd8d e7a7 bbef bc89 222c 0a20 2020 2020  ........",.     
+00002100: 2020 2022 7261 6e64 6f6d 5f65 7665 6e74     "random_event
+00002110: 5f6f 6e63 6522 3a5b 0a20 2020 2020 2020  _once":[.       
+00002120: 2020 2020 205b 3333 2c20 7b0a 2020 2020       [33, {.    
+00002130: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00002140: 6e74 5f6e 616d 6522 3a22 e4b8 80e5 bca0  nt_name":"......
+00002150: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00002160: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00002170: 303e efbc 9ae6 b182 e6b1 82e5 95a6 efbc  0>..............
+00002180: 81e6 9da5 e4b8 80e5 bca0 e590 a7ef bc81  ................
+00002190: efbc 88e5 86b2 e4b8 80e6 ada5 efbc 8922  ..............."
+000021a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000021b0: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+000021c0: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+000021d0: 6f76 6522 3a31 2c0a 2020 2020 2020 2020  ove":1,.        
+000021e0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+000021f0: e586 b2ef bc81 220a 2020 2020 2020 2020  ......".        
+00002200: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
+00002210: 2020 2020 2020 5d2c 0a20 2020 2020 2020        ],.       
+00002220: 2020 2020 205b 3637 2c20 7b0a 2020 2020       [67, {.    
+00002230: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00002240: 6e74 5f6e 616d 6522 3a22 e4b8 a4e5 bca0  nt_name":"......
+00002250: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00002260: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00002270: 303e efbc 9ae6 b182 e6b1 82e5 95a6 efbc  0>..............
+00002280: 81e6 9da5 e4b8 a4e5 bca0 e590 a7ef bc81  ................
+00002290: efbc 88e5 86b2 e4b8 a4e6 ada5 efbc 8922  ..............."
+000022a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000022b0: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+000022c0: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+000022d0: 6f76 6522 3a32 2c0a 2020 2020 2020 2020  ove":2,.        
+000022e0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+000022f0: e586 b2ef bc81 efbc 8122 0a20 2020 2020  .........".     
+00002300: 2020 2020 2020 207d 0a20 2020 2020 2020         }.       
+00002310: 2020 2020 205d 2c0a 2020 2020 2020 2020       ],.        
+00002320: 2020 2020 5b31 3030 2c20 7b0a 2020 2020      [100, {.    
+00002330: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00002340: 6e74 5f6e 616d 6522 3a22 e4b8 89e5 bca0  nt_name":"......
+00002350: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00002360: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+00002370: 303e efbc 9ae6 b182 e6b1 82e5 95a6 efbc  0>..............
+00002380: 81e6 9da5 e4b8 89e5 bca0 e590 a7ef bc81  ................
+00002390: efbc 88e5 86b2 e4b8 89e6 ada5 efbc 8922  ..............."
+000023a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000023b0: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+000023c0: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+000023d0: 6f76 6522 3a33 2c0a 2020 2020 2020 2020  ove":3,.        
+000023e0: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+000023f0: e586 b2ef bc81 efbc 81ef bc81 220a 2020  ............".  
+00002400: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
+00002410: 2020 2020 2020 2020 5d0a 2020 2020 2020          ].      
+00002420: 2020 2020 5d0a 2020 2020 2020 2020 7d2c      ].        },
+00002430: 0a20 2020 2020 2020 207b 0a20 2020 2020  .        {.     
+00002440: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+00002450: 6d65 223a 22e5 98bf e598 bfe2 80a6 e280  me":"...........
+00002460: a6e6 8891 e8a6 81e5 bc80 e5a7 8be5 8f91  ................
+00002470: e799 abe4 ba86 efbc 8122 2c0a 2020 2020  .........",.    
+00002480: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
+00002490: 6522 3a22 3c30 3eef bc9a e598 bfe5 98bf  e":"<0>.........
+000024a0: e280 a6e2 80a6 e7be a4e4 b8bb e280 a6e2  ................
+000024b0: 80a6 e7be a4e4 b8bb e79a 84e5 b08f 6a69  ..............ji
+000024c0: 6f6a 696f e280 a6e2 80a6 e598 bfe5 98bf  ojio............
+000024d0: efbc 88e8 87aa e5b7 b1e6 ada2 e6ad a5e4  ................
+000024e0: ba8e e6ad a433 e59b 9ee5 9088 efbc 8ce5  .....3..........
+000024f0: b9b6 e59c a8e4 b88b e59b 9ee5 9088 e8b5  ................
+00002500: b6e8 b791 e585 b6e4 bb96 e4ba bae5 9091  ................
+00002510: e589 8d34 e6ad a5ef bc89 222c 0a20 2020  ...4......",.   
+00002520: 2020 2020 2020 2020 2022 7461 7267 6574           "target
+00002530: 223a 302c 0a20 2020 2020 2020 2020 2020  ":0,.           
+00002540: 2022 6c6f 6361 7465 5f6c 6f63 6b22 3a31   "locate_lock":1
+00002550: 2c0a 2020 2020 2020 2020 2020 2020 2272  ,.            "r
+00002560: 6f75 6e64 7322 3a33 2c0a 2020 2020 2020  ounds":3,.      
+00002570: 2020 2020 2020 226e 616d 6522 3a22 e58f        "name":"..
+00002580: 91e7 99ab e4b8 ad22 2c0a 2020 2020 2020  .......",.      
+00002590: 2020 2020 2020 2264 656c 6179 5f65 7665        "delay_eve
+000025a0: 6e74 5f73 656c 6622 3a5b 322c 207b 0a20  nt_self":[2, {. 
+000025b0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+000025c0: 6576 656e 745f 6e61 6d65 223a 22e5 98bf  event_name":"...
+000025d0: e598 bfe2 80a6 e280 a6e6 8891 e8a6 81e5  ................
+000025e0: bc80 e5a7 8be5 8f91 e799 abe4 ba86 efbc  ................
+000025f0: 8122 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00002600: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00002610: 3c30 3ee5 bf8d e4b8 8de4 bd8f e4ba 86ef  <0>.............
+00002620: bc81 e8a6 81e5 8f91 e799 abe4 ba86 efbc  ................
+00002630: 81ef bc81 efbc 88e8 b5b6 e8b7 91e5 85b6  ................
+00002640: e4bb 96e4 baba e590 91e5 898d 34e6 ada5  ............4...
+00002650: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00002660: 2020 2020 2020 2274 6172 6765 7422 3a33        "target":3
+00002670: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00002680: 2020 226d 6f76 6522 3a34 0a20 2020 2020    "move":4.     
+00002690: 2020 2020 2020 207d 5d0a 0a20 2020 2020         }]..     
+000026a0: 2020 200a 2020 2020 2020 2020 2020 2020     .            
+000026b0: 0a20 2020 200a 2020 2020 2020 2020 7d2c  .    .        },
+000026c0: 0a20 2020 2020 2020 207b 0a20 2020 2020  .        {.     
+000026d0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+000026e0: 6d65 223a 22e5 be88 e68a b1e6 ad89 efbc  me":"...........
+000026f0: 8ce8 bf99 e987 8ce4 b88d e6ac a2e8 bf8e  ................
+00002700: e4bd a022 2c0a 2020 2020 2020 2020 2020  ...",.          
+00002710: 2020 2274 6172 6765 7422 3a34 2c0a 2020    "target":4,.  
+00002720: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
+00002730: 6962 6522 3a22 3c30 3e3a e5be 88e6 8ab1  ibe":"<0>:......
+00002740: e6ad 89ef bc8c e8bf 99e9 878c e4b8 8de6  ................
+00002750: aca2 e8bf 8ee4 bda0 efbc 88e5 b086 3c31  ..............<1
+00002760: 3ee8 b8a2 e587 bae8 b59b e981 93ef bc89  >...............
+00002770: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
+00002780: 6177 6179 223a 312c 0a20 2020 2020 2020  away":1,.       
+00002790: 2020 2020 2022 6e61 6d65 223a 22e6 82a8       "name":"...
+000027a0: e5b7 b2e8 a2ab e8b8 a2e5 87ba e7be a4e8  ................
+000027b0: 818a 220a 2020 2020 2020 2020 7d2c 0a20  ..".        },. 
+000027c0: 2020 2020 2020 207b 0a20 2020 2020 2020         {.       
+000027d0: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+000027e0: 223a 22e9 82a3 e698 afe5 9cba e8af afe4  ":".............
+000027f0: bc9a 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00002800: 2022 7461 7267 6574 223a 322c 0a20 2020   "target":2,.   
+00002810: 2020 2020 2020 2020 2022 7461 7267 6574           "target
+00002820: 5f69 735f 6275 6666 223a 2261 7761 7922  _is_buff":"away"
+00002830: 2c0a 2020 2020 2020 2020 2020 2020 2264  ,.            "d
+00002840: 6573 6372 6962 6522 3a22 3c30 3e3a e4b9  escribe":"<0>:..
+00002850: 8be5 898d e68a 8a3c 313e e8b8 a2e5 87ba  .......<1>......
+00002860: e58e bbe6 98af e59c bae8 afaf e4bc 9aef  ................
+00002870: bc88 e6b6 88e9 99a4 e7a6 bbe5 bc80 6275  ..............bu
+00002880: 6666 efbc 8ce4 b88d e8bf 87e7 9bae e6a0  ff..............
+00002890: 87e4 bc9a e8b8 b9e4 b880 e4b8 aae4 baba  ................
+000028a0: 35e6 ada5 e4bb a5e7 a4ba e695 ace6 848f  5...............
+000028b0: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+000028c0: 2020 2264 656c 5f62 7566 6622 3a22 e682    "del_buff":"..
+000028d0: a8e5 b7b2 e8a2 abe8 b8a2 e587 bae7 bea4  ................
+000028e0: e881 8a22 202c 0a20 2020 2020 2020 2020  ..." ,.         
+000028f0: 2020 2022 616e 6f74 6865 725f 6576 656e     "another_even
+00002900: 7422 3a7b 0a20 2020 2020 2020 2020 2020  t":{.           
+00002910: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00002920: 223a 22e6 8891 e4b8 8de8 a789 e5be 9722  ":"............"
+00002930: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00002940: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+00002950: 3e3a e688 91e5 8faf e4b8 8de8 a789 e5be  >:..............
+00002960: 97ef bc88 e8b8 b9e4 b880 e4b8 aae4 baba  ................
+00002970: 35e6 ada5 e4bb a5e7 a4ba e695 ace6 848f  5...............
+00002980: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00002990: 2020 2020 2020 2274 6172 6765 7422 3a31        "target":1
+000029a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000029b0: 2020 226d 6f76 6522 3a2d 350a 2020 2020    "move":-5.    
+000029c0: 2020 2020 2020 2020 7d20 0a20 2020 2020          } .     
+000029d0: 2020 207d 2c0a 2020 2020 2020 2020 7b0a     },.        {.
+000029e0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+000029f0: 6e74 5f6e 616d 6522 3a22 e6ac a2e8 bf8e  nt_name":"......
+00002a00: e696 b0e6 8890 e591 9822 2c0a 2020 2020  .........",.    
+00002a10: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
+00002a20: 3a30 2c0a 2020 2020 2020 2020 2020 2020  :0,.            
+00002a30: 2264 6573 6372 6962 6522 3a22 3c30 3e3a  "describe":"<0>:
+00002a40: e6ac a2e8 bf8e e696 b0e6 8890 e591 98e5  ................
+00002a50: 85a5 e7be a4ef bc8c e585 b6e5 ae9e e698  ................
+00002a60: afe5 b08f e58f b7ef bc88 e5b0 86e4 b880  ................
+00002a70: e58c b9e6 96b0 e9a9 ace5 8aa0 e585 a5e6  ................
+00002a80: af94 e8b5 9be5 b9b6 e69b bfe6 8da2 e58e  ................
+00002a90: 9fe9 a9ac efbc 8922 2c0a 2020 2020 2020  .......",.      
+00002aa0: 2020 2020 2020 226e 616d 6522 3a22 e5b0        "name":"..
+00002ab0: 8fe5 8fb7 222c 0a20 2020 2020 2020 2020  ....",.         
+00002ac0: 2020 2022 7261 6e64 6f6d 5f65 7665 6e74     "random_event
+00002ad0: 5f6f 6e63 6522 3a5b 0a20 2020 2020 2020  _once":[.       
+00002ae0: 2020 2020 2020 2020 205b 3130 2c20 7b0a           [10, {.
+00002af0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002b00: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+00002b10: 3a22 e4ba bae6 b4bb e79d 80e5 b0b1 e698  :"..............
+00002b20: afe4 b8ba e4ba 86e6 a8b1 e5b2 9be9 babb  ................
+00002b30: e8a1 a322 2c0a 2020 2020 2020 2020 2020  ...",.          
+00002b40: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
+00002b50: 6962 6522 3a22 e4ba bae6 b4bb e79d 80e5  ibe":"..........
+00002b60: b0b1 e698 afe4 b8ba e4ba 86e6 a8b1 e5b2  ................
+00002b70: 9be9 babb e8a1 a3e2 8094 e280 94e5 8aa0  ................
+00002b80: e585 a5e4 ba86 e6af 94e8 b59b efbc 88e4  ................
+00002b90: b88e e4b8 80e5 908d e99a 8fe6 9cba e79b  ................
+00002ba0: aee6 a087 e68d a2e4 bd8d efbc 8ce6 9c89  ................
+00002bb0: e58f afe8 83bd e4bc 9ae5 87bb e69d 80e5  ................
+00002bc0: 8fa6 e4b8 80e7 9bae e6a0 87ef bc89 222c  ..............",
+00002bd0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00002be0: 2020 2020 2022 7461 7267 6574 223a 302c       "target":0,
+00002bf0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00002c00: 2020 2020 2022 6164 645f 686f 7273 6522       "add_horse"
+00002c10: 3a7b 2268 6f72 7365 6e61 6d65 223a 22e4  :{"horsename":".
+00002c20: baba e6b4 bbe7 9d80 e5b0 b1e6 98af e4b8  ................
+00002c30: bae4 ba86 e6a8 b1e5 b29b e9ba bbe8 a1a3  ................
+00002c40: 222c 2022 7569 6422 3a31 2c20 226f 776e  ", "uid":1, "own
+00002c50: 6572 223a 22e5 b08f e58f b722 2c20 226c  er":"......", "l
+00002c60: 6f63 6174 696f 6e22 3a31 207d 2c0a 2020  ocation":1 },.  
+00002c70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002c80: 2020 2261 6e6f 7468 6572 5f65 7665 6e74    "another_event
+00002c90: 5f73 656c 6622 3a7b 0a20 2020 2020 2020  _self":{.       
+00002ca0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002cb0: 2022 6576 656e 745f 6e61 6d65 223a 22e6   "event_name":".
+00002cc0: 8da2 e4bd 8d22 2c0a 2020 2020 2020 2020  .....",.        
+00002cd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002ce0: 2274 6172 6765 7422 3a34 2c0a 2020 2020  "target":4,.    
+00002cf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002d00: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00002d10: e4b8 bae4 ba86 e6a8 b1e5 b29b e9ba bbe8  ................
+00002d20: a1a3 efbc 81ef bc81 efbc 88e6 8da2 e4bd  ................
+00002d30: 8def bc89 222c 0a20 2020 2020 2020 2020  ....",.         
+00002d40: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00002d50: 7472 6163 6b5f 6578 6368 616e 6765 5f6c  track_exchange_l
+00002d60: 6f63 6174 696f 6e22 3a31 2c0a 2020 2020  ocation":1,.    
+00002d70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002d80: 2020 2020 2272 616e 646f 6d5f 6576 656e      "random_even
+00002d90: 745f 6f6e 6365 223a 5b0a 2020 2020 2020  t_once":[.      
+00002da0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002db0: 2020 2020 2020 5b35 302c 7b0a 2020 2020        [50,{.    
+00002dc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002dd0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00002de0: 6e74 5f6e 616d 6522 3a22 e587 bbe6 9d80  nt_name":"......
+00002df0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00002e00: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002e10: 2020 2022 7461 7267 6574 223a 322c 0a20     "target":2,. 
+00002e20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002e30: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00002e40: 6465 7363 7269 6265 223a 223c 313e e587  describe":"<1>..
+00002e50: bbe6 9d80 e4ba 86e6 a8b1 e5b2 9be9 babb  ................
+00002e60: e8a1 a32c e6ad bbe5 90a7 222c 0a20 2020  ...,......",.   
+00002e70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002e80: 2020 2020 2020 2020 2020 2020 2022 6469               "di
+00002e90: 6522 3a31 0a20 2020 2020 2020 2020 2020  e":1.           
 00002ea0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002eb0: 2020 2022 7461 7267 6574 223a 2032 2c0a     "target": 2,.
+00002eb0: 207d 5d2c 0a20 2020 2020 2020 2020 2020   }],.           
 00002ec0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002ed0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002ee0: 2264 6573 6372 6962 6522 3a22 3c31 3ee5  "describe":"<1>.
-00002ef0: 87bb e69d 80e4 ba86 e6a8 b1e5 b29b e9ba  ................
-00002f00: bbe8 a1a3 2ce6 adbb e590 a722 2c0a 2020  ....,......",.  
-00002f10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002f20: 2020 2020 2020 2020 2020 2020 2020 2264                "d
-00002f30: 6965 223a 310a 2020 2020 2020 2020 2020  ie":1.          
-00002f40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002f50: 2020 7d5d 2c0a 2020 2020 2020 2020 2020    }],.          
-00002f60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002f70: 2020 5b31 3030 2c7b 0a20 2020 2020 2020    [100,{.       
+00002ed0: 205b 3130 302c 7b0a 2020 2020 2020 2020   [100,{.        
+00002ee0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002ef0: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
+00002f00: 616d 6522 3a22 e697 a0e4 ba8b e58f 91e7  ame":"..........
+00002f10: 949f 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00002f20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002f30: 2020 2020 2022 7461 7267 6574 223a 322c       "target":2,
+00002f40: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00002f50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002f60: 2022 6465 7363 7269 6265 223a 22e6 97a0   "describe":"...
+00002f70: e4ba 8be5 8f91 e794 9f22 0a20 2020 2020  .........".     
 00002f80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002f90: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
-00002fa0: 6e61 6d65 223a 2022 e697 a0e4 ba8b e58f  name": "........
-00002fb0: 91e7 949f 222c 0a20 2020 2020 2020 2020  ....",.         
-00002fc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002fd0: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00002fe0: 2032 2c0a 2020 2020 2020 2020 2020 2020   2,.            
-00002ff0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003000: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-00003010: e697 a0e4 ba8b e58f 91e7 949f 220a 2020  ............".  
-00003020: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003030: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
-00003040: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003050: 2020 2020 2020 2020 5d0a 2020 2020 2020          ].      
-00003060: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003070: 2020 5d0a 2020 2020 2020 2020 2020 2020    ].            
-00003080: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
-00003090: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
-000030a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000030b0: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
-000030c0: 2020 205b 3230 2c20 7b0a 2020 2020 2020     [20, {.      
-000030d0: 2020 2020 2020 2020 2020 2020 2020 2265                "e
-000030e0: 7665 6e74 5f6e 616d 6522 3a20 22e4 b880  vent_name": "...
-000030f0: e5b9 b6e8 b685 efbc 81e8 8a9c e6b9 96e8  ................
-00003100: b5b7 e9a3 9eef bc81 222c 0a20 2020 2020  ........",.     
-00003110: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00003120: 6465 7363 7269 6265 223a 2022 e4b8 80e5  describe": "....
+00002f90: 2020 2020 2020 207d 0a20 2020 2020 2020         }.       
+00002fa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002fb0: 2020 2020 205d 0a20 2020 2020 2020 2020       ].         
+00002fc0: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
+00002fd0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00002fe0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
+00002ff0: 2020 2020 2020 2020 2020 207d 0a20 2020             }.   
+00003000: 2020 2020 2020 2020 2020 2020 205d 2c0a               ],.
+00003010: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003020: 5b32 302c 207b 0a20 2020 2020 2020 2020  [20, {.         
+00003030: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+00003040: 745f 6e61 6d65 223a 22e4 b880 e5b9 b6e8  t_name":".......
+00003050: b685 efbc 81e8 8a9c e6b9 96e8 b5b7 e9a3  ................
+00003060: 9eef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
+00003070: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
+00003080: 7269 6265 223a 22e4 b880 e5b9 b6e8 b685  ribe":".........
+00003090: efbc 81e8 8a9c e6b9 96e8 b5b7 e9a3 9eef  ................
+000030a0: bc81 e280 94e2 8094 e58a a0e5 85a5 e4ba  ................
+000030b0: 86e6 af94 e8b5 9bef bc88 e69c 8931 3025  .............10%
+000030c0: e79a 84e6 a682 e78e 87e8 b5b7 e9a3 9ee5  ................
+000030d0: 88b0 e7bb 88e7 82b9 efbc 8922 2c0a 2020  ...........",.  
+000030e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000030f0: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+00003100: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003110: 2020 2261 6464 5f68 6f72 7365 223a 7b22    "add_horse":{"
+00003120: 686f 7273 656e 616d 6522 3a22 e4b8 80e5  horsename":"....
 00003130: b9b6 e8b6 85ef bc81 e88a 9ce6 b996 e8b5  ................
-00003140: b7e9 a39e efbc 81e2 8094 e280 94e5 8aa0  ................
-00003150: e585 a5e4 ba86 e6af 94e8 b59b efbc 88e6  ................
-00003160: 9c89 3130 25e7 9a84 e6a6 82e7 8e87 e8b5  ..10%...........
-00003170: b7e9 a39e e588 b0e7 bb88 e782 b9ef bc89  ................
-00003180: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00003190: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-000031a0: 2030 2c0a 2020 2020 2020 2020 2020 2020   0,.            
-000031b0: 2020 2020 2020 2020 2261 6464 5f68 6f72          "add_hor
-000031c0: 7365 223a 207b 2268 6f72 7365 6e61 6d65  se": {"horsename
-000031d0: 223a 2022 e4b8 80e5 b9b6 e8b6 85ef bc81  ": "............
-000031e0: e88a 9ce6 b996 e8b5 b7e9 a39e efbc 8122  ..............."
-000031f0: 2c20 2275 6964 223a 2032 2c20 226f 776e  , "uid": 2, "own
-00003200: 6572 223a 2022 e5b0 8fe5 8fb7 222c 2022  er": "......", "
-00003210: 6c6f 6361 7469 6f6e 223a 2031 207d 2c0a  location": 1 },.
+00003140: b7e9 a39e efbc 8122 2c20 2275 6964 223a  .......", "uid":
+00003150: 322c 2022 6f77 6e65 7222 3a22 e5b0 8fe5  2, "owner":"....
+00003160: 8fb7 222c 2022 6c6f 6361 7469 6f6e 223a  ..", "location":
+00003170: 3120 7d2c 0a20 2020 2020 2020 2020 2020  1 },.           
+00003180: 2020 2020 2020 2020 2022 7261 6e64 6f6d           "random
+00003190: 5f65 7665 6e74 5f6f 6e63 6522 3a5b 0a20  _event_once":[. 
+000031a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000031b0: 2020 2020 2020 205b 3130 2c7b 0a20 2020         [10,{.   
+000031c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000031d0: 2020 2020 2020 2020 2022 6576 656e 745f           "event_
+000031e0: 6e61 6d65 223a 22e8 b5b7 e9a3 9eef bc81  name":".........
+000031f0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00003200: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00003210: 7461 7267 6574 223a 302c 0a20 2020 2020  target":0,.     
 00003220: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003230: 2020 2020 2272 616e 646f 6d5f 6576 656e      "random_even
-00003240: 745f 6f6e 6365 223a 5b0a 2020 2020 2020  t_once":[.      
-00003250: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003260: 2020 5b31 302c 7b0a 2020 2020 2020 2020    [10,{.        
-00003270: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003280: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-00003290: 3a20 22e8 b5b7 e9a3 9eef bc81 222c 0a20  : ".........",. 
+00003230: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
+00003240: 223a 223c 303e e5b1 85e7 84b6 e8b5 b7e9  ":"<0>..........
+00003250: a39e e4ba 8622 2c0a 2020 2020 2020 2020  .....",.        
+00003260: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003270: 2020 2020 226d 6f76 6522 3a31 3030 0a20      "move":100. 
+00003280: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003290: 2020 2020 2020 207d 5d2c 0a20 2020 2020         }],.     
 000032a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000032b0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-000032c0: 6574 223a 2030 2c0a 2020 2020 2020 2020  et": 0,.        
-000032d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000032e0: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-000032f0: 3c30 3ee5 b185 e784 b6e8 b5b7 e9a3 9ee4  <0>.............
-00003300: ba86 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00003310: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003320: 2022 6d6f 7665 223a 3130 300a 2020 2020   "move":100.    
-00003330: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003340: 2020 2020 7d5d 2c0a 2020 2020 2020 2020      }],.        
-00003350: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003360: 5b31 3030 2c7b 0a20 2020 2020 2020 2020  [100,{.         
+000032b0: 2020 205b 3130 302c 7b0a 2020 2020 2020     [100,{.      
+000032c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000032d0: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
+000032e0: 6522 3a22 e697 a0e4 ba8b e58f 91e7 949f  e":"............
+000032f0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+00003300: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00003310: 7461 7267 6574 223a 302c 0a20 2020 2020  target":0,.     
+00003320: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003330: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
+00003340: 223a 22e6 97a0 e4ba 8be5 8f91 e794 9f22  ":"............"
+00003350: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003360: 2020 2020 2020 2020 207d 0a20 2020 2020           }.     
 00003370: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003380: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-00003390: 2022 e697 a0e4 ba8b e58f 91e7 949f 222c   "............",
-000033a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000033b0: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
-000033c0: 7267 6574 223a 2030 2c0a 2020 2020 2020  rget": 0,.      
-000033d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000033e0: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-000033f0: 3a22 e697 a0e4 ba8b e58f 91e7 949f 220a  :"............".
-00003400: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003410: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
-00003420: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003430: 2020 5d0a 2020 2020 2020 2020 2020 2020    ].            
-00003440: 2020 2020 2020 2020 5d0a 2020 2020 2020          ].      
-00003450: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
-00003460: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003470: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
-00003480: 2020 205b 3330 2c20 7b0a 2020 2020 2020     [30, {.      
-00003490: 2020 2020 2020 2020 2020 2020 2020 2265                "e
-000034a0: 7665 6e74 5f6e 616d 6522 3a20 22e4 ba8c  vent_name": "...
-000034b0: e890 a5e9 95bf e79a 84e6 848f e5a4 a7e5  ................
-000034c0: 88a9 e782 ae22 2c0a 2020 2020 2020 2020  .....",.        
-000034d0: 2020 2020 2020 2020 2020 2020 2264 6573              "des
-000034e0: 6372 6962 6522 3a20 22e4 ba8c e890 a5e9  cribe": ".......
-000034f0: 95bf e79a 84e6 848f e5a4 a7e5 88a9 e782  ................
-00003500: aee2 8094 e280 94e5 8aa0 e585 a5e4 ba86  ................
-00003510: e6af 94e8 b59b efbc 8831 3025 e587 bbe6  .........10%....
-00003520: 9d80 32e5 908d e79b aee6 a087 efbc 8922  ..2............"
-00003530: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00003540: 2020 2020 2020 2274 6172 6765 7422 3a20        "target": 
-00003550: 302c 0a20 2020 2020 2020 2020 2020 2020  0,.             
-00003560: 2020 2020 2020 2022 6164 645f 686f 7273         "add_hors
-00003570: 6522 3a20 7b22 686f 7273 656e 616d 6522  e": {"horsename"
-00003580: 3a20 22e4 ba8c e890 a5e9 95bf e79a 84e6  : ".............
-00003590: 848f e5a4 a7e5 88a9 e782 ae22 2c20 2275  ...........", "u
-000035a0: 6964 223a 2033 2c20 226f 776e 6572 223a  id": 3, "owner":
-000035b0: 2022 e5b0 8fe5 8fb7 222c 2022 6c6f 6361   "......", "loca
-000035c0: 7469 6f6e 223a 2031 207d 2c0a 2020 2020  tion": 1 },.    
-000035d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000035e0: 2272 616e 646f 6d5f 6576 656e 745f 6f6e  "random_event_on
-000035f0: 6365 223a 5b0a 2020 2020 2020 2020 2020  ce":[.          
-00003600: 2020 2020 2020 2020 2020 2020 2020 5b35                [5
-00003610: 302c 7b0a 2020 2020 2020 2020 2020 2020  0,{.            
+00003380: 2020 205d 0a20 2020 2020 2020 2020 2020     ].           
+00003390: 2020 2020 2020 2020 205d 0a20 2020 2020           ].     
+000033a0: 2020 2020 2020 2020 2020 2020 2020 207d                 }
+000033b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000033c0: 205d 2c0a 2020 2020 2020 2020 2020 2020   ],.            
+000033d0: 2020 2020 5b33 302c 207b 0a20 2020 2020      [30, {.     
+000033e0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+000033f0: 6576 656e 745f 6e61 6d65 223a 22e4 ba8c  event_name":"...
+00003400: e890 a5e9 95bf e79a 84e6 848f e5a4 a7e5  ................
+00003410: 88a9 e782 ae22 2c0a 2020 2020 2020 2020  .....",.        
+00003420: 2020 2020 2020 2020 2020 2020 2264 6573              "des
+00003430: 6372 6962 6522 3a22 e4ba 8ce8 90a5 e995  cribe":"........
+00003440: bfe7 9a84 e684 8fe5 a4a7 e588 a9e7 82ae  ................
+00003450: e280 94e2 8094 e58a a0e5 85a5 e4ba 86e6  ................
+00003460: af94 e8b5 9bef bc88 3130 25e5 87bb e69d  ........10%.....
+00003470: 8032 e590 8de7 9bae e6a0 87ef bc89 222c  .2............",
+00003480: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003490: 2020 2020 2022 7461 7267 6574 223a 302c       "target":0,
+000034a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000034b0: 2020 2020 2022 6164 645f 686f 7273 6522       "add_horse"
+000034c0: 3a7b 2268 6f72 7365 6e61 6d65 223a 22e4  :{"horsename":".
+000034d0: ba8c e890 a5e9 95bf e79a 84e6 848f e5a4  ................
+000034e0: a7e5 88a9 e782 ae22 2c20 2275 6964 223a  .......", "uid":
+000034f0: 332c 2022 6f77 6e65 7222 3a22 e5b0 8fe5  3, "owner":"....
+00003500: 8fb7 222c 2022 6c6f 6361 7469 6f6e 223a  ..", "location":
+00003510: 3120 7d2c 0a20 2020 2020 2020 2020 2020  1 },.           
+00003520: 2020 2020 2020 2020 2022 7261 6e64 6f6d           "random
+00003530: 5f65 7665 6e74 5f6f 6e63 6522 3a5b 0a20  _event_once":[. 
+00003540: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003550: 2020 2020 2020 205b 3530 2c7b 0a20 2020         [50,{.   
+00003560: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003570: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003580: 2022 6576 656e 745f 6e61 6d65 223a 22e9   "event_name":".
+00003590: 9a8f e69c bae5 87bb e69d 8032 222c 0a20  ...........2",. 
+000035a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000035b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000035c0: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
+000035d0: 303e e8a6 81e5 87bb e69d 80e6 80bb e585  0>..............
+000035e0: b132 e590 8de7 9bae e6a0 8722 2c0a 2020  .2.........",.  
+000035f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003600: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003610: 2020 2274 6172 6765 7422 3a31 2c0a 2020    "target":1,.  
 00003620: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003630: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00003640: 616d 6522 3a20 22e9 9a8f e69c bae5 87bb  ame": ".........
-00003650: e69d 8032 222c 0a20 2020 2020 2020 2020  ...2",.         
+00003630: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003640: 2020 2264 6965 2220 3a31 2c0a 2020 2020    "die" :1,.    
+00003650: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00003660: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003670: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-00003680: 7269 6265 223a 2022 3c30 3ee8 a681 e587  ribe": "<0>.....
-00003690: bbe6 9d80 e680 bbe5 85b1 32e5 908d e79b  ..........2.....
-000036a0: aee6 a087 222c 0a20 2020 2020 2020 2020  ....",.         
-000036b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000036c0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-000036d0: 6574 223a 2031 2c0a 2020 2020 2020 2020  et": 1,.        
+00003670: 2264 656c 6179 5f65 7665 6e74 223a 5b32  "delay_event":[2
+00003680: 2c20 7b0a 2020 2020 2020 2020 2020 2020  , {.            
+00003690: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000036a0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+000036b0: 6e74 5f6e 616d 6522 3a22 e99a 8fe6 9cba  nt_name":"......
+000036c0: e587 bbe6 9d80 3522 2c0a 2020 2020 2020  ......5",.      
+000036d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000036e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000036f0: 2020 2020 2020 2020 2020 2020 2264 6965              "die
-00003700: 2220 3a31 2c0a 2020 2020 2020 2020 2020  " :1,.          
-00003710: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003720: 2020 2020 2020 2020 2020 2264 656c 6179            "delay
-00003730: 5f65 7665 6e74 223a 205b 322c 207b 0a20  _event": [2, {. 
-00003740: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000036f0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+00003700: 3ee8 a681 e587 bbe6 9d80 31e5 908d e79b  >.........1.....
+00003710: aee6 a087 222c 0a20 2020 2020 2020 2020  ....",.         
+00003720: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003730: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00003740: 7461 7267 6574 223a 312c 0a20 2020 2020  target":1,.     
 00003750: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003760: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
-00003770: 6d65 223a 2022 e99a 8fe6 9cba e587 bbe6  me": "..........
-00003780: 9d80 3522 2c0a 2020 2020 2020 2020 2020  ..5",.          
-00003790: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000037a0: 2020 2020 2020 2020 2020 2020 2020 2264                "d
-000037b0: 6573 6372 6962 6522 3a20 223c 303e e8a6  escribe": "<0>..
-000037c0: 81e5 87bb e69d 8031 e590 8de7 9bae e6a0  .......1........
-000037d0: 8722 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-000037e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000037f0: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
-00003800: 6765 7422 3a20 312c 0a20 2020 2020 2020  get": 1,.       
-00003810: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003820: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003830: 2022 6469 6522 3a31 0a20 2020 2020 2020   "die":1.       
+00003760: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003770: 2020 2022 6469 6522 3a31 0a20 2020 2020     "die":1.     
+00003780: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003790: 2020 2020 2020 2020 2020 2020 2020 200a                 .
+000037a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000037b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000037c0: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
+000037d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000037e0: 2020 2020 2020 5d0a 2020 2020 2020 2020        ].        
+000037f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003800: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
+00003810: 2020 2020 2020 2020 2020 2020 2020 5d2c                ],
+00003820: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003830: 2020 2020 2020 2020 205b 3130 302c 7b0a           [100,{.
 00003840: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003850: 2020 2020 2020 2020 2020 2020 200a 2020               .  
-00003860: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003870: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003880: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-00003890: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000038a0: 2020 2020 5d0a 2020 2020 2020 2020 2020      ].          
-000038b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000038c0: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
-000038d0: 2020 2020 2020 2020 2020 2020 5d2c 0a20              ],. 
-000038e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000038f0: 2020 2020 2020 205b 3130 302c 7b0a 2020         [100,{.  
-00003900: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003910: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-00003920: 5f6e 616d 6522 3a20 22e6 97a0 e4ba 8be5  _name": ".......
-00003930: 8f91 e794 9f22 2c0a 2020 2020 2020 2020  .....",.        
-00003940: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003950: 2020 2020 2274 6172 6765 7422 3a20 302c      "target": 0,
+00003850: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
+00003860: 6e74 5f6e 616d 6522 3a22 e697 a0e4 ba8b  nt_name":"......
+00003870: e58f 91e7 949f 222c 0a20 2020 2020 2020  ......",.       
+00003880: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003890: 2020 2020 2022 7461 7267 6574 223a 302c       "target":0,
+000038a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000038b0: 2020 2020 2020 2020 2020 2020 2022 6465               "de
+000038c0: 7363 7269 6265 223a 22e6 97a0 e4ba 8be5  scribe":".......
+000038d0: 8f91 e794 9f22 0a20 2020 2020 2020 2020  .....".         
+000038e0: 2020 2020 2020 2020 2020 2020 2020 207d                 }
+000038f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003900: 2020 2020 2020 2020 205d 0a20 2020 2020           ].     
+00003910: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
+00003920: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003930: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
+00003940: 2020 2020 2020 205d 2c0a 2020 2020 2020         ],.      
+00003950: 2020 2020 2020 2020 2020 5b34 302c 207b            [40, {
 00003960: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00003970: 2020 2020 2020 2020 2020 2020 2022 6465               "de
-00003980: 7363 7269 6265 223a 22e6 97a0 e4ba 8be5  scribe":".......
-00003990: 8f91 e794 9f22 0a20 2020 2020 2020 2020  .....".         
-000039a0: 2020 2020 2020 2020 2020 2020 2020 207d                 }
-000039b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000039c0: 2020 2020 2020 2020 205d 0a20 2020 2020           ].     
-000039d0: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
-000039e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000039f0: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-00003a00: 2020 2020 2020 205d 2c0a 2020 2020 2020         ],.      
-00003a10: 2020 2020 2020 2020 2020 5b34 302c 207b            [40, {
-00003a20: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00003a30: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00003a40: 223a 2022 e688 bfe9 878c e69c 89e7 82b9  ": "............
-00003a50: e5a5 bde5 bab7 e79a 8422 2c0a 2020 2020  .........",.    
-00003a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003a70: 2264 6573 6372 6962 6522 3a20 22e6 88bf  "describe": "...
-00003a80: e987 8ce6 9c89 e782 b9e5 a5bd e5ba b7e7  ................
-00003a90: 9a84 e280 94e2 8094 e58a a0e5 85a5 e4ba  ................
-00003aa0: 86e6 af94 e8b5 9b28 e79c a9e6 9995 e585  .......(........
-00003ab0: b6e4 bb96 e78e a9e5 aeb6 35e5 9b9e e590  ..........5.....
-00003ac0: 88e5 b9b6 e587 bbe9 8080 35e6 ada5 efbc  ..........5.....
-00003ad0: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00003ae0: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-00003af0: 3a20 302c 0a20 2020 2020 2020 2020 2020  : 0,.           
-00003b00: 2020 2020 2020 2020 2022 6164 645f 686f           "add_ho
-00003b10: 7273 6522 3a20 7b22 686f 7273 656e 616d  rse": {"horsenam
-00003b20: 6522 3a20 22e6 88bf e987 8ce6 9c89 e782  e": "...........
-00003b30: b9e5 a5bd e5ba b7e7 9a84 222c 2022 7569  ..........", "ui
-00003b40: 6422 3a20 342c 2022 6f77 6e65 7222 3a20  d": 4, "owner": 
-00003b50: 22e5 b08f e58f b722 2c20 226c 6f63 6174  "......", "locat
-00003b60: 696f 6e22 3a20 3120 7d2c 0a20 2020 2020  ion": 1 },.     
-00003b70: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00003b80: 616e 6f74 6865 725f 6576 656e 7422 3a20  another_event": 
-00003b90: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-00003ba0: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-00003bb0: 5f6e 616d 6522 3a20 22e8 aea9 e688 91e5  _name": ".......
-00003bc0: bab7 e5ba b7ef bc81 222c 0a20 2020 2020  ........",.     
-00003bd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003be0: 2020 2022 6465 7363 7269 6265 223a 223c     "describe":"<
-00003bf0: 303e 3ae5 90ac e8af 9def bc8c e8ae a9e6  0>:.............
-00003c00: 8891 e5ba b7e5 bab7 efbc 81ef bc88 e79c  ................
-00003c10: a9e6 9995 e585 b6e4 bb96 e78e a9e5 aeb6  ................
-00003c20: 35e5 9b9e e590 88e5 b9b6 e4b8 80e6 8bb3  5...............
-00003c30: e587 bbe9 8080 35e6 ada5 efbc 8922 2c0a  ......5......",.
-00003c40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003c50: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-00003c60: 3a20 332c 0a20 2020 2020 2020 2020 2020  : 3,.           
-00003c70: 2020 2020 2020 2020 2020 2020 2022 7665               "ve
-00003c80: 7274 6967 6f22 3a20 312c 0a20 2020 2020  rtigo": 1,.     
+00003970: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00003980: 223a 22e6 88bf e987 8ce6 9c89 e782 b9e5  ":".............
+00003990: a5bd e5ba b7e7 9a84 222c 0a20 2020 2020  ........",.     
+000039a0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+000039b0: 6465 7363 7269 6265 223a 22e6 88bf e987  describe":".....
+000039c0: 8ce6 9c89 e782 b9e5 a5bd e5ba b7e7 9a84  ................
+000039d0: e280 94e2 8094 e58a a0e5 85a5 e4ba 86e6  ................
+000039e0: af94 e8b5 9b28 e79c a9e6 9995 e585 b6e4  .....(..........
+000039f0: bb96 e78e a9e5 aeb6 35e5 9b9e e590 88e5  ........5.......
+00003a00: b9b6 e587 bbe9 8080 35e6 ada5 efbc 8922  ........5......"
+00003a10: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00003a20: 2020 2020 2020 2274 6172 6765 7422 3a30        "target":0
+00003a30: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00003a40: 2020 2020 2020 2261 6464 5f68 6f72 7365        "add_horse
+00003a50: 223a 7b22 686f 7273 656e 616d 6522 3a22  ":{"horsename":"
+00003a60: e688 bfe9 878c e69c 89e7 82b9 e5a5 bde5  ................
+00003a70: bab7 e79a 8422 2c20 2275 6964 223a 342c  .....", "uid":4,
+00003a80: 2022 6f77 6e65 7222 3a22 e5b0 8fe5 8fb7   "owner":"......
+00003a90: 222c 2022 6c6f 6361 7469 6f6e 223a 3120  ", "location":1 
+00003aa0: 7d2c 0a20 2020 2020 2020 2020 2020 2020  },.             
+00003ab0: 2020 2020 2020 2022 616e 6f74 6865 725f         "another_
+00003ac0: 6576 656e 7422 3a7b 0a20 2020 2020 2020  event":{.       
+00003ad0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003ae0: 2022 6576 656e 745f 6e61 6d65 223a 22e8   "event_name":".
+00003af0: aea9 e688 91e5 bab7 e5ba b7ef bc81 222c  ..............",
+00003b00: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003b10: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
+00003b20: 6265 223a 223c 303e 3ae5 90ac e8af 9def  be":"<0>:.......
+00003b30: bc8c e8ae a9e6 8891 e5ba b7e5 bab7 efbc  ................
+00003b40: 81ef bc88 e79c a9e6 9995 e585 b6e4 bb96  ................
+00003b50: e78e a9e5 aeb6 35e5 9b9e e590 88e5 b9b6  ......5.........
+00003b60: e4b8 80e6 8bb3 e587 bbe9 8080 35e6 ada5  ............5...
+00003b70: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00003b80: 2020 2020 2020 2020 2020 2020 2020 2274                "t
+00003b90: 6172 6765 7422 3a33 2c0a 2020 2020 2020  arget":3,.      
+00003ba0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003bb0: 2020 2276 6572 7469 676f 223a 312c 0a20    "vertigo":1,. 
+00003bc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003bd0: 2020 2020 2020 2022 726f 756e 6473 223a         "rounds":
+00003be0: 352c 0a20 2020 2020 2020 2020 2020 2020  5,.             
+00003bf0: 2020 2020 2020 2020 2020 2022 6d6f 7665             "move
+00003c00: 223a 2d35 2c0a 2020 2020 2020 2020 2020  ":-5,.          
+00003c10: 2020 2020 2020 2020 2020 2020 2020 226e                "n
+00003c20: 616d 6522 3a22 e69d b0e6 8bb3 e981 9322  ame":"........."
+00003c30: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00003c40: 2020 2020 2020 2020 207d 200a 0a20 2020           } ..   
+00003c50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003c60: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
+00003c70: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
+00003c80: 2020 2020 2020 5b35 302c 207b 0a20 2020        [50, {.   
 00003c90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003ca0: 2020 2022 726f 756e 6473 223a 352c 0a20     "rounds":5,. 
-00003cb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003cc0: 2020 2020 2020 2022 6d6f 7665 223a 2d35         "move":-5
-00003cd0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00003ce0: 2020 2020 2020 2020 2020 226e 616d 6522            "name"
-00003cf0: 3a22 e69d b0e6 8bb3 e981 9322 0a20 2020  :".........".   
-00003d00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003d10: 2020 2020 207d 200a 0a20 2020 2020 2020       } ..       
-00003d20: 2020 2020 2020 2020 2020 2020 207d 0a20               }. 
-00003d30: 2020 2020 2020 2020 2020 2020 2020 205d                 ]
-00003d40: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00003d50: 2020 5b35 302c 207b 0a20 2020 2020 2020    [50, {.       
-00003d60: 2020 2020 2020 2020 2020 2020 2022 6576               "ev
-00003d70: 656e 745f 6e61 6d65 223a 2022 e889 b2e7  ent_name": "....
-00003d80: bea4 e58f 8be8 8081 e5ae 9ee7 82b9 efbc  ................
-00003d90: 8122 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00003da0: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-00003db0: 6522 3a20 22e8 89b2 e7be a4e5 8f8b e880  e": "...........
-00003dc0: 81e5 ae9e e782 b9ef bc81 e280 94e2 8094  ................
-00003dd0: e58a a0e5 85a5 e4ba 86e6 af94 e8b5 9bef  ................
-00003de0: bc88 e5b0 86e6 8980 e69c 89e5 9ba0 e889  ................
-00003df0: b2e5 9bbe e5be 97e5 88b0 e79a 84e5 8aa0  ................
-00003e00: e980 9fe5 8aa0 e688 90e6 b688 e999 a4ef  ................
-00003e10: bc8c e4bf 9de7 9599 6465 6275 6666 efbc  ........debuff..
-00003e20: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00003e30: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-00003e40: 3a20 302c 0a20 2020 2020 2020 2020 2020  : 0,.           
-00003e50: 2020 2020 2020 2020 2022 6164 645f 686f           "add_ho
-00003e60: 7273 6522 3a20 7b22 686f 7273 656e 616d  rse": {"horsenam
-00003e70: 6522 3a20 22e8 89b2 e7be a4e5 8f8b e880  e": "...........
-00003e80: 81e5 ae9e e782 b9ef bc81 222c 2022 7569  ..........", "ui
-00003e90: 6422 3a20 352c 2022 6f77 6e65 7222 3a20  d": 5, "owner": 
-00003ea0: 22e5 b08f e58f b722 2c20 226c 6f63 6174  "......", "locat
-00003eb0: 696f 6e22 3a20 3120 7d2c 0a20 2020 2020  ion": 1 },.     
-00003ec0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00003ed0: 616e 6f74 6865 725f 6576 656e 7422 3a20  another_event": 
-00003ee0: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-00003ef0: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-00003f00: 5f6e 616d 6522 3a20 22e8 89b2 e7be a4e5  _name": ".......
-00003f10: 8f8b e880 81e5 ae9e e782 b922 2c0a 2020  ...........",.  
-00003f20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003f30: 2020 2020 2020 2264 6573 6372 6962 6522        "describe"
-00003f40: 3a22 3c30 3e3a e889 b2e5 9bbe e4b8 8de5  :"<0>:..........
-00003f50: 8786 e79c 8bef bc81 222c 0a20 2020 2020  ........",.     
+00003ca0: 2022 6576 656e 745f 6e61 6d65 223a 22e8   "event_name":".
+00003cb0: 89b2 e7be a4e5 8f8b e880 81e5 ae9e e782  ................
+00003cc0: b9ef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
+00003cd0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
+00003ce0: 7269 6265 223a 22e8 89b2 e7be a4e5 8f8b  ribe":".........
+00003cf0: e880 81e5 ae9e e782 b9ef bc81 e280 94e2  ................
+00003d00: 8094 e58a a0e5 85a5 e4ba 86e6 af94 e8b5  ................
+00003d10: 9bef bc88 e5b0 86e6 8980 e69c 89e5 9ba0  ................
+00003d20: e889 b2e5 9bbe e5be 97e5 88b0 e79a 84e5  ................
+00003d30: 8aa0 e980 9fe5 8aa0 e688 90e6 b688 e999  ................
+00003d40: a4ef bc8c e4bf 9de7 9599 6465 6275 6666  ..........debuff
+00003d50: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00003d60: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+00003d70: 7422 3a30 2c0a 2020 2020 2020 2020 2020  t":0,.          
+00003d80: 2020 2020 2020 2020 2020 2261 6464 5f68            "add_h
+00003d90: 6f72 7365 223a 7b22 686f 7273 656e 616d  orse":{"horsenam
+00003da0: 6522 3a22 e889 b2e7 bea4 e58f 8be8 8081  e":"............
+00003db0: e5ae 9ee7 82b9 efbc 8122 2c20 2275 6964  .........", "uid
+00003dc0: 223a 352c 2022 6f77 6e65 7222 3a22 e5b0  ":5, "owner":"..
+00003dd0: 8fe5 8fb7 222c 2022 6c6f 6361 7469 6f6e  ....", "location
+00003de0: 223a 3120 7d2c 0a20 2020 2020 2020 2020  ":1 },.         
+00003df0: 2020 2020 2020 2020 2020 2022 616e 6f74             "anot
+00003e00: 6865 725f 6576 656e 7422 3a7b 0a20 2020  her_event":{.   
+00003e10: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003e20: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
+00003e30: 223a 22e8 89b2 e7be a4e5 8f8b e880 81e5  ":".............
+00003e40: ae9e e782 b922 2c0a 2020 2020 2020 2020  .....",.        
+00003e50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003e60: 2264 6573 6372 6962 6522 3a22 3c30 3e3a  "describe":"<0>:
+00003e70: e889 b2e5 9bbe e4b8 8de5 8786 e79c 8bef  ................
+00003e80: bc81 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00003e90: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
+00003ea0: 7267 6574 223a 322c 0a20 2020 2020 2020  rget":2,.       
+00003eb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003ec0: 2022 7461 7267 6574 5f69 735f 6275 6666   "target_is_buff
+00003ed0: 223a 22e5 86b2 e699 95e4 ba86 e4bd 86e7  ":".............
+00003ee0: 88bd 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00003ef0: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
+00003f00: 7665 5f6d 6178 223a 312c 0a20 2020 2020  ve_max":1,.     
+00003f10: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003f20: 2020 2022 6d6f 7665 5f6d 696e 223a 310a     "move_min":1.
+00003f30: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00003f40: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
+00003f50: 2020 2020 2020 2020 2020 2020 2020 7d0a                }.
 00003f60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003f70: 2020 2022 7461 7267 6574 223a 2032 2c0a     "target": 2,.
-00003f80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003f90: 2020 2020 2020 2020 2274 6172 6765 745f          "target_
-00003fa0: 6973 5f62 7566 6622 3a20 22e5 86b2 e699  is_buff": ".....
-00003fb0: 95e4 ba86 e4bd 86e7 88bd 222c 0a20 2020  ..........",.   
-00003fc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00003fd0: 2020 2020 2022 6d6f 7665 5f6d 6178 223a       "move_max":
-00003fe0: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
-00003ff0: 2020 2020 2020 2020 2020 2022 6d6f 7665             "move
-00004000: 5f6d 696e 223a 310a 2020 2020 2020 2020  _min":1.        
-00004010: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004020: 7d0a 2020 2020 2020 2020 2020 2020 2020  }.              
-00004030: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
-00004040: 2020 2020 2020 2020 5d2c 0a20 2020 2020          ],.     
-00004050: 2020 2020 2020 2020 2020 205b 3630 2c20             [60, 
-00004060: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
-00004070: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
-00004080: 6522 3a20 22e6 8abd e58d a1e5 8f88 e4ba  e": "...........
-00004090: 95e4 ba86 efbc 8ce6 8891 e697 a5ef bc81  ................
-000040a0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-000040b0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-000040c0: 223a 2022 e68a bde5 8da1 e58f 88e4 ba95  ": "............
-000040d0: e4ba 86ef bc8c e688 91e6 97a5 efbc 81e2  ................
-000040e0: 8094 e280 94e5 8aa0 e585 a5e4 ba86 e6af  ................
-000040f0: 94e8 b59b efbc 88e5 b086 e689 80e6 9c89  ................
-00004100: e4ba bae6 8b89 e585 a5e9 9a90 e8ba abe7  ................
-00004110: 8ab6 e680 81e4 b894 e59b 9ee5 88b0 e8b5  ................
-00004120: b7e7 82b9 efbc 8922 2c0a 2020 2020 2020  .......",.      
-00004130: 2020 2020 2020 2020 2020 2020 2020 2274                "t
-00004140: 6172 6765 7422 3a20 302c 0a20 2020 2020  arget": 0,.     
-00004150: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00004160: 6164 645f 686f 7273 6522 3a20 7b22 686f  add_horse": {"ho
-00004170: 7273 656e 616d 6522 3a20 22e6 8abd e58d  rsename": ".....
-00004180: a1e5 8f88 e4ba 95e4 ba86 efbc 8ce6 8891  ................
-00004190: e697 a5ef bc81 efbc 8122 2c20 2275 6964  .........", "uid
-000041a0: 223a 2036 2c20 226f 776e 6572 223a 2022  ": 6, "owner": "
-000041b0: e5b0 8fe5 8fb7 222c 2022 6c6f 6361 7469  ......", "locati
-000041c0: 6f6e 223a 2031 207d 2c0a 2020 2020 2020  on": 1 },.      
-000041d0: 2020 2020 2020 2020 2020 2020 2020 2261                "a
-000041e0: 6e6f 7468 6572 5f65 7665 6e74 223a 7b0a  nother_event":{.
-000041f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004200: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00004210: 616d 6522 3a20 22e6 8abd e58d a1e5 8f88  ame": ".........
-00004220: e4ba 95e4 ba86 efbc 8ce6 8891 e697 a5ef  ................
-00004230: bc81 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00004240: 2020 2020 2020 2020 2020 2020 2022 6465               "de
-00004250: 7363 7269 6265 223a 2022 efbc 88e5 b086  scribe": "......
-00004260: e689 80e6 9c89 e4ba bae6 8b89 e585 a5e9  ................
-00004270: 9a90 e8ba abe7 8ab6 e680 81e4 b894 e59b  ................
-00004280: 9ee5 88b0 e8b5 b7e7 82b9 efbc 8922 2c0a  .............",.
-00004290: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000042a0: 2020 2020 2020 2020 2274 6172 6765 7422          "target"
-000042b0: 3a20 322c 0a20 2020 2020 2020 2020 2020  : 2,.           
-000042c0: 2020 2020 2020 2020 2020 2020 2022 6869               "hi
-000042d0: 6469 6e67 223a 312c 0a20 2020 2020 2020  ding":1,.       
-000042e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000042f0: 2022 6d6f 7665 223a 2d31 3030 2c0a 2020   "move":-100,.  
-00004300: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004310: 2020 2020 2020 226e 616d 6522 3a22 e99d        "name":"..
-00004320: 9ee6 b094 e684 9fe6 9f93 220a 2020 2020  ..........".    
-00004330: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004340: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
-00004350: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
-00004360: 2020 2020 2020 2020 2020 2020 5d2c 0a20              ],. 
-00004370: 2020 2020 2020 2020 2020 2020 2020 205b                 [
-00004380: 3730 2c20 7b0a 2020 2020 2020 2020 2020  70, {.          
-00004390: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-000043a0: 5f6e 616d 6522 3a20 22e9 9c80 e8a6 81e7  _name": ".......
-000043b0: ab8b e588 bbe9 a9ac e4b8 8ae5 bc80 e5af  ................
-000043c0: bcef bc81 222c 0a20 2020 2020 2020 2020  ....",.         
-000043d0: 2020 2020 2020 2020 2020 2022 6465 7363             "desc
-000043e0: 7269 6265 223a 2022 e99c 80e8 a681 e7ab  ribe": "........
-000043f0: 8be5 88bb e9a9 ace4 b88a e5bc 80e5 afbc  ................
-00004400: efbc 81e2 8094 e280 94e5 8aa0 e585 a5e4  ................
-00004410: ba86 e6af 94e8 b59b efbc 88e5 afb9 e4b8  ................
-00004420: 80e4 b8aa e7be a4e5 8f8b e592 8ce8 87aa  ................
-00004430: e5b7 b1e8 bf9b e8a1 8c31 30e5 9b9e e590  .........10.....
-00004440: 88e7 9ca9 e699 95ef bc89 222c 0a20 2020  ..........",.   
-00004450: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004460: 2022 7461 7267 6574 223a 2030 2c0a 2020   "target": 0,.  
+00003f70: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
+00003f80: 2020 205b 3630 2c20 7b0a 2020 2020 2020     [60, {.      
+00003f90: 2020 2020 2020 2020 2020 2020 2020 2265                "e
+00003fa0: 7665 6e74 5f6e 616d 6522 3a22 e68a bde5  vent_name":"....
+00003fb0: 8da1 e58f 88e4 ba95 e4ba 86ef bc8c e688  ................
+00003fc0: 91e6 97a5 efbc 8122 2c0a 2020 2020 2020  .......",.      
+00003fd0: 2020 2020 2020 2020 2020 2020 2020 2264                "d
+00003fe0: 6573 6372 6962 6522 3a22 e68a bde5 8da1  escribe":"......
+00003ff0: e58f 88e4 ba95 e4ba 86ef bc8c e688 91e6  ................
+00004000: 97a5 efbc 81e2 8094 e280 94e5 8aa0 e585  ................
+00004010: a5e4 ba86 e6af 94e8 b59b efbc 88e5 b086  ................
+00004020: e689 80e6 9c89 e4ba bae6 8b89 e585 a5e9  ................
+00004030: 9a90 e8ba abe7 8ab6 e680 81e4 b894 e59b  ................
+00004040: 9ee5 88b0 e8b5 b7e7 82b9 efbc 8922 2c0a  .............",.
+00004050: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004060: 2020 2020 2274 6172 6765 7422 3a30 2c0a      "target":0,.
+00004070: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004080: 2020 2020 2261 6464 5f68 6f72 7365 223a      "add_horse":
+00004090: 7b22 686f 7273 656e 616d 6522 3a22 e68a  {"horsename":"..
+000040a0: bde5 8da1 e58f 88e4 ba95 e4ba 86ef bc8c  ................
+000040b0: e688 91e6 97a5 efbc 81ef bc81 222c 2022  ............", "
+000040c0: 7569 6422 3a36 2c20 226f 776e 6572 223a  uid":6, "owner":
+000040d0: 22e5 b08f e58f b722 2c20 226c 6f63 6174  "......", "locat
+000040e0: 696f 6e22 3a31 207d 2c0a 2020 2020 2020  ion":1 },.      
+000040f0: 2020 2020 2020 2020 2020 2020 2020 2261                "a
+00004100: 6e6f 7468 6572 5f65 7665 6e74 223a 7b0a  nother_event":{.
+00004110: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004120: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
+00004130: 616d 6522 3a22 e68a bde5 8da1 e58f 88e4  ame":"..........
+00004140: ba95 e4ba 86ef bc8c e688 91e6 97a5 efbc  ................
+00004150: 8122 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00004160: 2020 2020 2020 2020 2020 2020 2264 6573              "des
+00004170: 6372 6962 6522 3a22 efbc 88e5 b086 e689  cribe":"........
+00004180: 80e6 9c89 e4ba bae6 8b89 e585 a5e9 9a90  ................
+00004190: e8ba abe7 8ab6 e680 81e4 b894 e59b 9ee5  ................
+000041a0: 88b0 e8b5 b7e7 82b9 efbc 8922 2c0a 2020  ...........",.  
+000041b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000041c0: 2020 2020 2020 2274 6172 6765 7422 3a32        "target":2
+000041d0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000041e0: 2020 2020 2020 2020 2020 2268 6964 696e            "hidin
+000041f0: 6722 3a31 2c0a 2020 2020 2020 2020 2020  g":1,.          
+00004200: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+00004210: 6f76 6522 3a2d 3130 302c 0a20 2020 2020  ove":-100,.     
+00004220: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004230: 2020 2022 6e61 6d65 223a 22e9 9d9e e6b0     "name":".....
+00004240: 94e6 849f e69f 9322 0a20 2020 2020 2020  .......".       
+00004250: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004260: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
+00004270: 2020 2020 2020 207d 0a20 2020 2020 2020         }.       
+00004280: 2020 2020 2020 2020 205d 2c0a 2020 2020           ],.    
+00004290: 2020 2020 2020 2020 2020 2020 5b37 302c              [70,
+000042a0: 207b 0a20 2020 2020 2020 2020 2020 2020   {.             
+000042b0: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+000042c0: 6d65 223a 22e9 9c80 e8a6 81e7 ab8b e588  me":"...........
+000042d0: bbe9 a9ac e4b8 8ae5 bc80 e5af bcef bc81  ................
+000042e0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
+000042f0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
+00004300: 223a 22e9 9c80 e8a6 81e7 ab8b e588 bbe9  ":".............
+00004310: a9ac e4b8 8ae5 bc80 e5af bcef bc81 e280  ................
+00004320: 94e2 8094 e58a a0e5 85a5 e4ba 86e6 af94  ................
+00004330: e8b5 9bef bc88 e5af b9e4 b880 e4b8 aae7  ................
+00004340: bea4 e58f 8be5 928c e887 aae5 b7b1 e8bf  ................
+00004350: 9be8 a18c 3130 e59b 9ee5 9088 e79c a9e6  ....10..........
+00004360: 9995 efbc 8922 2c0a 2020 2020 2020 2020  .....",.        
+00004370: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
+00004380: 6765 7422 3a30 2c0a 2020 2020 2020 2020  get":0,.        
+00004390: 2020 2020 2020 2020 2020 2020 2261 6464              "add
+000043a0: 5f68 6f72 7365 223a 7b22 686f 7273 656e  _horse":{"horsen
+000043b0: 616d 6522 3a22 e99c 80e8 a681 e7ab 8be5  ame":"..........
+000043c0: 88bb e9a9 ace4 b88a e5bc 80e5 afbc efbc  ................
+000043d0: 8122 2c20 2275 6964 223a 372c 2022 6f77  .", "uid":7, "ow
+000043e0: 6e65 7222 3a22 e5b0 8fe5 8fb7 222c 2022  ner":"......", "
+000043f0: 6c6f 6361 7469 6f6e 223a 3120 7d2c 0a20  location":1 },. 
+00004400: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004410: 2020 2022 616e 6f74 6865 725f 6576 656e     "another_even
+00004420: 7422 3a7b 0a20 2020 2020 2020 2020 2020  t":{.           
+00004430: 2020 2020 2020 2020 2020 2020 2022 6576               "ev
+00004440: 656e 745f 6e61 6d65 223a 22e9 9c80 e8a6  ent_name":".....
+00004450: 81e7 ab8b e588 bbe9 a9ac e4b8 8ae5 bc80  ................
+00004460: e5af bcef bc81 222c 0a20 2020 2020 2020  ......",.       
 00004470: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004480: 2020 2261 6464 5f68 6f72 7365 223a 207b    "add_horse": {
-00004490: 2268 6f72 7365 6e61 6d65 223a 2022 e99c  "horsename": "..
-000044a0: 80e8 a681 e7ab 8be5 88bb e9a9 ace4 b88a  ................
-000044b0: e5bc 80e5 afbc efbc 8122 2c20 2275 6964  .........", "uid
-000044c0: 223a 2037 2c20 226f 776e 6572 223a 2022  ": 7, "owner": "
-000044d0: e5b0 8fe5 8fb7 222c 2022 6c6f 6361 7469  ......", "locati
-000044e0: 6f6e 223a 2031 207d 2c0a 2020 2020 2020  on": 1 },.      
-000044f0: 2020 2020 2020 2020 2020 2020 2020 2261                "a
-00004500: 6e6f 7468 6572 5f65 7665 6e74 223a 7b0a  nother_event":{.
+00004480: 2022 6465 7363 7269 6265 223a 22ef bc88   "describe":"...
+00004490: e5af b9e4 b880 e4b8 aae7 bea4 e58f 8be5  ................
+000044a0: 928c e887 aae5 b7b1 e8bf 9be8 a18c 3130  ..............10
+000044b0: e59b 9ee5 9088 e79c a9e6 9995 efbc 8922  ..............."
+000044c0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000044d0: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+000044e0: 7422 3a35 2c0a 2020 2020 2020 2020 2020  t":5,.          
+000044f0: 2020 2020 2020 2020 2020 2020 2020 2276                "v
+00004500: 6572 7469 676f 223a 312c 0a20 2020 2020  ertigo":1,.     
 00004510: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004520: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00004530: 616d 6522 3a20 22e9 9c80 e8a6 81e7 ab8b  ame": ".........
-00004540: e588 bbe9 a9ac e4b8 8ae5 bc80 e5af bcef  ................
-00004550: bc81 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-00004560: 2020 2020 2020 2020 2020 2020 2022 6465               "de
-00004570: 7363 7269 6265 223a 2022 efbc 88e5 afb9  scribe": "......
-00004580: e4b8 80e4 b8aa e7be a4e5 8f8b e592 8ce8  ................
-00004590: 87aa e5b7 b1e8 bf9b e8a1 8c31 30e5 9b9e  ...........10...
-000045a0: e590 88e7 9ca9 e699 95ef bc89 222c 0a20  ............",. 
-000045b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000045c0: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-000045d0: 2035 2c0a 2020 2020 2020 2020 2020 2020   5,.            
-000045e0: 2020 2020 2020 2020 2020 2020 2276 6572              "ver
-000045f0: 7469 676f 223a 2031 2c0a 2020 2020 2020  tigo": 1,.      
-00004600: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004610: 2020 2272 6f75 6e64 7322 3a31 302c 0a20    "rounds":10,. 
-00004620: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004630: 2020 2020 2020 2022 6e61 6d65 223a 22e6         "name":".
-00004640: ada3 e59c a8e5 bc80 e5af bce4 baba e794  ................
-00004650: 9f22 0a20 2020 2020 2020 2020 2020 2020  .".             
-00004660: 2020 2020 2020 2020 2020 207d 0a20 2020             }.   
-00004670: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004680: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
-00004690: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
-000046a0: 2020 2020 2020 5b38 302c 207b 0a20 2020        [80, {.   
-000046b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000046c0: 2022 6576 656e 745f 6e61 6d65 223a 2022   "event_name": "
-000046d0: e590 8ee6 8e92 e99d a0e7 aa97 e79a 84e7  ................
-000046e0: 8e8b 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-000046f0: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-00004700: 6265 223a 2022 e590 8ee6 8e92 e99d a0e7  be": "..........
-00004710: aa97 e79a 84e7 8e8b e280 94e2 8094 e58a  ................
-00004720: a0e5 85a5 e4ba 86e6 af94 e8b5 9bef bc88  ................
-00004730: e4bd bfe6 8980 e69c 89e4 baba e99a 90e8  ................
-00004740: baab efbc 8ce5 b9b6 e6ad a2e6 ada5 3130  ..............10
-00004750: e59b 9ee5 9088 efbc 8922 2c0a 2020 2020  .........",.    
-00004760: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004770: 2274 6172 6765 7422 3a20 302c 0a20 2020  "target": 0,.   
-00004780: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004790: 2022 6164 645f 686f 7273 6522 3a20 7b22   "add_horse": {"
-000047a0: 686f 7273 656e 616d 6522 3a20 22e5 908e  horsename": "...
-000047b0: e68e 92e9 9da0 e7aa 97e7 9a84 e78e 8b22  ..............."
-000047c0: 2c20 2275 6964 223a 2038 2c20 226f 776e  , "uid": 8, "own
-000047d0: 6572 223a 2022 e5b0 8fe5 8fb7 222c 2022  er": "......", "
-000047e0: 6c6f 6361 7469 6f6e 223a 2031 207d 2c0a  location": 1 },.
-000047f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004800: 2020 2020 2261 6e6f 7468 6572 5f65 7665      "another_eve
-00004810: 6e74 223a 7b0a 2020 2020 2020 2020 2020  nt":{.          
-00004820: 2020 2020 2020 2020 2020 2020 2020 2265                "e
-00004830: 7665 6e74 5f6e 616d 6522 3a20 22e7 8e8b  vent_name": "...
-00004840: e4b9 8be5 8a9b 222c 0a20 2020 2020 2020  ......",.       
-00004850: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004860: 2022 6465 7363 7269 6265 223a 2022 3c30   "describe": "<0
-00004870: 3ee6 9c89 e590 8ee5 aeab e4bd b3e4 b8bd  >...............
-00004880: e4b8 89e5 8d83 efbc 88e4 bdbf e689 80e6  ................
-00004890: 9c89 e4ba bae9 9a90 e8ba abef bc8c e5b9  ................
-000048a0: b6e6 ada2 e6ad a531 30e5 9b9e e590 88ef  .......10.......
-000048b0: bc89 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-000048c0: 2020 2020 2020 2020 2020 2020 2022 7461               "ta
-000048d0: 7267 6574 223a 2033 2c0a 2020 2020 2020  rget": 3,.      
-000048e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000048f0: 2020 226c 6f63 6174 655f 6c6f 636b 223a    "locate_lock":
-00004900: 2031 2c0a 2020 2020 2020 2020 2020 2020   1,.            
-00004910: 2020 2020 2020 2020 2020 2020 2272 6f75              "rou
-00004920: 6e64 7322 3a31 302c 0a20 2020 2020 2020  nds":10,.       
-00004930: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004940: 2022 6e61 6d65 223a 22e6 8890 e4b8 bae5   "name":".......
-00004950: 908e e5ae abe4 b98b e4b8 8022 0a20 2020  ...........".   
+00004520: 2020 2022 726f 756e 6473 223a 3130 2c0a     "rounds":10,.
+00004530: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004540: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
+00004550: e6ad a3e5 9ca8 e5bc 80e5 afbc e4ba bae7  ................
+00004560: 949f 220a 2020 2020 2020 2020 2020 2020  ..".            
+00004570: 2020 2020 2020 2020 2020 2020 7d0a 2020              }.  
+00004580: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004590: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
+000045a0: 2020 2020 5d2c 0a20 2020 2020 2020 2020      ],.         
+000045b0: 2020 2020 2020 205b 3830 2c20 7b0a 2020         [80, {.  
+000045c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000045d0: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+000045e0: e590 8ee6 8e92 e99d a0e7 aa97 e79a 84e7  ................
+000045f0: 8e8b 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00004600: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
+00004610: 6265 223a 22e5 908e e68e 92e9 9da0 e7aa  be":"...........
+00004620: 97e7 9a84 e78e 8be2 8094 e280 94e5 8aa0  ................
+00004630: e585 a5e4 ba86 e6af 94e8 b59b efbc 88e4  ................
+00004640: bdbf e689 80e6 9c89 e4ba bae9 9a90 e8ba  ................
+00004650: abef bc8c e5b9 b6e6 ada2 e6ad a531 30e5  .............10.
+00004660: 9b9e e590 88ef bc89 222c 0a20 2020 2020  ........",.     
+00004670: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+00004680: 7461 7267 6574 223a 302c 0a20 2020 2020  target":0,.     
+00004690: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+000046a0: 6164 645f 686f 7273 6522 3a7b 2268 6f72  add_horse":{"hor
+000046b0: 7365 6e61 6d65 223a 22e5 908e e68e 92e9  sename":".......
+000046c0: 9da0 e7aa 97e7 9a84 e78e 8b22 2c20 2275  ...........", "u
+000046d0: 6964 223a 382c 2022 6f77 6e65 7222 3a22  id":8, "owner":"
+000046e0: e5b0 8fe5 8fb7 222c 2022 6c6f 6361 7469  ......", "locati
+000046f0: 6f6e 223a 3120 7d2c 0a20 2020 2020 2020  on":1 },.       
+00004700: 2020 2020 2020 2020 2020 2020 2022 616e               "an
+00004710: 6f74 6865 725f 6576 656e 7422 3a7b 0a20  other_event":{. 
+00004720: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004730: 2020 2020 2020 2022 6576 656e 745f 6e61         "event_na
+00004740: 6d65 223a 22e7 8e8b e4b9 8be5 8a9b 222c  me":".........",
+00004750: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00004760: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
+00004770: 6265 223a 223c 303e e69c 89e5 908e e5ae  be":"<0>........
+00004780: abe4 bdb3 e4b8 bde4 b889 e58d 83ef bc88  ................
+00004790: e4bd bfe6 8980 e69c 89e4 baba e99a 90e8  ................
+000047a0: baab efbc 8ce5 b9b6 e6ad a2e6 ada5 3130  ..............10
+000047b0: e59b 9ee5 9088 efbc 8922 2c0a 2020 2020  .........",.    
+000047c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000047d0: 2020 2020 2274 6172 6765 7422 3a33 2c0a      "target":3,.
+000047e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000047f0: 2020 2020 2020 2020 226c 6f63 6174 655f          "locate_
+00004800: 6c6f 636b 223a 312c 0a20 2020 2020 2020  lock":1,.       
+00004810: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004820: 2022 726f 756e 6473 223a 3130 2c0a 2020   "rounds":10,.  
+00004830: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004840: 2020 2020 2020 226e 616d 6522 3a22 e688        "name":"..
+00004850: 90e4 b8ba e590 8ee5 aeab e4b9 8be4 b880  ................
+00004860: 220a 2020 2020 2020 2020 2020 2020 2020  ".              
+00004870: 2020 2020 2020 2020 2020 7d0a 2020 2020            }.    
+00004880: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004890: 7d0a 2020 2020 2020 2020 2020 2020 2020  }.              
+000048a0: 2020 5d2c 0a20 2020 2020 2020 2020 2020    ],.           
+000048b0: 2020 2020 205b 3930 2c20 7b0a 2020 2020       [90, {.    
+000048c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000048d0: 2265 7665 6e74 5f6e 616d 6522 3a22 6469  "event_name":"di
+000048e0: 6fe7 9a84 e5b0 8fe9 9da2 e58c 8522 2c0a  o............",.
+000048f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004900: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
+00004910: 6469 6fe7 9a84 e5b0 8fe9 9da2 e58c 85e2  dio.............
+00004920: 8094 e280 94e5 8aa0 e585 a5e4 ba86 e6af  ................
+00004930: 94e8 b59b efbc 88e8 87aa e5b7 b1e9 9a90  ................
+00004940: e8ba abe4 b894 e69c 80e5 a4a7 e980 9fe6  ................
+00004950: 8f90 e9ab 98e5 88b0 32ef bc89 222c 0a20  ........2...",. 
 00004960: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004970: 2020 2020 207d 0a20 2020 2020 2020 2020       }.         
-00004980: 2020 2020 2020 2020 2020 207d 0a20 2020             }.   
-00004990: 2020 2020 2020 2020 2020 2020 205d 2c0a               ],.
-000049a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000049b0: 5b39 302c 207b 0a20 2020 2020 2020 2020  [90, {.         
-000049c0: 2020 2020 2020 2020 2020 2022 6576 656e             "even
-000049d0: 745f 6e61 6d65 223a 2022 6469 6fe7 9a84  t_name": "dio...
-000049e0: e5b0 8fe9 9da2 e58c 8522 2c0a 2020 2020  .........",.    
-000049f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004a00: 2264 6573 6372 6962 6522 3a20 2264 696f  "describe": "dio
-00004a10: e79a 84e5 b08f e99d a2e5 8c85 e280 94e2  ................
-00004a20: 8094 e58a a0e5 85a5 e4ba 86e6 af94 e8b5  ................
-00004a30: 9bef bc88 e887 aae5 b7b1 e99a 90e8 baab  ................
-00004a40: e4b8 94e6 9c80 e5a4 a7e9 809f e68f 90e9  ................
-00004a50: ab98 e588 b032 efbc 8922 2c0a 2020 2020  .....2...",.    
-00004a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004a70: 2274 6172 6765 7422 3a20 302c 0a20 2020  "target": 0,.   
-00004a80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004a90: 2022 6164 645f 686f 7273 6522 3a20 7b22   "add_horse": {"
-00004aa0: 686f 7273 656e 616d 6522 3a20 2264 696f  horsename": "dio
-00004ab0: e79a 84e5 b08f e99d a2e5 8c85 222c 2022  ............", "
-00004ac0: 7569 6422 3a20 392c 2022 6f77 6e65 7222  uid": 9, "owner"
-00004ad0: 3a20 22e5 b08f e58f b722 2c20 226c 6f63  : "......", "loc
-00004ae0: 6174 696f 6e22 3a20 3120 7d2c 0a20 2020  ation": 1 },.   
-00004af0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004b00: 2022 6869 6469 6e67 223a 312c 0a20 2020   "hiding":1,.   
-00004b10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004b20: 2022 6d6f 7665 5f6d 6178 223a 322c 0a20   "move_max":2,. 
-00004b30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004b40: 2020 2022 6d6f 7665 5f6d 696e 223a 320a     "move_min":2.
-00004b50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004b60: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
-00004b70: 2020 2020 2020 5d2c 0a20 2020 2020 2020        ],.       
-00004b80: 2020 2020 2020 2020 205b 3130 302c 207b           [100, {
-00004b90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00004ba0: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00004bb0: 223a 2022 e5a4 a7e5 928c e8b5 a4e9 aaa5  ": "............
-00004bc0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00004bd0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
-00004be0: 223a 2022 e5a4 a7e5 928c e8b5 a4e9 aaa5  ": "............
-00004bf0: e280 94e2 8094 e58a a0e5 85a5 e4ba 86e6  ................
-00004c00: af94 e8b5 9bef bc88 e69c 80e5 a4a7 e980  ................
-00004c10: 9fe5 88b0 35ef bc89 222c 0a20 2020 2020  ....5...",.     
-00004c20: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00004c30: 7461 7267 6574 223a 2030 2c0a 2020 2020  target": 0,.    
-00004c40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004c50: 226d 6f76 655f 6d61 7822 3a35 2c0a 2020  "move_max":5,.  
-00004c60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004c70: 2020 226d 6f76 655f 6d69 6e22 3a35 2c0a    "move_min":5,.
-00004c80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004c90: 2020 2020 2261 6464 5f68 6f72 7365 223a      "add_horse":
-00004ca0: 207b 2268 6f72 7365 6e61 6d65 223a 2022   {"horsename": "
-00004cb0: e5a4 a7e5 928c e8b5 a4e9 aaa5 222c 2022  ............", "
-00004cc0: 7569 6422 3a20 3130 2c20 226f 776e 6572  uid": 10, "owner
-00004cd0: 223a 2022 e5b0 8fe5 8fb7 222c 2022 6c6f  ": "......", "lo
-00004ce0: 6361 7469 6f6e 223a 2031 207d 0a20 2020  cation": 1 }.   
-00004cf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00004d00: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
-00004d10: 2020 205d 0a20 2020 2020 2020 2020 2020     ].           
-00004d20: 205d 0a20 2020 2020 2020 200a 2020 2020   ].        .    
-00004d30: 2020 2020 7d2c 0a20 2020 2020 2020 207b      },.        {
-00004d40: 0a20 2020 2020 2020 2020 2020 2022 6576  .            "ev
-00004d50: 656e 745f 6e61 6d65 223a 2022 e688 91e6  ent_name": "....
-00004d60: 98af e4ba 8ce6 aca1 e585 83ef bc81 efbc  ................
-00004d70: 8122 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00004d80: 2274 6172 6765 7422 3a20 302c 0a20 2020  "target": 0,.   
-00004d90: 2020 2020 2020 2020 2022 6465 7363 7269           "descri
-00004da0: 6265 223a 223c 303e e5a4 a7e5 968a 3ae6  be":"<0>......:.
-00004db0: 8891 e698 afe4 ba8c e6ac a1e5 8583 efbc  ................
-00004dc0: 81ef bc81 efbc 88e6 b688 e999 a4e8 87aa  ................
-00004dd0: e8ba abe7 9a84 e99a 90e8 baab e4b8 94e6  ................
-00004de0: 8f90 e9ab 98e6 9c80 e5a4 a7e9 809f e588  ................
-00004df0: b032 e980 83e7 a6bb e78e b0e5 9cba efbc  .2..............
-00004e00: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00004e10: 2264 656c 5f62 7566 6622 3a20 2268 6964  "del_buff": "hid
-00004e20: 696e 6722 202c 0a20 2020 2020 2020 2020  ing" ,.         
-00004e30: 2020 2022 6d6f 7665 5f6d 6178 223a 322c     "move_max":2,
-00004e40: 0a20 2020 2020 2020 2020 2020 2022 6d6f  .            "mo
-00004e50: 7665 5f6d 696e 223a 322c 0a20 2020 2020  ve_min":2,.     
-00004e60: 2020 2020 2020 2022 6e61 6d65 223a 22e7         "name":".
-00004e70: a4be e6ad bb22 0a20 2020 2020 2020 207d  .....".        }
-00004e80: 2c0a 2020 2020 2020 2020 7b0a 2020 2020  ,.        {.    
-00004e90: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
-00004ea0: 616d 6522 3a20 22e5 86bb e7bb 9322 2c0a  ame": "......",.
-00004eb0: 2020 2020 2020 2020 2020 2020 2274 6172              "tar
-00004ec0: 6765 7422 3a20 302c 0a20 2020 2020 2020  get": 0,.       
-00004ed0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
-00004ee0: 223c 303e e8b4 a6e5 8fb7 e59b a0e4 bca0  "<0>............
-00004ef0: e692 ade8 89b2 e683 85e6 9ab4 e58a 9be8  ................
-00004f00: a2ab e586 bbe7 bb93 efbc 88e8 bf9b e5b1  ................
-00004f10: 80e5 ad90 e592 afef bc81 e7a6 bbe5 bc80  ................
-00004f20: e8b5 9be5 9cba efbc 8922 2c0a 2020 2020  .........",.    
-00004f30: 2020 2020 2020 2020 2261 7761 7922 3a20          "away": 
-00004f40: 312c 0a20 2020 2020 2020 2020 2020 2022  1,.            "
-00004f50: 6e61 6d65 223a 22e8 a2ab e586 bbe7 bb93  name":".........
-00004f60: 220a 2020 2020 2020 2020 7d2c 0a20 2020  ".        },.   
-00004f70: 2020 2020 207b 0a20 2020 2020 2020 2020       {.         
-00004f80: 2020 2022 6576 656e 745f 6e61 6d65 223a     "event_name":
-00004f90: 2022 e7a6 81e8 a880 222c 0a20 2020 2020   "......",.     
-00004fa0: 2020 2020 2020 2022 7461 7267 6574 223a         "target":
-00004fb0: 2031 2c0a 2020 2020 2020 2020 2020 2020   1,.            
-00004fc0: 2264 6573 6372 6962 6522 3a22 3c30 3e3a  "describe":"<0>:
-00004fd0: e8bf 99e7 a78d e4b8 9ce8 a5bf e4b8 8de8  ................
-00004fe0: 83bd e59c a8e7 bea4 e987 8ce8 afb4 efbc  ................
-00004ff0: 88e6 ada2 e6ad a535 e59b 9ee5 9088 efbc  .......5........
-00005000: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
-00005010: 226c 6f63 6174 655f 6c6f 636b 223a 2031  "locate_lock": 1
-00005020: 2c0a 2020 2020 2020 2020 2020 2020 2272  ,.            "r
-00005030: 6f75 6e64 7322 3a35 2c0a 2020 2020 2020  ounds":5,.      
-00005040: 2020 2020 2020 226e 616d 6522 3a22 e8a2        "name":"..
-00005050: abe7 a681 e8a8 8022 0a20 2020 2020 2020  .......".       
-00005060: 207d 2c0a 2020 2020 2020 2020 7b0a 2020   },.        {.  
-00005070: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
-00005080: 5f6e 616d 6522 3a20 22e6 8891 e5bc 80e6  _name": ".......
-00005090: 9186 e4ba 8622 2c0a 2020 2020 2020 2020  .....",.        
-000050a0: 2020 2020 2274 6172 6765 7422 3a20 302c      "target": 0,
-000050b0: 0a20 2020 2020 2020 2020 2020 2022 6465  .            "de
-000050c0: 7363 7269 6265 223a 223c 303e 3ae6 8891  scribe":"<0>:...
-000050d0: e5bc 80e6 9186 e4ba 86ef bc88 e8a1 a8e9  ................
-000050e0: 9da2 e4b8 8ae5 9ca8 e691 86e4 bd86 e69a  ................
-000050f0: 97e4 b8ad e58d b7e7 9a84 e7a6 bbe8 b0b1  ................
-00005100: efbc 8ce6 9c89 e587 a0e7 8e87 e980 9fe5  ................
-00005110: baa6 e588 b031 30ef bc8c e4b9 9fe6 9c89  .....10.........
-00005120: e587 a0e7 8e87 e6ad a2e6 ada5 35e5 9b9e  ............5...
-00005130: e590 88ef bc89 222c 0a20 2020 2020 2020  ......",.       
-00005140: 2020 2020 2022 7261 6e64 6f6d 5f65 7665       "random_eve
-00005150: 6e74 5f6f 6e63 6522 3a5b 0a20 2020 2020  nt_once":[.     
-00005160: 2020 2020 2020 2020 2020 205b 352c 7b0a             [5,{.
-00005170: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00005180: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
-00005190: 3a20 22e5 85b6 e5ae 9ee6 8891 e59c a8e5  : ".............
-000051a0: 8db7 222c 0a20 2020 2020 2020 2020 2020  ..",.           
-000051b0: 2020 2020 2020 2020 2022 7461 7267 6574           "target
-000051c0: 223a 2030 2c0a 2020 2020 2020 2020 2020  ": 0,.          
-000051d0: 2020 2020 2020 2020 2020 2264 6573 6372            "descr
-000051e0: 6962 6522 3a22 3c30 3e3a e585 b6e5 ae9e  ibe":"<0>:......
-000051f0: e688 91e5 9ca8 e58d b7ef bc88 e980 9fe5  ................
-00005200: baa6 e588 b031 30ef bc89 222c 200a 2020  .....10...", .  
-00005210: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00005220: 2020 226d 6f76 655f 6d61 7822 3a31 302c    "move_max":10,
-00005230: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00005240: 2020 2020 2022 6d6f 7665 5f6d 696e 223a       "move_min":
-00005250: 3130 2c0a 2020 2020 2020 2020 2020 2020  10,.            
-00005260: 2020 2020 2020 2020 226e 616d 6522 3a22          "name":"
-00005270: e58d b7e7 8e8b 220a 2020 2020 2020 2020  ......".        
-00005280: 2020 2020 2020 2020 2020 2020 7d0a 2020              }.  
-00005290: 2020 2020 2020 2020 2020 2020 2020 5d2c                ],
-000052a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000052b0: 205b 3130 302c 7b0a 2020 2020 2020 2020   [100,{.        
-000052c0: 2020 2020 2020 2020 2020 2020 2265 7665              "eve
-000052d0: 6e74 5f6e 616d 6522 3a20 22e7 9c9f e79a  nt_name": ".....
-000052e0: 84e5 9ca8 e691 8622 2c0a 2020 2020 2020  .......",.      
-000052f0: 2020 2020 2020 2020 2020 2020 2020 2274                "t
-00005300: 6172 6765 7422 3a20 302c 0a20 2020 2020  arget": 0,.     
-00005310: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00005320: 6465 7363 7269 6265 223a 223c 303e 3ae6  describe":"<0>:.
-00005330: 8891 e79c 9fe5 9ca8 e691 86ef bc88 e6ad  ................
-00005340: a2e6 ada5 35e5 9b9e e590 88ef bc89 222c  ....5.........",
-00005350: 200a 2020 2020 2020 2020 2020 2020 2020   .              
-00005360: 2020 2020 2020 226c 6f63 6174 655f 6c6f        "locate_lo
-00005370: 636b 223a 312c 0a20 2020 2020 2020 2020  ck":1,.         
-00005380: 2020 2020 2020 2020 2020 2022 726f 756e             "roun
-00005390: 6473 223a 352c 0a20 2020 2020 2020 2020  ds":5,.         
-000053a0: 2020 2020 2020 2020 2020 2022 6e61 6d65             "name
-000053b0: 223a 22e5 bc80 e691 86ef bc81 220a 2020  ":".........".  
-000053c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000053d0: 2020 7d0a 2020 2020 2020 2020 2020 2020    }.            
-000053e0: 2020 200a 2020 2020 2020 2020 2020 2020     .            
-000053f0: 2020 2020 5d0a 2020 2020 2020 2020 2020      ].          
-00005400: 2020 5d0a 2020 2020 2020 2020 7d2c 0a20    ].        },. 
-00005410: 2020 2020 2020 207b 0a20 2020 2020 2020         {.       
-00005420: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00005430: 223a 2022 e698 8ee5 a4a9 e591 a8e6 9cab  ": "............
-00005440: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
-00005450: 7461 7267 6574 223a 2032 2c0a 2020 2020  target": 2,.    
-00005460: 2020 2020 2020 2020 2264 6573 6372 6962          "describ
-00005470: 6522 3a22 e698 8ee5 a4a9 e591 a8e6 9cab  e":"............
-00005480: efbc 8ce4 b88d e79d a1e8 a789 efbc 81ef  ................
-00005490: bc88 e980 9fe5 baa6 e58f 98e4 b8ba 36e6  ..............6.
-000054a0: 8c81 e7bb ad32 e59b 9ee5 9088 efbc 8ce4  .....2..........
-000054b0: bd86 32e5 9b9e e590 88e4 b98b e590 8ee7  ..2.............
-000054c0: 9ca9 e699 9535 e59b 9ee5 9088 efbc 8922  .....5........."
-000054d0: 2c0a 2020 2020 2020 2020 2020 2020 226e  ,.            "n
-000054e0: 616d 6522 3a22 e591 a8e6 9cab efbc 8122  ame":"........."
-000054f0: 2c0a 2020 2020 2020 2020 2020 2020 226d  ,.            "m
-00005500: 6f76 655f 6d61 7822 3a36 2c0a 2020 2020  ove_max":6,.    
-00005510: 2020 2020 2020 2020 226d 6f76 655f 6d69          "move_mi
-00005520: 6e22 3a36 2c0a 2020 2020 2020 2020 2020  n":6,.          
-00005530: 2020 2272 6f75 6e64 7322 3a32 2c0a 2020    "rounds":2,.  
-00005540: 2020 2020 2020 2020 2020 2264 656c 6179            "delay
-00005550: 5f65 7665 6e74 5f73 656c 6622 3a20 5b33  _event_self": [3
-00005560: 2c20 0a20 2020 2020 2020 2020 2020 2020  , .             
+00004970: 2020 2022 7461 7267 6574 223a 302c 0a20     "target":0,. 
+00004980: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004990: 2020 2022 6164 645f 686f 7273 6522 3a7b     "add_horse":{
+000049a0: 2268 6f72 7365 6e61 6d65 223a 2264 696f  "horsename":"dio
+000049b0: e79a 84e5 b08f e99d a2e5 8c85 222c 2022  ............", "
+000049c0: 7569 6422 3a39 2c20 226f 776e 6572 223a  uid":9, "owner":
+000049d0: 22e5 b08f e58f b722 2c20 226c 6f63 6174  "......", "locat
+000049e0: 696f 6e22 3a31 207d 2c0a 2020 2020 2020  ion":1 },.      
+000049f0: 2020 2020 2020 2020 2020 2020 2020 2268                "h
+00004a00: 6964 696e 6722 3a31 2c0a 2020 2020 2020  iding":1,.      
+00004a10: 2020 2020 2020 2020 2020 2020 2020 226d                "m
+00004a20: 6f76 655f 6d61 7822 3a32 2c0a 2020 2020  ove_max":2,.    
+00004a30: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004a40: 226d 6f76 655f 6d69 6e22 3a32 0a20 2020  "move_min":2.   
+00004a50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004a60: 207d 0a20 2020 2020 2020 2020 2020 2020   }.             
+00004a70: 2020 205d 2c0a 2020 2020 2020 2020 2020     ],.          
+00004a80: 2020 2020 2020 5b31 3030 2c20 7b0a 2020        [100, {.  
+00004a90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004aa0: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00004ab0: e5a4 a7e5 928c e8b5 a4e9 aaa5 222c 0a20  ............",. 
+00004ac0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00004ad0: 2020 2022 6465 7363 7269 6265 223a 22e5     "describe":".
+00004ae0: a4a7 e592 8ce8 b5a4 e9aa a5e2 8094 e280  ................
+00004af0: 94e5 8aa0 e585 a5e4 ba86 e6af 94e8 b59b  ................
+00004b00: efbc 88e6 9c80 e5a4 a7e9 809f e588 b035  ...............5
+00004b10: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+00004b20: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+00004b30: 7422 3a30 2c0a 2020 2020 2020 2020 2020  t":0,.          
+00004b40: 2020 2020 2020 2020 2020 226d 6f76 655f            "move_
+00004b50: 6d61 7822 3a35 2c0a 2020 2020 2020 2020  max":5,.        
+00004b60: 2020 2020 2020 2020 2020 2020 226d 6f76              "mov
+00004b70: 655f 6d69 6e22 3a35 2c0a 2020 2020 2020  e_min":5,.      
+00004b80: 2020 2020 2020 2020 2020 2020 2020 2261                "a
+00004b90: 6464 5f68 6f72 7365 223a 7b22 686f 7273  dd_horse":{"hors
+00004ba0: 656e 616d 6522 3a22 e5a4 a7e5 928c e8b5  ename":"........
+00004bb0: a4e9 aaa5 222c 2022 7569 6422 3a31 302c  ....", "uid":10,
+00004bc0: 2022 6f77 6e65 7222 3a22 e5b0 8fe5 8fb7   "owner":"......
+00004bd0: 222c 2022 6c6f 6361 7469 6f6e 223a 3120  ", "location":1 
+00004be0: 7d0a 2020 2020 2020 2020 2020 2020 2020  }.              
+00004bf0: 2020 2020 2020 7d0a 2020 2020 2020 2020        }.        
+00004c00: 2020 2020 2020 2020 5d0a 2020 2020 2020          ].      
+00004c10: 2020 2020 2020 5d0a 2020 2020 2020 2020        ].        
+00004c20: 0a20 2020 2020 2020 207d 2c0a 2020 2020  .        },.    
+00004c30: 2020 2020 7b0a 2020 2020 2020 2020 2020      {.          
+00004c40: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00004c50: e688 91e6 98af e4ba 8ce6 aca1 e585 83ef  ................
+00004c60: bc81 efbc 8122 2c0a 2020 2020 2020 2020  .....",.        
+00004c70: 2020 2020 2274 6172 6765 7422 3a30 2c0a      "target":0,.
+00004c80: 2020 2020 2020 2020 2020 2020 2264 6573              "des
+00004c90: 6372 6962 6522 3a22 3c30 3ee5 a4a7 e596  cribe":"<0>.....
+00004ca0: 8a3a e688 91e6 98af e4ba 8ce6 aca1 e585  .:..............
+00004cb0: 83ef bc81 efbc 81ef bc88 e6b6 88e9 99a4  ................
+00004cc0: e887 aae8 baab e79a 84e9 9a90 e8ba abe4  ................
+00004cd0: b894 e68f 90e9 ab98 e69c 80e5 a4a7 e980  ................
+00004ce0: 9fe5 88b0 32e9 8083 e7a6 bbe7 8eb0 e59c  ....2...........
+00004cf0: baef bc89 222c 0a20 2020 2020 2020 2020  ....",.         
+00004d00: 2020 2022 6465 6c5f 6275 6666 223a 2268     "del_buff":"h
+00004d10: 6964 696e 6722 202c 0a20 2020 2020 2020  iding" ,.       
+00004d20: 2020 2020 2022 6d6f 7665 5f6d 6178 223a       "move_max":
+00004d30: 322c 0a20 2020 2020 2020 2020 2020 2022  2,.            "
+00004d40: 6d6f 7665 5f6d 696e 223a 322c 0a20 2020  move_min":2,.   
+00004d50: 2020 2020 2020 2020 2022 6e61 6d65 223a           "name":
+00004d60: 22e7 a4be e6ad bb22 0a20 2020 2020 2020  "......".       
+00004d70: 207d 2c0a 2020 2020 2020 2020 7b0a 2020   },.        {.  
+00004d80: 2020 2020 2020 2020 2020 2265 7665 6e74            "event
+00004d90: 5f6e 616d 6522 3a22 e586 bbe7 bb93 222c  _name":"......",
+00004da0: 0a20 2020 2020 2020 2020 2020 2022 7461  .            "ta
+00004db0: 7267 6574 223a 302c 0a20 2020 2020 2020  rget":0,.       
+00004dc0: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00004dd0: 223c 303e e8b4 a6e5 8fb7 e59b a0e4 bca0  "<0>............
+00004de0: e692 ade8 89b2 e683 85e6 9ab4 e58a 9be8  ................
+00004df0: a2ab e586 bbe7 bb93 efbc 88e8 bf9b e5b1  ................
+00004e00: 80e5 ad90 e592 afef bc81 e7a6 bbe5 bc80  ................
+00004e10: e8b5 9be5 9cba efbc 8922 2c0a 2020 2020  .........",.    
+00004e20: 2020 2020 2020 2020 2261 7761 7922 3a31          "away":1
+00004e30: 2c0a 2020 2020 2020 2020 2020 2020 226e  ,.            "n
+00004e40: 616d 6522 3a22 e8a2 abe5 86bb e7bb 9322  ame":"........."
+00004e50: 0a20 2020 2020 2020 207d 2c0a 2020 2020  .        },.    
+00004e60: 2020 2020 7b0a 2020 2020 2020 2020 2020      {.          
+00004e70: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00004e80: e7a6 81e8 a880 222c 0a20 2020 2020 2020  ......",.       
+00004e90: 2020 2020 2022 7461 7267 6574 223a 312c       "target":1,
+00004ea0: 0a20 2020 2020 2020 2020 2020 2022 6465  .            "de
+00004eb0: 7363 7269 6265 223a 223c 303e 3ae8 bf99  scribe":"<0>:...
+00004ec0: e7a7 8de4 b89c e8a5 bfe4 b88d e883 bde5  ................
+00004ed0: 9ca8 e7be a4e9 878c e8af b4ef bc88 e6ad  ................
+00004ee0: a2e6 ada5 35e5 9b9e e590 88ef bc89 222c  ....5.........",
+00004ef0: 0a20 2020 2020 2020 2020 2020 2022 6c6f  .            "lo
+00004f00: 6361 7465 5f6c 6f63 6b22 3a31 2c0a 2020  cate_lock":1,.  
+00004f10: 2020 2020 2020 2020 2020 2272 6f75 6e64            "round
+00004f20: 7322 3a35 2c0a 2020 2020 2020 2020 2020  s":5,.          
+00004f30: 2020 226e 616d 6522 3a22 e8a2 abe7 a681    "name":"......
+00004f40: e8a8 8022 0a20 2020 2020 2020 207d 2c0a  ...".        },.
+00004f50: 2020 2020 2020 2020 7b0a 2020 2020 2020          {.      
+00004f60: 2020 2020 2020 2265 7665 6e74 5f6e 616d        "event_nam
+00004f70: 6522 3a22 e688 91e5 bc80 e691 86e4 ba86  e":"............
+00004f80: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
+00004f90: 7461 7267 6574 223a 302c 0a20 2020 2020  target":0,.     
+00004fa0: 2020 2020 2020 2022 6465 7363 7269 6265         "describe
+00004fb0: 223a 223c 303e 3ae6 8891 e5bc 80e6 9186  ":"<0>:.........
+00004fc0: e4ba 86ef bc88 e8a1 a8e9 9da2 e4b8 8ae5  ................
+00004fd0: 9ca8 e691 86e4 bd86 e69a 97e4 b8ad e58d  ................
+00004fe0: b7e7 9a84 e7a6 bbe8 b0b1 efbc 8ce6 9c89  ................
+00004ff0: e587 a0e7 8e87 e980 9fe5 baa6 e588 b031  ...............1
+00005000: 30ef bc8c e4b9 9fe6 9c89 e587 a0e7 8e87  0...............
+00005010: e6ad a2e6 ada5 35e5 9b9e e590 88ef bc89  ......5.........
+00005020: 222c 0a20 2020 2020 2020 2020 2020 2022  ",.            "
+00005030: 7261 6e64 6f6d 5f65 7665 6e74 5f6f 6e63  random_event_onc
+00005040: 6522 3a5b 0a20 2020 2020 2020 2020 2020  e":[.           
+00005050: 2020 2020 205b 352c 7b0a 2020 2020 2020       [5,{.      
+00005060: 2020 2020 2020 2020 2020 2020 2020 2265                "e
+00005070: 7665 6e74 5f6e 616d 6522 3a22 e585 b6e5  vent_name":"....
+00005080: ae9e e688 91e5 9ca8 e58d b722 2c0a 2020  ...........",.  
+00005090: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000050a0: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+000050b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000050c0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+000050d0: 3e3a e585 b6e5 ae9e e688 91e5 9ca8 e58d  >:..............
+000050e0: b7ef bc88 e980 9fe5 baa6 e588 b031 30ef  .............10.
+000050f0: bc89 222c 200a 2020 2020 2020 2020 2020  ..", .          
+00005100: 2020 2020 2020 2020 2020 226d 6f76 655f            "move_
+00005110: 6d61 7822 3a31 302c 0a20 2020 2020 2020  max":10,.       
+00005120: 2020 2020 2020 2020 2020 2020 2022 6d6f               "mo
+00005130: 7665 5f6d 696e 223a 3130 2c0a 2020 2020  ve_min":10,.    
+00005140: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00005150: 226e 616d 6522 3a22 e58d b7e7 8e8b 220a  "name":"......".
+00005160: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00005170: 2020 2020 7d0a 2020 2020 2020 2020 2020      }.          
+00005180: 2020 2020 2020 5d2c 0a20 2020 2020 2020        ],.       
+00005190: 2020 2020 2020 2020 205b 3130 302c 7b0a           [100,{.
+000051a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000051b0: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+000051c0: 3a22 e79c 9fe7 9a84 e59c a8e6 9186 222c  :"............",
+000051d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000051e0: 2020 2020 2022 7461 7267 6574 223a 302c       "target":0,
+000051f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00005200: 2020 2020 2022 6465 7363 7269 6265 223a       "describe":
+00005210: 223c 303e 3ae6 8891 e79c 9fe5 9ca8 e691  "<0>:...........
+00005220: 86ef bc88 e6ad a2e6 ada5 35e5 9b9e e590  ..........5.....
+00005230: 88ef bc89 222c 200a 2020 2020 2020 2020  ....", .        
+00005240: 2020 2020 2020 2020 2020 2020 226c 6f63              "loc
+00005250: 6174 655f 6c6f 636b 223a 312c 0a20 2020  ate_lock":1,.   
+00005260: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00005270: 2022 726f 756e 6473 223a 352c 0a20 2020   "rounds":5,.   
+00005280: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00005290: 2022 6e61 6d65 223a 22e5 bc80 e691 86ef   "name":".......
+000052a0: bc81 220a 2020 2020 2020 2020 2020 2020  ..".            
+000052b0: 2020 2020 2020 2020 7d0a 2020 2020 2020          }.      
+000052c0: 2020 2020 2020 2020 200a 2020 2020 2020           .      
+000052d0: 2020 2020 2020 2020 2020 5d0a 2020 2020            ].    
+000052e0: 2020 2020 2020 2020 5d0a 2020 2020 2020          ].      
+000052f0: 2020 7d2c 0a20 2020 2020 2020 207b 0a20    },.        {. 
+00005300: 2020 2020 2020 2020 2020 2022 6576 656e             "even
+00005310: 745f 6e61 6d65 223a 22e6 988e e5a4 a9e5  t_name":".......
+00005320: 91a8 e69c ab22 2c0a 2020 2020 2020 2020  .....",.        
+00005330: 2020 2020 2274 6172 6765 7422 3a32 2c0a      "target":2,.
+00005340: 2020 2020 2020 2020 2020 2020 2264 6573              "des
+00005350: 6372 6962 6522 3a22 e698 8ee5 a4a9 e591  cribe":"........
+00005360: a8e6 9cab efbc 8ce4 b88d e79d a1e8 a789  ................
+00005370: efbc 81ef bc88 e980 9fe5 baa6 e58f 98e4  ................
+00005380: b8ba 36e6 8c81 e7bb ad32 e59b 9ee5 9088  ..6......2......
+00005390: efbc 8ce4 bd86 32e5 9b9e e590 88e4 b98b  ......2.........
+000053a0: e590 8ee7 9ca9 e699 9535 e59b 9ee5 9088  .........5......
+000053b0: efbc 8922 2c0a 2020 2020 2020 2020 2020  ...",.          
+000053c0: 2020 226e 616d 6522 3a22 e591 a8e6 9cab    "name":"......
+000053d0: efbc 8122 2c0a 2020 2020 2020 2020 2020  ...",.          
+000053e0: 2020 226d 6f76 655f 6d61 7822 3a36 2c0a    "move_max":6,.
+000053f0: 2020 2020 2020 2020 2020 2020 226d 6f76              "mov
+00005400: 655f 6d69 6e22 3a36 2c0a 2020 2020 2020  e_min":6,.      
+00005410: 2020 2020 2020 2272 6f75 6e64 7322 3a32        "rounds":2
+00005420: 2c0a 2020 2020 2020 2020 2020 2020 2264  ,.            "d
+00005430: 656c 6179 5f65 7665 6e74 5f73 656c 6622  elay_event_self"
+00005440: 3a5b 332c 200a 2020 2020 2020 2020 2020  :[3, .          
+00005450: 2020 2020 2020 7b0a 2020 2020 2020 2020        {.        
+00005460: 2020 2020 2020 2020 2265 7665 6e74 5f6e          "event_n
+00005470: 616d 6522 3a22 e8af a5e4 b88a e78f ade4  ame":"..........
+00005480: ba86 222c 0a20 2020 2020 2020 2020 2020  ..",.           
+00005490: 2020 2020 2022 7461 7267 6574 223a 322c       "target":2,
+000054a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000054b0: 2022 6465 7363 7269 6265 223a 22e4 b88a   "describe":"...
+000054c0: e78f ade4 ba86 efbc 8ce7 86ac e5a4 9ce7  ................
+000054d0: 9a84 e590 8ee8 bf87 e69d a5e4 ba86 efbc  ................
+000054e0: 88e7 9ca9 e699 9535 e59b 9ee5 9088 efbc  .......5........
+000054f0: 8922 2c0a 2020 2020 2020 2020 2020 2020  .",.            
+00005500: 2020 2020 2272 6f75 6e64 7322 3a35 2c0a      "rounds":5,.
+00005510: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00005520: 2276 6572 7469 676f 223a 312c 0a20 2020  "vertigo":1,.   
+00005530: 2020 2020 2020 2020 2020 2020 2022 6e61               "na
+00005540: 6d65 223a 22e4 b88a e78f ad22 0a20 2020  me":"......".   
+00005550: 2020 2020 2020 2020 2020 2020 207d 5d0a               }].
+00005560: 2020 2020 2020 2020 7d2c 0a20 2020 2020          },.     
 00005570: 2020 207b 0a20 2020 2020 2020 2020 2020     {.           
-00005580: 2020 2020 2022 6576 656e 745f 6e61 6d65       "event_name
-00005590: 223a 2022 e8af a5e4 b88a e78f ade4 ba86  ": "............
-000055a0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-000055b0: 2020 2022 7461 7267 6574 223a 2032 2c0a     "target": 2,.
-000055c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000055d0: 2264 6573 6372 6962 6522 3a22 e4b8 8ae7  "describe":"....
-000055e0: 8fad e4ba 86ef bc8c e786 ace5 a49c e79a  ................
-000055f0: 84e5 908e e8bf 87e6 9da5 e4ba 86ef bc88  ................
-00005600: e79c a9e6 9995 35e5 9b9e e590 88ef bc89  ......5.........
-00005610: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-00005620: 2020 2022 726f 756e 6473 223a 352c 0a20     "rounds":5,. 
-00005630: 2020 2020 2020 2020 2020 2020 2020 2022                 "
-00005640: 7665 7274 6967 6f22 3a20 312c 0a20 2020  vertigo": 1,.   
-00005650: 2020 2020 2020 2020 2020 2020 2022 6e61               "na
-00005660: 6d65 223a 22e4 b88a e78f ad22 0a20 2020  me":"......".   
-00005670: 2020 2020 2020 2020 2020 2020 207d 5d0a               }].
-00005680: 2020 2020 2020 2020 7d2c 0a20 2020 2020          },.     
-00005690: 2020 207b 0a20 2020 2020 2020 2020 2020     {.           
-000056a0: 2022 6576 656e 745f 6e61 6d65 223a 2022   "event_name": "
-000056b0: e5a4 a7e4 bdac e695 99e6 9599 222c 0a20  ............",. 
-000056c0: 2020 2020 2020 2020 2020 2022 7461 7267             "targ
-000056d0: 6574 223a 2033 2c0a 2020 2020 2020 2020  et": 3,.        
-000056e0: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-000056f0: 3c30 3ee5 a4a7 e4bd ace6 9599 e4bc 9ae4  <0>.............
-00005700: ba86 3c31 3eef bc88 e5a4 8de6 b4bb e79b  ..<1>...........
-00005710: aee6 a087 efbc 8922 2c0a 2020 2020 2020  .......",.      
-00005720: 2020 2020 2020 2274 6172 6765 745f 6973        "target_is
-00005730: 5f62 7566 6622 3a22 6177 6179 222c 0a20  _buff":"away",. 
-00005740: 2020 2020 2020 2020 2020 2022 6465 6c5f             "del_
-00005750: 6275 6666 223a 2261 7761 7922 0a20 2020  buff":"away".   
-00005760: 2020 2020 207d 0a0a 5d0a                      }..].
+00005580: 2022 6576 656e 745f 6e61 6d65 223a 22e5   "event_name":".
+00005590: a4a7 e4bd ace6 9599 e695 9922 2c0a 2020  ...........",.  
+000055a0: 2020 2020 2020 2020 2020 2274 6172 6765            "targe
+000055b0: 7422 3a33 2c0a 2020 2020 2020 2020 2020  t":3,.          
+000055c0: 2020 2264 6573 6372 6962 6522 3a22 3c30    "describe":"<0
+000055d0: 3ee5 a4a7 e4bd ace6 9599 e4bc 9ae4 ba86  >...............
+000055e0: 3c31 3eef bc88 e5a4 8de6 b4bb e79b aee6  <1>.............
+000055f0: a087 efbc 8922 2c0a 2020 2020 2020 2020  .....",.        
+00005600: 2020 2020 2274 6172 6765 745f 6973 5f62      "target_is_b
+00005610: 7566 6622 3a22 6177 6179 222c 0a20 2020  uff":"away",.   
+00005620: 2020 2020 2020 2020 2022 6465 6c5f 6275           "del_bu
+00005630: 6666 223a 2261 7761 7922 0a20 2020 2020  ff":"away".     
+00005640: 2020 207d 0a0a 5d0a                         }..].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/赫尔事件集v1.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/赫尔事件集v1.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 23% similar despite different names*

```diff
@@ -1,63 +1,61 @@
 00000000: 5b0a 2020 7b0a 2020 2265 7665 6e74 5f6e  [.  {.  "event_n
-00000010: 616d 6522 3a20 22e5 88b7 e696 b0e9 8089  ame": ".........
-00000020: e689 8be6 95b0 e68d ae31 222c 0a20 2022  .........1",.  "
-00000030: 7461 7267 6574 223a 2030 2c0a 2020 2264  target": 0,.  "d
-00000040: 6573 6372 6962 6522 3a22 e8b5 abe5 b094  escribe":"......
-00000050: e99a 8fe6 898b e4b8 80e7 82b9 efbc 8ce7  ................
-00000060: 94a8 e7a5 9ee7 a798 e58a 9be9 878f e58a  ................
-00000070: a0e5 bfab e4ba 863c 303e e79a 8442 7566  .......<0>...Buf
-00000080: 6673 e980 9fe5 baa6 efbc 8ce6 8980 e69c  fs..............
-00000090: 89e7 9a84 e695 88e6 9e9c e68c 81e7 bbad  ................
-000000a0: e697 b6e9 97b4 2d31 222c 0a20 2022 6275  ......-1",.  "bu
-000000b0: 6666 5f74 696d 655f 6164 6422 3a20 2d31  ff_time_add": -1
-000000c0: 0a20 207d 2c0a 2020 7b0a 2020 2265 7665  .  },.  {.  "eve
-000000d0: 6e74 5f6e 616d 6522 3a20 22e5 88b7 e696  nt_name": ".....
-000000e0: b0e9 8089 e689 8be6 95b0 e68d ae32 222c  .............2",
-000000f0: 0a20 2022 7461 7267 6574 223a 2032 2c0a  .  "target": 2,.
-00000100: 2020 2264 6573 6372 6962 6522 3a22 e8b5    "describe":"..
-00000110: abe5 b094 e99a 8fe6 898b e4b8 80e7 82b9  ................
-00000120: efbc 8ce7 94a8 e7a5 9ee7 a798 e58a 9be9  ................
-00000130: 878f e58a a0e5 bfab e4ba 863c 303e e79a  ...........<0>..
-00000140: 8442 7566 6673 e980 9fe5 baa6 efbc 8ce6  .Buffs..........
-00000150: 8980 e69c 89e7 9a84 e695 88e6 9e9c e68c  ................
-00000160: 81e7 bbad e697 b6e9 97b4 2d31 222c 0a20  ..........-1",. 
-00000170: 2022 6275 6666 5f74 696d 655f 6164 6422   "buff_time_add"
-00000180: 3a20 2d31 0a20 207d 2c0a 2020 7b0a 2020  : -1.  },.  {.  
-00000190: 2265 7665 6e74 5f6e 616d 6522 3a20 22e8  "event_name": ".
-000001a0: b58b e4ba 88e9 8089 e689 8be7 9ca9 e699  ................
-000001b0: 9542 7566 6622 2c0a 2020 2274 6172 6765  .Buff",.  "targe
-000001c0: 7422 3a20 302c 0a20 2022 6465 7363 7269  t": 0,.  "descri
-000001d0: 6265 223a 2022 e8b5 abe5 b094 e689 bee4  be": "..........
-000001e0: b88d e588 b0e7 94b7 e69c 8be5 8f8b e4b9  ................
-000001f0: 9fe6 89be e4b8 8de5 88b0 e5a5 b3e6 9c8b  ................
-00000200: e58f 8bef bc8c e99d 9ee5 b8b8 e794 9fe6  ................
-00000210: b094 efbc 8ce9 9a8f e4be bfe7 bb99 e4ba  ................
-00000220: 863c 303e e4b8 80e4 b8aa 33e5 9b9e e590  .<0>......3.....
-00000230: 88e7 9a84 e79c a9e6 9995 4275 6666 222c  ..........Buff",
-00000240: 0a20 2022 726f 756e 6473 223a 2033 2c0a  .  "rounds": 3,.
-00000250: 2020 226e 616d 6522 3a20 22e7 9ca9 e699    "name": ".....
-00000260: 9522 2c0a 2020 2276 6572 7469 676f 223a  .",.  "vertigo":
-00000270: 2031 0a20 207d 2c0a 2020 7b0a 2020 2265   1.  },.  {.  "e
-00000280: 7665 6e74 5f6e 616d 6522 3a20 22e6 8891  vent_name": "...
-00000290: e5b0 8621 e689 ade8 bdac e4b8 87e8 b1a1  ...!............
-000002a0: 2122 2c0a 2020 2274 6172 6765 7422 3a20  !",.  "target": 
-000002b0: 322c 0a20 2022 6465 7363 7269 6265 223a  2,.  "describe":
-000002c0: 2022 e8b5 abe5 b094 e59b a0e4 b8ba e68a   "..............
-000002d0: bde4 b88d e587 bae8 af86 e5ae 9def bc8c  ................
-000002e0: e6b0 94e6 84a4 e79a 84e5 a4a7 e596 8aef  ................
-000002f0: bc8c e688 91e5 b086 2121 e689 ade8 bdac  ........!!......
-00000300: e4b8 87e8 b1a1 2121 222c 0a20 2022 7472  ......!!",.  "tr
-00000310: 6163 6b5f 7261 6e64 6f6d 5f6c 6f63 6174  ack_random_locat
-00000320: 696f 6e22 3a20 310a 2020 7d2c 0a20 207b  ion": 1.  },.  {
-00000330: 0a20 2022 6576 656e 745f 6e61 6d65 223a  .  "event_name":
-00000340: 2022 e688 91e5 b086 21e6 89ad e8bd ace4   "......!.......
-00000350: b887 e8b1 a121 222c 0a20 2022 7461 7267  .....!",.  "targ
-00000360: 6574 223a 2032 2c0a 2020 2264 6573 6372  et": 2,.  "descr
-00000370: 6962 6522 3a20 22e8 b5ab e5b0 94e6 8abd  ibe": ".........
-00000380: e587 bae4 ba86 e8af 86e5 ae9d efbc 8ce5  ................
-00000390: bc80 e5bf 83e7 9a84 e5a4 a7e5 968a efbc  ................
-000003a0: 8ce6 8891 e5b0 8621 21e6 89ad e8bd ace4  .......!!.......
-000003b0: b880 e588 8721 2128 e689 80e6 9c89 e980  .....!!(........
-000003c0: 89e6 898b e5a4 8de6 b4bb efbc 8922 2c0a  .............",.
-000003d0: 2020 226c 6976 6522 3a20 310a 2020 7d0a    "live": 1.  }.
-000003e0: 5d0a 0a                                  ]..
+00000010: 616d 6522 3a22 e588 b7e6 96b0 e980 89e6  ame":"..........
+00000020: 898b e695 b0e6 8dae 3122 2c0a 2020 2274  ........1",.  "t
+00000030: 6172 6765 7422 3a30 2c0a 2020 2264 6573  arget":0,.  "des
+00000040: 6372 6962 6522 3a22 e8b5 abe5 b094 e99a  cribe":"........
+00000050: 8fe6 898b e4b8 80e7 82b9 efbc 8ce7 94a8  ................
+00000060: e7a5 9ee7 a798 e58a 9be9 878f e58a a0e5  ................
+00000070: bfab e4ba 863c 303e e79a 8442 7566 6673  .....<0>...Buffs
+00000080: e980 9fe5 baa6 efbc 8ce6 8980 e69c 89e7  ................
+00000090: 9a84 e695 88e6 9e9c e68c 81e7 bbad e697  ................
+000000a0: b6e9 97b4 2d31 222c 0a20 2022 6275 6666  ....-1",.  "buff
+000000b0: 5f74 696d 655f 6164 6422 3a2d 310a 2020  _time_add":-1.  
+000000c0: 7d2c 0a20 207b 0a20 2022 6576 656e 745f  },.  {.  "event_
+000000d0: 6e61 6d65 223a 22e5 88b7 e696 b0e9 8089  name":".........
+000000e0: e689 8be6 95b0 e68d ae32 222c 0a20 2022  .........2",.  "
+000000f0: 7461 7267 6574 223a 322c 0a20 2022 6465  target":2,.  "de
+00000100: 7363 7269 6265 223a 22e8 b5ab e5b0 94e9  scribe":".......
+00000110: 9a8f e689 8be4 b880 e782 b9ef bc8c e794  ................
+00000120: a8e7 a59e e7a7 98e5 8a9b e987 8fe5 8aa0  ................
+00000130: e5bf abe4 ba86 3c30 3ee7 9a84 4275 6666  ......<0>...Buff
+00000140: 73e9 809f e5ba a6ef bc8c e689 80e6 9c89  s...............
+00000150: e79a 84e6 9588 e69e 9ce6 8c81 e7bb ade6  ................
+00000160: 97b6 e997 b42d 3122 2c0a 2020 2262 7566  .....-1",.  "buf
+00000170: 665f 7469 6d65 5f61 6464 223a 2d31 0a20  f_time_add":-1. 
+00000180: 207d 2c0a 2020 7b0a 2020 2265 7665 6e74   },.  {.  "event
+00000190: 5f6e 616d 6522 3a22 e8b5 8be4 ba88 e980  _name":"........
+000001a0: 89e6 898b e79c a9e6 9995 4275 6666 222c  ..........Buff",
+000001b0: 0a20 2022 7461 7267 6574 223a 302c 0a20  .  "target":0,. 
+000001c0: 2022 6465 7363 7269 6265 223a 22e8 b5ab   "describe":"...
+000001d0: e5b0 94e6 89be e4b8 8de5 88b0 e794 b7e6  ................
+000001e0: 9c8b e58f 8be4 b99f e689 bee4 b88d e588  ................
+000001f0: b0e5 a5b3 e69c 8be5 8f8b efbc 8ce9 9d9e  ................
+00000200: e5b8 b8e7 949f e6b0 94ef bc8c e99a 8fe4  ................
+00000210: bebf e7bb 99e4 ba86 3c30 3ee4 b880 e4b8  ........<0>.....
+00000220: aa33 e59b 9ee5 9088 e79a 84e7 9ca9 e699  .3..............
+00000230: 9542 7566 6622 2c0a 2020 2272 6f75 6e64  .Buff",.  "round
+00000240: 7322 3a33 2c0a 2020 226e 616d 6522 3a22  s":3,.  "name":"
+00000250: e79c a9e6 9995 222c 0a20 2022 7665 7274  ......",.  "vert
+00000260: 6967 6f22 3a31 0a20 207d 2c0a 2020 7b0a  igo":1.  },.  {.
+00000270: 2020 2265 7665 6e74 5f6e 616d 6522 3a22    "event_name":"
+00000280: e688 91e5 b086 21e6 89ad e8bd ace4 b887  ......!.........
+00000290: e8b1 a121 222c 0a20 2022 7461 7267 6574  ...!",.  "target
+000002a0: 223a 322c 0a20 2022 6465 7363 7269 6265  ":2,.  "describe
+000002b0: 223a 22e8 b5ab e5b0 94e5 9ba0 e4b8 bae6  ":".............
+000002c0: 8abd e4b8 8de5 87ba e8af 86e5 ae9d efbc  ................
+000002d0: 8ce6 b094 e684 a4e7 9a84 e5a4 a7e5 968a  ................
+000002e0: efbc 8ce6 8891 e5b0 8621 21e6 89ad e8bd  .........!!.....
+000002f0: ace4 b887 e8b1 a121 2122 2c0a 2020 2274  .......!!",.  "t
+00000300: 7261 636b 5f72 616e 646f 6d5f 6c6f 6361  rack_random_loca
+00000310: 7469 6f6e 223a 310a 2020 7d2c 0a20 207b  tion":1.  },.  {
+00000320: 0a20 2022 6576 656e 745f 6e61 6d65 223a  .  "event_name":
+00000330: 22e6 8891 e5b0 8621 e689 ade8 bdac e4b8  "......!........
+00000340: 87e8 b1a1 2122 2c0a 2020 2274 6172 6765  ....!",.  "targe
+00000350: 7422 3a32 2c0a 2020 2264 6573 6372 6962  t":2,.  "describ
+00000360: 6522 3a22 e8b5 abe5 b094 e68a bde5 87ba  e":"............
+00000370: e4ba 86e8 af86 e5ae 9def bc8c e5bc 80e5  ................
+00000380: bf83 e79a 84e5 a4a7 e596 8aef bc8c e688  ................
+00000390: 91e5 b086 2121 e689 ade8 bdac e4b8 80e5  ....!!..........
+000003a0: 8887 2121 28e6 8980 e69c 89e9 8089 e689  ..!!(...........
+000003b0: 8be5 a48d e6b4 bbef bc89 222c 0a20 2022  ..........",.  "
+000003c0: 6c69 7665 223a 310a 2020 7d0a 5d0a 0a    live":1.  }.]..
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events/horserace/赫尔的赛马场事件簿.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/horserace/赫尔的赛马场事件簿.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 8% similar despite different names*

```diff
@@ -1,139 +1,138 @@
 00000000: 5b0a 2020 7b0a 2020 2020 2265 7665 6e74  [.  {.    "event
-00000010: 5f6e 616d 6522 3a20 22e8 b59b e9a9 ace5  _name": ".......
-00000020: 9cba e4ba 8be4 bbb6 e7b0 bf31 222c 0a20  ...........1",. 
-00000030: 2020 2022 7461 7267 6574 223a 2030 2c0a     "target": 0,.
-00000040: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-00000050: 5be8 b59b e9a9 ace5 9cba e680 aae8 b088  [...............
-00000060: 5d3c 303e e79c 8be5 88b0 e4ba 86e8 b59b  ]<0>............
-00000070: e9a9 ace5 9cba e79a 84e6 898b e586 8cef  ................
-00000080: bc9a 322e e8af b7e4 b88d e8a6 81e6 90ba  ..2.............
-00000090: e5b8 a6e9 a39f e789 a9ef bc8c e5b0 a4e5  ................
-000000a0: 85b6 e698 afe4 baba e7b1 bbe7 9a84 e9a3  ................
-000000b0: 9fe7 89a9 e68a 95e5 9682 e4bc 91e6 81af  ................
-000000c0: e58c bae4 b8ad e79a 84e9 a9ac e584 bfe3  ................
-000000d0: 8082 220a 7d2c 0a20 207b 0a20 2020 2022  ..".},.  {.    "
-000000e0: 6576 656e 745f 6e61 6d65 223a 2022 e8b5  event_name": "..
-000000f0: 9be9 a9ac e59c bae4 ba8b e4bb b6e7 b0bf  ................
-00000100: 3222 2c0a 2020 2020 2274 6172 6765 7422  2",.    "target"
-00000110: 3a20 302c 0a20 2020 2022 6465 7363 7269  : 0,.    "descri
-00000120: 6265 223a 225b e8b5 9be9 a9ac e59c bae6  be":"[..........
-00000130: 80aa e8b0 885d 3c30 3ee7 9c8b e588 b0e4  .....]<0>.......
-00000140: ba86 e8b5 9be9 a9ac e59c bae7 9a84 e689  ................
-00000150: 8be5 868c efbc 9a33 2ee5 a682 e69e 9ce4  .......3........
-00000160: bda0 e79c 8be5 88b0 e9a9 ace5 84bf e592  ................
-00000170: 8ce4 bda0 e5af b9e8 a786 efbc 8ce8 afb7  ................
-00000180: e7ab 8be5 88bb e8bd ace7 a7bb e8a7 86e7  ................
-00000190: babf 220a 7d2c 0a20 2020 207b 0a20 2020  ..".},.    {.   
-000001a0: 2022 6576 656e 745f 6e61 6d65 223a 2022   "event_name": "
-000001b0: e8b5 9be9 a9ac e59c bae4 ba8b e4bb b6e7  ................
-000001c0: b0bf 3322 2c0a 2020 2020 2274 6172 6765  ..3",.    "targe
-000001d0: 7422 3a20 302c 0a20 2020 2022 6465 7363  t": 0,.    "desc
-000001e0: 7269 6265 223a 225b e8b5 9be9 a9ac e59c  ribe":"[........
-000001f0: bae6 80aa e8b0 885d 3c30 3ee7 9c8b e588  .......]<0>.....
-00000200: b0e4 ba86 e8b5 9be9 a9ac e59c bae7 9a84  ................
-00000210: e689 8be5 868c efbc 9a37 2ee5 9ca8 e8b5  .........7......
-00000220: 9be9 a9ac e591 a8e8 beb9 e5b0 8fe9 93ba  ................
-00000230: e4b8 adef bc8c e688 91e4 bbac e4b8 8de4  ................
-00000240: bc9a e68f 90e4 be9b e4b8 94e4 bdbf e794  ................
-00000250: a8e5 908d e4b8 bae9 8791 e5b8 81e7 9a84  ................
-00000260: e5b0 8fe7 a1ac e5b8 81ef bc8c e5a6 82e6  ................
-00000270: 9e9c e58f 91e7 8eb0 e5b7 a5e4 bd9c e4ba  ................
-00000280: bae5 9198 e8af a2e9 97ae e4bd a0e6 98af  ................
-00000290: e590 a6e8 a681 e4bd bfe7 94a8 e987 91e5  ................
-000002a0: b881 e585 91e6 8da2 e789 a9e5 9381 efbc  ................
-000002b0: 8ce8 afb7 e7ab 8be5 88bb e7a6 bbe5 bc80  ................
-000002c0: e591 a8e8 beb9 e5b0 8fe9 93ba efbc 8ce5  ................
-000002d0: b9b6 e5af bbe6 89be e999 84e8 bf91 e79a  ................
-000002e0: 84e5 b7a5 e4bd 9ce4 baba e591 98e8 afb4  ................
-000002f0: e698 8ee6 8385 e586 b5e3 8082 220a 0a7d  ............"..}
-00000300: 2c0a 2020 7b0a 2020 2020 2265 7665 6e74  ,.  {.    "event
-00000310: 5f6e 616d 6522 3a20 22e8 b59b e9a9 ace5  _name": ".......
-00000320: 9cba e4ba 8be4 bbb6 e7b0 bf34 222c 0a20  ...........4",. 
-00000330: 2020 2022 7461 7267 6574 223a 2030 2c0a     "target": 0,.
-00000340: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-00000350: 5be8 b59b e9a9 ace5 9cba e680 aae8 b088  [...............
-00000360: 5d3c 303e e79c 8be5 88b0 e4ba 86e8 b59b  ]<0>............
-00000370: e9a9 ace5 9cba e79a 84e6 898b e586 8cef  ................
-00000380: bc9a 382e e8b5 9be9 a9ac e59c bae4 bbbb  ..8.............
-00000390: e4bd 95e4 b880 e4b8 aae6 af94 e8b5 9be5  ................
-000003a0: 8cba e59f 9fe5 8faa e4bc 9ae5 9ca8 393a  ..............9:
-000003b0: 3030 2d31 313a 3030 e592 8c31 353a 3030  00-11:00...15:00
-000003c0: 2d31 373a 3030 e5bc 80e6 94be efbc 8ce5  -17:00..........
-000003d0: a682 e69e 9ce5 85b6 e4bb 96e6 97b6 e997  ................
-000003e0: b4e5 b7a5 e4bd 9ce4 baba e591 98e6 8ea8  ................
-000003f0: e88d 90e4 bda0 e589 8de5 be80 e8a7 82e7  ................
-00000400: 9c8b e6af 94e8 b59b efbc 8ce8 afb7 e4b8  ................
-00000410: 8de8 a681 e78a b9e8 b1ab e79b b4e6 8ea5  ................
-00000420: e68b 92e7 bb9d e5b9 b6e8 bf9c e7a6 bbe6  ................
-00000430: ada4 e5b7 a5e4 bd9c e4ba bae5 9198 e380  ................
-00000440: 8222 0a7d 2c0a 2020 7b0a 2020 2020 2265  .".},.  {.    "e
-00000450: 7665 6e74 5f6e 616d 6522 3a20 22e8 b59b  vent_name": "...
-00000460: e9a9 ace5 9cba e4ba 8be4 bbb6 e7b0 bf35  ...............5
-00000470: 222c 0a20 2020 2022 7461 7267 6574 223a  ",.    "target":
-00000480: 2030 2c0a 2020 2020 2264 6573 6372 6962   0,.    "describ
-00000490: 6522 3a22 5be8 b59b e9a9 ace5 9cba e680  e":"[...........
-000004a0: aae8 b088 5d3c 303e e68d a1e5 88b0 e4ba  ....]<0>........
-000004b0: 86e4 b880 e4b8 aae8 b59b e9a9 ace5 9cba  ................
-000004c0: e689 8be5 868c e4b9 a6e3 8082 e58f afe4  ................
-000004d0: bba5 e587 ade5 809f e8bf 99e6 9da1 e6b6  ................
-000004e0: 88e6 81af e689 be20 e8b5 abe5 b094 20e9  ....... ...... .
-000004f0: a286 e58f 9620 3ee8 b59b e9a9 ace5 9cba  ..... >.........
-00000500: e680 aae8 b088 e8a7 84e5 8899 e696 87e6  ................
-00000510: a188 3c22 0a7d 2c0a 2020 7b0a 2020 2020  ..<".},.  {.    
-00000520: 2265 7665 6e74 5f6e 616d 6522 3a20 22e8  "event_name": ".
-00000530: b59b e9a9 ace5 9cba e4ba 8be4 bbb6 e7b0  ................
-00000540: bf36 222c 0a20 2020 2022 7461 7267 6574  .6",.    "target
-00000550: 223a 2030 2c0a 2020 2020 2264 6573 6372  ": 0,.    "descr
-00000560: 6962 6522 3a22 5be8 b59b e9a9 ace5 9cba  ibe":"[.........
-00000570: e680 aae8 b088 5d3c 303e e6ad a3e5 9ca8  ......]<0>......
-00000580: e4bb 94e7 bb86 e998 85e8 afbb e8b5 9be9  ................
-00000590: a9ac e59c bae6 898b e586 8cef bc9a 3130  ..............10
-000005a0: 2ee5 a682 e69e 9ce5 8f91 e78e b0e5 91a8  ................
-000005b0: e8be b9e6 9c89 e99b bee9 9cbe efbc 8ce8  ................
-000005c0: afb7 e68c 89e7 85a7 e59c b0e5 9bbe e68c  ................
-000005d0: 87e7 a4ba e79a 84e8 b7af e5be 84e7 a6bb  ................
-000005e0: e5bc 80e8 b59b e9a9 ace5 9cba e380 8222  ..............."
-000005f0: 0a7d 2c0a 2020 7b0a 2020 2020 2265 7665  .},.  {.    "eve
-00000600: 6e74 5f6e 616d 6522 3a20 22e8 b59b e9a9  nt_name": ".....
-00000610: ace5 9cba e4ba 8be4 bbb6 e7b0 bf37 222c  .............7",
-00000620: 0a20 2020 2022 7461 7267 6574 223a 2030  .    "target": 0
-00000630: 2c0a 2020 2020 2264 6573 6372 6962 6522  ,.    "describe"
-00000640: 3a22 5be5 8aa8 e789 a9e5 9bad e8a7 84e5  :"[.............
-00000650: 8899 e680 aae8 b088 5d3c 303e e59c a8e8  ........]<0>....
-00000660: b59b e9a9 ace5 9cba e79c 8be5 88b0 e4ba  ................
-00000670: 86e7 99bd e889 b2e7 9a84 e5a4 a7e8 b1a1  ................
-00000680: e59c a8e6 b8b8 e6b3 b3e3 8082 e5bc 80e5  ................
-00000690: a78b e680 80e7 9691 e887 aae5 b7b1 e698  ................
-000006a0: afe8 b081 efbc 8128 33e5 9b9e e590 882d  .......(3......-
-000006b0: 327e 2b32 2922 2c0a 2020 2020 2272 6f75  2~+2)",.    "rou
-000006c0: 6e64 7322 3a20 332c 0a20 2020 2022 6e61  nds": 3,.    "na
-000006d0: 6d65 223a 2022 3f22 2c0a 2020 2020 226d  me": "?",.    "m
-000006e0: 6f76 655f 6d61 7822 3a20 322c 0a20 2020  ove_max": 2,.   
-000006f0: 2022 6d6f 7665 5f6d 696e 223a 202d 320a   "move_min": -2.
-00000700: 7d2c 0a20 207b 0a20 2020 2022 6576 656e  },.  {.    "even
-00000710: 745f 6e61 6d65 223a 2022 e8b5 9be9 a9ac  t_name": "......
-00000720: e59c bae4 ba8b e4bb b6e7 b0bf 3822 2c0a  ............8",.
-00000730: 2020 2020 2274 6172 6765 7422 3a20 302c      "target": 0,
-00000740: 0a20 2020 2022 6465 7363 7269 6265 223a  .    "describe":
-00000750: 225b e58a a8e7 89a9 e59b ade8 a784 e588  "[..............
-00000760: 99e6 80aa e8b0 885d 3c30 3ee5 9ca8 e8b5  .......]<0>.....
-00000770: 9be9 a9ac e59c bae5 8685 e58f 91e7 8eb0  ................
-00000780: e4ba 86e6 b0b4 e697 8fe9 a686 efbc 8153  ...............S
-00000790: 616e e580 bce7 96af e78b 82e4 b88b e999  an..............
-000007a0: 8def bc81 e79b b4e6 8ea5 e980 80e5 9b9e  ................
-000007b0: e8b5 b7e7 82b9 efbc 8122 2c0a 2020 2020  .........",.    
-000007c0: 226d 6f76 6522 3a20 2d31 3030 0a20 207d  "move": -100.  }
-000007d0: 2c0a 2020 7b0a 2020 2020 2265 7665 6e74  ,.  {.    "event
-000007e0: 5f6e 616d 6522 3a20 22e8 b59b e9a9 ace5  _name": ".......
-000007f0: 9cba e4ba 8be4 bbb6 e7b0 bf39 222c 0a20  ...........9",. 
-00000800: 2020 2022 7461 7267 6574 223a 2030 2c0a     "target": 0,.
-00000810: 2020 2020 2264 6573 6372 6962 6522 3a22      "describe":"
-00000820: 5be5 8aa8 e789 a9e5 9bad e8a7 84e5 8899  [...............
-00000830: e680 aae8 b088 5d3c 303e e59c a8e8 b59b  ......]<0>......
-00000840: e9a9 ace5 9cba e586 85e5 969d e4ba 86e5  ................
-00000850: 8594 e5ad 90e8 a180 efbc 8ce5 9083 e4ba  ................
-00000860: 86e5 b1b1 e7be 8ae8 8289 e380 82e8 a789  ................
-00000870: e5be 97e8 87aa e5b7 b1e7 aa81 e784 b6e5  ................
-00000880: 8585 e6bb a1e4 ba86 e58a 9be9 878f efbc  ................
-00000890: 81e5 898d e8bf 9b35 222c 0a20 2020 2022  .......5",.    "
-000008a0: 6d6f 7665 223a 2035 0a20 207d 0a5d 0a    move": 5.  }.].
+00000010: 5f6e 616d 6522 3a22 e8b5 9be9 a9ac e59c  _name":"........
+00000020: bae4 ba8b e4bb b6e7 b0bf 3122 2c0a 2020  ..........1",.  
+00000030: 2020 2274 6172 6765 7422 3a30 2c0a 2020    "target":0,.  
+00000040: 2020 2264 6573 6372 6962 6522 3a22 5be8    "describe":"[.
+00000050: b59b e9a9 ace5 9cba e680 aae8 b088 5d3c  ..............]<
+00000060: 303e e79c 8be5 88b0 e4ba 86e8 b59b e9a9  0>..............
+00000070: ace5 9cba e79a 84e6 898b e586 8cef bc9a  ................
+00000080: 322e e8af b7e4 b88d e8a6 81e6 90ba e5b8  2...............
+00000090: a6e9 a39f e789 a9ef bc8c e5b0 a4e5 85b6  ................
+000000a0: e698 afe4 baba e7b1 bbe7 9a84 e9a3 9fe7  ................
+000000b0: 89a9 e68a 95e5 9682 e4bc 91e6 81af e58c  ................
+000000c0: bae4 b8ad e79a 84e9 a9ac e584 bfe3 8082  ................
+000000d0: 220a 7d2c 0a20 207b 0a20 2020 2022 6576  ".},.  {.    "ev
+000000e0: 656e 745f 6e61 6d65 223a 22e8 b59b e9a9  ent_name":".....
+000000f0: ace5 9cba e4ba 8be4 bbb6 e7b0 bf32 222c  .............2",
+00000100: 0a20 2020 2022 7461 7267 6574 223a 302c  .    "target":0,
+00000110: 0a20 2020 2022 6465 7363 7269 6265 223a  .    "describe":
+00000120: 225b e8b5 9be9 a9ac e59c bae6 80aa e8b0  "[..............
+00000130: 885d 3c30 3ee7 9c8b e588 b0e4 ba86 e8b5  .]<0>...........
+00000140: 9be9 a9ac e59c bae7 9a84 e689 8be5 868c  ................
+00000150: efbc 9a33 2ee5 a682 e69e 9ce4 bda0 e79c  ...3............
+00000160: 8be5 88b0 e9a9 ace5 84bf e592 8ce4 bda0  ................
+00000170: e5af b9e8 a786 efbc 8ce8 afb7 e7ab 8be5  ................
+00000180: 88bb e8bd ace7 a7bb e8a7 86e7 babf 220a  ..............".
+00000190: 7d2c 0a20 2020 207b 0a20 2020 2022 6576  },.    {.    "ev
+000001a0: 656e 745f 6e61 6d65 223a 22e8 b59b e9a9  ent_name":".....
+000001b0: ace5 9cba e4ba 8be4 bbb6 e7b0 bf33 222c  .............3",
+000001c0: 0a20 2020 2022 7461 7267 6574 223a 302c  .    "target":0,
+000001d0: 0a20 2020 2022 6465 7363 7269 6265 223a  .    "describe":
+000001e0: 225b e8b5 9be9 a9ac e59c bae6 80aa e8b0  "[..............
+000001f0: 885d 3c30 3ee7 9c8b e588 b0e4 ba86 e8b5  .]<0>...........
+00000200: 9be9 a9ac e59c bae7 9a84 e689 8be5 868c  ................
+00000210: efbc 9a37 2ee5 9ca8 e8b5 9be9 a9ac e591  ...7............
+00000220: a8e8 beb9 e5b0 8fe9 93ba e4b8 adef bc8c  ................
+00000230: e688 91e4 bbac e4b8 8de4 bc9a e68f 90e4  ................
+00000240: be9b e4b8 94e4 bdbf e794 a8e5 908d e4b8  ................
+00000250: bae9 8791 e5b8 81e7 9a84 e5b0 8fe7 a1ac  ................
+00000260: e5b8 81ef bc8c e5a6 82e6 9e9c e58f 91e7  ................
+00000270: 8eb0 e5b7 a5e4 bd9c e4ba bae5 9198 e8af  ................
+00000280: a2e9 97ae e4bd a0e6 98af e590 a6e8 a681  ................
+00000290: e4bd bfe7 94a8 e987 91e5 b881 e585 91e6  ................
+000002a0: 8da2 e789 a9e5 9381 efbc 8ce8 afb7 e7ab  ................
+000002b0: 8be5 88bb e7a6 bbe5 bc80 e591 a8e8 beb9  ................
+000002c0: e5b0 8fe9 93ba efbc 8ce5 b9b6 e5af bbe6  ................
+000002d0: 89be e999 84e8 bf91 e79a 84e5 b7a5 e4bd  ................
+000002e0: 9ce4 baba e591 98e8 afb4 e698 8ee6 8385  ................
+000002f0: e586 b5e3 8082 220a 0a7d 2c0a 2020 7b0a  ......"..},.  {.
+00000300: 2020 2020 2265 7665 6e74 5f6e 616d 6522      "event_name"
+00000310: 3a22 e8b5 9be9 a9ac e59c bae4 ba8b e4bb  :"..............
+00000320: b6e7 b0bf 3422 2c0a 2020 2020 2274 6172  ....4",.    "tar
+00000330: 6765 7422 3a30 2c0a 2020 2020 2264 6573  get":0,.    "des
+00000340: 6372 6962 6522 3a22 5be8 b59b e9a9 ace5  cribe":"[.......
+00000350: 9cba e680 aae8 b088 5d3c 303e e79c 8be5  ........]<0>....
+00000360: 88b0 e4ba 86e8 b59b e9a9 ace5 9cba e79a  ................
+00000370: 84e6 898b e586 8cef bc9a 382e e8b5 9be9  ..........8.....
+00000380: a9ac e59c bae4 bbbb e4bd 95e4 b880 e4b8  ................
+00000390: aae6 af94 e8b5 9be5 8cba e59f 9fe5 8faa  ................
+000003a0: e4bc 9ae5 9ca8 393a 3030 2d31 313a 3030  ......9:00-11:00
+000003b0: e592 8c31 353a 3030 2d31 373a 3030 e5bc  ...15:00-17:00..
+000003c0: 80e6 94be efbc 8ce5 a682 e69e 9ce5 85b6  ................
+000003d0: e4bb 96e6 97b6 e997 b4e5 b7a5 e4bd 9ce4  ................
+000003e0: baba e591 98e6 8ea8 e88d 90e4 bda0 e589  ................
+000003f0: 8de5 be80 e8a7 82e7 9c8b e6af 94e8 b59b  ................
+00000400: efbc 8ce8 afb7 e4b8 8de8 a681 e78a b9e8  ................
+00000410: b1ab e79b b4e6 8ea5 e68b 92e7 bb9d e5b9  ................
+00000420: b6e8 bf9c e7a6 bbe6 ada4 e5b7 a5e4 bd9c  ................
+00000430: e4ba bae5 9198 e380 8222 0a7d 2c0a 2020  .........".},.  
+00000440: 7b0a 2020 2020 2265 7665 6e74 5f6e 616d  {.    "event_nam
+00000450: 6522 3a22 e8b5 9be9 a9ac e59c bae4 ba8b  e":"............
+00000460: e4bb b6e7 b0bf 3522 2c0a 2020 2020 2274  ......5",.    "t
+00000470: 6172 6765 7422 3a30 2c0a 2020 2020 2264  arget":0,.    "d
+00000480: 6573 6372 6962 6522 3a22 5be8 b59b e9a9  escribe":"[.....
+00000490: ace5 9cba e680 aae8 b088 5d3c 303e e68d  ..........]<0>..
+000004a0: a1e5 88b0 e4ba 86e4 b880 e4b8 aae8 b59b  ................
+000004b0: e9a9 ace5 9cba e689 8be5 868c e4b9 a6e3  ................
+000004c0: 8082 e58f afe4 bba5 e587 ade5 809f e8bf  ................
+000004d0: 99e6 9da1 e6b6 88e6 81af e689 be20 e8b5  ............. ..
+000004e0: abe5 b094 20e9 a286 e58f 9620 3ee8 b59b  .... ...... >...
+000004f0: e9a9 ace5 9cba e680 aae8 b088 e8a7 84e5  ................
+00000500: 8899 e696 87e6 a188 3c22 0a7d 2c0a 2020  ........<".},.  
+00000510: 7b0a 2020 2020 2265 7665 6e74 5f6e 616d  {.    "event_nam
+00000520: 6522 3a22 e8b5 9be9 a9ac e59c bae4 ba8b  e":"............
+00000530: e4bb b6e7 b0bf 3622 2c0a 2020 2020 2274  ......6",.    "t
+00000540: 6172 6765 7422 3a30 2c0a 2020 2020 2264  arget":0,.    "d
+00000550: 6573 6372 6962 6522 3a22 5be8 b59b e9a9  escribe":"[.....
+00000560: ace5 9cba e680 aae8 b088 5d3c 303e e6ad  ..........]<0>..
+00000570: a3e5 9ca8 e4bb 94e7 bb86 e998 85e8 afbb  ................
+00000580: e8b5 9be9 a9ac e59c bae6 898b e586 8cef  ................
+00000590: bc9a 3130 2ee5 a682 e69e 9ce5 8f91 e78e  ..10............
+000005a0: b0e5 91a8 e8be b9e6 9c89 e99b bee9 9cbe  ................
+000005b0: efbc 8ce8 afb7 e68c 89e7 85a7 e59c b0e5  ................
+000005c0: 9bbe e68c 87e7 a4ba e79a 84e8 b7af e5be  ................
+000005d0: 84e7 a6bb e5bc 80e8 b59b e9a9 ace5 9cba  ................
+000005e0: e380 8222 0a7d 2c0a 2020 7b0a 2020 2020  ...".},.  {.    
+000005f0: 2265 7665 6e74 5f6e 616d 6522 3a22 e8b5  "event_name":"..
+00000600: 9be9 a9ac e59c bae4 ba8b e4bb b6e7 b0bf  ................
+00000610: 3722 2c0a 2020 2020 2274 6172 6765 7422  7",.    "target"
+00000620: 3a30 2c0a 2020 2020 2264 6573 6372 6962  :0,.    "describ
+00000630: 6522 3a22 5be5 8aa8 e789 a9e5 9bad e8a7  e":"[...........
+00000640: 84e5 8899 e680 aae8 b088 5d3c 303e e59c  ..........]<0>..
+00000650: a8e8 b59b e9a9 ace5 9cba e79c 8be5 88b0  ................
+00000660: e4ba 86e7 99bd e889 b2e7 9a84 e5a4 a7e8  ................
+00000670: b1a1 e59c a8e6 b8b8 e6b3 b3e3 8082 e5bc  ................
+00000680: 80e5 a78b e680 80e7 9691 e887 aae5 b7b1  ................
+00000690: e698 afe8 b081 efbc 8128 33e5 9b9e e590  .........(3.....
+000006a0: 882d 327e 2b32 2922 2c0a 2020 2020 2272  .-2~+2)",.    "r
+000006b0: 6f75 6e64 7322 3a33 2c0a 2020 2020 226e  ounds":3,.    "n
+000006c0: 616d 6522 3a22 3f22 2c0a 2020 2020 226d  ame":"?",.    "m
+000006d0: 6f76 655f 6d61 7822 3a32 2c0a 2020 2020  ove_max":2,.    
+000006e0: 226d 6f76 655f 6d69 6e22 3a2d 320a 7d2c  "move_min":-2.},
+000006f0: 0a20 207b 0a20 2020 2022 6576 656e 745f  .  {.    "event_
+00000700: 6e61 6d65 223a 22e8 b59b e9a9 ace5 9cba  name":".........
+00000710: e4ba 8be4 bbb6 e7b0 bf38 222c 0a20 2020  .........8",.   
+00000720: 2022 7461 7267 6574 223a 302c 0a20 2020   "target":0,.   
+00000730: 2022 6465 7363 7269 6265 223a 225b e58a   "describe":"[..
+00000740: a8e7 89a9 e59b ade8 a784 e588 99e6 80aa  ................
+00000750: e8b0 885d 3c30 3ee5 9ca8 e8b5 9be9 a9ac  ...]<0>.........
+00000760: e59c bae5 8685 e58f 91e7 8eb0 e4ba 86e6  ................
+00000770: b0b4 e697 8fe9 a686 efbc 8153 616e e580  ...........San..
+00000780: bce7 96af e78b 82e4 b88b e999 8def bc81  ................
+00000790: e79b b4e6 8ea5 e980 80e5 9b9e e8b5 b7e7  ................
+000007a0: 82b9 efbc 8122 2c0a 2020 2020 226d 6f76  .....",.    "mov
+000007b0: 6522 3a2d 3130 300a 2020 7d2c 0a20 207b  e":-100.  },.  {
+000007c0: 0a20 2020 2022 6576 656e 745f 6e61 6d65  .    "event_name
+000007d0: 223a 22e8 b59b e9a9 ace5 9cba e4ba 8be4  ":".............
+000007e0: bbb6 e7b0 bf39 222c 0a20 2020 2022 7461  .....9",.    "ta
+000007f0: 7267 6574 223a 302c 0a20 2020 2022 6465  rget":0,.    "de
+00000800: 7363 7269 6265 223a 225b e58a a8e7 89a9  scribe":"[......
+00000810: e59b ade8 a784 e588 99e6 80aa e8b0 885d  ...............]
+00000820: 3c30 3ee5 9ca8 e8b5 9be9 a9ac e59c bae5  <0>.............
+00000830: 8685 e596 9de4 ba86 e585 94e5 ad90 e8a1  ................
+00000840: 80ef bc8c e590 83e4 ba86 e5b1 b1e7 be8a  ................
+00000850: e882 89e3 8082 e8a7 89e5 be97 e887 aae5  ................
+00000860: b7b1 e7aa 81e7 84b6 e585 85e6 bba1 e4ba  ................
+00000870: 86e5 8a9b e987 8fef bc81 e589 8de8 bf9b  ................
+00000880: 3522 2c0a 2020 2020 226d 6f76 6522 3a35  5",.    "move":5
+00000890: 0a20 207d 0a5d 0a                        .  }.].
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/events_main.py` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/events_main.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 ﻿import random
-from .horse import horse
-from .setting import  *
 from nonebot.log import logger
 
+from ..config import setting_random_min_length, setting_random_max_length
+
+
 def event_main(race, horse_i, event, event_delay_key = 0):
     try:
     #读取 event_name
         event_name = event["event_name"]
     #该马儿是否死亡/离开/眩晕，死亡则结束事件链
         if race.player[horse_i].is_die() == True and event_delay_key == 0:
             return f''
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/horse.py` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/horse.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 ﻿import random
-from .setting import  *
+
+from ..config import setting_track_length, base_move_min, base_move_max
 
 class horse:
     def __init__(self, horsename = "the_horse", uid = 0, id = "the_player", location = 0, round = 0 ):
         self.horse = horsename
         self.playeruid = uid
         self.player =  id
         self.buff = []
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/menu_data.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/menu_data.json`

 * *Format-specific differences are supported for JSON files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: JSON text data*

 * *Files 8% similar despite different names*

```diff
@@ -1,714 +1,705 @@
 00000000: 5b0d 0a20 2020 207b 0d0a 2020 2020 2020  [..    {..      
-00000010: 2020 2266 756e 6322 3a20 22e8 8eb7 e58f    "func": ".....
-00000020: 96e9 8791 e5b8 8122 2c0d 0a20 2020 2020  .......",..     
-00000030: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
-00000040: 6f64 223a 2022 312e e987 91e5 b881 e7ad  od": "1.........
-00000050: bee5 88b0 2032 2ee9 878d e7bd aee7 adbe  .... 2..........
-00000060: e588 b022 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00000070: 7472 6967 6765 725f 636f 6e64 6974 696f  trigger_conditio
-00000080: 6e22 3a20 22e6 97a0 222c 0d0a 2020 2020  n": "...",..    
-00000090: 2020 2020 2262 7269 6566 5f64 6573 223a      "brief_des":
-000000a0: 2022 e88e b7e5 8f96 e987 91e5 b881 222c   "............",
-000000b0: 0d0a 2020 2020 2020 2020 2264 6574 6169  ..        "detai
-000000c0: 6c5f 6465 7322 3a20 22e9 8791 e5b8 81e7  l_des": ".......
-000000d0: adbe e588 b0ef bc9a 5c6e e78e a9e5 aeb6  ........\n......
-000000e0: e6af 8fe6 97a5 e58f afe7 adbe e588 b0e4  ................
-000000f0: b880 e6ac a1ef bc8c e6af 8fe6 97a5 30e7  ..............0.
-00000100: 82b9 e588 b7e6 96b0 e380 825c 6ee9 878d  ...........\n...
-00000110: e7bd aee7 adbe e588 b0ef bc9a 5c6e e6af  ............\n..
-00000120: 8fe6 aca1 e987 8de7 bdae e590 8ee5 8faf  ................
-00000130: e9a2 86e5 8f96 e4b8 80e6 aca1 e380 8222  ..............."
-00000140: 0d0a 2020 2020 7d2c 0d0a 2020 2020 7b0d  ..    },..    {.
-00000150: 0a20 2020 2020 2020 2022 6675 6e63 223a  .        "func":
-00000160: 2022 e58f 91e8 b5b7 e987 8de7 bdae 222c   "............",
-00000170: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
-00000180: 6572 5f6d 6574 686f 6422 3a20 22e5 8f91  er_method": "...
-00000190: e8b5 b7e9 878d e7bd ae22 2c0d 0a20 2020  .........",..   
-000001a0: 2020 2020 2022 7472 6967 6765 725f 636f       "trigger_co
-000001b0: 6e64 6974 696f 6e22 3a20 22e6 97a0 222c  ndition": "...",
-000001c0: 0d0a 2020 2020 2020 2020 2262 7269 6566  ..        "brief
-000001d0: 5f64 6573 223a 2022 e6b8 85e7 a9ba e589  _des": "........
-000001e0: 8de5 8d81 e590 8de7 9a84 e987 91e5 b881  ................
-000001f0: e380 8222 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00000200: 6465 7461 696c 5f64 6573 223a 2022 e5bd  detail_des": "..
-00000210: 93e9 8791 e5b8 81e6 8e92 e8a1 8ce6 a69c  ................
-00000220: e7ac ace4 b880 e590 8de7 9a84 e987 91e5  ................
-00000230: b881 e8b6 85e8 bf87 e7ac ace4 ba8c e590  ................
-00000240: 8de5 88b0 e7ac ace5 8d81 e590 8de7 9a84  ................
-00000250: e680 bbe5 928c efbc 8ce5 8faf e4bb a5e5  ................
-00000260: 8f91 e8b5 b7e9 878d e7bd aee3 8082 220d  ..............".
-00000270: 0a20 2020 207d 2c0d 0a20 2020 207b 0d0a  .    },..    {..
-00000280: 2020 2020 2020 2020 2266 756e 6322 3a20          "func": 
-00000290: 22e4 b8aa e4ba bae8 b4a6 e688 b722 2c0d  "............",.
-000002a0: 0a20 2020 2020 2020 2022 7472 6967 6765  .        "trigge
-000002b0: 725f 6d65 7468 6f64 223a 2022 312e e688  r_method": "1...
-000002c0: 91e7 9a84 e987 91e5 b881 2032 2ee6 8891  .......... 2....
-000002d0: e79a 84e4 bb93 e5ba 9320 332e e688 91e7  ......... 3.....
-000002e0: 9a84 e8b5 84e6 9699 e58d a122 2c0d 0a20  ...........",.. 
-000002f0: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
-00000300: 636f 6e64 6974 696f 6e22 3a20 22e6 97a0  condition": "...
-00000310: 222c 0d0a 2020 2020 2020 2020 2262 7269  ",..        "bri
-00000320: 6566 5f64 6573 223a 2022 e69f a5e7 9c8b  ef_des": "......
-00000330: e4b8 aae4 baba e8b4 a6e6 88b7 e8b5 84e6  ................
-00000340: 9699 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
-00000350: 6574 6169 6c5f 6465 7322 3a20 22e6 8891  etail_des": "...
-00000360: e79a 84e9 8791 e5b8 81ef bc9a 5c6e e69f  ............\n..
-00000370: a5e7 9c8b e887 aae5 b7b1 e79a 84e9 8791  ................
-00000380: e5b8 81e6 95b0 e987 8f5c 6ee6 8891 e79a  .........\n.....
-00000390: 84e4 bb93 e5ba 93ef bc9a 5c6e e69f a5e7  ..........\n....
-000003a0: 9c8b e887 aae5 b7b1 e88e b7e5 be97 e79a  ................
-000003b0: 84e7 9a84 e981 93e5 85b7 5c6e e688 91e7  ..........\n....
-000003c0: 9a84 e8b5 84e6 9699 e58d a1ef bc9a 5c6e  ..............\n
-000003d0: e69f a5e7 9c8b e4b8 aae4 baba e8b4 a6e6  ................
-000003e0: 88b7 e8af a6e7 bb86 e8b5 84e6 9699 5c6e  ..............\n
-000003f0: e688 91e7 9a84 e8b5 84e4 baa7 efbc 9a5c  ...............\
-00000400: 6ee6 9fa5 e79c 8be8 87aa e5b7 b1e7 9a84  n...............
-00000410: e585 a8e5 b180 e8b5 84e4 baa7 e588 86e5  ................
-00000420: b883 220d 0a20 2020 207d 2c0d 0a20 2020  .."..    },..   
-00000430: 207b 0d0a 2020 2020 2020 2020 2266 756e   {..        "fun
-00000440: 6322 3a20 22e5 8f91 e7ba a2e5 8c85 222c  c": ".........",
-00000450: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
-00000460: 6572 5f6d 6574 686f 6422 3a20 22e5 8f91  er_method": "...
-00000470: e7ba a2e5 8c85 20e3 8090 e987 91e9 a29d  ...... .........
-00000480: e380 9120 e380 9061 74e3 8091 222c 0d0a  ... ...at...",..
-00000490: 2020 2020 2020 2020 2274 7269 6767 6572          "trigger
-000004a0: 5f63 6f6e 6469 7469 6f6e 223a 2022 e697  _condition": "..
-000004b0: a022 2c0d 0a20 2020 2020 2020 2022 6272  .",..        "br
-000004c0: 6965 665f 6465 7322 3a20 22e7 bb99 6174  ief_des": "...at
-000004d0: e79a 84e7 94a8 e688 b7e5 8f91 e987 91e5  ................
-000004e0: b881 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
-000004f0: 6574 6169 6c5f 6465 7322 3a20 2222 0d0a  etail_des": ""..
-00000500: 2020 2020 7d2c 0d0a 2020 2020 7b0d 0a20      },..    {.. 
-00000510: 2020 2020 2020 2022 6675 6e63 223a 2022         "func": "
-00000520: e980 81e9 8193 e585 b722 2c0d 0a20 2020  .........",..   
-00000530: 2020 2020 2022 7472 6967 6765 725f 6d65       "trigger_me
-00000540: 7468 6f64 223a 2022 e980 81e9 8193 e585  thod": "........
-00000550: b720 e380 90e9 8193 e585 b7e5 908d e380  . ..............
-00000560: 9120 e380 90e9 8193 e585 b7e6 95b0 e987  . ..............
-00000570: 8fe3 8091 20e3 8090 6174 e380 9122 2c0d  .... ...at...",.
-00000580: 0a20 2020 2020 2020 2022 7472 6967 6765  .        "trigge
-00000590: 725f 636f 6e64 6974 696f 6e22 3a20 22e6  r_condition": ".
-000005a0: 97a0 222c 0d0a 2020 2020 2020 2020 2262  ..",..        "b
-000005b0: 7269 6566 5f64 6573 223a 2022 e7bb 9961  rief_des": "...a
-000005c0: 74e7 9a84 e794 a8e6 88b7 e980 81e9 8193  t...............
-000005d0: e585 b722 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-000005e0: 6465 7461 696c 5f64 6573 223a 2022 e58f  detail_des": "..
-000005f0: afe4 bba5 e4b8 8de5 a1ab e981 93e5 85b7  ................
-00000600: e695 b0e9 878f efbc 8ce9 bb98 e8ae a4e4  ................
-00000610: b8ba 3122 0d0a 2020 2020 7d2c 0d0a 2020  ..1"..    },..  
-00000620: 2020 7b0d 0a20 2020 2020 2020 2022 6675    {..        "fu
-00000630: 6e63 223a 2022 e987 91e5 b881 e8bd ace7  nc": "..........
-00000640: a7bb 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
-00000650: 7269 6767 6572 5f6d 6574 686f 6422 3a20  rigger_method": 
-00000660: 22e9 8791 e5b8 81e8 bdac e7a7 bb20 e380  "............ ..
-00000670: 90e5 85ac e58f b8e5 908d e380 9120 e380  ............. ..
-00000680: 90e9 8791 e9a2 9de3 8091 222c 0d0a 2020  ..........",..  
-00000690: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
-000006a0: 6f6e 6469 7469 6f6e 223a 2022 e8bd ace7  ondition": "....
-000006b0: a7bb e79b aee6 a087 e5b7 b2e6 b3a8 e586  ................
-000006c0: 8ce5 85ac e58f b8e3 8082 222c 0d0a 2020  ..........",..  
-000006d0: 2020 2020 2020 2262 7269 6566 5f64 6573        "brief_des
-000006e0: 223a 2022 e8b7 a8e7 bea4 e8bd ace7 a7bb  ": "............
-000006f0: e987 91e5 b881 222c 0d0a 2020 2020 2020  ......",..      
-00000700: 2020 2264 6574 6169 6c5f 6465 7322 3a20    "detail_des": 
-00000710: 22e8 bdac e7a7 bbe7 9bae e6a0 87e5 b7b2  "...............
-00000720: e6b3 a8e5 868c e585 ace5 8fb8 efbc 8ce4  ................
-00000730: bda0 e59c a8e7 9bae e6a0 87e7 bea4 e586  ................
-00000740: 85e6 9c89 e8b4 a6e6 88b7 e380 8222 0d0a  ............."..
-00000750: 2020 2020 7d2c 0d0a 2020 2020 7b0d 0a20      },..    {.. 
-00000760: 2020 2020 2020 2022 6675 6e63 223a 2022         "func": "
-00000770: e68a bde5 8da1 222c 0d0a 2020 2020 2020  ......",..      
-00000780: 2020 2274 7269 6767 6572 5f6d 6574 686f    "trigger_metho
-00000790: 6422 3a20 22e5 8d95 e68a bd5c 2f31 30e8  d": "......\/10.
-000007a0: bf9e 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
-000007b0: 7269 6767 6572 5f63 6f6e 6469 7469 6f6e  rigger_condition
-000007c0: 223a 2022 e99c 80e8 a681 4062 6f74 e688  ": "......@bot..
-000007d0: 96e5 8fab 626f 74e7 9a84 e590 8de5 ad97  ....bot.........
-000007e0: e380 8222 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-000007f0: 6272 6965 665f 6465 7322 3a20 22e8 8eb7  brief_des": "...
-00000800: e58f 96e9 8193 e585 b75c 6ee5 8faf e68c  .........\n.....
-00000810: 87e5 ae9a e68a bde5 8da1 e6ac a1e6 95b0  ................
-00000820: 5c6e e4be 8be5 a682 efbc 9a20 4062 6f74  \n......... @bot
-00000830: 2033 30e8 bf9e 222c 0d0a 2020 2020 2020   30...",..      
-00000840: 2020 2264 6574 6169 6c5f 6465 7322 3a20    "detail_des": 
-00000850: 22e9 8193 e585 b7e5 8886 e4b8 bae5 85a8  "...............
-00000860: e5b1 80e9 8193 e585 b7e5 928c e7be a4e5  ................
-00000870: 8685 e981 93e5 85b7 5c6e e4b9 9fe5 8faf  ........\n......
-00000880: e588 86e4 b8ba e6b0 b8e4 b985 e981 93e5  ................
-00000890: 85b7 e592 8ce6 97b6 e695 88e9 8193 e585  ................
-000008a0: b75c 6ee6 97b6 e695 88e9 8193 e585 b7e6  .\n.............
-000008b0: 9c80 e995 bfe5 8fa0 e58a a037 e5a4 a95c  ...........7...\
-000008c0: 6ee6 b0b8 e4b9 85e9 8193 e585 b7e6 9c80  n...............
-000008d0: e5a4 9ae5 8fa0 3130 e4b8 aa5c 6ee9 83a8  ......10...\n...
-000008e0: e588 86e9 8193 e585 b7e5 8faf e4bd bfe7  ................
-000008f0: 94a8 efbc 9a5c 6ee4 bdbf e794 a8e6 96b9  .....\n.........
-00000900: e6b3 95ef bc9a e4bd bfe7 94a8 e981 93e5  ................
-00000910: 85b7 20e3 8090 e981 93e5 85b7 e590 8de3  .. .............
-00000920: 8091 20e3 8090 e695 b0e9 878f 5c2f e58f  .. .........\/..
-00000930: 82e6 95b0 e380 9122 0d0a 2020 2020 7d2c  ......."..    },
-00000940: 0d0a 2020 2020 7b0d 0a20 2020 2020 2020  ..    {..       
-00000950: 2022 6675 6e63 223a 2022 e4bd bfe7 94a8   "func": "......
-00000960: e981 93e5 85b7 222c 0d0a 2020 2020 2020  ......",..      
-00000970: 2020 2274 7269 6767 6572 5f6d 6574 686f    "trigger_metho
-00000980: 6422 3a20 22e4 bdbf e794 a8e9 8193 e585  d": "...........
-00000990: b720 e380 90e9 8193 e585 b7e5 908d e380  . ..............
-000009a0: 9120 e380 90e6 95b0 e987 8f5c 2fe5 8f82  . .........\/...
-000009b0: e695 b0e3 8091 222c 0d0a 2020 2020 2020  ......",..      
-000009c0: 2020 2274 7269 6767 6572 5f63 6f6e 6469    "trigger_condi
-000009d0: 7469 6f6e 223a 2022 e697 a022 2c0d 0a20  tion": "...",.. 
-000009e0: 2020 2020 2020 2022 6272 6965 665f 6465         "brief_de
-000009f0: 7322 3a20 22e9 83a8 e588 86e9 8193 e585  s": "...........
-00000a00: b7e6 97a0 e6b3 95e4 bdbf e794 a822 2c0d  .............",.
-00000a10: 0a20 2020 2020 2020 2022 6465 7461 696c  .        "detail
-00000a20: 5f64 6573 223a 2022 220d 0a20 2020 207d  _des": ""..    }
-00000a30: 2c0d 0a20 2020 207b 0d0a 2020 2020 2020  ,..    {..      
-00000a40: 2020 2266 756e 6322 3a20 22e6 8e92 e8a1    "func": ".....
-00000a50: 8ce6 a69c 222c 0d0a 2020 2020 2020 2020  ....",..        
-00000a60: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
-00000a70: 3a20 22e9 8791 e5b8 81e6 8e92 e8a1 8c22  : "............"
-00000a80: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
-00000a90: 6765 725f 636f 6e64 6974 696f 6e22 3a20  ger_condition": 
-00000aa0: 22e6 97a0 222c 0d0a 2020 2020 2020 2020  "...",..        
-00000ab0: 2262 7269 6566 5f64 6573 223a 2022 e69f  "brief_des": "..
-00000ac0: a5e7 9c8b e68e 92e8 a18c e6a6 9c22 2c0d  .............",.
-00000ad0: 0a20 2020 2020 2020 2022 6465 7461 696c  .        "detail
-00000ae0: 5f64 6573 223a 2022 e987 91e5 b881 e68e  _des": "........
-00000af0: 92e8 a18c 5c6e e883 9ce5 9cba e68e 92e8  ....\n..........
-00000b00: a18c 5c6e e8b4 a5e5 9cba e68e 92e8 a18c  ..\n............
-00000b10: 5c6e e6ac a7e6 b4b2 e4ba bae6 8e92 e8a1  \n..............
-00000b20: 8c5c 6ee6 8588 e596 84e5 aeb6 e68e 92e8  .\n.............
-00000b30: a18c 5c6e e69f a5e7 9c8b e8b7 afe7 81af  ..\n............
-00000b40: e68c 82e4 bbb6 220d 0a20 2020 207d 2c0d  ......"..    },.
-00000b50: 0a20 2020 207b 0d0a 2020 2020 2020 2020  .    {..        
-00000b60: 2266 756e 6322 3a20 22e8 bf9e e68e a5e8  "func": ".......
-00000b70: b4a6 e688 b722 2c0d 0a20 2020 2020 2020  .....",..       
-00000b80: 2022 7472 6967 6765 725f 6d65 7468 6f64   "trigger_method
-00000b90: 223a 2022 312e e7be a4e5 8685 efbc 9a40  ": "1..........@
-00000ba0: 626f 74e5 85b3 e881 94e8 b4a6 e688 b720  bot............ 
-00000bb0: 322e e7a7 81e8 818a efbc 9ae5 85b3 e881  2...............
-00000bc0: 94e8 b4a6 e688 b75c 6e22 2c0d 0a20 2020  .......\n",..   
-00000bd0: 2020 2020 2022 7472 6967 6765 725f 636f       "trigger_co
-00000be0: 6e64 6974 696f 6e22 3a20 22e6 97a0 222c  ndition": "...",
-00000bf0: 0d0a 2020 2020 2020 2020 2262 7269 6566  ..        "brief
-00000c00: 5f64 6573 223a 2022 e7a7 81e8 818a e68c  _des": "........
-00000c10: 87e4 bba4 e585 b3e8 8194 e588 b0e7 bea4  ................
-00000c20: e380 8222 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00000c30: 6465 7461 696c 5f64 6573 223a 2022 e4bd  detail_des": "..
-00000c40: a0e5 8faf e4bb a5e5 9ca8 e7a7 81e8 818a  ................
-00000c50: e5ae 8ce6 8890 e4bb a5e4 b88b e693 8de4  ................
-00000c60: bd9c efbc 9a5c 6ee7 adbe e588 b05c 6ee6  .....\n......\n.
-00000c70: 8abd e58d a15c 6ee6 9fa5 e79c 8be4 b8aa  .....\n.........
-00000c80: e4ba bae8 b4a6 e688 b7ef bc9a 5c6e e69f  ............\n..
-00000c90: a5e7 9c8b e68e 92e8 a18c 5c6e e8b4 ade4  ..........\n....
-00000ca0: b9b0 e688 96e7 bb93 e7ae 97e8 82a1 e7a5  ................
-00000cb0: a822 0d0a 2020 2020 7d2c 0d0a 2020 2020  ."..    },..    
-00000cc0: 7b0d 0a20 2020 2020 2020 2022 6675 6e63  {..        "func
-00000cd0: 223a 2022 e4bf 84e7 bd97 e696 afe8 bdae  ": "............
-00000ce0: e79b 9822 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00000cf0: 7472 6967 6765 725f 6d65 7468 6f64 223a  trigger_method":
-00000d00: 2022 e8a3 85e5 bcb9 20e3 8090 e5ad 90e5   "...... .......
-00000d10: bcb9 e695 b0e3 8091 20e3 8090 e987 91e9  ........ .......
-00000d20: a29d e380 9120 e380 9061 74e3 8091 222c  ..... ...at...",
-00000d30: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
-00000d40: 6572 5f63 6f6e 6469 7469 6f6e 223a 2022  er_condition": "
-00000d50: e8b5 8ce6 b3a8 e4b8 8ae9 9990 e4b8 bae4  ................
-00000d60: b880 e580 8de8 b58c e6b3 a8e4 b88a e999  ................
-00000d70: 9022 2c0d 0a20 2020 2020 2020 2022 6272  .",..        "br
-00000d80: 6965 665f 6465 7322 3a20 22e5 8f91 e8b5  ief_des": ".....
-00000d90: b7e4 bf84 e7bd 97e6 96af e8bd aee7 9b98  ................
-00000da0: 222c 0d0a 2020 2020 2020 2020 2264 6574  ",..        "det
-00000db0: 6169 6c5f 6465 7322 3a20 22e9 809a e8bf  ail_des": ".....
-00000dc0: 8720 e8a3 85e5 bcb9 20e6 9da5 e5af b9e5  . ...... .......
-00000dd0: 85b6 e4bb 96e4 baba e58f 91e8 b5b7 e586  ................
-00000de0: b3e6 9697 5c6e e4b8 8d40 e588 99e6 8980  ....\n...@......
-00000df0: e69c 89e7 bea4 e58f 8be9 83bd e58f afe6  ................
-00000e00: 8ea5 e58f 975c 6ee8 bdae e6b5 81e5 bc80  .....\n.........
-00000e10: e69e aaef bc8c e79b b4e5 88b0 e8bf 90e6  ................
-00000e20: b094 e4b8 8de5 a5bd e79a 84e4 baba e585  ................
-00000e30: 88e5 8ebb e4b8 96e3 8082 5c6e e380 90e7  ..........\n....
-00000e40: 89b9 e6ae 8ae6 8a80 e883 bde3 8091 efbc  ................
-00000e50: 9ae5 bc80 e69e aa30 5c6e 5c6e e380 90e5  .......0\n\n....
-00000e60: bc80 e5a7 8be6 b8b8 e688 8fe3 8091 5c6e  ..............\n
-00000e70: e8a3 85e5 bcb9 20e3 8090 e5ad 90e5 bcb9  ...... .........
-00000e80: e695 b0e3 8091 20e3 8090 e987 91e9 a29d  ...... .........
-00000e90: e380 9120 e380 9061 74e3 8091 efbc 88e4  ... ...at.......
-00000ea0: b8ba e7a9 bae5 8899 e689 80e6 9c89 e7be  ................
-00000eb0: a4e5 8f8b e983 bde5 8faf e68e a5e5 8f97  ................
-00000ec0: efbc 895c 6ee3 8090 e59b 9ee5 ba94 e380  ...\n...........
-00000ed0: 915c 6ee6 8ea5 e58f 97e6 8c91 e688 985c  .\n............\
-00000ee0: 2fe6 8b92 e7bb 9de6 8c91 e688 985c 6ee3  /............\n.
-00000ef0: 8090 e59b 9ee5 9088 e4b8 ade3 8091 5c6e  ..............\n
-00000f00: e5bc 80e6 9eaa 5c2f e592 945c 2fe5 98ad  ......\/...\/...
-00000f10: 5c2f e598 a320 5be5 ad90 e5bc b9e6 95b0  \/... [.........
-00000f20: 5def bc88 e9bb 98e8 aea4 3129 efbc 88e8  ].........1)....
-00000f30: bdae e6b5 81e5 bc80 e69e aaef bc89 5c6e  ..............\n
-00000f40: e380 90e7 bb93 e7ae 97e3 8091 5c6e e7bb  ............\n..
-00000f50: 93e7 ae97 20ef bc88 e5bd 93e6 9f90 e4b8  .... ...........
-00000f60: 80e6 96b9 3630 e7a7 92e6 9caa e5bc 80e6  ....60..........
-00000f70: 9eaa efbc 8ce5 8faf e4bd bfe7 94a8 e8af  ................
-00000f80: a5e5 91bd e4bb a4e7 bb93 e69d 9fe5 afb9  ................
-00000f90: e586 b3e5 b9b6 e883 9ce5 88a9 efbc 8922  ..............."
-00000fa0: 0d0a 2020 2020 7d2c 0d0a 2020 2020 7b0d  ..    },..    {.
-00000fb0: 0a20 2020 2020 2020 2022 6675 6e63 223a  .        "func":
-00000fc0: 2022 e68e b7e9 aab0 e5ad 9022 2c0d 0a20   ".........",.. 
-00000fd0: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
-00000fe0: 6d65 7468 6f64 223a 2022 e691 87e9 aab0  method": "......
-00000ff0: e5ad 905c 2fe6 8eb7 e889 b2e5 ad90 20e3  ...\/......... .
-00001000: 8090 e987 91e9 a29d e380 9120 e380 9061  ........... ...a
-00001010: 74e3 8091 222c 0d0a 2020 2020 2020 2020  t...",..        
-00001020: 2274 7269 6767 6572 5f63 6f6e 6469 7469  "trigger_conditi
-00001030: 6f6e 223a 2022 e8b5 8ce6 b3a8 e4b8 8ae9  on": "..........
-00001040: 9990 e4b8 bae4 ba94 e580 8de8 b58c e6b3  ................
-00001050: a8e4 b88a e999 9022 2c0d 0a20 2020 2020  .......",..     
-00001060: 2020 2022 6272 6965 665f 6465 7322 3a20     "brief_des": 
-00001070: 22e5 8f91 e8b5 b7e6 8eb7 e9aa b0e5 ad90  "...............
-00001080: 222c 0d0a 2020 2020 2020 2020 2264 6574  ",..        "det
-00001090: 6169 6c5f 6465 7322 3a20 22e9 809a e8bf  ail_des": ".....
-000010a0: 8720 e68e b7e9 aab0 e5ad 9020 e69d a5e5  . ......... ....
-000010b0: afb9 e585 b6e4 bb96 e4ba bae5 8f91 e8b5  ................
-000010c0: b7e5 86b3 e696 975c 6ee8 bdae e6b5 81e5  .......\n.......
-000010d0: bc80 e695 b0e6 af94 e5a4 a7e5 b08f 5c6e  ..............\n
-000010e0: e4b8 ade9 8094 e58f afe7 bb93 e69d 9f5c  ...............\
-000010f0: 6ee8 bdae e6b5 81e5 bc80 e695 b0ef bc8c  n...............
-00001100: e585 88e6 af94 e7bb 84e5 9088 efbc 8ce5  ................
-00001110: 868d e6af 94e7 82b9 e695 b0e3 8082 5c6e  ..............\n
-00001120: e7bb 84e5 9088 efbc 9a5c 6ee5 bdb9 e6bb  .........\n.....
-00001130: a120 3e20 e4b8 b220 3e20 e69d a120 3e20  . > ... > ... > 
-00001140: e4b8 a4e5 afb9 203e 20e5 afb9 203e 20e6  ...... > ... > .
-00001150: 95a3 5c6e 5c6e e380 90e5 bc80 e5a7 8be6  ..\n\n..........
-00001160: b8b8 e688 8fe3 8091 5c6e e691 87e9 aab0  ........\n......
-00001170: e5ad 905c 2fe6 8eb7 e889 b2e5 ad90 20e3  ...\/......... .
-00001180: 8090 e987 91e9 a29d e380 9120 e380 9061  ........... ...a
-00001190: 74e3 8091 efbc 88e4 b8ba e7a9 bae5 8899  t...............
-000011a0: e689 80e6 9c89 e7be a4e5 8f8b e983 bde5  ................
-000011b0: 8faf e68e a5e5 8f97 efbc 895c 6ee3 8090  ...........\n...
-000011c0: e59b 9ee5 ba94 e380 915c 6ee6 8ea5 e58f  .........\n.....
-000011d0: 97e6 8c91 e688 985c 2fe6 8b92 e7bb 9de6  .......\/.......
-000011e0: 8c91 e688 985c 6ee3 8090 e59b 9ee5 9088  .....\n.........
-000011f0: e4b8 ade3 8091 5c6e e5bc 80e6 95b0 5c2f  ......\n......\/
-00001200: e5bc 80e7 82b9 5c2f e58f 96e5 87ba efbc  ......\/........
-00001210: 88e8 bdae e6b5 81e5 bc80 e695 b0ef bc89  ................
-00001220: 5c6e e380 90e7 bb93 e69d 9fe3 8091 5c6e  \n............\n
-00001230: e7bb 93e6 9d9f efbc 88e5 8faa e69c 89e6  ................
-00001240: 9a82 e8b4 a5e6 96b9 e58f afe5 8f91 e8b5  ................
-00001250: b7ef bc89 5c6e e380 90e7 bb93 e7ae 97e3  ....\n..........
-00001260: 8091 5c6e e7bb 93e7 ae97 efbc 88e5 bd93  ..\n............
-00001270: e69f 90e4 b880 e696 b936 30e7 a792 e6b2  .........60.....
-00001280: a1e6 9c89 e59b 9ee5 ba94 efbc 8ce4 bba5  ................
-00001290: e79b aee5 898d e6af 94e5 8886 e7bb 93e7  ................
-000012a0: ae97 efbc 8922 0d0a 2020 2020 7d2c 0d0a  ....."..    },..
-000012b0: 2020 2020 7b0d 0a20 2020 2020 2020 2022      {..        "
-000012c0: 6675 6e63 223a 2022 e689 91e5 858b e5af  func": "........
-000012d0: b9e6 8898 222c 0d0a 2020 2020 2020 2020  ....",..        
-000012e0: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
-000012f0: 3a20 22e6 8991 e585 8be5 afb9 e688 9820  : "............ 
-00001300: e380 90e9 8791 e9a2 9de3 8091 20e3 8090  ............ ...
-00001310: 6174 e380 9122 2c0d 0a20 2020 2020 2020  at...",..       
-00001320: 2022 7472 6967 6765 725f 636f 6e64 6974   "trigger_condit
-00001330: 696f 6e22 3a20 22e8 b58c e6b3 a8e4 b88a  ion": ".........
-00001340: e999 90e4 b8ba e4b8 80e5 808d e8b5 8ce6  ................
-00001350: b3a8 e4b8 8ae9 9990 222c 0d0a 2020 2020  ........",..    
-00001360: 2020 2020 2262 7269 6566 5f64 6573 223a      "brief_des":
-00001370: 2022 e58f 91e8 b5b7 e689 91e5 858b e5af   "..............
-00001380: b9e6 8898 222c 0d0a 2020 2020 2020 2020  ....",..        
-00001390: 2264 6574 6169 6c5f 6465 7322 3a20 22e9  "detail_des": ".
-000013a0: 809a e8bf 8720 e689 91e5 858b e5af b9e6  ..... ..........
-000013b0: 8898 20e6 9da5 e5af b9e5 85b6 e4bb 96e4  .. .............
-000013c0: baba e5af b9e6 8898 5c6e e689 93e5 87ba  ........\n......
-000013d0: e887 aae5 b7b1 e79a 84e6 898b e789 8c5c  ...............\
-000013e0: 6ee5 bd93 e5af b9e6 96b9 e79a 84e8 a180  n...............
-000013f0: e987 8fe5 b08f e4ba 8e31 e688 96e8 8085  .........1......
-00001400: e59c a8e8 87aa e5b7 b1e5 9b9e e590 88e5  ................
-00001410: 87ba e789 8ce5 898d e8a1 80e9 878f 3e34  ..............>4
-00001420: 30e5 8db3 e58f afe8 8eb7 e883 9c5c 6ee7  0............\n.
-00001430: 898c e5ba 93e4 b880 e585 b135 32e5 bca0  ...........52...
-00001440: e789 8cef bc8c e5bd 93e7 898c e5ba 93e6  ................
-00001450: b2a1 e69c 89e7 898c e4ba 86e5 b0b1 e4bb  ................
-00001460: a5e7 9bae e589 8de8 a180 e987 8fe7 bb93  ................
-00001470: e7ae 97ef bc8c e7bb 93e6 9d9f e6b8 b8e6  ................
-00001480: 888f e380 825c 6e5c 6ee5 8588 e689 8be5  .....\n\n.......
-00001490: 889d e5a7 8be7 82b9 e695 b0ef bc9a 4850  ..............HP
-000014a0: 2032 3020 5350 2030 2044 4546 2030 5c6e   20 SP 0 DEF 0\n
-000014b0: e590 8ee6 898b e588 9de5 a78b e782 b9e6  ................
-000014c0: 95b0 efbc 9a48 5020 3235 2053 5020 3220  .....HP 25 SP 2 
-000014d0: 4445 4620 305c 6ee6 af8f e59b 9ee5 9088  DEF 0\n.........
-000014e0: e68a bde4 b889 e5bc a0e7 898c efbc 8ce6  ................
-000014f0: 8993 e587 bae5 85b6 e4b8 ade7 9a84 e4b8  ................
-00001500: 80e5 bca0 e4bd 9ce4 b8ba e8a1 8ce5 8aa8  ................
-00001510: e789 8cef bc8c e5bc 83e6 8e89 e589 a9e4  ................
-00001520: bd99 e689 8be7 898c e380 825c 6eef bc88  ...........\n...
-00001530: e789 b9e5 88ab e6b3 a8e6 848f efbc 9ae9  ................
-00001540: 98b2 e5be a1e7 898c e4bd 9ce4 b8ba e8a1  ................
-00001550: 8ce5 8aa8 e789 8ce6 98af e694 bbe5 87bb  ................
-00001560: efbc 895c 6ee4 b98b e590 8ee5 afb9 e696  ...\n...........
-00001570: b9e6 9187 e4b8 80e4 b8aa 3230 e99d a2e9  ..........20....
-00001580: aab0 e5ad 90ef bc8c 5c6e e5a6 82e6 9e9c  ........\n......
-00001590: e782 b9e6 95b0 e5b0 8fe4 ba8e e5af b9e6  ................
-000015a0: 96b9 5350 e588 99e4 bb8e e789 8ce5 ba93  ..SP............
-000015b0: e7bf bbe5 87ba e4b8 80e5 bca0 e789 8ce4  ................
-000015c0: bd9c e4b8 bae6 8a80 e883 bde7 898c e689  ................
-000015d0: 93e5 87ba e380 825c 6ee6 8c89 e785 a7e6  .......\n.......
-000015e0: 8a80 e883 bde7 898c e782 b9e6 95b0 e689  ................
-000015f0: a3e9 99a4 e5af b9e6 96b9 5350 e782 b9e3  ..........SP....
-00001600: 8082 5c6e 5c6e 3c66 7420 7369 7a65 3d33  ..\n\n<ft size=3
-00001610: 3020 636f 6c6f 723d 626c 6163 6b3e e9bb  0 color=black>..
-00001620: 91e6 a183 3c5c 2f66 743e 5c6e e68f 8fe8  ....<\/ft>\n....
-00001630: bfb0 efbc 9ae9 98b2 e5be a15c 6ee8 a18c  ...........\n...
-00001640: e58a a8e7 898c e695 88e6 9e9c efbc 9ae6  ................
-00001650: 8993 e587 bae6 94bb e587 bb5c 6ee6 8a80  ...........\n...
-00001660: e883 bde7 898c e695 88e6 9e9c efbc 9ae5  ................
-00001670: a29e e58a a044 4546 5c6e 3c66 7420 7369  .....DEF\n<ft si
-00001680: 7a65 3d33 3020 636f 6c6f 723d 7265 643e  ze=30 color=red>
-00001690: e7ba a2e6 a183 3c5c 2f66 743e 5c6e e68f  ......<\/ft>\n..
-000016a0: 8fe8 bfb0 efbc 9ae7 949f e591 bd5c 6ee8  .............\n.
-000016b0: a18c e58a a8e7 898c e695 88e6 9e9c efbc  ................
-000016c0: 9ae6 81a2 e5a4 8d48 505c 6ee6 8a80 e883  .......HP\n.....
-000016d0: bde7 898c e695 88e6 9e9c efbc 9ae6 81a2  ................
-000016e0: e5a4 8d48 505c 6e3c 6674 2073 697a 653d  ...HP\n<ft size=
-000016f0: 3330 2063 6f6c 6f72 3d62 6c61 636b 3ee6  30 color=black>.
-00001700: a285 e88a b13c 5c2f 6674 3e5c 6ee6 8f8f  .....<\/ft>\n...
-00001710: e8bf b0ef bc9a e68a 80e8 83bd 5c6e e8a1  ............\n..
-00001720: 8ce5 8aa8 e789 8ce6 9588 e69e 9cef bc9a  ................
-00001730: e4b8 bbe5 8aa8 e68a 80e8 83bd 5c6e e68a  ............\n..
-00001740: 80e8 83bd e789 8ce6 9588 e69e 9cef bc9a  ................
-00001750: e5a2 9ee5 8aa0 5350 5c6e 3c66 7420 7369  ......SP\n<ft si
-00001760: 7a65 3d33 3020 636f 6c6f 723d 7265 643e  ze=30 color=red>
-00001770: e696 b9e7 8987 3c5c 2f66 743e 5c6e e68f  ......<\/ft>\n..
-00001780: 8fe8 bfb0 efbc 9ae6 94bb e587 bbe8 a18c  ................
-00001790: e58a a8e7 898c e695 88e6 9e9c efbc 9ae6  ................
-000017a0: 8993 e587 bae6 94bb e587 bb5c 6ee6 8a80  ...........\n...
-000017b0: e883 bde7 898c e695 88e6 9e9c efbc 9ae6  ................
-000017c0: 8993 e587 bae5 8f8d e587 bb5c 6e5c 6ee4  ...........\n\n.
-000017d0: b8bb e58a a8e6 8a80 e883 bdef bc9a 5c6e  ..............\n
-000017e0: e691 87e4 b880 e4b8 aa32 30e9 9da2 e9aa  .........20.....
-000017f0: b0e5 ad90 5c6e e5a6 82e6 9e9c e782 b9e6  ....\n..........
-00001800: 95b0 e5b0 8fe4 ba8e e887 aae8 baab 5350  ..............SP
-00001810: e588 99e6 8a8a e589 a9e4 bd99 e4b8 a4e5  ................
-00001820: bca0 e689 8be7 898c e4bd 9ce4 b8ba e68a  ................
-00001830: 80e8 83bd e789 8ce5 85a8 e983 a8e6 8993  ................
-00001840: e587 ba5c 6ee6 8c89 e785 a7e6 8a80 e883  ...\n...........
-00001850: bde7 898c e782 b9e6 95b0 e689 a3e9 99a4  ................
-00001860: e887 aae8 baab 5350 e782 b941 4345 e68a  ......SP...ACE..
-00001870: 80e8 83bd efbc 9a5c 6ee6 9187 e4b8 80e4  .......\n.......
-00001880: b8aa 36e9 9da2 e9aa b0e5 ad90 5c6e e68a  ..6.........\n..
-00001890: 8ae6 8993 e587 bae7 9a84 4143 45e7 898c  ..........ACE...
-000018a0: e782 b9e6 9bbf e68d a2e6 8890 e691 87e5  ................
-000018b0: 87ba e79a 84e7 82b9 e695 b05c 6ee5 868d  ...........\n...
-000018c0: e68a 8ae4 b889 e5bc a0e6 898b e789 8ce5  ................
-000018d0: 85a8 e983 a8e4 bd9c e4b8 bae6 8a80 e883  ................
-000018e0: bde7 898c e689 93e5 87ba 5c6e e68c 89e7  ..........\n....
-000018f0: 85a7 e68a 80e8 83bd e789 8ce7 82b9 e695  ................
-00001900: b0e6 89a3 e999 a4e8 87aa e8ba ab53 50e7  .............SP.
-00001910: 82b9 5c6e 5c6e e380 90e5 bc80 e5a7 8be6  ..\n\n..........
-00001920: b8b8 e688 8fe3 8091 5c6e e689 91e5 858b  ........\n......
-00001930: e5af b9e6 8898 20e3 8090 e987 91e9 a29d  ...... .........
-00001940: e380 9120 e380 9061 74e3 8091 efbc 88e4  ... ...at.......
-00001950: b8ba e7a9 bae5 8899 e689 80e6 9c89 e7be  ................
-00001960: a4e5 8f8b e983 bde5 8faf e68e a5e5 8f97  ................
-00001970: efbc 895c 6ee3 8090 e59b 9ee5 ba94 e380  ...\n...........
-00001980: 915c 6ee6 8ea5 e58f 97e6 8c91 e688 985c  .\n............\
-00001990: 2fe6 8b92 e7bb 9de6 8c91 e688 985c 6ee3  /............\n.
-000019a0: 8090 e59b 9ee5 9088 e4b8 ade3 8091 5c6e  ..............\n
-000019b0: e587 bae7 898c 2031 5c2f 325c 2f33 efbc  ...... 1\/2\/3..
-000019c0: 88e8 bdae e6b5 81e5 87ba e789 8cef bc89  ................
-000019d0: 5c6e e380 90e7 bb93 e7ae 97e3 8091 5c6e  \n............\n
-000019e0: e7bb 93e7 ae97 efbc 88e5 bd93 e69f 90e4  ................
-000019f0: b880 e696 b936 30e7 a792 e6b2 a1e6 9c89  .....60.........
-00001a00: e59b 9ee5 ba94 efbc 8ce4 bba5 e79b aee5  ................
-00001a10: 898d e8a1 80e9 878f e7bb 93e7 ae97 efbc  ................
-00001a20: 8922 0d0a 2020 2020 7d2c 0d0a 2020 2020  ."..    },..    
-00001a30: 7b0d 0a20 2020 2020 2020 2022 6675 6e63  {..        "func
-00001a40: 223a 2022 e8b5 9be9 a9ac e5b0 8fe6 b8b8  ": "............
-00001a50: e688 8f22 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00001a60: 7472 6967 6765 725f 6d65 7468 6f64 223a  trigger_method":
-00001a70: 2022 e8b5 9be9 a9ac e588 9be5 bbba 222c   "............",
-00001a80: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
-00001a90: 6572 5f63 6f6e 6469 7469 6f6e 223a 2022  er_condition": "
-00001aa0: e697 a022 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00001ab0: 6272 6965 665f 6465 7322 3a20 22e5 889b  brief_des": "...
-00001ac0: e5bb bae8 b59b e9a9 ace5 b08f e6b8 b8e6  ................
-00001ad0: 888f 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
-00001ae0: 6574 6169 6c5f 6465 7322 3a20 22e6 b581  etail_des": "...
-00001af0: e7a8 8bef bc9a 5c6e e8b5 9be9 a9ac e588  ......\n........
-00001b00: 9be5 bbba efbc 9ae7 acac e4b8 80e4 bd8d  ................
-00001b10: e78e a9e5 aeb6 e58f 91e8 b5b7 e6b4 bbe5  ................
-00001b20: 8aa8 20e2 8692 5c6e e8b5 9be9 a9ac e58a  .. ...\n........
-00001b30: a0e5 85a5 20e3 8090 e4bd a0e7 9a84 e9a9  .... ...........
-00001b40: ace5 84bf e590 8de7 a7b0 e380 91ef bc9a  ................
-00001b50: e78e a9e5 aeb6 e58f 82e8 b59b 20e2 8692  ............ ...
-00001b60: 5c6e e8b5 9be9 a9ac e5bc 80e5 a78b efbc  \n..............
-00001b70: 9ae6 b8b8 e688 8fe8 bf9b e8a1 8c20 e286  ............. ..
-00001b80: 925c 6ee8 bf9b e8a1 8ce4 b8ad 20e2 8692  .\n......... ...
-00001b90: 5c6e e7bb 93e7 ae97 5c6e 5c6e e5bd 93e9  \n......\n\n....
-00001ba0: 8187 e588 b0e9 9499 e8af afe6 8896 e585  ................
-00001bb0: b6e4 bb96 e683 85e5 86b5 e58f afe4 bdbf  ................
-00001bc0: e794 a8e8 b59b e9a9 ace9 878d e7bd aee6  ................
-00001bd0: 9da5 e987 8de7 bdae e9a9 ace5 9cba e380  ................
-00001be0: 8222 0d0a 2020 2020 7d2c 0d0a 2020 2020  ."..    },..    
-00001bf0: 7b0d 0a20 2020 2020 2020 2022 6675 6e63  {..        "func
-00001c00: 223a 2022 e5b8 82e5 9cba e4bf a1e6 81af  ": "............
-00001c10: 222c 0d0a 2020 2020 2020 2020 2274 7269  ",..        "tri
-00001c20: 6767 6572 5f6d 6574 686f 6422 3a20 22e5  gger_method": ".
-00001c30: b882 e59c bae4 bfa1 e681 af22 2c0d 0a20  ...........",.. 
-00001c40: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
-00001c50: 636f 6e64 6974 696f 6e22 3a20 22e6 97a0  condition": "...
-00001c60: 222c 0d0a 2020 2020 2020 2020 2262 7269  ",..        "bri
-00001c70: 6566 5f64 6573 223a 2022 e69f a5e7 9c8b  ef_des": "......
-00001c80: e5b8 82e5 9cba e4bf a1e6 81af 222c 0d0a  ............",..
-00001c90: 2020 2020 2020 2020 2264 6574 6169 6c5f          "detail_
-00001ca0: 6465 7322 3a20 22e6 9fa5 e79c 8be5 b882  des": ".........
-00001cb0: e59c bae4 b88a e689 80e6 9c89 e585 ace5  ................
-00001cc0: 8fb8 e79a 84e5 ae98 e696 b9e7 bb93 e7ae  ................
-00001cd0: 97e4 bbb7 e6a0 bc22 0d0a 2020 2020 7d2c  ......."..    },
-00001ce0: 0d0a 2020 2020 7b0d 0a20 2020 2020 2020  ..    {..       
-00001cf0: 2022 6675 6e63 223a 2022 e78e a9e5 aeb6   "func": "......
-00001d00: e5b8 82e5 9cba e4bf a1e6 81af 222c 0d0a  ............",..
-00001d10: 2020 2020 2020 2020 2274 7269 6767 6572          "trigger
-00001d20: 5f6d 6574 686f 6422 3a20 22e5 b882 e59c  _method": ".....
-00001d30: bae4 bfa1 e681 af20 e380 90e5 85ac e58f  ....... ........
-00001d40: b8e5 908d e7a7 b0e3 8091 222c 0d0a 2020  ..........",..  
-00001d50: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
-00001d60: 6f6e 6469 7469 6f6e 223a 2022 e697 a022  ondition": "..."
-00001d70: 2c0d 0a20 2020 2020 2020 2022 6272 6965  ,..        "brie
-00001d80: 665f 6465 7322 3a20 22e6 9fa5 e79c 8be3  f_des": ".......
-00001d90: 8090 e585 ace5 8fb8 e590 8de7 a7b0 e380  ................
-00001da0: 91e8 82a1 e4bb bde6 8aa5 e4bb b722 2c0d  .............",.
-00001db0: 0a20 2020 2020 2020 2022 6465 7461 696c  .        "detail
-00001dc0: 5f64 6573 223a 2022 220d 0a20 2020 207d  _des": ""..    }
-00001dd0: 2c0d 0a20 2020 207b 0d0a 2020 2020 2020  ,..    {..      
-00001de0: 2020 2266 756e 6322 3a20 22e5 b882 e59c    "func": ".....
-00001df0: bae8 a18c e683 8522 2c0d 0a20 2020 2020  .......",..     
-00001e00: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
-00001e10: 6f64 223a 2022 e5b8 82e5 9cba e8a1 8ce6  od": "..........
-00001e20: 8385 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
-00001e30: 7269 6767 6572 5f63 6f6e 6469 7469 6f6e  rigger_condition
-00001e40: 223a 2022 e697 a022 2c0d 0a20 2020 2020  ": "...",..     
-00001e50: 2020 2022 6272 6965 665f 6465 7322 3a20     "brief_des": 
-00001e60: 22e6 9fa5 e79c 8be5 b882 e59c bae8 a18c  "...............
-00001e70: e683 8522 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00001e80: 6465 7461 696c 5f64 6573 223a 2022 220d  detail_des": "".
-00001e90: 0a20 2020 207d 2c0d 0a20 2020 207b 0d0a  .    },..    {..
-00001ea0: 2020 2020 2020 2020 2266 756e 6322 3a20          "func": 
-00001eb0: 22e5 85ac e58f b8e4 bfa1 e681 af22 2c0d  "............",.
-00001ec0: 0a20 2020 2020 2020 2022 7472 6967 6765  .        "trigge
-00001ed0: 725f 6d65 7468 6f64 223a 2022 e585 ace5  r_method": "....
-00001ee0: 8fb8 e4bf a1e6 81af 20e3 8090 e585 ace5  ........ .......
-00001ef0: 8fb8 e590 8de7 a7b0 e380 9122 2c0d 0a20  ...........",.. 
-00001f00: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
-00001f10: 636f 6e64 6974 696f 6e22 3a20 22e6 97a0  condition": "...
-00001f20: 222c 0d0a 2020 2020 2020 2020 2262 7269  ",..        "bri
-00001f30: 6566 5f64 6573 223a 2022 e69f a5e7 9c8b  ef_des": "......
-00001f40: e585 ace5 8fb8 e79a 84e8 afa6 e7bb 86e4  ................
-00001f50: bfa1 e681 af22 2c0d 0a20 2020 2020 2020  .....",..       
-00001f60: 2022 6465 7461 696c 5f64 6573 223a 2022   "detail_des": "
-00001f70: 220d 0a20 2020 207d 2c0d 0a20 2020 207b  "..    },..    {
-00001f80: 0d0a 2020 2020 2020 2020 2266 756e 6322  ..        "func"
-00001f90: 3a20 22e5 8f91 e8a1 8ce8 b4ad e4b9 b022  : "............"
-00001fa0: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
-00001fb0: 6765 725f 6d65 7468 6f64 223a 2022 e58f  ger_method": "..
-00001fc0: 91e8 a18c e8b4 ade4 b9b0 20e3 8090 e585  .......... .....
-00001fd0: ace5 8fb8 e590 8de7 a7b0 e380 9120 e380  ............. ..
-00001fe0: 904e e380 9122 2c0d 0a20 2020 2020 2020  .N...",..       
-00001ff0: 2022 7472 6967 6765 725f 636f 6e64 6974   "trigger_condit
-00002000: 696f 6e22 3a20 22e6 97a0 222c 0d0a 2020  ion": "...",..  
-00002010: 2020 2020 2020 2262 7269 6566 5f64 6573        "brief_des
-00002020: 223a 2022 e4bb 8ee5 ae98 e696 b9e8 b4ad  ": "............
-00002030: e4b9 b0e8 82a1 e7a5 a822 2c0d 0a20 2020  .........",..   
-00002040: 2020 2020 2022 6465 7461 696c 5f64 6573       "detail_des
-00002050: 223a 2022 e4bb a5e5 8f91 e8a1 8ce4 bbb7  ": "............
-00002060: e6a0 bce4 bb8e 20e3 8090 e585 ace5 8fb8  ...... .........
-00002070: e590 8de7 a7b0 e380 91e8 b4ad e4b9 b04e  ...............N
-00002080: e882 a1e6 9cac e585 ace5 8fb8 e882 a1e4  ................
-00002090: bbbd e380 8222 0d0a 2020 2020 7d2c 0d0a  ....."..    },..
-000020a0: 2020 2020 7b0d 0a20 2020 2020 2020 2022      {..        "
-000020b0: 6675 6e63 223a 2022 e5ae 98e6 96b9 e7bb  func": "........
-000020c0: 93e7 ae97 222c 0d0a 2020 2020 2020 2020  ....",..        
-000020d0: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
-000020e0: 3a20 22e5 ae98 e696 b9e7 bb93 e7ae 9720  : "............ 
-000020f0: e380 90e5 85ac e58f b8e5 908d e7a7 b0e3  ................
-00002100: 8091 20e3 8090 4ee3 8091 222c 0d0a 2020  .. ...N...",..  
-00002110: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
-00002120: 6f6e 6469 7469 6f6e 223a 2022 e697 a022  ondition": "..."
-00002130: 2c0d 0a20 2020 2020 2020 2022 6272 6965  ,..        "brie
-00002140: 665f 6465 7322 3a20 22e4 bb8e e5ae 98e6  f_des": ".......
-00002150: 96b9 e7bb 93e7 ae97 e882 a1e7 a5a8 222c  ..............",
-00002160: 0d0a 2020 2020 2020 2020 2264 6574 6169  ..        "detai
-00002170: 6c5f 6465 7322 3a20 22e4 bba5 e7bb 93e7  l_des": ".......
-00002180: ae97 e4bb b7e6 a0bc e590 91e3 8090 e585  ................
-00002190: ace5 8fb8 e590 8de7 a7b0 e380 91e5 8d96  ................
-000021a0: e587 ba4e e882 a1e6 9cac e585 ace5 8fb8  ...N............
-000021b0: e882 a1e4 bbbd e380 8222 0d0a 2020 2020  ........."..    
-000021c0: 7d2c 0d0a 2020 2020 7b0d 0a20 2020 2020  },..    {..     
-000021d0: 2020 2022 6675 6e63 223a 2022 e8b4 ade4     "func": "....
-000021e0: b9b0 e882 a1e7 a5a8 222c 0d0a 2020 2020  ........",..    
-000021f0: 2020 2020 2274 7269 6767 6572 5f6d 6574      "trigger_met
-00002200: 686f 6422 3a20 22e8 b4ad e4b9 b020 e380  hod": "...... ..
-00002210: 90e5 85ac e58f b8e5 908d e7a7 b0e3 8091  ................
-00002220: 20e3 8090 4ee3 8091 222c 0d0a 2020 2020   ...N...",..    
-00002230: 2020 2020 2274 7269 6767 6572 5f63 6f6e      "trigger_con
-00002240: 6469 7469 6f6e 223a 2022 e697 a022 2c0d  dition": "...",.
-00002250: 0a20 2020 2020 2020 2022 6272 6965 665f  .        "brief_
-00002260: 6465 7322 3a20 22e4 bb8e e78e a9e5 aeb6  des": ".........
-00002270: e5b8 82e5 9cba e8b4 ade4 b9b0 e882 a1e7  ................
-00002280: a5a8 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
-00002290: 6574 6169 6c5f 6465 7322 3a20 22e4 bba5  etail_des": "...
-000022a0: e4bb 8ee4 bd8e e588 b0e9 ab98 e79a 84e6  ................
-000022b0: 8aa5 e4bb b7e4 b9b0 e585 a54e e882 a1e5  ...........N....
-000022c0: b882 e59c bae4 b8ad e79a 84e3 8090 e585  ................
-000022d0: ace5 8fb8 e590 8de7 a7b0 e380 91e3 8082  ................
-000022e0: 220d 0a20 2020 207d 2c0d 0a20 2020 207b  "..    },..    {
-000022f0: 0d0a 2020 2020 2020 2020 2266 756e 6322  ..        "func"
-00002300: 3a20 22e5 87ba e594 aee8 82a1 e7a5 a822  : "............"
-00002310: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
-00002320: 6765 725f 6d65 7468 6f64 223a 2022 e587  ger_method": "..
-00002330: bae5 94ae 20e3 8090 e585 ace5 8fb8 e590  .... ...........
-00002340: 8de7 a7b0 e380 9120 e380 90e6 8aa5 e4bb  ....... ........
-00002350: b7e3 8091 20e3 8090 4ee3 8091 222c 0d0a  .... ...N...",..
-00002360: 2020 2020 2020 2020 2274 7269 6767 6572          "trigger
-00002370: 5f63 6f6e 6469 7469 6f6e 223a 2022 e697  _condition": "..
-00002380: a022 2c0d 0a20 2020 2020 2020 2022 6272  .",..        "br
-00002390: 6965 665f 6465 7322 3a20 22e4 bb8e e78e  ief_des": ".....
-000023a0: a9e5 aeb6 e5b8 82e5 9cba e587 bae5 94ae  ................
-000023b0: e882 a1e7 a5a8 222c 0d0a 2020 2020 2020  ......",..      
-000023c0: 2020 2264 6574 6169 6c5f 6465 7322 3a20    "detail_des": 
-000023d0: 22e5 b086 e887 aae5 b7b1 e689 8be4 b8ad  "...............
-000023e0: e79a 84e3 8090 e585 ace5 8fb8 e590 8de7  ................
-000023f0: a7b0 e380 9120 e4bb a5e3 8090 e68a a5e4  ..... ..........
-00002400: bbb7 e380 91e5 8f91 e5b8 83e5 88b0 e5b8  ................
-00002410: 82e5 9cba 4ee8 82a1 e380 8222 0d0a 2020  ....N......"..  
-00002420: 2020 7d2c 0d0a 2020 2020 7b0d 0a20 2020    },..    {..   
-00002430: 2020 2020 2022 6675 6e63 223a 2022 e5b8       "func": "..
-00002440: 82e5 9cba e6b3 a8e5 868c 222c 0d0a 2020  ..........",..  
-00002450: 2020 2020 2020 2274 7269 6767 6572 5f6d        "trigger_m
-00002460: 6574 686f 6422 3a20 22e5 b882 e59c bae6  ethod": ".......
-00002470: b3a8 e586 8c20 e380 90e5 85ac e58f b8e5  ..... ..........
-00002480: 908d e7a7 b0e3 8091 222c 0d0a 2020 2020  ........",..    
-00002490: 2020 2020 2274 7269 6767 6572 5f63 6f6e      "trigger_con
-000024a0: 6469 7469 6f6e 223a 2022 e99c 80e8 a681  dition": "......
-000024b0: 4062 6f74 e688 96e5 8fab 626f 74e7 9a84  @bot......bot...
-000024c0: e590 8de5 ad97 efbc 8ce6 8c87 e4bb a4e6  ................
-000024d0: 9d83 e999 90ef bc9a e7ae a1e7 9086 e591  ................
-000024e0: 98e3 8082 222c 0d0a 2020 2020 2020 2020  ....",..        
-000024f0: 2262 7269 6566 5f64 6573 223a 2022 e688  "brief_des": "..
-00002500: 90e7 ab8b e585 ace5 8fb8 222c 0d0a 2020  ..........",..  
-00002510: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
-00002520: 7322 3a20 22e5 b086 e69c ace7 bea4 e4bb  s": "...........
-00002530: a5e3 8090 e585 ace5 8fb8 e590 8de7 a7b0  ................
-00002540: e380 91e6 b3a8 e586 8ce5 88b0 e5b8 82e5  ................
-00002550: 9cba efbc 8c5c 6ee5 a682 e69e 9ce5 85a8  .....\n.........
-00002560: e7be a4e9 8791 e5b8 81e6 95b0 e5b0 8fe4  ................
-00002570: ba8e e4b8 a4e4 b887 e588 99e4 bc9a e6b3  ................
-00002580: a8e5 868c e5a4 b1e8 b4a5 e380 8222 0d0a  ............."..
-00002590: 2020 2020 7d2c 0d0a 2020 2020 7b0d 0a20      },..    {.. 
-000025a0: 2020 2020 2020 2022 6675 6e63 223a 2022         "func": "
-000025b0: e69b b4e6 96b0 e585 ace5 8fb8 e7ae 80e4  ................
-000025c0: bb8b 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
-000025d0: 7269 6767 6572 5f6d 6574 686f 6422 3a20  rigger_method": 
-000025e0: 22e6 9bb4 e696 b0e5 85ac e58f b8e7 ae80  "...............
-000025f0: e4bb 8b20 e380 90e7 ae80 e4bb 8be5 8685  ... ............
-00002600: e5ae b9e3 8091 222c 0d0a 2020 2020 2020  ......",..      
-00002610: 2020 2274 7269 6767 6572 5f63 6f6e 6469    "trigger_condi
-00002620: 7469 6f6e 223a 2022 e68c 87e4 bba4 e69d  tion": "........
-00002630: 83e9 9990 efbc 9ae7 aea1 e790 86e5 9198  ................
-00002640: 222c 0d0a 2020 2020 2020 2020 2262 7269  ",..        "bri
-00002650: 6566 5f64 6573 223a 2022 e69b b4e6 96b0  ef_des": "......
-00002660: e585 ace5 8fb8 e7ae 80e4 bb8b 222c 0d0a  ............",..
-00002670: 2020 2020 2020 2020 2264 6574 6169 6c5f          "detail_
-00002680: 6465 7322 3a20 22e5 b086 e380 90e7 ae80  des": ".........
-00002690: e4bb 8be5 8685 e5ae b9e3 8091 e6b7 bbe5  ................
-000026a0: 8aa0 e588 b0e6 9cac e7be a4e5 85ac e58f  ................
-000026b0: b8e8 b584 e696 99e7 9a84 e7ae 80e4 bb8b  ................
-000026c0: e4b8 ad22 0d0a 2020 2020 7d2c 0d0a 2020  ..."..    },..  
-000026d0: 2020 7b0d 0a20 2020 2020 2020 2022 6675    {..        "fu
-000026e0: 6e63 223a 2022 e7ae a1e7 9086 e591 98e6  nc": "..........
-000026f0: 9bb4 e696 b0e5 85ac e58f b8e7 ae80 e4bb  ................
-00002700: 8b22 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
-00002710: 6967 6765 725f 6d65 7468 6f64 223a 2022  igger_method": "
-00002720: e7ae a1e7 9086 e591 98e6 9bb4 e696 b0e5  ................
-00002730: 85ac e58f b8e7 ae80 e4bb 8b20 e380 90e5  ........... ....
-00002740: 85ac e58f b8e5 908d e7a7 b0e3 8091 20e3  .............. .
-00002750: 8090 e7ae 80e4 bb8b e586 85e5 aeb9 e380  ................
-00002760: 9122 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
-00002770: 6967 6765 725f 636f 6e64 6974 696f 6e22  igger_condition"
-00002780: 3a20 22e6 8c87 e4bb a4e6 9d83 e999 90ef  : ".............
-00002790: bc9a e8b6 85e7 aea1 222c 0d0a 2020 2020  ........",..    
-000027a0: 2020 2020 2262 7269 6566 5f64 6573 223a      "brief_des":
-000027b0: 2022 e69b b4e6 96b0 e585 ace5 8fb8 e7ae   "..............
-000027c0: 80e4 bb8b 222c 0d0a 2020 2020 2020 2020  ....",..        
-000027d0: 2264 6574 6169 6c5f 6465 7322 3a20 22e5  "detail_des": ".
-000027e0: b086 e380 90e7 ae80 e4bb 8be5 8685 e5ae  ................
-000027f0: b9e3 8091 e6b7 bbe5 8aa0 e588 b0e3 8090  ................
-00002800: e585 ace5 8fb8 e590 8de7 a7b0 e380 91e8  ................
-00002810: b584 e696 99e7 9a84 e7ae 80e4 bb8b e4b8  ................
-00002820: ade3 8082 220d 0a20 2020 207d 2c0d 0a20  ...."..    },.. 
-00002830: 2020 207b 0d0a 2020 2020 2020 2020 2266     {..        "f
-00002840: 756e 6322 3a20 22e8 b584 e4ba a7e8 b083  unc": ".........
-00002850: e69f a522 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00002860: 7472 6967 6765 725f 6d65 7468 6f64 223a  trigger_method":
-00002870: 2022 312e e8b5 84e4 baa7 e8b0 83e6 9fa5   "1.............
-00002880: 2032 2ee8 b584 e4ba a7e8 b083 e69f a540   2.............@
-00002890: 736f 6d65 6f6e 655c 6e22 2c0d 0a20 2020  someone\n",..   
-000028a0: 2020 2020 2022 7472 6967 6765 725f 636f       "trigger_co
-000028b0: 6e64 6974 696f 6e22 3a20 22e6 8c87 e4bb  ndition": ".....
-000028c0: a4e6 9d83 e999 90ef bc9a e7ae a1e7 9086  ................
-000028d0: e591 9822 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-000028e0: 6272 6965 665f 6465 7322 3a20 22e8 b083  brief_des": "...
-000028f0: e69f a5e7 94a8 e688 b7e7 9a84 e8b5 84e4  ................
-00002900: baa7 e588 86e5 b883 e683 85e5 86b5 e380  ................
-00002910: 8222 2c0d 0a20 2020 2020 2020 2022 6465  .",..        "de
-00002920: 7461 696c 5f64 6573 223a 2022 e5a6 82e6  tail_des": "....
-00002930: 9e9c e69c aae6 8c87 e5ae 9ae7 94a8 e688  ................
-00002940: b7ef bc8c e588 99e8 b083 e69f a5e7 8ea9  ................
-00002950: e5ae b6e6 80bb e8b5 84e4 baa7 e589 8de5  ................
-00002960: 8d81 e590 8de7 9a84 e8b5 84e4 baa7 e588  ................
-00002970: 86e5 b883 e683 85e5 86b5 e380 8222 0d0a  ............."..
-00002980: 2020 2020 7d2c 0d0a 2020 2020 7b0d 0a20      },..    {.. 
-00002990: 2020 2020 2020 2022 6675 6e63 223a 2022         "func": "
-000029a0: e586 bbe7 bb93 e8b5 84e4 baa7 222c 0d0a  ............",..
-000029b0: 2020 2020 2020 2020 2274 7269 6767 6572          "trigger
-000029c0: 5f6d 6574 686f 6422 3a20 22e5 86bb e7bb  _method": ".....
-000029d0: 93e8 b584 e4ba a740 736f 6d65 6f6e 6522  .......@someone"
-000029e0: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
-000029f0: 6765 725f 636f 6e64 6974 696f 6e22 3a20  ger_condition": 
-00002a00: 22e6 8c87 e4bb a4e6 9d83 e999 90ef bc9a  "...............
-00002a10: e8b6 85e7 aea1 222c 0d0a 2020 2020 2020  ......",..      
-00002a20: 2020 2262 7269 6566 5f64 6573 223a 2022    "brief_des": "
-00002a30: e69f a5e5 b081 6174 e79a 84e7 bea4 e58f  ......at........
-00002a40: 8be7 9a84 e585 a8e9 83a8 e8b5 84e4 baa7  ................
-00002a50: e380 8222 2c0d 0a20 2020 2020 2020 2022  ...",..        "
-00002a60: 6465 7461 696c 5f64 6573 223a 2022 e69f  detail_des": "..
-00002a70: a5e5 b081 e590 8ee7 9a84 e794 a8e6 88b7  ................
-00002a80: e4bc 9ae6 8c81 e69c 89e6 9c80 e5a4 9a35  ...............5
-00002a90: 3030 e4b8 aae5 85a8 e5b1 80e9 8193 e585  00..............
-00002aa0: b7e3 8090 e8a2 abe5 86bb e7bb 93e7 9a84  ................
-00002ab0: e8b5 84e4 baa7 e380 91ef bc8c 5c6e e6ad  ............\n..
-00002ac0: a4e9 8193 e585 b7e5 8faf e4bb a5e5 9ca8  ................
-00002ad0: e4bb bbe6 848f e7be a4e4 bdbf e794 a8ef  ................
-00002ae0: bc8c 5c6e e6af 8fe4 b8aa e380 90e8 a2ab  ..\n............
-00002af0: e586 bbe7 bb93 e79a 84e8 b584 e4ba a7e3  ................
-00002b00: 8091 e4bd bfe7 94a8 e590 8ee4 bc9a e59c  ................
-00002b10: a8e4 bdbf e794 a8e7 9a84 e7be a4e8 8eb7  ................
-00002b20: e5be 97e4 b880 e580 8de8 b58c e6b3 a8e4  ................
-00002b30: b88a e999 90e7 9a84 e987 91e5 b881 e380  ................
-00002b40: 8222 0d0a 2020 2020 7d2c 0d0a 2020 2020  ."..    },..    
-00002b50: 7b0d 0a20 2020 2020 2020 2022 6675 6e63  {..        "func
-00002b60: 223a 2022 e6b8 85e7 9086 e697 a0e6 9588  ": "............
-00002b70: e8b4 a6e6 88b7 222c 0d0a 2020 2020 2020  ......",..      
-00002b80: 2020 2274 7269 6767 6572 5f6d 6574 686f    "trigger_metho
-00002b90: 6422 3a20 22e6 b885 e790 86e6 97a0 e695  d": "...........
-00002ba0: 88e8 b4a6 e688 b722 2c0d 0a20 2020 2020  .......",..     
-00002bb0: 2020 2022 7472 6967 6765 725f 636f 6e64     "trigger_cond
-00002bc0: 6974 696f 6e22 3a20 22e6 8c87 e4bb a4e6  ition": ".......
-00002bd0: 9d83 e999 90ef bc9a e8b6 85e7 aea1 222c  ..............",
-00002be0: 0d0a 2020 2020 2020 2020 2262 7269 6566  ..        "brief
-00002bf0: 5f64 6573 223a 2022 e6b8 85e7 9086 e697  _des": "........
-00002c00: a0e6 9588 e8b4 a6e6 88b7 222c 0d0a 2020  ..........",..  
-00002c10: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
-00002c20: 7322 3a20 22e6 97a0 e695 88e8 b4a6 e688  s": "...........
-00002c30: b7e8 8c83 e59b b4ef bc9a 5c6e 626f 74e4  ..........\nbot.
-00002c40: b88d e59c a8e7 9a84 e7be a45c 6ee9 8080  ...........\n...
-00002c50: e7be a4e7 9a84 e794 a8e6 88b7 5c6e e995  ............\n..
-00002c60: bfe6 9c9f e4b8 8de5 8692 e6b3 a1e7 9a84  ................
-00002c70: e7be a4e5 8f8b 5c6e e8b5 84e4 baa7 e8bf  ......\n........
-00002c80: 87e5 b08f e79a 84e5 85ac e58f b822 0d0a  ............."..
-00002c90: 2020 2020 7d0d 0a5d                          }..]
+00000010: 2020 2266 756e 6322 3a22 e88e b7e5 8f96    "func":"......
+00000020: e987 91e5 b881 222c 0d0a 2020 2020 2020  ......",..      
+00000030: 2020 2274 7269 6767 6572 5f6d 6574 686f    "trigger_metho
+00000040: 6422 3a22 312e e987 91e5 b881 e7ad bee5  d":"1...........
+00000050: 88b0 2032 2ee9 878d e7bd aee7 adbe e588  .. 2............
+00000060: b022 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
+00000070: 6967 6765 725f 636f 6e64 6974 696f 6e22  igger_condition"
+00000080: 3a22 e697 a022 2c0d 0a20 2020 2020 2020  :"...",..       
+00000090: 2022 6272 6965 665f 6465 7322 3a22 e88e   "brief_des":"..
+000000a0: b7e5 8f96 e987 91e5 b881 222c 0d0a 2020  ..........",..  
+000000b0: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
+000000c0: 7322 3a22 e987 91e5 b881 e7ad bee5 88b0  s":"............
+000000d0: efbc 9a5c 6ee7 8ea9 e5ae b6e6 af8f e697  ...\n...........
+000000e0: a5e5 8faf e7ad bee5 88b0 e4b8 80e6 aca1  ................
+000000f0: efbc 8ce6 af8f e697 a530 e782 b9e5 88b7  .........0......
+00000100: e696 b0e3 8082 5c6e e987 8de7 bdae e7ad  ......\n........
+00000110: bee5 88b0 efbc 9a5c 6ee6 af8f e6ac a1e9  .......\n.......
+00000120: 878d e7bd aee5 908e e58f afe9 a286 e58f  ................
+00000130: 96e4 b880 e6ac a1e3 8082 220d 0a20 2020  .........."..   
+00000140: 207d 2c0d 0a20 2020 207b 0d0a 2020 2020   },..    {..    
+00000150: 2020 2020 2266 756e 6322 3a22 e58f 91e8      "func":"....
+00000160: b5b7 e987 8de7 bdae 222c 0d0a 2020 2020  ........",..    
+00000170: 2020 2020 2274 7269 6767 6572 5f6d 6574      "trigger_met
+00000180: 686f 6422 3a22 e58f 91e8 b5b7 e987 8de7  hod":"..........
+00000190: bdae 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
+000001a0: 7269 6767 6572 5f63 6f6e 6469 7469 6f6e  rigger_condition
+000001b0: 223a 22e6 97a0 222c 0d0a 2020 2020 2020  ":"...",..      
+000001c0: 2020 2262 7269 6566 5f64 6573 223a 22e6    "brief_des":".
+000001d0: b885 e7a9 bae5 898d e58d 81e5 908d e79a  ................
+000001e0: 84e9 8791 e5b8 81e3 8082 222c 0d0a 2020  ..........",..  
+000001f0: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
+00000200: 7322 3a22 e5bd 93e9 8791 e5b8 81e6 8e92  s":"............
+00000210: e8a1 8ce6 a69c e7ac ace4 b880 e590 8de7  ................
+00000220: 9a84 e987 91e5 b881 e8b6 85e8 bf87 e7ac  ................
+00000230: ace4 ba8c e590 8de5 88b0 e7ac ace5 8d81  ................
+00000240: e590 8de7 9a84 e680 bbe5 928c efbc 8ce5  ................
+00000250: 8faf e4bb a5e5 8f91 e8b5 b7e9 878d e7bd  ................
+00000260: aee3 8082 220d 0a20 2020 207d 2c0d 0a20  ...."..    },.. 
+00000270: 2020 207b 0d0a 2020 2020 2020 2020 2266     {..        "f
+00000280: 756e 6322 3a22 e4b8 aae4 baba e8b4 a6e6  unc":"..........
+00000290: 88b7 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
+000002a0: 7269 6767 6572 5f6d 6574 686f 6422 3a22  rigger_method":"
+000002b0: 312e e688 91e7 9a84 e987 91e5 b881 2032  1............. 2
+000002c0: 2ee6 8891 e79a 84e4 bb93 e5ba 9320 332e  ............. 3.
+000002d0: e688 91e7 9a84 e8b5 84e6 9699 e58d a122  ..............."
+000002e0: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
+000002f0: 6765 725f 636f 6e64 6974 696f 6e22 3a22  ger_condition":"
+00000300: e697 a022 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00000310: 6272 6965 665f 6465 7322 3a22 e69f a5e7  brief_des":"....
+00000320: 9c8b e4b8 aae4 baba e8b4 a6e6 88b7 e8b5  ................
+00000330: 84e6 9699 222c 0d0a 2020 2020 2020 2020  ....",..        
+00000340: 2264 6574 6169 6c5f 6465 7322 3a22 e688  "detail_des":"..
+00000350: 91e7 9a84 e987 91e5 b881 efbc 9a5c 6ee6  .............\n.
+00000360: 9fa5 e79c 8be8 87aa e5b7 b1e7 9a84 e987  ................
+00000370: 91e5 b881 e695 b0e9 878f 5c6e e688 91e7  ..........\n....
+00000380: 9a84 e4bb 93e5 ba93 efbc 9a5c 6ee6 9fa5  ...........\n...
+00000390: e79c 8be8 87aa e5b7 b1e8 8eb7 e5be 97e7  ................
+000003a0: 9a84 e79a 84e9 8193 e585 b75c 6ee6 8891  ...........\n...
+000003b0: e79a 84e8 b584 e696 99e5 8da1 efbc 9a5c  ...............\
+000003c0: 6ee6 9fa5 e79c 8be4 b8aa e4ba bae8 b4a6  n...............
+000003d0: e688 b7e8 afa6 e7bb 86e8 b584 e696 995c  ...............\
+000003e0: 6ee6 8891 e79a 84e8 b584 e4ba a7ef bc9a  n...............
+000003f0: 5c6e e69f a5e7 9c8b e887 aae5 b7b1 e79a  \n..............
+00000400: 84e5 85a8 e5b1 80e8 b584 e4ba a7e5 8886  ................
+00000410: e5b8 8322 0d0a 2020 2020 7d2c 0d0a 2020  ..."..    },..  
+00000420: 2020 7b0d 0a20 2020 2020 2020 2022 6675    {..        "fu
+00000430: 6e63 223a 22e5 8f91 e7ba a2e5 8c85 222c  nc":".........",
+00000440: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
+00000450: 6572 5f6d 6574 686f 6422 3a22 e58f 91e7  er_method":"....
+00000460: baa2 e58c 8520 e380 90e9 8791 e9a2 9de3  ..... ..........
+00000470: 8091 20e3 8090 6174 e380 9122 2c0d 0a20  .. ...at...",.. 
+00000480: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+00000490: 636f 6e64 6974 696f 6e22 3a22 e697 a022  condition":"..."
+000004a0: 2c0d 0a20 2020 2020 2020 2022 6272 6965  ,..        "brie
+000004b0: 665f 6465 7322 3a22 e7bb 9961 74e7 9a84  f_des":"...at...
+000004c0: e794 a8e6 88b7 e58f 91e9 8791 e5b8 8122  ..............."
+000004d0: 2c0d 0a20 2020 2020 2020 2022 6465 7461  ,..        "deta
+000004e0: 696c 5f64 6573 223a 2222 0d0a 2020 2020  il_des":""..    
+000004f0: 7d2c 0d0a 2020 2020 7b0d 0a20 2020 2020  },..    {..     
+00000500: 2020 2022 6675 6e63 223a 22e9 8081 e981     "func":".....
+00000510: 93e5 85b7 222c 0d0a 2020 2020 2020 2020  ....",..        
+00000520: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
+00000530: 3a22 e980 81e9 8193 e585 b720 e380 90e9  :"......... ....
+00000540: 8193 e585 b7e5 908d e380 9120 e380 90e9  ........... ....
+00000550: 8193 e585 b7e6 95b0 e987 8fe3 8091 20e3  .............. .
+00000560: 8090 6174 e380 9122 2c0d 0a20 2020 2020  ..at...",..     
+00000570: 2020 2022 7472 6967 6765 725f 636f 6e64     "trigger_cond
+00000580: 6974 696f 6e22 3a22 e697 a022 2c0d 0a20  ition":"...",.. 
+00000590: 2020 2020 2020 2022 6272 6965 665f 6465         "brief_de
+000005a0: 7322 3a22 e7bb 9961 74e7 9a84 e794 a8e6  s":"...at.......
+000005b0: 88b7 e980 81e9 8193 e585 b722 2c0d 0a20  ...........",.. 
+000005c0: 2020 2020 2020 2022 6465 7461 696c 5f64         "detail_d
+000005d0: 6573 223a 22e5 8faf e4bb a5e4 b88d e5a1  es":"...........
+000005e0: abe9 8193 e585 b7e6 95b0 e987 8fef bc8c  ................
+000005f0: e9bb 98e8 aea4 e4b8 ba31 220d 0a20 2020  .........1"..   
+00000600: 207d 2c0d 0a20 2020 207b 0d0a 2020 2020   },..    {..    
+00000610: 2020 2020 2266 756e 6322 3a22 e987 91e5      "func":"....
+00000620: b881 e8bd ace7 a7bb 222c 0d0a 2020 2020  ........",..    
+00000630: 2020 2020 2274 7269 6767 6572 5f6d 6574      "trigger_met
+00000640: 686f 6422 3a22 e987 91e5 b881 e8bd ace7  hod":"..........
+00000650: a7bb 20e3 8090 e585 ace5 8fb8 e590 8de3  .. .............
+00000660: 8091 20e3 8090 e987 91e9 a29d e380 9122  .. ............"
+00000670: 2c0d 0a20 2020 2020 2020 2022 7472 6967  ,..        "trig
+00000680: 6765 725f 636f 6e64 6974 696f 6e22 3a22  ger_condition":"
+00000690: e8bd ace7 a7bb e79b aee6 a087 e5b7 b2e6  ................
+000006a0: b3a8 e586 8ce5 85ac e58f b8e3 8082 222c  ..............",
+000006b0: 0d0a 2020 2020 2020 2020 2262 7269 6566  ..        "brief
+000006c0: 5f64 6573 223a 22e8 b7a8 e7be a4e8 bdac  _des":".........
+000006d0: e7a7 bbe9 8791 e5b8 8122 2c0d 0a20 2020  .........",..   
+000006e0: 2020 2020 2022 6465 7461 696c 5f64 6573       "detail_des
+000006f0: 223a 22e8 bdac e7a7 bbe7 9bae e6a0 87e5  ":".............
+00000700: b7b2 e6b3 a8e5 868c e585 ace5 8fb8 efbc  ................
+00000710: 8ce4 bda0 e59c a8e7 9bae e6a0 87e7 bea4  ................
+00000720: e586 85e6 9c89 e8b4 a6e6 88b7 e380 8222  ..............."
+00000730: 0d0a 2020 2020 7d2c 0d0a 2020 2020 7b0d  ..    },..    {.
+00000740: 0a20 2020 2020 2020 2022 6675 6e63 223a  .        "func":
+00000750: 22e6 8abd e58d a122 2c0d 0a20 2020 2020  "......",..     
+00000760: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
+00000770: 6f64 223a 22e5 8d95 e68a bd5c 2f31 30e8  od":"......\/10.
+00000780: bf9e 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
+00000790: 7269 6767 6572 5f63 6f6e 6469 7469 6f6e  rigger_condition
+000007a0: 223a 22e9 9c80 e8a6 8140 626f 74e6 8896  ":"......@bot...
+000007b0: e58f ab62 6f74 e79a 84e5 908d e5ad 97e3  ...bot..........
+000007c0: 8082 222c 0d0a 2020 2020 2020 2020 2262  ..",..        "b
+000007d0: 7269 6566 5f64 6573 223a 22e8 8eb7 e58f  rief_des":".....
+000007e0: 96e9 8193 e585 b75c 6ee5 8faf e68c 87e5  .......\n.......
+000007f0: ae9a e68a bde5 8da1 e6ac a1e6 95b0 5c6e  ..............\n
+00000800: e4be 8be5 a682 efbc 9a20 4062 6f74 2033  ......... @bot 3
+00000810: 30e8 bf9e 222c 0d0a 2020 2020 2020 2020  0...",..        
+00000820: 2264 6574 6169 6c5f 6465 7322 3a22 e981  "detail_des":"..
+00000830: 93e5 85b7 e588 86e4 b8ba e585 a8e5 b180  ................
+00000840: e981 93e5 85b7 e592 8ce7 bea4 e586 85e9  ................
+00000850: 8193 e585 b75c 6ee4 b99f e58f afe5 8886  .....\n.........
+00000860: e4b8 bae6 b0b8 e4b9 85e9 8193 e585 b7e5  ................
+00000870: 928c e697 b6e6 9588 e981 93e5 85b7 5c6e  ..............\n
+00000880: e697 b6e6 9588 e981 93e5 85b7 e69c 80e9  ................
+00000890: 95bf e58f a0e5 8aa0 37e5 a4a9 5c6e e6b0  ........7...\n..
+000008a0: b8e4 b985 e981 93e5 85b7 e69c 80e5 a49a  ................
+000008b0: e58f a031 30e4 b8aa 5c6e e983 a8e5 8886  ...10...\n......
+000008c0: e981 93e5 85b7 e58f afe4 bdbf e794 a8ef  ................
+000008d0: bc9a 5c6e e4bd bfe7 94a8 e696 b9e6 b395  ..\n............
+000008e0: efbc 9ae4 bdbf e794 a8e9 8193 e585 b720  ............... 
+000008f0: e380 90e9 8193 e585 b7e5 908d e380 9120  ............... 
+00000900: e380 90e6 95b0 e987 8f5c 2fe5 8f82 e695  .........\/.....
+00000910: b0e3 8091 220d 0a20 2020 207d 2c0d 0a20  ...."..    },.. 
+00000920: 2020 207b 0d0a 2020 2020 2020 2020 2266     {..        "f
+00000930: 756e 6322 3a22 e4bd bfe7 94a8 e981 93e5  unc":"..........
+00000940: 85b7 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
+00000950: 7269 6767 6572 5f6d 6574 686f 6422 3a22  rigger_method":"
+00000960: e4bd bfe7 94a8 e981 93e5 85b7 20e3 8090  ............ ...
+00000970: e981 93e5 85b7 e590 8de3 8091 20e3 8090  ............ ...
+00000980: e695 b0e9 878f 5c2f e58f 82e6 95b0 e380  ......\/........
+00000990: 9122 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
+000009a0: 6967 6765 725f 636f 6e64 6974 696f 6e22  igger_condition"
+000009b0: 3a22 e697 a022 2c0d 0a20 2020 2020 2020  :"...",..       
+000009c0: 2022 6272 6965 665f 6465 7322 3a22 e983   "brief_des":"..
+000009d0: a8e5 8886 e981 93e5 85b7 e697 a0e6 b395  ................
+000009e0: e4bd bfe7 94a8 222c 0d0a 2020 2020 2020  ......",..      
+000009f0: 2020 2264 6574 6169 6c5f 6465 7322 3a22    "detail_des":"
+00000a00: 220d 0a20 2020 207d 2c0d 0a20 2020 207b  "..    },..    {
+00000a10: 0d0a 2020 2020 2020 2020 2266 756e 6322  ..        "func"
+00000a20: 3a22 e68e 92e8 a18c e6a6 9c22 2c0d 0a20  :".........",.. 
+00000a30: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+00000a40: 6d65 7468 6f64 223a 22e9 8791 e5b8 81e6  method":".......
+00000a50: 8e92 e8a1 8c22 2c0d 0a20 2020 2020 2020  .....",..       
+00000a60: 2022 7472 6967 6765 725f 636f 6e64 6974   "trigger_condit
+00000a70: 696f 6e22 3a22 e697 a022 2c0d 0a20 2020  ion":"...",..   
+00000a80: 2020 2020 2022 6272 6965 665f 6465 7322       "brief_des"
+00000a90: 3a22 e69f a5e7 9c8b e68e 92e8 a18c e6a6  :"..............
+00000aa0: 9c22 2c0d 0a20 2020 2020 2020 2022 6465  .",..        "de
+00000ab0: 7461 696c 5f64 6573 223a 22e9 8791 e5b8  tail_des":".....
+00000ac0: 81e6 8e92 e8a1 8c5c 6ee8 839c e59c bae6  .......\n.......
+00000ad0: 8e92 e8a1 8c5c 6ee8 b4a5 e59c bae6 8e92  .....\n.........
+00000ae0: e8a1 8c5c 6ee6 aca7 e6b4 b2e4 baba e68e  ...\n...........
+00000af0: 92e8 a18c 5c6e e685 88e5 9684 e5ae b6e6  ....\n..........
+00000b00: 8e92 e8a1 8c5c 6ee6 9fa5 e79c 8be8 b7af  .....\n.........
+00000b10: e781 afe6 8c82 e4bb b622 0d0a 2020 2020  ........."..    
+00000b20: 7d2c 0d0a 2020 2020 7b0d 0a20 2020 2020  },..    {..     
+00000b30: 2020 2022 6675 6e63 223a 22e8 bf9e e68e     "func":".....
+00000b40: a5e8 b4a6 e688 b722 2c0d 0a20 2020 2020  .......",..     
+00000b50: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
+00000b60: 6f64 223a 2231 2ee7 bea4 e586 85ef bc9a  od":"1..........
+00000b70: 4062 6f74 e585 b3e8 8194 e8b4 a6e6 88b7  @bot............
+00000b80: 2032 2ee7 a781 e881 8aef bc9a e585 b3e8   2..............
+00000b90: 8194 e8b4 a6e6 88b7 5c6e 222c 0d0a 2020  ........\n",..  
+00000ba0: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
+00000bb0: 6f6e 6469 7469 6f6e 223a 22e6 97a0 222c  ondition":"...",
+00000bc0: 0d0a 2020 2020 2020 2020 2262 7269 6566  ..        "brief
+00000bd0: 5f64 6573 223a 22e7 a781 e881 8ae6 8c87  _des":".........
+00000be0: e4bb a4e5 85b3 e881 94e5 88b0 e7be a4e3  ................
+00000bf0: 8082 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
+00000c00: 6574 6169 6c5f 6465 7322 3a22 e4bd a0e5  etail_des":"....
+00000c10: 8faf e4bb a5e5 9ca8 e7a7 81e8 818a e5ae  ................
+00000c20: 8ce6 8890 e4bb a5e4 b88b e693 8de4 bd9c  ................
+00000c30: efbc 9a5c 6ee7 adbe e588 b05c 6ee6 8abd  ...\n......\n...
+00000c40: e58d a15c 6ee6 9fa5 e79c 8be4 b8aa e4ba  ...\n...........
+00000c50: bae8 b4a6 e688 b7ef bc9a 5c6e e69f a5e7  ..........\n....
+00000c60: 9c8b e68e 92e8 a18c 5c6e e8b4 ade4 b9b0  ........\n......
+00000c70: e688 96e7 bb93 e7ae 97e8 82a1 e7a5 a822  ..............."
+00000c80: 0d0a 2020 2020 7d2c 0d0a 2020 2020 7b0d  ..    },..    {.
+00000c90: 0a20 2020 2020 2020 2022 6675 6e63 223a  .        "func":
+00000ca0: 22e4 bf84 e7bd 97e6 96af e8bd aee7 9b98  "...............
+00000cb0: 222c 0d0a 2020 2020 2020 2020 2274 7269  ",..        "tri
+00000cc0: 6767 6572 5f6d 6574 686f 6422 3a22 e8a3  gger_method":"..
+00000cd0: 85e5 bcb9 20e3 8090 e5ad 90e5 bcb9 e695  .... ...........
+00000ce0: b0e3 8091 20e3 8090 e987 91e9 a29d e380  .... ...........
+00000cf0: 9120 e380 9061 74e3 8091 222c 0d0a 2020  . ...at...",..  
+00000d00: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
+00000d10: 6f6e 6469 7469 6f6e 223a 22e8 b58c e6b3  ondition":".....
+00000d20: a8e4 b88a e999 90e4 b8ba e4b8 80e5 808d  ................
+00000d30: e8b5 8ce6 b3a8 e4b8 8ae9 9990 222c 0d0a  ............",..
+00000d40: 2020 2020 2020 2020 2262 7269 6566 5f64          "brief_d
+00000d50: 6573 223a 22e5 8f91 e8b5 b7e4 bf84 e7bd  es":"...........
+00000d60: 97e6 96af e8bd aee7 9b98 222c 0d0a 2020  ..........",..  
+00000d70: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
+00000d80: 7322 3a22 e980 9ae8 bf87 20e8 a385 e5bc  s":"...... .....
+00000d90: b920 e69d a5e5 afb9 e585 b6e4 bb96 e4ba  . ..............
+00000da0: bae5 8f91 e8b5 b7e5 86b3 e696 975c 6ee4  .............\n.
+00000db0: b88d 40e5 8899 e689 80e6 9c89 e7be a4e5  ..@.............
+00000dc0: 8f8b e983 bde5 8faf e68e a5e5 8f97 5c6e  ..............\n
+00000dd0: e8bd aee6 b581 e5bc 80e6 9eaa efbc 8ce7  ................
+00000de0: 9bb4 e588 b0e8 bf90 e6b0 94e4 b88d e5a5  ................
+00000df0: bde7 9a84 e4ba bae5 8588 e58e bbe4 b896  ................
+00000e00: e380 825c 6ee3 8090 e789 b9e6 ae8a e68a  ...\n...........
+00000e10: 80e8 83bd e380 91ef bc9a e5bc 80e6 9eaa  ................
+00000e20: 305c 6e5c 6ee3 8090 e5bc 80e5 a78b e6b8  0\n\n...........
+00000e30: b8e6 888f e380 915c 6ee8 a385 e5bc b920  .......\n...... 
+00000e40: e380 90e5 ad90 e5bc b9e6 95b0 e380 9120  ............... 
+00000e50: e380 90e9 8791 e9a2 9de3 8091 20e3 8090  ............ ...
+00000e60: 6174 e380 91ef bc88 e4b8 bae7 a9ba e588  at..............
+00000e70: 99e6 8980 e69c 89e7 bea4 e58f 8be9 83bd  ................
+00000e80: e58f afe6 8ea5 e58f 97ef bc89 5c6e e380  ............\n..
+00000e90: 90e5 9b9e e5ba 94e3 8091 5c6e e68e a5e5  ..........\n....
+00000ea0: 8f97 e68c 91e6 8898 5c2f e68b 92e7 bb9d  ........\/......
+00000eb0: e68c 91e6 8898 5c6e e380 90e5 9b9e e590  ......\n........
+00000ec0: 88e4 b8ad e380 915c 6ee5 bc80 e69e aa5c  .......\n......\
+00000ed0: 2fe5 9294 5c2f e598 ad5c 2fe5 98a3 205b  /...\/...\/... [
+00000ee0: e5ad 90e5 bcb9 e695 b05d efbc 88e9 bb98  .........]......
+00000ef0: e8ae a431 29ef bc88 e8bd aee6 b581 e5bc  ...1)...........
+00000f00: 80e6 9eaa efbc 895c 6ee3 8090 e7bb 93e7  .......\n.......
+00000f10: ae97 e380 915c 6ee7 bb93 e7ae 9720 efbc  .....\n...... ..
+00000f20: 88e5 bd93 e69f 90e4 b880 e696 b936 30e7  .............60.
+00000f30: a792 e69c aae5 bc80 e69e aaef bc8c e58f  ................
+00000f40: afe4 bdbf e794 a8e8 afa5 e591 bde4 bba4  ................
+00000f50: e7bb 93e6 9d9f e5af b9e5 86b3 e5b9 b6e8  ................
+00000f60: 839c e588 a9ef bc89 220d 0a20 2020 207d  ........"..    }
+00000f70: 2c0d 0a20 2020 207b 0d0a 2020 2020 2020  ,..    {..      
+00000f80: 2020 2266 756e 6322 3a22 e68e b7e9 aab0    "func":"......
+00000f90: e5ad 9022 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00000fa0: 7472 6967 6765 725f 6d65 7468 6f64 223a  trigger_method":
+00000fb0: 22e6 9187 e9aa b0e5 ad90 5c2f e68e b7e8  ".........\/....
+00000fc0: 89b2 e5ad 9020 e380 90e9 8791 e9a2 9de3  ..... ..........
+00000fd0: 8091 20e3 8090 6174 e380 9122 2c0d 0a20  .. ...at...",.. 
+00000fe0: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+00000ff0: 636f 6e64 6974 696f 6e22 3a22 e8b5 8ce6  condition":"....
+00001000: b3a8 e4b8 8ae9 9990 e4b8 bae4 ba94 e580  ................
+00001010: 8de8 b58c e6b3 a8e4 b88a e999 9022 2c0d  .............",.
+00001020: 0a20 2020 2020 2020 2022 6272 6965 665f  .        "brief_
+00001030: 6465 7322 3a22 e58f 91e8 b5b7 e68e b7e9  des":"..........
+00001040: aab0 e5ad 9022 2c0d 0a20 2020 2020 2020  .....",..       
+00001050: 2022 6465 7461 696c 5f64 6573 223a 22e9   "detail_des":".
+00001060: 809a e8bf 8720 e68e b7e9 aab0 e5ad 9020  ..... ......... 
+00001070: e69d a5e5 afb9 e585 b6e4 bb96 e4ba bae5  ................
+00001080: 8f91 e8b5 b7e5 86b3 e696 975c 6ee8 bdae  ...........\n...
+00001090: e6b5 81e5 bc80 e695 b0e6 af94 e5a4 a7e5  ................
+000010a0: b08f 5c6e e4b8 ade9 8094 e58f afe7 bb93  ..\n............
+000010b0: e69d 9f5c 6ee8 bdae e6b5 81e5 bc80 e695  ...\n...........
+000010c0: b0ef bc8c e585 88e6 af94 e7bb 84e5 9088  ................
+000010d0: efbc 8ce5 868d e6af 94e7 82b9 e695 b0e3  ................
+000010e0: 8082 5c6e e7bb 84e5 9088 efbc 9a5c 6ee5  ..\n.........\n.
+000010f0: bdb9 e6bb a120 3e20 e4b8 b220 3e20 e69d  ..... > ... > ..
+00001100: a120 3e20 e4b8 a4e5 afb9 203e 20e5 afb9  . > ...... > ...
+00001110: 203e 20e6 95a3 5c6e 5c6e e380 90e5 bc80   > ...\n\n......
+00001120: e5a7 8be6 b8b8 e688 8fe3 8091 5c6e e691  ............\n..
+00001130: 87e9 aab0 e5ad 905c 2fe6 8eb7 e889 b2e5  .......\/.......
+00001140: ad90 20e3 8090 e987 91e9 a29d e380 9120  .. ............ 
+00001150: e380 9061 74e3 8091 efbc 88e4 b8ba e7a9  ...at...........
+00001160: bae5 8899 e689 80e6 9c89 e7be a4e5 8f8b  ................
+00001170: e983 bde5 8faf e68e a5e5 8f97 efbc 895c  ...............\
+00001180: 6ee3 8090 e59b 9ee5 ba94 e380 915c 6ee6  n............\n.
+00001190: 8ea5 e58f 97e6 8c91 e688 985c 2fe6 8b92  ...........\/...
+000011a0: e7bb 9de6 8c91 e688 985c 6ee3 8090 e59b  .........\n.....
+000011b0: 9ee5 9088 e4b8 ade3 8091 5c6e e5bc 80e6  ..........\n....
+000011c0: 95b0 5c2f e5bc 80e7 82b9 5c2f e58f 96e5  ..\/......\/....
+000011d0: 87ba efbc 88e8 bdae e6b5 81e5 bc80 e695  ................
+000011e0: b0ef bc89 5c6e e380 90e7 bb93 e69d 9fe3  ....\n..........
+000011f0: 8091 5c6e e7bb 93e6 9d9f efbc 88e5 8faa  ..\n............
+00001200: e69c 89e6 9a82 e8b4 a5e6 96b9 e58f afe5  ................
+00001210: 8f91 e8b5 b7ef bc89 5c6e e380 90e7 bb93  ........\n......
+00001220: e7ae 97e3 8091 5c6e e7bb 93e7 ae97 efbc  ......\n........
+00001230: 88e5 bd93 e69f 90e4 b880 e696 b936 30e7  .............60.
+00001240: a792 e6b2 a1e6 9c89 e59b 9ee5 ba94 efbc  ................
+00001250: 8ce4 bba5 e79b aee5 898d e6af 94e5 8886  ................
+00001260: e7bb 93e7 ae97 efbc 8922 0d0a 2020 2020  ........."..    
+00001270: 7d2c 0d0a 2020 2020 7b0d 0a20 2020 2020  },..    {..     
+00001280: 2020 2022 6675 6e63 223a 22e6 8991 e585     "func":".....
+00001290: 8be5 afb9 e688 9822 2c0d 0a20 2020 2020  .......",..     
+000012a0: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
+000012b0: 6f64 223a 22e6 8991 e585 8be5 afb9 e688  od":"...........
+000012c0: 9820 e380 90e9 8791 e9a2 9de3 8091 20e3  . ............ .
+000012d0: 8090 6174 e380 9122 2c0d 0a20 2020 2020  ..at...",..     
+000012e0: 2020 2022 7472 6967 6765 725f 636f 6e64     "trigger_cond
+000012f0: 6974 696f 6e22 3a22 e8b5 8ce6 b3a8 e4b8  ition":"........
+00001300: 8ae9 9990 e4b8 bae4 b880 e580 8de8 b58c  ................
+00001310: e6b3 a8e4 b88a e999 9022 2c0d 0a20 2020  .........",..   
+00001320: 2020 2020 2022 6272 6965 665f 6465 7322       "brief_des"
+00001330: 3a22 e58f 91e8 b5b7 e689 91e5 858b e5af  :"..............
+00001340: b9e6 8898 222c 0d0a 2020 2020 2020 2020  ....",..        
+00001350: 2264 6574 6169 6c5f 6465 7322 3a22 e980  "detail_des":"..
+00001360: 9ae8 bf87 20e6 8991 e585 8be5 afb9 e688  .... ...........
+00001370: 9820 e69d a5e5 afb9 e585 b6e4 bb96 e4ba  . ..............
+00001380: bae5 afb9 e688 985c 6ee6 8993 e587 bae8  .......\n.......
+00001390: 87aa e5b7 b1e7 9a84 e689 8be7 898c 5c6e  ..............\n
+000013a0: e5bd 93e5 afb9 e696 b9e7 9a84 e8a1 80e9  ................
+000013b0: 878f e5b0 8fe4 ba8e 31e6 8896 e880 85e5  ........1.......
+000013c0: 9ca8 e887 aae5 b7b1 e59b 9ee5 9088 e587  ................
+000013d0: bae7 898c e589 8de8 a180 e987 8f3e 3430  .............>40
+000013e0: e58d b3e5 8faf e88e b7e8 839c 5c6e e789  ............\n..
+000013f0: 8ce5 ba93 e4b8 80e5 85b1 3532 e5bc a0e7  ..........52....
+00001400: 898c efbc 8ce5 bd93 e789 8ce5 ba93 e6b2  ................
+00001410: a1e6 9c89 e789 8ce4 ba86 e5b0 b1e4 bba5  ................
+00001420: e79b aee5 898d e8a1 80e9 878f e7bb 93e7  ................
+00001430: ae97 efbc 8ce7 bb93 e69d 9fe6 b8b8 e688  ................
+00001440: 8fe3 8082 5c6e 5c6e e585 88e6 898b e588  ....\n\n........
+00001450: 9de5 a78b e782 b9e6 95b0 efbc 9a48 5020  .............HP 
+00001460: 3230 2053 5020 3020 4445 4620 305c 6ee5  20 SP 0 DEF 0\n.
+00001470: 908e e689 8be5 889d e5a7 8be7 82b9 e695  ................
+00001480: b0ef bc9a 4850 2032 3520 5350 2032 2044  ....HP 25 SP 2 D
+00001490: 4546 2030 5c6e e6af 8fe5 9b9e e590 88e6  EF 0\n..........
+000014a0: 8abd e4b8 89e5 bca0 e789 8cef bc8c e689  ................
+000014b0: 93e5 87ba e585 b6e4 b8ad e79a 84e4 b880  ................
+000014c0: e5bc a0e4 bd9c e4b8 bae8 a18c e58a a8e7  ................
+000014d0: 898c efbc 8ce5 bc83 e68e 89e5 89a9 e4bd  ................
+000014e0: 99e6 898b e789 8ce3 8082 5c6e efbc 88e7  ..........\n....
+000014f0: 89b9 e588 abe6 b3a8 e684 8fef bc9a e998  ................
+00001500: b2e5 bea1 e789 8ce4 bd9c e4b8 bae8 a18c  ................
+00001510: e58a a8e7 898c e698 afe6 94bb e587 bbef  ................
+00001520: bc89 5c6e e4b9 8be5 908e e5af b9e6 96b9  ..\n............
+00001530: e691 87e4 b880 e4b8 aa32 30e9 9da2 e9aa  .........20.....
+00001540: b0e5 ad90 efbc 8c5c 6ee5 a682 e69e 9ce7  .......\n.......
+00001550: 82b9 e695 b0e5 b08f e4ba 8ee5 afb9 e696  ................
+00001560: b953 50e5 8899 e4bb 8ee7 898c e5ba 93e7  .SP.............
+00001570: bfbb e587 bae4 b880 e5bc a0e7 898c e4bd  ................
+00001580: 9ce4 b8ba e68a 80e8 83bd e789 8ce6 8993  ................
+00001590: e587 bae3 8082 5c6e e68c 89e7 85a7 e68a  ......\n........
+000015a0: 80e8 83bd e789 8ce7 82b9 e695 b0e6 89a3  ................
+000015b0: e999 a4e5 afb9 e696 b953 50e7 82b9 e380  .........SP.....
+000015c0: 825c 6e5c 6e3c 6674 2073 697a 653d 3330  .\n\n<ft size=30
+000015d0: 2063 6f6c 6f72 3d62 6c61 636b 3ee9 bb91   color=black>...
+000015e0: e6a1 833c 5c2f 6674 3e5c 6ee6 8f8f e8bf  ...<\/ft>\n.....
+000015f0: b0ef bc9a e998 b2e5 bea1 5c6e e8a1 8ce5  ..........\n....
+00001600: 8aa8 e789 8ce6 9588 e69e 9cef bc9a e689  ................
+00001610: 93e5 87ba e694 bbe5 87bb 5c6e e68a 80e8  ..........\n....
+00001620: 83bd e789 8ce6 9588 e69e 9cef bc9a e5a2  ................
+00001630: 9ee5 8aa0 4445 465c 6e3c 6674 2073 697a  ....DEF\n<ft siz
+00001640: 653d 3330 2063 6f6c 6f72 3d72 6564 3ee7  e=30 color=red>.
+00001650: baa2 e6a1 833c 5c2f 6674 3e5c 6ee6 8f8f  .....<\/ft>\n...
+00001660: e8bf b0ef bc9a e794 9fe5 91bd 5c6e e8a1  ............\n..
+00001670: 8ce5 8aa8 e789 8ce6 9588 e69e 9cef bc9a  ................
+00001680: e681 a2e5 a48d 4850 5c6e e68a 80e8 83bd  ......HP\n......
+00001690: e789 8ce6 9588 e69e 9cef bc9a e681 a2e5  ................
+000016a0: a48d 4850 5c6e 3c66 7420 7369 7a65 3d33  ..HP\n<ft size=3
+000016b0: 3020 636f 6c6f 723d 626c 6163 6b3e e6a2  0 color=black>..
+000016c0: 85e8 8ab1 3c5c 2f66 743e 5c6e e68f 8fe8  ....<\/ft>\n....
+000016d0: bfb0 efbc 9ae6 8a80 e883 bd5c 6ee8 a18c  ...........\n...
+000016e0: e58a a8e7 898c e695 88e6 9e9c efbc 9ae4  ................
+000016f0: b8bb e58a a8e6 8a80 e883 bd5c 6ee6 8a80  ...........\n...
+00001700: e883 bde7 898c e695 88e6 9e9c efbc 9ae5  ................
+00001710: a29e e58a a053 505c 6e3c 6674 2073 697a  .....SP\n<ft siz
+00001720: 653d 3330 2063 6f6c 6f72 3d72 6564 3ee6  e=30 color=red>.
+00001730: 96b9 e789 873c 5c2f 6674 3e5c 6ee6 8f8f  .....<\/ft>\n...
+00001740: e8bf b0ef bc9a e694 bbe5 87bb e8a1 8ce5  ................
+00001750: 8aa8 e789 8ce6 9588 e69e 9cef bc9a e689  ................
+00001760: 93e5 87ba e694 bbe5 87bb 5c6e e68a 80e8  ..........\n....
+00001770: 83bd e789 8ce6 9588 e69e 9cef bc9a e689  ................
+00001780: 93e5 87ba e58f 8de5 87bb 5c6e 5c6e e4b8  ..........\n\n..
+00001790: bbe5 8aa8 e68a 80e8 83bd efbc 9a5c 6ee6  .............\n.
+000017a0: 9187 e4b8 80e4 b8aa 3230 e99d a2e9 aab0  ........20......
+000017b0: e5ad 905c 6ee5 a682 e69e 9ce7 82b9 e695  ...\n...........
+000017c0: b0e5 b08f e4ba 8ee8 87aa e8ba ab53 50e5  .............SP.
+000017d0: 8899 e68a 8ae5 89a9 e4bd 99e4 b8a4 e5bc  ................
+000017e0: a0e6 898b e789 8ce4 bd9c e4b8 bae6 8a80  ................
+000017f0: e883 bde7 898c e585 a8e9 83a8 e689 93e5  ................
+00001800: 87ba 5c6e e68c 89e7 85a7 e68a 80e8 83bd  ..\n............
+00001810: e789 8ce7 82b9 e695 b0e6 89a3 e999 a4e8  ................
+00001820: 87aa e8ba ab53 50e7 82b9 4143 45e6 8a80  .....SP...ACE...
+00001830: e883 bdef bc9a 5c6e e691 87e4 b880 e4b8  ......\n........
+00001840: aa36 e99d a2e9 aab0 e5ad 905c 6ee6 8a8a  .6.........\n...
+00001850: e689 93e5 87ba e79a 8441 4345 e789 8ce7  .........ACE....
+00001860: 82b9 e69b bfe6 8da2 e688 90e6 9187 e587  ................
+00001870: bae7 9a84 e782 b9e6 95b0 5c6e e586 8de6  ..........\n....
+00001880: 8a8a e4b8 89e5 bca0 e689 8be7 898c e585  ................
+00001890: a8e9 83a8 e4bd 9ce4 b8ba e68a 80e8 83bd  ................
+000018a0: e789 8ce6 8993 e587 ba5c 6ee6 8c89 e785  .........\n.....
+000018b0: a7e6 8a80 e883 bde7 898c e782 b9e6 95b0  ................
+000018c0: e689 a3e9 99a4 e887 aae8 baab 5350 e782  ............SP..
+000018d0: b95c 6e5c 6ee3 8090 e5bc 80e5 a78b e6b8  .\n\n...........
+000018e0: b8e6 888f e380 915c 6ee6 8991 e585 8be5  .......\n.......
+000018f0: afb9 e688 9820 e380 90e9 8791 e9a2 9de3  ..... ..........
+00001900: 8091 20e3 8090 6174 e380 91ef bc88 e4b8  .. ...at........
+00001910: bae7 a9ba e588 99e6 8980 e69c 89e7 bea4  ................
+00001920: e58f 8be9 83bd e58f afe6 8ea5 e58f 97ef  ................
+00001930: bc89 5c6e e380 90e5 9b9e e5ba 94e3 8091  ..\n............
+00001940: 5c6e e68e a5e5 8f97 e68c 91e6 8898 5c2f  \n............\/
+00001950: e68b 92e7 bb9d e68c 91e6 8898 5c6e e380  ............\n..
+00001960: 90e5 9b9e e590 88e4 b8ad e380 915c 6ee5  .............\n.
+00001970: 87ba e789 8c20 315c 2f32 5c2f 33ef bc88  ..... 1\/2\/3...
+00001980: e8bd aee6 b581 e587 bae7 898c efbc 895c  ...............\
+00001990: 6ee3 8090 e7bb 93e7 ae97 e380 915c 6ee7  n............\n.
+000019a0: bb93 e7ae 97ef bc88 e5bd 93e6 9f90 e4b8  ................
+000019b0: 80e6 96b9 3630 e7a7 92e6 b2a1 e69c 89e5  ....60..........
+000019c0: 9b9e e5ba 94ef bc8c e4bb a5e7 9bae e589  ................
+000019d0: 8de8 a180 e987 8fe7 bb93 e7ae 97ef bc89  ................
+000019e0: 220d 0a20 2020 207d 2c0d 0a20 2020 207b  "..    },..    {
+000019f0: 0d0a 2020 2020 2020 2020 2266 756e 6322  ..        "func"
+00001a00: 3a22 e8b5 9be9 a9ac e5b0 8fe6 b8b8 e688  :"..............
+00001a10: 8f22 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
+00001a20: 6967 6765 725f 6d65 7468 6f64 223a 22e8  igger_method":".
+00001a30: b59b e9a9 ace5 889b e5bb ba22 2c0d 0a20  ...........",.. 
+00001a40: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+00001a50: 636f 6e64 6974 696f 6e22 3a22 e697 a022  condition":"..."
+00001a60: 2c0d 0a20 2020 2020 2020 2022 6272 6965  ,..        "brie
+00001a70: 665f 6465 7322 3a22 e588 9be5 bbba e8b5  f_des":"........
+00001a80: 9be9 a9ac e5b0 8fe6 b8b8 e688 8f22 2c0d  .............",.
+00001a90: 0a20 2020 2020 2020 2022 6465 7461 696c  .        "detail
+00001aa0: 5f64 6573 223a 22e6 b581 e7a8 8bef bc9a  _des":".........
+00001ab0: 5c6e e8b5 9be9 a9ac e588 9be5 bbba efbc  \n..............
+00001ac0: 9ae7 acac e4b8 80e4 bd8d e78e a9e5 aeb6  ................
+00001ad0: e58f 91e8 b5b7 e6b4 bbe5 8aa8 20e2 8692  ............ ...
+00001ae0: 5c6e e8b5 9be9 a9ac e58a a0e5 85a5 20e3  \n............ .
+00001af0: 8090 e4bd a0e7 9a84 e9a9 ace5 84bf e590  ................
+00001b00: 8de7 a7b0 e380 91ef bc9a e78e a9e5 aeb6  ................
+00001b10: e58f 82e8 b59b 20e2 8692 5c6e e8b5 9be9  ...... ...\n....
+00001b20: a9ac e5bc 80e5 a78b efbc 9ae6 b8b8 e688  ................
+00001b30: 8fe8 bf9b e8a1 8c20 e286 925c 6ee8 bf9b  ....... ...\n...
+00001b40: e8a1 8ce4 b8ad 20e2 8692 5c6e e7bb 93e7  ...... ...\n....
+00001b50: ae97 5c6e 5c6e e5bd 93e9 8187 e588 b0e9  ..\n\n..........
+00001b60: 9499 e8af afe6 8896 e585 b6e4 bb96 e683  ................
+00001b70: 85e5 86b5 e58f afe4 bdbf e794 a8e8 b59b  ................
+00001b80: e9a9 ace9 878d e7bd aee6 9da5 e987 8de7  ................
+00001b90: bdae e9a9 ace5 9cba e380 8222 0d0a 2020  ..........."..  
+00001ba0: 2020 7d2c 0d0a 2020 2020 7b0d 0a20 2020    },..    {..   
+00001bb0: 2020 2020 2022 6675 6e63 223a 22e5 b882       "func":"...
+00001bc0: e59c bae4 bfa1 e681 af22 2c0d 0a20 2020  .........",..   
+00001bd0: 2020 2020 2022 7472 6967 6765 725f 6d65       "trigger_me
+00001be0: 7468 6f64 223a 22e5 b882 e59c bae4 bfa1  thod":".........
+00001bf0: e681 af22 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00001c00: 7472 6967 6765 725f 636f 6e64 6974 696f  trigger_conditio
+00001c10: 6e22 3a22 e697 a022 2c0d 0a20 2020 2020  n":"...",..     
+00001c20: 2020 2022 6272 6965 665f 6465 7322 3a22     "brief_des":"
+00001c30: e69f a5e7 9c8b e5b8 82e5 9cba e4bf a1e6  ................
+00001c40: 81af 222c 0d0a 2020 2020 2020 2020 2264  ..",..        "d
+00001c50: 6574 6169 6c5f 6465 7322 3a22 e69f a5e7  etail_des":"....
+00001c60: 9c8b e5b8 82e5 9cba e4b8 8ae6 8980 e69c  ................
+00001c70: 89e5 85ac e58f b8e7 9a84 e5ae 98e6 96b9  ................
+00001c80: e7bb 93e7 ae97 e4bb b7e6 a0bc 220d 0a20  ............".. 
+00001c90: 2020 207d 2c0d 0a20 2020 207b 0d0a 2020     },..    {..  
+00001ca0: 2020 2020 2020 2266 756e 6322 3a22 e78e        "func":"..
+00001cb0: a9e5 aeb6 e5b8 82e5 9cba e4bf a1e6 81af  ................
+00001cc0: 222c 0d0a 2020 2020 2020 2020 2274 7269  ",..        "tri
+00001cd0: 6767 6572 5f6d 6574 686f 6422 3a22 e5b8  gger_method":"..
+00001ce0: 82e5 9cba e4bf a1e6 81af 20e3 8090 e585  .......... .....
+00001cf0: ace5 8fb8 e590 8de7 a7b0 e380 9122 2c0d  .............",.
+00001d00: 0a20 2020 2020 2020 2022 7472 6967 6765  .        "trigge
+00001d10: 725f 636f 6e64 6974 696f 6e22 3a22 e697  r_condition":"..
+00001d20: a022 2c0d 0a20 2020 2020 2020 2022 6272  .",..        "br
+00001d30: 6965 665f 6465 7322 3a22 e69f a5e7 9c8b  ief_des":"......
+00001d40: e380 90e5 85ac e58f b8e5 908d e7a7 b0e3  ................
+00001d50: 8091 e882 a1e4 bbbd e68a a5e4 bbb7 222c  ..............",
+00001d60: 0d0a 2020 2020 2020 2020 2264 6574 6169  ..        "detai
+00001d70: 6c5f 6465 7322 3a22 220d 0a20 2020 207d  l_des":""..    }
+00001d80: 2c0d 0a20 2020 207b 0d0a 2020 2020 2020  ,..    {..      
+00001d90: 2020 2266 756e 6322 3a22 e5b8 82e5 9cba    "func":"......
+00001da0: e8a1 8ce6 8385 222c 0d0a 2020 2020 2020  ......",..      
+00001db0: 2020 2274 7269 6767 6572 5f6d 6574 686f    "trigger_metho
+00001dc0: 6422 3a22 e5b8 82e5 9cba e8a1 8ce6 8385  d":"............
+00001dd0: 222c 0d0a 2020 2020 2020 2020 2274 7269  ",..        "tri
+00001de0: 6767 6572 5f63 6f6e 6469 7469 6f6e 223a  gger_condition":
+00001df0: 22e6 97a0 222c 0d0a 2020 2020 2020 2020  "...",..        
+00001e00: 2262 7269 6566 5f64 6573 223a 22e6 9fa5  "brief_des":"...
+00001e10: e79c 8be5 b882 e59c bae8 a18c e683 8522  ..............."
+00001e20: 2c0d 0a20 2020 2020 2020 2022 6465 7461  ,..        "deta
+00001e30: 696c 5f64 6573 223a 2222 0d0a 2020 2020  il_des":""..    
+00001e40: 7d2c 0d0a 2020 2020 7b0d 0a20 2020 2020  },..    {..     
+00001e50: 2020 2022 6675 6e63 223a 22e5 85ac e58f     "func":".....
+00001e60: b8e4 bfa1 e681 af22 2c0d 0a20 2020 2020  .......",..     
+00001e70: 2020 2022 7472 6967 6765 725f 6d65 7468     "trigger_meth
+00001e80: 6f64 223a 22e5 85ac e58f b8e4 bfa1 e681  od":"...........
+00001e90: af20 e380 90e5 85ac e58f b8e5 908d e7a7  . ..............
+00001ea0: b0e3 8091 222c 0d0a 2020 2020 2020 2020  ....",..        
+00001eb0: 2274 7269 6767 6572 5f63 6f6e 6469 7469  "trigger_conditi
+00001ec0: 6f6e 223a 22e6 97a0 222c 0d0a 2020 2020  on":"...",..    
+00001ed0: 2020 2020 2262 7269 6566 5f64 6573 223a      "brief_des":
+00001ee0: 22e6 9fa5 e79c 8be5 85ac e58f b8e7 9a84  "...............
+00001ef0: e8af a6e7 bb86 e4bf a1e6 81af 222c 0d0a  ............",..
+00001f00: 2020 2020 2020 2020 2264 6574 6169 6c5f          "detail_
+00001f10: 6465 7322 3a22 220d 0a20 2020 207d 2c0d  des":""..    },.
+00001f20: 0a20 2020 207b 0d0a 2020 2020 2020 2020  .    {..        
+00001f30: 2266 756e 6322 3a22 e58f 91e8 a18c e8b4  "func":"........
+00001f40: ade4 b9b0 222c 0d0a 2020 2020 2020 2020  ....",..        
+00001f50: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
+00001f60: 3a22 e58f 91e8 a18c e8b4 ade4 b9b0 20e3  :"............ .
+00001f70: 8090 e585 ace5 8fb8 e590 8de7 a7b0 e380  ................
+00001f80: 9120 e380 904e e380 9122 2c0d 0a20 2020  . ...N...",..   
+00001f90: 2020 2020 2022 7472 6967 6765 725f 636f       "trigger_co
+00001fa0: 6e64 6974 696f 6e22 3a22 e697 a022 2c0d  ndition":"...",.
+00001fb0: 0a20 2020 2020 2020 2022 6272 6965 665f  .        "brief_
+00001fc0: 6465 7322 3a22 e4bb 8ee5 ae98 e696 b9e8  des":"..........
+00001fd0: b4ad e4b9 b0e8 82a1 e7a5 a822 2c0d 0a20  ...........",.. 
+00001fe0: 2020 2020 2020 2022 6465 7461 696c 5f64         "detail_d
+00001ff0: 6573 223a 22e4 bba5 e58f 91e8 a18c e4bb  es":"...........
+00002000: b7e6 a0bc e4bb 8e20 e380 90e5 85ac e58f  ....... ........
+00002010: b8e5 908d e7a7 b0e3 8091 e8b4 ade4 b9b0  ................
+00002020: 4ee8 82a1 e69c ace5 85ac e58f b8e8 82a1  N...............
+00002030: e4bb bde3 8082 220d 0a20 2020 207d 2c0d  ......"..    },.
+00002040: 0a20 2020 207b 0d0a 2020 2020 2020 2020  .    {..        
+00002050: 2266 756e 6322 3a22 e5ae 98e6 96b9 e7bb  "func":"........
+00002060: 93e7 ae97 222c 0d0a 2020 2020 2020 2020  ....",..        
+00002070: 2274 7269 6767 6572 5f6d 6574 686f 6422  "trigger_method"
+00002080: 3a22 e5ae 98e6 96b9 e7bb 93e7 ae97 20e3  :"............ .
+00002090: 8090 e585 ace5 8fb8 e590 8de7 a7b0 e380  ................
+000020a0: 9120 e380 904e e380 9122 2c0d 0a20 2020  . ...N...",..   
+000020b0: 2020 2020 2022 7472 6967 6765 725f 636f       "trigger_co
+000020c0: 6e64 6974 696f 6e22 3a22 e697 a022 2c0d  ndition":"...",.
+000020d0: 0a20 2020 2020 2020 2022 6272 6965 665f  .        "brief_
+000020e0: 6465 7322 3a22 e4bb 8ee5 ae98 e696 b9e7  des":"..........
+000020f0: bb93 e7ae 97e8 82a1 e7a5 a822 2c0d 0a20  ...........",.. 
+00002100: 2020 2020 2020 2022 6465 7461 696c 5f64         "detail_d
+00002110: 6573 223a 22e4 bba5 e7bb 93e7 ae97 e4bb  es":"...........
+00002120: b7e6 a0bc e590 91e3 8090 e585 ace5 8fb8  ................
+00002130: e590 8de7 a7b0 e380 91e5 8d96 e587 ba4e  ...............N
+00002140: e882 a1e6 9cac e585 ace5 8fb8 e882 a1e4  ................
+00002150: bbbd e380 8222 0d0a 2020 2020 7d2c 0d0a  ....."..    },..
+00002160: 2020 2020 7b0d 0a20 2020 2020 2020 2022      {..        "
+00002170: 6675 6e63 223a 22e8 b4ad e4b9 b0e8 82a1  func":".........
+00002180: e7a5 a822 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00002190: 7472 6967 6765 725f 6d65 7468 6f64 223a  trigger_method":
+000021a0: 22e8 b4ad e4b9 b020 e380 90e5 85ac e58f  "...... ........
+000021b0: b8e5 908d e7a7 b0e3 8091 20e3 8090 4ee3  .......... ...N.
+000021c0: 8091 222c 0d0a 2020 2020 2020 2020 2274  ..",..        "t
+000021d0: 7269 6767 6572 5f63 6f6e 6469 7469 6f6e  rigger_condition
+000021e0: 223a 22e6 97a0 222c 0d0a 2020 2020 2020  ":"...",..      
+000021f0: 2020 2262 7269 6566 5f64 6573 223a 22e4    "brief_des":".
+00002200: bb8e e78e a9e5 aeb6 e5b8 82e5 9cba e8b4  ................
+00002210: ade4 b9b0 e882 a1e7 a5a8 222c 0d0a 2020  ..........",..  
+00002220: 2020 2020 2020 2264 6574 6169 6c5f 6465        "detail_de
+00002230: 7322 3a22 e4bb a5e4 bb8e e4bd 8ee5 88b0  s":"............
+00002240: e9ab 98e7 9a84 e68a a5e4 bbb7 e4b9 b0e5  ................
+00002250: 85a5 4ee8 82a1 e5b8 82e5 9cba e4b8 ade7  ..N.............
+00002260: 9a84 e380 90e5 85ac e58f b8e5 908d e7a7  ................
+00002270: b0e3 8091 e380 8222 0d0a 2020 2020 7d2c  ......."..    },
+00002280: 0d0a 2020 2020 7b0d 0a20 2020 2020 2020  ..    {..       
+00002290: 2022 6675 6e63 223a 22e5 87ba e594 aee8   "func":".......
+000022a0: 82a1 e7a5 a822 2c0d 0a20 2020 2020 2020  .....",..       
+000022b0: 2022 7472 6967 6765 725f 6d65 7468 6f64   "trigger_method
+000022c0: 223a 22e5 87ba e594 ae20 e380 90e5 85ac  ":"...... ......
+000022d0: e58f b8e5 908d e7a7 b0e3 8091 20e3 8090  ............ ...
+000022e0: e68a a5e4 bbb7 e380 9120 e380 904e e380  ......... ...N..
+000022f0: 9122 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
+00002300: 6967 6765 725f 636f 6e64 6974 696f 6e22  igger_condition"
+00002310: 3a22 e697 a022 2c0d 0a20 2020 2020 2020  :"...",..       
+00002320: 2022 6272 6965 665f 6465 7322 3a22 e4bb   "brief_des":"..
+00002330: 8ee7 8ea9 e5ae b6e5 b882 e59c bae5 87ba  ................
+00002340: e594 aee8 82a1 e7a5 a822 2c0d 0a20 2020  .........",..   
+00002350: 2020 2020 2022 6465 7461 696c 5f64 6573       "detail_des
+00002360: 223a 22e5 b086 e887 aae5 b7b1 e689 8be4  ":".............
+00002370: b8ad e79a 84e3 8090 e585 ace5 8fb8 e590  ................
+00002380: 8de7 a7b0 e380 9120 e4bb a5e3 8090 e68a  ....... ........
+00002390: a5e4 bbb7 e380 91e5 8f91 e5b8 83e5 88b0  ................
+000023a0: e5b8 82e5 9cba 4ee8 82a1 e380 8222 0d0a  ......N......"..
+000023b0: 2020 2020 7d2c 0d0a 2020 2020 7b0d 0a20      },..    {.. 
+000023c0: 2020 2020 2020 2022 6675 6e63 223a 22e5         "func":".
+000023d0: b882 e59c bae6 b3a8 e586 8c22 2c0d 0a20  ...........",.. 
+000023e0: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+000023f0: 6d65 7468 6f64 223a 22e5 b882 e59c bae6  method":".......
+00002400: b3a8 e586 8c20 e380 90e5 85ac e58f b8e5  ..... ..........
+00002410: 908d e7a7 b0e3 8091 222c 0d0a 2020 2020  ........",..    
+00002420: 2020 2020 2274 7269 6767 6572 5f63 6f6e      "trigger_con
+00002430: 6469 7469 6f6e 223a 22e9 9c80 e8a6 8140  dition":"......@
+00002440: 626f 74e6 8896 e58f ab62 6f74 e79a 84e5  bot......bot....
+00002450: 908d e5ad 97ef bc8c e68c 87e4 bba4 e69d  ................
+00002460: 83e9 9990 efbc 9ae7 aea1 e790 86e5 9198  ................
+00002470: e380 8222 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00002480: 6272 6965 665f 6465 7322 3a22 e688 90e7  brief_des":"....
+00002490: ab8b e585 ace5 8fb8 222c 0d0a 2020 2020  ........",..    
+000024a0: 2020 2020 2264 6574 6169 6c5f 6465 7322      "detail_des"
+000024b0: 3a22 e5b0 86e6 9cac e7be a4e4 bba5 e380  :"..............
+000024c0: 90e5 85ac e58f b8e5 908d e7a7 b0e3 8091  ................
+000024d0: e6b3 a8e5 868c e588 b0e5 b882 e59c baef  ................
+000024e0: bc8c 5c6e e5a6 82e6 9e9c e585 a8e7 bea4  ..\n............
+000024f0: e987 91e5 b881 e695 b0e5 b08f e4ba 8ee4  ................
+00002500: b8a4 e4b8 87e5 8899 e4bc 9ae6 b3a8 e586  ................
+00002510: 8ce5 a4b1 e8b4 a5e3 8082 220d 0a20 2020  .........."..   
+00002520: 207d 2c0d 0a20 2020 207b 0d0a 2020 2020   },..    {..    
+00002530: 2020 2020 2266 756e 6322 3a22 e69b b4e6      "func":"....
+00002540: 96b0 e585 ace5 8fb8 e7ae 80e4 bb8b 222c  ..............",
+00002550: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
+00002560: 6572 5f6d 6574 686f 6422 3a22 e69b b4e6  er_method":"....
+00002570: 96b0 e585 ace5 8fb8 e7ae 80e4 bb8b 20e3  .............. .
+00002580: 8090 e7ae 80e4 bb8b e586 85e5 aeb9 e380  ................
+00002590: 9122 2c0d 0a20 2020 2020 2020 2022 7472  .",..        "tr
+000025a0: 6967 6765 725f 636f 6e64 6974 696f 6e22  igger_condition"
+000025b0: 3a22 e68c 87e4 bba4 e69d 83e9 9990 efbc  :"..............
+000025c0: 9ae7 aea1 e790 86e5 9198 222c 0d0a 2020  ..........",..  
+000025d0: 2020 2020 2020 2262 7269 6566 5f64 6573        "brief_des
+000025e0: 223a 22e6 9bb4 e696 b0e5 85ac e58f b8e7  ":".............
+000025f0: ae80 e4bb 8b22 2c0d 0a20 2020 2020 2020  .....",..       
+00002600: 2022 6465 7461 696c 5f64 6573 223a 22e5   "detail_des":".
+00002610: b086 e380 90e7 ae80 e4bb 8be5 8685 e5ae  ................
+00002620: b9e3 8091 e6b7 bbe5 8aa0 e588 b0e6 9cac  ................
+00002630: e7be a4e5 85ac e58f b8e8 b584 e696 99e7  ................
+00002640: 9a84 e7ae 80e4 bb8b e4b8 ad22 0d0a 2020  ..........."..  
+00002650: 2020 7d2c 0d0a 2020 2020 7b0d 0a20 2020    },..    {..   
+00002660: 2020 2020 2022 6675 6e63 223a 22e7 aea1       "func":"...
+00002670: e790 86e5 9198 e69b b4e6 96b0 e585 ace5  ................
+00002680: 8fb8 e7ae 80e4 bb8b 222c 0d0a 2020 2020  ........",..    
+00002690: 2020 2020 2274 7269 6767 6572 5f6d 6574      "trigger_met
+000026a0: 686f 6422 3a22 e7ae a1e7 9086 e591 98e6  hod":"..........
+000026b0: 9bb4 e696 b0e5 85ac e58f b8e7 ae80 e4bb  ................
+000026c0: 8b20 e380 90e5 85ac e58f b8e5 908d e7a7  . ..............
+000026d0: b0e3 8091 20e3 8090 e7ae 80e4 bb8b e586  .... ...........
+000026e0: 85e5 aeb9 e380 9122 2c0d 0a20 2020 2020  .......",..     
+000026f0: 2020 2022 7472 6967 6765 725f 636f 6e64     "trigger_cond
+00002700: 6974 696f 6e22 3a22 e68c 87e4 bba4 e69d  ition":"........
+00002710: 83e9 9990 efbc 9ae8 b685 e7ae a122 2c0d  .............",.
+00002720: 0a20 2020 2020 2020 2022 6272 6965 665f  .        "brief_
+00002730: 6465 7322 3a22 e69b b4e6 96b0 e585 ace5  des":"..........
+00002740: 8fb8 e7ae 80e4 bb8b 222c 0d0a 2020 2020  ........",..    
+00002750: 2020 2020 2264 6574 6169 6c5f 6465 7322      "detail_des"
+00002760: 3a22 e5b0 86e3 8090 e7ae 80e4 bb8b e586  :"..............
+00002770: 85e5 aeb9 e380 91e6 b7bb e58a a0e5 88b0  ................
+00002780: e380 90e5 85ac e58f b8e5 908d e7a7 b0e3  ................
+00002790: 8091 e8b5 84e6 9699 e79a 84e7 ae80 e4bb  ................
+000027a0: 8be4 b8ad e380 8222 0d0a 2020 2020 7d2c  ......."..    },
+000027b0: 0d0a 2020 2020 7b0d 0a20 2020 2020 2020  ..    {..       
+000027c0: 2022 6675 6e63 223a 22e8 b584 e4ba a7e8   "func":".......
+000027d0: b083 e69f a522 2c0d 0a20 2020 2020 2020  .....",..       
+000027e0: 2022 7472 6967 6765 725f 6d65 7468 6f64   "trigger_method
+000027f0: 223a 2231 2ee8 b584 e4ba a7e8 b083 e69f  ":"1............
+00002800: a520 322e e8b5 84e4 baa7 e8b0 83e6 9fa5  . 2.............
+00002810: 4073 6f6d 656f 6e65 5c6e 222c 0d0a 2020  @someone\n",..  
+00002820: 2020 2020 2020 2274 7269 6767 6572 5f63        "trigger_c
+00002830: 6f6e 6469 7469 6f6e 223a 22e6 8c87 e4bb  ondition":".....
+00002840: a4e6 9d83 e999 90ef bc9a e7ae a1e7 9086  ................
+00002850: e591 9822 2c0d 0a20 2020 2020 2020 2022  ...",..        "
+00002860: 6272 6965 665f 6465 7322 3a22 e8b0 83e6  brief_des":"....
+00002870: 9fa5 e794 a8e6 88b7 e79a 84e8 b584 e4ba  ................
+00002880: a7e5 8886 e5b8 83e6 8385 e586 b5e3 8082  ................
+00002890: 222c 0d0a 2020 2020 2020 2020 2264 6574  ",..        "det
+000028a0: 6169 6c5f 6465 7322 3a22 e5a6 82e6 9e9c  ail_des":"......
+000028b0: e69c aae6 8c87 e5ae 9ae7 94a8 e688 b7ef  ................
+000028c0: bc8c e588 99e8 b083 e69f a5e7 8ea9 e5ae  ................
+000028d0: b6e6 80bb e8b5 84e4 baa7 e589 8de5 8d81  ................
+000028e0: e590 8de7 9a84 e8b5 84e4 baa7 e588 86e5  ................
+000028f0: b883 e683 85e5 86b5 e380 8222 0d0a 2020  ..........."..  
+00002900: 2020 7d2c 0d0a 2020 2020 7b0d 0a20 2020    },..    {..   
+00002910: 2020 2020 2022 6675 6e63 223a 22e5 86bb       "func":"...
+00002920: e7bb 93e8 b584 e4ba a722 2c0d 0a20 2020  .........",..   
+00002930: 2020 2020 2022 7472 6967 6765 725f 6d65       "trigger_me
+00002940: 7468 6f64 223a 22e5 86bb e7bb 93e8 b584  thod":".........
+00002950: e4ba a740 736f 6d65 6f6e 6522 2c0d 0a20  ...@someone",.. 
+00002960: 2020 2020 2020 2022 7472 6967 6765 725f         "trigger_
+00002970: 636f 6e64 6974 696f 6e22 3a22 e68c 87e4  condition":"....
+00002980: bba4 e69d 83e9 9990 efbc 9ae8 b685 e7ae  ................
+00002990: a122 2c0d 0a20 2020 2020 2020 2022 6272  .",..        "br
+000029a0: 6965 665f 6465 7322 3a22 e69f a5e5 b081  ief_des":"......
+000029b0: 6174 e79a 84e7 bea4 e58f 8be7 9a84 e585  at..............
+000029c0: a8e9 83a8 e8b5 84e4 baa7 e380 8222 2c0d  .............",.
+000029d0: 0a20 2020 2020 2020 2022 6465 7461 696c  .        "detail
+000029e0: 5f64 6573 223a 22e6 9fa5 e5b0 81e5 908e  _des":".........
+000029f0: e79a 84e7 94a8 e688 b7e4 bc9a e68c 81e6  ................
+00002a00: 9c89 e69c 80e5 a49a 3530 30e4 b8aa e585  ........500.....
+00002a10: a8e5 b180 e981 93e5 85b7 e380 90e8 a2ab  ................
+00002a20: e586 bbe7 bb93 e79a 84e8 b584 e4ba a7e3  ................
+00002a30: 8091 efbc 8c5c 6ee6 ada4 e981 93e5 85b7  .....\n.........
+00002a40: e58f afe4 bba5 e59c a8e4 bbbb e684 8fe7  ................
+00002a50: bea4 e4bd bfe7 94a8 efbc 8c5c 6ee6 af8f  ...........\n...
+00002a60: e4b8 aae3 8090 e8a2 abe5 86bb e7bb 93e7  ................
+00002a70: 9a84 e8b5 84e4 baa7 e380 91e4 bdbf e794  ................
+00002a80: a8e5 908e e4bc 9ae5 9ca8 e4bd bfe7 94a8  ................
+00002a90: e79a 84e7 bea4 e88e b7e5 be97 e4b8 80e5  ................
+00002aa0: 808d e8b5 8ce6 b3a8 e4b8 8ae9 9990 e79a  ................
+00002ab0: 84e9 8791 e5b8 81e3 8082 220d 0a20 2020  .........."..   
+00002ac0: 207d 2c0d 0a20 2020 207b 0d0a 2020 2020   },..    {..    
+00002ad0: 2020 2020 2266 756e 6322 3a22 e6b8 85e7      "func":"....
+00002ae0: 9086 e697 a0e6 9588 e8b4 a6e6 88b7 222c  ..............",
+00002af0: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
+00002b00: 6572 5f6d 6574 686f 6422 3a22 e6b8 85e7  er_method":"....
+00002b10: 9086 e697 a0e6 9588 e8b4 a6e6 88b7 222c  ..............",
+00002b20: 0d0a 2020 2020 2020 2020 2274 7269 6767  ..        "trigg
+00002b30: 6572 5f63 6f6e 6469 7469 6f6e 223a 22e6  er_condition":".
+00002b40: 8c87 e4bb a4e6 9d83 e999 90ef bc9a e8b6  ................
+00002b50: 85e7 aea1 222c 0d0a 2020 2020 2020 2020  ....",..        
+00002b60: 2262 7269 6566 5f64 6573 223a 22e6 b885  "brief_des":"...
+00002b70: e790 86e6 97a0 e695 88e8 b4a6 e688 b722  ..............."
+00002b80: 2c0d 0a20 2020 2020 2020 2022 6465 7461  ,..        "deta
+00002b90: 696c 5f64 6573 223a 22e6 97a0 e695 88e8  il_des":".......
+00002ba0: b4a6 e688 b7e8 8c83 e59b b4ef bc9a 5c6e  ..............\n
+00002bb0: 626f 74e4 b88d e59c a8e7 9a84 e7be a45c  bot............\
+00002bc0: 6ee9 8080 e7be a4e7 9a84 e794 a8e6 88b7  n...............
+00002bd0: 5c6e e995 bfe6 9c9f e4b8 8de5 8692 e6b3  \n..............
+00002be0: a1e7 9a84 e7be a4e5 8f8b 5c6e e8b5 84e4  ..........\n....
+00002bf0: baa7 e8bf 87e5 b08f e79a 84e5 85ac e58f  ................
+00002c00: b822 0d0a 2020 2020 7d0d 0a5d            ."..    }..]
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/props_library.json` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/resource/props_library.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8931818181818181%*

 * *Differences: {"'03100'": "{'color': '#CC0000'}",*

 * * "'33001'": "OrderedDict([('name', '设置许可证'), ('color', '#FF99CC'), ('rare', 3), ('intro', "*

 * *            "'可以设置一些东西'), ('des', '不要上传涩图！')])",*

 * * "'52001'": "{'name': '10%结算补贴', 'intro': "*

 * *            "'庄家提供的保险单，在对局中失败时庄家为您承担10%的损失。\\n\\n在详细审核这个业务之后，股东大会一致认为这是一门稳赔不赚的买卖。'}",*

 * * "'52002'": "{'name': '10%额外奖励', 'intro': "*

 * *            "'庄家提供的保险单，在对局中胜利时庄家为您提供10%的额外奖励。\\n\\n我觉得我们有必要提醒你咱们的业务并不是搞慈善。'}",*

 * * "'52101'": "{'intro': '与随机一个人平分金币。'}",*

 * * "'52102'": "{'intro': '50%的概率使你的金币数翻倍，另外5 […]*

```diff
@@ -3,15 +3,15 @@
         "color": "#696969",
         "des": "\u6bcf\u6b21\u91cd\u7f6e\u90fd\u4f1a\u7559\u4e0b\u8fd9\u6837\u4e00\u4e2a\u6807\u8bb0\u3002",
         "intro": "\u5f53\u4e00\u4e2a\u4eba\u7684\u91d1\u5e01\u6570\u91cf\u8d85\u8fc7\u5176\u4ed6\u4eba\u7684\u603b\u548c\uff0c\u90a3\u4e48\u8fd9\u91cc\u5c31\u4e0d\u7a33\u5b9a\u4e86\u3002\u6bcf\u4e2a\u4eba\u968f\u65f6\u90fd\u53ef\u4ee5\u53d1\u8d77\u91cd\u7f6e\u6765\u6253\u7834\u73b0\u72b6\u3002",
         "name": "\u8def\u706f\u6302\u4ef6\u6807\u8bb0",
         "rare": 0
     },
     "03100": {
-        "color": "#FF0000",
+        "color": "#CC0000",
         "des": "\u68a6\u91cc\u4ec0\u4e48\u90fd\u6709\u3002",
         "intro": "\u5185\u542b10\u4ebf\u91d1\u5e01\uff0c100\u4e07\u94bb\u77f3",
         "name": "\u6d4b\u8bd5\u91d1\u5e93",
         "rare": 0
     },
     "03101": {
         "color": "#FFCC00",
@@ -51,14 +51,21 @@
     "32002": {
         "color": "#330000",
         "des": "\u968f\u673a\u6e38\u620f\uff0c\u968f\u673a\u8d4c\u6ce8\u3002\u65e0\u89c6\u8d4c\u6ce8\u4e0a\u9650\u3002",
         "intro": "\u53ef\u4ee5\u53d1\u8d77\u968f\u673a\u5bf9\u6218",
         "name": "\u6311\u6218\u5fbd\u7ae0",
         "rare": 3
     },
+    "33001": {
+        "color": "#FF99CC",
+        "des": "\u4e0d\u8981\u4e0a\u4f20\u6da9\u56fe\uff01",
+        "intro": "\u53ef\u4ee5\u8bbe\u7f6e\u4e00\u4e9b\u4e1c\u897f",
+        "name": "\u8bbe\u7f6e\u8bb8\u53ef\u8bc1",
+        "rare": 3
+    },
     "33101": {
         "color": "#CCCCFF",
         "des": "\u6c34\uff0c\u706b\uff0c\u571f\uff0c\u98ce",
         "intro": "\u6253\u5f00\u53ef\u4ee5\u83b7\u5f97\u968f\u673a\u56db\u4e2a\u5143\u7d20\u3002",
         "name": "\u521d\u7ea7\u5143\u7d20",
         "rare": 3
     },
@@ -96,39 +103,46 @@
         "intro": "\u522b\u95ee\u4e3a\u4ec0\u4e48\u7a00\u6709\u5ea6\u8fd9\u4e48\u9ad8\uff0c\u8d35\u5c31\u8d35\u5728\u8fd0\u8d39\u3002",
         "name": "\u8fdb\u53e3\u7a7a\u6c14",
         "rare": 5
     },
     "52001": {
         "color": "#A0522D",
         "des": "--likaris",
-        "intro": "\u5e84\u5bb6\u63d0\u4f9b\u7684\u4fdd\u9669\u5355\uff0c\u5728\u5bf9\u5c40\u4e2d\u5931\u8d25\u65f6\u5e84\u5bb6\u4e3a\u60a8\u627f\u62c520%\u7684\u635f\u5931\u3002\n\n\u5728\u8be6\u7ec6\u5ba1\u6838\u8fd9\u4e2a\u4e1a\u52a1\u4e4b\u540e\uff0c\u80a1\u4e1c\u5927\u4f1a\u4e00\u81f4\u8ba4\u4e3a\u8fd9\u662f\u4e00\u95e8\u7a33\u8d54\u4e0d\u8d5a\u7684\u4e70\u5356\u3002",
-        "name": "20%\u7ed3\u7b97\u8865\u8d34",
+        "intro": "\u5e84\u5bb6\u63d0\u4f9b\u7684\u4fdd\u9669\u5355\uff0c\u5728\u5bf9\u5c40\u4e2d\u5931\u8d25\u65f6\u5e84\u5bb6\u4e3a\u60a8\u627f\u62c510%\u7684\u635f\u5931\u3002\n\n\u5728\u8be6\u7ec6\u5ba1\u6838\u8fd9\u4e2a\u4e1a\u52a1\u4e4b\u540e\uff0c\u80a1\u4e1c\u5927\u4f1a\u4e00\u81f4\u8ba4\u4e3a\u8fd9\u662f\u4e00\u95e8\u7a33\u8d54\u4e0d\u8d5a\u7684\u4e70\u5356\u3002",
+        "name": "10%\u7ed3\u7b97\u8865\u8d34",
         "rare": 5
     },
     "52002": {
         "color": "#B22222",
         "des": "--likaris",
-        "intro": "\u5e84\u5bb6\u63d0\u4f9b\u7684\u4fdd\u9669\u5355\uff0c\u5728\u5bf9\u5c40\u4e2d\u80dc\u5229\u65f6\u5e84\u5bb6\u4e3a\u60a8\u63d0\u4f9b20%\u7684\u989d\u5916\u5956\u52b1\u3002\n\n\u6211\u89c9\u5f97\u6211\u4eec\u6709\u5fc5\u8981\u63d0\u9192\u4f60\u54b1\u4eec\u7684\u4e1a\u52a1\u5e76\u4e0d\u662f\u641e\u6148\u5584\u3002",
-        "name": "20%\u989d\u5916\u5956\u52b1",
+        "intro": "\u5e84\u5bb6\u63d0\u4f9b\u7684\u4fdd\u9669\u5355\uff0c\u5728\u5bf9\u5c40\u4e2d\u80dc\u5229\u65f6\u5e84\u5bb6\u4e3a\u60a8\u63d0\u4f9b10%\u7684\u989d\u5916\u5956\u52b1\u3002\n\n\u6211\u89c9\u5f97\u6211\u4eec\u6709\u5fc5\u8981\u63d0\u9192\u4f60\u54b1\u4eec\u7684\u4e1a\u52a1\u5e76\u4e0d\u662f\u641e\u6148\u5584\u3002",
+        "name": "10%\u989d\u5916\u5956\u52b1",
         "rare": 5
     },
     "52101": {
         "color": "#9999FF",
         "des": "\u4f7f\u7528\u795e\u79d8\u5929\u5e73\u9700\u8981\u4e00\u70b9\u70b9\u624b\u7eed\u8d39\u3002",
-        "intro": "\u4e0e\u672c\u7fa4\u524d20\u7684\u968f\u673a\u4e00\u4e2a\u4eba\u5e73\u5206\u91d1\u5e01\u3002",
+        "intro": "\u4e0e\u968f\u673a\u4e00\u4e2a\u4eba\u5e73\u5206\u91d1\u5e01\u3002",
         "name": "\u795e\u79d8\u5929\u5e73",
         "rare": 5
     },
     "52102": {
         "color": "#FF6600",
         "des": "\u5c01\u9876Lv.50\u91d1\u5e93\u3002\n\u4f7f\u7528\u53c2\u65702\u53ef\u6d88\u8017\u4e00\u9897\u94bb\u77f3\u89e3\u9664\u5c01\u9876\u3002",
-        "intro": "50%\u7684\u6982\u7387\u4f7f\u4f60\u7684\u91d1\u5e01\u6570\u7ffb\u500d\uff0c\u53e6\u591650%\u7684\u6982\u7387\u4f7f\u4f60\u7684\u91d1\u5e01\u6570\u6e05\u96f6\u3002",
+        "intro": "50%\u7684\u6982\u7387\u4f7f\u4f60\u7684\u91d1\u5e01\u6570\u7ffb\u500d\uff0c\u53e6\u591650%\u7684\u6982\u7387\u4f7f\u4f60\u7684\u91d1\u5e01\u6570\u51cf\u534a\u3002",
         "name": "\u5e78\u8fd0\u786c\u5e01",
         "rare": 5
     },
+    "53101": {
+        "color": "#FF3300",
+        "des": "\u611f\u8c22\u5404\u4f4d\u73a9\u5bb6\u7684\u652f\u6301\uff01",
+        "intro": "\u6253\u5f00\u540e\u53ef\u4ee5\u83b7\u5f97\u3010\u91d1\u5e01\u7b7e\u5230-\u91cd\u7f6e\u7b7e\u5230\u3011\u8303\u56f4\u7684\u968f\u673a\u91d1\u5e01\u3002",
+        "name": "\u968f\u673a\u7ea2\u5305",
+        "rare": 5
+    },
     "61001": {
         "color": "#66CCFF",
         "des": "",
         "intro": "",
         "name": "\u7eaf\u51c0\u7a7a\u6c14",
         "rare": 6
     },
```

### Comparing `nonebot_plugin_game_collection-2.0.5/nonebot_plugin_game_collection/start.py` & `nonebot_plugin_game_collection-2.1.0/nonebot_plugin_game_collection/HorseRace/start.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,31 +1,30 @@
-﻿from nonebot.log import logger
-from nonebot import get_driver
-import json
-import os
+﻿from pathlib import Path
+from nonebot.log import logger
+try:
+    import ujson as json
+except ModuleNotFoundError:
+    import json
+from ..data.data import resourcefile
 
-async def load_dlcs():
+
+def load_dlcs():
     events_list = []
-    logs = f""
-    files = os.listdir(os.path.dirname(__file__) + '/events/horserace')
-    for file in files:
+    files = Path(resourcefile / "horserace").iterdir()
+    for x in files:
+        log = f"加载事件文件：{x.name}......"
         try:
-            with open(f'{os.path.dirname(__file__)}/events/horserace/{file}', "r", encoding="utf-8") as f:
-                logger.info(f'加载事件文件：{file}')
+            with open(x, "r", encoding="utf-8") as f:
                 events = deal_events(json.load(f))
                 events_list.extend(events)
-            logger.info(f"加载 {file} 成功")
-            logs += f'加载 {file} 成功\n'
-        except:
-            logger.info(f"加载 {file} 失败！失败！失败！")
-            logs += f"加载 {file} 失败！失败！失败！\n"
+            logger.info(log + "成功!")
+        except Exception as e:
+            logger.info(log + "失败：" + e)
     return events_list
 
-
-
 def deal_events(events):
     events_out = []
     for i in range(0,len(events)):
         event_i = deal(events[i])
         if event_i != {}:
             events_out.append(event_i)
     return events_out
```

### Comparing `nonebot_plugin_game_collection-2.0.5/setup.py` & `nonebot_plugin_game_collection-2.1.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup,find_namespace_packages
 
 setup(
 name='nonebot_plugin_game_collection',
-version='2.0.5',
+version='2.1.0',
 description='改自nonebot_plugin_russian合并了nonebot_plugin_horserace还有一些自编玩法的小游戏合集。',
 #long_description=open('README.md','r').read(),
 author='karisaya',
 author_email='1048827424@qq.com',
 license='MIT license',
 include_package_data=True,
 packages=find_namespace_packages(include=["nonebot_plugin_game_collection","nonebot_plugin_game_collection.*"]),
```

