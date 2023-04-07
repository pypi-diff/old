# Comparing `tmp/fosslight_dependency-3.9.3.tar.gz` & `tmp/fosslight_dependency-3.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/fosslight_dependency-3.9.3.tar", last modified: Fri Mar 11 05:44:15 2022, max compression
+gzip compressed data, was "dist/fosslight_dependency-3.9.4.tar", last modified: Mon Apr 11 08:49:24 2022, max compression
```

## Comparing `fosslight_dependency-3.9.3.tar` & `fosslight_dependency-3.9.4.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/
--rw-r--r--   0 runner    (1001) docker     (116)    11357 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/LICENSE
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/LICENSES/
--rw-r--r--   0 runner    (1001) docker     (116)    11357 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/LICENSES/Apache-2.0.txt
--rw-r--r--   0 runner    (1001) docker     (116)    95687 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/LICENSES/LicenseRef-3rd_party_licenses.txt
--rw-r--r--   0 runner    (1001) docker     (116)     1082 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/LICENSES/MIT.txt
--rw-r--r--   0 runner    (1001) docker     (116)       78 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (116)     6377 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     5418 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/README.md
--rw-r--r--   0 runner    (1001) docker     (116)       91 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (116)       92 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     1517 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/src/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/
--rw-r--r--   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     3181 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/_analyze_dependency.py
--rw-r--r--   0 runner    (1001) docker     (116)     2364 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/_help.py
--rw-r--r--   0 runner    (1001) docker     (116)     6173 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/_package_manager.py
--rw-r--r--   0 runner    (1001) docker     (116)      795 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/constant.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/
--rw-r--r--   0 runner    (1001) docker     (116)     1929 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Android.py
--rw-r--r--   0 runner    (1001) docker     (116)     5006 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Carthage.py
--rw-r--r--   0 runner    (1001) docker     (116)     6221 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Cocoapods.py
--rw-r--r--   0 runner    (1001) docker     (116)     3767 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Go.py
--rw-r--r--   0 runner    (1001) docker     (116)     3166 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Gradle.py
--rw-r--r--   0 runner    (1001) docker     (116)     8202 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Maven.py
--rw-r--r--   0 runner    (1001) docker     (116)     4397 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Npm.py
--rw-r--r--   0 runner    (1001) docker     (116)     3018 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Pub.py
--rw-r--r--   0 runner    (1001) docker     (116)    10213 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Pypi.py
--rw-r--r--   0 runner    (1001) docker     (116)     2847 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Swift.py
--rw-r--r--   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (116)     8335 2022-03-11 05:44:00.000000 fosslight_dependency-3.9.3/src/fosslight_dependency/run_dependency_scanner.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)     6377 2022-03-11 05:44:14.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     1246 2022-03-11 05:44:15.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2022-03-11 05:44:14.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       91 2022-03-11 05:44:14.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (116)       91 2022-03-11 05:44:14.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)       21 2022-03-11 05:44:14.000000 fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/
+-rw-r--r--   0 runner    (1001) docker     (116)    11357 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/LICENSE
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/LICENSES/
+-rw-r--r--   0 runner    (1001) docker     (116)    11357 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/LICENSES/Apache-2.0.txt
+-rw-r--r--   0 runner    (1001) docker     (116)    95687 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/LICENSES/LicenseRef-3rd_party_licenses.txt
+-rw-r--r--   0 runner    (1001) docker     (116)     1082 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/LICENSES/MIT.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       78 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (116)     6377 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     5418 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (116)       91 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       92 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (116)     1517 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3181 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/_analyze_dependency.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2364 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/_help.py
+-rw-r--r--   0 runner    (1001) docker     (116)     6173 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/_package_manager.py
+-rw-r--r--   0 runner    (1001) docker     (116)      795 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/constant.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/
+-rw-r--r--   0 runner    (1001) docker     (116)     1929 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Android.py
+-rw-r--r--   0 runner    (1001) docker     (116)     5006 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Carthage.py
+-rw-r--r--   0 runner    (1001) docker     (116)     6221 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Cocoapods.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3767 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Go.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3166 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Gradle.py
+-rw-r--r--   0 runner    (1001) docker     (116)     8202 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Maven.py
+-rw-r--r--   0 runner    (1001) docker     (116)     5306 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Npm.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3018 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Pub.py
+-rw-r--r--   0 runner    (1001) docker     (116)    10184 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Pypi.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3406 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Swift.py
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (116)     8335 2022-04-11 08:49:16.000000 fosslight_dependency-3.9.4/src/fosslight_dependency/run_dependency_scanner.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)     6377 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     1246 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       91 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       91 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       21 2022-04-11 08:49:24.000000 fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/top_level.txt
```

### Comparing `fosslight_dependency-3.9.3/LICENSE` & `fosslight_dependency-3.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/LICENSES/Apache-2.0.txt` & `fosslight_dependency-3.9.4/LICENSES/Apache-2.0.txt`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/LICENSES/LicenseRef-3rd_party_licenses.txt` & `fosslight_dependency-3.9.4/LICENSES/LicenseRef-3rd_party_licenses.txt`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/LICENSES/MIT.txt` & `fosslight_dependency-3.9.4/LICENSES/MIT.txt`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/PKG-INFO` & `fosslight_dependency-3.9.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fosslight_dependency
-Version: 3.9.3
+Version: 3.9.4
 Summary: FOSSLight Dependency Scanner
 Home-page: https://github.com/fosslight/fosslight_dependency_scanner
 Author: LG Electronics
 License: Apache-2.0
 Download-URL: https://github.com/fosslight/fosslight_dependency_scanner
 Description: <!--
         Copyright (c) 2021 LG Electronics
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: fosslight_dependency Version: 3.9.3 Summary:
+Metadata-Version: 2.1 Name: fosslight_dependency Version: 3.9.4 Summary:
 FOSSLight Dependency Scanner Home-page: https://github.com/fosslight/
 fosslight_dependency_scanner Author: LG Electronics License: Apache-2.0
 Download-URL: https://github.com/fosslight/fosslight_dependency_scanner
 Description:  # FOSSLight Dependency Scanner [License] [Current_python_package
 version.] [https://img.shields.io/pypi/pyversions/fosslight_dependency] [!
 [REUSE status](https://api.reuse.software/badge/github.com/fosslight/
 fosslight_dependency_scanner)](https://api.reuse.software/info/github.com/
```

### Comparing `fosslight_dependency-3.9.3/README.md` & `fosslight_dependency-3.9.4/README.md`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/setup.py` & `fosslight_dependency-3.9.4/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 with open('requirements.txt', 'r', 'utf-8') as f:
     required = f.read().splitlines()
 
 
 if __name__ == "__main__":
     setup(
         name='fosslight_dependency',
-        version='3.9.3',
+        version='3.9.4',
         package_dir={"": "src"},
         packages=find_packages(where='src'),
         description='FOSSLight Dependency Scanner',
         long_description=reamdme,
         long_description_content_type='text/markdown',
         license='Apache-2.0',
         author='LG Electronics',
```

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/_analyze_dependency.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/_analyze_dependency.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/_help.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/_help.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/_package_manager.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/_package_manager.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/constant.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/constant.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Android.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Android.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Carthage.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Carthage.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Cocoapods.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Cocoapods.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Go.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Go.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Gradle.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Gradle.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Maven.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Maven.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Npm.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Npm.py`

 * *Files 14% similar despite different names*

```diff
@@ -59,15 +59,15 @@
             logger.error("Please check if the license-checker is installed.(sudo npm install -g license-checker)")
             return False
         else:
             self.append_input_package_list_file(self.input_file_name)
 
         os.remove(tmp_custom_json)
         if flag_tmp_node_modules:
-            shutil.rmtree(node_modules)
+            shutil.rmtree(node_modules, ignore_errors=True)
 
         return ret
 
     def make_custom_json(self, tmp_custom_json):
         with open(tmp_custom_json, 'w', encoding='utf8') as custom:
             custom.write(
                 "{\n\t\"name\": \"\",\n\t\"version\": \"\",\n\t\"licenses\": \"\",\n\t\"repository\": \
@@ -88,39 +88,58 @@
 
             if d['licenses']:
                 license_name = d['licenses']
             else:
                 license_name = ''
 
             oss_version = d['version']
+            package_path = d['path']
 
             if d['repository']:
                 dn_loc = d['repository']
             else:
                 dn_loc = f"{self.dn_url}{oss_init_name}/v/{oss_version}"
 
             homepage = self.dn_url + oss_init_name
 
             multi_license = check_multi_license(license_name)
-
+            manifest_file_path = os.path.join(package_path, const.SUPPORT_PACKAE.get(self.package_manager_name))
             if multi_license:
                 for l_idx in range(0, len(license_name)):
                     license_name = license_name[l_idx].replace(",", "")
-
+                    license_name = check_unknown_license(license_name, manifest_file_path)
                     sheet_list.append([const.SUPPORT_PACKAE.get(self.package_manager_name),
                                       oss_name, oss_version, license_name, dn_loc, homepage, '', '', ''])
             else:
                 license_name = license_name.replace(",", "")
-
+                license_name = check_unknown_license(license_name, manifest_file_path)
                 sheet_list.append([const.SUPPORT_PACKAE.get(self.package_manager_name),
                                   oss_name, oss_version, license_name, dn_loc, homepage, '', '', ''])
 
         return sheet_list
 
 
 def check_multi_license(license_name):
     if isinstance(license_name, list):
         multi_license = True
     else:
         multi_license = False
 
     return multi_license
+
+
+def check_unknown_license(license_name, manifest_file_path):
+    if license_name.endswith('*'):
+        license_name = license_name[:-1]
+
+    if license_name == 'UNKNOWN':
+        try:
+            with open(manifest_file_path, 'r') as f:
+                json_f = json.load(f)
+                for key in json_f.keys():
+                    if key == 'license':
+                        license_name = json_f[key]
+                        break
+        except Exception as e:
+            logging.warning(f"Cannot check unknown license: {e}")
+
+    return license_name
```

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Pub.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Pub.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Pypi.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Pypi.py`

 * *Files 1% similar despite different names*

```diff
@@ -36,16 +36,15 @@
     def __del__(self):
         if os.path.isfile(self.tmp_file_name):
             os.remove(self.tmp_file_name)
 
         if os.path.isfile(self.tmp_pip_license_info_file_name):
             os.remove(self.tmp_pip_license_info_file_name)
 
-        if os.path.isdir(self.venv_tmp_dir):
-            shutil.rmtree(self.venv_tmp_dir)
+        shutil.rmtree(self.venv_tmp_dir, ignore_errors=True)
 
     def set_pip_activate_cmd(self, pip_activate_cmd):
         self.pip_activate_cmd = pip_activate_cmd
 
     def set_pip_deactivate_cmd(self, pip_deactivate_cmd):
         self.pip_deactivate_cmd = pip_deactivate_cmd
```

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/package_manager/Swift.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/package_manager/Swift.py`

 * *Files 7% similar despite different names*

```diff
@@ -36,34 +36,51 @@
                                                                 self.input_file_name)
                     if input_file_name_in_xcodeproj != self.input_file_name:
                         if os.path.isfile(input_file_name_in_xcodeproj):
                             self.input_file_name = input_file_name_in_xcodeproj
                             logger.info(f"It uses the manifest file: {self.input_file_name}")
 
     def parse_oss_information(self, f_name):
+        sheet_list = []
+        json_ver = 1
+
         with open(f_name, 'r', encoding='utf8') as json_file:
             json_raw = json.load(json_file)
-            json_data = json_raw["object"]["pins"]
+            json_ver = json_raw['version']
 
-        sheet_list = []
+            if json_ver == 1:
+                json_data = json_raw["object"]["pins"]
+            elif json_ver == 2:
+                json_data = json_raw["pins"]
+            else:
+                logger.error(f'Not supported Package.resolved version {json_ver}')
+                return sheet_list
 
         g = connect_github(self.github_token)
 
         for key in json_data:
-            oss_origin_name = key['package']
+            if json_ver == 1:
+                oss_origin_name = key['package']
+                homepage = key['repositoryURL']
+            elif json_ver == 2:
+                oss_origin_name = key['identity']
+                homepage = key['location']
+
+            if homepage.endswith('.git'):
+                homepage = homepage[:-4]
+
             oss_name = f"{self.package_manager_name}:{oss_origin_name}"
 
             revision = key['state']['revision']
             version = key['state']['version']
             if version is None:
                 oss_version = revision
             else:
                 oss_version = version
 
-            homepage = key['repositoryURL']
             dn_loc = homepage
             license_name = ''
 
             github_repo = "/".join(homepage.split('/')[-2:])
             license_name = get_github_license(g, github_repo, self.platform, self.license_scanner_bin)
 
             sheet_list.append([const.SUPPORT_PACKAE.get(self.package_manager_name),
```

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency/run_dependency_scanner.py` & `fosslight_dependency-3.9.4/src/fosslight_dependency/run_dependency_scanner.py`

 * *Files identical despite different names*

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/PKG-INFO` & `fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fosslight-dependency
-Version: 3.9.3
+Version: 3.9.4
 Summary: FOSSLight Dependency Scanner
 Home-page: https://github.com/fosslight/fosslight_dependency_scanner
 Author: LG Electronics
 License: Apache-2.0
 Download-URL: https://github.com/fosslight/fosslight_dependency_scanner
 Description: <!--
         Copyright (c) 2021 LG Electronics
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: fosslight-dependency Version: 3.9.3 Summary:
+Metadata-Version: 2.1 Name: fosslight-dependency Version: 3.9.4 Summary:
 FOSSLight Dependency Scanner Home-page: https://github.com/fosslight/
 fosslight_dependency_scanner Author: LG Electronics License: Apache-2.0
 Download-URL: https://github.com/fosslight/fosslight_dependency_scanner
 Description:  # FOSSLight Dependency Scanner [License] [Current_python_package
 version.] [https://img.shields.io/pypi/pyversions/fosslight_dependency] [!
 [REUSE status](https://api.reuse.software/badge/github.com/fosslight/
 fosslight_dependency_scanner)](https://api.reuse.software/info/github.com/
```

### Comparing `fosslight_dependency-3.9.3/src/fosslight_dependency.egg-info/SOURCES.txt` & `fosslight_dependency-3.9.4/src/fosslight_dependency.egg-info/SOURCES.txt`

 * *Files identical despite different names*

