# Comparing `tmp/snowflake-util-1.0.0b4.tar.gz` & `tmp/snowflake-util-1.0.0b6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "snowflake-util-1.0.0b4.tar", last modified: Sat Jul 30 15:07:10 2022, max compression
+gzip compressed data, was "snowflake-util-1.0.0b6.tar", last modified: Thu Apr  6 18:54:56 2023, max compression
```

## Comparing `snowflake-util-1.0.0b4.tar` & `snowflake-util-1.0.0b6.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2022-07-30 15:07:10.942867 snowflake-util-1.0.0b4/
--rw-rw-rw-   0        0        0     1087 2022-07-30 14:25:09.000000 snowflake-util-1.0.0b4/LICENSE
--rw-rw-rw-   0        0        0     3890 2022-07-30 15:07:10.941865 snowflake-util-1.0.0b4/PKG-INFO
--rw-rw-rw-   0        0        0     3178 2022-07-30 15:04:37.000000 snowflake-util-1.0.0b4/README.md
--rw-rw-rw-   0        0        0       42 2022-07-30 15:07:10.942867 snowflake-util-1.0.0b4/setup.cfg
--rw-rw-rw-   0        0        0     1198 2022-07-30 15:06:42.000000 snowflake-util-1.0.0b4/setup.py
-drwxrwxrwx   0        0        0        0 2022-07-30 15:07:10.913042 snowflake-util-1.0.0b4/snowflake/
--rw-rw-rw-   0        0        0     1212 2022-07-30 13:09:18.000000 snowflake-util-1.0.0b4/snowflake/__init__.py
--rw-rw-rw-   0        0        0     4398 2022-07-30 12:53:42.000000 snowflake-util-1.0.0b4/snowflake/config.py
--rw-rw-rw-   0        0        0     1367 2022-07-30 11:31:57.000000 snowflake-util-1.0.0b4/snowflake/enums.py
--rw-rw-rw-   0        0        0    18945 2022-07-30 15:06:57.000000 snowflake-util-1.0.0b4/snowflake/snowflake.py
-drwxrwxrwx   0        0        0        0 2022-07-30 15:07:10.938852 snowflake-util-1.0.0b4/snowflake_util.egg-info/
--rw-rw-rw-   0        0        0     3890 2022-07-30 15:07:10.000000 snowflake-util-1.0.0b4/snowflake_util.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      262 2022-07-30 15:07:10.000000 snowflake-util-1.0.0b4/snowflake_util.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-07-30 15:07:10.000000 snowflake-util-1.0.0b4/snowflake_util.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       10 2022-07-30 15:07:10.000000 snowflake-util-1.0.0b4/snowflake_util.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 18:54:56.837753 snowflake-util-1.0.0b6/
+-rw-rw-rw-   0        0        0     1087 2023-04-05 20:44:31.000000 snowflake-util-1.0.0b6/LICENSE
+-rw-rw-rw-   0        0        0     4117 2023-04-06 18:54:56.836757 snowflake-util-1.0.0b6/PKG-INFO
+-rw-rw-rw-   0        0        0     3148 2023-04-06 18:53:02.000000 snowflake-util-1.0.0b6/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 18:54:56.837753 snowflake-util-1.0.0b6/setup.cfg
+-rw-rw-rw-   0        0        0     1450 2023-04-06 18:54:51.000000 snowflake-util-1.0.0b6/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:54:56.820753 snowflake-util-1.0.0b6/snowflake/
+-rw-rw-rw-   0        0        0     1212 2023-04-05 20:44:31.000000 snowflake-util-1.0.0b6/snowflake/__init__.py
+-rw-rw-rw-   0        0        0     4398 2023-04-05 20:44:31.000000 snowflake-util-1.0.0b6/snowflake/config.py
+-rw-rw-rw-   0        0        0     1367 2023-04-05 20:44:31.000000 snowflake-util-1.0.0b6/snowflake/enums.py
+-rw-rw-rw-   0        0        0    19157 2023-04-06 18:52:03.000000 snowflake-util-1.0.0b6/snowflake/snowflake.py
+drwxrwxrwx   0        0        0        0 2023-04-06 18:54:56.835758 snowflake-util-1.0.0b6/snowflake_util.egg-info/
+-rw-rw-rw-   0        0        0     4117 2023-04-06 18:54:56.000000 snowflake-util-1.0.0b6/snowflake_util.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      262 2023-04-06 18:54:56.000000 snowflake-util-1.0.0b6/snowflake_util.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 18:54:56.000000 snowflake-util-1.0.0b6/snowflake_util.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       10 2023-04-06 18:54:56.000000 snowflake-util-1.0.0b6/snowflake_util.egg-info/top_level.txt
```

### Comparing `snowflake-util-1.0.0b4/LICENSE` & `snowflake-util-1.0.0b6/LICENSE`

 * *Files identical despite different names*

### Comparing `snowflake-util-1.0.0b4/PKG-INFO` & `snowflake-util-1.0.0b6/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,22 @@
 Metadata-Version: 2.1
 Name: snowflake-util
-Version: 1.0.0b4
+Version: 1.0.0b6
 Summary: A Python library for generating snowflakes.
 Author: TheMultii
 Project-URL: Repository, https://github.com/TheMultii/snowflake-util
 Keywords: python,snowflake,generator,custom,library,id generator,uid
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Operating System :: Unix
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Operating System :: Microsoft :: Windows
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
@@ -58,35 +63,35 @@
 print(custom_snowflake_TS, SnowClass.parse_snowflake(custom_snowflake_TS))
 ```
 
 Creating a Discord snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-discord_snowflake = SnowflakeClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+discord_snowflake = SnowClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_discord_snowflake(discord_snowflake))
+print(y, SnowClass.parse_discord_snowflake(discord_snowflake))
 ```
 
 Creating a Twitter snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-twitter_snowflake = SnowflakeClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+twitter_snowflake = SnowClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_twitter_snowflake(twitter_snowflake))
+print(y, SnowClass.parse_twitter_snowflake(twitter_snowflake))
 ```
 
 Creating an Instagram snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-instagram_snowflake = SnowflakeClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
+instagram_snowflake = SnowClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
 
-print(y, SnowflakeClass.parse_instagram_snowflake(instagram_snowflake))
+print(y, SnowClass.parse_instagram_snowflake(instagram_snowflake))
 ```
 
 ## IMPORTANT INFO:
 - Generating any snowflakes does not require sending the date as an argument - the snowflake will be generated based on the current time.
 - `snowflake.SnowflakeConfig` is not required if you want to use any of the ready-made templates for generating/reading snowflakes (Twitter, Discord, Instagram)
 - You can edit and read the current configuration settings using the `Snowflake.set_config()` and `Snowflake.get_config()` methods.
 - All methods are documented in the code.
```

### Comparing `snowflake-util-1.0.0b4/README.md` & `snowflake-util-1.0.0b6/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -41,35 +41,35 @@
 print(custom_snowflake_TS, SnowClass.parse_snowflake(custom_snowflake_TS))
 ```
 
 Creating a Discord snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-discord_snowflake = SnowflakeClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+discord_snowflake = SnowClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_discord_snowflake(discord_snowflake))
+print(y, SnowClass.parse_discord_snowflake(discord_snowflake))
 ```
 
 Creating a Twitter snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-twitter_snowflake = SnowflakeClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+twitter_snowflake = SnowClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_twitter_snowflake(twitter_snowflake))
+print(y, SnowClass.parse_twitter_snowflake(twitter_snowflake))
 ```
 
 Creating an Instagram snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-instagram_snowflake = SnowflakeClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
+instagram_snowflake = SnowClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
 
-print(y, SnowflakeClass.parse_instagram_snowflake(instagram_snowflake))
+print(y, SnowClass.parse_instagram_snowflake(instagram_snowflake))
 ```
 
 ## IMPORTANT INFO:
 - Generating any snowflakes does not require sending the date as an argument - the snowflake will be generated based on the current time.
 - `snowflake.SnowflakeConfig` is not required if you want to use any of the ready-made templates for generating/reading snowflakes (Twitter, Discord, Instagram)
 - You can edit and read the current configuration settings using the `Snowflake.set_config()` and `Snowflake.get_config()` methods.
 - All methods are documented in the code.
```

### Comparing `snowflake-util-1.0.0b4/setup.py` & `snowflake-util-1.0.0b6/setup.py`

 * *Files 21% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 import os
 
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
     long_description = f"\n{f.read()}"
 
-VERSION = '1.0.0b4'
+VERSION = '1.0.0b6'
 DESCRIPTION = 'A Python library for generating snowflakes.'
 LONG_DESCRIPTION = 'A Python library for generating Discord, Twitter, Instagram and custom snowflakes.'
 
 # Setup
 setup(
     name='snowflake-util',
     version=VERSION,
@@ -25,12 +25,17 @@
     },
     install_requires=[],
     keywords=['python', 'snowflake', 'generator', 'custom', 'library', 'id generator', 'uid'],
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3",
+        "Programming Language :: Python :: 3.7",
+        "Programming Language :: Python :: 3.8",
+        "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
         "Operating System :: Unix",
         "Operating System :: MacOS :: MacOS X",
         "Operating System :: Microsoft :: Windows",
     ]
 )
```

### Comparing `snowflake-util-1.0.0b4/snowflake/__init__.py` & `snowflake-util-1.0.0b6/snowflake/__init__.py`

 * *Files identical despite different names*

### Comparing `snowflake-util-1.0.0b4/snowflake/config.py` & `snowflake-util-1.0.0b6/snowflake/config.py`

 * *Files identical despite different names*

### Comparing `snowflake-util-1.0.0b4/snowflake/enums.py` & `snowflake-util-1.0.0b6/snowflake/enums.py`

 * *Files identical despite different names*

### Comparing `snowflake-util-1.0.0b4/snowflake/snowflake.py` & `snowflake-util-1.0.0b6/snowflake/snowflake.py`

 * *Files 1% similar despite different names*

```diff
@@ -112,15 +112,15 @@
         --------
 
         snowflake.SnowflakeConfig
             The configuration to use for the snowflake.
         """
         return self.__config
 
-    def generate_discord_snowflake(self, worker: int, process: int, sequence: int, date: Optional[datetime] = datetime.now()) -> str:
+    def generate_discord_snowflake(self, worker: int, process: int, sequence: int, date: Optional[datetime] = None) -> str:
         """
         Generates a snowflake in the Discord format.
 
         Parameters:
         -----------
 
         worker: int
@@ -146,14 +146,17 @@
         ValueError:
             If provided datetime is before the Discord epoch.
         """
         assert 0 <= worker < 32, "Worker must be between 0 and 31."
         assert 0 <= process < 32, "Process must be between 0 and 31."
         assert 0 <= sequence < 4096, "Sequence must be between 0 and 4095."
 
+        if date is None:
+            date = datetime.now()
+
         __dt_calculated = round(date.timestamp() * 1000) - Epoch.discord.value
         if __dt_calculated < 0:
             raise ValueError("Provided date is before the Discord epoch.")
 
         __binary_dt_calculated = bin(__dt_calculated)[2:].zfill(42)
         __binary_worker = bin(worker)[2:].zfill(5)
         __binary_process = bin(process)[2:].zfill(5)
@@ -202,15 +205,15 @@
         __sequence = int(__binary_sequence, 2)
 
         __timestamp = round((__timestamp + Epoch.discord.value) / 1000)
         __date = datetime.fromtimestamp(__timestamp)
 
         return __date, __worker, __process, __sequence
 
-    def generate_twitter_snowflake(self, machine: int, sequence: int, date: Optional[datetime] = datetime.now()) -> str:
+    def generate_twitter_snowflake(self, machine: int, sequence: int, date: Optional[datetime] = None) -> str:
         """
         Generates a snowflake in the Twitter format.
 
         Parameters:
         -----------
 
         machine: int
@@ -233,14 +236,17 @@
             If provided arguments are somehow invalid.
         ValueError:
             If provided datetime is before the Twitter epoch.
         """
         assert 0 <= machine < 1024, "Worker must be between 0 and 1023."
         assert 0 <= sequence < 4096, "Sequence must be between 0 and 4095."
 
+        if date is None:
+            date = datetime.now()
+
         __dt_calculated = round(date.timestamp() * 1000) - Epoch.twitter.value
         if __dt_calculated < 0:
             raise ValueError("Provided date is before the Twitter epoch.")
 
         __binary_dt_calculated = bin(__dt_calculated)[2:].zfill(41)
         __binary_machine = bin(machine)[2:].zfill(10)
         __binary_sequence = bin(sequence)[2:].zfill(12)
@@ -285,15 +291,15 @@
         __sequence = int(__binary_sequence, 2)
 
         __timestamp = round((__timestamp + Epoch.twitter.value) / 1000)
         __date = datetime.fromtimestamp(__timestamp)
 
         return __date, __machine, __sequence
 
-    def generate_instagram_snowflake(self, shard: int, sequence: int, date: Optional[datetime] = datetime.now()) -> str:
+    def generate_instagram_snowflake(self, shard: int, sequence: int, date: Optional[datetime] = None) -> str:
         """
         Generates a snowflake in the Instagram format.
 
         Parameters:
         -----------
 
         shard: int
@@ -316,14 +322,17 @@
             If provided arguemnts are somehow invalid.
         ValueError:
             If provided datetime is before the Instagram epoch.
         """
         assert 0 <= shard < 8192, "Shard must be between 0 and 8191."
         assert 0 <= sequence < 1024, "Sequence must be between 0 and 1023."
 
+        if date is None:
+            date = datetime.now()
+
         __dt_calculated = round(date.timestamp() * 1000) - Epoch.instagram.value
         if __dt_calculated < 0:
             raise ValueError("Provided date is before the Instagram epoch.")
 
         __binary_dt_calculated = bin(__dt_calculated)[2:].zfill(41)
         __binary_shard = bin(shard)[2:].zfill(13)
         __binary_sequence = bin(sequence)[2:].zfill(10)
@@ -368,15 +377,15 @@
         __sequence = int(__binary_sequence, 2)
 
         __timestamp = round((__timestamp + Epoch.instagram.value) / 1000)
         __date = datetime.fromtimestamp(__timestamp)
 
         return __date, __shard, __sequence
 
-    def generate_snowflake(self, param1: int, sequence: int, date: Optional[datetime] = datetime.now(), **kwargs) -> str:
+    def generate_snowflake(self, param1: int, sequence: int, date: Optional[datetime] = None, **kwargs) -> str:
         """
         Generates a snowflake in the specified format.
         
         Parameters:
         -----------
 
         param1: int
@@ -413,14 +422,17 @@
         __param2 = kwargs.get("param2", None)
         if __param2 is None and self.__config.param2_length > 0:
             raise TypeError("Required param2 is not provided.")
         
         assert 0 <= param1 < 10 ** self.__config.param1_length, "Param1 must be between 0 and (10**(config.param1_length) - 1)"
         assert 0 <= sequence < 10 ** self.__config.sequence_length, "Sequence must be between 0 and (10**(config.sequence_length) - 1)"
 
+        if date is None:
+            date = datetime.now()
+
         __dt_calculated = round(date.timestamp() * 1000) - self.__config.epoch.value
         if __dt_calculated < 0:
             raise ValueError("Provided date is before the epoch.")
         __binary_dt_calculated = bin(__dt_calculated)[2:].zfill(self.__config.timestamp_length)
         __param1_calculated = bin(param1)[2:].zfill(self.__config.param1_length)
         __param2_calculated = None
         if __param2 is not None:
```

### Comparing `snowflake-util-1.0.0b4/snowflake_util.egg-info/PKG-INFO` & `snowflake-util-1.0.0b6/snowflake_util.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,22 @@
 Metadata-Version: 2.1
 Name: snowflake-util
-Version: 1.0.0b4
+Version: 1.0.0b6
 Summary: A Python library for generating snowflakes.
 Author: TheMultii
 Project-URL: Repository, https://github.com/TheMultii/snowflake-util
 Keywords: python,snowflake,generator,custom,library,id generator,uid
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Operating System :: Unix
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Operating System :: Microsoft :: Windows
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
@@ -58,35 +63,35 @@
 print(custom_snowflake_TS, SnowClass.parse_snowflake(custom_snowflake_TS))
 ```
 
 Creating a Discord snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-discord_snowflake = SnowflakeClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+discord_snowflake = SnowClass.generate_discord_snowflake(worker=5, process=5, sequence=222, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_discord_snowflake(discord_snowflake))
+print(y, SnowClass.parse_discord_snowflake(discord_snowflake))
 ```
 
 Creating a Twitter snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-twitter_snowflake = SnowflakeClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
+twitter_snowflake = SnowClass.generate_twitter_snowflake(machine=333, sequence=666, date=datetime(2022, 1, 1, 16, 15, 0, 0))
 
-print(y, SnowflakeClass.parse_twitter_snowflake(twitter_snowflake))
+print(y, SnowClass.parse_twitter_snowflake(twitter_snowflake))
 ```
 
 Creating an Instagram snowflake
 ```python
 SnowClass = snowflake.Snowflake()
 
-instagram_snowflake = SnowflakeClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
+instagram_snowflake = SnowClass.generate_instagram_snowflake(shard=1605, sequence=420, date=datetime(2020, 6, 11, 8 ,13))
 
-print(y, SnowflakeClass.parse_instagram_snowflake(instagram_snowflake))
+print(y, SnowClass.parse_instagram_snowflake(instagram_snowflake))
 ```
 
 ## IMPORTANT INFO:
 - Generating any snowflakes does not require sending the date as an argument - the snowflake will be generated based on the current time.
 - `snowflake.SnowflakeConfig` is not required if you want to use any of the ready-made templates for generating/reading snowflakes (Twitter, Discord, Instagram)
 - You can edit and read the current configuration settings using the `Snowflake.set_config()` and `Snowflake.get_config()` methods.
 - All methods are documented in the code.
```

