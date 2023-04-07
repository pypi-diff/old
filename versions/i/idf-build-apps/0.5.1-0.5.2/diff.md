# Comparing `tmp/idf-build-apps-0.5.1.tar.gz` & `tmp/idf-build-apps-0.5.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "idf-build-apps-0.5.1.tar", last modified: Thu Apr  6 01:23:12 2023, max compression
+gzip compressed data, was "idf-build-apps-0.5.2.tar", last modified: Fri Apr  7 02:55:57 2023, max compression
```

## Comparing `idf-build-apps-0.5.1.tar` & `idf-build-apps-0.5.2.tar`

### file list

```diff
@@ -1,49 +1,49 @@
--rw-r--r--   0        0        0      351 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.editorconfig
--rw-r--r--   0        0        0      123 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.git-blame-ignore-revs
--rw-r--r--   0        0        0       25 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.gitattributes
--rw-r--r--   0        0        0      253 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/check-pre-commit.yml
--rw-r--r--   0        0        0      675 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/issue_comment.yml
--rw-r--r--   0        0        0      620 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/new_issues.yml
--rw-r--r--   0        0        0      796 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/new_prs.yml
--rw-r--r--   0        0        0      438 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/publish-pypi.yml
--rw-r--r--   0        0        0      521 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/test-build-docs.yml
--rw-r--r--   0        0        0     3707 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.github/workflows/test-build-idf-apps.yml
--rw-r--r--   0        0        0     3076 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.gitignore
--rw-r--r--   0        0        0     1077 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.pre-commit-config.yaml
--rw-r--r--   0        0        0      383 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/.readthedocs.yml
--rw-r--r--   0        0        0     2764 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/CHANGELOG.md
--rw-r--r--   0        0        0     1834 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/CONTRIBUTING.md
--rw-r--r--   0        0        0    11358 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/LICENSE
--rw-r--r--   0        0        0     3843 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/README.md
--rw-r--r--   0        0        0       33 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/CHANGELOG.md
--rw-r--r--   0        0        0       36 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/CONTRIBUTING.md
--rw-r--r--   0        0        0      634 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/Makefile
--rw-r--r--   0        0        0     6947 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/_static/espressif-logo.svg
--rw-r--r--   0        0        0      942 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/_static/theme_overrides.css
--rw-r--r--   0        0        0      119 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/_templates/layout.html
--rw-r--r--   0        0        0      490 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/api.rst
--rw-r--r--   0        0        0     1449 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/conf.py
--rw-r--r--   0        0        0    10368 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/find-build.md
--rw-r--r--   0        0        0      459 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/index.rst
--rw-r--r--   0        0        0     3651 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/docs/manifest.md
--rw-r--r--   0        0        0      483 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/idf_build_apps/__init__.py
--rw-r--r--   0        0        0      182 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/idf_build_apps/__main__.py
--rw-r--r--   0        0        0    21624 2023-04-06 01:23:06.703380 idf-build-apps-0.5.1/idf_build_apps/app.py
--rw-r--r--   0        0        0     2187 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/constants.py
--rw-r--r--   0        0        0     6026 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/finder.py
--rw-r--r--   0        0        0     1359 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/log.py
--rw-r--r--   0        0        0    26258 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/main.py
--rw-r--r--   0        0        0      133 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/manifest/__init__.py
--rw-r--r--   0        0        0     5547 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/manifest/if_parser.py
--rw-r--r--   0        0        0     5322 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/manifest/manifest.py
--rw-r--r--   0        0        0     3423 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/manifest/soc_header.py
--rw-r--r--   0        0        0     7459 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/idf_build_apps/utils.py
--rw-r--r--   0        0        0      101 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/license_header.txt
--rw-r--r--   0        0        0     1837 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/pyproject.toml
--rw-r--r--   0        0        0     1221 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/tests/conftest.py
--rw-r--r--   0        0        0     2181 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/tests/test_build.py
--rw-r--r--   0        0        0     7848 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/tests/test_finder.py
--rw-r--r--   0        0        0      995 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/tests/test_manifest.py
--rw-r--r--   0        0        0     2394 2023-04-06 01:23:06.707380 idf-build-apps-0.5.1/tests/test_utils.py
--rw-r--r--   0        0        0     1037 1970-01-01 00:00:00.000000 idf-build-apps-0.5.1/setup.py
--rw-r--r--   0        0        0     5450 1970-01-01 00:00:00.000000 idf-build-apps-0.5.1/PKG-INFO
+-rw-r--r--   0        0        0      351 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.editorconfig
+-rw-r--r--   0        0        0      123 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.git-blame-ignore-revs
+-rw-r--r--   0        0        0       25 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.gitattributes
+-rw-r--r--   0        0        0      253 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.github/workflows/check-pre-commit.yml
+-rw-r--r--   0        0        0      675 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.github/workflows/issue_comment.yml
+-rw-r--r--   0        0        0      620 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.github/workflows/new_issues.yml
+-rw-r--r--   0        0        0      796 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.github/workflows/new_prs.yml
+-rw-r--r--   0        0        0      438 2023-04-07 02:55:53.554697 idf-build-apps-0.5.2/.github/workflows/publish-pypi.yml
+-rw-r--r--   0        0        0      521 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/.github/workflows/test-build-docs.yml
+-rw-r--r--   0        0        0     3707 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/.github/workflows/test-build-idf-apps.yml
+-rw-r--r--   0        0        0     3076 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/.gitignore
+-rw-r--r--   0        0        0     1077 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      383 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/.readthedocs.yml
+-rw-r--r--   0        0        0     2923 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/CHANGELOG.md
+-rw-r--r--   0        0        0     1834 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/CONTRIBUTING.md
+-rw-r--r--   0        0        0    11358 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/LICENSE
+-rw-r--r--   0        0        0     3843 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/README.md
+-rw-r--r--   0        0        0       33 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/CHANGELOG.md
+-rw-r--r--   0        0        0       36 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/CONTRIBUTING.md
+-rw-r--r--   0        0        0      634 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/Makefile
+-rw-r--r--   0        0        0     6947 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/_static/espressif-logo.svg
+-rw-r--r--   0        0        0      942 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/_static/theme_overrides.css
+-rw-r--r--   0        0        0      119 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/_templates/layout.html
+-rw-r--r--   0        0        0      490 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/api.rst
+-rw-r--r--   0        0        0     1449 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/conf.py
+-rw-r--r--   0        0        0    10368 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/find-build.md
+-rw-r--r--   0        0        0      459 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/index.rst
+-rw-r--r--   0        0        0     3651 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/docs/manifest.md
+-rw-r--r--   0        0        0      483 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/__init__.py
+-rw-r--r--   0        0        0      182 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/__main__.py
+-rw-r--r--   0        0        0    21914 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/app.py
+-rw-r--r--   0        0        0     2187 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/constants.py
+-rw-r--r--   0        0        0     6026 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/finder.py
+-rw-r--r--   0        0        0     1359 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/log.py
+-rw-r--r--   0        0        0    26258 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/main.py
+-rw-r--r--   0        0        0      133 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/manifest/__init__.py
+-rw-r--r--   0        0        0     5547 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/manifest/if_parser.py
+-rw-r--r--   0        0        0     5322 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/manifest/manifest.py
+-rw-r--r--   0        0        0     3423 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/manifest/soc_header.py
+-rw-r--r--   0        0        0     7459 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/idf_build_apps/utils.py
+-rw-r--r--   0        0        0      101 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/license_header.txt
+-rw-r--r--   0        0        0     1837 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/pyproject.toml
+-rw-r--r--   0        0        0     1221 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/tests/conftest.py
+-rw-r--r--   0        0        0     2181 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/tests/test_build.py
+-rw-r--r--   0        0        0     7948 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/tests/test_finder.py
+-rw-r--r--   0        0        0      995 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/tests/test_manifest.py
+-rw-r--r--   0        0        0     2394 2023-04-07 02:55:53.558697 idf-build-apps-0.5.2/tests/test_utils.py
+-rw-r--r--   0        0        0     1037 1970-01-01 00:00:00.000000 idf-build-apps-0.5.2/setup.py
+-rw-r--r--   0        0        0     5450 1970-01-01 00:00:00.000000 idf-build-apps-0.5.2/PKG-INFO
```

### Comparing `idf-build-apps-0.5.1/.github/workflows/issue_comment.yml` & `idf-build-apps-0.5.2/.github/workflows/issue_comment.yml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.github/workflows/new_issues.yml` & `idf-build-apps-0.5.2/.github/workflows/new_issues.yml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.github/workflows/new_prs.yml` & `idf-build-apps-0.5.2/.github/workflows/new_prs.yml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.github/workflows/test-build-docs.yml` & `idf-build-apps-0.5.2/.github/workflows/test-build-docs.yml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.github/workflows/test-build-idf-apps.yml` & `idf-build-apps-0.5.2/.github/workflows/test-build-idf-apps.yml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.gitignore` & `idf-build-apps-0.5.2/.gitignore`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/.pre-commit-config.yaml` & `idf-build-apps-0.5.2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/CHANGELOG.md` & `idf-build-apps-0.5.2/CHANGELOG.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,18 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
+## [0.5.2] (2023-04-07)
+
+### Fixed
+
+- Remove empty expanded sdkconfig files folder after build
+- Split up expanded sdkconfig files folder for different build
+
 ## [0.5.1] (2023-04-06)
 
 ### Fixed
 
 - Build with expanded sdkconfig file would respect the target-specific one under the original path
 
 ## [0.5.0] (2023-03-29)
```

### Comparing `idf-build-apps-0.5.1/CONTRIBUTING.md` & `idf-build-apps-0.5.2/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/LICENSE` & `idf-build-apps-0.5.2/LICENSE`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/README.md` & `idf-build-apps-0.5.2/README.md`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/Makefile` & `idf-build-apps-0.5.2/docs/Makefile`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/_static/espressif-logo.svg` & `idf-build-apps-0.5.2/docs/_static/espressif-logo.svg`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/_static/theme_overrides.css` & `idf-build-apps-0.5.2/docs/_static/theme_overrides.css`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/conf.py` & `idf-build-apps-0.5.2/docs/conf.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/find-build.md` & `idf-build-apps-0.5.2/docs/find-build.md`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/docs/manifest.md` & `idf-build-apps-0.5.2/docs/manifest.md`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/app.py` & `idf-build-apps-0.5.2/idf_build_apps/app.py`

 * *Files 1% similar despite different names*

```diff
@@ -245,27 +245,27 @@
     def _process_sdkconfig_files(self):
         """
         Expand environment variables in default sdkconfig files and remove some CI
         related settings.
         """
         res = []
 
+        expanded_dir = os.path.join(self.work_dir, 'expanded_sdkconfig_files', os.path.basename(self.build_dir))
+        if not os.path.isdir(expanded_dir):
+            os.makedirs(expanded_dir)
+
         for f in self._sdkconfig_defaults + ([self.sdkconfig_path] if self.sdkconfig_path else []):
             if not os.path.isabs(f):
                 f = os.path.join(self.work_dir, f)
 
             if not os.path.isfile(f):
                 LOGGER.debug('=> sdkconfig file %s not exists, skipping...', f)
                 continue
 
-            expanded_dir = os.path.join(self.work_dir, 'expanded_sdkconfig_files')
             expanded_fp = os.path.join(expanded_dir, os.path.basename(f))
-            if not os.path.isdir(expanded_dir):
-                os.makedirs(expanded_dir)
-
             with open(f) as fr:
                 with open(expanded_fp, 'w') as fw:
                     for line in fr:
                         line = os.path.expandvars(line)
 
                         m = self.SDKCONFIG_LINE_REGEX.match(line)
                         key = m.group(1) if m else None
@@ -299,14 +299,25 @@
                             os.path.basename(f) + '.{}'.format(self.target)
                         ):
                             LOGGER.debug(
                                 '=> Copy target-specific sdkconfig file %s to %s', target_specific_file, expanded_dir
                             )
                             shutil.copy(target_specific_file, expanded_dir)
 
+        # remove if expanded folder is empty
+        try:
+            os.rmdir(expanded_dir)
+        except OSError:
+            pass
+
+        try:
+            os.rmdir(os.path.join(self.work_dir, 'expanded_sdkconfig_files'))
+        except OSError:
+            pass
+
         self._sdkconfig_files = res
 
     @property
     def sdkconfig_files_defined_idf_target(self):  # type: () -> str | None
         return self._sdkconfig_files_defined_target
 
     @property
```

### Comparing `idf-build-apps-0.5.1/idf_build_apps/constants.py` & `idf-build-apps-0.5.2/idf_build_apps/constants.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/finder.py` & `idf-build-apps-0.5.2/idf_build_apps/finder.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/log.py` & `idf-build-apps-0.5.2/idf_build_apps/log.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/main.py` & `idf-build-apps-0.5.2/idf_build_apps/main.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/manifest/if_parser.py` & `idf-build-apps-0.5.2/idf_build_apps/manifest/if_parser.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/manifest/manifest.py` & `idf-build-apps-0.5.2/idf_build_apps/manifest/manifest.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/manifest/soc_header.py` & `idf-build-apps-0.5.2/idf_build_apps/manifest/soc_header.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/idf_build_apps/utils.py` & `idf-build-apps-0.5.2/idf_build_apps/utils.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/pyproject.toml` & `idf-build-apps-0.5.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/tests/conftest.py` & `idf-build-apps-0.5.2/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/tests/test_build.py` & `idf-build-apps-0.5.2/tests/test_build.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/tests/test_finder.py` & `idf-build-apps-0.5.2/tests/test_finder.py`

 * *Files 2% similar despite different names*

```diff
@@ -212,18 +212,22 @@
         (tmp_path / 'test1' / 'sdkconfig.ci.foo').write_text('CONFIG_IDF_TARGET=${TEST_TARGET}', encoding='utf8')
         (tmp_path / 'test1' / 'sdkconfig.ci.bar').write_text('CONFIG_IDF_TARGET=esp32s2', encoding='utf8')
         (tmp_path / 'test1' / 'sdkconfig.ci.baz').write_text('CONFIG_IDF_TARGET=esp32s3', encoding='utf8')
 
         monkeypatch.setenv('TEST_TARGET', 'esp32')
         apps = find_apps(str(tmp_path), 'esp32', recursive=True, config_rules_str='sdkconfig.ci.*=')
         assert len(apps) == 1
-        assert Path(apps[0].sdkconfig_files[0]).parts[-2:] == ('expanded_sdkconfig_files', 'sdkconfig.ci.foo')
+        assert Path(apps[0].sdkconfig_files[0]).parts[-3:] == ('expanded_sdkconfig_files', 'build', 'sdkconfig.ci.foo')
 
         # test relative paths
         os.chdir(str(tmp_path))
-        apps = find_apps('test1', 'esp32', recursive=True, config_rules_str='sdkconfig.ci.*=')
+        apps = find_apps('test1', 'esp32', recursive=True, config_rules_str='sdkconfig.ci.*=', build_dir='build_@t_@w')
         assert len(apps) == 1
-        assert Path(apps[0].sdkconfig_files[0]).parts[-2:] == ('expanded_sdkconfig_files', 'sdkconfig.ci.foo')
+        assert Path(apps[0].sdkconfig_files[0]).parts[-3:] == (
+            'expanded_sdkconfig_files',
+            'build_esp32_foo',
+            'sdkconfig.ci.foo',
+        )
 
         monkeypatch.setenv('TEST_TARGET', 'esp32s2')
         apps = find_apps('test1', 'esp32', recursive=True, config_rules_str='sdkconfig.ci.*=')
         assert len(apps) == 0
```

### Comparing `idf-build-apps-0.5.1/tests/test_manifest.py` & `idf-build-apps-0.5.2/tests/test_manifest.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/tests/test_utils.py` & `idf-build-apps-0.5.2/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `idf-build-apps-0.5.1/setup.py` & `idf-build-apps-0.5.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -21,15 +21,15 @@
          'sphinxcontrib-mermaid'],
  'test': ['pytest', 'pytest-cov']}
 
 entry_points = \
 {'console_scripts': ['idf-build-apps = idf_build_apps:main.main']}
 
 setup(name='idf-build-apps',
-      version='0.5.1',
+      version='0.5.2',
       description='Tools for building ESP-IDF related apps.',
       author=None,
       author_email='Fu Hanxi <fuhanxi@espressif.com>',
       url=None,
       packages=packages,
       package_data=package_data,
       install_requires=install_requires,
```

### Comparing `idf-build-apps-0.5.1/PKG-INFO` & `idf-build-apps-0.5.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: idf-build-apps
-Version: 0.5.1
+Version: 0.5.2
 Summary: Tools for building ESP-IDF related apps.
 Author-email: Fu Hanxi <fuhanxi@espressif.com>
 Requires-Python: >=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
 Description-Content-Type: text/markdown
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 2.7
```

