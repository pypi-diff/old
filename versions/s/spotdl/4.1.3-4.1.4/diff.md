# Comparing `tmp/spotdl-4.1.3.tar.gz` & `tmp/spotdl-4.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "spotdl-4.1.3.tar", max compression
+gzip compressed data, was "spotdl-4.1.4.tar", max compression
```

## Comparing `spotdl-4.1.3.tar` & `spotdl-4.1.4.tar`

### file list

```diff
@@ -1,54 +1,54 @@
--rw-r--r--   0        0        0     1074 2023-03-15 12:07:52.031580 spotdl-4.1.3/LICENSE
--rw-r--r--   0        0        0     5519 2023-03-15 12:07:52.031580 spotdl-4.1.3/README.md
--rw-r--r--   0        0        0     2612 2023-03-15 12:07:52.039580 spotdl-4.1.3/pyproject.toml
--rw-r--r--   0        0        0     4668 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/__init__.py
--rw-r--r--   0        0        0      209 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/__main__.py
--rw-r--r--   0        0        0       58 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/_version.py
--rw-r--r--   0        0        0      186 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/__init__.py
--rw-r--r--   0        0        0      598 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/download.py
--rw-r--r--   0        0        0     3869 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/entry_point.py
--rw-r--r--   0        0        0     4160 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/meta.py
--rw-r--r--   0        0        0     2759 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/save.py
--rw-r--r--   0        0        0     4896 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/sync.py
--rw-r--r--   0        0        0     1702 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/url.py
--rw-r--r--   0        0        0     3041 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/console/web.py
--rw-r--r--   0        0        0       80 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/download/__init__.py
--rw-r--r--   0        0        0    26207 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/download/downloader.py
--rw-r--r--   0        0        0    13137 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/download/progress_handler.py
--rw-r--r--   0        0        0       54 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/__init__.py
--rw-r--r--   0        0        0      396 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/audio/__init__.py
--rw-r--r--   0        0        0    11033 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/audio/base.py
--rw-r--r--   0        0        0     1840 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/audio/youtube.py
--rw-r--r--   0        0        0     3069 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/audio/ytmusic.py
--rw-r--r--   0        0        0      382 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/__init__.py
--rw-r--r--   0        0        0     2397 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/azlyrics.py
--rw-r--r--   0        0        0     1495 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/base.py
--rw-r--r--   0        0        0     2420 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/genius.py
--rw-r--r--   0        0        0     2461 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/musixmatch.py
--rw-r--r--   0        0        0      856 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/providers/lyrics/synced.py
--rw-r--r--   0        0        0       38 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/__init__.py
--rw-r--r--   0        0        0     3451 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/album.py
--rw-r--r--   0        0        0     3101 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/artist.py
--rw-r--r--   0        0        0     3657 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/options.py
--rw-r--r--   0        0        0     4173 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/playlist.py
--rw-r--r--   0        0        0     2186 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/result.py
--rw-r--r--   0        0        0     3230 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/saved.py
--rw-r--r--   0        0        0     9758 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/types/song.py
--rw-r--r--   0        0        0      103 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/__init__.py
--rw-r--r--   0        0        0     1001 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/archive.py
--rw-r--r--   0        0        0    18627 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/arguments.py
--rw-r--r--   0        0        0     6675 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/config.py
--rw-r--r--   0        0        0     3109 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/console.py
--rw-r--r--   0        0        0      571 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/downloader.py
--rw-r--r--   0        0        0    11688 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/ffmpeg.py
--rw-r--r--   0        0        0    13002 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/formatter.py
--rw-r--r--   0        0        0     7018 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/github.py
--rw-r--r--   0        0        0     5364 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/logging.py
--rw-r--r--   0        0        0     4095 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/m3u.py
--rw-r--r--   0        0        0    21119 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/matching.py
--rw-r--r--   0        0        0    15369 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/metadata.py
--rw-r--r--   0        0        0    14408 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/search.py
--rw-r--r--   0        0        0     5660 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/spotify.py
--rw-r--r--   0        0        0    28221 2023-03-15 12:07:52.039580 spotdl-4.1.3/spotdl/utils/static.py
--rw-r--r--   0        0        0    15281 2023-03-15 12:07:52.043580 spotdl-4.1.3/spotdl/utils/web.py
--rw-r--r--   0        0        0     7755 1970-01-01 00:00:00.000000 spotdl-4.1.3/PKG-INFO
+-rw-r--r--   0        0        0     1074 2023-04-06 15:40:24.068964 spotdl-4.1.4/LICENSE
+-rw-r--r--   0        0        0     5814 2023-04-06 15:40:24.068964 spotdl-4.1.4/README.md
+-rw-r--r--   0        0        0     2745 2023-04-06 15:40:24.076964 spotdl-4.1.4/pyproject.toml
+-rw-r--r--   0        0        0     4668 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/__init__.py
+-rw-r--r--   0        0        0      209 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/__main__.py
+-rw-r--r--   0        0        0       58 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/_version.py
+-rw-r--r--   0        0        0      186 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/__init__.py
+-rw-r--r--   0        0        0      598 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/download.py
+-rw-r--r--   0        0        0     3869 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/entry_point.py
+-rw-r--r--   0        0        0     4695 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/meta.py
+-rw-r--r--   0        0        0     2759 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/save.py
+-rw-r--r--   0        0        0     4896 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/sync.py
+-rw-r--r--   0        0        0     1702 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/url.py
+-rw-r--r--   0        0        0     3041 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/console/web.py
+-rw-r--r--   0        0        0       80 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/download/__init__.py
+-rw-r--r--   0        0        0    26228 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/download/downloader.py
+-rw-r--r--   0        0        0    13137 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/download/progress_handler.py
+-rw-r--r--   0        0        0       54 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/__init__.py
+-rw-r--r--   0        0        0      396 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/audio/__init__.py
+-rw-r--r--   0        0        0    11033 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/audio/base.py
+-rw-r--r--   0        0        0     1840 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/audio/youtube.py
+-rw-r--r--   0        0        0     3111 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/audio/ytmusic.py
+-rw-r--r--   0        0        0      382 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/__init__.py
+-rw-r--r--   0        0        0     3304 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/azlyrics.py
+-rw-r--r--   0        0        0     3404 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/base.py
+-rw-r--r--   0        0        0     3091 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/genius.py
+-rw-r--r--   0        0        0     2765 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/musixmatch.py
+-rw-r--r--   0        0        0     1689 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/providers/lyrics/synced.py
+-rw-r--r--   0        0        0       38 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/__init__.py
+-rw-r--r--   0        0        0     3451 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/album.py
+-rw-r--r--   0        0        0     3101 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/artist.py
+-rw-r--r--   0        0        0     3657 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/options.py
+-rw-r--r--   0        0        0     4199 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/playlist.py
+-rw-r--r--   0        0        0     2186 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/result.py
+-rw-r--r--   0        0        0     3230 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/saved.py
+-rw-r--r--   0        0        0     9758 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/types/song.py
+-rw-r--r--   0        0        0      103 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/__init__.py
+-rw-r--r--   0        0        0     1001 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/archive.py
+-rw-r--r--   0        0        0    18627 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/arguments.py
+-rw-r--r--   0        0        0     6675 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/config.py
+-rw-r--r--   0        0        0     3109 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/console.py
+-rw-r--r--   0        0        0      571 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/downloader.py
+-rw-r--r--   0        0        0    11688 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/ffmpeg.py
+-rw-r--r--   0        0        0    14130 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/formatter.py
+-rw-r--r--   0        0        0     7018 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/github.py
+-rw-r--r--   0        0        0     5364 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/logging.py
+-rw-r--r--   0        0        0     4095 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/m3u.py
+-rw-r--r--   0        0        0    21866 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/matching.py
+-rw-r--r--   0        0        0    15344 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/metadata.py
+-rw-r--r--   0        0        0    15064 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/search.py
+-rw-r--r--   0        0        0     5660 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/spotify.py
+-rw-r--r--   0        0        0    28221 2023-04-06 15:40:24.076964 spotdl-4.1.4/spotdl/utils/static.py
+-rw-r--r--   0        0        0    15281 2023-04-06 15:40:24.080964 spotdl-4.1.4/spotdl/utils/web.py
+-rw-r--r--   0        0        0     8043 1970-01-01 00:00:00.000000 spotdl-4.1.4/PKG-INFO
```

### Comparing `spotdl-4.1.3/LICENSE` & `spotdl-4.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/README.md` & `spotdl-4.1.4/README.md`

 * *Files 7% similar despite different names*

```diff
@@ -132,18 +132,25 @@
 > **Note**
 > Users are responsible for their actions and potential legal consequences. We do not support unauthorized downloading of copyrighted material and take no responsibility for user actions.
 
 ### Audio Quality
 
 spotDL downloads music from YouTube and is designed to always download the highest possible bitrate; which is 128 kbps for regular users and 256 kbps for YouTube Music premium users.
 
-Check the [Audio Formats](docs/USAGE.md#audio-formats-and-quality) page for more info.
+Check the [Audio Formats](docs/usage.md#audio-formats-and-quality) page for more info.
 
 ## Contributing
 
 Interested in contributing? Check out our [CONTRIBUTING.md](docs/CONTRIBUTING.md) to find
 resources around contributing along with a guide on how to set up a development environment.
 
+## Donate
+
+### xnetcat
+
+[![paypal](https://img.shields.io/badge/paypal-%2300457C.svg?&style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/kko7)
+[![kofi](https://img.shields.io/badge/kofi-%23F16061.svg?&style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/xnetcat)
+
 ## License
 
 This project is Licensed under the [MIT](/LICENSE) License.
```

### Comparing `spotdl-4.1.3/pyproject.toml` & `spotdl-4.1.4/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "spotdl"
-version = "4.1.3"
+version = "4.1.4"
 description = "Download your Spotify playlists and songs along with album art and metadata"
 license = "MIT"
 authors = ["spotDL Team <spotdladmins@googlegroups.com>"]
 maintainers = ["xnetcat <xnetcat.dev@gmail.com>"]
 readme = "README.md"
 repository = "https://github.com/spotDL/spotify-downloader.git"
 homepage = "https://github.com/spotDL/spotify-downloader/"
@@ -29,70 +29,78 @@
 python = ">=3.7.2,<3.12"
 
 spotipy = "^2.22.1"
 ytmusicapi = [
     {version = "^0.22.0", python = "<3.8"},
     {version = "^0.24.0", python = ">=3.8"},
 ]
-pytube = "^12.1.2"
-yt-dlp = "^2023.3.3"
+pytube = "^12.1.3"
+yt-dlp = "^2023.3.4"
 mutagen = "^1.46.0"
-rich = "^13.3.1"
-beautifulsoup4 = "^4.11.2"
+rich = "^13.3.3"
+beautifulsoup4 = "^4.12.1"
 requests = "^2.28.2"
-rapidfuzz = "^2.13.7"
+rapidfuzz = "^2.15.0"
 python-slugify = {extras = ["unidecode"], version = "^8.0.1"}
 uvicorn = "^0.20.0"
-pydantic = "^1.10.5"
+pydantic = "^1.10.7"
 fastapi = "^0.89.1"
 platformdirs = "^2.6.2"
 pykakasi = "^2.2.1"
-syncedlyrics = "^0.2.2"
+syncedlyrics = "0.4.0"
 typing-extensions = "^4.5.0"
 
 [tool.poetry.dev-dependencies]
 pytest = "^7.2.2"
 pytest-mock = "^3.10.0"
 pytest-vcr = "^1.0.2"
-pyfakefs = "^5.1.0"
+pyfakefs = "^5.2.0"
 pytest-cov = "^4.0.0"
 pytest-subprocess = "^1.5.0"
 pytest-asyncio = "^0.20.3"
 mypy = "^0.991"
-pylint = "^2.16.3"
+pylint = "^2.17.2"
 black = "^22.12.0"
 mdformat-gfm = "^0.3.5"
 types-orjson = "^3.6.2"
 types-python-slugify = "^7.0.0.1"
-types-requests = "^2.28.11.15"
+types-requests = "^2.28.11.17"
 types-setuptools = "^65.7.0.4"
-types-toml = "^0.10.8.5"
+types-toml = "^0.10.8.6"
 types-ujson = "^5.7.0.1"
-pyinstaller = "^5.8.0"
+pyinstaller = "^5.9.0"
 mkdocs = "^1.4.2"
-mkdocs-material = "^9.1.0"
+isort = [
+    {version = "^5.11.4", python = "<3.8"},
+    {version = "^5.12.0", python = ">=3.8"},
+]
+dill = "^0.3.6"
+mkdocs-material = "^9.1.5"
 mkdocstrings = "^0.19.1"
 mkdocstrings-python = "^0.8.3"
-pymdown-extensions = "^9.9.2"
+pymdown-extensions = "^9.10"
 mkdocs-gen-files = "^0.4.0"
 mkdocs-literate-nav = "^0.6.0"
 mkdocs-section-index = "^0.3.5"
 
 [tool.poetry.scripts]
 spotdl = "spotdl:console_entry_point"
 
-[tool.poetry.group.dev.dependencies]
-isort = "^5.11.4"
-
 [tool.isort]
 profile = "black"
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.pylint.format]
 limit-inference-results = 0
 fail-under = 9
 
+[tool.pytest.ini_options]
+asyncio_mode = "auto"
+markers = [
+    "vcr",
+]
+
 [mypy]
 ignore_missing_imports = true
```

### Comparing `spotdl-4.1.3/spotdl/__init__.py` & `spotdl-4.1.4/spotdl/__init__.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/download.py` & `spotdl-4.1.4/spotdl/console/download.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/entry_point.py` & `spotdl-4.1.4/spotdl/console/entry_point.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/meta.py` & `spotdl-4.1.4/spotdl/console/meta.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """
 Sync Lyrics module for the console
 """
 
 import asyncio
 import logging
 from pathlib import Path
-from typing import List, Optional
+from typing import List
 
 from spotdl.download.downloader import Downloader
 from spotdl.types.song import Song
 from spotdl.utils.ffmpeg import FFMPEG_FORMATS
 from spotdl.utils.metadata import embed_metadata, get_file_metadata
-from spotdl.utils.search import get_search_results, get_song_from_file_metadata
+from spotdl.utils.search import QueryError, get_search_results, reinit_song
 
 __all__ = ["meta"]
 
 logger = logging.getLogger(__name__)
 
 
 def meta(query: List[str], downloader: Downloader) -> None:
@@ -49,47 +49,59 @@
                 continue
 
             paths.append(test_path)
 
     def process_file(file: Path):
         song_meta = get_file_metadata(file, downloader.settings["id3_separator"])
 
+        # Check if song has metadata
+        # and if it has all the required fields
+        # if it has all of these fields, we can assume that the metadata is correct
         if song_meta and not downloader.settings["force_update_metadata"]:
             if (
                 song_meta.get("artist")
                 and song_meta.get("artists")
                 and song_meta.get("name")
                 and song_meta.get("lyrics")
                 and song_meta.get("album_art")
             ):
                 logger.info("Song already has metadata: %s", file.name)
                 return None
 
-        song: Optional[Song] = None
-        if not song_meta or None in [
-            song_meta.get("name"),
-            song_meta.get("album_art"),
-            song_meta.get("artist"),
-            song_meta.get("artists"),
-            song_meta.get("track_number"),
-        ]:
-            logger.debug("Searching for metadata for %s", file.name)
+        # Same as above
+        if (
+            not song_meta
+            or None
+            in [
+                song_meta.get("name"),
+                song_meta.get("album_art"),
+                song_meta.get("artist"),
+                song_meta.get("artists"),
+                song_meta.get("track_number"),
+            ]
+            or downloader.settings["force_update_metadata"]
+        ):
+            # Song does not have metadata, or it is missing some fields
+            # or we are forcing update of metadata
+            # so we search for it
+            logger.debug("Searching metadata for %s", file.name)
             search_results = get_search_results(file.stem)
             if not search_results:
                 logger.error("Could not find metadata for %s", file.name)
                 return None
+
             song = search_results[0]
         else:
-            song = get_song_from_file_metadata(
-                file, downloader.settings["id3_separator"]
-            )
-
-        if song is None:
-            logger.error("Could not find metadata for %s", file.name)
-            return None
+            # Song has metadata, so we use it to reinitialize the song object
+            # and fill in the missing metadata
+            try:
+                song = reinit_song(Song.from_missing_data(**song_meta))
+            except QueryError:
+                logger.error("Could not find metadata for %s", file.name)
+                return None
 
         # Check if the song has lyric
         # if not use downloader to find lyrics
         if song_meta is None or song_meta.get("lyrics") is None:
             logger.debug("Fetching lyrics for %s", song.display_name)
             song.lyrics = downloader.search_lyrics(song)
             if song.lyrics:
```

### Comparing `spotdl-4.1.3/spotdl/console/save.py` & `spotdl-4.1.4/spotdl/console/save.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/sync.py` & `spotdl-4.1.4/spotdl/console/sync.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/url.py` & `spotdl-4.1.4/spotdl/console/url.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/console/web.py` & `spotdl-4.1.4/spotdl/console/web.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/download/downloader.py` & `spotdl-4.1.4/spotdl/download/downloader.py`

 * *Files 1% similar despite different names*

```diff
@@ -690,24 +690,24 @@
                 embed_metadata(output_file, song, self.settings["id3_separator"])
             except Exception as exception:
                 raise MetadataError(
                     "Failed to embed metadata to the song"
                 ) from exception
 
             if self.settings["generate_lrc"]:
-                if is_lrc_valid(song.lyrics):
+                if song.lyrics and is_lrc_valid(song.lyrics):
                     lrc_data = song.lyrics
                 else:
                     try:
                         lrc_data = syncedlyrics_search(song.display_name)
                     except Exception:
                         lrc_data = None
 
                 if lrc_data:
-                    save_lrc_file(output_file.with_suffix(".lrc"), lrc_data)
+                    save_lrc_file(str(output_file.with_suffix(".lrc")), lrc_data)
                     logger.debug("Saved lrc file for %s", song.display_name)
                 else:
                     logger.debug("No lrc file found for %s", song.display_name)
 
             display_progress_tracker.notify_complete()
 
             # Add the song to the known songs
```

### Comparing `spotdl-4.1.3/spotdl/download/progress_handler.py` & `spotdl-4.1.4/spotdl/download/progress_handler.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/providers/audio/base.py` & `spotdl-4.1.4/spotdl/providers/audio/base.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/providers/audio/youtube.py` & `spotdl-4.1.4/spotdl/providers/audio/youtube.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/providers/audio/ytmusic.py` & `spotdl-4.1.4/spotdl/providers/audio/ytmusic.py`

 * *Files 6% similar despite different names*

```diff
@@ -18,16 +18,16 @@
 class YouTubeMusic(AudioProvider):
     """
     YouTube Music audio provider class
     """
 
     SUPPORTS_ISRC = True
     GET_RESULTS_OPTS: List[Dict[str, Any]] = [
-        {"filter": "songs", "ignore_spelling": True},
-        {"filter": "videos", "ignore_spelling": True},
+        {"filter": "songs", "ignore_spelling": True, "limit": 50},
+        {"filter": "videos", "ignore_spelling": True, "limit": 50},
     ]
 
     def __init__(self, *args: Any, **kwargs: Any) -> None:
         """
         Initialize the YouTube Music API
 
         ### Arguments
@@ -36,15 +36,15 @@
         """
 
         super().__init__(*args, **kwargs)
 
         client_session = session()
         if kwargs.get("geo_bypass"):
             client_session.headers.update(
-                {"X-Forwarded-For": GeoUtils.random_ipv4("US")}
+                {"X-Forwarded-For": GeoUtils.random_ipv4("US")}  # type: ignore
             )
 
         self.client = YTMusic(language="de", requests_session=client_session)  # type: ignore
 
     def get_results(self, search_term: str, **kwargs) -> List[Result]:
         """
         Get results from YouTube Music API and simplify them
```

### Comparing `spotdl-4.1.3/spotdl/providers/lyrics/azlyrics.py` & `spotdl-4.1.4/spotdl/providers/lyrics/azlyrics.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """
 AZLyrics lyrics module.
 """
 
-from typing import List, Optional
+from typing import Dict, List, Optional
 
 import requests
 from bs4 import BeautifulSoup
 
 from spotdl.providers.lyrics.base import LyricsProvider
 
 __all__ = ["AzLyrics"]
@@ -19,68 +19,101 @@
 
     def __init__(self):
         super().__init__()
 
         self.session = requests.Session()
         self.session.headers.update(self.headers)
 
-        # Not sure if this is needed
-        # but it doesn't hurt
         self.session.get("https://www.azlyrics.com/")
 
         resp = self.session.get("https://www.azlyrics.com/geo.js")
 
         # extract value from js code
         js_code = resp.text
         start_index = js_code.find('value"') + 9
         end_index = js_code[start_index:].find('");')
 
         self.x_code = js_code[start_index : start_index + end_index]
 
-    def get_lyrics(self, name: str, artists: List[str], **_) -> Optional[str]:
+    def get_results(self, name: str, artists: List[str], **kwargs) -> Dict[str, str]:
         """
-        Try to get lyrics from azlyrics
+        Returns the results for the given song.
 
         ### Arguments
         - name: The name of the song.
         - artists: The artists of the song.
+        - kwargs: Additional arguments.
 
         ### Returns
-        - The lyrics of the song or None if no lyrics were found.
+        - A dictionary with the results. (The key is the title and the value is the url.)
         """
 
         # Join every artist by comma in artists
         artist_str = ", ".join(artist for artist in artists if artist)
 
         params = {
             "q": f"{artist_str} - {name}",
             "x": self.x_code,
         }
 
-        response = self.session.get(
-            "https://search.azlyrics.com/search.php", params=params
-        )
-        soup = BeautifulSoup(response.content, "html.parser")
+        counter = 0
+        soup = None
+        while counter < 4:
+            try:
+                response = self.session.get(
+                    "https://search.azlyrics.com/search.php", params=params
+                )
+            except requests.ConnectionError:
+                continue
+
+            if not response.ok:
+                counter += 1
+                continue
+
+            soup = BeautifulSoup(response.content, "html.parser")
+            break
+
+        if soup is None:
+            return {}
 
         td_tags = soup.find_all("td")
         if len(td_tags) == 0:
-            return None
+            return {}
+
+        results = {}
+        for td_tag in td_tags:
+            a_tags = td_tag.find_all("a", href=True)
+            if len(a_tags) == 0:
+                continue
+
+            a_tag = a_tags[0]
+            url = a_tag["href"].strip()
+            if url == "":
+                continue
+
+            title = td_tag.find("span").get_text().strip()
+            artist = td_tag.find("b").get_text().strip()
 
-        result = td_tags[0]
+            results[f"{artist} - {title}"] = url
 
-        a_tags = result.find_all("a", href=True)
-        if len(a_tags) != 0:
-            lyrics_url = a_tags[0]["href"]
-        else:
-            return None
+        return results
 
-        if lyrics_url.strip() == "":
-            return None
+    def extract_lyrics(self, url: str, **_) -> Optional[str]:
+        """
+        Extracts the lyrics from the given url.
+
+        ### Arguments
+        - url: The url to extract the lyrics from.
+        - kwargs: Additional arguments.
+
+        ### Returns
+        - The lyrics of the song or None if no lyrics were found.
+        """
 
-        response = self.session.get(lyrics_url)
+        response = self.session.get(url)
         soup = BeautifulSoup(response.content, "html.parser")
 
         # Find all divs that don't have a class
         div_tags = soup.find_all("div", class_=False, id_=False)
 
         # Find the div with the longest text
         lyrics_div = sorted(div_tags, key=lambda x: len(x.text))[-1]
```

### Comparing `spotdl-4.1.3/spotdl/providers/lyrics/genius.py` & `spotdl-4.1.4/spotdl/providers/lyrics/genius.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,88 +1,118 @@
 """
 Genius Lyrics module.
 """
 
-from typing import List, Optional
+from typing import Dict, List, Optional
 
 import requests
 from bs4 import BeautifulSoup
 
 from spotdl.providers.lyrics.base import LyricsProvider
 
 __all__ = ["Genius"]
 
 
 class Genius(LyricsProvider):
     """
     Genius lyrics provider class.
     """
 
-    def get_lyrics(self, name: str, artists: List[str], **_) -> Optional[str]:
+    def __init__(self):
         """
-        Try to get lyrics from genius
+        Init the lyrics provider search and set headers.
+        """
+
+        super().__init__()
+
+        self.headers.update(
+            {
+                "Authorization": "Bearer "
+                "alXXDbPZtK1m2RrZ8I4k2Hn8Ahsd0Gh_o076HYvcdlBvmc0ULL1H8Z8xRlew5qaG",
+            }
+        )
+
+    def get_results(self, name: str, artists: List[str], **_) -> Dict[str, str]:
+        """
+        Returns the results for the given song.
 
         ### Arguments
         - name: The name of the song.
         - artists: The artists of the song.
+        - kwargs: Additional arguments.
 
         ### Returns
-        - The lyrics of the song or None if no lyrics were found.
+        - A dictionary with the results. (The key is the title and the value is the url.)
         """
 
-        try:
-            headers = {
-                "Authorization": "Bearer "
-                "alXXDbPZtK1m2RrZ8I4k2Hn8Ahsd0Gh_o076HYvcdlBvmc0ULL1H8Z8xRlew5qaG",
-            }
+        artists_str = ", ".join(artists)
+        title = f"{name} - {artists_str}"
 
-            headers.update(self.headers)
+        search_response = requests.get(
+            "https://api.genius.com/search",
+            params={"q": title},
+            headers=self.headers,
+            timeout=10,
+        )
+
+        results: Dict[str, str] = {}
+        for hit in search_response.json()["response"]["hits"]:
+            results[hit["result"]["full_title"]] = hit["result"]["id"]
 
-            artist_str = ", ".join(
-                artist for artist in artists if artist.lower() not in name.lower()
-            )
+        return results
 
-            search_response = requests.get(
-                "https://api.genius.com/search",
-                params={"q": f"{name} {artist_str}"},
-                headers=headers,
-                timeout=10,
-            )
+    def extract_lyrics(self, url: str, **_) -> Optional[str]:
+        """
+        Extracts the lyrics from the given url.
 
-            song_id = search_response.json()["response"]["hits"][0]["result"]["id"]
+        ### Arguments
+        - url: The url to extract the lyrics from.
+        - kwargs: Additional arguments.
 
-            song_response = requests.get(
-                f"https://api.genius.com/songs/{song_id}", headers=headers, timeout=10
-            )
+        ### Returns
+        - The lyrics of the song or None if no lyrics were found.
+        """
+
+        url = f"https://api.genius.com/songs/{url}"
+        song_response = requests.get(url, headers=self.headers, timeout=10)
+        url = song_response.json()["response"]["song"]["url"]
+
+        soup = None
+        counter = 0
+        while counter < 4:
+            genius_page_response = requests.get(url, headers=self.headers, timeout=10)
+
+            if not genius_page_response.ok:
+                counter += 1
+                continue
 
-            song_url = song_response.json()["response"]["song"]["url"]
+            soup = BeautifulSoup(
+                genius_page_response.text.replace("<br/>", "\n"), "html.parser"
+            )
 
-            counter = 0
-            soup = None
-            while counter < 4:
-                genius_page_response = requests.get(
-                    song_url, headers=self.headers, timeout=10
-                )
+            break
 
-                if not genius_page_response.ok:
-                    counter += 1
-                    continue
+        if soup is None:
+            return None
 
-                soup = BeautifulSoup(
-                    genius_page_response.text.replace("<br/>", "\n"), "html.parser"
-                )
+        lyrics_div = soup.select_one("div.lyrics")
+        lyrics_containers = soup.select("div[class^=Lyrics__Container]")
 
-                break
+        # Get lyrics
+        if lyrics_div:
+            lyrics = lyrics_div.get_text()
+        elif lyrics_containers:
+            lyrics = "\n".join(con.get_text() for con in lyrics_containers)
+        else:
+            return None
 
-            if soup is None:
-                return None
+        if not lyrics:
+            return None
 
-            lyrics_div = soup.select_one("div.lyrics")
+        # Clean lyrics
+        lyrics = lyrics.strip()
 
-            if lyrics_div is not None:
-                return lyrics_div.get_text().strip()
+        # Remove desc at the beginning if it exists
+        for to_remove in ["desc", "Desc"]:
+            lyrics.replace(to_remove, "", 1)
 
-            lyrics_containers = soup.select("div[class^=Lyrics__Container]")
-            lyrics = "\n".join(con.get_text() for con in lyrics_containers)
-            return lyrics.strip()
-        except Exception:
-            return None
+        return lyrics
```

### Comparing `spotdl-4.1.3/spotdl/providers/lyrics/musixmatch.py` & `spotdl-4.1.4/spotdl/providers/lyrics/musixmatch.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """
 MusixMatch lyrics provider.
 """
 
-from typing import List, Optional
+from typing import Dict, List, Optional
 from urllib.parse import quote
 
 import requests
 from bs4 import BeautifulSoup
 
 from spotdl.providers.lyrics.base import LyricsProvider
 
@@ -14,62 +14,76 @@
 
 
 class MusixMatch(LyricsProvider):
     """
     MusixMatch lyrics provider class.
     """
 
-    def get_lyrics(self, name: str, artists: List[str], **kwargs) -> Optional[str]:
+    def extract_lyrics(self, url: str, **kwargs) -> Optional[str]:
         """
-        Try to get lyrics from musixmatch
+        Extracts the lyrics from the given url.
 
         ### Arguments
-        - name: The name of the song.
-        - artists: The artists of the song.
+        - url: The url to extract the lyrics from.
         - kwargs: Additional arguments.
 
         ### Returns
         - The lyrics of the song or None if no lyrics were found.
         """
 
-        try:
-            track_search = kwargs.get("track_search", False)
+        lyrics_resp = requests.get(url, headers=self.headers, timeout=10)
 
-            artists_str = ", ".join(
-                artist for artist in artists if artist.lower() not in name.lower()
-            )
+        lyrics_soup = BeautifulSoup(lyrics_resp.text, "html.parser")
+        lyrics_paragraphs = lyrics_soup.select("p.mxm-lyrics__content")
+        lyrics = "\n".join(i.get_text() for i in lyrics_paragraphs)
 
-            # quote the query so that it's safe to use in a url
-            # e.g "Au/Ra" -> "Au%2FRa"
-            query = quote(f"{name} - {artists_str}", safe="")
+        return lyrics
 
-            # search the `tracks page` if track_search is True
-            if track_search:
-                query += "/tracks"
+    def get_results(self, name: str, artists: List[str], **kwargs) -> Dict[str, str]:
+        """
+        Returns the results for the given song.
+
+        ### Arguments
+        - name: The name of the song.
+        - artists: The artists of the song.
+        - kwargs: Additional arguments.
 
-            search_url = f"https://www.musixmatch.com/search/{query}"
-            search_resp = requests.get(search_url, headers=self.headers, timeout=10)
+        ### Returns
+        - A dictionary with the results. (The key is the title and the value is the url.)
+        """
 
-            search_soup = BeautifulSoup(search_resp.text, "html.parser")
-            song_url_tag = search_soup.select_one("a[href^='/lyrics/']")
+        track_search = kwargs.get("track_search", False)
+        artists_str = ", ".join(
+            artist for artist in artists if artist.lower() not in name.lower()
+        )
+
+        # quote the query so that it's safe to use in a url
+        # e.g "Au/Ra" -> "Au%2FRa"
+        query = quote(f"{name} - {artists_str}", safe="")
+
+        # search the `tracks page` if track_search is True
+        if track_search:
+            query += "/tracks"
+
+        search_url = f"https://www.musixmatch.com/search/{query}"
+        search_resp = requests.get(search_url, headers=self.headers, timeout=10)
+        search_soup = BeautifulSoup(search_resp.text, "html.parser")
+        song_url_tag = search_soup.select("a[href^='/lyrics/']")
 
+        if not song_url_tag:
             # song_url_tag being None means no results were found on the
             # All Results page, therefore, we use `track_search` to
             # search the tracks page.
-            if song_url_tag is None:
-                # track_serach being True means we are already searching the tracks page.
-                if track_search:
-                    return None
-
-                lyrics = self.get_lyrics(name, artists, track_search=True)
-                return lyrics
-
-            song_url = "https://www.musixmatch.com" + str(song_url_tag.get("href", ""))
-            lyrics_resp = requests.get(song_url, headers=self.headers, timeout=10)
-
-            lyrics_soup = BeautifulSoup(lyrics_resp.text, "html.parser")
-            lyrics_paragraphs = lyrics_soup.select("p.mxm-lyrics__content")
-            lyrics = "\n".join(i.get_text() for i in lyrics_paragraphs)
-
-            return lyrics
-        except Exception:
-            return None
+
+            # track_serach being True means we are already searching the tracks page.
+            if track_search:
+                return {}
+
+            return self.get_results(name, artists, track_search=True)
+
+        results: Dict[str, str] = {}
+        for tag in song_url_tag:
+            results[tag.get_text()] = "https://www.musixmatch.com" + str(
+                tag.get("href", "")
+            )
+
+        return results
```

### Comparing `spotdl-4.1.3/spotdl/providers/lyrics/synced.py` & `spotdl-4.1.4/spotdl/providers/lyrics/synced.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,34 +1,64 @@
 """
 Synced lyrics provider using the syncedlyrics library
 """
 
-from typing import List, Optional
+from typing import Dict, List, Optional
 
 import syncedlyrics
 
 from spotdl.providers.lyrics.base import LyricsProvider
 
 __all__ = ["Synced"]
 
 
 class Synced(LyricsProvider):
     """
     Lyrics provider for synced lyrics using the syncedlyrics library
     Currently supported websites: Deezer, NetEase
     """
 
+    def get_results(self, name: str, artists: List[str], **kwargs) -> Dict[str, str]:
+        """
+        Returns the results for the given song.
+
+        ### Arguments
+        - name: The name of the song.
+        - artists: The artists of the song.
+        - kwargs: Additional arguments.
+
+        ### Returns
+        - A dictionary with the results. (The key is the title and the value is the url.)
+        """
+
+        raise NotImplementedError
+
+    def extract_lyrics(self, url: str, **kwargs) -> Optional[str]:
+        """
+        Extracts the lyrics from the given url.
+
+        ### Arguments
+        - url: The url to extract the lyrics from.
+        - kwargs: Additional arguments.
+
+        ### Returns
+        - The lyrics of the song or None if no lyrics were found.
+        """
+
+        raise NotImplementedError
+
     def get_lyrics(self, name: str, artists: List[str], **_) -> Optional[str]:
         """
         Try to get lyrics using syncedlyrics
 
         ### Arguments
         - name: The name of the song.
         - artists: The artists of the song.
         - kwargs: Additional arguments.
 
         ### Returns
         - The lyrics of the song or None if no lyrics were found.
         """
 
         lyrics = syncedlyrics.search(f"{name} - {artists[0]}", allow_plain_format=True)
+
         return lyrics
```

### Comparing `spotdl-4.1.3/spotdl/types/album.py` & `spotdl-4.1.4/spotdl/types/album.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/types/artist.py` & `spotdl-4.1.4/spotdl/types/artist.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/types/options.py` & `spotdl-4.1.4/spotdl/types/options.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/types/playlist.py` & `spotdl-4.1.4/spotdl/types/playlist.py`

 * *Files 2% similar despite different names*

```diff
@@ -109,15 +109,15 @@
                 album_id=album_meta.get("id"),
                 album_name=album_meta.get("name"),
                 album_artist=album_meta.get("artists", [])[0]["name"]
                 if album_meta.get("artists")
                 else None,
                 disc_number=track_meta["disc_number"],
                 duration=track_meta["duration_ms"],
-                year=release_date[:4],
+                year=release_date[:4] if release_date else None,
                 date=release_date,
                 track_number=track_meta["track_number"],
                 tracks_count=album_meta.get("total_tracks"),
                 song_id=track_meta["id"],
                 explicit=track_meta["explicit"],
                 url=track_meta["external_urls"]["spotify"],
                 isrc=track_meta.get("external_ids", {}).get("isrc"),
```

### Comparing `spotdl-4.1.3/spotdl/types/result.py` & `spotdl-4.1.4/spotdl/types/result.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/types/saved.py` & `spotdl-4.1.4/spotdl/types/saved.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/types/song.py` & `spotdl-4.1.4/spotdl/types/song.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/archive.py` & `spotdl-4.1.4/spotdl/utils/archive.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/arguments.py` & `spotdl-4.1.4/spotdl/utils/arguments.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/config.py` & `spotdl-4.1.4/spotdl/utils/config.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/console.py` & `spotdl-4.1.4/spotdl/utils/console.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/downloader.py` & `spotdl-4.1.4/spotdl/utils/downloader.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/ffmpeg.py` & `spotdl-4.1.4/spotdl/utils/ffmpeg.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/formatter.py` & `spotdl-4.1.4/spotdl/utils/formatter.py`

 * *Files 4% similar despite different names*

```diff
@@ -215,15 +215,15 @@
     # the code below is valid, song_list is actually checked for None
     formats = {
         "{title}": song.name,
         "{artists}": song.artists[0] if short is True else artists_str,
         "{artist}": song.artists[0],
         "{album}": song.album_name,
         "{album-artist}": song.album_artist,
-        "{genre}": song.genres[0] if len(song.genres) > 0 else "",
+        "{genre}": song.genres[0] if song.genres else "",
         "{disc-number}": song.disc_number,
         "{disc-count}": song.disc_count,
         "{duration}": song.duration,
         "{year}": song.year,
         "{original-date}": song.date,
         "{track-number}": f"{song.track_number:02d}",
         "{tracks-count}": song.tracks_count,
@@ -299,17 +299,20 @@
 
     ### Returns
     - the formatted string as a Path object
     """
 
     # If template does not contain any of the keys,
     # append {artists} - {title}.{output-ext} to it
-    if not any(key in template for key in VARS):
+    if not any(key in template for key in VARS) and template != "":
         template += "/{artists} - {title}.{output-ext}"
 
+    if template == "":
+        template = "{artists} - {title}.{output-ext}"
+
     # If template ends with a slash. Does not have a file name with extension
     # at the end of the template, append {artists} - {title}.{output-ext} to it
     if template.endswith("/") or template.endswith(r"\\") or template.endswith("\\\\"):
         template += "/{artists} - {title}.{output-ext}"
 
     # If template does not end with {output-ext}, append it to the end of the template
     if not template.endswith(".{output-ext}"):
@@ -334,47 +337,79 @@
         else:
             santitized_parts.append(part)
 
     # Join the parts of the path
     file = Path(*santitized_parts)
 
     # Check if the file name length is greater than 255
-    if len(file.name) > 255:
-        # If the file name length is greater than 255,
-        # and we are already using the short version of the template,
-        # fallback to default template
-        if short is True:
-            # This will probably never occur, but just in case
-            if template == "/{artist} - {title}.{output-ext}":
-                raise RecursionError(
-                    f'"{song.display_name} is too long to be shortened. File a bug report on GitHub'
+    if len(file.name) < 255:
+        # Restrict the filename if needed
+        if restrict:
+            return restrict_filename(file)
+
+        return file
+
+    # If the file name length is greater than 255,
+    # and we are already using the short version of the template,
+    # fallback to default template
+    if short is True:
+        # Path template is already short, but we still can't create a file
+        # so we reduce it even further
+        if template == "{artist} - {title}.{output-ext}":
+            if len(song.name) > 240:
+                logger.warning(
+                    "%s: File name is too long. Using only part of the song title.",
+                    song.display_name,
                 )
 
-            logger.warning(
-                "%s: File name is too long. Using the default template.",
-                song.display_name,
-            )
+                name_parts = song.name.split(" ")
+                new_name = ""
+                for part in name_parts:
+                    if len(new_name) + len(part) < 240:
+                        new_name += part + " "
+                    else:
+                        break
+
+                song.name = new_name.strip()
+            else:
+                logger.warning(
+                    "%s: File name is too long. Using only song title.",
+                    song.display_name,
+                )
 
             return create_file_name(
                 song=song,
-                template="/{artist} - {title}.{output-ext}",
+                template="{title}.{output-ext}",
                 file_extension=file_extension,
                 restrict=restrict,
                 short=short,
             )
 
-        return create_file_name(
-            song, template, file_extension, restrict=restrict, short=True
+        # This will probably never occur, but just in case
+        if template == "{title}.{output-ext}":
+            raise RecursionError(
+                f'"{song.display_name} is too long to be shortened. File a bug report on GitHub'
+            )
+
+        logger.warning(
+            "%s: File name is too long. Using the default template.",
+            song.display_name,
         )
 
-    # Restrict the filename if needed
-    if restrict:
-        return restrict_filename(file)
+        return create_file_name(
+            song=song,
+            template="{artist} - {title}.{output-ext}",
+            file_extension=file_extension,
+            restrict=restrict,
+            short=short,
+        )
 
-    return file
+    return create_file_name(
+        song, template, file_extension, restrict=restrict, short=True
+    )
 
 
 def parse_duration(duration: Optional[str]) -> float:
     """
     Convert string value of time (duration: "25:36:59") to a float value of seconds (92219.0)
 
     ### Arguments
```

### Comparing `spotdl-4.1.3/spotdl/utils/github.py` & `spotdl-4.1.4/spotdl/utils/github.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/logging.py` & `spotdl-4.1.4/spotdl/utils/logging.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/m3u.py` & `spotdl-4.1.4/spotdl/utils/m3u.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/matching.py` & `spotdl-4.1.4/spotdl/utils/matching.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 """
 Module for all things matching related
 """
 
 import logging
-from itertools import zip_longest
+from itertools import product, zip_longest
 from typing import Dict, List, Optional, Tuple
 
 from spotdl.types.result import Result
 from spotdl.types.song import Song
 from spotdl.utils.formatter import (
     create_search_query,
     create_song_title,
@@ -256,16 +256,26 @@
 
     main_artist_match = 0.0
 
     # Result has no artists, return 0.0
     if not result.artists:
         return main_artist_match
 
+    song_artists, result_artists = list(map(slugify, song.artists)), list(
+        map(slugify, result.artists)
+    )
+    sorted_song_artists, sorted_result_artists = based_sort(
+        song_artists, result_artists
+    )
+
+    debug(song.song_id, result.result_id, f"Song artists: {sorted_song_artists}")
+    debug(song.song_id, result.result_id, f"Result artists: {sorted_result_artists}")
+
     slug_song_main_artist = slugify(song.artists[0])
-    slug_result_main_artist = slugify(result.artists[0])
+    slug_result_main_artist = sorted_result_artists[0]
 
     # Result has only one artist, but song has multiple artists
     # we can assume that other artists are in the main artist name
     if len(song.artists) > 1 and len(result.artists) == 1:
         for artist in map(slugify, song.artists[1:]):
             artist = sort_string(slugify(artist).split("-"), "-")
 
@@ -273,15 +283,37 @@
 
             if artist in res_main_artist:
                 main_artist_match += 100 / len(song.artists)
 
         return main_artist_match
 
     # Match main result artist with main song artist
-    return ratio(slug_song_main_artist, slug_result_main_artist)
+    main_artist_match = ratio(slug_song_main_artist, slug_result_main_artist)
+
+    debug(
+        song.song_id, result.result_id, f"First main artist match: {main_artist_match}"
+    )
+
+    # Use second artist from the sorted list to
+    # calculate the match if the first artist match is too low
+    if main_artist_match < 50 and len(song_artists) > 1:
+        for song_artist, result_artist in product(
+            song_artists[:2], sorted_result_artists[:2]
+        ):
+            new_artist_match = ratio(song_artist, result_artist)
+            debug(
+                song.song_id,
+                result.result_id,
+                f"Matched {song_artist} with {result_artist}: {new_artist_match}",
+            )
+
+            if new_artist_match > main_artist_match:
+                main_artist_match = new_artist_match
+
+    return main_artist_match
 
 
 def calc_artists_match(song: Song, result: Result) -> float:
     """
     Check if all artists are present in list of artists
 
     ### Arguments
@@ -294,38 +326,26 @@
 
     artist_match_number = 0.0
 
     # Result has only one artist, return 0.0
     if len(song.artists) == 1 or not result.artists:
         return artist_match_number
 
-    slug_song_artists = slugify(", ".join(song.artists))
-    slug_result_artists = slugify(", ".join(result.artists)) if result.artists else ""
+    artist1_list, artist2_list = based_sort(
+        list(map(slugify, song.artists)), list(map(slugify, result.artists))
+    )
 
-    # match the song's artists with the result's artists
-    # if the number of artists is the same
-    if len(song.artists) == len(result.artists):
-        return ratio(slug_song_artists, slug_result_artists)
-
-    # Calculate the percentage of artists that are present in the result
-    artists_percentage = (len(result.artists) * 100) / len(song.artists)
-
-    if artists_percentage > 60 and len(song.artists) > 2:
-        # Create lists of artists in song and result
-        # After that sort them based on the order of the result's artists
-        artist1_list, artist2_list = based_sort(
-            list(map(slugify, song.artists)), list(map(slugify, result.artists))
-        )
+    artists_match = 0.0
+    for artist1, artist2 in zip_longest(artist1_list, artist2_list):
+        artist12_match = ratio(artist1, artist2)
+        artists_match += artist12_match
 
-        artists_match = 0.0
-        for artist1, artist2 in zip_longest(artist1_list, artist2_list):
-            artist12_match = ratio(artist1, artist2)
-            artists_match += artist12_match
+    artist_match_number = artists_match / len(artist1_list)
 
-        artist_match_number = artists_match / len(artist1_list)
+    debug(song.song_id, result.result_id, f"Artists match: {artist_match_number}")
 
     return artist_match_number
 
 
 def artists_match_fixup1(song: Song, result: Result, score: float) -> float:
     """
     Multiple fixes to the artists score for
@@ -628,20 +648,24 @@
                 song.song_id, result.result_id, "Skipping result due to no common words"
             )
 
             continue
 
         # Calculate match value for main artist
         artists_match = calc_main_artist_match(song, result)
-
         debug(song.song_id, result.result_id, f"Main artist match: {artists_match}")
 
         # Calculate match value for all artists
-        artists_match += calc_artists_match(song, result)
-        debug(song.song_id, result.result_id, f"Artists match: {artists_match}")
+        other_artists_match = calc_artists_match(song, result)
+        debug(
+            song.song_id,
+            result.result_id,
+            f"Other artists match: {other_artists_match}",
+        )
+        artists_match += other_artists_match
 
         # Calculate initial artist match value
         artists_match = artists_match / (2 if len(song.artists) > 1 else 1)
         debug(song.song_id, result.result_id, f"Initial artists match: {artists_match}")
 
         # First attempt to fix artist match
         artists_match = artists_match_fixup1(song, result, artists_match)
@@ -663,14 +687,16 @@
         artists_match = artists_match_fixup3(song, result, artists_match)
         debug(
             song.song_id,
             result.result_id,
             f"Artists match after fixup3: {artists_match}",
         )
 
+        debug(song.song_id, result.result_id, f"Final artists match: {artists_match}")
+
         # Calculate name match
         name_match = calc_name_match(song, result, search_query)
         debug(song.song_id, result.result_id, f"Final name match: {name_match}")
 
         # Calculate album match
         album_match = calc_album_match(song, result)
         debug(song.song_id, result.result_id, f"Final album match: {album_match}")
```

### Comparing `spotdl-4.1.3/spotdl/utils/metadata.py` & `spotdl-4.1.4/spotdl/utils/metadata.py`

 * *Files 1% similar despite different names*

```diff
@@ -163,15 +163,15 @@
     audio_file[tag_preset["encodedby"]] = song.publisher
 
     # Embed metadata that isn't always present
     album_name = song.album_name
     if album_name:
         audio_file[tag_preset["album"]] = album_name
 
-    if len(song.genres) > 0:
+    if song.genres:
         audio_file[tag_preset["genre"]] = song.genres[0].title()
 
     if song.copyright_text:
         audio_file[tag_preset["copyright"]] = song.copyright_text
 
     if song.download_url and encoding != "mp3":
         audio_file[tag_preset["comment"]] = song.download_url
@@ -417,19 +417,18 @@
                 count = val.text[0].split(id3_separator)
                 if len(count) == 2:
                     song_meta["disc_number"] = int(count[0])
                     song_meta["disc_count"] = int(count[1])
                 else:
                     song_meta["disc_number"] = val.text[0]
             elif key == "artist":
-                song_meta["artists"] = (
-                    val.text[0]
-                    if isinstance(val.text, list) and len(val.text) == 1
-                    else val.text
-                ).split(id3_separator)
+                artists_val: str = (
+                    val.text[0] if isinstance(val.text, list) else val.text
+                )
+                song_meta["artists"] = artists_val.split(id3_separator)
             else:
                 meta_key = TAG_TO_SONG.get(key)
                 if meta_key:
                     song_meta[meta_key] = (
                         val.text[0]
                         if isinstance(val.text, list) and len(val.text) == 1
                         else val.text
```

### Comparing `spotdl-4.1.3/spotdl/utils/search.py` & `spotdl-4.1.4/spotdl/utils/search.py`

 * *Files 8% similar despite different names*

```diff
@@ -29,15 +29,30 @@
     "get_song_from_file_metadata",
     "gather_known_songs",
     "create_ytm_album",
     "create_ytm_playlist",
 ]
 
 logger = logging.getLogger(__name__)
-client = YTMusic()
+client = None  # pylint: disable=invalid-name
+
+
+def get_ytm_client() -> YTMusic:
+    """
+    Lazily initialize the YTMusic client.
+
+    ### Returns
+    - the YTMusic client
+    """
+
+    global client  # pylint: disable=global-statement
+    if client is None:
+        client = YTMusic()
+
+    return client
 
 
 class QueryError(Exception):
     """
     Base class for all exceptions related to query.
     """
 
@@ -72,16 +87,21 @@
     - List of song objects
     """
 
     songs: List[Song] = get_simple_songs(query, use_ytm_data=use_ytm_data)
 
     results = []
     with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
-        for song in executor.map(reinit_song, songs):
-            results.append(song)
+        future_to_song = {executor.submit(reinit_song, song): song for song in songs}
+        for future in concurrent.futures.as_completed(future_to_song):
+            song = future_to_song[future]
+            try:
+                results.append(future.result())
+            except Exception as exc:
+                logger.error("%s generated an exception: %s", song.display_name, exc)
 
     return results
 
 
 def get_simple_songs(
     query: List[str],
     use_ytm_data: bool = False,
@@ -203,19 +223,19 @@
         logger.info(
             "Found %s songs in %s (%s)",
             len(song_list.urls),
             song_list.name,
             song_list.__class__.__name__,
         )
 
-        for song in song_list.songs:
+        for index, song in enumerate(song_list.songs):
             song_data = song.json
             song_data["list_name"] = song_list.name
             song_data["list_url"] = song_list.url
-            song_data["list_position"] = song_list.urls.index(song.url) + 1
+            song_data["list_position"] = index + 1
             song_data["list_length"] = song_list.length
 
             if playlist_numbering:
                 song_data["track_number"] = song_data["list_position"]
                 song_data["tracks_count"] = song_data["list_length"]
                 song_data["album_name"] = song_data["list_name"]
                 song_data["disc_number"] = 1
@@ -352,19 +372,21 @@
     ### Returns
     - a list of Song objects
     """
 
     if "?list=" not in url or not url.startswith("https://music.youtube.com/"):
         raise ValueError(f"Invalid album url: {url}")
 
-    browse_id = client.get_album_browse_id(url.split("?list=")[1].split("&")[0])
+    browse_id = get_ytm_client().get_album_browse_id(
+        url.split("?list=")[1].split("&")[0]
+    )
     if browse_id is None:
         raise ValueError(f"Invalid album url: {url}")
 
-    album = client.get_album(browse_id)
+    album = get_ytm_client().get_album(browse_id)
 
     if album is None:
         raise ValueError(f"Couldn't fetch album: {url}")
 
     metadata = {
         "artist": album["artists"][0]["name"],
         "name": album["title"],
@@ -408,15 +430,15 @@
     ):
         raise ValueError(f"Invalid playlist url: {url}")
 
     if "/browse/VLPL" in url:
         playlist_id = url.split("/browse/")[1]
     else:
         playlist_id = url.split("?list=")[1]
-    playlist = client.get_playlist(playlist_id, None)  # type: ignore
+    playlist = get_ytm_client().get_playlist(playlist_id, None)  # type: ignore
 
     if playlist is None:
         raise ValueError(f"Couldn't fetch playlist: {url}")
 
     metadata = {
         "description": playlist["description"]
         if playlist["description"] is not None
@@ -426,15 +448,15 @@
         "cover_url": playlist["thumbnails"][0]["url"],
         "name": playlist["title"],
         "url": url,
     }
 
     songs = []
     for track in playlist["tracks"]:
-        if track["videoId"] is None:
+        if track["videoId"] is None or track["isAvailable"] is False:
             continue
 
         song = Song.from_missing_data(
             name=track["title"],
             artists=[artist["name"] for artist in track["artists"]],
             artist=track["artists"][0]["name"],
             album_name=track.get("album", {}).get("name")
```

### Comparing `spotdl-4.1.3/spotdl/utils/spotify.py` & `spotdl-4.1.4/spotdl/utils/spotify.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/static.py` & `spotdl-4.1.4/spotdl/utils/static.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/spotdl/utils/web.py` & `spotdl-4.1.4/spotdl/utils/web.py`

 * *Files identical despite different names*

### Comparing `spotdl-4.1.3/PKG-INFO` & `spotdl-4.1.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spotdl
-Version: 4.1.3
+Version: 4.1.4
 Summary: Download your Spotify playlists and songs along with album art and metadata
 Home-page: https://github.com/spotDL/spotify-downloader/
 License: MIT
 Keywords: spotify,downloader,spotdl,music
 Author: spotDL Team
 Author-email: spotdladmins@googlegroups.com
 Maintainer: xnetcat
@@ -23,30 +23,30 @@
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Multimedia
 Classifier: Topic :: Multimedia :: Sound/Audio
 Classifier: Topic :: Utilities
-Requires-Dist: beautifulsoup4 (>=4.11.2,<5.0.0)
+Requires-Dist: beautifulsoup4 (>=4.12.1,<5.0.0)
 Requires-Dist: fastapi (>=0.89.1,<0.90.0)
 Requires-Dist: mutagen (>=1.46.0,<2.0.0)
 Requires-Dist: platformdirs (>=2.6.2,<3.0.0)
-Requires-Dist: pydantic (>=1.10.5,<2.0.0)
+Requires-Dist: pydantic (>=1.10.7,<2.0.0)
 Requires-Dist: pykakasi (>=2.2.1,<3.0.0)
 Requires-Dist: python-slugify[unidecode] (>=8.0.1,<9.0.0)
-Requires-Dist: pytube (>=12.1.2,<13.0.0)
-Requires-Dist: rapidfuzz (>=2.13.7,<3.0.0)
+Requires-Dist: pytube (>=12.1.3,<13.0.0)
+Requires-Dist: rapidfuzz (>=2.15.0,<3.0.0)
 Requires-Dist: requests (>=2.28.2,<3.0.0)
-Requires-Dist: rich (>=13.3.1,<14.0.0)
+Requires-Dist: rich (>=13.3.3,<14.0.0)
 Requires-Dist: spotipy (>=2.22.1,<3.0.0)
-Requires-Dist: syncedlyrics (>=0.2.2,<0.3.0)
+Requires-Dist: syncedlyrics (==0.4.0)
 Requires-Dist: typing-extensions (>=4.5.0,<5.0.0)
 Requires-Dist: uvicorn (>=0.20.0,<0.21.0)
-Requires-Dist: yt-dlp (>=2023.3.3,<2024.0.0)
+Requires-Dist: yt-dlp (>=2023.3.4,<2024.0.0)
 Requires-Dist: ytmusicapi (>=0.22.0,<0.23.0) ; python_version < "3.8"
 Requires-Dist: ytmusicapi (>=0.24.0,<0.25.0) ; python_version >= "3.8"
 Project-URL: Documentation, https://spotdl.rtfd.io/en/latest/
 Project-URL: Repository, https://github.com/spotDL/spotify-downloader.git
 Description-Content-Type: text/markdown
 
 
@@ -183,19 +183,26 @@
 > **Note**
 > Users are responsible for their actions and potential legal consequences. We do not support unauthorized downloading of copyrighted material and take no responsibility for user actions.
 
 ### Audio Quality
 
 spotDL downloads music from YouTube and is designed to always download the highest possible bitrate; which is 128 kbps for regular users and 256 kbps for YouTube Music premium users.
 
-Check the [Audio Formats](docs/USAGE.md#audio-formats-and-quality) page for more info.
+Check the [Audio Formats](docs/usage.md#audio-formats-and-quality) page for more info.
 
 ## Contributing
 
 Interested in contributing? Check out our [CONTRIBUTING.md](docs/CONTRIBUTING.md) to find
 resources around contributing along with a guide on how to set up a development environment.
 
+## Donate
+
+### xnetcat
+
+[![paypal](https://img.shields.io/badge/paypal-%2300457C.svg?&style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/kko7)
+[![kofi](https://img.shields.io/badge/kofi-%23F16061.svg?&style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/xnetcat)
+
 ## License
 
 This project is Licensed under the [MIT](/LICENSE) License.
```

