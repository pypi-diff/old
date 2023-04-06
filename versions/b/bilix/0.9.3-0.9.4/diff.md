# Comparing `tmp/bilix-0.9.3.tar.gz` & `tmp/bilix-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bilix-0.9.3.tar", last modified: Tue Sep  6 01:04:22 2022, max compression
+gzip compressed data, was "bilix-0.9.4.tar", last modified: Tue Oct 25 08:15:59 2022, max compression
```

## Comparing `bilix-0.9.3.tar` & `bilix-0.9.4.tar`

### file list

```diff
@@ -1,48 +1,49 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.302289 bilix-0.9.3/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-06 01:04:06.000000 bilix-0.9.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-09-06 01:04:06.000000 bilix-0.9.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-09-06 01:04:22.302289 bilix-0.9.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    10391 2022-09-06 01:04:06.000000 bilix-0.9.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.298288 bilix-0.9.3/bilix/
--rw-r--r--   0 runner    (1001) docker     (121)       24 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8116 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)      166 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/__version__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.298288 bilix-0.9.3/bilix/api/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8852 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/bilibili.py
--rw-r--r--   0 runner    (1001) docker     (121)     2663 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/cctv.py
--rw-r--r--   0 runner    (1001) docker     (121)     2463 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/douyin.py
--rw-r--r--   0 runner    (1001) docker     (121)     1572 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/jable.py
--rw-r--r--   0 runner    (1001) docker     (121)     3654 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/yhdmp.py
--rw-r--r--   0 runner    (1001) docker     (121)     1432 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/api/yinghuacd.py
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/assign.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.302289 bilix-0.9.3/bilix/dm/
--rw-r--r--   0 runner    (1001) docker     (121)     1685 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/dm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    17064 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/dm/reply_pb2.py
--rw-r--r--   0 runner    (1001) docker     (121)     3179 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/dm/view_pb2.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.302289 bilix-0.9.3/bilix/download/
--rw-r--r--   0 runner    (1001) docker     (121)      579 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3235 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/base_downloader.py
--rw-r--r--   0 runner    (1001) docker     (121)     6774 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/base_downloader_m3u8.py
--rw-r--r--   0 runner    (1001) docker     (121)     5603 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/base_downloader_part.py
--rw-r--r--   0 runner    (1001) docker     (121)    23272 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_bilibili.py
--rw-r--r--   0 runner    (1001) docker     (121)     2509 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_cctv.py
--rw-r--r--   0 runner    (1001) docker     (121)     1562 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_douyin.py
--rw-r--r--   0 runner    (1001) docker     (121)     2097 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_jable.py
--rw-r--r--   0 runner    (1001) docker     (121)     3082 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_yhdmp.py
--rw-r--r--   0 runner    (1001) docker     (121)     2928 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/download/downloader_yinghuacd.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.302289 bilix-0.9.3/bilix/js/
--rw-r--r--   0 runner    (1001) docker     (121)    23731 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/js/yhdmp.js
--rw-r--r--   0 runner    (1001) docker     (121)      777 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/log.py
--rw-r--r--   0 runner    (1001) docker     (121)      641 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/process.py
--rw-r--r--   0 runner    (1001) docker     (121)      724 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/subtitle.py
--rw-r--r--   0 runner    (1001) docker     (121)     2688 2022-09-06 01:04:06.000000 bilix-0.9.3/bilix/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 01:04:22.298288 bilix-0.9.3/bilix.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      931 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       46 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      130 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       40 2022-09-06 01:04:22.000000 bilix-0.9.3/bilix.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-06 01:04:22.302289 bilix-0.9.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1906 2022-09-06 01:04:06.000000 bilix-0.9.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-10-25 08:15:49.000000 bilix-0.9.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-10-25 08:15:49.000000 bilix-0.9.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-10-25 08:15:59.353625 bilix-0.9.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    10391 2022-10-25 08:15:49.000000 bilix-0.9.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix/
+-rw-r--r--   0 runner    (1001) docker     (121)       56 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8600 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      166 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/__version__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix/api/
+-rw-r--r--   0 runner    (1001) docker     (121)       99 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9128 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/bilibili.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2663 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/cctv.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2463 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/douyin.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1572 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/jable.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3654 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/yhdmp.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1432 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/api/yinghuacd.py
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/assign.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix/dm/
+-rw-r--r--   0 runner    (1001) docker     (121)       86 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/dm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17064 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/dm/reply_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1685 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/dm/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3179 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/dm/view_pb2.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix/download/
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3235 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/base_downloader.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6774 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/base_downloader_m3u8.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5603 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/base_downloader_part.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25301 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_bilibili.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2509 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_cctv.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1562 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_douyin.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2097 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_jable.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3082 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_yhdmp.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2928 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/download/downloader_yinghuacd.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix/js/
+-rw-r--r--   0 runner    (1001) docker     (121)    23731 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/js/yhdmp.js
+-rw-r--r--   0 runner    (1001) docker     (121)      777 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/log.py
+-rw-r--r--   0 runner    (1001) docker     (121)      641 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/process.py
+-rw-r--r--   0 runner    (1001) docker     (121)      724 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/subtitle.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2688 2022-10-25 08:15:49.000000 bilix-0.9.4/bilix/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-25 08:15:59.353625 bilix-0.9.4/bilix.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    11061 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      949 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       46 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      130 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       40 2022-10-25 08:15:59.000000 bilix-0.9.4/bilix.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-25 08:15:59.353625 bilix-0.9.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1906 2022-10-25 08:15:49.000000 bilix-0.9.4/setup.py
```

### Comparing `bilix-0.9.3/LICENSE` & `bilix-0.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/PKG-INFO` & `bilix-0.9.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bilix
-Version: 0.9.3
+Version: 0.9.4
 Summary: ⚡️快如闪电的b站视频下载工具，基于Python现代Async异步特性，高速批量下载整部动漫，电视剧，电影，up投稿等
 Home-page: https://github.com/HFrost0/bilix
 Author: HFrost0
 Author-email: hhlfrost@gmail.com
 License: Apache-2.0 license
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
```

### Comparing `bilix-0.9.3/README.md` & `bilix-0.9.4/README.md`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/__main__.py` & `bilix-0.9.4/bilix/__main__.py`

 * *Files 4% similar despite different names*

```diff
@@ -24,15 +24,15 @@
     ctx.exit()
 
 
 def handle_debug(ctx: click.Context, param: typing.Union[click.Option, click.Parameter], value: typing.Any, ):
     if not value or ctx.resilient_parsing:
         return
     logger.setLevel('DEBUG')
-    logger.debug("Debug level on")
+    logger.debug("Debug on, more information will be shown")
 
 
 def print_help():
     console = rich.console.Console()
     console.print(f"\n[bold]bilix {__version__}", justify="center")
     console.print("⚡️快如闪电的bilibili下载工具，基于Python现代Async特性，高速批量下载整部动漫，电视剧，up投稿等\n", justify="center")
     console.print("使用方法： bilix [cyan]<method> <key> [OPTIONS][/cyan] ", justify="left")
@@ -67,15 +67,15 @@
         "--dir",
         '[dark_cyan]str',
         "文件的下载目录，默认当前路径下的videos文件夹下，不存在会自动创建"
     )
     table.add_row(
         "-q --quality",
         '[dark_cyan]int',
-        "视频画面质量，默认0为最高画质，越大画质越低，超出范围时自动选最低画质"
+        "视频画面质量，默认0为最高画质，越大画质越低，超出范围时自动选最低画质，或者直接使用字符串指定'1080p'等名称"
     )
     table.add_row(
         "--max-con",
         '[dark_cyan]int',
         "控制最大同时下载的视频数量，理论上网络带宽越高可以设的越高，默认3",
     )
     table.add_row(
@@ -138,29 +138,43 @@
     )
     table.add_row("-h --help", '', "帮助信息")
     table.add_row("-v --version", '', "版本信息")
     table.add_row("--debug", '', "显示debug信息")
     console.print(Panel(table, border_style="dim", title="Options", title_align="left"))
 
 
+class BasedQualityType(click.ParamType):
+    name = "quality"
+
+    def convert(self, value, param, ctx):
+        try:
+            value = int(value)
+        except ValueError:
+            return value  # str
+        if value in (1080, 720, 480, 360):
+            return str(value)
+        else:
+            return value  # relative choice like 0, 1, 2, 999...
+
+
 @click.command(add_help_option=False)
 @click.argument("method", type=str)
 @click.argument("key", type=str)
 @click.option(
     "--dir",
     "videos_dir",
     type=str,
     default='videos',
 )
 @click.option(
     '-q',
     '--quality',
     'quality',
-    type=int,
-    default=0,
+    type=BasedQualityType(),
+    default=0,  # default relatively choice
 )
 @click.option(
     '--max-con',
     'video_concurrency',
     type=int,
     default=3,
 )
```

### Comparing `bilix-0.9.3/bilix/api/bilibili.py` & `bilix-0.9.4/bilix/api/bilibili.py`

 * *Files 4% similar despite different names*

```diff
@@ -154,14 +154,15 @@
     aid: Union[str, int]
     cid: Union[str, int]
     p: int
     pages: Sequence[Sequence[str]]
     img_url: str
     bvid: str = None
     dash: dict = None
+    support_formats: dict = None
 
 
 async def get_video_info(client: httpx.AsyncClient, url) -> VideoInfo:
     """
     获取视频信息
 
     :param url:
@@ -195,27 +196,29 @@
         title = legal_title(re.search('property="og:title" content="([^"]*)"', res.text).groups()[0])
         for idx, i in enumerate(init_info['initEpList']):
             p_url = i['link']
             add_name = i['title']
             pages.append([add_name, p_url])
     else:
         raise AttributeError("未知类型")
+
     # extract dash
     try:
         play_info = re.search('<script>window.__playinfo__=({.*})</script><script>', res.text).groups()[0]
         play_info = json.loads(play_info)
         dash = play_info['data']['dash']
+        support_formats = play_info['data']['support_formats']
     except (KeyError, AttributeError):  # KeyError-电影，AttributeError-动画
         # todo https://www.bilibili.com/video/BV1Jx411r776?p=3 未处理，没有dash下载方式的视频
-        dash = None
+        dash, support_formats = None, None
     # extract img url
     img_url = re.search('property="og:image" content="([^"]*)"', res.text).groups()[0]
     # construct data
     video_info = VideoInfo(title=title, h1_title=h1_title, aid=aid, cid=cid,
-                           p=p, pages=pages, img_url=img_url, bvid=bvid, dash=dash)
+                           p=p, pages=pages, img_url=img_url, bvid=bvid, dash=dash, support_formats=support_formats)
     return video_info
 
 
 async def get_subtitle_info(client: httpx.AsyncClient, bvid, cid):
     params = {'bvid': bvid, 'cid': cid}
     res = await req_retry(client, 'https://api.bilibili.com/x/player/v2', params=params)
     info = json.loads(res.text)
@@ -234,11 +237,12 @@
 
 if __name__ == '__main__':
     import rich
 
     # result = asyncio.run(get_cate_meta())
     # rich.print(result)
     _dft_client = httpx.AsyncClient(headers=_dft_headers, http2=True)
-    result = asyncio.run(get_favour_page_info(
-        _dft_client, "69072721",
+    result = asyncio.run(get_video_info(
+        _dft_client,
+        "https://www.bilibili.com/video/BV1fK4y1t7hj/?spm_id_from=333.337.search-card.all.click&vd_source=8f8d575add685a41dfeb68d9963dd93f",
     ))
     rich.print(result)
```

### Comparing `bilix-0.9.3/bilix/api/cctv.py` & `bilix-0.9.4/bilix/api/cctv.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/api/douyin.py` & `bilix-0.9.4/bilix/api/douyin.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/api/jable.py` & `bilix-0.9.4/bilix/api/jable.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/api/yhdmp.py` & `bilix-0.9.4/bilix/api/yhdmp.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/api/yinghuacd.py` & `bilix-0.9.4/bilix/api/yinghuacd.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/assign.py` & `bilix-0.9.4/bilix/assign.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/dm/__init__.py` & `bilix-0.9.4/bilix/dm/utils.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/dm/reply_pb2.py` & `bilix-0.9.4/bilix/dm/reply_pb2.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/dm/view_pb2.py` & `bilix-0.9.4/bilix/dm/view_pb2.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/__init__.py` & `bilix-0.9.4/bilix/download/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 # base
-import time
 from .base_downloader_m3u8 import BaseDownloaderM3u8
 from .base_downloader_part import BaseDownloaderPart
 # site
 from .downloader_bilibili import DownloaderBilibili
 from .downloader_jable import DownloaderJable
 from .downloader_douyin import DownloaderDouyin
 from .downloader_yinghuacd import DownloaderYinghuacd
```

### Comparing `bilix-0.9.3/bilix/download/base_downloader.py` & `bilix-0.9.4/bilix/download/base_downloader.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/base_downloader_m3u8.py` & `bilix-0.9.4/bilix/download/base_downloader_m3u8.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/base_downloader_part.py` & `bilix-0.9.4/bilix/download/base_downloader_part.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/downloader_bilibili.py` & `bilix-0.9.4/bilix/download/downloader_bilibili.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,23 +1,51 @@
 import asyncio
-from typing import Union, Sequence
+from typing import Union, Sequence, Tuple
 import aiofiles
 import httpx
 from datetime import datetime, timedelta
 import os
 from itertools import groupby
 from anyio import run_process
 import bilix.api.bilibili as api
 from bilix.assign import Handler
 from bilix.download.base_downloader_part import BaseDownloaderPart
 from bilix.subtitle import json2srt
 from bilix.dm import dm2ass_factory
 from bilix.utils import legal_title, req_retry, cors_slice
 from bilix.log import logger
 
+__all__ = ['DownloaderBilibili']
+
+
+def choose_quality(dash, support_formats, quality: Union[str, int]) -> Tuple[dict, Sequence]:
+    # 1. absolute choice with quality name like 4k 1080p '1080p 60帧'
+    if isinstance(quality, str):
+        for f_info in support_formats:
+            if quality.upper() in f_info['new_description'].upper():
+                q_id = f_info['quality']
+                for video_info in dash['video']:
+                    if video_info['id'] == q_id:
+                        video_urls = (video_info['base_url'], *(video_info['backup_url']
+                                                                if video_info['backup_url'] else ()))
+                        logger.debug(f"quality <{f_info['new_description']}> has been chosen")
+                        return video_info, video_urls
+        raise ValueError(f'No valid quality for {quality}')
+    # 2. relative choice
+    else:
+        video_info, video_urls = None, None
+        for q, (q_id, it) in enumerate(groupby(dash['video'], key=lambda x: x['id'])):
+            video_info = next(it)  # use the first codec
+            video_urls = (video_info['base_url'], *(video_info['backup_url']
+                                                    if video_info['backup_url'] else ()))
+            if q == quality:
+                break
+        logger.debug(f'Relative quality {quality} has been chosen')
+        return video_info, video_urls
+
 
 class DownloaderBilibili(BaseDownloaderPart):
     def __init__(self, videos_dir='videos', sess_data='', video_concurrency=3, part_concurrency=10):
         """
 
         :param videos_dir: 下载到哪个目录，默认当前目录下的为videos中，如果路径不存在将自动创建
         :param sess_data: 有条件的用户填写大会员凭证，填写后可下载大会员资源
@@ -77,15 +105,15 @@
 
     async def get_collect(self, url, quality=0, image=False, subtitle=False, dm=False, only_audio=False,
                           hierarchy: Union[bool, str] = True):
         """
         下载合集
 
         :param url: 合集详情页url
-        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param hierarchy:
         :return:
         """
@@ -102,15 +130,15 @@
                          dm=False, only_audio=False, hierarchy: Union[bool, str] = True):
         """
         下载收藏夹内的视频
 
         :param url_or_fid: 收藏夹url或收藏夹id
         :param num: 下载数量
         :param keyword: 搜索关键词
-        :param quality:
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param series: 每个视频是否下载所有p，False时仅下载系列中的第一个视频
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param hierarchy:
         :return:
@@ -161,15 +189,15 @@
         下载分区视频
 
         :param cate_name: 分区名称
         :param num: 下载数量
         :param order: 何种排序，click播放数，scores评论数，stow收藏数，coin硬币数，dm弹幕数
         :param keyword: 搜索关键词
         :param days: 过去days天中的结果
-        :param quality: 画面质量
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param series: 每个视频是否下载所有p，False时仅下载系列中的第一个视频
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param hierarchy:
         :return:
@@ -208,24 +236,24 @@
         func = self.get_series if series else self.get_video
         # noinspection PyArgumentList
         cors = [func(f"https://www.bilibili.com/video/{i}", quality=quality,
                      image=image, subtitle=subtitle, dm=dm, only_audio=only_audio, hierarchy=hierarchy)
                 for i in bvids]
         await asyncio.gather(*cors)
 
-    async def get_up_videos(self, url_or_mid: str, num=10, order='pubdate', keyword='', quality=0, series=True,
-                            image=False, subtitle=False, dm=False, only_audio=False,
+    async def get_up_videos(self, url_or_mid: str, num=10, order='pubdate', keyword='', quality: Union[int, str] = 0,
+                            series=True, image=False, subtitle=False, dm=False, only_audio=False,
                             hierarchy: Union[bool, str] = True):
         """
 
         :param url_or_mid: b站用户空间页面url 或b站用户id，在空间页面的url中可以找到
         :param num: 下载总数
         :param order: 何种排序，b站支持：最新发布pubdate，最多播放click，最多收藏stow
         :param keyword: 过滤关键词
-        :param quality: 下载视频画面的质量，默认0为可下载的最高画质，数字越大质量越低，数值超过范围时默认选取最低画质
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param series: 每个视频是否下载所有p，False时仅下载系列中的第一个视频
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param hierarchy:
         :return:
@@ -256,22 +284,22 @@
         bvids = bvids[:num]
         func = self.get_series if series else self.get_video
         # noinspection PyArgumentList
         await asyncio.gather(
             *[func(f'https://www.bilibili.com/video/{bv}', quality=quality,
                    image=image, subtitle=subtitle, dm=dm, only_audio=only_audio, hierarchy=hierarchy) for bv in bvids])
 
-    async def get_series(self, url: str, quality: int = 0, image=False, subtitle=False, dm=False, only_audio=False,
-                         p_range: Sequence[int] = None,
+    async def get_series(self, url: str, quality: Union[str, int] = 0, image=False, subtitle=False,
+                         dm=False, only_audio=False, p_range: Sequence[int] = None,
                          hierarchy: Union[bool, str] = True):
         """
         下载某个系列（包括up发布的多p投稿，动画，电视剧，电影等）的所有视频。只有一个视频的情况下仍然可用该方法
 
         :param url: 系列中任意一个视频的url
-        :param quality: 下载视频画面的质量，默认0为可下载的最高画质，数字越大质量越低，数值超过范围时默认选取最低画质
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param p_range: 下载集数范围，例如(1, 3)：P1至P3
         :param hierarchy:
         :return:
@@ -293,83 +321,81 @@
                                subtitle=subtitle, dm=dm, only_audio=only_audio, hierarchy=hierarchy,
                                extra=video_info if idx == p else None)
                 for idx, (add_name, p_url) in enumerate(pages)]
         if p_range:
             cors = cors_slice(cors, p_range)
         await asyncio.gather(*cors)
 
-    async def get_video(self, url: str, quality: int = 0, add_name='', image=False, subtitle=False, dm=False,
-                        only_audio=False, hierarchy: str = '', extra=None):
+    async def get_video(self, url: str, quality: Union[str, int] = 0, add_name='', image=False, subtitle=False,
+                        dm=False, only_audio=False, hierarchy: str = '', extra=None):
         """
         下载单个视频
 
         :param url: 视频的url
-        :param quality: 下载视频画面的质量，默认0为可下载的最高画质，数字越大质量越低，数值超过范围时默认选取最低画质
+        :param quality: 画面质量，0为可以观看的最高画质，越大质量越低，超过范围时自动选择最低画质，或者直接使用字符串指定'1080p'等名称
         :param add_name: 给文件的额外添加名，用户请直接保持默认
         :param image: 是否下载封面
         :param subtitle: 是否下载字幕
         :param dm: 是否下载弹幕
         :param only_audio: 是否仅下载音频
         :param hierarchy:
         :param extra: 额外数据，提供时不用再次请求页面
         :return:
         """
-        await self.v_sema.acquire()
-        if not extra:
+        async with self.v_sema:
+            if not extra:
+                try:
+                    extra = await api.get_video_info(self.client, url)
+                except AttributeError as e:
+                    logger.warning(f'{url} {e}')
+                    return
+            title = extra.h1_title
+            title = legal_title(title, add_name)
+            extra.title = title  # update extra title
+            dash = extra.dash
+            img_url = extra.img_url
+            formats = extra.support_formats
+            if not dash:
+                logger.warning(f'{extra.title} 需要大会员或该地区不支持')
+                return
+            # choose video quality
             try:
-                extra = await api.get_video_info(self.client, url)
-            except AttributeError as e:
-                logger.warning(f'{url} {e}')
-                self.v_sema.release()
+                video_info, video_urls = choose_quality(dash, formats, quality)
+            except ValueError:
+                logger.warning(f"{extra.title} 清晰度<{quality}>不可用，请检查输入是否正确或是否需要大会员")
                 return
-        title = extra.h1_title
-        title = legal_title(title, add_name)
-        extra.title = title  # update extra title
-        dash = extra.dash
-        img_url = extra.img_url
-        if not dash:
-            logger.warning(f'{extra.title} 需要大会员或该地区不支持')
-            self.v_sema.release()
-            return
-        video_info, video_urls = None, None  # avoid ide warning
-        # choose quality
-        for q, (_, i) in enumerate(groupby(dash['video'], key=lambda x: x['id'])):
-            video_info = next(i)
-            video_urls = (video_info['base_url'], *(video_info['backup_url'] if video_info['backup_url'] else ()))
-            if q == quality:
-                break
-        audio_info = dash['audio'][0]
-        audio_urls = (audio_info['base_url'], *(audio_info['backup_url'] if audio_info['backup_url'] else ()))
-
-        file_dir = f'{self.videos_dir}/{hierarchy}' if hierarchy else self.videos_dir
-        task_id = self.progress.add_task(
-            total=1,
-            description=title if len(title) < 33 else f'{title[:15]}...{title[-15:]}', visible=False)
-        cors = []
-        # add cor according to params
-        if not only_audio:
-            if os.path.exists(f'{file_dir}/{title}.mp4'):
-                logger.info(f'[green]已存在[/green] {title}.mp4')
+            # for audio, choose the highest quality
+            audio_info = dash['audio'][0]
+            audio_urls = (audio_info['base_url'], *(audio_info['backup_url'] if audio_info['backup_url'] else ()))
+
+            file_dir = f'{self.videos_dir}/{hierarchy}' if hierarchy else self.videos_dir
+            task_id = self.progress.add_task(
+                total=1, description=title if len(title) < 33 else f'{title[:15]}...{title[-15:]}', visible=False)
+            cors = []
+            # add cor according to params
+            if not only_audio:
+                if os.path.exists(f'{file_dir}/{title}.mp4'):
+                    logger.info(f'[green]已存在[/green] {title}.mp4')
+                else:
+                    cors.append(self.get_media(video_urls, f'{title}-video', task_id, hierarchy))
+                    cors.append(self.get_media(audio_urls, f'{title}-audio', task_id, hierarchy))
             else:
-                cors.append(self.get_media(video_urls, f'{title}-video', task_id, hierarchy))
-                cors.append(self.get_media(audio_urls, f'{title}-audio', task_id, hierarchy))
-        else:
-            cors.append(self.get_media(audio_urls, f'{title}.mp3', task_id, hierarchy))
-        # additional task
-        if image or subtitle or dm:
-            extra_hierarchy = self._make_hierarchy_dir(hierarchy if hierarchy else True, 'extra')
-            if image:
-                cors.append(self._get_static(img_url, title, hierarchy=extra_hierarchy))
-            if subtitle:
-                cors.append(self.get_subtitle(url, extra=extra, hierarchy=extra_hierarchy))
-            if dm:
-                w, h = video_info['width'], video_info['height']
-                cors.append(self.get_dm(url, convert_func=dm2ass_factory(w, h), hierarchy=extra_hierarchy, extra=extra))
-        await asyncio.gather(*cors)
-        self.v_sema.release()
+                cors.append(self.get_media(audio_urls, f'{title}.mp3', task_id, hierarchy))
+            # additional task
+            if image or subtitle or dm:
+                extra_hierarchy = self._make_hierarchy_dir(hierarchy if hierarchy else True, 'extra')
+                if image:
+                    cors.append(self._get_static(img_url, title, hierarchy=extra_hierarchy))
+                if subtitle:
+                    cors.append(self.get_subtitle(url, extra=extra, hierarchy=extra_hierarchy))
+                if dm:
+                    w, h = video_info['width'], video_info['height']
+                    cors.append(
+                        self.get_dm(url, convert_func=dm2ass_factory(w, h), hierarchy=extra_hierarchy, extra=extra))
+            await asyncio.gather(*cors)
 
         if not only_audio and not os.path.exists(f'{file_dir}/{title}.mp4'):
             await run_process(
                 ['ffmpeg', '-i', f'{file_dir}/{title}-video', '-i', f'{file_dir}/{title}-audio',
                  '-codec', 'copy', f'{file_dir}/{title}.mp4', '-loglevel', 'quiet'])
             os.remove(f'{file_dir}/{title}-video')
             os.remove(f'{file_dir}/{title}-audio')
@@ -448,15 +474,15 @@
 def handle(
         method: str,
         key: str,
         videos_dir: str,
         video_concurrency: int,
         part_concurrency: int,
         cookie: str,
-        quality: int,
+        quality: Union[str, int],
         days: int,
         num: int,
         order: str,
         keyword: str,
         no_series: bool,
         hierarchy: bool,
         image: bool,
```

### Comparing `bilix-0.9.3/bilix/download/downloader_cctv.py` & `bilix-0.9.4/bilix/download/downloader_cctv.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/downloader_douyin.py` & `bilix-0.9.4/bilix/download/downloader_douyin.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/downloader_jable.py` & `bilix-0.9.4/bilix/download/downloader_jable.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/downloader_yhdmp.py` & `bilix-0.9.4/bilix/download/downloader_yhdmp.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/download/downloader_yinghuacd.py` & `bilix-0.9.4/bilix/download/downloader_yinghuacd.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/js/yhdmp.js` & `bilix-0.9.4/bilix/js/yhdmp.js`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/log.py` & `bilix-0.9.4/bilix/log.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/process.py` & `bilix-0.9.4/bilix/process.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/subtitle.py` & `bilix-0.9.4/bilix/subtitle.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix/utils.py` & `bilix-0.9.4/bilix/utils.py`

 * *Files identical despite different names*

### Comparing `bilix-0.9.3/bilix.egg-info/PKG-INFO` & `bilix-0.9.4/bilix.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bilix
-Version: 0.9.3
+Version: 0.9.4
 Summary: ⚡️快如闪电的b站视频下载工具，基于Python现代Async异步特性，高速批量下载整部动漫，电视剧，电影，up投稿等
 Home-page: https://github.com/HFrost0/bilix
 Author: HFrost0
 Author-email: hhlfrost@gmail.com
 License: Apache-2.0 license
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
```

### Comparing `bilix-0.9.3/bilix.egg-info/SOURCES.txt` & `bilix-0.9.4/bilix.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 bilix/api/cctv.py
 bilix/api/douyin.py
 bilix/api/jable.py
 bilix/api/yhdmp.py
 bilix/api/yinghuacd.py
 bilix/dm/__init__.py
 bilix/dm/reply_pb2.py
+bilix/dm/utils.py
 bilix/dm/view_pb2.py
 bilix/download/__init__.py
 bilix/download/base_downloader.py
 bilix/download/base_downloader_m3u8.py
 bilix/download/base_downloader_part.py
 bilix/download/downloader_bilibili.py
 bilix/download/downloader_cctv.py
```

### Comparing `bilix-0.9.3/setup.py` & `bilix-0.9.4/setup.py`

 * *Files identical despite different names*

