# Comparing `tmp/sog-devops-client-0.0.1.tar.gz` & `tmp/sog-devops-client-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sog-devops-client-0.0.1.tar", last modified: Thu Apr  6 09:15:58 2023, max compression
+gzip compressed data, was "sog-devops-client-1.0.0.tar", last modified: Thu Apr  6 09:17:26 2023, max compression
```

## Comparing `sog-devops-client-0.0.1.tar` & `sog-devops-client-1.0.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 09:15:58.488680 sog-devops-client-0.0.1/
--rw-rw-rw-   0        0        0     1092 2023-03-31 09:21:16.000000 sog-devops-client-0.0.1/LICENSE
--rw-rw-rw-   0        0        0     1544 2023-04-06 09:15:58.487682 sog-devops-client-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      985 2023-04-06 07:46:50.000000 sog-devops-client-0.0.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 09:15:58.457681 sog-devops-client-0.0.1/generate/
--rw-rw-rw-   0        0        0        0 2023-03-31 09:52:03.000000 sog-devops-client-0.0.1/generate/__init__.py
--rw-rw-rw-   0        0        0     3812 2023-04-06 08:39:49.000000 sog-devops-client-0.0.1/generate/generate.py
--rw-rw-rw-   0        0        0       88 2023-03-31 09:06:53.000000 sog-devops-client-0.0.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 09:15:58.488680 sog-devops-client-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      875 2023-04-06 09:13:51.000000 sog-devops-client-0.0.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 09:15:58.486698 sog-devops-client-0.0.1/sog_devops_client.egg-info/
--rw-rw-rw-   0        0        0     1544 2023-04-06 09:15:58.000000 sog-devops-client-0.0.1/sog_devops_client.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      309 2023-04-06 09:15:58.000000 sog-devops-client-0.0.1/sog_devops_client.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 09:15:58.000000 sog-devops-client-0.0.1/sog_devops_client.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       33 2023-04-06 09:15:58.000000 sog-devops-client-0.0.1/sog_devops_client.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-06 09:15:58.000000 sog-devops-client-0.0.1/sog_devops_client.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-06 09:15:58.487682 sog-devops-client-0.0.1/test/
--rw-rw-rw-   0        0        0      987 2023-04-06 08:44:57.000000 sog-devops-client-0.0.1/test/test_generate.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:17:26.463725 sog-devops-client-1.0.0/
+-rw-rw-rw-   0        0        0     1092 2023-03-31 09:21:16.000000 sog-devops-client-1.0.0/LICENSE
+-rw-rw-rw-   0        0        0     1544 2023-04-06 09:17:26.462723 sog-devops-client-1.0.0/PKG-INFO
+-rw-rw-rw-   0        0        0      985 2023-04-06 07:46:50.000000 sog-devops-client-1.0.0/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 09:17:26.450723 sog-devops-client-1.0.0/generate/
+-rw-rw-rw-   0        0        0        0 2023-03-31 09:52:03.000000 sog-devops-client-1.0.0/generate/__init__.py
+-rw-rw-rw-   0        0        0     3812 2023-04-06 08:39:49.000000 sog-devops-client-1.0.0/generate/generate.py
+-rw-rw-rw-   0        0        0       88 2023-03-31 09:06:53.000000 sog-devops-client-1.0.0/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:17:26.463725 sog-devops-client-1.0.0/setup.cfg
+-rw-rw-rw-   0        0        0      875 2023-04-06 09:17:15.000000 sog-devops-client-1.0.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:17:26.461723 sog-devops-client-1.0.0/sog_devops_client.egg-info/
+-rw-rw-rw-   0        0        0     1544 2023-04-06 09:17:26.000000 sog-devops-client-1.0.0/sog_devops_client.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      309 2023-04-06 09:17:26.000000 sog-devops-client-1.0.0/sog_devops_client.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:17:26.000000 sog-devops-client-1.0.0/sog_devops_client.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       33 2023-04-06 09:17:26.000000 sog-devops-client-1.0.0/sog_devops_client.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 09:17:26.000000 sog-devops-client-1.0.0/sog_devops_client.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 09:17:26.462723 sog-devops-client-1.0.0/test/
+-rw-rw-rw-   0        0        0      987 2023-04-06 08:44:57.000000 sog-devops-client-1.0.0/test/test_generate.py
```

### Comparing `sog-devops-client-0.0.1/LICENSE` & `sog-devops-client-1.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `sog-devops-client-0.0.1/PKG-INFO` & `sog-devops-client-1.0.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sog-devops-client
-Version: 0.0.1
+Version: 1.0.0
 Author: v-yangchao
 Author-email: v-yangchao@sinooceangroup.com
 License: Apache
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Natural Language :: English
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

### Comparing `sog-devops-client-0.0.1/README.md` & `sog-devops-client-1.0.0/README.md`

 * *Files identical despite different names*

### Comparing `sog-devops-client-0.0.1/generate/generate.py` & `sog-devops-client-1.0.0/generate/generate.py`

 * *Files identical despite different names*

### Comparing `sog-devops-client-0.0.1/setup.py` & `sog-devops-client-1.0.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
 	name = "sog-devops-client",
-	version = '0.0.1',
+	version = '1.0.0',
   author ="v-yangchao",
   author_email = "v-yangchao@sinooceangroup.com",
   long_description_content_type="text/markdown",
 	long_description = open('README.md',encoding="utf-8").read(),
   python_requires=">=3.6",
   install_requires=['requests>=2.26.0', 'tenacity>=8.2.1'],
 	packages = find_packages(),
```

### Comparing `sog-devops-client-0.0.1/sog_devops_client.egg-info/PKG-INFO` & `sog-devops-client-1.0.0/sog_devops_client.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sog-devops-client
-Version: 0.0.1
+Version: 1.0.0
 Author: v-yangchao
 Author-email: v-yangchao@sinooceangroup.com
 License: Apache
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Natural Language :: English
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

### Comparing `sog-devops-client-0.0.1/test/test_generate.py` & `sog-devops-client-1.0.0/test/test_generate.py`

 * *Files identical despite different names*

