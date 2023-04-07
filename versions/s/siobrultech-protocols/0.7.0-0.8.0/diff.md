# Comparing `tmp/siobrultech-protocols-0.7.0.tar.gz` & `tmp/siobrultech-protocols-0.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "siobrultech-protocols-0.7.0.tar", last modified: Sun Oct 30 22:44:44 2022, max compression
+gzip compressed data, was "siobrultech-protocols-0.8.0.tar", last modified: Fri Apr  7 00:15:53 2023, max compression
```

## Comparing `siobrultech-protocols-0.7.0.tar` & `siobrultech-protocols-0.8.0.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/
--rw-r--r--   0 runner    (1001) docker     (121)     1104 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     6770 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     5916 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      900 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)     1014 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      116 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:44.100260 siobrultech-protocols-0.7.0/siobrultech_protocols/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5665 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/api.py
--rw-r--r--   0 runner    (1001) docker     (121)      653 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/const.py
--rw-r--r--   0 runner    (1001) docker     (121)     4770 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/fields.py
--rw-r--r--   0 runner    (1001) docker     (121)    11139 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/packets.py
--rw-r--r--   0 runner    (1001) docker     (121)    11998 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/gem/protocol.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/siobrultech_protocols/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     6770 2022-10-30 22:44:44.000000 siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      558 2022-10-30 22:44:44.000000 siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-30 22:44:44.000000 siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       28 2022-10-30 22:44:44.000000 siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:44.104260 siobrultech-protocols-0.7.0/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1871 2022-10-30 22:44:24.000000 siobrultech-protocols-0.7.0/tests/test_requirements.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1104 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     6770 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5916 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      900 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1014 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/siobrultech_protocols/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5665 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      653 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/const.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4770 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13443 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/packets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12178 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/gem/protocol.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/siobrultech_protocols/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6770 2023-04-07 00:15:52.000000 siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      558 2023-04-07 00:15:52.000000 siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:15:52.000000 siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-07 00:15:52.000000 siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:52.999210 siobrultech-protocols-0.8.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-04-07 00:15:47.000000 siobrultech-protocols-0.8.0/tests/test_requirements.py
```

### Comparing `siobrultech-protocols-0.7.0/LICENSE` & `siobrultech-protocols-0.8.0/LICENSE`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/PKG-INFO` & `siobrultech-protocols-0.8.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: siobrultech-protocols
-Version: 0.7.0
+Version: 0.8.0
 Summary: A Sans-I/O Python client library for Brultech Devices
 Author: Shawn Wilsher
 Author-email: me@shawnwilsher.com
 Project-URL: Bug Reports, https://github.com/sdwilsh/siobrultech-protocols/issues
 Project-URL: Release Notes, https://github.com/sdwilsh/siobrultech-protocols/releases/
 Project-URL: Source, https://github.com/sdwilsh/siobrultech-protocols
 Classifier: Development Status :: 4 - Beta
```

### Comparing `siobrultech-protocols-0.7.0/README.md` & `siobrultech-protocols-0.8.0/README.md`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/pyproject.toml` & `siobrultech-protocols-0.8.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/setup.cfg` & `siobrultech-protocols-0.8.0/setup.cfg`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = siobrultech-protocols
-version = 0.7.0
+version = 0.8.0
 author = Shawn Wilsher
 author_email = me@shawnwilsher.com
 description = A Sans-I/O Python client library for Brultech Devices
 long_description = file: README.md
 long_description_content_type = text/markdown
 license_file = LICENSE
 classifiers =
```

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols/gem/api.py` & `siobrultech-protocols-0.8.0/siobrultech_protocols/gem/api.py`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols/gem/const.py` & `siobrultech-protocols-0.8.0/siobrultech_protocols/gem/const.py`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols/gem/fields.py` & `siobrultech-protocols-0.8.0/siobrultech_protocols/gem/fields.py`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols/gem/packets.py` & `siobrultech-protocols-0.8.0/siobrultech_protocols/gem/packets.py`

 * *Files 14% similar despite different names*

```diff
@@ -34,35 +34,39 @@
         self,
         packet_format: PacketFormat,
         voltage: float,
         absolute_watt_seconds: List[int],
         device_id: int,
         serial_number: int,
         seconds: int,
-        pulse_counts: List[int],
-        temperatures: List[float],
+        pulse_counts: Optional[List[int]] = None,
+        temperatures: Optional[List[float]] = None,
         polarized_watt_seconds: Optional[List[int]] = None,
         currents: Optional[List[float]] = None,
         time_stamp: Optional[datetime] = None,
+        aux: Optional[List[int]] = None,
+        dc_voltage: Optional[int] = None,
         **kwargs: Dict[str, Any],
     ):
         self.packet_format: PacketFormat = packet_format
         self.voltage: float = voltage
         self.absolute_watt_seconds: List[int] = absolute_watt_seconds
         self.polarized_watt_seconds: Optional[List[int]] = polarized_watt_seconds
         self.currents: Optional[List[float]] = currents
         self.device_id: int = device_id
         self.serial_number: int = serial_number
         self.seconds: int = seconds
-        self.pulse_counts: List[int] = pulse_counts
-        self.temperatures: List[float] = temperatures
+        self.pulse_counts: List[int] = pulse_counts or []
+        self.temperatures: List[float] = temperatures or []
         if time_stamp:
             self.time_stamp: datetime = time_stamp
         else:
             self.time_stamp: datetime = datetime.now()
+        self.aux = aux
+        self.dc_voltage = dc_voltage
 
     def __str__(self) -> str:
         return json.dumps(
             {
                 "device_id": self.device_id,
                 "serial_number": self.serial_number,
                 "seconds": self.seconds,
@@ -181,73 +185,35 @@
             newest_packet.delta_pulse_count(index, oldest_packet.pulse_counts[index])
             / elapsed_seconds
         )
 
 
 @unique
 class PacketFormatType(IntEnum):
+    ECM_1220 = 1
+    ECM_1240 = 3
     BIN48_NET_TIME = 4
     BIN48_NET = 5
     BIN48_ABS = 7
     BIN32_NET = 8
     BIN32_ABS = 9
 
 
 class PacketFormat(object):
-    NUM_PULSE_COUNTERS: int = 4
-    NUM_TEMPERATURE_SENSORS: int = 8
-
     def __init__(
         self,
         name: str,
         type: PacketFormatType,
         num_channels: int,
-        has_net_metering: bool = False,
-        has_time_stamp: bool = False,
     ):
         self.name: str = name
         self.type: PacketFormatType = type
         self.num_channels: int = num_channels
         self.fields: OrderedDict[str, Field] = OrderedDict()
 
-        self.fields["header"] = NumericField(3, ByteOrder.HiToLo, Sign.Unsigned)
-        self.fields["voltage"] = FloatingPointField(
-            2, ByteOrder.HiToLo, Sign.Unsigned, 10.0
-        )
-        self.fields["absolute_watt_seconds"] = NumericArrayField(
-            num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
-        )
-        if has_net_metering:
-            self.fields["polarized_watt_seconds"] = NumericArrayField(
-                num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
-            )
-        self.fields["serial_number"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
-        self.fields["reserved"] = ByteField()
-        self.fields["device_id"] = NumericField(1, ByteOrder.HiToLo, Sign.Unsigned)
-        self.fields["currents"] = FloatingPointArrayField(
-            num_channels, 2, ByteOrder.LoToHi, Sign.Unsigned, 50.0
-        )
-        self.fields["seconds"] = NumericField(3, ByteOrder.LoToHi, Sign.Unsigned)
-        self.fields["pulse_counts"] = NumericArrayField(
-            PacketFormat.NUM_PULSE_COUNTERS, 3, ByteOrder.LoToHi, Sign.Unsigned
-        )
-        self.fields["temperatures"] = FloatingPointArrayField(
-            PacketFormat.NUM_TEMPERATURE_SENSORS,
-            2,
-            ByteOrder.LoToHi,
-            Sign.Signed,
-            2.0,
-        )
-        if num_channels == 32:
-            self.fields["spare_bytes"] = BytesField(2)
-        if has_time_stamp:
-            self.fields["time_stamp"] = DateTimeField()
-        self.fields["footer"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
-        self.fields["checksum"] = ByteField()
-
     @property
     def size(self) -> int:
         result = 0
         for value in self.fields.values():
             result += value.size
 
         return result
@@ -275,57 +241,153 @@
                     hex(args["footer"]), codecs.encode(packet, "hex")  # type: ignore
                 )
             )
 
         return Packet(**args)  # type: ignore
 
 
+class ECMPacketFormat(PacketFormat):
+    def __init__(
+        self,
+        name: str,
+        type: PacketFormatType,
+        has_aux_channels: bool = False,
+    ):
+        super().__init__(name, type, 2)
+
+        self.fields["header"] = NumericField(3, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["voltage"] = FloatingPointField(
+            2, ByteOrder.HiToLo, Sign.Unsigned, 10.0
+        )
+        self.fields["absolute_watt_seconds"] = NumericArrayField(
+            self.num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
+        )
+        self.fields["polarized_watt_seconds"] = NumericArrayField(
+            self.num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
+        )
+        self.fields["reserved"] = BytesField(size=4)
+        self.fields["serial_number"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["flag"] = ByteField()
+        self.fields["device_id"] = NumericField(1, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["currents"] = FloatingPointArrayField(
+            self.num_channels, 2, ByteOrder.LoToHi, Sign.Unsigned, 100.0
+        )
+        self.fields["seconds"] = NumericField(3, ByteOrder.LoToHi, Sign.Unsigned)
+        self.num_aux_channels = 0
+        if has_aux_channels:
+            self.num_aux_channels = 5
+            self.fields["aux"] = NumericArrayField(
+                self.num_aux_channels, 4, ByteOrder.LoToHi, Sign.Unsigned
+            )
+            self.fields["dc_voltage"] = NumericField(2, ByteOrder.LoToHi, Sign.Unsigned)
+        self.fields["footer"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["checksum"] = ByteField()
+
+
+class GEMPacketFormat(PacketFormat):
+    NUM_PULSE_COUNTERS: int = 4
+    NUM_TEMPERATURE_SENSORS: int = 8
+
+    def __init__(
+        self,
+        name: str,
+        type: PacketFormatType,
+        num_channels: int,
+        has_net_metering: bool = False,
+        has_time_stamp: bool = False,
+    ):
+        super().__init__(name, type, num_channels)
+
+        self.fields["header"] = NumericField(3, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["voltage"] = FloatingPointField(
+            2, ByteOrder.HiToLo, Sign.Unsigned, 10.0
+        )
+        self.fields["absolute_watt_seconds"] = NumericArrayField(
+            num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
+        )
+        if has_net_metering:
+            self.fields["polarized_watt_seconds"] = NumericArrayField(
+                num_channels, 5, ByteOrder.LoToHi, Sign.Unsigned
+            )
+        self.fields["serial_number"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["reserved"] = ByteField()
+        self.fields["device_id"] = NumericField(1, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["currents"] = FloatingPointArrayField(
+            num_channels, 2, ByteOrder.LoToHi, Sign.Unsigned, 50.0
+        )
+        self.fields["seconds"] = NumericField(3, ByteOrder.LoToHi, Sign.Unsigned)
+        self.fields["pulse_counts"] = NumericArrayField(
+            GEMPacketFormat.NUM_PULSE_COUNTERS, 3, ByteOrder.LoToHi, Sign.Unsigned
+        )
+        self.fields["temperatures"] = FloatingPointArrayField(
+            GEMPacketFormat.NUM_TEMPERATURE_SENSORS,
+            2,
+            ByteOrder.LoToHi,
+            Sign.Signed,
+            2.0,
+        )
+        if num_channels == 32:
+            self.fields["spare_bytes"] = BytesField(2)
+        if has_time_stamp:
+            self.fields["time_stamp"] = DateTimeField()
+        self.fields["footer"] = NumericField(2, ByteOrder.HiToLo, Sign.Unsigned)
+        self.fields["checksum"] = ByteField()
+
+
 def _checksum(packet: bytes, size: int):
     checksum = 0
     for i in packet[: size - 1]:
         checksum += i
     checksum = checksum % 256
     if checksum != packet[size - 1]:
         raise MalformedPacketException(
             "bad checksum for packet: {0}".format(codecs.encode(packet[:size], "hex"))
         )
 
 
-BIN48_NET_TIME = PacketFormat(
+BIN48_NET_TIME = GEMPacketFormat(
     name="BIN48-NET-TIME",
     type=PacketFormatType.BIN48_NET_TIME,
     num_channels=48,
     has_net_metering=True,
     has_time_stamp=True,
 )
 
-BIN48_NET = PacketFormat(
+BIN48_NET = GEMPacketFormat(
     name="BIN48-NET",
     type=PacketFormatType.BIN48_NET,
     num_channels=48,
     has_net_metering=True,
     has_time_stamp=False,
 )
 
-BIN48_ABS = PacketFormat(
+BIN48_ABS = GEMPacketFormat(
     name="BIN48-ABS",
     type=PacketFormatType.BIN48_ABS,
     num_channels=48,
     has_net_metering=False,
     has_time_stamp=False,
 )
 
-BIN32_NET = PacketFormat(
+BIN32_NET = GEMPacketFormat(
     name="BIN32-NET",
     type=PacketFormatType.BIN32_NET,
     num_channels=32,
     has_net_metering=True,
     has_time_stamp=False,
 )
 
-BIN32_ABS = PacketFormat(
+BIN32_ABS = GEMPacketFormat(
     name="BIN32-ABS",
     type=PacketFormatType.BIN32_ABS,
     num_channels=32,
     has_net_metering=False,
     has_time_stamp=False,
 )
+
+ECM_1240 = ECMPacketFormat(
+    name="ECM-1240", type=PacketFormatType.ECM_1240, has_aux_channels=True
+)
+
+ECM_1220 = ECMPacketFormat(
+    name="ECM-1220", type=PacketFormatType.ECM_1220, has_aux_channels=False
+)
```

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols/gem/protocol.py` & `siobrultech-protocols-0.8.0/siobrultech_protocols/gem/protocol.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,14 +10,16 @@
 from .const import CMD_DELAY_NEXT_PACKET, PACKET_DELAY_CLEAR_TIME_DEFAULT
 from .packets import (
     BIN32_ABS,
     BIN32_NET,
     BIN48_ABS,
     BIN48_NET,
     BIN48_NET_TIME,
+    ECM_1220,
+    ECM_1240,
     MalformedPacketException,
     Packet,
 )
 
 LOG = logging.getLogger(__name__)
 
 PACKET_HEADER = bytes.fromhex("feff")
@@ -144,14 +146,18 @@
                 packet_format = BIN32_ABS
             elif format_code == 7:
                 packet_format = BIN32_NET
             elif format_code == 6:
                 packet_format = BIN48_ABS
             elif format_code == 5:
                 packet_format = BIN48_NET
+            elif format_code == 3:
+                packet_format = ECM_1240
+            elif format_code == 1:
+                packet_format = ECM_1220
             else:
                 skip_malformed_packet("unknown format code 0x%x", format_code)
                 continue
 
             if len(self._buffer) < packet_format.size:
                 # Not enough length yet
                 LOG.debug(
```

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/PKG-INFO` & `siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: siobrultech-protocols
-Version: 0.7.0
+Version: 0.8.0
 Summary: A Sans-I/O Python client library for Brultech Devices
 Author: Shawn Wilsher
 Author-email: me@shawnwilsher.com
 Project-URL: Bug Reports, https://github.com/sdwilsh/siobrultech-protocols/issues
 Project-URL: Release Notes, https://github.com/sdwilsh/siobrultech-protocols/releases/
 Project-URL: Source, https://github.com/sdwilsh/siobrultech-protocols
 Classifier: Development Status :: 4 - Beta
```

### Comparing `siobrultech-protocols-0.7.0/siobrultech_protocols.egg-info/SOURCES.txt` & `siobrultech-protocols-0.8.0/siobrultech_protocols.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `siobrultech-protocols-0.7.0/tests/test_requirements.py` & `siobrultech-protocols-0.8.0/tests/test_requirements.py`

 * *Files identical despite different names*

