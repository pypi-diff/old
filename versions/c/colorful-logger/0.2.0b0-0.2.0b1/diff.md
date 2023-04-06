# Comparing `tmp/colorful-logger-0.2.0b0.tar.gz` & `tmp/colorful-logger-0.2.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "colorful-logger-0.2.0b0.tar", last modified: Wed Mar 22 07:32:20 2023, max compression
+gzip compressed data, was "colorful-logger-0.2.0b1.tar", last modified: Thu Apr  6 09:06:55 2023, max compression
```

## Comparing `colorful-logger-0.2.0b0.tar` & `colorful-logger-0.2.0b1.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 07:32:20.130436 colorful-logger-0.2.0b0/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 07:32:20.126436 colorful-logger-0.2.0b0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 07:32:20.126436 colorful-logger-0.2.0b0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      652 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/.github/workflows/publish.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1823 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     7345 2023-03-22 07:32:20.130436 colorful-logger-0.2.0b0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     5268 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/README.zh_CN.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 07:32:20.130436 colorful-logger-0.2.0b0/colorful_logger/
--rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      664 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/consts.py
--rw-r--r--   0 runner    (1001) docker     (123)     6962 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/formatter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/handlers.py
--rw-r--r--   0 runner    (1001) docker     (123)     8584 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)       74 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)      399 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/colorful_logger/types.py
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 07:32:20.130436 colorful-logger-0.2.0b0/colorful_logger.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     7345 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-22 07:32:20.000000 colorful-logger-0.2.0b0/colorful_logger.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-03-22 07:32:08.000000 colorful-logger-0.2.0b0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-22 07:32:20.130436 colorful-logger-0.2.0b0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:06:55.258862 colorful-logger-0.2.0b1/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:06:55.254862 colorful-logger-0.2.0b1/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:06:55.254862 colorful-logger-0.2.0b1/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      652 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/.github/workflows/publish.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1823 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     7345 2023-04-06 09:06:55.258862 colorful-logger-0.2.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     5268 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/README.zh_CN.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:06:55.258862 colorful-logger-0.2.0b1/colorful_logger/
+-rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      664 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/consts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6962 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/formatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/handlers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8634 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)       74 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)      399 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/colorful_logger/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:06:55.258862 colorful-logger-0.2.0b1/colorful_logger.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     7345 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 09:06:55.000000 colorful-logger-0.2.0b1/colorful_logger.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-04-06 09:06:41.000000 colorful-logger-0.2.0b1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:06:55.258862 colorful-logger-0.2.0b1/setup.cfg
```

### Comparing `colorful-logger-0.2.0b0/.github/workflows/publish.yaml` & `colorful-logger-0.2.0b1/.github/workflows/publish.yaml`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/.gitignore` & `colorful-logger-0.2.0b1/.gitignore`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/LICENSE` & `colorful-logger-0.2.0b1/LICENSE`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/PKG-INFO` & `colorful-logger-0.2.0b1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: colorful-logger
-Version: 0.2.0b0
+Version: 0.2.0b1
 Summary: A colorful logger for python3.
 Author-email: thep0y <thepoy@163.com>
 License: MIT License
         
         Copyright (c) 2021 thep0y
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `colorful-logger-0.2.0b0/README.md` & `colorful-logger-0.2.0b1/README.md`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/README.zh_CN.md` & `colorful-logger-0.2.0b1/README.zh_CN.md`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/colorful_logger/__init__.py` & `colorful-logger-0.2.0b1/colorful_logger/__init__.py`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/colorful_logger/consts.py` & `colorful-logger-0.2.0b1/colorful_logger/consts.py`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/colorful_logger/formatter.py` & `colorful-logger-0.2.0b1/colorful_logger/formatter.py`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/colorful_logger/handlers.py` & `colorful-logger-0.2.0b1/colorful_logger/handlers.py`

 * *Files identical despite different names*

### Comparing `colorful-logger-0.2.0b0/colorful_logger/logger.py` & `colorful-logger-0.2.0b1/colorful_logger/logger.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 #!/usr/bin/env python3
 # -*- coding:utf-8 -*-
 # @Author:      thepoy
 # @Email:       thepoy@163.com
 # @File Name:   logger.py
 # @Created At:  2021-05-21 13:53:40
-# @Modified At: 2023-03-22 15:29:03
+# @Modified At: 2023-04-06 16:09:03
 # @Modified By: thepoy
 
 import os
 import sys
 import queue
 import warnings
 
 from types import TracebackType
-from typing import Any, List, NoReturn, Optional, Tuple, Union, Mapping, Type
+from typing import Any, List, NoReturn, Optional, Tuple, Union, Mapping, Type, Dict
 from logging import Logger, Handler, _srcfile, addLevelName
 from logging.handlers import QueueListener
 from colorful_logger.types import StrPath
 
 from colorful_logger.handlers import (
     ColorfulQueueHandler,
     ColorfulQueueListener,
@@ -92,15 +92,15 @@
         self,
         level: int,
         msg: str,
         exc_info: Optional[_ExcInfoType] = None,
         extra: Optional[Mapping[str, Any]] = None,
         stack_info: bool = False,
         stacklevel: int = 3,
-        **kwargs: Any,
+        kwargs: Dict[str, Any] = {},
     ):
         """
         Low-level logging routine which creates a LogRecord and then calls
         all the handlers of this logger to handle the record.
         """
         sinfo = None
         if _srcfile:
@@ -132,61 +132,61 @@
     def fatal(self, msg: str, **kwargs: Any) -> NoReturn:
         """
         Log msg and kwargs with severity 'FATAL'.
 
         logger.fatal("got student failed", err="something error", status_code=403)
         """
         if self.isEnabledFor(FATAL):
-            self._log(FATAL, msg, **kwargs)
+            self._log(FATAL, msg, kwargs=kwargs)
         sys.exit(1)
 
     def info(self, msg: str, **kwargs: Any):
         """
         Log msg and kwargs with severity 'INFO'.
 
         logger.info("got a student", id=1, name="Tommy")
         """
         if self.isEnabledFor(INFO):
-            self._log(INFO, msg, **kwargs)
+            self._log(INFO, msg, kwargs=kwargs)
 
     def debug(self, msg: str, **kwargs: Any):
         """
         Log msg and kwargs with severity 'DEBUG'.
 
         logger.debug("got a student", id=1, name="Tommy")
         """
         if self.isEnabledFor(DEBUG):
-            self._log(DEBUG, msg, **kwargs)
+            self._log(DEBUG, msg, kwargs=kwargs)
 
     def warning(self, msg: str, **kwargs: Any):
         """
         Log msg and kwargs with severity 'WARNING'.
 
         logger.warning("got a student without name", id=1)
         """
         if self.isEnabledFor(WARNING):
-            self._log(WARNING, msg, **kwargs)
+            self._log(WARNING, msg, kwargs=kwargs)
 
     def error(self, msg: str, **kwargs: Any):
         """
         Log msg and kwargs with severity 'ERROR'.
 
         logger.error("got student failed", err="something error", status_code=403)
         """
         if self.isEnabledFor(ERROR):
-            self._log(ERROR, msg, **kwargs)
+            self._log(ERROR, msg, kwargs=kwargs)
 
     def trace(self, msg: str, **kwargs: Any):
         """
         Log msg and kwargs with severity 'TRACE'.
 
         logger.trace("got a student", id=1, name="Tommy")
         """
         if self.isEnabledFor(TRACE):
-            self._log(TRACE, msg, **kwargs)
+            self._log(TRACE, msg, kwargs=kwargs)
 
     def __enter__(self):
         if hasattr(self, "listener"):
             self.listener.start()
         else:
             warnings.warn(
                 "do not use the with statement when using synchronous mode",
```

### Comparing `colorful-logger-0.2.0b0/colorful_logger.egg-info/PKG-INFO` & `colorful-logger-0.2.0b1/colorful_logger.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: colorful-logger
-Version: 0.2.0b0
+Version: 0.2.0b1
 Summary: A colorful logger for python3.
 Author-email: thep0y <thepoy@163.com>
 License: MIT License
         
         Copyright (c) 2021 thep0y
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `colorful-logger-0.2.0b0/pyproject.toml` & `colorful-logger-0.2.0b1/pyproject.toml`

 * *Files identical despite different names*

