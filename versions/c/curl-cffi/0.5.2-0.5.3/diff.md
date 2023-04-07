# Comparing `tmp/curl_cffi-0.5.2.tar.gz` & `tmp/curl_cffi-0.5.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "curl_cffi-0.5.2.tar", last modified: Mon Apr  3 09:58:28 2023, max compression
+gzip compressed data, was "curl_cffi-0.5.3.tar", last modified: Fri Apr  7 11:14:11 2023, max compression
```

## Comparing `curl_cffi-0.5.2.tar` & `curl_cffi-0.5.3.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6164 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:58:28.959600 curl_cffi-0.5.2/curl_cffi/
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5531 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/aio.py
--rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/build.py
--rw-r--r--   0 runner    (1001) docker     (123)    12654 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/const.py
--rw-r--r--   0 runner    (1001) docker     (123)     7212 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/curl.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/curl_cffi/ffi/
--rw-r--r--   0 runner    (1001) docker     (123)     1625 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/ffi/cdef.c
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/ffi/shim.c
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/ffi/shim.h
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/curl_cffi/requests/
--rw-r--r--   0 runner    (1001) docker     (123)     1851 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/requests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8451 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/requests/cookies.py
--rw-r--r--   0 runner    (1001) docker     (123)       68 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/requests/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)    10803 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/requests/headers.py
--rw-r--r--   0 runner    (1001) docker     (123)    16849 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/curl_cffi/requests/session.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/curl_cffi.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-04-03 09:58:28.000000 curl_cffi-0.5.2/curl_cffi.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      525 2023-04-03 09:58:28.000000 curl_cffi-0.5.2/curl_cffi.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 09:58:28.000000 curl_cffi-0.5.2/curl_cffi.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-04-03 09:58:28.000000 curl_cffi-0.5.2/curl_cffi.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-03 09:58:28.000000 curl_cffi-0.5.2/curl_cffi.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2705 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 09:58:28.963600 curl_cffi-0.5.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-03 09:58:17.000000 curl_cffi-0.5.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6164 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/curl_cffi/
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5531 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/aio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/build.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12654 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/const.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7334 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/curl.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/curl_cffi/ffi/
+-rw-r--r--   0 runner    (1001) docker     (123)     1659 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/ffi/cdef.c
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/ffi/shim.c
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/ffi/shim.h
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/curl_cffi/requests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1851 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/requests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8451 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/requests/cookies.py
+-rw-r--r--   0 runner    (1001) docker     (123)       68 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/requests/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10803 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/requests/headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16941 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/curl_cffi/requests/session.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/curl_cffi.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8310 2023-04-07 11:14:11.000000 curl_cffi-0.5.3/curl_cffi.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-04-07 11:14:11.000000 curl_cffi-0.5.3/curl_cffi.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:14:11.000000 curl_cffi-0.5.3/curl_cffi.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      545 2023-04-07 11:14:11.000000 curl_cffi-0.5.3/curl_cffi.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 11:14:11.000000 curl_cffi-0.5.3/curl_cffi.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2705 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:14:11.802055 curl_cffi-0.5.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-07 11:14:03.000000 curl_cffi-0.5.3/setup.py
```

### Comparing `curl_cffi-0.5.2/LICENSE` & `curl_cffi-0.5.3/LICENSE`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/PKG-INFO` & `curl_cffi-0.5.3/curl_cffi.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: curl_cffi
-Version: 0.5.2
+Name: curl-cffi
+Version: 0.5.3
 Summary: libcurl ffi bindings for Python, with impersonation support
 Author-email: Yifei Kong <kong@yifei.me>
 License: MIT License
         
         Copyright (c) 2018 multippt
         Copyright (c) 2022 Yifei Kong
```

### Comparing `curl_cffi-0.5.2/README.md` & `curl_cffi-0.5.3/README.md`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/aio.py` & `curl_cffi-0.5.3/curl_cffi/aio.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/build.py` & `curl_cffi-0.5.3/curl_cffi/build.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/const.py` & `curl_cffi-0.5.3/curl_cffi/const.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/curl.py` & `curl_cffi-0.5.3/curl_cffi/curl.py`

 * *Files 2% similar despite different names*

```diff
@@ -63,17 +63,19 @@
         self._write_handle = None
         self._header_handle = None
         # TODO: use CURL_ERROR_SIZE
         self._error_buffer = ffi.new("char[]", 256)
         ret = lib._curl_easy_setopt(self._curl, CurlOpt.ERRORBUFFER, self._error_buffer)
         if ret != 0:
             warnings.warn(f"Failed to set error buffer")
-        if debug:
-            self.setopt(CurlOpt.VERBOSE, 1)
-            lib._curl_easy_setopt(self._curl, CurlOpt.DEBUGFUNCTION, lib.debug_function)
+        if debug: self.debug()
+
+    def debug(self):
+        self.setopt(CurlOpt.VERBOSE, 1)
+        lib._curl_easy_setopt(self._curl, CurlOpt.DEBUGFUNCTION, lib.debug_function)
 
     def __del__(self):
         self.close()
 
     def _check_error(self, errcode: int, action: str):
         error = self._get_error(errcode, action)
         if error is not None:
@@ -185,24 +187,28 @@
         # here we go
         ret = lib.curl_easy_perform(self._curl)
         self._check_error(ret, action="perform")
 
         # cleaning
         self._write_handle = None
         self._header_handle = None
+        self._body_handle = None
         if clear_headers:
             self.clear_headers()
 
     def clear_headers(self) -> int:
         ret = 0
         if self._headers != ffi.NULL:
             ret = lib.curl_slist_free_all(self._headers)
         self._headers = ffi.NULL
         return ret
 
+    def reset(self):
+        lib.curl_easy_reset(self._curl)
+
     def parse_cookie_headers(self, headers: List[bytes]) -> SimpleCookie:
         cookie = SimpleCookie()
         for header in headers:
             if header.lower().startswith(b"set-cookie: "):
                 cookie.load(header[12:].decode())  # len("set-cookie: ") == 12
         return cookie
```

### Comparing `curl_cffi-0.5.2/curl_cffi/ffi/cdef.c` & `curl_cffi-0.5.3/curl_cffi/ffi/cdef.c`

 * *Files 11% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 void *curl_easy_init();
 int _curl_easy_setopt(void *curl, int option, void *param);
 int curl_easy_getinfo(void *curl, int option, void *ret);
 int curl_easy_perform(void *curl);
 void curl_easy_cleanup(void *curl);
+void curl_easy_reset(void *curl);
 char *curl_version();
 int curl_easy_impersonate(void *curl, char *target, int default_headers);
 struct curl_slist *curl_slist_append(struct curl_slist *list, char *string);
 void curl_slist_free_all(struct curl_slist *list);
 extern "Python" size_t buffer_callback(void *ptr, size_t size, size_t nmemb, void *userdata);
 extern "Python" size_t write_callback(void *ptr, size_t size, size_t nmemb, void *userdata);
 extern "Python" int debug_function(void *curl, int type, char *data, size_t size, void *clientp);
```

### Comparing `curl_cffi-0.5.2/curl_cffi/ffi/shim.c` & `curl_cffi-0.5.3/curl_cffi/ffi/shim.c`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/requests/__init__.py` & `curl_cffi-0.5.3/curl_cffi/requests/__init__.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/requests/cookies.py` & `curl_cffi-0.5.3/curl_cffi/requests/cookies.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/requests/headers.py` & `curl_cffi-0.5.3/curl_cffi/requests/headers.py`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi/requests/session.py` & `curl_cffi-0.5.3/curl_cffi/requests/session.py`

 * *Files 1% similar despite different names*

```diff
@@ -388,15 +388,17 @@
             impersonate,
         )
         try:
             c.perform()
         except CurlError as e:
             raise RequestsError(e)
 
-        return self._parse_response(c, req, buffer, header_buffer)
+        rsp = self._parse_response(c, req, buffer, header_buffer)
+        self.curl.reset()
+        return rsp
 
     head = partialmethod(request, "HEAD")
     get = partialmethod(request, "GET")
     post = partialmethod(request, "POST")
     put = partialmethod(request, "PUT")
     patch = partialmethod(request, "PATCH")
     delete = partialmethod(request, "DELETE")
@@ -489,19 +491,21 @@
             verify,
             referer,
             accept_encoding,
             content_callback,
             impersonate,
         )
         try:
+            # curl.debug()
             await self.acurl.add_handle(curl)
             curl.clear_headers()
         except CurlError as e:
             raise RequestsError(e)
         rsp = self._parse_response(curl, req, buffer, header_buffer)
+        curl.reset()
         self.push_curl(curl)
         return rsp
 
     head = partialmethod(request, "HEAD")
     get = partialmethod(request, "GET")
     post = partialmethod(request, "POST")
     put = partialmethod(request, "PUT")
```

### Comparing `curl_cffi-0.5.2/curl_cffi.egg-info/PKG-INFO` & `curl_cffi-0.5.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: curl-cffi
-Version: 0.5.2
+Name: curl_cffi
+Version: 0.5.3
 Summary: libcurl ffi bindings for Python, with impersonation support
 Author-email: Yifei Kong <kong@yifei.me>
 License: MIT License
         
         Copyright (c) 2018 multippt
         Copyright (c) 2022 Yifei Kong
```

### Comparing `curl_cffi-0.5.2/curl_cffi.egg-info/SOURCES.txt` & `curl_cffi-0.5.3/curl_cffi.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/curl_cffi.egg-info/requires.txt` & `curl_cffi-0.5.3/curl_cffi.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `curl_cffi-0.5.2/pyproject.toml` & `curl_cffi-0.5.3/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "curl_cffi"
-version = "0.5.2"
+version = "0.5.3"
 authors = [{ name = "Yifei Kong", email = "kong@yifei.me" }]
 description = "libcurl ffi bindings for Python, with impersonation support"
 license = { file = "LICENSE" }
 dependencies = ["cffi>=1.12.0"]
 readme = "README.md"
 requires-python = ">=3.7"
 urls = { "repository" = "https://github.com/yifeikong/curl_cffi" }
```

### Comparing `curl_cffi-0.5.2/setup.py` & `curl_cffi-0.5.3/setup.py`

 * *Files identical despite different names*

