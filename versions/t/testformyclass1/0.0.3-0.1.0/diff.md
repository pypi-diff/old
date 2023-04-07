# Comparing `tmp/testformyclass1-0.0.3.tar.gz` & `tmp/testformyclass1-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "testformyclass1-0.0.3.tar", last modified: Fri Apr  7 07:36:26 2023, max compression
+gzip compressed data, was "testformyclass1-0.1.0.tar", last modified: Fri Apr  7 05:37:33 2023, max compression
```

## Comparing `testformyclass1-0.0.3.tar` & `testformyclass1-0.1.0.tar`

### file list

```diff
@@ -1,23 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.911348 testformyclass1-0.0.3/
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.890852 testformyclass1-0.0.3/.pytest_cache/
--rw-rw-rw-   0        0        0      310 2023-04-07 06:33:17.000000 testformyclass1-0.0.3/.pytest_cache/README.md
--rw-rw-rw-   0        0        0       75 2023-04-07 07:35:52.000000 testformyclass1-0.0.3/CHANGELOG.md
--rw-rw-rw-   0        0        0     1070 2022-06-20 00:06:04.000000 testformyclass1-0.0.3/LICENSE
--rw-rw-rw-   0        0        0       31 2023-04-07 06:59:07.000000 testformyclass1-0.0.3/MANIFEST.in
--rw-rw-rw-   0        0        0     8699 2023-04-07 07:36:26.911348 testformyclass1-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0     7474 2022-06-20 00:06:04.000000 testformyclass1-0.0.3/README.md
--rw-rw-rw-   0        0        0       96 2022-06-20 00:06:04.000000 testformyclass1-0.0.3/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 07:36:26.912325 testformyclass1-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0     4478 2023-04-07 07:34:05.000000 testformyclass1-0.0.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.879141 testformyclass1-0.0.3/testformyclasspks1/
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.902565 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/
--rw-rw-rw-   0        0        0     8699 2023-04-07 07:36:26.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      517 2023-04-07 07:36:26.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 07:36:26.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       14 2023-04-07 07:36:26.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/requires.txt
--rw-rw-rw-   0        0        0       43 2023-04-07 07:36:26.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.906468 testformyclass1-0.0.3/testformyclasspks1/testformyclassmodules1/
--rw-rw-rw-   0        0        0      199 2022-06-20 00:06:04.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclassmodules1/__init__.py
--rw-rw-rw-   0        0        0      213 2023-04-07 05:27:44.000000 testformyclass1-0.0.3/testformyclasspks1/testformyclassmodules1/testformyclassfile1.py
-drwxrwxrwx   0        0        0        0 2023-04-07 07:36:26.909397 testformyclass1-0.0.3/tests/
--rw-rw-rw-   0        0        0      176 2023-04-07 06:48:16.000000 testformyclass1-0.0.3/tests/test_code.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:37:33.297333 testformyclass1-0.1.0/
+-rw-rw-rw-   0        0        0     1070 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/LICENSE
+-rw-rw-rw-   0        0        0       26 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/MANIFEST.in
+-rw-rw-rw-   0        0        0     8784 2023-04-07 05:37:33.297333 testformyclass1-0.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0     7474 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/README.md
+-rw-rw-rw-   0        0        0       96 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 05:37:33.297333 testformyclass1-0.1.0/setup.cfg
+-rw-rw-rw-   0        0        0     4297 2023-04-07 05:35:27.000000 testformyclass1-0.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:37:33.266102 testformyclass1-0.1.0/testformyclasspks1/
+drwxrwxrwx   0        0        0        0 2023-04-07 05:37:33.287573 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/
+-rw-rw-rw-   0        0        0     8784 2023-04-07 05:37:33.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      480 2023-04-07 05:37:33.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 05:37:33.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       14 2023-04-07 05:37:33.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       43 2023-04-07 05:37:33.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 05:37:33.293429 testformyclass1-0.1.0/testformyclasspks1/testformyclassmodules1/
+-rw-rw-rw-   0        0        0      199 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclassmodules1/__init__.py
+-rw-rw-rw-   0        0        0      213 2023-04-07 05:27:44.000000 testformyclass1-0.1.0/testformyclasspks1/testformyclassmodules1/testformyclassfile1.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:37:33.294405 testformyclass1-0.1.0/tests/
+-rw-rw-rw-   0        0        0      132 2022-06-20 00:06:04.000000 testformyclass1-0.1.0/tests/test_code.py
```

### Comparing `testformyclass1-0.0.3/LICENSE` & `testformyclass1-0.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `testformyclass1-0.0.3/PKG-INFO` & `testformyclass1-0.1.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: testformyclass1
-Version: 0.0.3
+Version: 0.1.0
 Summary: An NLP python package for computing Boilerplate score and many other text features.
 Home-page: https://github.com/myNKUST/testformyclass.git
 Author: timenet2300
 Author-email: timenet2300@gmail.com
 Keywords: Text Mining,Data Science
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
@@ -192,7 +192,15 @@
 
 ## A few tips
 
 - Whenever you want to update your package, you should remove the 'build' and 'dist' folders, make changes to your code, edit the "CHANGLOG.txt" file, and revise the version number in the "setup.py". And repeat steps 5–7.
 - You may upgrade your package after the updates by doing this: ___pip install YOURPACKAGENAME --upgrade___
 - You can always find your package on PyPi here: ___ht<span>tp://</span>pypi.org/project/YOURPACKAGENAME/___
 - Do not publish packages arbitrarily. Even though there are no hard restrictions on what you can or cannot publish, make sure you are uploading something that is actually meaningful and someone will benefit from your work. 
+
+
+# CHANGELOG
+
+## Version 0.0.1 MM/DD/YYYY
+1. Upaded ...
+2. Fixed ...
+3. ...
```

### Comparing `testformyclass1-0.0.3/README.md` & `testformyclass1-0.1.0/README.md`

 * *Files identical despite different names*

### Comparing `testformyclass1-0.0.3/setup.py` & `testformyclass1-0.1.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,43 +1,43 @@
-# from setuptools import setup
-from setuptools import setup, find_packages
+from setuptools import setup
 
-with open("README.md", "r") as file:
-    long_description = file.read()
 ######################################################################################################
 ################ You May Remove All the Comments Once You Finish Modifying the Script ################
 ######################################################################################################
 
 setup(    
     #'''不能有three quotes '''
     # This name will be used when people try to do pip install. And it is CASE SENSITIVE. 
     # You should create an unique name. Search on pypi.org to see if the name is taken or not.
     #'''
     name = 'testformyclass1', 
     package_dir = {'':'testformyclasspks1'},
     packages = ['testformyclassmodules1',
                  # 'ThePackageName2',              
-  ],  
-    #'''
-    #This is the name of your main module file. No need to include the .py at the end.
-    #'''    
+  ],
     py_modules = ["testformyclassfile1"],
-    version = '0.0.3', #also check changelog.md version  
+        
     #'''
     #The version number of your package consists of three integers "Major.Minor.Patch".
     #Typically, when you fix a bug, that will lead to a patch release. (e.g. 0.1.1 --> 0.1.2)
     #If you add a new feature to your package, that will lead to a minor release. (e.g. 0.1.0 --> 0.2.0)
     #If a major change that will affect many users happened, you will want to make it as a major release (e.g. 0.1.0 --> 1.0.0)
     #'''
-      
+    version = '0.1.0',
+    
     #'''
     #This is the short description will show on the top of the webpage of your package on pypi.org
     #'''
     description = 'An NLP python package for computing Boilerplate score and many other text features.',
-       
+    
+    #'''
+    #This is the name of your main module file. No need to include the .py at the end.
+    #'''    
+    
+    
     #'''
     #Leave it as default. It shows where the module is stored.
     #'''
     
     
     #'''
     #If you have many modules included in your package, you want to use the following parameter instead of py_modules.
@@ -48,16 +48,15 @@
     #'''
     author = 'timenet2300',
     author_email = 'timenet2300@gmail.com',
     
     #'''
     #Leave the following as default. It will show the readme and changelog on the main page of your package.
     #'''
-    #long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
-    long_description=long_description,
+    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
     long_description_content_type = "text/markdown",
     
     #'''
     #The url to where your package is stored for public view. Normally, it will be the github url to the repository you just forked.
     #'''
     # url='https://github.com/jinhangjiang/morethansentiments',
     # url='https://github.com/myNKUST/testformyclass.git',
```

### Comparing `testformyclass1-0.0.3/testformyclasspks1/testformyclass1.egg-info/PKG-INFO` & `testformyclass1-0.1.0/testformyclasspks1/testformyclass1.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: testformyclass1
-Version: 0.0.3
+Version: 0.1.0
 Summary: An NLP python package for computing Boilerplate score and many other text features.
 Home-page: https://github.com/myNKUST/testformyclass.git
 Author: timenet2300
 Author-email: timenet2300@gmail.com
 Keywords: Text Mining,Data Science
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
@@ -192,7 +192,15 @@
 
 ## A few tips
 
 - Whenever you want to update your package, you should remove the 'build' and 'dist' folders, make changes to your code, edit the "CHANGLOG.txt" file, and revise the version number in the "setup.py". And repeat steps 5–7.
 - You may upgrade your package after the updates by doing this: ___pip install YOURPACKAGENAME --upgrade___
 - You can always find your package on PyPi here: ___ht<span>tp://</span>pypi.org/project/YOURPACKAGENAME/___
 - Do not publish packages arbitrarily. Even though there are no hard restrictions on what you can or cannot publish, make sure you are uploading something that is actually meaningful and someone will benefit from your work. 
+
+
+# CHANGELOG
+
+## Version 0.0.1 MM/DD/YYYY
+1. Upaded ...
+2. Fixed ...
+3. ...
```

