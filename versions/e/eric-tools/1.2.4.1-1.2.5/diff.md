# Comparing `tmp/eric_tools-1.2.4.1.tar.gz` & `tmp/eric_tools-1.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/eric_tools-1.2.4.1.tar", last modified: Thu Jun 30 15:13:41 2022, max compression
+gzip compressed data, was "dist/eric_tools-1.2.5.tar", last modified: Fri Apr  7 07:37:38 2023, max compression
```

## Comparing `eric_tools-1.2.4.1.tar` & `eric_tools-1.2.5.tar`

### file list

```diff
@@ -1,28 +1,27 @@
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/
--rw-r--r--   0 eric       (501) staff       (20)     1809 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/PKG-INFO
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools/
--rwxr-xr-x   0 eric       (501) staff       (20)     1619 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/Abstract.py
--rwxr-xr-x   0 eric       (501) staff       (20)      737 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/readconfig.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1324 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/jwt_encrypt.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1887 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/decorator.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1163 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/remove.py
--rwxr-xr-x   0 eric       (501) staff       (20)      567 2022-06-30 15:11:53.000000 eric_tools-1.2.4.1/eric_tools/__init__.py
--rwxr-xr-x   0 eric       (501) staff       (20)     2320 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/pgsql.py
--rwxr-xr-x   0 eric       (501) staff       (20)      638 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/convert_json.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1662 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/encryption_classmethod.py
--rwxr-xr-x   0 eric       (501) staff       (20)     3058 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/logger.py
--rwxr-xr-x   0 eric       (501) staff       (20)     8752 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/BingDwenDwen.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1002 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/ip.py
--rwxr-xr-x   0 eric       (501) staff       (20)      741 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/exception_class.py
--rwxr-xr-x   0 eric       (501) staff       (20)      423 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/sftp.py
--rwxr-xr-x   0 eric       (501) staff       (20)     1230 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/send_email.py
--rwxr-xr-x   0 eric       (501) staff       (20)     2855 2022-06-30 14:46:45.000000 eric_tools-1.2.4.1/eric_tools/resize_image.py
--rw-r--r--   0 eric       (501) staff       (20)      985 2022-06-30 15:12:40.000000 eric_tools-1.2.4.1/README.md
--rwxr-xr-x   0 eric       (501) staff       (20)      831 2022-06-30 15:12:16.000000 eric_tools-1.2.4.1/setup.py
--rw-r--r--   0 eric       (501) staff       (20)       38 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/setup.cfg
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/
--rw-r--r--   0 eric       (501) staff       (20)     1809 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/PKG-INFO
--rw-r--r--   0 eric       (501) staff       (20)      579 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/SOURCES.txt
--rw-r--r--   0 eric       (501) staff       (20)       34 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/requires.txt
--rw-r--r--   0 eric       (501) staff       (20)       11 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/top_level.txt
--rw-r--r--   0 eric       (501) staff       (20)        1 2022-06-30 15:13:41.000000 eric_tools-1.2.4.1/eric_tools.egg-info/dependency_links.txt
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2023-04-07 07:37:38.000000 eric_tools-1.2.5/
+-rw-r--r--   0 eric       (501) staff       (20)     1807 2023-04-07 07:37:38.000000 eric_tools-1.2.5/PKG-INFO
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2023-04-07 07:37:38.000000 eric_tools-1.2.5/eric_tools/
+-rwxr-xr-x   0 eric       (501) staff       (20)     1619 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/Abstract.py
+-rwxr-xr-x   0 eric       (501) staff       (20)      737 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/readconfig.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1324 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/jwt_encrypt.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1887 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/decorator.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1163 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/remove.py
+-rwxr-xr-x   0 eric       (501) staff       (20)      565 2023-04-07 07:36:21.000000 eric_tools-1.2.5/eric_tools/__init__.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     2320 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/pgsql.py
+-rwxr-xr-x   0 eric       (501) staff       (20)      638 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/convert_json.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1662 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/encryption_classmethod.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     3058 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/logger.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1002 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/ip.py
+-rwxr-xr-x   0 eric       (501) staff       (20)      741 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/exception_class.py
+-rwxr-xr-x   0 eric       (501) staff       (20)      423 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/sftp.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     1230 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/send_email.py
+-rwxr-xr-x   0 eric       (501) staff       (20)     2855 2022-06-30 14:46:45.000000 eric_tools-1.2.5/eric_tools/resize_image.py
+-rw-r--r--   0 eric       (501) staff       (20)      985 2022-06-30 15:14:49.000000 eric_tools-1.2.5/README.md
+-rwxr-xr-x   0 eric       (501) staff       (20)      829 2023-04-07 07:36:55.000000 eric_tools-1.2.5/setup.py
+-rw-r--r--   0 eric       (501) staff       (20)       38 2023-04-07 07:37:38.000000 eric_tools-1.2.5/setup.cfg
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2023-04-07 07:37:38.000000 eric_tools-1.2.5/eric_tools.egg-info/
+-rw-r--r--   0 eric       (501) staff       (20)     1807 2023-04-07 07:37:37.000000 eric_tools-1.2.5/eric_tools.egg-info/PKG-INFO
+-rw-r--r--   0 eric       (501) staff       (20)      552 2023-04-07 07:37:37.000000 eric_tools-1.2.5/eric_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 eric       (501) staff       (20)       34 2023-04-07 07:37:37.000000 eric_tools-1.2.5/eric_tools.egg-info/requires.txt
+-rw-r--r--   0 eric       (501) staff       (20)       11 2023-04-07 07:37:37.000000 eric_tools-1.2.5/eric_tools.egg-info/top_level.txt
+-rw-r--r--   0 eric       (501) staff       (20)        1 2023-04-07 07:37:37.000000 eric_tools-1.2.5/eric_tools.egg-info/dependency_links.txt
```

### Comparing `eric_tools-1.2.4.1/PKG-INFO` & `eric_tools-1.2.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eric_tools
-Version: 1.2.4.1
+Version: 1.2.5
 Summary: Python Daily Development Tools
 Home-page: https://github.com/Eric-jxl/Tools
 Author: Eric
 Author-email: jxleric95@gmail.com
 License: Apache License
 Description: # Tools
         [![License](https://img.shields.io/:license-apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
```

### Comparing `eric_tools-1.2.4.1/eric_tools/Abstract.py` & `eric_tools-1.2.5/eric_tools/Abstract.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/readconfig.py` & `eric_tools-1.2.5/eric_tools/readconfig.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/jwt_encrypt.py` & `eric_tools-1.2.5/eric_tools/jwt_encrypt.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/decorator.py` & `eric_tools-1.2.5/eric_tools/decorator.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/remove.py` & `eric_tools-1.2.5/eric_tools/remove.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/__init__.py` & `eric_tools-1.2.5/eric_tools/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,12 +17,12 @@
 import logger
 import resize_image
 import exception_class
 
 name = 'Eric-Tools'
 __title__ = 'tools'
 __description__ = 'Python HTTP for Humans.'
-__version__ = "1.2.4.1"
+__version__ = "1.2.5"
 __author__ = 'Eric'
 __doc__ = ["Python Daily Development Tools"]
 __url__ = "https://github.com/Eric-jxl/Tools"
 __license__ = "Apache"
```

### Comparing `eric_tools-1.2.4.1/eric_tools/pgsql.py` & `eric_tools-1.2.5/eric_tools/pgsql.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/convert_json.py` & `eric_tools-1.2.5/eric_tools/convert_json.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/encryption_classmethod.py` & `eric_tools-1.2.5/eric_tools/encryption_classmethod.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/logger.py` & `eric_tools-1.2.5/eric_tools/logger.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/ip.py` & `eric_tools-1.2.5/eric_tools/ip.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/exception_class.py` & `eric_tools-1.2.5/eric_tools/exception_class.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/send_email.py` & `eric_tools-1.2.5/eric_tools/send_email.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/eric_tools/resize_image.py` & `eric_tools-1.2.5/eric_tools/resize_image.py`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/README.md` & `eric_tools-1.2.5/README.md`

 * *Files identical despite different names*

### Comparing `eric_tools-1.2.4.1/setup.py` & `eric_tools-1.2.5/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="eric_tools",
-    version="1.2.4.1",
+    version="1.2.5",
     author="Eric",
     author_email="jxleric95@gmail.com",
     description="Python Daily Development Tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Eric-jxl/Tools",
     packages=setuptools.find_packages(),
```

### Comparing `eric_tools-1.2.4.1/eric_tools.egg-info/PKG-INFO` & `eric_tools-1.2.5/eric_tools.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eric-tools
-Version: 1.2.4.1
+Version: 1.2.5
 Summary: Python Daily Development Tools
 Home-page: https://github.com/Eric-jxl/Tools
 Author: Eric
 Author-email: jxleric95@gmail.com
 License: Apache License
 Description: # Tools
         [![License](https://img.shields.io/:license-apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
```

### Comparing `eric_tools-1.2.4.1/eric_tools.egg-info/SOURCES.txt` & `eric_tools-1.2.5/eric_tools.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 README.md
 setup.py
 eric_tools/Abstract.py
-eric_tools/BingDwenDwen.py
 eric_tools/__init__.py
 eric_tools/convert_json.py
 eric_tools/decorator.py
 eric_tools/encryption_classmethod.py
 eric_tools/exception_class.py
 eric_tools/ip.py
 eric_tools/jwt_encrypt.py
```

