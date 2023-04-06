# Comparing `tmp/ofscraper-1.51.tar.gz` & `tmp/ofscraper-1.60.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ofscraper-1.51.tar", max compression
+gzip compressed data, was "ofscraper-1.60.tar", max compression
```

## Comparing `ofscraper-1.51.tar` & `ofscraper-1.60.tar`

### file list

```diff
@@ -1,36 +1,37 @@
--rw-r--r--   0        0        0     1073 2023-03-22 21:18:39.850727 ofscraper-1.51/LICENSE
--rw-r--r--   0        0        0     9007 2023-04-03 02:12:11.205809 ofscraper-1.51/README.md
--rw-r--r--   0        0        0      784 2023-04-03 02:14:34.686230 ofscraper-1.51/pyproject.toml
--rw-r--r--   0        0        0      620 2023-03-24 22:29:29.450012 ofscraper-1.51/src/__init__.py
--rw-r--r--   0        0        0      751 2023-04-03 02:14:40.013283 ofscraper-1.51/src/__version__.py
--rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.51/src/api/__init__.py
--rw-r--r--   0        0        0     3347 2023-04-03 01:37:52.645200 ofscraper-1.51/src/api/highlights.py
--rw-r--r--   0        0        0      755 2023-03-29 19:55:39.286146 ofscraper-1.51/src/api/init.py
--rw-r--r--   0        0        0     1815 2023-04-03 02:06:55.444688 ofscraper-1.51/src/api/me.py
--rw-r--r--   0        0        0     1878 2023-04-03 01:37:52.645200 ofscraper-1.51/src/api/messages.py
--rw-r--r--   0        0        0     3122 2023-03-30 16:12:49.474620 ofscraper-1.51/src/api/paid.py
--rw-r--r--   0        0        0     3032 2023-04-03 01:37:52.645200 ofscraper-1.51/src/api/posts.py
--rw-r--r--   0        0        0     3274 2023-03-30 23:30:24.279725 ofscraper-1.51/src/api/profile.py
--rw-r--r--   0        0        0     2040 2023-03-31 00:48:20.726460 ofscraper-1.51/src/api/subscriptions.py
--rw-r--r--   0        0        0     3921 2023-04-03 01:37:52.646200 ofscraper-1.51/src/constants.py
--rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.51/src/db/__init__.py
--rw-r--r--   0        0        0     5779 2023-04-03 01:37:52.646200 ofscraper-1.51/src/db/operations.py
--rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.51/src/interaction/__init__.py
--rw-r--r--   0        0        0     3280 2023-03-29 19:55:39.287146 ofscraper-1.51/src/interaction/like.py
--rwxr-xr-x   0        0        0    18152 2023-04-03 02:05:58.926125 ofscraper-1.51/src/scraper.py
--rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.51/src/utils/__init__.py
--rw-r--r--   0        0        0     7954 2023-04-03 01:55:52.159072 ofscraper-1.51/src/utils/auth.py
--rw-r--r--   0        0        0      694 2023-03-29 19:55:39.287146 ofscraper-1.51/src/utils/browser.py
--rw-r--r--   0        0        0     2957 2023-03-29 19:55:39.287146 ofscraper-1.51/src/utils/config.py
--rw-r--r--   0        0        0      877 2023-03-24 22:29:29.452012 ofscraper-1.51/src/utils/dates.py
--rw-r--r--   0        0        0      372 2023-03-29 19:55:39.288146 ofscraper-1.51/src/utils/decorators.py
--rw-r--r--   0        0        0    13155 2023-04-03 01:37:52.646200 ofscraper-1.51/src/utils/download.py
--rw-r--r--   0        0        0      609 2023-03-24 22:29:29.452012 ofscraper-1.51/src/utils/encoding.py
--rw-r--r--   0        0        0       28 2023-03-16 19:02:39.000000 ofscraper-1.51/src/utils/login.py
--rw-r--r--   0        0        0      418 2023-03-29 19:55:39.288146 ofscraper-1.51/src/utils/nap.py
--rw-r--r--   0        0        0     3160 2023-03-29 19:55:39.288146 ofscraper-1.51/src/utils/old_nap.py
--rw-r--r--   0        0        0      685 2023-04-03 01:37:52.646200 ofscraper-1.51/src/utils/paths.py
--rw-r--r--   0        0        0     3688 2023-03-29 19:55:39.289146 ofscraper-1.51/src/utils/profiles.py
--rw-r--r--   0        0        0    13001 2023-03-30 17:54:31.935056 ofscraper-1.51/src/utils/prompts.py
--rw-r--r--   0        0        0      742 2023-03-24 22:29:29.453012 ofscraper-1.51/src/utils/separate.py
--rw-r--r--   0        0        0    10069 1970-01-01 00:00:00.000000 ofscraper-1.51/PKG-INFO
+-rw-r--r--   0        0        0     1073 2023-03-22 21:18:39.850727 ofscraper-1.60/LICENSE
+-rw-r--r--   0        0        0     8812 2023-04-04 09:33:32.853666 ofscraper-1.60/README.md
+-rw-r--r--   0        0        0      801 2023-04-06 14:02:26.757542 ofscraper-1.60/pyproject.toml
+-rw-r--r--   0        0        0      620 2023-03-24 22:29:29.450012 ofscraper-1.60/src/__init__.py
+-rw-r--r--   0        0        0      751 2023-04-06 14:02:21.940495 ofscraper-1.60/src/__version__.py
+-rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.60/src/api/__init__.py
+-rw-r--r--   0        0        0     3388 2023-04-06 05:47:26.318770 ofscraper-1.60/src/api/highlights.py
+-rw-r--r--   0        0        0      755 2023-03-29 19:55:39.286146 ofscraper-1.60/src/api/init.py
+-rw-r--r--   0        0        0     1724 2023-04-04 09:33:32.854666 ofscraper-1.60/src/api/me.py
+-rw-r--r--   0        0        0     4236 2023-04-06 05:43:48.734663 ofscraper-1.60/src/api/messages.py
+-rw-r--r--   0        0        0     2401 2023-04-06 13:57:13.648470 ofscraper-1.60/src/api/paid.py
+-rw-r--r--   0        0        0     6025 2023-04-06 05:44:32.315085 ofscraper-1.60/src/api/posts.py
+-rw-r--r--   0        0        0     3166 2023-04-06 01:16:42.690579 ofscraper-1.60/src/api/profile.py
+-rw-r--r--   0        0        0     2040 2023-03-31 00:48:20.726460 ofscraper-1.60/src/api/subscriptions.py
+-rw-r--r--   0        0        0     4100 2023-04-04 09:33:32.855666 ofscraper-1.60/src/constants.py
+-rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.60/src/db/__init__.py
+-rw-r--r--   0        0        0    11117 2023-04-05 17:21:49.601071 ofscraper-1.60/src/db/operations.py
+-rw-r--r--   0        0        0     3198 2023-04-04 20:03:08.469290 ofscraper-1.60/src/db/queries.py
+-rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.60/src/interaction/__init__.py
+-rw-r--r--   0        0        0     3280 2023-03-29 19:55:39.287146 ofscraper-1.60/src/interaction/like.py
+-rwxr-xr-x   0        0        0    20448 2023-04-06 13:49:08.561684 ofscraper-1.60/src/scraper.py
+-rw-r--r--   0        0        0        1 2023-03-16 19:02:39.000000 ofscraper-1.60/src/utils/__init__.py
+-rw-r--r--   0        0        0     7960 2023-04-04 09:33:32.857666 ofscraper-1.60/src/utils/auth.py
+-rw-r--r--   0        0        0      694 2023-03-29 19:55:39.287146 ofscraper-1.60/src/utils/browser.py
+-rw-r--r--   0        0        0     3428 2023-04-06 00:31:54.525738 ofscraper-1.60/src/utils/config.py
+-rw-r--r--   0        0        0      877 2023-03-24 22:29:29.452012 ofscraper-1.60/src/utils/dates.py
+-rw-r--r--   0        0        0      372 2023-03-29 19:55:39.288146 ofscraper-1.60/src/utils/decorators.py
+-rw-r--r--   0        0        0    16755 2023-04-06 13:34:38.908085 ofscraper-1.60/src/utils/download.py
+-rw-r--r--   0        0        0      609 2023-03-24 22:29:29.452012 ofscraper-1.60/src/utils/encoding.py
+-rw-r--r--   0        0        0       28 2023-03-16 19:02:39.000000 ofscraper-1.60/src/utils/login.py
+-rw-r--r--   0        0        0      418 2023-03-29 19:55:39.288146 ofscraper-1.60/src/utils/nap.py
+-rw-r--r--   0        0        0     3160 2023-03-29 19:55:39.288146 ofscraper-1.60/src/utils/old_nap.py
+-rw-r--r--   0        0        0     1744 2023-04-04 09:33:32.857666 ofscraper-1.60/src/utils/paths.py
+-rw-r--r--   0        0        0     3688 2023-03-29 19:55:39.289146 ofscraper-1.60/src/utils/profiles.py
+-rw-r--r--   0        0        0    13055 2023-04-04 22:15:17.042628 ofscraper-1.60/src/utils/prompts.py
+-rw-r--r--   0        0        0      750 2023-04-05 18:52:55.016034 ofscraper-1.60/src/utils/separate.py
+-rw-r--r--   0        0        0     9912 1970-01-01 00:00:00.000000 ofscraper-1.60/PKG-INFO
```

### Comparing `ofscraper-1.51/LICENSE` & `ofscraper-1.60/LICENSE`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/README.md` & `ofscraper-1.60/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,12 @@
 This is a fork of onlyfans-scraper with additional features and fixes
 
 Note the guide is still a little incomplete, so it might not be up to date with the changes I made 
 I hope to go through it and make the necessary changes soon.
 
-new db branch has some changes that will be coming to the main branch soon
-https://github.com/excludedBittern8/ofscraper/tree/db
-
-Will be added a feature to speed up repeated scraping of models
-
 <h3>DISCLAIMERS:</h3>
 <ol>
     <li>
         This tool is not affiliated, associated, or partnered with OnlyFans in any way. We are not authorized, endorsed, or sponsored by OnlyFans. All OnlyFans trademarks remain the property of Fenix International Limited.
     </li>
     <li>
         This is a theoritical program only and is for educational purposes. If you choose to use it then it may or may not work. You solely accept full responsability and indemnify the creator, hostors, contributors and all other involved persons from any any all responsability.
```

### Comparing `ofscraper-1.51/pyproject.toml` & `ofscraper-1.60/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ofscraper"
-version = "1.51"
+version = "1.60"
 description = "automatically scrape onlyfans"
 authors = ["excludedBittern8 <excludedBittern8@riseup.net>"]
 readme = "README.md"
 packages = [{include = "src"}]
 
 [tool.poetry.dependencies]
 python = ">=3.7.0,<4"
@@ -15,14 +15,15 @@
 setuptools = "^67.6.0"
 schedule = "^1.1.0"
 browser-cookie3 = "^0.17.1"
 requests = "^2.28.2"
 bs4 = "^0.0.1"
 rich = "^13.3.2"
 tenacity = "^8.2.2"
+arrow = "^1.2.3"
 
 
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry.scripts]
```

### Comparing `ofscraper-1.51/src/__init__.py` & `ofscraper-1.60/src/__init__.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/__version__.py` & `ofscraper-1.60/src/__version__.py`

 * *Files 19% similar despite different names*

```diff
@@ -4,14 +4,14 @@
  /  _ \   __\/  ___// ___\_  __ \__  \  /  _ \_/ __ \_  __ \
 (  <_> )  |  \___ \\  \___|  | \// __ \(  <_> )  ___/|  | \/
  \____/|__| /____  >\___  >__|  (____  /\____/ \___  >__|   
                  \/     \/           \/            \/       
 """
 
 __title__ = 'ofscraper'
-__version__ = '1.51'
+__version__ = '1.60'
 __author__ = 'excludedBittern8'
 __author_email__ = 'excludedBittern8@riseup.net'
 __description__ = 'A command-line program to quickly download,like or unlike posts, and more'
 __url__ = 'https://github.com/excludedBittern8/ofscraper'
 __license__ = 'GNU General Public License v3 or later (GPLv3+)'
 __copyright__ = 'Copyright 2023'
```

### Comparing `ofscraper-1.51/src/api/highlights.py` & `ofscraper-1.60/src/api/highlights.py`

 * *Files 12% similar despite different names*

```diff
@@ -29,34 +29,39 @@
         c.headers.update(auth.create_sign(url_stories, headers))
         r_multiple = c.get(url_stories, timeout=None)
 
         c.headers.update(auth.create_sign(url_story, headers))
         r_one = c.get(url_story, timeout=None)
 
         if not r_multiple.is_error and not r_one.is_error:
-            return r_multiple.json(), r_one.json()
+            return get_highlightList(r_multiple.json()),r_one.json()
 
         r_multiple.raise_for_status()
         r_one.raise_for_status()
 
+def get_highlightList(data):
+    for ele in list(filter(lambda x:isinstance(x,list),data.values())):
+        if len(list(filter(lambda x:isinstance(x.get("id"),int) and data.get("hasMore")!=None,ele)))>0:
+               return ele
+    return []
+
+
+    
+
 
 
 
 def parse_highlights(highlights: list) -> list:
     #This needs further work but will work for now. I was thinking of adding full recurssive ability until all conditions are met.
     #This means that whenever onlyfans changes the name of the list containing the highlights it wont matter because the name is variable.
     #To break this they would have to change the conditions or in this release the layers.
-    temp=[]
-    for item in list(filter(lambda x:isinstance(x,list),highlights.values())):
-        for highlight in list(filter(lambda x:x.get("id") and isinstance(x['id'],int),item)):
-            temp.append(highlight)
-    output=[]
-    for count,item in enumerate(temp):
-        output.append({"id":item["id"],"date":item["createdAt"],"text":item["title"],"responsetype":"highlight","count":count+1,"url":item["cover"],"mediatype":"photo","data":item})
-    return output
+    ids= [highlight['id'] for highlight in highlights]
+    results=asyncio.run(process_highlights_ids(auth.make_headers(auth.read_auth()),ids))
+    return parse_stories(results)
+    
 async def process_highlights_ids(headers, ids: list) -> list:
     if not ids:
         return []
 
     tasks = [scrape_story(headers, id_) for id_ in ids]
     results = await asyncio.gather(*tasks)
     return list(chain.from_iterable(results))
@@ -75,12 +80,12 @@
             return r.json()['stories']
         r.raise_for_status()
 
 
 def parse_stories(stories: list):
     output=[]
     for story in stories:
-        for media in story["media"]:
-            output.append({"url":media["files"]["source"]["url"],"id":media["id"],"date":media["createdAt"],"responsetype":"stories","count":1,"text":None,"mediatype":media["type"],"data":media})
+        for count, media in enumerate(story["media"]):
+            output.append({"url":media["files"]["source"]["url"],"id":media["id"],"date":media["createdAt"],"responsetype":"stories","count":count+1,"text":None,"mediatype":media["type"],"postid":story["id"],"data":media,"value":"free"})
     return output
```

### Comparing `ofscraper-1.51/src/api/init.py` & `ofscraper-1.60/src/api/init.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/api/me.py` & `ofscraper-1.60/src/api/me.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 import httpx
 from rich.console import Console
 console=Console()
 from tenacity import retry,stop_after_attempt,wait_random
 from ..constants import meEP,subscribeCountEP
 from ..utils import auth, encoding
 
-@retry(stop=stop_after_attempt(5),wait=wait_random(min=2, max=6),reraise=True,after=lambda retry_state:print(f"Attempting to login attempt:{retry_state.attempt_number}/5")) 
+@retry(stop=stop_after_attempt(5),wait=wait_random(min=5, max=20),reraise=True)   
 def scrape_user(headers):
     with httpx.Client(http2=True, headers=headers) as c:
         url = meEP
 
         auth.add_cookies(c)
         c.headers.update(auth.create_sign(url, headers))
```

### Comparing `ofscraper-1.51/src/api/profile.py` & `ofscraper-1.60/src/api/profile.py`

 * *Files 12% similar despite different names*

```diff
@@ -30,38 +30,37 @@
         if not r.is_error:
             return r.json()
         r.raise_for_status()
 
 
 def parse_profile(profile: dict) -> tuple:
     media = []
-    if (avatar := profile['avatar']):
-        media.append((avatar,"Profile"))
-    if (header := profile['header']):
-        media.append((header,"Header"))
-    # media_urls = list(zip_longest(media, [], fillvalue=None))
+    media.append(profile.get('avatar'))
+    media.append(profile.get('profile'))
+    media=list(filter(lambda x:x!=None,media))
+
+    output=[]
+    for ele in media:
+        output.append({"url":ele,"responsetype":"profile","mediatype":"images","value":"free","date":profile["joinDate"]})
+
 
     name = encoding.encode_utf_16(profile['name'])
     username = profile['username']
     id_ = profile['id']
     join_date = profile['joinDate']
     posts_count = profile['postsCount']
     photos_count = profile['photosCount']
     videos_count = profile['videosCount']
     audios_count = profile['audiosCount']
     archived_posts_count = profile['archivedPostsCount']
     info = (
         name, username, id_, join_date,
         posts_count, photos_count, videos_count, audios_count, archived_posts_count)
-    output=[]
-                    # ['id', 'date', 'text', 'post-type', 'count', 'url', 'mediatype', 'data']
-    for count,ele in enumerate(media):
-        output.append({})
+  
 
-    
     return output, info
 
 
 
 def print_profile_info(info):
     header_fmt = 'Name: {} | Username: {} | ID: {} | Joined: {}\n'
     info_fmt = '- {} posts\n -- {} photos\n -- {} videos\n -- {} audios\n- {} archived posts'
```

### Comparing `ofscraper-1.51/src/api/subscriptions.py` & `ofscraper-1.60/src/api/subscriptions.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/constants.py` & `ofscraper-1.60/src/constants.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,44 +16,45 @@
 requestAuth = 'request_auth.json'
 debug = False
 
 # LIST NAMES (IF HARDCODED, MOST WILL BE AUTOMATIC
 
 of_posts_list_name = 'list'
 
+
 initEP = 'https://onlyfans.com/api2/v2/init'
 
 meEP = 'https://onlyfans.com/api2/v2/users/me'
 
 subscriptionsEP = 'https://onlyfans.com/api2/v2/subscriptions/subscribes?offset={}&type=all&sort=asc&field=expire_date&limit=10'
 subscribeCountEP='https://onlyfans.com/api2/v2/subscriptions/count/all'
 profileEP = 'https://onlyfans.com/api2/v2/users/{}'
 
-timelineEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_desc&skip_users=all&skip_users_dups=1&pinned=0&format=infinite'
-timelineNextEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_desc&skip_users=all&skip_users_dups=1&beforePublishTime={}&pinned=0&format=infinite'
-timelinePinnedEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=10&order=publish_date_desc&skip_users=all&skip_users_dups=1&pinned=1&format=infinite'
-
-archivedEP = 'https://onlyfans.com/api2/v2/users/{}/posts/archived?limit=10&order=publish_date_desc&skip_users=all&skip_users_dups=1&format=infinite'
-archivedNextEP = 'https://onlyfans.com/api2/v2/users/{}/posts/archived?limit=10&order=publish_date_desc&skip_users=all&skip_users_dups=1&beforePublishTime={}&format=infinite'
+timelineEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&pinned=0&format=infinite'
+timelineNextEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&afterPublishTime={}&pinned=0&format=infinite'
+timelinePinnedEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&pinned=1&format=infinite'
+timelinePinnedNextEP = 'https://onlyfans.com/api2/v2/users/{}/posts?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&pinned=1&afterPublishTime={}&format=infinite'
+archivedEP = 'https://onlyfans.com/api2/v2/users/{}/posts/archived?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&format=infinite'
+archivedNextEP = 'https://onlyfans.com/api2/v2/users/{}/posts/archived?limit=100&order=publish_date_asc&skip_users=all&skip_users_dups=1&afterPublishTime={}&format=infinite'
 
 highlightsWithStoriesEP = 'https://onlyfans.com/api2/v2/users/{}/stories/highlights?limit=5&offset=0&unf=1'
 highlightsWithAStoryEP = 'https://onlyfans.com/api2/v2/users/{}/stories?unf=1'
 storyEP = 'https://onlyfans.com/api2/v2/stories/highlights/{}?unf=1'
 
-messagesEP = 'https://onlyfans.com/api2/v2/chats/{}/messages?limit=10&offset=0&order=desc&skip_users=all&skip_users_dups=1'
-messagesNextEP = 'https://onlyfans.com/api2/v2/chats/{}/messages?limit=10&offset=0&id={}&order=desc&skip_users=all&skip_users_dups=1'
+messagesEP = 'https://onlyfans.com/api2/v2/chats/{}/messages?limit=100&offset=0&order=desc&skip_users=all&skip_users_dups=1'
+messagesNextEP = 'https://onlyfans.com/api2/v2/chats/{}/messages?limit=100&offset=0&id={}&order=desc&skip_users=all&skip_users_dups=1'
 
 favoriteEP = 'https://onlyfans.com/api2/v2/posts/{}/favorites/{}'
 postURL = 'https://onlyfans.com/{}/{}'
 
 DC_EP = 'https://raw.githubusercontent.com/DATAHOARDERS/dynamic-rules/main/onlyfans.json'
 
 donateEP = "https://www.buymeacoffee.com/excludedBittern"
 
-purchased_contentEP = "https://onlyfans.com/api2/v2/posts/paid?limit=10&skip_users=all&format=infinite&offset={}&user_id={}"
+purchased_contentEP = "https://onlyfans.com/api2/v2/posts/paid?limit=100&skip_users=all&format=infinite&offset={}&user_id={}"
 
 mainPromptChoices = {
     'Download content from a user': 0,
     'Like all of a user\'s posts': 1,
     'Unlike all of a user\'s posts': 2,
     'Migrate an old database': 3,
     'Edit `auth.json` file': 4,
```

### Comparing `ofscraper-1.51/src/interaction/like.py` & `ofscraper-1.60/src/interaction/like.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/scraper.py` & `ofscraper-1.60/src/scraper.py`

 * *Files 8% similar despite different names*

```diff
@@ -38,104 +38,122 @@
 from .__version__ import  __version__
 
 
 
 
 
 
-# @need_revolution("Getting messages...")
 @Revolution(desc='Getting messages...')
-def process_messages(headers, model_id):
-    messages_ = messages.scrape_messages(headers, model_id)
+def process_messages(headers, model_id,username):
+    messages_ =asyncio.run(messages.get_messages(headers,  model_id,username)) 
+    operations.save_messages_response( model_id,username,messages_)
+    for message in messages_:
+     operations.write_messages_table(message,model_id,username)
     output=[]
     if messages_:
-        [output.extend(messages.parse_messages([ele],model_id)) for ele in messages_]       
+        [output.extend(messages.parse_messages([ele],model_id)) for ele in messages_] 
+        list(map(lambda x:mediaJsonHelper(x),output))      
     return output
 
 # @need_revolution("Getting highlights...")
 @Revolution(desc='Getting highlights and stories...')
-def process_highlights(headers, model_id):
+def process_highlights(headers, model_id,username):
     highlights_, stories = highlights.scrape_highlights(headers, model_id)
-    highlight_list=highlights.parse_highlights(highlights_)
-    stories_list=highlights.parse_stories(stories)
+    for post in highlights_:
+        operations.write_stories_table(post,model_id,username)
+    for post in stories:
+        operations.write_stories_table(post,model_id,username)    
+
+    highlight_list=list(map(lambda x:mediaJsonHelper(x),highlights.parse_highlights(highlights_)))
+    stories_list=list(map(lambda x:mediaJsonHelper(x),highlights.parse_stories(stories)))
+   
+
     return highlight_list,stories_list
 
 
 
 
 # @need_revolution("Getting subscriptions...")
 @Revolution(desc='Getting archived media...')
-def process_archived_posts(headers, model_id):
-    archived_posts = posts.scrape_archived_posts(headers, model_id)
-    if archived_posts:
-        archived_posts_urls = posts.parse_posts(archived_posts)
-        return archived_posts_urls
-    return []
+def process_archived_posts(headers, model_id,username):
+    archived_posts = posts.get_archive_post(headers, model_id)
+    operations.save_archive_response(model_id,username,archived_posts)
+    for post in archived_posts:
+        responseJsonHelper(post)
+        operations.write_post_table(post,model_id,username)
+    return list(map(lambda x:mediaJsonHelper(x),posts.parse_posts(archived_posts)))
+
 
 # @need_revolution("Getting timeline media...")
 @Revolution(desc='Getting timeline media...')
-def process_timeline_posts(headers, model_id):
-    timeline_posts = posts.scrape_timeline_posts(headers, model_id)
-    if timeline_posts:
-        timeline_posts_urls = posts.parse_posts(timeline_posts)
-        return timeline_posts_urls
-    return []
+def process_timeline_posts(headers, model_id,username):
+    timeline_posts = asyncio.run(posts.get_timeline_post(headers, model_id,username))
+    operations.save_timeline_response(model_id,username,timeline_posts)
+    for post in timeline_posts:
+        responseJsonHelper(post)
+        operations.write_post_table(post,model_id,username)
+    return list(map(lambda x:mediaJsonHelper(x),posts.parse_posts(timeline_posts)))
+
 
 
 # @need_revolution("Getting pinned media...")
 @Revolution(desc='Getting pinned media...')
-def process_pinned_posts(headers, model_id):
-    pinned_posts = posts.scrape_pinned_posts(headers, model_id)
-    if pinned_posts:
-        pinned_posts_urls = posts.parse_posts(pinned_posts)
-        return pinned_posts_urls
-    return []
+def process_pinned_posts(headers, model_id,username):
+    pinned_posts = posts.get_pinned_post(headers, model_id,username)
+    operations.save_pinned_response(model_id,username, pinned_posts)
+    for post in  pinned_posts:
+        responseJsonHelper(post)
+        operations.write_post_table(post,model_id,username)
+    timeline_posts_urls = posts.parse_posts( pinned_posts)
+    return list(map(lambda x:mediaJsonHelper(x),posts.parse_posts(timeline_posts_urls)))
+
+
 
 
 def process_profile(headers, username) -> list:
     user_profile = profile.scrape_profile(headers, username)
     urls, info = profile.parse_profile(user_profile)
     profile.print_profile_info(info)
     return urls
 
 
 
 
 def process_areas(headers, ele, model_id,selected=None) -> list:
     result_areas_prompt = list(map(lambda x:x.capitalize(),(selected or prompts.areas_prompt())
 ))
-    pinned_posts_dicts = []
     timeline_posts_dicts  = []
+    pinned_post_dict=[]
     archived_posts_dicts  = []
     highlights_dicts  = []
     messages_dicts  = []
     stories_dicts=[]
 
-    # profile_dicts  = process_profile(headers, ele["name"])
-    profile_dicts=[]
+    username=ele['name']
+    profile_dicts  = process_profile(headers,username)
 
-    if ('Timeline' in result_areas_prompt or 'All' in result_areas_prompt) and ele["active"]:
-            pinned_posts_dicts= process_pinned_posts(headers, model_id)
-            timeline_posts_dicts = process_timeline_posts(headers, model_id)
 
+    if ('Timeline' in result_areas_prompt or 'All' in result_areas_prompt) and ele["active"]:
+            timeline_posts_dicts = process_timeline_posts(headers, model_id,username)
+            pinned_post_dict=process_pinned_posts(headers, model_id,username)
     if ('Archived' in result_areas_prompt or 'All' in result_areas_prompt) and ele["active"]:
-            archived_posts_dicts = process_archived_posts(headers, model_id)
+            archived_posts_dicts = process_archived_posts(headers, model_id,username)
     if 'Messages' in result_areas_prompt or 'All' in result_areas_prompt:
-            messages_dicts = process_messages(headers, model_id)
+            messages_dicts = process_messages(headers, model_id,username)
 
     if ('Highlights'  in result_areas_prompt or 'Stories'  in result_areas_prompt or 'All' in result_areas_prompt)   and ele["active"]:
-            highlights_tuple = process_highlights(headers, model_id)
+            highlights_tuple = process_highlights(headers, model_id,username)
             if 'All' in result_areas_prompt:
                 highlights_dicts=highlights_tuple[0]
                 stories_dicts=highlights_tuple[1]    
             elif 'Highlights'  in result_areas_prompt:
                 highlights_dicts=highlights_tuple[0]
             elif 'Stories'  in result_areas_prompt:
                 stories_dicts=highlights_tuple[1]    
-    return list(chain(*[profile_dicts ,pinned_posts_dicts , timeline_posts_dicts ,
+    return list(chain(*[profile_dicts  , timeline_posts_dicts ,pinned_post_dict,
             archived_posts_dicts , highlights_dicts , messages_dicts,stories_dicts]))
 
 
 
 
 
 
@@ -171,15 +189,15 @@
     with Revolution(desc='Getting your subscriptions (this may take awhile)...') as _:
         list_subscriptions = asyncio.run(
             subscriptions.get_subscriptions(headers, subscribe_count))
         parsed_subscriptions = subscriptions.parse_subscriptions(
             list_subscriptions)
     return parsed_subscriptions
 
-
+#check if auth is valid
 def process_me(headers):
     my_profile = me.scrape_user(headers)
     name, username = me.parse_user(my_profile)
     subscribe_count=me.parse_subscriber_count(headers)
     me.print_user(name, username)
     return subscribe_count
 
@@ -269,68 +287,89 @@
 
     init.print_sign_status(headers)
     userdata=getselected_usernames()
     for ele in userdata:
         print(f"Getting paid content for {ele['name']}")
         try:
             model_id = profile.get_id(headers, ele["name"])
-            paid_content=paid.scrape_paid(ele["name"])
-            paid_url=paid.parse_paid(paid_content)
+            create_tables(model_id,ele['name'])
+            operations.write_profile_table(model_id,ele['name'])
+            paid_url=process_paid_post(model_id,ele['name'])
             profile.print_paid_info(paid_url,ele["name"])
             asyncio.run(download.process_dicts_paid(
-            headers,
             ele["name"],
             model_id,
             paid_url,
             forced=args.dupe,
-            outpath=args.outpath
             ))
         except Exception as e:
             console.print("run failed with exception: ", e)
 
-
+def process_paid_post(model_id,username):
+    paid_content=paid.scrape_paid(username)
+    for post in paid_content:
+        responseJsonHelper(post)
+        operations.write_post_table(post,model_id,username)
+    return list(map(lambda x:mediaJsonHelper(x),paid.parse_paid(paid_content)))
+def responseJsonHelper(data):
+    if data.get("responseType")=="post":
+        data["responseType"]="posts"
+    elif data.get("responseType")=="message":
+        data["responseType"]="messages"
+    return data
+def mediaJsonHelper(data):
+    if data.get("mediatype")=="photo" or data.get("mediatype")=="gif" :
+        data["mediatype"]="images"
+    elif data.get("mediatype")=="audio":
+        data["mediatype"]="audios"
+    elif data.get("mediatype")=="video":
+        data["mediatype"]="videos"
+    return data         
 def process_post():
     profiles.print_current_profile()
     headers = auth.make_headers(auth.read_auth())
     init.print_sign_status(headers)
     userdata=getselected_usernames()
     for ele in userdata:
         print(f"Getting Selected post type(s) for {ele['name']}\nSubscription Active: {ele['active']}")
         try:
             model_id = profile.get_id(headers, ele["name"])
+            create_tables(model_id,ele['name'])
+            operations.write_profile_table(model_id,ele['name'])
             combined_urls=process_areas(headers, ele, model_id,selected=args.posts)
             asyncio.run(download.process_dicts(
-            headers,
             ele["name"],
             model_id,
             combined_urls,
             forced=args.dupe,
             outpath=args.outpath
             ))
         except Exception as e:
             console.print("run failed with exception: ", e)
     
     
 
 def process_like():
     profiles.print_current_profile()
     headers = auth.make_headers(auth.read_auth())
-    init.print_sign_status(headers)
+
     userdata=getselected_usernames()
     for ele in list(filter(lambda x: x["active"],userdata)):
             model_id = profile.get_id(headers, ele["name"])
             posts = like.get_posts(headers, model_id)
             unfavorited_posts = like.filter_for_unfavorited(posts)
             post_ids = like.get_post_ids(unfavorited_posts)
             like.like(headers, model_id, ele["name"], post_ids)
 
 def process_unlike():
     profiles.print_current_profile()
     headers = auth.make_headers(auth.read_auth())
-    init.print_sign_status(headers)
+    if init.print_sign_status(headers)=="DOWN":
+        auth.make_auth(auth=auth.read_auth())
+        headers = auth.make_headers(auth.read_auth())
     userdata=getselected_usernames()
     for ele in list(filter(lambda x: x["active"],userdata)):
             model_id = profile.get_id(headers, ele["name"])
             posts = like.get_posts(headers, model_id)
             favorited_posts = like.filter_for_favorited(posts)
             post_ids = like.get_post_ids(favorited_posts)
             like.unlike(headers, model_id, ele["name"], post_ids)
@@ -355,15 +394,15 @@
         time.sleep(30)
 
 
 ## run script once or on schedule based on args
 def run(command,*params,**kwparams):
     # get usernames prior to potentially supressing output
     getselected_usernames()
-    console.print(f"starting script daemon:{args.daemon!=None} silent-mode:{args.silent}")    
+    console.print(f"starting script daemon: {args.daemon!=None} silent-mode: {args.silent}")    
     if args.silent:
         with suppress_stdout():
             run_helper(command,*params,**kwparams)
     else:
         run_helper(command,*params,**kwparams)
     console.print("script finished")
 
@@ -375,26 +414,15 @@
         worker_thread = threading.Thread(target=set_schedule,args=[command,*params],kwargs=kwparams)
         worker_thread.start()
         while True:
             job_func = jobqueue.get()
             job_func()
             jobqueue.task_done()
                 
-def checkAuth():
-    status=None
-    while status!="UP":
-        headers = auth.make_headers(auth.read_auth())
-        status=init.print_sign_status(headers)
-        if status=="DOWN":
-            auth.make_auth(auth=auth.read_auth())
-            continue
-        break
-        
-    
-
+      
        
 
 def getselected_usernames():
     #username list will be retrived once per run
     global selectedusers
     if selectedusers:
         return selectedusers
@@ -406,15 +434,15 @@
     filter_subscriptions=filteruserHelper(parsed_subscriptions )
     if args.username and "ALL" in args.username:
         selectedusers=filter_subscriptions
     
 
     elif args.username:
         userSelect=set(args.username)
-        selectedusers=list(filter(lambda x:x in userSelect,filter_subscriptions))
+        selectedusers=list(filter(lambda x:x["name"] in userSelect,filter_subscriptions))
     #manually select usernames
     else:
         selectedusers= get_model(filter_subscriptions)
     #remove dupes
     return selectedusers
 def filteruserHelper(usernames):
     #paid/free
@@ -430,17 +458,25 @@
     if args.sub_status=="active":
         filterusername=list(filter(lambda x:x["data"]["subscribedIsExpiredNow"]==False,filterusername))     
     if args.sub_status=="expired":
         filterusername=list(filter(lambda x:x["data"]["subscribedIsExpiredNow"]==True,filterusername))      
     return filterusername
 
 
+def create_tables(model_id,username):
+    operations.create_post_table(model_id,username)
+    operations.create_message_table(model_id,username)
+    operations.create_media_table(model_id,username)
+    operations.create_products_table(model_id,username)
+    operations.create_others_table(model_id,username)
+    operations.create_profile_table(model_id,username)
+    operations.create_stories_table(model_id,username)
+
+
 
-#force auth 
-checkAuth()
 def main():
     global args
     if platform.system == 'Windows':
         os.system('color')
     # try:
     #     webbrowser.open(donateEP)
     # except:
@@ -464,15 +500,15 @@
     general.add_argument(
         '-s', '--silent', help = 'mute output', action = 'store_true',default=False
     )
     post=parser.add_argument_group("Post",description="What type of post to scrape")                                      
 
     post.add_argument("-e","--dupe",action="store_true",default=False,help="Bypass the dupe check and redownload all files")
     post.add_argument(
-        '-o', '--posts', help = 'Download content from a models wall',default=None,required=False,type = str.lower,choices=["highlights","all","archived","messages","timeline","stories"],nargs="+"
+        '-o', '--posts', help = 'Download content from a models wall',default=None,required=False,type = str.lower,choices=["highlights","all","archived","messages","timeline","stories"],nargs="*"
     )
     post.add_argument("-p","--purchased",action="store_true",default=False,help="Download individually purchased content")
     post.add_argument("-a","--action",default=None,help="perform like or unlike action on each post",choices=["like","unlike"])
 
      #Filters for accounts
     filters=parser.add_argument_group("filters",description="Filters out usernames based on selected parameters")
     
@@ -495,17 +531,19 @@
     args = parser.parse_args()
     global selectedusers
     selectedusers=None
     if len(list(filter(lambda x:x!=None and x!=False,[args.action,args.purchased,args.posts])))==0:
         process_prompts()
         sys.exit(0)
     
-    #force off
-    
-   #process user selected option
+
+   #check auth
+   
+    if init.print_sign_status(auth.make_headers(auth.read_auth()))=="DOWN":
+        auth.make_auth(auth=auth.read_auth())
 
 
     if args.posts: 
         run(process_post)        
     if args.purchased:
         run(process_paid)
     if args.action=="like":
```

### Comparing `ofscraper-1.51/src/utils/auth.py` & `ofscraper-1.60/src/utils/auth.py`

 * *Files 0% similar despite different names*

```diff
@@ -69,15 +69,15 @@
     except FileNotFoundError:
         if ask_make_auth_prompt():
             make_auth(p)
 
 
 def make_auth(path=None, auth=None):
     path= path or  pathlib.Path.home() / configPath / get_current_profile()
-    defaultAuth=  {
+    defaultAuth= auth = {
             'auth': {
                 'app-token': '33d57ade8c02dbc5a333db99ff9ae26a',
                 'sess': '',
                 'auth_id': '',
                 'auth_uid_': '',
                 'user_agent': '',
                 'x-bc': ''
```

### Comparing `ofscraper-1.51/src/utils/browser.py` & `ofscraper-1.60/src/utils/browser.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/utils/config.py` & `ofscraper-1.60/src/utils/config.py`

 * *Files 12% similar despite different names*

```diff
@@ -46,25 +46,33 @@
     config = config['config']
 
     new_config = {
         'config': {
             mainProfile: config.get(mainProfile) or mainProfile,
             'save_location': config.get('save_location') or '',
             'file_size_limit': config.get('file_size_limit') or '',
+            'dir_format': config.get("dir_format") or '{model_username}/{responsetype}/{mediatype}/',
+            'file_format': config.get('file_format') or '{filename}.{ext}',
+            'textlength':config.get('textlength') or 0,
+            'date': config.get('date') or  "MM-DD-YYYY"
         }
     }
     return new_config
 
 
 def make_config(path, config):
     config = {
         'config': {
             mainProfile: mainProfile,
             'save_location': '',
-            'file_size_limit': ''
+            'file_size_limit': '',
+            'dir_format':'{model_username}/{responsetype}/{mediatype}/',
+            'file_format': '{filename}.{ext}',
+            'textlength':0,
+            'date':"MM-DD-YYYY"
         }
     }
 
     with open(path / configFile, 'w') as f:
         f.write(json.dumps(config, indent=4))
```

### Comparing `ofscraper-1.51/src/utils/dates.py` & `ofscraper-1.60/src/utils/dates.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/utils/download.py` & `ofscraper-1.60/src/utils/download.py`

 * *Files 20% similar despite different names*

```diff
@@ -10,241 +10,285 @@
 
 import asyncio
 import math
 import pathlib
 import platform
 import sys
 import shutil
-
+import traceback
+import re
 import httpx
+import os
 from rich.console import Console
 console=Console()
 from tqdm.asyncio import tqdm
+import arrow
 try:
     from win32_setctime import setctime  # pylint: disable=import-error
 except ModuleNotFoundError:
     pass
 from tenacity import retry,stop_after_attempt,wait_random
 
 from .auth import add_cookies
 from .config import read_config
-from .dates import convert_date_to_timestamp
 from .separate import separate_by_id
 from ..db import operations
 from .paths import set_directory
 from ..utils import auth
+from ..constants import configPath
+from ..utils.profiles import get_current_profile
+
 
 
 config = read_config()['config']
 
 
-async def process_dicts(headers, username, model_id, medialist,forced=False,outpath=None):
+async def process_dicts(username, model_id, medialist,forced=False,outpath=None):
     if medialist:
-        operations.create_database(model_id)
         if not forced:
-            media_ids = operations.get_media_ids(model_id)
+            media_ids = set(operations.get_media_ids(model_id,username))
             medialist = separate_by_id(medialist, media_ids)
-            console.print(f"Skipping previously downloaded\nPosts left for download {len(medialist)}")
+            console.print(f"Skipping previously downloaded\nMedia left for download {len(medialist)}")
         else:
             print("forcing all downloads")
         file_size_limit = config.get('file_size_limit')
         global sem
         sem = asyncio.Semaphore(8)
-        async with httpx.AsyncClient(headers=headers, timeout=None) as c:
-            add_cookies(c)
-            aws=[]
-            photo_count = 0
-            video_count = 0
-            skipped = 0
-            total_bytes_downloaded = 0
-            data = 0
-            desc = 'Progress: ({p_count} photos, {v_count} videos, {skipped} skipped || {data})'    
-            root= pathlib.Path((outpath or config.get('save_location') or pathlib.Path.cwd()))
-            print(f"Downloading to {pathlib.Path(root,username)}")
-            with tqdm(desc=desc.format(p_count=photo_count, v_count=video_count, skipped=skipped, data=data), total=len(aws), colour='cyan', leave=True) as main_bar:   
-                for ele in medialist:
-                    urldictHelper(ele)
-                    filename=createfilename(ele["url"],username,model_id,ele["date"],ele["id"],ele["mediatype"],ele["text"],ele["count"])
-                    with set_directory(str(pathlib.Path(root,username,ele["responsetype"].capitalize(),ele["mediatype"].capitalize()))):
-                        aws.append(asyncio.create_task(download(c,ele["url"],filename,pathlib.Path(".").absolute() ,ele["mediatype"],model_id, file_size_limit, ele["date"],ele["id"],forced=False)))
-                for coro in asyncio.as_completed(aws):
-                        try:
-                            media_type, num_bytes_downloaded = await coro
-                        except Exception as e:
-                            media_type = None
-                            num_bytes_downloaded = 0
-                            console.print(e)
-
-                        total_bytes_downloaded += num_bytes_downloaded
-                        data = convert_num_bytes(total_bytes_downloaded)
-
-                        if media_type == 'photo' or media_type == "gif":
-                            photo_count += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
-
-                        elif media_type == 'video':
-                            video_count += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
-
-                        elif media_type == 'skipped':
-                            skipped += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
+      
+        aws=[]
+        photo_count = 0
+        video_count = 0
+        audio_count=0
+        skipped = 0
+        total_bytes_downloaded = 0
+        data = 0
+        desc = 'Progress: ({p_count} photos, {v_count} videos, {skipped} skipped || {sumcount}/{mediacount}||{data})'    
+        print(f"\nDownloading to {(config.get('save_location') or pathlib.Path.home()/'ofscraper')}/{(config.get('dir_format') or '{model_username}/{responsetype}/{mediatype}')}\n\n")
+
+        with tqdm(desc=desc.format(p_count=photo_count, v_count=video_count, skipped=skipped,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped,data=data), total=len(aws), colour='cyan', leave=True) as main_bar:   
+            for ele in medialist:
+                with set_directory(getmediadir(ele,username,model_id)):
+
+                    aws.append(asyncio.create_task(download(ele,pathlib.Path(".").absolute() ,model_id, username,file_size_limit)))
+            for coro in asyncio.as_completed(aws):
+                    try:
+                        media_type, num_bytes_downloaded = await coro
+                    except Exception as e:
+                        media_type = None
+                        num_bytes_downloaded = 0
+                        console.print(e)
+
+                    total_bytes_downloaded += num_bytes_downloaded
+                    data = convert_num_bytes(total_bytes_downloaded)
+                    if media_type == 'images':
+                        photo_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=True)
+
+                    elif media_type == 'videos':
+                        video_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=True)
+
+                    elif media_type == 'audios':
+                        audio_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=True)
+
+                    elif media_type == 'skipped':
+                        skipped += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=True)
 
-                        main_bar.update()
+                    main_bar.update()
 
 
 def convert_num_bytes(num_bytes: int) -> str:
     if num_bytes == 0:
       return '0 B'
     num_digits = int(math.log10(num_bytes)) + 1
 
     if num_digits >= 10:
         return f'{round(num_bytes / 10**9, 2)} GB'
     return f'{round(num_bytes / 10 ** 6, 2)} MB'
 
-@retry(stop=stop_after_attempt(5),wait=wait_random(min=20, max=40),reraise=True)   
-async def download(client,url,filename,path,media_type,model_id,file_size_limit,date=None,id_=None,forced=False):
-    async with sem:  
-        async with client.stream('GET',url) as r:
-            if not r.is_error:
-                rheaders=r.headers
-                total = int(rheaders['Content-Length'])
-                if file_size_limit and total > int(file_size_limit): 
-                        return 'skipped', 1       
-                content_type = rheaders.get("content-type").split('/')[-1]
-                path_to_file = pathlib.Path(path,f"{filename}.{content_type}")
-                with set_directory(pathlib.Path(pathlib.Path(__file__).parents[2],".tempmedia")):
-                    temp=f"{filename}.{content_type}"
-                    pathlib.Path(temp).unlink(missing_ok=True)
-                    with open(temp, 'wb') as f:
-                        with tqdm(desc=temp ,total=total, unit_scale=True, unit_divisor=1024, unit='B', leave=False) as bar:
-                            num_bytes_downloaded = r.num_bytes_downloaded
-                            async for chunk in r.aiter_bytes(chunk_size=1024):
-                                f.write(chunk)
-                                bar.update(
-                                    r.num_bytes_downloaded - num_bytes_downloaded)
+@retry(stop=stop_after_attempt(5),wait=wait_random(min=20, max=40),reraise=True)  
+async def download(ele,path,model_id,username,file_size_limit,id_=None):
+    url=ele['url']
+    media_type=ele['mediatype']
+    id_=ele.get("id")
+    bar=None
+    temp=None
+
+    try:
+        async with sem:
+            async with httpx.AsyncClient(http2=True, headers = auth.make_headers(auth.read_auth()), follow_redirects=True, timeout=None) as c: 
+                auth.add_cookies(c)        
+                async with c.stream('GET',url) as r:
+                    if not r.is_error:
+                        rheaders=r.headers
+                        total = int(rheaders['Content-Length'])
+                        if file_size_limit and total > int(file_size_limit): 
+                                return 'skipped', 1       
+                        content_type = rheaders.get("content-type").split('/')[-1]
+                        filename=createfilename(ele,username,model_id,content_type)
+                        path_to_file = trunicate(pathlib.Path(path,f"{filename}"))
+                        with set_directory(pathlib.Path(pathlib.Path.home(),configPath,get_current_profile(),".tempmedia")):
+                            temp=trunicate(f"{filename}")
+                            pathlib.Path(temp).unlink(missing_ok=True)
+                            with open(temp, 'wb') as f:
+                                pathstr=str(temp)
+                                bar=tqdm(desc=(pathstr[:50] + '....') if len(pathstr) > 50 else pathstr ,total=total, unit_scale=True, unit_divisor=1024, unit='B', leave=False)
                                 num_bytes_downloaded = r.num_bytes_downloaded
-                 
-                    
-                    if pathlib.Path(temp).exists() and(total-pathlib.Path(temp).stat().st_size<=1000):
-                        shutil.move(temp,path_to_file)
-                        if date:
-                            set_time(path_to_file, convert_date_to_timestamp(date))
-
-                        if id_:
-                            data = (id_, filename)
-                            operations.write_from_data(data, model_id)
-                        return media_type,total
+                                async for chunk in r.aiter_bytes(chunk_size=1024):
+                                    f.write(chunk)
+                                    bar.update(
+                                        r.num_bytes_downloaded - num_bytes_downloaded)
+                                    num_bytes_downloaded = r.num_bytes_downloaded
+                        
+                            
+                            if pathlib.Path(temp).exists() and  abs(total-pathlib.Path(temp).stat().st_size)<=1000:
+                                shutil.move(temp,path_to_file)
+                                if id_:
+                                    operations.write_media(ele,path_to_file,model_id,username)
+                                return media_type,total
+                            else:
+                                return 'skipped', 1
                     else:
-                        return 'skipped', 1
-            else:
-                r.raise_for_status()
+                        r.raise_for_status()
+    except Exception as e:
+        if not r or r.status_code==200:
+            print(traceback.format_exc())
+        return 'skipped', 1
+    finally:
+        if bar:
+            bar.close()
+        if temp:
+            pathlib.Path(temp).unlink(missing_ok=True)
+        
 
-async def process_dicts_paid(headers,username,model_id,medialist,forced=False,outpath=None):
+async def process_dicts_paid(username,model_id,medialist,forced=False):
  """Takes a list of purchased content and downloads it."""
  if medialist:
-        operations.create_paid_database(model_id)
         if not forced:
-            media_ids = operations.get_paid_media_ids(model_id)
+            media_ids = set(operations.get_media_ids(model_id,username))
             medialist = separate_by_id(medialist, media_ids)
-            console.print(f"Skipping previously downloaded\nPaid content left for download {len(medialist)}")
+            console.print(f"Skipping previously downloaded\nPaid media content left for download {len(medialist)}")
         else:
             print("forcing all downloads")
         file_size_limit = config.get('file_size_limit')
         global sem
         sem = asyncio.Semaphore(8)
-        # Added pool limit:
-        async with httpx.AsyncClient(http2=True, headers=headers, follow_redirects=True, timeout=None) as c: 
-            auth.add_cookies(c)
-            aws=[]
-            photo_count = 0
-            video_count = 0
-            skipped = 0
-            total_bytes_downloaded = 0
-            data = 0
-            desc = 'Progress: ({p_count} photos, {v_count} videos, {skipped} skipped || {data})'   
-            root= pathlib.Path((outpath or config.get('save_location') or pathlib.Path.cwd()))
-            print(f"Downloading to {pathlib.Path(root,username)}")
-            with tqdm(desc=desc.format(p_count=photo_count, v_count=video_count, skipped=skipped, data=data), total=len(aws), colour='cyan', leave=True) as main_bar: 
-                for ele in medialist:
-                    urldictHelper(ele)
-                    filename=createfilename(ele["url"],username,model_id,ele["date"],ele["id"],ele["mediatype"],ele["text"],ele["count"])
-                    with set_directory(pathlib.Path(root,username, "Paid",ele["mediatype"].capitalize())):
-                        aws.append(asyncio.create_task(download_paid(c,ele["url"],filename,pathlib.Path(".").absolute(),ele["mediatype"],model_id, file_size_limit,ele["id"]
-                        ,forced=forced)))
-                for coro in asyncio.as_completed(aws):
-                        try:
-                            media_type, num_bytes_downloaded = await coro
-                        except Exception as e:
-                            media_type = None
-                            num_bytes_downloaded = 0
-                            console.print(e)
-
-                        total_bytes_downloaded += num_bytes_downloaded
-                        data = convert_num_bytes(total_bytes_downloaded)
-
-                        if media_type == 'photo' or media_type == "gif":
-                            photo_count += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
-
-                        elif media_type == 'video':
-                            video_count += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
-
-                        elif media_type == 'skipped':
-                            skipped += 1
-                            main_bar.set_description(
-                                desc.format(
-                                    p_count=photo_count, v_count=video_count, skipped=skipped, data=data), refresh=False)
+        aws=[]
+        photo_count = 0
+        video_count = 0
+        audio_count=0
+        skipped = 0
+        total_bytes_downloaded = 0
+        data = 0
+        desc = 'Progress: ({p_count} photos, {v_count} videos, {skipped} skipped || {data})'   
+        print(f"\nDownloading to {(config.get('save_location') or pathlib.Path.home()/'ofscraper')}/{(config.get('dir_format') or '{model_username}/{responsetype}/{mediatype}')}\n\n")
+
+        with tqdm(desc=desc.format(p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), total=len(aws), colour='cyan', leave=True) as main_bar: 
+            for ele in medialist:
+                with set_directory(getmediadir(ele,username,model_id)):
+                    aws.append(asyncio.create_task(download_paid(ele,pathlib.Path(".").absolute() ,model_id, username,file_size_limit)))
+            for coro in asyncio.as_completed(aws):
+                    try:
+                        media_type, num_bytes_downloaded = await coro
+                    except Exception as e:
+                        media_type = None
+                        num_bytes_downloaded = 0
+                        console.print(e)
+
+                    total_bytes_downloaded += num_bytes_downloaded
+                    data = convert_num_bytes(total_bytes_downloaded)
+
+                    if media_type == 'images':
+                        photo_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=False)
+
+                    elif media_type == 'audios':
+                        audio_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=False)                        
+                    elif media_type == 'videos':
+                        video_count += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=False)
+
+                    elif media_type == 'skipped':
+                        skipped += 1
+                        main_bar.set_description(
+                            desc.format(
+                                p_count=photo_count, v_count=video_count, skipped=skipped, data=data,mediacount=len(medialist), sumcount=video_count+audio_count+photo_count+skipped), refresh=False)
 
-                        main_bar.update()
+                    main_bar.update()
 
 
 @retry(stop=stop_after_attempt(5),wait=wait_random(min=20, max=40),reraise=True)                    
-async def download_paid(client,url,filename,path,media_type,model_id,file_size_limit,_id,forced=False):  
-    async with sem:  
-        async with client.stream('GET', url) as r:
-            if not r.is_error:            
-                rheaders=r.headers
-                total = int(rheaders["Content-Length"])
-                if file_size_limit and total>int(file_size_limit):
-                    return 'skipped', 1
-                content_type = rheaders.get("content-type").split('/')[-1]
-                path_to_file = pathlib.Path(path,f"{filename}.{content_type}")
-                with set_directory(pathlib.Path(pathlib.Path(__file__).parents[2],".tempmedia")):
-                    temp=f"{filename}.{content_type}"
-                    pathlib.Path(temp).unlink(missing_ok=True)
-                    with open(temp, 'wb') as f:
-                        with tqdm(desc=temp,total=total, unit_scale=True, unit_divisor=1024, unit="B",leave=False) as bar:
+async def download_paid(ele,path,model_id,username,file_size_limit,id_=None):  
+    url=ele['url']
+    media_type=ele['mediatype']
+    id_=ele['id']
+    bar=None
+    temp=None
+    try:
+        async with sem:  
+            async with httpx.AsyncClient(http2=True, headers = auth.make_headers(auth.read_auth()), follow_redirects=True, timeout=None) as c: 
+                auth.add_cookies(c)     
+                async with c.stream('GET', url) as r:
+                    if not r.is_error:            
+                        rheaders=r.headers
+                        total = int(rheaders["Content-Length"])
+                        if file_size_limit and total>int(file_size_limit):
+                            return 'skipped', 1
+                        content_type = rheaders.get("content-type").split('/')[-1]
+                        filename=createfilename(ele,username,model_id,content_type)
+                        path_to_file = trunicate(pathlib.Path(path,f"{filename}"))
+                        with set_directory(pathlib.Path(pathlib.Path.home(),configPath,get_current_profile(),".tempmedia")):
+                            temp=trunicate(f"{filename}")
+                            pathlib.Path(temp).unlink(missing_ok=True)
+                            with open(temp, 'wb') as f:
+                                pathstr=str(temp)
+                                bar=tqdm(desc=(pathstr[:10] + '....') if len(pathstr) > 10 else pathstr,total=total, unit_scale=True, unit_divisor=1024, unit="B",leave=False) 
                                 num_bytes_downloaded = r.num_bytes_downloaded
                                 async for chunk in r.aiter_bytes(chunk_size=1024):
                                     f.write(chunk)
                                     bar.update(r.num_bytes_downloaded - num_bytes_downloaded)
                                     num_bytes_downloaded = r.num_bytes_downloaded
-                    if pathlib.Path(temp).exists() and(total-pathlib.Path(temp).stat().st_size<=1000):
-                        shutil.move(temp,path_to_file)
-                        if _id:
-                            operations.paid_write_from_data(_id,model_id)
-                        return media_type,total
-                    else:
-                        return 'skipped', 1
-
-            else:
-                r.raise_for_status()
+                            if pathlib.Path(temp).exists() and(total-pathlib.Path(temp).stat().st_size<=1000):
+                                shutil.move(temp,path_to_file)
+                                if id_:
+                                    operations.write_media(ele,path_to_file,model_id,username)
+                                return media_type,total
+                            else:
+                                return 'skipped', 1
 
+                    else:
+                        r.raise_for_status()
+                        
+    except Exception as e:
+        if not r or r.status_code==200:
+            print(traceback.format_exc())
+        return 'skipped', 1
+    finally:
+        if bar:
+            bar.close()
+        if temp:
+            pathlib.Path(temp).unlink(missing_ok=True)
+        
 def convert_num_bytes(num_bytes: int) -> str:
     if num_bytes == 0:
       return '0 B'
     num_digits = int(math.log10(num_bytes)) + 1
 
     if num_digits >= 10:
         return f'{round(num_bytes / 10**9, 2)} GB'
@@ -259,15 +303,46 @@
 
 def get_error_message(content):
     error_content = content.get('error', 'No error message available')
     try:
         return error_content.get('message', 'No error message available')
     except AttributeError:
         return error_content
-def createfilename(url,username,model_id=None,date=None,id_=None,media_type=None,text=None,count=None):
-    return url.split('.')[-2].split('/')[-1].strip("/,.;!_-@#$%^&*()+\\ ")
+def createfilename(ele,username,model_id,ext):
+    filename=ele["url"].split('.')[-2].split('/')[-1].strip("/,.;!_-@#$%^&*()+\\ ")
+    if ele.get("responsetype") in "profile":
+        return filename
+    
+    return (config.get('file_format') or '{filename}.{ext}').format(filename=filename,sitename="Onlyfans",post_id=ele["postid"],media_id=ele["id"],first_letter=username[0],media_type=ele["mediatype"],value=ele["value"],text=texthelper(ele.get("text") or filename,ele),date=arrow.get(ele['date']).format(config.get('date')),ext=ext,model_username=username,model_id=model_id,responsetype=ele["responsetype"])
+
+def texthelper(text,ele):    
+    count=ele["count"]
+    length=int(config.get("textlength") or 0)
+    if length!=0:
+        text=text[0:length]
+    if (len(ele["data"].get("media",[]))>1) or ele.get("responsetype") in ["stories","highlights"]:
+        text= f"{text}{count}"
+    # text=re.sub("[^\x00-\x7F]","",text)
+    text=re.sub("<[^>]*>", "",text)
+    text=re.sub('[\n<>:"/\|?*]+', '', text)
+    text=re.sub(" +"," ",text)
+    return text
+    
+
+   
+
+
+
 
-def urldictHelper(data):
-    if data.get("reponsetype")=="post":
-        data["responesetype"]="posts"
-    if data.get("mediatype")=="photo" or data.get("mediatype")=="gif" :
-        data["mediatype"]="images"
+def getmediadir(ele,username,model_id):
+    root= pathlib.Path((config.get('save_location') or pathlib.Path.home()/"ofscraper"))
+    downloadDir=(config.get('dir_format') or "{model_username}/{responsetype}/{mediatype}").format(sitename="onlyfans",first_letter=username[0].capitalize(),model_id=model_id,model_username=username,responsetype=ele['responsetype'].capitalize(),mediatype=ele['mediatype'].capitalize(),value=ele['value'].capitalize(),date=arrow.get(ele['date']).format(config.get('date')))
+    return root /downloadDir
+
+def trunicate(path):
+    if platform.system() == 'Windows' and len(path)>256:
+        return path[0:256]
+    elif platform.system() == 'Linux':
+        dir=pathlib.Path(path).parent
+        file=pathlib.Path(path).name.encode("utf8")[:255].decode("utf8", "ignore")
+        return pathlib.Path(dir,file)
+    return path
```

### Comparing `ofscraper-1.51/src/utils/encoding.py` & `ofscraper-1.60/src/utils/encoding.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/utils/old_nap.py` & `ofscraper-1.60/src/utils/old_nap.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/utils/profiles.py` & `ofscraper-1.60/src/utils/profiles.py`

 * *Files identical despite different names*

### Comparing `ofscraper-1.51/src/utils/prompts.py` & `ofscraper-1.60/src/utils/prompts.py`

 * *Files 2% similar despite different names*

```diff
@@ -441,15 +441,15 @@
     answer = prompt(questions)
     return answer[0]
 
 def decide_filters_prompts():
     questions = [
         {
             'type': 'list',
-            'message': "Modify filters for accounts list?\nExample scraping free accounts only",
+            'message': "Modify filters for your accounts list?\nSome usage examples are scraping free accounts only or paid accounts without renewal",
             'choices':["Yes","No"]
         }
     ]
 
     answer = prompt(questions)
     return answer[0]
 def modify_filters_prompt(args):
```

### Comparing `ofscraper-1.51/src/utils/separate.py` & `ofscraper-1.60/src/utils/separate.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 (  <_> )  |  \___ \\  \___|  | \// __ \(  <_> )  ___/|  | \/
  \____/|__| /____  >\___  >__|  (____  /\____/ \___  >__|   
                  \/     \/           \/            \/         
 """
 
 
 def separate_by_id(data: list, media_ids: list) -> list:
-    return list(filter(lambda x:x["id"] in media_ids,data))
+    return list(filter(lambda x:x.get("id") not in media_ids,data))
     
   
 
 
 def separate_database_results_by_id(results: list, media_ids: list) -> list:
     filtered_results = [r for r in results if r[0] not in media_ids]
     return filtered_results
```

### Comparing `ofscraper-1.51/PKG-INFO` & `ofscraper-1.60/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 Metadata-Version: 2.1
 Name: ofscraper
-Version: 1.51
+Version: 1.60
 Summary: automatically scrape onlyfans
 Author: excludedBittern8
 Author-email: excludedBittern8@riseup.net
 Requires-Python: >=3.7.0,<4
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Requires-Dist: arrow (>=1.2.3,<2.0.0)
 Requires-Dist: browser-cookie3 (>=0.17.1,<0.18.0)
 Requires-Dist: bs4 (>=0.0.1,<0.0.2)
 Requires-Dist: httpx[http2] (>=0.23.3,<0.24.0)
 Requires-Dist: inquirerpy (>=0.3.4,<0.4.0)
 Requires-Dist: requests (>=2.28.2,<3.0.0)
 Requires-Dist: revolution (>=0.3.0,<0.4.0)
 Requires-Dist: rich (>=13.3.2,<14.0.0)
@@ -26,19 +27,14 @@
 Description-Content-Type: text/markdown
 
 This is a fork of onlyfans-scraper with additional features and fixes
 
 Note the guide is still a little incomplete, so it might not be up to date with the changes I made 
 I hope to go through it and make the necessary changes soon.
 
-new db branch has some changes that will be coming to the main branch soon
-https://github.com/excludedBittern8/ofscraper/tree/db
-
-Will be added a feature to speed up repeated scraping of models
-
 <h3>DISCLAIMERS:</h3>
 <ol>
     <li>
         This tool is not affiliated, associated, or partnered with OnlyFans in any way. We are not authorized, endorsed, or sponsored by OnlyFans. All OnlyFans trademarks remain the property of Fenix International Limited.
     </li>
     <li>
         This is a theoritical program only and is for educational purposes. If you choose to use it then it may or may not work. You solely accept full responsability and indemnify the creator, hostors, contributors and all other involved persons from any any all responsability.
```

