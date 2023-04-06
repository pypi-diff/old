# Comparing `tmp/xhs-0.0.3.tar.gz` & `tmp/xhs-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xhs-0.0.3.tar", last modified: Wed Apr  5 13:23:41 2023, max compression
+gzip compressed data, was "xhs-0.0.4.tar", last modified: Thu Apr  6 10:35:09 2023, max compression
```

## Comparing `xhs-0.0.3.tar` & `xhs-0.0.4.tar`

### file list

```diff
@@ -1,25 +1,26 @@
-drwxrwxrwx   0        0        0        0 2023-04-05 13:23:41.137981 xhs-0.0.3/
--rw-rw-rw-   0        0        0      350 2023-04-05 13:19:31.000000 xhs-0.0.3/CHANGELOG.md
--rw-rw-rw-   0        0        0     1086 2023-04-03 04:48:59.000000 xhs-0.0.3/LICENSE
--rw-rw-rw-   0        0        0       85 2023-04-03 14:57:56.000000 xhs-0.0.3/MANIFEST.in
--rw-rw-rw-   0        0        0     1872 2023-04-05 13:23:41.137981 xhs-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0      941 2023-04-05 13:21:46.000000 xhs-0.0.3/README.md
--rw-rw-rw-   0        0        0       50 2023-04-05 13:04:46.000000 xhs-0.0.3/requirements.txt
--rw-rw-rw-   0        0        0      178 2023-04-05 13:23:41.138951 xhs-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0     1479 2023-04-05 13:04:46.000000 xhs-0.0.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-05 13:23:41.123017 xhs-0.0.3/tests/
--rw-rw-rw-   0        0        0      244 2023-04-05 13:14:58.000000 xhs-0.0.3/tests/__init__.py
--rw-rw-rw-   0        0        0     2517 2023-04-05 13:12:51.000000 xhs-0.0.3/tests/test_help.py
--rw-rw-rw-   0        0        0      229 2023-04-05 13:14:58.000000 xhs-0.0.3/tests/test_xhs.py
-drwxrwxrwx   0        0        0        0 2023-04-05 13:23:41.128976 xhs-0.0.3/xhs/
--rw-rw-rw-   0        0        0      282 2023-04-05 13:12:56.000000 xhs-0.0.3/xhs/__init__.py
--rw-rw-rw-   0        0        0      448 2023-04-05 13:23:26.000000 xhs-0.0.3/xhs/__version__.py
--rw-rw-rw-   0        0        0      246 2023-04-05 13:12:56.000000 xhs-0.0.3/xhs/core.py
--rw-rw-rw-   0        0        0     1877 2023-04-05 13:10:32.000000 xhs-0.0.3/xhs/help.py
-drwxrwxrwx   0        0        0        0 2023-04-05 13:23:41.136956 xhs-0.0.3/xhs.egg-info/
--rw-rw-rw-   0        0        0     1872 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      352 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0        9 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-04-05 13:23:41.000000 xhs-0.0.3/xhs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/
+-rw-r--r--   0 runner    (1001) docker     (123)      473 2023-04-06 10:34:52.000000 xhs-0.0.4/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-04-06 10:34:52.000000 xhs-0.0.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-06 10:34:52.000000 xhs-0.0.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2921 2023-04-06 10:35:09.091733 xhs-0.0.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-04-06 10:34:52.000000 xhs-0.0.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 10:34:52.000000 xhs-0.0.4/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-04-06 10:35:09.091733 xhs-0.0.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-04-06 10:34:52.000000 xhs-0.0.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2578 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/test_help.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1473 2023-04-06 10:34:52.000000 xhs-0.0.4/tests/test_xhs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/xhs/
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4965 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/exception.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1994 2023-04-06 10:34:52.000000 xhs-0.0.4/xhs/help.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:35:09.091733 xhs-0.0.4/xhs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2921 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      369 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:35:08.000000 xhs-0.0.4/xhs.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 10:35:09.000000 xhs-0.0.4/xhs.egg-info/top_level.txt
```

### Comparing `xhs-0.0.3/LICENSE` & `xhs-0.0.4/LICENSE`

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

### Comparing `xhs-0.0.3/tests/test_help.py` & `xhs-0.0.4/tests/test_help.py`

 * *Files 5% similar despite different names*

```diff
@@ -57,14 +57,15 @@
     print(payload)
     response = requests.post(url, headers=headers, data=payload)
     json_data = response.json()
     print(json_data)
     assert json_data["code"] == 0
 
 
+@pytest.mark.skip(reason="xhs website limit search numbers")
 def test_search_id(header):
     search_id = help.get_search_id()
     uri = "/api/sns/web/v1/search/notes"
     data = {
       "keyword": "小红书",
       "page": 1,
       "page_size": 20,
```

### Comparing `xhs-0.0.3/xhs/help.py` & `xhs-0.0.4/xhs/help.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,73 +1,76 @@
-import hashlib
-import json
-import random
-import time
-
-
-def sign(uri, data=None, ctime=None):
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

