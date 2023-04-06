# Comparing `tmp/KUKA_youbot-0.0.8.tar.gz` & `tmp/KUKA_youbot-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "KUKA_youbot-0.0.8.tar", last modified: Wed Mar 22 05:14:34 2023, max compression
+gzip compressed data, was "KUKA_youbot-0.1.0.tar", last modified: Thu Apr  6 18:21:48 2023, max compression
```

## Comparing `KUKA_youbot-0.0.8.tar` & `KUKA_youbot-0.1.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1074 2023-03-18 13:45:02.000000 KUKA_youbot-0.0.8/LICENSE
--rw-rw-r--   0 mark      (1000) mark      (1000)     4457 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/PKG-INFO
--rw-rw-r--   0 mark      (1000) mark      (1000)     3944 2023-03-18 13:50:26.000000 KUKA_youbot-0.0.8/README.md
--rw-rw-r--   0 mark      (1000) mark      (1000)      760 2023-03-22 04:53:34.000000 KUKA_youbot-0.0.8/pyproject.toml
--rw-rw-r--   0 mark      (1000) mark      (1000)       38 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/setup.cfg
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/src/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/src/KUKA/
--rw-rw-r--   0 mark      (1000) mark      (1000)    33261 2023-03-22 04:49:29.000000 KUKA_youbot-0.0.8/src/KUKA/KUKA.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7226 2023-03-22 04:49:20.000000 KUKA_youbot-0.0.8/src/KUKA/SSH.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       24 2023-03-17 08:35:01.000000 KUKA_youbot-0.0.8/src/KUKA/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      382 2023-03-18 13:10:48.000000 KUKA_youbot-0.0.8/src/KUKA/service.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-03-22 05:14:34.766017 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4457 2023-03-22 05:14:34.000000 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/PKG-INFO
--rw-rw-r--   0 mark      (1000) mark      (1000)      300 2023-03-22 05:14:34.000000 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/SOURCES.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)        1 2023-03-22 05:14:34.000000 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/dependency_links.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)      103 2023-03-22 05:14:34.000000 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/requires.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)        5 2023-03-22 05:14:34.000000 KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/top_level.txt
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-04-06 18:21:48.407027 KUKA_youbot-0.1.0/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1074 2023-03-18 13:45:02.000000 KUKA_youbot-0.1.0/LICENSE
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4449 2023-04-06 18:21:48.403027 KUKA_youbot-0.1.0/PKG-INFO
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3944 2023-03-18 13:50:26.000000 KUKA_youbot-0.1.0/README.md
+-rw-rw-r--   0 mark      (1000) mark      (1000)      752 2023-04-06 18:21:35.000000 KUKA_youbot-0.1.0/pyproject.toml
+-rw-rw-r--   0 mark      (1000) mark      (1000)       38 2023-04-06 18:21:48.407027 KUKA_youbot-0.1.0/setup.cfg
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-04-06 18:21:48.403027 KUKA_youbot-0.1.0/src/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-04-06 18:21:48.403027 KUKA_youbot-0.1.0/src/KUKA/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    33277 2023-04-06 18:19:30.000000 KUKA_youbot-0.1.0/src/KUKA/KUKA.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7226 2023-03-22 04:49:20.000000 KUKA_youbot-0.1.0/src/KUKA/SSH.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       24 2023-03-17 08:35:01.000000 KUKA_youbot-0.1.0/src/KUKA/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      382 2023-03-18 13:10:48.000000 KUKA_youbot-0.1.0/src/KUKA/service.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2023-04-06 18:21:48.403027 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4449 2023-04-06 18:21:48.000000 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/PKG-INFO
+-rw-rw-r--   0 mark      (1000) mark      (1000)      300 2023-04-06 18:21:48.000000 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/SOURCES.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)        1 2023-04-06 18:21:48.000000 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/dependency_links.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)      103 2023-04-06 18:21:48.000000 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/requires.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)        5 2023-04-06 18:21:48.000000 KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/top_level.txt
```

### Comparing `KUKA_youbot-0.0.8/LICENSE` & `KUKA_youbot-0.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `KUKA_youbot-0.0.8/PKG-INFO` & `KUKA_youbot-0.1.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: KUKA_youbot
-Version: 0.0.8
+Version: 0.1.0
 Summary: package for easy KUKA-youbot control
 Author-email: ZaSKaR <mark.turkov@mail.ru>
-Project-URL: Homepage, https://github.com/MarkT5/KUKAyoubot_lib
-Project-URL: Bug Tracker, https://github.com/MarkT5/KUKAyoubot_lib/issues
+Project-URL: Homepage, https://github.com/MarkT5/YouBotKUKA
+Project-URL: Bug Tracker, https://github.com/MarkT5/YouBotKUKA/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: Framework :: Robot Framework :: Tool
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `KUKA_youbot-0.0.8/README.md` & `KUKA_youbot-0.1.0/README.md`

 * *Files identical despite different names*

### Comparing `KUKA_youbot-0.0.8/pyproject.toml` & `KUKA_youbot-0.1.0/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 [project]
 name = "KUKA_youbot"
-version = "0.0.8"
+version = "0.1.0"
 authors = [
   { name="ZaSKaR", email="mark.turkov@mail.ru" },
 ]
 dependencies = [
     "setuptools >= 40.9.0",
     "numpy >= 1.24.2",
     "opencv-python >= 4.7.0.72",
@@ -20,9 +20,9 @@
 requires-python = ">=3.8"
 classifiers = [
     "Programming Language :: Python :: 3",
     "Framework :: Robot Framework :: Tool",
     "Operating System :: OS Independent",
 ]
 [project.urls]
-"Homepage" = "https://github.com/MarkT5/KUKAyoubot_lib"
-"Bug Tracker" = "https://github.com/MarkT5/KUKAyoubot_lib/issues"
+"Homepage" = "https://github.com/MarkT5/YouBotKUKA"
+"Bug Tracker" = "https://github.com/MarkT5/YouBotKUKA/issues"
```

### Comparing `KUKA_youbot-0.0.8/src/KUKA/KUKA.py` & `KUKA_youbot-0.1.0/src/KUKA/KUKA.py`

 * *Files 2% similar despite different names*

```diff
@@ -373,41 +373,43 @@
     def _receive_data(self):
         """
         Reads data from sensors data port (thread)
         """
 
         data_buff_len = 0
         self.data_buff = b''
+        leftovers = b''
         while self.main_thr.is_alive():
-            if data_buff_len > 5000:
-                self.data_buff = b''
-                data_buff_len = 0
             try:
-                el = self.conn.recv(1)
+                el = self.conn.recv(4096)
+
             except TimeoutError:
                 debug("_receive_data thread died due to timeout")
                 break
             except Exception as exc:
                 debug(f"_receive_data thread died due to {exc}")
                 break
 
             if el != b'':
                 self.data_buff += el
-                data_buff_len += 1
-            if data_buff_len > 0 and self.data_buff[-1] == 13:
-                self.conn.recv(1)
-
                 try:
                     str_data = str(self.data_buff[:-1], encoding='utf-8')
-                    self.data_parser_tht = thr.Thread(target=self._parse_data, args=(str_data,))
-                    self.data_parser_tht.start()
-                except:
+                    last = str_data.rfind("\r\n")
+
+                    if last == -1:
+                        leftovers = self.data_buff[:]
+                    else:
+
+                        leftovers = str.encode(str_data[last+2:])
+                        str_data = str_data[:last]
+                        self._parse_data(str_data[:str_data.find("\r\n")])
+                except Exception as e:
+                    debug(e)
                     pass
-                self.data_buff = b''
-                data_buff_len = 0
+                self.data_buff = leftovers
         self.threads_number -= 1
         debug(f"_receive_data thread terminated, {self.threads_number} threads remain")
 
     def logger(self, path, freq):
         '''
         Logs odometry and lidar data to path with set frequency
         :param path: name and path to log file
```

### Comparing `KUKA_youbot-0.0.8/src/KUKA/SSH.py` & `KUKA_youbot-0.1.0/src/KUKA/SSH.py`

 * *Files identical despite different names*

### Comparing `KUKA_youbot-0.0.8/src/KUKA_youbot.egg-info/PKG-INFO` & `KUKA_youbot-0.1.0/src/KUKA_youbot.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: KUKA-youbot
-Version: 0.0.8
+Version: 0.1.0
 Summary: package for easy KUKA-youbot control
 Author-email: ZaSKaR <mark.turkov@mail.ru>
-Project-URL: Homepage, https://github.com/MarkT5/KUKAyoubot_lib
-Project-URL: Bug Tracker, https://github.com/MarkT5/KUKAyoubot_lib/issues
+Project-URL: Homepage, https://github.com/MarkT5/YouBotKUKA
+Project-URL: Bug Tracker, https://github.com/MarkT5/YouBotKUKA/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: Framework :: Robot Framework :: Tool
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

