# Comparing `tmp/sshfs-2023.4.0.tar.gz` & `tmp/sshfs-2023.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sshfs-2023.4.0.tar", last modified: Thu Apr  6 09:08:49 2023, max compression
+gzip compressed data, was "sshfs-2023.4.1.tar", last modified: Thu Apr  6 09:48:13 2023, max compression
```

## Comparing `sshfs-2023.4.0.tar` & `sshfs-2023.4.1.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/pre-commit.yml
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/publish.yml
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/test.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-04-06 09:08:39.000000 sshfs-2023.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:08:49.278503 sshfs-2023.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2623 2023-04-06 09:08:39.000000 sshfs-2023.4.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-06 09:08:39.000000 sshfs-2023.4.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 09:08:39.000000 sshfs-2023.4.0/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 09:08:49.278503 sshfs-2023.4.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:08:39.000000 sshfs-2023.4.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs/pools/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2472 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/hard.py
--rw-r--r--   0 runner    (1001) docker     (123)     2231 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/soft.py
--rw-r--r--   0 runner    (1001) docker     (123)     9176 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/spec.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      616 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/tests/static/
--rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/static/user.key
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/static/user.key.pub
--rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_sftp_pools.py
--rw-r--r--   0 runner    (1001) docker     (123)     8733 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_sshfs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.901432 sshfs-2023.4.1/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.893432 sshfs-2023.4.1/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.897432 sshfs-2023.4.1/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 09:48:00.000000 sshfs-2023.4.1/.github/workflows/pre-commit.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 09:48:00.000000 sshfs-2023.4.1/.github/workflows/publish.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 09:48:00.000000 sshfs-2023.4.1/.github/workflows/test.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-06 09:48:00.000000 sshfs-2023.4.1/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-06 09:48:00.000000 sshfs-2023.4.1/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-04-06 09:48:00.000000 sshfs-2023.4.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:48:13.901432 sshfs-2023.4.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2623 2023-04-06 09:48:00.000000 sshfs-2023.4.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-06 09:48:00.000000 sshfs-2023.4.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 09:48:00.000000 sshfs-2023.4.1/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 09:48:13.901432 sshfs-2023.4.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:48:00.000000 sshfs-2023.4.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.897432 sshfs-2023.4.1/sshfs/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      634 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.897432 sshfs-2023.4.1/sshfs/pools/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/pools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2472 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/pools/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/pools/hard.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2231 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/pools/soft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9271 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/spec.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-04-06 09:48:00.000000 sshfs-2023.4.1/sshfs/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.897432 sshfs-2023.4.1/sshfs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:48:13.000000 sshfs-2023.4.1/sshfs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      616 2023-04-06 09:48:13.000000 sshfs-2023.4.1/sshfs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:48:13.000000 sshfs-2023.4.1/sshfs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 09:48:13.000000 sshfs-2023.4.1/sshfs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 09:48:13.000000 sshfs-2023.4.1/sshfs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.897432 sshfs-2023.4.1/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:48:13.901432 sshfs-2023.4.1/tests/static/
+-rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-04-06 09:48:00.000000 sshfs-2023.4.1/tests/static/user.key
+-rw-r--r--   0 runner    (1001) docker     (123)      573 2023-04-06 09:48:00.000000 sshfs-2023.4.1/tests/static/user.key.pub
+-rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-04-06 09:48:00.000000 sshfs-2023.4.1/tests/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-04-06 09:48:00.000000 sshfs-2023.4.1/tests/test_sftp_pools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8733 2023-04-06 09:48:00.000000 sshfs-2023.4.1/tests/test_sshfs.py
```

### Comparing `sshfs-2023.4.0/.github/workflows/publish.yml` & `sshfs-2023.4.1/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/.github/workflows/test.yml` & `sshfs-2023.4.1/.github/workflows/test.yml`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/.gitignore` & `sshfs-2023.4.1/.gitignore`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/.pre-commit-config.yaml` & `sshfs-2023.4.1/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/LICENSE` & `sshfs-2023.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/PKG-INFO` & `sshfs-2023.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sshfs
-Version: 2023.4.0
+Version: 2023.4.1
 Summary: SSH Filesystem -- Async SSH/SFTP backend for fsspec
 License: Apache License 2.0
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `sshfs-2023.4.0/README.md` & `sshfs-2023.4.1/README.md`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/setup.cfg` & `sshfs-2023.4.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/config.py` & `sshfs-2023.4.1/sshfs/config.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/file.py` & `sshfs-2023.4.1/sshfs/file.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/pools/base.py` & `sshfs-2023.4.1/sshfs/pools/base.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/pools/hard.py` & `sshfs-2023.4.1/sshfs/pools/hard.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/pools/soft.py` & `sshfs-2023.4.1/sshfs/pools/soft.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs/spec.py` & `sshfs-2023.4.1/sshfs/spec.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 import asyncio
 import posixpath
 import shlex
 import stat
-import threading
 import weakref
 from contextlib import AsyncExitStack, suppress
 from datetime import datetime
 
 import asyncssh
 from asyncssh.sftp import SFTPOpUnsupported
 from fsspec.asyn import AsyncFileSystem, async_methods, sync, sync_wrapper
@@ -40,30 +39,32 @@
         Implementation of the SFTP/SSH protocols for the fsspec.
 
         Parameters
         ----------
         host: str
             SSH host to connect.
         **kwargs: Any
-            Any option that will be passed to either the top level `AsyncFileSystem`
-            or the `asyncssh.connect`.
+            Any option that will be passed to either the top level
+            `AsyncFileSystem` or the `asyncssh.connect`.
         pool_type: sshfs.pools.base.BaseSFTPChannelPool
             Pool manager to use (when doing concurrent operations together,
             pool managers offer the flexibility of prioritizing channels
             and deciding which to use).
         """
 
         super().__init__(self, **kwargs)
 
+        max_sessions = kwargs.pop("max_sessions", _DEFAULT_MAX_SESSIONS)
+        if max_sessions <= _SHELL_CHANNELS:
+            raise ValueError(
+                f"max_sessions must be greater than {_SHELL_CHANNELS}"
+            )
         _client_args = kwargs.copy()
         _client_args.setdefault("known_hosts", None)
 
-        max_sessions = kwargs.get("max_sessions", _DEFAULT_MAX_SESSIONS)
-        assert max_sessions > _SHELL_CHANNELS
-
         self._stack = AsyncExitStack()
         self.active_executors = 0
         self._client, self._pool = self.connect(
             host,
             pool_type,
             max_sftp_channels=max_sessions - _SHELL_CHANNELS,
             **_client_args,
```

### Comparing `sshfs-2023.4.0/sshfs/utils.py` & `sshfs-2023.4.1/sshfs/utils.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/sshfs.egg-info/PKG-INFO` & `sshfs-2023.4.1/sshfs.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sshfs
-Version: 2023.4.0
+Version: 2023.4.1
 Summary: SSH Filesystem -- Async SSH/SFTP backend for fsspec
 License: Apache License 2.0
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `sshfs-2023.4.0/sshfs.egg-info/SOURCES.txt` & `sshfs-2023.4.1/sshfs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/tests/static/user.key` & `sshfs-2023.4.1/tests/static/user.key`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/tests/static/user.key.pub` & `sshfs-2023.4.1/tests/static/user.key.pub`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/tests/test_config.py` & `sshfs-2023.4.1/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/tests/test_sftp_pools.py` & `sshfs-2023.4.1/tests/test_sftp_pools.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.4.0/tests/test_sshfs.py` & `sshfs-2023.4.1/tests/test_sshfs.py`

 * *Files identical despite different names*

