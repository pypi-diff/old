# Comparing `tmp/nonebot-plugin-acm-reminder-0.1.5.tar.gz` & `tmp/nonebot-plugin-acm-reminder-0.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nonebot-plugin-acm-reminder-0.1.5.tar", last modified: Tue Mar 14 13:37:04 2023, max compression
+gzip compressed data, was "nonebot-plugin-acm-reminder-0.1.6.tar", last modified: Thu Apr  6 15:34:14 2023, max compression
```

## Comparing `nonebot-plugin-acm-reminder-0.1.5.tar` & `nonebot-plugin-acm-reminder-0.1.6.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1088 2023-01-15 11:05:12.918513 nonebot-plugin-acm-reminder-0.1.5/LICENSE
--rw-r--r--   0        0        0     2826 2023-03-14 13:35:07.193928 nonebot-plugin-acm-reminder-0.1.5/nonebot_plugin_acm_reminder/__init__.py
--rw-r--r--   0        0        0      178 2023-03-14 13:33:05.205651 nonebot-plugin-acm-reminder-0.1.5/nonebot_plugin_acm_reminder/config.py
--rw-r--r--   0        0        0     3159 2023-03-14 13:35:43.848230 nonebot-plugin-acm-reminder-0.1.5/nonebot_plugin_acm_reminder/data_source.py
--rw-r--r--   0        0        0      636 2023-03-14 13:36:57.165478 nonebot-plugin-acm-reminder-0.1.5/pyproject.toml
--rw-r--r--   0        0        0      808 2023-02-08 08:16:44.223221 nonebot-plugin-acm-reminder-0.1.5/README.md
--rw-r--r--   0        0        0     1036 1970-01-01 00:00:00.000000 nonebot-plugin-acm-reminder-0.1.5/PKG-INFO
+-rw-r--r--   0        0        0     1088 2023-01-15 11:05:12.918513 nonebot-plugin-acm-reminder-0.1.6/LICENSE
+-rw-r--r--   0        0        0     3028 2023-04-06 15:33:46.324195 nonebot-plugin-acm-reminder-0.1.6/nonebot_plugin_acm_reminder/__init__.py
+-rw-r--r--   0        0        0      228 2023-04-06 15:33:46.324195 nonebot-plugin-acm-reminder-0.1.6/nonebot_plugin_acm_reminder/config.py
+-rw-r--r--   0        0        0     3579 2023-04-06 15:33:46.324195 nonebot-plugin-acm-reminder-0.1.6/nonebot_plugin_acm_reminder/data_source.py
+-rw-r--r--   0        0        0      636 2023-04-06 15:33:46.324195 nonebot-plugin-acm-reminder-0.1.6/pyproject.toml
+-rw-r--r--   0        0        0      852 2023-04-06 15:33:46.324195 nonebot-plugin-acm-reminder-0.1.6/README.md
+-rw-r--r--   0        0        0     1079 1970-01-01 00:00:00.000000 nonebot-plugin-acm-reminder-0.1.6/PKG-INFO
```

### Comparing `nonebot-plugin-acm-reminder-0.1.5/LICENSE` & `nonebot-plugin-acm-reminder-0.1.6/LICENSE`

 * *Files identical despite different names*

### Comparing `nonebot-plugin-acm-reminder-0.1.5/nonebot_plugin_acm_reminder/__init__.py` & `nonebot-plugin-acm-reminder-0.1.6/nonebot_plugin_acm_reminder/__init__.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,74 +1,81 @@
 from datetime import datetime
 from typing import List
-from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment, Message
+from httpx import URL
+from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
 from nonebot.plugin import on_command, PluginMetadata
-from nonebot.params import CommandArg
 from nonebot import get_driver, require
 
+
+from .config import Config
+from .data_source import ContestType, req_get, html_parse_cf, html_parse_nc
+
 require("nonebot_plugin_apscheduler")
 require("nonebot_plugin_htmlrender")
-from nonebot_plugin_apscheduler import scheduler
 from nonebot_plugin_htmlrender import md_to_pic
+from nonebot_plugin_apscheduler import scheduler
 
-from .data_source import ContestType, req_get, html_parse_cf, html_parse_nc
-from .config import Config
 
 __plugin_meta__ = PluginMetadata(
     name="ACMReminder",
     description="订阅牛客/CF平台的比赛信息",
-    usage="/contest.list 获取所有/CF/牛客平台的比赛信息"
+    usage=
+    "/contest.list 获取所有/CF/牛客平台的比赛信息"
     "/contest.subscribe 订阅CF/牛客平台的比赛信息"
     "/contest.update 手动更新比赛信息")
 
 contest_list = on_command(("contest", "list"), aliases={"比赛列表"}, priority=5)
-contest_update = on_command(("contest", "update"), aliases={"更新比赛"}, priority=5)
+contest_update = on_command(("contest", "update"),
+                            aliases={"更新比赛"}, priority=5)
 contest_subscribe = on_command(
     ("contest", "subscribe"), aliases={"订阅比赛"}, priority=5)
 
 driver = get_driver()
 contest_data: List[ContestType] = []
 plugin_config: Config = Config.parse_obj(driver.config)
 
 
-
 async def update():
     """
     更新比赛信息
     """
     contest_data.clear()
     contest_data.extend(html_parse_cf(await req_get("https://codeforces.com/contests")))
     contest_data.extend(html_parse_nc(await req_get("https://ac.nowcoder.com/acm/contest/vip-index?topCategoryFilter=13")))
+    contest_data.extend(html_parse_nc(await req_get("https://ac.nowcoder.com/acm/contest/vip-index?topCategoryFilter=14")))
 
 
 @scheduler.scheduled_job('interval', minutes=plugin_config.update_time, id="update_contest")
 async def update_contest():
     await update()
 
+
 @driver.on_startup
 async def startup():
     await update()
     # 防止因为网络问题导致机器人启动失败
 
+
 @contest_update.handle()
 async def update_handle(event: MessageEvent):
     try:
         await update()
-    except:
-        await contest_update.finish("更新失败")
+    except Exception as e:
+        await contest_update.finish(MessageSegment.image(await md_to_pic(f"更新失败 {e}")))
+
     await contest_update.finish("更新成功")
 
+
 @contest_list.handle()
 async def get_list(event: MessageEvent):
     msg = '<div align="center">\n <h1> 近期竞赛 </h1> \n</div>'
     for contest in contest_data:
         time = datetime.fromtimestamp(
             contest["time"]).strftime("%Y-%m-%d %H:%M")
         writes = ",".join(filter(None, contest["writes"])) if len(
             contest["writes"]) < 5 else ",".join(filter(None, contest["writes"][:5])) + "..."
         msg += f"## {contest['name']}\n" \
             f"* 竞赛平台  **{contest['platform']}**\n" \
             f"* 举办人员 {writes}\n" \
             f"* 开始时间 **{time}**\n" \
             f"* 竞赛时长 **{contest['length']/60}h**\n"
     await contest_list.finish(MessageSegment.image(await md_to_pic(msg)))
-
```

### Comparing `nonebot-plugin-acm-reminder-0.1.5/pyproject.toml` & `nonebot-plugin-acm-reminder-0.1.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 [tool.pdm]
 
 [project]
 name = "nonebot_plugin_acm_reminder"
-version = "0.1.5"
+version = "0.1.6"
 description = "A subscribe CodeForces/NowCoder contest info plugin for nonebot2"
 authors = [
     { name = "BigOrangeQWQ", email = "2284086963@qq.com" },
 ]
 dependencies = [
     "BeautifulSoup4>=4.11.2",
     "nonebot2>=2.0.0b5",
```

### Comparing `nonebot-plugin-acm-reminder-0.1.5/README.md` & `nonebot-plugin-acm-reminder-0.1.6/README.md`

 * *Files 7% similar despite different names*

```diff
@@ -15,26 +15,27 @@
 ```
 pip install nonebot-plugin-acm-reminder
 nb plugin install nonebot-plugin-acm-reminder
 ```
 
 ## 配置项
 
-* 拉取竞赛列表的更新时间
+* 拉取竞赛列表的更新时间(分钟)
 ```
-update_time = 360
+update_time = 720
 ```
 
 ## 用法
 
 ```
 / := [命令起始符]
 . := [命令分隔符]
 
 /contest.list 拉取竞赛列表
+/contest.update 更新竞赛列表
 ```
 
 ## TODO
 
 - [x] 获取竞赛信息并形成列表
 - [x] 支持CodeForces平台
 - [x] 支持牛客平台
```

#### html2text {}

```diff
@@ -1,8 +1,9 @@
    # ACMReminder ä¸æ¬¾å¯æ¥è¯¢ä¸è®¢éçå®¢/CFç«èµçæä»¶ [Download]
 ## å®è£ ``` pip install nonebot-plugin-acm-reminder nb plugin install
 nonebot-plugin-acm-reminder ``` ## éç½®é¡¹ *
-æåç«èµåè¡¨çæ´æ°æ¶é´ ``` update_time = 360 ``` ## ç¨æ³ ``` / :=
-[å½ä»¤èµ·å§ç¬¦] . := [å½ä»¤åéç¬¦] /contest.list æåç«èµåè¡¨ ```
-## TODO - [x] è·åç«èµä¿¡æ¯å¹¶å½¢æåè¡¨ - [x] æ¯æCodeForceså¹³å° -
-[x] æ¯æçå®¢å¹³å° - [ ] è®¢éæå®ç«èµï¼å¹¶æé - [ ]
+æåç«èµåè¡¨çæ´æ°æ¶é´(åé) ``` update_time = 720 ``` ## ç¨æ³
+``` / := [å½ä»¤èµ·å§ç¬¦] . := [å½ä»¤åéç¬¦] /contest.list
+æåç«èµåè¡¨ /contest.update æ´æ°ç«èµåè¡¨ ``` ## TODO - [x]
+è·åç«èµä¿¡æ¯å¹¶å½¢æåè¡¨ - [x] æ¯æCodeForceså¹³å° - [x]
+æ¯æçå®¢å¹³å° - [ ] è®¢éæå®ç«èµï¼å¹¶æé - [ ]
 å¯éè¿æä»¤è·åç«èµé¾æ¥ - [ ] æ¯æåæ£å¹³å°
```

### Comparing `nonebot-plugin-acm-reminder-0.1.5/PKG-INFO` & `nonebot-plugin-acm-reminder-0.1.6/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nonebot_plugin_acm_reminder
-Version: 0.1.5
+Version: 0.1.6
 Summary: A subscribe CodeForces/NowCoder contest info plugin for nonebot2
 License: MIT
 Author-email: BigOrangeQWQ <2284086963@qq.com>
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 
 <div align="center">
@@ -24,26 +24,27 @@
 ```
 pip install nonebot-plugin-acm-reminder
 nb plugin install nonebot-plugin-acm-reminder
 ```
 
 ## 配置项
 
-* 拉取竞赛列表的更新时间
+* 拉取竞赛列表的更新时间(分钟)
 ```
-update_time = 360
+update_time = 720
 ```
 
 ## 用法
 
 ```
 / := [命令起始符]
 . := [命令分隔符]
 
 /contest.list 拉取竞赛列表
+/contest.update 更新竞赛列表
 ```
 
 ## TODO
 
 - [x] 获取竞赛信息并形成列表
 - [x] 支持CodeForces平台
 - [x] 支持牛客平台
```

#### html2text {}

```diff
@@ -1,12 +1,13 @@
-Metadata-Version: 2.1 Name: nonebot_plugin_acm_reminder Version: 0.1.5 Summary:
+Metadata-Version: 2.1 Name: nonebot_plugin_acm_reminder Version: 0.1.6 Summary:
 A subscribe CodeForces/NowCoder contest info plugin for nonebot2 License: MIT
 Author-email: BigOrangeQWQ <2284086963@qq.com> Requires-Python: >=3.8
 Description-Content-Type: text/markdown
    # ACMReminder ä¸æ¬¾å¯æ¥è¯¢ä¸è®¢éçå®¢/CFç«èµçæä»¶ [Download]
 ## å®è£ ``` pip install nonebot-plugin-acm-reminder nb plugin install
 nonebot-plugin-acm-reminder ``` ## éç½®é¡¹ *
-æåç«èµåè¡¨çæ´æ°æ¶é´ ``` update_time = 360 ``` ## ç¨æ³ ``` / :=
-[å½ä»¤èµ·å§ç¬¦] . := [å½ä»¤åéç¬¦] /contest.list æåç«èµåè¡¨ ```
-## TODO - [x] è·åç«èµä¿¡æ¯å¹¶å½¢æåè¡¨ - [x] æ¯æCodeForceså¹³å° -
-[x] æ¯æçå®¢å¹³å° - [ ] è®¢éæå®ç«èµï¼å¹¶æé - [ ]
+æåç«èµåè¡¨çæ´æ°æ¶é´(åé) ``` update_time = 720 ``` ## ç¨æ³
+``` / := [å½ä»¤èµ·å§ç¬¦] . := [å½ä»¤åéç¬¦] /contest.list
+æåç«èµåè¡¨ /contest.update æ´æ°ç«èµåè¡¨ ``` ## TODO - [x]
+è·åç«èµä¿¡æ¯å¹¶å½¢æåè¡¨ - [x] æ¯æCodeForceså¹³å° - [x]
+æ¯æçå®¢å¹³å° - [ ] è®¢éæå®ç«èµï¼å¹¶æé - [ ]
 å¯éè¿æä»¤è·åç«èµé¾æ¥ - [ ] æ¯æåæ£å¹³å°
```

