# Comparing `tmp/pohan-0.0.1.tar.gz` & `tmp/pohan-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pohan-0.0.1.tar", last modified: Wed Apr  5 16:42:10 2023, max compression
+gzip compressed data, was "pohan-0.0.2.tar", last modified: Thu Apr  6 14:36:58 2023, max compression
```

## Comparing `pohan-0.0.1.tar` & `pohan-0.0.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.882792 pohan-0.0.1/
--rw-rw-rw-   0        0        0     1093 2022-09-13 01:21:27.000000 pohan-0.0.1/LICENSE
--rw-rw-rw-   0        0        0     2019 2023-04-05 16:42:10.882792 pohan-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0     1494 2023-04-02 05:09:27.000000 pohan-0.0.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.866803 pohan-0.0.1/pohan.egg-info/
--rw-rw-rw-   0        0        0     2019 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      323 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       10 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-04-05 16:42:10.000000 pohan-0.0.1/pohan.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.869796 pohan-0.0.1/popip/
--rw-rw-rw-   0        0        0       29 2023-03-15 14:35:05.000000 pohan-0.0.1/popip/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.873793 pohan-0.0.1/popip/api/
--rw-rw-rw-   0        0        0        0 2022-09-13 01:21:27.000000 pohan-0.0.1/popip/api/__init__.py
--rw-rw-rw-   0        0        0      775 2023-04-05 15:34:17.000000 pohan-0.0.1/popip/api/api.py
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.876788 pohan-0.0.1/popip/lib/
--rw-rw-rw-   0        0        0        0 2022-09-13 01:21:27.000000 pohan-0.0.1/popip/lib/__init__.py
--rw-rw-rw-   0        0        0      700 2023-04-05 16:42:10.885795 pohan-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      389 2022-10-23 08:47:10.000000 pohan-0.0.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-05 16:42:10.880793 pohan-0.0.1/tests/
--rw-rw-rw-   0        0        0      181 2023-03-15 14:33:48.000000 pohan-0.0.1/tests/__init__.py
--rw-rw-rw-   0        0        0      521 2023-04-05 15:34:17.000000 pohan-0.0.1/tests/test_pip.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.695425 pohan-0.0.2/
+-rw-rw-rw-   0        0        0     1093 2022-09-13 01:21:27.000000 pohan-0.0.2/LICENSE
+-rw-rw-rw-   0        0        0     2019 2023-04-06 14:36:58.695425 pohan-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0     1494 2023-04-05 16:44:51.000000 pohan-0.0.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.648331 pohan-0.0.2/pohan/
+-rw-rw-rw-   0        0        0       29 2023-04-05 16:47:11.000000 pohan-0.0.2/pohan/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.683441 pohan-0.0.2/pohan/api/
+-rw-rw-rw-   0        0        0        0 2022-09-13 01:21:27.000000 pohan-0.0.2/pohan/api/__init__.py
+-rw-rw-rw-   0        0        0      251 2023-04-06 14:36:34.000000 pohan-0.0.2/pohan/api/ood.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.685426 pohan-0.0.2/pohan/lib/
+-rw-rw-rw-   0        0        0        0 2022-09-13 01:21:27.000000 pohan-0.0.2/pohan/lib/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.680625 pohan-0.0.2/pohan.egg-info/
+-rw-rw-rw-   0        0        0     2019 2023-04-06 14:36:58.000000 pohan-0.0.2/pohan.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      325 2023-04-06 14:36:58.000000 pohan-0.0.2/pohan.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:36:58.000000 pohan-0.0.2/pohan.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-05 16:47:39.000000 pohan-0.0.2/pohan.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       10 2023-04-06 14:36:58.000000 pohan-0.0.2/pohan.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-06 14:36:58.000000 pohan-0.0.2/pohan.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      700 2023-04-06 14:36:58.697423 pohan-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      389 2022-10-23 08:47:10.000000 pohan-0.0.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:36:58.694426 pohan-0.0.2/tests/
+-rw-rw-rw-   0        0        0      181 2023-04-05 16:44:51.000000 pohan-0.0.2/tests/__init__.py
+-rw-rw-rw-   0        0        0      386 2023-04-06 14:33:25.000000 pohan-0.0.2/tests/test_pohan.py
```

### Comparing `pohan-0.0.1/LICENSE` & `pohan-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pohan-0.0.1/PKG-INFO` & `pohan-0.0.2/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: pohan
-Version: 0.0.1
-Summary: pip install popip
+Version: 0.0.2
+Summary: pip install pohan
 Home-page: https://www.python-office.com/
 Author: CoderWanFeng
 Author-email: 1957875073@qq.com
 License: MIT
-Project-URL: Bug Tracker, https://github.com/CoderWanFeng/popip/issues
-Project-URL: Documentation, https://github.com/CoderWanFeng/popip/blob/master/README.md
-Project-URL: Source Code, https://github.com/CoderWanFeng/popip
+Project-URL: Bug Tracker, https://github.com/CoderWanFeng/pohan/issues
+Project-URL: Documentation, https://github.com/CoderWanFeng/pohan/blob/master/README.md
+Project-URL: Source Code, https://github.com/CoderWanFeng/pohan
 Platform: any
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
 <p align="center">
@@ -26,39 +26,39 @@
 
 -------------------------------------------------------------------------------
 
 
 ## 📚简介
 
 
-popip是查看第三方库下载数据的小工具。
+pohan是查看第三方库下载数据的小工具。
 
 -------------------------------------------------------------------------------
 
 ## 📦安装
 
 ### 🍊pip 自动下载&更新
 
 已同步到清华镜像
 
 ```
-pip install -i https://mirrors.aliyun.com/pypi/simple/ popip -U
+pip install -i https://mirrors.aliyun.com/pypi/simple/ pohan -U
 ```
 
 
 -------------------------------------------------------------------------------
 
 ## 📝功能
 
 [📘官网：https://www.python-office.com/](https://www.python-office.com/)
 
 参考资料：
 
 - https://github.com/hugovk/pypistats
-- https://github.com/CoderWanFeng/popip
+- https://github.com/CoderWanFeng/pohan
 ### 🐞提供bug反馈或建议
 
 提交问题反馈时，请务必填写和python-office代码本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。
 
 - [Github issue](https://github.com/CoderWanFeng/wftools/issues)
 
 -------------------------------------------------------------------------------
```

### Comparing `pohan-0.0.1/README.md` & `pohan-0.0.2/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -10,39 +10,39 @@
 
 -------------------------------------------------------------------------------
 
 
 ## 📚简介
 
 
-popip是查看第三方库下载数据的小工具。
+pohan是查看第三方库下载数据的小工具。
 
 -------------------------------------------------------------------------------
 
 ## 📦安装
 
 ### 🍊pip 自动下载&更新
 
 已同步到清华镜像
 
 ```
-pip install -i https://mirrors.aliyun.com/pypi/simple/ popip -U
+pip install -i https://mirrors.aliyun.com/pypi/simple/ pohan -U
 ```
 
 
 -------------------------------------------------------------------------------
 
 ## 📝功能
 
 [📘官网：https://www.python-office.com/](https://www.python-office.com/)
 
 参考资料：
 
 - https://github.com/hugovk/pypistats
-- https://github.com/CoderWanFeng/popip
+- https://github.com/CoderWanFeng/pohan
 ### 🐞提供bug反馈或建议
 
 提交问题反馈时，请务必填写和python-office代码本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。
 
 - [Github issue](https://github.com/CoderWanFeng/wftools/issues)
 
 -------------------------------------------------------------------------------
```

### Comparing `pohan-0.0.1/pohan.egg-info/PKG-INFO` & `pohan-0.0.2/pohan.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: pohan
-Version: 0.0.1
-Summary: pip install popip
+Version: 0.0.2
+Summary: pip install pohan
 Home-page: https://www.python-office.com/
 Author: CoderWanFeng
 Author-email: 1957875073@qq.com
 License: MIT
-Project-URL: Bug Tracker, https://github.com/CoderWanFeng/popip/issues
-Project-URL: Documentation, https://github.com/CoderWanFeng/popip/blob/master/README.md
-Project-URL: Source Code, https://github.com/CoderWanFeng/popip
+Project-URL: Bug Tracker, https://github.com/CoderWanFeng/pohan/issues
+Project-URL: Documentation, https://github.com/CoderWanFeng/pohan/blob/master/README.md
+Project-URL: Source Code, https://github.com/CoderWanFeng/pohan
 Platform: any
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
 <p align="center">
@@ -26,39 +26,39 @@
 
 -------------------------------------------------------------------------------
 
 
 ## 📚简介
 
 
-popip是查看第三方库下载数据的小工具。
+pohan是查看第三方库下载数据的小工具。
 
 -------------------------------------------------------------------------------
 
 ## 📦安装
 
 ### 🍊pip 自动下载&更新
 
 已同步到清华镜像
 
 ```
-pip install -i https://mirrors.aliyun.com/pypi/simple/ popip -U
+pip install -i https://mirrors.aliyun.com/pypi/simple/ pohan -U
 ```
 
 
 -------------------------------------------------------------------------------
 
 ## 📝功能
 
 [📘官网：https://www.python-office.com/](https://www.python-office.com/)
 
 参考资料：
 
 - https://github.com/hugovk/pypistats
-- https://github.com/CoderWanFeng/popip
+- https://github.com/CoderWanFeng/pohan
 ### 🐞提供bug反馈或建议
 
 提交问题反馈时，请务必填写和python-office代码本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。
 
 - [Github issue](https://github.com/CoderWanFeng/wftools/issues)
 
 -------------------------------------------------------------------------------
```

### Comparing `pohan-0.0.1/setup.cfg` & `pohan-0.0.2/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2070 6f68 616e 0d0a 7665 7273 696f   = pohan..versio
-00000020: 6e20 3d20 302e 302e 310d 0a64 6573 6372  n = 0.0.1..descr
+00000020: 6e20 3d20 302e 302e 320d 0a64 6573 6372  n = 0.0.2..descr
 00000030: 6970 7469 6f6e 203d 2070 6970 2069 6e73  iption = pip ins
-00000040: 7461 6c6c 2070 6f70 6970 0d0a 6c6f 6e67  tall popip..long
+00000040: 7461 6c6c 2070 6f68 616e 0d0a 6c6f 6e67  tall pohan..long
 00000050: 5f64 6573 6372 6970 7469 6f6e 203d 2066  _description = f
 00000060: 696c 653a 2052 4541 444d 452e 6d64 0d0a  ile: README.md..
 00000070: 6c6f 6e67 5f64 6573 6372 6970 7469 6f6e  long_description
 00000080: 5f63 6f6e 7465 6e74 5f74 7970 6520 3d20  _content_type = 
 00000090: 7465 7874 2f6d 6172 6b64 6f77 6e0d 0a75  text/markdown..u
 000000a0: 726c 203d 2068 7474 7073 3a2f 2f77 7777  rl = https://www
 000000b0: 2e70 7974 686f 6e2d 6f66 6669 6365 2e63  .python-office.c
@@ -17,24 +17,24 @@
 00000100: 6365 6e73 6520 3d20 4d49 540d 0a6c 6963  cense = MIT..lic
 00000110: 656e 7365 5f66 696c 6520 3d20 4c49 4345  ense_file = LICE
 00000120: 4e53 450d 0a70 6c61 7466 6f72 6d73 203d  NSE..platforms =
 00000130: 2061 6e79 0d0a 7072 6f6a 6563 745f 7572   any..project_ur
 00000140: 6c73 203d 200d 0a09 4275 6720 5472 6163  ls = ...Bug Trac
 00000150: 6b65 7220 3d20 6874 7470 733a 2f2f 6769  ker = https://gi
 00000160: 7468 7562 2e63 6f6d 2f43 6f64 6572 5761  thub.com/CoderWa
-00000170: 6e46 656e 672f 706f 7069 702f 6973 7375  nFeng/popip/issu
+00000170: 6e46 656e 672f 706f 6861 6e2f 6973 7375  nFeng/pohan/issu
 00000180: 6573 0d0a 0944 6f63 756d 656e 7461 7469  es...Documentati
 00000190: 6f6e 203d 2068 7474 7073 3a2f 2f67 6974  on = https://git
 000001a0: 6875 622e 636f 6d2f 436f 6465 7257 616e  hub.com/CoderWan
-000001b0: 4665 6e67 2f70 6f70 6970 2f62 6c6f 622f  Feng/popip/blob/
+000001b0: 4665 6e67 2f70 6f68 616e 2f62 6c6f 622f  Feng/pohan/blob/
 000001c0: 6d61 7374 6572 2f52 4541 444d 452e 6d64  master/README.md
 000001d0: 0d0a 0953 6f75 7263 6520 436f 6465 203d  ...Source Code =
 000001e0: 2068 7474 7073 3a2f 2f67 6974 6875 622e   https://github.
 000001f0: 636f 6d2f 436f 6465 7257 616e 4665 6e67  com/CoderWanFeng
-00000200: 2f70 6f70 6970 0d0a 0d0a 5b6f 7074 696f  /popip....[optio
+00000200: 2f70 6f68 616e 0d0a 0d0a 5b6f 7074 696f  /pohan....[optio
 00000210: 6e73 5d0d 0a70 6163 6b61 6765 7320 3d20  ns]..packages = 
 00000220: 6669 6e64 3a0d 0a69 6e73 7461 6c6c 5f72  find:..install_r
 00000230: 6571 7569 7265 7320 3d20 0d0a 0970 7970  equires = ...pyp
 00000240: 6973 7461 7473 0d0a 7079 7468 6f6e 5f72  istats..python_r
 00000250: 6571 7569 7265 7320 3d20 3e3d 332e 360d  equires = >=3.6.
 00000260: 0a69 6e63 6c75 6465 5f70 6163 6b61 6765  .include_package
 00000270: 5f64 6174 6120 3d20 5472 7565 0d0a 7a69  _data = True..zi
```

