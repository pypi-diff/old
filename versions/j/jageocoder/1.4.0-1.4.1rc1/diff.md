# Comparing `tmp/jageocoder-1.4.0.tar.gz` & `tmp/jageocoder-1.4.1rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jageocoder-1.4.0.tar", last modified: Sat Mar 11 05:36:26 2023, max compression
+gzip compressed data, was "jageocoder-1.4.1rc1.tar", max compression
```

## Comparing `jageocoder-1.4.0.tar` & `jageocoder-1.4.1rc1.tar`

### file list

```diff
@@ -1,39 +1,21 @@
-drwxr-xr-x   0 sagara    (1000) sagara    (1000)        0 2023-03-11 05:36:26.534053 jageocoder-1.4.0/
--rw-r--r--   0 sagara    (1000) sagara    (1000)      113 2022-12-31 11:33:15.000000 jageocoder-1.4.0/LICENSE
--rw-r--r--   0 sagara    (1000) sagara    (1000)    12322 2023-03-11 05:36:26.534053 jageocoder-1.4.0/PKG-INFO
--rw-r--r--   0 sagara    (1000) sagara    (1000)    11683 2023-03-11 02:17:26.000000 jageocoder-1.4.0/README.md
-drwxr-xr-x   0 sagara    (1000) sagara    (1000)        0 2023-03-11 05:36:26.524053 jageocoder-1.4.0/jageocoder/
--rw-r--r--   0 sagara    (1000) sagara    (1000)     1405 2023-03-11 05:36:12.000000 jageocoder-1.4.0/jageocoder/__init__.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     5194 2023-03-11 02:17:26.000000 jageocoder-1.4.0/jageocoder/__main__.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     2574 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/address.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    12277 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/aza_master.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)      339 2023-02-12 06:55:46.000000 jageocoder-1.4.0/jageocoder/base.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)      676 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/dataset.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)      691 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/exceptions.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    18876 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/itaiji.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    14220 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/itaiji_dic.json
--rw-r--r--   0 sagara    (1000) sagara    (1000)    12276 2023-03-11 02:17:26.000000 jageocoder-1.4.0/jageocoder/module.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    29136 2023-03-11 02:17:26.000000 jageocoder-1.4.0/jageocoder/node.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)      991 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/note.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     2693 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/result.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    16587 2023-03-11 02:17:26.000000 jageocoder-1.4.0/jageocoder/rev.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     7854 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/strlib.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    51847 2023-03-11 02:17:26.000000 jageocoder-1.4.0/jageocoder/tree.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     5185 2022-12-31 11:33:15.000000 jageocoder-1.4.0/jageocoder/trie.py
-drwxr-xr-x   0 sagara    (1000) sagara    (1000)        0 2023-03-11 05:36:26.524053 jageocoder-1.4.0/jageocoder.egg-info/
--rw-r--r--   0 sagara    (1000) sagara    (1000)    12322 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/PKG-INFO
--rw-r--r--   0 sagara    (1000) sagara    (1000)      748 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/SOURCES.txt
--rw-r--r--   0 sagara    (1000) sagara    (1000)        1 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/dependency_links.txt
--rw-r--r--   0 sagara    (1000) sagara    (1000)       56 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/entry_points.txt
--rw-r--r--   0 sagara    (1000) sagara    (1000)       62 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/requires.txt
--rw-r--r--   0 sagara    (1000) sagara    (1000)       11 2023-03-11 05:36:26.000000 jageocoder-1.4.0/jageocoder.egg-info/top_level.txt
--rw-r--r--   0 sagara    (1000) sagara    (1000)     1038 2023-03-11 05:22:03.000000 jageocoder-1.4.0/pyproject.toml
--rw-r--r--   0 sagara    (1000) sagara    (1000)      957 2023-03-11 05:36:26.534053 jageocoder-1.4.0/setup.cfg
--rw-r--r--   0 sagara    (1000) sagara    (1000)       55 2023-03-11 04:20:52.000000 jageocoder-1.4.0/setup.py
-drwxr-xr-x   0 sagara    (1000) sagara    (1000)        0 2023-03-11 05:36:26.534053 jageocoder-1.4.0/tests/
--rw-r--r--   0 sagara    (1000) sagara    (1000)     2858 2022-12-31 11:33:15.000000 jageocoder-1.4.0/tests/test_code.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     2372 2022-12-31 11:33:15.000000 jageocoder-1.4.0/tests/test_createdb.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     2304 2022-12-31 11:33:15.000000 jageocoder-1.4.0/tests/test_itaiji.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)     3540 2023-02-12 06:55:46.000000 jageocoder-1.4.0/tests/test_reverse.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)    26873 2022-12-31 11:33:15.000000 jageocoder-1.4.0/tests/test_search.py
--rw-r--r--   0 sagara    (1000) sagara    (1000)      557 2022-12-31 11:33:15.000000 jageocoder-1.4.0/tests/test_strlib.py
+-rw-r--r--   0        0        0      113 2023-03-13 04:34:17.970010 jageocoder-1.4.1rc1/LICENSE
+-rw-r--r--   0        0        0    11683 2023-03-13 04:34:17.970010 jageocoder-1.4.1rc1/README.md
+-rw-r--r--   0        0        0     1365 2023-04-07 01:57:33.442274 jageocoder-1.4.1rc1/jageocoder/__init__.py
+-rw-r--r--   0        0        0     5792 2023-04-07 01:40:25.133090 jageocoder-1.4.1rc1/jageocoder/__main__.py
+-rw-r--r--   0        0        0     2574 2023-03-13 04:34:17.974010 jageocoder-1.4.1rc1/jageocoder/address.py
+-rw-r--r--   0        0        0    12277 2023-04-07 01:18:05.462895 jageocoder-1.4.1rc1/jageocoder/aza_master.py
+-rw-r--r--   0        0        0      339 2023-04-07 01:18:05.462895 jageocoder-1.4.1rc1/jageocoder/base.py
+-rw-r--r--   0        0        0      676 2023-04-07 01:18:05.462895 jageocoder-1.4.1rc1/jageocoder/dataset.py
+-rw-r--r--   0        0        0      691 2023-03-13 04:34:17.974010 jageocoder-1.4.1rc1/jageocoder/exceptions.py
+-rw-r--r--   0        0        0    18862 2023-04-07 01:47:15.772927 jageocoder-1.4.1rc1/jageocoder/itaiji.py
+-rw-r--r--   0        0        0    14220 2023-03-13 04:34:17.974010 jageocoder-1.4.1rc1/jageocoder/itaiji_dic.json
+-rw-r--r--   0        0        0    12242 2023-04-07 01:40:58.365275 jageocoder-1.4.1rc1/jageocoder/module.py
+-rw-r--r--   0        0        0    29136 2023-04-07 01:18:05.466894 jageocoder-1.4.1rc1/jageocoder/node.py
+-rw-r--r--   0        0        0      991 2023-04-07 01:18:05.466894 jageocoder-1.4.1rc1/jageocoder/note.py
+-rw-r--r--   0        0        0     2643 2023-04-07 01:49:25.338650 jageocoder-1.4.1rc1/jageocoder/result.py
+-rw-r--r--   0        0        0    16727 2023-04-07 01:55:47.264507 jageocoder-1.4.1rc1/jageocoder/rev.py
+-rw-r--r--   0        0        0     7854 2023-03-13 04:34:17.974010 jageocoder-1.4.1rc1/jageocoder/strlib.py
+-rw-r--r--   0        0        0    51920 2023-04-07 01:46:02.292036 jageocoder-1.4.1rc1/jageocoder/tree.py
+-rw-r--r--   0        0        0     5185 2023-04-07 01:18:05.466894 jageocoder-1.4.1rc1/jageocoder/trie.py
+-rw-r--r--   0        0        0     1071 2023-04-07 01:57:24.862130 jageocoder-1.4.1rc1/pyproject.toml
+-rw-r--r--   0        0        0    13007 1970-01-01 00:00:00.000000 jageocoder-1.4.1rc1/PKG-INFO
```

### Comparing `jageocoder-1.4.0/PKG-INFO` & `jageocoder-1.4.1rc1/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,25 +1,7 @@
-Metadata-Version: 2.1
-Name: jageocoder
-Version: 1.4.0
-Summary: A Python implementation of Japanese-address geocoder.
-Home-page: https://github.com/t-sagara/jageocoder
-Download-URL: https://github.com/t-sagara/jageocoder
-Author: Takeshi Sagara
-Author-email: sagara@info-proto.com
-License: MIT
-Keywords: geocoder,Japanese,address
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.6
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
 # jageocoder - A Python Japanese geocoder
 
 日本語版は README_ja.md をお読みください。
 
 This is a Python port of the Japanese-address geocoder used in CSIS at the University of Tokyo's ["Address Matching Service"](https://newspat.csis.u-tokyo.ac.jp/geocode/modules/addmatch/index.php?content_id=1) and [GSI Maps](https://maps.gsi.go.jp/).
 
 # Getting Started
```

### Comparing `jageocoder-1.4.0/README.md` & `jageocoder-1.4.1rc1/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,7 +1,39 @@
+Metadata-Version: 2.1
+Name: jageocoder
+Version: 1.4.1rc1
+Summary: A Japanese-address geocoder for Python.
+Home-page: https://github.com/t-sagara/jageocoder/
+License: The MIT License
+Author: Takeshi Sagara
+Author-email: sagara@info-proto.com
+Requires-Python: >=3.7,<4.0
+Classifier: License :: OSI Approved :: MIT License
+Classifier: License :: Other/Proprietary License
+Classifier: Operating System :: MacOS
+Classifier: Operating System :: Microsoft :: Windows :: Windows 11
+Classifier: Operating System :: POSIX :: Linux
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3
+Requires-Dist: SQLAlchemy (>=2.0.4,<3.0.0)
+Requires-Dist: Werkzeug (>=2.2.3)
+Requires-Dist: deprecated (>=1.2.13,<2.0.0)
+Requires-Dist: docopt (>=0.6.2,<0.7.0)
+Requires-Dist: geographiclib (>=2.0,<3.0)
+Requires-Dist: jaconv (>=0.3.4,<0.4.0)
+Requires-Dist: marisa-trie (>=0.7.8,<0.8.0)
+Project-URL: Documentation, https://jageocoder.readthedocs.io/
+Project-URL: Repository, https://github.com/t-sagara/jageocoder/
+Description-Content-Type: text/markdown
+
 # jageocoder - A Python Japanese geocoder
 
 日本語版は README_ja.md をお読みください。
 
 This is a Python port of the Japanese-address geocoder used in CSIS at the University of Tokyo's ["Address Matching Service"](https://newspat.csis.u-tokyo.ac.jp/geocode/modules/addmatch/index.php?content_id=1) and [GSI Maps](https://maps.gsi.go.jp/).
 
 # Getting Started
@@ -392,7 +424,8 @@
 
 We would like to thank CSIS for allowing us to provide address matching services
 on their institutional website for over 20 years.
 
 We would also like to thank Professor Asanobu Kitamoto of NII for providing us
 with a large sample of areas using the older address system and for his many help
 in confirming the results of our analysis.
+
```

### Comparing `jageocoder-1.4.0/jageocoder/__init__.py` & `jageocoder-1.4.1rc1/jageocoder/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 running the following steps.
 
     >>> import jageocoder
     >>> jageocoder.init()
     >>> jageocoder.searchNode('<Japanese-address>')
 """
 
-__version__ = '1.4.0'  # The package version
+__version__ = '1.4.1rc1'  # The package version
 __dictionary_version__ = '20220519'  # Compatible dictionary version
 __author__ = 'Takeshi Sagara <sagara@info-proto.com>'
 
 __all__ = [
     'init',
     'free',
     'is_initialized',
@@ -46,8 +46,8 @@
 ]
 
 from jageocoder.module import init, free, is_initialized,\
     get_db_dir, set_search_config, get_search_config,\
     get_module_tree, download_dictionary, install_dictionary,\
     uninstall_dictionary, migrate_dictionary, create_trie_index,\
     search, searchNode, reverse, version, dictionary_version,\
-    installed_dictionary_version, installed_dictionary_readme  # noqa: F401
+    installed_dictionary_version
```

### Comparing `jageocoder-1.4.0/jageocoder/__main__.py` & `jageocoder-1.4.1rc1/jageocoder/__main__.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,31 +1,34 @@
 import json
 import logging
+import os
 import sys
 from typing import Optional
 
 import jageocoder
 from jageocoder.exceptions import JageocoderError
 from docopt import docopt
 
-HELP = """
+HELP = r"""
 'jageocoder' is a Python package of Japanese-address geocoder.
 
 Usage:
   {p} -h
+  {p} -v
   {p} search [-d] [--area=<area>] [--db-dir=<dir>] [--force-aza-skip|--disable-aza-skip] <address>
   {p} reverse [-d] [--level=<level>] [--db-dir=<dir>] <longitude> <latitude>
   {p} get-db-dir [-d]
   {p} download-dictionary [-d] [--gaiku] [<url>]
   {p} install-dictionary [-d] [--gaiku] [--db-dir=<dir>] [<url_or_path>]
   {p} uninstall-dictionary [-d] [--db-dir=<dir>]
   {p} migrate-dictionary [-d] [--db-dir=<dir>]
 
 Options:
   -h --help           Show this help.
+  -v --version        Show package version.
   -d --debug          Show debug messages.
   --area=<area>       Specify the target area by jiscode or names.
   --force-aza-skip    Skip aza-names whenever possible.
   --disable-aza-skip  Do not skip aza-names.
   --level=<level>     Max address level to search.
   --gaiku             Use block-level (default: building-level)
   --db-dir=<dir>      Specify dictionary directory.
@@ -53,15 +56,15 @@
 - Uninstall dictionary in '/home/foo/jageocoder_db/'
 
   {p} uninstall-dictionary --db-dir=/home/foo/jagteocoder_db
 
 - Migrate dictionary (after upgrading the package)
 
   {p} migrate-dictionary
-""".format(p='jageocoder')
+""".format(p='jageocoder')  # noqa: E501
 
 
 def get_download_url(level: Optional[str] = None,
                      version: Optional[str] = None):
     """
     Generate dictionary file download url.
 
@@ -87,14 +90,18 @@
 
     return url
 
 
 def main():
     args = docopt(HELP)
 
+    if args['--version']:
+        print(jageocoder.__version__)
+        exit(0)
+
     if args['--debug']:
         log_level = logging.DEBUG
     else:
         log_level = logging.INFO
 
     if args['get-db-dir']:
         print(jageocoder.get_db_dir(mode='r'))
@@ -119,14 +126,24 @@
         try:
             jageocoder.set_search_config(
                 aza_skip=skip_aza, target_area=target_area)
             print(json.dumps(
                 jageocoder.search(query=args['<address>']),
                 ensure_ascii=False))
         except RuntimeError:
+            if args['--area'] is None:
+                db_dir = os.environ.get("JAGEOCODER_DB_DIR")
+                if db_dir is not None:
+                    print((
+                        "In the directory {} specified by the JAGEOCODER_DB_DIR "
+                        "environment variable, ").format(db_dir),
+                        end="")
+
+                print("The dictionary is not installed correctly")
+                exit(0)
             print(
                 "'{}' is incorrect as a parameter for the --area option.".format(
                     args['--area']),
                 file=sys.stderr)
 
     elif args['reverse']:
         from jageocoder.address import AddressLevel
```

### Comparing `jageocoder-1.4.0/jageocoder/address.py` & `jageocoder-1.4.1rc1/jageocoder/address.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/aza_master.py` & `jageocoder-1.4.1rc1/jageocoder/aza_master.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/dataset.py` & `jageocoder-1.4.1rc1/jageocoder/dataset.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/exceptions.py` & `jageocoder-1.4.1rc1/jageocoder/exceptions.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/itaiji.py` & `jageocoder-1.4.1rc1/jageocoder/itaiji.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import json
 from logging import getLogger
 import os
 import re
-from typing import Union, List, NoReturn, Optional
+from typing import Union, List, Optional
 
 import jaconv
 
 from jageocoder.address import AddressLevel
 from jageocoder.strlib import strlib
 
 logger = getLogger(__name__)
@@ -23,15 +23,15 @@
     kana_letters = (strlib.HIRAGANA, strlib.KATAKANA)
     latin1_letters = (strlib.ASCII, strlib.NUMERIC, strlib.ALPHABET)
     trans_itaiji = None
     trans_h2z = None
     trans_z2h = None
 
     @classmethod
-    def read_itaiji_table(cls) -> NoReturn:
+    def read_itaiji_table(cls) -> None:
         if cls.trans_itaiji is not None:
             # The table is already prepared.
             return
 
         itaiji_dic_json = os.path.join(
             os.path.dirname(__file__), 'itaiji_dic.json')
```

### Comparing `jageocoder-1.4.0/jageocoder/itaiji_dic.json` & `jageocoder-1.4.1rc1/jageocoder/itaiji_dic.json`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/module.py` & `jageocoder-1.4.1rc1/jageocoder/module.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import logging
 import os
 import tempfile
-from typing import Optional, NoReturn, Union, List
+from typing import Optional, Union, List
 import urllib.request
 from urllib.error import URLError
 import zipfile
 
 import jageocoder
 from jageocoder.exceptions import JageocoderError
 from jageocoder.tree import AddressTree, get_db_dir
@@ -14,15 +14,15 @@
 _tree = None  # The default AddressTree
 logger = logging.getLogger(__name__)
 
 
 def init(db_dir: Optional[os.PathLike] = None,
          mode: Optional[str] = 'r',
          debug: Optional[bool] = False,
-         **kwargs) -> NoReturn:
+         **kwargs) -> None:
     """
     Initialize the module-level AddressTree object `jageocoder.tree`
     ready for use.
 
     Parameters
     ----------
     db_dir: os.PathLike, optional
@@ -142,15 +142,15 @@
     AddressTree
         The singleton object.
     """
     global _tree
     return _tree
 
 
-def download_dictionary(url: str) -> NoReturn:
+def download_dictionary(url: str) -> None:
     """
     Download address-dictionary from the specified url into
     the current directory.
 
     Parameters
     ----------
     url: str
@@ -170,15 +170,15 @@
         raise JageocoderError(
             "The dictionary file could not be downloaded"
             + " from the URL {}".format(url))
 
 
 def install_dictionary(
         path_or_url: os.PathLike,
-        db_dir: Optional[os.PathLike] = None) -> NoReturn:
+        db_dir: Optional[os.PathLike] = None) -> None:
     """
     Install address-dictionary from the specified path or url.
 
     Parameters
     ----------
     path_or_url: os.PathLike
         The file path or url where the zipped address-dictionary file
@@ -239,15 +239,15 @@
     # Put metadata.txt
     with open(os.path.join(db_dir, "metadata.txt"), "w") as f:
         print(os.path.basename(path_or_url), file=f)
 
     logger.info('Installation completed.')
 
 
-def uninstall_dictionary(db_dir: Optional[os.PathLike] = None) -> NoReturn:
+def uninstall_dictionary(db_dir: Optional[os.PathLike] = None) -> None:
     """
     Uninstall address-dictionary.
 
     Parameters
     ----------
     db_dir: os.PathLike, optional
         The directory where the database files has been installed.
@@ -260,15 +260,15 @@
     # Remove the directory
     logger.info('Removing directory {}'.format(db_dir))
     import shutil
     shutil.rmtree(db_dir)
     logger.info('Dictionary has been uninstalled.')
 
 
-def migrate_dictionary(db_dir: Optional[os.PathLike] = None) -> NoReturn:
+def migrate_dictionary(db_dir: Optional[os.PathLike] = None) -> None:
     """
     Migrate address-dictionary.
 
     Parameters
     ----------
     db_dir: os.PathLike, optional
         The directory where the database files has been installed.
@@ -426,15 +426,15 @@
     global _tree
     _reverse = Reverse(x=x, y=y, tree=_tree, max_level=level)
     results = _reverse.search()
 
     return results
 
 
-def create_trie_index() -> NoReturn:
+def create_trie_index() -> None:
     """
     Create the TRIE index from the database file.
 
     This function is a shortcut for AddressTree.create_trie_index().
     """
     if not is_initialized():
         raise JageocoderError("Not initialized. Call 'init()' first.")
```

### Comparing `jageocoder-1.4.0/jageocoder/node.py` & `jageocoder-1.4.1rc1/jageocoder/node.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/note.py` & `jageocoder-1.4.1rc1/jageocoder/note.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/result.py` & `jageocoder-1.4.1rc1/jageocoder/result.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,13 @@
+from __future__ import annotations
 import json
 from logging import getLogger
-from typing import NoReturn, Optional, Union
+from typing import NoReturn, Optional, Union, TYPE_CHECKING
 
-if False:
-    # For Python 3.6 compatibility, do not use
-    # 'from __future__ import annotations' here.
+if TYPE_CHECKING:
     from jageocoder.node import AddressNode
 
 logger = getLogger(__name__)
 
 
 class Result(object):
     """
@@ -22,32 +21,32 @@
         The matched substring of the query.
     nchars: int
         The number of matched characters.
         It is used only for recursive search.
     """
 
     def __init__(self,
-                 node: Optional['AddressNode'] = None,
+                 node: Optional[AddressNode] = None,
                  matched: str = '',
                  nchars: int = 0):
         self.node = node
         self.matched = matched
         self.nchars = nchars
 
-    def set(self, node: 'AddressNode',
-            matched: str, nchars: int = 0) -> 'Result':
+    def set(self, node: AddressNode,
+            matched: str, nchars: int = 0) -> Result:
         """
         Set node and matched string.
         """
         self.node = node
         self.matched = matched
         self.matched = nchars or len(matched)
         return self
 
-    def get_node(self) -> 'AddressNode':
+    def get_node(self) -> AddressNode:
         """
         Get the node part of the result.
 
         Return
         ------
         AddressNode:
             The matched node.
@@ -64,25 +63,25 @@
             The matched substring.
         """
         return self.matched
 
     def get_matched_nchars(self) -> int:
         return self.nchars
 
-    def __getitem__(self, pos) -> Union['AddressNode', str]:
+    def __getitem__(self, pos) -> Union[AddressNode, str]:
         if pos == 0:
             return self.node
         elif pos == 1:
             return self.matched
         elif pos == 2:
             return self.nchars
 
         raise IndexError()
 
-    def __setitem__(self, pos, val: Union['AddressNode', str]) -> NoReturn:
+    def __setitem__(self, pos, val: Union[AddressNode, str]) -> NoReturn:
         from jageocoder.node import AddressNode
         if pos == 0 and isinstance(val, AddressNode):
             self.node = val
         elif pos == 1 and isinstance(val, str):
             self.matched = val
         elif pos == 2 and isinstance(val, int):
             self.nchars = val
```

### Comparing `jageocoder-1.4.0/jageocoder/rev.py` & `jageocoder-1.4.1rc1/jageocoder/rev.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 from logging import getLogger
 import math
-from typing import List, NoReturn, Optional, Union
+from typing import List, Optional, Union
 
 from geographiclib.geodesic import Geodesic
 from sqlalchemy.sql import text
 
 from jageocoder.address import AddressLevel
 from jageocoder.node import AddressNode
 from jageocoder.tree import AddressTree
 
 logger = getLogger(__name__)
 
 
 def p_contained(
-        p: [float, float], p0: [float, float],
-        p1: [float, float], p2: [float, float]) -> bool:
+        p: List[float, float],
+        p0: List[float, float],
+        p1: List[float, float],
+        p2: List[float, float]) -> bool:
     """
     Determine if the point p is inside the triangle (p0, p1, p2).
 
     Parameters
     ----------
     p: (float, float)
         x and y coordinates of point p.
@@ -45,16 +47,18 @@
     if 0 < s < area and 0 < t < area and 0 < area - s - t < area:
         return True
 
     return False
 
 
 def get_circumcircle(
-        p0: [float, float], p1: [float, float],
-        p2: [float, float]) -> [float, float, float]:
+    p0: List[float, float],
+    p1: List[float, float],
+    p2: List[float, float]
+) -> List[float, float, float]:
     """
     Calculate the coordinates and radius of the circumcircle
     of the triangle (p0, p1, p2).
 
     Parameters
     ----------
     p0, p1, p2: (float, float)
@@ -80,16 +84,19 @@
     x = xt / c
     y = yt / c
     r2 = (x - p0[0]) * (x - p0[0]) + (y - p0[1]) * (y - p0[1])
     return [x, y, r2]
 
 
 def p_contained_circumcircle(
-        p: [float, float], p0: [float, float],
-        p1: [float, float], p2: [float, float]) -> bool:
+    p: List[float, float],
+    p0: List[float, float],
+    p1: List[float, float],
+    p2: List[float, float]
+) -> bool:
     """
     Determine if the point p is inside the circumcircle of
     triangle (p0, p1, p2).
 
     Parameters
     ----------
     p: (float, float)
@@ -119,15 +126,15 @@
 
     def get_node(self) -> AddressNode:
         return self.node
 
     def get_dist(self) -> Union[float, None]:
         return self.dist
 
-    def set_dist(self, dist: float) -> NoReturn:
+    def set_dist(self, dist: float) -> None:
         self.dist = dist
 
 
 class Reverse(object):
     """
     Class for reverse geocoding.
 
@@ -144,16 +151,18 @@
     This class is not extended sqlalchemy.ext.declarative.
     Therefore, database operations are performed by calling SQL directly.
     """
 
     tablename = 'node_aza'
     geod = Geodesic.WGS84
 
-    def __init__(self, x: float, y: float,
-                 tree: AddressTree, max_level: Optional[int] = None):
+    def __init__(
+        self, x: float, y: float,
+        tree: AddressTree, max_level: Optional[int] = None
+    ) -> None:
         """
         Initialize.
 
         Attributes
         ----------
         x, y: float
             The x(lon) and y(lat) coordinates of the target point.
@@ -174,24 +183,23 @@
         self.y = y
         self.tree = tree
         self.max_level = max_level or AddressLevel.AZA
         self.candidates = []
         self.triangle = None
         self.mbr = None
 
-    def clear(self):
+    def clear(self) -> None:
         """
         Clear the stack of Address Candidates.
         """
         self.candidates.clear()
         self.triangle = None
         self.mbr = None
 
     def is_in_circumcircle(self, node: AddressNode) -> bool:
-
         if self.mbr:
             if node.x < self.mbr['minx'] or node.x > self.mbr['maxx'] or\
                     node.y < self.mbr['miny'] or node.y > self.mbr['maxy']:
                 return False
 
         if self.triangle:
             contained = p_contained_circumcircle(
@@ -200,15 +208,15 @@
                 [self.triangle[1].x, self.triangle[1].y],
                 [self.triangle[2].x, self.triangle[2].y])
 
             return contained
 
         return False
 
-    def update_mbr(self) -> NoReturn:
+    def update_mbr(self) -> None:
         x, y, r2 = get_circumcircle(
             [self.triangle[0].x, self.triangle[0].y],
             [self.triangle[1].x, self.triangle[1].y],
             [self.triangle[2].x, self.triangle[2].y])
 
         r = math.sqrt(r2)
 
@@ -303,15 +311,18 @@
                         return True
 
         self.candidates.append(cand)
         logger.debug(("The triangle could not be composed, "
                       "so the node added to the list."))
         return True
 
-    def add_candidate_by_distance(self, cand: ReverseCandidate) -> bool:
+    def add_candidate_by_distance(
+            self,
+            cand: ReverseCandidate
+    ) -> bool:
         """
         Add an address candidate and select top-k nearest neighbors.
 
         Parameters
         ----------
         node: AddressNode
             A candidate address node.
@@ -337,15 +348,16 @@
         self.candidates.insert(i, cand)
         self.candidates = self.candidates[0:3]
         return True
 
     def add_candidate_recursively(
             self,
             seed_node: AddressNode,
-            max_level: Optional[int] = None) -> bool:
+            max_level: Optional[int] = None
+    ) -> bool:
         """
         Add one address node as a candidate, and add its child nodes recursively.
         This method call `add_candidate()` which calls `add_candidate()`
         to compose Delaunay triangle.
 
         Parameters
         ----------
@@ -375,15 +387,16 @@
                 return False
 
         return True
 
     def add_candidate_recursively_simple(
             self,
             seed_node: AddressNode,
-            max_level: Optional[int] = None) -> bool:
+            max_level: Optional[int] = None
+    ) -> bool:
         """
         Add one address node as a candidate, and add its child nodes recursively.
 
         Parameters
         ----------
         seed_node: AddressNode
             A candidate address node.
@@ -443,15 +456,15 @@
                 results.append(row[0])
 
             dy *= 1.5
             dy *= 1.5
 
         return results
 
-    def searchNode(self) -> list:
+    def searchNode(self) -> List[ReverseCandidate]:
         """
         Search address nodes near the target point.
         """
         seeds = self.search_rough()
 
         for seed in seeds:
             node = self.tree.get_node_by_id(seed)
@@ -487,15 +500,15 @@
                     cand.set_dist(dist)
 
                 results.append(cand)
 
         results.sort(key=lambda cand: cand.get_dist())
         return results[0:3]
 
-    def search(self) -> list:
+    def search(self) -> List[ReverseCandidate]:
         """
         Search address nodes near the target point,
         and return as dict representations.
         """
         candidates = self.searchNode()
         results = []
         for cand in candidates:
```

### Comparing `jageocoder-1.4.0/jageocoder/strlib.py` & `jageocoder-1.4.1rc1/jageocoder/strlib.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/jageocoder/tree.py` & `jageocoder-1.4.1rc1/jageocoder/tree.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from collections import OrderedDict
 import csv
 from logging import getLogger
 import os
 import re
 import site
 import sys
-from typing import Any, Union, NoReturn, List, Optional, TextIO
+from typing import Any, Union, List, Optional, TextIO
 
 from deprecated import deprecated
 from sqlalchemy import Index
 from sqlalchemy.orm import sessionmaker, Session
 from sqlalchemy.orm.exc import NoResultFound
 from sqlalchemy.pool import NullPool
 from sqlalchemy import create_engine
@@ -164,16 +164,18 @@
         debug: bool, optional (default=False)
             Debugging flag. If set to True, write debugging messages.
             If omitted, refer 'JAGEOCODER_DEBUG' environment variable,
             or False if the environment variable is also undefined.
         """
         # Set default values
         self.mode = mode
+        db_dir = db_dir or get_db_dir(mode)
         if db_dir is None:
-            db_dir = get_db_dir(mode)
+            msg = "Dictionary is not installed correctly."
+            raise AddressTreeException(msg)
         else:
             db_dir = os.path.abspath(db_dir)
 
         if not os.path.isdir(db_dir):
             msg = "Directory '{}' does not exist.".format(db_dir)
             raise AddressTreeException(msg)
 
@@ -236,15 +238,15 @@
             'require_coordinates': os.environ.get(
                 'JAGEOCODER_REQUIRE_COORDINATES', True),
         })
 
         # Itaiji converter
         self.converter = Converter()
 
-    def close(self) -> NoReturn:
+    def close(self) -> None:
         if self.session:
             self.session.close()
 
         if self.engine:
             self.engine.dispose()
             del self.engine
             self.engine = None
@@ -261,25 +263,25 @@
         current_dict_ver = self.get_version()
         required_dict_ver = jageocoder.dictionary_version()
         if current_dict_ver != required_dict_ver:
             return False
 
         return True
 
-    def __not_in_readonly_mode(self) -> NoReturn:
+    def __not_in_readonly_mode(self) -> None:
         """
         Check if the dictionary is not opened in the read-only mode.
 
         If the mode is read-only, AddressTreeException will be raised.
         """
         if self.mode == 'r':
             raise AddressTreeException(
                 'This method is not available in read-only mode.')
 
-    def __create_db(self) -> NoReturn:
+    def __create_db(self) -> None:
         """
         Create database and tables.
         """
         self.__not_in_readonly_mode()
         Base.metadata.create_all(self.engine)
         root = self.get_root()
         root.save_recursive(self.session)
@@ -421,15 +423,15 @@
             Specify the areas to be searched.
             The area can be specified by the list of name of the node
             (such as prefecture name or city name), or JIS code.
         """
         for k, v in kwargs.items():
             self._set_config(k, v)
 
-    def validate_config(self, key: str, value: Any) -> NoReturn:
+    def validate_config(self, key: str, value: Any) -> None:
         """
         Validate configuration key and parameters.
 
         Parameters
         ----------
         key: str
             The name of the parameter.
@@ -862,15 +864,15 @@
         root_node = self.get_root()
         root_node.note = jageocoder.dictionary_version()
         self.session.add(root_node)
         self.session.commit()
 
         return diffs
 
-    def create_trie_index(self) -> NoReturn:
+    def create_trie_index(self) -> None:
         """
         Create the TRIE index from the tree.
         """
         self.__not_in_readonly_mode()
         self.index_table = {}
         logger.debug("Collecting labels for the trie index...")
         self._get_index_table()
@@ -878,15 +880,15 @@
 
         logger.debug("Building Trie...")
         self.trie = AddressTrie(self.trie_path, self.index_table)
         self.trie.save()
 
         self._set_index_table()
 
-    def _get_index_table(self) -> NoReturn:
+    def _get_index_table(self) -> None:
         """
         Collect the names of all address elements
         to be registered in the TRIE index.
         The collected notations will be stored in `tree.index_table`.
 
         Generates notations that describe everything from the name of
         the prefecture to the name of the oaza without abbreviation,
@@ -944,15 +946,15 @@
                 if candidate in self.index_table:
                     self.index_table[candidate].append(v.id)
                 else:
                     self.index_table[candidate] = [v.id]
 
         # self.session.commit()
 
-    def _extend_index_table(self) -> NoReturn:
+    def _extend_index_table(self) -> None:
         """
         Expand the index, including support for omission of county names.
         """
         # Build temporary lookup table
         logger.debug("Building temporary town and village table..")
         tmp_id_name_table = {}
         for node in self.session.query(
@@ -982,15 +984,15 @@
             if label_standardized in self.index_table:
                 self.index_table[label_standardized].append(v.id)
             else:
                 self.index_table[label_standardized] = [v.id]
 
         # self.session.commit()
 
-    def _set_index_table(self) -> NoReturn:
+    def _set_index_table(self) -> None:
         """
         Map all the id of the TRIE index (TRIE id) to the node id.
 
         Collect notations recursively the names of all address elements
         which was registered in the TRIE index, retrieve
         the id of each notations in the TRIE index,
         then add the TrieNode to the database that maps
@@ -1022,26 +1024,26 @@
             trienode_trie_id_index.create(self.engine)
         except OperationalError as e:
             logger.warning(e)
             logger.debug("  the index already exists. (ignored)")
 
         logger.debug("  done.")
 
-    def save_all(self) -> NoReturn:
+    def save_all(self) -> None:
         """
         Save all AddressNode in the tree to the database.
         """
         self.__not_in_readonly_mode()
         logger.debug("Starting save full tree (recursive)...")
         self.get_root().save_recursive(self.session)
         self.session.commit()
         logger.debug("Finished save tree.")
 
     def read_file(self, path: os.PathLike,
-                  do_update: bool = False) -> NoReturn:
+                  do_update: bool = False) -> None:
         """
         Add AddressNodes from a text file.
         See 'data/test.txt' for the format of the text file.
 
         Parameters
         ----------
         path : os.PathLike
@@ -1055,15 +1057,15 @@
             'This method is not available in read-only mode.')
         logger.debug("Starting read_file...")
         with open(path, 'r', encoding='utf-8',
                   errors='backslashreplace') as f:
             self.read_stream(f, do_update=do_update)
 
     def read_stream(self, fp: TextIO,
-                    do_update: bool = False) -> NoReturn:
+                    do_update: bool = False) -> None:
         """
         Add AddressNodes to the tree from a stream.
 
         Parameters
         ----------
         fp : io.TextIO
             Input text stream.
@@ -1137,26 +1139,26 @@
             for node in stocked:
                 self.session.add(node)
 
             self.session.commit()
 
         logger.debug("Done.")
 
-    def drop_indexes(self) -> NoReturn:
+    def drop_indexes(self) -> None:
         """
         Drop indexes to improve the speed of bulk insertion.
         - ix_node_parent_id ON node (parent_id)
         - ix_trienode_trie_id ON trienode (trie_id)
         """
         self.__not_in_readonly_mode()
         logger.debug("Dropping indexes...")
-        self.session.execute("DROP INDEX ix_node_parent_id")
+        self.session.execute(text("DROP INDEX ix_node_parent_id"))
         logger.debug("  done.")
 
-    def create_tree_index(self) -> NoReturn:
+    def create_tree_index(self) -> None:
         """
         Add index later that were not initially defined.
         - ix_node_parent_id ON node (parent_id)
         """
         self.__not_in_readonly_mode()
         logger.debug("Creating index on node.parent_id ...")
         node_parent_id_index = Index(
@@ -1447,45 +1449,45 @@
                 recovered = query[0:pos+1]
             elif query[-2:] in ('通り', '通リ'):
                 # '通' can be expressed as '通り'
                 recovered = query[0:pos+1]
 
         return recovered
 
-    def create_reverse_index(self) -> NoReturn:
+    def create_reverse_index(self) -> None:
         """
         Create table and index for reverse geocoding.
         """
         self.__not_in_readonly_mode()
         logger.info("Creating aza table for reverse geocoding...")
-        sql = ("DROP TABLE IF EXISTS node_aza")
+        sql = text("DROP TABLE IF EXISTS node_aza")
         self.session.execute(sql)
 
-        sql = ("CREATE TABLE node_aza AS"
-               " SELECT id, x, y, level FROM node"
-               " WHERE level IN (:oaza, :aza)")
+        sql = text("CREATE TABLE node_aza AS"
+                   " SELECT id, x, y, level FROM node"
+                   " WHERE level IN (:oaza, :aza)")
         self.session.execute(sql, {
             "oaza": AddressLevel.OAZA,
             "aza": AddressLevel.AZA,
         })
 
-        sql = ("CREATE INDEX idx_node_aza_x ON node_aza (x)")
+        sql = text("CREATE INDEX idx_node_aza_x ON node_aza (x)")
         self.session.execute(sql)
 
-        sql = ("CREATE INDEX idx_node_aza_y ON node_aza (y)")
+        sql = text("CREATE INDEX idx_node_aza_y ON node_aza (y)")
         self.session.execute(sql)
 
-    def create_note_index_table(self) -> NoReturn:
+    def create_note_index_table(self) -> None:
         """
         Collect notes from all address elements and create
         search table with index.
         """
         self.__not_in_readonly_mode()
         logger.info("Creating note-node table...")
-        sql = ("DROP TABLE IF EXISTS {}".format(NoteNode.__table__))
+        sql = text("DROP TABLE IF EXISTS {}".format(NoteNode.__table__))
         self.session.execute(sql)
         Base.metadata.create_all(
             bind=self.engine,
             tables=[NoteNode.__table__])
 
         # Create correspondence records between a note and a node id.
         for node in self.session.query(
```

### Comparing `jageocoder-1.4.0/jageocoder/trie.py` & `jageocoder-1.4.1rc1/jageocoder/trie.py`

 * *Files identical despite different names*

### Comparing `jageocoder-1.4.0/pyproject.toml` & `jageocoder-1.4.1rc1/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "jageocoder"
-version = "1.4.0"
+version = "1.4.1rc1"
 description = "A Japanese-address geocoder for Python."
 authors = ["Takeshi Sagara <sagara@info-proto.com>"]
 repository = "https://github.com/t-sagara/jageocoder/"
 license = "The MIT License"
 readme = "README.md"
 documentation = "https://jageocoder.readthedocs.io/"
 packages = [
@@ -13,14 +13,15 @@
 classifiers = [
     "Operating System :: MacOS",
     "Operating System :: Microsoft :: Windows :: Windows 11",
     "Operating System :: POSIX :: Linux",
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python :: 3",
 ]
+include = ["itaiji_dic.json"]
 
 [tool.poetry.dependencies]
 python = "^3.7"
 marisa-trie = "^0.7.8"
 SQLAlchemy = "^2.0.4"
 jaconv = "^0.3.4"
 docopt = "^0.6.2"
```

