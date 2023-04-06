# Comparing `tmp/forwarderd-8.tar.gz` & `tmp/forwarderd-9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "forwarderd-8.tar", last modified: Thu Apr  6 22:09:52 2023, max compression
+gzip compressed data, was "forwarderd-9.tar", last modified: Thu Apr  6 22:27:57 2023, max compression
```

## Comparing `forwarderd-8.tar` & `forwarderd-9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 22:09:52.735497 forwarderd-8/
--rw-rw-rw-   0        0        0      568 2023-04-04 14:37:31.000000 forwarderd-8/LICENSE
--rw-rw-rw-   0        0        0     1470 2023-04-06 22:09:52.735497 forwarderd-8/PKG-INFO
--rw-rw-rw-   0        0        0      971 2023-04-04 18:10:30.000000 forwarderd-8/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 22:09:52.723496 forwarderd-8/forwarderd/
--rw-rw-rw-   0        0        0      744 2023-04-04 14:54:50.000000 forwarderd-8/forwarderd/__init__.py
--rw-rw-rw-   0        0        0     1581 2023-04-04 16:09:59.000000 forwarderd-8/forwarderd/__main__.py
--rw-rw-rw-   0        0        0     3106 2023-04-04 18:20:02.000000 forwarderd-8/forwarderd/_daemon.py
--rw-rw-rw-   0        0        0     1302 2023-04-06 22:08:15.000000 forwarderd-8/forwarderd/_shared.py
-drwxrwxrwx   0        0        0        0 2023-04-06 22:09:52.734497 forwarderd-8/forwarderd.egg-info/
--rw-rw-rw-   0        0        0     1470 2023-04-06 22:09:52.000000 forwarderd-8/forwarderd.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      291 2023-04-06 22:09:52.000000 forwarderd-8/forwarderd.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 22:09:52.000000 forwarderd-8/forwarderd.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       29 2023-04-06 22:09:52.000000 forwarderd-8/forwarderd.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-06 22:09:52.000000 forwarderd-8/forwarderd.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      691 2023-04-06 22:08:29.000000 forwarderd-8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 22:09:52.735497 forwarderd-8/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 22:27:57.443436 forwarderd-9/
+-rw-rw-rw-   0        0        0      568 2023-04-04 14:37:31.000000 forwarderd-9/LICENSE
+-rw-rw-rw-   0        0        0     1470 2023-04-06 22:27:57.442434 forwarderd-9/PKG-INFO
+-rw-rw-rw-   0        0        0      971 2023-04-04 18:10:30.000000 forwarderd-9/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 22:27:57.437434 forwarderd-9/forwarderd/
+-rw-rw-rw-   0        0        0      744 2023-04-04 14:54:50.000000 forwarderd-9/forwarderd/__init__.py
+-rw-rw-rw-   0        0        0     1624 2023-04-06 22:27:16.000000 forwarderd-9/forwarderd/__main__.py
+-rw-rw-rw-   0        0        0     3106 2023-04-04 18:20:02.000000 forwarderd-9/forwarderd/_daemon.py
+-rw-rw-rw-   0        0        0     1304 2023-04-06 22:22:21.000000 forwarderd-9/forwarderd/_shared.py
+drwxrwxrwx   0        0        0        0 2023-04-06 22:27:57.441434 forwarderd-9/forwarderd.egg-info/
+-rw-rw-rw-   0        0        0     1470 2023-04-06 22:27:57.000000 forwarderd-9/forwarderd.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      291 2023-04-06 22:27:57.000000 forwarderd-9/forwarderd.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 22:27:57.000000 forwarderd-9/forwarderd.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       29 2023-04-06 22:27:57.000000 forwarderd-9/forwarderd.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 22:27:57.000000 forwarderd-9/forwarderd.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      691 2023-04-06 22:27:47.000000 forwarderd-9/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 22:27:57.443436 forwarderd-9/setup.cfg
```

### Comparing `forwarderd-8/LICENSE` & `forwarderd-9/LICENSE`

 * *Files identical despite different names*

### Comparing `forwarderd-8/PKG-INFO` & `forwarderd-9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forwarderd
-Version: 8
+Version: 9
 Summary: SSH Forward Daemon
 Author-email: Elchin Sarkarov <elchin751@gmail.com>
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: Microsoft :: Windows
```

### Comparing `forwarderd-8/README.md` & `forwarderd-9/README.md`

 * *Files identical despite different names*

### Comparing `forwarderd-8/forwarderd/__init__.py` & `forwarderd-9/forwarderd/__init__.py`

 * *Files identical despite different names*

### Comparing `forwarderd-8/forwarderd/__main__.py` & `forwarderd-9/forwarderd/__main__.py`

 * *Files 5% similar despite different names*

```diff
@@ -23,14 +23,15 @@
     template = '\n'.join([
         '[Unit]',
         'Description=SSH port forward daemon',
         'After=network.target',
         '',
         '[Service]',
         'Type=simple',
+       f'WorkingDirectory={os.getcwd()}',
        f'ExecStart={sys.executable} -m forwarderd',
         'Restart=always',
     ])
 
     UNIT_PATH = '/etc/systemd/system/forwarderd.service'
 
     if os.path.exists(UNIT_PATH):
```

### Comparing `forwarderd-8/forwarderd/_daemon.py` & `forwarderd-9/forwarderd/_daemon.py`

 * *Files identical despite different names*

### Comparing `forwarderd-8/forwarderd/_shared.py` & `forwarderd-9/forwarderd/_shared.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 if hasattr(asyncio, 'open_unix_connection'):
     async def connect():
         return await asyncio.open_unix_connection(SOCK_PATH)
 
     async def start_server(cb):
         os.makedirs(os.path.dirname(SOCK_PATH), exist_ok=True)
         server = await asyncio.start_unix_server(cb, SOCK_PATH)
-        os.chmod(SOCK_PATH, 777)
+        os.chmod(SOCK_PATH, 0o777)
         return server
 
 else:
     async def connect():
         return await asyncio.open_connection(*IP_ADDR)
 
     async def start_server(cb):
```

### Comparing `forwarderd-8/forwarderd.egg-info/PKG-INFO` & `forwarderd-9/forwarderd.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forwarderd
-Version: 8
+Version: 9
 Summary: SSH Forward Daemon
 Author-email: Elchin Sarkarov <elchin751@gmail.com>
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: Microsoft :: Windows
```

### Comparing `forwarderd-8/pyproject.toml` & `forwarderd-9/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "forwarderd"
-version = "8"
+version = "9"
 authors = [
   { name="Elchin Sarkarov", email="elchin751@gmail.com" },
 ]
 description = "SSH Forward Daemon"
 requires-python = ">=3.7"
 classifiers = [
   "Development Status :: 4 - Beta",
```

