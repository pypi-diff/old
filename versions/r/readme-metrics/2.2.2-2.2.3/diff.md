# Comparing `tmp/readme-metrics-2.2.2.tar.gz` & `tmp/readme-metrics-2.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "readme-metrics-2.2.2.tar", last modified: Fri Sep  2 13:14:16 2022, max compression
+gzip compressed data, was "readme-metrics-2.2.3.tar", last modified: Thu Apr  6 16:06:17 2023, max compression
```

## Comparing `readme-metrics-2.2.2.tar` & `readme-metrics-2.2.3.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 domh       (501) staff       (20)        0 2022-09-02 13:14:16.370689 readme-metrics-2.2.2/
--rw-r--r--   0 domh       (501) staff       (20)      725 2022-08-22 12:38:51.000000 readme-metrics-2.2.2/LICENSE
--rw-r--r--   0 domh       (501) staff       (20)     2394 2022-09-02 13:14:16.370550 readme-metrics-2.2.2/PKG-INFO
--rw-r--r--   0 domh       (501) staff       (20)     2071 2022-09-02 13:07:45.000000 readme-metrics-2.2.2/README.md
-drwxr-xr-x   0 domh       (501) staff       (20)        0 2022-09-02 13:14:16.369608 readme-metrics-2.2.2/readme_metrics/
--rw-r--r--   0 domh       (501) staff       (20)     3856 2022-09-02 13:07:45.000000 readme-metrics-2.2.2/readme_metrics/Metrics.py
--rw-r--r--   0 domh       (501) staff       (20)     5998 2022-09-02 13:07:45.000000 readme-metrics-2.2.2/readme_metrics/MetricsApiConfig.py
--rw-r--r--   0 domh       (501) staff       (20)     4225 2022-08-22 12:38:51.000000 readme-metrics-2.2.2/readme_metrics/MetricsMiddleware.py
--rw-r--r--   0 domh       (501) staff       (20)    14191 2022-09-02 13:07:45.000000 readme-metrics-2.2.2/readme_metrics/PayloadBuilder.py
--rw-r--r--   0 domh       (501) staff       (20)     1246 2022-04-13 15:12:08.000000 readme-metrics-2.2.2/readme_metrics/ResponseInfoWrapper.py
--rw-r--r--   0 domh       (501) staff       (20)     1058 2022-08-22 12:38:51.000000 readme-metrics-2.2.2/readme_metrics/VerifyWebhook.py
--rw-r--r--   0 domh       (501) staff       (20)      147 2022-09-02 13:13:24.000000 readme-metrics-2.2.2/readme_metrics/__init__.py
--rw-r--r--   0 domh       (501) staff       (20)     1868 2022-09-02 13:07:45.000000 readme-metrics-2.2.2/readme_metrics/django.py
--rw-r--r--   0 domh       (501) staff       (20)     2021 2022-08-24 14:21:21.000000 readme-metrics-2.2.2/readme_metrics/flask_readme.py
--rw-r--r--   0 domh       (501) staff       (20)     1536 2022-08-31 12:21:18.000000 readme-metrics-2.2.2/readme_metrics/publisher.py
--rw-r--r--   0 domh       (501) staff       (20)      357 2022-08-31 17:15:21.000000 readme-metrics-2.2.2/readme_metrics/util.py
-drwxr-xr-x   0 domh       (501) staff       (20)        0 2022-09-02 13:14:16.370345 readme-metrics-2.2.2/readme_metrics.egg-info/
--rw-r--r--   0 domh       (501) staff       (20)     2394 2022-09-02 13:14:16.000000 readme-metrics-2.2.2/readme_metrics.egg-info/PKG-INFO
--rw-r--r--   0 domh       (501) staff       (20)      549 2022-09-02 13:14:16.000000 readme-metrics-2.2.2/readme_metrics.egg-info/SOURCES.txt
--rw-r--r--   0 domh       (501) staff       (20)        1 2022-09-02 13:14:16.000000 readme-metrics-2.2.2/readme_metrics.egg-info/dependency_links.txt
--rw-r--r--   0 domh       (501) staff       (20)       50 2022-09-02 13:14:16.000000 readme-metrics-2.2.2/readme_metrics.egg-info/requires.txt
--rw-r--r--   0 domh       (501) staff       (20)       15 2022-09-02 13:14:16.000000 readme-metrics-2.2.2/readme_metrics.egg-info/top_level.txt
--rw-r--r--   0 domh       (501) staff       (20)       38 2022-09-02 13:14:16.370751 readme-metrics-2.2.2/setup.cfg
--rw-r--r--   0 domh       (501) staff       (20)      650 2022-08-22 12:38:51.000000 readme-metrics-2.2.2/setup.py
+drwxr-xr-x   0 domh       (501) staff       (20)        0 2023-04-06 16:06:17.022446 readme-metrics-2.2.3/
+-rw-r--r--   0 domh       (501) staff       (20)      725 2022-08-22 12:38:51.000000 readme-metrics-2.2.3/LICENSE
+-rw-r--r--   0 domh       (501) staff       (20)     2414 2023-04-06 16:06:17.022322 readme-metrics-2.2.3/PKG-INFO
+-rw-r--r--   0 domh       (501) staff       (20)     2091 2023-02-22 13:36:42.000000 readme-metrics-2.2.3/README.md
+drwxr-xr-x   0 domh       (501) staff       (20)        0 2023-04-06 16:06:17.021519 readme-metrics-2.2.3/readme_metrics/
+-rw-r--r--   0 domh       (501) staff       (20)     3856 2022-09-06 16:49:05.000000 readme-metrics-2.2.3/readme_metrics/Metrics.py
+-rw-r--r--   0 domh       (501) staff       (20)     5998 2022-09-06 16:49:05.000000 readme-metrics-2.2.3/readme_metrics/MetricsApiConfig.py
+-rw-r--r--   0 domh       (501) staff       (20)     4225 2022-08-22 12:38:51.000000 readme-metrics-2.2.3/readme_metrics/MetricsMiddleware.py
+-rw-r--r--   0 domh       (501) staff       (20)    14362 2022-09-15 09:53:54.000000 readme-metrics-2.2.3/readme_metrics/PayloadBuilder.py
+-rw-r--r--   0 domh       (501) staff       (20)     1246 2022-04-13 15:12:08.000000 readme-metrics-2.2.3/readme_metrics/ResponseInfoWrapper.py
+-rw-r--r--   0 domh       (501) staff       (20)     1058 2022-08-22 12:38:51.000000 readme-metrics-2.2.3/readme_metrics/VerifyWebhook.py
+-rw-r--r--   0 domh       (501) staff       (20)      147 2023-04-06 16:02:26.000000 readme-metrics-2.2.3/readme_metrics/__init__.py
+-rw-r--r--   0 domh       (501) staff       (20)     1868 2022-09-06 16:49:05.000000 readme-metrics-2.2.3/readme_metrics/django.py
+-rw-r--r--   0 domh       (501) staff       (20)     2021 2022-08-24 14:21:21.000000 readme-metrics-2.2.3/readme_metrics/flask_readme.py
+-rw-r--r--   0 domh       (501) staff       (20)     1565 2023-02-22 13:36:42.000000 readme-metrics-2.2.3/readme_metrics/publisher.py
+-rw-r--r--   0 domh       (501) staff       (20)      357 2022-09-06 09:57:52.000000 readme-metrics-2.2.3/readme_metrics/util.py
+drwxr-xr-x   0 domh       (501) staff       (20)        0 2023-04-06 16:06:17.022146 readme-metrics-2.2.3/readme_metrics.egg-info/
+-rw-r--r--   0 domh       (501) staff       (20)     2414 2023-04-06 16:06:16.000000 readme-metrics-2.2.3/readme_metrics.egg-info/PKG-INFO
+-rw-r--r--   0 domh       (501) staff       (20)      549 2023-04-06 16:06:16.000000 readme-metrics-2.2.3/readme_metrics.egg-info/SOURCES.txt
+-rw-r--r--   0 domh       (501) staff       (20)        1 2023-04-06 16:06:16.000000 readme-metrics-2.2.3/readme_metrics.egg-info/dependency_links.txt
+-rw-r--r--   0 domh       (501) staff       (20)       50 2023-04-06 16:06:16.000000 readme-metrics-2.2.3/readme_metrics.egg-info/requires.txt
+-rw-r--r--   0 domh       (501) staff       (20)       15 2023-04-06 16:06:16.000000 readme-metrics-2.2.3/readme_metrics.egg-info/top_level.txt
+-rw-r--r--   0 domh       (501) staff       (20)       38 2023-04-06 16:06:17.022498 readme-metrics-2.2.3/setup.cfg
+-rw-r--r--   0 domh       (501) staff       (20)      650 2022-08-22 12:38:51.000000 readme-metrics-2.2.3/setup.py
```

### Comparing `readme-metrics-2.2.2/LICENSE` & `readme-metrics-2.2.3/LICENSE`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/PKG-INFO` & `readme-metrics-2.2.3/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: readme-metrics
-Version: 2.2.2
+Version: 2.2.3
 Summary: ReadMe API Metrics SDK
 Home-page: https://github.com/readmeio/metrics-sdks/tree/main/packages/python
 Author: ReadMe
 Author-email: support@readme.io
 Description-Content-Type: text/markdown
 Provides-Extra: Flask
 Provides-Extra: Django
@@ -18,15 +18,15 @@
 
 <p align="center">
   Track usage of your API and troubleshoot issues faster.
 </p>
 
 <p align="center">
   <a href="https://pypi.org/project/readme-metrics/"><img src="https://img.shields.io/pypi/v/readme-metrics.svg?style=for-the-badge" alt="Latest release"></a>
-  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/workflow/status/readmeio/metrics-sdks/python.svg?style=for-the-badge" alt="Build status"></a>
+  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/actions/workflow/status/readmeio/metrics-sdks/python.yml?branch=main&style=for-the-badge" alt="Build status"></a>
 </p>
 
 With [ReadMe's Metrics API](https://readme.com/metrics) your team can get deep insights into your API's usage. If you're a developer, it takes a few small steps to send your API logs to [ReadMe](http://readme.com). Here's an overview of how the integration works:
 
 - You add the ReadMe middleware to your [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/), or [WSGI](https://wsgi.readthedocs.io/) application.
 - The middleware sends to ReadMe the response object that your application generates each time a user makes a request to your API. The entire response is sent, unless you allow or deny keys.
 - ReadMe populates Metrics with this information, such as which endpoint is being called, response code, and error messages. It also identifies the customer who called your API, using whichever keys in the middleware you call out as containing relevant customer info.
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: readme-metrics Version: 2.2.2 Summary: ReadMe API
+Metadata-Version: 2.1 Name: readme-metrics Version: 2.2.3 Summary: ReadMe API
 Metrics SDK Home-page: https://github.com/readmeio/metrics-sdks/tree/main/
 packages/python Author: ReadMe Author-email: support@readme.io Description-
 Content-Type: text/markdown Provides-Extra: Flask Provides-Extra: Django
 License-File: LICENSE # ReadMe Metrics
 [https://user-images.githubusercontent.com/33762/182927634-2aebeb46-c215-4ac3-
                             9e98-61f931e33583.png]
             Track usage of your API and troubleshoot issues faster.
```

### Comparing `readme-metrics-2.2.2/README.md` & `readme-metrics-2.2.3/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 
 <p align="center">
   Track usage of your API and troubleshoot issues faster.
 </p>
 
 <p align="center">
   <a href="https://pypi.org/project/readme-metrics/"><img src="https://img.shields.io/pypi/v/readme-metrics.svg?style=for-the-badge" alt="Latest release"></a>
-  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/workflow/status/readmeio/metrics-sdks/python.svg?style=for-the-badge" alt="Build status"></a>
+  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/actions/workflow/status/readmeio/metrics-sdks/python.yml?branch=main&style=for-the-badge" alt="Build status"></a>
 </p>
 
 With [ReadMe's Metrics API](https://readme.com/metrics) your team can get deep insights into your API's usage. If you're a developer, it takes a few small steps to send your API logs to [ReadMe](http://readme.com). Here's an overview of how the integration works:
 
 - You add the ReadMe middleware to your [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/), or [WSGI](https://wsgi.readthedocs.io/) application.
 - The middleware sends to ReadMe the response object that your application generates each time a user makes a request to your API. The entire response is sent, unless you allow or deny keys.
 - ReadMe populates Metrics with this information, such as which endpoint is being called, response code, and error messages. It also identifies the customer who called your API, using whichever keys in the middleware you call out as containing relevant customer info.
```

### Comparing `readme-metrics-2.2.2/readme_metrics/Metrics.py` & `readme-metrics-2.2.3/readme_metrics/Metrics.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/MetricsApiConfig.py` & `readme-metrics-2.2.3/readme_metrics/MetricsApiConfig.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/MetricsMiddleware.py` & `readme-metrics-2.2.3/readme_metrics/MetricsMiddleware.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/PayloadBuilder.py` & `readme-metrics-2.2.3/readme_metrics/PayloadBuilder.py`

 * *Files 4% similar despite different names*

```diff
@@ -199,15 +199,18 @@
                 post_data = self._process_body(content_type, request.rm_body)
 
         payload = {
             "method": request.method,
             "url": self._build_base_url(request),
             "httpVersion": request.environ["SERVER_PROTOCOL"],
             "headers": [{"name": k, "value": v} for (k, v) in headers.items()],
+            "headersSize": -1,
             "queryString": [{"name": k, "value": v} for (k, v) in queryString],
+            "cookies": [],
+            "bodySize": -1,
         }
 
         if not post_data is False:
             payload["postData"] = post_data
 
         return payload
 
@@ -230,14 +233,16 @@
         status_code = int(status_string.split(" ")[0])
         status_text = status_string.replace(str(status_code) + " ", "")
 
         return {
             "status": status_code,
             "statusText": status_text or "",
             "headers": headers,
+            "headersSize": -1,
+            "bodySize": int(response.content_length),
             "content": {
                 "text": body,
                 "size": int(response.content_length),
                 "mimeType": response.content_type,
             },
         }
```

### Comparing `readme-metrics-2.2.2/readme_metrics/ResponseInfoWrapper.py` & `readme-metrics-2.2.3/readme_metrics/ResponseInfoWrapper.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/VerifyWebhook.py` & `readme-metrics-2.2.3/readme_metrics/VerifyWebhook.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/django.py` & `readme-metrics-2.2.3/readme_metrics/django.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/flask_readme.py` & `readme-metrics-2.2.3/readme_metrics/flask_readme.py`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/readme_metrics/publisher.py` & `readme-metrics-2.2.3/readme_metrics/publisher.py`

 * *Files 6% similar despite different names*

```diff
@@ -18,15 +18,17 @@
         except Empty:
             pass
 
         if len(result_list) == 0:
             return
 
         version = importlib.import_module(__package__).__version__
-        url = urljoin(os.getenv("METRICS_SERVER", config.METRICS_API), "/v1/request")
+        url = urljoin(
+            os.getenv("README_METRICS_SERVER", config.METRICS_API), "/v1/request"
+        )
 
         readme_result = requests.post(
             url,
             auth=(config.README_API_KEY, ""),
             data=json.dumps(result_list),
             headers={
                 "Content-Type": "application/json",
```

### Comparing `readme-metrics-2.2.2/readme_metrics.egg-info/PKG-INFO` & `readme-metrics-2.2.3/readme_metrics.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: readme-metrics
-Version: 2.2.2
+Version: 2.2.3
 Summary: ReadMe API Metrics SDK
 Home-page: https://github.com/readmeio/metrics-sdks/tree/main/packages/python
 Author: ReadMe
 Author-email: support@readme.io
 Description-Content-Type: text/markdown
 Provides-Extra: Flask
 Provides-Extra: Django
@@ -18,15 +18,15 @@
 
 <p align="center">
   Track usage of your API and troubleshoot issues faster.
 </p>
 
 <p align="center">
   <a href="https://pypi.org/project/readme-metrics/"><img src="https://img.shields.io/pypi/v/readme-metrics.svg?style=for-the-badge" alt="Latest release"></a>
-  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/workflow/status/readmeio/metrics-sdks/python.svg?style=for-the-badge" alt="Build status"></a>
+  <a href="https://github.com/readmeio/metrics-sdks"><img src="https://img.shields.io/github/actions/workflow/status/readmeio/metrics-sdks/python.yml?branch=main&style=for-the-badge" alt="Build status"></a>
 </p>
 
 With [ReadMe's Metrics API](https://readme.com/metrics) your team can get deep insights into your API's usage. If you're a developer, it takes a few small steps to send your API logs to [ReadMe](http://readme.com). Here's an overview of how the integration works:
 
 - You add the ReadMe middleware to your [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/), or [WSGI](https://wsgi.readthedocs.io/) application.
 - The middleware sends to ReadMe the response object that your application generates each time a user makes a request to your API. The entire response is sent, unless you allow or deny keys.
 - ReadMe populates Metrics with this information, such as which endpoint is being called, response code, and error messages. It also identifies the customer who called your API, using whichever keys in the middleware you call out as containing relevant customer info.
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: readme-metrics Version: 2.2.2 Summary: ReadMe API
+Metadata-Version: 2.1 Name: readme-metrics Version: 2.2.3 Summary: ReadMe API
 Metrics SDK Home-page: https://github.com/readmeio/metrics-sdks/tree/main/
 packages/python Author: ReadMe Author-email: support@readme.io Description-
 Content-Type: text/markdown Provides-Extra: Flask Provides-Extra: Django
 License-File: LICENSE # ReadMe Metrics
 [https://user-images.githubusercontent.com/33762/182927634-2aebeb46-c215-4ac3-
                             9e98-61f931e33583.png]
             Track usage of your API and troubleshoot issues faster.
```

### Comparing `readme-metrics-2.2.2/readme_metrics.egg-info/SOURCES.txt` & `readme-metrics-2.2.3/readme_metrics.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `readme-metrics-2.2.2/setup.py` & `readme-metrics-2.2.3/setup.py`

 * *Files identical despite different names*

