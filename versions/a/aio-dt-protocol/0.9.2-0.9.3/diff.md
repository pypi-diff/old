# Comparing `tmp/aio_dt_protocol-0.9.2.tar.gz` & `tmp/aio_dt_protocol-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aio_dt_protocol-0.9.2.tar", last modified: Thu Apr  6 11:02:19 2023, max compression
+gzip compressed data, was "aio_dt_protocol-0.9.3.tar", last modified: Fri Apr  7 08:37:13 2023, max compression
```

## Comparing `aio_dt_protocol-0.9.2.tar` & `aio_dt_protocol-0.9.3.tar`

### file list

```diff
@@ -1,41 +1,41 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 11:02:19.943985 aio_dt_protocol-0.9.2/
--rw-rw-rw-   0        0        0     1526 2023-04-05 18:37:56.000000 aio_dt_protocol-0.9.2/LICENSE
--rw-rw-rw-   0        0        0     5620 2023-04-06 11:02:19.943985 aio_dt_protocol-0.9.2/PKG-INFO
--rw-rw-rw-   0        0        0     4878 2023-04-06 08:59:38.000000 aio_dt_protocol-0.9.2/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 11:02:19.885005 aio_dt_protocol-0.9.2/aio_dt_protocol/
--rw-rw-rw-   0        0        0    34959 2023-04-05 07:22:52.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/Actions.py
--rw-rw-rw-   0        0        0    53568 2023-04-06 06:48:58.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/Browser.py
--rw-rw-rw-   0        0        0     9971 2023-04-04 10:33:45.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/BrowserEx.py
--rw-rw-rw-   0        0        0    35317 2023-04-05 07:22:52.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/DOMElement.py
--rw-rw-rw-   0        0        0    32529 2023-04-05 17:29:55.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/Data.py
--rw-rw-rw-   0        0        0    22749 2023-04-06 07:01:02.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/Page.py
--rw-rw-rw-   0        0        0    16186 2023-04-05 18:34:56.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/PageEx.py
--rw-rw-rw-   0        0        0      399 2023-04-06 10:57:43.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 11:02:19.942983 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/
--rw-rw-rw-   0        0        0     3631 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/BackgroundService.py
--rw-rw-rw-   0        0        0    13809 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Browser.py
--rw-rw-rw-   0        0        0     7070 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/CSS.py
--rw-rw-rw-   0        0        0     2045 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Console.py
--rw-rw-rw-   0        0        0    16735 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/DOM.py
--rw-rw-rw-   0        0        0     1846 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/DeviceOrientation.py
--rw-rw-rw-   0        0        0    24645 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Emulation.py
--rw-rw-rw-   0        0        0    23128 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Fetch.py
--rw-rw-rw-   0        0        0     2066 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Log.py
--rw-rw-rw-   0        0        0    22099 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Network.py
--rw-rw-rw-   0        0        0     2124 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Overlay.py
--rw-rw-rw-   0        0        0    35374 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Page.py
--rw-rw-rw-   0        0        0    32897 2023-04-05 17:56:11.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Runtime.py
--rw-rw-rw-   0        0        0     1712 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/SystemInfo.py
--rw-rw-rw-   0        0        0    17569 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Target.py
--rw-rw-rw-   0        0        0        0 2021-06-02 19:57:07.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/domains/__init__.py
--rw-rw-rw-   0        0        0     3148 2023-04-05 17:16:11.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/exceptions.py
--rw-rw-rw-   0        0        0      905 2023-04-04 12:42:13.000000 aio_dt_protocol-0.9.2/aio_dt_protocol/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-06 11:02:19.889003 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/
--rw-rw-rw-   0        0        0     5620 2023-04-06 11:02:19.000000 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1083 2023-04-06 11:02:19.000000 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 11:02:19.000000 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       19 2023-04-06 11:02:19.000000 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/requires.txt
--rw-rw-rw-   0        0        0       16 2023-04-06 11:02:19.000000 aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       91 2023-04-06 10:50:43.000000 aio_dt_protocol-0.9.2/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 11:02:19.944983 aio_dt_protocol-0.9.2/setup.cfg
--rw-rw-rw-   0        0        0     1503 2023-04-06 10:09:07.000000 aio_dt_protocol-0.9.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:37:13.760469 aio_dt_protocol-0.9.3/
+-rw-rw-rw-   0        0        0     1526 2023-04-05 18:37:56.000000 aio_dt_protocol-0.9.3/LICENSE
+-rw-rw-rw-   0        0        0     6559 2023-04-07 08:37:13.760934 aio_dt_protocol-0.9.3/PKG-INFO
+-rw-rw-rw-   0        0        0     5815 2023-04-06 13:39:16.000000 aio_dt_protocol-0.9.3/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 08:37:13.451966 aio_dt_protocol-0.9.3/aio_dt_protocol/
+-rw-rw-rw-   0        0        0    34959 2023-04-05 07:22:52.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/Actions.py
+-rw-rw-rw-   0        0        0    52666 2023-04-06 19:40:03.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/Browser.py
+-rw-rw-rw-   0        0        0     9971 2023-04-04 10:33:45.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/BrowserEx.py
+-rw-rw-rw-   0        0        0    35317 2023-04-05 07:22:52.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/DOMElement.py
+-rw-rw-rw-   0        0        0    32529 2023-04-05 17:29:55.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/Data.py
+-rw-rw-rw-   0        0        0    22749 2023-04-06 07:01:02.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/Page.py
+-rw-rw-rw-   0        0        0    16198 2023-04-06 13:11:03.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/PageEx.py
+-rw-rw-rw-   0        0        0      399 2023-04-07 08:27:54.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:37:13.759437 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/
+-rw-rw-rw-   0        0        0     3631 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/BackgroundService.py
+-rw-rw-rw-   0        0        0    13809 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Browser.py
+-rw-rw-rw-   0        0        0     7070 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/CSS.py
+-rw-rw-rw-   0        0        0     2045 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Console.py
+-rw-rw-rw-   0        0        0    16735 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/DOM.py
+-rw-rw-rw-   0        0        0     1846 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/DeviceOrientation.py
+-rw-rw-rw-   0        0        0    24645 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Emulation.py
+-rw-rw-rw-   0        0        0    23128 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Fetch.py
+-rw-rw-rw-   0        0        0     2066 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Log.py
+-rw-rw-rw-   0        0        0    22099 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Network.py
+-rw-rw-rw-   0        0        0     2124 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Overlay.py
+-rw-rw-rw-   0        0        0    35374 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Page.py
+-rw-rw-rw-   0        0        0    32897 2023-04-05 17:56:11.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Runtime.py
+-rw-rw-rw-   0        0        0     1712 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/SystemInfo.py
+-rw-rw-rw-   0        0        0    17569 2023-04-04 09:48:23.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Target.py
+-rw-rw-rw-   0        0        0        0 2021-06-02 19:57:07.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/domains/__init__.py
+-rw-rw-rw-   0        0        0     3148 2023-04-05 17:16:11.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/exceptions.py
+-rw-rw-rw-   0        0        0     1645 2023-04-06 13:08:53.000000 aio_dt_protocol-0.9.3/aio_dt_protocol/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:37:13.479895 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/
+-rw-rw-rw-   0        0        0     6559 2023-04-07 08:37:13.000000 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1083 2023-04-07 08:37:13.000000 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 08:37:13.000000 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       19 2023-04-07 08:37:13.000000 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       16 2023-04-07 08:37:13.000000 aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       91 2023-04-06 10:50:43.000000 aio_dt_protocol-0.9.3/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 08:37:13.761932 aio_dt_protocol-0.9.3/setup.cfg
+-rw-rw-rw-   0        0        0     1503 2023-04-06 10:09:07.000000 aio_dt_protocol-0.9.3/setup.py
```

### Comparing `aio_dt_protocol-0.9.2/LICENSE` & `aio_dt_protocol-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/PKG-INFO` & `aio_dt_protocol-0.9.3/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aio_dt_protocol
-Version: 0.9.2
+Version: 0.9.3
 Summary: Asynchronous wrapper over Chromium browser debugger protocol.
 Home-page: https://github.com/PieceOfGood/aio_dt_protocol
 Author: PieceOfGood
 Author-email: 78sanchezz@gmail.com
 License: BSD 3-Clause
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3.8
@@ -133,7 +133,36 @@
     #     (test_func, [ {"name": "test", "value": True} ]),
     #     # (any_awaitable1, [1, 2, 3])
     #     # (any_awaitable2, [])
     # )
 
     await page.Navigate(html)
 ```
+### Headless
+Чтобы запустить браузер в `безголовом` режиме, нужно передать аргументу принимающему путь к папке профиля пустую строку.
+```python
+import asyncio
+from aio_dt_protocol import BrowserEx as Browser
+from aio_dt_protocol.utils import save_img_as, async_util_call
+
+
+async def main() -> None:
+    print("[- HEADLESS RUN -]")
+    browser = Browser(profile_path="")
+    print("[- WAITING PAGE -]")
+    page = await browser.WaitFirstTab()
+    print("[- GO TO GOOGLE -]")
+    await page.Navigate("https://www.google.com")
+    
+    print("[- MAKE SCREENSHOT -]")
+    await async_util_call(
+        save_img_as, "google.png", await page.MakeScreenshot()
+    )
+    
+    print("[- CLOSE BROWSER -]")
+    await page.CloseBrowser()
+    print("[- DONE -]")
+
+if __name__ == '__main__':
+    asyncio.run(main())
+
+```
```

### Comparing `aio_dt_protocol-0.9.2/README.md` & `aio_dt_protocol-0.9.3/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -114,7 +114,36 @@
     #     (test_func, [ {"name": "test", "value": True} ]),
     #     # (any_awaitable1, [1, 2, 3])
     #     # (any_awaitable2, [])
     # )
 
     await page.Navigate(html)
 ```
+### Headless
+Чтобы запустить браузер в `безголовом` режиме, нужно передать аргументу принимающему путь к папке профиля пустую строку.
+```python
+import asyncio
+from aio_dt_protocol import BrowserEx as Browser
+from aio_dt_protocol.utils import save_img_as, async_util_call
+
+
+async def main() -> None:
+    print("[- HEADLESS RUN -]")
+    browser = Browser(profile_path="")
+    print("[- WAITING PAGE -]")
+    page = await browser.WaitFirstTab()
+    print("[- GO TO GOOGLE -]")
+    await page.Navigate("https://www.google.com")
+    
+    print("[- MAKE SCREENSHOT -]")
+    await async_util_call(
+        save_img_as, "google.png", await page.MakeScreenshot()
+    )
+    
+    print("[- CLOSE BROWSER -]")
+    await page.CloseBrowser()
+    print("[- DONE -]")
+
+if __name__ == '__main__':
+    asyncio.run(main())
+
+```
```

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/Actions.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/Actions.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/Browser.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/Browser.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 try:
     import ujson as json
+    HAS_UJSON = True
 except ModuleNotFoundError:
+    HAS_UJSON = False
     import json
-import asyncio
 import warnings
 import re, os, sys, signal, subprocess
 from urllib.parse import quote
 from os.path import expanduser
 from inspect import iscoroutinefunction
 from typing import List, Dict, Union, Optional, Tuple
 from collections.abc import Sequence
 from enum import Enum
 from .Page import Page
 from .Data import TargetConnectionInfo, TargetConnectionType, CommonCallback
 from .exceptions import FlagArgumentContainError
-from .utils import get_request, registry_read_key, log
+from .utils import get_request, registry_read_key, log, async_util_call
 
 
 class Browser:
 
     @staticmethod
     def FindInstances(for_port: Optional[int] = None, browser: str = "chrome") -> Dict[int, int]:
         """
@@ -45,41 +46,43 @@
                                 если ничего не найдено.
                                 { 9222: 16017, 9223: 2001, ... }
         """
         result = {}
         if sys.platform == "win32":
             if "chrome" in browser: browser = "chrome.exe"
             elif "brave" in browser: browser = "brave.exe"
-            elif "netbox" in browser: browser = "netboxbrowser.exe"
+            elif "edge" in browser: browser = "msedge.exe"
+            else: ValueError("Not support browser: " + browser)
             cmd = f"WMIC PROCESS WHERE NAME='{browser}' GET Commandline,Processid"
             for line in subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout:
                 if b"--type=renderer" not in line and b"--remote-debugging-port=" in line:
                     port, pid = re.findall(r"--remote-debugging-port=(\d+).*?(\d+)\s*$", line.decode())[0]
                     port, pid = int(port), int(pid)
                     if for_port == port: return {port: pid}
                     result[port] = pid
         elif sys.platform == "linux":
             if "chrome" in browser: browser = "google-chrome"
             elif "brave" in browser: browser = "brave"
-            else: ValueError("Not support browser " + browser)
+            elif "edge" in browser: browser = "edge"
+            else: ValueError("Not support browser: " + browser)
             try: itr = map(int, subprocess.check_output(["pidof", browser]).split())
             except subprocess.CalledProcessError: itr = []
             for pid in itr:
                 with open("/proc/" + str(pid) + "/cmdline") as f: cmd_line =  f.read()[:-1]
                 if "--type=renderer" not in cmd_line and "--remote-debugging-port=" in cmd_line:
                     port = int(re.findall(r"--remote-debugging-port=(\d+)", cmd_line)[0])
                     if for_port == port: return {port: pid}
                     result[port] = pid
         else: raise OSError(f"Platform '{sys.platform}' — not supported")
         return {} if for_port else result
 
     def __init__(
             self,
             profile_path: str = "testProfile",
-            dev_tool_profiles:      bool = False,
+            dev_tool_profiles:  bool = False,
             url: Optional[Union[str, bytes]] = None,
             flags:  Optional[List[str]] = None,
             browser_path: str = "",
             debug_port:   Union[str, int] = 9222,
             browser_pid:  int = 0,
             app:         bool = False,
             browser_exe:  str = "chrome",
@@ -90,27 +93,14 @@
             sizes:    Optional[Tuple[int, int]] = None,
             prevent_restore: bool = False,
 
     ) -> None:
         """
         Все параметры — не обязательны.
         ==============================================================================================
-        Refused Error: <urlopen error [Errno 111] Connection refused>
-        !!! ВНИМАНИЕ !!! — на Linux, после получения инстанса браузера, часто встречается
-            невозможность установить HTTP соединение для получения инстансов его страниц(табов/вкладок).
-            Связано это(возможно) с тем, что браузер ещё не успел инициализировать свои службы.
-            Преодолевается простым ожиданием, например:
-                while True:
-                    try:
-                        while (page := await browser.GetPage()) is None:
-                            await asyncio.sleep(.1)
-                        break
-                    except urllib.error.URLError as e:
-                        await asyncio.sleep(.5)
-        ==============================================================================================
 
         :param profile_path:    Путь до каталога, в который будет сохранена сессия профиля.
                                     Если не передан, или указано название папки, браузер
                                     сам создаст папку, по месту вызывающего кода. Если указан
                                     несуществующий путь, он будет создан.
 
                                         [-!!!-] ВАЖНО [-!!!-] - для запуска в режиме "headless",
@@ -162,14 +152,17 @@
                                     Не имеет смысла для Headless.
 
         :param prevent_restore: Предотвращать восстановление предыдущей сессии после крашей.
         """
         if sys.platform not in ("win32", "linux"): raise OSError(f"Platform '{sys.platform}' — not supported")
         self.dev_tool_profiles = dev_tool_profiles if profile_path else False
 
+        if verbose and not HAS_UJSON:
+            log("Call 'python -m pip install ujson' for install", lvl="[- UJSON IS NOT INSTALLED -]")
+
         if self.dev_tool_profiles:
             self.profile_path = os.path.join(expanduser("~"), "DevTools_Profiles", profile_path)
         elif profile_path != "":
             self.profile_path = os.path.abspath(profile_path)
         else:
             self.profile_path = ""
 
@@ -370,15 +363,17 @@
                     "id": "DAB7FB6187B554E10B0BD18821265734",
                     "title": "Yahoo",
                     "type": "page",
                     "url": "https://www.yahoo.com/",
                     "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/DAB7FB6187B554E10B0BD18821265734"
                 }, { ... } ]
         """
-        result = await self._Get(f"http://127.0.0.1:{self.debug_port}/json/list")
+        result = await async_util_call(
+            get_request, f"http://127.0.0.1:{self.debug_port}/json/list")
+
         if self.verbose: log("GetPageList() => " + result)
         return json.loads(result)
 
     async def GetPageBy(
             self, key: Union[str, int],
             value: Union[str, int],
             match_mode: str = "exact",
@@ -499,34 +494,29 @@
         :param index:       - Желаемый индекс страницы начиная с нуля.
         :param callback:    - Корутина, которой будет передаваться контекст абсолютно
                                 всех событий страницы в виде словаря.
         :return:        <Page>
         """
         return await self.GetPageBy("url", value, match_mode, index, callback)
 
-    @staticmethod
-    async def _Get(url: str) -> str:
-        return await asyncio.get_running_loop().run_in_executor(
-            None, get_request, url
-        )
-
 
 class FlagBuilder:
 
     def __init__(self):
         self._flags: set = set()
 
     def add(self, flag: "CMDFlag", *args: Union[str, int, float], separator: str = ",") -> None:
         """
         Принимает один флаг, его аргументы и разделитель аргументов.
         """
         f = flag.value
         if f[-1] == "=":
             if not args:
-                raise FlagArgumentContainError(f"Для флага {flag.name} ожидается аргумент, или список аргументов.")
+                raise FlagArgumentContainError(
+                    f"Для флага {flag.name} ожидается аргумент, или список аргументов.")
             for arg in args:
                 f += str(arg) + separator
             f = f[:-1]
         self._flags.add(f)
 
     def set(self, *flags: Sequence["CMDFlag", Sequence[Union[str, int, float]]], separator: str = ",") -> None:
         """
```

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/BrowserEx.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/BrowserEx.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/DOMElement.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/DOMElement.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/Data.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/Data.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/Page.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/Page.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/PageEx.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/PageEx.py`

 * *Files 1% similar despite different names*

```diff
@@ -205,15 +205,15 @@
             languages=result["languages"].split(","),
             state_province=result.get("stateProv"),
             proxy_type=(pt:=result.get("proxyType"))
         )
         del result["ll"]
         del result["accuracy"]
         del result["stateProv"]
-        if pt:
+        if pt is not None:
             del result["proxyType"]
         return GeoInfo(**result)
 
 
     async def CatchMetaForUrl(self, url: str, uniq_key: Optional[str] = None) -> None:
         """
         Получает заголовки запроса, ответа, а так же cookie для конкретного url и сохраняет их
```

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/BackgroundService.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/BackgroundService.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Browser.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Browser.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/CSS.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/CSS.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Console.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Console.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/DOM.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/DOM.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/DeviceOrientation.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/DeviceOrientation.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Emulation.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Emulation.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Fetch.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Fetch.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Log.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Log.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Network.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Network.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Overlay.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Overlay.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Page.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Page.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Runtime.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Runtime.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/SystemInfo.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/SystemInfo.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/domains/Target.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/domains/Target.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol/exceptions.py` & `aio_dt_protocol-0.9.3/aio_dt_protocol/exceptions.py`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/PKG-INFO` & `aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aio-dt-protocol
-Version: 0.9.2
+Version: 0.9.3
 Summary: Asynchronous wrapper over Chromium browser debugger protocol.
 Home-page: https://github.com/PieceOfGood/aio_dt_protocol
 Author: PieceOfGood
 Author-email: 78sanchezz@gmail.com
 License: BSD 3-Clause
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3.8
@@ -133,7 +133,36 @@
     #     (test_func, [ {"name": "test", "value": True} ]),
     #     # (any_awaitable1, [1, 2, 3])
     #     # (any_awaitable2, [])
     # )
 
     await page.Navigate(html)
 ```
+### Headless
+Чтобы запустить браузер в `безголовом` режиме, нужно передать аргументу принимающему путь к папке профиля пустую строку.
+```python
+import asyncio
+from aio_dt_protocol import BrowserEx as Browser
+from aio_dt_protocol.utils import save_img_as, async_util_call
+
+
+async def main() -> None:
+    print("[- HEADLESS RUN -]")
+    browser = Browser(profile_path="")
+    print("[- WAITING PAGE -]")
+    page = await browser.WaitFirstTab()
+    print("[- GO TO GOOGLE -]")
+    await page.Navigate("https://www.google.com")
+    
+    print("[- MAKE SCREENSHOT -]")
+    await async_util_call(
+        save_img_as, "google.png", await page.MakeScreenshot()
+    )
+    
+    print("[- CLOSE BROWSER -]")
+    await page.CloseBrowser()
+    print("[- DONE -]")
+
+if __name__ == '__main__':
+    asyncio.run(main())
+
+```
```

### Comparing `aio_dt_protocol-0.9.2/aio_dt_protocol.egg-info/SOURCES.txt` & `aio_dt_protocol-0.9.3/aio_dt_protocol.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aio_dt_protocol-0.9.2/setup.py` & `aio_dt_protocol-0.9.3/setup.py`

 * *Files identical despite different names*

