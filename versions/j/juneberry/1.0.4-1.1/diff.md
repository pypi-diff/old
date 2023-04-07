# Comparing `tmp/juneberry-1.0.4.tar.gz` & `tmp/juneberry-1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "juneberry-1.0.4.tar", max compression
+gzip compressed data, was "juneberry-1.1.tar", max compression
```

## Comparing `juneberry-1.0.4.tar` & `juneberry-1.1.tar`

### file list

```diff
@@ -1,9 +1,14 @@
--rw-r--r--   0        0        0     1063 2023-03-27 16:02:46.104373 juneberry-1.0.4/LICENSE
--rw-r--r--   0        0        0      881 2023-03-28 07:50:03.872453 juneberry-1.0.4/README.md
--rw-r--r--   0        0        0      356 2023-03-28 14:23:52.579411 juneberry-1.0.4/pyproject.toml
--rw-r--r--   0        0        0     1246 2023-03-28 07:18:49.234831 juneberry-1.0.4/src/juneberry/__init__.py
--rw-r--r--   0        0        0     2639 2023-03-28 07:27:42.209987 juneberry-1.0.4/src/juneberry/colors.py
--rw-r--r--   0        0        0     4345 2023-03-28 14:23:37.070469 juneberry-1.0.4/src/juneberry/loggers.py
--rw-r--r--   0        0        0     2216 2023-03-28 07:24:05.955301 juneberry-1.0.4/src/juneberry/themes.py
--rw-r--r--   0        0        0     1701 2023-03-28 07:24:14.139102 juneberry-1.0.4/src/juneberry/timestamps.py
--rw-r--r--   0        0        0     1291 1970-01-01 00:00:00.000000 juneberry-1.0.4/PKG-INFO
+-rw-r--r--   0        0        0     1063 2023-04-06 08:28:33.770601 juneberry-1.1/LICENSE
+-rw-r--r--   0        0        0     1076 2023-04-07 07:51:57.957265 juneberry-1.1/README.md
+-rw-r--r--   0        0        0      373 2023-04-07 07:53:46.897823 juneberry-1.1/pyproject.toml
+-rw-r--r--   0        0        0     1386 2023-04-07 07:50:30.843980 juneberry-1.1/src/juneberry/__init__.py
+-rw-r--r--   0        0        0     2537 2023-04-07 07:50:33.039912 juneberry-1.1/src/juneberry/_colors.py
+-rw-r--r--   0        0        0     1723 2023-04-07 07:50:35.243843 juneberry-1.1/src/juneberry/_effects.py
+-rw-r--r--   0        0        0     1446 2023-04-07 07:50:37.415776 juneberry-1.1/src/juneberry/_levels.py
+-rw-r--r--   0        0        0     4146 2023-04-07 07:50:39.759704 juneberry-1.1/src/juneberry/_loggers.py
+-rw-r--r--   0        0        0     1497 2023-04-07 07:50:41.883638 juneberry-1.1/src/juneberry/_messages.py
+-rw-r--r--   0        0        0     1786 2023-04-07 07:50:43.895575 juneberry-1.1/src/juneberry/_modules.py
+-rw-r--r--   0        0        0     2630 2023-04-07 07:50:46.191504 juneberry-1.1/src/juneberry/_themes.py
+-rw-r--r--   0        0        0     1763 2023-04-07 07:50:48.575430 juneberry-1.1/src/juneberry/_timestamps.py
+-rw-r--r--   0        0        0     1242 2023-04-07 07:50:50.863359 juneberry-1.1/src/juneberry/_type.py
+-rw-r--r--   0        0        0     1515 1970-01-01 00:00:00.000000 juneberry-1.1/PKG-INFO
```

### Comparing `juneberry-1.0.4/LICENSE` & `juneberry-1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `juneberry-1.0.4/src/juneberry/__init__.py` & `juneberry-1.1/src/juneberry/_type.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # -*- coding: utf-8 -*-
 # MIT License
-# 
+#
 # Copyright (c) 2023 mmlvgx
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documentation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to whom the Software is
@@ -16,11 +16,13 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-'''Lightweight Python logging without dependencies'''
-from .loggers import *
-from .colors import *
-from .themes import *
+"""Juneberry types"""
+from typing import NewType
+
+
+_Color = NewType("_Color", str)
+_Effect = NewType("_Effect", str)
```

### Comparing `juneberry-1.0.4/src/juneberry/timestamps.py` & `juneberry-1.1/src/juneberry/_timestamps.py`

 * *Files 25% similar despite different names*

```diff
@@ -16,36 +16,36 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-'''Juneberry timestamps'''
+"""Juneberry timestamps"""
+
 from time import time
 from time import localtime
 from time import strftime
 
-from .colors import RESET
+from datetime import datetime
+
+from ._type import _Color
+from ._type import _Effect
 
 
 class Timestamp:
-    '''
-    Represents a Juneberry timestamp
+    """
+    Represents a Juneberry Timestamp
 
     Attributes:
-        color (str): Color for timestamp
-    '''
+        color (_Color): Color for timestamp
+        effect (_Effect): Effect for timestamp
+    """
 
-    def __init__(self, color: str) -> None:
+    def __init__(self, color: _Color, effect: _Effect) -> None:
         self.color = color
+        self.effect = effect
 
-    def new(self) -> str:
-        '''
-        Get formatted current time
-        '''
-        seconds = time()
-        local = localtime(seconds)
-
-        format = '%d.%m.%Y %H:%M:%S'
-
-        return self.color + strftime(format, local) + RESET
+    def get(self) -> str:
+        """Get current time"""
+        format__ = "%H:%M:%S.%f %Y.%m.%d"
+        return datetime.now().strftime(format__)
```

