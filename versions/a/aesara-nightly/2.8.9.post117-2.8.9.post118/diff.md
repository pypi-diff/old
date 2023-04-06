# Comparing `tmp/aesara-nightly-2.8.9.post117.tar.gz` & `tmp/aesara-nightly-2.8.9.post118.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aesara-nightly-2.8.9.post117.tar", last modified: Tue Jan 10 03:31:06 2023, max compression
+gzip compressed data, was "aesara-nightly-2.8.9.post118.tar", last modified: Wed Jan 18 20:56:56 2023, max compression
```

## Comparing `aesara-nightly-2.8.9.post117.tar` & `aesara-nightly-2.8.9.post118.tar`

### file list

```diff
@@ -1,502 +1,502 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.926043 aesara-nightly-2.8.9.post117/
--rw-r--r--   0 runner    (1001) docker     (123)      809 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/DESCRIPTION.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2515 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-01-10 03:31:06.926043 aesara-nightly-2.8.9.post117/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4112 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/
--rw-r--r--   0 runner    (1001) docker     (123)     5760 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      252 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/assert_op.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/bin/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/bin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4080 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/bin/aesara_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     6057 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/breakpoint.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/compile/
--rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    37547 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/builders.py
--rw-r--r--   0 runner    (1001) docker     (123)     9954 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/compiledir.py
--rw-r--r--   0 runner    (1001) docker     (123)     2041 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/compilelock.py
--rw-r--r--   0 runner    (1001) docker     (123)    85453 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/debugmode.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/compile/function/
--rw-r--r--   0 runner    (1001) docker     (123)    13377 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/function/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22099 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/function/pfunc.py
--rw-r--r--   0 runner    (1001) docker     (123)    71335 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/function/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     9102 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/io.py
--rw-r--r--   0 runner    (1001) docker     (123)    17823 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/mode.py
--rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/monitormode.py
--rw-r--r--   0 runner    (1001) docker     (123)     8326 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/nanguardmode.py
--rw-r--r--   0 runner    (1001) docker     (123)     9969 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)    59779 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/profiling.py
--rw-r--r--   0 runner    (1001) docker     (123)     7202 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/compile/sharedvalue.py
--rw-r--r--   0 runner    (1001) docker     (123)    46230 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/configdefaults.py
--rw-r--r--   0 runner    (1001) docker     (123)    22530 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/configparser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/d3viz/
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/d3viz/css/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/css/d3-context-menu.css
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/css/d3viz.css
--rw-r--r--   0 runner    (1001) docker     (123)     3830 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/d3viz.py
--rw-r--r--   0 runner    (1001) docker     (123)    11843 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/formatting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.870043 aesara-nightly-2.8.9.post117/aesara/d3viz/html/
--rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/html/template.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.874043 aesara-nightly-2.8.9.post117/aesara/d3viz/js/
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3-context-menu.js
--rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3.v3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    23208 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3viz.js
--rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/js/dagre-d3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/d3viz/js/graphlib-dot.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    87043 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/gradient.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.874043 aesara-nightly-2.8.9.post117/aesara/graph/
--rw-r--r--   0 runner    (1001) docker     (123)      505 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    59820 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    31374 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/destroyhandler.py
--rw-r--r--   0 runner    (1001) docker     (123)    26449 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/features.py
--rw-r--r--   0 runner    (1001) docker     (123)    35817 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/fg.py
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/kanren.py
--rw-r--r--   0 runner    (1001) docker     (123)     1150 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/null_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    25075 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      793 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/opt_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      786 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/optdb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.874043 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   114248 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    19934 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/db.py
--rw-r--r--   0 runner    (1001) docker     (123)     3035 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/kanren.py
--rw-r--r--   0 runner    (1001) docker     (123)     7239 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/unify.py
--rw-r--r--   0 runner    (1001) docker     (123)     9148 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/rewriting/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7865 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/sched.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/toolbox.py
--rw-r--r--   0 runner    (1001) docker     (123)     8926 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/type.py
--rw-r--r--   0 runner    (1001) docker     (123)      243 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/unify.py
--rw-r--r--   0 runner    (1001) docker     (123)    12164 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/graph/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    29070 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/ifelse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.874043 aesara-nightly-2.8.9.post117/aesara/link/
--rw-r--r--   0 runner    (1001) docker     (123)        3 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23890 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.878043 aesara-nightly-2.8.9.post117/aesara/link/c/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    72624 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.878043 aesara-nightly-2.8.9.post117/aesara/link/c/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)      706 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/c_code/aesara_mod_helper.h
--rw-r--r--   0 runner    (1001) docker     (123)    35583 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/c_code/lazylinker_c.c
--rw-r--r--   0 runner    (1001) docker     (123)   112626 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/cmodule.py
--rw-r--r--   0 runner    (1001) docker     (123)     4183 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/cutils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/cvm.py
--rw-r--r--   0 runner    (1001) docker     (123)      402 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    20016 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/interface.py
--rw-r--r--   0 runner    (1001) docker     (123)     6641 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/lazylinker_c.py
--rw-r--r--   0 runner    (1001) docker     (123)    24725 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/op.py
--rw-r--r--   0 runner    (1001) docker     (123)    31659 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/params_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    26568 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/c/type.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.878043 aesara-nightly-2.8.9.post117/aesara/link/jax/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.878043 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/
--rw-r--r--   0 runner    (1001) docker     (123)      529 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     2945 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)     3381 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     3072 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/nlinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    10930 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/random.py
--rw-r--r--   0 runner    (1001) docker     (123)     5612 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/scalar.py
--rw-r--r--   0 runner    (1001) docker     (123)     5382 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/slinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3192 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3380 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/tensor_basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/jax_dispatch.py
--rw-r--r--   0 runner    (1001) docker     (123)      232 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/jax_linker.py
--rw-r--r--   0 runner    (1001) docker     (123)     2991 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/jax/linker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.878043 aesara-nightly-2.8.9.post117/aesara/link/numba/
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.882043 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25914 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    22249 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)     9266 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     5085 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/nlinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    12537 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/random.py
--rw-r--r--   0 runner    (1001) docker     (123)     8896 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/scalar.py
--rw-r--r--   0 runner    (1001) docker     (123)    14205 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/sparse.py
--rw-r--r--   0 runner    (1001) docker     (123)     6405 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/tensor_basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/numba/linker.py
--rw-r--r--   0 runner    (1001) docker     (123)    28718 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    50578 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/link/vm.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.882043 aesara-nightly-2.8.9.post117/aesara/misc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9672 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/check_blas.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      600 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/check_blas_many.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2410 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/check_duplicate_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     2166 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/elemwise_openmp_speedup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/elemwise_time_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/frozendict.py
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/latence_gpu_transfert.py
--rw-r--r--   0 runner    (1001) docker     (123)      921 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/may_share_memory.py
--rw-r--r--   0 runner    (1001) docker     (123)     7191 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/ordered_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     9746 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/pkl_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2292 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/misc/safe_asarray.py
--rw-r--r--   0 runner    (1001) docker     (123)    64090 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/printing.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     5838 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/raise_op.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.882043 aesara-nightly-2.8.9.post117/aesara/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/fourier.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.882043 aesara-nightly-2.8.9.post117/aesara/sandbox/linalg/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/linalg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6062 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/linalg/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/minimal.py
--rw-r--r--   0 runner    (1001) docker     (123)    14812 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/multinomial.py
--rw-r--r--   0 runner    (1001) docker     (123)    48272 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/rng_mrg.py
--rw-r--r--   0 runner    (1001) docker     (123)     8105 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/samples_MRG31k3p_12_7_5.txt
--rw-r--r--   0 runner    (1001) docker     (123)      217 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sandbox/solve.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.882043 aesara-nightly-2.8.9.post117/aesara/scalar/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   139093 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/basic_scipy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/basic_sympy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.886043 aesara-nightly-2.8.9.post117/aesara/scalar/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)   126227 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/c_code/Faddeeva.cc
--rw-r--r--   0 runner    (1001) docker     (123)     2645 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/c_code/Faddeeva.hh
--rw-r--r--   0 runner    (1001) docker     (123)    16816 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/c_code/gamma.c
--rw-r--r--   0 runner    (1001) docker     (123)    40497 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/math.py
--rw-r--r--   0 runner    (1001) docker     (123)     1851 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scalar/sharedvar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.886043 aesara-nightly-2.8.9.post117/aesara/scan/
--rw-r--r--   0 runner    (1001) docker     (123)     1931 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    50325 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.886043 aesara-nightly-2.8.9.post117/aesara/scan/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)  1108062 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/c_code/scan_perform.c
--rw-r--r--   0 runner    (1001) docker     (123)     6743 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/checkpoints.py
--rw-r--r--   0 runner    (1001) docker     (123)   140552 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    95135 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)    23996 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/scan_perform.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     3512 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/scan_perform_ext.py
--rw-r--r--   0 runner    (1001) docker     (123)    38175 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4599 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/scan/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.886043 aesara-nightly-2.8.9.post117/aesara/sparse/
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   118012 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      232 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    76908 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/rewriting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.890043 aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17297 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/sp.py
--rw-r--r--   0 runner    (1001) docker     (123)     7194 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/sp2.py
--rw-r--r--   0 runner    (1001) docker     (123)      827 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/sharedvar.py
--rw-r--r--   0 runner    (1001) docker     (123)     8073 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/type.py
--rw-r--r--   0 runner    (1001) docker     (123)      767 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/sparse/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.894043 aesara-nightly-2.8.9.post117/aesara/tensor/
--rw-r--r--   0 runner    (1001) docker     (123)     4289 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   135697 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      461 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/basic_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    98873 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/blas.py
--rw-r--r--   0 runner    (1001) docker     (123)    26486 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/blas_c.py
--rw-r--r--   0 runner    (1001) docker     (123)    68050 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/blas_headers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/blas_scipy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.894043 aesara-nightly-2.8.9.post117/aesara/tensor/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)      897 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/c_code/alt_blas_common.h
--rw-r--r--   0 runner    (1001) docker     (123)    16236 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/c_code/alt_blas_template.c
--rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/c_code/dimshuffle.c
--rw-r--r--   0 runner    (1001) docker     (123)    66688 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)    20866 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/elemwise_cgen.py
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    57998 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     7591 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/fft.py
--rw-r--r--   0 runner    (1001) docker     (123)     6603 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/fourier.py
--rw-r--r--   0 runner    (1001) docker     (123)     7737 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/inplace.py
--rw-r--r--   0 runner    (1001) docker     (123)     7242 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/io.py
--rw-r--r--   0 runner    (1001) docker     (123)       72 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/linalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    92466 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/math.py
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/math_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    22763 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nlinalg.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.894043 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   138966 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/abstract_conv.py
--rw-r--r--   0 runner    (1001) docker     (123)    75762 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    35370 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/batchnorm.py
--rw-r--r--   0 runner    (1001) docker     (123)     8902 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/blocksparse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.894043 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)    18972 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/corr3d_gemm.c
--rw-r--r--   0 runner    (1001) docker     (123)    26551 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/corr_gemm.c
--rw-r--r--   0 runner    (1001) docker     (123)     8195 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/ctc_wrapper.c
--rw-r--r--   0 runner    (1001) docker     (123)    94525 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/conv.py
--rw-r--r--   0 runner    (1001) docker     (123)     9910 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/conv3d2d.py
--rw-r--r--   0 runner    (1001) docker     (123)    40356 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/corr.py
--rw-r--r--   0 runner    (1001) docker     (123)    36145 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/corr3d.py
--rw-r--r--   0 runner    (1001) docker     (123)     8522 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/ctc.py
--rw-r--r--   0 runner    (1001) docker     (123)    35353 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/neighbours.py
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    17298 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)     5212 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/nnet/sigm.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/opt_uncanonicalize.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara/tensor/random/
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    61298 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    14370 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/opt.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15291 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/jax.py
--rw-r--r--   0 runner    (1001) docker     (123)     6730 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     9021 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/random/var.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)      384 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    42710 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    39793 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)     4846 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     3954 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/jax.py
--rw-r--r--   0 runner    (1001) docker     (123)   122924 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/math.py
--rw-r--r--   0 runner    (1001) docker     (123)    44832 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     6102 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/special.py
--rw-r--r--   0 runner    (1001) docker     (123)    63205 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     9500 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/uncanonicalize.py
--rw-r--r--   0 runner    (1001) docker     (123)    33343 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/sharedvar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara/tensor/signal/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/signal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/signal/conv.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    97512 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/signal/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)    25027 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/slinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    17849 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)    27168 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/special.py
--rw-r--r--   0 runner    (1001) docker     (123)    91237 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/subtensor_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    41042 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4090 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/type_other.py
--rw-r--r--   0 runner    (1001) docker     (123)     3211 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    36091 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/var.py
--rw-r--r--   0 runner    (1001) docker     (123)     1831 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/tensor/xlogx.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara/typed_list/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/typed_list/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18222 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/typed_list/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      780 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/typed_list/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/typed_list/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2925 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/updates.py
--rw-r--r--   0 runner    (1001) docker     (123)    13641 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      939 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/aesara/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.898043 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    12555 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-10 03:31:06.000000 aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.902043 aesara-nightly-2.8.9.post117/bin/
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/bin/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      285 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/bin/aesara-cache
--rw-r--r--   0 runner    (1001) docker     (123)      332 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/bin/aesara_cache.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.902043 aesara-nightly-2.8.9.post117/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.902043 aesara-nightly-2.8.9.post117/doc/.build/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.build/PLACEHOLDER
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.902043 aesara-nightly-2.8.9.post117/doc/.static/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.static/PLACEHOLDER
--rw-r--r--   0 runner    (1001) docker     (123)      256 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.static/fix_rtd.css
--rw-r--r--   0 runner    (1001) docker     (123)     3799 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.static/version_switch.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.902043 aesara-nightly-2.8.9.post117/doc/.templates/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.templates/PLACEHOLDER
--rw-r--r--   0 runner    (1001) docker     (123)     1409 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/.templates/layout.html
--rw-r--r--   0 runner    (1001) docker     (123)     2515 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1159 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/acknowledgement.rst
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/bcast.svg
--rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1282 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/core_development_guide.rst
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/css.inc
--rw-r--r--   0 runner    (1001) docker     (123)     8604 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/dev_start_guide.rst
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/environment.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.906043 aesara-nightly-2.8.9.post117/doc/extending/
--rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/apply.png
--rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/apply.svg
--rw-r--r--   0 runner    (1001) docker     (123)    32078 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/apply2.svg
--rw-r--r--   0 runner    (1001) docker     (123)    46604 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/creating_a_c_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6334 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/creating_a_numba_jax_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)    32993 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/creating_an_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)    22664 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/ctype.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     5513 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/extending_aesara_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/extending_faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)    55625 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/graph_rewriting.rst
--rw-r--r--   0 runner    (1001) docker     (123)    13711 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/graphstructures.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9026 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/inplace.rst
--rw-r--r--   0 runner    (1001) docker     (123)    24970 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/op.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9538 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/other_ops.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.906043 aesara-nightly-2.8.9.post117/doc/extending/pics/
--rw-r--r--   0 runner    (1001) docker     (123)    23471 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/pics/symbolic_graph_opt.png
--rw-r--r--   0 runner    (1001) docker     (123)    62062 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/pics/symbolic_graph_unopt.png
--rw-r--r--   0 runner    (1001) docker     (123)     4929 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/pipeline.rst
--rw-r--r--   0 runner    (1001) docker     (123)    17120 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/scan.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1622 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/tips.rst
--rw-r--r--   0 runner    (1001) docker     (123)    19679 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/type.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10050 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/unittest.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7699 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/extending/using_params.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6714 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1283 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/generate_dtype_tensor_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     7094 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/glossary.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.906043 aesara-nightly-2.8.9.post117/doc/images/
--rw-r--r--   0 runner    (1001) docker     (123)    94102 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/Elman_srnn.png
--rw-r--r--   0 runner    (1001) docker     (123)   116646 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/aesara_logo_2400.png
--rw-r--r--   0 runner    (1001) docker     (123)   102018 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/blocksparse.png
--rw-r--r--   0 runner    (1001) docker     (123)    13780 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/lstm.png
--rw-r--r--   0 runner    (1001) docker     (123)    14362 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/lstm_memorycell.png
--rw-r--r--   0 runner    (1001) docker     (123)   273555 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/talk2010.gif
--rw-r--r--   0 runner    (1001) docker     (123)    12455 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/images/talk2010.png
--rw-r--r--   0 runner    (1001) docker     (123)     3122 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/install.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.906043 aesara-nightly-2.8.9.post117/doc/internal/
--rw-r--r--   0 runner    (1001) docker     (123)     1074 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/internal/how_to_release.rst
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/internal/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2534 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/internal/metadocumentation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7918 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/introduction.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.910043 aesara-nightly-2.8.9.post117/doc/library/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.910043 aesara-nightly-2.8.9.post117/doc/library/compile/
--rw-r--r--   0 runner    (1001) docker     (123)     8364 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/debugmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8910 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/function.rst
--rw-r--r--   0 runner    (1001) docker     (123)      454 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    11817 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/io.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2152 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/mode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/nanguardmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)      899 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/opfromgraph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)      414 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/profilemode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/compile/shared.rst
--rw-r--r--   0 runner    (1001) docker     (123)    30660 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/config.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.910043 aesara-nightly-2.8.9.post117/doc/library/d3viz/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.910043 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.866043 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.910043 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/css/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/css/d3-context-menu.css
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/css/d3viz.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js
--rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    23339 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3viz.js
--rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js
--rw-r--r--   0 runner    (1001) docker     (123)     6168 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp.html
--rw-r--r--   0 runner    (1001) docker     (123)    84140 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp.png
--rw-r--r--   0 runner    (1001) docker     (123)     6406 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.html
--rw-r--r--   0 runner    (1001) docker     (123)    13875 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.pdf
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.png
--rw-r--r--   0 runner    (1001) docker     (123)     8963 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/ofg.html
--rw-r--r--   0 runner    (1001) docker     (123)     8115 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/ofg2.html
--rw-r--r--   0 runner    (1001) docker     (123)   216157 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)     8530 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/
--rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_10_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_11_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_24_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_25_0.png
--rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/gradient.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/graph/
--rw-r--r--   0 runner    (1001) docker     (123)      793 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/features.rst
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/fgraph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/graph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/op.rst
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/params_type.rst
--rw-r--r--   0 runner    (1001) docker     (123)      356 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/type.rst
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/graph/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1273 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/misc/
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/misc/pkl_utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7161 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/printing.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/sandbox/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      471 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/sandbox/linalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/sandbox/rng_mrg.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/scalar/
--rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/scalar/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    26706 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/scan.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.914043 aesara-nightly-2.8.9.post117/doc/library/sparse/
--rw-r--r--   0 runner    (1001) docker     (123)    11348 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/sparse/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      532 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/sparse/sandbox.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.918043 aesara-nightly-2.8.9.post117/doc/library/tensor/
--rw-r--r--   0 runner    (1001) docker     (123)    65290 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/basic.rst
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/basic_opt.rst
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/bcast.svg
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/elemwise.rst
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/extra_ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/fft.rst
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      754 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/io.rst
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/math_opt.rst
--rw-r--r--   0 runner    (1001) docker     (123)      530 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/nlinalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)    24638 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/plot_fft.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.918043 aesara-nightly-2.8.9.post117/doc/library/tensor/random/
--rw-r--r--   0 runner    (1001) docker     (123)     4687 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/random/basic.rst
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/random/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2164 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/random/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)      732 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/slinalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/tensor/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/library/typed_list.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/links.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3022 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/mission.rst
--rw-r--r--   0 runner    (1001) docker     (123)    12085 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/optimizations.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9038 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/pylintrc
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.918043 aesara-nightly-2.8.9.post117/doc/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)    12643 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/ccodegen.rst
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/compilation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2906 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/debugging_with_stepmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5889 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/elemwise_compiler.rst
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/function.rst
--rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/functional.rst
--rw-r--r--   0 runner    (1001) docker     (123)    17336 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/how_to_make_ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/index2.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2360 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/interactive_debugger.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2618 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/logistic_regression_example.rst
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/performance.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/randomnumbers.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4261 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/rethinkccodegen.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5946 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/sandbox.rst
--rw-r--r--   0 runner    (1001) docker     (123)      985 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/software.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6172 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/sparse.rst
--rw-r--r--   0 runner    (1001) docker     (123)      117 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/sandbox/tensoroptools.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.918043 aesara-nightly-2.8.9.post117/doc/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     3886 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/scripts/docgen.py
--rw-r--r--   0 runner    (1001) docker     (123)    11515 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/troubleshooting.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.922043 aesara-nightly-2.8.9.post117/doc/tutorial/
--rw-r--r--   0 runner    (1001) docker     (123)     6983 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/adding.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      371 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/adding_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)    11485 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/aliasing.rst
--rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/apply.png
--rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/apply.svg
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/broadcasting.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/conditions.rst
--rw-r--r--   0 runner    (1001) docker     (123)    23084 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/debug_faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5838 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/dlogistic.png
--rw-r--r--   0 runner    (1001) docker     (123)    18865 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/examples.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/faq_tutorial.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10801 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/gradients.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5988 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/loading_and_saving.rst
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/logistic.gp
--rw-r--r--   0 runner    (1001) docker     (123)     4887 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/logistic.png
--rw-r--r--   0 runner    (1001) docker     (123)    12715 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/loop.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     2517 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/loop_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)    11672 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/modes.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     1881 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/modes_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2697 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/multi_cores.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4366 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/nan_tutorial.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 03:31:06.922043 aesara-nightly-2.8.9.post117/doc/tutorial/pics/
--rw-r--r--   0 runner    (1001) docker     (123)    55147 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/pics/d3viz.png
--rw-r--r--   0 runner    (1001) docker     (123)   106142 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_predict.png
--rw-r--r--   0 runner    (1001) docker     (123)   148860 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_prediction.png
--rw-r--r--   0 runner    (1001) docker     (123)   473403 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_train.png
--rw-r--r--   0 runner    (1001) docker     (123)     4965 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/printing_drawing.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3716 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/profiling.rst
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/profiling_example.py
--rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/profiling_example_out.prof
--rw-r--r--   0 runner    (1001) docker     (123)     3951 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/shape_info.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8410 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/sparse.rst
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/doc/tutorial/symbolic_graphs.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9891 2023-01-10 03:30:57.000000 aesara-nightly-2.8.9.post117/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/requirements-rtd.txt
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-01-10 03:30:55.000000 aesara-nightly-2.8.9.post117/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-10 03:31:06.926043 aesara-nightly-2.8.9.post117/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.757730 aesara-nightly-2.8.9.post118/
+-rw-r--r--   0 runner    (1001) docker     (123)      809 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/DESCRIPTION.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2515 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-01-18 20:56:56.757730 aesara-nightly-2.8.9.post118/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4112 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.701730 aesara-nightly-2.8.9.post118/aesara/
+-rw-r--r--   0 runner    (1001) docker     (123)     5760 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      252 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/assert_op.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.701730 aesara-nightly-2.8.9.post118/aesara/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/bin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4080 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/bin/aesara_cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6057 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/breakpoint.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.701730 aesara-nightly-2.8.9.post118/aesara/compile/
+-rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37547 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/builders.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9954 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/compiledir.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2041 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/compilelock.py
+-rw-r--r--   0 runner    (1001) docker     (123)    85453 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/debugmode.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.701730 aesara-nightly-2.8.9.post118/aesara/compile/function/
+-rw-r--r--   0 runner    (1001) docker     (123)    13377 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/function/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22099 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/function/pfunc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    71335 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/function/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9102 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17823 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/mode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/monitormode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8326 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/nanguardmode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9969 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59779 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/profiling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7202 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/compile/sharedvalue.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46230 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/configdefaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22530 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/configparser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.701730 aesara-nightly-2.8.9.post118/aesara/d3viz/
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.705730 aesara-nightly-2.8.9.post118/aesara/d3viz/css/
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/css/d3-context-menu.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/css/d3viz.css
+-rw-r--r--   0 runner    (1001) docker     (123)     3830 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/d3viz.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11843 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/formatting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.705730 aesara-nightly-2.8.9.post118/aesara/d3viz/html/
+-rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/html/template.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.705730 aesara-nightly-2.8.9.post118/aesara/d3viz/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3-context-menu.js
+-rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3.v3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    23208 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3viz.js
+-rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/js/dagre-d3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/d3viz/js/graphlib-dot.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    87043 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/gradient.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.705730 aesara-nightly-2.8.9.post118/aesara/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)      505 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59820 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31374 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/destroyhandler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26449 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35817 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/fg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/kanren.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1150 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/null_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25075 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)      793 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/opt_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      786 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/optdb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.705730 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   114248 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19934 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/db.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3035 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/kanren.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7239 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/unify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9148 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/rewriting/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7865 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/sched.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/toolbox.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8926 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/unify.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12164 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/graph/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29070 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/ifelse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.709730 aesara-nightly-2.8.9.post118/aesara/link/
+-rw-r--r--   0 runner    (1001) docker     (123)        3 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23890 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.709730 aesara-nightly-2.8.9.post118/aesara/link/c/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    72624 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.709730 aesara-nightly-2.8.9.post118/aesara/link/c/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)      706 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/c_code/aesara_mod_helper.h
+-rw-r--r--   0 runner    (1001) docker     (123)    35583 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/c_code/lazylinker_c.c
+-rw-r--r--   0 runner    (1001) docker     (123)   112626 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/cmodule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4183 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/cutils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/cvm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      402 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20016 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/interface.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6641 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/lazylinker_c.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24725 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31659 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/params_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26568 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/c/type.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.709730 aesara-nightly-2.8.9.post118/aesara/link/jax/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/
+-rw-r--r--   0 runner    (1001) docker     (123)      529 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2945 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3381 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3072 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/nlinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10930 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5612 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/scalar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5382 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/slinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3192 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3380 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/tensor_basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/jax_dispatch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      232 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/jax_linker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2991 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/jax/linker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/link/numba/
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25914 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22249 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9266 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5085 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/nlinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12537 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8896 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/scalar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14205 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/sparse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6405 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/tensor_basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/numba/linker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28718 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50578 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/link/vm.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9672 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/check_blas.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      600 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/check_blas_many.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2410 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/check_duplicate_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2166 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/elemwise_openmp_speedup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/elemwise_time_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/frozendict.py
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/latence_gpu_transfert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      921 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/may_share_memory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7191 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/ordered_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9746 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/pkl_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2292 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/misc/safe_asarray.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64090 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/printing.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     5838 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/raise_op.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/fourier.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.713730 aesara-nightly-2.8.9.post118/aesara/sandbox/linalg/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/linalg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6062 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/linalg/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/minimal.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14812 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/multinomial.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48272 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/rng_mrg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8105 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/samples_MRG31k3p_12_7_5.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      217 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sandbox/solve.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.717730 aesara-nightly-2.8.9.post118/aesara/scalar/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   139093 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/basic_scipy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/basic_sympy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.717730 aesara-nightly-2.8.9.post118/aesara/scalar/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)   126227 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/c_code/Faddeeva.cc
+-rw-r--r--   0 runner    (1001) docker     (123)     2645 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/c_code/Faddeeva.hh
+-rw-r--r--   0 runner    (1001) docker     (123)    16816 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/c_code/gamma.c
+-rw-r--r--   0 runner    (1001) docker     (123)    40497 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1851 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scalar/sharedvar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.717730 aesara-nightly-2.8.9.post118/aesara/scan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1931 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50325 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.717730 aesara-nightly-2.8.9.post118/aesara/scan/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)  1108062 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/c_code/scan_perform.c
+-rw-r--r--   0 runner    (1001) docker     (123)     6743 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/checkpoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)   140552 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    95135 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/rewriting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23996 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/scan_perform.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     3512 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/scan_perform_ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38175 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4599 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/scan/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.721730 aesara-nightly-2.8.9.post118/aesara/sparse/
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   118012 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      232 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    76908 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/rewriting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.721730 aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17297 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/sp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7194 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/sp2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      827 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/sharedvar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8073 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      767 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/sparse/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.725730 aesara-nightly-2.8.9.post118/aesara/tensor/
+-rw-r--r--   0 runner    (1001) docker     (123)     4289 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   135697 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/basic_opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    98873 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/blas.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26486 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/blas_c.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68050 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/blas_headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/blas_scipy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.725730 aesara-nightly-2.8.9.post118/aesara/tensor/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)      897 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/c_code/alt_blas_common.h
+-rw-r--r--   0 runner    (1001) docker     (123)    16236 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/c_code/alt_blas_template.c
+-rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/c_code/dimshuffle.c
+-rw-r--r--   0 runner    (1001) docker     (123)    66688 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20866 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/elemwise_cgen.py
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57998 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7591 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/fft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6603 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/fourier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7737 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/inplace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7242 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/linalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    92466 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/math_opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22763 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nlinalg.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.725730 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   138966 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/abstract_conv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75762 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35370 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/batchnorm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8902 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/blocksparse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)    18972 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/corr3d_gemm.c
+-rw-r--r--   0 runner    (1001) docker     (123)    26551 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/corr_gemm.c
+-rw-r--r--   0 runner    (1001) docker     (123)     8195 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/ctc_wrapper.c
+-rw-r--r--   0 runner    (1001) docker     (123)    94525 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/conv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9910 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/conv3d2d.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40356 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/corr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36145 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/corr3d.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8522 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/ctc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35353 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/neighbours.py
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17298 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/rewriting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5212 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/nnet/sigm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/opt_uncanonicalize.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/tensor/random/
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61298 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14370 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/opt.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15291 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/jax.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6730 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9021 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/random/var.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)      384 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42710 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39793 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4846 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3954 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/jax.py
+-rw-r--r--   0 runner    (1001) docker     (123)   122924 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44832 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6102 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/special.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63205 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9500 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/uncanonicalize.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33343 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3858 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/sharedvar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/tensor/signal/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/signal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/signal/conv.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    97512 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/signal/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25027 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/slinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17849 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27168 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/special.py
+-rw-r--r--   0 runner    (1001) docker     (123)    91237 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/subtensor_opt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41042 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4090 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/type_other.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3211 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36091 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/var.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1831 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/tensor/xlogx.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.729730 aesara-nightly-2.8.9.post118/aesara/typed_list/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/typed_list/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18222 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/typed_list/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      780 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/typed_list/rewriting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/typed_list/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2925 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/updates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13641 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      939 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/aesara/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    12555 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-18 20:56:56.000000 aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/bin/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      285 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/bin/aesara-cache
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/bin/aesara_cache.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/doc/.build/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.build/PLACEHOLDER
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/doc/.static/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.static/PLACEHOLDER
+-rw-r--r--   0 runner    (1001) docker     (123)      256 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.static/fix_rtd.css
+-rw-r--r--   0 runner    (1001) docker     (123)     3799 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.static/version_switch.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.733730 aesara-nightly-2.8.9.post118/doc/.templates/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.templates/PLACEHOLDER
+-rw-r--r--   0 runner    (1001) docker     (123)     1409 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/.templates/layout.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2515 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1159 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/acknowledgement.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/bcast.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1282 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/core_development_guide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/css.inc
+-rw-r--r--   0 runner    (1001) docker     (123)     8604 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/dev_start_guide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/environment.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.737730 aesara-nightly-2.8.9.post118/doc/extending/
+-rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/apply.png
+-rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/apply.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    32078 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/apply2.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    46604 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/creating_a_c_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6334 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/creating_a_numba_jax_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    32993 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/creating_an_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    22664 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/ctype.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     5513 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/extending_aesara_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/extending_faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    55625 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/graph_rewriting.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    13711 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/graphstructures.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9026 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/inplace.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    24970 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9538 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/other_ops.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.737730 aesara-nightly-2.8.9.post118/doc/extending/pics/
+-rw-r--r--   0 runner    (1001) docker     (123)    23471 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/pics/symbolic_graph_opt.png
+-rw-r--r--   0 runner    (1001) docker     (123)    62062 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/pics/symbolic_graph_unopt.png
+-rw-r--r--   0 runner    (1001) docker     (123)     4929 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/pipeline.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    17120 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/scan.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1622 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/tips.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    19679 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/type.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10050 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/unittest.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7699 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/extending/using_params.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6714 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1283 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/generate_dtype_tensor_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7094 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/glossary.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.737730 aesara-nightly-2.8.9.post118/doc/images/
+-rw-r--r--   0 runner    (1001) docker     (123)    94102 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/Elman_srnn.png
+-rw-r--r--   0 runner    (1001) docker     (123)   116646 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/aesara_logo_2400.png
+-rw-r--r--   0 runner    (1001) docker     (123)   102018 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/blocksparse.png
+-rw-r--r--   0 runner    (1001) docker     (123)    13780 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/lstm.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14362 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/lstm_memorycell.png
+-rw-r--r--   0 runner    (1001) docker     (123)   273555 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/talk2010.gif
+-rw-r--r--   0 runner    (1001) docker     (123)    12455 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/images/talk2010.png
+-rw-r--r--   0 runner    (1001) docker     (123)     3122 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/install.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/internal/
+-rw-r--r--   0 runner    (1001) docker     (123)     1074 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/internal/how_to_release.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/internal/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2534 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/internal/metadocumentation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7918 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/introduction.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/library/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/library/compile/
+-rw-r--r--   0 runner    (1001) docker     (123)     8364 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/debugmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8910 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/function.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      454 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    11817 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/io.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2152 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/mode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/nanguardmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      899 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/opfromgraph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      414 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/profilemode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/compile/shared.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    30660 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/config.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/library/d3viz/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.697730 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.741730 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/css/
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/css/d3-context-menu.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/css/d3viz.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js
+-rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    23339 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3viz.js
+-rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)     6168 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp.html
+-rw-r--r--   0 runner    (1001) docker     (123)    84140 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp.png
+-rw-r--r--   0 runner    (1001) docker     (123)     6406 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13875 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.pdf
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.png
+-rw-r--r--   0 runner    (1001) docker     (123)     8963 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/ofg.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8115 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/ofg2.html
+-rw-r--r--   0 runner    (1001) docker     (123)   216157 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)     8530 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/
+-rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_10_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_11_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_24_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_25_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/gradient.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)      793 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/features.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/fgraph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/graph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/params_type.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      356 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/type.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/graph/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1273 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/misc/pkl_utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7161 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/printing.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/sandbox/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      471 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/sandbox/linalg.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/sandbox/rng_mrg.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/scalar/
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/scalar/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    26706 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/scan.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.745730 aesara-nightly-2.8.9.post118/doc/library/sparse/
+-rw-r--r--   0 runner    (1001) docker     (123)    11348 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/sparse/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      532 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/sparse/sandbox.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.749730 aesara-nightly-2.8.9.post118/doc/library/tensor/
+-rw-r--r--   0 runner    (1001) docker     (123)    65290 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/basic.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/basic_opt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/bcast.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/elemwise.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/extra_ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/fft.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      754 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/io.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/math_opt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      530 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/nlinalg.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    24638 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/plot_fft.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.749730 aesara-nightly-2.8.9.post118/doc/library/tensor/random/
+-rw-r--r--   0 runner    (1001) docker     (123)     4687 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/random/basic.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/random/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2164 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/random/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      732 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/slinalg.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/tensor/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/library/typed_list.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/links.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3022 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/mission.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    12085 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/optimizations.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9038 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/pylintrc
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.749730 aesara-nightly-2.8.9.post118/doc/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)    12643 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/ccodegen.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/compilation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2906 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/debugging_with_stepmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5889 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/elemwise_compiler.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/function.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/functional.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    17336 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/how_to_make_ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/index2.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2360 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/interactive_debugger.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2618 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/logistic_regression_example.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/performance.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/randomnumbers.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4261 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/rethinkccodegen.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5946 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/sandbox.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      985 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/software.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6172 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/sparse.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/sandbox/tensoroptools.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.749730 aesara-nightly-2.8.9.post118/doc/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     3886 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/scripts/docgen.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11515 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/troubleshooting.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.753730 aesara-nightly-2.8.9.post118/doc/tutorial/
+-rw-r--r--   0 runner    (1001) docker     (123)     6983 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/adding.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      371 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/adding_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11485 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/aliasing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/apply.png
+-rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/apply.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/broadcasting.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/conditions.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    23084 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/debug_faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5838 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/dlogistic.png
+-rw-r--r--   0 runner    (1001) docker     (123)    18865 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/examples.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/faq_tutorial.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10801 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/gradients.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5988 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/loading_and_saving.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/logistic.gp
+-rw-r--r--   0 runner    (1001) docker     (123)     4887 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/logistic.png
+-rw-r--r--   0 runner    (1001) docker     (123)    12715 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/loop.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2517 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/loop_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11672 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/modes.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1881 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/modes_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2697 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/multi_cores.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4366 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/nan_tutorial.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-18 20:56:56.753730 aesara-nightly-2.8.9.post118/doc/tutorial/pics/
+-rw-r--r--   0 runner    (1001) docker     (123)    55147 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/pics/d3viz.png
+-rw-r--r--   0 runner    (1001) docker     (123)   106142 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_predict.png
+-rw-r--r--   0 runner    (1001) docker     (123)   148860 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_prediction.png
+-rw-r--r--   0 runner    (1001) docker     (123)   473403 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_train.png
+-rw-r--r--   0 runner    (1001) docker     (123)     4965 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/printing_drawing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3716 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/profiling.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/profiling_example.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/profiling_example_out.prof
+-rw-r--r--   0 runner    (1001) docker     (123)     3951 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/shape_info.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8410 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/sparse.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/doc/tutorial/symbolic_graphs.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9891 2023-01-18 20:56:46.000000 aesara-nightly-2.8.9.post118/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/requirements-rtd.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-01-18 20:56:45.000000 aesara-nightly-2.8.9.post118/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-18 20:56:56.757730 aesara-nightly-2.8.9.post118/setup.cfg
```

### Comparing `aesara-nightly-2.8.9.post117/DESCRIPTION.txt` & `aesara-nightly-2.8.9.post118/DESCRIPTION.txt`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/LICENSE.txt` & `aesara-nightly-2.8.9.post118/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/PKG-INFO` & `aesara-nightly-2.8.9.post118/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aesara-nightly
-Version: 2.8.9.post117
+Version: 2.8.9.post118
 Summary: A library for defining, optimizing, and efficiently evaluating mathematical expressions involving multi-dimensional arrays.
 Author-email: aesara-devs <aesara.devs@gmail.com>
 License: BSD-3-Clause
 Project-URL: Homepage, https://github.com/aesara-devs/aesara
 Keywords: aesara,math,numerical,symbolic,blas,numpy,autodiff,differentiation
 Platform: Windows
 Platform: Linux
```

### Comparing `aesara-nightly-2.8.9.post117/README.rst` & `aesara-nightly-2.8.9.post118/README.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/bin/aesara_cache.py` & `aesara-nightly-2.8.9.post118/aesara/bin/aesara_cache.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/breakpoint.py` & `aesara-nightly-2.8.9.post118/aesara/breakpoint.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/compile/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/builders.py` & `aesara-nightly-2.8.9.post118/aesara/compile/builders.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/compiledir.py` & `aesara-nightly-2.8.9.post118/aesara/compile/compiledir.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/compilelock.py` & `aesara-nightly-2.8.9.post118/aesara/compile/compilelock.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/debugmode.py` & `aesara-nightly-2.8.9.post118/aesara/compile/debugmode.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/function/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/compile/function/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/function/pfunc.py` & `aesara-nightly-2.8.9.post118/aesara/compile/function/pfunc.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/function/types.py` & `aesara-nightly-2.8.9.post118/aesara/compile/function/types.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/io.py` & `aesara-nightly-2.8.9.post118/aesara/compile/io.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/mode.py` & `aesara-nightly-2.8.9.post118/aesara/compile/mode.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/monitormode.py` & `aesara-nightly-2.8.9.post118/aesara/compile/monitormode.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/nanguardmode.py` & `aesara-nightly-2.8.9.post118/aesara/compile/nanguardmode.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/ops.py` & `aesara-nightly-2.8.9.post118/aesara/compile/ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/profiling.py` & `aesara-nightly-2.8.9.post118/aesara/compile/profiling.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/compile/sharedvalue.py` & `aesara-nightly-2.8.9.post118/aesara/compile/sharedvalue.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/configdefaults.py` & `aesara-nightly-2.8.9.post118/aesara/configdefaults.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/configparser.py` & `aesara-nightly-2.8.9.post118/aesara/configparser.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/css/d3viz.css` & `aesara-nightly-2.8.9.post118/aesara/d3viz/css/d3viz.css`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/d3viz.py` & `aesara-nightly-2.8.9.post118/aesara/d3viz/d3viz.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/formatting.py` & `aesara-nightly-2.8.9.post118/aesara/d3viz/formatting.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/html/template.html` & `aesara-nightly-2.8.9.post118/aesara/d3viz/html/template.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3-context-menu.js` & `aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3-context-menu.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3.v3.min.js` & `aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3.v3.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/js/d3viz.js` & `aesara-nightly-2.8.9.post118/aesara/d3viz/js/d3viz.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/js/dagre-d3.min.js` & `aesara-nightly-2.8.9.post118/aesara/d3viz/js/dagre-d3.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/d3viz/js/graphlib-dot.min.js` & `aesara-nightly-2.8.9.post118/aesara/d3viz/js/graphlib-dot.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/gradient.py` & `aesara-nightly-2.8.9.post118/aesara/gradient.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/basic.py` & `aesara-nightly-2.8.9.post118/aesara/graph/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/destroyhandler.py` & `aesara-nightly-2.8.9.post118/aesara/graph/destroyhandler.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/features.py` & `aesara-nightly-2.8.9.post118/aesara/graph/features.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/fg.py` & `aesara-nightly-2.8.9.post118/aesara/graph/fg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/null_type.py` & `aesara-nightly-2.8.9.post118/aesara/graph/null_type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/op.py` & `aesara-nightly-2.8.9.post118/aesara/graph/op.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/opt.py` & `aesara-nightly-2.8.9.post118/aesara/graph/opt.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/opt_utils.py` & `aesara-nightly-2.8.9.post118/aesara/graph/opt_utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/optdb.py` & `aesara-nightly-2.8.9.post118/aesara/graph/optdb.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/rewriting/basic.py` & `aesara-nightly-2.8.9.post118/aesara/graph/rewriting/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/rewriting/db.py` & `aesara-nightly-2.8.9.post118/aesara/graph/rewriting/db.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/rewriting/kanren.py` & `aesara-nightly-2.8.9.post118/aesara/graph/rewriting/kanren.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/rewriting/unify.py` & `aesara-nightly-2.8.9.post118/aesara/graph/rewriting/unify.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/rewriting/utils.py` & `aesara-nightly-2.8.9.post118/aesara/graph/rewriting/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/sched.py` & `aesara-nightly-2.8.9.post118/aesara/graph/sched.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/type.py` & `aesara-nightly-2.8.9.post118/aesara/graph/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/graph/utils.py` & `aesara-nightly-2.8.9.post118/aesara/graph/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/ifelse.py` & `aesara-nightly-2.8.9.post118/aesara/ifelse.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/c_code/aesara_mod_helper.h` & `aesara-nightly-2.8.9.post118/aesara/link/c/c_code/aesara_mod_helper.h`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/c_code/lazylinker_c.c` & `aesara-nightly-2.8.9.post118/aesara/link/c/c_code/lazylinker_c.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/cmodule.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/cmodule.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/cutils.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/cutils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/cvm.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/cvm.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/interface.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/interface.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/lazylinker_c.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/lazylinker_c.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/op.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/op.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/params_type.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/params_type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/c/type.py` & `aesara-nightly-2.8.9.post118/aesara/link/c/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/elemwise.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/elemwise.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/extra_ops.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/extra_ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/nlinalg.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/nlinalg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/random.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/random.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/scalar.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/scalar.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/scan.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/scan.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/shape.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/shape.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/slinalg.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/slinalg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/subtensor.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/subtensor.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/dispatch/tensor_basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/dispatch/tensor_basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/jax/linker.py` & `aesara-nightly-2.8.9.post118/aesara/link/jax/linker.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/elemwise.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/elemwise.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/extra_ops.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/extra_ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/nlinalg.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/nlinalg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/random.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/random.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/scalar.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/scalar.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/scan.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/scan.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/sparse.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/sparse.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/dispatch/tensor_basic.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/dispatch/tensor_basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/numba/linker.py` & `aesara-nightly-2.8.9.post118/aesara/link/numba/linker.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/utils.py` & `aesara-nightly-2.8.9.post118/aesara/link/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/link/vm.py` & `aesara-nightly-2.8.9.post118/aesara/link/vm.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/check_blas.py` & `aesara-nightly-2.8.9.post118/aesara/misc/check_blas.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/check_blas_many.sh` & `aesara-nightly-2.8.9.post118/aesara/misc/check_blas_many.sh`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/check_duplicate_key.py` & `aesara-nightly-2.8.9.post118/aesara/misc/check_duplicate_key.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/elemwise_openmp_speedup.py` & `aesara-nightly-2.8.9.post118/aesara/misc/elemwise_openmp_speedup.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/elemwise_time_test.py` & `aesara-nightly-2.8.9.post118/aesara/misc/elemwise_time_test.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/frozendict.py` & `aesara-nightly-2.8.9.post118/aesara/misc/frozendict.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/latence_gpu_transfert.py` & `aesara-nightly-2.8.9.post118/aesara/misc/latence_gpu_transfert.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/may_share_memory.py` & `aesara-nightly-2.8.9.post118/aesara/misc/may_share_memory.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/ordered_set.py` & `aesara-nightly-2.8.9.post118/aesara/misc/ordered_set.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/pkl_utils.py` & `aesara-nightly-2.8.9.post118/aesara/misc/pkl_utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/misc/safe_asarray.py` & `aesara-nightly-2.8.9.post118/aesara/misc/safe_asarray.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/printing.py` & `aesara-nightly-2.8.9.post118/aesara/printing.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/raise_op.py` & `aesara-nightly-2.8.9.post118/aesara/raise_op.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/fourier.py` & `aesara-nightly-2.8.9.post118/aesara/sandbox/fourier.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/linalg/ops.py` & `aesara-nightly-2.8.9.post118/aesara/sandbox/linalg/ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/minimal.py` & `aesara-nightly-2.8.9.post118/aesara/sandbox/minimal.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/multinomial.py` & `aesara-nightly-2.8.9.post118/aesara/sandbox/multinomial.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/rng_mrg.py` & `aesara-nightly-2.8.9.post118/aesara/sandbox/rng_mrg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sandbox/samples_MRG31k3p_12_7_5.txt` & `aesara-nightly-2.8.9.post118/aesara/sandbox/samples_MRG31k3p_12_7_5.txt`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/basic.py` & `aesara-nightly-2.8.9.post118/aesara/scalar/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/basic_sympy.py` & `aesara-nightly-2.8.9.post118/aesara/scalar/basic_sympy.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/c_code/Faddeeva.cc` & `aesara-nightly-2.8.9.post118/aesara/scalar/c_code/Faddeeva.cc`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/c_code/Faddeeva.hh` & `aesara-nightly-2.8.9.post118/aesara/scalar/c_code/Faddeeva.hh`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/c_code/gamma.c` & `aesara-nightly-2.8.9.post118/aesara/scalar/c_code/gamma.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/math.py` & `aesara-nightly-2.8.9.post118/aesara/scalar/math.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scalar/sharedvar.py` & `aesara-nightly-2.8.9.post118/aesara/scalar/sharedvar.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/scan/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/basic.py` & `aesara-nightly-2.8.9.post118/aesara/scan/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/c_code/scan_perform.c` & `aesara-nightly-2.8.9.post118/aesara/scan/c_code/scan_perform.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/checkpoints.py` & `aesara-nightly-2.8.9.post118/aesara/scan/checkpoints.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/op.py` & `aesara-nightly-2.8.9.post118/aesara/scan/op.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/rewriting.py` & `aesara-nightly-2.8.9.post118/aesara/scan/rewriting.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/scan_perform.pyx` & `aesara-nightly-2.8.9.post118/aesara/scan/scan_perform.pyx`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/scan_perform_ext.py` & `aesara-nightly-2.8.9.post118/aesara/scan/scan_perform_ext.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/utils.py` & `aesara-nightly-2.8.9.post118/aesara/scan/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/scan/views.py` & `aesara-nightly-2.8.9.post118/aesara/scan/views.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/basic.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/rewriting.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/rewriting.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/sp.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/sp.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/sandbox/sp2.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/sandbox/sp2.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/sharedvar.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/sharedvar.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/type.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/sparse/utils.py` & `aesara-nightly-2.8.9.post118/aesara/sparse/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/basic.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/blas.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/blas.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/blas_c.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/blas_c.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/blas_headers.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/blas_headers.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/blas_scipy.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/blas_scipy.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/c_code/alt_blas_common.h` & `aesara-nightly-2.8.9.post118/aesara/tensor/c_code/alt_blas_common.h`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/c_code/alt_blas_template.c` & `aesara-nightly-2.8.9.post118/aesara/tensor/c_code/alt_blas_template.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/c_code/dimshuffle.c` & `aesara-nightly-2.8.9.post118/aesara/tensor/c_code/dimshuffle.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/elemwise.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/elemwise.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/elemwise_cgen.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/elemwise_cgen.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/extra_ops.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/extra_ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/fft.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/fft.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/fourier.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/fourier.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/inplace.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/inplace.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/io.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/io.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/math.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/math.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nlinalg.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nlinalg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/__init__.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/__init__.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/abstract_conv.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/abstract_conv.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/basic.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/batchnorm.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/batchnorm.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/blocksparse.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/blocksparse.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/corr3d_gemm.c` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/corr3d_gemm.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/corr_gemm.c` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/corr_gemm.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/c_code/ctc_wrapper.c` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/c_code/ctc_wrapper.c`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/conv.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/conv.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/conv3d2d.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/conv3d2d.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/corr.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/corr.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/corr3d.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/corr3d.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/ctc.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/ctc.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/neighbours.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/neighbours.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/rewriting.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/rewriting.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/nnet/sigm.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/nnet/sigm.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/basic.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/op.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/op.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/basic.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/rewriting/jax.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/rewriting/jax.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/type.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/utils.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/random/var.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/random/var.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/basic.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/elemwise.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/elemwise.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/extra_ops.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/extra_ops.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/jax.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/jax.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/math.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/math.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/shape.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/shape.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/special.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/special.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/subtensor.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/subtensor.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/rewriting/uncanonicalize.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/rewriting/uncanonicalize.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/shape.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/shape.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/sharedvar.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/sharedvar.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/signal/conv.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/signal/conv.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/signal/pool.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/signal/pool.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/slinalg.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/slinalg.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/sort.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/sort.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/special.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/special.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/subtensor.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/subtensor.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/type.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/type_other.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/type_other.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/utils.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/var.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/var.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/tensor/xlogx.py` & `aesara-nightly-2.8.9.post118/aesara/tensor/xlogx.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/typed_list/basic.py` & `aesara-nightly-2.8.9.post118/aesara/typed_list/basic.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/typed_list/rewriting.py` & `aesara-nightly-2.8.9.post118/aesara/typed_list/rewriting.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/typed_list/type.py` & `aesara-nightly-2.8.9.post118/aesara/typed_list/type.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/updates.py` & `aesara-nightly-2.8.9.post118/aesara/updates.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/utils.py` & `aesara-nightly-2.8.9.post118/aesara/utils.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara/version.py` & `aesara-nightly-2.8.9.post118/aesara/version.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/PKG-INFO` & `aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aesara-nightly
-Version: 2.8.9.post117
+Version: 2.8.9.post118
 Summary: A library for defining, optimizing, and efficiently evaluating mathematical expressions involving multi-dimensional arrays.
 Author-email: aesara-devs <aesara.devs@gmail.com>
 License: BSD-3-Clause
 Project-URL: Homepage, https://github.com/aesara-devs/aesara
 Keywords: aesara,math,numerical,symbolic,blas,numpy,autodiff,differentiation
 Platform: Windows
 Platform: Linux
```

### Comparing `aesara-nightly-2.8.9.post117/aesara_nightly.egg-info/SOURCES.txt` & `aesara-nightly-2.8.9.post118/aesara_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/.static/version_switch.js` & `aesara-nightly-2.8.9.post118/doc/.static/version_switch.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/.templates/layout.html` & `aesara-nightly-2.8.9.post118/doc/.templates/layout.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/LICENSE.txt` & `aesara-nightly-2.8.9.post118/doc/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/acknowledgement.rst` & `aesara-nightly-2.8.9.post118/doc/acknowledgement.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/bcast.png` & `aesara-nightly-2.8.9.post118/doc/bcast.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/bcast.svg` & `aesara-nightly-2.8.9.post118/doc/bcast.svg`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/conf.py` & `aesara-nightly-2.8.9.post118/doc/conf.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/core_development_guide.rst` & `aesara-nightly-2.8.9.post118/doc/core_development_guide.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/dev_start_guide.rst` & `aesara-nightly-2.8.9.post118/doc/dev_start_guide.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/apply.png` & `aesara-nightly-2.8.9.post118/doc/extending/apply.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/apply.svg` & `aesara-nightly-2.8.9.post118/doc/extending/apply.svg`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/apply2.svg` & `aesara-nightly-2.8.9.post118/doc/extending/apply2.svg`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/creating_a_c_op.rst` & `aesara-nightly-2.8.9.post118/doc/extending/creating_a_c_op.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/creating_a_numba_jax_op.rst` & `aesara-nightly-2.8.9.post118/doc/extending/creating_a_numba_jax_op.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/creating_an_op.rst` & `aesara-nightly-2.8.9.post118/doc/extending/creating_an_op.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/ctype.rst` & `aesara-nightly-2.8.9.post118/doc/extending/ctype.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/extending_aesara_solution_1.py` & `aesara-nightly-2.8.9.post118/doc/extending/extending_aesara_solution_1.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/extending_faq.rst` & `aesara-nightly-2.8.9.post118/doc/extending/extending_faq.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/graph_rewriting.rst` & `aesara-nightly-2.8.9.post118/doc/extending/graph_rewriting.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/graphstructures.rst` & `aesara-nightly-2.8.9.post118/doc/extending/graphstructures.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/index.rst` & `aesara-nightly-2.8.9.post118/doc/extending/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/inplace.rst` & `aesara-nightly-2.8.9.post118/doc/extending/inplace.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/op.rst` & `aesara-nightly-2.8.9.post118/doc/extending/op.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/other_ops.rst` & `aesara-nightly-2.8.9.post118/doc/extending/other_ops.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/pics/symbolic_graph_opt.png` & `aesara-nightly-2.8.9.post118/doc/extending/pics/symbolic_graph_opt.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/pics/symbolic_graph_unopt.png` & `aesara-nightly-2.8.9.post118/doc/extending/pics/symbolic_graph_unopt.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/pipeline.rst` & `aesara-nightly-2.8.9.post118/doc/extending/pipeline.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/scan.rst` & `aesara-nightly-2.8.9.post118/doc/extending/scan.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/tips.rst` & `aesara-nightly-2.8.9.post118/doc/extending/tips.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/type.rst` & `aesara-nightly-2.8.9.post118/doc/extending/type.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/unittest.rst` & `aesara-nightly-2.8.9.post118/doc/extending/unittest.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/extending/using_params.rst` & `aesara-nightly-2.8.9.post118/doc/extending/using_params.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/faq.rst` & `aesara-nightly-2.8.9.post118/doc/faq.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/generate_dtype_tensor_table.py` & `aesara-nightly-2.8.9.post118/doc/generate_dtype_tensor_table.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/glossary.rst` & `aesara-nightly-2.8.9.post118/doc/glossary.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/Elman_srnn.png` & `aesara-nightly-2.8.9.post118/doc/images/Elman_srnn.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/aesara_logo_2400.png` & `aesara-nightly-2.8.9.post118/doc/images/aesara_logo_2400.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/blocksparse.png` & `aesara-nightly-2.8.9.post118/doc/images/blocksparse.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/lstm.png` & `aesara-nightly-2.8.9.post118/doc/images/lstm.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/lstm_memorycell.png` & `aesara-nightly-2.8.9.post118/doc/images/lstm_memorycell.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/talk2010.gif` & `aesara-nightly-2.8.9.post118/doc/images/talk2010.gif`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/images/talk2010.png` & `aesara-nightly-2.8.9.post118/doc/images/talk2010.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/index.rst` & `aesara-nightly-2.8.9.post118/doc/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/install.rst` & `aesara-nightly-2.8.9.post118/doc/install.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/internal/how_to_release.rst` & `aesara-nightly-2.8.9.post118/doc/internal/how_to_release.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/internal/metadocumentation.rst` & `aesara-nightly-2.8.9.post118/doc/internal/metadocumentation.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/introduction.rst` & `aesara-nightly-2.8.9.post118/doc/introduction.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/debugmode.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/debugmode.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/function.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/function.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/io.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/io.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/mode.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/mode.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/nanguardmode.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/nanguardmode.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/opfromgraph.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/opfromgraph.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/compile/shared.rst` & `aesara-nightly-2.8.9.post118/doc/library/compile/shared.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/config.rst` & `aesara-nightly-2.8.9.post118/doc/library/config.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/css/d3viz.css` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/css/d3viz.css`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/d3viz.js` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/d3viz.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp.html` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.html` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.pdf` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.pdf`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/mlp2.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/mlp2.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/ofg.html` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/ofg.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/examples/ofg2.html` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/examples/ofg2.html`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index.ipynb` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index.ipynb`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index.rst` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_10_0.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_10_0.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_11_0.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_11_0.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_24_0.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_24_0.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/d3viz/index_files/index_25_0.png` & `aesara-nightly-2.8.9.post118/doc/library/d3viz/index_files/index_25_0.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/gradient.rst` & `aesara-nightly-2.8.9.post118/doc/library/gradient.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/graph/features.rst` & `aesara-nightly-2.8.9.post118/doc/library/graph/features.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/graph/fgraph.rst` & `aesara-nightly-2.8.9.post118/doc/library/graph/fgraph.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/index.rst` & `aesara-nightly-2.8.9.post118/doc/library/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/printing.rst` & `aesara-nightly-2.8.9.post118/doc/library/printing.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/scan.rst` & `aesara-nightly-2.8.9.post118/doc/library/scan.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/sparse/index.rst` & `aesara-nightly-2.8.9.post118/doc/library/sparse/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/sparse/sandbox.rst` & `aesara-nightly-2.8.9.post118/doc/library/sparse/sandbox.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/basic.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/basic.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/bcast.png` & `aesara-nightly-2.8.9.post118/doc/library/tensor/bcast.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/bcast.svg` & `aesara-nightly-2.8.9.post118/doc/library/tensor/bcast.svg`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/fft.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/fft.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/index.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/io.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/io.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/nlinalg.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/nlinalg.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/plot_fft.png` & `aesara-nightly-2.8.9.post118/doc/library/tensor/plot_fft.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/random/basic.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/random/basic.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/random/utils.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/random/utils.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/tensor/slinalg.rst` & `aesara-nightly-2.8.9.post118/doc/library/tensor/slinalg.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/library/typed_list.rst` & `aesara-nightly-2.8.9.post118/doc/library/typed_list.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/links.rst` & `aesara-nightly-2.8.9.post118/doc/links.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/mission.rst` & `aesara-nightly-2.8.9.post118/doc/mission.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/optimizations.rst` & `aesara-nightly-2.8.9.post118/doc/optimizations.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/pylintrc` & `aesara-nightly-2.8.9.post118/doc/pylintrc`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/ccodegen.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/ccodegen.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/debugging_with_stepmode.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/debugging_with_stepmode.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/elemwise_compiler.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/elemwise_compiler.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/how_to_make_ops.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/how_to_make_ops.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/interactive_debugger.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/interactive_debugger.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/logistic_regression_example.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/logistic_regression_example.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/performance.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/performance.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/randomnumbers.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/randomnumbers.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/rethinkccodegen.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/rethinkccodegen.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/sandbox.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/sandbox.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/software.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/software.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/sandbox/sparse.rst` & `aesara-nightly-2.8.9.post118/doc/sandbox/sparse.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/scripts/docgen.py` & `aesara-nightly-2.8.9.post118/doc/scripts/docgen.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/troubleshooting.rst` & `aesara-nightly-2.8.9.post118/doc/troubleshooting.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/adding.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/adding.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/aliasing.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/aliasing.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/apply.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/apply.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/apply.svg` & `aesara-nightly-2.8.9.post118/doc/tutorial/apply.svg`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/bcast.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/bcast.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/broadcasting.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/broadcasting.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/conditions.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/conditions.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/debug_faq.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/debug_faq.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/dlogistic.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/dlogistic.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/examples.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/examples.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/faq_tutorial.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/faq_tutorial.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/gradients.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/gradients.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/index.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/index.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/loading_and_saving.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/loading_and_saving.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/logistic.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/logistic.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/loop.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/loop.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/loop_solution_1.py` & `aesara-nightly-2.8.9.post118/doc/tutorial/loop_solution_1.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/modes.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/modes.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/modes_solution_1.py` & `aesara-nightly-2.8.9.post118/doc/tutorial/modes_solution_1.py`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/multi_cores.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/multi_cores.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/nan_tutorial.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/nan_tutorial.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/pics/d3viz.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/pics/d3viz.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_predict.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_predict.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_prediction.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_prediction.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/pics/logreg_pydotprint_train.png` & `aesara-nightly-2.8.9.post118/doc/tutorial/pics/logreg_pydotprint_train.png`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/printing_drawing.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/printing_drawing.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/profiling.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/profiling.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/profiling_example_out.prof` & `aesara-nightly-2.8.9.post118/doc/tutorial/profiling_example_out.prof`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/shape_info.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/shape_info.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/doc/tutorial/sparse.rst` & `aesara-nightly-2.8.9.post118/doc/tutorial/sparse.rst`

 * *Files identical despite different names*

### Comparing `aesara-nightly-2.8.9.post117/pyproject.toml` & `aesara-nightly-2.8.9.post118/pyproject.toml`

 * *Files identical despite different names*

