# Comparing `tmp/PyGB-0.9.53.tar.gz` & `tmp/PyGB-0.9.54.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PyGB-0.9.53.tar", last modified: Wed Apr  5 19:57:32 2023, max compression
+gzip compressed data, was "PyGB-0.9.54.tar", last modified: Fri Apr  7 02:58:20 2023, max compression
```

## Comparing `PyGB-0.9.53.tar` & `PyGB-0.9.54.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.370265 PyGB-0.9.53/
--rw-r--r--   0 hecmay     (501) staff       (20)     2808 2022-10-16 15:05:02.000000 PyGB-0.9.53/AUTHORS.txt
--rw-r--r--   0 hecmay     (501) staff       (20)     1477 2022-10-16 15:05:02.000000 PyGB-0.9.53/LICENSE.txt
--rw-r--r--   0 hecmay     (501) staff       (20)      208 2022-10-16 15:04:37.000000 PyGB-0.9.53/MANIFEST.in
--rw-r--r--   0 hecmay     (501) staff       (20)     2244 2023-04-05 19:57:32.369803 PyGB-0.9.53/PKG-INFO
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.340549 PyGB-0.9.53/PyGB.egg-info/
--rw-r--r--   0 hecmay     (501) staff       (20)     2244 2023-04-05 19:57:31.000000 PyGB-0.9.53/PyGB.egg-info/PKG-INFO
--rw-r--r--   0 hecmay     (501) staff       (20)      598 2023-04-05 19:57:32.000000 PyGB-0.9.53/PyGB.egg-info/SOURCES.txt
--rw-r--r--   0 hecmay     (501) staff       (20)        1 2023-04-05 19:57:31.000000 PyGB-0.9.53/PyGB.egg-info/dependency_links.txt
--rw-r--r--   0 hecmay     (501) staff       (20)      203 2023-04-05 19:57:31.000000 PyGB-0.9.53/PyGB.egg-info/requires.txt
--rw-r--r--   0 hecmay     (501) staff       (20)        5 2023-04-05 19:57:31.000000 PyGB-0.9.53/PyGB.egg-info/top_level.txt
--rw-r--r--   0 hecmay     (501) staff       (20)      930 2022-11-29 22:21:50.000000 PyGB-0.9.53/README.md
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.352367 PyGB-0.9.53/docs/
--rw-r--r--   0 hecmay     (501) staff       (20)     6754 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/Makefile
--rw-r--r--   0 hecmay     (501) staff       (20)     4807 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/conf.py
--rw-r--r--   0 hecmay     (501) staff       (20)     5711 2022-10-23 14:24:05.000000 PyGB-0.9.53/docs/index.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     1320 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/install.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     5435 2022-10-16 15:04:37.000000 PyGB-0.9.53/docs/keyboard.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     6455 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/make.bat
--rw-r--r--   0 hecmay     (501) staff       (20)    10216 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/mouse.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     5008 2022-10-23 14:24:06.000000 PyGB-0.9.53/docs/quickstart.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     2445 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/roadmap.rst
--rw-r--r--   0 hecmay     (501) staff       (20)     7620 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/screenshot.rst
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.354822 PyGB-0.9.53/docs/source/
--rw-r--r--   0 hecmay     (501) staff       (20)       54 2022-10-16 15:04:37.000000 PyGB-0.9.53/docs/source/modules.rst
--rw-r--r--   0 hecmay     (501) staff       (20)      297 2022-10-16 15:04:37.000000 PyGB-0.9.53/docs/source/pyautogui.rst
--rw-r--r--   0 hecmay     (501) staff       (20)      584 2022-10-16 15:05:02.000000 PyGB-0.9.53/docs/tests.rst
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.365568 PyGB-0.9.53/pygb/
--rw-r--r--   0 hecmay     (501) staff       (20)    71641 2022-11-07 21:00:31.000000 PyGB-0.9.53/pygb/__init__.py
--rw-r--r--   0 hecmay     (501) staff       (20)       57 2022-10-16 09:12:44.000000 PyGB-0.9.53/pygb/__main__.py
--rw-r--r--   0 hecmay     (501) staff       (20)        0 2022-10-16 09:12:44.000000 PyGB-0.9.53/pygb/_pygb_java.py
--rw-r--r--   0 hecmay     (501) staff       (20)    16734 2022-10-27 21:54:15.000000 PyGB-0.9.53/pygb/_pygb_osx.py
--rw-r--r--   0 hecmay     (501) staff       (20)    24511 2022-11-20 20:57:38.000000 PyGB-0.9.53/pygb/_pygb_screen.py
--rw-r--r--   0 hecmay     (501) staff       (20)    20321 2022-10-27 21:46:01.000000 PyGB-0.9.53/pygb/_pygb_win.py
--rw-r--r--   0 hecmay     (501) staff       (20)    15414 2022-10-16 15:04:37.000000 PyGB-0.9.53/pygb/_pygb_x11.py
--rw-r--r--   0 hecmay     (501) staff       (20)       38 2023-04-05 19:57:32.370410 PyGB-0.9.53/setup.cfg
--rw-r--r--   0 hecmay     (501) staff       (20)     2257 2023-03-10 22:48:53.000000 PyGB-0.9.53/setup.py
-drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-05 19:57:32.368822 PyGB-0.9.53/tests/
--rw-r--r--   0 hecmay     (501) staff       (20)    31903 2022-10-23 14:14:25.000000 PyGB-0.9.53/tests/test_pyautogui.py
--rw-r--r--   0 hecmay     (501) staff       (20)      427 2022-10-27 21:52:19.000000 PyGB-0.9.53/tests/test_pygb_macos.py
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.652561 PyGB-0.9.54/
+-rw-r--r--   0 hecmay     (501) staff       (20)     2808 2022-10-16 15:05:02.000000 PyGB-0.9.54/AUTHORS.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)     1477 2022-10-16 15:05:02.000000 PyGB-0.9.54/LICENSE.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)      208 2022-10-16 15:04:37.000000 PyGB-0.9.54/MANIFEST.in
+-rw-r--r--   0 hecmay     (501) staff       (20)     2442 2023-04-07 02:58:20.651661 PyGB-0.9.54/PKG-INFO
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.622855 PyGB-0.9.54/PyGB.egg-info/
+-rw-r--r--   0 hecmay     (501) staff       (20)     2442 2023-04-07 02:58:20.000000 PyGB-0.9.54/PyGB.egg-info/PKG-INFO
+-rw-r--r--   0 hecmay     (501) staff       (20)      598 2023-04-07 02:58:20.000000 PyGB-0.9.54/PyGB.egg-info/SOURCES.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)        1 2023-04-07 02:58:20.000000 PyGB-0.9.54/PyGB.egg-info/dependency_links.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)      203 2023-04-07 02:58:20.000000 PyGB-0.9.54/PyGB.egg-info/requires.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)        5 2023-04-07 02:58:20.000000 PyGB-0.9.54/PyGB.egg-info/top_level.txt
+-rw-r--r--   0 hecmay     (501) staff       (20)     1128 2023-04-06 03:38:58.000000 PyGB-0.9.54/README.md
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.636424 PyGB-0.9.54/docs/
+-rw-r--r--   0 hecmay     (501) staff       (20)     6754 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/Makefile
+-rw-r--r--   0 hecmay     (501) staff       (20)     4807 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/conf.py
+-rw-r--r--   0 hecmay     (501) staff       (20)     5711 2022-10-23 14:24:05.000000 PyGB-0.9.54/docs/index.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     1320 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/install.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     5435 2022-10-16 15:04:37.000000 PyGB-0.9.54/docs/keyboard.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     6455 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/make.bat
+-rw-r--r--   0 hecmay     (501) staff       (20)    10216 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/mouse.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     5008 2022-10-23 14:24:06.000000 PyGB-0.9.54/docs/quickstart.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     2445 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/roadmap.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)     7620 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/screenshot.rst
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.638607 PyGB-0.9.54/docs/source/
+-rw-r--r--   0 hecmay     (501) staff       (20)       54 2022-10-16 15:04:37.000000 PyGB-0.9.54/docs/source/modules.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)      297 2022-10-16 15:04:37.000000 PyGB-0.9.54/docs/source/pyautogui.rst
+-rw-r--r--   0 hecmay     (501) staff       (20)      584 2022-10-16 15:05:02.000000 PyGB-0.9.54/docs/tests.rst
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.646944 PyGB-0.9.54/pygb/
+-rw-r--r--   0 hecmay     (501) staff       (20)    70010 2023-04-07 02:55:29.000000 PyGB-0.9.54/pygb/__init__.py
+-rw-r--r--   0 hecmay     (501) staff       (20)       57 2022-10-16 09:12:44.000000 PyGB-0.9.54/pygb/__main__.py
+-rw-r--r--   0 hecmay     (501) staff       (20)        0 2022-10-16 09:12:44.000000 PyGB-0.9.54/pygb/_pygb_java.py
+-rw-r--r--   0 hecmay     (501) staff       (20)    18642 2023-04-07 02:51:34.000000 PyGB-0.9.54/pygb/_pygb_osx.py
+-rw-r--r--   0 hecmay     (501) staff       (20)    25357 2023-04-07 01:04:36.000000 PyGB-0.9.54/pygb/_pygb_screen.py
+-rw-r--r--   0 hecmay     (501) staff       (20)    20280 2023-04-07 02:54:41.000000 PyGB-0.9.54/pygb/_pygb_win.py
+-rw-r--r--   0 hecmay     (501) staff       (20)    15414 2022-10-16 15:04:37.000000 PyGB-0.9.54/pygb/_pygb_x11.py
+-rw-r--r--   0 hecmay     (501) staff       (20)       38 2023-04-07 02:58:20.652993 PyGB-0.9.54/setup.cfg
+-rw-r--r--   0 hecmay     (501) staff       (20)     2257 2023-04-07 02:52:44.000000 PyGB-0.9.54/setup.py
+drwxr-xr-x   0 hecmay     (501) staff       (20)        0 2023-04-07 02:58:20.649899 PyGB-0.9.54/tests/
+-rw-r--r--   0 hecmay     (501) staff       (20)    31903 2022-10-23 14:14:25.000000 PyGB-0.9.54/tests/test_pyautogui.py
+-rw-r--r--   0 hecmay     (501) staff       (20)      427 2022-10-27 21:52:19.000000 PyGB-0.9.54/tests/test_pygb_macos.py
```

### Comparing `PyGB-0.9.53/AUTHORS.txt` & `PyGB-0.9.54/AUTHORS.txt`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/LICENSE.txt` & `PyGB-0.9.54/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/PKG-INFO` & `PyGB-0.9.54/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyGB
-Version: 0.9.53
+Version: 0.9.54
 Summary: PyGB lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.
 Home-page: https://github.com/danalites/pygb
 Author: Al Sweigart, and other contributors
 Author-email: al@inventwithpython.com
 License: BSD
 Keywords: gui automation test testing keyboard mouse cursor click press keystroke control
 Classifier: Development Status :: 4 - Beta
@@ -45,18 +45,18 @@
 pygb.keyDown('a', window=859)
 pygb.keyUp('a', window=859)
 
 # Take screenshot of a specific window
 img = pygb.screenshot('a', window=859)
 ```
 
-### Other Changes
-- Window support
+## Window APIs
 
-
-```python
-
-
-```
+### `pygb.getWindows()` 
+- returns a list of windows with their title
 
 ### Window resizing 
-- `pygb.resize(window, width, height)` - resize a window to a specific size: https://stackoverflow.com/questions/70535283/how-can-i-resize-terminal-window-from-python
+- `win.resize(width, height)` - resize a window to a specific size: https://stackoverflow.com/questions/70535283/how-can-i-resize-terminal-window-from-python
+
+### References
+- [cocoa-vanilla](https://github.com/robotools/vanilla): a Python library for building Cocoa GUIs on macOS
+- [ahk-python](https://github.com/spyoungtech/ahk)
```

### Comparing `PyGB-0.9.53/PyGB.egg-info/PKG-INFO` & `PyGB-0.9.54/PyGB.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyGB
-Version: 0.9.53
+Version: 0.9.54
 Summary: PyGB lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.
 Home-page: https://github.com/danalites/pygb
 Author: Al Sweigart, and other contributors
 Author-email: al@inventwithpython.com
 License: BSD
 Keywords: gui automation test testing keyboard mouse cursor click press keystroke control
 Classifier: Development Status :: 4 - Beta
@@ -45,18 +45,18 @@
 pygb.keyDown('a', window=859)
 pygb.keyUp('a', window=859)
 
 # Take screenshot of a specific window
 img = pygb.screenshot('a', window=859)
 ```
 
-### Other Changes
-- Window support
+## Window APIs
 
-
-```python
-
-
-```
+### `pygb.getWindows()` 
+- returns a list of windows with their title
 
 ### Window resizing 
-- `pygb.resize(window, width, height)` - resize a window to a specific size: https://stackoverflow.com/questions/70535283/how-can-i-resize-terminal-window-from-python
+- `win.resize(width, height)` - resize a window to a specific size: https://stackoverflow.com/questions/70535283/how-can-i-resize-terminal-window-from-python
+
+### References
+- [cocoa-vanilla](https://github.com/robotools/vanilla): a Python library for building Cocoa GUIs on macOS
+- [ahk-python](https://github.com/spyoungtech/ahk)
```

### Comparing `PyGB-0.9.53/PyGB.egg-info/SOURCES.txt` & `PyGB-0.9.54/PyGB.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/Makefile` & `PyGB-0.9.54/docs/Makefile`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/conf.py` & `PyGB-0.9.54/docs/conf.py`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/index.rst` & `PyGB-0.9.54/docs/index.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/install.rst` & `PyGB-0.9.54/docs/install.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/keyboard.rst` & `PyGB-0.9.54/docs/keyboard.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/make.bat` & `PyGB-0.9.54/docs/make.bat`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/mouse.rst` & `PyGB-0.9.54/docs/mouse.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/quickstart.rst` & `PyGB-0.9.54/docs/quickstart.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/roadmap.rst` & `PyGB-0.9.54/docs/roadmap.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/screenshot.rst` & `PyGB-0.9.54/docs/screenshot.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/docs/tests.rst` & `PyGB-0.9.54/docs/tests.rst`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/pygb/__init__.py` & `PyGB-0.9.54/pygb/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 # PyGB lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux,
 # on Python 3 and 2.
-# https://github.com/asweigart/pygb
-# Al Sweigart al@inventwithpython.com (Send me feedback & suggestions!)
+# https://github.com/danalite/pygb
 
 
 # TODO - the following features are half-implemented right now:
 # snapshot logging
 # non-qwerty keyboard mapping
 # primary secondary mouse button awareness
 
 
 from __future__ import absolute_import, division, print_function
 
 
-__version__ = "0.9.53"
+__version__ = "0.9.54"
 
 import sys
 import time
 import datetime
 import os
 import platform
 import re
@@ -75,15 +74,14 @@
 locateAllOnScreen = pyscreen.locateAllOnScreen
 locateCenterOnScreen = pyscreen.locateCenterOnScreen
 locateOnScreen = pyscreen.locateOnScreen
 locateOnWindow = pyscreen.locateOnWindow
 pixel = pyscreen.pixel
 pixelMatchesColor = pyscreen.pixelMatchesColor
 screenshot = pyscreen.screenshot
-# showRegionOnScreen = pyscreen.showRegionOnScreen
 
 
 try:
     import mouseinfo
 
     def mouseInfo():
         """
@@ -330,27 +328,14 @@
 # Different keyboard mappings:
 # TODO - finish this feature.
 # NOTE: Eventually, I'd like to come up with a better system than this. For now, this seems like it works.
 QWERTY = r"""`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"""
 QWERTZ = r"""=1234567890/0qwertzuiop89-asdfghjkl,\yxcvbnm,.7+!@#$%^&*()?)QWERTZUIOP*(_ASDFGHJKL<|YXCVBNM<>&"""
 
 
-class WindowInstance:
-    def __init__(self, pid: int = 0, windowID : int = 0, position: tuple = (0, 0),
-                 dimX: int = 0, dimY: int = 0, app: str = "", title: str = ""):
-        self.pid = pid
-        self.windowID = windowID
-        self.lt = position
-        self.wh = (dimX, dimY)
-        self.owner = app
-        self.title = title
-    
-    def __repr__(self):
-        return f"WindowInstance(pid={self.pid}, WID={self.windowID}, lt={self.lt}, wh={self.wh}, owner={self.owner}, title={self.title})"
-
 
 def isShiftCharacter(character):
     """
     Returns True if the ``character`` is a keyboard key that would require the shift key to be held down, such as
     uppercase letters or the symbols on the keyboard's number row.
     """
     # NOTE TODO - This will be different for non-qwerty keyboards.
@@ -691,20 +676,26 @@
                 return LEFT
             elif button == SECONDARY:
                 return RIGHT
 
     # Return a mouse button integer value, not a string like 'left':
     return {LEFT: LEFT, MIDDLE: MIDDLE, RIGHT: RIGHT, 1: LEFT, 2: MIDDLE, 3: RIGHT, 4: 4, 5: 5, 6: 6, 7: 7}[button]
 
+def moveWindow(windowName, x, y):
+    platformModule._moveWindow(windowName, x, y)
+
 def activateWindow(windowName):
     platformModule._activateWindow(windowName)
 
 def getActiveWindow():
     return platformModule._getActiveWindow()
 
+def getOpenedWindows():
+    return platformModule._getOpenedWindows()
+
 @_genericPyGBChecks
 def mouseDown(x=None, y=None, button=PRIMARY, duration=0.0, tween=linear, logScreenshot=None, _pause=True):
     """Performs pressing a mouse button down (but not up).
 
     The x and y parameters detail where the mouse event happens. If None, the
     current mouse position is used. If a float value, it is rounded down. If
     outside the boundaries of the screen, the event happens at edge of the
@@ -1588,51 +1579,18 @@
                 time.sleep(1)
             sys.stdout.flush()
     except KeyboardInterrupt:
         sys.stdout.write("\n")
         sys.stdout.flush()
 
 
-def _snapshot(tag, folder=None, region=None, radius=None):
-    # TODO feature not finished
-    if region is not None and radius is not None:
-        raise Exception("Either region or radius arguments (or neither) can be passed to snapshot, but not both")
-
-    if radius is not None:
-        x, y = platformModule._position()
-
-    if folder is None:
-        folder = os.getcwd()
-
-    now = datetime.datetime.now()
-    filename = "%s-%s-%s_%s-%s-%s-%s_%s.png" % (
-        now.year,
-        str(now.month).rjust(2, "0"),
-        str(now.day).rjust(2, "0"),
-        now.hour,
-        now.minute,
-        now.second,
-        str(now.microsecond)[:3],
-        tag,
-    )
-    filepath = os.path.join(folder, filename)
-    screenshot(filepath)
-
-
 def sleep(seconds):
     time.sleep(seconds)
 
 
-def countdown(seconds):
-    for i in range(seconds, 0, -1):
-        print(str(i), end=" ", flush=True)
-        time.sleep(1)
-    print()
-
-
 def _getNumberToken(commandStr):
     """Gets the number token at the start of commandStr.
 
     Given '5hello' returns '5'
     Given '  5hello' returns '  5'
     Given '-42hello' returns '-42'
     Given '+42hello' returns '+42'
@@ -1955,27 +1913,14 @@
 
     # Carry out each command.
     originalPAUSE = PAUSE
     _runCommandList(commandList, _ssCount)
     PAUSE = originalPAUSE
 
 
-def printInfo(dontPrint=False):
-    msg = '''
-         Platform: {}
-   Python Version: {}
-PyGB Version: {}
-       Executable: {}
-       Resolution: {}
-        Timestamp: {}'''.format(*getInfo())
-    if not dontPrint:
-        print(msg)
-    return msg
-
-
 def getInfo():
-    return (sys.platform, sys.version, __version__, sys.executable, size(), datetime.datetime.now())
+    return (sys.platform, __version__, sys.executable, size(), datetime.datetime.now())
 
 
 # Add the bottom left, top right, and bottom right corners to FAILSAFE_POINTS.
 _right, _bottom = size()
 FAILSAFE_POINTS.extend([(0, _bottom - 1), (_right - 1, 0), (_right - 1, _bottom - 1)])
```

### Comparing `PyGB-0.9.53/pygb/_pygb_osx.py` & `PyGB-0.9.54/pygb/_pygb_osx.py`

 * *Files 19% similar despite different names*

```diff
@@ -12,165 +12,165 @@
         kCGNullWindowID
     )
 except:
     assert False, "You must first install pyobjc-core and pyobjc: https://pygb.readthedocs.io/en/latest/install.html"
 import AppKit
 
 import pygb
-from pygb import LEFT, MIDDLE, RIGHT, WindowInstance
-
-if sys.platform !=  'darwin':
-    raise Exception('The pygb_osx module should only be loaded on an OS X system.')
+from pygb import LEFT, MIDDLE, RIGHT
 
+if sys.platform != 'darwin':
+    raise Exception(
+        'The pygb_osx module should only be loaded on an OS X system.')
 
 
 """ Taken from events.h
 /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h
 
 The *KB dictionaries in pygb map a string that can be passed to keyDown(),
 keyUp(), or press() into the code used for the OS-specific keyboard function.
 
 They should always be lowercase, and the same keys should be used across all OSes."""
 keyboardMapping = dict([(key, None) for key in pygb.KEY_NAMES])
 keyboardMapping.update({
-    'a': 0x00, # kVK_ANSI_A
-    's': 0x01, # kVK_ANSI_S
-    'd': 0x02, # kVK_ANSI_D
-    'f': 0x03, # kVK_ANSI_F
-    'h': 0x04, # kVK_ANSI_H
-    'g': 0x05, # kVK_ANSI_G
-    'z': 0x06, # kVK_ANSI_Z
-    'x': 0x07, # kVK_ANSI_X
-    'c': 0x08, # kVK_ANSI_C
-    'v': 0x09, # kVK_ANSI_V
-    'b': 0x0b, # kVK_ANSI_B
-    'q': 0x0c, # kVK_ANSI_Q
-    'w': 0x0d, # kVK_ANSI_W
-    'e': 0x0e, # kVK_ANSI_E
-    'r': 0x0f, # kVK_ANSI_R
-    'y': 0x10, # kVK_ANSI_Y
-    't': 0x11, # kVK_ANSI_T
-    '1': 0x12, # kVK_ANSI_1
-    '!': 0x12, # kVK_ANSI_1
-    '2': 0x13, # kVK_ANSI_2
-    '@': 0x13, # kVK_ANSI_2
-    '3': 0x14, # kVK_ANSI_3
-    '#': 0x14, # kVK_ANSI_3
-    '4': 0x15, # kVK_ANSI_4
-    '$': 0x15, # kVK_ANSI_4
-    '6': 0x16, # kVK_ANSI_6
-    '^': 0x16, # kVK_ANSI_6
-    '5': 0x17, # kVK_ANSI_5
-    '%': 0x17, # kVK_ANSI_5
-    '=': 0x18, # kVK_ANSI_Equal
-    '+': 0x18, # kVK_ANSI_Equal
-    '9': 0x19, # kVK_ANSI_9
-    '(': 0x19, # kVK_ANSI_9
-    '7': 0x1a, # kVK_ANSI_7
-    '&': 0x1a, # kVK_ANSI_7
-    '-': 0x1b, # kVK_ANSI_Minus
-    '_': 0x1b, # kVK_ANSI_Minus
-    '8': 0x1c, # kVK_ANSI_8
-    '*': 0x1c, # kVK_ANSI_8
-    '0': 0x1d, # kVK_ANSI_0
-    ')': 0x1d, # kVK_ANSI_0
-    ']': 0x1e, # kVK_ANSI_RightBracket
-    '}': 0x1e, # kVK_ANSI_RightBracket
-    'o': 0x1f, # kVK_ANSI_O
-    'u': 0x20, # kVK_ANSI_U
-    '[': 0x21, # kVK_ANSI_LeftBracket
-    '{': 0x21, # kVK_ANSI_LeftBracket
-    'i': 0x22, # kVK_ANSI_I
-    'p': 0x23, # kVK_ANSI_P
-    'l': 0x25, # kVK_ANSI_L
-    'j': 0x26, # kVK_ANSI_J
-    "'": 0x27, # kVK_ANSI_Quote
-    '"': 0x27, # kVK_ANSI_Quote
-    'k': 0x28, # kVK_ANSI_K
-    ';': 0x29, # kVK_ANSI_Semicolon
-    ':': 0x29, # kVK_ANSI_Semicolon
-    '\\': 0x2a, # kVK_ANSI_Backslash
-    '|': 0x2a, # kVK_ANSI_Backslash
-    ',': 0x2b, # kVK_ANSI_Comma
-    '<': 0x2b, # kVK_ANSI_Comma
-    '/': 0x2c, # kVK_ANSI_Slash
-    '?': 0x2c, # kVK_ANSI_Slash
-    'n': 0x2d, # kVK_ANSI_N
-    'm': 0x2e, # kVK_ANSI_M
-    '.': 0x2f, # kVK_ANSI_Period
-    '>': 0x2f, # kVK_ANSI_Period
-    '`': 0x32, # kVK_ANSI_Grave
-    '~': 0x32, # kVK_ANSI_Grave
-    ' ': 0x31, # kVK_Space
+    'a': 0x00,  # kVK_ANSI_A
+    's': 0x01,  # kVK_ANSI_S
+    'd': 0x02,  # kVK_ANSI_D
+    'f': 0x03,  # kVK_ANSI_F
+    'h': 0x04,  # kVK_ANSI_H
+    'g': 0x05,  # kVK_ANSI_G
+    'z': 0x06,  # kVK_ANSI_Z
+    'x': 0x07,  # kVK_ANSI_X
+    'c': 0x08,  # kVK_ANSI_C
+    'v': 0x09,  # kVK_ANSI_V
+    'b': 0x0b,  # kVK_ANSI_B
+    'q': 0x0c,  # kVK_ANSI_Q
+    'w': 0x0d,  # kVK_ANSI_W
+    'e': 0x0e,  # kVK_ANSI_E
+    'r': 0x0f,  # kVK_ANSI_R
+    'y': 0x10,  # kVK_ANSI_Y
+    't': 0x11,  # kVK_ANSI_T
+    '1': 0x12,  # kVK_ANSI_1
+    '!': 0x12,  # kVK_ANSI_1
+    '2': 0x13,  # kVK_ANSI_2
+    '@': 0x13,  # kVK_ANSI_2
+    '3': 0x14,  # kVK_ANSI_3
+    '#': 0x14,  # kVK_ANSI_3
+    '4': 0x15,  # kVK_ANSI_4
+    '$': 0x15,  # kVK_ANSI_4
+    '6': 0x16,  # kVK_ANSI_6
+    '^': 0x16,  # kVK_ANSI_6
+    '5': 0x17,  # kVK_ANSI_5
+    '%': 0x17,  # kVK_ANSI_5
+    '=': 0x18,  # kVK_ANSI_Equal
+    '+': 0x18,  # kVK_ANSI_Equal
+    '9': 0x19,  # kVK_ANSI_9
+    '(': 0x19,  # kVK_ANSI_9
+    '7': 0x1a,  # kVK_ANSI_7
+    '&': 0x1a,  # kVK_ANSI_7
+    '-': 0x1b,  # kVK_ANSI_Minus
+    '_': 0x1b,  # kVK_ANSI_Minus
+    '8': 0x1c,  # kVK_ANSI_8
+    '*': 0x1c,  # kVK_ANSI_8
+    '0': 0x1d,  # kVK_ANSI_0
+    ')': 0x1d,  # kVK_ANSI_0
+    ']': 0x1e,  # kVK_ANSI_RightBracket
+    '}': 0x1e,  # kVK_ANSI_RightBracket
+    'o': 0x1f,  # kVK_ANSI_O
+    'u': 0x20,  # kVK_ANSI_U
+    '[': 0x21,  # kVK_ANSI_LeftBracket
+    '{': 0x21,  # kVK_ANSI_LeftBracket
+    'i': 0x22,  # kVK_ANSI_I
+    'p': 0x23,  # kVK_ANSI_P
+    'l': 0x25,  # kVK_ANSI_L
+    'j': 0x26,  # kVK_ANSI_J
+    "'": 0x27,  # kVK_ANSI_Quote
+    '"': 0x27,  # kVK_ANSI_Quote
+    'k': 0x28,  # kVK_ANSI_K
+    ';': 0x29,  # kVK_ANSI_Semicolon
+    ':': 0x29,  # kVK_ANSI_Semicolon
+    '\\': 0x2a,  # kVK_ANSI_Backslash
+    '|': 0x2a,  # kVK_ANSI_Backslash
+    ',': 0x2b,  # kVK_ANSI_Comma
+    '<': 0x2b,  # kVK_ANSI_Comma
+    '/': 0x2c,  # kVK_ANSI_Slash
+    '?': 0x2c,  # kVK_ANSI_Slash
+    'n': 0x2d,  # kVK_ANSI_N
+    'm': 0x2e,  # kVK_ANSI_M
+    '.': 0x2f,  # kVK_ANSI_Period
+    '>': 0x2f,  # kVK_ANSI_Period
+    '`': 0x32,  # kVK_ANSI_Grave
+    '~': 0x32,  # kVK_ANSI_Grave
+    ' ': 0x31,  # kVK_Space
     'space': 0x31,
-    '\r': 0x24, # kVK_Return
-    '\n': 0x24, # kVK_Return
-    'enter': 0x24, # kVK_Return
-    'return': 0x24, # kVK_Return
-    '\t': 0x30, # kVK_Tab
-    'tab': 0x30, # kVK_Tab
-    'backspace': 0x33, # kVK_Delete, which is "Backspace" on OS X.
-    '\b': 0x33, # kVK_Delete, which is "Backspace" on OS X.
-    'esc': 0x35, # kVK_Escape
-    'escape': 0x35, # kVK_Escape
-    'command': 0x37, # kVK_Command
-    'shift': 0x38, # kVK_Shift
-    'shiftleft': 0x38, # kVK_Shift
-    'capslock': 0x39, # kVK_CapsLock
-    'option': 0x3a, # kVK_Option
-    'optionleft': 0x3a, # kVK_Option
-    'alt': 0x3a, # kVK_Option
-    'altleft': 0x3a, # kVK_Option
-    'ctrl': 0x3b, # kVK_Control
-    'ctrlleft': 0x3b, # kVK_Control
-    'shiftright': 0x3c, # kVK_RightShift
-    'optionright': 0x3d, # kVK_RightOption
-    'ctrlright': 0x3e, # kVK_RightControl
-    'fn': 0x3f, # kVK_Function
-    'f17': 0x40, # kVK_F17
-    'volumeup': 0x48, # kVK_VolumeUp
-    'volumedown': 0x49, # kVK_VolumeDown
-    'volumemute': 0x4a, # kVK_Mute
-    'f18': 0x4f, # kVK_F18
-    'f19': 0x50, # kVK_F19
-    'f20': 0x5a, # kVK_F20
-    'f5': 0x60, # kVK_F5
-    'f6': 0x61, # kVK_F6
-    'f7': 0x62, # kVK_F7
-    'f3': 0x63, # kVK_F3
-    'f8': 0x64, # kVK_F8
-    'f9': 0x65, # kVK_F9
-    'f11': 0x67, # kVK_F11
-    'f13': 0x69, # kVK_F13
-    'f16': 0x6a, # kVK_F16
-    'f14': 0x6b, # kVK_F14
-    'f10': 0x6d, # kVK_F10
-    'f12': 0x6f, # kVK_F12
-    'f15': 0x71, # kVK_F15
-    'help': 0x72, # kVK_Help
-    'home': 0x73, # kVK_Home
-    'pageup': 0x74, # kVK_PageUp
-    'pgup': 0x74, # kVK_PageUp
-    'del': 0x75, # kVK_ForwardDelete
-    'delete': 0x75, # kVK_ForwardDelete
-    'f4': 0x76, # kVK_F4
-    'end': 0x77, # kVK_End
-    'f2': 0x78, # kVK_F2
-    'pagedown': 0x79, # kVK_PageDown
-    'pgdn': 0x79, # kVK_PageDown
-    'f1': 0x7a, # kVK_F1
-    'left': 0x7b, # kVK_LeftArrow
-    'right': 0x7c, # kVK_RightArrow
-    'down': 0x7d, # kVK_DownArrow
-    'up': 0x7e, # kVK_UpArrow
-    'yen': 0x5d, # kVK_JIS_Yen
-    #'underscore' : 0x5e, # kVK_JIS_Underscore (only applies to Japanese keyboards)
-    #'comma': 0x5f, # kVK_JIS_KeypadComma (only applies to Japanese keyboards)
-    'eisu': 0x66, # kVK_JIS_Eisu
-    'kana': 0x68, # kVK_JIS_Kana
+    '\r': 0x24,  # kVK_Return
+    '\n': 0x24,  # kVK_Return
+    'enter': 0x24,  # kVK_Return
+    'return': 0x24,  # kVK_Return
+    '\t': 0x30,  # kVK_Tab
+    'tab': 0x30,  # kVK_Tab
+    'backspace': 0x33,  # kVK_Delete, which is "Backspace" on OS X.
+    '\b': 0x33,  # kVK_Delete, which is "Backspace" on OS X.
+    'esc': 0x35,  # kVK_Escape
+    'escape': 0x35,  # kVK_Escape
+    'command': 0x37,  # kVK_Command
+    'shift': 0x38,  # kVK_Shift
+    'shiftleft': 0x38,  # kVK_Shift
+    'capslock': 0x39,  # kVK_CapsLock
+    'option': 0x3a,  # kVK_Option
+    'optionleft': 0x3a,  # kVK_Option
+    'alt': 0x3a,  # kVK_Option
+    'altleft': 0x3a,  # kVK_Option
+    'ctrl': 0x3b,  # kVK_Control
+    'ctrlleft': 0x3b,  # kVK_Control
+    'shiftright': 0x3c,  # kVK_RightShift
+    'optionright': 0x3d,  # kVK_RightOption
+    'ctrlright': 0x3e,  # kVK_RightControl
+    'fn': 0x3f,  # kVK_Function
+    'f17': 0x40,  # kVK_F17
+    'volumeup': 0x48,  # kVK_VolumeUp
+    'volumedown': 0x49,  # kVK_VolumeDown
+    'volumemute': 0x4a,  # kVK_Mute
+    'f18': 0x4f,  # kVK_F18
+    'f19': 0x50,  # kVK_F19
+    'f20': 0x5a,  # kVK_F20
+    'f5': 0x60,  # kVK_F5
+    'f6': 0x61,  # kVK_F6
+    'f7': 0x62,  # kVK_F7
+    'f3': 0x63,  # kVK_F3
+    'f8': 0x64,  # kVK_F8
+    'f9': 0x65,  # kVK_F9
+    'f11': 0x67,  # kVK_F11
+    'f13': 0x69,  # kVK_F13
+    'f16': 0x6a,  # kVK_F16
+    'f14': 0x6b,  # kVK_F14
+    'f10': 0x6d,  # kVK_F10
+    'f12': 0x6f,  # kVK_F12
+    'f15': 0x71,  # kVK_F15
+    'help': 0x72,  # kVK_Help
+    'home': 0x73,  # kVK_Home
+    'pageup': 0x74,  # kVK_PageUp
+    'pgup': 0x74,  # kVK_PageUp
+    'del': 0x75,  # kVK_ForwardDelete
+    'delete': 0x75,  # kVK_ForwardDelete
+    'f4': 0x76,  # kVK_F4
+    'end': 0x77,  # kVK_End
+    'f2': 0x78,  # kVK_F2
+    'pagedown': 0x79,  # kVK_PageDown
+    'pgdn': 0x79,  # kVK_PageDown
+    'f1': 0x7a,  # kVK_F1
+    'left': 0x7b,  # kVK_LeftArrow
+    'right': 0x7c,  # kVK_RightArrow
+    'down': 0x7d,  # kVK_DownArrow
+    'up': 0x7e,  # kVK_UpArrow
+    'yen': 0x5d,  # kVK_JIS_Yen
+    # 'underscore' : 0x5e, # kVK_JIS_Underscore (only applies to Japanese keyboards)
+    # 'comma': 0x5f, # kVK_JIS_KeypadComma (only applies to Japanese keyboards)
+    'eisu': 0x66,  # kVK_JIS_Eisu
+    'kana': 0x68,  # kVK_JIS_Kana
 })
 
 """
 # TODO - additional key codes to add
   kVK_ANSI_KeypadDecimal        = 0x41,
   kVK_ANSI_KeypadMultiply       = 0x43,
   kVK_ANSI_KeypadPlus           = 0x45,
@@ -220,23 +220,25 @@
     'KEYTYPE_FAST': 19,
     'KEYTYPE_REWIND': 20,
     'KEYTYPE_ILLUMINATION_UP': 21,
     'KEYTYPE_ILLUMINATION_DOWN': 22,
     'KEYTYPE_ILLUMINATION_TOGGLE': 23
 }
 
+
 def _keyDown(key, window=None):
     if key not in keyboardMapping or keyboardMapping[key] is None:
         return
 
     if key in special_key_translate_table:
         _specialKeyEvent(key, 'down', window)
     else:
         _normalKeyEvent(key, 'down', window)
 
+
 def _keyUp(key, window=None):
     if key not in keyboardMapping or keyboardMapping[key] is None:
         return
 
     if key in special_key_translate_table:
         _specialKeyEvent(key, 'up', window)
     else:
@@ -247,176 +249,191 @@
     assert upDown in ('up', 'down'), "upDown argument must be 'up' or 'down'"
 
     try:
         if pygb.isShiftCharacter(key):
             key_code = keyboardMapping[key.lower()]
 
             event = Quartz.CGEventCreateKeyboardEvent(None,
-                        keyboardMapping['shift'], upDown == 'down')
+                                                      keyboardMapping['shift'], upDown == 'down')
             if window:
                 Quartz.CGEventPostToPid(window, event)
             else:
                 Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
 
             # Tiny sleep to let OS X catch up on us pressing shift
             time.sleep(pygb.DARWIN_CATCH_UP_TIME)
 
         else:
             key_code = keyboardMapping[key]
 
-        event = Quartz.CGEventCreateKeyboardEvent(None, key_code, upDown == 'down')
+        event = Quartz.CGEventCreateKeyboardEvent(
+            None, key_code, upDown == 'down')
         if window:
             Quartz.CGEventPostToPid(window, event)
         else:
             Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
 
         time.sleep(pygb.DARWIN_CATCH_UP_TIME)
 
     # TODO - wait, is the shift key's keyup not done?
     # TODO - get rid of this try-except.
 
     except KeyError:
         raise RuntimeError("Key %s not implemented." % (key))
 
+
 def _specialKeyEvent(key, upDown):
     """ Helper method for special keys.
 
     Source: http://stackoverflow.com/questions/11045814/emulate-media-key-press-on-mac
     """
     assert upDown in ('up', 'down'), "upDown argument must be 'up' or 'down'"
 
     key_code = special_key_translate_table[key]
 
     ev = AppKit.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
-            Quartz.NSSystemDefined, # type
-            (0,0), # location
-            0xa00 if upDown == 'down' else 0xb00, # flags
-            0, # timestamp
-            0, # window
-            0, # ctx
-            8, # subtype
-            (key_code << 16) | ((0xa if upDown == 'down' else 0xb) << 8), # data1
-            -1 # data2
-        )
+        Quartz.NSSystemDefined,  # type
+        (0, 0),  # location
+        0xa00 if upDown == 'down' else 0xb00,  # flags
+        0,  # timestamp
+        0,  # window
+        0,  # ctx
+        8,  # subtype
+            (key_code << 16) | ((0xa if upDown == 'down' else 0xb) << 8),  # data1
+        -1  # data2
+    )
 
     Quartz.CGEventPost(0, ev.CGEvent())
 
 
 def _position():
     loc = AppKit.NSEvent.mouseLocation()
     return int(loc.x), int(Quartz.CGDisplayPixelsHigh(0) - loc.y)
 
 
 def _size():
     return Quartz.CGDisplayPixelsWide(Quartz.CGMainDisplayID()), Quartz.CGDisplayPixelsHigh(Quartz.CGMainDisplayID())
 
 
-
 def _scroll(clicks, x=None, y=None):
     _vscroll(clicks, x, y)
 
 
 """
 According to https://developer.apple.com/library/mac/documentation/Carbon/Reference/QuartzEventServicesRef/Reference/reference.html#//apple_ref/c/func/Quartz.CGEventCreateScrollWheelEvent
 "Scrolling movement is generally represented by small signed integer values, typically in a range from -10 to +10. Large values may have unexpected results, depending on the application that processes the event."
 The scrolling functions will create multiple events that scroll 10 each, and then scroll the remainder.
 """
 
+
 def _vscroll(clicks, x=None, y=None):
     _moveTo(x, y)
     clicks = int(clicks)
     for _ in range(abs(clicks) // 10):
         scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
-            None, # no source
-            Quartz.kCGScrollEventUnitLine, # units
-            1, # wheelCount (number of dimensions)
-            10 if clicks >= 0 else -10) # vertical movement
+            None,  # no source
+            Quartz.kCGScrollEventUnitLine,  # units
+            1,  # wheelCount (number of dimensions)
+            10 if clicks >= 0 else -10)  # vertical movement
         Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)
 
     scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
-        None, # no source
-        Quartz.kCGScrollEventUnitLine, # units
-        1, # wheelCount (number of dimensions)
-        clicks % 10 if clicks >= 0 else -1 * (-clicks % 10)) # vertical movement
+        None,  # no source
+        Quartz.kCGScrollEventUnitLine,  # units
+        1,  # wheelCount (number of dimensions)
+        clicks % 10 if clicks >= 0 else -1 * (-clicks % 10))  # vertical movement
     Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)
 
 
 def _hscroll(clicks, x=None, y=None):
     _moveTo(x, y)
     clicks = int(clicks)
     for _ in range(abs(clicks) // 10):
         scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
-            None, # no source
-            Quartz.kCGScrollEventUnitLine, # units
-            2, # wheelCount (number of dimensions)
-            0, # vertical movement
-            10 if clicks >= 0 else -10) # horizontal movement
+            None,  # no source
+            Quartz.kCGScrollEventUnitLine,  # units
+            2,  # wheelCount (number of dimensions)
+            0,  # vertical movement
+            10 if clicks >= 0 else -10)  # horizontal movement
         Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)
 
     scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
-        None, # no source
-        Quartz.kCGScrollEventUnitLine, # units
-        2, # wheelCount (number of dimensions)
-        0, # vertical movement
-        (clicks % 10) if clicks >= 0 else (-1 * clicks % 10)) # horizontal movement
+        None,  # no source
+        Quartz.kCGScrollEventUnitLine,  # units
+        2,  # wheelCount (number of dimensions)
+        0,  # vertical movement
+        (clicks % 10) if clicks >= 0 else (-1 * clicks % 10))  # horizontal movement
     Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)
 
 
 def _mouseDown(x, y, button):
     if button == LEFT:
-        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
+        _sendMouseEvent(Quartz.kCGEventLeftMouseDown,
+                        x, y, Quartz.kCGMouseButtonLeft)
     elif button == MIDDLE:
-        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
+        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x,
+                        y, Quartz.kCGMouseButtonCenter)
     elif button == RIGHT:
-        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
+        _sendMouseEvent(Quartz.kCGEventRightMouseDown,
+                        x, y, Quartz.kCGMouseButtonRight)
     else:
         assert False, "button argument not in ('left', 'middle', 'right')"
 
 
 def _mouseUp(x, y, button):
     if button == LEFT:
-        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
+        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x,
+                        y, Quartz.kCGMouseButtonLeft)
     elif button == MIDDLE:
-        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
+        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x,
+                        y, Quartz.kCGMouseButtonCenter)
     elif button == RIGHT:
-        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
+        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x,
+                        y, Quartz.kCGMouseButtonRight)
     else:
         assert False, "button argument not in ('left', 'middle', 'right')"
 
 
 def _click(x, y, button):
     if button == LEFT:
-        _sendMouseEvent(Quartz.kCGEventLeftMouseDown, x, y, Quartz.kCGMouseButtonLeft)
-        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x, y, Quartz.kCGMouseButtonLeft)
+        _sendMouseEvent(Quartz.kCGEventLeftMouseDown,
+                        x, y, Quartz.kCGMouseButtonLeft)
+        _sendMouseEvent(Quartz.kCGEventLeftMouseUp, x,
+                        y, Quartz.kCGMouseButtonLeft)
     elif button == MIDDLE:
-        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x, y, Quartz.kCGMouseButtonCenter)
-        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x, y, Quartz.kCGMouseButtonCenter)
+        _sendMouseEvent(Quartz.kCGEventOtherMouseDown, x,
+                        y, Quartz.kCGMouseButtonCenter)
+        _sendMouseEvent(Quartz.kCGEventOtherMouseUp, x,
+                        y, Quartz.kCGMouseButtonCenter)
     elif button == RIGHT:
-        _sendMouseEvent(Quartz.kCGEventRightMouseDown, x, y, Quartz.kCGMouseButtonRight)
-        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x, y, Quartz.kCGMouseButtonRight)
+        _sendMouseEvent(Quartz.kCGEventRightMouseDown,
+                        x, y, Quartz.kCGMouseButtonRight)
+        _sendMouseEvent(Quartz.kCGEventRightMouseUp, x,
+                        y, Quartz.kCGMouseButtonRight)
     else:
         assert False, "button argument not in ('left', 'middle', 'right')"
 
+
 def _multiClick(x, y, button, num, interval=0.0):
-    btn    = None
-    down   = None
-    up     = None
+    btn = None
+    down = None
+    up = None
 
     if button == LEFT:
-        btn  = Quartz.kCGMouseButtonLeft
+        btn = Quartz.kCGMouseButtonLeft
         down = Quartz.kCGEventLeftMouseDown
-        up   = Quartz.kCGEventLeftMouseUp
+        up = Quartz.kCGEventLeftMouseUp
     elif button == MIDDLE:
-        btn  = Quartz.kCGMouseButtonCenter
+        btn = Quartz.kCGMouseButtonCenter
         down = Quartz.kCGEventOtherMouseDown
-        up   = Quartz.kCGEventOtherMouseUp
+        up = Quartz.kCGEventOtherMouseUp
     elif button == RIGHT:
-        btn  = Quartz.kCGMouseButtonRight
+        btn = Quartz.kCGMouseButtonRight
         down = Quartz.kCGEventRightMouseDown
-        up   = Quartz.kCGEventRightMouseUp
+        up = Quartz.kCGEventRightMouseUp
     else:
         assert False, "button argument not in ('left', 'middle', 'right')"
         return
 
     for i in range(num):
         _click(x, y, button)
         time.sleep(interval)
@@ -425,56 +442,105 @@
 def _sendMouseEvent(ev, x, y, button):
     mouseEvent = Quartz.CGEventCreateMouseEvent(None, ev, (x, y), button)
     Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseEvent)
 
 
 def _dragTo(x, y, button):
     if button == LEFT:
-        _sendMouseEvent(Quartz.kCGEventLeftMouseDragged , x, y, Quartz.kCGMouseButtonLeft)
+        _sendMouseEvent(Quartz.kCGEventLeftMouseDragged,
+                        x, y, Quartz.kCGMouseButtonLeft)
     elif button == MIDDLE:
-        _sendMouseEvent(Quartz.kCGEventOtherMouseDragged , x, y, Quartz.kCGMouseButtonCenter)
+        _sendMouseEvent(Quartz.kCGEventOtherMouseDragged,
+                        x, y, Quartz.kCGMouseButtonCenter)
     elif button == RIGHT:
-        _sendMouseEvent(Quartz.kCGEventRightMouseDragged , x, y, Quartz.kCGMouseButtonRight)
+        _sendMouseEvent(Quartz.kCGEventRightMouseDragged,
+                        x, y, Quartz.kCGMouseButtonRight)
     else:
         assert False, "button argument not in ('left', 'middle', 'right')"
-    time.sleep(pygb.DARWIN_CATCH_UP_TIME) # needed to allow OS time to catch up.
+    # needed to allow OS time to catch up.
+    time.sleep(pygb.DARWIN_CATCH_UP_TIME)
+
 
 def _moveTo(x, y):
     _sendMouseEvent(Quartz.kCGEventMouseMoved, x, y, 0)
-    time.sleep(pygb.DARWIN_CATCH_UP_TIME) # needed to allow OS time to catch up.
+    # needed to allow OS time to catch up.
+    time.sleep(pygb.DARWIN_CATCH_UP_TIME)
 
 
 def _activateWindow(name):
     runningApplications = NSWorkspace.sharedWorkspace().runningApplications()
     for app in runningApplications:
         # if getActiveApplicationName() == app.localizedName():
         if name in app.localizedName():
-            app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)    
+            app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
 
 
 def _getActiveWindow():
     # https://stackoverflow.com/a/44229825
     # https://github.com/asweigart/PyGetWindow
     curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()
     curr_pid = NSWorkspace.sharedWorkspace().activeApplication()[
         'NSApplicationProcessIdentifier']
     curr_app_name = curr_app.localizedName()
 
-    options = kCGWindowListOptionOnScreenOnly 
+    options = kCGWindowListOptionOnScreenOnly
     windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
 
     wi = None
     for window in windowList:
         pid = window['kCGWindowOwnerPID']
         windowNumber = window['kCGWindowNumber']
         ownerName = window['kCGWindowOwnerName']
         geometry = window['kCGWindowBounds']
         windowTitle = window.get('kCGWindowName', u'Unknown')
 
         if curr_pid == pid:
-            title = windowTitle.encode('ascii', 'ignore')
+            title = windowTitle.encode('ascii', 'ignore').decode("utf-8")
             h, w, x, y = geometry["Height"], geometry["Width"], geometry["X"], geometry["Y"]
             if h > 100 and w > 100:
-                wi = WindowInstance(pid, windowNumber, (x, y), w, h, ownerName, title)
-                return wi
+                return {
+                    "pid": pid,
+                    "windowNumber": windowNumber,
+                    "ownerName": ownerName,
+                    "title": title,
+                    "x": x,
+                    "y": y,
+                    "width": w,
+                    "height": h
+                }
+
+    return wi
+
+
+def _getOpenedWindows():
+    options = kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements
+    windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
+    openedApps = []
+    for window in windowList:
+        pid = window['kCGWindowOwnerPID']
+        windowNumber = window['kCGWindowNumber']
+        ownerName = window['kCGWindowOwnerName']
+        geometry = window['kCGWindowBounds']
+        windowTitle = window.get(
+            'kCGWindowName', u'Unknown').encode('ascii', 'ignore').decode('utf-8')
+        h, w, x, y = geometry["Height"], geometry["Width"], geometry["X"], geometry["Y"]
+
+        # Skip the instances in the system taskbar
+        if h < 100 or w < 100:
+            continue
+        else:
+            openedApps.append(
+                {
+                    "pid": pid,
+                    "windowNumber": windowNumber,
+                    "ownerName": ownerName,
+                    "title": windowTitle,
+                    "x": x,
+                    "y": y,
+                    "width": w,
+                    "height": h
+                }
+            )
+    return openedApps
 
-    return wi
+def _moveWindow(window, x, y):
+    pass
```

### Comparing `PyGB-0.9.53/pygb/_pygb_screen.py` & `PyGB-0.9.54/pygb/_pygb_screen.py`

 * *Files 6% similar despite different names*

```diff
@@ -44,23 +44,80 @@
     # TODO - How does macOS and Linux handle monitor scaling?
     import ctypes
     try:
        ctypes.windll.user32.SetProcessDPIAware()
     except AttributeError:
         pass # Windows XP doesn't support monitor scaling, so just do nothing.
 
-    try:
-        import pygetwindow
-    except ImportError:
-        _PYGETWINDOW_UNAVAILABLE = True
-    else:
-        _PYGETWINDOW_UNAVAILABLE = False
-else:
-    _PYGETWINDOW_UNAVAILABLE = True
+elif sys.platform == "darwin":
+    from AppKit import NSWorkspace
 
+    from AppKit import NSApplicationActivateIgnoringOtherApps
+    from Quartz import (
+        CGWindowListCopyWindowInfo,
+        kCGWindowListOptionOnScreenOnly,
+        kCGWindowListExcludeDesktopElements,
+        kCGNullWindowID
+    )
+
+
+
+class cWindow:
+    # https://stackoverflow.com/a/30314197
+    def __init__(self):
+        self._hwnd = None
+        self.shell = win32com.client.Dispatch("WScript.Shell")
+
+    def BringToTop(self):
+        win32gui.BringWindowToTop(self._hwnd)
+
+    def SetAsForegroundWindow(self):
+        self.shell.SendKeys('%')
+        win32gui.SetForegroundWindow(self._hwnd)
+
+    def Maximize(self):
+        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)
+
+    def SetWindowSize(self, width, height):
+        x0, y0, x1, y1 = win32gui.GetWindowRect(self._hwnd)
+        win32gui.MoveWindow(self._hwnd, x0, y0, x0+width, y0+height, True)
+
+    def getCoordinate(self):
+        return win32gui.GetWindowRect(self._hwnd)
+
+    def setActWin(self):
+        win32gui.SetActiveWindow(self._hwnd)
+
+    def _window_enum_callback(self, hwnd, wildcard):
+        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
+        # if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
+        if wildcard in str(win32gui.GetWindowText(hwnd)):
+            self._hwnd = hwnd
+
+    def find_window_wildcard(self, wildcard):
+        self._hwnd = None
+        win32gui.EnumWindows(self._window_enum_callback, wildcard)
+
+    def check_window_visibility(self):
+        if self._hwnd == None:
+            print(
+                "Window handle was not found. check if the program exists")
+            import sys
+            sys.exit(0)
+
+        while not win32gui.IsWindowVisible(self._hwnd):
+            time.sleep(2)
+            print(f"Waiting for process {self._hwnd} to start...")
+
+    def kill_task_manager(self):
+        wildcard = 'Task Manager'
+        self.find_window_wildcard(wildcard)
+        if self._hwnd:
+            win32gui.PostMessage(self._hwnd, win32con.WM_CLOSE, 0, 0)
+            time.sleep(0.5)
 
 GRAYSCALE_DEFAULT = False
 
 # For version 0.1.19 I changed it so that ImageNotFoundException was raised
 # instead of returning None. In hindsight, this change came too late, so I'm
 # changing it back to returning None. But I'm also including this option for
 # folks who would rather have it raise an exception.
@@ -413,39 +470,18 @@
     minIndex = distances.index(min(distances))
 
     # returning of center of found image at minimum distance from point
     return center(images[minIndex])
 
 
 def locateOnWindow(image, title, **kwargs):
-    """
-    TODO
-    """
-    if _PYGETWINDOW_UNAVAILABLE:
-        raise PyScreezeException('locateOnWindow() failed because PyGetWindow is not installed or is unsupported on this platform.')
-
-    matchingWindows = pygetwindow.getWindowsWithTitle(title)
-    if len(matchingWindows) == 0:
-        raise PyScreezeException('Could not find a window with %s in the title' % (title))
-    elif len(matchingWindows) > 1:
-        raise PyScreezeException('Found multiple windows with %s in the title: %s' % (title, [str(win) for win in matchingWindows]))
-
-    win = matchingWindows[0]
-    win.activate()
-    return locateOnScreen(image, region=(win.left, win.top, win.width, win.height), **kwargs)
-
-
-@requiresPillow
-def showRegionOnScreen(region, outlineColor='red', filename='_showRegionOnScreen.png'):
-    # TODO - This function is useful! Document it!
-    screenshotIm = screenshot()
-    draw = ImageDraw.Draw(screenshotIm)
-    region = (region[0], region[1], region[2] + region[0], region[3] + region[1]) # convert from (left, top, right, bottom) to (left, top, width, height)
-    draw.rectangle(region, outline=outlineColor)
-    screenshotIm.save(filename)
+    win = getOpenWindow(title)
+    left, top = win.origin
+    width, height = win.dim
+    return locateOnScreen(image, region=(left, top, width, height), **kwargs)
 
 
 @requiresPillow
 def _screenshot_win32(imageFilename=None, region=None):
     # TODO - Use the winapi to get a screenshot, and compare performance with ImageGrab.grab()
     # https://stackoverflow.com/a/3586280/1893164
     im = ImageGrab.grab()
@@ -490,17 +526,14 @@
 
     if imageFilename is None:
         os.unlink(tmpFilename)
     return im
 
 
 def _screenshot_linux(imageFilename=None, region=None):
-    """
-    TODO
-    """
     if not scrotExists:
         raise NotImplementedError('"scrot" must be installed to use screenshot functions in Linux. Run: sudo apt-get install scrot')
     if imageFilename is None:
         tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
     else:
         tmpFilename = imageFilename
     if scrotExists:
@@ -522,17 +555,15 @@
         return im
     else:
         raise Exception('The scrot program must be installed to take a screenshot with PyScreeze on Linux. Run: sudo apt-get install scrot')
 
 
 
 def _kmp(needle, haystack, _dummy): # Knuth-Morris-Pratt search algorithm implementation (to be used by screen capture)
-    """
-    TODO
-    """
+
     # build table of shift amounts
     shifts = [1] * (len(needle) + 1)
     shift = 1
     for pos in range(len(needle)):
         while shift <= pos and needle[pos] != needle[pos-shift]:
             shift += shifts[pos-shift]
         shifts[pos+1] = shift
@@ -547,17 +578,15 @@
             matchLen -= shifts[matchLen]
         matchLen += 1
         if matchLen == len(needle):
             yield startPos
 
 
 def _steppingFind(needle, haystack, step):
-    """
-    TODO
-    """
+
     for startPos in range(0, len(haystack) - len(needle) + 1):
         foundMatch = True
         for pos in range(0, len(needle), step):
             if haystack[startPos + pos] != needle[pos]:
                 foundMatch = False
                 break
         if foundMatch:
@@ -594,17 +623,15 @@
         r, g, b, a = pix
         exR, exG, exB, exA = expectedRGBColor
         return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance) and (abs(a - exA) <= tolerance)
     else:
         assert False, 'Color mode was expected to be length 3 (RGB) or 4 (RGBA), but pixel is length %s and expectedRGBColor is length %s' % (len(pix), len(expectedRGBColor))
 
 def pixel(x, y):
-    """
-    TODO
-    """
+
     if sys.platform == 'win32':
         # On Windows, calling GetDC() and GetPixel() is twice as fast as using our screenshot() function.
         with __win32_openDC(0) as hdc: # handle will be released automatically
             color = windll.gdi32.GetPixel(hdc, x, y)
             if color < 0:
                 raise WindowsError("windll.gdi32.GetPixel failed : return {}".format(color))
             # color is in the format 0xbbggrr https://msdn.microsoft.com/en-us/library/windows/desktop/dd183449(v=vs.85).aspx
```

### Comparing `PyGB-0.9.53/pygb/_pygb_win.py` & `PyGB-0.9.54/pygb/_pygb_win.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,20 +1,19 @@
 # Windows implementation of PyGB functions.
 # BSD license
-# Al Sweigart al@inventwithpython.com
 
 import ctypes
 import ctypes.wintypes
 import pygb
-from pygb import LEFT, MIDDLE, RIGHT, WindowInstance
+from pygb import LEFT, MIDDLE, RIGHT
 
-try:
-    from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
-except:
-    assert False, "You must first install win32gui"
+# try:
+#     from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
+# except:
+#     assert False, "You must first install win32gui"
 
 import sys
 if sys.platform !=  'win32':
     raise Exception('The pygb_win module should only be loaded on a Windows system.')
 
 
 # Fixes the scaling issues where PyGB was reporting the wrong resolution:
@@ -567,12 +566,12 @@
       y (int): The y position of the mouse event.
 
     Returns:
       None
     """
     return _scroll(clicks, x, y)
 
-def _getWindows():
+def _getActiveWindow():
     hwnd = GetForegroundWindow()
     title = GetWindowText(hwnd)
     x1, y1, x2, y2 = GetWindowRect(hwnd)
     wi = WindowInstance(hwnd, (x1, y1), x2-x1, y2-y1, title, "")
```

### Comparing `PyGB-0.9.53/pygb/_pygb_x11.py` & `PyGB-0.9.54/pygb/_pygb_x11.py`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/setup.py` & `PyGB-0.9.54/setup.py`

 * *Files identical despite different names*

### Comparing `PyGB-0.9.53/tests/test_pyautogui.py` & `PyGB-0.9.54/tests/test_pyautogui.py`

 * *Files identical despite different names*

