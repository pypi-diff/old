# Comparing `tmp/neuromeka-clients-0.1.1.tar.gz` & `tmp/neuromeka-clients-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "neuromeka-clients-0.1.1.tar", last modified: Fri Apr  7 01:28:46 2023, max compression
+gzip compressed data, was "neuromeka-clients-0.1.2.tar", last modified: Fri Apr  7 10:01:14 2023, max compression
```

## Comparing `neuromeka-clients-0.1.1.tar` & `neuromeka-clients-0.1.2.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.878910 neuromeka-clients-0.1.1/
--rw-rw-rw-   0        0        0     2480 2023-04-07 01:28:46.876916 neuromeka-clients-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0     1199 2023-04-06 12:40:10.000000 neuromeka-clients-0.1.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.796133 neuromeka-clients-0.1.1/neuromeka/
--rw-rw-rw-   0        0        0      117 2023-04-06 23:37:07.000000 neuromeka-clients-0.1.1/neuromeka/__init__.py
--rw-rw-rw-   0        0        0     7442 2023-04-06 12:30:11.000000 neuromeka-clients-0.1.1/neuromeka/ecat.py
--rw-rw-rw-   0        0        0    10651 2023-04-06 11:41:45.000000 neuromeka-clients-0.1.1/neuromeka/indy.py
--rw-rw-rw-   0        0        0     6364 2023-04-06 11:41:51.000000 neuromeka-clients-0.1.1/neuromeka/moby.py
--rw-rw-rw-   0        0        0     3379 2023-04-06 11:41:58.000000 neuromeka-clients-0.1.1/neuromeka/motor.py
-drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.848990 neuromeka-clients-0.1.1/neuromeka/proto/
--rw-rw-rw-   0        0        0    65863 2023-04-04 06:23:00.000000 neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2.py
--rw-rw-rw-   0        0        0    61370 2023-04-06 12:15:44.000000 neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0    61466 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2.py
--rw-rw-rw-   0        0        0   128168 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2_grpc.py
--rw-rw-rw-   0        0        0    74988 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2.py
--rw-rw-rw-   0        0        0    54393 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0    41733 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2.py
--rw-rw-rw-   0        0        0    39460 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0        0 2023-04-06 12:35:30.000000 neuromeka-clients-0.1.1/neuromeka/proto/__init__.py
--rw-rw-rw-   0        0        0      519 2023-04-06 12:33:27.000000 neuromeka-clients-0.1.1/neuromeka/proto/grpc_wrapper.py
-drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.872926 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/
--rw-rw-rw-   0        0        0     2480 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      729 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       53 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 01:28:46.878910 neuromeka-clients-0.1.1/setup.cfg
--rw-rw-rw-   0        0        0     1121 2023-04-07 01:26:55.000000 neuromeka-clients-0.1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:01:14.529444 neuromeka-clients-0.1.2/
+-rw-rw-rw-   0        0        0     2126 2023-04-07 10:01:14.528469 neuromeka-clients-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0     1199 2023-04-06 12:40:10.000000 neuromeka-clients-0.1.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 10:01:14.425014 neuromeka-clients-0.1.2/neuromeka/
+-rw-rw-rw-   0        0        0      117 2023-04-06 23:37:07.000000 neuromeka-clients-0.1.2/neuromeka/__init__.py
+-rw-rw-rw-   0        0        0     7442 2023-04-06 12:30:11.000000 neuromeka-clients-0.1.2/neuromeka/ecat.py
+-rw-rw-rw-   0        0        0    10651 2023-04-06 11:41:45.000000 neuromeka-clients-0.1.2/neuromeka/indy.py
+-rw-rw-rw-   0        0        0     7394 2023-04-07 08:00:44.000000 neuromeka-clients-0.1.2/neuromeka/moby.py
+-rw-rw-rw-   0        0        0     3379 2023-04-06 11:41:58.000000 neuromeka-clients-0.1.2/neuromeka/motor.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:01:14.496263 neuromeka-clients-0.1.2/neuromeka/proto/
+-rw-rw-rw-   0        0        0    65863 2023-04-04 06:23:00.000000 neuromeka-clients-0.1.2/neuromeka/proto/EtherCATCommgRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    61370 2023-04-06 12:15:44.000000 neuromeka-clients-0.1.2/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0    61466 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.2/neuromeka/proto/IndygRPCTask_pb2.py
+-rw-rw-rw-   0        0        0   128168 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.2/neuromeka/proto/IndygRPCTask_pb2_grpc.py
+-rw-rw-rw-   0        0        0    74988 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.2/neuromeka/proto/MobygRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    54393 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.2/neuromeka/proto/MobygRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0    41733 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.2/neuromeka/proto/MotorControlgRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    39460 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.2/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0        0 2023-04-06 12:35:30.000000 neuromeka-clients-0.1.2/neuromeka/proto/__init__.py
+-rw-rw-rw-   0        0        0      519 2023-04-06 12:33:27.000000 neuromeka-clients-0.1.2/neuromeka/proto/grpc_wrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:01:14.523590 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/
+-rw-rw-rw-   0        0        0     2126 2023-04-07 10:01:14.000000 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      729 2023-04-07 10:01:14.000000 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 10:01:14.000000 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-04-07 10:01:14.000000 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-07 10:01:14.000000 neuromeka-clients-0.1.2/neuromeka_clients.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 10:01:14.529444 neuromeka-clients-0.1.2/setup.cfg
+-rw-rw-rw-   0        0        0     1221 2023-04-07 10:00:12.000000 neuromeka-clients-0.1.2/setup.py
```

### Comparing `neuromeka-clients-0.1.1/PKG-INFO` & `neuromeka-clients-0.1.2/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,72 +1,72 @@
 Metadata-Version: 2.1
 Name: neuromeka-clients
-Version: 0.1.1
+Version: 0.1.2
 Summary: Neuromeka client protocols for Indy, Moby, Ecat, and Motor
 Home-page: https://github.com/neuromeka-robotics/neuromeka-clients
 Author: Your Name
 Author-email: youngjin.heo@neuromeka.com
-License: UNKNOWN
-Description: # Neuromeka Clients
-        
-        This package provides client protocols for users to interact with Neuromeka's products, including Indy, Moby, Ecat, and Motor.
-        
-        ## Installation
-        
-        You can install the package from PyPI:
-        
-        ```bash
-        pip install neuromeka-clients
-        ```
-        
-        ## Usage
-        The package contatins the following client classes:
-        
-        * IndyClient in indy.py
-        * MobyClient in moby.py
-        * EcatClient in ecat.py
-        * MotorClient in motor.py
-        
-        To use a client class, simply import it and create an instance:
-        
-        ```python
-        from neuromeka.ecat import EcatClient
-        
-        ecat_client = EcatClient("192.168.214.20")
-        ```
-        
-        Replace EcatClient with the desired client class and the IP address with the appropriate address for your device.
-        
-        ## Dependencies
-        This package requires the following dependencies:
-        
-        * grpcio
-        * grpcio-tools
-        * protobuf
-        * six
-        
-        These dependencies will be automatically installed when you install the package using pip.
-        
-        ## Examples
-        Please refer to the 'example.py' file in the package for usage examples.
-        
-        ## Support
-        If you encounter any issues or need help, please open an issue on the project's repository.
-        
-        ## License
-        This package is released under the [LICENSE_NAME]. For more information, please refer to the LICENSE file.
-        
-        
-        
-        
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+
+# Neuromeka Clients
+
+This package provides client protocols for users to interact with Neuromeka's products, including Indy, Moby, Ecat, and Motor.
+
+## Installation
+
+You can install the package from PyPI:
+
+```bash
+pip install neuromeka-clients
+```
+
+## Usage
+The package contatins the following client classes:
+
+* IndyClient in indy.py
+* MobyClient in moby.py
+* EcatClient in ecat.py
+* MotorClient in motor.py
+
+To use a client class, simply import it and create an instance:
+
+```python
+from neuromeka.ecat import EcatClient
+
+ecat_client = EcatClient("192.168.214.20")
+```
+
+Replace EcatClient with the desired client class and the IP address with the appropriate address for your device.
+
+## Dependencies
+This package requires the following dependencies:
+
+* grpcio
+* grpcio-tools
+* protobuf
+* six
+
+These dependencies will be automatically installed when you install the package using pip.
+
+## Examples
+Please refer to the 'example.py' file in the package for usage examples.
+
+## Support
+If you encounter any issues or need help, please open an issue on the project's repository.
+
+## License
+This package is released under the [LICENSE_NAME]. For more information, please refer to the LICENSE file.
+
+
+
```

### Comparing `neuromeka-clients-0.1.1/README.md` & `neuromeka-clients-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/ecat.py` & `neuromeka-clients-0.1.2/neuromeka/ecat.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/indy.py` & `neuromeka-clients-0.1.2/neuromeka/indy.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/motor.py` & `neuromeka-clients-0.1.2/neuromeka/motor.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2.py` & `neuromeka-clients-0.1.2/neuromeka/proto/EtherCATCommgRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.2/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2.py` & `neuromeka-clients-0.1.2/neuromeka/proto/IndygRPCTask_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2_grpc.py` & `neuromeka-clients-0.1.2/neuromeka/proto/IndygRPCTask_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2.py` & `neuromeka-clients-0.1.2/neuromeka/proto/MobygRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.2/neuromeka/proto/MobygRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2.py` & `neuromeka-clients-0.1.2/neuromeka/proto/MotorControlgRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.2/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka/proto/grpc_wrapper.py` & `neuromeka-clients-0.1.2/neuromeka/proto/grpc_wrapper.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/neuromeka_clients.egg-info/PKG-INFO` & `neuromeka-clients-0.1.2/neuromeka_clients.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,72 +1,72 @@
 Metadata-Version: 2.1
 Name: neuromeka-clients
-Version: 0.1.1
+Version: 0.1.2
 Summary: Neuromeka client protocols for Indy, Moby, Ecat, and Motor
 Home-page: https://github.com/neuromeka-robotics/neuromeka-clients
 Author: Your Name
 Author-email: youngjin.heo@neuromeka.com
-License: UNKNOWN
-Description: # Neuromeka Clients
-        
-        This package provides client protocols for users to interact with Neuromeka's products, including Indy, Moby, Ecat, and Motor.
-        
-        ## Installation
-        
-        You can install the package from PyPI:
-        
-        ```bash
-        pip install neuromeka-clients
-        ```
-        
-        ## Usage
-        The package contatins the following client classes:
-        
-        * IndyClient in indy.py
-        * MobyClient in moby.py
-        * EcatClient in ecat.py
-        * MotorClient in motor.py
-        
-        To use a client class, simply import it and create an instance:
-        
-        ```python
-        from neuromeka.ecat import EcatClient
-        
-        ecat_client = EcatClient("192.168.214.20")
-        ```
-        
-        Replace EcatClient with the desired client class and the IP address with the appropriate address for your device.
-        
-        ## Dependencies
-        This package requires the following dependencies:
-        
-        * grpcio
-        * grpcio-tools
-        * protobuf
-        * six
-        
-        These dependencies will be automatically installed when you install the package using pip.
-        
-        ## Examples
-        Please refer to the 'example.py' file in the package for usage examples.
-        
-        ## Support
-        If you encounter any issues or need help, please open an issue on the project's repository.
-        
-        ## License
-        This package is released under the [LICENSE_NAME]. For more information, please refer to the LICENSE file.
-        
-        
-        
-        
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+
+# Neuromeka Clients
+
+This package provides client protocols for users to interact with Neuromeka's products, including Indy, Moby, Ecat, and Motor.
+
+## Installation
+
+You can install the package from PyPI:
+
+```bash
+pip install neuromeka-clients
+```
+
+## Usage
+The package contatins the following client classes:
+
+* IndyClient in indy.py
+* MobyClient in moby.py
+* EcatClient in ecat.py
+* MotorClient in motor.py
+
+To use a client class, simply import it and create an instance:
+
+```python
+from neuromeka.ecat import EcatClient
+
+ecat_client = EcatClient("192.168.214.20")
+```
+
+Replace EcatClient with the desired client class and the IP address with the appropriate address for your device.
+
+## Dependencies
+This package requires the following dependencies:
+
+* grpcio
+* grpcio-tools
+* protobuf
+* six
+
+These dependencies will be automatically installed when you install the package using pip.
+
+## Examples
+Please refer to the 'example.py' file in the package for usage examples.
+
+## Support
+If you encounter any issues or need help, please open an issue on the project's repository.
+
+## License
+This package is released under the [LICENSE_NAME]. For more information, please refer to the LICENSE file.
+
+
+
```

### Comparing `neuromeka-clients-0.1.1/neuromeka_clients.egg-info/SOURCES.txt` & `neuromeka-clients-0.1.2/neuromeka_clients.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.1/setup.py` & `neuromeka-clients-0.1.2/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name="neuromeka-clients",
-    version="0.1.1",
+    version="0.1.2",
     author="Your Name",
     author_email="youngjin.heo@neuromeka.com",
     description="Neuromeka client protocols for Indy, Moby, Ecat, and Motor",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/neuromeka-robotics/neuromeka-clients",
     packages=find_packages(),
@@ -19,14 +19,16 @@
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
     ],
     python_requires=">=3.6",
     install_requires=[
         "grpcio==1.39.0",
         "grpcio-tools==1.39.0",
         "protobuf==3.17.3"
     ],
```

