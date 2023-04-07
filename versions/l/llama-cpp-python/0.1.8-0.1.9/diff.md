# Comparing `tmp/llama_cpp_python-0.1.8.tar.gz` & `tmp/llama_cpp_python-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "llama_cpp_python-0.1.8.tar", last modified: Tue Mar 28 08:04:39 2023, max compression
+gzip compressed data, was "llama_cpp_python-0.1.9.tar", last modified: Tue Mar 28 09:00:43 2023, max compression
```

## Comparing `llama_cpp_python-0.1.8.tar` & `llama_cpp_python-0.1.9.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     3106 2023-03-23 17:47:31.000000 llama_cpp_python-0.1.8/.gitignore
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      102 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/.gitmodules
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      181 2023-03-23 20:57:17.000000 llama_cpp_python-0.1.8/CMakeLists.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1069 2023-03-23 03:03:12.000000 llama_cpp_python-0.1.8/LICENSE.md
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      192 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/PKG-INFO
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1741 2023-03-27 22:29:57.000000 llama_cpp_python-0.1.8/README.md
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.614952 llama_cpp_python-0.1.8/_skbuild/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.618952 llama_cpp_python-0.1.8/_skbuild/linux-x86_64-3.8/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.618952 llama_cpp_python-0.1.8/_skbuild/linux-x86_64-3.8/cmake-install/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.618952 llama_cpp_python-0.1.8/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/
--rw-r--r--   0 andrei    (1000) andrei    (1000)   449360 2023-03-28 08:01:07.000000 llama_cpp_python-0.1.8/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/libllama.so
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.622952 llama_cpp_python-0.1.8/llama_cpp/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)       46 2023-03-24 18:50:13.000000 llama_cpp_python-0.1.8/llama_cpp/__init__.py
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    10812 2023-03-28 08:02:12.000000 llama_cpp_python-0.1.8/llama_cpp/llama.py
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     7167 2023-03-25 20:17:04.000000 llama_cpp_python-0.1.8/llama_cpp/llama_cpp.py
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.622952 llama_cpp_python-0.1.8/llama_cpp_python.egg-info/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      192 2023-03-28 08:04:39.000000 llama_cpp_python-0.1.8/llama_cpp_python.egg-info/PKG-INFO
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1338 2023-03-28 08:04:39.000000 llama_cpp_python-0.1.8/llama_cpp_python.egg-info/SOURCES.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)        1 2023-03-28 08:04:39.000000 llama_cpp_python-0.1.8/llama_cpp_python.egg-info/dependency_links.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)       10 2023-03-28 08:04:39.000000 llama_cpp_python-0.1.8/llama_cpp_python.egg-info/top_level.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    89316 2023-03-24 19:53:09.000000 llama_cpp_python-0.1.8/poetry.lock
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      753 2023-03-28 08:04:17.000000 llama_cpp_python-0.1.8/pyproject.toml
--rw-rw-r--   0 andrei    (1000) andrei    (1000)       38 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/setup.cfg
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      249 2023-03-28 08:04:12.000000 llama_cpp_python-0.1.8/setup.py
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.618952 llama_cpp_python-0.1.8/vendor/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.626952 llama_cpp_python-0.1.8/vendor/llama.cpp/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/.devops/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      328 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.devops/full.Dockerfile
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      259 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.devops/main.Dockerfile
--rwxrwxr-x   0 andrei    (1000) andrei    (1000)     1493 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.devops/tools.sh
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      231 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.dockerignore
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.618952 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/ISSUE_TEMPLATE/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    10063 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/ISSUE_TEMPLATE/custom.md
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/workflows/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    13191 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/workflows/build.yml
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1961 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.github/workflows/docker.yml
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      258 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/.gitignore
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     7695 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/CMakeLists.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1072 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/LICENSE
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     6838 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/Makefile
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    16157 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/README.md
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1898 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/SHA256SUMS
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     6042 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/convert-gptq-to-ggml.py
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     5373 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/convert-pth-to-ggml.py
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1025 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/flake.lock
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1557 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/flake.nix
--rw-rw-r--   0 andrei    (1000) andrei    (1000)   324514 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/ggml.c
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    22462 2023-03-24 18:36:08.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/ggml.h
--rw-rw-r--   0 andrei    (1000) andrei    (1000)    62703 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/llama.cpp
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     5180 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/llama.h
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/models/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)   432610 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/models/ggml-vocab.bin
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/prompts/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      106 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/prompts/alpaca.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      387 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/prompts/chat-with-bob.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     4289 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/quantize.py
-drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 08:04:39.630952 llama_cpp_python-0.1.8/vendor/llama.cpp/tests/
--rw-rw-r--   0 andrei    (1000) andrei    (1000)      408 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/tests/CMakeLists.txt
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     1362 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/tests/test-quantize.c
--rw-rw-r--   0 andrei    (1000) andrei    (1000)     2530 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.8/vendor/llama.cpp/tests/test-tokenizer-0.cpp
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.074222 llama_cpp_python-0.1.9/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     3106 2023-03-23 17:47:31.000000 llama_cpp_python-0.1.9/.gitignore
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      102 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/.gitmodules
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      181 2023-03-23 20:57:17.000000 llama_cpp_python-0.1.9/CMakeLists.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1069 2023-03-23 03:03:12.000000 llama_cpp_python-0.1.9/LICENSE.md
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      192 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/PKG-INFO
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1741 2023-03-27 22:29:57.000000 llama_cpp_python-0.1.9/README.md
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.062222 llama_cpp_python-0.1.9/_skbuild/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.062222 llama_cpp_python-0.1.9/_skbuild/linux-x86_64-3.8/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.062222 llama_cpp_python-0.1.9/_skbuild/linux-x86_64-3.8/cmake-install/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.066222 llama_cpp_python-0.1.9/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/
+-rw-r--r--   0 andrei    (1000) andrei    (1000)   449360 2023-03-28 08:01:07.000000 llama_cpp_python-0.1.9/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/libllama.so
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.066222 llama_cpp_python-0.1.9/llama_cpp/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)       46 2023-03-24 18:50:13.000000 llama_cpp_python-0.1.9/llama_cpp/__init__.py
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    11210 2023-03-28 08:39:12.000000 llama_cpp_python-0.1.9/llama_cpp/llama.py
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     7167 2023-03-25 20:17:04.000000 llama_cpp_python-0.1.9/llama_cpp/llama_cpp.py
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.066222 llama_cpp_python-0.1.9/llama_cpp_python.egg-info/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      192 2023-03-28 09:00:43.000000 llama_cpp_python-0.1.9/llama_cpp_python.egg-info/PKG-INFO
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1338 2023-03-28 09:00:43.000000 llama_cpp_python-0.1.9/llama_cpp_python.egg-info/SOURCES.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)        1 2023-03-28 09:00:43.000000 llama_cpp_python-0.1.9/llama_cpp_python.egg-info/dependency_links.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)       10 2023-03-28 09:00:43.000000 llama_cpp_python-0.1.9/llama_cpp_python.egg-info/top_level.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    89316 2023-03-24 19:53:09.000000 llama_cpp_python-0.1.9/poetry.lock
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      753 2023-03-28 09:00:20.000000 llama_cpp_python-0.1.9/pyproject.toml
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)       38 2023-03-28 09:00:43.074222 llama_cpp_python-0.1.9/setup.cfg
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      249 2023-03-28 09:00:16.000000 llama_cpp_python-0.1.9/setup.py
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.062222 llama_cpp_python-0.1.9/vendor/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/.devops/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      328 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.devops/full.Dockerfile
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      259 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.devops/main.Dockerfile
+-rwxrwxr-x   0 andrei    (1000) andrei    (1000)     1493 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.devops/tools.sh
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      231 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.dockerignore
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.062222 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/ISSUE_TEMPLATE/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    10063 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/ISSUE_TEMPLATE/custom.md
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/workflows/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    13191 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/workflows/build.yml
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1961 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.github/workflows/docker.yml
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      258 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/.gitignore
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     7695 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/CMakeLists.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1072 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/LICENSE
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     6838 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/Makefile
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    16157 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/README.md
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1898 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/SHA256SUMS
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     6042 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/convert-gptq-to-ggml.py
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     5373 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/convert-pth-to-ggml.py
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1025 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/flake.lock
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1557 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/flake.nix
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)   324514 2023-03-26 17:58:56.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/ggml.c
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    22462 2023-03-24 18:36:08.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/ggml.h
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)    62703 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/llama.cpp
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     5180 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/llama.h
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/models/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)   432610 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/models/ggml-vocab.bin
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/prompts/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      106 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/prompts/alpaca.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      387 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/prompts/chat-with-bob.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     4289 2023-03-23 20:56:51.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/quantize.py
+drwxrwxr-x   0 andrei    (1000) andrei    (1000)        0 2023-03-28 09:00:43.070222 llama_cpp_python-0.1.9/vendor/llama.cpp/tests/
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)      408 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/tests/CMakeLists.txt
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     1362 2023-03-23 09:36:33.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/tests/test-quantize.c
+-rw-rw-r--   0 andrei    (1000) andrei    (1000)     2530 2023-03-25 20:12:18.000000 llama_cpp_python-0.1.9/vendor/llama.cpp/tests/test-tokenizer-0.cpp
```

### Comparing `llama_cpp_python-0.1.8/.gitignore` & `llama_cpp_python-0.1.9/.gitignore`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/LICENSE.md` & `llama_cpp_python-0.1.9/LICENSE.md`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/README.md` & `llama_cpp_python-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/libllama.so` & `llama_cpp_python-0.1.9/_skbuild/linux-x86_64-3.8/cmake-install/llama_cpp/libllama.so`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/llama_cpp/llama.py` & `llama_cpp_python-0.1.9/llama_cpp/llama.py`

 * *Files 3% similar despite different names*

```diff
@@ -101,14 +101,28 @@
             The detokenized string.
         """
         output = b""
         for token in tokens:
             output += llama_cpp.llama_token_to_str(self.ctx, token)
         return output
 
+    def embed(self, text: str):
+        """Embed a string.
+
+        Args:
+            text: The utf-8 encoded string to embed.
+
+        Returns:
+            A list of embeddings.
+        """
+        tokens = self.tokenize(text.encode("utf-8"))
+        self._eval(tokens, 0)
+        embeddings = llama_cpp.llama_get_embeddings(self.ctx)
+        return embeddings[:llama_cpp.llama_n_embd(self.ctx)]
+
     def _eval(self, tokens: List[int], n_past):
         rc = llama_cpp.llama_eval(
             self.ctx,
             (llama_cpp.llama_token * len(tokens))(*tokens),
             len(tokens),
             n_past,
             self.n_threads,
```

### Comparing `llama_cpp_python-0.1.8/llama_cpp/llama_cpp.py` & `llama_cpp_python-0.1.9/llama_cpp/llama_cpp.py`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/llama_cpp_python.egg-info/SOURCES.txt` & `llama_cpp_python-0.1.9/llama_cpp_python.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/poetry.lock` & `llama_cpp_python-0.1.9/poetry.lock`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/pyproject.toml` & `llama_cpp_python-0.1.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "llama_cpp"
-version = "0.1.8"
+version = "0.1.9"
 description = "Python bindings for the llama.cpp library"
 authors = ["Andrei Betlen <abetlen@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://github.com/abetlen/llama-cpp-python"
 repository = "https://github.com/abetlen/llama-cpp-python"
 packages = [{include = "llama_cpp"}]
```

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/.devops/tools.sh` & `llama_cpp_python-0.1.9/vendor/llama.cpp/.devops/tools.sh`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/.github/ISSUE_TEMPLATE/custom.md` & `llama_cpp_python-0.1.9/vendor/llama.cpp/.github/ISSUE_TEMPLATE/custom.md`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/.github/workflows/build.yml` & `llama_cpp_python-0.1.9/vendor/llama.cpp/.github/workflows/build.yml`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/.github/workflows/docker.yml` & `llama_cpp_python-0.1.9/vendor/llama.cpp/.github/workflows/docker.yml`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/CMakeLists.txt` & `llama_cpp_python-0.1.9/vendor/llama.cpp/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/LICENSE` & `llama_cpp_python-0.1.9/vendor/llama.cpp/LICENSE`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/Makefile` & `llama_cpp_python-0.1.9/vendor/llama.cpp/Makefile`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/README.md` & `llama_cpp_python-0.1.9/vendor/llama.cpp/README.md`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/SHA256SUMS` & `llama_cpp_python-0.1.9/vendor/llama.cpp/SHA256SUMS`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/convert-gptq-to-ggml.py` & `llama_cpp_python-0.1.9/vendor/llama.cpp/convert-gptq-to-ggml.py`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/convert-pth-to-ggml.py` & `llama_cpp_python-0.1.9/vendor/llama.cpp/convert-pth-to-ggml.py`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/flake.lock` & `llama_cpp_python-0.1.9/vendor/llama.cpp/flake.lock`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/flake.nix` & `llama_cpp_python-0.1.9/vendor/llama.cpp/flake.nix`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/ggml.c` & `llama_cpp_python-0.1.9/vendor/llama.cpp/ggml.c`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/ggml.h` & `llama_cpp_python-0.1.9/vendor/llama.cpp/ggml.h`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/llama.cpp` & `llama_cpp_python-0.1.9/vendor/llama.cpp/llama.cpp`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/llama.h` & `llama_cpp_python-0.1.9/vendor/llama.cpp/llama.h`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/models/ggml-vocab.bin` & `llama_cpp_python-0.1.9/vendor/llama.cpp/models/ggml-vocab.bin`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/quantize.py` & `llama_cpp_python-0.1.9/vendor/llama.cpp/quantize.py`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/tests/test-quantize.c` & `llama_cpp_python-0.1.9/vendor/llama.cpp/tests/test-quantize.c`

 * *Files identical despite different names*

### Comparing `llama_cpp_python-0.1.8/vendor/llama.cpp/tests/test-tokenizer-0.cpp` & `llama_cpp_python-0.1.9/vendor/llama.cpp/tests/test-tokenizer-0.cpp`

 * *Files identical despite different names*

