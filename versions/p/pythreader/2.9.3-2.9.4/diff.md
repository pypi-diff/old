# Comparing `tmp/pythreader-2.9.3.tar.gz` & `tmp/pythreader-2.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pythreader-2.9.3.tar", last modified: Thu Feb  2 21:03:34 2023, max compression
+gzip compressed data, was "pythreader-2.9.4.tar", last modified: Fri Feb  3 18:34:27 2023, max compression
```

## Comparing `pythreader-2.9.3.tar` & `pythreader-2.9.4.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-02 21:03:34.323579 pythreader-2.9.3/
--rwxr-xr-x   0 ivm        (501) staff       (20)     1507 2019-11-05 15:22:43.000000 pythreader-2.9.3/LICENSE
--rw-r--r--   0 ivm        (501) staff       (20)      883 2023-02-02 21:03:34.323728 pythreader-2.9.3/PKG-INFO
--rwxr-xr-x   0 ivm        (501) staff       (20)     5239 2023-01-05 17:48:21.000000 pythreader-2.9.3/README.md
-drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-02 21:03:34.315995 pythreader-2.9.3/pythreader/
--rwxr-xr-x   0 ivm        (501) staff       (20)     5057 2022-06-29 16:10:23.000000 pythreader-2.9.3/pythreader/LogFile.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     3675 2022-02-02 13:50:38.000000 pythreader-2.9.3/pythreader/RWLock.py
--rwxr-xr-x   0 ivm        (501) staff       (20)    10532 2023-02-02 16:32:12.000000 pythreader-2.9.3/pythreader/Scheduler.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     3191 2022-06-29 16:10:23.000000 pythreader-2.9.3/pythreader/Subprocess.py
--rwxr-xr-x   0 ivm        (501) staff       (20)       65 2023-02-02 21:03:15.000000 pythreader-2.9.3/pythreader/Version.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      904 2023-01-08 16:00:27.000000 pythreader-2.9.3/pythreader/__init__.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      652 2022-02-02 13:50:38.000000 pythreader-2.9.3/pythreader/barrier.py
--rwxr-xr-x   0 ivm        (501) staff       (20)    11533 2023-02-02 21:02:55.000000 pythreader-2.9.3/pythreader/core.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     3532 2023-01-05 17:48:21.000000 pythreader-2.9.3/pythreader/dequeue.py
--rw-r--r--   0 ivm        (501) staff       (20)     2196 2022-08-25 15:09:02.000000 pythreader-2.9.3/pythreader/escrow.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      764 2023-01-05 17:48:21.000000 pythreader-2.9.3/pythreader/flag.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     1514 2022-02-02 13:50:38.000000 pythreader-2.9.3/pythreader/gate.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     4524 2023-01-05 17:48:21.000000 pythreader-2.9.3/pythreader/processor.py
--rw-r--r--   0 ivm        (501) staff       (20)      558 2022-02-02 13:50:38.000000 pythreader-2.9.3/pythreader/producer.py
--rwxr-xr-x   0 ivm        (501) staff       (20)    11756 2023-01-14 13:38:54.000000 pythreader-2.9.3/pythreader/promise.py
--rw-r--r--   0 ivm        (501) staff       (20)    15871 2023-02-02 21:02:32.000000 pythreader-2.9.3/pythreader/task_queue.py
-drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-02 21:03:34.317895 pythreader-2.9.3/pythreader.egg-info/
--rwxr-xr-x   0 ivm        (501) staff       (20)      883 2023-02-02 21:03:33.000000 pythreader-2.9.3/pythreader.egg-info/PKG-INFO
--rwxr-xr-x   0 ivm        (501) staff       (20)      759 2023-02-02 21:03:34.000000 pythreader-2.9.3/pythreader.egg-info/SOURCES.txt
--rwxr-xr-x   0 ivm        (501) staff       (20)        1 2023-02-02 21:03:33.000000 pythreader-2.9.3/pythreader.egg-info/dependency_links.txt
--rw-r--r--   0 ivm        (501) staff       (20)        1 2022-08-11 16:38:20.000000 pythreader-2.9.3/pythreader.egg-info/not-zip-safe
--rwxr-xr-x   0 ivm        (501) staff       (20)       17 2023-02-02 21:03:34.000000 pythreader-2.9.3/pythreader.egg-info/top_level.txt
--rwxr-xr-x   0 ivm        (501) staff       (20)       79 2023-02-02 21:03:34.324277 pythreader-2.9.3/setup.cfg
--rwxr-xr-x   0 ivm        (501) staff       (20)     1502 2022-08-11 16:38:17.000000 pythreader-2.9.3/setup.py
-drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-02 21:03:34.322931 pythreader-2.9.3/tests/
--rwxr-xr-x   0 ivm        (501) staff       (20)      575 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/chained_processors.py
--rw-r--r--   0 ivm        (501) staff       (20)     1262 2023-01-05 17:48:21.000000 pythreader-2.9.3/tests/processor.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      314 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/processor_async.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      597 2023-01-05 17:48:21.000000 pythreader-2.9.3/tests/processors.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     1326 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/rwlock.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      692 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/scheduler.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      836 2023-01-05 17:48:21.000000 pythreader-2.9.3/tests/task_queue.py
--rwxr-xr-x   0 ivm        (501) staff       (20)      618 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/task_queue_stagger.py
--rwxr-xr-x   0 ivm        (501) staff       (20)     1055 2022-02-02 13:50:38.000000 pythreader-2.9.3/tests/tasks_exceptions.py
+drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-03 18:34:27.815656 pythreader-2.9.4/
+-rwxr-xr-x   0 ivm        (501) staff       (20)     1507 2019-11-05 15:22:43.000000 pythreader-2.9.4/LICENSE
+-rw-r--r--   0 ivm        (501) staff       (20)      883 2023-02-03 18:34:27.815751 pythreader-2.9.4/PKG-INFO
+-rwxr-xr-x   0 ivm        (501) staff       (20)     5239 2023-01-05 17:48:21.000000 pythreader-2.9.4/README.md
+drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-03 18:34:27.811225 pythreader-2.9.4/pythreader/
+-rwxr-xr-x   0 ivm        (501) staff       (20)     5057 2022-06-29 16:10:23.000000 pythreader-2.9.4/pythreader/LogFile.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     3675 2022-02-02 13:50:38.000000 pythreader-2.9.4/pythreader/RWLock.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)    11008 2023-02-03 18:18:20.000000 pythreader-2.9.4/pythreader/Scheduler.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     3191 2022-06-29 16:10:23.000000 pythreader-2.9.4/pythreader/Subprocess.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)       65 2023-02-03 18:32:54.000000 pythreader-2.9.4/pythreader/Version.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      970 2023-02-03 15:34:42.000000 pythreader-2.9.4/pythreader/__init__.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      652 2022-02-02 13:50:38.000000 pythreader-2.9.4/pythreader/barrier.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)    11965 2023-02-03 18:33:44.000000 pythreader-2.9.4/pythreader/core.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     3532 2023-01-05 17:48:21.000000 pythreader-2.9.4/pythreader/dequeue.py
+-rw-r--r--   0 ivm        (501) staff       (20)     2196 2022-08-25 15:09:02.000000 pythreader-2.9.4/pythreader/escrow.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      764 2023-01-05 17:48:21.000000 pythreader-2.9.4/pythreader/flag.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     1514 2022-02-02 13:50:38.000000 pythreader-2.9.4/pythreader/gate.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     4524 2023-01-05 17:48:21.000000 pythreader-2.9.4/pythreader/processor.py
+-rw-r--r--   0 ivm        (501) staff       (20)      558 2022-02-02 13:50:38.000000 pythreader-2.9.4/pythreader/producer.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)    11756 2023-01-14 13:38:54.000000 pythreader-2.9.4/pythreader/promise.py
+-rw-r--r--   0 ivm        (501) staff       (20)    15871 2023-02-02 21:02:32.000000 pythreader-2.9.4/pythreader/task_queue.py
+drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-03 18:34:27.812351 pythreader-2.9.4/pythreader.egg-info/
+-rwxr-xr-x   0 ivm        (501) staff       (20)      883 2023-02-03 18:34:27.000000 pythreader-2.9.4/pythreader.egg-info/PKG-INFO
+-rwxr-xr-x   0 ivm        (501) staff       (20)      759 2023-02-03 18:34:27.000000 pythreader-2.9.4/pythreader.egg-info/SOURCES.txt
+-rwxr-xr-x   0 ivm        (501) staff       (20)        1 2023-02-03 18:34:27.000000 pythreader-2.9.4/pythreader.egg-info/dependency_links.txt
+-rw-r--r--   0 ivm        (501) staff       (20)        1 2022-08-11 16:38:20.000000 pythreader-2.9.4/pythreader.egg-info/not-zip-safe
+-rwxr-xr-x   0 ivm        (501) staff       (20)       17 2023-02-03 18:34:27.000000 pythreader-2.9.4/pythreader.egg-info/top_level.txt
+-rwxr-xr-x   0 ivm        (501) staff       (20)       79 2023-02-03 18:34:27.816069 pythreader-2.9.4/setup.cfg
+-rwxr-xr-x   0 ivm        (501) staff       (20)     1502 2022-08-11 16:38:17.000000 pythreader-2.9.4/setup.py
+drwxr-xr-x   0 ivm        (501) staff       (20)        0 2023-02-03 18:34:27.815399 pythreader-2.9.4/tests/
+-rwxr-xr-x   0 ivm        (501) staff       (20)      575 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/chained_processors.py
+-rw-r--r--   0 ivm        (501) staff       (20)     1262 2023-01-05 17:48:21.000000 pythreader-2.9.4/tests/processor.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      314 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/processor_async.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      597 2023-01-05 17:48:21.000000 pythreader-2.9.4/tests/processors.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     1326 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/rwlock.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      692 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/scheduler.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      836 2023-01-05 17:48:21.000000 pythreader-2.9.4/tests/task_queue.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)      618 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/task_queue_stagger.py
+-rwxr-xr-x   0 ivm        (501) staff       (20)     1055 2022-02-02 13:50:38.000000 pythreader-2.9.4/tests/tasks_exceptions.py
```

### Comparing `pythreader-2.9.3/LICENSE` & `pythreader-2.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/PKG-INFO` & `pythreader-2.9.4/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pythreader
-Version: 2.9.3
+Version: 2.9.4
 Summary: A set of useful tools built on top of standard Python threading module
 Home-page: https://github.com/imandr/pythreader
 Author: Igor Mandrichenko
 Author-email: igorvm@gmail.com
 License: BSD 3-clause
 Keywords: threading,synchronization,multiprocessing,parallel computing
 Platform: UNKNOWN
```

### Comparing `pythreader-2.9.3/README.md` & `pythreader-2.9.4/README.md`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/LogFile.py` & `pythreader-2.9.4/pythreader/LogFile.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/RWLock.py` & `pythreader-2.9.4/pythreader/RWLock.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/Scheduler.py` & `pythreader-2.9.4/pythreader/Scheduler.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from .core import PyThread, synchronized, Primitive
+from .core import PyThread, synchronized, Primitive, Timeout
 from .task_queue import Task, TaskQueue
 from .promise import Promise
 import time, uuid, traceback, random
 import sys
 
 class Job(object):
     
@@ -168,25 +168,25 @@
         #   next_t = fcn(**args)
         # 
         #   next_t:
         #       "stop" - remove task
         #       int or float - next time to run
         #       None - run at now+interval next time
         #
-        if t is None: t = t0            # alias, t0 is deprecated
+        if t is None: t = t0            # alias, t0 argument is deprecated
         if param is not None:       # for backward compatibility
             params = (param,)
         if id is None:
             id = uuid.uuid4().hex[:8]
-        if t0 is None:
-            t0 = time.time() + (interval or 0.0) + random.random()*jitter
-        elif t0 < 10*365*24*3600:           # ~ Jan 1 1980
-            t0 = time.time() + t0
-        job = Job(self, id, t0, interval, jitter, fcn, count, params, args)
-        return self.add_job(job, t0)
+        if t is None:
+            t = time.time() + (interval or 0.0) + random.random()*jitter
+        elif t < 10*365*24*3600:           # ~ Jan 1 1980
+            t = time.time() + t
+        job = Job(self, id, t, interval, jitter, fcn, count, params, args)
+        return self.add_job(job, t)
         
     @synchronized
     def remove(self, job_or_id):
         """Removes the job from the schedule. Will not stop the job if it is already running.
         
         Args:
             job_or_id: Either the Job object returned by the ``add`` method, or job id (str)
@@ -211,50 +211,67 @@
 
     @synchronized
     def is_empty(self):
         """Returns True if there are no pending jobs on the schedule. Note that if a repeating job is currently running, it will not
         be on the schedule until it completes or fails.
         """
         return not self.Timeline
+        
+    
+    @synchronized
+    def _next_run(self):
+        # returns run time of first job to run
+        if self.Timeline:
+            return min(j.NextT for j in self.Timeline)
+        else:
+            return None
+
+    @synchronized
+    def _job_is_ready(self):
+        return any(j.NextT <= time.time() for j in self.Timeline)
 
     def run(self):
         while not self.Stop and not (self.is_empty() and self.StopWhenEmpty):
-            delta = 100
-            if self.Timeline:
-                next_t = self.run_jobs()
-                if next_t is not None:
-                    delta = next_t - time.time()
-            if delta > 0:
+            with self:
+                delta = 100
+                if self.Timeline:
+                    next_t = self.run_jobs()
+                    if next_t is not None:
+                        delta = next_t - time.time()
                 self.sleep(delta)
-                
 
     @synchronized        
     def wait_until_empty(self):
         """Wait until the schedule is empty. Note that if a repeating job is currently running, it will not
         be on the schedule until it completes or fails.
         """
         while not self.is_empty():
             self.sleep(10)
     
     join = wait_until_empty
 
 _GLobalSchedulerLock = Primitive()
 _GlobalScheduler = None
 
-def init_global_scheduler(name="GlobalScheduler", **args):
+def global_scheduler(name="GlobalScheduler", **args):
     global _GlobalScheduler
     if _GlobalScheduler is None:
         with _GLobalSchedulerLock:
             if _GlobalScheduler is None:
                 _GlobalScheduler = Scheduler(name=name, **args)
+    return _GlobalScheduler
 
 def schedule_job(fcn, *params, **args):
-    global _GlobalScheduler
-    init_global_scheduler()         # init if needed
-    return _GlobalScheduler.add(fcn, *params, **args)
+    return global_scheduler().add(fcn, *params, **args)
+
+def unschedule_job(job_or_id):
+    return global_scheduler().remove(job_or_id)
+
+schedule_task = schedule_job        # aliases, deprecating term "job"
+unschedule_task = unschedule_job
 
 if __name__ == "__main__":
     from datetime import datetime
     
     s = Scheduler()
     
     class NTimes(object):
```

### Comparing `pythreader-2.9.3/pythreader/Subprocess.py` & `pythreader-2.9.4/pythreader/Subprocess.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/__init__.py` & `pythreader-2.9.4/pythreader/__init__.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from .core import Primitive, synchronized, PyThread, gated, Timeout, Timer
 from .dequeue import DEQueue
 from .task_queue import TaskQueue, Task
-from .Scheduler import Scheduler, schedule_job
+from .Scheduler import Scheduler, schedule_job, schedule_task, unschedule_job, unschedule_task, global_scheduler
 from .Subprocess import Subprocess, ShellCommand
 from .RWLock import RWLock
 from .Version import Version
 from .promise import Promise
 from .processor import Processor
 from .flag import Flag
 from .gate import Gate
```

### Comparing `pythreader-2.9.3/pythreader/barrier.py` & `pythreader-2.9.4/pythreader/barrier.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/core.py` & `pythreader-2.9.4/pythreader/core.py`

 * *Files 4% similar despite different names*

```diff
@@ -130,35 +130,39 @@
                 # continue doing something while the primitive is locked again
         """
         return UnlockContext(self)
 
     @synchronized
     def sleep(self, timeout = None, function=None, arguments=()):
         """
-        Blocks until wakep() method is called on the same primitive.
+        Blocks until wakep() method is called on the same primitive. The primitive will be unlocked for the duration of the sleep() call.
+        Then the primitive will be locked again and if the function is provided, it will be called while the primitive is locked
+        and then the sleep() methot will unlock the primitive and return the result.
         
         Args:
             timeout (float or int): time-out. If timed-out, RuntimeError exception will be raised.
         """
         self._WakeUp.wait(timeout)
         if function is not None:
             result = function(*arguments)
             return result
 
     @synchronized
     def sleep_until(self, predicate, *params, timeout = None, **args):
         """
         Blocks until a condition is satisfied. The method will continue calling sleep() and when it wakes up, it will call the
         predicate function and check if the predicate is satisfied and if not go back to sleep. The predicate function is
-        expected to return True or False. Basically, sleep_until runs this loop:
+        expected to return True or False. Basically, sleep_until implements this loop inside a critical section.
+        Note that the primitive is unlocked while the sleep() is in progress.
         
-            while not timed-out:
-                primitive.sleep()
-                if predicate(*params, **args):
-                    break
+            with self:
+                while not timed-out:
+                    primitive.sleep()
+                    if predicate(*params, **args):
+                        break
 
         Args:
             predicate (function): a function returning True or False. The method will exit when the function returns True
             params: positional arguments to pass to each predicate function call
             args: keyword arguments to pass to each predicate function call
             timeout (int or float): timeout. If timed-out, RuntimeError exception will be raised
         """
```

### Comparing `pythreader-2.9.3/pythreader/dequeue.py` & `pythreader-2.9.4/pythreader/dequeue.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/escrow.py` & `pythreader-2.9.4/pythreader/escrow.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/flag.py` & `pythreader-2.9.4/pythreader/flag.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/gate.py` & `pythreader-2.9.4/pythreader/gate.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/processor.py` & `pythreader-2.9.4/pythreader/processor.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/producer.py` & `pythreader-2.9.4/pythreader/producer.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/promise.py` & `pythreader-2.9.4/pythreader/promise.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader/task_queue.py` & `pythreader-2.9.4/pythreader/task_queue.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/pythreader.egg-info/PKG-INFO` & `pythreader-2.9.4/pythreader.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pythreader
-Version: 2.9.3
+Version: 2.9.4
 Summary: A set of useful tools built on top of standard Python threading module
 Home-page: https://github.com/imandr/pythreader
 Author: Igor Mandrichenko
 Author-email: igorvm@gmail.com
 License: BSD 3-clause
 Keywords: threading,synchronization,multiprocessing,parallel computing
 Platform: UNKNOWN
```

### Comparing `pythreader-2.9.3/pythreader.egg-info/SOURCES.txt` & `pythreader-2.9.4/pythreader.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/setup.py` & `pythreader-2.9.4/setup.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/chained_processors.py` & `pythreader-2.9.4/tests/chained_processors.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/processor.py` & `pythreader-2.9.4/tests/processor.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/processors.py` & `pythreader-2.9.4/tests/processors.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/rwlock.py` & `pythreader-2.9.4/tests/rwlock.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/scheduler.py` & `pythreader-2.9.4/tests/scheduler.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/task_queue.py` & `pythreader-2.9.4/tests/task_queue.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/task_queue_stagger.py` & `pythreader-2.9.4/tests/task_queue_stagger.py`

 * *Files identical despite different names*

### Comparing `pythreader-2.9.3/tests/tasks_exceptions.py` & `pythreader-2.9.4/tests/tasks_exceptions.py`

 * *Files identical despite different names*

