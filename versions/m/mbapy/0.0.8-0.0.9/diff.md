# Comparing `tmp/mbapy-0.0.8.tar.gz` & `tmp/mbapy-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mbapy-0.0.8.tar", last modified: Wed Dec 14 17:42:04 2022, max compression
+gzip compressed data, was "mbapy-0.0.9.tar", last modified: Mon Mar 20 16:40:50 2023, max compression
```

## Comparing `mbapy-0.0.8.tar` & `mbapy-0.0.9.tar`

### file list

```diff
@@ -1,22 +1,27 @@
-drwxrwxrwx   0        0        0        0 2022-12-14 17:42:04.231335 mbapy-0.0.8/
--rw-rw-rw-   0        0        0     1085 2022-10-19 14:16:22.000000 mbapy-0.0.8/LICENSE
--rw-rw-rw-   0        0        0     2097 2022-12-14 17:42:04.230333 mbapy-0.0.8/PKG-INFO
--rw-rw-rw-   0        0        0     1323 2022-12-09 09:23:24.000000 mbapy-0.0.8/README.md
-drwxrwxrwx   0        0        0        0 2022-12-14 17:42:04.215330 mbapy-0.0.8/mbapy/
--rw-rw-rw-   0        0        0      363 2022-12-14 17:23:32.000000 mbapy-0.0.8/mbapy/__init__.py
--rw-rw-rw-   0        0        0      212 2022-11-04 05:54:25.000000 mbapy-0.0.8/mbapy/__version__.py
--rw-rw-rw-   0        0        0     2285 2022-11-07 13:52:47.000000 mbapy-0.0.8/mbapy/base.py
--rw-rw-rw-   0        0        0      350 2022-11-02 03:58:20.000000 mbapy-0.0.8/mbapy/file.py
--rw-rw-rw-   0        0        0     9982 2022-12-14 17:14:26.000000 mbapy-0.0.8/mbapy/plot.py
-drwxrwxrwx   0        0        0        0 2022-12-14 17:42:04.228336 mbapy-0.0.8/mbapy/stats/
--rw-rw-rw-   0        0        0      331 2022-12-09 11:25:53.000000 mbapy-0.0.8/mbapy/stats/__init__.py
--rw-rw-rw-   0        0        0    19333 2022-12-05 10:10:18.000000 mbapy-0.0.8/mbapy/stats/geography.py
--rw-rw-rw-   0        0        0     9856 2022-12-14 17:14:11.000000 mbapy-0.0.8/mbapy/web.py
-drwxrwxrwx   0        0        0        0 2022-12-14 17:42:04.226332 mbapy-0.0.8/mbapy.egg-info/
--rw-rw-rw-   0        0        0     2097 2022-12-14 17:42:04.000000 mbapy-0.0.8/mbapy.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      362 2022-12-14 17:42:04.000000 mbapy-0.0.8/mbapy.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-12-14 17:42:04.000000 mbapy-0.0.8/mbapy.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      351 2022-12-14 17:42:04.000000 mbapy-0.0.8/mbapy.egg-info/requires.txt
--rw-rw-rw-   0        0        0       18 2022-12-14 17:42:04.000000 mbapy-0.0.8/mbapy.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2022-12-14 17:42:04.231335 mbapy-0.0.8/setup.cfg
--rw-rw-rw-   0        0        0     2506 2022-12-14 17:41:58.000000 mbapy-0.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-20 16:40:50.874974 mbapy-0.0.9/
+-rw-rw-rw-   0        0        0     1085 2022-10-19 14:16:22.000000 mbapy-0.0.9/LICENSE
+-rw-rw-rw-   0        0        0     2177 2023-03-20 16:40:50.874974 mbapy-0.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0     1403 2023-03-20 15:11:19.000000 mbapy-0.0.9/README.md
+drwxrwxrwx   0        0        0        0 2023-03-20 16:40:50.810969 mbapy-0.0.9/mbapy/
+-rw-rw-rw-   0        0        0      363 2023-03-20 16:40:02.000000 mbapy-0.0.9/mbapy/__init__.py
+-rw-rw-rw-   0        0        0      356 2023-03-20 16:39:34.000000 mbapy-0.0.9/mbapy/__version__.py
+-rw-rw-rw-   0        0        0     2572 2023-03-20 16:36:28.000000 mbapy-0.0.9/mbapy/base.py
+drwxrwxrwx   0        0        0        0 2023-03-20 16:40:50.866971 mbapy-0.0.9/mbapy/dl_torch/
+-rw-rw-rw-   0        0        0      181 2023-03-20 16:11:34.000000 mbapy-0.0.9/mbapy/dl_torch/__init__.py
+-rw-rw-rw-   0        0        0     3823 2023-03-20 16:35:29.000000 mbapy-0.0.9/mbapy/dl_torch/data.py
+-rw-rw-rw-   0        0        0     4113 2023-03-20 16:36:17.000000 mbapy-0.0.9/mbapy/dl_torch/loss.py
+-rw-rw-rw-   0        0        0     8732 2023-03-20 16:35:37.000000 mbapy-0.0.9/mbapy/dl_torch/utils.py
+-rw-rw-rw-   0        0        0     1622 2023-03-20 16:35:29.000000 mbapy-0.0.9/mbapy/file.py
+-rw-rw-rw-   0        0        0    11581 2023-03-20 15:04:49.000000 mbapy-0.0.9/mbapy/plot.py
+drwxrwxrwx   0        0        0        0 2023-03-20 16:40:50.874974 mbapy-0.0.9/mbapy/stats/
+-rw-rw-rw-   0        0        0      331 2022-12-09 11:25:53.000000 mbapy-0.0.9/mbapy/stats/__init__.py
+-rw-rw-rw-   0        0        0    19333 2022-12-05 10:10:18.000000 mbapy-0.0.9/mbapy/stats/geography.py
+-rw-rw-rw-   0        0        0     8827 2023-03-20 16:03:33.000000 mbapy-0.0.9/mbapy/web.py
+drwxrwxrwx   0        0        0        0 2023-03-20 16:40:50.850968 mbapy-0.0.9/mbapy.egg-info/
+-rw-rw-rw-   0        0        0     2177 2023-03-20 16:40:50.000000 mbapy-0.0.9/mbapy.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      556 2023-03-20 16:40:50.000000 mbapy-0.0.9/mbapy.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-20 16:40:50.000000 mbapy-0.0.9/mbapy.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      351 2023-03-20 16:40:50.000000 mbapy-0.0.9/mbapy.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       33 2023-03-20 16:40:50.000000 mbapy-0.0.9/mbapy.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-03-20 16:40:50.882973 mbapy-0.0.9/setup.cfg
+-rw-rw-rw-   0        0        0     2541 2023-03-20 16:37:52.000000 mbapy-0.0.9/setup.py
```

### Comparing `mbapy-0.0.8/LICENSE` & `mbapy-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `mbapy-0.0.8/PKG-INFO` & `mbapy-0.0.9/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mbapy
-Version: 0.0.8
+Version: 0.0.9
 Summary: MyBA in Python
 Home-page: https://github.com/BHM-Bob/BA_PY
 Author: BHM-Bob G
 Author-email: bhmfly@foxmail.com
 License: MIT Licence
 Keywords: mbapy,Utilities,plot
 Platform: any
@@ -21,15 +21,15 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <!--
  * @Author: BHM-Bob 2262029386@qq.com
  * @Date: 2022-10-19 22:16:22
  * @LastEditors: BHM-Bob
- * @LastEditTime: 2022-12-09 17:23:24
+ * @LastEditTime: 2023-03-20 23:11:05
  * @Description: 
 -->
 # BA_PY
 some helpful python scripts. (Basic for All in Python)
 
 ## contain  
 ### mbapy  
@@ -43,32 +43,32 @@
 5. get_wanted_args: a func to create MyArgs from defalut_args and kwargs
 
 ##### file
 1. detect_byte_coding: decode bytes depending it's encoding
 
 ##### plot
 1. pro_bar_data: func to calcu bar data as mean value and SE value
-2. sort_df_factors: func
-3. plot_bar: func to create a stack bar plot with hue style
-4. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
-5. plot_positional_hue: wrapper to create a pos-y plot with hue style
+2. pro_bar_data_R: wrapper to calcu bar data by a usr-define func to process value
+3. sort_df_factors: func
+4. plot_bar: func to create a stack bar plot with hue style
+5. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
+6. plot_positional_hue: wrapper to create a pos-y plot with hue style
 
 
 ##### web
 *some crawler utils things*
 
 ### examples
 ##### file
 *some file utils things*
 
 ##### plot
 1. stack bar plot with hue style
 
 ##### torch
-1. seq2seq core from bentrevett / pytorch-seq2seq
-
+1. seq2seq core from bentrevett/pytorch-seq2seq
 
 ##### web/crawler
 1. chaoxin ppt multi threads downloader (jpg->pdf)
 2. wujin search http://www.basechem.org
 3. chemSub search http://chemsub.online.fr/
```

### Comparing `mbapy-0.0.8/README.md` & `mbapy-0.0.9/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 <!--
  * @Author: BHM-Bob 2262029386@qq.com
  * @Date: 2022-10-19 22:16:22
  * @LastEditors: BHM-Bob
- * @LastEditTime: 2022-12-09 17:23:24
+ * @LastEditTime: 2023-03-20 23:11:05
  * @Description: 
 -->
 # BA_PY
 some helpful python scripts. (Basic for All in Python)
 
 ## contain  
 ### mbapy  
@@ -20,32 +20,32 @@
 5. get_wanted_args: a func to create MyArgs from defalut_args and kwargs
 
 ##### file
 1. detect_byte_coding: decode bytes depending it's encoding
 
 ##### plot
 1. pro_bar_data: func to calcu bar data as mean value and SE value
-2. sort_df_factors: func
-3. plot_bar: func to create a stack bar plot with hue style
-4. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
-5. plot_positional_hue: wrapper to create a pos-y plot with hue style
+2. pro_bar_data_R: wrapper to calcu bar data by a usr-define func to process value
+3. sort_df_factors: func
+4. plot_bar: func to create a stack bar plot with hue style
+5. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
+6. plot_positional_hue: wrapper to create a pos-y plot with hue style
 
 
 ##### web
 *some crawler utils things*
 
 ### examples
 ##### file
 *some file utils things*
 
 ##### plot
 1. stack bar plot with hue style
 
 ##### torch
-1. seq2seq core from bentrevett / pytorch-seq2seq
-
+1. seq2seq core from bentrevett/pytorch-seq2seq
 
 ##### web/crawler
 1. chaoxin ppt multi threads downloader (jpg->pdf)
 2. wujin search http://www.basechem.org
 3. chemSub search http://chemsub.online.fr/
```

### Comparing `mbapy-0.0.8/mbapy/base.py` & `mbapy-0.0.9/mbapy/base.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,21 @@
+'''
+Author: BHM-Bob 2262029386@qq.com
+Date: 2022-10-19 22:46:30
+LastEditors: BHM-Bob
+LastEditTime: 2023-03-21 00:36:28
+Description: 
+'''
 import sys
 import time
 from functools import wraps
 
 import numpy as np
 
+
 __NO_ERR__ = False
 
 def TimeCosts(runTimes:int = 1):
     """
     inner is func(times, *args, **kwargs)
     @TimeCosts(9)
     def f(idx, s):
@@ -51,14 +59,19 @@
             else:
                 setattr(self, arg_name, args[arg_name])
             if del_origin:
                 del args[arg_name]
         return self
     def add_arg(self, arg_name:str, arg_value, force_update = True):
         setattr(self, arg_name, arg_value)
+    def toDict(self):
+        dic = {}
+        for attr in vars(self):
+            dic[attr] = getattr(self,attr)
+        return dic   
 
 def get_wanted_args(defalut_args:dict, kwargs:dict, del_kwargs = True):
     """
     wanted_args:dict with default value
     localVar = locals()
     """
     return MyArgs(defalut_args).get_args(kwargs, True, del_kwargs)
```

### Comparing `mbapy-0.0.8/mbapy/plot.py` & `mbapy-0.0.9/mbapy/plot.py`

 * *Files 4% similar despite different names*

```diff
@@ -44,14 +44,47 @@
                 values = np.array(df.loc[factorMask, [tag]])
                 line.append(values.mean())
                 line.append(values.std(ddof = 1)/np.sqrt(values.shape[0]))
                 line.append(values.shape[0])
             ndf.append(list(factorCombi) + line)
     return pd.DataFrame(ndf[1:], columns=ndf[0])
 
+def pro_bar_data_R(factors:list[str], tags:list[str], df:pd.DataFrame, suffixs:list[str], **kwargs):
+    """
+    wrapper\n
+    @pro_bar_data_R(['solution', 'type'], ['root', 'leaf'], ndf)\n
+    def plot_func(values, **kwargs):
+        return produced vars in list format whose length equal to len(suffix)
+    """
+    def ret_wrapper(core_func):
+        def core_wrapper(**kwargs):
+            nonlocal tags
+            if len(tags) == 0:
+                tags = list(df.columns)[len(factors):]
+            factor_contents:list[list[str]] = [ df[f].unique().tolist() for f in factors ]
+            ndf = [factors.copy()]
+            for tag in tags:
+                for suffix in suffixs:
+                    ndf[0] += [tag+suffix]
+            for factorCombi in itertools.product(*factor_contents):
+                factorMask = np.array(df[factors[0]] == factorCombi[0])
+                for i in range(1, len(factors)):
+                    factorMask &= np.array(df[factors[i]] == factorCombi[i])
+                if(factorMask.sum() > 0):
+                    line = []
+                    for idx, tag in enumerate(tags):
+                        values = np.array(df.loc[factorMask, [tag]])
+                        ret_line = core_func(values)
+                        assert len(ret_line) == len(suffixs), 'length of return value of core_func != len(suffixs)'
+                        line += ret_line
+                    ndf.append(list(factorCombi) + line)
+            return pd.DataFrame(ndf[1:], columns=ndf[0])
+        return core_wrapper
+    return ret_wrapper
+
 def get_df_data(factors:dict[str, list[str]], tags:list[str], df:pd.DataFrame,
                 include_factors:bool = True):
     #sub_df = ndf.loc[(ndf['size'] == size1) & (ndf['light'] == light1), ['c', 'w', 'SE']]
     #sub_df = get_df_data([{'size':[size1], 'light':[light1]}, ['c', 'w', 'SE'])
     def update_mask(mask, other:np.ndarray, method:str = '&'):
         return other if mask is None else (mask&other if method == '&' else mask|other)
     if include_factors:
```

### Comparing `mbapy-0.0.8/mbapy/stats/geography.py` & `mbapy-0.0.9/mbapy/stats/geography.py`

 * *Files identical despite different names*

### Comparing `mbapy-0.0.8/mbapy/web.py` & `mbapy-0.0.9/mbapy/web.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 import _thread
 import http.cookiejar
-import json
 import os
 import re
 import time
 import urllib.error
 import urllib.parse
 import urllib.request
 from queue import Queue
@@ -13,26 +12,27 @@
 from bs4 import BeautifulSoup
 from selenium.webdriver.common.action_chains import ActionChains
 from selenium.webdriver.common.by import By
 from selenium.webdriver.support import expected_conditions as EC
 from selenium.webdriver.support.ui import WebDriverWait
 
 from mbapy.base import put_err
+from mbapy.file import save_json, read_json, save_excel, read_excel
 
 CHROMEDRIVERPATH = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
 
 def get_url_page(url:str, coding = 'gbk'):
     req = urllib.request.Request(url)
     # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
     # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63
     req.add_header("User-Agent",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
     urllib.request.install_opener(opener)
-    return opener.open(url,timeout = 30).read().decode(coding,errors = 'ignore')
+    return opener.open(req,timeout = 30).read().decode(coding,errors = 'ignore')
 def get_url_page_s(url:str, coding = 'gbk'):
     try:
         return get_url_page(url, coding)
     except:
         return '-html-None'
 def get_url_page(url:str, return_html_text:bool = False, debug:bool = False, coding = 'gbk'):
     if debug:
@@ -45,38 +45,14 @@
 def get_url_page(browser, url:str, return_html_text:bool = False, debug = False):
     browser.get(url)
     html = browser.page_source
     if return_html_text:
         return BeautifulSoup(html, 'html.parser'), html
     return BeautifulSoup(html, 'html.parser')
 
-
-def save_json(path:str, obj, encoding:str = 'utf-8', forceUpdate = True):
-    if forceUpdate or not os.path.isfile(path):
-        json_str = json.dumps(obj, indent=1)
-        with open(path, 'w' ,encoding=encoding, errors='ignore') as json_file:
-            json_file.write(json_str)
-def read_json(path:str, encoding:str = 'utf-8', invalidPathReturn = None):
-    if os.path.isfile(path):
-        with open(path, 'r' ,encoding=encoding, errors='ignore') as json_file:
-            json_str = json_file.read()
-        return json.loads(json_str)
-    return invalidPathReturn
-def save_excel(path:str, obj:list[list[str]], columns:list[str], encoding:str = 'utf-8', forceUpdate = True):
-    if forceUpdate or not os.path.isfile(path):
-        df = pd.DataFrame(obj, columns=columns)
-        df.to_excel(path, encoding = encoding)
-def read_excel(path:str, ignoreHead:bool = True,
-                  ignoreFirstCol:bool = True, invalidPathReturn = None):
-    if os.path.isfile(path):
-        df = pd.read_excel(path, )
-        return df
-    return invalidPathReturn
-
-
 def get_between(string:str, head:str, tail:str,
                headRFind:bool = False, tailRFind:bool = True,
                retHead:bool = False, retTail:bool = False):
     headIdx = string.rfind(head) if headRFind else string.find(head)
     tailIdx = string.rfind(tail) if tailRFind else string.find(tail)
     if headIdx == -1 or tailIdx == -1:
         return put_err(f"{head if headIdx == -1 else tail:s} not found, return string", string)
```

### Comparing `mbapy-0.0.8/mbapy.egg-info/PKG-INFO` & `mbapy-0.0.9/mbapy.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mbapy
-Version: 0.0.8
+Version: 0.0.9
 Summary: MyBA in Python
 Home-page: https://github.com/BHM-Bob/BA_PY
 Author: BHM-Bob G
 Author-email: bhmfly@foxmail.com
 License: MIT Licence
 Keywords: mbapy,Utilities,plot
 Platform: any
@@ -21,15 +21,15 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <!--
  * @Author: BHM-Bob 2262029386@qq.com
  * @Date: 2022-10-19 22:16:22
  * @LastEditors: BHM-Bob
- * @LastEditTime: 2022-12-09 17:23:24
+ * @LastEditTime: 2023-03-20 23:11:05
  * @Description: 
 -->
 # BA_PY
 some helpful python scripts. (Basic for All in Python)
 
 ## contain  
 ### mbapy  
@@ -43,32 +43,32 @@
 5. get_wanted_args: a func to create MyArgs from defalut_args and kwargs
 
 ##### file
 1. detect_byte_coding: decode bytes depending it's encoding
 
 ##### plot
 1. pro_bar_data: func to calcu bar data as mean value and SE value
-2. sort_df_factors: func
-3. plot_bar: func to create a stack bar plot with hue style
-4. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
-5. plot_positional_hue: wrapper to create a pos-y plot with hue style
+2. pro_bar_data_R: wrapper to calcu bar data by a usr-define func to process value
+3. sort_df_factors: func
+4. plot_bar: func to create a stack bar plot with hue style
+5. get_df_data: func to make extracting data from dataFrame more easily based on df.loc
+6. plot_positional_hue: wrapper to create a pos-y plot with hue style
 
 
 ##### web
 *some crawler utils things*
 
 ### examples
 ##### file
 *some file utils things*
 
 ##### plot
 1. stack bar plot with hue style
 
 ##### torch
-1. seq2seq core from bentrevett / pytorch-seq2seq
-
+1. seq2seq core from bentrevett/pytorch-seq2seq
 
 ##### web/crawler
 1. chaoxin ppt multi threads downloader (jpg->pdf)
 2. wujin search http://www.basechem.org
 3. chemSub search http://chemsub.online.fr/
```

### Comparing `mbapy-0.0.8/setup.py` & `mbapy-0.0.9/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 '''
 Author: BHM-Bob 2262029386@qq.com
 Date: 2022-11-01 18:30:01
 LastEditors: BHM-Bob
-LastEditTime: 2022-12-15 01:41:58
+LastEditTime: 2023-03-21 00:37:37
 Description: 
 '''
 """
 something is from https://github.com/pypa/sampleproject
 thanks to https://zetcode.com/python/package/
 """
 
@@ -50,15 +50,15 @@
     "selenium>=4.2.0",
     "urllib3>=1.22.12",
     "openpyxl",
 ]
 
 setup(
     name = "mbapy",
-    version = "0.0.8",
+    version = "0.0.9",
 
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Science/Research",
         "Topic :: Utilities",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
@@ -78,17 +78,17 @@
     license = "MIT Licence",
 
     url = "https://github.com/BHM-Bob/BA_PY",
     author = "BHM-Bob G",
     author_email = "bhmfly@foxmail.com",
     
     # packages=["mbapy"],
-    packages=["mbapy", "mbapy/stats"],
+    packages=["mbapy", "mbapy/stats", "mbapy/dl_torch"],
     
     include_package_data = True,
     platforms = "any",
     
     install_requires=requires,
 )
 
 # python setup.py sdist
-# twine upload dist/*
+# twine upload dist/mbapy-0.0.8.tar.gz
```

