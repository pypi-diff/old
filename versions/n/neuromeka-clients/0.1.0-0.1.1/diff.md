# Comparing `tmp/neuromeka-clients-0.1.0.tar.gz` & `tmp/neuromeka-clients-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "neuromeka-clients-0.1.0.tar", last modified: Thu Apr  6 23:45:12 2023, max compression
+gzip compressed data, was "neuromeka-clients-0.1.1.tar", last modified: Fri Apr  7 01:28:46 2023, max compression
```

## Comparing `neuromeka-clients-0.1.0.tar` & `neuromeka-clients-0.1.1.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 23:45:12.145021 neuromeka-clients-0.1.0/
--rw-rw-rw-   0        0        0     2480 2023-04-06 23:45:12.143027 neuromeka-clients-0.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     1199 2023-04-06 12:40:10.000000 neuromeka-clients-0.1.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 23:45:12.041408 neuromeka-clients-0.1.0/neuromeka/
--rw-rw-rw-   0        0        0      117 2023-04-06 23:37:07.000000 neuromeka-clients-0.1.0/neuromeka/__init__.py
--rw-rw-rw-   0        0        0     7442 2023-04-06 12:30:11.000000 neuromeka-clients-0.1.0/neuromeka/ecat.py
--rw-rw-rw-   0        0        0    10651 2023-04-06 11:41:45.000000 neuromeka-clients-0.1.0/neuromeka/indy.py
--rw-rw-rw-   0        0        0     6364 2023-04-06 11:41:51.000000 neuromeka-clients-0.1.0/neuromeka/moby.py
--rw-rw-rw-   0        0        0     3379 2023-04-06 11:41:58.000000 neuromeka-clients-0.1.0/neuromeka/motor.py
-drwxrwxrwx   0        0        0        0 2023-04-06 23:45:12.113108 neuromeka-clients-0.1.0/neuromeka/proto/
--rw-rw-rw-   0        0        0    65863 2023-04-04 06:23:00.000000 neuromeka-clients-0.1.0/neuromeka/proto/EtherCATCommgRPCServer_pb2.py
--rw-rw-rw-   0        0        0    61370 2023-04-06 12:15:44.000000 neuromeka-clients-0.1.0/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0    61466 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.0/neuromeka/proto/IndygRPCTask_pb2.py
--rw-rw-rw-   0        0        0   128168 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.0/neuromeka/proto/IndygRPCTask_pb2_grpc.py
--rw-rw-rw-   0        0        0    74988 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.0/neuromeka/proto/MobygRPCServer_pb2.py
--rw-rw-rw-   0        0        0    54393 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.0/neuromeka/proto/MobygRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0    41733 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.0/neuromeka/proto/MotorControlgRPCServer_pb2.py
--rw-rw-rw-   0        0        0    39460 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.0/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py
--rw-rw-rw-   0        0        0        0 2023-04-06 12:35:30.000000 neuromeka-clients-0.1.0/neuromeka/proto/__init__.py
--rw-rw-rw-   0        0        0      519 2023-04-06 12:33:27.000000 neuromeka-clients-0.1.0/neuromeka/proto/grpc_wrapper.py
-drwxrwxrwx   0        0        0        0 2023-04-06 23:45:12.138040 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/
--rw-rw-rw-   0        0        0     2480 2023-04-06 23:45:11.000000 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      729 2023-04-06 23:45:11.000000 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 23:45:11.000000 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       53 2023-04-06 23:45:11.000000 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-04-06 23:45:11.000000 neuromeka-clients-0.1.0/neuromeka_clients.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 23:45:12.145021 neuromeka-clients-0.1.0/setup.cfg
--rw-rw-rw-   0        0        0     1121 2023-04-06 23:16:27.000000 neuromeka-clients-0.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.878910 neuromeka-clients-0.1.1/
+-rw-rw-rw-   0        0        0     2480 2023-04-07 01:28:46.876916 neuromeka-clients-0.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     1199 2023-04-06 12:40:10.000000 neuromeka-clients-0.1.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.796133 neuromeka-clients-0.1.1/neuromeka/
+-rw-rw-rw-   0        0        0      117 2023-04-06 23:37:07.000000 neuromeka-clients-0.1.1/neuromeka/__init__.py
+-rw-rw-rw-   0        0        0     7442 2023-04-06 12:30:11.000000 neuromeka-clients-0.1.1/neuromeka/ecat.py
+-rw-rw-rw-   0        0        0    10651 2023-04-06 11:41:45.000000 neuromeka-clients-0.1.1/neuromeka/indy.py
+-rw-rw-rw-   0        0        0     6364 2023-04-06 11:41:51.000000 neuromeka-clients-0.1.1/neuromeka/moby.py
+-rw-rw-rw-   0        0        0     3379 2023-04-06 11:41:58.000000 neuromeka-clients-0.1.1/neuromeka/motor.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.848990 neuromeka-clients-0.1.1/neuromeka/proto/
+-rw-rw-rw-   0        0        0    65863 2023-04-04 06:23:00.000000 neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    61370 2023-04-06 12:15:44.000000 neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0    61466 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2.py
+-rw-rw-rw-   0        0        0   128168 2023-03-16 08:41:07.000000 neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2_grpc.py
+-rw-rw-rw-   0        0        0    74988 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    54393 2023-04-04 06:23:04.000000 neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0    41733 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2.py
+-rw-rw-rw-   0        0        0    39460 2023-04-04 06:23:10.000000 neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py
+-rw-rw-rw-   0        0        0        0 2023-04-06 12:35:30.000000 neuromeka-clients-0.1.1/neuromeka/proto/__init__.py
+-rw-rw-rw-   0        0        0      519 2023-04-06 12:33:27.000000 neuromeka-clients-0.1.1/neuromeka/proto/grpc_wrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:28:46.872926 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/
+-rw-rw-rw-   0        0        0     2480 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      729 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-07 01:28:46.000000 neuromeka-clients-0.1.1/neuromeka_clients.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 01:28:46.878910 neuromeka-clients-0.1.1/setup.cfg
+-rw-rw-rw-   0        0        0     1121 2023-04-07 01:26:55.000000 neuromeka-clients-0.1.1/setup.py
```

### Comparing `neuromeka-clients-0.1.0/PKG-INFO` & `neuromeka-clients-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: neuromeka-clients
-Version: 0.1.0
+Version: 0.1.1
 Summary: Neuromeka client protocols for Indy, Moby, Ecat, and Motor
 Home-page: https://github.com/neuromeka-robotics/neuromeka-clients
 Author: Your Name
 Author-email: youngjin.heo@neuromeka.com
 License: UNKNOWN
 Description: # Neuromeka Clients
```

### Comparing `neuromeka-clients-0.1.0/README.md` & `neuromeka-clients-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/ecat.py` & `neuromeka-clients-0.1.1/neuromeka/ecat.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/indy.py` & `neuromeka-clients-0.1.1/neuromeka/indy.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/moby.py` & `neuromeka-clients-0.1.1/neuromeka/moby.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/motor.py` & `neuromeka-clients-0.1.1/neuromeka/motor.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/EtherCATCommgRPCServer_pb2.py` & `neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.1/neuromeka/proto/EtherCATCommgRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/IndygRPCTask_pb2.py` & `neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/IndygRPCTask_pb2_grpc.py` & `neuromeka-clients-0.1.1/neuromeka/proto/IndygRPCTask_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/MobygRPCServer_pb2.py` & `neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/MobygRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.1/neuromeka/proto/MobygRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/MotorControlgRPCServer_pb2.py` & `neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py` & `neuromeka-clients-0.1.1/neuromeka/proto/MotorControlgRPCServer_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka/proto/grpc_wrapper.py` & `neuromeka-clients-0.1.1/neuromeka/proto/grpc_wrapper.py`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/neuromeka_clients.egg-info/PKG-INFO` & `neuromeka-clients-0.1.1/neuromeka_clients.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: neuromeka-clients
-Version: 0.1.0
+Version: 0.1.1
 Summary: Neuromeka client protocols for Indy, Moby, Ecat, and Motor
 Home-page: https://github.com/neuromeka-robotics/neuromeka-clients
 Author: Your Name
 Author-email: youngjin.heo@neuromeka.com
 License: UNKNOWN
 Description: # Neuromeka Clients
```

### Comparing `neuromeka-clients-0.1.0/neuromeka_clients.egg-info/SOURCES.txt` & `neuromeka-clients-0.1.1/neuromeka_clients.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `neuromeka-clients-0.1.0/setup.py` & `neuromeka-clients-0.1.1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name="neuromeka-clients",
-    version="0.1.0",
+    version="0.1.1",
     author="Your Name",
     author_email="youngjin.heo@neuromeka.com",
     description="Neuromeka client protocols for Indy, Moby, Ecat, and Motor",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/neuromeka-robotics/neuromeka-clients",
     packages=find_packages(),
@@ -22,12 +22,12 @@
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
     ],
     python_requires=">=3.6",
     install_requires=[
-        "grpcio==1.51.3",
-        "grpcio-tools==1.51.3",
+        "grpcio==1.39.0",
+        "grpcio-tools==1.39.0",
         "protobuf==3.17.3"
     ],
 )
```

