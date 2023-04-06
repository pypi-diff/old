# Comparing `tmp/flashcam-1.3.2.tar.gz` & `tmp/flashcam-1.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flashcam-1.3.2.tar", last modified: Wed Feb 15 18:20:59 2023, max compression
+gzip compressed data, was "flashcam-1.3.4.tar", last modified: Wed Mar  1 18:44:42 2023, max compression
```

## Comparing `flashcam-1.3.2.tar` & `flashcam-1.3.4.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-02-15 18:20:59.252995 flashcam-1.3.2/
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    10122 2023-02-15 18:20:59.252995 flashcam-1.3.2/PKG-INFO
--rw-rw-r--   0 ojr       (1000) ojr       (1000)     7670 2023-02-15 18:20:56.000000 flashcam-1.3.2/README.md
-drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-02-15 18:20:59.248995 flashcam-1.3.2/bin/
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    26096 2023-02-15 18:20:42.000000 flashcam-1.3.2/bin/flashcam
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)      150 2021-11-06 15:40:40.000000 flashcam-1.3.2/bin/flashcam_join
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)      311 2022-01-21 21:23:45.000000 flashcam-1.3.2/bin/flashcam_rep
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)      447 2022-06-10 13:50:42.000000 flashcam-1.3.2/bin/flashcamg
-drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-02-15 18:20:59.248995 flashcam-1.3.2/flashcam/
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)      249 2021-10-01 16:29:02.000000 flashcam-1.3.2/flashcam/__init__.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     5255 2022-01-28 21:15:30.000000 flashcam-1.3.2/flashcam/base_camera2.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     8079 2023-02-01 13:41:33.000000 flashcam-1.3.2/flashcam/config.py
-drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-02-15 18:20:59.252995 flashcam-1.3.2/flashcam/data/
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    24159 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/BEAM_OFF.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    27944 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/BEAM_ON_.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    27715 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/DET_NRDY.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    27483 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/DET_RDY_.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    88835 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/c120.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)   533468 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/c270_orig.png
--rw-rw-r--   0 ojr       (1000) ojr       (1000)     1697 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/cameras.org
--rw-rw-r--   0 ojr       (1000) ojr       (1000)  1024874 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/cameras.pdf
--rw-rw-r--   0 ojr       (1000) ojr       (1000)     1975 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/cameras.tex
--rw-rw-r--   0 ojr       (1000) ojr       (1000)   115345 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/f100.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    30371 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/f100_orig.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    19991 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/monoskop.jpg
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    82499 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/data/vf0770.jpg
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4173 2022-04-20 12:50:34.000000 flashcam-1.3.2/flashcam/direct.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4572 2023-02-06 11:14:13.000000 flashcam-1.3.2/flashcam/izmq_receiver.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4131 2023-02-15 18:12:04.000000 flashcam-1.3.2/flashcam/mmapwr.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    43175 2023-02-15 17:44:29.000000 flashcam-1.3.2/flashcam/real_camera.py
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    35197 2023-02-14 15:48:37.000000 flashcam-1.3.2/flashcam/stream_enhancer.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    91923 2023-02-03 18:19:37.000000 flashcam-1.3.2/flashcam/uniwrec.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    11293 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/usbcheck.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    27417 2022-11-16 13:28:21.000000 flashcam-1.3.2/flashcam/v4lc.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)       20 2023-02-15 18:20:58.000000 flashcam-1.3.2/flashcam/version.py
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)    29797 2023-02-15 17:29:21.000000 flashcam-1.3.2/flashcam/web.py
-drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-02-15 18:20:59.248995 flashcam-1.3.2/flashcam.egg-info/
--rw-rw-r--   0 ojr       (1000) ojr       (1000)    10122 2023-02-15 18:20:59.000000 flashcam-1.3.2/flashcam.egg-info/PKG-INFO
--rw-rw-r--   0 ojr       (1000) ojr       (1000)      854 2023-02-15 18:20:59.000000 flashcam-1.3.2/flashcam.egg-info/SOURCES.txt
--rw-rw-r--   0 ojr       (1000) ojr       (1000)        1 2023-02-15 18:20:59.000000 flashcam-1.3.2/flashcam.egg-info/dependency_links.txt
--rw-rw-r--   0 ojr       (1000) ojr       (1000)      157 2023-02-15 18:20:59.000000 flashcam-1.3.2/flashcam.egg-info/requires.txt
--rw-rw-r--   0 ojr       (1000) ojr       (1000)        9 2023-02-15 18:20:59.000000 flashcam-1.3.2/flashcam.egg-info/top_level.txt
--rw-rw-r--   0 ojr       (1000) ojr       (1000)       38 2023-02-15 18:20:59.252995 flashcam-1.3.2/setup.cfg
--rwxrwxr-x   0 ojr       (1000) ojr       (1000)     1612 2023-01-24 14:18:08.000000 flashcam-1.3.2/setup.py
+drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-03-01 18:44:42.243785 flashcam-1.3.4/
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    10122 2023-03-01 18:44:42.243785 flashcam-1.3.4/PKG-INFO
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)     7670 2023-03-01 18:44:38.000000 flashcam-1.3.4/README.md
+drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-03-01 18:44:42.239785 flashcam-1.3.4/bin/
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    26096 2023-02-15 18:20:42.000000 flashcam-1.3.4/bin/flashcam
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)      150 2021-11-06 15:40:40.000000 flashcam-1.3.4/bin/flashcam_join
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)      311 2022-01-21 21:23:45.000000 flashcam-1.3.4/bin/flashcam_rep
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)      447 2022-06-10 13:50:42.000000 flashcam-1.3.4/bin/flashcamg
+drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-03-01 18:44:42.239785 flashcam-1.3.4/flashcam/
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)      249 2021-10-01 16:29:02.000000 flashcam-1.3.4/flashcam/__init__.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     5255 2022-01-28 21:15:30.000000 flashcam-1.3.4/flashcam/base_camera2.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     8079 2023-02-01 13:41:33.000000 flashcam-1.3.4/flashcam/config.py
+drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-03-01 18:44:42.243785 flashcam-1.3.4/flashcam/data/
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    24159 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/BEAM_OFF.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    27944 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/BEAM_ON_.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    27715 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/DET_NRDY.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    27483 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/DET_RDY_.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    88835 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/c120.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)   533468 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/c270_orig.png
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)     1697 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/cameras.org
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)  1024874 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/cameras.pdf
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)     1975 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/cameras.tex
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)   115345 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/f100.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    30371 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/f100_orig.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    19991 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/monoskop.jpg
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    82499 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/data/vf0770.jpg
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4173 2022-04-20 12:50:34.000000 flashcam-1.3.4/flashcam/direct.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4572 2023-02-06 11:14:13.000000 flashcam-1.3.4/flashcam/izmq_receiver.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     4176 2023-03-01 15:27:12.000000 flashcam-1.3.4/flashcam/mmapwr.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    45014 2023-03-01 15:27:12.000000 flashcam-1.3.4/flashcam/real_camera.py
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    35197 2023-02-14 15:48:37.000000 flashcam-1.3.4/flashcam/stream_enhancer.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    97755 2023-03-01 18:42:49.000000 flashcam-1.3.4/flashcam/uniwrec.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    11293 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/usbcheck.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    27417 2022-11-16 13:28:21.000000 flashcam-1.3.4/flashcam/v4lc.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)       20 2023-03-01 18:44:41.000000 flashcam-1.3.4/flashcam/version.py
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)    29797 2023-02-15 17:29:21.000000 flashcam-1.3.4/flashcam/web.py
+drwxrwxr-x   0 ojr       (1000) ojr       (1000)        0 2023-03-01 18:44:42.239785 flashcam-1.3.4/flashcam.egg-info/
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)    10122 2023-03-01 18:44:42.000000 flashcam-1.3.4/flashcam.egg-info/PKG-INFO
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)      854 2023-03-01 18:44:42.000000 flashcam-1.3.4/flashcam.egg-info/SOURCES.txt
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)        1 2023-03-01 18:44:42.000000 flashcam-1.3.4/flashcam.egg-info/dependency_links.txt
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)      157 2023-03-01 18:44:42.000000 flashcam-1.3.4/flashcam.egg-info/requires.txt
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)        9 2023-03-01 18:44:42.000000 flashcam-1.3.4/flashcam.egg-info/top_level.txt
+-rw-rw-r--   0 ojr       (1000) ojr       (1000)       38 2023-03-01 18:44:42.243785 flashcam-1.3.4/setup.cfg
+-rwxrwxr-x   0 ojr       (1000) ojr       (1000)     1687 2023-03-01 15:27:12.000000 flashcam-1.3.4/setup.py
```

### Comparing `flashcam-1.3.2/PKG-INFO` & `flashcam-1.3.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flashcam
-Version: 1.3.2
+Version: 1.3.4
 Summary: Composition of scripts to control a web camera
 Home-page: https://gitlab.com/jaromrax/flashcam
 Author: jaromrax
 Author-email: jaromrax@gmail.com
 License: GPL2
 Description: Project flashcam
         ================
```

### Comparing `flashcam-1.3.2/README.md` & `flashcam-1.3.4/README.md`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/bin/flashcam` & `flashcam-1.3.4/bin/flashcam`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/base_camera2.py` & `flashcam-1.3.4/flashcam/base_camera2.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/config.py` & `flashcam-1.3.4/flashcam/config.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/BEAM_OFF.jpg` & `flashcam-1.3.4/flashcam/data/BEAM_OFF.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/BEAM_ON_.jpg` & `flashcam-1.3.4/flashcam/data/BEAM_ON_.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/DET_NRDY.jpg` & `flashcam-1.3.4/flashcam/data/DET_NRDY.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/DET_RDY_.jpg` & `flashcam-1.3.4/flashcam/data/DET_RDY_.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/c120.jpg` & `flashcam-1.3.4/flashcam/data/c120.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/c270_orig.png` & `flashcam-1.3.4/flashcam/data/c270_orig.png`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/cameras.org` & `flashcam-1.3.4/flashcam/data/cameras.org`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/cameras.pdf` & `flashcam-1.3.4/flashcam/data/cameras.pdf`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/cameras.tex` & `flashcam-1.3.4/flashcam/data/cameras.tex`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/f100.jpg` & `flashcam-1.3.4/flashcam/data/f100.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/f100_orig.jpg` & `flashcam-1.3.4/flashcam/data/f100_orig.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/monoskop.jpg` & `flashcam-1.3.4/flashcam/data/monoskop.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/data/vf0770.jpg` & `flashcam-1.3.4/flashcam/data/vf0770.jpg`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/direct.py` & `flashcam-1.3.4/flashcam/direct.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/izmq_receiver.py` & `flashcam-1.3.4/flashcam/izmq_receiver.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/mmapwr.py` & `flashcam-1.3.4/flashcam/mmapwr.py`

 * *Files 5% similar despite different names*

```diff
@@ -103,15 +103,16 @@
             # execute(text.decode("utf8"))
             if text[0] == "*":
                 response = "xxxxxx","1"
             elif "*" in text:
                 response = text.split("*")[0]
                 if len(response.split())>1:
                     spl01 = response.split()[0].strip()
-                    spl02 = response.split()[1].strip()
+                    spl02 = " ".join(response.split()[1:])
+                    spl02 = spl02.strip()
                     response = f"{spl01}",f"{spl02}"
                     print("i... mmapread'nclear returning ", response)
                 else:
                     response = "xxxxxx","1"
             else:
                 response = "xxxxxx","1"
```

### Comparing `flashcam-1.3.2/flashcam/real_camera.py` & `flashcam-1.3.4/flashcam/real_camera.py`

 * *Files 2% similar despite different names*

```diff
@@ -38,14 +38,39 @@
 
 try:
     import pyautogui # take screenshot
 except:
     print("X... no DISPLAY, pyautogui cannot be used")
 # -----------------------------------------------------------------
 
+
+def is_int(n):
+    try:
+        float_n = float(n)
+        int_n = int(float_n)
+    except ValueError:
+        return False
+    else:
+        return float_n == int_n
+
+def is_float(n):
+    try:
+        float_n = float(n)
+    except ValueError:
+        return False
+    else:
+        return True
+
+def is_bool(n):
+    if type(n) is str and n=="False": return True
+    if type(n) is str and n=="True": return True
+    return False
+
+
+
 # -----------------------------------------------------------------
 
 class Camera(BaseCamera):
 
     video_source = 0
     histomean = 50
     capdevice = None # global
@@ -168,14 +193,15 @@
                 scale_percent = 50
                 width = int(image.shape[1] * scale_percent / 100)
                 height = int(image.shape[0] * scale_percent / 100)
                 # dsize
                 dsize = (width, height)
                 # resize image
                 frame = cv2.resize(image, dsize)
+                time.sleep(0.1) # from 85%cpu to 20% ??????
                 return "image", frame, cap # repeat cap==image
 
             elif cap.find("clock.jpg")==0:
                 height, width = 480, 640
                 blank_image = np.zeros((height,width,3), np.uint8)
                 blank_image[:,0:width//2] = (20,20,20)      # (B, G, R)
                 blank_image[:,width//2:width] = (25,25,25)
@@ -189,14 +215,15 @@
                 draw = ImageDraw.Draw(img_pil)
                 drtext = dt.datetime.now().strftime("%H:%M:%S.%f")[:-5]
 
                 #draw.text( position,  "国庆节/中秋节 快乐!", font = font, fill = (b, g, r, a))
                 b,g,r,a = 0,255,0,200
                 draw.text( position,  drtext, font = font, fill = (b, g, r, a))
                 frame = np.array(img_pil)
+                time.sleep(0.1) # from 85%cpu to 20%
                 # cv2.putText(
                 #     blank_image, #numpy array on which text is written
                 #     drtext, #text
                 #     position, #position at which writing has to start
                 #     #cv2.FONT_HERSHEY_SIMPLEX, #font family
                 #     font,
                 #     4, #font size
@@ -208,14 +235,16 @@
             elif cap.find(".jpg")>=0:
                 #print("i... static image mode")
                 capfull = os.path.expanduser( f"~/.config/flashcam/{cap}" )
                 if  os.path.exists(capfull):
                     fullpath_fixed_image =  capfull
                 else:
                     print("X... image doesnt exist", cap, "using monoskop")
+
+                time.sleep(0.1) # from 85%cpu to 20%
                 return "image", cv2.imread( fullpath_fixed_image), cap # repeat cap==image
         else:
             #print("i...  camera mode")
             if cap is None and vidnum is None:
                 print("X... camera not accessible")
                 time.sleep(0.2)
                 return "image",  cv2.imread( fullpath_fixed_image), cap # repeat cap==image
@@ -647,20 +676,40 @@
                     #           -------------- or from seread (fixed_image ...)
                     expression,value = mmread_n_clear( )
 
                     if expression[:5] != "xxxxx":
                         print(f"i...  *  EXPR: {expression} == {value}")
                         print(f"i...  *  EXPR: {expression} == {value}")
                         print(f"i...  *  EXPR: {expression} == {value}")
-                    # --- fixed_image
 
-                    try:
-                        globals()[expression] = eval(value)
-                    except:
-                        print("X... EXEC FAIL",expression,value)
+                        # -------------------- conversions without eval inf float bool, string
+                        if is_int(value):
+                            print("i... ",value, 'can be safely converted to an integer.')
+                            value = int(float(value)) # 1.0 => int crashes
+                        elif is_float(value):
+                            print("i... ",value, 'is a float with non-zero digit(s) in the fractional-part.')
+                            value = float(value)
+                        elif is_bool(value):
+                            print("i... ",value, 'is true or false.')
+                            if value=="True":
+                                value = True
+                            else:
+                                value = False
+                        else:
+                            print(f"i... /{value}/ is string. It remains a string, without quotes though.")
+                            value = str(value) # i dont care anyway
+                            value = value.strip('"').strip("'")
+
+                        try:
+                            # eval makes float float and int int
+                            #print("o... evaluating")
+                            globals()[expression] = value  #was  eval(value)
+                            print("i... evaluated")
+                        except:
+                            print("X... globals expression FAIL",expression,value)
 
 
                     # THIs - I think - Is for send telegram via web interface
                     # it is rather DEBUG tool than a real use
                     # NOT TESTED
                     #senh.telegram_send_image()
 
@@ -954,15 +1003,15 @@
                     if framekind in ["detect","delta","histo"]:
                         frame = senh.get_frame(  typ = framekind)
                     else:
                         frame = senh.get_frame(  )
 
                     # --- here I can touch frame:
                     if overtext is not None:
-                        position = (200,400)
+                        position = (140,400)
                         fontpath = os.path.expanduser("~/.config/flashcam/digital-7.mono.ttf")
                         font = ImageFont.truetype(fontpath, 2*32)
                         img_pil = Image.fromarray(frame)
                         draw = ImageDraw.Draw(img_pil)
                         drtext =  str(overtext) # to be sure
                         b,g,r,a = 0,255,0,0
                         draw.text( position,  drtext, font = font, fill = (b, g, r, a))
```

### Comparing `flashcam-1.3.2/flashcam/stream_enhancer.py` & `flashcam-1.3.4/flashcam/stream_enhancer.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/uniwrec.py` & `flashcam-1.3.4/flashcam/uniwrec.py`

 * *Files 2% similar despite different names*

```diff
@@ -89,15 +89,15 @@
 
 # x ... expand 2x ... buggy
 HELPTEXT = """ a/A ... AVI/stop (~/DATA/) (alt-a PNG)
  s/S ... save 1 JPG (PNG) (to ~/DATA/)
 
  z ... cycle zoom 2x (mouse click fixes the center)
  Z ... zoom 1x
- r ... rotate by 180 degrees
+ r/R ... rotate by +-1; Alt-r= 180 degrees
 
  c/C ... red cross on/off (save when off)
  hjkl ... move the red/green* cross (HJKL)
  t/u ... tracker 1 (cross sync, speed)
  T/u ... tracker 2 (more steady, but fragile)
 
  m/M ... measure/not distance,  (-v 110,1.2)
@@ -114,14 +114,29 @@
  i/I* ... accumulate images
 
  w ... open web browser
  q ... quit
        * with remote flashcam server """
 
 
+
+
+
+def rotate_image(image, angle):
+    image_center = tuple(np.array(image.shape[1::-1]) / 2)
+    # print( "rotate", image_center, angle )
+    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
+    #print(rot_mat)
+    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
+    #print("rotated by ", angle)
+    return result
+
+
+
+
 def kb_on_press(key):
     global SHIFT, CTRL
     try:
         a = key.char
         # print('alphanumeric key {0} pressed'.format( key.char))
         # CTRL  = False
     except AttributeError:
@@ -728,15 +743,16 @@
 
         # measurements (distance)
         measure = 0  # 1.7
 
         if str(vof).find(",") > 0:
             vof = str(vof).strip("(")
             vof = str(vof).strip(")")
-            measure_fov, measure = (float(vof.split(",")[0]),)
+            measure_fov, measure = (float(vof.split(",")[0]),) # ??? BUG?
+            print("D... measure == ", measure )
             float(vof.split(",")[1])
         else:
             measure_fov = float(vof)  # config.CONFIG['vof'] #
 
         cross = None
         greencross = False  # just tell if on/off
 
@@ -757,14 +773,16 @@
         frame_from_file = None  # backup the frame: for effects + for CAMER
 
         # -see the values sent from the webpy - i can use in track,
         #   but not in savejpg,saveavi!
         webframen = ""  # frame number from web.py()
         webframetime = ""
 
+        save_decor = False # save with decor or original... save is def in call...
+
         while connection_ok:  # ===============================================
             # read the frame from the camera and send it to the server
             # time.sleep(0.05)
 
             # while True:
             if (str(videodev).find("http://") == 0) or (
                 str(videodev).find("https://") == 0
@@ -1102,14 +1120,16 @@
                 #         # w,h,c = frame.shape
                 #         # print(w-centerY1, h-centerX1)
                 #        senh.rotate180( 180 )
                 #        frame = senh.get_frame(  )
                 if rotate == 180:
                     frame = cv2.rotate(frame, cv2.ROTATE_180)
                     # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
+                elif rotate != 0:
+                    frame = rotate_image( frame , rotate )
 
                 # I just need to put local gamma before avisave...
                 # else astroimage shows nothing..
                 if local_gamma != 1:
                     frame = adjust_gamma(frame, local_gamma)
 
                 if savepngcont:
@@ -1122,20 +1142,22 @@
                     cv2.imwrite(sfilename, frame)
                     if senh.add_frame(frame):
                         # print("avi..")
                         senh.setbox("png", senh.jpg)
                         frame = senh.get_frame()
 
                 if save:
-                    # savepngcont = False
-                    # print("AVI")  # OR MKV now with H264
-                    saviout.write(frame)
+                    if not save_decor:
+                        saviout.write(frame)
                     if senh.add_frame(frame):
                         # print("avi..")
-                        senh.setbox("AVI", senh.avi)
+                        if save_decor:
+                            senh.setbox("AVId", senh.avi)
+                        else:
+                            senh.setbox("AVI", senh.avi)
                         frame = senh.get_frame()
 
                 if saved_jpg == 1:
                     if senh.add_frame(frame):
                         # print("avi..")
                         senh.setbox("JPG", senh.jpg)
                         frame = senh.get_frame()
@@ -1188,62 +1210,76 @@
 
                     # now arbitrarily define 1 meter..like.. 100px =>
                     # alpha = 100*radians_per_pixel
                     # b = 1m / math.tan( alpha )
 
                     def get_order(dist=1.7):  # determine order that fits
                         # list of marks on the ruler
-                        wide = 0.01
+                        wide = 0.001
+                        notfulrng = 1.0 # notfulrng==0.8; I want full range now..
                         while True:
                             wide *= 10
                             pixwid = math.atan(wide / dist) / radians_per_pixel2
                             alpha = pixwid * radians_per_pixel2
-                            if pixwid > w / 2 * 0.8:  # not full rANGE
+                            if pixwid > w / 2 * notfulrng:  # not full rANGE
                                 wide /= 10
                                 pixwid = math.atan(wide / dist) / radians_per_pixel2
                                 alpha = pixwid * radians_per_pixel2
                                 break
                         order = wide
+
                         row = []
 
                         while True:
                             wide += order
                             pixwid = math.atan(wide / dist) / radians_per_pixel2
                             alpha = pixwid * radians_per_pixel2
-                            if pixwid > w / 2 * 0.8:  # not full rANGE:
+                            if pixwid > w / 2 * notfulrng:  # not full rANGE:
                                 wide -= order
                                 pixwid = math.atan(wide / dist) / radians_per_pixel2
                                 # neverused alpha = pixwid * radians_per_pixel2
                                 break
                             else:
                                 row.append(wide)
                         # -----
                         # -----
-                        row = row[::-1]  # revert - we want Big to small
                         row.append(order)
-                        if len(row) < 4:
-                            in0 = row[-1] / 2
-                            in1 = row[-1] / 5
-                            # in2 = row[-1]/10
+                        row = sorted(row)
+                        row = row[::-1]  # revert - we want Big to small
+                        if len(row) <= 4:
+                            in0 = row[0] / 2
+                            in1 =  row[0] / 4
+                            in2 = row[0] / 4 *3
+                            in3 = row[0] / 5
+                            #in2 = row[-1]/10
                             row.append(in0)
                             row.append(in1)
+                            row.append(in2)
                             # row.append( in2 )
+                            # print("   > ",row)
                         return row  # Big to small
 
                     def one_mark(dist=1.7, wide=[1, 2], speed=0):
                         #  wide ...  # Big to small
                         # h,w = frame.shape[0], frame.shape[1]
                         # pixel distance of halfwidth
 
                         # alpha = pixwid * radians_per_pixel2
                         # dist = wide/math.tan( alpha)
                         # I need to calculate 1m
                         level = 0
                         # print("XXXXX",wide)
                         for iwide in wide:
+
+                            # multiply and round to one digit..before pixel calc
+                            for ix in range(4):
+                                if iwide*10**ix > 1:
+                                    iwide = round( iwide* 10**ix)/10**ix
+                                    break
+
                             pixwid = math.atan(iwide / dist) / radians_per_pixel2
                             # neverused alpha = pixwid * radians_per_pixel2
 
                             # print(f" {radians_per_pixel}radpp {pixwid}   {wide}m <- {dist} ")
                             step = 0
                             mX, mY = int(w / 2), int(h / 2)
                             if not (cross is None):
@@ -1255,99 +1291,135 @@
 
                             yA, yB = mY, mY
 
                             xA = mX
                             xB = mX + int(pixwid)
                             color = (0, 255, 0)  # BGR
                             color = (55, 0, 255)  # BGR same as the red cross
+                            colos = (255, 0, 55)  # BGR same as the red cross
                             if level == 0:
                                 # line
                                 cv2.line(
                                     frame,
                                     (int(xA), int(yA)),
                                     (int(xB), int(yB)),
                                     color,
                                     1,
                                 )
-                            # vet bars
+                                cv2.line(
+                                    frame,
+                                    (int(xA), int(yA)),
+                                    (int(2*xA-xB), int(yB)),
+                                    colos,
+                                    1,
+                                )
+
+                                cv2.line( # probably 1st mark
+                                    frame,
+                                    (int(xA), int(yA + 8)),
+                                    (int(xA), int(yA - 8)),
+                                    color,
+                                    1,
+                                )
+
+                            # vert bars -
                             cv2.line(
                                 frame,
-                                (int(xA), int(yA + 2)),
-                                (int(xA), int(yA - 2)),
+                                (int(xB), int(yB + 2)),
+                                (int(xB), int(yB - 2)),
                                 color,
                                 1,
                             )
                             cv2.line(
                                 frame,
-                                (int(xB), int(yB + 2)),
-                                (int(xB), int(yB - 2)),
-                                color,
+                                (int(2*xA-xB), int(yB + 2)),
+                                (int(2*xA-xB), int(yB - 2)),
+                                colos,
                                 1,
                             )
 
                             unit = "m"
-                            # --- check the biggest to set the unit
-                            if wide[0] <= 0.01:
+                            # --- check the biggest to set the unit [0] is biggest
+                            if wide[0] <= 0.001:
+                                iwide = round(iwide * 1000 * 1000) / 1000
+                                unit = "mm"
+                            elif wide[0] <= 0.01:
                                 iwide = round(iwide * 100 * 1000) / 1000
                                 unit = "cm"
                             elif wide[0] <= 0.1:
                                 iwide = round(iwide * 100 * 100) / 100
                                 unit = "cm"
                             elif wide[0] < 1:
-                                iwide = round(iwide * 100) / 100
+                                iwide = round(iwide * 10 *100) / 100
+                                unit = "dm"
                             else:
                                 iwide = round(iwide * 10) / 10
 
                             # only properly round whatever unit
-                            if iwide <= 0.01:
+                            if iwide <= 0.001:
+                                iwide = round(iwide * 10000) / 10000
+                            elif iwide <= 0.01:
                                 iwide = round(iwide * 1000) / 1000
                             elif iwide <= 0.1:
                                 iwide = round(iwide * 100) / 100
                             elif iwide < 1:
                                 iwide = round(iwide * 10) / 10
                             else:
                                 iwide = round(iwide)
 
+
                             if level > 0:
                                 unit = ""  # no unit during the scale
                             unit2 = "m"
 
                             if str(iwide)[:2] == "0.":
                                 iwide = str(iwide)[1:]
 
-                            # width on scale
+                            # width on scale - scale values
                             cv2.putText(
                                 frame,
                                 f"{iwide}{unit}",
                                 (int(xB - 10), int(mY - 7)),  # little rightx a bit up y
                                 cv2.FONT_HERSHEY_SIMPLEX,
                                 0.35,
                                 color,
                                 1,
                             )
+                            cv2.putText(
+                                frame,
+                                f"{iwide}{unit}",
+                                (int(2*xA-xB - 10), int(mY - 7)),  # little rightx a bit up y
+                                cv2.FONT_HERSHEY_SIMPLEX,
+                                0.35,
+                                colos,
+                                1,
+                            )
+
+
+
                             if level >= 0:
                                 # distance - only at first mark
                                 cv2.putText(
                                     frame,
                                     f"  at {dist} {unit2}",
                                     (
                                         int(xA - 130),
-                                        int(mY + 5),
+                                        int(mY + 5 -40),
                                     ),  # little rightx a bit up y
                                     cv2.FONT_HERSHEY_SIMPLEX,
                                     0.35,
                                     color,
                                     1,
                                 )
                                 cv2.putText(
                                     frame,
                                     f"  FOV {measure_fov:.1f}deg",
                                     (
                                         int(xA - 130),
-                                        int(mY + 15),
+                                        int(mY + 15 -40),
                                     ),  # little rightx a bit up y
                                     cv2.FONT_HERSHEY_SIMPLEX,
                                     0.35,
                                     color,
                                     1,
                                 )
                                 # I add velocity
@@ -1404,14 +1476,20 @@
                 #                         frame = disp_mutext(frame, TEXT)
 
                 # ======================================================== IMSHOW
                 # ======================================================== IMSHOW
                 # ======================================================== IMSHOW
                 # ======================================================== IMSHOW
                 cv2.imshow(rpi_name, frame)  # 1 window for each RPi
+                # ======================================================== IMSHOW
+                if save_decor:
+                    saviout.write(frame)
+                # ======================================================== IMSHOW
+                # ======================================================== IMSHOW
+                # ======================================================== IMSHOW
                 # this may be useful?
                 if False:
                     if not (cropped is None):
                         cropped = cv2.resize(cropped, (640, 480))
                         cv2.imshow("tracking1", cropped)  # ZOOM ON TRACK
                         # cv2.resizeWindow(
 
@@ -1453,21 +1531,48 @@
                     if (frame is not None) and (rpi_name != "") and (key == ord("h")):
                         print("h PRESSED! - ")
                         show_help = not (show_help)
                         print(HELPTEXT)
 
                 # -----------------------------------------------------rotate zoom
 
-                if (frame is not None) and (rpi_name != "") and (key == ord("r")):
+                if (frame is not None) and \
+                   (rpi_name != "") and \
+                   (key == ord("r") and not (CTRL)):
+                    print("r PRESSED! - rotate change")
+                    if rotate is None:
+                        rotate = 0
+                    if rotate == 180:
+                        rotate = 0
+                    else:
+                        rotate+=1
+
+                if (frame is not None) and \
+                   (rpi_name != "") and \
+                    (key == ord("R") and not (CTRL)):
                     print("r PRESSED! - rotate change")
+                    if rotate is None:
+                        rotate = 0
+                    if rotate == 180:
+                        rotate = 0
+                    else:
+                        rotate-=1
+
+                if (frame is not None) and \
+                   (rpi_name != "") and \
+                    (key == ord("r") and  (CTRL)):
+                    print("r PRESSED! - reset rotate")
+                    if rotate is None:
+                        rotate = 0
                     if rotate == 180:
                         rotate = 0
                     else:
                         rotate = 180
 
+
                 if (frame is not None) and (rpi_name != "") and (key == ord("z")):
                     print(f"z PRESSED! - ZOOM {zoomme}x")
                     zoomme *= 2
                     if zoomme > 16:
                         zoomme = 1
                     sfilenamea = ""
 
@@ -1507,36 +1612,61 @@
                 # -----------------------------------------------------save s a
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
                     and (key == ord("a") and not CTRL)
                 ):
-                    print("a PRESSED! - saving AVI (mkv)")
-                    save = True
+                    if save:
+                        print("a PRESSED! - STOPPING AVI ... decor==",save_decor)
+                        sfilenamea = ""
+                        savepngcont = False
+                        save = False
+                    else:
+                        print("a PRESSED! - saving AVI WITHOUT DECOR (mkv)")
+                        save = True
+                        save_decor = False
+
+                        height, width, channel = frame.shape
+
+                        sfilenamea, saviout = setupsave((width, height))
+                        print(">>>", sfilenamea)
+
+
+
+                if (frame is not None) and \
+                   (rpi_name != "") and \
+                   (key == ord("A") and not CTRL):  # not with alt
+                    if save:
+                        print("A PRESSED! - STOPPING AVI (mkv)  decor ==", save_decor)
+                        sfilenamea = ""
+                        savepngcont = False
+                        save = False
+                    else:
+                        print("A PRESSED! - WITH DECOR saving AVI (mkv)")
+                        save = True
+                        save_decor = True
+                        height, width, channel = frame.shape
+
+                        sfilenamea, saviout = setupsave((width, height))
+                        print(">>>", sfilenamea)
+
+
+
+                if ( (frame is not None) and \
+                     (rpi_name != "") and \
+                     (key == ord("a"))  and (CTRL) ):  # (key == 1310817):
+                    if savepngcont:
+                        savepngcont = False
+                    else:
+                        print("alt-a PRESSED! - saving PNG continuosly !!!")  # ctrla
+                        savepngcont = True
 
-                    height, width, channel = frame.shape
 
-                    sfilenamea, saviout = setupsave((width, height))
-                    print(">>>", sfilenamea)
 
-                if (
-                    (frame is not None)
-                    and (rpi_name != "")
-                    and (key == ord("a"))
-                    and (CTRL)
-                ):  # (key == 1310817):
-                    print("alt-a PRESSED! - saving PNG continuosly !!!")  # ctrla
-                    savepngcont = True
-
-                if (frame is not None) and (rpi_name != "") and (key == ord("A")):
-                    print("A PRESSED! - STOPPING stopping saving AVI (mkv)")
-                    save = False
-                    sfilenamea = ""
-                    savepngcont = False
 
                 saved_jpg = 0
                 if (
                     (frame is not None)
                     and (rpi_name != "")
                     and ((key == ord("s")) or (key == ord("S")))
                 ):
@@ -1623,68 +1753,84 @@
                         cross[1] -= 17
                     if (
                         (frame is not None) and (rpi_name != "") and (key == ord("L"))
                     ):  # >
                         cross[0] += 17
 
                 if (
-                    (measure != 0)
+                    (measure > 0)
                     and (frame is not None)
                     and (rpi_name != "")
                     and (key == ord("N"))
                 ):
-                    print("n PRESSED! - measure distance - far")
+                    print("N PRESSED! - measure distance - far")
+                    measure_prev_tmp = measure
                     measure = round(10 * measure / 1.15) / 10
-                    if measure < 0.4:
-                        measure = 0.4
+                    if measure_prev_tmp == measure:
+                        measure = measure/2
+                    if measure < 0.1:
+                        measure = 0.1
 
                 if (
-                    (measure != 0)
+                    (measure > 0)
                     and (frame is not None)
                     and (rpi_name != "")
                     and (key == ord("n"))
                 ):
                     print("m PRESSED! - measure distance - closer")
+                    measure_prev_tmp = measure
                     if measure == 0:
                         measure = 1
+                    if measure < 0:
+                        measure = -measure
                     measure = round(10 * measure * 1.15) / 10
+                    if measure_prev_tmp == measure:
+                        measure = measure*2
                     if measure > 20000:
                         measure = 20000
 
                 if (frame is not None) and (rpi_name != "") and (key == ord("m")):
                     print("m PRESSED! - measure distance - ON")
                     print("i... cheap Sonix :  44 deg")
                     print("i... Sony imx    : 101 deg")
                     print("i... zenbook     :  56 deg")
+                    if measure < 0:
+                        measure = -measure
                     if measure == 0:
                         measure = 1
 
                 if (frame is not None) and (rpi_name != "") and (key == ord("M")):
                     print("M PRESSED! - DEmeasure")
-                    measure = 0
+                    measure = -abs(measure)
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure != 0)
+                    and (measure > 0)
                     and (key == ord("f"))
                 ):
-                    print("f PRESSED! - FOV increase")
+                    print("f PRESSED! - FOV increase", measure_fov)
+                    prev_fov_tmp = measure_fov
                     measure_fov = measure_fov * 1.15
-                    if measure_fov > 3:
+                    if measure_fov > 4:
                         measure_fov = round(measure_fov)
+                        if measure_fov == prev_fov_tmp:
+                            measure_fov = 2* measure_fov
                     else:
                         measure_fov = round(measure_fov * 10) / 10
-                    if measure_fov > 180:
-                        measure_fov = 180
+                        if measure_fov == prev_fov_tmp:
+                            measure_fov = 2* measure_fov
+                    if measure_fov > 160:
+                        measure_fov = 160
+
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure != 0)
+                    and (measure > 0)
                     and (key == ord("F"))
                 ):
                     print("F PRESSED! - FOV decrease")
                     measure_fov = measure_fov / 1.25
                     if measure_fov > 3:
                         measure_fov = round(measure_fov)
                     else:
@@ -1821,26 +1967,26 @@
                     post_addr = videodev.replace("/video", "/cross")
                     post_data = {"savebg": "SAVEBG"}
                     post_response = requests.post(url=post_addr, data=post_data)
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure == 0)
+                    and (measure <= 0)
                     and (key == ord("f"))
                 ):
                     print("f PRESSED! - mix foreground")
                     post_addr = videodev.replace("/video", "/cross")
                     post_data = {"mixfg": "MIXFG"}
                     post_response = requests.post(url=post_addr, data=post_data)
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure == 0)
+                    and (measure <= 0)
                     and (key == ord("F"))
                 ):
                     print("F PRESSED! - save foreground")
                     post_addr = videodev.replace("/video", "/cross")
                     post_data = {"savefg": "SAVEFG"}
                     post_response = requests.post(url=post_addr, data=post_data)
 
@@ -2179,27 +2325,27 @@
 
                     if post_data != {}:
                         post_response = requests.post(url=post_addr, data=post_data)
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure == 0)
+                    and (measure <= 0)
                     and (key == ord("i"))
                 ):
                     integrate *= 2
                     print(f"i PRESSED! - accum  {integrate} snapshots")
                     post_addr = videodev.replace("/video", "/cross")
                     post_data = {"accum": "ACCUM", "accumtxt": int(integrate)}
                     post_response = requests.post(url=post_addr, data=post_data)
 
                 if (
                     (frame is not None)
                     and (rpi_name != "")
-                    and (measure == 0)
+                    and (measure <= 0)
                     and (key == ord("I"))
                 ):
                     print("i PRESSED! - accum integrate 1")
                     integrate = 1
                     post_addr = videodev.replace("/video", "/cross")
                     post_data = {"accum": "ACCUM", "accumtxt": 0}
                     post_response = requests.post(url=post_addr, data=post_data)
```

### Comparing `flashcam-1.3.2/flashcam/usbcheck.py` & `flashcam-1.3.4/flashcam/usbcheck.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/v4lc.py` & `flashcam-1.3.4/flashcam/v4lc.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam/web.py` & `flashcam-1.3.4/flashcam/web.py`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/flashcam.egg-info/PKG-INFO` & `flashcam-1.3.4/flashcam.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flashcam
-Version: 1.3.2
+Version: 1.3.4
 Summary: Composition of scripts to control a web camera
 Home-page: https://gitlab.com/jaromrax/flashcam
 Author: jaromrax
 Author-email: jaromrax@gmail.com
 License: GPL2
 Description: Project flashcam
         ================
```

### Comparing `flashcam-1.3.2/flashcam.egg-info/SOURCES.txt` & `flashcam-1.3.4/flashcam.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `flashcam-1.3.2/setup.py` & `flashcam-1.3.4/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,11 +1,14 @@
 #!/usr/bin/env python3
 import os
 from setuptools import setup, find_packages
+"""
+??? I saw an error with this... sudo apt-get install python3-smbus
 
+"""
 #-----------problematic------
 def read(fname):
     return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
 import os.path
 
 def readver(rel_path):
```

