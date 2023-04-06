# Comparing `tmp/nonebot_api_paddle-1.0.1.tar.gz` & `tmp/nonebot_api_paddle-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nonebot_api_paddle-1.0.1.tar", last modified: Thu Apr  6 15:09:52 2023, max compression
+gzip compressed data, was "nonebot_api_paddle-1.0.2.tar", last modified: Thu Apr  6 15:26:30 2023, max compression
```

## Comparing `nonebot_api_paddle-1.0.1.tar` & `nonebot_api_paddle-1.0.2.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 15:09:52.579657 nonebot_api_paddle-1.0.1/
--rw-rw-rw-   0        0        0    12533 2023-04-02 14:35:33.000000 nonebot_api_paddle-1.0.1/LICENSE.txt
--rw-rw-rw-   0        0        0       18 2023-04-06 15:09:22.000000 nonebot_api_paddle-1.0.1/MANIFEST.in
--rw-rw-rw-   0        0        0      858 2023-04-06 15:09:52.578660 nonebot_api_paddle-1.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      356 2023-04-06 14:52:18.000000 nonebot_api_paddle-1.0.1/README.rst
-drwxrwxrwx   0        0        0        0 2023-04-06 15:09:52.573677 nonebot_api_paddle-1.0.1/nonebot_api_paddle/
--rw-rw-rw-   0        0        0     5228 2023-04-06 14:20:19.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle/__init__.py
--rw-rw-rw-   0        0        0     3143 2023-04-06 12:04:09.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_excel.py
--rw-rw-rw-   0        0        0     2410 2023-04-06 07:39:32.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_ocr.py
--rw-rw-rw-   0        0        0     2461 2023-04-04 12:52:45.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_voice.py
-drwxrwxrwx   0        0        0        0 2023-04-06 15:09:52.578660 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/
--rw-rw-rw-   0        0        0      858 2023-04-06 15:09:52.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      377 2023-04-06 15:09:52.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 15:09:52.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      141 2023-04-06 15:09:52.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/requires.txt
--rw-rw-rw-   0        0        0       19 2023-04-06 15:09:52.000000 nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 15:09:52.579657 nonebot_api_paddle-1.0.1/setup.cfg
--rw-rw-rw-   0        0        0     1246 2023-04-06 15:09:34.000000 nonebot_api_paddle-1.0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:26:30.081319 nonebot_api_paddle-1.0.2/
+-rw-rw-rw-   0        0        0    12533 2023-04-02 14:35:33.000000 nonebot_api_paddle-1.0.2/LICENSE.txt
+-rw-rw-rw-   0        0        0       18 2023-04-06 15:09:22.000000 nonebot_api_paddle-1.0.2/MANIFEST.in
+-rw-rw-rw-   0        0        0      858 2023-04-06 15:26:30.080322 nonebot_api_paddle-1.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0      356 2023-04-06 14:52:18.000000 nonebot_api_paddle-1.0.2/README.rst
+drwxrwxrwx   0        0        0        0 2023-04-06 15:26:30.072349 nonebot_api_paddle-1.0.2/nonebot_api_paddle/
+-rw-rw-rw-   0        0        0     5430 2023-04-06 15:24:09.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle/__init__.py
+-rw-rw-rw-   0        0        0     3143 2023-04-06 12:04:09.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_excel.py
+-rw-rw-rw-   0        0        0     2410 2023-04-06 07:39:32.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_ocr.py
+-rw-rw-rw-   0        0        0     2314 2023-04-06 15:21:19.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_voice.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:26:30.079325 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/
+-rw-rw-rw-   0        0        0      858 2023-04-06 15:26:30.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      377 2023-04-06 15:26:30.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:26:30.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      141 2023-04-06 15:26:30.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       19 2023-04-06 15:26:30.000000 nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:26:30.081319 nonebot_api_paddle-1.0.2/setup.cfg
+-rw-rw-rw-   0        0        0     1246 2023-04-06 15:26:16.000000 nonebot_api_paddle-1.0.2/setup.py
```

### Comparing `nonebot_api_paddle-1.0.1/LICENSE.txt` & `nonebot_api_paddle-1.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-1.0.1/PKG-INFO` & `nonebot_api_paddle-1.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nonebot_api_paddle
-Version: 1.0.1
+Version: 1.0.2
 Summary: nonbot_api_paddle
 Home-page: https://github.com/canxin121/nonebot_api_paddle
 Author: canxin
 Author-email: 1969730106@qq.com
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `nonebot_api_paddle-1.0.1/nonebot_api_paddle/__init__.py` & `nonebot_api_paddle-1.0.2/nonebot_api_paddle/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -22,16 +22,17 @@
 _tome_ = Rule()
 
 try:
     api_command_config_ = eval(nonebot.get_driver().config.apiocr_command)
 except:
     api_command_config_ = ['apiocr','ocr']
 try:
-    if nonebot.get_driver().config.paddle_at == 'True':
-        _tome_ = to_me()
+    if nonebot.get_driver().config.paddle_at:
+        if nonebot.get_driver().config.paddle_at == 'True':
+            _tome_ = to_me()
 except:
     _tome_ = Rule()
 api_command = command(*api_command_config_)
 ##############################
 
 ocr_rule = Rule(api_command)
 ocr_api = on(rule=(api_command&_tome_))
@@ -115,20 +116,26 @@
                 await bot.call_api('upload_private_file', user_id= event.user_id, name=f'{filename}.xlsx', file=filepath)
                 await excel_api.reject()
         elif segment.type == 'text':
             if getmsg[0].data['text'] == '/结束':
                 await excel_api.finish("关闭apiexcel识别模式")
             else:
                 await excel_api.send("请发送纯图片，如要结束，请发送/结束")
-                
+#######################################                
+try: 
+    at_ornot = nonebot.get_driver().config.paddle_at
+except:
+    at_ornot = 'False'
+#######################################
+
 help_command = command('paddlehelp','飞桨帮助')               
 paddle_help = on(rule=help_command)
 @paddle_help.handle()
 async def paddle_help1_(bot: Bot, event: Event, state: T_State):
     await paddle_help.finish(f"""
 飞桨api功能大全
-以下功能是否需要艾特{nonebot.get_driver().config.paddle_at}
+以下功能是否需要艾特{at_ornot}
 1.ocr识别命令:/+{api_command_config_}，发送后进入ocr状态，可连续发图片，输入 /结束 退出
 2.表格识别转xlsx功能命令:/+{excel_command_config_},发送后进入表格识别状态，可连续发图片，输入 /结束 退出
 3.语音合成功能关键词:{voice_keyword_config_}，消息中有关键词（带/）触发，可以回复他人的消息来生成他人消息的语音
 by canxin
                        """)
```

### Comparing `nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_excel.py` & `nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_excel.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_ocr.py` & `nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_ocr.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-1.0.1/nonebot_api_paddle/api_voice.py` & `nonebot_api_paddle-1.0.2/nonebot_api_paddle/api_voice.py`

 * *Files 10% similar despite different names*

```diff
@@ -19,12 +19,8 @@
         "session_hash": "playgnwv9r"
     }
 
     response = requests.post(url, headers=headers, data=json.dumps(data))
     json_data = json.loads(response.text)
     file_name = str(json_data['data'][0]['name'])
     url = 'https://aistudio.baidu.com/serving/app/10/file=' + file_name
-    downname = file_name.split("/")[-1]
-    response = requests.get(url)
-    with open(downname, "wb") as f:
-        f.write(response.content)
     return url
```

### Comparing `nonebot_api_paddle-1.0.1/nonebot_api_paddle.egg-info/PKG-INFO` & `nonebot_api_paddle-1.0.2/nonebot_api_paddle.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nonebot-api-paddle
-Version: 1.0.1
+Version: 1.0.2
 Summary: nonbot_api_paddle
 Home-page: https://github.com/canxin121/nonebot_api_paddle
 Author: canxin
 Author-email: 1969730106@qq.com
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `nonebot_api_paddle-1.0.1/setup.py` & `nonebot_api_paddle-1.0.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.rst", "r", encoding="utf-8") as f:
     long_description = f.read()
 
 setuptools.setup(
     name="nonebot_api_paddle",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
-    version="1.0.1",  # 程序版本
+    version="1.0.2",  # 程序版本
     author="canxin",  # 项目作者
     author_email="1969730106@qq.com",  # 作者邮件
     description="nonbot_api_paddle",  # 项目的一句话描述
     long_description=long_description,  # 加长版描述
     long_description_content_type="text/markdown",  # 描述使用Markdown
     url="https://github.com/canxin121/nonebot_api_paddle",  # 项目地址
     packages=setuptools.find_packages(),  # 无需修改
```

