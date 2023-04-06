# Comparing `tmp/numerical-collection-py-0.2.0.tar.gz` & `tmp/numerical-collection-py-0.2.0a1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "numerical-collection-py-0.2.0.tar", last modified: Thu Apr  6 15:47:55 2023, max compression
+gzip compressed data, was "numerical-collection-py-0.2.0a1.tar", last modified: Thu Apr  6 15:25:41 2023, max compression
```

## Comparing `numerical-collection-py-0.2.0.tar` & `numerical-collection-py-0.2.0a1.tar`

### file list

```diff
@@ -1,66 +1,66 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.733447 numerical-collection-py-0.2.0/
--rw-rw-rw-   0 root         (0) root         (0)     2410 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/CMakeLists.txt
--rw-rw-rw-   0 root         (0) root         (0)    11358 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/LICENSE.txt
--rw-rw-rw-   0 root         (0) root         (0)      239 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2527 2023-04-06 15:47:55.732447 numerical-collection-py-0.2.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     1243 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/README.md
--rw-rw-rw-   0 root         (0) root         (0)       90 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/conanfile.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.717453 numerical-collection-py-0.2.0/cpp_module/
--rw-rw-rw-   0 root         (0) root         (0)      970 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/CMakeLists.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.718453 numerical-collection-py-0.2.0/cpp_module/base/
--rw-rw-rw-   0 root         (0) root         (0)     1686 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/base/bind.cpp
--rw-rw-rw-   0 root         (0) root         (0)      861 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/base/bind.h
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.720452 numerical-collection-py-0.2.0/cpp_module/logging/
--rw-rw-rw-   0 root         (0) root         (0)     2019 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/bind.cpp
--rw-rw-rw-   0 root         (0) root         (0)      828 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/bind.h
--rw-rw-rw-   0 root         (0) root         (0)     5000 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/config.cpp
--rw-rw-rw-   0 root         (0) root         (0)      927 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/config.h
--rw-rw-rw-   0 root         (0) root         (0)     2231 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/sinks.cpp
--rw-rw-rw-   0 root         (0) root         (0)     5350 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/logging/sinks.h
--rw-rw-rw-   0 root         (0) root         (0)      423 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/main.cpp
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.722451 numerical-collection-py-0.2.0/cpp_module/opt/
--rw-rw-rw-   0 root         (0) root         (0)      958 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/bind.cpp
--rw-rw-rw-   0 root         (0) root         (0)      820 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/bind.h
--rw-rw-rw-   0 root         (0) root         (0)     7729 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/multi_variate.cpp
--rw-rw-rw-   0 root         (0) root         (0)      854 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/multi_variate.h
--rw-rw-rw-   0 root         (0) root         (0)     3431 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/multi_variate_objective_function.h
--rw-rw-rw-   0 root         (0) root         (0)     2322 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/cpp_module/opt/multi_variate_optimizer_helper.h
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.723451 numerical-collection-py-0.2.0/num_collect/
--rw-rw-rw-   0 root         (0) root         (0)       99 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.724450 numerical-collection-py-0.2.0/num_collect/_cpp_module/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.725450 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/
--rw-rw-rw-   0 root         (0) root         (0)     7300 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/__init__.pyi
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.725450 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/
--rw-rw-rw-   0 root         (0) root         (0)      139 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/__init__.pyi
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.726450 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/
--rw-rw-rw-   0 root         (0) root         (0)     7707 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/__init__.pyi
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/py.typed
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/py.typed
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/py.typed
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/_cpp_module/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.727449 numerical-collection-py-0.2.0/num_collect/base/
--rw-rw-rw-   0 root         (0) root         (0)      541 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/base/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/base/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.728449 numerical-collection-py-0.2.0/num_collect/logging/
--rw-rw-rw-   0 root         (0) root         (0)      614 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/logging/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2466 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/logging/_handler.py
--rw-rw-rw-   0 root         (0) root         (0)     5835 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/logging/_logger.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/logging/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.729448 numerical-collection-py-0.2.0/num_collect/opt/
--rw-rw-rw-   0 root         (0) root         (0)       41 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/opt/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.730448 numerical-collection-py-0.2.0/num_collect/opt/multi_variate/
--rw-rw-rw-   0 root         (0) root         (0)      508 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/opt/multi_variate/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/opt/multi_variate/py.typed
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/opt/py.typed
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/num_collect/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:47:55.732447 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2527 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1673 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       19 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       12 2023-04-06 15:47:55.000000 numerical-collection-py-0.2.0/numerical_collection_py.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)     2015 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 15:47:55.733447 numerical-collection-py-0.2.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     5307 2023-04-06 15:47:24.000000 numerical-collection-py-0.2.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.860901 numerical-collection-py-0.2.0a1/
+-rw-rw-rw-   0 root         (0) root         (0)     2410 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/CMakeLists.txt
+-rw-rw-rw-   0 root         (0) root         (0)    11358 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/LICENSE.txt
+-rw-rw-rw-   0 root         (0) root         (0)      239 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2529 2023-04-06 15:25:41.860901 numerical-collection-py-0.2.0a1/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1243 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/README.md
+-rw-rw-rw-   0 root         (0) root         (0)       90 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/conanfile.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.843900 numerical-collection-py-0.2.0a1/cpp_module/
+-rw-rw-rw-   0 root         (0) root         (0)      970 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/CMakeLists.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.844900 numerical-collection-py-0.2.0a1/cpp_module/base/
+-rw-rw-rw-   0 root         (0) root         (0)     1686 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/base/bind.cpp
+-rw-rw-rw-   0 root         (0) root         (0)      861 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/base/bind.h
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.847900 numerical-collection-py-0.2.0a1/cpp_module/logging/
+-rw-rw-rw-   0 root         (0) root         (0)     2019 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/bind.cpp
+-rw-rw-rw-   0 root         (0) root         (0)      828 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/bind.h
+-rw-rw-rw-   0 root         (0) root         (0)     5000 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/config.cpp
+-rw-rw-rw-   0 root         (0) root         (0)      927 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/config.h
+-rw-rw-rw-   0 root         (0) root         (0)     2231 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/sinks.cpp
+-rw-rw-rw-   0 root         (0) root         (0)     5350 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/logging/sinks.h
+-rw-rw-rw-   0 root         (0) root         (0)      423 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/main.cpp
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.849900 numerical-collection-py-0.2.0a1/cpp_module/opt/
+-rw-rw-rw-   0 root         (0) root         (0)      958 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/bind.cpp
+-rw-rw-rw-   0 root         (0) root         (0)      820 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/bind.h
+-rw-rw-rw-   0 root         (0) root         (0)     7729 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate.cpp
+-rw-rw-rw-   0 root         (0) root         (0)      854 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate.h
+-rw-rw-rw-   0 root         (0) root         (0)     3431 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate_objective_function.h
+-rw-rw-rw-   0 root         (0) root         (0)     2322 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate_optimizer_helper.h
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.850901 numerical-collection-py-0.2.0a1/num_collect/
+-rw-rw-rw-   0 root         (0) root         (0)       99 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.851901 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.852901 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/
+-rw-rw-rw-   0 root         (0) root         (0)     7300 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/__init__.pyi
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.852901 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/
+-rw-rw-rw-   0 root         (0) root         (0)      139 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/__init__.pyi
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.853901 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/
+-rw-rw-rw-   0 root         (0) root         (0)     7707 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/__init__.pyi
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/_cpp_module/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.854901 numerical-collection-py-0.2.0a1/num_collect/base/
+-rw-rw-rw-   0 root         (0) root         (0)      541 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/base/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/base/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.856901 numerical-collection-py-0.2.0a1/num_collect/logging/
+-rw-rw-rw-   0 root         (0) root         (0)      614 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/logging/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2466 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/logging/_handler.py
+-rw-rw-rw-   0 root         (0) root         (0)     5835 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/logging/_logger.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/logging/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.856901 numerical-collection-py-0.2.0a1/num_collect/opt/
+-rw-rw-rw-   0 root         (0) root         (0)       41 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/opt/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.857901 numerical-collection-py-0.2.0a1/num_collect/opt/multi_variate/
+-rw-rw-rw-   0 root         (0) root         (0)      508 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/opt/multi_variate/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/opt/multi_variate/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/opt/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/num_collect/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 15:25:41.859902 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2529 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1673 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       19 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       12 2023-04-06 15:25:41.000000 numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)     2017 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 15:25:41.860901 numerical-collection-py-0.2.0a1/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     5307 2023-04-06 15:25:08.000000 numerical-collection-py-0.2.0a1/setup.py
```

### Comparing `numerical-collection-py-0.2.0/CMakeLists.txt` & `numerical-collection-py-0.2.0a1/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/LICENSE.txt` & `numerical-collection-py-0.2.0a1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/PKG-INFO` & `numerical-collection-py-0.2.0a1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: numerical-collection-py
-Version: 0.2.0
+Version: 0.2.0a1
 Summary: A collection of algorithms in numerical analysis for Python (originally implemented in C++).
 Home-page: https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py
 Author: Kenta Kabashima
 Author-email: kenta_program37@hotmail.co.jp
 License: Apache-2.0
 Project-URL: Bug Tracker, https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py/-/issues
 Project-URL: Documentation, https://musicscience37projects.gitlab.io/numerical-analysis/numerical-collection-py/
```

### Comparing `numerical-collection-py-0.2.0/README.md` & `numerical-collection-py-0.2.0a1/README.md`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/CMakeLists.txt` & `numerical-collection-py-0.2.0a1/cpp_module/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/base/bind.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/base/bind.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/base/bind.h` & `numerical-collection-py-0.2.0a1/cpp_module/base/bind.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/bind.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/logging/bind.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/bind.h` & `numerical-collection-py-0.2.0a1/cpp_module/logging/bind.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/config.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/logging/config.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/config.h` & `numerical-collection-py-0.2.0a1/cpp_module/logging/config.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/sinks.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/logging/sinks.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/logging/sinks.h` & `numerical-collection-py-0.2.0a1/cpp_module/logging/sinks.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/bind.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/opt/bind.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/bind.h` & `numerical-collection-py-0.2.0a1/cpp_module/opt/bind.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/multi_variate.cpp` & `numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate.cpp`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/multi_variate.h` & `numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/multi_variate_objective_function.h` & `numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate_objective_function.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/cpp_module/opt/multi_variate_optimizer_helper.h` & `numerical-collection-py-0.2.0a1/cpp_module/opt/multi_variate_optimizer_helper.h`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/__init__.pyi` & `numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/__init__.pyi`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/__init__.pyi` & `numerical-collection-py-0.2.0a1/num_collect/_cpp_module/num_collect_py_cpp_module/opt/multi_variate/__init__.pyi`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/base/__init__.py` & `numerical-collection-py-0.2.0a1/num_collect/base/__init__.py`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/logging/__init__.py` & `numerical-collection-py-0.2.0a1/num_collect/logging/__init__.py`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/logging/_handler.py` & `numerical-collection-py-0.2.0a1/num_collect/logging/_handler.py`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/num_collect/logging/_logger.py` & `numerical-collection-py-0.2.0a1/num_collect/logging/_logger.py`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/numerical_collection_py.egg-info/PKG-INFO` & `numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: numerical-collection-py
-Version: 0.2.0
+Version: 0.2.0a1
 Summary: A collection of algorithms in numerical analysis for Python (originally implemented in C++).
 Home-page: https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py
 Author: Kenta Kabashima
 Author-email: kenta_program37@hotmail.co.jp
 License: Apache-2.0
 Project-URL: Bug Tracker, https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py/-/issues
 Project-URL: Documentation, https://musicscience37projects.gitlab.io/numerical-analysis/numerical-collection-py/
```

### Comparing `numerical-collection-py-0.2.0/numerical_collection_py.egg-info/SOURCES.txt` & `numerical-collection-py-0.2.0a1/numerical_collection_py.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `numerical-collection-py-0.2.0/pyproject.toml` & `numerical-collection-py-0.2.0a1/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "numerical-collection-py"
-version = "0.2.0"
+version = "0.2.0a1"
 description = "A collection of algorithms in numerical analysis for Python (originally implemented in C++)."
 license = "Apache-2.0"
 authors = ["Kenta Kabashima <kenta_program37@hotmail.co.jp>"]
 readme = "README.md"
 homepage = "https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py"
 repository = "https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-collection-py"
 documentation = "https://musicscience37projects.gitlab.io/numerical-analysis/numerical-collection-py/"
```

### Comparing `numerical-collection-py-0.2.0/setup.py` & `numerical-collection-py-0.2.0a1/setup.py`

 * *Files identical despite different names*

