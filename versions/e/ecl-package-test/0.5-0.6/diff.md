# Comparing `tmp/ecl-package-test-0.5.tar.gz` & `tmp/ecl-package-test-0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ecl-package-test-0.5.tar", last modified: Thu Apr  6 07:59:40 2023, max compression
+gzip compressed data, was "ecl-package-test-0.6.tar", last modified: Thu Apr  6 08:08:17 2023, max compression
```

## Comparing `ecl-package-test-0.5.tar` & `ecl-package-test-0.6.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 07:59:40.644361 ecl-package-test-0.5/
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)     5142 2023-04-06 07:59:40.633606 ecl-package-test-0.5/PKG-INFO
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)     4901 2023-04-02 14:43:52.000000 ecl-package-test-0.5/README.md
-drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 07:59:39.935742 ecl-package-test-0.5/bin/
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)       36 2023-04-02 14:37:57.000000 ecl-package-test-0.5/bin/package.cmd
-drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 07:59:40.180287 ecl-package-test-0.5/ecl_package_test.egg-info/
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)     5142 2023-04-06 07:59:39.000000 ecl-package-test-0.5/ecl_package_test.egg-info/PKG-INFO
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)      402 2023-04-06 07:59:39.000000 ecl-package-test-0.5/ecl_package_test.egg-info/SOURCES.txt
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)        1 2023-04-06 07:59:39.000000 ecl-package-test-0.5/ecl_package_test.egg-info/dependency_links.txt
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)       50 2023-04-06 07:59:39.000000 ecl-package-test-0.5/ecl_package_test.egg-info/entry_points.txt
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)        8 2023-04-06 07:59:39.000000 ecl-package-test-0.5/ecl_package_test.egg-info/top_level.txt
-drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 07:59:40.278727 ecl-package-test-0.5/package/
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)       24 2023-04-02 15:21:23.000000 ecl-package-test-0.5/package/__init__.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)      884 2023-04-06 07:59:16.000000 ecl-package-test-0.5/package/main.py
-drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 07:59:40.581329 ecl-package-test-0.5/package/src/
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)      116 2023-04-02 14:23:08.000000 ecl-package-test-0.5/package/src/__init__.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)     1413 2023-04-02 14:02:40.000000 ecl-package-test-0.5/package/src/cli.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)       77 2023-03-29 05:34:14.000000 ecl-package-test-0.5/package/src/copy_helper.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-03-29 05:42:48.000000 ecl-package-test-0.5/package/src/make_template.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)      437 2023-04-02 14:22:34.000000 ecl-package-test-0.5/package/src/replace_helper.py
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)       38 2023-04-06 07:59:40.646372 ecl-package-test-0.5/setup.cfg
--rwxrwxrwx   0 facerain  (1000) facerain  (1000)      742 2023-04-06 07:59:32.000000 ecl-package-test-0.5/setup.py
+drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 08:08:17.752282 ecl-package-test-0.6/
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)     5142 2023-04-06 08:08:17.747281 ecl-package-test-0.6/PKG-INFO
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)     4901 2023-04-02 14:43:52.000000 ecl-package-test-0.6/README.md
+drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 08:08:17.151316 ecl-package-test-0.6/bin/
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)       36 2023-04-02 14:37:57.000000 ecl-package-test-0.6/bin/package.cmd
+drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 08:08:17.348906 ecl-package-test-0.6/ecl_package_test.egg-info/
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)     5142 2023-04-06 08:08:16.000000 ecl-package-test-0.6/ecl_package_test.egg-info/PKG-INFO
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)      402 2023-04-06 08:08:16.000000 ecl-package-test-0.6/ecl_package_test.egg-info/SOURCES.txt
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)        1 2023-04-06 08:08:16.000000 ecl-package-test-0.6/ecl_package_test.egg-info/dependency_links.txt
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)       50 2023-04-06 08:08:16.000000 ecl-package-test-0.6/ecl_package_test.egg-info/entry_points.txt
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)        8 2023-04-06 08:08:16.000000 ecl-package-test-0.6/ecl_package_test.egg-info/top_level.txt
+drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 08:08:17.424989 ecl-package-test-0.6/package/
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)       24 2023-04-02 15:21:23.000000 ecl-package-test-0.6/package/__init__.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)      931 2023-04-06 08:06:10.000000 ecl-package-test-0.6/package/main.py
+drwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-04-06 08:08:17.708280 ecl-package-test-0.6/package/src/
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)      116 2023-04-02 14:23:08.000000 ecl-package-test-0.6/package/src/__init__.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)     1413 2023-04-02 14:02:40.000000 ecl-package-test-0.6/package/src/cli.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)       77 2023-03-29 05:34:14.000000 ecl-package-test-0.6/package/src/copy_helper.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)        0 2023-03-29 05:42:48.000000 ecl-package-test-0.6/package/src/make_template.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)      437 2023-04-02 14:22:34.000000 ecl-package-test-0.6/package/src/replace_helper.py
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)       38 2023-04-06 08:08:17.753281 ecl-package-test-0.6/setup.cfg
+-rwxrwxrwx   0 facerain  (1000) facerain  (1000)      742 2023-04-06 08:06:21.000000 ecl-package-test-0.6/setup.py
```

### Comparing `ecl-package-test-0.5/PKG-INFO` & `ecl-package-test-0.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ecl-package-test
-Version: 0.5
+Version: 0.6
 Summary: ecl package TBA
 Home-page: https://github.com/EarthCodingLab/ecl-package
 Author: Earth Coding Lab
 Author-email: syw5141@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ecl-package-test-0.5/README.md` & `ecl-package-test-0.6/README.md`

 * *Files identical despite different names*

### Comparing `ecl-package-test-0.5/ecl_package_test.egg-info/PKG-INFO` & `ecl-package-test-0.6/ecl_package_test.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ecl-package-test
-Version: 0.5
+Version: 0.6
 Summary: ecl package TBA
 Home-page: https://github.com/EarthCodingLab/ecl-package
 Author: Earth Coding Lab
 Author-email: syw5141@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ecl-package-test-0.5/package/main.py` & `ecl-package-test-0.6/package/main.py`

 * *Files 19% similar despite different names*

```diff
@@ -5,15 +5,17 @@
 from .src import add_import, copy_dir, main_cli, replace_code
 
 
 def generate_example():
     options = main_cli()
     print(options)
     copy_dir_path = options["project_name"]
-    template_path = os.path.join(os.getcwd(), "templates")
+    template_path = os.path.join(
+        os.path.dirname(os.path.abspath(__file__)), "templates"
+    )
 
     copy_dir(template_path, copy_dir_path)
 
     # logger
     logger_path = os.path.join(copy_dir_path, "main.py")
     replacement = "logger = None"
     if options["mlops"] == "Wandb":
```

### Comparing `ecl-package-test-0.5/package/src/cli.py` & `ecl-package-test-0.6/package/src/cli.py`

 * *Files identical despite different names*

### Comparing `ecl-package-test-0.5/setup.py` & `ecl-package-test-0.6/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import setuptools
 
 setuptools.setup(
     name="ecl-package-test",
-    version="0.05",
+    version="0.06",
     license="MIT",
     author="Earth Coding Lab",
     author_email="syw5141@gmail.com",
     description="ecl package TBA",
     url="https://github.com/EarthCodingLab/ecl-package",
     long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
```

