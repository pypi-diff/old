# Comparing `tmp/numba-0.8.1.tar.gz` & `tmp/numba-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/numba-0.8.1.tar", last modified: Fri May  3 15:13:21 2013, max compression
+gzip compressed data, was "dist/numba-0.9.0.tar", last modified: Tue Jun  4 10:15:49 2013, max compression
```

## Comparing `numba-0.8.1.tar` & `numba-0.9.0.tar`

### file list

```diff
@@ -1,569 +1,587 @@
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/
--rw-rw-r--   0 mark      (1000) mark      (1000)    25596 2013-05-03 14:59:52.000000 numba-0.8.1/versioneer.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       60 2013-05-03 14:59:52.000000 numba-0.8.1/requirements.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)      237 2013-05-03 14:59:52.000000 numba-0.8.1/setup.cfg
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/docs/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2184 2013-05-03 14:59:52.000000 numba-0.8.1/docs/design_outline.txt
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/docs/ams_presentation/
--rw-rw-r--   0 mark      (1000) mark      (1000)      495 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/Makefile
--rw-rw-r--   0 mark      (1000) mark      (1000)      632 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/linregr_python.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      796 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/linregr_numba.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      683 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/linregr_numbapro.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2795 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/linregr_numbapro_cuda.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1728 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ams_presentation/linregr_bench.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3123 2013-05-03 14:59:52.000000 numba-0.8.1/docs/ctypes_support.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)     5633 2013-05-03 14:59:52.000000 numba-0.8.1/docs/Makefile
--rw-rw-r--   0 mark      (1000) mark      (1000)   677580 2013-05-03 14:59:52.000000 numba-0.8.1/docs/Fast Python.ipynb
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/docs/source/
--rw-rw-r--   0 mark      (1000) mark      (1000)     6000 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/pythonstuff.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     6593 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/arrays.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     5578 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/type_inference.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     2943 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/userguide.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      682 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/reference.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     1170 2013-05-03 15:01:06.000000 numba-0.8.1/docs/source/pycc.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     2500 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/releases.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     1005 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/index.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     2130 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/examples.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     9240 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/types.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     6459 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/interface_c.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)    24442 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/ir.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     8184 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/conf.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4634 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/architecture.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      843 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/doctest.rst
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/docs/source/modules/
--rw-rw-r--   0 mark      (1000) mark      (1000)      138 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/ast_constant_folding.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       94 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/pipeline.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       90 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/visitors.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       90 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/minivect.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       78 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/utils.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       98 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/transforms.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       94 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/functions.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       74 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/pycc.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      114 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/multiarray_api.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      130 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/ast_type_inference.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       78 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/nodes.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      110 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/ast_translate.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      118 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/ndarray_helpers.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       70 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/cfg.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       98 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/llvm_types.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       82 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/naming.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       98 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/decorators.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       54 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/numba.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       98 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/stdio_util.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       82 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/symtab.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       94 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/translate.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       86 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/modules/closure.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     9025 2013-05-03 14:59:52.000000 numba-0.8.1/docs/source/roadmap.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      950 2013-05-03 14:59:52.000000 numba-0.8.1/docs/update-release-notes.py
--rwxrwxr-x   0 mark      (1000) mark      (1000)     4374 2013-05-03 14:59:52.000000 numba-0.8.1/docs/gh-pages.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4325 2013-05-03 15:13:21.000000 numba-0.8.1/PKG-INFO
--rwxrwxr-x   0 mark      (1000) mark      (1000)      416 2013-05-03 14:59:52.000000 numba-0.8.1/runtests.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/pyextensibletype/
--rw-rw-r--   0 mark      (1000) mark      (1000)      638 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/README.rst
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/
--rw-rw-r--   0 mark      (1000) mark      (1000)      485 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/intern.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)     2463 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/extensibletype.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)     5168 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/methodtable.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)      530 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/intern.pxd
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2095 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/test_perfecthashing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      582 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/pstdint.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)     1130 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/test_interning.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       70 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/test_pstdint.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        7 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/test/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      723 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/extensibletype.pxd
--rw-rw-r--   0 mark      (1000) mark      (1000)        7 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/extensibletype/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/pyextensibletype/demo/
--rw-rw-r--   0 mark      (1000) mark      (1000)      296 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/bench.ipy
--rw-rw-r--   0 mark      (1000) mark      (1000)      192 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/provider.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)       51 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/thestandard.h
--rw-rw-r--   0 mark      (1000) mark      (1000)      453 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/setup.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      863 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/consumer.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)      446 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/customslots.pxd
--rw-rw-r--   0 mark      (1000) mark      (1000)      331 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/consumer_c_code.c
--rwxrwxr-x   0 mark      (1000) mark      (1000)       91 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/build.sh
--rw-rw-r--   0 mark      (1000) mark      (1000)      243 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/run.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4632 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/demo/provider_c_code.h
--rw-rw-r--   0 mark      (1000) mark      (1000)      107 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/.gitignore
--rw-rw-r--   0 mark      (1000) mark      (1000)     2011 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/setupconfig.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      975 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/setup.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/deps/pyextensibletype/include/
--rw-rw-r--   0 mark      (1000) mark      (1000)      152 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/siphash24.h
--rw-rw-r--   0 mark      (1000) mark      (1000)    26378 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/pstdint.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     6254 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/interning.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     6160 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/perfecthash.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     8143 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/siphash24.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     2659 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/customslots.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     2456 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/globalinterning.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     4766 2013-05-03 14:59:52.000000 numba-0.8.1/deps/pyextensibletype/include/extensibletype.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     1470 2013-05-03 14:59:52.000000 numba-0.8.1/AUTHORS
--rw-rw-r--   0 mark      (1000) mark      (1000)     7359 2013-05-03 14:59:52.000000 numba-0.8.1/setup.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5094 2013-05-03 14:59:52.000000 numba-0.8.1/gen_type_conversion.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3715 2013-05-03 14:59:52.000000 numba-0.8.1/CHANGE_LOG
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/
--rw-rw-r--   0 mark      (1000) mark      (1000)      651 2013-05-03 14:59:52.000000 numba-0.8.1/numba/missing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      417 2013-05-03 15:13:21.000000 numba-0.8.1/numba/_version.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/type_inference/
--rw-rw-r--   0 mark      (1000) mark      (1000)    64351 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/infer.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    11946 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/module_type_inference.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/type_inference/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1655 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/tests/test_user_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      983 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/tests/test_typesets.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      280 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/tests/test_extension_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7553 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/tests/test_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1823 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/infer_call.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      878 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/deferred.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/type_inference/modules/
--rw-rw-r--   0 mark      (1000) mark      (1000)    11015 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/numpymodule.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1669 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/utils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7943 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/numpyufuncs.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4537 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/mathmodule.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4087 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/builtinmodule.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      423 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/numbamodule.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      109 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/modules/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/type_inference/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/support/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/support/numpy_support/
--rw-rw-r--   0 mark      (1000) mark      (1000)     3018 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/numpy_support/slicing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5617 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/numpy_support/slicenodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8971 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/numpy_support/sliceutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      122 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/numpy_support/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4367 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/ctypes_support.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/support/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2194 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/test_ctypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      917 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/test_ctypes_gibbs.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1880 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/ctypes_values.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/support/tests/random/
--rw-rw-r--   0 mark      (1000) mark      (1000)      576 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/random/test_random_gibbs.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/random/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2857 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/cffi_support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/support/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10462 2013-05-03 14:59:52.000000 numba-0.8.1/numba/array_expressions.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    23112 2013-05-03 14:59:52.000000 numba-0.8.1/numba/closures.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/intrinsic/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1968 2013-05-03 14:59:52.000000 numba-0.8.1/numba/intrinsic/string_intrinsic.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4333 2013-05-03 14:59:52.000000 numba-0.8.1/numba/intrinsic/numba_intrinsic.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4870 2013-05-03 14:59:52.000000 numba-0.8.1/numba/intrinsic/intrinsic.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      895 2013-05-03 14:59:52.000000 numba-0.8.1/numba/intrinsic/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    40864 2013-05-03 14:59:52.000000 numba-0.8.1/numba/transforms.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/nodes/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2170 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/structnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5314 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/closurenodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3923 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/coercionnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1769 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/tempnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2056 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/constnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1623 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/llvmnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4258 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/basenodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      768 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/metadata.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1790 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/objectnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4096 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/cfnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5950 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/callnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3000 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/excnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2475 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/usernode.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1731 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/pointernodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10296 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/numpynodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      302 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/bitwise.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2397 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/extnodes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4230 2013-05-03 14:59:52.000000 numba-0.8.1/numba/nodes/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/control_flow/
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/block.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      368 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/debug.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    40261 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/control_flow.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/control_flow/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)    11233 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_circular_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2362 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_w_uninitialized_for.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      854 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_ast_cfg.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5723 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_cfg_type_infer.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1277 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_w_uninitialized_while.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2899 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_w_uninitialized.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1242 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/test_w_unreachable.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4787 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/graphviz.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6899 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/ssa.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1571 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/delete_cfnode.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6578 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/reaching.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4105 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/cfstats.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      332 2013-05-03 14:59:52.000000 numba-0.8.1/numba/control_flow/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3939 2013-05-03 14:59:52.000000 numba-0.8.1/numba/ufunc_builder.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/specialize/
--rw-rw-r--   0 mark      (1000) mark      (1000)     3775 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/mathcalls.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10565 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/loops.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4170 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/loopimpl.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1029 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/funccalls.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4267 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/comparisons.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     9504 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/exttypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5960 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/exceptions.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      109 2013-05-03 14:59:52.000000 numba-0.8.1/numba/specialize/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    14579 2013-05-03 14:59:52.000000 numba-0.8.1/numba/visitors.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7966 2013-05-03 14:59:52.000000 numba-0.8.1/numba/ad.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7891 2013-05-03 14:59:52.000000 numba-0.8.1/numba/templating.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6189 2013-05-03 14:59:52.000000 numba-0.8.1/numba/llvm_types.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7359 2013-05-03 14:59:52.000000 numba-0.8.1/numba/multiarray_api.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4868 2013-05-03 14:59:52.000000 numba-0.8.1/numba/reporting.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/pycc/
--rw-rw-r--   0 mark      (1000) mark      (1000)    14616 2013-05-03 14:59:52.000000 numba-0.8.1/numba/pycc/compiler.py
--rwxrwxr-x   0 mark      (1000) mark      (1000)     3192 2013-05-03 14:59:52.000000 numba-0.8.1/numba/pycc/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      174 2013-05-03 14:59:52.000000 numba-0.8.1/numba/pyconsts.pyx
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tools/
--rw-rw-r--   0 mark      (1000) mark      (1000)      668 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tools/astformat.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tools/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      660 2013-05-03 14:59:52.000000 numba-0.8.1/numba/naming.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3959 2013-05-03 14:59:52.000000 numba-0.8.1/numba/metadata.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3291 2013-05-03 14:59:52.000000 numba-0.8.1/numba/ndarray_helpers.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5979 2013-05-03 14:59:52.000000 numba-0.8.1/numba/scrape_multiarray_api.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2012 2013-05-03 14:59:52.000000 numba-0.8.1/numba/oset.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10615 2013-05-03 14:59:52.000000 numba-0.8.1/numba/decorators.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/containers/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/containers/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)      379 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/tests/test_typed_tuple.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4551 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/tests/test_typed_list.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1099 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/register.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2386 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/typedtuple.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3428 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/typedlist.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3282 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/orderedcontainer.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      128 2013-05-03 14:59:52.000000 numba-0.8.1/numba/containers/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/testing/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/testing/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)      369 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/tests/test_user_doctest.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      330 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/tests/test_parametrize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5510 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/test_support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1057 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/user_support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6665 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/runner.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2870 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/doctest_support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      184 2013-05-03 14:59:52.000000 numba-0.8.1/numba/testing/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1553 2013-05-03 14:59:52.000000 numba-0.8.1/numba/macros.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/codegen/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1864 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/refcounting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5682 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/llvmcontext.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8887 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/coerce.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      225 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/debug.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3181 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/complexsupport.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      995 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/globalconstants.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10357 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/llvmwrapper.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      987 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/codeutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    67592 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/translate.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/codegen/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3391 2013-05-03 14:59:52.000000 numba-0.8.1/numba/astsix.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6249 2013-05-03 14:59:52.000000 numba-0.8.1/numba/functions.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    15857 2013-05-03 14:59:52.000000 numba-0.8.1/numba/numbafunction.c
--rw-rw-r--   0 mark      (1000) mark      (1000)    28093 2013-05-03 14:59:52.000000 numba-0.8.1/numba/environment.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)      207 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_unbound_variables.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2322 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_fbcorr.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1672 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_reporting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2156 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_object_conversion.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/math_tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1108 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/math_tests/test_nopython_math.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1740 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/math_tests/test_math.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3108 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/math_tests/test_numpy_math.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/math_tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5339 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_const_folding.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1863 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_addressof.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2110 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_forces.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/issues/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1810 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_117.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      546 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_164.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      496 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_50.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      971 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_118.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      497 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_77.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      963 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_185.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      429 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_161.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1487 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_compare.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      561 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_112.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      562 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_165.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      956 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_125.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      314 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_169.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1027 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_192.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2179 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_57.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      262 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_204.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1180 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_126.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1551 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_138.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      364 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_172.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      684 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_163.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      849 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_56.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      662 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_184.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      458 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_potential_gcc_error.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      295 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/test_issue_159.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/issues/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/py2only/
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/py2only/test_print.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       35 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/py2only/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/closures/
--rw-rw-r--   0 mark      (1000) mark      (1000)     8088 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/closures/test_closure.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1012 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/closures/test_closure_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/closures/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5227 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_if.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      279 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_object_iteration.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1619 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_pycc_tresult.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/arrays/
--rw-rw-r--   0 mark      (1000) mark      (1000)      300 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/arrays/array_global.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/arrays/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      359 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_compiler_errors.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5694 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_forloop.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6105 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_while.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1955 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_extern_call.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      947 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_strings.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1448 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_print_function.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      518 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_redefine.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/np/
--rw-rw-r--   0 mark      (1000) mark      (1000)     7113 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/np/test_numpy_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4212 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/np/test_ufunc_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      893 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/np/test_numpy_calls.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1313 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/np/test_preloading.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/np/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/pointers/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1049 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/pointers/test_pointers.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      559 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/pointers/test_null.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/pointers/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1474 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_cstring.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1029 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_casting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2337 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_sum.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    12663 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_multiarray_api.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3963 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_indexing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3074 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_struct.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1070 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_ast_arrays.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1832 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_recursion.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/ops/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2228 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/ops/test_bitwise_ops.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1425 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/ops/test_unary_ops.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1610 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/ops/test_binary_ops.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/ops/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2911 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_ast_forloop.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1268 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_unsigned_arith.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3024 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_ast_getattr.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1856 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_avg2d.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1319 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_mandelbrot.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      145 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/conftest.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      753 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_dot.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/array_exprs/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1334 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_array_math.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1232 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_slicing2.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1870 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_vmdot.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2436 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_array_expressions.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3196 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_broadcasting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1547 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/test_slicing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/array_exprs/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/broken_issues/
--rw-rw-r--   0 mark      (1000) mark      (1000)      448 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/broken_issues/test_log1p_vectorize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1327 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/broken_issues/autojit_ext_method_call.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3014 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/broken_issues/test_binary_harder.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1845 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/broken_issues/test_bitwise_harder.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/broken_issues/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      598 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_object_literals.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/builtins/
--rw-rw-r--   0 mark      (1000) mark      (1000)      914 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_object_builtins.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1548 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_range.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      294 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_str.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      699 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_pow.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      714 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_round.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      404 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_float.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      501 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_complex.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      418 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_int.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1733 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/test_builtin_abs.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/builtins/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1121 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_typeof.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/foreign_call/
--rw-rw-r--   0 mark      (1000) mark      (1000)      809 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/foreign_call/test_cffi_call.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1575 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/foreign_call/test_callbacks.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1028 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/foreign_call/test_ctypes_call.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/foreign_call/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3710 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_for_in_range.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2523 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_listcomp.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      399 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_locals_override.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      567 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_globals_builtins.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5745 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_mandelbrot_2.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1782 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_filter2d.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1361 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_types.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5415 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_template_types.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      322 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_nosource.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      560 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_numbafunction.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7146 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_complex.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      632 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_exceptions.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      631 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_autojit.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1181 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_modulo.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1152 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_overflow.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3123 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_getattr.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1172 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_diffusion.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3924 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_object_counting.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/tests/vectorize/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2892 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/vectorize/test_usecase_1_1.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      591 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/vectorize/test_type_inference.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1513 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/vectorize/test_basic_vectorize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/vectorize/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      927 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_ifexp.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1483 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_issues.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      744 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_slicing.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      225 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/compile_with_pycc.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      242 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_intrinsic.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      905 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_rshift.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1237 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_withpython.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1139 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/test_tuple.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       88 2013-05-03 14:59:52.000000 numba-0.8.1/numba/_pyconsts.pxd
--rw-rw-r--   0 mark      (1000) mark      (1000)      471 2013-05-03 14:59:52.000000 numba-0.8.1/numba/_numba.pxd
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/include/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2292 2013-05-03 14:59:52.000000 numba-0.8.1/numba/include/_numba.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     2214 2013-05-03 14:59:52.000000 numba-0.8.1/numba/special.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/utility/
--rw-rw-r--   0 mark      (1000) mark      (1000)      650 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/math_utilities.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2903 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/virtuallookup.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/utility/cbuilder/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2925 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/cbuilder/refcounting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1753 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/cbuilder/library.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2165 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/cbuilder/numbacdef.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/cbuilder/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utility/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10738 2013-05-03 14:59:52.000000 numba-0.8.1/numba/ast_constant_folding.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6517 2013-05-03 14:59:52.000000 numba-0.8.1/numba/utils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7955 2013-05-03 14:59:52.000000 numba-0.8.1/numba/annotate.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/minivect/
--rw-rw-r--   0 mark      (1000) mark      (1000)    50407 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/miniast.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1821 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/type_promoter.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/minivect/pydot/
--rw-rw-r--   0 mark      (1000) mark      (1000)    57621 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/pydot/pydot.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/pydot/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    36865 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/minitypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1045 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/minierror.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6325 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/minivisitor.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/minivect/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)      995 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/llvm_testutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1856 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/test_specializations.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2100 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/test_hoisting.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1692 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/test_operators.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1785 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/testutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2972 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/graphviz.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/minivect/include/
--rw-rw-r--   0 mark      (1000) mark      (1000)     5944 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/include/miniutils.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     4263 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/include/miniutils.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)     7682 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/treepath.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2703 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/xmldumper.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8917 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/optimize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4118 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/ctypes_conversion.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2355 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/complex_support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    14134 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/codegen.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5393 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/minicode.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    17877 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/llvm_codegen.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4805 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/miniutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    57119 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/specializers.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      211 2013-05-03 14:59:52.000000 numba-0.8.1/numba/minivect/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1241 2013-05-03 14:59:52.000000 numba-0.8.1/numba/error.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    20213 2013-05-03 14:59:52.000000 numba-0.8.1/numba/pipeline.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3588 2013-05-03 14:59:52.000000 numba-0.8.1/numba/optimize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1189 2013-05-03 14:59:52.000000 numba-0.8.1/numba/traits.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1741 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/asdl.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    10063 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/schema.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)     1562 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/tests/test_good.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      463 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/tests/support.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2726 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/tests/test_bad.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/tests/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/py3_3/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4562 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py3_3/Python.asdl
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py3_3/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/py2_7/
--rw-rw-r--   0 mark      (1000) mark      (1000)    12446 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py2_7/asdl.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4330 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py2_7/Python.asdl
--rw-rw-r--   0 mark      (1000) mark      (1000)    27042 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py2_7/spark.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py2_7/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/common/
--rw-rw-r--   0 mark      (1000) mark      (1000)    13170 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/common/asdl.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4330 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/common/Python.asdl
--rw-rw-r--   0 mark      (1000) mark      (1000)    27001 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/common/spark.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/common/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/asdl/py3_2/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4343 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py3_2/Python.asdl
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/py3_2/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/asdl/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/typesystem/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2668 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/typeutils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8257 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/templatetypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2031 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/shorthands.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3096 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/containertypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1412 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/closuretypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      741 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/typematch.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    24597 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/ssatypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    11610 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/basetypes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3737 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/typeset.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7261 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/typemapper.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      599 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typesystem/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     9451 2013-05-03 14:59:52.000000 numba-0.8.1/numba/symtab.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      335 2013-05-03 14:59:52.000000 numba-0.8.1/numba/numbafunction.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     5427 2013-05-03 14:59:52.000000 numba-0.8.1/numba/_ext.c
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/exttypes/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/exttypes/types/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2548 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/types/extensiontype.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1972 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/types/methods.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      188 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/types/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5484 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/validators.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3128 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/methodtable.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2085 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/autojitmeta.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2951 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/ordering.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2660 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/attributetable.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    11998 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/extension_types.pyx
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/exttypes/tests/
--rw-rw-r--   0 mark      (1000) mark      (1000)     2756 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_methods.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3895 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_types.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3048 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_inheritance.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/exttypes/tests/autojit/
--rw-rw-r--   0 mark      (1000) mark      (1000)      573 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/autojit/test_extension_class_specializations.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2165 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/autojit/test_unspecialized_extension_methods.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2489 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/autojit/test_unannotated_extension_methods.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/autojit/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1480 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_attributes.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1461 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_type_recognition.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      963 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_sizeof.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      492 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_extension_warnings.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2518 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/test_vtables.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/tests/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1249 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/entrypoints.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      957 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/utils.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    15452 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/autojitclass.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8395 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/signatures.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    13818 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/compileclass.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      759 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/variable.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5739 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/virtual.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     3626 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/jitclass.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       52 2013-05-03 14:59:52.000000 numba-0.8.1/numba/exttypes/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     5040 2013-05-03 14:59:52.000000 numba-0.8.1/numba/normalize.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1646 2013-05-03 14:59:52.000000 numba-0.8.1/numba/typedefs.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/random/
--rw-rw-r--   0 mark      (1000) mark      (1000)     8571 2013-05-03 14:59:52.000000 numba-0.8.1/numba/random/_rng_generated.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     8450 2013-05-03 14:59:52.000000 numba-0.8.1/numba/random/__generate_rng.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2373 2013-05-03 14:59:52.000000 numba-0.8.1/numba/random/random.py
--rw-rw-r--   0 mark      (1000) mark      (1000)       22 2013-05-03 14:59:52.000000 numba-0.8.1/numba/random/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/vectorize/
--rw-rw-r--   0 mark      (1000) mark      (1000)     7380 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/_gufunc.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     6595 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/_common.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1838 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/_internal.h
--rw-rw-r--   0 mark      (1000) mark      (1000)     2313 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/basic.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     7441 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/_internal.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     6647 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/_ufunc.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     2350 2013-05-03 14:59:52.000000 numba-0.8.1/numba/vectorize/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     4318 2013-05-03 14:59:52.000000 numba-0.8.1/numba/odict.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1501 2013-05-03 14:59:52.000000 numba-0.8.1/numba/function_util.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/wrapping/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4143 2013-05-03 14:59:52.000000 numba-0.8.1/numba/wrapping/compiler.py
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-03 14:59:52.000000 numba-0.8.1/numba/wrapping/__init__.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/external/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-05-03 15:13:21.000000 numba-0.8.1/numba/external/utilities/
--rw-rw-r--   0 mark      (1000) mark      (1000)      872 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/utilities/virtuallookup.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     1627 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/utilities/utilities.c
--rw-rw-r--   0 mark      (1000) mark      (1000)     8530 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/utilities/type_conversion.c
--rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/utilities/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2889 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/external.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     6727 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/pyapi.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     1127 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/libc.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2659 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/utility.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      698 2013-05-03 14:59:52.000000 numba-0.8.1/numba/external/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2384 2013-05-03 14:59:52.000000 numba-0.8.1/numba/stdio_util.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    12156 2013-05-03 14:59:52.000000 numba-0.8.1/numba/numbawrapper.pyx
--rw-rw-r--   0 mark      (1000) mark      (1000)     3049 2013-05-03 14:59:52.000000 numba-0.8.1/numba/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      415 2013-05-03 14:59:52.000000 numba-0.8.1/getfailed.py
--rw-rw-r--   0 mark      (1000) mark      (1000)     2946 2013-05-03 14:59:52.000000 numba-0.8.1/README.md
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    25596 2013-05-29 10:02:25.000000 numba-0.9.0/versioneer.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       60 2013-05-29 10:02:25.000000 numba-0.9.0/requirements.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)      237 2013-05-29 10:02:25.000000 numba-0.9.0/setup.cfg
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/docs/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2184 2013-05-29 10:02:25.000000 numba-0.9.0/docs/design_outline.txt
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/docs/ams_presentation/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      495 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/Makefile
+-rw-rw-r--   0 mark      (1000) mark      (1000)      632 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/linregr_python.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      796 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/linregr_numba.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      683 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/linregr_numbapro.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2795 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/linregr_numbapro_cuda.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1728 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ams_presentation/linregr_bench.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3123 2013-05-29 10:02:25.000000 numba-0.9.0/docs/ctypes_support.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6004 2013-05-30 21:45:41.000000 numba-0.9.0/docs/Makefile
+-rw-rw-r--   0 mark      (1000) mark      (1000)   677580 2013-05-29 10:02:25.000000 numba-0.9.0/docs/Fast Python.ipynb
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/docs/source/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6000 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/pythonstuff.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     9292 2013-05-30 21:45:41.000000 numba-0.9.0/docs/source/arrays.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5578 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/type_inference.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2943 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/userguide.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1172 2013-05-30 21:45:28.000000 numba-0.9.0/docs/source/pycc.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2500 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/releases.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1011 2013-05-30 21:45:41.000000 numba-0.9.0/docs/source/index.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2130 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/examples.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     9240 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/types.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6459 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/interface_c.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)    21912 2013-05-30 21:45:41.000000 numba-0.9.0/docs/source/ir.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8184 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/conf.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4634 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/architecture.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)      843 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/doctest.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     9025 2013-05-29 10:02:25.000000 numba-0.9.0/docs/source/roadmap.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)      592 2013-05-30 21:45:41.000000 numba-0.9.0/docs/make_toc.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      950 2013-05-29 10:02:25.000000 numba-0.9.0/docs/update-release-notes.py
+-rwxrwxr-x   0 mark      (1000) mark      (1000)     4374 2013-05-29 10:02:25.000000 numba-0.9.0/docs/gh-pages.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4325 2013-06-04 10:15:49.000000 numba-0.9.0/PKG-INFO
+-rwxrwxr-x   0 mark      (1000) mark      (1000)      416 2013-06-04 10:10:31.000000 numba-0.9.0/runtests.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/pyextensibletype/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      638 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/README.rst
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      485 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/intern.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2463 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/extensibletype.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5168 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/methodtable.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)      530 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/intern.pxd
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2095 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/test_perfecthashing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      582 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/pstdint.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1130 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/test_interning.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       70 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/test_pstdint.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        7 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/test/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      723 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/extensibletype.pxd
+-rw-rw-r--   0 mark      (1000) mark      (1000)        7 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/extensibletype/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/pyextensibletype/demo/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      296 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/bench.ipy
+-rw-rw-r--   0 mark      (1000) mark      (1000)      192 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/provider.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)       51 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/thestandard.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)      453 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/setup.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      863 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/consumer.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)      446 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/customslots.pxd
+-rw-rw-r--   0 mark      (1000) mark      (1000)      331 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/consumer_c_code.c
+-rwxrwxr-x   0 mark      (1000) mark      (1000)       91 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/build.sh
+-rw-rw-r--   0 mark      (1000) mark      (1000)      243 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/run.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4632 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/demo/provider_c_code.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)      107 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/.gitignore
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2011 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/setupconfig.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      975 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/setup.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/deps/pyextensibletype/include/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      152 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/siphash24.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)    26378 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/pstdint.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6254 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/interning.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6160 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/perfecthash.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8143 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/siphash24.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2659 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/customslots.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2456 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/globalinterning.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4766 2013-05-29 10:02:25.000000 numba-0.9.0/deps/pyextensibletype/include/extensibletype.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1470 2013-05-29 10:02:25.000000 numba-0.9.0/AUTHORS
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7540 2013-05-31 09:23:28.000000 numba-0.9.0/setup.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5094 2013-05-29 10:02:25.000000 numba-0.9.0/gen_type_conversion.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3715 2013-05-29 10:02:25.000000 numba-0.9.0/CHANGE_LOG
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      651 2013-05-29 10:02:25.000000 numba-0.9.0/numba/missing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      417 2013-06-04 10:15:49.000000 numba-0.9.0/numba/_version.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/type_inference/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    63782 2013-06-04 10:10:31.000000 numba-0.9.0/numba/type_inference/infer.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    12070 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/module_type_inference.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/type_inference/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1673 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/tests/test_user_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      989 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/tests/test_typesets.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      280 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/tests/test_extension_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7619 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/tests/test_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1816 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/infer_call.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      878 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/deferred.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/type_inference/modules/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    11022 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/modules/numpymodule.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1669 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/modules/utils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7981 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/modules/numpyufuncs.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4713 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/modules/mathmodule.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4119 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/modules/builtinmodule.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      345 2013-05-31 09:23:28.000000 numba-0.9.0/numba/type_inference/modules/numbamodule.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      109 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/modules/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/type_inference/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/support/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/support/numpy_support/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3013 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/numpy_support/slicing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5577 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/numpy_support/slicenodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8877 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/numpy_support/sliceutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      122 2013-05-29 10:02:25.000000 numba-0.9.0/numba/support/numpy_support/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3645 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/ctypes_support.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/support/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2046 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/tests/test_ctypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      917 2013-05-29 10:02:25.000000 numba-0.9.0/numba/support/tests/test_ctypes_gibbs.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1880 2013-05-29 10:02:25.000000 numba-0.9.0/numba/support/tests/ctypes_values.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/support/tests/test_random/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      576 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/tests/test_random/test_random_gibbs.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/tests/test_random/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-29 10:02:25.000000 numba-0.9.0/numba/support/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2758 2013-05-31 09:23:28.000000 numba-0.9.0/numba/support/cffi_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/support/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    12200 2013-05-31 09:23:28.000000 numba-0.9.0/numba/array_expressions.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    22966 2013-05-31 09:23:28.000000 numba-0.9.0/numba/closures.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/intrinsic/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1950 2013-05-31 09:23:28.000000 numba-0.9.0/numba/intrinsic/string_intrinsic.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4333 2013-05-29 10:02:25.000000 numba-0.9.0/numba/intrinsic/numba_intrinsic.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4754 2013-05-31 09:23:28.000000 numba-0.9.0/numba/intrinsic/intrinsic.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      895 2013-05-29 10:02:25.000000 numba-0.9.0/numba/intrinsic/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    40155 2013-06-04 10:10:31.000000 numba-0.9.0/numba/transforms.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/nodes/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2170 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/structnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5314 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/closurenodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3923 2013-06-02 20:31:08.000000 numba-0.9.0/numba/nodes/coercionnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1769 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/tempnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1409 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/constnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1623 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/llvmnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4258 2013-05-29 10:09:37.000000 numba-0.9.0/numba/nodes/basenodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      768 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/metadata.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1814 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/objectnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4096 2013-05-29 10:09:37.000000 numba-0.9.0/numba/nodes/cfnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5506 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/callnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3001 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/excnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2475 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/usernode.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1731 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/pointernodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10348 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/numpynodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      302 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/bitwise.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2397 2013-05-29 10:02:25.000000 numba-0.9.0/numba/nodes/extnodes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4083 2013-05-31 09:23:28.000000 numba-0.9.0/numba/nodes/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/control_flow/
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:09:37.000000 numba-0.9.0/numba/control_flow/block.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      368 2013-05-29 10:55:20.000000 numba-0.9.0/numba/control_flow/debug.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    40320 2013-05-31 09:23:28.000000 numba-0.9.0/numba/control_flow/control_flow.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/control_flow/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    11043 2013-05-31 09:23:28.000000 numba-0.9.0/numba/control_flow/tests/test_circular_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2362 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/tests/test_w_uninitialized_for.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      839 2013-05-31 09:23:28.000000 numba-0.9.0/numba/control_flow/tests/test_ast_cfg.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5686 2013-06-04 10:10:31.000000 numba-0.9.0/numba/control_flow/tests/test_cfg_type_infer.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1277 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/tests/test_w_uninitialized_while.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2899 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/tests/test_w_uninitialized.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1242 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/tests/test_w_unreachable.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4787 2013-05-29 10:09:37.000000 numba-0.9.0/numba/control_flow/graphviz.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6899 2013-05-29 15:13:14.000000 numba-0.9.0/numba/control_flow/ssa.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1571 2013-05-29 10:04:13.000000 numba-0.9.0/numba/control_flow/delete_cfnode.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6480 2013-05-31 09:23:28.000000 numba-0.9.0/numba/control_flow/reaching.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4105 2013-05-29 10:55:20.000000 numba-0.9.0/numba/control_flow/cfstats.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      332 2013-06-04 10:10:31.000000 numba-0.9.0/numba/control_flow/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4377 2013-05-31 09:23:28.000000 numba-0.9.0/numba/ufunc_builder.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/specialize/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10449 2013-05-31 09:23:28.000000 numba-0.9.0/numba/specialize/loops.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4168 2013-05-31 09:23:28.000000 numba-0.9.0/numba/specialize/loopimpl.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      916 2013-06-04 10:10:31.000000 numba-0.9.0/numba/specialize/funccalls.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4294 2013-05-31 09:23:28.000000 numba-0.9.0/numba/specialize/comparisons.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     9566 2013-05-31 09:23:28.000000 numba-0.9.0/numba/specialize/exttypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5867 2013-05-31 09:23:28.000000 numba-0.9.0/numba/specialize/exceptions.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      109 2013-05-29 10:02:25.000000 numba-0.9.0/numba/specialize/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    14586 2013-06-04 10:10:31.000000 numba-0.9.0/numba/visitors.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7966 2013-05-29 10:02:25.000000 numba-0.9.0/numba/ad.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7891 2013-05-29 10:02:25.000000 numba-0.9.0/numba/templating.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6999 2013-05-31 09:23:28.000000 numba-0.9.0/numba/llvm_types.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7359 2013-05-29 10:02:25.000000 numba-0.9.0/numba/multiarray_api.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5093 2013-05-30 21:45:41.000000 numba-0.9.0/numba/reporting.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/pycc/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    15454 2013-06-04 10:10:31.000000 numba-0.9.0/numba/pycc/compiler.py
+-rwxrwxr-x   0 mark      (1000) mark      (1000)     3192 2013-05-29 10:02:25.000000 numba-0.9.0/numba/pycc/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      174 2013-05-29 10:02:25.000000 numba-0.9.0/numba/pyconsts.pyx
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tools/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      668 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tools/astformat.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tools/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      660 2013-05-29 10:02:25.000000 numba-0.9.0/numba/naming.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3962 2013-05-31 09:23:28.000000 numba-0.9.0/numba/metadata.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3260 2013-05-31 09:23:28.000000 numba-0.9.0/numba/ndarray_helpers.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5979 2013-05-29 10:02:25.000000 numba-0.9.0/numba/scrape_multiarray_api.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2012 2013-05-29 10:02:25.000000 numba-0.9.0/numba/oset.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10822 2013-05-31 09:23:28.000000 numba-0.9.0/numba/decorators.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/containers/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/containers/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      379 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/tests/test_typed_tuple.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5097 2013-05-30 21:45:28.000000 numba-0.9.0/numba/containers/tests/test_typed_list.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1099 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/register.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2386 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/typedtuple.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4484 2013-05-31 09:23:28.000000 numba-0.9.0/numba/containers/typedlist.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3282 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/orderedcontainer.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      128 2013-05-29 10:02:25.000000 numba-0.9.0/numba/containers/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/testing/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/testing/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      369 2013-05-29 10:02:25.000000 numba-0.9.0/numba/testing/tests/test_user_doctest.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      330 2013-05-29 10:02:25.000000 numba-0.9.0/numba/testing/tests/test_parametrize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/testing/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5497 2013-05-31 09:23:28.000000 numba-0.9.0/numba/testing/test_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1057 2013-05-29 10:02:25.000000 numba-0.9.0/numba/testing/user_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6665 2013-06-04 10:10:31.000000 numba-0.9.0/numba/testing/runner.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2870 2013-05-29 10:02:25.000000 numba-0.9.0/numba/testing/doctest_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      184 2013-05-29 10:09:37.000000 numba-0.9.0/numba/testing/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1548 2013-05-31 09:23:28.000000 numba-0.9.0/numba/macros.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/codegen/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1864 2013-05-29 10:02:25.000000 numba-0.9.0/numba/codegen/refcounting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6525 2013-05-31 09:23:28.000000 numba-0.9.0/numba/codegen/llvmcontext.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8468 2013-05-31 09:23:28.000000 numba-0.9.0/numba/codegen/coerce.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      225 2013-05-30 14:16:03.000000 numba-0.9.0/numba/codegen/debug.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3181 2013-05-29 10:02:25.000000 numba-0.9.0/numba/codegen/complexsupport.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      995 2013-05-29 10:02:25.000000 numba-0.9.0/numba/codegen/globalconstants.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10365 2013-06-04 10:10:31.000000 numba-0.9.0/numba/codegen/llvmwrapper.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      987 2013-05-29 10:02:25.000000 numba-0.9.0/numba/codegen/codeutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    68180 2013-06-04 10:10:31.000000 numba-0.9.0/numba/codegen/translate.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/codegen/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3391 2013-05-29 10:02:25.000000 numba-0.9.0/numba/astsix.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6238 2013-05-31 09:23:28.000000 numba-0.9.0/numba/functions.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    15857 2013-05-29 10:02:25.000000 numba-0.9.0/numba/numbafunction.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)    28982 2013-06-04 10:10:31.000000 numba-0.9.0/numba/environment.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      207 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_unbound_variables.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2322 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_fbcorr.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2370 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_reporting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2056 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_object_conversion.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/math_tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1108 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/math_tests/test_nopython_math.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3761 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/math_tests/test_allmath.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7376 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/math_tests/test_complex.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2020 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/math_tests/test_math.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3047 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/math_tests/test_numpy_math.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/math_tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5329 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_const_folding.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1865 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_addressof.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2110 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_forces.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/issues/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      423 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_215.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1810 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_117.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      546 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_164.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      496 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_50.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      968 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/issues/test_issue_118.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      497 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_77.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      963 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_185.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      267 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_198.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      465 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_161.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1455 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/issues/test_compare.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      558 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/issues/test_issue_112.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      562 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_165.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      956 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_125.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      372 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_212.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      426 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_216.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      314 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_169.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1027 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_192.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2253 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/issues/test_issue_57.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      352 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_204.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1180 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_126.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1551 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_138.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      364 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_172.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      704 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/issues/test_issue_163.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      849 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_56.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      675 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/issues/test_issue_184.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      458 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_potential_gcc_error.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      295 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/test_issue_159.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/issues/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/py2only/
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/py2only/test_print.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       35 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/py2only/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/closures/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7280 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/closures/test_closure.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1032 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/closures/test_closure_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/closures/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5227 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_if.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      279 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_object_iteration.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1755 2013-06-04 10:10:31.000000 numba-0.9.0/numba/tests/test_pycc_tresult.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/arrays/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      300 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/arrays/array_global.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/arrays/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5694 2013-05-29 10:09:37.000000 numba-0.9.0/numba/tests/test_forloop.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6104 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_while.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1955 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_extern_call.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      947 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_strings.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1453 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_print_function.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      518 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_redefine.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/np/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7077 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/np/test_numpy_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4141 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/np/test_ufunc_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      893 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/np/test_numpy_calls.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1311 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/np/test_preloading.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/np/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/pointers/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1049 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/pointers/test_pointers.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      559 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/pointers/test_null.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       20 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/pointers/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1468 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_cstring.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2337 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_sum.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    12663 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_multiarray_api.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3963 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_indexing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3089 2013-06-04 10:10:31.000000 numba-0.9.0/numba/tests/test_struct.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1070 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_ast_arrays.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1832 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_recursion.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/ops/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2291 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/ops/test_bitwise_ops.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1425 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/ops/test_unary_ops.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1610 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/ops/test_binary_ops.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/ops/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2788 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_ast_forloop.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1268 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_unsigned_arith.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3024 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_ast_getattr.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1856 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_avg2d.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1319 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_mandelbrot.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      145 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/conftest.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      753 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_dot.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/array_exprs/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1334 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/test_array_math.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1232 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/test_slicing2.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1870 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/test_vmdot.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2436 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/test_array_expressions.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3166 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/array_exprs/test_broadcasting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1547 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/test_slicing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/array_exprs/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/broken_issues/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      448 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/broken_issues/test_log1p_vectorize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1327 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/broken_issues/autojit_ext_method_call.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3014 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/broken_issues/test_binary_harder.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1845 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/broken_issues/test_bitwise_harder.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/broken_issues/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      598 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_object_literals.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/builtins/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      878 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/builtins/test_object_builtins.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1548 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_range.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      294 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_str.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      743 2013-06-04 10:10:31.000000 numba-0.9.0/numba/tests/builtins/test_builtin_pow.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      714 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_round.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      404 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_float.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      501 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_complex.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      418 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_int.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1733 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/test_builtin_abs.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/builtins/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/tests/foreign_call/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      809 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/foreign_call/test_cffi_call.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1575 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/foreign_call/test_callbacks.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1028 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/foreign_call/test_ctypes_call.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/foreign_call/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3710 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_for_in_range.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2541 2013-05-30 21:45:41.000000 numba-0.9.0/numba/tests/test_listcomp.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      399 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_locals_override.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      530 2013-05-31 09:23:28.000000 numba-0.9.0/numba/tests/test_globals_builtins.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5745 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_mandelbrot_2.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1782 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_filter2d.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1361 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_types.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      322 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_nosource.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      560 2013-05-29 14:36:49.000000 numba-0.9.0/numba/tests/test_numbafunction.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      632 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_exceptions.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      631 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_autojit.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1181 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_modulo.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1152 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_overflow.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3123 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_getattr.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1172 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_diffusion.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3924 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_object_counting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      927 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_ifexp.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1483 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_issues.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      744 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_slicing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      225 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/compile_with_pycc.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      242 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_intrinsic.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      905 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_rshift.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1237 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_withpython.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1139 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/test_tuple.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       88 2013-05-29 10:02:25.000000 numba-0.9.0/numba/_pyconsts.pxd
+-rw-rw-r--   0 mark      (1000) mark      (1000)      471 2013-05-29 10:02:25.000000 numba-0.9.0/numba/_numba.pxd
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/include/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2292 2013-05-29 10:02:25.000000 numba-0.9.0/numba/include/_numba.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2146 2013-05-31 09:23:28.000000 numba-0.9.0/numba/special.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/utility/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      650 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/math_utilities.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2903 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/virtuallookup.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/utility/cbuilder/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2925 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/cbuilder/refcounting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1753 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/cbuilder/library.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2165 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/cbuilder/numbacdef.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/cbuilder/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/utility/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10738 2013-05-29 10:02:25.000000 numba-0.9.0/numba/ast_constant_folding.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7748 2013-05-31 09:23:28.000000 numba-0.9.0/numba/utils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7955 2013-06-04 10:10:31.000000 numba-0.9.0/numba/annotate.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/minivect/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    50428 2013-05-31 09:23:28.000000 numba-0.9.0/numba/minivect/miniast.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1821 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/type_promoter.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/minivect/pydot/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    57621 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/pydot/pydot.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/pydot/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    36861 2013-06-04 10:10:31.000000 numba-0.9.0/numba/minivect/minitypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1045 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/minierror.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6325 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/minivisitor.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/minivect/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      995 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/llvm_testutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1856 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/test_specializations.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2100 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/test_hoisting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1692 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/test_operators.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1785 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/testutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2972 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/graphviz.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/minivect/include/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5944 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/include/miniutils.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4263 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/include/miniutils.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7682 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/treepath.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2703 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/xmldumper.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8917 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/optimize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4118 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/ctypes_conversion.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2263 2013-06-04 10:10:31.000000 numba-0.9.0/numba/minivect/complex_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    14134 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/codegen.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5393 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/minicode.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    18080 2013-05-31 09:23:28.000000 numba-0.9.0/numba/minivect/llvm_codegen.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4831 2013-05-31 09:23:28.000000 numba-0.9.0/numba/minivect/miniutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    57119 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/specializers.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      211 2013-05-29 10:02:25.000000 numba-0.9.0/numba/minivect/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1518 2013-05-31 09:23:28.000000 numba-0.9.0/numba/error.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/ir/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      698 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/build.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/ir/generator/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2262 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/classgen.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6820 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/visitorgen.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5615 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/build.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      155 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/naming.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1188 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/formatting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6046 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/astgen.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/ir/generator/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      409 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/tests/testschema1.asdl
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2377 2013-06-04 10:10:31.000000 numba-0.9.0/numba/ir/generator/tests/test_build.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2944 2013-06-04 10:10:31.000000 numba-0.9.0/numba/ir/generator/tests/test_visitors.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2287 2013-06-04 10:10:31.000000 numba-0.9.0/numba/ir/generator/tests/test_astgen.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      680 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/tests/testutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6949 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/generator.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/generator/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-30 21:45:41.000000 numba-0.9.0/numba/ir/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    20397 2013-06-04 10:10:31.000000 numba-0.9.0/numba/pipeline.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1062 2013-05-31 09:23:28.000000 numba-0.9.0/numba/postpasses.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3588 2013-05-29 15:13:14.000000 numba-0.9.0/numba/optimize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1189 2013-06-04 10:10:31.000000 numba-0.9.0/numba/traits.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5420 2013-05-30 21:45:41.000000 numba-0.9.0/numba/asdl/asdl.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    11109 2013-05-30 21:45:41.000000 numba-0.9.0/numba/asdl/schema.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3833 2013-05-30 21:45:41.000000 numba-0.9.0/numba/asdl/processor.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1562 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/tests/test_good.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      463 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/tests/support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2726 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/tests/test_bad.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/tests/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/py3_3/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4562 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py3_3/Python.asdl
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py3_3/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/py2_7/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    12446 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py2_7/asdl.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4330 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py2_7/Python.asdl
+-rw-rw-r--   0 mark      (1000) mark      (1000)    27042 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py2_7/spark.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py2_7/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/common/
+-rw-rw-r--   0 mark      (1000) mark      (1000)    13170 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/common/asdl.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4330 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/common/Python.asdl
+-rw-rw-r--   0 mark      (1000) mark      (1000)    27001 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/common/spark.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/common/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/asdl/py3_2/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4343 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py3_2/Python.asdl
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/py3_2/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/asdl/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/typesystem/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2644 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/typeutils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4274 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/lowering.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5830 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/promotion.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8129 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/templatetypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    20730 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/types.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1650 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/ctypestypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1640 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/defaults.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1162 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/closuretypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      701 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/kinds.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/typesystem/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1029 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_casting.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2012 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_consing.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      937 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_type_constructors.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4172 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_conversion.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1251 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_typeof.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5492 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_template_types.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      400 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/test_type_properties.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2788 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/universe.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      705 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/typematch.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    25347 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/ssatypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2086 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/llvmtypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4279 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/numbatypes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    10490 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/itypesystem.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6941 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/constants.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3195 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/numpy_support.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      744 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/tbaa.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3742 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/typeset.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      516 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typesystem/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     9421 2013-05-31 09:23:28.000000 numba-0.9.0/numba/symtab.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      335 2013-05-29 10:02:25.000000 numba-0.9.0/numba/numbafunction.h
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5427 2013-05-29 10:02:25.000000 numba-0.9.0/numba/_ext.c
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/exttypes/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/exttypes/types/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2493 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/types/extensiontype.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1853 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/types/methods.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      178 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/types/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5484 2013-05-29 10:09:37.000000 numba-0.9.0/numba/exttypes/validators.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3128 2013-05-29 10:09:37.000000 numba-0.9.0/numba/exttypes/methodtable.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2085 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/autojitmeta.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2951 2013-05-29 10:09:37.000000 numba-0.9.0/numba/exttypes/ordering.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2646 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/attributetable.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    11998 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/extension_types.pyx
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/exttypes/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2756 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_extension_methods.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3895 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_extension_types.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3015 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/tests/test_extension_inheritance.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/exttypes/tests/autojit/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      573 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/autojit/test_extension_class_specializations.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2165 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/autojit/test_unspecialized_extension_methods.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2489 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/autojit/test_unannotated_extension_methods.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/autojit/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1480 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_extension_attributes.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1461 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_type_recognition.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      963 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_extension_sizeof.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      492 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/test_extension_warnings.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2511 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/tests/test_vtables.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1249 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/entrypoints.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      957 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/utils.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    15368 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/autojitclass.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8334 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/signatures.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    13825 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/compileclass.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      759 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/variable.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5686 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/virtual.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3671 2013-05-31 09:23:28.000000 numba-0.9.0/numba/exttypes/jitclass.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       52 2013-05-29 10:02:25.000000 numba-0.9.0/numba/exttypes/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     5775 2013-06-04 10:10:31.000000 numba-0.9.0/numba/normalize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1671 2013-05-31 09:23:28.000000 numba-0.9.0/numba/typedefs.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/random/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8571 2013-05-29 10:02:25.000000 numba-0.9.0/numba/random/_rng_generated.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8450 2013-05-29 10:02:25.000000 numba-0.9.0/numba/random/__generate_rng.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2373 2013-05-29 10:02:25.000000 numba-0.9.0/numba/random/random.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)       22 2013-05-29 10:02:25.000000 numba-0.9.0/numba/random/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/vectorize/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7380 2013-05-29 10:02:25.000000 numba-0.9.0/numba/vectorize/_gufunc.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6550 2013-05-31 09:23:28.000000 numba-0.9.0/numba/vectorize/_common.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1838 2013-05-29 10:02:25.000000 numba-0.9.0/numba/vectorize/_internal.h
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/vectorize/tests/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2892 2013-05-30 21:45:41.000000 numba-0.9.0/numba/vectorize/tests/test_usecase_1_1.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2436 2013-05-31 09:23:28.000000 numba-0.9.0/numba/vectorize/tests/test_gufunc.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      591 2013-05-30 21:45:41.000000 numba-0.9.0/numba/vectorize/tests/test_type_inference.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1513 2013-05-30 21:45:41.000000 numba-0.9.0/numba/vectorize/tests/test_basic_vectorize.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-30 21:45:41.000000 numba-0.9.0/numba/vectorize/tests/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2313 2013-05-29 10:02:25.000000 numba-0.9.0/numba/vectorize/basic.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7441 2013-05-29 10:02:25.000000 numba-0.9.0/numba/vectorize/_internal.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6647 2013-05-29 10:02:25.000000 numba-0.9.0/numba/vectorize/_ufunc.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8438 2013-05-31 09:23:28.000000 numba-0.9.0/numba/vectorize/gufunc.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2315 2013-05-30 21:45:41.000000 numba-0.9.0/numba/vectorize/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4318 2013-05-29 10:02:25.000000 numba-0.9.0/numba/odict.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1466 2013-05-31 09:23:28.000000 numba-0.9.0/numba/function_util.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/wrapping/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4200 2013-05-31 09:23:28.000000 numba-0.9.0/numba/wrapping/compiler.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2013-05-29 10:02:25.000000 numba-0.9.0/numba/wrapping/__init__.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/external/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2013-06-04 10:15:49.000000 numba-0.9.0/numba/external/utilities/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      872 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/utilities/virtuallookup.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1627 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/utilities/utilities.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)     8530 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/utilities/type_conversion.c
+-rw-rw-r--   0 mark      (1000) mark      (1000)       89 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/utilities/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2841 2013-05-31 09:23:28.000000 numba-0.9.0/numba/external/external.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6794 2013-05-31 09:23:28.000000 numba-0.9.0/numba/external/pyapi.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1159 2013-05-31 09:23:28.000000 numba-0.9.0/numba/external/libc.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2659 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/utility.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      698 2013-05-29 10:02:25.000000 numba-0.9.0/numba/external/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2384 2013-05-29 10:02:25.000000 numba-0.9.0/numba/stdio_util.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    12158 2013-05-31 09:23:28.000000 numba-0.9.0/numba/numbawrapper.pyx
+-rw-rw-r--   0 mark      (1000) mark      (1000)     3167 2013-05-31 09:23:28.000000 numba-0.9.0/numba/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      415 2013-05-29 10:02:25.000000 numba-0.9.0/getfailed.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2946 2013-05-29 10:02:25.000000 numba-0.9.0/README.md
```

### Comparing `numba-0.8.1/versioneer.py` & `numba-0.9.0/versioneer.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/design_outline.txt` & `numba-0.9.0/docs/design_outline.txt`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ams_presentation/linregr_python.py` & `numba-0.9.0/docs/ams_presentation/linregr_python.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ams_presentation/linregr_numba.py` & `numba-0.9.0/docs/ams_presentation/linregr_numba.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ams_presentation/linregr_numbapro.py` & `numba-0.9.0/docs/ams_presentation/linregr_numbapro.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ams_presentation/linregr_numbapro_cuda.py` & `numba-0.9.0/docs/ams_presentation/linregr_numbapro_cuda.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ams_presentation/linregr_bench.py` & `numba-0.9.0/docs/ams_presentation/linregr_bench.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/ctypes_support.txt` & `numba-0.9.0/docs/ctypes_support.txt`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/Makefile` & `numba-0.9.0/docs/Makefile`

 * *Files 7% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 # Makefile for Sphinx documentation
 #
 
 # You can set these variables from the command line.
 SPHINXOPTS    =
 SPHINXBUILD   = sphinx-build
+SPHINXAPI     = sphinx-apidoc
 PAPER         =
 BUILDDIR      = _build
 SRCDIR        = source
 
 # Internal variables.
 PAPEROPT_a4     = -D latex_paper_size=a4
 PAPEROPT_letter = -D latex_paper_size=letter
@@ -38,15 +39,28 @@
 	@echo "  changes    to make an overview of all changed/added/deprecated items"
 	@echo "  linkcheck  to check all external links for integrity"
 	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
 
 clean:
 	-rm -rf $(BUILDDIR)/*
 
+api:
+	-rm -rf source/modules
+	$(SPHINXAPI) --no-toc -o source/modules ../numba
+	-rm -rf source/modules/*.tests.*
+	-rm -rf source/modules/numba.minivect.*
+	-rm -rf source/modules/numba.ir.*
+	-rm -rf source/modules/numba.asdl.*
+	-rm -rf source/modules/numba.pyextensibletype.*
+	python make_toc.py
+
 html:
+	@echo "RUN 'make api' first!"
+	@echo
+	@echo
 	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
 	@echo
 	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
 
 dirhtml:
 	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
 	@echo
```

### Comparing `numba-0.8.1/docs/Fast Python.ipynb` & `numba-0.9.0/docs/Fast Python.ipynb`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/pythonstuff.rst` & `numba-0.9.0/docs/source/pythonstuff.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/arrays.rst` & `numba-0.9.0/docs/source/arrays.rst`

 * *Files 25% similar despite different names*

```diff
@@ -210,7 +210,84 @@
     def sinc(x):
         if x == 0.0:
             return 1.0
         else:
             return math.sin(x*pi)/(pi*x)
 
 The `vectorize` decorator takes a list of function signature and an optional `target` keyword argument (default to 'cpu').  The example above generate a `sinc` ufunc that is overloaded to accept float and double.  This syntax replaces calls to `Vectorize.add` and `Vectorize.build_ufunc`.
+
+
+Generalized Ufuncs
+==================
+
+The ``numba.vectorize`` module also provides support for generalized ufuncs.
+Traditional ufuncs perfom element-wise operations, whereas generalized ufuncs operate on entire
+sub-arrays. Unlike other Numba Vectorize classes, the GUVectorize constructor takes
+an additional signature which specifies the shapes of the inner arrays we want to operate on.
+
+Imports
+-------
+
+::
+
+    from numba import float32, float64, int32
+    from numba.vectorize import GUVectorize
+    import numpy as np
+
+Generalized ufunc Definition
+----------------------------
+
+GUVectorize ufunc arguments are vectors of a NumPy array.  Function definitions can be arbitrary
+expressions.
+
+::
+
+    def matmulcore(A, B, C):
+        m, n = A.shape
+        n, p = B.shape
+        for i in range(m):
+            for j in range(p):
+                C[i, j] = 0
+                for k in range(n):
+                    C[i, j] += A[i, k] * B[k, j]
+
+Compilation requires type information. Numba assumes no knowledge of type when building native
+ufuncs. We must therefore define argument and return dtypes for the defined ufunc. We can add
+as many dtypes as we need, which do not need to be uniform, i.e. we can specify a gufunc
+taking an array of ints and an array of doubles while producing an array of complex numbers.
+The ``gufunc`` will dispatch to the right implementation depending on the argument types.
+
+We can define our gufunc as follows:
+
+::
+
+    gufunc = GUVectorize(matmulcore, '(m,n),(n,p)->(m,p)')
+    gufunc.add(argtypes=[float32[:,:], float32[:,:], float32[:,:]])
+    gufunc.add(argtypes=[float64[:,:], float64[:,:], float64[:,:]])
+    gufunc.add(argtypes=[int32[:,:], int32[:,:], int32[:,:]])
+
+Above we are using a float **float32**, a double **float64**, and a signed **32-bit int**.  The
+GUVectorize calls `PyDynUFunc_FromFuncAndDataAndSignature
+<http://scipy-lectures.github.com/advanced/advanced_numpy/index.html#generalized-ufuncs>`_ which
+requires a the signature: *(m,n),(n,p)->(m,p)* in the constructor.  This signature defines the *"core
+dimensions"* of the generalized ufunc.
+
+We can compile the ufunc as follows:
+
+::
+
+    gufunc = gufunc.build_ufunc()
+
+We can now use the gufunc with two NumPy matrices:
+
+::
+
+    matrix_ct = 10
+    A = np.arange(matrix_ct * 2 * 4, dtype=np.float32).reshape(matrix_ct, 2, 4)
+    B = np.arange(matrix_ct * 4 * 5, dtype=np.float32).reshape(matrix_ct, 4, 5)
+    C = gufunc(A, B)
+
+
+Notice that we don't have a third argument in the gufunc call but the generalized ufunc definition
+above has three arguments. The last argument of the generalized ufunc is the output, which is
+automatically allocated with the shape specified in the signature.
+
```

### Comparing `numba-0.8.1/docs/source/type_inference.rst` & `numba-0.9.0/docs/source/type_inference.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/userguide.rst` & `numba-0.9.0/docs/source/userguide.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/pycc.rst` & `numba-0.9.0/docs/source/pycc.rst`

 * *Files 12% similar despite different names*

```diff
@@ -6,17 +6,17 @@
 library. Below is an example::
 
     from numba import *
 
     def mult(a, b):
         return a * b
 
-    export('mult f8(f8, f8)'))(mult)
-    export(['multf f4(f4, f4)', 'multi i4(i4, i4)'])(mult)
-    export('multc c16(c16, c16)'))(mult)
+    export('mult f8(f8, f8)')(mult)
+    exportmany(['multf f4(f4, f4)', 'multi i4(i4, i4)'])(mult)
+    export('multc c16(c16, c16)')(mult)
 
 This defines a trivial function and exports four specializations under
 different names. The code can be compiled as follows::
 
     pycc thefile.py
 
 Which will create a pure shared library for your platform which can be
```

### Comparing `numba-0.8.1/docs/source/releases.rst` & `numba-0.9.0/docs/source/releases.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/index.rst` & `numba-0.9.0/docs/source/index.rst`

 * *Files 8% similar despite different names*

```diff
@@ -65,15 +65,15 @@
 .. toctree::
    :titlesonly:
    :maxdepth: 1
 
    architecture.rst
    ir.rst
    roadmap.rst
-   reference.rst
+   modules/modules.rst
 
 
 Indices and tables
 ------------------------
 
 * :ref:`genindex`
 * :ref:`modindex`
```

### Comparing `numba-0.8.1/docs/source/examples.rst` & `numba-0.9.0/docs/source/examples.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/types.rst` & `numba-0.9.0/docs/source/types.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/interface_c.rst` & `numba-0.9.0/docs/source/interface_c.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/ir.rst` & `numba-0.9.0/docs/source/ir.rst`

 * *Files 24% similar despite different names*

```diff
@@ -1,27 +1,35 @@
-===============
+===============================================
+Numba Intermediate Representation Specification
+===============================================
+
 Numba IR Stages
 ===============
 
-To allow Numba as a general purpose compiler, we provide different entry
-points. These entry points also allow for further decoupling of the Numba
-architecture. We propose several new Intermediate Representations (IRs),
-from high-level to low-level:
+We provide different entry and exit points in the Numba architecture
+to facilitate reuse. These entry points also allow for further
+decoupling (modularity) of the Numba architecture. The Numba
+architecture is broken into several stages, or compilation passes.  At
+the boundaries between each compilation stage, we define a specific
+intermediate representation (IR).
 
-    * The Python AST IR (input to a numba frontend)
-    * Normalized IR
+The Numba intermediate representations (IR's) are, from high-level to
+low-level, as follows:
+
+    * The `Python AST IR`_ (input to a numba frontend)
+    * `Normalized IR`_
 
         - Like a Python AST, but contains normalized structures
           (assignments, comparisons, list comprehensions, etc)
-    * Untyped IR in SSA form
+    * `Untyped IR in SSA form`_
 
         - Expanded control flow (with annotations)
-    * Typed IR in SSA form
-    * Low-level IR in SSA form
-    * Final LLVM IR, the final input for LLVM. This IR is unportable
+    * `Typed IR in SSA form`_
+    * `Low-level Portable IR`_
+    * `Final LLVM IR`_, the final input for LLVM. This IR is not portable
       since the sizes of types are fixed.
 
 All IRs except the last are portable across machine architectures.
 We get the following options for rewrites:
 
 .. digraph:: stages
 
@@ -61,17 +69,14 @@
 
 IRs up to the low-level IR (input to `Stage 4`) should still contain explicit
 variable stores, so that passes can rewrite variable assignments to for instance
 assignments to struct or extension type instance members. Keeping stores and loads
 to and from these variables in the original order is important in the context
 of closures (or any function call which can modify a stack variable through a pointer).
 
-.. NOTE:: Maybe we should only do this for cell- and free variables, and fix
-          closures before CFA?
-
 We must make sure to support preloads for variable definitions across basic
 blocks, e.g.::
 
     if ...:
         A = ...
     else:
         A = ...
@@ -86,305 +91,144 @@
     ValueC = BinOp(ValueA, Add, ValueB)
     Store(Name('c'), ValueC)
 
 Instead of::
 
     Assign(Name('c'), BinOp(Name('a'), Add, Name('b')))
 
-Intermediate Representations
-============================
-
-Each IR consists of two layers, namely a higher-level Abstract Syntax Tree
-encoding, specified, verified and generated by our variant of ASDL
-schemas. We add the symbol ``@`` to signal that the given type
-is to be treated as a "unique" object, i.e. one that compares by identity
-as opposed to structural equality. These objects each carry a unique id
-and are serialized in a table (and they may participate in circular
-references, i.e. in a graph):
-
-Serialization to LLVM IR (or a direct textual serialization) will
-consist of something like a generated table, e.g.
-
-.. code-block:: pycon
-
-    >>> mod = schema.parse("foo = @Foo(str name, foo attr)")
-
-    >>> foo1 = mod.Foo("foo1")
-    >>> foo2 = mod.Foo("foo2", foo1)
-    >>> foo1.attr = foo2
-
-    >>> foo1
-    Foo(name="foo1", attr=Foo("foo2", Foo(name="foo1", attr=...)))
-
-    >>> build_llvm_ir(foo1)   # name,  id,    attr
-    !0 = metadata !{ metadata !"foo1", i64 0, i64 1 }
-    !1 = metadata !{ metadata !"foo2", i64 1, i64 0 }
-
-Attributes may also be hidden using ``\``, which means the attribute
-is not considered a child for the purposes of visitors or term
-rewrites::
-
-    foo = @Foo(str name, foo \attr)
-
-Use of Schemas
---------------
-We can use our schemas to:
-
-    * Validate IR instances
-    * Generate Python AST classes with typed properties and fast
-      visitor dispatching
-    * Generate Higher- or Lower-level LLVM IR
-    * Generate conversion code to and from an ATerm representation
-    * Generate a flat representation. E.g. a form of Three Address Code
-    * Generate an implementation in other languages that can load a
-      serialized representation and construct an AST in that langauge
-    * Generate type definitions and serialization routines in
-      other languages.
-
-        .. NOTE:: This can help other languages target Numba as
-                  a backend compiler more easily, since they can
-                  build up the IR using in-memory data structures for
-                  the IR most suitable to their needs.
-
-    * Generate definitions for use in Attribute Grammars ([#]_)
-    * Executable IR (:ref:`executable`)
-
-.. _llvm_ir:
+Numba Intermediate Representations
+==================================
 
-LLVM IR
-^^^^^^^
+Python AST IR
+-------------
 
-We can generate automatic mapping code to map schema instances to
-opaquely typed LLVM IR automatically, which is the abstract syntax
-generated post-order. E.g. ``a + b * c`` becomes:
+Numba's initial intermediate representation is Python abstract syntax
+as defined in Python's ast_ module documentation.  Note that this
+definition is specific to the version of Python being compiled.
 
-.. code-block:: llvm
+.. _ast: http://docs.python.org/library/ast.html#abstract-grammar
 
-    !0 = metadata !{ metadata !"operator", i8* "Mul" }
-    !1 = metadata !{ metadata !"operator", i8* "Add" }
+Numba must support `Python 2 abstract syntax`__ (specifically versions
+2.6, and 2.7) for the foreseeable future.
 
-    define i8* some_func(i8* %a, i8* %b, i8* %c) {
-    entry:
-      %0 = call i8* @numba.ir.BinOp(%b, metadata !{0}, %c)
-      %1 = call i8* @numba.ir.BinOp(%a, metadata !{1}, %0)
-      ret %1
-    }
+.. _ast2: http://docs.python.org/2/library/ast.html#abstract-grammar
+.. _ast3: http://docs.python.org/3/library/ast.html#abstract-grammar
 
-The LLVM IR contains the high-level block structure, i.e. an ``if`` statement
-will generate IR along the following lines:
+__ ast2_
 
-.. code-block:: llvm
+Normalized IR
+-------------
 
-    define i8* @func() {
-    entry:
-        %0 = blockaddress(@func, %bb_test)
-        %1 = blockaddress(@func, %bb_true)
-        %2 = blockaddress(@func, %bb_false)
-        %3 = i8*  @If(i8* %0, i8* %1, i8* %2)
+The normalized IR starts with the latest ASDL definition for `Python
+3 abstract syntax`__, but makes the following changes:
 
-      bb_test:
-        ...
-
-      bb_true:
-        ...
+__ ast3_
 
-      bb_false:
-        ...
-    }
+    * Python's top-level module containers, defined in the ``mod`` sum
+      type, are abandoned.  The Numba normalization stage will return
+      one or more instances of the normalized ``stmt`` sum type.
+    * Constructs that modify the namespace may only reference a single
+      name or syntactic name container.  These constructs include:
 
-An LLVM IR instance can be mapped back losslessly to an IR instance of a
-different representation (e.g. a DAG).
+        - global, nonlocal
+        - import, import from
+        - assignments
+        - del
+    * Expressions are un-flattened.  Operators on more than two
+      sub-expressions are expanded into expression trees.  Comparison
+      expressions on more than two sub-expressions will use temporaries
+      and desugar into an expression tree.
 
-We can use a well-defined abstraction that can map these higher-level
-constructs to the lower-level equilvent. This can be used
-simultenously by:
+Numba must translate Python 2 code into Python 3 constructs.
+Specifically, the following transformations should be made:
 
-    * The control flow graph builder
-    * Any IR that wants control flow expanded
-    * The code generator
+    * Repr (backticks): Call(Name('repr'), value)
+    * Print(...): Call(Name('print'), ...)
+    * Exec(...): Call(Name('exec'), ...)
+    * Subscript(..., slices, ...): Subscript(..., ExtSlice(slices), ...)
+    * Ellipsis (the slice): Ellipsis (the expression)
+    * With(...): ...
+    * Raise(...): ...
 
-We can use this
-construct to expand our IR to IR that corresponds more closely to
-the final IR we would generate, where all control flow is expanded
-to branches::
+The formal ASDL definition of the normalized IR is given here:
+https://github.com/numba/numba/blob/devel/numba/ir/Normalized.asdl
 
-    define i8* @func() {
-    entry:
-        br label %bb_test
+Issue: Desugaring comparisons
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
-      bb_test:
-        %test = ...
-        br i1 %test, label %bb_true, label %bb_false
+Do we introduce this as being a DAG already?  If not, we have a
+problem with desugarring comparisons.  We need assignment to bind
+temporaries, so we're going to have a hard time handling the
+following::
 
-      bb_true:
-        ...
-        br label %bb_false
+    Compare(e0, [Eq, Lt], [e1, e2])
 
-      bb_false:
-        ...
-        br label %bb_exit
+We'd want "e1" to be the same sub-expression in the normalized IR::
 
-      bb_exit:
-        ...
+    BoolOp(Compare(e0, Eq, e1), And, Compare(e1, Lt, e2))
 
-    }
+How do later stages detect this as being the same sub-expression, etc?
 
-Passes can do not care about special control structures can then execute
-on this IR.
+Proposal
+~~~~~~~~
 
-.. _executable:
+We should add the following constructor to expr::
 
-Executable IR
-^^^^^^^^^^^^^
+    expr |= Let(identifier name, expr def, expr user)
 
-There are two ideas:
+Semantically, this is sugar for the following::
 
-    * Implement a library to which the generated abstract
-      LLVM IR can link. E.g. implement functions such as
-      ``@BinOp(%add, %lhs, %rhs)`` (we can call this function
-      ``PyNumber_Add``).
-
-If we define new lowered IRs are a specialized subset of higher-level
-IRs, we get execution for free:
-
-   * Generate conversion code to and from a high-level Python AST
-     or source code.
-
-     For instance, ``PointerIndex(base_type, node, index)`` becomes
-     ``Call(func=Name('base_type'), args=[Subscript(subnode, index)])``.
-     This function can then be compiled and interpreted with Python,
-     using abstract argument inputs.
+    Call(Lambda(name, user), [def])
 
-Alternatively, if we already know which operations our data corresponds
-to, we can generate a simple AST or bytecode evaluator.
+Later stages of the compiler should not bother to do this desugaring.
+They should instead prefer to just create a SSA definition::
 
-Initial Python-like IR
-----------------------
+    $name = [| def |]
+    $0 = [| user |]
 
-The initial, Python-like, IR is a subset of a Python AST, the
-syntax exludes:
+In the case of a chained comparison, we can then make the following
+transformation::
 
-    * ``FunctionDef`` and ``ClassDef``, which are normalized
-      to ``Assign`` of the function and subsequent
-      decorator applications and assignments
-    * No list, dict, set or generators comprehensions, which are
-      normalized to ``For(...)`` etc + method calls to ``list.append``,
-      etc.
-    * Normalized comparisons
-
-The initial IR is what numba decorators produce given a pure
-Python AST, function or class as input.
-
-Sample schema
-
-.. code-block:: ocaml
-
-    module initial {
-
-        mod = NumbaModule(unit* stats)
-
-        unit
-          = lambda
-          | class
-
-        -- functions --
-        lambda
-          = Lambda(posinfo pos, funcmeta meta, str name, arguments args,
-                   expr body)
-
-        funcmeta
-          = FunctionMetaData(
-                -- locals={'foo': double}
-                str* names,     -- 'foo'
-                nbtype* types,  -- double
-                bool nopython,
-            )
-
-        -- classes --
-        class
-          = ClassExpr(posinfo pos, bool is_jit, attrtable table, method* methods)
-
-        attrtable
-          = AttributeTable(str* attrnames, nbtype* attrtypes)
-
-        method
-          = Method(posinfo pos, methodsignature signature, stat* body)
-
-        -- Types --
-
-        type = nbtype
-        nbtype
-          = char | short | int_ | long_ | longlong
-          | uchar | ushort | uint | ulong | ulonglong
-          | ...
-          | functype
-          | methodtype
-
-        methodtype
-          = MethodSignature(functype signature,
-                            bool is_staticmethod,
-                            bool is_classmethod,
-                            bool is_jit, -- whether this is a jit or
-                                         -- autojit method
-                           )
-    }
+    Compare(e0, [cmp0, ...], [e1, ...])
+    ==>
+    Let(fresh0, e0,
+        Let(fresh1, e1,
+            BoolOp(Compare(fresh0, cmp0, fresh1), And, 
+                   Compare(fresh1, [...], [...]))
 
-.. NOTE:: Numba would construct this before starting any pipeline stage.
+Where ``fresh0`` and ``fresh1`` are fresh variable names.  The
+normalization transformer should recursively apply this rewrite until
+it reaches a case where the comparison is binary.
 
 Untyped IR in SSA form
 ----------------------
 
-Untyped IR in SSA form would be constructed internally by numba during
-and after the CFA pass and before type inference. This adds to the
-``initial`` schema control flow information such as::
-
-    * SSA
-    * Stack variable stack allocation (non-ssa variables)
-    * Def-use and use-def chains
+Given a normalized AST, we preserve the ``expr`` sum type, but perform
+control-flow analysis, data-flow analysis for phi-node injection,
+closure conversion, and lambda lifting.  These transformations result
+in the following intermediate representation::
 
-The high-level CFG at this stage is gone, and we
-have an untyped IR in SSA form (that is, it contains PhiNode AST nodes with uses
-from variables of incoming blocks). It also has a reference to all live phis
-in preorder according to the dominator tree in the ``FunctionDef``.
+   mod = Module(unit* units)
 
-Furthermore:
+   unit = CodeObject(..., block* blocks)
+        | DataObject(identifier label, expr init)
 
-    * ``ast.Name`` is rewritten to ``NameTarget``, ``NameReference`` or ``NameParam``
-    * ``If``, ``While`` and ``For`` lose the ``else`` clause
-    * In-place assignments are normalized
+   block = Block(identifier id, defn* defns, tail tail_expr)
 
-::
+   tail = Jump(identifier target)
+        | If(expr test, identifier true_target, identifier false_target)
+        | Raise(expr exn)
+        | Return(expr result)
 
-    module untyped {
+   defn = (identifier? def_id, expr value)
 
-        function
-          = FunctionDef(phi \all_phis, ...)
+   expr |= Phi(phi_source* incomming)
 
-        phi
-          = Phi(use* \incoming)
+   phi_source = (identifier in_block, expr in_val)
 
-        def
-          = NameTarget(posinfo pos, str id, use* \uses)
-          | phi
-
-        use
-          = NameReference(posinfo pos, str id, nbtype type, def \def)
-          | PhiRef(phi \def)
-
-        lambda
-          = Lambda(posinfo pos, funcmeta meta, str name, arguments args,
-                   expr body, cfg cfg)
-
-        stmt
-          = For(expr target,
-                expr iter,
-                stmt* body)
-          | ...
-
-    }
 
 Typed IR in SSA form
 --------------------
 
 The typed IR is similar to the untyped IR, except that every (sub-)expression
 is annotated with a type.
 
@@ -417,258 +261,429 @@
 Since the schema specifies the interfaces of the different nodes, users
 can supply their own node implementation (something we can do with the
 type system). Hence user-written classes can be automatically
 instantiated instead of generated ones. The code generator can still
 emit code for serialization.
 
 Low-level Portable IR
-=====================
+---------------------
 
 The low-level portable IR is a low-level, platform agnostic, IR that:
 
     * The IR contains only low-level, native types such as ``int_``,
       ``long_``, pointers, structs, etc. The notion of high-level
       concepts such as arrays or objects is gone.
 
-.. _cfg:
+This portable IR could be `LLVM IR`_ , which may still contain
+abstract or opaque types, and make calls to the Numba runtime
+library abstraction layer.
 
-Control Flow
-============
+Final LLVM IR
+-------------
 
-We can have a single abstraction that can create basic blocks and
-link blocks together. For instance we for the following structure::
+The final LLVM IR is `LLVM assembly code`__, with no opaque types, and
+specialized to a specific machine target.
 
-    For(expr target, expr iter, stmt* body, stmt* orelse)
+.. _`LLVM IR`: http://llvm.org/docs/LangRef.html
 
-We have the following CFG:
+__ `LLVM IR`_
 
-.. digraph:: cfg
+Appendicies
+===========
 
-    entry -> condition -> body -> condition -> orelse -> exit
+Appendix: Design Notes
+----------------------
 
-In this CFG, ``break`` and ``continue`` correspond to the following edges:
+This appendix looks at various features and discusses various options
+for representing these constructs across the compiler.
 
-.. digraph:: break
+Closures
+^^^^^^^^
 
-    break -> exit
-    continue -> condition
+A key step in the transition from the normalized AST IR to the untyped
+SSA IR is closure conversion.  For example, given the following code::
 
-We can use this single abstraction to:
+  def closure_test(foo):
+      foo += 3
+      def bar(baz):
+          return foo + (lambda x: x - global_z * foo)(baz)
+      foo += 2
+      return bar
 
-   * Create a CFG at any time in any IR stage. For instance we can
-     generate LLVM IR automatically with expanded control flow.
+Numba should generate SSA code equivalent to the following::
 
-     .. NOTE:: This also includes the code generator, which doesn't
-               have to handle any block structures.
+  def __anonymous(af, x):
+      return x - global_z * af.foo
 
-   * Retain high-level information that allows for simple
-     classification and accurate error reporting.
+  def __bar(af, baz):
+      return af.foo + make_closure(__anonymous,
+                                   make_activation_frame(af, []))(baz)
 
-     .. NOTE:: This is important to allow us to easily rewrite entire
-               control flow structures, such as outlining of the prange
-               construct.
+  def closure_test(foo):
+      af = make_activation_frame(None, ['foo'])
+      af.foo = foo
+      af.foo += 3
+      bar = make_closure(__bar, af)
+      af.foo += 2
+      return bar
 
-IR Suitability
-==============
-An important consideration for an IR is how well transformations are
-defined over it, and how efficient those transformations are. For instance,
-a pass that combines instructions works far better on a simple three-address
-representation than an AST. Design considerations ([#]_):
+Parent frames
+~~~~~~~~~~~~~
 
-    * Level and machine independence
-    * Structure
-    * Expressiveness
-    * Appropriateness for transformation and code generation
+The above convention implies the following ASDL definition of the
+``MakeFrame`` constructor (XXX cross reference discussion of IR expr
+language)::
 
+  MakeFrame(expr parent, identifier* ids)
 
-To evaluate some of these metrics we will look at some concretions.
+The parent frame provides a name space for identifiers unresolved in
+the current frame.  If we employ this constructor, we diverge slightly
+from CPython.  CPython manages each unbound variable within a cell,
+and these cells are copied into a new frame object (which is a tuple
+in CPython) for every child closure constructed.
 
-Structure
----------
-We can consider expanded or abstract control flow:
+Alternative: Explicit parameterization
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
-    * We want to compute an SSA graph. Clearly we need a control flow
-      graph in order to perform this computation.
+Another method for doing closure conversion involves parameterizing
+over all free variables, and is closer to CPython's approach::
 
-    * We want to *outline* a prange construct. Consider what this looks
-      like using unexpanded and expanded control flow.
+  def __anonymous(foo, x):
+      return x - global_z * foo.load()
 
-    Unexpanded::
+  def __bar(foo, baz):
+      return foo.load() + partial(__anonymous, [foo])(baz)
 
-        For(iter=prange(...)) ->
-            [ MakeClosure(For(iter=prange(adjust_bounds(...))) ; InvokeThreadPool ]
+  def closure_test(foo):
+      foo = make_cell(foo)
+      foo += 3
+      bar = partial(__bar, [foo])
+      foo += 2
+      return bar
 
-    Expanded:
+This approach uses partial function application to build closures.
+The resulting representation affords opportunities for optimizations
+such as rewriting ``partial(fn, [x])(y)`` to ``fn(x, y)``.
 
-        * Match a loop
-        * Scan preceding statements for ``t = iter(prange(...))``
-        * Outline ``[ t ; loop ]``
-        * Apply ``adjust_bounds`` to ``iter(prange(...))``
-        * Perform range transformation to rewrite using counters
+Default, variable, and keyword arguments
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
+XXX Do we need a MakeFunction() expression constructor for supplying
+default arguments?  This follows from discussion of closures, above.
 
-Consider also error reporting facilities. For instance, let's assume
-we want to disallow break from parallel loops.
+Iterators
+^^^^^^^^^
 
-    Unexanded:
+Iterators in the untyped IR
+~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
-        ``Break -> error``
+We considered three options for implementing iterators.  The first was
+to use exception handling constructs.  Given the following code::
 
-    Expanded:
+  for x in i:
+      if x == thingy: break
+  else:
+      bar()
+  baz()
 
-        * Scan for ``prange`` (similar to above, namely match a loop,
-          scan preceding statement for ``iter()``)
-        * Find a CFG edge that points outside the loop body region
-          (e.g. the exit block of the loop, or a block further outside
-          the region)
+Translation to the untyped IR could result in something like the
+following::
 
-Clearly, some transformations are easier to perform using expanded control flow, e.g.:
+  bb0: ...
+       $0 = Call(Constant(numba.ct.iter), [Name("i", Load())])
+       Try(bb1, [ExceptHandler(Constant(StopIteration), None, bb2)],
+           None, None)
 
-    * Computing SSA
-    * Dead-code elimination
-    * Control flow simplification
-    * Transformations to structured control flow
-    * and so forth
+  bb1: $1 = Call(Constant(numba.ct.next), [$0])
+       If(Compare($1, Eq(), Name("thingy", Load())), bb3, bb1)
 
-Expressiveness
---------------
-Consider a high-level type system, that has:
+  bb2: Call(Name("bar", Load()), [])
+       Jump(bb3)
 
-    * Full or partial functions as first-class values
+  bb3: Call(name("baz", Load()), [])
+       ...
 
-        * This subsumes closurs and all methods (bound, unbound, class, static)
-    * Types as first-class values
-    * (Extension) Classes as first-class values
-    * Containers such as
+The second option was defining a ``Next()`` terminator.  ``Next()``
+could provide sugar for the special case where we are specifically
+waiting for a ``StopIteration`` exception::
 
-        * Arrays
-        * Typed lists, sets, dicts, channels, and so forth
+  bb0: ...
+       $0 = Call(Constant(numba.ct.iter), [Name("i", Load())])
+       Jump(bb1)
 
-Program instances using these constructs must be quickly identifyable to aid
-easy tranformation. For instance, ``obj.method(10)`` should be quickly transformable
-using rules along the following lines:
+  bb1: Next(Name("x", Store()), $0, bb2, bb3)
 
-.. code-block:: ocaml
+  bb2: If(Compare(Name("x", Load()), Eq, Name("thingy", Load())), bb4, bb1)
 
-    Attribute(Value(type=object_), attr)
-        -> PyObject_GetAttrString(value, attr)
+  bb3: Call(Name("bar", Load()), [])
+       Jump(bb4)
 
-    Attribute(ExtensionMethod(..., is_jit=True), value, attr)
-        -> ExtensionMethodStruct(value, method)
+  bb4: Call(Name("baz", Load()), [])
+       ...
 
-with:
+We loose SSA information, but provide opportunity for more readily
+recognizing for loops.
 
-.. code-block:: c
+The third option was to follow the CPython VM semantics of
+``FOR_ITER``, where we define ``Next()`` as an expression constructor
+which can either return a result or some sentinel (specific to
+CPython, this is the ``NULL`` pointer)::
 
-      [
-          typedef {
-              double (*method1)(double);
-              ...
-          } vtab_struct;
+  bb0: ...
+       $0 = Iter(Name("i", Load()))
+       Jump(bb1)
 
-          vtab_struct *vtab = *(vtab_struct **) (((char *) obj) + vtab_offset)
-          void *method = vtab[index]
-      ]
+  bb1: $1 = Next($0)
+       If(Compare($1, Neq(), Constant(numba.ct.NULL)), bb2, bb3)
 
+  bb2: If(Compare($1, Eq(), Name("thingy", Load())), bb3, bb1)
 
-A call for object then exands to ``PyObject_Call``, and a method call to a
-``NativeCall`` of ``ExtensionMethodStruct.method`` with first argument
-``ExtensionMethodStruct.value`` ('self').
+  bb3: Call(Name("bar", Load()), [])
+       Jump(bb4)
 
-A later pass can then combine consecutive instructions and optimize them, i.e.
+  bb4: Call(name("baz", Load()), [])
+       ...
 
-.. code-block:: ocaml
+This final output looks very similar to the output of the second
+option, but prevents us from having to use the ``Name()`` expression
+for anything other than global and parameter variables.
 
-    [
-        method = PyObject_GetAttrString(obj, attr);
-        PyObject_Call(method, value, args)
-    ]
-        -> PyObject_CallMethod(obj, attr, args)
+Generators
+^^^^^^^^^^
 
-A similar pass for extension methods would then avoid building the
-intermediate struct.
+.. _`generator discussion`:
+   https://groups.google.com/a/continuum.io/forum/#!topic/numba-users/gaVgArRrXqw
 
-.. NOTE:: Note how we could combine the first and second passes to detect method
-          calls. Such a rule would be well-expressed on a tree or graph structure.
-          The first rule as specified would work well on both a tree or three-address
-          code. The latter is specified best on TAC.
+The Numba Google group's `generator discussion`_ identified two
+methods for implementing generators in Numba.  These can roughly be
+summarized as "enclosing everything in a big C-like switch statement",
+and "use goroutines".  The following web pages elaborate on these
+techniques:
 
-The point we're trying to make is that we need to encode many different kinds
-of first-class values, which have high-level types. These constucts must be
-quickly identifyable and transformable using a high-level type system that
-can support constructs of the high-level language.
+* http://www.chiark.greenend.org.uk/~sgtatham/coroutines.html
+* https://code.google.com/p/try-catch-finally/wiki/GoInternals
 
-Using a low-level type system such as LLVM's or C's means high-level types
-need low-level equivalents, which means one of two things:
 
-    * You use an abstract type classifier, which needs to be composable
-    * You use a lower-level representation which more closely resembles
-      the type of the value in its lowered representation (e.g. a struct
-      of a function pointer and an object pointer).
+Global and nonlocal variables
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
-LLVM facilitates the latter point, but is in no way caters to
-the first. Yet what we want is the former, for the sake of expressiveness.
+Given::
 
-Reusing LLVM Passes
-===================
-Although LLVM IR does not cater well to some of the high-level
-transformations we want to make, it provides a useful infrastructure to
-do certain things. This includes:
+  z = 42
+  def foo():
+      global z
+      bar(z)
+      z = 99
 
-    * SSA Graph Computation (as well as reaching definitions, etc)
-    * CFG simplification
-    * Finding SCCs in various graphs (CFG, SSA, call graph, etc)
-    * Build a call graph
-    * Aiding lower-level and TAC transformations
+We could generate the following in untyped IR::
 
-Below we will discuss a plan for resuability.
+  [
+    DataObject("z", Constant(42)),
+    CodeObject("foo", ([], None, None, ...), [
+      Block("entry", [
+          (None, Call(Name("bar", Load()), [LoadGlobal("z")])),
+          (None, StoreGlobal("z", Constant(99)))
+        ], Return(Constant(None)))])
+  ]
 
-SSA
----
-We currently construct our own CFG and compute the SSA graph from the
-CFG containing abstract statements that represent definitions and uses
-(loads and stores).
 
-As mentioned, the advantage of having our own CFG construction includes:
+.. XXX Globals as static data.
 
-    * Expressiveness of high-level operations
-    * Automatic code generation and translation into IRs with expanded
-      control flow
+Exceptions and exception handling
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
-The advantage of having our own reaching definitions (reused from Cython's
-control flow, ``Cython/Compiler/FlowControl``) is the great support for
-errors and warnings for:
+Both the raise and try-except-finally language constructs map into the
+untyped SSA IR as basic-block terminators::
 
-    * Definitely unbound variables (error)
-    * Potentionally unbound variables (warning)
-    * Unused variables (warning)
+  tail = ...
+       | Raise(expr exn)
+       | Try(identifier body,
+             excepthandler* handlers,
+             identifier? orelse,
+             identifier? finalbody)
 
-as well as other categories. LLVM on the other hand classifies reads
-from uninitialized variables as undefined behaviour.
+  ...
 
-Numba initializes potentially unbound variables to a "bad" value (``nan``,
-``0xdeadbeef``, etc). We can use the same mechanism to construct valid
-LLVM IR, and compute the SSA graph from our subset program, consisting only
-of:
+  excepthandler = ExceptHandler(expr *types,
+                                identifier? name,
+                                identifier body)
+                  attributes (int lineno, int col_offset)
 
-    * expanded control flow
-    * variable stores
-    * variable loads
+.. XXX Is there a better way to present this?  Maybe as a table?
 
-This LLVM-constructed SSA graph can be mapped back to our high-lever IR
-with relative ease if we simply remembered which LLVM basic block associates
-with which basic block in our IR.
+In the low-level IR, these constructs lower into Numba run-time calls::
 
+  bb0:  ...
+        Try('bb1', [ExceptHandler([ty0,...], 'name0', 'bb2'),
+                    ...
+                    ExceptHandler([tyn,...], 'namen', 'bbn0')],
+            'bbn1', 'bbn2')
+  bb1:  ...
+        Jump('bbn2')
+  bb2:  ...
+        Jump('bbn2')
+  ...
+  bbn0: ...
+        Jump('bbn2')
+  bbn1: ...
+        Jump('bbn2')
+  bbn2: ...
 
-.. NOTE:: This operates under the assumption that we have a general
-          framework that can map LLVM transformations back to our IR
-          representation automatically.
+Goes to::
 
-Type Dependence Graph Construction
+  bb0:  ...
+        $0 = SetupTry()
+        If($0, 'bb1', 'bb2')
+  bb1:  ...
+        Jump('bbn2')
+  bb2:  $1 = TestExn([ty0, ...])
+        If($1, 'bbx2', 'bb3')
+  bbx2: $name0 = GetExn()
+        ...
+        Jump('bbn2')
+  ...
+  bbn0: $2 = TestExn([tyn, ...])
+        If($2, 'bbxn', 'bbn1')
+  bbxn: $namen = GetExn()
+        ...
+        Jump('bbn2')
+  bbn1: GetExn()
+        ...
+        Jump('bbn2')
+  bbn2: ...
+
+
+Decorators
+^^^^^^^^^^
+
+Classes and objects
+^^^^^^^^^^^^^^^^^^^
+
+Namespaces
+^^^^^^^^^^
+
+
+Appendix: Language Cross Reference
 ----------------------------------
+
+The following sections follow the `Python Language Reference`_, and
+provide notes as on how the various Numba intermediate representations
+support the Python language.
+
+.. _`Python Language Reference`: http://docs.python.org/3/reference/index.html
+
+
+Expressions
+^^^^^^^^^^^
+
+Simple statements
+^^^^^^^^^^^^^^^^^
+
+Expression statements
+~~~~~~~~~~~~~~~~~~~~~
+
+Assignment statements
+~~~~~~~~~~~~~~~~~~~~~
+
+The assert statement
+~~~~~~~~~~~~~~~~~~~~
+
+The pass statement
+~~~~~~~~~~~~~~~~~~
+
+The del statement
+~~~~~~~~~~~~~~~~~
+
+The return statement
+~~~~~~~~~~~~~~~~~~~~
+
+The yield statement
+~~~~~~~~~~~~~~~~~~~
+
+The raise statement
+~~~~~~~~~~~~~~~~~~~
+
+The break statement
+~~~~~~~~~~~~~~~~~~~
+
+The continue statement
+~~~~~~~~~~~~~~~~~~~~~~
+
+The import statement
+~~~~~~~~~~~~~~~~~~~~
+
+The global statement
+~~~~~~~~~~~~~~~~~~~~
+
+Compound statements
+^^^^^^^^^^^^^^^^^^^
+
+The if statement
+~~~~~~~~~~~~~~~~
+
+The while statement
+~~~~~~~~~~~~~~~~~~~
+
+The for statement
+~~~~~~~~~~~~~~~~~
+
+The try statement
+~~~~~~~~~~~~~~~~~
+
+The with statement
+~~~~~~~~~~~~~~~~~~
+
+Function definitions
+~~~~~~~~~~~~~~~~~~~~
+
+Class definitions
+~~~~~~~~~~~~~~~~~
+
+Top-level components
+^^^^^^^^^^^^^^^^^^^^
+
+Appendix: Other Design Notes
+----------------------------
+
+Use of Schemas
+^^^^^^^^^^^^^^
+
+We can use our schemas to:
+
+    * Validate IR instances
+    * Generate Python AST classes with typed properties and fast
+      visitor dispatching
+    * Generate Higher- or Lower-level LLVM IR
+    * Generate conversion code to and from an ATerm representation
+    * Generate a flat representation. E.g. a form of Three Address Code
+    * Generate an implementation in other languages that can load a
+      serialized representation and construct an AST in that langauge
+    * Generate type definitions and serialization routines in
+      other languages.
+
+        .. NOTE:: This can help other languages target Numba as
+                  a backend compiler more easily, since they can
+                  build up the IR using in-memory data structures for
+                  the IR most suitable to their needs.
+
+    * Generate definitions for use in Attribute Grammars
+    * Executable IR (:ref:`executable`)
+
+.. _executable:
+
+Executable IR
+~~~~~~~~~~~~~
+
+There are two ideas:
+
+    * Write a simple interpreter
+    * Generate source code containing calls to a runtime library
+
+Type Dependence Graph Construction
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 From the SSA graph we compute a type graph by inferring all variable
 assignments. This graph often has cycles, due to the back-edge in
 the CFG for loops. For instance we may have the following code::
 
     x = 0
     for i in range(10):
         x = f(x)
@@ -733,31 +748,15 @@
     * If the node represents a function over an argument of the given input types,
       infer the result type of this function
     * For each SCC, process all internal nodes using fixpoint iteration
       given all input types to the SCC. Update internal nodes with their result
       types.
 
 Building a Call Graph
----------------------
+~~~~~~~~~~~~~~~~~~~~~
 This will be useful to use LLVM for in order to:
 
     * Efficiently infer types of direct or indirect uses of recursion for autojit
       functions or methods
     * Detect such recusion by letting LLVM find the SCCs in the call graph, and
       resolving in an analogous and cooperative manner to how we resolve the type graph
 
-Writing LLVM Passes
--------------------
-We have a few constructs that may be better written as LLVM passes over simpler
-(lower-level) constructs (with exapnded control flow, three-address code arithmetic
-instructions, etc). We showed one such example already, but one can think
-of many others.
-
-We can define the penultimate IR in LLVM, such that any passes before code generator
-and after lowering of high-level constructions an be performed on this IR. This allows
-us to use the full power of LLVM where it is most adequate. Furthermore, we can likely
-do away with (most of) our code generator if we define our IR stages well.
-
-References
-==========
-.. [#] Attribute Grammars in Haskell with UUAG, A. Loh, http://www.andres-loeh.de/AGee.pdf
-.. [#] Advanced Compiler Design and Implementation, Steven S. Muchnick
```

### Comparing `numba-0.8.1/docs/source/conf.py` & `numba-0.9.0/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/architecture.rst` & `numba-0.9.0/docs/source/architecture.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/doctest.rst` & `numba-0.9.0/docs/source/doctest.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/source/roadmap.rst` & `numba-0.9.0/docs/source/roadmap.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/update-release-notes.py` & `numba-0.9.0/docs/update-release-notes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/docs/gh-pages.py` & `numba-0.9.0/docs/gh-pages.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/PKG-INFO` & `numba-0.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: numba
-Version: 0.8.1
+Version: 0.9.0
 Summary: compiling Python code using LLVM
 Home-page: http://numba.github.com
 Author: Continuum Analytics, Inc.
 Author-email: numba-users@continuum.io
 License: BSD
 Description: Numba
         =====
```

### Comparing `numba-0.8.1/deps/pyextensibletype/README.rst` & `numba-0.9.0/deps/pyextensibletype/README.rst`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/extensibletype.pyx` & `numba-0.9.0/deps/pyextensibletype/extensibletype/extensibletype.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/methodtable.pyx` & `numba-0.9.0/deps/pyextensibletype/extensibletype/methodtable.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/intern.pxd` & `numba-0.9.0/deps/pyextensibletype/extensibletype/intern.pxd`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/test/test_perfecthashing.py` & `numba-0.9.0/deps/pyextensibletype/extensibletype/test/test_perfecthashing.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/test/pstdint.pyx` & `numba-0.9.0/deps/pyextensibletype/extensibletype/test/pstdint.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/test/test_interning.py` & `numba-0.9.0/deps/pyextensibletype/extensibletype/test/test_interning.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/extensibletype/extensibletype.pxd` & `numba-0.9.0/deps/pyextensibletype/extensibletype/extensibletype.pxd`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/demo/consumer.pyx` & `numba-0.9.0/deps/pyextensibletype/demo/consumer.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/demo/provider_c_code.h` & `numba-0.9.0/deps/pyextensibletype/demo/provider_c_code.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/setupconfig.py` & `numba-0.9.0/deps/pyextensibletype/setupconfig.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/setup.py` & `numba-0.9.0/deps/pyextensibletype/setup.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/pstdint.h` & `numba-0.9.0/deps/pyextensibletype/include/pstdint.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/interning.h` & `numba-0.9.0/deps/pyextensibletype/include/interning.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/perfecthash.h` & `numba-0.9.0/deps/pyextensibletype/include/perfecthash.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/siphash24.c` & `numba-0.9.0/deps/pyextensibletype/include/siphash24.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/customslots.h` & `numba-0.9.0/deps/pyextensibletype/include/customslots.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/globalinterning.h` & `numba-0.9.0/deps/pyextensibletype/include/globalinterning.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/deps/pyextensibletype/include/extensibletype.h` & `numba-0.9.0/deps/pyextensibletype/include/extensibletype.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/AUTHORS` & `numba-0.9.0/AUTHORS`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/setup.py` & `numba-0.9.0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -72,26 +72,27 @@
                 stack.append((fn, prefix+name+'.'))
 
     if sys.version_info[0] == 3:
         exclude = exclude + ('*py2only*', )
 
     for pat in list(exclude) + ['ez_setup', 'distribute_setup']:
         out = [item for item in out if not fnmatchcase(item, pat)]
+
     return out
 
 #------------------------------------------------------------------------
 # 2to3
 #------------------------------------------------------------------------
 
 def run_2to3():
     import lib2to3.refactor
     from distutils.command.build_py import build_py_2to3 as build_py
     print("Installing 2to3 fixers")
     # need to convert sources to Py3 on installation
-    fixes = 'dict imports imports2 unicode ' \
+    fixes = 'dict imports imports2 unicode metaclass basestring reduce ' \
             'xrange itertools itertools_imports long types'.split()
     fixes = ['lib2to3.fixes.fix_' + fix 
              for fix in fixes]
     build_py.fixer_names = fixes
     cmdclass["build_py"] = build_py
     # cmdclass["build"] = build_py
 
@@ -139,14 +140,18 @@
 if sys.version_info[0] >= 3:
     run_2to3()
 
 #------------------------------------------------------------------------
 # setup
 #------------------------------------------------------------------------
 
+exclude_packages = (
+    '*deps*', 'numba.ir.normalized', 'numba.ir.untyped', 'numba.ir.typed',
+)
+
 setup(
     name="numba",
     version=versioneer.get_version(),
     author="Continuum Analytics, Inc.",
     author_email="numba-users@continuum.io",
     url="http://numba.github.com",
     license="BSD",
@@ -157,23 +162,24 @@
         "Programming Language :: Python",
         # "Programming Language :: Python :: 2.6",
         "Programming Language :: Python :: 2.7",
         # "Programming Language :: Python :: 3.2",
         "Topic :: Utilities",
     ],
     description="compiling Python code using LLVM",
-    packages=find_packages(exclude=('*deps*',)),
+    packages=find_packages(exclude=exclude_packages),
     entry_points = {
         'console_scripts': [
             'pycc = numba.pycc:main',
             ]
     },
     package_data={
         '': ['*.md'],
         'numba.minivect': ['include/*'],
+        'numba.ir.generator.tests': ['*.asdl'],
         'numba.asdl.common': ['*.asdl'],
         'numba.asdl.py2_7': ['*.asdl'],
         'numba.asdl.py3_2': ['*.asdl'],
         'numba.asdl.py3_3': ['*.asdl'],
         'numba.external.utilities': ['*.c', '*.h'],
         'numba': ['*.c', '*.h', 'include/*', '*.pxd'],
         'numba.vectorize': ['*.h'],
```

### Comparing `numba-0.8.1/gen_type_conversion.py` & `numba-0.9.0/gen_type_conversion.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/CHANGE_LOG` & `numba-0.9.0/CHANGE_LOG`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/missing.py` & `numba-0.9.0/numba/missing.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/type_inference/infer.py` & `numba-0.9.0/numba/type_inference/infer.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,34 +5,33 @@
 import types
 import logging
 try:
     import __builtin__ as builtins
 except ImportError:
     import builtins
 
-from functools import reduce
+from functools import reduce, partial
 
 import numba
 from numba import *
 from numba import error, control_flow, visitors, nodes
 from numba import oset, odict
-from numba.specialize.mathcalls import is_math_function
+from numba.type_inference.modules import mathmodule
 from numba.type_inference import module_type_inference, infer_call, deferred
-from numba.minivect import minitypes
 from numba import utils, typesystem
 from numba.control_flow import ssa
+from numba.typesystem import ssatypes
 from numba.typesystem.ssatypes import kosaraju_strongly_connected
 from numba.symtab import Variable
 from numba import closures as closures
 import numba.wrapping.compiler
 from numba.support import numpy_support
 from numba.exttypes.variable import ExtensionAttributeVariable
 
-from numba.typesystem import is_obj, promote_closest, get_type
-from numba.utils import dump
+from numba.typesystem import get_type
 
 import llvm.core
 import numpy
 
 debug = False
 #debug = True
 
@@ -107,15 +106,15 @@
         ret_type = self.func_signature.return_type
 
         if ret_type and ret_type != self.return_type:
             self.assert_assignable(ret_type, self.return_type)
             self.return_type = self.promote_types(ret_type, self.return_type)
 
         restype, argtypes = self.return_type, self.func_signature.args
-        self.func_signature = minitypes.FunctionType(return_type=restype,
+        self.func_signature = typesystem.function(return_type=restype,
                                                      args=argtypes)
 
     #------------------------------------------------------------------------
     # Symbol Table Type Population and Argument Processing
     #------------------------------------------------------------------------
 
     def initialize_constants(self):
@@ -158,16 +157,15 @@
         arg_types = list(self.func_signature.args)
 
         self.initialize_constants()
         self.handle_locals(arg_types)
         self.initialize_argtypes(arg_types)
         self.initialize_ssa()
 
-        self.func_signature.args = tuple(arg_types)
-
+        self.func_signature = self.func_signature.add('args', arg_types)
         self.have_cfg = hasattr(self.ast, 'flow')
         if self.have_cfg:
             self.deferred_types = []
             self.resolve_variable_types()
 
         if debug and self.have_cfg:
             for block in self.ast.flow.blocks:
@@ -179,16 +177,16 @@
     #------------------------------------------------------------------------
     # Utilities
     #------------------------------------------------------------------------
 
     def is_object(self, type):
         return type.is_object or type.is_array
 
-    def promote_types(self, t1, t2):
-        return self.context.promote_types(t1, t2)
+    def promote_types(self, type1, type2):
+        return ssatypes.promote(self.env.crnt.typesystem, type1, type2)
 
     def promote_types_numeric(self, t1, t2):
         "Type promotion but demote objects to numeric types"
         if (t1.is_numeric or t2.is_numeric) and (self.is_object(t1) or
                                                  self.is_object(t2)):
             if t1.is_numeric:
                 return t1
@@ -200,15 +198,15 @@
     def promote(self, v1, v2):
         return self.promote_types(v1.type, v2.type)
 
     def assert_assignable(self, dst_type, src_type):
         self.promote_types(dst_type, src_type)
 
     def type_from_pyval(self, pyval):
-        return self.context.typemapper.from_python(pyval)
+        return self.env.crnt.typesystem.typeof(pyval)
 
     #------------------------------------------------------------------------
     # SSA-based type inference
     #------------------------------------------------------------------------
 
     def handle_NameAssignment(self, assignment_node):
         if assignment_node is None:
@@ -233,15 +231,16 @@
                 # resolution
                 v.type = v.deferred_type
                 self.deferred_types.append(v.type)
 
         incoming_types = [v.type for v in incoming]
         if len(incoming_types) > 1:
             promoted_type = typesystem.PromotionType(
-                node.variable, self.context,incoming_types, assignment=True)
+                node.variable, partial(ssatypes.promote, self.env.crnt.typesystem),
+                incoming_types, True)
             promoted_type.simplify()
             node.variable.type = promoted_type.resolve()
         else:
             node.variable.type = incoming_types[0]
 
         #print "handled", node.variable
         return node
@@ -530,15 +529,15 @@
             else:
                 # list or tuple literal
                 value = node.value.elts[i]
 
             assmt = ast.Assign(targets=[target], value=value)
             result.append(self.visit(assmt))
 
-        return result
+        return ast.Suite(result)
 
     def visit_Assign(self, node):
         # Initialize inplace operator
         node.inplace_op = getattr(node, 'inplace_op', None)
 
         node.value = self.visit(node.value)
         if len(node.targets) != 1 or isinstance(node.targets[0], (ast.List,
@@ -627,30 +626,30 @@
             self.visitlist(node.orelse)
 
         return node
 
     def visit_booltest(self, node):
         if isinstance(node.test, control_flow.ControlBlock):
             node.test.body[0] = nodes.CoercionNode(
-                node.test.body[0], minitypes.bool_)
+                node.test.body[0], typesystem.bool_)
         else:
-            node.test = nodes.CoercionNode(node.test, minitypes.bool_)
+            node.test = nodes.CoercionNode(node.test, typesystem.bool_)
 
     def visit_While(self, node):
         self.generic_visit(node)
         self.visit_booltest(node)
         return node
 
     visit_If = visit_While
 
     def visit_IfExp(self, node):
         self.generic_visit(node)
         type_ = self.promote(node.body.variable, node.orelse.variable)
         node.variable = Variable(type_)
-        node.test = nodes.CoercionNode(node.test, minitypes.bool_)
+        node.test = nodes.CoercionNode(node.test, typesystem.bool_)
         node.orelse = nodes.CoercionNode(node.orelse, type_)
         node.body = nodes.CoercionNode(node.body, type_)
         return node
 
     #------------------------------------------------------------------------
     # Return
     #------------------------------------------------------------------------
@@ -666,15 +665,15 @@
             # 'return'
             value = None
 
         if value is None or type.is_none:
             # When returning None, set the return type to void.
             # That way, we don't have to deal with the PyObject reference.
             if self.return_variable.type is None:
-                self.return_variable.type = minitypes.VoidType()
+                self.return_variable.type = typesystem.void
             value = None
         elif self.return_variable.type is None:
             self.return_variable.type = type
         elif self.return_variable.type != type:
             # TODO: in case of unpromotable types, return object?
             if self.given_return_type is None:
                 self.return_variable.type = self.promote_types_numeric(
@@ -722,23 +721,23 @@
         is_builtin = (global_name not in globals and
                       getattr(builtins, global_name, None))
         is_global = not is_builtin
 
         # Determine the type of the global, i.e. a builtin, global
         # or (numpy) module
         if is_builtin:
-            type = typesystem.BuiltinType(name=global_name)
+            type = typesystem.builtin_(global_name, getattr(builtins, global_name))
         else:
             # FIXME: analyse the bytecode of the entire module, to determine
             # overriding of builtins
             if isinstance(globals.get(global_name), types.ModuleType):
-                type = typesystem.ModuleType(globals.get(global_name))
+                type = typesystem.module(globals.get(global_name))
             else:
                 value = lookup_global(self.env, global_name, name_node)
-                type = typesystem.GlobalType(global_name, value)
+                type = typesystem.global_(value) # do away with this
 
         variable = Variable(type, name=global_name, is_constant=True,
                             is_global=is_global, is_builtin=is_builtin,
                             constant_value=type.value)
         self.symtab[global_name] = variable
         return variable
 
@@ -804,16 +803,16 @@
         "and/or expression"
         # NOTE: BoolOp.values can have as many items as possible.
         #       Only meta is doing 2 items.
         # if len(node.values) != 2:
         #     raise AssertionError
         assert len(node.values) >= 2
         node.values = self.visitlist(node.values)
-        node.values[:] = nodes.CoercionNode.coerce(node.values, minitypes.bool_)
-        node.variable = Variable(minitypes.bool_)
+        node.values[:] = nodes.CoercionNode.coerce(node.values, typesystem.bool_)
+        node.variable = Variable(typesystem.bool_)
         return node
 
     def _handle_floordiv(self, node):
         dst_type = self.promote(node.left.variable, node.right.variable)
         if dst_type.is_float or dst_type.is_int:
             node.op = ast.Div()
             node = nodes.CoercionNode(node, long_)
@@ -846,36 +845,36 @@
             # TODO: Do this better
             typesystem.require(
                 [n for n in [node.left, node.right]
                        if self.is_resolved(n.variable.type)],
                 ["is_int", 'is_object', 'is_bool'])
 
         v1, v2 = node.left.variable, node.right.variable
-        promotion_type = self.promote(v1, v2)
+        promoted_type = self.promote(v1, v2)
 
-        if (v1.type.is_pointer or v2.type.is_pointer):
+        if promoted_type.is_pointer:
             self._verify_pointer_type(node, v1, v2)
         elif not ((v1.type.is_array and v2.type.is_array) or
                   (v1.type.is_unresolved or v2.type.is_unresolved)):
             # Don't coerce arrays to lesser or higher dimensionality
             # Broadcasting transforms should take care of this
             node.left, node.right = nodes.CoercionNode.coerce(
-                                [node.left, node.right], promotion_type)
+                                [node.left, node.right], promoted_type)
 
-        node.variable = Variable(promotion_type)
+        node.variable = Variable(promoted_type)
         if isinstance(node.op, ast.FloorDiv):
             node = self._handle_floordiv(node)
 
         return node
 
     def visit_UnaryOp(self, node):
         node.operand = self.visit(node.operand)
         if isinstance(node.op, ast.Not):
-            node.operand = nodes.CoercionNode(node.operand, minitypes.bool_)
-            node.variable = Variable(minitypes.bool_)
+            node.operand = nodes.CoercionNode(node.operand, typesystem.bool_)
+            node.variable = Variable(typesystem.bool_)
         else:
             node.variable = Variable(node.operand.variable.type)
 
         if isinstance(node.op, ast.Invert):
             typesystem.require([node], ["is_int", "is_object"])
 
         return node
@@ -885,15 +884,15 @@
         lhs = node.left
         comparators = node.comparators
         types = [lhs.variable.type] + [c.variable.type for c in comparators]
 
         result_type = bool_
 
         if len(set(types)) != 1:
-            type = reduce(self.context.promote_types, types)
+            type = reduce(self.promote_types, types)
             if type.is_array:
                 result_type = typesystem.array(bool_, type.ndim)
             else:
                 node.left = nodes.CoercionNode(lhs, type)
                 node.comparators = [nodes.CoercionNode(c, type)
                                     for c in comparators]
 
@@ -904,15 +903,15 @@
     # Indexing and Slicing
     #------------------------------------------------------------------------
 
     def _handle_struct_index(self, node, value_type):
         slice_type = node.slice.variable.type
 
         if not isinstance(node.slice, ast.Index) or not (
-                slice_type.is_int or slice_type.is_c_string):
+                slice_type.is_int or slice_type.is_string):
             raise error.NumbaError(node.slice,
                                    "Struct index must be a single string "
                                    "or integer")
 
         if not isinstance(node.slice.value, nodes.ConstNode):
             raise error.NumbaError(node.slice,
                                    "Struct index must be constant")
@@ -983,17 +982,17 @@
             elif isinstance(node.slice, ast.Tuple):
                 slices = list(node.slice.elts)
 
             if slices is None:
                 if slice_type.is_tuple:
                     # result_type = value_type[slice_type.size:]
                     # TODO: use slice_variable.constant_value if available
-                    result_type = minitypes.object_
+                    result_type = typesystem.object_
                 else:
-                    result_type = minitypes.object_
+                    result_type = typesystem.object_
             elif any(slice_node.variable.type.is_unresolved for slice_node in slices):
                 for slice_node in slices:
                     if slice_node.variable.type.is_unresolved:
                         deferred_type.dependences.append(slice_node)
 
                 deferred_type.update()
                 result_type = deferred_type
@@ -1019,15 +1018,15 @@
         elif value_type.is_pointer:
             self.assert_index(slice_variable.type, node.slice)
             result_type = value_type.base_type
 
         elif value_type.is_object:
             result_type = object_
 
-        elif value_type.is_c_string:
+        elif value_type.is_string:
             # Handle string indexing
             if slice_type.is_int:
                 result_type = char
             elif slice_type.is_slice:
                 result_type = c_string_type
             elif slice_type.is_unresolved:
                 deferred_type.dependences.append(node.slice)
@@ -1050,25 +1049,25 @@
     def visit_Index(self, node):
         "Normal index"
         node.value = self.visit(node.value)
         variable = node.value.variable
         type = variable.type
         if (type.is_object and variable.is_constant and
                 variable.constant_value is None):
-            type = typesystem.NewAxisType()
+            type = typesystem.newaxis
 
         node.variable = Variable(type)
         return node
 
     def visit_Ellipsis(self, node):
-        return nodes.ConstNode(Ellipsis, typesystem.EllipsisType())
+        return nodes.ConstNode(Ellipsis, typesystem.ellipsis)
 
     def visit_Slice(self, node):
         self.generic_visit(node)
-        type = typesystem.SliceType()
+        type = typesystem.slice_
 
         is_constant = False
         const = None
 
         values = [node.lower, node.upper, node.step]
         constants = []
         for value in values:
@@ -1084,15 +1083,15 @@
 
         node.variable = Variable(type, is_constant=is_constant,
                                  constant_value=const)
         return node
 
     def visit_ExtSlice(self, node):
         self.generic_visit(node)
-        node.variable = Variable(minitypes.object_)
+        node.variable = Variable(typesystem.object_)
         return node
 
     #------------------------------------------------------------------------
     # Constants
     #------------------------------------------------------------------------
 
     def visit_Num(self, node):
@@ -1127,24 +1126,24 @@
 
     def visit_Tuple(self, node):
         self.visitlist(node.elts)
         constant_value = self._get_constant_list(node)
         if constant_value is not None:
             constant_value = tuple(constant_value)
         # TODO: determine element type of node.elts
-        type = typesystem.TupleType(object_, size=len(node.elts))
+        type = typesystem.tuple_(object_, size=len(node.elts))
         node.variable = Variable(type, is_constant=constant_value is not None,
                                  constant_value=constant_value)
         return node
 
     def visit_List(self, node):
         node.elts = self.visitlist(node.elts)
         constant_value = self._get_constant_list(node)
         # TODO: determine element type of node.elts
-        type = typesystem.ListType(object_, size=len(node.elts))
+        type = typesystem.list_(object_, size=len(node.elts))
         node.variable = Variable(type, is_constant=constant_value is not None,
                                  constant_value=constant_value)
         return node
 
     def visit_Dict(self, node):
         self.generic_visit(node)
         constant_keys = self._get_constants(node.keys)
@@ -1152,21 +1151,21 @@
 
         if constant_keys and constant_values:
             unify = self.promote_types
             key_type = reduce(unify, (self.type_from_pyval(key)
                                       for key in constant_keys))
             value_type = reduce(unify, (self.type_from_pyval(key)
                                         for key in constant_keys))
-            type = typesystem.DictType(key_type, value_type, size=len(node.keys))
+            type = typesystem.dict_(key_type, value_type, size=len(node.keys))
 
             variable = Variable(type, is_constant=True,
                                 constant_value=dict(zip(constant_keys,
                                                         constant_values)))
         else:
-            type = typesystem.DictType(object_, object_, size=len(node.keys))
+            type = typesystem.dict_(object_, object_, size=len(node.keys))
             variable = Variable(type)
 
         node.variable = variable
         return node
 
     #------------------------------------------------------------------------
     # Function and Method Calls
@@ -1205,22 +1204,19 @@
                                 self, arg_types, call_node)
                 if (module_type_inference.is_registered(py_func) and
                         module_type_inference.can_handle_deferred(py_func)):
                     new_node = infer_call.infer_typefunc(self.context, call_node,
                                                          func_type, new_node)
         elif self.function_cache.is_registered(py_func):
             py_func = py_func.py_func
-            signature = minitypes.FunctionType(None, arg_types)
+            signature = typesystem.function(None, arg_types)
 
             jitted_func = numba.jit(signature)(py_func)
             signature = jitted_func.signature
             llvm_func = jitted_func.lfunc
-        #elif not call_node.keywords and self._is_math_function(call_node.args,
-        #                                                       py_func):
-        #    new_node = self._resolve_math_call(call_node, py_func)
         else:
             # This should not be a function-cache method
             # signature = self.function_cache.get_signature(arg_types)
             new_node = self._resolve_return_type(func_type, new_node,
                                                  call_node, arg_types)
 
         if llvm_func is not None:
@@ -1248,33 +1244,27 @@
             new_node.variable = Variable(func_type.base_type)
 
         return new_node
 
     def _infer_complex_math(self, func_type, new_node, node, argtype):
         "Infer types for cmath.somefunc()"
         # Check for cmath.{sqrt,sin,etc}
-        # FIXME: This is not visited when the input is a non-complex scalar.
-        #        In that case, Numba will bypass the cmath and generate
-        #        a LLVM math intrinsic call.
-        if not argtype.is_array:
-            args = [nodes.const(1.0, float_)]
-            is_math = is_math_function(args, func_type.value)
-            if len(node.args) == 1 and is_math:
-                new_node = nodes.CoercionNode(new_node, complex128)
+        if (len(node.args) == 1 and
+                func_type.value.__name__ in mathmodule.mathsyms):
+            new_node = nodes.CoercionNode(new_node, complex128)
 
         return new_node
 
     def _resolve_return_type(self, func_type, new_node, node, argtypes):
         """
         We are performing a call through PyObject_Call, but we may be able
         to infer a more specific return value than 'object'.
         """
         if ((func_type.is_module_attribute and func_type.module is cmath) or
-                 (func_type.is_numpy_attribute and len(argtypes) == 1 and
-                  argtypes[0].is_complex)):
+                 (func_type.is_numpy_attribute and len(argtypes) == 1)):
             new_node = self._infer_complex_math(
                     func_type, new_node, node, argtypes[0])
 
         return infer_call.infer_typefunc(self.context, node,
                                          func_type, new_node)
 
     def _resolve_autojit_method_call(self, call_node, ext_type, attr):
@@ -1340,19 +1330,19 @@
         if visitchildren:
             self.visitlist(node.args)
             self.visitlist(node.keywords)
 
         # TODO: Resolve variable types based on how they are used as arguments
         # TODO: in calls with known signatures
         new_node = None
-        if func_type.is_autojit_method:
+        if func_type.is_autojit_extmethod:
             assert isinstance(node.func, nodes.ExtensionMethod)
             new_node = self._resolve_autojit_method_call(
                 node, node.func.ext_type, node.func.attr)
-        if func_type.is_function:
+        if func_type.is_function or func_type.is_extmethod:
             # Native function call
             no_keywords(node)
             new_node = nodes.NativeFunctionCallNode(
                             func_variable.type, node.func, node.args,
                             skip_self=True)
         elif func_type.is_method:
             # Call to special object method
@@ -1367,16 +1357,15 @@
 
         elif func_type.is_pointer_to_function:
             # Call to ctypes function
             no_keywords(node)
             new_node = nodes.PointerCallNode(
                     func_type.signature,
                     node.args,
-                    func_type.pointer,
-                    py_func=func_type.obj)
+                    func_type.ptr)
 
         elif func_type.is_cast:
             # Call of a numba type
             # 1) double(value) -> cast value to double
             # 2) double() or double(object_, double), ->
             #       this specifies a function signature
             no_keywords(node)
@@ -1417,33 +1406,33 @@
         "Resolve attributes of the numpy module or a submodule"
         attribute = getattr(type.module, node.attr)
 
         # TODO: Do this better
 
         result_type = None
         if attribute is numpy.newaxis:
-            result_type = typesystem.NewAxisType()
+            result_type = typesystem.newaxis
         elif attribute is numba.NULL:
-            return typesystem.null_type
+            return typesystem.null
         elif type.is_numpy_module or type.is_numpy_attribute:
-            result_type = typesystem.NumpyAttributeType(module=type.module,
+            result_type = typesystem.numpy_attribute(module=type.module,
                                                          attr=node.attr)
         elif type.is_numba_module or type.is_math_module:
             result_type = self.context.typemapper.from_python(attribute)
             if result_type == object_:
                 result_type = None
 
         if result_type is None:
             if hasattr(type.module, node.attr):
                 result_type = self.type_from_pyval(getattr(type.module,
                                                            node.attr))
                 if result_type != object_:
                     return result_type
 
-            result_type = typesystem.ModuleAttributeType(module=type.module,
+            result_type = typesystem.module_attribute(module=type.module,
                                                          attr=node.attr)
 
         return result_type
 
     def _resolve_ndarray_attribute(self, array_node, array_attr):
         "Resolve attributes of numpy arrays"
         return
@@ -1513,33 +1502,33 @@
 
         return result_type
 
     def visit_Attribute(self, node):
         node.value = self.visit(node.value)
         type = node.value.variable.type
         if node.attr == 'conjugate' and (type.is_complex or type.is_float):
-            result_type = typesystem.MethodType(type, 'conjugate')
+            result_type = typesystem.method(type, 'conjugate')
         elif type.is_complex:
             result_type = self._resolve_complex_attribute(node, type)
         elif type.is_struct or (type.is_reference and
                                 type.referenced_type.is_struct):
             return self._resolve_struct_attribute(node, type)
         elif type.is_module and hasattr(type.module, node.attr):
             result_type = self._resolve_module_attribute(node, type)
         elif (type.is_known_value and
                   module_type_inference.is_registered((type.value, node.attr))):
             # Unbound method call, e.g. np.add.reduce
-            result_type = typesystem.KnownValueType((type.value, node.attr),
+            result_type = typesystem.known_value((type.value, node.attr),
                                                     is_object=True)
         elif type.is_array and node.attr in ('data', 'shape', 'strides', 'ndim'):
             # handle shape/strides/ndim etc
             return nodes.ArrayAttributeNode(node.attr, node.value)
         elif type.is_array and node.attr == "dtype":
             # TODO: resolve as constant at compile time?
-            result_type = typesystem.dtype(type.dtype)
+            result_type = typesystem.numpy_dtype(type.dtype)
         elif type.is_extension:
             return self._resolve_extension_attribute(node, type)
         else:
             # use PyObject_GetAttrString
             node.value = nodes.CoercionNode(node.value, object_)
             result_type = object_
 
@@ -1642,15 +1631,15 @@
     def visit_Name(self, node):
         return node
 
     def visit_ExtSlice(self, node):
         self.generic_visit(node)
         types = [n.type for n in node.dims]
         if all(type.is_int for type in types):
-            node.type = reduce(self.context.promote_types, types)
+            node.type = reduce(self.env.crnt.typesystem.promote, types)
         else:
             node.type = object_
 
         return node
 
     def visit_DeferredCoercionNode(self, node):
         "Resolve deferred coercions"
```

### Comparing `numba-0.8.1/numba/type_inference/module_type_inference.py` & `numba-0.9.0/numba/type_inference/module_type_inference.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,17 +7,16 @@
 from __future__ import print_function, division, absolute_import
 
 import ast
 import inspect
 
 import numba
 from numba import *
-from numba.minivect import minitypes
 from numba import typesystem, error, nodes
-from numba.typesystem import get_type, typeset
+from numba.typesystem import get_type, typeset, Type
 
 import logging
 
 debug = False
 #debug = True
 
 logger = logging.getLogger(__name__)
@@ -149,15 +148,15 @@
     """
     See if the object is registered to any module which might handle
     type inference on the object.
     """
     result = module_registry.lookup_module_attribute(obj)
     if result is not None:
         module, attr = result
-        return typesystem.ModuleAttributeType(module=module, attr=attr)
+        return typesystem.module_attribute(module=module, attr=attr)
 
     return None
 
 def parse_args(call_node, arg_names):
     """
     Parse positional and keyword arguments.
     """
@@ -178,15 +177,15 @@
     return result
 
 def _build_arg(pass_in_types, node):
     if pass_in_types:
         return get_type(node)
     return node
 
-def dispatch_on_value(context, call_node, func_type):
+def dispatch_on_value(context, call_node, func_type): # TODO: Pass in typesystem here
     """
     Dispatch a call of a module attribute by value.
 
     For instance, a method
 
         def empty(shape, dtype, order):
             ...
@@ -199,17 +198,19 @@
     inferer, flags = get_inferer(func_type.value)
 
     # Detect needed arguments
     argspec = inspect.getargspec(inferer)
 
     # Pass in additional arguments (context and call_node)
     argnames = argspec.args
-    if argnames and argnames[0] == "context":
+    if argnames and argnames[0] in ("context", "typesystem"):
         argnames.pop(0)
-        args = [context]
+        # TODO: Remove this and reference in mathmodule.infer_unary_math_call
+        context.env.crnt.typesystem.env = context.env
+        args = [context.env.crnt.typesystem]
     else:
         args = []
 
     if flags['pass_in_callnode']:
         argnames.pop(0)
         args.append(call_node)
 
@@ -245,26 +246,26 @@
 
         call_node:     the original ast.Call node that we need to resolve
                        the type for
 
         obj_call_node: the nodes.ObjectCallNode that would replace the
                        ast.Call unless we override that with another node.
 
-        func_type: ModuleAttributeType
+        func_type: module_attribute
             |__________> module: Python module
             |__________> attr: Attribute name
             |__________> value: Attribute value
 
 
     Returns a new AST node that should replace the ast.Call node.
     """
     result = dispatch_on_value(context, call_node, func_type)
 
     if result is not None and not isinstance(result, ast.AST):
-        assert isinstance(result, minitypes.Type)
+        assert isinstance(result, Type), (Type, result)
         type = result
         result = obj_call_node
         # result.variable = symtab.Variable(type)
         result = nodes.CoercionNode(result, type)
 
     return result
 
@@ -300,45 +301,43 @@
         register_inferer(module, inferer.__name__, inferer, **kws)
         return inferer
 
     return decorator
 
 def register_callable(signature):
     """
-    signature := FunctionType | typeset(signature *)
+    signature := function | typeset(signature *)
 
     @register_callable(signature)
     def my_function(...):
         ...
     """
-    assert isinstance(signature, (typeset.typeset, minitypes.Type))
+    assert isinstance(signature, (typeset.typeset, Type))
 
     # convert void return type to object_ (None)
     def convert_void_to_object(sig):
-        from copy import copy
         if sig.return_type == void:
-            sig = copy(sig)
-            sig.return_type = object_
+            sig = sig.add('return_type', object_)
         return sig
 
     if isinstance(signature, typeset.typeset):
         signature = typeset.typeset([convert_void_to_object(x)
                                      for x in signature.types],
                                     name=signature.name)
     else:
-        assert isinstance(signature, minitypes.Type)
+        assert isinstance(signature, Type)
         signature = convert_void_to_object(signature)
 
 
     def decorator(function):
-        def infer(context, *args):
+        def infer(typesystem, *args):
             if signature.is_typeset:
-                specialization = signature.find_match(context, args)
+                specialization = signature.find_match(typesystem.promote, args)
             else:
-                specialization = typeset.match(context, signature, args)
+                specialization = typeset.match(typesystem.promote, signature, args)
 
             if specialization is None:
                 raise UnmatchedTypeError(
                         "Unmatched argument types for function '%s': %s" %
                                                     (function.__name__, args))
 
             assert specialization.is_function
```

### Comparing `numba-0.8.1/numba/type_inference/tests/test_user_type_inference.py` & `numba-0.9.0/numba/type_inference/tests/test_user_type_inference.py`

 * *Files 6% similar despite different names*

```diff
@@ -40,11 +40,11 @@
 def test_register_callable():
     assert use_user_type_function() == int32
     assert use_typeset_function_simple() == int32
 
     assert use_typeset_function_binding(double, double) == double
     assert use_typeset_function_binding(float_, double) == double
     assert use_typeset_function_binding(int_, float_) == float_
-    assert use_typeset_function_binding(int_, long_) == long_
+    assert use_typeset_function_binding(int_, long_).itemsize == long_.itemsize
 
 if __name__ == '__main__':
     test_register_callable()
```

### Comparing `numba-0.8.1/numba/type_inference/tests/test_typesets.py` & `numba-0.9.0/numba/type_inference/tests/test_typesets.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,30 +1,29 @@
 import numba
 from numba import *
-from numba.typesystem import typeset
+from numba.typesystem import typeset, promote
 from numba.environment import NumbaEnvironment
 
 def s(type):
     return type(type, type)
 
-def test_typeset_matching():
-    context = NumbaEnvironment.get_environment().context
-
+def typeset_matching():
     numeric = typeset.typeset([int_, longlong])
     n = numeric(numeric, numeric)
     f = numba.floating(numba.floating, numba.floating)
 
     signatures = [n, f, object_(object_, object_)]
     ts = typeset.typeset(signatures)
 
-    assert ts.find_match(context, [float_, float_]) == s(float_)
-    assert ts.find_match(context, [float_, double]) == s(double)
-    assert ts.find_match(context, [longdouble, float_]) == s(longdouble)
-
-    assert ts.find_match(context, [int_, int_]) == s(int_)
-    assert ts.find_match(context, [int_, longlong]) == s(longlong)
-    assert ts.find_match(context, [short, int_]) == s(int_)
+    assert ts.find_match(promote, [float_, float_]) == s(float_)
+    assert ts.find_match(promote, [float_, double]) == s(double)
+    assert ts.find_match(promote, [longdouble, float_]) == s(longdouble)
+
+    assert ts.find_match(promote, [int_, int_]) == s(int_)
+    # assert ts.find_match(promote, [int_, longlong]) == s(longlong)
+    # assert ts.find_match(promote, [short, int_]) == s(int_)
 
-    assert ts.find_match(context, [short, ulonglong]) is None
+    # np.result_type(np.short, np.ulonglong) -> np.float64
+    # assert ts.find_match(promote, [short, ulonglong]) is None
 
 if __name__ == '__main__':
-    test_typeset_matching()
+    typeset_matching()
```

### Comparing `numba-0.8.1/numba/type_inference/tests/test_type_inference.py` & `numba-0.9.0/numba/type_inference/tests/test_type_inference.py`

 * *Files 3% similar despite different names*

```diff
@@ -146,19 +146,20 @@
     def test_simple_for(self):
          self.assertEqual(for_loop(0, 10, 1), 45)
 
     def test_type_infer_simple_func(self):
         sig, symtab = infer(_simple_func, functype(None, [double]))
         self.assertEqual(sig.return_type, double)
 
-    def test_type_infer_for_loop(self):
-        sig, symtab = infer(_for_loop, functype(None, [int_, int_, int_]))
-        self.assertTrue(symtab['acc'].type.is_int)
-        self.assertEqual(symtab['value'].type, Py_ssize_t)
-        self.assertEqual(sig.return_type, Py_ssize_t)
+    # TODO: Re-enable once we flesh out the exact type promotion rules
+    # def test_type_infer_for_loop(self):
+    #     sig, symtab = infer(_for_loop, functype(None, [int_, int_, int_]))
+    #     self.assertTrue(symtab['acc'].type.is_int)
+    #     self.assertEqual(symtab['value'].type, Py_ssize_t)
+    #     self.assertEqual(sig.return_type, Py_ssize_t)
 
     def test_type_infer_arange(self):
         sig, symtab = infer(arange, functype())
         self.assertEqual(symtab['a'].type, npy_intp[:])
         self.assertEqual(symtab['b'].type, double[:])
 
     def test_empty_like(self):
@@ -175,17 +176,17 @@
         for i in range(4, 8):
             self.assertEqual(symtab['a%d' % i].type, float_[:])
 
         self.assertEqual(symtab['a8'].type, int64[:, :])
 
     def test_empty_arg(self):
         from numba import typesystem as nt
-        empty_t = nt.ModuleAttributeType(module=np, attr='empty')
-        zeros_t = nt.ModuleAttributeType(module=np, attr='zeros')
-        ones_t = nt.ModuleAttributeType(module=np, attr='ones')
+        empty_t = nt.module_attribute(module=np, attr='empty')
+        zeros_t = nt.module_attribute(module=np, attr='zeros')
+        ones_t = nt.module_attribute(module=np, attr='ones')
 
         sig, symtab = infer(_empty_arg, functype(None, [int_, empty_t,
                                                         zeros_t, ones_t]))
         for i in range(1, 4):
             self.assertEqual(symtab['a%d' % i].type, double[:])
 
     def test_dtype_attribute(self):
@@ -194,15 +195,15 @@
         A_result = assert_array_dtype(A, 3, np.empty, np.zeros, np.ones)
         assert np.all(A_result == 0)
         A_result = assert_array_dtype(A, 5, np.empty, np.zeros, np.ones)
         assert np.all(A_result == 1)
 
     def test_slicing(self):
         sig, symtab = infer(slicing, functype(None, [double[:]]))
-        self.assertEqual(symtab['n'].type, typesystem.NewAxisType())
+        self.assertEqual(symtab['n'].type, typesystem.newaxis)
 
         self.assertEqual(symtab['b'].type, double)
         self.assertEqual(symtab['c'].type, double)
         self.assertEqual(symtab['d'].type, double[:])
         self.assertEqual(symtab['e'].type, double[:])
         self.assertEqual(symtab['f'].type, double[:, :])
         self.assertEqual(symtab['g'].type, double[:, :])
```

### Comparing `numba-0.8.1/numba/type_inference/infer_call.py` & `numba-0.9.0/numba/type_inference/infer_call.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,15 +32,15 @@
         func = func_type.jit_func
 
     return func
 
 def infer_typefunc(context, call_node, func_type, default_node):
     func_var = call_node.func.variable
     if func_var.is_constant:
-        func_type = typesystem.KnownValueType(func_var.constant_value)
+        func_type = typesystem.known_value(func_var.constant_value)
 
     if (func_type.is_known_value and
             module_type_inference.is_registered(func_type.value)):
         # Try the module type inferers
         result_node = module_type_inference.resolve_call_or_none(
                                     context, call_node, func_type)
         if result_node:
@@ -53,9 +53,9 @@
     for arg in node.args:
         if not arg.variable.type.is_cast:
             raise error.NumbaError(arg, "Expected a numba type")
         else:
             types.append(arg.variable.type)
 
     signature = func_type.dst_type(*types)
-    new_node = nodes.const(signature, typesystem.CastType(signature))
+    new_node = nodes.const(signature, typesystem.meta(signature))
     return new_node
```

### Comparing `numba-0.8.1/numba/type_inference/deferred.py` & `numba-0.9.0/numba/type_inference/deferred.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/type_inference/modules/numpymodule.py` & `numba-0.9.0/numba/type_inference/modules/numpymodule.py`

 * *Files 24% similar despite different names*

```diff
@@ -13,15 +13,14 @@
 
 import warnings
 from functools import reduce
 
 import numpy as np
 
 from numba import *
-from numba.minivect import minitypes
 from numba import typesystem, error
 from numba.type_inference.module_type_inference import (register,
                                                         register_inferer,
                                                         register_unbound)
 from numba.typesystem import get_type
 
 
@@ -31,16 +30,16 @@
 
 index_array_t = npy_intp[:]
 
 #------------------------------------------------------------------------
 # Some utilities
 #------------------------------------------------------------------------
 
-def promote(context, *types):
-    return reduce(context.promote_types, map(array_from_type, types))
+def promote(typesystem, *types):
+    return reduce(typesystem.promote, map(array_from_type, types))
 
 def resolve_attribute_dtype(dtype, default=None):
     "Resolve the type for numpy dtype attributes"
     if dtype.is_numpy_dtype:
         return dtype
 
     if dtype.is_known_value:
@@ -64,22 +63,22 @@
     Simple helper function to map an AST node dtype keyword
     argument => NumPy dtype.
     '"""
     if dtype_arg is None:
         if default_dtype is None:
             return None
 
-        return typesystem.dtype(default_dtype)
+        return typesystem.numpy_dtype(default_dtype)
     else:
         return resolve_attribute_dtype(dtype_arg)
 
 def promote_to_array(dtype):
     "Promote scalar to 0d array type"
     if not dtype.is_array:
-        dtype = minitypes.ArrayType(dtype, 0)
+        dtype = typesystem.array_(dtype, 0)
     return dtype
 
 def demote_to_scalar(type):
     "Demote 0d arrays to scalars"
     if type and type.is_array and type.ndim == 0:
         return type.dtype
     return type
@@ -94,19 +93,17 @@
 
 def array_from_type(type):
     if type.is_array:
         return type
     elif type.is_tuple or type.is_list:
         dtype = array_from_type(type.base_type)
         if dtype.is_array:
-            type = dtype.copy()
-            type.ndim += 1
-            return type
+            return dtype.add('ndim', type.ndim + 1)
     elif not type.is_object:
-        return minitypes.ArrayType(dtype=type, ndim=0)
+        return typesystem.array(dtype=type, ndim=0)
 
     return object_
 
 #------------------------------------------------------------------------
 # Resolution of NumPy calls
 #------------------------------------------------------------------------
 
@@ -166,89 +163,89 @@
     # parameter
     dtype_type = get_dtype(dtype, npy_intp)
     if dtype_type is not None:
         # return a 1D array type of the given dtype
         return dtype_type.dtype[:]
 
 @register(np)
-def dot(context, a, b, out):
+def dot(typesystem, a, b, out):
     "Resolve a call to np.dot()"
     if out is not None:
         return out
 
     lhs_type = promote_to_array(a)
     rhs_type = promote_to_array(b)
 
-    dtype = context.promote_types(lhs_type.dtype, rhs_type.dtype)
+    dtype = typesystem.promote(lhs_type.dtype, rhs_type.dtype)
     dst_ndim = lhs_type.ndim + rhs_type.ndim - 2
 
     result_type = typesystem.array(dtype, dst_ndim)
     return result_type
 
 @register(np)
 def array(object, dtype, order, subok):
     type = array_from_type(object)
     if type.is_array and dtype is not None:
-        type = type.copy(dtype=dtype)
+        type = type.add('dtype', dtype)
     elif dtype is not None:
         return dtype
     else:
         return type
 
 @register(np)
 def nonzero(a):
     return _nonzero(array_from_type(a))
 
 def _nonzero(type):
     if type.is_array:
-        return typesystem.TupleType(index_array_t, type.ndim)
+        return typesystem.tuple_(index_array_t, type.ndim)
     else:
-        return typesystem.TupleType(index_array_t)
+        return typesystem.tuple_(index_array_t)
 
 @register(np)
-def where(context, condition, x, y):
+def where(typesystem, condition, x, y):
     if x is None and y is None:
         return nonzero(condition)
 
-    return promote(context, x, y)
+    return promote(typesystem, x, y)
 
 @register(np)
-def vdot(context, a, b):
+def vdot(typesystem, a, b):
     lhs_type = promote_to_array(a)
     rhs_type = promote_to_array(b)
-    dtype = context.promote_types(lhs_type.dtype, rhs_type.dtype)
+    dtype = typesystem.promote(lhs_type.dtype, rhs_type.dtype)
     return dtype
 
 @register(np)
-def inner(context, a, b):
+def inner(typesystem, a, b):
     lhs_type = promote_to_array(a)
     rhs_type = promote_to_array(b)
-    dtype = context.promote_types(lhs_type.dtype, rhs_type.dtype)
+    dtype = typesystem.promote(lhs_type.dtype, rhs_type.dtype)
     if lhs_type.ndim == 0:
         result_ndim = rhs_type.ndim
     elif rhs_type.ndim == 0:
         result_ndim = lhs_type.ndim
     else:
         result_ndim = lhs_type.ndim + rhs_type.ndim - 2
     if result_ndim == 0:
         result_type = dtype
     else:
         result_type = typesystem.array(dtype, result_ndim)
     return result_type
 
 @register(np)
-def outer(context, a, b):
-    result_type = promote(context, a, b)
+def outer(typesystem, a, b):
+    result_type = promote(typesystem, a, b)
     # promote() converts scalar types to 0-dim arrays, so it should
     # always return an array type.  Ensure this continues to hold...
     assert result_type.is_array
     return result_type.dtype[:, :]
 
 @register(np, pass_in_types=False)
-def tensordot(context, a, b, axes):
+def tensordot(typesystem, a, b, axes):
     '''Typing function for numpy.tensordot().
 
     Defaults to Python object for any caller that isn't using the
     default argument to axes.
 
     Otherwise, it is similar to inner(), but subtracts four dimensions
     from the result instead of two.
@@ -263,134 +260,134 @@
     rhs_type = array_from_object(b)
     if lhs_type.ndim < 1:
         raise error.NumbaError(a, 'First argument to numpy.tensordot() '
                                'requires array of dimensionality >= 1.')
     elif rhs_type.ndim < 1:
         raise error.NumbaError(b, 'First argument to numpy.tensordot() '
                                'requires array of dimensionality >= 1.')
-    dtype = context.promote_types(lhs_type.dtype, rhs_type.dtype)
+    dtype = typesystem.promote(lhs_type.dtype, rhs_type.dtype)
     if axes is None:
         result_ndim = lhs_type.ndim + rhs_type.ndim - 4
         if result_ndim < 0:
             raise error.NumbaError(a, 'Arguments to numpy.tensordot() should '
                                    'have combined dimensionality >= 4 (when '
                                    'axes argument is not specified).')
         result_type = typesystem.array(dtype, result_ndim)
     else:
         # XXX Issue warning to user?
         result_type = object_
     return result_type
 
 @register(np)
-def einsum(context, subs, operands, kws):
+def einsum(typesystem, subs, operands, kws):
     # XXX Issue warning to user?
     # XXX Attempt type inference in case where subs is a string?
     return object_
 
 @register(np)
-def kron(context, a, b):
+def kron(typesystem, a, b):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np)
-def trace(context, a, offset, axis1, axis2, dtype, out):
+def trace(typesystem, a, offset, axis1, axis2, dtype, out):
     #raise NotImplementedError("XXX")
     return object_
 
 #------------------------------------------------------------------------
 # numpy.linalg
 #------------------------------------------------------------------------
 
 @register(np.linalg)
-def cholesky(context, a):
+def cholesky(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def cond(context, x, p):
+def cond(typesystem, x, p):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def det(context, a):
+def det(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def eig(context, a):
+def eig(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def eigh(context, a, UPLO):
+def eigh(typesystem, a, UPLO):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def eigvals(context, a):
+def eigvals(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def eigvalsh(context, a, UPLO):
+def eigvalsh(typesystem, a, UPLO):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def inv(context, a):
+def inv(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def lstsq(context, a, b, rcond):
+def lstsq(typesystem, a, b, rcond):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def matrix_power(context, M, n):
+def matrix_power(typesystem, M, n):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def matrix_rank(context, M, tol):
+def matrix_rank(typesystem, M, tol):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def norm(context, x, ord):
+def norm(typesystem, x, ord):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def pinv(context, a, rcond):
+def pinv(typesystem, a, rcond):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def qr(context, a, mode):
+def qr(typesystem, a, mode):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def slogdet(context, a):
+def slogdet(typesystem, a):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def solve(context, a, b):
+def solve(typesystem, a, b):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def svd(context, a, full_matrices, compute_uv):
+def svd(typesystem, a, full_matrices, compute_uv):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def tensorinv(context, a, ind):
+def tensorinv(typesystem, a, ind):
     #raise NotImplementedError("XXX")
     return object_
 
 @register(np.linalg)
-def tensorsolve(context, a, b, axes):
+def tensorsolve(typesystem, a, b, axes):
     #raise NotImplementedError("XXX")
     return object_
```

### Comparing `numba-0.8.1/numba/type_inference/modules/utils.py` & `numba-0.9.0/numba/type_inference/modules/utils.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/type_inference/modules/numpyufuncs.py` & `numba-0.9.0/numba/type_inference/modules/numpyufuncs.py`

 * *Files 14% similar despite different names*

```diff
@@ -3,16 +3,16 @@
 Type inference for NumPy binary ufuncs and their methods.
 """
 from __future__ import print_function, division, absolute_import
 
 import numpy as np
 
 from numba import *
-from numba.minivect import minitypes
 from numba import typesystem
+from numba.typesystem import numpy_support
 from numba.type_inference.module_type_inference import (module_registry,
                                                         register,
                                                         register_inferer,
                                                         register_unbound)
 from numba.typesystem import get_type
 from numba.type_inference.modules.numpymodule import (get_dtype,
                                                       array_from_type,
@@ -25,18 +25,18 @@
 #----------------------------------------------------------------------------
 
 def array_of_dtype(a, dtype, static_dtype, out):
     if out is not None:
         return out
 
     a = array_from_type(a)
-    if not a.is_object:
+    if a.is_array:
         dtype = _dtype(a, dtype, static_dtype)
         if dtype is not None:
-            return a.copy(dtype=dtype)
+            return a.add('dtype', dtype)
 
 def _dtype(a, dtype, static_dtype):
     if static_dtype:
         return static_dtype
     elif dtype:
         return dtype.dtype
     elif a.is_array:
@@ -48,71 +48,71 @@
 
 #------------------------------------------------------------------------
 # Ufunc Type Strings
 #------------------------------------------------------------------------
 
 def numba_type_from_sig(ufunc_signature):
     """
-    Convert ufunc type signature string (e.g. 'dd->d') to a FunctionType
+    Convert ufunc type signature string (e.g. 'dd->d') to a function
     """
     args, ret = ufunc_signature.split('->')
-    to_numba = lambda c: minitypes.map_dtype(np.dtype(c))
+    to_numba = lambda c: numpy_support.map_dtype(np.dtype(c))
 
     signature = to_numba(ret)(*map(to_numba, args))
     return signature
 
 def find_signature(args, signatures):
     for signature in signatures:
         if signature.args == args:
             return signature
 
-def find_ufunc_signature(context, argtypes, signatures):
+def find_ufunc_signature(typesystem, argtypes, signatures):
     """
     Map (float_, double) and [double(double, double),
                               int_(int_, int_),
                               ...]
     to double(double, double)
     """
     signature = find_signature(tuple(argtypes), signatures)
 
     if signature is not None:
         return signature
 
-    argtype = reduce(context.promote_types, argtypes)
+    argtype = reduce(typesystem.promote, argtypes)
     if not argtype.is_object:
         args = (argtype,) * len(argtypes)
         return find_signature(args, signatures)
 
     return None
 
 class UfuncTypeInferer(object):
     "Infer types for arbitrary ufunc"
 
     def __init__(self, ufunc):
         self.ufunc = ufunc
         self.signatures = set(map(numba_type_from_sig, ufunc.types))
 
-    def infer(self, context, argtypes):
-        signature = find_ufunc_signature(context, argtypes, self.signatures)
+    def infer(self, typesystem, argtypes):
+        signature = find_ufunc_signature(typesystem, argtypes, self.signatures)
         if signature is None:
             return None
         else:
             return signature.return_type
 
 def register_arbitrary_ufunc(ufunc):
     "Type inference for arbitrary ufuncs"
     ufunc_infer = UfuncTypeInferer(ufunc)
 
-    def infer(context, *args, **kwargs):
+    def infer(typesystem, *args, **kwargs):
         if len(args) != ufunc.nin:
             return object_
 
         # Find the right ufunc signature
         argtypes = [type.dtype if type.is_array else type for type in args]
-        result_type = ufunc_infer.infer(context, argtypes)
+        result_type = ufunc_infer.infer(typesystem, argtypes)
 
         if result_type is None:
             return object_
 
         # Determine output ndim
         ndim = 0
         for argtype in args:
@@ -124,24 +124,24 @@
     module_registry.register_value(ufunc, infer)
     # module_registry.register_unbound_dotted_value
 
 #----------------------------------------------------------------------------
 # Ufunc type inference
 #----------------------------------------------------------------------------
 
-def binary_map(context, a, b, out):
+def binary_map(typesystem, a, b, out):
     if out is not None:
         return out
 
-    return promote(context, a, b)
+    return promote(typesystem, a, b)
 
-def binary_map_bool(context, a, b, out):
-    type = binary_map(context, a, b, out)
+def binary_map_bool(typesystem, a, b, out):
+    type = binary_map(typesystem, a, b, out)
     if type.is_array:
-        return type.copy(dtype=bool_)
+        return type.add('dtype', bool_)
     else:
         return bool_
 
 def reduce_(a, axis, dtype, out, static_dtype=None):
     if out is not None:
         return out
 
@@ -174,21 +174,21 @@
 
 def reduceat(a, indices, axis, dtype, out, static_dtype=None):
     return accumulate(a, axis, dtype, out, static_dtype)
 
 def reduceat_bool(a, indices, axis, dtype, out):
     return reduceat(a, indices, axis, dtype, out, bool_)
 
-def outer(context, a, b, static_dtype=None):
+def outer(typesystem, a, b, static_dtype=None):
     a = array_of_dtype(a, None, static_dtype, out=None)
     if a and a.is_array:
         return a.dtype[:, :]
 
-def outer_bool(context, a, b):
-    return outer(context, a, b, bool_)
+def outer_bool(typesystem, a, b):
+    return outer(typesystem, a, b, bool_)
 
 #------------------------------------------------------------------------
 # Binary Ufuncs
 #------------------------------------------------------------------------
 
 binary_ufuncs_compare = (
     # Comparisons
```

### Comparing `numba-0.8.1/numba/type_inference/modules/mathmodule.py` & `numba-0.9.0/numba/type_inference/modules/mathmodule.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,162 +1,173 @@
 # -*- coding: utf-8 -*-
 """
 Resolve calls to math functions.
 
-During type inference this produces MathNode nodes, and during
+During type inference this annotates math calls, and during
 final specialization it produces LLVMIntrinsicNode and MathCallNode
 nodes.
 """
 from __future__ import print_function, division, absolute_import
 
 import math
 import cmath
+import collections
 try:
     import __builtin__ as builtins
 except ImportError:
     import builtins
 
 import numpy as np
 
 from numba import *
 from numba import nodes
 from numba.symtab import Variable
-from numba.typesystem import get_type
+from numba.typesystem import get_type, rank
 from numba.type_inference.modules import utils
 
-
 #----------------------------------------------------------------------------
 # Utilities
 #----------------------------------------------------------------------------
 
 register_math_typefunc = utils.register_with_argchecking
 
-def binop_type(context, x, y):
+def binop_type(typesystem, x, y):
     "Binary result type for math operations"
     x_type = get_type(x)
     y_type = get_type(y)
-    return context.promote_types(x_type, y_type)
+    return typesystem.promote(x_type, y_type)
 
 #----------------------------------------------------------------------------
 # Determine math functions
 #----------------------------------------------------------------------------
 
 # sin(double), sinf(float), sinl(long double)
-unary_libc_math_funcs = [
+mathsyms = [
     'sin',
     'cos',
     'tan',
     'sqrt',
     'acos',
     'asin',
     'atan',
-    'atan2',
     'sinh',
     'cosh',
     'tanh',
     'asinh',
     'acosh',
     'atanh',
     'log',
     'log2',
     'log10',
-    'fabs',
     'erfc',
+    'floor',
     'ceil',
     'exp',
     'exp2',
     'expm1',
     'rint',
     'log1p',
 ]
 
-n_ary_libc_math_funcs = [
-    'pow',
-    'round',
-]
+n_ary_mathsyms = {
+    'hypot'     : 2,
+    'atan2'     : 2,
+    'logaddexp' : 2,
+    'logaddexp2': 2,
+}
+
+math2ufunc = {
+    'asin' : 'arcsin',
+    'acos' : 'arccos',
+    'atan' : 'arctan',
+    'asinh': 'arcsinh',
+    'acosh': 'arccosh',
+    'atanh': 'arctanh',
+    'atan2': 'arctan2',
+    'pow'  : 'power',
+}
 
-all_libc_math_funcs = unary_libc_math_funcs + n_ary_libc_math_funcs
+ufunc2math = dict((v, k) for k, v in math2ufunc.items())
 
 #----------------------------------------------------------------------------
 # Math Type Inferers
 #----------------------------------------------------------------------------
 
 # TODO: Move any rewriting parts to lowering phases
 
-def infer_unary_math_call(context, call_node, arg, default_result_type=double):
-    "Resolve calls to math functions to llvm.log.f32() etc"
-    # signature is a generic signature, build a correct one
-    type = get_type(call_node.args[0])
-
-    if type.is_numeric and type.kind < default_result_type.kind:
-        type = default_result_type
-    elif type.is_array and type.dtype.is_int:
-        type = type.copy(dtype=double)
-
-    # signature = minitypes.FunctionType(return_type=type, args=[type])
-    # result = nodes.MathNode(py_func, signature, call_node.args[0])
-    nodes.annotate(context.env, call_node, is_math=True)
-    call_node.variable = Variable(type)
-    return call_node
+def mk_infer_math_call(default_result_type):
+    def infer(typesystem, call_node, *args):
+        "Resolve calls to llvmmath math calls"
+        # signature is a generic signature, build a correct one
+        type = reduce(typesystem.promote, map(get_type, call_node.args))
+
+        if type.is_numeric and rank(type) < rank(default_result_type):
+            type = default_result_type
+        elif type.is_array and type.dtype.is_int:
+            type = typesystem.array(double, type.ndim)
+
+        call_node.args[:] = nodes.CoercionNode.coerce(call_node.args, type)
+
+        # TODO: Remove the abuse below
+        nodes.annotate(typesystem.env, call_node, is_math=True)
+        call_node.variable = Variable(type)
+        return call_node
 
-def infer_unary_cmath_call(context, call_node, arg):
-    result = infer_unary_math_call(context, call_node, arg,
-                                   default_result_type=complex128)
-    nodes.annotate(context.env, call_node, is_cmath=True)
-    return result
+    return infer
+
+infer_math_call = mk_infer_math_call(double)
+infer_cmath_call = mk_infer_math_call(complex128)
 
 # ______________________________________________________________________
 # pow()
 
-def pow_(context, call_node, node, power, mod=None):
-    dst_type = binop_type(context, node, power)
+def pow_(typesystem, call_node, node, power, mod=None):
+    dst_type = binop_type(typesystem, node, power)
     call_node.variable = Variable(dst_type)
     return call_node
 
 register_math_typefunc((2, 3), math.pow)
 register_math_typefunc(2, np.power)
 
 # ______________________________________________________________________
 # abs()
 
-def abs_(context, node, x):
+def abs_(typesystem, node, x):
     import builtinmodule
 
     argtype = get_type(x)
 
     if argtype.is_array and argtype.is_numeric:
         # Handle np.abs() on arrays
         dtype = builtinmodule.abstype(argtype.dtype)
-        result_type = argtype.copy(dtype=dtype)
+        result_type = argtype.add('dtype', dtype)
         node.variable = Variable(result_type)
         return node
 
-    return builtinmodule.abs_(context, node, x)
+    return builtinmodule.abs_(typesystem, node, x)
 
 register_math_typefunc(1, np.abs)
 
 #----------------------------------------------------------------------------
 # Register Type Functions
 #----------------------------------------------------------------------------
 
-def register_math(nargs, value):
+def register_math(infer_math_call, nargs, value):
     register = register_math_typefunc(nargs)
-    register(infer_unary_math_call, value)
+    register(infer_math_call, value)
 
-def register_cmath(nargs, value):
-    register = register_math_typefunc(nargs)
-    register(infer_unary_cmath_call, value)
+def npy_name(name):
+    return math2ufunc.get(name, name)
 
-def register_typefuncs():
-    modules = [builtins, math, cmath, np]
-    # print all_libc_math_funcs
-    for libc_math_func in unary_libc_math_funcs:
-        for module in modules:
-            if hasattr(module, libc_math_func):
-                if module is cmath:
-                    register = register_cmath
-                else:
-                    register = register_math
+id_name = lambda x: x
 
-                register(1, getattr(module, libc_math_func))
+# ______________________________________________________________________
 
-register_typefuncs()
+def reg(mod, register, getname):
+    nargs = lambda f: n_ary_mathsyms.get(f, 1)
+    for symname in mathsyms + list(n_ary_mathsyms):
+        if hasattr(mod, getname(symname)):
+            register(nargs(symname), getattr(mod, getname(symname)))
+
+reg(math, partial(register_math, infer_math_call), id_name)
+reg(cmath, partial(register_math, infer_cmath_call), id_name)
+reg(np, partial(register_math, infer_math_call), npy_name)
```

### Comparing `numba-0.8.1/numba/type_inference/modules/builtinmodule.py` & `numba-0.9.0/numba/type_inference/modules/builtinmodule.py`

 * *Files 14% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from numba import *
 from numba import nodes
 from numba import error
 # from numba import function_util
 # from numba.specialize.mathcalls import is_math_function
 from numba.symtab import Variable
 from numba import typesystem
-from numba.typesystem import is_obj, promote_closest, get_type
+from numba.typesystem import get_type
 
 from numba.type_inference.modules import utils
 
 #----------------------------------------------------------------------------
 # Utilities
 #----------------------------------------------------------------------------
 
@@ -31,84 +31,84 @@
 # Type Functions for Builtins
 #----------------------------------------------------------------------------
 
 # TODO: add specializer functions to insert coercions before late specialization
 # TODO: don't rewrite AST here
 
 @register_builtin((1, 2, 3), can_handle_deferred_types=True)
-def range_(context, node, start, stop, step):
-    node.variable = Variable(typesystem.RangeType())
+def range_(typesystem, node, start, stop, step):
+    node.variable = Variable(typesystem.range_)
     node.args = nodes.CoercionNode.coerce(node.args, dst_type=Py_ssize_t)
     return node
 
 if not PY3:
     @register_builtin((1, 2, 3), can_handle_deferred_types=True)
-    def xrange_(context, node, start, stop, step):
-        return range_(context, node, start, stop, step)
+    def xrange_(typesystem, node, start, stop, step):
+        return range_(typesystem, node, start, stop, step)
 
 @register_builtin(1)
-def len_(context, node, obj):
+def len_(typesystem, node, obj):
     # Simplify len(array) to ndarray.shape[0]
     argtype = get_type(obj)
     if argtype.is_array:
         shape_attr = nodes.ArrayAttributeNode('shape', node.args[0])
         new_node = nodes.index(shape_attr, 0)
         return new_node
 
     return Py_ssize_t
 
 @register_builtin((0, 1, 2), can_handle_deferred_types=True)
-def _int(context, node, x, base, dst_type=int_):
+def _int(typesystem, node, x, base, dst_type=int_):
     # Resolve int(x) and float(x) to an equivalent cast
 
     if len(node.args) < 2:
         return cast(node, dst_type)
 
     node.variable = Variable(dst_type)
     return node
 
 if not PY3:
     @register_builtin((0, 1, 2), can_handle_deferred_types=True)
-    def _long(context, node, x, base):
-        return _int(context, node, x, base)
+    def _long(typesystem, node, x, base):
+        return _int(typesystem, node, x, base)
 
 @register_builtin((0, 1), can_handle_deferred_types=True)
-def _float(context, node, x):
+def _float(typesystem, node, x):
     return cast(node, double)
 
 @register_builtin((0, 1, 2), can_handle_deferred_types=True)
-def complex_(context, node, a, b):
+def complex_(typesystem, node, a, b):
     if len(node.args) == 2:
         args = nodes.CoercionNode.coerce(node.args, double)
         return nodes.ComplexNode(real=args[0], imag=args[1])
     else:
         return cast(node, complex128)
 
 def abstype(argtype):
     if argtype.is_complex:
-        result_type = double
+        result_type = argtype.base_type
     elif argtype.is_float or argtype.is_int:
         result_type = argtype
     else:
         result_type = object_
 
     return result_type
 
 @register_builtin(1)
-def abs_(context, node, x):
+def abs_(typesystem, node, x):
     node.variable = Variable(abstype(get_type(x)))
     return node
 
 @register_builtin((2, 3))
-def pow_(context, node, base, exponent, mod):
+def pow_(typesystem, node, base, exponent, mod):
     from . import mathmodule
-    return mathmodule.pow_(context, node, base, exponent)
+    return mathmodule.pow_(typesystem, node, base, exponent)
 
 @register_builtin((1, 2))
-def round_(context, node, number, ndigits):
+def round_(typesystem, node, number, ndigits):
     # is_math = is_math_function(node.args, round)
     argtype = get_type(number)
 
     if len(node.args) == 1 and argtype.is_int:
         # round(myint) -> float(myint)
         return nodes.CoercionNode(node.args[0], double)
 
@@ -118,14 +118,14 @@
         dst_type = object_
         node.args[0] = nodes.CoercionNode(node.args[0], object_)
 
     node.variable = Variable(dst_type)
     return node # nodes.CoercionNode(node, double)
 
 @register_builtin(0)
-def globals_(context, node):
-    return typesystem.dict_
+def globals_(typesystem, node):
+    return typesystem.dict_of_obj
     # return nodes.ObjectInjectNode(func.__globals__)
 
 @register_builtin(0)
-def locals_(context, node):
+def locals_(typesystem, node):
     raise error.NumbaError("locals() is not supported in numba functions")
```

### Comparing `numba-0.8.1/numba/support/numpy_support/slicing.py` & `numba-0.9.0/numba/support/numpy_support/slicing.py`

 * *Files 4% similar despite different names*

```diff
@@ -39,15 +39,15 @@
     seen_ellipsis = False
 
     # Filter out newaxes
     newaxes = [newaxis for newaxis in slices if nodes.is_newaxis(newaxis)]
     n_indices = len(slices) - len(newaxes)
 
     full_slice = ast.Slice(lower=None, upper=None, step=None)
-    full_slice.variable = Variable(typesystem.SliceType())
+    full_slice.variable = Variable(typesystem.slice_)
     ast.copy_location(full_slice, slices[0])
 
     # process ellipses and count integer indices
     indices_seen = 0
     for slice_node in slices[::-1]:
         slice_type = slice_node.variable.type
         if slice_type.is_ellipsis:
```

### Comparing `numba-0.8.1/numba/support/numpy_support/slicenodes.py` & `numba-0.9.0/numba/support/numpy_support/slicenodes.py`

 * *Files 6% similar despite different names*

```diff
@@ -2,17 +2,17 @@
 """
 AST nodes for native slicing.
 """
 from __future__ import print_function, division, absolute_import
 
 import ast
 
+import numba
 from numba import *
 from numba import nodes
-from numba.minivect import minitypes
 
 class SliceDimNode(nodes.ExprNode):
     """
     Array is sliced, and this dimension contains an integer index or newaxis.
     """
 
     _fields = ['subslice']
@@ -53,15 +53,15 @@
 
     _fields = ['operands', 'check_errors']
 
     def __init__(self, array_type, operands, **kwargs):
         super(BroadcastNode, self).__init__(**kwargs)
         self.operands = operands
 
-        self.shape_type = minitypes.CArrayType(npy_intp, array_type.ndim)
+        self.shape_type = numba.carray(npy_intp, array_type.ndim)
         self.array_type = array_type
         self.type = npy_intp.pointer()
 
         self.broadcast_retvals = {}
         self.check_errors = []
 
         for op in operands:
@@ -100,15 +100,15 @@
         super(NativeSliceNode, self).__init__(**kwargs)
         value = nodes.CloneableNode(value)
 
         self.type = type
         self.value = value
         self.subslices = subslices
 
-        self.shape_type = minitypes.CArrayType(npy_intp, type.ndim)
+        self.shape_type = numba.carray(npy_intp, type.ndim)
         self.nopython = nopython
         if not nopython:
             self.build_array_node = self.build_array()
         else:
             self.build_array_node = None
 
     def mark_nopython(self):
```

### Comparing `numba-0.8.1/numba/support/numpy_support/sliceutils.py` & `numba-0.9.0/numba/support/numpy_support/sliceutils.py`

 * *Files 3% similar despite different names*

```diff
@@ -139,14 +139,15 @@
             with ifelse.then():
                 new_extent.assign(zero)
 
         result = self.var(data.type, name='result')
         result.assign(data[start * stride:])
         out_shape[dst_dim] = new_extent
         # self.debug("new_extent", new_extent)
+        # self.debug("out stride:", dst_dim, stride * step)
         out_strides[dst_dim] = stride * step
 
         self.ret(result)
 
     def specialize(self, context, have_start, have_stop, have_step):
         self.context = context
 
@@ -230,31 +231,27 @@
         ('ndim', C.int),
     ]
     _retty_ = C.int
 
     def body(self, dst_shape, src_shape, src_strides, max_ndim, ndim):
         dim_offset = max_ndim - ndim
 
-        # self.debug("max_ndim", max_ndim, "ndim:", ndim)
-
         def constants(type):
             return self.constant(type, 0), self.constant(type, 1)
 
         zero, one = constants(C.npy_intp)
         zero_int, one_int = constants(C.int)
 
         with self.for_range(ndim) as (loop, i):
             src_extent = src_shape[i]
             dst_extent = dst_shape[i + dim_offset]
 
             with self.ifelse(src_extent == one) as ifelse:
                 with ifelse.then():
-                    # p_broadcast[0] = True
                     src_strides[i] = zero
-                    # self.debug("set stride = 0")
                 with ifelse.otherwise():
                     with self.ifelse(dst_extent == one) as ifelse:
                         with ifelse.then():
                             dst_shape[i + dim_offset] = src_extent
 
                         with ifelse.otherwise():
                             with self.ifelse(src_extent != dst_extent) as ifelse:
```

### Comparing `numba-0.8.1/numba/support/tests/test_ctypes.py` & `numba-0.9.0/numba/support/tests/test_ctypes.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,29 +1,26 @@
 """
 Test support for ctypes. See also numba.tests.foreign_call.test_ctypes_call.
 """
 
 import ctypes
 
+import numba as nb
 from numba import *
-from numba import environment
-from numba.support import ctypes_support
 
 try:
     from numba.tests.support import ctypes_values
 except ImportError:
     ctypes_values = None
 
 #-------------------------------------------------------------------
 # Utilities
 #-------------------------------------------------------------------
 
-env = environment.NumbaEnvironment.get_environment()
-context = env.context
-from_python = context.typemapper.from_python
+from_python = nb.typeof
 
 def get_cast_type(type):
     assert type.is_cast
     return type.dst_type
 
 def assert_signature(ctypes_func, expected=None):
     sig = from_python(ctypes_func)
```

### Comparing `numba-0.8.1/numba/support/tests/test_ctypes_gibbs.py` & `numba-0.9.0/numba/support/tests/test_ctypes_gibbs.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/support/tests/ctypes_values.py` & `numba-0.9.0/numba/support/tests/ctypes_values.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/support/tests/random/test_random_gibbs.py` & `numba-0.9.0/numba/support/tests/test_random/test_random_gibbs.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/support/cffi_support.py` & `numba-0.9.0/numba/support/cffi_support.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 # -*- coding: utf-8 -*-
 """
 Support for CFFI. Allows checking whether objects are CFFI functions and
 obtaining the pointer and numba signature.
 """
 from __future__ import print_function, division, absolute_import
 
-from numba import *
-from numba.minivect.minitypes import *
-from numba.minivect import minitypes, minierror
+import numba
+from numba.typesystem import *
 
 try:
     import cffi
     ffi = cffi.FFI()
 except ImportError:
     ffi = None
 
@@ -40,21 +39,21 @@
             result = None
         else:
             result = struct([(name, map_type(field_type))
                                for name, field_type in cffi_type.fields])
     elif cffi_type.kind == 'function':
         restype = map_type(cffi_type.result)
         argtypes = [map_type(arg) for arg in cffi_type.args]
-        result = minitypes.FunctionType(restype, argtypes,
-                                        is_vararg=cffi_type.ellipsis).pointer()
+        result = numba.function(restype, argtypes,
+                                is_vararg=cffi_type.ellipsis).pointer()
     else:
         result = type_map.get(cffi_type)
 
     if result is None:
-        raise minierror.UnmappableTypeError(cffi_type)
+        raise TypeError(cffi_type)
 
     return result
 
 def get_signature(cffi_func):
     "Get the numba signature for a CFFI function"
     return map_type(ffi.typeof(cffi_func)).base_type
```

### Comparing `numba-0.8.1/numba/array_expressions.py` & `numba-0.9.0/numba/array_expressions.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,35 +1,70 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import ast
 
-from numba import templating
+from numba.templating import temp_name
 from numba import error, pipeline, nodes, ufunc_builder
-from numba.minivect import specializers, miniast, miniutils
+from numba.minivect import specializers, miniast, miniutils, minitypes
 from numba import utils, functions
 from numba import typesystem
 from numba import visitors
 
 from numba.support.numpy_support import slicenodes
 from numba.vectorize import basic
 
+import llvm.core
+
 print_ufunc = False
 
+# ______________________________________________________________________
 
-def is_elementwise_assignment(context, assmnt_node):
+def is_elementwise_assignment(assmnt_node):
     target_type = assmnt_node.targets[0].type
     value_type = assmnt_node.value.type
 
     if target_type.is_array:
         # Allow arrays and scalars
-        context.promote_types(target_type, value_type)
-        return not value_type.is_object
+        return value_type.is_array or not value_type.is_object
 
     return False
 
+# ______________________________________________________________________
+
+def get_py_ufunc_ast(env, lhs, node):
+    if lhs is not None:
+        lhs.ctx = ast.Load()
+
+    builder = ufunc_builder.UFuncConverter(env)
+    tree = builder.visit(node)
+    ufunc_ast = builder.build_ufunc_ast(tree)
+
+    if print_ufunc:
+        from meta import asttools
+        module = ast.Module(body=[ufunc_ast])
+        print((asttools.python_source(module)))
+
+    # Vectorize Python function
+    if lhs is None:
+        restype = node.type
+    else:
+        restype = lhs.type.dtype
+
+    argtypes = [op.type.dtype if op.type.is_array else op.type
+                    for op in builder.operands]
+    signature = restype(*argtypes)
+
+    return ufunc_ast, signature, builder
+
+def get_py_ufunc(env, lhs, node):
+    ufunc_ast, signature, ufunc_builder = get_py_ufunc_ast(env, lhs, node)
+    py_ufunc = ufunc_builder.compile_to_pyfunc(ufunc_ast)
+    return py_ufunc, signature, ufunc_builder
+
+# ______________________________________________________________________
 
 class ArrayExpressionRewrite(visitors.NumbaTransformer):
     """
     Find element-wise expressions and run ElementalMapper to turn it into
     a minivect AST or a ufunc.
     """
 
@@ -50,60 +85,28 @@
 
         self.nesting_level += 1
         self.generic_visit(node)
         self.nesting_level -= 1
         self.elementwise = elementwise
         return node
 
-    def get_py_ufunc_ast(self, lhs, node):
-        if lhs is not None:
-            lhs.ctx = ast.Load()
-
-        builder = ufunc_builder.UFuncConverter()
-        tree = builder.visit(node)
-        ufunc_ast = builder.build_ufunc_ast(tree)
-
-        if print_ufunc:
-            from meta import asttools
-
-            module = ast.Module(body=[ufunc_ast])
-            print((asttools.python_source(module)))
-
-        # Vectorize Python function
-        if lhs is None:
-            restype = node.type
-        else:
-            restype = lhs.type.dtype
-
-        argtypes = [op.type.dtype if op.type.is_array else op.type
-                        for op in builder.operands]
-        signature = restype(*argtypes)
-
-        return ufunc_ast, signature, builder
-
-    def get_py_ufunc(self, lhs, node):
-        ufunc_ast, signature, ufunc_builder = self.get_py_ufunc_ast(lhs, node)
-        py_ufunc = ufunc_builder.compile_to_pyfunc(ufunc_ast)
-        return py_ufunc, signature, ufunc_builder
-
     def visit_Assign(self, node):
         self.is_slice_assign = False
         self.visitlist(node.targets)
 
         target_node = node.targets[0]
         is_slice_assign = self.is_slice_assign
 
         self.nesting_level = self.is_slice_assign
         node.value = self.visit(node.value)
         self.nesting_level = 0
 
         elementwise = self.elementwise
-
         if (len(node.targets) == 1 and is_slice_assign and
-                is_elementwise_assignment(self.context, node)):
+                is_elementwise_assignment(node)): # and elementwise):
             target_node = slicenodes.rewrite_slice(target_node,
                                                       self.nopython)
             return self.register_array_expression(node.value, lhs=target_node)
 
         return node
 
     def visit_Subscript(self, node):
@@ -116,24 +119,29 @@
             if nodes.is_ellipsis(node.slice):
                 return node.value
         elif node.value.type.is_array and node.type.is_array:
             node = slicenodes.rewrite_slice(node, self.nopython)
 
         return node
 
-    def visit_MathNode(self, node):
-        elementwise = node.arg.type.is_array
-        return self.visit_elementwise(elementwise, node)
+    def visit_Call(self, node):
+        if self.query(node, 'is_math'):
+            elementwise = node.type.is_array
+            return self.visit_elementwise(elementwise, node)
+
+        self.visitchildren(node)
+        return node
 
     def visit_BinOp(self, node):
         elementwise = node.type.is_array
         return self.visit_elementwise(elementwise, node)
 
     visit_UnaryOp = visit_BinOp
 
+# ______________________________________________________________________
 
 class ArrayExpressionRewriteUfunc(ArrayExpressionRewrite):
     """
     Compile array expressions to ufuncs. Then call the ufunc with the array
     arguments.
 
         vectorizer_cls: the ufunc vectorizer to use
@@ -163,22 +171,38 @@
             keywords = [ast.keyword('out', lhs)]
 
         func = nodes.ObjectInjectNode(ufunc)
         call_ufunc = nodes.ObjectCallNode(signature=None, func=func, args=args,
                                           keywords=keywords, py_func=ufunc)
         return nodes.ObjectTempNode(call_ufunc)
 
+# ______________________________________________________________________
 
-class NumbaproStaticArgsContext(utils.NumbaContext):
+class NumbaStaticArgsContext(utils.NumbaContext):
     "Use a static argument list: shape, data1, strides1, data2, strides2, ..."
 
     astbuilder_cls = miniast.ASTBuilder
+    optimize_llvm = False
+    optimize_broadcasting = False
     # debug = True
     # debug_elements = True
 
+    def init(self):
+        self.astbuilder = self.astbuilder_cls(self)
+        self.typemapper = minitypes.TypeMapper(self)
+
+    # def promote_types(self, t1, t2):
+    #     return typesystem.promote(t1, t2)
+    #
+    def to_llvm(self, type):
+        if type.is_object:
+            return typesystem.object_.to_llvm(self)
+        return NotImplementedError("to_llvm", type)
+
+# ______________________________________________________________________
 
 class ArrayExpressionRewriteNative(ArrayExpressionRewrite):
     """
     Compile array expressions to a minivect kernel that calls a Numba
     scalar kernel with scalar inputs:
 
         a[:, :] = b[:, :] * c[:, :]
@@ -202,52 +226,59 @@
             for (...)
                 for(...)
                     a[i, j] = numba_kernel(b[i, j], c[i, j])
 
     CAN be used in a nopython context
     """
 
+    expr_count = 0
+
     def array_attr(self, node, attr):
         # Perform a low-level bitcast from object to an array type
         # array = nodes.CoercionNode(node, float_[:])
         array = node
         return nodes.ArrayAttributeNode(attr, array)
 
     def register_array_expression(self, node, lhs=None):
         super(ArrayExpressionRewriteNative, self).register_array_expression(
             node, lhs)
 
+        # llvm_module = llvm.core.Module.new(temp_name("array_expression_module"))
+        # llvm_module = self.env.llvm_context.module
+
         lhs_type = lhs.type if lhs else node.type
         is_expr = lhs is None
 
         if node.type.is_array and lhs_type.ndim < node.type.ndim:
             # TODO: this is valid in NumPy if the leading dimensions of the
             # TODO: RHS have extent 1
             raise error.NumbaError(
                 node, "Right hand side must have a "
                       "dimensionality <= %d" % lhs_type.ndim)
 
         # Create ufunc scalar kernel
-        ufunc_ast, signature, ufunc_builder = self.get_py_ufunc_ast(lhs, node)
-        signature.struct_by_reference = True
+        ufunc_ast, signature, ufunc_builder = get_py_ufunc_ast(self.env, lhs, node)
 
         # Compile ufunc scalar kernel with numba
         ast.fix_missing_locations(ufunc_ast)
+        # func_env = self.env.crnt.inherit(
+        #     func=None, ast=ufunc_ast, func_signature=signature,
+        #     wrap=False, #link=False, #llvm_module=llvm_module,
+        # )
+        # pipeline.run_env(self.env, func_env) #, pipeline_name='codegen')
+
         func_env, (_, _, _) = pipeline.run_pipeline2(
             self.env, None, ufunc_ast, signature,
-            function_globals={},
+            function_globals=self.env.crnt.function_globals,
+            wrap=False, link=False, nopython=True,
+            #llvm_module=llvm_module, # pipeline_name='codegen',
         )
+        llvm_module = func_env.llvm_module
 
-        # Manual linking
-        lfunc = func_env.lfunc
-
-        # print lfunc
         operands = ufunc_builder.operands
-        functions.keep_alive(self.func, lfunc)
-
         operands = [nodes.CloneableNode(operand) for operand in operands]
 
         if lhs is not None:
             lhs = nodes.CloneableNode(lhs)
             broadcast_operands = [lhs] + operands
             lhs = lhs.clone
         else:
@@ -262,29 +293,40 @@
         elif lhs is None:
             # TODO: determine best output order at runtime
             shape = shape.cloneable
             lhs = nodes.ArrayNewEmptyNode(lhs_type, shape.clone,
                                           lhs_type.is_f_contig).cloneable
 
         # Build minivect wrapper kernel
-        context = NumbaproStaticArgsContext()
-        context.llvm_module = self.env.llvm_context.module
-        # context.debug = True
-        context.optimize_broadcasting = False
-        b = context.astbuilder
+        context = NumbaStaticArgsContext()
+        context.llvm_module = llvm_module
+        # context.llvm_ee = self.env.llvm_context.execution_engine
 
+        b = context.astbuilder
         variables = [b.variable(name_node.type, "op%d" % i)
                      for i, name_node in enumerate([lhs] + operands)]
         miniargs = [b.funcarg(variable) for variable in variables]
-        body = miniutils.build_kernel_call(lfunc.name, signature, miniargs, b)
+        body = miniutils.build_kernel_call(func_env.lfunc.name, signature,
+                                           miniargs, b)
 
         minikernel = b.function_from_numpy(
-            templating.temp_name("array_expression"), body, miniargs)
-        lminikernel, ctypes_kernel = context.run_simple(
-            minikernel, specializers.StridedSpecializer)
+            temp_name("array_expression"), body, miniargs)
+        lminikernel, = context.run_simple(minikernel,
+                                          specializers.StridedSpecializer)
+        # lminikernel.linkage = llvm.core.LINKAGE_LINKONCE_ODR
+
+        # pipeline.run_env(self.env, func_env, pipeline_name='post_codegen')
+        # llvm_module.verify()
+        del func_env
+
+        assert lminikernel.module is llvm_module
+        # print("---------")
+        # print(llvm_module)
+        # print("~~~~~~~~~~~~")
+        lminikernel = self.env.llvm_context.link(lminikernel)
 
         # Build call to minivect kernel
         operands.insert(0, lhs)
         args = [shape]
         scalar_args = []
         for operand in operands:
             if operand.type.is_array:
```

### Comparing `numba-0.8.1/numba/closures.py` & `numba-0.9.0/numba/closures.py`

 * *Files 1% similar despite different names*

```diff
@@ -61,18 +61,17 @@
 from numba import nodes
 from numba import typesystem
 from numba import typedefs
 from numba import numbawrapper
 from numba.exttypes import extension_types
 from numba import utils
 from numba.type_inference import module_type_inference
-from numba.minivect import  minitypes
 from numba.symtab import Variable
-from numba.exttypes import methodtable
 from numba.exttypes import attributetable
+
 logger = logging.getLogger(__name__)
 #logger.setLevel(logging.DEBUG)
 
 #------------------------------------------------------------------------
 # Utilities
 #------------------------------------------------------------------------
 
@@ -90,15 +89,15 @@
 
 def err_decorator(decorator):
     raise error.NumbaError(
             decorator, "Only @jit and @autojit and signature decorators "
                        "are supported")
 
 def check_valid_argtype(argtype_node, argtype):
-    if not isinstance(argtype, minitypes.Type):
+    if not isinstance(argtype, typesystem.Type):
         raise error.NumbaError(argtype_node, "Invalid type: %r" % (argtype,))
 
 def assert_constant(visit_func, decorator, result_node):
     result = visit_func(result_node)
     if not result.variable.is_constant:
         raise error.NumbaError(decorator, "Expected a constant")
 
@@ -147,22 +146,20 @@
 
     if decorator.args or decorator.keywords:
         restype = parse_restype(visit_func, decorator, jit_args)
         if restype is not None and restype.is_function:
             signature = restype
         else:
             argtypes = parse_argtypes(visit_func, decorator, func_def, jit_args)
-            signature = minitypes.FunctionType(restype, argtypes,
-                                               name=func_def.name)
+            signature = typesystem.function(restype, argtypes,
+                                            name=func_def.name)
     else: #elif func_def.args:
         raise error.NumbaError(decorator,
                                "The argument types and return type "
                                "need to be specified")
-    #else:
-    #    signature = minitypes.FunctionType(None, [])
 
     # TODO: Analyse closure at call or outer function return time to
     # TODO:     infer return type
     # TODO: parse out nopython argument
     return signature
 
 def check_signature_decorator(visit_func, decorator):
```

### Comparing `numba-0.8.1/numba/intrinsic/string_intrinsic.py` & `numba-0.9.0/numba/intrinsic/string_intrinsic.py`

 * *Files 7% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from .intrinsic import Intrinsic
 from llpython.byte_translator import LLVMTranslator
 
 __all__ = ['CStringSlice2',
            'CStringSlice2Len']
 
 class CStringSlice2 (Intrinsic):
-    arg_types = [c_string_type, c_string_type, size_t, Py_ssize_t, Py_ssize_t]
+    arg_types = [string_, string_, size_t, Py_ssize_t, Py_ssize_t]
     return_type = void
 
     def implementation(self, module, lfunc):
         # logger.debug((module, str(lfunc)))
         def _py_c_string_slice(out_string, in_string, in_str_len, lower,
                                upper):
             zero = lc_size_t(0)
@@ -29,15 +29,15 @@
             out_string[temp_len] = li8(0)
             return
         LLVMTranslator(module).translate(_py_c_string_slice,
                                          llvm_function = lfunc)
         return lfunc
 
 class CStringSlice2Len(Intrinsic):
-    arg_types = [c_string_type, size_t, Py_ssize_t, Py_ssize_t]
+    arg_types = [string_, size_t, Py_ssize_t, Py_ssize_t]
     return_type = size_t
 
     def implementation(self, module, lfunc):
         def _py_c_string_slice_len(in_string, in_str_len, lower, upper):
             zero = lc_size_t(0)
             if lower < zero:
                 lower += in_str_len
```

### Comparing `numba-0.8.1/numba/intrinsic/numba_intrinsic.py` & `numba-0.9.0/numba/intrinsic/numba_intrinsic.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/intrinsic/intrinsic.py` & `numba-0.9.0/numba/intrinsic/intrinsic.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import llvm.core
-from numba.minivect import minitypes
+from numba.typesystem import function
 
 from collections import namedtuple
 
 Signature = namedtuple('Signature', ['return_type', 'arg_types'])
 
 class Intrinsic(object):
     _attributes = ('func_name', 'arg_types', 'return_type')
@@ -28,17 +28,15 @@
             for k, v in kwargs.items():
                 if k not in self._attributes:
                     raise TypeError("Invalid keyword arg %s -> %s" % (k, v))
         vars(self).update(kwargs)
 
     @property
     def signature(self):
-        return minitypes.FunctionType(return_type=self.return_type,
-                                      args=self.arg_types,
-                                      is_vararg=self.is_vararg)
+        return function(self.return_type, self.arg_types, self.is_vararg)
 
     @property
     def name(self):
         if self.func_name is None:
             return type(self).__name__
         else:
             return self.func_name
```

### Comparing `numba-0.8.1/numba/intrinsic/__init__.py` & `numba-0.9.0/numba/intrinsic/__init__.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/transforms.py` & `numba-0.9.0/numba/transforms.py`

 * *Files 4% similar despite different names*

```diff
@@ -77,52 +77,77 @@
 """
 from __future__ import print_function, division, absolute_import
 
 
 import sys
 import ast
 import ctypes
-from numba.specialize.mathcalls import (is_intrinsic, is_math_function,
-                                        resolve_intrinsic, resolve_libc_math,
-                                        resolve_math_call)
 
 if __debug__:
     import pprint
 
 import numba
 from numba import *
-from numba import error, closures
-from .minivect import minierror, minitypes, codegen
+from numba import error
+from .minivect import codegen
 from numba import macros, utils, typesystem
-from numba.symtab import Variable
-from numba import visitors, nodes, error, functions
-from numba import stdio_util, function_util
-from numba.typesystem import is_obj, promote_closest, promote_to_native
+from numba import visitors, nodes
+from numba import function_util
+from numba.typesystem import is_obj, promote_to_native
+from numba.type_inference.modules import mathmodule
 from numba.nodes import constnodes
 from numba.external import utility
 from numba.utils import dump
 
 import llvm.core
 import numpy as np
 
 logger = logging.getLogger(__name__)
 
 from numba.external import pyapi
 
-is_win32 = sys.platform == 'win32'
+# ______________________________________________________________________
 
-class BuiltinResolverMixinBase(object):
-    """
-    Base class for mixins resolving calls to built-in functions.
+def get_funcname(py_func):
+    if py_func in (abs, np.abs):
+        return 'fabs'
+    elif py_func is np.round:
+        return 'round'
+
+    return mathmodule.ufunc2math.get(py_func.__name__, py_func.__name__)
+
+def resolve_pow(env, restype, args):
+    promote = env.crnt.typesystem.promote
+    have_mod = len(args) == 3
+    if restype.is_numeric and not have_mod:
+        type = reduce(promote, [double, restype] + [a.type for a in args])
+        signature = type(*[type] * len(args))
+        result = nodes.MathCallNode(signature, args, None, name='pow')
+    else:
+        result = nodes.call_pyfunc(pow, args)
+    return nodes.CoercionNode(result, restype)
+
+def math_call(name, args, dst_type):
+    signature = dst_type(*[a.type for a in args])
+    return nodes.MathCallNode(signature, args, None, name=name)
+
+def math_call2(name, call_node):
+    return math_call(name, [call_node.args[0]], call_node.type)
+
+# ______________________________________________________________________
 
-    Methods called _resolve_<built-in name> are called to handle calls
-    to the built-in of that name.
+class BuiltinResolver(object):
+    """
+    Perform final low-level transformations such as abs(value) -> fabs(value)
     """
 
-    def _resolve_builtin_call(self, node, func):
+    def __init__(self, env):
+        self.env = env
+
+    def resolve_builtin_call(self, node, func):
         """
         Resolve an ast.Call() of a built-in function.
 
         Returns None if no specific transformation is applied.
         """
         resolver = getattr(self, '_resolve_' + func.__name__, None)
         if resolver is not None:
@@ -131,113 +156,85 @@
             if len(node.args) >= 1:
                 argtype = node.args[0].variable.type
 
             return resolver(func, node, argtype)
 
         return None
 
-    def _resolve_builtin_call_or_object(self, node, func):
+    def resolve_builtin_call_or_object(self, node, func):
         """
         Resolve an ast.Call() of a built-in function, or call the built-in
         through the object layer otherwise.
         """
-        result = self._resolve_builtin_call(node, func)
+        result = self.resolve_builtin_call(node, func)
         if result is None:
             result = nodes.call_pyfunc(func, node.args)
 
         return nodes.CoercionNode(result, node.type)
 
-def resolve_pow(type, args):
-    have_mod = len(args) == 3
-
-    if (type.is_int or type.is_float) and not have_mod and not is_win32:
-        result = resolve_intrinsic(args, pow, type)
-    else:
-        result = nodes.call_pyfunc(pow, args)
-
-    return nodes.CoercionNode(result, type)
-
-class LateBuiltinResolverMixin(BuiltinResolverMixinBase):
-    """
-    Perform final low-level transformations such as abs(value) -> fabs(value)
-    """
 
     def _resolve_abs(self, func, node, argtype):
-        is_math = is_math_function(node.args, abs)
-
-        # TODO: generate efficient inline code
-        if is_math and argtype.is_float:
-            return resolve_math_call(node, abs)
-        elif is_math and argtype.is_int:
-            if argtype.signed:
-                type = promote_closest(self.context, argtype, [long_, longlong])
-                funcs = {long_: 'labs', longlong: 'llabs'}
-                return function_util.external_call(
-                                            self.context,
-                                            self.llvm_module,
-                                            funcs[type],
-                                            args=[node.args[0]])
-            else:
-                # abs() on unsigned integral value
-                return node.args[0]
-
-        return None
+        if argtype.is_int and not argtype.signed:
+            # abs() on unsigned integral value
+            return node.args[0]
+        elif not node.type.is_numeric:
+            result = nodes.call_pyfunc(func, node.args)
+        else:
+            return math_call2('abs', node)
 
     def _resolve_round(self, func, node, argtype):
-        if is_math_function(node.args, round):
-            # round() always returns a float
-            return resolve_math_call(node, round)
-
-        return None
+        return nodes.call_pyfunc(round, node.args)
 
     def _resolve_pow(self, func, node, argtype):
-        return resolve_pow(node.type, node.args)
+        return resolve_pow(self.env, node.type, node.args)
 
     def _resolve_int_number(self, func, node, argtype, dst_type, ext_name):
         assert len(node.args) == 2
 
         arg1, arg2 = node.args
-        if arg1.variable.type.is_c_string:
+        if arg1.variable.type.is_string:
             return nodes.CoercionNode(
                 nodes.ObjectTempNode(
                     function_util.external_call(
-                        self.context,
-                        self.llvm_module,
+                        self.env.context,
+                        self.env.crnt.llvm_module,
                         ext_name,
                         args=[arg1, nodes.NULL, arg2])),
                 dst_type=dst_type)
 
     def _resolve_int(self, func, node, argtype, dst_type=int_):
         if PY3:
             return self._resolve_int_number(func, node, argtype, long_, 'PyLong_FromString')
         return self._resolve_int_number(func, node, argtype, int_, 'PyInt_FromString')
 
     def _resolve_long(self, func, node, argtype, dst_type=int_):
         return self._resolve_int_number(func, node, argtype, long_, 'PyLong_FromString')
 
-
 class ResolveCoercions(visitors.NumbaTransformer):
 
     def visit_CoercionNode(self, node):
         if not isinstance(node, nodes.CoercionNode):
             # CoercionNode.__new__ returns the node to be coerced if it doesn't
             # need coercion
             return node
 
         node_type = node.node.type
         dst_type = node.dst_type
         if __debug__ and self.env and self.env.debug_coercions:
             logger.debug('coercion: %s --> %s\n%s',
                          node_type, dst_type, utils.pformat_ast(node))
 
-        if self.nopython and (is_obj(node_type) ^ is_obj(dst_type)):
+        # TODO: the below is a problem due to implicit string <-> int coercions!
+        if (node_type.is_string and dst_type.is_numeric and not
+            (node_type.is_pointer or node_type.is_null)):
+            result = self.str_to_int(dst_type, node)
+        elif self.nopython and (is_obj(node_type) ^ is_obj(dst_type)):
             raise error.NumbaError(node, "Cannot coerce to or from object in "
                                          "nopython context")
-
-        if is_obj(node.dst_type) and not is_obj(node_type):
+        elif is_obj(node.dst_type) and not is_obj(node_type):
             node = nodes.ObjectTempNode(nodes.CoerceToObject(
                     node.node, node.dst_type, name=node.name))
             result = self.visit(node)
         elif is_obj(node_type) and not is_obj(node.dst_type):
             node = nodes.CoerceToNative(node.node, node.dst_type,
                                         name=node.name)
             result = self.visit(node)
@@ -248,56 +245,58 @@
                                        "coerced to a pointer type")
             result = self.visit(nodes.NULL.coerce(dst_type))
         elif node_type.is_numeric and dst_type.is_bool:
             to_bool = ast.Compare(node.node, [ast.NotEq()],
                                   [nodes.const(0, node_type)])
             to_bool = nodes.typednode(to_bool, bool_)
             result = self.visit(to_bool)
-        elif node_type.is_c_string and dst_type.is_numeric:
-            # TODO: int <-> string conversions are explicit, this should not
-            # TODO: be a coercion
-            if self.nopython:
-                node = nodes.CoercionNode(
-                    function_util.external_call(
-                                self.context,
-                                self.llvm_module,
-                                ('atol' if dst_type.is_int else 'atof'),
-                                args=[node.node]),
-                    dst_type, name=node.name,)
-            else:
-                if dst_type.is_int:
-                    cvtobj = function_util.external_call(
-                                              self.context,
-                                              self.llvm_module,
-                                              'PyInt_FromString' if not PY3 else 'PyLong_FromString',
-                                              args=[node.node, nodes.NULL,
-                                                    nodes.const(10, int_)])
-                else:
-                    cvtobj = function_util.external_call(
-                                          self.context,
-                                          self.llvm_module,
-                                          'PyFloat_FromString',
-                                          args=[node.node,
-                                                nodes.const(0, Py_ssize_t)])
-                node = nodes.CoerceToNative(nodes.ObjectTempNode(cvtobj),
-                                            dst_type, name=node.name)
-            result = self.visit(node)
         else:
             self.generic_visit(node)
 
             if dst_type == node.node.type:
                 result = node.node
             else:
                 result = node
 
         if __debug__ and self.env and self.env.debug_coercions:
             logger.debug('result = %s', utils.pformat_ast(result))
 
         return result
 
+    def str_to_int(self, dst_type, node):
+        # TODO: int <-> string conversions are explicit, this should not
+        # TODO: be a coercion
+        if self.nopython:
+            node = nodes.CoercionNode(
+                function_util.external_call(
+                    self.context,
+                    self.llvm_module,
+                    ('atol' if dst_type.is_int else 'atof'),
+                    args=[node.node]),
+                dst_type, name=node.name, )
+        else:
+            if dst_type.is_int:
+                cvtobj = function_util.external_call(
+                    self.context,
+                    self.llvm_module,
+                    'PyInt_FromString' if not PY3 else 'PyLong_FromString',
+                    args=[node.node, nodes.NULL,
+                          nodes.const(10, int_)])
+            else:
+                cvtobj = function_util.external_call(
+                    self.context,
+                    self.llvm_module,
+                    'PyFloat_FromString',
+                    args=[node.node,
+                          nodes.const(0, Py_ssize_t)])
+            node = nodes.CoerceToNative(nodes.ObjectTempNode(cvtobj),
+                                        dst_type, name=node.name)
+        result = self.visit(node)
+        return result
+
     def _get_int_conversion_func(self, type, funcs_dict):
         type = promote_to_native(type)
         if type.itemsize <= long_.itemsize:
             types = [ulong, long_]
         else:
             assert type.itemsize > long_.itemsize
             types = [ulonglong, longlong]
@@ -334,15 +333,15 @@
                     node_type)
 
             if cls:
                 new_node = function_util.external_call(self.context,
                                                        self.llvm_module,
                                                        cls.__name__,
                                                        args=args)
-        elif node_type.is_pointer and not node_type.is_string():
+        elif node_type.is_pointer and not node_type == char.pointer():
             # Create ctypes pointer object
             ctypes_pointer_type = node_type.to_ctypes()
             args = [nodes.CoercionNode(node.node, int64),
                     nodes.ObjectInjectNode(ctypes_pointer_type, object_)]
             new_node = nodes.call_pyfunc(ctypes.cast, args)
 
         self.generic_visit(new_node)
@@ -355,15 +354,15 @@
         a Python int or long if necessary.
 
         PyLong_AsLong and friends do not do this (overflow/underflow checking
         is only for longs, and conversion to int|long depends on the Python
         version).
         """
         dst_type = promote_to_native(dst_type)
-        assert dst_type in utility.object_to_numeric
+        assert dst_type in utility.object_to_numeric, (dst_type, utility.object_to_numeric)
         utility_func = utility.object_to_numeric[dst_type]
         result = function_util.external_call_func(self.context,
                                                   self.llvm_module,
                                                   utility_func,
                                                   args=[node])
         return result
 
@@ -415,21 +414,21 @@
 
             if cls:
                 # TODO: error checking!
                 new_node = function_util.external_call(self.context,
                                                        self.llvm_module,
                                                        cls.__name__,
                                                        args=[node.node])
-        elif node_type.is_pointer:
+        elif node_type.is_pointer and not node_type.is_string:
             if from_type.is_jit_function and node_type.base_type.is_function:
                 new_node = self.coerce_to_function_pointer(
                     node, from_type, node_type)
             else:
                 raise error.NumbaError(node, "Obtaining pointers from objects "
-                                             "is not yet supported")
+                                             "is not yet supported (%s)" % node_type)
         elif node_type.is_void:
             raise error.NumbaError(node, "Cannot coerce %s to void" %
                                    (from_type,))
 
         if new_node is None:
             # Create a tuple for PyArg_ParseTuple
             new_node = node
@@ -444,18 +443,18 @@
             new_node = nodes.CoercionNode(new_node, node.type)
 
         # Specialize replacement node
         new_node = self.visit(new_node)
         return new_node
 
 
-class LateSpecializer(ResolveCoercions, LateBuiltinResolverMixin,
-                      visitors.NoPythonContextMixin):
+class LateSpecializer(ResolveCoercions, visitors.NoPythonContextMixin):
 
     def visit_FunctionDef(self, node):
+        self.builtin_resolver = BuiltinResolver(self.env)
         node.decorator_list = self.visitlist(node.decorator_list)
 
         # Make sure to visit the entry block (not part of the CFG) and the
         # first actual code block which may have synthetically
         # inserted promotions
         self.visit_ControlBlock(node.flow.blocks[0])
         self.visit_ControlBlock(node.flow.blocks[1])
@@ -546,15 +545,15 @@
                                             args=[value])
         args = [dest, nodes.ConstNode("write"), nodes.ConstNode("O"), value]
         return nodes.NativeCallNode(signature, args, lfunc)
 
     def visit_Print(self, node):
         if self.nopython:
             printfunc = self._print_nopython
-            dst_type = c_string_type
+            dst_type = string_
         else:
             printfunc = self._print
             dst_type = object_
 
         result = []
 
         if node.values:
@@ -567,41 +566,25 @@
                 result.pop() # pop last space
 
         if node.nl:
             result.append(printfunc(nodes.const("\n", dst_type), node.dest))
 
         return ast.Suite(body=self.visitlist(result))
 
-    def visit_Call(self, node):
-        func_type = node.func.type
-
-        if self.query(node, "is_math"):
-            assert node.func.type.is_known_value
-            result = resolve_math_call(node, node.func.type.value)
-            return self.visit(result)
-
-        elif func_type.is_builtin:
-            result = self._resolve_builtin_call_or_object(node, func_type.func)
-            result =  self.visit(result)
-            return result
-
-        self.generic_visit(node)
-        return node
-
     def visit_Tuple(self, node):
         self.check_context(node)
 
         sig, lfunc = self.context.external_library.declare(self.llvm_module,
                                                            'PyTuple_Pack')
         objs = self.visitlist(nodes.CoercionNode.coerce(node.elts, object_))
-        n = nodes.ConstNode(len(node.elts), minitypes.Py_ssize_t)
+        n = nodes.ConstNode(len(node.elts), Py_ssize_t)
         args = [n] + objs
         new_node = nodes.NativeCallNode(sig, args, lfunc, name='tuple')
         # TODO: determine element type of node.elts
-        new_node.type = typesystem.TupleType(object_, size=len(node.elts))
+        new_node.type = typesystem.tuple_(object_, size=len(node.elts))
         return nodes.ObjectTempNode(new_node)
 
     def visit_List(self, node):
         self.check_context(node)
         self.generic_visit(node)
         return nodes.ObjectTempNode(node)
 
@@ -620,31 +603,28 @@
                                          "nopython context" + meth_name)
 
         node.function = self.visit(node.function)
         node.args_tuple = self.visit(node.args_tuple)
         node.kwargs_dict = self.visit(node.kwargs_dict)
         return nodes.ObjectTempNode(node)
 
-    def visit_MathNode(self, math_node):
-        "Translate a nodes.MathNode to an intrinsic or libc math call"
-        from numba.type_inference.modules import mathmodule
-        lowerable = is_math_function([math_node.arg], math_node.py_func)
-
-        if math_node.type.is_array or not lowerable:
-            # Generate a Python call
-            assert math_node.py_func is not None
-            result = nodes.call_pyfunc(math_node.py_func, [math_node.arg])
-            result = result.coerce(math_node.type)
-        else:
-            # Lower to intrinsic or libc math call
-            args = [math_node.arg], math_node.py_func, math_node.type
-            if is_intrinsic(math_node.py_func):
-                result = resolve_intrinsic(*args)
-            else:
-                result = resolve_libc_math(*args)
+    def visit_Call(self, node):
+        func_type = node.func.type
+
+        if self.query(node, "is_math") and node.type.is_numeric:
+            assert node.func.type.is_known_value
+            name = get_funcname(node.func.type.value)
+            result = math_call(name, node.args, node.type)
+
+        elif func_type.is_builtin:
+            result = self.builtin_resolver.resolve_builtin_call_or_object(
+                node, func_type.func)
+
+        else:
+            result = nodes.call_obj(node)
 
         return self.visit(result)
 
     def _c_string_slice(self, node):
         ret_val = node
         logger.debug(node.slice)
         node_slice = node.slice
@@ -679,25 +659,25 @@
     def visit_Subscript(self, node):
         if isinstance(node.value, nodes.ArrayAttributeNode):
             if node.value.is_read_only and isinstance(node.ctx, ast.Store):
                 raise error.NumbaError("Attempt to load read-only attribute")
 
         # Short-circuit visiting a Slice child if this is a nopython
         # string slice.
-        if (self.nopython and node.value.type.is_c_string and
-                node.type.is_c_string):
+        if (self.nopython and node.value.type.is_string and
+                node.type.is_string):
             return self.visit(self._c_string_slice(node))
 
         # logging.debug(ast.dump(node))
         # TODO: do this in the respective cases below when needed
         self.generic_visit(node)
 
         node_type = node.value.type
-        if node_type.is_object or (node_type.is_array and
-                                   node.slice.type.is_object):
+        if ((node_type.is_object and not node_type.is_array) or
+            (node_type.is_array and node.slice.type.is_object)):
             # Array or object slicing
             if isinstance(node.ctx, ast.Load):
                 result = function_util.external_call(self.context,
                                                      self.llvm_module,
                                                      'PyObject_GetItem',
                                                      args=[node.value,
                                                            node.slice])
@@ -706,15 +686,15 @@
             else:
                 # This is handled in visit_Assign
                 pass
         elif (node.value.type.is_array and not node.type.is_array and
                   node.slice.type.is_int):
             # Array index with integer indices
             node = nodes.DataPointerNode(node.value, node.slice, node.ctx)
-        elif node.value.type.is_c_string and node.type.is_c_string:
+        elif node.value.type.is_string and node.type.is_string:
             node.value = nodes.CoercionNode(node.value, dst_type = object_)
             node.type = object_
             node = nodes.CoercionNode(nodes.ObjectTempNode(node),
                                       dst_type = c_string_type)
             node = self.visit(node)
 
         return node
@@ -825,17 +805,16 @@
             return self.visit(new_node)
 
         self.generic_visit(node)
         return node
 
     def visit_ArrayNewNode(self, node):
         if self.nopython:
-            # Give the codegen (subclass) a chance to handle this
-            self.generic_visit(node)
-            return node
+            raise error.NumbaError(
+                node, "Cannot yet allocate new array in nopython context")
 
         PyArray_Type = nodes.ObjectInjectNode(np.ndarray)
         descr = nodes.ObjectInjectNode(node.type.dtype.get_dtype()).cloneable
         ndim = nodes.const(node.type.ndim, int_)
         flags = nodes.const(0, int_)
         args = [PyArray_Type, descr.clone, ndim,
                 node.shape, node.strides, node.data, flags]
@@ -859,19 +838,25 @@
             body.append(nodes.PyArray_SetBaseObject([array.clone, base.clone]))
 
         # TODO: PyArray_UpdateFlags()
         result = nodes.ExpressionNode(filter(None, body), array.clone)
         return self.visit(result)
 
     def visit_ArrayNewEmptyNode(self, node):
+        if self.nopython:
+            raise error.NumbaError(
+                node, "Cannot yet allocate new empty array in nopython context")
+
         ndim = nodes.const(node.type.ndim, int_)
-        dtype = nodes.const(node.type.dtype.get_dtype(), object_)
+        dtype = nodes.const(node.type.dtype.get_dtype(), object_).cloneable
         is_fortran = nodes.const(node.is_fortran, int_)
         result = nodes.PyArray_Empty([ndim, node.shape, dtype, is_fortran])
-        return self.visit(result)
+        result = nodes.ObjectTempNode(result)
+        incref_descr = nodes.IncrefNode(dtype)
+        return self.visit(nodes.ExpressionNode([incref_descr], result))
 
     def visit_Name(self, node):
         if node.variable.is_constant:
             obj = node.variable.constant_value
             return self.visit(nodes.const(obj, node.type))
 
         return node
@@ -938,15 +923,16 @@
         return self._object_binop(node, 'PyNumber_And')
 
     def _object_FloorDiv(self, node):
         return self._object_binop(node, 'PyNumber_FloorDivide')
 
     def visit_BinOp(self, node):
         if isinstance(node.op, ast.Pow):
-            return self.visit(resolve_pow(node.type, [node.left, node.right]))
+            return self.visit(resolve_pow(self.env, node.type, [node.left,
+                                                                node.right]))
 
         self.generic_visit(node)
         if is_obj(node.left.type) or is_obj(node.right.type):
             op_name = type(node.op).__name__
             op_method = getattr(self, '_object_%s' % op_name, None)
             if op_method:
                 node = op_method(node)
@@ -993,21 +979,23 @@
                 raise error.NumbaError(
                     node, 'Unsupported unary operation for objects: %s' %
                     op_name)
         return node
 
     def visit_ConstNode(self, node):
         constant = node.pyval
+        if node.type.is_known_value:
+            node.type = object_ # TODO: Get rid of known_value
 
         if node.type.is_complex:
             real = nodes.ConstNode(constant.real, node.type.base_type)
             imag = nodes.ConstNode(constant.imag, node.type.base_type)
             node = nodes.ComplexNode(real, imag)
 
-        elif node.type.is_pointer:
+        elif node.type.is_pointer and not node.type.is_string:
             addr_int = constnodes.get_pointer_address(constant, node.type)
             node = nodes.ptrfromint(addr_int, node.type)
 
         elif node.type.is_object and not nodes.is_null_constant(constant):
             node = nodes.ObjectInjectNode(constant, node.type)
 
         return node
```

### Comparing `numba-0.8.1/numba/nodes/structnodes.py` & `numba-0.9.0/numba/nodes/structnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/closurenodes.py` & `numba-0.9.0/numba/nodes/closurenodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/coercionnodes.py` & `numba-0.9.0/numba/nodes/coercionnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/tempnodes.py` & `numba-0.9.0/numba/nodes/tempnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/constnodes.py` & `numba-0.9.0/numba/nodes/constnodes.py`

 * *Files 23% similar despite different names*

```diff
@@ -25,44 +25,23 @@
     Wrap a constant.
     """
 
     _attributes = ['type', 'pyval']
 
     def __init__(self, pyval, type=None):
         if type is None:
-            type = context.typemapper.from_python(pyval)
+            type = numba.typeof(pyval)
 
         # if pyval is not _NULL:
         #     assert not type.is_object
 
         self.variable = Variable(type, is_constant=True, constant_value=pyval)
         self.type = type
         self.pyval = pyval
 
-    def cast(self, dst_type):
-        # This should probably happen in a transform !
-        if dst_type.is_int:
-            caster = int
-        elif dst_type.is_float:
-            caster = float
-        elif dst_type.is_complex:
-            caster = complex
-        else:
-            raise NotImplementedError(dst_type)
-
-        try:
-            self.pyval = caster(self.pyval)
-        except ValueError:
-            if dst_type.is_int and self.type.is_c_string:
-                raise
-            raise minierror.UnpromotableTypeError((dst_type, self.type))
-
-        self.type = dst_type
-        self.variable.type = dst_type
-
     def __repr__(self):
         return "const(%s, %s)" % (self.pyval, self.type)
 
 #------------------------------------------------------------------------
 # NULL Constants
 #------------------------------------------------------------------------
```

### Comparing `numba-0.8.1/numba/nodes/llvmnodes.py` & `numba-0.9.0/numba/nodes/llvmnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/basenodes.py` & `numba-0.9.0/numba/nodes/basenodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/metadata.py` & `numba-0.9.0/numba/nodes/metadata.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/objectnodes.py` & `numba-0.9.0/numba/nodes/objectnodes.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
+
+from numba import typesystem
 from numba.nodes import *
 
 class ObjectInjectNode(ExprNode):
     """
     Refer to a Python object in the llvm code.
     """
 
@@ -39,15 +41,15 @@
         return "objtemp(%s)" % self.node
 
 class NoneNode(ExprNode):
     """
     Return None.
     """
 
-    type = typesystem.NoneType()
+    type = typesystem.none
     variable = Variable(type)
 
 class ObjectTempRefNode(ExprNode):
     """
     Reference an ObjectTempNode, without evaluating its subexpressions.
     The ObjectTempNode must already have been evaluated.
     """
```

### Comparing `numba-0.8.1/numba/nodes/cfnodes.py` & `numba-0.9.0/numba/nodes/cfnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/callnodes.py` & `numba-0.9.0/numba/nodes/callnodes.py`

 * *Files 3% similar despite different names*

```diff
@@ -78,28 +78,14 @@
 
     _fields = ['macro', 'args']
 
     def __init__(self, signature, macro, *args, **kw):
         super(LLMacroNode, self).__init__(signature, args, None, None, **kw)
         self.macro = macro
 
-class MathNode(ExprNode):
-    """
-    Represents a high-level call to a math function.
-    """
-
-    _fields = ['arg']
-
-    def __init__(self, py_func, signature, arg, **kwargs):
-        super(MathNode, self).__init__(**kwargs)
-        self.py_func = py_func
-        self.signature = signature
-        self.arg = arg
-        self.type = signature.return_type
-
 class LLVMExternalFunctionNode(ExprNode):
     '''For calling an external llvm function where you only have the
     signature and the function name.
     '''
     def __init__(self, signature, fname):
         super(LLVMExternalFunctionNode, self).__init__(signature=signature,
                                                        fname=fname)
@@ -129,33 +115,32 @@
 class ObjectCallNode(FunctionCallNode):
     _fields = ['function', 'args_tuple', 'kwargs_dict']
 
     def __init__(self, signature, func, args, keywords=None, py_func=None, **kw):
         if py_func and not kw.get('name', None):
             kw['name'] = py_func.__name__
         if signature is None:
-            signature = minitypes.FunctionType(return_type=object_,
-                                               args=[object_] * len(args))
+            signature = numba.function(object_, [object_] * len(args))
             if keywords:
                 signature.args.extend([object_] * len(keywords))
 
         super(ObjectCallNode, self).__init__(signature, args)
         assert func is not None
         self.function = func
         self.py_func = py_func
 
         self.args_tuple = ast.Tuple(elts=list(args), ctx=ast.Load())
         self.args_tuple.variable = Variable(
-                typesystem.TupleType(object_, size=len(args)))
+                typesystem.tuple_(object_, size=len(args)))
 
         if keywords:
             keywords = [(ConstNode(k.arg), k.value) for k in keywords]
             keys, values = zip(*keywords)
             self.kwargs_dict = ast.Dict(list(keys), list(values))
-            self.kwargs_dict.variable = Variable(minitypes.object_)
+            self.kwargs_dict.variable = Variable(object_)
         else:
             self.kwargs_dict = NULL_obj
 
         self.type = signature.return_type
 
     def __repr__(self):
         return 'objcall(%s, %s)' % (self.function, self.original_args)
```

### Comparing `numba-0.8.1/numba/nodes/excnodes.py` & `numba-0.9.0/numba/nodes/excnodes.py`

 * *Files 1% similar despite different names*

```diff
@@ -57,15 +57,15 @@
                  **kwargs):
         super(RaiseNode, self).__init__(**kwargs)
         self.exception_type = None
         if isinstance(exc_type, type) and issubclass(exc_type, BaseException):
             self.exception_type = exc_type
             exc_type = const(exc_type, object_)
         if isinstance(exc_msg, (str, unicode)):
-            exc_msg = const(exc_msg, c_string_type)
+            exc_msg = const(exc_msg, char.pointer())
 
         self.exc_type = exc_type
         self.exc_msg = exc_msg
         self.exc_args = exc_args
 
         self.print_on_trap = print_on_trap
```

### Comparing `numba-0.8.1/numba/nodes/usernode.py` & `numba-0.9.0/numba/nodes/usernode.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/pointernodes.py` & `numba-0.9.0/numba/nodes/pointernodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/numpynodes.py` & `numba-0.9.0/numba/nodes/numpynodes.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,16 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import collections
 
+import llvm.core
+
 from numba import typesystem
+from numba.typesystem import tbaa
 from numba.nodes import *
-import numba.nodes
 from numba.ndarray_helpers import PyArrayAccessor
 
 #----------------------------------------------------------------------------
 # External Utilities
 #----------------------------------------------------------------------------
 
 def is_constant_index(node):
@@ -27,27 +29,27 @@
 #----------------------------------------------------------------------------
 # Internal Utilities
 #----------------------------------------------------------------------------
 
 def _const_int(X):
     return llvm.core.Constant.int(llvm.core.Type.int(), X)
 
-def get_shape(builder, tbaa, shape_pointer, ndim):
+def get_shape(builder, tbaa_metadata, shape_pointer, ndim):
     "Load the shape values from an ndarray"
-    shape_metadata = tbaa.get_metadata(typesystem.numpy_shape)
+    shape_metadata = tbaa_metadata.get_metadata(tbaa_metadata.numpy_shape)
 
     for i in range(ndim):
         shape_ptr = builder.gep(shape_pointer, [_const_int(i)])
         extent = builder.load(shape_ptr)
         extent.set_metadata("tbaa", shape_metadata)
         yield extent
 
-def get_strides(builder, tbaa, strides_pointer, ndim):
+def get_strides(builder, tbaa_metadata, strides_pointer, ndim):
     "Load the stride values from an ndarray"
-    stride_metadata = tbaa.get_metadata(typesystem.numpy_strides)
+    stride_metadata = tbaa_metadata.get_metadata(tbaa.numpy_strides)
 
     for i in range(ndim):
         stride_ptr = builder.gep(strides_pointer, [_const_int(i)])
         stride = builder.load(stride_ptr)
         stride.set_metadata("tbaa", stride_metadata)
         yield stride
 
@@ -189,17 +191,17 @@
 
     def __init__(self, attribute_name, array):
         self.array = array
         self.attr_name = attribute_name
 
         self.array_type = array.variable.type
         if attribute_name == 'ndim':
-            type = minitypes.int_
+            type = int_
         elif attribute_name in ('shape', 'strides'):
-            type = typesystem.SizedPointerType(typesystem.intp,
+            type = typesystem.sized_pointer(typesystem.npy_intp,
                                                 size=self.array_type.ndim)
         elif attribute_name == 'data':
             type = self.array_type.dtype.pointer()
         else:
             raise error._UnknownAttribute(attribute_name)
 
         self.type = type
@@ -211,17 +213,17 @@
     # NOTE: better do this at code generation time, and not depend on
     #       variable.lvalue
     _fields = ['array']
 
     def __init__(self, array):
         super(ShapeAttributeNode, self).__init__('shape', array)
         self.array = array
-        self.element_type = typesystem.intp
-        self.type = minitypes.CArrayType(self.element_type,
-                                         array.variable.type.ndim)
+        self.element_type = typesystem.npy_intp
+        self.type = typesystem.carray(self.element_type,
+                                      array.variable.type.ndim)
 
 #----------------------------------------------------------------------------
 # NumPy Array Creation
 #----------------------------------------------------------------------------
 
 class ArrayNewNode(ExprNode):
     """
@@ -288,15 +290,15 @@
     return MultiArrayAPINode('PyArray_SetBaseObject', signature, args)
 
 def PyArray_UpdateFlags(args):
     return MultiArrayAPINode('PyArray_UpdateFlags', void(object_, int_), args)
 
 def PyArray_Empty(args, name='PyArray_Empty'):
     nd, shape, dtype, fortran = args
-    return_type = minitypes.ArrayType(dtype, nd)
+    return_type = typesystem.array(dtype, nd)
     signature = return_type(
                 int_,                   # nd
                 npy_intp.pointer(),     # shape
                 object_,                # dtype
                 int_)                   # fortran
     return MultiArrayAPINode(name, signature, args)
```

### Comparing `numba-0.8.1/numba/nodes/extnodes.py` & `numba-0.9.0/numba/nodes/extnodes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/nodes/__init__.py` & `numba-0.9.0/numba/nodes/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,23 +1,16 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import ast
-import ctypes
 
-import numba
-import numba.functions
-from numba import function_util
 from numba import *
+from numba import function_util
 from numba.symtab import Variable
 from numba import typesystem
-from numba import utils, error
-from numba import typesystem
-from numba.minivect import minitypes, minierror
-
-import llvm.core
+from numba import utils
 
 context = utils.get_minivect_context()
 
 #----------------------------------------------------------------------------
 # Utility Functions
 #----------------------------------------------------------------------------
 
@@ -33,15 +26,15 @@
     return node
 
 def call_pyfunc(py_func, args):
     "Generate an object call for a python function given during compilation time"
     func = ObjectInjectNode(py_func)
     return ObjectCallNode(None, func, args)
 
-def call_obj(call_node, py_func):
+def call_obj(call_node, py_func=None):
     nargs = len(call_node.args)
     signature = typesystem.pyfunc_signature(nargs)
     node = ObjectCallNode(signature, call_node.func,
                           call_node.args,
                           call_node.keywords,
                           py_func)
     return node
```

### Comparing `numba-0.8.1/numba/control_flow/control_flow.py` & `numba-0.9.0/numba/control_flow/control_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1021,15 +1021,15 @@
             'ifs' represent a chain of ANDs
         """
         assert len(node.generators) > 0
 
         # Create innermost body, i.e. list.append(expr)
         # TODO: size hint for PyList_New
         list_create = ast.List(elts=[], ctx=ast.Load())
-        list_create.type = object_ # typesystem.ListType()
+        list_create.type = object_ # typesystem.list_()
         list_create = nodes.CloneableNode(list_create)
         list_value = nodes.CloneNode(list_create)
         list_append = ast.Attribute(list_value, "append", ast.Load())
         append_call = ast.Call(func=list_append, args=[node.elt],
                                keywords=[], starargs=None, kwargs=None)
 
         # Build up the loops from inwards to outwards
@@ -1068,14 +1068,15 @@
         raise error.NumbaError(
                 node, "Dict comprehensions are not yet supported")
 
     def visit_With(self, node):
         node.context_expr = self.visit(node.context_expr)
         if node.optional_vars:
             # TODO: Mark these as assignments!
+            # Note: This is current caught in validators.py !
             node.optional_vars = self.visit(node.optional_vars)
 
         self.visitlist(node.body)
         return node
 
     def visit_Raise(self, node):
         raise error.NumbaError(node, "Raise statement not implemented yet")
```

### Comparing `numba-0.8.1/numba/control_flow/tests/test_circular_type_inference.py` & `numba-0.9.0/numba/control_flow/tests/test_circular_type_inference.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from numba.control_flow.tests.test_cfg_type_infer import *
 from numba.testing.test_support import autojit_py3doc
 
 
 
-@autojit_py3doc(warnstyle='simple')
+@autojit_py3doc(warnstyle='simple', warn=False)
 def test_circular_error():
     """
     >>> test_circular_error()
     Traceback (most recent call last):
         ...
     NumbaError: Unable to infer type for assignment to ..., insert a cast or initialize the variable.
     """
@@ -47,15 +47,15 @@
 def test_simple_circular3():
     """
     >>> test_simple_circular3()
     (Value(5), Value(5))
     >>> sig, syms = infer(test_simple_circular3.py_func,
     ...                   functype(None, []))
     >>> types(syms, 'x', 'y')
-    (object_, object_)
+    (object, object)
     """
     x = values[5]
     y = 2.0
     for i in range(10):
         if i > 5:
             x = y
         else:
@@ -111,15 +111,15 @@
 def test_circular_binop():
     """
     >>> test_circular_binop()
     (1.0, 2.0, 1.0, -3L)
     >>> sig, syms = infer(test_circular_binop.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'x', 'y', 'z', 'a')
-    (double, double, double, int)
+    (float64, float64, float64, int)
     """
     x = 1
     y = 2
     for i in range(10):
         if i > 5:
             x = y - z
             z = 1.0
@@ -134,15 +134,15 @@
 def test_circular_compare():
     """
     >>> test_circular_compare()
     (5.0, 1.0)
     >>> sig, syms = infer(test_circular_compare.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'x', 'y')
-    (double, double)
+    (float64, float64)
     """
     x = 1
     for i in range(10):
         if i == 0:
             y = float(x)
         if x < 5:
             x += y
@@ -153,15 +153,15 @@
 def test_circular_compare2():
     """
     >>> test_circular_compare2()
     (2.0, 1.0)
     >>> sig, syms = infer(test_circular_compare.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'x', 'y')
-    (double, double)
+    (float64, float64)
     """
     x = 1
     for i in range(10):
         if i == 0:
             y = float(x)
         if x < 5 and (x > 2 or i == 0):
             x += y
@@ -175,16 +175,18 @@
     1
     2
     3
     4
     (False, 10L)
     >>> sig, syms = infer(test_circular_compare3.py_func,
     ...                   functype(None, []), warn=False)
-    >>> [str(x) for x in types(syms, 'cond', 'x')]
-    ['bool', 'Py_ssize_t']
+    >>> types(syms, 'cond')
+    (bool,)
+    >>> t, = types(syms, 'x'); assert t.is_int
+    >>> assert t.itemsize == Py_ssize_t.itemsize
     """
     x = 1
     cond = True
     for i in range(10):
         if cond:
             x = i
         else:
@@ -208,15 +210,15 @@
     >>> test_delayed_array_indexing()
     (array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.]), 1.0, 10L)
     >>> sig, syms = infer(test_delayed_array_indexing.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'array', 'var', 'x')
     (float64[:], float64, int)
     """
-    array = np.ones(10, dtype=np.double)
+    array = np.ones(10, dtype=np.float64)
     x = 0
     for i in range(11):
         var = array[x]
         array[x] = var * x
         x = int(i * 1.0)
 
     return array, var, x
@@ -230,15 +232,15 @@
     >>> assert np.all(row == row2)
 
     >>> sig, syms = infer(test_delayed_array_slicing.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'array', 'row')
     (float64[:, :], float64[:])
     """
-    array = np.ones((8, 10), dtype=np.double)
+    array = np.ones((8, 10), dtype=np.float64)
     for i in range(8):
         row = array[i, :]
         array[i, i] = row[i] * i
         array = array[:, :]
 
     return array, row
 
@@ -254,15 +256,15 @@
     >>> sig, syms = infer(test_delayed_array_slicing.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 'array', 'row')
     (float64[:, :], float64[:])
     """
     for i in range(8):
         if i == 0:
-            array = np.ones((8, 10), dtype=np.double)
+            array = np.ones((8, 10), dtype=np.float64)
 
         row = array[i, :]
         array[i, i] = row[i] * i
         array = array[:, :]
 
     return array, row
 
@@ -270,15 +272,15 @@
 def test_delayed_string_indexing_simple():
     """
     >>> test_delayed_string_indexing_simple()
     ('eggs', 3L)
     >>> sig, syms = infer(test_delayed_string_indexing_simple.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 's', 'x')
-    (const char *, Py_ssize_t)
+    (string, Py_ssize_t)
     """
     s = "spam ham eggs"
     for i in range(4):
         if i < 3:
             x = i + i
 
         s = s[x:]
@@ -290,15 +292,15 @@
 def test_delayed_string_indexing():
     """
     >>> test_delayed_string_indexing()
     ('ham eggs', 3L)
     >>> sig, syms = infer(test_delayed_string_indexing.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 's', 'x')
-    (const char *, Py_ssize_t)
+    (string, Py_ssize_t)
     """
     s = "spam ham eggs"
     for i in range(4):
         if i < 3:
             x = i
             tmp1 = s[x:]
             tmp2 = tmp1
@@ -316,15 +318,15 @@
 def test_delayed_string_indexing2():
     """
     >>> test_delayed_string_indexing2()
     ('ham eggs', 3L)
     >>> sig, syms = infer(test_delayed_string_indexing2.py_func,
     ...                   functype(None, []), warn=False)
     >>> types(syms, 's', 'x')
-    (const char *, Py_ssize_t)
+    (string, Py_ssize_t)
     """
     for i in range(4):
         if i == 0:
             s = "spam ham eggs"
 
         if i < 3:
             x = i
@@ -336,47 +338,45 @@
         else:
             s = "hello"
 
         x = i
 
     return s, x
 
-@autojit_py3doc(warn=False)
+@autojit_py3doc(warn=False, warnstyle='simple')
 def test_string_indexing_error():
     """
-    >>> test_string_indexing_error()
-    Traceback (most recent call last):
-        ...
-    NumbaError: Cannot promote types (char, const char *) for variable s
+    >>> try: test_string_indexing_error()
+    ... except Exception as e: print(e)
+    Cannot promote types string and char
     """
     for i in range(4):
         if i == 0:
             s = "spam ham eggs"
 
         if i < 3:
             s = s[i]
         elif i < 5:
             s = s[i:]
 
-@autojit_py3doc(warn=False)
+@autojit_py3doc(warn=False, warnstyle='simple')
 def test_string_indexing_error2():
     """
-    >>> chr(test_string_indexing_error2())
-    Traceback (most recent call last):
-        ...
-    NumbaError: Cannot promote types (char, const char *) for variable s
+    >>> try: chr(test_string_indexing_error2())
+    ... except Exception as e: print(e)
+    Cannot promote types string and char
     """
     for i in range(4):
         if i == 0:
             s = "spam ham eggs"
         s = s[i]
 
     return s
 
-@autojit(warn=False)
+@autojit(warn=False, warnstyle='simple')
 def test_string_indexing_valid():
     """
     >>> chr(test_string_indexing_valid())
     'm'
     """
     for i in range(4):
         s = "spam ham eggs"
@@ -389,15 +389,15 @@
 #------------------------------------------------------------------------
 
 @autojit
 def simple_func(x):
     y = x * x + 4
     return y
 
-@autojit_py3doc(warn=False)
+@autojit_py3doc(warn=False, warnstyle='simple')
 def test_simple_call():
     """
     >>> test_simple_call()
     1091100052L
     >>> infer_simple(test_simple_call, 'x')
     (int,)
     """
@@ -414,30 +414,30 @@
 
 @autojit(warn=False)
 def test_simple_call_promotion():
     """
     >>> test_simple_call_promotion()
     26640768404.0
     >>> infer_simple(test_simple_call_promotion, 'x')
-    (double,)
+    (float64,)
     """
     x = 0
     for i in range(5):
         x = func_with_promotion(x)
 
     return x
 
 #print test_simple_call_promotion.py_func()
 
 @autojit
 def func_with_promotion2(x):
     y = x * x + 4.0
     return np.sqrt(y) + 1j
 
-@autojit(warn=False)
+@autojit(warn=False, warnstyle='simple')
 def test_simple_call_promotion2():
     """
     >>> result =test_simple_call_promotion2()
     >>> "%.4f" % round(result.real, 4)
     '3.9818'
     >>> round(result.imag, 4)
     3.9312
@@ -456,16 +456,8 @@
 # Test Utilities
 #------------------------------------------------------------------------
 
 def infer_simple(numba_func, *varnames):
     sig, syms = infer(numba_func.py_func, functype(None, []), warn=False)
     return types(syms, *varnames)
 
-#from numba.minivect import minitypes
-#sig = minitypes.FunctionType(None, [])
-#func = jit(sig)(test_delayed_string_indexing_simple.py_func)
-#print vars(func)
-#test_delayed_string_indexing_simple()
-#test_delayed_array_slicing2()
-#test_simple_circular()
-#test_circular_error()
 testmod()
```

### Comparing `numba-0.8.1/numba/control_flow/tests/test_w_uninitialized_for.py` & `numba-0.9.0/numba/control_flow/tests/test_w_uninitialized_for.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/tests/test_ast_cfg.py` & `numba-0.9.0/numba/control_flow/tests/test_ast_cfg.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import numba
 from numba import *
 
 if not numba.PY3:
     #@jit(void(int_)) # directives={'control_flow.dot_output': 'out.dot'})
     #@jit(void, [int_], backend='bytecode')
-    @jit(void(int_), nopython=True)
+    @jit(void(int_))
     def func(x):
         i = 0
         #y = 12
         h = 30
         print(i)
         while i < 10:
             if x > i:
```

### Comparing `numba-0.8.1/numba/control_flow/tests/test_cfg_type_infer.py` & `numba-0.9.0/numba/control_flow/tests/test_cfg_type_infer.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 import numpy as np
 
 from numba.testing.test_support import *
-from numba.minivect import minitypes
+from numba import typesystem
 from numba import pipeline, environment, functions, error
 
 def construct_infer_pipeline():
     order = environment.default_pipeline_order
     dump_cfg_index = order.index('dump_cfg')
     return pipeline.ComposedPipelineStage(order[:dump_cfg_index+1])
 
 def functype(restype=None, argtypes=()):
-    return minitypes.FunctionType(return_type=restype, args=list(argtypes))
+    return typesystem.function(return_type=restype, args=list(argtypes))
 
 def lookup(block, var_name):
     var = None
     try:
         var = block.symtab.lookup_most_recent(var_name)
     except (AssertionError, KeyError):
         if block.idom:
@@ -58,17 +58,17 @@
 @autojit
 def test_reassign(obj):
     """
     >>> test_reassign(object())
     'hello'
     >>> sig, syms = infer(test_reassign.py_func, functype(None, [object_]))
     >>> sig
-    const char * (*)(object_)
+    string (*)(object)
     >>> syms['obj'].type
-    const char *
+    string
     """
     obj = 1
     obj = 1.0
     obj = 1 + 4j
     obj = 2
     obj = "hello"
     return obj
@@ -77,15 +77,15 @@
 def test_if_reassign(obj1, obj2):
     """
     >>> test_if_reassign(*values[:2])
     (4.0, 5.0)
     >>> sig, syms = infer(test_if_reassign.py_func,
     ...                   functype(None, [object_] * 2))
     >>> types(syms, 'obj1', 'obj2')
-    (double, object_)
+    (float64, object)
     """
     x = 4.0
     y = 5.0
     z = 6.0
     if int(obj1) < int(obj2):
         obj1 = x
         obj2 = y
@@ -103,15 +103,15 @@
     ('hello', 'world', 'hedgehog')
     >>> test_if_reassign2(2, *values[:2])
     ([Value(0)], Value(12), 'igel')
 
     >>> sig, syms = infer(test_if_reassign2.py_func,
     ...                   functype(None, [int_, object_, object_]))
     >>> types(syms, 'obj1', 'obj2', 'obj3')
-    (object_, object_, const char *)
+    (object, object, string)
     """
     x = 4.0
     y = 5.0
     z = "hedgehog"
     if value < 1:
         obj1 = x
         obj2 = y
@@ -130,16 +130,16 @@
 @autojit_py3doc
 def test_for_reassign(obj1, obj2, obj3, obj4):
     """
     >>> test_for_reassign(*values[:4])
     (9L, Value(1), 2L, 5L)
     >>> sig, syms = infer(test_for_reassign.py_func,
     ...                   functype(None, [object_] * 4))
-    >>> types(syms, 'obj1', 'obj2', 'obj3', 'obj4')
-    (object_, object_, int, Py_ssize_t)
+    >>> types(syms, 'obj1', 'obj2', 'obj3')
+    (object, object, int)
     """
     for i in range(10):
         obj1 = i
 
     for i in range(0):
         obj2 = i
 
@@ -160,15 +160,15 @@
 def test_while_reassign(obj1, obj2, obj3, obj4):
     """
     >>> test_while_reassign(*values[:4])
     (9L, Value(1), 2L, 5L)
     >>> sig, syms = infer(test_while_reassign.py_func,
     ...                   functype(None, [object_] * 4))
     >>> types(syms, 'obj1', 'obj2', 'obj3', 'obj4')
-    (object_, object_, int, int)
+    (object, object, int, int)
     """
     i = 0
     while i < 10:
         obj1 = i
         i += 1
 
     i = 0
@@ -209,26 +209,26 @@
 
     return obj1
 
 
 #
 ### Test for errors
 #
-@autojit
-def test_error_array_variable1(value, obj1):
-    """
-    >>> test_error_array_variable1(0, object())
-    Traceback (most recent call last):
-        ...
-    TypeError: Arrays must have consistent types in assignment for variable 'obj1': 'float32[:]' and 'object_'
-    """
-    if value < 1:
-        obj1 = np.empty(10, dtype=np.float32)
-    
-    return obj1
+# @autojit
+# def test_error_array_variable1(value, obj1):
+#     """
+#     >>> test_error_array_variable1(0, object())
+#     Traceback (most recent call last):
+#         ...
+#     TypeError: Arrays must have consistent types in assignment for variable 'obj1': 'float32[:]' and 'object_'
+#     """
+#     if value < 1:
+#         obj1 = np.empty(10, dtype=np.float32)
+#
+#     return obj1
 
 def test():
     from . import test_cfg_type_infer
     testmod(test_cfg_type_infer)
 
 if __name__ == '__main__':
     testmod()
```

### Comparing `numba-0.8.1/numba/control_flow/tests/test_w_uninitialized_while.py` & `numba-0.9.0/numba/control_flow/tests/test_w_uninitialized_while.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/tests/test_w_uninitialized.py` & `numba-0.9.0/numba/control_flow/tests/test_w_uninitialized.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/tests/test_w_unreachable.py` & `numba-0.9.0/numba/control_flow/tests/test_w_unreachable.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/graphviz.py` & `numba-0.9.0/numba/control_flow/graphviz.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/ssa.py` & `numba-0.9.0/numba/control_flow/ssa.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/delete_cfnode.py` & `numba-0.9.0/numba/control_flow/delete_cfnode.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/control_flow/reaching.py` & `numba-0.9.0/numba/control_flow/reaching.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,13 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 
-from numba import error
 from numba import traits
-from numba import reporting
 from numba.control_flow.cfstats import (
     NameReference, NameAssignment, Uninitialized)
-from numba.reporting import MessageCollection
 
 def allow_null(node):
     return False
 
 
 def check_definitions(env, flow, warner):
     flow.initialize()
```

### Comparing `numba-0.8.1/numba/control_flow/cfstats.py` & `numba-0.9.0/numba/control_flow/cfstats.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/ufunc_builder.py` & `numba-0.9.0/numba/ufunc_builder.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,24 +1,23 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import ast
 import types
 
-from numba import visitors, nodes, error, functions
+from numba import visitors, nodes, error, functions, traits
 
 class UFuncBuilder(object):
     """
     Create a Python ufunc AST function. Demote the types of arrays to scalars
     in the ufunc and generate a return.
     """
 
     ufunc_counter = 0
 
-    def __init__(self, *args, **kwargs):
-        super(UFuncBuilder, self).__init__(*args, **kwargs)
+    def __init__(self):
         self.operands = []
 
     def register_operand(self, node):
         """
         Register a sub-expression as something that will be evaluated
         outside the kernel, and the result of which will be passed into the
         kernel. This can be a variable name:
@@ -76,60 +75,75 @@
         self.operands = []
         return state
 
     def restore(self, state):
         "Restore saved state"
         self.operands = state
 
-
-class UFuncConverter(UFuncBuilder, ast.NodeVisitor):
+@traits.traits
+class UFuncConverter(ast.NodeTransformer):
     """
     Convert a Python array expression AST to a scalar ufunc kernel by demoting
     array types to scalar types.
     """
 
+    build_ufunc_ast = traits.Delegate('ufunc_builder')
+    operands = traits.Delegate('ufunc_builder')
+
+    def __init__(self, env):
+        self.ufunc_builder = UFuncBuilder()
+        self.env = env
+
     def demote_type(self, node):
         node.type = self.demote(node.type)
         if hasattr(node, 'variable'):
             node.variable.type = node.type
 
     def demote(self, type):
         if type.is_array:
             return type.dtype
         return type
 
     def visit_BinOp(self, node):
-        self.demote_type(node)
-        node.left = self.visit(node.left)
-        node.right = self.visit(node.right)
+        if node.type.is_array:
+            self.demote_type(node)
+            node.left = self.visit(node.left)
+            node.right = self.visit(node.right)
+        else:
+            node = self.generic_visit(node)
         return node
 
     def visit_UnaryOp(self, node):
         self.demote_type(node)
-        node.op = self.visit(node.op)
+        node.operand = self.visit(node.operand)
         return node
 
-    def visit_MathNode(self, node):
-        self.demote_type(node)
-        node.arg = self.visit(node.arg)
-
-        # Demote math signature
-        argtypes = [self.demote(argtype) for argtype in node.signature.args]
-        signature = self.demote(node.signature.return_type)(*argtypes)
-        node.signature = signature
-
+    def visit_Call(self, node):
+        if nodes.query(self.env, node, "is_math") and node.type.is_array:
+            self.demote_type(node)
+            node.args = list(map(self.visit_scalar_or_array, node.args))
+        else:
+            node = self.generic_visit(node)
         return node
 
     def visit_CoercionNode(self, node):
         return self.visit(node.node)
 
     def _generic_visit(self, node):
         super(UFuncBuilder, self).generic_visit(node)
 
+    def visit_scalar_or_array(self, node):
+        if node.type.is_array:
+            node =  self.visit(node)
+            self.demote_type(node)
+            return node
+        else:
+            return self.generic_visit(node)
+
     def generic_visit(self, node):
         """
         Register Name etc as operands to the ufunc
         """
-        result = self.register_operand(node)
+        result = self.ufunc_builder.register_operand(node)
         result.type = node.type
         self.demote_type(result)
         return result
```

### Comparing `numba-0.8.1/numba/specialize/loops.py` & `numba-0.9.0/numba/specialize/loops.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import ast
 import textwrap
 
 import numba
 from numba import *
-from numba import error, closures, function_util
-from numba import macros, utils, typesystem
-from numba.symtab import Variable
-from numba import visitors, nodes, error, functions
-from numba.typesystem import get_type, is_obj, typematch
+from numba import error
+from numba import typesystem
+from numba import visitors, nodes
+from numba.typesystem import get_type
 from numba.specialize import loopimpl
 
 logger = logging.getLogger(__name__)
 
 #------------------------------------------------------------------------
 # Utilities
 #------------------------------------------------------------------------
@@ -201,15 +200,15 @@
         node.target = target_temp.store()
 
         #--------------------------------------------------------------------
         # Create range(A.shape[0])
         #--------------------------------------------------------------------
 
         call_func = ast.Name(id='range', ctx=ast.Load())
-        nodes.typednode(call_func, typesystem.RangeType())
+        nodes.typednode(call_func, typesystem.range_)
 
         shape_index = ast.Index(nodes.ConstNode(0, typesystem.Py_ssize_t))
         shape_index.type = typesystem.npy_intp
 
         stop = ast.Subscript(value=nodes.ShapeAttributeNode(orig_iter),
                              slice=shape_index,
                              ctx=ast.Load())
```

### Comparing `numba-0.8.1/numba/specialize/loopimpl.py` & `numba-0.9.0/numba/specialize/loopimpl.py`

 * *Files 0% similar despite different names*

```diff
@@ -111,10 +111,10 @@
         "Length of the iterable"
         raise NotImplementedError
 
 #------------------------------------------------------------------------
 # Register Loop Implementations
 #------------------------------------------------------------------------
 
-register_iterator_implementation("object_", NativeIteratorImpl("PyObject_GetIter",
-                                                               "PyIter_Next"))
+register_iterator_implementation("object", NativeIteratorImpl("PyObject_GetIter",
+                                                              "PyIter_Next"))
```

### Comparing `numba-0.8.1/numba/specialize/funccalls.py` & `numba-0.9.0/numba/specialize/funccalls.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
+
 import numba
 from numba import *
-from numba import visitors, nodes, error, functions, transforms
-from numba.typesystem import is_obj, promote_closest, promote_to_native
+from numba import visitors, nodes, error, transforms
+from numba.typesystem import is_obj
 
 logger = logging.getLogger(__name__)
 
 from numba.external import pyapi
 
 class FunctionCallSpecializer(visitors.NumbaTransformer,
-                              visitors.NoPythonContextMixin,
-                              transforms.BuiltinResolverMixinBase):
+                              visitors.NoPythonContextMixin):
 
     def visit_NativeCallNode(self, node):
         if is_obj(node.signature.return_type):
             if self.nopython:
                 raise error.NumbaError(
                     node, "Cannot call function returning object in "
                           "nopython context")
```

### Comparing `numba-0.8.1/numba/specialize/comparisons.py` & `numba-0.9.0/numba/specialize/comparisons.py`

 * *Files 1% similar despite different names*

```diff
@@ -113,15 +113,16 @@
 
             # Set result type of comparison:
             #     bool array of array comparison
             #     bool otherwise
 
             if left.type.is_array or right.type.is_array:
                 # array < x -> Array(bool_, array.ndim)
-                result_type = self.context.promote_types(left.type, right.type)
+                result_type = self.env.crnt.typesystem.promote(
+                    left.type, right.type)
             else:
                 result_type = bool_
 
             nodes.typednode(node, result_type)
 
             # Handle comparisons specially based on their types
             node = self.single_compare(node)
```

### Comparing `numba-0.8.1/numba/specialize/exttypes.py` & `numba-0.9.0/numba/specialize/exttypes.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,25 +5,25 @@
 from numba import error
 from numba import typesystem
 from numba import visitors
 from numba import nodes
 from numba import function_util
 from numba.exttypes import virtual
 from numba.traits import traits, Delegate
-from numba.typesystem import is_obj, promote_closest, promote_to_native
 
 class ExtensionTypeLowerer(visitors.NumbaTransformer):
     """
     Lower extension type attribute accesses and method calls.
     """
 
     def get_handler(self, ext_type):
-        if ext_type.is_jit_extension:
+        if ext_type.is_extension and not ext_type.is_autojit_exttype:
             return StaticExtensionHandler()
         else:
+            assert ext_type.is_autojit_exttype, ext_type
             return DynamicExtensionHandler()
 
     # ______________________________________________________________________
     # Attributes
 
     def visit_ExtTypeAttribute(self, node):
         """
@@ -159,15 +159,15 @@
         However, we could *preload* (**vtab_slot), where function calls
         invalidate the preload, if we were so inclined.
         """
         # Make the object we call the method on clone-able
         node.value = nodes.CloneableNode(node.value)
 
         ext_type = node.ext_type
-        func_signature = node.type
+        func_signature = node.type #typesystem.extmethod_to_function(node.type)
         offset = ext_type.vtab_offset
 
         # __________________________________________________________________
         # Retrieve vtab
 
         vtab_ppp = nodes.value_at_offset(node.value, offset,
                                          void.pointer().pointer())
```

### Comparing `numba-0.8.1/numba/specialize/exceptions.py` & `numba-0.9.0/numba/specialize/exceptions.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,17 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import ast
 
-import numba
 from numba import *
-from numba import visitors, nodes, error, functions, function_util
+from numba import visitors, nodes, error, function_util
 
 logger = logging.getLogger(__name__)
 
-from numba.external import pyapi
-from numba.typesystem import is_obj, promote_closest, promote_to_native
+from numba.typesystem import is_obj
 
 #------------------------------------------------------------------------
 # Specialize Error Checking and Raising
 #------------------------------------------------------------------------
 
 class ExceptionSpecializer(visitors.NumbaTransformer):
     """
```

### Comparing `numba-0.8.1/numba/visitors.py` & `numba-0.9.0/numba/visitors.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,19 +2,20 @@
 from __future__ import print_function, division, absolute_import
 import ast
 import ast as ast_module
 try:
     import __builtin__ as builtins
 except ImportError:
     import builtins
+
 import types
 from numba import functions, PY3
 from numba import nodes
 from numba.nodes.metadata import annotate, query
-from numba.typesystem.typemapper import have_properties
+from numba.typesystem.promotion import have_properties
 
 try:
     import numbers
 except ImportError:
     # pre-2.6
     numbers = None
 
@@ -91,15 +92,15 @@
                             continue
                         self.varnames.extend((_name for _name in _var.co_varnames
                                               if not _name.startswith('.')))
                         recurse_co_consts(_var)
 
                 recurse_co_consts(f_code)
 
-            self.argnames = self.varnames[:f_code.co_argcount]
+            self.argnames = tuple(self.varnames[:f_code.co_argcount])
 
             if f_code.co_cellvars:
                 self.varnames.extend(
                     cellvar for cellvar in f_code.co_cellvars
                     if cellvar not in self.varnames)
 
             self.cellvars = set(f_code.co_cellvars)
```

### Comparing `numba-0.8.1/numba/ad.py` & `numba-0.9.0/numba/ad.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/templating.py` & `numba-0.9.0/numba/templating.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/llvm_types.py` & `numba-0.9.0/numba/llvm_types.py`

 * *Files 18% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 
 import ctypes
 import struct as struct_
 import llvm.core as lc
 
 from numba import utils
 from numba.typedefs import _trace_refs_, PyObject_HEAD
+from numba.typesystem import numba_typesystem
 
 import logging
 
 logger = logging.getLogger(__name__)
 
 # ______________________________________________________________________
 
@@ -39,15 +40,16 @@
 _float = lc.Type.float()
 _double = lc.Type.double()
 _complex64 = lc.Type.struct([_float, _float])
 _complex128 = lc.Type.struct([_double, _double])
 
 
 def to_llvm(type):
-    return type.to_llvm(utils.context)
+    return numba_typesystem.convert("llvm", type)
+    # return type.to_llvm(utils.context)
 
 _pyobject_head = [to_llvm(ty) for name, ty in PyObject_HEAD.fields]
 _pyobject_head_struct = to_llvm(PyObject_HEAD)
 _pyobject_head_struct_p = lc.Type.pointer(_pyobject_head_struct)
 
 _head_len = len(_pyobject_head)
 _numpy_struct = lc.Type.struct(_pyobject_head+\
@@ -129,27 +131,37 @@
             ret_val = builder.fptosi(lval1, lty2)
         return ret_val
 
     CAST_MAP = {
         lc.TYPE_POINTER : build_pointer_cast,
         lc.TYPE_INTEGER: build_int_cast,
 
-        (lc.TYPE_FLOAT, lc.TYPE_DOUBLE) : build_float_ext,
-        (lc.TYPE_DOUBLE, lc.TYPE_FP128) : build_float_ext,
+        (lc.TYPE_FLOAT, lc.TYPE_DOUBLE)     : build_float_ext,
+        (lc.TYPE_DOUBLE, lc.TYPE_FP128)     : build_float_ext,
+        (lc.TYPE_DOUBLE, lc.TYPE_PPC_FP128) : build_float_ext,
+        (lc.TYPE_DOUBLE, lc.TYPE_X86_FP80)  : build_float_ext,
+
+        (lc.TYPE_DOUBLE, lc.TYPE_FLOAT)     : build_float_trunc,
+        (lc.TYPE_FP128, lc.TYPE_DOUBLE)     : build_float_trunc,
+        (lc.TYPE_PPC_FP128, lc.TYPE_DOUBLE) : build_float_trunc,
+        (lc.TYPE_X86_FP80, lc.TYPE_DOUBLE)  : build_float_trunc,
+
+        (lc.TYPE_INTEGER, lc.TYPE_FLOAT)    : build_int_to_float_cast,
+        (lc.TYPE_INTEGER, lc.TYPE_DOUBLE)   : build_int_to_float_cast,
+        (lc.TYPE_INTEGER, lc.TYPE_FP128)    : build_int_to_float_cast,
+        (lc.TYPE_INTEGER, lc.TYPE_PPC_FP128): build_int_to_float_cast,
+        (lc.TYPE_INTEGER, lc.TYPE_X86_FP80) : build_int_to_float_cast,
+
+        (lc.TYPE_FLOAT, lc.TYPE_INTEGER)    : build_float_to_int_cast,
+        (lc.TYPE_DOUBLE, lc.TYPE_INTEGER)   : build_float_to_int_cast,
+        (lc.TYPE_FP128, lc.TYPE_INTEGER)    : build_float_to_int_cast,
+        (lc.TYPE_PPC_FP128, lc.TYPE_INTEGER): build_float_to_int_cast,
+        (lc.TYPE_X86_FP80, lc.TYPE_INTEGER) : build_float_to_int_cast,
 
-        (lc.TYPE_DOUBLE, lc.TYPE_FLOAT) : build_float_trunc,
-        (lc.TYPE_FP128, lc.TYPE_DOUBLE) : build_float_trunc,
-
-        (lc.TYPE_INTEGER, lc.TYPE_FLOAT) : build_int_to_float_cast,
-        (lc.TYPE_INTEGER, lc.TYPE_DOUBLE) : build_int_to_float_cast,
-
-        (lc.TYPE_FLOAT, lc.TYPE_INTEGER) : build_float_to_int_cast,
-        (lc.TYPE_DOUBLE, lc.TYPE_INTEGER) : build_float_to_int_cast,
-
-    }
+        }
 
     @classmethod
     def build_cast(cls, builder, lval1, lty2, *args, **kws):
         ret_val = lval1
         lty1 = lval1.type
         lkind1 = lty1.kind
         lkind2 = lty2.kind
```

### Comparing `numba-0.8.1/numba/multiarray_api.py` & `numba-0.9.0/numba/multiarray_api.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/reporting.py` & `numba-0.9.0/numba/reporting.py`

 * *Files 7% similar despite different names*

```diff
@@ -71,14 +71,15 @@
     return not is_error, lineno, colno, message
 
 class MessageCollection(object):
     """Collect error/warnings messages first then sort"""
 
     def __init__(self, ast=None, source_lines=None, file=None):
         # (node, is_error, message)
+        self.buf = []
         self.file = file or sys.stdout
         self.ast = ast
         self.source_lines = source_lines
         self.messages = []
         self.have_errors = False
 
     def error(self, node, message):
@@ -91,15 +92,15 @@
     def header(self):
         pass
 
     def footer(self):
         pass
 
     def report_message(self, message, node, type):
-        self.file.write(format_msg_simple(type, node, message))
+        self.buf.append(format_msg_simple(type, node, message))
 
     def report(self, post_mortem=False):
         self.messages.sort(key=sort_message)
 
         if self.messages:
             self.header()
 
@@ -110,48 +111,56 @@
                 type = "Error"
             else:
                 type = "Warning"
 
             self.report_message(message, node, type)
 
         if self.messages:
+            self.buf[-1] = self.buf[-1].rstrip() + '\n'
             self.footer()
 
-        if errors and not post_mortem:
-            raise error.NumbaError(*errors[0])
+        message = "".join(self.buf)
+
+        # clear buffer
+        del self.messages[:]
+        del self.buf[:]
 
+        if errors and not post_mortem:
+            if len(message.splitlines()) == 1:
+                raise error.NumbaError(*errors[0])
+            raise error.NumbaError("(see below)\n" + message.strip(), has_report=True)
+        else:
+            self.file.write(message)
 
 class FancyMessageCollection(MessageCollection):
 
     def header(self):
-        self.file.write(" Numba Encountered Errors or Warnings ".center(80, "-") + '\n')
+        self.buf.append(
+            " Numba Encountered Errors or Warnings ".center(80, "-") + '\n')
 
     def footer(self):
-        self.file.write("-" * 80 + '\n')
+        self.buf.append("-" * 80 + '\n')
 
     def report_message(self, message, node, type):
-        self.file.write(format_msg(type, self.source_lines, node, message))
+        self.buf.append(format_msg(type, self.source_lines, node, message))
 
 # ______________________________________________________________________
 
 def format_msg(type, source_lines, node, msg):
     ret = ''
     if node and hasattr(node, 'lineno') and source_lines:
         lineno, colno = getpos(node)
         if lineno < len(source_lines):
             line = source_lines[lineno]
             ret = line + '\n' + "%s^" % ("-" * colno) + '\n'
 
-    return ret + format_msg_simple(type, node, msg)
+    return ret + format_msg_simple(type, node, msg) + "\n"
 
 def format_msg_simple(type, node, message):
-    "Issue a warning"
-    # printing allows us to test the code
     return "%s %s%s\n" % (type, error.format_pos(node), message)
-    # logger.warning("Warning %s: %s", error.format_postup(getpos(node)), message)
 
 # ______________________________________________________________________
 
 def report(env, exc=None):
     """
     :param function_error_env: the FunctionErrorEnvironment
     :param post_mortem: whether to enable post-mortem debugging of Numba
@@ -161,13 +170,12 @@
     post_mortem = function_error_env.enable_post_mortem
     if exc is not None:
         function_error_env.collection.error(exc.node, exc.msg)
 
     try:
         function_error_env.collection.report(post_mortem)
     except error.NumbaError as e:
-        if exc is None:
-            exc = e
+        exc = e
 
     if exc is not None and not post_mortem:
         # Shorten traceback
         raise exc
```

### Comparing `numba-0.8.1/numba/pycc/compiler.py` & `numba-0.9.0/numba/pycc/compiler.py`

 * *Files 2% similar despite different names*

```diff
@@ -128,14 +128,16 @@
         with open(output, 'wb') as fout:
             lmod.to_bitcode(fout)
 
     def write_native_object(self, output, **kws):
         self._process_inputs(**kws)
         lmod = self._cull_exports()
         tm = le.TargetMachine.new(reloc=le.RELOC_PIC, features='-avx')
+        if not kws.get('wrap'):
+            _hack_strip_python_ref(lmod)
         with open(output, 'wb') as fout:
             objfile = tm.emit_object(lmod)
             fout.write(objfile)
 
     def emit_header(self, output):
         from numba.minivect import minitypes
 
@@ -375,7 +377,34 @@
         builder.ret(NULL)
 
         builder.position_at_end(cond_false)
         builder.ret(mod)
 
 
 Compiler = CompilerPy3 if PY3 else CompilerPy2
+
+
+# XXX: hack
+def _hack_strip_python_ref(mod):
+    if int(os.environ.get('NO_PYCC_SYMBOL_STRIP', False)):
+        return # do nothing if the environment variable is set
+
+    removeglobals = ['PyArray_API']
+    for g in removeglobals:
+        try:
+            gv = mod.get_global_variable_named(g)
+        except:
+            pass
+        else:
+            if not gv.uses:
+                gv.delete()
+    removethese = ['IndexAxis', 'NewAxis', 'Broadcast']
+    while True:
+        for func in mod.functions:
+            if func.name.startswith('Py') and not func.uses:
+                func.delete()
+                break
+            elif func.name in removethese and not func.uses:
+                func.delete()
+                break
+        else:
+            break
```

### Comparing `numba-0.8.1/numba/pycc/__init__.py` & `numba-0.9.0/numba/pycc/__init__.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tools/astformat.py` & `numba-0.9.0/numba/tools/astformat.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/naming.py` & `numba-0.9.0/numba/naming.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/metadata.py` & `numba-0.9.0/numba/metadata.py`

 * *Files 0% similar despite different names*

```diff
@@ -109,15 +109,15 @@
                 root = self.metadata_cache[type.root]
             else:
                 root = self.get_metadata(type.root)
         else:
             root = self.find_root(type)
 
         node = self.make_metadata(typename(type), root,
-                                  is_constant="const" in type.qualifiers)
+                                  ) #is_constant="const" in type.qualifiers)
 
         # Cache result
         self.metadata_cache[type] = node
 
         return node
 
     def set_metadata(self, load_instr, metadata):
```

### Comparing `numba-0.8.1/numba/ndarray_helpers.py` & `numba-0.9.0/numba/ndarray_helpers.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 #    int *dimensions, *strides;      // 2, 3
 #    PyObject *base;                 // 4
 #    PyArray_Descr *descr;           // 5
 #    int flags;                      // 6
 #    } PyArrayObject;
 
 from numba import *
-from numba import typesystem
+from numba.typesystem import tbaa
 from numba.llvm_types import _head_len, _int32
 import llvm.core as lc
 
 const_int = lambda X: lc.Constant.int(_int32, X)
 
 def set_metadata(tbaa, instr, type):
     if type is not None:
@@ -78,33 +78,33 @@
     data = property(get_data, set_data, "The array.data attribute")
 
     def typed_data(self, context):
         data = self.data
         ltype = self.dtype.pointer().to_llvm(context)
         return self.builder.bitcast(data, ltype)
 
-    @make_property(typesystem.numpy_ndim)
+    @make_property(tbaa.numpy_ndim)
     def ndim(self):
         return self._get_element(1)
 
-    @make_property(typesystem.numpy_shape.pointer().qualify("const"))
+    @make_property(tbaa.numpy_shape.pointer().qualify("const"))
     def dimensions(self):
         return self._get_element(2)
 
     shape = dimensions
 
-    @make_property(typesystem.numpy_strides.pointer().qualify("const"))
+    @make_property(tbaa.numpy_strides.pointer().qualify("const"))
     def strides(self):
         return self._get_element(3)
 
-    @make_property(typesystem.numpy_base)
+    @make_property(tbaa.numpy_base)
     def base(self):
         return self._get_element(4)
 
-    @make_property(typesystem.numpy_dtype)
+    @make_property(tbaa.numpy_dtype)
     def descr(self):
         return self._get_element(5)
 
-    @make_property(typesystem.numpy_flags)
+    @make_property(tbaa.numpy_flags)
     def flags(self):
         return self._get_element(6)
```

### Comparing `numba-0.8.1/numba/scrape_multiarray_api.py` & `numba-0.9.0/numba/scrape_multiarray_api.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/oset.py` & `numba-0.9.0/numba/oset.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/decorators.py` & `numba-0.9.0/numba/decorators.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 import types
 import logging
 import inspect
 
 from numba import *
 from numba import typesystem, numbawrapper
 from numba import  functions
-from .minivect import minitypes
 from numba.utils import  process_signature
 from numba.codegen import llvmwrapper
 from numba import environment
 import llvm.core as _lc
 from numba.wrapping import compiler
 
 logger = logging.getLogger(__name__)
@@ -173,15 +172,15 @@
             nopython=False, locals=None, **kwargs):
     """
     Creates a function that dispatches to type-specialized LLVM
     functions based on the input argument types.  If no specialized
     function exists for a set of input argument types, the dispatcher
     creates and caches a new specialized function at call time.
     """
-    if template_signature and not isinstance(template_signature, minitypes.Type):
+    if template_signature and not isinstance(template_signature, typesystem.Type):
         if callable(template_signature):
             func = template_signature
             return autojit(backend='ast', target=target,
                            nopython=nopython, locals=locals, **kwargs)(func)
         else:
             raise Exception("The autojit decorator should be called: "
                             "@autojit()")
@@ -199,24 +198,32 @@
     def _jit_decorator(func):
         if isinstance(func, CLASS_TYPES):
             cls = func
             kwargs.update(env_name=env_name)
             return jit_extension_class(cls, kwargs, env)
 
         argtys = argtypes
-        if func.__code__.co_argcount == 0 and argtys is None:
+        if argtys is None and restype:
+            assert restype.is_function
+            return_type = restype.return_type
+            argtys = restype.args
+        elif argtys is None:
+            assert func.__code__.co_argcount == 0, func
+            return_type = None
             argtys = []
+        else:
+            return_type = restype
 
         assert argtys is not None
         env.specializations.register(func)
 
         assert kwargs.get('llvm_module') is None # TODO link to user module
         assert kwargs.get('llvm_ee') is None, "Engine should never be provided"
-        sig, lfunc, wrapper = compile_function(env, func, argtys, restype=restype,
-                                    nopython=nopython, **kwargs)
+        sig, lfunc, wrapper = compile_function(
+            env, func, argtys, restype=return_type, nopython=nopython, **kwargs)
         return numbawrapper.create_numba_wrapper(func, wrapper, sig, lfunc)
 
     return _jit_decorator
 
 def _not_implemented(*args, **kws):
     raise NotImplementedError('Bytecode backend is no longer supported.')
 
@@ -259,15 +266,15 @@
     if isinstance(restype, CLASS_TYPES):
         cls = restype
         env = kws.pop('env', None) or environment.NumbaEnvironment.get_environment(
                                                          kws.get('env_name', None))
         return jit_extension_class(cls, kws, env)
 
     # Called with f8(f8) syntax which returns a dictionary of argtypes and restype
-    if isinstance(restype, minitypes.FunctionType):
+    if isinstance(restype, typesystem.function):
         if argtypes is not None:
             raise TypeError("Cannot use both calling syntax and argtypes keyword")
         argtypes = restype.args
         restype = restype.return_type
     # Called with a string like 'f8(f8)'
     elif isinstance(restype, str) and argtypes is None:
         signature = process_signature(restype, kws.get('name', None))
```

### Comparing `numba-0.8.1/numba/containers/tests/test_typed_list.py` & `numba-0.9.0/numba/containers/tests/test_typed_list.py`

 * *Files 10% similar despite different names*

```diff
@@ -133,14 +133,45 @@
     Traceback (most recent call last):
         ...
     TypeError: 'object' object is not iterable
     """
     return nb.typedlist(type, iterable)
 
 @autojit_py3doc
+def test_insert(type):
+    """
+    >>> test_insert(int_)
+    [0, 1, 2, 3, 4, 5]
+    """
+    tlist = nb.typedlist(type, [1,3])
+    tlist.insert(0,0)
+    tlist.insert(2,2)
+    tlist.insert(4,4)
+    tlist.insert(8,5)
+    return tlist
+
+@autojit_py3doc
+def test_remove(type):
+    """
+    >>> test_remove(int_)
+    4
+    3
+    2
+    [1, 3]
+    """
+    tlist = nb.typedlist(type, range(5))
+    tlist.remove(0)
+    print (len(tlist))
+    tlist.remove(2)
+    print (len(tlist))
+    tlist.remove(4)
+    print (len(tlist))
+    return tlist
+
+@autojit_py3doc
 def test_count(type, L):
     """
     >>> test_count(int_, [1, 2, 3, 4, 5, 1, 2])
     (0L, 1L, 2L)
     """
     tlist = nb.typedlist(type, L)
     return tlist.count(0), tlist.count(3), tlist.count(1)
```

### Comparing `numba-0.8.1/numba/containers/register.py` & `numba-0.9.0/numba/containers/register.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/containers/typedtuple.py` & `numba-0.9.0/numba/containers/typedtuple.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/containers/typedlist.py` & `numba-0.9.0/numba/containers/orderedcontainer.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,123 +1,105 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import numba as nb
 from numba import *
-from numba.containers import orderedcontainer
+from numba import nodes
+from numba import typesystem
+from numba.typesystem import get_type
 
 import numpy as np
 
-INITIAL_BUFSIZE = 10
-SHRINK = 1.5
 GROW = 2
 
 def notimplemented(msg):
-    raise NotImplementedError("'%s' method of type 'typedlist'" % msg)
+    raise NotImplementedError("'%s' method" % msg)
 
-_list_cache = {}
+def container_methods(item_type, notimplemented):
+    # NOTE: numba will use the global 'notimplemented' function, not the
+    # one passed in :(
+
+    @item_type(Py_ssize_t) # TODO: slicing!
+    def getitem(self, key):
+        if not (0 <= key < self.size):
+            # TODO: Implement raise !
+            # raise IndexError(key)
+            [][key] # tee hee
+
+        return self.buf[key]
+
+    @void(Py_ssize_t, item_type) # TODO: slice assignment!
+    def setitem(self, key, value):
+        if not (0 <= key < self.size):
+            # TODO: Implement raise !
+            # raise IndexError(key)
+            [][key]
+
+        self.buf[key] = value
+
+    @void(item_type)
+    def append(self, value):
+        size = self.size
+        if size >= self.buf.shape[0]:
+            # NOTE: initial bufsize must be greater than zero
+            self.buf.resize(int(size * GROW), refcheck=False)
+
+        self.buf[size] = value
+        self.size = size + 1
+
+    @void(object_)
+    def extend(self, iterable):
+        # TODO: something fast for common cases (e.g. typedlist,
+        #                                        np.ndarray, etc)
+        for obj in iterable:
+            self.append(obj)
+
+    @Py_ssize_t(item_type)
+    def index(self, value):
+        # TODO: comparison of complex numbers (#121)
+        buf = self.buf
+        for i in range(self.size):
+             if buf[i] == value:
+                 return i
+
+        [].index(value) # raise ValueError
+
+    @Py_ssize_t(item_type)
+    def count(self, value):
+        # TODO: comparison of complex numbers (#121)
+        count = 0
+        buf = self.buf
+        for i in range(self.size):
+             # TODO: promotion of (bool_, int_)
+             if buf[i] == value:
+                 count += 1
+
+        return count
+
+    return locals()
 
 #-----------------------------------------------------------------------
-# Runtime Constructor
+# Infer types for typed containers (typedlist, typedtuple)
 #-----------------------------------------------------------------------
 
-def typedlist(item_type, iterable=None):
+def typedcontainer_infer(compile_typedcontainer, type_node, iterable_node):
     """
-    >>> typedlist(int_)
-    []
-    >>> tlist = typedlist(int_, range(10))
-    >>> tlist
-    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-    >>> tlist[5]
-    5L
+    Type inferer for typed containers, register with numba.register_inferer().
 
-    >>> typedlist(float_, range(10))
-    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
+    :param compile_typedcontainer: item_type -> typed container extension class
+    :param type_node: type parameter to typed container constructor
+    :param iterable_node: value parameter to typed container constructor (optional)
     """
-    typedlist_ctor = compile_typedlist(item_type)
-    return typedlist_ctor(iterable)
+    assert type_node is not None
 
-#-----------------------------------------------------------------------
-# Typedlist implementation
-#-----------------------------------------------------------------------
+    type = get_type(type_node)
+    if type.is_cast:
+        elem_type = type.dst_type
+
+        # Pre-compile typed list implementation
+        typedcontainer_ctor = compile_typedcontainer(elem_type)
+
+        # Inject the typedlist directly to avoid runtime implementation lookup
+        iterable_node = iterable_node or nodes.const(None, object_)
+        result = nodes.call_pyfunc(typedcontainer_ctor, (iterable_node,))
+        return nodes.CoercionNode(result, typedcontainer_ctor.exttype)
 
-def compile_typedlist(item_type, _list_cache=_list_cache):
-    # item_type_t = typesystem.CastType(item_type)
-    # dtype_t = typesystem.NumpyDtypeType(item_type)
-
-    if item_type in _list_cache:
-        return _list_cache[item_type]
-
-    dtype = item_type.get_dtype()
-    methods = orderedcontainer.container_methods(item_type, notimplemented)
-
-    @nb.jit(warn=False)
-    class typedlist(object):
-        @void(object_)
-        def __init__(self, iterable):
-            self.size = 0
-
-            # TODO: Use length hint of iterable for initial buffer size
-            self.buf = np.empty(INITIAL_BUFSIZE, dtype=dtype)
-
-            # TODO: implement 'is'/'is not'
-            if iterable != None:
-                self.extend(iterable)
-
-        # TODO: Jit __getitem__/__setitem__ of numba extension types
-
-        __getitem__ = methods['getitem']
-        __setitem__ = methods['setitem']
-        append = methods['append']
-        extend = methods['extend']
-        index = methods['index']
-        count = methods['count']
-
-        @item_type()
-        def pop(self):
-            # TODO: Optional argument 'index'
-            size = self.size - 1
-            item = self.buf[size]
-            self.size = size
-
-            if INITIAL_BUFSIZE < size < self.buf.shape[0] / 2:
-                self.buf.resize(int(SHRINK * size), refcheck=False)
-
-            return item
-
-        @void(Py_ssize_t, item_type)
-        def insert(self, index, value):
-            notimplemented("insert")
-
-        @void(item_type)
-        def remove(self, value):
-            notimplemented("remove")
-
-        @void()
-        def reverse(self):
-            buf = self.buf
-            size = self.size - 1
-            for i in range(self.size / 2):
-                tmp = buf[i]
-                buf[i] = buf[size - i]
-                buf[size - i] = tmp
-
-        @void()
-        def sort(self):
-            # TODO: optional arguments cmp, key, reverse
-            self.buf[:self.size].sort()
-
-        @Py_ssize_t()
-        def __len__(self):
-            return self.size
-
-        @nb.c_string_type()
-        def __repr__(self):
-            buf = ", ".join([str(self.buf[i]) for i in range(self.size)])
-            return "[" + buf + "]"
-
-    _list_cache[item_type] = typedlist
-    return typedlist
-
-
-if __name__ == "__main__":
-    import doctest
-    doctest.testmod()
+    return object_
```

### Comparing `numba-0.8.1/numba/testing/test_support.py` & `numba-0.9.0/numba/testing/test_support.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 if numba.PY3:
     import re
     def rewrite_doc(doc):
         doc = re.sub(r'(\d+)L', r'\1', doc)
         doc = re.sub(r'([^\.])NumbaError', r'\1numba.error.NumbaError', doc)
         doc = re.sub(r'([^\.])InvalidTemplateError', r'\1numba.error.InvalidTemplateError', doc)
-        doc = re.sub(r'([^\.])UnpromotableTypeError', r'\1numba.minivect.minierror.UnpromotableTypeError', doc)
+        doc = re.sub(r'([^\.])UnpromotableTypeError', r'\1numba.error.UnpromotableTypeError', doc)
         return doc
     def autojit_py3doc(*args, **kwargs):
         if kwargs:
             def _inner(fun):
                 fun.__doc__ = rewrite_doc(fun.__doc__)
                 return autojit(*args, **kwargs)(fun)
             return _inner
```

### Comparing `numba-0.8.1/numba/testing/user_support.py` & `numba-0.9.0/numba/testing/user_support.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/testing/runner.py` & `numba-0.9.0/numba/testing/runner.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/testing/doctest_support.py` & `numba-0.9.0/numba/testing/doctest_support.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/macros.py` & `numba-0.9.0/numba/macros.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 from numba import *
-from .minivect import minitypes
+from numba import typesystem
 from . import llvm_types
 
 import logging
 logger = logging.getLogger(__name__)
 
 # TODO: Create a subclass of
 # llpython.byte_translator.LLVMTranslator that does macro
@@ -23,17 +23,17 @@
     if ub is None:
         ub = c_str_len
     out_len = builder.call(CStringSlice2Len, [c_string, c_str_len, lb, ub])
     ret_val = builder.alloca_array(llvm_types._int8, out_len)
     builder.call(CStringSlice2, [ret_val, c_string, c_str_len, lb, ub])
     return ret_val
 
-c_string_slice_2.__signature__ = minitypes.FunctionType(
-    return_type = c_string_type,
-    args = (c_string_type, Py_ssize_t, Py_ssize_t))
+c_string_slice_2.__signature__ = typesystem.function(
+    return_type = char.pointer(),
+    args = (char.pointer(), Py_ssize_t, Py_ssize_t))
 
 def c_string_slice_1 (context, builder, c_string, lb):
     return c_string_slice_2(context, builder, c_string, lb)
 
-c_string_slice_1.__signature__ = minitypes.FunctionType(
-    return_type = c_string_type,
-    args = (c_string_type, Py_ssize_t))
+c_string_slice_1.__signature__ = typesystem.function(
+    return_type = char.pointer(),
+    args = (char.pointer(), Py_ssize_t))
```

### Comparing `numba-0.8.1/numba/codegen/refcounting.py` & `numba-0.9.0/numba/codegen/refcounting.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/codegen/llvmcontext.py` & `numba-0.9.0/numba/codegen/llvmcontext.py`

 * *Files 8% similar despite different names*

```diff
@@ -122,19 +122,15 @@
                         func_name = func.name
                     else:
                         # If the duplicated function is not the currently
                         # compiling function, ignore it.
                         # We assume this is a utility function.
                         assert func.linkage == lc.LINKAGE_LINKONCE_ODR, func.name
 
-            self.module.link_in(lfunc_module, preserve=False)
-            #
-            #            print 'linked'.center(80, '='), lfunc.module, lfunc.name
-            #            print self.module
-
+            link_module(self.execution_engine, lfunc_module, self.module)
             lfunc = self.module.get_function_named(func_name)
 
         assert lfunc.module is self.module
         self.verify(lfunc)
         #        print lfunc
         return lfunc
 
@@ -147,7 +143,34 @@
         for bb in lfunc.basic_blocks:
             for instr in bb.instructions:
                 if isinstance(instr, lc.CallOrInvokeInstruction):
                     callee = instr.called_function
                     if callee is not None:
                         assert callee.module is lfunc.module,\
                         "Inter module call for call to %s" % callee.name
+
+
+# ______________________________________________________________________
+
+handle = lambda llvm_value: llvm_value._ptr
+
+def link_module(engine, src_module, dst_module, preserve=False):
+    """
+    Link a source module into a destination module while preserving the
+    execution engine's global mapping of pointers.
+    """
+    dst_module.link_in(src_module, preserve=preserve)
+    ptr = lambda gv: handle(engine).getPointerToGlobalIfAvailable(handle(gv))
+
+    def update_gv(src_gv, dst_gv):
+        if ptr(src_gv) != 0 and ptr(dst_gv) == 0:
+            engine.add_global_mapping(dst_gv, ptr(src_gv))
+
+    # Update function mapping
+    for function in src_module.functions:
+        dst_lfunc = dst_module.get_function_named(function.name)
+        update_gv(function, dst_lfunc)
+
+    # Update other global symbols' mapping
+    for src_gv in src_module.global_variables:
+        dst_gv = dst_module.get_global_variable_named(src_gv.name)
+        update_gv(src_gv, dst_gv)
```

### Comparing `numba-0.8.1/numba/codegen/coerce.py` & `numba-0.9.0/numba/codegen/coerce.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import llvm
 
 from numba import *
+from numba import string_ as c_string_type
 from numba import nodes
 from numba.typesystem import is_obj, promote_to_native
 from numba.codegen.codeutils import llvm_alloca, if_badval
 from numba.codegen import debug
 
 
 class ObjectCoercer(object):
@@ -34,16 +35,17 @@
 
         float_: "f",
         double: "d",
         complex128: "D",
 
         object_: "O",
         bool_: "b", # ?
-        c_string_type: "s",
+        char.pointer(): "s",
         char.pointer() : "s",
+        c_string_type: "s",
     }
 
     def __init__(self, translator):
         self.context = translator.context
         self.translator = translator
         self.builder = translator.builder
         self.llvm_module = self.builder.basic_block.function.module
@@ -83,15 +85,15 @@
 
     def check_err_int(self, llvm_result, badval):
         llvm_badval = llvm.core.Constant.int(llvm_result.type, badval)
         if_badval(self.translator, llvm_result, llvm_badval,
                   callback=lambda b, *args: b.branch(self.translator.error_label))
 
     def _create_llvm_string(self, str):
-        return self.translator.visit(nodes.ConstNode(str, c_string_type))
+        return self.translator.visit(nodes.ConstNode(str, char.pointer()))
 
     def lstr(self, types, fmt=None):
         "Get an llvm format string for the given types"
         typestrs = []
         result_types = []
         for type in types:
             if is_obj(type):
@@ -132,27 +134,17 @@
             self.translator.puts("done building... %s" % name)
             nodes.print_llvm(self.translator.env, object_, result)
             self.translator.puts("--------------------------")
 
         return result
 
     def npy_intp_to_py_ssize_t(self, llvm_result, type):
-    #        if type == minitypes.npy_intp:
-    #            lpy_ssize_t = minitypes.Py_ssize_t.to_llvm(self.context)
-    #            llvm_result = self.translator.caster.cast(llvm_result, lpy_ssize_t)
-    #            type = minitypes.Py_ssize_t
-
         return llvm_result, type
 
     def py_ssize_t_to_npy_intp(self, llvm_result, type):
-    #        if type == minitypes.npy_intp:
-    #            lnpy_intp = minitypes.npy_intp.to_llvm(self.context)
-    #            llvm_result = self.translator.caster.cast(llvm_result, lnpy_intp)
-    #            type = minitypes.Py_ssize_t
-
         return llvm_result, type
 
     def convert_single_struct(self, llvm_result, type):
         types = []
         largs = []
         for i, (field_name, field_type) in enumerate(type.fields):
             types.extend((c_string_type, field_type))
```

### Comparing `numba-0.8.1/numba/codegen/complexsupport.py` & `numba-0.9.0/numba/codegen/complexsupport.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/codegen/globalconstants.py` & `numba-0.9.0/numba/codegen/globalconstants.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/codegen/llvmwrapper.py` & `numba-0.9.0/numba/codegen/llvmwrapper.py`

 * *Files 0% similar despite different names*

```diff
@@ -35,18 +35,18 @@
          const char  *ml_name;   /* The name of the built-in function/method */
          PyCFunction  ml_meth;   /* The C function that implements it */
          int      ml_flags;      /* Combination of METH_xxx flags, which mostly
                                     describe the args expected by the C func */
          const char  *ml_doc;    /* The __doc__ attribute, or NULL */
     };
     """
-    PyMethodDef = struct([('name', c_string_type),
+    PyMethodDef = struct([('name',   char.pointer()),
                           ('method', void.pointer()),
-                          ('flags', int_),
-                          ('doc', c_string_type)])
+                          ('flags',  int_),
+                          ('doc',    char.pointer())])
     c_PyMethodDef = PyMethodDef.to_ctypes()
 
     PyCFunction_NewEx = ctypes.pythonapi.PyCFunction_NewEx
     PyCFunction_NewEx.argtypes = [ctypes.POINTER(c_PyMethodDef),
                                   ctypes.py_object,
                                   ctypes.c_void_p]
     PyCFunction_NewEx.restype = ctypes.py_object
```

### Comparing `numba-0.8.1/numba/codegen/codeutils.py` & `numba-0.9.0/numba/codegen/codeutils.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/codegen/translate.py` & `numba-0.9.0/numba/codegen/translate.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 
 import llvm
 import llvm.core as lc
 import llvm.core
 
 from numba.llvm_types import _int1, _int32, _LLVMCaster
 from numba.multiarray_api import MultiarrayAPI # not used
+from numba.typesystem import llvmtypes
 from numba import typesystem
 
 from numba import *
 
 from numba.codegen import debug
 from numba.codegen.debug import logger
 from numba.codegen.codeutils import llvm_alloca
@@ -23,14 +24,15 @@
 from numba import ndarray_helpers, error
 from numba.typesystem import is_obj
 from numba.utils import dump
 from numba import metadata
 from numba.control_flow import ssa
 from numba.support.numpy_support import sliceutils
 from numba.nodes import constnodes
+from numba.typesystem import llvm_typesystem as lts
 
 from llvm_cbuilder import shortnames as C
 
 
 _int32_zero = lc.Constant.int(_int32, 0)
 
 
@@ -430,16 +432,18 @@
                                                'puts',
                                                args=[const]))
 
     def setup_return(self):
         # Assign to this value which will be returned
         self.is_void_return = \
                 self.func_signature.actual_signature.return_type.is_void
-        if self.func_signature.struct_by_reference:
+        ret_by_ref = minitypes.pass_by_ref(self.func_signature.return_type)
+        if self.func_signature.struct_by_reference and ret_by_ref:
             self.return_value = self.lfunc.args[-1]
+            assert self.return_value.type.kind == llvm.core.TYPE_POINTER
         elif not self.is_void_return:
             llvm_ret_type = self.func_signature.return_type.to_llvm(self.context)
             self.return_value = self.builder.alloca(llvm_ret_type,
                                                     "return_value")
 
         # All non-NULL object emporaries are DECREFed here
         self.cleanup_label = self.append_basic_block('cleanup_label')
@@ -570,14 +574,15 @@
         instr = self.builder.store(lvalue, ltarget)
 
         # Set TBAA on store instruction
         if tbaa_node is None:
             assert tbaa_type is not None
             tbaa_node = self.tbaa.get_metadata(tbaa_type)
 
+        assert tbaa_node
         self.tbaa.set_metadata(instr, tbaa_node)
 
     def preload_attributes(self, var, value):
         """
         Pre-load ndarray attributes data/shape/strides.
         """
         if not (var.preload_data or var.preload_shape or var.preload_strides):
@@ -907,15 +912,15 @@
 
     #------------------------------------------------------------------------
     # Indexing
     #------------------------------------------------------------------------
 
     def visit_Subscript(self, node):
         value_type = node.value.type
-        if not (value_type.is_carray or value_type.is_c_string or
+        if not (value_type.is_carray or value_type.is_string or
                     value_type.is_pointer):
             raise error.InternalError(node, "Unsupported type:", node.value.type)
 
         value = self.visit(node.value)
         index = self.visit(node.slice)
         indices = [index]
 
@@ -1004,15 +1009,15 @@
 
     def visit_UnaryOp(self, node):
         operand_type = node.operand.type
         operand = self.visit(node.operand)
         operand_ltype = operand.type
         op = node.op
         if isinstance(op, ast.Not) and (operand_type.is_bool or
-                                        operand_type.is_int_like):
+                                        operand_type.is_int):
             bb_false = self.builder.basic_block
             bb_true = self.append_basic_block('not.true')
             bb_done = self.append_basic_block('not.done')
             self.builder.cbranch(
                 self.builder.icmp(lc.ICMP_NE, operand,
                                   lc.Constant.null(operand_ltype)),
                 bb_true, bb_done)
@@ -1023,20 +1028,20 @@
             phi.add_incoming(lc.Constant.int(operand_ltype, 1), bb_false)
             phi.add_incoming(lc.Constant.int(operand_ltype, 0), bb_true)
             return phi
         elif isinstance(op, ast.USub) and operand_type.is_numeric:
             if operand_type.is_float:
                 return self.builder.fsub(lc.Constant.null(operand_ltype),
                                          operand)
-            elif operand_type.is_int_like and operand_type.signed:
+            elif operand_type.is_int and operand_type.signed:
                 return self.builder.sub(lc.Constant.null(operand_ltype),
                                         operand)
         elif isinstance(op, ast.UAdd) and operand_type.is_numeric:
             return operand
-        elif isinstance(op, ast.Invert) and operand_type.is_int_like:
+        elif isinstance(op, ast.Invert) and operand_type.is_int:
             return self.builder.xor(lc.Constant.int(operand_ltype, -1), operand)
         raise error.NumbaError(node, "Unary operator %s" % node.op)
 
     # ____________________________________________________________
     # Compare
 
     def visit_Compare(self, node):
@@ -1242,15 +1247,14 @@
         _, pyobject_call = self.context.external_library.declare(
                                         self.llvm_module, 'PyObject_Call')
 
         res = self.builder.call(pyobject_call, largs, name=node.name)
         return self.caster.cast(res, node.variable.type.to_llvm(self.context))
 
     def visit_NativeCallNode(self, node, largs=None):
-        # print node.py_func, node.llvm_func
         if largs is None:
             largs = self.visitlist(node.args)
 
         return_value = llvm_codegen.handle_struct_passing(
                             self.builder, self.alloca, largs, node.signature)
 
         if hasattr(node.llvm_func, 'module') and node.llvm_func.module != self.llvm_module:
@@ -1296,19 +1300,26 @@
             ltypes = []
         node.llvm_func = llvm.core.Function.intrinsic(self.llvm_module,
                                                       intr,
                                                       ltypes)
         return self.visit_NativeCallNode(node, largs=largs)
 
     def visit_MathCallNode(self, node):
-        lfunc_type = node.signature.to_llvm(self.context)
-        lfunc = self.llvm_module.get_or_insert_function(lfunc_type, node.name)
+        # Make sure we don't pass anything by reference
+        resty = node.signature.return_type.to_llvm()
+        argtys = [a.to_llvm() for a in node.signature.args]
+        lfunc_type = llvmtypes.function(resty, argtys)
+
+        type_namespace = map(str, argtys)
+        lfunc = self.llvm_module.get_or_insert_function(
+            lfunc_type, 'numba.math.%s.%s' % (type_namespace, node.name))
 
         node.llvm_func = lfunc
-        return self.visit_NativeCallNode(node)
+        largs = self.visitlist(node.args)
+        return self.builder.call(lfunc, largs)
 
     def visit_IntrinsicNode(self, node):
         args = self.visitlist(node.args)
         return node.intrinsic.emit_code(self.lfunc, self.builder, args)
 
     def visit_PointerCallNode(self, node):
         node.llvm_func = self.visit(node.function)
@@ -1384,14 +1395,15 @@
             "code for complex conjugates.")
 
         return self.builder.insert_value(lcomplex, new_imag_lval, 1)
 
     def visit_ComplexAttributeNode(self, node):
         result = self.visit(node.value)
         if node.value.type.is_complex:
+            assert result.type.kind == llvm.core.TYPE_STRUCT, result.type
             if node.attr == 'real':
                 return self.builder.extract_value(result, 0)
             elif node.attr == 'imag':
                 return self.builder.extract_value(result, 1)
 
     #------------------------------------------------------------------------
     # Structs
@@ -1570,24 +1582,25 @@
             self.llvm_module)
         return func_def
 
     def visit_NativeSliceNode(self, node):
         """
         Slice an array. Allocate fake PyArray and allocate shape/strides
         """
-        shape_ltype = npy_intp.pointer().to_llvm(self.context)
+        llvmtype = lambda t: t.to_llvm()
+        shape_ltype = llvmtype(npy_intp.pointer())
 
         # Create PyArrayObject accessors
         view = self.visit(node.value)
         view_accessor = ndarray_helpers.PyArrayAccessor(self.builder, view)
 
         # TODO: change this attribute name to stack_allocate or something
         if node.nopython:
             # Stack-allocate array object
-            array_struct_ltype = float_[:].to_llvm(self.context).pointee
+            array_struct_ltype = llvmtype(float_[:]).pointee
             view_copy = self.llvm_alloca(array_struct_ltype)
             array_struct = self.builder.load(view)
             self.builder.store(array_struct, view_copy)
             view_copy_accessor = ndarray_helpers.PyArrayAccessor(self.builder,
                                                                  view_copy)
         else:
             class NonMutatingPyArrayAccessor(object):
@@ -1734,24 +1747,24 @@
         elif type.is_float:
             lvalue = llvm.core.Constant.real(ltype, constant)
         elif type.is_int:
             if type.signed:
                 lvalue = llvm.core.Constant.int_signextend(ltype, constant)
             else:
                 lvalue = llvm.core.Constant.int(ltype, constant)
-        elif type.is_c_string:
+        elif type.is_string:
             lvalue = self.env.constants_manager.get_string_constant(constant)
-            type_char_p = typesystem.c_string_type.to_llvm(self.context)
+            type_char_p = lts.pointer(lts.char)
             lvalue = self.builder.bitcast(lvalue, type_char_p)
         elif type.is_bool:
             return self._bool_constants[constant]
         elif type.is_function:
             # lvalue = map_to_function(constant, type, self.mod)
             raise NotImplementedError
-        elif type.is_object and not constnodes.is_null_constant(pyval):
+        elif type.is_object and not constnodes.is_null_constant(constant):
             raise NotImplementedError("Use ObjectInjectNode")
         else:
             raise NotImplementedError("Constant %s of type %s" %
                                                     (constant, type))
 
         return lvalue
```

### Comparing `numba-0.8.1/numba/astsix.py` & `numba-0.9.0/numba/astsix.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/functions.py` & `numba-0.9.0/numba/functions.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from __future__ import print_function, division, absolute_import
 import ast, inspect, os
 import logging
 import textwrap
 from collections import defaultdict
 
 from numba import *
-from numba.minivect import minitypes
+from numba import typesystem
 from numba import numbawrapper
 
 import llvm.core
 
 logger = logging.getLogger(__name__)
 
 try:
@@ -162,12 +162,12 @@
         compiled = (
             func_env.func_signature,
             func_env.lfunc,
             func_env.numba_wrapper_func,
         )
 
         # Sanity check
-        assert isinstance(func_env.func_signature, minitypes.FunctionType)
+        assert isinstance(func_env.func_signature, typesystem.function)
         assert isinstance(func_env.lfunc, llvm.core.Function)
 
         argtypes_flags = tuple(argtypes), None
         self.__compiled_funcs[func][argtypes_flags] = compiled
```

### Comparing `numba-0.8.1/numba/numbafunction.c` & `numba-0.9.0/numba/numbafunction.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/environment.py` & `numba-0.9.0/numba/environment.py`

 * *Files 6% similar despite different names*

```diff
@@ -7,16 +7,16 @@
 import pprint
 
 import llvm.core
 
 from numba import pipeline, naming, error, reporting, PY3
 from numba.control_flow.control_flow import ControlFlow
 from numba.utils import TypedProperty, WriteOnceTypedProperty, NumbaContext
-from numba.minivect.minitypes import FunctionType
 from numba import functions, symtab
+from numba.typesystem import TypeSystem, numba_typesystem, function
 from numba.utility.cbuilder import library
 from numba.nodes import metadata
 from numba.codegen import translate
 from numba.codegen import globalconstants
 
 from numba.intrinsic import default_intrinsic_library
 from numba.external import default_external_library
@@ -63,28 +63,26 @@
     'LateSpecializer',
     'ExtensionTypeLowerer',
     'SpecializeFunccalls',
     'SpecializeExceptions',
     'FixASTLocations',
     'cleanup_symtab',
     'CodeGen',
+    'PostPass',
     'LinkingStage',
     'WrapperStage',
     'ErrorReporting',
 ]
 
 default_type_infer_pipeline_order = [
     'ast3to2',
     'ControlFlowAnalysis',
     'TypeInfer',
 ]
 
-compile_idx = default_pipeline_order.index('TypeInfer') + 1
-default_compile_pipeline_order = default_pipeline_order[compile_idx:]
-
 default_dummy_type_infer_pipeline_order = [
     'ast3to2',
     'TypeInfer',
     'TypeSet',
 ]
 
 default_numba_lower_pipeline_order = [
@@ -98,14 +96,21 @@
 default_numba_wrapper_pipeline_order = default_numba_lower_pipeline_order
 
 default_numba_late_translate_pipeline_order = \
     default_numba_lower_pipeline_order + [
     'CodeGen',
 ]
 
+upto = lambda order, x: order[:order.index(x)+1]
+upfr = lambda order, x: order[order.index(x)+1:]
+
+default_compile_pipeline_order = upfr(default_pipeline_order, 'TypeInfer')
+default_codegen_pipeline = upto(default_pipeline_order, 'CodeGen')
+default_post_codegen_pipeline = upfr(default_pipeline_order, 'CodeGen')
+
 # ______________________________________________________________________
 # Convenience functions
 
 def insert_stage(pipeline_order, stage, after=None, before=None):
     if after is not None:
         idx = pipeline_order.index(after) + 1
     else:
@@ -139,15 +144,15 @@
     source = TypedProperty(
         list, #(str, unicode),
         "Function source code")
 
     enable_post_mortem = TypedProperty(
         bool,
         "Enable post-mortem debugging for the Numba compiler",
-        False|1
+        False,
     )
 
     collection = TypedProperty(
         reporting.MessageCollection,
         "Collection of error and warning messages")
 
     warning_styles = {
@@ -189,15 +194,15 @@
         object, 'Function (or similar) being translated.')
 
     ast = TypedProperty(
         ast_module.AST,
         'Abstract syntax tree for the function being translated.')
 
     func_signature = TypedProperty(
-        FunctionType,
+        function,
         'Type signature for the function being translated.')
 
     is_partial = TypedProperty(
         bool,
         "Whether this environment is a partially constructed environment",
         False)
 
@@ -265,18 +270,20 @@
     locals = TypedProperty(
         dict,
         'A map from local variable names to types.  Used to handle the locals '
         'keyword argument to the autojit decorator. '
         '({ "local_var_name" : local_var_type } for @autojit(locals=...))')
 
     template_signature = TypedProperty(
-        object, # FIXME
+        (function, NoneType),
         'Template signature for @autojit.  E.g. T(T[:, :]).  See '
         'numba.typesystem.templatetypes.')
 
+    typesystem = TypedProperty(TypeSystem, "Typesystem for this compilation")
+
     ast_metadata = TypedProperty(
         object,
         'Metadata for AST nodes of the function being compiled.')
 
     flow = TypedProperty(
         (NoneType, ControlFlow),
         "Control flow graph. See numba.control_flow.",
@@ -330,14 +337,19 @@
 
     warnstyle = TypedProperty(
         str if PY3 else basestring,
         'Warning style, currently available: simple, fancy',
         default='fancy'
     )
 
+    postpasses = TypedProperty(
+        dict,
+        "List of passes that should run on the final llvm ir before linking",
+    )
+
     kwargs = TypedProperty(
         dict,
         'Additional keyword arguments.  Deprecated, but kept for backward '
         'compatibility.')
 
     # ____________________________________________________________
     # Methods
@@ -351,14 +363,15 @@
              llvm_module=None, wrap=True, link=True,
              symtab=None,
              error_env=None, function_globals=None, locals=None,
              template_signature=None, cfg_transform=None,
              is_closure=False, closures=None, closure_scope=None,
              refcount_args=True,
              ast_metadata=None, warn=True, warnstyle='fancy',
+             typesystem=None, postpasses=None,
              **kws):
 
         self.parent = parent
         self.numba = parent.numba
         self.func = func
         self.ast = ast
         self.func_signature = func_signature
@@ -401,14 +414,18 @@
         self.template_signature = template_signature
         self.cfg_transform = cfg_transform
         self.is_closure = is_closure
         self.closures = closures if closures is not None else {}
         self.closure_scope = closure_scope
 
         self.refcount_args = refcount_args
+        self.typesystem = typesystem or numba_typesystem
+
+        import numba.postpasses
+        self.postpasses = postpasses or numba.postpasses.default_postpasses
 
         if ast_metadata is not None:
             self.ast_metadata = ast_metadata
         else:
             self.ast_metadata = metadata.create_metadata_env()
 
         self.warn = warn
@@ -433,14 +450,15 @@
             template_signature=self.template_signature,
             cfg_transform=self.cfg_transform,
             is_closure=self.is_closure,
             closures=self.closures,
             closure_scope=self.closure_scope,
             warn=self.warn,
             warnstyle=self.warnstyle,
+            postpasses=self.postpasses,
         )
         return state
 
     def inherit(self, **kwds):
         """
         Inherit from a parent FunctionEnvironment (e.g. to run pipeline stages
         on a subset of the AST).
@@ -751,14 +769,18 @@
                 default_compile_pipeline_order),
             'wrap_func' : pipeline.ComposedPipelineStage(
                 default_numba_wrapper_pipeline_order),
             'lower' : pipeline.ComposedPipelineStage(
                 default_numba_lower_pipeline_order),
             'late_translate' : pipeline.ComposedPipelineStage(
                 default_numba_late_translate_pipeline_order),
+            'codegen' : pipeline.ComposedPipelineStage(
+                default_codegen_pipeline),
+            'post_codegen' : pipeline.ComposedPipelineStage(
+                default_post_codegen_pipeline),
             }
         self.context = NumbaContext()
         self.specializations = functions.FunctionCache(env=self)
         self.exports = PyccEnvironment()
         self.translation = self.TranslationEnvironment(self)
         self.debug = logger.getEffectiveLevel() < logging.DEBUG
```

### Comparing `numba-0.8.1/numba/tests/test_fbcorr.py` & `numba-0.9.0/numba/tests/test_fbcorr.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_reporting.py` & `numba-0.9.0/numba/tests/test_reporting.py`

 * *Files 26% similar despite different names*

```diff
@@ -12,57 +12,86 @@
     try:
         jit(void())(func)
     except error.NumbaError as e:
         print("exception: %s" % e)
 
 __doc__ = """
 >>> compile_func1()
+exception: (see below)
 --------------------- Numba Encountered Errors or Warnings ---------------------
     if x:
 -------^
-Error 6:7: No global named 'x'
+Error ...: No global named 'x'
 --------------------------------------------------------------------------------
-exception: 6:7: No global named 'x'
 """
 
 #@autojit
 def func2():
     print(10[20])
 
 def compile_func2():
     try:
         jit(void())(func2)
     except error.NumbaError as e:
         print("exception: %s" % e)
 
 __doc__ += """>>> compile_func2()
+exception: (see below)
 --------------------- Numba Encountered Errors or Warnings ---------------------
     print(10[20])
 ----------^
-Error 29:10: object of type int cannot be indexed
+Error ...: object of type int cannot be indexed
 --------------------------------------------------------------------------------
-exception: 29:10: object of type int cannot be indexed
 """
 
 @autojit # this often messes up line numbers
 def func_decorated():
     print(10[20])
 
 def compile_func3():
     try:
         func_decorated()
     except error.NumbaError as e:
         print("exception: %s" % e)
 
 __doc__ += """
 >>> compile_func3()
+exception: (see below)
 --------------------- Numba Encountered Errors or Warnings ---------------------
     print(10[20])
 ----------^
-Error 48:10: object of type int cannot be indexed
+Error ...: object of type int cannot be indexed
 --------------------------------------------------------------------------------
-exception: 48:10: object of type int cannot be indexed
+"""
+
+def warn_and_error(a, b):
+    print(a)
+    1[2]
+
+__doc__ += """
+>>> autojit(warn=False)(warn_and_error)(1, 2)
+Traceback (most recent call last):
+    ...
+NumbaError: (see below)
+--------------------- Numba Encountered Errors or Warnings ---------------------
+    1[2]
+----^
+Error 68:4: object of type int cannot be indexed
+<BLANKLINE>
+--------------------------------------------------------------------------------
+
+>>> autojit(warnstyle='simple')(warn_and_error)(1, 2)
+Traceback (most recent call last):
+    ...
+NumbaError: (see below)
+Error ...: object of type int cannot be indexed
+Warning ...: Unused argument 'b'
+
+>>> autojit(func_decorated.py_func, warnstyle='simple')()
+Traceback (most recent call last):
+    ...
+NumbaError: ...: object of type int cannot be indexed
 """
 
 if __name__ == '__main__':
     import numba
     numba.testing.testmod()
```

### Comparing `numba-0.8.1/numba/tests/test_object_conversion.py` & `numba-0.9.0/numba/tests/test_object_conversion.py`

 * *Files 9% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 See also numba.tests.test_overflow.
 """
 
 import ctypes
 import unittest
 
 import numpy as np
-from numba.minivect import minitypes
 from numba import *
 
 @autojit(backend='ast')
 def convert(obj_var, native_var):
     obj_var = native_var
     native_var = obj_var
     return native_var
@@ -66,20 +65,19 @@
             # print dst_type
             if dst_type.is_int:
                 expected = 2
             else:
                 expected = 2.5
 
             result = convert_numeric(value, dst_type)
-            assert result == expected, (result, dst_type)
+            assert result == expected, (result, expected, dst_type)
 
     def test_pointer_conversion(self):
         type = double.pointer()
         array = np.arange(10, dtype=np.double)
         # p = array.ctypes.data_as(type.to_ctypes())
         result = convert_to_pointer(array)
         assert ctypes.cast(result, ctypes.c_void_p).value == array.ctypes.data
 
 if __name__ == "__main__":
-#    TestConversion("test_pointer_conversion").test_pointer_conversion()
     from numba.testing import test_support
     test_support.main()
```

### Comparing `numba-0.8.1/numba/tests/math_tests/test_nopython_math.py` & `numba-0.9.0/numba/tests/math_tests/test_nopython_math.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/math_tests/test_math.py` & `numba-0.9.0/numba/tests/math_tests/test_math.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,13 +1,17 @@
-from numba import *
+# -*- coding: utf-8 -*-
+from __future__ import print_function, division, absolute_import
 
-import math
+from numba import *
 import numpy as np
 
-def a(dtype=np.double):
+# ______________________________________________________________________
+# NumPy
+
+def array_of_type(dtype=np.double):
     return np.arange(1, 10, dtype=dtype)
 
 def expected(a):
     return np.sum(np.log(a) * np.sqrt(a) - np.cos(a) * np.sin(a))
 
 def expected2(a):
     return np.sum(np.expm1(a) + np.ceil(a + 0.5) * np.rint(a + 1.5))
@@ -28,29 +32,35 @@
 
 dtypes = np.float32, np.float64 #, np.float128
 
 def test_numpy_math():
     for dtype in dtypes:
         print(dtype)
 
-        array = a(dtype)
+        array = array_of_type(dtype)
         result = numpy_math(array)
         assert np.allclose(result, expected(array)), (result, expected(array))
 
         result = numpy_math2(array)
         assert np.allclose(result, expected2(array))
 
+# ______________________________________________________________________
+# Pow
+
 @autojit(backend='ast')
 def power(x, y):
     return x ** y
 
 def test_power():
     assert power(5.0, 2.0) == 25.0
     assert power(5, 2) == 25
 
+# ______________________________________________________________________
+# Mod
+
 @autojit(backend='ast')
 def modulo(x, y):
     return x % y
 
 def test_modulo():
     for lsign in (1, -1):
         for rsign in (1, -1):
@@ -58,16 +68,11 @@
             float_rhs = rsign * 0.2
             assert np.allclose(modulo(float_lhs, float_rhs),
                                float_lhs % float_rhs)
             int_lhs = lsign * 5
             int_rhs = rsign * 2
             assert modulo(int_lhs, int_rhs) == (int_lhs % int_rhs)
 
-@autojit
-def sin(a):
-    return np.sin(a)
-
 if __name__ == "__main__":
-    # print sin(10)
    test_numpy_math()
    test_power()
    test_modulo()
```

### Comparing `numba-0.8.1/numba/tests/math_tests/test_numpy_math.py` & `numba-0.9.0/numba/tests/math_tests/test_numpy_math.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,7 @@
-import inspect
-
-from numba.minivect import minitypes
 from numba import error
 import numba
 from numba import *
 import numpy as np
 
 def get_functions():
     def sqrt(a, b):
@@ -61,15 +58,15 @@
 def test_math_funcs():
     functions = get_functions()
     exceptions = 0
     for func_name in functions:
         # func_name = 'sqrt'
         func = functions[func_name]
         for dest_type in dest_types:
-            signature = minitypes.FunctionType(None, [dest_type, dest_type])
+            signature = numba.function(None, [dest_type, dest_type])
             print(("executing...", func_name, signature))
 
             try:
                 numba_func = jit(signature)(func)
             except error.NumbaError as e:
                 exceptions += 1
                 print((func_name, dest_type, e))
```

### Comparing `numba-0.8.1/numba/tests/test_const_folding.py` & `numba-0.9.0/numba/tests/test_const_folding.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import unittest
 import ast, inspect
 import numpy as np
 from numba import utils, decorators, environment, pipeline
-from numba.minivect import minitypes
+from numba import typesystem
 from numba import *
 
 def cf_1():
     return 1 + 2
 
 def cf_2():
     return 1 + 2 - 3 * 4 / 5 // 6 ** 7
@@ -53,15 +53,15 @@
     return M + 2
 
 
 class TestConstFolding(unittest.TestCase):
     env = environment.NumbaEnvironment.get_environment()
 
     def run_pipeline(self, func):
-        func_sig = minitypes.FunctionType(minitypes.void, [])
+        func_sig = typesystem.function(typesystem.void, [])
         source = inspect.getsource(func)
         astree = ast.parse(source)
         with environment.TranslationContext(self.env, func, astree, func_sig):
             pipeline_callable = self.env.get_or_add_pipeline(
                 'const_folding', pipeline.ConstFolding)
             astree = pipeline.AST3to2()(astree, self.env)
             ret_val = pipeline_callable(astree, self.env)
```

### Comparing `numba-0.8.1/numba/tests/test_addressof.py` & `numba-0.9.0/numba/tests/test_addressof.py`

 * *Files 6% similar despite different names*

```diff
@@ -18,19 +18,19 @@
 
 @autojit
 def error_func():
     pass
 
 # TODO: struct pointer support
 
-before_computed_column = struct([
+before_computed_column = struct_([
     ('x', float32),
     ('y', float32)])
 
-with_computed_column = struct([
+with_computed_column = struct_([
     ('mean', float32),
     ('x', float32),
     ('y', float32)])
 
 signature = void(with_computed_column.ref(),
                  before_computed_column.ref())
```

### Comparing `numba-0.8.1/numba/tests/test_forces.py` & `numba-0.9.0/numba/tests/test_forces.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_117.py` & `numba-0.9.0/numba/tests/issues/test_issue_117.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_164.py` & `numba-0.9.0/numba/tests/issues/test_issue_164.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_118.py` & `numba-0.9.0/numba/tests/issues/test_issue_118.py`

 * *Files 8% similar despite different names*

```diff
@@ -16,12 +16,12 @@
     data = np.ones(10)
     lower_class_limits = np.empty((data.size + 1, n_classes + 1))
     #
     #        File "/Users/sklam/dev/numba/numba/type_inference/infer.py", line 1055, in visit_Subscript
     #    if slice_type.variable.type.is_unresolved:
     #        File "/Users/sklam/dev/numba/numba/minivect/minitypes.py", line 492, in __getattr__
     #            return getattr(type(self), attr)
-    #AttributeError: type object 'TupleType' has no attribute 'variable'
+    #AttributeError: type object 'tuple_' has no attribute 'variable'
     print((get_jenks_breaks(data, lower_class_limits, n_classes)))
 
 if __name__ == '__main__':
     test()
```

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_185.py` & `numba-0.9.0/numba/tests/issues/test_issue_185.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_compare.py` & `numba-0.9.0/numba/tests/issues/test_compare.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,17 @@
-from numba.minivect import minitypes
+import numba
 from numba import *
 
 tests = []
 
 def _make_test(f):
     def test():
         for argtype in [object_, float_, double]:
             # f_ = autojit(f)
-            f_ = jit(minitypes.FunctionType(None, [argtype]))(f)
+            f_ = jit(numba.function(None, [argtype]))(f)
             for v in range(-10,10):
                 assert f_(v)==f(v)
                 assert f_(float(v))==f(float(v))
 
     test.__name__ = f.__name__
     tests.append(test)
     return test
```

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_112.py` & `numba-0.9.0/numba/tests/issues/test_issue_112.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 
 import numpy as np
 
 from numba import autojit, register_callable, npy_intp, typesystem
 
-restype = typesystem.TupleType(npy_intp[:, :], 2)
+restype = typesystem.tuple_(npy_intp[:, :], 2)
 
 @register_callable(restype(npy_intp[:], npy_intp[:]))
 def meshgrid(x, y):
     return np.meshgrid(x, y)
 
 @autojit
 def run_meshgrid(size):
```

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_165.py` & `numba-0.9.0/numba/tests/issues/test_issue_165.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_125.py` & `numba-0.9.0/numba/tests/issues/test_issue_125.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_192.py` & `numba-0.9.0/numba/tests/issues/test_issue_192.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_57.py` & `numba-0.9.0/numba/tests/issues/test_issue_57.py`

 * *Files 6% similar despite different names*

```diff
@@ -49,15 +49,16 @@
 
 class TestIssue57(unittest.TestCase):
     def test_ra_numba(self):
         test_fn = jit('f4[:,:](i2,f4[:,:])')(ra_numba)
         lat = np.deg2rad(np.ones((5, 5), dtype=np.float32) * 45.)
         control_arr = ra_numpy(120, lat)
         test_arr = test_fn(120, lat)
-        self.assertTrue(np.allclose(test_arr, control_arr))
+        self.assertTrue(np.allclose(test_arr, control_arr),
+                        test_arr - control_arr)
 
 def benchmark(test_fn=None, control_fn=None):
     if test_fn is None:
         test_fn = jit('f4[:,:](i2,f4[:,:])')(ra_numba)
     if control_fn is None:
         control_fn = ra_numpy
     lat = np.deg2rad(np.ones((2000, 2000), dtype=np.float32) * 45.)
@@ -65,12 +66,12 @@
     control_arr = control_fn(120, lat)
     t1 = time.time()
     test_arr = test_fn(120, lat)
     t2 = time.time()
     dt0 = t1 - t0
     dt1 = t2 - t1
     logger.info('Control time %0.6fs, test time %0.6fs' % (dt0, dt1))
-    assert np.allclose(test_arr, control_arr)
+    assert np.allclose(test_arr, control_arr), (test_arr - control_arr)
     return dt0, dt1
 
 if __name__ == "__main__":
     test_support.main()
```

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_126.py` & `numba-0.9.0/numba/tests/issues/test_issue_126.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_138.py` & `numba-0.9.0/numba/tests/issues/test_issue_138.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_163.py` & `numba-0.9.0/numba/tests/issues/test_issue_163.py`

 * *Files 9% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 #fails too
 #array_nb = jit(b1[:](double[:]))(array)
 def test_valid_compare():
     array_nb = autojit(array)
     a = np.random.rand(1e6)
     assert np.allclose(array(a), array_nb(a))
 
-@autojit
+@autojit(warnstyle="simple")
 def invalid_compare(a):
     return 1 < a < 2
 
 
 if __name__ == '__main__':
     from numba.testing import test_support
     test_support.testmod()
```

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_56.py` & `numba-0.9.0/numba/tests/issues/test_issue_56.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/issues/test_issue_184.py` & `numba-0.9.0/numba/tests/issues/test_issue_184.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 
 import sys
 from numba import *
 import numpy as np
-
+import numba
 @jit(object_(double[:, :]))
 def func2(A):
     L = []
     n = A.shape[0]
+
     for i in range(10):
         for j in range(10):
             temp = A[i-n : i+n+1, j-2 : j+n+1]
             L.append(temp)
 
     return L
```

### Comparing `numba-0.8.1/numba/tests/closures/test_closure.py` & `numba-0.9.0/numba/tests/closures/test_closure.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,9 +1,13 @@
-import numba; from numba import *; from numba.error import NumbaError
-from numba.testing.test_support import rewrite_doc
+import numba
+from numba import *
+from numba.error import NumbaError
+
+autojit = autojit(warn=False, warnstyle='simple')
+
 @autojit
 def error1():
     def inner():
         pass
 
 @autojit
 def error2():
@@ -31,15 +35,15 @@
 def error5():
     @jit(restype=void, argtypes=[int_, int_, int_])
     def inner(a, b, c):
         print(str(a) + ' ' + str(b) + ' ' + str(c))
 
     inner(10, a=20, b=30)
 
-@autojit(warnstyle='simple')
+@autojit
 def closure1():
     a = 10
     @jit(restype=void, argtypes=[int_])
     def inner(arg):
         print(str(arg))
 
     return inner
@@ -95,36 +99,35 @@
 
     return c1, c3
 
 __doc__ = """
 >>> error1()
 Traceback (most recent call last):
     ...
-NumbaError: 5:4: Closure must be decorated with 'jit' or 'autojit'
+NumbaError: ...: Closure must be decorated with 'jit' or 'autojit'
 >>> error2()
 Traceback (most recent call last):
     ...
-NumbaError: 10:5: Dynamic closures not yet supported, use @jit
+NumbaError: ...: Dynamic closures not yet supported, use @jit
 >>> error3()
 Traceback (most recent call last):
     ...
-NumbaError: 16:4: local variable 'inner' referenced before assignment
+NumbaError: ...: local variable 'inner' referenced before assignment
 >>> error4()
 Traceback (most recent call last):
     ...
-NumbaError: 28:4: Expected 3 arguments, got 4
+NumbaError: ...: Expected 3 arguments, got 4
 >>> error5()
 Traceback (most recent call last):
     ...
 NumbaError: Got multiple values for positional argument 'a'
 
 Test closures
 
 >>> closure1().__name__
-Warning 40:4: Unused variable 'a'
 'inner'
 >>> closure1()()
 Traceback (most recent call last):
     ...
 TypeError: function takes exactly 1 argument (0 given)
 >>> closure1()(object())
 Traceback (most recent call last):
@@ -157,18 +160,14 @@
 'c2'
 >>> c1()()
 20 10
 >>> c3()
 21
 """
 
-
-
-
-
 @autojit
 def closure_arg(a):
     @jit('object_(object_)')
     def closure1(b):
         print(str(a) + ' ' + str(b))
         x = 10 + int_(b)
         @jit('object_(object_)')
@@ -262,39 +261,27 @@
     @jit('object_(object_)')
     def inner():
         return s.upper()
     return inner
 
 __doc__ += """
 >>> try_(wrong_signature, "foo")
---------------------- Numba Encountered Errors or Warnings ---------------------
-    @jit('object_(object_)')
------^
-Error 262:5: Expected 1 arguments type(s), got 0
---------------------------------------------------------------------------------
-NumbaError: 262:5: Expected 1 arguments type(s), got 0
+NumbaError: ...: Expected 1 arguments type(s), got 0
 """
 
-
-
 @autojit
 def wrong_restype():
     @jit('object_()')
     def inner():
         pass
     return inner
 
 __doc__ += """
 >>> try_(wrong_restype)
---------------------- Numba Encountered Errors or Warnings ---------------------
-    @jit('object_()')
-----^
-Error 281:4: Function with non-void return does not return a value
---------------------------------------------------------------------------------
-NumbaError: 281:4: Function with non-void return does not return a value
+NumbaError: ...: Function with non-void return does not return a value
 """
 
 #
 ### Test signatures like @double(object_)
 #
 @autojit
 def signature_dec():
@@ -313,20 +300,15 @@
     @object_(object_)
     def inner():
         return s.upper()
     return inner
 
 __doc__ += """
 >>> try_(wrong_signature2, "foo")
---------------------- Numba Encountered Errors or Warnings ---------------------
-    @object_(object_)
------^
-Error 313:5: Expected 1 arguments type(s), got 0
---------------------------------------------------------------------------------
-NumbaError: 313:5: Expected 1 arguments type(s), got 0
+NumbaError: ...: Expected 1 arguments type(s), got 0
 """
 
 @autojit
 def get_closure(arg):
     @void()
     def closure():
         print(arg)
@@ -383,15 +365,15 @@
         for i in range(cellvar):
             for j in range(cellvar):
                 if i == j:
                     print(str(i) + ' ' + str(cellvar))
 
     inner()
 
-@autojit(locals=dict(var=int_), warn=False)
+@numba.autojit(locals=dict(var=int_), warn=False)
 def test_closure_outer_locals():
     """
     >>> test_closure_outer_locals()
     """
     var = 10
     @jit(void())
     def inner():
```

### Comparing `numba-0.8.1/numba/tests/closures/test_closure_type_inference.py` & `numba-0.9.0/numba/tests/closures/test_closure_type_inference.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 """
 >>> from numba.tests.closures import test_closure_type_inference
 """
 
 import numpy as np
 
 from numba import *
-from numba.testing.test_support import *
+from numba import error
+from numba.testing.test_support import testmod
 
 @autojit
 def test_cellvar_promotion(a):
     """
     >>> inner = test_cellvar_promotion(10)
     200.0
     >>> inner.__name__
@@ -30,17 +31,17 @@
 
 @autojit
 def test_cellvar_promotion_error(a):
     """
     >>> from numba.minivect import minierror
     >>> try:
     ...     test_cellvar_promotion_error(10)
-    ... except minierror.UnpromotableTypeError as e:
+    ... except error.UnpromotableTypeError as e:
     ...     print(sorted(e.args, key=str))
-    [(int, const char *)]
+    [(int, string)]
     """
     b = int(a) * 2
 
     @jit(void())
     def inner():
         print((a * b))
```

### Comparing `numba-0.8.1/numba/tests/test_if.py` & `numba-0.9.0/numba/tests/test_if.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_forloop.py` & `numba-0.9.0/numba/tests/test_forloop.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_while.py` & `numba-0.9.0/numba/tests/test_while.py`

 * *Files 0% similar despite different names*

```diff
@@ -179,15 +179,15 @@
     def test_while_loop_fn_7(self, *args, **kws):
         return super(TestASTWhile, self).test_while_loop_fn_7(*args, **kws)
 
 
 # ______________________________________________________________________
 
 if __name__ == "__main__":
-#    TestASTWhile("test_while_loop_fn_8").debug()
+    TestASTWhile("test_while_loop_fn_8").debug()
 #    autojit(while_loop_fn_2)(numpy.array([1., 2., 3.]))
 #    jit(argtypes = [long_])(while_loop_fn_3)
 #    jit(argtypes = (long_, long_, long_),
 #        restype = long_)(while_loop_fn_4)
 #    jit(argtypes = [double, double])(while_loop_fn_5)
 #    jit(restype=double, argtypes=[double])(while_loop_fn_6)
 #    jit(restype=double, argtypes=[double])(while_loop_fn_7)
```

### Comparing `numba-0.8.1/numba/tests/test_extern_call.py` & `numba-0.9.0/numba/tests/test_extern_call.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_strings.py` & `numba-0.9.0/numba/tests/test_strings.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_print_function.py` & `numba-0.9.0/numba/tests/test_print_function.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 from __future__ import print_function
 
 import sys
 import unittest
 import StringIO
 
-from numba.minivect import minitypes
 from numba import *
 
 @autojit(backend='ast')
 def print_(value):
     print(value)
 
 @autojit(backend='ast', nopython=True)
@@ -51,9 +50,9 @@
         assert data == "14.1 ", repr(data)
 
 if __name__ == "__main__":
     # The following isn't currently supported.  See issue #147
     #(https://github.com/numba/numba/issues/147).
 
     #print_nopython(10)
-
+    TestPrint('test_print_stream').debug()
     unittest.main()
```

### Comparing `numba-0.8.1/numba/tests/test_redefine.py` & `numba-0.9.0/numba/tests/test_redefine.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/np/test_numpy_type_inference.py` & `numba-0.9.0/numba/tests/np/test_numpy_type_inference.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import numpy as np
 
 import numba
 from numba import *
 from numba import typesystem
-
-tup_t = typesystem.TupleType
+from numba.typesystem import tuple_
 
 #------------------------------------------------------------------------
 # Test functions
 #------------------------------------------------------------------------
 
 @autojit
 def array(value):
@@ -80,34 +79,33 @@
     return numba.typeof(np.sum(a, out=out))
 
 #------------------------------------------------------------------------
 # Tests
 #------------------------------------------------------------------------
 
 def equals(a, b):
-    assert a == b, (a, b, type(a), type(b),
-                    a.comparison_type_list, b.comparison_type_list)
+    assert a == b, (a, b, type(a), type(b))
 
 def test_array():
     equals(array(np.array([1, 2, 3], dtype=np.double)), float64[:])
     equals(array(np.array([[1, 2, 3]], dtype=np.int32)), int32[:, :])
     equals(array(np.array([[1, 2, 3],
                            [4, 5, 6]], dtype=np.int32).T), int32[:, :])
 
 def test_nonzero():
     equals(nonzero(np.array([1, 2, 3], dtype=np.double)),
-           tup_t(npy_intp[:], 1))
+           tuple_(npy_intp[:], 1))
     equals(nonzero(np.array([[1, 2, 3]], dtype=np.double)),
-           tup_t(npy_intp[:], 2))
+           tuple_(npy_intp[:], 2))
     equals(nonzero(np.array((((1, 2, 3),),), dtype=np.double)),
-           tup_t(npy_intp[:], 3))
+           tuple_(npy_intp[:], 3))
 
 def test_where():
     equals(where(np.array([1, 2, 3], dtype=np.double)),
-           tup_t(npy_intp[:], 1))
+           tuple_(npy_intp[:], 1))
 
     equals(where3(np.array([True, False, True]),
                   np.array([1, 2, 3], dtype=np.double),
                   np.array([1, 2, 3], dtype=np.complex128)),
            complex128[:])
 
     equals(where3(np.array([True, False, True]),
@@ -133,15 +131,15 @@
 
             result_type, result = numba_dot(x, y)
 
             assert result == np.dot(x, y)
             if i + j - 2 > 0:
                 assert result.ndim == result_type.ndim
             else:
-                assert result_type == dtype
+                assert result_type == dtype, (result_type, dtype)
 
 def test_numba_vdot():
     for a, b in ((np.array([1+2j,3+4j]),
                   np.array([5+6j,7+8j])),
                  (np.array([[1, 4], [5, 6]]),
                   np.array([[4, 1], [2, 2]]))):
         result_type, result = numba_vdot(a, b)
```

### Comparing `numba-0.8.1/numba/tests/np/test_ufunc_type_inference.py` & `numba-0.9.0/numba/tests/np/test_ufunc_type_inference.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import numpy as np
 
 import numba
 from numba import *
 from numba import typesystem
 
-tup_t = typesystem.TupleType
+tup_t = typesystem.tuple_
 
 #------------------------------------------------------------------------
 # Test data
 #------------------------------------------------------------------------
 
 a = np.array([1, 2, 3], dtype=np.int32)
 b = np.array([[1, 2], [3, 4]], dtype=np.int64)
@@ -64,16 +64,15 @@
     return numba.typeof(ufunc.outer(a, a))
 
 #------------------------------------------------------------------------
 # Tests
 #------------------------------------------------------------------------
 
 def equals(a, b):
-    assert a == b, (a, b, type(a), type(b),
-                    a.comparison_type_list, b.comparison_type_list)
+    assert a == b, (a, b, type(a), type(b))
 
 def test_binary_ufunc():
     equals(binary_ufunc(np.add, a, b), int64[:, :])
     equals(binary_ufunc(np.subtract, a, b), int64[:, :])
     equals(binary_ufunc(np.multiply, a, b), int64[:, :])
     equals(binary_ufunc(np.true_divide, a, b), int64[:, :])
     equals(binary_ufunc(np.floor_divide, a, b), int64[:, :])
```

### Comparing `numba-0.8.1/numba/tests/np/test_numpy_calls.py` & `numba-0.9.0/numba/tests/np/test_numpy_calls.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/np/test_preloading.py` & `numba-0.9.0/numba/tests/np/test_preloading.py`

 * *Files 1% similar despite different names*

```diff
@@ -59,12 +59,12 @@
         # A_3 = phi(A_1, A_2)       # <- preload
         sum += A[i]
 
 
     return sum
 
 if __name__ == "__main__":
-#    a = np.arange(10, dtype=np.double)
-#    preload_arg(a)
-#    preload_phi(a)
-    import numba
-    numba.testing.testmod()
+   a = np.arange(10, dtype=np.double)
+   preload_arg(a)
+   preload_phi(a)
+    # import numba
+    # numba.testing.testmod()
```

### Comparing `numba-0.8.1/numba/tests/pointers/test_pointers.py` & `numba-0.9.0/numba/tests/pointers/test_pointers.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/pointers/test_null.py` & `numba-0.9.0/numba/tests/pointers/test_null.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_cstring.py` & `numba-0.9.0/numba/tests/test_cstring.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #! /usr/bin/env python
 # ______________________________________________________________________
 
 from numba import *
-from numba import c_string_type as cstring, int_
+from numba import string_ as cstring, int_
 
 from nose.tools import nottest
 from numba.testing import test_support
 
 # ______________________________________________________________________
 
 def convert(input_str):
```

### Comparing `numba-0.8.1/numba/tests/test_casting.py` & `numba-0.9.0/numba/typesystem/tests/test_casting.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_sum.py` & `numba-0.9.0/numba/tests/test_sum.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_multiarray_api.py` & `numba-0.9.0/numba/tests/test_multiarray_api.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_indexing.py` & `numba-0.9.0/numba/tests/test_indexing.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_struct.py` & `numba-0.9.0/numba/tests/test_struct.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 
 import numpy as np
 
 #------------------------------------------------------------------------
 # Structs as locals
 #------------------------------------------------------------------------
 
-struct_type = struct(a=char.pointer(), b=int_)
+struct_type = struct_([('a', char.pointer()), ('b', int_)])
 
 @autojit(backend='ast', locals=dict(value=struct_type))
 def struct_local():
     value.a = "foo"
     value.b = 10
     return value.a, value.b
 
@@ -80,27 +80,27 @@
 
 @autojit(backend='ast')
 def record_array(array):
     array[0].a = 4
     array[0].b = 5.0
 
 def test_record_array():
-    struct_type = struct([('a', int32), ('b', double)])
+    struct_type = struct_([('a', int32), ('b', double)])
     struct_dtype = struct_type.get_dtype()
 
     array = np.empty((1,), dtype=struct_dtype)
     record_array(array)
     assert array[0]['a'] == 4, array[0]
     assert array[0]['b'] == 5.0, array[0]
 
 #------------------------------------------------------------------------
 # Object Coercion
 #------------------------------------------------------------------------
 
-struct_type = struct([('a', int_), ('b', double)])
+struct_type = struct_([('a', int_), ('b', double)])
 
 @autojit(backend='ast', locals=dict(value=struct_type))
 def coerce_to_obj():
     value.a = 10
     value.b = 20.2
     return object_(value)
```

### Comparing `numba-0.8.1/numba/tests/test_ast_arrays.py` & `numba-0.9.0/numba/tests/test_ast_arrays.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_recursion.py` & `numba-0.9.0/numba/tests/test_recursion.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/ops/test_bitwise_ops.py` & `numba-0.9.0/numba/tests/ops/test_bitwise_ops.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import sys
-
 import numba
-
 from numba.testing.test_support import autojit_py3doc
 # NOTE: See also issues/test_issue_56
 
+autojit_py3doc = autojit_py3doc(warn=False, warnstyle='simple')
+
 @autojit_py3doc
 def test_bitwise_and(a, b):
     """
     >>> test_bitwise_and(0b01, 0b10)
     0L
     >>> test_bitwise_and(0b01, 0b11)
     1L
```

### Comparing `numba-0.8.1/numba/tests/ops/test_unary_ops.py` & `numba-0.9.0/numba/tests/ops/test_unary_ops.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/ops/test_binary_ops.py` & `numba-0.9.0/numba/tests/ops/test_binary_ops.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_ast_forloop.py` & `numba-0.9.0/numba/tests/test_ast_forloop.py`

 * *Files 5% similar despite different names*

```diff
@@ -2,25 +2,17 @@
 # ______________________________________________________________________
 '''test_forloop
 
 Test the Numba compiler on a simple for loop over an iterable object.
 '''
 # ______________________________________________________________________
 
-import numba
-from numba import *
-from numba.decorators import autojit
-
-from numba.minivect import minitypes
-hash(minitypes.double[:])
-
-import numpy
-import numpy as np
-
 import unittest
+from numba import autojit
+import numpy as np
 
 # ______________________________________________________________________
 
 def _for_loop_fn_0 (iterable):
     acc = 0.
     for value in iterable:
         acc += value
```

### Comparing `numba-0.8.1/numba/tests/test_unsigned_arith.py` & `numba-0.9.0/numba/tests/test_unsigned_arith.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_ast_getattr.py` & `numba-0.9.0/numba/tests/test_ast_getattr.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_avg2d.py` & `numba-0.9.0/numba/tests/test_avg2d.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_mandelbrot.py` & `numba-0.9.0/numba/tests/test_mandelbrot.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_dot.py` & `numba-0.9.0/numba/tests/test_dot.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_array_math.py` & `numba-0.9.0/numba/tests/array_exprs/test_array_math.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_slicing2.py` & `numba-0.9.0/numba/tests/array_exprs/test_slicing2.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_vmdot.py` & `numba-0.9.0/numba/tests/array_exprs/test_vmdot.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_array_expressions.py` & `numba-0.9.0/numba/tests/array_exprs/test_array_expressions.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_broadcasting.py` & `numba-0.9.0/numba/tests/array_exprs/test_broadcasting.py`

 * *Files 3% similar despite different names*

```diff
@@ -114,15 +114,15 @@
 def test_shape_mismatch():
     """
     >>> a, b = operands(np.double)
 
     >>> shape_mismatch(a[:2], b)
     Traceback (most recent call last):
         ...
-    ValueError: Shape mismatch while broadcasting
+    ValueError: ...
 
     # This will abort, so don't run it :)
     >> shape_mismatch_nopython(a[:2], b)
     ValueError: Shape mismatch while broadcasting
     """
 
 if __name__ == "__main__":
```

### Comparing `numba-0.8.1/numba/tests/array_exprs/test_slicing.py` & `numba-0.9.0/numba/tests/array_exprs/test_slicing.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/broken_issues/autojit_ext_method_call.py` & `numba-0.9.0/numba/tests/broken_issues/autojit_ext_method_call.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/broken_issues/test_binary_harder.py` & `numba-0.9.0/numba/tests/broken_issues/test_binary_harder.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/broken_issues/test_bitwise_harder.py` & `numba-0.9.0/numba/tests/broken_issues/test_bitwise_harder.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_object_literals.py` & `numba-0.9.0/numba/tests/test_object_literals.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/builtins/test_object_builtins.py` & `numba-0.9.0/numba/tests/builtins/test_object_builtins.py`

 * *Files 16% similar despite different names*

```diff
@@ -17,39 +17,42 @@
 True
 """
 
 from numba import *
 
 myglobal = 20
 
-@autojit(backend='ast')
+autojit = autojit(warn=False, warnstyle="simple")
+
+@autojit
 def get_globals():
     return globals()['myglobal']
 
-@autojit(backend='ast')
+@autojit
 def get_locals():
     x = 2
     return locals()['x']
 
-@autojit(backend='ast')
+@autojit
 def get_sum(x):
     return sum([1, 2, x])
 
-@autojit(backend='ast')
+@autojit
 def eval_something(s):
     return eval(s)
 
-@autojit(backend='ast')
+@autojit
 def enumerate_list():
     return enumerate([1, 2, 3])
 
-@autojit(backend='ast')
+@autojit
 def max_(x):
     return max(1, 2.0, x, 14)
 
-@autojit(backend='ast')
+@autojit
 def min_(x):
     return min(1, 2.0, x, 14)
 
 if __name__ == '__main__':
+    get_globals()
     import numba
     numba.testing.testmod()
```

### Comparing `numba-0.8.1/numba/tests/builtins/test_builtin_range.py` & `numba-0.9.0/numba/tests/builtins/test_builtin_range.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/builtins/test_builtin_round.py` & `numba-0.9.0/numba/tests/builtins/test_builtin_round.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/builtins/test_builtin_abs.py` & `numba-0.9.0/numba/tests/builtins/test_builtin_abs.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_typeof.py` & `numba-0.9.0/numba/typesystem/tests/test_typeof.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,17 +9,17 @@
         self.arg = double(arg)
 
 def test_typeof_pure(arg):
     """
     >>> test_typeof_pure(10)
     int
     >>> test_typeof_pure(10.0)
-    double
+    float64
     >>> print(test_typeof_pure(Foo(10)))
-    <JitExtension Foo({'arg': double})>
+    <JitExtension Foo({'arg': float64})>
     """
     return numba.typeof(arg)
 
 @autojit_py3doc
 def test_typeof_numba(a, b):
     """
     >>> test_typeof_numba(10, 11.0)
@@ -43,12 +43,20 @@
 
 @autojit
 def test_typeof_numba3(arg):
     """
     >>> print(test_typeof_numba3(10))
     int
     >>> print(test_typeof_numba3(Foo(10)))
-    <JitExtension Foo({'arg': double})>
+    <JitExtension Foo({'arg': float64})>
+    """
+    return numba.typeof(arg)
+
+@autojit
+def test_typeof_type(arg):
+    """
+    >>> test_typeof_type(int_)
+    meta(int)
     """
     return numba.typeof(arg)
 
 numba.testing.testmod()
```

### Comparing `numba-0.8.1/numba/tests/foreign_call/test_cffi_call.py` & `numba-0.9.0/numba/tests/foreign_call/test_cffi_call.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/foreign_call/test_callbacks.py` & `numba-0.9.0/numba/tests/foreign_call/test_callbacks.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/foreign_call/test_ctypes_call.py` & `numba-0.9.0/numba/tests/foreign_call/test_ctypes_call.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_for_in_range.py` & `numba-0.9.0/numba/tests/test_for_in_range.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_listcomp.py` & `numba-0.9.0/numba/tests/test_listcomp.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,21 +10,21 @@
     ([0L, 4L, 8L], 4L)
     """
     x = -10 # 'abc'
     result = [x*2 for x in range(5) if x % 2 == 0]
     # assert x != -10 # 'abc'
     return result, x
 
-@autojit_py3doc
+@autojit_py3doc(warnstyle="simple")
 def list_genexp():
     """
     >>> list_genexp()
     Traceback (most recent call last):
         ...
-    NumbaError: 26:18: Generator comprehensions are not yet supported
+    NumbaError: ...: Generator comprehensions are not yet supported
     """
     x = -10 # 'abc'
     result = list(x*2 for x in range(5) if x % 2 == 0)
     # assert x == 'abc'
     return result, x
 
 @autojit_py3doc(locals={"x": int_})
```

### Comparing `numba-0.8.1/numba/tests/test_globals_builtins.py` & `numba-0.9.0/numba/tests/test_globals_builtins.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 import unittest
 
-from numba.minivect import minitypes
 from numba import *
 
 some_global = "hello"
 
 @autojit(backend='ast')
 def access_global():
     return some_global
```

### Comparing `numba-0.8.1/numba/tests/test_mandelbrot_2.py` & `numba-0.9.0/numba/tests/test_mandelbrot_2.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_filter2d.py` & `numba-0.9.0/numba/tests/test_filter2d.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_types.py` & `numba-0.9.0/numba/tests/test_types.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_template_types.py` & `numba-0.9.0/numba/typesystem/tests/test_template_types.py`

 * *Files 16% similar despite different names*

```diff
@@ -21,30 +21,30 @@
 
     >>> test_simple_template(np.arange(10, 12, dtype=np.float32).reshape(2, 1))
     10.0
 
     #------------------------------------------------------------------------
     # Test type resolving
     #------------------------------------------------------------------------
-    >>> infer(test_simple_template.py_func, double(double[:, :]), T(T[:, :]),
+    >>> infer(test_simple_template.py_func, float64(float64[:, :]), T(T[:, :]),
     ...       locals=dict(scalar=T))
-    [('array', double[:, :]), ('scalar', double)]
+    [('array', float64[:, :]), ('scalar', float64)]
 
-    >>> infer(test_simple_template.py_func, double(double[:, :]), T(T[:, :]),
+    >>> infer(test_simple_template.py_func, float64(float64[:, :]), T(T[:, :]),
     ...       locals=dict(scalar=T.pointer()))
     Traceback (most recent call last):
         ...
-    UnpromotableTypeError: (double *, double)
+    UnpromotableTypeError: Cannot promote types float64 * and float64
 
     #------------------------------------------------------------------------
     # Test type attributes
     #------------------------------------------------------------------------
-    >>> infer(test_simple_template.py_func, double(double[:, :]), T.dtype(T),
+    >>> infer(test_simple_template.py_func, float64(float64[:, :]), T.dtype(T),
     ...       locals=dict(scalar=T.dtype))
-    [('array', double[:, :]), ('scalar', double)]
+    [('array', float64[:, :]), ('scalar', float64)]
     """
     scalar = array[0, 0]
     return scalar
 
 #------------------------------------------------------------------------
 # Test type matching
 #------------------------------------------------------------------------
@@ -52,61 +52,61 @@
 T1 = numba.template("T1")
 T2 = numba.template("T2")
 T3 = numba.template("T3")
 T4 = numba.template("T4")
 
 A = T1[:, :]
 F = void(T1)
-S = numba.struct(a=T1, b=T2.pointer(), c=T3[:], d=void(T4))
+S = numba.struct([('a', T1), ('b', T2.pointer()), ('c', T3[:]), ('d', void(T4))])
 P = T2.pointer()
 
-type_context1 = { T1: int_, T2: float_, T3: double, T4: short, }
-type_context2 = { T1: int_[:, :], T2: void(float_),
-                  T3: numba.struct(a=double, b=float_), T4: short.pointer(), }
+type_context1 = { T1: int_, T2: float_, T3: float64, T4: short, }
+type_context2 = { T1: int_[:, :], T2: void(float32),
+                  T3: numba.struct(a=float64, b=float_), T4: short.pointer(), }
 
 def test_type_matching(array, func, struct, pointer):
     """
     >>> infer(test_type_matching, template_signature=void(A, F, S, P),
     ...       type_context=type_context1)
-    [('array', int[:, :]), ('func', void (*)(int)), ('pointer', float *), ('struct', struct { float * b, double[:] c, int a, void (*)(short) d })]
+    [('array', int[:, :]), ('func', void (*)(int)), ('pointer', float32 *), ('struct', struct { int a, float32 * b, float64[:] c, void (*)(short) d })]
     """
     func(array[0, 0])
     struct.b = pointer
 
 def test_type_attributes(array, func, struct, pointer):
     """
     >>> locals = dict(dtype=T1.dtype, arg=T2.args[0], field_a=T3.fielddict['a'],
     ...               field_b=T3.fielddict['b'], scalar=T4.base_type)
     >>> pprint(infer(test_type_attributes, template_signature=void(T1, T2, T3, T4),
     ...              type_context=type_context2, locals=locals))
     [('array', int[:, :]),
-     ('func', void (*)(float)),
+     ('func', void (*)(float32)),
      ('pointer', short *),
-     ('struct', struct { double a, float b }),
-     ('arg', float),
+     ('struct', struct { float64 a, float32 b }),
+     ('arg', float32),
      ('dtype', int),
-     ('field_a', double),
-     ('field_b', float),
+     ('field_a', float64),
+     ('field_b', float32),
      ('scalar', short)]
     """
     dtype = array[0, 0]
     arg = 0
     field_a = 0
     field_b = 0
     scalar = 0
 
-@autojit_py3doc(T(T, double), locals=None)
+@autojit_py3doc(T(T, float64), locals=None)
 def test_template_with_concretes(a, b):
     """
     >>> test_template_with_concretes(1, 2)
     3L
     """
     return a + b
 
-@autojit(complex128(T, double), locals=None)
+@autojit(complex128(T, float64), locals=None)
 def test_template_with_concretes2(a, b):
     """
     >>> test_template_with_concretes2(1, 2)
     (3+0j)
     >>> test_template_with_concretes2(1.0, 2.0)
     (3+0j)
     >>> test_template_with_concretes2(1+0j, 2)
@@ -116,15 +116,15 @@
     Traceback (most recent call last):
         ...
     TypeError: can't convert complex to float
     """
     return a + b
 
 
-@autojit_py3doc(T2(T1, double), locals=None)
+@autojit_py3doc(T2(T1, float64), locals=None)
 def test_unknown_template_error(a, b):
     """
     >>> test_unknown_template_error(1, 2)
     Traceback (most recent call last):
         ...
     InvalidTemplateError: Unknown template type: T2
     """
@@ -134,15 +134,15 @@
 def test_template_inconsistent_types_error(a, b):
     """
     >>> test_template_inconsistent_types_error(1, 2)
     3L
     >>> test_template_inconsistent_types_error(1, 2.0)
     Traceback (most recent call last):
         ...
-    InvalidTemplateError: Inconsistent types found for template: int and double
+    InvalidTemplateError: Inconsistent types found for template: int and float64
     """
     return a + b
 
 #------------------------------------------------------------------------
 # Test utilities
 #------------------------------------------------------------------------
 
@@ -168,8 +168,8 @@
     return vars + local_vars
 
 def specialize(T, context):
     return typesystem.resolve_template_type(T, context)
 
 
 if __name__ == '__main__':
-    testmod()
+    testmod()
```

### Comparing `numba-0.8.1/numba/tests/test_numbafunction.py` & `numba-0.9.0/numba/tests/test_numbafunction.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_complex.py` & `numba-0.9.0/numba/tests/math_tests/test_complex.py`

 * *Files 1% similar despite different names*

```diff
@@ -171,18 +171,18 @@
         if not numba.PY3:
             self.assertAlmostEqual(self.autojit(floordiv)(m, n), floordiv(m, n))
 
     def test_complex_math(self):
         self.assertAlmostEqual(self.autojit(sqrt)(m, n), sqrt(m, n))
         self.assertAlmostEqual(self.autojit(log)(m, n), log(m, n))
         self.assertAlmostEqual(self.autojit(log10)(m, n), log10(m, n))
-        self.assertAlmostEqual(self.autojit(exp)(m, n), exp(m, n))
+        self.assertAlmostEqual(self.autojit(exp)(m, n), exp(m, n), places=4)
         self.assertAlmostEqual(self.autojit(sin)(m, n), sin(m, n))
         self.assertAlmostEqual(self.autojit(cos)(m, n), cos(m, n))
-        self.assertAlmostEqual(self.autojit(cosh)(m, n), cosh(m, n))
+        self.assertAlmostEqual(self.autojit(cosh)(m, n), cosh(m, n), places=4)
         self.assertAlmostEqual(self.autojit(atan)(m, n), atan(m, n))
         self.assertAlmostEqual(self.autojit(asinh)(m, n), asinh(m, n))
         self.assertAlmostEqual(self.autojit(absolute)(m, n), absolute(m, n))
 
 
     def test_complex_math_float_input(self):
         m, n = .12, .32
@@ -201,14 +201,19 @@
     def test_mandel(self):
         self.assertEqual(self.autojit(mandel)(-1, -1, 20), 2)
         self.assertEqual(mandel(-1, -1, 20), 2)
 
 # ______________________________________________________________________
 
 if __name__ == "__main__":
-#    m, n = .12, .32
-#    print autojit(add)(m, n)
-#    print autojit(cosh)(m, n), cosh(m, n)
-    unittest.main()
+    # m, n = .12, .32
+    # print autojit(add)(m, n)
+    # print autojit(cosh)(m, n), cosh(m, n)
+    # print(autojit(sqrt)(m, n))
+    # num0 = 0 - 2j
+    # num1 = numpy.complex128(num0)
+    # compiled_get_imag_fn = jit(argtypes = [complex128])(get_imag_fn)
+    # compiled_get_imag_fn(num0)
+    unittest.main() #verbosity=3)
 
 # ______________________________________________________________________
 # End of test_complex.py
```

### Comparing `numba-0.8.1/numba/tests/test_exceptions.py` & `numba-0.9.0/numba/tests/test_exceptions.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_autojit.py` & `numba-0.9.0/numba/tests/test_autojit.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_modulo.py` & `numba-0.9.0/numba/tests/test_modulo.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_overflow.py` & `numba-0.9.0/numba/tests/test_overflow.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_getattr.py` & `numba-0.9.0/numba/tests/test_getattr.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_diffusion.py` & `numba-0.9.0/numba/tests/test_diffusion.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_object_counting.py` & `numba-0.9.0/numba/tests/test_object_counting.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/vectorize/test_usecase_1_1.py` & `numba-0.9.0/numba/vectorize/tests/test_usecase_1_1.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/vectorize/test_type_inference.py` & `numba-0.9.0/numba/vectorize/tests/test_type_inference.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/vectorize/test_basic_vectorize.py` & `numba-0.9.0/numba/vectorize/tests/test_basic_vectorize.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_ifexp.py` & `numba-0.9.0/numba/tests/test_ifexp.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_issues.py` & `numba-0.9.0/numba/tests/test_issues.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_slicing.py` & `numba-0.9.0/numba/tests/test_slicing.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_rshift.py` & `numba-0.9.0/numba/tests/test_rshift.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_withpython.py` & `numba-0.9.0/numba/tests/test_withpython.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/tests/test_tuple.py` & `numba-0.9.0/numba/tests/test_tuple.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/include/_numba.h` & `numba-0.9.0/numba/include/_numba.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/special.py` & `numba-0.9.0/numba/special.py`

 * *Files 11% similar despite different names*

```diff
@@ -47,23 +47,22 @@
     ctypes_sig = obj.signature.to_ctypes()
     return ctypes.cast(obj.lfunc_pointer, ctypes_sig)
 
 #------------------------------------------------------------------------
 # Types
 #------------------------------------------------------------------------
 
-def typeof(variable):
+def typeof(value):
     """
-    Get the type of a variable.
+    Get the type of a variable or value.
 
     Used outside of Numba code, infers the type for the object.
     """
-    from numba.environment import NumbaEnvironment
-    context = NumbaEnvironment.get_environment().context
-    return context.typemapper.from_python(variable)
+    from numba import typesystem
+    return typesystem.numba_typesystem.typeof(value)
 
 #------------------------------------------------------------------------
 # python/nopython context managers
 #------------------------------------------------------------------------
 
 class NoopContext(object):
```

### Comparing `numba-0.8.1/numba/utility/math_utilities.py` & `numba-0.9.0/numba/utility/math_utilities.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/utility/virtuallookup.py` & `numba-0.9.0/numba/utility/virtuallookup.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/utility/cbuilder/refcounting.py` & `numba-0.9.0/numba/utility/cbuilder/refcounting.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/utility/cbuilder/library.py` & `numba-0.9.0/numba/utility/cbuilder/library.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/utility/cbuilder/numbacdef.py` & `numba-0.9.0/numba/utility/cbuilder/numbacdef.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/ast_constant_folding.py` & `numba-0.9.0/numba/ast_constant_folding.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/utils.py` & `numba-0.9.0/numba/utils.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,18 +1,25 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import sys
 import opcode
 import ast
 import pprint
 
+try:
+    import __builtin__ as builtins
+except ImportError:
+    import builtins
+
 import numba
 from .minivect.complex_support import Complex64, Complex128, Complex256
 from .minivect import miniast, minitypes
-from numba.typesystem.typemapper import NumbaTypeMapper
+
+def is_builtin(name):
+    return hasattr(builtins, name)
 
 def itercode(code):
     """Return a generator of byte-offset, opcode, and argument
     from a byte-code-string
     """
     i = 0
     extended_arg = 0
@@ -53,20 +60,19 @@
     types_dict = dict(numba.__dict__, d=numba.double, i=numba.int_)
     loc = {}
     # FIXME:  Need something more robust to differentiate between
     #   name ret(arg1,arg2)
     #   and ret(arg1, arg2) or ret ( arg1, arg2 )
     if len(parts) < 2 or '(' in parts[0] or '[' in parts[0] or '('==parts[1][0]:
         signature = eval(sigstr, loc, types_dict)
-        signature.name = None
     else: # Signature has a name
         signature = eval(' '.join(parts[1:]), loc, types_dict)
-        signature.name = parts[0]
+        signature = signature.add('name', parts[0])
     if name is not None:
-        signature.name = name
+        signature = signature.add('name', name)
     return signature
 
 def process_sig(sigstr, name=None):
     signature = process_signature(sigstr, name)
     return signature.name, signature.return_type, signature.args
 
 class NumbaContext(miniast.LLVMContext):
@@ -78,21 +84,21 @@
 
     shape_type = minitypes.npy_intp.pointer()
     strides_type = shape_type
     optimize_broadcasting = False
 
     def init(self):
         self.astbuilder = self.astbuilder_cls(self)
-        self.typemapper = NumbaTypeMapper(self)
+        self.typemapper = None
 
     def is_object(self, type):
         return super(NumbaContext, self).is_object(type) or type.is_array
 
-    def promote_types(self, *args, **kwargs):
-        return self.typemapper.promote_types(*args, **kwargs)
+    # def promote_types(self, *args, **kwargs):
+    #     return self.typemapper.promote_types(*args, **kwargs)
 
 def get_minivect_context():
     return NumbaContext()
 
 context = get_minivect_context()
 
 def ast2tree (node, include_attrs = True):
@@ -110,14 +116,41 @@
         elif isinstance(node, list):
             return [_transform(x) for x in node]
         return node
     if not isinstance(node, ast.AST):
         raise TypeError('expected AST, got %r' % node.__class__.__name__)
     return _transform(node)
 
+def tree2ast(node, namespace):
+    '''Given an AST represented as tuples and lists, attempt to
+    reconstruct the AST object, given a namespace that defines the
+    node constructors.'''
+    def _construct(node):
+        if isinstance(node, tuple):
+            node_len = len(node)
+            if node_len in (2, 3) and hasattr(namespace, node[0]):
+                ctor = getattr(namespace, node[0])
+                assert dict == type(node[1])
+                kwargs = dict((k, _construct(v))
+                              for k, v in node[1].items())
+                if node_len == 3:
+                    kwargs.update((k, _construct(v))
+                                  for k, v in node[2].items())
+                try:
+                    node = ctor(**kwargs)
+                except Exception as exn:
+                    raise Exception('Could not construct %s given %r: %r' %
+                                    (node[0], kwargs, exn))
+            else:
+                node = tuple(_construct(x) for x in node)
+        elif isinstance(node, list):
+            node = [_construct(x) for x in node]
+        return node
+    return _construct(node)
+
 def pformat_ast (node, include_attrs = True, **kws):
     '''Transform a Python AST object into nested tuples and lists, and
     return as a string formatted using pprint.pformat().'''
     return pprint.pformat(ast2tree(node, include_attrs), **kws)
 
 def dump(node, *args, **kws):
     '''Transform a Python AST object into nested tuples and lists, and
```

### Comparing `numba-0.8.1/numba/annotate.py` & `numba-0.9.0/numba/annotate.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/miniast.py` & `numba-0.9.0/numba/minivect/miniast.py`

 * *Files 1% similar despite different names*

```diff
@@ -107,14 +107,15 @@
     Use subclass :py:class:`CContext` to get the defaults for C code generation.
     """
 
     debug = False
     debug_elements = False
 
     use_llvm = False
+    optimize_llvm = True
     optimize_broadcasting = True
 
     shape_type = minitypes.Py_ssize_t.pointer()
     strides_type = shape_type
 
     astbuilder_cls = None
     codegen_cls = UndocClassAttribute(codegen.VectorCodegen)
@@ -480,15 +481,15 @@
     def print_(self, *args):
         "Print out all arguments to stdout"
         return PrintNode(self.pos, args=list(args))
 
     def funccall(self, func_or_pointer, args, inline=False):
         """
         Generate a call to the given function (a :py:class:`FuncNameNode`) of
-        :py:class:`minivect.minitypes.FunctionType` or a
+        :py:class:`minivect.minitypes.function` or a
         pointer to a function type and the given arguments.
         """
         type = func_or_pointer.type
         if type.is_pointer:
             type = func_or_pointer.type.base_type
         return FuncCallNode(self.pos, type.return_type,
                             func_or_pointer=func_or_pointer, args=args,
```

### Comparing `numba-0.8.1/numba/minivect/type_promoter.py` & `numba-0.9.0/numba/minivect/type_promoter.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/pydot/pydot.py` & `numba-0.9.0/numba/minivect/pydot/pydot.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/minitypes.py` & `numba-0.9.0/numba/minivect/minitypes.py`

 * *Files 0% similar despite different names*

```diff
@@ -293,17 +293,17 @@
         int32    : np.int32,
         int64    : np.int64,
         uint8    : np.uint8,
         uint16   : np.uint16,
         uint32   : np.uint32,
         uint64   : np.uint64,
 
-        float_   : np.float32,
-        double   : np.float64,
         longdouble: np.longdouble,
+        double   : np.float64,
+        float_   : np.float32,
 
         short    : np.dtype('h'),
         int_     : np.dtype('i'),
         long_    : np.dtype('l'),
         longlong : np.longlong,
         ushort   : np.dtype('H'),
         uint     : np.dtype('I'),
@@ -504,15 +504,15 @@
 
     def __getattr__(self, attr):
         if attr.startswith('is_'):
             return False
         return getattr(type(self), attr)
 
     def __call__(self, *args):
-        """Return a FunctionType with return_type and args set
+        """Return a function with return_type and args set
         """
         if len(args) == 1 and not isinstance(args[0], Type):
             # Cast in Python space
             # TODO: Create proxy object
             # TODO: Fully customizable type system (do this in Numba, not
             #       minivect)
             return args[0]
```

### Comparing `numba-0.8.1/numba/minivect/minierror.py` & `numba-0.9.0/numba/minivect/minierror.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/minivisitor.py` & `numba-0.9.0/numba/minivect/minivisitor.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/tests/llvm_testutils.py` & `numba-0.9.0/numba/minivect/tests/llvm_testutils.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/tests/test_specializations.py` & `numba-0.9.0/numba/minivect/tests/test_specializations.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/tests/test_hoisting.py` & `numba-0.9.0/numba/minivect/tests/test_hoisting.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/tests/test_operators.py` & `numba-0.9.0/numba/minivect/tests/test_operators.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/tests/testutils.py` & `numba-0.9.0/numba/minivect/tests/testutils.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/graphviz.py` & `numba-0.9.0/numba/minivect/graphviz.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/include/miniutils.h` & `numba-0.9.0/numba/minivect/include/miniutils.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/include/miniutils.pyx` & `numba-0.9.0/numba/minivect/include/miniutils.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/treepath.py` & `numba-0.9.0/numba/minivect/treepath.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/xmldumper.py` & `numba-0.9.0/numba/minivect/xmldumper.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/optimize.py` & `numba-0.9.0/numba/minivect/optimize.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/ctypes_conversion.py` & `numba-0.9.0/numba/minivect/ctypes_conversion.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/complex_support.py` & `numba-0.9.0/numba/minivect/complex_support.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
+import numpy as np
 from .miniutils import ctypes
 from .minitypes import *
 
 ### Taken from Numba ###
 
 # NOTE: The following ctypes structures were inspired by Joseph
 # Heller's response to python-list question about ctypes complex
@@ -41,28 +42,23 @@
                 # Return the value property, not the ComplexMixin
                 # instance built by ctypes.
                 result = ctypes_function(*args, **kws)
                 return result.value
             return _complex_result_wrapper
         return _make_complex_result_wrapper
 
-try:
-    import numpy as np
-except ImportError:
-    pass
+class Complex64(ctypes.Structure, ComplexMixin):
+    _fields_ = [('real', ctypes.c_float), ('imag', ctypes.c_float)]
+    _numpy_ty_ = np.complex64
+
+class Complex128(ctypes.Structure, ComplexMixin):
+    _fields_ = [('real', ctypes.c_double), ('imag', ctypes.c_double)]
+    _numpy_ty_ = np.complex128
+
+if hasattr(np, 'complex256'):
+    class Complex256(ctypes.Structure, ComplexMixin):
+        _fields_ = [('real', ctypes.c_longdouble), ('imag', ctypes.c_longdouble)]
+        _numpy_ty_ = np.complex256
 else:
-    class Complex64(ctypes.Structure, ComplexMixin):
-        _fields_ = [('real', ctypes.c_float), ('imag', ctypes.c_float)]
-        _numpy_ty_ = np.complex64
-
-    class Complex128(ctypes.Structure, ComplexMixin):
-        _fields_ = [('real', ctypes.c_double), ('imag', ctypes.c_double)]
-        _numpy_ty_ = np.complex128
-
-    if hasattr(np, 'complex256'):
-        class Complex256(ctypes.Structure, ComplexMixin):
-            _fields_ = [('real', ctypes.c_longdouble), ('imag', ctypes.c_longdouble)]
-            _numpy_ty_ = np.complex256
-    else:
-        Complex256 = None
+    Complex256 = None
 
 ### End Taken from Numba ###
```

### Comparing `numba-0.8.1/numba/minivect/codegen.py` & `numba-0.9.0/numba/minivect/codegen.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/minicode.py` & `numba-0.9.0/numba/minivect/minicode.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/minivect/llvm_codegen.py` & `numba-0.9.0/numba/minivect/llvm_codegen.py`

 * *Files 3% similar despite different names*

```diff
@@ -77,71 +77,72 @@
     def append_basic_block(self, name='unamed'):
         "append a basic block and keep track of it"
         idx = len(self.blocks)
         bb = self.lfunc.append_basic_block('%s_%d' % (name, idx))
         self.blocks.append(bb)
         return bb
 
-    def optimize(self):
-        "Run llvm optimizations on the generated LLVM code (using the old llvm-py)"
-        llvm_fpm = llvm.passes.FunctionPassManager.new(self.llvm_module)
-        for llvm_pass in self.context.llvm_passes():
-            llvm_fpm.add(llvm_pass)
-
-        llvm_fpm.initialize()
-        llvm_fpm.run(self.lfunc)
-        llvm_fpm.finalize()
-
-        # self.context.llvm_fpm.run(self.lfunc)
-
-    def optimize(self):
-        "Run llvm optimizations on the generated LLVM code"
+    def inline_funcs(self):
         for call_instr in self.inline_calls:
             # print 'inlining...', call_instr
             llvm.core.inline_function(call_instr)
 
+    def optimize(self):
+        "Run llvm optimizations on the generated LLVM code"
         llvm_fpm = llvm.passes.FunctionPassManager.new(self.llvm_module)
         # target_data = llvm.ee.TargetData(self.context.llvm_ee)
         #llvm_fpm.add(self.context.llvm_ee.target_data.clone())
         pmb = llvm.passes.PassManagerBuilder.new()
         pmb.opt_level = 3
         pmb.vectorize = True
 
         pmb.populate(llvm_fpm)
         llvm_fpm.run(self.lfunc)
 
+    def optimize2(self, opt=3, cg=3, inline=1000):
+        features = '-avx'
+        tm = self.__machine = llvm.ee.TargetMachine.new(
+            opt=cg, cm=llvm.ee.CM_JITDEFAULT, features=features)
+        has_loop_vectorizer = llvm.version >= (3, 2)
+        passmanagers = llvm.passes.build_pass_managers(
+            tm, opt=opt, inline_threshold=inline,
+            loop_vectorize=has_loop_vectorizer, fpm=False)
+        passmanagers.pm.run(self.llvm_module)
+
     def visit_FunctionNode(self, node):
         self.specializer = node.specializer
         self.function = node
         self.llvm_module = self.context.llvm_module
 
         name = node.name + node.specialization_name
         node.mangled_name = name
 
         lfunc_type = node.type.to_llvm(self.context)
         self.lfunc = self.llvm_module.add_function(lfunc_type, node.mangled_name)
+        # self.lfunc.linkage = llvm.core.LINKAGE_LINKONCE_ODR
 
         self.entry_bb = self.append_basic_block('entry')
         self.builder = llvm.core.Builder.new(self.entry_bb)
 
         self.add_arguments(node)
         self.visit(node.body)
 
         # print self.lfunc
-        self.lfunc.verify()
-        self.optimize()
-        # print self.lfunc
+        self.llvm_module.verify()
+        self.inline_funcs()
+        if self.context.optimize_llvm:
+            self.optimize2()
 
         self.code.write(self.lfunc)
 
-        from numba.codegen.llvmcontext import LLVMContextManager
-        ctypes_func = ctypes_conversion.get_ctypes_func(
-                    node, self.lfunc, LLVMContextManager().execution_engine,
-                                                        self.context)
-        self.code.write(ctypes_func)
+        # from numba.codegen.llvmcontext import LLVMContextManager
+        # ctypes_func = ctypes_conversion.get_ctypes_func(
+        #             node, self.lfunc, LLVMContextManager().execution_engine,
+        #                                                 self.context)
+        # self.code.write(ctypes_func)
 
     def add_arguments(self, function):
         "Insert function arguments into the symtab"
         i = 0
         for arg in function.arguments + function.scalar_arguments:
             if arg.used:
                 for var in arg.variables:
```

### Comparing `numba-0.8.1/numba/minivect/miniutils.py` & `numba-0.9.0/numba/minivect/miniutils.py`

 * *Files 4% similar despite different names*

```diff
@@ -51,15 +51,15 @@
     funcname = builder.funcname(signature, func_name, is_external=False)
 
     # Generate 'lhs[i, j] = kernel(A[i, j], B[i, j])'
     lhs = miniargs[0].variable
     kernel_args = [arg.variable for arg in miniargs[1:]]
     funccall = builder.funccall(funcname, kernel_args, inline=True)
     assmt = builder.assign(lhs, funccall)
-    if lhs.type.is_object:
+    if lhs.type.is_object and not lhs.type.is_array:
         assmt = builder.stats(builder.decref(lhs), assmt)
 
     return assmt
 
 def specialize(context, specializer_cls, ast, print_tree=False):
     "Specialize an AST with given specializer and compile"
     context = context or getcontext()
```

### Comparing `numba-0.8.1/numba/minivect/specializers.py` & `numba-0.9.0/numba/minivect/specializers.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/error.py` & `numba-0.9.0/numba/error.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,47 +1,53 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import traceback
 
-from numba.minivect.minierror import Error
-
-__all__ = ["Error", "NumbaError", "InternalError", "InvalidTemplateError"]
+__all__ = ["NumbaError", "InternalError", "InvalidTemplateError"]
 
 def format_pos(node):
     if node is not None and hasattr(node, 'lineno'):
         return format_postup((node.lineno, node.col_offset))
     else:
         return ""
 
 def format_postup(tup):
     lineno, col_offset = tup
     return "%s:%s: " % (lineno - 1, col_offset)
 
-class NumbaError(Error):
+class NumbaError(Exception):
     "Some error happened during compilation"
 
-    def __init__(self, node, msg=None, *args):
+    def __init__(self, node, msg=None, *args, **kwds):
         if msg is None:
             node, msg = None, node
 
         self.node = node
         self.msg = msg
         self.args = args
+        self.has_report = kwds.get("has_report", False)
 
     def __str__(self):
         try:
+            if self.has_report:
+                return self.msg.strip()
             pos = format_pos(self.node)
             msg = "%s%s %s" % (pos, self.msg, " ".join(map(str, self.args)))
             return msg.rstrip()
         except:
             traceback.print_exc()
             return "<internal error creating numba error message>"
 
 
-class InternalError(Error):
+class InternalError(Exception):
     "Indicates a compiler bug"
 
-class _UnknownAttribute(Error):
+class _UnknownAttribute(Exception):
     pass
 
-class InvalidTemplateError(Error):
+class InvalidTemplateError(Exception):
     "Raised for invalid template type specifications"
+
+class UnpromotableTypeError(TypeError):
+    "Raised when we can't promote two given types"
+    def __str__(self):
+        return "Cannot promote types %s and %s" % self.args[0]
```

### Comparing `numba-0.8.1/numba/pipeline.py` & `numba-0.9.0/numba/pipeline.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,23 +18,23 @@
 from numba import functions
 from numba import transforms
 from numba import control_flow
 from numba import optimize
 from numba import closures
 from numba import reporting
 from numba import normalize
+from numba import typesystem
 from numba.codegen import llvmwrapper
 from numba import ast_constant_folding as constant_folding
 from numba.control_flow import ssa
 from numba.codegen import translate
 from numba import utils
 from numba.missing import FixMissingLocations
 from numba.type_inference import infer as type_inference
 from numba.asdl import schema
-from numba.minivect import minitypes
 import numba.visitors
 
 from numba.specialize import comparisons
 from numba.specialize import loops
 from numba.specialize import exceptions
 from numba.specialize import funccalls
 from numba.specialize import exttypes
@@ -92,21 +92,20 @@
     try:
         pipeline(func_env.ast, env)
     finally:
         env.translation.pop()
 
 def _infer_types2(env, func, restype=None, argtypes=None, **kwargs):
     ast = functions._get_ast(func)
-    func_signature = minitypes.FunctionType(return_type=restype,
-                                            args=argtypes)
+    func_signature = typesystem.function(restype, argtypes)
     return run_pipeline2(env, func, ast, func_signature, **kwargs)
 
 def infer_types2(env, func, restype=None, argtypes=None, **kwargs):
     """
-    Like run_pipeline, but takes restype and argtypes instead of a FunctionType
+    Like run_pipeline, but takes restype and argtypes instead of a function
     """
     pipeline, (sig, symtab, ast) = _infer_types2(
         env, func, restype, argtypes, pipeline_name='type_infer', **kwargs)
     return sig, symtab, ast
 
 
 def compile2(env, func, restype=None, argtypes=None, ctypes=False,
@@ -120,16 +119,15 @@
     """
     # Let the pipeline create a module for the function it is compiling
     # and the user will link that in.
     assert 'llvm_module' not in kwds
     kwds['llvm_module'] = lc.Module.new(module_name(func))
     logger.debug(kwds)
     func_ast = functions._get_ast(func)
-    func_signature = minitypes.FunctionType(return_type=restype,
-                                            args=argtypes)
+    func_signature = typesystem.function(restype, argtypes)
     #pipeline, (func_signature, symtab, ast) = _infer_types2(
     #            env, func, restype, argtypes, codegen=True, **kwds)
     with env.TranslationContext(env, func, func_ast, func_signature,
                                 need_lfunc_wrapper=not compile_only,
                                 **kwds) as func_env:
         pipeline = env.get_pipeline(kwds.get('pipeline_name', None))
         func_ast.pipeline = pipeline
@@ -186,15 +184,15 @@
                 ast = self.transform(ast, env)
             except error.NumbaError as e:
                 func_env = env.translation.crnt
                 error_env = func_env.error_env
                 if func_env.is_closure:
                     flags, parent_func_env = env.translation.stack[-2]
                     error_env.merge_in(parent_func_env.error_env)
-                else:
+                elif not e.has_report:
                     reporting.report(env, exc=e)
                 raise
 
         env.translation.crnt.ast = ast
         if env.stage_checks: self.check_postconditions(ast, env)
         return ast
 
@@ -226,19 +224,17 @@
     crnt = env.translation.crnt
     if crnt.template_signature is not None:
         from numba import typesystem
 
         argnames = [name.id for name in ast.args.args]
         argtypes = list(crnt.func_signature.args)
 
-        typesystem.resolve_templates(crnt.locals, crnt.template_signature,
-                                     argnames, argtypes)
-        crnt.func_signature = minitypes.FunctionType(
-            return_type=crnt.func_signature.return_type,
-            args=tuple(argtypes))
+        template_context, signature = typesystem.resolve_templates(
+            crnt.locals, crnt.template_signature, argnames, argtypes)
+        crnt.func_signature = signature
 
     return ast
 
 
 def validate_signature(tree, env):
     arg_types = env.translation.crnt.func_signature.args
     if (isinstance(tree, ast_module.FunctionDef) and
@@ -255,15 +251,14 @@
 
     restype = func_signature.return_type
     if restype and (restype.is_struct or restype.is_complex):
         # Change signatures returning complex numbers or structs to
         # signatures taking a pointer argument to a complex number
         # or struct
         func_signature = func_signature.return_type(*func_signature.args)
-        func_signature.struct_by_reference = True
         func_env.func_signature = func_signature
 
     return tree
 
 
 def get_lfunc(env, func_env):
     lfunc = func_env.llvm_module.add_function(
@@ -501,33 +496,44 @@
             translate.LLVMCodeGenerator, ast, env,
             **func_env.kwargs)
 
         func_env.translator.translate()
         func_env.lfunc = func_env.translator.lfunc
         return ast
 
+class PostPass(PipelineStage):
+    def transform(self, ast, env):
+        for postpass_name, postpass in env.crnt.postpasses.iteritems():
+            env.crnt.lfunc = postpass(env,
+                                      env.llvm_context.execution_engine,
+                                      env.crnt.llvm_module,
+                                      env.crnt.lfunc)
+        return ast
+
 class LinkingStage(PipelineStage):
     """
     Link the resulting LLVM function into the global fat module.
     """
 
     def transform(self, ast, env):
         func_env = env.translation.crnt
 
         # Link libraries into module
         env.context.intrinsic_library.link(func_env.lfunc.module)
         # env.context.cbuilder_library.link(func_env.lfunc.module)
         env.constants_manager.link(func_env.lfunc.module)
 
+        lfunc_pointer = 0
         if func_env.link:
             # Link function into fat LLVM module
             func_env.lfunc = env.llvm_context.link(func_env.lfunc)
             func_env.translator.lfunc = func_env.lfunc
+            lfunc_pointer = func_env.translator.lfunc_pointer
 
-        func_env.lfunc_pointer = func_env.translator.lfunc_pointer
+        func_env.lfunc_pointer = lfunc_pointer
 
         return ast
 
 class WrapperStage(PipelineStage):
     """
     Build a wrapper LLVM function around the compiled numba function to call
     it from Python.
```

### Comparing `numba-0.8.1/numba/optimize.py` & `numba-0.9.0/numba/optimize.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/traits.py` & `numba-0.9.0/numba/traits.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/schema.py` & `numba-0.9.0/numba/asdl/schema.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,33 +1,40 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
-import sys
+
 import ast
-from . import asdl
+import keyword
 from collections import defaultdict, namedtuple
 import contextlib
 
+from . import asdl
+from .asdl import pyasdl
+
 def load(name):
     '''Load a ASDL Schema by name; e.g. "Python.asdl".
         
     Returns a Schema object.
 
     This tries to load from the version-specific directory, first.
     If it failed, it loads from the common-directory.
     '''
-    python_asdl = asdl.load(name)
+    parser, loader = asdl.load_pyschema(name)
+    python_asdl = loader.load()
+    return build_schema(python_asdl)
+
+def build_schema(asdl_tree):
     schblr = SchemaBuilder()
-    schblr.visit(python_asdl)
+    schblr.visit(asdl_tree)
     return schblr.schema
 
 class _rule(namedtuple('rule', ['kind', 'fields'])):
     __slots__ = ()
 
-    SUM = 0
-    PROD = 1
+    SUM = 0     # sums, e.g. Foo | Bar
+    PROD = 1    # producs, e.g. (Foo, Bar)
 
     @classmethod
     def sum(cls, fields):
         return cls(kind=cls.SUM, fields=fields)
 
     @classmethod
     def product(cls, fields):
@@ -72,28 +79,41 @@
 
         schema.verify(ast)
         schema.verify(ast, context=SchemaContext())
     '''
     def __init__(self, name):
         # name of the asdl module
         self.name = name
+
         # a dictionary of {type name -> fields}
         self.types = defaultdict(list)
+
         # a dictionary of {definition name -> _rule}
         self.dfns = {}
 
+        # { type name -> fields }
+        self.attributes = defaultdict(list)
+
     def verify(self, ast, context=None):
         '''Check against an AST raises SchemaError upon error.
         
         ast --- The ast being verified
         context --- [optional] a SchemaContext.
         '''
         context = context if context is not None else SchemaContext()
         return SchemaVerifier(self, context).visit(ast)
 
+    def __str__(self):
+        return "%s(name=%s, types=%s, rules=%s, attributes=%s)" % (
+            type(self).__name__,
+            self.name,
+            self.types,
+            self.dfns,
+            self.attributes)
+
     def debug(self):
         print(("Schema %s" % self.name))
         for k, fs in self.types.items():
             print(('    --', k, fs))
         for k, fs in self.dfns.items():
             if fs.is_sum():
                 print(('   ', k))
@@ -233,21 +253,22 @@
                               "Missing definition for '%s' in the ASDL" % name)
         return ret
 
     def _get_type(self, cls_or_name):
         name = (cls_or_name
                 if isinstance(cls_or_name, str)
                 else type(cls_or_name).__name__)
-        ret = self.schema.types.get(name)
-        if ret is None:
+        fields = self.schema.types.get(name)
+        attrs = self.schema.attributes.get(name)
+        if fields is None or attrs is None:
             raise SchemaError(self._debug_context,
                               "Unknown AST node type: %s" % name)
-        return ret
+        return fields + attrs
 
-class SchemaBuilder(asdl.VisitorBase):
+class SchemaBuilder(pyasdl.VisitorBase):
     '''A single instance of SchemaBuilder can be used build different 
     Schema from different ASDL.
 
     Usage:
         schblr = SchemaBuilder()
         schblr.visit(some_asdl)
         schema = schblr.schema      # get the schema object
@@ -255,48 +276,46 @@
     NOTE:
         - It ignore the attributes of the nodes.
     '''
     def __init__(self):
         super(SchemaBuilder, self).__init__()
 
     def visitModule(self, mod):
-        self.__schema = Schema(str(mod.name))
+        self._schema = Schema(str(mod.name))
         for dfn in mod.dfns:
             self.visit(dfn)
 
     def visitType(self, type):
         self.visit(type.value, str(type.name))
 
     def visitSum(self, sum, name):
         self.schema.dfns[str(name)] = _rule.sum([str(t.name)
                                                  for t in sum.types])
+        self.schema.attributes[name].extend(sum.attributes)
+
         for t in sum.types:
             self.visit(t, name, sum.attributes)
 
-    def visitConstructor(self, cons, name, attr=[]):
+    def visitConstructor(self, cons, name, attrs=[]):
         typename = str(cons.name)
-        fields = self.schema.types[typename]
-        for f in cons.fields:
-            fields.append(f)
-        for f in attr:
-            fields.append(f)
-
+        self.schema.types[typename].extend(cons.fields)
+        self.schema.attributes[typename].extend(attrs)
 
     def visitField(self, field, name):
         key = str(field.type)
 
     def visitProduct(self, prod, name):
         assert not hasattr(prod, 'attributes')
         self.schema.dfns[str(name)] = _rule.product(prod.fields)
         for f in prod.fields:
             self.visit(f, name)
 
     @property
     def schema(self):
-        return self.__schema
+        return self._schema
 
 #
 # Builtin types handler
 #
 
 def _verify_identifier(value):
     return isinstance(value, str)
@@ -319,7 +338,21 @@
 def _is_iterable(value):
     try:
         iter(value)
     except TypeError:
         return False
     else:
         return True
+
+def verify_names(names):
+    for name in names:
+        if keyword.iskeyword(name):
+            raise ValueError("%r is a keyword" % (name,))
+
+def verify_schema_keywords(schema):
+    """
+    Verify schema, checking for the use of any Python keywords.
+    """
+    verify_names(schema.dfns)
+    verify_names(schema.types)
+    verify_names([field.name for fields in schema.types.itervalues()
+                                 for field in fields])
```

### Comparing `numba-0.8.1/numba/asdl/tests/test_good.py` & `numba-0.9.0/numba/asdl/tests/test_good.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/tests/test_bad.py` & `numba-0.9.0/numba/asdl/tests/test_bad.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/py3_3/Python.asdl` & `numba-0.9.0/numba/asdl/py3_3/Python.asdl`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/py2_7/asdl.py` & `numba-0.9.0/numba/asdl/py2_7/asdl.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/py2_7/Python.asdl` & `numba-0.9.0/numba/asdl/py2_7/Python.asdl`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/py2_7/spark.py` & `numba-0.9.0/numba/asdl/py2_7/spark.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/common/asdl.py` & `numba-0.9.0/numba/asdl/common/asdl.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/common/Python.asdl` & `numba-0.9.0/numba/asdl/common/Python.asdl`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/common/spark.py` & `numba-0.9.0/numba/asdl/common/spark.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/asdl/py3_2/Python.asdl` & `numba-0.9.0/numba/asdl/py3_2/Python.asdl`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/typesystem/typeutils.py` & `numba-0.9.0/numba/typesystem/typeutils.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,31 +1,36 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
+
+from numba import error
 from numba.typesystem import *
 
 #------------------------------------------------------------------------
 # Utilities
 #------------------------------------------------------------------------
 
+ts = numba_typesystem
+
 def is_obj(type):
     return type.is_object or type.is_array
 
 native_type_dict = {}
-for native_type in minitypes.native_integral:
-    native_type_dict[(native_type.itemsize, native_type.signed)] = native_type
+for native_type in native_integral:
+    if native_type not in (Py_ssize_t, npy_intp, Py_uintptr_t, size_t): # TODO: do this better
+        native_type_dict[(native_type.itemsize, native_type.signed)] = native_type
 
 def promote_to_native(int_type):
     return native_type_dict[int_type.itemsize, int_type.signed]
 
-def promote_closest(context, int_type, candidates):
+def promote_closest(ts, int_type, candidates):
     """
     promote_closest(Py_ssize_t, [int_, long_, longlong]) -> longlong
     """
     for candidate in candidates:
-        promoted = context.promote_types(int_type, candidate)
+        promoted = ts.promote(int_type, candidate)
         if promoted.itemsize == candidate.itemsize and promoted.signed == candidate.signed:
             return candidate
 
     return candidates[-1]
 
 def get_type(ast_node):
     """
@@ -39,18 +44,15 @@
     raise error.NumbaError("Type %s can not be indexed or "
                            "iterated over" % (type,))
 
 
 def index_type(type):
     "Result of indexing a value of the given type with an integer index"
     if type.is_array:
-        result = type.copy()
-        result.ndim -= 1
-        if result.ndim == 0:
-            result = result.dtype
+        result = array(type.dtype, type.ndim - 1)
     elif type.is_container or type.is_pointer:
         result = type.base_type
     elif type.is_dict:
         result = type.value_type
     elif type.is_range:
         result = Py_ssize_t
     elif type.is_object:
@@ -66,18 +68,16 @@
         return type.key_type
     elif type.is_pointer and not type.is_sized_pointer:
         error_index(type)
     else:
         return index_type(type)
 
 def require(ast_nodes, properties):
-    "Assert that the types of the given nodes meets a certainrequirement"
+    "Assert that the types of the given nodes meets a certain requirement"
     for ast_node in ast_nodes:
         if not any(getattr(get_type(ast_node), p) for p in properties):
             typenames = ", or ".join(p[3:] for p in properties) # remove 'is_' prefix
             raise error.NumbaError(ast_node, "Expected an %s" % (typenames,))
 
 def pyfunc_signature(nargs):
     "Signature of a python function with N arguments"
-    signature = minitypes.FunctionType(args=(object_,) * nargs,
-                                       return_type=object_)
-    return signature
+    return function(args=(object_,) * nargs, return_type=object_)
```

### Comparing `numba-0.8.1/numba/typesystem/templatetypes.py` & `numba-0.9.0/numba/typesystem/templatetypes.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,71 +1,78 @@
 # -*- coding: utf-8 -*-
 """
 Autojit template types.
 """
 from __future__ import print_function, division, absolute_import
 
-from numba.typesystem import *
+import numba as nb
+from numba import error
+from numba.typesystem import Type, NumbaType
 
 # type_attribute => [type_assertions]
 VALID_TYPE_ATTRIBUTES = {
     "dtype": ["is_array"],
     "base_type": ["is_pointer", "is_carray", "is_complex",
                   "is_list", "is_tuple"],
     "args": ["is_function"],
     "return_type": ["is_function"],
     # "fields": ["is_struct"],
     "fielddict": ["is_struct"],
 }
 
-class TemplateType(NumbaType):
-
-    is_template = True
-    template_count = 0
-
-    def __init__(self, name=None, **kwds):
-        if name is None:
-            name = "T%d" % self.template_count
-            TemplateType.template_count += 1
-
-        self.name = name
+class _TemplateType(NumbaType):
 
     def resolve_template(self, template_context):
         if self not in template_context:
             raise error.InvalidTemplateError("Unknown template type: %s" % self)
         return template_context[self]
 
     def __getitem__(self, index):
         if isinstance(index, (tuple, slice)):
-            return super(TemplateType, self).__getitem__(index)
+            return super(_TemplateType, self).__getitem__(index)
 
         return TemplateIndexType(self, index)
 
     def __getattr__(self, attr):
         if attr in VALID_TYPE_ATTRIBUTES:
             return TemplateAttributeType(self, attr)
 
-        return super(TemplateType, self).__getattr__(attr)
+        return super(_TemplateType, self).__getattr__(attr)
 
     def __repr__(self):
         return "template(%s)" % self.name
 
     def __str__(self):
         return self.name
 
 
-class TemplateAttributeType(TemplateType):
+class template(_TemplateType):
 
-    is_template_attribute = True
-    subtypes = ['template_type']
+    argnames = [("name", None)]
+    flags    = ["object"]
 
-    def __init__(self, template_type, attribute_name, **kwds):
-        self.template_type = template_type
-        self.attribute_name = attribute_name
+    template_count = 0
+
+    def __init__(self, name):
+        super(template, self).__init__(name)
+        if name is None:
+            name = "T%d" % self.template_count
+            template.template_count += 1
+
+        self.name = name
+
+
+class TemplateAttributeType(_TemplateType):
+
+    typename = "template_attribute"
+    argnames = ["template_type", "attribute_name"]
+    flags = ["object", "template"]
 
+    def __init__(self, template_type, attribute_name, **kwds):
+        super(TemplateAttributeType, self).__init__(template_type, attribute_name)
         assert attribute_name in VALID_TYPE_ATTRIBUTES
 
     def resolve_template(self, template_context):
         resolved_type = self.template_type.resolve_template(template_context)
 
         assertions = VALID_TYPE_ATTRIBUTES[self.attribute_name]
         valid_attribute = any(getattr(resolved_type, a) for a in assertions)
@@ -78,38 +85,32 @@
 
     def __repr__(self):
         return "%r.%s" % (self.template_type, self.attribute_name)
 
     def __str__(self):
         return "%s.%s" % (self.template_type, self.attribute_name)
 
-class TemplateIndexType(TemplateType):
-
-    is_template_index = True
-    subtypes = ['template_type']
+class TemplateIndexType(_TemplateType):
 
-    def __init__(self, template_type, index, **kwds):
-        self.template_type = template_type
-        self.index = index
+    typename = "template_index"
+    argnames = ["template_type", "index"]
+    flags = ["object", "template"]
 
     def resolve_template(self, template_context):
         attrib = self.template_type.resolve_template(template_context)
         assert isinstance(attrib, (list, tuple, dict))
         return attrib[self.index]
 
     def __repr__(self):
         return "%r[%r]" % (self.template_type, self.index)
 
     def __str__(self):
         return "%s[%r]" % (self.template_type, self.index)
 
 
-
-template = TemplateType
-
 def validate_template(concrete_type, template_type):
     if not isinstance(template_type, type(concrete_type)):
         raise error.InvalidTemplateError(
                 "Type argument does not match template type: %s and %s" % (
                 concrete_type, template_type))
 
     if concrete_type.is_array:
@@ -159,63 +160,64 @@
                         "Inconsistent types found for template: %s and %s" % (
                                                     prev_type, concrete_type))
         else:
             template_context[template_type] = concrete_type
     else:
         validate_template(concrete_type, template_type)
 
-        for t1, t2 in zip(template_type.subtype_list,
-                          concrete_type.subtype_list):
+        for t1, t2 in zip(subtype_list(template_type),
+                          subtype_list(concrete_type)):
             if not isinstance(t1, (list, tuple)):
                 t1, t2 = [t1], [t2]
 
             for t1, t2 in zip(t1, t2):
                 match_template(t1, t2, template_context)
 
-def resolve_template_type(template_type, template_context):
+def resolve_template_type(ty, template_context):
     """
     After the template context is known, resolve functions on template types
     E.g.
 
-        T[:]                -> ArrayType(dtype=T)
-        void(T)             -> FunctionType(args=[T])
+        T[:]                -> array_(dtype=T)
+        void(T)             -> function(args=[T])
         Struct { T arg }    -> struct(fields={'arg': T})
-        T *                 -> PointerType(base_type=T)
+        T *                 -> pointer(base_type=T)
 
     Any other compound types?
     """
     r = lambda t: resolve_template_type(t, template_context)
 
-    if template_type.is_template:
-        template_type = template_type.resolve_template(template_context)
-    elif template_type.is_array:
-        template_type = template_type.copy()
-        template_type.dtype = r(template_type.dtype)
-    elif template_type.is_function:
-        template_type = r(template_type.return_type)(*map(r, template_type.args))
-    elif template_type.is_struct:
-        S = template_type
+    if ty.is_template:
+        ty = ty.resolve_template(template_context)
+    elif ty.is_array:
+        ty = nb.array(r(ty.dtype), ty.ndim)
+    elif ty.is_function:
+        ty = r(ty.return_type)(*map(r, ty.args))
+    elif ty.is_struct:
+        S = ty
         fields = []
         for field_name, field_type in S.fields:
             fields.append((field_name, r(field_type)))
-        template_type = numba.struct(fields, name=S.name, readonly=S.readonly,
-                                     packed=S.packed)
-    elif template_type.is_pointer:
-        template_type = r(template_type.base_type).pointer()
+        ty = nb.struct_(fields, name=S.name, readonly=S.readonly, packed=S.packed)
+    elif ty.is_pointer:
+        ty = r(ty.base_type).pointer()
 
-    return template_type
+    return ty
 
 def is_template_list(types):
     return any(is_template(type) for type in types)
 
+def subtype_list(T):
+    return T.subtypes
+
 def is_template(T):
     if isinstance(T, (list, tuple)):
         return is_template_list(T)
 
-    return T.is_template or is_template_list(T.subtype_list)
+    return T.is_template or is_template_list(subtype_list(T))
 
 def resolve_templates(locals, template_signature, arg_names, arg_types):
     """
     Resolve template types given a signature with concrete types.
     """
     template_context = {}
     locals = locals or {}
```

### Comparing `numba-0.8.1/numba/typesystem/closuretypes.py` & `numba-0.9.0/numba/typesystem/closuretypes.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,49 +1,44 @@
 # -*- coding: utf-8 -*-
+
 """
 Types for closures and inner functions.
 """
+
 from __future__ import print_function, division, absolute_import
 
-from numba.minivect import minitypes
-from numba.typesystem.basetypes import NumbaType
+from numba.typesystem import NumbaType
 from numba.exttypes.types.extensiontype import ExtensionType
 
-class ClosureType(NumbaType, minitypes.ObjectType):
+class ClosureType(NumbaType):
     """
     Type of closures and inner functions.
     """
 
-    is_closure = True
-
-    def __init__(self, signature, **kwds):
-        super(ClosureType, self).__init__(**kwds)
-        self.signature = signature
-        self.closure = None
+    typename = "closure"
+    argnames = ["signature", ("closure", None)]
+    flags = ["object"]
 
     def add_scope_arg(self, scope_type):
-        self.signature.args = (scope_type,) + self.signature.args
+        self.signature = self.signature.add_arg(0, scope_type)
 
     def __repr__(self):
         return "<closure(%s)>" % self.signature
 
 class ClosureScopeType(ExtensionType):
     """
     Type of the enclosing scope for closures. This is always passed in as
     first argument to the function.
     """
 
-    is_closure_scope = True
+    typename = "closure_scope"
     is_final = True
 
-    def __init__(self, py_class, parent_scope, **kwds):
-        super(ClosureScopeType, self).__init__(py_class, **kwds)
+    def __init__(self, py_class, parent_scope):
+        super(ClosureScopeType, self).__init__(py_class)
         self.parent_scope = parent_scope
         self.unmangled_symtab = None
 
         if self.parent_scope is None:
             self.scope_prefix = ""
         else:
-            self.scope_prefix = self.parent_scope.scope_prefix + "0"
-
-    def __repr__(self):
-        return "closure_scope(%s)" % self.attribute_table
+            self.scope_prefix = self.parent_scope.scope_prefix + "0"
```

### Comparing `numba-0.8.1/numba/typesystem/ssatypes.py` & `numba-0.9.0/numba/typesystem/ssatypes.py`

 * *Files 1% similar despite different names*

```diff
@@ -34,14 +34,16 @@
                 \   \
                   X_2
                     \
                       i_0 (Py_ssize_t)
 """
 from __future__ import print_function, division, absolute_import
 
+from functools import partial
+
 from numba import oset
 from numba.minivect import minierror
 from numba.typesystem import *
 
 class UninitializedType(NumbaType):
 
     is_uninitialized = True
@@ -127,17 +129,17 @@
 class PromotionType(UnresolvedType):
 
     is_promotion = True
     resolved_type = None
 
     count = 0 # for debugging
 
-    def __init__(self, variable, context, types, assignment=False, **kwds):
+    def __init__(self, variable, promote, types, assignment=False, **kwds):
         super(PromotionType, self).__init__(variable, **kwds)
-        self.context = context
+        self.promote = promote
         self.types = oset.OrderedSet(types)
         self.assignment = assignment
         variable.type = self
 
         self.add_parents(type for type in types if type.is_unresolved)
 
         self.count = PromotionType.count
@@ -228,18 +230,18 @@
             # Everything is deferred
             self.resolved_type = None
             return False
         else:
             # Simplify as much as possible
             if self.assignment:
                 result_type, unresolved_types = promote_for_assignment(
-                        self.context, resolved_types, unresolved_types,
-                        self.variable.name)
+                    self.promote, resolved_types, unresolved_types,
+                    self.variable.name)
             else:
-                result_type = promote_for_arithmetic(self.context, resolved_types)
+                result_type = promote_for_arithmetic(self.promote, resolved_types)
 
             self.resolved_type = result_type
             if len(resolved_types) == len(types) or not unresolved_types:
                 self.variable.type = result_type
                 return True
             else:
                 old_types = self.types
@@ -366,14 +368,15 @@
 
         a = np.empty((10, 10, 10))
         for i in range(3):
             a = a[0]
 
     Here the type would change on each iteration. Arrays do not demote to
     object, but other types do. The same goes for a call:
+            error_circular(result_type.variable)
 
         for i in range(n):
             f = f(i)
 
     but also
 
         x = 0
@@ -709,18 +712,18 @@
                 "Cannot unify arrays with distinct dimensionality: "
                 "%d and %d" % (first_array_type.ndim, array_type.ndim))
         elif array_type.dtype != first_array_type.dtype:
             raise TypeError("Cannot unify arrays with distinct dtypes: "
                             "%s and %s" % (first_array_type.dtype,
                                            array_type.dtype))
 
-def promote_for_arithmetic(context, types, assignment=False):
+def promote_for_arithmetic(promote, types, assignment=False):
     result_type = types[0]
     for type in types[1:]:
-        result_type = context.promote_types(result_type, type, assignment)
+        result_type = promote(result_type, type, assignment)
 
     return result_type
 
 def promote_arrays(array_types, non_array_types, types,
                    unresolved_types, var_name):
     """
     This promotes arrays for assignments. Arrays must have a single consistent
@@ -744,15 +747,15 @@
 
     # Add delayed assertion that triggers when the delayed types are resolved
     for unresolved_type in unresolved_types:
         unresolved_type.assertions.append(assert_equal)
 
     return result_type, []
 
-def promote_for_assignment(context, types, unresolved_types, var_name):
+def promote_for_assignment(promote, types, unresolved_types, var_name):
     """
     Promote a list of types for assignment (e.g. in a phi node).
 
         - if there are any objects, the result will always be an object
         - if there is an array, all types must be of that array type
               (minus any contiguity constraints)
     """
@@ -763,10 +766,30 @@
         if array_types:
             return promote_arrays(array_types, non_array_types, types,
                                   unresolved_types, var_name)
         else:
             # resolved_types = obj_types
             return object_, []
 
-    partial_result_type = promote_for_arithmetic(context, types,
+    partial_result_type = promote_for_arithmetic(promote, types,
                                                  assignment=True)
     return partial_result_type, unresolved_types
+
+def promote(typesystem, type1, type2, assignment=False):
+    promote_ = partial(promote, typesystem)
+
+    if type1.is_unresolved or type2.is_unresolved:
+        if type1.is_unresolved:
+            type1 = type1.resolve()
+        if type2.is_unresolved:
+            type2 = type2.resolve()
+
+        if type1.is_unresolved or type2.is_unresolved:
+            # The Variable is really only important for ast.Name, fabricate
+            # one
+            from numba import symtab
+            var = symtab.Variable(None)
+            return PromotionType(var, promote_, [type1, type2])
+        else:
+            return typesystem.promote(type1, type2)
+
+    return typesystem.promote(type1, type2)
```

### Comparing `numba-0.8.1/numba/typesystem/typeset.py` & `numba-0.9.0/numba/typesystem/typeset.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,16 +6,16 @@
 
 import collections
 from functools import reduce
 from itertools import starmap
 
 from itertools import izip
 
-from numba.typesystem import basetypes
-from numba.minivect import minitypes
+from numba import typesystem
+from numba.typesystem import types
 
 __all__ = [ 'typeset', 'numeric', 'integral', 'floating', 'complextypes' ]
 
 #----------------------------------------------------------------------------
 # Signature matching
 #----------------------------------------------------------------------------
 
@@ -26,15 +26,15 @@
     table = collections.defaultdict(list)
     for i, argtype in enumerate(signature.args):
         if argtype.is_typeset:
             table[argtype].append(i)
 
     return table
 
-def get_effective_argtypes(context, signature, argtypes):
+def get_effective_argtypes(promote, signature, argtypes):
     """
     Get promoted argtypes for typeset arguments, e.g.
 
         signature = floating(floating, floating)
         argtypes = [float, double]
 
     =>
@@ -47,73 +47,73 @@
 
     for poslist in position_table.values():
         if len(poslist) > 1:
             # Find all argument types corresponding to a type set
             types = [args[i] for i in poslist]
 
             # Promote corresponding argument types
-            result_type = reduce(context.promote_types, types)
+            result_type = reduce(promote, types)
 
             # Update promotion table
             type_set = signature.args[poslist[-1]]
             promotion_table[type_set] = result_type
 
             # Build coherent argument type list
             for i in poslist:
                 args[i] = result_type
 
     return promotion_table, args
 
-def match(context, signature, argtypes):
+def match(promote, signature, argtypes):
     """
     See whether a specialization matches the given function signature.
     """
     if len(signature.args) == len(argtypes):
         promotion_table, args = get_effective_argtypes(
-                            context, signature, argtypes)
+            promote, signature, argtypes)
 
         if all(starmap(_match_argtype, izip(signature.args, args))):
             restype = signature.return_type
             restype = promotion_table.get(restype, restype)
             return restype(*args)
 
     return None
 
 
 #----------------------------------------------------------------------------
 # Type sets
 #----------------------------------------------------------------------------
 
-class typeset(minitypes.Type):
+class typeset(types.NumbaType):
     """
     Holds a set of types that can be used to specify signatures for
     type inference.
     """
 
-    is_typeset = True
+    typename = "typeset"
+    argnames = ["types", "name"]
+    defaults = {"name": None}
+    flags = ["object"]
 
-    def __init__(self, types, name=None):
-        super(typeset, self).__init__()
-
-        self.types = frozenset(types)
-        self.name = name
+    def __init__(self, types, name):
+        super(typeset, self).__init__(frozenset(types), name)
         self.first_type = types[0]
 
         self._from_argtypes = {}
         for type in types:
             if type.is_function:
                 self._from_argtypes[type.args] = type
 
-    def find_match(self, context, argtypes):
+    def find_match(self, promote, argtypes):
         argtypes = tuple(argtypes)
         if argtypes in self._from_argtypes:
             return self._from_argtypes[argtypes]
 
         for type in self.types:
-            signature = match(context, type, argtypes)
+            signature = match(promote, type, argtypes)
             if signature:
                 return signature
 
         return None
 
     def __iter__(self):
         return iter(self.types)
@@ -121,11 +121,11 @@
     def __repr__(self):
         return "typeset(%s, ...)" % (self.first_type,)
 
     def __hash__(self):
         return hash(id(self))
 
 
-numeric = typeset(minitypes.numeric)
-integral = typeset(minitypes.integral)
-floating = typeset(minitypes.floating)
-complextypes = typeset(minitypes.complextypes)
+numeric = typeset(typesystem.numeric)
+integral = typeset(typesystem.integral)
+floating = typeset(typesystem.floating)
+complextypes = typeset(typesystem.complextypes)
```

### Comparing `numba-0.8.1/numba/typesystem/__init__.py` & `numba-0.9.0/numba/typesystem/__init__.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 
-from numba.minivect.minitypes import *
-from numba.minivect.minitypes import (FunctionType)
-
-from .basetypes import *
+from .types import *
+from .itypesystem import *
 from .closuretypes import *
-from .ssatypes import *
 from .templatetypes import *
-from .containertypes import *
-from .typemapper import *
-from .typeutils import *
+from numba.exttypes.types.extensiontype import *
+from numba.exttypes.types.methods import *
 
-from .shorthands import *
+from . import numbatypes
+from .numbatypes import *
 
+from .ssatypes import *
 # from typeset import *
 from .typematch import *
 
-__all__ = minitypes.__all__ + [
-    'O', 'b1', 'i1', 'i2', 'i4', 'i8', 'u1', 'u2', 'u4', 'u8',
-    'f4', 'f8', 'f16', 'c8', 'c16', 'c32', 'template',
-]
+from .universe import *
+from .defaults import *
+from .typeutils import *
+
+__all__ = numbatypes.__all__
```

### Comparing `numba-0.8.1/numba/symtab.py` & `numba-0.9.0/numba/symtab.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 class Variable(object):
     """
     Variables placed on the stack. They allow an indirection
     so, that when used in an operation, the correct LLVM type can be inserted.
 
     Attributes:
-        type: the Numba type (see numba.typesystem and minivect/minitypes)
+        type: the Numba type (see numba.typesystem)
         is_local/is_global/is_constant
         name: name of local or global
         lvalue: LLVM Value
         state: state passed from one stage to the next
     """
 
     _type = None
@@ -133,18 +133,18 @@
         return self._deferred_type
 
     def _type_get(self):
         return self._type
 
     def _type_set(self, type):
         assert not (self.type and type is None)
-        from numba.minivect import minitypes
+        from numba import typesystem
         if type is None:
             print('Setting None type!')
-        elif not isinstance(type, minitypes.Type):
+        elif not isinstance(type, typesystem.Type):
             print(type)
         self._type = type
 
     # type = property(_type_get, _type_set)
 
     @classmethod
     def from_variable(cls, variable, **kwds):
```

### Comparing `numba-0.8.1/numba/_ext.c` & `numba-0.9.0/numba/_ext.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/types/extensiontype.py` & `numba-0.9.0/numba/exttypes/types/extensiontype.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,41 +1,43 @@
 # -*- coding: utf-8 -*-
 
 """
 Extension type types.
 """
 
-from numba.minivect import minitypes
+from functools import partial
 
 from numba.traits import traits, Delegate
 from numba.typesystem import NumbaType
 
 @traits
-class ExtensionType(NumbaType, minitypes.ObjectType):
+class ExtensionType(NumbaType):
     """
     Extension type Numba type.
 
     Available to users through MyExtensionType.exttype (or
     numba.typeof(MyExtensionType).
     """
 
-    is_extension = True
+    typename = "extension"
+    argnames = ["py_class"]
+    flags = ["object"]
     is_final = False
 
     methoddict = Delegate('vtab_type')
     untyped_methods = Delegate('vtab_type')
     specialized_methods = Delegate('vtab_type')
     methodnames = Delegate('vtab_type')
     add_method = Delegate('vtab_type')
 
     attributedict = Delegate('attribute_table')
     attributes = Delegate('attribute_table')
 
-    def __init__(self, py_class, **kwds):
-        super(ExtensionType, self).__init__(**kwds)
+    def __init__(self, py_class):
+        super(ExtensionType, self).__init__(py_class)
         assert isinstance(py_class, type), ("Must be a new-style class "
                                             "(inherit from 'object')")
         self.name = py_class.__name__
         self.py_class = py_class
         self.extclass = None
 
         self.symtab = {}  # attr_name -> attr_type
@@ -51,42 +53,36 @@
 
     def compute_offsets(self, py_class):
         from numba.exttypes import extension_types
 
         self.vtab_offset = extension_types.compute_vtab_offset(py_class)
         self.attr_offset = extension_types.compute_attrs_offset(py_class)
 
-
 # ______________________________________________________________________
 # @jit
 
-class JitExtensionType(ExtensionType):
+class jit_exttype(ExtensionType):
     "Type for @jit extension types"
 
-    is_jit_extension = True
-
     def __repr__(self):
         return "<JitExtension %s>" % self.name
 
     def __str__(self):
         if self.attribute_table:
             return "<JitExtension %s(%s)>" % (
                     self.name, self.attribute_table.strtable())
         return repr(self)
 
 # ______________________________________________________________________
 # @autojit
 
-class AutojitExtensionType(ExtensionType):
+class autojit_exttype(ExtensionType):
     "Type for @autojit extension types"
 
-    is_autojit_extension = True
-
     def __repr__(self):
         return "<AutojitExtension %s>" % self.name
 
     def __str__(self):
         if self.attribute_table:
             return "<AutojitExtension %s(%s)>" % (
                     self.name, self.attribute_table.strtable())
         return repr(self)
-
```

### Comparing `numba-0.8.1/numba/exttypes/types/methods.py` & `numba-0.9.0/numba/exttypes/types/methods.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,53 +1,43 @@
 # -*- coding: utf-8 -*-
 
 """
 Extension method types.
 """
 
 from __future__ import print_function, division, absolute_import
-
-from numba.typesystem import *
+from numba.typesystem import types, numbatypes
 
 #------------------------------------------------------------------------
 # Extension Method Types
 #------------------------------------------------------------------------
 
-class ExtMethodType(NumbaType, minitypes.FunctionType):
-    """
-    Extension method type, a FunctionType plus the following fields:
-
-        is_class_method: is classmethod?
-        is_static_method: is staticmethod?
-        is_bound_method: is bound method?
-    """
-
-    is_extension_method = True
-
-    def __init__(self, return_type, args, name=None,
-                 is_class=False, is_static=False, **kwds):
-        super(ExtMethodType, self).__init__(return_type, args, name, **kwds)
-
-        self.is_class_method = is_class
-        self.is_static_method = is_static
-        self.is_bound_method = not (is_class or is_static)
-
-class AutojitMethodType(NumbaType):
-
-    is_autojit_method = True
+class ExtMethodType(types.function):
+    typename = "extmethod"
+    argnames = ["return_type", "args", ("name", None), ("is_vararg", False),
+                ("is_class_method", False), ("is_static_method", False)]
+    flags = ["function", "object"]
+
+    @property
+    def is_bound_method(self):
+        return not (self.is_class_method or self.is_static_method)
+
+class AutojitMethodType(types.NumbaType):
+    typename = "autojit_extmethod"
+    flags = ["object"]
 
 #------------------------------------------------------------------------
 # Method Signature Comparison
 #------------------------------------------------------------------------
 
 def drop_self(type):
     if type.is_static_method or type.is_class_method:
         return type.args
 
-    assert len(type.args) >= 1 and type.args[0].is_extension
+    assert len(type.args) >= 1 and type.args[0].is_extension, type
     return type.args[1:]
 
 def equal_signature_args(t1, t2):
     """
     Compare method signatures without regarding the 'self' type (which is
     set to the base extension type in the base class, and the derived
     extension type in the derived class).
@@ -56,7 +46,10 @@
             t1.is_class_method == t2.is_class_method and
             t1.is_bound_method == t2.is_bound_method and
             drop_self(t1) == drop_self(t2))
 
 def equal_signatures(t1, t2):
     return (equal_signature_args(t1, t2) and
             t1.return_type == t2.return_type)
+
+def extmethod_to_function(ty):
+    return numbatypes.function(ty.return_type, ty.args, ty.name)
```

### Comparing `numba-0.8.1/numba/exttypes/validators.py` & `numba-0.9.0/numba/exttypes/validators.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/methodtable.py` & `numba-0.9.0/numba/exttypes/methodtable.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/autojitmeta.py` & `numba-0.9.0/numba/exttypes/autojitmeta.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/ordering.py` & `numba-0.9.0/numba/exttypes/ordering.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/attributetable.py` & `numba-0.9.0/numba/exttypes/attributetable.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,22 +4,22 @@
 Extension attribute table type. Supports ordered (struct) fields, or
 unordered (hash-based) fields.
 """
 
 from __future__ import print_function, division, absolute_import
 
 import numba
-from numba.typesystem import NumbaType, is_obj
+from numba.typesystem import is_obj
 from numba.exttypes import ordering
 
 #------------------------------------------------------------------------
 # Extension Attributes Type
 #------------------------------------------------------------------------
 
-class AttributeTable(NumbaType):
+class AttributeTable(object):
     """
     Type for extension type attributes.
     """
 
     def __init__(self, py_class, parents):
         self.py_class = py_class
```

### Comparing `numba-0.8.1/numba/exttypes/extension_types.pyx` & `numba-0.9.0/numba/exttypes/extension_types.pyx`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_extension_methods.py` & `numba-0.9.0/numba/exttypes/tests/test_extension_methods.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_extension_types.py` & `numba-0.9.0/numba/exttypes/tests/test_extension_types.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_extension_inheritance.py` & `numba-0.9.0/numba/exttypes/tests/test_extension_inheritance.py`

 * *Files 2% similar despite different names*

```diff
@@ -110,14 +110,13 @@
     assert Derived(10.0).py_method() == 10.0
 
     assert Derived(4.0).method() == 8.0
     assert Derived(4.0).getvalue() == 8.0
 
     obj = Derived(4.0)
     obj.value2 = 3.0
-    assert obj.method() == 12.0
+    result = obj.method()
+    assert result == 12.0, result
 
 
 if __name__ == '__main__':
-    test_baseclass(autojit)
-    # test_derivedclass(autojit)
     main()
```

### Comparing `numba-0.8.1/numba/exttypes/tests/autojit/test_extension_class_specializations.py` & `numba-0.9.0/numba/exttypes/tests/autojit/test_extension_class_specializations.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/autojit/test_unspecialized_extension_methods.py` & `numba-0.9.0/numba/exttypes/tests/autojit/test_unspecialized_extension_methods.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/autojit/test_unannotated_extension_methods.py` & `numba-0.9.0/numba/exttypes/tests/autojit/test_unannotated_extension_methods.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_extension_attributes.py` & `numba-0.9.0/numba/exttypes/tests/test_extension_attributes.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_type_recognition.py` & `numba-0.9.0/numba/exttypes/tests/test_type_recognition.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_extension_sizeof.py` & `numba-0.9.0/numba/exttypes/tests/test_extension_sizeof.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/tests/test_vtables.py` & `numba-0.9.0/numba/exttypes/tests/test_vtables.py`

 * *Files 9% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 
 from __future__ import print_function, division, absolute_import
 
 import itertools
 
 import numba as nb
 from numba import *
-from numba.minivect.minitypes import FunctionType
+from numba import typesystem
 from numba.exttypes import virtual
 from numba.exttypes import methodtable
 from numba.exttypes.signatures import Method
 from numba.testing.test_support import parametrize, main
 
 #------------------------------------------------------------------------
 # Signature enumeration
@@ -40,19 +40,19 @@
 
 all_types = types + array_types
 
 def method(func, name, sig):
     return Method(func, name, sig, False, False)
 
 make_methods1 = lambda: [
-    method(myfunc1, 'method', FunctionType(argtype, [argtype]))
+    method(myfunc1, 'method', typesystem.function(argtype, [argtype]))
         for argtype in all_types]
 
 make_methods2 = lambda: [
-    method(myfunc2, 'method', FunctionType(argtype1, [argtype1, argtype2]))
+    method(myfunc2, 'method', typesystem.function(argtype1, [argtype1, argtype2]))
         for argtype1, argtype2 in itertools.product(all_types, all_types)]
 
 #------------------------------------------------------------------------
 # Table building
 #------------------------------------------------------------------------
 
 def make_table(methods):
```

### Comparing `numba-0.8.1/numba/exttypes/entrypoints.py` & `numba-0.9.0/numba/exttypes/entrypoints.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/utils.py` & `numba-0.9.0/numba/exttypes/utils.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/autojitclass.py` & `numba-0.9.0/numba/exttypes/autojitclass.py`

 * *Files 1% similar despite different names*

```diff
@@ -66,22 +66,18 @@
 
         We need to store a PyCustomSlots_Table ** in the object to allow
         the producer of the table to replace the table with a new table
         for all live objects (e.g. by adding a specialization for
         an autojit method).
 """
 
-import copy
-from functools import partial
-
 from numba import error
 from numba import pipeline
-from numba import typesystem
 from numba import numbawrapper
-from numba.minivect import minitypes
+from numba import typesystem
 
 from numba.exttypes import types as etypes
 from numba.exttypes import utils
 from numba.exttypes import virtual
 from numba.exttypes import signatures
 from numba.exttypes import validators
 from numba.exttypes import compileclass
@@ -320,15 +316,15 @@
     class to the specialized class. E.g.
 
         m = A.method
         m(A(10.0))      # Delegate to A[double].method
     """
     class_dict = vars(py_class)
     for name, func in class_dict.iteritems():
-        if isinstance(func, (minitypes.Function, staticmethod, classmethod)):
+        if isinstance(func, (typesystem.Function, staticmethod, classmethod)):
             method = signatures.process_signature(func, name)
             if method.is_class or method.is_static:
                 # Class or static method: use the pure Python function wrapped
                 # in classmethod()/staticmethod()
                 method.wrapper_func = method.py_func
                 new_func = method.get_wrapper()
             else:
@@ -394,15 +390,15 @@
     Inovked when calling the wrapped class to compile a specialized
     new extension type.
     """
     # TODO: Remove argtypes! Partial environment!
 
     flags.pop('llvm_module', None)
 
-    ext_type = etypes.AutojitExtensionType(py_class)
+    ext_type = etypes.autojit_exttype(py_class)
 
     class_dict = dict(utils.get_class_dict(py_class))
 
     extension_compiler = AutojitExtensionCompiler(
         env, py_class, class_dict, ext_type, flags,
         signatures.AutojitMethodMaker(argtypes),
         compileclass.AttributesInheriter(),
```

### Comparing `numba-0.8.1/numba/exttypes/signatures.py` & `numba-0.9.0/numba/exttypes/signatures.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,16 +8,14 @@
 
 import types
 
 import numba
 from numba import *
 from numba import error
 from numba import typesystem
-from numba.exttypes import types as etypes
-from numba.minivect import minitypes
 
 #------------------------------------------------------------------------
 # Parse method signatures
 #------------------------------------------------------------------------
 
 class Method(object):
     """
@@ -106,17 +104,17 @@
         else:
             return None
 
     def make_method_type(self, method):
         "Create a method type for the given Method and declared signature"
         restype = method.signature.return_type
         argtypes = method.signature.args
-        signature = etypes.ExtMethodType(
+        signature = typesystem.ExtMethodType(
                     return_type=restype, args=argtypes, name=method.name,
-                    is_class=method.is_class, is_static=method.is_static)
+                    is_class_method=method.is_class, is_static_method=method.is_static)
         return signature
 
 def has_known_signature(method):
     argcount = method.py_func.__code__.co_argcount
     return ((method.is_static and argcount == 0) or
             (not method.is_static and argcount == 1))
 
@@ -190,15 +188,15 @@
             if signature is None:
                 method_maker.no_signature(method)
 
             method = Method(method, method_name, signature,
                             is_class, is_static)
             return method
 
-        elif isinstance(method, minitypes.Function):
+        elif isinstance(method, typesystem.Function):
             # @double(...)
             # def func(self, ...): ...
             signature = method.signature
             method = method.py_func
 
         else:
             # Process staticmethod and classmethod
```

### Comparing `numba-0.8.1/numba/exttypes/compileclass.py` & `numba-0.9.0/numba/exttypes/compileclass.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 
 from __future__ import print_function, division, absolute_import
 
 from numba import pipeline
 from numba import symtab
-from numba.minivect import minitypes
+from numba import typesystem
 
 from numba.exttypes import signatures
 from numba.exttypes import utils
 from numba.exttypes import extension_types
 from numba.exttypes import methodtable
 from numba.exttypes import attributetable
 from numba.exttypes.types import methods
@@ -123,16 +123,16 @@
 
         # Verify signature after type inference with registered
         # (user-declared) signature
         method.signature = methods.ExtMethodType(
             method.signature.return_type,
             method.signature.args,
             method.name,
-            is_class=method.is_class,
-            is_static=method.is_static)
+            is_class_method=method.is_class,
+            is_static_method=method.is_static)
 
         self.ext_type.add_method(method)
 
     def type_infer_init_method(self):
         initfunc = self.class_dict.get('__init__', None)
         if initfunc is None:
             return
@@ -314,15 +314,15 @@
         @jit
         class Foo(object):
 
             attr = double
     """
     table = ext_type.attribute_table
     for name, value in class_dict.iteritems():
-        if isinstance(value, minitypes.Type):
+        if isinstance(value, typesystem.Type):
             table.attributedict[name] = value
 
 def build_extension_symtab(ext_type):
     """
     Create symbol table for all attributes of the extension type. These
     are Variables which are used by the type inferencer and used to
     type check attribute assignments.
```

### Comparing `numba-0.8.1/numba/exttypes/variable.py` & `numba-0.9.0/numba/exttypes/variable.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/exttypes/virtual.py` & `numba-0.9.0/numba/exttypes/virtual.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,14 @@
     https://github.com/numfocus/sep/blob/master/sep201.rst
 """
 
 import ctypes
 
 import numba
 from numba.typesystem import *
-from numba.minivect import minitypes
 from numba.exttypes import ordering
 from numba.exttypes import extension_types
 
 #------------------------------------------------------------------------
 # Virtual Method Table Interface
 #------------------------------------------------------------------------
 
@@ -117,27 +116,27 @@
     ('m_g', uint64),
     ('entries', PyCustomSlots_Entry.pointer()),
     ('n', uint16),
     ('b', uint16),
     ('r', uint8),
     ('reserved', uint8),
     # actually: uint16[b], 'b' trailing displacements
-    # ('d', minitypes.CArrayType(uint16, 0)), #0xffff)),
+    # ('d', numba.carray(uint16, 0)), #0xffff)),
     # ('entries_mem', PyCustomSlot_Entry[n]), # 'n' trailing customslot entries
 ])
 
 # ______________________________________________________________________
 # Hash-table building
 
 def initialize_interner():
     from numba.pyextensibletype.extensibletype import intern
     intern.global_intern_initialize()
 
 def sep201_signature_string(functype, name):
-    functype = minitypes.FunctionType(functype.return_type, functype.args, name)
+    functype = numba.function(functype.return_type, functype.args, name)
     return str(functype)
 
 def hash_signature(functype, name):
     from numba.pyextensibletype.extensibletype import methodtable
 
     initialize_interner()
     sep201_hasher = methodtable.Hasher()
```

### Comparing `numba-0.8.1/numba/exttypes/jitclass.py` & `numba-0.9.0/numba/exttypes/jitclass.py`

 * *Files 2% similar despite different names*

```diff
@@ -90,15 +90,16 @@
 def create_extension(env, py_class, flags):
     """
     Compile an extension class given the NumbaEnvironment and the Python
     class that contains the functions that are to be compiled.
     """
     flags.pop('llvm_module', None)
 
-    ext_type = etypes.JitExtensionType(py_class)
+    # ext_type = etypes.jit_exttype(py_class)
+    ext_type = typesystem.jit_exttype(py_class)
 
     extension_compiler = JitExtensionCompiler(
         env, py_class, dict(vars(py_class)), ext_type, flags,
         signatures.JitMethodMaker(),
         compileclass.AttributesInheriter(),
         compileclass.Filterer(),
         JitAttributeBuilder(),
```

### Comparing `numba-0.8.1/numba/normalize.py` & `numba-0.9.0/numba/normalize.py`

 * *Files 12% similar despite different names*

```diff
@@ -90,15 +90,15 @@
             'ifs' represent a chain of ANDs
         """
         assert len(node.generators) > 0
 
         # Create innermost body, i.e. list.append(expr)
         # TODO: size hint for PyList_New
         list_create = ast.List(elts=[], ctx=ast.Load())
-        list_create.type = typesystem.object_ # typesystem.ListType()
+        list_create.type = typesystem.object_ # typesystem.list_()
         list_create = nodes.CloneableNode(list_create)
         list_value = nodes.CloneNode(list_create)
         list_append = ast.Attribute(list_value, "append", ast.Load())
         append_call = ast.Call(func=list_append, args=[node.elt],
                                keywords=[], starargs=None, kwargs=None)
 
         # Build up the loops from inwards to outwards
@@ -142,14 +142,37 @@
 
         bin_op = ast.BinOp(rhs_target, node.op, node.value)
         assignment = ast.Assign([target], bin_op)
         assignment.inplace_op = node.op
         return self.visit(assignment)
 
 
+    ######## Sync with cf2 branch in validators.py ###########
+
+    def visit_With(self, node):
+        node.context_expr = self.visit(node.context_expr)
+        if node.optional_vars:
+            raise error.NumbaError(
+                node.context_expr,
+                "Only 'with python' and 'with nopython' is "
+                "supported at this moment")
+
+        self.visitlist(node.body)
+        return node
+
+
+    def visit_For(self, node):
+        if not isinstance(node.target, (ast.Name, ast.Attribute)):
+            raise error.NumbaError(
+                node.target, "Only a single target iteration variable is "
+                             "supported at the moment")
+
+        self.visitchildren(node)
+        return node
+
 #------------------------------------------------------------------------
 # Nodes
 #------------------------------------------------------------------------
 
 class FuncDefExprNode(nodes.Node):
     """
     Wraps an inner function node until the closure code kicks in.
```

### Comparing `numba-0.8.1/numba/random/_rng_generated.py` & `numba-0.9.0/numba/random/_rng_generated.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/random/__generate_rng.py` & `numba-0.9.0/numba/random/__generate_rng.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/random/random.py` & `numba-0.9.0/numba/random/random.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/_gufunc.c` & `numba-0.9.0/numba/vectorize/_gufunc.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/_common.py` & `numba-0.9.0/numba/vectorize/_common.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 import numpy as np
 
+import numba
 from numba import decorators
 from numba.codegen.llvmcontext import LLVMContextManager
-from numba.minivect import minitypes
 from . import _internal
 
 try:
     ptr_t = long
 except NameError:
     ptr_t = int
     assert False, "Have not check this yet" # Py3.0?
@@ -120,15 +120,15 @@
 
     def _get_tys_list(self):
         types_lists = []
         for numba_func in self.translates:
             dtype_nums = []
             types_lists.append(dtype_nums)
             for arg_type in self.get_argtypes(numba_func):
-                dtype = minitypes.map_minitype_to_dtype(arg_type)
+                dtype = arg_type.get_dtype()
                 dtype_nums.append(dtype)
 
         return types_lists
 
     def _get_lfunc_list(self):
         return [t.lfunc for t in self.translates]
```

### Comparing `numba-0.8.1/numba/vectorize/_internal.h` & `numba-0.9.0/numba/vectorize/_internal.h`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/basic.py` & `numba-0.9.0/numba/vectorize/basic.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/_internal.c` & `numba-0.9.0/numba/vectorize/_internal.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/_ufunc.c` & `numba-0.9.0/numba/vectorize/_ufunc.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/vectorize/__init__.py` & `numba-0.9.0/numba/vectorize/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,18 +1,21 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 __all__ = [
            'vectorize',
            'Vectorize',
            'BasicVectorize',
            'BasicASTVectorize',
+           'GUVectorize',
            ]
 
 
 from .basic import BasicVectorize, BasicASTVectorize
+from .gufunc import GUFuncVectorize as GUVectorize
+
 from numba.utils import process_sig
 import warnings
 
 #_bytecode_vectorizers = {
 #    'cpu': BasicVectorize,
 #}
 
@@ -56,23 +59,21 @@
 
         func: the function to vectorize
         backend: 'ast'
         Default: 'ast'
         target: 'basic'
         Default: 'basic'
         """
-    assert backend in _vectorizers, tuple(backends)
+    assert backend in _vectorizers, tuple(_vectorizers)
     targets = _vectorizers[backend]
     assert target in targets, tuple(targets)
     if target in targets:
         return targets[target](func)
     else: # fall back
-        warnings.warn("fallback to bytecode vectorizer")
-        # Use the default bytecode backend
-        return _bytecode_vectorizers[target](func)
+        raise NotImplementedError
 
 def vectorize(signatures, backend='ast', target='cpu'):
     def _vectorize(fn):
         vect = Vectorize(fn, backend=backend, target=target)
         for sig in signatures:
             kws = _prepare_sig(sig)
             vect.add(**kws)
```

### Comparing `numba-0.8.1/numba/odict.py` & `numba-0.9.0/numba/odict.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/function_util.py` & `numba-0.9.0/numba/function_util.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
-from numba.external import utility
 
 def external_call(context, llvm_module, name, args=(), temp_name=None):
     extfn = context.external_library.get(name)
     return external_call_func(context, llvm_module, extfn, args, temp_name)
 
 def utility_call(context, llvm_module, name, args=(), temp_name=None):
     extfn = context.utility_library.get(name)
```

### Comparing `numba-0.8.1/numba/wrapping/compiler.py` & `numba-0.9.0/numba/wrapping/compiler.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import inspect
 
 from numba import typesystem
 import numba.pipeline
 from numba.exttypes import virtual
-from numba.exttypes import signatures
 import numba.exttypes.entrypoints
 
 import numba.decorators
 
 def resolve_argtypes(env, py_func, template_signature,
                      args, kwargs, translator_kwargs):
     """
@@ -28,15 +27,15 @@
             arguments = 'arguments'
         raise TypeError("%s() takes exactly %d %s (%d given)" % (
                                 py_func.__name__, argcount,
                                 arguments, len(args)))
 
     return_type = None
     argnames = inspect.getargspec(py_func).args
-    argtypes = [env.context.typemapper.from_python(x) for x in args]
+    argtypes = [typesystem.numba_typesystem.typeof(x) for x in args]
 
     if template_signature is not None:
         template_context, signature = typesystem.resolve_templates(
                 locals_dict, template_signature, argnames, argtypes)
         return_type = signature.return_type
         argtypes = list(signature.args)
 
@@ -84,15 +83,16 @@
         compiled_function = dec(self.py_func)
         return compiled_function
 
 class ClassCompiler(Compiler):
 
     def resolve_argtypes(self, args, kwargs):
         assert not kwargs
-        argtypes = map(self.env.context.typemapper.from_python, args)
+        # argtypes = map(self.env.crnt.typesystem.typeof, args)
+        argtypes = map(numba.typeof, args) # TODO: allow registering a type system and using it here
         signature = typesystem.function(None, argtypes)
         return signature
 
     def compile(self, signature):
         py_class = self.py_func
         return numba.exttypes.entrypoints.autojit_extension_class(
             self.env, py_class, self.flags, signature.args)
```

### Comparing `numba-0.8.1/numba/external/utilities/virtuallookup.c` & `numba-0.9.0/numba/external/utilities/virtuallookup.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/external/utilities/utilities.c` & `numba-0.9.0/numba/external/utilities/utilities.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/external/utilities/type_conversion.c` & `numba-0.9.0/numba/external/utilities/type_conversion.c`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/external/external.py` & `numba-0.9.0/numba/external/external.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 """
 This module adds a way to declare external functions.
 
 See numba.function_util on how to call them.
 """
 from __future__ import print_function, division, absolute_import
 
-from numba.minivect import minitypes
+import numba
 
 class ExternalFunction(object):
     _attributes = ('func_name', 'arg_types', 'return_type', 'is_vararg',
                    'check_pyerr_occurred')
     func_name = None
     arg_types = None
     return_type = None
@@ -37,17 +37,17 @@
             for k, v in kwargs.items():
                 if k not in self._attributes:
                     raise TypeError("Invalid keyword arg %s -> %s" % (k, v))
         vars(self).update(kwargs)
 
     @property
     def signature(self):
-        return minitypes.FunctionType(return_type=self.return_type,
-                                      args=self.arg_types,
-                                      is_vararg=self.is_vararg)
+        return numba.function(return_type=self.return_type,
+                              args=self.arg_types,
+                              is_vararg=self.is_vararg)
 
     @property
     def name(self):
         if self.func_name is None:
             return type(self).__name__
         else:
             return self.func_name
```

### Comparing `numba-0.8.1/numba/external/pyapi.py` & `numba-0.9.0/numba/external/pyapi.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,16 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
+
+from numba import PY3
+
 from .external import ExternalFunction
-from numba import *
+from numba.typesystem import *
+
+c_string_type = char.pointer()
 
 class ofunc(ExternalFunction):
     arg_types = [object_]
     return_type = object_
 
 class Py_IncRef(ofunc):
     # TODO: rewrite calls to Py_IncRef/Py_DecRef to direct integer
```

### Comparing `numba-0.8.1/numba/external/libc.py` & `numba-0.9.0/numba/external/libc.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,14 @@
 # -*- coding: utf-8 -*-
 from __future__ import print_function, division, absolute_import
 from .external import ExternalFunction
 from numba import *
 
+c_string_type = char.pointer()
+
 class printf(ExternalFunction):
     arg_types = [void.pointer()]
     return_type = int32
     is_vararg = True
 
 class puts(ExternalFunction):
     arg_types = [c_string_type]
```

### Comparing `numba-0.8.1/numba/external/utility.py` & `numba-0.9.0/numba/external/utility.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/external/__init__.py` & `numba-0.9.0/numba/external/__init__.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/stdio_util.py` & `numba-0.9.0/numba/stdio_util.py`

 * *Files identical despite different names*

### Comparing `numba-0.8.1/numba/numbawrapper.pyx` & `numba-0.9.0/numba/numbawrapper.pyx`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 cimport numpy as cnp
 
 import types
 import ctypes
 
 import numba
 from numba import error
-from numba.minivect import minitypes
+from numba.typesystem import itypesystem
 from numba.support import ctypes_support, cffi_support
 
 import numpy as np
 
 
 cdef extern from *:
     ctypedef struct PyTypeObject:
@@ -74,15 +74,15 @@
 #------------------------------------------------------------------------
 
 support_classes = (ctypes_support.CData,)
 if cffi_support.ffi is not None:
     support_classes += (cffi_support.cffi_func_type,)
 
 cdef tuple hash_on_value_types = (
-    minitypes.Type,
+    itypesystem.Type,
     np.ufunc,
     np.dtype,
     np.generic,
     NumbaWrapper,
     types.FunctionType,
     types.BuiltinFunctionType,
     types.MethodType,
@@ -99,15 +99,15 @@
 # @jit function creation
 #------------------------------------------------------------------------
 
 cdef class NumbaCompiledWrapper(NumbaWrapper):
     """
     Temporary numba wrapper function for @jit, only used for recursion.
 
-        signature: minitype FunctionType signature
+        signature: minitype function signature
         lfunc: LLVM function
     """
 
     cdef public object lfunc, signature, wrapper, lfunc_pointer
 
     def __init__(self, py_func, signature, lfunc):
         super(NumbaCompiledWrapper, self).__init__(py_func)
```

### Comparing `numba-0.8.1/numba/__init__.py` & `numba-0.9.0/numba/__init__.py`

 * *Files 22% similar despite different names*

```diff
@@ -9,18 +9,18 @@
 # type inferer
 from numba.special import *
 
 import os
 import sys
 import logging
 
-from numba import utils, typesystem
-
 PY3 = sys.version_info[0] == 3
 
+from numba import utils, typesystem
+
 def get_include():
     numba_root = os.path.dirname(os.path.abspath(__file__))
     return os.path.join(numba_root, "include")
 
 # NOTE: Be sure to keep the logging level commented out before commiting.  See:
 #   https://github.com/numba/numba/issues/31
 # A good work around is to make your tests handle a debug flag, per
@@ -57,21 +57,23 @@
     root.addHandler(hldr)
     root.propagate = False # do not propagate to the root logger
 
 _config_logger()
 
 
 from . import special
+from numba.typesystem import template
 from numba.typesystem import *
-from numba.minivect.minitypes import FunctionType
+from numba.typesystem import struct_ as struct # don't export this in __all__
+from numba.typesystem import function
 from numba.error import *
 
 from numba.containers.typedlist import typedlist
 from numba.containers.typedtuple import typedtuple
-from numba.typesystem import map_dtype
+from numba.typesystem.numpy_support import map_dtype
 from numba.type_inference.module_type_inference import (is_registered,
                                                         register,
                                                         register_inferer,
                                                         get_inferer,
                                                         register_unbound,
                                                         register_callable)
 from numba.typesystem.typeset import *
```

### Comparing `numba-0.8.1/README.md` & `numba-0.9.0/README.md`

 * *Files identical despite different names*

