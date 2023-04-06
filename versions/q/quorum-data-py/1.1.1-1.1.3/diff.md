# Comparing `tmp/quorum_data_py-1.1.1.tar.gz` & `tmp/quorum_data_py-1.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quorum_data_py-1.1.1.tar", last modified: Thu Mar 30 06:05:27 2023, max compression
+gzip compressed data, was "quorum_data_py-1.1.3.tar", last modified: Thu Apr  6 12:22:13 2023, max compression
```

## Comparing `quorum_data_py-1.1.1.tar` & `quorum_data_py-1.1.3.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-03-30 06:05:27.593238 quorum_data_py-1.1.1/
--rw-rw-rw-   0        0        0     1087 2023-02-24 07:10:48.000000 quorum_data_py-1.1.1/LICENSE
--rw-rw-rw-   0        0        0     2151 2023-03-30 06:05:27.592241 quorum_data_py-1.1.1/PKG-INFO
--rw-rw-rw-   0        0        0     1192 2023-03-27 05:51:36.000000 quorum_data_py-1.1.1/README.md
--rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.1/pyproject.toml
-drwxrwxrwx   0        0        0        0 2023-03-30 06:05:27.576284 quorum_data_py-1.1.1/quorum_data_py/
--rw-rw-rw-   0        0        0      365 2023-03-30 06:05:07.000000 quorum_data_py-1.1.1/quorum_data_py/__init__.py
--rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.1/quorum_data_py/_utils.py
--rw-rw-rw-   0        0        0     2904 2023-03-29 07:46:37.000000 quorum_data_py-1.1.1/quorum_data_py/converter.py
--rw-rw-rw-   0        0        0     4720 2023-03-17 16:31:28.000000 quorum_data_py-1.1.1/quorum_data_py/feed.py
--rw-rw-rw-   0        0        0     1434 2023-03-30 06:02:52.000000 quorum_data_py-1.1.1/quorum_data_py/trx_type.py
-drwxrwxrwx   0        0        0        0 2023-03-30 06:05:27.589250 quorum_data_py-1.1.1/quorum_data_py.egg-info/
--rw-rw-rw-   0        0        0     2151 2023-03-30 06:05:27.000000 quorum_data_py-1.1.1/quorum_data_py.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      360 2023-03-30 06:05:27.000000 quorum_data_py-1.1.1/quorum_data_py.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-30 06:05:27.000000 quorum_data_py-1.1.1/quorum_data_py.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       27 2023-03-30 06:05:27.000000 quorum_data_py-1.1.1/quorum_data_py.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-03-30 06:05:27.000000 quorum_data_py-1.1.1/quorum_data_py.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-30 06:05:27.593238 quorum_data_py-1.1.1/setup.cfg
--rw-rw-rw-   0        0        0     1314 2023-03-30 06:05:02.000000 quorum_data_py-1.1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.472657 quorum_data_py-1.1.3/
+-rw-rw-rw-   0        0        0     1087 2023-04-03 04:08:10.000000 quorum_data_py-1.1.3/LICENSE
+-rw-rw-rw-   0        0        0     2977 2023-04-06 12:22:13.471658 quorum_data_py-1.1.3/PKG-INFO
+-rw-rw-rw-   0        0        0     2018 2023-04-03 04:16:39.000000 quorum_data_py-1.1.3/README.md
+-rw-rw-rw-   0        0        0      162 2023-02-24 07:11:51.000000 quorum_data_py-1.1.3/pyproject.toml
+drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.456701 quorum_data_py-1.1.3/quorum_data_py/
+-rw-rw-rw-   0        0        0      349 2023-04-06 12:09:56.000000 quorum_data_py-1.1.3/quorum_data_py/__init__.py
+-rw-rw-rw-   0        0        0     5500 2023-03-28 06:45:29.000000 quorum_data_py-1.1.3/quorum_data_py/_utils.py
+-rw-rw-rw-   0        0        0     2904 2023-03-29 07:46:37.000000 quorum_data_py-1.1.3/quorum_data_py/converter.py
+-rw-rw-rw-   0        0        0     5794 2023-04-06 12:19:32.000000 quorum_data_py-1.1.3/quorum_data_py/feed.py
+-rw-rw-rw-   0        0        0     1434 2023-03-30 06:02:52.000000 quorum_data_py-1.1.3/quorum_data_py/trx_type.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:22:13.468667 quorum_data_py-1.1.3/quorum_data_py.egg-info/
+-rw-rw-rw-   0        0        0     2977 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      360 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       27 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 12:22:13.000000 quorum_data_py-1.1.3/quorum_data_py.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 12:22:13.473654 quorum_data_py-1.1.3/setup.cfg
+-rw-rw-rw-   0        0        0     1314 2023-04-06 12:09:56.000000 quorum_data_py-1.1.3/setup.py
```

### Comparing `quorum_data_py-1.1.1/LICENSE` & `quorum_data_py-1.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.1/PKG-INFO` & `quorum_data_py-1.1.3/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum_data_py
-Version: 1.1.1
+Version: 1.1.3
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
@@ -34,38 +34,70 @@
 
 请留意，这只是推荐结构，并不是唯一标准。quorum chain 是非常开放的，客户端完全可以按照自己的需求来构造上链数据的结构。
 
 2、converter：
 
 基于 quorum 新共识，从旧链 trx 或从 新链 trx 转换为待发布的数据。目前主要用作数据迁移：从旧共识链迁移到新共识链；在新共识链之间迁移。
 
+3、trx_type：
+
+判断 trx 的类型。该方法所返回的结果，与 rum-app，feed 等产品的处理保持一致。
+
 ### Install
 
 
 ```sh
 pip install quorum_data_py
 ```
 
 ### Examples
 
 ```python
 
 from quorum_data_py import feed
 
+# create a new post data 
 data = feed.new_post(content='hello guys')
+
+# create a like post data
 data = feed.like('a-post-id')
 
 ```
 
-### pylint
+适用于 fullnode 也适用于 lightnode，比如：
 
-```sh
-isort ./quorum_data_py
-black ./quorum_data_py
-pylint ./quorum_data_py --output=pylint.log
+```python
+
+from quorum_data_py import feed
+from quorum_fullnode_py import FullNode 
+
+jwt = "xxx"
+url = "xxx"
+
+fullnode = FullNode(url,jwt)
+data = feed.new_post(content='hello guys')
+fullnode.api.post_content(data)
 
 ```
 
+```python
+
+from quorum_data_py import feed
+from quorum_mininode_py import MiniNode 
+
+seed = "xxx"
+
+mininode = MiniNode(seed)
+data = feed.new_post(content='hello guys')
+mininode.api.post_content(data)
+
+```
+
+### Source
+
+- quorum fullnode sdk for python: https://github.com/liujuanjuan1984/quorum-fullnode-py 
+- quorum mininode sdk for python: https://github.com/liujuanjuan1984/quorum-mininode-py 
+- and more ...  https://github.com/okdaodine/awesome-quorum
 
 ### License
 
 This work is released under the `MIT` license. A copy of the license is provided in the [LICENSE](https://github.com/liujuanjuan1984/quorum_data_py/blob/master/LICENSE) file.
```

### Comparing `quorum_data_py-1.1.1/quorum_data_py/_utils.py` & `quorum_data_py-1.1.3/quorum_data_py/_utils.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.1/quorum_data_py/converter.py` & `quorum_data_py-1.1.3/quorum_data_py/converter.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.1/quorum_data_py/trx_type.py` & `quorum_data_py-1.1.3/quorum_data_py/trx_type.py`

 * *Files identical despite different names*

### Comparing `quorum_data_py-1.1.1/quorum_data_py.egg-info/PKG-INFO` & `quorum_data_py-1.1.3/quorum_data_py.egg-info/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quorum-data-py
-Version: 1.1.1
+Version: 1.1.3
 Summary: Python Data for Apps of QuoRum
 Home-page: https://github.com/liujuanjuan1984/quorum_data_py
 Author: liujuanjuan1984
 Author-email: qiaoanlu@163.com
 Project-URL: Github Repo, https://github.com/liujuanjuan1984/quorum_data_py
 Project-URL: Bug Tracker, https://github.com/liujuanjuan1984/quorum_data_py/issues
 Project-URL: About Quorum, https://github.com/rumsystem/quorum
@@ -34,38 +34,70 @@
 
 请留意，这只是推荐结构，并不是唯一标准。quorum chain 是非常开放的，客户端完全可以按照自己的需求来构造上链数据的结构。
 
 2、converter：
 
 基于 quorum 新共识，从旧链 trx 或从 新链 trx 转换为待发布的数据。目前主要用作数据迁移：从旧共识链迁移到新共识链；在新共识链之间迁移。
 
+3、trx_type：
+
+判断 trx 的类型。该方法所返回的结果，与 rum-app，feed 等产品的处理保持一致。
+
 ### Install
 
 
 ```sh
 pip install quorum_data_py
 ```
 
 ### Examples
 
 ```python
 
 from quorum_data_py import feed
 
+# create a new post data 
 data = feed.new_post(content='hello guys')
+
+# create a like post data
 data = feed.like('a-post-id')
 
 ```
 
-### pylint
+适用于 fullnode 也适用于 lightnode，比如：
 
-```sh
-isort ./quorum_data_py
-black ./quorum_data_py
-pylint ./quorum_data_py --output=pylint.log
+```python
+
+from quorum_data_py import feed
+from quorum_fullnode_py import FullNode 
+
+jwt = "xxx"
+url = "xxx"
+
+fullnode = FullNode(url,jwt)
+data = feed.new_post(content='hello guys')
+fullnode.api.post_content(data)
 
 ```
 
+```python
+
+from quorum_data_py import feed
+from quorum_mininode_py import MiniNode 
+
+seed = "xxx"
+
+mininode = MiniNode(seed)
+data = feed.new_post(content='hello guys')
+mininode.api.post_content(data)
+
+```
+
+### Source
+
+- quorum fullnode sdk for python: https://github.com/liujuanjuan1984/quorum-fullnode-py 
+- quorum mininode sdk for python: https://github.com/liujuanjuan1984/quorum-mininode-py 
+- and more ...  https://github.com/okdaodine/awesome-quorum
 
 ### License
 
 This work is released under the `MIT` license. A copy of the license is provided in the [LICENSE](https://github.com/liujuanjuan1984/quorum_data_py/blob/master/LICENSE) file.
```

### Comparing `quorum_data_py-1.1.1/setup.py` & `quorum_data_py-1.1.3/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="quorum_data_py",
-    version="1.1.1",
+    version="1.1.3",
     author="liujuanjuan1984",
     author_email="qiaoanlu@163.com",
     description="Python Data for Apps of QuoRum",
     keywords=["quorum_data_py", "rumsystem", "quorum"],
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/liujuanjuan1984/quorum_data_py",
```

