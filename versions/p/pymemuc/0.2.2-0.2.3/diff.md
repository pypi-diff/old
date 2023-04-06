# Comparing `tmp/pymemuc-0.2.2.tar.gz` & `tmp/pymemuc-0.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymemuc-0.2.2.tar", max compression
+gzip compressed data, was "pymemuc-0.2.3.tar", max compression
```

## Comparing `pymemuc-0.2.2.tar` & `pymemuc-0.2.3.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0     1057 2023-04-06 02:44:51.742951 pymemuc-0.2.2/LICENSE
--rw-r--r--   0        0        0     1577 2023-04-06 02:44:51.742951 pymemuc-0.2.2/README.md
--rw-r--r--   0        0        0      386 2023-04-06 02:44:51.742951 pymemuc-0.2.2/pymemuc/__init__.py
--rw-r--r--   0        0        0    22468 2023-04-06 02:44:51.742951 pymemuc-0.2.2/pymemuc/_command.py
--rw-r--r--   0        0        0      465 2023-04-06 02:44:51.742951 pymemuc-0.2.2/pymemuc/_constants.py
--rw-r--r--   0        0        0     4941 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/_control.py
--rw-r--r--   0        0        0     1150 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/_decorators.py
--rw-r--r--   0        0        0    12399 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/_manage.py
--rw-r--r--   0        0        0     3937 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/_memuc.py
--rw-r--r--   0        0        0      891 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/exceptions.py
--rw-r--r--   0        0        0     2194 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/pymemuc.py
--rw-r--r--   0        0        0      379 2023-04-06 02:44:51.746951 pymemuc-0.2.2/pymemuc/vminfo.py
--rw-r--r--   0        0        0     1632 2023-04-06 02:45:09.599182 pymemuc-0.2.2/pyproject.toml
--rw-r--r--   0        0        0     2479 1970-01-01 00:00:00.000000 pymemuc-0.2.2/PKG-INFO
+-rw-r--r--   0        0        0     1057 2023-04-06 21:52:46.040773 pymemuc-0.2.3/LICENSE
+-rw-r--r--   0        0        0     1577 2023-04-06 21:52:46.040773 pymemuc-0.2.3/README.md
+-rw-r--r--   0        0        0      386 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/__init__.py
+-rw-r--r--   0        0        0    22468 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_command.py
+-rw-r--r--   0        0        0      465 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_constants.py
+-rw-r--r--   0        0        0     4941 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_control.py
+-rw-r--r--   0        0        0     1150 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_decorators.py
+-rw-r--r--   0        0        0    12559 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_manage.py
+-rw-r--r--   0        0        0     3937 2023-04-06 21:52:46.040773 pymemuc-0.2.3/pymemuc/_memuc.py
+-rw-r--r--   0        0        0      891 2023-04-06 21:52:46.044774 pymemuc-0.2.3/pymemuc/exceptions.py
+-rw-r--r--   0        0        0     2194 2023-04-06 21:52:46.044774 pymemuc-0.2.3/pymemuc/pymemuc.py
+-rw-r--r--   0        0        0      379 2023-04-06 21:52:46.044774 pymemuc-0.2.3/pymemuc/vminfo.py
+-rw-r--r--   0        0        0     1632 2023-04-06 21:53:05.444241 pymemuc-0.2.3/pyproject.toml
+-rw-r--r--   0        0        0     2479 1970-01-01 00:00:00.000000 pymemuc-0.2.3/PKG-INFO
```

### Comparing `pymemuc-0.2.2/LICENSE` & `pymemuc-0.2.3/LICENSE`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/README.md` & `pymemuc-0.2.3/README.md`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/_command.py` & `pymemuc-0.2.3/pymemuc/_command.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/_control.py` & `pymemuc-0.2.3/pymemuc/_control.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/_decorators.py` & `pymemuc-0.2.3/pymemuc/_decorators.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/_manage.py` & `pymemuc-0.2.3/pymemuc/_manage.py`

 * *Files 2% similar despite different names*

```diff
@@ -229,14 +229,19 @@
             ]
         )
     else:
         _, output = self.memuc_run(
             ["listvms", "-r" if running else "", "-s" if disk_info else ""]
         )
 
+    # handle when no VMs are on the system
+    # memuc.exe will output a "read failed" error
+    if "read failed" in output:
+        return []
+
     output = output.split("\n")
     parsed_output = []
 
     # parse the output into a list of dictionaries representing the VMs
     # output will contain a list of vm values seperated by commas
     # if disk_info is True, each vm will have 6 values, otherwise 5
     for vm_str in output:
@@ -268,15 +273,16 @@
 
 
 def get_configuration_vm(
     self: "PyMemuc", config_key, vm_index: int | None = None, vm_name: str | None = None
 ) -> str:
     """Get a VM configuration, must specify either a vm index or a vm name
 
-    :param config_key: Configuration key, keys are noted in `configuration keys table <https://pymemuc.readthedocs.io/pymemuc.html#the-vm-configuration-keys-table>`_
+    :param config_key: Configuration key, keys are noted in `configuration keys table
+        <https://pymemuc.readthedocs.io/pymemuc.html#the-vm-configuration-keys-table>`_
     :type config_key: str
     :param vm_index: VM index. Defaults to None.
     :type vm_index: int, optional
     :param vm_name: VM name. Defaults to None.
     :type vm_name: str, optional
     :raises PyMemucIndexError: an error if neither a vm index or a vm name is specified
     :return: The configuration value
@@ -301,15 +307,16 @@
     config_key: str,
     config_value: str,
     vm_index: int | None = None,
     vm_name: str | None = None,
 ) -> Literal[True]:
     """Set a VM configuration, must specify either a vm index or a vm name
 
-    :param config_key: Configuration key, keys are noted in `configuration keys table <https://pymemuc.readthedocs.io/pymemuc.html#the-vm-configuration-keys-table>`_
+    :param config_key: Configuration key, keys are noted in `configuration keys table
+        <https://pymemuc.readthedocs.io/pymemuc.html#the-vm-configuration-keys-table>`_
     :type config_key: str
     :param config_value: Configuration value
     :type config_value: str
     :param vm_index: VM index. Defaults to None.
     :type vm_index: int, optional
     :param vm_name: VM name. Defaults to None.
     :type vm_name: str, optional
```

### Comparing `pymemuc-0.2.2/pymemuc/_memuc.py` & `pymemuc-0.2.3/pymemuc/_memuc.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/exceptions.py` & `pymemuc-0.2.3/pymemuc/exceptions.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pymemuc/pymemuc.py` & `pymemuc-0.2.3/pymemuc/pymemuc.py`

 * *Files identical despite different names*

### Comparing `pymemuc-0.2.2/pyproject.toml` & `pymemuc-0.2.3/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "pymemuc"
-version = "v0.2.2"
+version = "v0.2.3"
 description = "A Memuc.exe wrapper for Python"
 readme = "README.md"
 authors = ["Martin Miglio <code@martinmiglio.dev>"]
 license = "MIT"
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
```

### Comparing `pymemuc-0.2.2/PKG-INFO` & `pymemuc-0.2.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymemuc
-Version: 0.2.2
+Version: 0.2.3
 Summary: A Memuc.exe wrapper for Python
 Home-page: https://github.com/marmig0404/pymemuc
 License: MIT
 Keywords: memu,memuc,wrapper,api
 Author: Martin Miglio
 Author-email: code@martinmiglio.dev
 Requires-Python: >=3.8,<4.0
```

