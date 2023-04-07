# Comparing `tmp/xhs-0.0.4.tar.gz` & `tmp/xhs-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xhs-0.0.4.tar", last modified: Thu Apr  6 10:35:09 2023, max compression
+gzip compressed data, was "xhs-0.1.0.tar", last modified: Fri Apr  7 09:55:12 2023, max compression
```

## Comparing `xhs-0.0.4.tar` & `xhs-0.1.0.tar`

### file list

```diff
@@ -1,26 +1,27 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)      473 2023-04-06 10:34:52.000000 xhs-0.0.4/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-04-06 10:34:52.000000 xhs-0.0.4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-06 10:34:52.000000 xhs-0.0.4/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2921 2023-04-06 10:35:09.091733 xhs-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-04-06 10:34:52.000000 xhs-0.0.4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 10:34:52.000000 xhs-0.0.4/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-04-06 10:35:09.091733 xhs-0.0.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-04-06 10:34:52.000000 xhs-0.0.4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2578 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/test_help.py
--rw-r--r--   0 runner    (1001) docker     (123)     1473 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/test_xhs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/xhs/
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4965 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/core.py
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/exception.py
--rw-r--r--   0 runner    (1001) docker     (123)     1994 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/help.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/xhs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2921 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      369 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:35:08.000000 xhs-0.0.4/xhs.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 09:55:12.222416 xhs-0.1.0/
+-rw-rw-rw-   0        0        0      909 2023-04-07 09:49:39.000000 xhs-0.1.0/CHANGELOG.md
+-rw-rw-rw-   0        0        0     1086 2023-04-03 04:48:59.000000 xhs-0.1.0/LICENSE
+-rw-rw-rw-   0        0        0       85 2023-04-03 14:57:56.000000 xhs-0.1.0/MANIFEST.in
+-rw-rw-rw-   0        0        0     3014 2023-04-07 09:55:12.222416 xhs-0.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0     2083 2023-04-06 10:28:30.000000 xhs-0.1.0/README.md
+-rw-rw-rw-   0        0        0       62 2023-04-06 09:50:49.000000 xhs-0.1.0/requirements.txt
+-rw-rw-rw-   0        0        0      274 2023-04-07 09:55:12.223414 xhs-0.1.0/setup.cfg
+-rw-rw-rw-   0        0        0     1479 2023-04-05 13:04:46.000000 xhs-0.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:55:12.207497 xhs-0.1.0/tests/
+-rw-rw-rw-   0        0        0      244 2023-04-05 13:14:58.000000 xhs-0.1.0/tests/__init__.py
+-rw-rw-rw-   0        0        0     2578 2023-04-06 07:52:54.000000 xhs-0.1.0/tests/test_help.py
+-rw-rw-rw-   0        0        0     3108 2023-04-07 09:36:51.000000 xhs-0.1.0/tests/test_xhs.py
+-rw-rw-rw-   0        0        0      102 2023-04-07 06:13:42.000000 xhs-0.1.0/tests/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:55:12.213439 xhs-0.1.0/xhs/
+-rw-rw-rw-   0        0        0      331 2023-04-06 09:42:14.000000 xhs-0.1.0/xhs/__init__.py
+-rw-rw-rw-   0        0        0      465 2023-04-07 09:55:04.000000 xhs-0.1.0/xhs/__version__.py
+-rw-rw-rw-   0        0        0    12557 2023-04-07 09:30:09.000000 xhs-0.1.0/xhs/core.py
+-rw-rw-rw-   0        0        0       91 2023-04-06 08:24:03.000000 xhs-0.1.0/xhs/exception.py
+-rw-rw-rw-   0        0        0     2070 2023-04-07 02:28:25.000000 xhs-0.1.0/xhs/help.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:55:12.221452 xhs-0.1.0/xhs.egg-info/
+-rw-rw-rw-   0        0        0     3014 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      384 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0        9 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        4 2023-04-07 09:55:12.000000 xhs-0.1.0/xhs.egg-info/top_level.txt
```

### Comparing `xhs-0.0.4/LICENSE` & `xhs-0.1.0/LICENSE`

 * *Ordering differences only*

 * *Files 18% similar despite different names*

```diff
@@ -1,21 +1,21 @@
-MIT License
-
-Copyright (c) 2023 ReaJason
-
-Permission is hereby granted, free of charge, to any person obtaining a copy
-of this software and associated documentation files (the "Software"), to deal
-in the Software without restriction, including without limitation the rights
-to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-copies of the Software, and to permit persons to whom the Software is
-furnished to do so, subject to the following conditions:
-
-The above copyright notice and this permission notice shall be included in all
-copies or substantial portions of the Software.
-
-THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-SOFTWARE.
+MIT License
+
+Copyright (c) 2023 ReaJason
+
+Permission is hereby granted, free of charge, to any person obtaining a copy
+of this software and associated documentation files (the "Software"), to deal
+in the Software without restriction, including without limitation the rights
+to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
+copies of the Software, and to permit persons to whom the Software is
+furnished to do so, subject to the following conditions:
+
+The above copyright notice and this permission notice shall be included in all
+copies or substantial portions of the Software.
+
+THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
+IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
+FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
+AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
+LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
+OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
+SOFTWARE.
```

### Comparing `xhs-0.0.4/PKG-INFO` & `xhs-0.1.0/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,93 +1,93 @@
-Metadata-Version: 2.1
-Name: xhs
-Version: 0.0.4
-Summary: xiaohongshu crawl sdk.
-Home-page: https://github.com/ReaJason/xhs
-Author: ReaJason
-Author-email: reajason1225@gmail.com
-License: MIT
-Keywords: xhs crawl
-Classifier: Development Status :: 3 - Alpha
-Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: 3.11
-Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-<div align="center">
-
-<h1 align="center">
-🍰xhs
-</h1>
-
-[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
-[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
-[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
-[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
-
-</div>
-
-**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
-
-# Usage
-
-xhs is available on PyPI:
-
-```console
-$ python -m pip install xhs
-```
-
-basic usage:
-
-```python
-from xhs import FeedType, XhsClient
-
-cookie = "please get cookie in website"
-xhs_client = XhsClient(cookie)
-
-# get note info
-note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
-
-# get user info
-user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
-
-# get user notes
-user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
-
-# search note
-notes = xhs_client.get_note_by_keyword("小红书")
-
-# get home recommend feed
-recommend_type = FeedType.RECOMMEND
-recommend_notes = xhs_client.get_home_feed(recommend_type)
-
-# more functions in development
-```
-
-Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
-
-use signature function:
-
-```python
-# sign get request
->>> from xhs import help
->>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
-{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
-
-# sign post request
->>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
-{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
-
-# get search_id parameter
->>> help.get_search_id()
-'2BHU39J8HCTIW665YHFCW'
-```
+Metadata-Version: 2.1
+Name: xhs
+Version: 0.1.0
+Summary: xiaohongshu crawl sdk.
+Home-page: https://github.com/ReaJason/xhs
+Author: ReaJason
+Author-email: reajason1225@gmail.com
+License: MIT
+Keywords: xhs crawl
+Classifier: Development Status :: 3 - Alpha
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3 :: Only
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+<div align="center">
+
+<h1 align="center">
+🍰xhs
+</h1>
+
+[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
+[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
+[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
+[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
+
+</div>
+
+**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
+
+# Usage
+
+xhs is available on PyPI:
+
+```console
+$ python -m pip install xhs
+```
+
+basic usage:
+
+```python
+from xhs import FeedType, XhsClient
+
+cookie = "please get cookie in website"
+xhs_client = XhsClient(cookie)
+
+# get note info
+note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
+
+# get user info
+user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
+
+# get user notes
+user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
+
+# search note
+notes = xhs_client.get_note_by_keyword("小红书")
+
+# get home recommend feed
+recommend_type = FeedType.RECOMMEND
+recommend_notes = xhs_client.get_home_feed(recommend_type)
+
+# more functions in development
+```
+
+Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
+
+use signature function:
+
+```python
+# sign get request
+>>> from xhs import help
+>>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
+{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
+
+# sign post request
+>>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
+{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
+
+# get search_id parameter
+>>> help.get_search_id()
+'2BHU39J8HCTIW665YHFCW'
+```
```

### Comparing `xhs-0.0.4/README.md` & `xhs-0.1.0/README.md`

 * *Ordering differences only*

 * *Files 16% similar despite different names*

```diff
@@ -1,68 +1,68 @@
-<div align="center">
-
-<h1 align="center">
-🍰xhs
-</h1>
-
-[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
-[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
-[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
-[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
-
-</div>
-
-**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
-
-# Usage
-
-xhs is available on PyPI:
-
-```console
-$ python -m pip install xhs
-```
-
-basic usage:
-
-```python
-from xhs import FeedType, XhsClient
-
-cookie = "please get cookie in website"
-xhs_client = XhsClient(cookie)
-
-# get note info
-note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
-
-# get user info
-user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
-
-# get user notes
-user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
-
-# search note
-notes = xhs_client.get_note_by_keyword("小红书")
-
-# get home recommend feed
-recommend_type = FeedType.RECOMMEND
-recommend_notes = xhs_client.get_home_feed(recommend_type)
-
-# more functions in development
-```
-
-Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
-
-use signature function:
-
-```python
-# sign get request
->>> from xhs import help
->>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
-{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
-
-# sign post request
->>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
-{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
-
-# get search_id parameter
->>> help.get_search_id()
-'2BHU39J8HCTIW665YHFCW'
-```
+<div align="center">
+
+<h1 align="center">
+🍰xhs
+</h1>
+
+[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
+[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
+[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
+[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
+
+</div>
+
+**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
+
+# Usage
+
+xhs is available on PyPI:
+
+```console
+$ python -m pip install xhs
+```
+
+basic usage:
+
+```python
+from xhs import FeedType, XhsClient
+
+cookie = "please get cookie in website"
+xhs_client = XhsClient(cookie)
+
+# get note info
+note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
+
+# get user info
+user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
+
+# get user notes
+user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
+
+# search note
+notes = xhs_client.get_note_by_keyword("小红书")
+
+# get home recommend feed
+recommend_type = FeedType.RECOMMEND
+recommend_notes = xhs_client.get_home_feed(recommend_type)
+
+# more functions in development
+```
+
+Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
+
+use signature function:
+
+```python
+# sign get request
+>>> from xhs import help
+>>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
+{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
+
+# sign post request
+>>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
+{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
+
+# get search_id parameter
+>>> help.get_search_id()
+'2BHU39J8HCTIW665YHFCW'
+```
```

### Comparing `xhs-0.0.4/tests/test_help.py` & `xhs-0.1.0/tests/test_help.py`

 * *Files identical despite different names*

### Comparing `xhs-0.0.4/xhs/help.py` & `xhs-0.1.0/xhs/help.py`

 * *Ordering differences only*

 * *Files 19% similar despite different names*

```diff
@@ -1,76 +1,76 @@
-import hashlib
-import json
-import random
-import time
-
-
-def sign(uri, data=None, ctime=None):
-    """
-    takes in a URI (uniform resource identifier), an optional data dictionary, and an optional ctime parameter. It returns a dictionary containing two keys: "x-s" and "x-t".
-    """
-    def h(n):
-        m = ""
-        a = 0
-        d = "A4NjFqYu5wPHsO0XTdDgMa2r1ZQocVte9UJBvk6/7=yRnhISGKblCWi+LpfE8xzm3"
-        while a < 32:
-            o = ord(n[a])
-            a += 1
-            g = 0
-            if a < 32:
-                g = ord(n[a])
-            a += 1
-            h = 0
-            if a < 32:
-                h = ord(n[a])
-            a += 1
-            x = ((o & 3) << 4) | (g >> 4)
-            p = ((15 & g) << 2) | (h >> 6)
-            v = o >> 2
-            if h:
-                b = h & 63
-            else:
-                b = 64
-            if not g:
-                p = b = 64
-            m += d[v] + d[x] + d[p] + d[b]
-        return m
-
-    v = int(round(time.time() * 1000) if not ctime else ctime)
-    raw_str = f"{v}test{uri}{json.dumps(data, separators=(',', ':'), ensure_ascii=False) if isinstance(data, dict) else ''}"
-    md5_str = hashlib.md5(raw_str.encode('utf-8')).hexdigest()
-    return {
-        "x-s": h(md5_str),
-        "x-t": str(v),
-    }
-
-
-def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
-    """Converts an integer to a base36 string."""
-    if not isinstance(number, int):
-        raise TypeError('number must be an integer')
-
-    base36 = ''
-    sign = ''
-
-    if number < 0:
-        sign = '-'
-        number = -number
-
-    if 0 <= number < len(alphabet):
-        return sign + alphabet[number]
-
-    while number != 0:
-        number, i = divmod(number, len(alphabet))
-        base36 = alphabet[i] + base36
-
-    return sign + base36
-
-
-def base36decode(number):
-    return int(number, 36)
-
-
-def get_search_id():
-    e = int(time.time() * 1000) << 64
-    t = int(random.uniform(0, 2147483646))
-    return base36encode((e + t))
+import hashlib
+import json
+import random
+import time
+
+
+def sign(uri, data=None, ctime=None):
+    """
+    takes in a URI (uniform resource identifier), an optional data dictionary, and an optional ctime parameter. It returns a dictionary containing two keys: "x-s" and "x-t".
+    """
+    def h(n):
+        m = ""
+        a = 0
+        d = "A4NjFqYu5wPHsO0XTdDgMa2r1ZQocVte9UJBvk6/7=yRnhISGKblCWi+LpfE8xzm3"
+        while a < 32:
+            o = ord(n[a])
+            a += 1
+            g = 0
+            if a < 32:
+                g = ord(n[a])
+            a += 1
+            h = 0
+            if a < 32:
+                h = ord(n[a])
+            a += 1
+            x = ((o & 3) << 4) | (g >> 4)
+            p = ((15 & g) << 2) | (h >> 6)
+            v = o >> 2
+            if h:
+                b = h & 63
+            else:
+                b = 64
+            if not g:
+                p = b = 64
+            m += d[v] + d[x] + d[p] + d[b]
+        return m
+
+    v = int(round(time.time() * 1000) if not ctime else ctime)
+    raw_str = f"{v}test{uri}{json.dumps(data, separators=(',', ':'), ensure_ascii=False) if isinstance(data, dict) else ''}"
+    md5_str = hashlib.md5(raw_str.encode('utf-8')).hexdigest()
+    return {
+        "x-s": h(md5_str),
+        "x-t": str(v),
+    }
+
+
+def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
+    """Converts an integer to a base36 string."""
+    if not isinstance(number, int):
+        raise TypeError('number must be an integer')
+
+    base36 = ''
+    sign = ''
+
+    if number < 0:
+        sign = '-'
+        number = -number
+
+    if 0 <= number < len(alphabet):
+        return sign + alphabet[number]
+
+    while number != 0:
+        number, i = divmod(number, len(alphabet))
+        base36 = alphabet[i] + base36
+
+    return sign + base36
+
+
+def base36decode(number):
+    return int(number, 36)
+
+
+def get_search_id():
+    e = int(time.time() * 1000) << 64
+    t = int(random.uniform(0, 2147483646))
+    return base36encode((e + t))
```

### Comparing `xhs-0.0.4/xhs.egg-info/PKG-INFO` & `xhs-0.1.0/xhs.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,93 +1,93 @@
-Metadata-Version: 2.1
-Name: xhs
-Version: 0.0.4
-Summary: xiaohongshu crawl sdk.
-Home-page: https://github.com/ReaJason/xhs
-Author: ReaJason
-Author-email: reajason1225@gmail.com
-License: MIT
-Keywords: xhs crawl
-Classifier: Development Status :: 3 - Alpha
-Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: 3.11
-Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-<div align="center">
-
-<h1 align="center">
-🍰xhs
-</h1>
-
-[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
-[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
-[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
-[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
-
-</div>
-
-**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
-
-# Usage
-
-xhs is available on PyPI:
-
-```console
-$ python -m pip install xhs
-```
-
-basic usage:
-
-```python
-from xhs import FeedType, XhsClient
-
-cookie = "please get cookie in website"
-xhs_client = XhsClient(cookie)
-
-# get note info
-note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
-
-# get user info
-user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
-
-# get user notes
-user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
-
-# search note
-notes = xhs_client.get_note_by_keyword("小红书")
-
-# get home recommend feed
-recommend_type = FeedType.RECOMMEND
-recommend_notes = xhs_client.get_home_feed(recommend_type)
-
-# more functions in development
-```
-
-Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
-
-use signature function:
-
-```python
-# sign get request
->>> from xhs import help
->>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
-{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
-
-# sign post request
->>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
-{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
-
-# get search_id parameter
->>> help.get_search_id()
-'2BHU39J8HCTIW665YHFCW'
-```
+Metadata-Version: 2.1
+Name: xhs
+Version: 0.1.0
+Summary: xiaohongshu crawl sdk.
+Home-page: https://github.com/ReaJason/xhs
+Author: ReaJason
+Author-email: reajason1225@gmail.com
+License: MIT
+Keywords: xhs crawl
+Classifier: Development Status :: 3 - Alpha
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3 :: Only
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+<div align="center">
+
+<h1 align="center">
+🍰xhs
+</h1>
+
+[![](https://img.shields.io/github/license/ReaJason/17wanxiaoCheckin-Actions "协议")](https://github.com/ReaJason/17wanxiaoCheckin/blob/master/LICENSE)
+[![](https://github.com/ReaJason/xhs/actions/workflows/doc.yml/badge.svg)](https://reajason.github.io/xhs/)
+[![](https://github.com/ReaJason/xhs/actions/workflows/test.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/test.yml)
+[![](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml/badge.svg)](https://github.com/ReaJason/xhs/actions/workflows/pypi.yml)
+
+</div>
+
+**xhs** is a crawling tool designed to extract data from [xiaohongshu website](https://www.xiaohongshu.com/explore)
+
+# Usage
+
+xhs is available on PyPI:
+
+```console
+$ python -m pip install xhs
+```
+
+basic usage:
+
+```python
+from xhs import FeedType, XhsClient
+
+cookie = "please get cookie in website"
+xhs_client = XhsClient(cookie)
+
+# get note info
+note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")
+
+# get user info
+user_info = xhs_client.get_user_info("5ff0e6410000000001008400")
+
+# get user notes
+user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")
+
+# search note
+notes = xhs_client.get_note_by_keyword("小红书")
+
+# get home recommend feed
+recommend_type = FeedType.RECOMMEND
+recommend_notes = xhs_client.get_home_feed(recommend_type)
+
+# more functions in development
+```
+
+Please refer to the [document(WIP)](https://reajason.github.io/xhs/) for more API references.
+
+use signature function:
+
+```python
+# sign get request
+>>> from xhs import help
+>>> help.sign("/api/sns/web/v1/user/otherinfo?target_user_id=5ff0e6410000000001008400")
+{'x-s': '1l5LsiTlZYavOYwvOid6OlU6OisCZ6dBZjvL1gsCOg13', 'x-t': '1680701208022'}
+
+# sign post request
+>>> help.sign("/api/sns/web/v1/feed", {"source_note_id": "63db8819000000001a01ead1"})
+{'x-s': 'sY5LOg9WOYFKsYFWOBcis2MlsiFCsjMb0jTKZja6OjA3', 'x-t': '1680701310666'}
+
+# get search_id parameter
+>>> help.get_search_id()
+'2BHU39J8HCTIW665YHFCW'
+```
```

