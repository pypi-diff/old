# Comparing `tmp/quorum_data_py-1.1.4.tar.gz` & `tmp/quorum_data_py-1.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quorum_data_py-1.1.4.tar", last modified: Thu Apr  6 12:31:54 2023, max compression
+gzip compressed data, was "quorum_data_py-1.1.5.tar", last modified: Thu Apr  6 13:07:05 2023, max compression
```

## Comparing `quorum_data_py-1.1.4.tar` & `quorum_data_py-1.1.5.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.799842 quorum_data_py-1.1.4/
--rw-rw-rw-   0        0        0     1087 2023-04-03 04:08:10.000000 quorum_data_py-1.1.4/LICENSE
--rw-rw-rw-   0        0        0     2977 2023-04-06 12:31:54.798846 quorum_data_py-1.1.4/PKG-INFO
--rw-rw-rw-   0        0        0     2018 2023-04-03 04:16:39.000000 quorum_data_py-1.1.4/README.md
--rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.4/pyproject.toml
-drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.784883 quorum_data_py-1.1.4/quorum_data_py/
--rw-rw-rw-   0        0        0      349 2023-04-06 12:28:15.000000 quorum_data_py-1.1.4/quorum_data_py/__init__.py
--rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.4/quorum_data_py/_utils.py
--rw-rw-rw-   0        0        0     2904 2023-03-29 07:46:37.000000 quorum_data_py-1.1.4/quorum_data_py/converter.py
--rw-rw-rw-   0        0        0     5778 2023-04-06 12:27:52.000000 quorum_data_py-1.1.4/quorum_data_py/feed.py
--rw-rw-rw-   0        0        0     1357 2023-04-06 12:24:56.000000 quorum_data_py-1.1.4/quorum_data_py/trx_type.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:31:54.796851 quorum_data_py-1.1.4/quorum_data_py.egg-info/
--rw-rw-rw-   0        0        0     2977 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      360 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       27 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-06 12:31:54.000000 quorum_data_py-1.1.4/quorum_data_py.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 12:31:54.800841 quorum_data_py-1.1.4/setup.cfg
--rw-rw-rw-   0        0        0     1314 2023-04-06 12:28:15.000000 quorum_data_py-1.1.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:07:05.858582 quorum_data_py-1.1.5/
+-rw-rw-rw-   0        0        0     1087 2023-04-03 04:08:10.000000 quorum_data_py-1.1.5/LICENSE
+-rw-rw-rw-   0        0        0     2977 2023-04-06 13:07:05.857630 quorum_data_py-1.1.5/PKG-INFO
+-rw-rw-rw-   0        0        0     2018 2023-04-03 04:16:39.000000 quorum_data_py-1.1.5/README.md
+-rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.5/pyproject.toml
+drwxrwxrwx   0        0        0        0 2023-04-06 13:07:05.842979 quorum_data_py-1.1.5/quorum_data_py/
+-rw-rw-rw-   0        0        0      349 2023-04-06 13:04:34.000000 quorum_data_py-1.1.5/quorum_data_py/__init__.py
+-rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.5/quorum_data_py/_utils.py
+-rw-rw-rw-   0        0        0     2980 2023-04-06 13:03:34.000000 quorum_data_py-1.1.5/quorum_data_py/converter.py
+-rw-rw-rw-   0        0        0     5778 2023-04-06 12:27:52.000000 quorum_data_py-1.1.5/quorum_data_py/feed.py
+-rw-rw-rw-   0        0        0     1357 2023-04-06 12:24:56.000000 quorum_data_py-1.1.5/quorum_data_py/trx_type.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:07:05.855592 quorum_data_py-1.1.5/quorum_data_py.egg-info/
+-rw-rw-rw-   0        0        0     2977 2023-04-06 13:07:05.000000 quorum_data_py-1.1.5/quorum_data_py.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      360 2023-04-06 13:07:05.000000 quorum_data_py-1.1.5/quorum_data_py.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 13:07:05.000000 quorum_data_py-1.1.5/quorum_data_py.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       27 2023-04-06 13:07:05.000000 quorum_data_py-1.1.5/quorum_data_py.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 13:07:05.000000 quorum_data_py-1.1.5/quorum_data_py.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 13:07:05.858582 quorum_data_py-1.1.5/setup.cfg
+-rw-rw-rw-   0        0        0     1314 2023-04-06 13:04:34.000000 quorum_data_py-1.1.5/setup.py
```

### Comparing `quorum_data_py-1.1.4/LICENSE` & `quorum_data_py-1.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.4/PKG-INFO` & `quorum_data_py-1.1.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum_data_py
-Version: 1.1.4
+Version: 1.1.5
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
```

### Comparing `quorum_data_py-1.1.4/README.md` & `quorum_data_py-1.1.5/README.md`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.4/quorum_data_py/_utils.py` & `quorum_data_py-1.1.5/quorum_data_py/_utils.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.4/quorum_data_py/converter.py` & `quorum_data_py-1.1.5/quorum_data_py/converter.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,27 +1,29 @@
 """
 数据结构转换
 
 把 解密后的 trx （通过 get content api 所获得的 trx）转换成新版的 trx data 和 timestamp 等，用来重新发布上链
 """
 from quorum_mininode_py.crypto.account import public_key_to_address
 
+from quorum_data_py import feed
+
 
 def from_new_chain(trx: dict):
     """
     把新共识版本的 trx 还原为 trx data 和 timestamp，
     然后通过轻节点的 post to group api 发送上链
     适用场景：把链 a 的 trx 发送到 链 b
     保留原有 trx_id 是为了继承此前所产生的交互数据
     """
     if isinstance(trx.get("Data"), str):
         raise ValueError("trx is encrypted.")
+    data = trx.get("Content") or trx.get("Data")
     new = {
-        "data": trx.get("Content") or trx.get("Data"),
-        "timestamp": trx["TimeStamp"],
+        "data": feed.add_published(data, int(trx["TimeStamp"])),
         "trx_id": trx["TrxId"],
     }
     return new
 
 
 def from_old_chain(trx: dict):
     """
@@ -82,9 +84,11 @@
             if "inreplyto" in contentobj:
                 contentobj["inreplyto"] = {
                     "type": "Note",
                     "id": contentobj["inreplyto"]["trxid"],
                 }
             obj = {"type": "Create", "object": contentobj}
 
-    new = {"data": obj, "timestamp": trx.get("TimeStamp")}
+    new = {
+        "data": feed.add_published(obj, int(trx["TimeStamp"])),
+    }
     return new
```

### Comparing `quorum_data_py-1.1.4/quorum_data_py/feed.py` & `quorum_data_py-1.1.5/quorum_data_py/feed.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.4/quorum_data_py/trx_type.py` & `quorum_data_py-1.1.5/quorum_data_py/trx_type.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.4/quorum_data_py.egg-info/PKG-INFO` & `quorum_data_py-1.1.5/quorum_data_py.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum-data-py
-Version: 1.1.4
+Version: 1.1.5
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
```

### Comparing `quorum_data_py-1.1.4/setup.py` & `quorum_data_py-1.1.5/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="quorum_data_py",
-    version="1.1.4",
+    version="1.1.5",
     author="liujuanjuan1984",
     author_email="qiaoanlu@163.com",
     description="Python Data for Apps of QuoRum",
     keywords=["quorum_data_py", "rumsystem", "quorum"],
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/liujuanjuan1984/quorum_data_py",
```

