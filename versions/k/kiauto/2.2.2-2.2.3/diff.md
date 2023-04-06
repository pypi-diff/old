# Comparing `tmp/kiauto-2.2.2.tar.gz` & `tmp/kiauto-2.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kiauto-2.2.2.tar", last modified: Sun Apr  2 20:52:58 2023, max compression
+gzip compressed data, was "kiauto-2.2.3.tar", last modified: Thu Apr  6 19:05:49 2023, max compression
```

## Comparing `kiauto-2.2.2.tar` & `kiauto-2.2.3.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 20:52:58.196621 kiauto-2.2.2/
--rw-rw-r--   0 root         (0) root         (0)    11358 2023-04-02 20:35:01.000000 kiauto-2.2.2/LICENSE
--rw-rw-r--   0 root         (0) root         (0)       67 2023-04-02 20:35:01.000000 kiauto-2.2.2/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)    17079 2023-04-02 20:52:58.196621 kiauto-2.2.2/PKG-INFO
--rw-rw-r--   0 root         (0) root         (0)    13874 2023-04-02 20:35:01.000000 kiauto-2.2.2/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 20:52:58.196621 kiauto-2.2.2/kiauto/
--rw-rw-r--   0 root         (0) root         (0)        0 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    14772 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/file_util.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 20:52:58.196621 kiauto-2.2.2/kiauto/interposer/
--rwxrwxr-x   0 root         (0) root         (0)    27344 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/interposer/libinterposer.so
--rw-rw-r--   0 root         (0) root         (0)    27085 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/interposer.py
--rw-rw-r--   0 root         (0) root         (0)     3755 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/log.py
--rw-rw-r--   0 root         (0) root         (0)    13108 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/misc.py
--rw-rw-r--   0 root         (0) root         (0)    18923 2023-04-02 20:35:01.000000 kiauto-2.2.2/kiauto/ui_automation.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 20:52:58.196621 kiauto-2.2.2/kiauto.egg-info/
--rw-r--r--   0 root         (0) root         (0)    17079 2023-04-02 20:52:58.000000 kiauto-2.2.2/kiauto.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      383 2023-04-02 20:52:58.000000 kiauto-2.2.2/kiauto.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 20:52:58.000000 kiauto-2.2.2/kiauto.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       19 2023-04-02 20:52:58.000000 kiauto-2.2.2/kiauto.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        7 2023-04-02 20:52:58.000000 kiauto-2.2.2/kiauto.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-02 20:52:58.196621 kiauto-2.2.2/setup.cfg
--rwxrwxr-x   0 root         (0) root         (0)     1410 2023-04-02 20:35:01.000000 kiauto-2.2.2/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 20:52:58.196621 kiauto-2.2.2/src/
--rwxrwxr-x   0 root         (0) root         (0)    40519 2023-04-02 20:35:01.000000 kiauto-2.2.2/src/eeschema_do
--rwxrwxr-x   0 root         (0) root         (0)     6979 2023-04-02 20:35:01.000000 kiauto-2.2.2/src/kicad2step_do
--rwxrwxr-x   0 root         (0) root         (0)    75176 2023-04-02 20:35:01.000000 kiauto-2.2.2/src/pcbnew_do
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:05:49.381743 kiauto-2.2.3/
+-rw-rw-r--   0 root         (0) root         (0)    11358 2023-04-06 19:04:40.000000 kiauto-2.2.3/LICENSE
+-rw-rw-r--   0 root         (0) root         (0)       67 2023-04-06 19:04:40.000000 kiauto-2.2.3/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)    17079 2023-04-06 19:05:49.381743 kiauto-2.2.3/PKG-INFO
+-rw-rw-r--   0 root         (0) root         (0)    13874 2023-04-06 19:04:40.000000 kiauto-2.2.3/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:05:49.377743 kiauto-2.2.3/kiauto/
+-rw-rw-r--   0 root         (0) root         (0)        0 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    14772 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/file_util.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:05:49.381743 kiauto-2.2.3/kiauto/interposer/
+-rwxrwxr-x   0 root         (0) root         (0)    27344 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/interposer/libinterposer.so
+-rw-rw-r--   0 root         (0) root         (0)    27535 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/interposer.py
+-rw-rw-r--   0 root         (0) root         (0)     3755 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/log.py
+-rw-rw-r--   0 root         (0) root         (0)    13108 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/misc.py
+-rw-rw-r--   0 root         (0) root         (0)    18923 2023-04-06 19:04:40.000000 kiauto-2.2.3/kiauto/ui_automation.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:05:49.377743 kiauto-2.2.3/kiauto.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    17079 2023-04-06 19:05:49.000000 kiauto-2.2.3/kiauto.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      383 2023-04-06 19:05:49.000000 kiauto-2.2.3/kiauto.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 19:05:49.000000 kiauto-2.2.3/kiauto.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       19 2023-04-06 19:05:49.000000 kiauto-2.2.3/kiauto.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        7 2023-04-06 19:05:49.000000 kiauto-2.2.3/kiauto.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 19:05:49.381743 kiauto-2.2.3/setup.cfg
+-rwxrwxr-x   0 root         (0) root         (0)     1410 2023-04-06 19:04:40.000000 kiauto-2.2.3/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:05:49.381743 kiauto-2.2.3/src/
+-rwxrwxr-x   0 root         (0) root         (0)    40519 2023-04-06 19:04:40.000000 kiauto-2.2.3/src/eeschema_do
+-rwxrwxr-x   0 root         (0) root         (0)     6979 2023-04-06 19:04:40.000000 kiauto-2.2.3/src/kicad2step_do
+-rwxrwxr-x   0 root         (0) root         (0)    75176 2023-04-06 19:04:40.000000 kiauto-2.2.3/src/pcbnew_do
```

### Comparing `kiauto-2.2.2/LICENSE` & `kiauto-2.2.3/LICENSE`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/PKG-INFO` & `kiauto-2.2.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kiauto
-Version: 2.2.2
+Version: 2.2.3
 Summary: KiCad Automation Scripts
 Home-page: https://github.com/INTI-CMNB/KiAuto/
 Author: Salvador E. Tropea
 Author-email: stropea@inti.gob.ar
 License: Apache License 2.0
 Description: 
         KiAuto
```

### Comparing `kiauto-2.2.2/README.md` & `kiauto-2.2.3/README.md`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/kiauto/file_util.py` & `kiauto-2.2.3/kiauto/file_util.py`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/kiauto/interposer/libinterposer.so` & `kiauto-2.2.3/kiauto/interposer/libinterposer.so`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/kiauto/interposer.py` & `kiauto-2.2.3/kiauto/interposer.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,14 +22,16 @@
 INTERPOSER_OPS = 'interposer_options.txt'
 IGNORED_DIALOG_MSGS = {'The quick brown fox jumps over the lazy dog.', '0123456789'}
 BOGUS_FILENAME = '#'
 KIKIT_HIDE = 'Specify which components to hide'
 # These dialogs are asynchronous, they can pop-up at anytime.
 # One example is when the .kicad_wks is missing, KiCad starts drawing and then detects it.
 INFO_DIALOGS = {'KiCad PCB Editor Information', 'KiCad Schematic Editor Information'}
+WARN_DIALOGS = {'KiCad PCB Editor Warning', 'KiCad Schematic Editor Warning'}
+ASYNC_DIALOGS = INFO_DIALOGS | WARN_DIALOGS
 
 
 def check_interposer(args, logger, cfg):
     # Name of the interposer library
     interposer_lib = os.path.abspath(os.path.join(os.path.dirname(__file__), 'interposer', 'libinterposer.so'))
     if (not os.path.isfile(interposer_lib) or  # The lib isn't there
        args.disable_interposer or              # The user disabled it
@@ -191,16 +193,17 @@
            not(not cfg.ki5 and line.endswith(cfg.window_title_end))):
             # We aren't expecting a window, but something seems to be there
             # Note that window title change is normal when we expect KiCad exiting
             title = line[17:]
             if title in INFO_DIALOGS:
                 # Async dialogs
                 dismiss_pcb_info(cfg, title)
-            elif title == 'pcbnew Warning':
+            elif title == 'pcbnew Warning' or title in WARN_DIALOGS:
                 # KiCad 5 error during post-load, before releasing the CPU
+                # KiCad 7 missing fonts
                 dismiss_pcbnew_warning(cfg, title)
             elif title.startswith(KIKIT_HIDE):
                 # Buggy KiKit plugin creating a dialog at start-up (many times)
                 pass
             else:
                 unknown_dialog(cfg, title)
             if dialog_interrupts:
@@ -260,25 +263,28 @@
     xdotool(keys)
     pre_gtk_title = 'GTK:Window Title:'
     pre_gtk = pre_gtk_title if no_show else 'GTK:Window Show:'
     if isinstance(name, str):
         name = [name]
     name_w_pre = [pre_gtk+f for f in name]
     # Add the async dialogs
-    for t in INFO_DIALOGS:
+    for t in ASYNC_DIALOGS:
         name_w_pre.append(pre_gtk_title+t)
     # Wait for our dialog or any async dialog
     # Note: wait_queue won't dismiss them because we use "with_windows=True"
     while True:
         res = wait_queue(cfg, name_w_pre, with_windows=True)
         title = res[len(pre_gtk_title):]
-        if title not in INFO_DIALOGS:
+        if title not in ASYNC_DIALOGS:
             break
-        # Get rid of the info dialog
-        dismiss_pcb_info(cfg, title)
+        if title in INFO_DIALOGS:
+            # Get rid of the info dialog
+            dismiss_pcb_info(cfg, title)
+        else:
+            dismiss_pcbnew_warning(cfg, title)
         # Send the keys again
         xdotool(keys)
     name = res[len(pre_gtk):]
     if no_wait:
         return name, None
     if not no_main:
         wait_queue(cfg, 'GTK:Main:In')
@@ -493,20 +499,22 @@
     if 'Error loading schematic file "'+os.path.abspath(cfg.input_file)+'".' in msgs:
         cfg.logger.error('eeschema reported an error while loading the schematic')
         exit(EESCHEMA_ERROR)
     unknown_dialog(cfg, title, msgs)
 
 
 def dismiss_pcbnew_warning(cfg, title):
-    """ Pad in invalid layer """
+    """ Pad in invalid layer
+        Missing font """
     msgs = collect_dialog_messages(cfg, title)
     # More generic cases
     for msg in msgs:
         # Warning about pad using an invalid layer
-        if msg.endswith("could not find valid layer for pad"):
+        # Missing font
+        if msg.endswith("could not find valid layer for pad") or re.search(r"Font '(.*)' not found; substituting '(.*)'", msg):
             cfg.logger.warning(msg)
             dismiss_dialog(cfg, title, 'Return')
             return
     unknown_dialog(cfg, title, msgs)
 
 
 def dismiss_remap_symbols(cfg, title):
@@ -615,36 +623,36 @@
                 if skip_match is None or m != skip_match:
                     m = msg_reg+': '+m+padding
                     log.info_progress(m[:80])
                     with_info = True
 
 
 def wait_start_by_msg(cfg):
-    cfg.logger.info('Waiting for PCB new window ...')
-    pre = 'GTK:Window Title:'
-    pre_l = len(pre)
-    cfg.logger.debug('Waiting pcbnew to start and load the PCB')
-    # Inform the elapsed time for slow loads
-    pres = [pre, 'PANGO:0:']
-    elapsed_r = re.compile(r'PANGO:(\d:\d\d:\d\d)')
     if cfg.is_pcbnew:
         kind = 'PCB'
         prg_name = 'Pcbnew'
         unsaved = '  [Unsaved]'
     else:
         kind = 'Schematic'
         prg_name = 'Eeschema'
         unsaved = ' noname.sch'
+    cfg.logger.info('Waiting for {} window ...'.format(prg_name))
+    pre = 'GTK:Window Title:'
+    pre_l = len(pre)
+    cfg.logger.debug('Waiting {} to start and load the {}'.format(prg_name, kind))
+    # Inform the elapsed time for slow loads
+    pres = [pre, 'PANGO:0:']
+    elapsed_r = re.compile(r'PANGO:(\d:\d\d:\d\d)')
     loading_msg = 'Loading '+kind
     prg_msg = prg_name+' —'
     with_elapsed = False
     while True:
         # Wait for any window
         res = wait_queue(cfg, pres, starts=True, timeout=cfg.wait_start, with_windows=True)
-        cfg.logger.debug('wait_pcbew_start_by_msg got '+res)
+        cfg.logger.debug('wait_start_by_msg got '+res)
         match = elapsed_r.match(res)
         title = res[pre_l:]
         if not match and with_elapsed:
             log.flush_info()
         if not cfg.ki5 and title.endswith(cfg.window_title_end):
             # KiCad 6
             if title.startswith('[no schematic loaded]'):
@@ -683,15 +691,15 @@
             dismiss_file_open_error(cfg, title)
         elif cfg.ki7 and title == 'File Open Warning':
             dismiss_file_open_error(cfg, title)
         elif title == 'Confirmation':
             dismiss_already_running(cfg, title)
         elif title == 'Warning':
             dismiss_warning(cfg, title)
-        elif title == 'pcbnew Warning':
+        elif title == 'pcbnew Warning' or title in WARN_DIALOGS:
             dismiss_pcbnew_warning(cfg, title)
         elif title == 'Remap Symbols':
             dismiss_remap_symbols(cfg, title)
         elif title in INFO_DIALOGS:
             dismiss_pcb_info(cfg, title)
         elif title.startswith(KIKIT_HIDE):
             # Buggy KiKit plugin creating a dialog at start-up (many times)
```

### Comparing `kiauto-2.2.2/kiauto/log.py` & `kiauto-2.2.3/kiauto/log.py`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/kiauto/misc.py` & `kiauto-2.2.3/kiauto/misc.py`

 * *Files 0% similar despite different names*

```diff
@@ -314,8 +314,8 @@
 __author__ = 'Salvador E. Tropea'
 __copyright__ = 'Copyright 2018-2023, INTI/Productize SPRL'
 __credits__ = ['Salvador E. Tropea', 'Seppe Stas', 'Jesse Vincent', 'Scott Bezek']
 __license__ = 'Apache 2.0'
 __email__ = 'stropea@inti.gob.ar'
 __status__ = 'stable'
 __url__ = 'https://github.com/INTI-CMNB/KiAuto/'
-__version__ = '2.2.2'
+__version__ = '2.2.3'
```

### Comparing `kiauto-2.2.2/kiauto/ui_automation.py` & `kiauto-2.2.3/kiauto/ui_automation.py`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/kiauto.egg-info/PKG-INFO` & `kiauto-2.2.3/kiauto.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kiauto
-Version: 2.2.2
+Version: 2.2.3
 Summary: KiCad Automation Scripts
 Home-page: https://github.com/INTI-CMNB/KiAuto/
 Author: Salvador E. Tropea
 Author-email: stropea@inti.gob.ar
 License: Apache License 2.0
 Description: 
         KiAuto
```

### Comparing `kiauto-2.2.2/setup.py` & `kiauto-2.2.3/setup.py`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/src/eeschema_do` & `kiauto-2.2.3/src/eeschema_do`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/src/kicad2step_do` & `kiauto-2.2.3/src/kicad2step_do`

 * *Files identical despite different names*

### Comparing `kiauto-2.2.2/src/pcbnew_do` & `kiauto-2.2.3/src/pcbnew_do`

 * *Files identical despite different names*

