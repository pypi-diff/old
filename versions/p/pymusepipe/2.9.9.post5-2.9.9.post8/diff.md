# Comparing `tmp/pymusepipe-2.9.9.post5.tar.gz` & `tmp/pymusepipe-2.9.9.post8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pymusepipe-2.9.9.post5.tar", last modified: Mon Apr  6 13:25:07 2020, max compression
+gzip compressed data, was "dist/pymusepipe-2.9.9.post8.tar", last modified: Tue Apr 21 16:15:35 2020, max compression
```

## Comparing `pymusepipe-2.9.9.post5.tar` & `pymusepipe-2.9.9.post8.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      222 2020-03-27 12:32:02.000000 pymusepipe-2.9.9.post5/.gitignore
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/.idea/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       39 2019-12-03 11:04:38.000000 pymusepipe-2.9.9.post5/.idea/.gitignore
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/.idea/inspectionProfiles/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      228 2020-03-20 17:17:15.000000 pymusepipe-2.9.9.post5/.idea/inspectionProfiles/profiles_settings.xml
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      301 2020-03-20 17:17:15.000000 pymusepipe-2.9.9.post5/.idea/misc.xml
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      272 2019-12-03 11:11:27.000000 pymusepipe-2.9.9.post5/.idea/modules.xml
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      597 2020-02-27 11:18:40.000000 pymusepipe-2.9.9.post5/.idea/pymusepipe.iml
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      167 2019-12-03 11:09:12.000000 pymusepipe-2.9.9.post5/.idea/vcs.xml
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/.spyproject/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       56 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post5/.spyproject/codestyle.ini
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       58 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post5/.spyproject/encoding.ini
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       85 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post5/.spyproject/vcs.ini
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      247 2019-12-03 11:08:15.000000 pymusepipe-2.9.9.post5/.spyproject/workspace.ini
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1074 2019-07-11 20:45:04.000000 pymusepipe-2.9.9.post5/LICENSE.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       34 2018-07-06 14:27:10.000000 pymusepipe-2.9.9.post5/MANIFEST.in
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    14459 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/PKG-INFO
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    11829 2020-03-27 13:09:19.000000 pymusepipe-2.9.9.post5/README.md
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/config_templates/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      443 2019-07-15 08:39:19.000000 pymusepipe-2.9.9.post5/config_templates/calib_tables.dic
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      129 2019-07-12 10:08:17.000000 pymusepipe-2.9.9.post5/config_templates/rc.dic
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      747 2020-03-26 10:49:18.000000 pymusepipe-2.9.9.post5/pymusepipe/__init__.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    70144 2020-04-06 12:16:50.000000 pymusepipe-2.9.9.post5/pymusepipe/align_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     4844 2019-12-03 12:17:31.000000 pymusepipe-2.9.9.post5/pymusepipe/check_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    44570 2020-03-26 15:48:34.000000 pymusepipe-2.9.9.post5/pymusepipe/combine.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    11518 2020-03-26 15:48:45.000000 pymusepipe-2.9.9.post5/pymusepipe/config_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     7045 2020-03-26 15:48:58.000000 pymusepipe-2.9.9.post5/pymusepipe/create_sof.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    17999 2020-04-03 12:36:33.000000 pymusepipe-2.9.9.post5/pymusepipe/cube_convolve.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     2710 2018-08-02 08:13:39.000000 pymusepipe-2.9.9.post5/pymusepipe/emission_lines.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     5335 2019-12-03 10:47:31.000000 pymusepipe-2.9.9.post5/pymusepipe/graph_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     5526 2020-03-26 15:51:13.000000 pymusepipe-2.9.9.post5/pymusepipe/init_musepipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    44189 2020-04-03 15:36:22.000000 pymusepipe-2.9.9.post5/pymusepipe/mpdaf_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    31913 2020-03-26 15:46:38.000000 pymusepipe-2.9.9.post5/pymusepipe/musepipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    68989 2020-03-26 15:46:36.000000 pymusepipe-2.9.9.post5/pymusepipe/prep_recipes_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    17920 2020-03-26 12:24:59.000000 pymusepipe-2.9.9.post5/pymusepipe/recipes_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    33323 2020-03-26 15:52:42.000000 pymusepipe-2.9.9.post5/pymusepipe/target_sample.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    11902 2020-03-26 15:53:09.000000 pymusepipe-2.9.9.post5/pymusepipe/util_pipe.py
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1588 2020-04-06 12:00:44.000000 pymusepipe-2.9.9.post5/pymusepipe/version.py
-drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    14459 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/PKG-INFO
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1006 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/SOURCES.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)        1 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/dependency_links.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)        1 2018-03-15 14:27:42.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/not-zip-safe
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       26 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/requires.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       11 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/pymusepipe.egg-info/top_level.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       51 2020-03-20 18:00:54.000000 pymusepipe-2.9.9.post5/requirements.txt
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       79 2020-04-06 13:25:07.000000 pymusepipe-2.9.9.post5/setup.cfg
--rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1224 2020-03-27 12:20:46.000000 pymusepipe-2.9.9.post5/setup.py
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      222 2020-03-27 12:32:02.000000 pymusepipe-2.9.9.post8/.gitignore
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/.idea/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       39 2019-12-03 11:04:38.000000 pymusepipe-2.9.9.post8/.idea/.gitignore
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/.idea/inspectionProfiles/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      228 2020-03-20 17:17:15.000000 pymusepipe-2.9.9.post8/.idea/inspectionProfiles/profiles_settings.xml
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      301 2020-03-20 17:17:15.000000 pymusepipe-2.9.9.post8/.idea/misc.xml
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      272 2019-12-03 11:11:27.000000 pymusepipe-2.9.9.post8/.idea/modules.xml
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      597 2020-02-27 11:18:40.000000 pymusepipe-2.9.9.post8/.idea/pymusepipe.iml
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      167 2019-12-03 11:09:12.000000 pymusepipe-2.9.9.post8/.idea/vcs.xml
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/.spyproject/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       56 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post8/.spyproject/codestyle.ini
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       58 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post8/.spyproject/encoding.ini
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       85 2019-12-03 11:04:57.000000 pymusepipe-2.9.9.post8/.spyproject/vcs.ini
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      247 2019-12-03 11:08:15.000000 pymusepipe-2.9.9.post8/.spyproject/workspace.ini
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1074 2019-07-11 20:45:04.000000 pymusepipe-2.9.9.post8/LICENSE.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       34 2018-07-06 14:27:10.000000 pymusepipe-2.9.9.post8/MANIFEST.in
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    14459 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/PKG-INFO
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    11829 2020-03-27 13:09:19.000000 pymusepipe-2.9.9.post8/README.md
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/config_templates/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      443 2019-07-15 08:39:19.000000 pymusepipe-2.9.9.post8/config_templates/calib_tables.dic
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      129 2019-07-12 10:08:17.000000 pymusepipe-2.9.9.post8/config_templates/rc.dic
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)      747 2020-03-26 10:49:18.000000 pymusepipe-2.9.9.post8/pymusepipe/__init__.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    75820 2020-04-21 16:12:59.000000 pymusepipe-2.9.9.post8/pymusepipe/align_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     4844 2019-12-03 12:17:31.000000 pymusepipe-2.9.9.post8/pymusepipe/check_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    44570 2020-03-26 15:48:34.000000 pymusepipe-2.9.9.post8/pymusepipe/combine.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    11518 2020-03-26 15:48:45.000000 pymusepipe-2.9.9.post8/pymusepipe/config_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     7045 2020-03-26 15:48:58.000000 pymusepipe-2.9.9.post8/pymusepipe/create_sof.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    17999 2020-04-03 12:36:33.000000 pymusepipe-2.9.9.post8/pymusepipe/cube_convolve.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     2710 2018-08-02 08:13:39.000000 pymusepipe-2.9.9.post8/pymusepipe/emission_lines.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     5335 2019-12-03 10:47:31.000000 pymusepipe-2.9.9.post8/pymusepipe/graph_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     5526 2020-03-26 15:51:13.000000 pymusepipe-2.9.9.post8/pymusepipe/init_musepipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    44189 2020-04-03 15:36:22.000000 pymusepipe-2.9.9.post8/pymusepipe/mpdaf_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    31854 2020-04-21 07:22:52.000000 pymusepipe-2.9.9.post8/pymusepipe/musepipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    69120 2020-04-21 07:21:38.000000 pymusepipe-2.9.9.post8/pymusepipe/prep_recipes_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    17920 2020-03-26 12:24:59.000000 pymusepipe-2.9.9.post8/pymusepipe/recipes_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    33323 2020-03-26 15:52:42.000000 pymusepipe-2.9.9.post8/pymusepipe/target_sample.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    12038 2020-04-20 16:49:50.000000 pymusepipe-2.9.9.post8/pymusepipe/util_pipe.py
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1588 2020-04-21 16:14:37.000000 pymusepipe-2.9.9.post8/pymusepipe/version.py
+drwxrwxr-x   0 emsellem  (1000) emsellem  (1000)        0 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)    14459 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/PKG-INFO
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1006 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/SOURCES.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)        1 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/dependency_links.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)        1 2018-03-15 14:27:42.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/not-zip-safe
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       26 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/requires.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       11 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/pymusepipe.egg-info/top_level.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       51 2020-03-20 18:00:54.000000 pymusepipe-2.9.9.post8/requirements.txt
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)       79 2020-04-21 16:15:35.000000 pymusepipe-2.9.9.post8/setup.cfg
+-rw-rw-r--   0 emsellem  (1000) emsellem  (1000)     1224 2020-03-27 12:20:46.000000 pymusepipe-2.9.9.post8/setup.py
```

### Comparing `pymusepipe-2.9.9.post5/.idea/pymusepipe.iml` & `pymusepipe-2.9.9.post8/.idea/pymusepipe.iml`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/LICENSE.txt` & `pymusepipe-2.9.9.post8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/PKG-INFO` & `pymusepipe-2.9.9.post8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymusepipe
-Version: 2.9.9.post5
+Version: 2.9.9.post8
 Summary: python module to reduce MUSE Raw data and combine them
 Home-page: https://github.com/emsellem/pipemusepipe
 Author: Eric Emsellem
 Author-email: eric.emsellem@eso.org
 License: MIT
 Download-URL: https://github.com/emsellem/pymusepipe/archive/v2.9.6.beta.tar.gz
 Description: # pymusepipe
```

### Comparing `pymusepipe-2.9.9.post5/README.md` & `pymusepipe-2.9.9.post8/README.md`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/__init__.py` & `pymusepipe-2.9.9.post8/pymusepipe/__init__.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/align_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/align_pipe.py`

 * *Files 2% similar despite different names*

```diff
@@ -419,15 +419,15 @@
     Returns
     -------
     cdata: 2d array
         Processed array
     """
     # Omit the border pixels
     if border > 0:
-        data = crop_data(data)
+        data = crop_data(data, border=border)
     meddata = nd.filters.median_filter(data, filter_size)
 
     return meddata
 
 def prepare_image(data, border=10, dynamic_range=10, 
                   median_window=10, minflux=0.0):
     """Process image by squeezing the range, removing 
@@ -677,14 +677,20 @@
         self.name_refhdr = kwargs.pop("name_refhdr", "reference.hdr")
         self.suffix_images = kwargs.pop("suffix_muse_images", "IMAGE_FOV")
         self.filter_name = kwargs.pop("filter_name", "WFI_BB")
 
         # Use polynorm or not
         self.use_polynorm = kwargs.pop("use_polynorm", True)
 
+        # Use rotation angles if they exist or not
+        self.use_rotangles = kwargs.pop("use_rotangles", True)
+        if self.use_rotangles:
+            upipe.print_warning("By default, rotation angles given in initial "
+                                "offset table will be used if present.")
+
         # Getting the unit conversions
         self.convert_units = kwargs.pop("convert_units", True)
         if self.convert_units :
             self.ref_unit = kwargs.pop("ref_unit", default_reference_unit)
             self.muse_unit = kwargs.pop("muse_unit", default_muse_unit)
             self.conversion_factor = get_conversion_factor(self.ref_unit, 
                                                            self.muse_unit,
@@ -697,15 +703,15 @@
         self.folder_offset_table = kwargs.pop("folder_offset_table", None)
         if self.folder_offset_table is None:
             self.folder_offset_table = self.folder_muse_images
         self.name_offset_table = kwargs.pop("name_offset_table", None)
         self.minflux_crosscorr = kwargs.pop("minflux_crosscorr", 0.)
 
         # Get the MUSE images
-        self._get_list_muse_images(**kwargs)
+        self._get_list_muse_images()
         upipe.print_info("{0} MUSE images detected as input".format(
                             self.nimages))
         if self.nimages == 0:
             upipe.print_error("No MUSE images detected. Aborted")
             return
         self.list_offmuse_hdu = [None] * self.nimages
         self.list_wcs_offmuse_hdu = [None] * self.nimages
@@ -726,14 +732,16 @@
         # This contains the parameters of the linear fit
         self.ima_polypar = [None] * self.nimages
         # Normalisation factor to be saved or used
         self.ima_norm_factors = np.zeros((self.nimages), dtype=np.float64)
         self.ima_background = np.zeros_like(self.ima_norm_factors)
         self.muse_rotangles = np.zeros_like(self.ima_norm_factors)
         self.threshold_muse = np.zeros_like(self.ima_norm_factors) + threshold_muse
+        self._convolve_muse = np.zeros_like(self.ima_norm_factors)
+        self._convolve_reference = np.zeros_like(self.ima_norm_factors)
         # Default lists for date, mjd, tpls of the MUSE images
         self.ima_dateobs = [None] * self.nimages
         self.ima_mjdobs = [None] * self.nimages
         self.ima_tplstart = [None] * self.nimages
         self.ima_iexpo = [None] * self.nimages
         self.ima_pointing = [None] * self.nimages
 
@@ -742,23 +750,16 @@
 
         # Open the Ref and MUSE image
         status_open = self.open_hdu()
         if not status_open:
             upipe.print_error("Problem in opening frames, please check your input")
             return
 
-        # find the cross correlation peaks for each image
-        # This is using zero offset and zero rotation
-        # as all parameters have been reset above
-        # New values will be taken out from the cross-correlation or fits table 
-        # just below with the init_guess_offset
-        self.find_ncross_peak()
-
         # Initialise the offsets using the cross-correlation or FITS table
-        self.init_guess_offset(self.firstguess, **kwargs)
+        self.init_guess_offset(self.firstguess)
 
         self.total_off_arcsec = self.init_off_arcsec + self.extra_off_arcsec
         self.total_off_pixel = self.init_off_pixel + self.extra_off_pixel
 
         # Now doing the shifts and projections with the guess/input values
         for nima in range(self.nimages):
             self.shift(nima)
@@ -810,14 +811,21 @@
             firstguess = "crosscorr"
             upipe.print_warning("Keyword 'firstguess' not recognised")
             upipe.print_warning("Using Cross-Correlation as "
                                 "a first guess of the alignment")
 
         if firstguess == "crosscorr":
             upipe.print_info("Using cross-correlation as the initial guess")
+            # find the cross correlation peaks for each image
+            # This is using zero offset and zero rotation
+            # as all parameters have been reset above
+            # New values will be taken out from the cross-correlation or fits table
+            # just below with the init_guess_offset
+            self.find_ncross_peak()
+
             self.init_off_arcsec = self.cross_off_arcsec * 1.0
             self.init_off_pixel = self.cross_off_pixel * 1.0
         elif firstguess == "fits":
             exist_table, self.offset_table = self.open_offset_table(
                     joinpath(self.folder_offset_table, self.name_offset_table))
             if exist_table is not True :
                 upipe.print_warning("Fits initialisation table not found, "
@@ -847,14 +855,19 @@
             # Extracting the rotangle, but only if there
             rotangle_exist = False
             if ('ROTANGLE' in self.offset_table.columns):
                 nonan_rotangle_table = np.where(
                         np.isnan(self.offset_table['ROTANGLE']), 
                         0., self.offset_table['ROTANGLE'])
                 rotangle_exist = True
+            if not rotangle_exist:
+                upipe.print_warning("Rotation angles not present in offset table."
+                                    "Please use argument 'rotation' in 'run' "
+                                    "to force a non zero value.")
+                self.use_rotangles = False
 
             # Loop over the images, using MJD
             for nima, mjd in enumerate(self.ima_mjdobs):
                 # Test if mjd is in the set of mjd_values
                 if mjd in mjd_values:
                     # Find the index of the value array where mjd
                     ind = np.nonzero(mjd_values == mjd)[0][0]
@@ -1072,16 +1085,17 @@
             (before extra_arcsec).
         extra_arcsec: list of 2 floats [0,0]
             Offsets in X and Y in arcsec to add to the existing
             guessed offsets. Ignored if extra_pixel is given.
         rotation: float [0]
             Angle to rotate the image (in degrees)
         use_rotangles: bool
-            Default is False. If True, use the rotation value
-            from self.init_muse_rotangles
+            Default is defined by the self.use_rotangles parameter.
+            If True, use the rotation value from self.init_muse_rotangles
+            If False, use the given rotation.
         threshold_muse: float [0]
             Threshold to consider when plotting the comparison
         
         Plots (if self.plot is True)
         ----------------------------
         This plots a set of comparison maps:
            * flux comparison (1 to 1)
@@ -1100,23 +1114,26 @@
         if "extra_pixel" in kwargs:
             extra_pixel = kwargs.pop("extra_pixel", [0., 0.])
             extra_arcsec = pixel_to_arcsec(self.list_muse_hdu[nima], 
                                            extra_pixel)
         else:
             extra_arcsec = kwargs.pop("extra_arcsec", [0., 0.])
 
-        use_rotangles = kwargs.pop("use_rotangles", False)
+        # Use or not the initial rotation angles
+        use_rotangles = kwargs.pop("use_rotangles", self.use_rotangles)
         if use_rotangles:
             # Using the initial given value
             self.muse_rotangles[nima] = self.init_muse_rotangles[nima]
             upipe.print_warning("Rotation angle read from the initial values "
-                                "in self.init_muse_rotangles")
+                                "in self.init_muse_rotangles. Input argument"
+                                "'rotation' will be ignored")
         else:
             # Using default 0 rotation and threshold for this run
             self.muse_rotangles[nima] = kwargs.pop("rotation", 0.0)
+
         upipe.print_warning("Rotation will be = {0} degrees".format(
                                  self.muse_rotangles[nima]))
         self.threshold_muse[nima] = kwargs.pop("threshold_muse", 0.0)
 
         # Add the offset from user
         self.shift_arcsecond(extra_arcsec, nima)
 
@@ -1126,17 +1143,17 @@
     def _get_list_muse_images(self):
         """Extract the name of the muse images
         and build the list
         """
         from pathlib import Path
 
         if self.name_muse_images is None:
-            set_of_paths = glob.glob("{0}{1}*{2}*".format(
-                    self.folder_muse_images,
-                    self.suffix_images, self.filter_name))
+            set_of_paths = glob.glob("{0}*{1}*.fits".format(
+                    joinpath(self.folder_muse_images,
+                    self.suffix_images), self.filter_name))
             self.list_muse_images = [Path(muse_path).name 
                                      for muse_path in set_of_paths]
             # Sort alphabetically
             self.list_muse_images.sort()
             # Subselection if sel_indices_images is given
             if self.sel_indices_images is not None:
                 if not all([i in np.arange(len(self.list_muse_images)) 
@@ -1181,15 +1198,15 @@
         """Open the MUSE images hdu
         """
         self.list_name_musehdr = ["{0}{1:03d}.hdr".format(
                 self.name_musehdr, i+1) for i in range(self.nimages)]
         self.list_name_offmusehdr = ["{0}{1:03d}.hdr".format(
                 self.name_offmusehdr, i+1) for i in range(self.nimages)]
         self.list_hdulist_muse = [pyfits.open(
-                self.folder_muse_images + self.list_muse_images[i]) 
+                joinpath(self.folder_muse_images, self.list_muse_images[i]))
                 for i in range(self.nimages)]
         self.list_muse_hdu = [hdu[self.hdu_ext[1]] 
                               for hdu in self.list_hdulist_muse]
         # CHANGE to mpdaf WCS
         self.list_wcs_muse = [WCS(hdu[1].header) 
                               for hdu in self.list_hdulist_muse]
         self.list_dec_muse = np.array([muse_wcs.get_crval2()
@@ -1228,16 +1245,16 @@
 
         return 1
 
     def _open_ref_hdu(self):
         """Open the reference image hdu
         """
         # Open the images
-        hdulist_reference = pyfits.open(self.folder_reference 
-                                        + self.name_reference)
+        hdulist_reference = pyfits.open(joinpath(self.folder_reference,
+                                        self.name_reference))
         self.reference_hdu = hdulist_reference[self.hdu_ext[0]]
         if self.reference_hdu.data is None:
             upipe.print_error("No data found in extension of reference frame")
             upipe.print_error("Check your input, "
                     "or change the extention number in input hdu_ext[0]")
             return 0
 
@@ -1287,15 +1304,15 @@
         -------
         xpix_cross
         ypix_cross: x and y pixel coordinates of the cross-correlation peak
         """
         # Projecting the reference image onto the MUSE field
         tmphdr = muse_hdu.header.totextfile(joinpath(self.header_folder_name,
                                             name_musehdr), overwrite=True)
-        proj_ref_hdu = self._project_reference_hdu(muse_hdu, rotation=rotation)
+        proj_ref_hdu = self._align_reference_hdu(muse_hdu, rotation=rotation)
 
         # Cleaning the images
         if minflux is None:
             minflux = self.minflux_crosscorr
 
         minflux_ref = minflux / self.conversion_factor
         ima_ref = prepare_image(proj_ref_hdu.data, self.border, 
@@ -1393,51 +1410,83 @@
         # Clean up the NaNs
         data = np.nan_to_num(data)
         lperc = np.percentile(data[data > 0.], low)
         hperc = np.percentile(data[data > 0.], high)
 
         return lperc, hperc
 
-    def _project_reference_hdu(self, muse_hdu=None, rotation=0.0):
+    def _align_hdu(self, hdu_target=None, hdu_to_align=None, rotation=0.0,
+                   conversion=False):
         """Project the reference image onto the MUSE field
         Hidden function, as only used internally
-         
+
         Input
         -----
         muse_hdu: HDU [None]
             Input hdu
+        hdu_ref: HDU [None]
         rotation: float [0]
             Rotation angle in degrees
-        
+
         Returns
         -------
         hdu_repr: HDU
             Reprojected HDU. None if nothing is provided
         """
         # The mpdaf way to project an image onto an other one
         # WARNING: the reference image will be converted in flux
-        if muse_hdu is not None:
-            wcs_ref = WCS(hdr=self.reference_hdu.header)
-            ima_ref = Image(
-                    data=self.reference_hdu.data * self.conversion_factor, 
-                    wcs=wcs_ref)
+        if conversion:
+            conversion_factor = self.conversion_factor
+        else:
+            conversion_factor = 1.0
 
-            wcs_muse = WCS(hdr=muse_hdu.header)
-            if rotation != 0.:
-                wcs_muse.rotate(-rotation)
-            ima_muse = Image(data=np.nan_to_num(muse_hdu.data), wcs=wcs_muse)
+        if hdu_target is not None and hdu_to_align is not None:
+            # Getting the reference image data and WCS
+            wcs_to_align = WCS(hdr=hdu_to_align.header)
+            ima_to_align = Image(data=hdu_to_align.data * conversion_factor,
+                                 wcs=wcs_to_align)
 
-            ima_ref_proj = ima_ref.align_with_image(ima_muse, flux=True)
-            hdu_repr = ima_ref_proj.get_data_hdu()
+            # Getting the MUSE image data and WCS
+            wcs_target = WCS(hdr=hdu_target.header)
+            if rotation != 0.:
+                wcs_target.rotate(-rotation)
+            ima_target = Image(data=np.nan_to_num(hdu_target.data),
+                               wcs=wcs_target)
+
+            # Aligning the reference image with the MUSE image using mpdaf
+            # align_with_image
+            ima_aligned = ima_to_align.align_with_image(ima_target, flux=True)
+            hdu_aligned = ima_aligned.get_data_hdu()
 
         else:
-            hdu_repr = None
+            hdu_aligned = None
             print("Warning: please provide target HDU to allow reprojection")
 
-        return hdu_repr
+        return hdu_aligned
+
+    def _align_reference_hdu(self, hdu_target=None, rotation=0.0):
+        """Project the reference image onto the MUSE field
+        Hidden function, as only used internally
+         
+        Input
+        -----
+        muse_hdu: HDU [None]
+            Input hdu
+        rotation: float [0]
+            Rotation angle in degrees
+        
+        Returns
+        -------
+        hdu_repr: HDU
+            Reprojected HDU. None if nothing is provided
+        """
+
+        return self._align_hdu(hdu_target=hdu_target, rotation=rotation,
+                               hdu_to_align=self.reference_hdu,
+                               conversion=True)
 
     def _add_user_arc_offset(self, extra_arcsec=[0., 0.], nima=0):
         """Add user offset in arcseconds
         and update total_off_pixel and arcsec
          
         Input
         -----
@@ -1513,16 +1562,16 @@
 
         # Writing this up in an ascii file for record purposes
         tmphdr = self.list_offmuse_hdu[nima].header.totextfile(
                 joinpath(self.header_folder_name, self.list_name_offmusehdr[nima]), 
                 overwrite=True)
 
         # Reprojecting the Reference image onto the new MUSE frame
-        self.list_proj_refhdu[nima] = self._project_reference_hdu(
-                muse_hdu=self.list_offmuse_hdu[nima], 
+        self.list_proj_refhdu[nima] = self._align_reference_hdu(
+                hdu_target=self.list_offmuse_hdu[nima],
                 rotation=self.muse_rotangles[nima])
         # Now reading the WCS and saving it in the list
         self.list_wcs_proj_refhdu[nima] = WCS(
                 self.list_proj_refhdu[nima].header)
 
         # Getting the normalisation factors again
         musedata, refdata = self.get_image_normfactor(nima)
@@ -1551,53 +1600,56 @@
         -------
         data: 2d array
         refdata: 2d array
             The 2 arrays (input, reference) after processing
         """
         # If median filter do the filtermed_image process including the border
         # Both for the muse data and the reference data
+        # No cropping here
         if median_filter:
-            musedata = filtermed_image(self.list_offmuse_hdu[nima].data, 
-                                       self.border)
-            refdata = filtermed_image(
-                    self.list_proj_refhdu[nima].data,
-                    self.border)
+            musedata = filtermed_image(self.list_offmuse_hdu[nima].data, 0.)
+            refdata = filtermed_image(self.list_proj_refhdu[nima].data, 0.)
         # Otherwise just copy the data
         else:
             musedata = copy.copy(self.list_offmuse_hdu[nima].data)
             refdata = self.list_proj_refhdu[nima].data
 
         # Smoothing out the result in case it is needed
         if convolve_muse > 0 :
             kernel = Gaussian2DKernel(x_stddev=convolve_muse)
             musedata = convolve(musedata, kernel)
+            self._convolve_muse[nima] = convolve_muse
         if convolve_reference > 0 :
             kernel = Gaussian2DKernel(x_stddev=convolve_reference)
             refdata = convolve(refdata, kernel)
+            self._convolve_reference[nima] = convolve_reference
 
         # Getting the result of the normalisation
         if threshold_muse is not None:
             self.threshold_muse[nima] = threshold_muse
 
-        self.ima_polypar[nima] = get_image_norm_poly(musedata, 
-                        refdata, chunk_size=self.chunk_size,
+        # Cropping the data
+        musedataC = crop_data(musedata, self.border)
+        refdataC = crop_data(refdata, self.border)
+
+        self.ima_polypar[nima] = get_image_norm_poly(musedataC,
+                        refdataC, chunk_size=self.chunk_size,
                         threshold1=self.threshold_muse[nima])
         if self.use_polynorm:
             self.ima_norm_factors[nima] = self.ima_polypar[nima].beta[1]
             self.ima_background[nima] = self.ima_polypar[nima].beta[0]
+
+        # Returning the uncropped data
         return musedata, refdata
 
     def compare(self, start_nfig=1, nlevels=10, levels=None, convolve_muse=0.,
-            convolve_reference=0., samecontour=True, nima=0,
-            showcontours=True, showcuts=True, 
-            shownormalise=True, showdiff=True,
-            normalise=True, median_filter=True, 
-            ncuts=5, percentage=5.,
-            rotation=0.0,
-            threshold_muse=None):
+                convolve_reference=0., samecontour=True, nima=0,
+                showcontours=True, showcuts=True, shownormalise=True, showdiff=True,
+                normalise=True, median_filter=True, ncuts=5, percentage=5.,
+                rotation=0.0, threshold_muse=None, nima_museref=None):
         """Compare the projected reference and MUSE image
         by plotting the contours, the difference and vertical/horizontal cuts.
          
         Input
         -----
         nima: int
             Index of image to consider
@@ -1627,83 +1679,108 @@
             with a gaussian of that sigma
         samecontour: bool [True]
             If True, will use the same levels for both images
             (this is recommended). Otherwise levels can be
             automatically derived from percentiles, but will
             not necessarily be the same (which can bring
             confusion but may sometimes be useful).
+        nima_museref
         
         Makes a maximum of 4 figures
         """
         # Getting the data
         musedata, refdata = self.get_image_normfactor(nima=nima, 
-                median_filter=median_filter, 
-                convolve_muse=convolve_muse,
-                convolve_reference=convolve_reference,
-                threshold_muse=threshold_muse)
+                                median_filter=median_filter,
+                                convolve_muse=convolve_muse,
+                                convolve_reference=convolve_reference,
+                                threshold_muse=threshold_muse)
+
+        # Getting data from the MUSE ref image if one is given
+        museref = nima_museref is not None
+        if museref:
+            drot = self.muse_rotangles[nima] - self.muse_rotangles[nima_museref]
+            # Projecting the MUSE image onto the MUSE reference
+            musehduR = self._align_hdu(hdu_to_align=self.list_offmuse_hdu[nima],
+                                       rotation=drot,
+                                       hdu_target=self.list_offmuse_hdu[nima_museref],
+                                       conversion=False)
+            # Getting the data
+            musedataC = filtermed_image(musehduR.data, 0.)
+            musedataR = filtermed_image(self.list_offmuse_hdu[nima_museref].data, 0.)
+            if self._convolve_muse[nima_museref] > 0 :
+                kernel = Gaussian2DKernel(x_stddev=self._convolve_muse[nima_museref])
+                musedataR = convolve(musedataR, kernel)
+            if self._convolve_muse[nima] > 0 :
+                kernel = Gaussian2DKernel(x_stddev=self._convolve_muse[nima])
+                musedataC = convolve(musedataC, kernel)
 
         # If normalising, using the median ratio fit
         if normalise or shownormalise :
             polypar = self.ima_polypar[nima]
+            if museref:
+                polyparR = self.ima_polypar[nima_museref]
 
         # If normalising, use the polypar slope and background
         if normalise :
             if self.verbose:
                 upipe.print_info("Renormalising the MUSE data as NewMUSE = "
                         "{0:8.4e} * ({1:8.4e} + MUSE)".format(polypar.beta[1], 
                          polypar.beta[0]))
 
             musedata = (polypar.beta[0] + musedata) * polypar.beta[1]
+            if museref:
+                musedataC = (polypar.beta[0] + musedataC) * polypar.beta[1]
+                musedataR = (polyparR.beta[0] + musedataR) * polyparR.beta[1]
 
         # Getting the range of relevant fluxes
         lowlevel_muse, highlevel_muse = self._get_flux_range(musedata)
         lowlevel_ref, highlevel_ref = self._get_flux_range(refdata)
         if self.verbose:
             print("Low / High level MUSE flux: "
                     "{0:8.4e} {1:8.4e}".format(lowlevel_muse, highlevel_muse))
             print("Low / High level REF  flux: "
                     "{0:8.4e} {1:8.4e}".format(lowlevel_ref, highlevel_ref))
 
         # Save the frames in case this is needed
         self._temp_refdata = refdata
         self._temp_musedata = musedata
+        if museref:
+            self._temp_musedataR = musedataR
+            self._temp_musedataC = musedataC
 
         # Stop here if plot is not needed
         if not self.plot:
             return
 
-        # Get the WCS from mpdaf to allow rotation if needed
-        refwcs = self.list_wcs_proj_refhdu[nima]
-
         # WCS for plotting using astropy
         plotwcs = awcs.WCS(self.list_offmuse_hdu[nima].header)
 
         # Apply rotation in degrees
         # Apply it to the reference image not to couple it with the offset
         if rotation != 0:
             if self.verbose:
                 upipe.print_warning("Apply a rotation of "
                                     "{0} degrees".format(rotation))
-            refwcs.rotate(rotation)
 
         # Preparing the figure
         current_fig = start_nfig
         self.list_figures = []
 
         # Starting the plotting
         if shownormalise:
-            #plotting the normalization
+            # plotting the normalization
             fig, ax = open_new_wcs_figure(current_fig)
             (x, y) = (polypar.med[0][polypar.selection], 
                       polypar.med[1][polypar.selection])
             ax.plot(x, y, '.')
             ax.set_xlabel("MuseData")
             ax.set_ylabel("RefData")
             ax.plot(x, my_linear_model(polypar.beta, x), 'k')
             # ax.plot([np.min(x), np.max(x)], [np.min(x), np.max(x)], 'r')
+            plt.tight_layout()
 
             self.list_figures.append(current_fig)
             current_fig += 1
             
         if showcontours:
             np.seterr(divide = 'ignore', invalid='ignore') 
             fig, ax = open_new_wcs_figure(current_fig, plotwcs)
@@ -1734,34 +1811,77 @@
 
             ax.set_aspect('equal')
             h1,_ = cmuseset.legend_elements()
             h2,_ = crefset.legend_elements()
             ax.legend([h1[0], h2[0]], ['MUSE', 'REF'])
             if nima is not None:
                 plt.title("Image #{0:03d}".format(nima))
+            plt.tight_layout()
 
             self.list_figures.append(current_fig)
             current_fig += 1
-            np.seterr(divide = 'warn', invalid='warn') 
+            np.seterr(divide = 'warn', invalid='warn')
 
         if showcuts:
             fig, ax = open_new_wcs_figure(current_fig)
             diffima = (refdata - musedata) * 200. / (lowlevel_muse 
                       + highlevel_muse)
             chunk_x = musedata.shape[0] // (ncuts + 1)
             chunk_y = musedata.shape[1] // (ncuts + 1)
-            ax.plot(diffima[np.arange(ncuts)*chunk_x,:].T, 'k-', label='X')
-            ax.plot(diffima[:,np.arange(ncuts)*chunk_y], 'r-', label='Y')
-            ax.legend(loc=0)
+            c1 = ax.plot(diffima[np.arange(ncuts)*chunk_x,:].T, 'k-', label='X')
+            c2 = ax.plot(diffima[:,np.arange(ncuts)*chunk_y], 'r-', label='Y')
+            ax.legend(handles=[c1[0], c2[0]], loc=0)
             ax.set_ylim(-20,20)
             ax.set_xlabel("[pixels]", fontsize=20)
             ax.set_ylabel("[%]", fontsize=20)
+            plt.tight_layout()
             self.list_figures.append(current_fig)
             current_fig += 1
 
         if showdiff:
             fig, ax = open_new_wcs_figure(current_fig, plotwcs)
             ratio = 100. * (refdata - musedata) / (musedata + 1.e-12)
             im = ax.imshow(ratio, vmin=-percentage, vmax=percentage)
-            cbar = fig.colorbar(im)
+            cbar = fig.colorbar(im, shrink=0.8)
+            plt.tight_layout()
+            self.list_figures.append(current_fig)
+            current_fig += 1
+
+        if museref:
+            np.seterr(divide = 'ignore', invalid='ignore')
+            fig, ax = open_new_wcs_figure(current_fig, plotwcs)
+
+            # Defining the levels for MUSE
+            if levels is not None:
+                levels_muse = levels
+            else :
+                levels_muse = np.linspace(np.log10(lowlevel_muse),
+                                          np.log10(highlevel_muse),
+                                          nlevels)
+            # Plot contours for MUSE current image
+            cmusesetC = ax.contour(np.log10(musedataC),
+                                  levels_muse, colors='k',
+                                  origin='lower', linestyles='solid')
+
+            # now define Ref levels if not samecontour
+            if samecontour:
+                levels_ref = cmusesetC.levels
+            else:
+                levels_ref = np.linspace(np.log10(lowlevel_ref),
+                                         np.log10(highlevel_ref),
+                                         nlevels)
+            # Plot contours for Ref
+            cmusesetR = ax.contour(np.log10(musedataR), levels=levels_muse,
+                                   colors='r', origin='lower',
+                                   linestyles='solid', alpha=0.5)
+
+            ax.set_aspect('equal')
+            h1,_ = cmusesetC.legend_elements()
+            h2,_ = cmusesetR.legend_elements()
+            ax.legend([h1[0], h2[0]], ['MUSE', 'MUSEREF'])
+            if nima is not None:
+                plt.title("Image #{0:03d} / #{1:03d}".format(nima, nima_museref))
+            plt.tight_layout()
+
             self.list_figures.append(current_fig)
             current_fig += 1
+            np.seterr(divide = 'warn', invalid='warn')
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/check_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/check_pipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/combine.py` & `pymusepipe-2.9.9.post8/pymusepipe/combine.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/config_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/config_pipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/create_sof.py` & `pymusepipe-2.9.9.post8/pymusepipe/create_sof.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/cube_convolve.py` & `pymusepipe-2.9.9.post8/pymusepipe/cube_convolve.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/emission_lines.py` & `pymusepipe-2.9.9.post8/pymusepipe/emission_lines.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/graph_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/graph_pipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/init_musepipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/init_musepipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/mpdaf_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/mpdaf_pipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/musepipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/musepipe.py`

 * *Files 1% similar despite different names*

```diff
@@ -585,15 +585,16 @@
             # Going back to the original folder
             self.goto_prevfolder()
 
         # Sorting the types ====================================
         self.sort_raw_tables()
 
     def save_expo_table(self, expotype, tpl_gtable, stage="master",
-                        fits_tablename=None, aggregate=True, suffix="", overwrite=None, update=None):
+                        fits_tablename=None, aggregate=True, suffix="",
+                        overwrite=None, update=None):
         """Save the Expo (Master or not) Table corresponding to the expotype
         """
         self._set_option_astropy_table(overwrite, update)
 
         if fits_tablename is None:
             fits_tablename = self._get_fitstablename_expo(expotype, stage, suffix)
 
@@ -624,33 +625,30 @@
                     upipe.print_warning("Astropy Table cannot be joined to the existing one",
                                         pipe=self)
                     return
 
             # Check if we want to overwrite or add the line in
             elif not self._overwrite_astropy_table:
                 upipe.print_warning("Astropy Table {0} already exists, "
-                                    " use overwrite_astropy_table to overwrite it".format(fits_tablename),
+                                    " use overwrite_astropy_table to "
+                                    "overwrite it".format(fits_tablename),
                                     pipe=self)
                 return
 
         table_to_save.write(full_tablename, format="fits", overwrite=True)
         setattr(self._dic_tables[stage], attr_expo, table_to_save)
 
     def sort_raw_tables(self, checkmode=None, strong_checkmode=None):
         """Provide lists of exposures with types defined in the dictionary
         """
         if checkmode is not None:
             self.checkmode = checkmode
-        else:
-            checkmode = self.checkmode
 
         if strong_checkmode is not None:
             self.strong_checkmode = strong_checkmode
-        else:
-            strong_checkmode = self.strong_checkmode
 
         if len(self.Tables.Rawfiles) == 0:
             upipe.print_error("Raw files is empty, hence cannot be sorted")
             return
 
         # Sorting alphabetically (thus by date)
         for expotype in dic_expotypes:
@@ -738,11 +736,11 @@
             masterfolder = joinpath(self.pipe_params.master, masterfolder)
         return masterfolder
 
     def _get_fullpath_expo(self, expotype, stage="master"):
         if stage not in self._dic_paths:
             upipe.print_error("[_get_fullpath_expo] stage {} not "
                               "in dic_paths dict".format(stage))
-        return upipe.normpath(getattr(self._dic_paths[stage], self._get_attr_expo(expotype)))
+        return upipe.abspath(getattr(self._dic_paths[stage], self._get_attr_expo(expotype)))
 
     def _get_path_files(self, expotype):
-        return upipe.normpath(getattr(self.paths, expotype.lower()))
+        return upipe.abspath(getattr(self.paths, expotype.lower()))
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/prep_recipes_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/prep_recipes_pipe.py`

 * *Files 0% similar despite different names*

```diff
@@ -574,16 +574,18 @@
             name_products = []
             list_expo = np.arange(Nexpo).astype(np.int) + 1
             for iexpo in list_expo:
                 name_products += ['{0:04d}-{1:02d}.fits'.format(iexpo, j+1) for j in range(24)]
             self.recipe_scibasic(self.current_sof, tpl, expotype, dir_products, name_products, suffix)
 
             # Write the Processed files Table and save it
+            # Note: always overwrite the table so that a fresh numbering is done
             gtable['iexpo'] = list_expo
-            self.save_expo_table(expotype, gtable, "processed", aggregate=False, update=True)
+            self.save_expo_table(expotype, gtable, "processed", aggregate=False,
+                                 update=False, overwrite=True)
 
         # Go back to original folder
         self.goto_prevfolder(addtolog=True)
 
     @print_my_function_name
     def run_standard(self, sof_filename='standard', tpl="ALL", update=None):
         """Reducing the STD files after they have been obtained
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/recipes_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/recipes_pipe.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/target_sample.py` & `pymusepipe-2.9.9.post8/pymusepipe/target_sample.py`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/util_pipe.py` & `pymusepipe-2.9.9.post8/pymusepipe/util_pipe.py`

 * *Files 2% similar despite different names*

```diff
@@ -190,18 +190,23 @@
 
 def append_file(filename, content):
     """Append in ascii file
     """
     with open(filename, "a") as myfile:
         myfile.write(content)
         
+def abspath(path) :
+    """Normalise the path to get it short but absolute
+    """
+    return os.path.abspath(os.path.realpath(path))
+
 def normpath(path) :
     """Normalise the path to get it short
     """
-    return os.path.relpath(os.path.realpath(path))
+    return os.path.normpath(os.path.realpath(path))
 
 def doppler_shift(wavelength, velocity=0.):
     """Return the redshifted wavelength
     """
     doppler_factor = np.sqrt((1. + velocity / const.c.value) / (1. - velocity / const.c.value))
     return wavelength * doppler_factor
 
@@ -389,10 +394,10 @@
     pointing: int
     """
     # Writing the pointing and iexpo in the IMAGE_FOV
     this_image = pyfits.open(name_image, mode='update')
     this_image[0].header['MUSEPIPE_POINTING'] = (pointing, "Pointing number")
     this_image[0].header['MUSEPIPE_IEXPO'] = (iexpo, "Exposure number")
     this_image.flush()
-    print_info("Keyworks MUSEPIPE_POINTING/EXPO updated for image {}".format(
+    print_info("Keywords MUSEPIPE_POINTING/EXPO updated for image {}".format(
         name_image))
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe/version.py` & `pymusepipe-2.9.9.post8/pymusepipe/version.py`

 * *Files 9% similar despite different names*

```diff
@@ -24,9 +24,9 @@
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 """
-__version__ = '2.9.9.post5'
-__date__ = '2020/04/06'
+__version__ = '2.9.9.post8'
+__date__ = '2020/04/21'
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe.egg-info/PKG-INFO` & `pymusepipe-2.9.9.post8/pymusepipe.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymusepipe
-Version: 2.9.9.post5
+Version: 2.9.9.post8
 Summary: python module to reduce MUSE Raw data and combine them
 Home-page: https://github.com/emsellem/pipemusepipe
 Author: Eric Emsellem
 Author-email: eric.emsellem@eso.org
 License: MIT
 Download-URL: https://github.com/emsellem/pymusepipe/archive/v2.9.6.beta.tar.gz
 Description: # pymusepipe
```

### Comparing `pymusepipe-2.9.9.post5/pymusepipe.egg-info/SOURCES.txt` & `pymusepipe-2.9.9.post8/pymusepipe.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pymusepipe-2.9.9.post5/setup.py` & `pymusepipe-2.9.9.post8/setup.py`

 * *Files identical despite different names*

