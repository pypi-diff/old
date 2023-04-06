# Comparing `tmp/python-project-structure-0.8.2.tar.gz` & `tmp/python-project-structure-0.8.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python-project-structure-0.8.2.tar", last modified: Fri Dec  9 23:04:58 2022, max compression
+gzip compressed data, was "python-project-structure-0.8.3.tar", last modified: Fri Dec  9 23:23:16 2022, max compression
```

## Comparing `python-project-structure-0.8.2.tar` & `python-project-structure-0.8.3.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.347515 python-project-structure-0.8.2/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      324 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.dir-locals.el.in
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1499 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.dockerignore
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      447 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.env.in
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.340515 python-project-structure-0.8.2/.github/
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.345515 python-project-structure-0.8.2/.github/workflows/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     4364 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.github/workflows/ci-cd.yml
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1499 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.gitignore
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2915 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.gitlab-ci.yml
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      555 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/.pre-commit-config.yaml
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1822 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/Dockerfile
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1029 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/Dockerfile.devel
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1081 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/LICENSE
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)    21840 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/Makefile
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     4944 2022-12-09 23:03:10.000000 python-project-structure-0.8.2/NEWS.rst
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)     8282 2022-12-09 23:04:58.348515 python-project-structure-0.8.2/PKG-INFO
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     7474 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/README.rst
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1760 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/TODO.rst
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.345515 python-project-structure-0.8.2/bin/
--rwxrwxrwx   0 python-project-structure  (1001) python-project-structure  (1001)      936 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/bin/entrypoint
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2728 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/docker-compose.override.yml
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      611 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/docker-compose.yml
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.345515 python-project-structure-0.8.2/home/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       65 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/home/.gitignore
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      327 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/home/.pypirc.in
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2043 2022-12-09 23:03:11.000000 python-project-structure-0.8.2/pyproject.toml
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2961 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/requirements-build.txt
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      812 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/requirements-build.txt.in
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2914 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/requirements-devel.txt
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      186 2022-12-09 23:03:11.000000 python-project-structure-0.8.2/requirements.txt
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1429 2022-12-09 23:04:58.348515 python-project-structure-0.8.2/setup.cfg
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.340515 python-project-structure-0.8.2/src/
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.346515 python-project-structure-0.8.2/src/python_project_structure.egg-info/
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)     8282 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/PKG-INFO
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      979 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/SOURCES.txt
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)        1 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/dependency_links.txt
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)       73 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/entry_points.txt
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      105 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/requires.txt
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)       23 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/python_project_structure.egg-info/top_level.txt
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.347515 python-project-structure-0.8.2/src/pythonprojectstructure/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     3395 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/src/pythonprojectstructure/__init__.py
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      223 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/src/pythonprojectstructure/__main__.py
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.347515 python-project-structure-0.8.2/src/pythonprojectstructure/newsfragments/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       91 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/src/pythonprojectstructure/newsfragments/.gitignore
-drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:04:58.347515 python-project-structure-0.8.2/src/pythonprojectstructure/tests/
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       72 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/src/pythonprojectstructure/tests/__init__.py
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     3875 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/src/pythonprojectstructure/tests/test_cli.py
--rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      176 2022-12-09 23:04:58.000000 python-project-structure-0.8.2/src/pythonprojectstructure/version.py
--rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2036 2022-12-09 23:02:37.000000 python-project-structure-0.8.2/tox.ini
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.116452 python-project-structure-0.8.3/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      324 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.dir-locals.el.in
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1499 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.dockerignore
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      447 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.env.in
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.107452 python-project-structure-0.8.3/.github/
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.112452 python-project-structure-0.8.3/.github/workflows/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     4364 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.github/workflows/ci-cd.yml
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1499 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.gitignore
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2915 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.gitlab-ci.yml
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      555 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/.pre-commit-config.yaml
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1822 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/Dockerfile
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1029 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/Dockerfile.devel
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1081 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/LICENSE
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)    21891 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/Makefile
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     5163 2022-12-09 23:21:24.000000 python-project-structure-0.8.3/NEWS.rst
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)     8282 2022-12-09 23:23:16.116452 python-project-structure-0.8.3/PKG-INFO
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     7474 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/README.rst
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1760 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/TODO.rst
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.113452 python-project-structure-0.8.3/bin/
+-rwxrwxrwx   0 python-project-structure  (1001) python-project-structure  (1001)      936 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/bin/entrypoint
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2728 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/docker-compose.override.yml
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      611 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/docker-compose.yml
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.113452 python-project-structure-0.8.3/home/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       65 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/home/.gitignore
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      327 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/home/.pypirc.in
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2043 2022-12-09 23:21:24.000000 python-project-structure-0.8.3/pyproject.toml
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2961 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/requirements-build.txt
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      812 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/requirements-build.txt.in
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2914 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/requirements-devel.txt
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      186 2022-12-09 23:21:25.000000 python-project-structure-0.8.3/requirements.txt
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     1429 2022-12-09 23:23:16.117452 python-project-structure-0.8.3/setup.cfg
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.107452 python-project-structure-0.8.3/src/
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.114452 python-project-structure-0.8.3/src/python_project_structure.egg-info/
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)     8282 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/PKG-INFO
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      979 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/SOURCES.txt
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)        1 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/dependency_links.txt
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)       73 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/entry_points.txt
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      105 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/requires.txt
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)       23 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/python_project_structure.egg-info/top_level.txt
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.115452 python-project-structure-0.8.3/src/pythonprojectstructure/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     3395 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/src/pythonprojectstructure/__init__.py
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)      223 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/src/pythonprojectstructure/__main__.py
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.115452 python-project-structure-0.8.3/src/pythonprojectstructure/newsfragments/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       91 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/src/pythonprojectstructure/newsfragments/.gitignore
+drwxr-xr-x   0 python-project-structure  (1001) python-project-structure  (1001)        0 2022-12-09 23:23:16.116452 python-project-structure-0.8.3/src/pythonprojectstructure/tests/
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)       72 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/src/pythonprojectstructure/tests/__init__.py
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     3875 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/src/pythonprojectstructure/tests/test_cli.py
+-rw-r--r--   0 python-project-structure  (1001) python-project-structure  (1001)      176 2022-12-09 23:23:16.000000 python-project-structure-0.8.3/src/pythonprojectstructure/version.py
+-rw-rw-rw-   0 python-project-structure  (1001) python-project-structure  (1001)     2036 2022-12-09 23:20:50.000000 python-project-structure-0.8.3/tox.ini
```

### Comparing `python-project-structure-0.8.2/.dockerignore` & `python-project-structure-0.8.3/.dockerignore`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/.github/workflows/ci-cd.yml` & `python-project-structure-0.8.3/.github/workflows/ci-cd.yml`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/.gitignore` & `python-project-structure-0.8.3/.gitignore`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/.gitlab-ci.yml` & `python-project-structure-0.8.3/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/.pre-commit-config.yaml` & `python-project-structure-0.8.3/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/Dockerfile` & `python-project-structure-0.8.3/Dockerfile`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/Dockerfile.devel` & `python-project-structure-0.8.3/Dockerfile.devel`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/LICENSE` & `python-project-structure-0.8.3/LICENSE`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/Makefile` & `python-project-structure-0.8.3/Makefile`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,16 @@
 .DELETE_ON_ERROR:
 MAKEFLAGS+=--warn-undefined-variables
 MAKEFLAGS+=--no-builtin-rules
 PS1?=$$
 
 # Project-specific variables
 GPG_SIGNING_KEYID=2EFF7CCE6828E359
-CI_REGISTRY_IMAGE=registry.gitlab.com/rpatterson/python-project-structure
+GITHUB_REPOSITORY_OWNER=rpatterson
+CI_REGISTRY_IMAGE=registry.gitlab.com/$(GITHUB_REPOSITORY_OWNER)/python-project-structure
 
 # Values derived from the environment
 USER_NAME:=$(shell id -u -n)
 USER_FULL_NAME=$(shell getent passwd "$(USER_NAME)" | cut -d ":" -f 5 | cut -d "," -f 1)
 ifeq ($(USER_FULL_NAME),)
 USER_FULL_NAME=$(USER_NAME)
 endif
```

### Comparing `python-project-structure-0.8.2/NEWS.rst` & `python-project-structure-0.8.3/NEWS.rst`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,22 @@
+Pythonprojectstructure 0.8.3 (2022-12-09)
+=========================================
+
+No significant changes.
+
+
+Pythonprojectstructure 0.8.3b0 (2022-12-09)
+===========================================
+
+Misc
+----
+
+- #37
+
+
 Pythonprojectstructure 0.8.2 (2022-12-09)
 =========================================
 
 No significant changes.
 
 
 Pythonprojectstructure 0.8.2b2 (2022-12-09)
```

### Comparing `python-project-structure-0.8.2/PKG-INFO` & `python-project-structure-0.8.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-project-structure
-Version: 0.8.2
+Version: 0.8.3
 Summary: Python project structure foundation or template, CLI console scripts.
 Home-page: https://gitlab.com/rpatterson/python-project-structure
 Author: Ross Patterson
 Author-email: me@rpatterson.net
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
```

### Comparing `python-project-structure-0.8.2/README.rst` & `python-project-structure-0.8.3/README.rst`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/TODO.rst` & `python-project-structure-0.8.3/TODO.rst`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/bin/entrypoint` & `python-project-structure-0.8.3/bin/entrypoint`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/docker-compose.override.yml` & `python-project-structure-0.8.3/docker-compose.override.yml`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/docker-compose.yml` & `python-project-structure-0.8.3/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/pyproject.toml` & `python-project-structure-0.8.3/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 # local_scheme = "no-local-version"
 [tool.commitizen]
 # Parse commit messages according to conventional commits to decide wether the next
 # versin tag should be a major, minor or patch bump and create the VCS tag.  Also
 # provides VCS hooks to enforce that commit messages comply with conventional commits:
 # https://commitizen-tools.github.io/commitizen/
 name = "cz_conventional_commits"
-version = "0.8.2"
+version = "0.8.3"
 tag_format = "v$version"
 annotated_tag = true
 bump_message = """\
 build(release): Version $current_version → $new_version
 
 [actions skip]
 """
```

### Comparing `python-project-structure-0.8.2/requirements-build.txt` & `python-project-structure-0.8.3/requirements-build.txt`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/requirements-build.txt.in` & `python-project-structure-0.8.3/requirements-build.txt.in`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/requirements-devel.txt` & `python-project-structure-0.8.3/requirements-devel.txt`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/setup.cfg` & `python-project-structure-0.8.3/setup.cfg`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/src/python_project_structure.egg-info/PKG-INFO` & `python-project-structure-0.8.3/src/python_project_structure.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-project-structure
-Version: 0.8.2
+Version: 0.8.3
 Summary: Python project structure foundation or template, CLI console scripts.
 Home-page: https://gitlab.com/rpatterson/python-project-structure
 Author: Ross Patterson
 Author-email: me@rpatterson.net
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
```

### Comparing `python-project-structure-0.8.2/src/python_project_structure.egg-info/SOURCES.txt` & `python-project-structure-0.8.3/src/python_project_structure.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/src/pythonprojectstructure/__init__.py` & `python-project-structure-0.8.3/src/pythonprojectstructure/__init__.py`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/src/pythonprojectstructure/tests/test_cli.py` & `python-project-structure-0.8.3/src/pythonprojectstructure/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `python-project-structure-0.8.2/tox.ini` & `python-project-structure-0.8.3/tox.ini`

 * *Files identical despite different names*

