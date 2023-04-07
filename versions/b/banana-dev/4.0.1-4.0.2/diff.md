# Comparing `tmp/banana_dev-4.0.1.tar.gz` & `tmp/banana_dev-4.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "banana_dev-4.0.1.tar", last modified: Wed Jan 11 00:31:33 2023, max compression
+gzip compressed data, was "banana_dev-4.0.2.tar", last modified: Fri Apr  7 03:09:55 2023, max compression
```

## Comparing `banana_dev-4.0.1.tar` & `banana_dev-4.0.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-01-11 00:31:33.070524 banana_dev-4.0.1/
--rw-r--r--   0 erik       (501) staff       (20)     1591 2023-01-11 00:31:33.070597 banana_dev-4.0.1/PKG-INFO
--rw-r--r--   0 erik       (501) staff       (20)      931 2022-04-14 01:45:27.000000 banana_dev-4.0.1/README.md
-drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-01-11 00:31:33.069704 banana_dev-4.0.1/banana_dev/
--rw-r--r--   0 erik       (501) staff       (20)       38 2022-11-04 12:23:27.000000 banana_dev-4.0.1/banana_dev/__init__.py
--rw-r--r--   0 erik       (501) staff       (20)     3057 2023-01-11 00:24:31.000000 banana_dev-4.0.1/banana_dev/generics.py
--rw-r--r--   0 erik       (501) staff       (20)      571 2022-11-04 12:23:27.000000 banana_dev-4.0.1/banana_dev/package.py
-drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-01-11 00:31:33.070431 banana_dev-4.0.1/banana_dev.egg-info/
--rw-r--r--   0 erik       (501) staff       (20)     1591 2023-01-11 00:31:33.000000 banana_dev-4.0.1/banana_dev.egg-info/PKG-INFO
--rw-r--r--   0 erik       (501) staff       (20)      265 2023-01-11 00:31:33.000000 banana_dev-4.0.1/banana_dev.egg-info/SOURCES.txt
--rw-r--r--   0 erik       (501) staff       (20)        1 2023-01-11 00:31:33.000000 banana_dev-4.0.1/banana_dev.egg-info/dependency_links.txt
--rw-r--r--   0 erik       (501) staff       (20)       24 2023-01-11 00:31:33.000000 banana_dev-4.0.1/banana_dev.egg-info/requires.txt
--rw-r--r--   0 erik       (501) staff       (20)       11 2023-01-11 00:31:33.000000 banana_dev-4.0.1/banana_dev.egg-info/top_level.txt
--rw-r--r--   0 erik       (501) staff       (20)       79 2023-01-11 00:31:33.070826 banana_dev-4.0.1/setup.cfg
--rw-r--r--   0 erik       (501) staff       (20)     1235 2023-01-11 00:23:55.000000 banana_dev-4.0.1/setup.py
+drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-04-07 03:09:55.032023 banana_dev-4.0.2/
+-rw-r--r--   0 erik       (501) staff       (20)     1880 2023-04-07 03:09:55.032081 banana_dev-4.0.2/PKG-INFO
+-rw-r--r--   0 erik       (501) staff       (20)     1220 2023-04-07 03:03:29.000000 banana_dev-4.0.2/README.md
+drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-04-07 03:09:55.031354 banana_dev-4.0.2/banana_dev/
+-rw-r--r--   0 erik       (501) staff       (20)       38 2022-11-04 12:23:27.000000 banana_dev-4.0.2/banana_dev/__init__.py
+-rw-r--r--   0 erik       (501) staff       (20)     4193 2023-04-07 03:06:39.000000 banana_dev-4.0.2/banana_dev/generics.py
+-rw-r--r--   0 erik       (501) staff       (20)      571 2023-04-07 01:40:16.000000 banana_dev-4.0.2/banana_dev/package.py
+drwxr-xr-x   0 erik       (501) staff       (20)        0 2023-04-07 03:09:55.031933 banana_dev-4.0.2/banana_dev.egg-info/
+-rw-r--r--   0 erik       (501) staff       (20)     1880 2023-04-07 03:09:55.000000 banana_dev-4.0.2/banana_dev.egg-info/PKG-INFO
+-rw-r--r--   0 erik       (501) staff       (20)      265 2023-04-07 03:09:55.000000 banana_dev-4.0.2/banana_dev.egg-info/SOURCES.txt
+-rw-r--r--   0 erik       (501) staff       (20)        1 2023-04-07 03:09:55.000000 banana_dev-4.0.2/banana_dev.egg-info/dependency_links.txt
+-rw-r--r--   0 erik       (501) staff       (20)       24 2023-04-07 03:09:55.000000 banana_dev-4.0.2/banana_dev.egg-info/requires.txt
+-rw-r--r--   0 erik       (501) staff       (20)       11 2023-04-07 03:09:55.000000 banana_dev-4.0.2/banana_dev.egg-info/top_level.txt
+-rw-r--r--   0 erik       (501) staff       (20)       79 2023-04-07 03:09:55.032261 banana_dev-4.0.2/setup.cfg
+-rw-r--r--   0 erik       (501) staff       (20)     1235 2023-04-07 02:55:27.000000 banana_dev-4.0.2/setup.py
```

### Comparing `banana_dev-4.0.1/PKG-INFO` & `banana_dev-4.0.2/banana_dev.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: banana_dev
-Version: 4.0.1
+Name: banana-dev
+Version: 4.0.2
 Summary: The banana package is a python client to interact with your machine learning models hosted on Banana
 Home-page: https://www.banana.dev
 Author: Erik Dunteman
 Author-email: erik@banana.dev
 License: MIT
 Keywords: Banana client,API wrapper,Banana,SDK
 Classifier: Development Status :: 5 - Production/Stable
@@ -16,25 +16,37 @@
 Description-Content-Type: text/markdown
 
 # Banana Python SDK
 
 ### Getting Started
 
 Install via pip
-`pip3 install banana-dev`
+```bash
+pip3 install banana-dev
+```
 
-Get your API Key
-- [Sign in / log in here](https://app.banana.dev)
+If integration testing against a local Potassium server:
+```bash
+export BANANA_SERVER=local
+```
+to call `http://localhost:8000/` directly. Be sure to unset in prod!
+
+
+If deploying to prod:
+[Sign in / log in here](https://app.banana.dev) to get your API and Model Keys
+
+### Run:
 
-Run:
 ```python
 import banana_dev as banana
 
-api_key = "demo" # "YOUR_API_KEY"
-model_key = "carrot" # "YOUR_MODEL_KEY"
+# Your credentials. Can be empty strings if testing against a local server.
+api_key = "demo" # YOUR_API_KEY
+model_key = "carrot" # YOUR_MODEL_KEY
+
 model_inputs = {
     # a json specific to your model. For example:
     "imageURL":  "https://demo-images-banana.s3.us-west-1.amazonaws.com/image2.jpg"
 }
 
 out = banana.run(api_key, model_key, model_inputs)
 print(out)
```

### Comparing `banana_dev-4.0.1/banana_dev/generics.py` & `banana_dev-4.0.2/banana_dev/generics.py`

 * *Files 25% similar despite different names*

```diff
@@ -10,19 +10,30 @@
     print("Dev Mode")
     if os.environ['BANANA_URL'] == 'local':
         endpoint = 'http://localhost/'
     else:
         endpoint = os.environ['BANANA_URL']
     print("Hitting endpoint:", endpoint)
 
+direct_call_endpoint = "http://localhost:8000/"
+is_direct = False
+if 'BANANA_SERVER' in os.environ:
+    is_direct = True    
+    if os.getenv("BANANA_SERVER") != "local":
+        direct_call_endpoint = os.getenv("BANANA_SERVER")
+    print("Routing calls directly to server hosted at", direct_call_endpoint)
+
 # THE MAIN FUNCTIONS
 # ___________________________________
 
-
 def run_main(api_key, model_key, model_inputs):
+    # run against self-hosted potassiun server if BANANA_SERVER was set
+    if is_direct:
+        return run_direct(model_inputs)
+
     result = start_api(api_key, model_key, model_inputs)
 
     # likely we get results on first call
     if result["finished"]:
         dict_out = {
             "id": result["id"],
             "message": result["message"],
@@ -46,14 +57,34 @@
     dict_out = check_api(api_key, call_id)
     return dict_out
 
 
 # THE API CALLING FUNCTIONS
 # ________________________
 
+def run_direct(model_inputs):
+    global direct_call_endpoint
+    response = requests.post(direct_call_endpoint, json=model_inputs)
+    if response.status_code != 200:
+        raise Exception("server error: status code: {}\content: {}".format(response.status_code, response.content))
+    try:
+        out = response.json()
+    except:
+        raise Exception("server error: returned invalid json")
+    
+    # We must match the same API as the prod inference server,
+    # so wrap direct API's results in same response shape
+    return {
+        "id": str(uuid4()),
+        "message": "",
+        "created": str(int(time.time())),
+        "apiVersion": "DIRECT",
+        "modelOutputs": [out]
+    }
+
 # Takes in start params and returns the full server json response
 def start_api(api_key, model_key, model_inputs, start_only=False):
     global endpoint
     route_start = "start/v4/"
     url_start = endpoint + route_start
 
     payload = {
@@ -65,15 +96,14 @@
         "startOnly": start_only
     }
 
     response = requests.post(url_start, json=payload)
 
     if response.status_code != 200:
         raise Exception("server error: status code {}".format(response.status_code))
-
     try:
         out = response.json()
     except:
         raise Exception("server error: returned invalid json")
 
     if "error" in out['message'].lower():
         raise Exception(out['message'])
```

### Comparing `banana_dev-4.0.1/banana_dev/package.py` & `banana_dev-4.0.2/banana_dev/package.py`

 * *Files identical despite different names*

### Comparing `banana_dev-4.0.1/banana_dev.egg-info/PKG-INFO` & `banana_dev-4.0.2/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: banana-dev
-Version: 4.0.1
+Name: banana_dev
+Version: 4.0.2
 Summary: The banana package is a python client to interact with your machine learning models hosted on Banana
 Home-page: https://www.banana.dev
 Author: Erik Dunteman
 Author-email: erik@banana.dev
 License: MIT
 Keywords: Banana client,API wrapper,Banana,SDK
 Classifier: Development Status :: 5 - Production/Stable
@@ -16,25 +16,37 @@
 Description-Content-Type: text/markdown
 
 # Banana Python SDK
 
 ### Getting Started
 
 Install via pip
-`pip3 install banana-dev`
+```bash
+pip3 install banana-dev
+```
 
-Get your API Key
-- [Sign in / log in here](https://app.banana.dev)
+If integration testing against a local Potassium server:
+```bash
+export BANANA_SERVER=local
+```
+to call `http://localhost:8000/` directly. Be sure to unset in prod!
+
+
+If deploying to prod:
+[Sign in / log in here](https://app.banana.dev) to get your API and Model Keys
+
+### Run:
 
-Run:
 ```python
 import banana_dev as banana
 
-api_key = "demo" # "YOUR_API_KEY"
-model_key = "carrot" # "YOUR_MODEL_KEY"
+# Your credentials. Can be empty strings if testing against a local server.
+api_key = "demo" # YOUR_API_KEY
+model_key = "carrot" # YOUR_MODEL_KEY
+
 model_inputs = {
     # a json specific to your model. For example:
     "imageURL":  "https://demo-images-banana.s3.us-west-1.amazonaws.com/image2.jpg"
 }
 
 out = banana.run(api_key, model_key, model_inputs)
 print(out)
```

### Comparing `banana_dev-4.0.1/setup.py` & `banana_dev-4.0.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text()
 
 setup(
     name='banana_dev',
     packages=['banana_dev'],
-    version='4.0.1',
+    version='4.0.2',
     license='MIT',
     # Give a short description about your library
     description='The banana package is a python client to interact with your machine learning models hosted on Banana',
     long_description=long_description,
     long_description_content_type='text/markdown',
     author='Erik Dunteman',
     author_email='erik@banana.dev',
```

