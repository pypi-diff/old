# Comparing `tmp/p-template-generator-0.1.8.tar.gz` & `tmp/p-template-generator-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "p-template-generator-0.1.8.tar", last modified: Tue Mar 21 09:11:39 2023, max compression
+gzip compressed data, was "p-template-generator-0.1.9.tar", last modified: Tue Mar 21 09:17:50 2023, max compression
```

## Comparing `p-template-generator-0.1.8.tar` & `p-template-generator-0.1.9.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxrwxrwx   0        0        0        0 2023-03-21 09:11:39.944405 p-template-generator-0.1.8/
--rw-rw-rw-   0        0        0     1074 2023-02-27 11:23:20.000000 p-template-generator-0.1.8/LICENSE
--rw-rw-rw-   0        0        0      405 2023-03-21 09:11:39.943487 p-template-generator-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0       20 2023-03-14 06:24:47.000000 p-template-generator-0.1.8/README.md
-drwxrwxrwx   0        0        0        0 2023-03-21 09:11:39.934487 p-template-generator-0.1.8/p_template_generator.egg-info/
--rw-rw-rw-   0        0        0      405 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      581 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       58 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0        9 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/requires.txt
--rw-rw-rw-   0        0        0       19 2023-03-21 09:11:39.000000 p-template-generator-0.1.8/p_template_generator.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-21 09:11:39.944405 p-template-generator-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0      825 2023-03-21 09:11:34.000000 p-template-generator-0.1.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-21 09:11:39.938487 p-template-generator-0.1.8/template_generator/
--rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-generator-0.1.8/template_generator/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-21 09:11:39.939488 p-template-generator-0.1.8/template_generator/bin/
--rw-rw-rw-   0        0        0        0 2023-03-14 07:30:37.000000 p-template-generator-0.1.8/template_generator/bin/__init__.py
--rw-rw-rw-   0        0        0     1378 2023-03-21 09:11:21.000000 p-template-generator-0.1.8/template_generator/binary.py
--rw-rw-rw-   0        0        0     3822 2023-03-21 08:31:17.000000 p-template-generator-0.1.8/template_generator/ffmpeg.py
--rw-rw-rw-   0        0        0     2615 2023-03-21 08:51:03.000000 p-template-generator-0.1.8/template_generator/main.py
--rw-rw-rw-   0        0        0     3994 2023-03-21 07:31:10.000000 p-template-generator-0.1.8/template_generator/template.py
--rw-rw-rw-   0        0        0     1856 2023-03-21 08:45:11.000000 p-template-generator-0.1.8/template_generator/template_test.py
-drwxrwxrwx   0        0        0        0 2023-03-21 09:11:39.940487 p-template-generator-0.1.8/template_generator/test/
--rw-rw-rw-   0        0        0        0 2023-03-14 07:30:37.000000 p-template-generator-0.1.8/template_generator/test/__init__.py
--rw-rw-rw-   0        0        0  2446703 2023-03-20 12:10:43.000000 p-template-generator-0.1.8/template_generator/test/res.zip.py
+drwxrwxrwx   0        0        0        0 2023-03-21 09:17:50.059647 p-template-generator-0.1.9/
+-rw-rw-rw-   0        0        0     1074 2023-02-27 11:23:20.000000 p-template-generator-0.1.9/LICENSE
+-rw-rw-rw-   0        0        0      405 2023-03-21 09:17:50.059647 p-template-generator-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0       20 2023-03-14 06:24:47.000000 p-template-generator-0.1.9/README.md
+drwxrwxrwx   0        0        0        0 2023-03-21 09:17:50.049648 p-template-generator-0.1.9/p_template_generator.egg-info/
+-rw-rw-rw-   0        0        0      405 2023-03-21 09:17:49.000000 p-template-generator-0.1.9/p_template_generator.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      581 2023-03-21 09:17:50.000000 p-template-generator-0.1.9/p_template_generator.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-21 09:17:49.000000 p-template-generator-0.1.9/p_template_generator.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       58 2023-03-21 09:17:49.000000 p-template-generator-0.1.9/p_template_generator.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0        9 2023-03-21 09:17:49.000000 p-template-generator-0.1.9/p_template_generator.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       19 2023-03-21 09:17:49.000000 p-template-generator-0.1.9/p_template_generator.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-03-21 09:17:50.059647 p-template-generator-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0      825 2023-03-21 09:17:41.000000 p-template-generator-0.1.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-21 09:17:50.054648 p-template-generator-0.1.9/template_generator/
+-rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-generator-0.1.9/template_generator/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-21 09:17:50.055648 p-template-generator-0.1.9/template_generator/bin/
+-rw-rw-rw-   0        0        0        0 2023-03-14 07:30:37.000000 p-template-generator-0.1.9/template_generator/bin/__init__.py
+-rw-rw-rw-   0        0        0     1378 2023-03-21 09:11:21.000000 p-template-generator-0.1.9/template_generator/binary.py
+-rw-rw-rw-   0        0        0     3822 2023-03-21 08:31:17.000000 p-template-generator-0.1.9/template_generator/ffmpeg.py
+-rw-rw-rw-   0        0        0     2615 2023-03-21 08:51:03.000000 p-template-generator-0.1.9/template_generator/main.py
+-rw-rw-rw-   0        0        0     3822 2023-03-21 09:17:34.000000 p-template-generator-0.1.9/template_generator/template.py
+-rw-rw-rw-   0        0        0     1856 2023-03-21 08:45:11.000000 p-template-generator-0.1.9/template_generator/template_test.py
+drwxrwxrwx   0        0        0        0 2023-03-21 09:17:50.056647 p-template-generator-0.1.9/template_generator/test/
+-rw-rw-rw-   0        0        0        0 2023-03-14 07:30:37.000000 p-template-generator-0.1.9/template_generator/test/__init__.py
+-rw-rw-rw-   0        0        0  2446703 2023-03-20 12:10:43.000000 p-template-generator-0.1.9/template_generator/test/res.zip.py
```

### Comparing `p-template-generator-0.1.8/LICENSE` & `p-template-generator-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/p_template_generator.egg-info/SOURCES.txt` & `p-template-generator-0.1.9/p_template_generator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/setup.py` & `p-template-generator-0.1.9/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 setuptools.setup(
     name="p-template-generator",
-    version="0.1.8",
+    version="0.1.9",
     author="pengjun",
     author_email="mr_lonely@foxmail.com",
     description="temple tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
```

### Comparing `p-template-generator-0.1.8/template_generator/binary.py` & `p-template-generator-0.1.9/template_generator/binary.py`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/template_generator/ffmpeg.py` & `p-template-generator-0.1.9/template_generator/ffmpeg.py`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/template_generator/main.py` & `p-template-generator-0.1.9/template_generator/main.py`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/template_generator/template.py` & `p-template-generator-0.1.9/template_generator/template.py`

 * *Files 9% similar despite different names*

```diff
@@ -22,25 +22,21 @@
                 return binaryFile
         if root != files:
             break
     return ""
 
 def linuxEnvCheck(rootDir):
     if os.path.exists("/usr/lib/libskycore.so") == False:
-        for root,dirs,files in os.walk(rootDir):
-            for dir in dirs:
-                if "linux" in dir:
-                    shCommand = os.path.join(root, dir, "setup.sh")
-                    print("=================== begin Initialize environment ==================")
-                    cmd = subprocess.Popen(f"sh {shCommand}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
-                    while cmd.poll() is None:
-                        print(cmd.stdout.readline().rstrip())
-                    print("===================             end              ==================")
-            if root != files:
-                break
+        setupShell = os.path.join(rootDir, "skymedia", "setup.sh")
+        if os.path.join(setupShell):
+            print("=================== begin Initialize environment ==================")
+            cmd = subprocess.Popen(f"sh {setupShell}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
+            while cmd.poll() is None:
+                print(cmd.stdout.readline().rstrip())
+            print("===================             end              ==================")
     return os.path.exists("/usr/lib/libskycore.so")
 
 def getBinary(rootDir):
     binary = ""
     if sys.platform == "win32":
         binary = winBinary(rootDir)
     elif sys.platform == "linux":
```

### Comparing `p-template-generator-0.1.8/template_generator/template_test.py` & `p-template-generator-0.1.9/template_generator/template_test.py`

 * *Files identical despite different names*

### Comparing `p-template-generator-0.1.8/template_generator/test/res.zip.py` & `p-template-generator-0.1.9/template_generator/test/res.zip.py`

 * *Files identical despite different names*

