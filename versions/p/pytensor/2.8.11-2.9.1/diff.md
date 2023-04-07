# Comparing `tmp/pytensor-2.8.11.tar.gz` & `tmp/pytensor-2.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytensor-2.8.11.tar", last modified: Wed Dec 14 07:21:22 2022, max compression
+gzip compressed data, was "pytensor-2.9.1.tar", last modified: Tue Jan 10 16:00:13 2023, max compression
```

## Comparing `pytensor-2.8.11.tar` & `pytensor-2.9.1.tar`

### file list

```diff
@@ -1,501 +1,462 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.500630 pytensor-2.8.11/
--rw-r--r--   0 runner    (1001) docker     (123)      817 2022-12-14 07:21:20.000000 pytensor-2.8.11/DESCRIPTION.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2641 2022-12-14 07:21:20.000000 pytensor-2.8.11/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      243 2022-12-14 07:21:20.000000 pytensor-2.8.11/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2197 2022-12-14 07:21:22.500630 pytensor-2.8.11/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3736 2022-12-14 07:21:20.000000 pytensor-2.8.11/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.448650 pytensor-2.8.11/bin/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/bin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2022-12-14 07:21:20.000000 pytensor-2.8.11/bin/downstream_pr.sh
--rw-r--r--   0 runner    (1001) docker     (123)       66 2022-12-14 07:21:20.000000 pytensor-2.8.11/bin/pytensor-cache
--rw-r--r--   0 runner    (1001) docker     (123)     4173 2022-12-14 07:21:20.000000 pytensor-2.8.11/bin/pytensor_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     1326 2022-12-14 07:21:20.000000 pytensor-2.8.11/bin/upstream_pr.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.452648 pytensor-2.8.11/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.452648 pytensor-2.8.11/doc/.templates/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/.templates/PLACEHOLDER
--rw-r--r--   0 runner    (1001) docker     (123)     1409 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/.templates/layout.html
--rw-r--r--   0 runner    (1001) docker     (123)     2641 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1161 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/acknowledgement.rst
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)    14117 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/bcast.svg
--rw-r--r--   0 runner    (1001) docker     (123)     8205 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1310 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/core_development_guide.rst
--rw-r--r--   0 runner    (1001) docker     (123)      269 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/css.inc
--rw-r--r--   0 runner    (1001) docker     (123)     8691 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/dev_start_guide.rst
--rw-r--r--   0 runner    (1001) docker     (123)      272 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/environment.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/extending/
--rw-r--r--   0 runner    (1001) docker     (123)    28371 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/apply.png
--rw-r--r--   0 runner    (1001) docker     (123)    20340 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/apply.svg
--rw-r--r--   0 runner    (1001) docker     (123)    32078 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/apply2.svg
--rw-r--r--   0 runner    (1001) docker     (123)    46694 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/creating_a_c_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6362 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/creating_a_numba_jax_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)    33109 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/creating_an_op.rst
--rw-r--r--   0 runner    (1001) docker     (123)    22706 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/ctype.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1136 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/extending_faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5509 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/extending_pytensor_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)    55789 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/graph_rewriting.rst
--rw-r--r--   0 runner    (1001) docker     (123)    13797 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/graphstructures.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1704 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9060 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/inplace.rst
--rw-r--r--   0 runner    (1001) docker     (123)    25030 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/op.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9624 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/other_ops.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/extending/pics/
--rw-r--r--   0 runner    (1001) docker     (123)    23471 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/pics/symbolic_graph_opt.png
--rw-r--r--   0 runner    (1001) docker     (123)    62062 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/pics/symbolic_graph_unopt.png
--rw-r--r--   0 runner    (1001) docker     (123)     4951 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/pipeline.rst
--rw-r--r--   0 runner    (1001) docker     (123)    17158 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/scan.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1634 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/tips.rst
--rw-r--r--   0 runner    (1001) docker     (123)    19727 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/type.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10092 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/unittest.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7717 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/extending/using_params.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6800 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1281 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/generate_dtype_tensor_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     7126 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/glossary.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/images/
--rw-r--r--   0 runner    (1001) docker     (123)    94102 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/Elman_srnn.png
--rw-r--r--   0 runner    (1001) docker     (123)   102018 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/blocksparse.png
--rw-r--r--   0 runner    (1001) docker     (123)    13780 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/lstm.png
--rw-r--r--   0 runner    (1001) docker     (123)    14362 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/lstm_memorycell.png
--rw-r--r--   0 runner    (1001) docker     (123)    14107 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/pytensor_logo.svg
--rw-r--r--   0 runner    (1001) docker     (123)   273555 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/talk2010.gif
--rw-r--r--   0 runner    (1001) docker     (123)    12455 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/images/talk2010.png
--rw-r--r--   0 runner    (1001) docker     (123)     3054 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      747 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/install.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/internal/
--rw-r--r--   0 runner    (1001) docker     (123)     1082 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/internal/how_to_release.rst
--rw-r--r--   0 runner    (1001) docker     (123)      155 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/internal/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2538 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/internal/metadocumentation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8042 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/introduction.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/library/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.456647 pytensor-2.8.11/doc/library/compile/
--rw-r--r--   0 runner    (1001) docker     (123)     8382 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/debugmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8934 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/function.rst
--rw-r--r--   0 runner    (1001) docker     (123)      454 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    11851 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/io.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2160 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/mode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2053 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/nanguardmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)      911 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/opfromgraph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      205 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)      424 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/profilemode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3043 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/compile/shared.rst
--rw-r--r--   0 runner    (1001) docker     (123)    30830 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/config.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/d3viz/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/d3viz/examples/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.444651 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/css/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/css/d3-context-menu.css
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/css/d3viz.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js
--rw-r--r--   0 runner    (1001) docker     (123)   151143 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    23339 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3viz.js
--rw-r--r--   0 runner    (1001) docker     (123)    47566 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)   115617 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js
--rw-r--r--   0 runner    (1001) docker     (123)     6168 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/mlp.html
--rw-r--r--   0 runner    (1001) docker     (123)    84140 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/mlp.png
--rw-r--r--   0 runner    (1001) docker     (123)     6406 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/mlp2.html
--rw-r--r--   0 runner    (1001) docker     (123)    13875 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/mlp2.pdf
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/mlp2.png
--rw-r--r--   0 runner    (1001) docker     (123)     8963 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/ofg.html
--rw-r--r--   0 runner    (1001) docker     (123)     8115 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/examples/ofg2.html
--rw-r--r--   0 runner    (1001) docker     (123)   216173 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)     8566 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/d3viz/index_files/
--rw-r--r--   0 runner    (1001) docker     (123)    93049 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index_files/index_10_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    93049 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index_files/index_11_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index_files/index_24_0.png
--rw-r--r--   0 runner    (1001) docker     (123)    46699 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/d3viz/index_files/index_25_0.png
--rw-r--r--   0 runner    (1001) docker     (123)     1724 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/gradient.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/graph/
--rw-r--r--   0 runner    (1001) docker     (123)      797 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/features.rst
--rw-r--r--   0 runner    (1001) docker     (123)      906 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/fgraph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      361 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/graph.rst
--rw-r--r--   0 runner    (1001) docker     (123)      371 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      367 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/op.rst
--rw-r--r--   0 runner    (1001) docker     (123)      457 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/params_type.rst
--rw-r--r--   0 runner    (1001) docker     (123)      358 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/type.rst
--rw-r--r--   0 runner    (1001) docker     (123)      449 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/graph/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1297 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.460645 pytensor-2.8.11/doc/library/misc/
--rw-r--r--   0 runner    (1001) docker     (123)      419 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/misc/pkl_utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7209 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/printing.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.464643 pytensor-2.8.11/doc/library/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)      358 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/sandbox/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      477 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/sandbox/linalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)      399 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/sandbox/rng_mrg.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.464643 pytensor-2.8.11/doc/library/scalar/
--rw-r--r--   0 runner    (1001) docker     (123)      202 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/scalar/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    26866 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/scan.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.464643 pytensor-2.8.11/doc/library/sparse/
--rw-r--r--   0 runner    (1001) docker     (123)    11440 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/sparse/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      540 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/sparse/sandbox.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.464643 pytensor-2.8.11/doc/library/tensor/
--rw-r--r--   0 runner    (1001) docker     (123)    65563 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/basic.rst
--rw-r--r--   0 runner    (1001) docker     (123)      365 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/basic_opt.rst
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)    14117 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/bcast.svg
--rw-r--r--   0 runner    (1001) docker     (123)      404 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/elemwise.rst
--rw-r--r--   0 runner    (1001) docker     (123)      412 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/extra_ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1329 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/fft.rst
--rw-r--r--   0 runner    (1001) docker     (123)      658 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      768 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/io.rst
--rw-r--r--   0 runner    (1001) docker     (123)      440 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/math_opt.rst
--rw-r--r--   0 runner    (1001) docker     (123)      534 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/nlinalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)    24638 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/plot_fft.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.464643 pytensor-2.8.11/doc/library/tensor/random/
--rw-r--r--   0 runner    (1001) docker     (123)     4771 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/random/basic.rst
--rw-r--r--   0 runner    (1001) docker     (123)      467 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/random/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2172 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/random/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)      736 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/slinalg.rst
--rw-r--r--   0 runner    (1001) docker     (123)      386 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/tensor/utils.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1421 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/library/typed_list.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1842 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/links.rst
--rw-r--r--   0 runner    (1001) docker     (123)    12103 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/optimizations.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9038 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/pylintrc
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.468642 pytensor-2.8.11/doc/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)    12643 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/ccodegen.rst
--rw-r--r--   0 runner    (1001) docker     (123)      160 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/compilation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2914 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/debugging_with_stepmode.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5889 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/elemwise_compiler.rst
--rw-r--r--   0 runner    (1001) docker     (123)       83 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/function.rst
--rw-r--r--   0 runner    (1001) docker     (123)      166 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/functional.rst
--rw-r--r--   0 runner    (1001) docker     (123)    17348 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/how_to_make_ops.rst
--rw-r--r--   0 runner    (1001) docker     (123)      215 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      230 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/index2.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2360 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/interactive_debugger.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2622 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/logistic_regression_example.rst
--rw-r--r--   0 runner    (1001) docker     (123)      753 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/performance.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10492 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/randomnumbers.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4261 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/rethinkccodegen.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5960 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/sandbox.rst
--rw-r--r--   0 runner    (1001) docker     (123)      987 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/software.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6176 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/sparse.rst
--rw-r--r--   0 runner    (1001) docker     (123)      117 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/sandbox/tensoroptools.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.468642 pytensor-2.8.11/doc/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     3806 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/scripts/docgen.py
--rw-r--r--   0 runner    (1001) docker     (123)    11617 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/troubleshooting.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.468642 pytensor-2.8.11/doc/tutorial/
--rw-r--r--   0 runner    (1001) docker     (123)     7021 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/adding.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      381 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/adding_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)    11573 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/aliasing.rst
--rw-r--r--   0 runner    (1001) docker     (123)    28371 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/apply.png
--rw-r--r--   0 runner    (1001) docker     (123)    20340 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/apply.svg
--rw-r--r--   0 runner    (1001) docker     (123)    25804 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/bcast.png
--rw-r--r--   0 runner    (1001) docker     (123)     2453 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/broadcasting.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2898 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/conditions.rst
--rw-r--r--   0 runner    (1001) docker     (123)    23310 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/debug_faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5838 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/dlogistic.png
--rw-r--r--   0 runner    (1001) docker     (123)    18949 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/examples.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3235 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/faq_tutorial.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10875 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/gradients.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6004 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/loading_and_saving.rst
--rw-r--r--   0 runner    (1001) docker     (123)      483 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/logistic.gp
--rw-r--r--   0 runner    (1001) docker     (123)     4887 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/logistic.png
--rw-r--r--   0 runner    (1001) docker     (123)    12867 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/loop.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     2535 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/loop_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)    11762 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/modes.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     1911 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/modes_solution_1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2719 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/multi_cores.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4374 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/nan_tutorial.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.472640 pytensor-2.8.11/doc/tutorial/pics/
--rw-r--r--   0 runner    (1001) docker     (123)    55147 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/pics/d3viz.png
--rw-r--r--   0 runner    (1001) docker     (123)   106142 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_predict.png
--rw-r--r--   0 runner    (1001) docker     (123)   148860 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_prediction.png
--rw-r--r--   0 runner    (1001) docker     (123)   473403 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_train.png
--rw-r--r--   0 runner    (1001) docker     (123)     5023 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/printing_drawing.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3756 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/profiling.rst
--rw-r--r--   0 runner    (1001) docker     (123)      324 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/profiling_example.py
--rw-r--r--   0 runner    (1001) docker     (123)     1560 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/profiling_example_out.prof
--rw-r--r--   0 runner    (1001) docker     (123)     4011 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/shape_info.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8436 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/sparse.rst
--rw-r--r--   0 runner    (1001) docker     (123)       78 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/tutorial/symbolic_graphs.rst
--rw-r--r--   0 runner    (1001) docker     (123)      177 2022-12-14 07:21:20.000000 pytensor-2.8.11/doc/user_guide.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.500630 pytensor-2.8.11/pytensor/
--rw-r--r--   0 runner    (1001) docker     (123)     5881 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      503 2022-12-14 07:21:22.500630 pytensor-2.8.11/pytensor/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      258 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/assert_op.py
--rw-r--r--   0 runner    (1001) docker     (123)     6085 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/breakpoint.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/compile/
--rw-r--r--   0 runner    (1001) docker     (123)     1426 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    37639 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/builders.py
--rw-r--r--   0 runner    (1001) docker     (123)     9987 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/compiledir.py
--rw-r--r--   0 runner    (1001) docker     (123)     2047 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/compilelock.py
--rw-r--r--   0 runner    (1001) docker     (123)    85489 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/debugmode.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/compile/function/
--rw-r--r--   0 runner    (1001) docker     (123)    13384 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/function/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22142 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/function/pfunc.py
--rw-r--r--   0 runner    (1001) docker     (123)    71417 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/function/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     9108 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/io.py
--rw-r--r--   0 runner    (1001) docker     (123)    17859 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/mode.py
--rw-r--r--   0 runner    (1001) docker     (123)     3716 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/monitormode.py
--rw-r--r--   0 runner    (1001) docker     (123)     8365 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/nanguardmode.py
--rw-r--r--   0 runner    (1001) docker     (123)    10017 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)    59850 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/profiling.py
--rw-r--r--   0 runner    (1001) docker     (123)     7219 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/compile/sharedvalue.py
--rw-r--r--   0 runner    (1001) docker     (123)    46318 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/configdefaults.py
--rw-r--r--   0 runner    (1001) docker     (123)    22586 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/configparser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/d3viz/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/d3viz/css/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/css/d3-context-menu.css
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/css/d3viz.css
--rw-r--r--   0 runner    (1001) docker     (123)     3850 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/d3viz.py
--rw-r--r--   0 runner    (1001) docker     (123)    11915 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/formatting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/d3viz/js/
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/js/d3-context-menu.js
--rw-r--r--   0 runner    (1001) docker     (123)   151143 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/js/d3.v3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    23210 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/js/d3viz.js
--rw-r--r--   0 runner    (1001) docker     (123)    47566 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/js/dagre-d3.min.js
--rw-r--r--   0 runner    (1001) docker     (123)   115617 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/d3viz/js/graphlib-dot.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    86985 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/gradient.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/graph/
--rw-r--r--   0 runner    (1001) docker     (123)      564 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    63272 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    31388 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/destroyhandler.py
--rw-r--r--   0 runner    (1001) docker     (123)    26460 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/features.py
--rw-r--r--   0 runner    (1001) docker     (123)    35874 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/fg.py
--rw-r--r--   0 runner    (1001) docker     (123)      252 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/kanren.py
--rw-r--r--   0 runner    (1001) docker     (123)     1152 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/null_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    25095 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      801 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)      807 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/opt_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      794 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/optdb.py
--rw-r--r--   0 runner    (1001) docker     (123)     4823 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/replace.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.476639 pytensor-2.8.11/pytensor/graph/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   114284 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    19978 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/db.py
--rw-r--r--   0 runner    (1001) docker     (123)     3045 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/kanren.py
--rw-r--r--   0 runner    (1001) docker     (123)     7247 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/unify.py
--rw-r--r--   0 runner    (1001) docker     (123)     9170 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/rewriting/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7875 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/sched.py
--rw-r--r--   0 runner    (1001) docker     (123)      191 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/toolbox.py
--rw-r--r--   0 runner    (1001) docker     (123)     8925 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/type.py
--rw-r--r--   0 runner    (1001) docker     (123)      249 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/unify.py
--rw-r--r--   0 runner    (1001) docker     (123)    12130 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/graph/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    29132 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/ifelse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23914 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/c/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    72617 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/c/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)    35585 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/c_code/lazylinker_c.c
--rw-r--r--   0 runner    (1001) docker     (123)      722 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/c_code/pytensor_mod_helper.h
--rw-r--r--   0 runner    (1001) docker     (123)   112765 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/cmodule.py
--rw-r--r--   0 runner    (1001) docker     (123)     4193 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/cutils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/cvm.py
--rw-r--r--   0 runner    (1001) docker     (123)      402 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    19929 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/interface.py
--rw-r--r--   0 runner    (1001) docker     (123)     6657 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/lazylinker_c.py
--rw-r--r--   0 runner    (1001) docker     (123)    24729 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/op.py
--rw-r--r--   0 runner    (1001) docker     (123)    31631 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/params_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    26570 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/c/type.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/jax/
--rw-r--r--   0 runner    (1001) docker     (123)       47 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/jax/dispatch/
--rw-r--r--   0 runner    (1001) docker     (123)      551 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2723 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     2973 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)     3385 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     3080 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/nlinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)     9417 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/random.py
--rw-r--r--   0 runner    (1001) docker     (123)     3360 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/scalar.py
--rw-r--r--   0 runner    (1001) docker     (123)     5390 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/slinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)     2331 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2588 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/tensor_basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     7420 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/dispatch/test_subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)      202 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/jax_dispatch.py
--rw-r--r--   0 runner    (1001) docker     (123)      198 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/jax_linker.py
--rw-r--r--   0 runner    (1001) docker     (123)     3003 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/jax/linker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.480637 pytensor-2.8.11/pytensor/link/numba/
--rw-r--r--   0 runner    (1001) docker     (123)       51 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/link/numba/dispatch/
--rw-r--r--   0 runner    (1001) docker     (123)      488 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25013 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     7125 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/cython_support.py
--rw-r--r--   0 runner    (1001) docker     (123)    23397 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)    10592 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     4604 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/nlinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    12172 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/random.py
--rw-r--r--   0 runner    (1001) docker     (123)     9430 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/scalar.py
--rw-r--r--   0 runner    (1001) docker     (123)    14511 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     4076 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/sparse.py
--rw-r--r--   0 runner    (1001) docker     (123)     6402 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/dispatch/tensor_basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1662 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/numba/linker.py
--rw-r--r--   0 runner    (1001) docker     (123)    28759 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    50606 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/link/vm.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/misc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9697 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/check_blas.py
--rw-r--r--   0 runner    (1001) docker     (123)      606 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/check_blas_many.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2412 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/check_duplicate_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     2174 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/elemwise_openmp_speedup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1899 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/elemwise_time_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1347 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/frozendict.py
--rw-r--r--   0 runner    (1001) docker     (123)      617 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/latence_gpu_transfert.py
--rw-r--r--   0 runner    (1001) docker     (123)      922 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/may_share_memory.py
--rw-r--r--   0 runner    (1001) docker     (123)     7203 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/ordered_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     9764 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/pkl_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2294 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/misc/safe_asarray.py
--rw-r--r--   0 runner    (1001) docker     (123)    64131 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/printing.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     5832 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/raise_op.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3887 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/fourier.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/sandbox/linalg/
--rw-r--r--   0 runner    (1001) docker     (123)       62 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/linalg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6079 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/linalg/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     1463 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/minimal.py
--rw-r--r--   0 runner    (1001) docker     (123)    14806 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/multinomial.py
--rw-r--r--   0 runner    (1001) docker     (123)    48304 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/rng_mrg.py
--rw-r--r--   0 runner    (1001) docker     (123)     8105 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/samples_MRG31k3p_12_7_5.txt
--rw-r--r--   0 runner    (1001) docker     (123)      221 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sandbox/solve.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/scalar/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   139164 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      193 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/basic_scipy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3291 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/basic_sympy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/scalar/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)   126227 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/c_code/Faddeeva.cc
--rw-r--r--   0 runner    (1001) docker     (123)     2645 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/c_code/Faddeeva.hh
--rw-r--r--   0 runner    (1001) docker     (123)    16816 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/c_code/gamma.c
--rw-r--r--   0 runner    (1001) docker     (123)    40503 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/math.py
--rw-r--r--   0 runner    (1001) docker     (123)     1857 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scalar/sharedvar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.484636 pytensor-2.8.11/pytensor/scan/
--rw-r--r--   0 runner    (1001) docker     (123)     1947 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    50178 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.488634 pytensor-2.8.11/pytensor/scan/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)  1108978 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/c_code/scan_perform.c
--rw-r--r--   0 runner    (1001) docker     (123)     6769 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/checkpoints.py
--rw-r--r--   0 runner    (1001) docker     (123)   140589 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      232 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    95225 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)     3554 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/scan_perform_ext.py
--rw-r--r--   0 runner    (1001) docker     (123)    38104 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4603 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/scan/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.488634 pytensor-2.8.11/pytensor/sparse/
--rw-r--r--   0 runner    (1001) docker     (123)     1107 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   118078 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    76938 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/rewriting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.488634 pytensor-2.8.11/pytensor/sparse/sandbox/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/sandbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17516 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/sandbox/sp.py
--rw-r--r--   0 runner    (1001) docker     (123)     7238 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/sandbox/sp2.py
--rw-r--r--   0 runner    (1001) docker     (123)      833 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/sharedvar.py
--rw-r--r--   0 runner    (1001) docker     (123)     8093 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/type.py
--rw-r--r--   0 runner    (1001) docker     (123)      769 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/sparse/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.492632 pytensor-2.8.11/pytensor/tensor/
--rw-r--r--   0 runner    (1001) docker     (123)     4337 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   135754 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      473 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/basic_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    98921 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/blas.py
--rw-r--r--   0 runner    (1001) docker     (123)    26502 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/blas_c.py
--rw-r--r--   0 runner    (1001) docker     (123)    68058 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/blas_headers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2789 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/blas_scipy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.492632 pytensor-2.8.11/pytensor/tensor/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)      901 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/c_code/alt_blas_common.h
--rw-r--r--   0 runner    (1001) docker     (123)    16242 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/c_code/alt_blas_template.c
--rw-r--r--   0 runner    (1001) docker     (123)     2038 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/c_code/dimshuffle.c
--rw-r--r--   0 runner    (1001) docker     (123)    66765 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)    20872 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/elemwise_cgen.py
--rw-r--r--   0 runner    (1001) docker     (123)      362 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    58085 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     7605 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/fft.py
--rw-r--r--   0 runner    (1001) docker     (123)     6625 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/fourier.py
--rw-r--r--   0 runner    (1001) docker     (123)     7743 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/inplace.py
--rw-r--r--   0 runner    (1001) docker     (123)     7256 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/io.py
--rw-r--r--   0 runner    (1001) docker     (123)       76 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/linalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    92617 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/math.py
--rw-r--r--   0 runner    (1001) docker     (123)      253 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/math_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    22771 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nlinalg.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/nnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   139002 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/abstract_conv.py
--rw-r--r--   0 runner    (1001) docker     (123)    75888 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    35431 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/batchnorm.py
--rw-r--r--   0 runner    (1001) docker     (123)     8930 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/blocksparse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/nnet/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)    18976 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/c_code/corr3d_gemm.c
--rw-r--r--   0 runner    (1001) docker     (123)    26561 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/c_code/corr_gemm.c
--rw-r--r--   0 runner    (1001) docker     (123)     8195 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/c_code/ctc_wrapper.c
--rw-r--r--   0 runner    (1001) docker     (123)    94567 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/conv.py
--rw-r--r--   0 runner    (1001) docker     (123)     9932 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/conv3d2d.py
--rw-r--r--   0 runner    (1001) docker     (123)    40389 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/corr.py
--rw-r--r--   0 runner    (1001) docker     (123)    36183 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/corr3d.py
--rw-r--r--   0 runner    (1001) docker     (123)     8544 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/ctc.py
--rw-r--r--   0 runner    (1001) docker     (123)    35406 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/neighbours.py
--rw-r--r--   0 runner    (1001) docker     (123)      253 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    17357 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)     5240 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/nnet/sigm.py
--rw-r--r--   0 runner    (1001) docker     (123)      283 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/opt_uncanonicalize.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/random/
--rw-r--r--   0 runner    (1001) docker     (123)      275 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    61450 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    15041 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/op.py
--rw-r--r--   0 runner    (1001) docker     (123)      259 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/opt.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/random/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)      225 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12139 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1901 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/rewriting/jax.py
--rw-r--r--   0 runner    (1001) docker     (123)     6738 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     9080 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1317 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/random/var.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/rewriting/
--rw-r--r--   0 runner    (1001) docker     (123)      333 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    42758 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    39717 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/elemwise.py
--rw-r--r--   0 runner    (1001) docker     (123)     4858 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/extra_ops.py
--rw-r--r--   0 runner    (1001) docker     (123)   123017 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/math.py
--rw-r--r--   0 runner    (1001) docker     (123)    44824 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     6137 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/special.py
--rw-r--r--   0 runner    (1001) docker     (123)    63248 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     9516 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/rewriting/uncanonicalize.py
--rw-r--r--   0 runner    (1001) docker     (123)    33402 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/shape.py
--rw-r--r--   0 runner    (1001) docker     (123)     3870 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/sharedvar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.496631 pytensor-2.8.11/pytensor/tensor/signal/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/signal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3527 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/signal/conv.py
--rw-r--r--   0 runner    (1001) docker     (123)    97562 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/signal/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)    25097 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/slinalg.py
--rw-r--r--   0 runner    (1001) docker     (123)    17864 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)    27176 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/special.py
--rw-r--r--   0 runner    (1001) docker     (123)    91544 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/subtensor.py
--rw-r--r--   0 runner    (1001) docker     (123)      268 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/subtensor_opt.py
--rw-r--r--   0 runner    (1001) docker     (123)    41098 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4106 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/type_other.py
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    36043 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/var.py
--rw-r--r--   0 runner    (1001) docker     (123)     1835 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/tensor/xlogx.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.500630 pytensor-2.8.11/pytensor/typed_list/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/typed_list/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18248 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/typed_list/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)      786 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/typed_list/rewriting.py
--rw-r--r--   0 runner    (1001) docker     (123)     3877 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/typed_list/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2931 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/updates.py
--rw-r--r--   0 runner    (1001) docker     (123)    13641 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      578 2022-12-14 07:21:20.000000 pytensor-2.8.11/pytensor/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.472640 pytensor-2.8.11/pytensor.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2197 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    13007 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       60 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      116 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2022-12-14 07:21:22.000000 pytensor-2.8.11/pytensor.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      107 2022-12-14 07:21:20.000000 pytensor-2.8.11/requirements-rtd.txt
--rw-r--r--   0 runner    (1001) docker     (123)      218 2022-12-14 07:21:20.000000 pytensor-2.8.11/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3738 2022-12-14 07:21:22.500630 pytensor-2.8.11/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)      863 2022-12-14 07:21:20.000000 pytensor-2.8.11/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.448650 pytensor-2.8.11/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.448650 pytensor-2.8.11/tests/link/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.448650 pytensor-2.8.11/tests/link/c/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-14 07:21:22.500630 pytensor-2.8.11/tests/link/c/c_code/
--rw-r--r--   0 runner    (1001) docker     (123)      148 2022-12-14 07:21:20.000000 pytensor-2.8.11/tests/link/c/c_code/test_cenum.h
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2022-12-14 07:21:20.000000 pytensor-2.8.11/tests/link/c/c_code/test_quadratic_function.c
--rw-r--r--   0 runner    (1001) docker     (123)    81047 2022-12-14 07:21:20.000000 pytensor-2.8.11/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     2641 2023-01-10 16:00:00.000000 pytensor-2.9.1/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-01-10 16:00:00.000000 pytensor-2.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8437 2023-01-10 16:00:13.509126 pytensor-2.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3885 2023-01-10 16:00:00.000000 pytensor-2.9.1/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.465125 pytensor-2.9.1/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/bin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-01-10 16:00:00.000000 pytensor-2.9.1/bin/downstream_pr.sh
+-rw-r--r--   0 runner    (1001) docker     (123)       66 2023-01-10 16:00:00.000000 pytensor-2.9.1/bin/pytensor-cache
+-rw-r--r--   0 runner    (1001) docker     (123)     4173 2023-01-10 16:00:00.000000 pytensor-2.9.1/bin/pytensor_cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-01-10 16:00:00.000000 pytensor-2.9.1/bin/upstream_pr.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.465125 pytensor-2.9.1/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.465125 pytensor-2.9.1/doc/.templates/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/.templates/PLACEHOLDER
+-rw-r--r--   0 runner    (1001) docker     (123)     1409 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/.templates/layout.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2641 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/acknowledgement.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/bcast.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     8304 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/core_development_guide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/css.inc
+-rw-r--r--   0 runner    (1001) docker     (123)     8691 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/dev_start_guide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/environment.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.469126 pytensor-2.9.1/doc/extending/
+-rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/apply.png
+-rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/apply.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    32078 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/apply2.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    46694 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/creating_a_c_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6362 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/creating_a_numba_jax_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    33109 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/creating_an_op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    22706 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/ctype.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/extending_faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5509 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/extending_pytensor_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55789 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/graph_rewriting.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    13797 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/graphstructures.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1704 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9060 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/inplace.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    25030 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9624 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/other_ops.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.469126 pytensor-2.9.1/doc/extending/pics/
+-rw-r--r--   0 runner    (1001) docker     (123)    23471 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/pics/symbolic_graph_opt.png
+-rw-r--r--   0 runner    (1001) docker     (123)    62062 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/pics/symbolic_graph_unopt.png
+-rw-r--r--   0 runner    (1001) docker     (123)     4951 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/pipeline.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    17158 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/scan.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/tips.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    19721 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/type.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10092 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/unittest.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7618 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/extending/using_params.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6800 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/generate_dtype_tensor_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7126 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/glossary.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.469126 pytensor-2.9.1/doc/images/
+-rw-r--r--   0 runner    (1001) docker     (123)    94102 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/Elman_srnn.png
+-rw-r--r--   0 runner    (1001) docker     (123)     7491 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/PyTensor_RGB.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   102018 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/blocksparse.png
+-rw-r--r--   0 runner    (1001) docker     (123)    13780 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/lstm.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14362 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/lstm_memorycell.png
+-rw-r--r--   0 runner    (1001) docker     (123)   273555 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/talk2010.gif
+-rw-r--r--   0 runner    (1001) docker     (123)    12455 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/images/talk2010.png
+-rw-r--r--   0 runner    (1001) docker     (123)     3054 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/install.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.469126 pytensor-2.9.1/doc/internal/
+-rw-r--r--   0 runner    (1001) docker     (123)     1082 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/internal/how_to_release.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/internal/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2538 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/internal/metadocumentation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8042 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/introduction.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.469126 pytensor-2.9.1/doc/library/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/compile/
+-rw-r--r--   0 runner    (1001) docker     (123)     8382 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/debugmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8934 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/function.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      454 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    11853 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/io.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/mode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2053 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/nanguardmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      913 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/opfromgraph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      424 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/profilemode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3043 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/compile/shared.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    30830 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/config.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/d3viz/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/d3viz/examples/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.457126 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/css/
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/css/d3-context-menu.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/css/d3viz.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js
+-rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    23339 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3viz.js
+-rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)     6168 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/mlp.html
+-rw-r--r--   0 runner    (1001) docker     (123)    84140 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/mlp.png
+-rw-r--r--   0 runner    (1001) docker     (123)     6406 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/mlp2.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13875 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/mlp2.pdf
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/mlp2.png
+-rw-r--r--   0 runner    (1001) docker     (123)     8963 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/ofg.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8115 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/examples/ofg2.html
+-rw-r--r--   0 runner    (1001) docker     (123)   216173 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)     8566 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.473126 pytensor-2.9.1/doc/library/d3viz/index_files/
+-rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index_files/index_10_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    93049 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index_files/index_11_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index_files/index_24_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)    46699 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/d3viz/index_files/index_25_0.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1724 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/gradient.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/features.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      906 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/fgraph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/graph.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/op.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/type.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      449 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/graph/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1279 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)      419 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/misc/pkl_utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7209 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/printing.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)      331 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/sandbox/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      477 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/sandbox/linalg.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/scalar/
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/scalar/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    26866 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/scan.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/sparse/
+-rw-r--r--   0 runner    (1001) docker     (123)    11440 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/sparse/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      540 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/sparse/sandbox.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/tensor/
+-rw-r--r--   0 runner    (1001) docker     (123)    65486 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/basic.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/basic_opt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)    14117 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/bcast.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      325 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/conv.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/elemwise.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      412 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/extra_ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/fft.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      667 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/io.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      440 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/math_opt.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/nlinalg.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    24638 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/plot_fft.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.477126 pytensor-2.9.1/doc/library/tensor/random/
+-rw-r--r--   0 runner    (1001) docker     (123)     4771 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/random/basic.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/random/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2172 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/random/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      536 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/slinalg.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      386 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/tensor/utils.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1421 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/library/typed_list.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1842 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/links.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    12103 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/optimizations.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9038 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/pylintrc
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.481126 pytensor-2.9.1/doc/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)    12643 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/ccodegen.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/compilation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2914 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/debugging_with_stepmode.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5889 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/elemwise_compiler.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/function.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/functional.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    17348 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/how_to_make_ops.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/index2.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2360 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/interactive_debugger.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/logistic_regression_example.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      753 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/performance.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10492 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/randomnumbers.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4261 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/rethinkccodegen.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5960 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/sandbox.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      987 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/software.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6180 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/sparse.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/sandbox/tensoroptools.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.481126 pytensor-2.9.1/doc/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     3806 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/scripts/docgen.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11623 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/troubleshooting.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.485126 pytensor-2.9.1/doc/tutorial/
+-rw-r--r--   0 runner    (1001) docker     (123)     7021 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/adding.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      381 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/adding_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11573 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/aliasing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    28371 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/apply.png
+-rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/apply.svg
+-rw-r--r--   0 runner    (1001) docker     (123)    25804 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/bcast.png
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/broadcasting.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2898 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/conditions.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    23310 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/debug_faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5838 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/dlogistic.png
+-rw-r--r--   0 runner    (1001) docker     (123)    18949 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/examples.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3235 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/faq_tutorial.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10875 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/gradients.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6004 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/loading_and_saving.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/logistic.gp
+-rw-r--r--   0 runner    (1001) docker     (123)     4887 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/logistic.png
+-rw-r--r--   0 runner    (1001) docker     (123)    12867 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/loop.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2535 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/loop_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11762 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/modes.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1911 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/modes_solution_1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/multi_cores.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4374 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/nan_tutorial.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.485126 pytensor-2.9.1/doc/tutorial/pics/
+-rw-r--r--   0 runner    (1001) docker     (123)    55147 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/pics/d3viz.png
+-rw-r--r--   0 runner    (1001) docker     (123)   106142 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_predict.png
+-rw-r--r--   0 runner    (1001) docker     (123)   148860 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_prediction.png
+-rw-r--r--   0 runner    (1001) docker     (123)   473403 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_train.png
+-rw-r--r--   0 runner    (1001) docker     (123)     5023 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/printing_drawing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/profiling.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/profiling_example.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1560 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/profiling_example_out.prof
+-rw-r--r--   0 runner    (1001) docker     (123)     4011 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/shape_info.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8436 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/sparse.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/tutorial/symbolic_graphs.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      177 2023-01-10 16:00:00.000000 pytensor-2.9.1/doc/user_guide.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4900 2023-01-10 16:00:00.000000 pytensor-2.9.1/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/
+-rw-r--r--   0 runner    (1001) docker     (123)     5232 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      497 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6085 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/breakpoint.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.489126 pytensor-2.9.1/pytensor/compile/
+-rw-r--r--   0 runner    (1001) docker     (123)     1426 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37639 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/builders.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9987 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/compiledir.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2047 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/compilelock.py
+-rw-r--r--   0 runner    (1001) docker     (123)    85489 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/debugmode.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.489126 pytensor-2.9.1/pytensor/compile/function/
+-rw-r--r--   0 runner    (1001) docker     (123)    13384 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/function/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22142 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/function/pfunc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    71316 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/function/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9108 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17859 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/mode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3716 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/monitormode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8365 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/nanguardmode.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10017 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59312 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/profiling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7219 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/compile/sharedvalue.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46035 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/configdefaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18973 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/configparser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.489126 pytensor-2.9.1/pytensor/d3viz/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.489126 pytensor-2.9.1/pytensor/d3viz/css/
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/css/d3-context-menu.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/css/d3viz.css
+-rw-r--r--   0 runner    (1001) docker     (123)     3850 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/d3viz.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11915 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/formatting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.489126 pytensor-2.9.1/pytensor/d3viz/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/js/d3-context-menu.js
+-rw-r--r--   0 runner    (1001) docker     (123)   151143 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/js/d3.v3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    23210 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/js/d3viz.js
+-rw-r--r--   0 runner    (1001) docker     (123)    47566 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/js/dagre-d3.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)   115617 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/d3viz/js/graphlib-dot.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    85285 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/gradient.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)      564 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63243 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31388 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/destroyhandler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26460 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35874 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/fg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/null_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25133 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4823 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/replace.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/graph/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   110119 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18964 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/db.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3045 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/kanren.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7247 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/unify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8272 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/rewriting/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8925 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10905 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/graph/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29132 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/ifelse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/link/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23914 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/link/c/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    72617 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/link/c/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)    35585 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/c_code/lazylinker_c.c
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/c_code/pytensor_mod_helper.h
+-rw-r--r--   0 runner    (1001) docker     (123)   112765 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/cmodule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4193 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/cutils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/cvm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      402 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19929 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/interface.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6657 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/lazylinker_c.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24729 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31631 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/params_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26570 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/c/type.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.493126 pytensor-2.9.1/pytensor/link/jax/
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/link/jax/dispatch/
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2723 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3385 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3238 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/nlinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10325 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/scalar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5390 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/slinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2331 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/tensor_basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7420 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/dispatch/test_subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3003 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/jax/linker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/link/numba/
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/link/numba/dispatch/
+-rw-r--r--   0 runner    (1001) docker     (123)      488 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24888 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7125 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/cython_support.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30536 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9779 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/elemwise_codegen.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10624 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5124 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/nlinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12172 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9495 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/scalar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14881 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4076 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/sparse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6402 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/dispatch/tensor_basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/numba/linker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28759 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50606 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/link/vm.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9697 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/check_blas.py
+-rw-r--r--   0 runner    (1001) docker     (123)      606 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/check_blas_many.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2412 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/check_duplicate_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2174 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/elemwise_openmp_speedup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1899 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/elemwise_time_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/frozendict.py
+-rw-r--r--   0 runner    (1001) docker     (123)      922 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/may_share_memory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7203 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/ordered_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9790 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/pkl_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2294 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/misc/safe_asarray.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63879 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/printing.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     5832 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/raise_op.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sandbox/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.497126 pytensor-2.9.1/pytensor/sandbox/linalg/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sandbox/linalg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6079 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sandbox/linalg/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1463 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sandbox/minimal.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.501126 pytensor-2.9.1/pytensor/scalar/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   138467 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.501126 pytensor-2.9.1/pytensor/scalar/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)   126227 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/c_code/Faddeeva.cc
+-rw-r--r--   0 runner    (1001) docker     (123)     2645 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/c_code/Faddeeva.hh
+-rw-r--r--   0 runner    (1001) docker     (123)    16816 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/c_code/gamma.c
+-rw-r--r--   0 runner    (1001) docker     (123)    45915 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scalar/sharedvar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.501126 pytensor-2.9.1/pytensor/scan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1947 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49962 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6769 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/checkpoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)   140597 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/op.py
+-rw-r--r--   0 runner    (1001) docker     (123)    95225 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/rewriting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23998 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/scan_perform.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)      480 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/scan_perform_ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38104 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4603 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/scan/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.501126 pytensor-2.9.1/pytensor/sparse/
+-rw-r--r--   0 runner    (1001) docker     (123)     1107 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   118230 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    77305 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/rewriting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.501126 pytensor-2.9.1/pytensor/sparse/sandbox/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/sandbox/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17516 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/sandbox/sp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7238 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/sandbox/sp2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/sharedvar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7989 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      769 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/sparse/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.505126 pytensor-2.9.1/pytensor/tensor/
+-rw-r--r--   0 runner    (1001) docker     (123)     4318 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   135904 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    98939 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/blas.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26502 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/blas_c.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68058 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/blas_headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/blas_scipy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.505126 pytensor-2.9.1/pytensor/tensor/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)      901 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/c_code/alt_blas_common.h
+-rw-r--r--   0 runner    (1001) docker     (123)    16242 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/c_code/alt_blas_template.c
+-rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/c_code/dimshuffle.c
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.505126 pytensor-2.9.1/pytensor/tensor/conv/
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/conv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   137706 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/conv/abstract_conv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66771 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20872 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/elemwise_cgen.py
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59039 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7605 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/fft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6625 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/fourier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7837 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/inplace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2678 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/linalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    92091 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23564 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/nlinalg.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/tensor/random/
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61450 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15041 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/op.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/tensor/random/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)      225 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12139 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1901 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/rewriting/jax.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6738 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9080 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/random/var.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/tensor/rewriting/
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42067 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39717 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/elemwise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4858 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/extra_ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)   123022 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44824 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6137 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/special.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63182 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9516 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/rewriting/uncanonicalize.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33408 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3870 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/sharedvar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24096 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/slinalg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17864 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27450 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/special.py
+-rw-r--r--   0 runner    (1001) docker     (123)    91544 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/subtensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45991 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4106 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/type_other.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36157 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/var.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1835 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/tensor/xlogx.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/pytensor/typed_list/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/typed_list/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18332 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/typed_list/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)      786 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/typed_list/rewriting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3877 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/typed_list/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2931 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/updates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12304 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-01-10 16:00:00.000000 pytensor-2.9.1/pytensor/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.485126 pytensor-2.9.1/pytensor.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8437 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    11788 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-01-10 16:00:13.000000 pytensor-2.9.1/pytensor.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-01-10 16:00:00.000000 pytensor-2.9.1/scripts/mypy-failing.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     5576 2023-01-10 16:00:00.000000 pytensor-2.9.1/scripts/run_mypy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      774 2023-01-10 16:00:13.509126 pytensor-2.9.1/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1121 2023-01-10 16:00:00.000000 pytensor-2.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.461125 pytensor-2.9.1/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.461125 pytensor-2.9.1/tests/link/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.461125 pytensor-2.9.1/tests/link/c/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/tests/link/c/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-01-10 16:00:00.000000 pytensor-2.9.1/tests/link/c/c_code/test_cenum.h
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-01-10 16:00:00.000000 pytensor-2.9.1/tests/link/c/c_code/test_quadratic_function.c
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.461125 pytensor-2.9.1/tests/tensor/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.461125 pytensor-2.9.1/tests/tensor/conv/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-10 16:00:13.509126 pytensor-2.9.1/tests/tensor/conv/c_code/
+-rw-r--r--   0 runner    (1001) docker     (123)    18976 2023-01-10 16:00:00.000000 pytensor-2.9.1/tests/tensor/conv/c_code/corr3d_gemm.c
+-rw-r--r--   0 runner    (1001) docker     (123)    26561 2023-01-10 16:00:00.000000 pytensor-2.9.1/tests/tensor/conv/c_code/corr_gemm.c
+-rw-r--r--   0 runner    (1001) docker     (123)    83607 2023-01-10 16:00:00.000000 pytensor-2.9.1/versioneer.py
```

### Comparing `pytensor-2.8.11/LICENSE.txt` & `pytensor-2.9.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/README.rst` & `pytensor-2.9.1/README.rst`

 * *Files 4% similar despite different names*

```diff
@@ -1,7 +1,12 @@
+.. image:: https://cdn.rawgit.com/pymc-devs/pytensor/main/doc/images/PyTensor_RGB.svg
+    :height: 100px
+    :alt: PyTensor logo
+    :align: center
+
 |Tests Status| |Coverage|
 
 |Project Name| is a fork of `Aesara <https://github.com/aesara-devs/aesara>`__ -- a Python library that allows one to define, optimize, and
 efficiently evaluate mathematical expressions involving multi-dimensional arrays.
 
 Features
 ========
```

### Comparing `pytensor-2.8.11/bin/downstream_pr.sh` & `pytensor-2.9.1/bin/downstream_pr.sh`

 * *Files 13% similar despite different names*

```diff
@@ -39,8 +39,8 @@
 
 echo "Running pre-commit"
 pre-commit run --all
 
 git push origin downstream_$1
 # get the informative title
 title=$(curl https://api.github.com/repos/aesara-devs/aesara/pulls/$1 2>/dev/null | jq '.title')
-gh pr create --repo pymc-devs/pytensor --title "Downstreaming Aesara PR $1: $title" --body "Downstreaming https://github.com/aesara-devs/aesara/pull/$1. PR port done by downstream_pr.sh script."
+gh pr create --repo pymc-devs/pytensor --label "aesara downstream" --title "🔄 From Aesara: $1: $title" --body "Downstreaming https://github.com/aesara-devs/aesara/pull/$1. PR port done by downstream_pr.sh script."
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `pytensor-2.8.11/bin/pytensor_cache.py` & `pytensor-2.9.1/bin/pytensor_cache.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/bin/upstream_pr.sh` & `pytensor-2.9.1/bin/upstream_pr.sh`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/.templates/layout.html` & `pytensor-2.9.1/doc/.templates/layout.html`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/LICENSE.txt` & `pytensor-2.9.1/doc/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/acknowledgement.rst` & `pytensor-2.9.1/doc/acknowledgement.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/bcast.png` & `pytensor-2.9.1/doc/bcast.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/bcast.svg` & `pytensor-2.9.1/doc/bcast.svg`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/conf.py` & `pytensor-2.9.1/doc/conf.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,14 +13,15 @@
 
 # If your extensions are in another directory, add it here. If the directory
 # is relative to the documentation root, use os.path.abspath to make it
 # absolute, like shown here.
 # sys.path.append(os.path.abspath('some/directory'))
 
 import os
+import sys
 import pytensor
 
 # General configuration
 # ---------------------
 
 # Add any Sphinx extension module names here, as strings. They can be
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
@@ -56,15 +57,15 @@
 # other places throughout the built documents.
 #
 
 version = pytensor.__version__
 if os.environ.get("READTHEDOCS", False):
     rtd_version = os.environ.get("READTHEDOCS_VERSION", "")
     if rtd_version.lower() == "stable":
-        version = pymc.__version__.split("+")[0]
+        version = pytensor.__version__.split("+")[0]
     elif rtd_version.lower() == "latest":
         version = "dev"
     else:
         version = rtd_version
 else:
     rtd_version = "local"
 # The full version, including alpha/beta/rc tags.
@@ -109,17 +110,18 @@
 # must exist either in Sphinx' static/ path, or in one of the custom paths
 # given in html_static_path.
 # html_style = 'default.css'
 # html_theme = 'sphinxdoc'
 
 # html4_writer added to Fix colon & whitespace misalignment
 # https://github.com/readthedocs/sphinx_rtd_theme/issues/766#issuecomment-513852197
-html4_writer = True
+# https://github.com/readthedocs/sphinx_rtd_theme/issues/766#issuecomment-629666319
+# html4_writer = False
 
-html_logo = "images/pytensor_logo.svg"
+html_logo = "images/PyTensor_RGB.svg"
 html_theme = "pymc_sphinx_theme"
 html_theme_options = {
     "use_search_override": False,
 }
 html_context = {
     "github_user": "pymc-devs",
     "github_repo": "pytensor",
@@ -134,15 +136,15 @@
 # html_title = None
 
 # A shorter title for the navigation bar.  Default is the same as html_title.
 # html_short_title = None
 
 # The name of an image file (within the static path) to place at the top of
 # the sidebar.
-# html_logo = 'images/pytensor_logo.svg'
+# html_logo = 'images/PyTensor_RGB.svg'
 
 # The name of an image file (within the static path) to use as favicon of the
 # docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
 # pixels large.
 # html_favicon = None
 
 # Add any paths that contain custom static files (such as style sheets) here,
@@ -238,15 +240,15 @@
 # [howto/manual]).
 latex_documents = [
     ("index", "pytensor.tex", "PyTensor Documentation", "PyTensor Developers", "manual"),
 ]
 
 # The name of an image file (relative to this directory) to place at the top of
 # the title page.
-# latex_logo = 'images/pytensor_logo.svg'
+# latex_logo = 'images/PyTensor_RGB.svg'
 
 # For "manual" documents, if this is true, then toplevel headings are parts,
 # not chapters.
 # latex_use_parts = False
 
 # Documents to append as an appendix to all manuals.
 # latex_appendices = []
```

### Comparing `pytensor-2.8.11/doc/core_development_guide.rst` & `pytensor-2.9.1/doc/core_development_guide.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/dev_start_guide.rst` & `pytensor-2.9.1/doc/dev_start_guide.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/apply.png` & `pytensor-2.9.1/doc/extending/apply.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/apply.svg` & `pytensor-2.9.1/doc/extending/apply.svg`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/apply2.svg` & `pytensor-2.9.1/doc/extending/apply2.svg`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/creating_a_c_op.rst` & `pytensor-2.9.1/doc/extending/creating_a_c_op.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/creating_a_numba_jax_op.rst` & `pytensor-2.9.1/doc/extending/creating_a_numba_jax_op.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/creating_an_op.rst` & `pytensor-2.9.1/doc/extending/creating_an_op.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/ctype.rst` & `pytensor-2.9.1/doc/extending/ctype.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/extending_faq.rst` & `pytensor-2.9.1/doc/extending/extending_faq.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/extending_pytensor_solution_1.py` & `pytensor-2.9.1/doc/extending/extending_pytensor_solution_1.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/graph_rewriting.rst` & `pytensor-2.9.1/doc/extending/graph_rewriting.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/graphstructures.rst` & `pytensor-2.9.1/doc/extending/graphstructures.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/index.rst` & `pytensor-2.9.1/doc/extending/index.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/inplace.rst` & `pytensor-2.9.1/doc/extending/inplace.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/op.rst` & `pytensor-2.9.1/doc/extending/op.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/other_ops.rst` & `pytensor-2.9.1/doc/extending/other_ops.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/pics/symbolic_graph_opt.png` & `pytensor-2.9.1/doc/extending/pics/symbolic_graph_opt.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/pics/symbolic_graph_unopt.png` & `pytensor-2.9.1/doc/extending/pics/symbolic_graph_unopt.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/pipeline.rst` & `pytensor-2.9.1/doc/extending/pipeline.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/scan.rst` & `pytensor-2.9.1/doc/extending/scan.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/tips.rst` & `pytensor-2.9.1/doc/extending/tips.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/type.rst` & `pytensor-2.9.1/doc/extending/type.rst`

 * *Files 0% similar despite different names*

```diff
@@ -320,16 +320,16 @@
 Additional definitions
 ----------------------
 
 For certain mechanisms, you can register functions and other such
 things to plus your type into pytensor's mechanisms.  These are optional
 but will allow people to use you type with familiar interfaces.
 
-`transfer`
-~~~~~~~~~~
+**`transfer`**
+
 
 To plug in additional options for the transfer target, define a
 function which takes an PyTensor variable and a target argument and
 returns eitehr a new transferred variable (which can be the same as
 the input if no transfer is necessary) or returns None if the transfer
 can't be done.
```

### Comparing `pytensor-2.8.11/doc/extending/unittest.rst` & `pytensor-2.9.1/doc/extending/unittest.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/extending/using_params.rst` & `pytensor-2.9.1/doc/extending/using_params.rst`

 * *Files 2% similar despite different names*

```diff
@@ -72,15 +72,14 @@
 attribute :attr:`params_type` to an instance of your params Type.
 
 .. note::
 
    If you want to have multiple parameters, PyTensor provides the convenient class
    :class:`pytensor.link.c.params_type.ParamsType` that allows to bundle many parameters into
    one object that will be available in both Python (as a Python object) and C code (as a struct).
-   See :ref:`ParamsType tutorial and API documentation <libdoc_graph_params_type>` for more infos.
 
 For example if we decide to use an int as the params the following
 would be appropriate:
 
 .. code-block:: python
 
    class MyOp(Op):
```

### Comparing `pytensor-2.8.11/doc/faq.rst` & `pytensor-2.9.1/doc/faq.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/generate_dtype_tensor_table.py` & `pytensor-2.9.1/doc/generate_dtype_tensor_table.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/glossary.rst` & `pytensor-2.9.1/doc/glossary.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/Elman_srnn.png` & `pytensor-2.9.1/doc/images/Elman_srnn.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/blocksparse.png` & `pytensor-2.9.1/doc/images/blocksparse.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/lstm.png` & `pytensor-2.9.1/doc/images/lstm.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/lstm_memorycell.png` & `pytensor-2.9.1/doc/images/lstm_memorycell.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/talk2010.gif` & `pytensor-2.9.1/doc/images/talk2010.gif`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/images/talk2010.png` & `pytensor-2.9.1/doc/images/talk2010.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/index.rst` & `pytensor-2.9.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/install.rst` & `pytensor-2.9.1/doc/install.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/internal/how_to_release.rst` & `pytensor-2.9.1/doc/internal/how_to_release.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/internal/metadocumentation.rst` & `pytensor-2.9.1/doc/internal/metadocumentation.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/introduction.rst` & `pytensor-2.9.1/doc/introduction.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/compile/debugmode.rst` & `pytensor-2.9.1/doc/library/compile/debugmode.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/compile/function.rst` & `pytensor-2.9.1/doc/library/compile/function.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/compile/io.rst` & `pytensor-2.9.1/doc/library/compile/io.rst`

 * *Files 0% similar despite different names*

```diff
@@ -2,17 +2,17 @@
 .. note::
 
     ***TODO*** Freshen up this old documentation
 
 
 .. _function_inputs:
 
-===========================================
+============================================
 :mod:`io` - defines pytensor.function [TODO]
-===========================================
+============================================
 
 .. module:: pytensor.compile.io
    :platform: Unix, Windows
    :synopsis: defines In and Out
 .. moduleauthor:: LISA
```

### Comparing `pytensor-2.8.11/doc/library/compile/mode.rst` & `pytensor-2.9.1/doc/library/compile/mode.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/compile/nanguardmode.rst` & `pytensor-2.9.1/doc/library/compile/nanguardmode.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/compile/opfromgraph.rst` & `pytensor-2.9.1/doc/library/compile/opfromgraph.rst`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 :orphan:
 
 .. _opfromgraph:
 
-============
+=============
 `OpFromGraph`
-============
+=============
 
 This page describes :class:`pytensor.compile.builders.OpFromGraph
 <pytensor.compile.builders.OpFromGraph>`, an `Op` constructor that allows one to
 encapsulate an PyTensor graph in a single `Op`.
 
 This can be used to encapsulate some functionality in one block. It is
 useful to scale PyTensor compilation for regular bigger graphs when we
```

### Comparing `pytensor-2.8.11/doc/library/compile/shared.rst` & `pytensor-2.9.1/doc/library/compile/shared.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/config.rst` & `pytensor-2.9.1/doc/library/config.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/css/d3viz.css` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/css/d3viz.css`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3-context-menu.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3.v3.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/d3viz.js` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/d3viz.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/dagre-d3.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js` & `pytensor-2.9.1/doc/library/d3viz/examples/d3viz/js/graphlib-dot.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/mlp.html` & `pytensor-2.9.1/doc/library/d3viz/examples/mlp.html`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/mlp.png` & `pytensor-2.9.1/doc/library/d3viz/examples/mlp.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/mlp2.html` & `pytensor-2.9.1/doc/library/d3viz/examples/mlp2.html`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/mlp2.pdf` & `pytensor-2.9.1/doc/library/d3viz/examples/mlp2.pdf`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/mlp2.png` & `pytensor-2.9.1/doc/library/d3viz/examples/mlp2.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/ofg.html` & `pytensor-2.9.1/doc/library/d3viz/examples/ofg.html`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/examples/ofg2.html` & `pytensor-2.9.1/doc/library/d3viz/examples/ofg2.html`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index.ipynb` & `pytensor-2.9.1/doc/library/d3viz/index.ipynb`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index.rst` & `pytensor-2.9.1/doc/library/d3viz/index.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index_files/index_10_0.png` & `pytensor-2.9.1/doc/library/d3viz/index_files/index_10_0.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index_files/index_11_0.png` & `pytensor-2.9.1/doc/library/d3viz/index_files/index_11_0.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index_files/index_24_0.png` & `pytensor-2.9.1/doc/library/d3viz/index_files/index_24_0.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/d3viz/index_files/index_25_0.png` & `pytensor-2.9.1/doc/library/d3viz/index_files/index_25_0.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/gradient.rst` & `pytensor-2.9.1/doc/library/gradient.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/graph/features.rst` & `pytensor-2.9.1/doc/library/graph/features.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/graph/fgraph.rst` & `pytensor-2.9.1/doc/library/graph/fgraph.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/index.rst` & `pytensor-2.9.1/doc/library/index.rst`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,14 @@
 .. toctree::
    :maxdepth: 1
 
    compile/index
    config
    d3viz/index
    graph/index
-   gpuarray/index
    gradient
    misc/pkl_utils
    printing
    sandbox/index
    scalar/index
    scan
    sparse/index
```

### Comparing `pytensor-2.8.11/doc/library/printing.rst` & `pytensor-2.9.1/doc/library/printing.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/scan.rst` & `pytensor-2.9.1/doc/library/scan.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/sparse/index.rst` & `pytensor-2.9.1/doc/library/sparse/index.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/sparse/sandbox.rst` & `pytensor-2.9.1/doc/library/sparse/sandbox.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/basic.rst` & `pytensor-2.9.1/doc/library/tensor/basic.rst`

 * *Files 0% similar despite different names*

```diff
@@ -553,14 +553,15 @@
     .. method:: {any,all}(axis=None, keepdims=False)
     .. method:: {sum,prod,mean}(axis=None, dtype=None, keepdims=False, acc_dtype=None)
     .. method:: {var,std,min,max,argmin,argmax}(axis=None, keepdims=False),
     .. method:: diagonal(offset=0, axis1=0, axis2=1)
     .. method:: astype(dtype)
     .. method:: take(indices, axis=None, mode='raise')
     .. method:: copy()
+       :noindex:
 
         Return a new symbolic variable that is a copy of the variable. Does not copy the tag.
 
     .. method:: norm(L, axis=None)
     .. method:: nonzero(self, return_matrix=False)
        :noindex:
     .. method:: nonzero_values(self)
@@ -663,19 +664,15 @@
     >>> pytensor.tensor.shape_padaxis(tensor, axis=1)
     InplaceDimShuffle{0,x,1,2}.0
     >>> pytensor.tensor.shape_padaxis(tensor, axis=3)
     InplaceDimShuffle{0,1,2,x}.0
     >>> pytensor.tensor.shape_padaxis(tensor, axis=-1)
     InplaceDimShuffle{0,1,2,x}.0
 
-.. autofunction:: unbroadcast(x, *axes)
-
-.. autofunction:: addbroadcast(x, *axes)
-
-.. autofunction:: patternbroadcast(x, broadcastable)
+.. autofunction:: specify_shape(x, shape)
 
 .. function:: flatten(x, ndim=1)
 
     Similar to :func:`reshape`, but the shape is inferred from the shape of `x`.
 
     :param x: variable to be flattened
     :type x: any `TensorVariable` (or compatible)
```

### Comparing `pytensor-2.8.11/doc/library/tensor/bcast.png` & `pytensor-2.9.1/doc/library/tensor/bcast.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/bcast.svg` & `pytensor-2.9.1/doc/library/tensor/bcast.svg`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/fft.rst` & `pytensor-2.9.1/doc/library/tensor/fft.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/index.rst` & `pytensor-2.9.1/doc/library/tensor/index.rst`

 * *Files 1% similar despite different names*

```diff
@@ -22,9 +22,10 @@
     utils
     elemwise
     extra_ops
     io
     slinalg
     nlinalg
     fft
+    conv
     math_opt
     basic_opt
```

### Comparing `pytensor-2.8.11/doc/library/tensor/io.rst` & `pytensor-2.9.1/doc/library/tensor/io.rst`

 * *Files 16% similar despite different names*

```diff
@@ -8,17 +8,12 @@
 .. moduleauthor:: LISA
 
 File operation
 ==============
 
 - Load from disk with the function :func:`load <pytensor.tensor.io.load>` and its associated op :class:`LoadFromDisk <pytensor.tensor.io.LoadFromDisk>`
 
-MPI operation
-=============
-- Non-blocking transfer: :func:`isend <pytensor.tensor.io.isend>` and :func:`irecv <pytensor.tensor.io.irecv>`.
-- Blocking transfer: :func:`send <pytensor.tensor.io.send>` and :func:`recv <pytensor.tensor.io.recv>`
-
 Details
 =======
 
 .. automodule:: pytensor.tensor.io
     :members:
```

### Comparing `pytensor-2.8.11/doc/library/tensor/nlinalg.rst` & `pytensor-2.9.1/doc/library/tensor/nlinalg.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/plot_fft.png` & `pytensor-2.9.1/doc/library/tensor/plot_fft.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/random/basic.rst` & `pytensor-2.9.1/doc/library/tensor/random/basic.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/random/utils.rst` & `pytensor-2.9.1/doc/library/tensor/random/utils.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/library/tensor/slinalg.rst` & `pytensor-2.9.1/doc/library/tensor/slinalg.rst`

 * *Files 19% similar despite different names*

```diff
@@ -16,12 +16,8 @@
    This module is not imported by default. You need to import it to use it.
 
 API
 ===
 
 .. automodule:: pytensor.tensor.slinalg
     :members:
-    :exclude-members: solve, solve_lower_triangular, solve_upper_triangular
 
-.. autofunction:: solve(a, b)
-.. autofunction:: solve_lower_triangular(a, b)
-.. autofunction:: solve_upper_triangular(a, b)
```

### Comparing `pytensor-2.8.11/doc/library/typed_list.rst` & `pytensor-2.9.1/doc/library/typed_list.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/links.rst` & `pytensor-2.9.1/doc/links.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/optimizations.rst` & `pytensor-2.9.1/doc/optimizations.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/pylintrc` & `pytensor-2.9.1/doc/pylintrc`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/ccodegen.rst` & `pytensor-2.9.1/doc/sandbox/ccodegen.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/debugging_with_stepmode.rst` & `pytensor-2.9.1/doc/sandbox/debugging_with_stepmode.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/elemwise_compiler.rst` & `pytensor-2.9.1/doc/sandbox/elemwise_compiler.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/how_to_make_ops.rst` & `pytensor-2.9.1/doc/sandbox/how_to_make_ops.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/interactive_debugger.rst` & `pytensor-2.9.1/doc/sandbox/interactive_debugger.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/logistic_regression_example.rst` & `pytensor-2.9.1/doc/sandbox/logistic_regression_example.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/performance.rst` & `pytensor-2.9.1/doc/sandbox/performance.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/randomnumbers.rst` & `pytensor-2.9.1/doc/sandbox/randomnumbers.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/rethinkccodegen.rst` & `pytensor-2.9.1/doc/sandbox/rethinkccodegen.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/sandbox.rst` & `pytensor-2.9.1/doc/sandbox/sandbox.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/software.rst` & `pytensor-2.9.1/doc/sandbox/software.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/sandbox/sparse.rst` & `pytensor-2.9.1/doc/sandbox/sparse.rst`

 * *Files 0% similar despite different names*

```diff
@@ -116,15 +116,15 @@
     computations on sparse matrices." (Nathan Bell on scipy mailing list)
 
 Misc
 ----
 The sparse equivalent of `dmatrix` is `csc_matrix` and `csr_matrix`.
 
 :class:`~pytensor.sparse.basic.Dot` vs. :class:`~pytensor.sparse.basic.StructuredDot`
----------------------------------------------------------------------------------
+-------------------------------------------------------------------------------------
 
 Often when you use a sparse matrix it is because there is a meaning to the
 structure of non-zeros. The gradient on terms outside that structure
 has no meaning, so it is computationally efficient not to compute them.
 
 `StructuredDot` is when you want the gradient to have zeroes corresponding to
 the sparse entries in the matrix.
```

### Comparing `pytensor-2.8.11/doc/scripts/docgen.py` & `pytensor-2.9.1/doc/scripts/docgen.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/troubleshooting.rst` & `pytensor-2.9.1/doc/troubleshooting.rst`

 * *Files 0% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 - :ref:`float64_output`
 - :ref:`test_pytensor`
 - :ref:`test_BLAS`
 
 .. _network_error_proxy:
 
 Why do I get a network error when I install PyTensor
-^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
 If you are behind a proxy, you must do some extra configuration steps
 before starting the installation. You must set the environment
 variable ``http_proxy`` to the proxy address. Using bash this is
 accomplished with the command
 ``export http_proxy="http://user:pass@my.site:port/"``
 You can also provide the ``--proxy=[user:pass@]url:port`` parameter
@@ -65,26 +65,26 @@
 memory fragmentation which means that a continugous block of memory of
 sufficient capacity may not be available even if the free memory overall is
 large enough.
 
 .. _float64_output:
 
 pytensor.function returns a float64 when the inputs are float32 and int{32, 64}
-^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
 It should be noted that using float32 and int{32, 64} together
 inside a function would provide float64 as output.
 
 To help you find where float64 are created, see the
 :attr:`warn_float64` PyTensor flag.
 
 .. _test_pytensor:
 
 How to test that PyTensor works properly
-^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
 An easy way to check something that could be wrong is by making sure ``PYTENSOR_FLAGS``
 have the desired values as well as the ``~/.pytensorrc``
 
 Also, check the following outputs :
 
 .. code-block:: bash
```

### Comparing `pytensor-2.8.11/doc/tutorial/adding.rst` & `pytensor-2.9.1/doc/tutorial/adding.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/aliasing.rst` & `pytensor-2.9.1/doc/tutorial/aliasing.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/apply.png` & `pytensor-2.9.1/doc/tutorial/apply.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/apply.svg` & `pytensor-2.9.1/doc/tutorial/apply.svg`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/bcast.png` & `pytensor-2.9.1/doc/tutorial/bcast.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/broadcasting.rst` & `pytensor-2.9.1/doc/tutorial/broadcasting.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/conditions.rst` & `pytensor-2.9.1/doc/tutorial/conditions.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/debug_faq.rst` & `pytensor-2.9.1/doc/tutorial/debug_faq.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/dlogistic.png` & `pytensor-2.9.1/doc/tutorial/dlogistic.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/examples.rst` & `pytensor-2.9.1/doc/tutorial/examples.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/faq_tutorial.rst` & `pytensor-2.9.1/doc/tutorial/faq_tutorial.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/gradients.rst` & `pytensor-2.9.1/doc/tutorial/gradients.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/index.rst` & `pytensor-2.9.1/doc/tutorial/index.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/loading_and_saving.rst` & `pytensor-2.9.1/doc/tutorial/loading_and_saving.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/logistic.png` & `pytensor-2.9.1/doc/tutorial/logistic.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/loop.rst` & `pytensor-2.9.1/doc/tutorial/loop.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/loop_solution_1.py` & `pytensor-2.9.1/doc/tutorial/loop_solution_1.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/modes.rst` & `pytensor-2.9.1/doc/tutorial/modes.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/modes_solution_1.py` & `pytensor-2.9.1/doc/tutorial/modes_solution_1.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/multi_cores.rst` & `pytensor-2.9.1/doc/tutorial/multi_cores.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/nan_tutorial.rst` & `pytensor-2.9.1/doc/tutorial/nan_tutorial.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/pics/d3viz.png` & `pytensor-2.9.1/doc/tutorial/pics/d3viz.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_predict.png` & `pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_predict.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_prediction.png` & `pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_prediction.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/pics/logreg_pydotprint_train.png` & `pytensor-2.9.1/doc/tutorial/pics/logreg_pydotprint_train.png`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/printing_drawing.rst` & `pytensor-2.9.1/doc/tutorial/printing_drawing.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/profiling.rst` & `pytensor-2.9.1/doc/tutorial/profiling.rst`

 * *Files 0% similar despite different names*

```diff
@@ -23,17 +23,18 @@
     - You can also use the PyTensor flags :attr:`profiling__n_apply`,
       :attr:`profiling__n_ops` and :attr:`profiling__min_memory_size`
       to modify the quantity of information printed.
 
 2. Pass the argument :attr:`profile=True` to the function :func:`pytensor.function
    <function.function>` and then call :attr:`f.profile.summary()` for a single
    function.
-    - Use this option when you want to profile not all the
-      functions but only one or more specific function(s).
-    - You can also combine the profile results of many functions:
+
+   - Use this option when you want to profile not all the
+     functions but only one or more specific function(s).
+   - You can also combine the profile results of many functions:
 
       .. doctest::
           :hide:
 
           profile = pytensor.compile.ProfileStats()
           f = pytensor.function(..., profile=profile)  # doctest: +SKIP
           g = pytensor.function(..., profile=profile)  # doctest: +SKIP
```

### Comparing `pytensor-2.8.11/doc/tutorial/profiling_example_out.prof` & `pytensor-2.9.1/doc/tutorial/profiling_example_out.prof`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/shape_info.rst` & `pytensor-2.9.1/doc/tutorial/shape_info.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/doc/tutorial/sparse.rst` & `pytensor-2.9.1/doc/tutorial/sparse.rst`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/__init__.py` & `pytensor-2.9.1/pytensor/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -25,14 +25,16 @@
 # pytensor code, since this code may want to log some messages.
 import logging
 import os
 import sys
 from functools import singledispatch
 from typing import Any, NoReturn, Optional
 
+from pytensor.version import version as __version__
+
 
 pytensor_logger = logging.getLogger("pytensor")
 logging_default_handler = logging.StreamHandler()
 logging_default_formatter = logging.Formatter(
     fmt="%(levelname)s (%(name)s): %(message)s"
 )
 logging_default_handler.setFormatter(logging_default_formatter)
@@ -45,18 +47,14 @@
 # Disable default log handler added to pytensor_logger when the module
 # is imported.
 def disable_log_handler(logger=pytensor_logger, handler=logging_default_handler):
     if logger.hasHandlers():
         logger.removeHandler(handler)
 
 
-# Version information.
-from pytensor.version import version as __version__
-
-
 # Raise a meaningful warning/error if the pytensor directory is in the Python
 # path.
 rpath = os.path.realpath(__path__[0])
 for p in sys.path:
     if os.path.realpath(p) != rpath:
         continue
     raise RuntimeError("You have the pytensor directory in your Python path.")
@@ -169,31 +167,7 @@
 # isort: on
 
 
 # Some config variables are registered by submodules. Only after all those
 # imports were executed, we can warn about remaining flags provided by the user
 # through PYTENSOR_FLAGS.
 config.warn_unused_flags()
-
-DEPRECATED_NAMES = [
-    (
-        "change_flags",
-        "`pytensor.change_flags` is deprecated: use `pytensor.config.change_flags` instead.",
-        config.change_flags,
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/breakpoint.py` & `pytensor-2.9.1/pytensor/breakpoint.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/__init__.py` & `pytensor-2.9.1/pytensor/compile/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/builders.py` & `pytensor-2.9.1/pytensor/compile/builders.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/compiledir.py` & `pytensor-2.9.1/pytensor/compile/compiledir.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/compilelock.py` & `pytensor-2.9.1/pytensor/compile/compilelock.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/debugmode.py` & `pytensor-2.9.1/pytensor/compile/debugmode.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/function/__init__.py` & `pytensor-2.9.1/pytensor/compile/function/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/function/pfunc.py` & `pytensor-2.9.1/pytensor/compile/function/pfunc.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/function/types.py` & `pytensor-2.9.1/pytensor/compile/function/types.py`

 * *Files 0% similar despite different names*

```diff
@@ -1154,15 +1154,15 @@
     return rval
 
 
 def _constructor_Function(maker, input_storage, inputs_data, trust_input=False):
     if not config.unpickle_function:
         return None
 
-    f = maker.create(input_storage, trustme=True)
+    f = maker.create(input_storage)
     assert len(f.input_storage) == len(inputs_data)
     for container, x in zip(f.input_storage, inputs_data):
         assert (
             (container.data is x)
             or (isinstance(x, np.ndarray) and (container.data == x).all())
             or (container.data == x)
         )
@@ -1570,27 +1570,24 @@
                 i.value is not None
                 and not isinstance(i.value, Container)
                 and i.update is None
             )
             for i in self.inputs
         ]
 
-    def create(self, input_storage=None, trustme=False, storage_map=None):
+    def create(self, input_storage=None, storage_map=None):
         """
         Create a function.
 
         Parameters
         ----------
         input_storage
             A list matching the inputs list and providing default values if the
             default for an input is None, then that input is a required input.
             For an input with an update, the default acts as initialization.
-        trustme
-            Disables some exceptions, used internally.
-
         """
 
         if input_storage is None:
             input_storage = [None] * len(self.inputs)
         # list of independent one-element lists, will be passed to the linker
         input_storage_lists = []
         defaults = []
```

### Comparing `pytensor-2.8.11/pytensor/compile/io.py` & `pytensor-2.9.1/pytensor/compile/io.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/mode.py` & `pytensor-2.9.1/pytensor/compile/mode.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/monitormode.py` & `pytensor-2.9.1/pytensor/compile/monitormode.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/nanguardmode.py` & `pytensor-2.9.1/pytensor/compile/nanguardmode.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/ops.py` & `pytensor-2.9.1/pytensor/compile/ops.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/compile/profiling.py` & `pytensor-2.9.1/pytensor/compile/profiling.py`

 * *Files 1% similar despite different names*

```diff
@@ -1481,15 +1481,14 @@
                  Test them first, as they are not guaranteed to always provide a speedup.""",
             file=file,
         )
 
         from pytensor import scalar as aes
         from pytensor.tensor.elemwise import Elemwise
         from pytensor.tensor.math import Dot
-        from pytensor.tensor.random.op import RandomVariable
 
         scalar_op_amdlibm_no_speed_up = [
             aes.LT,
             aes.GT,
             aes.LE,
             aes.GE,
             aes.EQ,
@@ -1624,26 +1623,15 @@
                         f"Currently they are: {[i.type for i in node.inputs]}"
                     ),
                     file=file,
                 )
                 printed_tip = True
 
         # tip 5
-        for (fgraph, a) in self.apply_time:
-            node = a
-            if isinstance(node.op, RandomVariable):
-                printed_tip = True
-                print(
-                    "  - Replace the default random number generator by "
-                    "'from pytensor.sandbox.rng_mrg import MRG_RandomStream "
-                    "as RandomStream', as this is is faster. It is still "
-                    "experimental, but seems to work correctly.",
-                    file=file,
-                )
-                break
+        # The tip was about MRG_RandomStream which is removed
 
         # tip 6
         for (fgraph, a) in self.apply_time:
             node = a
             if isinstance(node.op, Dot) and len({i.dtype for i in node.inputs}) != 1:
                 print(
                     (
```

### Comparing `pytensor-2.8.11/pytensor/compile/sharedvalue.py` & `pytensor-2.9.1/pytensor/compile/sharedvalue.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/configdefaults.py` & `pytensor-2.9.1/pytensor/configdefaults.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,23 +7,23 @@
 import sys
 import textwrap
 
 import numpy as np
 from setuptools._distutils.spawn import find_executable
 
 import pytensor
-import pytensor.configparser
 from pytensor.configparser import (
     BoolParam,
     ConfigParam,
     DeviceParam,
     EnumStr,
     FloatParam,
     IntParam,
     StrParam,
+    _create_default_config,
 )
 from pytensor.utils import (
     LOCAL_BITWIDTH,
     PYTHON_INT_BITWIDTH,
     call_subprocess_Popen,
     maybe_add_to_os_environ_pathlist,
     output_subprocess_Popen,
@@ -1193,15 +1193,15 @@
         ConfigParam("None", apply=_filter_vm_lazy),
         in_c_key=False,
     )
 
 
 def add_deprecated_configvars():
 
-    # TODO: remove this?
+    # TODO: remove this? Agree
     config.add(
         "unittests__rseed",
         "Seed to use for randomized unit tests. "
         "Special value 'random' means using a seed of None.",
         StrParam(666, validate=_good_seem_param),
         in_c_key=False,
     )
@@ -1440,20 +1440,16 @@
     "as_input",
     "float16",
     "float32",
     "float64",
 )
 
 # Eventually, the instance of `PyTensorConfigParser` should be created right here,
-# where it is also populated with settings.  But for a transition period, it
-# remains as `configparser._config`, while everybody accessing it through
-# `configparser.config` is flooded with deprecation warnings. These warnings
-# instruct one to use `pytensor.config`, which is an alias for
-# `pytensor.configdefaults.config`.
-config = pytensor.configparser._config
+# where it is also populated with settings.
+config = _create_default_config()
 
 # The functions below register config variables into the config instance above.
 add_basic_configvars()
 add_compile_configvars()
 add_tensor_configvars()
 add_traceback_configvars()
 add_experimental_configvars()
@@ -1462,16 +1458,16 @@
 add_multiprocessing_configvars()
 add_optimizer_configvars()
 # TODO: Module-specific configs should probably be added upon import of the module.
 # This would mean either calling the function from there, or even moving all the related code there.
 # Blas-related config are a special pain-point, because their addition depends on a lot of stuff from
 # that module, which introduces a circular dependency!
 add_metaopt_configvars()
-add_vm_configvars()
 add_deprecated_configvars()
+add_vm_configvars()
 add_numba_configvars()
 
 # TODO: `gcc_version_str` is used by other modules.. Should it become an immutable config var?
 try:
     p_out = output_subprocess_Popen([config.cxx, "-dumpversion"])
     gcc_version_str = p_out[0].strip().decode()
 except OSError:
```

### Comparing `pytensor-2.8.11/pytensor/configparser.py` & `pytensor-2.9.1/pytensor/configparser.py`

 * *Files 20% similar despite different names*

```diff
@@ -61,35 +61,14 @@
             raise
 
     def __exit__(self, *args):
         for k, v in self.confs.items():
             v.__set__(self._root, self.old_vals[k])
 
 
-class _SectionRedirect:
-    """Functions as a mock property on the PyTensorConfigParser.
-
-    It redirects attribute access (to config subsectinos) to the
-    new config variable properties that use "__" in their name.
-    """
-
-    def __init__(self, root, section_name):
-        self._root = root
-        self._section_name = section_name
-        super().__init__()
-
-    def __getattr__(self, attr):
-        warnings.warn(
-            f"Accessing section '{attr}' through old .-based API. "
-            f"This will be removed. Use 'config.{self._section_name}__{attr}' instead.",
-            DeprecationWarning,
-        )
-        return getattr(self._root, f"{self._section_name}__{attr}")
-
-
 class PyTensorConfigParser:
     """Object that holds configuration settings."""
 
     def __init__(self, flags_dict: dict, pytensor_cfg, pytensor_raw_cfg):
         self._flags_dict = flags_dict
         self._pytensor_cfg = pytensor_cfg
         self._pytensor_raw_cfg = pytensor_raw_cfg
@@ -185,26 +164,14 @@
                 _logger.info(
                     f"Suppressed KeyError in PyTensorConfigParser.add for parameter '{name}'!"
                 )
 
         # the ConfigParam implements __get__/__set__, enabling us to create a property:
         setattr(self.__class__, name, configparam)
 
-        # The old API used dots for accessing a hierarchy of sections.
-        # The following code adds redirects that spill DeprecationWarnings
-        # while allowing backwards-compatible access to dot-based subsections.
-        # Because the subsectioning is recursive, redirects must be added for
-        # all levels. For example: ".test", ".test.subsection".
-        sections = name.split("__")
-        for s in range(1, len(sections)):
-            section_name = "__".join(sections[:s])
-            if not hasattr(self, section_name):
-                redirect = _SectionRedirect(self, section_name)
-                setattr(self.__class__, section_name, redirect)
-
     def fetch_val_for_key(self, key, delete_key=False):
         """Return the overriding config value for a key.
         A successful search returns a string value.
         An unsuccessful search raises a KeyError
 
         The (decreasing) priority order is:
         - PYTENSOR_FLAGS
@@ -561,80 +528,7 @@
     # But because the properties are assigned to the type, their existence is global.
     config = PyTensorConfigParser(
         flags_dict=PYTENSOR_FLAGS_DICT,
         pytensor_cfg=pytensor_cfg,
         pytensor_raw_cfg=pytensor_raw_cfg,
     )
     return config
-
-
-class _ConfigProxy:
-    """Like _SectionRedirect this class enables backwards-compatible access to the
-    config settings, but raises DeprecationWarnings with instructions to use `pytensor.config`.
-    """
-
-    def __init__(self, actual):
-        _ConfigProxy._actual = actual
-
-    def __getattr__(self, attr):
-        if attr == "_actual":
-            return _ConfigProxy._actual
-        warnings.warn(
-            "`pytensor.configparser.config` is deprecated; use `pytensor.config` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        return getattr(self._actual, attr)
-
-    def __setattr__(self, attr, value):
-        if attr == "_actual":
-            return setattr(_ConfigProxy._actual, attr, value)
-        warnings.warn(
-            "`pytensor.configparser.config` is deprecated; use `pytensor.config` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        return setattr(self._actual, attr, value)
-
-
-# Create the actual instance of the config. This one should eventually move to
-# `configdefaults`:
-_config = _create_default_config()
-
-# The old API often imported the default config object from `configparser`.
-# These imports/accesses should be replaced with `pytensor.config`, so this wraps
-# it with warnings:
-config = _ConfigProxy(_config)
-
-DEPRECATED_NAMES = [
-    (
-        "change_flags",
-        "`change_flags` is deprecated; use `pytensor.config.change_flags` instead.",
-        _config.change_flags,
-    ),
-    (
-        "_change_flags",
-        "`_change_flags` is deprecated; use `pytensor.config.change_flags` instead.",
-        _config.change_flags,
-    ),
-    (
-        "_config_print",
-        "`_config_print` is deprecated; use `pytensor.config.config_print` instead.",
-        _config.config_print,
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/d3viz/css/d3viz.css` & `pytensor-2.9.1/pytensor/d3viz/css/d3viz.css`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/d3viz.py` & `pytensor-2.9.1/pytensor/d3viz/d3viz.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/formatting.py` & `pytensor-2.9.1/pytensor/d3viz/formatting.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/js/d3-context-menu.js` & `pytensor-2.9.1/pytensor/d3viz/js/d3-context-menu.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/js/d3.v3.min.js` & `pytensor-2.9.1/pytensor/d3viz/js/d3.v3.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/js/d3viz.js` & `pytensor-2.9.1/pytensor/d3viz/js/d3viz.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/js/dagre-d3.min.js` & `pytensor-2.9.1/pytensor/d3viz/js/dagre-d3.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/d3viz/js/graphlib-dot.min.js` & `pytensor-2.9.1/pytensor/d3viz/js/graphlib-dot.min.js`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/gradient.py` & `pytensor-2.9.1/pytensor/gradient.py`

 * *Files 2% similar despite different names*

```diff
@@ -2104,52 +2104,14 @@
 
     if constant_value != 0.0:
         return "no"
 
     return "yes"
 
 
-class ConsiderConstant(ViewOp):
-    def grad(self, args, g_outs):
-        return [g_out.zeros_like(g_out) for g_out in g_outs]
-
-
-consider_constant_ = ConsiderConstant()
-
-
-def consider_constant(x):
-    """Consider an expression constant when computing gradients.
-
-    DEPRECATED: use `zero_grad` or `disconnected_grad` instead.
-
-    The expression itself is unaffected, but when its gradient is
-    computed, or the gradient of another expression that this
-    expression is a subexpression of, it will not be backpropagated
-    through. In other words, the gradient of the expression is
-    truncated to 0.
-
-    :param x: A PyTensor expression whose gradient should be truncated.
-
-    :return: The expression is returned unmodified, but its gradient
-        is now truncated to 0.
-
-    .. versionadded:: 0.7
-    """
-    warnings.warn(
-        (
-            "`ConsiderConstant` is deprecated; use `zero_grad` or "
-            "`disconnected_grad` instead."
-        ),
-        category=DeprecationWarning,
-        stacklevel=3,
-    )
-
-    return ConsiderConstant()(x)
-
-
 class ZeroGrad(ViewOp):
     def grad(self, args, g_outs):
         return [g_out.zeros_like(g_out) for g_out in g_outs]
 
     def R_op(self, inputs, eval_points):
         if eval_points[0] is None:
             return [None]
@@ -2348,32 +2310,7 @@
     >>> f_inverse=grad_scale(fx, -1.)
     >>> fpp = pytensor.grad(f_inverse, wrt=x)
     >>> fpprime = pytensor.function([x], fpp)
     >>> print(fpprime(2))  # doctest: +ELLIPSIS
     0.416...
     """
     return GradScale(multiplier)(x)
-
-
-DEPRECATED_NAMES = [
-    (
-        "consider_constant_",
-        "`consider_constant_` is deprecated; use `zero_grad` or `disconnected_grad` instead.",
-        ConsiderConstant(),
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/graph/__init__.py` & `pytensor-2.9.1/pytensor/graph/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/basic.py` & `pytensor-2.9.1/pytensor/graph/basic.py`

 * *Files 0% similar despite different names*

```diff
@@ -1052,55 +1052,56 @@
     if not ancestors_to_include:  # None or empty
         # just filter out unique variables
         for node in candidates:
             if node not in truncated_inputs:
                 truncated_inputs.append(node)
         # no more actions are needed
         return truncated_inputs
+
     blockers: Set[Variable] = set(ancestors_to_include)
     # enforce O(1) check for node in ancestors to include
     ancestors_to_include = blockers.copy()
 
     while candidates:
         # on any new candidate
         node = candidates.pop()
-        # check if the node is independent, never go above blockers
+
+        # There was a repeated reference to this node, we have already investigated it
+        if node in truncated_inputs:
+            continue
+
+        # check if the node is independent, never go above blockers;
         # blockers are independent nodes and ancestors to include
         if node in ancestors_to_include:
             # The case where node is in ancestors to include so we check if it depends on others
             # it should be removed from the blockers to check against the rest
-            dependent = variable_depends_on(node, blockers - {node})
+            dependent = variable_depends_on(node, ancestors_to_include - {node})
             # ancestors to include that are present in the graph (not disconnected)
             # should be added to truncated_inputs
             truncated_inputs.append(node)
             if dependent:
-                # if the ancestors to include is still dependent we need to go above,
-                # the search is not yet finished
-                # the node _has_ to have owner to be dependent
-                # so we do not check it
-                # and populate search to go above
+                # if the ancestors to include is still dependent we need to go above, the search is not yet finished
                 # owner can never be None for a dependent node
                 candidates.extend(node.owner.inputs)
         else:
             # A regular node to check
             dependent = variable_depends_on(node, blockers)
-            # all regular nodes fall to blockes
+            # all regular nodes fall to blockers
             # 1. it is dependent - further search irrelevant
             # 2. it is independent - the search node is inside the closure
             blockers.add(node)
             # if we've found an independent node and it is not in blockers so far
-            # it is a new indepenent node not present in ancestors to include
-            if not dependent:
-                # we've found an independent node
-                # do not search beyond
-                truncated_inputs.append(node)
-            else:
-                # populate search otherwise
+            # it is a new independent node not present in ancestors to include
+            if dependent:
+                # populate search if it's not an independent node
                 # owner can never be None for a dependent node
                 candidates.extend(node.owner.inputs)
+            else:
+                # otherwise, do not search beyond
+                truncated_inputs.append(node)
     return truncated_inputs
 
 
 def clone(
     inputs: List[Variable],
     outputs: List[Variable],
     copy_inputs: bool = True,
```

### Comparing `pytensor-2.8.11/pytensor/graph/destroyhandler.py` & `pytensor-2.9.1/pytensor/graph/destroyhandler.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/features.py` & `pytensor-2.9.1/pytensor/graph/features.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/fg.py` & `pytensor-2.9.1/pytensor/graph/fg.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/null_type.py` & `pytensor-2.9.1/pytensor/graph/null_type.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/op.py` & `pytensor-2.9.1/pytensor/graph/op.py`

 * *Files 1% similar despite different names*

```diff
@@ -352,14 +352,16 @@
             The gradients of the output variables.
 
         Returns
         -------
         grads
             The gradients with respect to each `Variable` in `inputs`.
 
+        References
+        ----------
         .. [1] Giles, Mike. 2008. “An Extended Collection of Matrix Derivative Results for Forward and Reverse Mode Automatic Differentiation.”
 
         """
         raise NotImplementedError()
 
     def L_op(
         self,
```

### Comparing `pytensor-2.8.11/pytensor/graph/replace.py` & `pytensor-2.9.1/pytensor/graph/replace.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/rewriting/basic.py` & `pytensor-2.9.1/pytensor/graph/rewriting/basic.py`

 * *Files 4% similar despite different names*

```diff
@@ -106,22 +106,14 @@
         It may use all the methods defined by the `FunctionGraph`. If the
         `GraphRewriter` needs to use a certain tool, such as an
         `InstanceFinder`, it can do so in its `add_requirements` method.
 
         """
         raise NotImplementedError()
 
-    def optimize(self, *args, **kwargs):
-        warnings.warn(
-            "`GraphRewriter.optimize` is deprecated; use `GraphRewriter.rewrite` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        self.rewrite(*args, **kwargs)
-
     def rewrite(self, fgraph, *args, **kwargs):
         """
 
         This is meant as a shortcut for the following::
 
             self.add_requirements(fgraph)
             self.apply(fgraph)
@@ -172,15 +164,15 @@
 
         Subclasses should implement this function so that it returns one of the
         following:
 
         - ``False`` to indicate that this rewrite cannot be applied to `node`
         - A list of `Variable`\s to use in place of the `node`'s current outputs
         - A ``dict`` mapping old `Variable`\s to `Variable`\s, or the key
-        ``"remove"`` mapping to a list of `Variable`\s to be removed.
+            ``"remove"`` mapping to a list of `Variable`\s to be removed.
 
         Parameters
         ----------
         fgraph
             A `FunctionGraph` containing `node`.
         node
             An `Apply` node to be rewritten.
@@ -2302,22 +2294,14 @@
             self.cleanup_rewriters = []
 
         self.max_use_ratio = max_use_ratio
 
     def get_node_rewriters(self):
         yield from self.node_tracker.get_rewriters()
 
-    def get_local_optimizers(self):
-        warnings.warn(
-            "`get_local_optimizers` is deprecated; use `get_node_rewriters` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        yield from self.get_node_rewriters()
-
     def add_requirements(self, fgraph):
         super().add_requirements(fgraph)
         for rewriter in self.get_node_rewriters():
             rewriter.add_requirements(fgraph)
         for rewriter in self.global_rewriters:
             rewriter.add_requirements(fgraph)
         for rewriter in self.final_rewriters:
@@ -3133,132 +3117,7 @@
 
     def add_requirements(self, fgraph):
         if not hasattr(fgraph, "CheckStackTraceFeature"):
             fgraph.attach_feature(CheckStackTraceFeature())
 
     def apply(self, fgraph):
         pass
-
-
-DEPRECATED_NAMES = [
-    (
-        "LocalMetaOptimizerSkipAssertionError",
-        "`LocalMetaOptimizerSkipAssertionError` is deprecated: use `MetaNodeRewriterSkip` instead.",
-        MetaNodeRewriterSkip,
-    ),
-    (
-        "GlobalOptimizer",
-        "`GlobalOptimizer` is deprecated: use `GraphRewriter` instead.",
-        GraphRewriter,
-    ),
-    (
-        "LocalOptimizer",
-        "`LocalOptimizer` is deprecated: use `NodeRewriter` instead.",
-        NodeRewriter,
-    ),
-    (
-        "local_optimizer",
-        "`local_optimizer` is deprecated: use `node_rewriter` instead.",
-        node_rewriter,
-    ),
-    (
-        "pre_greedy_local_optimizer",
-        "`pre_greedy_local_optimizer` is deprecated: use `pre_greedy_node_rewriter` instead.",
-        pre_greedy_node_rewriter,
-    ),
-    (
-        "FromFunctionOptimizer",
-        "`FromFunctionOptimizer` is deprecated: use `FromFunctionGraphRewriter` instead.",
-        FromFunctionGraphRewriter,
-    ),
-    (
-        "optimizer",
-        "`optimizer` is deprecated: use `graph_rewriter` instead.",
-        graph_rewriter,
-    ),
-    (
-        "inplace_optimizer",
-        "`inplace_optimizer` is deprecated: use `graph_rewriter` instead.",
-        graph_rewriter,
-    ),
-    (
-        "LocalMetaOptimizer",
-        "`LocalMetaOptimizer` is deprecated: use `MetaNodeRewriter` instead.",
-        MetaNodeRewriter,
-    ),
-    (
-        "SeqOptimizer",
-        "`SeqOptimizer` is deprecated: use `SequentialGraphRewriter` instead.",
-        SequentialGraphRewriter,
-    ),
-    (
-        "FromFunctionLocalOptimizer",
-        "`FromFunctionLocalOptimizer` is deprecated: use `FromFunctionNodeRewriter` instead.",
-        FromFunctionNodeRewriter,
-    ),
-    (
-        "LocalOptTracker",
-        "`LocalOptTracker` is deprecated: use `OpToRewriterTracker` instead.",
-        OpToRewriterTracker,
-    ),
-    (
-        "LocalOptGroup",
-        "`LocalOptGroup` is deprecated: use `SequentialNodeRewriter` instead.",
-        SequentialNodeRewriter,
-    ),
-    (
-        "OpSub",
-        "`OpSub` is deprecated: use `SubstitutionNodeRewriter` instead.",
-        SubstitutionNodeRewriter,
-    ),
-    (
-        "OpRemove",
-        "`OpRemove` is deprecated: use `RemovalNodeRewriter` instead.",
-        RemovalNodeRewriter,
-    ),
-    (
-        "PatternSub",
-        "`PatternSub` is deprecated: use `PatternNodeRewriter` instead.",
-        PatternNodeRewriter,
-    ),
-    (
-        "NavigatorOptimizer",
-        "`NavigatorOptimizer` is deprecated: use `NodeProcessingGraphRewriter` instead.",
-        NodeProcessingGraphRewriter,
-    ),
-    (
-        "TopoOptimizer",
-        "`TopoOptimizer` is deprecated: use `WalkingGraphRewriter` instead.",
-        WalkingGraphRewriter,
-    ),
-    (
-        "topogroup_optimizer",
-        "`topogroup_optimizer` is deprecated: use `walking_rewriter` instead.",
-        walking_rewriter,
-    ),
-    (
-        "OpKeyOptimizer",
-        "`OpKeyOptimizer` is deprecated: use `OpKeyGraphRewriter` instead.",
-        OpKeyGraphRewriter,
-    ),
-    (
-        "EquilibriumOptimizer",
-        "`EquilibriumOptimizer` is deprecated: use `EquilibriumGraphRewriter` instead.",
-        EquilibriumGraphRewriter,
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/graph/rewriting/db.py` & `pytensor-2.9.1/pytensor/graph/rewriting/db.py`

 * *Files 3% similar despite different names*

```diff
@@ -534,47 +534,7 @@
         if not isinstance(db, RewriteDatabase):
             raise TypeError("`db` must be an `RewriteDatabase`.")
 
         self.db = db
 
     def query(self, *tags, **kwtags):
         return self.db.query(*tags, **kwtags)
-
-
-DEPRECATED_NAMES = [
-    (
-        "DB",
-        "`DB` is deprecated; use `RewriteDatabase` instead.",
-        RewriteDatabase,
-    ),
-    (
-        "Query",
-        "`Query` is deprecated; use `RewriteDatabaseQuery` instead.",
-        RewriteDatabaseQuery,
-    ),
-    (
-        "OptimizationDatabase",
-        "`OptimizationDatabase` is deprecated; use `RewriteDatabase` instead.",
-        RewriteDatabase,
-    ),
-    (
-        "OptimizationQuery",
-        "`OptimizationQuery` is deprecated; use `RewriteDatabaseQuery` instead.",
-        RewriteDatabaseQuery,
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/graph/rewriting/kanren.py` & `pytensor-2.9.1/pytensor/graph/rewriting/kanren.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/rewriting/unify.py` & `pytensor-2.9.1/pytensor/graph/rewriting/unify.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/graph/rewriting/utils.py` & `pytensor-2.9.1/pytensor/graph/rewriting/utils.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 import copy
-import warnings
 from typing import TYPE_CHECKING, Generator, Optional, Sequence, Union, cast
 
 import pytensor
 from pytensor.graph.basic import (
     Apply,
     Variable,
     equal_computations,
@@ -19,15 +18,14 @@
 
 
 def rewrite_graph(
     graph: Union[Variable, Sequence[Variable], FunctionGraph],
     include: Sequence[str] = ("canonicalize",),
     custom_rewrite: Optional["GraphRewriter"] = None,
     clone: bool = False,
-    custom_opt: Optional["GraphRewriter"] = None,
     **kwargs,
 ) -> Union[Variable, Sequence[Variable], FunctionGraph]:
     """Easily apply rewrites to a graph.
 
     Parameters
     ----------
     graph
@@ -58,22 +56,14 @@
             outputs = [graph]
 
         fgraph = FunctionGraph(outputs=outputs, clone=clone)
 
     query_rewrites = optdb.query(RewriteDatabaseQuery(include=include, **kwargs))
     _ = query_rewrites.rewrite(fgraph)
 
-    if custom_opt is not None:
-        warnings.warn(
-            "`custom_opt` is deprecated; use `custom_rewrite` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        custom_rewrite = custom_opt
-
     if custom_rewrite:
         custom_rewrite.rewrite(fgraph)
 
     if return_fgraph:
         return fgraph
     else:
         if isinstance(graph, (list, tuple)):
@@ -244,32 +234,7 @@
                     continue
                 yield from get_clients_at_depth(
                     fgraph, cast(Apply, out_node), depth - 1
                 )
         else:
             assert var.owner is not None
             yield var.owner
-
-
-DEPRECATED_NAMES = [
-    (
-        "optimize_graph",
-        "`optimize_graph` is deprecated: use `rewrite_graph` instead.",
-        rewrite_graph,
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/graph/sched.py` & `pytensor-2.9.1/pytensor/graph/type.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,283 +1,275 @@
-from collections import defaultdict
+from abc import abstractmethod
+from typing import Any, Generic, Optional, Tuple, TypeVar, Union
 
-from pytensor.graph.basic import list_of_nodes
-from pytensor.utils import cmp
+from typing_extensions import TypeAlias
 
+from pytensor.graph import utils
+from pytensor.graph.basic import Constant, Variable
+from pytensor.graph.utils import MetaObject
 
-# {{{ http://code.activestate.com/recipes/578231/ (r1)
-# Copyright (c) Oren Tirosh 2012
-#
-# Permission is hereby granted, free of charge, to any person obtaining a copy
-# of this software and associated documentation files (the "Software"), to deal
-# in the Software without restriction, including without limitation the rights
-# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-# copies of the Software, and to permit persons to whom the Software is
-# furnished to do so, subject to the following conditions:
-#
-# The above copyright notice and this permission notice shall be included in
-# all copies or substantial portions of the Software.
-#
-# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-# SOFTWARE.
 
+D = TypeVar("D")
 
-def memodict(f):
-    """
-    Memoization decorator for a function taking a single argument.
 
+class Type(MetaObject, Generic[D]):
     """
+    Interface specification for variable type instances.
 
-    class memodict(defaultdict):
-        def __missing__(self, key):
-            ret = self[key] = f(key)
-            return ret
-
-    return memodict().__getitem__
+    A :term:`Type` instance is mainly responsible for two things:
 
+    - creating `Variable` instances (conventionally, `__call__` does this), and
 
-# end of http://code.activestate.com/recipes/578231/ }}}
+    - filtering a value assigned to a `Variable` so that the value
+      conforms to restrictions imposed by the type (also known as
+      casting, this is done by `filter`).
 
+    """
 
-def make_depends():
-    @memodict
-    def depends(pair):
-        """
-        Returns True if a depends on b.
+    variable_type: TypeAlias = Variable
+    """
+    The `Type` that will be created by a call to `Type.make_variable`.
+    """
 
-        """
-        a, b = pair
-        return any(bout in a.inputs for bout in b.outputs) or any(
-            depends((ainp.owner, b)) for ainp in a.inputs if ainp.owner
-        )
+    constant_type: TypeAlias = Constant
+    """
+    The `Type` that will be created by a call to `Type.make_constant`.
+    """
 
-    return depends
+    def in_same_class(self, otype: "Type") -> Optional[bool]:
+        """Determine if another `Type` represents a subset from the same "class" of types represented by `self`.
 
+        A "class" of types could be something like "float64 tensors with four
+        dimensions".  One `Type` could represent a set containing only a type
+        for "float64 tensors with shape (1, 2, 3, 4)" and another the set of
+        "float64 tensors with shape (1, x, x, x)" for all suitable "x".
 
-def make_dependence_cmp():
-    """
-    Create a comparator to represent the dependence of nodes in a graph.
+        It's up to each subclass of `Type` to determine to which "classes" of types this
+        method applies.
 
-    """
-    depends = make_depends()
+        The default implementation assumes that all "classes" have only one
+        unique element (i.e. it uses `self.__eq__`).
 
-    def dependence(a, b):
         """
-        A cmp function for nodes in a graph - does a depend on b?
+        if self == otype:
+            return True
 
-        Returns
-        -------
-        int
-            Positive number if a depends on b, negative number
-            if b depends on a, 0 otherwise.
+        return False
 
-        """
-        if depends((a, b)):
-            return 1
-        if depends((b, a)):
-            return -1
-        return 0
+    def is_super(self, otype: "Type") -> Optional[bool]:
+        """Determine if `self` is a supertype of `otype`.
 
-    return dependence
+        This method effectively implements the type relation ``>``.
 
+        In general, ``t1.is_super(t2) == True`` implies that ``t1`` can be
+        replaced with ``t2``.
 
-def reverse_dict(d):
-    """
-    Reverses direction of dependence dict.
+        See `Type.in_same_class`.
 
-    Notes
-    -----
-    dict order is not deterministic. As we iterate on the
-    input dict, it makes the output of this function depend on the
-    dict order. So this function output order should be considered
-    as undeterministic.
-
-    Examples
-    --------
-    >>> d = {'a': (1, 2), 'b': (2, 3), 'c':()}
-    >>> reverse_dict(d)
-    {1: ('a',), 2: ('a', 'b'), 3: ('b',)}
+        Returns
+        -------
+        ``None`` if the type relation cannot be applied/determined.
 
-    """
-    result = {}
-    for key in d:
-        for val in d[key]:
-            result[val] = result.get(val, tuple()) + (key,)
-    return result
+        """
+        if self.in_same_class(otype):
+            return True
 
+        return None
 
-def _toposort(edges):
-    """
-    Topological sort algorithm by Kahn [1] - O(nodes + vertices).
+    @abstractmethod
+    def filter(
+        self, data: Any, strict: bool = False, allow_downcast: Optional[bool] = None
+    ) -> D:
+        """Return data or an appropriately wrapped/converted data.
+
+        Subclass implementations should raise a TypeError exception if
+        the data is not of an acceptable type.
+
+        Parameters
+        ----------
+        data: array-like
+            The data to be filtered/converted.
+        strict: bool (optional)
+            If ``True``, the data returned must be the same as the
+            data passed as an argument.
+        allow_downcast: bool (optional)
+            If `strict` is ``False``, and `allow_downcast` is ``True``, the
+            data may be cast to an appropriate type. If `allow_downcast` is
+            ``False``, it may only be up-cast and not lose precision. If
+            `allow_downcast` is ``None`` (default), the behaviour can be
+            type-dependent, but for now it means only Python floats can be
+            down-casted, and only to floatX scalars.
 
-    Parameters
-    ----------
-    edges
-        A dict of the form {a: {b, c}} where b and c depend on a.
-
-    Returns
-    -------
-    L : list
-        An ordered list of nodes that satisfy the dependencies of edges.
-
-    Closely follows the wikipedia page [2]
-
-    References
-    ----------
-    [1] Kahn, Arthur B. (1962), "Topological sorting of large networks",
-    Communications of the ACM
-    [2] http://en.wikipedia.org/wiki/Toposort#Algorithms
-
-    Examples
-    --------
-    >>> _toposort({1: {2, 3}, 2: (3, )})
-    [1, 2, 3]
+        """
 
-    """
-    incoming_edges = reverse_dict(edges)
-    incoming_edges = {k: set(val) for k, val in incoming_edges.items()}
-    S = {v for v in edges if v not in incoming_edges}
-    L = []
-
-    while S:
-        n = S.pop()
-        L.append(n)
-        for m in edges.get(n, ()):
-            assert n in incoming_edges[m]
-            incoming_edges[m].remove(n)
-            if not incoming_edges[m]:
-                S.add(m)
-    if any(incoming_edges.get(v, None) for v in edges):
-        raise ValueError("Input has cycles")
-    return L
+    def filter_inplace(
+        self,
+        value: Any,
+        storage: Any,
+        strict: bool = False,
+        allow_downcast: Optional[bool] = None,
+    ):
+        """Return data or an appropriately wrapped/converted data by converting it in-place.
+
+        This method allows one to reuse old allocated memory.  If this method
+        is implemented, it will be called instead of `Type.filter`.
+
+        As of now, this method is not implemented and was previously used for transferring memory to and from GPU.
+
+        Parameters
+        ----------
+        value: array-like
+        storage: array-like
+            The old value (e.g. the old NumPy array)
+        strict: bool
+        allow_downcast: bool (optional)
+
+        Raises
+        ------
+        NotImplementedError
+        """
+        raise NotImplementedError()
 
+    def filter_variable(
+        self, other: Union[Variable, D], allow_convert: bool = True
+    ) -> variable_type:
+        r"""Convert a `other` into a `Variable` with a `Type` that's compatible with `self`.
 
-def posort(nodes, *cmps):
-    """
-    Partially ordered sort with multiple comparators.
+        If the involved `Type`\s are not compatible, a `TypeError` will be raised.
+        """
+        if not isinstance(other, Variable):
+            # The value is not a Variable: we cast it into
+            # a Constant of the appropriate Type.
+            other = self.constant_type(type=self, data=other)
+
+        if other.type != self and allow_convert:
+            other2 = self.convert_variable(other)
+            if other2 is not None:
+                return other2
+
+        if other.type != self:
+            raise TypeError(
+                f"Cannot convert Type {other.type} "
+                f"(of Variable {other}) into Type {self}. "
+                f"You can try to manually convert {other} into a {self}."
+            )
+        return other
 
-    Given a list of comparators, orders the elements in `nodes` so that the
-    comparators are satisfied as much as possible giving precedence to
-    earlier comparators.
-
-    Parameters
-    ----------
-    nodes
-        An iterable of nodes in a graph.
-    cmps
-        A sequence of comparator functions that describe which nodes should
-        come before which others.
-
-    Returns
-    -------
-    list
-        A list of nodes which satisfy the comparators as much as possible.
-
-    Notes
-    -----
-    Implemented with _toposort.
-
-    Examples
-    --------
-    >>> lower_tens = lambda a, b: a/10 - b/10 # prefer lower numbers div 10
-    >>> prefer evens = lambda a, b: a%2 - b%2 # prefer even numbers
-    >>> posort(list(range(20)), lower_tens, prefer_evens)
-    [0, 8, 2, 4, 6, 1, 3, 5, 7, 9, 16, 18, 10, 12, 14, 17, 19, 11, 13, 15]
+    def convert_variable(self, var: Variable) -> Optional[Variable]:
+        """Produce a `Variable` that's compatible with both `self` and `var.type`, if possible.
 
-    """
-    comes_before = {a: set() for a in nodes}
-    comes_after = {a: set() for a in nodes}
+        A compatible `Variable` is a `Variable` with a `Type` that's the
+        "narrower" of `self` and `var.type`.
 
-    def add_links(a, b):  # b depends on a
-        comes_after[a].add(b)
-        comes_after[a].update(comes_after[b])
-        for c in comes_before[a]:
-            comes_after[c].update(comes_after[a])
-        comes_before[b].add(a)
-        comes_before[b].update(comes_before[a])
-        for c in comes_after[b]:
-            comes_before[c].update(comes_before[b])
+        If a compatible `Type` cannot be found, this method will return
+        ``None``.
 
-    def check():
         """
-        Tests for cycles in manufactured edges.
+        var_type = var.type
+
+        if self.is_super(var_type):
+            # `var.type` is at least as specific as `self`, so we return it
+            # as-is
+            return var
+        elif var_type.is_super(self):
+            # `var.type` is less specific than `self`, so we need to convert it
+            # to `self`'s `Type`.
+            #
+            # Note that, in this case, `var.type != self`, because equality is
+            # covered by the branch above.
+            raise NotImplementedError()
+
+        return None
+
+    def is_valid_value(self, data: D, strict: bool = True) -> bool:
+        """Return ``True`` for any python object that would be a legal value for a `Variable` of this `Type`."""
+        try:
+            self.filter(data, strict=strict)
+            return True
+        except (TypeError, ValueError):
+            return False
+
+    def make_variable(self, name: Optional[str] = None) -> variable_type:
+        """Return a new `Variable` instance of this `Type`.
+
+        Parameters
+        ----------
+        name: None or str
+            A pretty string for printing and debugging.
 
         """
-        for a in nodes:
-            for b in nodes:
-                assert not (b in comes_after[a] and a in comes_after[b])
+        return self.variable_type(self, None, name=name)
 
-    for cmp_fn in cmps:
-        for a in nodes:
-            for b in nodes:
-                if cmp_fn(a, b) < 0:  # a wants to come before b
-                    # if this wouldn't cause a cycle and isn't already known
-                    if b not in comes_before[a] and b not in comes_after[a]:
-                        add_links(a, b)
-    # check() # debug code
+    def make_constant(self, value: D, name: Optional[str] = None) -> constant_type:
+        """Return a new `Constant` instance of this `Type`.
 
-    return _toposort(comes_after)
+        Parameters
+        ----------
+        value: array-like
+            The constant value.
+        name: None or str
+            A pretty string for printing and debugging.
 
+        """
+        return self.constant_type(type=self, data=value, name=name)
 
-def sort_apply_nodes(inputs, outputs, cmps):
-    """
-    Order a graph of apply nodes according to a list of comparators.
+    def clone(self, *args, **kwargs) -> "Type":
+        """Clone a copy of this type with the given arguments/keyword values, if any."""
+        return type(self)(*args, **kwargs)
+
+    def __call__(self, name: Optional[str] = None) -> variable_type:
+        """Return a new `Variable` instance of Type `self`.
+
+        Parameters
+        ----------
+        name : None or str
+            A pretty string for printing and debugging.
 
-    The following example sorts first by dependence of nodes (this is a
-    topological sort) and then by lexicographical ordering (nodes that start
-    with 'E' come before nodes that start with 'I' if there is no dependence.
-
-    Examples
-    --------
-    >>> from pytensor.graph.basic import sort_apply_nodes, dependence
-    >>> from pytensor.tensor.type import matrix
-    >>> from pytensor.tensor.math import dot
-    >>> x = matrix('x')
-    >>> y = dot(x*2, x+1)
-    >>> str_cmp = lambda a, b: cmp(str(a), str(b)) # lexicographical sort
-    >>> sort_apply_nodes([x], [y], cmps=[dependence, str_cmp])
-    [Elemwise{add,no_inplace}(x, InplaceDimShuffle{x,x}.0),
-     InplaceDimShuffle{x,x}(TensorConstant{2}),
-     Elemwise{mul,no_inplace}(x, InplaceDimShuffle{x,x}.0),
-     InplaceDimShuffle{x,x}(TensorConstant{1}),
-     dot(Elemwise{mul,no_inplace}.0, Elemwise{add,no_inplace}.0)]
+        """
+        return utils.add_tag_trace(self.make_variable(name))
 
-    """
-    return posort(list_of_nodes(inputs, outputs), *cmps)
+    @classmethod
+    def values_eq(cls, a: D, b: D) -> bool:
+        """Return ``True`` if `a` and `b` can be considered exactly equal.
 
+        `a` and `b` are assumed to be valid values of this `Type`.
 
-def sort_schedule_fn(*cmps):
-    """
-    Make a schedule function from comparators.
+        """
+        return a == b
 
-    See Also
-    --------
-    sort_apply_nodes
+    @classmethod
+    def values_eq_approx(cls, a: D, b: D) -> bool:
+        """Return ``True`` if `a` and `b` can be considered approximately equal.
+
+        This function is used by PyTensor debugging tools to decide
+        whether two values are equivalent, admitting a certain amount
+        of numerical instability. For example, for floating-point
+        numbers this function should be an approximate comparison.
+
+        By default, this does an exact comparison.
+
+        Parameters
+        ----------
+        a: array-like
+            A potential value for a `Variable` of this `Type`.
+        b: array-like
+            A potential value for a `Variable` of this `Type`.
 
-    """
-    dependence = make_dependence_cmp()
-    cmps = (dependence,) + cmps
+        Returns
+        -------
+        bool
 
-    def schedule(fgraph):
         """
-        Order nodes in a FunctionGraph.
+        return cls.values_eq(a, b)
 
-        """
-        return sort_apply_nodes(fgraph.inputs, fgraph.outputs, cmps)
 
-    return schedule
+class HasDataType:
+    """A mixin for a type that has a :attr:`dtype` attribute."""
 
+    dtype: str
 
-def key_to_cmp(key):
-    """
-    comparator function based on "key" function
-    """
 
-    def key_cmp(a, b):
-        return cmp(key(a), key(b))
+class HasShape:
+    """A mixin for a type that has :attr:`shape` and :attr:`ndim` attributes."""
 
-    return key_cmp
+    ndim: int
+    shape: Tuple[Optional[int], ...]
```

### Comparing `pytensor-2.8.11/pytensor/graph/type.py` & `pytensor-2.9.1/pytensor/tensor/random/utils.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,275 +1,290 @@
-from abc import abstractmethod
-from typing import Any, Generic, Optional, Tuple, TypeVar, Union
+from collections.abc import Sequence
+from functools import wraps
+from itertools import zip_longest
+from types import ModuleType
+from typing import TYPE_CHECKING, Optional, Union
 
-from typing_extensions import TypeAlias
+import numpy as np
+from typing_extensions import Literal
 
-from pytensor.graph import utils
+from pytensor.compile.sharedvalue import shared
 from pytensor.graph.basic import Constant, Variable
-from pytensor.graph.utils import MetaObject
-
-
-D = TypeVar("D")
-
-
-class Type(MetaObject, Generic[D]):
-    """
-    Interface specification for variable type instances.
-
-    A :term:`Type` instance is mainly responsible for two things:
-
-    - creating `Variable` instances (conventionally, `__call__` does this), and
-
-    - filtering a value assigned to a `Variable` so that the value
-      conforms to restrictions imposed by the type (also known as
-      casting, this is done by `filter`).
-
+from pytensor.tensor import get_vector_length
+from pytensor.tensor.basic import as_tensor_variable, cast, constant
+from pytensor.tensor.extra_ops import broadcast_to
+from pytensor.tensor.math import maximum
+from pytensor.tensor.shape import specify_shape
+from pytensor.tensor.type import int_dtypes
+from pytensor.tensor.var import TensorVariable
+
+
+if TYPE_CHECKING:
+    from pytensor.tensor.random.op import RandomVariable
+
+
+def params_broadcast_shapes(param_shapes, ndims_params, use_pytensor=True):
+    """Broadcast parameters that have different dimensions.
+
+    Parameters
+    ==========
+    param_shapes : list of ndarray or Variable
+        The shapes of each parameters to broadcast.
+    ndims_params : list of int
+        The expected number of dimensions for each element in `params`.
+    use_pytensor : bool
+        If ``True``, use PyTensor `Op`; otherwise, use NumPy.
+
+    Returns
+    =======
+    bcast_shapes : list of ndarray
+        The broadcasted values of `params`.
     """
+    max_fn = maximum if use_pytensor else max
 
-    variable_type: TypeAlias = Variable
-    """
-    The `Type` that will be created by a call to `Type.make_variable`.
+    rev_extra_dims = []
+    for ndim_param, param_shape in zip(ndims_params, param_shapes):
+        # We need this in order to use `len`
+        param_shape = tuple(param_shape)
+        extras = tuple(param_shape[: (len(param_shape) - ndim_param)])
+
+        def max_bcast(x, y):
+            if getattr(x, "value", x) == 1:
+                return y
+            if getattr(y, "value", y) == 1:
+                return x
+            return max_fn(x, y)
+
+        rev_extra_dims = [
+            max_bcast(a, b)
+            for a, b in zip_longest(reversed(extras), rev_extra_dims, fillvalue=1)
+        ]
+
+    extra_dims = tuple(reversed(rev_extra_dims))
+
+    bcast_shapes = [
+        (extra_dims + tuple(param_shape)[-ndim_param:])
+        if ndim_param > 0
+        else extra_dims
+        for ndim_param, param_shape in zip(ndims_params, param_shapes)
+    ]
+
+    return bcast_shapes
+
+
+def broadcast_params(params, ndims_params):
+    """Broadcast parameters that have different dimensions.
+
+    >>> ndims_params = [1, 2]
+    >>> mean = np.array([1, 2, 3])
+    >>> cov = np.stack([np.eye(3), np.eye(3)])
+    >>> params = [mean, cov]
+    >>> res = broadcast_params(params, ndims_params)
+    [array([[1, 2, 3]]),
+    array([[[1., 0., 0.],
+             [0., 1., 0.],
+             [0., 0., 1.]],
+            [[1., 0., 0.],
+             [0., 1., 0.],
+             [0., 0., 1.]]])]
+
+    Parameters
+    ==========
+    params : list of ndarray
+        The parameters to broadcast.
+    ndims_params : list of int
+        The expected number of dimensions for each element in `params`.
+
+    Returns
+    =======
+    bcast_params : list of ndarray
+        The broadcasted values of `params`.
     """
+    use_pytensor = False
+    param_shapes = []
+    for p in params:
+        param_shape = tuple(
+            1 if bcast else s
+            for s, bcast in zip(p.shape, getattr(p, "broadcastable", (False,) * p.ndim))
+        )
+        use_pytensor |= isinstance(p, Variable)
+        param_shapes.append(param_shape)
+
+    shapes = params_broadcast_shapes(
+        param_shapes, ndims_params, use_pytensor=use_pytensor
+    )
+    broadcast_to_fn = broadcast_to if use_pytensor else np.broadcast_to
+
+    bcast_params = [
+        broadcast_to_fn(param, shape) for shape, param in zip(shapes, params)
+    ]
+
+    return bcast_params
+
+
+def normalize_size_param(
+    size: Optional[Union[int, np.ndarray, Variable, Sequence]]
+) -> Variable:
+    """Create an PyTensor value for a ``RandomVariable`` ``size`` parameter."""
+    if size is None:
+        size = constant([], dtype="int64")
+    elif isinstance(size, int):
+        size = as_tensor_variable([size], ndim=1)
+    elif not isinstance(size, (np.ndarray, Variable, Sequence)):
+        raise TypeError(
+            "Parameter size must be None, an integer, or a sequence with integers."
+        )
+    else:
+        size = cast(as_tensor_variable(size, ndim=1, dtype="int64"), "int64")
+
+        if not isinstance(size, Constant):
+            # This should help ensure that the length of non-constant `size`s
+            # will be available after certain types of cloning (e.g. the kind
+            # `Scan` performs)
+            size = specify_shape(size, (get_vector_length(size),))
+
+    assert not any(s is None for s in size.type.shape)
+    assert size.dtype in int_dtypes
+
+    return size
+
+
+class RandomStream:
+    """Module component with similar interface to `numpy.random.Generator`.
+
+    Attributes
+    ----------
+    seed: None or int
+        A default seed to initialize the `Generator` instances after build.
+    state_updates: list
+        A list of pairs of the form ``(input_r, output_r)``.  This will be
+        over-ridden by the module instance to contain stream generators.
+    default_instance_seed: int
+        Instance variable should take None or integer value. Used to seed the
+        random number generator that provides seeds for member streams.
+    gen_seedgen: numpy.random.Generator
+        `Generator` instance that `RandomStream.gen` uses to seed new
+        streams.
+    rng_ctor: type
+        Constructor used to create the underlying RNG objects.  The default
+        is `np.random.default_rng`.
 
-    constant_type: TypeAlias = Constant
-    """
-    The `Type` that will be created by a call to `Type.make_constant`.
     """
 
-    def in_same_class(self, otype: "Type") -> Optional[bool]:
-        """Determine if another `Type` represents a subset from the same "class" of types represented by `self`.
-
-        A "class" of types could be something like "float64 tensors with four
-        dimensions".  One `Type` could represent a set containing only a type
-        for "float64 tensors with shape (1, 2, 3, 4)" and another the set of
-        "float64 tensors with shape (1, x, x, x)" for all suitable "x".
-
-        It's up to each subclass of `Type` to determine to which "classes" of types this
-        method applies.
-
-        The default implementation assumes that all "classes" have only one
-        unique element (i.e. it uses `self.__eq__`).
-
-        """
-        if self == otype:
-            return True
-
-        return False
-
-    def is_super(self, otype: "Type") -> Optional[bool]:
-        """Determine if `self` is a supertype of `otype`.
-
-        This method effectively implements the type relation ``>``.
-
-        In general, ``t1.is_super(t2) == True`` implies that ``t1`` can be
-        replaced with ``t2``.
-
-        See `Type.in_same_class`.
-
-        Returns
-        -------
-        ``None`` if the type relation cannot be applied/determined.
-
-        """
-        if self.in_same_class(otype):
-            return True
-
-        return None
-
-    @abstractmethod
-    def filter(
-        self, data: Any, strict: bool = False, allow_downcast: Optional[bool] = None
-    ) -> D:
-        """Return data or an appropriately wrapped/converted data.
-
-        Subclass implementations should raise a TypeError exception if
-        the data is not of an acceptable type.
-
-        Parameters
-        ----------
-        data: array-like
-            The data to be filtered/converted.
-        strict: bool (optional)
-            If ``True``, the data returned must be the same as the
-            data passed as an argument.
-        allow_downcast: bool (optional)
-            If `strict` is ``False``, and `allow_downcast` is ``True``, the
-            data may be cast to an appropriate type. If `allow_downcast` is
-            ``False``, it may only be up-cast and not lose precision. If
-            `allow_downcast` is ``None`` (default), the behaviour can be
-            type-dependent, but for now it means only Python floats can be
-            down-casted, and only to floatX scalars.
-
-        """
-
-    def filter_inplace(
+    def __init__(
         self,
-        value: Any,
-        storage: Any,
-        strict: bool = False,
-        allow_downcast: Optional[bool] = None,
+        seed: Optional[int] = None,
+        namespace: Optional[ModuleType] = None,
+        rng_ctor: Literal[
+            np.random.RandomState, np.random.Generator
+        ] = np.random.default_rng,
     ):
-        """Return data or an appropriately wrapped/converted data by converting it in-place.
+        if namespace is None:
+            from pytensor.tensor.random import basic  # pylint: disable=import-self
 
-        This method allows one to reuse old allocated memory.  If this method
-        is implemented, it will be called instead of `Type.filter`.
+            self.namespaces = [basic]
+        else:
+            self.namespaces = [namespace]
 
-        As of now, this method is not implemented and was previously used for transferring memory to and from GPU.
+        self.default_instance_seed = seed
+        self.state_updates = []
+        self.gen_seedgen = np.random.SeedSequence(seed)
 
-        Parameters
-        ----------
-        value: array-like
-        storage: array-like
-            The old value (e.g. the old NumPy array)
-        strict: bool
-        allow_downcast: bool (optional)
-
-        Raises
-        ------
-        NotImplementedError
-        """
-        raise NotImplementedError()
+        if isinstance(rng_ctor, type) and issubclass(rng_ctor, np.random.RandomState):
 
-    def filter_variable(
-        self, other: Union[Variable, D], allow_convert: bool = True
-    ) -> variable_type:
-        r"""Convert a `other` into a `Variable` with a `Type` that's compatible with `self`.
+            # The legacy state does not accept `SeedSequence`s directly
+            def rng_ctor(seed):
+                return np.random.RandomState(np.random.MT19937(seed))
 
-        If the involved `Type`\s are not compatible, a `TypeError` will be raised.
-        """
-        if not isinstance(other, Variable):
-            # The value is not a Variable: we cast it into
-            # a Constant of the appropriate Type.
-            other = self.constant_type(type=self, data=other)
-
-        if other.type != self and allow_convert:
-            other2 = self.convert_variable(other)
-            if other2 is not None:
-                return other2
-
-        if other.type != self:
-            raise TypeError(
-                f"Cannot convert Type {other.type} "
-                f"(of Variable {other}) into Type {self}. "
-                f"You can try to manually convert {other} into a {self}."
-            )
-        return other
-
-    def convert_variable(self, var: Variable) -> Optional[Variable]:
-        """Produce a `Variable` that's compatible with both `self` and `var.type`, if possible.
+        self.rng_ctor = rng_ctor
 
-        A compatible `Variable` is a `Variable` with a `Type` that's the
-        "narrower" of `self` and `var.type`.
+    def __getattr__(self, obj):
 
-        If a compatible `Type` cannot be found, this method will return
-        ``None``.
+        ns_obj = next(
+            (getattr(ns, obj) for ns in self.namespaces if hasattr(ns, obj)), None
+        )
 
-        """
-        var_type = var.type
+        if ns_obj is None:
+            raise AttributeError(f"No attribute {obj}.")
 
-        if self.is_super(var_type):
-            # `var.type` is at least as specific as `self`, so we return it
-            # as-is
-            return var
-        elif var_type.is_super(self):
-            # `var.type` is less specific than `self`, so we need to convert it
-            # to `self`'s `Type`.
-            #
-            # Note that, in this case, `var.type != self`, because equality is
-            # covered by the branch above.
-            raise NotImplementedError()
-
-        return None
-
-    def is_valid_value(self, data: D, strict: bool = True) -> bool:
-        """Return ``True`` for any python object that would be a legal value for a `Variable` of this `Type`."""
-        try:
-            self.filter(data, strict=strict)
-            return True
-        except (TypeError, ValueError):
-            return False
+        from pytensor.tensor.random.op import RandomVariable
 
-    def make_variable(self, name: Optional[str] = None) -> variable_type:
-        """Return a new `Variable` instance of this `Type`.
+        if isinstance(ns_obj, RandomVariable):
 
-        Parameters
-        ----------
-        name: None or str
-            A pretty string for printing and debugging.
+            @wraps(ns_obj)
+            def meta_obj(*args, **kwargs):
+                return self.gen(ns_obj, *args, **kwargs)
 
-        """
-        return self.variable_type(self, None, name=name)
+        else:
+            raise AttributeError(f"No attribute {obj}.")
 
-    def make_constant(self, value: D, name: Optional[str] = None) -> constant_type:
-        """Return a new `Constant` instance of this `Type`.
+        setattr(self, obj, meta_obj)
+        return getattr(self, obj)
 
-        Parameters
-        ----------
-        value: array-like
-            The constant value.
-        name: None or str
-            A pretty string for printing and debugging.
+    def updates(self):
+        return list(self.state_updates)
 
+    def seed(self, seed=None):
         """
-        return self.constant_type(type=self, data=value, name=name)
-
-    def clone(self, *args, **kwargs) -> "Type":
-        """Clone a copy of this type with the given arguments/keyword values, if any."""
-        return type(self)(*args, **kwargs)
-
-    def __call__(self, name: Optional[str] = None) -> variable_type:
-        """Return a new `Variable` instance of Type `self`.
+        Re-initialize each random stream.
 
         Parameters
         ----------
-        name : None or str
-            A pretty string for printing and debugging.
+        seed : None or integer
+            Each random stream will be assigned a unique state that depends
+            deterministically on this value.
 
-        """
-        return utils.add_tag_trace(self.make_variable(name))
-
-    @classmethod
-    def values_eq(cls, a: D, b: D) -> bool:
-        """Return ``True`` if `a` and `b` can be considered exactly equal.
-
-        `a` and `b` are assumed to be valid values of this `Type`.
+        Returns
+        -------
+        None
 
         """
-        return a == b
+        if seed is None:
+            seed = self.default_instance_seed
+
+        self.gen_seedgen = np.random.SeedSequence(seed)
+        old_r_seeds = self.gen_seedgen.spawn(len(self.state_updates))
 
-    @classmethod
-    def values_eq_approx(cls, a: D, b: D) -> bool:
-        """Return ``True`` if `a` and `b` can be considered approximately equal.
-
-        This function is used by PyTensor debugging tools to decide
-        whether two values are equivalent, admitting a certain amount
-        of numerical instability. For example, for floating-point
-        numbers this function should be an approximate comparison.
+        for (old_r, new_r), old_r_seed in zip(self.state_updates, old_r_seeds):
+            old_r.set_value(self.rng_ctor(old_r_seed), borrow=True)
 
-        By default, this does an exact comparison.
+    def gen(self, op: "RandomVariable", *args, **kwargs) -> TensorVariable:
+        r"""Generate a draw from `op` seeded from this `RandomStream`.
 
         Parameters
         ----------
-        a: array-like
-            A potential value for a `Variable` of this `Type`.
-        b: array-like
-            A potential value for a `Variable` of this `Type`.
+        op
+            A `RandomVariable` instance
+        args
+            Positional arguments passed to `op`.
+        kwargs
+            Keyword arguments passed to `op`.
 
         Returns
         -------
-        bool
+        The symbolic random draw performed by `op`.  This function stores
+        the updated `RandomType`\s for use at compile time.
 
         """
-        return cls.values_eq(a, b)
+        if "rng" in kwargs:
+            raise ValueError(
+                "The `rng` option cannot be used with a variate in a `RandomStream`"
+            )
 
+        # Generate a new random state
+        (seed,) = self.gen_seedgen.spawn(1)
+        rng = shared(self.rng_ctor(seed), borrow=True)
 
-class HasDataType:
-    """A mixin for a type that has a :attr:`dtype` attribute."""
+        # Generate the sample
+        out = op(*args, **kwargs, rng=rng)
 
-    dtype: str
+        # This is the value that should be used to replace the old state
+        # (i.e. `rng`) after `out` is sampled/evaluated.
+        # The updates mechanism in `pytensor.function` is supposed to perform
+        # this replace action.
+        new_rng = out.owner.outputs[0]
 
+        self.state_updates.append((rng, new_rng))
 
-class HasShape:
-    """A mixin for a type that has :attr:`shape` and :attr:`ndim` attributes."""
+        rng.default_update = new_rng
 
-    ndim: int
-    shape: Tuple[Optional[int], ...]
+        return out
```

### Comparing `pytensor-2.8.11/pytensor/graph/utils.py` & `pytensor-2.9.1/pytensor/graph/utils.py`

 * *Files 11% similar despite different names*

```diff
@@ -300,19 +300,14 @@
 
         if getattr(self, "attr", None) == attr:
             obj = self.attr_filter(obj)
 
         return object.__setattr__(self, attr, obj)
 
 
-class D:
-    def __init__(self, **d):
-        self.__dict__.update(d)
-
-
 class AssocList:
     """An associative list.
 
     This class is like a `dict` that accepts unhashable keys by using an
     assoc list for internal use only
     """
 
@@ -375,48 +370,7 @@
 
     def clear(self):
         self._dict = {}
         self._list = []
 
     def __repr__(self):
         return f"AssocList({self._dict}, {self._list})"
-
-
-def toposort(prereqs_d):
-    """
-    Sorts prereqs_d.keys() topologically.
-
-    prereqs_d[x] contains all the elements that must come before x
-    in the ordering.
-
-    """
-
-    #     all1 = set(prereqs_d.keys())
-    #     all2 = set()
-    #     for x, y in prereqs_d.items():
-    #         all2.update(y)
-    #     print all1.difference(all2)
-
-    seq = []
-    done = set()
-    postreqs_d = {}
-    for x, prereqs in prereqs_d.items():
-        for prereq in prereqs:
-            postreqs_d.setdefault(prereq, set()).add(x)
-    next = {k for k in prereqs_d if not prereqs_d[k]}
-    while next:
-        bases = next
-        next = set()
-        for x in bases:
-            done.add(x)
-            seq.append(x)
-        for x in bases:
-            for postreq in postreqs_d.get(x, []):
-                if not prereqs_d[postreq].difference(done):
-                    next.add(postreq)
-    if len(prereqs_d) != len(seq):
-        raise Exception(
-            "Cannot sort topologically: there might be cycles, "
-            "prereqs_d does not have a key for each element or "
-            "some orderings contain invalid elements."
-        )
-    return seq
```

### Comparing `pytensor-2.8.11/pytensor/ifelse.py` & `pytensor-2.9.1/pytensor/ifelse.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/basic.py` & `pytensor-2.9.1/pytensor/link/basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/basic.py` & `pytensor-2.9.1/pytensor/link/c/basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/c_code/lazylinker_c.c` & `pytensor-2.9.1/pytensor/link/c/c_code/lazylinker_c.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/c_code/pytensor_mod_helper.h` & `pytensor-2.9.1/pytensor/link/c/c_code/pytensor_mod_helper.h`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/cmodule.py` & `pytensor-2.9.1/pytensor/link/c/cmodule.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/cutils.py` & `pytensor-2.9.1/pytensor/link/c/cutils.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/cvm.py` & `pytensor-2.9.1/pytensor/link/c/cvm.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/interface.py` & `pytensor-2.9.1/pytensor/link/c/interface.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/lazylinker_c.py` & `pytensor-2.9.1/pytensor/link/c/lazylinker_c.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/op.py` & `pytensor-2.9.1/pytensor/link/c/op.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/params_type.py` & `pytensor-2.9.1/pytensor/link/c/params_type.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/c/type.py` & `pytensor-2.9.1/pytensor/link/c/type.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/__init__.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/basic.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/elemwise.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/elemwise.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/extra_ops.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/extra_ops.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/nlinalg.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/nlinalg.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import jax.numpy as jnp
 
 from pytensor.link.jax.dispatch import jax_funcify
 from pytensor.tensor.blas import BatchedDot
 from pytensor.tensor.math import Dot, MaxAndArgmax
-from pytensor.tensor.nlinalg import SVD, Det, Eig, Eigh, MatrixInverse, QRFull
+from pytensor.tensor.nlinalg import SVD, Det, Eig, Eigh, MatrixInverse, QRFull, SLogDet
 
 
 @jax_funcify.register(SVD)
 def jax_funcify_SVD(op, **kwargs):
     full_matrices = op.full_matrices
     compute_uv = op.compute_uv
 
@@ -21,14 +21,22 @@
 def jax_funcify_Det(op, **kwargs):
     def det(x):
         return jnp.linalg.det(x)
 
     return det
 
 
+@jax_funcify.register(SLogDet)
+def jax_funcify_SLogDet(op, **kwargs):
+    def slogdet(x):
+        return jnp.linalg.slogdet(x)
+
+    return slogdet
+
+
 @jax_funcify.register(Eig)
 def jax_funcify_Eig(op, **kwargs):
     def eig(x):
         return jnp.linalg.eig(x)
 
     return eig
```

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/random.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/random.py`

 * *Files 27% similar despite different names*

```diff
@@ -121,16 +121,17 @@
 def jax_sample_fn_generic(op):
     """Generic JAX implementation of random variables."""
     name = op.name
     jax_op = getattr(jax.random, name)
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
-        sample = jax_op(rng_key, *parameters, shape=size, dtype=dtype)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
+        sample = jax_op(sampling_key, *parameters, shape=size, dtype=dtype)
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.CauchyRV)
 @jax_sample_fn.register(aer.GumbelRV)
@@ -147,33 +148,35 @@
 
     """
     name = op.name
     jax_op = getattr(jax.random, name)
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         loc, scale = parameters
-        sample = loc + jax_op(rng_key, size, dtype) * scale
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = loc + jax_op(sampling_key, size, dtype) * scale
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.BernoulliRV)
 @jax_sample_fn.register(aer.CategoricalRV)
 def jax_sample_fn_no_dtype(op):
     """Generic JAX implementation of random variables."""
     name = op.name
     jax_op = getattr(jax.random, name)
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
-        sample = jax_op(rng_key, *parameters, shape=size)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
+        sample = jax_op(sampling_key, *parameters, shape=size)
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.RandIntRV)
 @jax_sample_fn.register(aer.UniformRV)
@@ -185,17 +188,20 @@
 
     """
     name = op.name
     jax_op = getattr(jax.random, name)
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         minval, maxval = parameters
-        sample = jax_op(rng_key, shape=size, dtype=dtype, minval=minval, maxval=maxval)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = jax_op(
+            sampling_key, shape=size, dtype=dtype, minval=minval, maxval=maxval
+        )
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.ParetoRV)
 @jax_sample_fn.register(aer.GammaRV)
@@ -207,88 +213,111 @@
 
     """
     name = op.name
     jax_op = getattr(jax.random, name)
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         (shape, rate) = parameters
-        sample = jax_op(rng_key, shape, size, dtype) / rate
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = jax_op(sampling_key, shape, size, dtype) / rate
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.ExponentialRV)
 def jax_sample_fn_exponential(op):
     """JAX implementation of `ExponentialRV`."""
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         (scale,) = parameters
-        sample = jax.random.exponential(rng_key, size, dtype) * scale
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = jax.random.exponential(sampling_key, size, dtype) * scale
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.StudentTRV)
 def jax_sample_fn_t(op):
     """JAX implementation of `StudentTRV`."""
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         (
             df,
             loc,
             scale,
         ) = parameters
-        sample = loc + jax.random.t(rng_key, df, size, dtype) * scale
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = loc + jax.random.t(sampling_key, df, size, dtype) * scale
+        rng["jax_state"] = rng_key
+        return (rng, sample)
+
+    return sample_fn
+
+
+@jax_sample_fn.register(aer.HalfNormalRV)
+def jax_sample_fn_halfnormal(op):
+    """JAX implementation of `HalfNormalRV`."""
+
+    def sample_fn(rng, size, dtype, *parameters):
+        rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
+        loc, scale = parameters
+        sample = (
+            loc + jax.numpy.abs(jax.random.normal(sampling_key, size, dtype)) * scale
+        )
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.ChoiceRV)
 def jax_funcify_choice(op):
     """JAX implementation of `ChoiceRV`."""
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         (a, p, replace) = parameters
-        smpl_value = jax.random.choice(rng_key, a, size, replace, p)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        smpl_value = jax.random.choice(sampling_key, a, size, replace, p)
+        rng["jax_state"] = rng_key
         return (rng, smpl_value)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.PermutationRV)
 def jax_sample_fn_permutation(op):
     """JAX implementation of `PermutationRV`."""
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         (x,) = parameters
-        sample = jax.random.permutation(rng_key, x)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        sample = jax.random.permutation(sampling_key, x)
+        rng["jax_state"] = rng_key
         return (rng, sample)
 
     return sample_fn
 
 
 @jax_sample_fn.register(aer.LogNormalRV)
 def jax_sample_fn_lognormal(op):
     """JAX implementation of `LogNormalRV`."""
 
     def sample_fn(rng, size, dtype, *parameters):
         rng_key = rng["jax_state"]
+        rng_key, sampling_key = jax.random.split(rng_key, 2)
         loc, scale = parameters
-        sample = loc + jax.random.normal(rng_key, size, dtype) * scale
+        sample = loc + jax.random.normal(sampling_key, size, dtype) * scale
         sample_exp = jax.numpy.exp(sample)
-        rng["jax_state"] = jax.random.split(rng_key, num=1)[0]
+        rng["jax_state"] = rng_key
         return (rng, sample_exp)
 
     return sample_fn
```

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/scalar.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/scalar.py`

 * *Files 2% similar despite different names*

```diff
@@ -59,19 +59,26 @@
     def clip(x, min, max):
         return jnp.where(x < min, min, jnp.where(x > max, max, x))
 
     return clip
 
 
 @jax_funcify.register(Composite)
-def jax_funcify_Composite(op, vectorize=True, **kwargs):
+def jax_funcify_Composite(op, node, vectorize=True, **kwargs):
     jax_impl = jax_funcify(op.fgraph)
 
-    def composite(*args):
-        return jax_impl(*args)[0]
+    if len(node.outputs) == 1:
+
+        def composite(*args):
+            return jax_impl(*args)[0]
+
+    else:
+
+        def composite(*args):
+            return jax_impl(*args)
 
     return jnp.vectorize(composite)
 
 
 @jax_funcify.register(Second)
 def jax_funcify_Second(op, **kwargs):
     def second(x, y):
```

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/scan.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/scan.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/shape.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/shape.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/slinalg.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/slinalg.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/subtensor.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/subtensor.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/tensor_basic.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/tensor_basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/dispatch/test_subtensor.py` & `pytensor-2.9.1/pytensor/link/jax/dispatch/test_subtensor.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/jax/linker.py` & `pytensor-2.9.1/pytensor/link/jax/linker.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/basic.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/basic.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 import operator
 import sys
 import warnings
 from contextlib import contextmanager
+from copy import copy
 from functools import singledispatch
 from textwrap import dedent
 from typing import Union
 
 import numba
 import numba.np.unsafe.ndarray as numba_ndarray
 import numpy as np
 import scipy
 import scipy.special
 from llvmlite import ir
 from numba import types
 from numba.core.errors import TypingError
 from numba.cpython.unsafe.tuple import tuple_setitem  # noqa: F401
-from numba.extending import box
+from numba.extending import box, overload
 
 from pytensor import config
 from pytensor.compile.builders import OpFromGraph
 from pytensor.compile.ops import DeepCopyOp
 from pytensor.graph.basic import Apply, NoParams
 from pytensor.graph.fg import FunctionGraph
 from pytensor.graph.type import Type
@@ -43,14 +44,22 @@
     IncSubtensor,
     Subtensor,
 )
 from pytensor.tensor.type import TensorType
 from pytensor.tensor.type_other import MakeSlice, NoneConst
 
 
+def global_numba_func(func):
+    """Use to return global numba functions in numba_funcify_*.
+
+    This allows tests to remove the compilation using mock.
+    """
+    return func
+
+
 def numba_njit(*args, **kwargs):
 
     kwargs = kwargs.copy()
     kwargs.setdefault("cache", config.numba__cache)
 
     if len(args) > 0 and callable(args[0]):
         return numba.njit(*args[1:], **kwargs)(args[0])
@@ -191,15 +200,15 @@
             return lambda x, y: False
 
 
 enable_slice_boxing()
 
 
 def to_scalar(x):
-    raise NotImplementedError()
+    return np.asarray(x).item()
 
 
 @numba.extending.overload(to_scalar)
 def impl_to_scalar(x):
     if isinstance(x, (numba.types.Number, numba.types.Boolean)):
         return lambda x: x
     elif isinstance(x, numba.types.Array):
@@ -530,15 +539,15 @@
         """
 
     subtensor_def_src = f"""
 def {fn_name}({", ".join(input_names)}):
     {index_prologue}
     {indices_creation_src}
     {index_body}
-    return z
+    return np.asarray(z)
     """
 
     return subtensor_def_src
 
 
 @numba_funcify.register(Subtensor)
 @numba_funcify.register(AdvancedSubtensor1)
@@ -569,94 +578,98 @@
     incsubtensor_fn = compile_function_src(
         incsubtensor_def_src, "incsubtensor", {**globals(), **global_env}
     )
 
     return numba_njit(incsubtensor_fn, boundscheck=True)
 
 
+@numba_njit(boundscheck=True)
+def advancedincsubtensor1_inplace_set(x, vals, idxs):
+    for idx, val in zip(idxs, vals):
+        x[idx] = val
+    return x
+
+
+@numba_njit(boundscheck=True)
+def advancedincsubtensor1_inplace_inc(x, vals, idxs):
+    for idx, val in zip(idxs, vals):
+        x[idx] += val
+    return x
+
+
 @numba_funcify.register(AdvancedIncSubtensor1)
 def numba_funcify_AdvancedIncSubtensor1(op, node, **kwargs):
     inplace = op.inplace
     set_instead_of_inc = op.set_instead_of_inc
 
     if set_instead_of_inc:
-
-        @numba_njit(boundscheck=True)
-        def advancedincsubtensor1_inplace(x, vals, idxs):
-            for idx, val in zip(idxs, vals):
-                x[idx] = val
-            return x
-
+        advancedincsubtensor1_inplace = global_numba_func(
+            advancedincsubtensor1_inplace_set
+        )
     else:
-
-        @numba_njit(boundscheck=True)
-        def advancedincsubtensor1_inplace(x, vals, idxs):
-            for idx, val in zip(idxs, vals):
-                x[idx] += val
-            return x
+        advancedincsubtensor1_inplace = global_numba_func(
+            advancedincsubtensor1_inplace_inc
+        )
 
     if inplace:
-        return advancedincsubtensor1_inplace
+        return global_numba_func(advancedincsubtensor1_inplace)
     else:
 
         @numba_njit
         def advancedincsubtensor1(x, vals, idxs):
             x = x.copy()
             return advancedincsubtensor1_inplace(x, vals, idxs)
 
         return advancedincsubtensor1
 
 
-@numba_funcify.register(DeepCopyOp)
-def numba_funcify_DeepCopyOp(op, node, **kwargs):
+def deepcopyop(x):
+    return copy(x)
 
-    # Scalars are apparently returned as actual Python scalar types and not
-    # NumPy scalars, so we need two separate Numba functions for each case.
 
-    # The type can also be RandomType with no ndims
-    if not hasattr(node.outputs[0].type, "ndim") or node.outputs[0].type.ndim == 0:
-        # TODO: Do we really need to compile a pass-through function like this?
-        @numba_njit(inline="always")
-        def deepcopyop(x):
-            return x
+@overload(deepcopyop)
+def dispatch_deepcopyop(x):
+    if isinstance(x, types.Array):
+        return lambda x: np.copy(x)
 
-    else:
+    return lambda x: x
 
-        @numba_njit(inline="always")
-        def deepcopyop(x):
-            return x.copy()
 
+@numba_funcify.register(DeepCopyOp)
+def numba_funcify_DeepCopyOp(op, node, **kwargs):
     return deepcopyop
 
 
+@numba_njit
+def makeslice(*x):
+    return slice(*x)
+
+
 @numba_funcify.register(MakeSlice)
 def numba_funcify_MakeSlice(op, **kwargs):
-    @numba_njit
-    def makeslice(*x):
-        return slice(*x)
+    return global_numba_func(makeslice)
 
-    return makeslice
+
+@numba_njit
+def shape(x):
+    return np.asarray(np.shape(x))
 
 
 @numba_funcify.register(Shape)
 def numba_funcify_Shape(op, **kwargs):
-    @numba_njit(inline="always")
-    def shape(x):
-        return np.asarray(np.shape(x))
-
-    return shape
+    return global_numba_func(shape)
 
 
 @numba_funcify.register(Shape_i)
 def numba_funcify_Shape_i(op, **kwargs):
     i = op.i
 
-    @numba_njit(inline="always")
+    @numba_njit
     def shape_i(x):
-        return np.shape(x)[i]
+        return np.asarray(np.shape(x)[i])
 
     return shape_i
 
 
 @numba.extending.intrinsic
 def direct_cast(typingctx, val, typ):
 
@@ -679,21 +692,21 @@
 
 @numba_funcify.register(Reshape)
 def numba_funcify_Reshape(op, **kwargs):
     ndim = op.ndim
 
     if ndim == 0:
 
-        @numba_njit(inline="always")
+        @numba_njit
         def reshape(x, shape):
-            return x.item()
+            return np.asarray(x.item())
 
     else:
 
-        @numba_njit(inline="always")
+        @numba_njit
         def reshape(x, shape):
             # TODO: Use this until https://github.com/numba/numba/issues/7353 is closed.
             return np.reshape(
                 np.ascontiguousarray(np.asarray(x)),
                 numba_ndarray.to_fixed_tuple(shape, ndim),
             )
 
@@ -728,74 +741,75 @@
 def int_to_float_fn(inputs, out_dtype):
     """Create a Numba function that converts integer and boolean ``ndarray``s to floats."""
 
     if any(i.type.numpy_dtype.kind in "ib" for i in inputs):
 
         args_dtype = np.dtype(f"f{out_dtype.itemsize}")
 
-        @numba_njit(inline="always")
+        @numba_njit
         def inputs_cast(x):
             return x.astype(args_dtype)
 
     else:
         args_dtype_sz = max(_arg.type.numpy_dtype.itemsize for _arg in inputs)
         args_dtype = np.dtype(f"f{args_dtype_sz}")
 
-        @numba_njit(inline="always")
+        @numba_njit
         def inputs_cast(x):
             return x.astype(args_dtype)
 
     return inputs_cast
 
 
 @numba_funcify.register(Dot)
 def numba_funcify_Dot(op, node, **kwargs):
     # Numba's `np.dot` does not support integer dtypes, so we need to cast to
     # float.
 
     out_dtype = node.outputs[0].type.numpy_dtype
     inputs_cast = int_to_float_fn(node.inputs, out_dtype)
 
-    @numba_njit(inline="always")
+    @numba_njit
     def dot(x, y):
         return np.asarray(np.dot(inputs_cast(x), inputs_cast(y))).astype(out_dtype)
 
     return dot
 
 
 @numba_funcify.register(Softplus)
 def numba_funcify_Softplus(op, node, **kwargs):
 
     x_dtype = np.dtype(node.inputs[0].dtype)
 
     @numba_njit
     def softplus(x):
         if x < -37.0:
-            return direct_cast(np.exp(x), x_dtype)
+            value = np.exp(x)
         elif x < 18.0:
-            return direct_cast(np.log1p(np.exp(x)), x_dtype)
+            value = np.log1p(np.exp(x))
         elif x < 33.3:
-            return direct_cast(x + np.exp(-x), x_dtype)
+            value = x + np.exp(-x)
         else:
-            return direct_cast(x, x_dtype)
+            value = x
+        return direct_cast(value, x_dtype)
 
     return softplus
 
 
 @numba_funcify.register(Cholesky)
 def numba_funcify_Cholesky(op, node, **kwargs):
     lower = op.lower
 
     out_dtype = node.outputs[0].type.numpy_dtype
 
     if lower:
 
         inputs_cast = int_to_float_fn(node.inputs, out_dtype)
 
-        @numba_njit(inline="always")
+        @numba_njit
         def cholesky(a):
             return np.linalg.cholesky(inputs_cast(a)).astype(out_dtype)
 
     else:
         # TODO: Use SciPy's BLAS/LAPACK Cython wrappers.
 
         warnings.warn(
@@ -848,15 +862,15 @@
                 )
             return ret
 
     else:
         out_dtype = node.outputs[0].type.numpy_dtype
         inputs_cast = int_to_float_fn(node.inputs, out_dtype)
 
-        @numba_njit(inline="always")
+        @numba_njit
         def solve(a, b):
             return np.linalg.solve(
                 inputs_cast(a),
                 inputs_cast(b),
                 # assume_a=assume_a,
                 # check_finite=check_finite,
             ).astype(out_dtype)
```

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/cython_support.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/cython_support.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/elemwise.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/elemwise.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,32 +1,35 @@
-import inspect
+import base64
+import pickle
 from functools import singledispatch
 from numbers import Number
 from textwrap import indent
 from typing import Any, Callable, Optional, Union
 
 import numba
 import numpy as np
+from numba import TypingError, types
+from numba.core import cgutils
+from numba.core.extending import overload
+from numba.np import arrayobj
 from numpy.core.numeric import normalize_axis_index, normalize_axis_tuple
 
 from pytensor import config
 from pytensor.graph.basic import Apply
 from pytensor.graph.op import Op
 from pytensor.link.numba.dispatch import basic as numba_basic
+from pytensor.link.numba.dispatch import elemwise_codegen
 from pytensor.link.numba.dispatch.basic import (
     create_numba_signature,
     create_tuple_creator,
     numba_funcify,
+    numba_njit,
     use_optimized_cheap_pass,
 )
-from pytensor.link.utils import (
-    compile_function_src,
-    get_name_for_object,
-    unique_name_generator,
-)
+from pytensor.link.utils import compile_function_src, get_name_for_object
 from pytensor.scalar.basic import (
     AND,
     OR,
     XOR,
     Add,
     Composite,
     IntDiv,
@@ -36,15 +39,15 @@
     ScalarMinimum,
     Sub,
     TrueDiv,
 )
 from pytensor.scalar.basic import add as add_as
 from pytensor.scalar.basic import scalar_maximum
 from pytensor.tensor.elemwise import CAReduce, DimShuffle, Elemwise
-from pytensor.tensor.math import MaxAndArgmax, MulWithoutZeros
+from pytensor.tensor.math import MaxAndArgmax, MulWithoutZeros, Sum
 from pytensor.tensor.special import LogSoftmax, Softmax, SoftmaxGrad
 from pytensor.tensor.type import scalar
 
 
 @singledispatch
 def scalar_in_place_fn(op: Op, idx: str, res: str, arr: str):
     """Return code for an in-place update on an array using a binary scalar :class:`Op`.
@@ -168,14 +171,15 @@
 def create_axis_reducer(
     scalar_op: Op,
     identity: Union[np.ndarray, Number],
     axis: int,
     ndim: int,
     dtype: numba.types.Type,
     keepdims: bool = False,
+    return_scalar=False,
 ) -> numba.core.dispatcher.Dispatcher:
     r"""Create Python function that performs a NumPy-like reduction on a given axis.
 
     The functions generated by this function take the following form:
 
     .. code-block:: python
 
@@ -278,14 +282,16 @@
     return {return_expr}
         """
     else:
         inplace_update_statement = scalar_in_place_fn(scalar_op, "0", "res", "x[i]")
         inplace_update_statement = indent(inplace_update_statement, " " * 4 * 2)
 
         return_expr = "res" if keepdims else "res.item()"
+        if not return_scalar:
+            return_expr = f"np.asarray({return_expr})"
         reduce_elemwise_def_src = f"""
 def {reduce_elemwise_fn_name}(x):
 
     res = np.full(1, numba_basic.to_scalar({identity}), dtype=out_dtype)
 
     axis_shape = x.shape[{axis}]
 
@@ -299,15 +305,21 @@
         reduce_elemwise_def_src, reduce_elemwise_fn_name, {**globals(), **global_env}
     )
 
     return reduce_elemwise_fn_py
 
 
 def create_multiaxis_reducer(
-    scalar_op, identity, axes, ndim, dtype, input_name="input"
+    scalar_op,
+    identity,
+    axes,
+    ndim,
+    dtype,
+    input_name="input",
+    return_scalar=False,
 ):
     r"""Construct a function that reduces multiple axes.
 
     The functions generated by this function take the following form:
 
     .. code-block:: python
 
@@ -330,14 +342,16 @@
         The identity value for the reduction.
     axes:
         The axes to reduce.
     ndim:
         The number of dimensions of the result.
     dtype:
         The data type of the result.
+    return_scalar:
+        If True, return a scalar, otherwise an array.
 
     Returns
     =======
     A Python function that can be JITed.
 
     """
     if len(axes) == 1:
@@ -364,28 +378,35 @@
         last_var_name = var_name
         var_name = f"axis_{i}_res"
         careduce_lines_src.append(
             f"{var_name} = {careducer_axes_fn_name}({last_var_name})"
         )
 
     careduce_assign_lines = indent("\n".join(careduce_lines_src), " " * 4)
+    if not return_scalar:
+        pre_result = "np.asarray"
+        post_result = ""
+    else:
+        pre_result = "np.asarray"
+        post_result = ".item()"
+
     careduce_def_src = f"""
 def {careduce_fn_name}({input_name}):
 {careduce_assign_lines}
-    return {var_name}
+    return {pre_result}({var_name}){post_result}
     """
 
     careduce_fn = compile_function_src(
         careduce_def_src, careduce_fn_name, {**globals(), **global_env}
     )
 
     return careduce_fn
 
 
-def jit_compile_reducer(node, fn, **kwds):
+def jit_compile_reducer(node, fn, *, reduce_to_scalar=False, **kwds):
     """Compile Python source for reduction loops using additional optimizations.
 
     Parameters
     ==========
     node
         An node from which the signature can be derived.
     fn
@@ -394,15 +415,15 @@
         Extra keywords to be added to the :func:`numba.njit` function.
 
     Returns
     =======
     A :func:`numba.njit`-compiled function.
 
     """
-    signature = create_numba_signature(node, reduce_to_scalar=True)
+    signature = create_numba_signature(node, reduce_to_scalar=reduce_to_scalar)
 
     # Eagerly compile the function using increased optimizations.  This should
     # help improve nested loop reductions.
     with use_optimized_cheap_pass():
         res = numba_basic.numba_njit(
             signature,
             boundscheck=False,
@@ -427,73 +448,288 @@
             v = fn(x_reaxis[m])
             res[m] = v
         return res
 
     return axis_apply_fn
 
 
+_jit_options = {
+    "fastmath": {
+        "arcp",  # Allow Reciprocal
+        "contract",  # Allow floating-point contraction
+        "afn",  # Approximate functions
+        "reassoc",
+        "nsz",  # TODO Do we want this one?
+    }
+}
+
+
+@numba.extending.intrinsic(jit_options=_jit_options, prefer_literal=True)
+def _vectorized(
+    typingctx,
+    scalar_func,
+    input_bc_patterns,
+    output_bc_patterns,
+    output_dtypes,
+    inplace_pattern,
+    inputs,
+):
+    arg_types = [
+        scalar_func,
+        input_bc_patterns,
+        output_bc_patterns,
+        output_dtypes,
+        inplace_pattern,
+        inputs,
+    ]
+
+    if not isinstance(input_bc_patterns, types.Literal):
+        raise TypingError("input_bc_patterns must be literal.")
+    input_bc_patterns = input_bc_patterns.literal_value
+    input_bc_patterns = pickle.loads(base64.decodebytes(input_bc_patterns.encode()))
+
+    if not isinstance(output_bc_patterns, types.Literal):
+        raise TypeError("output_bc_patterns must be literal.")
+    output_bc_patterns = output_bc_patterns.literal_value
+    output_bc_patterns = pickle.loads(base64.decodebytes(output_bc_patterns.encode()))
+
+    if not isinstance(output_dtypes, types.Literal):
+        raise TypeError("output_dtypes must be literal.")
+    output_dtypes = output_dtypes.literal_value
+    output_dtypes = pickle.loads(base64.decodebytes(output_dtypes.encode()))
+
+    if not isinstance(inplace_pattern, types.Literal):
+        raise TypeError("inplace_pattern must be literal.")
+    inplace_pattern = inplace_pattern.literal_value
+    inplace_pattern = pickle.loads(base64.decodebytes(inplace_pattern.encode()))
+
+    n_outputs = len(output_bc_patterns)
+
+    if not len(inputs) > 0:
+        raise TypingError("Empty argument list to elemwise op.")
+
+    if not n_outputs > 0:
+        raise TypingError("Empty list of outputs for elemwise op.")
+
+    if not all(isinstance(input, types.Array) for input in inputs):
+        raise TypingError("Inputs to elemwise must be arrays.")
+    ndim = inputs[0].ndim
+
+    if not all(input.ndim == ndim for input in inputs):
+        raise TypingError("Inputs to elemwise must have the same rank.")
+
+    if not all(len(pattern) == ndim for pattern in output_bc_patterns):
+        raise TypingError("Invalid output broadcasting pattern.")
+
+    scalar_signature = typingctx.resolve_function_type(
+        scalar_func, [in_type.dtype for in_type in inputs], {}
+    )
+
+    # So we can access the constant values in codegen...
+    input_bc_patterns_val = input_bc_patterns
+    output_bc_patterns_val = output_bc_patterns
+    output_dtypes_val = output_dtypes
+    inplace_pattern_val = inplace_pattern
+    input_types = inputs
+
+    def codegen(
+        ctx,
+        builder,
+        sig,
+        args,
+    ):
+
+        [_, _, _, _, _, inputs] = args
+        inputs = cgutils.unpack_tuple(builder, inputs)
+        inputs = [
+            arrayobj.make_array(ty)(ctx, builder, val)
+            for ty, val in zip(input_types, inputs)
+        ]
+        in_shapes = [cgutils.unpack_tuple(builder, obj.shape) for obj in inputs]
+
+        iter_shape = elemwise_codegen.compute_itershape(
+            ctx,
+            builder,
+            in_shapes,
+            input_bc_patterns_val,
+        )
+
+        outputs, output_types = elemwise_codegen.make_outputs(
+            ctx,
+            builder,
+            iter_shape,
+            output_bc_patterns_val,
+            output_dtypes_val,
+            inplace_pattern_val,
+            inputs,
+            input_types,
+        )
+
+        elemwise_codegen.make_loop_call(
+            typingctx,
+            ctx,
+            builder,
+            scalar_func,
+            scalar_signature,
+            iter_shape,
+            inputs,
+            outputs,
+            input_bc_patterns_val,
+            output_bc_patterns_val,
+            input_types,
+            output_types,
+        )
+
+        if len(outputs) == 1:
+            if inplace_pattern:
+                assert inplace_pattern[0][0] == 0
+                ctx.nrt.incref(builder, sig.return_type, outputs[0]._getvalue())
+            return outputs[0]._getvalue()
+
+        for inplace_idx in dict(inplace_pattern):
+            ctx.nrt.incref(
+                builder,
+                sig.return_type.types[inplace_idx],
+                outputs[inplace_idx]._get_value(),
+            )
+        return ctx.make_tuple(
+            builder, sig.return_type, [out._getvalue() for out in outputs]
+        )
+
+    ret_type = types.Tuple(
+        [
+            types.Array(numba.from_dtype(np.dtype(dtype)), ndim, "C")
+            for dtype in output_dtypes
+        ]
+    )
+    if len(output_dtypes) == 1:
+        ret_type = ret_type.types[0]
+    sig = ret_type(*arg_types)
+
+    return sig, codegen
+
+
 @numba_funcify.register(Elemwise)
 def numba_funcify_Elemwise(op, node, **kwargs):
     # Creating a new scalar node is more involved and unnecessary
     # if the scalar_op is composite, as the fgraph already contains
     # all the necessary information.
     scalar_node = None
     if not isinstance(op.scalar_op, Composite):
         scalar_inputs = [scalar(dtype=input.dtype) for input in node.inputs]
         scalar_node = op.scalar_op.make_node(*scalar_inputs)
 
+    flags = {
+        "arcp",  # Allow Reciprocal
+        "contract",  # Allow floating-point contraction
+        "afn",  # Approximate functions
+        "reassoc",
+        "nsz",  # TODO Do we want this one?
+    }
+
     scalar_op_fn = numba_funcify(
-        op.scalar_op, node=scalar_node, parent_node=node, inline="always", **kwargs
+        op.scalar_op, node=scalar_node, parent_node=node, fastmath=flags, **kwargs
     )
-    elemwise_fn = create_vectorize_func(scalar_op_fn, node, use_signature=False)
-    elemwise_fn_name = elemwise_fn.__name__
 
-    if op.inplace_pattern:
-        input_idx = op.inplace_pattern[0]
-        sign_obj = inspect.signature(elemwise_fn.py_scalar_func)
-        input_names = list(sign_obj.parameters.keys())
+    ndim = node.outputs[0].ndim
+    output_bc_patterns = tuple([(False,) * ndim for _ in node.outputs])
+    input_bc_patterns = tuple([input_var.broadcastable for input_var in node.inputs])
+    output_dtypes = tuple(variable.dtype for variable in node.outputs)
+    inplace_pattern = tuple(op.inplace_pattern.items())
+
+    # numba doesn't support nested literals right now...
+    input_bc_patterns_enc = base64.encodebytes(pickle.dumps(input_bc_patterns)).decode()
+    output_bc_patterns_enc = base64.encodebytes(
+        pickle.dumps(output_bc_patterns)
+    ).decode()
+    output_dtypes_enc = base64.encodebytes(pickle.dumps(output_dtypes)).decode()
+    inplace_pattern_enc = base64.encodebytes(pickle.dumps(inplace_pattern)).decode()
+
+    def elemwise_wrapper(*inputs):
+        return _vectorized(
+            scalar_op_fn,
+            input_bc_patterns_enc,
+            output_bc_patterns_enc,
+            output_dtypes_enc,
+            inplace_pattern_enc,
+            inputs,
+        )
+
+    # Pure python implementation, that will be used in tests
+    def elemwise(*inputs):
+        inputs = [np.asarray(input) for input in inputs]
+        inputs_bc = np.broadcast_arrays(*inputs)
+        shape = inputs[0].shape
+        for input, bc in zip(inputs, input_bc_patterns):
+            for length, allow_bc, iter_length in zip(input.shape, bc, shape):
+                if length == 1 and shape and iter_length != 1 and not allow_bc:
+                    raise ValueError("Broadcast not allowed.")
+
+        outputs = []
+        for dtype in output_dtypes:
+            outputs.append(np.empty(shape, dtype=dtype))
+
+        for idx in np.ndindex(shape):
+            vals = [input[idx] for input in inputs_bc]
+            outs = scalar_op_fn(*vals)
+            if not isinstance(outs, tuple):
+                outs = (outs,)
+            for out, out_val in zip(outputs, outs):
+                out[idx] = out_val
+
+        outputs_summed = []
+        for output, bc in zip(outputs, output_bc_patterns):
+            axes = tuple(np.nonzero(bc)[0])
+            outputs_summed.append(output.sum(axes, keepdims=True))
+        if len(outputs_summed) != 1:
+            return tuple(outputs_summed)
+        return outputs_summed[0]
+
+    @overload(elemwise)
+    def ov_elemwise(*inputs):
+        return elemwise_wrapper
 
-        unique_names = unique_name_generator([elemwise_fn_name, "np"], suffix_sep="_")
-        input_names = [unique_names(i, force_unique=True) for i in input_names]
+    return elemwise
 
-        updated_input_name = input_names[input_idx]
 
-        inplace_global_env = {elemwise_fn_name: elemwise_fn, "np": np}
+@numba_funcify.register(Sum)
+def numba_funcify_Sum(op, node, **kwargs):
+    axes = op.axis
+    if axes is None:
+        axes = list(range(node.inputs[0].ndim))
 
-        inplace_elemwise_fn_name = f"{elemwise_fn_name}_inplace"
+    axes = tuple(axes)
 
-        input_signature_str = ", ".join(input_names)
+    ndim_input = node.inputs[0].ndim
 
-        if node.inputs[input_idx].ndim > 0:
-            inplace_elemwise_src = f"""
-def {inplace_elemwise_fn_name}({input_signature_str}):
-    return {elemwise_fn_name}({input_signature_str + ", " + updated_input_name})
-            """
-        else:
-            # We can't perform in-place updates on Numba scalars, so we need to
-            # convert them to NumPy scalars.
-            # TODO: We should really prevent the rewrites from creating
-            # in-place updates on scalars when the Numba mode is selected (or
-            # in general?).
-            inplace_elemwise_src = f"""
-def {inplace_elemwise_fn_name}({input_signature_str}):
-    {updated_input_name}_scalar = np.asarray({updated_input_name})
-    return {elemwise_fn_name}({input_signature_str + ", " + updated_input_name}_scalar).item()
-            """
-
-        inplace_elemwise_fn = compile_function_src(
-            inplace_elemwise_src,
-            inplace_elemwise_fn_name,
-            {**globals(), **inplace_global_env},
-        )
-        return numba_basic.numba_njit(inline="always", fastmath=config.numba__fastmath)(
-            inplace_elemwise_fn
-        )
+    if hasattr(op, "acc_dtype") and op.acc_dtype is not None:
+        acc_dtype = op.acc_dtype
+    else:
+        acc_dtype = node.outputs[0].type.dtype
 
-    return elemwise_fn
+    np_acc_dtype = np.dtype(acc_dtype)
+
+    out_dtype = np.dtype(node.outputs[0].dtype)
+
+    if ndim_input == len(axes):
+
+        @numba_njit(fastmath=True)
+        def impl_sum(array):
+            return np.asarray(array.sum(), dtype=np_acc_dtype).astype(out_dtype)
+
+    elif len(axes) == 0:
+
+        @numba_njit(fastmath=True)
+        def impl_sum(array):
+            return np.asarray(array, dtype=out_dtype)
+
+    else:
+        impl_sum = numba_funcify_CAReduce(op, node, **kwargs)
+
+    return impl_sum
 
 
 @numba_funcify.register(CAReduce)
 def numba_funcify_CAReduce(op, node, **kwargs):
     axes = op.axis
     if axes is None:
         axes = list(range(node.inputs[0].ndim))
@@ -522,15 +758,15 @@
         scalar_op_identity,
         axes,
         ndim,
         np.dtype(node.outputs[0].type.dtype),
         input_name=input_name,
     )
 
-    careduce_fn = jit_compile_reducer(node, careduce_py_fn)
+    careduce_fn = jit_compile_reducer(node, careduce_py_fn, reduce_to_scalar=False)
     return careduce_fn
 
 
 @numba_funcify.register(DimShuffle)
 def numba_funcify_DimShuffle(op, node, **kwargs):
     shuffle = tuple(op.shuffle)
     transposition = tuple(op.transposition)
@@ -705,15 +941,20 @@
     x_dtype = x_at.type.numpy_dtype
     x_dtype = numba.np.numpy_support.from_dtype(x_dtype)
     axis = op.axis
 
     if axis is not None:
         axis = normalize_axis_index(axis, x_at.ndim)
         reduce_max_py = create_axis_reducer(
-            scalar_maximum, -np.inf, axis, x_at.ndim, x_dtype, keepdims=True
+            scalar_maximum,
+            -np.inf,
+            axis,
+            x_at.ndim,
+            x_dtype,
+            keepdims=True,
         )
         reduce_sum_py = create_axis_reducer(
             add_as, 0.0, axis, x_at.ndim, x_dtype, keepdims=True
         )
 
         jit_fn = numba_basic.numba_njit(
             boundscheck=False, fastmath=config.numba__fastmath
@@ -752,18 +993,25 @@
         axes = tuple(int(ax) for ax in axis)
 
         # NumPy does not support multiple axes for argmax; this is a
         # work-around
         keep_axes = tuple(i for i in range(x_ndim) if i not in axes)
 
         reduce_max_py_fn = create_multiaxis_reducer(
-            scalar_maximum, -np.inf, axes, x_ndim, x_dtype
+            scalar_maximum,
+            -np.inf,
+            axes,
+            x_ndim,
+            x_dtype,
+            return_scalar=False,
         )
         reduce_max = jit_compile_reducer(
-            Apply(node.op, node.inputs, [node.outputs[0].clone()]), reduce_max_py_fn
+            Apply(node.op, node.inputs, [node.outputs[0].clone()]),
+            reduce_max_py_fn,
+            reduce_to_scalar=False,
         )
 
         reduced_x_ndim = x_ndim - len(axes) + 1
         argmax_axis = create_axis_apply_fn(
             np.argmax, reduced_x_ndim - 1, reduced_x_ndim, np.int64
         )
```

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/extra_ops.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/extra_ops.py`

 * *Files 1% similar despite different names*

```diff
@@ -360,14 +360,15 @@
 @numba_funcify.register(BroadcastTo)
 def numba_funcify_BroadcastTo(op, node, **kwargs):
 
     create_zeros_tuple = numba_basic.create_tuple_creator(
         lambda _: 0, len(node.inputs) - 1
     )
 
+    # TODO broadcastable checks
     @numba_basic.numba_njit
     def broadcast_to(x, *shape):
         scalars_shape = create_zeros_tuple()
 
         i = 0
         for s_i in literal_unroll(shape):
             scalars_shape = numba_basic.tuple_setitem(
```

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/nlinalg.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/nlinalg.py`

 * *Files 8% similar despite different names*

```diff
@@ -14,14 +14,15 @@
     Det,
     Eig,
     Eigh,
     Inv,
     MatrixInverse,
     MatrixPinv,
     QRFull,
+    SLogDet,
 )
 
 
 @numba_funcify.register(SVD)
 def numba_funcify_SVD(op, node, **kwargs):
     full_matrices = op.full_matrices
     compute_uv = op.compute_uv
@@ -54,14 +55,33 @@
     @numba_basic.numba_njit(inline="always")
     def det(x):
         return numba_basic.direct_cast(np.linalg.det(inputs_cast(x)), out_dtype)
 
     return det
 
 
+@numba_funcify.register(SLogDet)
+def numba_funcify_SLogDet(op, node, **kwargs):
+
+    out_dtype_1 = node.outputs[0].type.numpy_dtype
+    out_dtype_2 = node.outputs[1].type.numpy_dtype
+
+    inputs_cast = int_to_float_fn(node.inputs, out_dtype_1)
+
+    @numba_basic.numba_njit
+    def slogdet(x):
+        sign, det = np.linalg.slogdet(inputs_cast(x))
+        return (
+            numba_basic.direct_cast(sign, out_dtype_1),
+            numba_basic.direct_cast(det, out_dtype_2),
+        )
+
+    return slogdet
+
+
 @numba_funcify.register(Eig)
 def numba_funcify_Eig(op, node, **kwargs):
 
     out_dtype_1 = node.outputs[0].type.numpy_dtype
     out_dtype_2 = node.outputs[1].type.numpy_dtype
 
     inputs_cast = int_to_float_fn(node.inputs, out_dtype_1)
```

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/random.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/random.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/scan.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/scan.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,30 +13,37 @@
 )
 from pytensor.link.utils import compile_function_src
 from pytensor.scan.op import Scan
 from pytensor.tensor.type import TensorType
 
 
 def idx_to_str(
-    array_name: str, offset: int, size: Optional[str] = None, idx_symbol: str = "i"
+    array_name: str,
+    offset: int,
+    size: Optional[str] = None,
+    idx_symbol: str = "i",
+    allow_scalar=False,
 ) -> str:
     if offset < 0:
         indices = f"{idx_symbol} + {array_name}.shape[0] - {offset}"
     elif offset > 0:
         indices = f"{idx_symbol} + {offset}"
     else:
         indices = idx_symbol
 
     if size:
         # TODO FIXME: The `Scan` `Op` should tell us which outputs are computed
         # in this way.  We shouldn't have to waste run-time efforts in order to
         # compensate for this poor `Op`/rewrite design and implementation.
         indices = f"({indices}) % {size}"
 
-    return f"{array_name}[{indices}]"
+    if allow_scalar:
+        return f"{array_name}[{indices}]"
+    else:
+        return f"np.asarray({array_name}[{indices}])"
 
 
 @overload(range)
 def array0d_range(x):
     if isinstance(x, types.Array) and x.ndim == 0:
 
         def range_arr(x):
@@ -111,15 +118,17 @@
         outer_in_name: str, tap_offset: Optional[int], storage_size_var: Optional[str]
     ):
         """Construct an inner-input expression."""
         storage_name = outer_in_to_storage_name.get(outer_in_name, outer_in_name)
         indexed_inner_in_str = (
             storage_name
             if tap_offset is None
-            else idx_to_str(storage_name, tap_offset, size=storage_size_var)
+            else idx_to_str(
+                storage_name, tap_offset, size=storage_size_var, allow_scalar=False
+            )
         )
         inner_in_exprs.append(indexed_inner_in_str)
 
     for outer_in_name in outer_in_seqs_names:
         # These outer-inputs are indexed without offsets or storage wrap-around
         add_inner_in_expr(outer_in_name, 0, None)
 
@@ -228,15 +237,20 @@
                     add_inner_in_expr(outer_in_name, tap_offset, storage_size_name)
 
                 output_taps = inner_in_names_to_output_taps.get(
                     outer_in_name, [tap_storage_size]
                 )
                 for out_tap in output_taps:
                     inner_out_to_outer_in_stmts.append(
-                        idx_to_str(storage_name, out_tap, size=storage_size_name)
+                        idx_to_str(
+                            storage_name,
+                            out_tap,
+                            size=storage_size_name,
+                            allow_scalar=True,
+                        )
                     )
 
                 add_output_storage_post_proc_stmt(
                     storage_name, output_taps, storage_size_name
                 )
 
             else:
@@ -265,15 +279,15 @@
             # This is a special case in which there are no outer-inputs used
             # for outer-output storage, so we need to create our own storage
             # from scratch.
             storage_name = outer_in_to_storage_name[outer_in_name]
             storage_size_name = f"{outer_in_name}_len"
 
             inner_out_to_outer_in_stmts.append(
-                idx_to_str(storage_name, 0, size=storage_size_name)
+                idx_to_str(storage_name, 0, size=storage_size_name, allow_scalar=True)
             )
             add_output_storage_post_proc_stmt(storage_name, (0,), storage_size_name)
 
             # In case of nit-sots we are provided the length of the array in
             # the iteration dimension instead of actual arrays, hence we
             # allocate space for the results accordingly.
             curr_nit_sot_position = outer_in_nit_sot_names.index(outer_in_name)
@@ -333,16 +347,16 @@
 
     scan_op_src = f"""
 def scan({", ".join(outer_in_names)}):
 
 {indent(input_storage_block, " " * 4)}
 
     i = 0
-    cond = False
-    while i < n_steps and not cond:
+    cond = np.array(False)
+    while i < n_steps and not cond.item():
         {inner_outputs} = scan_inner_func({inner_in_args})
 {indent(inner_out_post_processing_block, " " * 8)}
 {indent(inner_out_to_outer_out_stmts, " " * 8)}
         i += 1
 
 {indent(output_storage_post_processing_block, " " * 4)}
```

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/sparse.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/sparse.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/numba/dispatch/tensor_basic.py` & `pytensor-2.9.1/pytensor/link/numba/dispatch/tensor_basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/numba/linker.py` & `pytensor-2.9.1/pytensor/link/numba/linker.py`

 * *Files 15% similar despite different names*

```diff
@@ -23,17 +23,17 @@
 
     def fgraph_convert(self, fgraph, **kwargs):
         from pytensor.link.numba.dispatch import numba_funcify
 
         return numba_funcify(fgraph, **kwargs)
 
     def jit_compile(self, fn):
-        import numba
+        from pytensor.link.numba.dispatch.basic import numba_njit
 
-        jitted_fn = numba.njit(fn)
+        jitted_fn = numba_njit(fn)
         return jitted_fn
 
     def create_thunk_inputs(self, storage_map):
         from numpy.random import RandomState
 
         from pytensor.link.numba.dispatch import numba_typify
```

### Comparing `pytensor-2.8.11/pytensor/link/utils.py` & `pytensor-2.9.1/pytensor/link/utils.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/link/vm.py` & `pytensor-2.9.1/pytensor/link/vm.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/check_blas.py` & `pytensor-2.9.1/pytensor/misc/check_blas.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/check_blas_many.sh` & `pytensor-2.9.1/pytensor/misc/check_blas_many.sh`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/check_duplicate_key.py` & `pytensor-2.9.1/pytensor/misc/check_duplicate_key.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/elemwise_openmp_speedup.py` & `pytensor-2.9.1/pytensor/misc/elemwise_openmp_speedup.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/elemwise_time_test.py` & `pytensor-2.9.1/pytensor/misc/elemwise_time_test.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/frozendict.py` & `pytensor-2.9.1/pytensor/misc/frozendict.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/may_share_memory.py` & `pytensor-2.9.1/pytensor/misc/may_share_memory.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/ordered_set.py` & `pytensor-2.9.1/pytensor/misc/ordered_set.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/misc/pkl_utils.py` & `pytensor-2.9.1/pytensor/misc/pkl_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -43,22 +43,23 @@
 
 class StripPickler(Pickler):
     """Subclass of `Pickler` that strips unnecessary attributes from PyTensor objects.
 
     Example
     -------
 
+    ..code-block:: python
+
         fn_args = dict(inputs=inputs,
                        outputs=outputs,
                        updates=updates)
         dest_pkl = 'my_test.pkl'
         with open(dest_pkl, 'wb') as f:
             strip_pickler = StripPickler(f, protocol=-1)
             strip_pickler.dump(fn_args)
-
     """
 
     def __init__(self, file, protocol=0, extra_tag_to_remove=None):
         # Can't use super as Pickler isn't a new style class
         super().__init__(file, protocol)
         self.tag_to_remove = ["trace", "test_value"]
         if extra_tag_to_remove:
```

### Comparing `pytensor-2.8.11/pytensor/misc/safe_asarray.py` & `pytensor-2.9.1/pytensor/misc/safe_asarray.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/printing.py` & `pytensor-2.9.1/pytensor/printing.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 """Functions for printing PyTensor graphs."""
 
 import hashlib
 import logging
 import os
 import sys
-import warnings
 from abc import ABC, abstractmethod
 from contextlib import contextmanager
 from copy import copy
 from functools import reduce, singledispatch
 from io import StringIO
 from typing import Any, Callable, Dict, List, Optional, Sequence, TextIO, Tuple, Union
 
@@ -116,15 +115,14 @@
     done: Optional[Dict[Union[Literal["output"], Variable, Apply], str]] = None,
     print_storage: bool = False,
     used_ids: Optional[Dict[Union[Literal["output"], Variable, Apply], str]] = None,
     print_op_info: bool = False,
     print_destroy_map: bool = False,
     print_view_map: bool = False,
     print_fgraph_inputs: bool = False,
-    ids: Optional[IDTypesType] = None,
 ) -> Union[str, TextIO]:
     r"""Print a graph as text.
 
     Each line printed represents a `Variable` in a graph.
     The indentation of lines corresponds to its depth in the symbolic graph.
     The first part of the text identifies whether it is an input or the output
     of some `Apply` node.
@@ -189,22 +187,14 @@
     if file == "str":
         _file: Union[TextIO, StringIO] = StringIO()
     elif file is None:
         _file = sys.stdout
     else:
         _file = file
 
-    if ids is not None:
-        warnings.warn(
-            "`ids` is deprecated; use `id_type` instead.",
-            DeprecationWarning,
-            stacklevel=2,
-        )
-        id_type = ids
-
     if done is None:
         done = dict()
 
     if used_ids is None:
         used_ids = dict()
 
     inputs_to_print = []
```

### Comparing `pytensor-2.8.11/pytensor/raise_op.py` & `pytensor-2.9.1/pytensor/raise_op.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sandbox/linalg/ops.py` & `pytensor-2.9.1/pytensor/sandbox/linalg/ops.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sandbox/minimal.py` & `pytensor-2.9.1/pytensor/sandbox/minimal.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sandbox/rng_mrg.py` & `pytensor-2.9.1/pytensor/scan/basic.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,1372 +1,1234 @@
-"""
-Implementation of MRG31k3p random number generator for PyTensor.
-
-Generator code in SSJ package (L'Ecuyer & Simard).
-http://www.iro.umontreal.ca/~simardr/ssj/indexe.html
-
-The MRG31k3p algorithm was published in:
-
-P. L'Ecuyer and R. Touzin, Fast Combined Multiple Recursive Generators with Multipliers of the form a = +/- 2^d +/- 2^e, Proceedings of the 2000 Winter Simulation Conference, Dec. 2000, 683-689.
-
-The conception of the multi-stream from MRG31k3p was published in:
-
-P. L'Ecuyer and R. Simard and E. Jack Chen and W. David Kelton, An Object-Oriented Random-Number Package with Many Long Streams and Substreams, Operations Research, volume 50, number 6, 2002, 1073-1075.
-"""
-
 import warnings
 
 import numpy as np
 
-from pytensor import function, gradient
-from pytensor import scalar as aes
-from pytensor import shared
-from pytensor import tensor as at
-from pytensor.compile import optdb
+import pytensor.tensor as at
+from pytensor.compile.function.pfunc import construct_pfunc_ins_and_outs
+from pytensor.compile.sharedvalue import SharedVariable, collect_new_shareds
 from pytensor.configdefaults import config
-from pytensor.gradient import undefined_grad
-from pytensor.graph.basic import Apply, Constant, Variable
-from pytensor.graph.rewriting.basic import in2out, node_rewriter
-from pytensor.link.c.op import COp, Op
-from pytensor.link.c.params_type import ParamsType
-from pytensor.sandbox import multinomial
-from pytensor.scalar import bool as bool_t
-from pytensor.scalar import int32 as int_t
-from pytensor.tensor import as_tensor_variable, cast, get_vector_length
-from pytensor.tensor.math import cos, log, prod, sin, sqrt
-from pytensor.tensor.shape import reshape
-from pytensor.tensor.type import TensorType, iscalar, ivector, lmatrix
-
-
-warnings.warn(
-    "The module `pytensor.sandbox.rng_mrg` is deprecated. "
-    "Use the module `pytensor.tensor.random` for random variables instead.",
-    DeprecationWarning,
-    stacklevel=2,
-)
-
-
-def matVecModM(A, s, m):
-    # TODO : need description for method, parameter and return
-    assert A.dtype == "int64"
-    return np.int32(np.sum((A * s) % m, 1) % m)
-
-
-def multMatVect(v, A, m1, B, m2):
-    # TODO : need description for parameter and return
-    """
-    Multiply the first half of v by A with a modulo of m1 and the second half
-    by B with a modulo of m2.
-
-    Notes
-    -----
-    The parameters of dot_modulo are passed implicitly because passing them
-    explicitly takes more time than running the function's C-code.
-
-    """
-    if multMatVect.dot_modulo is None:
-        A_sym = lmatrix("A")
-        s_sym = ivector("s")
-        m_sym = iscalar("m")
-        A2_sym = lmatrix("A2")
-        s2_sym = ivector("s2")
-        m2_sym = iscalar("m2")
-        o = DotModulo()(A_sym, s_sym, m_sym, A2_sym, s2_sym, m2_sym)
-        multMatVect.dot_modulo = function(
-            [A_sym, s_sym, m_sym, A2_sym, s2_sym, m2_sym], o, profile=False
-        )
-
-    # This way of calling the PyTensor fct is done to bypass PyTensor overhead.
-    f = multMatVect.dot_modulo
-    f.input_storage[0].storage[0] = A
-    f.input_storage[1].storage[0] = v[:3]
-    f.input_storage[2].storage[0] = m1
-    f.input_storage[3].storage[0] = B
-    f.input_storage[4].storage[0] = v[3:]
-    f.input_storage[5].storage[0] = m2
-    f.vm()
-    r = f.output_storage[0].storage[0]
-
-    return r
-
-
-multMatVect.dot_modulo = None
-
-
-class DotModulo(COp):
-    """
-    Efficient and numerically stable implementation of a dot product followed
-    by a modulo operation. This performs the same function as matVecModM.
-
-    We do this 2 times on 2 triple inputs and concatenating the output.
+from pytensor.graph.basic import Constant, Variable, graph_inputs
+from pytensor.graph.op import get_test_value
+from pytensor.graph.replace import clone_replace
+from pytensor.graph.utils import MissingInputError, TestValueError
+from pytensor.scan.op import Scan, ScanInfo
+from pytensor.scan.utils import expand_empty, safe_new, until
+from pytensor.tensor.basic import get_scalar_constant_value
+from pytensor.tensor.exceptions import NotScalarConstantError
+from pytensor.tensor.math import minimum
+from pytensor.tensor.shape import shape_padleft, unbroadcast
+from pytensor.tensor.type import TensorType, integer_dtypes
+from pytensor.updates import OrderedUpdates
+
+
+def get_updates_and_outputs(ls):
+    """Recognize and order the updates, outputs, and stopping condition for a `Scan`.
+
+    WRITEME: what is the type of ls? how is it formatted?  if it's not in the
+    predefined order already, how does this function know how to put it in that
+    order?
 
     """
 
-    __props__ = ()
-
-    def make_node(self, A, s, m, A2, s2, m2):
-        return Apply(self, [A, s, m, A2, s2, m2], [s.type()])
+    def is_outputs(elem):
+        if isinstance(elem, (list, tuple)) and all(
+            isinstance(x, Variable) for x in elem
+        ):
+            return True
+        if isinstance(elem, Variable):
+            return True
+        return False
+
+    def is_updates(elem):
+        if isinstance(elem, dict):
+            # Make sure the updates will be applied in a deterministic order
+            return True
+        # Dictionaries can be given as lists of tuples
+        if isinstance(elem, (list, tuple)) and all(
+            isinstance(x, (list, tuple)) and len(x) == 2 for x in elem
+        ):
+            return True
+        return False
+
+    def is_condition(elem):
+        return isinstance(elem, until)
+
+    def _list(x):
+        if isinstance(x, (list, tuple)):
+            return list(x)
+        else:
+            return [x]
 
-    def perform(self, node, inputs, outputs):
-        (A, s, m, A2, s2, m2) = inputs
-        (out,) = outputs
-        o1 = matVecModM(A, s, m)
-        o2 = matVecModM(A2, s2, m2)
-        out[0] = np.concatenate((o1, o2))
-
-    def c_code_cache_version(self):
-        return (6,)
-
-    def c_code(self, node, name, inputs, outputs, sub):
-        (_A, _s, _m, _A2, _s2, _m2) = inputs
-        (_z,) = outputs
-        return """
-        int osize = -1;
-        if (PyArray_NDIM(%(_A)s) != 2) {PyErr_SetString(PyExc_NotImplementedError, "rank(A) != 2"); %(fail)s;}
-        if (PyArray_NDIM(%(_s)s) != 1) {PyErr_SetString(PyExc_NotImplementedError, "rank(v) != 1"); %(fail)s;}
-        if (PyArray_NDIM(%(_m)s) != 0) {PyErr_SetString(PyExc_NotImplementedError, "rank(m) != 0"); %(fail)s;}
-        if (PyArray_NDIM(%(_A2)s) != 2) {PyErr_SetString(PyExc_NotImplementedError, "rank(A2) != 2"); %(fail)s;}
-        if (PyArray_NDIM(%(_s2)s) != 1) {PyErr_SetString(PyExc_NotImplementedError, "rank(v2) != 1"); %(fail)s;}
-        if (PyArray_NDIM(%(_m2)s) != 0) {PyErr_SetString(PyExc_NotImplementedError, "rank(m2) != 0"); %(fail)s;}
-
-        if( PyArray_DIMS(%(_A)s)[1] != PyArray_DIMS(%(_s)s)[0])
-        {PyErr_SetString(PyExc_NotImplementedError, "A and s shapes don't agree."); %(fail)s;}
-        if( PyArray_DIMS(%(_A2)s)[1] != PyArray_DIMS(%(_s2)s)[0])
-        {PyErr_SetString(PyExc_NotImplementedError, "A2 and s2 shapes don't agree."); %(fail)s;}
-
-        osize = PyArray_DIMS(%(_A)s)[0] + PyArray_DIMS(%(_A2)s)[0];
-        if (!%(_z)s
-            || (PyArray_DIMS(%(_z)s)[0] != osize))
-        {
-            {Py_XDECREF(%(_z)s);}
-            npy_intp dims[] = {0,};
-            dims[0] = osize;
-            %(_z)s = (PyArrayObject*) PyArray_SimpleNew(1, dims, PyArray_TYPE(%(_s)s));
-        }
-
-        if(!%(_z)s){%(fail)s;}
-
-        {   //makes it compile even though labels jump over variable definitions.
-
-            // A has size MxN, s has N, output M
-            npy_intp M = PyArray_DIMS(%(_A)s)[0];
-            npy_intp N = PyArray_DIMS(%(_A)s)[1];
-
-            const dtype_%(_A)s* __restrict__ DA = (dtype_%(_A)s*)PyArray_DATA(%(_A)s);
-            dtype_%(_s)s* __restrict__ Ds = (dtype_%(_s)s*)PyArray_DATA(%(_s)s);
-            dtype_%(_z)s* __restrict__ Dz = (dtype_%(_z)s*)PyArray_DATA(%(_z)s);
-            const dtype_%(_m)s m = ((dtype_%(_m)s*)PyArray_DATA(%(_m)s))[0];
-
-            npy_intp SA = PyArray_STRIDES(%(_A)s)[1] / PyArray_DESCR(%(_A)s)->elsize;
-            npy_intp Ss = PyArray_STRIDES(%(_s)s)[0] / PyArray_DESCR(%(_s)s)->elsize;
-            npy_intp Sz = PyArray_STRIDES(%(_z)s)[0] / PyArray_DESCR(%(_z)s)->elsize;
-
-            for (npy_int32 i = 0; i < M; ++i)
-            {
-                const dtype_%(_A)s* __restrict__ Ak = (dtype_%(_A)s*)(PyArray_BYTES(%(_A)s) + PyArray_STRIDES(%(_A)s)[0] * i);
-
-                npy_int64 r = 0;
-
-                for (npy_int32 j = 0; j < N; ++j)
-                {
-                    r += (npy_int64)(Ds[j * Ss] * (npy_int64)(Ak[j * SA])) %% m;
-                }
-
-                Dz[i * Sz] = r %% m;
-            }
-        }
-
-        //redo it with the second triple of inputs
-        {
-            // A has size MxN, s has N, output M
-            npy_intp M = PyArray_DIMS(%(_A2)s)[0];
-            npy_intp N = PyArray_DIMS(%(_A2)s)[1];
-
-            const dtype_%(_A2)s* __restrict__ DA = (dtype_%(_A2)s*)PyArray_DATA(%(_A2)s);
-            dtype_%(_s2)s* __restrict__ Ds = (dtype_%(_s2)s*)PyArray_DATA(%(_s2)s);
-            const dtype_%(_m2)s m = ((dtype_%(_m2)s*)PyArray_DATA(%(_m2)s))[0];
-
-            npy_intp SA = PyArray_STRIDES(%(_A2)s)[1] / PyArray_DESCR(%(_A2)s)->elsize;
-            npy_intp Ss = PyArray_STRIDES(%(_s2)s)[0] / PyArray_DESCR(%(_s2)s)->elsize;
-            npy_intp Sz = PyArray_STRIDES(%(_z)s)[0] / PyArray_DESCR(%(_z)s)->elsize;
-
-            dtype_%(_z)s* __restrict__ Dz = (dtype_%(_z)s*)PyArray_DATA(%(_z)s) + PyArray_DIMS(%(_A)s)[0] * Sz;
-
-            for (npy_int32 i = 0; i < M; ++i)
-            {
-                const dtype_%(_A2)s* __restrict__ Ak = (dtype_%(_A2)s*)(PyArray_BYTES(%(_A2)s) + PyArray_STRIDES(%(_A2)s)[0] * i);
-
-                npy_int64 r = 0;
-
-                for (npy_int32 j = 0; j < N; ++j)
-                {
-                    r += (npy_int64)(Ds[j * Ss] * (npy_int64)(Ak[j * SA])) %% m;
-                }
+    def _filter(x):
+        """
+        Ensure `x` is made only of allowed data types.
 
-                Dz[i * Sz] = r %% m;
-            }
+        Return True iff `x` is made only of lists, tuples, dictionaries, PyTensor
+        variables or `pytensor.scan.utils.until` objects.
 
-        }
+        """
+        # Is `x` a container we can iterate on?
+        iter_on = None
+        if isinstance(x, list) or isinstance(x, tuple):
+            iter_on = x
+        elif isinstance(x, dict):
+            iter_on = x.items()
+        if iter_on is not None:
+            return all(_filter(y) for y in iter_on)
+        else:
+            return isinstance(x, Variable) or isinstance(x, until)
 
-        """ % dict(
-            locals(), **sub
+    if not _filter(ls):
+        raise ValueError(
+            "The return value of your scan lambda expression may only be "
+            "made of lists, tuples, or dictionaries containing PyTensor "
+            "variables (or `pytensor.scan.utils.until` objects for "
+            "conditions). In particular if you need to use constant "
+            "values, you can use `tensor.constant` to turn them into "
+            "PyTensor variables."
         )
 
-
-# MRG31k3p
-# generator constants :
-M1 = np.asarray(np.int32(2147483647))  # 2^31 - 1
-M2 = np.asarray(np.int32(2147462579))  # 2^31 - 21069
-MASK12 = np.int32(511)  # 2^9 - 1
-MASK13 = np.int32(16777215)  # 2^24 - 1
-MASK2 = np.int32(65535)  # 2^16 - 1
-MULT2 = np.int32(21069)
-NORM = 4.656612873077392578125e-10  # 1./2^31
-
-# A1p0 = np.asarray([[0, 4194304, 129], [1, 0, 0], [0, 1, 0]],
-#                      dtype='int64')
-# A2p0 = np.asarray([[32768, 0, 32769], [1, 0, 0], [0, 1, 0]],
-#                      dtype='int64')
-
-A1p72 = np.asarray(
-    [
-        [1516919229, 758510237, 499121365],
-        [1884998244, 1516919229, 335398200],
-        [601897748, 1884998244, 358115744],
-    ],
-    dtype="int64",
-)
-A2p72 = np.asarray(
-    [
-        [1228857673, 1496414766, 954677935],
-        [1133297478, 1407477216, 1496414766],
-        [2002613992, 1639496704, 1407477216],
-    ],
-    dtype="int64",
-)
-
-A1p134 = np.asarray(
-    [
-        [1702500920, 1849582496, 1656874625],
-        [828554832, 1702500920, 1512419905],
-        [1143731069, 828554832, 102237247],
-    ],
-    dtype="int64",
-)
-A2p134 = np.asarray(
-    [
-        [796789021, 1464208080, 607337906],
-        [1241679051, 1431130166, 1464208080],
-        [1401213391, 1178684362, 1431130166],
-    ],
-    dtype="int64",
-)
-np_int32_vals = [np.int32(i) for i in (0, 7, 9, 15, 16, 22, 24)]
-
-
-def ff_2p134(rstate):
-    # TODO : need description for method, parameter and return
-    return multMatVect(rstate, A1p134, M1, A2p134, M2)
-
-
-def ff_2p72(rstate):
-    # TODO : need description for method, parameter and return
-    return multMatVect(rstate, A1p72, M1, A2p72, M2)
-
-
-def mrg_next_value(rstate, new_rstate, NORM, mask, offset):
-    # TODO : need description for method, parameter and return
-    x11, x12, x13, x21, x22, x23 = rstate
-    assert isinstance(x11, np.int32)
-
-    i0, i7, i9, i15, i16, i22, i24 = np_int32_vals
-    # first component
-    y1 = ((x12 & MASK12) << i22) + (x12 >> i9) + ((x13 & MASK13) << i7) + (x13 >> i24)
-
-    assert isinstance(y1, np.int32)
-    if y1 < 0 or y1 >= M1:  # must also check overflow
-        y1 -= M1
-    y1 += x13
-    if y1 < 0 or y1 >= M1:
-        y1 -= M1
-
-    x13 = x12
-    x12 = x11
-    x11 = y1
-
-    # second component
-    y1 = ((x21 & MASK2) << i15) + (MULT2 * (x21 >> i16))
-    assert isinstance(y1, np.int32)
-    if y1 < 0 or y1 >= M2:
-        y1 -= M2
-    y2 = ((x23 & MASK2) << i15) + (MULT2 * (x23 >> i16))
-    assert isinstance(y2, np.int32)
-    if y2 < 0 or y2 >= M2:
-        y2 -= M2
-    y2 += x23
-    if y2 < 0 or y2 >= M2:
-        y2 -= M2
-    y2 += y1
-    if y2 < 0 or y2 >= M2:
-        y2 -= M2
-
-    x23 = x22
-    x22 = x21
-    x21 = y2
-
-    # Must never return either 0 or M1+1
-    new_rstate[...] = [x11, x12, x13, x21, x22, x23]
-    assert new_rstate.dtype == np.int32
-    if x11 <= x21:
-        return (((x11 - x21 + M1) & mask) + offset) * NORM
-    else:
-        return (((x11 - x21) & mask) + offset) * NORM
-
-
-class mrg_uniform_base(Op):
-    # TODO : need description for class, parameter
-    __props__ = ("output_type", "inplace")
-    params_type = ParamsType(
-        inplace=bool_t,
-        # following params will come from self.output_type.
-        # NB: As output object may not be allocated in C code,
-        # we can not be sure to get these properties from output.
-        # So, we should better get them as params from self.output_type.
-        ndim=int_t,
-        otypenum=int_t,
-        otype_is_float32=bool_t,
+    if is_outputs(ls):
+        return None, _list(ls), dict()
+    if is_updates(ls):
+        return None, [], dict(ls)
+    error_msg = (
+        f"Scan cannot parse the return value of your lambda expression, which is: {ls}"
     )
-
-    def __init__(self, output_type, inplace=False):
-        Op.__init__(self)
-        self.output_type = output_type
-        self.inplace = inplace
-        if inplace:
-            self.destroy_map = {0: [0]}
-        self.warned_numpy_version = False
-
-    # These attributes (used as params) are created as properties
-    # to make them available even for old pickled objects, e.g.
-    # when testing old interface or when using FAST_COMPILE mode.
-    ndim = property(lambda self: self.output_type.ndim)
-    otypenum = property(lambda self: np.dtype(self.output_type.dtype).num)
-    otype_is_float32 = property(lambda self: self.output_type.dtype == "float32")
-
-    def __str__(self):
-        if self.inplace:
-            s = "inplace"
+    if not isinstance(ls, (list, tuple)):
+        raise ValueError(error_msg)
+    ls = list(ls)
+    deprecation_msg = (
+        "The return value of the lambda function"
+        " has been restricted. you have to always return first the"
+        " outputs (if any), afterwards the updates (if any) and"
+        " at the end the conclusion"
+    )
+    if len(ls) == 2:
+        if is_outputs(ls[0]):
+            if is_updates(ls[1]):
+                return (None, _list(ls[0]), dict(ls[1]))
+            elif is_condition(ls[1]):
+                return (ls[1].condition, _list(ls[0]), dict())
+            else:
+                raise ValueError(error_msg)
+        elif is_updates(ls[0]):
+            if is_outputs(ls[1]):
+                raise ValueError(deprecation_msg)
+            elif is_condition(ls[1]):
+                return (ls[1].condition, [], dict(ls[0]))
+            else:
+                raise ValueError(error_msg)
         else:
-            s = "no_inplace"
-        return self.__class__.__name__ + f"{{{self.output_type},{s}}}"
-
-    def grad(self, inputs, ograd):
-        return [
-            gradient.grad_undefined(
-                self, k, inp, "No gradient defined through random sampling op"
-            )
-            for k, inp in enumerate(inputs)
-        ]
-
-    def R_op(self, inputs, eval_points):
-        return [None for i in eval_points]
-
-
-class mrg_uniform(COp, mrg_uniform_base):
-    # CPU VERSION
-    _f16_ok = True
-
-    def make_node(self, rstate, size):
-        # error checking slightly redundant here, since
-        # this op should not be called directly.
-        #
-        # call through MRG_RandomStream instead.
-        out_shape = ()
-        for i in range(self.output_type.ndim):
-            if at.extract_constant(size[i]) == 1:
-                out_shape += (1,)
+            raise ValueError(error_msg)
+    elif len(ls) == 3:
+        if is_outputs(ls[0]):
+            if is_updates(ls[1]):
+                if is_condition(ls[2]):
+                    return (ls[2].condition, _list(ls[0]), dict(ls[1]))
+                else:
+                    raise ValueError(error_msg)
             else:
-                out_shape += (None,)
-        output_var = self.output_type.clone(shape=out_shape)()
-        rstate = as_tensor_variable(rstate)
-        size = as_tensor_variable(size)
-        return Apply(self, [rstate, size], [rstate.type(), output_var])
-
-    @classmethod
-    def new(cls, rstate, ndim, dtype, size):
-        v_size = as_tensor_variable(size)
-        if ndim is None:
-            ndim = get_vector_length(v_size)
-        op = cls(TensorType(dtype, shape=(None,) * ndim))
-        return op(rstate, v_size)
-
-    def perform(self, node, inp, out, params):
-        rstate, size = inp
-        o_rstate, o_sample = out
-        n_elements = 1
-        for s in size:
-            n_elements *= s
-        if n_elements > M1:
-            # The limit is on the C code. This perform don't
-            # have this limit.  But to have all of them behave the
-            # same (and have DebugMode don't use too much memory for
-            # some rng_mrg tests) I also add this limit here.
-            raise ValueError("rng_mrg does not support more then (2**31 -1) samples")
-
-        rstate = np.asarray(rstate)  # bring state from XXX if necessary
-        if not self.inplace:
-            rstate = rstate.copy()
-
-        n_streams, _ = rstate.shape
-
-        rval = np.zeros(n_elements, dtype=self.output_type.dtype)
-        if rval.dtype == "float16":
-            mask = 0x7FFF
-            offset = 1
-            NORM = np.float16(3.0458e-05)
-        elif rval.dtype == "float32":
-            mask = 0xFFFFFFFF
-            offset = 0
-            NORM = np.float32(4.6566126e-10)
-        elif rval.dtype == "float64":
-            mask = 0xFFFFFFFF
-            offset = 0
-            NORM = 4.656612873077392578125e-10  # 1./2^31
-
-        err_orig = np.seterr(over="ignore")
-        try:
-            for i in range(n_elements):
-                sample = mrg_next_value(
-                    rstate[i % n_streams],
-                    rstate[i % n_streams],
-                    NORM=NORM,
-                    mask=mask,
-                    offset=offset,
-                )
-                rval[i] = sample
-        finally:
-            np.seterr(**err_orig)
-
-        # send to GPU if necessary
-        o_rstate[0] = node.outputs[0].type.filter(rstate)
-        o_sample[0] = node.outputs[1].type.filter(rval.reshape(size))
-
-    def c_support_code(self, **kwargs):
-        return "\n".join(
-            """
-        void cpu_rng_mrg_uniform_%(dtype)s(PyArrayObject* o_sample, PyArrayObject* o_rstate,
-                                           npy_int64 n_elements, int n_streams) {
-            const npy_int32 i0 = 0;
-            const npy_int32 i7 = 7;
-            const npy_int32 i9 = 9;
-            const npy_int32 i15 = 15;
-            const npy_int32 i16 = 16;
-            const npy_int32 i22 = 22;
-            const npy_int32 i24 = 24;
-
-            const npy_int32 M1 = 2147483647;      //2^31 - 1
-            const npy_int32 M2 = 2147462579;      //2^31 - 21069
-            const npy_int32 MASK12 = 511;       //2^9 - 1
-            const npy_int32 MASK13 = 16777215;  //2^24 - 1
-            const npy_int32 MASK2 = 65535;      //2^16 - 1
-            const npy_int32 MULT2 = 21069;
-
-            %(dtype)s* sample_data = (%(dtype)s *) PyArray_DATA(o_sample);
-            npy_int32* state_data = (npy_int32 *) PyArray_DATA(o_rstate);
-            for (int i = 0; i < n_elements; ++i)
-            {
-                npy_int32 * state_data_i = state_data + (i%%n_streams)*6;
-                npy_int32 y1, y2, x11, x12, x13, x21, x22, x23;
-
-                x11 = state_data_i[0];
-                x12 = state_data_i[1];
-                x13 = state_data_i[2];
-                x21 = state_data_i[3];
-                x22 = state_data_i[4];
-                x23 = state_data_i[5];
-
-                y1 = ((x12 & MASK12) << i22) + (x12 >> i9) + ((x13 & MASK13) << i7) + (x13 >> i24);
-                if ((y1 < 0 || y1 >= M1))     //must also check overflow
-                    y1 -= M1;
-                y1 += x13;
-                if ((y1 < 0 or y1 >= M1))
-                    y1 -= M1;
-                x13 = x12;
-                x12 = x11;
-                x11 = y1;
-
-                y1 = ((x21 & MASK2) << i15) + (MULT2 * (x21 >> i16));
-                if (y1 < 0 || y1 >= M2)
-                    y1 -= M2;
-                y2 = ((x23 & MASK2) << i15) + (MULT2 * (x23 >> i16));
-                if (y2 < 0 || y2 >= M2)
-                    y2 -= M2;
-                y2 += x23;
-                if (y2 < 0 || y2 >= M2)
-                    y2 -= M2;
-                y2 += y1;
-                if (y2 < 0 or y2 >= M2)
-                    y2 -= M2;
-
-                x23 = x22;
-                x22 = x21;
-                x21 = y2;
-
-                if (x11 <= x21) {
-                    assert((x11 - x21 + M1) <= M1);
-                    sample_data[i] = (x11 - x21 + M1) * %(NORM)s;
-                }
-                else
-                {
-                    assert(x11 - x21 <= M1);
-                    sample_data[i] = (x11 - x21) * %(NORM)s;
-                }
-
-                state_data_i[0]= x11;
-                state_data_i[1]= x12;
-                state_data_i[2]= x13;
-                state_data_i[3]= x21;
-                state_data_i[4]= x22;
-                state_data_i[5]= x23;
-            }
-        }
-        """
-            % dict(dtype=dtype, NORM=NORM)
-            for dtype, NORM in (
-                ("npy_float32", "4.6566126e-10f"),
-                ("npy_float64", "4.656612873077392578125e-10"),
-            )
-        )
-
-    def c_code(self, node, name, inp, out, sub):
-        # If we try to use the C code here with something else than a
-        # TensorType, something is wrong.
-        assert isinstance(node.inputs[0].type, TensorType)
-        if self.output_type.dtype == "float16":
-            # C code is not tested, fall back to Python
-            raise NotImplementedError()
-        return """
-        //////// <code generated by mrg_uniform>
-        npy_int64 odims_i;
-        npy_int64 n_elements = 1;
-        int n_streams = 0;
-        int must_alloc_sample = ((NULL == %(o_sample)s)
-                                 || (PyArray_NDIM(%(o_sample)s) != %(params)s->ndim)
-                                 || !(PyArray_ISCONTIGUOUS(%(o_sample)s)));
-        int o_rstate_requirement = %(params)s->inplace ?
-                                    (NPY_ARRAY_C_CONTIGUOUS|NPY_ARRAY_ALIGNED) :
-                                    (NPY_ARRAY_ENSURECOPY|NPY_ARRAY_C_CONTIGUOUS|NPY_ARRAY_ALIGNED);
-
-        const npy_int32 i0 = 0;
-        const npy_int32 i7 = 7;
-        const npy_int32 i9 = 9;
-        const npy_int32 i15 = 15;
-        const npy_int32 i16 = 16;
-        const npy_int32 i22 = 22;
-        const npy_int32 i24 = 24;
-
-        const npy_int32 M1 = 2147483647;      //2^31 - 1
-        const npy_int32 M2 = 2147462579;      //2^31 - 21069
-        const npy_int32 MASK12 = 511;       //2^9 - 1
-        const npy_int32 MASK13 = 16777215;  //2^24 - 1
-        const npy_int32 MASK2 = 65535;      //2^16 - 1
-        const npy_int32 MULT2 = 21069;
-
-        // We have to read size[i] as an int64, but odims has to be intp*
-        // for NumPy on 32-bit platforms.
-        npy_intp* odims = (npy_intp*)malloc(%(params)s->ndim * sizeof(npy_intp));
-        if (odims == NULL) {
-            PyErr_NoMemory();
-            %(just_fail)s
-        }
-
-        if (PyArray_NDIM(%(size)s) != 1)
-        {
-            PyErr_SetString(PyExc_ValueError, "size must be vector");
-            %(fail)s
-        }
-        if (PyArray_DIMS(%(size)s)[0] != %(params)s->ndim)
-        {
-            PyErr_Format(PyExc_ValueError, "size must have length %%i (not %%i)",
-                %(params)s->ndim, int(PyArray_DIMS(%(size)s)[0]));
-            %(fail)s
-        }
-
-        for (int i = 0; i < %(params)s->ndim; ++i)
-        {
-            odims_i = *(dtype_%(size)s *)PyArray_GETPTR1(%(size)s, i);
-            odims[i] = odims_i;
-            n_elements *= odims_i;
-            must_alloc_sample = must_alloc_sample || (PyArray_DIMS(%(o_sample)s)[i] != odims[i]);
-            //fprintf(stderr, "size %%i %%i\\n", i, (int)odims[i]);
-            //printf("%%li", n_elements);
-        }
-        //fprintf(stderr, "n_elements %%lld\\n", (long long)n_elements);
-        if (n_elements > M1)
-        {
-            PyErr_SetString(
-                PyExc_ValueError,
-                "rng_mrg cpu-implementation does not support more than (2**31 -1) samples");
-            %(fail)s
-        }
-
-        if (must_alloc_sample)
-        {
-            Py_XDECREF(%(o_sample)s);
-            %(o_sample)s = (PyArrayObject*)PyArray_SimpleNew(%(params)s->ndim, odims, %(params)s->otypenum);
-            if(!%(o_sample)s) {
-                PyErr_SetString(PyExc_MemoryError, "failed to alloc mrg_uniform output");
-                %(fail)s
-            }
-        }
-        Py_XDECREF(%(o_rstate)s);
-        %(o_rstate)s = (PyArrayObject*)PyArray_FromAny(
-            (PyObject*)%(rstate)s,
-            NULL, 0, 0, o_rstate_requirement,NULL);
-
-        if (PyArray_NDIM(%(o_rstate)s) != 2)
-        {
-            PyErr_SetString(PyExc_ValueError, "rstate must be matrix");
-            %(fail)s
-        }
-        if (PyArray_DIMS(%(o_rstate)s)[1] != 6)
-        {
-            PyErr_Format(PyExc_ValueError, "rstate must have 6 columns");
-            %(fail)s
-        }
-        if (PyArray_DESCR(%(o_rstate)s)->type_num != NPY_INT32)
-        {
-            PyErr_SetString(PyExc_ValueError, "rstate must be int32");
-            %(fail)s
-        }
-        n_streams = PyArray_DIMS(%(o_rstate)s)[0];
-
-        if (%(params)s->otype_is_float32) {
-            cpu_rng_mrg_uniform_npy_float32(%(o_sample)s, %(o_rstate)s, n_elements, n_streams);
-        } else {
-            cpu_rng_mrg_uniform_npy_float64(%(o_sample)s, %(o_rstate)s, n_elements, n_streams);
-        }
-
-        free(odims);
-        //////// </ code generated by mrg_uniform>
-        """ % dict(
-            rstate=inp[0],
-            size=inp[1],
-            o_rstate=out[0],
-            o_sample=out[1],
-            params=sub["params"],
-            just_fail=sub["fail"],
-            fail="""
-                   {
-                       free(odims);
-                       %(fail)s
-                   }
-                   """
-            % dict(fail=sub["fail"]),
-        )
-
-    def c_code_cache_version(self):
-        return (10,)
-
-
-def guess_n_streams(size, warn=False):
-    # TODO : need description for parameter 'size'
-    """
-    Return a guess at a good number of streams.
+                raise ValueError(error_msg)
+        else:
+            raise ValueError(error_msg)
+    else:
+        raise ValueError(error_msg)
 
-    Parameters
-    ----------
-    warn : bool, optional
-        If True, warn when a guess cannot be made (in which case we
-        return 60 * 256).
 
-    """
-    # TODO: a smart way of choosing the number of streams, see #612.
-    # Note that this code was moved out of `MRG_RandomStream` so that it can
-    # be easily accessed from tests, where we want to disable the warning.
-    if isinstance(size, (tuple, list)) and all(isinstance(i, int) for i in size):
-        # We can make a guess.
-        r = 1
-        for s in size:
-            r *= s
-        if r > 6:
-            r = r // 6  # chosen as fastest for rbm_benchmark
-
-        # The purpose of sampling from many streams is to be able to use
-        # the GPU to its full capacity. It just wastes RAM and
-        # stream-initialization time to allocate more streams than necessary
-        # for the GPU.
-        # XXX: This number is chosen to be good for 280 and 480 architectures,
-        #      Better would be to use pycuda to query the number of
-        #      processors on the GPU device,
-        #      rather than guessing 60.
-        return min(r, 60 * 256)
+def isNaN_or_Inf_or_None(x):
+    isNone = x is None
+    try:
+        isNaN = np.isnan(x)
+        isInf = np.isinf(x)
+        isStr = isinstance(x, str)
+    except Exception:
+        isNaN = False
+        isInf = False
+        isStr = False
+    if not isNaN and not isInf:
+        try:
+            val = get_scalar_constant_value(x)
+            isInf = np.isinf(val)
+            isNaN = np.isnan(val)
+        except Exception:
+            isNaN = False
+            isInf = False
+    if isinstance(x, Constant) and isinstance(x.data, str):
+        isStr = True
     else:
-        if warn:
-            warnings.warn(
-                (
-                    "MRG_RandomStream can't determine the number ofstreams "
-                    f"from size ({size}), guessing 60*256"
-                ),
-                DeprecationWarning,
-                stacklevel=3,
-            )
-        return 60 * 256
+        isStr = False
+    return isNone or isNaN or isInf or isStr
 
 
-class MRG_RandomStream:
-    """
-    Module component with similar interface to numpy.random
-    (numpy.random.RandomState).
+def scan(
+    fn,
+    sequences=None,
+    outputs_info=None,
+    non_sequences=None,
+    n_steps=None,
+    truncate_gradient=-1,
+    go_backwards=False,
+    mode=None,
+    name=None,
+    profile=False,
+    allow_gc=None,
+    strict=False,
+    return_list=False,
+):
+    r"""This function constructs and applies a `Scan` `Op` to the provided arguments.
 
     Parameters
     ----------
-    seed : int or list of 6 int
-        A default seed to initialize the random state.
-        If a single int is given, it will be replicated 6 times.
-        The first 3 values of the seed must all be less than M1 = 2147483647,
-        and not all 0; and the last 3 values must all be less than
-        M2 = 2147462579, and not all 0.
+    fn
+        `fn` is a function that describes the operations involved in one
+        step of `scan`. `fn` should construct variables describing the
+        output of one iteration step. It should expect as input
+        `Variable`\s representing all the slices of the input sequences
+        and previous values of the outputs, as well as all other arguments
+        given to scan as `non_sequences`. The order in which scan passes
+        these variables to `fn`  is the following :
+
+        * all time slices of the first sequence
+        * all time slices of the second sequence
+        * ...
+        * all time slices of the last sequence
+        * all past slices of the first output
+        * all past slices of the second output
+        * ...
+        * all past slices of the last output
+        * all other arguments (the list given as `non_sequences` to
+            `scan`)
+
+        The order of the sequences is the same as the one in the list
+        `sequences` given to `scan`. The order of the outputs is the same
+        as the order of `outputs_info`. For any sequence or output the
+        order of the time slices is the same as the one in which they have
+        been given as taps. For example if one writes the following :
+
+        .. code-block:: python
+
+            scan(fn, sequences = [ dict(input= Sequence1, taps = [-3,2,-1])
+                                 , Sequence2
+                                 , dict(input =  Sequence3, taps = 3) ]
+                   , outputs_info = [ dict(initial =  Output1, taps = [-3,-5])
+                                    , dict(initial = Output2, taps = None)
+                                    , Output3 ]
+                   , non_sequences = [ Argument1, Argument2])
+
+        `fn` should expect the following arguments in this given order:
+
+        #. ``sequence1[t-3]``
+        #. ``sequence1[t+2]``
+        #. ``sequence1[t-1]``
+        #. ``sequence2[t]``
+        #. ``sequence3[t+3]``
+        #. ``output1[t-3]``
+        #. ``output1[t-5]``
+        #. ``output3[t-1]``
+        #. ``argument1``
+        #. ``argument2``
+
+        The list of `non_sequences` can also contain shared variables
+        used in the function, though `scan` is able to figure those
+        out on its own so they can be skipped. For the clarity of the
+        code we recommend though to provide them to `scan`. To some extend
+        `scan` can also figure out other `non sequences` (not shared)
+        even if not passed to `scan` (but used by `fn`). A simple example of
+        this would be :
+
+        .. code-block:: python
+
+            import pytensor.tensor as at
+
+            W   = at.matrix()
+            W_2 = W**2
+
+            def f(x):
+                return at.dot(x,W_2)
+
+        The function `fn` is expected to return two things. One is a list of
+        outputs ordered in the same order as `outputs_info`, with the
+        difference that there should be only one output variable per
+        output initial state (even if no tap value is used). Secondly
+        `fn` should return an update dictionary (that tells how to
+        update any shared variable after each iteration step). The
+        dictionary can optionally be given as a list of tuples. There is
+        no constraint on the order of these two list, `fn` can return
+        either ``(outputs_list, update_dictionary)`` or
+        ``(update_dictionary, outputs_list)`` or just one of the two (in
+        case the other is empty).
+
+        To use `scan` as a ``while`` loop, the user needs to change the
+        function `fn` such that also a stopping condition is returned.
+        To do so, one needs to wrap the condition in an `until` class.
+        The condition should be returned as a third element, for example:
+
+        .. code-block:: python
+
+            ...
+            return [y1_t, y2_t], {x:x+1}, until(x < 50)
+
+        Note that a number of steps--considered in here as the maximum
+        number of steps--is still required even though a condition is
+        passed.  It is used to allocate memory if needed.
+
+    sequences
+        `sequences` is the list of `Variable`\s or ``dict``\s
+        describing the sequences `scan` has to iterate over. If a
+        sequence is given as wrapped in a ``dict``, then a set of optional
+        information can be provided about the sequence. The ``dict``
+        should have the following keys:
+
+        * ``input`` (*mandatory*) -- `Variable` representing the
+          sequence.
+
+        * ``taps`` -- Temporal taps of the sequence required by `fn`.
+          They are provided as a list of integers, where a value ``k``
+          impiles that at iteration step ``t`` scan will pass to `fn`
+          the slice ``t+k``. Default value is ``[0]``
+
+        All `Variable`\s in the list `sequences` are automatically
+        wrapped into a ``dict`` where ``taps`` is set to ``[0]``
+
+    outputs_info
+        `outputs_info` is the list of `Variable`\s or ``dict``\s
+        describing the initial state of the outputs computed
+        recurrently. When the initial states are given as ``dict``\s,
+        optional information can be provided about the output corresponding
+        to those initial states. The ``dict`` should have the following
+        keys:
+
+        * ``initial`` -- A `Variable` that represents the initial
+          state of a given output. In case the output is not computed
+          recursively (e.g. a ``map``-like function) and does not require an initial
+          state, this field can be skipped. Given that only the previous
+          time step of the output is used by `fn`, the initial state
+          **should have the same shape** as the output and **should not
+          involve a downcast** of the data type of the output. If multiple
+          time taps are used, the initial state should have one extra
+          dimension that covers all the possible taps. For example
+          if we use ``-5``, ``-2`` and ``-1`` as past taps, at step ``0``,
+          `fn` will require (by an abuse of notation) ``output[-5]``,
+          ``output[-2]`` and ``output[-1]``. This will be given by
+          the initial state, which in this case should have the shape
+          ``(5,) + output.shape``. If this `Variable` containing the initial
+          state is called ``init_y`` then ``init_y[0]`` corresponds to
+          ``output[-5]``. ``init_y[1]`` corresponds to ``output[-4]``,
+          ``init_y[2]`` corresponds to ``output[-3]``, ``init_y[3]``
+          corresponds to ``output[-2]``, ``init_y[4]`` corresponds to
+          ``output[-1]``.
+          While this order might seem strange, it comes natural from splitting
+          an array at a given point. assume that we have a array ``x``, and we
+          choose ``k`` to be time step ``0``. Then our initial state would be
+          ``x[:k]``, while the output will be ``x[k:]``. Looking at this split,
+          elements in ``x[:k]`` are ordered exactly like those in ``init_y``.
+        * ``taps`` -- Temporal taps of the output that will be passed to
+          `fn`. They are provided as a list of *negative* integers,
+          where a value ``k`` implies that at iteration step ``t`` scan
+          will pass to `fn` the slice ``t+k``.
+
+        `scan` will follow this logic if partial information is given:
+
+        * If an output is not wrapped in a ``dict``, `scan` will wrap
+          it in one assuming that you use only the last step of the output
+          (i.e. it makes your tap value list equal to ``[-1]``).
+        * If you wrap an output in a ``dict`` and you do not provide any
+          taps but you provide an initial state it will assume that you are
+          using only a tap value of ``-1``.
+        * If you wrap an output in a ``dict`` but you do not provide any
+          initial state, it assumes that you are not using any form of
+          taps.
+        * If you provide a ``None`` instead of a `Variable` or a empty
+          ``dict`` `scan` assumes that you will not use any taps for
+          this output (like for example in case of a ``map``)
+
+        If `outputs_info` is an empty ``list`` or ``None``, `scan` assumes
+        that no tap is used for any of the outputs. If information is
+        provided just for a subset of the outputs, an exception is
+        raised, because there is no convention on how scan should map
+        the provided information to the outputs of `fn`.
+
+    non_sequences
+        `non_sequences` is the list of arguments that are passed to
+        `fn` at each steps. One can choose to exclude variables
+        used in `fn` from this list, as long as they are part of the
+        computational graph, although--for clarity--this is *not* encouraged.
+
+    n_steps
+        `n_steps` is the number of steps to iterate given as an ``int``
+        or a scalar `Variable`. If any of the input sequences do not have
+        enough elements, `scan` will raise an error. If the value is ``0``, the
+        outputs will have ``0`` rows. If `n_steps` is not provided, `scan` will
+        figure out the amount of steps it should run given its input
+        sequences. ``n_steps < 0`` is not supported anymore.
+
+    truncate_gradient
+        `truncate_gradient` is the number of steps to use in truncated
+        back-propagation through time (BPTT).  If you compute gradients through
+        a `Scan` `Op`, they are computed using BPTT. By providing a different
+        value then ``-1``, you choose to use truncated BPTT instead of classical
+        BPTT, where you go for only `truncate_gradient` number of steps back in
+        time.
+
+    go_backwards
+        `go_backwards` is a flag indicating if `scan` should go
+        backwards through the sequences. If you think of each sequence
+        as indexed by time, making this flag ``True`` would mean that
+        `scan` goes back in time, namely that for any sequence it
+        starts from the end and goes towards ``0``.
+
+    name
+        When profiling `scan`, it is helpful to provide a name for any
+        instance of `scan`.
+        For example, the profiler will produce an overall profile of your code
+        as well as profiles for the computation of one step of each instance of
+        `Scan`. The `name` of the instance appears in those profiles and can
+        greatly help to disambiguate information.
+
+    mode
+        The mode used to compile the inner-graph.
+        If you prefer the computations of one step of `scan` to be done
+        differently then the entire function, you can use this parameter to
+        describe how the computations in this loop are done (see
+        `pytensor.function` for details about possible values and their meaning).
+
+    profile
+        If ``True`` or a non-empty string, a profile object will be created and
+        attached to the inner graph of `Scan`. When `profile` is ``True``, the
+        profiler results will use the name of the `Scan` instance, otherwise it
+        will use the passed string.  The profiler only collects and prints
+        information when running the inner graph with the `CVM` `Linker`.
+
+    allow_gc
+        Set the value of `allow_gc` for the internal graph of the `Scan`.  If
+        set to ``None``, this will use the value of
+        `pytensor.config.scan__allow_gc`.
+
+        The full `Scan` behavior related to allocation is determined by this
+        value and the flag `pytensor.config.allow_gc`. If the flag
+        `allow_gc` is ``True`` (default) and this `allow_gc` is ``False``
+        (default), then we let `Scan` allocate all intermediate memory
+        on the first iteration, and they are not garbage collected
+        after that first iteration; this is determined by `allow_gc`. This can
+        speed up allocation of the subsequent iterations. All those temporary
+        allocations are freed at the end of all iterations; this is what the
+        flag `pytensor.config.allow_gc` means.
+
+    strict
+        If ``True``, all the shared variables used in `fn` must be provided as a
+        part of `non_sequences` or `sequences`.
 
-    """
-
-    def updates(self):
-        # TODO : need description for method and return
-        return list(self.state_updates)
-
-    def __init__(self, seed=12345):
-        # A list of pairs of the form (input_r, output_r), representing the
-        # update rules of all the random states generated
-        # by this RandomStream.
-        self.state_updates = []
-
-        super().__init__()
-
-        # Needed to reset the streams.
-        self.default_instance_seed = seed
-
-        self.set_rstate(seed)
-
-    def set_rstate(self, seed):
-        # TODO : need description for method, parameter
-        if isinstance(seed, (int, np.int32, np.int64)):
-            if seed == 0:
-                raise ValueError("seed should not be 0", seed)
-            elif seed >= M2:
-                raise ValueError(f"seed should be less than {int(M2)}", seed)
-            self.rstate = np.asarray([seed] * 6, dtype="int32")
-        elif len(seed) == 6:
-            if seed[0] == 0 and seed[1] == 0 and seed[2] == 0:
-                raise ValueError("The first 3 values of seed should not be all 0", seed)
-            if seed[3] == 0 and seed[4] == 0 and seed[5] == 0:
-                raise ValueError("The last 3 values of seed should not be all 0", seed)
-            if seed[0] >= M1 or seed[1] >= M1 or seed[2] >= M1:
-                raise ValueError(
-                    f"The first 3 values of seed should be less than {int(M1)}", seed
-                )
-            if seed[3] >= M2 or seed[4] >= M2 or seed[5] >= M2:
-                raise ValueError(
-                    f"The last 3 values of seed should be less than {M2}", seed
-                )
-            self.rstate = np.asarray(seed, dtype="int32")
-        else:
-            raise TypeError("seed should be 1 integer or 6 integers")
-
-    def seed(self, seed=None):
-        """
-        Re-initialize each random stream.
-
-        Parameters
-        ----------
-        seed : None or integer in range 0 to 2**30
-            Each random stream will be assigned a unique state that depends
-            deterministically on this value.
-
-        Returns
-        -------
-        None
+    return_list
+        If ``True``, will always return a ``list``, even if there is only one output.
 
-        """
-        if seed is None:
-            seed = self.default_instance_seed
-        self.set_rstate(seed)
-
-        for old_r, new_r, size, nstreams in self.state_updates:
-            if nstreams is None:
-                nstreams = self.n_streams(size)
-            rstates = self.get_substream_rstates(nstreams, new_r.owner.outputs[1].dtype)
-            assert (
-                old_r.get_value(borrow=True, return_internal_type=True).shape
-                == rstates.shape
-            )
-            assert rstates.dtype == old_r.dtype
-            old_r.set_value(rstates, borrow=True)
+    Returns
+    -------
+    tuple
+        ``tuple`` of the form ``(outputs, updates)``.
+        ``outputs`` is either a `Variable` or a ``list`` of `Variable`\s
+        representing the outputs in the same order as in `outputs_info`.
+        ``updates`` is a subclass of ``dict`` specifying the update rules for
+        all shared variables used in `Scan`.
+        This ``dict`` should be passed to `pytensor.function` when you compile
+        your function.
 
-    def inc_rstate(self):
-        """
-        Update self.rstate to be skipped 2^134 steps forward to the next stream
-        start.
+    """
+    # General observation : this code is executed only once, at creation
+    # of the computational graph, so we don't yet need to be smart about
+    # anything (to speed things up)
+
+    ##
+    # Step 1. Wrap all inputs in dictionaries and add default values
+    ##
 
+    # check if inputs are just single variables instead of lists
+    def wrap_into_list(x):
         """
-        # self.rstate = ff_2p134(self.rstate)
-        self.rstate = multMatVect(self.rstate, A1p134, M1, A2p134, M2)
-        assert self.rstate.dtype == np.int32
-
-    @config.change_flags(compute_test_value="off")
-    def get_substream_rstates(self, n_streams, dtype, inc_rstate=True):
-        # TODO : need description for parameter and return
-        """
-        Initialize a matrix in which each row is a MRG stream state,
-        and they are spaced by 2**72 samples.
+        Wrap the input into a list if it is not already a list.
 
         """
-        assert isinstance(dtype, str)
-        assert n_streams < 2**72
-        assert n_streams > 0
-        rval = np.zeros((n_streams, 6), dtype="int32")
-        rval[0] = self.rstate
-
-        # If multMatVect.dot_modulo isn't compiled, compile it.
-        if multMatVect.dot_modulo is None:
-            multMatVect(rval[0], A1p72, M1, A2p72, M2)
-
-        # This way of calling the PyTensor fct is done to bypass PyTensor overhead.
-        f = multMatVect.dot_modulo
-        f.input_storage[0].storage[0] = A1p72
-        f.input_storage[2].storage[0] = M1
-        f.input_storage[3].storage[0] = A2p72
-        f.input_storage[5].storage[0] = M2
-        for i in range(1, n_streams):
-            # Inline the following call to bypass Python overhead
-            # rval[i] = ff_2p72(rval[i - 1])
-            v = rval[i - 1]
-            f.input_storage[1].storage[0] = v[:3]
-            f.input_storage[4].storage[0] = v[3:]
-            f.vm()
-            rval[i] = f.output_storage[0].storage[0]
-
-        if inc_rstate:
-            self.inc_rstate()
-
-        return rval
-
-    def n_streams(self, size):
-        # TODO : need description for method, parameter and return
-        return guess_n_streams(size)
-
-    def pretty_return(self, node_rstate, new_rstate, sample, size, nstreams):
-        # TODO : need description for method, parameter and return
-        sample.rstate = node_rstate
-        sample.update = (node_rstate, new_rstate)
-        self.state_updates.append((node_rstate, new_rstate, size, nstreams))
-        node_rstate.default_update = new_rstate
-        return sample
-
-    def uniform(
-        self, size, low=0.0, high=1.0, ndim=None, dtype=None, nstreams=None, **kwargs
-    ):
-        # TODO : need description for parameter 'size', 'ndim', 'nstreams'
-        """
-        Sample a tensor of given size whose element from a uniform
-        distribution between low and high.
-
-        If the size argument is ambiguous on the number of dimensions,
-        ndim may be a plain integer to supplement the missing information.
-
-        Parameters
-        ----------
-        low
-            Lower bound of the interval on which values are sampled.
-            If the ``dtype`` arg is provided, ``low`` will be cast into
-            dtype. This bound is excluded.
-        high
-            Higher bound of the interval on which values are sampled.
-            If the ``dtype`` arg is provided, ``high`` will be cast into
-            dtype. This bound is excluded.
-        size
-          Can be a list of integer or PyTensor variable (ex: the shape
-          of other PyTensor Variable).
-        dtype
-            The output data type. If dtype is not specified, it will be
-            inferred from the dtype of low and high, but will be at
-            least as precise as floatX.
-
-        """
-        low = as_tensor_variable(low)
-        high = as_tensor_variable(high)
-
-        if dtype is None:
-            dtype = aes.upcast(config.floatX, low.dtype, high.dtype)
-
-        low = cast(low, dtype=dtype)
-        high = cast(high, dtype=dtype)
-
-        low = undefined_grad(low)
-        high = undefined_grad(high)
-
-        if isinstance(size, tuple):
-            msg = "size must be a tuple of int or an PyTensor variable"
-            assert all(isinstance(i, (np.integer, int, Variable)) for i in size), msg
-            if any(isinstance(i, (np.integer, int)) and i <= 0 for i in size):
-                raise ValueError(
-                    "The specified size contains a dimension with value <= 0", size
-                )
-
+        if x is None:
+            return []
+        elif not isinstance(x, (list, tuple)):
+            return [x]
         else:
-            if not (isinstance(size, Variable) and size.ndim == 1):
-                raise TypeError(
-                    "size must be a tuple of int or an PyTensor "
-                    "Variable with 1 dimension, got "
-                    + str(size)
-                    + " of type "
-                    + str(type(size))
-                )
-        orig_nstreams = nstreams
-        if nstreams is None:
-            nstreams = self.n_streams(size)
-        rstates = self.get_substream_rstates(nstreams, dtype)
-
-        d = {}
-        if "target" in kwargs:
-            d = dict(target=kwargs.pop("target"))
-        if len(kwargs) > 0:
-            raise TypeError(
-                f"uniform() got unexpected keyword arguments {kwargs.keys()}"
-            )
-        node_rstate = shared(rstates, **d)
-        u = self.pretty_return(
-            node_rstate,
-            *mrg_uniform.new(node_rstate, ndim, dtype, size),
-            size=size,
-            nstreams=orig_nstreams,
-        )
-        r = u * (high - low) + low
-
-        if u.type.broadcastable != r.type.broadcastable:
-            raise NotImplementedError(
-                "Increase the size to match the broadcasting pattern of "
-                "`low` and `high` arguments"
-            )
+            return list(x)
 
-        assert r.dtype == dtype
-        return r
+    seqs = wrap_into_list(sequences)
+    outs_info = wrap_into_list(outputs_info)
 
-    def binomial(
-        self, size=None, n=1, p=0.5, ndim=None, dtype="int64", nstreams=None, **kwargs
-    ):
-        # TODO : need description for method, parameter and return
-        if n == 1:
-            p = undefined_grad(as_tensor_variable(p))
-            x = self.uniform(size=size, nstreams=nstreams, **kwargs)
-            return cast(x < p, dtype)
+    # Make sure we get rid of numpy arrays or ints or anything like that
+    # passed as inputs to scan
+    non_seqs = []
+    for elem in wrap_into_list(non_sequences):
+        if not isinstance(elem, Variable):
+            non_seqs.append(at.as_tensor_variable(elem))
         else:
-            raise NotImplementedError("MRG_RandomStream.binomial with n > 1")
-
-    def multinomial(
-        self,
-        size=None,
-        n=1,
-        pvals=None,
-        ndim=None,
-        dtype="int64",
-        nstreams=None,
-        **kwargs,
-    ):
-        # TODO : need description for parameter and return
-        """
-        Sample `n` (`n` needs to be >= 1, default 1) times from a multinomial
-        distribution defined by probabilities pvals.
+            non_seqs.append(elem)
 
-        Example : pvals = [[.98, .01, .01], [.01, .49, .50]] and n=1 will
-        probably result in [[1,0,0],[0,0,1]]. When setting n=2, this
-        will probably result in [[2,0,0],[0,1,1]].
-
-        Notes
-        -----
-        -`size` and `ndim` are only there keep the same signature as other
-        uniform, binomial, normal, etc.
-        TODO : adapt multinomial to take that into account
-
-        -Does not do any value checking on pvals, i.e. there is no
-        check that the elements are non-negative, less than 1, or
-        sum to 1. passing pvals = [[-2., 2.]] will result in
-        sampling [[0, 0]]
+    # If we provided a known number of steps ( before compilation)
+    # and if that number is 1 or -1, then we can skip the Scan Op,
+    # and just apply the inner function once
+    # To do that we check here to see the nature of n_steps
+    n_fixed_steps = None
 
-        """
-        if pvals is None:
-            raise TypeError("You have to specify pvals")
-        pvals = as_tensor_variable(pvals)
-        pvals = undefined_grad(pvals)
-        if size is not None:
-            if any(isinstance(i, int) and i <= 0 for i in size):
+    if isinstance(n_steps, (float, int)):
+        n_fixed_steps = int(n_steps)
+    else:
+        try:
+            n_fixed_steps = at.get_scalar_constant_value(n_steps)
+        except NotScalarConstantError:
+            n_fixed_steps = None
+
+    # Check n_steps is an int
+    if hasattr(n_steps, "dtype") and str(n_steps.dtype) not in integer_dtypes:
+        raise ValueError(f" n_steps must be an int. dtype provided is {n_steps.dtype}")
+
+    # compute number of sequences and number of outputs
+    n_seqs = len(seqs)
+    n_outs = len(outs_info)
+
+    return_steps = {}
+    # wrap sequences in a dictionary if they are not already dictionaries
+    for i in range(n_seqs):
+        if not isinstance(seqs[i], dict):
+            seqs[i] = dict([("input", seqs[i]), ("taps", [0])])
+        elif seqs[i].get("taps", None) is not None:
+            seqs[i]["taps"] = wrap_into_list(seqs[i]["taps"])
+        elif seqs[i].get("taps", None) is None:
+            # seqs dictionary does not have the ``taps`` key
+            seqs[i]["taps"] = [0]
+
+    # wrap outputs info in a dictionary if they are not already in one
+    for i in range(n_outs):
+        if outs_info[i] is not None:
+            if not isinstance(outs_info[i], dict):
+                # by default any output has a tap value of -1
+                outs_info[i] = dict([("initial", outs_info[i]), ("taps", [-1])])
+            elif (
+                outs_info[i].get("initial", None) is None
+                and outs_info[i].get("taps", None) is not None
+            ):
+                # ^ no initial state but taps provided
                 raise ValueError(
-                    "The specified size contains a dimension with value <= 0", size
+                    "If you are using slices of an output "
+                    "you need to provide a initial state "
+                    f"for it: {outs_info[i]}"
+                )
+            elif (
+                outs_info[i].get("initial", None) is not None
+                and outs_info[i].get("taps", None) is None
+            ):
+                # ^ initial state but taps not provided
+                if "taps" in outs_info[i]:
+                    # ^ explicitly provided a None for taps
+                    warnings.warn(
+                        f"Output {getattr(outs_info[i]['initial'], 'name', 'None')} (index {i}) has a initial "
+                        "state but taps is explicitly set to None ",
+                    )
+                outs_info[i]["taps"] = [-1]
+            elif outs_info[i].get("taps", None) is not None:
+                # Check that taps are valid (< 0 and all dfferent)
+                taps = outs_info[i]["taps"]
+                if len(taps) > len(set(taps)):
+                    raise ValueError(
+                        ("All the taps must be different in `outputs_info`"),
+                        outs_info[i],
+                    )
+                for t in taps:
+                    if t >= 0:
+                        raise ValueError(
+                            ("All the tap values must be smaller than 0."),
+                            outs_info[i],
+                        )
+            _unexpected_keys = set(outs_info[i]) - {"initial", "taps", "inplace"}
+            if _unexpected_keys:
+                raise ValueError(
+                    f"These keys were unexpected in Scan outputs_info[{i}]: {_unexpected_keys}"
                 )
-
-        if size is not None:
-            raise ValueError(
-                "Provided a size argument to MRG_RandomStream.multinomial, "
-                "which does not use the size argument."
-            )
-        if ndim is not None:
-            raise ValueError(
-                "Provided an ndim argument to MRG_RandomStream.multinomial, "
-                "which does not use the ndim argument."
-            )
-        if pvals.ndim == 2:
-            size = pvals[:, 0].shape * n
-            unis = self.uniform(size=size, ndim=1, nstreams=nstreams, **kwargs)
-            op = multinomial.MultinomialFromUniform(dtype)
-            n_samples = as_tensor_variable(n)
-            return op(pvals, unis, n_samples)
         else:
-            raise NotImplementedError(
-                "MRG_RandomStream.multinomial only implemented for pvals.ndim = 2"
-            )
-
-    def choice(
-        self,
-        size=1,
-        a=None,
-        replace=True,
-        p=None,
-        ndim=None,
-        dtype="int64",
-        nstreams=None,
-        **kwargs,
-    ):
-        """
-        Sample `size` times from a multinomial distribution defined by
-        probabilities `p`, and returns the indices of the sampled elements.
-        Sampled values are between 0 and `p.shape[1]-1`.
-        Only sampling without replacement is implemented for now.
-
-        Parameters
-        ----------
-        size: integer or integer tensor (default 1)
-            The number of samples. It should be between 1 and `p.shape[1]-1`.
-        a: int or None (default None)
-            For now, a should be None. This function will sample
-            values between 0 and `p.shape[1]-1`. When a != None will be
-            implemented, if `a` is a scalar, the samples are drawn from the
-            range 0,...,a-1. We default to 2 as to have the same interface as
-            RandomStream.
-        replace: bool (default True)
-            Whether the sample is with or without replacement.
-            Only replace=False is implemented for now.
-        p: 2d numpy array or pytensor tensor
-            the probabilities of the distribution, corresponding to values
-            0 to `p.shape[1]-1`.
-
-        Example : p = [[.98, .01, .01], [.01, .49, .50]] and size=1 will
-        probably result in [[0],[2]]. When setting size=2, this
-        will probably result in [[0,1],[2,1]].
-
-        Notes
-        -----
-        -`ndim` is only there keep the same signature as other
-        uniform, binomial, normal, etc.
-
-        -Does not do any value checking on pvals, i.e. there is no
-        check that the elements are non-negative, less than 1, or
-        sum to 1. passing pvals = [[-2., 2.]] will result in
-        sampling [[0, 0]]
+            # if a None is provided as the output info we replace it
+            # with an empty OrdereDict() to simplify handling
+            outs_info[i] = {}
+
+    ##
+    # Step 2. Generate inputs and outputs of the inner functions
+    # for compiling a dummy function (Iteration #1)
+    ##
+
+    # create pytensor inputs for the recursive function
+    # note : this is a first batch of possible inputs that will
+    #        be compiled in a dummy function; we used this dummy
+    #        function to detect shared variables and their updates
+    #        and to construct a new and complete list of inputs and
+    #        outputs
+
+    n_seqs = 0
+    scan_seqs = []  # Variables passed as inputs to the scan op
+    inner_seqs = []  # Variables passed as inputs to the inner function
+    inner_slices = []  # Actual slices if scan is removed from the picture
+    # go through sequences picking up time slices as needed
+    for i, seq in enumerate(seqs):
+        # Note that you can have something like no taps for
+        # a sequence, though is highly unlikely in practice
+        if "taps" in seq:
+            # go through the indicated slice
+            mintap = np.min(seq["taps"])
+            maxtap = np.max(seq["taps"])
+            # We cut the sequence such that seq[i] to correspond to
+            # seq[i-k]. For the purposes of cutting the sequences, we
+            # need to pretend tap 0 is used to avoid cutting the sequences
+            # too long if the taps are all lower or all higher than 0.
+            maxtap_proxy = max(maxtap, 0)
+            mintap_proxy = min(mintap, 0)
+            for k in seq["taps"]:
+                # create one slice of the input
+                # Later on, if we decide not to use scan because we are
+                # going for just one step, it makes things easier if we
+                # compute the correct outputs here. This way we can use
+                # the output of the lambda expression directly to replace
+                # the output of scan.
+
+                # If not we need to use copies, that will be replaced at
+                # each frame by the corresponding slice
+                actual_slice = seq["input"][k - mintap_proxy]
+                _seq_val = at.as_tensor_variable(seq["input"])
+                _seq_val_slice = _seq_val[k - mintap_proxy]
+                nw_slice = _seq_val_slice.type()
+
+                # Try to transfer test_value to the new variable
+                if config.compute_test_value != "off":
+                    try:
+                        nw_slice.tag.test_value = get_test_value(_seq_val_slice)
+                    except TestValueError:
+                        if config.compute_test_value != "ignore":
+                            # No need to print a warning or raise an error now,
+                            # it will be done when fn will be called.
+                            warnings.warn(
+                                "Cannot compute test value for "
+                                "the inner function of scan, input value "
+                                f"missing {_seq_val_slice}"
+                            )
+
+                # Add names to slices for debugging and pretty printing ..
+                # that is if the input already has a name
+                if getattr(seq["input"], "name", None) is not None:
+                    if k > 0:
+                        nw_name = seq["input"].name + f"[t+{int(k)}]"
+                    elif k == 0:
+                        nw_name = seq["input"].name + "[t]"
+                    else:
+                        nw_name = seq["input"].name + f"[t{int(k)}]"
+                    nw_slice.name = nw_name
+
+                start = k - mintap_proxy
+                nw_name = None
+                if k == maxtap_proxy:
+                    nw_seq = seq["input"][start:]
+                    if getattr(seq["input"], "name", None) is not None:
+                        nw_name = seq["input"].name + f"[{int(start)}:]"
+                else:
+                    end = -(maxtap_proxy - k)
+                    nw_seq = seq["input"][start:end]
+                    if getattr(seq["input"], "name", None) is not None:
+                        nw_name = seq["input"].name + f"[{int(start)}:{int(end)}]"
+
+                if go_backwards:
+                    nw_seq = nw_seq[::-1]
+
+                scan_seqs.append(nw_seq)
+                inner_seqs.append(nw_slice)
+                inner_slices.append(actual_slice)
+                n_seqs += 1
+                # Add names -- it helps a lot when debugging
+                if nw_name is not None:
+                    nw_seq.name = nw_name
+
+    # Since we've added all sequences now we need to level them up based on
+    # n_steps or their different shapes
+    lengths_vec = []
+    for seq in scan_seqs:
+        lengths_vec.append(seq.shape[0])
+
+    if not isNaN_or_Inf_or_None(n_steps):
+        # ^ N_steps should also be considered
+        lengths_vec.append(at.as_tensor(n_steps))
+
+    if len(lengths_vec) == 0:
+        # ^ No information about the number of steps
+        raise ValueError(
+            "No information about the number of steps "
+            "provided. Either provide a value for "
+            "n_steps argument of scan or provide an input "
+            "sequence"
+        )
 
-        -Only replace=False is implemented for now.
+    # If the user has provided the number of steps, do that regardless ( and
+    # raise an error if the sequences are not long enough )
+    if isNaN_or_Inf_or_None(n_steps):
+        actual_n_steps = lengths_vec[0]
+        for contestant in lengths_vec[1:]:
+            actual_n_steps = minimum(actual_n_steps, contestant)
+    else:
+        actual_n_steps = at.as_tensor(n_steps)
 
-        """
-        if replace:
-            raise NotImplementedError(
-                "MRG_RandomStream.choice only works without replacement for now."
+    scan_seqs = [seq[:actual_n_steps] for seq in scan_seqs]
+    # Conventions :
+    #   mit_mot = multiple input taps, multiple output taps ( only provided
+    #             by the gradient function )
+    #   mit_sot = multiple input taps, single output tap (t + 0)
+    #   sit_sot = single input tap, single output tap (t + 0)
+    #   nit_sot = no input tap, single output tap (t + 0)
+
+    # MIT_MOT -- not provided by the user only by the grad function
+    n_mit_mot = 0
+    mit_mot_scan_inputs = []
+    mit_mot_inner_inputs = []
+    mit_mot_inner_outputs = []
+    mit_mot_out_slices = []
+
+    # SIT_SOT -- provided by the user
+    n_mit_sot = 0
+    mit_sot_scan_inputs = []
+    mit_sot_inner_inputs = []
+    mit_sot_inner_slices = []
+    mit_sot_inner_outputs = []
+    mit_sot_return_steps = {}
+    mit_sot_tap_array = []
+    mit_sot_rightOrder = []
+
+    n_sit_sot = 0
+    sit_sot_scan_inputs = []
+    sit_sot_inner_inputs = []
+    sit_sot_inner_slices = []
+    sit_sot_inner_outputs = []
+    sit_sot_return_steps = {}
+    sit_sot_rightOrder = []
+
+    # go through outputs picking up time slices as needed
+    for i, init_out in enumerate(outs_info):
+        # Note that our convention dictates that if an output uses
+        # just the previous time step, as a initial state we will only
+        # provide a tensor of the same dimension as one time step; This
+        # makes code much cleaner for those who do not use taps. Otherwise
+        # they would always had to shape_padleft the initial state ..
+        # which is ugly
+        if init_out.get("taps", None) == [-1]:
+
+            actual_arg = init_out["initial"]
+            if not isinstance(actual_arg, Variable):
+                actual_arg = at.as_tensor_variable(actual_arg)
+            arg = safe_new(actual_arg)
+            if isinstance(arg, Constant):
+                # safe new returns a clone of the constants, but that is not
+                # what we need for initial states
+                arg = arg.type()
+
+            # Try to transfer test_value to the new variable
+            if config.compute_test_value != "off":
+                try:
+                    arg.tag.test_value = get_test_value(actual_arg)
+                except TestValueError:
+                    if config.compute_test_value != "ignore":
+                        warnings.warn(
+                            "Cannot compute test value for the "
+                            f"inner function of scan, test value missing: {actual_arg}"
+                        )
+
+            if getattr(init_out["initial"], "name", None) is not None:
+                arg.name = init_out["initial"].name + "[t-1]"
+
+            # We need now to allocate space for storing the output and copy
+            # the initial state over. We do this using the expand function
+            # defined in scan utils
+            sit_sot_scan_inputs.append(
+                expand_empty(
+                    unbroadcast(shape_padleft(actual_arg), 0),
+                    actual_n_steps,
+                )
             )
 
-        if a is not None:
-            raise TypeError(
-                "For now, a has to be None in "
-                "MRG_RandomStream.choice. Sampled values are "
-                "between 0 and p.shape[1]-1"
+            sit_sot_inner_slices.append(actual_arg)
+            if i in return_steps:
+                sit_sot_return_steps[n_sit_sot] = return_steps[i]
+            sit_sot_inner_inputs.append(arg)
+            sit_sot_rightOrder.append(i)
+            n_sit_sot += 1
+
+        elif init_out.get("taps", None):
+
+            if np.any(np.array(init_out.get("taps", [])) > 0):
+                # Make sure we do not have requests for future values of a
+                # sequence we can not provide such values
+                raise ValueError("Can not use future taps of outputs", init_out)
+            # go through the taps
+            mintap = abs(np.min(init_out["taps"]))
+            mit_sot_tap_array.append(init_out["taps"])
+            # Sequence
+            mit_sot_scan_inputs.append(
+                expand_empty(init_out["initial"][:mintap], actual_n_steps)
             )
 
-        if p is None:
-            raise TypeError(
-                "For now, p has to be specified in MRG_RandomStream.choice."
-            )
-        p = as_tensor_variable(p)
-        p = undefined_grad(p)
+            if i in return_steps:
+                mit_sot_return_steps[n_mit_sot] = return_steps[i]
+            mit_sot_rightOrder.append(i)
+            n_mit_sot += 1
+            for k in init_out["taps"]:
+                # create a new slice
+                actual_nw_slice = init_out["initial"][k + mintap]
+                _init_out_var = at.as_tensor_variable(init_out["initial"])
+                _init_out_var_slice = _init_out_var[k + mintap]
+                nw_slice = _init_out_var_slice.type()
+
+                # Try to transfer test_value to the new variable
+                if config.compute_test_value != "off":
+                    try:
+                        nw_slice.tag.test_value = get_test_value(_init_out_var_slice)
+                    except TestValueError:
+                        if config.compute_test_value != "ignore":
+                            warnings.warn(
+                                "Cannot compute test value for "
+                                "the inner function of scan, test value "
+                                f"missing: {_init_out_var_slice}"
+                            )
+
+                # give it a name or debugging and pretty printing
+                if getattr(init_out["initial"], "name", None) is not None:
+                    if k > 0:
+                        nw_slice.name = init_out["initial"].name + f"[t+{int(k)}]"
+                    elif k == 0:
+                        nw_slice.name = init_out["initial"].name + "[t]"
+                    else:
+                        nw_slice.name = init_out["initial"].name + f"[t{int(k)}]"
+                mit_sot_inner_inputs.append(nw_slice)
+                mit_sot_inner_slices.append(actual_nw_slice)
+        # NOTE: there is another case, in which we do not want to provide
+        #      any previous value of the output to the inner function (i.e.
+        #      a map); in that case we do not have to do anything ..
+
+    # Re-order args
+    max_mit_sot = np.max([-1] + mit_sot_rightOrder) + 1
+    max_sit_sot = np.max([-1] + sit_sot_rightOrder) + 1
+    n_elems = np.max([max_mit_sot, max_sit_sot])
+    _ordered_args = [[] for x in range(n_elems)]
+    offset = 0
+    for idx in range(n_mit_sot):
+        n_inputs = len(mit_sot_tap_array[idx])
+        if n_fixed_steps in (1, -1):
+            _ordered_args[mit_sot_rightOrder[idx]] = mit_sot_inner_slices[
+                offset : offset + n_inputs
+            ]
+        else:
+            _ordered_args[mit_sot_rightOrder[idx]] = mit_sot_inner_inputs[
+                offset : offset + n_inputs
+            ]
+        offset += n_inputs
+
+    for idx in range(n_sit_sot):
+        if n_fixed_steps in (1, -1):
+            _ordered_args[sit_sot_rightOrder[idx]] = [sit_sot_inner_slices[idx]]
+        else:
+            _ordered_args[sit_sot_rightOrder[idx]] = [sit_sot_inner_inputs[idx]]
 
-        if ndim is not None:
-            raise ValueError("ndim argument to MRG_RandomStream.choice is not used.")
+    ordered_args = []
+    for ls in _ordered_args:
+        ordered_args += ls
+    if n_fixed_steps in (1, -1):
+        args = inner_slices + ordered_args + non_seqs
 
-        if p.ndim != 2:
-            raise NotImplementedError(
-                "MRG_RandomStream.choice is only implemented for p.ndim = 2"
-            )
+    else:
+        args = inner_seqs + ordered_args + non_seqs
 
-        shape = p[:, 0].shape * size
-        unis = self.uniform(size=shape, ndim=1, nstreams=nstreams, **kwargs)
-        op = multinomial.ChoiceFromUniform(odtype=dtype)
-        return op(p, unis, as_tensor_variable(size))
-
-    def multinomial_wo_replacement(
-        self,
-        size=None,
-        n=1,
-        pvals=None,
-        ndim=None,
-        dtype="int64",
-        nstreams=None,
-        **kwargs,
-    ):
-        warnings.warn(
-            "`MRG_RandomStream.multinomial_wo_replacement` is "
-            "deprecated; use `MRG_RandomStream.choice` instead.",
-            DeprecationWarning,
-            stacklevel=2,
+    # add only the non-shared variables and non-constants to the arguments of
+    # the dummy function [ a function should not get shared variables or
+    # constants as input ]
+    dummy_args = [
+        arg
+        for arg in args
+        if (not isinstance(arg, SharedVariable) and not isinstance(arg, Constant))
+    ]
+    # when we apply the lambda expression we get a mixture of update rules
+    # and outputs that needs to be separated
+
+    with collect_new_shareds() as new_shareds:
+        raw_inner_outputs = fn(*args)
+
+    condition, outputs, updates = get_updates_and_outputs(raw_inner_outputs)
+    if condition is not None:
+        as_while = True
+    else:
+        as_while = False
+    ##
+    # Step 3. Check if we actually need scan and remove it if we don't
+    ##
+
+    if n_fixed_steps in (1, -1):
+        for pos, inner_out in enumerate(outputs):
+            # we need to see if we need to pad our sequences with an
+            # unbroadcastable dimension; case example : we return an
+            # output for which we want all intermediate. If n_steps is 1
+            # then, if we return the output as given by the innner function
+            # this will represent only a slice and it will have one
+            # dimension less.
+            if isinstance(inner_out.type, TensorType) and return_steps.get(pos, 0) != 1:
+                outputs[pos] = unbroadcast(shape_padleft(inner_out), 0)
+
+        if not return_list and len(outputs) == 1:
+            outputs = outputs[0]
+
+        return (outputs, updates)
+
+    ##
+    # Step 4. Compile the dummy function
+    ##
+
+    # We can now compile a dummy function just to see what shared variable
+    # we have and what are their update rules (note that the user has
+    # the option not to pass the shared variable to scan, so we need to
+    # pick them manually and add them to scan)
+
+    # extract still missing inputs (there still might be so) and add them
+    # as non sequences at the end of our args
+    if condition is not None:
+        outputs.append(condition)
+    fake_nonseqs = [x.type() for x in non_seqs]
+    fake_outputs = clone_replace(outputs, replace=dict(zip(non_seqs, fake_nonseqs)))
+    all_inputs = filter(
+        lambda x: (
+            isinstance(x, Variable)
+            and not isinstance(x, SharedVariable)
+            and not isinstance(x, Constant)
+        ),
+        graph_inputs(fake_outputs),
+    )
+    extra_inputs = [x for x in all_inputs if x not in args + fake_nonseqs]
+    non_seqs += extra_inputs
+    # Note we do not use all_inputs directly since the order of variables
+    # in args is quite important
+    dummy_args += extra_inputs
+
+    dummy_outs = outputs
+    # Perform a try-except to provide a meaningful error message to the
+    # user if inputs of the inner function are missing.
+    try:
+        dummy_inputs, dummy_outputs = construct_pfunc_ins_and_outs(
+            dummy_args, dummy_outs, updates=updates
+        )
+    except MissingInputError as err:
+        msg = (
+            "\nPlease pass this variable to the scan's inner function. Do "
+            "not forget to also pass it to the `non_sequences` attribute "
+            "of scan."
         )
-        assert size is None
-        return self.choice(
-            size=n,
-            a=None,
-            replace=False,
-            p=pvals,
-            dtype=dtype,
-            nstreams=nstreams,
-            ndim=ndim,
-            **kwargs,
+        raise MissingInputError(err.args[0] + msg)
+    ##
+    # Step 5. Re-arange inputs of scan into a more strict order
+    ##
+
+    # Step 5.0 Check the outputs of the dummy function to see if they
+    # match with user provided data
+
+    # if the number of outputs to the function does not match the number of
+    # assumed outputs until now (provided by the user) there can be
+    # only one explanation: No information is provided for any of the
+    # outputs (i.e. we are dealing with a map)
+    tmp_dummy_f_outs = len(dummy_outputs)
+    if as_while:
+        tmp_dummy_f_outs -= 1
+    if not (tmp_dummy_f_outs == n_outs or outs_info == []):
+        raise ValueError(
+            "Please provide None as outputs_info for "
+            "any output that does not feed back into "
+            "scan (i.e. it behaves like a map) "
         )
 
-    def normal(
-        self,
-        size,
-        avg=0.0,
-        std=1.0,
-        ndim=None,
-        dtype=None,
-        nstreams=None,
-        truncate=False,
-        **kwargs,
-    ):
-        """
-        Sample a tensor of values from a normal distribution.
+    if outs_info == []:
+        n_outs = len(dummy_outputs)
+        if as_while:
+            n_outs = n_outs - 1
+        outs_info = [{} for x in range(n_outs)]
+
+    # Step 5.1 Outputs with taps different then -1
+
+    for i, out in enumerate(outs_info):
+        if "taps" in out and out["taps"] != [-1]:
+            mit_sot_inner_outputs.append(outputs[i])
+
+    # Step 5.2 Outputs with tap equal to -1
+    for i, out in enumerate(outs_info):
+        if "taps" in out and out["taps"] == [-1]:
+            sit_sot_inner_outputs.append(outputs[i])
+
+    # Step 5.3 Outputs that correspond to update rules of shared variables
+    inner_replacements = {}
+    n_shared_outs = 0
+    shared_scan_inputs = []
+    shared_inner_inputs = []
+    shared_inner_outputs = []
+    sit_sot_shared = []
+    no_update_shared_inputs = []
+    for input in dummy_inputs:
+        if not isinstance(input.variable, SharedVariable):
+            continue
+
+        is_local = input.variable in new_shareds
+
+        # We only want to add shared variable updates that were either
+        # user-specified within the inner-function (e.g. by returning an update
+        # `dict`) or the `SharedVariable.default_update`s of a shared variable
+        # created in the inner-function.
+        if input.update and (is_local or input.variable in updates):
+            # We need to remove the `default_update`s on the shared
+            # variables created within the context of the loop function
+            # (e.g. via use of `RandomStream`); otherwise, they'll get
+            # picked up during compilation and produce errors when the
+            # updates include inner-graph variables.
+            # We also don't want to remove a default update that applies to
+            # the scope/context containing this `Scan`, so we only remove
+            # default updates on "local" variables.
+            if is_local and input.variable.default_update is not None:
+                input.variable.default_update = None
+
+            new_var = safe_new(input.variable)
+
+            if getattr(input.variable, "name", None) is not None:
+                new_var.name = input.variable.name + "_copy"
+
+            inner_replacements[input.variable] = new_var
+
+            if isinstance(new_var.type, TensorType):
+                sit_sot_inner_inputs.append(new_var)
+                sit_sot_scan_inputs.append(
+                    expand_empty(
+                        unbroadcast(shape_padleft(input.variable), 0),
+                        actual_n_steps,
+                    )
+                )
 
-        Parameters
-        ----------
-        size : int_vector_like
-            Array dimensions for the output tensor.
-        avg : float_like, optional
-            The mean value for the truncated normal to sample from (defaults to 0.0).
-        std : float_like, optional
-            The standard deviation for the truncated normal to sample from (defaults to 1.0).
-        truncate : bool, optional
-            Truncates the normal distribution at 2 standard deviations if True (defaults to False).
-            When this flag is set, the standard deviation of the result will be less than the one specified.
-        ndim : int, optional
-            The number of dimensions for the output tensor (defaults to None).
-            This argument is necessary if the size argument is ambiguous on the number of dimensions.
-        dtype : str, optional
-            The data-type for the output tensor. If not specified,
-            the dtype is inferred from avg and std, but it is at least as precise as floatX.
-        kwargs
-            Other keyword arguments for random number generation (see uniform).
-
-        Returns
-        -------
-        samples : TensorVariable
-            A PyTensor tensor of samples randomly drawn from a normal distribution.
+                tensor_update = at.as_tensor_variable(input.update)
+                sit_sot_inner_outputs.append(tensor_update)
+                # Note that `pos` is not a negative index. The sign of `pos` is used
+                # as a flag to indicate if this output should be part of the
+                # update rules or part of the standard outputs of `scan`.
+                # If `pos` is positive then it corresponds to the standard
+                # outputs of `scan` and it refers to output of index `pos`. If `pos`
+                # is negative that it corresponds to update rules of `scan` and it
+                # refers to the update rule with index `-1 - pos`.
+                sit_sot_rightOrder.append(-1 - len(sit_sot_shared))
+                sit_sot_shared.append(input.variable)
 
-        """
-        size = _check_size(size)
-        avg = undefined_grad(as_tensor_variable(avg))
-        std = undefined_grad(as_tensor_variable(std))
-
-        if dtype is None:
-            dtype = aes.upcast(config.floatX, avg.dtype, std.dtype)
-
-        avg = at.cast(avg, dtype=dtype)
-        std = at.cast(std, dtype=dtype)
-
-        # generate even number of uniform samples
-        # Do manual constant folding to lower optiimizer work.
-        if isinstance(size, Constant):
-            n_odd_samples = size.prod(dtype="int64")
+            else:
+                shared_inner_inputs.append(new_var)
+                shared_scan_inputs.append(input.variable)
+                shared_inner_outputs.append(input.update)
+                n_shared_outs += 1
         else:
-            n_odd_samples = prod(size, dtype="int64")
-        n_even_samples = n_odd_samples + n_odd_samples % 2
-        uniform = self.uniform(
-            (n_even_samples,),
-            low=0.0,
-            high=1.0,
-            ndim=1,
-            dtype=dtype,
-            nstreams=nstreams,
-            **kwargs,
-        )
+            no_update_shared_inputs.append(input)
 
-        # box-muller transform
-        u1 = uniform[: n_even_samples // 2]
-        u2 = uniform[n_even_samples // 2 :]
-        r = sqrt(-2.0 * log(u1))
-        theta = np.array(2.0 * np.pi, dtype=dtype) * u2
-        cos_theta, sin_theta = cos(theta), sin(theta)
-        z0 = r * cos_theta
-        z1 = r * sin_theta
-
-        if truncate:
-            # use valid samples
-            to_fix0 = (z0 < -2.0) | (z0 > 2.0)
-            to_fix1 = (z1 < -2.0) | (z1 > 2.0)
-            z0_valid = z0[at.nonzero(~to_fix0)]
-            z1_valid = z1[at.nonzero(~to_fix1)]
-
-            # re-sample invalid samples
-            to_fix0 = at.nonzero(to_fix0)[0]
-            to_fix1 = at.nonzero(to_fix1)[0]
-            n_fix_samples = to_fix0.size + to_fix1.size
-            lower = at.constant(1.0 / np.e**2, dtype=dtype)
-            u_fix = self.uniform(
-                (n_fix_samples,),
-                low=lower,
-                high=1.0,
-                ndim=1,
-                dtype=dtype,
-                nstreams=nstreams,
-                **kwargs,
-            )
-            r_fix = sqrt(-2.0 * log(u_fix))
-            z0_fixed = r_fix[: to_fix0.size] * cos_theta[to_fix0]
-            z1_fixed = r_fix[to_fix0.size :] * sin_theta[to_fix1]
+    n_sit_sot = len(sit_sot_inner_inputs)
 
-            # pack everything together to a useful result
-            norm_samples = at.join(0, z0_valid, z0_fixed, z1_valid, z1_fixed)
-        else:
-            norm_samples = at.join(0, z0, z1)
-        if isinstance(n_odd_samples, Variable):
-            samples = norm_samples[:n_odd_samples]
-        elif n_odd_samples % 2 == 1:
-            samples = norm_samples[:-1]
-        else:
-            samples = norm_samples
-        samples = reshape(samples, newshape=size, ndim=ndim)
-        samples *= std
-        samples += avg
-
-        return samples
-
-    def truncated_normal(
-        self, size, avg=0.0, std=1.0, ndim=None, dtype=None, nstreams=None, **kwargs
-    ):
-        """
-        Sample a tensor of values from a symmetrically truncated normal distribution.
+    # Step 5.4 Outputs with no taps used in the input
+    n_nit_sot = 0
+    nit_sot_inner_outputs = []
+    nit_sot_return_steps = {}
+    nit_sot_rightOrder = []
+    for i, out in enumerate(outs_info):
+        if "taps" not in out:
+            nit_sot_inner_outputs.append(outputs[i])
+            if i in return_steps:
+                nit_sot_return_steps[n_nit_sot] = return_steps[i]
+            nit_sot_rightOrder.append(i)
+            n_nit_sot += 1
+
+    # Step 5.5 all other arguments including extra inputs
+    other_scan_args = []
+    other_inner_args = []
+
+    other_scan_args += [
+        arg
+        for arg in non_seqs
+        if (not isinstance(arg, SharedVariable) and not isinstance(arg, Constant))
+    ]
+
+    # Step 5.6 all shared variables with no update rules
+    other_inner_args += [
+        safe_new(arg, "_copy")
+        for arg in non_seqs
+        if (not isinstance(arg, SharedVariable) and not isinstance(arg, Constant))
+    ]
+
+    inner_replacements.update(dict(zip(other_scan_args, other_inner_args)))
+
+    if strict:
+        non_seqs_set = set(non_sequences if non_sequences is not None else [])
+
+        other_shared_scan_args = [
+            arg.variable
+            for arg in no_update_shared_inputs
+            if arg.variable in non_seqs_set
+        ]
+        other_shared_inner_args = [
+            safe_new(arg.variable, "_copy")
+            for arg in no_update_shared_inputs
+            if arg.variable in non_seqs_set
+        ]
+    else:
+        other_shared_scan_args = [arg.variable for arg in no_update_shared_inputs]
+        other_shared_inner_args = [
+            safe_new(arg.variable, "_copy") for arg in no_update_shared_inputs
+        ]
 
-        Parameters
-        ----------
-        size : int_vector_like
-            Array dimensions for the output tensor.
-        avg : float_like, optional
-            The mean value for the truncated normal to sample from (defaults to 0.0).
-        std : float_like, optional
-            The standard deviation for the truncated normal to sample from (defaults to 1.0).
-        ndim : int, optional
-            The number of dimensions for the output tensor (defaults to None).
-            This argument is necessary if the size argument is ambiguous on the number of dimensions.
-        dtype : str, optional
-            The data-type for the output tensor. If not specified,
-            the dtype is inferred from avg and std, but it is at least as precise as floatX.
-        kwargs
-            Other keyword arguments for random number generation (see uniform).
-
-        Returns
-        -------
-        samples : TensorVariable
-            A PyTensor tensor of samples randomly drawn from a truncated normal distribution.
-
-        See Also
-        --------
-        normal
-        """
-        # constant taken from scipy.stats.truncnorm.std(a=-2, b=2, loc=0., scale=1.)
-        std = std / at.constant(0.87962566103423978)
-        return self.normal(
-            size=size,
-            avg=avg,
-            std=std,
-            truncate=True,
-            ndim=ndim,
-            dtype=dtype,
-            nstreams=nstreams,
-            **kwargs,
-        )
+    inner_replacements.update(
+        dict(zip(other_shared_scan_args, other_shared_inner_args))
+    )
 
+    ##
+    # Step 6. Re-order the outputs and clone them replacing things
+    # using `inner_replacements`
+    ##
+    inner_inputs = (
+        inner_seqs
+        + mit_mot_inner_inputs
+        + mit_sot_inner_inputs
+        + sit_sot_inner_inputs
+        + shared_inner_inputs
+        + other_shared_inner_args
+        + other_inner_args
+    )
 
-def _check_size(size):
-    """
-    Canonicalise inputs to get valid output sizes for PyTensor tensors.
+    inner_outs = (
+        mit_mot_inner_outputs
+        + mit_sot_inner_outputs
+        + sit_sot_inner_outputs
+        + nit_sot_inner_outputs
+        + shared_inner_outputs
+    )
+    if condition is not None:
+        inner_outs.append(condition)
 
-    Parameters
-    ----------
-    size : int_vector_like
-        Some variable that could serve as the shape for an PyTensor tensor.
-        This can be an int, a tuple of ints, a list of ints
-        or an PyTensor Variable with similar properties.
+    new_outs = clone_replace(inner_outs, replace=inner_replacements)
 
-    Returns
-    -------
-    size_var : int_vector
-        A one-dimensional PyTensor variable encapsulating the given size.
+    ##
+    # Step 7. Create the Scan Op
+    ##
+
+    if allow_gc is None:
+        allow_gc = config.scan__allow_gc
+
+    info = ScanInfo(
+        n_seqs=n_seqs,
+        mit_mot_in_slices=(),
+        mit_mot_out_slices=tuple(tuple(v) for v in mit_mot_out_slices),
+        mit_sot_in_slices=tuple(tuple(v) for v in mit_sot_tap_array),
+        sit_sot_in_slices=tuple((-1,) for x in range(n_sit_sot)),
+        n_shared_outs=n_shared_outs,
+        n_nit_sot=n_nit_sot,
+        n_non_seqs=len(other_shared_inner_args) + len(other_inner_args),
+        as_while=as_while,
+    )
 
-    Raises
-    ------
-    ValueError
-        If this method can not build a valid size from the input.
-    """
-    # non-tuple checks and scalar-to-tuple transform
-    if isinstance(size, Variable):
-        if size.ndim == 1:
-            return size
-        elif size.ndim == 0:
-            return at.stack([size], ndim=1)
-        else:
-            raise ValueError(
-                "PyTensor variable must have 1 dimension to be a valid size.", size
-            )
-    elif isinstance(size, (np.integer, int)):
-        return at.constant([size], ndim=1)
-    elif not isinstance(size, (tuple, list)):
-        raise ValueError("Size must be a int, tuple, list or PyTensor variable.", size)
-
-    # check entries of list or tuple
-    for i in size:
-        if isinstance(i, Variable):
-            if i.ndim != 0:
-                raise ValueError("Non-scalar PyTensor variable in size", size, i)
-        elif isinstance(i, (np.integer, int)):
-            if i <= 0:
-                raise ValueError(
-                    "Non-positive dimensions not allowed in size.", size, i
-                )
-        else:
-            raise ValueError(
-                "Only PyTensor variables and integers are allowed in a size-tuple.",
-                size,
-                i,
-            )
+    local_op = Scan(
+        inner_inputs,
+        new_outs,
+        info,
+        mode=mode,
+        truncate_gradient=truncate_gradient,
+        name=name,
+        profile=profile,
+        allow_gc=allow_gc,
+        strict=strict,
+    )
 
-    return at.as_tensor_variable(size, ndim=1)
+    ##
+    # Step 8. Compute the outputs using the scan op
+    ##
+    _scan_inputs = (
+        scan_seqs
+        + mit_mot_scan_inputs
+        + mit_sot_scan_inputs
+        + sit_sot_scan_inputs
+        + shared_scan_inputs
+        + [actual_n_steps for x in range(n_nit_sot)]
+        + other_shared_scan_args
+        + other_scan_args
+    )
 
+    scan_inputs = []
+    for arg in [actual_n_steps] + _scan_inputs:
+        try:
+            arg = at.as_tensor_variable(arg)
+        except TypeError:
+            # This happens for Random States for e.g. but it is a good way
+            # to make sure all inputs are tensors.
+            pass
+        scan_inputs += [arg]
+    scan_outs = local_op(*scan_inputs)
+    if not isinstance(scan_outs, (list, tuple)):
+        scan_outs = [scan_outs]
+    ##
+    # Step 9. Figure out which outs are update rules for shared variables
+    # and so on ...
+    ##
+
+    update_map = OrderedUpdates()
+
+    def remove_dimensions(outs, steps_return, offsets=None):
+        out_ls = []
+        for idx, out in enumerate(outs):
+            if idx in steps_return:
+                if steps_return[idx] > 1:
+                    out_ls.append(out[-steps_return[idx] :])
+                else:
+                    out_ls.append(out[-1])
+            else:
+                if offsets is None:
+                    out_ls.append(out)
+                else:
+                    out_ls.append(out[offsets[idx] :])
+        return out_ls
+
+    offset = n_mit_mot
+    offsets = [abs(np.min(x)) for x in mit_sot_tap_array]
+    mit_sot_outs = remove_dimensions(
+        scan_outs[offset : offset + n_mit_sot], mit_sot_return_steps, offsets
+    )
 
-@node_rewriter((mrg_uniform_base,))
-def mrg_random_make_inplace(fgraph, node):
+    offset += n_mit_sot
+    offsets = [1 for x in range(n_sit_sot)]
+    sit_sot_outs = remove_dimensions(
+        scan_outs[offset : offset + n_sit_sot], sit_sot_return_steps, offsets
+    )
+
+    offset += n_sit_sot
+    nit_sot_outs = remove_dimensions(
+        scan_outs[offset : offset + n_nit_sot], nit_sot_return_steps
+    )
+
+    offset += n_nit_sot
+    for idx, update_rule in enumerate(scan_outs[offset : offset + n_shared_outs]):
+        update_map[shared_scan_inputs[idx]] = update_rule
+
+    _scan_out_list = mit_sot_outs + sit_sot_outs + nit_sot_outs
+    # Step 10. I need to reorder the outputs to be in the order expected by
+    # the user
+    rightOrder = mit_sot_rightOrder + sit_sot_rightOrder + nit_sot_rightOrder
+    scan_out_list = [None] * len(rightOrder)
+    for idx, pos in enumerate(rightOrder):
+        if pos >= 0:
+            scan_out_list[pos] = _scan_out_list[idx]
+        else:
+            # Not that pos is not a negative index. The sign of pos is used
+            # as a flag to indicate if this output should be part of the
+            # update rules or part of the standard outputs of scan.
+            # If `pos` is positive than it corresponds to the standard
+            # outputs of scan and it refers to output of index `pos`. If `pos`
+            # is negative that it corresponds to update rules of scan and it
+            # refers to update rule of index -1 - `pos`.
+            update_map[sit_sot_shared[abs(pos) - 1]] = _scan_out_list[idx][-1]
+    scan_out_list = [x for x in scan_out_list if x is not None]
+    if not return_list and len(scan_out_list) == 1:
+        scan_out_list = scan_out_list[0]
+    elif len(scan_out_list) == 0:
+        scan_out_list = None
 
-    op = node.op
-    if isinstance(op, mrg_uniform_base) and not op.inplace:
-        # op might be gpu version
-        new_op = op.__class__(op.output_type, inplace=True)
-        return new_op.make_node(*node.inputs).outputs
-    return False
-
-
-optdb.register(
-    "random_make_inplace_mrg",
-    in2out(mrg_random_make_inplace, ignore_newtrees=True),
-    "fast_run",
-    "inplace",
-    position=99,
-)
+    return (scan_out_list, update_map)
```

### Comparing `pytensor-2.8.11/pytensor/scalar/basic.py` & `pytensor-2.9.1/pytensor/scalar/basic.py`

 * *Files 0% similar despite different names*

```diff
@@ -4445,30 +4445,7 @@
     new_outs = new_op(*[mapping[i] for i in node.inputs], return_list=True)
     assert len(new_outs) == len(node.outputs)
     for o, no in zip(node.outputs, new_outs):
         mapping[o] = no
 
 
 Compositef32.special[Composite] = handle_composite
-
-
-DEPRECATED_NAMES = [
-    ("Inv", "`Inv` is deprecated; use `Reciprocal` instead.", Reciprocal),
-    ("inv", "`inv` is deprecated; use `reciprocal` instead.", reciprocal),
-    ("Scalar", "`Scalar` is deprecated; use `ScalarType` instead.", ScalarType),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
```

### Comparing `pytensor-2.8.11/pytensor/scalar/c_code/Faddeeva.cc` & `pytensor-2.9.1/pytensor/scalar/c_code/Faddeeva.cc`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scalar/c_code/Faddeeva.hh` & `pytensor-2.9.1/pytensor/scalar/c_code/Faddeeva.hh`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scalar/c_code/gamma.c` & `pytensor-2.9.1/pytensor/scalar/c_code/gamma.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scalar/math.py` & `pytensor-2.9.1/pytensor/scalar/math.py`

 * *Files 15% similar despite different names*

```diff
@@ -1477,7 +1477,173 @@
         return np.nan
 
     def c_code(self, *args, **kwargs):
         raise NotImplementedError()
 
 
 betainc_der = BetaIncDer(upgrade_to_float_no_complex, name="betainc_der")
+
+
+class Hyp2F1(ScalarOp):
+    """
+    Gaussian hypergeometric function ``2F1(a, b; c; z)``.
+
+    """
+
+    nin = 4
+    nfunc_spec = ("scipy.special.hyp2f1", 4, 1)
+
+    @staticmethod
+    def st_impl(a, b, c, z):
+        return scipy.special.hyp2f1(a, b, c, z)
+
+    def impl(self, a, b, c, z):
+        return Hyp2F1.st_impl(a, b, c, z)
+
+    def grad(self, inputs, grads):
+        a, b, c, z = inputs
+        (gz,) = grads
+        return [
+            gz * hyp2f1_der(a, b, c, z, wrt=0),
+            gz * hyp2f1_der(a, b, c, z, wrt=1),
+            gz * hyp2f1_der(a, b, c, z, wrt=2),
+            gz * ((a * b) / c) * hyp2f1(a + 1, b + 1, c + 1, z),
+        ]
+
+    def c_code(self, *args, **kwargs):
+        raise NotImplementedError()
+
+
+hyp2f1 = Hyp2F1(upgrade_to_float, name="hyp2f1")
+
+
+class Hyp2F1Der(ScalarOp):
+    """
+    Derivatives of the Gaussian Hypergeometric function ``2F1(a, b; c; z)`` with respect to one of the first 3 inputs.
+
+    Adapted from https://github.com/stan-dev/math/blob/develop/stan/math/prim/fun/grad_2F1.hpp
+    """
+
+    nin = 5
+
+    def impl(self, a, b, c, z, wrt):
+        def check_2f1_converges(a, b, c, z) -> bool:
+            num_terms = 0
+            is_polynomial = False
+
+            def is_nonpositive_integer(x):
+                return x <= 0 and x.is_integer()
+
+            if is_nonpositive_integer(a) and abs(a) >= num_terms:
+                is_polynomial = True
+                num_terms = int(np.floor(abs(a)))
+            if is_nonpositive_integer(b) and abs(b) >= num_terms:
+                is_polynomial = True
+                num_terms = int(np.floor(abs(b)))
+
+            is_undefined = is_nonpositive_integer(c) and abs(c) <= num_terms
+
+            return not is_undefined and (
+                is_polynomial or np.abs(z) < 1 or (np.abs(z) == 1 and c > (a + b))
+            )
+
+        def compute_grad_2f1(a, b, c, z, wrt):
+            """
+            Notes
+            -----
+            The algorithm can be derived by looking at the ratio of two successive terms in the series
+            β_{k+1}/β_{k} = A(k)/B(k)
+            β_{k+1} = A(k)/B(k) * β_{k}
+            d[β_{k+1}] = d[A(k)/B(k)] * β_{k} + A(k)/B(k) * d[β_{k}] via the product rule
+
+            In the 2F1, A(k)/B(k) corresponds to (((a + k) * (b + k) / ((c + k) (1 + k))) * z
+
+            The partial d[A(k)/B(k)] with respect to the 3 first inputs can be obtained from the ratio A(k)/B(k),
+            by dropping the respective term
+            d/da[A(k)/B(k)] = A(k)/B(k) / (a + k)
+            d/db[A(k)/B(k)] = A(k)/B(k) / (b + k)
+            d/dc[A(k)/B(k)] = A(k)/B(k) * (c + k)
+
+            The algorithm is implemented in the log scale, which adds the complexity of working with absolute terms and
+            tracking their signs.
+            """
+
+            wrt_a = wrt_b = False
+            if wrt == 0:
+                wrt_a = True
+            elif wrt == 1:
+                wrt_b = True
+            elif wrt != 2:
+                raise ValueError(f"wrt must be 0, 1, or 2, got {wrt}")
+
+            min_steps = 10  # https://github.com/stan-dev/math/issues/2857
+            max_steps = int(1e6)
+            precision = 1e-14
+
+            res = 0
+
+            if z == 0:
+                return res
+
+            log_g_old = -np.inf
+            log_t_old = 0.0
+            log_t_new = 0.0
+            sign_z = np.sign(z)
+            log_z = np.log(np.abs(z))
+
+            log_g_old_sign = 1
+            log_t_old_sign = 1
+            log_t_new_sign = 1
+            sign_zk = sign_z
+
+            for k in range(max_steps):
+                p = (a + k) * (b + k) / ((c + k) * (k + 1))
+                if p == 0:
+                    return res
+                log_t_new += np.log(np.abs(p)) + log_z
+                log_t_new_sign = np.sign(p) * log_t_new_sign
+
+                term = log_g_old_sign * log_t_old_sign * np.exp(log_g_old - log_t_old)
+                if wrt_a:
+                    term += np.reciprocal(a + k)
+                elif wrt_b:
+                    term += np.reciprocal(b + k)
+                else:
+                    term -= np.reciprocal(c + k)
+
+                log_g_old = log_t_new + np.log(np.abs(term))
+                log_g_old_sign = np.sign(term) * log_t_new_sign
+                g_current = log_g_old_sign * np.exp(log_g_old) * sign_zk
+                res += g_current
+
+                log_t_old = log_t_new
+                log_t_old_sign = log_t_new_sign
+                sign_zk *= sign_z
+
+                if k >= min_steps and np.abs(g_current) <= precision:
+                    return res
+
+            warnings.warn(
+                f"hyp2f1_der did not converge after {k} iterations",
+                RuntimeWarning,
+            )
+            return np.nan
+
+        # TODO: We could implement the Euler transform to expand supported domain, as Stan does
+        if not check_2f1_converges(a, b, c, z):
+            warnings.warn(
+                f"Hyp2F1 does not meet convergence conditions with given arguments a={a}, b={b}, c={c}, z={z}",
+                RuntimeWarning,
+            )
+            return np.nan
+
+        return compute_grad_2f1(a, b, c, z, wrt=wrt)
+
+    def __call__(self, a, b, c, z, wrt):
+        # This allows wrt to be a keyword argument
+        return super().__call__(a, b, c, z, wrt)
+
+    def c_code(self, *args, **kwargs):
+        raise NotImplementedError()
+
+
+hyp2f1_der = Hyp2F1Der(upgrade_to_float, name="hyp2f1_der")
```

### Comparing `pytensor-2.8.11/pytensor/scalar/sharedvar.py` & `pytensor-2.9.1/pytensor/scalar/sharedvar.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scan/__init__.py` & `pytensor-2.9.1/pytensor/scan/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scan/checkpoints.py` & `pytensor-2.9.1/pytensor/scan/checkpoints.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scan/op.py` & `pytensor-2.9.1/pytensor/scan/op.py`

 * *Files 0% similar despite different names*

```diff
@@ -3421,15 +3421,15 @@
                     total_scan_fct_time / total_super_scan_time * 100,
                     total_scan_op_time / total_super_scan_time * 100,
                 ),
                 file=file,
             )
 
 
-@op_debug_information.register(Scan)
+@op_debug_information.register(Scan)  # noqa
 def _op_debug_information_Scan(op: Scan, node: Apply):
     from typing import Sequence
 
     from pytensor.scan.utils import ScanArgs
 
     extra_information = {}
```

### Comparing `pytensor-2.8.11/pytensor/scan/rewriting.py` & `pytensor-2.9.1/pytensor/scan/rewriting.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scan/utils.py` & `pytensor-2.9.1/pytensor/scan/utils.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/scan/views.py` & `pytensor-2.9.1/pytensor/scan/views.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sparse/__init__.py` & `pytensor-2.9.1/pytensor/sparse/__init__.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sparse/basic.py` & `pytensor-2.9.1/pytensor/sparse/basic.py`

 * *Files 1% similar despite different names*

```diff
@@ -3447,15 +3447,20 @@
 
         if _is_sparse_variable(b):
             return Apply(self, [a, b], [SparseTensorType(a.type.format, dtype_out)()])
         else:
             return Apply(
                 self,
                 [a, b],
-                [tensor(dtype_out, shape=(None, 1 if b.type.shape[1] == 1 else None))],
+                [
+                    tensor(
+                        dtype=dtype_out,
+                        shape=(None, 1 if b.type.shape[1] == 1 else None),
+                    )
+                ],
             )
 
     def perform(self, node, inputs, outputs):
         (a, b) = inputs
         (out,) = outputs
         if a.shape[1] != b.shape[0]:
             raise ValueError(
@@ -3578,15 +3583,17 @@
     # :note: The grad implemented is structured.
     # :note: a_* are the corresponding properties of a sparse
     #        matrix in csc format.
     __props__ = ()
 
     def make_node(self, a_indices, a_indptr, b, g_ab):
         return Apply(
-            self, [a_indices, a_indptr, b, g_ab], [tensor(g_ab.dtype, shape=(None,))]
+            self,
+            [a_indices, a_indptr, b, g_ab],
+            [tensor(dtype=g_ab.dtype, shape=(None,))],
         )
 
     def perform(self, node, inputs, outputs):
         (a_indices, a_indptr, b, g_ab) = inputs
         (out,) = outputs
         g_a_data = np.zeros(a_indices.shape, dtype=g_ab.dtype)
         for j in range(len(a_indptr) - 1):
@@ -3712,15 +3719,15 @@
     # :note: The grad implemented is structured.
     # :note: a_* are the corresponding properties of a sparse
     #        matrix in csr format.
     __props__ = ()
 
     def make_node(self, a_indices, a_indptr, b, g_ab):
         return Apply(
-            self, [a_indices, a_indptr, b, g_ab], [tensor(b.dtype, shape=(None,))]
+            self, [a_indices, a_indptr, b, g_ab], [tensor(dtype=b.dtype, shape=(None,))]
         )
 
     def perform(self, node, inputs, outputs):
         (a_indices, a_indptr, b, g_ab) = inputs
         (out,) = outputs
         g_a_data = np.zeros(a_indices.shape, dtype=g_ab.dtype)
         for i in range(len(a_indptr) - 1):  # loop over rows
```

### Comparing `pytensor-2.8.11/pytensor/sparse/rewriting.py` & `pytensor-2.9.1/pytensor/sparse/rewriting.py`

 * *Files 2% similar despite different names*

```diff
@@ -266,15 +266,19 @@
     __props__ = ()
 
     def make_node(self, a_val, a_ind, a_ptr, a_nrows, b):
         dtype_out = aes.upcast(a_val.type.dtype, b.type.dtype)
         r = Apply(
             self,
             [a_val, a_ind, a_ptr, a_nrows, b],
-            [tensor(dtype_out, shape=(None, 1 if b.type.shape[1] == 1 else None))],
+            [
+                tensor(
+                    dtype=dtype_out, shape=(None, 1 if b.type.shape[1] == 1 else None)
+                )
+            ],
         )
         return r
 
     def perform(self, node, inputs, outputs):
         (a_val, a_ind, a_ptr, a_nrows, b) = inputs
         (out,) = outputs
         a = scipy.sparse.csc_matrix(
@@ -461,15 +465,20 @@
     __props__ = ()
 
     def make_node(self, a_val, a_ind, a_ptr, b):
         self.dtype_out = aes.upcast(a_val.type.dtype, b.type.dtype)
         r = Apply(
             self,
             [a_val, a_ind, a_ptr, b],
-            [tensor(self.dtype_out, shape=(None, 1 if b.type.shape[1] == 1 else None))],
+            [
+                tensor(
+                    dtype=self.dtype_out,
+                    shape=(None, 1 if b.type.shape[1] == 1 else None),
+                )
+            ],
         )
         return r
 
     def perform(self, node, inputs, outputs):
         (a_val, a_ind, a_ptr, b) = inputs
         (out,) = outputs
         a = scipy.sparse.csr_matrix(
@@ -701,15 +710,19 @@
             y = cast(y, dtype_out)
         if dtype_out != z.type.dtype:
             z = cast(z, dtype_out)
 
         r = Apply(
             self,
             [alpha, x_val, x_ind, x_ptr, x_nrows, y, z],
-            [tensor(dtype_out, shape=(None, 1 if y.type.shape[1] == 1 else None))],
+            [
+                tensor(
+                    dtype=dtype_out, shape=(None, 1 if y.type.shape[1] == 1 else None)
+                )
+            ],
         )
         return r
 
     def c_support_code(self, **kwargs):
         return blas.blas_header_text()
 
     def c_libraries(self, **kwargs):
@@ -1138,15 +1151,17 @@
 
         The dtype of `a_data`, i.e. the dtype of the sparse matrix, cannot be a
         complex type.
 
         """
         assert b.type.ndim == 2
         return Apply(
-            self, [a_data, a_indices, a_indptr, b], [tensor(b.dtype, shape=(None,))]
+            self,
+            [a_data, a_indices, a_indptr, b],
+            [tensor(dtype=b.dtype, shape=(None,))],
         )
 
     def c_code_cache_version(self):
         return (3,)
 
     def c_code(self, node, name, inputs, outputs, sub):
 
@@ -1276,15 +1291,17 @@
 
         The dtype of `a_data`, i.e. the dtype of the sparse matrix,
         cannot be a complex type.
 
         """
         assert b.type.ndim == 2
         return Apply(
-            self, [a_data, a_indices, a_indptr, b], [tensor(b.dtype, shape=(None,))]
+            self,
+            [a_data, a_indices, a_indptr, b],
+            [tensor(dtype=b.dtype, shape=(None,))],
         )
 
     def c_code_cache_version(self):
         return (3,)
 
     def c_code(self, node, name, inputs, outputs, sub):
 
@@ -1466,15 +1483,17 @@
 
         The dtype of `a_data`, i.e. the dtype of the sparse matrix,
         cannot be a complex type.
 
         """
         assert b.type.ndim == 1
         return Apply(
-            self, [a_data, a_indices, a_indptr, b], [tensor(b.dtype, shape=(None,))]
+            self,
+            [a_data, a_indices, a_indptr, b],
+            [tensor(dtype=b.dtype, shape=(None,))],
         )
 
     def c_code_cache_version(self):
         return (2,)
 
     def c_code(self, node, name, inputs, outputs, sub):
         (
@@ -1638,15 +1657,17 @@
         a_indices = as_tensor_variable(a_indices)
         a_indptr = as_tensor_variable(a_indptr)
         assert a_data.type.ndim == 1
         assert a_indices.type.ndim == 1
         assert a_indptr.type.ndim == 1
         assert b.type.ndim == 1
         return Apply(
-            self, [a_data, a_indices, a_indptr, b], [tensor(b.dtype, shape=(None,))]
+            self,
+            [a_data, a_indices, a_indptr, b],
+            [tensor(dtype=b.dtype, shape=(None,))],
         )
 
     def c_code_cache_version(self):
         return (3,)
 
     def c_code(self, node, name, inputs, outputs, sub):
         (
```

### Comparing `pytensor-2.8.11/pytensor/sparse/sandbox/sp.py` & `pytensor-2.9.1/pytensor/sparse/sandbox/sp.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sparse/sandbox/sp2.py` & `pytensor-2.9.1/pytensor/sparse/sandbox/sp2.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sparse/sharedvar.py` & `pytensor-2.9.1/pytensor/sparse/sharedvar.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/sparse/type.py` & `pytensor-2.9.1/pytensor/sparse/type.py`

 * *Files 4% similar despite different names*

```diff
@@ -247,10 +247,7 @@
     """
     Py_XDECREF(%(oname)s);
     %(oname)s = %(iname)s;
     Py_XINCREF(%(oname)s);
     """,
     1,
 )
-
-# This is a deprecated alias used for (temporary) backward-compatibility
-SparseType = SparseTensorType
```

### Comparing `pytensor-2.8.11/pytensor/sparse/utils.py` & `pytensor-2.9.1/pytensor/sparse/utils.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/__init__.py` & `pytensor-2.9.1/pytensor/tensor/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -95,15 +95,15 @@
 
 @_get_vector_length.register(Constant)
 def _get_vector_length_Constant(op: Union[Op, Variable], var: Constant) -> int:
     return len(var.data)
 
 
 import pytensor.tensor.exceptions  # noqa
-from pytensor.gradient import consider_constant, grad, hessian, jacobian  # noqa
+from pytensor.gradient import grad, hessian, jacobian  # noqa
 
 # adds shared-variable constructors
 from pytensor.tensor import sharedvar  # noqa
 from pytensor.tensor import (  # noqa
     blas,
     blas_c,
     blas_scipy,
```

### Comparing `pytensor-2.8.11/pytensor/tensor/basic.py` & `pytensor-2.9.1/pytensor/tensor/basic.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,20 +3,17 @@
 This module primarily defines `Op`\s for the creation, conversion, and
 manipulation of tensors.
 
 """
 
 import builtins
 import warnings
-from collections.abc import Sequence
 from functools import partial
 from numbers import Number
-from typing import TYPE_CHECKING, Optional
-from typing import Sequence as TypeSequence
-from typing import Tuple, Union
+from typing import TYPE_CHECKING, Optional, Sequence, Tuple, Union
 from typing import cast as type_cast
 
 import numpy as np
 from numpy.core.multiarray import normalize_axis_index
 from numpy.core.numeric import normalize_axis_tuple
 
 import pytensor
@@ -1333,16 +1330,16 @@
     _x = as_tensor_variable(x)
     if dtype is None:
         dtype = _x.dtype
     return eye(_x.shape[0], _x.shape[1], k=0, dtype=dtype)
 
 
 def infer_static_shape(
-    shape: Union[Variable, TypeSequence[Union[Variable, int]]]
-) -> Tuple[TypeSequence["TensorLike"], TypeSequence[Optional[int]]]:
+    shape: Union[Variable, Sequence[Union[Variable, int]]]
+) -> Tuple[Sequence["TensorLike"], Sequence[Optional[int]]]:
     """Infer the static shapes implied by the potentially symbolic elements in `shape`.
 
     `shape` will be validated and constant folded.  As a result, this function
     can be expensive and shouldn't be used unless absolutely necessary.
 
     It mostly exists as a hold-over from pre-static shape times, when it was
     required in order to produce correct broadcastable arrays and prevent
@@ -2216,23 +2213,22 @@
         else:
             # When the axis is fixed, a dimension should be
             # broadcastable if at least one of the inputs is
             # broadcastable on that dimension (see justification below),
             # except for the axis dimension.
             # Initialize bcastable all false, and then fill in some trues with
             # the loops.
-            ndim = tensors[0].type.ndim
-            out_shape = [None] * ndim
 
             if not isinstance(axis, int):
                 try:
                     axis = int(get_scalar_constant_value(axis))
                 except NotScalarConstantError:
                     pass
 
+            ndim = tensors[0].type.ndim
             if isinstance(axis, int):
                 # Basically, broadcastable -> length 1, but the
                 # converse does not hold. So we permit e.g. T/F/T
                 # joins, and if they fail at runtime they fail, but if
                 # they don't then it means that the argument where
                 # that broadcastable flag was False had length 1 along
                 # this dimension, and therefore this dimension should
@@ -2240,38 +2236,63 @@
 
                 if axis < -ndim:
                     raise IndexError(
                         f"Axis value {axis} is out of range for the given input dimensions"
                     )
                 if axis < 0:
                     axis += ndim
-
-                for x in tensors:
-                    for current_axis, s in enumerate(x.type.shape):
-                        # Constant negative axis can no longer be negative at
-                        # this point. It safe to compare this way.
-                        if current_axis == axis:
-                            continue
-                        if s == 1:
-                            out_shape[current_axis] = 1
-                try:
-                    out_shape[axis] = None
-                except IndexError:
+                if axis > ndim - 1:
                     raise ValueError(
                         f"Axis value {axis} is out of range for the given input dimensions"
                     )
+                # NOTE: Constant negative axis can no longer be negative at this point.
+
+                in_shapes = [x.type.shape for x in tensors]
+                in_ndims = [len(s) for s in in_shapes]
+                if set(in_ndims) != {ndim}:
+                    raise TypeError(
+                        "Only tensors with the same number of dimensions can be joined."
+                        f" Input ndims were: {in_ndims}."
+                    )
+
+                # Determine output shapes from a matrix of input shapes
+                in_shapes = np.array(in_shapes)
+                out_shape = [None] * ndim
+                for d in range(ndim):
+                    ins = in_shapes[:, d]
+                    if d == axis:
+                        # Any unknown size along the axis means we can't sum
+                        if None in ins:
+                            out_shape[d] = None
+                        else:
+                            out_shape[d] = sum(ins)
+                    else:
+                        inset = set(in_shapes[:, d])
+                        # Other dims must match exactly,
+                        # or if a mix of None and ? the output will be ?
+                        # otherwise the input shapes are incompatible.
+                        if len(inset) == 1:
+                            (out_shape[d],) = inset
+                        elif len(inset - {None}) == 1:
+                            (out_shape[d],) = inset - {None}
+                        else:
+                            raise ValueError(
+                                f"all input array dimensions other than the specified `axis` ({axis})"
+                                " must match exactly, or be unknown (None),"
+                                f" but along dimension {d}, the inputs shapes are incompatible: {ins}"
+                            )
             else:
                 # When the axis may vary, no dimension can be guaranteed to be
                 # broadcastable.
                 out_shape = [None] * tensors[0].type.ndim
 
-        if not builtins.all(x.ndim == len(out_shape) for x in tensors):
-            raise TypeError(
-                "Only tensors with the same number of dimensions can be joined"
-            )
+            if not builtins.all(x.ndim == len(out_shape) for x in tensors):
+                raise TypeError(
+                    "Only tensors with the same number of dimensions can be joined"
+                )
 
         inputs = [as_tensor_variable(axis)] + list(tensors)
 
         if inputs[0].type.dtype not in int_dtypes:
             raise TypeError(f"Axis value {inputs[0]} must be an integer type")
 
         return Apply(self, inputs, [tensor(dtype=out_dtype, shape=out_shape)])
@@ -2534,27 +2555,24 @@
     end_slice = slice(0, -shift)
     end_list = [allslice] * axis + [end_slice] + [allslice] * (_x.ndim - axis - 1)
     return join(
         axis, _x.__getitem__(tuple(front_list)), _x.__getitem__(tuple(end_list))
     )
 
 
-def stack(*tensors, **kwargs):
+def stack(tensors: Sequence[TensorVariable], axis: int = 0):
     """Stack tensors in sequence on given axis (default is 0).
 
     Take a sequence of tensors and stack them on given axis to make a single
     tensor. The size in dimension `axis` of the result will be equal to the number
     of tensors passed.
 
-    Note: The interface stack(*tensors) is deprecated, you should use
-    stack(tensors, axis=0) instead.
-
     Parameters
     ----------
-    tensors : list or tuple of tensors
+    tensors : Sequence[TensorVariable]
         A list of tensors to be stacked.
     axis : int
         The index of the new axis. Default value is 0.
 
     Examples
     --------
     >>> a = pytensor.tensor.type.scalar()
@@ -2581,43 +2599,17 @@
     >>> x = pytensor.tensor.stack([a, b, c], axis=-2)
     >>> x.ndim
     5
     >>> rval = x.eval(dict((t, np.zeros((2, 2, 2, 2))) for t in [a, b, c]))
     >>> rval.shape # 3 tensors are stacked on axis -2
     (2, 2, 2, 3, 2)
     """
-    # ---> Remove this when moving to the new interface:
-    if not tensors and not kwargs:
-        raise ValueError("No tensor arguments provided")
-
-    if not kwargs and not isinstance(tensors[0], (list, tuple)):
-        warnings.warn(
-            "stack(*tensors) interface is deprecated, use"
-            " stack(tensors, axis=0) instead.",
-            DeprecationWarning,
-            stacklevel=3,
-        )
-        axis = 0
-    elif "tensors" in kwargs:
-        tensors = kwargs["tensors"]
-        if "axis" in kwargs:
-            axis = kwargs["axis"]
-        else:
-            axis = 0
-    else:
-        if len(tensors) == 2:
-            axis = tensors[1]
-        elif "axis" in kwargs:
-            axis = kwargs["axis"]
-        else:
-            axis = 0
-        tensors = tensors[0]
-    # <--- Until here.
-
-    if len(tensors) == 0:
+    if not isinstance(tensors, Sequence):
+        raise TypeError("First argument should be Sequence[TensorVariable]")
+    elif len(tensors) == 0:
         raise ValueError("No tensor arguments provided")
 
     # If all tensors are scalars of the same type, call make_vector.
     # It makes the graph simpler, by not adding DimShuffles and SpecifyShapes
 
     # This should be an optimization!
     # Doing it here make the graph less canonicalized
@@ -2698,44 +2690,37 @@
         if _arg.type.ndim != 2:
             raise ValueError("All arguments must have two dimensions")
         _args.append(_arg)
 
     return concatenate(_args, axis=0)
 
 
-def is_flat(var, ndim=None, outdim=None):
+def is_flat(var, ndim=1):
     """
     Verifies the dimensionality of the var is equal to
-    outdim. This method is usually called after flatten method on a
-    variable, where the first outdim-1 dimension size(s) of the variable
+    ndim. This method is usually called after flatten method on a
+    variable, where the first ndim-1 dimension size(s) of the variable
     is kept intact, and the last dimension size of the variable is made
     equal to the multiplication of its remaining dimension size(s), such that
-    the variable would end up with as many dimension as outdim.
+    the variable would end up with as many dimension as ndim.
 
     Parameters
     ----------
-        var : pytensor.tensor.var.TensorVariable
-            the pytensor var on which the dimensionality is checked.
+    var : pytensor.tensor.var.TensorVariable
+        the pytensor var on which the dimensionality is checked.
 
-        outdim : int
-            the expected dimensionality of var.
+    ndim : int
+        the expected dimensionality of var.
 
     Returns
     -------
     bool
         the comparison result of var's dim
         and the expected outdim.
     """
-    if outdim is None and ndim is None:
-        ndim = 1
-    elif outdim is not None and ndim is not None:
-        raise ValueError("You should only specify ndim")
-    elif outdim is not None:
-        warnings.warn("outdim` is deprecated; use `ndim` instead.")
-        ndim = outdim
     return var.ndim == ndim
 
 
 def flatten(x, ndim=1):
     """Return a copy of the array collapsed into one dimension.
 
     Reshapes the variable `x` by keeping the first outdim-1 dimension size(s)
@@ -2878,15 +2863,15 @@
     def make_node(self, start, stop, step):
         start, stop, step = map(as_tensor_variable, (start, stop, step))
         assert start.ndim == 0
         assert stop.ndim == 0
         assert step.ndim == 0
 
         inputs = [start, stop, step]
-        outputs = [tensor(self.dtype, shape=(None,))]
+        outputs = [tensor(dtype=self.dtype, shape=(None,))]
 
         return Apply(self, inputs, outputs)
 
     @config.change_flags(warn_float64="ignore")
     def infer_shape(self, fgraph, node, i_shapes):
         from pytensor.tensor.math import ceil, maximum
 
@@ -3658,16 +3643,16 @@
     li = list(range(0, ndim))
     li[axis1], li[axis2] = li[axis2], li[axis1]
     return y.dimshuffle(li)
 
 
 def moveaxis(
     a: Union[np.ndarray, TensorVariable],
-    source: Union[int, TypeSequence[int]],
-    destination: Union[int, TypeSequence[int]],
+    source: Union[int, Sequence[int]],
+    destination: Union[int, Sequence[int]],
 ) -> TensorVariable:
     """Move axes of a TensorVariable to new positions.
 
     Other axes remain in their original order.
 
     Parameters
     ----------
```

### Comparing `pytensor-2.8.11/pytensor/tensor/blas.py` & `pytensor-2.9.1/pytensor/tensor/blas.py`

 * *Files 0% similar despite different names*

```diff
@@ -1676,15 +1676,15 @@
         dtypes = ("float16", "float32", "float64", "complex64", "complex128")
         if x.type.ndim != 2 or x.type.dtype not in dtypes:
             raise TypeError(x)
         if y.type.ndim != 2 or y.type.dtype not in dtypes:
             raise TypeError(y)
         if y.type.dtype != x.type.dtype:
             raise TypeError("dtype mismatch to Dot22")
-        outputs = [tensor(x.type.dtype, shape=(x.type.shape[0], y.type.shape[1]))]
+        outputs = [tensor(dtype=x.type.dtype, shape=(x.type.shape[0], y.type.shape[1]))]
         return Apply(self, [x, y], outputs)
 
     def perform(self, node, inp, out):
         x, y = inp
         (z,) = out
         try:
             z[0] = np.asarray(np.dot(x, y))
@@ -1981,15 +1981,15 @@
                 "Dot22Scalar requires matching dtypes", (a.dtype, x.dtype, y.dtype)
             )
 
         if not a.dtype.startswith("float") and not a.dtype.startswith("complex"):
             raise TypeError("Dot22Scalar requires float or complex args", a.dtype)
 
         sz = (x.type.shape[0], y.type.shape[1])
-        outputs = [tensor(x.type.dtype, shape=sz)]
+        outputs = [tensor(dtype=x.type.dtype, shape=sz)]
         return Apply(self, [x, y, a], outputs)
 
     def perform(self, node, inp, out):
         x, y, scalar = inp
         (z,) = out
         try:
             z[0] = np.asarray(scalar * np.dot(x, y))
@@ -2217,15 +2217,15 @@
                 if inputs[0].type.shape[0] == 1 or inputs[1].type.shape[0] == 1
                 else None,
             )
             + inputs[0].type.shape[1:-1]
             + inputs[1].type.shape[2:]
         )
         out_shape = tuple(1 if s == 1 else None for s in out_shape)
-        return Apply(self, upcasted_inputs, [tensor(dtype, shape=out_shape)])
+        return Apply(self, upcasted_inputs, [tensor(dtype=dtype, shape=out_shape)])
 
     def perform(self, node, inp, out):
         x, y = inp
         (z,) = out
 
         if x.shape[0] != y.shape[0]:
             raise TypeError(
```

### Comparing `pytensor-2.8.11/pytensor/tensor/blas_c.py` & `pytensor-2.9.1/pytensor/tensor/blas_c.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/blas_headers.py` & `pytensor-2.9.1/pytensor/tensor/blas_headers.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/blas_scipy.py` & `pytensor-2.9.1/pytensor/tensor/blas_scipy.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/c_code/alt_blas_common.h` & `pytensor-2.9.1/pytensor/tensor/c_code/alt_blas_common.h`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/c_code/alt_blas_template.c` & `pytensor-2.9.1/pytensor/tensor/c_code/alt_blas_template.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/c_code/dimshuffle.c` & `pytensor-2.9.1/pytensor/tensor/c_code/dimshuffle.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/elemwise.py` & `pytensor-2.9.1/pytensor/tensor/elemwise.py`

 * *Files 0% similar despite different names*

```diff
@@ -1754,15 +1754,15 @@
             elemwise_name = f"Elemwise{{{symbolname},no_inplace}}"
             scalar_op = getattr(scalar, symbolname)
             rval = Elemwise(
                 scalar_op, name=elemwise_name, nfunc_spec=(nfunc and (nfunc, nin, nout))
             )
 
         if getattr(symbol, "__doc__"):
-            rval.__doc__ = symbol.__doc__ + "\n" + rval.__doc__
+            rval.__doc__ = symbol.__doc__ + "\n\n    " + rval.__doc__
 
         # for the meaning of this see the ./epydoc script
         # it makes epydoc display rval as if it were a function, not an object
         rval.__epydoc_asRoutine = symbol
         rval.__module__ = symbol.__module__
 
         pprint.assign(rval, FunctionPrinter([symbolname.replace("_inplace", "=")]))
```

### Comparing `pytensor-2.8.11/pytensor/tensor/elemwise_cgen.py` & `pytensor-2.9.1/pytensor/tensor/elemwise_cgen.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/extra_ops.py` & `pytensor-2.9.1/pytensor/tensor/extra_ops.py`

 * *Files 2% similar despite different names*

```diff
@@ -1639,14 +1639,19 @@
         return super().__call__(a, *shape, **kwargs)
 
     def make_node(self, a, *shape):
         a = at.as_tensor_variable(a)
 
         shape, static_shape = at.infer_static_shape(shape)
 
+        if len(shape) < a.ndim:
+            raise ValueError(
+                f"Broadcast target shape has {len(shape)} dims, which is shorter than input with {a.ndim} dims"
+            )
+
         out = TensorType(dtype=a.type.dtype, shape=static_shape)()
 
         # Attempt to prevent in-place operations on this view-based output
         out.tag.indestructible = True
 
         return Apply(self, [a] + shape, [out])
 
@@ -1682,43 +1687,60 @@
             grad_undefined(self, i, shp) for i, shp in enumerate(shape, 1)
         ]
 
     def infer_shape(self, fgraph, node, ins_shapes):
         return [node.inputs[1:]]
 
     def c_code(self, node, name, inputs, outputs, sub):
+        inp_dims = node.inputs[0].ndim
+        out_dims = node.outputs[0].ndim
+        new_dims = out_dims - inp_dims
+
         (x, *shape) = inputs
         (out,) = outputs
-        ndims = len(shape)
         fail = sub["fail"]
 
         # TODO: Could just use `PyArray_Return`, no?
         dims_array = ", ".join(
             [
                 f"((dtype_{shape}*)(PyArray_DATA({shape})))[0]"
                 for i, shape in enumerate(shape)
             ]
         )
 
         src = (
             """
-            npy_intp itershape[%(ndims)s] = {%(dims_array)s};
+            npy_intp itershape[%(out_dims)s] = {%(dims_array)s};
 
+            NpyIter *iter;
             PyArrayObject *ops[1] = {%(x)s};
             npy_uint32 flags = NPY_ITER_MULTI_INDEX | NPY_ITER_REFS_OK | NPY_ITER_ZEROSIZE_OK;
             npy_uint32 op_flags[1] = {NPY_ITER_READONLY};
             PyArray_Descr *op_dtypes[1] = {NULL};
-            int oa_ndim = %(ndims)s;
+            int oa_ndim = %(out_dims)s;
             int* op_axes[1] = {NULL};
             npy_intp buffersize = 0;
 
-            NpyIter *iter = NpyIter_AdvancedNew(
+            for(int i = 0; i < %(inp_dims)s; i++)
+            {
+                if ((PyArray_DIMS(%(x)s)[i] != 1) && (PyArray_DIMS(%(x)s)[i] != itershape[i + %(new_dims)s]))
+                {
+                    PyErr_Format(PyExc_ValueError,
+                                 "Shape mismatch in broadcast_to: target shape[%%i] = %%lld is incompatible with input shape = %%lld.",
+                                 i,
+                                 (long long int) itershape[i + %(new_dims)s],
+                                 (long long int) PyArray_DIMS(%(x)s)[i]
+                    );
+                    %(fail)s
+                }
+            }
+
+            iter = NpyIter_AdvancedNew(
                 1, ops, flags, NPY_CORDER, NPY_NO_CASTING, op_flags, op_dtypes, oa_ndim, op_axes, itershape, buffersize
             );
-
             %(out)s = NpyIter_GetIterView(iter, 0);
 
             if(%(out)s == NULL){
                 NpyIter_Deallocate(iter);
                 %(fail)s;
             }
 
@@ -1729,15 +1751,15 @@
             """
             % locals()
         )
 
         return src
 
     def c_code_cache_version(self):
-        return (1,)
+        return (2,)
 
 
 broadcast_to_ = BroadcastTo()
 
 
 def geomspace(start, end, steps, base=10.0):
     from pytensor.tensor.math import log
```

### Comparing `pytensor-2.8.11/pytensor/tensor/fft.py` & `pytensor-2.9.1/pytensor/tensor/fft.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/fourier.py` & `pytensor-2.9.1/pytensor/tensor/fourier.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/inplace.py` & `pytensor-2.9.1/pytensor/tensor/inplace.py`

 * *Files 2% similar despite different names*

```diff
@@ -388,14 +388,19 @@
 
 
 @scalar_elemwise
 def conj_inplace(a):
     """elementwise conjugate (inplace on `a`)"""
 
 
+@scalar_elemwise
+def hyp2f1_inplace(a, b, c, z):
+    """gaussian hypergeometric function"""
+
+
 pprint.assign(add_inplace, printing.OperatorPrinter("+=", -2, "either"))
 pprint.assign(mul_inplace, printing.OperatorPrinter("*=", -1, "either"))
 pprint.assign(sub_inplace, printing.OperatorPrinter("-=", -2, "left"))
 pprint.assign(neg_inplace, printing.OperatorPrinter("-=", 0, "either"))
 pprint.assign(true_div_inplace, printing.OperatorPrinter("/=", -1, "left"))
 pprint.assign(int_div_inplace, printing.OperatorPrinter("//=", -1, "left"))
 pprint.assign(pow_inplace, printing.OperatorPrinter("**=", 1, "right"))
```

### Comparing `pytensor-2.8.11/pytensor/tensor/math.py` & `pytensor-2.9.1/pytensor/tensor/math.py`

 * *Files 1% similar despite different names*

```diff
@@ -148,16 +148,16 @@
         inputs = [x]
         out_shape = tuple(
             1 if s == 1 else None
             for i, s in enumerate(x.type.shape)
             if i not in all_axes
         )
         outputs = [
-            tensor(x.type.dtype, shape=out_shape, name="max"),
-            tensor("int64", shape=out_shape, name="argmax"),
+            tensor(dtype=x.type.dtype, shape=out_shape, name="max"),
+            tensor(dtype="int64", shape=out_shape, name="argmax"),
         ]
         return Apply(self, inputs, outputs)
 
     def perform(self, node, inp, outs, params):
         x = inp[0]
         axes = params
         max, max_idx = outs
@@ -366,15 +366,15 @@
         else:
             all_axes = self.axis
         inputs = [x]
 
         # We keep the original broadcastable flags for dimensions on which
         # we do not perform the argmax.
         out_shape = tuple(s for i, s in enumerate(x.type.shape) if i not in all_axes)
-        outputs = [tensor("int64", shape=out_shape, name="argmax")]
+        outputs = [tensor(dtype="int64", shape=out_shape, name="argmax")]
         return Apply(self, inputs, outputs)
 
     def prepare_node(self, node, storage_map, compute_map, impl):
         if len(node.inputs) == 2:
             raise ValueError(
                 "You are trying to compile a graph with an old Argmax node.  Either reoptimize your graph or rebuild it to get the new node format."
             )
@@ -1381,14 +1381,19 @@
 
 @scalar_elemwise
 def gammal(k, x):
     """Lower incomplete gamma function."""
 
 
 @scalar_elemwise
+def hyp2f1(a, b, c, z):
+    """Gaussian hypergeometric function."""
+
+
+@scalar_elemwise
 def j0(x):
     """Bessel function of the first kind of order 0."""
 
 
 @scalar_elemwise
 def j1(x):
     """Bessel function of the first kind of order 1."""
@@ -1412,15 +1417,15 @@
 @scalar_elemwise
 def iv(v, x):
     """Modified Bessel function of the first kind of order v (real)."""
 
 
 @scalar_elemwise
 def sigmoid(x):
-    """Logistic sigmoid function (1 / (1 + exp(x)), also known as expit or inverse logit"""
+    """Logistic sigmoid function (1 / (1 + exp(-x)), also known as expit or inverse logit"""
 
 
 expit = sigmoid
 
 
 @scalar_elemwise
 def softplus(x):
@@ -1438,26 +1443,26 @@
 @scalar_elemwise
 def betainc(a, b, x):
     """Regularized incomplete beta function"""
 
 
 @scalar_elemwise
 def real(z):
-    """Return real component of complex-valued tensor `z`"""
+    """Return real component of complex-valued tensor `z`."""
 
 
-_tensor_py_operators.real = property(real)
+_tensor_py_operators.real = property(real, doc=real.__doc__)
 
 
 @scalar_elemwise
 def imag(z):
-    """Return imaginary component of complex-valued tensor `z`"""
+    """Return imaginary component of complex-valued tensor `z`."""
 
 
-_tensor_py_operators.imag = property(imag)
+_tensor_py_operators.imag = property(imag, doc=imag.__doc__)
 
 
 @scalar_elemwise
 def angle(z):
     """Return polar-coordinate angle of complex-valued tensor `z`"""
 
 
@@ -1918,15 +1923,15 @@
         sx, sy = (input.type.shape for input in inputs)
         if len(sy) == 2:
             sz = sx[:-1] + sy[-1:]
         elif len(sy) == 1:
             sz = sx[:-1]
 
         i_dtypes = [input.type.dtype for input in inputs]
-        outputs = [tensor(aes.upcast(*i_dtypes), shape=sz)]
+        outputs = [tensor(dtype=aes.upcast(*i_dtypes), shape=sz)]
         return Apply(self, inputs, outputs)
 
     def perform(self, node, inp, out):
         x, y = inp
         (z,) = out
 
         # the asarray is here because dot between two vectors
@@ -3128,33 +3133,9 @@
     "outer",
     "any",
     "all",
     "ptp",
     "power",
     "logaddexp",
     "logsumexp",
+    "hyp2f1",
 ]
-
-DEPRECATED_NAMES = [
-    ("abs_", "`abs_` is deprecated; use `abs` instead.", abs),
-    ("inv", "`inv` is deprecated; use `reciprocal` instead.", reciprocal),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
-
-
-def __dir__():
-    return sorted(__all__ + [names[0] for names in DEPRECATED_NAMES])
```

### Comparing `pytensor-2.8.11/pytensor/tensor/nlinalg.py` & `pytensor-2.9.1/pytensor/tensor/nlinalg.py`

 * *Files 3% similar despite different names*

```diff
@@ -227,14 +227,47 @@
     def __str__(self):
         return "Det"
 
 
 det = Det()
 
 
+class SLogDet(Op):
+    """
+    Compute the log determinant and its sign of the matrix. Input should be a square matrix.
+    """
+
+    __props__ = ()
+
+    def make_node(self, x):
+        x = as_tensor_variable(x)
+        assert x.ndim == 2
+        sign = scalar(dtype=x.dtype)
+        det = scalar(dtype=x.dtype)
+        return Apply(self, [x], [sign, det])
+
+    def perform(self, node, inputs, outputs):
+        (x,) = inputs
+        (sign, det) = outputs
+        try:
+            sign[0], det[0] = (z.astype(x.dtype) for z in np.linalg.slogdet(x))
+        except Exception:
+            print("Failed to compute determinant", x)
+            raise
+
+    def infer_shape(self, fgraph, node, shapes):
+        return [(), ()]
+
+    def __str__(self):
+        return "SLogDet"
+
+
+slogdet = SLogDet()
+
+
 class Eig(Op):
     """
     Compute the eigenvalues and right eigenvectors of a square array.
 
     """
 
     _numop = staticmethod(np.linalg.eig)
```

### Comparing `pytensor-2.8.11/pytensor/tensor/nnet/abstract_conv.py` & `pytensor-2.9.1/pytensor/tensor/conv/abstract_conv.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,22 +1,16 @@
 """
 Abstract conv interface
 """
 
 
 import logging
 import sys
-
-
-try:
-    from math import gcd
-except ImportError:
-    from fractions import gcd
-
 import warnings
+from math import gcd
 
 import numpy as np
 
 
 try:
     from scipy.signal.signaltools import _bvalfromboundary, _valfrommode, convolve
     from scipy.signal.sigtools import _convolve2d
@@ -31,16 +25,15 @@
 from pytensor.graph.op import Op
 from pytensor.raise_op import Assert
 from pytensor.tensor.basic import as_tensor_variable, get_scalar_constant_value
 from pytensor.tensor.exceptions import NotScalarConstantError
 from pytensor.tensor.var import TensorConstant, TensorVariable
 
 
-__docformat__ = "restructuredtext en"
-_logger = logging.getLogger("pytensor.tensor.nnet.abstract_conv")
+_logger = logging.getLogger(__name__)
 
 
 def get_conv_output_shape(
     image_shape, kernel_shape, border_mode, subsample, filter_dilation=None
 ):
     """
     This function compute the output shape of convolution operation.
@@ -674,15 +667,15 @@
     num_groups=1,
     unshared=False,
 ):
     """This function will build the symbolic graph for convolving a mini-batch of a
     stack of 2D inputs with a set of 2D filters. The implementation is modelled
     after Convolutional Neural Networks (CNN).
 
-    Refer to :func:`nnet.conv2d <pytensor.tensor.nnet.conv2d>` for a more detailed documentation.
+    Refer to :func:`nnet.conv2d <pytensor.tensor.conv.conv2d>` for a more detailed documentation.
     """
 
     input = as_tensor_variable(input)
     filters = as_tensor_variable(filters)
     conv_op = AbstractConv2d(
         imshp=input_shape,
         kshp=filter_shape,
@@ -2426,15 +2419,15 @@
         else:
             raise ValueError(f"unshared2d: invalid value '{direction}' for 'direction'")
         return out
 
 
 class AbstractConv(BaseAbstractConv):
     """Abstract Op for the forward convolution.
-    Refer to :func:`BaseAbstractConv <pytensor.tensor.nnet.abstract_conv.BaseAbstractConv>`
+    Refer to :func:`BaseAbstractConv <pytensor.tensor.conv.abstract_conv.BaseAbstractConv>`
     for a more detailed documentation.
     """
 
     def __init__(
         self,
         convdim,
         imshp=None,
@@ -2642,15 +2635,15 @@
             imshp, kshp, self.border_mode, self.subsample, self.filter_dilation
         )
         return [res]
 
 
 class AbstractConv2d(AbstractConv):
     """Abstract Op for the forward convolution.
-    Refer to :func:`BaseAbstractConv <pytensor.tensor.nnet.abstract_conv.BaseAbstractConv>`
+    Refer to :func:`BaseAbstractConv <pytensor.tensor.conv.abstract_conv.BaseAbstractConv>`
     for a more detailed documentation.
     """
 
     def __init__(
         self,
         imshp=None,
         kshp=None,
@@ -2704,15 +2697,15 @@
         d_bottom = bottom.type.filter_variable(d_bottom)
         d_weights = weights.type.filter_variable(d_weights)
         return d_bottom, d_weights
 
 
 class AbstractConv3d(AbstractConv):
     """Abstract Op for the forward convolution.
-    Refer to :func:`BaseAbstractConv <pytensor.tensor.nnet.abstract_conv.BaseAbstractConv>`
+    Refer to :func:`BaseAbstractConv <pytensor.tensor.conv.abstract_conv.BaseAbstractConv>`
     for a more detailed documentation.
     """
 
     def __init__(
         self,
         imshp=None,
         kshp=None,
@@ -3485,19 +3478,17 @@
     input,
     filters,
     input_shape=None,
     filter_shape=None,
     border_mode="valid",
     subsample=(1, 1),
     filter_flip=True,
-    image_shape=None,
     filter_dilation=(1, 1),
     num_groups=1,
     unshared=False,
-    **kwargs,
 ):
     """
     This function will build the symbolic graph for convolving a mini-batch of a
     stack of 2D inputs with a set of 2D filters. The implementation is modelled
     after Convolutional Neural Networks (CNN).
 
 
@@ -3580,44 +3571,14 @@
     Returns
     -------
     Symbolic 4D tensor
         Set of feature maps generated by convolutional layer. Tensor is
         of shape (batch size, output channels, output rows, output columns)
     """
 
-    if "imshp_logical" in kwargs or "kshp_logical" in kwargs:
-        raise ValueError(
-            "Keyword arguments 'imshp_logical' and 'kshp_logical' for conv2d "
-            "are not supported anymore (and have not been a reliable way to "
-            "perform upsampling). That feature is still available by calling "
-            "pytensor.tensor.nnet.conv.conv2d() for the time being."
-        )
-    if len(kwargs.keys()) > 0:
-        warnings.warn(
-            str(kwargs.keys()) + " are now deprecated in "
-            "`tensor.nnet.abstract_conv.conv2d` interface"
-            " and will be ignored.",
-            stacklevel=2,
-        )
-
-    if image_shape is not None:
-        warnings.warn(
-            "The `image_shape` keyword argument to "
-            "`tensor.nnet.conv2d` is deprecated, it has been "
-            "renamed to `input_shape`.",
-            stacklevel=2,
-        )
-        if input_shape is None:
-            input_shape = image_shape
-        else:
-            raise ValueError(
-                "input_shape and image_shape should not"
-                " be provided at the same time."
-            )
-
     return abstract_conv2d(
         input,
         filters,
         input_shape,
         filter_shape,
         border_mode,
         subsample,
```

### Comparing `pytensor-2.8.11/pytensor/tensor/nnet/c_code/corr3d_gemm.c` & `pytensor-2.9.1/tests/tensor/conv/c_code/corr3d_gemm.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/nnet/c_code/corr_gemm.c` & `pytensor-2.9.1/tests/tensor/conv/c_code/corr_gemm.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/basic.py` & `pytensor-2.9.1/pytensor/tensor/random/basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/op.py` & `pytensor-2.9.1/pytensor/tensor/random/op.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/rewriting/basic.py` & `pytensor-2.9.1/pytensor/tensor/random/rewriting/basic.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/rewriting/jax.py` & `pytensor-2.9.1/pytensor/tensor/random/rewriting/jax.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/type.py` & `pytensor-2.9.1/pytensor/tensor/random/type.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/random/var.py` & `pytensor-2.9.1/pytensor/tensor/random/var.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/basic.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/basic.py`

 * *Files 1% similar despite different names*

```diff
@@ -1263,39 +1263,8 @@
         return_values=ret_val,
         return_indices=ret_idx,
     )(x, k)
     copy_stack_trace(node.outputs[0], new_output)
     return {old_output: new_output}
 
 
-def import_ShapeFeature():
-    from pytensor.tensor.rewriting.shape import ShapeFeature
-
-    return ShapeFeature
-
-
-DEPRECATED_NAMES = {
-    "ShapeFeature": (
-        "`ShapeFeature` is now located in `pytensor.tensor.rewriting.shape`.",
-        import_ShapeFeature,
-    ),
-}
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    res = DEPRECATED_NAMES.get(name)
-    if res:
-        msg, fn = res
-        warn(msg, DeprecationWarning, stacklevel=2)
-        return fn()
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
-
-
 register_canonicalize(RemovalNodeRewriter(tensor_copy), name="remove_tensor_copy")
```

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/elemwise.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/elemwise.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/extra_ops.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/extra_ops.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/math.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/math.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-r"""Rewrites for the `Op`\s in `pytensor.tensor.math`."""
+r"""Rewrites for the `Op`\s in :mod:`pytensor.tensor.math`."""
 
 import itertools
 import operator
 from functools import partial, reduce
 
 import numpy as np
```

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/shape.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/shape.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/special.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/special.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/subtensor.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/subtensor.py`

 * *Files 0% similar despite different names*

```diff
@@ -1190,15 +1190,14 @@
                 # correspond to an error in the original add operation.
                 copy_stack_trace(node.outputs[0], new_add)
 
             # stack up the new incsubtensors
             tip = new_add
             for mi in movable_inputs:
                 assert o_type.is_super(tip.type)
-                assert mi.owner.inputs[0].type.is_super(tip.type)
                 tip = mi.owner.op(tip, *mi.owner.inputs[1:])
                 # Copy over stacktrace from outputs of the original
                 # "movable" operation to the new operation.
                 copy_stack_trace(node.outputs + mi.owner.outputs, tip)
 
             return [tip]
```

### Comparing `pytensor-2.8.11/pytensor/tensor/rewriting/uncanonicalize.py` & `pytensor-2.9.1/pytensor/tensor/rewriting/uncanonicalize.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/shape.py` & `pytensor-2.9.1/pytensor/tensor/shape.py`

 * *Files 0% similar despite different names*

```diff
@@ -637,15 +637,15 @@
                 try:
                     s_val = at.get_scalar_constant_value(y).item()
                     if s_val >= 0:
                         out_shape[index] = s_val
                 except NotScalarConstantError:
                     pass
 
-        return Apply(self, [x, shp], [tensor(x.type.dtype, shape=out_shape)])
+        return Apply(self, [x, shp], [tensor(dtype=x.type.dtype, shape=out_shape)])
 
     def perform(self, node, inp, out_, params):
         x, shp = inp
         (out,) = out_
         if len(shp) != self.ndim:
             raise ValueError(
                 "Shape argument to Reshape has incorrect"
```

### Comparing `pytensor-2.8.11/pytensor/tensor/sharedvar.py` & `pytensor-2.9.1/pytensor/tensor/sharedvar.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/slinalg.py` & `pytensor-2.9.1/pytensor/tensor/slinalg.py`

 * *Files 4% similar despite different names*

```diff
@@ -831,45 +831,7 @@
 __all__ = [
     "cholesky",
     "solve",
     "eigvalsh",
     "kron",
     "expm",
 ]
-
-DEPRECATED_NAMES = [
-    (
-        "solve_lower_triangular",
-        "`solve_lower_triangular` is deprecated; use `solve` instead.",
-        SolveTriangular(lower=True),
-    ),
-    (
-        "solve_upper_triangular",
-        "`solve_upper_triangular` is deprecated; use `solve` instead.",
-        SolveTriangular(lower=False),
-    ),
-    (
-        "solve_symmetric",
-        "`solve_symmetric` is deprecated; use `solve` instead.",
-        Solve(assume_a="sym"),
-    ),
-]
-
-
-def __getattr__(name):
-    """Intercept module-level attribute access of deprecated symbols.
-
-    Adapted from https://stackoverflow.com/a/55139609/3006474.
-
-    """
-    from warnings import warn
-
-    for old_name, msg, old_object in DEPRECATED_NAMES:
-        if name == old_name:
-            warn(msg, DeprecationWarning, stacklevel=2)
-            return old_object
-
-    raise AttributeError(f"module {__name__} has no attribute {name}")
-
-
-def __dir__():
-    return sorted(__all__ + [names[0] for names in DEPRECATED_NAMES])
```

### Comparing `pytensor-2.8.11/pytensor/tensor/sort.py` & `pytensor-2.9.1/pytensor/tensor/sort.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/special.py` & `pytensor-2.9.1/pytensor/tensor/special.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 import numpy as np
 import scipy
 
 from pytensor.graph.basic import Apply
 from pytensor.link.c.op import COp
 from pytensor.tensor.basic import as_tensor_variable
-from pytensor.tensor.math import neg, sum
+from pytensor.tensor.math import gamma, neg, sum
 
 
 class SoftmaxGrad(COp):
     """
     Gradient wrt x of the Softmax Op.
 
     """
@@ -764,11 +764,29 @@
         warnings.warn(
             "Softmax no longer converts a vector to a row matrix.",
             UserWarning,
         )
     return LogSoftmax(axis=axis)(c)
 
 
+def poch(z, m):
+    """
+    Pochhammer symbol (rising factorial) function.
+
+    """
+    return gamma(z + m) / gamma(z)
+
+
+def factorial(n):
+    """
+    Factorial function of a scalar or array of numbers.
+
+    """
+    return gamma(n + 1)
+
+
 __all__ = [
     "softmax",
     "log_softmax",
+    "poch",
+    "factorial",
 ]
```

### Comparing `pytensor-2.8.11/pytensor/tensor/subtensor.py` & `pytensor-2.9.1/pytensor/tensor/subtensor.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/type.py` & `pytensor-2.9.1/pytensor/tensor/type.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import logging
 import warnings
 from typing import TYPE_CHECKING, Iterable, Optional, Tuple, Union
 
 import numpy as np
+from typing_extensions import Literal
 
 import pytensor
 from pytensor import scalar as aes
 from pytensor.configdefaults import config
 from pytensor.graph.basic import Variable
 from pytensor.graph.type import HasDataType, HasShape
 from pytensor.graph.utils import MetaType
@@ -770,18 +771,40 @@
             %(fail)s;
         }
     }
     """,
     version=2,
 )
 
+# Valid static type entries
+ST = Union[int, None]
 
-def tensor(*args, **kwargs):
-    name = kwargs.pop("name", None)
-    return TensorType(*args, **kwargs)(name=name)
+
+def tensor(
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ...]] = None,
+    **kwargs,
+) -> "TensorVariable":
+
+    if name is not None:
+        # Help catching errors with the new tensor API
+        # Many single letter strings are valid sctypes
+        if str(name) == "floatX" or (len(str(name)) > 1 and np.obj2sctype(name)):
+            np.obj2sctype(name)
+            raise ValueError(
+                f"The first and only positional argument of tensor is now `name`. Got {name}.\n"
+                "This name looks like a dtype, which you should pass as a keyword argument only."
+            )
+
+    if dtype is None:
+        dtype = config.floatX
+
+    return TensorType(dtype=dtype, shape=shape, **kwargs)(name=name)
 
 
 cscalar = TensorType("complex64", ())
 zscalar = TensorType("complex128", ())
 fscalar = TensorType("float32", ())
 dscalar = TensorType("float64", ())
 bscalar = TensorType("int8", ())
@@ -790,15 +813,19 @@
 lscalar = TensorType("int64", ())
 ubscalar = TensorType("uint8", ())
 uwscalar = TensorType("uint16", ())
 uiscalar = TensorType("uint32", ())
 ulscalar = TensorType("uint64", ())
 
 
-def scalar(name=None, dtype=None):
+def scalar(
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+) -> "TensorVariable":
     """Return a symbolic scalar variable.
 
     Parameters
     ----------
     dtype: numeric
         None means to use pytensor.config.floatX.
     name
@@ -828,28 +855,53 @@
 dvector = TensorType("float64", shape=(None,))
 bvector = TensorType("int8", shape=(None,))
 wvector = TensorType("int16", shape=(None,))
 ivector = TensorType("int32", shape=(None,))
 lvector = TensorType("int64", shape=(None,))
 
 
-def vector(name=None, dtype=None):
+def _validate_static_shape(shape, ndim: int) -> Tuple[ST, ...]:
+
+    if not isinstance(shape, tuple):
+        raise TypeError(f"Shape must be a tuple, got {type(shape)}")
+
+    if len(shape) != ndim:
+        raise ValueError(f"Shape must be a tuple of length {ndim}, got {shape}")
+
+    if not all(sh is None or isinstance(sh, int) for sh in shape):
+        raise TypeError(f"Shape entries must be None or integer, got {shape}")
+
+    return shape
+
+
+def vector(
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST]] = (None,),
+) -> "TensorVariable":
     """Return a symbolic vector variable.
 
     Parameters
     ----------
-    dtype: numeric
-        None means to use pytensor.config.floatX.
     name
         A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
+    dtype
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None,))
+
+    shape = _validate_static_shape(shape, ndim=1)
+
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 vectors, fvectors, dvectors, ivectors, lvectors = apply_across_args(
     vector, fvector, dvector, ivector, lvector
 )
 
@@ -863,28 +915,37 @@
 dmatrix = TensorType("float64", shape=(None, None))
 bmatrix = TensorType("int8", shape=(None, None))
 wmatrix = TensorType("int16", shape=(None, None))
 imatrix = TensorType("int32", shape=(None, None))
 lmatrix = TensorType("int64", shape=(None, None))
 
 
-def matrix(name=None, dtype=None):
+def matrix(
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST]] = (None, None),
+) -> "TensorVariable":
     """Return a symbolic matrix variable.
 
     Parameters
     ----------
-    dtype: numeric
-        None means to use pytensor.config.floatX.
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
+    dtype
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None, None))
+    shape = _validate_static_shape(shape, ndim=2)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 matrices, fmatrices, dmatrices, imatrices, lmatrices = apply_across_args(
     matrix, fmatrix, dmatrix, imatrix, lmatrix
 )
 
@@ -898,28 +959,43 @@
 drow = TensorType("float64", shape=(1, None))
 brow = TensorType("int8", shape=(1, None))
 wrow = TensorType("int16", shape=(1, None))
 irow = TensorType("int32", shape=(1, None))
 lrow = TensorType("int64", shape=(1, None))
 
 
-def row(name=None, dtype=None):
+def row(
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[Literal[1], ST]] = (1, None),
+) -> "TensorVariable":
     """Return a symbolic row variable (i.e. shape ``(1, None)``).
 
     Parameters
     ----------
-    dtype: numeric type
-        None means to use pytensor.config.floatX.
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
+    dtype
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(1, None))
+    shape = _validate_static_shape(shape, ndim=2)
+
+    if shape[0] != 1:
+        raise ValueError(
+            f"The first dimension of a `row` must have shape 1, got {shape[0]}"
+        )
+
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 rows, frows, drows, irows, lrows = apply_across_args(row, frow, drow, irow, lrow)
 
 ccol = TensorType("complex64", shape=(None, 1))
 zcol = TensorType("complex128", shape=(None, 1))
@@ -928,29 +1004,40 @@
 bcol = TensorType("int8", shape=(None, 1))
 wcol = TensorType("int16", shape=(None, 1))
 icol = TensorType("int32", shape=(None, 1))
 lcol = TensorType("int64", shape=(None, 1))
 
 
 def col(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, Literal[1]]] = (None, 1),
 ) -> "TensorVariable":
     """Return a symbolic column variable (i.e. shape ``(None, 1)``).
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None, 1))
+    shape = _validate_static_shape(shape, ndim=2)
+    if shape[1] != 1:
+        raise ValueError(
+            f"The second dimension of a `col` must have shape 1, got {shape[1]}"
+        )
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 cols, fcols, dcols, icols, lcols = apply_across_args(col, fcol, dcol, icol, lcol)
 
 ctensor3 = TensorType("complex64", shape=((None,) * 3))
 ztensor3 = TensorType("complex128", shape=((None,) * 3))
@@ -959,29 +1046,36 @@
 btensor3 = TensorType("int8", shape=((None,) * 3))
 wtensor3 = TensorType("int16", shape=((None,) * 3))
 itensor3 = TensorType("int32", shape=((None,) * 3))
 ltensor3 = TensorType("int64", shape=((None,) * 3))
 
 
 def tensor3(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST, ST]] = (None, None, None),
 ) -> "TensorVariable":
     """Return a symbolic 3D variable.
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None, None, None))
+    shape = _validate_static_shape(shape, ndim=3)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 tensor3s, ftensor3s, dtensor3s, itensor3s, ltensor3s = apply_across_args(
     tensor3, ftensor3, dtensor3, itensor3, ltensor3
 )
 
@@ -992,29 +1086,36 @@
 btensor4 = TensorType("int8", shape=((None,) * 4))
 wtensor4 = TensorType("int16", shape=((None,) * 4))
 itensor4 = TensorType("int32", shape=((None,) * 4))
 ltensor4 = TensorType("int64", shape=((None,) * 4))
 
 
 def tensor4(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST, ST, ST]] = (None, None, None, None),
 ) -> "TensorVariable":
     """Return a symbolic 4D variable.
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None, None, None, None))
+    shape = _validate_static_shape(shape, ndim=4)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 tensor4s, ftensor4s, dtensor4s, itensor4s, ltensor4s = apply_across_args(
     tensor4, ftensor4, dtensor4, itensor4, ltensor4
 )
 
@@ -1025,29 +1126,36 @@
 btensor5 = TensorType("int8", shape=((None,) * 5))
 wtensor5 = TensorType("int16", shape=((None,) * 5))
 itensor5 = TensorType("int32", shape=((None,) * 5))
 ltensor5 = TensorType("int64", shape=((None,) * 5))
 
 
 def tensor5(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST, ST, ST, ST]] = (None, None, None, None, None),
 ) -> "TensorVariable":
     """Return a symbolic 5D variable.
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None, None, None, None, None))
+    shape = _validate_static_shape(shape, ndim=5)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 tensor5s, ftensor5s, dtensor5s, itensor5s, ltensor5s = apply_across_args(
     tensor5, ftensor5, dtensor5, itensor5, ltensor5
 )
 
@@ -1058,29 +1166,43 @@
 btensor6 = TensorType("int8", shape=((None,) * 6))
 wtensor6 = TensorType("int16", shape=((None,) * 6))
 itensor6 = TensorType("int32", shape=((None,) * 6))
 ltensor6 = TensorType("int64", shape=((None,) * 6))
 
 
 def tensor6(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST, ST, ST, ST, ST]] = (
+        None,
+        None,
+        None,
+        None,
+        None,
+        None,
+    ),
 ) -> "TensorVariable":
     """Return a symbolic 6D variable.
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None,) * 6)
+    shape = _validate_static_shape(shape, ndim=6)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 tensor6s, ftensor6s, dtensor6s, itensor6s, ltensor6s = apply_across_args(
     tensor6, ftensor6, dtensor6, itensor6, ltensor6
 )
 
@@ -1091,29 +1213,44 @@
 btensor7 = TensorType("int8", shape=((None,) * 7))
 wtensor7 = TensorType("int16", shape=((None,) * 7))
 itensor7 = TensorType("int32", shape=((None,) * 7))
 ltensor7 = TensorType("int64", shape=((None,) * 7))
 
 
 def tensor7(
-    name: Optional[str] = None, dtype: Optional["DTypeLike"] = None
+    name: Optional[str] = None,
+    *,
+    dtype: Optional["DTypeLike"] = None,
+    shape: Optional[Tuple[ST, ST, ST, ST, ST, ST, ST]] = (
+        None,
+        None,
+        None,
+        None,
+        None,
+        None,
+        None,
+    ),
 ) -> "TensorVariable":
     """Return a symbolic 7-D variable.
 
     Parameters
     ----------
     name
-        A name to attach to this variable.
+        A name to attach to this variable
+    shape
+        A tuple of static sizes for each dimension of the variable. By default, each dimension length is `None` which
+        allows that dimension to change size across evaluations.
     dtype
-        ``None`` means to use `pytensor.config.floatX`.
+        Data type of tensor variable. By default, it's pytensor.config.floatX.
 
     """
     if dtype is None:
         dtype = config.floatX
-    type = TensorType(dtype, shape=(None,) * 7)
+    shape = _validate_static_shape(shape, ndim=7)
+    type = TensorType(dtype, shape=shape)
     return type(name)
 
 
 tensor7s, ftensor7s, dtensor7s, itensor7s, ltensor7s = apply_across_args(
     tensor7, ftensor7, dtensor7, itensor7, ltensor7
 )
```

### Comparing `pytensor-2.8.11/pytensor/tensor/type_other.py` & `pytensor-2.9.1/pytensor/tensor/type_other.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/utils.py` & `pytensor-2.9.1/pytensor/tensor/utils.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/tensor/var.py` & `pytensor-2.9.1/pytensor/tensor/var.py`

 * *Files 1% similar despite different names*

```diff
@@ -650,21 +650,21 @@
         return at.math.dense_dot(left, right)
 
     dot = __dot__
     __matmul__ = __dot__
     __rmatmul__ = __rdot__
 
     def sum(self, axis=None, dtype=None, keepdims=False, acc_dtype=None):
-        """See `pytensor.tensor.math.sum`."""
+        """See :func:`pytensor.tensor.math.sum`."""
         return at.math.sum(
             self, axis=axis, dtype=dtype, keepdims=keepdims, acc_dtype=acc_dtype
         )
 
     def prod(self, axis=None, dtype=None, keepdims=False, acc_dtype=None):
-        """See `pytensor.tensor.math.prod`."""
+        """See :func:`pytensor.tensor.math.prod`."""
         return at.math.prod(
             self, axis=axis, dtype=dtype, keepdims=keepdims, acc_dtype=acc_dtype
         )
 
     def norm(self, L, axis=None, keepdims=False):
         if L == 0:
             raise NotImplementedError()
@@ -677,81 +677,81 @@
         )
         if keepdims:
             return at.math.makeKeepDims(self, y, axis)
         else:
             return y
 
     def mean(self, axis=None, dtype=None, keepdims=False, acc_dtype=None):
-        """See `pytensor.tensor.math.mean`."""
+        """See :func:`pytensor.tensor.math.mean`."""
         return at.math.mean(
             self, axis=axis, dtype=dtype, keepdims=keepdims, acc_dtype=acc_dtype
         )
 
     def var(self, axis=None, ddof=0, keepdims=False, corrected=False):
-        """See `pytensor.tensor.math.var`."""
+        """See :func:`pytensor.tensor.math.var`."""
         return at.math.var(
             self, axis=axis, ddof=ddof, keepdims=keepdims, corrected=corrected
         )
 
     def std(self, axis=None, ddof=0, keepdims=False, corrected=False):
-        """See `pytensor.tensor.math.std`."""
+        """See :func:`pytensor.tensor.math.std`."""
         return at.math.std(
             self, axis=axis, ddof=ddof, keepdims=keepdims, corrected=corrected
         )
 
     def min(self, axis=None, keepdims=False):
-        """See `pytensor.tensor.math.min`."""
+        """See :func:`pytensor.tensor.math.min`."""
         return at.math.min(self, axis, keepdims=keepdims)
 
     def max(self, axis=None, keepdims=False):
-        """See `pytensor.tensor.math.max`."""
+        """See :func:`pytensor.tensor.math.max`."""
         return at.math.max(self, axis, keepdims=keepdims)
 
     def argmin(self, axis=None, keepdims=False):
-        """See `pytensor.tensor.math.argmin`."""
+        """See :func:`pytensor.tensor.math.argmin`."""
         return at.math.argmin(self, axis, keepdims=keepdims)
 
     def argmax(self, axis=None, keepdims=False):
-        """See `pytensor.tensor.math.argmax`."""
+        """See :func:`pytensor.tensor.math.argmax`."""
         return at.math.argmax(self, axis, keepdims=keepdims)
 
     def nonzero(self, return_matrix=False):
-        """See `pytensor.tensor.basic.nonzero`."""
+        """See :func:`pytensor.tensor.basic.nonzero`."""
         return at.nonzero(self, return_matrix=return_matrix)
 
     def nonzero_values(self):
-        """See `pytensor.tensor.basic.nonzero_values`."""
+        """See :func:`pytensor.tensor.basic.nonzero_values`."""
         return at.nonzero_values(self)
 
     def sort(self, axis=-1, kind="quicksort", order=None):
-        """See `pytensor.tensor.sort.sort`."""
+        """See :func:`pytensor.tensor.sort.sort`."""
         return at.sort(self, axis, kind, order)
 
     def argsort(self, axis=-1, kind="quicksort", order=None):
-        """See `pytensor.tensor.sort.argsort`."""
+        """See :func:`pytensor.tensor.sort.argsort`."""
         from pytensor.tensor.sort import argsort
 
         return argsort(self, axis, kind, order)
 
     def clip(self, a_min, a_max):
-        "See `pytensor.tensor.math.clip`."
+        "See :func:`pytensor.tensor.math.clip`."
         return at.math.clip(self, a_min, a_max)
 
     def conj(self):
-        """See `pytensor.tensor.math.conj`."""
+        """See :func:`pytensor.tensor.math.conj`."""
         return at.math.conj(self)
 
     conjugate = conj
 
     def repeat(self, repeats, axis=None):
-        """See `pytensor.tensor.basic.repeat`."""
+        """See :func:`pytensor.tensor.basic.repeat`."""
         return at.extra_ops.repeat(self, repeats, axis)
 
     def round(self, mode=None):
-        """See `pytensor.tensor.math.round`."""
+        """See :func:`pytensor.tensor.math.round`."""
         return at.math.round(self, mode)
 
     def trace(self):
         return at.linalg.trace(self)
 
     # This value is set so that PyTensor arrays will trump NumPy operators.
     __array_priority__ = 1000
@@ -771,20 +771,20 @@
     def cumprod(self, axis=None):
         return at.extra_ops.cumprod(self, axis)
 
     def searchsorted(self, v, side="left", sorter=None):
         return at.extra_ops.searchsorted(self, v, side, sorter)
 
     def ptp(self, axis=None):
-        """See `pytensor.tensor.math.ptp`."""
+        """See :func:`pytensor.tensor.math.ptp`."""
 
         return at.math.ptp(self, axis)
 
     def swapaxes(self, axis1, axis2):
-        """See `pytensor.tensor.basic.swapaxes`.
+        """See :func:`pytensor.tensor.basic.swapaxes`.
 
         If a matrix is provided with the right axes, its transpose
         will be returned.
 
         """
         return at.basic.swapaxes(self, axis1, axis2)
```

### Comparing `pytensor-2.8.11/pytensor/tensor/xlogx.py` & `pytensor-2.9.1/pytensor/tensor/xlogx.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/typed_list/basic.py` & `pytensor-2.9.1/pytensor/typed_list/basic.py`

 * *Files 5% similar despite different names*

```diff
@@ -162,16 +162,16 @@
         # need to copy toAppend due to destroy_handler limitation
         toAppend = _lessbroken_deepcopy(toAppend)
         out[0].append(toAppend)
 
     def __str__(self):
         return self.__class__.__name__
 
-    # DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend().
-    def _c_code_(self, node, name, inp, out, sub):
+    def c_code(self, node, name, inp, out, sub):
+        raise NotImplementedError("DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend()")
         x_name, toAppend = inp[0], inp[1]
         output_name = out[0]
         fail = sub["fail"]
         if not self.inplace:
             init = (
                 """
             %(output_name)s = (PyListObject*) PyList_GetSlice((PyObject*) %(x_name)s, 0, PyList_GET_SIZE((PyObject*) %(x_name)s)) ;
@@ -247,16 +247,16 @@
             o = out[0]
             for i in toAppend:
                 o.append(_lessbroken_deepcopy(i))
 
     def __str__(self):
         return self.__class__.__name__
 
-    # DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend().
-    def _c_code_(self, node, name, inp, out, sub):
+    def c_code(self, node, name, inp, out, sub):
+        raise NotImplementedError("DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend()")
         x_name, toAppend = inp[0], inp[1]
         output_name = out[0]
         fail = sub["fail"]
         if not self.inplace:
             init = (
                 """
             %(output_name)s = (PyListObject*) PyList_GetSlice((PyObject*) %(x_name)s, 0, PyList_GET_SIZE((PyObject*) %(x_name)s)) ;
@@ -339,16 +339,16 @@
         # need to copy toAppend due to destroy_handler limitation
         toInsert = _lessbroken_deepcopy(toInsert)
         out[0].insert(index, toInsert)
 
     def __str__(self):
         return self.__class__.__name__
 
-    # DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend().
-    def _c_code_(self, node, name, inp, out, sub):
+    def c_code(self, node, name, inp, out, sub):
+        raise NotImplementedError("DISABLED AS WE NEED TO UPDATE IT TO COPY toAppend()")
         x_name, index, toInsert = inp[0], inp[1], inp[2]
         output_name = out[0]
         fail = sub["fail"]
         if not self.inplace:
             init = (
                 """
             %(output_name)s = (PyListObject*) PyList_GetSlice((PyObject*) %(x_name)s, 0, PyList_GET_SIZE((PyObject*) %(x_name)s)) ;
```

### Comparing `pytensor-2.8.11/pytensor/typed_list/rewriting.py` & `pytensor-2.9.1/pytensor/typed_list/rewriting.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/typed_list/type.py` & `pytensor-2.9.1/pytensor/typed_list/type.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/updates.py` & `pytensor-2.9.1/pytensor/updates.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor/utils.py` & `pytensor-2.9.1/pytensor/utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,30 +1,25 @@
 """Utility functions that only depend on the standard library."""
 
 import hashlib
-import inspect
 import logging
 import os
 import struct
 import subprocess
 import sys
-import traceback
-import warnings
 from collections import OrderedDict
 from collections.abc import Callable
-from functools import partial, wraps
+from functools import partial
 from typing import List, Set
 
 
 __all__ = [
-    "cmp",
     "get_unbound_function",
     "maybe_add_to_os_environ_pathlist",
     "DefaultOrderedDict",
-    "deprecated",
     "subprocess_Popen",
     "call_subprocess_Popen",
     "output_subprocess_Popen",
     "LOCAL_BITWIDTH",
     "PYTHON_INT_BITWIDTH",
     "NoDuplicateOptWarningFilter",
 ]
@@ -102,19 +97,14 @@
     """
     msg = e.args[0]
     if isinstance(msg, Exception):
         return exc_message(msg)
     return msg
 
 
-def cmp(x, y):
-    """Return -1 if x < y, 0 if x == y, 1 if x > y."""
-    return (x > y) - (x < y)
-
-
 def get_unbound_function(unbound):
     # Op.make_thunk isn't bound, so don't have a __func__ attr.
     # But bound method, have a __func__ method that point to the
     # not bound method. That is what we want.
     if hasattr(unbound, "__func__"):
         return unbound.__func__
     return unbound
@@ -142,52 +132,14 @@
             if newpath not in oldpaths:
                 newpaths = os.pathsep.join([newpath] + oldpaths)
                 os.environ[var] = newpaths
         except Exception:
             pass
 
 
-def deprecated(message: str = ""):
-    """
-    This is a decorator which can be used to mark functions
-    as deprecated. It will result in a warning being emitted
-    when the function is used first time and filter is set for show DeprecationWarning.
-
-    Taken from https://stackoverflow.com/a/40899499/4473230
-    """
-
-    def decorator_wrapper(func):
-        @wraps(func)
-        def function_wrapper(*args, **kwargs):
-            nonlocal message
-
-            current_call_source = "|".join(
-                traceback.format_stack(inspect.currentframe())
-            )
-            if current_call_source not in function_wrapper.last_call_source:
-
-                if not message:
-                    message = f"Function {func.__name__} is deprecated."
-
-                warnings.warn(
-                    message,
-                    category=DeprecationWarning,
-                    stacklevel=2,
-                )
-                function_wrapper.last_call_source.add(current_call_source)
-
-            return func(*args, **kwargs)
-
-        function_wrapper.last_call_source = set()
-
-        return function_wrapper
-
-    return decorator_wrapper
-
-
 def subprocess_Popen(command, **params):
     """
     Utility function to work around windows behavior that open windows.
 
     :see: call_subprocess_Popen and output_subprocess_Popen
     """
     startupinfo = None
```

### Comparing `pytensor-2.8.11/pytensor/version.py` & `pytensor-2.9.1/pytensor/version.py`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/pytensor.egg-info/SOURCES.txt` & `pytensor-2.9.1/pytensor.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,22 +1,21 @@
-DESCRIPTION.txt
 LICENSE.txt
 MANIFEST.in
 README.rst
-requirements-rtd.txt
-requirements.txt
+pyproject.toml
 setup.cfg
 setup.py
 versioneer.py
 bin/__init__.py
 bin/downstream_pr.sh
 bin/pytensor-cache
 bin/pytensor_cache.py
 bin/upstream_pr.sh
 doc/LICENSE.txt
+doc/README.md
 doc/acknowledgement.rst
 doc/bcast.png
 doc/bcast.svg
 doc/conf.py
 doc/core_development_guide.rst
 doc/css.inc
 doc/dev_start_guide.rst
@@ -54,18 +53,18 @@
 doc/extending/tips.rst
 doc/extending/type.rst
 doc/extending/unittest.rst
 doc/extending/using_params.rst
 doc/extending/pics/symbolic_graph_opt.png
 doc/extending/pics/symbolic_graph_unopt.png
 doc/images/Elman_srnn.png
+doc/images/PyTensor_RGB.svg
 doc/images/blocksparse.png
 doc/images/lstm.png
 doc/images/lstm_memorycell.png
-doc/images/pytensor_logo.svg
 doc/images/talk2010.gif
 doc/images/talk2010.png
 doc/internal/how_to_release.rst
 doc/internal/index.rst
 doc/internal/metadocumentation.rst
 doc/library/config.rst
 doc/library/gradient.rst
@@ -104,28 +103,27 @@
 doc/library/d3viz/index_files/index_24_0.png
 doc/library/d3viz/index_files/index_25_0.png
 doc/library/graph/features.rst
 doc/library/graph/fgraph.rst
 doc/library/graph/graph.rst
 doc/library/graph/index.rst
 doc/library/graph/op.rst
-doc/library/graph/params_type.rst
 doc/library/graph/type.rst
 doc/library/graph/utils.rst
 doc/library/misc/pkl_utils.rst
 doc/library/sandbox/index.rst
 doc/library/sandbox/linalg.rst
-doc/library/sandbox/rng_mrg.rst
 doc/library/scalar/index.rst
 doc/library/sparse/index.rst
 doc/library/sparse/sandbox.rst
 doc/library/tensor/basic.rst
 doc/library/tensor/basic_opt.rst
 doc/library/tensor/bcast.png
 doc/library/tensor/bcast.svg
+doc/library/tensor/conv.rst
 doc/library/tensor/elemwise.rst
 doc/library/tensor/extra_ops.rst
 doc/library/tensor/fft.rst
 doc/library/tensor/index.rst
 doc/library/tensor/io.rst
 doc/library/tensor/math_opt.rst
 doc/library/tensor/nlinalg.rst
@@ -186,15 +184,14 @@
 doc/tutorial/symbolic_graphs.rst
 doc/tutorial/pics/d3viz.png
 doc/tutorial/pics/logreg_pydotprint_predict.png
 doc/tutorial/pics/logreg_pydotprint_prediction.png
 doc/tutorial/pics/logreg_pydotprint_train.png
 pytensor/__init__.py
 pytensor/_version.py
-pytensor/assert_op.py
 pytensor/breakpoint.py
 pytensor/configdefaults.py
 pytensor/configparser.py
 pytensor/gradient.py
 pytensor/ifelse.py
 pytensor/printing.py
 pytensor/py.typed
@@ -234,25 +231,18 @@
 pytensor/d3viz/js/dagre-d3.min.js
 pytensor/d3viz/js/graphlib-dot.min.js
 pytensor/graph/__init__.py
 pytensor/graph/basic.py
 pytensor/graph/destroyhandler.py
 pytensor/graph/features.py
 pytensor/graph/fg.py
-pytensor/graph/kanren.py
 pytensor/graph/null_type.py
 pytensor/graph/op.py
-pytensor/graph/opt.py
-pytensor/graph/opt_utils.py
-pytensor/graph/optdb.py
 pytensor/graph/replace.py
-pytensor/graph/sched.py
-pytensor/graph/toolbox.py
 pytensor/graph/type.py
-pytensor/graph/unify.py
 pytensor/graph/utils.py
 pytensor/graph/rewriting/__init__.py
 pytensor/graph/rewriting/basic.py
 pytensor/graph/rewriting/db.py
 pytensor/graph/rewriting/kanren.py
 pytensor/graph/rewriting/unify.py
 pytensor/graph/rewriting/utils.py
@@ -270,16 +260,14 @@
 pytensor/link/c/lazylinker_c.py
 pytensor/link/c/op.py
 pytensor/link/c/params_type.py
 pytensor/link/c/type.py
 pytensor/link/c/c_code/lazylinker_c.c
 pytensor/link/c/c_code/pytensor_mod_helper.h
 pytensor/link/jax/__init__.py
-pytensor/link/jax/jax_dispatch.py
-pytensor/link/jax/jax_linker.py
 pytensor/link/jax/linker.py
 pytensor/link/jax/dispatch/__init__.py
 pytensor/link/jax/dispatch/basic.py
 pytensor/link/jax/dispatch/elemwise.py
 pytensor/link/jax/dispatch/extra_ops.py
 pytensor/link/jax/dispatch/nlinalg.py
 pytensor/link/jax/dispatch/random.py
@@ -292,127 +280,98 @@
 pytensor/link/jax/dispatch/test_subtensor.py
 pytensor/link/numba/__init__.py
 pytensor/link/numba/linker.py
 pytensor/link/numba/dispatch/__init__.py
 pytensor/link/numba/dispatch/basic.py
 pytensor/link/numba/dispatch/cython_support.py
 pytensor/link/numba/dispatch/elemwise.py
+pytensor/link/numba/dispatch/elemwise_codegen.py
 pytensor/link/numba/dispatch/extra_ops.py
 pytensor/link/numba/dispatch/nlinalg.py
 pytensor/link/numba/dispatch/random.py
 pytensor/link/numba/dispatch/scalar.py
 pytensor/link/numba/dispatch/scan.py
 pytensor/link/numba/dispatch/sparse.py
 pytensor/link/numba/dispatch/tensor_basic.py
 pytensor/misc/__init__.py
 pytensor/misc/check_blas.py
 pytensor/misc/check_blas_many.sh
 pytensor/misc/check_duplicate_key.py
 pytensor/misc/elemwise_openmp_speedup.py
 pytensor/misc/elemwise_time_test.py
 pytensor/misc/frozendict.py
-pytensor/misc/latence_gpu_transfert.py
 pytensor/misc/may_share_memory.py
 pytensor/misc/ordered_set.py
 pytensor/misc/pkl_utils.py
 pytensor/misc/safe_asarray.py
 pytensor/sandbox/__init__.py
-pytensor/sandbox/fourier.py
 pytensor/sandbox/minimal.py
-pytensor/sandbox/multinomial.py
-pytensor/sandbox/rng_mrg.py
-pytensor/sandbox/samples_MRG31k3p_12_7_5.txt
-pytensor/sandbox/solve.py
 pytensor/sandbox/linalg/__init__.py
 pytensor/sandbox/linalg/ops.py
 pytensor/scalar/__init__.py
 pytensor/scalar/basic.py
-pytensor/scalar/basic_scipy.py
-pytensor/scalar/basic_sympy.py
 pytensor/scalar/math.py
 pytensor/scalar/sharedvar.py
 pytensor/scalar/c_code/Faddeeva.cc
 pytensor/scalar/c_code/Faddeeva.hh
 pytensor/scalar/c_code/gamma.c
 pytensor/scan/__init__.py
 pytensor/scan/basic.py
 pytensor/scan/checkpoints.py
 pytensor/scan/op.py
-pytensor/scan/opt.py
 pytensor/scan/rewriting.py
+pytensor/scan/scan_perform.pyx
 pytensor/scan/scan_perform_ext.py
 pytensor/scan/utils.py
 pytensor/scan/views.py
-pytensor/scan/c_code/scan_perform.c
 pytensor/sparse/__init__.py
 pytensor/sparse/basic.py
-pytensor/sparse/opt.py
 pytensor/sparse/rewriting.py
 pytensor/sparse/sharedvar.py
 pytensor/sparse/type.py
 pytensor/sparse/utils.py
 pytensor/sparse/sandbox/__init__.py
 pytensor/sparse/sandbox/sp.py
 pytensor/sparse/sandbox/sp2.py
 pytensor/tensor/__init__.py
 pytensor/tensor/basic.py
-pytensor/tensor/basic_opt.py
 pytensor/tensor/blas.py
 pytensor/tensor/blas_c.py
 pytensor/tensor/blas_headers.py
 pytensor/tensor/blas_scipy.py
 pytensor/tensor/elemwise.py
 pytensor/tensor/elemwise_cgen.py
 pytensor/tensor/exceptions.py
 pytensor/tensor/extra_ops.py
 pytensor/tensor/fft.py
 pytensor/tensor/fourier.py
 pytensor/tensor/inplace.py
 pytensor/tensor/io.py
 pytensor/tensor/linalg.py
 pytensor/tensor/math.py
-pytensor/tensor/math_opt.py
 pytensor/tensor/nlinalg.py
-pytensor/tensor/opt_uncanonicalize.py
 pytensor/tensor/shape.py
 pytensor/tensor/sharedvar.py
 pytensor/tensor/slinalg.py
 pytensor/tensor/sort.py
 pytensor/tensor/special.py
 pytensor/tensor/subtensor.py
-pytensor/tensor/subtensor_opt.py
 pytensor/tensor/type.py
 pytensor/tensor/type_other.py
 pytensor/tensor/utils.py
 pytensor/tensor/var.py
 pytensor/tensor/xlogx.py
 pytensor/tensor/c_code/alt_blas_common.h
 pytensor/tensor/c_code/alt_blas_template.c
 pytensor/tensor/c_code/dimshuffle.c
-pytensor/tensor/nnet/__init__.py
-pytensor/tensor/nnet/abstract_conv.py
-pytensor/tensor/nnet/basic.py
-pytensor/tensor/nnet/batchnorm.py
-pytensor/tensor/nnet/blocksparse.py
-pytensor/tensor/nnet/conv.py
-pytensor/tensor/nnet/conv3d2d.py
-pytensor/tensor/nnet/corr.py
-pytensor/tensor/nnet/corr3d.py
-pytensor/tensor/nnet/ctc.py
-pytensor/tensor/nnet/neighbours.py
-pytensor/tensor/nnet/opt.py
-pytensor/tensor/nnet/rewriting.py
-pytensor/tensor/nnet/sigm.py
-pytensor/tensor/nnet/c_code/corr3d_gemm.c
-pytensor/tensor/nnet/c_code/corr_gemm.c
-pytensor/tensor/nnet/c_code/ctc_wrapper.c
+pytensor/tensor/conv/__init__.py
+pytensor/tensor/conv/abstract_conv.py
 pytensor/tensor/random/__init__.py
 pytensor/tensor/random/basic.py
 pytensor/tensor/random/op.py
-pytensor/tensor/random/opt.py
 pytensor/tensor/random/type.py
 pytensor/tensor/random/utils.py
 pytensor/tensor/random/var.py
 pytensor/tensor/random/rewriting/__init__.py
 pytensor/tensor/random/rewriting/basic.py
 pytensor/tensor/random/rewriting/jax.py
 pytensor/tensor/rewriting/__init__.py
@@ -420,16 +379,17 @@
 pytensor/tensor/rewriting/elemwise.py
 pytensor/tensor/rewriting/extra_ops.py
 pytensor/tensor/rewriting/math.py
 pytensor/tensor/rewriting/shape.py
 pytensor/tensor/rewriting/special.py
 pytensor/tensor/rewriting/subtensor.py
 pytensor/tensor/rewriting/uncanonicalize.py
-pytensor/tensor/signal/__init__.py
-pytensor/tensor/signal/conv.py
-pytensor/tensor/signal/pool.py
 pytensor/typed_list/__init__.py
 pytensor/typed_list/basic.py
 pytensor/typed_list/rewriting.py
 pytensor/typed_list/type.py
+scripts/mypy-failing.txt
+scripts/run_mypy.py
 tests/link/c/c_code/test_cenum.h
-tests/link/c/c_code/test_quadratic_function.c
+tests/link/c/c_code/test_quadratic_function.c
+tests/tensor/conv/c_code/corr3d_gemm.c
+tests/tensor/conv/c_code/corr_gemm.c
```

### Comparing `pytensor-2.8.11/setup.py` & `pytensor-2.9.1/setup.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 #!/usr/bin/env python
 import os
 
-from setuptools import setup
+import numpy
+from setuptools import Extension, setup
 from setuptools.dist import Distribution
 
 import versioneer
 
 
 dist = Distribution()
 dist.parse_config_files()
@@ -31,8 +32,15 @@
 
 
 if __name__ == "__main__":
     setup(
         name=NAME,
         version=versioneer.get_version(),
         cmdclass=versioneer.get_cmdclass(),
+        ext_modules=[
+            Extension(
+                name="pytensor.scan.scan_perform",
+                sources=["pytensor/scan/scan_perform.pyx"],
+                include_dirs=[numpy.get_include()],
+            ),
+        ],
     )
```

### Comparing `pytensor-2.8.11/tests/link/c/c_code/test_quadratic_function.c` & `pytensor-2.9.1/tests/link/c/c_code/test_quadratic_function.c`

 * *Files identical despite different names*

### Comparing `pytensor-2.8.11/versioneer.py` & `pytensor-2.9.1/versioneer.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,35 +1,64 @@
-# Version: 0.23.dev0
+
+# Version: 0.28
 
 """The Versioneer - like a rocketeer, but for versions.
 
 The Versioneer
 ==============
 
 * like a rocketeer, but for versions!
 * https://github.com/python-versioneer/python-versioneer
 * Brian Warner
-* License: Public Domain (CC0-1.0)
+* License: Public Domain (Unlicense)
 * Compatible with: Python 3.7, 3.8, 3.9, 3.10 and pypy3
 * [![Latest Version][pypi-image]][pypi-url]
 * [![Build Status][travis-image]][travis-url]
 
-This is a tool for managing a recorded version number in distutils/setuptools-based
+This is a tool for managing a recorded version number in setuptools-based
 python projects. The goal is to remove the tedious and error-prone "update
 the embedded version string" step from your release process. Making a new
 release should be as easy as recording a new tag in your version-control
 system, and maybe making new tarballs.
 
 
 ## Quick Install
 
+Versioneer provides two installation modes. The "classic" vendored mode installs
+a copy of versioneer into your repository. The experimental build-time dependency mode
+is intended to allow you to skip this step and simplify the process of upgrading.
+
+### Vendored mode
+
+* `pip install versioneer` to somewhere in your $PATH
+   * A [conda-forge recipe](https://github.com/conda-forge/versioneer-feedstock) is
+     available, so you can also use `conda install -c conda-forge versioneer`
+* add a `[tool.versioneer]` section to your `pyproject.toml` or a
+  `[versioneer]` section to your `setup.cfg` (see [Install](INSTALL.md))
+   * Note that you will need to add `tomli; python_version < "3.11"` to your
+     build-time dependencies if you use `pyproject.toml`
+* run `versioneer install --vendor` in your source tree, commit the results
+* verify version information with `python setup.py version`
+
+### Build-time dependency mode
+
 * `pip install versioneer` to somewhere in your $PATH
-* add a `[versioneer]` section to your setup.cfg (see [Install](INSTALL.md))
-* run `versioneer install` in your source tree, commit the results
-* Verify version information with `python setup.py version`
+   * A [conda-forge recipe](https://github.com/conda-forge/versioneer-feedstock) is
+     available, so you can also use `conda install -c conda-forge versioneer`
+* add a `[tool.versioneer]` section to your `pyproject.toml` or a
+  `[versioneer]` section to your `setup.cfg` (see [Install](INSTALL.md))
+* add `versioneer` (with `[toml]` extra, if configuring in `pyproject.toml`)
+  to the `requires` key of the `build-system` table in `pyproject.toml`:
+  ```toml
+  [build-system]
+  requires = ["setuptools", "versioneer[toml]"]
+  build-backend = "setuptools.build_meta"
+  ```
+* run `versioneer install --no-vendor` in your source tree, commit the results
+* verify version information with `python setup.py version`
 
 ## Version Identifiers
 
 Source trees come from a variety of places:
 
 * a version-control system checkout (mostly used by developers)
 * a nightly tarball, produced by build automation
@@ -226,17 +255,18 @@
 
 
 ## Updating Versioneer
 
 To upgrade your project to a new release of Versioneer, do the following:
 
 * install the new Versioneer (`pip install -U versioneer` or equivalent)
-* edit `setup.cfg`, if necessary, to include any new configuration settings
-  indicated by the release notes. See [UPGRADING](./UPGRADING.md) for details.
-* re-run `versioneer install` in your source tree, to replace
+* edit `setup.cfg` and `pyproject.toml`, if necessary,
+  to include any new configuration settings indicated by the release notes.
+  See [UPGRADING](./UPGRADING.md) for details.
+* re-run `versioneer install --[no-]vendor` in your source tree, to replace
   `SRC/_version.py`
 * commit any changed files
 
 ## Future Directions
 
 This tool is designed to make it easily extended to other version-control
 systems: all VCS-specific components are in separate directories like
@@ -258,17 +288,16 @@
 * [versioningit](https://github.com/jwodder/versioningit) - a PEP 518-based setuptools
   plugin
 
 ## License
 
 To make Versioneer easier to embed, all its code is dedicated to the public
 domain. The `_version.py` that it creates is also in the public domain.
-Specifically, both are released under the Creative Commons "Public Domain
-Dedication" license (CC0-1.0), as described in
-https://creativecommons.org/publicdomain/zero/1.0/ .
+Specifically, both are released under the "Unlicense", as described in
+https://unlicense.org/.
 
 [pypi-image]: https://img.shields.io/pypi/v/versioneer.svg
 [pypi-url]: https://pypi.python.org/pypi/versioneer/
 [travis-image]:
 https://img.shields.io/travis/com/python-versioneer/python-versioneer.svg
 [travis-url]: https://travis-ci.com/github/python-versioneer/python-versioneer
 
@@ -282,17 +311,27 @@
 import configparser
 import errno
 import json
 import os
 import re
 import subprocess
 import sys
+from pathlib import Path
 from typing import Callable, Dict
 import functools
 
+have_tomllib = True
+if sys.version_info >= (3, 11):
+    import tomllib
+else:
+    try:
+        import tomli as tomllib
+    except ImportError:
+        have_tomllib = False
+
 
 class VersioneerConfig:
     """Container for Versioneer configuration parameters."""
 
 
 def get_root():
     """Get the project root directory.
@@ -321,44 +360,54 @@
         # "versioneer" may be imported multiple times, and python's shared
         # module-import table will cache the first one. So we can't use
         # os.path.dirname(__file__), as that will find whichever
         # versioneer.py was first imported, even in later projects.
         my_path = os.path.realpath(os.path.abspath(__file__))
         me_dir = os.path.normcase(os.path.splitext(my_path)[0])
         vsr_dir = os.path.normcase(os.path.splitext(versioneer_py)[0])
-        if me_dir != vsr_dir:
+        if me_dir != vsr_dir and "VERSIONEER_PEP518" not in globals():
             print("Warning: build in %s is using versioneer.py from %s"
                   % (os.path.dirname(my_path), versioneer_py))
     except NameError:
         pass
     return root
 
 
 def get_config_from_root(root):
     """Read the project setup.cfg file to determine Versioneer config."""
     # This might raise OSError (if setup.cfg is missing), or
     # configparser.NoSectionError (if it lacks a [versioneer] section), or
     # configparser.NoOptionError (if it lacks "VCS="). See the docstring at
     # the top of versioneer.py for instructions on writing your setup.cfg .
-    setup_cfg = os.path.join(root, "setup.cfg")
-    parser = configparser.ConfigParser()
-    with open(setup_cfg) as cfg_file:
-        parser.read_file(cfg_file)
-    VCS = parser.get("versioneer", "VCS")  # mandatory
+    root = Path(root)
+    pyproject_toml = root / "pyproject.toml"
+    setup_cfg = root / "setup.cfg"
+    section = None
+    if pyproject_toml.exists() and have_tomllib:
+        try:
+            with open(pyproject_toml, 'rb') as fobj:
+                pp = tomllib.load(fobj)
+            section = pp['tool']['versioneer']
+        except (tomllib.TOMLDecodeError, KeyError):
+            pass
+    if not section:
+        parser = configparser.ConfigParser()
+        with open(setup_cfg) as cfg_file:
+            parser.read_file(cfg_file)
+        parser.get("versioneer", "VCS")  # raise error if missing
 
-    # Dict-like interface for non-mandatory entries
-    section = parser["versioneer"]
+        section = parser["versioneer"]
 
     cfg = VersioneerConfig()
-    cfg.VCS = VCS
+    cfg.VCS = section['VCS']
     cfg.style = section.get("style", "")
     cfg.versionfile_source = section.get("versionfile_source")
     cfg.versionfile_build = section.get("versionfile_build")
     cfg.tag_prefix = section.get("tag_prefix")
-    if cfg.tag_prefix in ("''", '""'):
+    if cfg.tag_prefix in ("''", '""', None):
         cfg.tag_prefix = ""
     cfg.parentdir_prefix = section.get("parentdir_prefix")
     cfg.verbose = section.get("verbose")
     return cfg
 
 
 class NotThisMethod(Exception):
@@ -407,15 +456,15 @@
                 continue
             if verbose:
                 print("unable to run %s" % dispcmd)
                 print(e)
             return None, None
     else:
         if verbose:
-            print(f"unable to find command, tried {commands}")
+            print("unable to find command, tried %s" % (commands,))
         return None, None
     stdout = process.communicate()[0].strip().decode()
     if process.returncode != 0:
         if verbose:
             print("unable to run %s (error)" % dispcmd)
             print("stdout was %s" % stdout)
         return None, process.returncode
@@ -425,16 +474,17 @@
 LONG_VERSION_PY['git'] = r'''
 # This file helps to compute a version number in source trees obtained from
 # git-archive tarball (such as those provided by githubs download-from-tag
 # feature). Distribution tarballs (built by setup.py sdist) and build
 # directories (produced by setup.py build) will contain a much shorter file
 # that just contains the computed version number.
 
-# This file is released into the public domain. Generated by
-# versioneer-0.23.dev0 (https://github.com/python-versioneer/python-versioneer)
+# This file is released into the public domain.
+# Generated by versioneer-0.28
+# https://github.com/python-versioneer/python-versioneer
 
 """Git implementation of _version.py."""
 
 import errno
 import os
 import re
 import subprocess
@@ -668,27 +718,26 @@
     # It may be intended to be passed to the Versioneer-versioned project,
     # but that should not change where we get our version from.
     env = os.environ.copy()
     env.pop("GIT_DIR", None)
     runner = functools.partial(runner, env=env)
 
     _, rc = runner(GITS, ["rev-parse", "--git-dir"], cwd=root,
-                   hide_stderr=True)
+                   hide_stderr=not verbose)
     if rc != 0:
         if verbose:
             print("Directory %%s not under git control" %% root)
         raise NotThisMethod("'git rev-parse --git-dir' returned error")
 
-    MATCH_ARGS = ["--match", "%%s*" %% tag_prefix] if tag_prefix else []
-
     # if there is a tag matching tag_prefix, this yields TAG-NUM-gHEX[-dirty]
     # if there isn't one, this yields HEX[-dirty] (no NUM)
-    describe_out, rc = runner(GITS, ["describe", "--tags", "--dirty",
-                                     "--always", "--long", *MATCH_ARGS],
-                              cwd=root)
+    describe_out, rc = runner(GITS, [
+        "describe", "--tags", "--dirty", "--always", "--long",
+        "--match", f"{tag_prefix}[[:digit:]]*"
+    ], cwd=root)
     # --long was added in git-1.5.5
     if describe_out is None:
         raise NotThisMethod("'git describe' failed")
     describe_out = describe_out.strip()
     full_out, rc = runner(GITS, ["rev-parse", "HEAD"], cwd=root)
     if full_out is None:
         raise NotThisMethod("'git rev-parse' failed")
@@ -769,16 +818,16 @@
 
         # commit: short hex revision ID
         pieces["short"] = mo.group(3)
 
     else:
         # HEX: no tags
         pieces["closest-tag"] = None
-        count_out, rc = runner(GITS, ["rev-list", "HEAD", "--count"], cwd=root)
-        pieces["distance"] = int(count_out)  # total number of commits
+        out, rc = runner(GITS, ["rev-list", "HEAD", "--left-right"], cwd=root)
+        pieces["distance"] = len(out.split())  # total number of commits
 
     # commit date: see ISO-8601 comment in git_versions_from_keywords()
     date = runner(GITS, ["show", "-s", "--format=%%ci", "HEAD"], cwd=root)[0].strip()
     # Use only the last line.  Previous lines may contain GPG signature
     # information.
     date = date.splitlines()[-1]
     pieces["date"] = date.strip().replace(" ", "T", 1).replace(" ", "", 1)
@@ -866,15 +915,15 @@
     """
     if pieces["closest-tag"]:
         if pieces["distance"]:
             # update the post release segment
             tag_version, post_version = pep440_split_post(pieces["closest-tag"])
             rendered = tag_version
             if post_version is not None:
-                rendered += ".post%%d.dev%%d" %% (post_version+1, pieces["distance"])
+                rendered += ".post%%d.dev%%d" %% (post_version + 1, pieces["distance"])
             else:
                 rendered += ".post0.dev%%d" %% (pieces["distance"])
         else:
             # no commits, use the tag as the version
             rendered = pieces["closest-tag"]
     else:
         # exception #1
@@ -1088,15 +1137,15 @@
     """Extract version information from the given file."""
     # the code embedded in _version.py can just fetch the value of these
     # keywords. When used from setup.py, we don't want to import _version.py,
     # so we do it with a regexp instead. This function is not used from
     # _version.py.
     keywords = {}
     try:
-        with open(versionfile_abs) as fobj:
+        with open(versionfile_abs, "r") as fobj:
             for line in fobj:
                 if line.strip().startswith("git_refnames ="):
                     mo = re.search(r'=\s*"(.*)"', line)
                     if mo:
                         keywords["refnames"] = mo.group(1)
                 if line.strip().startswith("git_full ="):
                     mo = re.search(r'=\s*"(.*)"', line)
@@ -1191,27 +1240,26 @@
     # It may be intended to be passed to the Versioneer-versioned project,
     # but that should not change where we get our version from.
     env = os.environ.copy()
     env.pop("GIT_DIR", None)
     runner = functools.partial(runner, env=env)
 
     _, rc = runner(GITS, ["rev-parse", "--git-dir"], cwd=root,
-                   hide_stderr=True)
+                   hide_stderr=not verbose)
     if rc != 0:
         if verbose:
             print("Directory %s not under git control" % root)
         raise NotThisMethod("'git rev-parse --git-dir' returned error")
 
-    MATCH_ARGS = ["--match", "%s*" % tag_prefix] if tag_prefix else []
-
     # if there is a tag matching tag_prefix, this yields TAG-NUM-gHEX[-dirty]
     # if there isn't one, this yields HEX[-dirty] (no NUM)
-    describe_out, rc = runner(GITS, ["describe", "--tags", "--dirty",
-                                     "--always", "--long", *MATCH_ARGS],
-                              cwd=root)
+    describe_out, rc = runner(GITS, [
+        "describe", "--tags", "--dirty", "--always", "--long",
+        "--match", f"{tag_prefix}[[:digit:]]*"
+    ], cwd=root)
     # --long was added in git-1.5.5
     if describe_out is None:
         raise NotThisMethod("'git describe' failed")
     describe_out = describe_out.strip()
     full_out, rc = runner(GITS, ["rev-parse", "HEAD"], cwd=root)
     if full_out is None:
         raise NotThisMethod("'git rev-parse' failed")
@@ -1292,50 +1340,51 @@
 
         # commit: short hex revision ID
         pieces["short"] = mo.group(3)
 
     else:
         # HEX: no tags
         pieces["closest-tag"] = None
-        count_out, rc = runner(GITS, ["rev-list", "HEAD", "--count"], cwd=root)
-        pieces["distance"] = int(count_out)  # total number of commits
+        out, rc = runner(GITS, ["rev-list", "HEAD", "--left-right"], cwd=root)
+        pieces["distance"] = len(out.split())  # total number of commits
 
     # commit date: see ISO-8601 comment in git_versions_from_keywords()
     date = runner(GITS, ["show", "-s", "--format=%ci", "HEAD"], cwd=root)[0].strip()
     # Use only the last line.  Previous lines may contain GPG signature
     # information.
     date = date.splitlines()[-1]
     pieces["date"] = date.strip().replace(" ", "T", 1).replace(" ", "", 1)
 
     return pieces
 
 
-def do_vcs_install(manifest_in, versionfile_source, ipy):
+def do_vcs_install(versionfile_source, ipy):
     """Git-specific installation logic for Versioneer.
 
     For Git, this means creating/changing .gitattributes to mark _version.py
     for export-subst keyword substitution.
     """
     GITS = ["git"]
     if sys.platform == "win32":
         GITS = ["git.cmd", "git.exe"]
-    files = [manifest_in, versionfile_source]
+    files = [versionfile_source]
     if ipy:
         files.append(ipy)
-    try:
-        my_path = __file__
-        if my_path.endswith(".pyc") or my_path.endswith(".pyo"):
-            my_path = os.path.splitext(my_path)[0] + ".py"
-        versioneer_file = os.path.relpath(my_path)
-    except NameError:
-        versioneer_file = "versioneer.py"
-    files.append(versioneer_file)
+    if "VERSIONEER_PEP518" not in globals():
+        try:
+            my_path = __file__
+            if my_path.endswith((".pyc", ".pyo")):
+                my_path = os.path.splitext(my_path)[0] + ".py"
+            versioneer_file = os.path.relpath(my_path)
+        except NameError:
+            versioneer_file = "versioneer.py"
+        files.append(versioneer_file)
     present = False
     try:
-        with open(".gitattributes") as fobj:
+        with open(".gitattributes", "r") as fobj:
             for line in fobj:
                 if line.strip().startswith(versionfile_source):
                     if "export-subst" in line.strip().split()[1:]:
                         present = True
                         break
     except OSError:
         pass
@@ -1367,15 +1416,15 @@
     if verbose:
         print("Tried directories %s but none started with prefix %s" %
               (str(rootdirs), parentdir_prefix))
     raise NotThisMethod("rootdir doesn't start with parentdir_prefix")
 
 
 SHORT_VERSION_PY = """
-# This file was generated by 'versioneer.py' (0.23.dev0) from
+# This file was generated by 'versioneer.py' (0.28) from
 # revision-control system data, or from the parent directory name of an
 # unpacked source archive. Distribution tarballs contain a pre-generated copy
 # of this file.
 
 import json
 
 version_json = '''
@@ -1409,15 +1458,15 @@
     """Write the given version number to the given _version.py file."""
     os.unlink(filename)
     contents = json.dumps(versions, sort_keys=True,
                           indent=1, separators=(",", ": "))
     with open(filename, "w") as f:
         f.write(SHORT_VERSION_PY % contents)
 
-    print("set {} to '{}'".format(filename, versions["version"]))
+    print("set %s to '%s'" % (filename, versions["version"]))
 
 
 def plus_or_dot(pieces):
     """Return a + if we don't already have one, else return a ."""
     if "+" in pieces.get("closest-tag", ""):
         return "."
     return "+"
@@ -1496,15 +1545,15 @@
     """
     if pieces["closest-tag"]:
         if pieces["distance"]:
             # update the post release segment
             tag_version, post_version = pep440_split_post(pieces["closest-tag"])
             rendered = tag_version
             if post_version is not None:
-                rendered += ".post%d.dev%d" % (post_version+1, pieces["distance"])
+                rendered += ".post%d.dev%d" % (post_version + 1, pieces["distance"])
             else:
                 rendered += ".post0.dev%d" % (pieces["distance"])
         else:
             # no commits, use the tag as the version
             rendered = pieces["closest-tag"]
     else:
         # exception #1
@@ -1709,15 +1758,15 @@
             return ver
         except NotThisMethod:
             pass
 
     try:
         ver = versions_from_file(versionfile_abs)
         if verbose:
-            print(f"got version from file {versionfile_abs} {ver}")
+            print("got version from file %s %s" % (versionfile_abs, ver))
         return ver
     except NotThisMethod:
         pass
 
     from_vcs_f = handlers.get("pieces_from_vcs")
     if from_vcs_f:
         try:
@@ -1809,26 +1858,33 @@
     #  setuptools/develop -> ?
     #  pip install:
     #   copies source tree to a tempdir before running egg_info/etc
     #   if .git isn't copied too, 'git describe' will fail
     #   then does setup.py bdist_wheel, or sometimes setup.py install
     #  setup.py egg_info -> ?
 
+    # pip install -e . and setuptool/editable_wheel will invoke build_py
+    # but the build_py command is not expected to copy any files.
+
     # we override different "build_py" commands for both environments
     if 'build_py' in cmds:
         _build_py = cmds['build_py']
     else:
         from setuptools.command.build_py import build_py as _build_py
 
     class cmd_build_py(_build_py):
         def run(self):
             root = get_root()
             cfg = get_config_from_root(root)
             versions = get_versions()
             _build_py.run(self)
+            if getattr(self, "editable_mode", False):
+                # During editable installs `.py` and data files are
+                # not copied to build_lib
+                return
             # now locate _version.py in the new build/ directory and replace
             # it with an updated value
             if cfg.versionfile_build:
                 target_versionfile = os.path.join(self.build_lib,
                                                   cfg.versionfile_build)
                 print("UPDATING %s" % target_versionfile)
                 write_to_version_file(target_versionfile, versions)
@@ -1849,14 +1905,16 @@
                 # build_ext --inplace will only build extensions in
                 # build/lib<..> dir with no _version.py to write to.
                 # As in place builds will already have a _version.py
                 # in the module dir, we do not need to write one.
                 return
             # now locate _version.py in the new build/ directory and replace
             # it with an updated value
+            if not cfg.versionfile_build:
+                return
             target_versionfile = os.path.join(self.build_lib,
                                               cfg.versionfile_build)
             if not os.path.exists(target_versionfile):
                 print(f"Warning: {target_versionfile} does not exist, skipping "
                       "version update. This can happen if you are running build_ext "
                       "without first running build_py.")
                 return
@@ -1893,15 +1951,18 @@
                              "PARENTDIR_PREFIX": cfg.parentdir_prefix,
                              "VERSIONFILE_SOURCE": cfg.versionfile_source,
                              })
         cmds["build_exe"] = cmd_build_exe
         del cmds["build_py"]
 
     if 'py2exe' in sys.modules:  # py2exe enabled?
-        from py2exe.distutils_buildexe import py2exe as _py2exe
+        try:
+            from py2exe.setuptools_buildexe import py2exe as _py2exe
+        except ImportError:
+            from py2exe.distutils_buildexe import py2exe as _py2exe
 
         class cmd_py2exe(_py2exe):
             def run(self):
                 root = get_root()
                 cfg = get_config_from_root(root)
                 versions = get_versions()
                 target_versionfile = cfg.versionfile_source
@@ -1917,14 +1978,51 @@
                              "STYLE": cfg.style,
                              "TAG_PREFIX": cfg.tag_prefix,
                              "PARENTDIR_PREFIX": cfg.parentdir_prefix,
                              "VERSIONFILE_SOURCE": cfg.versionfile_source,
                              })
         cmds["py2exe"] = cmd_py2exe
 
+    # sdist farms its file list building out to egg_info
+    if 'egg_info' in cmds:
+        _egg_info = cmds['egg_info']
+    else:
+        from setuptools.command.egg_info import egg_info as _egg_info
+
+    class cmd_egg_info(_egg_info):
+        def find_sources(self):
+            # egg_info.find_sources builds the manifest list and writes it
+            # in one shot
+            super().find_sources()
+
+            # Modify the filelist and normalize it
+            root = get_root()
+            cfg = get_config_from_root(root)
+            self.filelist.append('versioneer.py')
+            if cfg.versionfile_source:
+                # There are rare cases where versionfile_source might not be
+                # included by default, so we must be explicit
+                self.filelist.append(cfg.versionfile_source)
+            self.filelist.sort()
+            self.filelist.remove_duplicates()
+
+            # The write method is hidden in the manifest_maker instance that
+            # generated the filelist and was thrown away
+            # We will instead replicate their final normalization (to unicode,
+            # and POSIX-style paths)
+            from setuptools import unicode_utils
+            normalized = [unicode_utils.filesys_decode(f).replace(os.sep, '/')
+                          for f in self.filelist.files]
+
+            manifest_filename = os.path.join(self.egg_info, 'SOURCES.txt')
+            with open(manifest_filename, 'w') as fobj:
+                fobj.write('\n'.join(normalized))
+
+    cmds['egg_info'] = cmd_egg_info
+
     # we override different "sdist" commands for both environments
     if 'sdist' in cmds:
         _sdist = cmds['sdist']
     else:
         from setuptools.command.sdist import sdist as _sdist
 
     class cmd_sdist(_sdist):
@@ -2026,15 +2124,15 @@
                         "VERSIONFILE_SOURCE": cfg.versionfile_source,
                         })
 
     ipy = os.path.join(os.path.dirname(cfg.versionfile_source),
                        "__init__.py")
     if os.path.exists(ipy):
         try:
-            with open(ipy) as f:
+            with open(ipy, "r") as f:
                 old = f.read()
         except OSError:
             old = ""
         module = os.path.splitext(os.path.basename(cfg.versionfile_source))[0]
         snippet = INIT_PY_SNIPPET.format(module)
         if OLD_SNIPPET in old:
             print(" replacing boilerplate in %s" % ipy)
@@ -2046,59 +2144,27 @@
                 f.write(snippet)
         else:
             print(" %s unmodified" % ipy)
     else:
         print(" %s doesn't exist, ok" % ipy)
         ipy = None
 
-    # Make sure both the top-level "versioneer.py" and versionfile_source
-    # (PKG/_version.py, used by runtime code) are in MANIFEST.in, so
-    # they'll be copied into source distributions. Pip won't be able to
-    # install the package without this.
-    manifest_in = os.path.join(root, "MANIFEST.in")
-    simple_includes = set()
-    try:
-        with open(manifest_in) as f:
-            for line in f:
-                if line.startswith("include "):
-                    for include in line.split()[1:]:
-                        simple_includes.add(include)
-    except OSError:
-        pass
-    # That doesn't cover everything MANIFEST.in can do
-    # (https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands),
-    # so it might give some false negatives. Appending redundant 'include'
-    # lines is safe, though.
-    if "versioneer.py" not in simple_includes:
-        print(" appending 'versioneer.py' to MANIFEST.in")
-        with open(manifest_in, "a") as f:
-            f.write("include versioneer.py\n")
-    else:
-        print(" 'versioneer.py' already in MANIFEST.in")
-    if cfg.versionfile_source not in simple_includes:
-        print(" appending versionfile_source ('%s') to MANIFEST.in" %
-              cfg.versionfile_source)
-        with open(manifest_in, "a") as f:
-            f.write("include %s\n" % cfg.versionfile_source)
-    else:
-        print(" versionfile_source already in MANIFEST.in")
-
     # Make VCS-specific changes. For git, this means creating/changing
     # .gitattributes to mark _version.py for export-subst keyword
     # substitution.
-    do_vcs_install(manifest_in, cfg.versionfile_source, ipy)
+    do_vcs_install(cfg.versionfile_source, ipy)
     return 0
 
 
 def scan_setup_py():
     """Validate the contents of setup.py against Versioneer's expectations."""
     found = set()
     setters = False
     errors = 0
-    with open("setup.py") as f:
+    with open("setup.py", "r") as f:
         for line in f.readlines():
             if "import versioneer" in line:
                 found.add("import")
             if "versioneer.get_cmdclass()" in line:
                 found.add("cmdclass")
             if "versioneer.get_version()" in line:
                 found.add("get_version")
@@ -2122,14 +2188,18 @@
         print("'versioneer.versionfile_source = ' . This configuration")
         print("now lives in setup.cfg, and should be removed from setup.py")
         print("")
         errors += 1
     return errors
 
 
+def setup_command():
+    """Set up Versioneer and exit with appropriate error code."""
+    errors = do_setup()
+    errors += scan_setup_py()
+    sys.exit(1 if errors else 0)
+
+
 if __name__ == "__main__":
     cmd = sys.argv[1]
     if cmd == "setup":
-        errors = do_setup()
-        errors += scan_setup_py()
-        if errors:
-            sys.exit(1)
+        setup_command()
```

