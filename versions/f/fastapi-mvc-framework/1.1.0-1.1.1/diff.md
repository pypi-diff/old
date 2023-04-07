# Comparing `tmp/fastapi_mvc_framework-1.1.0.tar.gz` & `tmp/fastapi_mvc_framework-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fastapi_mvc_framework-1.1.0.tar", last modified: Thu Apr  6 07:48:04 2023, max compression
+gzip compressed data, was "fastapi_mvc_framework-1.1.1.tar", last modified: Fri Apr  7 12:05:02 2023, max compression
```

## Comparing `fastapi_mvc_framework-1.1.0.tar` & `fastapi_mvc_framework-1.1.1.tar`

### file list

```diff
@@ -1,23 +1,24 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 07:48:04.247879 fastapi_mvc_framework-1.1.0/
--rw-rw-rw-   0        0        0     3323 2023-04-06 07:48:04.246881 fastapi_mvc_framework-1.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     2183 2023-04-06 07:07:48.000000 fastapi_mvc_framework-1.1.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 07:48:04.241894 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/
--rw-rw-rw-   0        0        0      251 2023-04-06 06:00:47.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/__init__.py
--rw-rw-rw-   0        0        0     8382 2023-04-06 07:41:18.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/auth.py
--rw-rw-rw-   0        0        0     8573 2023-04-06 07:01:12.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/base_controller.py
--rw-rw-rw-   0        0        0     4381 2023-02-25 09:43:32.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/cbv.py
--rw-rw-rw-   0        0        0     2551 2023-03-31 11:57:28.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/config.py
--rw-rw-rw-   0        0        0     3703 2023-04-03 05:51:44.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/controller.py
--rw-rw-rw-   0        0        0    12595 2023-04-06 07:36:54.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/controller_utils.py
--rw-rw-rw-   0        0        0     9045 2023-04-06 07:45:57.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/core.py
--rw-rw-rw-   0        0        0     3936 2023-04-05 10:13:29.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/midware.py
--rw-rw-rw-   0        0        0     2141 2023-04-03 14:30:15.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/midware_casbin.py
--rw-rw-rw-   0        0        0     9056 2023-04-05 10:02:00.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/midware_session.py
--rw-rw-rw-   0        0        0     1597 2023-04-06 04:58:51.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/view.py
-drwxrwxrwx   0        0        0        0 2023-04-06 07:48:04.245886 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/
--rw-rw-rw-   0        0        0     3323 2023-04-06 07:48:04.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      616 2023-04-06 07:48:04.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 07:48:04.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       22 2023-04-06 07:48:04.000000 fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 07:48:04.247879 fastapi_mvc_framework-1.1.0/setup.cfg
--rw-rw-rw-   0        0        0      721 2023-04-06 07:47:32.000000 fastapi_mvc_framework-1.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:05:02.760934 fastapi_mvc_framework-1.1.1/
+-rw-rw-rw-   0        0        0     4479 2023-04-07 12:05:02.760934 fastapi_mvc_framework-1.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3123 2023-04-07 12:04:39.000000 fastapi_mvc_framework-1.1.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 12:05:02.754951 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/
+-rw-rw-rw-   0        0        0      251 2023-04-06 06:00:47.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/__init__.py
+-rw-rw-rw-   0        0        0      931 2023-04-07 07:39:59.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/_utils.py
+-rw-rw-rw-   0        0        0     9701 2023-04-07 12:01:10.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/auth.py
+-rw-rw-rw-   0        0        0     8084 2023-04-07 11:46:59.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/base_controller.py
+-rw-rw-rw-   0        0        0     4381 2023-02-25 09:43:32.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/cbv.py
+-rw-rw-rw-   0        0        0     2996 2023-04-07 10:55:51.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/config.py
+-rw-rw-rw-   0        0        0     3897 2023-04-06 12:09:13.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/controller.py
+-rw-rw-rw-   0        0        0    12827 2023-04-07 11:59:46.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/controller_utils.py
+-rw-rw-rw-   0        0        0    10058 2023-04-07 12:00:08.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/core.py
+-rw-rw-rw-   0        0        0     5507 2023-04-07 11:35:06.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/midware.py
+-rw-rw-rw-   0        0        0     2141 2023-04-03 14:30:15.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/midware_casbin.py
+-rw-rw-rw-   0        0        0     9510 2023-04-07 09:27:38.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/midware_session.py
+-rw-rw-rw-   0        0        0     1597 2023-04-06 04:58:51.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/view.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:05:02.759936 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/
+-rw-rw-rw-   0        0        0     4479 2023-04-07 12:05:02.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      648 2023-04-07 12:05:02.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 12:05:02.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       22 2023-04-07 12:05:02.000000 fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 12:05:02.760934 fastapi_mvc_framework-1.1.1/setup.cfg
+-rw-rw-rw-   0        0        0      721 2023-04-07 12:03:52.000000 fastapi_mvc_framework-1.1.1/setup.py
```

### Comparing `fastapi_mvc_framework-1.1.0/PKG-INFO` & `fastapi_mvc_framework-1.1.1/README.md`

 * *Files 24% similar despite different names*

```diff
@@ -1,208 +1,196 @@
-00000000: 4d65 7461 6461 7461 2d56 6572 7369 6f6e  Metadata-Version
-00000010: 3a20 322e 310d 0a4e 616d 653a 2066 6173  : 2.1..Name: fas
-00000020: 7461 7069 5f6d 7663 5f66 7261 6d65 776f  tapi_mvc_framewo
-00000030: 726b 0d0a 5665 7273 696f 6e3a 2031 2e31  rk..Version: 1.1
-00000040: 2e30 0d0a 5375 6d6d 6172 793a 2053 696d  .0..Summary: Sim
-00000050: 706c 6520 616e 6420 656c 6567 616e 7420  ple and elegant 
-00000060: 7573 6520 6f66 2046 6173 7441 7069 2069  use of FastApi i
-00000070: 6e20 4d56 4320 6d6f 6465 0d0a 486f 6d65  n MVC mode..Home
-00000080: 2d70 6167 653a 2068 7474 7073 3a2f 2f67  -page: https://g
-00000090: 6974 6875 622e 636f 6d2f 736d 6a6b 7a73  ithub.com/smjkzs
-000000a0: 6c2f 6661 7374 6170 695f 6672 616d 6577  l/fastapi_framew
-000000b0: 6f72 6b0d 0a41 7574 686f 723a 2042 7275  ork..Author: Bru
-000000c0: 6365 2063 686f 750d 0a41 7574 686f 722d  ce chou..Author-
-000000d0: 656d 6169 6c3a 2073 6d6a 6b7a 736c 4067  email: smjkzsl@g
-000000e0: 6d61 696c 2e63 6f6d 0d0a 4c69 6365 6e73  mail.com..Licens
-000000f0: 653a 2055 4e4b 4e4f 574e 0d0a 4465 7363  e: UNKNOWN..Desc
-00000100: 7269 7074 696f 6e3a 2023 2066 6173 7461  ription: # fasta
-00000110: 7069 5f66 7261 6d65 776f 726b 0d0a 2020  pi_framework..  
-00000120: 2020 2020 2020 4120 6d76 6320 6672 616d        A mvc fram
-00000130: 6577 6f72 6b20 7573 6564 2046 6173 7441  ework used FastA
-00000140: 7069 0d0a 2020 2020 2020 2020 5369 6d70  pi..        Simp
-00000150: 6c65 2061 6e64 2065 6c65 6761 6e74 2075  le and elegant u
-00000160: 7365 206f 6620 4661 7374 4170 6920 696e  se of FastApi in
-00000170: 204d 5643 206d 6f64 650d 0a20 2020 2020   MVC mode..     
-00000180: 2020 200d 0a20 2020 2020 2020 2075 7361     ..        usa
-00000190: 6765 3a0d 0a20 2020 2020 2020 200d 0a20  ge:..        .. 
-000001a0: 2020 2020 2020 200d 0a20 2020 2020 2020         ..       
-000001b0: 2060 6060 0d0a 2020 2020 2020 2020 0d0a   ```..        ..
-000001c0: 2020 2020 2020 2020 6672 6f6d 2066 6173          from fas
-000001d0: 7461 7069 5f6d 7663 5f66 7261 6d65 776f  tapi_mvc_framewo
-000001e0: 726b 2069 6d70 6f72 7420 6170 695f 726f  rk import api_ro
-000001f0: 7574 6572 2c61 7069 2c52 6571 7565 7374  uter,api,Request
-00000200: 2c52 6573 706f 6e73 652c 4261 7365 436f  ,Response,BaseCo
-00000210: 6e74 726f 6c6c 6572 2c61 7070 6c69 6361  ntroller,applica
-00000220: 7469 6f6e 2c57 6562 536f 636b 6574 2c57  tion,WebSocket,W
-00000230: 6562 536f 636b 6574 4469 7363 6f6e 6e65  ebSocketDisconne
-00000240: 6374 0d0a 2020 2020 2020 2020 696d 706f  ct..        impo
-00000250: 7274 2072 6571 7565 7374 732c 6f70 656e  rt requests,open
-00000260: 6169 2c6a 736f 6e0d 0a20 2020 2020 2020  ai,json..       
-00000270: 2066 726f 6d20 7479 7069 6e67 2069 6d70   from typing imp
-00000280: 6f72 7420 4469 6374 0d0a 2020 2020 2020  ort Dict..      
-00000290: 2020 6672 6f6d 2066 6173 7461 7069 5f6d    from fastapi_m
-000002a0: 7663 5f66 7261 6d65 776f 726b 2069 6d70  vc_framework imp
-000002b0: 6f72 7420 466f 726d 0d0a 2020 2020 2020  ort Form..      
-000002c0: 2020 200d 0a20 2020 2020 2020 2040 6170     ..        @ap
-000002d0: 695f 726f 7574 6572 2861 7574 683d 2770  i_router(auth='p
-000002e0: 7562 6c69 6327 290d 0a20 2020 2020 2020  ublic')..       
-000002f0: 2063 6c61 7373 2054 6573 7443 6f6e 7472   class TestContr
-00000300: 6f6c 6c65 7228 4261 7365 436f 6e74 726f  oller(BaseContro
-00000310: 6c6c 6572 293a 0d0a 2020 2020 2020 2020  ller):..        
-00000320: 2020 2020 5f61 7574 685f 7572 6c20 3d20      _auth_url = 
-00000330: 272f 7573 6572 2f6c 6f67 696e 270d 0a20  '/user/login'.. 
-00000340: 2020 2020 2020 2020 0d0a 2020 2020 2020          ..      
-00000350: 2020 2020 2020 4061 7069 2e67 6574 2822        @api.get("
-00000360: 2f75 7365 722f 6c6f 6769 6e22 290d 0a20  /user/login").. 
-00000370: 2020 2020 2020 2020 2020 2064 6566 206c             def l
-00000380: 6f67 696e 2873 656c 6629 3a0d 0a20 2020  ogin(self):..   
-00000390: 2020 2020 2020 2020 2020 2020 2022 2222               """
-000003a0: 3a74 6974 6c65 204c 6f67 696e 2222 220d  :title Login""".
-000003b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000003c0: 2073 656c 662e 7265 7175 6573 742e 7374   self.request.st
-000003d0: 6174 652e 6b65 6570 5f66 6c61 7368 203d  ate.keep_flash =
-000003e0: 2054 7275 650d 0a20 2020 2020 2020 2020   True..         
-000003f0: 2020 2020 2020 2072 6574 7572 6e20 7365         return se
-00000400: 6c66 2e76 6965 7728 2920 0d0a 2020 2020  lf.view() ..    
-00000410: 2020 2020 2020 2020 0d0a 2020 2020 2020          ..      
-00000420: 2020 2020 2020 4061 7069 2e70 6f73 7428        @api.post(
-00000430: 222f 7465 7374 2f76 6572 6974 795f 7573  "/test/verity_us
-00000440: 6572 2229 0d0a 2020 2020 2020 2020 2020  er")..          
-00000450: 2020 6465 6620 7665 7269 7479 5f75 7365    def verity_use
-00000460: 7228 7365 6c66 2c75 7365 726e 616d 653a  r(self,username:
-00000470: 2073 7472 203d 2046 6f72 6d28 292c 2070   str = Form(), p
-00000480: 6173 7377 6f72 643a 2073 7472 203d 2046  assword: str = F
-00000490: 6f72 6d28 2929 3a20 0d0a 2020 2020 2020  orm()): ..      
-000004a0: 2020 2020 2020 2020 2020 6966 2075 7365            if use
-000004b0: 726e 616d 6520 616e 6420 7061 7373 776f  rname and passwo
-000004c0: 7264 3a0d 0a20 2020 2020 2020 2020 2020  rd:..           
-000004d0: 2020 2020 2020 2020 2023 646f 2076 6572           #do ver
-000004e0: 6974 6965 640d 0a20 2020 2020 2020 2020  itied..         
-000004f0: 2020 2020 2020 2020 2020 2069 6620 7573             if us
-00000500: 6572 6e61 6d65 2069 6e20 5b27 6272 7563  ername in ['bruc
-00000510: 6527 2c27 616c 6963 6527 5d20 616e 6420  e','alice'] and 
-00000520: 7061 7373 776f 7264 3a0d 0a20 2020 2020  password:..     
-00000530: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000540: 2020 2072 6574 7572 6e20 7365 6c66 2e5f     return self._
-00000550: 7665 7269 7479 5f73 7563 6365 7373 6564  verity_successed
-00000560: 2875 7365 726e 616d 6529 0d0a 2020 2020  (username)..    
-00000570: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000580: 656c 7365 3a0d 0a20 2020 2020 2020 2020  else:..         
-00000590: 2020 2020 2020 2020 2020 2020 2020 2072                 r
-000005a0: 6574 7572 6e20 7365 6c66 2e5f 7665 7269  eturn self._veri
-000005b0: 7479 5f65 7272 6f72 2829 0d0a 2020 2020  ty_error()..    
-000005c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000005d0: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
-000005e0: 2020 7265 7475 726e 2073 656c 662e 5f76    return self._v
-000005f0: 6572 6974 795f 6572 726f 7228 290d 0a20  erity_error().. 
-00000600: 2020 2020 2020 2020 2020 200d 0a20 2020             ..   
-00000610: 2020 2020 2020 2020 2040 6170 692e 6765           @api.ge
-00000620: 7428 222f 2220 290d 0a20 2020 2020 2020  t("/" )..       
-00000630: 2020 2020 2064 6566 2068 6f6d 6528 7365       def home(se
-00000640: 6c66 2c72 6571 7565 7374 3a52 6571 7565  lf,request:Reque
-00000650: 7374 293a 200d 0a20 2020 2020 2020 2020  st): ..         
-00000660: 2020 2020 2020 2027 2727 0d0a 2020 2020         '''..    
-00000670: 2020 2020 2020 2020 2020 2020 3a74 6974              :tit
-00000680: 6c65 2048 6f6d 650d 0a20 2020 2020 2020  le Home..       
-00000690: 2020 2020 2020 2020 2027 2727 0d0a 2020           '''..  
-000006a0: 2020 2020 2020 2020 2020 2020 2020 6320                c 
-000006b0: 3d20 7365 6c66 2e73 6573 7369 6f6e 2e67  = self.session.g
-000006c0: 6574 2827 686f 6d65 272c 3129 0d0a 2020  et('home',1)..  
-000006d0: 2020 2020 2020 2020 2020 2020 2020 6320                c 
-000006e0: 3d20 632b 3120 0d0a 2020 2020 2020 2020  = c+1 ..        
-000006f0: 2020 2020 2020 2020 2320 2373 6574 7469          # #setti
-00000700: 6e67 2063 6f6f 6b69 6573 2020 200d 0a20  ng cookies   .. 
-00000710: 2020 2020 2020 2020 2020 2020 2020 2023                 #
-00000720: 2073 656c 662e 7265 7370 6f6e 7365 2e73   self.response.s
-00000730: 6574 5f63 6f6f 6b69 6528 2761 272c 6329  et_cookie('a',c)
-00000740: 200d 0a20 2020 2020 2020 2020 2020 2020   ..             
-00000750: 2020 2073 656c 662e 636f 6f6b 6965 735b     self.cookies[
-00000760: 2261 225d 203d 2063 0d0a 2020 2020 2020  "a"] = c..      
-00000770: 2020 2020 2020 2020 2020 6966 2063 3e31            if c>1
-00000780: 303a 0d0a 2020 2020 2020 2020 2020 2020  0:..            
-00000790: 2020 2020 2020 2020 6465 6c20 7365 6c66          del self
-000007a0: 2e63 6f6f 6b69 6573 5b22 6122 5d0d 0a20  .cookies["a"].. 
-000007b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000007c0: 2020 2063 203d 2030 0d0a 2020 2020 2020     c = 0..      
-000007d0: 2020 2020 2020 2020 2020 7365 6c66 2e73            self.s
-000007e0: 6573 7369 6f6e 5b27 686f 6d65 275d 203d  ession['home'] =
-000007f0: 2063 0d0a 2020 2020 2020 2020 2020 2020   c..            
-00000800: 2020 2020 7465 7874 203d 2022 4865 6c6c      text = "Hell
-00000810: 6f20 576f 726c 6421 2049 276d 2069 6e20  o World! I'm in 
-00000820: 4661 7374 6170 694d 7663 4672 616d 6577  FastapiMvcFramew
-00000830: 6f72 6b22 0d0a 2020 2020 2020 2020 2020  ork"..          
-00000840: 2020 2020 2020 726f 7574 6572 735f 6d61        routers_ma
-00000850: 7020 3d20 6170 706c 6963 6174 696f 6e2e  p = application.
-00000860: 726f 7574 6572 735f 6d61 700d 0a20 2020  routers_map..   
-00000870: 2020 2020 2020 2020 2020 2020 2072 6f75               rou
-00000880: 7465 7273 203d 2061 7070 6c69 6361 7469  ters = applicati
-00000890: 6f6e 2e72 6f75 7465 730d 0a20 2020 2020  on.routes..     
-000008a0: 2020 2020 2020 2020 2020 2072 6574 7572             retur
-000008b0: 6e20 7365 6c66 2e76 6965 7728 290d 0a20  n self.view().. 
-000008c0: 2020 2020 2020 2020 2020 2040 6170 692e             @api.
-000008d0: 6765 7428 222f 786d 6c22 2c61 7574 683d  get("/xml",auth=
-000008e0: 2775 7365 7227 290d 0a20 2020 2020 2020  'user')..       
-000008f0: 2020 2020 2064 6566 2067 6574 5f6c 6567       def get_leg
-00000900: 6163 795f 6461 7461 2873 656c 6629 3a0d  acy_data(self):.
-00000910: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000920: 2022 2222 3a74 6974 6c65 2058 4d4c 2850   """:title XML(P
-00000930: 726f 7465 6374 6564 2922 2222 0d0a 2020  rotected)"""..  
-00000940: 2020 2020 2020 0d0a 2020 2020 2020 2020        ..        
-00000950: 2020 2020 2020 2020 6461 7461 203d 2022          data = "
-00000960: 2222 3c3f 786d 6c20 7665 7273 696f 6e3d  ""<?xml version=
-00000970: 2231 2e30 223f 3e0d 0a20 2020 2020 2020  "1.0"?>..       
-00000980: 2020 2020 2020 2020 203c 7368 616d 706f           <shampo
-00000990: 6f3e 0d0a 2020 2020 2020 2020 2020 2020  o>..            
-000009a0: 2020 2020 3c48 6561 6465 723e 0d0a 2020      <Header>..  
-000009b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000009c0: 2020 4170 706c 7920 7368 616d 706f 6f20    Apply shampoo 
-000009d0: 6865 7265 2e0d 0a20 2020 2020 2020 2020  here...         
-000009e0: 2020 2020 2020 203c 2f48 6561 6465 723e         </Header>
-000009f0: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
-00000a00: 2020 3c42 6f64 793e 0d0a 2020 2020 2020    <Body>..      
-00000a10: 2020 2020 2020 2020 2020 2020 2020 596f                Yo
-00000a20: 7527 6c6c 2068 6176 6520 746f 2075 7365  u'll have to use
-00000a30: 2073 6f61 7020 6865 7265 2e0d 0a20 2020   soap here...   
-00000a40: 2020 2020 2020 2020 2020 2020 203c 2f42               </B
-00000a50: 6f64 793e 0d0a 2020 2020 2020 2020 2020  ody>..          
-00000a60: 2020 2020 2020 3c2f 7368 616d 706f 6f3e        </shampoo>
-00000a70: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
-00000a80: 2020 2222 220d 0a20 2020 2020 2020 2020    """..         
-00000a90: 2020 2020 2020 2072 6574 7572 6e20 7365         return se
-00000aa0: 6c66 2e76 6965 7728 636f 6e74 656e 743d  lf.view(content=
-00000ab0: 6461 7461 2c6d 6564 6961 5f74 7970 653d  data,media_type=
-00000ac0: 2261 7070 6c69 6361 7469 6f6e 2f78 6d6c  "application/xml
-00000ad0: 2229 0d0a 2020 2020 2020 2020 2020 2020  ")..            
-00000ae0: 2020 2020 7265 7475 726e 2052 6573 706f      return Respo
-00000af0: 6e73 6528 636f 6e74 656e 743d 6461 7461  nse(content=data
-00000b00: 2c20 6d65 6469 615f 7479 7065 3d22 6170  , media_type="ap
-00000b10: 706c 6963 6174 696f 6e2f 786d 6c22 290d  plication/xml").
-00000b20: 0a20 2020 2020 2020 200d 0a20 2020 2020  .        ..     
-00000b30: 2020 2020 2020 2020 0d0a 2020 2020 2020          ..      
-00000b40: 2020 2020 2020 4061 7069 2e67 6574 2822        @api.get("
-00000b50: 2f63 6861 7467 7074 2229 0d0a 2020 2020  /chatgpt")..    
-00000b60: 2020 2020 2020 2020 6465 6620 6368 6174          def chat
-00000b70: 6770 7428 7365 6c66 293a 0d0a 2020 2020  gpt(self):..    
-00000b80: 2020 2020 2020 2020 2020 2020 2222 220d              """.
-00000b90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000ba0: 203a 7469 746c 6520 4368 6174 0d0a 2020   :title Chat..  
-00000bb0: 2020 2020 2020 2020 2020 2020 2020 2222                ""
-00000bc0: 220d 0a20 2020 2020 2020 2020 2020 2020  "..             
-00000bd0: 2020 2072 6574 7572 6e20 7365 6c66 2e76     return self.v
-00000be0: 6965 7728 290d 0a20 2020 2020 2020 200d  iew()..        .
-00000bf0: 0a20 2020 2020 2020 200d 0a20 2020 2020  .        ..     
-00000c00: 2020 2060 6060 0d0a 2020 2020 2020 2020     ```..        
-00000c10: 0d0a 506c 6174 666f 726d 3a20 554e 4b4e  ..Platform: UNKN
-00000c20: 4f57 4e0d 0a43 6c61 7373 6966 6965 723a  OWN..Classifier:
-00000c30: 2050 726f 6772 616d 6d69 6e67 204c 616e   Programming Lan
-00000c40: 6775 6167 6520 3a3a 2050 7974 686f 6e20  guage :: Python 
-00000c50: 3a3a 2033 0d0a 436c 6173 7369 6669 6572  :: 3..Classifier
-00000c60: 3a20 4c69 6365 6e73 6520 3a3a 204f 5349  : License :: OSI
-00000c70: 2041 7070 726f 7665 6420 3a3a 204d 4954   Approved :: MIT
-00000c80: 204c 6963 656e 7365 0d0a 436c 6173 7369   License..Classi
-00000c90: 6669 6572 3a20 4f70 6572 6174 696e 6720  fier: Operating 
-00000ca0: 5379 7374 656d 203a 3a20 4f53 2049 6e64  System :: OS Ind
-00000cb0: 6570 656e 6465 6e74 0d0a 5265 7175 6972  ependent..Requir
-00000cc0: 6573 2d50 7974 686f 6e3a 203e 3d33 2e36  es-Python: >=3.6
-00000cd0: 0d0a 4465 7363 7269 7074 696f 6e2d 436f  ..Description-Co
-00000ce0: 6e74 656e 742d 5479 7065 3a20 7465 7874  ntent-Type: text
-00000cf0: 2f6d 6172 6b64 6f77 6e0d 0a              /markdown..
+00000000: 2320 6661 7374 6170 695f 6672 616d 6577  # fastapi_framew
+00000010: 6f72 6b0d 0a41 206d 7663 2066 7261 6d65  ork..A mvc frame
+00000020: 776f 726b 2075 7365 6420 4661 7374 4170  work used FastAp
+00000030: 690d 0a53 696d 706c 6520 616e 6420 656c  i..Simple and el
+00000040: 6567 616e 7420 7573 6520 6f66 2046 6173  egant use of Fas
+00000050: 7441 7069 2069 6e20 4d56 4320 6d6f 6465  tApi in MVC mode
+00000060: 0d0a 0d0a 7573 6167 653a 0d0a 0d0a 0d0a  ....usage:......
+00000070: 6060 600d 0a0d 0a66 726f 6d20 6661 7374  ```....from fast
+00000080: 6170 695f 6d76 635f 6672 616d 6577 6f72  api_mvc_framewor
+00000090: 6b20 696d 706f 7274 2061 7069 5f72 6f75  k import api_rou
+000000a0: 7465 722c 6170 692c 5265 7175 6573 742c  ter,api,Request,
+000000b0: 5265 7370 6f6e 7365 2c42 6173 6543 6f6e  Response,BaseCon
+000000c0: 7472 6f6c 6c65 722c 6170 706c 6963 6174  troller,applicat
+000000d0: 696f 6e2c 5765 6253 6f63 6b65 742c 5765  ion,WebSocket,We
+000000e0: 6253 6f63 6b65 7444 6973 636f 6e6e 6563  bSocketDisconnec
+000000f0: 740d 0a69 6d70 6f72 7420 7265 7175 6573  t..import reques
+00000100: 7473 2c6f 7065 6e61 692c 6a73 6f6e 0d0a  ts,openai,json..
+00000110: 6672 6f6d 2074 7970 696e 6720 696d 706f  from typing impo
+00000120: 7274 2044 6963 740d 0a66 726f 6d20 6661  rt Dict..from fa
+00000130: 7374 6170 695f 6d76 635f 6672 616d 6577  stapi_mvc_framew
+00000140: 6f72 6b20 696d 706f 7274 2046 6f72 6d0d  ork import Form.
+00000150: 0a20 0d0a 4061 7069 5f72 6f75 7465 7228  . ..@api_router(
+00000160: 6175 7468 3d27 7075 626c 6963 2729 0d0a  auth='public')..
+00000170: 636c 6173 7320 5465 7374 436f 6e74 726f  class TestContro
+00000180: 6c6c 6572 2842 6173 6543 6f6e 7472 6f6c  ller(BaseControl
+00000190: 6c65 7229 3a0d 0a20 2020 205f 6175 7468  ler):..    _auth
+000001a0: 5f75 726c 203d 2027 2f75 7365 722f 6c6f  _url = '/user/lo
+000001b0: 6769 6e27 0d0a 200d 0a20 2020 2040 6170  gin'.. ..    @ap
+000001c0: 692e 6765 7428 222f 7573 6572 2f6c 6f67  i.get("/user/log
+000001d0: 696e 2229 0d0a 2020 2020 6465 6620 6c6f  in")..    def lo
+000001e0: 6769 6e28 7365 6c66 293a 0d0a 2020 2020  gin(self):..    
+000001f0: 2020 2020 2222 223a 7469 746c 6520 4c6f      """:title Lo
+00000200: 6769 6e22 2222 0d0a 2020 2020 2020 2020  gin"""..        
+00000210: 7365 6c66 2e72 6571 7565 7374 2e73 7461  self.request.sta
+00000220: 7465 2e6b 6565 705f 666c 6173 6820 3d20  te.keep_flash = 
+00000230: 5472 7565 0d0a 2020 2020 2020 2020 7265  True..        re
+00000240: 7475 726e 2073 656c 662e 7669 6577 2829  turn self.view()
+00000250: 200d 0a20 2020 200d 0a20 2020 2040 6170   ..    ..    @ap
+00000260: 692e 706f 7374 2822 2f74 6573 742f 7665  i.post("/test/ve
+00000270: 7269 7479 5f75 7365 7222 290d 0a20 2020  rity_user")..   
+00000280: 2064 6566 2076 6572 6974 795f 7573 6572   def verity_user
+00000290: 2873 656c 662c 7573 6572 6e61 6d65 3a20  (self,username: 
+000002a0: 7374 7220 3d20 466f 726d 2829 2c20 7061  str = Form(), pa
+000002b0: 7373 776f 7264 3a20 7374 7220 3d20 466f  ssword: str = Fo
+000002c0: 726d 2829 293a 200d 0a20 2020 2020 2020  rm()): ..       
+000002d0: 2069 6620 7573 6572 6e61 6d65 2061 6e64   if username and
+000002e0: 2070 6173 7377 6f72 643a 0d0a 2020 2020   password:..    
+000002f0: 2020 2020 2020 2020 2364 6f20 7665 7269          #do veri
+00000300: 7469 6564 0d0a 2020 2020 2020 2020 2020  tied..          
+00000310: 2020 6966 2075 7365 726e 616d 6520 696e    if username in
+00000320: 205b 2762 7275 6365 272c 2761 6c69 6365   ['bruce','alice
+00000330: 275d 2061 6e64 2070 6173 7377 6f72 643a  '] and password:
+00000340: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
+00000350: 2020 7265 7475 726e 2073 656c 662e 5f76    return self._v
+00000360: 6572 6974 795f 7375 6363 6573 7365 6428  erity_successed(
+00000370: 7573 6572 6e61 6d65 290d 0a20 2020 2020  username)..     
+00000380: 2020 2020 2020 2065 6c73 653a 0d0a 2020         else:..  
+00000390: 2020 2020 2020 2020 2020 2020 2020 7265                re
+000003a0: 7475 726e 2073 656c 662e 5f76 6572 6974  turn self._verit
+000003b0: 795f 6572 726f 7228 290d 0a20 2020 2020  y_error()..     
+000003c0: 2020 2020 2020 200d 0a20 2020 2020 2020         ..       
+000003d0: 2072 6574 7572 6e20 7365 6c66 2e5f 7665   return self._ve
+000003e0: 7269 7479 5f65 7272 6f72 2829 0d0a 2020  rity_error()..  
+000003f0: 2020 0d0a 2020 2020 4061 7069 2e67 6574    ..    @api.get
+00000400: 2822 2f22 2029 0d0a 2020 2020 6465 6620  ("/" )..    def 
+00000410: 686f 6d65 2873 656c 662c 7265 7175 6573  home(self,reques
+00000420: 743a 5265 7175 6573 7429 3a20 0d0a 2020  t:Request): ..  
+00000430: 2020 2020 2020 2727 270d 0a20 2020 2020        '''..     
+00000440: 2020 203a 7469 746c 6520 486f 6d65 0d0a     :title Home..
+00000450: 2020 2020 2020 2020 2727 270d 0a20 2020          '''..   
+00000460: 2020 2020 2063 203d 2073 656c 662e 7365       c = self.se
+00000470: 7373 696f 6e2e 6765 7428 2768 6f6d 6527  ssion.get('home'
+00000480: 2c31 290d 0a20 2020 2020 2020 2063 203d  ,1)..        c =
+00000490: 2063 2b31 200d 0a20 2020 2020 2020 2023   c+1 ..        #
+000004a0: 2023 7365 7474 696e 6720 636f 6f6b 6965   #setting cookie
+000004b0: 7320 2020 0d0a 2020 2020 2020 2020 2320  s   ..        # 
+000004c0: 7365 6c66 2e72 6573 706f 6e73 652e 7365  self.response.se
+000004d0: 745f 636f 6f6b 6965 2827 6127 2c63 2920  t_cookie('a',c) 
+000004e0: 0d0a 2020 2020 2020 2020 7365 6c66 2e63  ..        self.c
+000004f0: 6f6f 6b69 6573 5b22 6122 5d20 3d20 630d  ookies["a"] = c.
+00000500: 0a20 2020 2020 2020 2069 6620 633e 3130  .        if c>10
+00000510: 3a0d 0a20 2020 2020 2020 2020 2020 2064  :..            d
+00000520: 656c 2073 656c 662e 636f 6f6b 6965 735b  el self.cookies[
+00000530: 2261 225d 0d0a 2020 2020 2020 2020 2020  "a"]..          
+00000540: 2020 6320 3d20 300d 0a20 2020 2020 2020    c = 0..       
+00000550: 2073 656c 662e 7365 7373 696f 6e5b 2768   self.session['h
+00000560: 6f6d 6527 5d20 3d20 630d 0a20 2020 2020  ome'] = c..     
+00000570: 2020 2074 6578 7420 3d20 2248 656c 6c6f     text = "Hello
+00000580: 2057 6f72 6c64 2120 4927 6d20 696e 2046   World! I'm in F
+00000590: 6173 7461 7069 4d76 6346 7261 6d65 776f  astapiMvcFramewo
+000005a0: 726b 220d 0a20 2020 2020 2020 2072 6f75  rk"..        rou
+000005b0: 7465 7273 5f6d 6170 203d 2061 7070 6c69  ters_map = appli
+000005c0: 6361 7469 6f6e 2e72 6f75 7465 7273 5f6d  cation.routers_m
+000005d0: 6170 0d0a 2020 2020 2020 2020 726f 7574  ap..        rout
+000005e0: 6572 7320 3d20 6170 706c 6963 6174 696f  ers = applicatio
+000005f0: 6e2e 726f 7574 6573 0d0a 2020 2020 2020  n.routes..      
+00000600: 2020 7265 7475 726e 2073 656c 662e 7669    return self.vi
+00000610: 6577 2829 0d0a 2020 2020 4061 7069 2e67  ew()..    @api.g
+00000620: 6574 2822 2f78 6d6c 222c 6175 7468 3d27  et("/xml",auth='
+00000630: 7573 6572 2729 0d0a 2020 2020 6465 6620  user')..    def 
+00000640: 6765 745f 6c65 6761 6379 5f64 6174 6128  get_legacy_data(
+00000650: 7365 6c66 293a 0d0a 2020 2020 2020 2020  self):..        
+00000660: 2222 223a 7469 746c 6520 584d 4c28 5072  """:title XML(Pr
+00000670: 6f74 6563 7465 6429 2222 220d 0a0d 0a20  otected)""".... 
+00000680: 2020 2020 2020 2064 6174 6120 3d20 2222         data = ""
+00000690: 223c 3f78 6d6c 2076 6572 7369 6f6e 3d22  "<?xml version="
+000006a0: 312e 3022 3f3e 0d0a 2020 2020 2020 2020  1.0"?>..        
+000006b0: 3c73 6861 6d70 6f6f 3e0d 0a20 2020 2020  <shampoo>..     
+000006c0: 2020 203c 4865 6164 6572 3e0d 0a20 2020     <Header>..   
+000006d0: 2020 2020 2020 2020 2041 7070 6c79 2073           Apply s
+000006e0: 6861 6d70 6f6f 2068 6572 652e 0d0a 2020  hampoo here...  
+000006f0: 2020 2020 2020 3c2f 4865 6164 6572 3e0d        </Header>.
+00000700: 0a20 2020 2020 2020 203c 426f 6479 3e0d  .        <Body>.
+00000710: 0a20 2020 2020 2020 2020 2020 2059 6f75  .            You
+00000720: 276c 6c20 6861 7665 2074 6f20 7573 6520  'll have to use 
+00000730: 736f 6170 2068 6572 652e 0d0a 2020 2020  soap here...    
+00000740: 2020 2020 3c2f 426f 6479 3e0d 0a20 2020      </Body>..   
+00000750: 2020 2020 203c 2f73 6861 6d70 6f6f 3e0d       </shampoo>.
+00000760: 0a20 2020 2020 2020 2022 2222 0d0a 2020  .        """..  
+00000770: 2020 2020 2020 7265 7475 726e 2073 656c        return sel
+00000780: 662e 7669 6577 2863 6f6e 7465 6e74 3d64  f.view(content=d
+00000790: 6174 612c 6d65 6469 615f 7479 7065 3d22  ata,media_type="
+000007a0: 6170 706c 6963 6174 696f 6e2f 786d 6c22  application/xml"
+000007b0: 290d 0a20 2020 2020 2020 2072 6574 7572  )..        retur
+000007c0: 6e20 5265 7370 6f6e 7365 2863 6f6e 7465  n Response(conte
+000007d0: 6e74 3d64 6174 612c 206d 6564 6961 5f74  nt=data, media_t
+000007e0: 7970 653d 2261 7070 6c69 6361 7469 6f6e  ype="application
+000007f0: 2f78 6d6c 2229 0d0a 0d0a 2020 2020 200d  /xml")....     .
+00000800: 0a20 2020 2040 6170 692e 6765 7428 222f  .    @api.get("/
+00000810: 6368 6174 6770 7422 290d 0a20 2020 2064  chatgpt")..    d
+00000820: 6566 2063 6861 7467 7074 2873 656c 6629  ef chatgpt(self)
+00000830: 3a0d 0a20 2020 2020 2020 2022 2222 0d0a  :..        """..
+00000840: 2020 2020 2020 2020 3a74 6974 6c65 2043          :title C
+00000850: 6861 740d 0a20 2020 2020 2020 2022 2222  hat..        """
+00000860: 0d0a 2020 2020 2020 2020 7265 7475 726e  ..        return
+00000870: 2073 656c 662e 7669 6577 2829 0d0a 0d0a   self.view()....
+00000880: 0d0a 6060 600d 0a0d 0a68 6f6d 652e 6874  ..```....home.ht
+00000890: 6d6c 3a0d 0a0d 0a60 6060 0d0a 3c62 6f64  ml:....```..<bod
+000008a0: 793e 0d0a 2020 2020 3c68 6561 6465 723e  y>..    <header>
+000008b0: 0d0a 2020 2020 2020 2020 3c68 313e 4d79  ..        <h1>My
+000008c0: 2057 6562 7369 7465 3c2f 6831 3e0d 0a20   Website</h1>.. 
+000008d0: 2020 203c 2f68 6561 6465 723e 0d0a 2020     </header>..  
+000008e0: 2020 3c6e 6176 3e0d 0a20 2020 2020 2020    <nav>..       
+000008f0: 207b 2520 666f 7220 6974 656d 2069 6e20   {% for item in 
+00000900: 726f 7574 6572 735f 6d61 7020 257d 207b  routers_map %} {
+00000910: 2520 6966 2027 4745 5427 2069 6e20 726f  % if 'GET' in ro
+00000920: 7574 6572 735f 6d61 705b 6974 656d 5d5b  uters_map[item][
+00000930: 276d 6574 686f 6473 275d 2025 7d0d 0a20  'methods'] %}.. 
+00000940: 2020 2020 2020 203c 6120 6872 6566 3d22         <a href="
+00000950: 7b7b 726f 7574 6572 735f 6d61 705b 6974  {{routers_map[it
+00000960: 656d 5d5b 2770 6174 6827 5d7d 7d22 3e7b  em]['path']}}">{
+00000970: 7b72 6f75 7465 7273 5f6d 6170 5b69 7465  {routers_map[ite
+00000980: 6d5d 5b27 646f 6327 5d20 616e 6420 726f  m]['doc'] and ro
+00000990: 7574 6572 735f 6d61 705b 6974 656d 5d5b  uters_map[item][
+000009a0: 2764 6f63 275d 5b27 7469 746c 6527 5d20  'doc']['title'] 
+000009b0: 6f72 2069 7465 6d7d 7d3c 2f61 3e20 7b25  or item}}</a> {%
+000009c0: 2065 6e64 6966 2025 7d20 7b25 2065 6e64   endif %} {% end
+000009d0: 666f 7220 257d 0d0a 0d0a 2020 2020 2020  for %}....      
+000009e0: 2020 3c61 2068 7265 663d 2223 223e 4162    <a href="#">Ab
+000009f0: 6f75 743c 2f61 3e0d 0a20 2020 2020 2020  out</a>..       
+00000a00: 203c 6120 6872 6566 3d22 2322 3e43 6f6e   <a href="#">Con
+00000a10: 7461 6374 3c2f 613e 207b 2520 6966 2072  tact</a> {% if r
+00000a20: 6571 7565 7374 2e73 6573 7369 6f6e 5b27  equest.session['
+00000a30: 7573 6572 275d 2025 7d0d 0a20 2020 2020  user'] %}..     
+00000a40: 2020 203c 6120 6872 6566 3d22 2f75 7365     <a href="/use
+00000a50: 722f 6c6f 676f 7574 223e 3c62 3e7b 7b72  r/logout"><b>{{r
+00000a60: 6571 7565 7374 2e73 6573 7369 6f6e 5b27  equest.session['
+00000a70: 7573 6572 275d 5b27 7573 6572 6e61 6d65  user']['username
+00000a80: 275d 7d7d 3c2f 623e 204c 6f67 6f75 743c  ']}}</b> Logout<
+00000a90: 2f61 3e20 7b25 2065 6e64 6966 2025 7d0d  /a> {% endif %}.
+00000aa0: 0a20 2020 203c 2f6e 6176 3e0d 0a20 2020  .    </nav>..   
+00000ab0: 203c 7365 6374 696f 6e3e 0d0a 2020 2020   <section>..    
+00000ac0: 2020 2020 3c68 323e 5765 6c63 6f6d 6520      <h2>Welcome 
+00000ad0: 746f 206d 7920 7765 6273 6974 653c 2f68  to my website</h
+00000ae0: 323e 0d0a 2020 2020 2020 2020 3c70 3e54  2>..        <p>T
+00000af0: 6869 7320 6973 2061 6e20 6578 616d 706c  his is an exampl
+00000b00: 6520 6f66 2061 2072 6573 706f 6e73 6976  e of a responsiv
+00000b10: 6520 6465 7369 676e 2074 6861 7420 776f  e design that wo
+00000b20: 726b 7320 7765 6c6c 206f 6e20 626f 7468  rks well on both
+00000b30: 2064 6573 6b74 6f70 2061 6e64 206d 6f62   desktop and mob
+00000b40: 696c 6520 6465 7669 6365 732e 3c2f 703e  ile devices.</p>
+00000b50: 0d0a 2020 2020 2020 2020 3c70 3e68 6572  ..        <p>her
+00000b60: 6520 6973 2074 6865 2060 7465 7874 6020  e is the `text` 
+00000b70: 7661 7269 6162 6c65 2069 6e20 636c 6173  variable in clas
+00000b80: 7320 6d65 7468 6f64 3a7b 7b74 6578 747d  s method:{{text}
+00000b90: 7d3c 2f70 3e0d 0a20 2020 2020 2020 203c  }</p>..        <
+00000ba0: 7020 7374 796c 653d 2263 6f6c 6f72 3a72  p style="color:r
+00000bb0: 6564 223e 3c62 3e7b 7b66 6c61 7368 5b27  ed"><b>{{flash['
+00000bc0: 6d73 6727 5d7d 7d3c 2f62 3e3c 2f70 3e0d  msg']}}</b></p>.
+00000bd0: 0a20 2020 203c 2f73 6563 7469 6f6e 3e0d  .    </section>.
+00000be0: 0a20 2020 203c 666f 6f74 6572 3e0d 0a20  .    <footer>.. 
+00000bf0: 2020 2020 2020 203c 703e 2663 6f70 793b         <p>&copy;
+00000c00: 2032 3032 3320 4d79 2057 6562 7369 7465   2023 My Website
+00000c10: 3c2f 703e 0d0a 2020 2020 3c2f 666f 6f74  </p>..    </foot
+00000c20: 6572 3e0d 0a3c 2f62 6f64 793e 0d0a 6060  er>..</body>..``
+00000c30: 600d 0a                                  `..
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/auth.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/auth.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 from casbin.persist.adapter import Adapter
 # from .midware_casbin import CasbinMiddleware
  
 from .config import config
 import jwt
 from datetime import datetime, timedelta
 from typing import Optional, Tuple, Union,Dict
-
+from ._utils import iJSONEncoder,is_datetime_format
 _session_name:str = ""
 
 class CasbinAuth:
     def __init__(self,enforcer:Enforcer,session_name="user") -> None:
         global _session_name
         self.enforcer = enforcer
         self.__session_name = _session_name = session_name
@@ -39,40 +39,50 @@
             raise AuthenticationError('Could not separate Authorization scheme and token') from e 
         if scheme.lower() != prefix.lower():
             raise AuthenticationError(f'Authorization scheme {scheme} is not supported')
         return token
     def get_user_from_request(self,request:Request,prefix:str="Bearer",is_jwt:bool=False,**kwargs) : 
         userobj = request.session.get(self.__session_name)
         payload = None
-        if userobj:
-            if not isinstance(userobj,str):
-                if hasattr(userobj,"username"):
-                    userobj=getattr(userobj,"username")
-        if not userobj or is_jwt:   
+        username = ''
+       
+        if is_jwt:   
+            username_field = kwargs['username_field']
             auth = request.headers["Authorization"] if 'Authorization' in request.headers else None
             if auth:
-                scheme, credentials = auth.split()
+                scheme, credentials = auth.split() 
+                token = self.__get_token_from_header(authorization=auth, prefix=prefix)
                 
-                if not is_jwt: #not userobj?
-                    decoded = base64.b64decode(credentials).decode("ascii")
-                    username, _, password = decoded.partition(":")
-                    return username,password,None
-                else:
-                    token = self.__get_token_from_header(authorization=auth, prefix=prefix)
-                    username_field = kwargs['username_field']
-                    del kwargs['username_field']
+                del kwargs['username_field']
+                try:
+                    payload = jwt.decode(token,**kwargs)
+                except jwt.InvalidTokenError as e:
+                    raise AuthenticationError(str(e)) from e
+                if is_datetime_format(payload['exp']):
+                    payload['exp'] =   datetime.fromisoformat(payload['exp'])
+
+
+                return  payload[username_field],token,payload
+            elif userobj:
+                if 'token' in userobj:
                     try:
-                        payload = jwt.decode(token,**kwargs)
-                    except jwt.InvalidTokenError as e:
+                        payload = jwt.decode(userobj['token'],**kwargs)
+                    except jwt.InvalidTokenError as e:#Signature has expired
+                        return "","",None
                         raise AuthenticationError(str(e)) from e
-                    return  payload[username_field],token,payload
-            elif userobj:
-                return userobj,"",None
+                     
+                    return  payload[username_field],userobj['token'],payload
         else:
-            return userobj,"",None
+            if userobj: 
+                return userobj,"",None
+            else:
+                decoded = base64.b64decode(credentials).decode("ascii")
+                username, _, password = decoded.partition(":")
+                if username:
+                    return username,password,None
         return "","",None
     
 class BasicAuth(AuthenticationBackend):
     def __init__(self,**kwargs) -> None:
         super().__init__()
      
     
@@ -85,15 +95,18 @@
         auth_type:str = kwargs.get("auth_type")
         if not auth_type or auth_type.lower()=='public': 
             return True,  user
         result = _casbin_auth._auth(request=request,username=username)
         return result, user
 
         return AuthCredentials(["authenticated"]), SimpleUser(username)
-    
+    def clear_userinfo(self,request:Request):
+        global _session_name
+        del request.session[_session_name] 
+        
     def create_access_token(self,  username,**kwargs):
         global _session_name
         request:Request = kwargs['request'] if 'request' in kwargs else None
         if request:
             request.session[_session_name] = username
         return None
         
@@ -127,49 +140,67 @@
         self.username_field = username_field
         self.audience = audience
         self.options = options or dict()
     
      
     
     async def authenticate(self, request,response,**kwargs) -> Union[None, Tuple[AuthCredentials, BaseUser]]:
+        auth_type:str = kwargs.get("auth_type")
+
         args = {'username_field':self.username_field, 'key':self.secret_key, 'algorithms': self.algorithm , 'audience':self.audience ,
                                             'options':self.options }
-        username,token,payload = _casbin_auth.get_user_from_request(request=request,
+        userobj,token,payload = _casbin_auth.get_user_from_request(request=request,
                                                                  prefix=self.prefix, 
                                                                  is_jwt=True,**args)
-        if not username:
-            return False,None
-        user = SimpleUser(username)
+         
+        user = userobj#SimpleUser(userobj['username'])
         request.scope['user'] = user
-        auth_type:str = kwargs.get("auth_type")
-        if not auth_type or auth_type.lower()=='public': 
-            return True,SimpleUser(username)    
-        
+        if  auth_type.lower()=='public': 
+            if userobj:
+                if hasattr(userobj,'token') or token or payload:
+                    if payload and token:
+                        request.scope['user'] = JWTUser(username=payload[self.username_field], token=token,
+                                                        payload=payload)  
+                        return True, request.scope['user']
+                else:
+                    return True,None
+            else:
+                return True, None
         if  payload:
-            result = _casbin_auth._auth(request=request,username=payload[self.username_field])
-            return result, JWTUser(username=payload[self.username_field], token=token,
+            user = JWTUser(username=payload[self.username_field], token=token,
                                                         payload=payload) 
+            request.scope['user'] = user
+            result = _casbin_auth._auth(request=request,username=payload[self.username_field])
+            
+            return result, user  
         return False,None
- 
+    def clear_userinfo(self,request:Request):
+        global _session_name
+        del request.session[_session_name] 
     def create_access_token(self,  user , expires_delta: timedelta = None,**kwargs)  :
+        global _session_name
         if expires_delta:
             expire = datetime.utcnow() + expires_delta
         else:
             authCfg = config.get('auth')
             if authCfg:
                 expires_delta = int(authCfg.get('expires_delta',60))
             else:
                 expires_delta = 60
             expire = datetime.utcnow() + timedelta(
                 minutes=expires_delta
             )
-        to_encode = {"exp": expire, "username": user }
+        userObj = {"exp": expire, "username": user }
+        request:Request = kwargs['request']
         
-        return jwt.encode(to_encode, self.secret_key ,self.algorithm )
-
+        access_token = jwt.encode(userObj, self.secret_key ,self.algorithm )
+        userObj.update({"token":access_token})
+        request.session[_session_name] = userObj
+        return access_token
+    
 _casbin_auth:CasbinAuth = None
 
 def init(app:FastAPI,backend:AuthenticationBackend,adapter:Adapter=None,**kwagrs)->AuthenticationBackend:
     """
         kwargs:secret_key=KEY
     """
     __session_name = config.get("auth").get("session_name",'user')
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/base_controller.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/base_controller.py`

 * *Files 10% similar despite different names*

```diff
@@ -44,33 +44,43 @@
     # @response.setter
     # def response(self,value):
     #     self.__response = value
     @property
     def session(self)->Dict:
         return self._session  
     @classmethod
-    def redirect(self,url,flash:str="",statu_code=StateCodes.HTTP_303_SEE_OTHER):
-        self._session['flash'] = {"url" : flash }
+    def redirect(self,url ,statu_code=StateCodes.HTTP_303_SEE_OTHER):
+         
         return RedirectResponse(url,status_code=statu_code)
     
     def _verity_successed(self,user,msg="User authentication successed!"):
         """see .core.py"""
         pass
         
-    
+    def _user_logout(self):
+        """see .core.py"""
+        pass
+
     def _verity_error(self,msg="User authentication failed!"):
         """see .core.py"""
         pass
 
     def check_redirect_back(self):
         flash = self.session.get('flash')
-        flash = flash['url'] if flash else ""
-        return self.redirect(url=flash) if flash else self.redirect("/")
-
-     
+        url = flash['url'] if flash and flash.get("url") else "/"
+        return self.redirect(url=url)  
+    @classmethod
+    def _set_flash(self,msg,url=""): 
+        self._request.state.keep_flash = True
+        if url:
+            self._session['flash'] = {'url':url,'msg':msg}
+        else:
+            
+            self._session['flash']['msg']=msg
+    
     # @property
     def view(self,content:str="",view_path:str="", format:str="html", context: dict={},local2context:bool=True,**kwargs): 
         def url_for(url:str="",type:str="static",**kws):
             url_path :str = self.__view_url__ 
             url = url.strip()
             if type!='static' or kws: #url route
                 if kws:
@@ -151,24 +161,20 @@
         save_file = os.path.join(_save_dir, md5_name) 
         if not os.path.exists(save_file): 
             f = open(save_file, 'wb') 
             f.write(data)
             f.close()
         return save_file
     async def _constructor(base_controller_class,request:Request,response:Response):  
-        # if not hasattr(request,'params') and request.method!='GET' :
-        #     request.params = await request.json()
-        # if not hasattr(request,'params'):
-        #     request.params = {}
-        #     if request.query_params:
-        #         request.params = dict(request.query_params)
+   
+        request.state.keep_flash = False 
         if not _session_key in request.cookies or not request.cookies[_session_key]:
             request.cookies[_session_key] = str(uuid.uuid4())
 
-        request.state.keep_flash = False
+         
         base_controller_class._request:Request = request
         base_controller_class._response:Response = response 
         base_controller_class._cookies:Dict[str,str] = request.cookies.copy()
         # base_controller_class._session = await  _sessionManager.initSession(request,response )
         base_controller_class._session = request.session
         
          
@@ -183,16 +189,11 @@
             response.set_cookie(key=_session_key,
                                 value=base_controller_class._request.cookies[_session_key],
                                 max_age = 14 * 24 * 60 * 60,  # 14 days, in seconds
                                 path  = "/",
                                 samesite  = "lax",
                                 httponly  = False ) 
         process_cookies(new_response,base_controller_class._cookies,base_controller_class._request.cookies)
-        # await _sessionManager.process(session =  base_controller_class._session,response = new_response,request=base_controller_class._request)
-        flash:Dict =  base_controller_class._session.get("flash")
-        if flash and not base_controller_class._request.state.keep_flash:
-            base_controller_class._session['flash'] = {}
-            url = flash.get("url") 
-            if url: 
-                return base_controller_class.redirect(url)
+    
+
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/cbv.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/cbv.py`

 * *Files identical despite different names*

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/config.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/config.py`

 * *Files 19% similar despite different names*

```diff
@@ -8,14 +8,22 @@
  'ERROR' : 40,
  'WARNING' : 30,
  'INFO' : 20,
  'DEBUG' : 10,
  'NOTSET' : 0,
 }
 
+import re
+
+def extract_name(string):
+    match = re.search(r'{([^}]*)}', string)
+    if match:
+        return match.group(1)
+    else:
+        return None
 
 class YamlConfig:
     def __init__(self, filename):
         self.filename = filename
         self.config = {}
         self.load()
 
@@ -29,15 +37,22 @@
             raise ValueError(f"{self.filename} is not a file or directory")
 
     def save(self):
         with open(self.filename, "w") as f:
             yaml.safe_dump(self.config, f)
 
     def get(self, key, default=None):
-        return self.config.get(key, default)
+        value:str = self.config.get(key, default)
+        if isinstance(value,str) and value.find("{")>-1:
+            name = extract_name(value)
+            if name:
+                expr = self.config.get(name,"")
+                x = f"{name}"
+                value = value.replace('{'+x+'}',expr)
+        return value
 
     def set(self, key, value):
         self.config[key] = value
 
     def delete(self, key):
         del self.config[key]
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/controller.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/controller.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from typing import Type,TYPE_CHECKING, Any, Callable, get_type_hints 
 from fastapi import FastAPI,APIRouter  
 from .controller_utils import (TEMPLATE_PATH_KEY, VER_KEY, ControllerBase,
                                _get_leaf_controllers,
                                _register_controller_to_router, _route_method)
 
  
- 
+import inspect
 
 class InferringRouter(APIRouter):
     """
     Overrides the route decorator logic to use the annotated return type as the `response_model` if unspecified.
     """
 
     if not TYPE_CHECKING:  # pragma: no branch
@@ -72,14 +72,20 @@
     setattr(GeneratedController, TEMPLATE_PATH_KEY, template_path_prefix)
     setattr(GeneratedController, VER_KEY, version)
 
     return GeneratedController
 
 
 class controller:
+    @staticmethod
+    def login(path,*args,**kwargs):  
+        kwargs['__auth_url__']=path
+        return  _route_method(path,method='get',*args,**kwargs)
+         
+        
     """ """
     @staticmethod
     def http(path,methods=['GET'],*args,**kwargs):
         return _route_method(path,method=methods,*args,**kwargs)
     @staticmethod
     def get(path: str, *args, **kwargs): 
         return _route_method(path, "get", *args, **kwargs)
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/controller_utils.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/controller_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -286,14 +286,16 @@
     # response_status_code = 403
     # response = Response(content=response_content, headers=response_headers, status_code=response_status_code)
     
     # 抛出 403 错误，使用自定义的响应对象
     raise HTTPException(status_code=403, detail="未经授权的访问" )
 
 def _route_method(path: str, method, *args, **mwargs): 
+    if not path.startswith("/"):
+        raise "path must start with '/'"
     def wrapper(func ): 
         @wraps(func)
         async def decorator(  *args, **kwargs):
             # 获取当前方法的名称
             # method_name = inspect.currentframe().f_code.co_name
             # # 获取当前方法的对象
             # method_obj = inspect.currentframe().f_back.f_locals.get(method_name)
@@ -309,23 +311,24 @@
             #instance = cls.__dict__.get('__wrapped__', None).__self__ #or cls.__dict__.get('__objclass__', None)(obj)
             response:Response = None
             result:Response = None
             
             if 'request' in kwargs and 'response' in kwargs:
                 response  = kwargs["response"]
                 rqst = kwargs['request'] 
-                await cls._constructor(cls,request = kwargs['request'],response=kwargs['response'])
                 
-                if auth_type.lower() !="none":
+                
+                if auth_type and auth_type !="none"  :
                     auth_result,user = await cls._auth__(request=rqst,response=kwargs['response'],auth_type=auth_type)
                     if isinstance(auth_result,Response):
                         return auth_result
                     if not auth_result:
                         auth_error()
-                
+                await cls._constructor(cls,request = kwargs['request'],response=kwargs['response'])
+
             if 'request' in kwargs and not has_request:  
                 del kwargs['request']  
             if 'response' in kwargs and not has_response:  
                 del kwargs['response']  
             del kwargs["__has_request__"]
             del kwargs["__has_response__"]
             if inspect.iscoroutinefunction(func):
@@ -338,14 +341,18 @@
                 ret = await cls._deconstructor(cls,result)
                 if isinstance(ret,Response):
                     return ret
             return result
         setattr(decorator, PATH_KEY, path)
         setattr(decorator, METHOD_KEY, method)
         setattr(decorator, ARGS_KEY, args)
+        if '__auth_url__' in mwargs: 
+            setattr(func,'__auth_url__',mwargs['__auth_url__'])
+            del mwargs['__auth_url__']
+
         if not 'auth' in mwargs:
             mwargs["auth"] = 'public'
         setattr(func,"__auth__",mwargs['auth'])
         del mwargs['auth']
         setattr(decorator, KWARGS_KEY, mwargs)
         # setattr(decorator,'__doc__',getattr(func,'__doc__'))
         setattr(decorator, "__signature__", inspect.signature(func))
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/core.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/core.py`

 * *Files 9% similar despite different names*

```diff
@@ -77,68 +77,84 @@
     __all_controller__.append(_controllerBase)
     
     def _wapper(targetController):  
         
         class puppetController( targetController ,_controllerBase ): 
             '''puppet class inherited by the User defined controller class '''
             def __init__(self,**kwags) -> None: 
+                
                 super().__init__()
+            def _user_logout(self):
+                """see .core.py"""
+                if  hasattr(application,'authObj'):
+                    application.authObj.clear_userinfo(request=self.request)
+                accept_header = self.request.headers.get("Accept")    
+                if accept_header == "application/json":
+                    return {'status':'success','msg':'your are successed logout!'}
+                else:
+                    return self.redirect('/')
             def _verity_successed(self,user,msg="User authentication successed!"):
                 '''call by targetController'''
                 ret = None
+                self._set_flash( msg=msg)
+    
+                accept_header = self.request.headers.get("Accept")
                 if  hasattr(application,'authObj'):
-                    ret = application.authObj.create_access_token(user,request=self.request)
-                if not ret:
+                    access_token = application.authObj.create_access_token(user,request=self.request)
+                if not access_token:
+                    if accept_header == "application/json":
+                        return {'status':'success' }
                     return self.check_redirect_back()
-                else:
-                    return {'status':'success','token':str(ret)}
+                else:  
+                    if accept_header == "application/json":
+                        return {'status':'success','token':str(access_token)}
+                    else:
+                        return self.check_redirect_back()
             
             def _verity_error(self,msg="User authentication failed!"):
                 '''call by targetController'''
                 self.request.state.keep_flash = True 
                 self._session['flash'] = {'url':str(self.request.url), 'msg':msg}
-                url =  self.request.headers.get("Referer")
+                url =  self.request.headers.get("Referer") or '/'
                 accept_header = self.request.headers.get("Accept")
                 if accept_header == "application/json":
-                    return JSONResponse(content={'status':StateCodes.HTTP_401_UNAUTHORIZED,'msg':msg})
+                    return JSONResponse(content={'status':StateCodes.HTTP_200_OK,'msg':msg})
                 return RedirectResponse(url,status_code=StateCodes.HTTP_303_SEE_OTHER),None
             
             @classmethod
             async def _auth__(cls,request:Request,response:Response,**kwargs):
                 '''called by .controller_util.py->route_method'''
-
                 if not hasattr(application,'authObj'):
                     return True,None
-                
-                kwargs['session'] = cls._session
+                auth_type = kwargs['auth_type'] 
+                kwargs['session'] = request.session # cls._session
                 ret,user = await application.authObj.authenticate(request,response,**kwargs)
                 def add_redirect_param(url: str, redirect_url: str) -> str:
                     if "?" in url:
                         return url + "&redirect=" + redirect_url
                     else:
                         return url + "?redirect=" + redirect_url
                 accept_header = request.headers.get("Accept")
                 
-
-                if not ret and not user:
-                    if hasattr(cls,"_auth_url"):
-                        url = getattr(cls,"_auth_url") 
-                        # cls._session['flash'] = {'url':str(request.url), 'msg':'you are not authenticated,please login!'}
-                        url = add_redirect_param(url,str(request.url))
-                        if accept_header == "application/json":
-                            return  ORJSONResponse(content={"message": f"401 UNAUTHORIZED! go to `{url}` to Authenticate"},
+                #
+                if not ret and not user: 
+                    if accept_header == "application/json":
+                        return  ORJSONResponse(content={"message": "401 UNAUTHORIZED!"},
                                                    status_code=StateCodes.HTTP_401_UNAUTHORIZED),None
-                        return RedirectResponse(url,status_code=StateCodes.HTTP_303_SEE_OTHER),None
-                    else:
-                        if accept_header == "application/json":
-                            return  ORJSONResponse(content={"message": "401 UNAUTHORIZED!"},
-                                                   status_code=StateCodes.HTTP_401_UNAUTHORIZED),None
-                        cls._session['flash'] = {'msg':'you are not authenticated!'}
+                    _auth_url = getattr(application,f"_{auth_type}_auth_url") if hasattr(application,f"_{auth_type}_auth_url") else None
+
+                    if _auth_url:
+                        request.state.keep_flash = True
+                        request.session['flash']={'url':str(request.url),'msg':'you are not authenticated,please login!'}
+                        _auth_url = add_redirect_param(_auth_url,str(request.url))
+                        return RedirectResponse(_auth_url,status_code=StateCodes.HTTP_303_SEE_OTHER),None
+                    else:  
                         return RedirectResponse('/',status_code=StateCodes.HTTP_303_SEE_OTHER),None
-                return ret,user
+                else:
+                    return ret,user
 
         setattr(puppetController,"__auth__",allargs['auth'])         
         setattr(puppetController,"__name__",targetController.__name__)  
         setattr(puppetController,"__controller_name__",targetController.__name__.lower().replace("controller",""))  
         
         setattr(puppetController,"__version__",version)  
         setattr(puppetController,"__location__",relative_path)  
@@ -157,34 +173,40 @@
             _static_path = _view_url_path              
             __app.mount(_static_path,  StaticFiles(directory=__app_views_dirs[app_dir]), name=os.path.basename(app_dir))
  
         return puppetController 
     return _wapper #: @puppetController 
 
 
+def get_wrapped_endpoint(func):
+    ret = func
+    while hasattr(ret,'__wrapped__'):
+        ret = getattr(ret,'__wrapped__')
+    return ret
 
 def generate_mvc_app(isDebug):
     if not len(__all_controller__)>0:
         raise "must use @api_route to define a controller class"
     all_routers = []
     all_routers_map = {}
     for ctrl in __all_controller__:
         all_routers.append(register_controllers_to_app(__app, ctrl))
     for router in all_routers:
         for r in router.routes:
             funcname = str(r.endpoint).split('<function ')[1].split(" at ")[0] 
+            end_point_abs = get_wrapped_endpoint(r.endpoint)
+            auth_type = getattr(end_point_abs,'__auth__') if hasattr(end_point_abs,'__auth__') else 'None'
             doc_map =  get_docs(r.description) if hasattr(r,'description') else {}
             if hasattr(r,'methods'):
                 methods = r.methods
             else:
                 methods = r.name
-            if isDebug: 
-                # _log.debug('{:18}{:30}{}'.format(str(methods),r.path,funcname) )
+            if isDebug:  
                 _log.debug('{:20}-->{:50}-->{}'.format(str(methods),r.path,funcname) )
-            all_routers_map[funcname] = {'path':r.path,'methods':methods,'doc':doc_map}
+            all_routers_map[funcname] = {'path':r.path,'methods':methods,'doc':doc_map,'auth':auth_type}
     application.routers_map = all_routers_map  
     midware.init(app=application,debug=isDebug)
     
     auth_type = config.get("auth",None)
     if auth_type:
         auth_type=auth_type.get("type" )
         if auth_type:
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/midware_casbin.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/midware_casbin.py`

 * *Files identical despite different names*

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/midware_session.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/midware_session.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 from starlette.types import ASGIApp, Message, Receive, Scope, Send
 from .config import _log
 from .base_controller import _session_key
 if sys.version_info >= (3, 8):  # pragma: no cover
     from typing import Literal
 else:  # pragma: no cover
     from typing_extensions import Literal
+from ._utils import iJSONEncoder,is_datetime_format
 
 class SessionStorage(): 
     def __init__(self) -> None:  
         super().__init__()
      
     def get(self, session_id: str) :
         raise NotImplementedError
@@ -104,15 +105,15 @@
         def get(self, session_id: str) -> Dict:
             data = self.redis_client.get(session_id)
             if data is None:
                 return {}
             return json.loads(data)
 
         def set(self, session_id: str, data: Dict) -> None:
-            self.redis_client.set(session_id, json.dumps(data))
+            self.redis_client.set(session_id, json.dumps(data,cls=iJSONEncoder))
 
         def delete(self, session_id: str) -> None:
             self.redis_client.delete(session_id)
 except(ImportError):
     class RedisStorage(SessionStorage):
         def __init__(self, k: str = "") -> None:
             raise ImportError("redis seen is not installed,please use `pip install redis` to install it.")
@@ -170,19 +171,26 @@
                 scope["session"] = {}
         else:
             
             scope["session"] = {}
         # old_data = scope["session"].copy()
 
         async def send_wrapper(message: Message) -> None:
+            if message["type"] == "http.response.start":
+                if 'state' in scope and 'keep_flash' in scope['state']:
+                    if not scope['state']['keep_flash']:
+                        scope['session']['flash'] = {}
+                # else:
+                #     scope['session']['flash'] = {}
+
             if self.storage is None:
                 if message["type"] == "http.response.start":
                     if scope["session"]:
                         # We have session data to persist.
-                        data = b64encode(json.dumps(scope["session"]).encode("utf-8"))
+                        data = b64encode(json.dumps(scope["session"],cls=iJSONEncoder).encode("utf-8"))
                         data = self.signer.sign(data)
                         headers = MutableHeaders(scope=message)
                         header_value = "{session_cookie}={data}; path={path}; {max_age}{security_flags}".format(  # noqa E501
                             session_cookie=self.session_cookie_key,
                             data=data.decode("utf-8"),
                             path=self.path,
                             max_age=f"Max-Age={self.max_age}; " if self.max_age else "",
@@ -198,15 +206,17 @@
                             path=self.path,
                             expires="expires=Thu, 01 Jan 1970 00:00:00 GMT; ",
                             security_flags=self.security_flags,
                         )
                         headers.append("Set-Cookie", header_value)
             else:
                 if message["type"] == "http.response.start":
-                    data = b64encode(json.dumps(scope["session"]).encode("utf-8"))
+                    
+
+                    data = b64encode(json.dumps(scope["session"],cls=iJSONEncoder).encode("utf-8"))
                     data = self.signer.sign(data)
                     # data = data.decode("utf-8")
                     
                         # The session has not been inited.
                     def find_session_id():
                         for key,content in message['headers']:
                             if key==b'set-cookie' and content.startswith(bytes(self.session_cookie_key,'utf-8')):
```

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework/view.py` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework/view.py`

 * *Files identical despite different names*

### Comparing `fastapi_mvc_framework-1.1.0/fastapi_mvc_framework.egg-info/SOURCES.txt` & `fastapi_mvc_framework-1.1.1/fastapi_mvc_framework.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 README.md
 setup.py
 fastapi_mvc_framework/__init__.py
+fastapi_mvc_framework/_utils.py
 fastapi_mvc_framework/auth.py
 fastapi_mvc_framework/base_controller.py
 fastapi_mvc_framework/cbv.py
 fastapi_mvc_framework/config.py
 fastapi_mvc_framework/controller.py
 fastapi_mvc_framework/controller_utils.py
 fastapi_mvc_framework/core.py
```

### Comparing `fastapi_mvc_framework-1.1.0/setup.py` & `fastapi_mvc_framework-1.1.1/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 
 setup(
     name='fastapi_mvc_framework',
-    version='1.1.0',
+    version='1.1.1',
     author='Bruce chou',
     author_email='smjkzsl@gmail.com',
     description='Simple and elegant use of FastApi in MVC mode',
     long_description=long_description,
     long_description_content_type="text/markdown",
     
     url='https://github.com/smjkzsl/fastapi_framework',
```

