# Comparing `tmp/pywencai-0.5.0.tar.gz` & `tmp/pywencai-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pywencai-0.5.0.tar", max compression
+gzip compressed data, was "pywencai-0.5.1.tar", max compression
```

## Comparing `pywencai-0.5.0.tar` & `pywencai-0.5.1.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1062 2023-04-01 05:08:18.366314 pywencai-0.5.0/LICENSE
--rw-r--r--   0        0        0     1814 2023-04-01 05:08:18.366314 pywencai-0.5.0/README.md
--rw-r--r--   0        0        0      490 2023-04-01 05:08:18.370314 pywencai-0.5.0/pyproject.toml
--rw-r--r--   0        0        0       23 2023-04-01 05:08:18.370314 pywencai-0.5.0/pywencai/__init__.py
--rw-r--r--   0        0        0    39677 2023-04-01 05:08:18.370314 pywencai-0.5.0/pywencai/hexin-v.js
--rw-r--r--   0        0        0     4117 2023-04-01 05:08:18.370314 pywencai-0.5.0/pywencai/wencai.py
--rw-r--r--   0        0        0     2302 1970-01-01 00:00:00.000000 pywencai-0.5.0/PKG-INFO
+-rw-r--r--   0        0        0     1062 2023-04-06 13:05:04.130357 pywencai-0.5.1/LICENSE
+-rw-r--r--   0        0        0     1814 2023-04-06 13:05:04.130357 pywencai-0.5.1/README.md
+-rw-r--r--   0        0        0      516 2023-04-06 13:05:04.134357 pywencai-0.5.1/pyproject.toml
+-rw-r--r--   0        0        0       23 2023-04-06 13:05:04.134357 pywencai-0.5.1/pywencai/__init__.py
+-rw-r--r--   0        0        0    39677 2023-04-06 13:05:04.134357 pywencai-0.5.1/pywencai/hexin-v.js
+-rw-r--r--   0        0        0     3964 2023-04-06 13:05:04.134357 pywencai-0.5.1/pywencai/wencai.py
+-rw-r--r--   0        0        0     2349 1970-01-01 00:00:00.000000 pywencai-0.5.1/PKG-INFO
```

### Comparing `pywencai-0.5.0/LICENSE` & `pywencai-0.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pywencai-0.5.0/README.md` & `pywencai-0.5.1/README.md`

 * *Files identical despite different names*

### Comparing `pywencai-0.5.0/pywencai/hexin-v.js` & `pywencai-0.5.1/pywencai/hexin-v.js`

 * *Files identical despite different names*

### Comparing `pywencai-0.5.0/pywencai/wencai.py` & `pywencai-0.5.1/pywencai/wencai.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,17 @@
 import os
 import execjs
 import json
 import requests as rq
 import pandas as pd
 import time
 import logging
+from fake_useragent import UserAgent
+
+ua = UserAgent()
 
 logging.basicConfig(
     level=logging.INFO,
     format='[pywencai] %(asctime)s - %(levelname)s - %(message)s'
 )
 
 # 获取token
@@ -38,15 +41,15 @@
     time.sleep(sleep)
     res = rq.request(
       method='POST',
       url='http://www.iwencai.com/customized/chart/get-robot-data',
       json=data,
       headers={
         'hexin-v': getToken(),
-        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
+        'User-Agent': ua.random
       }
     )
     result = json.loads(res.text)
     condition = result['data']['answer'][0]['txt'][0]['content']['components'][0]['data']['meta']['extra']['condition']
     log and logging.info(f'获取condition成功')
     return condition
   log and logging.info(f'获取condition失败')
@@ -109,15 +112,15 @@
     try: 
       res = rq.request(
         method='POST',
         url='http://www.iwencai.com/gateway/urp/v7/landing/getDataList',
         data=data,
         headers={
           'hexin-v': getToken(),
-          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
+          'User-Agent': ua.random
         },
         timeout=(5, 10)
       )
       result = json.loads(res.text)
       list = result['answer']['components'][0]['data']['datas']
       log and logging.info(f'第{data.get("page")}页成功')
       return pd.DataFrame.from_dict(list)
```

### Comparing `pywencai-0.5.0/PKG-INFO` & `pywencai-0.5.1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: pywencai
-Version: 0.5.0
+Version: 0.5.1
 Summary: 
 Author: pluto
 Author-email: mayuanchi1029@gmail.com
 Requires-Python: >=3.8,<3.11
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Dist: PyExecJS (>=1.5.1,<2.0.0)
+Requires-Dist: fake-useragent (>=1.1.1,<2.0.0)
 Requires-Dist: pandas (>=1.5.0,<2.0.0)
 Requires-Dist: requests
 Description-Content-Type: text/markdown
 
 # pywencai
 
 获取同花顺问财数据
```

