# Comparing `tmp/sroll-0.2.9.1.tar.gz` & `tmp/sroll-0.2.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/sroll-0.2.9.1.tar", last modified: Thu Mar 16 15:18:13 2023, max compression
+gzip compressed data, was "dist/sroll-0.2.9.2.tar", last modified: Thu Apr  6 09:52:05 2023, max compression
```

## Comparing `sroll-0.2.9.1.tar` & `sroll-0.2.9.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-03-16 15:18:13.000000 sroll-0.2.9.1/
--rw-r--r--   0 tfoulqui (205105) droos    (10042)       38 2023-03-16 15:18:13.000000 sroll-0.2.9.1/setup.cfg
--rw-r--r--   0 tfoulqui (205105) droos    (10042)       46 2023-01-26 14:13:59.000000 sroll-0.2.9.1/MANIFEST.in
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      787 2023-03-16 15:17:55.000000 sroll-0.2.9.1/setup.py
-drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/
--rw-r--r--   0 tfoulqui (205105) droos    (10042)        1 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/dependency_links.txt
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      253 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/SOURCES.txt
--rw-r--r--   0 tfoulqui (205105) droos    (10042)       21 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/requires.txt
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      506 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/PKG-INFO
--rw-r--r--   0 tfoulqui (205105) droos    (10042)       14 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll.egg-info/top_level.txt
-drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll_package/
--rw-r--r--   0 tfoulqui (205105) droos    (10042)     8230 2023-03-16 15:05:13.000000 sroll-0.2.9.1/sroll_package/set_env.py
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      142 2023-01-26 14:13:59.000000 sroll-0.2.9.1/sroll_package/__init__.py
-drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-03-16 15:18:13.000000 sroll-0.2.9.1/sroll_package/static/
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      807 2023-03-16 15:17:45.000000 sroll-0.2.9.1/sroll_package/static/requirements.txt
--rw-r--r--   0 tfoulqui (205105) droos    (10042)      506 2023-03-16 15:18:13.000000 sroll-0.2.9.1/PKG-INFO
+drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-04-06 09:52:05.000000 sroll-0.2.9.2/
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)       38 2023-04-06 09:52:05.000000 sroll-0.2.9.2/setup.cfg
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)       46 2023-01-26 14:13:59.000000 sroll-0.2.9.2/MANIFEST.in
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      787 2023-04-06 09:51:49.000000 sroll-0.2.9.2/setup.py
+drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)        1 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/dependency_links.txt
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      253 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/SOURCES.txt
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)       21 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/requires.txt
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      506 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/PKG-INFO
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)       14 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll.egg-info/top_level.txt
+drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll_package/
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)     8266 2023-04-06 09:50:23.000000 sroll-0.2.9.2/sroll_package/set_env.py
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      142 2023-01-26 14:13:59.000000 sroll-0.2.9.2/sroll_package/__init__.py
+drwxr-xr-x   0 tfoulqui (205105) droos    (10042)        0 2023-04-06 09:52:05.000000 sroll-0.2.9.2/sroll_package/static/
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      793 2023-03-29 12:59:48.000000 sroll-0.2.9.2/sroll_package/static/requirements.txt
+-rw-r--r--   0 tfoulqui (205105) droos    (10042)      506 2023-04-06 09:52:05.000000 sroll-0.2.9.2/PKG-INFO
```

### Comparing `sroll-0.2.9.1/setup.py` & `sroll-0.2.9.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from pathlib import Path
 
 
 
 
 setuptools.setup(
     name='sroll',
-    version='0.2.9.1',    
+    version='0.2.9.2',    
     description='Python package for SRoll installation',    
     url='https://gitlab.ifremer.fr/iaocea/srollex.git',
     author='Theo Foulquier',
     author_email='tfoulqui@ifremer.fr',
     license='BSD 2-clause',
     include_package_data = True,
     packages=['sroll_package'],
```

### Comparing `sroll-0.2.9.1/sroll_package/set_env.py` & `sroll-0.2.9.2/sroll_package/set_env.py`

 * *Files 6% similar despite different names*

```diff
@@ -23,20 +23,20 @@
   os.system('mkdir -p '+str(vecout))
   
   # Read in the file
   with open(str(path)+"/srollex/sroll4/unit_test_"+str(name)+".py", 'r') as file :
     filedata = file.read()
 
   # Replace the target string
-  filedata = filedata.replace(' MAP = ',' MAP = ["'+str(mapout)+'%s%s"%(OMAP,i) for i in bolo_map]')
-  filedata = filedata.replace('Out_VEC = ','Out_VEC = ["'+str(vecout)+'%s%s"%(OMAP,i) for i in bolo]')
-  filedata = filedata.replace('Out_Offset = ','Out_Offset = ["'+str(vecout)+'%s%s"%(OMAP,i) for i in bolo]')
-  filedata = filedata.replace('Out_Offset_corr = ','Out_Offset_corr = ["'+str(vecout)+'%s%s"%(OMAP,i) for i in bolo]')
-  filedata = filedata.replace('Out_xi2 = ','Out_xi2 = ["'+str(vecout)+'%s%s"%(OMAP,i) for i in bolo]')
-  filedata = filedata.replace('Out_xi2_corr = ','Out_xi2_corr = ["'+str(vecout)+'%s%s"%(OMAP,i) for i in bolo]')
+  filedata = filedata.replace(' MAP = ',' MAP = ["'+str(mapout)+'Nside%s%s"%(Nside,i) for i in bolo_map]')
+  filedata = filedata.replace('Out_VEC = ','Out_VEC = ["'+str(vecout)+'Nside%s%s"%(Nside,i) for i in bolo]')
+  filedata = filedata.replace('Out_Offset = ','Out_Offset = ["'+str(vecout)+'Nside%s%s"%(Nside,i) for i in bolo]')
+  filedata = filedata.replace('Out_Offset_corr = ','Out_Offset_corr = ["'+str(vecout)+'Nside%s%s"%(Nside,i) for i in bolo]')
+  filedata = filedata.replace('Out_xi2 = ','Out_xi2 = ["'+str(vecout)+'Nside%s%s"%(Nside,i) for i in bolo]')
+  filedata = filedata.replace('Out_xi2_corr = ','Out_xi2_corr = ["'+str(vecout)+'Nside%s%s"%(Nside,i) for i in bolo]')
 
 
   # Write the file out again
   with open(str(path)+"/srollex/sroll4/unit_test_"+str(name)+".py", 'w') as file:
     file.write(filedata)
```

### Comparing `sroll-0.2.9.1/sroll_package/static/requirements.txt` & `sroll-0.2.9.2/sroll_package/static/requirements.txt`

 * *Files 12% similar despite different names*

```diff
@@ -31,17 +31,16 @@
 pyparsing==2.4.7
 python-dateutil==2.8.1
 requests==2.25.1
 requests-oauthlib==1.3.0
 rsa==4.7.2
 scipy==1.4.1
 six==1.15.0
-tensorflow==2.1.0
+tensorflow==2.2.0
 termcolor==1.1.0
 typing-extensions==3.7.4.3
 urllib3==1.26.4
 Werkzeug==1.0.1
 wrapt==1.12.1
 zipp==3.4.1
-foscat==1.9.1
 healpy==1.14.0
 Cython==0.29.33
```

