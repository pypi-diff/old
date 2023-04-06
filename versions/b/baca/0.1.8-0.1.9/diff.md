# Comparing `tmp/baca-0.1.8.tar.gz` & `tmp/baca-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "baca-0.1.8.tar", max compression
+gzip compressed data, was "baca-0.1.9.tar", max compression
```

## Comparing `baca-0.1.8.tar` & `baca-0.1.9.tar`

### file list

```diff
@@ -1,55 +1,55 @@
--rw-r--r--   0        0        0    35081 2023-03-27 06:23:41.354772 baca-0.1.8/LICENSE
--rw-r--r--   0        0        0     4580 2023-04-01 00:55:03.806358 baca-0.1.8/README.md
--rw-r--r--   0        0        0      894 2023-04-01 00:55:03.806358 baca-0.1.8/pyproject.toml
--rw-r--r--   0        0        0      172 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/__init__.py
--rw-r--r--   0        0        0      762 2023-03-29 05:51:48.738852 baca-0.1.8/src/baca/__main__.py
--rw-r--r--   0        0        0    12705 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/app.py
--rw-r--r--   0        0        0        0 2023-03-24 09:03:49.917174 baca-0.1.8/src/baca/components/__init__.py
--rw-r--r--   0        0        0     6322 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/components/contents.py
--rw-r--r--   0        0        0      618 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/components/events.py
--rw-r--r--   0        0        0     6334 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/components/windows.py
--rw-r--r--   0        0        0     3172 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/config.py
--rw-r--r--   0        0        0     1278 2023-03-28 00:31:58.605346 baca-0.1.8/src/baca/db.py
--rw-r--r--   0        0        0      155 2023-03-26 15:02:41.203146 baca-0.1.8/src/baca/ebooks/__init__.py
--rw-r--r--   0        0        0      608 2023-03-26 13:36:59.470254 baca-0.1.8/src/baca/ebooks/azw.py
--rw-r--r--   0        0        0      991 2023-03-26 13:36:59.470254 baca-0.1.8/src/baca/ebooks/base.py
--rw-r--r--   0        0        0     7734 2023-03-27 03:59:52.261233 baca-0.1.8/src/baca/ebooks/epub.py
--rw-r--r--   0        0        0     2981 2023-03-27 06:15:56.219366 baca-0.1.8/src/baca/ebooks/mobi.py
--rw-r--r--   0        0        0      884 2023-03-29 05:49:48.740643 baca-0.1.8/src/baca/exceptions.py
--rw-r--r--   0        0        0     2665 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/models.py
--rw-r--r--   0        0        0        0 2023-03-25 05:22:56.599267 baca-0.1.8/src/baca/resources/__init__.py
--rw-r--r--   0        0        0      834 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/resources/config.ini
--rw-r--r--   0        0        0     2684 2023-04-01 00:55:03.806358 baca-0.1.8/src/baca/resources/style.css
--rw-r--r--   0        0        0       73 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/__init__.py
--rwxr-xr-x   0        0        0     9189 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/compatibility_utils.py
--rw-r--r--   0        0        0    44186 2023-03-27 03:59:46.052896 baca-0.1.8/src/baca/tools/KindleUnpack/kindleunpack.py
--rw-r--r--   0        0        0     8864 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_cover.py
--rw-r--r--   0        0        0    16612 2023-03-27 03:59:46.052896 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_dict.py
--rw-r--r--   0        0        0    38999 2023-03-27 03:59:46.056897 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_header.py
--rw-r--r--   0        0        0    20849 2023-03-27 03:59:46.056897 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_html.py
--rw-r--r--   0        0        0    11224 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_index.py
--rw-r--r--   0        0        0    22375 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_k8proc.py
--rw-r--r--   0        0        0    10163 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_k8resc.py
--rw-r--r--   0        0        0     6813 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_nav.py
--rw-r--r--   0        0        0     9838 2023-03-27 03:59:46.056897 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_ncx.py
--rw-r--r--   0        0        0    31813 2023-03-27 03:59:46.060897 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_opf.py
--rw-r--r--   0        0        0     5675 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_pagemap.py
--rw-r--r--   0        0        0     5260 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_sectioner.py
--rwxr-xr-x   0        0        0    19270 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_split.py
--rw-r--r--   0        0        0     4309 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_uncompress.py
--rw-r--r--   0        0        0     8654 2023-03-27 03:59:46.060897 baca-0.1.8/src/baca/tools/KindleUnpack/mobi_utils.py
--rwxr-xr-x   0        0        0    19828 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/mobiml2xhtml.py
--rwxr-xr-x   0        0        0     3144 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/unipath.py
--rw-r--r--   0        0        0     7158 2023-03-26 22:02:42.297059 baca-0.1.8/src/baca/tools/KindleUnpack/unpack_structure.py
--rw-r--r--   0        0        0      106 2023-03-26 09:33:10.617248 baca-0.1.8/src/baca/tools/__init__.py
--rw-r--r--   0        0        0        0 2023-03-24 09:03:49.917174 baca-0.1.8/src/baca/utils/__init__.py
--rw-r--r--   0        0        0      228 2023-03-29 01:58:22.118542 baca-0.1.8/src/baca/utils/app_resources.py
--rw-r--r--   0        0        0     4237 2023-03-31 23:37:47.307783 baca-0.1.8/src/baca/utils/cli.py
--rw-r--r--   0        0        0     2609 2023-03-28 07:35:29.438886 baca-0.1.8/src/baca/utils/html_parser.py
--rw-r--r--   0        0        0      653 2023-03-25 01:39:18.097675 baca-0.1.8/src/baca/utils/keys_parser.py
--rw-r--r--   0        0        0     1517 2023-03-29 01:33:38.486692 baca-0.1.8/src/baca/utils/queries.py
--rw-r--r--   0        0        0      532 2023-03-29 05:49:39.061875 baca-0.1.8/src/baca/utils/systems.py
--rw-r--r--   0        0        0      161 2023-03-26 13:36:59.530257 baca-0.1.8/src/baca/utils/tempdir.py
--rw-r--r--   0        0        0      880 2023-03-29 01:57:21.301449 baca-0.1.8/src/baca/utils/user_appdirs.py
--rw-r--r--   0        0        0     5775 1970-01-01 00:00:00.000000 baca-0.1.8/setup.py
--rw-r--r--   0        0        0     5285 1970-01-01 00:00:00.000000 baca-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0    35081 2023-03-27 06:23:41.354772 baca-0.1.9/LICENSE
+-rw-r--r--   0        0        0     4580 2023-04-01 00:55:03.806358 baca-0.1.9/README.md
+-rw-r--r--   0        0        0      894 2023-04-01 01:17:35.055846 baca-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0      172 2023-04-01 01:17:29.383982 baca-0.1.9/src/baca/__init__.py
+-rw-r--r--   0        0        0      762 2023-03-29 05:51:48.738852 baca-0.1.9/src/baca/__main__.py
+-rw-r--r--   0        0        0    12879 2023-04-01 01:17:24.168108 baca-0.1.9/src/baca/app.py
+-rw-r--r--   0        0        0        0 2023-03-24 09:03:49.917174 baca-0.1.9/src/baca/components/__init__.py
+-rw-r--r--   0        0        0     6301 2023-04-01 00:58:47.980773 baca-0.1.9/src/baca/components/contents.py
+-rw-r--r--   0        0        0      618 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/components/events.py
+-rw-r--r--   0        0        0     6334 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/components/windows.py
+-rw-r--r--   0        0        0     3172 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/config.py
+-rw-r--r--   0        0        0     1278 2023-03-28 00:31:58.605346 baca-0.1.9/src/baca/db.py
+-rw-r--r--   0        0        0      155 2023-03-26 15:02:41.203146 baca-0.1.9/src/baca/ebooks/__init__.py
+-rw-r--r--   0        0        0      608 2023-03-26 13:36:59.470254 baca-0.1.9/src/baca/ebooks/azw.py
+-rw-r--r--   0        0        0      991 2023-03-26 13:36:59.470254 baca-0.1.9/src/baca/ebooks/base.py
+-rw-r--r--   0        0        0     7734 2023-03-27 03:59:52.261233 baca-0.1.9/src/baca/ebooks/epub.py
+-rw-r--r--   0        0        0     2981 2023-03-27 06:15:56.219366 baca-0.1.9/src/baca/ebooks/mobi.py
+-rw-r--r--   0        0        0      884 2023-03-29 05:49:48.740643 baca-0.1.9/src/baca/exceptions.py
+-rw-r--r--   0        0        0     2665 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/models.py
+-rw-r--r--   0        0        0        0 2023-03-25 05:22:56.599267 baca-0.1.9/src/baca/resources/__init__.py
+-rw-r--r--   0        0        0      834 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/resources/config.ini
+-rw-r--r--   0        0        0     2684 2023-04-01 00:55:03.806358 baca-0.1.9/src/baca/resources/style.css
+-rw-r--r--   0        0        0       73 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/__init__.py
+-rwxr-xr-x   0        0        0     9189 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/compatibility_utils.py
+-rw-r--r--   0        0        0    44186 2023-03-27 03:59:46.052896 baca-0.1.9/src/baca/tools/KindleUnpack/kindleunpack.py
+-rw-r--r--   0        0        0     8864 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_cover.py
+-rw-r--r--   0        0        0    16612 2023-03-27 03:59:46.052896 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_dict.py
+-rw-r--r--   0        0        0    38999 2023-03-27 03:59:46.056897 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_header.py
+-rw-r--r--   0        0        0    20849 2023-03-27 03:59:46.056897 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_html.py
+-rw-r--r--   0        0        0    11224 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_index.py
+-rw-r--r--   0        0        0    22375 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_k8proc.py
+-rw-r--r--   0        0        0    10163 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_k8resc.py
+-rw-r--r--   0        0        0     6813 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_nav.py
+-rw-r--r--   0        0        0     9838 2023-03-27 03:59:46.056897 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_ncx.py
+-rw-r--r--   0        0        0    31813 2023-03-27 03:59:46.060897 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_opf.py
+-rw-r--r--   0        0        0     5675 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_pagemap.py
+-rw-r--r--   0        0        0     5260 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_sectioner.py
+-rwxr-xr-x   0        0        0    19270 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_split.py
+-rw-r--r--   0        0        0     4309 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_uncompress.py
+-rw-r--r--   0        0        0     8654 2023-03-27 03:59:46.060897 baca-0.1.9/src/baca/tools/KindleUnpack/mobi_utils.py
+-rwxr-xr-x   0        0        0    19828 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/mobiml2xhtml.py
+-rwxr-xr-x   0        0        0     3144 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/unipath.py
+-rw-r--r--   0        0        0     7158 2023-03-26 22:02:42.297059 baca-0.1.9/src/baca/tools/KindleUnpack/unpack_structure.py
+-rw-r--r--   0        0        0      106 2023-03-26 09:33:10.617248 baca-0.1.9/src/baca/tools/__init__.py
+-rw-r--r--   0        0        0        0 2023-03-24 09:03:49.917174 baca-0.1.9/src/baca/utils/__init__.py
+-rw-r--r--   0        0        0      228 2023-03-29 01:58:22.118542 baca-0.1.9/src/baca/utils/app_resources.py
+-rw-r--r--   0        0        0     4237 2023-03-31 23:37:47.307783 baca-0.1.9/src/baca/utils/cli.py
+-rw-r--r--   0        0        0     2609 2023-03-28 07:35:29.438886 baca-0.1.9/src/baca/utils/html_parser.py
+-rw-r--r--   0        0        0      653 2023-03-25 01:39:18.097675 baca-0.1.9/src/baca/utils/keys_parser.py
+-rw-r--r--   0        0        0     1517 2023-03-29 01:33:38.486692 baca-0.1.9/src/baca/utils/queries.py
+-rw-r--r--   0        0        0      532 2023-03-29 05:49:39.061875 baca-0.1.9/src/baca/utils/systems.py
+-rw-r--r--   0        0        0      161 2023-03-26 13:36:59.530257 baca-0.1.9/src/baca/utils/tempdir.py
+-rw-r--r--   0        0        0      880 2023-03-29 01:57:21.301449 baca-0.1.9/src/baca/utils/user_appdirs.py
+-rw-r--r--   0        0        0     5775 1970-01-01 00:00:00.000000 baca-0.1.9/setup.py
+-rw-r--r--   0        0        0     5285 1970-01-01 00:00:00.000000 baca-0.1.9/PKG-INFO
```

### Comparing `baca-0.1.8/LICENSE` & `baca-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/README.md` & `baca-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/pyproject.toml` & `baca-0.1.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "baca"
-version = "0.1.8"
+version = "0.1.9"
 description = "TUI Ebook Reader"
 authors = ["Benawi Adha <benawiadha@gmail.com>"]
 license = "GPL-3.0"
 readme = "README.md"
 packages = [
     { include = "baca", from = "src" }
 ]
```

### Comparing `baca-0.1.8/src/baca/__main__.py` & `baca-0.1.9/src/baca/__main__.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/app.py` & `baca-0.1.9/src/baca/app.py`

 * *Files 1% similar despite different names*

```diff
@@ -149,15 +149,19 @@
 
     def action_page_up(self) -> None:
         if not self.screen.allow_vertical_scroll:
             raise SkipAction()
         self.screen.scroll_page_up(duration=self.config.page_scroll_duration)
 
     async def action_input_search(self, forward: bool) -> None:
-        await self.mount(SearchInputPrompt(forward=forward))
+        if self.config.pretty:
+            # TODO:
+            await self.alert("Currently search feature isn't implemented for pretty=yes configuration.")
+        else:
+            await self.mount(SearchInputPrompt(forward=forward))
 
     async def action_search_next(self) -> bool:
         if self.search_mode is not None:
             new_coord = await self.content.search_next(
                 self.search_mode.pattern_str,
                 self.search_mode.current_coord,
                 self.search_mode.forward,
```

### Comparing `baca-0.1.8/src/baca/components/contents.py` & `baca-0.1.9/src/baca/components/contents.py`

 * *Files 1% similar despite different names*

```diff
@@ -142,15 +142,14 @@
     def get_text_at(self, y: int) -> str | None:
         accumulated_height = 0
         for segment in self._segments:
             if accumulated_height + segment.virtual_size.height > y:
                 return segment.render_lines(Region(0, y - accumulated_height, self.virtual_size.width, 1))[0].text
             accumulated_height += segment.virtual_size.height
 
-    # TODO: annotate
     async def search_next(
         self, pattern_str: str, current_coord: Coordinate = Coordinate(-1, 0), forward: bool = True
     ) -> Coordinate | None:
         pattern = re.compile(pattern_str, re.IGNORECASE)
         current_x = current_coord.x
         line_range = (
             range(current_coord.y, self.virtual_size.height) if forward else reversed(range(0, current_coord.y + 1))
```

### Comparing `baca-0.1.8/src/baca/components/events.py` & `baca-0.1.9/src/baca/components/events.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/components/windows.py` & `baca-0.1.9/src/baca/components/windows.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/config.py` & `baca-0.1.9/src/baca/config.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/db.py` & `baca-0.1.9/src/baca/db.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/ebooks/azw.py` & `baca-0.1.9/src/baca/ebooks/azw.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/ebooks/base.py` & `baca-0.1.9/src/baca/ebooks/base.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/ebooks/epub.py` & `baca-0.1.9/src/baca/ebooks/epub.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/ebooks/mobi.py` & `baca-0.1.9/src/baca/ebooks/mobi.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/exceptions.py` & `baca-0.1.9/src/baca/exceptions.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/models.py` & `baca-0.1.9/src/baca/models.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/resources/config.ini` & `baca-0.1.9/src/baca/resources/config.ini`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/resources/style.css` & `baca-0.1.9/src/baca/resources/style.css`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/compatibility_utils.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/compatibility_utils.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/kindleunpack.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/kindleunpack.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_cover.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_cover.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_dict.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_dict.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_header.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_header.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_html.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_html.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_index.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_index.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_k8proc.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_k8proc.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_k8resc.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_k8resc.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_nav.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_nav.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_ncx.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_ncx.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_opf.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_opf.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_pagemap.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_pagemap.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_sectioner.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_sectioner.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_split.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_split.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_uncompress.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_uncompress.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobi_utils.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobi_utils.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/mobiml2xhtml.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/mobiml2xhtml.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/unipath.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/unipath.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/tools/KindleUnpack/unpack_structure.py` & `baca-0.1.9/src/baca/tools/KindleUnpack/unpack_structure.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/cli.py` & `baca-0.1.9/src/baca/utils/cli.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/html_parser.py` & `baca-0.1.9/src/baca/utils/html_parser.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/keys_parser.py` & `baca-0.1.9/src/baca/utils/keys_parser.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/queries.py` & `baca-0.1.9/src/baca/utils/queries.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/systems.py` & `baca-0.1.9/src/baca/utils/systems.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/src/baca/utils/user_appdirs.py` & `baca-0.1.9/src/baca/utils/user_appdirs.py`

 * *Files identical despite different names*

### Comparing `baca-0.1.8/setup.py` & `baca-0.1.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -25,15 +25,15 @@
  'textual>=0.16.0,<0.17.0']
 
 entry_points = \
 {'console_scripts': ['baca = baca.__main__:main']}
 
 setup_kwargs = {
     'name': 'baca',
-    'version': '0.1.8',
+    'version': '0.1.9',
     'description': 'TUI Ebook Reader',
     'long_description': '# `baca`: TUI Ebook Reader\n\n![baca_fit](https://user-images.githubusercontent.com/43810055/227891952-45df1c36-5113-4793-84b6-249725d3ba19.png)\n\nMeet `baca`, [epy](https://github.com/wustho/epy)\'s lovely sister who lets you indulge\nin your favorite e-books in the comfort of your terminal.\nBut with a sleek and contemporary appearance that\'s sure to captivate you!\n\n## Features\n\n- Formats supported: Epub, Epub3, Mobi & Azw\n- Remembers last reading position\n- Scroll animations\n- Clean & modern looks\n- Lets you open images\n- Text justification\n- Dark & light colorscheme\n- Regex search\n\n## Requirements\n\n- `python>=3.10`\n\n## Installation\n\n- Via pip: `pip install baca`\n- Via git: `pip install git+https://github.com/wustho/baca`\n\n## Usage\n\n```sh\n# to read an ebook\nbaca path/to/your/ebook.epub\n\n# to read your last read ebook, just run baca without any argument\nbaca\n\n# to see your reading history use -r as an argument\nbaca -r\n\n# say you want to read an ebook from your reading history,\n# but you forgot the path to your ebook\n# just type any words you remember about your ebook\n# and baca will try to match it to path or title+author\nbaca doc ebook.epub\nbaca alice wonder lewis carroll\n```\n\n## Opening an Image\n\nTo open an image, when you encounter some thing like this:\n\n```\n┌──────────────────────────────────────────────────────────────────────────────┐\n│                                    IMAGE                                     │\n└──────────────────────────────────────────────────────────────────────────────┘\n```\n\njust click on it using mouse and it will open the image.\nYeah, I know you want to use keyboard for this, me too, but bear with this for now.\n\n## Configurations\n\n![pretty_yes_no_cap](https://user-images.githubusercontent.com/43810055/228417623-ac78fb84-0ee0-4930-a843-752ef693822d.png)\n\nConfiguration file available at `~/.config/baca/config.ini` for linux users. Here is the default:\n\n```ini\n[General]\n# pick your favorite image viewer\nPreferredImageViewer = auto\n\n# int or css value string like 90%%\n# (escape percent with double percent %%)\nMaxTextWidth = 80\n\n# \'justify\', \'center\', \'left\', \'right\'\nTextJustification = justify\n\n# currently using pretty=yes is slow\n# and taking huge amount of memory\nPretty = no\n\nPageScrollDuration = 0.2\n\n[Color Dark]\nBackground = #1e1e1e\nForeground = #f5f5f5\nAccent = #0178d4\n\n[Color Light]\nBackground = #f5f5f5\nForeground = #1e1e1e\nAccent = #0178d4\n\n[Keymaps]\nToggleLightDark = c\nScrollDown = down,j\nScrollUp = up,k\nPageDown = ctrl+f,pagedown,l,space\nPageUp = ctrl+b,pageup,h\nHome = home,g\nEnd = end,G\nOpenToc = tab\nOpenMetadata = M\nOpenHelp = f1\nSearchForward = slash\nSearchBackward = question_mark\nNextMatch = n\nPreviousMatch = N\nConfirm = enter\nCloseOrQuit = q,escape\nScreenshot = f12\n```\n\n## Known Limitations\n\n- When searching for specific phrases in `baca`,\n  keep in mind that it may not be able to find them if they span across two lines,\n  much like in the search behavior of editor vi(m).\n\n  For example, `baca` won\'t be able to find the phrase `"for it"` because it is split into two lines\n  in this example.\n\n  ```\n  ...\n  she had forgotten the little golden key, and when she went back to the table for\n  it, she found she could not possibly reach it: she could see  it  quite  plainly\n  ...\n  ```\n\n\n  Additionally, `baca` may struggle to locate certain phrases due to adjustments made for text justification.\n  See the example above, `"see_it"` may become `"see__it"` due to adjusted spacing between words.\n  In this case, it may be more effective to use a regex search for `"see +it"` or simply search for the word `"see"` alone.\n\n  Overall, `baca`\'s search feature is most effective for locating individual words\n  rather than phrases that may be split across multiple lines or impacted by text justification.\n\n- Compared to [epy](https://github.com/wustho/epy), currently `baca` has some missing features.\n  But these are planned to be implemented to `baca` in the near future:\n\n  - [ ] **TODO** Bookmarks\n  - [ ] **TODO** FictionBook support\n  - [ ] **TODO** URL reading support\n\n## Credits\n\n- Thanks to awesome [Textual Project](https://github.com/Textualize/textual)\n- [Kindle Unpack](https://github.com/kevinhendricks/KindleUnpack)\n- And many others!\n\n## License\n\nGPL-3\n\n',
     'author': 'Benawi Adha',
     'author_email': 'benawiadha@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `baca-0.1.8/PKG-INFO` & `baca-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: baca
-Version: 0.1.8
+Version: 0.1.9
 Summary: TUI Ebook Reader
 License: GPL-3.0
 Author: Benawi Adha
 Author-email: benawiadha@gmail.com
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3
```

