# Comparing `tmp/quorum_data_py-1.1.3.tar.gz` & `tmp/quorum_data_py-1.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quorum_data_py-1.1.3.tar", last modified: Thu Apr  6 12:22:13 2023, max compression
+gzip compressed data, was "quorum_data_py-1.1.4.tar", last modified: Thu Apr  6 12:31:54 2023, max compression
```

## Comparing `quorum_data_py-1.1.3.tar` & `quorum_data_py-1.1.4.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.472657 quorum_data_py-1.1.3/
--rw-rw-rw-   0        0        0     1087 2023-04-03 04:08:10.000000 quorum_data_py-1.1.3/LICENSE
--rw-rw-rw-   0        0        0     2977 2023-04-06 12:22:13.471658 quorum_data_py-1.1.3/PKG-INFO
--rw-rw-rw-   0        0        0     2018 2023-04-03 04:16:39.000000 quorum_data_py-1.1.3/README.md
--rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.3/pyproject.toml
-drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.456701 quorum_data_py-1.1.3/quorum_data_py/
--rw-rw-rw-   0        0        0      349 2023-04-06 12:09:56.000000 quorum_data_py-1.1.3/quorum_data_py/__init__.py
--rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.3/quorum_data_py/_utils.py
--rw-rw-rw-   0        0        0     2904 2023-03-29 07:46:37.000000 quorum_data_py-1.1.3/quorum_data_py/converter.py
--rw-rw-rw-   0        0        0     5794 2023-04-06 12:19:32.000000 quorum_data_py-1.1.3/quorum_data_py/feed.py
--rw-rw-rw-   0        0        0     1434 2023-03-30 06:02:52.000000 quorum_data_py-1.1.3/quorum_data_py/trx_type.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.468667 quorum_data_py-1.1.3/quorum_data_py.egg-info/
--rw-rw-rw-   0        0        0     2977 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      360 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       27 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 12:22:13.473654 quorum_data_py-1.1.3/setup.cfg
--rw-rw-rw-   0        0        0     1314 2023-04-06 12:09:56.000000 quorum_data_py-1.1.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.799842 quorum_data_py-1.1.4/
+-rw-rw-rw-   0        0        0     1087 2023-04-03 04:08:10.000000 quorum_data_py-1.1.4/LICENSE
+-rw-rw-rw-   0        0        0     2977 2023-04-06 12:31:54.798846 quorum_data_py-1.1.4/PKG-INFO
+-rw-rw-rw-   0        0        0     2018 2023-04-03 04:16:39.000000 quorum_data_py-1.1.4/README.md
+-rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.4/pyproject.toml
+drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.784883 quorum_data_py-1.1.4/quorum_data_py/
+-rw-rw-rw-   0        0        0      349 2023-04-06 12:28:15.000000 quorum_data_py-1.1.4/quorum_data_py/__init__.py
+-rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.4/quorum_data_py/_utils.py
+-rw-rw-rw-   0        0        0     2904 2023-03-29 07:46:37.000000 quorum_data_py-1.1.4/quorum_data_py/converter.py
+-rw-rw-rw-   0        0        0     5778 2023-04-06 12:27:52.000000 quorum_data_py-1.1.4/quorum_data_py/feed.py
+-rw-rw-rw-   0        0        0     1357 2023-04-06 12:24:56.000000 quorum_data_py-1.1.4/quorum_data_py/trx_type.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.796851 quorum_data_py-1.1.4/quorum_data_py.egg-info/
+-rw-rw-rw-   0        0        0     2977 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      360 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       27 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 12:31:54.800841 quorum_data_py-1.1.4/setup.cfg
+-rw-rw-rw-   0        0        0     1314 2023-04-06 12:28:15.000000 quorum_data_py-1.1.4/setup.py
```

### Comparing `quorum_data_py-1.1.3/LICENSE` & `quorum_data_py-1.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.3/PKG-INFO` & `quorum_data_py-1.1.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum_data_py
-Version: 1.1.3
+Version: 1.1.4
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
```

### Comparing `quorum_data_py-1.1.3/README.md` & `quorum_data_py-1.1.4/README.md`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.3/quorum_data_py/_utils.py` & `quorum_data_py-1.1.4/quorum_data_py/_utils.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.3/quorum_data_py/converter.py` & `quorum_data_py-1.1.4/quorum_data_py/converter.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.3/quorum_data_py/feed.py` & `quorum_data_py-1.1.4/quorum_data_py/feed.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,24 +11,24 @@
 
 
 def add_published(data: dict, published):
     """
     published: timestamp int or ISO format string
     e.g. 2020-01-01T00:00:00Z, 2023-04-04T10:31:45+08:00
     """
-    if isinstance(published, int) or isinstance(published, float):
+    if isinstance(published, (float, int)):
         published = int(str(published)[:10])
         dt = datetime.datetime.fromtimestamp(published, datetime.timezone.utc)
         published = dt.isoformat(timespec="seconds")
     else:
         try:
             dt = parser.parse(published)
             published = dt.isoformat(timespec="seconds")
         except Exception as e:
-            raise ValueError(f"published format error: {published}")
+            raise ValueError(f"published format error: {published}") from e
     data["published"] = published
     return data
 
 
 def add_origin(data: dict, origin_name, origin_type=None):
     origin_type = origin_type or "Application"
     if origin_type not in ["Application", "Service"]:
```

### Comparing `quorum_data_py-1.1.3/quorum_data_py/trx_type.py` & `quorum_data_py-1.1.4/quorum_data_py/trx_type.py`

 * *Files 15% similar despite different names*

```diff
@@ -21,17 +21,14 @@
                 trx_type = "comment"
         elif inner_type == "Profile":
             trx_type = "profile"
     elif out_type == "Like" or (out_type == "Undo" and inner_type == "Like"):
         trx_type = "counter"
     elif out_type == "Delete" and inner_type == "Note":
         trx_type = "delete"
-    elif (
-        out_type == "Follow"
-        or (out_type == "Undo" and inner_type == "Follow")
-        or out_type == "Block"
-        or (out_type == "Undo" and inner_type == "Block")
+    elif out_type in ["Follow", "Block"] or (
+        out_type == "Undo" and inner_type in ["Follow", "Block"]
     ):
         trx_type = "relation"
     elif out_type == "Announce" and data.get("name").find("private key") != -1:
         trx_type = "wallet"
     return trx_type
```

### Comparing `quorum_data_py-1.1.3/quorum_data_py.egg-info/PKG-INFO` & `quorum_data_py-1.1.4/quorum_data_py.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum-data-py
-Version: 1.1.3
+Version: 1.1.4
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
```

### Comparing `quorum_data_py-1.1.3/setup.py` & `quorum_data_py-1.1.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="quorum_data_py",
-    version="1.1.3",
+    version="1.1.4",
     author="liujuanjuan1984",
     author_email="qiaoanlu@163.com",
     description="Python Data for Apps of QuoRum",
     keywords=["quorum_data_py", "rumsystem", "quorum"],
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/liujuanjuan1984/quorum_data_py",
```

