# Comparing `tmp/llvmlite-0.8.0.tar.gz` & `tmp/llvmlite-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/llvmlite-0.8.0.tar", last modified: Fri Oct 23 21:31:22 2015, max compression
+gzip compressed data, was "dist/llvmlite-0.9.0.tar", last modified: Mon Feb 29 16:58:57 2016, max compression
```

## Comparing `llvmlite-0.8.0.tar` & `llvmlite-0.9.0.tar`

### file list

```diff
@@ -1,79 +1,93 @@
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/examples/
--rw-r--r--   0 sklam      (502) staff       (20)      324 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/floatrep.py
--rw-r--r--   0 sklam      (502) staff       (20)      613 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/ir_fpadd.py
--rw-r--r--   0 sklam      (502) staff       (20)     1778 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/ll_fpadd.py
--rw-r--r--   0 sklam      (502) staff       (20)      870 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/llvmir.py
--rw-r--r--   0 sklam      (502) staff       (20)      838 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/parseasm.py
--rw-r--r--   0 sklam      (502) staff       (20)     2316 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/sum.py
--rw-r--r--   0 sklam      (502) staff       (20)      283 2015-10-23 21:31:03.000000 llvmlite-0.8.0/examples/test.ll
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/ffi/
--rw-r--r--   0 sklam      (502) staff       (20)      828 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/assembly.cpp
--rw-r--r--   0 sklam      (502) staff       (20)      927 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/bitcode.cpp
--rwxr-xr-x   0 sklam      (502) staff       (20)     3696 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/build.py
--rw-r--r--   0 sklam      (502) staff       (20)     1002 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/CMakeLists.txt
--rw-r--r--   0 sklam      (502) staff       (20)      762 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/core.cpp
--rw-r--r--   0 sklam      (502) staff       (20)      634 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/core.h
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/ffi/dummy/
--rw-r--r--   0 sklam      (502) staff       (20)       70 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/dummy/CMakeLists.txt
--rw-r--r--   0 sklam      (502) staff       (20)      694 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/dylib.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     6541 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/executionengine.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     1318 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/initfini.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     1187 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/linker.cpp
--rw-r--r--   0 sklam      (502) staff       (20)      516 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/Makefile.freebsd
--rw-r--r--   0 sklam      (502) staff       (20)      751 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/Makefile.linux
--rw-r--r--   0 sklam      (502) staff       (20)      535 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/Makefile.osx
--rw-r--r--   0 sklam      (502) staff       (20)     4730 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/module.cpp
--rw-r--r--   0 sklam      (502) staff       (20)      975 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/passmanagers.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     7655 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/targets.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     3873 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/transforms.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     1591 2015-10-23 21:31:03.000000 llvmlite-0.8.0/ffi/value.cpp
--rw-r--r--   0 sklam      (502) staff       (20)     1298 2015-10-23 21:31:03.000000 llvmlite-0.8.0/LICENSE
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/
--rw-r--r--   0 sklam      (502) staff       (20)      308 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/__init__.py
--rw-r--r--   0 sklam      (502) staff       (20)      417 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/_version.py
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/binding/
--rw-r--r--   0 sklam      (502) staff       (20)      340 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/__init__.py
--rw-r--r--   0 sklam      (502) staff       (20)      985 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/common.py
--rw-r--r--   0 sklam      (502) staff       (20)     1322 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/dylib.py
--rwxr-xr-x   0 sklam      (502) staff       (20)    10398 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/executionengine.py
--rw-r--r--   0 sklam      (502) staff       (20)     4686 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/ffi.py
--rw-r--r--   0 sklam      (502) staff       (20)      866 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/initfini.py
--rw-r--r--   0 sklam      (502) staff       (20)      514 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/linker.py
--rw-r--r--   0 sklam      (502) staff       (20)     8878 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/module.py
--rw-r--r--   0 sklam      (502) staff       (20)      291 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/options.py
--rw-r--r--   0 sklam      (502) staff       (20)     2456 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/passmanagers.py
--rw-r--r--   0 sklam      (502) staff       (20)    12503 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/targets.py
--rw-r--r--   0 sklam      (502) staff       (20)     4706 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/transforms.py
--rw-r--r--   0 sklam      (502) staff       (20)     4770 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/binding/value.py
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/ir/
--rw-r--r--   0 sklam      (502) staff       (20)      258 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/__init__.py
--rw-r--r--   0 sklam      (502) staff       (20)      973 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/_utils.py
--rw-r--r--   0 sklam      (502) staff       (20)    16516 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/builder.py
--rw-r--r--   0 sklam      (502) staff       (20)      553 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/context.py
--rw-r--r--   0 sklam      (502) staff       (20)    21771 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/instructions.py
--rw-r--r--   0 sklam      (502) staff       (20)     4715 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/module.py
--rw-r--r--   0 sklam      (502) staff       (20)     1542 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/transforms.py
--rw-r--r--   0 sklam      (502) staff       (20)    10403 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/types.py
--rw-r--r--   0 sklam      (502) staff       (20)    15671 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/ir/values.py
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/llvmpy/
--rw-r--r--   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/llvmpy/__init__.py
--rw-r--r--   0 sklam      (502) staff       (20)       43 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/llvmpy/avx_support.py
--rw-r--r--   0 sklam      (502) staff       (20)     6228 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/llvmpy/core.py
--rw-r--r--   0 sklam      (502) staff       (20)     2494 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/llvmpy/ee.py
--rw-r--r--   0 sklam      (502) staff       (20)     2634 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/llvmpy/passes.py
--rw-r--r--   0 sklam      (502) staff       (20)    27760 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/six.py
-drwxr-xr-x   0 sklam      (502) staff       (20)        0 2015-10-23 21:31:22.000000 llvmlite-0.8.0/llvmlite/tests/
--rw-r--r--   0 sklam      (502) staff       (20)     1632 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/__init__.py
--rw-r--r--   0 sklam      (502) staff       (20)       27 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/__main__.py
--rw-r--r--   0 sklam      (502) staff       (20)    13105 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/customize.py
--rw-r--r--   0 sklam      (502) staff       (20)    27640 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/test_binding.py
--rw-r--r--   0 sklam      (502) staff       (20)    48953 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/test_ir.py
--rw-r--r--   0 sklam      (502) staff       (20)     1573 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/tests/test_valuerepr.py
--rw-r--r--   0 sklam      (502) staff       (20)      710 2015-10-23 21:31:03.000000 llvmlite-0.8.0/llvmlite/utils.py
--rw-r--r--   0 sklam      (502) staff       (20)      817 2015-10-23 21:31:22.000000 llvmlite-0.8.0/PKG-INFO
--rw-r--r--   0 sklam      (502) staff       (20)     2575 2015-10-23 21:31:03.000000 llvmlite-0.8.0/README.rst
--rw-r--r--   0 sklam      (502) staff       (20)      977 2015-10-23 21:31:03.000000 llvmlite-0.8.0/run_coverage.py
--rw-r--r--   0 sklam      (502) staff       (20)      107 2015-10-23 21:31:03.000000 llvmlite-0.8.0/runtests.py
--rw-r--r--   0 sklam      (502) staff       (20)     3756 2015-10-23 21:31:03.000000 llvmlite-0.8.0/setup.py
--rw-r--r--   0 sklam      (502) staff       (20)    40346 2015-10-23 21:31:03.000000 llvmlite-0.8.0/versioneer.py
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/ir/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    11594 2016-02-16 20:32:05.000000 llvmlite-0.9.0/llvmlite/ir/types.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      553 2014-10-20 09:24:09.000000 llvmlite-0.9.0/llvmlite/ir/context.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    23255 2016-02-16 20:26:11.000000 llvmlite-0.9.0/llvmlite/ir/builder.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1542 2014-11-05 00:08:47.000000 llvmlite-0.9.0/llvmlite/ir/transforms.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      258 2015-01-05 15:38:44.000000 llvmlite-0.9.0/llvmlite/ir/__init__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1536 2016-02-08 21:39:29.000000 llvmlite-0.9.0/llvmlite/ir/_utils.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     4929 2016-02-16 20:28:53.000000 llvmlite-0.9.0/llvmlite/ir/module.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    21837 2016-02-08 21:43:49.000000 llvmlite-0.9.0/llvmlite/ir/instructions.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    16187 2016-02-16 20:40:17.000000 llvmlite-0.9.0/llvmlite/ir/values.py
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/tests/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)       27 2014-10-27 15:24:05.000000 llvmlite-0.9.0/llvmlite/tests/__main__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    51450 2016-02-08 19:06:03.000000 llvmlite-0.9.0/llvmlite/tests/test_ir.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    13105 2014-10-20 17:57:02.000000 llvmlite-0.9.0/llvmlite/tests/customize.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1573 2015-01-22 14:07:57.000000 llvmlite-0.9.0/llvmlite/tests/test_valuerepr.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1632 2014-10-28 18:08:02.000000 llvmlite-0.9.0/llvmlite/tests/__init__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    27834 2016-02-29 16:53:22.000000 llvmlite-0.9.0/llvmlite/tests/test_binding.py
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/llvmpy/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     6228 2015-03-17 12:44:29.000000 llvmlite-0.9.0/llvmlite/llvmpy/core.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     2634 2014-12-11 16:20:31.000000 llvmlite-0.9.0/llvmlite/llvmpy/passes.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)        0 2014-10-20 09:24:09.000000 llvmlite-0.9.0/llvmlite/llvmpy/__init__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     2494 2014-11-25 15:09:30.000000 llvmlite-0.9.0/llvmlite/llvmpy/ee.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)       43 2014-10-20 09:24:09.000000 llvmlite-0.9.0/llvmlite/llvmpy/avx_support.py
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/binding/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1322 2015-02-23 11:53:22.000000 llvmlite-0.9.0/llvmlite/binding/dylib.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      478 2016-02-16 19:42:07.000000 llvmlite-0.9.0/llvmlite/binding/options.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     2612 2016-02-16 19:43:48.000000 llvmlite-0.9.0/llvmlite/binding/passmanagers.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      866 2015-02-23 11:53:22.000000 llvmlite-0.9.0/llvmlite/binding/initfini.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     5395 2016-02-16 19:46:00.000000 llvmlite-0.9.0/llvmlite/binding/transforms.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     4883 2016-02-16 19:51:36.000000 llvmlite-0.9.0/llvmlite/binding/value.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      985 2015-06-04 14:09:39.000000 llvmlite-0.9.0/llvmlite/binding/common.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    12805 2016-02-29 16:53:22.000000 llvmlite-0.9.0/llvmlite/binding/targets.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      514 2014-10-21 09:48:45.000000 llvmlite-0.9.0/llvmlite/binding/linker.py
+-rwxrwxr-x   0 antoine   (1000) antoine   (1000)    10732 2016-02-16 19:32:27.000000 llvmlite-0.9.0/llvmlite/binding/executionengine.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      340 2014-11-06 15:29:20.000000 llvmlite-0.9.0/llvmlite/binding/__init__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     8878 2015-08-20 16:10:36.000000 llvmlite-0.9.0/llvmlite/binding/module.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     4686 2015-09-28 13:23:22.000000 llvmlite-0.9.0/llvmlite/binding/ffi.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      710 2014-11-25 11:34:23.000000 llvmlite-0.9.0/llvmlite/utils.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      308 2015-02-23 11:53:22.000000 llvmlite-0.9.0/llvmlite/__init__.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    27760 2014-10-20 17:45:09.000000 llvmlite-0.9.0/llvmlite/six.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      417 2016-02-29 16:58:57.000000 llvmlite-0.9.0/llvmlite/_version.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     2678 2016-02-08 16:18:44.000000 llvmlite-0.9.0/README.rst
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      817 2016-02-29 16:58:57.000000 llvmlite-0.9.0/PKG-INFO
+-rw-r--r--   0 antoine   (1000) antoine   (1000)     1298 2014-10-23 12:29:39.000000 llvmlite-0.9.0/LICENSE
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     3756 2015-06-04 14:09:39.000000 llvmlite-0.9.0/setup.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      977 2014-10-20 18:58:48.000000 llvmlite-0.9.0/run_coverage.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)    40346 2015-06-04 14:09:39.000000 llvmlite-0.9.0/versioneer.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      107 2014-10-20 17:42:31.000000 llvmlite-0.9.0/runtests.py
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     6541 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/executionengine.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1187 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/linker.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      975 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/passmanagers.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      828 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/assembly.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      927 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/bitcode.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     7617 2016-02-29 16:53:22.000000 llvmlite-0.9.0/ffi/targets.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1318 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/initfini.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      446 2016-01-26 14:11:43.000000 llvmlite-0.9.0/ffi/Makefile.osx
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/build/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/build/CMakeFiles/
+-rwxr--r--   0 antoine   (1000) antoine   (1000)      144 2016-01-26 10:56:45.000000 llvmlite-0.9.0/ffi/build/CMakeFiles/TargetDirectories.txt
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/build/CMakeFiles/3.0.2/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/build/CMakeFiles/3.0.2/CompilerIdCXX/
+-rwxr--r--   0 antoine   (1000) antoine   (1000)    13731 2016-01-26 10:50:30.000000 llvmlite-0.9.0/ffi/build/CMakeFiles/3.0.2/CompilerIdCXX/CMakeCXXCompilerId.cpp
+-rwxr--r--   0 antoine   (1000) antoine   (1000)    13680 2016-01-26 10:56:24.000000 llvmlite-0.9.0/ffi/build/CMakeCache.txt
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1591 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/value.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     4730 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/module.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      694 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/dylib.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      427 2016-01-26 14:11:43.000000 llvmlite-0.9.0/ffi/Makefile.freebsd
+-rwxrwxr-x   0 antoine   (1000) antoine   (1000)     1002 2016-01-26 14:11:43.000000 llvmlite-0.9.0/ffi/CMakeLists.txt
+-rwxrwxr-x   0 antoine   (1000) antoine   (1000)     4920 2016-01-26 14:11:43.000000 llvmlite-0.9.0/ffi/build.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      762 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/core.cpp
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     3874 2016-02-16 13:15:49.000000 llvmlite-0.9.0/ffi/transforms.cpp
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/dummy/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/dummy/build/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeFiles/
+-rwxr--r--   0 antoine   (1000) antoine   (1000)      109 2014-10-27 17:28:24.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeFiles/TargetDirectories.txt
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeFiles/3.0.2/
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeFiles/3.0.2/CompilerIdCXX/
+-rwxr--r--   0 antoine   (1000) antoine   (1000)    13731 2014-10-27 17:28:17.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeFiles/3.0.2/CompilerIdCXX/CMakeCXXCompilerId.cpp
+-rwxr--r--   0 antoine   (1000) antoine   (1000)    12088 2014-10-27 17:28:24.000000 llvmlite-0.9.0/ffi/dummy/build/CMakeCache.txt
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)       70 2014-10-27 17:41:57.000000 llvmlite-0.9.0/ffi/dummy/CMakeLists.txt
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      634 2016-01-18 13:24:14.000000 llvmlite-0.9.0/ffi/core.h
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      765 2016-01-26 14:11:43.000000 llvmlite-0.9.0/ffi/Makefile.linux
+drwxrwxr-x   0 antoine   (1000) antoine   (1000)        0 2016-02-29 16:58:57.000000 llvmlite-0.9.0/examples/
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     2316 2015-08-17 11:44:16.000000 llvmlite-0.9.0/examples/sum.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      613 2015-06-04 14:09:39.000000 llvmlite-0.9.0/examples/ir_fpadd.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      870 2014-10-20 09:24:09.000000 llvmlite-0.9.0/examples/llvmir.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      324 2014-10-20 09:24:09.000000 llvmlite-0.9.0/examples/floatrep.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)     1778 2016-02-16 19:41:43.000000 llvmlite-0.9.0/examples/ll_fpadd.py
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      283 2014-10-20 09:24:09.000000 llvmlite-0.9.0/examples/test.ll
+-rw-rw-r--   0 antoine   (1000) antoine   (1000)      838 2015-08-17 11:44:16.000000 llvmlite-0.9.0/examples/parseasm.py
```

### Comparing `llvmlite-0.8.0/examples/ir_fpadd.py` & `llvmlite-0.9.0/examples/ir_fpadd.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/examples/ll_fpadd.py` & `llvmlite-0.9.0/examples/ll_fpadd.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/examples/llvmir.py` & `llvmlite-0.9.0/examples/llvmir.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/examples/parseasm.py` & `llvmlite-0.9.0/examples/parseasm.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/examples/sum.py` & `llvmlite-0.9.0/examples/sum.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/assembly.cpp` & `llvmlite-0.9.0/ffi/assembly.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/bitcode.cpp` & `llvmlite-0.9.0/ffi/bitcode.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/build.py` & `llvmlite-0.9.0/ffi/build.py`

 * *Files 27% similar despite different names*

```diff
@@ -25,25 +25,39 @@
     try:
         os.chdir(build_dir)
         subprocess.check_call(['cmake', '-G', generator, cmake_dir])
     finally:
         os.chdir(old_dir)
 
 
+def run_llvm_config(llvm_config, args):
+    cmd = [llvm_config] + args
+    p = subprocess.Popen(cmd,
+                         stdout=subprocess.PIPE,
+                         stderr=subprocess.PIPE)
+    out, err = p.communicate()
+    out = out.decode()
+    err = err.decode()
+    rc = p.wait()
+    if rc != 0:
+        raise RuntimeError("Command %s returned with code %d; stderr follows:\n%s\n"
+                           % (cmd, rc, err))
+    return out
+
+
 def find_win32_generator():
     """
     Find a suitable cmake "generator" under Windows.
     """
     # XXX this assumes we will find a generator that's the same, or
     # compatible with, the one which was used to compile LLVM... cmake
     # seems a bit lacking here.
     cmake_dir = os.path.join(here_dir, 'dummy')
-    # LLVM 3.5 needs VS 2012 minimum.
-    for generator in ['Visual Studio 12 2013',
-                      'Visual Studio 11 2012']:
+    # LLVM 3.7 needs VS 2013 minimum.
+    for generator in ['Visual Studio 12 2013']:
         if is_64bit:
             generator += ' Win64'
         build_dir = tempfile.mkdtemp()
         print("Trying generator %r" % (generator,))
         try:
             try_cmake(cmake_dir, build_dir, generator)
         except subprocess.CalledProcessError:
@@ -57,14 +71,15 @@
 
 
 def main_win32():
     generator = find_win32_generator()
     config = 'Release'
     if not os.path.exists(build_dir):
         os.mkdir(build_dir)
+    # Run configuration step
     try_cmake(here_dir, build_dir, generator)
     subprocess.check_call(['cmake', '--build', build_dir, '--config', config])
     shutil.copy(os.path.join(build_dir, config, 'llvmlite.dll'), target_dir)
     # Copy CRT libraries as well, so as to package them.
     if os.environ.get('PROCESSOR_ARCHITEW6432'):
         # Hard-code WoW64 path if we're a 32-bit Python in a 64-bit system,
         # otherwise the wrong DLL file will be found by find_library().
@@ -88,14 +103,32 @@
     sys.stdout.flush()
     try:
         subprocess.check_call([llvm_config, '--version'])
     except (OSError, subprocess.CalledProcessError):
         raise RuntimeError("%s failed executing, please point LLVM_CONFIG "
                            "to the path for llvm-config" % (llvm_config,))
 
+    # Get LLVM information for building
+    # Note we can't use "--libs all" anymore:
+    # https://llvm.org/bugs/show_bug.cgi?id=25088
+    # https://llvm.org/bugs/show_bug.cgi?id=25089
+    libs = run_llvm_config(llvm_config,
+                           "--system-libs --libs engine bitreader "
+                           "bitwriter instrumentation lto irreader "
+                           "asmprinter".split())
+    # Normalize whitespace (trim newlines)
+    os.environ['LLVM_LIBS'] = ' '.join(libs.split())
+
+    cxxflags = run_llvm_config(llvm_config, ["--cxxflags"])
+    cxxflags = cxxflags.split() + ['-fno-rtti', '-g']
+    os.environ['LLVM_CXXFLAGS'] = ' '.join(cxxflags)
+
+    ldflags = run_llvm_config(llvm_config, ["--ldflags"])
+    os.environ['LLVM_LDFLAGS'] = ldflags.strip()
+
     makefile = "Makefile.%s" % (kind,)
     subprocess.check_call(['make', '-f', makefile])
     shutil.copy('libllvmlite' + library_ext, target_dir)
 
 
 def main():
     if sys.platform == 'win32':
```

### Comparing `llvmlite-0.8.0/ffi/CMakeLists.txt` & `llvmlite-0.9.0/ffi/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/core.cpp` & `llvmlite-0.9.0/ffi/core.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/core.h` & `llvmlite-0.9.0/ffi/core.h`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/dylib.cpp` & `llvmlite-0.9.0/ffi/dylib.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/executionengine.cpp` & `llvmlite-0.9.0/ffi/executionengine.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/initfini.cpp` & `llvmlite-0.9.0/ffi/initfini.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/linker.cpp` & `llvmlite-0.9.0/ffi/linker.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/module.cpp` & `llvmlite-0.9.0/ffi/module.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/passmanagers.cpp` & `llvmlite-0.9.0/ffi/passmanagers.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/ffi/targets.cpp` & `llvmlite-0.9.0/ffi/targets.cpp`

 * *Files 7% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 #include "core.h"
 #include "llvm-c/Target.h"
 #include "llvm/Support/Host.h"
 #include "llvm-c/TargetMachine.h"
 #include "llvm/Target/TargetMachine.h"
 #include "llvm/IR/LegacyPassManager.h"
-#include "llvm/Target/TargetLibraryInfo.h"
+#include "llvm/Analysis/TargetLibraryInfo.h"
 #include "llvm/ADT/Triple.h"
 #include "llvm/Support/TargetRegistry.h"
 #include "llvm/IR/Type.h"
 
 #include <cstdio>
 #include <cstring>
+#include <sstream>
 
 
 namespace llvm {
 
 
 inline LLVMTargetLibraryInfoRef wrap(TargetLibraryInfo *TLI) {
     return reinterpret_cast<LLVMTargetLibraryInfoRef>(TLI);
@@ -33,16 +34,40 @@
 }
 
 }
 
 extern "C" {
 
 API_EXPORT(void)
+LLVMPY_GetProcessTriple(const char **Out) {
+    *Out = LLVMPY_CreateString(llvm::sys::getProcessTriple().c_str());
+}
+
+/**
+ * Output the feature string to the output argument.
+ * Features are prefixed with '+' or '-' for enabled or disabled, respectively.
+ * Features are separated by ','.
+ */
+API_EXPORT(void)
+LLVMPY_GetHostCPUFeatures(const char **Out){
+    llvm::StringMap<bool> features;
+    std::ostringstream buf;
+    if ( llvm::sys::getHostCPUFeatures(features) ) {
+        for (auto &F : features) {
+            if (buf.tellp()){
+                buf << ',';
+            }
+            buf << ((F.second? "+": "-") + F.first()).str();
+        }
+    }
+    *Out = LLVMPY_CreateString(buf.str().c_str());
+}
+
+API_EXPORT(void)
 LLVMPY_GetDefaultTargetTriple(const char **Out) {
-    // Should we use getProcessTriple() instead?
     *Out = LLVMPY_CreateString(llvm::sys::getDefaultTargetTriple().c_str());
 }
 
 API_EXPORT(void)
 LLVMPY_GetHostCPUName(const char **Out) {
     *Out = LLVMPY_CreateString(llvm::sys::getHostCPUName().data());
 }
@@ -191,15 +216,15 @@
         rm = Reloc::PIC_;
     else if (rms == "dynamicnopic")
         rm = Reloc::DynamicNoPIC;
     else
         rm = Reloc::Default;
 
     TargetOptions opt;
-    opt.JITEmitDebugInfo = EmitJITDebug;
+//     opt.JITEmitDebugInfo = EmitJITDebug;
     opt.PrintMachineCode = PrintMC;
 
     return wrap(unwrap(T)->createTargetMachine(Triple, CPU, Features, opt,
                                                rm, cm, cgol));
 }
 
 
@@ -272,57 +297,20 @@
 
 API_EXPORT(void)
 LLVMPY_DisposeMemoryBuffer(LLVMMemoryBufferRef MB)
 {
     return LLVMDisposeMemoryBuffer(MB);
 }
 
+/*
 
-API_EXPORT(LLVMTargetLibraryInfoRef)
-LLVMPY_CreateTargetLibraryInfo(const char *Triple)
-{
-    return llvm::wrap(new llvm::TargetLibraryInfo(llvm::Triple(Triple)));
-}
+If needed:
 
-API_EXPORT(void)
-LLVMPY_DisposeTargetLibraryInfo(LLVMTargetLibraryInfoRef TLI)
-{
-    delete llvm::unwrap(TLI);
-}
+explicit TargetLibraryInfoWrapperPass(const Triple &T);
 
-API_EXPORT(void)
-LLVMPY_AddTargetLibraryInfo(
-    LLVMTargetLibraryInfoRef TLI,
-    LLVMPassManagerRef PM
-    )
-{
-    LLVMAddTargetLibraryInfo(TLI, PM);
+void LLVMAddTargetLibraryInfo(LLVMTargetLibraryInfoRef TLI,
+                              LLVMPassManagerRef PM) {
+  unwrap(PM)->add(new TargetLibraryInfoWrapperPass(*unwrap(TLI)));
 }
-
-API_EXPORT(void)
-LLVMPY_DisableAllBuiltins(LLVMTargetLibraryInfoRef TLI)
-{
-    llvm::unwrap(TLI)->disableAllFunctions();
-}
-
-API_EXPORT(int)
-LLVMPY_GetLibFunc(LLVMTargetLibraryInfoRef TLI, const char *Name, int *OutF)
-{
-    llvm::LibFunc::Func F;
-    if (llvm::unwrap(TLI)->getLibFunc(Name, F)) {
-        /* Ok */
-        *OutF = F;
-        return 1;
-    } else {
-        /* Failed */
-        return 0;
-    }
-}
-
-API_EXPORT(void)
-LLVMPY_SetUnavailableLibFunc(LLVMTargetLibraryInfoRef TLI, int F)
-{
-    llvm::unwrap(TLI)->setUnavailable((llvm::LibFunc::Func)F);
-}
-
+*/
 
 } // end extern "C"
```

### Comparing `llvmlite-0.8.0/ffi/transforms.cpp` & `llvmlite-0.9.0/ffi/transforms.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -8,18 +8,18 @@
 
 namespace llvm {
     inline PassManagerBuilder *unwrap(LLVMPassManagerBuilderRef P) {
         return reinterpret_cast<PassManagerBuilder*>(P);
     }
 
     inline LLVMPassManagerBuilderRef wrap(PassManagerBuilder *P) {
-      return reinterpret_cast<LLVMPassManagerBuilderRef>(P);
+        return reinterpret_cast<LLVMPassManagerBuilderRef>(P);
     }
+}
 
-};
 
 API_EXPORT(LLVMPassManagerBuilderRef)
 LLVMPY_PassManagerBuilderCreate()
 {
     return LLVMPassManagerBuilderCreate();
 }
```

### Comparing `llvmlite-0.8.0/ffi/value.cpp` & `llvmlite-0.9.0/ffi/value.cpp`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/LICENSE` & `llvmlite-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/common.py` & `llvmlite-0.9.0/llvmlite/binding/common.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/dylib.py` & `llvmlite-0.9.0/llvmlite/binding/dylib.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/executionengine.py` & `llvmlite-0.9.0/llvmlite/binding/executionengine.py`

 * *Files 4% similar despite different names*

```diff
@@ -63,20 +63,26 @@
                       ".get_function_address() instead.", DeprecationWarning)
         ptr = ffi.lib.LLVMPY_GetPointerToGlobal(self, gv)
         if ptr is None:
             raise ValueError("Cannot find given global value %r" % (gv.name))
         return ptr
 
     def get_function_address(self, name):
+        """
+        Return the address of the function named *name* as an integer.
+        """
         ptr = ffi.lib.LLVMPY_GetFunctionAddress(self, name.encode("ascii"))
         if ptr is None:
             raise ValueError("Cannot find given function %s" % name)
         return ptr
 
     def get_global_value_address(self, name):
+        """
+        Return the address of the global value named *name* as an integer.
+        """
         ptr = ffi.lib.LLVMPY_GetGlobalValueAddress(self, name.encode("ascii"))
         if ptr is None:
             raise ValueError("Cannot find given global value %s" % name)
         return ptr
 
     def add_global_mapping(self, gv, addr):
         # XXX unused?
@@ -89,14 +95,18 @@
         if module in self._modules:
             raise KeyError("module already added to this engine")
         ffi.lib.LLVMPY_AddModule(self, module)
         module._owned = True
         self._modules.add(module)
 
     def finalize_object(self):
+        """
+        Make sure all modules owned by the execution engine are fully processed
+        and "usable" for execution.
+        """
         ffi.lib.LLVMPY_FinalizeObject(self)
 
     def remove_module(self, module):
         """
         Ownership of module is returned
         """
         with ffi.OutputString() as outerr:
```

### Comparing `llvmlite-0.8.0/llvmlite/binding/ffi.py` & `llvmlite-0.9.0/llvmlite/binding/ffi.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/initfini.py` & `llvmlite-0.9.0/llvmlite/binding/initfini.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/linker.py` & `llvmlite-0.9.0/llvmlite/binding/linker.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/module.py` & `llvmlite-0.9.0/llvmlite/binding/module.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/binding/passmanagers.py` & `llvmlite-0.9.0/llvmlite/binding/passmanagers.py`

 * *Files 12% similar despite different names*

```diff
@@ -23,14 +23,17 @@
 
     def __init__(self, ptr=None):
         if ptr is None:
             ptr = ffi.lib.LLVMPY_CreatePassManager()
         PassManager.__init__(self, ptr)
 
     def run(self, module):
+        """
+        Run optimization passes on the given module.
+        """
         return ffi.lib.LLVMPY_RunPassManager(self, module)
 
 
 class FunctionPassManager(PassManager):
 
     def __init__(self, module):
         ptr = ffi.lib.LLVMPY_CreateFunctionPassManager(module)
@@ -49,14 +52,17 @@
         """
         Finalize the FunctionPassManager.  Returns True if it produced
         any changes (?).
         """
         return ffi.lib.LLVMPY_FinalizeFunctionPassManager(self)
 
     def run(self, function):
+        """
+        Run optimization passes on the given function.
+        """
         return ffi.lib.LLVMPY_RunFunctionPassManager(self, function)
 
 
 # ============================================================================
 # FFI
 
 ffi.lib.LLVMPY_CreatePassManager.restype = ffi.LLVMPassManagerRef
```

### Comparing `llvmlite-0.8.0/llvmlite/binding/targets.py` & `llvmlite-0.9.0/llvmlite/binding/targets.py`

 * *Files 16% similar despite different names*

```diff
@@ -2,18 +2,71 @@
 
 import collections
 import os
 from ctypes import (POINTER, c_char_p, c_longlong, c_int, c_size_t,
                     c_void_p, string_at, byref)
 
 from . import ffi
-from .module import parse_assembly
 from .common import _decode_string, _encode_string
 
 
+def get_process_triple():
+    """
+    Return a target triple suitable for generating code for the current process.
+    An example when the default triple from ``get_default_triple()`` is not be
+    suitable is when LLVM is compiled for 32-bit but the process is executing
+    in 64-bit mode.
+    """
+    with ffi.OutputString() as out:
+        ffi.lib.LLVMPY_GetProcessTriple(out)
+        return str(out)
+
+
+class FeatureMap(dict):
+    """
+    Maps feature name to a boolean indicating the availability of the feature.
+    Extends ``dict`` to add `.flatten()` method.
+    """
+    def flatten(self, sort=True):
+        """
+        Args
+        ----
+        sort: bool
+            Optional.  If True, the features are sorted by name; otherwise,
+            the ordering is unstable between python session due to hash
+            randomization.  Defaults to True.
+
+        Returns a string suitable for use as the ``features`` argument to
+        ``Target.create_target_machine()``.
+
+        """
+        iterator = sorted(self.items()) if sort else iter(self.items())
+        flag_map = {True: '+', False: '-'}
+        return ','.join('{0}{1}'.format(flag_map[v], k)
+                        for k, v in iterator)
+
+
+def get_host_cpu_features():
+    """
+    Returns a dictionary-like object indicating the CPU features for current
+    architecture and whether they are enabled for this CPU.  The key-value pairs
+    are the feature name as string and a boolean indicating whether the feature
+    is available.  The returned value is an instance of ``FeatureMap`` class,
+    which adds a new method ``.flatten()`` for returning a string suitable for
+    use as the "features" argument to ``Target.create_target_machine()``.
+    """
+    with ffi.OutputString() as out:
+        ffi.lib.LLVMPY_GetHostCPUFeatures(out)
+        outdict = FeatureMap()
+        flag_map = {'+': True, '-': False}
+        for feat in str(out).split(','):
+            outdict[feat[1:]] = flag_map[feat[0]]
+        return outdict
+
+
 def get_default_triple():
     """
     Return the default target triple LLVM is configured to produce code for.
     """
     with ffi.OutputString() as out:
         ffi.lib.LLVMPY_GetDefaultTargetTriple(out)
         return str(out)
@@ -41,16 +94,19 @@
     """
     if triple is None:
         triple = get_default_triple()
     res = ffi.lib.LLVMPY_GetTripleObjectFormat(_encode_string(triple))
     return _object_formats[res]
 
 
-def create_target_data(strrep):
-    return TargetData(ffi.lib.LLVMPY_CreateTargetData(_encode_string(strrep)))
+def create_target_data(layout):
+    """
+    Create a TargetData instance for the given *layout* string.
+    """
+    return TargetData(ffi.lib.LLVMPY_CreateTargetData(_encode_string(layout)))
 
 
 class TargetData(ffi.ObjectRef):
     """
     A TargetData provides structured access to a data layout.
     Use :func:`create_target_data` to create instances.
     """
@@ -107,19 +163,25 @@
     _triple = ''
 
     # No _dispose() method since LLVMGetTargetFromTriple() returns a
     # persistent object.
 
     @classmethod
     def from_default_triple(cls):
+        """
+        Create a Target instance for the default triple.
+        """
         triple = get_default_triple()
         return cls.from_triple(triple)
 
     @classmethod
     def from_triple(cls, triple):
+        """
+        Create a Target instance for the given triple (a string).
+        """
         with ffi.OutputString() as outerr:
             target = ffi.lib.LLVMPY_GetTargetFromTriple(triple.encode('utf8'),
                                                         outerr)
             if not target:
                 raise RuntimeError(str(outerr))
             target = cls(target)
             target._triple = triple
@@ -141,14 +203,17 @@
 
     def __str__(self):
         return "<Target {0} ({1})>".format(self.name, self.description)
 
     def create_target_machine(self, cpu='', features='',
                               opt=2, reloc='default', codemodel='jitdefault',
                               jitdebug=False, printmc=False):
+        """
+        Create a new TargetMachine for this target and the given options.
+        """
         assert 0 <= opt <= 3
         assert reloc in RELOC
         assert codemodel in CODEMODEL
         triple = self._triple
         # MCJIT under Windows only supports ELF objects, see
         # http://lists.llvm.org/pipermail/llvm-dev/2013-December/068341.html
         # Note we still want to produce regular COFF files in AOT mode.
@@ -227,65 +292,21 @@
     @property
     def triple(self):
         with ffi.OutputString() as out:
             ffi.lib.LLVMPY_GetTargetMachineTriple(self, out)
             return str(out)
 
 
-def create_target_library_info(triple):
-    return TargetLibraryInfo(
-        ffi.lib.LLVMPY_CreateTargetLibraryInfo(_encode_string(triple, ))
-    )
-
-
-class TargetLibraryInfo(ffi.ObjectRef):
-    """
-    A LLVM TargetLibraryInfo.  Use :func:`create_target_library_info`
-    to create instances.
-    """
-
-    def _dispose(self):
-        self._capi.LLVMPY_DisposeTargetLibraryInfo(self)
-
-    def add_pass(self, pm):
-        """
-        Add this library info as a pass to PassManager *pm*.
-        """
-        ffi.lib.LLVMPY_AddTargetLibraryInfo(self, pm)
-        # Once added to a PassManager, we can never get it back.
-        self._owned = True
-
-    def disable_all(self):
-        """
-        Disable all "builtin" functions.
-        """
-        ffi.lib.LLVMPY_DisableAllBuiltins(self)
-
-    def get_libfunc(self, name):
-        """
-        Get the library function *name*.  NameError is raised if not found.
-        """
-        lf = c_int()
-        if not ffi.lib.LLVMPY_GetLibFunc(self, _encode_string(name),
-                                         byref(lf)):
-            raise NameError("LibFunc '{name}' not found".format(name=name))
-        return LibFunc(name=name, identity=lf.value)
-
-    def set_unavailable(self, libfunc):
-        """
-        Mark the given library function (*libfunc*) as unavailable.
-        """
-        ffi.lib.LLVMPY_SetUnavailableLibFunc(self, libfunc.identity)
-
-
-LibFunc = collections.namedtuple("LibFunc", ["identity", "name"])
-
 # ============================================================================
 # FFI
 
+ffi.lib.LLVMPY_GetProcessTriple.argtypes = [POINTER(c_char_p)]
+
+ffi.lib.LLVMPY_GetHostCPUFeatures.argtypes = [POINTER(c_char_p)]
+
 ffi.lib.LLVMPY_GetDefaultTargetTriple.argtypes = [POINTER(c_char_p)]
 
 ffi.lib.LLVMPY_GetHostCPUName.argtypes = [POINTER(c_char_p)]
 
 ffi.lib.LLVMPY_GetTripleObjectFormat.argtypes = [c_char_p]
 ffi.lib.LLVMPY_GetTripleObjectFormat.restype = c_int
 
@@ -364,39 +385,11 @@
 ffi.lib.LLVMPY_GetBufferStart.restype = c_void_p
 
 ffi.lib.LLVMPY_GetBufferSize.argtypes = [ffi.LLVMMemoryBufferRef]
 ffi.lib.LLVMPY_GetBufferSize.restype = c_size_t
 
 ffi.lib.LLVMPY_DisposeMemoryBuffer.argtypes = [ffi.LLVMMemoryBufferRef]
 
-ffi.lib.LLVMPY_CreateTargetLibraryInfo.argtypes = [c_char_p]
-ffi.lib.LLVMPY_CreateTargetLibraryInfo.restype = ffi.LLVMTargetLibraryInfoRef
-
-ffi.lib.LLVMPY_DisposeTargetLibraryInfo.argtypes = [
-    ffi.LLVMTargetLibraryInfoRef,
-]
-
-ffi.lib.LLVMPY_AddTargetLibraryInfo.argtypes = [
-    ffi.LLVMTargetLibraryInfoRef,
-    ffi.LLVMPassManagerRef,
-]
-
-ffi.lib.LLVMPY_DisableAllBuiltins.argtypes = [
-    ffi.LLVMTargetLibraryInfoRef,
-]
-
-ffi.lib.LLVMPY_GetLibFunc.argtypes = [
-    ffi.LLVMTargetLibraryInfoRef,
-    c_char_p,
-    POINTER(c_int),
-]
-ffi.lib.LLVMPY_GetLibFunc.restype = c_int
-
-ffi.lib.LLVMPY_SetUnavailableLibFunc.argtypes = [
-    ffi.LLVMTargetLibraryInfoRef,
-    c_int,
-]
-
 ffi.lib.LLVMPY_GetTargetMachineData.argtypes = [
     ffi.LLVMTargetMachineRef,
 ]
 ffi.lib.LLVMPY_GetTargetMachineData.restype = ffi.LLVMTargetDataRef
```

### Comparing `llvmlite-0.8.0/llvmlite/binding/transforms.py` & `llvmlite-0.9.0/llvmlite/binding/transforms.py`

 * *Files 10% similar despite different names*

```diff
@@ -14,30 +14,40 @@
     def __init__(self, ptr=None):
         if ptr is None:
             ptr = ffi.lib.LLVMPY_PassManagerBuilderCreate()
         ffi.ObjectRef.__init__(self, ptr)
 
     @property
     def opt_level(self):
+        """
+        The general optimization level as an integer between 0 and 3.
+        """
         return ffi.lib.LLVMPY_PassManagerBuilderGetOptLevel(self)
 
     @opt_level.setter
     def opt_level(self, level):
         ffi.lib.LLVMPY_PassManagerBuilderSetOptLevel(self, level)
 
     @property
     def size_level(self):
+        """
+        Whether and how much to optimize for size.  An integer between 0 and 2.
+        """
         return ffi.lib.LLVMPY_PassManagerBuilderGetSizeLevel(self)
 
     @size_level.setter
     def size_level(self, size):
         ffi.lib.LLVMPY_PassManagerBuilderSetSizeLevel(self, size)
 
     @property
     def inlining_threshold(self):
+        """
+        The integer threshold for inlining a function into another.  The higher,
+        the more likely inlining a function is.  This attribute is write-only.
+        """
         raise NotImplementedError("inlining_threshold is write-only")
 
     @inlining_threshold.setter
     def inlining_threshold(self, threshold):
         ffi.lib.LLVMPY_PassManagerBuilderUseInlinerWithThreshold(self, threshold)
 
     @property
@@ -46,30 +56,40 @@
 
     @disable_unit_at_a_time.setter
     def disable_unit_at_a_time(self, disable=True):
         ffi.lib.LLVMPY_PassManagerBuilderSetDisableUnitAtATime(self, disable)
 
     @property
     def disable_unroll_loops(self):
+        """
+        If true, disable loop unrolling.
+        """
         return ffi.lib.LLVMPY_PassManagerBuilderGetDisableUnrollLoops(self)
 
     @disable_unroll_loops.setter
     def disable_unroll_loops(self, disable=True):
         ffi.lib.LLVMPY_PassManagerBuilderSetDisableUnrollLoops(self, disable)
 
     @property
     def loop_vectorize(self):
+        """
+        If true, allow vectorizing loops.
+        """
         return ffi.lib.LLVMPY_PassManagerBuilderGetLoopVectorize(self)
 
     @loop_vectorize.setter
     def loop_vectorize(self, enable=True):
         return ffi.lib.LLVMPY_PassManagerBuilderSetLoopVectorize(self, enable)
 
     @property
     def slp_vectorize(self):
+        """
+        If true, enable the "SLP vectorizer", which uses a different algorithm
+        from the loop vectorizer.  Both may be enabled at the same time.
+        """
         return ffi.lib.LLVMPY_PassManagerBuilderGetSLPVectorize(self)
 
     @slp_vectorize.setter
     def slp_vectorize(self, enable=True):
         return ffi.lib.LLVMPY_PassManagerBuilderSetSLPVectorize(self, enable)
 
     def _populate_module_pm(self, pm):
```

### Comparing `llvmlite-0.8.0/llvmlite/binding/value.py` & `llvmlite-0.9.0/llvmlite/binding/value.py`

 * *Files 6% similar despite different names*

```diff
@@ -87,15 +87,16 @@
     def __str__(self):
         with ffi.OutputString() as outstr:
             ffi.lib.LLVMPY_PrintValueToString(self, outstr)
             return str(outstr)
 
     @property
     def module(self):
-        """The module this value is defined in.
+        """
+        The module this value was obtained from.
         """
         return self._module
 
     @property
     def name(self):
         return _decode_string(ffi.lib.LLVMPY_GetValueName(self))
 
@@ -138,20 +139,25 @@
         # XXX unused?
         if not isinstance(attr, Attribute):
             attr = Attribute[attr]
         ffi.lib.LLVMPY_AddFunctionAttr(self, attr.value)
 
     @property
     def type(self):
+        """
+        This value's LLVM type.
+        """
         # XXX what does this return?
         return ffi.lib.LLVMPY_TypeOf(self)
 
     @property
     def is_declaration(self):
-        """Is this global defined in the current module?
+        """
+        Whether this value (presumably global) is defined in the current
+        module.
         """
         return ffi.lib.LLVMPY_IsDeclaration(self)
 
 # FFI
 
 ffi.lib.LLVMPY_PrintValueToString.argtypes = [
     ffi.LLVMValueRef,
```

### Comparing `llvmlite-0.8.0/llvmlite/ir/_utils.py` & `llvmlite-0.9.0/llvmlite/ir/_utils.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,38 +1,61 @@
 from __future__ import print_function, absolute_import
 
+from collections import defaultdict
+
 
 class DuplicatedNameError(NameError):
     pass
 
 
 class NameScope(object):
     def __init__(self, parent=None):
         self.parent = parent
         self._useset = set([''])
-        self._basenamemap = {}
+        self._basenamemap = defaultdict(int)
 
     def is_used(self, name):
-        if name in self._useset:
-            return True
-        elif self.parent and self.parent.is_used(name):
-            return True
-        else:
-            return False
-
-    def register(self, name):
-        assert name, "name is empty"
-        if self.is_used(name):
+        scope = self
+        while scope is not None:
+            if name in scope._useset:
+                return True
+            scope = scope.parent
+        return False
+
+    def register(self, name, deduplicate=False):
+        if deduplicate:
+            name = self.deduplicate(name)
+        elif self.is_used(name):
             raise DuplicatedNameError(name)
-
         self._useset.add(name)
+        return name
 
     def deduplicate(self, name):
         basename = name
         while self.is_used(name):
-            ident = self._basenamemap.get(basename, 1)
-            self._basenamemap[basename] = ident + 1
-            name = "%s.%u" % (basename, ident)
+            ident = self._basenamemap[basename] + 1
+            self._basenamemap[basename] = ident
+            name = "{0}.{1}".format(basename, ident)
         return name
 
     def get_child(self):
         return type(self)(parent=self)
+
+
+class _StrCaching(object):
+
+    def __str__(self):
+        try:
+            return self.__cached_str
+        except AttributeError:
+            s = self.__cached_str = self._to_string()
+            return s
+
+
+class _StringReferenceCaching(object):
+
+    def get_reference(self):
+        try:
+            return self.__cached_refstr
+        except AttributeError:
+            s = self.__cached_refstr = self._get_reference()
+            return s
```

### Comparing `llvmlite-0.8.0/llvmlite/ir/builder.py` & `llvmlite-0.9.0/llvmlite/ir/values.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,589 +1,570 @@
+"""
+Classes that are LLVM values: Value, Constant...
+Instructions are in the instructions module.
+"""
+
 from __future__ import print_function, absolute_import
 
-import contextlib
-import functools
+import string
+
+from ..six import StringIO
+from . import types
+from ._utils import _StrCaching, _StringReferenceCaching
+
+
+_VALID_CHARS = (frozenset(map(ord, string.ascii_letters)) |
+                frozenset(map(ord, string.digits)) |
+                frozenset('._-$'))
+
+
+def _escape_string(text):
+    buf = []
+    for ch in text:
+        if ch in _VALID_CHARS:
+            buf.append(chr(ch))
+        else:
+            ashex = hex(ch)[2:]
+            if len(ashex) == 1:
+                ashex = '0' + ashex
+            buf.append('\\' + ashex)
+    return ''.join(buf)
+
+
+class _Undefined(object):
+    pass
+
+Undefined = _Undefined()
+
+
+class ConstOp(object):
+    """
+    A simple value-like object representing the result of a constant operation.
+    """
+
+    def __init__(self, typ, op):
+        assert isinstance(typ, types.Type)
+        self.type = typ
+        self.op = op
+
+    def __str__(self):
+        return self.op
+
+    get_reference = __str__
+
+
+class ConstOpMixin(object):
+    """
+    A mixin defining constant operations, for use in constant-like classes.
+    """
+
+    def bitcast(self, typ):
+        """
+        Bitcast this pointer constant to the given type.
+        """
+        if typ == self.type:
+            return self
+        op = "bitcast ({0} {1} to {2})".format(self.type, self.get_reference(),
+                                               typ)
+        return ConstOp(typ, op)
+
+    def inttoptr(self, typ):
+        """
+        Cast this integer constant to the given pointer type.
+        """
+        assert isinstance(self.type, types.IntType)
+        assert isinstance(typ, types.PointerType)
+        op = "inttoptr ({0} {1} to {2})".format(self.type,
+                                                self.get_reference(),
+                                                typ)
+        return ConstOp(typ, op)
+
+    def gep(self, indices):
+        """
+        Call getelementptr on this pointer constant.
+        """
+        if not isinstance(self.type, types.PointerType):
+            raise TypeError("cannot only call gep() on pointer constants")
+
+        outtype = self.type
+        for i in indices:
+            outtype = outtype.gep(i)
+
+        strindices = ["{0} {1}".format(idx.type, idx.get_reference())
+                      for idx in indices]
+
+        op = "getelementptr ({0}, {1} {2}, {3})".format(
+            self.type.pointee, self.type,
+            self.get_reference(), ', '.join(strindices))
+        return ConstOp(outtype.as_pointer(), op)
+
+
+class Constant(_StrCaching, _StringReferenceCaching, ConstOpMixin):
+    """
+    A constant LLVM value.
+    """
+
+    def __init__(self, typ, constant):
+        assert isinstance(typ, types.Type)
+        assert not isinstance(typ, types.VoidType)
+        self.type = typ
+        self.constant = constant
+
+    def _to_string(self):
+        return '{0} {1}'.format(self.type, self.get_reference())
+
+    def _get_reference(self):
+        if isinstance(self.constant, bytearray):
+            val = 'c"{0}"'.format(_escape_string(self.constant))
+
+        elif self.constant is None:
+            val = self.type.null
+
+        elif self.constant is Undefined:
+            val = "undef"
+
+        else:
+            val = self.type.format_const(self.constant)
+
+        return val
+
+    @classmethod
+    def literal_struct(cls, elems):
+        """
+        Construct a literal structure constant made of the given members.
+        """
+        tys = [el.type for el in elems]
+        return cls(types.LiteralStructType(tys), elems)
+
+    def __eq__(self, other):
+        if isinstance(other, Constant):
+            return str(self) == str(other)
+        else:
+            return False
+
+    def __ne__(self, other):
+        return not self.__eq__(other)
+
+    def __hash__(self):
+        return hash(str(self))
+
+
+class Value(_StrCaching, _StringReferenceCaching):
+    name_prefix = '%'
+    deduplicate_name = True
+    creates_nested_scope = False
+
+    def __init__(self, parent, type, name):
+        assert parent is not None
+        assert isinstance(type, types.Type)
+        self.parent = parent
+        self.type = type
+        pscope = self.parent.scope
+        self.scope = pscope.get_child() if self.creates_nested_scope else pscope
+        self._set_name(name)
+
+    def _to_string(self):
+        buf = []
+        if self.type != types.VoidType():
+            buf.append("{0} = ".format(self.get_reference()))
+        self.descr(buf)
+        return "".join(buf).rstrip()
+
+    def descr(self, buf):
+        raise NotImplementedError
+
+    def _get_name(self):
+        return self._name
+
+    def _set_name(self, name):
+        name = self.scope.register(name, deduplicate=self.deduplicate_name)
+        self._name = name
+
+    name = property(_get_name, _set_name)
+
+    def _get_reference(self):
+        name = self.name
+        # Quote and escape value name
+        if '\\' in name or '"' in name:
+            name = name.replace('\\', '\\5c').replace('"', '\\22')
+        return '{0}"{1}"'.format(self.name_prefix, name)
+
+    @property
+    def function_type(self):
+        ty = self.type
+        if isinstance(ty, types.PointerType):
+            ty = self.type.pointee
+        if isinstance(ty, types.FunctionType):
+            return ty
+        else:
+            raise TypeError("Not a function: {0}".format(self.type))
+
+
+class MetaDataString(Value):
+    """
+    A metadata string, i.e. a constant string used as a value in a metadata
+    node.
+    """
+
+    def __init__(self, parent, string):
+        super(MetaDataString, self).__init__(parent, types.MetaData(), name="")
+        self.string = string
+
+    def descr(self, buf):
+        buf += (self.get_reference(), "\n")
 
-from . import instructions, types, values
+    def _get_reference(self):
+        return '!"{0}"'.format(self.string)
 
-_CMP_MAP = {
-    '>': 'gt',
-    '<': 'lt',
-    '==': 'eq',
-    '!=': 'ne',
-    '>=': 'ge',
-    '<=': 'le',
-}
-
-
-def _binop(opname, cls=instructions.Instruction):
-    def wrap(fn):
-        @functools.wraps(fn)
-        def wrapped(self, lhs, rhs, name='', flags=()):
-            assert lhs.type == rhs.type, "Operands must be the same type"
-            instr = cls(self.block, lhs.type, opname, (lhs, rhs), name, flags)
-            self._insert(instr)
-            return instr
-
-        return wrapped
-
-    return wrap
-
-
-def _binop_with_overflow(opname, cls=instructions.Instruction):
-    def wrap(fn):
-        @functools.wraps(fn)
-        def wrapped(self, lhs, rhs, name=''):
-            assert lhs.type == rhs.type, "Operands must be the same type"
-            ty = lhs.type
-            if not isinstance(ty, types.IntType):
-                raise TypeError("expected an integer type, got %s" % (ty,))
-            bool_ty = types.IntType(1)
-
-            mod = self.module
-            fnty = types.FunctionType(types.LiteralStructType([ty, bool_ty]),
-                                      [ty, ty])
-            fn = mod.declare_intrinsic("llvm.%s.with.overflow" % (opname,),
-                                       [ty], fnty)
-            ret = self.call(fn, [lhs, rhs], name=name)
-            return ret
-
-        return wrapped
-
-    return wrap
-
-
-def _uniop(opname, cls=instructions.Instruction):
-    def wrap(fn):
-        @functools.wraps(fn)
-        def wrapped(self, operand, name=''):
-            instr = cls(self.block, operand.type, opname, [operand], name)
-            self._insert(instr)
-            return instr
-
-        return wrapped
-
-    return wrap
-
-
-def _castop(opname, cls=instructions.CastInstr):
-    def wrap(fn):
-        @functools.wraps(fn)
-        def wrapped(self, val, typ, name=''):
-            if val.type == typ:
-                return val
-            instr = cls(self.block, opname, val, typ, name)
-            self._insert(instr)
-            return instr
-
-        return wrapped
-
-    return wrap
-
-
-class IRBuilder(object):
-    def __init__(self, block=None):
-        self._block = block
-        self._anchor = len(block.instructions) if block else 0
-        self.debug_metadata = None
+    _to_string = _get_reference
+
+    def __eq__(self, other):
+        if isinstance(other, MetaDataString):
+            return self.string == other.string
+        else:
+            return False
+
+    def __ne__(self, other):
+        return not self.__eq__(other)
+
+    def __hash__(self):
+        return hash(self.string)
+
+
+class NamedMetaData(object):
+
+    def __init__(self, parent):
+        self.parent = parent
+        self.operands = []
+
+    def add(self, md):
+        self.operands.append(md)
+
+
+class MDValue(Value):
+    name_prefix = '!'
+
+    def __init__(self, parent, values, name):
+        super(MDValue, self).__init__(parent, types.MetaData(), name=name)
+        self.operands = tuple(values)
+        parent.metadata.append(self)
 
     @property
-    def block(self):
-        return self._block
+    def operand_count(self):
+        return len(self.operands)
+
+    def descr(self, buf):
+        operands = []
+        for op in self.operands:
+            typestr = str(op.type)
+            if isinstance(op.type, types.MetaData):
+                operands.append(op.get_reference())
+            else:
+                operands.append("{0} {1}".format(op.type, op.get_reference()))
+        operands = ', '.join(operands)
+        buf += ("!{{ {0} }}".format(operands), "\n")
+
+    def _get_reference(self):
+        return self.name_prefix + str(self.name)
+
+    def __eq__(self, other):
+        if isinstance(other, MDValue):
+            return self.operands == other.operands
+        else:
+            return False
+
+    def __ne__(self, other):
+        return not self.__eq__(other)
 
-    basic_block = block
+    def __hash__(self):
+        return hash(self.operands)
+
+
+class GlobalValue(Value, ConstOpMixin):
+    """
+    A global value.
+    """
+    name_prefix = '@'
+    deduplicate_name = False
+
+    def __init__(self, *args, **kwargs):
+        super(GlobalValue, self).__init__(*args, **kwargs)
+        self.linkage = ''
+        self.storage_class = ''
+
+
+class GlobalVariable(GlobalValue):
+    """
+    A global variable.
+    """
+
+    def __init__(self, module, typ, name, addrspace=0):
+        assert isinstance(typ, types.Type)
+        super(GlobalVariable, self).__init__(module, typ.as_pointer(addrspace),
+                                             name=name)
+        self.gtype = typ
+        self.initializer = None
+        self.unnamed_addr = False
+        self.global_constant = False
+        self.addrspace = addrspace
+        self.parent.add_global(self)
+
+    def descr(self, buf):
+        if self.global_constant:
+            kind = 'constant'
+        else:
+            kind = 'global'
+
+        if not self.linkage:
+            # Default to external linkage
+            linkage = 'external' if self.initializer is None else ''
+        else:
+            linkage = self.linkage
+
+        if self.addrspace != 0:
+            addrspace = 'addrspace({0:d})'.format(self.addrspace)
+        else:
+            addrspace = ''
+
+        if self.unnamed_addr:
+            unnamed_addr = 'unnamed_addr'
+        else:
+            unnamed_addr = ''
+
+        buf.append("{linkage} {storage_class} {unnamed_addr} {addrspace} {kind} {type} "
+                   .format(linkage=linkage,
+                           storage_class=self.storage_class,
+                           unnamed_addr=unnamed_addr,
+                           addrspace=addrspace,
+                           kind=kind,
+                           type=self.gtype))
+
+        if self.initializer is not None:
+            buf.append(self.initializer.get_reference())
+        buf.append("\n")
+
+
+class AttributeSet(set):
+    _known = ()
+
+    def add(self, name):
+        assert name in self._known
+        return super(AttributeSet, self).add(name)
+
+
+class FunctionAttributes(AttributeSet):
+    _known = frozenset(['alwaysinline', 'builtin', 'cold', 'inlinehint',
+                        'jumptable', 'minsize', 'naked', 'nobuiltin',
+                        'noduplicate', 'noimplicitfloat', 'noinline',
+                        'nonlazybind', 'noredzone', 'noreturn', 'nounwind',
+                        'optnone', 'optsize', 'readnone', 'readonly',
+                        'returns_twice', 'sanitize_address',
+                        'sanitize_memory', 'sanitize_thread', 'ssp',
+                        'sspreg', 'sspstrong', 'uwtable'])
+
+    def __init__(self):
+        self._alignstack = 0
 
     @property
-    def function(self):
-        return self.block.parent
+    def alignstack(self):
+        return self._alignstack
+
+    @alignstack.setter
+    def alignstack(self, val):
+        assert val >= 0
+        self._alignstack = val
+
+    def __repr__(self):
+        attrs = sorted(self)
+        if self.alignstack:
+            attrs.append('alignstack({0:d})'.format(self.alignstack))
+        return ' '.join(attrs)
+
+
+class Function(GlobalValue):
+    """Represent a LLVM Function but does uses a Module as parent.
+    Global Values are stored as a set of dependencies (attribute `depends`).
+    """
+    creates_nested_scope = True
+
+    def __init__(self, module, ftype, name):
+        assert isinstance(ftype, types.Type)
+        super(Function, self).__init__(module, ftype.as_pointer(), name=name)
+        self.ftype = ftype
+        self.blocks = []
+        self.attributes = FunctionAttributes()
+        self.args = tuple([Argument(self, t)
+                           for t in ftype.args])
+        self.return_value = ReturnValue(self, ftype.return_type)
+        self.parent.add_global(self)
+        self.calling_convention = ''
 
     @property
     def module(self):
-        return self.block.parent.module
+        return self.parent
 
-    def position_before(self, instr):
-        self._block = instr.parent
-        self._anchor = self._block.instructions.index(instr)
-
-    def position_after(self, instr):
-        self._block = instr.parent
-        self._anchor = self._block.instructions.index(instr) + 1
-
-    def position_at_start(self, block):
-        self._block = block
-        self._anchor = 0
-
-    def position_at_end(self, block):
-        self._block = block
-        self._anchor = len(block.instructions)
+    @property
+    def entry_basic_block(self):
+        return self.blocks[0]
+
+    @property
+    def basic_blocks(self):
+        return self.blocks
 
     def append_basic_block(self, name=''):
-        return self.function.append_basic_block(name)
+        blk = Block(parent=self, name=name)
+        self.blocks.append(blk)
+        return blk
+
+    def insert_basic_block(self, before, name=''):
+        """Insert block before
+        """
+        blk = Block(parent=self, name=name)
+        self.blocks.insert(before, blk)
+        return blk
+
+    def descr_prototype(self, buf):
+        """
+        Describe the prototype ("head") of the function.
+        """
+        state = "define" if self.blocks else "declare"
+        ret = self.return_value
+        args = ", ".join(str(a) for a in self.args)
+        name = self.get_reference()
+        attrs = self.attributes
+        if any(self.args):
+            vararg = ', ...' if self.ftype.var_arg else ''
+        else:
+            vararg = '...' if self.ftype.var_arg else ''
+        linkage = self.linkage
+        cconv = self.calling_convention
+        prefix = " ".join(str(x) for x in [state, linkage, cconv, ret] if x)
+        prototype = "{prefix} {name}({args}{vararg}) {attrs}\n".format(**locals())
+        buf.append(prototype)
+
+    def descr_body(self, buf):
+        """
+        Describe of the body of the function.
+        """
+        for blk in self.blocks:
+            blk.descr(buf)
+
+    def descr(self, buf):
+        self.descr_prototype(buf)
+        if self.blocks:
+            buf.append("{\n")
+            self.descr_body(buf)
+            buf.append("}\n")
+
+    def __str__(self):
+        buf = []
+        self.descr(buf)
+        return "".join(buf)
 
-    @contextlib.contextmanager
-    def goto_block(self, block):
-        """
-        A context manager which temporarily positions the builder at the end
-        of basic block *bb* (but before any terminator).
-        """
-        old_block = self.basic_block
-        term = block.terminator
-        if term is not None:
-            self.position_before(term)
-        else:
-            self.position_at_end(block)
-        try:
-            yield
-        finally:
-            self.position_at_end(old_block)
-
-    @contextlib.contextmanager
-    def goto_entry_block(self):
-        """
-        A context manager which temporarily positions the builder at the
-        end of the function's entry block.
-        """
-        with self.goto_block(self.function.entry_basic_block):
-            yield
-
-    @contextlib.contextmanager
-    def _branch_helper(self, bbenter, bbexit):
-        self.position_at_end(bbenter)
-        yield bbexit
-        if self.basic_block.terminator is None:
-            self.branch(bbexit)
-
-    @contextlib.contextmanager
-    def if_then(self, pred, likely=None):
-        """
-        A context manager which sets up a conditional basic block based
-        on the given predicate (a i1 value).  If the conditional block
-        is not explicitly terminated, a branch will be added to the next
-        block.
-        If *likely* is given, its boolean value indicates whether the
-        predicate is likely to be true or not, and metadata is issued
-        for LLVM's optimizers to account for that.
-        """
-        bb = self.basic_block
-        bbif = self.append_basic_block(name=bb.name + '.if')
-        bbend = self.append_basic_block(name=bb.name + '.endif')
-        br = self.cbranch(pred, bbif, bbend)
-        if likely is not None:
-            br.set_weights([99, 1] if likely else [1, 99])
-
-        with self._branch_helper(bbif, bbend):
-            yield bbend
-
-        self.position_at_end(bbend)
-
-    @contextlib.contextmanager
-    def if_else(self, pred, likely=None):
-        """
-        A context manager which sets up two conditional basic blocks based
-        on the given predicate (a i1 value).
-        A tuple of context managers is yield'ed.  Each context manager
-        acts as a if_then() block.
-        *likely* has the same meaning as in if_then().
-
-        Typical use::
-            with builder.if_else(pred) as (then, otherwise):
-                with then:
-                    # emit instructions for when the predicate is true
-                with otherwise:
-                    # emit instructions for when the predicate is false
-        """
-        bb = self.basic_block
-        bbif = self.append_basic_block(name=bb.name + '.if')
-        bbelse = self.append_basic_block(name=bb.name + '.else')
-        bbend = self.append_basic_block(name=bb.name + '.endif')
-        br = self.cbranch(pred, bbif, bbelse)
-        if likely is not None:
-            br.set_weights([99, 1] if likely else [1, 99])
-
-        then = self._branch_helper(bbif, bbend)
-        otherwise = self._branch_helper(bbelse, bbend)
-
-        yield then, otherwise
-
-        self.position_at_end(bbend)
-
-    def _insert(self, instr):
-        if self.debug_metadata is not None and 'dbg' not in instr.metadata:
-            instr.metadata['dbg'] = self.debug_metadata
-        self._block.instructions.insert(self._anchor, instr)
-        self._anchor += 1
-
-    def _set_terminator(self, term):
-        assert not self.block.is_terminated
-        self._insert(term)
-        self.block.terminator = term
-        return term
-
-    #
-    # Arithmetic APIs
-    #
-
-    @_binop('shl')
-    def shl(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('lshr')
-    def lshr(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('ashr')
-    def ashr(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('add')
-    def add(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('fadd')
-    def fadd(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('sub')
-    def sub(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('fsub')
-    def fsub(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('mul')
-    def mul(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('fmul')
-    def fmul(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('udiv')
-    def udiv(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('sdiv')
-    def sdiv(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('fdiv')
-    def fdiv(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('urem')
-    def urem(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('srem')
-    def srem(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('frem')
-    def frem(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('or')
-    def or_(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('and')
-    def and_(self, lhs, rhs, name=''):
-        pass
-
-    @_binop('xor')
-    def xor(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('sadd')
-    def sadd_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('smul')
-    def smul_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('ssub')
-    def ssub_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('uadd')
-    def uadd_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('umul')
-    def umul_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    @_binop_with_overflow('usub')
-    def usub_with_overflow(self, lhs, rhs, name=''):
-        pass
-
-    #
-    # Unary APIs
-    #
-
-    def not_(self, value, name=''):
-        return self.xor(value, values.Constant(value.type, -1), name=name)
-
-    def neg(self, value, name=''):
-        return self.sub(values.Constant(value.type, 0), value, name=name)
-
-    #
-    # Comparison APIs
-    #
-
-    def _icmp(self, prefix, cmpop, lhs, rhs, name):
-        try:
-            op = _CMP_MAP[cmpop]
-        except KeyError:
-            raise ValueError("invalid comparison %r for icmp" % (cmpop,))
-        if cmpop not in ('==', '!='):
-            op = prefix + op
-        instr = instructions.ICMPInstr(self.block, op, lhs, rhs, name=name)
-        self._insert(instr)
-        return instr
-
-    def icmp_signed(self, cmpop, lhs, rhs, name=''):
-        return self._icmp('s', cmpop, lhs, rhs, name)
-
-    def icmp_unsigned(self, cmpop, lhs, rhs, name=''):
-        return self._icmp('u', cmpop, lhs, rhs, name)
-
-    def fcmp_ordered(self, cmpop, lhs, rhs, name=''):
-        if cmpop in _CMP_MAP:
-            op = 'o' + _CMP_MAP[cmpop]
-        else:
-            op = cmpop
-        instr = instructions.FCMPInstr(self.block, op, lhs, rhs, name=name)
-        self._insert(instr)
-        return instr
-
-    def fcmp_unordered(self, cmpop, lhs, rhs, name=''):
-        if cmpop in _CMP_MAP:
-            op = 'u' + _CMP_MAP[cmpop]
-        else:
-            op = cmpop
-        instr = instructions.FCMPInstr(self.block, op, lhs, rhs, name=name)
-        self._insert(instr)
-        return instr
-
-    def select(self, cond, lhs, rhs, name=''):
-        instr = instructions.SelectInstr(self.block, cond, lhs, rhs, name=name)
-        self._insert(instr)
-        return instr
-
-    #
-    # Cast APIs
-    #
-
-    @_castop('trunc')
-    def trunc(self, value, typ, name=''):
-        pass
-
-    @_castop('zext')
-    def zext(self, value, typ, name=''):
-        pass
-
-    @_castop('sext')
-    def sext(self, value, typ, name=''):
-        pass
-
-    @_castop('fptrunc')
-    def fptrunc(self, value, typ, name=''):
-        pass
-
-    @_castop('fpext')
-    def fpext(self, value, typ, name=''):
-        pass
-
-    @_castop('bitcast')
-    def bitcast(self, value, typ, name=''):
-        pass
-
-    @_castop('fptoui')
-    def fptoui(self, value, typ, name=''):
-        pass
-
-    @_castop('uitofp')
-    def uitofp(self, value, typ, name=''):
-        pass
-
-    @_castop('fptosi')
-    def fptosi(self, value, typ, name=''):
-        pass
-
-    @_castop('sitofp')
-    def sitofp(self, value, typ, name=''):
-        pass
-
-    @_castop('ptrtoint')
-    def ptrtoint(self, value, typ, name=''):
-        pass
-
-    @_castop('inttoptr')
-    def inttoptr(self, value, typ, name=''):
-        pass
-
-    @_castop('addrspacecast')
-    def addrspacecast(self, value, typ, name=''):
-        pass
-
-    #
-    # Memory APIs
-    #
-
-    def alloca(self, typ, size=None, name=''):
-        if size is None:
-            pass
-        elif isinstance(size, (values.Value, values.Constant)):
-            assert isinstance(size.type, types.IntType)
-        else:
-            # If it is not a Value instance,
-            # assume to be a Python integer.
-            size = values.Constant(types.IntType(32), size)
-
-        al = instructions.AllocaInstr(self.block, typ, size, name)
-        self._insert(al)
-        return al
-
-    def load(self, ptr, name='', align=None):
-        if not isinstance(ptr.type, types.PointerType):
-            raise TypeError("cannot load from value of type %s (%r): not a pointer"
-                            % (ptr.type, str(ptr)))
-        ld = instructions.LoadInstr(self.block, ptr, name)
-        ld.align = align
-        self._insert(ld)
-        return ld
-
-    def store(self, value, ptr, align=None):
-        if not isinstance(ptr.type, types.PointerType):
-            raise TypeError("cannot store to value of type %s (%r): not a pointer"
-                            % (ptr.type, str(ptr)))
-        st = instructions.StoreInstr(self.block, value, ptr)
-        st.align = align
-        self._insert(st)
-        return st
-
-
-    #
-    # Terminators APIs
-    #
-
-    def switch(self, value, default):
-        swt = instructions.SwitchInstr(self.block, 'switch', value, default)
-        self._set_terminator(swt)
-        return swt
-
-    def branch(self, target):
-        """Jump to target
-        """
-        br = instructions.Branch(self.block, "br", [target])
-        self._set_terminator(br)
-        return br
-
-    def cbranch(self, cond, truebr, falsebr):
-        """Branch conditionally
-        """
-        br = instructions.ConditionalBranch(self.block, "br",
-                                            [cond, truebr, falsebr])
-        self._set_terminator(br)
-        return br
-
-    def branch_indirect(self, addr):
-        """Branch indirectly
-        """
-        br = instructions.IndirectBranch(self.block, "indirectbr", addr)
-        self._set_terminator(br)
-        return br
-
-    def ret_void(self):
-        return self._set_terminator(
-            instructions.Ret(self.block, "ret void"))
-
-    def ret(self, value):
-        return self._set_terminator(
-            instructions.Ret(self.block, "ret", value))
-
-    def resume(self, landingpad):
-        """Resume an in-flight exception
-        """
-        br = instructions.Branch(self.block, "resume", [landingpad])
-        self._set_terminator(br)
-        return br
-
-    # Call APIs
-
-    def call(self, fn, args, name='', cconv=None, tail=False):
-        inst = instructions.CallInstr(self.block, fn, args, name=name,
-                                      cconv=cconv, tail=tail)
-        self._insert(inst)
-        return inst
-
-    def invoke(self, fn, args, normal_to, unwind_to, name='', cconv=None, tail=False):
-        inst = instructions.InvokeInstr(self.block, fn, args, normal_to, unwind_to, name=name,
-                                        cconv=cconv)
-        self._set_terminator(inst)
-        return inst
-
-    # GEP APIs
-
-    def gep(self, ptr, indices, inbounds=False, name=''):
-        instr = instructions.GEPInstr(self.block, ptr, indices,
-                                      inbounds=inbounds, name=name)
-        self._insert(instr)
-        return instr
-
-    # Aggregate APIs
-
-    def extract_value(self, agg, idx, name=''):
-        if not isinstance(idx, (tuple, list)):
-            idx = [idx]
-        instr = instructions.ExtractValue(self.block, agg, idx, name=name)
-        self._insert(instr)
-        return instr
-
-    def insert_value(self, agg, value, idx, name=''):
-        if not isinstance(idx, (tuple, list)):
-            idx = [idx]
-        instr = instructions.InsertValue(self.block, agg, value, idx, name=name)
-        self._insert(instr)
-        return instr
-
-    # PHI APIs
-
-    def phi(self, typ, name=''):
-        inst = instructions.PhiInstr(self.block, typ, name=name)
-        self._insert(inst)
-        return inst
-
-    # Special API
-
-    def unreachable(self):
-        inst = instructions.Unreachable(self.block)
-        self._set_terminator(inst)
-        return inst
-
-    def atomic_rmw(self, op, ptr, val, ordering, name=''):
-        inst = instructions.AtomicRMW(self.block, op, ptr, val, ordering, name=name)
-        self._insert(inst)
-        return inst
-
-    def cmpxchg(self, ptr, cmp, val, ordering, failordering=None, name=''):
-        """
-        If failordering is `None`, the value of `ordering` is used.
-        """
-        failordering = ordering if failordering is None else failordering
-        inst = instructions.CmpXchg(self.block, ptr, cmp, val, ordering,
-                                    failordering, name=name)
-        self._insert(inst)
-        return inst
-
-    def landingpad(self, typ, personality, name='', cleanup=False):
-        inst = instructions.LandingPadInstr(self.block, typ, personality, name, cleanup)
-        self._insert(inst)
-        return inst
-
-    def assume(self, cond):
-        fn = self.module.declare_intrinsic("llvm.assume")
-        return self.call(fn, [cond])
+    @property
+    def is_declaration(self):
+        return len(self.blocks) == 0
+
+
+class ArgumentAttributes(AttributeSet):
+    _known = frozenset(['byval', 'inalloca', 'inreg', 'nest', 'noalias',
+                        'nocapture', 'nonnull', 'returned', 'signext',
+                        'sret', 'zeroext'])
+
+
+class _BaseArgument(Value):
+    def __init__(self, parent, typ, name=''):
+        assert isinstance(typ, types.Type)
+        super(_BaseArgument, self).__init__(parent, typ, name=name)
+        self.parent = parent
+        self.attributes = ArgumentAttributes()
+
+    def __repr__(self):
+        return "<Argument %r of type %s>" % (self.name, self.type)
+
+    def add_attribute(self, attr):
+        self.attributes.add(attr)
+
+
+class Argument(_BaseArgument):
+    """
+    The specification of a function argument.
+    """
+
+    def __str__(self):
+        if self.attributes:
+            return "{0} {1} {2}".format(self.type, ' '.join(self.attributes),
+                                        self.get_reference())
+        else:
+            return "{0} {1}".format(self.type, self.get_reference())
+
+
+class ReturnValue(_BaseArgument):
+    """
+    The specification of a function's return value.
+    """
+
+    def __str__(self):
+        if self.attributes:
+            return "{0} {1}".format(' '.join(self.attributes), self.type)
+        else:
+            return str(self.type)
+
+
+class Block(Value):
+    """
+    A LLVM IR basic block. A basic block is a sequence of
+    instructions whose execution always goes from start to end.  That
+    is, a control flow instruction (branch) can only appear as the
+    last instruction, and incoming branches can only jump to the first
+    instruction.
+    """
+
+    def __init__(self, parent, name=''):
+        super(Block, self).__init__(parent, types.LabelType(), name=name)
+        self.instructions = []
+        self.terminator = None
+
+    @property
+    def is_terminated(self):
+        return self.terminator is not None
+
+    @property
+    def function(self):
+        return self.parent
 
+    def descr(self, buf):
+        buf.append("{0}:\n".format(self.name))
+        buf += ["  {0}\n".format(instr) for instr in self.instructions]
+
+    def replace(self, old, new):
+        """Replace an instruction"""
+        if old.type != new.type:
+            raise TypeError("new instruction has a different type")
+        pos = self.instructions.index(old)
+        self.instructions.remove(old)
+        self.instructions.insert(pos, new)
+
+        for bb in self.parent.basic_blocks:
+            for instr in bb.instructions:
+                instr.replace_usage(old, new)
+
+
+class BlockAddress(object):
+    """
+    The address of a basic block.
+    """
+
+    def __init__(self, function, basic_block):
+        assert isinstance(function, Function)
+        assert isinstance(basic_block, Block)
+        self.type = types.IntType(8).as_pointer()
+        self.function = function
+        self.basic_block = basic_block
+
+    def __str__(self):
+        return '{0} {1}'.format(self.type, self.get_reference())
+
+    def get_reference(self):
+        return "blockaddress({0}, {1})".format(
+                    self.function.get_reference(),
+                    self.basic_block.get_reference())
```

### Comparing `llvmlite-0.8.0/llvmlite/ir/context.py` & `llvmlite-0.9.0/llvmlite/ir/context.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/ir/instructions.py` & `llvmlite-0.9.0/llvmlite/ir/instructions.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,27 +9,26 @@
 from .values import Block, Function, Value, Constant, MetaDataString, AttributeSet
 
 
 class Instruction(Value):
     def __init__(self, parent, typ, opname, operands, name='', flags=()):
         super(Instruction, self).__init__(parent, typ, name=name)
         assert isinstance(parent, Block)
+        assert isinstance(flags, (tuple, list))
         self.opname = opname
         self.operands = operands
-        assert isinstance(flags, (tuple, list))
         self.flags = list(flags)
-
         self.metadata = {}
 
-    def _stringify_metatdata(self):
+    def _stringify_metadata(self):
         if self.metadata:
-            buf = []
-            for k, v in self.metadata.items():
-                buf.append("!{0} {1}".format(k, v.get_reference()))
-            return ', ' + ', '.join(buf)
+            buf = [""]
+            buf += ["!{0} {1}".format(k, v.get_reference())
+                    for k, v in self.metadata.items()]
+            return ', '.join(buf)
         else:
             return ''
 
     @property
     def function(self):
         return self.parent.function
 
@@ -40,30 +39,32 @@
     def set_metadata(self, name, node):
         self.metadata[name] = node
 
     def descr(self, buf):
         opname = self.opname
         if self.flags:
             opname = ' '.join([opname] + self.flags)
-        operands = ', '.join(op.get_reference() for op in self.operands)
+        operands = ', '.join([op.get_reference() for op in self.operands])
         typ = self.type
-        metadata = self._stringify_metatdata()
-        print("{opname} {typ} {operands}{metadata}".format(**locals()),
-              file=buf)
+        metadata = self._stringify_metadata()
+        buf.append("{0} {1} {2}{3}\n"
+                   .format(opname, typ, operands, metadata))
 
     def replace_usage(self, old, new):
         if old in self.operands:
             ops = []
             for op in self.operands:
                 ops.append(new if op is old else op)
             self.operands = tuple(ops)
 
+
 class CallInstrAttributes(AttributeSet):
     _known = frozenset(['noreturn', 'nounwind', 'readonly', 'readnone'])
 
+
 class CallInstr(Instruction):
     def __init__(self, parent, func, args, name='', cconv=None, tail=False):
         self.cconv = (func.calling_convention
                       if cconv is None and isinstance(func, Function)
                       else cconv)
         self.tail = tail
         self.attributes = CallInstrAttributes()
@@ -95,28 +96,30 @@
 
     @property
     def called_function(self):
         """Alias for llvmpy"""
         return self.callee
 
     def _descr(self, buf, add_metadata):
-        args = ', '.join('{0} {1}'.format(a.type, a.get_reference())
-                         for a in self.args)
+        args = ', '.join(['{0} {1}'.format(a.type, a.get_reference())
+                          for a in self.args])
         fnty = self.callee.type
+        if isinstance(fnty, types.PointerType):
+            fnty = fnty.pointee
         callee_ref = "{0} {1}".format(fnty, self.callee.get_reference())
         if self.cconv:
             callee_ref = "{0} {1}".format(self.cconv, callee_ref)
-        print("{tail}{opname} {callee}({args}){attributes}{metadata}".format(
-            tail='tail ' if self.tail else '',
-            opname=self.opname,
-            callee=callee_ref,
-            args=args,
-            attributes=''.join([" " + attr for attr in self.attributes]),
-            metadata=self._stringify_metatdata() if add_metadata else "",
-            ), file=buf)
+        buf.append("{0}{1} {2}({3}){4}{5}\n".format(
+            'tail ' if self.tail else '',
+            self.opname,
+            callee_ref,
+            args,
+            ''.join([" " + attr for attr in self.attributes]),
+            self._stringify_metadata() if add_metadata else "",
+            ))
 
     def descr(self, buf):
         self._descr(buf, add_metadata=True)
 
 
 class InvokeInstr(CallInstr):
     def __init__(self, parent, func, args, normal_to, unwind_to, name='', cconv=None):
@@ -125,34 +128,33 @@
         super(InvokeInstr, self).__init__(parent, func, args, name, cconv)
         self.opname = "invoke"
         self.normal_to = normal_to
         self.unwind_to = unwind_to
 
     def descr(self, buf):
         super(InvokeInstr, self)._descr(buf, add_metadata=False)
-        print("      to label {0} unwind label {1}{metadata}".format(
+        buf.append("      to label {0} unwind label {1}{metadata}\n".format(
             self.normal_to.get_reference(),
             self.unwind_to.get_reference(),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            metadata=self._stringify_metadata(),
+            ))
 
 
 class Terminator(Instruction):
     def __init__(self, parent, opname, operands):
         super(Terminator, self).__init__(parent, types.VoidType(), opname,
                                          operands)
         self.metadata = {}
 
     def descr(self, buf):
         opname = self.opname
-        operands = ', '.join("{0} {1}".format(op.type, op.get_reference())
-                             for op in self.operands)
-        metadata = self._stringify_metatdata()
-        print("{opname} {operands}{metadata}".format(**locals()), file=buf,
-              end='')
+        operands = ', '.join(["{0} {1}".format(op.type, op.get_reference())
+                              for op in self.operands])
+        metadata = self._stringify_metadata()
+        buf.append("{0} {1}{2}".format(opname, operands, metadata))
 
 
 class PredictableInstr(Instruction):
 
     def set_weights(self, weights):
         operands = [MetaDataString(self.module, "branch_weights")]
         for w in weights:
@@ -174,19 +176,19 @@
             return self.operands[0]
         else:
             return None
 
     def descr(self, buf):
         return_value = self.return_value
         if return_value is not None:
-            msg = "{0} {1} {2}".format(self.opname, return_value.type,
-                                       return_value.get_reference())
+            buf.append("{0} {1} {2}\n"
+                       .format(self.opname, return_value.type,
+                               return_value.get_reference()))
         else:
-            msg = str(self.opname)
-        print(msg, file=buf)
+            buf.append("{0}\n".format(self.opname))
 
 
 class Branch(Terminator):
     pass
 
 
 class ConditionalBranch(PredictableInstr, Terminator):
@@ -205,20 +207,20 @@
     def add_destination(self, block):
         assert isinstance(block, Block)
         self.destinations.append(block)
 
     def descr(self, buf):
         destinations = ["label {0}".format(blk.get_reference())
                         for blk in self.destinations]
-        print("indirectbr {0} {1}, [{2}]  {metadata}".format(
+        buf.append("indirectbr {0} {1}, [{2}]  {3}\n".format(
             self.address.type,
             self.address.get_reference(),
             ', '.join(destinations),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            self._stringify_metadata(),
+            ))
 
 
 class SwitchInstr(PredictableInstr, Terminator):
 
     def __init__(self, parent, opname, val, default):
         super(SwitchInstr, self).__init__(parent, opname, [val])
         self.default = default
@@ -234,21 +236,21 @@
             val = Constant(self.value.type, val)
         self.cases.append((val, block))
 
     def descr(self, buf):
         cases = ["{0} {1}, label {2}".format(val.type, val.get_reference(),
                                              blk.get_reference())
                  for val, blk in self.cases]
-        print("switch {0} {1}, label {2} [{3}]  {metadata}".format(
+        buf.append("switch {0} {1}, label {2} [{3}]  {4}\n".format(
             self.value.type,
             self.value.get_reference(),
             self.default.get_reference(),
             ' '.join(cases),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            self._stringify_metadata(),
+            ))
 
 
 class Resume(Terminator):
     pass
 
 
 class SelectInstr(Instruction):
@@ -266,20 +268,20 @@
         return self.operands[1]
 
     @property
     def rhs(self):
         return self.operands[2]
 
     def descr(self, buf):
-        print("select {0} {1}, {2} {3}, {4} {5} {metadata}".format(
+        buf.append("select {0} {1}, {2} {3}, {4} {5} {6}\n".format(
             self.cond.type, self.cond.get_reference(),
             self.lhs.type, self.lhs.get_reference(),
             self.rhs.type, self.rhs.get_reference(),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            self._stringify_metadata(),
+            ))
 
 
 class CompareInstr(Instruction):
     # Define the following in subclasses
     OPNAME = 'invalid-compare'
     VALID_OP = {}
 
@@ -287,22 +289,22 @@
         if op not in self.VALID_OP:
             raise ValueError("invalid comparison %r for %s" % (op, self.OPNAME))
         super(CompareInstr, self).__init__(parent, types.IntType(1),
                                            self.OPNAME, [lhs, rhs], name=name)
         self.op = op
 
     def descr(self, buf):
-        print("{0} {1} {2} {3}, {4}{metadata}".format(
+        buf.append("{0} {1} {2} {3}, {4} {5}\n".format(
             self.OPNAME,
             self.op,
             self.operands[0].type,
             self.operands[0].get_reference(),
             self.operands[1].get_reference(),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            self._stringify_metadata(),
+            ))
 
 
 class ICMPInstr(CompareInstr):
     OPNAME = 'icmp'
     VALID_OP = {
         'eq': 'equal',
         'ne': 'not equal',
@@ -340,21 +342,21 @@
 
 
 class CastInstr(Instruction):
     def __init__(self, parent, op, val, typ, name=''):
         super(CastInstr, self).__init__(parent, typ, op, [val], name=name)
 
     def descr(self, buf):
-        print("{0} {1} {2} to {3}{metadata}".format(
+        buf.append("{0} {1} {2} to {3} {4}\n".format(
             self.opname,
             self.operands[0].type,
             self.operands[0].get_reference(),
             self.type,
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+            self._stringify_metadata(),
+            ))
 
 
 class LoadInstr(Instruction):
 
     def __init__(self, parent, ptr, name=''):
         super(LoadInstr, self).__init__(parent, ptr.type.pointee, "load",
                                         [ptr], name=name)
@@ -362,55 +364,57 @@
 
     def descr(self, buf):
         [val] = self.operands
         if self.align is not None:
             align = ', align %d' % (self.align)
         else:
             align = ''
-        print("load {0} {1}{align}{metadata}".format(
-            val.type, val.get_reference(), align=align,
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+        buf.append("load {0}, {1} {2}{3}{4}\n".format(
+            val.type.pointee,
+            val.type,
+            val.get_reference(),
+            align,
+            self._stringify_metadata(),
+            ))
 
 
 class StoreInstr(Instruction):
     def __init__(self, parent, val, ptr):
         super(StoreInstr, self).__init__(parent, types.VoidType(), "store",
                                          [val, ptr])
 
     def descr(self, buf):
         val, ptr = self.operands
         if self.align is not None:
             align = ', align %d' % (self.align)
         else:
             align = ''
-        print("store {0} {1}, {2} {3}{align}{metadata}".format(
-            val.type, val.get_reference(),
-            ptr.type, ptr.get_reference(),
-            align=align,
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+        buf.append("store {0} {1}, {2} {3}{4}{5}\n".format(
+            val.type,
+            val.get_reference(),
+            ptr.type,
+            ptr.get_reference(),
+            align,
+            self._stringify_metadata(),
+            ))
 
 
 class AllocaInstr(Instruction):
     def __init__(self, parent, typ, count, name):
         operands = [count] if count else ()
         super(AllocaInstr, self).__init__(parent, typ.as_pointer(), "alloca",
                                           operands, name)
 
     def descr(self, buf):
-        print("{0} {1}".format(self.opname, self.type.pointee),
-              file=buf, end='')
+        buf.append("{0} {1}".format(self.opname, self.type.pointee))
         if self.operands:
-            print(", {0} {1}".format(
-                self.operands[0].type,
-                self.operands[0].get_reference(),
-                ), file=buf, end='')
+            op, = self.operands
+            buf.append(", {0} {1}".format(op.type, op.get_reference()))
         if self.metadata:
-            print(self._stringify_metatdata(), file=buf)
+            buf.append(self._stringify_metadata())
 
 
 class GEPInstr(Instruction):
     def __init__(self, parent, ptr, indices, inbounds, name):
         typ = ptr.type
         lasttyp = None
         for i in indices:
@@ -427,36 +431,39 @@
         self.pointer = ptr
         self.indices = indices
         self.inbounds = inbounds
 
     def descr(self, buf):
         indices = ['{0} {1}'.format(i.type, i.get_reference())
                    for i in self.indices]
-        head = "getelementptr inbounds" if self.inbounds else "getelementptr"
-        print("{0} {1} {2}, {3} {metadata}".format(
-                  head,
-                  self.pointer.type,
-                  self.pointer.get_reference(),
-                  ', '.join(indices),
-                  metadata=self._stringify_metatdata(),
-                  ), file=buf)
+        op = "getelementptr inbounds" if self.inbounds else "getelementptr"
+        buf.append("{0} {1}, {2} {3}, {4} {5}\n".format(
+                   op,
+                   self.pointer.type.pointee,
+                   self.pointer.type,
+                   self.pointer.get_reference(),
+                   ', '.join(indices),
+                   self._stringify_metadata(),
+                   ))
 
 
 class PhiInstr(Instruction):
     def __init__(self, parent, typ, name):
         super(PhiInstr, self).__init__(parent, typ, "phi", (), name=name)
         self.incomings = []
 
     def descr(self, buf):
         incs = ', '.join('[{0}, {1}]'.format(v.get_reference(),
                                              b.get_reference())
                          for v, b in self.incomings)
-        print("phi {0} {1} {metadata}".format(
-            self.type, incs, metadata=self._stringify_metatdata(),
-            ), file=buf)
+        buf.append("phi {0} {1} {2}\n".format(
+                   self.type,
+                   incs,
+                   self._stringify_metadata(),
+                   ))
 
     def add_incoming(self, value, block):
         assert isinstance(block, Block)
         self.incomings.append((value, block))
 
     def replace_usage(self, old, new):
         self.incomings = [((new if val is old else val), blk)
@@ -478,20 +485,20 @@
 
         self.aggregate = agg
         self.indices = indices
 
     def descr(self, buf):
         indices = [str(i) for i in self.indices]
 
-        print("extractvalue {0} {1}, {2} {metadata}".format(
-            self.aggregate.type,
-            self.aggregate.get_reference(),
-            ', '.join(indices),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+        buf.append("extractvalue {0} {1}, {2} {3}\n".format(
+                   self.aggregate.type,
+                   self.aggregate.get_reference(),
+                   ', '.join(indices),
+                   self._stringify_metadata(),
+                   ))
 
 
 class InsertValue(Instruction):
     def __init__(self, parent, agg, elem, indices, name=''):
         typ = agg.type
         try:
             for i in indices:
@@ -508,97 +515,98 @@
         self.aggregate = agg
         self.value = elem
         self.indices = indices
 
     def descr(self, buf):
         indices = [str(i) for i in self.indices]
 
-        print("insertvalue {0} {1}, {2} {3}, {4} {metadata}".format(
-            self.aggregate.type, self.aggregate.get_reference(),
-            self.value.type, self.value.get_reference(),
-            ', '.join(indices),
-            metadata=self._stringify_metatdata(),
-            ), file=buf)
+        buf.append("insertvalue {0} {1}, {2} {3}, {4} {5}\n".format(
+                   self.aggregate.type, self.aggregate.get_reference(),
+                   self.value.type, self.value.get_reference(),
+                   ', '.join(indices),
+                   self._stringify_metadata(),
+                   ))
 
 
 class Unreachable(Instruction):
     def __init__(self, parent):
         super(Unreachable, self).__init__(parent, types.VoidType(),
                                           "unreachable", (), name='')
 
     def descr(self, buf):
-        print(self.opname, file=buf)
+        buf += (self.opname, "\n")
 
 
 class InlineAsm(object):
     def __init__(self, ftype, asm, constraint, side_effect=False):
         self.type = ftype.return_type
         self.function_type = ftype
         self.asm = asm
         self.constraint = constraint
         self.side_effect = side_effect
 
     def descr(self, buf):
         sideeffect = 'sideeffect' if self.side_effect else ''
-        fmt = "asm {sideeffect} \"{asm}\", \"{constraint}\""
-        print(fmt.format(sideeffect=sideeffect, asm=self.asm,
-                         constraint=self.constraint,),
-              file=buf, end='')
+        fmt = 'asm {sideeffect} "{asm}", "{constraint}"\n'
+        buf.append(fmt.format(sideeffect=sideeffect, asm=self.asm,
+                              constraint=self.constraint))
 
     def get_reference(self):
-        buf = StringIO()
+        buf = []
         self.descr(buf)
-        return buf.getvalue()
+        return "".join(buf)
 
     def __str__(self):
         return "{0} {1}".format(self.type, self.get_reference())
 
 
 class AtomicRMW(Instruction):
     def __init__(self, parent, op, ptr, val, ordering, name):
         super(AtomicRMW, self).__init__(parent, val.type, "atomicrmw",
                                         (ptr, val), name=name)
         self.operation = op
         self.ordering = ordering
 
     def descr(self, buf):
-        fmt = "atomicrmw {op} {ptrty} {ptr}, {ty} {val} {ordering} {metadata}"
-        print(fmt.format(op=self.operation,
-                         ptrty=self.operands[0].type,
-                         ptr=self.operands[0].get_reference(),
-                         ty=self.operands[1].type,
-                         val=self.operands[1].get_reference(),
-                         ordering=self.ordering,
-                         metadata=self._stringify_metatdata(),),
-              file=buf)
+        ptr, val = self.operands
+        fmt = "atomicrmw {op} {ptrty} {ptr}, {valty} {val} {ordering} {metadata}\n"
+        buf.append(fmt.format(op=self.operation,
+                              ptrty=ptr.type,
+                              ptr=ptr.get_reference(),
+                              valty=val.type,
+                              val=val.get_reference(),
+                              ordering=self.ordering,
+                              metadata=self._stringify_metadata(),
+                              ))
 
 
 class CmpXchg(Instruction):
     """This instruction has changed since llvm3.5.  It is not compatible with
     older llvm versions.
     """
     def __init__(self, parent, ptr, cmp, val, ordering, failordering, name):
         outtype = types.LiteralStructType([val.type, types.IntType(1)])
         super(CmpXchg, self).__init__(parent, outtype, "cmpxchg",
                                       (ptr, cmp, val), name=name)
         self.ordering = ordering
         self.failordering = failordering
 
     def descr(self, buf):
+        ptr, cmpval, val = self.operands
         fmt = "cmpxchg {ptrty} {ptr}, {ty} {cmp}, {ty} {val} {ordering} " \
-              "{failordering} {metadata}"
-        print(fmt.format(ptrty=self.operands[0].type,
-                         ptr=self.operands[0].get_reference(),
-                         ty=self.operands[1].type,
-                         cmp=self.operands[1].get_reference(),
-                         val=self.operands[2].get_reference(),
-                         ordering=self.ordering,
-                         failordering=self.failordering,
-                         metadata=self._stringify_metatdata(), ),
-              file=buf)
+              "{failordering} {metadata}\n"
+        buf.append(fmt.format(ptrty=ptr.type,
+                              ptr=ptr.get_reference(),
+                              ty=cmpval.type,
+                              cmp=cmpval.get_reference(),
+                              val=val.get_reference(),
+                              ordering=self.ordering,
+                              failordering=self.failordering,
+                              metadata=self._stringify_metadata(),
+                              ))
 
 
 class _LandingPadClause(object):
     def __init__(self, value):
         self.value = value
 
     def __str__(self):
@@ -626,15 +634,16 @@
         self.clauses = []
 
     def add_clause(self, clause):
         assert isinstance(clause, _LandingPadClause)
         self.clauses.append(clause)
 
     def descr(self, buf):
-        print("landingpad {type} personality {persty} {persfn}"
-              "{cleanup}{clauses}".format(
-            type=self.type,
-            persty=self.personality.type,
-            persfn=self.personality.get_reference(),
-            cleanup=' cleanup' if self.cleanup else '',
-            clauses=''.join(["\n      " + str(clause) for clause in self.clauses])
-            ), file=buf)
+        pers = self.personality
+        fmt = "landingpad {type} personality {persty} {persfn}{cleanup}{clauses}\n"
+        buf.append(fmt.format(type=self.type,
+                              persty=pers.type,
+                              persfn=pers.get_reference(),
+                              cleanup=' cleanup' if self.cleanup else '',
+                              clauses=''.join(["\n      {0}".format(clause)
+                                               for clause in self.clauses]),
+                              ))
```

### Comparing `llvmlite-0.8.0/llvmlite/ir/module.py` & `llvmlite-0.9.0/llvmlite/ir/module.py`

 * *Files 16% similar despite different names*

```diff
@@ -37,35 +37,44 @@
         return nmd
 
     def get_named_metadata(self, name):
         return self.namedmetadata[name]
 
     @property
     def functions(self):
+        """
+        A list of functions declared or defined in this module.
+        """
         return [v for v in self.globals.values()
                 if isinstance(v, values.Function)]
 
     @property
     def global_values(self):
+        """
+        An iterable of global values in this module.
+        """
         return self.globals.values()
 
     def get_global(self, name):
-        """Get a global value by name.
+        """
+        Get a global value by name.
         """
         return self.globals.get(name)
 
     def add_global(self, globalvalue):
-        """Add a global value
+        """
+        Add a new global value.
         """
         assert globalvalue.name not in self.globals
         self.globals[globalvalue.name] = globalvalue
         self._sequence.append(globalvalue.name)
 
     def get_unique_name(self, name=''):
-        """Util for getting a unique name.
+        """
+        Get a unique global name with the following *name* hint.
         """
         return self.scope.deduplicate(name)
 
     def declare_intrinsic(self, intrinsic, tys=(), fnty=None):
         def _error():
             raise NotImplementedError("unknown intrinsic %r with %d types"
                                       % (intrinsic, len(tys)))
@@ -97,34 +106,38 @@
         else:
             _error()
         return values.Function(self, fnty, name=name)
 
     def get_identified_types(self):
         return self.context.identified_types
 
-    def _stringify_metadata(self):
+    def _get_metadata_lines(self):
         mdbuf = []
         for k, v in self.namedmetadata.items():
             mdbuf.append("!{name} = !{{ {operands} }}".format(
                 name=k, operands=','.join(i.get_reference()
                                           for i in v.operands)))
         for md in self.metadata:
             mdbuf.append(str(md))
-        return '\n'.join(mdbuf)
+        return mdbuf
+
+    def _stringify_metadata(self):
+        # For testing
+        return "\n".join(self._get_metadata_lines())
 
     def __repr__(self):
-        body = '\n'.join(str(self.globals[k]) for k in self._sequence)
+        lines = []
+        # Header
+        lines += [
+            '; ModuleID = "%s"' % (self.name,),
+            'target triple = "%s"' % (self.triple,),
+            'target datalayout = "%s"' % (self.data_layout,),
+            '']
+        # Type declarations
+        lines += [it.get_declaration()
+                  for it in self.get_identified_types().values()]
+        # Body
+        lines += [str(self.globals[k]) for k in self._sequence]
+        # Metadata
+        lines += self._get_metadata_lines()
 
-        fmt = ('; ModuleID = "{name}"\n'
-               'target triple = "{triple}"\n'
-               'target datalayout = "{data}"\n'
-               '\n'
-               '{typedecl}\n'
-               '{body}\n'
-               '{md}\n')
-
-        idtypes = [it.get_declaration()
-                   for it in self.get_identified_types().values()]
-        return fmt.format(name=self.name, triple=self.triple, body=body,
-                          md=self._stringify_metadata(),
-                          data=self.data_layout,
-                          typedecl='\n'.join(idtypes))
+        return "\n".join(lines)
```

### Comparing `llvmlite-0.8.0/llvmlite/ir/transforms.py` & `llvmlite-0.9.0/llvmlite/ir/transforms.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/ir/types.py` & `llvmlite-0.9.0/llvmlite/ir/types.py`

 * *Files 5% similar despite different names*

```diff
@@ -2,97 +2,106 @@
 Classes that are LLVM types
 """
 
 from __future__ import print_function, absolute_import
 
 import struct
 
+from ._utils import _StrCaching
+
 
 # XXX This doesn't seem to be used
 _type_state = iter(range(50))
 _type_enum = lambda: next(_type_state)
 
 TYPE_UNKNOWN = _type_enum()
 TYPE_POINTER = _type_enum()
 TYPE_STRUCT = _type_enum()
 TYPE_METADATA = _type_enum()
 
 
-class Type(object):
+def _wrapname(x):
+    return '"{0}"'.format(x.replace('\\', '\\5c').replace('"', '\\22'))
+
+
+class Type(_StrCaching):
     """
     The base class for all LLVM types.
     """
     is_pointer = False
     null = 'zeroinitializer'
 
     kind = TYPE_UNKNOWN
 
     def __repr__(self):
         return "<%s %s>" % (type(self), str(self))
 
-    def __str__(self):
+    def _to_string(self):
         raise NotImplementedError
 
     def as_pointer(self, addrspace=0):
         return PointerType(self, addrspace)
 
     def __ne__(self, other):
         return not (self == other)
 
-    def _get_ll_pointer_type(self, target_data):
+    def _get_ll_pointer_type(self, target_data, context=None):
         """
         Convert this type object to an LLVM type.
         """
         from . import Module, GlobalVariable
         from ..binding import parse_assembly
 
-        m = Module()
+        if context is None:
+            m = Module()
+        else:
+            m = Module(context=context)
         foo = GlobalVariable(m, self, name="foo")
         with parse_assembly(str(m)) as llmod:
             return llmod.get_global_variable(foo.name).type
 
-    def get_abi_size(self, target_data):
+    def get_abi_size(self, target_data, context=None):
         """
         Get the ABI size of this type according to data layout *target_data*.
         """
-        llty = self._get_ll_pointer_type(target_data)
+        llty = self._get_ll_pointer_type(target_data, context)
         return target_data.get_pointee_abi_size(llty)
 
-    def get_abi_alignment(self, target_data):
+    def get_abi_alignment(self, target_data, context=None):
         """
         Get the minimum ABI alignment of this type according to data layout
         *target_data*.
         """
-        llty = self._get_ll_pointer_type(target_data)
+        llty = self._get_ll_pointer_type(target_data, context)
         return target_data.get_pointee_abi_alignment(llty)
 
     def format_const(self, val):
         """
         Format constant *val* of this type.  This method may be overriden
         by subclasses.
         """
         return str(val)
 
 
 class MetaData(Type):
     kind = TYPE_METADATA
 
-    def __str__(self):
+    def _to_string(self):
         return "metadata"
 
     def as_pointer(self):
         raise TypeError
 
 
 class LabelType(Type):
     """
     The label type is the type of e.g. basic blocks.
     """
 
-    def __str__(self):
+    def _to_string(self):
         return "label"
 
 
 class PointerType(Type):
     """
     The type of all pointer values.
     """
@@ -101,15 +110,15 @@
     null = 'null'
 
     def __init__(self, pointee, addrspace=0):
         assert not isinstance(pointee, VoidType)
         self.pointee = pointee
         self.addrspace = addrspace
 
-    def __str__(self):
+    def _to_string(self):
         if self.addrspace != 0:
             return "{0} addrspace({1})* ".format(self.pointee, self.addrspace)
         else:
             return "{0}*".format(self.pointee)
 
     def __eq__(self, other):
         if isinstance(other, PointerType):
@@ -132,15 +141,15 @@
 
 
 class VoidType(Type):
     """
     The type for empty values (e.g. a function returning no value).
     """
 
-    def __str__(self):
+    def _to_string(self):
         return 'void'
 
     def __eq__(self, other):
         return isinstance(other, VoidType)
 
 
 class FunctionType(Type):
@@ -149,17 +158,17 @@
     """
 
     def __init__(self, return_type, args, var_arg=False):
         self.return_type = return_type
         self.args = tuple(args)
         self.var_arg = var_arg
 
-    def __str__(self):
+    def _to_string(self):
         if self.args:
-            strargs = ', '.join(str(a) for a in self.args)
+            strargs = ', '.join([str(a) for a in self.args])
             if self.var_arg:
                 return '{0} ({1}, ...)'.format(self.return_type, strargs)
             else:
                 return '{0} ({1})'.format(self.return_type, strargs)
         elif self.var_arg:
             return '{0} (...)'.format(self.return_type)
         else:
@@ -174,20 +183,40 @@
 
 
 class IntType(Type):
     """
     The type for integers.
     """
     null = '0'
+    _instance_cache = {}
 
-    def __init__(self, bits):
-        assert isinstance(bits, int)
+    def __new__(cls, bits):
+        # Cache all common integer types
+        if 0 <= bits <= 128:
+            try:
+                return cls._instance_cache[bits]
+            except KeyError:
+                inst = cls._instance_cache[bits] = cls.__new(bits)
+                return inst
+        return cls.__new(bits)
+
+    @classmethod
+    def __new(cls, bits):
+        assert isinstance(bits, int) and bits >= 0
+        self = super(IntType, cls).__new__(cls)
         self.width = bits
+        return self
 
-    def __str__(self):
+    def __getnewargs__(self):
+        return self.width,
+
+    def __copy__(self):
+        return self
+
+    def _to_string(self):
         return 'i%u' % (self.width,)
 
     def __eq__(self, other):
         if isinstance(other, IntType):
             return self.width == other.width
         else:
             return False
@@ -219,48 +248,59 @@
     """
     Format *value* as a hexadecimal string of its IEEE double precision
     representation.
     """
     return _format_float_as_hex(value, 'd', 'Q', 16)
 
 
-class FloatType(Type):
+class _BaseFloatType(Type):
+
+    def __new__(cls):
+        return cls._instance_cache
+
+    def __eq__(self, other):
+        return isinstance(other, type(self))
+
+    @classmethod
+    def _create_instance(cls):
+        cls._instance_cache = super(_BaseFloatType, cls).__new__(cls)
+
+
+class FloatType(_BaseFloatType):
     """
     The type for single-precision floats.
     """
     null = '0.0'
     intrinsic_name = 'f32'
 
     def __str__(self):
         return 'float'
 
-    def __eq__(self, other):
-        return isinstance(other, type(self))
-
     def format_const(self, val):
         return _format_double(_as_float(val))
 
 
-class DoubleType(Type):
+class DoubleType(_BaseFloatType):
     """
     The type for double-precision floats.
     """
     null = '0.0'
     intrinsic_name = 'f64'
 
     def __str__(self):
         return 'double'
 
-    def __eq__(self, other):
-        return isinstance(other, type(self))
-
     def format_const(self, val):
         return _format_double(val)
 
 
+for _cls in (FloatType, DoubleType):
+    _cls._create_instance()
+
+
 class _Repeat(object):
     def __init__(self, value, size):
         self.value = value
         self.size = size
 
     def __len__(self):
         return self.size
@@ -291,61 +331,64 @@
     @property
     def elements(self):
         return _Repeat(self.element, self.count)
 
     def __len__(self):
         return self.count
 
-    def __str__(self):
-        return '[{0:d} x {1}]'.format(self.count, self.element)
+    def _to_string(self):
+        return "[%d x %s]" % (self.count, self.element)
 
     def __eq__(self, other):
         if isinstance(other, ArrayType):
             return self.element == other.element and self.count == other.count
 
     def gep(self, i):
         """
         Resolve the type of the i-th element (for getelementptr lookups).
         """
         if not isinstance(i.type, IntType):
             raise TypeError(i.type)
         return self.element
 
     def format_const(self, val):
-        fmter = lambda x: "{0} {1}".format(x.type, x.get_reference())
-        return "[{0}]".format(', '.join(map(fmter, val)))
+        itemstring = ", " .join(["{0} {1}".format(x.type, x.get_reference())
+                                 for x in val])
+        return "[{0}]".format(itemstring)
 
 
 class BaseStructType(Aggregate):
     """
     The base type for heterogenous struct types.
     """
 
     kind = TYPE_STRUCT
 
     def __len__(self):
-        assert not self.is_opaque
+        assert self.elements is not None
         return len(self.elements)
 
     def __iter__(self):
-        assert not self.is_opaque
+        assert self.elements is not None
         return iter(self.elements)
 
     @property
     def is_opaque(self):
         return self.elements is None
 
     def structure_repr(self):
-        """Return the LLVM IR for the structure representation
         """
-        return '{%s}' % ', '.join(map(str, self.elements))
+        Return the LLVM IR for the structure representation
+        """
+        return '{%s}' % ', '.join([str(x) for x in self.elements])
 
     def format_const(self, val):
-        fmter = lambda x: "{0} {1}".format(x.type, x.get_reference())
-        return "{{{0}}}".format(', '.join(map(fmter, val)))
+        itemstring = ", " .join(["{0} {1}".format(x.type, x.get_reference())
+                                 for x in val])
+        return "{{{0}}}".format(itemstring)
 
     def gep(self, i):
         """
         Resolve the type of the i-th element (for getelementptr lookups).
 
         *i* needs to be a LLVM constant, so that the type can be determined
         at compile-time.
@@ -362,15 +405,15 @@
     """
 
     null = 'zeroinitializer'
 
     def __init__(self, elems):
         self.elements = tuple(elems)
 
-    def __str__(self):
+    def _to_string(self):
         return self.structure_repr()
 
     def __eq__(self, other):
         if isinstance(other, LiteralStructType):
             return self.elements == other.elements
 
 
@@ -386,19 +429,20 @@
 
     def __init__(self, context, name):
         assert name
         self.context = context
         self.name = name
         self.elements = None
 
-    def __str__(self):
-        return "%{name}".format(name=self.name)
+    def _to_string(self):
+        return "%{name}".format(name=_wrapname(self.name))
 
     def get_declaration(self):
-        """Returns the string for the declaration of the type
+        """
+        Returns the string for the declaration of the type
         """
         if self.is_opaque:
             out = "{strrep} = type opaque".format(strrep=str(self))
         else:
             out = "{strrep} = type {struct}".format(
                 strrep=str(self), struct=self.structure_repr())
         return out
```

### Comparing `llvmlite-0.8.0/llvmlite/llvmpy/core.py` & `llvmlite-0.9.0/llvmlite/llvmpy/core.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/llvmpy/ee.py` & `llvmlite-0.9.0/llvmlite/llvmpy/ee.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/llvmpy/passes.py` & `llvmlite-0.9.0/llvmlite/llvmpy/passes.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/six.py` & `llvmlite-0.9.0/llvmlite/six.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/tests/__init__.py` & `llvmlite-0.9.0/llvmlite/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/tests/customize.py` & `llvmlite-0.9.0/llvmlite/tests/customize.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/tests/test_binding.py` & `llvmlite-0.9.0/llvmlite/tests/test_binding.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 from ctypes.util import find_library
 import gc
 import subprocess
 import sys
 import unittest
 import platform
 import locale
+import re
 
 from llvmlite import six
 from llvmlite import binding as llvm
 from llvmlite.binding import ffi
 from . import TestCase
 
 
@@ -162,14 +163,44 @@
         self.assertIs(addr, None)
 
     def test_get_default_triple(self):
         triple = llvm.get_default_triple()
         self.assertIsInstance(triple, str)
         self.assertTrue(triple)
 
+    def test_get_process_triple(self):
+        triple = llvm.get_process_triple()
+        default = llvm.get_default_triple()
+        self.assertIsInstance(triple, str)
+        self.assertTrue(triple)
+
+        default_parts = default.split('-')
+        triple_parts = triple.split('-')
+        # Arch must be equal
+        self.assertEqual(default_parts[0], triple_parts[0])
+
+    def test_get_host_cpu_features(self):
+        features = llvm.get_host_cpu_features()
+        self.assertIsInstance(features, dict)
+        self.assertIsInstance(features, llvm.FeatureMap)
+        for k, v in features.items():
+            self.assertIsInstance(k, str)
+            self.assertTrue(k)  # feature string cannot be empty
+            self.assertIsInstance(v, bool)
+        self.assertIsInstance(features.flatten(), str)
+
+        re_term = r"[+\-][a-zA-Z0-9\._]+"
+        regex = r"^({0}|{0}(,{0})*)?$".format(re_term)
+        # quick check for our regex
+        self.assertIsNotNone(re.match(regex, ""))
+        self.assertIsNotNone(re.match(regex, "+aa"))
+        self.assertIsNotNone(re.match(regex, "+a,-bb"))
+        # check CpuFeature.flatten()
+        self.assertIsNotNone(re.match(regex, features.flatten()))
+
     def test_get_host_cpu_name(self):
         cpu = llvm.get_host_cpu_name()
         self.assertIsInstance(cpu, str)
         self.assertTrue(cpu)
 
     def test_initfini(self):
         code = """if 1:
@@ -190,15 +221,15 @@
 
             llvm.set_option("progname", "-debug-pass=Disabled")
             """
         subprocess.check_call([sys.executable, "-c", code])
 
     def test_version(self):
         major, minor, patch = llvm.llvm_version_info
-        self.assertIn((major, minor), [(3, 5), (3, 6)])
+        self.assertIn((major, minor), [(3, 6), (3, 7)])
         self.assertIn(patch, range(10))
 
     def test_check_jit_execution(self):
         llvm.check_jit_execution()
 
     @unittest.skipIf(no_de_locale(), "Locale not available")
     def test_print_double_locale(self):
@@ -737,50 +768,14 @@
         mod = self.module()
         gv_i32 = mod.get_global_variable("glob")
         # A global is a pointer, it has the ABI size of a pointer
         pointer_size = 4 if sys.maxsize < 2 ** 32 else 8
         self.assertEqual(td.get_abi_size(gv_i32.type), pointer_size)
 
 
-class TestTargetLibraryInfo(BaseTest):
-
-    def tli(self):
-        return llvm.create_target_library_info(llvm.get_default_triple())
-
-    def test_create_target_library_info(self):
-        tli = llvm.create_target_library_info(llvm.get_default_triple())
-        with tli:
-            pass
-        tli.close()
-
-    def test_get_libfunc(self):
-        tli = self.tli()
-        with self.assertRaises(NameError):
-            tli.get_libfunc("xyzzy")
-        fmin = tli.get_libfunc("fmin")
-        self.assertEqual(fmin.name, "fmin")
-        self.assertIsInstance(fmin.identity, int)
-        fmax = tli.get_libfunc("fmax")
-        self.assertNotEqual(fmax.identity, fmin.identity)
-
-    def test_set_unavailable(self):
-        tli = self.tli()
-        fmin = tli.get_libfunc("fmin")
-        tli.set_unavailable(fmin)
-
-    def test_disable_all(self):
-        tli = self.tli()
-        tli.disable_all()
-
-    def test_add_pass(self):
-        tli = self.tli()
-        pm = llvm.create_module_pass_manager()
-        tli.add_pass(pm)
-
-
 class TestPassManagerBuilder(BaseTest):
 
     def pmb(self):
         return llvm.PassManagerBuilder()
 
     def test_old_api(self):
         # Test the create_pass_manager_builder() factory function
```

### Comparing `llvmlite-0.8.0/llvmlite/tests/test_ir.py` & `llvmlite-0.9.0/llvmlite/tests/test_ir.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 IR Construction Tests
 """
 
 from __future__ import print_function, absolute_import
 
 import copy
 import itertools
+import pickle
 import re
 import textwrap
 import unittest
 from array import array
 
 from . import TestCase
 from llvmlite import ir
@@ -55,17 +56,17 @@
         return ir.Function(self.module(), fnty, name)
 
     def block(self, func=None, name=''):
         func = func or self.function()
         return func.append_basic_block(name)
 
     def descr(self, thing):
-        sio = six.StringIO()
-        thing.descr(sio)
-        return sio.getvalue()
+        buf = []
+        thing.descr(buf)
+        return "".join(buf)
 
     def _normalize_asm(self, asm):
         asm = textwrap.dedent(asm)
         # Normalize indent
         asm = asm.replace("\n    ", "\n  ")
         return asm
 
@@ -265,28 +266,30 @@
 
 
 class TestBuildInstructions(TestBase):
     """
     Test IR generation of LLVM instructions through the IRBuilder class.
     """
 
+    maxDiff = 4000
+
     def test_simple(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
         builder.add(a, b, 'res')
         self.check_block(block, """\
             my_block:
                 %"res" = add i32 %".1", %".2"
             """)
 
     def test_binops(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
-        a, b = builder.function.args[:2]
+        a, b, ff = builder.function.args[:3]
         builder.add(a, b, 'c')
         builder.fadd(a, b, 'd')
         builder.sub(a, b, 'e')
         builder.fsub(a, b, 'f')
         builder.mul(a, b, 'g')
         builder.fmul(a, b, 'h')
         builder.udiv(a, b, 'i')
@@ -297,14 +300,18 @@
         builder.frem(a, b, 'n')
         builder.or_(a, b, 'o')
         builder.and_(a, b, 'p')
         builder.xor(a, b, 'q')
         builder.shl(a, b, 'r')
         builder.ashr(a, b, 's')
         builder.lshr(a, b, 't')
+        with self.assertRaises(ValueError) as cm:
+            builder.add(a, ff)
+        self.assertEqual(str(cm.exception),
+                         "Operands must be the same type, got (i32, double)")
         self.assertFalse(block.is_terminated)
         self.check_block(block, """\
             my_block:
                 %"c" = add i32 %".1", %".2"
                 %"d" = fadd i32 %".1", %".2"
                 %"e" = sub i32 %".1", %".2"
                 %"f" = fsub i32 %".1", %".2"
@@ -346,20 +353,20 @@
         builder.smul_with_overflow(a, b, 'd')
         builder.ssub_with_overflow(a, b, 'e')
         builder.uadd_with_overflow(a, b, 'f')
         builder.umul_with_overflow(a, b, 'g')
         builder.usub_with_overflow(a, b, 'h')
         self.check_block(block, """\
             my_block:
-                %"c" = call {i32, i1} (i32, i32)* @"llvm.sadd.with.overflow.i32"(i32 %".1", i32 %".2")
-                %"d" = call {i32, i1} (i32, i32)* @"llvm.smul.with.overflow.i32"(i32 %".1", i32 %".2")
-                %"e" = call {i32, i1} (i32, i32)* @"llvm.ssub.with.overflow.i32"(i32 %".1", i32 %".2")
-                %"f" = call {i32, i1} (i32, i32)* @"llvm.uadd.with.overflow.i32"(i32 %".1", i32 %".2")
-                %"g" = call {i32, i1} (i32, i32)* @"llvm.umul.with.overflow.i32"(i32 %".1", i32 %".2")
-                %"h" = call {i32, i1} (i32, i32)* @"llvm.usub.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"c" = call {i32, i1} (i32, i32) @"llvm.sadd.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"d" = call {i32, i1} (i32, i32) @"llvm.smul.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"e" = call {i32, i1} (i32, i32) @"llvm.ssub.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"f" = call {i32, i1} (i32, i32) @"llvm.uadd.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"g" = call {i32, i1} (i32, i32) @"llvm.umul.with.overflow.i32"(i32 %".1", i32 %".2")
+                %"h" = call {i32, i1} (i32, i32) @"llvm.usub.with.overflow.i32"(i32 %".1", i32 %".2")
             """)
 
     def test_unary_ops(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
         builder.neg(a, 'c')
@@ -479,55 +486,63 @@
             my_block:
                 %"my_phi" = phi i32 [%".1", %"b2"], [%".2", %"b3"]
             """)
 
     def test_mem_ops(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
-        a, b = builder.function.args[:2]
+        a, b, z = builder.function.args[:3]
         c = builder.alloca(int32, name='c')
         d = builder.alloca(int32, size=42, name='d')
-        e = builder.alloca(int32, size=a, name='e')
-        self.assertEqual(e.type, ir.PointerType(int32))
+        e = builder.alloca(dbl, size=a, name='e')
+        self.assertEqual(e.type, ir.PointerType(dbl))
+        ee = builder.store(z, e)
+        self.assertEqual(ee.type, ir.VoidType())
         f = builder.store(b, c)
         self.assertEqual(f.type, ir.VoidType())
         g = builder.load(c, 'g')
         self.assertEqual(g.type, int32)
         # With alignment
         h = builder.store(b, c, align=1)
         self.assertEqual(h.type, ir.VoidType())
         i = builder.load(c, 'i', align=1)
         self.assertEqual(i.type, int32)
         # Not pointer types
         with self.assertRaises(TypeError):
             builder.store(b, a)
         with self.assertRaises(TypeError):
             builder.load(b)
+        # Mismatching pointer type
+        with self.assertRaises(TypeError) as cm:
+            builder.store(b, e)
+        self.assertEqual(str(cm.exception),
+                         "cannot store i32 to double*: mismatching types")
         self.check_block(block, """\
             my_block:
                 %"c" = alloca i32
                 %"d" = alloca i32, i32 42
-                %"e" = alloca i32, i32 %".1"
+                %"e" = alloca double, i32 %".1"
+                store double %".3", double* %"e"
                 store i32 %".2", i32* %"c"
-                %"g" = load i32* %"c"
+                %"g" = load i32, i32* %"c"
                 store i32 %".2", i32* %"c", align 1
-                %"i" = load i32* %"c", align 1
+                %"i" = load i32, i32* %"c", align 1
             """)
 
     def test_gep(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
         c = builder.alloca(ir.PointerType(int32), name='c')
         d = builder.gep(c, [ir.Constant(int32, 5), a], name='d')
         self.assertEqual(d.type, ir.PointerType(int32))
         self.check_block(block, """\
             my_block:
                 %"c" = alloca i32*
-                %"d" = getelementptr i32** %"c", i32 5, i32 %".1"
+                %"d" = getelementptr i32*, i32** %"c", i32 5, i32 %".1"
             """)
         # XXX test with more complex types
 
     def test_extract_insert_value(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
@@ -575,15 +590,15 @@
 
         self.check_block(block, """\
             my_block:
                 %"c" = extractvalue {i32, i1} {i32 4, i1 true}, 0
                 %"d" = insertvalue {i32, i1} {i32 4, i1 true}, i32 %".1", 0
                 %"e" = insertvalue {i32, i1} %"d", i1 false, 1
                 %"ptr" = alloca {i8, {i32, i1}}
-                %"j" = load {i8, {i32, i1}}* %"ptr"
+                %"j" = load {i8, {i32, i1}}, {i8, {i32, i1}}* %"ptr"
                 %"k" = extractvalue {i8, {i32, i1}} %"j", 0
                 %"l" = extractvalue {i8, {i32, i1}} %"j", 1
                 %"m" = extractvalue {i8, {i32, i1}} %"j", 1, 0
                 %"n" = extractvalue {i8, {i32, i1}} %"j", 1, 1
                 %"o" = insertvalue {i8, {i32, i1}} %"j", {i32, i1} %"l", 1
                 %"p" = insertvalue {i8, {i32, i1}} %"j", i32 %".1", 1, 0
             """)
@@ -735,32 +750,32 @@
         builder.call(f, (a, b), 'res_f')
         builder.call(g, (b, a), 'res_g')
         builder.call(f, (a, b), 'res_f_fast', cconv='fastcc')
         res_f_readonly = builder.call(f, (a, b), 'res_f_readonly')
         res_f_readonly.attributes.add('readonly')
         self.check_block(block, """\
             my_block:
-                %"res_f" = call float (i32, i32)* @"f"(i32 %".1", i32 %".2")
-                %"res_g" = call double (i32, ...)* @"g"(i32 %".2", i32 %".1")
-                %"res_f_fast" = call fastcc float (i32, i32)* @"f"(i32 %".1", i32 %".2")
-                %"res_f_readonly" = call float (i32, i32)* @"f"(i32 %".1", i32 %".2") readonly
+                %"res_f" = call float (i32, i32) @"f"(i32 %".1", i32 %".2")
+                %"res_g" = call double (i32, ...) @"g"(i32 %".2", i32 %".1")
+                %"res_f_fast" = call fastcc float (i32, i32) @"f"(i32 %".1", i32 %".2")
+                %"res_f_readonly" = call float (i32, i32) @"f"(i32 %".1", i32 %".2") readonly
             """)
 
     def test_invoke(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
         tp_f = ir.FunctionType(flt, (int32, int32))
         f = ir.Function(builder.function.module, tp_f, 'f')
         bb_normal = builder.function.append_basic_block(name='normal')
         bb_unwind = builder.function.append_basic_block(name='unwind')
         builder.invoke(f, (a, b), bb_normal, bb_unwind, 'res_f')
         self.check_block(block, """\
             my_block:
-                %"res_f" = invoke float (i32, i32)* @"f"(i32 %".1", i32 %".2")
+                %"res_f" = invoke float (i32, i32) @"f"(i32 %".1", i32 %".2")
                     to label %"normal" unwind label %"unwind"
             """)
 
     def test_landingpad(self):
         block = self.block(name='my_block')
         builder = ir.IRBuilder(block)
         tp_pers = ir.FunctionType(int8, (), var_arg=True)
@@ -785,15 +800,15 @@
         builder = ir.IRBuilder(block)
         a, b = builder.function.args[:2]
         c = builder.icmp_signed('>', a, b, name='c')
         builder.assume(c)
         self.check_block(block, """\
             my_block:
                 %"c" = icmp sgt i32 %".1", %".2"
-                call void (i1)* @"llvm.assume"(i1 %"c")
+                call void (i1) @"llvm.assume"(i1 %"c")
             """)
 
 
 class TestBuilderMisc(TestBase):
     """
     Test various other features of the IRBuilder class.
     """
@@ -1035,41 +1050,66 @@
             my_block:
                 %"c" = alloca i32*, !dbg !0
             """)
 
 
 class TestTypes(TestBase):
 
-    def test_comparisons(self):
-        # A bunch of mutually unequal types
+    def has_logical_equality(self, ty):
+        while isinstance(ty, ir.PointerType):
+            ty = ty.pointee
+        return not isinstance(ty, ir.LabelType)
+
+    def assorted_types(self):
+        """
+        A bunch of mutually unequal types
+        """
+        # Avoid polluting the namespace
+        context = ir.Context()
         types = [
             ir.LabelType(), ir.VoidType(),
             ir.FunctionType(int1, (int8, int8)), ir.FunctionType(int1, (int8,)),
             ir.FunctionType(int1, (int8,), var_arg=True),
             ir.FunctionType(int8, (int8,)),
             int1, int8, int32, flt, dbl,
             ir.ArrayType(flt, 5), ir.ArrayType(dbl, 5), ir.ArrayType(dbl, 4),
             ir.LiteralStructType((int1, int8)), ir.LiteralStructType((int8, int1)),
+            context.get_identified_type("MyType1"),
+            context.get_identified_type("MyType2"),
             ]
-        types.extend([ir.PointerType(tp) for tp in types
-                      if not isinstance(tp, ir.VoidType)])
+        types += [ir.PointerType(tp) for tp in types
+                  if not isinstance(tp, (ir.VoidType, ir.LabelType))]
+
+        return types
+
+    def test_pickling(self):
+        types = self.assorted_types()
+        for ty in types:
+            data = pickle.dumps(ty, protocol=-1)
+            newty = pickle.loads(data)
+            self.assertIs(newty.__class__, ty.__class__)
+            self.assertEqual(str(newty), str(ty))
+            if self.has_logical_equality(ty):
+                self.assertEqual(newty, ty)
+
+    def test_comparisons(self):
+        types = self.assorted_types()
         for a, b in itertools.product(types, types):
             if a is not b:
                 self.assertFalse(a == b, (a, b))
                 self.assertTrue(a != b, (a, b))
         # We assume copy.copy() works fine here...
         for tp in types:
             other = copy.copy(tp)
-            self.assertIsNot(other, tp)
-            if isinstance(tp, ir.LabelType):
-                self.assertFalse(tp == other, (tp, other))
-                self.assertTrue(tp != other, (tp, other))
-            else:
+            if self.has_logical_equality(tp):
                 self.assertTrue(tp == other, (tp, other))
                 self.assertFalse(tp != other, (tp, other))
+            else:
+                self.assertFalse(tp == other, (tp, other))
+                self.assertTrue(tp != other, (tp, other))
 
     def test_str(self):
         """
         Test the string representation of types.
         """
         self.assertEqual(str(int1), 'i1')
         self.assertEqual(str(ir.IntType(29)), 'i29')
@@ -1096,15 +1136,19 @@
         self.assertEqual(str(ir.LiteralStructType((
             ir.PointerType(int1), ir.LiteralStructType((int32, int8))))),
             '{i1*, {i32, i8}}')
 
         # Avoid polluting the namespace
         context = ir.Context()
         mytype = context.get_identified_type("MyType")
-        self.assertEqual(str(mytype), "%MyType")
+        self.assertEqual(str(mytype), "%\"MyType\"")
+        mytype1 = context.get_identified_type("MyType\\")
+        self.assertEqual(str(mytype1), "%\"MyType\\5c\"")
+        mytype2 = context.get_identified_type("MyType\"")
+        self.assertEqual(str(mytype2), "%\"MyType\\22\"")
 
     def test_gep(self):
         def check_constant(tp, i, expected):
             actual = tp.gep(ir.Constant(int32, i))
             self.assertEqual(actual, expected)
         def check_index_type(tp):
             index = ir.Constant(dbl, 1.0)
@@ -1167,14 +1211,22 @@
         self.assert_valid_ir(module)
         oldstr = str(module)
         mytype.set_body(ir.IntType(32), ir.IntType(64), ir.FloatType())
         self.assertFalse(mytype.is_opaque)
         self.assert_valid_ir(module)
         self.assertNotEqual(oldstr, str(module))
 
+    def test_target_data_non_default_context(self):
+        context = ir.Context()
+        mytype = context.get_identified_type("MyType")
+        mytype.elements = [ir.IntType(32)]
+        module = ir.Module(context=context)
+        td = llvm.create_target_data("e-m:e-i64:64-f80:128-n8:16:32:64-S128")
+        self.assertEqual(mytype.get_abi_size(td, context=context), 4)
+
 
 c32 = lambda i: ir.Constant(int32, i)
 
 
 class TestConstant(TestBase):
 
     def test_integers(self):
@@ -1201,21 +1253,22 @@
         self.assertEqual(str(c), 'double 0x3ff8000000000000')
         c = ir.Constant(dbl, -1.5)
         self.assertEqual(str(c), 'double 0xbff8000000000000')
         c = ir.Constant(dbl, ir.Undefined)
         self.assertEqual(str(c), 'double undef')
 
     def test_arrays(self):
-        # XXX Test byte array special case
         c = ir.Constant(ir.ArrayType(int32, 3), (c32(5), c32(6), c32(4)))
         self.assertEqual(str(c), '[3 x i32] [i32 5, i32 6, i32 4]')
         c = ir.Constant(ir.ArrayType(int32, 2), (c32(5), c32(ir.Undefined)))
         self.assertEqual(str(c), '[2 x i32] [i32 5, i32 undef]')
         c = ir.Constant(ir.ArrayType(int32, 2), ir.Undefined)
         self.assertEqual(str(c), '[2 x i32] undef')
+        c = ir.Constant(ir.ArrayType(int8, 3), bytearray(b"\x01\x04\xff"))
+        self.assertEqual(str(c), r'[3 x i8] c"\01\04\ff"')
 
     def test_structs(self):
         c = ir.Constant(ir.LiteralStructType((flt, int1)),
                         (ir.Constant(ir.FloatType(), 1.5),
                          ir.Constant(int1, True)))
         self.assertEqual(str(c), '{float, i1} {float 0x3ff8000000000000, i1 true}')
         c = ir.Constant.literal_struct((ir.Constant(ir.FloatType(), 1.5),
@@ -1237,14 +1290,23 @@
         # With utf-8, the following will cause:
         # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe0 in position 136: invalid continuation byte
         parsed = llvm.parse_assembly(str(m))
         # Make sure the encoding does not modify the IR
         reparsed = llvm.parse_assembly(str(parsed))
         self.assertEqual(str(parsed), str(reparsed))
 
+    def test_gep(self):
+        m = self.module()
+        tp = ir.LiteralStructType((flt, int1))
+        gv = ir.GlobalVariable(m, tp, "myconstant")
+        c = gv.gep([ir.Constant(int32, x) for x in (0, 1)])
+        self.assertEqual(str(c),
+            'getelementptr ({float, i1}, {float, i1}* @"myconstant", i32 0, i32 1)')
+        self.assertEqual(c.type, ir.PointerType(int1))
+
 
 class TestTransforms(TestBase):
     def test_call_transform(self):
         mod = ir.Module()
         foo = ir.Function(mod, ir.FunctionType(ir.VoidType(), ()), "foo")
         bar = ir.Function(mod, ir.FunctionType(ir.VoidType(), ()), "bar")
         builder = ir.IRBuilder()
```

### Comparing `llvmlite-0.8.0/llvmlite/tests/test_valuerepr.py` & `llvmlite-0.9.0/llvmlite/tests/test_valuerepr.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/llvmlite/utils.py` & `llvmlite-0.9.0/llvmlite/utils.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/PKG-INFO` & `llvmlite-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: llvmlite
-Version: 0.8.0
+Version: 0.9.0
 Summary: lightweight wrapper around basic LLVM functionality
 Home-page: http://llvmlite.pydata.org
 Author: Continuum Analytics, Inc.
 Author-email: numba-users@continuum.io
 License: BSD
 Download-URL: https://github.com/numba/llvmlite
 Description: UNKNOWN
```

### Comparing `llvmlite-0.8.0/README.rst` & `llvmlite-0.9.0/README.rst`

 * *Files 10% similar despite different names*

```diff
@@ -46,14 +46,15 @@
 
 
 Compatibility
 =============
 
 llvmlite works with Python 2.6 or greater (including Python 3.3 or greater).
 
+As of version 0.9, llvmlite requires LLVM 3.7.  It does not support earlier or later versions of LLVM.
 
 Documentation
 =============
 
 You'll find the documentation at http://llvmlite.pydata.org
```

### Comparing `llvmlite-0.8.0/run_coverage.py` & `llvmlite-0.9.0/run_coverage.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/setup.py` & `llvmlite-0.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `llvmlite-0.8.0/versioneer.py` & `llvmlite-0.9.0/versioneer.py`

 * *Files identical despite different names*

