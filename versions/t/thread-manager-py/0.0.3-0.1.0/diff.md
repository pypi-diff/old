# Comparing `tmp/thread-manager-py-0.0.3.tar.gz` & `tmp/thread-manager-py-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "thread-manager-py-0.0.3.tar", last modified: Thu Apr  6 06:21:42 2023, max compression
+gzip compressed data, was "thread-manager-py-0.1.0.tar", last modified: Fri Apr  7 07:05:10 2023, max compression
```

## Comparing `thread-manager-py-0.0.3.tar` & `thread-manager-py-0.1.0.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-06 06:21:42.493227 thread-manager-py-0.0.3/
--rw-r--r--   0 raynor     (501) staff       (20)     1072 2023-04-05 03:36:31.000000 thread-manager-py-0.0.3/LICENSE
--rw-r--r--   0 raynor     (501) staff       (20)       58 2023-04-05 05:54:07.000000 thread-manager-py-0.0.3/MANIFEST.in
--rw-r--r--   0 raynor     (501) staff       (20)     2564 2023-04-06 06:21:42.493276 thread-manager-py-0.0.3/PKG-INFO
--rw-r--r--   0 raynor     (501) staff       (20)     1921 2023-04-06 06:21:25.000000 thread-manager-py-0.0.3/README.md
--rw-r--r--   0 raynor     (501) staff       (20)        0 2023-04-05 05:38:12.000000 thread-manager-py-0.0.3/requirements.txt
--rw-r--r--   0 raynor     (501) staff       (20)       79 2023-04-06 06:21:42.493463 thread-manager-py-0.0.3/setup.cfg
--rw-r--r--   0 raynor     (501) staff       (20)      879 2023-04-06 06:21:25.000000 thread-manager-py-0.0.3/setup.py
-drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-06 06:21:42.491609 thread-manager-py-0.0.3/tests/
--rw-r--r--   0 raynor     (501) staff       (20)     2767 2023-04-06 06:21:25.000000 thread-manager-py-0.0.3/tests/test_package.py
-drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-06 06:21:42.492481 thread-manager-py-0.0.3/thread_manager/
--rw-r--r--   0 raynor     (501) staff       (20)      281 2023-04-06 06:21:25.000000 thread-manager-py-0.0.3/thread_manager/__init__.py
--rw-r--r--   0 raynor     (501) staff       (20)      490 2023-04-05 05:38:12.000000 thread-manager-py-0.0.3/thread_manager/argument.py
--rw-r--r--   0 raynor     (501) staff       (20)      252 2023-04-05 12:40:39.000000 thread-manager-py-0.0.3/thread_manager/decorator.py
--rw-r--r--   0 raynor     (501) staff       (20)     3316 2023-04-06 06:21:25.000000 thread-manager-py-0.0.3/thread_manager/manager.py
-drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-06 06:21:42.493118 thread-manager-py-0.0.3/thread_manager_py.egg-info/
--rw-r--r--   0 raynor     (501) staff       (20)     2564 2023-04-06 06:21:42.000000 thread-manager-py-0.0.3/thread_manager_py.egg-info/PKG-INFO
--rw-r--r--   0 raynor     (501) staff       (20)      399 2023-04-06 06:21:42.000000 thread-manager-py-0.0.3/thread_manager_py.egg-info/SOURCES.txt
--rw-r--r--   0 raynor     (501) staff       (20)        1 2023-04-06 06:21:42.000000 thread-manager-py-0.0.3/thread_manager_py.egg-info/dependency_links.txt
--rw-r--r--   0 raynor     (501) staff       (20)        1 2023-04-06 06:21:42.000000 thread-manager-py-0.0.3/thread_manager_py.egg-info/not-zip-safe
--rw-r--r--   0 raynor     (501) staff       (20)       15 2023-04-06 06:21:42.000000 thread-manager-py-0.0.3/thread_manager_py.egg-info/top_level.txt
+drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-07 07:05:10.744873 thread-manager-py-0.1.0/
+-rw-r--r--   0 raynor     (501) staff       (20)     1072 2023-04-05 03:36:31.000000 thread-manager-py-0.1.0/LICENSE
+-rw-r--r--   0 raynor     (501) staff       (20)       58 2023-04-05 05:54:07.000000 thread-manager-py-0.1.0/MANIFEST.in
+-rw-r--r--   0 raynor     (501) staff       (20)     2564 2023-04-07 07:05:10.744940 thread-manager-py-0.1.0/PKG-INFO
+-rw-r--r--   0 raynor     (501) staff       (20)     1921 2023-04-06 06:21:25.000000 thread-manager-py-0.1.0/README.md
+-rw-r--r--   0 raynor     (501) staff       (20)        0 2023-04-05 05:38:12.000000 thread-manager-py-0.1.0/requirements.txt
+-rw-r--r--   0 raynor     (501) staff       (20)       79 2023-04-07 07:05:10.745111 thread-manager-py-0.1.0/setup.cfg
+-rw-r--r--   0 raynor     (501) staff       (20)      879 2023-04-07 07:05:05.000000 thread-manager-py-0.1.0/setup.py
+drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-07 07:05:10.743401 thread-manager-py-0.1.0/tests/
+-rw-r--r--   0 raynor     (501) staff       (20)     3827 2023-04-07 07:04:40.000000 thread-manager-py-0.1.0/tests/test_package.py
+drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-07 07:05:10.744182 thread-manager-py-0.1.0/thread_manager/
+-rw-r--r--   0 raynor     (501) staff       (20)      281 2023-04-06 06:21:25.000000 thread-manager-py-0.1.0/thread_manager/__init__.py
+-rw-r--r--   0 raynor     (501) staff       (20)      497 2023-04-07 07:04:40.000000 thread-manager-py-0.1.0/thread_manager/argument.py
+-rw-r--r--   0 raynor     (501) staff       (20)      252 2023-04-05 12:40:39.000000 thread-manager-py-0.1.0/thread_manager/decorator.py
+-rw-r--r--   0 raynor     (501) staff       (20)     3474 2023-04-07 07:04:40.000000 thread-manager-py-0.1.0/thread_manager/manager.py
+drwxr-xr-x   0 raynor     (501) staff       (20)        0 2023-04-07 07:05:10.744761 thread-manager-py-0.1.0/thread_manager_py.egg-info/
+-rw-r--r--   0 raynor     (501) staff       (20)     2564 2023-04-07 07:05:10.000000 thread-manager-py-0.1.0/thread_manager_py.egg-info/PKG-INFO
+-rw-r--r--   0 raynor     (501) staff       (20)      399 2023-04-07 07:05:10.000000 thread-manager-py-0.1.0/thread_manager_py.egg-info/SOURCES.txt
+-rw-r--r--   0 raynor     (501) staff       (20)        1 2023-04-07 07:05:10.000000 thread-manager-py-0.1.0/thread_manager_py.egg-info/dependency_links.txt
+-rw-r--r--   0 raynor     (501) staff       (20)        1 2023-04-07 07:05:10.000000 thread-manager-py-0.1.0/thread_manager_py.egg-info/not-zip-safe
+-rw-r--r--   0 raynor     (501) staff       (20)       15 2023-04-07 07:05:10.000000 thread-manager-py-0.1.0/thread_manager_py.egg-info/top_level.txt
```

### Comparing `thread-manager-py-0.0.3/LICENSE` & `thread-manager-py-0.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `thread-manager-py-0.0.3/PKG-INFO` & `thread-manager-py-0.1.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: thread-manager-py
-Version: 0.0.3
+Version: 0.1.0
 Summary: Python Thread Manager
 Home-page: https://github.com/sanggi-wjg/py-thread-manager
 Author: SangGi
 Author-email: girr311@naver.com
 Project-URL: Bug Tracker, https://github.com/sanggi-wjg/py-thread-manager/issues
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `thread-manager-py-0.0.3/README.md` & `thread-manager-py-0.1.0/README.md`

 * *Files identical despite different names*

### Comparing `thread-manager-py-0.0.3/setup.py` & `thread-manager-py-0.1.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name='thread-manager-py',
-    version='0.0.3',
+    version='0.1.0',
     url='https://github.com/sanggi-wjg/py-thread-manager',
     author='SangGi',
     author_email='girr311@naver.com',
     description='Python Thread Manager',
     packages=find_packages(exclude=['tests']),
     long_description=open('README.md').read(),
     long_description_content_type='text/markdown',
```

### Comparing `thread-manager-py-0.0.3/tests/test_package.py` & `thread-manager-py-0.1.0/tests/test_package.py`

 * *Files 22% similar despite different names*

```diff
@@ -10,21 +10,23 @@
     def test_print_something(self):
         # given function
         def print_something(name: str, number: int):
             print(name, number)
 
         # given
         thread_arguments = [
-            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}", x), kwargs={}, )
+            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}", x))
             for x in range(1, 23)
         ]
         # when
         thread_manager = ThreadManager(print_something, thread_arguments)
         thread_manager.set_concurrency(15)
         thread_manager.run()
+        # then
+        assert not thread_manager.has_error()
 
     def test_request_get(self):
         # given function
         def request_something(*args, **kwargs):
             response = requests.get(kwargs.get("request_url"))
             print(args, response.status_code)
 
@@ -32,54 +34,83 @@
         thread_arguments = [
             ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",), kwargs={"request_url": "https://www.naver.com"})
             for x in range(1, 23)
         ]
         # when
         thread_manager = ThreadManager(request_something, thread_arguments)
         thread_manager.run()
+        # then
+        assert not thread_manager.has_error()
 
     def test_default_exception_hook(self):
         # given function
         def func_something(*args):
-            raise Exception("test error")
+            raise Exception("test_default_exception_hook")
+
+        # given
+        thread_arguments = [
+            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",))
+            for x in range(1, 23)
+        ]
+        # when
+        thread_manager = ThreadManager(func_something, thread_arguments)
+        thread_manager.run()
+        # then
+        errors = thread_manager.get_errors()
+        for e in errors:
+            print(e)
+        assert thread_manager.get_errors()
+        assert thread_manager.has_error()
+        assert thread_manager.get_error_count() == 22, f"Errors Length: {len(errors)}"
+
+    def test_default_exception_hook_2(self):
+        # given function
+        def func_something(*args):
+            raise Exception("test_default_exception_hook_2")
 
         # given
         thread_arguments = [
-            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",), kwargs={})
+            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",))
             for x in range(1, 23)
         ]
         # when
         thread_manager = ThreadManager(func_something, thread_arguments)
         thread_manager.run()
         # then
-        error_queue = thread_manager.get_error_queue()
-        print(error_queue)
-        assert len(error_queue) == 22, f"errors length: {len(error_queue)}"
+        errors = thread_manager.get_errors()
+        for e in errors:
+            print(e)
+        assert thread_manager.get_errors()
+        assert thread_manager.has_error()
+        assert thread_manager.get_error_count() == 22, f"Errors Length: {len(errors)}"
 
     def test_custom_exception_hook(self):
         # given function
         def func_something(*args):
             raise Exception("test error")
 
-        errors = []
+        custom_errors = []
 
         def func_exception_hook(*args):
-            errors.append(args)
+            custom_errors.append(args)
 
         # given
         thread_arguments = [
-            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",), kwargs={})
+            ThreadArgument(thread_name=f"[THREAD-{x}]", args=(f"Thread-{x}",))
             for x in range(1, 23)
         ]
         # when
         thread_manager = ThreadManager(func_something, thread_arguments, except_hook=func_exception_hook)
         thread_manager.run()
         # then
-        print(errors)
-        assert len(errors) == 22, f"errors length: {len(errors)}"
+        for e in custom_errors:
+            print(e)
+        assert len(custom_errors) == 22, f"Errors Length: {len(custom_errors)}"
+        # then
+        assert not thread_manager.has_error()
 
     def test_using_thread_decorator(self):
         # given
         @using_thread
         def print_something(number, **kwargs):
             print(number, kwargs)
```

### Comparing `thread-manager-py-0.0.3/thread_manager/manager.py` & `thread-manager-py-0.1.0/thread_manager/manager.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,45 +1,52 @@
 import collections
 import threading
 from threading import Thread, RLock
 from typing import List, Callable
 
 from .argument import ThreadArgument
 
-_thread_error_queue = collections.deque()
-
-
-def default_thread_exception_hook(*args):
-    _thread_error_queue.append(*args)
-
 
 class ThreadManager:
-    default_thead_manager_concurrency = 10
+    default_concurrency = 10
 
-    def __init__(self, callable_func: Callable, thread_arguments: List[ThreadArgument], except_hook: Callable = default_thread_exception_hook):
+    def __init__(self, callable_func: Callable, thread_arguments: List[ThreadArgument], except_hook: Callable = None):
         """
         Constructor
         :param callable_func: source function, 실행할 함수
         :type callable_func: Callable
         :param thread_arguments: thread arguments of source function, 실행할 함수의 인자
         :type thread_arguments: List[tuple]
         :param except_hook: when error occurred, run hook function, 에러시 실행할 함수의 인자
         :type except_hook: Callable
         """
         self.func: Callable = callable_func
-        self.thread_arguments: List[ThreadArgument] = thread_arguments
-        self.total_thread_arguments_count: int = len(thread_arguments)
-        self.concurrency: int = self.default_thead_manager_concurrency
+        # threads
         self.threads: List[Thread] = []
+        self.thread_arguments: List[ThreadArgument] = thread_arguments
+        self.thread_arguments_count: int = len(thread_arguments)
+        # configs
+        self.concurrency: int = self.default_concurrency
         self.is_interrupted: bool = False
         self.consumer_lock = RLock()
-        threading.excepthook = except_hook
+        # errors
+        self.error_deque = collections.deque()
+        threading.excepthook = self.add_errors if except_hook is None else except_hook
+
+    def add_errors(self, error):
+        self.error_deque.append(error)
+
+    def get_errors(self) -> collections.deque:
+        return self.error_deque.copy()
+
+    def get_error_count(self) -> int:
+        return len(self.error_deque)
 
-    def get_error_queue(self) -> collections.deque:
-        return _thread_error_queue.copy()
+    def has_error(self) -> bool:
+        return len(self.error_deque) > 0
 
     def set_concurrency(self, number: int):
         """
         동시 실행 수 설정
         :param number: number of concurrency, 동시 실행 수
         :type number: int
         """
@@ -77,17 +84,17 @@
                 for th in self.threads:
                     th.join()
                 del self.threads
 
     def run(self):
         start_index = 0
         while True:
-            is_exceed_index = start_index >= self.total_thread_arguments_count
+            is_exceed_index = start_index >= self.thread_arguments_count
             if self.is_interrupted or is_exceed_index:
                 return
             # 만약 end_index 가 총 실행 크기 보다 크다면 end_index 를 실행 크기로 맞추어 IndexError 방지
             end_index = start_index + self.concurrency
-            if end_index > self.total_thread_arguments_count:
-                end_index = self.total_thread_arguments_count
+            if end_index > self.thread_arguments_count:
+                end_index = self.thread_arguments_count
 
             self.start_thread(start_index, end_index)
             start_index += self.concurrency
```

### Comparing `thread-manager-py-0.0.3/thread_manager_py.egg-info/PKG-INFO` & `thread-manager-py-0.1.0/thread_manager_py.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: thread-manager-py
-Version: 0.0.3
+Version: 0.1.0
 Summary: Python Thread Manager
 Home-page: https://github.com/sanggi-wjg/py-thread-manager
 Author: SangGi
 Author-email: girr311@naver.com
 Project-URL: Bug Tracker, https://github.com/sanggi-wjg/py-thread-manager/issues
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: MIT License
```

