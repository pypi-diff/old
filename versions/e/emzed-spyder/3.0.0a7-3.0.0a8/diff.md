# Comparing `tmp/emzed-spyder-3.0.0a7.tar.gz` & `tmp/emzed-spyder-3.0.0a8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "emzed-spyder-3.0.0a7.tar", last modified: Wed Apr  5 12:46:52 2023, max compression
+gzip compressed data, was "emzed-spyder-3.0.0a8.tar", last modified: Thu Apr  6 21:20:25 2023, max compression
```

## Comparing `emzed-spyder-3.0.0a7.tar` & `emzed-spyder-3.0.0a8.tar`

### file list

```diff
@@ -1,51 +1,51 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.415546 emzed-spyder-3.0.0a7/
--rw-rw-rw-   0 root         (0) root         (0)      267 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      444 2023-04-05 12:46:52.414546 emzed-spyder-3.0.0a7/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)       96 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/README.md
--rw-rw-rw-   0 root         (0) root         (0)     2026 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/requirements.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-05 12:46:52.415546 emzed-spyder-3.0.0a7/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1465 2023-04-05 08:46:33.000000 emzed-spyder-3.0.0a7/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.407546 emzed-spyder-3.0.0a7/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.410546 emzed-spyder-3.0.0a7/src/emzed_spyder/
--rw-rw-rw-   0 root         (0) root         (0)      279 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.411546 emzed-spyder-3.0.0a7/src/emzed_spyder/assets/
--rw-rw-rw-   0 root         (0) root         (0)   191029 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/assets/splash.png
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.411546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed3_examples/
--rw-rw-rw-   0 root         (0) root         (0)      106 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed3_examples/README.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.412546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/
--rw-rw-rw-   0 root         (0) root         (0)       57 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/cookiecutter.json
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.413546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/
--rw-rw-rw-   0 root         (0) root         (0)    33038 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/LICENSE.txt
--rw-rw-rw-   0 root         (0) root         (0)       85 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/MANIFEST.in
--rw-rw-rw-   0 root         (0) root         (0)       34 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/requirements_dev.txt
--rw-rw-rw-   0 root         (0) root         (0)     2987 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/setup.pytemplate
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.407546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.413546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/
--rw-rw-rw-   0 root         (0) root         (0)      283 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/__init__.pytemplate
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.413546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/data/
--rw-rw-rw-   0 root         (0) root         (0)      249 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/data/readme.txt
--rw-rw-rw-   0 root         (0) root         (0)      348 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/example_module.pytemplate
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.413546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tests/
--rw-rw-rw-   0 root         (0) root         (0)      320 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tests/test_{{cookiecutter.pkg_name}}.pytemplate
--rw-rw-rw-   0 root         (0) root         (0)      249 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tox.ini
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.414546 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_spyder_kernels/
--rw-rw-rw-   0 root         (0) root         (0)     2184 2023-04-05 08:53:49.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_spyder_kernels/emzed_spyder_kernels.py
--rw-rw-rw-   0 root         (0) root         (0)      252 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_spyder_kernels/setup.py
--rw-rw-rw-   0 root         (0) root         (0)     1683 2023-04-05 08:46:33.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/patch_all.py
--rw-rw-rw-   0 root         (0) root         (0)     5079 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/patch_config.py
--rw-rw-rw-   0 root         (0) root         (0)     5022 2023-04-05 08:53:49.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/patch_gui.py
--rw-rw-rw-   0 root         (0) root         (0)     7956 2023-04-05 08:53:49.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/patch_remote_kernel_startup.py
--rw-rw-rw-   0 root         (0) root         (0)    16235 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/remote_interpreter_startup.py
--rw-rw-rw-   0 root         (0) root         (0)      234 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/start.py
--rw-rw-rw-   0 root         (0) root         (0)     9182 2023-04-05 12:10:33.000000 emzed-spyder-3.0.0a7/src/emzed_spyder/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.411546 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/
--rw-r--r--   0 root         (0) root         (0)      444 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1836 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      117 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)     2026 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 12:46:52.000000 emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 12:46:52.414546 emzed-spyder-3.0.0a7/tests/
--rw-rw-rw-   0 root         (0) root         (0)     1536 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/tests/test_bootstrap.py
--rw-rw-rw-   0 root         (0) root         (0)      173 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a7/tests/test_import.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.696717 emzed-spyder-3.0.0a8/
+-rw-rw-rw-   0 root         (0) root         (0)      267 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      444 2023-04-06 21:20:25.696717 emzed-spyder-3.0.0a8/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)       96 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     2026 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/requirements.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 21:20:25.696717 emzed-spyder-3.0.0a8/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     1465 2023-04-06 21:03:58.000000 emzed-spyder-3.0.0a8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.690717 emzed-spyder-3.0.0a8/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.692717 emzed-spyder-3.0.0a8/src/emzed_spyder/
+-rw-rw-rw-   0 root         (0) root         (0)      279 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.693717 emzed-spyder-3.0.0a8/src/emzed_spyder/assets/
+-rw-rw-rw-   0 root         (0) root         (0)   191029 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/assets/splash.png
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.694717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed3_examples/
+-rw-rw-rw-   0 root         (0) root         (0)      106 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed3_examples/README.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.694717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/
+-rw-rw-rw-   0 root         (0) root         (0)       57 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/cookiecutter.json
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.695717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/
+-rw-rw-rw-   0 root         (0) root         (0)    33038 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/LICENSE.txt
+-rw-rw-rw-   0 root         (0) root         (0)       85 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/MANIFEST.in
+-rw-rw-rw-   0 root         (0) root         (0)       34 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/requirements_dev.txt
+-rw-rw-rw-   0 root         (0) root         (0)     2987 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/setup.pytemplate
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.690717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.695717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/
+-rw-rw-rw-   0 root         (0) root         (0)      283 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/__init__.pytemplate
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.695717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/data/
+-rw-rw-rw-   0 root         (0) root         (0)      249 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/data/readme.txt
+-rw-rw-rw-   0 root         (0) root         (0)      348 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/src/emzed_ext_{{cookiecutter.pkg_name}}/example_module.pytemplate
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.695717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tests/
+-rw-rw-rw-   0 root         (0) root         (0)      320 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tests/test_{{cookiecutter.pkg_name}}.pytemplate
+-rw-rw-rw-   0 root         (0) root         (0)      249 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/tox.ini
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.695717 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_spyder_kernels/
+-rw-rw-rw-   0 root         (0) root         (0)     2184 2023-04-05 08:53:49.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_spyder_kernels/emzed_spyder_kernels.py
+-rw-rw-rw-   0 root         (0) root         (0)      252 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_spyder_kernels/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)     1637 2023-04-06 09:38:22.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/patch_all.py
+-rw-rw-rw-   0 root         (0) root         (0)     5079 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/patch_config.py
+-rw-rw-rw-   0 root         (0) root         (0)     5022 2023-04-05 08:53:49.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/patch_gui.py
+-rw-rw-rw-   0 root         (0) root         (0)     7846 2023-04-06 16:32:04.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/patch_remote_kernel_startup.py
+-rw-rw-rw-   0 root         (0) root         (0)    16235 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/remote_interpreter_startup.py
+-rw-rw-rw-   0 root         (0) root         (0)      234 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/start.py
+-rw-rw-rw-   0 root         (0) root         (0)     9300 2023-04-06 16:32:04.000000 emzed-spyder-3.0.0a8/src/emzed_spyder/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.693717 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      444 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1836 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      117 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)     2026 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-06 21:20:25.000000 emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 21:20:25.696717 emzed-spyder-3.0.0a8/tests/
+-rw-rw-rw-   0 root         (0) root         (0)     1536 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/tests/test_bootstrap.py
+-rw-rw-rw-   0 root         (0) root         (0)      173 2023-02-09 02:04:28.000000 emzed-spyder-3.0.0a8/tests/test_import.py
```

### Comparing `emzed-spyder-3.0.0a7/requirements.txt` & `emzed-spyder-3.0.0a8/requirements.txt`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/setup.py` & `emzed-spyder-3.0.0a8/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 analysis workflows in Python and makes experimenting with new analysis strategies for
 LCMS data as easy as possible.
 """
 
 
 setup(
     name="emzed-spyder",
-    version="3.0.0a7",
+    version="3.0.0a8",
     description="emzed IDE, see also https://emzed.ethz.ch",
     long_description=long_description,
     url="https://emzed.ethz.ch",
     author="Uwe Schmitt",
     author_email="uwe.schmitt@id.ethz.ch",
     license="MIT",
     package_dir={"": "src"},
```

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/assets/splash.png` & `emzed-spyder-3.0.0a8/src/emzed_spyder/assets/splash.png`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/LICENSE.txt` & `emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/setup.pytemplate` & `emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_package_template/{{cookiecutter.directory_name}}/setup.pytemplate`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/emzed_spyder_kernels/emzed_spyder_kernels.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/emzed_spyder_kernels/emzed_spyder_kernels.py`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/patch_all.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/patch_all.py`

 * *Files 3% similar despite different names*

```diff
@@ -19,16 +19,14 @@
     patch_editor_code_completion,
     patch_in_prompt,
 )
 from .patch_remote_kernel_startup import set_banner, set_emzed_spyder_kernels
 from .utils import setup_venv_for_remote_interpreter
 
 remote_executable = setup_venv_for_remote_interpreter()
-if remote_executable is None:
-    sys.exit(1)
 
 if os.environ.get("SPYDER_PYTEST") is not None:
     sys.exit(0)
 
 # order matters, if we'd run set_remote_python_interpreter eariler, patching the configs
 # would not work!
```

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/patch_config.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/patch_config.py`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/patch_gui.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/patch_gui.py`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/patch_remote_kernel_startup.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/patch_remote_kernel_startup.py`

 * *Files 7% similar despite different names*

```diff
@@ -3,16 +3,14 @@
 
 import os
 import re
 import subprocess
 import sys
 from datetime import datetime
 
-import pkg_resources
-
 from .utils import (
     active_python_exe,
     emzed_projects,
     get_active_project,
     is_valid_project,
     python_executable_in,
     update_active_project,
@@ -47,28 +45,17 @@
                 if (
                     python_exe is not None
                     and python_exe.exists()
                     and os.access(python_exe, os.X_OK)
                 ):
                     result[0] = str(python_exe)
             result[2] = "emzed_spyder_kernels"
+            print(result, file=sys.__stderr__)
             return result
 
-        @property
-        def env(self):
-            env_vars = super().env
-            try:
-                emzed_spyder_location = pkg_resources.require("emzed_spyder")[
-                    0
-                ].location
-                env_vars["EMZED_SPYDER_LOCATION"] = emzed_spyder_location
-            except pkg_resources.DistributionNotFound:
-                pass
-            return env_vars
-
     kernelspec.SpyderKernelSpec = PatchedKernelSpec
 
 
 ITALICS = "\033[0;3m"
 RESET = "\033[0;0m"
 BLUE_FG = "\033[0;34m"
 RED_FG = "\033[0;31m"
@@ -84,16 +71,15 @@
     |_____)_|_|_(_____)_____)\____|
 {FG_TEXT}
 {ITALICS}
       Copyright (c) 2020 ETH Zurich
              Scientific IT Services
               https://emzed.ethz.ch
 {RESET}
-run {ITALICS}emzed_help(){RESET} for an overview of
-available functions.
+run {ITALICS}emzed_help(){RESET} for an overview of available functions.
 """
 
 latest_version_check = None
 
 
 def set_banner(remote_interpreter):
     from spyder.plugins.ipythonconsole.widgets.shell import (
@@ -180,21 +166,22 @@
             + "you must close emzed.spyder first and then use pip to upgrade."
         )
 
     return lines
 
 
 def check_updates(remote_interpreter):
-    for package in ("emzed3", "emzed3_gui"):
+    for package in ("emzed", "emzed-gui"):
         yield _check_update(remote_interpreter, package)
 
 
 def _check_update(remote_interpreter, package):
 
     latest = _latest_version(remote_interpreter, package)
+    print(package, latest)
     if latest is None:
         return (package, None, None, f"could not determine latest version of {package}")
 
     local_version = _local_version(remote_interpreter, package)
     if isinstance(local_version, str):
         local_version = tuple(map(int, local_version.split(".")))
         local_version = (local_version + (0, 0))[:3]
@@ -206,34 +193,42 @@
 
 def _check_emzed_spyder_update():
     latest_version = _latest_version(sys.executable, "emzed_spyder")
     if latest_version is None:
         return None, None, "could not determine latest version of emzed_spyder"
     from . import __version__ as current_version_str
 
+    if "a" in current_version_str:
+        current_version_str = current_version_str.split("a")[0]
+    if "b" in current_version_str:
+        current_version_str = current_version_str.split("b")[0]
+
     current_version = tuple(map(int, current_version_str.split(".")))
     return latest_version, current_version, None
 
 
 def _latest_version(remote_interpreter, package):
 
     output = ""
     try:
         # will fail as version 'x' is not available, will print available versions
         # to stderr then:
         binary_only = "--only-binary :all:" if sys.platform == "win32" else ""
-        line = f"{remote_interpreter} -m pip install -v {binary_only}" f" {package}==x"
+        line = (
+            f"{remote_interpreter} -m pip install --pre -vv {binary_only}"
+            f" {package}==x"
+        )
         subprocess.check_output(line.split(), stderr=subprocess.STDOUT)
     except subprocess.CalledProcessError as e:
         output = str(e.output, "utf-8")
 
     versions = []
     for line in output.split("\n"):
         if "Found link" in line:
-            match = re.search(rf"/{package}-(\d+\.\d+\.\d+)", line)
+            match = re.search(r"version: (\d+\.\d+\.\d+)$", line)
             if match is not None:
                 versions.append(match.group(1))
 
     if versions:
         latest = max(tuple(map(int, version.split("."))) for version in versions)
         return latest
     return None
```

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/remote_interpreter_startup.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/remote_interpreter_startup.py`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder/utils.py` & `emzed-spyder-3.0.0a8/src/emzed_spyder/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 import subprocess
 import sys
 from datetime import datetime
 from os.path import abspath, dirname, join
 from pathlib import Path
 from subprocess import call, check_output
 
+import pkg_resources
 import requests
 
 IS_WIN = sys.platform == "win32"
 
 
 def win_app_data_folder():
     import winreg
@@ -132,15 +133,15 @@
 emzed_spyder installed.  locally.
 """
 
 
 cache_invalidation_token = str(random.random())
 
 DOWNLOAD_URL = (
-    "https://gitlab.com/emzed3/emzed-spyder/-/raw/development/setup_files_remote_shell"
+    "https://gitlab.com/emzed3/emzed-spyder/-/raw/main/setup_files_remote_shell"
     f"/setup_remote_shell_{sys.platform}.txt"
     f"?{cache_invalidation_token}"
 )
 
 
 IS_WIN = sys.platform == "win32"
 
@@ -273,33 +274,35 @@
         assert (
             site_packages is not None
         ), f"venv at {folder} has not site-packages sub folder"
         (site_packages / "remote_venv.pth").write_text(str(inherit_from))
 
     os.environ["QT_API"] = "pyqt5"
 
-    location = os.environ.get("EMZED_SPYDER_LOCATION")
-    if location is None:
-        print("internal error: setup venv failed.")
-        return
-
-    installed_in_edit_mode = location.endswith("/emzed_spyder/src")
+    installed_in_edit_mode = False
+    try:
+        location = pkg_resources.require("emzed_spyder")[0].location
+        installed_in_edit_mode = location.endswith("/emzed_spyder/src")
+    except Exception:
+        pass
 
     if installed_in_edit_mode:
+        print("emzed.spyder is installed in edit mode")
         # important during local testing
         with open(
             os.path.join(
                 os.path.dirname(location),
                 "setup_files_remote_shell",
                 f"setup_remote_shell_{sys.platform}.txt",
             )
         ) as fh:
             pip_install_args = fh.read()
 
     else:
+        print("download requirements file")
         response = requests.get(DOWNLOAD_URL)
         try:
             response.raise_for_status()
         except IOError as e:
             raise IOError(f"could not download setup files from {DOWNLOAD_URL}: {e}")
 
         pip_install_args = response.text
```

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/SOURCES.txt` & `emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/src/emzed_spyder.egg-info/requires.txt` & `emzed-spyder-3.0.0a8/src/emzed_spyder.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `emzed-spyder-3.0.0a7/tests/test_bootstrap.py` & `emzed-spyder-3.0.0a8/tests/test_bootstrap.py`

 * *Files identical despite different names*

