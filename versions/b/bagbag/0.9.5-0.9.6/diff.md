# Comparing `tmp/bagbag-0.9.5.tar.gz` & `tmp/bagbag-0.9.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bagbag-0.9.5.tar", max compression
+gzip compressed data, was "bagbag-0.9.6.tar", max compression
```

## Comparing `bagbag-0.9.5.tar` & `bagbag-0.9.6.tar`

### file list

```diff
@@ -1,20 +1,20 @@
--rw-r--r--   0        0        0     1084 2022-07-07 19:24:15.851188 bagbag-0.9.5/LICENSE
--rw-r--r--   0        0        0     3233 2022-07-23 19:37:42.781366 bagbag-0.9.5/README.md
--rw-r--r--   0        0        0      631 2022-07-23 20:24:44.911513 bagbag-0.9.5/pyproject.toml
--rw-r--r--   0        0        0      275 2022-07-22 08:24:55.246689 bagbag-0.9.5/src/bagbag/Base64.py
--rw-r--r--   0        0        0      313 2022-07-23 19:37:34.648864 bagbag-0.9.5/src/bagbag/Json.py
--rw-r--r--   0        0        0     5318 2022-07-22 11:24:52.432582 bagbag-0.9.5/src/bagbag/Lg.py
--rw-r--r--   0        0        0       13 2022-07-07 20:07:39.198090 bagbag-0.9.5/src/bagbag/Python.py
--rw-r--r--   0        0        0       31 2022-07-09 10:48:09.858157 bagbag-0.9.5/src/bagbag/Re.py
--rw-r--r--   0        0        0      737 2022-07-12 16:12:55.514784 bagbag-0.9.5/src/bagbag/String.py
--rw-r--r--   0        0        0     1157 2022-07-09 10:40:20.519063 bagbag-0.9.5/src/bagbag/Time.py
--rw-r--r--   0        0        0      877 2022-07-22 06:37:05.440070 bagbag-0.9.5/src/bagbag/Tools/Lock.py
--rw-r--r--   0        0        0     9464 2022-07-09 10:40:20.473233 bagbag-0.9.5/src/bagbag/Tools/MySQL_SQLite.py
--rw-r--r--   0        0        0      878 2022-07-09 10:40:20.473299 bagbag-0.9.5/src/bagbag/Tools/ProgressBar.py
--rw-r--r--   0        0        0     3423 2022-07-09 10:47:39.671884 bagbag-0.9.5/src/bagbag/Tools/Redis.py
--rw-r--r--   0        0        0     7919 2022-07-23 19:43:35.852598 bagbag-0.9.5/src/bagbag/Tools/Selenium.py
--rw-r--r--   0        0        0     9126 2022-07-22 06:05:43.412803 bagbag-0.9.5/src/bagbag/Tools/Telegram.py
--rw-r--r--   0        0        0      246 2022-07-22 06:37:24.712446 bagbag-0.9.5/src/bagbag/Tools/__init__.py
--rw-r--r--   0        0        0      148 2022-07-22 08:30:02.659578 bagbag-0.9.5/src/bagbag/__init__.py
--rw-r--r--   0        0        0     4219 1970-01-01 00:00:00.000000 bagbag-0.9.5/setup.py
--rw-r--r--   0        0        0     4107 1970-01-01 00:00:00.000000 bagbag-0.9.5/PKG-INFO
+-rw-r--r--   0        0        0     1084 2022-07-07 19:24:15.851188 bagbag-0.9.6/LICENSE
+-rw-r--r--   0        0        0     3570 2022-07-23 20:29:13.858751 bagbag-0.9.6/README.md
+-rw-r--r--   0        0        0      631 2022-07-23 20:29:36.844857 bagbag-0.9.6/pyproject.toml
+-rw-r--r--   0        0        0      275 2022-07-22 08:24:55.246689 bagbag-0.9.6/src/bagbag/Base64.py
+-rw-r--r--   0        0        0      313 2022-07-23 19:37:34.648864 bagbag-0.9.6/src/bagbag/Json.py
+-rw-r--r--   0        0        0     5318 2022-07-22 11:24:52.432582 bagbag-0.9.6/src/bagbag/Lg.py
+-rw-r--r--   0        0        0       13 2022-07-07 20:07:39.198090 bagbag-0.9.6/src/bagbag/Python.py
+-rw-r--r--   0        0        0       31 2022-07-09 10:48:09.858157 bagbag-0.9.6/src/bagbag/Re.py
+-rw-r--r--   0        0        0      737 2022-07-12 16:12:55.514784 bagbag-0.9.6/src/bagbag/String.py
+-rw-r--r--   0        0        0     1157 2022-07-09 10:40:20.519063 bagbag-0.9.6/src/bagbag/Time.py
+-rw-r--r--   0        0        0      877 2022-07-22 06:37:05.440070 bagbag-0.9.6/src/bagbag/Tools/Lock.py
+-rw-r--r--   0        0        0     9464 2022-07-09 10:40:20.473233 bagbag-0.9.6/src/bagbag/Tools/MySQL_SQLite.py
+-rw-r--r--   0        0        0      878 2022-07-09 10:40:20.473299 bagbag-0.9.6/src/bagbag/Tools/ProgressBar.py
+-rw-r--r--   0        0        0     3423 2022-07-09 10:47:39.671884 bagbag-0.9.6/src/bagbag/Tools/Redis.py
+-rw-r--r--   0        0        0     7993 2022-07-23 20:26:11.637012 bagbag-0.9.6/src/bagbag/Tools/Selenium.py
+-rw-r--r--   0        0        0     9118 2022-07-23 20:29:23.807324 bagbag-0.9.6/src/bagbag/Tools/Telegram.py
+-rw-r--r--   0        0        0      246 2022-07-22 06:37:24.712446 bagbag-0.9.6/src/bagbag/Tools/__init__.py
+-rw-r--r--   0        0        0      148 2022-07-22 08:30:02.659578 bagbag-0.9.6/src/bagbag/__init__.py
+-rw-r--r--   0        0        0     4574 1970-01-01 00:00:00.000000 bagbag-0.9.6/setup.py
+-rw-r--r--   0        0        0     4444 1970-01-01 00:00:00.000000 bagbag-0.9.6/PKG-INFO
```

### Comparing `bagbag-0.9.5/LICENSE` & `bagbag-0.9.6/LICENSE`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/README.md` & `bagbag-0.9.6/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -30,52 +30,70 @@
   * Encode(s:str) -> str
   * Decode(s:str) -> str
 * Json
   * Dumps(obj, indent=4, ensure_ascii=False) -> str
   * Loads(s:str) -> list | dict
 * Tools 一些工具
   * Selenium(SeleniumServer:str=None)
+    * ResizeWindow(width:int, height:int)
+    * ScrollRight(pixel:int)
+    * ScrollLeft(pixel:int)
+    * ScrollUp(pixel:int)
+    * ScrollDown(pixel:int)
+    * Url() -> str
+    * Cookie() -> List[dict]
+    * SetCookie(cookie_dict:dict)
+    * Refresh()
+    * GetSession() -> str
     * Get(url:str)
     * PageSource() -> str
     * Title() -> str
     * Close()
+    * Find(xpath:str, waiting=True) -> SeleniumElement
+      * Clear()
+      * Click()
+      * Text() -> str
+      * Attribute(name:str) -> str
+      * Input(string:str)
+      * Submit()
+      * PressEnter()
   * Telegram(appid:str, apphash:str, sessionString:str=None)
     * SessionString() -> str
     * ResolvePeerByUsername(username:str) -> TelegramPeer
       * History(limit:int=100, offset:int=0) -> list
-      * Resolve() -> None # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息
+      * Resolve() # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息
   * ProgressBar(iterable_obj, startfrom=0, total=None, title=None, leave=False)
   * Redis(host: str, port: int = 6379, database: int = 0, password: str = "")
     * Set(key:str, value:str, ttl:int=None) -> (bool | None)
     * Get(key:str) -> (str | None)
     * Del(key:str) -> int
     * Lock(key:str) -> RedisLock
       * Acquire()
       * Release()
   * MySQL(host: str, port: int, user: str, password: str, database: str, prefix:str = "")
   * SQLite(path: str, prefix:str = "")
-    * Execute(self, sql: str) -> (bool | int | list)
-    * Table(self, tbname: str) -> MySQLSQLiteTable
-      * AddColumn(self, colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable
-      * AddIndex(self, *cols: str) -> MySQLSQLiteTable
-      * Fields(self, *cols: str) -> MySQLSQLiteTable
-      * Where(self, key:str, opera:str, value:str) -> MySQLSQLiteTable
-      * WhereIn(self, key:str, value: list) -> MySQLSQLiteTable
-      * WhereNotIn(self, key:str, value: list) -> MySQLSQLiteTable
-      * WhereNull(self, key:str) -> MySQLSQLiteTable
-      * WhereNotNull_WillNotImplement(self, key:str)
-      * OrWhere(self, key:str, opera:str, value:str) -> MySQLSQLiteTable
-      * OrWhereIn_WillNotImplement(self, key:str, value: list)
-      * OrderBy(self, *key:str) -> MySQLSQLiteTable
-      * Limit(self, num:int) -> MySQLSQLiteTable
-      * Paginate(self, size:int, page:int) -> MySQLSQLiteTable
-      * Data(self, value:map) -> MySQLSQLiteTable
-      * Offset(self, num:int) -> MySQLSQLiteTable
-      * Insert(self)
-      * Update(self)
-      * Delete(self)
-      * InsertGetID(self) -> int
-      * Exists(self) -> bool
-      * Count(self) -> int
-      * Find(self, id:int) -> map
-      * First(self) -> map
-      * Get(self) -> list
+    * Execute(sql: str) -> (bool | int | list)
+    * Table(tbname: str) -> MySQLSQLiteTable
+      * AddColumn(colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable
+      * AddIndex(*cols: str) -> MySQLSQLiteTable
+      * Fields(*cols: str) -> MySQLSQLiteTable
+      * Where(key:str, opera:str, value:str) -> MySQLSQLiteTable
+      * WhereIn(key:str, value: list) -> MySQLSQLiteTable
+      * WhereNotIn(key:str, value: list) -> MySQLSQLiteTable
+      * WhereNull(key:str) -> MySQLSQLiteTable
+      * WhereNotNull_WillNotImplement(key:str)
+      * OrWhere(key:str, opera:str, value:str) -> MySQLSQLiteTable
+      * OrWhereIn_WillNotImplement(key:str, value: list)
+      * OrderBy(*key:str) -> MySQLSQLiteTable
+      * Limit(num:int) -> MySQLSQLiteTable
+      * Paginate(size:int, page:int) -> MySQLSQLiteTable
+      * Data(value:map) -> MySQLSQLiteTable
+      * Offset(num:int) -> MySQLSQLiteTable
+      * Insert()
+      * Update()
+      * Delete()
+      * InsertGetID() -> int
+      * Exists() -> bool
+      * Count() -> int
+      * Find(id:int) -> map
+      * First() -> map
+      * Get() -> list
```

### Comparing `bagbag-0.9.5/src/bagbag/Lg.py` & `bagbag-0.9.6/src/bagbag/Lg.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/String.py` & `bagbag-0.9.6/src/bagbag/String.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Time.py` & `bagbag-0.9.6/src/bagbag/Time.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Tools/Lock.py` & `bagbag-0.9.6/src/bagbag/Tools/Lock.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Tools/MySQL_SQLite.py` & `bagbag-0.9.6/src/bagbag/Tools/MySQL_SQLite.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Tools/ProgressBar.py` & `bagbag-0.9.6/src/bagbag/Tools/ProgressBar.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Tools/Redis.py` & `bagbag-0.9.6/src/bagbag/Tools/Redis.py`

 * *Files identical despite different names*

### Comparing `bagbag-0.9.5/src/bagbag/Tools/Selenium.py` & `bagbag-0.9.6/src/bagbag/Tools/Selenium.py`

 * *Files 4% similar despite different names*

```diff
@@ -230,15 +230,13 @@
         self.driver.close()
         self.driver.quit()
 
 if __name__ == "__main__":
     # se = Selenium()
     se = Selenium("http://127.0.0.1:4444")
     se.Get("https://find-and-update.company-information.service.gov.uk/")
-    try:
-        se.Find("abc")
-        # print(se.PageSource())
-        import time 
-        time.sleep(86400)
-    except:
-        se.Close()
+    inputBar = se.Find("/html/body/div[1]/main/div[3]/div/form/div/div/input")
+    inputBar.Input("ade")
+    button = se.Find("/html/body/div[1]/main/div[3]/div/form/div/div/button")
+    button.Click()
+    se.Close()
```

### Comparing `bagbag-0.9.5/src/bagbag/Tools/Telegram.py` & `bagbag-0.9.6/src/bagbag/Tools/Telegram.py`

 * *Files 1% similar despite different names*

```diff
@@ -136,15 +136,15 @@
             if message.message:
                 msg.Message = message.message
             if message.from_id:
                 msg.User = TelegramPeer(ID=message.from_id.user_id, client=self.client)
             res.append(msg)
         return res
 
-    def Resolve(self) -> None:
+    def Resolve(self):
         """
         Resolve Peer, get information by peer id. 
         """
         if self.ID:
             obj = self.client.get_entity(self.ID)
             # import ipdb
             # ipdb.set_trace()
```

### Comparing `bagbag-0.9.5/setup.py` & `bagbag-0.9.6/setup.py`

 * *Files 14% similar despite different names*

```diff
@@ -19,17 +19,17 @@
  'redis>=4.3.4,<5.0.0',
  'selenium>=4.3.0,<5.0.0',
  'telethon>=1.24.0,<2.0.0',
  'tqdm>=4.64.0,<5.0.0']
 
 setup_kwargs = {
     'name': 'bagbag',
-    'version': '0.9.5',
+    'version': '0.9.6',
     'description': 'An all in one python library',
-    'long_description': '# bagbag\n\nAn all in one python library\n\n# Install \n\n```bash\npip3 install bagbag --upgrade\n```\n\n# Library\n\n* Lg 日志模块\n  * Lg.SetLevel(level:日志级别:str)\n  * Lg.SetFile(path:日志路径:str, size:文件大小，MB:int, during:日志保留时间，天:int, color:是否带ANSI颜色:bool=True, json:是否格式化为json:bool=False):\n  * Lg.Debug(message:日志内容)\n  * Lg.Trace(message:日志内容)\n  * Lg.Info(message:日志内容)\n  * Lg.Warn(message:日志内容)\n  * Lg.Error(message:日志内容)\n* String(string:str) 一些字符串处理函数\n  * HasChinese() -> bool 是否包含中文\n  * Language() -> str 语言\n* Time 时间\n  * Strftime(format:str, timestamp:float|int) -> str\n  * Strptime(format:str, timestring:str) -> int\n* Re 正则\n  * FindAll(pattern: str | Pattern[str], string: str, flags: _FlagsType = ...) -> list\n* Base64\n  * Encode(s:str) -> str\n  * Decode(s:str) -> str\n* Json\n  * Dumps(obj, indent=4, ensure_ascii=False) -> str\n  * Loads(s:str) -> list | dict\n* Tools 一些工具\n  * Selenium(SeleniumServer:str=None)\n    * Get(url:str)\n    * PageSource() -> str\n    * Title() -> str\n    * Close()\n  * Telegram(appid:str, apphash:str, sessionString:str=None)\n    * SessionString() -> str\n    * ResolvePeerByUsername(username:str) -> TelegramPeer\n      * History(limit:int=100, offset:int=0) -> list\n      * Resolve() -> None # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息\n  * ProgressBar(iterable_obj, startfrom=0, total=None, title=None, leave=False)\n  * Redis(host: str, port: int = 6379, database: int = 0, password: str = "")\n    * Set(key:str, value:str, ttl:int=None) -> (bool | None)\n    * Get(key:str) -> (str | None)\n    * Del(key:str) -> int\n    * Lock(key:str) -> RedisLock\n      * Acquire()\n      * Release()\n  * MySQL(host: str, port: int, user: str, password: str, database: str, prefix:str = "")\n  * SQLite(path: str, prefix:str = "")\n    * Execute(self, sql: str) -> (bool | int | list)\n    * Table(self, tbname: str) -> MySQLSQLiteTable\n      * AddColumn(self, colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable\n      * AddIndex(self, *cols: str) -> MySQLSQLiteTable\n      * Fields(self, *cols: str) -> MySQLSQLiteTable\n      * Where(self, key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * WhereIn(self, key:str, value: list) -> MySQLSQLiteTable\n      * WhereNotIn(self, key:str, value: list) -> MySQLSQLiteTable\n      * WhereNull(self, key:str) -> MySQLSQLiteTable\n      * WhereNotNull_WillNotImplement(self, key:str)\n      * OrWhere(self, key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * OrWhereIn_WillNotImplement(self, key:str, value: list)\n      * OrderBy(self, *key:str) -> MySQLSQLiteTable\n      * Limit(self, num:int) -> MySQLSQLiteTable\n      * Paginate(self, size:int, page:int) -> MySQLSQLiteTable\n      * Data(self, value:map) -> MySQLSQLiteTable\n      * Offset(self, num:int) -> MySQLSQLiteTable\n      * Insert(self)\n      * Update(self)\n      * Delete(self)\n      * InsertGetID(self) -> int\n      * Exists(self) -> bool\n      * Count(self) -> int\n      * Find(self, id:int) -> map\n      * First(self) -> map\n      * Get(self) -> list\n',
+    'long_description': '# bagbag\n\nAn all in one python library\n\n# Install \n\n```bash\npip3 install bagbag --upgrade\n```\n\n# Library\n\n* Lg 日志模块\n  * Lg.SetLevel(level:日志级别:str)\n  * Lg.SetFile(path:日志路径:str, size:文件大小，MB:int, during:日志保留时间，天:int, color:是否带ANSI颜色:bool=True, json:是否格式化为json:bool=False):\n  * Lg.Debug(message:日志内容)\n  * Lg.Trace(message:日志内容)\n  * Lg.Info(message:日志内容)\n  * Lg.Warn(message:日志内容)\n  * Lg.Error(message:日志内容)\n* String(string:str) 一些字符串处理函数\n  * HasChinese() -> bool 是否包含中文\n  * Language() -> str 语言\n* Time 时间\n  * Strftime(format:str, timestamp:float|int) -> str\n  * Strptime(format:str, timestring:str) -> int\n* Re 正则\n  * FindAll(pattern: str | Pattern[str], string: str, flags: _FlagsType = ...) -> list\n* Base64\n  * Encode(s:str) -> str\n  * Decode(s:str) -> str\n* Json\n  * Dumps(obj, indent=4, ensure_ascii=False) -> str\n  * Loads(s:str) -> list | dict\n* Tools 一些工具\n  * Selenium(SeleniumServer:str=None)\n    * ResizeWindow(width:int, height:int)\n    * ScrollRight(pixel:int)\n    * ScrollLeft(pixel:int)\n    * ScrollUp(pixel:int)\n    * ScrollDown(pixel:int)\n    * Url() -> str\n    * Cookie() -> List[dict]\n    * SetCookie(cookie_dict:dict)\n    * Refresh()\n    * GetSession() -> str\n    * Get(url:str)\n    * PageSource() -> str\n    * Title() -> str\n    * Close()\n    * Find(xpath:str, waiting=True) -> SeleniumElement\n      * Clear()\n      * Click()\n      * Text() -> str\n      * Attribute(name:str) -> str\n      * Input(string:str)\n      * Submit()\n      * PressEnter()\n  * Telegram(appid:str, apphash:str, sessionString:str=None)\n    * SessionString() -> str\n    * ResolvePeerByUsername(username:str) -> TelegramPeer\n      * History(limit:int=100, offset:int=0) -> list\n      * Resolve() # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息\n  * ProgressBar(iterable_obj, startfrom=0, total=None, title=None, leave=False)\n  * Redis(host: str, port: int = 6379, database: int = 0, password: str = "")\n    * Set(key:str, value:str, ttl:int=None) -> (bool | None)\n    * Get(key:str) -> (str | None)\n    * Del(key:str) -> int\n    * Lock(key:str) -> RedisLock\n      * Acquire()\n      * Release()\n  * MySQL(host: str, port: int, user: str, password: str, database: str, prefix:str = "")\n  * SQLite(path: str, prefix:str = "")\n    * Execute(sql: str) -> (bool | int | list)\n    * Table(tbname: str) -> MySQLSQLiteTable\n      * AddColumn(colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable\n      * AddIndex(*cols: str) -> MySQLSQLiteTable\n      * Fields(*cols: str) -> MySQLSQLiteTable\n      * Where(key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * WhereIn(key:str, value: list) -> MySQLSQLiteTable\n      * WhereNotIn(key:str, value: list) -> MySQLSQLiteTable\n      * WhereNull(key:str) -> MySQLSQLiteTable\n      * WhereNotNull_WillNotImplement(key:str)\n      * OrWhere(key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * OrWhereIn_WillNotImplement(key:str, value: list)\n      * OrderBy(*key:str) -> MySQLSQLiteTable\n      * Limit(num:int) -> MySQLSQLiteTable\n      * Paginate(size:int, page:int) -> MySQLSQLiteTable\n      * Data(value:map) -> MySQLSQLiteTable\n      * Offset(num:int) -> MySQLSQLiteTable\n      * Insert()\n      * Update()\n      * Delete()\n      * InsertGetID() -> int\n      * Exists() -> bool\n      * Count() -> int\n      * Find(id:int) -> map\n      * First() -> map\n      * Get() -> list\n',
     'author': 'Darren',
     'author_email': 'None',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/darren2046/bagbag',
     'package_dir': package_dir,
     'packages': packages,
```

### Comparing `bagbag-0.9.5/PKG-INFO` & `bagbag-0.9.6/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bagbag
-Version: 0.9.5
+Version: 0.9.6
 Summary: An all in one python library
 Home-page: https://github.com/darren2046/bagbag
 License: MIT
 Keywords: base,library
 Author: Darren
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
@@ -55,53 +55,71 @@
   * Encode(s:str) -> str
   * Decode(s:str) -> str
 * Json
   * Dumps(obj, indent=4, ensure_ascii=False) -> str
   * Loads(s:str) -> list | dict
 * Tools 一些工具
   * Selenium(SeleniumServer:str=None)
+    * ResizeWindow(width:int, height:int)
+    * ScrollRight(pixel:int)
+    * ScrollLeft(pixel:int)
+    * ScrollUp(pixel:int)
+    * ScrollDown(pixel:int)
+    * Url() -> str
+    * Cookie() -> List[dict]
+    * SetCookie(cookie_dict:dict)
+    * Refresh()
+    * GetSession() -> str
     * Get(url:str)
     * PageSource() -> str
     * Title() -> str
     * Close()
+    * Find(xpath:str, waiting=True) -> SeleniumElement
+      * Clear()
+      * Click()
+      * Text() -> str
+      * Attribute(name:str) -> str
+      * Input(string:str)
+      * Submit()
+      * PressEnter()
   * Telegram(appid:str, apphash:str, sessionString:str=None)
     * SessionString() -> str
     * ResolvePeerByUsername(username:str) -> TelegramPeer
       * History(limit:int=100, offset:int=0) -> list
-      * Resolve() -> None # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息
+      * Resolve() # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息
   * ProgressBar(iterable_obj, startfrom=0, total=None, title=None, leave=False)
   * Redis(host: str, port: int = 6379, database: int = 0, password: str = "")
     * Set(key:str, value:str, ttl:int=None) -> (bool | None)
     * Get(key:str) -> (str | None)
     * Del(key:str) -> int
     * Lock(key:str) -> RedisLock
       * Acquire()
       * Release()
   * MySQL(host: str, port: int, user: str, password: str, database: str, prefix:str = "")
   * SQLite(path: str, prefix:str = "")
-    * Execute(self, sql: str) -> (bool | int | list)
-    * Table(self, tbname: str) -> MySQLSQLiteTable
-      * AddColumn(self, colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable
-      * AddIndex(self, *cols: str) -> MySQLSQLiteTable
-      * Fields(self, *cols: str) -> MySQLSQLiteTable
-      * Where(self, key:str, opera:str, value:str) -> MySQLSQLiteTable
-      * WhereIn(self, key:str, value: list) -> MySQLSQLiteTable
-      * WhereNotIn(self, key:str, value: list) -> MySQLSQLiteTable
-      * WhereNull(self, key:str) -> MySQLSQLiteTable
-      * WhereNotNull_WillNotImplement(self, key:str)
-      * OrWhere(self, key:str, opera:str, value:str) -> MySQLSQLiteTable
-      * OrWhereIn_WillNotImplement(self, key:str, value: list)
-      * OrderBy(self, *key:str) -> MySQLSQLiteTable
-      * Limit(self, num:int) -> MySQLSQLiteTable
-      * Paginate(self, size:int, page:int) -> MySQLSQLiteTable
-      * Data(self, value:map) -> MySQLSQLiteTable
-      * Offset(self, num:int) -> MySQLSQLiteTable
-      * Insert(self)
-      * Update(self)
-      * Delete(self)
-      * InsertGetID(self) -> int
-      * Exists(self) -> bool
-      * Count(self) -> int
-      * Find(self, id:int) -> map
-      * First(self) -> map
-      * Get(self) -> list
+    * Execute(sql: str) -> (bool | int | list)
+    * Table(tbname: str) -> MySQLSQLiteTable
+      * AddColumn(colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable
+      * AddIndex(*cols: str) -> MySQLSQLiteTable
+      * Fields(*cols: str) -> MySQLSQLiteTable
+      * Where(key:str, opera:str, value:str) -> MySQLSQLiteTable
+      * WhereIn(key:str, value: list) -> MySQLSQLiteTable
+      * WhereNotIn(key:str, value: list) -> MySQLSQLiteTable
+      * WhereNull(key:str) -> MySQLSQLiteTable
+      * WhereNotNull_WillNotImplement(key:str)
+      * OrWhere(key:str, opera:str, value:str) -> MySQLSQLiteTable
+      * OrWhereIn_WillNotImplement(key:str, value: list)
+      * OrderBy(*key:str) -> MySQLSQLiteTable
+      * Limit(num:int) -> MySQLSQLiteTable
+      * Paginate(size:int, page:int) -> MySQLSQLiteTable
+      * Data(value:map) -> MySQLSQLiteTable
+      * Offset(num:int) -> MySQLSQLiteTable
+      * Insert()
+      * Update()
+      * Delete()
+      * InsertGetID() -> int
+      * Exists() -> bool
+      * Count() -> int
+      * Find(id:int) -> map
+      * First() -> map
+      * Get() -> list
```

