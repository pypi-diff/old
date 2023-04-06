# Comparing `tmp/mplite-1.2.1-py3-none-any.whl.zip` & `tmp/mplite-1.2.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,11 +1,11 @@
-Zip file size: 12679 bytes, number of entries: 9
--rw-r--r--  2.0 unx     5120 b- defN 22-Nov-23 12:01 mplite/__init__.py
--rw-r--r--  2.0 unx     1069 b- defN 22-Nov-23 12:01 mplite-1.2.1.data/data/LICENSE
--rw-r--r--  2.0 unx    14039 b- defN 22-Nov-23 12:01 mplite-1.2.1.data/data/README.md
--rw-r--r--  2.0 unx       12 b- defN 22-Nov-23 12:01 mplite-1.2.1.data/data/requirements.txt
--rw-r--r--  2.0 unx     1069 b- defN 22-Nov-23 12:01 mplite-1.2.1.dist-info/LICENSE
--rw-r--r--  2.0 unx    14803 b- defN 22-Nov-23 12:01 mplite-1.2.1.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 22-Nov-23 12:01 mplite-1.2.1.dist-info/WHEEL
--rw-r--r--  2.0 unx        7 b- defN 22-Nov-23 12:01 mplite-1.2.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      727 b- defN 22-Nov-23 12:01 mplite-1.2.1.dist-info/RECORD
-9 files, 36938 bytes uncompressed, 11427 bytes compressed:  69.1%
+Zip file size: 12871 bytes, number of entries: 9
+-rw-r--r--  2.0 unx     5739 b- defN 23-Apr-06 13:35 mplite/__init__.py
+-rw-r--r--  2.0 unx     1069 b- defN 23-Apr-06 13:35 mplite-1.2.2.data/data/LICENSE
+-rw-r--r--  2.0 unx    14039 b- defN 23-Apr-06 13:35 mplite-1.2.2.data/data/README.md
+-rw-r--r--  2.0 unx       12 b- defN 23-Apr-06 13:35 mplite-1.2.2.data/data/requirements.txt
+-rw-r--r--  2.0 unx     1069 b- defN 23-Apr-06 13:36 mplite-1.2.2.dist-info/LICENSE
+-rw-r--r--  2.0 unx    14803 b- defN 23-Apr-06 13:36 mplite-1.2.2.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-06 13:36 mplite-1.2.2.dist-info/WHEEL
+-rw-r--r--  2.0 unx        7 b- defN 23-Apr-06 13:36 mplite-1.2.2.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      727 b- defN 23-Apr-06 13:36 mplite-1.2.2.dist-info/RECORD
+9 files, 37557 bytes uncompressed, 11619 bytes compressed:  69.1%
```

## zipnote {}

```diff
@@ -1,28 +1,28 @@
 Filename: mplite/__init__.py
 Comment: 
 
-Filename: mplite-1.2.1.data/data/LICENSE
+Filename: mplite-1.2.2.data/data/LICENSE
 Comment: 
 
-Filename: mplite-1.2.1.data/data/README.md
+Filename: mplite-1.2.2.data/data/README.md
 Comment: 
 
-Filename: mplite-1.2.1.data/data/requirements.txt
+Filename: mplite-1.2.2.data/data/requirements.txt
 Comment: 
 
-Filename: mplite-1.2.1.dist-info/LICENSE
+Filename: mplite-1.2.2.dist-info/LICENSE
 Comment: 
 
-Filename: mplite-1.2.1.dist-info/METADATA
+Filename: mplite-1.2.2.dist-info/METADATA
 Comment: 
 
-Filename: mplite-1.2.1.dist-info/WHEEL
+Filename: mplite-1.2.2.dist-info/WHEEL
 Comment: 
 
-Filename: mplite-1.2.1.dist-info/top_level.txt
+Filename: mplite-1.2.2.dist-info/top_level.txt
 Comment: 
 
-Filename: mplite-1.2.1.dist-info/RECORD
+Filename: mplite-1.2.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## mplite/__init__.py

```diff
@@ -2,15 +2,15 @@
 import multiprocessing
 import traceback
 import time
 from tqdm import tqdm as _tqdm
 import queue
 
 
-major, minor, patch = 1, 2, 1
+major, minor, patch = 1, 2, 2
 __version_info__ = (major, minor, patch)
 __version__ = '.'.join(str(i) for i in __version_info__)
 
 
 class Task(object):
     def __init__(self, f, *args, **kwargs) -> None:
         if not callable(f):
@@ -18,43 +18,47 @@
         self.f = f
         if not isinstance(args, tuple):
             raise TypeError(f"{args} is not a tuple")
         self.args = args
         if not isinstance(kwargs, dict):
             raise TypeError(f"{kwargs} is not a dict")
         self.kwargs = kwargs
+
     def __str__(self) -> str:
         return f"Task(f={self.f.__name__}, *{self.args}, **{self.kwargs})"
+
     def __repr__(self) -> str:
         return f"Task(f={self.f.__name__}, *{self.args}, **{self.kwargs})"
+
     def execute(self):
         try:
-            return self.f(*self.args,**self.kwargs)
+            return self.f(*self.args, **self.kwargs)
         except Exception as e:
             f = io.StringIO()
             traceback.print_exc(limit=3, file=f)
             f.seek(0)
             error = f.read()
             f.close()
             return error
-                    
+
 
 class Worker(multiprocessing.Process):
-    def __init__(self,name,tq,rq):
+    def __init__(self, name, tq, rq):
         super().__init__(group=None, target=self.update, name=name, daemon=False)
         self.exit = multiprocessing.Event()
         self.tq = tq  # workers task queue
         self.rq = rq  # workers result queue
+
     def update(self):
         while True:
             try:
                 task = self.tq.get_nowait()
             except queue.Empty:
                 task = None
-            
+
             if task == "stop":
                 self.tq.put_nowait(task)
                 self.exit.set()
                 break
 
             elif isinstance(task, Task):
                 result = task.execute()
@@ -64,28 +68,32 @@
 
 
 class TaskManager(object):
     def __init__(self, cpu_count=None) -> None:
         self._cpus = multiprocessing.cpu_count() if cpu_count is None else cpu_count
         self.tq = multiprocessing.Queue()
         self.rq = multiprocessing.Queue()
-        self.pool = []
+        self.pool: list[Worker] = []
         self._open_tasks = 0
+
     def __enter__(self):
         self.start()
         return self
-    def __exit__(self, exc_type, exc_val, exc_tb): # signature requires these, though I don't use them.
+
+    def __exit__(self, exc_type, exc_val, exc_tb):  # signature requires these, though I don't use them.
         self.stop()  # stop the workers.
+
     def start(self):
         for i in range(self._cpus):  # create workers
             worker = Worker(name=str(i), tq=self.tq, rq=self.rq)
             self.pool.append(worker)
             worker.start()
         while not all(p.is_alive() for p in self.pool):
             time.sleep(0.01)
+
     def execute(self, tasks, tqdm=_tqdm, pbar=None):
         """
         Execute tasks using mplite
 
         REQUIRED
         --------
         tasks: list
@@ -115,33 +123,42 @@
         if pbar is None:
             """ if pbar object was not passed, create a new tqdm compatibe object """
             pbar = tqdm(total=self._open_tasks, unit='tasks')
 
         while self._open_tasks != 0:
             try:
                 task = self.rq.get_nowait()
-                self._open_tasks-=1
+                self._open_tasks -= 1
                 results.append(task)
                 pbar.update(1)
             except queue.Empty:
+                dead_processes = list(filter(lambda p: not p.is_alive() and p.exitcode != 0, self.pool))
+                if len(dead_processes) > 0:
+                    return_codes = [p.exitcode for p in dead_processes]
+                    return_codes_str = ", ".join(str(p) for p in return_codes)
+
+                    if -9 in return_codes:
+                        raise ChildProcessError(f"One or more of processes were killed, likely because system ran out of memory. Exit codes: {return_codes_str}")
+                    raise ChildProcessError(f"One or more processes exited abruptly. Exit codes: {return_codes_str}")
+
                 time.sleep(0.01)
         return results
 
     def submit(self, task):
         """ permits asynchronous submission of tasks. """
         if not isinstance(task, Task):
             raise TypeError(f"expected mplite.Task, not {type(task)}")
         self._open_tasks += 1
         self.tq.put(task)
 
     def take(self):
         """ permits asynchronous retrieval of results """
         try:
             result = self.rq.get_nowait()
-            self._open_tasks-=1
+            self._open_tasks -= 1
         except queue.Empty:
             result = None
         return result
 
     @property
     def open_tasks(self):
         return self._open_tasks
@@ -152,12 +169,7 @@
         while any(p.is_alive() for p in self.pool):
             time.sleep(0.01)
         self.pool.clear()
         while not self.tq.empty:
             _ = self.tq.get_nowait()
         while not self.rq.empty:
             _ = self.rq.get_nowait()
-
-
-
-
-
```

## Comparing `mplite-1.2.1.data/data/LICENSE` & `mplite-1.2.2.data/data/LICENSE`

 * *Files identical despite different names*

## Comparing `mplite-1.2.1.data/data/README.md` & `mplite-1.2.2.data/data/README.md`

 * *Files identical despite different names*

## Comparing `mplite-1.2.1.dist-info/LICENSE` & `mplite-1.2.2.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `mplite-1.2.1.dist-info/METADATA` & `mplite-1.2.2.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mplite
-Version: 1.2.1
+Version: 1.2.2
 Summary: A module that makes multiprocessing easy.
 Home-page: https://github.com/root-11/mplite
 Author: root-11
 License: MIT
 Keywords: multiprocessing,tasks
 Platform: any
 Classifier: Development Status :: 5 - Production/Stable
```

