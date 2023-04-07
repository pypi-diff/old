# Comparing `tmp/mecord-cli-0.1.8.tar.gz` & `tmp/mecord-cli-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mecord-cli-0.1.8.tar", last modified: Mon Mar 13 09:37:51 2023, max compression
+gzip compressed data, was "mecord-cli-0.1.9.tar", last modified: Mon Mar 13 11:30:29 2023, max compression
```

## Comparing `mecord-cli-0.1.8.tar` & `mecord-cli-0.1.9.tar`

### file list

```diff
@@ -1,41 +1,42 @@
-drwxrwxrwx   0        0        0        0 2023-03-13 09:37:51.048383 mecord-cli-0.1.8/
--rw-rw-rw-   0        0        0     1078 2023-02-16 06:18:02.000000 mecord-cli-0.1.8/LICENSE
--rw-rw-rw-   0        0        0     1757 2023-03-13 09:37:51.048383 mecord-cli-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0     1336 2023-03-04 10:14:50.000000 mecord-cli-0.1.8/README.md
-drwxrwxrwx   0        0        0        0 2023-03-13 09:37:51.031440 mecord-cli-0.1.8/mecord/
--rw-rw-rw-   0        0        0        0 2023-02-27 08:17:36.000000 mecord-cli-0.1.8/mecord/__init__.py
--rw-rw-rw-   0        0        0    18260 2023-03-10 11:49:43.000000 mecord-cli-0.1.8/mecord/aigc_ext_pb2.py
--rw-rw-rw-   0        0        0    39477 2023-03-10 11:27:08.000000 mecord-cli-0.1.8/mecord/common_ext_pb2.py
--rw-rw-rw-   0        0        0     1119 2023-02-27 06:35:59.000000 mecord-cli-0.1.8/mecord/ftp_upload.py
--rw-rw-rw-   0        0        0     5423 2023-03-10 09:35:28.000000 mecord-cli-0.1.8/mecord/main.py
--rw-rw-rw-   0        0        0     6605 2023-03-13 09:24:15.000000 mecord-cli-0.1.8/mecord/mecord_service.py
--rw-rw-rw-   0        0        0     6310 2023-03-13 09:25:06.000000 mecord-cli-0.1.8/mecord/mecord_widget.py
--rw-rw-rw-   0        0        0     3250 2023-03-10 11:27:08.000000 mecord-cli-0.1.8/mecord/rpcinput_pb2.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:37:51.034431 mecord-cli-0.1.8/mecord/script_template/
--rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 mecord-cli-0.1.8/mecord/script_template/__init__.py
--rw-rw-rw-   0        0        0      966 2023-03-13 08:44:35.000000 mecord-cli-0.1.8/mecord/script_template/main.py
--rw-rw-rw-   0        0        0      801 2023-03-13 08:52:23.000000 mecord-cli-0.1.8/mecord/script_template/run.py
--rw-rw-rw-   0        0        0     2039 2023-03-13 09:37:32.000000 mecord-cli-0.1.8/mecord/store.py
--rw-rw-rw-   0        0        0     8745 2023-03-10 11:27:08.000000 mecord-cli-0.1.8/mecord/uauth_common_pb2.py
--rw-rw-rw-   0        0        0   108609 2023-03-10 11:27:29.000000 mecord-cli-0.1.8/mecord/uauth_ext_pb2.py
--rw-rw-rw-   0        0        0     1556 2023-03-10 12:17:03.000000 mecord-cli-0.1.8/mecord/upload.py
--rw-rw-rw-   0        0        0    12849 2023-03-10 11:27:27.000000 mecord-cli-0.1.8/mecord/user_status_ext_pb2.py
--rw-rw-rw-   0        0        0     3766 2023-03-10 09:46:01.000000 mecord-cli-0.1.8/mecord/utils.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:37:51.038416 mecord-cli-0.1.8/mecord/widget_template/
--rw-rw-rw-   0        0        0     1977 2023-03-13 09:18:19.000000 mecord-cli-0.1.8/mecord/widget_template/MekongJS.js.py
--rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 mecord-cli-0.1.8/mecord/widget_template/__init__.py
--rw-rw-rw-   0        0        0      147 2023-03-01 01:46:57.000000 mecord-cli-0.1.8/mecord/widget_template/config.json.py
--rw-rw-rw-   0        0        0     1678 2023-03-13 02:53:47.000000 mecord-cli-0.1.8/mecord/widget_template/icon.png.py
--rw-rw-rw-   0        0        0      703 2023-03-13 09:05:41.000000 mecord-cli-0.1.8/mecord/widget_template/index.html.py
--rw-rw-rw-   0        0        0     6718 2023-03-10 11:50:50.000000 mecord-cli-0.1.8/mecord/xy_pb.py
--rw-rw-rw-   0        0        0     2738 2023-02-20 13:11:01.000000 mecord-cli-0.1.8/mecord/xy_socket.py
--rw-rw-rw-   0        0        0     2234 2023-03-02 08:06:21.000000 mecord-cli-0.1.8/mecord/xy_user.py
-drwxrwxrwx   0        0        0        0 2023-03-13 09:37:51.046389 mecord-cli-0.1.8/mecord_cli.egg-info/
--rw-rw-rw-   0        0        0     1757 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      870 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       44 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       66 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-03-13 09:37:50.000000 mecord-cli-0.1.8/mecord_cli.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-13 09:37:51.049380 mecord-cli-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0     1427 2023-03-13 09:15:08.000000 mecord-cli-0.1.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-13 11:30:29.835509 mecord-cli-0.1.9/
+-rw-rw-rw-   0        0        0     1078 2023-02-16 06:18:02.000000 mecord-cli-0.1.9/LICENSE
+-rw-rw-rw-   0        0        0     1757 2023-03-13 11:30:29.835509 mecord-cli-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0     1336 2023-03-04 10:14:50.000000 mecord-cli-0.1.9/README.md
+drwxrwxrwx   0        0        0        0 2023-03-13 11:30:29.826539 mecord-cli-0.1.9/mecord/
+-rw-rw-rw-   0        0        0        0 2023-02-27 08:17:36.000000 mecord-cli-0.1.9/mecord/__init__.py
+-rw-rw-rw-   0        0        0    17672 2023-03-13 10:24:58.000000 mecord-cli-0.1.9/mecord/aigc_ext_pb2.py
+-rw-rw-rw-   0        0        0    39477 2023-03-13 10:24:23.000000 mecord-cli-0.1.9/mecord/common_ext_pb2.py
+-rw-rw-rw-   0        0        0       66 2023-03-13 11:25:22.000000 mecord-cli-0.1.9/mecord/constant.py
+-rw-rw-rw-   0        0        0     1119 2023-02-27 06:35:59.000000 mecord-cli-0.1.9/mecord/ftp_upload.py
+-rw-rw-rw-   0        0        0     5423 2023-03-10 09:35:28.000000 mecord-cli-0.1.9/mecord/main.py
+-rw-rw-rw-   0        0        0     6632 2023-03-13 11:28:39.000000 mecord-cli-0.1.9/mecord/mecord_service.py
+-rw-rw-rw-   0        0        0     6257 2023-03-13 11:20:07.000000 mecord-cli-0.1.9/mecord/mecord_widget.py
+-rw-rw-rw-   0        0        0     3250 2023-03-13 10:24:23.000000 mecord-cli-0.1.9/mecord/rpcinput_pb2.py
+drwxrwxrwx   0        0        0        0 2023-03-13 11:30:29.828533 mecord-cli-0.1.9/mecord/script_template/
+-rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 mecord-cli-0.1.9/mecord/script_template/__init__.py
+-rw-rw-rw-   0        0        0      966 2023-03-13 08:44:35.000000 mecord-cli-0.1.9/mecord/script_template/main.py
+-rw-rw-rw-   0        0        0      801 2023-03-13 08:52:23.000000 mecord-cli-0.1.9/mecord/script_template/run.py
+-rw-rw-rw-   0        0        0     2354 2023-03-13 10:22:49.000000 mecord-cli-0.1.9/mecord/store.py
+-rw-rw-rw-   0        0        0     8745 2023-03-13 10:24:23.000000 mecord-cli-0.1.9/mecord/uauth_common_pb2.py
+-rw-rw-rw-   0        0        0   108609 2023-03-13 10:25:01.000000 mecord-cli-0.1.9/mecord/uauth_ext_pb2.py
+-rw-rw-rw-   0        0        0     1828 2023-03-13 10:54:19.000000 mecord-cli-0.1.9/mecord/upload.py
+-rw-rw-rw-   0        0        0    12849 2023-03-13 10:24:59.000000 mecord-cli-0.1.9/mecord/user_status_ext_pb2.py
+-rw-rw-rw-   0        0        0     4774 2023-03-13 10:42:05.000000 mecord-cli-0.1.9/mecord/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-13 11:30:29.831523 mecord-cli-0.1.9/mecord/widget_template/
+-rw-rw-rw-   0        0        0     1977 2023-03-13 09:18:19.000000 mecord-cli-0.1.9/mecord/widget_template/MekongJS.js.py
+-rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 mecord-cli-0.1.9/mecord/widget_template/__init__.py
+-rw-rw-rw-   0        0        0      147 2023-03-01 01:46:57.000000 mecord-cli-0.1.9/mecord/widget_template/config.json.py
+-rw-rw-rw-   0        0        0     1678 2023-03-13 02:53:47.000000 mecord-cli-0.1.9/mecord/widget_template/icon.png.py
+-rw-rw-rw-   0        0        0      719 2023-03-13 11:19:24.000000 mecord-cli-0.1.9/mecord/widget_template/index.html.py
+-rw-rw-rw-   0        0        0     7004 2023-03-13 11:26:14.000000 mecord-cli-0.1.9/mecord/xy_pb.py
+-rw-rw-rw-   0        0        0     2738 2023-02-20 13:11:01.000000 mecord-cli-0.1.9/mecord/xy_socket.py
+-rw-rw-rw-   0        0        0     2234 2023-03-02 08:06:21.000000 mecord-cli-0.1.9/mecord/xy_user.py
+drwxrwxrwx   0        0        0        0 2023-03-13 11:30:29.834513 mecord-cli-0.1.9/mecord_cli.egg-info/
+-rw-rw-rw-   0        0        0     1757 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      889 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       44 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       73 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-03-13 11:30:29.000000 mecord-cli-0.1.9/mecord_cli.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-03-13 11:30:29.835509 mecord-cli-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0     1446 2023-03-13 11:30:12.000000 mecord-cli-0.1.9/setup.py
```

### Comparing `mecord-cli-0.1.8/LICENSE` & `mecord-cli-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/PKG-INFO` & `mecord-cli-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mecord-cli
-Version: 0.1.8
+Version: 0.1.9
 Summary: mecord tools
 Home-page: https://github.com/mecordofficial
 Author: pengjun
 Author-email: mr_lonely@foxmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `mecord-cli-0.1.8/README.md` & `mecord-cli-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/aigc_ext_pb2.py` & `mecord-cli-0.1.9/mecord/aigc_ext_pb2.py`

 * *Files 10% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 _sym_db = _symbol_database.Default()
 
 
 from mecord import common_ext_pb2 as common__ext__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61igc_ext.proto\x12\x02pb\x1a\x10\x63ommon_ext.proto\"J\n\x08TaskItem\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\x12\x10\n\x08taskUUID\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"^\n\nGetTaskReq\x12\x11\n\tDeviceKey\x18\x01 \x01(\t\x12\x0f\n\x07widgets\x18\x02 \x03(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06\x65xtend\x18\x05 \x01(\t\"F\n\nGetTaskRes\x12\x1a\n\x04list\x18\x01 \x03(\x0b\x32\x0c.pb.TaskItem\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"g\n\rTaskNotifyReq\x12\x10\n\x08taskUUID\x18\x01 \x01(\t\x12\"\n\ntaskStatus\x18\x02 \x01(\x0e\x32\x0e.pb.TaskStatus\x12\x12\n\nfailReason\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x0f\n\rTaskNotifyRes\"o\n\x11\x41igcDeviceBindReq\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\x12\x11\n\tGroupUUID\x18\x02 \x01(\t\x12 \n\tLabelType\x18\x03 \x01(\x0e\x32\r.pb.LabelType\x12\x12\n\nlabelValue\x18\x04 \x01(\t\"\x13\n\x11\x41igcDeviceBindRes\":\n\x13\x41igcDeviceUnBindReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\x03\x12\x11\n\tdeviceKey\x18\x02 \x01(\t\"\x15\n\x13\x41igcDeviceUnBindRes\"&\n\x11\x41igcDeviceInfoReq\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\"`\n\x11\x41igcDeviceInfoRes\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\x12\x11\n\tgroupUUID\x18\x02 \x01(\t\x12\x16\n\x0eisCreateWidget\x18\x03 \x01(\x08\x12\r\n\x05token\x18\x04 \x01(\t\"\x11\n\x0f\x43reateWidgetReq\"%\n\x0f\x43reateWidgetRes\x12\x12\n\nwidgetUUID\x18\x01 \x01(\t\"(\n\x12UploadWidgetUrlReq\x12\x12\n\nwidgetUUID\x18\x01 \x01(\t\"!\n\x12UploadWidgetUrlRes\x12\x0b\n\x03url\x18\x01 \x01(\t\"(\n\x12UploadWidgetEndReq\x12\x12\n\nwidgetUUID\x18\x01 \x01(\t\"%\n\x12UploadWidgetEndRes\x12\x0f\n\x07\x63heckId\x18\x01 \x01(\x03\"\"\n\x0fUploadWidgetReq\x12\x0f\n\x07\x66ileUrl\x18\x01 \x01(\t\"\"\n\x0fUploadWidgetRes\x12\x0f\n\x07\x63heckId\x18\x01 \x01(\x03\"\'\n\x14UploadWidgetCheckReq\x12\x0f\n\x07\x63heckId\x18\x01 \x01(\x03\"R\n\x14UploadWidgetCheckRes\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.pb.UploadWidgetStatus\x12\x12\n\nfailReason\x18\x02 \x01(\t\"\x88\x01\n\x12\x41igcCreateGroupReq\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12 \n\tlabelType\x18\x05 \x01(\x0e\x32\r.pb.LabelType\x12\x0f\n\x07labelId\x18\x06 \x01(\x03\x12\x0e\n\x06status\x18\x07 \x01(\x05\".\n\x12\x41igcCreateGroupRes\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"V\n\x12\x41igcRemoveGroupReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12 \n\tlabelType\x18\x02 \x01(\x0e\x32\r.pb.LabelType\x12\x12\n\nlabelValue\x18\x03 \x01(\t\"\x14\n\x12\x41igcRemoveGroupRes\"W\n\nTaskResult\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\x12*\n\textension\x18\x03 \x01(\x0b\x32\x17.pb.TaskResultExtension\"U\n\x13TaskResultExtension\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\x11\n\tcover_url\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\t\x12\r\n\x05width\x18\x04 \x01(\t\"H\n\x10UploadFileUrlReq\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x13\n\x0b\x63ontentType\x18\x03 \x01(\t\"\x1f\n\x10UploadFileUrlRes\x12\x0b\n\x03url\x18\x01 \x01(\t*X\n\x12UploadWidgetStatus\x12\x0c\n\x08UWS_NONE\x10\x00\x12\x12\n\x0eUWS_PROCESSING\x10\x01\x12\x0f\n\x0bUWS_SUCCESS\x10\x02\x12\x0f\n\x0bUWS_FAILURE\x10\x03\x32\xa2\x05\n\nAigcExtObj\x12)\n\x07GetTask\x12\x0e.pb.GetTaskReq\x1a\x0e.pb.GetTaskRes\x12\x32\n\nTaskNotify\x12\x11.pb.TaskNotifyReq\x1a\x11.pb.TaskNotifyRes\x12:\n\nDeviceBind\x12\x15.pb.AigcDeviceBindReq\x1a\x15.pb.AigcDeviceBindRes\x12:\n\nDeviceInfo\x12\x15.pb.AigcDeviceInfoReq\x1a\x15.pb.AigcDeviceInfoRes\x12\x38\n\x0c\x43reateWidget\x12\x13.pb.CreateWidgetReq\x1a\x13.pb.CreateWidgetRes\x12\x38\n\x0cUploadWidget\x12\x13.pb.UploadWidgetReq\x1a\x13.pb.UploadWidgetRes\x12\x41\n\x0fUploadWidgetUrl\x12\x16.pb.UploadWidgetUrlReq\x1a\x16.pb.UploadWidgetUrlRes\x12\x41\n\x0fUploadWidgetEnd\x12\x16.pb.UploadWidgetEndReq\x1a\x16.pb.UploadWidgetEndRes\x12;\n\rUploadFileUrl\x12\x14.pb.UploadFileUrlReq\x1a\x14.pb.UploadFileUrlRes\x12G\n\x11UploadWidgetCheck\x12\x18.pb.UploadWidgetCheckReq\x1a\x18.pb.UploadWidgetCheckRes\x12=\n\x0bRemoveGroup\x12\x16.pb.AigcRemoveGroupReq\x1a\x16.pb.AigcRemoveGroupResB\x06\xa2\x02\x03PB3b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61igc_ext.proto\x12\x02pb\x1a\x10\x63ommon_ext.proto\"J\n\x08TaskItem\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\x12\x10\n\x08taskUUID\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"^\n\nGetTaskReq\x12\x11\n\tDeviceKey\x18\x01 \x01(\t\x12\x0f\n\x07widgets\x18\x02 \x03(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06\x65xtend\x18\x05 \x01(\t\"F\n\nGetTaskRes\x12\x1a\n\x04list\x18\x01 \x03(\x0b\x32\x0c.pb.TaskItem\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"g\n\rTaskNotifyReq\x12\x10\n\x08taskUUID\x18\x01 \x01(\t\x12\"\n\ntaskStatus\x18\x02 \x01(\x0e\x32\x0e.pb.TaskStatus\x12\x12\n\nfailReason\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x0f\n\rTaskNotifyRes\"o\n\x11\x41igcDeviceBindReq\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\x12\x11\n\tGroupUUID\x18\x02 \x01(\t\x12 \n\tLabelType\x18\x03 \x01(\x0e\x32\r.pb.LabelType\x12\x12\n\nlabelValue\x18\x04 \x01(\t\"\x13\n\x11\x41igcDeviceBindRes\":\n\x13\x41igcDeviceUnBindReq\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\x03\x12\x11\n\tdeviceKey\x18\x02 \x01(\t\"\x15\n\x13\x41igcDeviceUnBindRes\"&\n\x11\x41igcDeviceInfoReq\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\"`\n\x11\x41igcDeviceInfoRes\x12\x11\n\tdeviceKey\x18\x01 \x01(\t\x12\x11\n\tgroupUUID\x18\x02 \x01(\t\x12\x16\n\x0eisCreateWidget\x18\x03 \x01(\x08\x12\r\n\x05token\x18\x04 \x01(\t\"\x11\n\x0f\x43reateWidgetReq\"%\n\x0f\x43reateWidgetRes\x12\x12\n\nwidgetUUID\x18\x01 \x01(\t\"(\n\x12UploadWidgetUrlReq\x12\x12\n\nwidgetUUID\x18\x01 \x01(\t\"6\n\x12UploadWidgetUrlRes\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontentType\x18\x02 \x01(\t\"\"\n\x0fUploadWidgetReq\x12\x0f\n\x07\x66ileUrl\x18\x01 \x01(\t\"\"\n\x0fUploadWidgetRes\x12\x0f\n\x07\x63heckId\x18\x01 \x01(\x03\"\'\n\x14UploadWidgetCheckReq\x12\x0f\n\x07\x63heckId\x18\x01 \x01(\x03\"R\n\x14UploadWidgetCheckRes\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.pb.UploadWidgetStatus\x12\x12\n\nfailReason\x18\x02 \x01(\t\"\x88\x01\n\x12\x41igcCreateGroupReq\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12 \n\tlabelType\x18\x05 \x01(\x0e\x32\r.pb.LabelType\x12\x0f\n\x07labelId\x18\x06 \x01(\x03\x12\x0e\n\x06status\x18\x07 \x01(\x05\".\n\x12\x41igcCreateGroupRes\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"V\n\x12\x41igcRemoveGroupReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12 \n\tlabelType\x18\x02 \x01(\x0e\x32\r.pb.LabelType\x12\x12\n\nlabelValue\x18\x03 \x01(\t\"\x14\n\x12\x41igcRemoveGroupRes\",\n\x0e\x41igcTaskResult\x12\x1a\n\x04list\x18\x01 \x03(\x0b\x32\x0c.pb.AigcData\"S\n\x08\x41igcData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\x12(\n\textension\x18\x03 \x01(\x0b\x32\x15.pb.AigcDataExtension\"S\n\x11\x41igcDataExtension\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\x11\n\tcover_url\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\t\x12\r\n\x05width\x18\x04 \x01(\t\"C\n\x10UploadFileUrlReq\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\r\n\x05token\x18\x02 \x01(\t\x12\x0f\n\x07\x66ileExt\x18\x03 \x01(\t\"4\n\x10UploadFileUrlRes\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontentType\x18\x02 \x01(\t*X\n\x12UploadWidgetStatus\x12\x0c\n\x08UWS_NONE\x10\x00\x12\x12\n\x0eUWS_PROCESSING\x10\x01\x12\x0f\n\x0bUWS_SUCCESS\x10\x02\x12\x0f\n\x0bUWS_FAILURE\x10\x03\x32\xdf\x04\n\nAigcExtObj\x12)\n\x07GetTask\x12\x0e.pb.GetTaskReq\x1a\x0e.pb.GetTaskRes\x12\x32\n\nTaskNotify\x12\x11.pb.TaskNotifyReq\x1a\x11.pb.TaskNotifyRes\x12:\n\nDeviceBind\x12\x15.pb.AigcDeviceBindReq\x1a\x15.pb.AigcDeviceBindRes\x12:\n\nDeviceInfo\x12\x15.pb.AigcDeviceInfoReq\x1a\x15.pb.AigcDeviceInfoRes\x12\x38\n\x0c\x43reateWidget\x12\x13.pb.CreateWidgetReq\x1a\x13.pb.CreateWidgetRes\x12\x38\n\x0cUploadWidget\x12\x13.pb.UploadWidgetReq\x1a\x13.pb.UploadWidgetRes\x12\x41\n\x0fUploadWidgetUrl\x12\x16.pb.UploadWidgetUrlReq\x1a\x16.pb.UploadWidgetUrlRes\x12;\n\rUploadFileUrl\x12\x14.pb.UploadFileUrlReq\x1a\x14.pb.UploadFileUrlRes\x12G\n\x11UploadWidgetCheck\x12\x18.pb.UploadWidgetCheckReq\x1a\x18.pb.UploadWidgetCheckRes\x12=\n\x0bRemoveGroup\x12\x16.pb.AigcRemoveGroupReq\x1a\x16.pb.AigcRemoveGroupResB\x06\xa2\x02\x03PB3b\x06proto3')
 
 _UPLOADWIDGETSTATUS = DESCRIPTOR.enum_types_by_name['UploadWidgetStatus']
 UploadWidgetStatus = enum_type_wrapper.EnumTypeWrapper(_UPLOADWIDGETSTATUS)
 UWS_NONE = 0
 UWS_PROCESSING = 1
 UWS_SUCCESS = 2
 UWS_FAILURE = 3
@@ -37,26 +37,25 @@
 _AIGCDEVICEUNBINDRES = DESCRIPTOR.message_types_by_name['AigcDeviceUnBindRes']
 _AIGCDEVICEINFOREQ = DESCRIPTOR.message_types_by_name['AigcDeviceInfoReq']
 _AIGCDEVICEINFORES = DESCRIPTOR.message_types_by_name['AigcDeviceInfoRes']
 _CREATEWIDGETREQ = DESCRIPTOR.message_types_by_name['CreateWidgetReq']
 _CREATEWIDGETRES = DESCRIPTOR.message_types_by_name['CreateWidgetRes']
 _UPLOADWIDGETURLREQ = DESCRIPTOR.message_types_by_name['UploadWidgetUrlReq']
 _UPLOADWIDGETURLRES = DESCRIPTOR.message_types_by_name['UploadWidgetUrlRes']
-_UPLOADWIDGETENDREQ = DESCRIPTOR.message_types_by_name['UploadWidgetEndReq']
-_UPLOADWIDGETENDRES = DESCRIPTOR.message_types_by_name['UploadWidgetEndRes']
 _UPLOADWIDGETREQ = DESCRIPTOR.message_types_by_name['UploadWidgetReq']
 _UPLOADWIDGETRES = DESCRIPTOR.message_types_by_name['UploadWidgetRes']
 _UPLOADWIDGETCHECKREQ = DESCRIPTOR.message_types_by_name['UploadWidgetCheckReq']
 _UPLOADWIDGETCHECKRES = DESCRIPTOR.message_types_by_name['UploadWidgetCheckRes']
 _AIGCCREATEGROUPREQ = DESCRIPTOR.message_types_by_name['AigcCreateGroupReq']
 _AIGCCREATEGROUPRES = DESCRIPTOR.message_types_by_name['AigcCreateGroupRes']
 _AIGCREMOVEGROUPREQ = DESCRIPTOR.message_types_by_name['AigcRemoveGroupReq']
 _AIGCREMOVEGROUPRES = DESCRIPTOR.message_types_by_name['AigcRemoveGroupRes']
-_TASKRESULT = DESCRIPTOR.message_types_by_name['TaskResult']
-_TASKRESULTEXTENSION = DESCRIPTOR.message_types_by_name['TaskResultExtension']
+_AIGCTASKRESULT = DESCRIPTOR.message_types_by_name['AigcTaskResult']
+_AIGCDATA = DESCRIPTOR.message_types_by_name['AigcData']
+_AIGCDATAEXTENSION = DESCRIPTOR.message_types_by_name['AigcDataExtension']
 _UPLOADFILEURLREQ = DESCRIPTOR.message_types_by_name['UploadFileUrlReq']
 _UPLOADFILEURLRES = DESCRIPTOR.message_types_by_name['UploadFileUrlRes']
 TaskItem = _reflection.GeneratedProtocolMessageType('TaskItem', (_message.Message,), {
   'DESCRIPTOR' : _TASKITEM,
   '__module__' : 'aigc_ext_pb2'
   # @@protoc_insertion_point(class_scope:pb.TaskItem)
   })
@@ -156,28 +155,14 @@
 UploadWidgetUrlRes = _reflection.GeneratedProtocolMessageType('UploadWidgetUrlRes', (_message.Message,), {
   'DESCRIPTOR' : _UPLOADWIDGETURLRES,
   '__module__' : 'aigc_ext_pb2'
   # @@protoc_insertion_point(class_scope:pb.UploadWidgetUrlRes)
   })
 _sym_db.RegisterMessage(UploadWidgetUrlRes)
 
-UploadWidgetEndReq = _reflection.GeneratedProtocolMessageType('UploadWidgetEndReq', (_message.Message,), {
-  'DESCRIPTOR' : _UPLOADWIDGETENDREQ,
-  '__module__' : 'aigc_ext_pb2'
-  # @@protoc_insertion_point(class_scope:pb.UploadWidgetEndReq)
-  })
-_sym_db.RegisterMessage(UploadWidgetEndReq)
-
-UploadWidgetEndRes = _reflection.GeneratedProtocolMessageType('UploadWidgetEndRes', (_message.Message,), {
-  'DESCRIPTOR' : _UPLOADWIDGETENDRES,
-  '__module__' : 'aigc_ext_pb2'
-  # @@protoc_insertion_point(class_scope:pb.UploadWidgetEndRes)
-  })
-_sym_db.RegisterMessage(UploadWidgetEndRes)
-
 UploadWidgetReq = _reflection.GeneratedProtocolMessageType('UploadWidgetReq', (_message.Message,), {
   'DESCRIPTOR' : _UPLOADWIDGETREQ,
   '__module__' : 'aigc_ext_pb2'
   # @@protoc_insertion_point(class_scope:pb.UploadWidgetReq)
   })
 _sym_db.RegisterMessage(UploadWidgetReq)
 
@@ -226,27 +211,34 @@
 AigcRemoveGroupRes = _reflection.GeneratedProtocolMessageType('AigcRemoveGroupRes', (_message.Message,), {
   'DESCRIPTOR' : _AIGCREMOVEGROUPRES,
   '__module__' : 'aigc_ext_pb2'
   # @@protoc_insertion_point(class_scope:pb.AigcRemoveGroupRes)
   })
 _sym_db.RegisterMessage(AigcRemoveGroupRes)
 
-TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), {
-  'DESCRIPTOR' : _TASKRESULT,
+AigcTaskResult = _reflection.GeneratedProtocolMessageType('AigcTaskResult', (_message.Message,), {
+  'DESCRIPTOR' : _AIGCTASKRESULT,
+  '__module__' : 'aigc_ext_pb2'
+  # @@protoc_insertion_point(class_scope:pb.AigcTaskResult)
+  })
+_sym_db.RegisterMessage(AigcTaskResult)
+
+AigcData = _reflection.GeneratedProtocolMessageType('AigcData', (_message.Message,), {
+  'DESCRIPTOR' : _AIGCDATA,
   '__module__' : 'aigc_ext_pb2'
-  # @@protoc_insertion_point(class_scope:pb.TaskResult)
+  # @@protoc_insertion_point(class_scope:pb.AigcData)
   })
-_sym_db.RegisterMessage(TaskResult)
+_sym_db.RegisterMessage(AigcData)
 
-TaskResultExtension = _reflection.GeneratedProtocolMessageType('TaskResultExtension', (_message.Message,), {
-  'DESCRIPTOR' : _TASKRESULTEXTENSION,
+AigcDataExtension = _reflection.GeneratedProtocolMessageType('AigcDataExtension', (_message.Message,), {
+  'DESCRIPTOR' : _AIGCDATAEXTENSION,
   '__module__' : 'aigc_ext_pb2'
-  # @@protoc_insertion_point(class_scope:pb.TaskResultExtension)
+  # @@protoc_insertion_point(class_scope:pb.AigcDataExtension)
   })
-_sym_db.RegisterMessage(TaskResultExtension)
+_sym_db.RegisterMessage(AigcDataExtension)
 
 UploadFileUrlReq = _reflection.GeneratedProtocolMessageType('UploadFileUrlReq', (_message.Message,), {
   'DESCRIPTOR' : _UPLOADFILEURLREQ,
   '__module__' : 'aigc_ext_pb2'
   # @@protoc_insertion_point(class_scope:pb.UploadFileUrlReq)
   })
 _sym_db.RegisterMessage(UploadFileUrlReq)
@@ -259,16 +251,16 @@
 _sym_db.RegisterMessage(UploadFileUrlRes)
 
 _AIGCEXTOBJ = DESCRIPTOR.services_by_name['AigcExtObj']
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'\242\002\003PB3'
-  _UPLOADWIDGETSTATUS._serialized_start=1754
-  _UPLOADWIDGETSTATUS._serialized_end=1842
+  _UPLOADWIDGETSTATUS._serialized_start=1750
+  _UPLOADWIDGETSTATUS._serialized_end=1838
   _TASKITEM._serialized_start=40
   _TASKITEM._serialized_end=114
   _GETTASKREQ._serialized_start=116
   _GETTASKREQ._serialized_end=210
   _GETTASKRES._serialized_start=212
   _GETTASKRES._serialized_end=282
   _TASKNOTIFYREQ._serialized_start=284
@@ -290,39 +282,37 @@
   _CREATEWIDGETREQ._serialized_start=761
   _CREATEWIDGETREQ._serialized_end=778
   _CREATEWIDGETRES._serialized_start=780
   _CREATEWIDGETRES._serialized_end=817
   _UPLOADWIDGETURLREQ._serialized_start=819
   _UPLOADWIDGETURLREQ._serialized_end=859
   _UPLOADWIDGETURLRES._serialized_start=861
-  _UPLOADWIDGETURLRES._serialized_end=894
-  _UPLOADWIDGETENDREQ._serialized_start=896
-  _UPLOADWIDGETENDREQ._serialized_end=936
-  _UPLOADWIDGETENDRES._serialized_start=938
-  _UPLOADWIDGETENDRES._serialized_end=975
-  _UPLOADWIDGETREQ._serialized_start=977
-  _UPLOADWIDGETREQ._serialized_end=1011
-  _UPLOADWIDGETRES._serialized_start=1013
-  _UPLOADWIDGETRES._serialized_end=1047
-  _UPLOADWIDGETCHECKREQ._serialized_start=1049
-  _UPLOADWIDGETCHECKREQ._serialized_end=1088
-  _UPLOADWIDGETCHECKRES._serialized_start=1090
-  _UPLOADWIDGETCHECKRES._serialized_end=1172
-  _AIGCCREATEGROUPREQ._serialized_start=1175
-  _AIGCCREATEGROUPREQ._serialized_end=1311
-  _AIGCCREATEGROUPRES._serialized_start=1313
-  _AIGCCREATEGROUPRES._serialized_end=1359
-  _AIGCREMOVEGROUPREQ._serialized_start=1361
-  _AIGCREMOVEGROUPREQ._serialized_end=1447
-  _AIGCREMOVEGROUPRES._serialized_start=1449
-  _AIGCREMOVEGROUPRES._serialized_end=1469
-  _TASKRESULT._serialized_start=1471
-  _TASKRESULT._serialized_end=1558
-  _TASKRESULTEXTENSION._serialized_start=1560
-  _TASKRESULTEXTENSION._serialized_end=1645
-  _UPLOADFILEURLREQ._serialized_start=1647
-  _UPLOADFILEURLREQ._serialized_end=1719
-  _UPLOADFILEURLRES._serialized_start=1721
-  _UPLOADFILEURLRES._serialized_end=1752
-  _AIGCEXTOBJ._serialized_start=1845
-  _AIGCEXTOBJ._serialized_end=2519
+  _UPLOADWIDGETURLRES._serialized_end=915
+  _UPLOADWIDGETREQ._serialized_start=917
+  _UPLOADWIDGETREQ._serialized_end=951
+  _UPLOADWIDGETRES._serialized_start=953
+  _UPLOADWIDGETRES._serialized_end=987
+  _UPLOADWIDGETCHECKREQ._serialized_start=989
+  _UPLOADWIDGETCHECKREQ._serialized_end=1028
+  _UPLOADWIDGETCHECKRES._serialized_start=1030
+  _UPLOADWIDGETCHECKRES._serialized_end=1112
+  _AIGCCREATEGROUPREQ._serialized_start=1115
+  _AIGCCREATEGROUPREQ._serialized_end=1251
+  _AIGCCREATEGROUPRES._serialized_start=1253
+  _AIGCCREATEGROUPRES._serialized_end=1299
+  _AIGCREMOVEGROUPREQ._serialized_start=1301
+  _AIGCREMOVEGROUPREQ._serialized_end=1387
+  _AIGCREMOVEGROUPRES._serialized_start=1389
+  _AIGCREMOVEGROUPRES._serialized_end=1409
+  _AIGCTASKRESULT._serialized_start=1411
+  _AIGCTASKRESULT._serialized_end=1455
+  _AIGCDATA._serialized_start=1457
+  _AIGCDATA._serialized_end=1540
+  _AIGCDATAEXTENSION._serialized_start=1542
+  _AIGCDATAEXTENSION._serialized_end=1625
+  _UPLOADFILEURLREQ._serialized_start=1627
+  _UPLOADFILEURLREQ._serialized_end=1694
+  _UPLOADFILEURLRES._serialized_start=1696
+  _UPLOADFILEURLRES._serialized_end=1748
+  _AIGCEXTOBJ._serialized_start=1841
+  _AIGCEXTOBJ._serialized_end=2448
 # @@protoc_insertion_point(module_scope)
```

### Comparing `mecord-cli-0.1.8/mecord/common_ext_pb2.py` & `mecord-cli-0.1.9/mecord/common_ext_pb2.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/ftp_upload.py` & `mecord-cli-0.1.9/mecord/ftp_upload.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/main.py` & `mecord-cli-0.1.9/mecord/main.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/mecord_service.py` & `mecord-cli-0.1.9/mecord/mecord_service.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,14 +17,15 @@
     def __init__(self, name, pid_file=None):
         self.name = name
         self.pid_file = pid_file
         self.running = False
         self.halt = False
 
     def start(self):
+        store.writeDeviceInfo(utils.deviceInfo())
         self.halt = False
         if self.pid_file:
             with open(self.pid_file, 'w') as f:
                 f.write(str(os.getpid()))
         self.running = True
         signal.signal(signal.SIGTERM, self.stop)
         self.run()
@@ -72,15 +73,14 @@
         with open(inputArgs, 'w') as f:
             json.dump(param, f)
         outArgs = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{taskUUID}.out")
         if os.path.exists(outArgs):
             os.remove(outArgs)
             
         command = f'{sys.executable} "{cmd}" --run "{inputArgs}" --out "{outArgs}"'
-        print(command)
         result = subprocess.run(command, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
         print(result.stdout.decode(encoding="utf8", errors="ignore"))
         if os.path.exists(outArgs):
             with open(outArgs, 'r') as f:
                 outData = json.load(f)
         else:
```

### Comparing `mecord-cli-0.1.8/mecord/mecord_widget.py` & `mecord-cli-0.1.9/mecord/mecord_widget.py`

 * *Files 0% similar despite different names*

```diff
@@ -160,15 +160,14 @@
             filepath = os.path.join(root, file)
             writepath = os.path.relpath(filepath, package_folder)
             zip.write(filepath, writepath)
     zip.close()
 
     (ossurl, checkid) = upload.uploadWidget(dist, widget_id)
     if checkid > 0:
-        time.sleep(3) #unbelievable reason to sleep
         checkUploadComplate(checkid, dist)
     else:
         os.remove(dist)
 
 def checkUploadComplate(checkid, dist):
     rst = xy_pb.UploadWidgetCheck(checkid)
     if rst == 1: #success
```

### Comparing `mecord-cli-0.1.8/mecord/rpcinput_pb2.py` & `mecord-cli-0.1.9/mecord/rpcinput_pb2.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/script_template/main.py` & `mecord-cli-0.1.9/mecord/script_template/main.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/script_template/run.py` & `mecord-cli-0.1.9/mecord/script_template/run.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/store.py` & `mecord-cli-0.1.9/mecord/store.py`

 * *Files 12% similar despite different names*

```diff
@@ -75,12 +75,26 @@
         read_data["widgets"] = {}
     widgetsMap = read_data["widgets"]
     widgetsMap[widget_id] = path
     for k in list(widgetsMap.keys()):
         if os.path.exists(widgetsMap[k]) == False:
             del widgetsMap[k]
     sp.write(read_data)
+
+def writeDeviceInfo(data):
+    sp = Store()
+    read_data = sp.read()
+    read_data["deviceInfo"] = data
+    sp.write(read_data)
+    
+def readDeviceInfo():
+    sp = Store()
+    read_data = sp.read()
+    if "deviceInfo" in read_data:
+        return read_data["deviceInfo"]
+    else:
+        return {}
     
 def clear():
     sp = Store()
     sp.write("{}")
     read_data = sp.read()
```

### Comparing `mecord-cli-0.1.8/mecord/uauth_common_pb2.py` & `mecord-cli-0.1.9/mecord/uauth_common_pb2.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/uauth_ext_pb2.py` & `mecord-cli-0.1.9/mecord/uauth_ext_pb2.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/upload.py` & `mecord-cli-0.1.9/mecord/upload.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,47 +1,48 @@
 import requests
-import time
+import os
 from urllib.parse import *
 
 from mecord import ftp_upload
 from mecord import xy_pb
 from pathlib import Path
 
-def upload(src, content_type):
+def upload(src):
     file_name = Path(src).name
-    ossurl = xy_pb.GetOssUrl(file_name, content_type)
+    ossurl, content_type = xy_pb.GetOssUrl(os.path.splitext(file_name)[-1][1:])
     if len(ossurl) == 0:
         print("oss server is not avalid")
         return ""
 
     headers = dict()
     headers['Content-Type'] = content_type
     res = requests.put(ossurl, data=open(src, 'rb').read(), headers=headers)
     if res.status_code == 200:
-        time.sleep(2) #unbelievable reason to sleep
-        return urljoin(ossurl, "?s=mecord")
+        realOssUrl = urljoin(ossurl, "?s")
+        return realOssUrl
     else:
         print(f"upload file fail! res = {res}")
         return ""
 
 def uploadWidget(src, widgetid):
-    ossurl = xy_pb.GetWidgetOssUrl(widgetid)
+    ossurl, content_type = xy_pb.GetWidgetOssUrl(widgetid)
     if len(ossurl) == 0:
         print("oss server is not avalid")
         return "", -1
     
     headers = dict()
-    headers['Content-Type'] = 'application/zip'
+    headers['Content-Type'] = content_type
     res = requests.put(ossurl, data=open(src, 'rb').read(), headers=headers)
     if res.status_code == 200:
-        time.sleep(3) #unbelievable reason to sleep
-        checkid = xy_pb.OssUploadEnd(widgetid)
+        realOssUrl = urljoin(ossurl, "?s")
+        checkid = xy_pb.WidgetUploadEnd(realOssUrl)
         if checkid > 0:
-            return ossurl, checkid
+            return realOssUrl, checkid
         else:
             return "", -1
     else:
         print(f"upload file fail! res = {res}")
         return "", -1
 
+# print(urljoin("http://yesdesktop-web-beta.oss-cn-shenzhen.aliyuncs.com/uploads/aigc/widgets/9475cb02-becb-45de-8656-ebe0204201b2/9475cb02-becb-45de-8656-ebe0204201b2.zip?Expires=1678705199&OSSAccessKeyId=LTAI5tGmTwAZJEzGL38wAjXV&Signature=uDvQJUs83WQ1ZU9dbMcHTw6zuDQ=", "?s"))
 # print(upload("E:\\aigc\\mecord_python\\publish_mecord_pip.zip", "application/zip"))
 # print(uploadWidget("E:\\aigc\\mecord_python\\publish_mecord_pip.zip", "fac64812-23c1-4a37-8e99-ddc4fb4d2a01"))
```

### Comparing `mecord-cli-0.1.8/mecord/user_status_ext_pb2.py` & `mecord-cli-0.1.9/mecord/user_status_ext_pb2.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/utils.py` & `mecord-cli-0.1.9/mecord/utils.py`

 * *Files 26% similar despite different names*

```diff
@@ -2,14 +2,16 @@
 import platform
 import subprocess
 import qrcode
 import qrcode_terminal
 import os
 import requests
 from io import BytesIO
+import psutil
+import pynvml
 
 from PIL import Image
 from qrcode.image.styledpil import StyledPilImage
 from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer
 from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask, SolidFillColorMask
 
 def get_mac_address():
@@ -98,8 +100,37 @@
 
 def getOssImageSize(p):
     try:
         res = requests.get(p)
         image = Image.open(BytesIO(res.content), "r")
         return image.size
     except:
-        return 0, 0
+        return 0, 0
+    
+def deviceInfo():
+    pynvml.nvmlInit()
+    gpuCount = pynvml.nvmlDeviceGetCount()
+    M=1024*1024
+    data = {
+        "cpu": {
+            "logical_count" : psutil.cpu_count(),
+            "count" : psutil.cpu_count(logical=False),
+            "max_freq" : f"{psutil.cpu_freq().max / 1000} GHz",
+        },
+        "memory": {
+            "total" : f"{psutil.virtual_memory().total/M} M",
+            "free" : f"{psutil.virtual_memory().free/M} M"
+        },
+        "gpu": {
+            "count" : gpuCount,
+            "list" : [],
+            "mem" : []
+        }
+    }
+    for i in range(gpuCount):
+        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
+        data["gpu"]["list"].append(f"GPU{i}: {pynvml.nvmlDeviceGetName(handle)}")
+        memInfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
+        data["gpu"]["mem"].append(f"GPU{i}: total:{memInfo.total/M} M free:{memInfo.free/M} M")
+        
+    pynvml.nvmlShutdown()
+    return data
```

### Comparing `mecord-cli-0.1.8/mecord/widget_template/MekongJS.js.py` & `mecord-cli-0.1.9/mecord/widget_template/MekongJS.js.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/widget_template/icon.png.py` & `mecord-cli-0.1.9/mecord/widget_template/icon.png.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/widget_template/index.html.py` & `mecord-cli-0.1.9/mecord/widget_template/index.html.py`

 * *Files 21% similar despite different names*

```diff
@@ -17,12 +17,12 @@
             "taskType": "text",  //image, video, audio, text
             "fn_name": "test",
             "param": {
                 "text":"Hello World"
             }
         };
 
-        MekongJS.excuting(params, function(res) { console.log(res); });
+        MekongJS.excuting(JSON.stringify(params), function(res) { console.log(res); });
     }
     </script>
 </body>
 </html>
```

### Comparing `mecord-cli-0.1.8/mecord/xy_pb.py` & `mecord-cli-0.1.9/mecord/xy_pb.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 from mecord import uauth_common_pb2 
 from mecord import uauth_ext_pb2 
 from mecord import common_ext_pb2 
 from mecord import aigc_ext_pb2 
 from mecord import rpcinput_pb2 
 from mecord import store 
 from mecord import utils 
+from mecord import constant 
 
 uuid = utils.generate_unique_id()
 
 def _aigc_post(request, function):
     return _post(url="https://mecord-beta.2tianxin.com/proxymsg", 
                  objStr="mecord.aigc.AigcExtObj", 
                  request=request, 
@@ -93,14 +94,19 @@
     req = aigc_ext_pb2.GetTaskReq()
     req.DeviceKey = uuid
     map = store.widgetMap()
     for it in map:
         req.widgets.append(it)
     req.token = token
     req.limit = 1
+    extInfo = store.readDeviceInfo()
+    extInfo["app_version"] = constant.app_version
+    extInfo["app_bulld_number"] = constant.app_bulld_number
+    extInfo["app_name"] = constant.app_name
+    req.extend = json.dumps(extInfo)
 
     rsp = aigc_ext_pb2.GetTaskRes()
     r1, r2, r3 = _aigc_post(req, "GetTask")
     if r1 != 0:
         print(r2)
         return []
     rsp.ParseFromString(r3)
@@ -138,14 +144,15 @@
 
     rsp = aigc_ext_pb2.AigcDeviceInfoRes()
     r1, r2, r3 = _aigc_post(req, "DeviceInfo")
     if r1 != 0:
         print(r2)
         return False
     rsp.ParseFromString(r3)
+    print(f"====={rsp}")
     if len(rsp.groupUUID) > 0:
         sp = store.Store()
         data = sp.read()
         data["groupUUID"] = rsp.groupUUID
         data["token"] = rsp.token
         if rsp.isCreateWidget == True:
             data["isCreateWidget"] = rsp.isCreateWidget
@@ -159,46 +166,46 @@
     r1, r2, r3 = _aigc_post(req, "CreateWidget")
     if r1 != 0:
         print(r2)
         return ""
     rsp.ParseFromString(r3)
     return rsp.widgetUUID
 
-def GetOssUrl(file_name, content_type):
+def GetOssUrl(ext):
     req = aigc_ext_pb2.UploadFileUrlReq()
     req.token = store.token()
-    req.filename = file_name
-    req.contentType = content_type
+    req.version = constant.app_bulld_number
+    req.fileExt = ext
 
     rsp = aigc_ext_pb2.UploadFileUrlRes()
     r1, r2, r3 = _aigc_post(req, "UploadFileUrl")
     if r1 != 0:
         print(r2)
         return ""
     rsp.ParseFromString(r3)
-    return rsp.url
+    return rsp.url, rsp.contentType
     
 def GetWidgetOssUrl(widgetid):
     req = aigc_ext_pb2.UploadWidgetUrlReq()
     req.widgetUUID = widgetid
 
     rsp = aigc_ext_pb2.UploadWidgetUrlRes()
     r1, r2, r3 = _aigc_post(req, "UploadWidgetUrl")
     if r1 != 0:
         print(r2)
         return ""
     rsp.ParseFromString(r3)
-    return rsp.url
+    return rsp.url, rsp.contentType
 
-def OssUploadEnd(widgetid):
-    req = aigc_ext_pb2.UploadWidgetEndReq()
-    req.widgetUUID = widgetid
+def WidgetUploadEnd(url):
+    req = aigc_ext_pb2.UploadWidgetReq()
+    req.fileUrl = url
     
-    rsp = aigc_ext_pb2.UploadWidgetEndRes()
-    r1, r2, r3 = _aigc_post(req, "UploadWidgetEnd")
+    rsp = aigc_ext_pb2.UploadWidgetRes()
+    r1, r2, r3 = _aigc_post(req, "UploadWidget")
     if r1 != 0:
         print(r2)
         return 0
     rsp.ParseFromString(r3)
     return rsp.checkId
 
 # def PublishWidget(widgetid, oss_path):
```

### Comparing `mecord-cli-0.1.8/mecord/xy_socket.py` & `mecord-cli-0.1.9/mecord/xy_socket.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord/xy_user.py` & `mecord-cli-0.1.9/mecord/xy_user.py`

 * *Files identical despite different names*

### Comparing `mecord-cli-0.1.8/mecord_cli.egg-info/PKG-INFO` & `mecord-cli-0.1.9/mecord_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mecord-cli
-Version: 0.1.8
+Version: 0.1.9
 Summary: mecord tools
 Home-page: https://github.com/mecordofficial
 Author: pengjun
 Author-email: mr_lonely@foxmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `mecord-cli-0.1.8/mecord_cli.egg-info/SOURCES.txt` & `mecord-cli-0.1.9/mecord_cli.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 LICENSE
 README.md
 setup.py
 mecord/__init__.py
 mecord/aigc_ext_pb2.py
 mecord/common_ext_pb2.py
+mecord/constant.py
 mecord/ftp_upload.py
 mecord/main.py
 mecord/mecord_service.py
 mecord/mecord_widget.py
 mecord/rpcinput_pb2.py
 mecord/store.py
 mecord/uauth_common_pb2.py
```

### Comparing `mecord-cli-0.1.8/setup.py` & `mecord-cli-0.1.9/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 setuptools.setup(
     name="mecord-cli",
-    version="0.1.8",
+    version="0.1.9",
     author="pengjun",
     author_email="mr_lonely@foxmail.com",
     description="mecord tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mecordofficial",
     packages=setuptools.find_packages(),
@@ -33,15 +33,16 @@
         'requests',
         'uuid',
         'qrcode',
         'Image',
         'pillow',
         'protobuf',
         'psutil',
-        'qrcode-terminal'
+        'qrcode-terminal',
+        'pynvml'
 
     ],
     dependency_links=[],
     entry_points={
         'console_scripts':[
             'mecord = mecord.main:main'
         ]
```

