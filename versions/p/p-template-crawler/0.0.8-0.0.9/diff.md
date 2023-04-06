# Comparing `tmp/p-template-crawler-0.0.8.tar.gz` & `tmp/p-template-crawler-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "p-template-crawler-0.0.8.tar", last modified: Tue Mar 21 03:07:22 2023, max compression
+gzip compressed data, was "p-template-crawler-0.0.9.tar", last modified: Tue Mar 21 03:16:03 2023, max compression
```

## Comparing `p-template-crawler-0.0.8.tar` & `p-template-crawler-0.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-03-21 03:07:22.330135 p-template-crawler-0.0.8/
--rw-rw-rw-   0        0        0     1074 2023-02-27 11:23:20.000000 p-template-crawler-0.0.8/LICENSE
--rw-rw-rw-   0        0        0      405 2023-03-21 03:07:22.330135 p-template-crawler-0.0.8/PKG-INFO
--rw-rw-rw-   0        0        0       20 2023-03-14 06:24:47.000000 p-template-crawler-0.0.8/README.md
-drwxrwxrwx   0        0        0        0 2023-03-21 03:07:22.323135 p-template-crawler-0.0.8/mecord_crawler/
--rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-crawler-0.0.8/mecord_crawler/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-21 03:07:22.323135 p-template-crawler-0.0.8/mecord_crawler/bin/
--rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-crawler-0.0.8/mecord_crawler/bin/__init__.py
--rw-rw-rw-   0        0        0     6178 2023-03-21 02:07:32.000000 p-template-crawler-0.0.8/mecord_crawler/main.py
--rw-rw-rw-   0        0        0     4857 2023-03-21 03:07:17.000000 p-template-crawler-0.0.8/mecord_crawler/utils.py
-drwxrwxrwx   0        0        0        0 2023-03-21 03:07:22.329136 p-template-crawler-0.0.8/p_template_crawler.egg-info/
--rw-rw-rw-   0        0        0      405 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      385 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       53 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       14 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-03-21 03:07:22.000000 p-template-crawler-0.0.8/p_template_crawler.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-21 03:07:22.330135 p-template-crawler-0.0.8/setup.cfg
--rw-rw-rw-   0        0        0      837 2023-03-21 03:02:14.000000 p-template-crawler-0.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-21 03:16:03.735860 p-template-crawler-0.0.9/
+-rw-rw-rw-   0        0        0     1074 2023-02-27 11:23:20.000000 p-template-crawler-0.0.9/LICENSE
+-rw-rw-rw-   0        0        0      405 2023-03-21 03:16:03.735860 p-template-crawler-0.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0       20 2023-03-14 06:24:47.000000 p-template-crawler-0.0.9/README.md
+drwxrwxrwx   0        0        0        0 2023-03-21 03:16:03.728860 p-template-crawler-0.0.9/mecord_crawler/
+-rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-crawler-0.0.9/mecord_crawler/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-21 03:16:03.729860 p-template-crawler-0.0.9/mecord_crawler/bin/
+-rw-rw-rw-   0        0        0        0 2023-03-01 01:46:57.000000 p-template-crawler-0.0.9/mecord_crawler/bin/__init__.py
+-rw-rw-rw-   0        0        0     6178 2023-03-21 02:07:32.000000 p-template-crawler-0.0.9/mecord_crawler/main.py
+-rw-rw-rw-   0        0        0     4989 2023-03-21 03:15:47.000000 p-template-crawler-0.0.9/mecord_crawler/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-21 03:16:03.734861 p-template-crawler-0.0.9/p_template_crawler.egg-info/
+-rw-rw-rw-   0        0        0      405 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      385 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       14 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-03-21 03:16:03.000000 p-template-crawler-0.0.9/p_template_crawler.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-03-21 03:16:03.735860 p-template-crawler-0.0.9/setup.cfg
+-rw-rw-rw-   0        0        0      837 2023-03-21 03:15:55.000000 p-template-crawler-0.0.9/setup.py
```

### Comparing `p-template-crawler-0.0.8/LICENSE` & `p-template-crawler-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `p-template-crawler-0.0.8/mecord_crawler/main.py` & `p-template-crawler-0.0.9/mecord_crawler/main.py`

 * *Files identical despite different names*

### Comparing `p-template-crawler-0.0.8/mecord_crawler/utils.py` & `p-template-crawler-0.0.9/mecord_crawler/utils.py`

 * *Files 6% similar despite different names*

```diff
@@ -43,14 +43,18 @@
 def ffmpegBinary():
     binDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
     updateBin(binDir)
     if sys.platform == "win32":
         return os.path.join(binDir, "ffmpeg", "win", "ffmpeg.exe")
     elif sys.platform == "linux":
         machine = platform.machine().lower()
+        if machine == "x86_64" or machine == "amd64":
+            machine = "amd64"
+        else:
+            machine = "arm64"
         return os.path.join(binDir, "ffmpeg", "linux", machine, "ffmpeg")
     elif sys.platform == "darwin":
         return os.path.join(binDir, "ffmpeg", "darwin", "ffmpeg")
     else:
         return ""
     
 def ffmpegTest():
```

### Comparing `p-template-crawler-0.0.8/setup.py` & `p-template-crawler-0.0.9/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 setuptools.setup(
     name="p-template-crawler",
-    version="0.0.8",
+    version="0.0.9",
     author="pengjun",
     author_email="mr_lonely@foxmail.com",
     description="template tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
```

