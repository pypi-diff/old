# Comparing `tmp/hightea-client-0.5.4.tar.gz` & `tmp/hightea-client-0.5.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hightea-client-0.5.4.tar", last modified: Sun Mar 26 04:27:18 2023, max compression
+gzip compressed data, was "dist/hightea-client-0.5.5.tar", last modified: Thu Apr  6 13:37:24 2023, max compression
```

## Comparing `hightea-client-0.5.4.tar` & `hightea-client-0.5.5.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/
--rw-rw-r--   0 rene      (1001) rene      (1001)      281 2023-03-26 04:27:18.000000 hightea-client-0.5.4/PKG-INFO
--rw-rw-r--   0 rene      (1001) rene      (1001)    10967 2023-03-26 03:46:52.000000 hightea-client-0.5.4/README.md
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/bin/
--rwxrwxr-x   0 rene      (1001) rene      (1001)     6545 2021-11-05 19:06:06.000000 hightea-client-0.5.4/bin/highteacli
--rw-rw-r--   0 rene      (1001) rene      (1001)       38 2023-03-26 04:27:18.000000 hightea-client-0.5.4/setup.cfg
--rw-rw-r--   0 rene      (1001) rene      (1001)      755 2023-02-06 12:18:57.000000 hightea-client-0.5.4/setup.py
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/src/
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/src/hightea/
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/src/hightea/client/
--rw-rw-r--   0 rene      (1001) rene      (1001)      165 2023-03-26 04:25:38.000000 hightea-client-0.5.4/src/hightea/client/__init__.py
--rw-rw-r--   0 rene      (1001) rene      (1001)    11277 2023-02-20 10:51:58.000000 hightea-client-0.5.4/src/hightea/client/apiactions.py
--rw-rw-r--   0 rene      (1001) rene      (1001)    10845 2023-02-08 15:53:19.000000 hightea-client-0.5.4/src/hightea/client/datahandler.py
--rw-rw-r--   0 rene      (1001) rene      (1001)    38768 2023-03-26 02:57:15.000000 hightea-client-0.5.4/src/hightea/client/interface.py
-drwxrwxr-x   0 rene      (1001) rene      (1001)        0 2023-03-26 04:27:18.000000 hightea-client-0.5.4/src/hightea_client.egg-info/
--rw-rw-r--   0 rene      (1001) rene      (1001)      281 2023-03-26 04:27:17.000000 hightea-client-0.5.4/src/hightea_client.egg-info/PKG-INFO
--rw-rw-r--   0 rene      (1001) rene      (1001)      374 2023-03-26 04:27:18.000000 hightea-client-0.5.4/src/hightea_client.egg-info/SOURCES.txt
--rw-rw-r--   0 rene      (1001) rene      (1001)        1 2023-03-26 04:27:17.000000 hightea-client-0.5.4/src/hightea_client.egg-info/dependency_links.txt
--rw-rw-r--   0 rene      (1001) rene      (1001)       30 2023-03-26 04:27:17.000000 hightea-client-0.5.4/src/hightea_client.egg-info/requires.txt
--rw-rw-r--   0 rene      (1001) rene      (1001)        8 2023-03-26 04:27:17.000000 hightea-client-0.5.4/src/hightea_client.egg-info/top_level.txt
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/
+-rw-rw-r--   0 rene      (1000) rene      (1000)      281 2023-04-06 13:37:24.000000 hightea-client-0.5.5/PKG-INFO
+-rw-rw-r--   0 rene      (1000) rene      (1000)    10967 2023-03-26 03:46:52.000000 hightea-client-0.5.5/README.md
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/bin/
+-rw-rw-r--   0 rene      (1000) rene      (1000)     6821 2023-04-06 11:49:20.000000 hightea-client-0.5.5/bin/highteacli
+-rw-rw-r--   0 rene      (1000) rene      (1000)       38 2023-04-06 13:37:24.000000 hightea-client-0.5.5/setup.cfg
+-rw-rw-r--   0 rene      (1000) rene      (1000)      755 2023-02-06 12:18:57.000000 hightea-client-0.5.5/setup.py
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/src/
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/src/hightea/
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/src/hightea/client/
+-rw-rw-r--   0 rene      (1000) rene      (1000)      165 2023-04-06 13:36:12.000000 hightea-client-0.5.5/src/hightea/client/__init__.py
+-rw-rw-r--   0 rene      (1000) rene      (1000)    11265 2023-04-06 11:52:33.000000 hightea-client-0.5.5/src/hightea/client/apiactions.py
+-rw-rw-r--   0 rene      (1000) rene      (1000)    10845 2023-02-08 15:53:19.000000 hightea-client-0.5.5/src/hightea/client/datahandler.py
+-rw-rw-r--   0 rene      (1000) rene      (1000)    38761 2023-04-06 11:52:33.000000 hightea-client-0.5.5/src/hightea/client/interface.py
+drwxrwxr-x   0 rene      (1000) rene      (1000)        0 2023-04-06 13:37:24.000000 hightea-client-0.5.5/src/hightea_client.egg-info/
+-rw-rw-r--   0 rene      (1000) rene      (1000)      281 2023-04-06 13:37:23.000000 hightea-client-0.5.5/src/hightea_client.egg-info/PKG-INFO
+-rw-rw-r--   0 rene      (1000) rene      (1000)      374 2023-04-06 13:37:23.000000 hightea-client-0.5.5/src/hightea_client.egg-info/SOURCES.txt
+-rw-rw-r--   0 rene      (1000) rene      (1000)        1 2023-04-06 13:37:23.000000 hightea-client-0.5.5/src/hightea_client.egg-info/dependency_links.txt
+-rw-rw-r--   0 rene      (1000) rene      (1000)       30 2023-04-06 13:37:23.000000 hightea-client-0.5.5/src/hightea_client.egg-info/requires.txt
+-rw-rw-r--   0 rene      (1000) rene      (1000)        8 2023-04-06 13:37:23.000000 hightea-client-0.5.5/src/hightea_client.egg-info/top_level.txt
```

### Comparing `hightea-client-0.5.4/README.md` & `hightea-client-0.5.5/README.md`

 * *Files identical despite different names*

### Comparing `hightea-client-0.5.4/bin/highteacli` & `hightea-client-0.5.5/bin/highteacli`

 * *Files 2% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     """
 
     def __init__(self, delay=0.1):
         self.spinner_generator = self.spinning_cursor()
         self.delay = delay
 
     def spinner_task(self):
-        while not self.event.isSet():
+        while not self.event.is_set():
             sys.stdout.write(next(self.spinner_generator))
             sys.stdout.flush()
             time.sleep(self.delay)
             sys.stdout.write('\b')
             sys.stdout.flush()
 
     def __enter__(self):
@@ -60,16 +60,16 @@
                 print(msg, file=sys.stderr)
             except Exception:
                 pass
             sys.exit(1)
 
 
 class CommandLineApp:
-    def __init__(self):
-        self.api = ErrorPrintAPI()
+    def __init__(self, **kwargs):
+        self.api = ErrorPrintAPI(**kwargs)
 
     def list_pdfs(self):
         lpdfs = self.api.list_pdfs()
         print('\n'.join(lpdfs))
 
     def list_processes(self):
         lproc = self.api.list_processes()
@@ -84,15 +84,15 @@
                     data = json.load(f)
             except Exception as e:
                 sys.exit(e)
         resp = self.api.request_hist(proc, data)
         token = resp['token']
         print(f"Processing request. The token is {token}.", file=sys.stderr)
         print(
-            f"Wait for the result here or run\n\n    hightea token {token}\n",
+            f"Wait for the result here or run\n\n    highteacli token {token}\n",
             file=sys.stderr,
         )
         self.wait_token(token, do_plot, json_fname, plot_fname)
 
     def check_status(self, token):
         res = self.api.check_token(token)
         self.handle_token_result(res, token, do_plot=False)
@@ -166,14 +166,16 @@
         help="path to save the plot to. By default it will be derived from the name of the token.",
         default=None,
     )
 
 
 def main():
     parser = argparse.ArgumentParser(description=__doc__)
+    parser.add_argument("--auth", help="API authentication token")
+    parser.add_argument("--endpoint", help="API server", default=apiactions.DEFAULT_ENDPOINT)
     commands = parser.add_subparsers(title='commands', dest='command')
     commands.add_parser('lproc', help='List available processes')
     commands.add_parser('lpdf', help='List available pdfs')
 
     hist = commands.add_parser('hist', help='make and histogram')
     hist.add_argument('process', help='process to compute the histogram for')
     hist.add_argument('file', help='JSON file with the hisogram specification')
@@ -181,15 +183,15 @@
 
     token_cmd = commands.add_parser('token', help='query the status of a token')
     token_cmd.add_argument('token', help='a token that has been requested')
     _add_common_args(token_cmd)
 
     ns = parser.parse_args()
     cmd = ns.command
-    app = CommandLineApp()
+    app = CommandLineApp(auth=ns.auth, endpoint=ns.endpoint)
     if cmd == 'lpdf':
         app.list_pdfs()
     elif cmd == 'lproc':
         app.list_processes()
     elif cmd == 'hist':
         pname = ns.process
         fname = ns.file
@@ -198,11 +200,14 @@
         plot_fname = ns.plot_output
         app.make_hist(pname, fname, do_plot, json_fname, plot_fname)
     elif cmd == 'token':
         do_plot = ns.plot
         json_fname = ns.output
         plot_fname = ns.plot_output
         app.wait_token(ns.token, do_plot, json_fname, plot_fname)
+    else:
+        parser.print_usage()
+        sys.exit(1)
 
 
 if __name__ == '__main__':
     main()
```

### Comparing `hightea-client-0.5.4/setup.py` & `hightea-client-0.5.5/setup.py`

 * *Files identical despite different names*

### Comparing `hightea-client-0.5.4/src/hightea/client/apiactions.py` & `hightea-client-0.5.5/src/hightea/client/apiactions.py`

 * *Files 0% similar despite different names*

```diff
@@ -280,15 +280,15 @@
             A dictionary representing the result of the computation.
         """
         for token_res in self.wait_token_impl(token):
             st = token_res['status']
             if st == 'errored':
                 raise RuntimeError("Bad status")
             elif st == 'completed':
-                return json.loads(token_res['result'])
+                return token_res['result']
 
 
     def wait_token_plot(self, token):
         """Block until the specified token is available. When it is, return an
         histogram representation.
 
         Parameters
```

### Comparing `hightea-client-0.5.4/src/hightea/client/datahandler.py` & `hightea-client-0.5.5/src/hightea/client/datahandler.py`

 * *Files identical despite different names*

### Comparing `hightea-client-0.5.4/src/hightea/client/interface.py` & `hightea-client-0.5.5/src/hightea/client/interface.py`

 * *Files 0% similar despite different names*

```diff
@@ -382,15 +382,15 @@
         Parameters
         ----------
         jet_parameters: dict
             A dict containing "maxnjet", "p" and "R".
         """
         if type(jet_parameters) == dict:
             success = True
-            if 'maxnjet' not in jet_parameters: success = False
+            if 'maxnjets' not in jet_parameters: success = False
             if 'p' not in jet_parameters: success = False
             if 'R' not in jet_parameters: success = False
             return success;
         else:
             return False;
 
 
@@ -613,15 +613,15 @@
         ids = list(range(0,len(self._requests)))
 
         finished = True
         for jt, req in enumerate(self._requests):
             if req['status'] == 'submitted':
                 resp = self._api.simple_req('get',f'token/'+req['token'])
                 if resp['status'] == 'completed':
-                    self._requests[jt]['result'] = json.loads(resp['result'])
+                    self._requests[jt]['result'] = resp['result']
                     self._requests[jt]['status'] = 'completed'
                 elif resp == 'errored':
                     print('error occured    : ',datetime.now())
                     self._requests[it]['status'] = 'errored'
                 else:
                     finished = False;
 
@@ -1013,28 +1013,28 @@
         """Specify jet parameters.
 
         This allows to specify parameters for the jet algorithm. This is
         possible for processes where a corresponding default parameters set
         is defined in the metadata.
 
         The following parameter are available:
-         - ``'maxnjet'``: the number of jets returned by the algorithm
-         - ``'p'``      : the power of the kt-algorithm (-1: anti-kT,1: kt)
-         - ``'R'``      : the radius parameter
+         - ``'maxnjets'``: the number of jets returned by the algorithm
+         - ``'p'``       : the power of the kt-algorithm (-1: anti-kT,1: kt)
+         - ``'R'``       : the radius parameter
 
         **NOTE**: Please be advised that, similar to cuts, results for processes
         that require a jet-algorithm on the generation level are only correct
         for more exclusive definitions of the jet-algorithm. This is a bit more
         subtle in case of the jet-algorithm case and therefore these parameters
         should be used carefully.
 
         Parameters
         ----------
         jet_parameters: dict
-            A dict containing the members 'maxnjet'(int), 'p'(int), 'R'(float).
+            A dict containing the members 'maxnjets'(int), 'p'(int), 'R'(float).
         """
 
         if self._status == 'submitted' or self._status == 'finished':
             print('WARNING: job already submitted. Nothing changed')
             return
 
         if self._is_valid_jet_parameters(jet_parameters) and 'default_jet_parameters' in self._metadata :
```

