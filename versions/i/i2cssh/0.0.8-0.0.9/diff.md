# Comparing `tmp/i2cssh-0.0.8.tar.gz` & `tmp/i2cssh-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "i2cssh-0.0.8.tar", last modified: Wed Nov 16 21:45:28 2022, max compression
+gzip compressed data, was "i2cssh-0.0.9.tar", last modified: Thu Nov 17 18:22:49 2022, max compression
```

## Comparing `i2cssh-0.0.8.tar` & `i2cssh-0.0.9.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxr-xr-x   0 wouter.de.bie   (501) staff       (20)        0 2022-11-16 21:45:28.944818 i2cssh-0.0.8/
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)     1057 2019-08-06 15:05:32.000000 i2cssh-0.0.8/LICENSE.txt
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)      711 2022-11-16 21:45:28.944193 i2cssh-0.0.8/PKG-INFO
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)     7795 2022-11-16 19:41:39.000000 i2cssh-0.0.8/README.md
--rwxr-xr-x   0 wouter.de.bie   (501) staff       (20)    18511 2022-11-16 21:44:33.000000 i2cssh-0.0.8/i2cssh
-drwxr-xr-x   0 wouter.de.bie   (501) staff       (20)        0 2022-11-16 21:45:28.943246 i2cssh-0.0.8/i2cssh.egg-info/
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)      711 2022-11-16 21:45:28.000000 i2cssh-0.0.8/i2cssh.egg-info/PKG-INFO
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)      197 2022-11-16 21:45:28.000000 i2cssh-0.0.8/i2cssh.egg-info/SOURCES.txt
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)        1 2022-11-16 21:45:28.000000 i2cssh-0.0.8/i2cssh.egg-info/dependency_links.txt
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)       63 2022-11-16 21:45:28.000000 i2cssh-0.0.8/i2cssh.egg-info/requires.txt
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)        8 2022-11-16 21:45:28.000000 i2cssh-0.0.8/i2cssh.egg-info/top_level.txt
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)       38 2022-11-16 21:45:28.945068 i2cssh-0.0.8/setup.cfg
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)     1019 2022-11-16 19:36:17.000000 i2cssh-0.0.8/setup.py
--rw-r--r--   0 wouter.de.bie   (501) staff       (20)       34 2022-11-16 21:44:55.000000 i2cssh-0.0.8/version.py
+drwxr-xr-x   0 wouter.de.bie   (501) staff       (20)        0 2022-11-17 18:22:49.452806 i2cssh-0.0.9/
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)     1057 2019-08-06 15:05:32.000000 i2cssh-0.0.9/LICENSE.txt
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)      711 2022-11-17 18:22:49.452419 i2cssh-0.0.9/PKG-INFO
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)    11780 2022-11-17 18:22:11.000000 i2cssh-0.0.9/README.md
+-rwxr-xr-x   0 wouter.de.bie   (501) staff       (20)    18722 2022-11-17 18:17:57.000000 i2cssh-0.0.9/i2cssh
+drwxr-xr-x   0 wouter.de.bie   (501) staff       (20)        0 2022-11-17 18:22:49.451600 i2cssh-0.0.9/i2cssh.egg-info/
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)      711 2022-11-17 18:22:49.000000 i2cssh-0.0.9/i2cssh.egg-info/PKG-INFO
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)      197 2022-11-17 18:22:49.000000 i2cssh-0.0.9/i2cssh.egg-info/SOURCES.txt
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)        1 2022-11-17 18:22:49.000000 i2cssh-0.0.9/i2cssh.egg-info/dependency_links.txt
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)       63 2022-11-17 18:22:49.000000 i2cssh-0.0.9/i2cssh.egg-info/requires.txt
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)        7 2022-11-17 18:22:49.000000 i2cssh-0.0.9/i2cssh.egg-info/top_level.txt
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)       38 2022-11-17 18:22:49.453184 i2cssh-0.0.9/setup.cfg
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)     1019 2022-11-16 19:36:17.000000 i2cssh-0.0.9/setup.py
+-rw-r--r--   0 wouter.de.bie   (501) staff       (20)       34 2022-11-17 18:18:35.000000 i2cssh-0.0.9/version.py
```

### Comparing `i2cssh-0.0.8/LICENSE.txt` & `i2cssh-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `i2cssh-0.0.8/PKG-INFO` & `i2cssh-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: i2cssh
-Version: 0.0.8
+Version: 0.0.9
 Summary: csshX like ssh tool for iTerm2
 Home-page: http://github.com/wouterdebie/i2cssh
 Author: Wouter de Bie
 Author-email: wouter@evenflow.nl
 License: MIT
 Keywords: ssh,i2cssh,csshX
 Classifier: Operating System :: MacOS
```

### Comparing `i2cssh-0.0.8/i2cssh` & `i2cssh-0.0.9/i2cssh`

 * *Files 1% similar despite different names*

```diff
@@ -175,15 +175,15 @@
             # we create a new window. In any other cases we just create a new tab for the group
             if i == 0 and not opts.get("same_window"):
                 window = await window.async_create(connection, profile_name, profile_customizations=lwop)
             else:
                 await window.async_create_tab(profile_name, profile_customizations=lwop)
 
             # Set window to fullscreen if necessary
-            if i == 0 and opts.get("fullscreen"):
+            if i == 0 and opts.get("fullscreen") or group["geometry"].get("requires_fullscreen"):
                 await window.async_set_fullscreen(True)
 
             cols = group["geometry"]["cols"]
             rows = group["geometry"]["rows"]
 
             if opts.get("direction") == "column":
                 vertical = True
@@ -347,17 +347,19 @@
         cols = math.ceil(hosts / rows)
     elif cols:
         rows = math.ceil(hosts / cols)
     else:
         rows = math.ceil(math.sqrt(hosts))
         cols = math.ceil(hosts / rows)
 
-    # Quick hack: iTerms default window only supports up to 11 rows and 22 columns
-    # If we surpass either one, we resort to full screen.
-    return {"rows": rows, "cols": cols, "requires_fullscreen": rows > 11 or cols > 22}
+    # Quick hack: iTerms default window only supports up to 12 rows and 16 columns in the default
+    # 80x25 profile. If we surpass either one, we resort to full screen.
+    # TODO: figure out the height and with of the profile and toggle full screen based on that
+    # rather than hardcoded values.
+    return {"rows": rows, "cols": cols, "requires_fullscreen": rows >= 12 or cols >= 16}
 
 
 def get_hosts(host_strings):
     """Get hosts from a list of hostname or login@hostname strings"""
     hosts = host_strings_to_hosts(host_strings)
     return hosts
```

### Comparing `i2cssh-0.0.8/i2cssh.egg-info/PKG-INFO` & `i2cssh-0.0.9/i2cssh.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: i2cssh
-Version: 0.0.8
+Version: 0.0.9
 Summary: csshX like ssh tool for iTerm2
 Home-page: http://github.com/wouterdebie/i2cssh
 Author: Wouter de Bie
 Author-email: wouter@evenflow.nl
 License: MIT
 Keywords: ssh,i2cssh,csshX
 Classifier: Operating System :: MacOS
```

### Comparing `i2cssh-0.0.8/setup.py` & `i2cssh-0.0.9/setup.py`

 * *Files identical despite different names*

