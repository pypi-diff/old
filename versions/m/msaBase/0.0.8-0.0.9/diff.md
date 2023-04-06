# Comparing `tmp/msaBase-0.0.8.tar.gz` & `tmp/msaBase-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "msaBase-0.0.8.tar", last modified: Thu Nov 24 10:53:30 2022, max compression
+gzip compressed data, was "msaBase-0.0.9.tar", last modified: Thu Nov 24 17:12:13 2022, max compression
```

## Comparing `msaBase-0.0.8.tar` & `msaBase-0.0.9.tar`

### file list

```diff
@@ -1,31 +1,32 @@
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 10:53:30.510191 msaBase-0.0.8/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1094 2022-11-21 07:44:37.000000 msaBase-0.0.8/LICENCE
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       58 2022-11-21 15:10:41.000000 msaBase-0.0.8/MANIFEST.in
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     4134 2022-11-24 10:53:30.510191 msaBase-0.0.8/PKG-INFO
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2689 2022-11-21 07:50:43.000000 msaBase-0.0.8/README.md
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 10:53:30.510191 msaBase-0.0.8/msaBase/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      477 2022-11-24 10:50:01.000000 msaBase-0.0.8/msaBase/__init__.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     6982 2022-11-24 10:45:11.000000 msaBase-0.0.8/msaBase/config.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    30421 2022-11-24 10:19:29.000000 msaBase-0.0.8/msaBase/configurate.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2128 2022-11-11 15:20:27.000000 msaBase-0.0.8/msaBase/errorhandling.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2171 2022-11-18 16:56:36.000000 msaBase-0.0.8/msaBase/healthcheck.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3656 2022-11-11 15:19:43.000000 msaBase-0.0.8/msaBase/logger.py
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 10:53:30.510191 msaBase-0.0.8/msaBase/models/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      217 2022-11-10 09:04:48.000000 msaBase-0.0.8/msaBase/models/__init__.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      951 2022-11-18 16:52:17.000000 msaBase-0.0.8/msaBase/models/functionality.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1182 2022-11-21 07:50:43.000000 msaBase-0.0.8/msaBase/models/middlewares.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      380 2022-11-16 08:59:39.000000 msaBase-0.0.8/msaBase/models/settings.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    10963 2022-11-16 08:59:39.000000 msaBase-0.0.8/msaBase/models/sysinfo.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3869 2022-11-21 07:41:44.000000 msaBase-0.0.8/msaBase/profiler.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1265 2022-11-22 16:56:16.000000 msaBase-0.0.8/msaBase/router.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    14384 2022-11-21 08:04:11.000000 msaBase-0.0.8/msaBase/sysinfo.py
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 10:53:30.510191 msaBase-0.0.8/msaBase.egg-info/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     4134 2022-11-24 10:53:30.000000 msaBase-0.0.8/msaBase.egg-info/PKG-INFO
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      561 2022-11-24 10:53:30.000000 msaBase-0.0.8/msaBase.egg-info/SOURCES.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-24 10:53:30.000000 msaBase-0.0.8/msaBase.egg-info/dependency_links.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      912 2022-11-24 10:53:30.000000 msaBase-0.0.8/msaBase.egg-info/requires.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        8 2022-11-24 10:53:30.000000 msaBase-0.0.8/msaBase.egg-info/top_level.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-21 08:16:24.000000 msaBase-0.0.8/msaBase.egg-info/zip-safe
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     4343 2022-11-24 10:34:03.000000 msaBase-0.0.8/requirements.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       38 2022-11-24 10:53:30.510191 msaBase-0.0.8/setup.cfg
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2319 2022-11-21 15:04:48.000000 msaBase-0.0.8/setup.py
+drwxrwxr-x   0 cornhub   (1000) cornhub   (1000)        0 2022-11-24 17:12:13.607689 msaBase-0.0.9/
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     1094 2022-11-22 10:10:58.000000 msaBase-0.0.9/LICENCE
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)       58 2022-11-22 10:10:58.000000 msaBase-0.0.9/MANIFEST.in
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     4154 2022-11-24 17:12:13.607689 msaBase-0.0.9/PKG-INFO
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     2689 2022-11-22 10:10:58.000000 msaBase-0.0.9/README.md
+drwxrwxr-x   0 cornhub   (1000) cornhub   (1000)        0 2022-11-24 17:12:13.607689 msaBase-0.0.9/msaBase/
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      477 2022-11-24 16:54:20.000000 msaBase-0.0.9/msaBase/__init__.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     6982 2022-11-24 15:50:02.000000 msaBase-0.0.9/msaBase/config.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)    31229 2022-11-24 16:53:20.000000 msaBase-0.0.9/msaBase/configurate.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     2128 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/errorhandling.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     2171 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/healthcheck.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      676 2022-11-24 17:03:51.000000 msaBase-0.0.9/msaBase/helpers.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     3656 2022-11-24 15:49:31.000000 msaBase-0.0.9/msaBase/logger.py
+drwxrwxr-x   0 cornhub   (1000) cornhub   (1000)        0 2022-11-24 17:12:13.607689 msaBase-0.0.9/msaBase/models/
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      217 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/models/__init__.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      951 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/models/functionality.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     1182 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/models/middlewares.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      380 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/models/settings.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)    10963 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/models/sysinfo.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     3869 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/profiler.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     1265 2022-11-24 15:50:02.000000 msaBase-0.0.9/msaBase/router.py
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)    14384 2022-11-22 10:10:58.000000 msaBase-0.0.9/msaBase/sysinfo.py
+drwxrwxr-x   0 cornhub   (1000) cornhub   (1000)        0 2022-11-24 17:12:13.607689 msaBase-0.0.9/msaBase.egg-info/
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     4154 2022-11-24 17:12:13.000000 msaBase-0.0.9/msaBase.egg-info/PKG-INFO
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      580 2022-11-24 17:12:13.000000 msaBase-0.0.9/msaBase.egg-info/SOURCES.txt
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)        1 2022-11-24 17:12:13.000000 msaBase-0.0.9/msaBase.egg-info/dependency_links.txt
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)      912 2022-11-24 17:12:13.000000 msaBase-0.0.9/msaBase.egg-info/requires.txt
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)        8 2022-11-24 17:12:13.000000 msaBase-0.0.9/msaBase.egg-info/top_level.txt
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)        1 2022-11-24 17:06:05.000000 msaBase-0.0.9/msaBase.egg-info/zip-safe
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     4343 2022-11-24 17:11:51.000000 msaBase-0.0.9/requirements.txt
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)       38 2022-11-24 17:12:13.607689 msaBase-0.0.9/setup.cfg
+-rw-rw-r--   0 cornhub   (1000) cornhub   (1000)     2319 2022-11-22 10:10:58.000000 msaBase-0.0.9/setup.py
```

### Comparing `msaBase-0.0.8/LICENCE` & `msaBase-0.0.9/LICENCE`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/PKG-INFO` & `msaBase-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: msaBase
-Version: 0.0.8
+Version: 0.0.9
 Summary: msaBase - General package for Microservices based on FastAPI like Profiler, Scheduler, Sysinfo, Healtcheck, Error Handling etc.
 Home-page: https://github.com/u2d-ai/msaBase
-Download-URL: http://pypi.python.org/pypi/msaBase
 Author: Stefan Welcker
 Author-email: stefan@u2d.ai
 License: MIT
+Download-URL: http://pypi.python.org/pypi/msaBase
 Project-URL: Documentation, http://msaBase.u2d.ai/
 Project-URL: Source, https://github.com/u2d-ai/msaBase
 Project-URL: Tracker, https://github.com/u2d-ai/msaBase/issues
+Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Framework :: FastAPI
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Operating System :: Microsoft :: Windows
 Classifier: Operating System :: POSIX :: Linux
@@ -92,7 +93,9 @@
 Build:  
 
     python setup.py sdist
 
 Publish to pypi:
 
     twine upload dist/*
+
+
```

#### html2text {}

```diff
@@ -1,26 +1,27 @@
-Metadata-Version: 2.1 Name: msaBase Version: 0.0.8 Summary: msaBase - General
+Metadata-Version: 2.1 Name: msaBase Version: 0.0.9 Summary: msaBase - General
 package for Microservices based on FastAPI like Profiler, Scheduler, Sysinfo,
 Healtcheck, Error Handling etc. Home-page: https://github.com/u2d-ai/msaBase
-Download-URL: http://pypi.python.org/pypi/msaBase Author: Stefan Welcker
-Author-email: stefan@u2d.ai License: MIT Project-URL: Documentation, http://
+Author: Stefan Welcker Author-email: stefan@u2d.ai License: MIT Download-URL:
+http://pypi.python.org/pypi/msaBase Project-URL: Documentation, http://
 msaBase.u2d.ai/ Project-URL: Source, https://github.com/u2d-ai/msaBase Project-
-URL: Tracker, https://github.com/u2d-ai/msaBase/issues Classifier: Development
-Status :: 4 - Beta Classifier: Framework :: FastAPI Classifier: Intended
-Audience :: Developers Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: MacOS :: MacOS X Classifier: Operating System
-:: Microsoft :: Windows Classifier: Operating System :: POSIX :: Linux
-Classifier: Programming Language :: Python :: 3 Classifier: Programming
-Language :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9 Classifier: Programming
-Language :: Python :: 3.10 Classifier: Topic :: Database Classifier: Topic ::
-Database :: Front-Ends Classifier: Topic :: Documentation Classifier: Topic ::
-Internet :: WWW/HTTP :: WSGI :: Server Classifier: Topic :: Software
-Development :: Libraries Classifier: Topic :: Software Development :: Libraries
-:: Python Modules Description-Content-Type: text/markdown License-File: LICENCE
+URL: Tracker, https://github.com/u2d-ai/msaBase/issues Platform: UNKNOWN
+Classifier: Development Status :: 4 - Beta Classifier: Framework :: FastAPI
+Classifier: Intended Audience :: Developers Classifier: License :: OSI Approved
+:: MIT License Classifier: Operating System :: MacOS :: MacOS X Classifier:
+Operating System :: Microsoft :: Windows Classifier: Operating System :: POSIX
+:: Linux Classifier: Programming Language :: Python :: 3 Classifier:
+Programming Language :: Python :: 3.7 Classifier: Programming Language ::
+Python :: 3.8 Classifier: Programming Language :: Python :: 3.9 Classifier:
+Programming Language :: Python :: 3.10 Classifier: Topic :: Database
+Classifier: Topic :: Database :: Front-Ends Classifier: Topic :: Documentation
+Classifier: Topic :: Internet :: WWW/HTTP :: WSGI :: Server Classifier: Topic
+:: Software Development :: Libraries Classifier: Topic :: Software Development
+:: Libraries :: Python Modules Description-Content-Type: text/markdown License-
+File: LICENCE
  > msaBase- General Package for Microservices based on FastAPI like Profiler,
              Scheduler, Sysinfo, Healtcheck, Error Handling etc.
                    Optimized for use with FastAPI/Pydantic.
                  [Package_version] [Supported_Python_versions]
 ------ **Documentation**: Documentation_(https://msaBase.u2d.ai/) ------ ##
 Features - **MSABaseExceptionHandler**: Central exception handler which sends
 formatted exception to logger - **Filehandler utilities**: Classes for
```

### Comparing `msaBase-0.0.8/README.md` & `msaBase-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/config.py` & `msaBase-0.0.9/msaBase/config.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/configurate.py` & `msaBase-0.0.9/msaBase/configurate.py`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,16 @@
 
 Initialize with a MSAServiceDefintion Instance to control the features and functions of the MSAApp.
 
 """
 import os
 from asyncio import Task
 from datetime import datetime
-from typing import List, Type, Union
+from typing import List, Optional, Type, Union
+from dapr.clients import DaprClient
 
 from fastapi import FastAPI, HTTPException
 from fastapi.encoders import jsonable_encoder
 from fastapi.exception_handlers import http_exception_handler
 from fastapi.exceptions import RequestValidationError
 from fastapi.responses import ORJSONResponse
 from loguru import logger as logger_gruru
@@ -116,22 +117,30 @@
     """
 
     def __init__(
         self,
         settings: MSAServiceDefinition,
         sql_models: List[SQLModel] = None,
         auto_mount_site: bool = True,
+        title: str = "FastAPI",
+        description: str = "",
+        version: str = "0.1.0",
+        openapi_url: Optional[str] = "/openapi.json",
         *args,
         **kwargs,
     ) -> None:
         # call super class __init__
         super().__init__(*args, **settings.fastapi_kwargs)
 
         self.logger = logger_gruru
-
+        self.fastApi = FastAPI
+        self.title = title
+        self.description = description
+        self.version = version
+        self.openapi_url = openapi_url
         self.auto_mount_site: bool = auto_mount_site
         self.settings = settings
         self.SDUVersion = SDUVersion(
             version=self.settings.version, creation_date=datetime.utcnow().isoformat()
         )
         self.healthdefinition: MSAHealthDefinition = self.settings.healthdefinition
         self.limiter: "Limiter" = None
@@ -143,23 +152,34 @@
         self.asyncio_scheduler: "AsyncIOScheduler" = None
         self.site = None
         self._scheduler_task: Task = None
         self.ROOTPATH = os.path.join(os.path.dirname(__file__))
         self.abstract_fs: "MSAFilesystem" = None
         self.fs: "FS" = None
         self.healthcheck: "health.MSAHealthCheck" = None
+        self.logger.info_pub = self.logger_info
 
         init_logging()
         self.add_middlewares()
         self.add_functionality()
-
         self.logger.info("Events - Add Internal Handlers")
         self.add_event_handler("shutdown", self.shutdown_event)
         self.add_event_handler("startup", self.startup_event)
 
+    def logger_info(self, message: str, topic_name: str = ""):
+        if topic_name:
+            with DaprClient() as client:
+                client.publish_event(
+                    pubsub_name="spk_pub_sub",
+                    topic_name=topic_name,
+                    data=message,
+                    data_content_type="application/json",
+                )
+        self.logger.info(message)
+
     async def extend_startup_event(self) -> None:
         """You can extend the main shutdown"""
 
     async def startup_event(self) -> None:
         """Internal Startup Event Handler"""
         self.logger.info("msaBase Internal Startup MSAUIEvent")
         await self.extend_startup_event()
```

### Comparing `msaBase-0.0.8/msaBase/errorhandling.py` & `msaBase-0.0.9/msaBase/errorhandling.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/healthcheck.py` & `msaBase-0.0.9/msaBase/healthcheck.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/logger.py` & `msaBase-0.0.9/msaBase/logger.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/models/functionality.py` & `msaBase-0.0.9/msaBase/models/functionality.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/models/middlewares.py` & `msaBase-0.0.9/msaBase/models/middlewares.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/models/sysinfo.py` & `msaBase-0.0.9/msaBase/models/sysinfo.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/profiler.py` & `msaBase-0.0.9/msaBase/profiler.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/router.py` & `msaBase-0.0.9/msaBase/router.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase/sysinfo.py` & `msaBase-0.0.9/msaBase/sysinfo.py`

 * *Files identical despite different names*

### Comparing `msaBase-0.0.8/msaBase.egg-info/PKG-INFO` & `msaBase-0.0.9/msaBase.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: msaBase
-Version: 0.0.8
+Version: 0.0.9
 Summary: msaBase - General package for Microservices based on FastAPI like Profiler, Scheduler, Sysinfo, Healtcheck, Error Handling etc.
 Home-page: https://github.com/u2d-ai/msaBase
-Download-URL: http://pypi.python.org/pypi/msaBase
 Author: Stefan Welcker
 Author-email: stefan@u2d.ai
 License: MIT
+Download-URL: http://pypi.python.org/pypi/msaBase
 Project-URL: Documentation, http://msaBase.u2d.ai/
 Project-URL: Source, https://github.com/u2d-ai/msaBase
 Project-URL: Tracker, https://github.com/u2d-ai/msaBase/issues
+Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Framework :: FastAPI
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Operating System :: Microsoft :: Windows
 Classifier: Operating System :: POSIX :: Linux
@@ -92,7 +93,9 @@
 Build:  
 
     python setup.py sdist
 
 Publish to pypi:
 
     twine upload dist/*
+
+
```

#### html2text {}

```diff
@@ -1,26 +1,27 @@
-Metadata-Version: 2.1 Name: msaBase Version: 0.0.8 Summary: msaBase - General
+Metadata-Version: 2.1 Name: msaBase Version: 0.0.9 Summary: msaBase - General
 package for Microservices based on FastAPI like Profiler, Scheduler, Sysinfo,
 Healtcheck, Error Handling etc. Home-page: https://github.com/u2d-ai/msaBase
-Download-URL: http://pypi.python.org/pypi/msaBase Author: Stefan Welcker
-Author-email: stefan@u2d.ai License: MIT Project-URL: Documentation, http://
+Author: Stefan Welcker Author-email: stefan@u2d.ai License: MIT Download-URL:
+http://pypi.python.org/pypi/msaBase Project-URL: Documentation, http://
 msaBase.u2d.ai/ Project-URL: Source, https://github.com/u2d-ai/msaBase Project-
-URL: Tracker, https://github.com/u2d-ai/msaBase/issues Classifier: Development
-Status :: 4 - Beta Classifier: Framework :: FastAPI Classifier: Intended
-Audience :: Developers Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: MacOS :: MacOS X Classifier: Operating System
-:: Microsoft :: Windows Classifier: Operating System :: POSIX :: Linux
-Classifier: Programming Language :: Python :: 3 Classifier: Programming
-Language :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9 Classifier: Programming
-Language :: Python :: 3.10 Classifier: Topic :: Database Classifier: Topic ::
-Database :: Front-Ends Classifier: Topic :: Documentation Classifier: Topic ::
-Internet :: WWW/HTTP :: WSGI :: Server Classifier: Topic :: Software
-Development :: Libraries Classifier: Topic :: Software Development :: Libraries
-:: Python Modules Description-Content-Type: text/markdown License-File: LICENCE
+URL: Tracker, https://github.com/u2d-ai/msaBase/issues Platform: UNKNOWN
+Classifier: Development Status :: 4 - Beta Classifier: Framework :: FastAPI
+Classifier: Intended Audience :: Developers Classifier: License :: OSI Approved
+:: MIT License Classifier: Operating System :: MacOS :: MacOS X Classifier:
+Operating System :: Microsoft :: Windows Classifier: Operating System :: POSIX
+:: Linux Classifier: Programming Language :: Python :: 3 Classifier:
+Programming Language :: Python :: 3.7 Classifier: Programming Language ::
+Python :: 3.8 Classifier: Programming Language :: Python :: 3.9 Classifier:
+Programming Language :: Python :: 3.10 Classifier: Topic :: Database
+Classifier: Topic :: Database :: Front-Ends Classifier: Topic :: Documentation
+Classifier: Topic :: Internet :: WWW/HTTP :: WSGI :: Server Classifier: Topic
+:: Software Development :: Libraries Classifier: Topic :: Software Development
+:: Libraries :: Python Modules Description-Content-Type: text/markdown License-
+File: LICENCE
  > msaBase- General Package for Microservices based on FastAPI like Profiler,
              Scheduler, Sysinfo, Healtcheck, Error Handling etc.
                    Optimized for use with FastAPI/Pydantic.
                  [Package_version] [Supported_Python_versions]
 ------ **Documentation**: Documentation_(https://msaBase.u2d.ai/) ------ ##
 Features - **MSABaseExceptionHandler**: Central exception handler which sends
 formatted exception to logger - **Filehandler utilities**: Classes for
```

### Comparing `msaBase-0.0.8/msaBase.egg-info/SOURCES.txt` & `msaBase-0.0.9/msaBase.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 requirements.txt
 setup.py
 msaBase/__init__.py
 msaBase/config.py
 msaBase/configurate.py
 msaBase/errorhandling.py
 msaBase/healthcheck.py
+msaBase/helpers.py
 msaBase/logger.py
 msaBase/profiler.py
 msaBase/router.py
 msaBase/sysinfo.py
 msaBase.egg-info/PKG-INFO
 msaBase.egg-info/SOURCES.txt
 msaBase.egg-info/dependency_links.txt
```

### Comparing `msaBase-0.0.8/msaBase.egg-info/requires.txt` & `msaBase-0.0.9/msaBase.egg-info/requires.txt`

 * *Files 15% similar despite different names*

```diff
@@ -1,49 +1,49 @@
-msaCRUD>=0.0.1
-msaFileSystem>=0.0.1
-msaDocModels>=0.0.7
-fastapi[all]>=0.85.0
-fastapi_utils>=0.2.1
-pydantic[dotenv,email]~=1.9.2
-pyinstrument>=4.3.0
-strawberry-graphql>=0.130.4
-strawberry-graphql[fastapi]>=0.130.4
+Jinja2>=3.1.2
+Starlette-WTF~=0.4.3
+addict>=2.4.0
+aiofiles>=22.1.0
+aiohttp>=3.8.3
+aioredis>=2.0.1
+aiosqlite>=0.17.0
+apscheduler>=3.9.1
 autoflake>=1.6.1
 black>=22.8.0
-pyproject-flake8>=5.0.4
+dapr-ext-fastapi~=1.7.0
+dapr-ext-grpc~=1.7.0
+dapr~=1.7.0
+fastapi[all]>=0.85.0
+fastapi_utils>=0.2.1
 flake8>=5.0.4
+fs>=2.4.16
+gputil>=1.4.0
+hjson~=3.1.0
+httpx~=0.23.0
 isort>=5.10.1
 loguru>=0.6.0
 lxml>=4.9.1
+msaCRUD>=0.0.1
+msaDocModels>=0.0.8
+msaFileSystem>=0.0.1
+msgpack-asgi>=1.1.0
 mypy>=0.971
-setuptools>=65.2.0
-prometheus_fastapi_instrumentator>=5.9.1
-Jinja2>=3.1.2
 orjson>=3.8.0
+prometheus_fastapi_instrumentator>=5.9.1
+psutil>=5.9.2
+pydantic[dotenv,email]~=1.9.2
 pyinstrument>=4.3.0
-msgpack-asgi>=1.1.0
+pyinstrument>=4.3.0
+pyproject-flake8>=5.0.4
+pytest>=7.2.0
+setuptools>=65.2.0
 slowapi>=0.1.6
-addict>=2.4.0
-dapr~=1.7.0
-dapr-ext-grpc~=1.7.0
-dapr-ext-fastapi~=1.7.0
-aiofiles>=22.1.0
-fs>=2.4.16
-starlette~=0.20.4
-starlette-context~=0.3.4
-starception~=0.4.0
-Starlette-WTF~=0.4.3
-aiosqlite>=0.17.0
-aioredis>=2.0.1
-sqlmodel>=0.0.8
 sqlalchemy[asyncio]>=1.4.41
 sqlalchemy_database>=0.0.7
+sqlmodel>=0.0.8
+starception~=0.4.0
+starlette-context~=0.3.4
+starlette~=0.20.4
+strawberry-graphql>=0.130.4
+strawberry-graphql[fastapi]>=0.130.4
 tinydb>=4.7.0
-httpx~=0.23.0
-aiohttp>=3.8.3
-hjson~=3.1.0
 uvicorn~=0.18.3
 uvloop~=0.17.0
-gputil>=1.4.0
-psutil>=5.9.2
-apscheduler>=3.9.1
-pytest>=7.2.0
```

### Comparing `msaBase-0.0.8/requirements.txt` & `msaBase-0.0.9/requirements.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # MSA Dependencies
 msaCRUD>=0.0.1 # SQLModel/SQLAlchemy/FastAPI - DB Object CRUD/API Automation
 msaFileSystem>=0.0.1 # Agnostic Abstract Filesystem API which allows to use S3, GCS, Azure Datalake, your local FS, Youtube etc Optimized for use with FastAPI/Pydantic.
-msaDocModels>=0.0.7 # MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI results for processed documents
+msaDocModels>=0.0.8 # MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI results for processed documents
 
 # FastAPI related Dependencies
 fastapi[all]>=0.85.0 # FastAPI framework, high performance, easy to learn, fast to code, ready for production
 fastapi_utils>=0.2.1 # Reusable utilities for FastAPI, Repeated Tasks, APIModel, APISettings
 pydantic[email,dotenv]~=1.9.2 # Data validation and settings management using python type hints
 pyinstrument>=4.3.0 # pyinstrument to check service performance.
```

### Comparing `msaBase-0.0.8/setup.py` & `msaBase-0.0.9/setup.py`

 * *Files identical despite different names*

