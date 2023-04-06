# Comparing `tmp/agora_config-1.0.8-py2.py3-none-any.whl.zip` & `tmp/agora_config-1.0.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,15 +1,15 @@
-Zip file size: 8641 bytes, number of entries: 13
+Zip file size: 8647 bytes, number of entries: 13
 -rw-r--r--  2.0 fat      105 b- defN 23-Feb-13 17:19 agora_config/__init__.py
--rw-r--r--  2.0 fat     5255 b- defN 23-Feb-13 17:17 agora_config/agora_config.py
+-rw-r--r--  2.0 fat     5279 b- defN 23-Mar-16 09:13 agora_config/agora_config.py
 -rw-r--r--  2.0 fat      549 b- defN 23-Jan-29 10:17 agora_config/command_line_provider.py
 -rw-r--r--  2.0 fat     2771 b- defN 23-Jan-29 13:29 agora_config/dict_of_dict.py
 -rw-r--r--  2.0 fat      407 b- defN 23-Jan-29 10:17 agora_config/environment_variable_provider.py
 -rw-r--r--  2.0 fat     3689 b- defN 23-Jan-29 13:35 agora_config/events.py
 -rw-r--r--  2.0 fat     3438 b- defN 23-Jan-30 13:00 agora_config/file_key_provider.py
 -rw-r--r--  2.0 fat     1927 b- defN 23-Jan-30 13:00 agora_config/file_provider.py
--rw-r--r--  2.0 fat       24 b- defN 23-Mar-09 19:16 agora_config/version.py
--rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_config-1.0.8.dist-info/LICENSE
-?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_config-1.0.8.dist-info/WHEEL
-?rw-r--r--  2.0 fat      756 b- defN 16-Jan-01 00:00 agora_config-1.0.8.dist-info/METADATA
-?rw-r--r--  2.0 fat     1089 b- defN 16-Jan-01 00:00 agora_config-1.0.8.dist-info/RECORD
-13 files, 20248 bytes uncompressed, 6809 bytes compressed:  66.4%
+-rw-r--r--  2.0 fat       24 b- defN 23-Mar-16 20:19 agora_config/version.py
+-rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_config-1.0.9.dist-info/LICENSE
+?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_config-1.0.9.dist-info/WHEEL
+?rw-r--r--  2.0 fat      756 b- defN 16-Jan-01 00:00 agora_config-1.0.9.dist-info/METADATA
+?rw-r--r--  2.0 fat     1089 b- defN 16-Jan-01 00:00 agora_config-1.0.9.dist-info/RECORD
+13 files, 20272 bytes uncompressed, 6815 bytes compressed:  66.4%
```

## zipnote {}

```diff
@@ -21,20 +21,20 @@
 
 Filename: agora_config/file_provider.py
 Comment: 
 
 Filename: agora_config/version.py
 Comment: 
 
-Filename: agora_config-1.0.8.dist-info/LICENSE
+Filename: agora_config-1.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: agora_config-1.0.8.dist-info/WHEEL
+Filename: agora_config-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: agora_config-1.0.8.dist-info/METADATA
+Filename: agora_config-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: agora_config-1.0.8.dist-info/RECORD
+Filename: agora_config-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## agora_config/agora_config.py

```diff
@@ -48,43 +48,43 @@
     
     
     def observe_config(self,fn):
         self.events.add_event('##',fn)
     
               
     def build(self):
-        #print("rebuilding config")
+        print("rebuilding config")
         super().clear()
-        # print (f"build this 0: {super().get_dict()}")
-        # print (f"  add defaults: {config_defaults.get_dict()}")
+        print (f"build this 0: {super().get_dict()}")
+        print (f"  add defaults: {config_defaults.get_dict()}")
         if isinstance(config_defaults, DictOfDict):
             super().merge(config_defaults.get_dict())
-        # print (f"build this 1: {super().get_dict()}")
-        # print (f"  add primary: {self.primary_config.get_dict()}")
+        print (f"build this 1: {super().get_dict()}")
+        print (f"  add primary: {self.primary_config.get_dict()}")
         self.primary_config.check_for_updates()
         super().merge(self.primary_config.get_dict())        
-        # print (f"build this 2: {super().get_dict()}")
-        # print (f"  add environ: {self.evp.get_dict()}")
+        print (f"build this 2: {super().get_dict()}")
+        print (f"  add environ: {self.evp.get_dict()}")
         super().merge(self.evp.get_dict())
-        # print (f"build this 3: {super().get_dict()}")
-        # print (f"  add commandline: {self.clp.get_dict()}")
+        print (f"build this 3: {super().get_dict()}")
+        print (f"  add commandline: {self.clp.get_dict()}")
         super().merge(self.clp.get_dict())
-        # print (f"build this 4: {super().get_dict()}")
-        # print (f"  add alt: {self.alt_config.get_dict()}")
+        print (f"build this 4: {super().get_dict()}")
+        print (f"  add alt: {self.alt_config.get_dict()}")
         self.alt_config.check_for_updates()
         super().merge(self.alt_config.get_dict())
-        # print (f"build this 5: {super().get_dict()}")
-        # print (f"  add fkp: {self.fkp.get_dict()}")
+        print (f"build this 5: {super().get_dict()}")
+        print (f"  add fkp: {self.fkp.get_dict()}")
         self.fkp.check_for_updates()
         super().merge(self.fkp.get_dict())
-        # print (f"build this 6: {super().get_dict()}")
-        # print (f"  add overrides: {config_overrides.get_dict()}")
+        print (f"build this 6: {super().get_dict()}")
+        print (f"  add overrides: {config_overrides.get_dict()}")
         if isinstance(config_overrides, DictOfDict):
             super().merge(config_overrides.get_dict())
-        # print (f"final       : {super().get_dict()}")
+        print (f"final       : {super().get_dict()}")
         self.__dispatch()
 
 
     # below are the methods which watch for updates to the AEA.config.json
 
 
     def __dispatch(self):
@@ -127,14 +127,15 @@
 
 
 config_overrides = DictOfDict()
 config_defaults = DictOfDict()
 
 config = ConfigSingleton()
 config.observe("AEA2:Logging:Verbosity",__set_logging_level)
+__set_logging_level(config["AEA2:Logging:Verbosity"])
 
 
 def log_except_hook(*exc_info):
     """
     Handles unhandled exceptions
     """
     exception=exc_info[1]
```

## agora_config/version.py

```diff
@@ -1 +1 @@
-__version__ = '1.0.8'
+__version__ = '1.0.9'
```

## Comparing `agora_config-1.0.8.dist-info/METADATA` & `agora_config-1.0.9.dist-info/METADATA`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: agora_config
-Version: 1.0.8
+Version: 1.0.9
 Summary: Configuration libraries for the Agora Edge Apps SDK 2.0 (Python)
 Author-email: AgoraIoT <agoraiot@slb.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Dist: agora_logging
 Project-URL: Home, https://agoraiot.github.io
```

## Comparing `agora_config-1.0.8.dist-info/RECORD` & `agora_config-1.0.9.dist-info/RECORD`

 * *Files 16% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 agora_config/__init__.py,sha256=Ql_wTaqiaUcVVQA9spK6UtMpH0BPH6_DvA9Q7pgGvtI,105
-agora_config/agora_config.py,sha256=KN24fg2z-UD3C29vvyWcWWvHGhtPtUo5fDVZzadNfrI,5255
+agora_config/agora_config.py,sha256=UbJerPMX-o-ElAdXRIOwTzHOkkAtYJel_DbTu_zHjMw,5279
 agora_config/command_line_provider.py,sha256=9rxkurSA386teMxlpyYB-lvutUZWcL0HyX5DCMRIHh8,549
 agora_config/dict_of_dict.py,sha256=HHcp-3dbRnACZot2uudbQ81AxRnXdQveCf9PoPy1D3w,2771
 agora_config/environment_variable_provider.py,sha256=LQxGtLX_4bKdQujmy05cKmc1-nTmx8VhQN-rWC3iS1M,407
 agora_config/events.py,sha256=feTeCdrD4eR3lTH_Ft0oPnFRZXUax4ZWkT7HDEdjv6U,3689
 agora_config/file_key_provider.py,sha256=q1zv1wPsWp5lUuH_dBaUo-MYl3R5VDmoMxfe1goTPd0,3438
 agora_config/file_provider.py,sha256=v3fvfMuxJwbutMvS5d3IR_ubz-e5r-IEr35uhkOsCsI,1927
-agora_config/version.py,sha256=HXG2Fim729WF9R0Op7tVdzk8ojlvSCoafD127Cl88T4,24
-agora_config-1.0.8.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
-agora_config-1.0.8.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
-agora_config-1.0.8.dist-info/METADATA,sha256=txuLbb8z2A1BvDWjVGxtaN7qNxhGRPuq9Rf9Q60lQqI,756
-agora_config-1.0.8.dist-info/RECORD,,
+agora_config/version.py,sha256=-nHdmfbrEEZoCUg1nFNZBjmdzMhPwWALABnXcptli_o,24
+agora_config-1.0.9.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
+agora_config-1.0.9.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
+agora_config-1.0.9.dist-info/METADATA,sha256=EFH7qdt8GKjrg3mD-RPcv-W4-JzLU2n1DuPfhJ7wYls,756
+agora_config-1.0.9.dist-info/RECORD,,
```

