# Comparing `tmp/mlogconfig-0.1.0.tar.gz` & `tmp/mlogconfig-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlogconfig-0.1.0.tar", last modified: Fri Apr  7 02:29:14 2023, max compression
+gzip compressed data, was "mlogconfig-0.1.1.tar", last modified: Fri Apr  7 05:15:57 2023, max compression
```

## Comparing `mlogconfig-0.1.0.tar` & `mlogconfig-0.1.1.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxr-xr-x   0 mattwyen   (501) staff       (20)        0 2023-04-07 02:29:14.952490 mlogconfig-0.1.0/
--rw-r--r--   0 mattwyen   (501) staff       (20)     1099 2023-04-06 21:39:26.000000 mlogconfig-0.1.0/LICENSE.md
--rw-r--r--   0 mattwyen   (501) staff       (20)       12 2023-04-07 02:20:05.000000 mlogconfig-0.1.0/MANIFEST.in
--rw-r--r--   0 mattwyen   (501) staff       (20)     6486 2023-04-07 02:29:14.952231 mlogconfig-0.1.0/PKG-INFO
--rw-r--r--   0 mattwyen   (501) staff       (20)     5694 2023-04-07 02:14:07.000000 mlogconfig-0.1.0/README.md
-drwxr-xr-x   0 mattwyen   (501) staff       (20)        0 2023-04-07 02:29:14.951800 mlogconfig-0.1.0/mlogconfig.egg-info/
--rw-r--r--   0 mattwyen   (501) staff       (20)     6486 2023-04-07 02:29:14.000000 mlogconfig-0.1.0/mlogconfig.egg-info/PKG-INFO
--rw-r--r--   0 mattwyen   (501) staff       (20)      177 2023-04-07 02:29:14.000000 mlogconfig-0.1.0/mlogconfig.egg-info/SOURCES.txt
--rw-r--r--   0 mattwyen   (501) staff       (20)        1 2023-04-07 02:29:14.000000 mlogconfig-0.1.0/mlogconfig.egg-info/dependency_links.txt
--rw-r--r--   0 mattwyen   (501) staff       (20)        1 2023-04-07 02:29:14.000000 mlogconfig-0.1.0/mlogconfig.egg-info/top_level.txt
--rw-r--r--   0 mattwyen   (501) staff       (20)       38 2023-04-07 02:29:14.952550 mlogconfig-0.1.0/setup.cfg
--rw-r--r--   0 mattwyen   (501) staff       (20)     1105 2023-04-07 02:26:30.000000 mlogconfig-0.1.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:15:57.302211 mlogconfig-0.1.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 05:15:41.000000 mlogconfig-0.1.1/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-07 05:15:41.000000 mlogconfig-0.1.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     7580 2023-04-07 05:15:57.302211 mlogconfig-0.1.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6788 2023-04-07 05:15:41.000000 mlogconfig-0.1.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:15:57.302211 mlogconfig-0.1.1/mlogconfig.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     7580 2023-04-07 05:15:57.000000 mlogconfig-0.1.1/mlogconfig.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      177 2023-04-07 05:15:57.000000 mlogconfig-0.1.1/mlogconfig.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 05:15:57.000000 mlogconfig-0.1.1/mlogconfig.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 05:15:57.000000 mlogconfig-0.1.1/mlogconfig.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 05:15:57.302211 mlogconfig-0.1.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1105 2023-04-07 05:15:41.000000 mlogconfig-0.1.1/setup.py
```

### Comparing `mlogconfig-0.1.0/LICENSE.md` & `mlogconfig-0.1.1/LICENSE.md`

 * *Files identical despite different names*

### Comparing `mlogconfig-0.1.0/PKG-INFO` & `mlogconfig-0.1.1/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,42 +1,25 @@
-Metadata-Version: 2.1
-Name: mlogconfig
-Version: 0.1.0
-Summary: A simple logging setup utility that configures logging with file, console, syslog, and Windows event log handlers.
-Home-page: https://github.com/talltechy/logger
-Author: Matt Wyen
-Author-email: matt@mattwyen.me
-Classifier: Development Status :: 3 - Alpha
-Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: 3.11
-Requires-Python: >=3.9
-Description-Content-Type: text/markdown
-License-File: LICENSE.md
-
 # [mlogconfig.py](mlogconfig.py)
 
 [![Pylint](https://github.com/talltechy/logger/actions/workflows/pylint.yml/badge.svg)](https://github.com/talltechy/logger/actions/workflows/pylint.yml)
 [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
 
 This is a Python script for configuring logging with various handlers such as console, file, syslog, and Windows event log. The script defines two functions; validate_log_file() and setup_logging(). The validate_log_file() takes in a log file path and validates it. It checks if the directory exists, is accessible and writable, and also checks if the log file already exists. If the log file already exists, the function asks the user what to do with it; append to it, overwrite it or create a new file. If the user chooses to create a new file, the function prompts for a new path. If the user chooses to append or overwrite, the function sets up a file handler accordingly and returns it. The file handler and the log file path are returned by the function.
 
 The setup_logging() function takes in a log file path, boolean values of console_logging, syslog_logging, and windows_event_logging. It calls the validate_log_file() function to validate the log file path and creates a file handler. The function adds the file handler to the root logger and sets the log level to INFO. It also creates a formatter to use for all the handlers. If console_logging is True, the function creates a console handler, sets the formatter for it, and adds the handler to the root logger. If syslog_logging is True and the platform running is either Linux or Darwin, the function creates a SysLogHandler and sets the formatter for it. If windows_event_logging is True and the platform running is Windows, the function creates an NTEventLogHandler and adds it to the root logger.
 
 Finally, if the script is run directly (not imported as a module), it calls the setup_logging() function with default values of log_file_path, console_logging, syslog_logging, and windows_event_logging. It sets console_logging, syslog_logging, and windows_event_logging to True. The log file path is set to "./log_file.log".
 
 The module contains two functions:
 
-1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path.
-2. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
+1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path. In the `validate_log_file` function, the mode parameter refers to the mode in which the log file should be opened. You can pass the desired mode directly as a parameter to control how the log file will be opened and used. There are three possible modes:
+   1. 'a' - Append: In this mode, new log entries will be added to the existing log file, preserving the existing content. If the file does not exist, it will be created. This is the default mode, as it ensures that existing log data is not lost.
+   2. 'w' - Overwrite: In this mode, if the log file already exists, its content will be erased, and new log entries will overwrite the previous content. If the file does not exist, it will be created. This mode is useful when you want to start a new log session and discard previous log data.
+   3. 'n' - New file: In this mode, if the log file already exists, an error will be raised, prompting the user to choose a different file path for the new log file. This mode is useful when you want to create a new log file and avoid accidentally overwriting or appending to an existing log file.
+1. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
 
 ## Requirements
 
 The program requires the following:
 
 - Python 3.x
 - A valid file path for logging.
@@ -101,15 +84,15 @@
 
 The following code sets up logging with a file handler and a Windows event log handler. In this example, windows_event_logging is set to True, while console_logging and syslog_logging are set to False.
 
 ```python
 setup_logging("./log_file.log", windows_event_logging=True)
 ```
 
-## Example Python Script
+### Example Python Script
 
 Here's an example of how to use the module in a Python script:
 
 ```python
 import mlogconfig
 
 # Set up logging with file, console, syslog and Windows event log handlers
```

### Comparing `mlogconfig-0.1.0/README.md` & `mlogconfig-0.1.1/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,22 +1,45 @@
+Metadata-Version: 2.1
+Name: mlogconfig
+Version: 0.1.1
+Summary: A simple logging setup utility that configures logging with file, console, syslog, and Windows event log handlers.
+Home-page: https://github.com/talltechy/logger
+Author: Matt Wyen
+Author-email: matt@mattwyen.me
+Classifier: Development Status :: 3 - Alpha
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Classifier: Programming Language :: Python
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Requires-Python: >=3.9
+Description-Content-Type: text/markdown
+License-File: LICENSE.md
+
 # [mlogconfig.py](mlogconfig.py)
 
 [![Pylint](https://github.com/talltechy/logger/actions/workflows/pylint.yml/badge.svg)](https://github.com/talltechy/logger/actions/workflows/pylint.yml)
 [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
 
 This is a Python script for configuring logging with various handlers such as console, file, syslog, and Windows event log. The script defines two functions; validate_log_file() and setup_logging(). The validate_log_file() takes in a log file path and validates it. It checks if the directory exists, is accessible and writable, and also checks if the log file already exists. If the log file already exists, the function asks the user what to do with it; append to it, overwrite it or create a new file. If the user chooses to create a new file, the function prompts for a new path. If the user chooses to append or overwrite, the function sets up a file handler accordingly and returns it. The file handler and the log file path are returned by the function.
 
 The setup_logging() function takes in a log file path, boolean values of console_logging, syslog_logging, and windows_event_logging. It calls the validate_log_file() function to validate the log file path and creates a file handler. The function adds the file handler to the root logger and sets the log level to INFO. It also creates a formatter to use for all the handlers. If console_logging is True, the function creates a console handler, sets the formatter for it, and adds the handler to the root logger. If syslog_logging is True and the platform running is either Linux or Darwin, the function creates a SysLogHandler and sets the formatter for it. If windows_event_logging is True and the platform running is Windows, the function creates an NTEventLogHandler and adds it to the root logger.
 
 Finally, if the script is run directly (not imported as a module), it calls the setup_logging() function with default values of log_file_path, console_logging, syslog_logging, and windows_event_logging. It sets console_logging, syslog_logging, and windows_event_logging to True. The log file path is set to "./log_file.log".
 
 The module contains two functions:
 
-1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path.
-2. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
+1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path. In the `validate_log_file` function, the mode parameter refers to the mode in which the log file should be opened. You can pass the desired mode directly as a parameter to control how the log file will be opened and used. There are three possible modes:
+   1. 'a' - Append: In this mode, new log entries will be added to the existing log file, preserving the existing content. If the file does not exist, it will be created. This is the default mode, as it ensures that existing log data is not lost.
+   2. 'w' - Overwrite: In this mode, if the log file already exists, its content will be erased, and new log entries will overwrite the previous content. If the file does not exist, it will be created. This mode is useful when you want to start a new log session and discard previous log data.
+   3. 'n' - New file: In this mode, if the log file already exists, an error will be raised, prompting the user to choose a different file path for the new log file. This mode is useful when you want to create a new log file and avoid accidentally overwriting or appending to an existing log file.
+1. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
 
 ## Requirements
 
 The program requires the following:
 
 - Python 3.x
 - A valid file path for logging.
@@ -81,15 +104,15 @@
 
 The following code sets up logging with a file handler and a Windows event log handler. In this example, windows_event_logging is set to True, while console_logging and syslog_logging are set to False.
 
 ```python
 setup_logging("./log_file.log", windows_event_logging=True)
 ```
 
-## Example Python Script
+### Example Python Script
 
 Here's an example of how to use the module in a Python script:
 
 ```python
 import mlogconfig
 
 # Set up logging with file, console, syslog and Windows event log handlers
```

### Comparing `mlogconfig-0.1.0/mlogconfig.egg-info/PKG-INFO` & `mlogconfig-0.1.1/mlogconfig.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlogconfig
-Version: 0.1.0
+Version: 0.1.1
 Summary: A simple logging setup utility that configures logging with file, console, syslog, and Windows event log handlers.
 Home-page: https://github.com/talltechy/logger
 Author: Matt Wyen
 Author-email: matt@mattwyen.me
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
@@ -27,16 +27,19 @@
 
 The setup_logging() function takes in a log file path, boolean values of console_logging, syslog_logging, and windows_event_logging. It calls the validate_log_file() function to validate the log file path and creates a file handler. The function adds the file handler to the root logger and sets the log level to INFO. It also creates a formatter to use for all the handlers. If console_logging is True, the function creates a console handler, sets the formatter for it, and adds the handler to the root logger. If syslog_logging is True and the platform running is either Linux or Darwin, the function creates a SysLogHandler and sets the formatter for it. If windows_event_logging is True and the platform running is Windows, the function creates an NTEventLogHandler and adds it to the root logger.
 
 Finally, if the script is run directly (not imported as a module), it calls the setup_logging() function with default values of log_file_path, console_logging, syslog_logging, and windows_event_logging. It sets console_logging, syslog_logging, and windows_event_logging to True. The log file path is set to "./log_file.log".
 
 The module contains two functions:
 
-1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path.
-2. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
+1. `validate_log_file(log_file_path)`: Validates and handles the provided log file path. In the `validate_log_file` function, the mode parameter refers to the mode in which the log file should be opened. You can pass the desired mode directly as a parameter to control how the log file will be opened and used. There are three possible modes:
+   1. 'a' - Append: In this mode, new log entries will be added to the existing log file, preserving the existing content. If the file does not exist, it will be created. This is the default mode, as it ensures that existing log data is not lost.
+   2. 'w' - Overwrite: In this mode, if the log file already exists, its content will be erased, and new log entries will overwrite the previous content. If the file does not exist, it will be created. This mode is useful when you want to start a new log session and discard previous log data.
+   3. 'n' - New file: In this mode, if the log file already exists, an error will be raised, prompting the user to choose a different file path for the new log file. This mode is useful when you want to create a new log file and avoid accidentally overwriting or appending to an existing log file.
+1. `setup_logging(log_file_path, syslog_address=None)`: Sets up logging with a file and, if applicable, a syslog or Windows event log handler.
 
 ## Requirements
 
 The program requires the following:
 
 - Python 3.x
 - A valid file path for logging.
@@ -101,15 +104,15 @@
 
 The following code sets up logging with a file handler and a Windows event log handler. In this example, windows_event_logging is set to True, while console_logging and syslog_logging are set to False.
 
 ```python
 setup_logging("./log_file.log", windows_event_logging=True)
 ```
 
-## Example Python Script
+### Example Python Script
 
 Here's an example of how to use the module in a Python script:
 
 ```python
 import mlogconfig
 
 # Set up logging with file, console, syslog and Windows event log handlers
```

### Comparing `mlogconfig-0.1.0/setup.py` & `mlogconfig-0.1.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name="mlogconfig",
-    version="0.1.0",
+    version="0.1.1",
     author="Matt Wyen",
     author_email="matt@mattwyen.me",
     description="A simple logging setup utility that configures logging with file, console, syslog, and Windows event log handlers.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/talltechy/logger",
     packages=find_packages(),
```

