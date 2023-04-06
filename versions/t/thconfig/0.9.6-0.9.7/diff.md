# Comparing `tmp/thconfig-0.9.6.tar.gz` & `tmp/thconfig-0.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "thconfig-0.9.6.tar", max compression
+gzip compressed data, was "thconfig-0.9.7.tar", max compression
```

## Comparing `thconfig-0.9.6.tar` & `thconfig-0.9.7.tar`

### file list

```diff
@@ -1,14 +1,13 @@
--rw-r--r--   0        0        0     1497 2022-12-16 12:17:07.000000 thconfig-0.9.6/LICENSE
--rw-r--r--   0        0        0     5912 2022-12-16 12:17:07.000000 thconfig-0.9.6/README.md
--rw-r--r--   0        0        0     1181 2022-12-16 12:17:07.000000 thconfig-0.9.6/pyproject.toml
--rw-r--r--   0        0        0        0 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/__init__.py
--rw-r--r--   0        0        0      759 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/config.py
--rw-r--r--   0        0        0      245 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/error.py
--rw-r--r--   0        0        0       27 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/file/__init__.py
--rw-r--r--   0        0        0     2968 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/file/file_config.py
--rw-r--r--   0        0        0      110 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/http/__init__.py
--rw-r--r--   0        0        0     6799 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/http/couch_config.py
--rw-r--r--   0        0        0     2153 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/http/etcd_config.py
--rw-r--r--   0        0        0       98 2022-12-16 12:17:07.000000 thconfig-0.9.6/thconfig/http/http_config.py
--rw-r--r--   0        0        0     6996 1970-01-01 00:00:00.000000 thconfig-0.9.6/setup.py
--rw-r--r--   0        0        0     7159 1970-01-01 00:00:00.000000 thconfig-0.9.6/PKG-INFO
+-rw-r--r--   0        0        0     1497 2023-04-06 13:17:58.138151 thconfig-0.9.7/LICENSE
+-rw-r--r--   0        0        0     5912 2023-04-06 13:17:58.138151 thconfig-0.9.7/README.md
+-rw-r--r--   0        0        0     1181 2023-04-06 13:17:58.139151 thconfig-0.9.7/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/__init__.py
+-rw-r--r--   0        0        0      759 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/config.py
+-rw-r--r--   0        0        0      245 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/error.py
+-rw-r--r--   0        0        0       27 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/file/__init__.py
+-rw-r--r--   0        0        0     2968 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/file/file_config.py
+-rw-r--r--   0        0        0      168 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/__init__.py
+-rw-r--r--   0        0        0     6799 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/couch_config.py
+-rw-r--r--   0        0        0     2153 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/etcd_config.py
+-rw-r--r--   0        0        0       98 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/http_config.py
+-rw-r--r--   0        0        0     7159 1970-01-01 00:00:00.000000 thconfig-0.9.7/PKG-INFO
```

### Comparing `thconfig-0.9.6/LICENSE` & `thconfig-0.9.7/LICENSE`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/README.md` & `thconfig-0.9.7/README.md`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/pyproject.toml` & `thconfig-0.9.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # Refference: https://python-poetry.org/docs/pyproject/
 [tool.poetry]
 name = "thconfig"
-version = "0.9.6"
+version = "0.9.7"
 description = "TangledHub Config reader/writter"
 license = "BSD 3-clause"
 authors = ["TangledHub <info@tangledgroup.com>"]
 readme = "README.md"
 repository = "https://gitlab.com/tangledlabs/thconfig"
 keywords = ["tangled", "tangledhub", "tangledlabs", "thconfig"]
 # Classifiers reference: https://pypi.org/classifiers/
```

### Comparing `thconfig-0.9.6/thconfig/config.py` & `thconfig-0.9.7/thconfig/config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/thconfig/file/file_config.py` & `thconfig-0.9.7/thconfig/file/file_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/thconfig/http/couch_config.py` & `thconfig-0.9.7/thconfig/http/couch_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/thconfig/http/etcd_config.py` & `thconfig-0.9.7/thconfig/http/etcd_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.6/setup.py` & `thconfig-0.9.7/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,35 +1,297 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: thconfig
+Version: 0.9.7
+Summary: TangledHub Config reader/writter
+Home-page: https://gitlab.com/tangledlabs/thconfig
+License: BSD 3-clause
+Keywords: tangled,tangledhub,tangledlabs,thconfig
+Author: TangledHub
+Author-email: info@tangledgroup.com
+Requires-Python: >=3.10,<4.0
+Classifier: Development Status :: 4 - Beta
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: BSD License
+Classifier: License :: Other/Proprietary License
+Classifier: Operating System :: OS Independent
+Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Requires-Dist: PyYAML (>=6.0,<7.0)
+Requires-Dist: aetcd (>=1.0.0a2,<2.0.0)
+Requires-Dist: aiohttp (>=3.8.3,<4.0.0)
+Requires-Dist: json5 (>=0.9.10,<0.10.0)
+Requires-Dist: thresult (>=0.9.25,<0.10.0)
+Requires-Dist: toml (>=0.10.2,<0.11.0)
+Project-URL: Repository, https://gitlab.com/tangledlabs/thconfig
+Description-Content-Type: text/markdown
 
-packages = \
-['thconfig', 'thconfig.file', 'thconfig.http']
+[![Build][build-image]]()
+[![Status][status-image]][pypi-project-url]
+[![Stable Version][stable-ver-image]][pypi-project-url]
+[![Coverage][coverage-image]]()
+[![Python][python-ver-image]][pypi-project-url]
+[![License][bsd3-image]][bsd3-url]
 
-package_data = \
-{'': ['*']}
 
-install_requires = \
-['PyYAML>=6.0,<7.0',
- 'aetcd>=1.0.0a2,<2.0.0',
- 'aiohttp>=3.8.3,<4.0.0',
- 'json5>=0.9.10,<0.10.0',
- 'thresult>=0.9.25,<0.10.0',
- 'toml>=0.10.2,<0.11.0']
-
-setup_kwargs = {
-    'name': 'thconfig',
-    'version': '0.9.6',
-    'description': 'TangledHub Config reader/writter',
-    'long_description': "[![Build][build-image]]()\n[![Status][status-image]][pypi-project-url]\n[![Stable Version][stable-ver-image]][pypi-project-url]\n[![Coverage][coverage-image]]()\n[![Python][python-ver-image]][pypi-project-url]\n[![License][bsd3-image]][bsd3-url]\n\n\n# thconfig\n\n## Overview\nTangledHub library for config with a focus on asynchronous functions\n\n## Licensing\nthconfig is licensed under the BSD license. Check the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details\n\n## Installation\n```bash\npip install thconfig\n```\n\n---\n\n## Testing\n```bash\ndocker-compose build thconfig-test ; docker-compose run --rm thconfig-test\n```\n\n## Building\n```bash\ndocker-compose build thconfig-build ; docker-compose run --rm thconfig-build\n```\n\n## Publish\n```bash\ndocker-compose build thconfig-publish ; docker-compose run --rm -e PYPI_USERNAME=__token__ -e PYPI_PASSWORD=__SECRET__ thconfig-publish\n```\n\n\n## THCONFIG supported in this library\n...\n\n## Testing\n```python\ndocker-compose build thconfig-test ; docker-compose run --rm thconfig-test\n```\n\n## Usage\n\n### File \nConfiguration from file \n\n#### setup\n```python\n'''\nA class to handle reading and writing configuration data from file\n'''\n\n# you need to provide file with data { configuration }\nconfig_path = 'example_1.json'\n\n# create instance of FileConfig\nconfig = FileConfig(config_path)\n```\n\n#### fetch\n```python\n'''\nReads config data from file\n'''\n\n# you need to provide file with data { configuration }\nconfig_path = 'example_1.json'\n\n# create instance of FileConfig\nconfig = FileConfig(config_path)\n\n# load data from configuration file if success\nres: bool = (await config.fetch()).unwrap()\n```\n\n#### commit\n```python\n'''\nWrite config data to file\n'''\n\n# you need to provide file with data { configuration }\nconfig_path = 'example_1.json'\n\n# create instance of FileConfig\nconfig = FileConfig(config_path)\n\n# set title\nconfig['title'] = 'Config Example'\n\nconfig.title2 = 'Config Example'\n\n# this function change title in file\n(await config.commit()).unwrap()\n```\n\n### CouchConfig \nConfiguration from couchdb \n\n#### setup\n```python\n'''\nA class to handle reading and writing configuration data from couchdb\n\ninstantiate CouchConfig:\n        parameters:\n            uri: str\n'''\n\n# this is url for couchdb where are configuration data \nURI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config'\n\n# create intance CouchConfig and set URI property\nconfig = CouchConfig(URI)\n```\n\n#### fetch\nFetching configuration document from couchdb\n```python\n'''\nFetching document and store data in self._state\nSync couchdb -> self._state\nhttps://docs.couchdb.org/en/stable/api/document/common.html#get--db-docid\n\nFetch:\n    parameters:\n        self: CouchConfig\n'''\n\n# this is url for couchdb where are configuration data \nURI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config'\n\n# create intance CouchConfig and set URI property\nconfig = CouchConfig(URI)\n\n# fetching data from database\nfetched_data = (await config.fetch()).unwrap()\n```\n\n#### commit\nCommit changes in configuration data in documment in couchdb\n```python\n'''\nCommit document, save data from self._state to couchdb\nSync self._state -> couchdb\nhttps://docs.couchdb.org/en/stable/api/document/common.html#put--db-docid\n\nCommit:\n    parameters:\n        self: CouchConfig\n'''\n\n# this is url for couchdb where are configuration data \nURI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config_commit_changes'\n\n# create intance CouchConfig and set URI property\nconfig = CouchConfig(URI)\n\ntitle = 'Couch Config Example'\ndatabase = {'server': '192.168.1.1'}\n\n# set title and database\nconfig['title'] = title\nconfig['database'] = database\n\n# commit\ncommit_0 = (await config.commit()).unwrap()\n```\n\n### EtcdConfig \nConfiguration from EtcdConfig \n\n#### setup\n```python\n'''\nA class to handle reading and writing configuration data from etcd\ninstantiate EtcdConfig:\n    parameters:\n        HOST: str\n        PORT: int\n'''\n\n# you need to provide host and port\nHOST = 'etcd-test'\nPORT = 2379\n\n# create instance of EtcdConfig\nconfig = EtcdConfig(host = HOST, port = PORT)\n```\n\n#### fetch\nFetching configuration document from etcd\n```python\n'''\nFetching document and store data in self._state\nSync etcd -> self._state\nhttps://aetcd3.readthedocs.io/en/latest/reference/client.html#aetcd3.client.Etcd3Client.get_all\n\nFetch:\n    parameters:\n        self: EtcdConfig\n'''\n\n# you need to provide host and port\nHOST = 'etcd-test'\nPORT = 2379\n\n# create instance of EtcdConfig\nconfig = EtcdConfig(host = HOST, port = PORT)\n\n# fetching data from etcd\nfetched_data = (await config.fetch()).unwrap()\n```\n\n#### commit\nCommit changes in configuration data to etcd\n```python\n'''\nCommit document, save data from self._state to etcd\nSync self._state -> etcd\nhttps://aetcd3.readthedocs.io/en/latest/reference/client.html#aetcd3.client.Etcd3Client.put\n\ncommit changes:\n    parameters:\n        self: EtcdConfig\n'''\n\n# you need to provide host and port\nHOST = 'etcd-test'\nPORT = 2379\n\n# create instance of EtcdConfig\nconfig = EtcdConfig(host = HOST, port = PORT)\n\ntitle = 'Couch Config Example'\ndatabase = {'server': '192.168.1.1'}\n\n# set title and database\nconfig['title'] = title\nconfig['database'] = database\n\n# commit\ncommit_0 = (await config.commit()).unwrap()\n```\n\n<!-- Links -->\n\n<!-- Badges -->\n[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg\n[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause\n[build-image]: https://img.shields.io/badge/build-success-brightgreen\n[coverage-image]: https://img.shields.io/badge/Coverage-100%25-green\n\n[pypi-project-url]: https://pypi.org/project/thquickjs/\n[stable-ver-image]: https://img.shields.io/pypi/v/thquickjs?label=stable\n[python-ver-image]: https://img.shields.io/pypi/pyversions/thquickjs.svg?logo=python&logoColor=FBE072\n[status-image]: https://img.shields.io/pypi/status/thquickjs.svg\n\n\n",
-    'author': 'TangledHub',
-    'author_email': 'info@tangledgroup.com',
-    'maintainer': 'None',
-    'maintainer_email': 'None',
-    'url': 'https://gitlab.com/tangledlabs/thconfig',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'python_requires': '>=3.10,<4.0',
-}
+# thconfig
+
+## Overview
+TangledHub library for config with a focus on asynchronous functions
+
+## Licensing
+thconfig is licensed under the BSD license. Check the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details
+
+## Installation
+```bash
+pip install thconfig
+```
+
+---
+
+## Testing
+```bash
+docker-compose build thconfig-test ; docker-compose run --rm thconfig-test
+```
+
+## Building
+```bash
+docker-compose build thconfig-build ; docker-compose run --rm thconfig-build
+```
+
+## Publish
+```bash
+docker-compose build thconfig-publish ; docker-compose run --rm -e PYPI_USERNAME=__token__ -e PYPI_PASSWORD=__SECRET__ thconfig-publish
+```
+
+
+## THCONFIG supported in this library
+...
+
+## Testing
+```python
+docker-compose build thconfig-test ; docker-compose run --rm thconfig-test
+```
+
+## Usage
+
+### File 
+Configuration from file 
+
+#### setup
+```python
+'''
+A class to handle reading and writing configuration data from file
+'''
+
+# you need to provide file with data { configuration }
+config_path = 'example_1.json'
+
+# create instance of FileConfig
+config = FileConfig(config_path)
+```
+
+#### fetch
+```python
+'''
+Reads config data from file
+'''
+
+# you need to provide file with data { configuration }
+config_path = 'example_1.json'
+
+# create instance of FileConfig
+config = FileConfig(config_path)
+
+# load data from configuration file if success
+res: bool = (await config.fetch()).unwrap()
+```
+
+#### commit
+```python
+'''
+Write config data to file
+'''
+
+# you need to provide file with data { configuration }
+config_path = 'example_1.json'
+
+# create instance of FileConfig
+config = FileConfig(config_path)
+
+# set title
+config['title'] = 'Config Example'
+
+config.title2 = 'Config Example'
+
+# this function change title in file
+(await config.commit()).unwrap()
+```
+
+### CouchConfig 
+Configuration from couchdb 
+
+#### setup
+```python
+'''
+A class to handle reading and writing configuration data from couchdb
+
+instantiate CouchConfig:
+        parameters:
+            uri: str
+'''
+
+# this is url for couchdb where are configuration data 
+URI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config'
+
+# create intance CouchConfig and set URI property
+config = CouchConfig(URI)
+```
+
+#### fetch
+Fetching configuration document from couchdb
+```python
+'''
+Fetching document and store data in self._state
+Sync couchdb -> self._state
+https://docs.couchdb.org/en/stable/api/document/common.html#get--db-docid
+
+Fetch:
+    parameters:
+        self: CouchConfig
+'''
+
+# this is url for couchdb where are configuration data 
+URI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config'
+
+# create intance CouchConfig and set URI property
+config = CouchConfig(URI)
+
+# fetching data from database
+fetched_data = (await config.fetch()).unwrap()
+```
+
+#### commit
+Commit changes in configuration data in documment in couchdb
+```python
+'''
+Commit document, save data from self._state to couchdb
+Sync self._state -> couchdb
+https://docs.couchdb.org/en/stable/api/document/common.html#put--db-docid
+
+Commit:
+    parameters:
+        self: CouchConfig
+'''
+
+# this is url for couchdb where are configuration data 
+URI = 'http://tangledhub:tangledhub@couchdb-test:5984/thconfig-test/test_couch_config_commit_changes'
+
+# create intance CouchConfig and set URI property
+config = CouchConfig(URI)
+
+title = 'Couch Config Example'
+database = {'server': '192.168.1.1'}
+
+# set title and database
+config['title'] = title
+config['database'] = database
+
+# commit
+commit_0 = (await config.commit()).unwrap()
+```
+
+### EtcdConfig 
+Configuration from EtcdConfig 
+
+#### setup
+```python
+'''
+A class to handle reading and writing configuration data from etcd
+instantiate EtcdConfig:
+    parameters:
+        HOST: str
+        PORT: int
+'''
+
+# you need to provide host and port
+HOST = 'etcd-test'
+PORT = 2379
+
+# create instance of EtcdConfig
+config = EtcdConfig(host = HOST, port = PORT)
+```
+
+#### fetch
+Fetching configuration document from etcd
+```python
+'''
+Fetching document and store data in self._state
+Sync etcd -> self._state
+https://aetcd3.readthedocs.io/en/latest/reference/client.html#aetcd3.client.Etcd3Client.get_all
+
+Fetch:
+    parameters:
+        self: EtcdConfig
+'''
+
+# you need to provide host and port
+HOST = 'etcd-test'
+PORT = 2379
+
+# create instance of EtcdConfig
+config = EtcdConfig(host = HOST, port = PORT)
+
+# fetching data from etcd
+fetched_data = (await config.fetch()).unwrap()
+```
+
+#### commit
+Commit changes in configuration data to etcd
+```python
+'''
+Commit document, save data from self._state to etcd
+Sync self._state -> etcd
+https://aetcd3.readthedocs.io/en/latest/reference/client.html#aetcd3.client.Etcd3Client.put
+
+commit changes:
+    parameters:
+        self: EtcdConfig
+'''
+
+# you need to provide host and port
+HOST = 'etcd-test'
+PORT = 2379
+
+# create instance of EtcdConfig
+config = EtcdConfig(host = HOST, port = PORT)
+
+title = 'Couch Config Example'
+database = {'server': '192.168.1.1'}
+
+# set title and database
+config['title'] = title
+config['database'] = database
+
+# commit
+commit_0 = (await config.commit()).unwrap()
+```
+
+<!-- Links -->
+
+<!-- Badges -->
+[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
+[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause
+[build-image]: https://img.shields.io/badge/build-success-brightgreen
+[coverage-image]: https://img.shields.io/badge/Coverage-100%25-green
+
+[pypi-project-url]: https://pypi.org/project/thquickjs/
+[stable-ver-image]: https://img.shields.io/pypi/v/thquickjs?label=stable
+[python-ver-image]: https://img.shields.io/pypi/pyversions/thquickjs.svg?logo=python&logoColor=FBE072
+[status-image]: https://img.shields.io/pypi/status/thquickjs.svg
+
 
 
-setup(**setup_kwargs)
```

