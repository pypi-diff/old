# Comparing `tmp/agora_busclient-1.0.8-py2.py3-none-any.whl.zip` & `tmp/agora_busclient-1.0.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,20 +1,20 @@
-Zip file size: 10817 bytes, number of entries: 18
+Zip file size: 10821 bytes, number of entries: 18
 -rw-r--r--  2.0 fat      132 b- defN 23-Feb-23 09:11 agora_busclient/__init__.py
 -rw-r--r--  2.0 fat     3583 b- defN 23-Mar-07 15:23 agora_busclient/bus_client.py
 -rw-r--r--  2.0 fat     3061 b- defN 23-Feb-13 16:33 agora_busclient/message_queue.py
 -rw-r--r--  2.0 fat     4969 b- defN 23-Feb-23 09:06 agora_busclient/mqtt_client.py
--rw-r--r--  2.0 fat       24 b- defN 23-Mar-09 19:16 agora_busclient/version.py
+-rw-r--r--  2.0 fat       24 b- defN 23-Mar-16 20:19 agora_busclient/version.py
 -rw-r--r--  2.0 fat      331 b- defN 23-Feb-23 09:11 agora_busclient/messages/__init__.py
 -rw-r--r--  2.0 fat      225 b- defN 23-Feb-02 12:37 agora_busclient/messages/io_device_data.py
 -rw-r--r--  2.0 fat      694 b- defN 23-Feb-02 13:57 agora_busclient/messages/io_point.py
 -rw-r--r--  2.0 fat      563 b- defN 23-Feb-13 14:02 agora_busclient/messages/io_tag_data_dict.py
 -rw-r--r--  2.0 fat     1934 b- defN 23-Feb-23 09:11 agora_busclient/messages/iodatareport_message.py
 -rw-r--r--  2.0 fat      624 b- defN 23-Feb-02 13:28 agora_busclient/messages/message_header.py
 -rw-r--r--  2.0 fat     3333 b- defN 23-Feb-22 07:44 agora_busclient/messages/msg_decoder.py
 -rw-r--r--  2.0 fat     1996 b- defN 23-Feb-23 08:36 agora_busclient/messages/msg_encoder.py
 -rw-r--r--  2.0 fat      549 b- defN 23-Feb-13 16:30 agora_busclient/messages/request_msg.py
--rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:13 agora_busclient-1.0.8.dist-info/LICENSE
-?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_busclient-1.0.8.dist-info/WHEEL
-?rw-r--r--  2.0 fat      931 b- defN 16-Jan-01 00:00 agora_busclient-1.0.8.dist-info/METADATA
-?rw-r--r--  2.0 fat     1622 b- defN 16-Jan-01 00:00 agora_busclient-1.0.8.dist-info/RECORD
-18 files, 24809 bytes uncompressed, 8101 bytes compressed:  67.3%
+-rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:13 agora_busclient-1.0.9.dist-info/LICENSE
+?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_busclient-1.0.9.dist-info/WHEEL
+?rw-r--r--  2.0 fat      931 b- defN 16-Jan-01 00:00 agora_busclient-1.0.9.dist-info/METADATA
+?rw-r--r--  2.0 fat     1622 b- defN 16-Jan-01 00:00 agora_busclient-1.0.9.dist-info/RECORD
+18 files, 24809 bytes uncompressed, 8105 bytes compressed:  67.3%
```

## zipnote {}

```diff
@@ -36,20 +36,20 @@
 
 Filename: agora_busclient/messages/msg_encoder.py
 Comment: 
 
 Filename: agora_busclient/messages/request_msg.py
 Comment: 
 
-Filename: agora_busclient-1.0.8.dist-info/LICENSE
+Filename: agora_busclient-1.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: agora_busclient-1.0.8.dist-info/WHEEL
+Filename: agora_busclient-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: agora_busclient-1.0.8.dist-info/METADATA
+Filename: agora_busclient-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: agora_busclient-1.0.8.dist-info/RECORD
+Filename: agora_busclient-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## agora_busclient/version.py

```diff
@@ -1 +1 @@
-__version__ = '1.0.8'
+__version__ = '1.0.9'
```

## Comparing `agora_busclient-1.0.8.dist-info/METADATA` & `agora_busclient-1.0.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: agora_busclient
-Version: 1.0.8
+Version: 1.0.9
 Summary: Bus Client libraries for the Agora Edge Apps SDK 2.0 (Python)
 Author-email: AgoraIoT <agoraiot@slb.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Dist: agora_logging
 Requires-Dist: agora_config
 Requires-Dist: agora_utils
```

## Comparing `agora_busclient-1.0.8.dist-info/RECORD` & `agora_busclient-1.0.9.dist-info/RECORD`

 * *Files 20% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 agora_busclient/__init__.py,sha256=lxRLy8JMRb_xrzud88d22xdUzR1WvPpmy7viti3ZHyc,132
 agora_busclient/bus_client.py,sha256=Jz5VaT6YhJI-lrbmmwuK7ICKTghx4Kjk-Ub9WhHLkCQ,3583
 agora_busclient/message_queue.py,sha256=YCy_jH7sh0SAE3nmWtUjYJZC_7fRvrWNnW2XmRmVvfg,3061
 agora_busclient/mqtt_client.py,sha256=wpCP1GSubD4bob79_PxXp0QTdmQuSHDpL6oWY7Xo9-E,4969
-agora_busclient/version.py,sha256=HXG2Fim729WF9R0Op7tVdzk8ojlvSCoafD127Cl88T4,24
+agora_busclient/version.py,sha256=-nHdmfbrEEZoCUg1nFNZBjmdzMhPwWALABnXcptli_o,24
 agora_busclient/messages/__init__.py,sha256=Dbz3Sz4pIy4594WgWVXqwEoehf7eN8uqRGC8JF8y2jE,331
 agora_busclient/messages/io_device_data.py,sha256=Lxukm6MOCT8mIX3TYE5HsDRqHXysfXOFv7LPQhUcd0E,225
 agora_busclient/messages/io_point.py,sha256=FKT7bu5kUonUmI-GB0jG6-0MeWhRf-o5v7vV4fqNVLo,694
 agora_busclient/messages/io_tag_data_dict.py,sha256=Mcb2-cxP_7gjXcIh0aPfdGBuTm_2VFUyc4b7k2BUqw0,563
 agora_busclient/messages/iodatareport_message.py,sha256=0Klx9QwD_ue9_2qpvsem4uyIYz68NsMD6m6R9rIgIMA,1934
 agora_busclient/messages/message_header.py,sha256=dlermnXujKnDnwGPCc38sLluu4iQ12-boO-eNGWoHak,624
 agora_busclient/messages/msg_decoder.py,sha256=SjniqrioCdvDA_PyJvjW277wa6JIFUTK6oNblXw2-fg,3333
 agora_busclient/messages/msg_encoder.py,sha256=ARPsX4PZwXnkE_q1btuM34vOt0TouXTmdOIxfF59GGA,1996
 agora_busclient/messages/request_msg.py,sha256=7KN_6UftGpT6qk0gdSSkkWZZ214ZxMln8ESUv-O46aQ,549
-agora_busclient-1.0.8.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
-agora_busclient-1.0.8.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
-agora_busclient-1.0.8.dist-info/METADATA,sha256=4CB8t_45xHOnO3MQ9X2NN6TuMjlBNwNy225haj9jikk,931
-agora_busclient-1.0.8.dist-info/RECORD,,
+agora_busclient-1.0.9.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
+agora_busclient-1.0.9.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
+agora_busclient-1.0.9.dist-info/METADATA,sha256=vE8DYTsH-0Ow2K3eWwqlxKCcSvqM9rxWpQAFmWtqAm0,931
+agora_busclient-1.0.9.dist-info/RECORD,,
```

