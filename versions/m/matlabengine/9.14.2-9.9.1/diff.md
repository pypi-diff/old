# Comparing `tmp/matlabengine-9.14.2.tar.gz` & `tmp/matlabengine-9.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "matlabengine-9.14.2.tar", last modified: Thu Apr  6 14:43:53 2023, max compression
+gzip compressed data, was "matlabengine-9.9.1.tar", last modified: Mon Sep 12 22:54:23 2022, max compression
```

## Comparing `matlabengine-9.14.2.tar` & `matlabengine-9.9.1.tar`

### file list

```diff
@@ -1,27 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:43:53.631889 matlabengine-9.14.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-04-06 14:43:43.000000 matlabengine-9.14.2/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     6014 2023-04-06 14:43:53.631889 matlabengine-9.14.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5148 2023-04-06 14:43:43.000000 matlabengine-9.14.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-04-06 14:43:43.000000 matlabengine-9.14.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:43:53.631889 matlabengine-9.14.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)    20281 2023-04-06 14:43:43.000000 matlabengine-9.14.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:43:53.627889 matlabengine-9.14.2/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:43:53.627889 matlabengine-9.14.2/src/matlab/
--rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:43:53.627889 matlabengine-9.14.2/src/matlab/engine/
--rw-r--r--   0 runner    (1001) docker     (123)     7630 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/_arch.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/basefuture.py
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/engineerror.py
--rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/enginehelper.py
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/enginesession.py
--rw-r--r--   0 runner    (1001) docker     (123)     4989 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/fevalfuture.py
--rw-r--r--   0 runner    (1001) docker     (123)     4025 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/futureresult.py
--rw-r--r--   0 runner    (1001) docker     (123)    10224 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/matlabengine.py
--rw-r--r--   0 runner    (1001) docker     (123)     4617 2023-04-06 14:43:43.000000 matlabengine-9.14.2/src/matlab/engine/matlabfuture.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:43:53.627889 matlabengine-9.14.2/src/matlabengine.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6014 2023-04-06 14:43:53.000000 matlabengine-9.14.2/src/matlabengine.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      594 2023-04-06 14:43:53.000000 matlabengine-9.14.2/src/matlabengine.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:43:53.000000 matlabengine-9.14.2/src/matlabengine.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:43:53.000000 matlabengine-9.14.2/src/matlabengine.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 14:43:53.000000 matlabengine-9.14.2/src/matlabengine.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.525110 matlabengine-9.9.1/
+-rw-r--r--   0 runner    (1001) docker     (121)     1485 2022-09-12 22:54:14.000000 matlabengine-9.9.1/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)     6007 2022-09-12 22:54:23.525110 matlabengine-9.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     5144 2022-09-12 22:54:14.000000 matlabengine-9.9.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)       95 2022-09-12 22:54:14.000000 matlabengine-9.9.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-12 22:54:23.525110 matlabengine-9.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)    14336 2022-09-12 22:54:14.000000 matlabengine-9.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.517109 matlabengine-9.9.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.521110 matlabengine-9.9.1/src/matlab/
+-rw-r--r--   0 runner    (1001) docker     (121)      883 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.521110 matlabengine-9.9.1/src/matlab/_internal/
+-rw-r--r--   0 runner    (1001) docker     (121)       33 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/_internal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13093 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/_internal/mlarray_sequence.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3924 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/_internal/mlarray_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.521110 matlabengine-9.9.1/src/matlab/engine/
+-rw-r--r--   0 runner    (1001) docker     (121)     7215 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1203 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/basefuture.py
+-rw-r--r--   0 runner    (1001) docker     (121)      264 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/engineerror.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1127 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/enginehelper.py
+-rw-r--r--   0 runner    (1001) docker     (121)      524 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/enginesession.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4989 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/fevalfuture.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4025 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/futureresult.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10224 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/matlabengine.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4617 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/engine/matlabfuture.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9105 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/mlarray.py
+-rw-r--r--   0 runner    (1001) docker     (121)      983 2022-09-12 22:54:14.000000 matlabengine-9.9.1/src/matlab/mlexceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-12 22:54:23.521110 matlabengine-9.9.1/src/matlabengine.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     6007 2022-09-12 22:54:23.000000 matlabengine-9.9.1/src/matlabengine.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      727 2022-09-12 22:54:23.000000 matlabengine-9.9.1/src/matlabengine.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-12 22:54:23.000000 matlabengine-9.9.1/src/matlabengine.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-12 22:54:23.000000 matlabengine-9.9.1/src/matlabengine.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)        7 2022-09-12 22:54:23.000000 matlabengine-9.9.1/src/matlabengine.egg-info/top_level.txt
```

### Comparing `matlabengine-9.14.2/LICENSE.txt` & `matlabengine-9.9.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/PKG-INFO` & `matlabengine-9.9.1/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,60 +1,39 @@
-Metadata-Version: 2.1
-Name: matlabengine
-Version: 9.14.2
-Summary: A module to call MATLAB from Python
-Home-page: https://github.com/mathworks/matlab-engine-for-python/
-Author: MathWorks
-License: MathWorks XSLA License
-Project-URL: Documentation, https://www.mathworks.com/help/matlab/matlab-engine-for-python.html
-Project-URL: Source, https://github.com/mathworks/matlab-engine-for-python
-Project-URL: Tracker, https://github.com/mathworks/matlab-engine-for-python/issues
-Keywords: MATLAB,MATLAB Engine for Python
-Platform: UNKNOWN
-Classifier: Natural Language :: English
-Classifier: Intended Audience :: Developers
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Requires-Python: >=3.8, <3.11
-Description-Content-Type: text/markdown
-License-File: LICENSE.txt
-
 # MATLAB Engine API for Python
 
 The MATLAB&reg; Engine API for Python&reg; provides a package to integrate MATLAB functionality directly with a Python application, creating an interface to call functions from your MATLAB installation from Python code. 
 
 ---
 ## Requirements
 ### Required MathWorks Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* MATLAB release R2023a
+* MATLAB release R2020b
 
 ### Required 3rd Party Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* Python 3.8, 3.9, or 3.10
+* Python 3.6, 3.7, or 3.8
     * Supported Python versions by MATLAB release can be found [here](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf).
 
 ---
 
 ## Install
 
 ### Windows
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 
 
 ### Linux&reg; 
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, Linux installs MATLAB at:<br>
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/usr/local/MATLAB/R2023a```
+```/usr/local/MATLAB/R2020b```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<matlabroot>/bin/glnxa64
 ```
@@ -63,22 +42,22 @@
 # in .tcshrc
 setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:<matlabroot>/bin/glnxa64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ### macOS
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, macOS installs MATLAB at:<br>
 
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/Applications/MATLAB_R2023a.app```
+```/Applications/MATLAB_R2020b.app```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:<matlabroot>/bin/maci64
 ```
@@ -87,15 +66,15 @@
 # in .tcshrc
 setenv DYLD_LIBRARY_PATH ${DYLD_LIBRARY_PATH}:<matlabroot>/bin/maci64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ---
 
 ## Getting Started
 * Start Python.
 * Import the ```matlab.engine``` package into the Python session.
@@ -155,9 +134,7 @@
 Copyright &copy; 2022 MathWorks, Inc. All rights reserved.
 
 Linux&reg; is the registered trademark of Linus Torvalds in the U.S. and other countries.
 
 Mac OS is a trademark of Apple Inc., registered in the U.S. and other countries.
 
 "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation, used by MathWorks with permission from the Foundation.
-
-
```

### Comparing `matlabengine-9.14.2/README.md` & `matlabengine-9.9.1/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,39 +1,60 @@
+Metadata-Version: 2.1
+Name: matlabengine
+Version: 9.9.1
+Summary: A module to call MATLAB from Python
+Home-page: https://github.com/mathworks/matlab-engine-for-python/
+Author: MathWorks
+License: MathWorks XSLA License
+Project-URL: Documentation, https://www.mathworks.com/help/matlab/matlab-engine-for-python.html
+Project-URL: Source, https://github.com/mathworks/matlab-engine-for-python
+Project-URL: Tracker, https://github.com/mathworks/matlab-engine-for-python/issues
+Keywords: MATLAB,MATLAB Engine for Python
+Platform: UNKNOWN
+Classifier: Natural Language :: English
+Classifier: Intended Audience :: Developers
+Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Requires-Python: >=3.6, <3.9
+Description-Content-Type: text/markdown
+License-File: LICENSE.txt
+
 # MATLAB Engine API for Python
 
 The MATLAB&reg; Engine API for Python&reg; provides a package to integrate MATLAB functionality directly with a Python application, creating an interface to call functions from your MATLAB installation from Python code. 
 
 ---
 ## Requirements
 ### Required MathWorks Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* MATLAB release R2023a
+* MATLAB release R2020b
 
 ### Required 3rd Party Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* Python 3.8, 3.9, or 3.10
+* Python 3.6, 3.7, or 3.8
     * Supported Python versions by MATLAB release can be found [here](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf).
 
 ---
 
 ## Install
 
 ### Windows
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 
 
 ### Linux&reg; 
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, Linux installs MATLAB at:<br>
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/usr/local/MATLAB/R2023a```
+```/usr/local/MATLAB/R2020b```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<matlabroot>/bin/glnxa64
 ```
@@ -42,22 +63,22 @@
 # in .tcshrc
 setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:<matlabroot>/bin/glnxa64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ### macOS
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, macOS installs MATLAB at:<br>
 
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/Applications/MATLAB_R2023a.app```
+```/Applications/MATLAB_R2020b.app```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:<matlabroot>/bin/maci64
 ```
@@ -66,15 +87,15 @@
 # in .tcshrc
 setenv DYLD_LIBRARY_PATH ${DYLD_LIBRARY_PATH}:<matlabroot>/bin/maci64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ---
 
 ## Getting Started
 * Start Python.
 * Import the ```matlab.engine``` package into the Python session.
@@ -134,7 +155,9 @@
 Copyright &copy; 2022 MathWorks, Inc. All rights reserved.
 
 Linux&reg; is the registered trademark of Linus Torvalds in the U.S. and other countries.
 
 Mac OS is a trademark of Apple Inc., registered in the U.S. and other countries.
 
 "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation, used by MathWorks with permission from the Foundation.
+
+
```

### Comparing `matlabengine-9.14.2/src/matlab/engine/__init__.py` & `matlabengine-9.9.1/src/matlab/engine/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#Copyright 2014-2022 MathWorks, Inc.
+#Copyright 2014-2020 MathWorks, Inc.
 
 """
 The MATLAB Engine enables you to call any MATLAB statement either synchronously
 or asynchronously.  With synchronous execution, the invocation of a MATLAB
 statement returns the result after the call finishes.  With asynchronous
 execution, the invocation of a MATLAB statement is performed in the background 
 and a FutureResult object is returned immediately.  You can call its "done" 
@@ -24,61 +24,50 @@
 import importlib
 import atexit
 import weakref
 import threading
 
 # UPDATE_IF_PYTHON_VERSION_ADDED_OR_REMOVED : search for this string in codebase 
 # when support for a Python version must be added or removed
-_supported_versions = ['2_7', '3_8', '3_9', '3_10']
+_supported_versions = ['2_7', '3_6', '3_7', '3_8']
 _ver = sys.version_info
 _version = '{0}_{1}'.format(_ver[0], _ver[1])
 _PYTHONVERSION = None
 
 if _version in _supported_versions:
     _PYTHONVERSION = _version
 else:
     raise EnvironmentError("Python %s is not supported." % _version)
 
 _module_folder = os.path.dirname(os.path.realpath(__file__))
-_arch_filename = os.path.join(_module_folder, "_arch.txt")
-success = False 
-firstExceptionMessage = ''
-secondExceptionMessage = ''
+_arch_filename = _module_folder+os.sep+"_arch.txt"
+ 
 try:
     pythonengine = importlib.import_module("matlabengineforpython"+_PYTHONVERSION)
-except Exception as firstE:
-    firstExceptionMessage = str(firstE)
-
-if firstExceptionMessage:
+except:
     try:
         _arch_file = open(_arch_filename,'r')
         _lines = _arch_file.readlines()
-        [_arch, _bin_dir,_engine_dir, _extern_bin_dir] = [x.rstrip() for x in _lines if x.rstrip() != ""]
+        [_arch, _bin_dir,_engine_dir] = [x.rstrip() for x in _lines if x.rstrip() != ""]
         _arch_file.close()
         sys.path.insert(0,_engine_dir)
-        sys.path.insert(0,_extern_bin_dir)
 
         _envs = {'win32': 'PATH', 'win64': 'PATH'}
         if _arch in _envs:
             if _envs[_arch] in os.environ:
                 _env = os.environ[_envs[_arch]]
-                os.environ[_envs[_arch]] = _bin_dir + os.pathsep + os.environ[_envs[_arch]]
+                os.environ[_envs[_arch]] = _bin_dir+os.pathsep+os.environ[_envs[_arch]]
             else:
                 os.environ[_envs[_arch]] = _bin_dir
             if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
                 os.add_dll_directory(_bin_dir)
         pythonengine = importlib.import_module("matlabengineforpython"+_PYTHONVERSION)
-    except Exception as secondE:
-        str1 = 'Please reinstall MATLAB Engine for Python or contact '
-        str2 = 'MathWorks Technical Support for assistance:\nFirst issue: {}\nSecond issue: {}'.format(
-            firstExceptionMessage, secondE)
-        secondExceptionMessage = str1 + str2
-
-if secondExceptionMessage:        
-    raise EnvironmentError(secondExceptionMessage)
+    except Exception as e:
+        raise EnvironmentError('Please reinstall MATLAB Engine for Python or contact '
+                               'MathWorks Technical Support for assistance: %s' % e)
 
 
 """
 This lock can make sure the global variable _engines is updated correctly in
 multi-thread use case.  Also, it guarantees that only one MATLAB is launched
 when connect_matlab() is called if there is no shared MATLAB session.
 """
```

### Comparing `matlabengine-9.14.2/src/matlab/engine/basefuture.py` & `matlabengine-9.9.1/src/matlab/engine/basefuture.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/enginehelper.py` & `matlabengine-9.9.1/src/matlab/engine/enginehelper.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/enginesession.py` & `matlabengine-9.9.1/src/matlab/engine/enginesession.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/fevalfuture.py` & `matlabengine-9.9.1/src/matlab/engine/fevalfuture.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/futureresult.py` & `matlabengine-9.9.1/src/matlab/engine/futureresult.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/matlabengine.py` & `matlabengine-9.9.1/src/matlab/engine/matlabengine.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlab/engine/matlabfuture.py` & `matlabengine-9.9.1/src/matlab/engine/matlabfuture.py`

 * *Files identical despite different names*

### Comparing `matlabengine-9.14.2/src/matlabengine.egg-info/PKG-INFO` & `matlabengine-9.9.1/src/matlabengine.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,60 +1,60 @@
 Metadata-Version: 2.1
 Name: matlabengine
-Version: 9.14.2
+Version: 9.9.1
 Summary: A module to call MATLAB from Python
 Home-page: https://github.com/mathworks/matlab-engine-for-python/
 Author: MathWorks
 License: MathWorks XSLA License
 Project-URL: Documentation, https://www.mathworks.com/help/matlab/matlab-engine-for-python.html
 Project-URL: Source, https://github.com/mathworks/matlab-engine-for-python
 Project-URL: Tracker, https://github.com/mathworks/matlab-engine-for-python/issues
 Keywords: MATLAB,MATLAB Engine for Python
 Platform: UNKNOWN
 Classifier: Natural Language :: English
 Classifier: Intended Audience :: Developers
+Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Requires-Python: >=3.8, <3.11
+Requires-Python: >=3.6, <3.9
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # MATLAB Engine API for Python
 
 The MATLAB&reg; Engine API for Python&reg; provides a package to integrate MATLAB functionality directly with a Python application, creating an interface to call functions from your MATLAB installation from Python code. 
 
 ---
 ## Requirements
 ### Required MathWorks Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* MATLAB release R2023a
+* MATLAB release R2020b
 
 ### Required 3rd Party Products
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-* Python 3.8, 3.9, or 3.10
+* Python 3.6, 3.7, or 3.8
     * Supported Python versions by MATLAB release can be found [here](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf).
 
 ---
 
 ## Install
 
 ### Windows
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 
 
 ### Linux&reg; 
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, Linux installs MATLAB at:<br>
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/usr/local/MATLAB/R2023a```
+```/usr/local/MATLAB/R2020b```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<matlabroot>/bin/glnxa64
 ```
@@ -63,22 +63,22 @@
 # in .tcshrc
 setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:<matlabroot>/bin/glnxa64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ### macOS
 Prior to installation, check the default install location of MATLAB by calling ```matlabroot``` in a MATLAB Command Window. By default, macOS installs MATLAB at:<br>
 
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
-```/Applications/MATLAB_R2023a.app```
+```/Applications/MATLAB_R2020b.app```
 
 When MATLAB is not installed in the default location, the bin/*architecture* directory within the MATLAB root directory must be added to an environment variable. The path can be added to the environment variable within the shell startup configuration file (for example, .bashrc for bash shell or .tcshrc for tcsh).
 
 ```bash
 # in .bashrc
 export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:<matlabroot>/bin/maci64
 ```
@@ -87,15 +87,15 @@
 # in .tcshrc
 setenv DYLD_LIBRARY_PATH ${DYLD_LIBRARY_PATH}:<matlabroot>/bin/maci64
 ```
 
 MATLAB Engine API for Python can be installed directly from the Python Package Index.
 <!-- MUST_BE_UPDATED_EACH_RELEASE (Search repo for this string) -->
 ```bash
-$ python -m pip install matlabengine==9.14.2
+$ python -m pip install matlabengine==9.9.1
 ```
 
 ---
 
 ## Getting Started
 * Start Python.
 * Import the ```matlab.engine``` package into the Python session.
```

### Comparing `matlabengine-9.14.2/src/matlabengine.egg-info/SOURCES.txt` & `matlabengine-9.9.1/src/matlabengine.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,18 @@
 LICENSE.txt
 README.md
 pyproject.toml
 setup.py
 src/matlab/__init__.py
+src/matlab/mlarray.py
+src/matlab/mlexceptions.py
+src/matlab/_internal/__init__.py
+src/matlab/_internal/mlarray_sequence.py
+src/matlab/_internal/mlarray_utils.py
 src/matlab/engine/__init__.py
-src/matlab/engine/_arch.txt
 src/matlab/engine/basefuture.py
 src/matlab/engine/engineerror.py
 src/matlab/engine/enginehelper.py
 src/matlab/engine/enginesession.py
 src/matlab/engine/fevalfuture.py
 src/matlab/engine/futureresult.py
 src/matlab/engine/matlabengine.py
```

