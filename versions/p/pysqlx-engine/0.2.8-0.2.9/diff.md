# Comparing `tmp/pysqlx_engine-0.2.8.tar.gz` & `tmp/pysqlx_engine-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pysqlx_engine-0.2.8.tar", max compression
+gzip compressed data, was "pysqlx_engine-0.2.9.tar", max compression
```

## Comparing `pysqlx_engine-0.2.8.tar` & `pysqlx_engine-0.2.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0     2346 2023-01-27 20:03:57.696355 pysqlx_engine-0.2.8/pyproject.toml
--rw-r--r--   0        0        0      342 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/__init__.py
--rw-r--r--   0        0        0     6532 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/aconn.py
--rw-r--r--   0        0        0    30261 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/aconn.pyi
--rw-r--r--   0        0        0      917 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/apool.py
--rw-r--r--   0        0        0     2786 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/apool.pyi
--rw-r--r--   0        0        0     2312 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/conn.py
--rw-r--r--   0        0        0    30012 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/conn.pyi
--rw-r--r--   0        0        0     2882 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/const.py
--rw-r--r--   0        0        0     7056 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/errors.py
--rw-r--r--   0        0        0     6337 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/helper.py
--rw-r--r--   0        0        0     4878 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/param.py
--rw-r--r--   0        0        0     3015 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/parser.py
--rw-r--r--   0        0        0      946 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/pool.py
--rw-r--r--   0        0        0     2644 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/pool.pyi
--rw-r--r--   0        0        0     3603 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/_core/until.py
--rw-r--r--   0        0        0      875 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/errors.py
--rw-r--r--   0        0        0        0 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/pysqlx_engine/py.typed
--rw-r--r--   0        0        0     4926 2023-01-27 20:03:52.724326 pysqlx_engine-0.2.8/readme.md
--rw-r--r--   0        0        0     5949 1970-01-01 00:00:00.000000 pysqlx_engine-0.2.8/setup.py
--rw-r--r--   0        0        0     6880 1970-01-01 00:00:00.000000 pysqlx_engine-0.2.8/PKG-INFO
+-rw-r--r--   0        0        0     2346 2023-01-31 13:38:27.516929 pysqlx_engine-0.2.9/pyproject.toml
+-rw-r--r--   0        0        0      342 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/__init__.py
+-rw-r--r--   0        0        0     6532 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/_core/aconn.py
+-rw-r--r--   0        0        0    30261 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/_core/aconn.pyi
+-rw-r--r--   0        0        0      917 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/_core/apool.py
+-rw-r--r--   0        0        0     2786 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/_core/apool.pyi
+-rw-r--r--   0        0        0     2312 2023-01-31 13:38:24.232802 pysqlx_engine-0.2.9/pysqlx_engine/_core/conn.py
+-rw-r--r--   0        0        0    30012 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/conn.pyi
+-rw-r--r--   0        0        0     2882 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/const.py
+-rw-r--r--   0        0        0     7056 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/errors.py
+-rw-r--r--   0        0        0     6337 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/helper.py
+-rw-r--r--   0        0        0     4878 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/param.py
+-rw-r--r--   0        0        0     3015 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/parser.py
+-rw-r--r--   0        0        0      946 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/pool.py
+-rw-r--r--   0        0        0     2644 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/pool.pyi
+-rw-r--r--   0        0        0     3603 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/_core/until.py
+-rw-r--r--   0        0        0      875 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/errors.py
+-rw-r--r--   0        0        0        0 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/pysqlx_engine/py.typed
+-rw-r--r--   0        0        0     4926 2023-01-31 13:38:24.236802 pysqlx_engine-0.2.9/readme.md
+-rw-r--r--   0        0        0     5949 1970-01-01 00:00:00.000000 pysqlx_engine-0.2.9/setup.py
+-rw-r--r--   0        0        0     6880 1970-01-01 00:00:00.000000 pysqlx_engine-0.2.9/PKG-INFO
```

### Comparing `pysqlx_engine-0.2.8/pyproject.toml` & `pysqlx_engine-0.2.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool.poetry]
 name = "pysqlx-engine"
 
-version = "0.2.8"
+version = "0.2.9"
 description = "Async and Sync SQL Engine for Python, with support for MySQL, PostgreSQL, SQLite and Microsoft SQL Server."
 authors = ["Carlos Rian <crian.rian@gmail.com>"]
 license = "MIT"
 readme = "readme.md"
 repository = "https://github.com/carlos-rian/pysqlx-engine"
 homepage = "https://carlos-rian.github.io/pysqlx-engine"
 documentation = "https://carlos-rian.github.io/pysqlx-engine"
```

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/aconn.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/aconn.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/aconn.pyi` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/aconn.pyi`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/apool.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/apool.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/apool.pyi` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/apool.pyi`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/conn.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/conn.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/conn.pyi` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/conn.pyi`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/const.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/const.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/errors.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/errors.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/helper.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/helper.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/param.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/param.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/parser.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/parser.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/pool.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/pool.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/pool.pyi` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/pool.pyi`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/_core/until.py` & `pysqlx_engine-0.2.9/pysqlx_engine/_core/until.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/pysqlx_engine/errors.py` & `pysqlx_engine-0.2.9/pysqlx_engine/errors.py`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/readme.md` & `pysqlx_engine-0.2.9/readme.md`

 * *Files identical despite different names*

### Comparing `pysqlx_engine-0.2.8/setup.py` & `pysqlx_engine-0.2.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 ['Pygments>=2.14.0,<3.0.0',
  'pydantic>=1.10.4,<2.0.0',
  'pysqlx-core>=0.1.39,<0.2.0',
  'typing-extensions>=4.4.0,<5.0.0']
 
 setup_kwargs = {
     'name': 'pysqlx-engine',
-    'version': '0.2.8',
+    'version': '0.2.9',
     'description': 'Async and Sync SQL Engine for Python, with support for MySQL, PostgreSQL, SQLite and Microsoft SQL Server.',
     'long_description': '# PySQLXEngine\n\n<p align="center">\n  <a href="/"><img src="https://carlos-rian.github.io/pysqlx-engine/img/logo-text3.png" alt="PySQLXEngine Logo"></a>\n</p>\n<p align="center">\n    <em>PySQLXEngine, a fast and minimalist SQL engine</em>\n</p>\n\n<p align="center">\n<a href="https://github.com/carlos-rian/pysqlx-engine/actions?query=workflow%3ATest+event%3Apush+branch%3Amain" target="_blank">\n    <img src="https://github.com/carlos-rian/pysqlx-engine/workflows/Test/badge.svg?event=push&branch=main" alt="test">\n</a>\n<a href="https://app.codecov.io/gh/carlos-rian/pysqlx-engine" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/carlos-rian/pysqlx-engine?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/pysqlx-engine" target="_blank">\n    <img src="https://img.shields.io/pypi/v/pysqlx-engine?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/pysqlx-engine" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/pysqlx-engine.svg?color=%2334D058" alt="Supported Python versions">\n</a>\n<a href="https://pepy.tech/project/pysqlx-engine" target="_blank">\n    <img src="https://static.pepy.tech/personalized-badge/pysqlx-engine?period=total&units=international_system&left_color=grey&right_color=%2334D058&left_text=downloads" alt="Downloads">\n</a>\n</p>\n\n---\n\n**Documentation**: <a href="https://carlos-rian.github.io/pysqlx-engine/" target="_blank">https://carlos-rian.github.io/pysqlx-engine/</a>\n\n**Source Code**: <a href="https://github.com/carlos-rian/pysqlx-engine" target="_blank">https://github.com/carlos-rian/pysqlx-engine</a>\n\n---\n\nPySQLXEngine supports the option of sending **Raw SQL** to your database.\n\nThe PySQLXEngine is a minimalist [SQL Engine](https://github.com/carlos-rian/pysqlx-engine).\n\nThe PySQLXEngine was created and thought to be minimalistic, but very efficient. The core is write in [**Rust**](https://www.rust-lang.org), making communication between Databases and [**Python**](https://python-poetry.org) more efficient.\n\nAll SQL executed using PySQLXEngine is atomic; only one instruction is executed at a time. Only the first one will be completed if you send an Insert and a select. This is one of the ways to handle SQL ingestion. As of version **0.2.0**, PySQLXEngine supports transactions, where you can control [`BEGIN`](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/begin-end-transact-sql?view=sql-server-ver16), [`COMMIT`](https://www.geeksforgeeks.org/difference-between-commit-and-rollback-in-sql), [ `ROLLBACK` ](https://www.geeksforgeeks.org/difference-between-commit-and-rollback-in-sql), [`ISOLATION LEVEL`](https://levelup.gitconnected.com/understanding-isolation-levels-in-a-database-transaction-af78aea3f44), etc. as you wish.\n\n\n> **NOTE**:\n    Minimalism is not the lack of something, but having exactly what you need.\n    PySQLXEngine aims to expose an easy interface for you to communicate with the database in a simple, intuitive way and with good help through documentation, autocompletion, typing, and good practices.\n---\n\nDatabase Support:\n\n* [`SQLite`](https://www.sqlite.org/index.html)\n* [`PostgreSQL`](https://www.postgresql.org/)\n* [`MySQL`](https://www.mysql.com/)\n* [`Microsoft SQL Server`](https://www.microsoft.com/sql-server)\n\nOS Support:\n\n* [`Linux`](https://pt.wikipedia.org/wiki/Linux)\n* [`MacOS`](https://pt.wikipedia.org/wiki/Macos)\n* [`Windows`](https://pt.wikipedia.org/wiki/Microsoft_Windows)\n\n\n## Installation\n\n\nPIP\n\n```console\n$ pip install pysqlx-engine\n```\n\nPoetry\n\n```console\n$ poetry add pysqlx-engine\n```\n\n## Async Example\n\nCreate a `main.py` file and add the code examples below.\n\n```python\nfrom pysqlx_engine import PySQLXEngine\n\nasync def main():\n    db = PySQLXEngine(uri="sqlite:./db.db")\n    await db.connect()\n\n    await db.execute(sql="CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name TEXT, age INT)")\n    await db.execute(sql="INSERT INTO users (name, age) VALUES (\'Rian\', \'28\')")\n    await db.execute(sql="INSERT INTO users (name, age) VALUES (\'Carlos\', \'29\')")\n\n    rows = await db.query(sql="SELECT * FROM users")\n\n    print(rows)\n\nimport asyncio\nasyncio.run(main())\n```\n\n## Sync Example\n\nCreate a `main.py` file and add the code examples below.\n\n```python\nfrom pysqlx_engine import PySQLXEngineSync\n\ndef main():\n    db = PySQLXEngineSync(uri="sqlite:./db.db")\n    db.connect()\n\n    db.execute(sql="CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name TEXT, age INT)")\n    db.execute(sql="INSERT INTO users (name, age) VALUES (\'Rian\', \'28\')")\n    db.execute(sql="INSERT INTO users (name, age) VALUES (\'Carlos\', \'29\')")\n\n    rows = db.query(sql="SELECT * FROM users")\n\n    print(rows)\n\n# running the code\nmain()\n```\n\nRunning the code using the terminal\n\n\n```console\n$ python3 main.py\n```\nOutput\n\n```python\n[\n    BaseRow(id=1, name=\'Rian\', age=28),  \n    BaseRow(id=2, name=\'Carlos\', age=29)\n]\n```\n',
     'author': 'Carlos Rian',
     'author_email': 'crian.rian@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://carlos-rian.github.io/pysqlx-engine',
```

#### html2text {}

```diff
@@ -1,12 +1,12 @@
 # -*- coding: utf-8 -*- from setuptools import setup packages = \
 ['pysqlx_engine', 'pysqlx_engine._core'] package_data = \ {'': ['*']}
 install_requires = \ ['Pygments>=2.14.0,<3.0.0', 'pydantic>=1.10.4,<2.0.0',
 'pysqlx-core>=0.1.39,<0.2.0', 'typing-extensions>=4.4.0,<5.0.0'] setup_kwargs =
-{ 'name': 'pysqlx-engine', 'version': '0.2.8', 'description': 'Async and Sync
+{ 'name': 'pysqlx-engine', 'version': '0.2.9', 'description': 'Async and Sync
 SQL Engine for Python, with support for MySQL, PostgreSQL, SQLite and Microsoft
 SQL Server.', 'long_description': '# PySQLXEngine\n\n
                            \n [PySQLXEngine_Logo]\n
 \n
               \n PySQLXEngine, a fast and minimalist SQL engine\n
 \n\n
  \n\n_[test]\n\n\n_[Coverage]\n\n\n_[Package_version]\n\n\n_[Supported_Python
```

### Comparing `pysqlx_engine-0.2.8/PKG-INFO` & `pysqlx_engine-0.2.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysqlx-engine
-Version: 0.2.8
+Version: 0.2.9
 Summary: Async and Sync SQL Engine for Python, with support for MySQL, PostgreSQL, SQLite and Microsoft SQL Server.
 Home-page: https://carlos-rian.github.io/pysqlx-engine
 License: MIT
 Keywords: async,database,sql,engine,fastapi
 Author: Carlos Rian
 Author-email: crian.rian@gmail.com
 Requires-Python: >=3.7,<4.0
```

