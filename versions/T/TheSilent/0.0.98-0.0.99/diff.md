# Comparing `tmp/TheSilent-0.0.98.tar.gz` & `tmp/TheSilent-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "TheSilent-0.0.98.tar", last modified: Sun Jan  8 22:12:33 2023, max compression
+gzip compressed data, was "TheSilent-0.0.99.tar", last modified: Mon Jan  9 15:25:09 2023, max compression
```

## Comparing `TheSilent-0.0.98.tar` & `TheSilent-0.0.99.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-08 22:12:33.524835 TheSilent-0.0.98/
--rw-r--r--   0 linux     (1000) linux     (1000)      643 2023-01-08 22:12:33.524835 TheSilent-0.0.98/PKG-INFO
--rw-r--r--   0 linux     (1000) linux     (1000)      101 2023-01-06 01:24:13.000000 TheSilent-0.0.98/README.md
--rw-r--r--   0 linux     (1000) linux     (1000)      735 2023-01-08 22:09:10.000000 TheSilent-0.0.98/pyproject.toml
--rw-r--r--   0 linux     (1000) linux     (1000)       38 2023-01-08 22:12:33.524835 TheSilent-0.0.98/setup.cfg
-drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-08 22:12:33.515835 TheSilent-0.0.98/src/
-drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-08 22:12:33.522835 TheSilent-0.0.98/src/TheSilent/
--rw-r--r--   0 linux     (1000) linux     (1000)      762 2023-01-08 22:12:06.000000 TheSilent-0.0.98/src/TheSilent/TheSilent.py
--rw-r--r--   0 linux     (1000) linux     (1000)        0 2023-01-06 01:24:13.000000 TheSilent-0.0.98/src/TheSilent/__init__.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1324 2023-01-08 22:09:59.000000 TheSilent-0.0.98/src/TheSilent/arp_void.py
--rw-r--r--   0 linux     (1000) linux     (1000)     6976 2023-01-08 22:10:13.000000 TheSilent-0.0.98/src/TheSilent/brute_force_hash.py
--rw-r--r--   0 linux     (1000) linux     (1000)      167 2023-01-08 20:46:15.000000 TheSilent-0.0.98/src/TheSilent/clear.py
--rw-r--r--   0 linux     (1000) linux     (1000)    17412 2023-01-08 22:10:20.000000 TheSilent-0.0.98/src/TheSilent/dictionary_hash.py
--rw-r--r--   0 linux     (1000) linux     (1000)     7894 2023-01-08 22:10:23.000000 TheSilent-0.0.98/src/TheSilent/email_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1247 2023-01-08 21:08:17.000000 TheSilent-0.0.98/src/TheSilent/form_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1812 2023-01-08 22:10:31.000000 TheSilent-0.0.98/src/TheSilent/ftp_cracker.py
--rw-r--r--   0 linux     (1000) linux     (1000)      781 2023-01-08 22:10:35.000000 TheSilent-0.0.98/src/TheSilent/hex_viewer.py
--rw-r--r--   0 linux     (1000) linux     (1000)     8795 2023-01-08 22:10:41.000000 TheSilent-0.0.98/src/TheSilent/link_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     5982 2023-01-08 22:10:47.000000 TheSilent-0.0.98/src/TheSilent/login_cracker.py
--rw-r--r--   0 linux     (1000) linux     (1000)     5074 2023-01-08 22:10:51.000000 TheSilent-0.0.98/src/TheSilent/nmap.py
--rw-r--r--   0 linux     (1000) linux     (1000)    19506 2023-01-08 22:10:56.000000 TheSilent-0.0.98/src/TheSilent/packet_sniffer.py
--rw-r--r--   0 linux     (1000) linux     (1000)     2541 2023-01-08 22:11:02.000000 TheSilent-0.0.98/src/TheSilent/port_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1833 2023-01-08 22:11:07.000000 TheSilent-0.0.98/src/TheSilent/secure_overwrite.py
--rw-r--r--   0 linux     (1000) linux     (1000)      800 2023-01-08 22:11:13.000000 TheSilent-0.0.98/src/TheSilent/security_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)      831 2023-01-08 22:11:18.000000 TheSilent-0.0.98/src/TheSilent/source_code_viewer.py
--rw-r--r--   0 linux     (1000) linux     (1000)     9363 2023-01-08 22:11:23.000000 TheSilent-0.0.98/src/TheSilent/sql_injection_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1307 2023-01-08 22:11:27.000000 TheSilent-0.0.98/src/TheSilent/subdomain_scanner.py
--rw-r--r--   0 linux     (1000) linux     (1000)     1366 2023-01-08 22:11:32.000000 TheSilent-0.0.98/src/TheSilent/subdomain_takeover.py
--rw-r--r--   0 linux     (1000) linux     (1000)     6125 2023-01-08 22:11:40.000000 TheSilent-0.0.98/src/TheSilent/xss_scanner.py
-drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-08 22:12:33.523835 TheSilent-0.0.98/src/TheSilent.egg-info/
--rw-r--r--   0 linux     (1000) linux     (1000)      643 2023-01-08 22:12:33.000000 TheSilent-0.0.98/src/TheSilent.egg-info/PKG-INFO
--rw-r--r--   0 linux     (1000) linux     (1000)      883 2023-01-08 22:12:33.000000 TheSilent-0.0.98/src/TheSilent.egg-info/SOURCES.txt
--rw-r--r--   0 linux     (1000) linux     (1000)        1 2023-01-08 22:12:33.000000 TheSilent-0.0.98/src/TheSilent.egg-info/dependency_links.txt
--rw-r--r--   0 linux     (1000) linux     (1000)       23 2023-01-08 22:12:33.000000 TheSilent-0.0.98/src/TheSilent.egg-info/requires.txt
--rw-r--r--   0 linux     (1000) linux     (1000)       10 2023-01-08 22:12:33.000000 TheSilent-0.0.98/src/TheSilent.egg-info/top_level.txt
+drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-09 15:25:09.786667 TheSilent-0.0.99/
+-rw-r--r--   0 linux     (1000) linux     (1000)      643 2023-01-09 15:25:09.786667 TheSilent-0.0.99/PKG-INFO
+-rw-r--r--   0 linux     (1000) linux     (1000)      101 2023-01-06 01:24:13.000000 TheSilent-0.0.99/README.md
+-rw-r--r--   0 linux     (1000) linux     (1000)      735 2023-01-09 15:05:42.000000 TheSilent-0.0.99/pyproject.toml
+-rw-r--r--   0 linux     (1000) linux     (1000)       38 2023-01-09 15:25:09.786667 TheSilent-0.0.99/setup.cfg
+drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-09 15:25:09.777667 TheSilent-0.0.99/src/
+drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-09 15:25:09.785667 TheSilent-0.0.99/src/TheSilent/
+-rw-r--r--   0 linux     (1000) linux     (1000)      762 2023-01-08 22:12:06.000000 TheSilent-0.0.99/src/TheSilent/TheSilent.py
+-rw-r--r--   0 linux     (1000) linux     (1000)        0 2023-01-06 01:24:13.000000 TheSilent-0.0.99/src/TheSilent/__init__.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1324 2023-01-08 22:09:59.000000 TheSilent-0.0.99/src/TheSilent/arp_void.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     6976 2023-01-08 22:10:13.000000 TheSilent-0.0.99/src/TheSilent/brute_force_hash.py
+-rw-r--r--   0 linux     (1000) linux     (1000)      167 2023-01-08 20:46:15.000000 TheSilent-0.0.99/src/TheSilent/clear.py
+-rw-r--r--   0 linux     (1000) linux     (1000)    17412 2023-01-08 22:10:20.000000 TheSilent-0.0.99/src/TheSilent/dictionary_hash.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     7894 2023-01-08 22:10:23.000000 TheSilent-0.0.99/src/TheSilent/email_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1247 2023-01-08 21:08:17.000000 TheSilent-0.0.99/src/TheSilent/form_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1812 2023-01-08 22:10:31.000000 TheSilent-0.0.99/src/TheSilent/ftp_cracker.py
+-rw-r--r--   0 linux     (1000) linux     (1000)      781 2023-01-08 22:10:35.000000 TheSilent-0.0.99/src/TheSilent/hex_viewer.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     9590 2023-01-09 15:24:17.000000 TheSilent-0.0.99/src/TheSilent/link_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     5982 2023-01-08 22:10:47.000000 TheSilent-0.0.99/src/TheSilent/login_cracker.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     5074 2023-01-08 22:10:51.000000 TheSilent-0.0.99/src/TheSilent/nmap.py
+-rw-r--r--   0 linux     (1000) linux     (1000)    19506 2023-01-08 22:10:56.000000 TheSilent-0.0.99/src/TheSilent/packet_sniffer.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     2541 2023-01-08 22:11:02.000000 TheSilent-0.0.99/src/TheSilent/port_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1833 2023-01-08 22:11:07.000000 TheSilent-0.0.99/src/TheSilent/secure_overwrite.py
+-rw-r--r--   0 linux     (1000) linux     (1000)      800 2023-01-08 22:11:13.000000 TheSilent-0.0.99/src/TheSilent/security_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)      831 2023-01-08 22:11:18.000000 TheSilent-0.0.99/src/TheSilent/source_code_viewer.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     9363 2023-01-08 22:11:23.000000 TheSilent-0.0.99/src/TheSilent/sql_injection_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1307 2023-01-08 22:11:27.000000 TheSilent-0.0.99/src/TheSilent/subdomain_scanner.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     1366 2023-01-08 22:11:32.000000 TheSilent-0.0.99/src/TheSilent/subdomain_takeover.py
+-rw-r--r--   0 linux     (1000) linux     (1000)     7212 2023-01-09 15:19:41.000000 TheSilent-0.0.99/src/TheSilent/xss_scanner.py
+drwxr-xr-x   0 linux     (1000) linux     (1000)        0 2023-01-09 15:25:09.786667 TheSilent-0.0.99/src/TheSilent.egg-info/
+-rw-r--r--   0 linux     (1000) linux     (1000)      643 2023-01-09 15:25:09.000000 TheSilent-0.0.99/src/TheSilent.egg-info/PKG-INFO
+-rw-r--r--   0 linux     (1000) linux     (1000)      883 2023-01-09 15:25:09.000000 TheSilent-0.0.99/src/TheSilent.egg-info/SOURCES.txt
+-rw-r--r--   0 linux     (1000) linux     (1000)        1 2023-01-09 15:25:09.000000 TheSilent-0.0.99/src/TheSilent.egg-info/dependency_links.txt
+-rw-r--r--   0 linux     (1000) linux     (1000)       23 2023-01-09 15:25:09.000000 TheSilent-0.0.99/src/TheSilent.egg-info/requires.txt
+-rw-r--r--   0 linux     (1000) linux     (1000)       10 2023-01-09 15:25:09.000000 TheSilent-0.0.99/src/TheSilent.egg-info/top_level.txt
```

### Comparing `TheSilent-0.0.98/PKG-INFO` & `TheSilent-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: TheSilent
-Version: 0.0.98
+Version: 0.0.99
 Summary: Python penetration testing, osint, and digital forensics multi tool!
 Author-email: Michael Mueller <michael.j.mueller.pro@gmail.com>
 Project-URL: Homepage, https://github.com/Invizabel/The-Silent
 Project-URL: Bug Tracker, https://github.com/Invizabel/The-Silent/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `TheSilent-0.0.98/pyproject.toml` & `TheSilent-0.0.99/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "TheSilent"
-version = "0.0.98"
+version = "0.0.99"
 authors = [
   { name="Michael Mueller", email="michael.j.mueller.pro@gmail.com" },
 ]
 description = "Python penetration testing, osint, and digital forensics multi tool!"
 readme = "README.md"
 license = { file="LICENSE.txt" }
 requires-python = ">=3.7"
```

### Comparing `TheSilent-0.0.98/src/TheSilent/TheSilent.py` & `TheSilent-0.0.99/src/TheSilent/TheSilent.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/arp_void.py` & `TheSilent-0.0.99/src/TheSilent/arp_void.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/brute_force_hash.py` & `TheSilent-0.0.99/src/TheSilent/brute_force_hash.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/dictionary_hash.py` & `TheSilent-0.0.99/src/TheSilent/dictionary_hash.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/email_scanner.py` & `TheSilent-0.0.99/src/TheSilent/email_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/form_scanner.py` & `TheSilent-0.0.99/src/TheSilent/form_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/ftp_cracker.py` & `TheSilent-0.0.99/src/TheSilent/ftp_cracker.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/hex_viewer.py` & `TheSilent-0.0.99/src/TheSilent/hex_viewer.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/link_scanner.py` & `TheSilent-0.0.99/src/TheSilent/link_scanner.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,550 +1,600 @@
 00000000: 6672 6f6d 2054 6865 5369 6c65 6e74 2e63  from TheSilent.c
 00000010: 6c65 6172 2069 6d70 6f72 7420 2a0a 0a69  lear import *..i
 00000020: 6d70 6f72 7420 7265 0a69 6d70 6f72 7420  mport re.import 
 00000030: 7265 7175 6573 7473 0a0a 7265 6420 3d20  requests..red = 
-00000040: 225c 3033 335b 313b 3331 6d22 0a0a 2363  "\033[1;31m"..#c
-00000050: 7265 6174 6520 6874 6d6c 2073 6573 7369  reate html sessi
-00000060: 6f6e 7320 6f62 6a65 6374 0a77 6562 5f73  ons object.web_s
-00000070: 6573 7369 6f6e 203d 2072 6571 7565 7374  ession = request
-00000080: 732e 5365 7373 696f 6e28 290a 0a23 6661  s.Session()..#fa
-00000090: 6b65 2075 7365 7220 6167 656e 740a 7573  ke user agent.us
-000000a0: 6572 5f61 6765 6e74 203d 207b 2255 7365  er_agent = {"Use
-000000b0: 722d 4167 656e 7422 203a 2022 4d6f 7a69  r-Agent" : "Mozi
-000000c0: 6c6c 612f 352e 3020 2858 3131 3b20 4665  lla/5.0 (X11; Fe
-000000d0: 646f 7261 3b20 4c69 6e75 7820 7838 365f  dora; Linux x86_
-000000e0: 3634 2920 4170 706c 6557 6562 4b69 742f  64) AppleWebKit/
-000000f0: 3533 372e 3336 2028 4b48 544d 4c2c 206c  537.36 (KHTML, l
-00000100: 696b 6520 4765 636b 6f29 2043 6872 6f6d  ike Gecko) Chrom
-00000110: 652f 3130 372e 302e 302e 3020 5361 6661  e/107.0.0.0 Safa
-00000120: 7269 2f35 3337 2e33 3622 7d0a 0a23 696e  ri/537.36"}..#in
-00000130: 6372 6561 7365 6420 7365 6375 7269 7479  creased security
-00000140: 0a72 6571 7565 7374 732e 7061 636b 6167  .requests.packag
-00000150: 6573 2e75 726c 6c69 6233 2e64 6973 6162  es.urllib3.disab
-00000160: 6c65 5f77 6172 6e69 6e67 7328 290a 7265  le_warnings().re
-00000170: 7175 6573 7473 2e70 6163 6b61 6765 732e  quests.packages.
-00000180: 7572 6c6c 6962 332e 7574 696c 2e73 736c  urllib3.util.ssl
-00000190: 5f2e 4445 4641 554c 545f 4349 5048 4552  _.DEFAULT_CIPHER
-000001a0: 5320 2b3d 2022 3a48 4947 483a 2144 483a  S += ":HIGH:!DH:
-000001b0: 2161 4e55 4c4c 220a 0a23 696e 6372 6561  !aNULL"..#increa
-000001c0: 7365 6420 7365 6375 7269 7479 0a74 7279  sed security.try
-000001d0: 3a0a 2020 2020 7265 7175 6573 7473 2e70  :.    requests.p
-000001e0: 6163 6b61 6765 732e 7572 6c6c 6962 332e  ackages.urllib3.
-000001f0: 636f 6e74 7269 622e 7079 6f70 656e 7373  contrib.pyopenss
-00000200: 6c2e 7574 696c 2e73 736c 5f2e 4445 4641  l.util.ssl_.DEFA
-00000210: 554c 545f 4349 5048 4552 5320 2b3d 2022  ULT_CIPHERS += "
-00000220: 3a48 4947 483a 2144 483a 2161 4e55 4c4c  :HIGH:!DH:!aNULL
-00000230: 220a 0a65 7863 6570 7420 4174 7472 6962  "..except Attrib
-00000240: 7574 6545 7272 6f72 3a0a 2020 2020 7061  uteError:.    pa
-00000250: 7373 0a0a 2363 7261 776c 7320 6120 7765  ss..#crawls a we
-00000260: 6273 6974 6520 6c6f 6f6b 696e 6720 666f  bsite looking fo
-00000270: 7220 6c69 6e6b 730a 6465 6620 6c69 6e6b  r links.def link
-00000280: 5f73 6361 6e6e 6572 2875 726c 2c20 7365  _scanner(url, se
-00000290: 6375 7265 203d 2054 7275 652c 206d 795f  cure = True, my_
-000002a0: 6669 6c65 203d 2022 2022 293a 0a20 2020  file = " "):.   
-000002b0: 2069 6620 7365 6375 7265 203d 3d20 5472   if secure == Tr
-000002c0: 7565 3a0a 2020 2020 2020 2020 6d79 5f73  ue:.        my_s
-000002d0: 6563 7572 6520 3d20 2268 7474 7073 3a2f  ecure = "https:/
-000002e0: 2f22 0a0a 2020 2020 6966 2073 6563 7572  /"..    if secur
-000002f0: 6520 3d3d 2046 616c 7365 3a0a 2020 2020  e == False:.    
-00000300: 2020 2020 6d79 5f73 6563 7572 6520 3d20      my_secure = 
-00000310: 2268 7474 703a 2f2f 220a 0a20 2020 206d  "http://"..    m
-00000320: 795f 7572 6c20 3d20 6d79 5f73 6563 7572  y_url = my_secur
-00000330: 6520 2b20 7572 6c0a 2020 2020 7472 6163  e + url.    trac
-00000340: 6b65 7220 3d20 300a 0a20 2020 2077 6562  ker = 0..    web
-00000350: 7369 7465 5f6c 6973 7420 3d20 5b5d 0a20  site_list = []. 
-00000360: 2020 2077 6562 7369 7465 5f6c 6973 742e     website_list.
-00000370: 6170 7065 6e64 286d 795f 7572 6c29 0a0a  append(my_url)..
-00000380: 2020 2020 636c 6561 7228 290a 0a20 2020      clear()..   
-00000390: 2077 6869 6c65 2054 7275 653a 0a20 2020   while True:.   
-000003a0: 2020 2020 206c 656e 6774 685f 636f 756e       length_coun
-000003b0: 7420 3d20 300a 0a20 2020 2020 2020 2077  t = 0..        w
-000003c0: 6562 7369 7465 5f6c 6973 7420 3d20 6c69  ebsite_list = li
-000003d0: 7374 2864 6963 742e 6672 6f6d 6b65 7973  st(dict.fromkeys
-000003e0: 2877 6562 7369 7465 5f6c 6973 7429 290a  (website_list)).
-000003f0: 2020 2020 2020 2020 0a20 2020 2020 2020          .       
-00000400: 2074 7279 3a0a 2020 2020 2020 2020 2020   try:.          
-00000410: 2020 6d79 5f66 696c 7465 7220 3d20 7265    my_filter = re
-00000420: 2e66 696e 6461 6c6c 2822 2868 7474 7073  .findall("(https
-00000430: 3a2f 2f7c 6874 7470 3a2f 2f29 282e 2b3f  ://|http://)(.+?
-00000440: 2f29 222c 2077 6562 7369 7465 5f6c 6973  /)", website_lis
-00000450: 745b 7472 6163 6b65 725d 290a 2020 2020  t[tracker]).    
-00000460: 2020 2020 2020 2020 6669 6e64 5f6d 7920          find_my 
-00000470: 3d20 7265 2e73 6561 7263 6828 7572 6c2c  = re.search(url,
-00000480: 2073 7472 286d 795f 6669 6c74 6572 2929   str(my_filter))
-00000490: 0a0a 2020 2020 2020 2020 2020 2020 6966  ..            if
-000004a0: 2066 696e 645f 6d79 206f 7220 7765 6273   find_my or webs
-000004b0: 6974 655f 6c69 7374 5b74 7261 636b 6572  ite_list[tracker
-000004c0: 5d20 3d3d 206d 795f 7572 6c3a 0a20 2020  ] == my_url:.   
-000004d0: 2020 2020 2020 2020 2020 2020 2073 7472               str
-000004e0: 6561 6d5f 626f 6f6c 6561 6e20 3d20 7765  eam_boolean = we
-000004f0: 625f 7365 7373 696f 6e2e 6765 7428 7765  b_session.get(we
-00000500: 6273 6974 655f 6c69 7374 5b74 7261 636b  bsite_list[track
-00000510: 6572 5d2c 2076 6572 6966 7920 3d20 4661  er], verify = Fa
-00000520: 6c73 652c 2068 6561 6465 7273 203d 2075  lse, headers = u
-00000530: 7365 725f 6167 656e 742c 2074 696d 656f  ser_agent, timeo
-00000540: 7574 203d 2028 352c 2033 3029 2c20 7374  ut = (5, 30), st
-00000550: 7265 616d 203d 2054 7275 6529 0a0a 2020  ream = True)..  
-00000560: 2020 2020 2020 2020 2020 2020 2020 666f                fo
-00000570: 7220 6920 696e 2073 7472 6561 6d5f 626f  r i in stream_bo
-00000580: 6f6c 6561 6e2e 6974 6572 5f6c 696e 6573  olean.iter_lines
-00000590: 2829 3a0a 2020 2020 2020 2020 2020 2020  ():.            
-000005a0: 2020 2020 2020 2020 6c65 6e67 7468 5f63          length_c
-000005b0: 6f75 6e74 202b 3d20 6c65 6e28 6929 0a0a  ount += len(i)..
-000005c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000005d0: 6966 206c 656e 6774 685f 636f 756e 7420  if length_count 
-000005e0: 3e20 3130 3030 3030 3030 303a 0a20 2020  > 100000000:.   
-000005f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000600: 2070 7269 6e74 2872 6564 202b 2022 746f   print(red + "to
-00000610: 6f20 6c6f 6e67 2220 2b20 223a 2022 202b  o long" + ": " +
-00000620: 2073 7472 2877 6562 7369 7465 5f6c 6973   str(website_lis
-00000630: 745b 7472 6163 6b65 725d 2929 0a20 2020  t[tracker])).   
-00000640: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000650: 2077 6562 7369 7465 5f6c 6973 742e 706f   website_list.po
-00000660: 7028 7472 6163 6b65 7229 0a0a 2020 2020  p(tracker)..    
-00000670: 2020 2020 2020 2020 2020 2020 6966 206c              if l
-00000680: 656e 6774 685f 636f 756e 7420 3c3d 2031  ength_count <= 1
-00000690: 3030 3030 3030 3030 3a0a 2020 2020 2020  00000000:.      
-000006a0: 2020 2020 2020 2020 2020 2020 2020 7374                st
-000006b0: 6174 7573 203d 2077 6562 5f73 6573 7369  atus = web_sessi
-000006c0: 6f6e 2e67 6574 2877 6562 7369 7465 5f6c  on.get(website_l
-000006d0: 6973 745b 7472 6163 6b65 725d 2c20 7665  ist[tracker], ve
-000006e0: 7269 6679 203d 2046 616c 7365 2c20 6865  rify = False, he
-000006f0: 6164 6572 7320 3d20 7573 6572 5f61 6765  aders = user_age
-00000700: 6e74 2c20 7469 6d65 6f75 7420 3d20 2835  nt, timeout = (5
-00000710: 2c20 3330 2929 2e73 7461 7475 735f 636f  , 30)).status_co
-00000720: 6465 0a0a 2020 2020 2020 2020 2020 2020  de..            
-00000730: 2020 2020 2020 2020 6966 2073 7461 7475          if statu
-00000740: 7320 3d3d 2032 3030 3a0a 2020 2020 2020  s == 200:.      
-00000750: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000760: 2020 7072 696e 7428 7265 6420 2b20 7765    print(red + we
-00000770: 6273 6974 655f 6c69 7374 5b74 7261 636b  bsite_list[track
-00000780: 6572 5d29 0a20 2020 2020 2020 2020 2020  er]).           
-00000790: 2020 2020 2020 2020 2020 2020 206d 795f               my_
-000007a0: 7265 7175 6573 7420 3d20 7765 625f 7365  request = web_se
-000007b0: 7373 696f 6e2e 6765 7428 7765 6273 6974  ssion.get(websit
-000007c0: 655f 6c69 7374 5b74 7261 636b 6572 5d2c  e_list[tracker],
-000007d0: 2076 6572 6966 7920 3d20 4661 6c73 652c   verify = False,
-000007e0: 2068 6561 6465 7273 203d 2075 7365 725f   headers = user_
-000007f0: 6167 656e 742c 2074 696d 656f 7574 203d  agent, timeout =
-00000800: 2028 352c 2033 3029 292e 7465 7874 0a0a   (5, 30)).text..
-00000810: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000820: 2020 2020 2020 2020 6966 206c 656e 286d          if len(m
-00000830: 795f 7265 7175 6573 7429 203c 3d20 3130  y_request) <= 10
-00000840: 3030 3030 3030 303a 0a20 2020 2020 2020  0000000:.       
-00000850: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000860: 2020 2020 2074 7261 636b 6572 202b 3d20       tracker += 
-00000870: 310a 0a20 2020 2020 2020 2020 2020 2020  1..             
-00000880: 2020 2020 2020 2020 2020 2020 2020 2023                 #
-00000890: 7572 6c73 0a20 2020 2020 2020 2020 2020  urls.           
-000008a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000008b0: 2077 6562 7369 7465 203d 2072 652e 6669   website = re.fi
-000008c0: 6e64 616c 6c28 2268 7474 703a 2f2f 7c68  ndall("http://|h
-000008d0: 7474 7073 3a2f 2f5c 532b 222c 206d 795f  ttps://\S+", my_
-000008e0: 7265 7175 6573 7429 0a20 2020 2020 2020  request).       
-000008f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000900: 2020 2020 2077 6562 7369 7465 203d 206c       website = l
-00000910: 6973 7428 6469 6374 2e66 726f 6d6b 6579  ist(dict.fromkey
-00000920: 7328 7765 6273 6974 6529 290a 0a20 2020  s(website))..   
-00000930: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000940: 2020 2020 2020 2020 2066 6f72 2069 2069           for i i
-00000950: 6e20 7765 6273 6974 653a 0a20 2020 2020  n website:.     
-00000960: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000970: 2020 2020 2020 2020 2020 2074 7279 3a0a             try:.
-00000980: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000040: 225c 3033 335b 313b 3331 6d22 0a0a 746f  "\033[1;31m"..to
+00000050: 725f 7072 6f78 7920 3d20 7b22 6874 7470  r_proxy = {"http
+00000060: 7322 3a20 2273 6f63 6b73 3568 3a2f 2f6c  s": "socks5h://l
+00000070: 6f63 616c 686f 7374 3a39 3035 3022 2c20  ocalhost:9050", 
+00000080: 2268 7474 7022 3a20 2273 6f63 6b73 3568  "http": "socks5h
+00000090: 3a2f 2f6c 6f63 616c 686f 7374 3a39 3035  ://localhost:905
+000000a0: 3022 7d0a 0a23 6372 6561 7465 2068 746d  0"}..#create htm
+000000b0: 6c20 7365 7373 696f 6e73 206f 626a 6563  l sessions objec
+000000c0: 740a 7765 625f 7365 7373 696f 6e20 3d20  t.web_session = 
+000000d0: 7265 7175 6573 7473 2e53 6573 7369 6f6e  requests.Session
+000000e0: 2829 0a0a 2366 616b 6520 7573 6572 2061  ()..#fake user a
+000000f0: 6765 6e74 0a75 7365 725f 6167 656e 7420  gent.user_agent 
+00000100: 3d20 7b22 5573 6572 2d41 6765 6e74 2220  = {"User-Agent" 
+00000110: 3a20 224d 6f7a 696c 6c61 2f35 2e30 2028  : "Mozilla/5.0 (
+00000120: 5831 313b 2046 6564 6f72 613b 204c 696e  X11; Fedora; Lin
+00000130: 7578 2078 3836 5f36 3429 2041 7070 6c65  ux x86_64) Apple
+00000140: 5765 624b 6974 2f35 3337 2e33 3620 284b  WebKit/537.36 (K
+00000150: 4854 4d4c 2c20 6c69 6b65 2047 6563 6b6f  HTML, like Gecko
+00000160: 2920 4368 726f 6d65 2f31 3037 2e30 2e30  ) Chrome/107.0.0
+00000170: 2e30 2053 6166 6172 692f 3533 372e 3336  .0 Safari/537.36
+00000180: 227d 0a0a 2369 6e63 7265 6173 6564 2073  "}..#increased s
+00000190: 6563 7572 6974 790a 7265 7175 6573 7473  ecurity.requests
+000001a0: 2e70 6163 6b61 6765 732e 7572 6c6c 6962  .packages.urllib
+000001b0: 332e 6469 7361 626c 655f 7761 726e 696e  3.disable_warnin
+000001c0: 6773 2829 0a72 6571 7565 7374 732e 7061  gs().requests.pa
+000001d0: 636b 6167 6573 2e75 726c 6c69 6233 2e75  ckages.urllib3.u
+000001e0: 7469 6c2e 7373 6c5f 2e44 4546 4155 4c54  til.ssl_.DEFAULT
+000001f0: 5f43 4950 4845 5253 202b 3d20 223a 4849  _CIPHERS += ":HI
+00000200: 4748 3a21 4448 3a21 614e 554c 4c22 0a0a  GH:!DH:!aNULL"..
+00000210: 2369 6e63 7265 6173 6564 2073 6563 7572  #increased secur
+00000220: 6974 790a 7472 793a 0a20 2020 2072 6571  ity.try:.    req
+00000230: 7565 7374 732e 7061 636b 6167 6573 2e75  uests.packages.u
+00000240: 726c 6c69 6233 2e63 6f6e 7472 6962 2e70  rllib3.contrib.p
+00000250: 796f 7065 6e73 736c 2e75 7469 6c2e 7373  yopenssl.util.ss
+00000260: 6c5f 2e44 4546 4155 4c54 5f43 4950 4845  l_.DEFAULT_CIPHE
+00000270: 5253 202b 3d20 223a 4849 4748 3a21 4448  RS += ":HIGH:!DH
+00000280: 3a21 614e 554c 4c22 0a0a 6578 6365 7074  :!aNULL"..except
+00000290: 2041 7474 7269 6275 7465 4572 726f 723a   AttributeError:
+000002a0: 0a20 2020 2070 6173 730a 0a23 6372 6177  .    pass..#craw
+000002b0: 6c73 2061 2077 6562 7369 7465 206c 6f6f  ls a website loo
+000002c0: 6b69 6e67 2066 6f72 206c 696e 6b73 0a64  king for links.d
+000002d0: 6566 206c 696e 6b5f 7363 616e 6e65 7228  ef link_scanner(
+000002e0: 7572 6c2c 2073 6563 7572 6520 3d20 5472  url, secure = Tr
+000002f0: 7565 2c20 746f 7220 3d20 4661 6c73 652c  ue, tor = False,
+00000300: 206d 795f 6669 6c65 203d 2022 2022 293a   my_file = " "):
+00000310: 0a20 2020 2069 6620 7365 6375 7265 203d  .    if secure =
+00000320: 3d20 5472 7565 3a0a 2020 2020 2020 2020  = True:.        
+00000330: 6d79 5f73 6563 7572 6520 3d20 2268 7474  my_secure = "htt
+00000340: 7073 3a2f 2f22 0a0a 2020 2020 6966 2073  ps://"..    if s
+00000350: 6563 7572 6520 3d3d 2046 616c 7365 3a0a  ecure == False:.
+00000360: 2020 2020 2020 2020 6d79 5f73 6563 7572          my_secur
+00000370: 6520 3d20 2268 7474 703a 2f2f 220a 0a20  e = "http://".. 
+00000380: 2020 206d 795f 7572 6c20 3d20 6d79 5f73     my_url = my_s
+00000390: 6563 7572 6520 2b20 7572 6c0a 2020 2020  ecure + url.    
+000003a0: 7472 6163 6b65 7220 3d20 300a 0a20 2020  tracker = 0..   
+000003b0: 2077 6562 7369 7465 5f6c 6973 7420 3d20   website_list = 
+000003c0: 5b5d 0a20 2020 2077 6562 7369 7465 5f6c  [].    website_l
+000003d0: 6973 742e 6170 7065 6e64 286d 795f 7572  ist.append(my_ur
+000003e0: 6c29 0a0a 2020 2020 636c 6561 7228 290a  l)..    clear().
+000003f0: 0a20 2020 2077 6869 6c65 2054 7275 653a  .    while True:
+00000400: 0a20 2020 2020 2020 206c 656e 6774 685f  .        length_
+00000410: 636f 756e 7420 3d20 300a 0a20 2020 2020  count = 0..     
+00000420: 2020 2077 6562 7369 7465 5f6c 6973 7420     website_list 
+00000430: 3d20 6c69 7374 2864 6963 742e 6672 6f6d  = list(dict.from
+00000440: 6b65 7973 2877 6562 7369 7465 5f6c 6973  keys(website_lis
+00000450: 7429 290a 2020 2020 2020 2020 0a20 2020  t)).        .   
+00000460: 2020 2020 2074 7279 3a0a 2020 2020 2020       try:.      
+00000470: 2020 2020 2020 6d79 5f66 696c 7465 7220        my_filter 
+00000480: 3d20 7265 2e66 696e 6461 6c6c 2822 2868  = re.findall("(h
+00000490: 7474 7073 3a2f 2f7c 6874 7470 3a2f 2f29  ttps://|http://)
+000004a0: 282e 2b3f 2f29 222c 2077 6562 7369 7465  (.+?/)", website
+000004b0: 5f6c 6973 745b 7472 6163 6b65 725d 290a  _list[tracker]).
+000004c0: 2020 2020 2020 2020 2020 2020 6669 6e64              find
+000004d0: 5f6d 7920 3d20 7265 2e73 6561 7263 6828  _my = re.search(
+000004e0: 7572 6c2c 2073 7472 286d 795f 6669 6c74  url, str(my_filt
+000004f0: 6572 2929 0a0a 2020 2020 2020 2020 2020  er))..          
+00000500: 2020 6966 2066 696e 645f 6d79 206f 7220    if find_my or 
+00000510: 7765 6273 6974 655f 6c69 7374 5b74 7261  website_list[tra
+00000520: 636b 6572 5d20 3d3d 206d 795f 7572 6c3a  cker] == my_url:
+00000530: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00000540: 2069 6620 746f 7220 3d3d 2054 7275 653a   if tor == True:
+00000550: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00000560: 2020 2020 2073 7472 6561 6d5f 626f 6f6c       stream_bool
+00000570: 6561 6e20 3d20 7765 625f 7365 7373 696f  ean = web_sessio
+00000580: 6e2e 6765 7428 7765 6273 6974 655f 6c69  n.get(website_li
+00000590: 7374 5b74 7261 636b 6572 5d2c 2076 6572  st[tracker], ver
+000005a0: 6966 7920 3d20 4661 6c73 652c 2068 6561  ify = False, hea
+000005b0: 6465 7273 203d 2075 7365 725f 6167 656e  ders = user_agen
+000005c0: 742c 2070 726f 7869 6573 203d 2074 6f72  t, proxies = tor
+000005d0: 5f70 726f 7879 2c20 7469 6d65 6f75 7420  _proxy, timeout 
+000005e0: 3d20 2835 2c20 3330 292c 2073 7472 6561  = (5, 30), strea
+000005f0: 6d20 3d20 5472 7565 290a 0a20 2020 2020  m = True)..     
+00000600: 2020 2020 2020 2020 2020 2065 6c73 653a             else:
+00000610: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00000620: 2020 2020 2073 7472 6561 6d5f 626f 6f6c       stream_bool
+00000630: 6561 6e20 3d20 7765 625f 7365 7373 696f  ean = web_sessio
+00000640: 6e2e 6765 7428 7765 6273 6974 655f 6c69  n.get(website_li
+00000650: 7374 5b74 7261 636b 6572 5d2c 2076 6572  st[tracker], ver
+00000660: 6966 7920 3d20 4661 6c73 652c 2068 6561  ify = False, hea
+00000670: 6465 7273 203d 2075 7365 725f 6167 656e  ders = user_agen
+00000680: 742c 2074 696d 656f 7574 203d 2028 352c  t, timeout = (5,
+00000690: 2033 3029 2c20 7374 7265 616d 203d 2054   30), stream = T
+000006a0: 7275 6529 0a0a 2020 2020 2020 2020 2020  rue)..          
+000006b0: 2020 2020 2020 666f 7220 6920 696e 2073        for i in s
+000006c0: 7472 6561 6d5f 626f 6f6c 6561 6e2e 6974  tream_boolean.it
+000006d0: 6572 5f6c 696e 6573 2829 3a0a 2020 2020  er_lines():.    
+000006e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000006f0: 6c65 6e67 7468 5f63 6f75 6e74 202b 3d20  length_count += 
+00000700: 6c65 6e28 6929 0a0a 2020 2020 2020 2020  len(i)..        
+00000710: 2020 2020 2020 2020 6966 206c 656e 6774          if lengt
+00000720: 685f 636f 756e 7420 3e20 3130 3030 3030  h_count > 100000
+00000730: 3030 303a 0a20 2020 2020 2020 2020 2020  000:.           
+00000740: 2020 2020 2020 2020 2070 7269 6e74 2872           print(r
+00000750: 6564 202b 2022 746f 6f20 6c6f 6e67 2220  ed + "too long" 
+00000760: 2b20 223a 2022 202b 2073 7472 2877 6562  + ": " + str(web
+00000770: 7369 7465 5f6c 6973 745b 7472 6163 6b65  site_list[tracke
+00000780: 725d 2929 0a20 2020 2020 2020 2020 2020  r])).           
+00000790: 2020 2020 2020 2020 2077 6562 7369 7465           website
+000007a0: 5f6c 6973 742e 706f 7028 7472 6163 6b65  _list.pop(tracke
+000007b0: 7229 0a0a 2020 2020 2020 2020 2020 2020  r)..            
+000007c0: 2020 2020 6966 206c 656e 6774 685f 636f      if length_co
+000007d0: 756e 7420 3c3d 2031 3030 3030 3030 3030  unt <= 100000000
+000007e0: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+000007f0: 2020 2020 2020 6966 2074 6f72 203d 3d20        if tor == 
+00000800: 5472 7565 3a0a 2020 2020 2020 2020 2020  True:.          
+00000810: 2020 2020 2020 2020 2020 2020 2020 7374                st
+00000820: 6174 7573 203d 2077 6562 5f73 6573 7369  atus = web_sessi
+00000830: 6f6e 2e67 6574 2877 6562 7369 7465 5f6c  on.get(website_l
+00000840: 6973 745b 7472 6163 6b65 725d 2c20 7665  ist[tracker], ve
+00000850: 7269 6679 203d 2046 616c 7365 2c20 6865  rify = False, he
+00000860: 6164 6572 7320 3d20 7573 6572 5f61 6765  aders = user_age
+00000870: 6e74 2c20 7072 6f78 6965 7320 3d20 746f  nt, proxies = to
+00000880: 725f 7072 6f78 792c 2074 696d 656f 7574  r_proxy, timeout
+00000890: 203d 2028 352c 2033 3029 292e 7374 6174   = (5, 30)).stat
+000008a0: 7573 5f63 6f64 650a 0a20 2020 2020 2020  us_code..       
+000008b0: 2020 2020 2020 2020 2020 2020 2065 6c73               els
+000008c0: 653a 0a20 2020 2020 2020 2020 2020 2020  e:.             
+000008d0: 2020 2020 2020 2020 2020 2073 7461 7475             statu
+000008e0: 7320 3d20 7765 625f 7365 7373 696f 6e2e  s = web_session.
+000008f0: 6765 7428 7765 6273 6974 655f 6c69 7374  get(website_list
+00000900: 5b74 7261 636b 6572 5d2c 2076 6572 6966  [tracker], verif
+00000910: 7920 3d20 4661 6c73 652c 2068 6561 6465  y = False, heade
+00000920: 7273 203d 2075 7365 725f 6167 656e 742c  rs = user_agent,
+00000930: 2070 726f 7869 6573 203d 2074 6f72 5f70   proxies = tor_p
+00000940: 726f 7879 2c20 7469 6d65 6f75 7420 3d20  roxy, timeout = 
+00000950: 2835 2c20 3330 2929 2e73 7461 7475 735f  (5, 30)).status_
+00000960: 636f 6465 0a0a 2020 2020 2020 2020 2020  code..          
+00000970: 2020 2020 2020 2020 2020 6966 2073 7461            if sta
+00000980: 7475 7320 3d3d 2032 3030 3a0a 2020 2020  tus == 200:.    
 00000990: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000009a0: 2020 2020 7265 7375 6c74 203d 2072 652e      result = re.
-000009b0: 7370 6c69 7428 225b 255c 285c 293c 3e5c  split("[%\(\)<>\
-000009c0: 5b5c 5d2c 5c7b 5c7d 3bef bfbd 047c 5d22  [\],\{\};....|]"
-000009d0: 2c20 6929 0a20 2020 2020 2020 2020 2020  , i).           
-000009e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000009f0: 2020 2020 2020 2020 2072 6573 756c 7420           result 
-00000a00: 3d20 7265 7375 6c74 5b30 5d0a 2020 2020  = result[0].    
-00000a10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a30: 7265 7375 6c74 203d 2072 652e 7375 6228  result = re.sub(
-00000a40: 225b 5c22 5c27 5d22 2c20 2222 2c20 7265  "[\"\']", "", re
-00000a50: 7375 6c74 290a 0a20 2020 2020 2020 2020  sult)..         
-00000a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a70: 2020 2020 2020 2065 7863 6570 743a 0a20         except:. 
+000009a0: 2020 2020 7072 696e 7428 7265 6420 2b20      print(red + 
+000009b0: 7765 6273 6974 655f 6c69 7374 5b74 7261  website_list[tra
+000009c0: 636b 6572 5d29 0a20 2020 2020 2020 2020  cker]).         
+000009d0: 2020 2020 2020 2020 2020 2020 2020 2069                 i
+000009e0: 6620 746f 7220 3d3d 2054 7275 653a 0a20  f tor == True:. 
+000009f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000a00: 2020 2020 2020 2020 2020 206d 795f 7265             my_re
+00000a10: 7175 6573 7420 3d20 7765 625f 7365 7373  quest = web_sess
+00000a20: 696f 6e2e 6765 7428 7765 6273 6974 655f  ion.get(website_
+00000a30: 6c69 7374 5b74 7261 636b 6572 5d2c 2076  list[tracker], v
+00000a40: 6572 6966 7920 3d20 4661 6c73 652c 2068  erify = False, h
+00000a50: 6561 6465 7273 203d 2075 7365 725f 6167  eaders = user_ag
+00000a60: 656e 742c 2074 696d 656f 7574 203d 2028  ent, timeout = (
+00000a70: 352c 2033 3029 292e 7465 7874 0a0a 2020  5, 30)).text..  
 00000a80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000a90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000aa0: 2020 2072 6573 756c 7420 3d20 690a 2020     result = i.  
-00000ab0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000ac0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000ad0: 2020 0a20 2020 2020 2020 2020 2020 2020    .             
-00000ae0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000af0: 2020 2069 6620 7572 6c20 696e 2069 3a0a     if url in i:.
-00000b00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000b10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000b20: 2020 2020 7765 6273 6974 655f 6c69 7374      website_list
-00000b30: 2e61 7070 656e 6428 7265 2e73 7562 2822  .append(re.sub("
-00000b40: 5b5c 5c5c 225c 275d 222c 2022 222c 2072  [\\\"\']", "", r
-00000b50: 6573 756c 7429 290a 0a20 2020 2020 2020  esult))..       
-00000b60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000b70: 2020 2020 2023 6872 6566 0a20 2020 2020       #href.     
-00000b80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000b90: 2020 2020 2020 2068 7265 6620 3d20 7265         href = re
-00000ba0: 2e73 7562 2822 2022 2c20 2222 2c20 6d79  .sub(" ", "", my
-00000bb0: 5f72 6571 7565 7374 290a 2020 2020 2020  _request).      
-00000bc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000bd0: 2020 2020 2020 6872 6566 203d 2072 652e        href = re.
-00000be0: 6669 6e64 616c 6c28 2268 7265 665c 732a  findall("href\s*
-00000bf0: 3d5c 732a 5b5c 225c 275d 5c53 2b3f 5b5c  =\s*[\"\']\S+?[\
-00000c00: 275c 225d 222c 2068 7265 6629 0a20 2020  '\"]", href).   
+00000a90: 2020 2020 2020 656c 7365 3a0a 2020 2020        else:.    
+00000aa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000ab0: 2020 2020 2020 2020 6d79 5f72 6571 7565          my_reque
+00000ac0: 7374 203d 2077 6562 5f73 6573 7369 6f6e  st = web_session
+00000ad0: 2e67 6574 2877 6562 7369 7465 5f6c 6973  .get(website_lis
+00000ae0: 745b 7472 6163 6b65 725d 2c20 7665 7269  t[tracker], veri
+00000af0: 6679 203d 2046 616c 7365 2c20 6865 6164  fy = False, head
+00000b00: 6572 7320 3d20 7573 6572 5f61 6765 6e74  ers = user_agent
+00000b10: 2c20 7469 6d65 6f75 7420 3d20 2835 2c20  , timeout = (5, 
+00000b20: 3330 2929 2e74 6578 740a 0a20 2020 2020  30)).text..     
+00000b30: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000b40: 2020 2069 6620 6c65 6e28 6d79 5f72 6571     if len(my_req
+00000b50: 7565 7374 2920 3c3d 2031 3030 3030 3030  uest) <= 1000000
+00000b60: 3030 3a0a 2020 2020 2020 2020 2020 2020  00:.            
+00000b70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000b80: 7472 6163 6b65 7220 2b3d 2031 0a0a 2020  tracker += 1..  
+00000b90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000ba0: 2020 2020 2020 2020 2020 2375 726c 730a            #urls.
+00000bb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000bc0: 2020 2020 2020 2020 2020 2020 7765 6273              webs
+00000bd0: 6974 6520 3d20 7265 2e66 696e 6461 6c6c  ite = re.findall
+00000be0: 2822 6874 7470 3a2f 2f7c 6874 7470 733a  ("http://|https:
+00000bf0: 2f2f 5c53 2b22 2c20 6d79 5f72 6571 7565  //\S+", my_reque
+00000c00: 7374 290a 2020 2020 2020 2020 2020 2020  st).            
 00000c10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000c20: 2020 2020 2020 2020 2068 7265 6620 3d20           href = 
-00000c30: 6c69 7374 2864 6963 742e 6672 6f6d 6b65  list(dict.fromke
-00000c40: 7973 2868 7265 6629 290a 2020 2020 2020  ys(href)).      
+00000c20: 7765 6273 6974 6520 3d20 6c69 7374 2864  website = list(d
+00000c30: 6963 742e 6672 6f6d 6b65 7973 2877 6562  ict.fromkeys(web
+00000c40: 7369 7465 2929 0a0a 2020 2020 2020 2020  site))..        
 00000c50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000c60: 2020 2020 2020 666f 7220 6920 696e 2068        for i in h
-00000c70: 7265 663a 0a20 2020 2020 2020 2020 2020  ref:.           
+00000c60: 2020 2020 666f 7220 6920 696e 2077 6562      for i in web
+00000c70: 7369 7465 3a0a 2020 2020 2020 2020 2020  site:.          
 00000c80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000c90: 2020 2020 2074 7279 3a0a 2020 2020 2020       try:.      
+00000c90: 2020 2020 2020 7472 793a 0a20 2020 2020        try:.     
 00000ca0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000cb0: 2020 2020 2020 2020 2020 2020 2020 6920                i 
-00000cc0: 3d20 692e 636c 6561 6e28 2220 222c 2022  = i.clean(" ", "
-00000cd0: 2229 0a20 2020 2020 2020 2020 2020 2020  ").             
-00000ce0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000cf0: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
-00000d00: 7265 2e73 706c 6974 2822 5b25 5c28 5c29  re.split("[%\(\)
-00000d10: 3c3e 5c5b 5c5d 2c5c 7b5c 7d3b efbf bd04  <>\[\],\{\};....
-00000d20: 7c5d 222c 2069 290a 2020 2020 2020 2020  |]", i).        
+00000cb0: 2020 2020 2020 2020 2020 2020 2020 2072                 r
+00000cc0: 6573 756c 7420 3d20 7265 2e73 706c 6974  esult = re.split
+00000cd0: 2822 5b25 5c28 5c29 3c3e 5c5b 5c5d 2c5c  ("[%\(\)<>\[\],\
+00000ce0: 7b5c 7d3b efbf bd04 7c5d 222c 2069 290a  {\};....|]", i).
+00000cf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000d00: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000d10: 2020 2020 7265 7375 6c74 203d 2072 6573      result = res
+00000d20: 756c 745b 305d 0a20 2020 2020 2020 2020  ult[0].         
 00000d30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000d40: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-00000d50: 6c74 203d 2072 6573 756c 745b 305d 0a0a  lt = result[0]..
-00000d60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000d70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000d80: 6578 6365 7074 3a0a 2020 2020 2020 2020  except:.        
-00000d90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000da0: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-00000db0: 6c74 203d 2069 0a20 2020 2020 2020 2020  lt = i.         
-00000dc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000dd0: 2020 2020 2020 200a 2020 2020 2020 2020         .        
-00000de0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000df0: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-00000e00: 2072 652e 7375 6228 225b 5c5c 5c22 5c27   re.sub("[\\\"\'
-00000e10: 3b3d 5c73 5d7c 6872 6566 222c 2022 222c  ;=\s]|href", "",
-00000e20: 2069 290a 0a20 2020 2020 2020 2020 2020   i)..           
-00000e30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000e40: 2020 2020 2069 6620 7265 7375 6c74 2e73       if result.s
-00000e50: 7461 7274 7377 6974 6828 2268 7474 7022  tartswith("http"
-00000e60: 293a 0a20 2020 2020 2020 2020 2020 2020  ):.             
-00000e70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000e80: 2020 2020 2020 2069 6620 7572 6c20 696e         if url in
-00000e90: 2072 6573 756c 743a 0a20 2020 2020 2020   result:.       
+00000d40: 2020 2020 2020 2020 2020 2072 6573 756c             resul
+00000d50: 7420 3d20 7265 2e73 7562 2822 5b5c 225c  t = re.sub("[\"\
+00000d60: 275d 222c 2022 222c 2072 6573 756c 7429  ']", "", result)
+00000d70: 0a0a 2020 2020 2020 2020 2020 2020 2020  ..              
+00000d80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000d90: 2020 6578 6365 7074 3a0a 2020 2020 2020    except:.      
+00000da0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000db0: 2020 2020 2020 2020 2020 2020 2020 7265                re
+00000dc0: 7375 6c74 203d 2069 0a20 2020 2020 2020  sult = i.       
+00000dd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000de0: 2020 2020 2020 2020 2020 2020 200a 2020               .  
+00000df0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000e00: 2020 2020 2020 2020 2020 2020 2020 6966                if
+00000e10: 2075 726c 2069 6e20 693a 0a20 2020 2020   url in i:.     
+00000e20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000e30: 2020 2020 2020 2020 2020 2020 2020 2077                 w
+00000e40: 6562 7369 7465 5f6c 6973 742e 6170 7065  ebsite_list.appe
+00000e50: 6e64 2872 652e 7375 6228 225b 5c5c 5c22  nd(re.sub("[\\\"
+00000e60: 5c27 5d22 2c20 2222 2c20 7265 7375 6c74  \']", "", result
+00000e70: 2929 0a0a 2020 2020 2020 2020 2020 2020  ))..            
+00000e80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000e90: 2368 7265 660a 2020 2020 2020 2020 2020  #href.          
 00000ea0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000eb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000ec0: 2077 6562 7369 7465 5f6c 6973 742e 6170   website_list.ap
-00000ed0: 7065 6e64 2872 6573 756c 7429 0a0a 2020  pend(result)..  
+00000eb0: 2020 6872 6566 203d 2072 652e 7375 6228    href = re.sub(
+00000ec0: 2220 222c 2022 222c 206d 795f 7265 7175  " ", "", my_requ
+00000ed0: 6573 7429 0a20 2020 2020 2020 2020 2020  est).           
 00000ee0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000ef0: 2020 2020 2020 2020 2020 2020 2020 6966                if
-00000f00: 2072 6573 756c 742e 7374 6172 7473 7769   result.startswi
-00000f10: 7468 2822 6874 7470 2229 203d 3d20 4661  th("http") == Fa
-00000f20: 6c73 6520 616e 6420 7265 7375 6c74 5b30  lse and result[0
-00000f30: 5d20 213d 2022 2f22 3a0a 2020 2020 2020  ] != "/":.      
-00000f40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000f50: 2020 2020 2020 2020 2020 2020 2020 7265                re
-00000f60: 7375 6c74 203d 2072 652e 7375 6228 7572  sult = re.sub(ur
-00000f70: 6c2c 2022 222c 2072 6573 756c 7429 0a20  l, "", result). 
-00000f80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000ef0: 2068 7265 6620 3d20 7265 2e66 696e 6461   href = re.finda
+00000f00: 6c6c 2822 6872 6566 5c73 2a3d 5c73 2a5b  ll("href\s*=\s*[
+00000f10: 5c22 5c27 5d5c 532b 3f5b 5c27 5c22 5d22  \"\']\S+?[\'\"]"
+00000f20: 2c20 6872 6566 290a 2020 2020 2020 2020  , href).        
+00000f30: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000f40: 2020 2020 6872 6566 203d 206c 6973 7428      href = list(
+00000f50: 6469 6374 2e66 726f 6d6b 6579 7328 6872  dict.fromkeys(hr
+00000f60: 6566 2929 0a20 2020 2020 2020 2020 2020  ef)).           
+00000f70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000f80: 2066 6f72 2069 2069 6e20 6872 6566 3a0a   for i in href:.
 00000f90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000fa0: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
-00000fb0: 7562 2822 7777 7722 2c20 2222 2c20 7265  ub("www", "", re
-00000fc0: 7375 6c74 290a 2020 2020 2020 2020 2020  sult).          
-00000fd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000fe0: 2020 2020 2020 2020 2020 7765 6273 6974            websit
-00000ff0: 655f 6c69 7374 2e61 7070 656e 6428 6d79  e_list.append(my
-00001000: 5f75 726c 202b 2022 2f22 202b 2072 6573  _url + "/" + res
-00001010: 756c 7429 0a0a 2020 2020 2020 2020 2020  ult)..          
-00001020: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001030: 2020 2020 2020 6966 2072 6573 756c 742e        if result.
-00001040: 7374 6172 7473 7769 7468 2822 6874 7470  startswith("http
-00001050: 2229 203d 3d20 4661 6c73 6520 616e 6420  ") == False and 
-00001060: 7265 7375 6c74 5b30 5d20 3d3d 2022 2f22  result[0] == "/"
-00001070: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+00000fa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000fb0: 7472 793a 0a20 2020 2020 2020 2020 2020  try:.           
+00000fc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000fd0: 2020 2020 2020 2020 2069 203d 2069 2e63           i = i.c
+00000fe0: 6c65 616e 2822 2022 2c20 2222 290a 2020  lean(" ", "").  
+00000ff0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001000: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001010: 2020 7265 7375 6c74 203d 2072 652e 7370    result = re.sp
+00001020: 6c69 7428 225b 255c 285c 293c 3e5c 5b5c  lit("[%\(\)<>\[\
+00001030: 5d2c 5c7b 5c7d 3bef bfbd 047c 5d22 2c20  ],\{\};....|]", 
+00001040: 6929 0a20 2020 2020 2020 2020 2020 2020  i).             
+00001050: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001060: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
+00001070: 7265 7375 6c74 5b30 5d0a 0a20 2020 2020  result[0]..     
 00001080: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001090: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
-000010a0: 652e 7375 6228 7572 6c2c 2022 222c 2072  e.sub(url, "", r
-000010b0: 6573 756c 7429 0a20 2020 2020 2020 2020  esult).         
-000010c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000010d0: 2020 2020 2020 2020 2020 2072 6573 756c             resul
-000010e0: 7420 3d20 7265 2e73 7562 2822 7777 7722  t = re.sub("www"
-000010f0: 2c20 2222 2c20 7265 7375 6c74 290a 2020  , "", result).  
+00001090: 2020 2020 2020 2020 2020 2065 7863 6570             excep
+000010a0: 743a 0a20 2020 2020 2020 2020 2020 2020  t:.             
+000010b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000010c0: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
+000010d0: 690a 2020 2020 2020 2020 2020 2020 2020  i.              
+000010e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000010f0: 2020 0a20 2020 2020 2020 2020 2020 2020    .             
 00001100: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001110: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001120: 2020 7765 6273 6974 655f 6c69 7374 2e61    website_list.a
-00001130: 7070 656e 6428 6d79 5f75 726c 202b 2072  ppend(my_url + r
-00001140: 6573 756c 7429 0a0a 2020 2020 2020 2020  esult)..        
+00001110: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
+00001120: 7562 2822 5b5c 5c5c 225c 273b 3d5c 735d  ub("[\\\"\';=\s]
+00001130: 7c68 7265 6622 2c20 2222 2c20 6929 0a0a  |href", "", i)..
+00001140: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00001150: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001160: 2020 2020 2361 6374 696f 6e0a 2020 2020      #action.    
-00001170: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001180: 2020 2020 2020 2020 6163 7469 6f6e 203d          action =
-00001190: 2072 652e 7375 6228 2220 222c 2022 222c   re.sub(" ", "",
-000011a0: 206d 795f 7265 7175 6573 7429 0a20 2020   my_request).   
-000011b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000011c0: 2020 2020 2020 2020 2061 6374 696f 6e20           action 
-000011d0: 3d20 7265 2e66 696e 6461 6c6c 2822 6163  = re.findall("ac
-000011e0: 7469 6f6e 5c73 2a3d 5c73 2a5b 5c22 5c27  tion\s*=\s*[\"\'
-000011f0: 5d5c 532b 3f5b 5c27 5c22 5d22 2c20 6163  ]\S+?[\'\"]", ac
-00001200: 7469 6f6e 290a 2020 2020 2020 2020 2020  tion).          
-00001210: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001220: 2020 6163 7469 6f6e 203d 206c 6973 7428    action = list(
-00001230: 6469 6374 2e66 726f 6d6b 6579 7328 6163  dict.fromkeys(ac
-00001240: 7469 6f6e 2929 0a20 2020 2020 2020 2020  tion)).         
-00001250: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001260: 2020 200a 2020 2020 2020 2020 2020 2020     .            
-00001270: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001280: 666f 7220 6920 696e 2061 6374 696f 6e3a  for i in action:
-00001290: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001160: 6966 2072 6573 756c 742e 7374 6172 7473  if result.starts
+00001170: 7769 7468 2822 6874 7470 2229 3a0a 2020  with("http"):.  
+00001180: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001190: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000011a0: 2020 6966 2075 726c 2069 6e20 7265 7375    if url in resu
+000011b0: 6c74 3a0a 2020 2020 2020 2020 2020 2020  lt:.            
+000011c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000011d0: 2020 2020 2020 2020 2020 2020 7765 6273              webs
+000011e0: 6974 655f 6c69 7374 2e61 7070 656e 6428  ite_list.append(
+000011f0: 7265 7375 6c74 290a 0a20 2020 2020 2020  result)..       
+00001200: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001210: 2020 2020 2020 2020 2069 6620 7265 7375           if resu
+00001220: 6c74 2e73 7461 7274 7377 6974 6828 2268  lt.startswith("h
+00001230: 7474 7022 2920 3d3d 2046 616c 7365 2061  ttp") == False a
+00001240: 6e64 2072 6573 756c 745b 305d 2021 3d20  nd result[0] != 
+00001250: 222f 223a 0a20 2020 2020 2020 2020 2020  "/":.           
+00001260: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001270: 2020 2020 2020 2020 2072 6573 756c 7420           result 
+00001280: 3d20 7265 2e73 7562 2875 726c 2c20 2222  = re.sub(url, ""
+00001290: 2c20 7265 7375 6c74 290a 2020 2020 2020  , result).      
 000012a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012b0: 2074 7279 3a0a 2020 2020 2020 2020 2020   try:.          
-000012c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012d0: 2020 2020 2020 2020 2020 6920 3d20 692e            i = i.
-000012e0: 636c 6561 6e28 2220 222c 2022 2229 0a20  clean(" ", ""). 
+000012b0: 2020 2020 2020 2020 2020 2020 2020 7265                re
+000012c0: 7375 6c74 203d 2072 652e 7375 6228 2277  sult = re.sub("w
+000012d0: 7777 222c 2022 222c 2072 6573 756c 7429  ww", "", result)
+000012e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 000012f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001300: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001310: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
-00001320: 706c 6974 2822 5b25 5c28 5c29 3c3e 5c5b  plit("[%\(\)<>\[
-00001330: 5c5d 2c5c 7b5c 7d3b efbf bd04 7c5d 222c  \],\{\};....|]",
-00001340: 2069 290a 2020 2020 2020 2020 2020 2020   i).            
-00001350: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001360: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-00001370: 2072 6573 756c 745b 305d 0a0a 2020 2020   result[0]..    
-00001380: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001390: 2020 2020 2020 2020 2020 2020 6578 6365              exce
-000013a0: 7074 3a0a 2020 2020 2020 2020 2020 2020  pt:.            
-000013b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000013c0: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-000013d0: 2069 0a20 2020 2020 2020 2020 2020 2020   i.             
+00001300: 2020 2020 2077 6562 7369 7465 5f6c 6973       website_lis
+00001310: 742e 6170 7065 6e64 286d 795f 7572 6c20  t.append(my_url 
+00001320: 2b20 222f 2220 2b20 7265 7375 6c74 290a  + "/" + result).
+00001330: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001340: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001350: 2069 6620 7265 7375 6c74 2e73 7461 7274   if result.start
+00001360: 7377 6974 6828 2268 7474 7022 2920 3d3d  swith("http") ==
+00001370: 2046 616c 7365 2061 6e64 2072 6573 756c   False and resul
+00001380: 745b 305d 203d 3d20 222f 223a 0a20 2020  t[0] == "/":.   
+00001390: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000013a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000013b0: 2072 6573 756c 7420 3d20 7265 2e73 7562   result = re.sub
+000013c0: 2875 726c 2c20 2222 2c20 7265 7375 6c74  (url, "", result
+000013d0: 290a 2020 2020 2020 2020 2020 2020 2020  ).              
 000013e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000013f0: 2020 2020 2020 200a 2020 2020 2020 2020         .        
-00001400: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001410: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-00001420: 2072 652e 7375 6228 225b 5c5c 5c22 5c27   re.sub("[\\\"\'
-00001430: 3b3d 5c73 5d7c 6163 7469 6f6e 222c 2022  ;=\s]|action", "
-00001440: 222c 2069 290a 0a20 2020 2020 2020 2020  ", i)..         
-00001450: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001460: 2020 2020 2020 2069 6620 7265 7375 6c74         if result
-00001470: 2e73 7461 7274 7377 6974 6828 2268 7474  .startswith("htt
-00001480: 7022 293a 0a20 2020 2020 2020 2020 2020  p"):.           
+000013f0: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
+00001400: 652e 7375 6228 2277 7777 222c 2022 222c  e.sub("www", "",
+00001410: 2072 6573 756c 7429 0a20 2020 2020 2020   result).       
+00001420: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001430: 2020 2020 2020 2020 2020 2020 2077 6562               web
+00001440: 7369 7465 5f6c 6973 742e 6170 7065 6e64  site_list.append
+00001450: 286d 795f 7572 6c20 2b20 7265 7375 6c74  (my_url + result
+00001460: 290a 0a20 2020 2020 2020 2020 2020 2020  )..             
+00001470: 2020 2020 2020 2020 2020 2020 2020 2023                 #
+00001480: 6163 7469 6f6e 0a20 2020 2020 2020 2020  action.         
 00001490: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000014a0: 2020 2020 2020 2020 2069 6620 7572 6c20           if url 
-000014b0: 696e 2072 6573 756c 743a 0a20 2020 2020  in result:.     
-000014c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000014a0: 2020 2061 6374 696f 6e20 3d20 7265 2e73     action = re.s
+000014b0: 7562 2822 2022 2c20 2222 2c20 6d79 5f72  ub(" ", "", my_r
+000014c0: 6571 7565 7374 290a 2020 2020 2020 2020  equest).        
 000014d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000014e0: 2020 2077 6562 7369 7465 5f6c 6973 742e     website_list.
-000014f0: 6170 7065 6e64 2872 6573 756c 7429 0a0a  append(result)..
-00001500: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001510: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001520: 6966 2072 6573 756c 742e 7374 6172 7473  if result.starts
-00001530: 7769 7468 2822 6874 7470 2229 203d 3d20  with("http") == 
-00001540: 4661 6c73 6520 616e 6420 7265 7375 6c74  False and result
-00001550: 5b30 5d20 213d 2022 2f22 3a0a 2020 2020  [0] != "/":.    
-00001560: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001570: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001580: 7265 7375 6c74 203d 2072 652e 7375 6228  result = re.sub(
-00001590: 7572 6c2c 2022 222c 2072 6573 756c 7429  url, "", result)
-000015a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000014e0: 2020 2020 6163 7469 6f6e 203d 2072 652e      action = re.
+000014f0: 6669 6e64 616c 6c28 2261 6374 696f 6e5c  findall("action\
+00001500: 732a 3d5c 732a 5b5c 225c 275d 5c53 2b3f  s*=\s*[\"\']\S+?
+00001510: 5b5c 275c 225d 222c 2061 6374 696f 6e29  [\'\"]", action)
+00001520: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001530: 2020 2020 2020 2020 2020 2020 2061 6374               act
+00001540: 696f 6e20 3d20 6c69 7374 2864 6963 742e  ion = list(dict.
+00001550: 6672 6f6d 6b65 7973 2861 6374 696f 6e29  fromkeys(action)
+00001560: 290a 2020 2020 2020 2020 2020 2020 2020  ).              
+00001570: 2020 2020 2020 2020 2020 2020 2020 0a20                . 
+00001580: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001590: 2020 2020 2020 2020 2020 2066 6f72 2069             for i
+000015a0: 2069 6e20 6163 7469 6f6e 3a0a 2020 2020   in action:.    
 000015b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000015c0: 2020 2020 2072 6573 756c 7420 3d20 7265       result = re
-000015d0: 2e73 7562 2822 7777 7722 2c20 2222 2c20  .sub("www", "", 
-000015e0: 7265 7375 6c74 290a 2020 2020 2020 2020  result).        
-000015f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001600: 2020 2020 2020 2020 2020 2020 7765 6273              webs
-00001610: 6974 655f 6c69 7374 2e61 7070 656e 6428  ite_list.append(
-00001620: 6d79 5f75 726c 202b 2022 2f22 202b 2072  my_url + "/" + r
-00001630: 6573 756c 7429 0a0a 2020 2020 2020 2020  esult)..        
-00001640: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001650: 2020 2020 2020 2020 6966 2072 6573 756c          if resul
-00001660: 742e 7374 6172 7473 7769 7468 2822 6874  t.startswith("ht
-00001670: 7470 2229 203d 3d20 4661 6c73 6520 616e  tp") == False an
-00001680: 6420 7265 7375 6c74 5b30 5d20 3d3d 2022  d result[0] == "
-00001690: 2f22 3a0a 2020 2020 2020 2020 2020 2020  /":.            
+000015c0: 2020 2020 2020 2020 2020 2020 7472 793a              try:
+000015d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000015e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000015f0: 2020 2020 2069 203d 2069 2e63 6c65 616e       i = i.clean
+00001600: 2822 2022 2c20 2222 290a 2020 2020 2020  (" ", "").      
+00001610: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001620: 2020 2020 2020 2020 2020 2020 2020 7265                re
+00001630: 7375 6c74 203d 2072 652e 7370 6c69 7428  sult = re.split(
+00001640: 225b 255c 285c 293c 3e5c 5b5c 5d2c 5c7b  "[%\(\)<>\[\],\{
+00001650: 5c7d 3bef bfbd 047c 5d22 2c20 6929 0a20  \};....|]", i). 
+00001660: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001670: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001680: 2020 2072 6573 756c 7420 3d20 7265 7375     result = resu
+00001690: 6c74 5b30 5d0a 0a20 2020 2020 2020 2020  lt[0]..         
 000016a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000016b0: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-000016c0: 2072 652e 7375 6228 7572 6c2c 2022 222c   re.sub(url, "",
-000016d0: 2072 6573 756c 7429 0a20 2020 2020 2020   result).       
-000016e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000016f0: 2020 2020 2020 2020 2020 2020 2072 6573               res
-00001700: 756c 7420 3d20 7265 2e73 7562 2822 7777  ult = re.sub("ww
-00001710: 7722 2c20 2222 2c20 7265 7375 6c74 290a  w", "", result).
+000016b0: 2020 2020 2020 2065 7863 6570 743a 0a20         except:. 
+000016c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000016d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000016e0: 2020 2072 6573 756c 7420 3d20 690a 2020     result = i.  
+000016f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001700: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001710: 2020 0a20 2020 2020 2020 2020 2020 2020    .             
 00001720: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001730: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001740: 2020 2020 7765 6273 6974 655f 6c69 7374      website_list
-00001750: 2e61 7070 656e 6428 6d79 5f75 726c 202b  .append(my_url +
-00001760: 2072 6573 756c 7429 0a0a 2020 2020 2020   result)..      
+00001730: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
+00001740: 7562 2822 5b5c 5c5c 225c 273b 3d5c 735d  ub("[\\\"\';=\s]
+00001750: 7c61 6374 696f 6e22 2c20 2222 2c20 6929  |action", "", i)
+00001760: 0a0a 2020 2020 2020 2020 2020 2020 2020  ..              
 00001770: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001780: 2020 2020 2020 2373 7263 0a20 2020 2020        #src.     
-00001790: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000017a0: 2020 2020 2020 2073 7263 203d 2072 652e         src = re.
-000017b0: 7375 6228 2220 222c 2022 222c 206d 795f  sub(" ", "", my_
-000017c0: 7265 7175 6573 7429 0a20 2020 2020 2020  request).       
-000017d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000017e0: 2020 2020 2073 7263 203d 2072 652e 6669       src = re.fi
-000017f0: 6e64 616c 6c28 2273 7263 5c73 2a3d 5c73  ndall("src\s*=\s
-00001800: 2a5b 5c22 5c27 5d5c 532b 3f5b 5c27 5c22  *[\"\']\S+?[\'\"
-00001810: 5d22 2c20 7372 6329 0a20 2020 2020 2020  ]", src).       
+00001780: 2020 6966 2072 6573 756c 742e 7374 6172    if result.star
+00001790: 7473 7769 7468 2822 6874 7470 2229 3a0a  tswith("http"):.
+000017a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000017b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000017c0: 2020 2020 6966 2075 726c 2069 6e20 7265      if url in re
+000017d0: 7375 6c74 3a0a 2020 2020 2020 2020 2020  sult:.          
+000017e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000017f0: 2020 2020 2020 2020 2020 2020 2020 7765                we
+00001800: 6273 6974 655f 6c69 7374 2e61 7070 656e  bsite_list.appen
+00001810: 6428 7265 7375 6c74 290a 0a20 2020 2020  d(result)..     
 00001820: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001830: 2020 2020 2073 7263 203d 206c 6973 7428       src = list(
-00001840: 6469 6374 2e66 726f 6d6b 6579 7328 7372  dict.fromkeys(sr
-00001850: 6329 290a 0a20 2020 2020 2020 2020 2020  c))..           
-00001860: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001870: 2066 6f72 2069 2069 6e20 7372 633a 0a20   for i in src:. 
+00001830: 2020 2020 2020 2020 2020 2069 6620 7265             if re
+00001840: 7375 6c74 2e73 7461 7274 7377 6974 6828  sult.startswith(
+00001850: 2268 7474 7022 2920 3d3d 2046 616c 7365  "http") == False
+00001860: 2061 6e64 2072 6573 756c 745b 305d 2021   and result[0] !
+00001870: 3d20 222f 223a 0a20 2020 2020 2020 2020  = "/":.         
 00001880: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001890: 2020 2020 2020 2020 2020 2020 2020 2074                 t
-000018a0: 7279 3a0a 2020 2020 2020 2020 2020 2020  ry:.            
-000018b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000018c0: 2020 2020 2020 2020 6920 3d20 692e 636c          i = i.cl
-000018d0: 6561 6e28 2220 222c 2022 2229 0a20 2020  ean(" ", "").   
-000018e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000018f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001900: 2072 6573 756c 7420 3d20 7265 2e73 706c   result = re.spl
-00001910: 6974 2822 5b25 5c28 5c29 3c3e 5c5b 5c5d  it("[%\(\)<>\[\]
-00001920: 2c5c 7b5c 7d3b efbf bd04 7c5d 222c 2069  ,\{\};....|]", i
-00001930: 290a 2020 2020 2020 2020 2020 2020 2020  ).              
-00001940: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001950: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
-00001960: 6573 756c 745b 305d 0a0a 2020 2020 2020  esult[0]..      
-00001970: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001980: 2020 2020 2020 2020 2020 6578 6365 7074            except
-00001990: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-000019a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000019b0: 2020 2020 2020 7265 7375 6c74 203d 2069        result = i
-000019c0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-000019d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000019e0: 2020 2020 200a 2020 2020 2020 2020 2020       .          
-000019f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001a00: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
-00001a10: 652e 7375 6228 225b 5c5c 5c22 5c27 3b3d  e.sub("[\\\"\';=
-00001a20: 5c73 5d7c 7372 6322 2c20 2222 2c20 6929  \s]|src", "", i)
-00001a30: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001890: 2020 2020 2020 2020 2020 2072 6573 756c             resul
+000018a0: 7420 3d20 7265 2e73 7562 2875 726c 2c20  t = re.sub(url, 
+000018b0: 2222 2c20 7265 7375 6c74 290a 2020 2020  "", result).    
+000018c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000018d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000018e0: 7265 7375 6c74 203d 2072 652e 7375 6228  result = re.sub(
+000018f0: 2277 7777 222c 2022 222c 2072 6573 756c  "www", "", resul
+00001900: 7429 0a20 2020 2020 2020 2020 2020 2020  t).             
+00001910: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001920: 2020 2020 2020 2077 6562 7369 7465 5f6c         website_l
+00001930: 6973 742e 6170 7065 6e64 286d 795f 7572  ist.append(my_ur
+00001940: 6c20 2b20 222f 2220 2b20 7265 7375 6c74  l + "/" + result
+00001950: 290a 0a20 2020 2020 2020 2020 2020 2020  )..             
+00001960: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001970: 2020 2069 6620 7265 7375 6c74 2e73 7461     if result.sta
+00001980: 7274 7377 6974 6828 2268 7474 7022 2920  rtswith("http") 
+00001990: 3d3d 2046 616c 7365 2061 6e64 2072 6573  == False and res
+000019a0: 756c 745b 305d 203d 3d20 222f 223a 0a20  ult[0] == "/":. 
+000019b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000019c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000019d0: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
+000019e0: 7562 2875 726c 2c20 2222 2c20 7265 7375  ub(url, "", resu
+000019f0: 6c74 290a 2020 2020 2020 2020 2020 2020  lt).            
+00001a00: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001a10: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
+00001a20: 2072 652e 7375 6228 2277 7777 222c 2022   re.sub("www", "
+00001a30: 222c 2072 6573 756c 7429 0a20 2020 2020  ", result).     
 00001a40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001a50: 200a 2020 2020 2020 2020 2020 2020 2020   .              
-00001a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001a70: 2020 6966 2072 6573 756c 742e 7374 6172    if result.star
-00001a80: 7473 7769 7468 2822 6874 7470 2229 3a0a  tswith("http"):.
+00001a50: 2020 2020 2020 2020 2020 2020 2020 2077                 w
+00001a60: 6562 7369 7465 5f6c 6973 742e 6170 7065  ebsite_list.appe
+00001a70: 6e64 286d 795f 7572 6c20 2b20 7265 7375  nd(my_url + resu
+00001a80: 6c74 290a 0a20 2020 2020 2020 2020 2020  lt)..           
 00001a90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001aa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001ab0: 2020 2020 6966 2075 726c 2069 6e20 7265      if url in re
-00001ac0: 7375 6c74 3a0a 2020 2020 2020 2020 2020  sult:.          
-00001ad0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001ae0: 2020 2020 2020 2020 2020 2020 2020 7765                we
-00001af0: 6273 6974 655f 6c69 7374 2e61 7070 656e  bsite_list.appen
-00001b00: 6428 7265 7375 6c74 290a 0a20 2020 2020  d(result)..     
-00001b10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001b20: 2020 2020 2020 2020 2020 2069 6620 7265             if re
-00001b30: 7375 6c74 2e73 7461 7274 7377 6974 6828  sult.startswith(
-00001b40: 2268 7474 7022 2920 3d3d 2046 616c 7365  "http") == False
-00001b50: 2061 6e64 2072 6573 756c 745b 305d 2021   and result[0] !
-00001b60: 3d20 222f 223a 0a20 2020 2020 2020 2020  = "/":.         
+00001aa0: 2023 7372 630a 2020 2020 2020 2020 2020   #src.          
+00001ab0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001ac0: 2020 7372 6320 3d20 7265 2e73 7562 2822    src = re.sub("
+00001ad0: 2022 2c20 2222 2c20 6d79 5f72 6571 7565   ", "", my_reque
+00001ae0: 7374 290a 2020 2020 2020 2020 2020 2020  st).            
+00001af0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001b00: 7372 6320 3d20 7265 2e66 696e 6461 6c6c  src = re.findall
+00001b10: 2822 7372 635c 732a 3d5c 732a 5b5c 225c  ("src\s*=\s*[\"\
+00001b20: 275d 5c53 2b3f 5b5c 275c 225d 222c 2073  ']\S+?[\'\"]", s
+00001b30: 7263 290a 2020 2020 2020 2020 2020 2020  rc).            
+00001b40: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001b50: 7372 6320 3d20 6c69 7374 2864 6963 742e  src = list(dict.
+00001b60: 6672 6f6d 6b65 7973 2873 7263 2929 0a0a  fromkeys(src))..
 00001b70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001b80: 2020 2020 2020 2020 2020 2072 6573 756c             resul
-00001b90: 7420 3d20 7265 2e73 7562 2875 726c 2c20  t = re.sub(url, 
-00001ba0: 2222 2c20 7265 7375 6c74 290a 2020 2020  "", result).    
-00001bb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001b80: 2020 2020 2020 2020 2020 2020 666f 7220              for 
+00001b90: 6920 696e 2073 7263 3a0a 2020 2020 2020  i in src:.      
+00001ba0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001bb0: 2020 2020 2020 2020 2020 7472 793a 0a20            try:. 
 00001bc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001bd0: 7265 7375 6c74 203d 2072 652e 7375 6228  result = re.sub(
-00001be0: 2277 7777 222c 2022 222c 2072 6573 756c  "www", "", resul
-00001bf0: 7429 0a20 2020 2020 2020 2020 2020 2020  t).             
+00001bd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001be0: 2020 2069 203d 2069 2e63 6c65 616e 2822     i = i.clean("
+00001bf0: 2022 2c20 2222 290a 2020 2020 2020 2020   ", "").        
 00001c00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001c10: 2020 2020 2020 2077 6562 7369 7465 5f6c         website_l
-00001c20: 6973 742e 6170 7065 6e64 286d 795f 7572  ist.append(my_ur
-00001c30: 6c20 2b20 222f 2220 2b20 7265 7375 6c74  l + "/" + result
-00001c40: 290a 0a20 2020 2020 2020 2020 2020 2020  )..             
+00001c10: 2020 2020 2020 2020 2020 2020 7265 7375              resu
+00001c20: 6c74 203d 2072 652e 7370 6c69 7428 225b  lt = re.split("[
+00001c30: 255c 285c 293c 3e5c 5b5c 5d2c 5c7b 5c7d  %\(\)<>\[\],\{\}
+00001c40: 3bef bfbd 047c 5d22 2c20 6929 0a20 2020  ;....|]", i).   
 00001c50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001c60: 2020 2069 6620 7265 7375 6c74 2e73 7461     if result.sta
-00001c70: 7274 7377 6974 6828 2268 7474 7022 2920  rtswith("http") 
-00001c80: 3d3d 2046 616c 7365 2061 6e64 2072 6573  == False and res
-00001c90: 756c 745b 305d 203d 3d20 222f 223a 0a20  ult[0] == "/":. 
-00001ca0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001c60: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001c70: 2072 6573 756c 7420 3d20 7265 7375 6c74   result = result
+00001c80: 5b30 5d0a 0a20 2020 2020 2020 2020 2020  [0]..           
+00001c90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001ca0: 2020 2020 2065 7863 6570 743a 0a20 2020       except:.   
 00001cb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001cc0: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
-00001cd0: 7562 2875 726c 2c20 2222 2c20 7265 7375  ub(url, "", resu
-00001ce0: 6c74 290a 2020 2020 2020 2020 2020 2020  lt).            
+00001cc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001cd0: 2072 6573 756c 7420 3d20 690a 2020 2020   result = i.    
+00001ce0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00001cf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001d00: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-00001d10: 2072 652e 7375 6228 2277 7777 222c 2022   re.sub("www", "
-00001d20: 222c 2072 6573 756c 7429 0a20 2020 2020  ", result).     
-00001d30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001d40: 2020 2020 2020 2020 2020 2020 2020 2077                 w
-00001d50: 6562 7369 7465 5f6c 6973 742e 6170 7065  ebsite_list.appe
-00001d60: 6e64 286d 795f 7572 6c20 2b20 7265 7375  nd(my_url + resu
-00001d70: 6c74 290a 0a20 2020 2020 2020 2020 2020  lt)..           
-00001d80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001d90: 2023 736c 6173 680a 2020 2020 2020 2020   #slash.        
-00001da0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001db0: 2020 2020 736c 6173 6820 3d20 7265 2e66      slash = re.f
-00001dc0: 696e 6461 6c6c 2822 5b5c 277c 5c22 5d2f  indall("[\'|\"]/
-00001dd0: 5c53 2b5b 5c22 7c5c 275d 222c 206d 795f  \S+[\"|\']", my_
-00001de0: 7265 7175 6573 7429 0a0a 2020 2020 2020  request)..      
+00001d00: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001d10: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001d20: 2072 6573 756c 7420 3d20 7265 2e73 7562   result = re.sub
+00001d30: 2822 5b5c 5c5c 225c 273b 3d5c 735d 7c73  ("[\\\"\';=\s]|s
+00001d40: 7263 222c 2022 222c 2069 290a 2020 2020  rc", "", i).    
+00001d50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001d60: 2020 2020 2020 2020 2020 2020 0a20 2020              .   
+00001d70: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001d80: 2020 2020 2020 2020 2020 2020 2069 6620               if 
+00001d90: 7265 7375 6c74 2e73 7461 7274 7377 6974  result.startswit
+00001da0: 6828 2268 7474 7022 293a 0a20 2020 2020  h("http"):.     
+00001db0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001dc0: 2020 2020 2020 2020 2020 2020 2020 2069                 i
+00001dd0: 6620 7572 6c20 696e 2072 6573 756c 743a  f url in result:
+00001de0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 00001df0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001e00: 2020 2020 2020 666f 7220 6920 696e 2073        for i in s
-00001e10: 6c61 7368 3a0a 2020 2020 2020 2020 2020  lash:.          
-00001e20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001e30: 2020 2020 2020 6d79 5f73 6561 7263 6820        my_search 
-00001e40: 3d20 7265 2e73 6561 7263 6828 2268 7474  = re.search("htt
-00001e50: 707c 5c2e 636f 6d7c 5c2e 6564 757c 5c2e  p|\.com|\.edu|\.
-00001e60: 6e65 747c 5c2e 6f72 677c 5c2e 7476 7c77  net|\.org|\.tv|w
-00001e70: 7777 7c68 7474 7022 2c20 6929 0a0a 2020  ww|http", i)..  
-00001e80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001e90: 2020 2020 2020 2020 2020 2020 2020 6966                if
-00001ea0: 206e 6f74 206d 795f 7365 6172 6368 3a0a   not my_search:.
-00001eb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001ec0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001ed0: 2020 2020 7265 7375 6c74 203d 2072 652e      result = re.
-00001ee0: 7375 6228 225b 5c22 5c27 5d22 2c20 2222  sub("[\"\']", ""
-00001ef0: 2c20 6929 0a20 2020 2020 2020 2020 2020  , i).           
-00001f00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001f10: 2020 2020 2020 2020 2072 6573 756c 7420           result 
-00001f20: 3d20 7265 2e73 706c 6974 2822 5b25 5c28  = re.split("[%\(
-00001f30: 5c29 3c3e 5c5b 5c5d 2c5c 7b5c 7d3b efbf  \)<>\[\],\{\};..
-00001f40: bd04 7c5d 222c 2072 6573 756c 7429 0a20  ..|]", result). 
-00001f50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001e00: 2020 2020 2020 2020 2077 6562 7369 7465           website
+00001e10: 5f6c 6973 742e 6170 7065 6e64 2872 6573  _list.append(res
+00001e20: 756c 7429 0a0a 2020 2020 2020 2020 2020  ult)..          
+00001e30: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001e40: 2020 2020 2020 6966 2072 6573 756c 742e        if result.
+00001e50: 7374 6172 7473 7769 7468 2822 6874 7470  startswith("http
+00001e60: 2229 203d 3d20 4661 6c73 6520 616e 6420  ") == False and 
+00001e70: 7265 7375 6c74 5b30 5d20 213d 2022 2f22  result[0] != "/"
+00001e80: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+00001e90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001ea0: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
+00001eb0: 652e 7375 6228 7572 6c2c 2022 222c 2072  e.sub(url, "", r
+00001ec0: 6573 756c 7429 0a20 2020 2020 2020 2020  esult).         
+00001ed0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001ee0: 2020 2020 2020 2020 2020 2072 6573 756c             resul
+00001ef0: 7420 3d20 7265 2e73 7562 2822 7777 7722  t = re.sub("www"
+00001f00: 2c20 2222 2c20 7265 7375 6c74 290a 2020  , "", result).  
+00001f10: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001f20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001f30: 2020 7765 6273 6974 655f 6c69 7374 2e61    website_list.a
+00001f40: 7070 656e 6428 6d79 5f75 726c 202b 2022  ppend(my_url + "
+00001f50: 2f22 202b 2072 6573 756c 7429 0a0a 2020  /" + result)..  
 00001f60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001f70: 2020 2072 6573 756c 7420 3d20 7265 7375     result = resu
-00001f80: 6c74 5b30 5d0a 2020 2020 2020 2020 2020  lt[0].          
-00001f90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001fa0: 2020 2020 2020 2020 2020 7765 6273 6974            websit
-00001fb0: 655f 6c69 7374 2e61 7070 656e 6428 6d79  e_list.append(my
-00001fc0: 5f75 726c 202b 2072 6573 756c 7429 0a0a  _url + result)..
-00001fd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001fe0: 2020 2020 656c 7365 3a0a 2020 2020 2020      else:.      
-00001ff0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002000: 2020 7072 696e 7428 7265 6420 2b20 7374    print(red + st
-00002010: 7228 7374 6174 7573 2920 2b20 223a 2022  r(status) + ": "
-00002020: 202b 2073 7472 2877 6562 7369 7465 5f6c   + str(website_l
-00002030: 6973 745b 7472 6163 6b65 725d 2929 0a20  ist[tracker])). 
-00002040: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002050: 2020 2020 2020 2077 6562 7369 7465 5f6c         website_l
-00002060: 6973 742e 706f 7028 7472 6163 6b65 7229  ist.pop(tracker)
-00002070: 0a0a 2020 2020 2020 2020 2020 2020 6966  ..            if
-00002080: 206e 6f74 2066 696e 645f 6d79 3a0a 2020   not find_my:.  
-00002090: 2020 2020 2020 2020 2020 2020 2020 7765                we
-000020a0: 6273 6974 655f 6c69 7374 2e70 6f70 2874  bsite_list.pop(t
-000020b0: 7261 636b 6572 290a 0a20 2020 2020 2020  racker)..       
-000020c0: 2065 7863 6570 7420 496e 6465 7845 7272   except IndexErr
-000020d0: 6f72 3a0a 2020 2020 2020 2020 2020 2020  or:.            
-000020e0: 6272 6561 6b0a 0a20 2020 2020 2020 2065  break..        e
-000020f0: 7863 6570 743a 0a20 2020 2020 2020 2020  xcept:.         
-00002100: 2020 2070 7269 6e74 2872 6564 202b 2022     print(red + "
-00002110: 4552 524f 523a 2022 202b 2073 7472 2877  ERROR: " + str(w
-00002120: 6562 7369 7465 5f6c 6973 745b 7472 6163  ebsite_list[trac
-00002130: 6b65 725d 2929 0a20 2020 2020 2020 2020  ker])).         
-00002140: 2020 2077 6562 7369 7465 5f6c 6973 742e     website_list.
-00002150: 706f 7028 7472 6163 6b65 7229 0a0a 0a20  pop(tracker)... 
-00002160: 2020 2077 6562 7369 7465 5f6c 6973 7420     website_list 
-00002170: 3d20 6c69 7374 2864 6963 742e 6672 6f6d  = list(dict.from
-00002180: 6b65 7973 2877 6562 7369 7465 5f6c 6973  keys(website_lis
-00002190: 7429 290a 2020 2020 7765 6273 6974 655f  t)).    website_
-000021a0: 6c69 7374 2e73 6f72 7428 290a 0a20 2020  list.sort()..   
-000021b0: 2063 6c65 6172 2829 0a0a 2020 2020 6966   clear()..    if
-000021c0: 206d 795f 6669 6c65 2021 3d20 2220 223a   my_file != " ":
-000021d0: 0a20 2020 2020 2020 2077 6974 6820 6f70  .        with op
-000021e0: 656e 286d 795f 6669 6c65 2c20 2261 2229  en(my_file, "a")
-000021f0: 2061 7320 6669 6c65 3a0a 2020 2020 2020   as file:.      
-00002200: 2020 2020 2020 666f 7220 6920 696e 2077        for i in w
-00002210: 6562 7369 7465 5f6c 6973 743a 0a20 2020  ebsite_list:.   
-00002220: 2020 2020 2020 2020 2020 2020 2066 696c               fil
-00002230: 652e 7772 6974 6528 6920 2b20 225c 6e22  e.write(i + "\n"
-00002240: 290a 0a20 2020 2072 6574 7572 6e20 7765  )..    return we
-00002250: 6273 6974 655f 6c69 7374 0a              bsite_list.
+00001f70: 2020 2020 2020 2020 2020 2020 2020 6966                if
+00001f80: 2072 6573 756c 742e 7374 6172 7473 7769   result.startswi
+00001f90: 7468 2822 6874 7470 2229 203d 3d20 4661  th("http") == Fa
+00001fa0: 6c73 6520 616e 6420 7265 7375 6c74 5b30  lse and result[0
+00001fb0: 5d20 3d3d 2022 2f22 3a0a 2020 2020 2020  ] == "/":.      
+00001fc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001fd0: 2020 2020 2020 2020 2020 2020 2020 7265                re
+00001fe0: 7375 6c74 203d 2072 652e 7375 6228 7572  sult = re.sub(ur
+00001ff0: 6c2c 2022 222c 2072 6573 756c 7429 0a20  l, "", result). 
+00002000: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002010: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002020: 2020 2072 6573 756c 7420 3d20 7265 2e73     result = re.s
+00002030: 7562 2822 7777 7722 2c20 2222 2c20 7265  ub("www", "", re
+00002040: 7375 6c74 290a 2020 2020 2020 2020 2020  sult).          
+00002050: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002060: 2020 2020 2020 2020 2020 7765 6273 6974            websit
+00002070: 655f 6c69 7374 2e61 7070 656e 6428 6d79  e_list.append(my
+00002080: 5f75 726c 202b 2072 6573 756c 7429 0a0a  _url + result)..
+00002090: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000020a0: 2020 2020 2020 2020 2020 2020 2373 6c61              #sla
+000020b0: 7368 0a20 2020 2020 2020 2020 2020 2020  sh.             
+000020c0: 2020 2020 2020 2020 2020 2020 2020 2073                 s
+000020d0: 6c61 7368 203d 2072 652e 6669 6e64 616c  lash = re.findal
+000020e0: 6c28 225b 5c27 7c5c 225d 2f5c 532b 5b5c  l("[\'|\"]/\S+[\
+000020f0: 227c 5c27 5d22 2c20 6d79 5f72 6571 7565  "|\']", my_reque
+00002100: 7374 290a 0a20 2020 2020 2020 2020 2020  st)..           
+00002110: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002120: 2066 6f72 2069 2069 6e20 736c 6173 683a   for i in slash:
+00002130: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00002140: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002150: 206d 795f 7365 6172 6368 203d 2072 652e   my_search = re.
+00002160: 7365 6172 6368 2822 6874 7470 7c5c 2e63  search("http|\.c
+00002170: 6f6d 7c5c 2e65 6475 7c5c 2e6e 6574 7c5c  om|\.edu|\.net|\
+00002180: 2e6f 7267 7c5c 2e74 767c 7777 777c 6874  .org|\.tv|www|ht
+00002190: 7470 222c 2069 290a 0a20 2020 2020 2020  tp", i)..       
+000021a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000021b0: 2020 2020 2020 2020 2069 6620 6e6f 7420           if not 
+000021c0: 6d79 5f73 6561 7263 683a 0a20 2020 2020  my_search:.     
+000021d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000021e0: 2020 2020 2020 2020 2020 2020 2020 2072                 r
+000021f0: 6573 756c 7420 3d20 7265 2e73 7562 2822  esult = re.sub("
+00002200: 5b5c 225c 275d 222c 2022 222c 2069 290a  [\"\']", "", i).
+00002210: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002220: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002230: 2020 2020 7265 7375 6c74 203d 2072 652e      result = re.
+00002240: 7370 6c69 7428 225b 255c 285c 293c 3e5c  split("[%\(\)<>\
+00002250: 5b5c 5d2c 5c7b 5c7d 3bef bfbd 047c 5d22  [\],\{\};....|]"
+00002260: 2c20 7265 7375 6c74 290a 2020 2020 2020  , result).      
+00002270: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002280: 2020 2020 2020 2020 2020 2020 2020 7265                re
+00002290: 7375 6c74 203d 2072 6573 756c 745b 305d  sult = result[0]
+000022a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000022b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000022c0: 2020 2020 2077 6562 7369 7465 5f6c 6973       website_lis
+000022d0: 742e 6170 7065 6e64 286d 795f 7572 6c20  t.append(my_url 
+000022e0: 2b20 7265 7375 6c74 290a 0a20 2020 2020  + result)..     
+000022f0: 2020 2020 2020 2020 2020 2020 2020 2065                 e
+00002300: 6c73 653a 0a20 2020 2020 2020 2020 2020  lse:.           
+00002310: 2020 2020 2020 2020 2020 2020 2070 7269               pri
+00002320: 6e74 2872 6564 202b 2073 7472 2873 7461  nt(red + str(sta
+00002330: 7475 7329 202b 2022 3a20 2220 2b20 7374  tus) + ": " + st
+00002340: 7228 7765 6273 6974 655f 6c69 7374 5b74  r(website_list[t
+00002350: 7261 636b 6572 5d29 290a 2020 2020 2020  racker])).      
+00002360: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002370: 2020 7765 6273 6974 655f 6c69 7374 2e70    website_list.p
+00002380: 6f70 2874 7261 636b 6572 290a 0a20 2020  op(tracker)..   
+00002390: 2020 2020 2020 2020 2069 6620 6e6f 7420           if not 
+000023a0: 6669 6e64 5f6d 793a 0a20 2020 2020 2020  find_my:.       
+000023b0: 2020 2020 2020 2020 2077 6562 7369 7465           website
+000023c0: 5f6c 6973 742e 706f 7028 7472 6163 6b65  _list.pop(tracke
+000023d0: 7229 0a0a 2020 2020 2020 2020 6578 6365  r)..        exce
+000023e0: 7074 2049 6e64 6578 4572 726f 723a 0a20  pt IndexError:. 
+000023f0: 2020 2020 2020 2020 2020 2062 7265 616b             break
+00002400: 0a0a 2020 2020 2020 2020 6578 6365 7074  ..        except
+00002410: 3a0a 2020 2020 2020 2020 2020 2020 7072  :.            pr
+00002420: 696e 7428 7265 6420 2b20 2245 5252 4f52  int(red + "ERROR
+00002430: 3a20 2220 2b20 7374 7228 7765 6273 6974  : " + str(websit
+00002440: 655f 6c69 7374 5b74 7261 636b 6572 5d29  e_list[tracker])
+00002450: 290a 2020 2020 2020 2020 2020 2020 7765  ).            we
+00002460: 6273 6974 655f 6c69 7374 2e70 6f70 2874  bsite_list.pop(t
+00002470: 7261 636b 6572 290a 0a0a 2020 2020 7765  racker)...    we
+00002480: 6273 6974 655f 6c69 7374 203d 206c 6973  bsite_list = lis
+00002490: 7428 6469 6374 2e66 726f 6d6b 6579 7328  t(dict.fromkeys(
+000024a0: 7765 6273 6974 655f 6c69 7374 2929 0a20  website_list)). 
+000024b0: 2020 2077 6562 7369 7465 5f6c 6973 742e     website_list.
+000024c0: 736f 7274 2829 0a0a 2020 2020 636c 6561  sort()..    clea
+000024d0: 7228 290a 0a20 2020 2069 6620 6d79 5f66  r()..    if my_f
+000024e0: 696c 6520 213d 2022 2022 3a0a 2020 2020  ile != " ":.    
+000024f0: 2020 2020 7769 7468 206f 7065 6e28 6d79      with open(my
+00002500: 5f66 696c 652c 2022 6122 2920 6173 2066  _file, "a") as f
+00002510: 696c 653a 0a20 2020 2020 2020 2020 2020  ile:.           
+00002520: 2066 6f72 2069 2069 6e20 7765 6273 6974   for i in websit
+00002530: 655f 6c69 7374 3a0a 2020 2020 2020 2020  e_list:.        
+00002540: 2020 2020 2020 2020 6669 6c65 2e77 7269          file.wri
+00002550: 7465 2869 202b 2022 5c6e 2229 0a0a 2020  te(i + "\n")..  
+00002560: 2020 7265 7475 726e 2077 6562 7369 7465    return website
+00002570: 5f6c 6973 740a                           _list.
```

### Comparing `TheSilent-0.0.98/src/TheSilent/login_cracker.py` & `TheSilent-0.0.99/src/TheSilent/login_cracker.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/nmap.py` & `TheSilent-0.0.99/src/TheSilent/nmap.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/packet_sniffer.py` & `TheSilent-0.0.99/src/TheSilent/packet_sniffer.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/port_scanner.py` & `TheSilent-0.0.99/src/TheSilent/port_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/secure_overwrite.py` & `TheSilent-0.0.99/src/TheSilent/secure_overwrite.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/security_scanner.py` & `TheSilent-0.0.99/src/TheSilent/security_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/source_code_viewer.py` & `TheSilent-0.0.99/src/TheSilent/source_code_viewer.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/sql_injection_scanner.py` & `TheSilent-0.0.99/src/TheSilent/sql_injection_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/subdomain_scanner.py` & `TheSilent-0.0.99/src/TheSilent/subdomain_scanner.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/subdomain_takeover.py` & `TheSilent-0.0.99/src/TheSilent/subdomain_takeover.py`

 * *Files identical despite different names*

### Comparing `TheSilent-0.0.98/src/TheSilent/xss_scanner.py` & `TheSilent-0.0.99/src/TheSilent/xss_scanner.py`

 * *Files 21% similar despite different names*

```diff
@@ -4,14 +4,16 @@
 import requests
 
 red = "\033[1;31m"
 
 #create html sessions object
 web_session = requests.Session()
 
+tor_proxy = {"https": "socks5h://localhost:9050", "http": "socks5h://localhost:9050"}
+
 #fake user agent
 user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
 
 #increased security
 requests.packages.urllib3.disable_warnings()
 requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"
 
@@ -19,15 +21,15 @@
 try:
     requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"
 
 except AttributeError:
     pass
 
 #scans for xss
-def xss_scanner(url, secure = True, my_file = " "):
+def xss_scanner(url, secure = True, my_file = " ", tor = False):
     if secure == True:
         my_secure = "https://"
 
     if secure == False:
         my_secure = "http://"
 
     cyan = "\033[1;36m"
@@ -59,15 +61,19 @@
                     my_url = links + mal_script
 
                 if not links.endswith("/"):
                     my_url = links + "/" + mal_script
 
                 print(red + "checking: " + str(my_url)) 
 
-                result = web_session.get(my_url, verify = False, headers = user_agent, timeout = (5, 30))
+                if tor == True:
+                    result = web_session.get(my_url, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))
+                    
+                else:
+                    result = web_session.get(my_url, verify = False, headers = user_agent, timeout = (5, 30))
 
                 if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                     print(cyan + "firewall detected")
 
                 if result.status_code >= 200 and result.status_code < 300:
                     if mal_script in result.text and "404" not in result.text:
                         print(red + "true: " + my_url)
@@ -78,15 +84,19 @@
         
         print(red + "checking: " + str(links) + " (user agent)")  
 
         try:
             for mal_script in mal_payloads:
                 user_agent_moded = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", mal_script: mal_script}
 
-                result = web_session.get(links, verify = False, headers = user_agent_moded, timeout = (5, 30))
+                if tor == True:
+                    result = web_session.get(links, verify = False, headers = user_agent_moded, proxies = tor_proxy, timeout = (5, 30))
+
+                else:
+                    result = web_session.get(links, verify = False, headers = user_agent_moded, timeout = (5, 30))
                 
                 if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                     print(cyan + "firewall detected")
 
                 if result.status_code >= 200 and result.status_code < 300:
                     if mal_script in result.text and "404" not in result.text:
                         print(red + "true: " + links + " (user agent) " + mal_script)
@@ -99,15 +109,19 @@
 
         print(red + "checking: " + str(links) + " (cookie)")  
 
         try:
             for mal_script in mal_payloads:
                 mal_cookie = {mal_script: mal_script}
 
-                result = web_session.get(links, verify = False, headers = user_agent, cookies = mal_cookie, timeout = (5, 30))
+                if tor == True:
+                    result = web_session.get(links, verify = False, headers = user_agent, cookies = mal_cookie, proxies = tor_proxy, timeout = (5, 30))
+
+                else:
+                    result = web_session.get(links, verify = False, headers = user_agent, cookies = mal_cookie, timeout = (5, 30))
                 
                 if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                     print(cyan + "firewall detected")
 
                 if result.status_code >= 200 and result.status_code < 300:
                     if mal_script in result.text and "404" not in result.text:
                         print(red + "true: " + links + " (cookie) " + mal_script)
@@ -125,16 +139,21 @@
             for i in form_input:
                 for mal_script in mal_payloads:
                     name = str(re.findall("name.+\".+\"", i)).split("\"")
                     mal_dict = {name[1] : mal_script}
 
                     print(red + "checking: " + str(links) + " " + str(mal_dict))
 
-                    get = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
-                    post = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
+                    if tor == True:
+                        get = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))
+                        post = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))
+
+                    else:
+                        get = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
+                        post = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
 
                     if get.status_code == 401 or get.status_code == 403 or get.status_code == 405:
                         print(cyan + "firewall detected")
 
                     if get.status_code >= 200 and get.status_code < 300:
                         if mal_script in get.text and "404" not in get.text:
                             print(red + "true: " + str(links) + " " + str(mal_dict))
```

### Comparing `TheSilent-0.0.98/src/TheSilent.egg-info/PKG-INFO` & `TheSilent-0.0.99/src/TheSilent.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: TheSilent
-Version: 0.0.98
+Version: 0.0.99
 Summary: Python penetration testing, osint, and digital forensics multi tool!
 Author-email: Michael Mueller <michael.j.mueller.pro@gmail.com>
 Project-URL: Homepage, https://github.com/Invizabel/The-Silent
 Project-URL: Bug Tracker, https://github.com/Invizabel/The-Silent/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `TheSilent-0.0.98/src/TheSilent.egg-info/SOURCES.txt` & `TheSilent-0.0.99/src/TheSilent.egg-info/SOURCES.txt`

 * *Files identical despite different names*

