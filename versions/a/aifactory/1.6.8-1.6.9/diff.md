# Comparing `tmp/aifactory-1.6.8.tar.gz` & `tmp/aifactory-1.6.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aifactory-1.6.8.tar", last modified: Fri Apr  7 06:45:08 2023, max compression
+gzip compressed data, was "aifactory-1.6.9.tar", last modified: Fri Apr  7 08:24:30 2023, max compression
```

## Comparing `aifactory-1.6.8.tar` & `aifactory-1.6.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 06:45:08.930703 aifactory-1.6.8/
--rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 06:45:08.930558 aifactory-1.6.8/PKG-INFO
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 06:45:08.929474 aifactory-1.6.8/aifactory/
--rw-r--r--   0 kyj        (501) staff       (20)        0 2022-08-02 00:40:18.000000 aifactory-1.6.8/aifactory/__init__.py
--rw-r--r--   0 kyj        (501) staff       (20)     3743 2022-11-14 05:11:27.000000 aifactory-1.6.8/aifactory/api.py
--rw-r--r--   0 kyj        (501) staff       (20)     3710 2022-11-14 05:11:05.000000 aifactory-1.6.8/aifactory/demo.py
--rw-r--r--   0 kyj        (501) staff       (20)    14314 2023-03-30 07:01:37.000000 aifactory-1.6.8/aifactory/grade.py
--rw-r--r--   0 kyj        (501) staff       (20)     5966 2022-11-05 14:24:05.000000 aifactory-1.6.8/aifactory/make_zip.py
--rw-r--r--   0 kyj        (501) staff       (20)     3312 2023-04-07 06:43:22.000000 aifactory-1.6.8/aifactory/score.py
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 06:45:08.930367 aifactory-1.6.8/aifactory.egg-info/
--rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 06:45:08.000000 aifactory-1.6.8/aifactory.egg-info/PKG-INFO
--rw-r--r--   0 kyj        (501) staff       (20)      289 2023-04-07 06:45:08.000000 aifactory-1.6.8/aifactory.egg-info/SOURCES.txt
--rw-r--r--   0 kyj        (501) staff       (20)        1 2023-04-07 06:45:08.000000 aifactory-1.6.8/aifactory.egg-info/dependency_links.txt
--rw-r--r--   0 kyj        (501) staff       (20)       41 2023-04-07 06:45:08.000000 aifactory-1.6.8/aifactory.egg-info/requires.txt
--rw-r--r--   0 kyj        (501) staff       (20)       17 2023-04-07 06:45:08.000000 aifactory-1.6.8/aifactory.egg-info/top_level.txt
--rw-r--r--   0 kyj        (501) staff       (20)       38 2023-04-07 06:45:08.930745 aifactory-1.6.8/setup.cfg
--rw-r--r--   0 kyj        (501) staff       (20)      430 2023-04-07 06:42:05.000000 aifactory-1.6.8/setup.py
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 08:24:30.810726 aifactory-1.6.9/
+-rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 08:24:30.810568 aifactory-1.6.9/PKG-INFO
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 08:24:30.809061 aifactory-1.6.9/aifactory/
+-rw-r--r--   0 kyj        (501) staff       (20)        0 2022-08-02 00:40:18.000000 aifactory-1.6.9/aifactory/__init__.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3743 2022-11-14 05:11:27.000000 aifactory-1.6.9/aifactory/api.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3710 2022-11-14 05:11:05.000000 aifactory-1.6.9/aifactory/demo.py
+-rw-r--r--   0 kyj        (501) staff       (20)    14314 2023-03-30 07:01:37.000000 aifactory-1.6.9/aifactory/grade.py
+-rw-r--r--   0 kyj        (501) staff       (20)     5966 2022-11-05 14:24:05.000000 aifactory-1.6.9/aifactory/make_zip.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3630 2023-04-07 08:24:18.000000 aifactory-1.6.9/aifactory/score.py
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 08:24:30.810348 aifactory-1.6.9/aifactory.egg-info/
+-rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 08:24:30.000000 aifactory-1.6.9/aifactory.egg-info/PKG-INFO
+-rw-r--r--   0 kyj        (501) staff       (20)      289 2023-04-07 08:24:30.000000 aifactory-1.6.9/aifactory.egg-info/SOURCES.txt
+-rw-r--r--   0 kyj        (501) staff       (20)        1 2023-04-07 08:24:30.000000 aifactory-1.6.9/aifactory.egg-info/dependency_links.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       41 2023-04-07 08:24:30.000000 aifactory-1.6.9/aifactory.egg-info/requires.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       17 2023-04-07 08:24:30.000000 aifactory-1.6.9/aifactory.egg-info/top_level.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       38 2023-04-07 08:24:30.811018 aifactory-1.6.9/setup.cfg
+-rw-r--r--   0 kyj        (501) staff       (20)      430 2023-04-07 08:23:50.000000 aifactory-1.6.9/setup.py
```

### Comparing `aifactory-1.6.8/aifactory/api.py` & `aifactory-1.6.9/aifactory/api.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.8/aifactory/demo.py` & `aifactory-1.6.9/aifactory/demo.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.8/aifactory/grade.py` & `aifactory-1.6.9/aifactory/grade.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.8/aifactory/make_zip.py` & `aifactory-1.6.9/aifactory/make_zip.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.8/aifactory/score.py` & `aifactory-1.6.9/aifactory/score.py`

 * *Files 6% similar despite different names*

```diff
@@ -55,23 +55,28 @@
   res = requests.post(bridge_test_url, files = {'file': open("./aif.zip",'rb', )}, data=values)  
   if res.status_code == 200 or res.status_code == 201: 
     print(res.text)
     requestID = res.text
     while True:
       try:
         res = requests.get(api_test_url + requestID)  
-        data_json = json.loads(res.text)      
-        if data_json["ct"] == 0 or data_json["ct"] == 3:
-          print(data_json["message"])
+        if res.status_code == 200:
+          data_json = json.loads(res.text)      
+          if data_json["ct"] == 0 or data_json["ct"] == 3:
+            print(data_json["message"])
+            break
+          elif data_json["ct"] == 1:          
+            print(data_json["message"], sep='', end='\r', flush=True)
+          # elif data_json["ct"] == 2:
+          #   print(data_json["message"])
+          time.sleep(10)
+        else:
+          print(res.status_code)  
+          print(res.text)
           break
-        elif data_json["ct"] == 1:          
-          print(data_json["message"], end='\r')
-        # elif data_json["ct"] == 2:
-        #   print(data_json["message"])
-        time.sleep(10)
       except Exception as e:          
         print(" error :" + str(e))
         break    
     return
   print(res.status_code)  
   print(res.text)
 
@@ -82,22 +87,27 @@
   res = requests.post(bridge_test_url, files = {'file': open("./aif.zip",'rb', )}, data=values)  
   if res.status_code == 200 or res.status_code == 201: 
     print(res.text)
     requestID = res.text
     while True:
       try:
         res = requests.get(api_test_url + requestID)  
-        data_json = json.loads(res.text)      
-        if data_json["ct"] == 0 or data_json["ct"] == 3:
-          print(data_json["message"])
+        if res.status_code == 200:
+          data_json = json.loads(res.text)      
+          if data_json["ct"] == 0 or data_json["ct"] == 3:
+            print(data_json["message"])
+            break
+          elif data_json["ct"] == 1:          
+            print(data_json["message"], end='\r')
+          # elif data_json["ct"] == 2:
+          #   print(data_json["message"])
+          time.sleep(10)
+        else:
+          print(res.status_code)  
+          print(res.text)
           break
-        elif data_json["ct"] == 1:
-          print(data_json["message"], end='\r')
-        # elif data_json["ct"] == 2:
-        #   print(data_json["message"])
-        time.sleep(10)
       except Exception as e:          
         print(" error :" + str(e))
         break    
     return
   print(res.status_code)  
   print(res.text)
```

