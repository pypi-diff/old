# Comparing `tmp/jmcomic-1.4.0.tar.gz` & `tmp/jmcomic-1.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/JMComic-Crawler-Python/JMComic-Crawler-Python/dist/.tmp-e8dib_04/jmcomic-1.4.0.tar", last modified: Fri Apr  7 08:14:38 2023, max compression
+gzip compressed data, was "/home/runner/work/JMComic-Crawler-Python/JMComic-Crawler-Python/dist/.tmp-8lmu8dc7/jmcomic-1.5.0.tar", last modified: Fri Apr  7 10:08:21 2023, max compression
```

## Comparing `jmcomic-1.4.0.tar` & `jmcomic-1.5.0.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:14:38.000000 jmcomic-1.4.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-07 08:14:30.000000 jmcomic-1.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 08:14:38.000000 jmcomic-1.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-04-07 08:14:30.000000 jmcomic-1.4.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 08:14:38.000000 jmcomic-1.4.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 08:14:30.000000 jmcomic-1.4.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic/
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5971 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     6182 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2773 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9475 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_entity.py
--rw-r--r--   0 runner    (1001) docker     (123)    16396 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_option.py
--rw-r--r--   0 runner    (1001) docker     (123)     8537 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_service.py
--rw-r--r--   0 runner    (1001) docker     (123)    10136 2023-04-07 08:14:30.000000 jmcomic-1.4.0/src/jmcomic/jm_toolkit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 08:14:38.000000 jmcomic-1.4.0/src/jmcomic.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-07 10:08:03.000000 jmcomic-1.5.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:08:21.000000 jmcomic-1.5.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-04-07 10:08:03.000000 jmcomic-1.5.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 10:08:21.000000 jmcomic-1.5.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 10:08:03.000000 jmcomic-1.5.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/src/jmcomic/
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5129 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6971 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9480 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17129 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_option.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8537 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10136 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_toolkit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/src/jmcomic.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/top_level.txt
```

### Comparing `jmcomic-1.4.0/LICENSE` & `jmcomic-1.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `jmcomic-1.4.0/PKG-INFO` & `jmcomic-1.5.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jmcomic
-Version: 1.4.0
+Version: 1.5.0
 Summary: Python API For JMComic (禁漫天堂)
 Home-page: https://github.com/hect0x7/JMComic-Crawler-Python
 Author: hect0x7
 Author-email: 93357912+hect0x7@users.noreply.github.com
 Keywords: python,jmcomic,18comic,禁漫天堂,NSFW
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `jmcomic-1.4.0/README.md` & `jmcomic-1.5.0/README.md`

 * *Files identical despite different names*

### Comparing `jmcomic-1.4.0/setup.py` & `jmcomic-1.5.0/setup.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.4.0/src/jmcomic/api.py` & `jmcomic-1.5.0/src/jmcomic/api.py`

 * *Files 18% similar despite different names*

```diff
@@ -127,41 +127,21 @@
         multi_task_launcher_batch(
             iter_objs=enumerate(photo_detail),
             apply_each_obj_func=download_image,
             batch_size=option.download_multi_thread_photo_batch_count
         )
 
 
-def renew_jm_default_domain():
-    """
-    由于禁漫的域名经常变化，调用此方法可以获取一个当前可用的最新的域名 domain，
-    并且设置把 domain 设置为禁漫模块的默认域名。
-    这样一来，配置文件也不用配置域名了，一切都在运行时动态获取。
-    """
-    domain = JmcomicText.parse_to_jm_domain(JmModuleConfig.get_jmcomic_url())
-    JmModuleConfig.DOMAIN = domain
-    return domain
-
-
 def build_client(option: Optional[JmOption]) -> Tuple[JmOption, JmcomicClient]:
     """
     处理option的判空，并且创建jm_client
     """
     if option is None:
         option = JmOption.default()
-        option.client_config['domain'] = renew_jm_default_domain()
+
     jm_client = option.build_jm_client()
     return option, jm_client
 
 
 def create_option(filepath: str) -> JmOption:
-    """
-    创建 JmOption，同时检查域名是否配置，未配置则补上配置
-    @param filepath:
-    @return:
-    """
     option = JmOption.create_from_file(filepath)
-    client_config = option.client_config
-    key = 'domain'
-    if client_config.get(key, None) is None or client_config[key] is None:
-        client_config[key] = renew_jm_default_domain()
     return option
```

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_client.py` & `jmcomic-1.5.0/src/jmcomic/jm_client.py`

 * *Files 19% similar despite different names*

```diff
@@ -116,15 +116,15 @@
         resp = self.jm_get('/search/photos', params=params)
 
         return JmSearchSupport.analyse_jm_search_html(resp.text)
 
     # -- 对象方法 --
 
     def of_api_url(self, api_path):
-        return f"{JmModuleConfig.HTTP}{self.domain}{api_path}"
+        return f"{JmModuleConfig.PROT}{self.domain}{api_path}"
 
     def jm_get(self, url, is_api=True, require_200=True, **kwargs):
         """
         向禁漫发请求的统一入口
         """
         url = self.of_api_url(url) if is_api is True else url
         if is_api is True:
@@ -153,14 +153,36 @@
     def is_empty_image(cls, resp):
         return resp.status_code != 200 or len(resp.content) == 0
 
     @classmethod
     def img_is_not_need_to_decode(cls, data_original: str, _resp):
         return data_original.endswith('.gif')
 
+    # noinspection PyAttributeOutsideInit
+    def enable_cache(self):
+        def wrap_func_cache(func_name, cache_dict_name):
+            if hasattr(self, cache_dict_name):
+                return
+
+            cache_dict = {}
+            setattr(self, cache_dict_name, cache_dict)
+
+            # 重载本对象的方法
+            func = getattr(self, func_name)
+            wrap_func = enable_cache(
+                cache_dict=cache_dict,
+                cache_hit_msg=f'命中 {cache_dict_name} ' + '→ [{}]]',
+                cache_miss_msg=f'缺失 {cache_dict_name} ' + '← [{}]',
+            )(func)
+
+            setattr(self, func_name, wrap_func)
+
+        wrap_func_cache('get_photo_detail', 'album_cache_dict')
+        wrap_func_cache('get_album_detail', 'photo_cache_dict')
+
 
 # 爬取策略
 class FetchStrategy:
 
     def __init__(self,
                  from_index,
                  photo_len,
```

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_config.py` & `jmcomic-1.5.0/src/jmcomic/jm_config.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 class JmModuleConfig:
     # 网站相关
-    HTTP = "https://"
-    DOMAIN = "jmcomic1.group"  # jmcomic默认域名
-    JM_REDIRECT_URL = f'{HTTP}jm365.xyz/3YeBdF'  # 永久網域，怕走失的小伙伴收藏起来↓
-    JM_PUB_URL = f'{HTTP}jmcomic1.bet'
-    JM_CDN_IMAGE_URL_TEMPLATE = HTTP + 'cdn-msp.{domain}/media/photos/{photo_id}/{index:05}{suffix}'  # index 从1开始
+    PROT = "https://"
+    _DOMAIN = None
+    JM_REDIRECT_URL = f'{PROT}jm365.xyz/3YeBdF'  # 永久網域，怕走失的小伙伴收藏起来
+    JM_PUB_URL = f'{PROT}jmcomic1.bet'
+    JM_CDN_IMAGE_URL_TEMPLATE = PROT + 'cdn-msp.{domain}/media/photos/{photo_id}/{index:05}{suffix}'  # index 从1开始
     JM_SERVER_ERROR_HTML = "Could not connect to mysql! Please check your database settings!"
     JM_IMAGE_SUFFIX = ['.jpg', '.webp', '.png', '.gif']
 
     # 图片分隔相关
     SCRAMBLE_0 = 220980
     SCRAMBLE_10 = 268850
     SCRAMBLE_NUM_8 = 421926  # 2023-02-08后改了图片切割算法
@@ -22,17 +22,29 @@
     enable_jm_debug = True
     debug_printer = print
 
     # 缓存
     jm_client_caches = {}
 
     @classmethod
-    def default_headers(cls):
+    def domain(cls, postman=None):
+        """
+        由于禁漫的域名经常变化，调用此方法可以获取一个当前可用的最新的域名 domain，
+        并且设置把 domain 设置为禁漫模块的默认域名。
+        这样一来，配置文件也不用配置域名了，一切都在运行时动态获取。
+        """
+        if cls._DOMAIN is None:
+            cls._DOMAIN = cls.get_jmcomic_url(postman).replace(cls.PROT, '')
+
+        return cls._DOMAIN  # jmcomic默认域名
+
+    @classmethod
+    def headers(cls, authority=None):
         return {
-            'authority': cls.DOMAIN,
+            'authority': authority or cls.domain(),
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                       'application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'zh-CN,zh;q=0.9',
             'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
             'sec-ch-ua-mobile': '?0',
             'sec-ch-ua-platform': '"Windows"',
             'sec-fetch-dest': 'document',
@@ -51,24 +63,24 @@
             cls.debug_printer(f'【{topic}】{msg}')
 
     @classmethod
     def disable_jm_debug(cls):
         cls.enable_jm_debug = False
 
     @classmethod
-    def get_jmcomic_url(cls):
+    def get_jmcomic_url(cls, postman=None):
         """
         访问禁漫的永久网域，从而得到一个可用的禁漫网址，
         """
-        from common import Postmans
+        if postman is None:
+            from common import Postmans
+            postman = Postmans.get_impl_clazz('cffi') \
+                .create(headers=cls.headers(cls.JM_REDIRECT_URL))
 
-        domain = Postmans \
-            .get_impl_clazz('cffi') \
-            .create(headers=cls.default_headers()) \
-            .with_wrap_resp() \
+        domain = postman.with_wrap_resp() \
             .get(cls.JM_REDIRECT_URL, allow_redirects=False) \
             .redirect_url
 
         cls.jm_debug('获取禁漫地址', f'获取成功，最新可用的禁漫地址: {domain}')
         return domain
```

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_entity.py` & `jmcomic-1.5.0/src/jmcomic/jm_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -127,15 +127,15 @@
 
     @property
     def keyword_list(self) -> List[str]:
         return self._keywords.split(',')
 
     @property
     def album_id(self) -> str:
-        return self.photo_id if self.is_single_album else self._series_id
+        return self.photo_id if self.is_single_album else str(self._series_id)
 
     @property
     def album_index(self) -> int:
         """
         返回这个章节在本子中的序号，从1开始
         """
```

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_option.py` & `jmcomic-1.5.0/src/jmcomic/jm_option.py`

 * *Files 4% similar despite different names*

```diff
@@ -313,18 +313,18 @@
         jm_option: JmOption = PackerUtil.unpack(filepath, JmOption)[0]
         jm_option.filepath = filepath
         return jm_option
 
     @classmethod
     def default_client_config(cls):
         return {
-            'domain': JmModuleConfig.DOMAIN,
+            'domain': JmModuleConfig.domain(),
             'meta_data': {
                 'cookies': None,
-                'headers': JmModuleConfig.default_headers(),
+                'headers': JmModuleConfig.headers(),
                 'allow_redirects': True,
             },
             'postman_type_list': [
                 'requests',
                 'requests_Session',
                 'cffi',
                 'cffi_Session',
@@ -360,64 +360,89 @@
                 client = self.new_jm_client()
                 JmModuleConfig.jm_client_caches.setdefault(key, client)
 
         return client
 
     def new_jm_client(self) -> JmcomicClient:
         meta_data = self.client_config['meta_data']
+        postman_clazz = Postmans.get_impl_clazz(self.client_config.get('postman_type', 'cffi'))
+        proxies = None
+        domain = None
+        postman: Optional[Postman] = None
 
-        # 处理代理
-        def handle_proxies(key='proxies'):
+        def decide_proxies(key='proxies'):
+            nonlocal proxies
             proxies = meta_data.get(key, None)
 
             # 无代理，或代理已配置好好的
             if proxies is None or isinstance(proxies, dict):
                 return
 
             # 有代理
             if proxies in self._proxies_mapping:
                 proxies = self._proxies_mapping[proxies]()
             else:
                 proxies = ProxyBuilder.build_proxy(proxies)
 
             meta_data[key] = proxies
 
-        # 处理 headers
+        def decide_domain(key='domain') -> str:
+            nonlocal domain
+            domain = self.client_config.get(key, None)
+            if domain is None:
+                temp_postman = postman_clazz.create(
+                    headers=JmModuleConfig.headers(JmModuleConfig.JM_REDIRECT_URL),
+                    proxies=proxies,
+                )
+                domain = JmModuleConfig.domain(temp_postman)
+
+            domain = JmcomicText.parse_to_jm_domain(domain)
+            self.client_config[key] = domain
+            return domain
+
         def handle_headers(key='headers'):
             headers = meta_data.get(key, None)
             if headers is None or (not isinstance(headers, dict)) or len(headers) == 0:
-                meta_data[key] = JmModuleConfig.default_headers()
+                # 未配置headers，使用默认headers
+                headers = JmModuleConfig.headers()
 
-        # 处理【特殊配置项】
-        handle_proxies()
-        handle_headers()
+            meta_data[key] = headers
 
-        # 决定Postman的实现类，根据配置项 client_config.postman
-        postman_clazz = Postmans.get_impl_clazz(self.client_config.get('postman_type', 'cffi'))
-        # 决定域名
-        domain = self.client_config.get('domain', JmModuleConfig.DOMAIN)
+        def handle_postman():
+            nonlocal postman
+            postman = postman_clazz(meta_data)
+
+        # 1. 决定 代理
+        decide_proxies()
+        # 2. 指定 JM域名
+        decide_domain()
+        # 3. 处理 headers
+        handle_headers()
+        # 4. 创建 postman
+        handle_postman()
 
         jm_debug('创建JmcomicClient', f'使用域名: {domain}，使用Postman实现: {postman_clazz}')
-        # 创建 JmcomicClient 实例
+
+        # 创建 JmcomicClient 对象
         client = JmcomicClient(
-            postman=postman_clazz(meta_data),
+            postman=postman,
             domain=domain,
             retry_times=self.client_config.get('retry_times', None)
         )
 
         return client
 
     """
     下面的方法是对【CdnOption】的支持，已弃用
     """
 
     def build_cdn_option(self, use_multi_thread_strategy=True):
 
         return CdnConfig.create(
-            cdn_domain=self.client_config.get('domain', JmModuleConfig.DOMAIN),
+            cdn_domain=self.client_config.get('domain', JmModuleConfig.domain()),
             fetch_strategy=MultiThreadFetch if use_multi_thread_strategy else InOrderFetch,
             cdn_image_suffix=None,
             use_cache=self.download_use_disk_cache,
             decode_image=self.download_image_then_decode
         )
 
     def build_cdn_crawler(self, use_multi_thread_strategy=True):
```

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_service.py` & `jmcomic-1.5.0/src/jmcomic/jm_service.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.4.0/src/jmcomic/jm_toolkit.py` & `jmcomic-1.5.0/src/jmcomic/jm_toolkit.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.4.0/src/jmcomic.egg-info/PKG-INFO` & `jmcomic-1.5.0/src/jmcomic.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jmcomic
-Version: 1.4.0
+Version: 1.5.0
 Summary: Python API For JMComic (禁漫天堂)
 Home-page: https://github.com/hect0x7/JMComic-Crawler-Python
 Author: hect0x7
 Author-email: 93357912+hect0x7@users.noreply.github.com
 Keywords: python,jmcomic,18comic,禁漫天堂,NSFW
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

