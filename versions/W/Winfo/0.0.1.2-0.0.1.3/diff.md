# Comparing `tmp/Winfo-0.0.1.2.tar.gz` & `tmp/Winfo-0.0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Winfo-0.0.1.2.tar", last modified: Fri Apr  7 13:57:37 2023, max compression
+gzip compressed data, was "Winfo-0.0.1.3.tar", last modified: Fri Apr  7 14:52:43 2023, max compression
```

## Comparing `Winfo-0.0.1.2.tar` & `Winfo-0.0.1.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.810587 Winfo-0.0.1.2/
--rw-rw-rw-   0        0        0     1156 2023-04-07 10:35:15.000000 Winfo-0.0.1.2/LICENSE
--rw-rw-rw-   0        0        0     4296 2023-04-07 13:57:37.809587 Winfo-0.0.1.2/PKG-INFO
--rw-rw-rw-   0        0        0     3803 2023-04-07 09:58:38.000000 Winfo-0.0.1.2/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.790586 Winfo-0.0.1.2/Winfo/
--rw-rw-rw-   0        0        0     6855 2023-04-07 13:49:40.000000 Winfo-0.0.1.2/Winfo/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.808585 Winfo-0.0.1.2/Winfo.egg-info/
--rw-rw-rw-   0        0        0     4296 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      160 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 13:57:37.810587 Winfo-0.0.1.2/setup.cfg
--rw-rw-rw-   0        0        0      728 2023-04-07 13:54:42.000000 Winfo-0.0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:43.258851 Winfo-0.0.1.3/
+-rw-rw-rw-   0        0        0     1156 2023-04-07 10:35:15.000000 Winfo-0.0.1.3/LICENSE
+-rw-rw-rw-   0        0        0     4165 2023-04-07 14:52:43.257854 Winfo-0.0.1.3/PKG-INFO
+-rw-rw-rw-   0        0        0     3672 2023-04-07 14:51:25.000000 Winfo-0.0.1.3/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:43.241128 Winfo-0.0.1.3/Winfo/
+-rw-rw-rw-   0        0        0     6855 2023-04-07 13:49:40.000000 Winfo-0.0.1.3/Winfo/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:43.257136 Winfo-0.0.1.3/Winfo.egg-info/
+-rw-rw-rw-   0        0        0     4165 2023-04-07 14:52:43.000000 Winfo-0.0.1.3/Winfo.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      160 2023-04-07 14:52:43.000000 Winfo-0.0.1.3/Winfo.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:52:43.000000 Winfo-0.0.1.3/Winfo.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 14:52:43.000000 Winfo-0.0.1.3/Winfo.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:52:43.258851 Winfo-0.0.1.3/setup.cfg
+-rw-rw-rw-   0        0        0      728 2023-04-07 14:51:42.000000 Winfo-0.0.1.3/setup.py
```

### Comparing `Winfo-0.0.1.2/LICENSE` & `Winfo-0.0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `Winfo-0.0.1.2/PKG-INFO` & `Winfo-0.0.1.3/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Winfo
-Version: 0.0.1.2
+Version: 0.0.1.3
 Summary: Get information about your windows system
 Author: BLUEAMETHYST Studios
 Author-email: simon.schoeneberg@t-online.de
 Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
@@ -111,16 +111,16 @@
 import Winfo
 
 print("I'm current running Windows " + Winfo.software.system() + " on version " + Winfo.software.version())
 print("I named my computer " + Winfo.software.devicename())
 print("I'm logged in as " + Winfo.software.username())
 ```
 ## Questions you might have:
-- Q: Is this on PyPi?, A: Current not but soon
-- Q: How can I install this then?, A: By cloning the repo in to this directory "C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib"
+
+- Q: How can I install this library? A: pip install Winfo
 - Q: MacOS/Linux/BSD Support? A: Windows-only.
 - Q: What can I do with the code? A: Read the license (CC BY-SA 4.0)
 
 ### If you've further questions, join our [discord](https://discord.gg/jDAGR26yXe)!
 
 ## License
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.2 Summary: Get information
+Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.3 Summary: Get information
 about your windows system Author: BLUEAMETHYST Studios Author-email:
 simon.schoeneberg@t-online.de Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning Classifier: Intended Audience ::
 Developers Classifier: Programming Language :: Python :: 3 Classifier:
 Operating System :: Microsoft :: Windows Description-Content-Type: text/
 markdown License-File: LICENSE # Winfo Winfo is a Python Library for getting
 System Stats (Made for Windows) ## Features List of all features: ### Processor
@@ -30,18 +30,16 @@
 (prettylist) ``` - Instead of looking like this when printed: ``` ['Disk 0',
 'Disk 1', 'Disk 2'] ``` - It would now look like this: ``` Disk 0 Disk 1 Disk 2
 ``` ### Software Information - Get current Windows version - Get current
 Windows release - Get device name - Get user name ```Python import Winfo print
 ("I'm current running Windows " + Winfo.software.system() + " on version " +
 Winfo.software.version()) print("I named my computer " +
 Winfo.software.devicename()) print("I'm logged in as " +
-Winfo.software.username()) ``` ## Questions you might have: - Q: Is this on
-PyPi?, A: Current not but soon - Q: How can I install this then?, A: By cloning
-the repo in to this directory "C:
-\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib" - Q: MacOS/Linux/
-BSD Support? A: Windows-only. - Q: What can I do with the code? A: Read the
-license (CC BY-SA 4.0) ### If you've further questions, join our [discord]
-(https://discord.gg/jDAGR26yXe)! ## License
+Winfo.software.username()) ``` ## Questions you might have: - Q: How can I
+install this library? A: pip install Winfo - Q: MacOS/Linux/BSD Support? A:
+Windows-only. - Q: What can I do with the code? A: Read the license (CC BY-SA
+4.0) ### If you've further questions, join our [discord](https://discord.gg/
+jDAGR26yXe)! ## License
 Winfo by BLUEAMETHYST_Studios is licensed under CC_BY-SA_4.0[https://
 mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1]
```

### Comparing `Winfo-0.0.1.2/README.md` & `Winfo-0.0.1.3/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -97,16 +97,16 @@
 import Winfo
 
 print("I'm current running Windows " + Winfo.software.system() + " on version " + Winfo.software.version())
 print("I named my computer " + Winfo.software.devicename())
 print("I'm logged in as " + Winfo.software.username())
 ```
 ## Questions you might have:
-- Q: Is this on PyPi?, A: Current not but soon
-- Q: How can I install this then?, A: By cloning the repo in to this directory "C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib"
+
+- Q: How can I install this library? A: pip install Winfo
 - Q: MacOS/Linux/BSD Support? A: Windows-only.
 - Q: What can I do with the code? A: Read the license (CC BY-SA 4.0)
 
 ### If you've further questions, join our [discord](https://discord.gg/jDAGR26yXe)!
 
 ## License
```

#### html2text {}

```diff
@@ -24,18 +24,16 @@
 (prettylist) ``` - Instead of looking like this when printed: ``` ['Disk 0',
 'Disk 1', 'Disk 2'] ``` - It would now look like this: ``` Disk 0 Disk 1 Disk 2
 ``` ### Software Information - Get current Windows version - Get current
 Windows release - Get device name - Get user name ```Python import Winfo print
 ("I'm current running Windows " + Winfo.software.system() + " on version " +
 Winfo.software.version()) print("I named my computer " +
 Winfo.software.devicename()) print("I'm logged in as " +
-Winfo.software.username()) ``` ## Questions you might have: - Q: Is this on
-PyPi?, A: Current not but soon - Q: How can I install this then?, A: By cloning
-the repo in to this directory "C:
-\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib" - Q: MacOS/Linux/
-BSD Support? A: Windows-only. - Q: What can I do with the code? A: Read the
-license (CC BY-SA 4.0) ### If you've further questions, join our [discord]
-(https://discord.gg/jDAGR26yXe)! ## License
+Winfo.software.username()) ``` ## Questions you might have: - Q: How can I
+install this library? A: pip install Winfo - Q: MacOS/Linux/BSD Support? A:
+Windows-only. - Q: What can I do with the code? A: Read the license (CC BY-SA
+4.0) ### If you've further questions, join our [discord](https://discord.gg/
+jDAGR26yXe)! ## License
 Winfo by BLUEAMETHYST_Studios is licensed under CC_BY-SA_4.0[https://
 mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1]
```

### Comparing `Winfo-0.0.1.2/Winfo/__init__.py` & `Winfo-0.0.1.3/Winfo/__init__.py`

 * *Files identical despite different names*

### Comparing `Winfo-0.0.1.2/Winfo.egg-info/PKG-INFO` & `Winfo-0.0.1.3/Winfo.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Winfo
-Version: 0.0.1.2
+Version: 0.0.1.3
 Summary: Get information about your windows system
 Author: BLUEAMETHYST Studios
 Author-email: simon.schoeneberg@t-online.de
 Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
@@ -111,16 +111,16 @@
 import Winfo
 
 print("I'm current running Windows " + Winfo.software.system() + " on version " + Winfo.software.version())
 print("I named my computer " + Winfo.software.devicename())
 print("I'm logged in as " + Winfo.software.username())
 ```
 ## Questions you might have:
-- Q: Is this on PyPi?, A: Current not but soon
-- Q: How can I install this then?, A: By cloning the repo in to this directory "C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib"
+
+- Q: How can I install this library? A: pip install Winfo
 - Q: MacOS/Linux/BSD Support? A: Windows-only.
 - Q: What can I do with the code? A: Read the license (CC BY-SA 4.0)
 
 ### If you've further questions, join our [discord](https://discord.gg/jDAGR26yXe)!
 
 ## License
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.2 Summary: Get information
+Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.3 Summary: Get information
 about your windows system Author: BLUEAMETHYST Studios Author-email:
 simon.schoeneberg@t-online.de Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning Classifier: Intended Audience ::
 Developers Classifier: Programming Language :: Python :: 3 Classifier:
 Operating System :: Microsoft :: Windows Description-Content-Type: text/
 markdown License-File: LICENSE # Winfo Winfo is a Python Library for getting
 System Stats (Made for Windows) ## Features List of all features: ### Processor
@@ -30,18 +30,16 @@
 (prettylist) ``` - Instead of looking like this when printed: ``` ['Disk 0',
 'Disk 1', 'Disk 2'] ``` - It would now look like this: ``` Disk 0 Disk 1 Disk 2
 ``` ### Software Information - Get current Windows version - Get current
 Windows release - Get device name - Get user name ```Python import Winfo print
 ("I'm current running Windows " + Winfo.software.system() + " on version " +
 Winfo.software.version()) print("I named my computer " +
 Winfo.software.devicename()) print("I'm logged in as " +
-Winfo.software.username()) ``` ## Questions you might have: - Q: Is this on
-PyPi?, A: Current not but soon - Q: How can I install this then?, A: By cloning
-the repo in to this directory "C:
-\Users\USERNAME\AppData\Local\Programs\Python\Python311\Lib" - Q: MacOS/Linux/
-BSD Support? A: Windows-only. - Q: What can I do with the code? A: Read the
-license (CC BY-SA 4.0) ### If you've further questions, join our [discord]
-(https://discord.gg/jDAGR26yXe)! ## License
+Winfo.software.username()) ``` ## Questions you might have: - Q: How can I
+install this library? A: pip install Winfo - Q: MacOS/Linux/BSD Support? A:
+Windows-only. - Q: What can I do with the code? A: Read the license (CC BY-SA
+4.0) ### If you've further questions, join our [discord](https://discord.gg/
+jDAGR26yXe)! ## License
 Winfo by BLUEAMETHYST_Studios is licensed under CC_BY-SA_4.0[https://
 mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1][https://
 mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1]
```

### Comparing `Winfo-0.0.1.2/setup.py` & `Winfo-0.0.1.3/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 with open("README.md", "r") as f:
     readme = f.read()
     f.close()
     
 setup(
     name="Winfo",
-    version="0.0.1.2",
+    version="0.0.1.3",
     author="BLUEAMETHYST Studios",
     author_email="simon.schoeneberg@t-online.de",
     description="Get information about your windows system",
     long_description_content_type="text/markdown",
     long_description=readme,
     packages=find_packages(),
     keywords=['python', 'windows', 'util', 'information', 'system'],
```

