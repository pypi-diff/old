# Comparing `tmp/recon_lw-2.0.0.dev4636658792.tar.gz` & `tmp/recon_lw-2.0.0.dev4638480940.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/recon_lw-2.0.0.dev4636658792.tar", last modified: Fri Apr  7 08:19:50 2023, max compression
+gzip compressed data, was "dist/recon_lw-2.0.0.dev4638480940.tar", last modified: Fri Apr  7 13:19:54 2023, max compression
```

## Comparing `recon_lw-2.0.0.dev4636658792.tar` & `recon_lw-2.0.0.dev4638480940.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/
--rw-r--r--   0 runner    (1001) docker     (122)       69 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)       10 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/README.md
--rw-r--r--   0 runner    (1001) docker     (122)       76 2023-04-07 08:19:36.000000 recon_lw-2.0.0.dev4636658792/package_info.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw/
--rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/recon_lw/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    12849 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/recon_lw/recon_lw.py
--rw-r--r--   0 runner    (1001) docker     (122)    11951 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/recon_lw/recon_ob.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      287 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)      219 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/recon_lw.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 08:19:50.000000 recon_lw-2.0.0.dev4636658792/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-07 08:19:30.000000 recon_lw-2.0.0.dev4636658792/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/
+-rw-r--r--   0 runner    (1001) docker     (122)       69 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)       10 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)       76 2023-04-07 13:19:39.000000 recon_lw-2.0.0.dev4638480940/package_info.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw/
+-rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12849 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/recon_lw.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12122 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/recon_ob.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      287 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      219 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/setup.py
```

### Comparing `recon_lw-2.0.0.dev4636658792/recon_lw/recon_lw.py` & `recon_lw-2.0.0.dev4638480940/recon_lw/recon_lw.py`

 * *Files identical despite different names*

### Comparing `recon_lw-2.0.0.dev4636658792/recon_lw/recon_ob.py` & `recon_lw-2.0.0.dev4638480940/recon_lw/recon_ob.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,22 +34,29 @@
         sequence.add(seq_element)
         times.add((ts, seq_num))
 
 
 def flush_sequence_get_collection(current_ts, horizon_delay, sequence_cache):
     times = sequence_cache["times"]
     sequence = sequence_cache["sequence"]
+    sub_seq = None
     if current_ts is not None:
         edge_timestamp = {"epochSecond": current_ts["epochSecond"] - horizon_delay,
                           "nano": 0}
         horizon_edge = times.bisect_key_left(recon_lw.time_stamp_key(edge_timestamp))
-        seq_index = times[horizon_edge][1]
-        for i in range(0,horizon_edge):
-            times.pop(0)
-        return sequence.irange(None, (seq_index,None))
+        if horizon_edge < len(times):
+            seq_index = times[horizon_edge][1]
+            sub_seq = sequence.irange(None, (seq_index,None))
+            for i in range(0,horizon_edge):
+                times.pop(0)
+        else:
+            sub_seq = sequence
+            times.clear()
+
+        return sub_seq
     else:
         times.clear()
         return sequence
 
 
 def flush_sequence_clear_cache(processed_len, sequence_cache):
     sequence = sequence_cache["sequence"]
```

### Comparing `recon_lw-2.0.0.dev4636658792/setup.py` & `recon_lw-2.0.0.dev4638480940/setup.py`

 * *Files identical despite different names*

