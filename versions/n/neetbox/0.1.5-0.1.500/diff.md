# Comparing `tmp/neetbox-0.1.5.tar.gz` & `tmp/neetbox-0.1.500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "neetbox-0.1.5.tar", max compression
+gzip compressed data, was "neetbox-0.1.500.tar", max compression
```

## Comparing `neetbox-0.1.5.tar` & `neetbox-0.1.500.tar`

### file list

```diff
@@ -1,24 +1,31 @@
--rw-r--r--   0        0        0      397 2023-03-18 11:27:31.197893 neetbox-0.1.5/README.md
--rw-r--r--   0        0        0        0 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/__init__.py
--rw-r--r--   0        0        0      107 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/core/__init__.py
--rw-r--r--   0        0        0     2314 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/core/environment.py
--rw-r--r--   0        0        0     2230 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/core/framing.py
--rw-r--r--   0        0        0     3176 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/image.py
--rw-r--r--   0        0        0      143 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/logging/__init__.py
--rw-r--r--   0        0        0       93 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/logging/_handling.py
--rw-r--r--   0        0        0     3959 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/logging/formatting.py
--rw-r--r--   0        0        0     9741 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/logging/logger.py
--rw-r--r--   0        0        0        0 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/pipline/__init__.py
--rw-r--r--   0        0        0      101 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/pipline/registry.py
--rw-r--r--   0        0        0       72 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/pipline/runner.py
--rw-r--r--   0        0        0        0 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/plotting/__init__.py
--rw-r--r--   0        0        0     4922 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/plotting/plot.py
--rw-r--r--   0        0        0       88 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/__init__.py
--rw-r--r--   0        0        0     5227 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/arch/canny.py
--rw-r--r--   0        0        0     6437 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/arch/cnn.py
--rw-r--r--   0        0        0     2284 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/arch/kernels.py
--rw-r--r--   0        0        0     2440 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/arch/mask_boundary_finder.py
--rw-r--r--   0        0        0     3378 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/nlp.py
--rw-r--r--   0        0        0     4449 2023-03-18 11:27:31.205893 neetbox-0.1.5/neetbox/torch/profile.py
--rw-r--r--   0        0        0     1070 2023-03-18 11:27:31.205893 neetbox-0.1.5/pyproject.toml
--rw-r--r--   0        0        0     1650 1970-01-01 00:00:00.000000 neetbox-0.1.5/PKG-INFO
+-rw-r--r--   0        0        0      397 2023-04-07 09:06:59.220904 neetbox-0.1.500/README.md
+-rw-r--r--   0        0        0        0 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/__init__.py
+-rw-r--r--   0        0        0       19 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/core/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/core/core.py
+-rw-r--r--   0        0        0      418 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/integrations/__init__.py
+-rw-r--r--   0        0        0     1022 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/integrations/engine.py
+-rw-r--r--   0        0        0     6752 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/integrations/environment.py
+-rw-r--r--   0        0        0     7468 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/integrations/resource.py
+-rw-r--r--   0        0        0      255 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/logging/__init__.py
+-rw-r--r--   0        0        0     2106 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/logging/_colorama.py
+-rw-r--r--   0        0        0        0 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/logging/_default.py
+-rw-r--r--   0        0        0     3697 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/logging/formatting.py
+-rw-r--r--   0        0        0    17105 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/logging/logger.py
+-rw-r--r--   0        0        0       54 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/pipeline/__init__.py
+-rw-r--r--   0        0        0      171 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/pipeline/pipe.py
+-rw-r--r--   0        0        0     4754 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/pipeline/registry.py
+-rw-r--r--   0        0        0       72 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/pipeline/runner.py
+-rw-r--r--   0        0        0        0 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/plotting/__init__.py
+-rw-r--r--   0        0        0     4922 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/plotting/plot.py
+-rw-r--r--   0        0        0      115 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/__init__.py
+-rw-r--r--   0        0        0     5227 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/arch/canny.py
+-rw-r--r--   0        0        0     6437 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/arch/cnn.py
+-rw-r--r--   0        0        0     2319 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/arch/kernels.py
+-rw-r--r--   0        0        0     2440 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/arch/mask_boundary_finder.py
+-rw-r--r--   0        0        0     3122 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/nlp.py
+-rw-r--r--   0        0        0     4517 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/torch/profile.py
+-rw-r--r--   0        0        0        0 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/utils/__init__.py
+-rw-r--r--   0        0        0     2303 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/utils/framing.py
+-rw-r--r--   0        0        0     1420 2023-04-07 09:06:59.228905 neetbox-0.1.500/neetbox/utils/utils.py
+-rw-r--r--   0        0        0     1140 2023-04-07 09:06:59.228905 neetbox-0.1.500/pyproject.toml
+-rw-r--r--   0        0        0     1784 1970-01-01 00:00:00.000000 neetbox-0.1.500/PKG-INFO
```

### Comparing `neetbox-0.1.5/neetbox/core/framing.py` & `neetbox-0.1.500/neetbox/utils/framing.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,9 +1,13 @@
-import sys
-from sys import exc_info
+# -*- coding: utf-8 -*-
+#
+# Author: GavinGong aka VisualDust
+# URL:    https://gong.host
+# Date:   20230319
+
 from os import path
 import inspect
 
 
 def get_frame_traceback(traceback=1):
     stack = inspect.stack()[traceback]
     return stack
```

### Comparing `neetbox-0.1.5/neetbox/logging/formatting.py` & `neetbox-0.1.500/neetbox/logging/formatting.py`

 * *Files 24% similar despite different names*

```diff
@@ -2,60 +2,49 @@
 #
 # Author: GavinGong aka VisualDust
 # URL:    https://gong.host
 # Date:   20230318
 
 import warnings
 import os
-from colorama import Fore, Back
-from enum import Enum
+from colorama import Fore, Back, Style
 from random import random
-
-
-class AnsiColor(Enum):
-    BLACK = "BLACK"
-    RED = "RED"
-    GREEN = "GREEN"
-    YELLOW = "YELLOW"
-    BLUE = "BLUE"
-    MAGENTA = "MAGENTA"
-    CYAN = "CYAN"
-    WHITE = "WHITE"
-    RESET = "RESET"
-    # These are fairly well supported, but not part of the standard.
-    LIGHT_BLACK = "LIGHTBLACK_EX"
-    LIGHT_RED = "LIGHTRED_EX"
-    LIGHT_GREEN = "LIGHTGREEN_EX"
-    LIGHT_YELLOW = "LIGHTYELLOW_EX"
-    LIGHT_BLUE = "LIGHTBLUE_EX"
-    LIGHT_MAGENTA = "LIGHTMAGENTA_EX"
-    LIGHT_CYAN = "LIGHTCYAN_EX"
-    LIGHT_WHITE = "LIGHTWHITE_EX"
-
+from ._colorama import *
 
 # todo use @cache when migrate to python 3.9
 def get_supported_colors():
     supported_colors = []
     for color in AnsiColor:
         supported_colors.append(color)
     return supported_colors
 
+def get_supported_styles():
+    supported_styles = []
+    for style in AnsiStyle:
+        supported_styles.append(style)
+    return supported_styles
+
 
 class LogStyle:
     def __init__(self) -> None:
         self.fore: AnsiColor = None
         self.back: AnsiColor = None
         self.prefix: str = ""
+        self.pattern = ""  # todo default pattern
         self.datetime_format: str = "%Y-%m-%d-%H:%M:%S"
         self.with_identifier: bool = True
         self.trace_level = 3
         self.with_datetime: bool = True
         self.split_char_cmd = " > "
         self.split_char_identity = "/"
         self.split_char_txt = " | "
+        
+    def parse(pattern:str):
+        # todo
+        pass
 
     def set_foreground_color(self, color: AnsiColor):
         self.fore = color
         return self
 
     def set_background_color(self, color: AnsiColor):
         self.back = color
@@ -79,15 +68,17 @@
         self.fore = colors[(split_index - index_offset) % len(colors)]
         return self
 
 
 DEFAULT_STYLE = LogStyle()
 
 
-def colored(text, color_foreground: AnsiColor = None, color_background: AnsiColor = None):
+def colored(
+    text, color_foreground: AnsiColor = None, color_background: AnsiColor = None
+):
     """_summary_
 
     Args:
         text (str): original raw string
         color (AnsiColor): which color
 
     Raises: Nothing
@@ -107,19 +98,19 @@
         if hasattr(Fore, color_foreground.upper()):
             text = getattr(Fore, color_foreground.upper()) + text + Fore.RESET
         else:
             raise ValueError("Wrong color was inputed in colored func.")
 
     # Resolving background color
     if color_background:
-        if type(color_foreground) is AnsiColor:
+        if type(color_background) is AnsiColor:
             color_background = color_background.value
         color_background = color_background.value
-        if hasattr(Fore, color_foreground.upper()):
-            text = getattr(Back, color_foreground.upper()) + text + Fore.RESET
+        if hasattr(Back, color_background.upper()):
+            text = getattr(Back, color_background.upper()) + text + Fore.RESET
         else:
             raise ValueError("Wrong color was inputed in colored func.")
 
     return text
 
 
 def colored_by_style(text, style: LogStyle):
```

### Comparing `neetbox-0.1.5/neetbox/plotting/plot.py` & `neetbox-0.1.500/neetbox/plotting/plot.py`

 * *Files identical despite different names*

### Comparing `neetbox-0.1.5/neetbox/torch/arch/canny.py` & `neetbox-0.1.500/neetbox/torch/arch/canny.py`

 * *Files identical despite different names*

### Comparing `neetbox-0.1.5/neetbox/torch/arch/cnn.py` & `neetbox-0.1.500/neetbox/torch/arch/cnn.py`

 * *Files identical despite different names*

### Comparing `neetbox-0.1.5/neetbox/torch/arch/kernels.py` & `neetbox-0.1.500/neetbox/torch/arch/kernels.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 import numpy as np
-from neetbox.core import env
-import cv2
+from neetbox.integrations import pkg
 
 
 def get_gaussian_kernel(k=3, mu=0, sigma=1, normalize=True):
     # compute 1 dimension gaussian
     gaussian_1D = np.linspace(-1, 1, k)
     # compute a grid distance from center
     x, y = np.meshgrid(gaussian_1D, gaussian_1D)
@@ -29,15 +28,16 @@
     sobel_2D_denominator = x**2 + y**2
     sobel_2D_denominator[:, k // 2] = 1  # avoid division by zero
     sobel_2D = sobel_2D_numerator / sobel_2D_denominator
     return sobel_2D
 
 
 def get_thin_kernels(start=0, end=360, step=45):
-    assert env.installed("cv2", terminate=True)
+    assert pkg.is_installed("cv2", try_install_if_not="opencv-python")
+    import cv2
     k_thin = 3  # actual size of the directional kernel
     # increase for a while to avoid interpolation when rotating
     k_increased = k_thin + 2
 
     # get 0° angle directional kernel
     thin_kernel_0 = np.zeros((k_increased, k_increased))
     thin_kernel_0[k_increased // 2, k_increased // 2] = 1
```

### Comparing `neetbox-0.1.5/neetbox/torch/arch/mask_boundary_finder.py` & `neetbox-0.1.500/neetbox/torch/arch/mask_boundary_finder.py`

 * *Files identical despite different names*

### Comparing `neetbox-0.1.5/neetbox/torch/nlp.py` & `neetbox-0.1.500/neetbox/torch/nlp.py`

 * *Files 4% similar despite different names*

```diff
@@ -75,18 +75,7 @@
             wv_tokens.append(word)
 
     wv_dict = {word: i for i, word in enumerate(wv_tokens)}
     wv_arr = torch.Tensor(wv_arr).view(-1, wv_size)
     ret = (wv_dict, wv_arr, wv_size)
     torch.save(ret, fname + '.pt')
     return ret
-
-
-def reporthook(t):
-    """https://github.com/tqdm/tqdm"""
-    last_b = [0]
-    def inner(b=1, bsize=1, tsize=None):
-        if tsize is not None:
-            t.total = tsize
-        t.update((b - last_b[0]) * bsize)
-        last_b[0] = b
-    return inner
```

### Comparing `neetbox-0.1.5/neetbox/torch/profile.py` & `neetbox-0.1.500/neetbox/torch/profile.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 # -*- coding: utf-8 -*-
 #
 # Author: GavinGong aka VisualDust
 # URL:    https://gong.host
 # Date:   20230315
 
-from neetbox.core import env
-from thop import profile as _profile
+from neetbox.integrations import pkg
 import time
 from tqdm import tqdm
 import torch
 
 from neetbox.logging import get_logger
 
 logger = get_logger("NEETBOX")
@@ -18,15 +17,15 @@
 def profile(
     model,
     input_shape=(1, 3, 1280, 720),
     specific_input=None,
     profiling=True,
     speedtest=1000,
 ):
-    assert env.installed('thop', terminate=True)
+    assert pkg.is_installed('thop', try_install_if_not=True)
     if speedtest:
         input_tensor = specific_input
         if not input_tensor:
             input_tensor = torch.rand(input_shape)
             if next(model.parameters()).is_cuda:
                 input_tensor = input_tensor.cuda()
         counter = []
@@ -101,9 +100,11 @@
         logger.log("model profiling...")
         input_tensor = specific_input
         if not input_tensor:
             input_tensor = torch.rand(input_shape)
             if next(model.parameters()).is_cuda:
                 input_tensor = input_tensor.cuda()
         input_tensor = (input_tensor,)
+        assert pkg.is_installed('thop')
+        from thop import profile as _profile
         flops, params = _profile(model, inputs=input_tensor)
         logger.log(f"Model FLOPs = {flops/1e9}G, params = {params/1e6}M")
```

### Comparing `neetbox-0.1.5/pyproject.toml` & `neetbox-0.1.500/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "neetbox"
-version = "0.1.5"
+version = "0.1.500"
 description = "NEETBox contains useless CV code snippets."
 license = "MIT"
 authors = [
     "VisualDust <gavin@gong.host>",
 ]
 maintainers = [
     "VisualDust <gavin@gong.host>",
@@ -35,12 +35,16 @@
 [tool.poetry.dependencies]
 python = ">=3.8"
 numpy = ">=1"
 pillow = ">=8"
 pandas = ">=1"
 tqdm = ">=4"
 colorama = ">=0.3"
-toml = "^0.10.2"
+toml = ">0.10"
+pytest = "*"
+gputil = "^1.4.0"
+psutil = "^5.9.4"
+injector = "^0.20.1"
 
 [build-system]
 requires = ["poetry>=0.12"]
 build-backend = "poetry.masonry.api"
```

