# Comparing `tmp/smawe_tools-0.2.3.tar.gz` & `tmp/smawe_tools-0.2.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "smawe_tools-0.2.3.tar", last modified: Tue Apr  4 15:14:15 2023, max compression
+gzip compressed data, was "smawe_tools-0.2.4.tar", last modified: Thu Apr  6 12:28:17 2023, max compression
```

## Comparing `smawe_tools-0.2.3.tar` & `smawe_tools-0.2.4.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.294511 smawe_tools-0.2.3/
--rw-rw-rw-   0        0        0     1091 2023-01-15 03:19:33.000000 smawe_tools-0.2.3/LICENSE
--rw-rw-rw-   0        0        0     4760 2023-04-04 15:14:15.293515 smawe_tools-0.2.3/PKG-INFO
--rw-rw-rw-   0        0        0     4283 2023-04-04 15:13:27.000000 smawe_tools-0.2.3/README.md
--rw-rw-rw-   0        0        0       42 2023-04-04 15:14:15.294511 smawe_tools-0.2.3/setup.cfg
--rw-rw-rw-   0        0        0     1019 2023-04-04 10:22:33.000000 smawe_tools-0.2.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.273514 smawe_tools-0.2.3/smawe_tools/
--rw-rw-rw-   0        0        0      194 2023-04-04 09:49:25.000000 smawe_tools-0.2.3/smawe_tools/__init__.py
--rw-rw-rw-   0        0        0       76 2023-04-04 15:13:27.000000 smawe_tools-0.2.3/smawe_tools/__version__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.282510 smawe_tools-0.2.3/smawe_tools/exception/
--rw-rw-rw-   0        0        0       98 2023-04-02 12:50:55.000000 smawe_tools-0.2.3/smawe_tools/exception/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.285513 smawe_tools-0.2.3/smawe_tools/net/
--rw-rw-rw-   0        0        0       29 2023-03-29 05:15:59.000000 smawe_tools-0.2.3/smawe_tools/net/__init__.py
--rw-rw-rw-   0        0        0     2905 2023-04-04 10:22:33.000000 smawe_tools-0.2.3/smawe_tools/net/network_tool.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.288510 smawe_tools-0.2.3/smawe_tools/retrying/
--rw-rw-rw-   0        0        0       26 2023-04-04 07:07:45.000000 smawe_tools-0.2.3/smawe_tools/retrying/__init__.py
--rw-rw-rw-   0        0        0     2889 2023-04-04 14:50:18.000000 smawe_tools-0.2.3/smawe_tools/retrying/retry.py
--rw-rw-rw-   0        0        0      654 2023-04-04 09:21:43.000000 smawe_tools-0.2.3/smawe_tools/settings.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.289515 smawe_tools-0.2.3/smawe_tools/struct/
--rw-rw-rw-   0        0        0      902 2023-04-04 09:27:01.000000 smawe_tools-0.2.3/smawe_tools/struct/__init__.py
--rw-rw-rw-   0        0        0     2842 2023-03-19 15:58:44.000000 smawe_tools-0.2.3/smawe_tools/tool.py
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.281511 smawe_tools-0.2.3/smawe_tools.egg-info/
--rw-rw-rw-   0        0        0     4760 2023-04-04 15:14:15.000000 smawe_tools-0.2.3/smawe_tools.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      497 2023-04-04 15:14:15.000000 smawe_tools-0.2.3/smawe_tools.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 15:14:15.000000 smawe_tools-0.2.3/smawe_tools.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        9 2023-04-04 15:14:15.000000 smawe_tools-0.2.3/smawe_tools.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-04-04 15:14:15.000000 smawe_tools-0.2.3/smawe_tools.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-04 15:14:15.292514 smawe_tools-0.2.3/tests/
--rw-rw-rw-   0        0        0       79 2023-04-04 15:13:27.000000 smawe_tools-0.2.3/tests/test.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.548912 smawe_tools-0.2.4/
+-rw-rw-rw-   0        0        0     1091 2023-01-15 03:19:33.000000 smawe_tools-0.2.4/LICENSE
+-rw-rw-rw-   0        0        0     4922 2023-04-06 12:28:17.547913 smawe_tools-0.2.4/PKG-INFO
+-rw-rw-rw-   0        0        0     4445 2023-04-06 12:27:07.000000 smawe_tools-0.2.4/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 12:28:17.548912 smawe_tools-0.2.4/setup.cfg
+-rw-rw-rw-   0        0        0     1019 2023-04-04 10:22:33.000000 smawe_tools-0.2.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.527913 smawe_tools-0.2.4/smawe_tools/
+-rw-rw-rw-   0        0        0      194 2023-04-04 09:49:25.000000 smawe_tools-0.2.4/smawe_tools/__init__.py
+-rw-rw-rw-   0        0        0       76 2023-04-06 12:27:07.000000 smawe_tools-0.2.4/smawe_tools/__version__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.537913 smawe_tools-0.2.4/smawe_tools/exception/
+-rw-rw-rw-   0        0        0       98 2023-04-02 12:50:55.000000 smawe_tools-0.2.4/smawe_tools/exception/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.540913 smawe_tools-0.2.4/smawe_tools/net/
+-rw-rw-rw-   0        0        0       29 2023-03-29 05:15:59.000000 smawe_tools-0.2.4/smawe_tools/net/__init__.py
+-rw-rw-rw-   0        0        0     2905 2023-04-04 10:22:33.000000 smawe_tools-0.2.4/smawe_tools/net/network_tool.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.543913 smawe_tools-0.2.4/smawe_tools/retrying/
+-rw-rw-rw-   0        0        0       26 2023-04-04 07:07:45.000000 smawe_tools-0.2.4/smawe_tools/retrying/__init__.py
+-rw-rw-rw-   0        0        0     2889 2023-04-04 14:50:18.000000 smawe_tools-0.2.4/smawe_tools/retrying/retry.py
+-rw-rw-rw-   0        0        0      654 2023-04-04 09:21:43.000000 smawe_tools-0.2.4/smawe_tools/settings.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.544913 smawe_tools-0.2.4/smawe_tools/struct/
+-rw-rw-rw-   0        0        0      946 2023-04-06 10:03:49.000000 smawe_tools-0.2.4/smawe_tools/struct/__init__.py
+-rw-rw-rw-   0        0        0     2842 2023-03-19 15:58:44.000000 smawe_tools-0.2.4/smawe_tools/tool.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.535912 smawe_tools-0.2.4/smawe_tools.egg-info/
+-rw-rw-rw-   0        0        0     4922 2023-04-06 12:28:17.000000 smawe_tools-0.2.4/smawe_tools.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      497 2023-04-06 12:28:17.000000 smawe_tools-0.2.4/smawe_tools.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 12:28:17.000000 smawe_tools-0.2.4/smawe_tools.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 12:28:17.000000 smawe_tools-0.2.4/smawe_tools.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-06 12:28:17.000000 smawe_tools-0.2.4/smawe_tools.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 12:28:17.545914 smawe_tools-0.2.4/tests/
+-rw-rw-rw-   0        0        0       79 2023-04-06 12:20:07.000000 smawe_tools-0.2.4/tests/test.py
```

### Comparing `smawe_tools-0.2.3/LICENSE` & `smawe_tools-0.2.4/LICENSE`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/PKG-INFO` & `smawe_tools-0.2.4/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: smawe_tools
-Version: 0.2.3
+Version: 0.2.4
 Summary: small tool
 Author: Samwe
 Author-email: 1281722462@qq.com
 License: MIT
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: Implementation :: CPython
@@ -40,28 +40,33 @@
 
 - get_ip(url, domain):  
     获取目标网站url或者域名domain的ip地址  
     返回包含ip地址的列表
 
 
 - get_pubnet_ip():  
-    获取本机的外网ip(也就是上网时所使用的ip)  
+    获取本机的公网ip(也就是上网时所使用的ip)  
     return: str
 
 
-- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None):  
+- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None, retry_exception=None):  
     发生异常进行重试，默认进行1次重试且每次重试前睡眠0-1s的随机时间，超过最大重试次数后还发生异常，则抛出MaxRetryError异常 
     重试期间如果正常返回结果或没发生异常，则不进行重试。
     stop_max_attempt_number: 停止时的最大重试次数，超出次数后还发生异常，则抛出MaxRetryError异常  
     wait_random_min：随机等待的最小时间(单位毫秒)  
-    wait_random_max: 随机等待的最大时间(单位毫秒) 
-
+    wait_random_max: 随机等待的最大时间(单位毫秒)  
+    retry_exception: 要重试的异常类型，默认为Exception
   
 - modify_encoding():   
-    此函数要从smawe_tools.settings模块进行导入，如: from smawe_tools.settings import modify_encoding  
+    此函数要从smawe_tools.settings模块进行导入, 如: 
+    ```
+    from smawe_tools.settings import modify_encoding 
+    # 直接调用即可
+    modify_encoding()  
+    ```
     调用此函数可以修正以下此类的错误:  
     UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 188608: illegal multibyte sequence
     
 ---
 
 **启用默认日志**  
 *默认日志级别为logging.INFO*
```

### Comparing `smawe_tools-0.2.3/README.md` & `smawe_tools-0.2.4/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -25,28 +25,33 @@
 
 - get_ip(url, domain):  
     获取目标网站url或者域名domain的ip地址  
     返回包含ip地址的列表
 
 
 - get_pubnet_ip():  
-    获取本机的外网ip(也就是上网时所使用的ip)  
+    获取本机的公网ip(也就是上网时所使用的ip)  
     return: str
 
 
-- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None):  
+- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None, retry_exception=None):  
     发生异常进行重试，默认进行1次重试且每次重试前睡眠0-1s的随机时间，超过最大重试次数后还发生异常，则抛出MaxRetryError异常 
     重试期间如果正常返回结果或没发生异常，则不进行重试。
     stop_max_attempt_number: 停止时的最大重试次数，超出次数后还发生异常，则抛出MaxRetryError异常  
     wait_random_min：随机等待的最小时间(单位毫秒)  
-    wait_random_max: 随机等待的最大时间(单位毫秒) 
-
+    wait_random_max: 随机等待的最大时间(单位毫秒)  
+    retry_exception: 要重试的异常类型，默认为Exception
   
 - modify_encoding():   
-    此函数要从smawe_tools.settings模块进行导入，如: from smawe_tools.settings import modify_encoding  
+    此函数要从smawe_tools.settings模块进行导入, 如: 
+    ```
+    from smawe_tools.settings import modify_encoding 
+    # 直接调用即可
+    modify_encoding()  
+    ```
     调用此函数可以修正以下此类的错误:  
     UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 188608: illegal multibyte sequence
     
 ---
 
 **启用默认日志**  
 *默认日志级别为logging.INFO*
```

### Comparing `smawe_tools-0.2.3/setup.py` & `smawe_tools-0.2.4/setup.py`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/smawe_tools/net/network_tool.py` & `smawe_tools-0.2.4/smawe_tools/net/network_tool.py`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/smawe_tools/retrying/retry.py` & `smawe_tools-0.2.4/smawe_tools/retrying/retry.py`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/smawe_tools/settings.py` & `smawe_tools-0.2.4/smawe_tools/settings.py`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/smawe_tools/struct/__init__.py` & `smawe_tools-0.2.4/smawe_tools/struct/__init__.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,28 +1,27 @@
 from types import ModuleType
 import logging
 import sys
 
 
 class LoggingModule(ModuleType):
 
+    _name = "smawe_tools.settings"
+
     def __getattr__(self, name):
-        if "__getattr__" in sys.modules[__name__].__dict__:
-            r = sys.modules[__name__].__dict__["__getattr__"](name)
+        if "__getattr__" in sys.modules["__main__"].__dict__:
+            r = sys.modules["__main__"].__dict__["__getattr__"](name)
             if not r:
-                raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
+                raise AttributeError(f"module {type(self)._name!r} has no attribute {name!r}")
             return r
+        raise AttributeError(f"module {type(self)._name!r} has no attribute {name!r}")
 
-    def __getattribute__(self, name):
-        return super(LoggingModule, self).__getattribute__(name)
+    def __getattribute__(self, name: str):
+        return object.__getattribute__(self, name)
 
     def __setattr__(self, attr, value):
         if attr == "ENABLED_LOG":
             if value:
                 logging.basicConfig(format="%(asctime)s:%(filename)s:%(threadName)s:%(levelname)s:%(message)s",
                                     level=logging.INFO)
         super().__setattr__(attr, value)
 
-
-def __getattr__(name: str):
-    if name.lower() == "debug":
-        return True
```

### Comparing `smawe_tools-0.2.3/smawe_tools/tool.py` & `smawe_tools-0.2.4/smawe_tools/tool.py`

 * *Files identical despite different names*

### Comparing `smawe_tools-0.2.3/smawe_tools.egg-info/PKG-INFO` & `smawe_tools-0.2.4/smawe_tools.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: smawe-tools
-Version: 0.2.3
+Version: 0.2.4
 Summary: small tool
 Author: Samwe
 Author-email: 1281722462@qq.com
 License: MIT
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: Implementation :: CPython
@@ -40,28 +40,33 @@
 
 - get_ip(url, domain):  
     获取目标网站url或者域名domain的ip地址  
     返回包含ip地址的列表
 
 
 - get_pubnet_ip():  
-    获取本机的外网ip(也就是上网时所使用的ip)  
+    获取本机的公网ip(也就是上网时所使用的ip)  
     return: str
 
 
-- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None):  
+- retry(stop_max_attempt_number=None, wait_random_min=None, wait_random_max=None, retry_exception=None):  
     发生异常进行重试，默认进行1次重试且每次重试前睡眠0-1s的随机时间，超过最大重试次数后还发生异常，则抛出MaxRetryError异常 
     重试期间如果正常返回结果或没发生异常，则不进行重试。
     stop_max_attempt_number: 停止时的最大重试次数，超出次数后还发生异常，则抛出MaxRetryError异常  
     wait_random_min：随机等待的最小时间(单位毫秒)  
-    wait_random_max: 随机等待的最大时间(单位毫秒) 
-
+    wait_random_max: 随机等待的最大时间(单位毫秒)  
+    retry_exception: 要重试的异常类型，默认为Exception
   
 - modify_encoding():   
-    此函数要从smawe_tools.settings模块进行导入，如: from smawe_tools.settings import modify_encoding  
+    此函数要从smawe_tools.settings模块进行导入, 如: 
+    ```
+    from smawe_tools.settings import modify_encoding 
+    # 直接调用即可
+    modify_encoding()  
+    ```
     调用此函数可以修正以下此类的错误:  
     UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 188608: illegal multibyte sequence
     
 ---
 
 **启用默认日志**  
 *默认日志级别为logging.INFO*
```

