# Comparing `tmp/jupyverse-0.0.7.tar.gz` & `tmp/jupyverse-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jupyverse-0.0.7.tar", last modified: Thu Sep 16 16:07:17 2021, max compression
+gzip compressed data, last modified: Sun Feb  2 00:00:00 2020, max compression
```

## Comparing `jupyverse-0.0.7.tar` & `jupyverse-0.1.2.tar`

### file list

```diff
@@ -1,21 +1,207 @@
-drwxrwxr-x   0 david     (1000) david     (1000)        0 2021-09-16 16:07:17.835438 jupyverse-0.0.7/
--rw-rw-r--   0 david     (1000) david     (1000)     1081 2021-09-13 07:14:31.000000 jupyverse-0.0.7/LICENSE
--rw-rw-r--   0 david     (1000) david     (1000)       37 2021-09-13 07:14:31.000000 jupyverse-0.0.7/MANIFEST.in
--rw-rw-r--   0 david     (1000) david     (1000)     3095 2021-09-16 16:07:17.835438 jupyverse-0.0.7/PKG-INFO
--rw-rw-r--   0 david     (1000) david     (1000)     2594 2021-09-16 16:00:05.000000 jupyverse-0.0.7/README.md
-drwxrwxr-x   0 david     (1000) david     (1000)        0 2021-09-16 16:07:17.835438 jupyverse-0.0.7/jupyverse/
--rw-rw-r--   0 david     (1000) david     (1000)       42 2021-09-13 07:14:31.000000 jupyverse-0.0.7/jupyverse/__init__.py
--rw-rw-r--   0 david     (1000) david     (1000)       72 2021-09-16 16:02:17.000000 jupyverse-0.0.7/jupyverse/_version.py
-drwxrwxr-x   0 david     (1000) david     (1000)        0 2021-09-16 16:07:17.835438 jupyverse-0.0.7/jupyverse/static/
--rw-rw-r--   0 david     (1000) david     (1000)    32038 2021-09-13 07:14:31.000000 jupyverse-0.0.7/jupyverse/static/favicon.ico
-drwxrwxr-x   0 david     (1000) david     (1000)        0 2021-09-16 16:07:17.835438 jupyverse-0.0.7/jupyverse.egg-info/
--rw-rw-r--   0 david     (1000) david     (1000)     3095 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/PKG-INFO
--rw-rw-r--   0 david     (1000) david     (1000)      341 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/SOURCES.txt
--rw-rw-r--   0 david     (1000) david     (1000)        1 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/dependency_links.txt
--rw-rw-r--   0 david     (1000) david     (1000)       43 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/entry_points.txt
--rw-rw-r--   0 david     (1000) david     (1000)      177 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/requires.txt
--rw-rw-r--   0 david     (1000) david     (1000)       18 2021-09-16 16:07:17.000000 jupyverse-0.0.7/jupyverse.egg-info/top_level.txt
-drwxrwxr-x   0 david     (1000) david     (1000)        0 2021-09-16 16:07:17.835438 jupyverse-0.0.7/plugins/
--rw-rw-r--   0 david     (1000) david     (1000)      104 2021-09-13 07:14:31.000000 jupyverse-0.0.7/plugins/__init__.py
--rw-rw-r--   0 david     (1000) david     (1000)      894 2021-09-16 16:07:17.835438 jupyverse-0.0.7/setup.cfg
--rw-rw-r--   0 david     (1000) david     (1000)       38 2021-09-13 12:38:46.000000 jupyverse-0.0.7/setup.py
+-rw-r--r--   0        0        0      691 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.pre-commit-config.yaml
+-rw-r--r--   0        0        0    58291 2020-02-02 00:00:00.000000 jupyverse-0.1.2/CHANGELOG.md
+-rw-r--r--   0        0        0     1066 2020-02-02 00:00:00.000000 jupyverse-0.1.2/CONTRIBUTING.md
+-rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 jupyverse-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0      895 2020-02-02 00:00:00.000000 jupyverse-0.1.2/config.yaml
+-rw-r--r--   0        0        0     1240 2020-02-02 00:00:00.000000 jupyverse-0.1.2/mkdocs.yml
+-rw-r--r--   0        0        0       38 2020-02-02 00:00:00.000000 jupyverse-0.1.2/pytest.ini
+-rw-r--r--   0        0        0     1804 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.devcontainer/devcontainer.json
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.devcontainer/requirements.txt
+-rw-r--r--   0        0        0     1913 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.github/workflows/check-release.yml
+-rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.github/workflows/main.yml
+-rw-r--r--   0        0        0      140 2020-02-02 00:00:00.000000 jupyverse-0.1.2/binder/environment.yml
+-rw-r--r--   0        0        0     1036 2020-02-02 00:00:00.000000 jupyverse-0.1.2/binder/jupyter_notebook_config.py
+-rw-r--r--   0        0        0      446 2020-02-02 00:00:00.000000 jupyverse-0.1.2/binder/postBuild
+-rw-r--r--   0        0        0      251 2020-02-02 00:00:00.000000 jupyverse-0.1.2/binder/start
+-rw-r--r--   0        0        0      893 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/index.md
+-rw-r--r--   0        0        0     5262 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/install.md
+-rw-r--r--   0        0        0    11002 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/jupyter.svg
+-rw-r--r--   0        0        0     3711 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/auth.md
+-rw-r--r--   0        0        0      235 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/contents.md
+-rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/frontend.md
+-rw-r--r--   0        0        0       48 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/jupyterlab.md
+-rw-r--r--   0        0        0      128 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/kernels.md
+-rw-r--r--   0        0        0       75 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/lab.md
+-rw-r--r--   0        0        0       96 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/login.md
+-rw-r--r--   0        0        0       79 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/nbconvert.md
+-rw-r--r--   0        0        0      153 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/resource_usage.md
+-rw-r--r--   0        0        0       44 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/retrolab.md
+-rw-r--r--   0        0        0      100 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/terminals.md
+-rw-r--r--   0        0        0      108 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/plugins/yjs.md
+-rw-r--r--   0        0        0     2854 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/usage/multi_user.md
+-rw-r--r--   0        0        0     2472 2020-02-02 00:00:00.000000 jupyverse-0.1.2/docs/usage/single_user.md
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse/__init__.py
+-rw-r--r--   0        0        0     2006 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse/cli.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse/py.typed
+-rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse/static/favicon.ico
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/COPYING.md
+-rw-r--r--   0        0        0       47 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/README.md
+-rw-r--r--   0        0        0     1191 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/pyproject.toml
+-rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/__init__.py
+-rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/exceptions.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/py.typed
+-rw-r--r--   0        0        0     1820 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/app/__init__.py
+-rw-r--r--   0        0        0      612 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/auth/__init__.py
+-rw-r--r--   0        0        0      308 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/auth/models.py
+-rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/contents/__init__.py
+-rw-r--r--   0        0        0      474 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/contents/models.py
+-rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/frontend/__init__.py
+-rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/jupyterlab/__init__.py
+-rw-r--r--   0        0        0      366 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/kernels/__init__.py
+-rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/kernels/models.py
+-rw-r--r--   0        0        0      464 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/lab/__init__.py
+-rw-r--r--   0        0        0       65 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/login/__init__.py
+-rw-r--r--   0        0        0     2191 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/main/__init__.py
+-rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/nbconvert/__init__.py
+-rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/resource_usage/__init__.py
+-rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/retrolab/__init__.py
+-rw-r--r--   0        0        0      281 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/terminals/__init__.py
+-rw-r--r--   0        0        0      110 2020-02-02 00:00:00.000000 jupyverse-0.1.2/jupyverse_api/jupyverse_api/yjs/__init__.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/MANIFEST.in
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/README.md
+-rw-r--r--   0        0        0      950 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/__init__.py
+-rw-r--r--   0        0        0    10954 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/backends.py
+-rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/config.py
+-rw-r--r--   0        0        0     3281 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/db.py
+-rw-r--r--   0        0        0     2229 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/main.py
+-rw-r--r--   0        0        0      406 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/py.typed
+-rw-r--r--   0        0        0     5837 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth/fps_auth/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/MANIFEST.in
+-rw-r--r--   0        0        0       71 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/README.md
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/fps_auth_fief/__init__.py
+-rw-r--r--   0        0        0     4008 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/fps_auth_fief/backend.py
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/fps_auth_fief/config.py
+-rw-r--r--   0        0        0      616 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/fps_auth_fief/main.py
+-rw-r--r--   0        0        0     2797 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/auth_fief/fps_auth_fief/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/MANIFEST.in
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/README.md
+-rw-r--r--   0        0        0      965 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/__init__.py
+-rw-r--r--   0        0        0     8386 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/fileid.py
+-rw-r--r--   0        0        0      501 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/main.py
+-rw-r--r--   0        0        0      259 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/py.typed
+-rw-r--r--   0        0        0    10716 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/contents/fps_contents/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/MANIFEST.in
+-rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/README.md
+-rw-r--r--   0        0        0      896 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/fps_frontend/__init__.py
+-rw-r--r--   0        0        0      364 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/fps_frontend/main.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/frontend/fps_frontend/py.typed
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/MANIFEST.in
+-rw-r--r--   0        0        0       56 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/README.md
+-rw-r--r--   0        0        0      930 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/fps_jupyterlab/__init__.py
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/fps_jupyterlab/index.py
+-rw-r--r--   0        0        0      965 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/fps_jupyterlab/main.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/fps_jupyterlab/py.typed
+-rw-r--r--   0        0        0     6692 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/jupyterlab/fps_jupyterlab/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/MANIFEST.in
+-rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/README.md
+-rw-r--r--   0        0        0      987 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/__init__.py
+-rw-r--r--   0        0        0     1582 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/main.py
+-rw-r--r--   0        0        0    15262 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/routes.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/__init__.py
+-rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/connect.py
+-rw-r--r--   0        0        0     8632 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/driver.py
+-rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/kernelspec.py
+-rw-r--r--   0        0        0     4078 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/message.py
+-rw-r--r--   0        0        0     2916 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_driver/paths.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_server/__init__.py
+-rw-r--r--   0        0        0     2731 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_server/message.py
+-rw-r--r--   0        0        0    11591 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/kernels/fps_kernels/kernel_server/server.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/MANIFEST.in
+-rw-r--r--   0        0        0       58 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/README.md
+-rw-r--r--   0        0        0      874 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/fps_lab/__init__.py
+-rw-r--r--   0        0        0      733 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/fps_lab/main.py
+-rw-r--r--   0        0        0     9498 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/lab/fps_lab/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/COPYING.md
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/MANIFEST.in
+-rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/README.md
+-rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/__init__.py
+-rw-r--r--   0        0        0      487 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/main.py
+-rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/routes.py
+-rw-r--r--   0        0        0     3104 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/index.html
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-busy-1.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-busy-2.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-busy-3.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-file.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-notebook.ico
+-rw-r--r--   0        0        0     1150 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon-terminal.ico
+-rw-r--r--   0        0        0    32038 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/favicons/favicon.ico
+-rw-r--r--   0        0        0     2798 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/logo/github.svg
+-rw-r--r--   0        0        0     5922 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/logo/logo.png
+-rw-r--r--   0        0        0     1408 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/login/fps_login/static/style/index.css
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/MANIFEST.in
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/README.md
+-rw-r--r--   0        0        0      909 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/fps_nbconvert/__init__.py
+-rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/fps_nbconvert/main.py
+-rw-r--r--   0        0        0     1563 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/nbconvert/fps_nbconvert/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/MANIFEST.in
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/README.md
+-rw-r--r--   0        0        0      868 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/fps_noauth/__init__.py
+-rw-r--r--   0        0        0      787 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/fps_noauth/backends.py
+-rw-r--r--   0        0        0      293 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/fps_noauth/main.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/noauth/fps_noauth/py.typed
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/COPYING.md
+-rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/README.md
+-rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/fps_resource_usage/__init__.py
+-rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/fps_resource_usage/main.py
+-rw-r--r--   0        0        0     2620 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/resource_usage/fps_resource_usage/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/MANIFEST.in
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/README.md
+-rw-r--r--   0        0        0      899 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/fps_retrolab/__init__.py
+-rw-r--r--   0        0        0      738 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/fps_retrolab/main.py
+-rw-r--r--   0        0        0     6717 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/retrolab/fps_retrolab/routes.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/MANIFEST.in
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/README.md
+-rw-r--r--   0        0        0      951 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/__init__.py
+-rw-r--r--   0        0        0      726 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/main.py
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/models.py
+-rw-r--r--   0        0        0     2442 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/routes.py
+-rw-r--r--   0        0        0     2419 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/server.py
+-rw-r--r--   0        0        0     1850 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/terminals/fps_terminals/win_server.py
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/COPYING.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/MANIFEST.in
+-rw-r--r--   0        0        0       42 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/README.md
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/pyproject.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/fps_yjs/__init__.py
+-rw-r--r--   0        0        0      996 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/fps_yjs/main.py
+-rw-r--r--   0        0        0      103 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/fps_yjs/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/fps_yjs/py.typed
+-rw-r--r--   0        0        0    15573 2020-02-02 00:00:00.000000 jupyverse-0.1.2/plugins/yjs/fps_yjs/routes.py
+-rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/conftest.py
+-rw-r--r--   0        0        0     4485 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/test_auth.py
+-rw-r--r--   0        0        0     2507 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/test_contents.py
+-rw-r--r--   0        0        0     3574 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/test_kernels.py
+-rw-r--r--   0        0        0     3995 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/test_server.py
+-rw-r--r--   0        0        0     2016 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/test_settings.py
+-rw-r--r--   0        0        0     3965 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/utils.py
+-rw-r--r--   0        0        0     1097 2020-02-02 00:00:00.000000 jupyverse-0.1.2/tests/data/notebook0.ipynb
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 jupyverse-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 jupyverse-0.1.2/COPYING.md
+-rw-r--r--   0        0        0      938 2020-02-02 00:00:00.000000 jupyverse-0.1.2/README.md
+-rw-r--r--   0        0        0     4703 2020-02-02 00:00:00.000000 jupyverse-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     2545 2020-02-02 00:00:00.000000 jupyverse-0.1.2/PKG-INFO
```

### Comparing `jupyverse-0.0.7/jupyverse/static/favicon.ico` & `jupyverse-0.1.2/jupyverse/static/favicon.ico`

 * *Files identical despite different names*

