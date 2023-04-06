# Comparing `tmp/coverage-7.2.2.tar.gz` & `tmp/coverage-7.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "coverage-7.2.2.tar", last modified: Thu Mar 16 12:42:09 2023, max compression
+gzip compressed data, was "coverage-7.2.3.tar", last modified: Thu Apr  6 14:06:56 2023, max compression
```

## Comparing `coverage-7.2.2.tar` & `coverage-7.2.3.tar`

### file list

```diff
@@ -1,421 +1,424 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.660595 coverage-7.2.2/
--rw-r--r--   0 runner    (1001) docker     (123)      873 2023-03-16 12:41:52.000000 coverage-7.2.2/.editorconfig
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-03-16 12:41:52.000000 coverage-7.2.2/.git-blame-ignore-revs
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.572594 coverage-7.2.2/.github/
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/FUNDING.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.572594 coverage-7.2.2/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (123)      926 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/ISSUE_TEMPLATE/bug_report.md
--rw-r--r--   0 runner    (1001) docker     (123)      592 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/ISSUE_TEMPLATE/config.yml
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/ISSUE_TEMPLATE/feature_request.md
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/SECURITY.md
--rw-r--r--   0 runner    (1001) docker     (123)      386 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.576594 coverage-7.2.2/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     2406 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/codeql-analysis.yml
--rw-r--r--   0 runner    (1001) docker     (123)     7558 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/coverage.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1125 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/dependency-review.yml
--rw-r--r--   0 runner    (1001) docker     (123)     8301 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/kit.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2687 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/python-nightly.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/quality.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2914 2023-03-16 12:41:52.000000 coverage-7.2.2/.github/workflows/testsuite.yml
--rw-r--r--   0 runner    (1001) docker     (123)      527 2023-03-16 12:41:52.000000 coverage-7.2.2/.readthedocs.yml
--rw-r--r--   0 runner    (1001) docker     (123)    44115 2023-03-16 12:41:52.000000 coverage-7.2.2/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-03-16 12:41:52.000000 coverage-7.2.2/CONTRIBUTORS.txt
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-16 12:41:52.000000 coverage-7.2.2/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-03-16 12:41:52.000000 coverage-7.2.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     9046 2023-03-16 12:41:52.000000 coverage-7.2.2/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-03-16 12:41:52.000000 coverage-7.2.2/NOTICE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     9436 2023-03-16 12:42:09.660595 coverage-7.2.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7747 2023-03-16 12:41:52.000000 coverage-7.2.2/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)      421 2023-03-16 12:41:52.000000 coverage-7.2.2/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.576594 coverage-7.2.2/ci/
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/README.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/comment_on_fixes.py
--rw-r--r--   0 runner    (1001) docker     (123)     2140 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/download_gha_artifacts.py
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/ghrel_template.md.j2
--rw-r--r--   0 runner    (1001) docker     (123)     3541 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/parse_relnotes.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-03-16 12:41:52.000000 coverage-7.2.2/ci/trigger_build_kits.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.588594 coverage-7.2.2/coverage/
--rw-r--r--   0 runner    (1001) docker     (123)     1296 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3753 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/annotate.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/bytecode.py
--rw-r--r--   0 runner    (1001) docker     (123)    34436 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/cmdline.py
--rw-r--r--   0 runner    (1001) docker     (123)    20553 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/collector.py
--rw-r--r--   0 runner    (1001) docker     (123)    21989 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/context.py
--rw-r--r--   0 runner    (1001) docker     (123)    51845 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/control.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.588594 coverage-7.2.2/coverage/ctracer/
--rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/datastack.c
--rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/datastack.h
--rw-r--r--   0 runner    (1001) docker     (123)     3264 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/filedisp.c
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/filedisp.h
--rw-r--r--   0 runner    (1001) docker     (123)     1588 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/module.c
--rw-r--r--   0 runner    (1001) docker     (123)      710 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/stats.h
--rw-r--r--   0 runner    (1001) docker     (123)    35213 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/tracer.c
--rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/tracer.h
--rw-r--r--   0 runner    (1001) docker     (123)     2309 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/ctracer/util.h
--rw-r--r--   0 runner    (1001) docker     (123)     7508 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/data.py
--rw-r--r--   0 runner    (1001) docker     (123)    16810 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/debug.py
--rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/disposition.py
--rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/env.py
--rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    12133 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/execfile.py
--rw-r--r--   0 runner    (1001) docker     (123)    19388 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/files.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.588594 coverage-7.2.2/coverage/fullcoverage/
--rw-r--r--   0 runner    (1001) docker     (123)     2423 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/fullcoverage/encodings.py
--rw-r--r--   0 runner    (1001) docker     (123)    21654 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/html.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.592594 coverage-7.2.2/coverage/htmlfiles/
--rw-r--r--   0 runner    (1001) docker     (123)    20650 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/coverage_html.js
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/favicon_32.png
--rw-r--r--   0 runner    (1001) docker     (123)     5400 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/keybd_closed.png
--rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/keybd_open.png
--rw-r--r--   0 runner    (1001) docker     (123)     6437 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/pyfile.html
--rw-r--r--   0 runner    (1001) docker     (123)    12429 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/style.css
--rw-r--r--   0 runner    (1001) docker     (123)    17425 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/htmlfiles/style.scss
--rw-r--r--   0 runner    (1001) docker     (123)    23900 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/inorout.py
--rw-r--r--   0 runner    (1001) docker     (123)     4749 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/jsonreport.py
--rw-r--r--   0 runner    (1001) docker     (123)     4859 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/lcovreport.py
--rw-r--r--   0 runner    (1001) docker     (123)    11829 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/misc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3846 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/multiproc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4669 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/numbits.py
--rw-r--r--   0 runner    (1001) docker     (123)    56643 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     7805 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/phystokens.py
--rw-r--r--   0 runner    (1001) docker     (123)    19525 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)    10351 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/plugin_support.py
--rw-r--r--   0 runner    (1001) docker     (123)       72 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/python.py
--rw-r--r--   0 runner    (1001) docker     (123)    14420 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/pytracer.py
--rw-r--r--   0 runner    (1001) docker     (123)     4068 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/report.py
--rw-r--r--   0 runner    (1001) docker     (123)    13384 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/results.py
--rw-r--r--   0 runner    (1001) docker     (123)    51295 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/sqldata.py
--rw-r--r--   0 runner    (1001) docker     (123)    10618 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/summary.py
--rw-r--r--   0 runner    (1001) docker     (123)    10952 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/templite.py
--rw-r--r--   0 runner    (1001) docker     (123)     7569 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/tomlconfig.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/tracer.pyi
--rw-r--r--   0 runner    (1001) docker     (123)     5526 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/version.py
--rw-r--r--   0 runner    (1001) docker     (123)     9737 2023-03-16 12:41:52.000000 coverage-7.2.2/coverage/xmlreport.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.588594 coverage-7.2.2/coverage.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     9436 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     9146 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      122 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-16 12:42:09.000000 coverage-7.2.2/coverage.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.600594 coverage-7.2.2/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.600594 coverage-7.2.2/doc/_static/
--rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/_static/coverage.css
--rw-r--r--   0 runner    (1001) docker     (123)     1685 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api.rst
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api_coverage.rst
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api_coveragedata.rst
--rw-r--r--   0 runner    (1001) docker     (123)      391 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api_exceptions.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api_module.rst
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/api_plugin.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4034 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/branch.rst
--rw-r--r--   0 runner    (1001) docker     (123)   112598 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/changes.rst
--rw-r--r--   0 runner    (1001) docker     (123)    44128 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/cmd.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8509 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)    18158 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/config.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3871 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/contexts.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10449 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/dbschema.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2291 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/dict.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3986 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/excluding.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7372 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/howitworks.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7213 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/install.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.600594 coverage-7.2.2/doc/media/
--rw-r--r--   0 runner    (1001) docker     (123)     4069 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White.png
--rw-r--r--   0 runner    (1001) docker     (123)     7070 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
--rw-r--r--   0 runner    (1001) docker     (123)   165210 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/media/sleepy-snake-600.png
--rw-r--r--   0 runner    (1001) docker     (123)    24168 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/media/sleepy-snake-circle-150.png
--rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/plugins.rst
--rw-r--r--   0 runner    (1001) docker     (123)    12524 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/python-coverage.1.txt
--rw-r--r--   0 runner    (1001) docker     (123)      477 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/requirements.in
--rw-r--r--   0 runner    (1001) docker     (123)    20477 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/requirements.pip
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.600594 coverage-7.2.2/doc/sample_html/
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/sample_html/favicon_32.png
--rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/sample_html/keybd_closed.png
--rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/sample_html/keybd_open.png
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/sleepy.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4686 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/source.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4297 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/subprocess.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/trouble.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6936 2023-03-16 12:41:52.000000 coverage-7.2.2/doc/whatsnew5x.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3714 2023-03-16 12:41:52.000000 coverage-7.2.2/howto.txt
--rw-r--r--   0 runner    (1001) docker     (123)    15362 2023-03-16 12:41:52.000000 coverage-7.2.2/igor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.608594 coverage-7.2.2/lab/
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/README.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.608594 coverage-7.2.2/lab/benchmark/
--rw-r--r--   0 runner    (1001) docker     (123)    18339 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/benchmark/benchmark.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/benchmark/empty.py
--rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/benchmark/run.py
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/bpo_prelude.py
--rw-r--r--   0 runner    (1001) docker     (123)      291 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/branch_trace.py
--rw-r--r--   0 runner    (1001) docker     (123)     2701 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/branches.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2066 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/compare_times.sh
--rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/coverage-03.dtd
--rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/coverage-04.dtd
--rw-r--r--   0 runner    (1001) docker     (123)     2191 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/extract_code.py
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/find_class.py
--rw-r--r--   0 runner    (1001) docker     (123)     9634 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/genpy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3415 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/goals.py
--rw-r--r--   0 runner    (1001) docker     (123)     2791 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/hack_pyc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/new-data.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.608594 coverage-7.2.2/lab/notes/
--rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/notes/bug1303.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/notes/pypy-738-decorated-functions.txt
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/parse_all.py
--rw-r--r--   0 runner    (1001) docker     (123)     7246 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      618 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/platform_info.py
--rw-r--r--   0 runner    (1001) docker     (123)      778 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/run_trace.py
--rw-r--r--   0 runner    (1001) docker     (123)     2168 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/select_contexts.py
--rw-r--r--   0 runner    (1001) docker     (123)      300 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/show_ast.py
--rw-r--r--   0 runner    (1001) docker     (123)      480 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/show_platform.py
--rw-r--r--   0 runner    (1001) docker     (123)     6093 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/show_pyc.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/lab/treetopy.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2874 2023-03-16 12:41:52.000000 coverage-7.2.2/metacov.ini
--rw-r--r--   0 runner    (1001) docker     (123)     9050 2023-03-16 12:41:52.000000 coverage-7.2.2/pylintrc
--rw-r--r--   0 runner    (1001) docker     (123)     1113 2023-03-16 12:41:52.000000 coverage-7.2.2/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.616594 coverage-7.2.2/requirements/
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/dev.in
--rw-r--r--   0 runner    (1001) docker     (123)    37678 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/dev.pip
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/kit.in
--rw-r--r--   0 runner    (1001) docker     (123)     4187 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/kit.pip
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/light-threads.in
--rw-r--r--   0 runner    (1001) docker     (123)    19793 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/light-threads.pip
--rw-r--r--   0 runner    (1001) docker     (123)    48562 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/lint.pip
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/mypy.in
--rw-r--r--   0 runner    (1001) docker     (123)     8198 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/mypy.pip
--rw-r--r--   0 runner    (1001) docker     (123)      613 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pins.pip
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pip-tools.in
--rw-r--r--   0 runner    (1001) docker     (123)     2792 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pip-tools.pip
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pip.in
--rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pip.pip
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pytest.in
--rw-r--r--   0 runner    (1001) docker     (123)     3620 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/pytest.pip
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/tox.in
--rw-r--r--   0 runner    (1001) docker     (123)     3663 2023-03-16 12:41:52.000000 coverage-7.2.2/requirements/tox.pip
--rw-r--r--   0 runner    (1001) docker     (123)      620 2023-03-16 12:42:09.660595 coverage-7.2.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     7308 2023-03-16 12:41:52.000000 coverage-7.2.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.632594 coverage-7.2.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6924 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/balance_xdist_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)     4410 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)    20466 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/coveragetest.py
--rw-r--r--   0 runner    (1001) docker     (123)      366 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/covmodzip1.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.632594 coverage-7.2.2/tests/gold/
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.560594 coverage-7.2.2/tests/gold/annotate/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.632594 coverage-7.2.2/tests/gold/annotate/anno_dir/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/anno_dir/d_80084bf2fba02475___init__.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/anno_dir/d_80084bf2fba02475_a.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/anno_dir/d_b039179a8a4ce2c2___init__.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       53 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/anno_dir/d_b039179a8a4ce2c2_b.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/anno_dir/multi.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/encodings/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/encodings/utf8.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/mae/
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/mae/mae.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/multi/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/multi/a/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/multi/a/__init__.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/multi/a/a.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/multi/b/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/multi/b/__init__.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/multi/b/b.py,cover
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/multi/multi.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/annotate/white/
--rw-r--r--   0 runner    (1001) docker     (123)      527 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/annotate/white/white.py,cover
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/html/
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/Makefile
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/html/a/
--rw-r--r--   0 runner    (1001) docker     (123)     5430 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/a/a_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     3798 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/a/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.636595 coverage-7.2.2/tests/gold/html/b_branch/
--rw-r--r--   0 runner    (1001) docker     (123)    10830 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/b_branch/b_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4197 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/b_branch/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.640595 coverage-7.2.2/tests/gold/html/bom/
--rw-r--r--   0 runner    (1001) docker     (123)     7444 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/bom/bom_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     3806 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/bom/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.640595 coverage-7.2.2/tests/gold/html/isolatin1/
--rw-r--r--   0 runner    (1001) docker     (123)     3833 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/isolatin1/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     5444 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/isolatin1/isolatin1_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.640595 coverage-7.2.2/tests/gold/html/omit_1/
--rw-r--r--   0 runner    (1001) docker     (123)     4606 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_1/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_1/m1_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_1/m2_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_1/m3_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_1/main_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.640595 coverage-7.2.2/tests/gold/html/omit_2/
--rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_2/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_2/m2_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_2/m3_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_2/main_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.640595 coverage-7.2.2/tests/gold/html/omit_3/
--rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_3/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_3/m3_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_3/main_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.644595 coverage-7.2.2/tests/gold/html/omit_4/
--rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_4/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_4/m1_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_4/m3_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_4/main_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.644595 coverage-7.2.2/tests/gold/html/omit_5/
--rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_5/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_5/m1_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/omit_5/main_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.644595 coverage-7.2.2/tests/gold/html/other/
--rw-r--r--   0 runner    (1001) docker     (123)     5374 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/other/blah_blah_other_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     5598 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/other/here_py.html
--rw-r--r--   0 runner    (1001) docker     (123)     4233 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/other/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.644595 coverage-7.2.2/tests/gold/html/partial/
--rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/partial/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     8167 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/partial/partial_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.644595 coverage-7.2.2/tests/gold/html/partial_626/
--rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/partial_626/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     8359 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/partial_626/partial_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/html/styled/
--rw-r--r--   0 runner    (1001) docker     (123)     5495 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/styled/a_py.html
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/styled/extra.css
--rw-r--r--   0 runner    (1001) docker     (123)     3863 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/styled/index.html
--rw-r--r--   0 runner    (1001) docker     (123)    12429 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/styled/style.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/html/support/
--rw-r--r--   0 runner    (1001) docker     (123)    20629 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/support/coverage_html.js
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/support/favicon_32.png
--rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/support/keybd_closed.png
--rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/support/keybd_open.png
--rw-r--r--   0 runner    (1001) docker     (123)    12429 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/support/style.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/html/unicode/
--rw-r--r--   0 runner    (1001) docker     (123)     3825 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/unicode/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     5379 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/html/unicode/unicode_py.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.564594 coverage-7.2.2/tests/gold/testing/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/testing/getty/
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/testing/getty/gettysburg.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/testing/xml/
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/testing/xml/output.xml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.564594 coverage-7.2.2/tests/gold/xml/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/xml/x_xml/
--rw-r--r--   0 runner    (1001) docker     (123)      945 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/xml/x_xml/coverage.xml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/gold/xml/y_xml_branch/
--rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/gold/xml/y_xml_branch/coverage.xml
--rw-r--r--   0 runner    (1001) docker     (123)     6624 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/goldtest.py
--rw-r--r--   0 runner    (1001) docker     (123)    10386 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.648595 coverage-7.2.2/tests/js/
--rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/js/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     5770 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/js/tests.js
--rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/mixins.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/aa/
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/afile.odd.py
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/afile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/aa/bb/
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb/bfile.odd.py
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb/bfile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/aa/bb/cc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb/cc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb/cc/cfile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/aa/bb.odd/
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/bb.odd/bfile.py
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/aa/zfile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/ambiguous/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/ambiguous/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/ambiguous/pkg1/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/ambiguous/pkg1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/ambiguous/pkg1/ambiguous.py
--rw-r--r--   0 runner    (1001) docker     (123)      212 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/covmod1.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.564594 coverage-7.2.2/tests/modules/namespace_420/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.652595 coverage-7.2.2/tests/modules/namespace_420/sub1/
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/namespace_420/sub1/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/modules/pkg1/
--rw-r--r--   0 runner    (1001) docker     (123)       73 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/p1a.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/p1b.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/p1c.py
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/runmod2.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/modules/pkg1/sub/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/sub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/sub/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/sub/ps1a.py
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg1/sub/runmod3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/modules/pkg2/
--rw-r--r--   0 runner    (1001) docker     (123)      113 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg2/p2a.py
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/pkg2/p2b.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/modules/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/plugins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/plugins/a_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      518 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/plugins/another.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/modules/process_test/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/process_test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3542 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/process_test/try_execfile.py
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/runmod1.py
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/modules/usepkgs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.568594 coverage-7.2.2/tests/moremodules/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.568594 coverage-7.2.2/tests/moremodules/namespace_420/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.656595 coverage-7.2.2/tests/moremodules/namespace_420/sub2/
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/namespace_420/sub2/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.660595 coverage-7.2.2/tests/moremodules/othermods/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/othera.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/otherb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.660595 coverage-7.2.2/tests/moremodules/othermods/sub/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/sub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/sub/osa.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/moremodules/othermods/sub/osb.py
--rw-r--r--   0 runner    (1001) docker     (123)     2813 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/osinfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/plugin1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/plugin2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/plugin_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.660595 coverage-7.2.2/tests/qunit/
--rw-r--r--   0 runner    (1001) docker     (123)     6115 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/qunit/jquery.tmpl.min.js
--rw-r--r--   0 runner    (1001) docker     (123)     1290 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/stress_phystoken.tok
--rw-r--r--   0 runner    (1001) docker     (123)     1156 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/stress_phystoken_dos.tok
--rw-r--r--   0 runner    (1001) docker     (123)     3766 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_annotate.py
--rw-r--r--   0 runner    (1001) docker     (123)    61833 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    63100 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_arcs.py
--rw-r--r--   0 runner    (1001) docker     (123)    44163 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_cmdline.py
--rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_collector.py
--rw-r--r--   0 runner    (1001) docker     (123)    26195 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_concurrency.py
--rw-r--r--   0 runner    (1001) docker     (123)    31526 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    10307 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_context.py
--rw-r--r--   0 runner    (1001) docker     (123)    50465 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_coverage.py
--rw-r--r--   0 runner    (1001) docker     (123)    37653 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_data.py
--rw-r--r--   0 runner    (1001) docker     (123)    10474 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_debug.py
--rw-r--r--   0 runner    (1001) docker     (123)    10991 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_execfile.py
--rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_filereporter.py
--rw-r--r--   0 runner    (1001) docker     (123)    27463 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_files.py
--rw-r--r--   0 runner    (1001) docker     (123)     6886 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_goldtest.py
--rw-r--r--   0 runner    (1001) docker     (123)    48499 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_html.py
--rw-r--r--   0 runner    (1001) docker     (123)     6972 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_json.py
--rw-r--r--   0 runner    (1001) docker     (123)     9850 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_lcov.py
--rw-r--r--   0 runner    (1001) docker     (123)     5144 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_misc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2995 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_mixins.py
--rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_numbits.py
--rw-r--r--   0 runner    (1001) docker     (123)    22363 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_oddball.py
--rw-r--r--   0 runner    (1001) docker     (123)    19838 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     7546 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_phystokens.py
--rw-r--r--   0 runner    (1001) docker     (123)    43888 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_plugins.py
--rw-r--r--   0 runner    (1001) docker     (123)    47552 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_process.py
--rw-r--r--   0 runner    (1001) docker     (123)     2085 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_python.py
--rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_report.py
--rw-r--r--   0 runner    (1001) docker     (123)     5948 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_results.py
--rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    39894 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_summary.py
--rw-r--r--   0 runner    (1001) docker     (123)    12072 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_templite.py
--rw-r--r--   0 runner    (1001) docker     (123)    17034 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_testing.py
--rw-r--r--   0 runner    (1001) docker     (123)    13685 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_venv.py
--rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_version.py
--rw-r--r--   0 runner    (1001) docker     (123)    21585 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/test_xml.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.568594 coverage-7.2.2/tests/zipsrc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 12:42:09.660595 coverage-7.2.2/tests/zipsrc/zip1/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/zipsrc/zip1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      214 2023-03-16 12:41:52.000000 coverage-7.2.2/tests/zipsrc/zip1/zip1.py
--rw-r--r--   0 runner    (1001) docker     (123)     3617 2023-03-16 12:41:52.000000 coverage-7.2.2/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/
+-rw-r--r--   0 runner    (1001) docker     (123)      873 2023-04-06 14:06:42.000000 coverage-7.2.3/.editorconfig
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-04-06 14:06:42.000000 coverage-7.2.3/.git-blame-ignore-revs
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.129750 coverage-7.2.3/.github/
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/FUNDING.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.133750 coverage-7.2.3/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (123)      926 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-r--r--   0 runner    (1001) docker     (123)      592 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/ISSUE_TEMPLATE/config.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/ISSUE_TEMPLATE/feature_request.md
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/SECURITY.md
+-rw-r--r--   0 runner    (1001) docker     (123)      386 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.133750 coverage-7.2.3/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     2406 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/codeql-analysis.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     7541 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/coverage.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1125 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/dependency-review.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     8249 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/kit.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2670 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/python-nightly.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2466 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/quality.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2897 2023-04-06 14:06:42.000000 coverage-7.2.3/.github/workflows/testsuite.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      527 2023-04-06 14:06:42.000000 coverage-7.2.3/.readthedocs.yml
+-rw-r--r--   0 runner    (1001) docker     (123)    45068 2023-04-06 14:06:42.000000 coverage-7.2.3/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-04-06 14:06:42.000000 coverage-7.2.3/CONTRIBUTORS.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-04-06 14:06:42.000000 coverage-7.2.3/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-04-06 14:06:42.000000 coverage-7.2.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     9507 2023-04-06 14:06:42.000000 coverage-7.2.3/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)      681 2023-04-06 14:06:42.000000 coverage-7.2.3/NOTICE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     9545 2023-04-06 14:06:56.177750 coverage-7.2.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7856 2023-04-06 14:06:42.000000 coverage-7.2.3/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-06 14:06:42.000000 coverage-7.2.3/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.133750 coverage-7.2.3/ci/
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/README.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/comment_on_fixes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2140 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/download_gha_artifacts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/ghrel_template.md.j2
+-rw-r--r--   0 runner    (1001) docker     (123)     3541 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/parse_relnotes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-06 14:06:42.000000 coverage-7.2.3/ci/trigger_build_kits.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.137750 coverage-7.2.3/coverage/
+-rw-r--r--   0 runner    (1001) docker     (123)     1296 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3753 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/annotate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/bytecode.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34436 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/cmdline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20553 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/collector.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21989 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51867 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/control.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.141750 coverage-7.2.3/coverage/ctracer/
+-rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/datastack.c
+-rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/datastack.h
+-rw-r--r--   0 runner    (1001) docker     (123)     3264 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/filedisp.c
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/filedisp.h
+-rw-r--r--   0 runner    (1001) docker     (123)     1588 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/module.c
+-rw-r--r--   0 runner    (1001) docker     (123)      710 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/stats.h
+-rw-r--r--   0 runner    (1001) docker     (123)    35213 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/tracer.c
+-rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/tracer.h
+-rw-r--r--   0 runner    (1001) docker     (123)     2309 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/ctracer/util.h
+-rw-r--r--   0 runner    (1001) docker     (123)     7508 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16810 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/disposition.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12133 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/execfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19388 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/files.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.141750 coverage-7.2.3/coverage/fullcoverage/
+-rw-r--r--   0 runner    (1001) docker     (123)     2423 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/fullcoverage/encodings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23060 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/html.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.141750 coverage-7.2.3/coverage/htmlfiles/
+-rw-r--r--   0 runner    (1001) docker     (123)    21359 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/coverage_html.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/favicon_32.png
+-rw-r--r--   0 runner    (1001) docker     (123)     5400 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/keybd_closed.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/keybd_open.png
+-rw-r--r--   0 runner    (1001) docker     (123)     6434 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/pyfile.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12387 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/style.css
+-rw-r--r--   0 runner    (1001) docker     (123)    17356 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/htmlfiles/style.scss
+-rw-r--r--   0 runner    (1001) docker     (123)    23900 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/inorout.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4749 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/jsonreport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4859 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/lcovreport.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11829 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/misc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3846 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/multiproc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4669 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/numbits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    56643 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7805 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/phystokens.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19525 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10351 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/plugin_support.py
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/python.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14420 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/pytracer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4068 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13384 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/results.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51295 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/sqldata.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10618 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10952 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/templite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7569 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/tomlconfig.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/tracer.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)     5526 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9737 2023-04-06 14:06:42.000000 coverage-7.2.3/coverage/xmlreport.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.141750 coverage-7.2.3/coverage.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     9545 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     9225 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:06:55.000000 coverage-7.2.3/coverage.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 14:06:56.000000 coverage-7.2.3/coverage.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.145750 coverage-7.2.3/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.145750 coverage-7.2.3/doc/_static/
+-rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/_static/coverage.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1685 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api_coverage.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api_coveragedata.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      391 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api_exceptions.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api_module.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/api_plugin.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4034 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/branch.rst
+-rw-r--r--   0 runner    (1001) docker     (123)   112598 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/changes.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    44128 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/cmd.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8683 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18158 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/config.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3871 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/contexts.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    13160 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/contributing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/dbschema.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2439 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/dict.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     3986 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/excluding.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7371 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/howitworks.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7213 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/install.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.149750 coverage-7.2.3/doc/media/
+-rw-r--r--   0 runner    (1001) docker     (123)     4069 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White.png
+-rw-r--r--   0 runner    (1001) docker     (123)     7070 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
+-rw-r--r--   0 runner    (1001) docker     (123)   165210 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/media/sleepy-snake-600.png
+-rw-r--r--   0 runner    (1001) docker     (123)    24168 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/media/sleepy-snake-circle-150.png
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/plugins.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    12524 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/python-coverage.1.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      477 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/requirements.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2136 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/requirements.pip
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.149750 coverage-7.2.3/doc/sample_html/
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/sample_html/favicon_32.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/sample_html/keybd_closed.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/sample_html/keybd_open.png
+-rw-r--r--   0 runner    (1001) docker     (123)      643 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/sleepy.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4686 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/source.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4297 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/subprocess.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/trouble.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6936 2023-04-06 14:06:42.000000 coverage-7.2.3/doc/whatsnew5x.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-04-06 14:06:42.000000 coverage-7.2.3/howto.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    15362 2023-04-06 14:06:42.000000 coverage-7.2.3/igor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.149750 coverage-7.2.3/lab/
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/README.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.153750 coverage-7.2.3/lab/benchmark/
+-rw-r--r--   0 runner    (1001) docker     (123)    18339 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/benchmark/benchmark.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/benchmark/empty.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/benchmark/run.py
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/bpo_prelude.py
+-rw-r--r--   0 runner    (1001) docker     (123)      291 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/branch_trace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2701 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/branches.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2066 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/compare_times.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/coverage-03.dtd
+-rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/coverage-04.dtd
+-rw-r--r--   0 runner    (1001) docker     (123)     2191 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/extract_code.py
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/find_class.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9634 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/genpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3415 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/goals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2791 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/hack_pyc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/new-data.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.153750 coverage-7.2.3/lab/notes/
+-rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/notes/bug1303.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/notes/pypy-738-decorated-functions.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/parse_all.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7246 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      618 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/platform_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)      778 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/run_trace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2168 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/select_contexts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      300 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/show_ast.py
+-rw-r--r--   0 runner    (1001) docker     (123)      480 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/show_platform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6093 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/show_pyc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/lab/treetopy.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2874 2023-04-06 14:06:42.000000 coverage-7.2.3/metacov.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     9050 2023-04-06 14:06:42.000000 coverage-7.2.3/pylintrc
+-rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-04-06 14:06:42.000000 coverage-7.2.3/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.153750 coverage-7.2.3/requirements/
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/dev.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3849 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/dev.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/kit.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/kit.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/light-threads.in
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/light-threads.pip
+-rw-r--r--   0 runner    (1001) docker     (123)     5464 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/lint.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/mypy.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/mypy.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      613 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pins.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pip-tools.in
+-rw-r--r--   0 runner    (1001) docker     (123)      752 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pip-tools.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pip.in
+-rw-r--r--   0 runner    (1001) docker     (123)      627 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pip.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pytest.in
+-rw-r--r--   0 runner    (1001) docker     (123)      900 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/pytest.pip
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/tox.in
+-rw-r--r--   0 runner    (1001) docker     (123)      944 2023-04-06 14:06:42.000000 coverage-7.2.3/requirements/tox.pip
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-06 14:06:56.177750 coverage-7.2.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     7308 2023-04-06 14:06:42.000000 coverage-7.2.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6924 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/balance_xdist_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4410 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20466 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/coveragetest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      366 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/covmodzip1.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.125750 coverage-7.2.3/tests/gold/annotate/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/annotate/anno_dir/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/anno_dir/d_80084bf2fba02475___init__.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/anno_dir/d_80084bf2fba02475_a.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/anno_dir/d_b039179a8a4ce2c2___init__.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       53 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/anno_dir/d_b039179a8a4ce2c2_b.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/anno_dir/multi.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/annotate/encodings/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/encodings/utf8.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/annotate/mae/
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/mae/mae.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/annotate/multi/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.161750 coverage-7.2.3/tests/gold/annotate/multi/a/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/multi/a/__init__.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/multi/a/a.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/annotate/multi/b/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/multi/b/__init__.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/multi/b/b.py,cover
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/multi/multi.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/annotate/white/
+-rw-r--r--   0 runner    (1001) docker     (123)      527 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/annotate/white/white.py,cover
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/
+-rw-r--r--   0 runner    (1001) docker     (123)      967 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/Makefile
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/a/
+-rw-r--r--   0 runner    (1001) docker     (123)     5430 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/a/a_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     3798 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/a/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/b_branch/
+-rw-r--r--   0 runner    (1001) docker     (123)    10830 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/b_branch/b_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4197 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/b_branch/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/bom/
+-rw-r--r--   0 runner    (1001) docker     (123)     7444 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/bom/bom_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     3806 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/bom/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/contexts/
+-rw-r--r--   0 runner    (1001) docker     (123)     3864 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/contexts/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10713 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/contexts/two_tests_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/isolatin1/
+-rw-r--r--   0 runner    (1001) docker     (123)     3833 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/isolatin1/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     5444 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/isolatin1/isolatin1_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/omit_1/
+-rw-r--r--   0 runner    (1001) docker     (123)     4606 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_1/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_1/m1_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_1/m2_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_1/m3_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_1/main_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/omit_2/
+-rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_2/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_2/m2_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_2/m3_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_2/main_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.165750 coverage-7.2.3/tests/gold/html/omit_3/
+-rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_3/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_3/m3_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_3/main_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/omit_4/
+-rw-r--r--   0 runner    (1001) docker     (123)     4342 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_4/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4784 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_4/m1_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_4/m3_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_4/main_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/omit_5/
+-rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_5/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4788 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_5/m1_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6470 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/omit_5/main_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/other/
+-rw-r--r--   0 runner    (1001) docker     (123)     5374 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/other/blah_blah_other_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     5598 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/other/here_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)     4233 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/other/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/partial/
+-rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/partial/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8167 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/partial/partial_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/partial_626/
+-rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/partial_626/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8359 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/partial_626/partial_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/styled/
+-rw-r--r--   0 runner    (1001) docker     (123)     5495 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/styled/a_py.html
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/styled/extra.css
+-rw-r--r--   0 runner    (1001) docker     (123)     3863 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/styled/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12387 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/styled/style.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/support/
+-rw-r--r--   0 runner    (1001) docker     (123)    21359 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/support/coverage_html.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/support/favicon_32.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9004 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/support/keybd_closed.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9003 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/support/keybd_open.png
+-rw-r--r--   0 runner    (1001) docker     (123)    12387 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/support/style.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/html/unicode/
+-rw-r--r--   0 runner    (1001) docker     (123)     3825 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/unicode/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     5379 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/html/unicode/unicode_py.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.125750 coverage-7.2.3/tests/gold/testing/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/testing/getty/
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/testing/getty/gettysburg.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/testing/xml/
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/testing/xml/output.xml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.125750 coverage-7.2.3/tests/gold/xml/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/xml/x_xml/
+-rw-r--r--   0 runner    (1001) docker     (123)      945 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/xml/x_xml/coverage.xml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/gold/xml/y_xml_branch/
+-rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/gold/xml/y_xml_branch/coverage.xml
+-rw-r--r--   0 runner    (1001) docker     (123)     6835 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/goldtest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10386 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.169750 coverage-7.2.3/tests/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/js/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     5770 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/js/tests.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/mixins.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/aa/
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/afile.odd.py
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/afile.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/aa/bb/
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb/bfile.odd.py
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb/bfile.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/aa/bb/cc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb/cc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb/cc/cfile.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/aa/bb.odd/
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/bb.odd/bfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/aa/zfile.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/ambiguous/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/ambiguous/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/ambiguous/pkg1/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/ambiguous/pkg1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/ambiguous/pkg1/ambiguous.py
+-rw-r--r--   0 runner    (1001) docker     (123)      212 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/covmod1.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.125750 coverage-7.2.3/tests/modules/namespace_420/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/namespace_420/sub1/
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/namespace_420/sub1/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/pkg1/
+-rw-r--r--   0 runner    (1001) docker     (123)       73 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/p1a.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/p1b.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/p1c.py
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/runmod2.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/pkg1/sub/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/sub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/sub/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/sub/ps1a.py
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg1/sub/runmod3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/pkg2/
+-rw-r--r--   0 runner    (1001) docker     (123)      113 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg2/p2a.py
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/pkg2/p2b.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/plugins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/plugins/a_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      518 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/plugins/another.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.173750 coverage-7.2.3/tests/modules/process_test/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/process_test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3542 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/process_test/try_execfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/runmod1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/modules/usepkgs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.129750 coverage-7.2.3/tests/moremodules/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.129750 coverage-7.2.3/tests/moremodules/namespace_420/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/tests/moremodules/namespace_420/sub2/
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/namespace_420/sub2/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/tests/moremodules/othermods/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/othera.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/otherb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/tests/moremodules/othermods/sub/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/sub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/sub/osa.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/moremodules/othermods/sub/osb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2813 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/osinfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/plugin1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/plugin2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/plugin_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/tests/qunit/
+-rw-r--r--   0 runner    (1001) docker     (123)     6115 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/qunit/jquery.tmpl.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1290 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/stress_phystoken.tok
+-rw-r--r--   0 runner    (1001) docker     (123)     1156 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/stress_phystoken_dos.tok
+-rw-r--r--   0 runner    (1001) docker     (123)     3766 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_annotate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61833 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63100 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_arcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44163 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_cmdline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_collector.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27122 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_concurrency.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31526 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10307 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50465 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_coverage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37653 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10474 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10991 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_execfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_filereporter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27463 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_files.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7046 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_goldtest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48809 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_html.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6972 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9850 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_lcov.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5144 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_misc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2995 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_mixins.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_numbits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22363 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_oddball.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19838 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7546 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_phystokens.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43888 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_plugins.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47552 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_process.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2085 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_python.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5948 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39894 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12072 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_templite.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17034 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_testing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13685 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_venv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21585 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/test_xml.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.129750 coverage-7.2.3/tests/zipsrc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:56.177750 coverage-7.2.3/tests/zipsrc/zip1/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/zipsrc/zip1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      214 2023-04-06 14:06:42.000000 coverage-7.2.3/tests/zipsrc/zip1/zip1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3617 2023-04-06 14:06:42.000000 coverage-7.2.3/tox.ini
```

### Comparing `coverage-7.2.2/.editorconfig` & `coverage-7.2.3/.editorconfig`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/ISSUE_TEMPLATE/bug_report.md` & `coverage-7.2.3/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/ISSUE_TEMPLATE/config.yml` & `coverage-7.2.3/.github/ISSUE_TEMPLATE/config.yml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/ISSUE_TEMPLATE/feature_request.md` & `coverage-7.2.3/.github/ISSUE_TEMPLATE/feature_request.md`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/workflows/codeql-analysis.yml` & `coverage-7.2.3/.github/workflows/codeql-analysis.yml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/workflows/coverage.yml` & `coverage-7.2.3/.github/workflows/coverage.yml`

 * *Files 0% similar despite different names*

```diff
@@ -81,15 +81,15 @@
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install dependencies"
         run: |
           set -xe
           python -VV
           python -m site
-          python -m pip install --require-hashes -r requirements/tox.pip
+          python -m pip install -r requirements/tox.pip
 
       - name: "Run tox coverage for ${{ matrix.python-version }}"
         env:
           COVERAGE_COVERAGE: "yes"
           COVERAGE_CONTEXT: "${{ matrix.python-version }}.${{ matrix.os }}"
         run: |
           set -xe
```

### Comparing `coverage-7.2.2/.github/workflows/dependency-review.yml` & `coverage-7.2.3/.github/workflows/dependency-review.yml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/.github/workflows/kit.yml` & `coverage-7.2.3/.github/workflows/kit.yml`

 * *Files 2% similar despite different names*

```diff
@@ -43,15 +43,15 @@
 
 concurrency:
   group: "${{ github.workflow }}-${{ github.ref }}"
   cancel-in-progress: true
 
 jobs:
   wheels:
-    name: "Build ${{ matrix.os }} ${{ matrix.py }} ${{ matrix.arch }} wheels"
+    name: "${{ matrix.py }} ${{ matrix.os }} ${{ matrix.arch }} wheels"
     runs-on: ${{ matrix.os }}-latest
     strategy:
       matrix:
         include:
           # To change the matrix, edit the choices, then process this file with cog:
           #
           # $ make workflows
@@ -151,15 +151,15 @@
         with:
           python-version: "3.8"
           cache: pip
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install tools"
         run: |
-          python -m pip install --require-hashes -r requirements/kit.pip
+          python -m pip install -r requirements/kit.pip
 
       - name: "Build wheels"
         env:
           CIBW_BUILD: ${{ matrix.py }}-*
           CIBW_ARCHS: ${{ matrix.arch }}
           CIBW_ENVIRONMENT: PIP_DISABLE_PIP_VERSION_CHECK=1
           CIBW_TEST_COMMAND: python -c "from coverage.tracer import CTracer; print('CTracer OK!')"
@@ -173,30 +173,30 @@
       - name: "Upload wheels"
         uses: actions/upload-artifact@v3
         with:
           name: dist
           path: wheelhouse/*.whl
 
   sdist:
-    name: "Build source distribution"
+    name: "Source distribution"
     runs-on: ubuntu-latest
     steps:
       - name: "Check out the repo"
         uses: actions/checkout@v3
 
       - name: "Install Python 3.8"
         uses: actions/setup-python@v4
         with:
           python-version: "3.8"
           cache: pip
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install tools"
         run: |
-          python -m pip install --require-hashes -r requirements/kit.pip
+          python -m pip install -r requirements/kit.pip
 
       - name: "Build sdist"
         run: |
           python -m build
 
       - name: "List tarballs"
         run: |
@@ -205,15 +205,15 @@
       - name: "Upload sdist"
         uses: actions/upload-artifact@v3
         with:
           name: dist
           path: dist/*.tar.gz
 
   pypy:
-    name: "Build PyPy wheel"
+    name: "PyPy wheel"
     runs-on: ubuntu-latest
     steps:
       - name: "Check out the repo"
         uses: actions/checkout@v3
 
       - name: "Install PyPy"
         uses: actions/setup-python@v4
```

### Comparing `coverage-7.2.2/.github/workflows/python-nightly.yml` & `coverage-7.2.3/.github/workflows/python-nightly.yml`

 * *Files 3% similar despite different names*

```diff
@@ -77,12 +77,12 @@
           python -VV
           python -m site
           python -m coverage debug sys
           python -m coverage debug pybehave
 
       - name: "Install dependencies"
         run: |
-          python -m pip install --require-hashes -r requirements/tox.pip
+          python -m pip install -r requirements/tox.pip
 
       - name: "Run tox"
         run: |
           python -m tox -- -rfsEX
```

### Comparing `coverage-7.2.2/.github/workflows/quality.yml` & `coverage-7.2.3/.github/workflows/quality.yml`

 * *Files 5% similar despite different names*

```diff
@@ -42,15 +42,15 @@
         with:
           python-version: "3.7" # Minimum of PYVERSIONS
           cache: pip
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install dependencies"
         run: |
-          python -m pip install --require-hashes -r requirements/tox.pip
+          python -m pip install -r requirements/tox.pip
 
       - name: "Tox lint"
         run: |
           python -m tox -e lint
 
   mypy:
     name: "Check types"
@@ -93,12 +93,12 @@
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install dependencies"
         run: |
           set -xe
           python -VV
           python -m site
-          python -m pip install --require-hashes -r requirements/tox.pip
+          python -m pip install -r requirements/tox.pip
 
       - name: "Tox doc"
         run: |
           python -m tox -e doc
```

### Comparing `coverage-7.2.2/.github/workflows/testsuite.yml` & `coverage-7.2.3/.github/workflows/testsuite.yml`

 * *Files 2% similar despite different names*

```diff
@@ -69,15 +69,15 @@
           cache-dependency-path: 'requirements/*.pip'
 
       - name: "Install dependencies"
         run: |
           set -xe
           python -VV
           python -m site
-          python -m pip install --require-hashes -r requirements/tox.pip
+          python -m pip install -r requirements/tox.pip
           # For extreme debugging:
           # python -c "import urllib.request as r; exec(r.urlopen('https://bit.ly/pydoctor').read())"
 
       - name: "Run tox for ${{ matrix.python-version }}"
         run: |
           python -m tox -- -rfsEX
```

### Comparing `coverage-7.2.2/.readthedocs.yml` & `coverage-7.2.3/.readthedocs.yml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/CHANGES.rst` & `coverage-7.2.3/CHANGES.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,14 +15,37 @@
     ..  .. _changes_9-8-1:
     ..
     ..  Version 9.8.1 — 2027-07-27
     ..  --------------------------
 
 .. scriv-start-here
 
+.. _changes_7-2-3:
+
+Version 7.2.3 — 2023-04-06
+--------------------------
+
+- Fix: the :ref:`config_run_sigterm` setting was meant to capture data if a
+  process was terminated with a SIGTERM signal, but it didn't always.  This was
+  fixed thanks to `Lewis Gaul <pull 1600_>`_, closing `issue 1599`_.
+
+- Performance: HTML reports with context information are now much more compact.
+  File sizes are typically as small as one-third the previous size, but can be
+  dramatically smaller. This closes `issue 1584`_ thanks to `Oleh Krehel
+  <pull 1587_>`_.
+
+- Development dependencies no longer use hashed pins, closing `issue 1592`_.
+
+.. _issue 1584: https://github.com/nedbat/coveragepy/issues/1584
+.. _pull 1587: https://github.com/nedbat/coveragepy/pull/1587
+.. _issue 1592: https://github.com/nedbat/coveragepy/issues/1592
+.. _issue 1599: https://github.com/nedbat/coveragepy/issues/1599
+.. _pull 1600: https://github.com/nedbat/coveragepy/pull/1600
+
+
 .. _changes_7-2-2:
 
 Version 7.2.2 — 2023-03-16
 --------------------------
 
 - Fix: if a virtualenv was created inside a source directory, and a sourced
   package was installed inside the virtualenv, then all of the third-party
```

### Comparing `coverage-7.2.2/CONTRIBUTORS.txt` & `coverage-7.2.3/CONTRIBUTORS.txt`

 * *Files 4% similar despite different names*

```diff
@@ -95,53 +95,59 @@
 Jon Dufresne
 Joseph Tate
 Josh Williams
 Judson Neer
 Julian Berman
 Julien Voisin
 Justas Sadzevičius
+Kassandra Keeton
 Kjell Braden
 Krystian Kichewko
 Kyle Altendorf
 Lars Hupfeldt Nielsen
 Leonardo Pistone
+Lewis Gaul
 Lex Berezhny
 Loïc Dachary
 Lorenzo Micò
 Manuel Jacob
 Marc Abramowitz
 Marc Legendre
 Marcelo Trylesinski
 Marcus Cobden
 Marius Gedminas
 Mark van der Wal
 Martin Fuzzey
+Mathieu Kniewallner
 Matt Bachmann
 Matthew Boehm
 Matthew Desmarais
 Matus Valo
 Max Linke
 Michael Krebs
 Michał Bultrowicz
 Michał Górny
 Mickie Betz
 Mike Fiedler
-Naveen Yadav
 Nathan Land
+Naveen Yadav
+Neil Pilgrim
 Nikita Bloshchanevich
 Nils Kattenbeck
 Noel O'Boyle
+Oleh Krehel
 Olivier Grisel
 Ori Avtalion
-Pankaj Pandey
 Pablo Carballo
+Pankaj Pandey
 Patrick Mezard
 Peter Baughman
 Peter Ebden
 Peter Portante
+Phebe Polk
 Reya B
 Rodrigue Cloutier
 Roger Hu
 Ross Lawley
 Roy Williams
 Russell Keith-Magee
 Salvatore Zagaria
@@ -164,14 +170,14 @@
 S. Y. Lee
 Teake Nutma
 Ted Wexler
 Thijs Triemstra
 Thomas Grainger
 Titus Brown
 Valentin Lab
-Vince Salvino
 Ville Skyttä
+Vince Salvino
 Xie Yanbo
 Yilei "Dolee" Yang
 Yury Selivanov
 Zac Hatfield-Dodds
 Zooko Wilcox-O'Hearn
```

### Comparing `coverage-7.2.2/LICENSE.txt` & `coverage-7.2.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/MANIFEST.in` & `coverage-7.2.3/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/Makefile` & `coverage-7.2.3/Makefile`

 * *Files 7% similar despite different names*

```diff
@@ -7,39 +7,41 @@
 
 ##@ Utilities
 
 .PHONY: help clean_platform clean sterile
 
 clean_platform:
 	@rm -f *.so */*.so
+	@rm -f *.pyd */*.pyd
 	@rm -rf __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__ */*/*/*/*/__pycache__
 	@rm -f *.pyc */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc */*/*/*/*/*.pyc
 	@rm -f *.pyo */*.pyo */*/*.pyo */*/*/*.pyo */*/*/*/*.pyo */*/*/*/*/*.pyo
+	@rm -f *$$py.class */*$$py.class */*/*$$py.class */*/*/*$$py.class */*/*/*/*$$py.class */*/*/*/*/*$$py.class
 
 clean: clean_platform			## Remove artifacts of test execution, installation, etc.
 	@echo "Cleaning..."
 	@-pip uninstall -yq coverage
-	@rm -f *.pyd */*.pyd
+	@chmod -R 777 build
 	@rm -rf build coverage.egg-info dist htmlcov
 	@rm -f *.bak */*.bak */*/*.bak */*/*/*.bak */*/*/*/*.bak */*/*/*/*/*.bak
-	@rm -f *$$py.class */*$$py.class */*/*$$py.class */*/*/*$$py.class */*/*/*/*$$py.class */*/*/*/*/*$$py.class
 	@rm -f coverage/*,cover
 	@rm -f MANIFEST
 	@rm -f .coverage .coverage.* coverage.xml coverage.json .metacov*
 	@rm -f .tox/*/lib/*/site-packages/zzz_metacov.pth
 	@rm -f */.coverage */*/.coverage */*/*/.coverage */*/*/*/.coverage */*/*/*/*/.coverage */*/*/*/*/*/.coverage
 	@rm -f tests/covmain.zip tests/zipmods.zip tests/zip1.zip
 	@rm -rf doc/_build doc/_spell doc/sample_html_beta
 	@rm -rf tmp
 	@rm -rf .cache .hypothesis .mypy_cache .pytest_cache
 	@rm -rf tests/actual
 	@-make -C tests/gold/html clean
 
 sterile: clean				## Remove all non-controlled content, even if expensive.
 	rm -rf .tox
+	rm -f cheats.txt
 
 help:					## Show this help.
 	@# Adapted from https://www.thapaliya.com/en/writings/well-documented-makefiles/
 	@echo Available targets:
 	@awk -F ':.*##' '/^[^: ]+:.*##/{printf "  \033[1m%-20s\033[m %s\n",$$1,$$2} /^##@/{printf "\n%s\n",substr($$0,5)}' $(MAKEFILE_LIST)
 
 ##@ Tests and quality checks
@@ -79,15 +81,15 @@
 #
 # 2) Check manual pins before `make upgrade` to see if they can be removed. Look
 # in requirements/pins.pip, and search for "windows" in .in files to find pins
 # and extra requirements that have been needed, but might be obsolete.
 
 .PHONY: upgrade
 
-PIP_COMPILE = pip-compile --upgrade --allow-unsafe --generate-hashes --resolver=backtracking
+PIP_COMPILE = pip-compile --upgrade --allow-unsafe --resolver=backtracking
 upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
 upgrade: 				## Update the *.pip files with the latest packages satisfying *.in files.
 	pip install -q -r requirements/pip-tools.pip
 	$(PIP_COMPILE) -o requirements/pip-tools.pip requirements/pip-tools.in
 	$(PIP_COMPILE) -o requirements/pip.pip requirements/pip.in
 	$(PIP_COMPILE) -o requirements/pytest.pip requirements/pytest.in
 	$(PIP_COMPILE) -o requirements/kit.pip requirements/kit.in
@@ -154,14 +156,26 @@
 .PHONY: update_stable comment_on_fixes
 
 REPO_OWNER = nedbat/coveragepy
 
 edit_for_release:			## Edit sources to insert release facts.
 	python igor.py edit_for_release
 
+cheats:					## Create some useful snippets for releasing.
+	python igor.py cheats | tee cheats.txt
+
+relbranch:				## Create the branch for releasing.
+	git switch -c nedbat/release-$$(date +%Y%m%d)
+
+relcommit1:				## Commit the first release changes.
+	git commit -am "docs: prep for $$(python setup.py --version)"
+
+relcommit2:				## Commit the latest sample HTML report.
+	git commit -am "docs: sample HTML for $$(python setup.py --version)"
+
 kit:					## Make the source distribution.
 	python -m build
 
 kit_upload:				## Upload the built distributions to PyPI.
 	twine upload --verbose dist/*
 
 test_upload:				## Upload the distributions to PyPI's testing server.
```

### Comparing `coverage-7.2.2/NOTICE.txt` & `coverage-7.2.3/NOTICE.txt`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/PKG-INFO` & `coverage-7.2.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: coverage
-Version: 7.2.2
+Version: 7.2.3
 Summary: Code coverage measurement for Python
 Home-page: https://github.com/nedbat/coveragepy
-Author: Ned Batchelder and 172 others
+Author: Ned Batchelder and 178 others
 Author-email: ned@nedbatchelder.com
 License: Apache-2.0
-Project-URL: Documentation, https://coverage.readthedocs.io/en/7.2.2
+Project-URL: Documentation, https://coverage.readthedocs.io/en/7.2.3
 Project-URL: Funding, https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=pypi
 Project-URL: Issues, https://github.com/nedbat/coveragepy/issues
 Project-URL: Mastodon, https://hachyderm.io/@coveragepy
 Project-URL: Mastodon (nedbat), https://hachyderm.io/@nedbat
 Keywords: code coverage testing
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
@@ -60,21 +60,21 @@
 the code analysis tools and tracing hooks provided in the Python standard
 library to determine which lines are executable, and which have been executed.
 
 Coverage.py runs on these versions of Python:
 
 .. PYVERSIONS
 
-* CPython 3.7 through 3.12.0a6
+* CPython 3.7 through 3.12.0a7
 * PyPy3 7.3.11.
 
 Documentation is on `Read the Docs`_.  Code repository and issue tracker are on
 `GitHub`_.
 
-.. _Read the Docs: https://coverage.readthedocs.io/en/7.2.2/
+.. _Read the Docs: https://coverage.readthedocs.io/en/7.2.3/
 .. _GitHub: https://github.com/nedbat/coveragepy
 
 **New in 7.x:**
 improved data combining;
 ``report --format=``;
 type annotations.
 
@@ -102,25 +102,26 @@
        of commercial-grade software, this is for you.
        `Learn more. <https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=readme>`_
 
 
 Getting Started
 ---------------
 
-See the `Quick Start section`_ of the docs.
+Looking to run ``coverage`` on your test suite? See the `Quick Start section`_
+of the docs.
 
-.. _Quick Start section: https://coverage.readthedocs.io/en/7.2.2/#quick-start
+.. _Quick Start section: https://coverage.readthedocs.io/en/7.2.3/#quick-start
 
 
 Change history
 --------------
 
 The complete history of changes is on the `change history page`_.
 
-.. _change history page: https://coverage.readthedocs.io/en/7.2.2/changes.html
+.. _change history page: https://coverage.readthedocs.io/en/7.2.3/changes.html
 
 
 Code of Conduct
 ---------------
 
 Everyone participating in the coverage.py project is expected to treat other
 people with respect and to follow the guidelines articulated in the `Python
@@ -128,17 +129,18 @@
 
 .. _Python Community Code of Conduct: https://www.python.org/psf/codeofconduct/
 
 
 Contributing
 ------------
 
-See the `Contributing section`_ of the docs.
+Found a bug? Want to help improve the code or documentation? See the
+`Contributing section`_ of the docs.
 
-.. _Contributing section: https://coverage.readthedocs.io/en/7.2.2/contributing.html
+.. _Contributing section: https://coverage.readthedocs.io/en/7.2.3/contributing.html
 
 
 Security
 --------
 
 To report a security vulnerability, please use the `Tidelift security
 contact`_.  Tidelift will coordinate the fix and disclosure.
@@ -158,15 +160,15 @@
 .. |test-status| image:: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml/badge.svg?branch=master&event=push
     :target: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml
     :alt: Test suite status
 .. |quality-status| image:: https://github.com/nedbat/coveragepy/actions/workflows/quality.yml/badge.svg?branch=master&event=push
     :target: https://github.com/nedbat/coveragepy/actions/workflows/quality.yml
     :alt: Quality check status
 .. |docs| image:: https://readthedocs.org/projects/coverage/badge/?version=latest&style=flat
-    :target: https://coverage.readthedocs.io/en/7.2.2/
+    :target: https://coverage.readthedocs.io/en/7.2.3/
     :alt: Documentation
 .. |kit| image:: https://badge.fury.io/py/coverage.svg
     :target: https://pypi.org/project/coverage/
     :alt: PyPI status
 .. |format| image:: https://img.shields.io/pypi/format/coverage.svg
     :target: https://pypi.org/project/coverage/
     :alt: Kit format
```

### Comparing `coverage-7.2.2/README.rst` & `coverage-7.2.3/README.rst`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 the code analysis tools and tracing hooks provided in the Python standard
 library to determine which lines are executable, and which have been executed.
 
 Coverage.py runs on these versions of Python:
 
 .. PYVERSIONS
 
-* CPython 3.7 through 3.12.0a6
+* CPython 3.7 through 3.12.0a7
 * PyPy3 7.3.11.
 
 Documentation is on `Read the Docs`_.  Code repository and issue tracker are on
 `GitHub`_.
 
 .. _Read the Docs: https://coverage.readthedocs.io/
 .. _GitHub: https://github.com/nedbat/coveragepy
@@ -66,15 +66,16 @@
        of commercial-grade software, this is for you.
        `Learn more. <https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=readme>`_
 
 
 Getting Started
 ---------------
 
-See the `Quick Start section`_ of the docs.
+Looking to run ``coverage`` on your test suite? See the `Quick Start section`_
+of the docs.
 
 .. _Quick Start section: https://coverage.readthedocs.io/#quick-start
 
 
 Change history
 --------------
 
@@ -92,15 +93,16 @@
 
 .. _Python Community Code of Conduct: https://www.python.org/psf/codeofconduct/
 
 
 Contributing
 ------------
 
-See the `Contributing section`_ of the docs.
+Found a bug? Want to help improve the code or documentation? See the
+`Contributing section`_ of the docs.
 
 .. _Contributing section: https://coverage.readthedocs.io/en/latest/contributing.html
 
 
 Security
 --------
```

### Comparing `coverage-7.2.2/ci/comment_on_fixes.py` & `coverage-7.2.3/ci/comment_on_fixes.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/ci/download_gha_artifacts.py` & `coverage-7.2.3/ci/download_gha_artifacts.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/ci/parse_relnotes.py` & `coverage-7.2.3/ci/parse_relnotes.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/ci/trigger_build_kits.py` & `coverage-7.2.3/ci/trigger_build_kits.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/__init__.py` & `coverage-7.2.3/coverage/__init__.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/annotate.py` & `coverage-7.2.3/coverage/annotate.py`

 * *Files 6% similar despite different names*

```diff
@@ -36,16 +36,16 @@
         >     if x == 1:
         !         a = 1
         >     else:
         >         a = 2
 
         > h(2)
 
-    Executed lines use '>', lines not executed use '!', lines excluded from
-    consideration use '-'.
+    Executed lines use ">", lines not executed use "!", lines excluded from
+    consideration use "-".
 
     """
 
     def __init__(self, coverage: Coverage) -> None:
         self.coverage = coverage
         self.config = self.coverage.config
         self.directory: Optional[str] = None
@@ -79,36 +79,36 @@
             dest_file = os.path.join(self.directory, flat_rootname(fr.relative_filename()))
             if dest_file.endswith("_py"):
                 dest_file = dest_file[:-3] + ".py"
             dest_file += ",cover"
         else:
             dest_file = fr.filename + ",cover"
 
-        with open(dest_file, 'w', encoding='utf-8') as dest:
+        with open(dest_file, "w", encoding="utf-8") as dest:
             i = j = 0
             covered = True
             source = fr.source()
             for lineno, line in enumerate(source.splitlines(True), start=1):
                 while i < len(statements) and statements[i] < lineno:
                     i += 1
                 while j < len(missing) and missing[j] < lineno:
                     j += 1
                 if i < len(statements) and statements[i] == lineno:
                     covered = j >= len(missing) or missing[j] > lineno
                 if self.blank_re.match(line):
-                    dest.write('  ')
+                    dest.write("  ")
                 elif self.else_re.match(line):
-                    # Special logic for lines containing only 'else:'.
+                    # Special logic for lines containing only "else:".
                     if j >= len(missing):
-                        dest.write('> ')
+                        dest.write("> ")
                     elif statements[i] == missing[j]:
-                        dest.write('! ')
+                        dest.write("! ")
                     else:
-                        dest.write('> ')
+                        dest.write("> ")
                 elif lineno in excluded:
-                    dest.write('- ')
+                    dest.write("- ")
                 elif covered:
-                    dest.write('> ')
+                    dest.write("> ")
                 else:
-                    dest.write('! ')
+                    dest.write("! ")
 
                 dest.write(line)
```

### Comparing `coverage-7.2.2/coverage/bytecode.py` & `coverage-7.2.3/coverage/bytecode.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/cmdline.py` & `coverage-7.2.3/coverage/cmdline.py`

 * *Files 18% similar despite different names*

```diff
@@ -35,203 +35,203 @@
 class Opts:
     """A namespace class for individual options we'll build parsers from."""
 
     # Keep these entries alphabetized (roughly) by the option name as it
     # appears on the command line.
 
     append = optparse.make_option(
-        '-a', '--append', action='store_true',
+        "-a", "--append", action="store_true",
         help="Append coverage data to .coverage, otherwise it starts clean each time.",
     )
     keep = optparse.make_option(
-        '', '--keep', action='store_true',
+        "", "--keep", action="store_true",
         help="Keep original coverage files, otherwise they are deleted.",
     )
     branch = optparse.make_option(
-        '', '--branch', action='store_true',
+        "", "--branch", action="store_true",
         help="Measure branch coverage in addition to statement coverage.",
     )
     concurrency = optparse.make_option(
-        '', '--concurrency', action='store', metavar="LIBS",
+        "", "--concurrency", action="store", metavar="LIBS",
         help=(
             "Properly measure code using a concurrency library. " +
             "Valid values are: {}, or a comma-list of them."
         ).format(", ".join(sorted(CoverageConfig.CONCURRENCY_CHOICES))),
     )
     context = optparse.make_option(
-        '', '--context', action='store', metavar="LABEL",
+        "", "--context", action="store", metavar="LABEL",
         help="The context label to record for this coverage run.",
     )
     contexts = optparse.make_option(
-        '', '--contexts', action='store', metavar="REGEX1,REGEX2,...",
+        "", "--contexts", action="store", metavar="REGEX1,REGEX2,...",
         help=(
             "Only display data from lines covered in the given contexts. " +
             "Accepts Python regexes, which must be quoted."
         ),
     )
     combine_datafile = optparse.make_option(
-        '', '--data-file', action='store', metavar="DATAFILE",
+        "", "--data-file", action="store", metavar="DATAFILE",
         help=(
             "Base name of the data files to operate on. " +
             "Defaults to '.coverage'. [env: COVERAGE_FILE]"
         ),
     )
     input_datafile = optparse.make_option(
-        '', '--data-file', action='store', metavar="INFILE",
+        "", "--data-file", action="store", metavar="INFILE",
         help=(
             "Read coverage data for report generation from this file. " +
             "Defaults to '.coverage'. [env: COVERAGE_FILE]"
         ),
     )
     output_datafile = optparse.make_option(
-        '', '--data-file', action='store', metavar="OUTFILE",
+        "", "--data-file", action="store", metavar="OUTFILE",
         help=(
             "Write the recorded coverage data to this file. " +
             "Defaults to '.coverage'. [env: COVERAGE_FILE]"
         ),
     )
     debug = optparse.make_option(
-        '', '--debug', action='store', metavar="OPTS",
+        "", "--debug", action="store", metavar="OPTS",
         help="Debug options, separated by commas. [env: COVERAGE_DEBUG]",
     )
     directory = optparse.make_option(
-        '-d', '--directory', action='store', metavar="DIR",
+        "-d", "--directory", action="store", metavar="DIR",
         help="Write the output files to DIR.",
     )
     fail_under = optparse.make_option(
-        '', '--fail-under', action='store', metavar="MIN", type="float",
+        "", "--fail-under", action="store", metavar="MIN", type="float",
         help="Exit with a status of 2 if the total coverage is less than MIN.",
     )
     format = optparse.make_option(
-        '', '--format', action='store', metavar="FORMAT",
+        "", "--format", action="store", metavar="FORMAT",
         help="Output format, either text (default), markdown, or total.",
     )
     help = optparse.make_option(
-        '-h', '--help', action='store_true',
+        "-h", "--help", action="store_true",
         help="Get help on this command.",
     )
     ignore_errors = optparse.make_option(
-        '-i', '--ignore-errors', action='store_true',
+        "-i", "--ignore-errors", action="store_true",
         help="Ignore errors while reading source files.",
     )
     include = optparse.make_option(
-        '', '--include', action='store', metavar="PAT1,PAT2,...",
+        "", "--include", action="store", metavar="PAT1,PAT2,...",
         help=(
             "Include only files whose paths match one of these patterns. " +
             "Accepts shell-style wildcards, which must be quoted."
         ),
     )
     pylib = optparse.make_option(
-        '-L', '--pylib', action='store_true',
+        "-L", "--pylib", action="store_true",
         help=(
             "Measure coverage even inside the Python installed library, " +
             "which isn't done by default."
         ),
     )
     show_missing = optparse.make_option(
-        '-m', '--show-missing', action='store_true',
+        "-m", "--show-missing", action="store_true",
         help="Show line numbers of statements in each module that weren't executed.",
     )
     module = optparse.make_option(
-        '-m', '--module', action='store_true',
+        "-m", "--module", action="store_true",
         help=(
             "<pyfile> is an importable Python module, not a script path, " +
             "to be run as 'python -m' would run it."
         ),
     )
     omit = optparse.make_option(
-        '', '--omit', action='store', metavar="PAT1,PAT2,...",
+        "", "--omit", action="store", metavar="PAT1,PAT2,...",
         help=(
             "Omit files whose paths match one of these patterns. " +
             "Accepts shell-style wildcards, which must be quoted."
         ),
     )
     output_xml = optparse.make_option(
-        '-o', '', action='store', dest="outfile", metavar="OUTFILE",
+        "-o", "", action="store", dest="outfile", metavar="OUTFILE",
         help="Write the XML report to this file. Defaults to 'coverage.xml'",
     )
     output_json = optparse.make_option(
-        '-o', '', action='store', dest="outfile", metavar="OUTFILE",
+        "-o", "", action="store", dest="outfile", metavar="OUTFILE",
         help="Write the JSON report to this file. Defaults to 'coverage.json'",
     )
     output_lcov = optparse.make_option(
-        '-o', '', action='store', dest='outfile', metavar="OUTFILE",
+        "-o", "", action="store", dest="outfile", metavar="OUTFILE",
         help="Write the LCOV report to this file. Defaults to 'coverage.lcov'",
     )
     json_pretty_print = optparse.make_option(
-        '', '--pretty-print', action='store_true',
+        "", "--pretty-print", action="store_true",
         help="Format the JSON for human readers.",
     )
     parallel_mode = optparse.make_option(
-        '-p', '--parallel-mode', action='store_true',
+        "-p", "--parallel-mode", action="store_true",
         help=(
             "Append the machine name, process id and random number to the " +
             "data file name to simplify collecting data from " +
             "many processes."
         ),
     )
     precision = optparse.make_option(
-        '', '--precision', action='store', metavar='N', type=int,
+        "", "--precision", action="store", metavar="N", type=int,
         help=(
             "Number of digits after the decimal point to display for " +
             "reported coverage percentages."
         ),
     )
     quiet = optparse.make_option(
-        '-q', '--quiet', action='store_true',
+        "-q", "--quiet", action="store_true",
         help="Don't print messages about what is happening.",
     )
     rcfile = optparse.make_option(
-        '', '--rcfile', action='store',
+        "", "--rcfile", action="store",
         help=(
             "Specify configuration file. " +
             "By default '.coveragerc', 'setup.cfg', 'tox.ini', and " +
             "'pyproject.toml' are tried. [env: COVERAGE_RCFILE]"
         ),
     )
     show_contexts = optparse.make_option(
-        '--show-contexts', action='store_true',
+        "--show-contexts", action="store_true",
         help="Show contexts for covered lines.",
     )
     skip_covered = optparse.make_option(
-        '--skip-covered', action='store_true',
+        "--skip-covered", action="store_true",
         help="Skip files with 100% coverage.",
     )
     no_skip_covered = optparse.make_option(
-        '--no-skip-covered', action='store_false', dest='skip_covered',
+        "--no-skip-covered", action="store_false", dest="skip_covered",
         help="Disable --skip-covered.",
     )
     skip_empty = optparse.make_option(
-        '--skip-empty', action='store_true',
+        "--skip-empty", action="store_true",
         help="Skip files with no code.",
     )
     sort = optparse.make_option(
-        '--sort', action='store', metavar='COLUMN',
+        "--sort", action="store", metavar="COLUMN",
         help=(
             "Sort the report by the named column: name, stmts, miss, branch, brpart, or cover. " +
              "Default is name."
         ),
     )
     source = optparse.make_option(
-        '', '--source', action='store', metavar="SRC1,SRC2,...",
+        "", "--source", action="store", metavar="SRC1,SRC2,...",
         help="A list of directories or importable names of code to measure.",
     )
     timid = optparse.make_option(
-        '', '--timid', action='store_true',
+        "", "--timid", action="store_true",
         help=(
             "Use a simpler but slower trace method. Try this if you get " +
             "seemingly impossible results!"
         ),
     )
     title = optparse.make_option(
-        '', '--title', action='store', metavar="TITLE",
+        "", "--title", action="store", metavar="TITLE",
         help="A text string to use as the title on the HTML.",
     )
     version = optparse.make_option(
-        '', '--version', action='store_true',
+        "", "--version", action="store_true",
         help="Display version information and exit.",
     )
 
 
 class CoverageOptionParser(optparse.OptionParser):
     """Base OptionParser for coverage.py.
 
@@ -365,15 +365,15 @@
 GLOBAL_ARGS = [
     Opts.debug,
     Opts.help,
     Opts.rcfile,
 ]
 
 COMMANDS = {
-    'annotate': CmdOptionParser(
+    "annotate": CmdOptionParser(
         "annotate",
         [
             Opts.directory,
             Opts.input_datafile,
             Opts.ignore_errors,
             Opts.include,
             Opts.omit,
@@ -381,15 +381,15 @@
         usage="[options] [modules]",
         description=(
             "Make annotated copies of the given files, marking statements that are executed " +
             "with > and statements that are missed with !."
         ),
     ),
 
-    'combine': CmdOptionParser(
+    "combine": CmdOptionParser(
         "combine",
         [
             Opts.append,
             Opts.combine_datafile,
             Opts.keep,
             Opts.quiet,
             ] + GLOBAL_ARGS,
@@ -400,44 +400,44 @@
             "file representing the union of the data. The positional " +
             "arguments are data files or directories containing data files. " +
             "If no paths are provided, data files in the default data file's " +
             "directory are combined."
         ),
     ),
 
-    'debug': CmdOptionParser(
+    "debug": CmdOptionParser(
         "debug", GLOBAL_ARGS,
         usage="<topic>",
         description=(
             "Display information about the internals of coverage.py, " +
             "for diagnosing problems. " +
             "Topics are: " +
                 "'data' to show a summary of the collected data; " +
                 "'sys' to show installation information; " +
                 "'config' to show the configuration; " +
                 "'premain' to show what is calling coverage; " +
                 "'pybehave' to show internal flags describing Python behavior."
         ),
     ),
 
-    'erase': CmdOptionParser(
+    "erase": CmdOptionParser(
         "erase",
         [
             Opts.combine_datafile
             ] + GLOBAL_ARGS,
         description="Erase previously collected coverage data.",
     ),
 
-    'help': CmdOptionParser(
+    "help": CmdOptionParser(
         "help", GLOBAL_ARGS,
         usage="[command]",
         description="Describe how to use coverage.py",
     ),
 
-    'html': CmdOptionParser(
+    "html": CmdOptionParser(
         "html",
         [
             Opts.contexts,
             Opts.directory,
             Opts.input_datafile,
             Opts.fail_under,
             Opts.ignore_errors,
@@ -455,15 +455,15 @@
         description=(
             "Create an HTML report of the coverage of the files.  " +
             "Each file gets its own page, with the source decorated to show " +
             "executed, excluded, and missed lines."
         ),
     ),
 
-    'json': CmdOptionParser(
+    "json": CmdOptionParser(
         "json",
         [
             Opts.contexts,
             Opts.input_datafile,
             Opts.fail_under,
             Opts.ignore_errors,
             Opts.include,
@@ -473,30 +473,30 @@
             Opts.quiet,
             Opts.show_contexts,
             ] + GLOBAL_ARGS,
         usage="[options] [modules]",
         description="Generate a JSON report of coverage results.",
     ),
 
-    'lcov': CmdOptionParser(
+    "lcov": CmdOptionParser(
         "lcov",
         [
             Opts.input_datafile,
             Opts.fail_under,
             Opts.ignore_errors,
             Opts.include,
             Opts.output_lcov,
             Opts.omit,
             Opts.quiet,
             ] + GLOBAL_ARGS,
         usage="[options] [modules]",
         description="Generate an LCOV report of coverage results.",
     ),
 
-    'report': CmdOptionParser(
+    "report": CmdOptionParser(
         "report",
         [
             Opts.contexts,
             Opts.input_datafile,
             Opts.fail_under,
             Opts.format,
             Opts.ignore_errors,
@@ -509,15 +509,15 @@
             Opts.no_skip_covered,
             Opts.skip_empty,
             ] + GLOBAL_ARGS,
         usage="[options] [modules]",
         description="Report coverage statistics on modules.",
     ),
 
-    'run': CmdOptionParser(
+    "run": CmdOptionParser(
         "run",
         [
             Opts.append,
             Opts.branch,
             Opts.concurrency,
             Opts.context,
             Opts.output_datafile,
@@ -529,15 +529,15 @@
             Opts.source,
             Opts.timid,
             ] + GLOBAL_ARGS,
         usage="[options] <pyfile> [program options]",
         description="Run a Python program, measuring code execution.",
     ),
 
-    'xml': CmdOptionParser(
+    "xml": CmdOptionParser(
         "xml",
         [
             Opts.input_datafile,
             Opts.fail_under,
             Opts.ignore_errors,
             Opts.include,
             Opts.omit,
@@ -556,45 +556,45 @@
     topic: Optional[str] = None,
     parser: Optional[optparse.OptionParser] = None,
 ) -> None:
     """Display an error message, or the named topic."""
     assert error or topic or parser
 
     program_path = sys.argv[0]
-    if program_path.endswith(os.path.sep + '__main__.py'):
+    if program_path.endswith(os.path.sep + "__main__.py"):
         # The path is the main module of a package; get that path instead.
         program_path = os.path.dirname(program_path)
     program_name = os.path.basename(program_path)
     if env.WINDOWS:
-        # entry_points={'console_scripts':...} on Windows makes files
+        # entry_points={"console_scripts":...} on Windows makes files
         # called coverage.exe, coverage3.exe, and coverage-3.5.exe. These
         # invoke coverage-script.py, coverage3-script.py, and
         # coverage-3.5-script.py.  argv[0] is the .py file, but we want to
         # get back to the original form.
         auto_suffix = "-script.py"
         if program_name.endswith(auto_suffix):
             program_name = program_name[:-len(auto_suffix)]
 
     help_params = dict(coverage.__dict__)
     help_params["__url__"] = __url__
-    help_params['program_name'] = program_name
+    help_params["program_name"] = program_name
     if HAS_CTRACER:
-        help_params['extension_modifier'] = 'with C extension'
+        help_params["extension_modifier"] = "with C extension"
     else:
-        help_params['extension_modifier'] = 'without C extension'
+        help_params["extension_modifier"] = "without C extension"
 
     if error:
         print(error, file=sys.stderr)
         print(f"Use '{program_name} help' for help.", file=sys.stderr)
     elif parser:
         print(parser.format_help().strip())
         print()
     else:
         assert topic is not None
-        help_msg = textwrap.dedent(HELP_TOPICS.get(topic, '')).strip()
+        help_msg = textwrap.dedent(HELP_TOPICS.get(topic, "")).strip()
         if help_msg:
             print(help_msg.format(**help_params))
         else:
             print(f"Don't know topic {topic!r}")
     print("Full documentation is at {__url__}".format(**help_params))
 
 
@@ -614,21 +614,21 @@
         `argv` is the argument list to process.
 
         Returns 0 if all is well, 1 if something went wrong.
 
         """
         # Collect the command-line options.
         if not argv:
-            show_help(topic='minimum_help')
+            show_help(topic="minimum_help")
             return OK
 
         # The command syntax we parse depends on the first argument.  Global
         # switch syntax always starts with an option.
         parser: Optional[optparse.OptionParser]
-        self.global_option = argv[0].startswith('-')
+        self.global_option = argv[0].startswith("-")
         if self.global_option:
             parser = GlobalOptionParser()
         else:
             parser = COMMANDS.get(argv[0])
             if not parser:
                 show_help(f"Unknown command: {argv[0]!r}")
                 return ERR
@@ -698,15 +698,15 @@
             omit=omit,
             include=include,
             contexts=contexts,
         )
 
         # We need to be able to import from the current directory, because
         # plugins may try to, for example, to read Django settings.
-        sys.path.insert(0, '')
+        sys.path.insert(0, "")
 
         self.coverage.load()
 
         total = None
         if options.action == "report":
             total = self.coverage.report(
                 precision=options.precision,
@@ -782,34 +782,34 @@
 
         Return True if it handled the request, False if not.
 
         """
         # Handle help.
         if options.help:
             if self.global_option:
-                show_help(topic='help')
+                show_help(topic="help")
             else:
                 show_help(parser=parser)
             return True
 
         if options.action == "help":
             if args:
                 for a in args:
                     parser_maybe = COMMANDS.get(a)
                     if parser_maybe is not None:
                         show_help(parser=parser_maybe)
                     else:
                         show_help(topic=a)
             else:
-                show_help(topic='help')
+                show_help(topic="help")
             return True
 
         # Handle version.
         if options.version:
-            show_help(topic='version')
+            show_help(topic="version")
             return True
 
         return False
 
     def do_run(self, options: optparse.Values, args: List[str]) -> int:
         """Implementation of 'coverage run'."""
 
@@ -831,15 +831,15 @@
         if options.append and self.coverage.get_option("run:parallel"):
             show_help("Can't append to data files in parallel mode.")
             return ERR
 
         if options.concurrency == "multiprocessing":
             # Can't set other run-affecting command line options with
             # multiprocessing.
-            for opt_name in ['branch', 'include', 'omit', 'pylib', 'source', 'timid']:
+            for opt_name in ["branch", "include", "omit", "pylib", "source", "timid"]:
                 # As it happens, all of these options have no default, meaning
                 # they will be None if they have not been specified.
                 if getattr(options, opt_name) is not None:
                     show_help(
                         "Options affecting multiprocessing must only be specified " +
                         "in a configuration file.\n" +
                         f"Remove --{opt_name} from the command line."
@@ -909,32 +909,32 @@
     if env.WINDOWS:
         # When running coverage.py as coverage.exe, some of the behavior
         # of the shell is emulated: wildcards are expanded into a list of
         # file names.  So you have to single-quote patterns on the command
         # line, but (not) helpfully, the single quotes are included in the
         # argument, so we have to strip them off here.
         s = s.strip("'")
-    return s.split(',')
+    return s.split(",")
 
 
 def unglob_args(args: List[str]) -> List[str]:
     """Interpret shell wildcards for platforms that need it."""
     if env.WINDOWS:
         globbed = []
         for arg in args:
-            if '?' in arg or '*' in arg:
+            if "?" in arg or "*" in arg:
                 globbed.extend(glob.glob(arg))
             else:
                 globbed.append(arg)
         args = globbed
     return args
 
 
 HELP_TOPICS = {
-    'help': """\
+    "help": """\
         Coverage.py, version {__version__} {extension_modifier}
         Measure, collect, and report on code coverage in Python programs.
 
         usage: {program_name} <command> [options] [args]
 
         Commands:
             annotate    Annotate source files with execution information.
@@ -948,19 +948,19 @@
             report      Report coverage stats on modules.
             run         Run a Python program and measure code execution.
             xml         Create an XML report of coverage results.
 
         Use "{program_name} help <command>" for detailed help on any command.
     """,
 
-    'minimum_help': """\
+    "minimum_help": """\
         Code coverage for Python, version {__version__} {extension_modifier}.  Use '{program_name} help' for help.
     """,
 
-    'version': """\
+    "version": """\
         Coverage.py, version {__version__} {extension_modifier}
     """,
 }
 
 
 def main(argv: Optional[List[str]] = None) -> Optional[int]:
     """The main entry point to coverage.py.
@@ -1004,10 +1004,10 @@
         argv: Optional[List[str]] = None,
     ) -> Optional[int]:
         """A wrapper around main that profiles."""
         profiler = SimpleLauncher.launch()
         try:
             return original_main(argv)
         finally:
-            data, _ = profiler.query(re_filter='coverage', max_records=100)
-            print(profiler.show(query=data, limit=100, sep='', col=''))
+            data, _ = profiler.query(re_filter="coverage", max_records=100)
+            print(profiler.show(query=data, limit=100, sep="", col=""))
             profiler.cancel()
```

### Comparing `coverage-7.2.2/coverage/collector.py` & `coverage-7.2.3/coverage/collector.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/config.py` & `coverage-7.2.3/coverage/config.py`

 * *Files 6% similar despite different names*

```diff
@@ -110,16 +110,16 @@
         separated list of strings.  Each value is stripped of white space.
 
         Returns the list of strings.
 
         """
         value_list = self.get(section, option)
         values = []
-        for value_line in value_list.split('\n'):
-            for value in value_line.split(','):
+        for value_line in value_list.split("\n"):
+            for value in value_line.split(","):
                 value = value.strip()
                 if value:
                     values.append(value)
         return values
 
     def getregexlist(self, section: str, option: str) -> List[str]:
         """Read a list of full-line regexes.
@@ -146,28 +146,28 @@
 
 
 TConfigParser = Union[HandyConfigParser, TomlConfigParser]
 
 
 # The default line exclusion regexes.
 DEFAULT_EXCLUDE = [
-    r'#\s*(pragma|PRAGMA)[:\s]?\s*(no|NO)\s*(cover|COVER)',
+    r"#\s*(pragma|PRAGMA)[:\s]?\s*(no|NO)\s*(cover|COVER)",
 ]
 
 # The default partial branch regexes, to be modified by the user.
 DEFAULT_PARTIAL = [
-    r'#\s*(pragma|PRAGMA)[:\s]?\s*(no|NO)\s*(branch|BRANCH)',
+    r"#\s*(pragma|PRAGMA)[:\s]?\s*(no|NO)\s*(branch|BRANCH)",
 ]
 
 # The default partial branch regexes, based on Python semantics.
 # These are any Python branching constructs that can't actually execute all
 # their branches.
 DEFAULT_PARTIAL_ALWAYS = [
-    'while (True|1|False|0):',
-    'if (True|1|False|0):',
+    "while (True|1|False|0):",
+    "if (True|1|False|0):",
 ]
 
 
 class CoverageConfig(TConfigurable, TPluginConfig):
     """Coverage.py configuration.
 
     The attributes of this class are the various settings that control the
@@ -282,15 +282,15 @@
 
         Returns True or False, whether the file could be read, and it had some
         coverage.py settings in it.
 
         """
         _, ext = os.path.splitext(filename)
         cp: TConfigParser
-        if ext == '.toml':
+        if ext == ".toml":
             cp = TomlConfigParser(our_file)
         else:
             cp = HandyConfigParser(our_file)
 
         self.attempted_config_files.append(filename)
 
         try:
@@ -324,17 +324,17 @@
                     warn(
                         "Unrecognized option '[{}] {}=' in config file {}".format(
                             real_section, unknown, filename
                         )
                     )
 
         # [paths] is special
-        if cp.has_section('paths'):
-            for option in cp.options('paths'):
-                self.paths[option] = cp.getlist('paths', option)
+        if cp.has_section("paths"):
+            for option in cp.options("paths"):
+                self.paths[option] = cp.getlist("paths", option)
                 any_set = True
 
         # plugins can have options
         for plugin in self.plugins:
             if cp.has_section(plugin):
                 self.plugin_options[plugin] = cp.get_section(plugin)
                 any_set = True
@@ -366,89 +366,89 @@
         #
         #   attr is the attribute to set on the CoverageConfig object.
         #   where is the section:name to read from the configuration file.
         #   type_ is the optional type to apply, by using .getTYPE to read the
         #       configuration value from the file.
 
         # [run]
-        ('branch', 'run:branch', 'boolean'),
-        ('command_line', 'run:command_line'),
-        ('concurrency', 'run:concurrency', 'list'),
-        ('context', 'run:context'),
-        ('cover_pylib', 'run:cover_pylib', 'boolean'),
-        ('data_file', 'run:data_file'),
-        ('debug', 'run:debug', 'list'),
-        ('debug_file', 'run:debug_file'),
-        ('disable_warnings', 'run:disable_warnings', 'list'),
-        ('dynamic_context', 'run:dynamic_context'),
-        ('parallel', 'run:parallel', 'boolean'),
-        ('plugins', 'run:plugins', 'list'),
-        ('relative_files', 'run:relative_files', 'boolean'),
-        ('run_include', 'run:include', 'list'),
-        ('run_omit', 'run:omit', 'list'),
-        ('sigterm', 'run:sigterm', 'boolean'),
-        ('source', 'run:source', 'list'),
-        ('source_pkgs', 'run:source_pkgs', 'list'),
-        ('timid', 'run:timid', 'boolean'),
-        ('_crash', 'run:_crash'),
+        ("branch", "run:branch", "boolean"),
+        ("command_line", "run:command_line"),
+        ("concurrency", "run:concurrency", "list"),
+        ("context", "run:context"),
+        ("cover_pylib", "run:cover_pylib", "boolean"),
+        ("data_file", "run:data_file"),
+        ("debug", "run:debug", "list"),
+        ("debug_file", "run:debug_file"),
+        ("disable_warnings", "run:disable_warnings", "list"),
+        ("dynamic_context", "run:dynamic_context"),
+        ("parallel", "run:parallel", "boolean"),
+        ("plugins", "run:plugins", "list"),
+        ("relative_files", "run:relative_files", "boolean"),
+        ("run_include", "run:include", "list"),
+        ("run_omit", "run:omit", "list"),
+        ("sigterm", "run:sigterm", "boolean"),
+        ("source", "run:source", "list"),
+        ("source_pkgs", "run:source_pkgs", "list"),
+        ("timid", "run:timid", "boolean"),
+        ("_crash", "run:_crash"),
 
         # [report]
-        ('exclude_list', 'report:exclude_lines', 'regexlist'),
-        ('exclude_also', 'report:exclude_also', 'regexlist'),
-        ('fail_under', 'report:fail_under', 'float'),
-        ('format', 'report:format', 'boolean'),
-        ('ignore_errors', 'report:ignore_errors', 'boolean'),
-        ('include_namespace_packages', 'report:include_namespace_packages', 'boolean'),
-        ('partial_always_list', 'report:partial_branches_always', 'regexlist'),
-        ('partial_list', 'report:partial_branches', 'regexlist'),
-        ('precision', 'report:precision', 'int'),
-        ('report_contexts', 'report:contexts', 'list'),
-        ('report_include', 'report:include', 'list'),
-        ('report_omit', 'report:omit', 'list'),
-        ('show_missing', 'report:show_missing', 'boolean'),
-        ('skip_covered', 'report:skip_covered', 'boolean'),
-        ('skip_empty', 'report:skip_empty', 'boolean'),
-        ('sort', 'report:sort'),
+        ("exclude_list", "report:exclude_lines", "regexlist"),
+        ("exclude_also", "report:exclude_also", "regexlist"),
+        ("fail_under", "report:fail_under", "float"),
+        ("format", "report:format", "boolean"),
+        ("ignore_errors", "report:ignore_errors", "boolean"),
+        ("include_namespace_packages", "report:include_namespace_packages", "boolean"),
+        ("partial_always_list", "report:partial_branches_always", "regexlist"),
+        ("partial_list", "report:partial_branches", "regexlist"),
+        ("precision", "report:precision", "int"),
+        ("report_contexts", "report:contexts", "list"),
+        ("report_include", "report:include", "list"),
+        ("report_omit", "report:omit", "list"),
+        ("show_missing", "report:show_missing", "boolean"),
+        ("skip_covered", "report:skip_covered", "boolean"),
+        ("skip_empty", "report:skip_empty", "boolean"),
+        ("sort", "report:sort"),
 
         # [html]
-        ('extra_css', 'html:extra_css'),
-        ('html_dir', 'html:directory'),
-        ('html_skip_covered', 'html:skip_covered', 'boolean'),
-        ('html_skip_empty', 'html:skip_empty', 'boolean'),
-        ('html_title', 'html:title'),
-        ('show_contexts', 'html:show_contexts', 'boolean'),
+        ("extra_css", "html:extra_css"),
+        ("html_dir", "html:directory"),
+        ("html_skip_covered", "html:skip_covered", "boolean"),
+        ("html_skip_empty", "html:skip_empty", "boolean"),
+        ("html_title", "html:title"),
+        ("show_contexts", "html:show_contexts", "boolean"),
 
         # [xml]
-        ('xml_output', 'xml:output'),
-        ('xml_package_depth', 'xml:package_depth', 'int'),
+        ("xml_output", "xml:output"),
+        ("xml_package_depth", "xml:package_depth", "int"),
 
         # [json]
-        ('json_output', 'json:output'),
-        ('json_pretty_print', 'json:pretty_print', 'boolean'),
-        ('json_show_contexts', 'json:show_contexts', 'boolean'),
+        ("json_output", "json:output"),
+        ("json_pretty_print", "json:pretty_print", "boolean"),
+        ("json_show_contexts", "json:show_contexts", "boolean"),
 
         # [lcov]
-        ('lcov_output', 'lcov:output'),
+        ("lcov_output", "lcov:output"),
     ]
 
     def _set_attr_from_config_option(
         self,
         cp: TConfigParser,
         attr: str,
         where: str,
-        type_: str = '',
+        type_: str = "",
     ) -> bool:
         """Set an attribute on self if it exists in the ConfigParser.
 
         Returns True if the attribute was set.
 
         """
         section, option = where.split(":")
         if cp.has_option(section, option):
-            method = getattr(cp, 'get' + type_)
+            method = getattr(cp, "get" + type_)
             setattr(self, attr, method(section, option))
             return True
         return False
 
     def get_plugin_options(self, plugin: str) -> TConfigSectionOut:
         """Get a dictionary of options for the plugin named `plugin`."""
         return self.plugin_options.get(plugin, {})
@@ -544,15 +544,15 @@
     # Some API users were specifying ".coveragerc" to mean the same as
     # True, so make it so.
     if config_file == ".coveragerc":
         config_file = True
     specified_file = (config_file is not True)
     if not specified_file:
         # No file was specified. Check COVERAGE_RCFILE.
-        rcfile = os.environ.get('COVERAGE_RCFILE')
+        rcfile = os.environ.get("COVERAGE_RCFILE")
         if rcfile:
             config_file = rcfile
             specified_file = True
     if not specified_file:
         # Still no file specified. Default to .coveragerc
         config_file = ".coveragerc"
     assert isinstance(config_file, str)
@@ -598,18 +598,18 @@
             if config_read:
                 break
             if specified_file:
                 raise ConfigError(f"Couldn't read {fname!r} as a config file")
 
     # $set_env.py: COVERAGE_DEBUG - Options for --debug.
     # 3) from environment variables:
-    env_data_file = os.environ.get('COVERAGE_FILE')
+    env_data_file = os.environ.get("COVERAGE_FILE")
     if env_data_file:
         config.data_file = env_data_file
-    debugs = os.environ.get('COVERAGE_DEBUG')
+    debugs = os.environ.get("COVERAGE_DEBUG")
     if debugs:
         config.debug.extend(d.strip() for d in debugs.split(","))
 
     # 4) from constructor arguments:
     config.from_args(**kwargs)
 
     # Once all the config has been collected, there's a little post-processing
```

### Comparing `coverage-7.2.2/coverage/context.py` & `coverage-7.2.3/coverage/context.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/control.py` & `coverage-7.2.3/coverage/control.py`

 * *Files 1% similar despite different names*

```diff
@@ -80,15 +80,15 @@
 
         from coverage import Coverage
 
         cov = Coverage()
         cov.start()
         #.. call your code ..
         cov.stop()
-        cov.html_report(directory='covhtml')
+        cov.html_report(directory="covhtml")
 
     Note: in keeping with Python custom, names starting with underscore are
     not part of the public API. They might stop working at any point.  Please
     limit yourself to documented methods to avoid problems.
 
     Methods can raise any of the exceptions described in :ref:`api_exceptions`.
 
@@ -339,15 +339,15 @@
 
     def _post_init(self) -> None:
         """Stuff to do after everything is initialized."""
         if self._should_write_debug:
             self._should_write_debug = False
             self._write_startup_debug()
 
-        # '[run] _crash' will raise an exception if the value is close by in
+        # "[run] _crash" will raise an exception if the value is close by in
         # the call stack, for testing error handling.
         if self.config._crash and self.config._crash in short_stack(limit=4):
             raise RuntimeError(f"Crashing because called by {self.config._crash}")
 
     def _write_startup_debug(self) -> None:
         """Write out debug info at startup if needed."""
         wrote_any = False
@@ -376,27 +376,27 @@
         """Decide whether to trace execution in `filename`.
 
         Calls `_should_trace_internal`, and returns the FileDisposition.
 
         """
         assert self._inorout is not None
         disp = self._inorout.should_trace(filename, frame)
-        if self._debug.should('trace'):
+        if self._debug.should("trace"):
             self._debug.write(disposition_debug_msg(disp))
         return disp
 
     def _check_include_omit_etc(self, filename: str, frame: FrameType) -> bool:
         """Check a file name against the include/omit/etc, rules, verbosely.
 
         Returns a boolean: True if the file should be traced, False if not.
 
         """
         assert self._inorout is not None
         reason = self._inorout.check_include_omit_etc(filename, frame)
-        if self._debug.should('trace'):
+        if self._debug.should("trace"):
             if not reason:
                 msg = f"Including {filename!r}"
             else:
                 msg = f"Not including {filename!r}: {reason}"
             self._debug.write(msg)
 
         return not reason
@@ -416,15 +416,15 @@
         if slug in self._no_warn_slugs:
             # Don't issue the warning
             return
 
         self._warnings.append(msg)
         if slug:
             msg = f"{msg} ({slug})"
-        if self._debug.should('pid'):
+        if self._debug.should("pid"):
             msg = f"[{os.getpid()}] {msg}"
         warnings.warn(msg, category=CoverageWarning, stacklevel=2)
 
         if once:
             assert slug is not None
             self._no_warn_slugs.append(slug)
 
@@ -562,15 +562,15 @@
             for plugin in self._plugins.file_tracers:
                 plugin._coverage_enabled = False
 
         # Create the file classifying substructure.
         self._inorout = InOrOut(
             config=self.config,
             warn=self._warn,
-            debug=(self._debug if self._debug.should('trace') else None),
+            debug=(self._debug if self._debug.should("trace") else None),
             include_namespace_packages=self.config.include_namespace_packages,
         )
         self._inorout.plugins = self._plugins
         self._inorout.disp_class = self._collector.file_disposition_class
 
         # It's useful to write debug info after initing for start.
         self._should_write_debug = True
@@ -649,15 +649,15 @@
 
     def _atexit(self, event: str = "atexit") -> None:
         """Clean up on process shutdown."""
         if self._debug.should("process"):
             self._debug.write(f"{event}: pid: {os.getpid()}, instance: {self!r}")
         if self._started:
             self.stop()
-        if self._auto_save:
+        if self._auto_save or event == "sigterm":
             self.save()
 
     def _on_sigterm(self, signum_unused: int, frame_unused: Optional[FrameType]) -> None:
         """A handler for signal.SIGTERM."""
         self._atexit("sigterm")
         # Statements after here won't be seen by metacov because we just wrote
         # the data, and are about to kill the process.
@@ -699,21 +699,21 @@
 
         assert self._collector is not None
         if self._collector.should_start_context:
             self._warn("Conflicting dynamic contexts", slug="dynamic-conflict", once=True)
 
         self._collector.switch_context(new_context)
 
-    def clear_exclude(self, which: str = 'exclude') -> None:
+    def clear_exclude(self, which: str = "exclude") -> None:
         """Clear the exclude list."""
         self._init()
         setattr(self.config, which + "_list", [])
         self._exclude_regex_stale()
 
-    def exclude(self, regex: str, which: str = 'exclude') -> None:
+    def exclude(self, regex: str, which: str = "exclude") -> None:
         """Exclude source lines from execution consideration.
 
         A number of lists of regular expressions are maintained.  Each list
         selects lines that are treated differently during reporting.
 
         `which` determines which list is modified.  The "exclude" list selects
         lines that are not considered executable at all.  The "partial" list
@@ -736,15 +736,15 @@
     def _exclude_regex(self, which: str) -> str:
         """Return a regex string for the given exclusion list."""
         if which not in self._exclude_re:
             excl_list = getattr(self.config, which + "_list")
             self._exclude_re[which] = join_regex(excl_list)
         return self._exclude_re[which]
 
-    def get_exclude_list(self, which: str = 'exclude') -> List[str]:
+    def get_exclude_list(self, which: str = "exclude") -> List[str]:
         """Return a list of excluded regex strings.
 
         `which` indicates which list is desired.  See :meth:`exclude` for the
         lists that are available, and their meaning.
 
         """
         self._init()
@@ -965,15 +965,15 @@
         if not isinstance(morfs, (list, tuple, set)):
             morfs = [morfs]     # type: ignore[list-item]
 
         file_reporters = [self._get_file_reporter(morf) for morf in morfs]
         return file_reporters
 
     def _prepare_data_for_reporting(self) -> None:
-        """Re-map data before reporting, to get implicit 'combine' behavior."""
+        """Re-map data before reporting, to get implicit "combine" behavior."""
         if self.config.paths:
             mapped_data = CoverageData(warn=self._warn, debug=self._debug, no_disk=True)
             if self._data is not None:
                 mapped_data.update(self._data, aliases=self._make_aliases())
             self._data = mapped_data
 
     def report(
@@ -1234,18 +1234,18 @@
         ignore_errors: Optional[bool] = None,
         omit: Optional[Union[str, List[str]]] = None,
         include: Optional[Union[str, List[str]]] = None,
         contexts: Optional[List[str]] = None,
     ) -> float:
         """Generate an LCOV report of coverage results.
 
-        Each module in 'morfs' is included in the report. 'outfile' is the
+        Each module in `morfs` is included in the report. `outfile` is the
         path to write the file to, "-" will write to stdout.
 
-        See :meth 'report' for other arguments.
+        See :meth:`report` for other arguments.
 
         .. versionadded:: 6.3
         """
         self._prepare_data_for_reporting()
         with override_config(
             self,
             ignore_errors=ignore_errors,
@@ -1271,46 +1271,46 @@
                 entry = plugin._coverage_plugin_name
                 if not plugin._coverage_enabled:
                     entry += " (disabled)"
                 entries.append(entry)
             return entries
 
         info = [
-            ('coverage_version', covmod.__version__),
-            ('coverage_module', covmod.__file__),
-            ('tracer', self._collector.tracer_name() if self._collector is not None else "-none-"),
-            ('CTracer', 'available' if HAS_CTRACER else "unavailable"),
-            ('plugins.file_tracers', plugin_info(self._plugins.file_tracers)),
-            ('plugins.configurers', plugin_info(self._plugins.configurers)),
-            ('plugins.context_switchers', plugin_info(self._plugins.context_switchers)),
-            ('configs_attempted', self.config.attempted_config_files),
-            ('configs_read', self.config.config_files_read),
-            ('config_file', self.config.config_file),
-            ('config_contents',
-                repr(self.config._config_contents) if self.config._config_contents else '-none-'
+            ("coverage_version", covmod.__version__),
+            ("coverage_module", covmod.__file__),
+            ("tracer", self._collector.tracer_name() if self._collector is not None else "-none-"),
+            ("CTracer", "available" if HAS_CTRACER else "unavailable"),
+            ("plugins.file_tracers", plugin_info(self._plugins.file_tracers)),
+            ("plugins.configurers", plugin_info(self._plugins.configurers)),
+            ("plugins.context_switchers", plugin_info(self._plugins.context_switchers)),
+            ("configs_attempted", self.config.attempted_config_files),
+            ("configs_read", self.config.config_files_read),
+            ("config_file", self.config.config_file),
+            ("config_contents",
+                repr(self.config._config_contents) if self.config._config_contents else "-none-"
             ),
-            ('data_file', self._data.data_filename() if self._data is not None else "-none-"),
-            ('python', sys.version.replace('\n', '')),
-            ('platform', platform.platform()),
-            ('implementation', platform.python_implementation()),
-            ('executable', sys.executable),
-            ('def_encoding', sys.getdefaultencoding()),
-            ('fs_encoding', sys.getfilesystemencoding()),
-            ('pid', os.getpid()),
-            ('cwd', os.getcwd()),
-            ('path', sys.path),
-            ('environment', human_sorted(
+            ("data_file", self._data.data_filename() if self._data is not None else "-none-"),
+            ("python", sys.version.replace("\n", "")),
+            ("platform", platform.platform()),
+            ("implementation", platform.python_implementation()),
+            ("executable", sys.executable),
+            ("def_encoding", sys.getdefaultencoding()),
+            ("fs_encoding", sys.getfilesystemencoding()),
+            ("pid", os.getpid()),
+            ("cwd", os.getcwd()),
+            ("path", sys.path),
+            ("environment", human_sorted(
                 f"{k} = {v}"
                 for k, v in os.environ.items()
                 if (
                     any(slug in k for slug in ("COV", "PY")) or
                     (k in ("HOME", "TEMP", "TMP"))
                 )
             )),
-            ('command_line', " ".join(getattr(sys, 'argv', ['-none-']))),
+            ("command_line", " ".join(getattr(sys, "argv", ["-none-"]))),
         ]
 
         if self._inorout is not None:
             info.extend(self._inorout.sys_info())
 
         info.extend(CoverageData.sys_info())
 
@@ -1320,15 +1320,15 @@
 # Mega debugging...
 # $set_env.py: COVERAGE_DEBUG_CALLS - Lots and lots of output about calls to Coverage.
 if int(os.environ.get("COVERAGE_DEBUG_CALLS", 0)):              # pragma: debugging
     from coverage.debug import decorate_methods, show_calls
 
     Coverage = decorate_methods(        # type: ignore[misc]
         show_calls(show_args=True),
-        butnot=['get_data']
+        butnot=["get_data"]
     )(Coverage)
 
 
 def process_startup() -> Optional[Coverage]:
     """Call this at Python start-up to perhaps measure coverage.
 
     If the environment variable COVERAGE_PROCESS_START is defined, coverage
```

### Comparing `coverage-7.2.2/coverage/ctracer/datastack.c` & `coverage-7.2.3/coverage/ctracer/datastack.c`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/datastack.h` & `coverage-7.2.3/coverage/ctracer/datastack.h`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/filedisp.c` & `coverage-7.2.3/coverage/ctracer/filedisp.c`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/filedisp.h` & `coverage-7.2.3/coverage/ctracer/filedisp.h`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/module.c` & `coverage-7.2.3/coverage/ctracer/module.c`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/stats.h` & `coverage-7.2.3/coverage/ctracer/stats.h`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/tracer.c` & `coverage-7.2.3/coverage/ctracer/tracer.c`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/tracer.h` & `coverage-7.2.3/coverage/ctracer/tracer.h`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/ctracer/util.h` & `coverage-7.2.3/coverage/ctracer/util.h`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/data.py` & `coverage-7.2.3/coverage/data.py`

 * *Files 2% similar despite different names*

```diff
@@ -129,15 +129,15 @@
     file_hashes = set()
     combined_any = False
 
     for f in files_to_combine:
         if f == data.data_filename():
             # Sometimes we are combining into a file which is one of the
             # parallel files.  Skip that file.
-            if data._debug.should('dataio'):
+            if data._debug.should("dataio"):
                 data._debug.write(f"Skipping combining ourself: {f!r}")
             continue
 
         try:
             rel_file_name = os.path.relpath(f)
         except ValueError:
             # ValueError can be raised under Windows when os.getcwd() returns a
@@ -149,15 +149,15 @@
             hasher = hashlib.new("sha3_256")
             hasher.update(fobj.read())
             sha = hasher.digest()
             combine_this_one = sha not in file_hashes
 
         delete_this_one = not keep
         if combine_this_one:
-            if data._debug.should('dataio'):
+            if data._debug.should("dataio"):
                 data._debug.write(f"Combining data file {f!r}")
             file_hashes.add(sha)
             try:
                 new_data = CoverageData(f, debug=data._debug)
                 new_data.read()
             except CoverageException as exc:
                 if data._warn:
@@ -173,15 +173,15 @@
                 if message:
                     message(f"Combined data file {rel_file_name}")
         else:
             if message:
                 message(f"Skipping duplicate data {rel_file_name}")
 
         if delete_this_one:
-            if data._debug.should('dataio'):
+            if data._debug.should("dataio"):
                 data._debug.write(f"Deleting data file {f!r}")
             file_be_gone(f)
 
     if strict and not combined_any:
         raise NoDataError("No usable data files")
```

### Comparing `coverage-7.2.2/coverage/debug.py` & `coverage-7.2.3/coverage/debug.py`

 * *Files 2% similar despite different names*

```diff
@@ -46,20 +46,20 @@
         file_name: Optional[str] = None,
     ) -> None:
         """Configure the options and output file for debugging."""
         self.options = list(options) + FORCED_DEBUG
         self.suppress_callers = False
 
         filters = []
-        if self.should('pid'):
+        if self.should("pid"):
             filters.append(add_pid_and_tid)
         self.output = DebugOutputFile.get_one(
             output,
             file_name=file_name,
-            show_process=self.should('process'),
+            show_process=self.should("process"),
             filters=filters,
         )
         self.raw_output = self.output.outfile
 
     def __repr__(self) -> str:
         return f"<DebugControl options={self.options!r} raw_output={self.raw_output!r}>"
 
@@ -82,19 +82,19 @@
     def write(self, msg: str) -> None:
         """Write a line of debug output.
 
         `msg` is the line to write. A newline will be appended.
 
         """
         self.output.write(msg+"\n")
-        if self.should('self'):
-            caller_self = inspect.stack()[1][0].f_locals.get('self')
+        if self.should("self"):
+            caller_self = inspect.stack()[1][0].f_locals.get("self")
             if caller_self is not None:
                 self.output.write(f"self: {caller_self!r}\n")
-        if self.should('callers'):
+        if self.should("callers"):
             dump_stack_frames(out=self.output, skip=1)
         self.output.flush()
 
 
 class DebugControlString(DebugControl):
     """A `DebugControl` that writes to a StringIO, for testing."""
     def __init__(self, options: Iterable[str]) -> None:
@@ -224,15 +224,15 @@
     tid = f"{short_id(_thread.get_ident()):04x}"
     text = f"{os.getpid():5d}.{tid}: {text}"
     return text
 
 
 class AutoReprMixin:
     """A mixin implementing an automatic __repr__ for debugging."""
-    auto_repr_ignore = ['auto_repr_ignore', '$coverage.object_id']
+    auto_repr_ignore = ["auto_repr_ignore", "$coverage.object_id"]
 
     def __repr__(self) -> str:
         show_attrs = (
             (k, v) for k, v in self.__dict__.items()
             if getattr(v, "show_repr_attr", True)
             and not callable(v)
             and k not in self.auto_repr_ignore
@@ -247,15 +247,15 @@
 def simplify(v: Any) -> Any:                                # pragma: debugging
     """Turn things which are nearly dict/list/etc into dict/list/etc."""
     if isinstance(v, dict):
         return {k:simplify(vv) for k, vv in v.items()}
     elif isinstance(v, (list, tuple)):
         return type(v)(simplify(vv) for vv in v)
     elif hasattr(v, "__dict__"):
-        return simplify({'.'+k: v for k, v in v.__dict__.items()})
+        return simplify({"."+k: v for k, v in v.__dict__.items()})
     else:
         return v
 
 
 def pp(v: Any) -> None:                                     # pragma: debugging
     """Debug helper to pretty-print data, including SimpleNamespace objects."""
     # Might not be needed in 3.9+
@@ -308,16 +308,16 @@
         self.outfile = outfile
         self.show_process = show_process
         self.filters = list(filters)
 
         if self.show_process:
             self.filters.insert(0, CwdTracker().filter)
             self.write(f"New process: executable: {sys.executable!r}\n")
-            self.write("New process: cmd: {!r}\n".format(getattr(sys, 'argv', None)))
-            if hasattr(os, 'getppid'):
+            self.write("New process: cmd: {!r}\n".format(getattr(sys, "argv", None)))
+            if hasattr(os, "getppid"):
                 self.write(f"New process: pid: {os.getpid()!r}, parent pid: {os.getppid()!r}\n")
 
     @classmethod
     def get_one(
         cls,
         fileobj: Optional[IO[str]] = None,
         file_name: Optional[str] = None,
@@ -363,16 +363,16 @@
         return the_one
 
     # Because of the way igor.py deletes and re-imports modules,
     # this class can be defined more than once. But we really want
     # a process-wide singleton. So stash it in sys.modules instead of
     # on a class attribute. Yes, this is aggressively gross.
 
-    SYS_MOD_NAME = '$coverage.debug.DebugOutputFile.the_one'
-    SINGLETON_ATTR = 'the_one_and_is_interim'
+    SYS_MOD_NAME = "$coverage.debug.DebugOutputFile.the_one"
+    SINGLETON_ATTR = "the_one_and_is_interim"
 
     @classmethod
     def _set_singleton_data(cls, the_one: DebugOutputFile, interim: bool) -> None:
         """Set the one DebugOutputFile to rule them all."""
         singleton_module = types.ModuleType(cls.SYS_MOD_NAME)
         setattr(singleton_module, cls.SINGLETON_ATTR, (the_one, interim))
         sys.modules[cls.SYS_MOD_NAME] = singleton_module
@@ -481,11 +481,11 @@
         return _wrapper
     return _decorator
 
 
 def _clean_stack_line(s: str) -> str:                       # pragma: debugging
     """Simplify some paths in a stack trace, for compactness."""
     s = s.strip()
-    s = s.replace(os.path.dirname(__file__) + '/', '')
-    s = s.replace(os.path.dirname(os.__file__) + '/', '')
-    s = s.replace(sys.prefix + '/', '')
+    s = s.replace(os.path.dirname(__file__) + "/", "")
+    s = s.replace(os.path.dirname(os.__file__) + "/", "")
+    s = s.replace(sys.prefix + "/", "")
     return s
```

### Comparing `coverage-7.2.2/coverage/disposition.py` & `coverage-7.2.3/coverage/disposition.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/env.py` & `coverage-7.2.3/coverage/env.py`

 * *Files 5% similar despite different names*

```diff
@@ -36,15 +36,15 @@
 
 # Python behavior.
 class PYBEHAVIOR:
     """Flags indicating this Python's behavior."""
 
     # Does Python conform to PEP626, Precise line numbers for debugging and other tools.
     # https://www.python.org/dev/peps/pep-0626
-    pep626 = CPYTHON and (PYVERSION > (3, 10, 0, 'alpha', 4))
+    pep626 = CPYTHON and (PYVERSION > (3, 10, 0, "alpha", 4))
 
     # Is "if __debug__" optimized away?
     if PYPY:
         optimize_if_debug = True
     else:
         optimize_if_debug = not pep626
 
@@ -56,24 +56,24 @@
         if PYVERSION >= (3, 9):
             optimize_if_not_debug = 2
         elif PYVERSION[:2] == (3, 8):
             optimize_if_not_debug = 3
         else:
             optimize_if_not_debug = 1
     else:
-        if PYVERSION >= (3, 8, 0, 'beta', 1):
+        if PYVERSION >= (3, 8, 0, "beta", 1):
             optimize_if_not_debug = 2
         else:
             optimize_if_not_debug = 1
 
     # Can co_lnotab have negative deltas?
     negative_lnotab = not (PYPY and PYPYVERSION < (7, 2))
 
     # 3.7 changed how functions with only docstrings are numbered.
-    docstring_only_function = (not PYPY) and ((3, 7, 0, 'beta', 5) <= PYVERSION <= (3, 10))
+    docstring_only_function = (not PYPY) and ((3, 7, 0, "beta", 5) <= PYVERSION <= (3, 10))
 
     # When a break/continue/return statement in a try block jumps to a finally
     # block, does the finally block do the break/continue/return (pre-3.8), or
     # does the finally jump back to the break/continue/return (3.8) to do the
     # work?
     finally_jumps_back = ((3, 8) <= PYVERSION < (3, 10))
     if PYPY and PYPYVERSION < (7, 3, 7):
@@ -89,15 +89,15 @@
 
     # Functions are no longer claimed to start at their earliest decorator even though
     # the decorators are traced?
     def_ast_no_decorator = (PYPY and PYVERSION >= (3, 9))
 
     # CPython 3.11 now jumps to the decorator line again while executing
     # the decorator.
-    trace_decorator_line_again = (CPYTHON and PYVERSION > (3, 11, 0, 'alpha', 3, 0))
+    trace_decorator_line_again = (CPYTHON and PYVERSION > (3, 11, 0, "alpha", 3, 0))
 
     # Are while-true loops optimized into absolute jumps with no loop setup?
     nix_while_true = (PYVERSION >= (3, 8))
 
     # CPython 3.9a1 made sys.argv[0] and other reported files absolute paths.
     report_absolute_files = (
         (CPYTHON or (PYPY and PYPYVERSION >= (7, 3, 10)))
@@ -121,38 +121,38 @@
     # real line of code.  Now they always start at 1.
     module_firstline_1 = pep626
 
     # Are "if 0:" lines (and similar) kept in the compiled code?
     keep_constant_test = pep626
 
     # When leaving a with-block, do we visit the with-line again for the exit?
-    exit_through_with = (PYVERSION >= (3, 10, 0, 'beta'))
+    exit_through_with = (PYVERSION >= (3, 10, 0, "beta"))
 
     # Match-case construct.
     match_case = (PYVERSION >= (3, 10))
 
     # Some words are keywords in some places, identifiers in other places.
     soft_keywords = (PYVERSION >= (3, 10))
 
     # Modules start with a line numbered zero. This means empty modules have
     # only a 0-number line, which is ignored, giving a truly empty module.
-    empty_is_empty = (PYVERSION >= (3, 11, 0, 'beta', 4))
+    empty_is_empty = (PYVERSION >= (3, 11, 0, "beta", 4))
 
 # Coverage.py specifics.
 
 # Are we using the C-implemented trace function?
-C_TRACER = os.getenv('COVERAGE_TEST_TRACER', 'c') == 'c'
+C_TRACER = os.getenv("COVERAGE_TEST_TRACER", "c") == "c"
 
 # Are we coverage-measuring ourselves?
-METACOV = os.getenv('COVERAGE_COVERAGE', '') != ''
+METACOV = os.getenv("COVERAGE_COVERAGE", "") != ""
 
 # Are we running our test suite?
 # Even when running tests, you can use COVERAGE_TESTING=0 to disable the
 # test-specific behavior like AST checking.
-TESTING = os.getenv('COVERAGE_TESTING', '') == 'True'
+TESTING = os.getenv("COVERAGE_TESTING", "") == "True"
 
 
 def debug_info() -> Iterable[Tuple[str, Any]]:
     """Return a list of (name, value) pairs for printing debug information."""
     info = [
         (name, value) for name, value in globals().items()
         if not name.startswith("_") and name not in _UNINTERESTING_GLOBALS
```

### Comparing `coverage-7.2.2/coverage/exceptions.py` & `coverage-7.2.3/coverage/exceptions.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/execfile.py` & `coverage-7.2.3/coverage/execfile.py`

 * *Files 2% similar despite different names*

```diff
@@ -168,29 +168,29 @@
 
     def run(self) -> None:
         """Run the Python code!"""
 
         self._prepare2()
 
         # Create a module to serve as __main__
-        main_mod = ModuleType('__main__')
+        main_mod = ModuleType("__main__")
 
         from_pyc = self.arg0.endswith((".pyc", ".pyo"))
         main_mod.__file__ = self.arg0
         if from_pyc:
             main_mod.__file__ = main_mod.__file__[:-1]
         if self.package is not None:
             main_mod.__package__ = self.package
         main_mod.__loader__ = self.loader   # type: ignore[assignment]
         if self.spec is not None:
             main_mod.__spec__ = self.spec
 
-        main_mod.__builtins__ = sys.modules['builtins']     # type: ignore[attr-defined]
+        main_mod.__builtins__ = sys.modules["builtins"]     # type: ignore[attr-defined]
 
-        sys.modules['__main__'] = main_mod
+        sys.modules["__main__"] = main_mod
 
         # Set sys.argv properly.
         sys.argv = self.args
 
         try:
             # Make a code object somehow.
             if from_pyc:
@@ -224,15 +224,15 @@
             assert err is not None
             assert tb is not None
 
             # PyPy3 weirdness.  If I don't access __context__, then somehow it
             # is non-None when the exception is reported at the upper layer,
             # and a nested exception is shown to the user.  This getattr fixes
             # it somehow? https://bitbucket.org/pypy/pypy/issue/1903
-            getattr(err, '__context__', None)
+            getattr(err, "__context__", None)
 
             # Call the excepthook.
             try:
                 assert err.__traceback__ is not None
                 err.__traceback__ = err.__traceback__.tb_next
                 sys.excepthook(typ, err, tb.tb_next)
             except SystemExit:                      # pylint: disable=try-except-raise
@@ -307,15 +307,15 @@
     with fpyc:
         # First four bytes are a version-specific magic number.  It has to
         # match or we won't run the file.
         magic = fpyc.read(4)
         if magic != PYC_MAGIC_NUMBER:
             raise NoCode(f"Bad magic number in .pyc file: {magic!r} != {PYC_MAGIC_NUMBER!r}")
 
-        flags = struct.unpack('<L', fpyc.read(4))[0]
+        flags = struct.unpack("<L", fpyc.read(4))[0]
         hash_based = flags & 0x01
         if hash_based:
             fpyc.read(8)    # Skip the hash.
         else:
             # Skip the junk in the header that we don't need.
             fpyc.read(4)    # Skip the moddate.
             fpyc.read(4)    # Skip the size.
```

### Comparing `coverage-7.2.2/coverage/files.py` & `coverage-7.2.3/coverage/files.py`

 * *Files 0% similar despite different names*

```diff
@@ -159,15 +159,15 @@
 def zip_location(filename: str) -> Optional[Tuple[str, str]]:
     """Split a filename into a zipfile / inner name pair.
 
     Only return a pair if the zipfile exists.  No check is made if the inner
     name is in the zipfile.
 
     """
-    for ext in ['.zip', '.whl', '.egg', '.pex']:
+    for ext in [".zip", ".whl", ".egg", ".pex"]:
         zipbase, extension, inner = filename.partition(ext + sep(filename))
         if extension:
             zipfile = zipbase + ext
             if os.path.exists(zipfile):
                 return zipfile, inner
     return None
 
@@ -269,15 +269,15 @@
         if not module_name:
             return False
 
         for m in self.modules:
             if module_name.startswith(m):
                 if module_name == m:
                     return True
-                if module_name[len(m)] == '.':
+                if module_name[len(m)] == ".":
                     # This is a module in the package
                     return True
 
         return False
 
 
 class GlobMatcher:
@@ -429,15 +429,15 @@
         # The pattern can't end with a wildcard component.
         if pattern.endswith("*"):
             raise ConfigError("Pattern must not end with wildcards.")
 
         # The pattern is meant to match a file path.  Let's make it absolute
         # unless it already is, or is meant to match any prefix.
         if not self.relative:
-            if not pattern.startswith('*') and not isabs_anywhere(pattern + pattern_sep):
+            if not pattern.startswith("*") and not isabs_anywhere(pattern + pattern_sep):
                 pattern = abs_file(pattern)
         if not pattern.endswith(pattern_sep):
             pattern += pattern_sep
 
         # Make a regex from the pattern.
         regex = globs_to_regex([pattern], case_insensitive=True, partial=True)
```

### Comparing `coverage-7.2.2/coverage/fullcoverage/encodings.py` & `coverage-7.2.3/coverage/fullcoverage/encodings.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/html.py` & `coverage-7.2.3/coverage/html.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,19 +1,22 @@
 # Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
 # For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt
 
 """HTML reporting for coverage.py."""
 
 from __future__ import annotations
 
+import collections
 import datetime
+import functools
 import json
 import os
 import re
 import shutil
+import string  # pylint: disable=deprecated-module
 
 from dataclasses import dataclass
 from typing import Any, Dict, Iterable, List, Optional, Tuple, TYPE_CHECKING, cast
 
 import coverage
 from coverage.data import CoverageData, add_data_to_hash
 from coverage.exceptions import NoDataError
@@ -64,15 +67,15 @@
         return data_file.read()
 
 
 def write_html(fname: str, html: str) -> None:
     """Write `html` to `fname`, properly encoded."""
     html = re.sub(r"(\A\s+)|(\s+$)", "", html, flags=re.MULTILINE) + "\n"
     with open(fname, "wb") as fout:
-        fout.write(html.encode('ascii', 'xmlcharrefreplace'))
+        fout.write(html.encode("ascii", "xmlcharrefreplace"))
 
 
 @dataclass
 class LineData:
     """The data for each source line of HTML output."""
     tokens: List[Tuple[str, str]]
     number: TLineNo
@@ -80,14 +83,15 @@
     statement: bool
     contexts: List[str]
     contexts_label: str
     context_list: List[str]
     short_annotations: List[str]
     long_annotations: List[str]
     html: str = ""
+    context_str: Optional[str] = None
     annotate: Optional[str] = None
     annotate_long: Optional[str] = None
     css_class: str = ""
 
 
 @dataclass
 class FileData:
@@ -126,27 +130,27 @@
         for lineno, tokens in enumerate(fr.source_token_lines(), start=1):
             # Figure out how to mark this line.
             category = ""
             short_annotations = []
             long_annotations = []
 
             if lineno in analysis.excluded:
-                category = 'exc'
+                category = "exc"
             elif lineno in analysis.missing:
-                category = 'mis'
+                category = "mis"
             elif self.has_arcs and lineno in missing_branch_arcs:
-                category = 'par'
+                category = "par"
                 for b in missing_branch_arcs[lineno]:
                     if b < 0:
                         short_annotations.append("exit")
                     else:
                         short_annotations.append(str(b))
                     long_annotations.append(fr.missing_arc_description(lineno, b, arcs_executed))
             elif lineno in analysis.statements:
-                category = 'run'
+                category = "run"
 
             contexts = []
             contexts_label = ""
             context_list = []
             if category and self.config.show_contexts:
                 contexts = human_sorted(c or self.EMPTY for c in contexts_by_lineno.get(lineno, ()))
                 if contexts == [self.EMPTY]:
@@ -181,14 +185,29 @@
     def __init__(self, fr: FileReporter, analysis: Analysis) -> None:
         self.fr = fr
         self.analysis = analysis
         self.rootname = flat_rootname(fr.relative_filename())
         self.html_filename = self.rootname + ".html"
 
 
+HTML_SAFE = string.ascii_letters + string.digits + "!#$%'()*+,-./:;=?@[]^_`{|}~"
+
+@functools.lru_cache(maxsize=None)
+def encode_int(n: int) -> str:
+    """Create a short HTML-safe string from an integer, using HTML_SAFE."""
+    if n == 0:
+        return HTML_SAFE[0]
+
+    r = []
+    while n:
+        n, t = divmod(n, len(HTML_SAFE))
+        r.append(HTML_SAFE[t])
+    return "".join(r)
+
+
 class HtmlReporter:
     """HTML reporting."""
 
     # These files will be copied from the htmlfiles directory to the output
     # directory.
     STATIC_FILES = [
         "style.css",
@@ -230,34 +249,34 @@
         self.totals = Numbers(precision=self.config.precision)
         self.directory_was_empty = False
         self.first_fr = None
         self.final_fr = None
 
         self.template_globals = {
             # Functions available in the templates.
-            'escape': escape,
-            'pair': pair,
-            'len': len,
+            "escape": escape,
+            "pair": pair,
+            "len": len,
 
             # Constants for this report.
-            '__url__': __url__,
-            '__version__': coverage.__version__,
-            'title': title,
-            'time_stamp': format_local_datetime(datetime.datetime.now()),
-            'extra_css': self.extra_css,
-            'has_arcs': self.has_arcs,
-            'show_contexts': self.config.show_contexts,
+            "__url__": __url__,
+            "__version__": coverage.__version__,
+            "title": title,
+            "time_stamp": format_local_datetime(datetime.datetime.now()),
+            "extra_css": self.extra_css,
+            "has_arcs": self.has_arcs,
+            "show_contexts": self.config.show_contexts,
 
             # Constants for all reports.
             # These css classes determine which lines are highlighted by default.
-            'category': {
-                'exc': 'exc show_exc',
-                'mis': 'mis show_mis',
-                'par': 'par run show_par',
-                'run': 'run',
+            "category": {
+                "exc": "exc show_exc",
+                "mis": "mis show_mis",
+                "par": "par run show_par",
+                "run": "run",
             },
         }
         self.pyfile_html_source = read_data("pyfile.html")
         self.source_tmpl = Templite(self.pyfile_html_source, self.template_globals)
 
     def report(self, morfs: Optional[Iterable[TMorf]]) -> float:
         """Generate an HTML report for `morfs`.
@@ -363,26 +382,46 @@
         # Find out if the file on disk is already correct.
         if self.incr.can_skip_file(self.data, ftr.fr, ftr.rootname):
             self.file_summaries.append(self.incr.index_info(ftr.rootname))
             return
 
         # Write the HTML page for this file.
         file_data = self.datagen.data_for_file(ftr.fr, ftr.analysis)
+
+        contexts = collections.Counter(c for cline in file_data.lines for c in cline.contexts)
+        context_codes = {y: i for (i, y) in enumerate(x[0] for x in contexts.most_common())}
+        if context_codes:
+            contexts_json = json.dumps(
+                {encode_int(v): k for (k, v) in context_codes.items()},
+                indent=2,
+            )
+        else:
+            contexts_json = None
+
         for ldata in file_data.lines:
             # Build the HTML for the line.
             html_parts = []
             for tok_type, tok_text in ldata.tokens:
                 if tok_type == "ws":
                     html_parts.append(escape(tok_text))
                 else:
-                    tok_html = escape(tok_text) or '&nbsp;'
-                    html_parts.append(
-                        f'<span class="{tok_type}">{tok_html}</span>'
-                    )
-            ldata.html = ''.join(html_parts)
+                    tok_html = escape(tok_text) or "&nbsp;"
+                    html_parts.append(f'<span class="{tok_type}">{tok_html}</span>')
+            ldata.html = "".join(html_parts)
+            if ldata.context_list:
+                encoded_contexts = [
+                    encode_int(context_codes[c_context]) for c_context in ldata.context_list
+                ]
+                code_width = max(len(ec) for ec in encoded_contexts)
+                ldata.context_str = (
+                    str(code_width)
+                    + "".join(ec.ljust(code_width) for ec in encoded_contexts)
+                )
+            else:
+                ldata.context_str = ""
 
             if ldata.short_annotations:
                 # 202F is NARROW NO-BREAK SPACE.
                 # 219B is RIGHTWARDS ARROW WITH STROKE.
                 ldata.annotate = ",&nbsp;&nbsp; ".join(
                     f"{ldata.number}&#x202F;&#x219B;&#x202F;{d}"
                     for d in ldata.short_annotations
@@ -404,31 +443,32 @@
                     )
             else:
                 ldata.annotate_long = None
 
             css_classes = []
             if ldata.category:
                 css_classes.append(
-                    self.template_globals['category'][ldata.category]   # type: ignore[index]
+                    self.template_globals["category"][ldata.category]   # type: ignore[index]
                 )
-            ldata.css_class = ' '.join(css_classes) or "pln"
+            ldata.css_class = " ".join(css_classes) or "pln"
 
         html_path = os.path.join(self.directory, ftr.html_filename)
         html = self.source_tmpl.render({
             **file_data.__dict__,
-            'prev_html': prev_html,
-            'next_html': next_html,
+            "contexts_json": contexts_json,
+            "prev_html": prev_html,
+            "next_html": next_html,
         })
         write_html(html_path, html)
 
         # Save this file's information for the index file.
         index_info: IndexInfoDict = {
-            'nums': ftr.analysis.numbers,
-            'html_filename': ftr.html_filename,
-            'relative_filename': ftr.fr.relative_filename(),
+            "nums": ftr.analysis.numbers,
+            "html_filename": ftr.html_filename,
+            "relative_filename": ftr.fr.relative_filename(),
         }
         self.file_summaries.append(index_info)
         self.incr.set_index_info(ftr.rootname, index_info)
 
     def index_file(self, first_html: str, final_html: str) -> None:
         """Write the index.html file for this report."""
         self.make_directory()
@@ -439,20 +479,20 @@
             n = self.skipped_covered_count
             skipped_covered_msg = f"{n} file{plural(n)} skipped due to complete coverage."
         if self.skipped_empty_count:
             n = self.skipped_empty_count
             skipped_empty_msg = f"{n} empty file{plural(n)} skipped."
 
         html = index_tmpl.render({
-            'files': self.file_summaries,
-            'totals': self.totals,
-            'skipped_covered_msg': skipped_covered_msg,
-            'skipped_empty_msg': skipped_empty_msg,
-            'first_html': first_html,
-            'final_html': final_html,
+            "files": self.file_summaries,
+            "totals": self.totals,
+            "skipped_covered_msg": skipped_covered_msg,
+            "skipped_empty_msg": skipped_empty_msg,
+            "first_html": first_html,
+            "final_html": final_html,
         })
 
         index_file = os.path.join(self.directory, "index.html")
         write_html(index_file, html)
         self.coverage._message(f"Wrote HTML report to {index_file}")
 
         # Write the latest hashes for next time.
@@ -494,59 +534,59 @@
 
     def __init__(self, directory: str) -> None:
         self.directory = directory
         self.reset()
 
     def reset(self) -> None:
         """Initialize to empty. Causes all files to be reported."""
-        self.globals = ''
+        self.globals = ""
         self.files: Dict[str, FileInfoDict] = {}
 
     def read(self) -> None:
         """Read the information we stored last time."""
         usable = False
         try:
             status_file = os.path.join(self.directory, self.STATUS_FILE)
             with open(status_file) as fstatus:
                 status = json.load(fstatus)
         except (OSError, ValueError):
             usable = False
         else:
             usable = True
-            if status['format'] != self.STATUS_FORMAT:
+            if status["format"] != self.STATUS_FORMAT:
                 usable = False
-            elif status['version'] != coverage.__version__:
+            elif status["version"] != coverage.__version__:
                 usable = False
 
         if usable:
             self.files = {}
-            for filename, fileinfo in status['files'].items():
-                fileinfo['index']['nums'] = Numbers(*fileinfo['index']['nums'])
+            for filename, fileinfo in status["files"].items():
+                fileinfo["index"]["nums"] = Numbers(*fileinfo["index"]["nums"])
                 self.files[filename] = fileinfo
-            self.globals = status['globals']
+            self.globals = status["globals"]
         else:
             self.reset()
 
     def write(self) -> None:
         """Write the current status."""
         status_file = os.path.join(self.directory, self.STATUS_FILE)
         files = {}
         for filename, fileinfo in self.files.items():
-            index = fileinfo['index']
-            index['nums'] = index['nums'].init_args()   # type: ignore[typeddict-item]
+            index = fileinfo["index"]
+            index["nums"] = index["nums"].init_args()   # type: ignore[typeddict-item]
             files[filename] = fileinfo
 
         status = {
-            'format': self.STATUS_FORMAT,
-            'version': coverage.__version__,
-            'globals': self.globals,
-            'files': files,
+            "format": self.STATUS_FORMAT,
+            "version": coverage.__version__,
+            "globals": self.globals,
+            "files": files,
         }
         with open(status_file, "w") as fout:
-            json.dump(status, fout, separators=(',', ':'))
+            json.dump(status, fout, separators=(",", ":"))
 
     def check_global_data(self, *data: Any) -> None:
         """Check the global data that can affect incremental reporting."""
         m = Hasher()
         for d in data:
             m.update(d)
         these_globals = m.hexdigest()
@@ -557,42 +597,42 @@
     def can_skip_file(self, data: CoverageData, fr: FileReporter, rootname: str) -> bool:
         """Can we skip reporting this file?
 
         `data` is a CoverageData object, `fr` is a `FileReporter`, and
         `rootname` is the name being used for the file.
         """
         m = Hasher()
-        m.update(fr.source().encode('utf-8'))
+        m.update(fr.source().encode("utf-8"))
         add_data_to_hash(data, fr.filename, m)
         this_hash = m.hexdigest()
 
         that_hash = self.file_hash(rootname)
 
         if this_hash == that_hash:
             # Nothing has changed to require the file to be reported again.
             return True
         else:
             self.set_file_hash(rootname, this_hash)
             return False
 
     def file_hash(self, fname: str) -> str:
         """Get the hash of `fname`'s contents."""
-        return self.files.get(fname, {}).get('hash', '')    # type: ignore[call-overload]
+        return self.files.get(fname, {}).get("hash", "")    # type: ignore[call-overload]
 
     def set_file_hash(self, fname: str, val: str) -> None:
         """Set the hash of `fname`'s contents."""
-        self.files.setdefault(fname, {})['hash'] = val      # type: ignore[typeddict-item]
+        self.files.setdefault(fname, {})["hash"] = val      # type: ignore[typeddict-item]
 
     def index_info(self, fname: str) -> IndexInfoDict:
         """Get the information for index.html for `fname`."""
-        return self.files.get(fname, {}).get('index', {})   # type: ignore
+        return self.files.get(fname, {}).get("index", {})   # type: ignore
 
     def set_index_info(self, fname: str, info: IndexInfoDict) -> None:
         """Set the information for index.html for `fname`."""
-        self.files.setdefault(fname, {})['index'] = info    # type: ignore[typeddict-item]
+        self.files.setdefault(fname, {})["index"] = info    # type: ignore[typeddict-item]
 
 
 # Helpers for templates and generating HTML
 
 def escape(t: str) -> str:
     """HTML-escape the text in `t`.
```

### Comparing `coverage-7.2.2/coverage/htmlfiles/coverage_html.js` & `coverage-7.2.3/coverage/htmlfiles/coverage_html.js`

 * *Files 3% similar despite different names*

#### js-beautify {}

```diff
@@ -221,15 +221,15 @@
 // -- pyfile stuff --
 
 coverage.LINE_FILTERS_STORAGE = "COVERAGE_LINE_FILTERS";
 
 coverage.pyfile_ready = function() {
     // If we're directed to a particular line number, highlight the line.
     var frag = location.hash;
-    if (frag.length > 2 && frag[1] === 't') {
+    if (frag.length > 2 && frag[1] === "t") {
         document.querySelector(frag).closest(".n").classList.add("highlight");
         coverage.set_sel(parseInt(frag.substr(2), 10));
     } else {
         coverage.set_sel(0);
     }
 
     on_click(".button_toggle_run", coverage.toggle_lines);
@@ -268,14 +268,18 @@
         coverage.set_line_visibilty(cls, coverage.filters[cls]);
     }
 
     coverage.assign_shortkeys();
     coverage.init_scroll_markers();
     coverage.wire_up_sticky_header();
 
+    document.querySelectorAll("[id^=ctxs]").forEach(
+        cbox => cbox.addEventListener("click", coverage.expand_contexts)
+    );
+
     // Rebuild scroll markers when the window height changes.
     window.addEventListener("resize", coverage.build_scroll_markers);
 };
 
 coverage.toggle_lines = function(event) {
     const btn = event.target.closest("button");
     const category = btn.value
@@ -540,38 +544,38 @@
         top: to_pos,
         behavior: "smooth"
     });
 };
 
 coverage.init_scroll_markers = function() {
     // Init some variables
-    coverage.lines_len = document.querySelectorAll('#source > p').length;
+    coverage.lines_len = document.querySelectorAll("#source > p").length;
 
     // Build html
     coverage.build_scroll_markers();
 };
 
 coverage.build_scroll_markers = function() {
-    const temp_scroll_marker = document.getElementById('scroll_marker')
+    const temp_scroll_marker = document.getElementById("scroll_marker")
     if (temp_scroll_marker) temp_scroll_marker.remove();
     // Don't build markers if the window has no scroll bar.
     if (document.body.scrollHeight <= window.innerHeight) {
         return;
     }
 
     const marker_scale = window.innerHeight / document.body.scrollHeight;
     const line_height = Math.min(Math.max(3, window.innerHeight / coverage.lines_len), 10);
 
     let previous_line = -99,
         last_mark, last_top;
 
     const scroll_marker = document.createElement("div");
     scroll_marker.id = "scroll_marker";
-    document.getElementById('source').querySelectorAll(
-        'p.show_run, p.show_mis, p.show_exc, p.show_exc, p.show_par'
+    document.getElementById("source").querySelectorAll(
+        "p.show_run, p.show_mis, p.show_exc, p.show_exc, p.show_par"
     ).forEach(element => {
         const line_top = Math.floor(element.offsetTop * marker_scale);
         const line_number = parseInt(element.querySelector(".n a").id.substr(1));
 
         if (line_number === previous_line + 1) {
             // If this solid missed block just make previous mark higher.
             last_mark.style.height = `${line_top + line_height - last_top}px`;
@@ -590,32 +594,48 @@
     });
 
     // Append last to prevent layout calculation
     document.body.append(scroll_marker);
 };
 
 coverage.wire_up_sticky_header = function() {
-    const header = document.querySelector('header');
+    const header = document.querySelector("header");
     const header_bottom = (
-        header.querySelector('.content h2').getBoundingClientRect().top -
+        header.querySelector(".content h2").getBoundingClientRect().top -
         header.getBoundingClientRect().top
     );
 
     function updateHeader() {
         if (window.scrollY > header_bottom) {
-            header.classList.add('sticky');
+            header.classList.add("sticky");
         } else {
-            header.classList.remove('sticky');
+            header.classList.remove("sticky");
         }
     }
 
-    window.addEventListener('scroll', updateHeader);
+    window.addEventListener("scroll", updateHeader);
     updateHeader();
 };
 
+coverage.expand_contexts = function(e) {
+    var ctxs = e.target.parentNode.querySelector(".ctxs");
+
+    if (!ctxs.classList.contains("expanded")) {
+        var ctxs_text = ctxs.textContent;
+        var width = Number(ctxs_text[0]);
+        ctxs.textContent = "";
+        for (var i = 1; i < ctxs_text.length; i += width) {
+            key = ctxs_text.substring(i, i + width).trim();
+            ctxs.appendChild(document.createTextNode(contexts[key]));
+            ctxs.appendChild(document.createElement("br"));
+        }
+        ctxs.classList.add("expanded");
+    }
+};
+
 document.addEventListener("DOMContentLoaded", () => {
     if (document.body.classList.contains("indexfile")) {
         coverage.index_ready();
     } else {
         coverage.pyfile_ready();
     }
 });
```

### Comparing `coverage-7.2.2/coverage/htmlfiles/favicon_32.png` & `coverage-7.2.3/coverage/htmlfiles/favicon_32.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/htmlfiles/index.html` & `coverage-7.2.3/coverage/htmlfiles/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/htmlfiles/keybd_closed.png` & `coverage-7.2.3/coverage/htmlfiles/keybd_closed.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/htmlfiles/keybd_open.png` & `coverage-7.2.3/coverage/htmlfiles/keybd_open.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/htmlfiles/pyfile.html` & `coverage-7.2.3/coverage/htmlfiles/pyfile.html`

 * *Files 6% similar despite different names*

```diff
@@ -7,14 +7,21 @@
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>Coverage for {{relative_filename|escape}}: {{nums.pc_covered_str}}%</title>
     <link rel="icon" sizes="32x32" href="favicon_32.png">
     <link rel="stylesheet" href="style.css" type="text/css">
     {% if extra_css %}
         <link rel="stylesheet" href="{{ extra_css }}" type="text/css">
     {% endif %}
+
+    {% if contexts_json %}
+    <script type="text/javascript">
+        contexts = {{ contexts_json }}
+    </script>
+    {% endif %}
+
     <script type="text/javascript" src="coverage_html.js" defer></script>
 </head>
 <body class="pyfile">
 
 <header>
     <div class="content">
         <h1>
@@ -113,20 +120,16 @@
                     <span class="annotate long">{{line.annotate_long}}</span>
                 {% endif %}
                 {% if line.contexts %}
                     <label for="ctxs{{line.number}}" class="ctx">{{ line.contexts_label }}</label>
                 {% endif %}
             </span>
             {# Things that should appear below the line. #}
-            {% if line.context_list %}
-                <span class="ctxs">
-                    {% for context in line.context_list %}
-                        <span>{{context}}</span>
-                    {% endfor %}
-                </span>
+            {% if line.context_str %}
+                <span class="ctxs">{{ line.context_str }}</span>
             {% endif %}
         </p>
         {% endjoined %}
     {% endfor %}
 </main>
 
 <footer>
```

#### html2text {}

```diff
@@ -1,12 +1,13 @@
 {# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-
 2.0 #} {# For details: https://github.com/nedbat/coveragepy/blob/master/
 NOTICE.txt #}
 
  {% if extra_css %}
+ {% endif %} {% if contexts_json %}
  {% endif %}
 ****** Coverage for {{relative_filename|escape}}: {{nums.pc_covered_str}}%
 ******
  ⁰  [Show/hide keyboard shortcuts]
 Shortcuts on this page
 r m x {% if has_arcs %} p {% endif %}   toggle line displays
 j k   next/prev highlighted chunk
@@ -22,12 +23,11 @@
 created at {{ time_stamp }}
 
   {% for line in lines -%} {% joined %}
 {{line.number}} {{line.html}}  {% if line.context_list %} ⁰ {% endif %} {#
 Things that should float right in the line. #}  {% if line.annotate %} {
 {line.annotate}} {{line.annotate_long}} {% endif %} {% if line.contexts %} {
 { line.contexts_label }} {% endif %}  {# Things that should appear below the
-line. #} {% if line.context_list %}  {% for context in line.context_list %} {
-{context}} {% endfor %}  {% endif %}
+line. #} {% if line.context_str %} {{ line.context_str }} {% endif %}
 {% endjoined %} {% endfor %}
 &#xab;_prev     &Hat;_index     &#xbb;_next       coverage.py_v{{__version__}},
 created at {{ time_stamp }}
```

### Comparing `coverage-7.2.2/coverage/htmlfiles/style.css` & `coverage-7.2.3/coverage/htmlfiles/style.css`

 * *Files 0% similar despite different names*

```diff
@@ -254,20 +254,18 @@
 
 #source p input:checked ~ .ctxs { padding: .25em .5em; overflow-y: scroll; max-height: 10.5em; }
 
 #source p label.ctx { color: #999; display: inline-block; padding: 0 .5em; font-size: .8333em; }
 
 @media (prefers-color-scheme: dark) { #source p label.ctx { color: #777; } }
 
-#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; }
+#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; text-align: right; }
 
 @media (prefers-color-scheme: dark) { #source p .ctxs { background: #056; } }
 
-#source p .ctxs span { display: block; text-align: right; }
-
 #index { font-family: SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 0.875em; }
 
 #index table.index { margin-left: -.5em; }
 
 #index td, #index th { text-align: right; width: 5em; padding: .25em .5em; border-bottom: 1px solid #eee; }
 
 @media (prefers-color-scheme: dark) { #index td, #index th { border-color: #333; } }
```

### Comparing `coverage-7.2.2/coverage/htmlfiles/style.scss` & `coverage-7.2.3/coverage/htmlfiles/style.scss`

 * *Files 0% similar despite different names*

```diff
@@ -618,18 +618,15 @@
             padding: 0 .5em;
             font-family: $font-normal;
             white-space: nowrap;
             background: $light-context-bg-color;
             @include background-dark($dark-context-bg-color);
             border-radius: .25em;
             margin-right: 1.75em;
-            span {
-                display: block;
-                text-align: right;
-            }
+            text-align: right;
         }
     }
 }
 
 
 // index styles
 #index {
```

### Comparing `coverage-7.2.2/coverage/inorout.py` & `coverage-7.2.3/coverage/inorout.py`

 * *Files 2% similar despite different names*

```diff
@@ -79,47 +79,47 @@
     If loaded via runpy (aka -m), we can usually recover the "original"
     full dotted module name, otherwise, we resort to interpreting the
     file name to get the module's name.  In the case that the module name
     can't be determined, None is returned.
 
     """
     module_globals = frame.f_globals if frame is not None else {}
-    dunder_name: str = module_globals.get('__name__', None)
+    dunder_name: str = module_globals.get("__name__", None)
 
-    if isinstance(dunder_name, str) and dunder_name != '__main__':
+    if isinstance(dunder_name, str) and dunder_name != "__main__":
         # This is the usual case: an imported module.
         return dunder_name
 
-    loader = module_globals.get('__loader__', None)
-    for attrname in ('fullname', 'name'):   # attribute renamed in py3.2
+    loader = module_globals.get("__loader__", None)
+    for attrname in ("fullname", "name"):   # attribute renamed in py3.2
         if hasattr(loader, attrname):
             fullname = getattr(loader, attrname)
         else:
             continue
 
-        if isinstance(fullname, str) and fullname != '__main__':
+        if isinstance(fullname, str) and fullname != "__main__":
             # Module loaded via: runpy -m
             return fullname
 
     # Script as first argument to Python command line.
     inspectedname = inspect.getmodulename(filename)
     if inspectedname is not None:
         return inspectedname
     else:
         return dunder_name
 
 
 def module_is_namespace(mod: ModuleType) -> bool:
     """Is the module object `mod` a PEP420 namespace module?"""
-    return hasattr(mod, '__path__') and getattr(mod, '__file__', None) is None
+    return hasattr(mod, "__path__") and getattr(mod, "__file__", None) is None
 
 
 def module_has_file(mod: ModuleType) -> bool:
     """Does the module object `mod` have an existing __file__ ?"""
-    mod__file__ = getattr(mod, '__file__', None)
+    mod__file__ = getattr(mod, "__file__", None)
     if mod__file__ is None:
         return False
     return os.path.exists(mod__file__)
 
 
 def file_and_path_for_module(modulename: str) -> Tuple[Optional[str], List[str]]:
     """Find the file and search path for `modulename`.
@@ -309,43 +309,43 @@
 
         def nope(disp: TFileDisposition, reason: str) -> TFileDisposition:
             """Simple helper to make it easy to return NO."""
             disp.trace = False
             disp.reason = reason
             return disp
 
-        if original_filename.startswith('<'):
+        if original_filename.startswith("<"):
             return nope(disp, "original file name is not real")
 
         if frame is not None:
             # Compiled Python files have two file names: frame.f_code.co_filename is
             # the file name at the time the .pyc was compiled.  The second name is
             # __file__, which is where the .pyc was actually loaded from.  Since
             # .pyc files can be moved after compilation (for example, by being
             # installed), we look for __file__ in the frame and prefer it to the
             # co_filename value.
-            dunder_file = frame.f_globals and frame.f_globals.get('__file__')
+            dunder_file = frame.f_globals and frame.f_globals.get("__file__")
             if dunder_file:
                 filename = source_for_file(dunder_file)
-                if original_filename and not original_filename.startswith('<'):
+                if original_filename and not original_filename.startswith("<"):
                     orig = os.path.basename(original_filename)
                     if orig != os.path.basename(filename):
                         # Files shouldn't be renamed when moved. This happens when
                         # exec'ing code.  If it seems like something is wrong with
                         # the frame's file name, then just use the original.
                         filename = original_filename
 
         if not filename:
             # Empty string is pretty useless.
             return nope(disp, "empty string isn't a file name")
 
-        if filename.startswith('memory:'):
+        if filename.startswith("memory:"):
             return nope(disp, "memory isn't traceable")
 
-        if filename.startswith('<'):
+        if filename.startswith("<"):
             # Lots of non-file execution is represented with artificial
             # file names like "<string>", "<doctest readme.txt[0]>", or
             # "<exec_function>".  Don't ever trace these executions, since we
             # can't do anything with the data later anyway.
             return nope(disp, "file name is not real")
 
         canonical = canonical_filename(filename)
@@ -480,15 +480,15 @@
                     # shouldn't cause a warning, since it won't be the subject
                     # of tracing anyway.
                     continue
                 if disp.trace:
                     msg = f"Already imported a file that will be measured: {filename}"
                     self.warn(msg, slug="already-imported")
                     warned.add(filename)
-                elif self.debug and self.debug.should('trace'):
+                elif self.debug and self.debug.should("trace"):
                     self.debug.write(
                         "Didn't trace already imported file {!r}: {}".format(
                             disp.original_filename, disp.reason
                         )
                     )
 
     def warn_unimported_source(self) -> None:
@@ -576,21 +576,21 @@
             ("coverage_paths", self.cover_paths),
             ("stdlib_paths", self.pylib_paths),
             ("third_party_paths", self.third_paths),
             ("source_in_third_party_paths", self.source_in_third_paths),
         ]
 
         matcher_names = [
-            'source_match', 'source_pkgs_match',
-            'include_match', 'omit_match',
-            'cover_match', 'pylib_match', 'third_match', 'source_in_third_match',
+            "source_match", "source_pkgs_match",
+            "include_match", "omit_match",
+            "cover_match", "pylib_match", "third_match", "source_in_third_match",
         ]
 
         for matcher_name in matcher_names:
             matcher = getattr(self, matcher_name)
             if matcher:
                 matcher_info = matcher.info()
             else:
-                matcher_info = '-none-'
+                matcher_info = "-none-"
             info.append((matcher_name, matcher_info))
 
         return info
```

### Comparing `coverage-7.2.2/coverage/jsonreport.py` & `coverage-7.2.3/coverage/jsonreport.py`

 * *Files 6% similar despite different names*

```diff
@@ -56,28 +56,28 @@
                 coverage_data,
                 analysis
             )
 
         self.report_data["files"] = measured_files
 
         self.report_data["totals"] = {
-            'covered_lines': self.total.n_executed,
-            'num_statements': self.total.n_statements,
-            'percent_covered': self.total.pc_covered,
-            'percent_covered_display': self.total.pc_covered_str,
-            'missing_lines': self.total.n_missing,
-            'excluded_lines': self.total.n_excluded,
+            "covered_lines": self.total.n_executed,
+            "num_statements": self.total.n_statements,
+            "percent_covered": self.total.pc_covered,
+            "percent_covered_display": self.total.pc_covered_str,
+            "missing_lines": self.total.n_missing,
+            "excluded_lines": self.total.n_excluded,
         }
 
         if coverage_data.has_arcs():
             self.report_data["totals"].update({
-                'num_branches': self.total.n_branches,
-                'num_partial_branches': self.total.n_partial_branches,
-                'covered_branches': self.total.n_executed_branches,
-                'missing_branches': self.total.n_missing_branches,
+                "num_branches": self.total.n_branches,
+                "num_partial_branches": self.total.n_partial_branches,
+                "covered_branches": self.total.n_executed_branches,
+                "missing_branches": self.total.n_missing_branches,
             })
 
         json.dump(
             self.report_data,
             outfile,
             indent=(4 if self.config.json_pretty_print else None),
         )
@@ -85,40 +85,40 @@
         return self.total.n_statements and self.total.pc_covered
 
     def report_one_file(self, coverage_data: CoverageData, analysis: Analysis) -> Dict[str, Any]:
         """Extract the relevant report data for a single file."""
         nums = analysis.numbers
         self.total += nums
         summary = {
-            'covered_lines': nums.n_executed,
-            'num_statements': nums.n_statements,
-            'percent_covered': nums.pc_covered,
-            'percent_covered_display': nums.pc_covered_str,
-            'missing_lines': nums.n_missing,
-            'excluded_lines': nums.n_excluded,
+            "covered_lines": nums.n_executed,
+            "num_statements": nums.n_statements,
+            "percent_covered": nums.pc_covered,
+            "percent_covered_display": nums.pc_covered_str,
+            "missing_lines": nums.n_missing,
+            "excluded_lines": nums.n_excluded,
         }
         reported_file = {
-            'executed_lines': sorted(analysis.executed),
-            'summary': summary,
-            'missing_lines': sorted(analysis.missing),
-            'excluded_lines': sorted(analysis.excluded),
+            "executed_lines": sorted(analysis.executed),
+            "summary": summary,
+            "missing_lines": sorted(analysis.missing),
+            "excluded_lines": sorted(analysis.excluded),
         }
         if self.config.json_show_contexts:
-            reported_file['contexts'] = analysis.data.contexts_by_lineno(analysis.filename)
+            reported_file["contexts"] = analysis.data.contexts_by_lineno(analysis.filename)
         if coverage_data.has_arcs():
             summary.update({
-                'num_branches': nums.n_branches,
-                'num_partial_branches': nums.n_partial_branches,
-                'covered_branches': nums.n_executed_branches,
-                'missing_branches': nums.n_missing_branches,
+                "num_branches": nums.n_branches,
+                "num_partial_branches": nums.n_partial_branches,
+                "covered_branches": nums.n_executed_branches,
+                "missing_branches": nums.n_missing_branches,
             })
-            reported_file['executed_branches'] = list(
+            reported_file["executed_branches"] = list(
                 _convert_branch_arcs(analysis.executed_branch_arcs())
             )
-            reported_file['missing_branches'] = list(
+            reported_file["missing_branches"] = list(
                 _convert_branch_arcs(analysis.missing_branch_arcs())
             )
         return reported_file
 
 
 def _convert_branch_arcs(
     branch_arcs: Dict[TLineNo, List[TLineNo]],
```

### Comparing `coverage-7.2.2/coverage/lcovreport.py` & `coverage-7.2.3/coverage/lcovreport.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,15 @@
     def __init__(self, coverage: Coverage) -> None:
         self.coverage = coverage
         self.total = Numbers(self.coverage.config.precision)
 
     def report(self, morfs: Optional[Iterable[TMorf]], outfile: IO[str]) -> float:
         """Renders the full lcov report.
 
-        'morfs' is a list of modules or filenames
+        `morfs` is a list of modules or filenames
 
         outfile is the file object to write the file into.
         """
 
         self.coverage.get_data()
         outfile = outfile or sys.stdout
```

### Comparing `coverage-7.2.2/coverage/misc.py` & `coverage-7.2.3/coverage/misc.py`

 * *Files 0% similar despite different names*

```diff
@@ -214,22 +214,22 @@
         elif isinstance(v, dict):
             keys = v.keys()
             for k in sorted(keys):
                 self.update(k)
                 self.update(v[k])
         else:
             for k in dir(v):
-                if k.startswith('__'):
+                if k.startswith("__"):
                     continue
                 a = getattr(v, k)
                 if inspect.isroutine(a):
                     continue
                 self.update(k)
                 self.update(a)
-        self.hash.update(b'.')
+        self.hash.update(b".")
 
     def hexdigest(self) -> str:
         """Retrieve the hex digest of the hash."""
         return self.hash.hexdigest()[:32]
 
 
 def _needs_to_implement(that: Any, func_name: str) -> None:
@@ -288,50 +288,50 @@
                     (?P<strict>\?) |        # with a strict marker
                     -(?P<defval>[^}]*)      # or a default value
                 )?                      # maybe.
             }
         )
         """
 
-    dollar_groups = ('dollar', 'word1', 'word2')
+    dollar_groups = ("dollar", "word1", "word2")
 
     def dollar_replace(match: re.Match[str]) -> str:
         """Called for each $replacement."""
         # Only one of the dollar_groups will have matched, just get its text.
         word = next(g for g in match.group(*dollar_groups) if g)    # pragma: always breaks
         if word == "$":
             return "$"
         elif word in variables:
             return variables[word]
-        elif match['strict']:
+        elif match["strict"]:
             msg = f"Variable {word} is undefined: {text!r}"
             raise CoverageException(msg)
         else:
-            return match['defval']
+            return match["defval"]
 
     text = re.sub(dollar_pattern, dollar_replace, text)
     return text
 
 
 def format_local_datetime(dt: datetime.datetime) -> str:
     """Return a string with local timezone representing the date.
     """
-    return dt.astimezone().strftime('%Y-%m-%d %H:%M %z')
+    return dt.astimezone().strftime("%Y-%m-%d %H:%M %z")
 
 
 def import_local_file(modname: str, modfile: Optional[str] = None) -> ModuleType:
     """Import a local file as a module.
 
     Opens a file in the current directory named `modname`.py, imports it
     as `modname`, and returns the module object.  `modfile` is the file to
     import if it isn't in the current directory.
 
     """
     if modfile is None:
-        modfile = modname + '.py'
+        modfile = modname + ".py"
     spec = importlib.util.spec_from_file_location(modname, modfile)
     assert spec is not None
     mod = importlib.util.module_from_spec(spec)
     sys.modules[modname] = mod
     assert spec.loader is not None
     spec.loader.exec_module(mod)
```

### Comparing `coverage-7.2.2/coverage/multiproc.py` & `coverage-7.2.3/coverage/multiproc.py`

 * *Files 5% similar despite different names*

```diff
@@ -52,18 +52,18 @@
 
 class Stowaway:
     """An object to pickle, so when it is unpickled, it can apply the monkey-patch."""
     def __init__(self, rcfile: str) -> None:
         self.rcfile = rcfile
 
     def __getstate__(self) -> Dict[str, str]:
-        return {'rcfile': self.rcfile}
+        return {"rcfile": self.rcfile}
 
     def __setstate__(self, state: Dict[str, str]) -> None:
-        patch_multiprocessing(state['rcfile'])
+        patch_multiprocessing(state["rcfile"])
 
 
 def patch_multiprocessing(rcfile: str) -> None:
     """Monkey-patch the multiprocessing module.
 
     This enables coverage measurement of processes started by multiprocessing.
     This involves aggressive monkey-patching.
@@ -92,13 +92,13 @@
         original_get_preparation_data = spawn.get_preparation_data
     except (ImportError, AttributeError):
         pass
     else:
         def get_preparation_data_with_stowaway(name: str) -> Dict[str, Any]:
             """Get the original preparation data, and also insert our stowaway."""
             d = original_get_preparation_data(name)
-            d['stowaway'] = Stowaway(rcfile)
+            d["stowaway"] = Stowaway(rcfile)
             return d
 
         spawn.get_preparation_data = get_preparation_data_with_stowaway
 
     setattr(multiprocessing, PATCHED_MARKER, True)
```

### Comparing `coverage-7.2.2/coverage/numbits.py` & `coverage-7.2.3/coverage/numbits.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,15 +32,15 @@
     Returns:
         A binary blob.
     """
     try:
         nbytes = max(nums) // 8 + 1
     except ValueError:
         # nums was empty.
-        return b''
+        return b""
     b = bytearray(nbytes)
     for num in nums:
         b[num//8] |= 1 << num % 8
     return bytes(b)
 
 
 def numbits_to_nums(numbits: bytes) -> List[int]:
@@ -78,15 +78,15 @@
     """Compute the intersection of two numbits.
 
     Returns:
         A new numbits, the intersection `numbits1` and `numbits2`.
     """
     byte_pairs = zip_longest(numbits1, numbits2, fillvalue=0)
     intersection_bytes = bytes(b1 & b2 for b1, b2 in byte_pairs)
-    return intersection_bytes.rstrip(b'\0')
+    return intersection_bytes.rstrip(b"\0")
 
 
 def numbits_any_intersection(numbits1: bytes, numbits2: bytes) -> bool:
     """Is there any number that appears in both numbits?
 
     Determine whether two number sets have a non-empty intersection. This is
     faster than computing the intersection.
@@ -126,15 +126,15 @@
     object.  After creating the connection, pass it to this function to
     register the numbits functions.  Then you can use numbits functions in your
     queries::
 
         import sqlite3
         from coverage.numbits import register_sqlite_functions
 
-        conn = sqlite3.connect('example.db')
+        conn = sqlite3.connect("example.db")
         register_sqlite_functions(conn)
         c = conn.cursor()
         # Kind of a nonsense query:
         # Find all the files and contexts that executed line 47 in any file:
         c.execute(
             "select file_id, context_id from line_bits where num_in_numbits(?, numbits)",
             (47,)
```

### Comparing `coverage-7.2.2/coverage/parser.py` & `coverage-7.2.3/coverage/parser.py`

 * *Files 1% similar despite different names*

```diff
@@ -56,15 +56,15 @@
                 self.text = get_python_source(self.filename)
             except OSError as err:
                 raise NoSource(f"No source for code: '{self.filename}': {err}") from err
 
         self.exclude = exclude
 
         # The text lines of the parsed code.
-        self.lines: List[str] = self.text.split('\n')
+        self.lines: List[str] = self.text.split("\n")
 
         # The normalized line numbers of the statements in the code. Exclusions
         # are taken into account, and statements are adjusted to their first
         # lines.
         self.statements: Set[TLineNo] = set()
 
         # The normalized line numbers of the excluded lines in the code,
@@ -145,31 +145,31 @@
                     nice_pair((slineno, elineno)), ttext, ltext
                 ))
             if toktype == token.INDENT:
                 indent += 1
             elif toktype == token.DEDENT:
                 indent -= 1
             elif toktype == token.NAME:
-                if ttext == 'class':
+                if ttext == "class":
                     # Class definitions look like branches in the bytecode, so
                     # we need to exclude them.  The simplest way is to note the
-                    # lines with the 'class' keyword.
+                    # lines with the "class" keyword.
                     self.raw_classdefs.add(slineno)
             elif toktype == token.OP:
-                if ttext == ':' and nesting == 0:
+                if ttext == ":" and nesting == 0:
                     should_exclude = (elineno in self.raw_excluded) or excluding_decorators
                     if not excluding and should_exclude:
                         # Start excluding a suite.  We trigger off of the colon
                         # token so that the #pragma comment will be recognized on
                         # the same line as the colon.
                         self.raw_excluded.add(elineno)
                         exclude_indent = indent
                         excluding = True
                         excluding_decorators = False
-                elif ttext == '@' and first_on_line:
+                elif ttext == "@" and first_on_line:
                     # A decorator.
                     if elineno in self.raw_excluded:
                         excluding_decorators = True
                     if excluding_decorators:
                         self.raw_excluded.add(elineno)
                 elif ttext in "([{":
                     nesting += 1
@@ -759,15 +759,15 @@
     _line__ClassDef = _line_decorated
 
     def _line__Dict(self, node: ast.Dict) -> TLineNo:
         if node.keys:
             if node.keys[0] is not None:
                 return node.keys[0].lineno
             else:
-                # Unpacked dict literals `{**{'a':1}}` have None as the key,
+                # Unpacked dict literals `{**{"a":1}}` have None as the key,
                 # use the value in that case.
                 return node.values[0].lineno
         else:
             return node.lineno
 
     _line__FunctionDef = _line_decorated
     _line__AsyncFunctionDef = _line_decorated
```

### Comparing `coverage-7.2.2/coverage/phystokens.py` & `coverage-7.2.3/coverage/phystokens.py`

 * *Files 2% similar despite different names*

```diff
@@ -53,15 +53,15 @@
                 #
                 # so we need to figure out if the backslash is already in the
                 # string token or not.
                 inject_backslash = True
                 if last_ttext.endswith("\\"):
                     inject_backslash = False
                 elif ttype == token.STRING:
-                    if "\n" in ttext and ttext.split('\n', 1)[0][-1] == '\\':
+                    if "\n" in ttext and ttext.split("\n", 1)[0][-1] == "\\":
                         # It's a multi-line string and the first line ends with
                         # a backslash, so we don't need to inject another.
                         inject_backslash = False
                 if inject_backslash:
                     # Figure out what column the backslash is in.
                     ccol = len(last_line.split("\n")[-2]) - 1
                     # Yield the token, with a fake token type.
@@ -109,37 +109,37 @@
 
     """
 
     ws_tokens = {token.INDENT, token.DEDENT, token.NEWLINE, tokenize.NL}
     line: List[Tuple[str, str]] = []
     col = 0
 
-    source = source.expandtabs(8).replace('\r\n', '\n')
+    source = source.expandtabs(8).replace("\r\n", "\n")
     tokgen = generate_tokens(source)
 
     if env.PYBEHAVIOR.soft_keywords:
         match_case_lines = MatchCaseFinder(source).match_case_lines
 
     for ttype, ttext, (sline, scol), (_, ecol), _ in _phys_tokens(tokgen):
         mark_start = True
-        for part in re.split('(\n)', ttext):
-            if part == '\n':
+        for part in re.split("(\n)", ttext):
+            if part == "\n":
                 yield line
                 line = []
                 col = 0
                 mark_end = False
-            elif part == '':
+            elif part == "":
                 mark_end = False
             elif ttype in ws_tokens:
                 mark_end = False
             else:
                 if mark_start and scol > col:
                     line.append(("ws", " " * (scol - col)))
                     mark_start = False
-                tok_class = tokenize.tok_name.get(ttype, 'xx').lower()[:3]
+                tok_class = tokenize.tok_name.get(ttype, "xx").lower()[:3]
                 if ttype == token.NAME:
                     if keyword.iskeyword(ttext):
                         # Hard keywords are always keywords.
                         tok_class = "key"
                     elif sys.version_info >= (3, 10):   # PYVERSIONS
                         # Need the version_info check to keep mypy from borking
                         # on issoftkeyword here.
```

### Comparing `coverage-7.2.2/coverage/plugin.py` & `coverage-7.2.3/coverage/plugin.py`

 * *Files 2% similar despite different names*

```diff
@@ -515,37 +515,37 @@
     def source_token_lines(self) -> TSourceTokenLines:
         """Generate a series of tokenized lines, one for each line in `source`.
 
         These tokens are used for syntax-colored reports.
 
         Each line is a list of pairs, each pair is a token::
 
-            [('key', 'def'), ('ws', ' '), ('nam', 'hello'), ('op', '('), ... ]
+            [("key", "def"), ("ws", " "), ("nam", "hello"), ("op", "("), ... ]
 
         Each pair has a token class, and the token text.  The token classes
         are:
 
-        * ``'com'``: a comment
-        * ``'key'``: a keyword
-        * ``'nam'``: a name, or identifier
-        * ``'num'``: a number
-        * ``'op'``: an operator
-        * ``'str'``: a string literal
-        * ``'ws'``: some white space
-        * ``'txt'``: some other kind of text
+        * ``"com"``: a comment
+        * ``"key"``: a keyword
+        * ``"nam"``: a name, or identifier
+        * ``"num"``: a number
+        * ``"op"``: an operator
+        * ``"str"``: a string literal
+        * ``"ws"``: some white space
+        * ``"txt"``: some other kind of text
 
         If you concatenate all the token texts, and then join them with
         newlines, you should have your original source back.
 
         The default implementation simply returns each line tagged as
-        ``'txt'``.
+        ``"txt"``.
 
         """
         for line in self.source().splitlines():
-            yield [('txt', line)]
+            yield [("txt", line)]
 
     def __eq__(self, other: Any) -> bool:
         return isinstance(other, FileReporter) and self.filename == other.filename
 
     def __lt__(self, other: Any) -> bool:
         return isinstance(other, FileReporter) and self.filename < other.filename
```

### Comparing `coverage-7.2.2/coverage/plugin_support.py` & `coverage-7.2.3/coverage/plugin_support.py`

 * *Files 1% similar despite different names*

```diff
@@ -110,15 +110,15 @@
         """Add a plugin object.
 
         `plugin` is a :class:`CoveragePlugin` instance to add.  `specialized`
         is a list to append the plugin to.
 
         """
         plugin_name = f"{self.current_module}.{plugin.__class__.__name__}"
-        if self.debug and self.debug.should('plugin'):
+        if self.debug and self.debug.should("plugin"):
             self.debug.write(f"Loaded plugin {self.current_module!r}: {plugin!r}")
             labelled = LabelledDebug(f"plugin {self.current_module!r}", self.debug)
             plugin = DebugPluginWrapper(plugin, labelled)
 
         plugin._coverage_plugin_name = plugin_name
         plugin._coverage_enabled = True
         self.order.append(plugin)
@@ -146,15 +146,15 @@
 
     def add_label(self, label: str) -> LabelledDebug:
         """Add a label to the writer, and return a new `LabelledDebug`."""
         return LabelledDebug(label, self.debug, self.labels)
 
     def message_prefix(self) -> str:
         """The prefix to use on messages, combining the labels."""
-        prefixes = self.labels + ['']
+        prefixes = self.labels + [""]
         return ":\n".join("  "*i+label for i, label in enumerate(prefixes))
 
     def write(self, message: str) -> None:
         """Write `message`, but with the labels prepended."""
         self.debug.write(f"{self.message_prefix()}{message}")
```

### Comparing `coverage-7.2.2/coverage/python.py` & `coverage-7.2.3/coverage/python.py`

 * *Files 2% similar despite different names*

```diff
@@ -59,20 +59,20 @@
         if source_bytes is not None:
             break
     else:
         # Couldn't find source.
         raise NoSource(f"No source for code: '{filename}'.")
 
     # Replace \f because of http://bugs.python.org/issue19035
-    source_bytes = source_bytes.replace(b'\f', b' ')
+    source_bytes = source_bytes.replace(b"\f", b" ")
     source = source_bytes.decode(source_encoding(source_bytes), "replace")
 
     # Python code should always end with a line with a newline.
-    if source and source[-1] != '\n':
-        source += '\n'
+    if source and source[-1] != "\n":
+        source += "\n"
 
     return source
 
 
 def get_zip_bytes(filename: str) -> Optional[bytes]:
     """Get data from `filename` if it is a zip file path.
 
@@ -123,15 +123,15 @@
 
     # No idea, just use the file name as-is.
     return filename
 
 
 def source_for_morf(morf: TMorf) -> str:
     """Get the source filename for the module-or-file `morf`."""
-    if hasattr(morf, '__file__') and morf.__file__:
+    if hasattr(morf, "__file__") and morf.__file__:
         filename = morf.__file__
     elif isinstance(morf, types.ModuleType):
         # A module should have had .__file__, otherwise we can't use it.
         # This could be a PEP-420 namespace package.
         raise CoverageException(f"Module {morf} has no file")
     else:
         filename = morf
@@ -153,17 +153,17 @@
         if self.coverage is not None:
             if self.coverage.config.relative_files:
                 canonicalize = False
         if canonicalize:
             fname = canonical_filename(filename)
         super().__init__(fname)
 
-        if hasattr(morf, '__name__'):
+        if hasattr(morf, "__name__"):
             name = morf.__name__.replace(".", os.sep)
-            if os.path.basename(filename).startswith('__init__.'):
+            if os.path.basename(filename).startswith("__init__."):
                 name += os.sep + "__init__"
             name += ".py"
         else:
             name = relative_filename(filename)
         self.relname = name
 
         self._source: Optional[str] = None
@@ -179,15 +179,15 @@
     @property
     def parser(self) -> PythonParser:
         """Lazily create a :class:`PythonParser`."""
         assert self.coverage is not None
         if self._parser is None:
             self._parser = PythonParser(
                 filename=self.filename,
-                exclude=self.coverage._exclude_regex('exclude'),
+                exclude=self.coverage._exclude_regex("exclude"),
             )
             self._parser.parse_source()
         return self._parser
 
     def lines(self) -> Set[TLineNo]:
         """Return the line numbers of statements in the file."""
         return self.parser.statements
@@ -240,15 +240,15 @@
         place.
 
         """
         # Get the file extension.
         _, ext = os.path.splitext(self.filename)
 
         # Anything named *.py* should be Python.
-        if ext.startswith('.py'):
+        if ext.startswith(".py"):
             return True
         # A file with no extension should be Python.
         if not ext:
             return True
         # Everything else is probably not Python.
         return False
```

### Comparing `coverage-7.2.2/coverage/pytracer.py` & `coverage-7.2.3/coverage/pytracer.py`

 * *Files 2% similar despite different names*

```diff
@@ -16,19 +16,19 @@
 from coverage import env
 from coverage.types import (
     TArc, TFileDisposition, TLineNo, TTraceData, TTraceFileData, TTraceFn,
     TTracer, TWarnFn,
 )
 
 # We need the YIELD_VALUE opcode below, in a comparison-friendly form.
-RESUME = dis.opmap.get('RESUME')
-RETURN_VALUE = dis.opmap['RETURN_VALUE']
+RESUME = dis.opmap.get("RESUME")
+RETURN_VALUE = dis.opmap["RETURN_VALUE"]
 if RESUME is None:
-    YIELD_VALUE = dis.opmap['YIELD_VALUE']
-    YIELD_FROM = dis.opmap['YIELD_FROM']
+    YIELD_VALUE = dis.opmap["YIELD_VALUE"]
+    YIELD_FROM = dis.opmap["YIELD_FROM"]
     YIELD_FROM_OFFSET = 0 if env.PYPY else 2
 
 # When running meta-coverage, this file can try to trace itself, which confuses
 # everything.  Don't trace ourselves.
 
 THIS_FILE = __file__.rstrip("co")
 
@@ -74,15 +74,15 @@
         self.data_stack: List[Tuple[Optional[TTraceFileData], Optional[str], TLineNo, bool]] = []
         self.thread: Optional[threading.Thread] = None
         self.stopped = False
         self._activity = False
 
         self.in_atexit = False
         # On exit, self.in_atexit = True
-        atexit.register(setattr, self, 'in_atexit', True)
+        atexit.register(setattr, self, "in_atexit", True)
 
         # Cache a bound method on the instance, so that we don't have to
         # re-create a bound method object all the time.
         self._cached_bound_method_trace: TTraceFn = self._trace
 
     def __repr__(self) -> str:
         me = id(self)
@@ -146,18 +146,18 @@
                     "Empty stack!",
                     frame.f_code.co_filename,
                     frame.f_lineno,
                     frame.f_code.co_name
                 )
             return None
 
-        # if event != 'call' and frame.f_code.co_filename != self.cur_file_name:
+        # if event != "call" and frame.f_code.co_filename != self.cur_file_name:
         #     self.log("---\n*", frame.f_code.co_filename, self.cur_file_name, frame.f_lineno)
 
-        if event == 'call':
+        if event == "call":
             # Should we start a new context?
             if self.should_start_context and self.context is None:
                 context_maybe = self.should_start_context(frame)
                 if context_maybe is not None:
                     self.context = context_maybe
                     started_context = True
                     assert self.switch_context is not None
@@ -211,32 +211,32 @@
             # line number for calls, and the real line number for generators.
             if RESUME is not None:
                 # The current opcode is guaranteed to be RESUME. The argument
                 # determines what kind of resume it is.
                 oparg = frame.f_code.co_code[frame.f_lasti + 1]
                 real_call = (oparg == 0)
             else:
-                real_call = (getattr(frame, 'f_lasti', -1) < 0)
+                real_call = (getattr(frame, "f_lasti", -1) < 0)
             if real_call:
                 self.last_line = -frame.f_code.co_firstlineno
             else:
                 self.last_line = frame.f_lineno
 
-        elif event == 'line':
+        elif event == "line":
             # Record an executed line.
             if self.cur_file_data is not None:
                 flineno: TLineNo = frame.f_lineno
 
                 if self.trace_arcs:
                     cast(Set[TArc], self.cur_file_data).add((self.last_line, flineno))
                 else:
                     cast(Set[TLineNo], self.cur_file_data).add(flineno)
                 self.last_line = flineno
 
-        elif event == 'return':
+        elif event == "return":
             if self.trace_arcs and self.cur_file_data:
                 # Record an arc leaving the function, but beware that a
                 # "return" event might just mean yielding from a generator.
                 code = frame.f_code.co_code
                 lasti = frame.f_lasti
                 if RESUME is not None:
                     if len(code) == lasti + 2:
```

### Comparing `coverage-7.2.2/coverage/report.py` & `coverage-7.2.3/coverage/report.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/results.py` & `coverage-7.2.3/coverage/results.py`

 * *Files 0% similar despite different names*

```diff
@@ -353,15 +353,15 @@
         line_exits = sorted(arcs)
         for line, exits in line_exits:
             for ex in sorted(exits):
                 if line not in lines and ex not in lines:
                     dest = (ex if ex > 0 else "exit")
                     line_items.append((line, f"{line}->{dest}"))
 
-    ret = ', '.join(t[-1] for t in sorted(line_items))
+    ret = ", ".join(t[-1] for t in sorted(line_items))
     return ret
 
 
 def should_fail_under(total: float, fail_under: float, precision: int) -> bool:
     """Determine if a total should fail due to fail-under.
 
     `total` is a float, the coverage measurement total. `fail_under` is the
```

### Comparing `coverage-7.2.2/coverage/sqldata.py` & `coverage-7.2.3/coverage/sqldata.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/summary.py` & `coverage-7.2.3/coverage/summary.py`

 * *Files 4% similar despite different names*

```diff
@@ -133,16 +133,16 @@
             BrPart="{:>9} |",
             Cover="{:>{n}} |",
             Missing="{:>10} |",
         )
         max_n = max(len(total_line[header.index("Cover")]) + 6, len(" Cover "))
         header_items = [formats[item].format(item, name_len=max_name, n=max_n) for item in header]
         header_str = "".join(header_items)
-        rule_str = "|" + " ".join(["- |".rjust(len(header_items[0])-1, '-')] +
-            ["-: |".rjust(len(item)-1, '-') for item in header_items[1:]]
+        rule_str = "|" + " ".join(["- |".rjust(len(header_items[0])-1, "-")] +
+            ["-: |".rjust(len(item)-1, "-") for item in header_items[1:]]
         )
 
         # Write the header
         self.write(header_str)
         self.write(rule_str)
 
         for values in lines_values:
@@ -219,18 +219,18 @@
                 args += [analysis.missing_formatted(branches=True)]
             args += [nums.pc_covered]
             lines_values.append(args)
 
         # Line sorting.
         sort_option = (self.config.sort or "name").lower()
         reverse = False
-        if sort_option[0] == '-':
+        if sort_option[0] == "-":
             reverse = True
             sort_option = sort_option[1:]
-        elif sort_option[0] == '+':
+        elif sort_option[0] == "+":
             sort_option = sort_option[1:]
         sort_idx = column_order.get(sort_option)
         if sort_idx is None:
             raise ConfigError(f"Invalid sorting option: {self.config.sort!r}")
         if sort_option == "name":
             lines_values = human_sorted_items(lines_values, reverse=reverse)
         else:
@@ -246,20 +246,20 @@
         total_line += [self.total.pc_covered_str]
         if self.config.show_missing:
             total_line += [""]
 
         # Create other final lines.
         end_lines = []
         if self.config.skip_covered and self.skipped_count:
-            file_suffix = 's' if self.skipped_count>1 else ''
+            file_suffix = "s" if self.skipped_count>1 else ""
             end_lines.append(
                 f"\n{self.skipped_count} file{file_suffix} skipped due to complete coverage."
             )
         if self.config.skip_empty and self.empty_count:
-            file_suffix = 's' if self.empty_count > 1 else ''
+            file_suffix = "s" if self.empty_count > 1 else ""
             end_lines.append(f"\n{self.empty_count} empty file{file_suffix} skipped.")
 
         if self.output_format == "markdown":
             formatter = self._report_markdown
         else:
             formatter = self._report_text
         formatter(header, lines_values, total_line, end_lines)
```

### Comparing `coverage-7.2.2/coverage/templite.py` & `coverage-7.2.3/coverage/templite.py`

 * *Files 6% similar despite different names*

```diff
@@ -105,19 +105,19 @@
 
         templite = Templite('''
             <h1>Hello {{name|upper}}!</h1>
             {% for topic in topics %}
                 <p>You are interested in {{topic}}.</p>
             {% endif %}
             ''',
-            {'upper': str.upper},
+            {"upper": str.upper},
         )
         text = templite.render({
-            'name': "Ned",
-            'topics': ['Python', 'Geometry', 'Juggling'],
+            "name": "Ned",
+            "topics": ["Python", "Geometry", "Juggling"],
         })
 
     """
     def __init__(self, text: str, *contexts: Dict[str, Any]) -> None:
         """Construct a Templite with the given `text`.
 
         `contexts` are dictionaries of values to use for future renderings.
@@ -157,67 +157,67 @@
 
         # Split the text to form a list of tokens.
         tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
 
         squash = in_joined = False
 
         for token in tokens:
-            if token.startswith('{'):
+            if token.startswith("{"):
                 start, end = 2, -2
-                squash = (token[-3] == '-')
+                squash = (token[-3] == "-")
                 if squash:
                     end = -3
 
-                if token.startswith('{#'):
+                if token.startswith("{#"):
                     # Comment: ignore it and move on.
                     continue
-                elif token.startswith('{{'):
+                elif token.startswith("{{"):
                     # An expression to evaluate.
                     expr = self._expr_code(token[start:end].strip())
                     buffered.append("to_str(%s)" % expr)
                 else:
-                    # token.startswith('{%')
+                    # token.startswith("{%")
                     # Action tag: split into words and parse further.
                     flush_output()
 
                     words = token[start:end].strip().split()
-                    if words[0] == 'if':
+                    if words[0] == "if":
                         # An if statement: evaluate the expression to determine if.
                         if len(words) != 2:
                             self._syntax_error("Don't understand if", token)
-                        ops_stack.append('if')
+                        ops_stack.append("if")
                         code.add_line("if %s:" % self._expr_code(words[1]))
                         code.indent()
-                    elif words[0] == 'for':
+                    elif words[0] == "for":
                         # A loop: iterate over expression result.
-                        if len(words) != 4 or words[2] != 'in':
+                        if len(words) != 4 or words[2] != "in":
                             self._syntax_error("Don't understand for", token)
-                        ops_stack.append('for')
+                        ops_stack.append("for")
                         self._variable(words[1], self.loop_vars)
                         code.add_line(
                             "for c_{} in {}:".format(
                                 words[1],
                                 self._expr_code(words[3])
                             )
                         )
                         code.indent()
-                    elif words[0] == 'joined':
-                        ops_stack.append('joined')
+                    elif words[0] == "joined":
+                        ops_stack.append("joined")
                         in_joined = True
-                    elif words[0].startswith('end'):
+                    elif words[0].startswith("end"):
                         # Endsomething.  Pop the ops stack.
                         if len(words) != 1:
                             self._syntax_error("Don't understand end", token)
                         end_what = words[0][3:]
                         if not ops_stack:
                             self._syntax_error("Too many ends", token)
                         start_what = ops_stack.pop()
                         if start_what != end_what:
                             self._syntax_error("Mismatched end tag", end_what)
-                        if end_what == 'joined':
+                        if end_what == "joined":
                             in_joined = False
                         else:
                             code.dedent()
                     else:
                         self._syntax_error("Don't understand tag", words[0])
             else:
                 # Literal content.  If it isn't empty, output it.
@@ -232,22 +232,22 @@
             self._syntax_error("Unmatched action tag", ops_stack[-1])
 
         flush_output()
 
         for var_name in self.all_vars - self.loop_vars:
             vars_code.add_line(f"c_{var_name} = context[{var_name!r}]")
 
-        code.add_line('return "".join(result)')
+        code.add_line("return ''.join(result)")
         code.dedent()
         self._render_function = cast(
             Callable[
                 [Dict[str, Any], Callable[..., Any]],
                 str
             ],
-            code.get_globals()['render_function'],
+            code.get_globals()["render_function"],
         )
 
     def _expr_code(self, expr: str) -> str:
         """Generate a Python expression for `expr`."""
         if "|" in expr:
             pipes = expr.split("|")
             code = self._expr_code(pipes[0])
```

### Comparing `coverage-7.2.2/coverage/tomlconfig.py` & `coverage-7.2.3/coverage/tomlconfig.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/tracer.pyi` & `coverage-7.2.3/coverage/tracer.pyi`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/types.py` & `coverage-7.2.3/coverage/types.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/coverage/version.py` & `coverage-7.2.3/coverage/version.py`

 * *Files 12% similar despite different names*

```diff
@@ -4,31 +4,31 @@
 """The version and URL for coverage.py"""
 # This file is exec'ed in setup.py, don't import anything!
 
 from __future__ import annotations
 
 # version_info: same semantics as sys.version_info.
 # _dev: the .devN suffix if any.
-version_info = (7, 2, 2, "final", 0)
+version_info = (7, 2, 3, "final", 0)
 _dev = 0
 
 
 def _make_version(
     major: int,
     minor: int,
     micro: int,
     releaselevel: str = "final",
     serial: int = 0,
     dev: int = 0,
 ) -> str:
     """Create a readable version string from version_info tuple components."""
-    assert releaselevel in ['alpha', 'beta', 'candidate', 'final']
+    assert releaselevel in ["alpha", "beta", "candidate", "final"]
     version = "%d.%d.%d" % (major, minor, micro)
-    if releaselevel != 'final':
-        short = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc'}[releaselevel]
+    if releaselevel != "final":
+        short = {"alpha": "a", "beta": "b", "candidate": "rc"}[releaselevel]
         version += f"{short}{serial}"
     if dev != 0:
         version += f".dev{dev}"
     return version
 
 
 def _make_url(
```

### Comparing `coverage-7.2.2/coverage/xmlreport.py` & `coverage-7.2.3/coverage/xmlreport.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 
 if TYPE_CHECKING:
     from coverage import Coverage
 
 os = isolate_module(os)
 
 
-DTD_URL = 'https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd'
+DTD_URL = "https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd"
 
 
 def rate(hit: int, num: int) -> str:
     """Return the fraction of `hit`/`num`, as a string."""
     if num == 0:
         return "1"
     else:
@@ -123,15 +123,15 @@
         for pkg_name, pkg_data in human_sorted_items(self.packages.items()):
             xpackage = self.xml_out.createElement("package")
             appendChild(xpackages, xpackage)
             xclasses = self.xml_out.createElement("classes")
             appendChild(xpackage, xclasses)
             for _, class_elt in human_sorted_items(pkg_data.elements.items()):
                 appendChild(xclasses, class_elt)
-            xpackage.setAttribute("name", pkg_name.replace(os.sep, '.'))
+            xpackage.setAttribute("name", pkg_name.replace(os.sep, "."))
             xpackage.setAttribute("line-rate", rate(pkg_data.hits, pkg_data.lines))
             if has_arcs:
                 branch_rate = rate(pkg_data.br_hits, pkg_data.branches)
             else:
                 branch_rate = "0"
             xpackage.setAttribute("branch-rate", branch_rate)
             xpackage.setAttribute("complexity", "0")
@@ -168,15 +168,15 @@
     def xml_file(self, fr: FileReporter, analysis: Analysis, has_arcs: bool) -> None:
         """Add to the XML report for a single file."""
 
         if self.config.skip_empty:
             if analysis.numbers.n_statements == 0:
                 return
 
-        # Create the 'lines' and 'package' XML elements, which
+        # Create the "lines" and "package" XML elements, which
         # are populated later.  Note that a package == a directory.
         filename = fr.filename.replace("\\", "/")
         for source_path in self.source_paths:
             if not self.config.relative_files:
                 source_path = files.canonical_filename(source_path)
             if filename.startswith(source_path.replace("\\", "/") + "/"):
                 rel_name = filename[len(source_path)+1:]
@@ -201,15 +201,15 @@
         xclass.setAttribute("name", os.path.relpath(rel_name, dirname))
         xclass.setAttribute("filename", rel_name.replace("\\", "/"))
         xclass.setAttribute("complexity", "0")
 
         branch_stats = analysis.branch_stats()
         missing_branch_arcs = analysis.missing_branch_arcs()
 
-        # For each statement, create an XML 'line' element.
+        # For each statement, create an XML "line" element.
         for line in sorted(analysis.statements):
             xline = self.xml_out.createElement("line")
             xline.setAttribute("number", str(line))
 
             # Q: can we get info about the number of times a statement is
             # executed?  If so, that should be recorded here.
             xline.setAttribute("hits", str(int(line not in analysis.missing)))
```

### Comparing `coverage-7.2.2/coverage.egg-info/PKG-INFO` & `coverage-7.2.3/coverage.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: coverage
-Version: 7.2.2
+Version: 7.2.3
 Summary: Code coverage measurement for Python
 Home-page: https://github.com/nedbat/coveragepy
-Author: Ned Batchelder and 172 others
+Author: Ned Batchelder and 178 others
 Author-email: ned@nedbatchelder.com
 License: Apache-2.0
-Project-URL: Documentation, https://coverage.readthedocs.io/en/7.2.2
+Project-URL: Documentation, https://coverage.readthedocs.io/en/7.2.3
 Project-URL: Funding, https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=pypi
 Project-URL: Issues, https://github.com/nedbat/coveragepy/issues
 Project-URL: Mastodon, https://hachyderm.io/@coveragepy
 Project-URL: Mastodon (nedbat), https://hachyderm.io/@nedbat
 Keywords: code coverage testing
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
@@ -60,21 +60,21 @@
 the code analysis tools and tracing hooks provided in the Python standard
 library to determine which lines are executable, and which have been executed.
 
 Coverage.py runs on these versions of Python:
 
 .. PYVERSIONS
 
-* CPython 3.7 through 3.12.0a6
+* CPython 3.7 through 3.12.0a7
 * PyPy3 7.3.11.
 
 Documentation is on `Read the Docs`_.  Code repository and issue tracker are on
 `GitHub`_.
 
-.. _Read the Docs: https://coverage.readthedocs.io/en/7.2.2/
+.. _Read the Docs: https://coverage.readthedocs.io/en/7.2.3/
 .. _GitHub: https://github.com/nedbat/coveragepy
 
 **New in 7.x:**
 improved data combining;
 ``report --format=``;
 type annotations.
 
@@ -102,25 +102,26 @@
        of commercial-grade software, this is for you.
        `Learn more. <https://tidelift.com/subscription/pkg/pypi-coverage?utm_source=pypi-coverage&utm_medium=referral&utm_campaign=readme>`_
 
 
 Getting Started
 ---------------
 
-See the `Quick Start section`_ of the docs.
+Looking to run ``coverage`` on your test suite? See the `Quick Start section`_
+of the docs.
 
-.. _Quick Start section: https://coverage.readthedocs.io/en/7.2.2/#quick-start
+.. _Quick Start section: https://coverage.readthedocs.io/en/7.2.3/#quick-start
 
 
 Change history
 --------------
 
 The complete history of changes is on the `change history page`_.
 
-.. _change history page: https://coverage.readthedocs.io/en/7.2.2/changes.html
+.. _change history page: https://coverage.readthedocs.io/en/7.2.3/changes.html
 
 
 Code of Conduct
 ---------------
 
 Everyone participating in the coverage.py project is expected to treat other
 people with respect and to follow the guidelines articulated in the `Python
@@ -128,17 +129,18 @@
 
 .. _Python Community Code of Conduct: https://www.python.org/psf/codeofconduct/
 
 
 Contributing
 ------------
 
-See the `Contributing section`_ of the docs.
+Found a bug? Want to help improve the code or documentation? See the
+`Contributing section`_ of the docs.
 
-.. _Contributing section: https://coverage.readthedocs.io/en/7.2.2/contributing.html
+.. _Contributing section: https://coverage.readthedocs.io/en/7.2.3/contributing.html
 
 
 Security
 --------
 
 To report a security vulnerability, please use the `Tidelift security
 contact`_.  Tidelift will coordinate the fix and disclosure.
@@ -158,15 +160,15 @@
 .. |test-status| image:: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml/badge.svg?branch=master&event=push
     :target: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml
     :alt: Test suite status
 .. |quality-status| image:: https://github.com/nedbat/coveragepy/actions/workflows/quality.yml/badge.svg?branch=master&event=push
     :target: https://github.com/nedbat/coveragepy/actions/workflows/quality.yml
     :alt: Quality check status
 .. |docs| image:: https://readthedocs.org/projects/coverage/badge/?version=latest&style=flat
-    :target: https://coverage.readthedocs.io/en/7.2.2/
+    :target: https://coverage.readthedocs.io/en/7.2.3/
     :alt: Documentation
 .. |kit| image:: https://badge.fury.io/py/coverage.svg
     :target: https://pypi.org/project/coverage/
     :alt: PyPI status
 .. |format| image:: https://img.shields.io/pypi/format/coverage.svg
     :target: https://pypi.org/project/coverage/
     :alt: Kit format
```

### Comparing `coverage-7.2.2/coverage.egg-info/SOURCES.txt` & `coverage-7.2.3/coverage.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -251,14 +251,16 @@
 tests/gold/html/Makefile
 tests/gold/html/a/a_py.html
 tests/gold/html/a/index.html
 tests/gold/html/b_branch/b_py.html
 tests/gold/html/b_branch/index.html
 tests/gold/html/bom/bom_py.html
 tests/gold/html/bom/index.html
+tests/gold/html/contexts/index.html
+tests/gold/html/contexts/two_tests_py.html
 tests/gold/html/isolatin1/index.html
 tests/gold/html/isolatin1/isolatin1_py.html
 tests/gold/html/omit_1/index.html
 tests/gold/html/omit_1/m1_py.html
 tests/gold/html/omit_1/m2_py.html
 tests/gold/html/omit_1/m3_py.html
 tests/gold/html/omit_1/main_py.html
```

### Comparing `coverage-7.2.2/doc/_static/coverage.css` & `coverage-7.2.3/doc/_static/coverage.css`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/api.rst` & `coverage-7.2.3/doc/api.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/api_module.rst` & `coverage-7.2.3/doc/api_module.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/api_plugin.rst` & `coverage-7.2.3/doc/api_plugin.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/branch.rst` & `coverage-7.2.3/doc/branch.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/changes.rst` & `coverage-7.2.3/doc/changes.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/cmd.rst` & `coverage-7.2.3/doc/cmd.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/conf.py` & `coverage-7.2.3/doc/conf.py`

 * *Files 3% similar despite different names*

```diff
@@ -32,15 +32,14 @@
 
 # Add any Sphinx extension module names here, as strings. They can be extensions
 # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
 extensions = [
     'sphinx.ext.autodoc',
     'sphinx.ext.todo',
     'sphinx.ext.ifconfig',
-    'sphinxcontrib.spelling',
     'sphinx.ext.intersphinx',
     'sphinxcontrib.restbuilder',
     'sphinx.ext.napoleon',
     #'sphinx_tabs.tabs',
 ]
 
 autodoc_typehints = "description"
@@ -63,19 +62,19 @@
 # The version info for the project you're documenting, acts as replacement for
 # |version| and |release|, also used in various other places throughout the
 # built documents.
 
 # @@@ editable
 copyright = "2009–2023, Ned Batchelder" # pylint: disable=redefined-builtin
 # The short X.Y.Z version.
-version = "7.2.2"
+version = "7.2.3"
 # The full version, including alpha/beta/rc tags.
-release = "7.2.2"
+release = "7.2.3"
 # The date of release, in "monthname day, year" format.
-release_date = "March 16, 2023"
+release_date = "April 6, 2023"
 # @@@ end
 
 rst_epilog = """
 .. |release_date| replace:: {release_date}
 .. |coverage-equals-release| replace:: coverage=={release}
 .. |doc-url| replace:: https://coverage.readthedocs.io/en/{release}
 .. |br| raw:: html
@@ -216,14 +215,17 @@
 
 # Output file base name for HTML help builder.
 htmlhelp_basename = 'coveragepydoc'
 
 # -- Spelling ---
 
 if any("spell" in arg for arg in sys.argv):
+    # sphinxcontrib.spelling needs the native "enchant" library, which often is
+    # missing, so only use the extension if we are specifically spell-checking.
+    extensions += ['sphinxcontrib.spelling']
     names_file = tempfile.NamedTemporaryFile(mode='w', prefix="coverage_names_", suffix=".txt")
     with open("../CONTRIBUTORS.txt") as contributors:
         names = set(re.split(r"[^\w']", contributors.read()))
         names = [n for n in names if len(n) >= 2 and n[0].isupper()]
         names_file.write("\n".join(names))
         names_file.flush()
     atexit.register(os.remove, names_file.name)
```

### Comparing `coverage-7.2.2/doc/config.rst` & `coverage-7.2.3/doc/config.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/contexts.rst` & `coverage-7.2.3/doc/contexts.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/contributing.rst` & `coverage-7.2.3/doc/contributing.rst`

 * *Files 23% similar despite different names*

```diff
@@ -33,95 +33,125 @@
 Getting the code
 ----------------
 
 The coverage.py code is hosted on a GitHub repository at
 https://github.com/nedbat/coveragepy.  To get a working environment, follow
 these steps:
 
-.. minimum of PYVERSIONS:
+#.  `Fork the repo`_ into your own GitHub account.  The coverage.py code will
+    then be copied into a GitHub repository at
+    ``https://github.com/GITHUB_USER/coveragepy`` where GITHUB_USER is your
+    GitHub username.
 
-#.  Create a Python 3.7 virtualenv to work in, and activate it.
+#.  (Optional) Create a virtualenv to work in, and activate it.  There
+    are a number of ways to do this.  Use the method you are comfortable with.
 
 #.  Clone the repository::
 
-    $ git clone https://github.com/nedbat/coveragepy
+    $ git clone https://github.com/GITHUB_USER/coveragepy
     $ cd coveragepy
 
 #.  Install the requirements::
 
-    $ python3 -m pip install -r requirements/dev.pip
-
-    If this fails due to incorrect or missing hashes, use
-    ``dev.in`` instead::
-
     $ python3 -m pip install -r requirements/dev.in
 
-#.  Install a number of versions of Python.  Coverage.py supports a range
-    of Python versions.  The more you can test with, the more easily your code
-    can be used as-is.  If you only have one version, that's OK too, but may
-    mean more work integrating your contribution.
+    Note: You may need to upgrade pip to install the requirements.
 
 
 Running the tests
 -----------------
 
 The tests are written mostly as standard unittest-style tests, and are run with
 pytest running under `tox`_::
 
-    $ tox
-    py37 create: /Users/nedbat/coverage/trunk/.tox/py37
-    py37 installdeps: -rrequirements/pip.pip, -rrequirements/pytest.pip, eventlet==0.25.1, greenlet==0.4.15
-    py37 develop-inst: /Users/nedbat/coverage/trunk
-    py37 installed: apipkg==1.5,appdirs==1.4.4,attrs==20.3.0,backports.functools-lru-cache==1.6.4,-e git+git@github.com:nedbat/coveragepy.git@36ef0e03c0439159c2245d38de70734fa08cddb4#egg=coverage,decorator==5.0.7,distlib==0.3.1,dnspython==2.1.0,eventlet==0.25.1,execnet==1.8.0,filelock==3.0.12,flaky==3.7.0,future==0.18.2,greenlet==0.4.15,hypothesis==6.10.1,importlib-metadata==4.0.1,iniconfig==1.1.1,monotonic==1.6,packaging==20.9,pluggy==0.13.1,py==1.10.0,PyContracts @ git+https://github.com/slorg1/contracts@c5a6da27d4dc9985f68e574d20d86000880919c3,pyparsing==2.4.7,pytest==6.2.3,pytest-forked==1.3.0,pytest-xdist==2.2.1,qualname==0.1.0,six==1.15.0,sortedcontainers==2.3.0,toml==0.10.2,typing-extensions==3.10.0.0,virtualenv==20.4.4,zipp==3.4.1
-    py37 run-test-pre: PYTHONHASHSEED='376882681'
-    py37 run-test: commands[0] | python setup.py --quiet clean develop
-    py37 run-test: commands[1] | python igor.py zip_mods remove_extension
-    py37 run-test: commands[2] | python igor.py test_with_tracer py
-    === CPython 3.7.10 with Python tracer (.tox/py37/bin/python) ===
+    % python3 -m tox
+    ROOT: tox-gh won't override envlist because tox is not running in GitHub Actions
+    .pkg: _optional_hooks> python /usr/local/virtualenvs/coverage/lib/python3.7/site-packages/pyproject_api/_backend.py True setuptools.build_meta
+    .pkg: get_requires_for_build_editable> python /usr/local/virtualenvs/coverage/lib/python3.7/site-packages/pyproject_api/_backend.py True setuptools.build_meta
+    .pkg: build_editable> python /usr/local/virtualenvs/coverage/lib/python3.7/site-packages/pyproject_api/_backend.py True setuptools.build_meta
+    py37: install_package> python -m pip install -U --force-reinstall --no-deps .tox/.tmp/package/87/coverage-7.2.3a0.dev1-0.editable-cp37-cp37m-macosx_10_15_x86_64.whl
+    py37: commands[0]> python igor.py zip_mods
+    py37: commands[1]> python setup.py --quiet build_ext --inplace
+    py37: commands[2]> python -m pip install -q -e .
+    py37: commands[3]> python igor.py test_with_tracer c
+    === CPython 3.7.15 with C tracer (.tox/py37/bin/python) ===
     bringing up nodes...
-    ........................................................................................................................................................... [ 15%]
-    ........................................................................................................................................................... [ 31%]
-    ...........................................................................................................................................s............... [ 47%]
-    ...........................................s...................................................................................sss.sssssssssssssssssss..... [ 63%]
-    ........................................................................................................................................................s.. [ 79%]
-    ......................................s..................................s................................................................................. [ 95%]
-    ........................................ss......                                                                                                            [100%]
-    949 passed, 29 skipped in 40.56s
-    py37 run-test: commands[3] | python setup.py --quiet build_ext --inplace
-    py37 run-test: commands[4] | python igor.py test_with_tracer c
-    === CPython 3.7.10 with C tracer (.tox/py37/bin/python) ===
+    .........................................................................................................................x.................s....s....... [ 11%]
+    ..s.....x.............................................s................................................................................................. [ 22%]
+    ........................................................................................................................................................ [ 34%]
+    ........................................................................................................................................................ [ 45%]
+    ........................................................................................................................................................ [ 57%]
+    .........s....................................................................................................................s......................... [ 68%]
+    .................................s..............................s...............s..................................s.................................... [ 80%]
+    ........................................................s............................................................................................... [ 91%]
+    ......................................s.........................................................................                                         [100%]
+    1316 passed, 12 skipped, 2 xfailed in 36.42s
+    py37: commands[4]> python igor.py remove_extension
+    py37: commands[5]> python igor.py test_with_tracer py
+    === CPython 3.7.15 with Python tracer (.tox/py37/bin/python) ===
     bringing up nodes...
-    ........................................................................................................................................................... [ 15%]
-    ........................................................................................................................................................... [ 31%]
-    ......................................................................s.................................................................................... [ 47%]
-    ........................................................................................................................................................... [ 63%]
-    ..........................s................................................s............................................................................... [ 79%]
-    .................................................................................s......................................................................... [ 95%]
-    ......................................s.........                                                                                                            [100%]
-    973 passed, 5 skipped in 41.36s
-    ____________________________________________________________________________ summary _____________________________________________________________________________
-      py37: commands succeeded
-      congratulations :)
+    ................................................................................................x...........................x.................s......... [ 11%]
+    .....s.............s.s.....................................................s..............ss............................s.ss....ss.ss................... [ 22%]
+    ......................................................................................................................................s................. [ 34%]
+    ..................................................................................................................s..................................... [ 45%]
+    ...................s.ss.....................................................................................s....................s.ss................... [ 57%]
+    ..................s.s................................................................................................................................... [ 68%]
+    ..........................s.........................................ssss...............s.................s...sss..................s...ss...ssss.s....... [ 80%]
+    .......................................................................................................................................................s [ 91%]
+    .........................................................................s.................................ss....                                        [100%]
+    1281 passed, 47 skipped, 2 xfailed in 33.86s
+    .pkg: _exit> python /usr/local/virtualenvs/coverage/lib/python3.7/site-packages/pyproject_api/_backend.py True setuptools.build_meta
+      py37: OK (82.38=setup[2.80]+cmd[0.20,0.35,7.30,37.20,0.21,34.32] seconds)
+      congratulations :) (83.61 seconds)
 
 Tox runs the complete test suite twice for each version of Python you have
-installed.  The first run uses the Python implementation of the trace function,
-the second uses the C implementation.
+installed.  The first run uses the C implementation of the trace function,
+the second uses the Python implementation.
 
 To limit tox to just a few versions of Python, use the ``-e`` switch::
 
-    $ tox -e py37,py39
-
-To run just a few tests, you can use `pytest test selectors`_::
+    $ python3 -m tox -e py37,py39
 
-    $ tox tests/test_misc.py
-    $ tox tests/test_misc.py::HasherTest
-    $ tox tests/test_misc.py::HasherTest::test_string_hashing
+On the tox command line, options after ``--`` are passed to pytest.  To run
+just a few tests, you can use `pytest test selectors`_::
 
-These command run the tests in one file, one class, and just one test,
-respectively.
+    $ python3 -m tox -- tests/test_misc.py
+    $ python3 -m tox -- tests/test_misc.py::HasherTest
+    $ python3 -m tox -- tests/test_misc.py::HasherTest::test_string_hashing
+
+These commands run the tests in one file, one class, and just one test,
+respectively.  The pytest ``-k`` option selects tests based on a word in their
+name, which can be very convenient for ad-hoc test selection.  Of course you
+can combine tox and pytest options::
+
+    $ python3 -m tox -q -e py37 -- -n 0 -vv -k hash
+    === CPython 3.7.15 with C tracer (.tox/py37/bin/python) ===
+    ======================================= test session starts ========================================
+    platform darwin -- Python 3.7.15, pytest-7.2.2, pluggy-1.0.0 -- /Users/nedbat/coverage/.tox/py37/bin/python
+    cachedir: .tox/py37/.pytest_cache
+    rootdir: /Users/nedbat/coverage, configfile: setup.cfg
+    plugins: flaky-3.7.0, hypothesis-6.70.0, xdist-3.2.1
+    collected 1330 items / 1320 deselected / 10 selected
+    run-last-failure: no previously failed tests, not deselecting items.
+
+    tests/test_data.py::CoverageDataTest::test_add_to_hash_with_lines PASSED                     [ 10%]
+    tests/test_data.py::CoverageDataTest::test_add_to_hash_with_arcs PASSED                      [ 20%]
+    tests/test_data.py::CoverageDataTest::test_add_to_lines_hash_with_missing_file PASSED        [ 30%]
+    tests/test_data.py::CoverageDataTest::test_add_to_arcs_hash_with_missing_file PASSED         [ 40%]
+    tests/test_execfile.py::RunPycFileTest::test_running_hashed_pyc PASSED                       [ 50%]
+    tests/test_misc.py::HasherTest::test_string_hashing PASSED                                   [ 60%]
+    tests/test_misc.py::HasherTest::test_bytes_hashing PASSED                                    [ 70%]
+    tests/test_misc.py::HasherTest::test_unicode_hashing PASSED                                  [ 80%]
+    tests/test_misc.py::HasherTest::test_dict_hashing PASSED                                     [ 90%]
+    tests/test_misc.py::HasherTest::test_dict_collision PASSED                                   [100%]
+
+    =============================== 10 passed, 1320 deselected in 1.88s ================================
+    Skipping tests with Python tracer: Only one tracer: no Python tracer for CPython
+      py37: OK (12.22=setup[2.19]+cmd[0.20,0.36,6.57,2.51,0.20,0.19] seconds)
+      congratulations :) (13.10 seconds)
 
 You can also affect the test runs with environment variables. Define any of
 these as 1 to use them:
 
 - ``COVERAGE_NO_PYTRACER=1`` disables the Python tracer if you only want to
   run the CTracer tests.
 
@@ -152,15 +182,16 @@
     $ make lint
 
 The source is pylint-clean, even if it's because there are pragmas quieting
 some warnings.  Please try to keep it that way, but don't let pylint warnings
 keep you from sending patches.  I can clean them up.
 
 Lines should be kept to a 100-character maximum length.  I recommend an
-`editorconfig.org`_ plugin for your editor of choice.
+`editorconfig.org`_ plugin for your editor of choice, which will also help with
+indentation, line endings and so on.
 
 Other style questions are best answered by looking at the existing code.
 Formatting of docstrings, comments, long lines, and so on, should match the
 code that already exists.
 
 Many people love `black`_, but I would prefer not to run it on coverage.py.
 
@@ -216,11 +247,12 @@
 probably fine.  A pull request on GitHub is great, but a simple diff or
 patch works too.
 
 All contributions are expected to include tests for new functionality and
 fixes.  If you need help writing tests, please ask.
 
 
+.. _fork the repo: https://docs.github.com/en/get-started/quickstart/fork-a-repo
 .. _editorconfig.org: http://editorconfig.org
 .. _tox: https://tox.readthedocs.io/
 .. _black: https://pypi.org/project/black/
 .. _set_env.py: https://nedbatchelder.com/blog/201907/set_envpy.html
```

### Comparing `coverage-7.2.2/doc/dbschema.rst` & `coverage-7.2.3/doc/dbschema.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/dict.txt` & `coverage-7.2.3/doc/dict.txt`

 * *Files 13% similar despite different names*

```diff
@@ -1,84 +1,99 @@
+API
+BOM
+BTW
+CPython
+CTracer
+Cobertura
+Consolas
+Cython
+DOCTYPE
+DOM
+HTML
+Jinja
+Mako
+OK
+PYTHONPATH
+TODO
+Tidelift
+URL
+UTF
+XML
 activestate
-api
 apache
-API
+api
 args
 argv
 ascii
+async
 basename
 basenames
 bitbucket
-BOM
 bom
 boolean
 booleans
-BTW
 btw
 builtin
 builtins
 bytecode
 bytecodes
 bytestring
 callable
 callables
 canonicalize
 canonicalized
 canonicalizes
 chdir'd
 clickable
 cmdline
-Cobertura
 codecs
 colorsys
 combinable
 conditionalizing
 config
 configparser
 configurability
 configurability's
 configurer
 configurers
-Consolas
 cov
 coveragepy
 coveragerc
 covhtml
-CPython
 css
-CTracer
-Cython
+dataio
 datetime
 deallocating
+debounce
+decodable
 dedent
 defaultdict
 deserialize
 deserialized
 dict
 dict's
 dicts
 dirname
 django
 docstring
 docstrings
 doctest
 doctests
-DOCTYPE
-DOM
 encodable
 encodings
 endfor
 endif
 eventlet
 exe
 exec'd
 exec'ing
 execfile
 executability
 executable's
+execv
 expr
 extensibility
 favicon
 filename
 filenames
 filepath
 filereporter
@@ -92,38 +107,36 @@
 getattr
 gevent
 gevent's
 github
 gitignore
 globals
 greenlet
+hintedness
 hotkey
 hotkeys
 html
-HTML
 htmlcov
 http
 https
 importlib
 installable
 instancemethod
 int
 ints
 invariants
 iterable
 iterables
-Jinja
-jquery
 jQuery
+jquery
 json
 jython
 kwargs
 lcov
 localStorage
-Mako
 manylinux
 matcher
 matchers
 merchantability
 metadata
 meth
 mischaracterize
@@ -132,75 +145,84 @@
 modulename
 monkeypatch
 monkeypatching
 monospaced
 morf
 morfs
 multi
+multiproc
 mumbo
 mycode
+mypy
 namespace
 namespaces
 nano
 nbsp
 ned
 nedbat
 nedbatchelder
+newb
+nocover
 nosetests
 nullary
 num
 numbits
 numpy
 ok
-OK
 opcode
 opcodes
 optparse
 os
 outfile
 overridable
 parallelizing
 parsable
 parsers
+pathlib
 pathnames
 plugin
 plugins
 pragma
-pragmas
 pragma'd
+pragmas
 pre
+premain
 prepended
 prepending
 programmability
 programmatically
 py
 py's
 pyc
+pyenv
 pyexpat
+pylib
 pylint
 pyproject
 pypy
 pytest
 pythonpath
-PYTHONPATH
 pyw
 rcfile
 readme
 readthedocs
+realpath
 recordable
 refactored
 refactoring
 refactorings
 regex
 regexes
 reimplemented
 renderer
+rootname
 runnable
 runtime
 scrollbar
+septatrix
 serializable
 settrace
 setuptools
 sigterm
 sitecustomize
 sortable
 src
@@ -213,20 +235,18 @@
 subdirectory
 subprocess
 subprocesses
 symlink
 symlinks
 syntaxes
 sys
-templite
 templating
+templite
 testability
-Tidelift
 todo
-TODO
 tokenization
 tokenize
 tokenized
 tokenizer
 tokenizes
 tokenizing
 toml
@@ -243,22 +263,21 @@
 unicode
 uninstall
 unittest
 unparsable
 unrunnable
 unsubscriptable
 untokenizable
+usecache
 username
-URL
-UTF
 utf
 vendored
 versionadded
 virtualenv
 wikipedia
 wildcard
 wildcards
 www
+xdist
 xml
-XML
 xrange
 xyzzy
```

### Comparing `coverage-7.2.2/doc/excluding.rst` & `coverage-7.2.3/doc/excluding.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/faq.rst` & `coverage-7.2.3/doc/faq.rst`

 * *Files 1% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 :ref:`option <cmd_run_debug>`, also settable as ``[run] debug=trace`` in the
 :ref:`settings file <config_run_debug>`, or as ``COVERAGE_DEBUG=trace`` in an
 environment variable.
 
 This will write a line for each file considered, indicating whether it is
 traced or not, and if not, why not.  Be careful though: the output might be
 swallowed by your test runner.  If so, a ``COVERAGE_DEBUG_FILE=/tmp/cov.out``
-environemnt variable can direct the output to a file insttead to ensure you see
+environment variable can direct the output to a file instead to ensure you see
 everything.
 
 
 Q: Why do unexecutable lines show up as executed?
 .................................................
 
 Usually this is because you've updated your code and run coverage.py on it
```

### Comparing `coverage-7.2.2/doc/howitworks.rst` & `coverage-7.2.3/doc/howitworks.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/index.rst` & `coverage-7.2.3/doc/index.rst`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 not.
 
 The latest version is coverage.py |release|, released |release_date|.  It is
 supported on:
 
 .. PYVERSIONS
 
-* Python versions 3.7 through 3.12.0a6.
+* Python versions 3.7 through 3.12.0a7.
 * PyPy3 7.3.11.
 
 .. ifconfig:: prerelease
 
     **This is a pre-release build.  The usual warnings about possible bugs
     apply.** The latest stable version is coverage.py 6.5.0, `described here`_.
```

### Comparing `coverage-7.2.2/doc/install.rst` & `coverage-7.2.3/doc/install.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White.png` & `coverage-7.2.3/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png` & `coverage-7.2.3/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/media/sleepy-snake-600.png` & `coverage-7.2.3/doc/media/sleepy-snake-600.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/media/sleepy-snake-circle-150.png` & `coverage-7.2.3/doc/media/sleepy-snake-circle-150.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/plugins.rst` & `coverage-7.2.3/doc/plugins.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/python-coverage.1.txt` & `coverage-7.2.3/doc/python-coverage.1.txt`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/sample_html/favicon_32.png` & `coverage-7.2.3/doc/sample_html/favicon_32.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/sample_html/keybd_closed.png` & `coverage-7.2.3/doc/sample_html/keybd_closed.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/sample_html/keybd_open.png` & `coverage-7.2.3/doc/sample_html/keybd_open.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/sleepy.rst` & `coverage-7.2.3/doc/sleepy.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/source.rst` & `coverage-7.2.3/doc/source.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/subprocess.rst` & `coverage-7.2.3/doc/subprocess.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/trouble.rst` & `coverage-7.2.3/doc/trouble.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/doc/whatsnew5x.rst` & `coverage-7.2.3/doc/whatsnew5x.rst`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/howto.txt` & `coverage-7.2.3/howto.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,41 +1,45 @@
 * Release checklist
 
 - Check that the current virtualenv matches the current coverage branch.
 - start branch for release work
-- Version number in coverage/version.py
+    $ make relbranch
+- Edit version number in coverage/version.py
         version_info = (4, 0, 2, "alpha", 1)
         version_info = (4, 0, 2, "beta", 1)
         version_info = (4, 0, 2, "candidate", 1)
         version_info = (4, 0, 2, "final", 0)
     - make sure: _dev = 0
-- Supported Python version numbers. Search for "PYVERSIONS".
+- Edit supported Python version numbers. Search for "PYVERSIONS".
 - Update source files with release facts:
     $ make edit_for_release
-- run `python igor.py cheats` to get useful snippets for next steps.
+- Get useful snippets for next steps, and beyond, in cheats.txt
+    $ make cheats
 - Look over CHANGES.rst
 - Update README.rst
     - "New in x.y:"
     - Python versions supported
 - Update docs
     - Python versions in doc/index.rst
     - IF PRE-RELEASE:
         - Version of latest stable release in doc/index.rst
     - Make sure the docs are cogged:
         $ make prebuild
     - Don't forget the man page: doc/python-coverage.1.txt
     - Check that the docs build correctly:
         $ tox -e doc
 - commit the release-prep changes
+    $ make relcommit1
 - Generate new sample_html to get the latest, incl footer version number:
     - IF PRE-RELEASE:
         $ make sample_html_beta
     - IF NOT PRE-RELEASE:
         $ make sample_html
-        check in the new sample html
+        - check in the new sample html
+            $ make relcommit2
 - Done with changes to source files
     - check them in on the release prep branch
     - wait for ci to finish
     - merge to master
     - git push
 - Start the kits:
     - Trigger the kit GitHub Action
```

### Comparing `coverage-7.2.2/igor.py` & `coverage-7.2.3/igor.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/benchmark/benchmark.py` & `coverage-7.2.3/lab/benchmark/benchmark.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/benchmark/empty.py` & `coverage-7.2.3/lab/benchmark/empty.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/benchmark/run.py` & `coverage-7.2.3/lab/benchmark/run.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/branches.py` & `coverage-7.2.3/lab/branches.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/compare_times.sh` & `coverage-7.2.3/lab/compare_times.sh`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/coverage-03.dtd` & `coverage-7.2.3/lab/coverage-03.dtd`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/coverage-04.dtd` & `coverage-7.2.3/lab/coverage-04.dtd`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/extract_code.py` & `coverage-7.2.3/lab/extract_code.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/find_class.py` & `coverage-7.2.3/lab/find_class.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/genpy.py` & `coverage-7.2.3/lab/genpy.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/goals.py` & `coverage-7.2.3/lab/goals.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/hack_pyc.py` & `coverage-7.2.3/lab/hack_pyc.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/new-data.js` & `coverage-7.2.3/lab/new-data.js`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/notes/bug1303.txt` & `coverage-7.2.3/lab/notes/bug1303.txt`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/notes/pypy-738-decorated-functions.txt` & `coverage-7.2.3/lab/notes/pypy-738-decorated-functions.txt`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/parse_all.py` & `coverage-7.2.3/lab/parse_all.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/parser.py` & `coverage-7.2.3/lab/parser.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/platform_info.py` & `coverage-7.2.3/lab/platform_info.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/run_trace.py` & `coverage-7.2.3/lab/run_trace.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/select_contexts.py` & `coverage-7.2.3/lab/select_contexts.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/lab/show_pyc.py` & `coverage-7.2.3/lab/show_pyc.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/metacov.ini` & `coverage-7.2.3/metacov.ini`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/pylintrc` & `coverage-7.2.3/pylintrc`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/requirements/dev.in` & `coverage-7.2.3/requirements/dev.in`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/requirements/pins.pip` & `coverage-7.2.3/requirements/pins.pip`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/setup.py` & `coverage-7.2.3/setup.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/balance_xdist_plugin.py` & `coverage-7.2.3/tests/balance_xdist_plugin.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/conftest.py` & `coverage-7.2.3/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/coveragetest.py` & `coverage-7.2.3/tests/coveragetest.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/annotate/white/white.py,cover` & `coverage-7.2.3/tests/gold/annotate/white/white.py,cover`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/Makefile` & `coverage-7.2.3/tests/gold/html/Makefile`

 * *Files 2% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 		fi ; \
 	done ; \
 	true	# because the for loop exits with 1 for some reason.
 
 clean:		## Remove the effects of this Makefile.
 	@git clean -fq .
 
-update-gold:	## Copy output files from latest tests to gold files.
+update-gold:	## Copy actual output files from latest tests to gold files.
 	@for sub in ../../actual/html/*; do \
 		rsync --verbose --existing --recursive $$sub/ $$(basename $$sub) ; \
 	done ; \
 	true
 
 update-support:	## Copy latest support files here for posterity.
 	cp ../../../coverage/htmlfiles/*.{css,js,png} support
```

### Comparing `coverage-7.2.2/tests/gold/html/a/a_py.html` & `coverage-7.2.3/tests/gold/html/a/a_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/a/index.html` & `coverage-7.2.3/tests/gold/html/a/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/b_branch/b_py.html` & `coverage-7.2.3/tests/gold/html/b_branch/b_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/b_branch/index.html` & `coverage-7.2.3/tests/gold/html/b_branch/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/bom/bom_py.html` & `coverage-7.2.3/tests/gold/html/bom/bom_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/bom/index.html` & `coverage-7.2.3/tests/gold/html/bom/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/isolatin1/index.html` & `coverage-7.2.3/tests/gold/html/isolatin1/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/isolatin1/isolatin1_py.html` & `coverage-7.2.3/tests/gold/html/isolatin1/isolatin1_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_1/index.html` & `coverage-7.2.3/tests/gold/html/omit_1/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_1/m1_py.html` & `coverage-7.2.3/tests/gold/html/omit_1/m1_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_1/m2_py.html` & `coverage-7.2.3/tests/gold/html/omit_1/m2_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_1/m3_py.html` & `coverage-7.2.3/tests/gold/html/omit_1/m3_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_1/main_py.html` & `coverage-7.2.3/tests/gold/html/omit_1/main_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_2/index.html` & `coverage-7.2.3/tests/gold/html/omit_2/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_2/m2_py.html` & `coverage-7.2.3/tests/gold/html/omit_2/m2_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_2/m3_py.html` & `coverage-7.2.3/tests/gold/html/omit_2/m3_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_2/main_py.html` & `coverage-7.2.3/tests/gold/html/omit_2/main_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_3/index.html` & `coverage-7.2.3/tests/gold/html/omit_3/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_3/m3_py.html` & `coverage-7.2.3/tests/gold/html/omit_3/m3_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_3/main_py.html` & `coverage-7.2.3/tests/gold/html/omit_3/main_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_4/index.html` & `coverage-7.2.3/tests/gold/html/omit_4/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_4/m1_py.html` & `coverage-7.2.3/tests/gold/html/omit_4/m1_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_4/m3_py.html` & `coverage-7.2.3/tests/gold/html/omit_4/m3_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_4/main_py.html` & `coverage-7.2.3/tests/gold/html/omit_4/main_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_5/index.html` & `coverage-7.2.3/tests/gold/html/omit_5/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_5/m1_py.html` & `coverage-7.2.3/tests/gold/html/omit_5/m1_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/omit_5/main_py.html` & `coverage-7.2.3/tests/gold/html/omit_5/main_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/other/blah_blah_other_py.html` & `coverage-7.2.3/tests/gold/html/other/blah_blah_other_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/other/here_py.html` & `coverage-7.2.3/tests/gold/html/other/here_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/other/index.html` & `coverage-7.2.3/tests/gold/html/other/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/partial/index.html` & `coverage-7.2.3/tests/gold/html/partial/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/partial/partial_py.html` & `coverage-7.2.3/tests/gold/html/partial/partial_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/partial_626/index.html` & `coverage-7.2.3/tests/gold/html/partial_626/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/partial_626/partial_py.html` & `coverage-7.2.3/tests/gold/html/partial_626/partial_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/styled/a_py.html` & `coverage-7.2.3/tests/gold/html/styled/a_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/styled/index.html` & `coverage-7.2.3/tests/gold/html/styled/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/styled/style.css` & `coverage-7.2.3/tests/gold/html/styled/style.css`

 * *Files 0% similar despite different names*

```diff
@@ -254,20 +254,18 @@
 
 #source p input:checked ~ .ctxs { padding: .25em .5em; overflow-y: scroll; max-height: 10.5em; }
 
 #source p label.ctx { color: #999; display: inline-block; padding: 0 .5em; font-size: .8333em; }
 
 @media (prefers-color-scheme: dark) { #source p label.ctx { color: #777; } }
 
-#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; }
+#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; text-align: right; }
 
 @media (prefers-color-scheme: dark) { #source p .ctxs { background: #056; } }
 
-#source p .ctxs span { display: block; text-align: right; }
-
 #index { font-family: SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 0.875em; }
 
 #index table.index { margin-left: -.5em; }
 
 #index td, #index th { text-align: right; width: 5em; padding: .25em .5em; border-bottom: 1px solid #eee; }
 
 @media (prefers-color-scheme: dark) { #index td, #index th { border-color: #333; } }
```

### Comparing `coverage-7.2.2/tests/gold/html/support/coverage_html.js` & `coverage-7.2.3/tests/gold/html/support/coverage_html.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -170,15 +170,15 @@
                 cell.textContent = totals[column];
             }
         }
     }));
 
     // Trigger change event on setup, to force filter on page refresh
     // (filter value may still be present).
-    document.getElementById("filter").dispatchEvent(new Event("change"));
+    document.getElementById("filter").dispatchEvent(new Event("input"));
 };
 
 coverage.INDEX_SORT_STORAGE = "COVERAGE_INDEX_SORT_2";
 
 // Loaded on index.html
 coverage.index_ready = function() {
     coverage.assign_shortkeys();
@@ -221,15 +221,15 @@
 // -- pyfile stuff --
 
 coverage.LINE_FILTERS_STORAGE = "COVERAGE_LINE_FILTERS";
 
 coverage.pyfile_ready = function() {
     // If we're directed to a particular line number, highlight the line.
     var frag = location.hash;
-    if (frag.length > 2 && frag[1] === 't') {
+    if (frag.length > 2 && frag[1] === "t") {
         document.querySelector(frag).closest(".n").classList.add("highlight");
         coverage.set_sel(parseInt(frag.substr(2), 10));
     } else {
         coverage.set_sel(0);
     }
 
     on_click(".button_toggle_run", coverage.toggle_lines);
@@ -268,14 +268,18 @@
         coverage.set_line_visibilty(cls, coverage.filters[cls]);
     }
 
     coverage.assign_shortkeys();
     coverage.init_scroll_markers();
     coverage.wire_up_sticky_header();
 
+    document.querySelectorAll("[id^=ctxs]").forEach(
+        cbox => cbox.addEventListener("click", coverage.expand_contexts)
+    );
+
     // Rebuild scroll markers when the window height changes.
     window.addEventListener("resize", coverage.build_scroll_markers);
 };
 
 coverage.toggle_lines = function(event) {
     const btn = event.target.closest("button");
     const category = btn.value
@@ -540,41 +544,41 @@
         top: to_pos,
         behavior: "smooth"
     });
 };
 
 coverage.init_scroll_markers = function() {
     // Init some variables
-    coverage.lines_len = document.querySelectorAll('#source > p').length;
+    coverage.lines_len = document.querySelectorAll("#source > p").length;
 
     // Build html
     coverage.build_scroll_markers();
 };
 
 coverage.build_scroll_markers = function() {
-    const temp_scroll_marker = document.getElementById('scroll_marker')
+    const temp_scroll_marker = document.getElementById("scroll_marker")
     if (temp_scroll_marker) temp_scroll_marker.remove();
     // Don't build markers if the window has no scroll bar.
     if (document.body.scrollHeight <= window.innerHeight) {
         return;
     }
 
     const marker_scale = window.innerHeight / document.body.scrollHeight;
     const line_height = Math.min(Math.max(3, window.innerHeight / coverage.lines_len), 10);
 
     let previous_line = -99,
         last_mark, last_top;
 
     const scroll_marker = document.createElement("div");
     scroll_marker.id = "scroll_marker";
-    document.getElementById('source').querySelectorAll(
-        'p.show_run, p.show_mis, p.show_exc, p.show_exc, p.show_par'
+    document.getElementById("source").querySelectorAll(
+        "p.show_run, p.show_mis, p.show_exc, p.show_exc, p.show_par"
     ).forEach(element => {
         const line_top = Math.floor(element.offsetTop * marker_scale);
-        const line_number = parseInt(element.id.substr(1));
+        const line_number = parseInt(element.querySelector(".n a").id.substr(1));
 
         if (line_number === previous_line + 1) {
             // If this solid missed block just make previous mark higher.
             last_mark.style.height = `${line_top + line_height - last_top}px`;
         } else {
             // Add colored line in scroll_marker block.
             last_mark = document.createElement("div");
@@ -590,32 +594,48 @@
     });
 
     // Append last to prevent layout calculation
     document.body.append(scroll_marker);
 };
 
 coverage.wire_up_sticky_header = function() {
-    const header = document.querySelector('header');
+    const header = document.querySelector("header");
     const header_bottom = (
-        header.querySelector('.content h2').getBoundingClientRect().top -
+        header.querySelector(".content h2").getBoundingClientRect().top -
         header.getBoundingClientRect().top
     );
 
     function updateHeader() {
         if (window.scrollY > header_bottom) {
-            header.classList.add('sticky');
+            header.classList.add("sticky");
         } else {
-            header.classList.remove('sticky');
+            header.classList.remove("sticky");
         }
     }
 
-    window.addEventListener('scroll', updateHeader);
+    window.addEventListener("scroll", updateHeader);
     updateHeader();
 };
 
+coverage.expand_contexts = function(e) {
+    var ctxs = e.target.parentNode.querySelector(".ctxs");
+
+    if (!ctxs.classList.contains("expanded")) {
+        var ctxs_text = ctxs.textContent;
+        var width = Number(ctxs_text[0]);
+        ctxs.textContent = "";
+        for (var i = 1; i < ctxs_text.length; i += width) {
+            key = ctxs_text.substring(i, i + width).trim();
+            ctxs.appendChild(document.createTextNode(contexts[key]));
+            ctxs.appendChild(document.createElement("br"));
+        }
+        ctxs.classList.add("expanded");
+    }
+};
+
 document.addEventListener("DOMContentLoaded", () => {
     if (document.body.classList.contains("indexfile")) {
         coverage.index_ready();
     } else {
         coverage.pyfile_ready();
     }
 });
```

### Comparing `coverage-7.2.2/tests/gold/html/support/favicon_32.png` & `coverage-7.2.3/tests/gold/html/support/favicon_32.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/support/keybd_closed.png` & `coverage-7.2.3/tests/gold/html/support/keybd_closed.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/support/keybd_open.png` & `coverage-7.2.3/tests/gold/html/support/keybd_open.png`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/support/style.css` & `coverage-7.2.3/tests/gold/html/support/style.css`

 * *Files 0% similar despite different names*

```diff
@@ -254,20 +254,18 @@
 
 #source p input:checked ~ .ctxs { padding: .25em .5em; overflow-y: scroll; max-height: 10.5em; }
 
 #source p label.ctx { color: #999; display: inline-block; padding: 0 .5em; font-size: .8333em; }
 
 @media (prefers-color-scheme: dark) { #source p label.ctx { color: #777; } }
 
-#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; }
+#source p .ctxs { display: block; max-height: 0; overflow-y: hidden; transition: all .2s; padding: 0 .5em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; white-space: nowrap; background: #d0e8ff; border-radius: .25em; margin-right: 1.75em; text-align: right; }
 
 @media (prefers-color-scheme: dark) { #source p .ctxs { background: #056; } }
 
-#source p .ctxs span { display: block; text-align: right; }
-
 #index { font-family: SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 0.875em; }
 
 #index table.index { margin-left: -.5em; }
 
 #index td, #index th { text-align: right; width: 5em; padding: .25em .5em; border-bottom: 1px solid #eee; }
 
 @media (prefers-color-scheme: dark) { #index td, #index th { border-color: #333; } }
```

### Comparing `coverage-7.2.2/tests/gold/html/unicode/index.html` & `coverage-7.2.3/tests/gold/html/unicode/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/html/unicode/unicode_py.html` & `coverage-7.2.3/tests/gold/html/unicode/unicode_py.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/xml/x_xml/coverage.xml` & `coverage-7.2.3/tests/gold/xml/x_xml/coverage.xml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/gold/xml/y_xml_branch/coverage.xml` & `coverage-7.2.3/tests/gold/xml/y_xml_branch/coverage.xml`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/goldtest.py` & `coverage-7.2.3/tests/goldtest.py`

 * *Files 2% similar despite different names*

```diff
@@ -42,27 +42,31 @@
     If a comparison fails, a message will be written to stdout, the original
     unscrubbed output of the test will be written to an "/actual/" directory
     alongside the "/gold/" directory, and an assertion will be raised.
 
     """
     __tracebackhide__ = True    # pytest, please don't show me this function.
     assert os_sep("/gold/") in expected_dir
+    assert os.path.exists(actual_dir)
+    os.makedirs(expected_dir, exist_ok=True)
 
     dc = filecmp.dircmp(expected_dir, actual_dir)
     diff_files = _fnmatch_list(dc.diff_files, file_pattern)
     expected_only = _fnmatch_list(dc.left_only, file_pattern)
     actual_only = _fnmatch_list(dc.right_only, file_pattern)
 
     def save_mismatch(f: str) -> None:
         """Save a mismatched result to tests/actual."""
         save_path = expected_dir.replace(os_sep("/gold/"), os_sep("/actual/"))
         os.makedirs(save_path, exist_ok=True)
-        with open(os.path.join(save_path, f), "w") as savef:
+        save_file = os.path.join(save_path, f)
+        with open(save_file, "w") as savef:
             with open(os.path.join(actual_dir, f)) as readf:
                 savef.write(readf.read())
+                print(os_sep(f"Saved actual output to '{save_file}': see tests/gold/README.rst"))
 
     # filecmp only compares in binary mode, but we want text mode.  So
     # look through the list of different files, and compare them
     # ourselves.
     text_diff = []
     for f in diff_files:
         expected_file = os.path.join(expected_dir, f)
```

### Comparing `coverage-7.2.2/tests/helpers.py` & `coverage-7.2.3/tests/helpers.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/js/index.html` & `coverage-7.2.3/tests/js/index.html`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/js/tests.js` & `coverage-7.2.3/tests/js/tests.js`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/mixins.py` & `coverage-7.2.3/tests/mixins.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/modules/plugins/another.py` & `coverage-7.2.3/tests/modules/plugins/another.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/modules/process_test/try_execfile.py` & `coverage-7.2.3/tests/modules/process_test/try_execfile.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/osinfo.py` & `coverage-7.2.3/tests/osinfo.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/plugin1.py` & `coverage-7.2.3/tests/plugin1.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/plugin2.py` & `coverage-7.2.3/tests/plugin2.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/plugin_config.py` & `coverage-7.2.3/tests/plugin_config.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/qunit/jquery.tmpl.min.js` & `coverage-7.2.3/tests/qunit/jquery.tmpl.min.js`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/stress_phystoken.tok` & `coverage-7.2.3/tests/stress_phystoken.tok`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/stress_phystoken_dos.tok` & `coverage-7.2.3/tests/stress_phystoken_dos.tok`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_annotate.py` & `coverage-7.2.3/tests/test_annotate.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_api.py` & `coverage-7.2.3/tests/test_api.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_arcs.py` & `coverage-7.2.3/tests/test_arcs.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_cmdline.py` & `coverage-7.2.3/tests/test_cmdline.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_collector.py` & `coverage-7.2.3/tests/test_collector.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_concurrency.py` & `coverage-7.2.3/tests/test_concurrency.py`

 * *Files 2% similar despite different names*

```diff
@@ -701,15 +701,15 @@
 
 @pytest.mark.skipif(env.WINDOWS, reason="SIGTERM doesn't work the same on Windows")
 @flaky(max_runs=3)          # Sometimes a test fails due to inherent randomness. Try more times.
 class SigtermTest(CoverageTest):
     """Tests of our handling of SIGTERM."""
 
     @pytest.mark.parametrize("sigterm", [False, True])
-    def test_sigterm_saves_data(self, sigterm: bool) -> None:
+    def test_sigterm_multiprocessing_saves_data(self, sigterm: bool) -> None:
         # A terminated process should save its coverage data.
         self.make_file("clobbered.py", """\
             import multiprocessing
             import time
 
             def subproc(x):
                 if x.value == 3:
@@ -747,14 +747,39 @@
         out = self.run_command("coverage report -m")
         if sigterm:
             expected = "clobbered.py 17 1 94% 6"
         else:
             expected = "clobbered.py 17 5 71% 5-10"
         assert self.squeezed_lines(out)[2] == expected
 
+    def test_sigterm_threading_saves_data(self) -> None:
+        # A terminated process should save its coverage data.
+        self.make_file("handler.py", """\
+            import os, signal
+
+            print("START", flush=True)
+            print("SIGTERM", flush=True)
+            os.kill(os.getpid(), signal.SIGTERM)
+            print("NOT HERE", flush=True)
+            """)
+        self.make_file(".coveragerc", """\
+            [run]
+            # The default concurrency option.
+            concurrency = thread
+            sigterm = true
+            """)
+        out = self.run_command("coverage run handler.py")
+        if env.LINUX:
+            assert out == "START\nSIGTERM\nTerminated\n"
+        else:
+            assert out == "START\nSIGTERM\n"
+        out = self.run_command("coverage report -m")
+        expected = "handler.py 5 1 80% 6"
+        assert self.squeezed_lines(out)[2] == expected
+
     def test_sigterm_still_runs(self) -> None:
         # A terminated process still runs its own SIGTERM handler.
         self.make_file("handler.py", """\
             import multiprocessing
             import signal
             import time
```

### Comparing `coverage-7.2.2/tests/test_config.py` & `coverage-7.2.3/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_context.py` & `coverage-7.2.3/tests/test_context.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_coverage.py` & `coverage-7.2.3/tests/test_coverage.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_data.py` & `coverage-7.2.3/tests/test_data.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_debug.py` & `coverage-7.2.3/tests/test_debug.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_execfile.py` & `coverage-7.2.3/tests/test_execfile.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_filereporter.py` & `coverage-7.2.3/tests/test_filereporter.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_files.py` & `coverage-7.2.3/tests/test_files.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_goldtest.py` & `coverage-7.2.3/tests/test_goldtest.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 import re
 
 import pytest
 
 from tests.coveragetest import CoverageTest, TESTS_DIR
 from tests.goldtest import compare, gold_path
 from tests.goldtest import contains, contains_any, contains_rx, doesnt_contain
-from tests.helpers import re_line, remove_tree
+from tests.helpers import os_sep, re_line, remove_tree
 
 GOOD_GETTY = """\
 Four score and seven years ago our fathers brought forth upon this continent, a
 new nation, conceived in Liberty, and dedicated to the proposition that all men
 are created equal.
 11/19/9999, Gettysburg, Pennsylvania
 """
@@ -69,14 +69,18 @@
 
         # Stdout has a description of the diff.  The diff shows the scrubbed content.
         stdout = self.stdout()
         assert "- Four score" in stdout
         assert "+ Five score" in stdout
         assert re_line(rf"^:::: diff '.*{GOLD_PATH_RX}' and '{OUT_PATH_RX}'", stdout)
         assert re_line(rf"^:::: end diff '.*{GOLD_PATH_RX}' and '{OUT_PATH_RX}'", stdout)
+        assert (
+            os_sep(f"Saved actual output to '{ACTUAL_GETTY_FILE}': see tests/gold/README.rst")
+            in os_sep(stdout)
+        )
         assert "  D/D/D, Gxxx, Pennsylvania" in stdout
 
         # The actual file was saved.
         with open(ACTUAL_GETTY_FILE) as f:
             saved = f.read()
         assert saved == BAD_GETTY
```

### Comparing `coverage-7.2.2/tests/test_html.py` & `coverage-7.2.3/tests/test_html.py`

 * *Files 0% similar despite different names*

```diff
@@ -1195,14 +1195,17 @@
         for label, expected in zip(context_labels, expected_lines):
             actual = [
                 ld.number for ld in d.lines
                 if label == ld.contexts_label or label in (ld.contexts or ())
             ]
             assert sorted(expected) == sorted(actual)
 
+        cov.html_report(mod, directory="out/contexts")
+        compare_html(gold_path("html/contexts"), "out/contexts")
+
     def test_filtered_dynamic_contexts(self) -> None:
         self.make_file("two_tests.py", self.SOURCE)
         cov = coverage.Coverage(source=["."])
         cov.set_option("run:dynamic_context", "test_function")
         cov.set_option("html:show_contexts", True)
         cov.set_option("report:contexts", ["test_one"])
         mod = self.start_import_stop(cov, "two_tests")
@@ -1253,7 +1256,16 @@
 
     def test_bad_anchor(self) -> None:
         # Does assert_valid_hrefs detect fragments that go nowhere?
         self.make_file("htmlcov/index.html", "<a href='#nothing'>Nothing</a>")
         msg = "Fragment '#nothing' in htmlcov.index.html has no anchor"
         with pytest.raises(AssertionError, match=msg):
             self.assert_valid_hrefs()
+
+
+@pytest.mark.parametrize("n, key", [
+    (0, "a"),
+    (1, "b"),
+    (999999999, "e9S_p"),
+])
+def test_encode_int(n: int, key: str) -> None:
+    assert coverage.html.encode_int(n) == key
```

### Comparing `coverage-7.2.2/tests/test_json.py` & `coverage-7.2.3/tests/test_json.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_lcov.py` & `coverage-7.2.3/tests/test_lcov.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_misc.py` & `coverage-7.2.3/tests/test_misc.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_mixins.py` & `coverage-7.2.3/tests/test_mixins.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_numbits.py` & `coverage-7.2.3/tests/test_numbits.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_oddball.py` & `coverage-7.2.3/tests/test_oddball.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_parser.py` & `coverage-7.2.3/tests/test_parser.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_phystokens.py` & `coverage-7.2.3/tests/test_phystokens.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_plugins.py` & `coverage-7.2.3/tests/test_plugins.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_process.py` & `coverage-7.2.3/tests/test_process.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_python.py` & `coverage-7.2.3/tests/test_python.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_report.py` & `coverage-7.2.3/tests/test_report.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_results.py` & `coverage-7.2.3/tests/test_results.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_setup.py` & `coverage-7.2.3/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_summary.py` & `coverage-7.2.3/tests/test_summary.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_templite.py` & `coverage-7.2.3/tests/test_templite.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_testing.py` & `coverage-7.2.3/tests/test_testing.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_venv.py` & `coverage-7.2.3/tests/test_venv.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_version.py` & `coverage-7.2.3/tests/test_version.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tests/test_xml.py` & `coverage-7.2.3/tests/test_xml.py`

 * *Files identical despite different names*

### Comparing `coverage-7.2.2/tox.ini` & `coverage-7.2.3/tox.ini`

 * *Files identical despite different names*

