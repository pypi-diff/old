# Comparing `tmp/FlashGBX-3.8.tar.gz` & `tmp/FlashGBX-3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\FlashGBX-3.8.tar", last modified: Thu Apr 21 20:13:00 2022, max compression
+gzip compressed data, was "dist\FlashGBX-3.9.tar", last modified: Fri Apr 29 10:21:55 2022, max compression
```

## Comparing `FlashGBX-3.8.tar` & `FlashGBX-3.9.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxrwxrwx   0        0        0        0 2022-04-21 20:13:00.000000 FlashGBX-3.8/
-drwxrwxrwx   0        0        0        0 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX/
--rw-rw-rw-   0        0        0     1125 2022-03-05 00:13:15.000000 FlashGBX-3.8/FlashGBX/DataTransfer.py
--rw-rw-rw-   0        0        0    11300 2022-04-09 14:29:33.000000 FlashGBX-3.8/FlashGBX/FlashGBX.py
--rw-rw-rw-   0        0        0    55984 2022-04-18 15:35:49.000000 FlashGBX-3.8/FlashGBX/FlashGBX_CLI.py
--rw-rw-rw-   0        0        0   110097 2022-04-20 10:59:47.000000 FlashGBX-3.8/FlashGBX/FlashGBX_GUI.py
--rw-rw-rw-   0        0        0    27006 2022-04-20 13:26:24.000000 FlashGBX-3.8/FlashGBX/Flashcart.py
--rw-rw-rw-   0        0        0     7997 2022-04-18 21:13:11.000000 FlashGBX-3.8/FlashGBX/GBMemory.py
--rw-rw-rw-   0        0        0    44002 2022-04-20 10:45:30.000000 FlashGBX-3.8/FlashGBX/Mapper.py
--rw-rw-rw-   0        0        0     4753 2022-04-05 15:51:32.000000 FlashGBX-3.8/FlashGBX/PocketCamera.py
--rw-rw-rw-   0        0        0    16767 2022-02-17 14:17:13.000000 FlashGBX-3.8/FlashGBX/PocketCameraWindow.py
--rw-rw-rw-   0        0        0     4956 2022-04-18 20:00:28.000000 FlashGBX-3.8/FlashGBX/RomFileAGB.py
--rw-rw-rw-   0        0        0    14604 2022-04-20 10:57:24.000000 FlashGBX-3.8/FlashGBX/RomFileDMG.py
--rw-rw-rw-   0        0        0    17612 2022-04-21 00:08:02.000000 FlashGBX-3.8/FlashGBX/Util.py
--rw-rw-rw-   0        0        0        0 2020-09-25 16:23:13.000000 FlashGBX-3.8/FlashGBX/__init__.py
--rw-rw-rw-   0        0        0       39 2021-02-07 14:47:49.000000 FlashGBX-3.8/FlashGBX/__main__.py
--rw-rw-rw-   0        0        0    21916 2022-04-08 14:40:25.000000 FlashGBX-3.8/FlashGBX/fw_GBxCartRW_v1_3.py
--rw-rw-rw-   0        0        0    14049 2022-03-30 17:28:09.000000 FlashGBX-3.8/FlashGBX/fw_GBxCartRW_v1_4.py
--rw-rw-rw-   0        0        0   116962 2022-04-21 09:01:16.000000 FlashGBX-3.8/FlashGBX/hw_GBxCartRW.py
--rw-rw-rw-   0        0        0   108029 2022-04-21 20:12:45.000000 FlashGBX-3.8/FlashGBX/hw_GBxCartRW_ofw.py
-drwxrwxrwx   0        0        0        0 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX/res/
--rw-rw-rw-   0        0        0   145188 2022-04-21 20:12:59.000000 FlashGBX-3.8/FlashGBX/res/config.zip
--rw-rw-rw-   0        0        0     4774 2022-04-08 13:49:54.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_Mini_v1_0.zip
--rw-rw-rw-   0        0        0     8093 2022-04-08 13:50:24.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_XMAS_v1_0.zip
--rw-rw-rw-   0        0        0     8108 2022-04-08 13:50:10.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_1_v1_2.zip
--rw-rw-rw-   0        0        0    15557 2021-06-07 14:27:46.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_3.zip
--rw-rw-rw-   0        0        0    24489 2022-04-18 10:22:09.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_4.zip
--rw-rw-rw-   0        0        0    25001 2022-04-18 10:32:49.000000 FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_4a.zip
--rw-rw-rw-   0        0        0   129959 2020-09-19 22:06:37.000000 FlashGBX-3.8/FlashGBX/res/icon.ico
--rw-rw-rw-   0        0        0    19286 2020-09-22 23:20:19.000000 FlashGBX-3.8/FlashGBX/res/icon.png
--rw-rw-rw-   0        0        0      653 2022-01-10 12:43:48.000000 FlashGBX-3.8/FlashGBX/res/pc_frame.png
-drwxrwxrwx   0        0        0        0 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/
--rw-rw-rw-   0        0        0    16417 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      991 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       53 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       60 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2022-04-21 20:13:00.000000 FlashGBX-3.8/FlashGBX.egg-info/top_level.txt
--rw-rw-rw-   0        0        0    35149 2020-07-10 14:55:14.000000 FlashGBX-3.8/LICENSE
--rw-rw-rw-   0        0        0       34 2020-09-26 13:03:53.000000 FlashGBX-3.8/MANIFEST.in
--rw-rw-rw-   0        0        0    16417 2022-04-21 20:13:00.000000 FlashGBX-3.8/PKG-INFO
--rw-rw-rw-   0        0        0    15136 2022-04-21 09:43:05.000000 FlashGBX-3.8/README.md
--rw-rw-rw-   0        0        0       42 2022-04-21 20:13:00.000000 FlashGBX-3.8/setup.cfg
--rw-rw-rw-   0        0        0     1278 2022-04-21 00:08:02.000000 FlashGBX-3.8/setup.py
+drwxrwxrwx   0        0        0        0 2022-04-29 10:21:55.000000 FlashGBX-3.9/
+drwxrwxrwx   0        0        0        0 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX/
+-rw-rw-rw-   0        0        0     1125 2022-03-05 00:13:15.000000 FlashGBX-3.9/FlashGBX/DataTransfer.py
+-rw-rw-rw-   0        0        0    11370 2022-04-28 21:31:31.000000 FlashGBX-3.9/FlashGBX/FlashGBX.py
+-rw-rw-rw-   0        0        0    55984 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/FlashGBX_CLI.py
+-rw-rw-rw-   0        0        0   110097 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/FlashGBX_GUI.py
+-rw-rw-rw-   0        0        0    27006 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/Flashcart.py
+-rw-rw-rw-   0        0        0     7997 2022-04-18 21:13:11.000000 FlashGBX-3.9/FlashGBX/GBMemory.py
+-rw-rw-rw-   0        0        0    44002 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/Mapper.py
+-rw-rw-rw-   0        0        0     4753 2022-04-05 15:51:32.000000 FlashGBX-3.9/FlashGBX/PocketCamera.py
+-rw-rw-rw-   0        0        0    16767 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/PocketCameraWindow.py
+-rw-rw-rw-   0        0        0     4956 2022-04-18 20:00:28.000000 FlashGBX-3.9/FlashGBX/RomFileAGB.py
+-rw-rw-rw-   0        0        0    14604 2022-04-20 10:57:24.000000 FlashGBX-3.9/FlashGBX/RomFileDMG.py
+-rw-rw-rw-   0        0        0    17612 2022-04-28 21:27:02.000000 FlashGBX-3.9/FlashGBX/Util.py
+-rw-rw-rw-   0        0        0        0 2020-09-25 16:23:13.000000 FlashGBX-3.9/FlashGBX/__init__.py
+-rw-rw-rw-   0        0        0       39 2021-02-07 14:47:49.000000 FlashGBX-3.9/FlashGBX/__main__.py
+-rw-rw-rw-   0        0        0    22091 2022-04-29 08:32:32.000000 FlashGBX-3.9/FlashGBX/fw_GBxCartRW_v1_3.py
+-rw-rw-rw-   0        0        0    13935 2022-04-28 19:30:59.000000 FlashGBX-3.9/FlashGBX/fw_GBxCartRW_v1_4.py
+-rw-rw-rw-   0        0        0   117089 2022-04-28 17:53:33.000000 FlashGBX-3.9/FlashGBX/hw_GBxCartRW.py
+-rw-rw-rw-   0        0        0   108102 2022-04-26 15:02:09.000000 FlashGBX-3.9/FlashGBX/hw_GBxCartRW_ofw.py
+drwxrwxrwx   0        0        0        0 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX/res/
+-rw-rw-rw-   0        0        0   146685 2022-04-29 10:21:54.000000 FlashGBX-3.9/FlashGBX/res/config.zip
+-rw-rw-rw-   0        0        0     4774 2022-04-08 13:49:54.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_Mini_v1_0.zip
+-rw-rw-rw-   0        0        0     8093 2022-04-08 13:50:24.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_XMAS_v1_0.zip
+-rw-rw-rw-   0        0        0     8108 2022-04-08 13:50:10.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_1_v1_2.zip
+-rw-rw-rw-   0        0        0    15567 2022-04-28 23:19:58.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_3.zip
+-rw-rw-rw-   0        0        0    24489 2022-04-18 10:22:09.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_4.zip
+-rw-rw-rw-   0        0        0    25001 2022-04-18 10:32:49.000000 FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_4a.zip
+-rw-rw-rw-   0        0        0   129959 2020-09-19 22:06:37.000000 FlashGBX-3.9/FlashGBX/res/icon.ico
+-rw-rw-rw-   0        0        0    19286 2020-09-22 23:20:19.000000 FlashGBX-3.9/FlashGBX/res/icon.png
+-rw-rw-rw-   0        0        0      653 2022-01-10 12:43:48.000000 FlashGBX-3.9/FlashGBX/res/pc_frame.png
+drwxrwxrwx   0        0        0        0 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/
+-rw-rw-rw-   0        0        0    16565 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      991 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       60 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2022-04-29 10:21:55.000000 FlashGBX-3.9/FlashGBX.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0    35149 2020-07-10 14:55:14.000000 FlashGBX-3.9/LICENSE
+-rw-rw-rw-   0        0        0       34 2020-09-26 13:03:53.000000 FlashGBX-3.9/MANIFEST.in
+-rw-rw-rw-   0        0        0    16565 2022-04-29 10:21:55.000000 FlashGBX-3.9/PKG-INFO
+-rw-rw-rw-   0        0        0    15279 2022-04-28 18:18:14.000000 FlashGBX-3.9/README.md
+-rw-rw-rw-   0        0        0       42 2022-04-29 10:21:55.000000 FlashGBX-3.9/setup.cfg
+-rw-rw-rw-   0        0        0     1278 2022-04-28 21:27:02.000000 FlashGBX-3.9/setup.py
```

### Comparing `FlashGBX-3.8/FlashGBX/DataTransfer.py` & `FlashGBX-3.9/FlashGBX/DataTransfer.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/FlashGBX.py` & `FlashGBX-3.9/FlashGBX/FlashGBX.py`

 * *Files 2% similar despite different names*

```diff
@@ -29,15 +29,15 @@
 	ret = []
 	flashcarts = { "DMG":{}, "AGB":{} }
 	
 	# Settings and Config
 	(config_version, fc_files) = ReadConfigFiles(args=args)
 	if config_version != Util.VERSION:
 		# Rename old files that have since been replaced/renamed/merged
-		deprecated_files = [ "fc_AGB_TEST.txt", "fc_DMG_TEST.txt", "fc_AGB_Nintendo_E201850.txt", "fc_AGB_Nintendo_E201868.txt", "config.ini", "fc_DMG_MX29LV320ABTC.txt", "fc_DMG_iG_4MB_MBC3_RTC.txt", "fc_AGB_Flash2Advance.txt", "fc_AGB_MX29LV640_AUDIO.txt", "fc_AGB_M36L0R7050T.txt", "fc_AGB_M36L0R8060B.txt", "fc_AGB_M36L0R8060T.txt", "fc_AGB_iG_32MB_S29GL512N.txt" ]
+		deprecated_files = [ "fc_AGB_TEST.txt", "fc_DMG_TEST.txt", "fc_AGB_Nintendo_E201850.txt", "fc_AGB_Nintendo_E201868.txt", "config.ini", "fc_DMG_MX29LV320ABTC.txt", "fc_DMG_iG_4MB_MBC3_RTC.txt", "fc_AGB_Flash2Advance.txt", "fc_AGB_MX29LV640_AUDIO.txt", "fc_AGB_M36L0R7050T.txt", "fc_AGB_M36L0R8060B.txt", "fc_AGB_M36L0R8060T.txt", "fc_AGB_iG_32MB_S29GL512N.txt", "fc_DMG_SST39SF010_AUDIO.txt" ]
 		for file in deprecated_files:
 			if os.path.exists(config_path + "/" + file):
 				os.rename(config_path + "/" + file, config_path + "/" + file + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".bak")
 		
 		rf_list = ""
 		if os.path.exists(app_path + "/res/config.zip"):
 			with zipfile.ZipFile(app_path + "/res/config.zip") as zip:
@@ -55,25 +55,26 @@
 				ret.append([1, "The application was recently updated and some flashcart type files have been updated as well. You will find backup copies of them in your configuration directory.\n\nUpdated files:\n" + rf_list[:-1]])
 			fc_files = glob.glob("{0:s}/fc_*.txt".format(config_path))
 		else:
 			print("WARNING: {:s} not found. This is required to load new flash cartridge type configurations after updating.".format(app_path + "/res/config.zip"))
 	
 	# Read flash cart types
 	for file in fc_files:
-		with open(file, encoding='utf-8') as f:
-			data = f.read()
-			specs_int = re.sub("(0x[0-9A-F]+)", lambda m: str(int(m.group(1), 16)), data) # hex numbers to int numbers, otherwise not valid json
-			try:
-				specs = json.loads(specs_int)
-			except:
-				ret.append([2, "The flashchip type file “{:s}” could not be parsed and needs to be fixed before it can be used.".format(os.path.basename(file))])
-				continue
-			for name in specs["names"]:
-				if not specs["type"] in flashcarts: continue # only DMG and AGB are supported right now
-				flashcarts[specs["type"]][name] = specs
+		if os.path.exists(file):
+			with open(file, encoding='utf-8') as f:
+				data = f.read()
+				specs_int = re.sub("(0x[0-9A-F]+)", lambda m: str(int(m.group(1), 16)), data) # hex numbers to int numbers, otherwise not valid json
+				try:
+					specs = json.loads(specs_int)
+				except:
+					ret.append([2, "The flashchip type file “{:s}” could not be parsed and needs to be fixed before it can be used.".format(os.path.basename(file))])
+					continue
+				for name in specs["names"]:
+					if not specs["type"] in flashcarts: continue # only DMG and AGB are supported right now
+					flashcarts[specs["type"]][name] = specs
 	
 	return { "flashcarts":flashcarts, "config_ret":ret }
 
 class ArgParseCustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass
 def main(portableMode=False):
 	if platform.system() == "Windows": os.system("color")
 	os.environ['QT_MAC_WANTS_LAYER'] = '1'
```

### Comparing `FlashGBX-3.8/FlashGBX/FlashGBX_CLI.py` & `FlashGBX-3.9/FlashGBX/FlashGBX_CLI.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/FlashGBX_GUI.py` & `FlashGBX-3.9/FlashGBX/FlashGBX_GUI.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/Flashcart.py` & `FlashGBX-3.9/FlashGBX/Flashcart.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/GBMemory.py` & `FlashGBX-3.9/FlashGBX/GBMemory.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/Mapper.py` & `FlashGBX-3.9/FlashGBX/Mapper.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/PocketCamera.py` & `FlashGBX-3.9/FlashGBX/PocketCamera.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/PocketCameraWindow.py` & `FlashGBX-3.9/FlashGBX/PocketCameraWindow.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/RomFileAGB.py` & `FlashGBX-3.9/FlashGBX/RomFileAGB.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/RomFileDMG.py` & `FlashGBX-3.9/FlashGBX/RomFileDMG.py`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/Util.py` & `FlashGBX-3.9/FlashGBX/Util.py`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # Author: Lesserkuma (github.com/lesserkuma)
 
 import math, time, datetime, copy, configparser, threading, statistics, os, platform, traceback, io, struct
 from enum import Enum
 
 # Common constants
 APPNAME = "FlashGBX"
-VERSION_PEP440 = "3.8"
+VERSION_PEP440 = "3.9"
 VERSION = "v{:s}".format(VERSION_PEP440)
 DEBUG = False
 
 AGB_Header_ROM_Sizes = [ "1 MB", "2 MB", "4 MB", "8 MB", "16 MB", "32 MB", "64 MB", "128 MB", "256 MB" ]
 AGB_Header_ROM_Sizes_Map = [ 0x100000, 0x200000, 0x400000, 0x800000, 0x1000000, 0x2000000, 0x4000000, 0x8000000, 0x10000000 ]
 AGB_Header_Save_Types = [ "None", "4K EEPROM (512 Bytes)", "64K EEPROM (8 KB)", "256K SRAM/FRAM (32 KB)", "512K FLASH (64 KB)", "1M FLASH (128 KB)", "8M DACS (1008 KB)", "Unlicensed 512K SRAM (64 KB)", "Unlicensed 1M SRAM (128 KB)" ]
 AGB_Header_Save_Sizes = [ 0, 512, 8192, 32768, 65536, 131072, 1032192, 65536, 131072 ]
```

### Comparing `FlashGBX-3.8/FlashGBX/fw_GBxCartRW_v1_3.py` & `FlashGBX-3.9/FlashGBX/fw_GBxCartRW_v1_3.py`

 * *Files 2% similar despite different names*

```diff
@@ -189,18 +189,18 @@
 		dev.close()
 		return True
 
 	def UpdateFirmware(self):
 		fw = ""
 		path = ""
 		if self.optCFW.isChecked():
-			fw = "Version {:s}".format(self.CFW_VER)
+			fw = self.CFW_VER
 			fn = "cfw.hex"
 		elif self.optOFW.isChecked():
-			fw = "Version {:s}".format(self.OFW_VER)
+			fw = self.OFW_VER
 			fn = "ofw.hex"
 		else:
 			path = self.APP.SETTINGS.value("LastDirFirmwareUpdate")
 			path = QtWidgets.QFileDialog.getOpenFileName(self, "Choose GBxCart RW Firmware File", path, "Firmware Update (*.hex);;All Files (*.*)")[0]
 			if path == "": return
 			temp = re.search(r"^(gbx(?:cart|mas)_rw_.+_pcb_r.+\.hex)$", os.path.basename(path))
 			if temp is None:
@@ -294,15 +294,15 @@
 		lives = 10
 		buffer = bytearray()
 
 		fncSetStatus(text="Status: Waiting for bootloader...", setProgress=0)
 		if self.ResetAVR(delay) is False:
 			fncSetStatus(text="Status: Bootloader error.", enableUI=True)
 			self.prgStatus.setValue(0)
-			msgbox = QtWidgets.QMessageBox(parent=self, icon=QtWidgets.QMessageBox.Critical, windowTitle="FlashGBX", text="The firmware update was not successful as the GBxCart RW bootloader is not responding. If it doesn’t work even after multiple retries, please use the official firmware updater instead.", standardButtons=QtWidgets.QMessageBox.Ok)
+			msgbox = QtWidgets.QMessageBox(parent=self, icon=QtWidgets.QMessageBox.Critical, windowTitle="FlashGBX", text="The firmware update failed as the device is not responding correctly. Please ensure you use a <a href=\"https://www.gbxcart.com/\">genuine GBxCart RW</a>, re-connect using a different USB cable and try again.\n\n⚠️ For safety reasons and to avoid potential fire hazards, do not use unauthorized clone hardware that have no electrical fuses, such as the “FLASH&nbsp;BOY” series.".replace("\n", "<br>"), standardButtons=QtWidgets.QMessageBox.Ok)
 			answer = msgbox.exec()
 			return 2
 		
 		while True:
 			try:
 				dev = serial.Serial(port=port, baudrate=9600, timeout=1)
 			except:
```

### Comparing `FlashGBX-3.8/FlashGBX/fw_GBxCartRW_v1_4.py` & `FlashGBX-3.9/FlashGBX/fw_GBxCartRW_v1_4.py`

 * *Files 1% similar despite different names*

```diff
@@ -105,15 +105,15 @@
 			self.FWUPD = FirmwareUpdater(app_path, device.GetPort())
 			self.DEV_NAME = device.GetName()
 			self.FW_VER = device.GetFirmwareVersion(more=True)
 			self.PCB_VER = device.GetPCBVersion()
 			self.DEVICE = device
 		else:
 			self.APP.QT_APP.processEvents()
-			text = "This Firmware Updater is for insideGadgets GBxCart RW v1.4 devices only. Please only proceed if your device matches this hardware revision.\n\nGBxCart RW v1.3 can be updated only after connecting to it first. If you want to update another GBxCart RW hardware revision, please use the official firmware updater by insideGadgets instead."
+			text = "This Firmware Updater is for insideGadgets GBxCart RW v1.4 devices only. Please only proceed if your device matches this hardware revision.\n\nOlder GBxCart RW revisions can be updated only after connecting to them first."
 			msgbox = QtWidgets.QMessageBox(parent=self, icon=QtWidgets.QMessageBox.Warning, windowTitle="FlashGBX", text=text, standardButtons=QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
 			msgbox.setDefaultButton(QtWidgets.QMessageBox.Ok)
 			answer = msgbox.exec()
 			if answer == QtWidgets.QMessageBox.Cancel: return
 			self.FWUPD = FirmwareUpdater(app_path, None)
 
 		self.layout = QtWidgets.QGridLayout()
```

### Comparing `FlashGBX-3.8/FlashGBX/hw_GBxCartRW.py` & `FlashGBX-3.9/FlashGBX/hw_GBxCartRW.py`

 * *Files 0% similar despite different names*

```diff
@@ -891,15 +891,15 @@
 			if temp is False or len(temp) != length: return bytearray()
 			buffer += temp
 			if self.INFO["action"] in (self.ACTIONS["ROM_READ"], self.ACTIONS["SAVE_READ"], self.ACTIONS["ROM_WRITE_VERIFY"]) and not self.NO_PROG_UPDATE:
 				self.SetProgress({"action":"READ", "bytes_added":len(temp)})
 		
 		return buffer
 
-	def ReadROM_3DMemory(self, address, length, max_length=512):
+	def ReadROM_3DMemory(self, address, length, max_length=64):
 		buffer_size = 0x1000
 		num = math.ceil(length / max_length)
 		dprint("Reading 0x{:X} bytes from cartridge ROM in {:d} iteration(s)".format(length, num))
 		if length > max_length: length = max_length
 
 		self._set_fw_variable("TRANSFER_SIZE", length)
 		self._set_fw_variable("BUFFER_SIZE", buffer_size)
@@ -916,15 +916,15 @@
 			
 			if self.INFO["action"] == self.ACTIONS["ROM_READ"] and not self.NO_PROG_UPDATE:
 				self.SetProgress({"action":"READ", "bytes_added":buffer_size})
 			self._write(0)
 
 		return buffer
 
-	def ReadRAM(self, address, length, command=None, max_length=512):
+	def ReadRAM(self, address, length, command=None, max_length=64):
 		num = math.ceil(length / max_length)
 		dprint("Reading 0x{:X} bytes from cartridge RAM in {:d} iteration(s)".format(length, num))
 		if length > max_length: length = max_length
 		buffer = bytearray()
 		self._set_fw_variable("TRANSFER_SIZE", length)
 		
 		if self.MODE == "DMG":
@@ -1410,39 +1410,42 @@
 						flash_id = cart_flash_id
 						flash_id_found = True
 						flash_type = f
 						flash_types.append(flash_type)
 						flashcart.Reset(full_reset=False)
 						dprint("Found the correct cartridge type!")
 		
+		if self.CanPowerCycleCart(): self.CartPowerCycle()
+
 		# Check flash size
 		flash_type_id = 0
 		cfi_s = ""
 		cfi = None
 		if len(flash_types) > 0:
 			flash_type_id = flash_types[0]
 			if self.MODE == "DMG":
 				supp_flash_types = self.GetSupportedCartridgesDMG()
 			elif self.MODE == "AGB":
 				supp_flash_types = self.GetSupportedCartridgesAGB()
 			
 			(flash_id, cfi_s, cfi) = self.CheckFlashChip(limitVoltage=limitVoltage, cart_type=supp_flash_types[1][flash_type_id])
-			size = supp_flash_types[1][flash_types[0]]["flash_size"]
-			size_undetected = False
-			for i in range(0, len(flash_types)):
-				if size != supp_flash_types[1][flash_types[i]]["flash_size"]:
-					size_undetected = True
-			
-			if size_undetected:
-				if isinstance(cfi, dict) and "device_size" in cfi:
-					for i in range(0, len(flash_types)):
-						if cfi['device_size'] == supp_flash_types[1][flash_types[i]]["flash_size"]:
-							flash_type_id = flash_types[i]
-							size_undetected = False
-							break
+			if "flash_size" in supp_flash_types[1][flash_types[0]]:
+				size = supp_flash_types[1][flash_types[0]]["flash_size"]
+				size_undetected = False
+				for i in range(0, len(flash_types)):
+					if size != supp_flash_types[1][flash_types[i]]["flash_size"]:
+						size_undetected = True
+				
+				if size_undetected:
+					if isinstance(cfi, dict) and "device_size" in cfi:
+						for i in range(0, len(flash_types)):
+							if cfi['device_size'] == supp_flash_types[1][flash_types[i]]["flash_size"]:
+								flash_type_id = flash_types[i]
+								size_undetected = False
+								break
 		
 		else:
 			(flash_id, cfi_s, cfi) = self.CheckFlashChip(limitVoltage=limitVoltage)
 		
 		if self.MODE == "DMG" and not flash_id_found:
 			self._write(self.DEVICE_CMD["SET_VOLTAGE_5V"])
 			time.sleep(0.1)
```

### Comparing `FlashGBX-3.8/FlashGBX/hw_GBxCartRW_ofw.py` & `FlashGBX-3.9/FlashGBX/hw_GBxCartRW_ofw.py`

 * *Files 0% similar despite different names*

```diff
@@ -899,27 +899,28 @@
 			flash_type_id = flash_types[0]
 			if self.MODE == "DMG":
 				supp_flash_types = self.GetSupportedCartridgesDMG()
 			elif self.MODE == "AGB":
 				supp_flash_types = self.GetSupportedCartridgesAGB()
 			
 			(flash_id, cfi_s, cfi) = self.CheckFlashChip(limitVoltage=limitVoltage, cart_type=supp_flash_types[1][flash_type_id])
-			size = supp_flash_types[1][flash_types[0]]["flash_size"]
-			size_undetected = False
-			for i in range(0, len(flash_types)):
-				if size != supp_flash_types[1][flash_types[i]]["flash_size"]:
-					size_undetected = True
-			
-			if size_undetected:
-				if isinstance(cfi, dict) and "device_size" in cfi:
-					for i in range(0, len(flash_types)):
-						if cfi['device_size'] == supp_flash_types[1][flash_types[i]]["flash_size"]:
-							flash_type_id = flash_types[i]
-							size_undetected = False
-							break
+			if "flash_size" in supp_flash_types[1][flash_types[0]]:
+				size = supp_flash_types[1][flash_types[0]]["flash_size"]
+				size_undetected = False
+				for i in range(0, len(flash_types)):
+					if size != supp_flash_types[1][flash_types[i]]["flash_size"]:
+						size_undetected = True
+				
+				if size_undetected:
+					if isinstance(cfi, dict) and "device_size" in cfi:
+						for i in range(0, len(flash_types)):
+							if cfi['device_size'] == supp_flash_types[1][flash_types[i]]["flash_size"]:
+								flash_type_id = flash_types[i]
+								size_undetected = False
+								break
 		
 		else:
 			(flash_id, cfi_s, cfi) = self.CheckFlashChip(limitVoltage=limitVoltage)
 		
 		if self.MODE == "DMG" and not flash_id_found:
 			self.set_mode(self.DEVICE_CMD["VOLTAGE_5V"])
```

### Comparing `FlashGBX-3.8/FlashGBX/res/config.zip` & `FlashGBX-3.9/FlashGBX/res/config.zip`

 * *Files 4% similar despite different names*

#### zipinfo -v {}

 * *Differences in extra fields detected; using output from zipinfo -v*

```diff
@@ -1,22 +1,22 @@
 There is no zipfile comment.
 
 End-of-central-directory record:
 -------------------------------
 
-  Zip archive file size:                    145188 (0000000000023724h)
-  Actual end-cent-dir record offset:        145166 (000000000002370Eh)
-  Expected end-cent-dir record offset:      145166 (000000000002370Eh)
+  Zip archive file size:                    146685 (0000000000023CFDh)
+  Actual end-cent-dir record offset:        146663 (0000000000023CE7h)
+  Expected end-cent-dir record offset:      146663 (0000000000023CE7h)
   (based on the length of the central directory and its expected offset)
 
   This zipfile constitutes the sole disk of a single-part archive; its
-  central directory contains 99 entries.
-  The central directory is 10364 (000000000000287Ch) bytes long,
+  central directory contains 102 entries.
+  The central directory is 10707 (00000000000029D3h) bytes long,
   and its (expected) offset in bytes from the beginning of the zipfile
-  is 134802 (0000000000020E92h).
+  is 135956 (0000000000021314h).
 
 
 Central directory entry #1:
 ---------------------------
 
   db_AGB.json
 
@@ -40,15 +40,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d9 f4 3e 4a 6d 40 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 d9 f4 3e 4a 6d 40 d8 01 74 3c 58 2f.
 
   There is no file comment.
 
 Central directory entry #2:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -75,15 +75,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 1c 9b d8 e3 c9 21 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 1c 9b d8 e3 c9 21 d8 01 09 ad 82 24.
 
   There is no file comment.
 
 Central directory entry #3:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -110,15 +110,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 05 c5 cd e3 c9 21 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 05 c5 cd e3 c9 21 d8 01 09 ad 82 24.
 
   There is no file comment.
 
 Central directory entry #4:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -145,15 +145,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 58 67 b0 5d bb 3f d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 58 67 b0 5d bb 3f d8 01 02 d4 82 24.
 
   There is no file comment.
 
 Central directory entry #5:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -180,15 +180,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 99 7c b7 e3 c9 21 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 99 7c b7 e3 c9 21 d8 01 19 ec 82 24.
 
   There is no file comment.
 
 Central directory entry #6:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -215,15 +215,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 a0 cd ac e3 c9 21 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 a0 cd ac e3 c9 21 d8 01 22 fb 82 24.
 
   There is no file comment.
 
 Central directory entry #7:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -250,15 +250,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 62 5f 9f e3 c9 21 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 62 5f 9f e3 c9 21 d8 01 22 fb 82 24.
 
   There is no file comment.
 
 Central directory entry #8:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -285,15 +285,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 0b 60 9a bf 9d 30 d8 01 33 0d 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 0b 60 9a bf 9d 30 d8 01 3e 22 83 24.
 
   There is no file comment.
 
 Central directory entry #9:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -320,15 +320,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 12 fd 9e d1 ea 19 d8 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 12 fd 9e d1 ea 19 d8 01 3e 22 83 24.
 
   There is no file comment.
 
 Central directory entry #10:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -355,15 +355,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 83 1f b8 d0 ea 19 d8 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 83 1f b8 d0 ea 19 d8 01 3e 22 83 24.
 
   There is no file comment.
 
 Central directory entry #11:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -390,15 +390,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 27 5b 23 7d 4b d7 d7 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 27 5b 23 7d 4b d7 d7 01 5f 49 83 24.
 
   There is no file comment.
 
 Central directory entry #12:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -425,15 +425,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 79 2e b6 da 53 fa d7 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 79 2e b6 da 53 fa d7 01 5f 49 83 24.
 
   There is no file comment.
 
 Central directory entry #13:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -460,15 +460,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 16 eb 6e dc 53 fa d7 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 16 eb 6e dc 53 fa d7 01 60 70 83 24.
 
   There is no file comment.
 
 Central directory entry #14:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -495,15 +495,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 20 9b 28 c0 fe 3f d7 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 20 9b 28 c0 fe 3f d7 01 60 70 83 24.
 
   There is no file comment.
 
 Central directory entry #15:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -530,15 +530,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 6c 2c fe a3 05 30 d8 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 6c 2c fe a3 05 30 d8 01 60 70 83 24.
 
   There is no file comment.
 
 Central directory entry #16:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -565,15 +565,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 e4 a8 85 e6 2f 4c d7 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 e4 a8 85 e6 2f 4c d7 01 73 97 83 24.
 
   There is no file comment.
 
 Central directory entry #17:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -600,15 +600,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 05 bd 7a 37 8e 4f d8 01 4a 34 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 05 bd 7a 37 8e 4f d8 01 73 97 83 24.
 
   There is no file comment.
 
 Central directory entry #18:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -635,15 +635,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 b5 5b a5 0f 8e 4f d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 b5 5b a5 0f 8e 4f d8 01 73 97 83 24.
 
   There is no file comment.
 
 Central directory entry #19:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -670,15 +670,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 2a 0e f0 1e 8e 4f d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 2a 0e f0 1e 8e 4f d8 01 77 be 83 24.
 
   There is no file comment.
 
 Central directory entry #20:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -705,15 +705,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 7c 28 8a e3 c9 21 d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 7c 28 8a e3 c9 21 d8 01 77 be 83 24.
 
   There is no file comment.
 
 Central directory entry #21:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -740,15 +740,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 41 20 39 cb b5 d5 d7 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 41 20 39 cb b5 d5 d7 01 77 be 83 24.
 
   There is no file comment.
 
 Central directory entry #22:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -775,15 +775,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 55 8c a7 ca b5 d5 d7 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 55 8c a7 ca b5 d5 d7 01 89 e5 83 24.
 
   There is no file comment.
 
 Central directory entry #23:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -810,15 +810,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 c8 3c 80 e3 c9 21 d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 c8 3c 80 e3 c9 21 d8 01 89 e5 83 24.
 
   There is no file comment.
 
 Central directory entry #24:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -845,15 +845,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 86 ca 74 e3 c9 21 d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 86 ca 74 e3 c9 21 d8 01 9b 0c 84 24.
 
   There is no file comment.
 
 Central directory entry #25:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -880,15 +880,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 01 31 69 e3 c9 21 d8 01 5a 5b 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 01 31 69 e3 c9 21 d8 01 9b 0c 84 24.
 
   There is no file comment.
 
 Central directory entry #26:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -915,15 +915,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 fd 5a 5e e3 c9 21 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 fd 5a 5e e3 c9 21 d8 01 9b 0c 84 24.
 
   There is no file comment.
 
 Central directory entry #27:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -950,15 +950,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d4 5d 53 e3 c9 21 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 d4 5d 53 e3 c9 21 d8 01 ba 33 84 24.
 
   There is no file comment.
 
 Central directory entry #28:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -985,15 +985,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 40 99 49 e3 c9 21 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 40 99 49 e3 c9 21 d8 01 ba 33 84 24.
 
   There is no file comment.
 
 Central directory entry #29:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1020,15 +1020,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 3b 9f 3e e3 c9 21 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 3b 9f 3e e3 c9 21 d8 01 ba 33 84 24.
 
   There is no file comment.
 
 Central directory entry #30:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1055,15 +1055,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 a6 e2 89 e8 c9 49 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 a6 e2 89 e8 c9 49 d8 01 c3 5a 84 24.
 
   There is no file comment.
 
 Central directory entry #31:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1090,15 +1090,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 93 57 9a 96 33 33 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 93 57 9a 96 33 33 d8 01 c3 5a 84 24.
 
   There is no file comment.
 
 Central directory entry #32:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1125,15 +1125,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 82 11 0e 3e e9 32 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 82 11 0e 3e e9 32 d8 01 c3 5a 84 24.
 
   There is no file comment.
 
 Central directory entry #33:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1160,15 +1160,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 4e 78 d8 9b c0 4d d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 4e 78 d8 9b c0 4d d8 01 d0 81 84 24.
 
   There is no file comment.
 
 Central directory entry #34:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1195,15 +1195,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 f3 d8 26 e3 c9 21 d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 f3 d8 26 e3 c9 21 d8 01 d0 81 84 24.
 
   There is no file comment.
 
 Central directory entry #35:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1230,15 +1230,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 63 59 25 5f bb 3f d8 01 72 82 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 63 59 25 5f bb 3f d8 01 d0 81 84 24.
 
   There is no file comment.
 
 Central directory entry #36:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1265,15 +1265,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 db 95 b9 1e 85 44 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 db 95 b9 1e 85 44 d8 01 e7 a8 84 24.
 
   There is no file comment.
 
 Central directory entry #37:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1300,15 +1300,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 a0 1f 85 84 76 34 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 a0 1f 85 84 76 34 d8 01 e7 a8 84 24.
 
   There is no file comment.
 
 Central directory entry #38:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1335,15 +1335,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d9 53 11 e3 c9 21 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 d9 53 11 e3 c9 21 d8 01 f6 cf 84 24.
 
   There is no file comment.
 
 Central directory entry #39:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1370,15 +1370,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 be 2f 06 e3 c9 21 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 be 2f 06 e3 c9 21 d8 01 f6 cf 84 24.
 
   There is no file comment.
 
 Central directory entry #40:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1405,15 +1405,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 1a 94 f9 e2 c9 21 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 1a 94 f9 e2 c9 21 d8 01 f6 cf 84 24.
 
   There is no file comment.
 
 Central directory entry #41:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1426,29 +1426,29 @@
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Apr 11 18:19:28
+  file last modified on (DOS date/time):          2022 Apr 22 15:57:24
   32-bit CRC value (hex):                         be27054c
   compressed size:                                316 bytes
   uncompressed size:                              912 bytes
   length of filename:                             19 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 e4 8a 71 ea bf 4d d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 e1 6a 76 e3 50 56 d8 01 14 f7 84 24.
 
   There is no file comment.
 
 Central directory entry #42:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1475,15 +1475,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 c1 b5 fb ce c9 21 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 c1 b5 fb ce c9 21 d8 01 14 f7 84 24.
 
   There is no file comment.
 
 Central directory entry #43:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1496,29 +1496,29 @@
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Feb 14 19:40:00
+  file last modified on (DOS date/time):          2022 Apr 24 14:41:20
   32-bit CRC value (hex):                         cfa8701b
   compressed size:                                364 bytes
   uncompressed size:                              1253 bytes
   length of filename:                             19 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 2c 8b ee e2 c9 21 d8 01 84 a9 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 e2 b4 bd 98 d8 57 d8 01 14 f7 84 24.
 
   There is no file comment.
 
 Central directory entry #44:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1531,29 +1531,29 @@
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Feb 14 19:40:00
+  file last modified on (DOS date/time):          2022 Apr 24 20:26:22
   32-bit CRC value (hex):                         0090f439
   compressed size:                                346 bytes
   uncompressed size:                              1072 bytes
   length of filename:                             21 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 89 9f e4 e2 c9 21 d8 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 31 a8 66 cc 08 58 d8 01 34 1e 85 24.
 
   There is no file comment.
 
 Central directory entry #45:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1580,15 +1580,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 76 0f 0c b4 5f 3d d8 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 76 0f 0c b4 5f 3d d8 01 34 1e 85 24.
 
   There is no file comment.
 
 Central directory entry #46:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1615,15 +1615,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 74 74 e1 5a 53 f4 d7 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 74 74 e1 5a 53 f4 d7 01 34 1e 85 24.
 
   There is no file comment.
 
 Central directory entry #47:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1650,15 +1650,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 99 c7 83 4d 53 f4 d7 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 99 c7 83 4d 53 f4 d7 01 25 45 85 24.
 
   There is no file comment.
 
 Central directory entry #48:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1685,15 +1685,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 e5 1a 01 89 c9 30 d8 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 e5 1a 01 89 c9 30 d8 01 25 45 85 24.
 
   There is no file comment.
 
 Central directory entry #49:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1720,15 +1720,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 00 62 6e 9b c9 30 d8 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 00 62 6e 9b c9 30 d8 01 25 45 85 24.
 
   There is no file comment.
 
 Central directory entry #50:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1755,15 +1755,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 06 f3 e6 a4 5f 3d d8 01 97 d0 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 06 f3 e6 a4 5f 3d d8 01 3b 6c 85 24.
 
   There is no file comment.
 
 Central directory entry #51:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1790,15 +1790,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d0 e1 4e e1 73 3f d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 d0 e1 4e e1 73 3f d8 01 3b 6c 85 24.
 
   There is no file comment.
 
 Central directory entry #52:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1825,15 +1825,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 74 94 40 d6 73 3f d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 74 94 40 d6 73 3f d8 01 46 93 85 24.
 
   There is no file comment.
 
 Central directory entry #53:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1860,15 +1860,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 59 cf 22 6c 00 33 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 59 cf 22 6c 00 33 d8 01 46 93 85 24.
 
   There is no file comment.
 
 Central directory entry #54:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1895,15 +1895,15 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 65 9e db e2 c9 21 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 65 9e db e2 c9 21 d8 01 66 ba 85 24.
 
   There is no file comment.
 
 Central directory entry #55:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1916,29 +1916,29 @@
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Apr 20 15:37:38
+  file last modified on (DOS date/time):          2022 Apr 24 14:16:56
   32-bit CRC value (hex):                         d0103ac6
   compressed size:                                345 bytes
   uncompressed size:                              1056 bytes
   length of filename:                             25 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 0f 55 7f cc bb 54 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 a8 b9 d0 2f d5 57 d8 01 66 ba 85 24.
 
   There is no file comment.
 
 Central directory entry #56:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
@@ -1951,41 +1951,41 @@
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Mar 9 15:41:28
-  32-bit CRC value (hex):                         40e91b62
-  compressed size:                                353 bytes
-  uncompressed size:                              1093 bytes
+  file last modified on (DOS date/time):          2022 Apr 25 23:44:52
+  32-bit CRC value (hex):                         033303d2
+  compressed size:                                343 bytes
+  uncompressed size:                              1050 bytes
   length of filename:                             22 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 9a 69 a0 5f bb 33 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 83 a7 ad b0 ed 58 d8 01 66 ba 85 24.
 
   There is no file comment.
 
 Central directory entry #57:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Dev_E201264.txt
 
-  offset of local header from start of archive:   117271
-                                                  (000000000001CA17h) bytes
+  offset of local header from start of archive:   117261
+                                                  (000000000001CA0Dh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2000,27 +2000,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 4d de 25 ed df 19 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 4d de 25 ed df 19 d8 01 81 e1 85 24.
 
   There is no file comment.
 
 Central directory entry #58:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Doctor_GB_Card_64M.txt
 
-  offset of local header from start of archive:   117673
-                                                  (000000000001CBA9h) bytes
+  offset of local header from start of archive:   117663
+                                                  (000000000001CB9Fh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2035,27 +2035,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 c0 58 0c 5f 45 44 d8 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 c0 58 0c 5f 45 44 d8 01 81 e1 85 24.
 
   There is no file comment.
 
 Central directory entry #59:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_ES29LV160ET.txt
 
-  offset of local header from start of archive:   118098
-                                                  (000000000001CD52h) bytes
+  offset of local header from start of archive:   118088
+                                                  (000000000001CD48h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2070,27 +2070,97 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d4 8e 9e 41 b5 a5 d7 01 aa f7 4d 2f.
+    20 are:   00 00 00 00 01 00 18 00 d4 8e 9e 41 b5 a5 d7 01 9c 08 86 24.
 
   There is no file comment.
 
 Central directory entry #60:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
+  fc_DMG_FerranteCrafts_32KB.txt
+
+  offset of local header from start of archive:   118473
+                                                  (000000000001CEC9h) bytes
+  file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
+  version of encoding software:                   6.3
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             deflated
+  compression sub-type (deflation):               normal
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2022 Apr 24 14:14:32
+  32-bit CRC value (hex):                         fcfa031a
+  compressed size:                                319 bytes
+  uncompressed size:                              1005 bytes
+  length of filename:                             30 characters
+  length of extra field:                          36 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  non-MSDOS external file attributes:             000000 hex
+  MS-DOS file attributes (20 hex):                arc 
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
+    20 are:   00 00 00 00 01 00 18 00 dc d0 ff d9 d4 57 d8 01 9c 08 86 24.
+
+  There is no file comment.
+
+Central directory entry #61:
+---------------------------
+
+  There are an extra -36 bytes preceding this file.
+
+  fc_DMG_FerranteCrafts_64KB.txt
+
+  offset of local header from start of archive:   118852
+                                                  (000000000001D044h) bytes
+  file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
+  version of encoding software:                   6.3
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             deflated
+  compression sub-type (deflation):               normal
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2022 Apr 24 13:34:14
+  32-bit CRC value (hex):                         be6f0e5e
+  compressed size:                                333 bytes
+  uncompressed size:                              1041 bytes
+  length of filename:                             30 characters
+  length of extra field:                          36 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  non-MSDOS external file attributes:             000000 hex
+  MS-DOS file attributes (20 hex):                arc 
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
+    20 are:   00 00 00 00 01 00 18 00 51 70 d1 38 cf 57 d8 01 9c 08 86 24.
+
+  There is no file comment.
+
+Central directory entry #62:
+---------------------------
+
+  There are an extra -36 bytes preceding this file.
+
   fc_DMG_GB_Memory.txt
 
-  offset of local header from start of archive:   118483
-                                                  (000000000001CED3h) bytes
+  offset of local header from start of archive:   119245
+                                                  (000000000001D1CDh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2105,27 +2175,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 1c 8d 5a 86 a6 33 d8 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 1c 8d 5a 86 a6 33 d8 01 92 2f 86 24.
 
   There is no file comment.
 
-Central directory entry #61:
+Central directory entry #63:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_GB_Smart_32M.txt
 
-  offset of local header from start of archive:   118997
-                                                  (000000000001D0D5h) bytes
+  offset of local header from start of archive:   119759
+                                                  (000000000001D3CFh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2140,27 +2210,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 51 b4 e2 fc 67 26 d7 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 51 b4 e2 fc 67 26 d7 01 92 2f 86 24.
 
   There is no file comment.
 
-Central directory entry #62:
+Central directory entry #64:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_AUDIO_555_AA.txt
 
-  offset of local header from start of archive:   119396
-                                                  (000000000001D264h) bytes
+  offset of local header from start of archive:   120158
+                                                  (000000000001D55Eh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2175,27 +2245,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 43 70 19 bd 44 44 d8 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 43 70 19 bd 44 44 d8 01 92 2f 86 24.
 
   There is no file comment.
 
-Central directory entry #63:
+Central directory entry #65:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_AUDIO_AAA_AA.txt
 
-  offset of local header from start of archive:   119777
-                                                  (000000000001D3E1h) bytes
+  offset of local header from start of archive:   120539
+                                                  (000000000001D6DBh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2210,27 +2280,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 29 fe f3 bf 44 44 d8 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 29 fe f3 bf 44 44 d8 01 b2 56 86 24.
 
   There is no file comment.
 
-Central directory entry #64:
+Central directory entry #66:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_WR_555_A9.txt
 
-  offset of local header from start of archive:   120156
-                                                  (000000000001D55Ch) bytes
+  offset of local header from start of archive:   120918
+                                                  (000000000001D856h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2245,27 +2315,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 00 13 3a 0b 88 11 d8 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 00 13 3a 0b 88 11 d8 01 b2 56 86 24.
 
   There is no file comment.
 
-Central directory entry #65:
+Central directory entry #67:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_WR_555_AA.txt
 
-  offset of local header from start of archive:   120535
-                                                  (000000000001D6D7h) bytes
+  offset of local header from start of archive:   121297
+                                                  (000000000001D9D1h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2280,27 +2350,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 87 57 5c b9 a6 36 d7 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 87 57 5c b9 a6 36 d7 01 b9 7d 86 24.
 
   There is no file comment.
 
-Central directory entry #66:
+Central directory entry #68:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_WR_AAA_A9.txt
 
-  offset of local header from start of archive:   120910
-                                                  (000000000001D84Eh) bytes
+  offset of local header from start of archive:   121672
+                                                  (000000000001DB48h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2315,27 +2385,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 37 1f b5 f9 a6 36 d7 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 37 1f b5 f9 a6 36 d7 01 b9 7d 86 24.
 
   There is no file comment.
 
-Central directory entry #67:
+Central directory entry #69:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Generic_WR_AAA_AA.txt
 
-  offset of local header from start of archive:   121287
-                                                  (000000000001D9C7h) bytes
+  offset of local header from start of archive:   122049
+                                                  (000000000001DCC1h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2350,27 +2420,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 ea 42 f3 fa a6 36 d7 01 b6 1e 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 ea 42 f3 fa a6 36 d7 01 cb a4 86 24.
 
   There is no file comment.
 
-Central directory entry #68:
+Central directory entry #70:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_GL032M11BAIR4.txt
 
-  offset of local header from start of archive:   121660
-                                                  (000000000001DB3Ch) bytes
+  offset of local header from start of archive:   122422
+                                                  (000000000001DE36h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2385,27 +2455,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 37 48 a7 38 f4 03 d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 37 48 a7 38 f4 03 d8 01 cb a4 86 24.
 
   There is no file comment.
 
-Central directory entry #69:
+Central directory entry #71:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_HDR_GBD.txt
 
-  offset of local header from start of archive:   122174
-                                                  (000000000001DD3Eh) bytes
+  offset of local header from start of archive:   122936
+                                                  (000000000001E038h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2420,27 +2490,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 d8 ef 4e 4c 53 f4 d7 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 d8 ef 4e 4c 53 f4 d7 01 de cb 86 24.
 
   There is no file comment.
 
-Central directory entry #70:
+Central directory entry #72:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_HY29LV160TT.txt
 
-  offset of local header from start of archive:   122549
-                                                  (000000000001DEB5h) bytes
+  offset of local header from start of archive:   123311
+                                                  (000000000001E1AFh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2455,27 +2525,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 22 43 3b c7 69 4f d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 22 43 3b c7 69 4f d8 01 de cb 86 24.
 
   There is no file comment.
 
-Central directory entry #71:
+Central directory entry #73:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_1MB.txt
 
-  offset of local header from start of archive:   123029
-                                                  (000000000001E095h) bytes
+  offset of local header from start of archive:   123791
+                                                  (000000000001E38Fh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2490,27 +2560,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 ea 94 21 1e 8f 5b d7 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 ea 94 21 1e 8f 5b d7 01 ff f2 86 24.
 
   There is no file comment.
 
-Central directory entry #72:
+Central directory entry #74:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_2MB.txt
 
-  offset of local header from start of archive:   123403
-                                                  (000000000001E20Bh) bytes
+  offset of local header from start of archive:   124165
+                                                  (000000000001E505h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2525,27 +2595,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 97 76 6b b0 69 1b d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 97 76 6b b0 69 1b d8 01 ff f2 86 24.
 
   There is no file comment.
 
-Central directory entry #73:
+Central directory entry #75:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_2MB_WT.txt
 
-  offset of local header from start of archive:   123782
-                                                  (000000000001E386h) bytes
+  offset of local header from start of archive:   124544
+                                                  (000000000001E680h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2560,27 +2630,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 13 15 4e e8 0f 0a d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 13 15 4e e8 0f 0a d8 01 fb 19 87 24.
 
   There is no file comment.
 
-Central directory entry #74:
+Central directory entry #76:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_32KB.txt
 
-  offset of local header from start of archive:   124143
-                                                  (000000000001E4EFh) bytes
+  offset of local header from start of archive:   124905
+                                                  (000000000001E7E9h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2595,27 +2665,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 c9 30 e8 be 03 54 d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 c9 30 e8 be 03 54 d8 01 fb 19 87 24.
 
   There is no file comment.
 
-Central directory entry #75:
+Central directory entry #77:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_4MB.txt
 
-  offset of local header from start of archive:   124503
-                                                  (000000000001E657h) bytes
+  offset of local header from start of archive:   125265
+                                                  (000000000001E951h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2630,27 +2700,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 8b 70 7e 31 ea 23 d8 01 d2 45 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 8b 70 7e 31 ea 23 d8 01 fb 19 87 24.
 
   There is no file comment.
 
-Central directory entry #76:
+Central directory entry #78:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_4MB_2x2.txt
 
-  offset of local header from start of archive:   124942
-                                                  (000000000001E80Eh) bytes
+  offset of local header from start of archive:   125704
+                                                  (000000000001EB08h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2665,62 +2735,62 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 86 91 eb 59 05 11 d8 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 86 91 eb 59 05 11 d8 01 0e 41 87 24.
 
   There is no file comment.
 
-Central directory entry #77:
+Central directory entry #79:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_512KB.txt
 
-  offset of local header from start of archive:   125347
-                                                  (000000000001E9A3h) bytes
+  offset of local header from start of archive:   126109
+                                                  (000000000001EC9Dh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Apr 20 15:46:42
-  32-bit CRC value (hex):                         f3ed0cc4
-  compressed size:                                354 bytes
-  uncompressed size:                              1127 bytes
+  file last modified on (DOS date/time):          2022 Apr 25 23:44:52
+  32-bit CRC value (hex):                         1255b810
+  compressed size:                                345 bytes
+  uncompressed size:                              1103 bytes
   length of filename:                             19 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 b1 53 76 10 bd 54 d8 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 e4 7d b8 b0 ed 58 d8 01 0e 41 87 24.
 
   There is no file comment.
 
-Central directory entry #78:
+Central directory entry #80:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_8MB.txt
 
-  offset of local header from start of archive:   125750
-                                                  (000000000001EB36h) bytes
+  offset of local header from start of archive:   126503
+                                                  (000000000001EE27h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2735,27 +2805,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 1e 06 00 a8 94 5b d7 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 1e 06 00 a8 94 5b d7 01 21 68 87 24.
 
   There is no file comment.
 
-Central directory entry #79:
+Central directory entry #81:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_iG_Power_Cart.txt
 
-  offset of local header from start of archive:   126177
-                                                  (000000000001ECE1h) bytes
+  offset of local header from start of archive:   126930
+                                                  (000000000001EFD2h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2770,27 +2840,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 68 50 45 78 fe a0 d7 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 68 50 45 78 fe a0 d7 01 21 68 87 24.
 
   There is no file comment.
 
-Central directory entry #80:
+Central directory entry #82:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_K8D3216UBC.txt
 
-  offset of local header from start of archive:   126356
-                                                  (000000000001ED94h) bytes
+  offset of local header from start of archive:   127109
+                                                  (000000000001F085h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2805,27 +2875,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 9a 91 c5 a7 68 26 d7 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 9a 91 c5 a7 68 26 d7 01 21 68 87 24.
 
   There is no file comment.
 
-Central directory entry #81:
+Central directory entry #83:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_K8D3216UTC.txt
 
-  offset of local header from start of archive:   126781
-                                                  (000000000001EF3Dh) bytes
+  offset of local header from start of archive:   127534
+                                                  (000000000001F22Eh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2840,27 +2910,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 f4 09 86 b2 68 26 d7 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 f4 09 86 b2 68 26 d7 01 21 68 87 24.
 
   There is no file comment.
 
-Central directory entry #82:
+Central directory entry #84:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_M29W160EB.txt
 
-  offset of local header from start of archive:   127204
-                                                  (000000000001F0E4h) bytes
+  offset of local header from start of archive:   127957
+                                                  (000000000001F3D5h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2875,27 +2945,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 13 73 63 99 31 2e d7 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 13 73 63 99 31 2e d7 01 38 8f 87 24.
 
   There is no file comment.
 
-Central directory entry #83:
+Central directory entry #85:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_M29W320DT.txt
 
-  offset of local header from start of archive:   127651
-                                                  (000000000001F2A3h) bytes
+  offset of local header from start of archive:   128404
+                                                  (000000000001F594h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2910,27 +2980,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 5e f5 d0 85 8c 43 d8 01 e6 6c 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 5e f5 d0 85 8c 43 d8 01 38 8f 87 24.
 
   There is no file comment.
 
-Central directory entry #84:
+Central directory entry #86:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_M29W320DT_2.txt
 
-  offset of local header from start of archive:   128160
-                                                  (000000000001F4A0h) bytes
+  offset of local header from start of archive:   128913
+                                                  (000000000001F791h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2945,27 +3015,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 b8 b4 a8 80 44 44 d8 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 b8 b4 a8 80 44 44 d8 01 47 b6 87 24.
 
   There is no file comment.
 
-Central directory entry #85:
+Central directory entry #87:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_M29W640.txt
 
-  offset of local header from start of archive:   128672
-                                                  (000000000001F6A0h) bytes
+  offset of local header from start of archive:   129425
+                                                  (000000000001F991h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -2980,62 +3050,62 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 33 84 28 03 71 21 d7 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 33 84 28 03 71 21 d7 01 47 b6 87 24.
 
   There is no file comment.
 
-Central directory entry #86:
+Central directory entry #88:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MSP55LV512.txt
 
-  offset of local header from start of archive:   129137
-                                                  (000000000001F871h) bytes
+  offset of local header from start of archive:   129890
+                                                  (000000000001FB62h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Jan 12 17:14:24
+  file last modified on (DOS date/time):          2022 Apr 24 00:16:34
   32-bit CRC value (hex):                         33f5d863
   compressed size:                                353 bytes
   uncompressed size:                              1065 bytes
   length of filename:                             21 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 56 03 58 14 c7 07 d8 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 3b 06 99 ca 5f 57 d8 01 47 b6 87 24.
 
   There is no file comment.
 
-Central directory entry #87:
+Central directory entry #89:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29CL256FH.txt
 
-  offset of local header from start of archive:   129541
-                                                  (000000000001FA05h) bytes
+  offset of local header from start of archive:   130294
+                                                  (000000000001FCF6h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3050,62 +3120,62 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 03 63 3e c8 be 43 d8 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 03 63 3e c8 be 43 d8 01 5a dd 87 24.
 
   There is no file comment.
 
-Central directory entry #88:
+Central directory entry #90:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29GL256EL.txt
 
-  offset of local header from start of archive:   130024
-                                                  (000000000001FBE8h) bytes
+  offset of local header from start of archive:   130777
+                                                  (000000000001FED9h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Jan 12 14:12:20
-  32-bit CRC value (hex):                         d786c092
-  compressed size:                                380 bytes
-  uncompressed size:                              1140 bytes
+  file last modified on (DOS date/time):          2022 Apr 25 23:44:52
+  32-bit CRC value (hex):                         4b5c86da
+  compressed size:                                367 bytes
+  uncompressed size:                              1094 bytes
   length of filename:                             22 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 71 ee b1 a4 ad 07 d8 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 a2 90 c2 b0 ed 58 d8 01 68 04 88 24.
 
   There is no file comment.
 
-Central directory entry #89:
+Central directory entry #91:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29LV160CT.txt
 
-  offset of local header from start of archive:   130456
-                                                  (000000000001FD98h) bytes
+  offset of local header from start of archive:   131196
+                                                  (000000000002007Ch) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3120,27 +3190,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 01 12 92 dc 68 26 d7 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 01 12 92 dc 68 26 d7 01 68 04 88 24.
 
   There is no file comment.
 
-Central directory entry #90:
+Central directory entry #92:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29LV320BTC.txt
 
-  offset of local header from start of archive:   130888
-                                                  (000000000001FF48h) bytes
+  offset of local header from start of archive:   131628
+                                                  (000000000002022Ch) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3155,27 +3225,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 23 7a fb fe 18 e2 d7 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 23 7a fb fe 18 e2 d7 01 79 2b 88 24.
 
   There is no file comment.
 
-Central directory entry #91:
+Central directory entry #93:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29LV320ET.txt
 
-  offset of local header from start of archive:   131304
-                                                  (00000000000200E8h) bytes
+  offset of local header from start of archive:   132044
+                                                  (00000000000203CCh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3190,27 +3260,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 15 45 42 02 10 8d d7 01 ee 93 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 15 45 42 02 10 8d d7 01 79 2b 88 24.
 
   There is no file comment.
 
-Central directory entry #92:
+Central directory entry #94:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_MX29LV640_AUDIO.txt
 
-  offset of local header from start of archive:   131739
-                                                  (000000000002029Bh) bytes
+  offset of local header from start of archive:   132479
+                                                  (000000000002057Fh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3225,27 +3295,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 71 b4 86 7e 4f f3 d7 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 71 b4 86 7e 4f f3 d7 01 79 2b 88 24.
 
   There is no file comment.
 
-Central directory entry #93:
+Central directory entry #95:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_Retrostage.txt
 
-  offset of local header from start of archive:   132143
-                                                  (000000000002042Fh) bytes
+  offset of local header from start of archive:   132883
+                                                  (0000000000020713h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3260,27 +3330,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 90 5d a5 7b fe a0 d7 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 90 5d a5 7b fe a0 d7 01 8b 52 88 24.
 
   There is no file comment.
 
-Central directory entry #94:
+Central directory entry #96:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_S29GL032M90T.txt
 
-  offset of local header from start of archive:   132301
-                                                  (00000000000204CDh) bytes
+  offset of local header from start of archive:   133041
+                                                  (00000000000207B1h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3295,27 +3365,27 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 84 df 30 d8 d5 61 d7 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 84 df 30 d8 d5 61 d7 01 8b 52 88 24.
 
   There is no file comment.
 
-Central directory entry #95:
+Central directory entry #97:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_S29GL032N90T_MBC1.txt
 
-  offset of local header from start of archive:   132763
-                                                  (000000000002069Bh) bytes
+  offset of local header from start of archive:   133503
+                                                  (000000000002097Fh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3330,132 +3400,167 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 ca 1a 50 e1 3f 44 d8 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 ca 1a 50 e1 3f 44 d8 01 b7 79 88 24.
 
   There is no file comment.
 
-Central directory entry #96:
+Central directory entry #98:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
-  fc_DMG_SST39SF010_AUDIO.txt
+  fc_DMG_SST39SF020_MBC1_AUDIO.txt
 
-  offset of local header from start of archive:   133187
-                                                  (0000000000020843h) bytes
+  offset of local header from start of archive:   133927
+                                                  (0000000000020B27h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Mar 7 15:15:30
-  32-bit CRC value (hex):                         fbf9c580
-  compressed size:                                359 bytes
-  uncompressed size:                              1126 bytes
-  length of filename:                             27 characters
+  file last modified on (DOS date/time):          2022 Apr 24 12:40:10
+  32-bit CRC value (hex):                         0b022811
+  compressed size:                                346 bytes
+  uncompressed size:                              1058 bytes
+  length of filename:                             32 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 7f 8c f3 69 25 32 d8 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 e1 02 44 ab c7 57 d8 01 b7 79 88 24.
 
   There is no file comment.
 
-Central directory entry #97:
+Central directory entry #99:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_SST39SF040_MBC1_AUDIO.txt
 
-  offset of local header from start of archive:   133603
-                                                  (00000000000209E3h) bytes
+  offset of local header from start of archive:   134335
+                                                  (0000000000020CBFh) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Mar 24 13:37:56
-  32-bit CRC value (hex):                         a147af72
-  compressed size:                                346 bytes
+  file last modified on (DOS date/time):          2022 Apr 25 23:44:52
+  32-bit CRC value (hex):                         fdc9054c
+  compressed size:                                353 bytes
+  uncompressed size:                              1070 bytes
+  length of filename:                             32 characters
+  length of extra field:                          36 bytes
+  length of file comment:                         0 characters
+  disk number on which file begins:               disk 1
+  apparent file type:                             binary
+  non-MSDOS external file attributes:             000000 hex
+  MS-DOS file attributes (20 hex):                arc 
+
+  The central-directory extra field contains:
+  - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
+    20 are:   00 00 00 00 01 00 18 00 2b 04 d7 b0 ed 58 d8 01 b7 79 88 24.
+
+  There is no file comment.
+
+Central directory entry #100:
+---------------------------
+
+  There are an extra -36 bytes preceding this file.
+
+  fc_DMG_SST39SF040_MBC5_AUDIO.txt
+
+  offset of local header from start of archive:   134750
+                                                  (0000000000020E5Eh) bytes
+  file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
+  version of encoding software:                   6.3
+  minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
+  minimum software version required to extract:   2.0
+  compression method:                             deflated
+  compression sub-type (deflation):               normal
+  file security status:                           not encrypted
+  extended local header:                          no
+  file last modified on (DOS date/time):          2022 Apr 24 13:04:18
+  32-bit CRC value (hex):                         d5a3b7d2
+  compressed size:                                341 bytes
   uncompressed size:                              1056 bytes
   length of filename:                             32 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 76 e7 66 9a 73 3f d8 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 51 ad 8f 0a cb 57 d8 01 d3 a0 88 24.
 
   There is no file comment.
 
-Central directory entry #98:
+Central directory entry #101:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_TC58FVB016FT.txt
 
-  offset of local header from start of archive:   134011
-                                                  (0000000000020B7Bh) bytes
+  offset of local header from start of archive:   135153
+                                                  (0000000000020FF1h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
   extended local header:                          no
-  file last modified on (DOS date/time):          2022 Jan 25 03:32:48
-  32-bit CRC value (hex):                         445c033e
-  compressed size:                                311 bytes
-  uncompressed size:                              870 bytes
+  file last modified on (DOS date/time):          2022 Apr 25 23:44:52
+  32-bit CRC value (hex):                         355d1d82
+  compressed size:                                323 bytes
+  uncompressed size:                              919 bytes
   length of filename:                             23 characters
   length of extra field:                          36 bytes
   length of file comment:                         0 characters
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 60 3a 60 75 8b 11 d8 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 6c 2c e0 b0 ed 58 d8 01 d3 a0 88 24.
 
   There is no file comment.
 
-Central directory entry #99:
+Central directory entry #102:
 ---------------------------
 
   There are an extra -36 bytes preceding this file.
 
   fc_DMG_XploderGB.txt
 
-  offset of local header from start of archive:   134375
-                                                  (0000000000020CE7h) bytes
+  offset of local header from start of archive:   135529
+                                                  (0000000000021169h) bytes
   file system or operating system of origin:      MS-DOS, OS/2 or NT FAT
   version of encoding software:                   6.3
   minimum file system compatibility required:     MS-DOS, OS/2 or NT FAT
   minimum software version required to extract:   2.0
   compression method:                             deflated
   compression sub-type (deflation):               normal
   file security status:                           not encrypted
@@ -3470,11 +3575,11 @@
   disk number on which file begins:               disk 1
   apparent file type:                             binary
   non-MSDOS external file attributes:             000000 hex
   MS-DOS file attributes (20 hex):                arc 
 
   The central-directory extra field contains:
   - A subfield with ID 0x000a (PKWARE Win32) and 32 data bytes.  The first
-    20 are:   00 00 00 00 01 00 18 00 03 7b 47 22 bc 55 d8 01 04 bb 4e 2f.
+    20 are:   00 00 00 00 01 00 18 00 03 7b 47 22 bc 55 d8 01 d3 a0 88 24.
 
   There is no file comment.
```

#### zipnote {}

```diff
@@ -171,14 +171,20 @@
 
 Filename: fc_DMG_Doctor_GB_Card_64M.txt
 Comment: 
 
 Filename: fc_DMG_ES29LV160ET.txt
 Comment: 
 
+Filename: fc_DMG_FerranteCrafts_32KB.txt
+Comment: 
+
+Filename: fc_DMG_FerranteCrafts_64KB.txt
+Comment: 
+
 Filename: fc_DMG_GB_Memory.txt
 Comment: 
 
 Filename: fc_DMG_GB_Smart_32M.txt
 Comment: 
 
 Filename: fc_DMG_Generic_AUDIO_555_AA.txt
@@ -279,20 +285,23 @@
 
 Filename: fc_DMG_S29GL032M90T.txt
 Comment: 
 
 Filename: fc_DMG_S29GL032N90T_MBC1.txt
 Comment: 
 
-Filename: fc_DMG_SST39SF010_AUDIO.txt
+Filename: fc_DMG_SST39SF020_MBC1_AUDIO.txt
 Comment: 
 
 Filename: fc_DMG_SST39SF040_MBC1_AUDIO.txt
 Comment: 
 
+Filename: fc_DMG_SST39SF040_MBC5_AUDIO.txt
+Comment: 
+
 Filename: fc_DMG_TC58FVB016FT.txt
 Comment: 
 
 Filename: fc_DMG_XploderGB.txt
 Comment: 
 
 Zip file comment:
```

#### fc_DMG_AT49F040_WR.txt

```diff
@@ -20,17 +20,14 @@
 			[ 0, 0xF0 ]
 		],
 		"read_identifier":[
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x90 ]
 		],
-		"read_cfi":[
-			[ 0x5555, 0x98 ]
-		],
 		"chip_erase":[
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x80 ],
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x10 ]
```

#### fc_DMG_iG_512KB.txt

```diff
@@ -6,15 +6,14 @@
 	"flash_ids":[
 		[ 0xBF, 0xB5, 0x01, 0xFF ],
 		[ 0xBF, 0xB6, 0x01, 0xFF ],
 		[ 0xBF, 0xB7, 0x01, 0xFF ]
 	],
 	"voltage":5,
 	"power_cycle":true,
-	"flash_size":0x80000,
 	"start_addr":0,
 	"first_bank":1,
 	"flash_commands_on_bank_1":true,
 	"write_pin":"AUDIO",
 	"chip_erase_timeout":30,
 	"command_set":"AMD",
 	"commands":{
```

#### fc_DMG_MX29GL256EL.txt

```diff
@@ -1,12 +1,11 @@
 {
 	"type":"DMG",
 	"names":[
-		"SD008-6810-V4 with MX29GL256EL",
-		"SD008-6810-V4 with unlabeled flash chip"
+		"SD008-6810-V4 with MX29GL256EL"
 	],
 	"flash_ids":[
 		[ 0xF3, 0xC3, 0x00, 0x01 ],
 		[ 0x8A, 0x8A, 0x00, 0x00 ]
 	],
 	"voltage":3.3,
 	"flash_size":0x2000000,
```

#### fc_DMG_SST39SF040_MBC1_AUDIO.txt

```diff
@@ -6,14 +6,15 @@
 	"flash_ids":[
 		[ 0xBF, 0xB7, 0x01, 0xFF ]
 	],
 	"voltage":5,
 	"flash_size":0x80000,
 	"start_addr":0,
 	"first_bank":1,
+	"mbc":0x03,
 	"flash_commands_on_bank_1":true,
 	"write_pin":"AUDIO",
 	"chip_erase_timeout":30,
 	"command_set":"AMD",
 	"commands":{
 		"reset":[
 			[ 0, 0xF0 ]
```

#### fc_DMG_TC58FVB016FT.txt

```diff
@@ -1,13 +1,16 @@
 {
 	"type":"DMG",
 	"names":[
 		"SD007_T40_64BALL_TSOP28 with TC58FVB016FT-85"
 	],
-	"voltage":3.3,
+	"flash_ids":[
+		[ 0x98, 0x45, 0x00, 0x2A ]
+	],
+	"voltage":5,
 	"flash_size":0x200000,
 	"start_addr":0,
 	"first_bank":1,
 	"write_pin":"WR",
 	"chip_erase_timeout":60,
 	"command_set":"AMD",
 	"commands":{
```

#### Comparing `fc_DMG_SST39SF010_AUDIO.txt` & `fc_DMG_FerranteCrafts_64KB.txt`

 * *Files 4% similar despite different names*

```diff
@@ -1,36 +1,32 @@
 {
 	"type":"DMG",
 	"names":[
-		"Ferrante Crafts cart with SST39SF010A",
-		"GB-CART32K-A with SST39SF020A"
+		"Ferrante Crafts cart 64 KB"
 	],
 	"flash_ids":[
-		[ 0xBF, 0xB5, 0x01, 0xFF ],
-		[ 0xBF, 0xB6, 0x01, 0xFF ]
+		[ 0xBF, 0xB5, 0x01, 0xFF ]
 	],
 	"voltage":5,
-	"flash_size":0x8000,
+	"flash_size":0x10000,
 	"start_addr":0,
 	"first_bank":1,
+	"flash_commands_on_bank_1":true,
 	"write_pin":"AUDIO",
-	"chip_erase_timeout":60,
+	"chip_erase_timeout":20,
 	"command_set":"AMD",
 	"commands":{
 		"reset":[
 			[ 0, 0xF0 ]
 		],
 		"read_identifier":[
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x90 ]
 		],
-		"read_cfi":[
-			[ 0x5555, 0x98 ]
-		],
 		"chip_erase":[
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x80 ],
 			[ 0x5555, 0xAA ],
 			[ 0x2AAA, 0x55 ],
 			[ 0x5555, 0x10 ]
```

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_Mini_v1_0.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_Mini_v1_0.zip`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_XMAS_v1_0.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_XMAS_v1_0.zip`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_1_v1_2.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_1_v1_2.zip`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_3.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_3.zip`

 * *Files 6% similar despite different names*

#### zipinfo {}

```diff
@@ -1,5 +1,5 @@
-Zip file size: 15557 bytes, number of entries: 3
--rw-a--     3.1 fat      658 bx defN 21-Jun-07 16:27 fw.ini
+Zip file size: 15567 bytes, number of entries: 3
+-rw-a--     3.1 fat      698 bx defN 22-Apr-29 01:19 fw.ini
 -rw-a--     3.1 fat    19908 bx defN 21-Apr-29 18:32 ofw.hex
 ?rw-------  2.0 fat    20153 b- defN 21-Apr-27 12:52 cfw.hex
-3 files, 40719 bytes uncompressed, 15195 bytes compressed:  62.7%
+3 files, 40759 bytes uncompressed, 15205 bytes compressed:  62.7%
```

#### fw.ini

```diff
@@ -1,5 +1,5 @@
 [Firmware]
-cfw_ver=L1 (custom high compatibility firmware)
+cfw_ver=Firmware version L1 (Lesserkuma’s firmware)
 cfw_text=<ul><li>Works with all licensed Game Boy and Game Boy Advance cartridges, except media players and external peripherals</li><li>Supported mappers: MBC1, MBC2, MBC3, MBC30, MBC5, MBC6, MBC7, MBC1M, MMM01, GBD (Game Boy Camera), G-MMC1 (GB Memory), M161, HuC-1, HuC-3, TAMA5, DACS, 3D Memory (GBA Video)</li><li>Adds support for some more reproduction and flash cartridges</li><li>Currently not supported by official interface software by insideGadgets</li></ul>
-ofw_ver=R30 (official firmware)
+ofw_ver=Firmware version R30 (insideGadgets’ official firmware)
 ofw_text=<ul><li>Works with all official interface software by insideGadgets</li></ul>
```

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_4.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_4.zip`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/fw_GBxCart_RW_v1_4a.zip` & `FlashGBX-3.9/FlashGBX/res/fw_GBxCart_RW_v1_4a.zip`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/icon.ico` & `FlashGBX-3.9/FlashGBX/res/icon.ico`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/icon.png` & `FlashGBX-3.9/FlashGBX/res/icon.png`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX/res/pc_frame.png` & `FlashGBX-3.9/FlashGBX/res/pc_frame.png`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/FlashGBX.egg-info/PKG-INFO` & `FlashGBX-3.9/FlashGBX.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: FlashGBX
-Version: 3.8
+Version: 3.9
 Summary: Reads and writes Game Boy and Game Boy Advance cartridge data. Supported hardware: GBxCart RW v1.3 and v1.4 by insideGadgets.
 Home-page: https://github.com/lesserkuma/FlashGBX
 Author: Lesserkuma
 License: UNKNOWN
 Project-URL: Source, https://github.com/lesserkuma/FlashGBX/
 Project-URL: Tracker, https://github.com/lesserkuma/FlashGBX/issues
 Platform: UNKNOWN
@@ -116,15 +116,17 @@
   - DIY cart with AM29F032
   - DIY cart with AM29F040
   - DIY cart with AM29F080
   - DIY cart with AT49F040
   - DIY cart with MX29LV640
   - DIY cart with SST39SF040
   - DMG-MBC5-32M-FLASH Development Cartridge, E201264
-  - Ferrante Crafts cart with SST39SF010A
+  - Ferrante Crafts cart 32 KB
+  - Ferrante Crafts cart 64 KB
+  - Ferrante Crafts cart 512 KB
   - GB-CART32K-A with SST39SF020A
   - GB Smart 32M
   - HDR Game Boy Camera Flashcart
   - insideGadgets 32 KB
   - insideGadgets 128 KB
   - insideGadgets 256 KB
   - insideGadgets 512 KB
@@ -255,15 +257,15 @@
   - GA-07 with unlabeled flash chip
   - GE28F128W30 with 128W30B0
   - M5M29G130AN (no PCB text)
   - M6MGJ927 (no PCB text)
 
 Many different reproduction cartridges share their flash chip command set, so even if yours is not on this list, it may still work fine or even be auto-detected as another one. Support for more cartridges can also be added by creating external config files that include the necessary flash chip commands.
 
-*¹ = Cannot be auto-detected, select cartridge type manually*
+*¹ = Cannot always be auto-detected, select cartridge type manually*
 
 ### Troubleshooting
 
 * If something doesn’t work as expected, first try to clean the game cartridge contacts (best with IPA 99.9%+ on a cotton swab) and reconnect the device. An unstable cartridge connection is the most common reason for read or write errors.
 
 * Depending on your system configuration, you may have to use `pip` and `python` commands instead of `pip3` and `python3`.
 
@@ -287,14 +289,15 @@
 
 ## Thanks
 
 The author would like to thank the following very kind people for their help and contributions (in alphabetical order):
 
 - 90sFlav (flash chip info)
 - AcoVanConis (bug reports, flash chip info)
+- AdmirtheSableye (bug reports)
 - AlexiG (GBxCart RW hardware, bug reports, flash chip info)
 - AndehX (app icon, flash chip info)
 - antPL (flash chip info)
 - bbsan (flash chip info)
 - BennVenn (unlicensed mapper reverse engineering)
 - ClassicOldSong (bug reports)
 - crizzlycruz (flash chip info)
@@ -303,17 +306,19 @@
 - djedditt (testing)
 - dyf2007 (flash chip info)
 - easthighNerd (feature suggestions)
 - EchelonPrime (flash chip info)
 - EmperorOfTigers (bug reports, flash chip info)
 - endrift (research, mGBA emulator)
 - eveningmoose (flash chip info)
+- FerrantePescara (flash chip info)
 - frarees (bug reports)
 - Frost Clock (flash chip info)
 - Grender (testing)
+- HDR (testing)
 - Herax (flash chip info)
 - hiks (flash chip info)
 - howie0210 (flash chip info, bug reports)
 - iamevn (flash chip info)
 - Icesythe7 (feature suggestions, testing, bug reports)
 - Jayro (flash chip info)
 - JFox (help with properly packaging the app for pip, Linux help, bug reports)
```

### Comparing `FlashGBX-3.8/FlashGBX.egg-info/SOURCES.txt` & `FlashGBX-3.9/FlashGBX.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/LICENSE` & `FlashGBX-3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `FlashGBX-3.8/PKG-INFO` & `FlashGBX-3.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: FlashGBX
-Version: 3.8
+Version: 3.9
 Summary: Reads and writes Game Boy and Game Boy Advance cartridge data. Supported hardware: GBxCart RW v1.3 and v1.4 by insideGadgets.
 Home-page: https://github.com/lesserkuma/FlashGBX
 Author: Lesserkuma
 License: UNKNOWN
 Project-URL: Source, https://github.com/lesserkuma/FlashGBX/
 Project-URL: Tracker, https://github.com/lesserkuma/FlashGBX/issues
 Platform: UNKNOWN
@@ -116,15 +116,17 @@
   - DIY cart with AM29F032
   - DIY cart with AM29F040
   - DIY cart with AM29F080
   - DIY cart with AT49F040
   - DIY cart with MX29LV640
   - DIY cart with SST39SF040
   - DMG-MBC5-32M-FLASH Development Cartridge, E201264
-  - Ferrante Crafts cart with SST39SF010A
+  - Ferrante Crafts cart 32 KB
+  - Ferrante Crafts cart 64 KB
+  - Ferrante Crafts cart 512 KB
   - GB-CART32K-A with SST39SF020A
   - GB Smart 32M
   - HDR Game Boy Camera Flashcart
   - insideGadgets 32 KB
   - insideGadgets 128 KB
   - insideGadgets 256 KB
   - insideGadgets 512 KB
@@ -255,15 +257,15 @@
   - GA-07 with unlabeled flash chip
   - GE28F128W30 with 128W30B0
   - M5M29G130AN (no PCB text)
   - M6MGJ927 (no PCB text)
 
 Many different reproduction cartridges share their flash chip command set, so even if yours is not on this list, it may still work fine or even be auto-detected as another one. Support for more cartridges can also be added by creating external config files that include the necessary flash chip commands.
 
-*¹ = Cannot be auto-detected, select cartridge type manually*
+*¹ = Cannot always be auto-detected, select cartridge type manually*
 
 ### Troubleshooting
 
 * If something doesn’t work as expected, first try to clean the game cartridge contacts (best with IPA 99.9%+ on a cotton swab) and reconnect the device. An unstable cartridge connection is the most common reason for read or write errors.
 
 * Depending on your system configuration, you may have to use `pip` and `python` commands instead of `pip3` and `python3`.
 
@@ -287,14 +289,15 @@
 
 ## Thanks
 
 The author would like to thank the following very kind people for their help and contributions (in alphabetical order):
 
 - 90sFlav (flash chip info)
 - AcoVanConis (bug reports, flash chip info)
+- AdmirtheSableye (bug reports)
 - AlexiG (GBxCart RW hardware, bug reports, flash chip info)
 - AndehX (app icon, flash chip info)
 - antPL (flash chip info)
 - bbsan (flash chip info)
 - BennVenn (unlicensed mapper reverse engineering)
 - ClassicOldSong (bug reports)
 - crizzlycruz (flash chip info)
@@ -303,17 +306,19 @@
 - djedditt (testing)
 - dyf2007 (flash chip info)
 - easthighNerd (feature suggestions)
 - EchelonPrime (flash chip info)
 - EmperorOfTigers (bug reports, flash chip info)
 - endrift (research, mGBA emulator)
 - eveningmoose (flash chip info)
+- FerrantePescara (flash chip info)
 - frarees (bug reports)
 - Frost Clock (flash chip info)
 - Grender (testing)
+- HDR (testing)
 - Herax (flash chip info)
 - hiks (flash chip info)
 - howie0210 (flash chip info, bug reports)
 - iamevn (flash chip info)
 - Icesythe7 (feature suggestions, testing, bug reports)
 - Jayro (flash chip info)
 - JFox (help with properly packaging the app for pip, Linux help, bug reports)
```

### Comparing `FlashGBX-3.8/README.md` & `FlashGBX-3.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -94,15 +94,17 @@
   - DIY cart with AM29F032
   - DIY cart with AM29F040
   - DIY cart with AM29F080
   - DIY cart with AT49F040
   - DIY cart with MX29LV640
   - DIY cart with SST39SF040
   - DMG-MBC5-32M-FLASH Development Cartridge, E201264
-  - Ferrante Crafts cart with SST39SF010A
+  - Ferrante Crafts cart 32 KB
+  - Ferrante Crafts cart 64 KB
+  - Ferrante Crafts cart 512 KB
   - GB-CART32K-A with SST39SF020A
   - GB Smart 32M
   - HDR Game Boy Camera Flashcart
   - insideGadgets 32 KB
   - insideGadgets 128 KB
   - insideGadgets 256 KB
   - insideGadgets 512 KB
@@ -233,15 +235,15 @@
   - GA-07 with unlabeled flash chip
   - GE28F128W30 with 128W30B0
   - M5M29G130AN (no PCB text)
   - M6MGJ927 (no PCB text)
 
 Many different reproduction cartridges share their flash chip command set, so even if yours is not on this list, it may still work fine or even be auto-detected as another one. Support for more cartridges can also be added by creating external config files that include the necessary flash chip commands.
 
-*¹ = Cannot be auto-detected, select cartridge type manually*
+*¹ = Cannot always be auto-detected, select cartridge type manually*
 
 ### Troubleshooting
 
 * If something doesn’t work as expected, first try to clean the game cartridge contacts (best with IPA 99.9%+ on a cotton swab) and reconnect the device. An unstable cartridge connection is the most common reason for read or write errors.
 
 * Depending on your system configuration, you may have to use `pip` and `python` commands instead of `pip3` and `python3`.
 
@@ -265,14 +267,15 @@
 
 ## Thanks
 
 The author would like to thank the following very kind people for their help and contributions (in alphabetical order):
 
 - 90sFlav (flash chip info)
 - AcoVanConis (bug reports, flash chip info)
+- AdmirtheSableye (bug reports)
 - AlexiG (GBxCart RW hardware, bug reports, flash chip info)
 - AndehX (app icon, flash chip info)
 - antPL (flash chip info)
 - bbsan (flash chip info)
 - BennVenn (unlicensed mapper reverse engineering)
 - ClassicOldSong (bug reports)
 - crizzlycruz (flash chip info)
@@ -281,17 +284,19 @@
 - djedditt (testing)
 - dyf2007 (flash chip info)
 - easthighNerd (feature suggestions)
 - EchelonPrime (flash chip info)
 - EmperorOfTigers (bug reports, flash chip info)
 - endrift (research, mGBA emulator)
 - eveningmoose (flash chip info)
+- FerrantePescara (flash chip info)
 - frarees (bug reports)
 - Frost Clock (flash chip info)
 - Grender (testing)
+- HDR (testing)
 - Herax (flash chip info)
 - hiks (flash chip info)
 - howie0210 (flash chip info, bug reports)
 - iamevn (flash chip info)
 - Icesythe7 (feature suggestions, testing, bug reports)
 - Jayro (flash chip info)
 - JFox (help with properly packaging the app for pip, Linux help, bug reports)
```

### Comparing `FlashGBX-3.8/setup.py` & `FlashGBX-3.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh: long_description = fh.read()
 
 setuptools.setup(
 	name="FlashGBX",
-	version="3.8",
+	version="3.9",
 	author="Lesserkuma",
 	description="Reads and writes Game Boy and Game Boy Advance cartridge data. Supported hardware: GBxCart RW v1.3 and v1.4 by insideGadgets.",
 	url="https://github.com/lesserkuma/FlashGBX",
 	packages=setuptools.find_packages(),
 	install_requires=['PySide2', 'pyserial', 'Pillow', 'setuptools', 'requests', 'python-dateutil'],
 	include_package_data=True,
 	classifiers=[
```

