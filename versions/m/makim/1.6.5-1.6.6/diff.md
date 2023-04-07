# Comparing `tmp/makim-1.6.5.tar.gz` & `tmp/makim-1.6.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "makim-1.6.5.tar", max compression
+gzip compressed data, was "makim-1.6.6.tar", max compression
```

## Comparing `makim-1.6.5.tar` & `makim-1.6.6.tar`

### file list

```diff
@@ -1,24 +1,24 @@
--rw-r--r--   0        0        0       88 2023-04-05 05:21:09.112468 makim-1.6.5/.github/FUNDING.yml
--rw-r--r--   0        0        0      316 2023-04-05 05:21:09.112468 makim-1.6.5/.github/ISSUE_TEMPLATE.md
--rw-r--r--   0        0        0     1395 2023-04-05 05:21:09.112468 makim-1.6.5/.github/PULL_REQUEST_TEMPLATE.md
--rw-r--r--   0        0        0     3813 2023-04-05 05:21:09.112468 makim-1.6.5/.github/workflows/main.yaml
--rw-r--r--   0        0        0     1451 2023-04-05 05:21:09.112468 makim-1.6.5/.github/workflows/release.yaml
--rw-r--r--   0        0        0     1799 2023-04-05 05:21:09.112468 makim-1.6.5/.gitignore
--rw-r--r--   0        0        0     6482 2023-04-05 05:21:09.112468 makim-1.6.5/.makim.yaml
--rw-r--r--   0        0        0     1095 2023-04-05 05:21:09.112468 makim-1.6.5/.pre-commit-config.yaml
--rw-r--r--   0        0        0     1854 2023-04-05 05:21:09.112468 makim-1.6.5/.releaserc.json
--rw-r--r--   0        0        0     1514 2023-04-05 05:21:09.112468 makim-1.6.5/LICENSE
--rw-r--r--   0        0        0     3409 2023-04-05 05:21:09.112468 makim-1.6.5/README.md
--rw-r--r--   0        0        0      159 2023-04-05 05:21:09.112468 makim-1.6.5/conda/dev.yaml
--rw-r--r--   0        0        0     4312 2023-04-05 05:23:35.651651 makim-1.6.5/docs/changelog.md
--rw-r--r--   0        0        0     5253 2023-04-05 05:21:09.112468 makim-1.6.5/docs/contributing.md
--rw-r--r--   0        0        0    72342 2023-04-05 05:21:09.112468 makim-1.6.5/docs/images/favicon.ico
--rw-r--r--   0        0        0    20402 2023-04-05 05:21:09.112468 makim-1.6.5/docs/images/logo.png
--rw-r--r--   0        0        0     1083 2023-04-05 05:21:09.112468 makim-1.6.5/docs/installation.md
--rw-r--r--   0        0        0     3832 2023-04-05 05:21:09.112468 makim-1.6.5/docs/mkdocs.yaml
--rw-r--r--   0        0        0      194 2023-04-05 05:23:35.639651 makim-1.6.5/makim/__init__.py
--rw-r--r--   0        0        0     4746 2023-04-05 05:21:09.116468 makim-1.6.5/makim/__main__.py
--rw-r--r--   0        0        0    11359 2023-04-05 05:21:09.116468 makim-1.6.5/makim/makim.py
--rw-r--r--   0        0        0   153994 2023-04-05 05:21:09.116468 makim-1.6.5/poetry.lock
--rw-r--r--   0        0        0     1660 2023-04-05 05:23:35.639651 makim-1.6.5/pyproject.toml
--rw-r--r--   0        0        0     4245 1970-01-01 00:00:00.000000 makim-1.6.5/PKG-INFO
+-rw-r--r--   0        0        0       88 2023-04-07 04:18:25.479232 makim-1.6.6/.github/FUNDING.yml
+-rw-r--r--   0        0        0      316 2023-04-07 04:18:25.479232 makim-1.6.6/.github/ISSUE_TEMPLATE.md
+-rw-r--r--   0        0        0     1395 2023-04-07 04:18:25.479232 makim-1.6.6/.github/PULL_REQUEST_TEMPLATE.md
+-rw-r--r--   0        0        0     3813 2023-04-07 04:18:25.479232 makim-1.6.6/.github/workflows/main.yaml
+-rw-r--r--   0        0        0     1451 2023-04-07 04:18:25.479232 makim-1.6.6/.github/workflows/release.yaml
+-rw-r--r--   0        0        0     1799 2023-04-07 04:18:25.479232 makim-1.6.6/.gitignore
+-rw-r--r--   0        0        0     6482 2023-04-07 04:18:25.479232 makim-1.6.6/.makim.yaml
+-rw-r--r--   0        0        0     1095 2023-04-07 04:18:25.479232 makim-1.6.6/.pre-commit-config.yaml
+-rw-r--r--   0        0        0     1854 2023-04-07 04:18:25.479232 makim-1.6.6/.releaserc.json
+-rw-r--r--   0        0        0     1514 2023-04-07 04:18:25.479232 makim-1.6.6/LICENSE
+-rw-r--r--   0        0        0     3409 2023-04-07 04:18:25.479232 makim-1.6.6/README.md
+-rw-r--r--   0        0        0      159 2023-04-07 04:18:25.479232 makim-1.6.6/conda/dev.yaml
+-rw-r--r--   0        0        0     4641 2023-04-07 04:21:14.277203 makim-1.6.6/docs/changelog.md
+-rw-r--r--   0        0        0     5253 2023-04-07 04:18:25.479232 makim-1.6.6/docs/contributing.md
+-rw-r--r--   0        0        0    72342 2023-04-07 04:18:25.479232 makim-1.6.6/docs/images/favicon.ico
+-rw-r--r--   0        0        0    20402 2023-04-07 04:18:25.479232 makim-1.6.6/docs/images/logo.png
+-rw-r--r--   0        0        0     1083 2023-04-07 04:18:25.479232 makim-1.6.6/docs/installation.md
+-rw-r--r--   0        0        0     3832 2023-04-07 04:18:25.479232 makim-1.6.6/docs/mkdocs.yaml
+-rw-r--r--   0        0        0      194 2023-04-07 04:21:14.265203 makim-1.6.6/makim/__init__.py
+-rw-r--r--   0        0        0     4746 2023-04-07 04:18:25.479232 makim-1.6.6/makim/__main__.py
+-rw-r--r--   0        0        0    11380 2023-04-07 04:18:25.479232 makim-1.6.6/makim/makim.py
+-rw-r--r--   0        0        0   153994 2023-04-07 04:18:25.479232 makim-1.6.6/poetry.lock
+-rw-r--r--   0        0        0     1660 2023-04-07 04:21:14.265203 makim-1.6.6/pyproject.toml
+-rw-r--r--   0        0        0     4245 1970-01-01 00:00:00.000000 makim-1.6.6/PKG-INFO
```

### Comparing `makim-1.6.5/.github/PULL_REQUEST_TEMPLATE.md` & `makim-1.6.6/.github/PULL_REQUEST_TEMPLATE.md`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.github/workflows/main.yaml` & `makim-1.6.6/.github/workflows/main.yaml`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.github/workflows/release.yaml` & `makim-1.6.6/.github/workflows/release.yaml`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.gitignore` & `makim-1.6.6/.gitignore`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.makim.yaml` & `makim-1.6.6/.makim.yaml`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.pre-commit-config.yaml` & `makim-1.6.6/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/.releaserc.json` & `makim-1.6.6/.releaserc.json`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/LICENSE` & `makim-1.6.6/LICENSE`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/README.md` & `makim-1.6.6/README.md`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/docs/changelog.md` & `makim-1.6.6/docs/changelog.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,17 @@
 # Release Notes
 ---
 
+## [1.6.6](https://github.com/osl-incubator/makim/compare/1.6.5...1.6.6) (2023-04-07)
+
+
+### Bug Fixes
+
+* Fix both --version usage and the required property for arguments ([#35](https://github.com/osl-incubator/makim/issues/35)) ([3bc20e1](https://github.com/osl-incubator/makim/commit/3bc20e1941774ad07ca34ecfe511e4a54f766a7b))
+
 ## [1.6.5](https://github.com/osl-incubator/makim/compare/1.6.4...1.6.5) (2023-04-05)
 
 
 ### Bug Fixes
 
 * Fix nested commands ([#34](https://github.com/osl-incubator/makim/issues/34)) ([790d2ba](https://github.com/osl-incubator/makim/commit/790d2bad746b2462bb8a6795b48eb913502a775e))
```

### Comparing `makim-1.6.5/docs/contributing.md` & `makim-1.6.6/docs/contributing.md`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/docs/images/favicon.ico` & `makim-1.6.6/docs/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/docs/images/logo.png` & `makim-1.6.6/docs/images/logo.png`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/docs/installation.md` & `makim-1.6.6/docs/installation.md`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/docs/mkdocs.yaml` & `makim-1.6.6/docs/mkdocs.yaml`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/makim/__main__.py` & `makim-1.6.6/makim/__main__.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -171,23 +171,23 @@
 
 
 def app():
     makim_args = extract_makim_args()
     args_parser = _get_args()
     args = args_parser.parse_args()
 
+    if args.version:
+        return show_version()
+
     if not args.target or args.help:
         return args_parser.print_help()
 
     if args.help:
         return args_parser.print_help()
 
-    if args.version:
-        return show_version()
-
     makim.load(args.makim_file)
     makim_args.update(dict(args._get_kwargs()))
     return makim.run(makim_args)
 
 
 if __name__ == '__main__':
     app()
```

### Comparing `makim-1.6.5/makim/makim.py` & `makim-1.6.6/makim/makim.py`

 * *Files 1% similar despite different names*

```diff
@@ -246,15 +246,15 @@
             action = v.get('action', '').replace('-', '_')
             is_store_true = action == 'store_true'
             default = v.get('default', False if is_store_true else None)
 
             args_input[k_clean] = default
 
             input_flag = f'--{k}'
-            if input_flag in args:
+            if input_flag in args and args[input_flag]:
                 if action == 'store_true':
                     args_input[k_clean] = (
                         True if args[input_flag] is None else args[input_flag]
                     )
                     continue
 
                 args_input[k_clean] = (
```

### Comparing `makim-1.6.5/poetry.lock` & `makim-1.6.6/poetry.lock`

 * *Files identical despite different names*

### Comparing `makim-1.6.5/pyproject.toml` & `makim-1.6.6/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "makim"
-version = "1.6.5"  # semantic-release
+version = "1.6.6"  # semantic-release
 description = "Simplify the usage of containers"
 authors = ["Ivan Ogasawara <ivan.ogasawara@gmail.com>"]
 license = "BSD 3 Clause"
 repository = "https://github.com/osl-incubator/makim"
 homepage = "https://github.com/osl-incubator/makim"
 readme = "README.md"
 include = [
```

### Comparing `makim-1.6.5/PKG-INFO` & `makim-1.6.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: makim
-Version: 1.6.5
+Version: 1.6.6
 Summary: Simplify the usage of containers
 Home-page: https://github.com/osl-incubator/makim
 License: BSD 3 Clause
 Author: Ivan Ogasawara
 Author-email: ivan.ogasawara@gmail.com
 Requires-Python: >=3.8.1,<4.0.0
 Classifier: License :: Other/Proprietary License
```

