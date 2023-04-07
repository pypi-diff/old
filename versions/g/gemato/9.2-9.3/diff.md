# Comparing `tmp/gemato-9.2.tar.gz` & `tmp/gemato-9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/gemato-9.2.tar", last modified: Sun Dec 10 09:39:15 2017, max compression
+gzip compressed data, was "dist/gemato-9.3.tar", last modified: Tue Jan 16 10:14:46 2018, max compression
```

## Comparing `gemato-9.2.tar` & `gemato-9.3.tar`

### file list

```diff
@@ -1,54 +1,54 @@
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      641 2017-12-10 09:39:15.000000 gemato-9.2/PKG-INFO
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     1164 2017-12-10 08:51:04.000000 gemato-9.2/setup.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      933 2017-12-03 09:09:51.000000 gemato-9.2/tox.ini
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)       55 2017-10-28 14:36:40.000000 gemato-9.2/.gitignore
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2600 2017-10-27 22:19:11.000000 gemato-9.2/README.rst
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/gemato/
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     5055 2017-12-02 17:07:18.000000 gemato-9.2/gemato/openpgp.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     4289 2017-12-02 17:07:18.000000 gemato-9.2/gemato/compression.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)        0 2017-10-22 13:23:51.000000 gemato-9.2/gemato/__init__.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    16676 2017-12-02 13:07:25.000000 gemato-9.2/gemato/manifest.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     4313 2017-12-02 17:07:18.000000 gemato-9.2/gemato/exceptions.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    49860 2017-12-03 08:28:43.000000 gemato-9.2/gemato/recursiveloader.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     6304 2017-12-02 17:07:18.000000 gemato-9.2/gemato/profile.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      856 2017-10-27 22:19:11.000000 gemato-9.2/gemato/util.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    10466 2017-11-08 09:18:22.000000 gemato-9.2/gemato/verify.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2651 2017-11-14 15:32:33.000000 gemato-9.2/gemato/find_top_level.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    14769 2017-12-02 23:57:18.000000 gemato-9.2/gemato/cli.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2026 2017-11-14 06:17:15.000000 gemato-9.2/gemato/hash.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      149 2017-12-10 08:49:47.000000 gemato-9.2/MANIFEST.in
--rw-r-----   0 mgorny    (1000) mgorny    (1000)     1300 2017-10-22 13:24:37.000000 gemato-9.2/COPYING
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/tests/
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)        0 2017-10-22 13:47:25.000000 gemato-9.2/tests/__init__.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)   107498 2017-12-02 19:40:50.000000 gemato-9.2/tests/test_recursiveloader.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    11982 2017-10-24 21:51:01.000000 gemato-9.2/tests/test_hash.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    29868 2017-10-29 15:39:50.000000 gemato-9.2/tests/test_compression.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    29123 2017-11-08 09:06:56.000000 gemato-9.2/tests/test_openpgp.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    40775 2017-11-14 15:45:49.000000 gemato-9.2/tests/test_verify.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     9957 2017-11-24 20:59:08.000000 gemato-9.2/tests/test_profile.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     9488 2017-11-14 15:32:33.000000 gemato-9.2/tests/test_find_top_level.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)    28528 2017-11-23 21:02:29.000000 gemato-9.2/tests/test_manifest.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     1181 2017-10-29 21:53:09.000000 gemato-9.2/tests/testutil.py
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2472 2017-10-24 16:34:19.000000 gemato-9.2/tests/test_util.py
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/utils/
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     2579 2017-10-30 20:48:31.000000 gemato-9.2/utils/gen-test-manifest.py
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      513 2017-10-27 22:19:11.000000 gemato-9.2/utils/gen-compression-tests.bash
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     2320 2017-11-14 18:45:17.000000 gemato-9.2/utils/fuzzy-hash-tester.py
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     3667 2017-12-02 17:07:18.000000 gemato-9.2/utils/gen_fast_manifest.py
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/utils/repo.postsync.d/
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      306 2017-12-10 08:07:34.000000 gemato-9.2/utils/repo.postsync.d/00gemato
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      584 2017-10-27 22:19:11.000000 gemato-9.2/utils/benchmark-verify.py
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      794 2017-10-27 22:19:11.000000 gemato-9.2/utils/gen-hash-tests.bash
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     4195 2017-12-02 17:07:18.000000 gemato-9.2/utils/gen_fast_metamanifest.py
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      736 2017-10-25 07:58:11.000000 gemato-9.2/utils/benchmark.py
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/bin/
--rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      367 2017-10-27 22:19:11.000000 gemato-9.2/bin/gemato
-drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      641 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/PKG-INFO
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)        1 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/dependency_links.txt
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      984 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/SOURCES.txt
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)       55 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/entry_points.txt
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)        7 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/top_level.txt
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)      197 2017-12-10 09:39:15.000000 gemato-9.2/gemato.egg-info/requires.txt
--rw-r--r--   0 mgorny    (1000) mgorny    (1000)       70 2017-12-10 09:39:15.000000 gemato-9.2/setup.cfg
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      641 2018-01-16 10:14:45.000000 gemato-9.3/PKG-INFO
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     1164 2018-01-16 10:13:45.000000 gemato-9.3/setup.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     1038 2018-01-04 14:05:10.000000 gemato-9.3/tox.ini
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)       55 2017-10-28 14:36:40.000000 gemato-9.3/.gitignore
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2600 2017-10-27 22:19:11.000000 gemato-9.3/README.rst
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/gemato/
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     5278 2018-01-03 19:11:23.000000 gemato-9.3/gemato/openpgp.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     4474 2018-01-03 19:11:31.000000 gemato-9.3/gemato/compression.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)        0 2017-10-22 13:23:51.000000 gemato-9.3/gemato/__init__.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    16676 2017-12-02 13:07:25.000000 gemato-9.3/gemato/manifest.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     4525 2018-01-04 14:29:46.000000 gemato-9.3/gemato/exceptions.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    49860 2018-01-03 19:11:23.000000 gemato-9.3/gemato/recursiveloader.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     6304 2017-12-02 17:07:18.000000 gemato-9.3/gemato/profile.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      856 2017-10-27 22:19:11.000000 gemato-9.3/gemato/util.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    10466 2017-11-08 09:18:22.000000 gemato-9.3/gemato/verify.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2651 2017-11-14 15:32:33.000000 gemato-9.3/gemato/find_top_level.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    14769 2018-01-04 14:27:37.000000 gemato-9.3/gemato/cli.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2026 2017-11-14 06:17:15.000000 gemato-9.3/gemato/hash.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      149 2018-01-03 19:11:23.000000 gemato-9.3/MANIFEST.in
+-rw-r-----   0 mgorny    (1000) mgorny    (1000)     1300 2017-10-22 13:24:37.000000 gemato-9.3/COPYING
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/tests/
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)        0 2017-10-22 13:47:25.000000 gemato-9.3/tests/__init__.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)   108779 2018-01-03 19:11:23.000000 gemato-9.3/tests/test_recursiveloader.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    11982 2017-10-24 21:51:01.000000 gemato-9.3/tests/test_hash.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    29868 2017-10-29 15:39:50.000000 gemato-9.3/tests/test_compression.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    29123 2017-11-08 09:06:56.000000 gemato-9.3/tests/test_openpgp.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    40775 2017-11-14 15:45:49.000000 gemato-9.3/tests/test_verify.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     9957 2017-11-24 20:59:08.000000 gemato-9.3/tests/test_profile.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     9488 2017-11-14 15:32:33.000000 gemato-9.3/tests/test_find_top_level.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)    28528 2017-11-23 21:02:29.000000 gemato-9.3/tests/test_manifest.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     1181 2017-10-29 21:53:09.000000 gemato-9.3/tests/testutil.py
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)     2472 2017-10-24 16:34:19.000000 gemato-9.3/tests/test_util.py
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/utils/
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     2579 2017-10-30 20:48:31.000000 gemato-9.3/utils/gen-test-manifest.py
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      513 2017-10-27 22:19:11.000000 gemato-9.3/utils/gen-compression-tests.bash
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     2320 2017-11-14 18:45:17.000000 gemato-9.3/utils/fuzzy-hash-tester.py
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     3667 2017-12-02 17:07:18.000000 gemato-9.3/utils/gen_fast_manifest.py
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/utils/repo.postsync.d/
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      306 2018-01-03 19:11:23.000000 gemato-9.3/utils/repo.postsync.d/00gemato
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      584 2017-10-27 22:19:11.000000 gemato-9.3/utils/benchmark-verify.py
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      794 2017-10-27 22:19:11.000000 gemato-9.3/utils/gen-hash-tests.bash
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)     4195 2017-12-02 17:07:18.000000 gemato-9.3/utils/gen_fast_metamanifest.py
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      736 2017-10-25 07:58:11.000000 gemato-9.3/utils/benchmark.py
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/bin/
+-rwxr-xr-x   0 mgorny    (1000) mgorny    (1000)      367 2017-10-27 22:19:11.000000 gemato-9.3/bin/gemato
+drwxr-xr-x   0 mgorny    (1000) mgorny    (1000)        0 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      641 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/PKG-INFO
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)        1 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/dependency_links.txt
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      984 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/SOURCES.txt
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)       55 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/entry_points.txt
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)        7 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/top_level.txt
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)      197 2018-01-16 10:14:45.000000 gemato-9.3/gemato.egg-info/requires.txt
+-rw-r--r--   0 mgorny    (1000) mgorny    (1000)       70 2018-01-16 10:14:45.000000 gemato-9.3/setup.cfg
```

### Comparing `gemato-9.2/PKG-INFO` & `gemato-9.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: gemato
-Version: 9.2
+Version: 9.3
 Summary: Gentoo Manifest Tool -- a stand-alone utility to verify and update Gentoo Manifest files
 Home-page: http://github.com/mgorny/gemato
 Author: Michał Górny
 Author-email: mgorny@gentoo.org
 License: BSD
 Description-Content-Type: UNKNOWN
 Description: UNKNOWN
```

### Comparing `gemato-9.2/setup.py` & `gemato-9.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 # Licensed under the terms of 2-clause BSD license
 
 from setuptools import setup
 
 
 setup(
     name='gemato',
-    version='9.2',
+    version='9.3',
     description='Gentoo Manifest Tool -- a stand-alone utility to verify and update Gentoo Manifest files',
 
     author='Michał Górny',
     author_email='mgorny@gentoo.org',
     license='BSD',
     url='http://github.com/mgorny/gemato',
```

### Comparing `gemato-9.2/tox.ini` & `gemato-9.3/tox.ini`

 * *Files 17% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [tox]
-envlist = begin,py27,py34,py35,py36,pypy,pypy3,nodeps,end
+envlist = begin,py27,py34,py35,py36,pypy,pypy3,incompatible-lzma,nodeps,end
 # we operate on sources anyway
 skipsdist = True
 
 [testenv:begin]
 deps =
 	coverage
 	pyflakes
@@ -34,15 +34,15 @@
 [testenv:py36]
 # blake2 & sha3 are built-in
 deps =
 	coverage
 
 [testenv:pypy]
 deps =
-	backports.lzma
+	backports.lzma!=0.0.9
 	bz2file
 	coverage
 	pyblake2
 	pysha3
 
 [testenv:pypy3]
 # note: pyblake2, pysha3 don't build
@@ -50,14 +50,20 @@
 	coverage
 
 [testenv:nodeps]
 basepython = python2.7
 deps =
 	coverage
 
+[testenv:incompatible-lzma]
+basepython = python2.7
+deps =
+	coverage
+	pyliblzma
+
 [testenv]
 commands = coverage run -p -m unittest discover -v
 
 [testenv:end]
 deps =
 	coverage
 	wheel
```

### Comparing `gemato-9.2/README.rst` & `gemato-9.3/README.rst`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/openpgp.py` & `gemato-9.3/gemato/openpgp.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 # gemato: OpenPGP verification support
 # vim:fileencoding=utf-8
 # (c) 2017 Michał Górny
 # Licensed under the terms of 2-clause BSD license
 
 import errno
+import os.path
 import shutil
 import subprocess
 import tempfile
 
 import gemato.exceptions
 
 
@@ -52,14 +53,21 @@
 
     __slots__ = ['_home', '_impl']
 
     def __init__(self):
         self._home = tempfile.mkdtemp()
         self._impl = None
 
+        with open(os.path.join(self._home, 'gpg-agent.conf'), 'w') as f:
+            f.write('''# autogenerated by gemato
+
+# avoid any smartcard operations, we are running in isolation
+disable-scdaemon
+''')
+
     def __enter__(self):
         return self
 
     def __exit__(self, exc_type, exc_value, exc_cb):
         if self._home is not None:
             self.close()
```

### Comparing `gemato-9.2/gemato/compression.py` & `gemato-9.3/gemato/compression.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # gemato: compressed file support
 # vim:fileencoding=utf-8
-# (c) 2017 Michał Górny
+# (c) 2017-2018 Michał Górny
 # Licensed under the terms of 2-clause BSD license
 
 import gzip
 import io
 import os.path
 import sys
 
@@ -14,17 +14,20 @@
     # older bz2 module versions do not handle multiple streams correctly
     # so use the backport instead
     try:
         import bz2file as bz2
     except ImportError:
         bz2 = None
 
-try:
+# Python 3.3+ has a built-in lzma module. Older versions may have
+# an incompatible external module of the same name, so explicitly
+# force using the backport there.
+if sys.hexversion >= 0x03030000:
     import lzma
-except ImportError:
+else:
     try:
         import backports.lzma as lzma
     except ImportError:
         lzma = None
 
 import gemato.exceptions
```

### Comparing `gemato-9.2/gemato/manifest.py` & `gemato-9.3/gemato/manifest.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/exceptions.py` & `gemato-9.3/gemato/exceptions.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,147 +1,167 @@
 # gemato: exceptions
 # vim:fileencoding=utf-8
 # (c) 2017 Michał Górny
 # Licensed under the terms of 2-clause BSD license
 
 class UnsupportedCompression(Exception):
+    __slots__ = ['suffix']
+
     def __init__(self, suffix):
-        super(UnsupportedCompression, self).__init__(
-                'Unsupported compression suffix: {}'.format(suffix))
-        self.args = (suffix,)
+        super(UnsupportedCompression, self).__init__(suffix)
+        self.suffix = suffix
+
+    def __str__(self):
+        return 'Unsupported compression suffix: {}'.format(self.suffix)
 
 
 class UnsupportedHash(Exception):
+    __slots__ = ['hash_name']
+
     def __init__(self, hash_name):
-        super(UnsupportedHash, self).__init__(
-                'Unsupported hash name: {}'.format(hash_name))
-        self.args = (hash_name,)
+        super(UnsupportedHash, self).__init__(hash_name)
+        self.hash_name = hash_name
+
+    def __str__(self):
+        return 'Unsupported hash name: {}'.format(self.hash_name)
 
 
 class ManifestSyntaxError(Exception):
     def __init__(self, message):
         super(ManifestSyntaxError, self).__init__(message)
-        self.args = (message,)
 
 
 class ManifestIncompatibleEntry(Exception):
     __slots__ = ['e1', 'e2', 'diff']
 
     def __init__(self, e1, e2, diff):
-        msg = "Incompatible Manifest entries for {}".format(e1.path)
-        for k, d1, d2 in diff:
-            msg += "\n  {}: e1: {}, e2: {}".format(k, e1, e2)
-        super(ManifestIncompatibleEntry, self).__init__(msg)
+        super(ManifestIncompatibleEntry, self).__init__(e1, e2, diff)
         self.e1 = e1
         self.e2 = e2
         self.diff = diff
-        self.args = (e1, e2, diff)
+
+    def __str__(self):
+        msg = "Incompatible Manifest entries for {}".format(self.e1.path)
+        for k, d1, d2 in self.diff:
+            msg += "\n  {}: e1: {}, e2: {}".format(k, d1, d2)
+        return msg
 
 
 class ManifestMismatch(Exception):
     """
     An exception raised for verification failure.
     """
 
     __slots__ = ['path', 'entry', 'diff']
 
     def __init__(self, path, entry, diff):
-        msg = "Manifest mismatch for {}".format(path)
-        for k, exp, got in diff:
-            msg += "\n  {}: expected: {}, have: {}".format(k, exp, got)
-        super(ManifestMismatch, self).__init__(msg)
+        super(ManifestMismatch, self).__init__(path, entry, diff)
         self.path = path
         self.entry = entry
         self.diff = diff
-        self.args = (path, entry, diff)
+
+    def __str__(self):
+        msg = "Manifest mismatch for {}".format(self.path)
+        for k, exp, got in self.diff:
+            msg += "\n  {}: expected: {}, have: {}".format(k, exp, got)
+        return msg
 
 
 class ManifestCrossDevice(Exception):
     """
     An exception caused by attempting to cross filesystem boundaries.
     """
 
     __slots__ = ['path']
 
     def __init__(self, path):
+        super(ManifestCrossDevice, self).__init__(path)
         self.path = path
-        super(ManifestCrossDevice, self).__init__(
-            "Path {} crosses filesystem boundaries, it must be IGNORE-d explicitly"
-            .format(path))
-        self.args = (path,)
+
+    def __str__(self):
+        return ("Path {} crosses filesystem boundaries, it must be IGNORE-d explicitly"
+            .format(self.path))
 
 
 class ManifestUnsignedData(Exception):
     """
     An exception caused by a Manifest file containing non-whitespace
     outside the OpenPGP-signed part.
     """
 
-    def __init__(self):
-        super(ManifestUnsignedData, self).__init__(
-                "Unsigned data found in an OpenPGP signed Manifest")
+    def __str__(self):
+        return "Unsigned data found in an OpenPGP signed Manifest"
 
 
 class OpenPGPVerificationFailure(Exception):
     """
     An exception raised when OpenPGP verification fails.
     """
 
+    __slots__ = ['output']
+
     def __init__(self, output):
-        super(OpenPGPVerificationFailure, self).__init__(
-                "OpenPGP verification failed:\n{}".format(output))
-        self.args = (output,)
+        super(OpenPGPVerificationFailure, self).__init__(output)
+        self.output = output
+
+    def __str__(self):
+        return "OpenPGP verification failed:\n{}".format(self.output)
 
 
 class OpenPGPSigningFailure(Exception):
     """
     An exception raised when OpenPGP signing fails.
     """
 
+    __slots__ = ['output']
+
     def __init__(self, output):
-        super(OpenPGPSigningFailure, self).__init__(
-                "OpenPGP signing failed:\n{}".format(output))
-        self.args = (output,)
+        super(OpenPGPSigningFailure, self).__init__(output)
+        self.output = output
+
+    def __str__(self):
+        return "OpenPGP signing failed:\n{}".format(self.output)
 
 
 class OpenPGPNoImplementation(Exception):
     """
     An exception raised when no supported OpenPGP implementation
     is available.
     """
 
-    def __init__(self):
-        super(OpenPGPNoImplementation, self).__init__(
-                "No supported OpenPGP implementation found (install gnupg)")
+    def __str__(self):
+        return "No supported OpenPGP implementation found (install gnupg)"
 
 
 class ManifestInvalidPath(Exception):
     """
     An exception raised when an invalid path tries to be added to
     Manifest.
     """
 
     __slots__ = ['path', 'detail']
 
     def __init__(self, path, detail):
+        super(ManifestInvalidPath, self).__init__(path, detail)
         self.path = path
         self.detail = detail
-        super(ManifestInvalidPath, self).__init__(
-                "Attempting to add invalid path {} to Manifest: {} must not be {}"
-                .format(path, detail[0], detail[1]))
-        self.args = (path, detail)
+
+    def __str__(self):
+        return ("Attempting to add invalid path {} to Manifest: {} must not be {}"
+                .format(self.path, self.detail[0], self.detail[1]))
 
 
 class ManifestInvalidFilename(Exception):
     """
     An exception raised when an entry for invalid filename is created.
     """
 
     __slots__ = ['filename', 'pos']
 
     def __init__(self, filename, pos):
+        super(ManifestInvalidFilename, self).__init__(filename, pos)
         self.filename = filename
         self.pos = pos
-        super(ManifestInvalidFilename, self).__init__(
-                "Attempting to add invalid filename {!r} to Manifest: disallowed character U+{:04X} at position {}"
-                .format(filename, ord(filename[pos]), pos))
-        self.args = (filename, pos)
+
+    def __str__(self):
+        return ("Attempting to add invalid filename {!r} to Manifest: disallowed character U+{:04X} at position {}"
+                .format(self.filename, ord(self.filename[self.pos]), self.pos))
```

### Comparing `gemato-9.2/gemato/recursiveloader.py` & `gemato-9.3/gemato/recursiveloader.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/profile.py` & `gemato-9.3/gemato/profile.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/util.py` & `gemato-9.3/gemato/util.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/verify.py` & `gemato-9.3/gemato/verify.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/find_top_level.py` & `gemato-9.3/gemato/find_top_level.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/cli.py` & `gemato-9.3/gemato/cli.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato/hash.py` & `gemato-9.3/gemato/hash.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/COPYING` & `gemato-9.3/COPYING`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_recursiveloader.py` & `gemato-9.3/tests/test_recursiveloader.py`

 * *Files 1% similar despite different names*

```diff
@@ -2704,7 +2704,48 @@
         m.update_entries_for_directory('')
         self.assertIsNone(m.find_path_entry('sub/test'))
         m.save_manifests()
         with io.open(os.path.join(self.dir, 'Manifest'),
                      'r', encoding='utf8') as f:
             self.assertNotEqual(f.read(), self.FILES['Manifest'])
         m.assert_directory_verifies()
+
+
+class SymlinkLoopTest(TempDirTestCase):
+    """
+    Test dealing with a directory that contains a symlink to itself.
+    """
+
+    DIRS = ['sub']
+    FILES = {
+        'Manifest': u'',
+    }
+
+    def setUp(self):
+        super(SymlinkLoopTest, self).setUp()
+        os.symlink('.', os.path.join(self.dir, 'sub/sub'))
+
+    def tearDown(self):
+        os.remove(os.path.join(self.dir, 'sub/sub'))
+        super(SymlinkLoopTest, self).tearDown()
+
+    def test_assert_directory_verifies(self):
+        m = gemato.recursiveloader.ManifestRecursiveLoader(
+            os.path.join(self.dir, 'Manifest'))
+        self.assertRaises(OSError,
+                m.assert_directory_verifies, '')
+
+    def test_cli_verifies(self):
+        self.assertRaises(OSError,
+                gemato.cli.main, ['gemato', 'verify', self.dir])
+
+    def test_update_entries_for_directory(self):
+        m = gemato.recursiveloader.ManifestRecursiveLoader(
+            os.path.join(self.dir, 'Manifest'),
+            hashes=['SHA256', 'SHA512'])
+        self.assertRaises(OSError,
+                m.update_entries_for_directory, '')
+
+    def test_cli_update(self):
+        self.assertRaises(OSError,
+                gemato.cli.main, ['gemato', 'update',
+                    '--hashes=SHA256 SHA512', self.dir])
```

### Comparing `gemato-9.2/tests/test_hash.py` & `gemato-9.3/tests/test_hash.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_compression.py` & `gemato-9.3/tests/test_compression.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_openpgp.py` & `gemato-9.3/tests/test_openpgp.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_verify.py` & `gemato-9.3/tests/test_verify.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_profile.py` & `gemato-9.3/tests/test_profile.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_find_top_level.py` & `gemato-9.3/tests/test_find_top_level.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_manifest.py` & `gemato-9.3/tests/test_manifest.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/testutil.py` & `gemato-9.3/tests/testutil.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/tests/test_util.py` & `gemato-9.3/tests/test_util.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/gen-test-manifest.py` & `gemato-9.3/utils/gen-test-manifest.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/gen-compression-tests.bash` & `gemato-9.3/utils/gen-compression-tests.bash`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/fuzzy-hash-tester.py` & `gemato-9.3/utils/fuzzy-hash-tester.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/gen_fast_manifest.py` & `gemato-9.3/utils/gen_fast_manifest.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/benchmark-verify.py` & `gemato-9.3/utils/benchmark-verify.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/gen-hash-tests.bash` & `gemato-9.3/utils/gen-hash-tests.bash`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/gen_fast_metamanifest.py` & `gemato-9.3/utils/gen_fast_metamanifest.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/utils/benchmark.py` & `gemato-9.3/utils/benchmark.py`

 * *Files identical despite different names*

### Comparing `gemato-9.2/gemato.egg-info/PKG-INFO` & `gemato-9.3/gemato.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: gemato
-Version: 9.2
+Version: 9.3
 Summary: Gentoo Manifest Tool -- a stand-alone utility to verify and update Gentoo Manifest files
 Home-page: http://github.com/mgorny/gemato
 Author: Michał Górny
 Author-email: mgorny@gentoo.org
 License: BSD
 Description-Content-Type: UNKNOWN
 Description: UNKNOWN
```

### Comparing `gemato-9.2/gemato.egg-info/SOURCES.txt` & `gemato-9.3/gemato.egg-info/SOURCES.txt`

 * *Files identical despite different names*

