# Comparing `tmp/sagemath-repl-9.8b7.tar.gz` & `tmp/sagemath-repl-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sagemath-repl-9.8b7.tar", last modified: Thu Jan 19 06:51:55 2023, max compression
+gzip compressed data, was "sagemath-repl-9.8rc0.tar", last modified: Sun Jan 29 23:47:21 2023, max compression
```

## Comparing `sagemath-repl-9.8b7.tar` & `sagemath-repl-9.8rc0.tar`

### file list

```diff
@@ -1,159 +1,159 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.554983 sagemath-repl-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-01-19 06:51:55.554983 sagemath-repl-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/VERSION.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.542982 sagemath-repl-9.8b7/bin/
--rwxr-xr-x   0 runner    (1001) docker     (123)      793 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/math-readline
--rwxr-xr-x   0 runner    (1001) docker     (123)    43257 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage
--rwxr-xr-x   0 runner    (1001) docker     (123)      651 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-cachegrind
--rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-callgrind
--rwxr-xr-x   0 runner    (1001) docker     (123)     7405 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-cleaner
--rwxr-xr-x   0 runner    (1001) docker     (123)    10212 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-coverage
--rwxr-xr-x   0 runner    (1001) docker     (123)     1363 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-cython
--rw-r--r--   0 runner    (1001) docker     (123)    21921 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-env
--rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-env-config.in
--rwxr-xr-x   0 runner    (1001) docker     (123)      246 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-eval
--rwxr-xr-x   0 runner    (1001) docker     (123)     6144 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-fixdoctests
--rwxr-xr-x   0 runner    (1001) docker     (123)       99 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-grep
--rwxr-xr-x   0 runner    (1001) docker     (123)       93 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-grepdoc
--rwxr-xr-x   0 runner    (1001) docker     (123)      234 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-inline-fortran
--rwxr-xr-x   0 runner    (1001) docker     (123)     1345 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-ipynb2rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      360 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-ipython
--rwxr-xr-x   0 runner    (1001) docker     (123)     3668 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-list-packages
--rwxr-xr-x   0 runner    (1001) docker     (123)      613 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-massif
--rwxr-xr-x   0 runner    (1001) docker     (123)     8347 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-notebook
--rwxr-xr-x   0 runner    (1001) docker     (123)     3141 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-num-threads.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      595 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-omega
--rwxr-xr-x   0 runner    (1001) docker     (123)    10614 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-preparse
--rwxr-xr-x   0 runner    (1001) docker     (123)       28 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-python
--rwxr-xr-x   0 runner    (1001) docker     (123)     1524 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-rebase.bat
--rwxr-xr-x   0 runner    (1001) docker     (123)     2260 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-rebase.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)     1752 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-rebaseall.bat
--rwxr-xr-x   0 runner    (1001) docker     (123)      747 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-rebaseall.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      707 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-run
--rwxr-xr-x   0 runner    (1001) docker     (123)      253 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-run-cython
--rwxr-xr-x   0 runner    (1001) docker     (123)    11131 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-runtests
--rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-src-env-config.in
--rwxr-xr-x   0 runner    (1001) docker     (123)     6227 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-startuptime.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     3597 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-update-version
--rwxr-xr-x   0 runner    (1001) docker     (123)     1133 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-valgrind
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-venv-config
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/bin/sage-version.sh
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-19 06:47:53.000000 sagemath-repl-9.8b7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/pyproject.toml.m4
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/requirements.txt.m4
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.542982 sagemath-repl-9.8b7/sage/
--rw-r--r--   0 runner    (1001) docker     (123)      337 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/all__sagemath_repl.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.542982 sagemath-repl-9.8b7/sage/doctest/
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/all.py
--rw-r--r--   0 runner    (1001) docker     (123)    56046 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/control.py
--rw-r--r--   0 runner    (1001) docker     (123)    13930 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/external.py
--rw-r--r--   0 runner    (1001) docker     (123)    12724 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/fixtures.py
--rw-r--r--   0 runner    (1001) docker     (123)   103935 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/forker.py
--rw-r--r--   0 runner    (1001) docker     (123)    45339 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/parsing.py
--rw-r--r--   0 runner    (1001) docker     (123)    29654 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/reporting.py
--rw-r--r--   0 runner    (1001) docker     (123)    62236 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/sources.py
--rw-r--r--   0 runner    (1001) docker     (123)    22295 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.546983 sagemath-repl-9.8b7/sage/doctest/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       74 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/1second.rst
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/99seconds.rst
--rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/abort.rst
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/atexit.rst
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/fail_and_die.rst
--rw-r--r--   0 runner    (1001) docker     (123)      327 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/initial.rst
--rw-r--r--   0 runner    (1001) docker     (123)      188 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/interrupt.rst
--rw-r--r--   0 runner    (1001) docker     (123)      517 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/interrupt_diehard.rst
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/keyboardinterrupt.rst
--rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/longtime.rst
--rw-r--r--   0 runner    (1001) docker     (123)      178 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/nodoctest
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/random_seed.rst
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/show_skipped.rst
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/sig_on.rst
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/simple_failure.rst
--rw-r--r--   0 runner    (1001) docker     (123)      900 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/sleep_and_raise.rst
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/tests/tolerance.rst
--rw-r--r--   0 runner    (1001) docker     (123)    14537 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/sage/doctest/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.546983 sagemath-repl-9.8b7/sage/misc/
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/misc/all__sagemath_repl.py
--rw-r--r--   0 runner    (1001) docker     (123)     7905 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/misc/banner.py
--rw-r--r--   0 runner    (1001) docker     (123)     6927 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/misc/sage_eval.py
--rw-r--r--   0 runner    (1001) docker     (123)   120238 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/misc/sage_input.py
--rw-r--r--   0 runner    (1001) docker     (123)    64083 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/misc/sagedoc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.546983 sagemath-repl-9.8b7/sage/repl/
--rw-r--r--   0 runner    (1001) docker     (123)      620 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/all.py
--rw-r--r--   0 runner    (1001) docker     (123)    18874 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/attach.py
--rw-r--r--   0 runner    (1001) docker     (123)     5764 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.546983 sagemath-repl-9.8b7/sage/repl/display/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10360 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/fancy_repr.py
--rw-r--r--   0 runner    (1001) docker     (123)    11937 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/formatter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8968 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/jsmol_iframe.py
--rw-r--r--   0 runner    (1001) docker     (123)     4850 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/pretty_print.py
--rw-r--r--   0 runner    (1001) docker     (123)     5933 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/display/util.py
--rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/image.py
--rw-r--r--   0 runner    (1001) docker     (123)     1832 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/inputhook.py
--rw-r--r--   0 runner    (1001) docker     (123)     8693 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/interface_magic.py
--rw-r--r--   0 runner    (1001) docker     (123)    27709 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/interpreter.py
--rw-r--r--   0 runner    (1001) docker     (123)    20825 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_extension.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.550983 sagemath-repl-9.8b7/sage/repl/ipython_kernel/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/all_jupyter.py
--rw-r--r--   0 runner    (1001) docker     (123)     9350 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/install.py
--rw-r--r--   0 runner    (1001) docker     (123)    11673 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/interact.py
--rw-r--r--   0 runner    (1001) docker     (123)     5821 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/kernel.py
--rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/widgets.py
--rw-r--r--   0 runner    (1001) docker     (123)    20084 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_kernel/widgets_sagenb.py
--rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/ipython_tests.py
--rw-r--r--   0 runner    (1001) docker     (123)    10981 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/load.py
--rw-r--r--   0 runner    (1001) docker     (123)    76772 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/preparse.py
--rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/prompts.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.550983 sagemath-repl-9.8b7/sage/repl/rich_output/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22168 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/backend_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    12485 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/backend_doctest.py
--rw-r--r--   0 runner    (1001) docker     (123)     5909 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/backend_emacs.py
--rw-r--r--   0 runner    (1001) docker     (123)    22304 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/backend_ipython.py
--rw-r--r--   0 runner    (1001) docker     (123)     9949 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/buffer.py
--rw-r--r--   0 runner    (1001) docker     (123)    29763 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/display_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     7976 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.avi
--rw-r--r--   0 runner    (1001) docker     (123)      829 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.canvas3d
--rw-r--r--   0 runner    (1001) docker     (123)      212 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.dvi
--rw-r--r--   0 runner    (1001) docker     (123)     2710 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.flv
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.gif
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.jpg
--rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.mkv
--rw-r--r--   0 runner    (1001) docker     (123)     2493 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.mov
--rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.mp4
--rw-r--r--   0 runner    (1001) docker     (123)     5612 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.ogv
--rw-r--r--   0 runner    (1001) docker     (123)     4285 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.pdf
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.png
--rw-r--r--   0 runner    (1001) docker     (123)     1422 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.svg
--rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.webm
--rw-r--r--   0 runner    (1001) docker     (123)     3937 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example.wmv
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example_jmol.spt.zip
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example_wavefront_scene.mtl
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/example_wavefront_scene.obj
--rw-r--r--   0 runner    (1001) docker     (123)    12745 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_browser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_catalog.py
--rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_graphics.py
--rw-r--r--   0 runner    (1001) docker     (123)    11865 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_graphics3d.py
--rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/output_video.py
--rw-r--r--   0 runner    (1001) docker     (123)    12938 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/preferences.py
--rw-r--r--   0 runner    (1001) docker     (123)    11661 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/pretty_print.py
--rw-r--r--   0 runner    (1001) docker     (123)     6606 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/rich_output/test_backend.py
--rw-r--r--   0 runner    (1001) docker     (123)     5853 2023-01-19 06:47:41.000000 sagemath-repl-9.8b7/sage/repl/user_globals.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:55.554983 sagemath-repl-9.8b7/sagemath_repl.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-01-19 06:51:54.000000 sagemath-repl-9.8b7/sagemath_repl.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4064 2023-01-19 06:51:55.000000 sagemath-repl-9.8b7/sagemath_repl.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:54.000000 sagemath-repl-9.8b7/sagemath_repl.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-01-19 06:51:54.000000 sagemath-repl-9.8b7/sagemath_repl.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-19 06:51:54.000000 sagemath-repl-9.8b7/sagemath_repl.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1851 2023-01-19 06:51:55.554983 sagemath-repl-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2376 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/setup.cfg.m4
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-01-19 06:47:40.000000 sagemath-repl-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.585596 sagemath-repl-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2484 2023-01-29 23:47:21.585596 sagemath-repl-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/VERSION.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.577597 sagemath-repl-9.8rc0/bin/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      793 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/math-readline
+-rwxr-xr-x   0 runner    (1001) docker     (123)    43257 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage
+-rwxr-xr-x   0 runner    (1001) docker     (123)      651 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-cachegrind
+-rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-callgrind
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7405 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-cleaner
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10212 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-coverage
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1363 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-cython
+-rw-r--r--   0 runner    (1001) docker     (123)    21921 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-env
+-rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-env-config.in
+-rwxr-xr-x   0 runner    (1001) docker     (123)      246 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-eval
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6144 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-fixdoctests
+-rwxr-xr-x   0 runner    (1001) docker     (123)       99 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-grep
+-rwxr-xr-x   0 runner    (1001) docker     (123)       93 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-grepdoc
+-rwxr-xr-x   0 runner    (1001) docker     (123)      234 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-inline-fortran
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1345 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-ipynb2rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      360 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-ipython
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3668 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-list-packages
+-rwxr-xr-x   0 runner    (1001) docker     (123)      613 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-massif
+-rwxr-xr-x   0 runner    (1001) docker     (123)     8347 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-notebook
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3141 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-num-threads.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      595 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-omega
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10614 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-preparse
+-rwxr-xr-x   0 runner    (1001) docker     (123)       28 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-python
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1524 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-rebase.bat
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2260 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-rebase.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1752 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-rebaseall.bat
+-rwxr-xr-x   0 runner    (1001) docker     (123)      747 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-rebaseall.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      707 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-run
+-rwxr-xr-x   0 runner    (1001) docker     (123)      253 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-run-cython
+-rwxr-xr-x   0 runner    (1001) docker     (123)    11131 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-runtests
+-rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-src-env-config.in
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6227 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-startuptime.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3597 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-update-version
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1133 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-valgrind
+-rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-venv-config
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/bin/sage-version.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-29 23:43:56.000000 sagemath-repl-9.8rc0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/pyproject.toml.m4
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/requirements.txt.m4
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.577597 sagemath-repl-9.8rc0/sage/
+-rw-r--r--   0 runner    (1001) docker     (123)      337 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/all__sagemath_repl.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.577597 sagemath-repl-9.8rc0/sage/doctest/
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)    56046 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13930 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/external.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12724 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/fixtures.py
+-rw-r--r--   0 runner    (1001) docker     (123)   103935 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/forker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45339 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/parsing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29654 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/reporting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62236 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/sources.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22295 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.577597 sagemath-repl-9.8rc0/sage/doctest/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       74 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/1second.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/99seconds.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/abort.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/atexit.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/fail_and_die.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      327 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/initial.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      188 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/interrupt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      517 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/interrupt_diehard.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/keyboardinterrupt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/longtime.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      178 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/nodoctest
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/random_seed.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/show_skipped.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/sig_on.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/simple_failure.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      900 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/sleep_and_raise.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/tests/tolerance.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    14537 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/doctest/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.577597 sagemath-repl-9.8rc0/sage/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/misc/all__sagemath_repl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7905 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/misc/banner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6927 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/misc/sage_eval.py
+-rw-r--r--   0 runner    (1001) docker     (123)   120238 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/misc/sage_input.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64083 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/misc/sagedoc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.581596 sagemath-repl-9.8rc0/sage/repl/
+-rw-r--r--   0 runner    (1001) docker     (123)      620 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18874 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/attach.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5764 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.581596 sagemath-repl-9.8rc0/sage/repl/display/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10360 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/fancy_repr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11937 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/formatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8968 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/jsmol_iframe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4850 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/pretty_print.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5933 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/display/util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1832 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/inputhook.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8693 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/interface_magic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27709 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/interpreter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20825 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_extension.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.581596 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/all_jupyter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9350 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/install.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11673 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/interact.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5821 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/kernel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/widgets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20084 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_kernel/widgets_sagenb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/ipython_tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10981 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/load.py
+-rw-r--r--   0 runner    (1001) docker     (123)    76772 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/preparse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/prompts.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.585596 sagemath-repl-9.8rc0/sage/repl/rich_output/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22168 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/backend_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12485 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/backend_doctest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5909 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/backend_emacs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22304 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/backend_ipython.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9949 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/buffer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29763 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/display_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7976 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.avi
+-rw-r--r--   0 runner    (1001) docker     (123)      829 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.canvas3d
+-rw-r--r--   0 runner    (1001) docker     (123)      212 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.dvi
+-rw-r--r--   0 runner    (1001) docker     (123)     2710 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.flv
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.gif
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.mkv
+-rw-r--r--   0 runner    (1001) docker     (123)     2493 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.mov
+-rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.mp4
+-rw-r--r--   0 runner    (1001) docker     (123)     5612 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.ogv
+-rw-r--r--   0 runner    (1001) docker     (123)     4285 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.pdf
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1422 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.webm
+-rw-r--r--   0 runner    (1001) docker     (123)     3937 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example.wmv
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example_jmol.spt.zip
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example_wavefront_scene.mtl
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/example_wavefront_scene.obj
+-rw-r--r--   0 runner    (1001) docker     (123)    12745 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_browser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_catalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9923 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_graphics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11865 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_graphics3d.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/output_video.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12938 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/preferences.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11661 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/pretty_print.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6606 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/rich_output/test_backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5853 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/sage/repl/user_globals.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:21.585596 sagemath-repl-9.8rc0/sagemath_repl.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2484 2023-01-29 23:47:20.000000 sagemath-repl-9.8rc0/sagemath_repl.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4064 2023-01-29 23:47:21.000000 sagemath-repl-9.8rc0/sagemath_repl.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:47:20.000000 sagemath-repl-9.8rc0/sagemath_repl.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-01-29 23:47:20.000000 sagemath-repl-9.8rc0/sagemath_repl.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-29 23:47:20.000000 sagemath-repl-9.8rc0/sagemath_repl.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1853 2023-01-29 23:47:21.585596 sagemath-repl-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2376 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/setup.cfg.m4
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-01-29 23:43:48.000000 sagemath-repl-9.8rc0/tox.ini
```

### Comparing `sagemath-repl-9.8b7/PKG-INFO` & `sagemath-repl-9.8rc0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-repl
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: System and software environment
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-repl-9.8b7/README.rst` & `sagemath-repl-9.8rc0/README.rst`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/math-readline` & `sagemath-repl-9.8rc0/bin/math-readline`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage` & `sagemath-repl-9.8rc0/bin/sage`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-cachegrind` & `sagemath-repl-9.8rc0/bin/sage-cachegrind`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-cleaner` & `sagemath-repl-9.8rc0/bin/sage-cleaner`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-coverage` & `sagemath-repl-9.8rc0/bin/sage-coverage`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-cython` & `sagemath-repl-9.8rc0/bin/sage-cython`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-env` & `sagemath-repl-9.8rc0/bin/sage-env`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-env-config.in` & `sagemath-repl-9.8rc0/bin/sage-env-config.in`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-fixdoctests` & `sagemath-repl-9.8rc0/bin/sage-fixdoctests`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-ipynb2rst` & `sagemath-repl-9.8rc0/bin/sage-ipynb2rst`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-list-packages` & `sagemath-repl-9.8rc0/bin/sage-list-packages`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-massif` & `sagemath-repl-9.8rc0/bin/sage-massif`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-notebook` & `sagemath-repl-9.8rc0/bin/sage-notebook`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-num-threads.py` & `sagemath-repl-9.8rc0/bin/sage-num-threads.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-omega` & `sagemath-repl-9.8rc0/bin/sage-omega`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-preparse` & `sagemath-repl-9.8rc0/bin/sage-preparse`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-rebase.bat` & `sagemath-repl-9.8rc0/bin/sage-rebase.bat`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-rebase.sh` & `sagemath-repl-9.8rc0/bin/sage-rebase.sh`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-rebaseall.bat` & `sagemath-repl-9.8rc0/bin/sage-rebaseall.bat`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-rebaseall.sh` & `sagemath-repl-9.8rc0/bin/sage-rebaseall.sh`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-run` & `sagemath-repl-9.8rc0/bin/sage-run`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-runtests` & `sagemath-repl-9.8rc0/bin/sage-runtests`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-src-env-config.in` & `sagemath-repl-9.8rc0/bin/sage-src-env-config.in`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-startuptime.py` & `sagemath-repl-9.8rc0/bin/sage-startuptime.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-update-version` & `sagemath-repl-9.8rc0/bin/sage-update-version`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-valgrind` & `sagemath-repl-9.8rc0/bin/sage-valgrind`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/bin/sage-venv-config` & `sagemath-repl-9.8rc0/bin/sage-venv-config`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/control.py` & `sagemath-repl-9.8rc0/sage/doctest/control.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/external.py` & `sagemath-repl-9.8rc0/sage/doctest/external.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/fixtures.py` & `sagemath-repl-9.8rc0/sage/doctest/fixtures.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/forker.py` & `sagemath-repl-9.8rc0/sage/doctest/forker.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/parsing.py` & `sagemath-repl-9.8rc0/sage/doctest/parsing.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/reporting.py` & `sagemath-repl-9.8rc0/sage/doctest/reporting.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/sources.py` & `sagemath-repl-9.8rc0/sage/doctest/sources.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/test.py` & `sagemath-repl-9.8rc0/sage/doctest/test.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/tests/interrupt_diehard.rst` & `sagemath-repl-9.8rc0/sage/doctest/tests/interrupt_diehard.rst`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/tests/sleep_and_raise.rst` & `sagemath-repl-9.8rc0/sage/doctest/tests/sleep_and_raise.rst`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/tests/tolerance.rst` & `sagemath-repl-9.8rc0/sage/doctest/tests/tolerance.rst`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/doctest/util.py` & `sagemath-repl-9.8rc0/sage/doctest/util.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/misc/banner.py` & `sagemath-repl-9.8rc0/sage/misc/banner.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/misc/sage_eval.py` & `sagemath-repl-9.8rc0/sage/misc/sage_eval.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/misc/sage_input.py` & `sagemath-repl-9.8rc0/sage/misc/sage_input.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/misc/sagedoc.py` & `sagemath-repl-9.8rc0/sage/misc/sagedoc.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/__init__.py` & `sagemath-repl-9.8rc0/sage/repl/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/attach.py` & `sagemath-repl-9.8rc0/sage/repl/attach.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/configuration.py` & `sagemath-repl-9.8rc0/sage/repl/configuration.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/display/fancy_repr.py` & `sagemath-repl-9.8rc0/sage/repl/display/fancy_repr.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/display/formatter.py` & `sagemath-repl-9.8rc0/sage/repl/display/formatter.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/display/jsmol_iframe.py` & `sagemath-repl-9.8rc0/sage/repl/display/jsmol_iframe.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/display/pretty_print.py` & `sagemath-repl-9.8rc0/sage/repl/display/pretty_print.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/display/util.py` & `sagemath-repl-9.8rc0/sage/repl/display/util.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/image.py` & `sagemath-repl-9.8rc0/sage/repl/image.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/inputhook.py` & `sagemath-repl-9.8rc0/sage/repl/inputhook.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/interface_magic.py` & `sagemath-repl-9.8rc0/sage/repl/interface_magic.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/interpreter.py` & `sagemath-repl-9.8rc0/sage/repl/interpreter.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_extension.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_extension.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_kernel/install.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_kernel/install.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_kernel/interact.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_kernel/interact.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_kernel/kernel.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_kernel/kernel.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_kernel/widgets.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_kernel/widgets.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_kernel/widgets_sagenb.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_kernel/widgets_sagenb.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/ipython_tests.py` & `sagemath-repl-9.8rc0/sage/repl/ipython_tests.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/load.py` & `sagemath-repl-9.8rc0/sage/repl/load.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/preparse.py` & `sagemath-repl-9.8rc0/sage/repl/preparse.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/prompts.py` & `sagemath-repl-9.8rc0/sage/repl/prompts.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/backend_base.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/backend_base.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/backend_doctest.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/backend_doctest.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/backend_emacs.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/backend_emacs.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/backend_ipython.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/backend_ipython.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/buffer.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/buffer.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/display_manager.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/display_manager.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.avi` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.avi`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.canvas3d` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.canvas3d`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.flv` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.flv`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.jpg` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.jpg`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.mkv` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.mkv`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.mov` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.mov`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.mp4` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.mp4`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.ogv` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.ogv`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.pdf` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.pdf`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.png` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.png`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.svg` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.svg`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.webm` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.webm`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example.wmv` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example.wmv`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/example_jmol.spt.zip` & `sagemath-repl-9.8rc0/sage/repl/rich_output/example_jmol.spt.zip`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_basic.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_basic.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_browser.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_browser.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_catalog.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_catalog.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_graphics.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_graphics.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_graphics3d.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_graphics3d.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/output_video.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/output_video.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/preferences.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/preferences.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/pretty_print.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/pretty_print.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/rich_output/test_backend.py` & `sagemath-repl-9.8rc0/sage/repl/rich_output/test_backend.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sage/repl/user_globals.py` & `sagemath-repl-9.8rc0/sage/repl/user_globals.py`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/sagemath_repl.egg-info/PKG-INFO` & `sagemath-repl-9.8rc0/sagemath_repl.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-repl
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: System and software environment
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-repl-9.8b7/sagemath_repl.egg-info/SOURCES.txt` & `sagemath-repl-9.8rc0/sagemath_repl.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/setup.cfg` & `sagemath-repl-9.8rc0/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -22,16 +22,16 @@
 	Programming Language :: Python :: 3.11
 	Programming Language :: Python :: Implementation :: CPython
 	Topic :: Scientific/Engineering :: Mathematics
 
 [options]
 python_requires = >=3.8, <3.12
 install_requires = 
-	sagemath-objects ~= 9.8b7
-	sagemath-environment ~= 9.8b7
+	sagemath-objects ~= 9.8rc0
+	sagemath-environment ~= 9.8rc0
 	ipython >=7.13.0
 	ipywidgets >=7.5.1
 py_modules = 
 	sage.all__sagemath_repl
 	sage.misc.all__sagemath_repl
 	sage.misc.banner
 	sage.misc.sagedoc
```

### Comparing `sagemath-repl-9.8b7/setup.cfg.m4` & `sagemath-repl-9.8rc0/setup.cfg.m4`

 * *Files identical despite different names*

### Comparing `sagemath-repl-9.8b7/tox.ini` & `sagemath-repl-9.8rc0/tox.ini`

 * *Files 4% similar despite different names*

```diff
@@ -33,15 +33,15 @@
     # Sage scripts such as sage-runtests like to use $HOME/.sage
                              HOME={envdir}
     # We supply pip options by environment variables so that they
     # apply both to the installation of the dependencies and of the package
     sagewheels:              PIP_FIND_LINKS=file://{env:SAGE_SPKG_WHEELS:{env:SAGE_VENV:{toxinidir}/../../../../venv}/var/lib/sage/wheels}
     nopypi:                  PIP_NO_INDEX=true
 
-whitelist_externals =
+allowlist_externals =
     bash
 
 commands =
     # Beware of the treacherous non-src layout. "./sage/" shadows the installed sage package.
     {envpython} -c 'import sys; "" in sys.path and sys.path.remove(""); import sage.repl.all; import sage.doctest.all'
 
     bash -c 'cd bin && SAGE_SRC=$({envpython} -c "from sage.env import SAGE_SRC; print(SAGE_SRC)") && sage-runtests --environment=sage.all__sagemath_repl --initial --optional=sage $SAGE_SRC/sage/repl $SAGE_SRC/sage/doctest $SAGE_SRC/sage/misc/sage_input.py $SAGE_SRC/sage/misc/sage_eval.py || echo "(lots of doctest failures are expected)"'
```

