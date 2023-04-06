# Comparing `tmp/ofscraper-1.61.tar.gz` & `tmp/ofscraper-1.62.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ofscraper-1.61.tar", max compression
+gzip compressed data, was "ofscraper-1.62.tar", max compression
```

## Comparing `ofscraper-1.61.tar` & `ofscraper-1.62.tar`

### file list

```diff
@@ -1,37 +1,37 @@
--rw-r--r--   0        0        0     1073 2023-04-06 15:33:38.736121 ofscraper-1.61/LICENSE
--rw-r--r--   0        0        0     9234 2023-04-06 15:33:38.736121 ofscraper-1.61/README.md
--rw-r--r--   0        0        0      801 2023-04-06 16:42:22.123716 ofscraper-1.61/pyproject.toml
--rw-r--r--   0        0        0      620 2023-04-06 15:33:38.742121 ofscraper-1.61/src/__init__.py
--rw-r--r--   0        0        0      751 2023-04-06 16:42:03.484531 ofscraper-1.61/src/__version__.py
--rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/__init__.py
--rw-r--r--   0        0        0     3388 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/highlights.py
--rw-r--r--   0        0        0      755 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/init.py
--rw-r--r--   0        0        0     1815 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/me.py
--rw-r--r--   0        0        0     4236 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/messages.py
--rw-r--r--   0        0        0     2401 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/paid.py
--rw-r--r--   0        0        0     6025 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/posts.py
--rw-r--r--   0        0        0     3166 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/profile.py
--rw-r--r--   0        0        0     2040 2023-04-06 15:33:38.742121 ofscraper-1.61/src/api/subscriptions.py
--rw-r--r--   0        0        0     4100 2023-04-06 16:40:58.038879 ofscraper-1.61/src/constants.py
--rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.61/src/db/__init__.py
--rw-r--r--   0        0        0    11255 2023-04-06 16:27:45.941953 ofscraper-1.61/src/db/operations.py
--rw-r--r--   0        0        0     3198 2023-04-06 15:33:38.742121 ofscraper-1.61/src/db/queries.py
--rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.61/src/interaction/__init__.py
--rw-r--r--   0        0        0     3280 2023-04-06 15:33:38.742121 ofscraper-1.61/src/interaction/like.py
--rwxr-xr-x   0        0        0    20417 2023-04-06 16:29:19.745896 ofscraper-1.61/src/scraper.py
--rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.61/src/utils/__init__.py
--rw-r--r--   0        0        0     7950 2023-04-06 16:40:41.605715 ofscraper-1.61/src/utils/auth.py
--rw-r--r--   0        0        0      694 2023-04-06 15:33:38.742121 ofscraper-1.61/src/utils/browser.py
--rw-r--r--   0        0        0     3428 2023-04-06 15:33:38.742121 ofscraper-1.61/src/utils/config.py
--rw-r--r--   0        0        0      877 2023-04-06 15:33:38.742121 ofscraper-1.61/src/utils/dates.py
--rw-r--r--   0        0        0      372 2023-04-06 15:33:38.742121 ofscraper-1.61/src/utils/decorators.py
--rw-r--r--   0        0        0    16755 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/download.py
--rw-r--r--   0        0        0      609 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/encoding.py
--rw-r--r--   0        0        0       28 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/login.py
--rw-r--r--   0        0        0      418 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/nap.py
--rw-r--r--   0        0        0     3160 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/old_nap.py
--rw-r--r--   0        0        0     1744 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/paths.py
--rw-r--r--   0        0        0     3688 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/profiles.py
--rw-r--r--   0        0        0    13466 2023-04-06 15:38:48.853128 ofscraper-1.61/src/utils/prompts.py
--rw-r--r--   0        0        0      750 2023-04-06 15:33:38.743121 ofscraper-1.61/src/utils/separate.py
--rw-r--r--   0        0        0    10334 1970-01-01 00:00:00.000000 ofscraper-1.61/PKG-INFO
+-rw-r--r--   0        0        0     1073 2023-04-06 15:33:38.736121 ofscraper-1.62/LICENSE
+-rw-r--r--   0        0        0     9234 2023-04-06 15:33:38.736121 ofscraper-1.62/README.md
+-rw-r--r--   0        0        0      801 2023-04-06 16:55:37.365826 ofscraper-1.62/pyproject.toml
+-rw-r--r--   0        0        0      620 2023-04-06 15:33:38.742121 ofscraper-1.62/src/__init__.py
+-rw-r--r--   0        0        0      751 2023-04-06 16:55:37.365826 ofscraper-1.62/src/__version__.py
+-rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/__init__.py
+-rw-r--r--   0        0        0     3388 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/highlights.py
+-rw-r--r--   0        0        0      755 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/init.py
+-rw-r--r--   0        0        0     1815 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/me.py
+-rw-r--r--   0        0        0     4236 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/messages.py
+-rw-r--r--   0        0        0     2401 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/paid.py
+-rw-r--r--   0        0        0     6025 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/posts.py
+-rw-r--r--   0        0        0     3166 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/profile.py
+-rw-r--r--   0        0        0     2040 2023-04-06 15:33:38.742121 ofscraper-1.62/src/api/subscriptions.py
+-rw-r--r--   0        0        0     4100 2023-04-06 16:40:58.038879 ofscraper-1.62/src/constants.py
+-rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.62/src/db/__init__.py
+-rw-r--r--   0        0        0    11255 2023-04-06 16:27:45.941953 ofscraper-1.62/src/db/operations.py
+-rw-r--r--   0        0        0     3198 2023-04-06 15:33:38.742121 ofscraper-1.62/src/db/queries.py
+-rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.62/src/interaction/__init__.py
+-rw-r--r--   0        0        0     3280 2023-04-06 15:33:38.742121 ofscraper-1.62/src/interaction/like.py
+-rwxr-xr-x   0        0        0    20417 2023-04-06 16:29:19.745896 ofscraper-1.62/src/scraper.py
+-rw-r--r--   0        0        0        1 2023-04-06 15:33:38.742121 ofscraper-1.62/src/utils/__init__.py
+-rw-r--r--   0        0        0     7950 2023-04-06 16:40:41.605715 ofscraper-1.62/src/utils/auth.py
+-rw-r--r--   0        0        0      694 2023-04-06 15:33:38.742121 ofscraper-1.62/src/utils/browser.py
+-rw-r--r--   0        0        0     3498 2023-04-06 16:55:20.060649 ofscraper-1.62/src/utils/config.py
+-rw-r--r--   0        0        0      877 2023-04-06 15:33:38.742121 ofscraper-1.62/src/utils/dates.py
+-rw-r--r--   0        0        0      372 2023-04-06 15:33:38.742121 ofscraper-1.62/src/utils/decorators.py
+-rw-r--r--   0        0        0    16759 2023-04-06 16:53:07.544293 ofscraper-1.62/src/utils/download.py
+-rw-r--r--   0        0        0      609 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/encoding.py
+-rw-r--r--   0        0        0       28 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/login.py
+-rw-r--r--   0        0        0      418 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/nap.py
+-rw-r--r--   0        0        0     3160 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/old_nap.py
+-rw-r--r--   0        0        0     1744 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/paths.py
+-rw-r--r--   0        0        0     3688 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/profiles.py
+-rw-r--r--   0        0        0    13466 2023-04-06 15:38:48.853128 ofscraper-1.62/src/utils/prompts.py
+-rw-r--r--   0        0        0      750 2023-04-06 15:33:38.743121 ofscraper-1.62/src/utils/separate.py
+-rw-r--r--   0        0        0    10334 1970-01-01 00:00:00.000000 ofscraper-1.62/PKG-INFO
```

### Comparing `ofscraper-1.61/LICENSE` & `ofscraper-1.62/LICENSE`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/README.md` & `ofscraper-1.62/README.md`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/pyproject.toml` & `ofscraper-1.62/pyproject.toml`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ofscraper"
-version = "1.61"
+version = "1.62"
 description = "automatically scrape onlyfans"
 authors = ["excludedBittern8 <excludedBittern8@riseup.net>"]
 readme = "README.md"
 packages = [{include = "src"}]
 
 [tool.poetry.dependencies]
 python = ">=3.7.0,<4"
```

### Comparing `ofscraper-1.61/src/__init__.py` & `ofscraper-1.62/src/__init__.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/__version__.py` & `ofscraper-1.62/src/__version__.py`

 * *Files 18% similar despite different names*

```diff
@@ -4,14 +4,14 @@
  /  _ \   __\/  ___// ___\_  __ \__  \  /  _ \_/ __ \_  __ \
 (  <_> )  |  \___ \\  \___|  | \// __ \(  <_> )  ___/|  | \/
  \____/|__| /____  >\___  >__|  (____  /\____/ \___  >__|   
                  \/     \/           \/            \/       
 """
 
 __title__ = 'ofscraper'
-__version__ = '1.61'
+__version__ = '1.62'
 __author__ = 'excludedBittern8'
 __author_email__ = 'excludedBittern8@riseup.net'
 __description__ = 'A command-line program to quickly download,like or unlike posts, and more'
 __url__ = 'https://github.com/excludedBittern8/ofscraper'
 __license__ = 'GNU General Public License v3 or later (GPLv3+)'
 __copyright__ = 'Copyright 2023'
```

### Comparing `ofscraper-1.61/src/api/highlights.py` & `ofscraper-1.62/src/api/highlights.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/init.py` & `ofscraper-1.62/src/api/init.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/me.py` & `ofscraper-1.62/src/api/me.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/messages.py` & `ofscraper-1.62/src/api/messages.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/paid.py` & `ofscraper-1.62/src/api/paid.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/posts.py` & `ofscraper-1.62/src/api/posts.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/profile.py` & `ofscraper-1.62/src/api/profile.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/api/subscriptions.py` & `ofscraper-1.62/src/api/subscriptions.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/constants.py` & `ofscraper-1.62/src/constants.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/db/operations.py` & `ofscraper-1.62/src/db/operations.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/db/queries.py` & `ofscraper-1.62/src/db/queries.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/interaction/like.py` & `ofscraper-1.62/src/interaction/like.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/scraper.py` & `ofscraper-1.62/src/scraper.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/auth.py` & `ofscraper-1.62/src/utils/auth.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/browser.py` & `ofscraper-1.62/src/utils/browser.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/config.py` & `ofscraper-1.62/src/utils/config.py`

 * *Files 3% similar despite different names*

```diff
@@ -44,30 +44,30 @@
 
 def get_current_config_schema(config: dict) -> dict:
     config = config['config']
 
     new_config = {
         'config': {
             mainProfile: config.get(mainProfile) or mainProfile,
-            'save_location': config.get('save_location') or '',
+            'save_location': config.get('save_location') or pathlib.Path.home() /'ofscraper/Data',
             'file_size_limit': config.get('file_size_limit') or '',
             'dir_format': config.get("dir_format") or '{model_username}/{responsetype}/{mediatype}/',
             'file_format': config.get('file_format') or '{filename}.{ext}',
             'textlength':config.get('textlength') or 0,
             'date': config.get('date') or  "MM-DD-YYYY"
         }
     }
     return new_config
 
 
 def make_config(path, config):
     config = {
         'config': {
             mainProfile: mainProfile,
-            'save_location': '',
+            'save_location': pathlib.Path.home() /'ofscraper/Data',
             'file_size_limit': '',
             'dir_format':'{model_username}/{responsetype}/{mediatype}/',
             'file_format': '{filename}.{ext}',
             'textlength':0,
             'date':"MM-DD-YYYY"
         }
     }
```

### Comparing `ofscraper-1.61/src/utils/dates.py` & `ofscraper-1.62/src/utils/dates.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/download.py` & `ofscraper-1.62/src/utils/download.py`

 * *Files 0% similar despite different names*

```diff
@@ -58,15 +58,15 @@
         photo_count = 0
         video_count = 0
         audio_count=0
         skipped = 0
         total_bytes_downloaded = 0
         data = 0
         desc = 'Progress: ({p_count} photos, {v_count} videos, {skipped} skipped || {sumcount}/{mediacount}||{data})'    
-        print(f"\nDownloading to {(config.get('save_location') or pathlib.Path.home()/'ofscraper')}/{(config.get('dir_format') or '{model_username}/{responsetype}/{mediatype}')}\n\n")
+        print(f"\nDownloading to {(config.get('save_location') or pathlib.Path.home()/'ofscraper/Data')}{(config.get('dir_format') or '{model_username}/{responsetype}/{mediatype}')}\n\n")
 
         with tqdm(desc=desc.format(p_count=photo_count, v_count=video_count, skipped=skipped,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped,data=data), total=len(aws), colour='cyan', leave=True) as main_bar:   
             for ele in medialist:
                 with set_directory(getmediadir(ele,username,model_id)):
 
                     aws.append(asyncio.create_task(download(ele,pathlib.Path(".").absolute() ,model_id, username,file_size_limit)))
             for coro in asyncio.as_completed(aws):
```

### Comparing `ofscraper-1.61/src/utils/encoding.py` & `ofscraper-1.62/src/utils/encoding.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/old_nap.py` & `ofscraper-1.62/src/utils/old_nap.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/paths.py` & `ofscraper-1.62/src/utils/paths.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/profiles.py` & `ofscraper-1.62/src/utils/profiles.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/prompts.py` & `ofscraper-1.62/src/utils/prompts.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/src/utils/separate.py` & `ofscraper-1.62/src/utils/separate.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.61/PKG-INFO` & `ofscraper-1.62/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ofscraper
-Version: 1.61
+Version: 1.62
 Summary: automatically scrape onlyfans
 Author: excludedBittern8
 Author-email: excludedBittern8@riseup.net
 Requires-Python: >=3.7.0,<4
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

