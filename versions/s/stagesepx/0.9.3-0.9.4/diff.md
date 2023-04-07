# Comparing `tmp/stagesepx-0.9.3.tar.gz` & `tmp/stagesepx-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/stagesepx-0.9.3.tar", last modified: Thu Dec 26 14:45:51 2019, max compression
+gzip compressed data, was "dist/stagesepx-0.9.4.tar", last modified: Thu Jan  2 03:40:38 2020, max compression
```

## Comparing `stagesepx-0.9.3.tar` & `stagesepx-0.9.4.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     1067 2019-07-19 15:00:04.000000 stagesepx-0.9.3/LICENSE
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      161 2019-09-10 13:53:00.000000 stagesepx-0.9.3/MANIFEST.in
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      523 2019-12-26 14:45:51.000000 stagesepx-0.9.3/PKG-INFO
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     6199 2019-12-26 14:44:46.000000 stagesepx-0.9.3/README.md
--rw-r--r--   0 fengzhangchi   (501) staff       (20)       38 2019-12-26 14:45:51.000000 stagesepx-0.9.3/setup.cfg
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     1148 2019-12-06 12:07:44.000000 stagesepx-0.9.3/setup.py
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     2141 2019-12-26 14:45:47.000000 stagesepx-0.9.3/stagesepx/__init__.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     5818 2019-11-21 13:12:51.000000 stagesepx-0.9.3/stagesepx/api.py
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx/classifier/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      184 2019-10-26 07:15:34.000000 stagesepx-0.9.3/stagesepx/classifier/__init__.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)    12058 2019-12-25 15:40:52.000000 stagesepx-0.9.3/stagesepx/classifier/base.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     1162 2019-12-25 15:35:16.000000 stagesepx-0.9.3/stagesepx/classifier/ssim.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     6247 2019-12-25 15:40:52.000000 stagesepx-0.9.3/stagesepx/classifier/svm.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      598 2019-11-21 13:12:51.000000 stagesepx-0.9.3/stagesepx/cli.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      258 2019-11-21 13:12:51.000000 stagesepx-0.9.3/stagesepx/constants.py
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx/cutter/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      108 2019-08-06 12:11:42.000000 stagesepx-0.9.3/stagesepx/cutter/__init__.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     5353 2019-12-05 15:18:43.000000 stagesepx-0.9.3/stagesepx/cutter/cut_range.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)    16612 2019-09-28 08:16:34.000000 stagesepx-0.9.3/stagesepx/cutter/cut_result.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     5722 2019-12-25 15:40:52.000000 stagesepx-0.9.3/stagesepx/cutter/cutter.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     8463 2019-12-26 14:01:09.000000 stagesepx-0.9.3/stagesepx/hook.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     9185 2019-11-21 13:12:51.000000 stagesepx-0.9.3/stagesepx/reporter.py
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx/template/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     4818 2019-11-21 13:12:51.000000 stagesepx-0.9.3/stagesepx/template/report.html
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     8733 2019-12-06 16:37:47.000000 stagesepx-0.9.3/stagesepx/toolbox.py
--rw-r--r--   0 fengzhangchi   (501) staff       (20)     5642 2019-12-17 16:00:28.000000 stagesepx-0.9.3/stagesepx/video.py
-drwxr-xr-x   0 fengzhangchi   (501) staff       (20)        0 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      523 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/PKG-INFO
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      664 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/SOURCES.txt
--rw-r--r--   0 fengzhangchi   (501) staff       (20)        1 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/dependency_links.txt
--rw-r--r--   0 fengzhangchi   (501) staff       (20)       50 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/entry_points.txt
--rw-r--r--   0 fengzhangchi   (501) staff       (20)      184 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/requires.txt
--rw-r--r--   0 fengzhangchi   (501) staff       (20)       10 2019-12-26 14:45:51.000000 stagesepx-0.9.3/stagesepx.egg-info/top_level.txt
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     1067 2020-01-02 03:37:40.000000 stagesepx-0.9.4/LICENSE
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      161 2020-01-02 03:37:40.000000 stagesepx-0.9.4/MANIFEST.in
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      523 2020-01-02 03:40:38.000000 stagesepx-0.9.4/PKG-INFO
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     6454 2020-01-02 03:37:40.000000 stagesepx-0.9.4/README.md
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       38 2020-01-02 03:40:38.000000 stagesepx-0.9.4/setup.cfg
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     1148 2020-01-02 03:37:40.000000 stagesepx-0.9.4/setup.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     2141 2020-01-02 03:40:34.000000 stagesepx-0.9.4/stagesepx/__init__.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     5818 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/api.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx/classifier/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      184 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/classifier/__init__.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)    12495 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/classifier/base.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     1162 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/classifier/ssim.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     6247 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/classifier/svm.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      598 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/cli.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      258 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/constants.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx/cutter/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      108 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/cutter/__init__.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     5353 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/cutter/cut_range.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)    16612 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/cutter/cut_result.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     5722 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/cutter/cutter.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     8463 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/hook.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     9185 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/reporter.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx/template/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     4818 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/template/report.html
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     8733 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/toolbox.py
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     5642 2020-01-02 03:37:40.000000 stagesepx-0.9.4/stagesepx/video.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      523 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/PKG-INFO
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      664 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/SOURCES.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)        1 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/dependency_links.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       50 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/entry_points.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      184 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/requires.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       10 2020-01-02 03:40:38.000000 stagesepx-0.9.4/stagesepx.egg-info/top_level.txt
```

### Comparing `stagesepx-0.9.3/LICENSE` & `stagesepx-0.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/PKG-INFO` & `stagesepx-0.9.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: stagesepx
-Version: 0.9.3
+Version: 0.9.4
 Summary: detect stages in video automatically
 Home-page: https://github.com/williamfzc/stagesepx
 Author: williamfzc
 Author-email: fengzc@vip.qq.com
 License: MIT
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `stagesepx-0.9.3/README.md` & `stagesepx-0.9.4/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -53,14 +53,28 @@
 
 - [用30行代码快速跑一个demo](example/mini.py)
 - [30行代码怎么没有注释？](example/cut_and_classify.py)
 - [老板让我看看这个项目怎么落地](example)
 - [我有问题要问](https://github.com/williamfzc/stagesepx/issues/new)
 - [官方文档](https://williamfzc.github.io/stagesepx/)
 
+## 安装
+
+标准版（pypi）
+
+```bash
+pip install stagesepx
+```
+
+预览版（github）：
+
+```bash
+pip install --upgrade git+https://github.com/williamfzc/stagesepx.git
+```
+
 ## 常见问题
 
 最终我还是决定通过 issue 面板维护所有的 Q&A ，毕竟问题的提出与回复是一个强交互过程。如果在查看下列链接之后你的问题依旧没有得到解答：
 
 - 请 [新建issue](https://github.com/williamfzc/stagesepx/issues/new)
 - 或在相关的 issue 下进行追问与补充
 - 你的提问将不止帮助到你一个人 :)
@@ -69,14 +83,15 @@
 
 - [安装过程遇到问题？](https://github.com/williamfzc/stagesepx/issues/80)
 - [如何根据图表分析得出app启动的时间？](https://github.com/williamfzc/stagesepx/issues/73)
 - [日志太多了，如何关闭或者导出成文件？](https://github.com/williamfzc/stagesepx/issues/58)
 - [我的视频有 轮播图 或 干扰分类 的区域](https://github.com/williamfzc/stagesepx/issues/55)
 - [分类结果如何定制？](https://github.com/williamfzc/stagesepx/issues/48)
 - [算出来的结果不准确 / 跟传统方式有差距](https://github.com/williamfzc/stagesepx/issues/46)
+- [出现 OutOfMemoryError](https://github.com/williamfzc/stagesepx/issues/86)
 - ...
 
 不仅是问题，如果有任何建议与交流想法，同样可以通过 issue 面板找到我。我们每天都会查看 issue 面板，无需担心跟进不足。
 
 ## 参与项目
 
 项目发展至今，基础需求已经逐步进入稳定与可用阶段。接下来的工作主要分为下面几个部分：
```

### Comparing `stagesepx-0.9.3/setup.py` & `stagesepx-0.9.4/setup.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/__init__.py` & `stagesepx-0.9.4/stagesepx/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -33,9 +33,9 @@
 """
 
 __PROJECT_NAME__ = r"stagesepx"
 __AUTHOR__ = r"williamfzc"
 __AUTHOR_EMAIL__ = r"fengzc@vip.qq.com"
 __LICENSE__ = r"MIT"
 __URL__ = r"https://github.com/williamfzc/stagesepx"
-__VERSION__ = r"0.9.3"
+__VERSION__ = r"0.9.4"
 __DESCRIPTION__ = r"detect stages in video automatically"
```

### Comparing `stagesepx-0.9.3/stagesepx/api.py` & `stagesepx-0.9.4/stagesepx/api.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/classifier/base.py` & `stagesepx-0.9.4/stagesepx/classifier/base.py`

 * *Files 6% similar despite different names*

```diff
@@ -78,14 +78,30 @@
 
     def get_stage_list(self) -> typing.List[str]:
         return [each.stage for each in self.data]
 
     def get_stage_set(self) -> typing.Set[str]:
         return set(self.get_stage_list())
 
+    def get_important_frame_list(self) -> typing.List[SingleClassifierResult]:
+        # save the first frame
+        result = [self.data[0]]
+
+        prev = self.data[0]
+        for cur in self.data[1:]:
+            if cur.stage != prev.stage:
+                result.append(prev)
+                result.append(cur)
+            prev = cur
+
+        # save the latest frame
+        if result[-1] != self.data[-1]:
+            result.append(self.data[-1])
+        return result
+
     def get_offset(self) -> float:
         # timestamp offset between frames
         return self.data[1].timestamp - self.data[0].timestamp
 
     def get_specific_stage(
         self, stage_name: str
     ) -> typing.List[SingleClassifierResult]:
@@ -310,34 +326,34 @@
         final_result: typing.List[SingleClassifierResult] = list()
         if isinstance(video, str):
             video = VideoObject(video)
 
         operator = video.get_operator()
         frame = operator.get_frame_by_id(1)
         while frame is not None:
-            if limit_range:
-                if not any([each.contain(frame.frame_id) for each in limit_range]):
-                    logger.debug(
-                        f"frame {frame.frame_id} ({frame.timestamp}) not in target range, skip"
-                    )
-                    final_result.append(
-                        SingleClassifierResult(
-                            video.path,
-                            frame.frame_id,
-                            frame.timestamp,
-                            constants.IGNORE_FLAG,
-                            frame.data if keep_data else None,
-                        )
-                    )
-                    frame = operator.get_frame_by_id(frame.frame_id + step)
-                    continue
-
             # hook
             frame = self._apply_hook(frame, *args, **kwargs)
 
+            # ignore some ranges
+            if limit_range and not any([each.contain(frame.frame_id) for each in limit_range]):
+                logger.debug(
+                    f"frame {frame.frame_id} ({frame.timestamp}) not in target range, skip"
+                )
+                final_result.append(
+                    SingleClassifierResult(
+                        video.path,
+                        frame.frame_id,
+                        frame.timestamp,
+                        constants.IGNORE_FLAG,
+                        frame.data if keep_data else None,
+                    )
+                )
+                frame = operator.get_frame_by_id(frame.frame_id + step)
+                continue
+
             result = self._classify_frame(frame, *args, **kwargs)
             logger.debug(
                 f"frame {frame.frame_id} ({frame.timestamp}) belongs to {result}"
             )
 
             final_result.append(
                 SingleClassifierResult(
```

### Comparing `stagesepx-0.9.3/stagesepx/classifier/ssim.py` & `stagesepx-0.9.4/stagesepx/classifier/ssim.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/classifier/svm.py` & `stagesepx-0.9.4/stagesepx/classifier/svm.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/cli.py` & `stagesepx-0.9.4/stagesepx/cli.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/cutter/cut_range.py` & `stagesepx-0.9.4/stagesepx/cutter/cut_range.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/cutter/cut_result.py` & `stagesepx-0.9.4/stagesepx/cutter/cut_result.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/cutter/cutter.py` & `stagesepx-0.9.4/stagesepx/cutter/cutter.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/hook.py` & `stagesepx-0.9.4/stagesepx/hook.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/reporter.py` & `stagesepx-0.9.4/stagesepx/reporter.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/template/report.html` & `stagesepx-0.9.4/stagesepx/template/report.html`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/toolbox.py` & `stagesepx-0.9.4/stagesepx/toolbox.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx/video.py` & `stagesepx-0.9.4/stagesepx/video.py`

 * *Files identical despite different names*

### Comparing `stagesepx-0.9.3/stagesepx.egg-info/PKG-INFO` & `stagesepx-0.9.4/stagesepx.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: stagesepx
-Version: 0.9.3
+Version: 0.9.4
 Summary: detect stages in video automatically
 Home-page: https://github.com/williamfzc/stagesepx
 Author: williamfzc
 Author-email: fengzc@vip.qq.com
 License: MIT
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `stagesepx-0.9.3/stagesepx.egg-info/SOURCES.txt` & `stagesepx-0.9.4/stagesepx.egg-info/SOURCES.txt`

 * *Files identical despite different names*

