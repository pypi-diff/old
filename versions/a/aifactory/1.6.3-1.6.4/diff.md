# Comparing `tmp/aifactory-1.6.3.tar.gz` & `tmp/aifactory-1.6.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aifactory-1.6.3.tar", last modified: Fri Apr  7 04:53:50 2023, max compression
+gzip compressed data, was "aifactory-1.6.4.tar", last modified: Fri Apr  7 05:21:37 2023, max compression
```

## Comparing `aifactory-1.6.3.tar` & `aifactory-1.6.4.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 04:53:50.963797 aifactory-1.6.3/
--rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 04:53:50.963668 aifactory-1.6.3/PKG-INFO
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 04:53:50.962800 aifactory-1.6.3/aifactory/
--rw-r--r--   0 kyj        (501) staff       (20)        0 2022-08-02 00:40:18.000000 aifactory-1.6.3/aifactory/__init__.py
--rw-r--r--   0 kyj        (501) staff       (20)     3743 2022-11-14 05:11:27.000000 aifactory-1.6.3/aifactory/api.py
--rw-r--r--   0 kyj        (501) staff       (20)     3710 2022-11-14 05:11:05.000000 aifactory-1.6.3/aifactory/demo.py
--rw-r--r--   0 kyj        (501) staff       (20)    14314 2023-03-30 07:01:37.000000 aifactory-1.6.3/aifactory/grade.py
--rw-r--r--   0 kyj        (501) staff       (20)     5966 2022-11-05 14:24:05.000000 aifactory-1.6.3/aifactory/make_zip.py
--rw-r--r--   0 kyj        (501) staff       (20)     3333 2023-04-07 04:53:44.000000 aifactory-1.6.3/aifactory/score.py
-drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 04:53:50.963499 aifactory-1.6.3/aifactory.egg-info/
--rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 04:53:50.000000 aifactory-1.6.3/aifactory.egg-info/PKG-INFO
--rw-r--r--   0 kyj        (501) staff       (20)      289 2023-04-07 04:53:50.000000 aifactory-1.6.3/aifactory.egg-info/SOURCES.txt
--rw-r--r--   0 kyj        (501) staff       (20)        1 2023-04-07 04:53:50.000000 aifactory-1.6.3/aifactory.egg-info/dependency_links.txt
--rw-r--r--   0 kyj        (501) staff       (20)       41 2023-04-07 04:53:50.000000 aifactory-1.6.3/aifactory.egg-info/requires.txt
--rw-r--r--   0 kyj        (501) staff       (20)       17 2023-04-07 04:53:50.000000 aifactory-1.6.3/aifactory.egg-info/top_level.txt
--rw-r--r--   0 kyj        (501) staff       (20)       38 2023-04-07 04:53:50.963835 aifactory-1.6.3/setup.cfg
--rw-r--r--   0 kyj        (501) staff       (20)      430 2023-04-07 04:53:33.000000 aifactory-1.6.3/setup.py
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 05:21:37.236772 aifactory-1.6.4/
+-rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 05:21:37.236643 aifactory-1.6.4/PKG-INFO
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 05:21:37.235708 aifactory-1.6.4/aifactory/
+-rw-r--r--   0 kyj        (501) staff       (20)        0 2022-08-02 00:40:18.000000 aifactory-1.6.4/aifactory/__init__.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3743 2022-11-14 05:11:27.000000 aifactory-1.6.4/aifactory/api.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3710 2022-11-14 05:11:05.000000 aifactory-1.6.4/aifactory/demo.py
+-rw-r--r--   0 kyj        (501) staff       (20)    14314 2023-03-30 07:01:37.000000 aifactory-1.6.4/aifactory/grade.py
+-rw-r--r--   0 kyj        (501) staff       (20)     5966 2022-11-05 14:24:05.000000 aifactory-1.6.4/aifactory/make_zip.py
+-rw-r--r--   0 kyj        (501) staff       (20)     3360 2023-04-07 05:11:03.000000 aifactory-1.6.4/aifactory/score.py
+drwxr-xr-x   0 kyj        (501) staff       (20)        0 2023-04-07 05:21:37.236444 aifactory-1.6.4/aifactory.egg-info/
+-rw-r--r--   0 kyj        (501) staff       (20)      228 2023-04-07 05:21:37.000000 aifactory-1.6.4/aifactory.egg-info/PKG-INFO
+-rw-r--r--   0 kyj        (501) staff       (20)      289 2023-04-07 05:21:37.000000 aifactory-1.6.4/aifactory.egg-info/SOURCES.txt
+-rw-r--r--   0 kyj        (501) staff       (20)        1 2023-04-07 05:21:37.000000 aifactory-1.6.4/aifactory.egg-info/dependency_links.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       41 2023-04-07 05:21:37.000000 aifactory-1.6.4/aifactory.egg-info/requires.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       17 2023-04-07 05:21:37.000000 aifactory-1.6.4/aifactory.egg-info/top_level.txt
+-rw-r--r--   0 kyj        (501) staff       (20)       38 2023-04-07 05:21:37.236848 aifactory-1.6.4/setup.cfg
+-rw-r--r--   0 kyj        (501) staff       (20)      430 2023-04-07 05:20:56.000000 aifactory-1.6.4/setup.py
```

### Comparing `aifactory-1.6.3/aifactory/api.py` & `aifactory-1.6.4/aifactory/api.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.3/aifactory/demo.py` & `aifactory-1.6.4/aifactory/demo.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.3/aifactory/grade.py` & `aifactory-1.6.4/aifactory/grade.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.3/aifactory/make_zip.py` & `aifactory-1.6.4/aifactory/make_zip.py`

 * *Files identical despite different names*

### Comparing `aifactory-1.6.3/aifactory/score.py` & `aifactory-1.6.4/aifactory/score.py`

 * *Files 1% similar despite different names*

```diff
@@ -77,14 +77,15 @@
 
 def submit_test(model_name, key, main_name, func):
   make_zip(key, main_name, func)
   
   try:
     values = {"key": key, "modelname": model_name}
     res = requests.post(bridge_test_url, files = {'file': open("./aif.zip",'rb', )}, data=values)  
+    res.raise_for_status()
     if res.status_code == 200 or res.status_code == 201: 
       print(res.text)
       requestID = res.text
       while True:
         try:
           res = requests.get(api_test_url + requestID)  
           data_json = json.loads(res.text)
```

