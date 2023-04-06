# Comparing `tmp/wigli-0.1.6.tar.gz` & `tmp/wigli-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wigli-0.1.6.tar", max compression
+gzip compressed data, was "wigli-0.1.7.tar", max compression
```

## Comparing `wigli-0.1.6.tar` & `wigli-0.1.7.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.6/LICENSE
--rw-r--r--   0        0        0      677 2023-04-06 23:00:40.462008 wigli-0.1.6/pyproject.toml
--rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.6/README.md
--rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.6/src/wigli/__init__.py
--rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.6/src/wigli/__main__.py
--rw-r--r--   0        0        0     7195 2023-04-06 22:54:08.419627 wigli-0.1.6/src/wigli/_wigli_argparser.py
--rw-r--r--   0        0        0    21743 2023-04-06 22:58:36.043527 wigli-0.1.6/src/wigli/_wigli_bots.py
--rw-r--r--   0        0        0    10054 2023-04-06 22:49:04.260547 wigli-0.1.6/src/wigli/_wigli_cli.py
--rw-r--r--   0        0        0     9493 2023-04-06 03:10:14.371028 wigli-0.1.6/src/wigli/_wigli_data.py
--rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.6/src/wigli/_wigli_plugins.py
--rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.6/src/wigli/_wigli_testutils.py
--rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.6/src/wigli/_wigli_tools.py
--rw-r--r--   0        0        0       48 2023-04-06 23:00:40.462995 wigli-0.1.6/src/wigli/_wigli_version.py
--rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.7/LICENSE
+-rw-r--r--   0        0        0      677 2023-04-06 23:06:25.576593 wigli-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.7/README.md
+-rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.7/src/wigli/__init__.py
+-rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.7/src/wigli/__main__.py
+-rw-r--r--   0        0        0     7195 2023-04-06 22:54:08.419627 wigli-0.1.7/src/wigli/_wigli_argparser.py
+-rw-r--r--   0        0        0    21698 2023-04-06 23:06:16.262367 wigli-0.1.7/src/wigli/_wigli_bots.py
+-rw-r--r--   0        0        0    10039 2023-04-06 23:05:45.868597 wigli-0.1.7/src/wigli/_wigli_cli.py
+-rw-r--r--   0        0        0     9493 2023-04-06 03:10:14.371028 wigli-0.1.7/src/wigli/_wigli_data.py
+-rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.7/src/wigli/_wigli_plugins.py
+-rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.7/src/wigli/_wigli_testutils.py
+-rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.7/src/wigli/_wigli_tools.py
+-rw-r--r--   0        0        0       48 2023-04-06 23:06:25.576593 wigli-0.1.7/src/wigli/_wigli_version.py
+-rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.7/PKG-INFO
```

### Comparing `wigli-0.1.6/LICENSE` & `wigli-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/pyproject.toml` & `wigli-0.1.7/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "wigli"
-version = "0.1.6"
+version = "0.1.7"
 description = "Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more."
 authors = ["Douglas Graham <doug.n.graham@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.7"
```

### Comparing `wigli-0.1.6/README.md` & `wigli-0.1.7/README.md`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/__init__.py` & `wigli-0.1.7/src/wigli/__init__.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/_wigli_argparser.py` & `wigli-0.1.7/src/wigli/_wigli_argparser.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/_wigli_bots.py` & `wigli-0.1.7/src/wigli/_wigli_bots.py`

 * *Files 4% similar despite different names*

```diff
@@ -212,44 +212,44 @@
         self,
         messages: str
         | dict
         | WigliMessage
         | Iterable[WigliMessage | dict]
         | WigliInjection
         | None = None,
-        wiglidata: None or "WigliData" = None,
+        data: None or "WigliData" = None,
         prompt: str | None = None,
         title: str | None = None,
         filename: str | None = None,
         birthstamp: float = time(),
         touchstamp: float | None = None,
         stream: bool = True,
         reminders: set | None = set(),
     ):
         # Default class attribute values
         self.messages = []
         self.reminders = reminders
         self.stream = stream
 
-        self.wiglidata = wiglidata
-        if self.wiglidata is not None:
-            self.log = self.wiglidata.log
+        self.data = data
+        if self.data is not None:
+            self.log = self.data.log
 
         self.title = title
         self.filename = filename
         self.birthstamp = birthstamp
         self.touchstamp = (
             self.birthstamp
             if touchstamp is None
             else touchstamp
         )
 
         if openai.api_key == "":
             load_dotenv()
-            load_dotenv(dotenv_path=join(self.wiglidata.data_dir, ".env"))
+            load_dotenv(dotenv_path=join(self.data.data_dir, ".env"))
             openai.api_key = getenv("OPENAI_API_KEY")
 
         if messages is not None:
             self.Inject(messages)
         if prompt is not None:
             self.Inject(prompt)
 
@@ -323,26 +323,26 @@
         ):
             return self
         if not isinstance(messages, WigliInjection):
             messages = WigliInjection(messages, role=role)
         self.messages += messages.injection_messages
         if messages.reminder_messages is not None:
             self.reminders |= {messages}
-        if self.wiglidata is not None:
-            self.wiglidata.archive_chat(self)
+        if self.data is not None:
+            self.data.archive_chat(self)
         return self
 
     def make_filename(self):
         filename = slugify(
             self.title, ok="_", only_ascii=True, lower=False
         )
         self.filename = str(self.touchstamp) + "_" + filename
 
     def set_logger(self, logger: "WigliData"):
-        self.wiglidata = logger
+        self.data = logger
         self.log = logger.log
 
     def do_reminders_tick(self):
         for reminder in self.reminders:
             self.Inject(reminder.do_reminder_tick())
 
     def Chat(
```

### Comparing `wigli-0.1.6/src/wigli/_wigli_cli.py` & `wigli-0.1.7/src/wigli/_wigli_cli.py`

 * *Files 1% similar despite different names*

```diff
@@ -82,15 +82,15 @@
 
         if self.args.system is not None:
             injection = [
                 WigliMessage(self.args.system, "system")
             ] + injection
 
         if self.bot is None:
-            self.bot = WigliBot(wiglidata=self.data)
+            self.bot = WigliBot(data=self.data)
 
         if self.args.professor:
             self.log("Summoning Professor Wigli", v=0)
             self.bot = HistoryProfessor.FromBot(self.bot)
 
         if self.args.python:
             self.log("Injecting Python capabilities", v=0)
@@ -145,15 +145,15 @@
         if not self.args.clean:
             self.bot = self._load_chat()
             if isinstance(self.bot, WigliBot):
                 self.log(
                     f"""
 Loaded previous chat: {getattr(self.bot, "title", "No title")}""",
                 )
-                self.bot.wiglidata = self.data
+                self.bot.data = self.data
                 self.bot.log = self.data.log
                 if self.args.erase is not None:
                     self.bot.erase_messages(self.args.erase)
             else:
                 self.bot = None
 
         # Now everything is initialized
@@ -209,15 +209,15 @@
 
         prompt = self._bot_from_args()
 
         if self.bot is None:
             self.log(
                 "No previous chat to load, starting a new one"
             )
-            self.bot = WigliBot(wiglidata=self.data)
+            self.bot = WigliBot(data=self.data)
 
         # Parse the last message for commands and don't prompt
         if self.args.usercommands and isinstance(
             self.bot, CommandBot
         ):
             self.log(
                 "Parsing last message for commands, then exiting"
```

### Comparing `wigli-0.1.6/src/wigli/_wigli_data.py` & `wigli-0.1.7/src/wigli/_wigli_data.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/_wigli_plugins.py` & `wigli-0.1.7/src/wigli/_wigli_plugins.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/_wigli_testutils.py` & `wigli-0.1.7/src/wigli/_wigli_testutils.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/src/wigli/_wigli_tools.py` & `wigli-0.1.7/src/wigli/_wigli_tools.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.6/PKG-INFO` & `wigli-0.1.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wigli
-Version: 0.1.6
+Version: 0.1.7
 Summary: Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more.
 License: MIT
 Author: Douglas Graham
 Author-email: doug.n.graham@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

