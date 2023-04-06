# Comparing `tmp/durin-0.0.72.tar.gz` & `tmp/durin-0.0.73.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "durin-0.0.72.tar", last modified: Sat Mar 18 17:34:55 2023, max compression
+gzip compressed data, was "durin-0.0.73.tar", last modified: Thu Apr  6 13:07:03 2023, max compression
```

## Comparing `durin-0.0.72.tar` & `durin-0.0.73.tar`

### file list

```diff
@@ -1,45 +1,50 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.410679 durin-0.0.72/
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-18 17:34:44.000000 durin-0.0.72/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-03-18 17:34:55.410679 durin-0.0.72/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (123)     2683 2023-03-18 17:34:44.000000 durin-0.0.72/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.406679 durin-0.0.72/bin/
--rwxr-xr-x   0 runner    (1001) docker     (123)       34 2023-03-18 17:34:44.000000 durin-0.0.72/bin/durin
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.406679 durin-0.0.72/durin/
--rwxr-xr-x   0 runner    (1001) docker     (123)      124 2023-03-18 17:34:44.000000 durin-0.0.72/durin/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      475 2023-03-18 17:34:44.000000 durin-0.0.72/durin/__main__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      766 2023-03-18 17:34:44.000000 durin-0.0.72/durin/actuator.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4148 2023-03-18 17:34:44.000000 durin-0.0.72/durin/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.410679 durin-0.0.72/durin/controller/
--rwxr-xr-x   0 runner    (1001) docker     (123)       40 2023-03-18 17:34:44.000000 durin-0.0.72/durin/controller/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      344 2023-03-18 17:34:44.000000 durin-0.0.72/durin/controller/dvs.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4307 2023-03-18 17:34:44.000000 durin-0.0.72/durin/controller/server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.410679 durin-0.0.72/durin/controller/test/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:44.000000 durin-0.0.72/durin/controller/test/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      947 2023-03-18 17:34:44.000000 durin-0.0.72/durin/controller/test/test_stream.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4694 2023-03-18 17:34:44.000000 durin-0.0.72/durin/durin.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      504 2023-03-18 17:34:44.000000 durin-0.0.72/durin/dvs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.410679 durin-0.0.72/durin/examples/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2281 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/braitenberg.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2631 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/commands.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1208 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/dashboard.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      958 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/main.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      589 2023-03-18 17:34:44.000000 durin-0.0.72/durin/examples/record.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.410679 durin-0.0.72/durin/io/
--rwxr-xr-x   0 runner    (1001) docker     (123)      673 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4572 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/command.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1442 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/gamepad.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     6206 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/network.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      525 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/ringbuffer.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1824 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/runnable.py
--rw-r--r--   0 runner    (1001) docker     (123)     8853 2023-03-18 17:34:44.000000 durin-0.0.72/durin/io/schema.capnp
--rwxr-xr-x   0 runner    (1001) docker     (123)     6686 2023-03-18 17:34:44.000000 durin-0.0.72/durin/sensor.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     9565 2023-03-18 17:34:44.000000 durin-0.0.72/durin/ui.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 17:34:55.406679 durin-0.0.72/durin.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-03-18 17:34:55.000000 durin-0.0.72/durin.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      765 2023-03-18 17:34:55.000000 durin-0.0.72/durin.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-18 17:34:55.000000 durin-0.0.72/durin.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       66 2023-03-18 17:34:55.000000 durin-0.0.72/durin.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-18 17:34:55.000000 durin-0.0.72/durin.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-18 17:34:55.410679 durin-0.0.72/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)      674 2023-03-18 17:34:44.000000 durin-0.0.72/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.053076 durin-0.0.73/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 13:06:51.000000 durin-0.0.73/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-04-06 13:07:03.053076 durin-0.0.73/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2683 2023-04-06 13:06:51.000000 durin-0.0.73/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.045076 durin-0.0.73/bin/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       34 2023-04-06 13:06:51.000000 durin-0.0.73/bin/durin
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.049076 durin-0.0.73/durin/
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-04-06 13:06:51.000000 durin-0.0.73/durin/Profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-06 13:06:51.000000 durin-0.0.73/durin/Read_profilers.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)       80 2023-04-06 13:06:51.000000 durin-0.0.73/durin/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      475 2023-04-06 13:06:51.000000 durin-0.0.73/durin/__main__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      766 2023-04-06 13:06:51.000000 durin-0.0.73/durin/actuator.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4148 2023-04-06 13:06:51.000000 durin-0.0.73/durin/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.049076 durin-0.0.73/durin/controller/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       40 2023-04-06 13:06:51.000000 durin-0.0.73/durin/controller/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      344 2023-04-06 13:06:51.000000 durin-0.0.73/durin/controller/dvs.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4307 2023-04-06 13:06:51.000000 durin-0.0.73/durin/controller/server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.049076 durin-0.0.73/durin/controller/test/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:06:51.000000 durin-0.0.73/durin/controller/test/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      947 2023-04-06 13:06:51.000000 durin-0.0.73/durin/controller/test/test_stream.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4694 2023-04-06 13:06:51.000000 durin-0.0.73/durin/durin.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)   181742 2023-04-06 13:06:51.000000 durin-0.0.73/durin/durin_birdseye.jpg
+-rwxr-xr-x   0 runner    (1001) docker     (123)      504 2023-04-06 13:06:51.000000 durin-0.0.73/durin/dvs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.053076 durin-0.0.73/durin/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/CPU_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2281 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/braitenberg.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2631 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/commands.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1459 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/dashboard.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      923 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/main.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      589 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/record.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1972 2023-04-06 13:06:51.000000 durin-0.0.73/durin/examples/stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.053076 durin-0.0.73/durin/io/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      673 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4815 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/command.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1442 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/gamepad.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6181 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/network.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      525 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/ringbuffer.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1824 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/runnable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8932 2023-04-06 13:06:51.000000 durin-0.0.73/durin/io/schema.capnp
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6844 2023-04-06 13:06:51.000000 durin-0.0.73/durin/sensor.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    12157 2023-04-06 13:06:51.000000 durin-0.0.73/durin/ui.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:07:03.049076 durin-0.0.73/durin.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-04-06 13:07:03.000000 durin-0.0.73/durin.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      883 2023-04-06 13:07:03.000000 durin-0.0.73/durin.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:07:03.000000 durin-0.0.73/durin.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 13:07:03.000000 durin-0.0.73/durin.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 13:07:03.000000 durin-0.0.73/durin.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:07:03.053076 durin-0.0.73/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)      663 2023-04-06 13:06:51.000000 durin-0.0.73/setup.py
```

### Comparing `durin-0.0.72/PKG-INFO` & `durin-0.0.73/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: durin
-Version: 0.0.72
+Version: 0.0.73
 Summary: Python control interface for the Durin robot
 Maintainer: Jens E. Pedersen
 Maintainer-email: jeped@kth.se
 License: LGPLv3
 Description-Content-Type: text/markdown
 Provides-Extra: aestream
```

### Comparing `durin-0.0.72/README.md` & `durin-0.0.73/README.md`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/actuator.py` & `durin-0.0.73/durin/actuator.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/cli.py` & `durin-0.0.73/durin/cli.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/controller/server.py` & `durin-0.0.73/durin/controller/server.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/controller/test/test_stream.py` & `durin-0.0.73/durin/controller/test/test_stream.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/durin.py` & `durin-0.0.73/durin/durin.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/examples/braitenberg.py` & `durin-0.0.73/durin/examples/braitenberg.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/examples/commands.py` & `durin-0.0.73/durin/examples/commands.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/examples/record.py` & `durin-0.0.73/durin/examples/record.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/io/__init__.py` & `durin-0.0.73/durin/io/__init__.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/io/command.py` & `durin-0.0.73/durin/io/command.py`

 * *Files 4% similar despite different names*

```diff
@@ -146,16 +146,25 @@
         self.port = port
 
     def encode(self):
         enable_message = schema.EnableStreaming.new_message()
         udpOnly = enable_message.destination.init("udpOnly")
         udpOnly.ip = list(map(lambda x: int(x), self.host.split(".")))
         udpOnly.port = self.port
-        return _wrap_base(enable_message, "enableStreaming")
+        return _wrap_base(enable_message, "enableStreaming")   
 
 
 class StreamOff(Command):
     def __init__(self):
         self.cmd_id = 19
 
     def encode(self):
         return _wrap_base(schema.DisableStreaming.new_message(), "disableStreaming")
+
+
+class GetSystemInfo(Command):
+    """ Returns IP address, MAC address, and Durin ID """
+    def __init__(self):
+        self.cmd_id = 20
+
+    def encode(self):
+        return _wrap_base(schema.GetSystemInfo.new_message(), "getSystemInfo")
```

### Comparing `durin-0.0.72/durin/io/gamepad.py` & `durin-0.0.73/durin/io/gamepad.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/io/network.py` & `durin-0.0.73/durin/io/network.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         self.receiver.stop()
         logging.debug(f"TCP control communication stopped")
 
     def send(self, command: ByteString, timeout: float) -> None:
         try:
             self.buffer_send.put(command, block=False, timeout=timeout)
         except Full:
-            print("hej")
             return None
 
     def read(self) -> Optional[ByteString]:
         try:
             return self.buffer_receive.get(block=False)
         except Empty:
             return None
```

### Comparing `durin-0.0.72/durin/io/ringbuffer.py` & `durin-0.0.73/durin/io/ringbuffer.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/io/runnable.py` & `durin-0.0.73/durin/io/runnable.py`

 * *Files identical despite different names*

### Comparing `durin-0.0.72/durin/io/schema.capnp` & `durin-0.0.73/durin/io/schema.capnp`

 * *Files 1% similar despite different names*

```diff
@@ -49,14 +49,17 @@
         setWifiConfig @24 :SetWifiConfig;
         setNodeId @25 :SetNodeId;
         textLogging @26 :TextLogging;
         otaUpdateCommit @27 :OtaUpdateCommit;
         otaUpdate @28 :OtaUpdate;
         enableLogging @29 :EnableLogging;
         otaUpdateBegin @30 :OtaUpdateBegin;
+
+        getSystemInfo @33 :GetSystemInfo;
+        systemInfo @34 :SystemInfo;
     }
 }
 
 # Response signifying that the previous message was invalid or ignored
 struct Reject {
 
 }
```

### Comparing `durin-0.0.72/durin/sensor.py` & `durin-0.0.73/durin/sensor.py`

 * *Files 6% similar despite different names*

```diff
@@ -140,14 +140,17 @@
     ):
         which = item.which()
 
         try:
             if which == "tofObservations":
                 for obs in item.tofObservations.observations:
                     data = np.array(obs.ranges)
+                    data = data & 0b0011111111111111
+                    # TODO use the status bytes
+                    # status = data & 0b1100000000000000
                     tof.get_obj()[obs.id * 64: (obs.id+1) * 64] = data
                 self._update_frequency(tof_ringbuffer, tof_ringbuffer_idx)
 
 
             elif which == "systemStatus":
                 voltage.value = item.systemStatus.batteryMv
                 charge.value = item.systemStatus.batteryPercent
```

### Comparing `durin-0.0.72/durin/ui.py` & `durin-0.0.73/durin/ui.py`

 * *Files 15% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 import time
 
 import numpy as np
 from durin.actuator import Move
 
 from durin.durin import Durin
 from durin.io.gamepad import Gamepad
-import durin
+from durin import SetSensorPeriod, GetSystemInfo
 
 
 # Constants
 surface_width = 200
 surface_height = 200
 sleep_interval = 0.02
 
@@ -31,70 +31,81 @@
 ]
 
 SENSOR_ROTATIONS = [180, 180+45, -90, 180-45, 90, 45, -45, 0]
 
 # A distance (in % of screen size) constant related to the layout.
 d= 0.02
 x=0.68
+y0 = 0.1
 
-TITLE_PLACEMENT = (x, 0.1)
+TITLE_PLACEMENT = (x, 0.05)
+
+INSTR_PLACEMENT = (x, 0.05+2*d)          # Keyboard instruction (static text)
 
 IP_PLACEMENT = (x, 0.1 + 3* d)
 
 BATTERY_PLACEMENT = (x,0.1 + 8*d)
 
-IMU_PLACEMENT = (x+2*d, 0.1 +14*d)  # Upper left corner
+IMU_PLACEMENT = (x, 0.1 +11*d)  # Upper left corner
 
-IMU_INTEG_PLACEMENT = (x, 0.1 + 19*d)
+IMU_INTEG_PLACEMENT = (x, 0.1 + 17*d)
 
-POSITION_PLACEMENT = [(x,0.1+26*d), (x+2*d,0.1+26*d), (x+ 4*d, 0.1+26*d)]
+POSITION_PLACEMENT = (x,0.1+21*d)
 
-UWB_PLACEMENT = (x, 0.1+32*d)              # Upper left corner
+MV_CMD_PLACEMENT = (x+7*d,0.1+21*d)         # Movement command placement
 
+UWB_PLACEMENT = (x, 0.1+25*d)              # Upper left corner
 
 
 
 
 class DurinUI(Durin):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.gamepad = Gamepad()
 
+        self.ip = None
+        self.mac = None
+        self.id = None
+
         self.vertical = 0
         self.horizontal = 0
         self.tau = 0.9999
         self.rot = 0
 
     def __enter__(self):
         self.a = 0 # Just for debugging. Delete soon!
 
+        self.set_frequency()
+
         pygame.init()
         self.clock = pygame.time.Clock()
-        self.font = pygame.font.SysFont(None, 24)
+        self.font = pygame.font.SysFont(None, 22)
         self.big_font = pygame.font.SysFont(None, 34)
 
 
         # Set up the display
         # Get screen size
         info = pygame.display.Info()
-        self.screen_width, self.screen_height = info.current_w, info.current_h-100
+        self.screen_width, self.screen_height = info.current_w, info.current_h-50
 
         self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
 
         # Buffer screen:
         #self.back_buffer = pygame.Surface((self.screen_width, self.screen_height))
 
         # Make it fullscreen
         if sys.platform == "win32":
             HWND = pygame.display.get_wm_info()['window']
             SW_MAXIMIZE = 3
             ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)
-        
+
+
         # Durin Image
-        resource_file = "durin\durin\durin_birdseye.jpg"
+        resource_file = "durin/durin_birdseye.jpg"
         resource_path = os.path.join(os.getcwd(), resource_file)
         self.image = pygame.image.load(resource_path)
         self.image = pygame.transform.scale(self.image, (1.75*self.screen_width//3, self.screen_height))
 
 
         self.image_surface = pygame.Surface(self.image.get_size())
         self.image_surface.blit(self.image, (0,0))
@@ -107,68 +118,73 @@
 
         pygame.display.update()
 
 
 
 
         return super().__enter__()
-    
+
     def __exit__(self, e, b, t):
         pygame.quit()
         self.gamepad.stop()
-        exit()
         return super().__exit__(e, b, t)
-    
+
     def read_user_input(self, allow_movement: bool = True, sleep_interval: float=0.02):
         keys = pygame.key.get_pressed()
 
         # Gamepad
         if not self.gamepad.queue.empty():
             x, y, r = self.gamepad.queue.get()
             self.horizontal = x
             self.vertical = y
             self.rot = r
-        
+
         for event in pygame.event.get():
-            if event.type == pygame.QUIT:
+            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                 return False
-            
+
             # Keyboard
             elif event.type == pygame.KEYDOWN:
                 # Key pressed
                 if event.key == pygame.K_UP or event.key == pygame.K_w:
                     self.vertical = 500
                 elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                     self.vertical = -500
-                elif event.key == pygame.K_LEFT or event.key == pygame.K_d:
+                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                     self.horizontal = -500
-                elif event.key == pygame.K_RIGHT or event.key == pygame.K_a:
+                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                     self.horizontal = 500
+                elif event.key == pygame.K_q:
+                    self.rot = 500
+                elif event.key == pygame.K_e:
+                    self.rot = -500
 
             elif event.type == pygame.KEYUP:
                 # Key released
                 if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                     self.vertical = 0
-                elif event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_a:
+                if event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                     self.horizontal = 0
+                if event.key == pygame.K_e or event.key == pygame.K_q:
+                    self.rot = 0
 
         if allow_movement:
             self(Move(self.horizontal, self.vertical, self.rot))
 
-        time.sleep(sleep_interval) # Sleep to avoid sending too many commands
+        # time.sleep(sleep_interval) # Sleep to avoid sending too many commands
 
         return True
-        
-    
+
+
     def render_sensors(self, obs, size: int = 180):
 
         self.screen.fill((0,0,0))   # Fill screen with black
         self.screen.blit(self.image_surface, (0,0))
 
-        
+
         # Update ToF-sensors ######################
         tofs = (np.tanh((obs.tof / 1000)) * 255).astype(np.int32)
 
         # Rotated surfaces
         rotated_surfaces = []
 
         for o in range(len(self.surfaces)):
@@ -190,62 +206,66 @@
             rotation_angle = SENSOR_ROTATIONS[o]
             rotated_surface = pygame.transform.rotate(surface, rotation_angle)
             rotated_surfaces.append(rotated_surface)
 
 
         for i in range(8):
             self.screen.blit(rotated_surfaces[i], (SENSOR_PLACEMENTS[i][0]*self.screen_width,SENSOR_PLACEMENTS[i][1]*self.screen_height))
-                
+
         # Update UWB ######################
 
         uwb = obs.uwb
         #self.render_text("Becon ID\t\t\tDistance (mm)", UWB_PLACEMENT[0])
 
 
         for i in range(10):
             if uwb[i][0] != 0:
-                self.render_text(str(uwb[i][0]), (UWB_PLACEMENT[0], UWB_PLACEMENT[1] + i*d))
-                self.render_text(str(uwb[i][1]), (UWB_PLACEMENT[0]+ 5*d, UWB_PLACEMENT[1]+i*d))
+                self.render_text(str(uwb[i][0]), (UWB_PLACEMENT[0], UWB_PLACEMENT[1] + (i+1)*d))
+                self.render_text(str(uwb[i][1]), (UWB_PLACEMENT[0]+ 7*d, UWB_PLACEMENT[1]+(i+1)*d))
             else:
                 break
 
 
 
         # Update IMU ######################
         imu = obs.imu
         #type = ["Acce", "Gyro", "Magn."]
         for type in range(3):
             for xyz in range(3):
-                self.render_text(str(imu[type][xyz]), (IMU_PLACEMENT[0]+xyz*3*d, IMU_PLACEMENT[1]+type*d))
-        
+                self.render_text(str(imu[type][xyz]), (IMU_PLACEMENT[0]+(xyz+1)*3*d, IMU_PLACEMENT[1]+(type+1)*d))
+
 
         # Update battery level and voltage ######################
         voltage = obs.voltage
         charge = obs.charge
         self.render_text(str(charge) + " %", BATTERY_PLACEMENT)
         self.render_text(str(voltage) + " mV", (BATTERY_PLACEMENT[0]+5*d,BATTERY_PLACEMENT[1]))
 
 
         # Update Durin position ######################
         for m in range(3):
-            self.render_text(str(obs.position[m]), POSITION_PLACEMENT[m])
+            self.render_text(str(obs.position[m]), (POSITION_PLACEMENT[0]+2*m, POSITION_PLACEMENT[1]+2*d))
+
+        # Update movement commands ################
+        self.render_text(str(self.horizontal),(MV_CMD_PLACEMENT[0],MV_CMD_PLACEMENT[1]+2*d))
+        self.render_text(str(self.vertical),(MV_CMD_PLACEMENT[0]+2*d,MV_CMD_PLACEMENT[1]+2*d))
+        self.render_text(str(self.rot),(MV_CMD_PLACEMENT[0]+4*d,MV_CMD_PLACEMENT[1]+2*d))
 
-        
         self.render_static_texts()
 
         # Just for debugging.
         self.a += 1
-        self.render_text("Time step (for debugging): " + str(self.a),(UWB_PLACEMENT[0],UWB_PLACEMENT[1]+10*d))
+        #self.render_text("Time step (for debugging): " + str(self.a),(UWB_PLACEMENT[0],UWB_PLACEMENT[1]+10*d))
 
         # Update screen
         pygame.display.update()
 
-        #self.clock.tick(100)
+        # self.clock.tick(25)
+
 
-    
     def render_text(self, input_text, position, color="w", size = "small"):
         if color == "w":
             c = (255,255,255)
         elif color == "o":
             c = (255,183,91)
         elif color == "b":
             c = (100,100,255)
@@ -257,41 +277,76 @@
         elif size == "big":
             text=  self.big_font.render(input_text, True, c)
         self.screen.blit(text, (position[0]*self.screen_width,position[1]*self.screen_height))
 
     def render_static_texts(self):
         # Static texts¨
 
+        # Dashboard title
         self.render_text("Durin Dashboard", TITLE_PLACEMENT, "t", "big")
 
+        # Titles for Durin IP, MAC and ID
         self.render_text("IP address", IP_PLACEMENT, "o")
         self.render_text("MAC address", (IP_PLACEMENT[0]+5*d,IP_PLACEMENT[1]), "o")
         self.render_text("Durin ID", (IP_PLACEMENT[0]+10*d,IP_PLACEMENT[1]), "o")
 
-        self.render_text("Integrated IMU data", (IMU_INTEG_PLACEMENT), "o")
-
+        # The IP, MAC and ID values
+        self.render_text(str(self.ip), (IP_PLACEMENT[0],IP_PLACEMENT[1]+d))
+        self.render_text(str(self.mac), (IP_PLACEMENT[0]+5*d,IP_PLACEMENT[1]+d))
+        self.render_text(str(self.id), (IP_PLACEMENT[0]+10*d,IP_PLACEMENT[1]+d))
+
+        # IMU-related titles
+        self.render_text("IMU data",(IMU_PLACEMENT[0],IMU_PLACEMENT[1]), "o")
+        self.render_text("x",(IMU_PLACEMENT[0]+3*d,IMU_PLACEMENT[1]), "b")
+        self.render_text("y",(IMU_PLACEMENT[0]+6*d,IMU_PLACEMENT[1]),"b")
+        self.render_text("z",(IMU_PLACEMENT[0]+9*d,IMU_PLACEMENT[1]),"b")
+        self.render_text("Acce",(IMU_PLACEMENT[0],IMU_PLACEMENT[1]+d),"b")
+        self.render_text("Gyro",(IMU_PLACEMENT[0],IMU_PLACEMENT[1]+2*d),"b")
+        self.render_text("Magn",(IMU_PLACEMENT[0],IMU_PLACEMENT[1]+3*d),"b")
 
+        # Integrated IMU title
+        self.render_text("Integrated IMU data", (IMU_INTEG_PLACEMENT), "o")
 
-        self.render_text("UWB ID", (UWB_PLACEMENT[0],UWB_PLACEMENT[1]-2*d), "o")
-        self.render_text("Distance (mm)", (UWB_PLACEMENT[0]+5*d,UWB_PLACEMENT[1]-2*d), "o")
-
-        self.render_text("IMU data",(IMU_PLACEMENT[0]-2*d,IMU_PLACEMENT[1]-3*d), "o")
-        self.render_text("x",(IMU_PLACEMENT[0],IMU_PLACEMENT[1]-d), "b")
-        self.render_text("y",(IMU_PLACEMENT[0]+3*d,IMU_PLACEMENT[1]-d),"b")
-        self.render_text("z",(IMU_PLACEMENT[0]+6*d,IMU_PLACEMENT[1]-d),"b")
-        self.render_text("Acce",(IMU_PLACEMENT[0]-2*d,IMU_PLACEMENT[1]),"b")
-        self.render_text("Gyro",(IMU_PLACEMENT[0]-2*d,IMU_PLACEMENT[1]+d),"b")
-        self.render_text("Magn",(IMU_PLACEMENT[0]-2*d,IMU_PLACEMENT[1]+2*d),"b")
-
+        # Battery related titles
         self.render_text("Battery level",(BATTERY_PLACEMENT[0],BATTERY_PLACEMENT[1]-d), "o")
         self.render_text("Voltage",(BATTERY_PLACEMENT[0]+5*d,BATTERY_PLACEMENT[1]-d), "o")
 
+        # Durin coordinate titles
+        self.render_text("Durin coordinates",(POSITION_PLACEMENT[0],POSITION_PLACEMENT[1]), "o")
+        self.render_text("x",(POSITION_PLACEMENT[0],POSITION_PLACEMENT[1]+d),"b")
+        self.render_text("y",(POSITION_PLACEMENT[0]+2*d,POSITION_PLACEMENT[1]+d),"b")
+        self.render_text("z",(POSITION_PLACEMENT[0]+4*d,POSITION_PLACEMENT[1]+d),"b")
+
+        # Instructions for keyboard shortcuts
+        keyboard_instruction = "Use the keys w, a, s, d or arrow keys or a gamepad"
+        keyboard_instruction2 = "to move Durin. Press q or e for rotations."
+        self.render_text(keyboard_instruction,INSTR_PLACEMENT)
+        self.render_text(keyboard_instruction2,(INSTR_PLACEMENT[0],INSTR_PLACEMENT[1]+d))
+
+        # Movement commands titles
+        self.render_text("Movement commands", MV_CMD_PLACEMENT, "o")
+        self.render_text("x",(MV_CMD_PLACEMENT[0],MV_CMD_PLACEMENT[1]+d),"b")
+        self.render_text("y",(MV_CMD_PLACEMENT[0]+2*d,MV_CMD_PLACEMENT[1]+d),"b")
+        self.render_text("rot",(MV_CMD_PLACEMENT[0]+4*d,MV_CMD_PLACEMENT[1]+d),"b")
+
+        # UWB related titles
+        self.render_text("UWB ID", (UWB_PLACEMENT[0],UWB_PLACEMENT[1]), "o")
+        self.render_text("Distance (mm)", (UWB_PLACEMENT[0]+7*d,UWB_PLACEMENT[1]), "o")
+
+    def set_ip_mac_id(self, ip, mac, id):
+        self.ip = ip
+        self.mac = mac
+        self.id = id
+
+    def set_frequency(self):
+        # The sensor frequencies in Hz
+        sensor_frequencies = (["Imu", 50],
+                              ["Position", 50],
+                              ["SystemStatus", 1],
+                              ["Uwb", 50],
+                              ["Tof", 50],
+                              )
 
-        self.render_text("Durin coordinates",(POSITION_PLACEMENT[0][0],POSITION_PLACEMENT[0][1]-3*d), "o")
-        self.render_text("x",(POSITION_PLACEMENT[0][0],POSITION_PLACEMENT[0][1]-d),"b")
-        self.render_text("y",(POSITION_PLACEMENT[1][0],POSITION_PLACEMENT[0][1]-d),"b")
-        self.render_text("z",(POSITION_PLACEMENT[2][0],POSITION_PLACEMENT[0][1]-d),"b")
-    
-
-
-
+        
+        for sensor in sensor_frequencies:
+            self(SetSensorPeriod(sensor[0],1000/sensor[1]))    # Frequency (Hz) to period (ms)
```

### Comparing `durin-0.0.72/durin.egg-info/PKG-INFO` & `durin-0.0.73/durin.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: durin
-Version: 0.0.72
+Version: 0.0.73
 Summary: Python control interface for the Durin robot
 Maintainer: Jens E. Pedersen
 Maintainer-email: jeped@kth.se
 License: LGPLv3
 Description-Content-Type: text/markdown
 Provides-Extra: aestream
```

### Comparing `durin-0.0.72/durin.egg-info/SOURCES.txt` & `durin-0.0.73/durin.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,35 +1,40 @@
 MANIFEST.in
 README.md
 setup.py
 bin/durin
+durin/Profiler.py
+durin/Read_profilers.py
 durin/__init__.py
 durin/__main__.py
 durin/actuator.py
 durin/cli.py
 durin/durin.py
+durin/durin_birdseye.jpg
 durin/dvs.py
 durin/sensor.py
 durin/ui.py
 durin.egg-info/PKG-INFO
 durin.egg-info/SOURCES.txt
 durin.egg-info/dependency_links.txt
 durin.egg-info/requires.txt
 durin.egg-info/top_level.txt
 durin/controller/__init__.py
 durin/controller/dvs.py
 durin/controller/server.py
 durin/controller/test/__init__.py
 durin/controller/test/test_stream.py
+durin/examples/CPU_test.py
 durin/examples/__init__.py
 durin/examples/braitenberg.py
 durin/examples/commands.py
 durin/examples/dashboard.py
 durin/examples/main.py
 durin/examples/record.py
+durin/examples/stats.py
 durin/io/__init__.py
 durin/io/command.py
 durin/io/gamepad.py
 durin/io/network.py
 durin/io/ringbuffer.py
 durin/io/runnable.py
 durin/io/schema.capnp
```

### Comparing `durin-0.0.72/setup.py` & `durin-0.0.73/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -4,20 +4,20 @@
     requirements = fp.read().split("\n")
 
 with open("README.md", "r") as fp:
     long_description = fp.read()
 
 setup(
     name="durin",
-    version="0.0.72",
+    version="0.0.73",
     install_requires=requirements,
     packages=find_packages(),
     license="LGPLv3",
     maintainer="Jens E. Pedersen",
     maintainer_email="jeped@kth.se",
     extras_require={"aestream": ["aestream"]},
     scripts=["bin/durin"],
     description="Python control interface for the Durin robot",
     long_description=long_description,
     long_description_content_type="text/markdown",
-    package_data={"durin": ["*.capnp"]}
-)
+    include_package_data=True
+)
```

