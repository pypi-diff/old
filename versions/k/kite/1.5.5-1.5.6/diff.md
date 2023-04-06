# Comparing `tmp/kite-1.5.5.tar.gz` & `tmp/kite-1.5.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kite-1.5.5.tar", last modified: Thu Jan 12 14:10:13 2023, max compression
+gzip compressed data, was "kite-1.5.6.tar", last modified: Thu Apr  6 10:33:49 2023, max compression
```

## Comparing `kite-1.5.5.tar` & `kite-1.5.6.tar`

### file list

```diff
@@ -1,169 +1,169 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.194117 kite-1.5.5/
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-01-12 14:09:53.000000 kite-1.5.5/.coveralls.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.174116 kite-1.5.5/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.178116 kite-1.5.5/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     1750 2023-01-12 14:09:53.000000 kite-1.5.5/.github/workflows/build-wheels.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      248 2023-01-12 14:09:53.000000 kite-1.5.5/.github/workflows/lint.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1784 2023-01-12 14:09:53.000000 kite-1.5.5/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-01-12 14:09:53.000000 kite-1.5.5/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-01-12 14:09:53.000000 kite-1.5.5/.travis.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3460 2023-01-12 14:09:53.000000 kite-1.5.5/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (123)    32196 2023-01-12 14:09:53.000000 kite-1.5.5/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-01-12 14:10:13.194117 kite-1.5.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-01-12 14:09:53.000000 kite-1.5.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.178116 kite-1.5.5/docs/
--rw-r--r--   0 runner    (1001) docker     (123)     7607 2023-01-12 14:09:53.000000 kite-1.5.5/docs/Makefile
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.178116 kite-1.5.5/docs/_images/
--rw-r--r--   0 runner    (1001) docker     (123)   117677 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/quadtree-myanmar-quadtree.gif
--rw-r--r--   0 runner    (1001) docker     (123)   149593 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/spool-covariance.png
--rw-r--r--   0 runner    (1001) docker     (123)   157890 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/spool-covariance_noise.png
--rw-r--r--   0 runner    (1001) docker     (123)    91476 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/spool-quadtree_mean.png
--rw-r--r--   0 runner    (1001) docker     (123)    92063 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/spool-quadtree_weight.png
--rw-r--r--   0 runner    (1001) docker     (123)   213100 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/spool-scene.png
--rw-r--r--   0 runner    (1001) docker     (123)   166211 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/talpa-src_add.gif
--rw-r--r--   0 runner    (1001) docker     (123)    48340 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/talpa-src_add.png
--rw-r--r--   0 runner    (1001) docker     (123)    29703 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/talpa-src_dialog.png
--rw-r--r--   0 runner    (1001) docker     (123)   501345 2023-01-12 14:09:53.000000 kite-1.5.5/docs/_images/talpa-src_mod.gif
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.182117 kite-1.5.5/docs/source/
--rw-r--r--   0 runner    (1001) docker     (123)    11270 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/contributing.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.182117 kite-1.5.5/docs/source/examples/
--rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/covariance.rst
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4222 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/quadtree.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/sandbox.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.182117 kite-1.5.5/docs/source/examples/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)      788 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/scripts/covariance-calculation.py
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/scripts/covariance-manual.py
--rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/scripts/sandbox-animation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/scripts/sandboxscene-add_source.py
--rw-r--r--   0 runner    (1001) docker     (123)      414 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/examples/scripts/sandboxscene-save_load.py
--rw-r--r--   0 runner    (1001) docker     (123)      719 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/installation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8844 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/quickstart.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.182117 kite-1.5.5/docs/source/reference/
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      409 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.covariance.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1226 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.quadtree.rst
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.sandboxscene.rst
--rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.scene.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2400 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.sources.rst
--rw-r--r--   0 runner    (1001) docker     (123)      243 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/reference/kite.spool.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.182117 kite-1.5.5/docs/source/tools/
--rw-r--r--   0 runner    (1001) docker     (123)      252 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/tools/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5240 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/tools/spool.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-01-12 14:09:53.000000 kite-1.5.5/docs/source/tools/talpa.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite/
--rw-r--r--   0 runner    (1001) docker     (123)      305 2023-01-12 14:09:53.000000 kite-1.5.5/kite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2621 2023-01-12 14:09:53.000000 kite-1.5.5/kite/aps.py
--rw-r--r--   0 runner    (1001) docker     (123)     1504 2023-01-12 14:09:53.000000 kite-1.5.5/kite/clients.py
--rw-r--r--   0 runner    (1001) docker     (123)    40916 2023-01-12 14:09:53.000000 kite-1.5.5/kite/covariance.py
--rw-r--r--   0 runner    (1001) docker     (123)     1963 2023-01-12 14:09:53.000000 kite-1.5.5/kite/deramp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite/ext/
--rw-r--r--   0 runner    (1001) docker     (123)    12339 2023-01-12 14:09:53.000000 kite-1.5.5/kite/ext/covariance.c
--rw-r--r--   0 runner    (1001) docker     (123)     6491 2023-01-12 14:09:53.000000 kite-1.5.5/kite/gacos.py
--rw-r--r--   0 runner    (1001) docker     (123)    20635 2023-01-12 14:09:53.000000 kite-1.5.5/kite/plot2d.py
--rw-r--r--   0 runner    (1001) docker     (123)      814 2023-01-12 14:09:53.000000 kite-1.5.5/kite/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)    23612 2023-01-12 14:09:53.000000 kite-1.5.5/kite/qt_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    34961 2023-01-12 14:09:53.000000 kite-1.5.5/kite/quadtree.py
--rw-r--r--   0 runner    (1001) docker     (123)    14448 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sandbox_scene.py
--rw-r--r--   0 runner    (1001) docker     (123)    37876 2023-01-12 14:09:53.000000 kite-1.5.5/kite/scene.py
--rw-r--r--   0 runner    (1001) docker     (123)    46486 2023-01-12 14:09:53.000000 kite-1.5.5/kite/scene_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     2280 2023-01-12 14:09:53.000000 kite-1.5.5/kite/scene_mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     2350 2023-01-12 14:09:53.000000 kite-1.5.5/kite/scene_processing.py
--rw-r--r--   0 runner    (1001) docker     (123)     2870 2023-01-12 14:09:53.000000 kite-1.5.5/kite/scene_stack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite/sources/
--rw-r--r--   0 runner    (1001) docker     (123)      256 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    15795 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/compound_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     4771 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/compound_sources.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite/sources/ext/
--rw-r--r--   0 runner    (1001) docker     (123)    11945 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/ext/disloc.c
--rw-r--r--   0 runner    (1001) docker     (123)     8087 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/okada.py
--rw-r--r--   0 runner    (1001) docker     (123)     9632 2023-01-12 14:09:53.000000 kite-1.5.5/kite/sources/pyrocko_gf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite/spool/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3072 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15227 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.190117 kite-1.5.5/kite/spool/res/
--rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/about.ui
--rw-r--r--   0 runner    (1001) docker     (123)     6693 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/boxkite-sketch.jpg
--rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/gacos_correction.ui
--rw-r--r--   0 runner    (1001) docker     (123)     4541 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/logging.ui
--rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/noise_dialog.ui
--rw-r--r--   0 runner    (1001) docker     (123)     9420 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/radar_splash.png
--rw-r--r--   0 runner    (1001) docker     (123)    10911 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/spool.ui
--rw-r--r--   0 runner    (1001) docker     (123)   206673 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/spool_splash.png
--rw-r--r--   0 runner    (1001) docker     (123)     2048 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/transect.ui
--rw-r--r--   0 runner    (1001) docker     (123)     5628 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/res/weight_matrix.ui
--rw-r--r--   0 runner    (1001) docker     (123)     7014 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/scene_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    13811 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/spool.py
--rw-r--r--   0 runner    (1001) docker     (123)     9198 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/tab_aps.py
--rw-r--r--   0 runner    (1001) docker     (123)    29524 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/tab_covariance.py
--rw-r--r--   0 runner    (1001) docker     (123)    14139 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/tab_quadtree.py
--rw-r--r--   0 runner    (1001) docker     (123)    14368 2023-01-12 14:09:53.000000 kite-1.5.5/kite/spool/tab_scene.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.190117 kite-1.5.5/kite/talpa/
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5617 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    17405 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/multiplot.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.190117 kite-1.5.5/kite/talpa/res/
--rw-r--r--   0 runner    (1001) docker     (123)     2648 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/about.ui
--rw-r--r--   0 runner    (1001) docker     (123)    16242 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/dialog_config.ui
--rw-r--r--   0 runner    (1001) docker     (123)     5960 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/dialog_extent.ui
--rw-r--r--   0 runner    (1001) docker     (123)     4512 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/dialog_los.ui
--rw-r--r--   0 runner    (1001) docker     (123)    24371 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/ellipsoid_source.ui
--rw-r--r--   0 runner    (1001) docker     (123)    22641 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/okada_source.ui
--rw-r--r--   0 runner    (1001) docker     (123)    21169 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pCDM_source.ui
--rw-r--r--   0 runner    (1001) docker     (123)    16889 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pyrocko_double_couple.ui
--rw-r--r--   0 runner    (1001) docker     (123)    22165 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pyrocko_moment_tensor.ui
--rw-r--r--   0 runner    (1001) docker     (123)    21068 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pyrocko_rectangular_source.ui
--rw-r--r--   0 runner    (1001) docker     (123)    18322 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pyrocko_ringfault.ui
--rw-r--r--   0 runner    (1001) docker     (123)    18756 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/pyrocko_vlvd_source.ui
--rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/spin_widget.ui
--rw-r--r--   0 runner    (1001) docker     (123)   225370 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/talpa-splash-full.png
--rw-r--r--   0 runner    (1001) docker     (123)     4431 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/talpa.ui
--rw-r--r--   0 runner    (1001) docker     (123)    92602 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/talpa_splash.png
--rw-r--r--   0 runner    (1001) docker     (123)     1924 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/res/window_reference.ui
--rw-r--r--   0 runner    (1001) docker     (123)     5634 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sandbox_model.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.194117 kite-1.5.5/kite/talpa/sources/
--rw-r--r--   0 runner    (1001) docker     (123)      582 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8948 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4199 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources/compound_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources/okada.py
--rw-r--r--   0 runner    (1001) docker     (123)    17763 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources/pyrocko.py
--rw-r--r--   0 runner    (1001) docker     (123)     6544 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/sources_dock.py
--rw-r--r--   0 runner    (1001) docker     (123)     6291 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/talpa.py
--rw-r--r--   0 runner    (1001) docker     (123)     2728 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/tool_dialogs.py
--rw-r--r--   0 runner    (1001) docker     (123)      167 2023-01-12 14:09:53.000000 kite-1.5.5/kite/talpa/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.194117 kite-1.5.5/kite/util/
--rw-r--r--   0 runner    (1001) docker     (123)     6554 2023-01-12 14:09:53.000000 kite-1.5.5/kite/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8222 2023-01-12 14:09:53.000000 kite-1.5.5/kite/util/bbd2kite.py
--rw-r--r--   0 runner    (1001) docker     (123)    12672 2023-01-12 14:09:53.000000 kite-1.5.5/kite/util/stamps2kite.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.186117 kite-1.5.5/kite.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-12 14:10:13.000000 kite-1.5.5/kite.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.194117 kite-1.5.5/maintenance/
--rwxr-xr-x   0 runner    (1001) docker     (123)      924 2023-01-12 14:09:53.000000 kite-1.5.5/maintenance/deploy-docs.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2090 2023-01-12 14:09:53.000000 kite-1.5.5/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-12 14:10:13.194117 kite-1.5.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3852 2023-01-12 14:09:53.000000 kite-1.5.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-12 14:10:13.194117 kite-1.5.5/test/
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-01-12 14:09:53.000000 kite-1.5.5/test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3231 2023-01-12 14:09:53.000000 kite-1.5.5/test/common.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-12 14:09:53.000000 kite-1.5.5/test/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)   333008 2023-01-12 14:09:53.000000 kite-1.5.5/test/covariance_ref.npy
--rw-r--r--   0 runner    (1001) docker     (123)     2884 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_covariance.py
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_deramp.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_gacos.py
--rw-r--r--   0 runner    (1001) docker     (123)     1536 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_scene.py
--rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_scene_stack.py
--rw-r--r--   0 runner    (1001) docker     (123)     5486 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_source_compound_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_source_okada.py
--rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_source_pyrocko.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-01-12 14:09:53.000000 kite-1.5.5/test/test_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.743285 kite-1.5.6/
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 10:33:34.000000 kite-1.5.6/.coveralls.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.719291 kite-1.5.6/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.723290 kite-1.5.6/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     1750 2023-04-06 10:33:34.000000 kite-1.5.6/.github/workflows/build-wheels.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 10:33:34.000000 kite-1.5.6/.github/workflows/lint.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1784 2023-04-06 10:33:34.000000 kite-1.5.6/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      554 2023-04-06 10:33:34.000000 kite-1.5.6/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-04-06 10:33:34.000000 kite-1.5.6/.travis.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3460 2023-04-06 10:33:34.000000 kite-1.5.6/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (123)    32196 2023-04-06 10:33:34.000000 kite-1.5.6/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-04-06 10:33:49.743285 kite-1.5.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-06 10:33:34.000000 kite-1.5.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.723290 kite-1.5.6/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)     7607 2023-04-06 10:33:34.000000 kite-1.5.6/docs/Makefile
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.723290 kite-1.5.6/docs/_images/
+-rw-r--r--   0 runner    (1001) docker     (123)   117677 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/quadtree-myanmar-quadtree.gif
+-rw-r--r--   0 runner    (1001) docker     (123)   149593 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/spool-covariance.png
+-rw-r--r--   0 runner    (1001) docker     (123)   157890 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/spool-covariance_noise.png
+-rw-r--r--   0 runner    (1001) docker     (123)    91476 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/spool-quadtree_mean.png
+-rw-r--r--   0 runner    (1001) docker     (123)    92063 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/spool-quadtree_weight.png
+-rw-r--r--   0 runner    (1001) docker     (123)   213100 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/spool-scene.png
+-rw-r--r--   0 runner    (1001) docker     (123)   166211 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/talpa-src_add.gif
+-rw-r--r--   0 runner    (1001) docker     (123)    48340 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/talpa-src_add.png
+-rw-r--r--   0 runner    (1001) docker     (123)    29703 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/talpa-src_dialog.png
+-rw-r--r--   0 runner    (1001) docker     (123)   501345 2023-04-06 10:33:34.000000 kite-1.5.6/docs/_images/talpa-src_mod.gif
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.723290 kite-1.5.6/docs/source/
+-rw-r--r--   0 runner    (1001) docker     (123)    11270 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/contributing.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.723290 kite-1.5.6/docs/source/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/covariance.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4222 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/quadtree.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/sandbox.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.727289 kite-1.5.6/docs/source/examples/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)      788 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/scripts/covariance-calculation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/scripts/covariance-manual.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/scripts/sandbox-animation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/scripts/sandboxscene-add_source.py
+-rw-r--r--   0 runner    (1001) docker     (123)      414 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/examples/scripts/sandboxscene-save_load.py
+-rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8844 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/quickstart.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.727289 kite-1.5.6/docs/source/reference/
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      409 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.covariance.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1226 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.quadtree.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.sandboxscene.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      690 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.scene.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2400 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.sources.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/reference/kite.spool.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.727289 kite-1.5.6/docs/source/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)      252 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/tools/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5240 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/tools/spool.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-04-06 10:33:34.000000 kite-1.5.6/docs/source/tools/talpa.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.727289 kite-1.5.6/kite/
+-rw-r--r--   0 runner    (1001) docker     (123)      305 2023-04-06 10:33:34.000000 kite-1.5.6/kite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2621 2023-04-06 10:33:34.000000 kite-1.5.6/kite/aps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1504 2023-04-06 10:33:34.000000 kite-1.5.6/kite/clients.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40903 2023-04-06 10:33:34.000000 kite-1.5.6/kite/covariance.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-04-06 10:33:34.000000 kite-1.5.6/kite/deramp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)    12339 2023-04-06 10:33:34.000000 kite-1.5.6/kite/ext/covariance.c
+-rw-r--r--   0 runner    (1001) docker     (123)     6491 2023-04-06 10:33:34.000000 kite-1.5.6/kite/gacos.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20635 2023-04-06 10:33:34.000000 kite-1.5.6/kite/plot2d.py
+-rw-r--r--   0 runner    (1001) docker     (123)      813 2023-04-06 10:33:34.000000 kite-1.5.6/kite/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23541 2023-04-06 10:33:34.000000 kite-1.5.6/kite/qt_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34961 2023-04-06 10:33:34.000000 kite-1.5.6/kite/quadtree.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14448 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sandbox_scene.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37875 2023-04-06 10:33:34.000000 kite-1.5.6/kite/scene.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46486 2023-04-06 10:33:34.000000 kite-1.5.6/kite/scene_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2280 2023-04-06 10:33:34.000000 kite-1.5.6/kite/scene_mask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2350 2023-04-06 10:33:34.000000 kite-1.5.6/kite/scene_processing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-04-06 10:33:34.000000 kite-1.5.6/kite/scene_stack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite/sources/
+-rw-r--r--   0 runner    (1001) docker     (123)      643 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3915 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15795 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/compound_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4768 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/compound_sources.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite/sources/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)    11945 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/ext/disloc.c
+-rw-r--r--   0 runner    (1001) docker     (123)     8086 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/okada.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9631 2023-04-06 10:33:34.000000 kite-1.5.6/kite/sources/pyrocko_gf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite/spool/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3072 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15162 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite/spool/res/
+-rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/about.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     6693 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/boxkite-sketch.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/gacos_correction.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     4541 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/logging.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/noise_dialog.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     9420 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/radar_splash.png
+-rw-r--r--   0 runner    (1001) docker     (123)    10911 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/spool.ui
+-rw-r--r--   0 runner    (1001) docker     (123)   206673 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/spool_splash.png
+-rw-r--r--   0 runner    (1001) docker     (123)     2048 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/transect.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     5628 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/res/weight_matrix.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     7014 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/scene_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13811 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/spool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9189 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/tab_aps.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29524 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/tab_covariance.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14118 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/tab_quadtree.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14368 2023-04-06 10:33:34.000000 kite-1.5.6/kite/spool/tab_scene.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.735287 kite-1.5.6/kite/talpa/
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5606 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17403 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/multiplot.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.739286 kite-1.5.6/kite/talpa/res/
+-rw-r--r--   0 runner    (1001) docker     (123)     2648 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/about.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    16242 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/dialog_config.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     5960 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/dialog_extent.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     4512 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/dialog_los.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    24371 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/ellipsoid_source.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    22641 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/okada_source.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    21169 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pCDM_source.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    16889 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pyrocko_double_couple.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    22165 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pyrocko_moment_tensor.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    21068 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pyrocko_rectangular_source.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    18322 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pyrocko_ringfault.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    18756 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/pyrocko_vlvd_source.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     1882 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/spin_widget.ui
+-rw-r--r--   0 runner    (1001) docker     (123)   225370 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/talpa-splash-full.png
+-rw-r--r--   0 runner    (1001) docker     (123)     4431 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/talpa.ui
+-rw-r--r--   0 runner    (1001) docker     (123)    92602 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/talpa_splash.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1924 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/res/window_reference.ui
+-rw-r--r--   0 runner    (1001) docker     (123)     5632 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sandbox_model.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.739286 kite-1.5.6/kite/talpa/sources/
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8949 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4197 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources/compound_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2473 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources/okada.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17772 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources/pyrocko.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6554 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/sources_dock.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6279 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/talpa.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2698 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/tool_dialogs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      167 2023-04-06 10:33:34.000000 kite-1.5.6/kite/talpa/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.739286 kite-1.5.6/kite/util/
+-rw-r--r--   0 runner    (1001) docker     (123)     6589 2023-04-06 10:33:34.000000 kite-1.5.6/kite/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8190 2023-04-06 10:33:34.000000 kite-1.5.6/kite/util/bbd2kite.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12672 2023-04-06 10:33:34.000000 kite-1.5.6/kite/util/stamps2kite.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.731288 kite-1.5.6/kite.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 10:33:49.000000 kite-1.5.6/kite.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.739286 kite-1.5.6/maintenance/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      924 2023-04-06 10:33:34.000000 kite-1.5.6/maintenance/deploy-docs.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2124 2023-04-06 10:33:34.000000 kite-1.5.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 10:33:49.743285 kite-1.5.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3851 2023-04-06 10:33:34.000000 kite-1.5.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:49.743285 kite-1.5.6/test/
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 10:33:34.000000 kite-1.5.6/test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3231 2023-04-06 10:33:34.000000 kite-1.5.6/test/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:33:34.000000 kite-1.5.6/test/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)   333008 2023-04-06 10:33:34.000000 kite-1.5.6/test/covariance_ref.npy
+-rw-r--r--   0 runner    (1001) docker     (123)     2884 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_covariance.py
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_deramp.py
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_gacos.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1536 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_scene.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1027 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_scene_stack.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5486 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_source_compound_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_source_okada.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_source_pyrocko.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-06 10:33:34.000000 kite-1.5.6/test/test_util.py
```

### Comparing `kite-1.5.5/.github/workflows/build-wheels.yaml` & `kite-1.5.6/.github/workflows/build-wheels.yaml`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/.gitignore` & `kite-1.5.6/.gitignore`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/.pre-commit-config.yaml` & `kite-1.5.6/.pre-commit-config.yaml`

 * *Files 12% similar despite different names*

```diff
@@ -9,17 +9,15 @@
   - id: end-of-file-fixer
   - id: trailing-whitespace
 - repo: https://github.com/codespell-project/codespell
   rev: v2.2.2
   hooks:
   - id: codespell
     args: [--write-changes, "-L ure,nd,ue,parms,Ue,lamda"]
-- repo: https://github.com/pycqa/isort
-  rev: 5.11.4
-  hooks:
-  - id: isort
-    name: isort (python)
-    args: [--profile, black]
 - repo: https://github.com/psf/black
-  rev: 22.12.0
+  rev: 23.1.0
   hooks:
   - id: black
+- repo: https://github.com/charliermarsh/ruff-pre-commit
+  rev: 'v0.0.241'
+  hooks:
+  - id: ruff
```

### Comparing `kite-1.5.5/.travis.yml` & `kite-1.5.6/.travis.yml`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/CHANGELOG.md` & `kite-1.5.6/CHANGELOG.md`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/LICENSE.md` & `kite-1.5.6/LICENSE.md`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/PKG-INFO` & `kite-1.5.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kite
-Version: 1.5.5
+Version: 1.5.6
 Summary: InSAR unwrapped surface displacement processing for earthquake modelling.
 Author-email: Marius Paul Isken <mi@gfz-potsdam.de>, Henriette Sudhaus <hsudhaus@ifg.uni-kiel.de>
 Maintainer-email: Marius Paul Isken <mi@gfz-potsdam.de>
 License: GPLv3
 Project-URL: Home, https://pyrocko.org
 Project-URL: GitHub, https://github.com/pyrocko/kite
 Project-URL: Issues, https://github.com/pyrocko/kite/issues
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: kite Version: 1.5.5 Summary: InSAR unwrapped
+Metadata-Version: 2.1 Name: kite Version: 1.5.6 Summary: InSAR unwrapped
 surface displacement processing for earthquake modelling. Author-email: Marius
 Paul Isken
 gfz-potsdam.de>, Henriette Sudhaus
 ifg.uni-kiel.de> Maintainer-email: Marius Paul Isken
 gfz-potsdam.de> License: GPLv3 Project-URL: Home, https://pyrocko.org Project-
 URL: GitHub, https://github.com/pyrocko/kite Project-URL: Issues, https://
 github.com/pyrocko/kite/issues Keywords:
```

### Comparing `kite-1.5.5/README.md` & `kite-1.5.6/README.md`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/Makefile` & `kite-1.5.6/docs/Makefile`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/quadtree-myanmar-quadtree.gif` & `kite-1.5.6/docs/_images/quadtree-myanmar-quadtree.gif`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/spool-covariance.png` & `kite-1.5.6/docs/_images/spool-covariance.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/spool-covariance_noise.png` & `kite-1.5.6/docs/_images/spool-covariance_noise.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/spool-quadtree_mean.png` & `kite-1.5.6/docs/_images/spool-quadtree_mean.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/spool-quadtree_weight.png` & `kite-1.5.6/docs/_images/spool-quadtree_weight.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/spool-scene.png` & `kite-1.5.6/docs/_images/spool-scene.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/talpa-src_add.gif` & `kite-1.5.6/docs/_images/talpa-src_add.gif`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/talpa-src_add.png` & `kite-1.5.6/docs/_images/talpa-src_add.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/talpa-src_dialog.png` & `kite-1.5.6/docs/_images/talpa-src_dialog.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/_images/talpa-src_mod.gif` & `kite-1.5.6/docs/_images/talpa-src_mod.gif`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/conf.py` & `kite-1.5.6/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/covariance.rst` & `kite-1.5.6/docs/source/examples/covariance.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/quadtree.rst` & `kite-1.5.6/docs/source/examples/quadtree.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/sandbox.rst` & `kite-1.5.6/docs/source/examples/sandbox.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/scripts/covariance-calculation.py` & `kite-1.5.6/docs/source/examples/scripts/covariance-calculation.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/scripts/sandbox-animation.py` & `kite-1.5.6/docs/source/examples/scripts/sandbox-animation.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/examples/scripts/sandboxscene-add_source.py` & `kite-1.5.6/docs/source/examples/scripts/sandboxscene-add_source.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/index.rst` & `kite-1.5.6/docs/source/index.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/installation.rst` & `kite-1.5.6/docs/source/installation.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/quickstart.rst` & `kite-1.5.6/docs/source/quickstart.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/reference/kite.quadtree.rst` & `kite-1.5.6/docs/source/reference/kite.quadtree.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/reference/kite.scene.rst` & `kite-1.5.6/docs/source/reference/kite.scene.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/reference/kite.sources.rst` & `kite-1.5.6/docs/source/reference/kite.sources.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/tools/spool.rst` & `kite-1.5.6/docs/source/tools/spool.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/docs/source/tools/talpa.rst` & `kite-1.5.6/docs/source/tools/talpa.rst`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/aps.py` & `kite-1.5.6/kite/aps.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/clients.py` & `kite-1.5.6/kite/clients.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/covariance.py` & `kite-1.5.6/kite/covariance.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,16 +12,20 @@
 
 import time
 
 from pyrocko import guts
 from pyrocko.guts_array import Array
 
 from kite import covariance_ext
-from kite.util import property_cached  # noqa
-from kite.util import Subject, derampMatrix, squareMatrix, trimMatrix
+from kite.util import (
+    Subject,
+    derampMatrix,
+    property_cached,  # noqa
+    trimMatrix,
+)
 
 __all__ = ["Covariance", "CovarianceConfig"]
 
 NOISE_PATCH_MIN_PX = 256 * 256
 NOISE_PATCH_MAX_NAN = 0.8
 
 noise_regimes = [
@@ -1102,15 +1106,14 @@
     def variance(self, value):
         self.config.variance = float(value)
         # self._clear(config=False, spectrum=False, spatial=False)
         self.evChanged.notify()
 
     @variance.getter
     def variance(self):
-
         if self.config.variance is None and self.config.sampling_method == "spatial":
             structure_spatial, dist = self.structure_spatial
 
             last_20p = -int(structure_spatial.size * 0.2)
             self.config.variance = float(np.mean(structure_spatial[(last_20p):]))
 
         elif self.config.variance is None and self.config.sampling_method == "spectral":
@@ -1135,15 +1138,15 @@
         """
         self._log.debug("Exporting Covariance.weight_matrix to %s" % filename)
         header = (
             "Exported kite.Covariance.weight_matrix, "
             "for more information visit https://pyrocko.org\n"
             "\nThe matrix is symmetric and ordered by QuadNode.id:\n"
         )
-        header += ", ".join([l.id for l in self.quadtree.leaves])
+        header += ", ".join([lv.id for lv in self.quadtree.leaves])
         np.savetxt(filename, self.weight_matrix, header=header)
 
     def get_state_hash(self):
         sha = sha1()
         sha.update(str(self.config).encode())
         return sha.digest().hex()
```

### Comparing `kite-1.5.5/kite/deramp.py` & `kite-1.5.6/kite/deramp.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 import numpy as np
 from pyrocko.guts import Bool
 
 from .plugin import Plugin, PluginConfig
 
 
 class DerampConfig(PluginConfig):
-
     demean = Bool.T(optional=True, default=True)
 
 
 class Deramp(Plugin):
     def __init__(self, scene, config=None):
         self.scene = scene
         self.config = config or DerampConfig()
```

### Comparing `kite-1.5.5/kite/ext/covariance.c` & `kite-1.5.6/kite/ext/covariance.c`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/gacos.py` & `kite-1.5.6/kite/gacos.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/plot2d.py` & `kite-1.5.6/kite/plot2d.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/plugin.py` & `kite-1.5.6/kite/plugin.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 from hashlib import sha1
 
 from pyrocko.guts import Bool, Object
 
 
 class PluginConfig(Object):
-
     applied = Bool.T(default=False)
 
     def get_hash(self):
         sha = sha1()
         sha.update(str(self).encode())
         return sha.hexdigest()
```

### Comparing `kite-1.5.5/kite/qt_utils.py` & `kite-1.5.6/kite/qt_utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 import logging
 import os
 from os import path as op
 
-import pyqtgraph.parametertree.parameterTypes as pTypes
 from PyQt5 import QtCore, QtGui, QtWidgets, uic
 from pyqtgraph.parametertree.parameterTypes import WidgetParameterItem
 
 SCRIPT_DIRECTORY = op.dirname(op.abspath(__file__))
 
 _viridis_data = [
     [68, 1, 84],
@@ -279,26 +278,24 @@
     def newRecord(self, record):
         self.beginInsertRows(QtCore.QModelIndex(), self.nlogs, self.nlogs)
         self.log_records.append(record)
         self.endInsertRows()
 
 
 class SceneLog(QtWidgets.QDialog):
-
     levels = {
         50: "Critical",
         40: "Error",
         30: "Warning",
         20: "Info",
         10: "Debug",
         0: "All",
     }
 
     class LogEntryDelegate(QtWidgets.QStyledItemDelegate):
-
         levels = {
             50: QtWidgets.QStyle.SP_MessageBoxCritical,
             40: QtWidgets.QStyle.SP_MessageBoxCritical,
             30: QtWidgets.QStyle.SP_MessageBoxWarning,
             20: QtWidgets.QStyle.SP_MessageBoxInformation,
             10: QtWidgets.QStyle.SP_FileIcon,
         }
@@ -784,15 +781,15 @@
 
     def _posToValue(self, xpos):
         """converts local pixel x coord to slider value"""
         return scale(xpos, (0, self.width()), (self.min(), self.max()))
 
     def _handleMoveSplitter(self, xpos, index):
         """private method for handling moving splitter handles"""
-        hw = self._splitter.handleWidth()
+        self._splitter.handleWidth()
 
         def _lockWidth(widget):
             width = widget.size().width()
             widget.setMinimumWidth(width)
             widget.setMaximumWidth(width)
 
         def _unlockWidth(widget):
@@ -803,22 +800,22 @@
 
         if index == self._SPLIT_START:
             _lockWidth(self._tail)
             if v >= self.end():
                 return
 
             offset = -20
-            w = xpos + offset
+            xpos + offset
             self._setStart(v)
 
         elif index == self._SPLIT_END:
             _lockWidth(self._head)
             if v <= self.start():
                 return
 
             offset = -40
-            w = self.width() - xpos + offset
+            self.width() - xpos + offset
             self._setEnd(v)
 
         _unlockWidth(self._tail)
         _unlockWidth(self._head)
         _unlockWidth(self._handle)
```

### Comparing `kite-1.5.5/kite/quadtree.py` & `kite-1.5.6/kite/quadtree.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/sandbox_scene.py` & `kite-1.5.6/kite/sandbox_scene.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/scene.py` & `kite-1.5.6/kite/scene.py`

 * *Files 0% similar despite different names*

```diff
@@ -201,15 +201,15 @@
         lat, lon = ne_to_latlon(self.llLat, self.llLon, 0.0, self.dE * self.cols)
         distLon = lon - self.llLon
         return distLon / self.cols
 
     @property
     def dNdegree(self):
         if self.isDegree():
-            return self.dE
+            return self.dN
 
         lat, lon = ne_to_latlon(self.llLat, self.llLon, self.dN * self.rows, 0.0)
         distLat = lat - self.llLat
         return distLat / self.rows
 
     @property
     def spacing(self):
@@ -763,15 +763,14 @@
             self.polygon_mask: None,
             self.deramp: None,
         }
 
     @property
     def displacement(self):
         if self.has_processing_changed() or self._proc_displacement is None:
-
             self._proc_displacement = self._displacement.copy()
             for plugin, state in self.processing_states.items():
                 self.processing_states[plugin] = plugin.get_state_hash()
                 if not plugin.is_enabled():
                     continue
 
                 t = time.time()
```

### Comparing `kite-1.5.5/kite/scene_io.py` & `kite-1.5.6/kite/scene_io.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/scene_mask.py` & `kite-1.5.6/kite/scene_mask.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/scene_processing.py` & `kite-1.5.6/kite/scene_processing.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/scene_stack.py` & `kite-1.5.6/kite/scene_stack.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from datetime import datetime
 
 import numpy as np
 
-from .scene import BaseScene, Scene
+from .scene import Scene
 
 
 def dtime(timestamp):
     return datetime.fromtimestamp(timestamp)
 
 
 class TSScene(Scene):
```

### Comparing `kite-1.5.5/kite/sources/base.py` & `kite-1.5.6/kite/sources/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 
 d2r = np.pi / 180.0
 r2d = 180.0 / np.pi
 km = 1e3
 
 
 class SandboxSource(Object):
-
     lat = Float.T(default=0.0, help="Latitude in [deg]")
     lon = Float.T(default=0.0, help="Longitude in [deg]")
     easting = Float.T(default=0.0, help="Easting in [m]")
     northing = Float.T(default=0.0, help="Northing in [m]")
     depth = Float.T(default=1.0 * km, help="Depth in [m]")
 
     def __init__(self, *args, **kwargs):
@@ -35,15 +34,14 @@
         )
 
     def getParametersArray(self):
         raise NotImplementedError
 
 
 class SandboxSourceRectangular(SandboxSource):
-
     width = Float.T(
         help="Width, downdip in [m]",
         default=10000.0,
     )
     length = Float.T(
         help="Length in [m]",
         default=10000.0,
```

### Comparing `kite-1.5.5/kite/sources/compound_engine.py` & `kite-1.5.6/kite/sources/compound_engine.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/sources/compound_sources.py` & `kite-1.5.6/kite/sources/compound_sources.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 
 d2r = np.pi / 180.0
 r2d = 180.0 / np.pi
 km = 1e3
 
 
 class EllipsoidSource(SandboxSource):
-
     __implements__ = "CompoundModel"
 
     length_x = Float.T(
         help="Length of x semi-axis of ellisoid before rotation in [m]", default=1.0
     )
     length_y = Float.T(
         help="Length of y semi-axis of ellisoid before rotation in [m]", default=1.0
@@ -70,15 +69,14 @@
             "mu": self.mu * 1e9,
             "lamda": self.lamda * 1e9,
         }
         return params
 
 
 class PointCompoundSource(SandboxSource):
-
     __implements__ = "CompoundModel"
 
     rotation_x = Float.T(
         help="Clockwise rotation of ellipsoid around x-axis in [deg]", default=0.0
     )
     rotation_y = Float.T(
         help="Clockwise rotation of ellipsoid around y-axis in [deg]", default=0.0
@@ -117,15 +115,14 @@
             "dVz": self.dVz**3,
             "nu": self.nu,
         }
         return params
 
 
 class CompoundModelProcessor(SourceProcessor):
-
     __implements__ = "CompoundModel"
 
     def process(self, sources, sandbox, nthreads=0):
         result = {
             "processor_profile": dict(),
             "displacement.e": np.zeros(sandbox.frame.npixel),
             "displacement.n": np.zeros(sandbox.frame.npixel),
```

### Comparing `kite-1.5.5/kite/sources/ext/disloc.c` & `kite-1.5.6/kite/sources/ext/disloc.c`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/sources/okada.py` & `kite-1.5.6/kite/sources/okada.py`

 * *Files 0% similar despite different names*

```diff
@@ -101,15 +101,14 @@
 
 
 class OkadaSegment(OkadaSource):
     enabled = Bool.T(default=True, optional=True)
 
 
 class OkadaPath(SandboxSource):
-
     __implements__ = "disloc"
 
     depth = None
     nu = Float.T(default=0.25, help="Poisson's ratio, typically 0.25")
     nodes = List.T(
         default=[],
         optional=True,
```

### Comparing `kite-1.5.5/kite/sources/pyrocko_gf.py` & `kite-1.5.6/kite/sources/pyrocko_gf.py`

 * *Files 0% similar despite different names*

```diff
@@ -227,15 +227,14 @@
             "azimuth": self.azimuth,
             "dip": self.dip,
             "clvd_moment": self.clvd_moment,
         }
 
 
 class PyrockoProcessor(SourceProcessor):
-
     __implements__ = "pyrocko"
 
     def __init__(self, *args):
         SourceProcessor.__init__(self, *args)
         self.engine = gf.LocalEngine()
 
     def process(self, sources, sandbox, nthreads=0):
```

### Comparing `kite-1.5.5/kite/spool/__main__.py` & `kite-1.5.6/kite/spool/__main__.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/base.py` & `kite-1.5.6/kite/spool/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -109,15 +109,15 @@
 
         self.arrow.setStyle(
             angle=0.0, tipAngle=tipAngle, tailLen=tailLen, tailWidth=6, headLen=25
         )
         self.arrow.setRotation(angle)
 
         rect_label = self.label.boundingRect()
-        rect_arr = self.arrow.boundingRect()
+        self.arrow.boundingRect()
 
         self.label.setPos(-rect_label.width() / 2.0, rect_label.height() * 1.33)
 
     def setParentItem(self, parent):
         pg.GraphicsWidget.setParentItem(self, parent)
 
     def boundingRect(self):
@@ -203,16 +203,14 @@
 
         frame = self.model.frame
         scene = self.model.scene
 
         elevation = scene.get_elevation()
 
         contrast = 1.0
-        elevation_angle = 45.0
-        azimuth = 45.0
 
         size_ramp = 10
         ramp = np.linspace(-1, 1, size_ramp)[::-1]
 
         ramp_x = np.tile(ramp, size_ramp).reshape(size_ramp, size_ramp)
         ramp_y = ramp_x.T
         ramp = ramp_x + ramp_y
```

### Comparing `kite-1.5.5/kite/spool/res/about.ui` & `kite-1.5.6/kite/spool/res/about.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/boxkite-sketch.jpg` & `kite-1.5.6/kite/spool/res/boxkite-sketch.jpg`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/gacos_correction.ui` & `kite-1.5.6/kite/spool/res/gacos_correction.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/logging.ui` & `kite-1.5.6/kite/spool/res/logging.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/noise_dialog.ui` & `kite-1.5.6/kite/spool/res/noise_dialog.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/radar_splash.png` & `kite-1.5.6/kite/spool/res/radar_splash.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/spool.ui` & `kite-1.5.6/kite/spool/res/spool.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/spool_splash.png` & `kite-1.5.6/kite/spool/res/spool_splash.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/transect.ui` & `kite-1.5.6/kite/spool/res/transect.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/res/weight_matrix.ui` & `kite-1.5.6/kite/spool/res/weight_matrix.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/scene_model.py` & `kite-1.5.6/kite/spool/scene_model.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/spool.py` & `kite-1.5.6/kite/spool/spool.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/spool/tab_aps.py` & `kite-1.5.6/kite/spool/tab_aps.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import numpy as np
 import pyqtgraph as pg
 import pyqtgraph.parametertree.parameterTypes as pTypes
-from PyQt5 import QtCore, QtGui, QtWidgets
+from PyQt5 import QtCore, QtWidgets
 from pyqtgraph import dockarea
 
 from kite.qt_utils import loadUi
 
 from .base import KiteParameterGroup, KitePlot, KiteView, get_resource
 from .tab_covariance import KiteSubplot
 
@@ -66,15 +66,14 @@
             if msg == QtWidgets.QMessageBox.StandardButton.Yes:
                 self.model.getScene().aps.set_enabled(True)
         else:
             self.model.getScene().aps.set_enabled(False)
 
 
 class KiteAPSPlot(KitePlot):
-
     region_changed = QtCore.pyqtSignal()
 
     class TopoPatchROI(pg.RectROI):
         def _makePen(self):
             # Generate the pen color for this ROI based on its current state.
             if self.mouseHovering:
                 return pen_roi_highlight
@@ -117,15 +116,14 @@
         self.model.sigSceneChanged.connect(self.update)
 
     def deactivatePlot(self):
         self.model.sigSceneChanged.disconnect(self.update)
 
 
 class KiteAPSCorrelation(KiteSubplot):
-
     MAXPOINTS = 10000
 
     def __init__(self, parent_plot):
         KiteSubplot.__init__(self, parent_plot)
 
         self.aps_correlation = pg.ScatterPlotItem(
             antialias=True, brush=brush_aps, pen=pen_aps, size=4
```

### Comparing `kite-1.5.5/kite/spool/tab_covariance.py` & `kite-1.5.6/kite/spool/tab_covariance.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from collections import OrderedDict
 
 import numpy as np
 import pyqtgraph as pg
 import pyqtgraph.parametertree.parameterTypes as pTypes
-from PyQt5 import QtCore, QtGui, QtWidgets
+from PyQt5 import QtCore, QtWidgets
 from pyqtgraph import dockarea
 
 from kite.covariance import CovarianceConfig
 from kite.qt_utils import loadUi
 
 from .base import KiteParameterGroup, KitePlot, KiteToolColormap, KiteView, get_resource
 
@@ -237,18 +237,18 @@
         self.update()
 
     def deactivatePlot(self):
         self.model.sigCovarianceChanged.disconnect(self.update)
 
 
 class KiteCovariogram(KiteSubplot):
-
     legend_template = {
         "exponential": "Model: {0:.2g} e^(-d/{1:.1f}) | RMS: {rms:.4e}",
-        "exponential_cosine": "Model: {0:.2g} e^(-d/{1:.1f}) - cos((d-({2:.1f}))/{3:.1f}) "
+        "exponential_cosine": "Model: {0:.2g}"
+        " e^(-d/{1:.1f}) - cos((d-({2:.1f}))/{3:.1f})"
         "| RMS: {rms:.4e}",
     }
 
     class VarianceLine(pg.InfiniteLine):
         def __init__(self, *args, **kwargs):
             pg.InfiniteLine.__init__(self, *args, **kwargs)
             self.setCursor(QtCore.Qt.SizeVerCursor)
@@ -713,30 +713,28 @@
             meta = model.metaObject()
             meta.invokeMethod(
                 model, "calculateWeightMatrix", QtCore.Qt.QueuedConnection
             )
 
 
 class CovarianceCalcResultDialog(QtWidgets.QMessageBox):
-
     text_tmpl = (
         '<span style="font-family: monospace;">' "Covariance.covariance_matrix</span>"
     )
 
     def __init__(self, model, *args, **kwargs):
         QtWidgets.QMessageBox.__init__(self, *args, **kwargs)
 
         self.setIcon(QtWidgets.QMessageBox.Information)
         self.model = model
         self.setWindowTitle("Covariance Calculation")
         self.setTextFormat(QtCore.Qt.RichText)
 
     @QtCore.pyqtSlot(object)
     def show(self, elapsed_time, *args, **kwargs):
-
         if self.model.covariance.isMatrixPosDefinite(full=True):
             self.setIcon(QtWidgets.QMessageBox.Information)
             self.setText("Finished, %s is positive definite!" % self.text_tmpl)
             self.setInformativeText("")
         else:
             self.setIcon(QtWidgets.QMessageBox.Warning)
             self.setText("<b>%s is not positive definite!</b>" % self.text_tmpl)
```

### Comparing `kite-1.5.5/kite/spool/tab_quadtree.py` & `kite-1.5.6/kite/spool/tab_quadtree.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import math
-import time
 from collections import OrderedDict
 
 import pyqtgraph as pg
 import pyqtgraph.parametertree.parameterTypes as pTypes
-from PyQt5 import QtCore, QtGui, QtWidgets
+from PyQt5 import QtCore, QtWidgets
 
 from kite.qt_utils import SliderWidgetParameterItem
 from kite.quadtree import QuadtreeConfig
 
 from .base import KiteParameterGroup, KitePlot, KiteView
 
 
@@ -44,15 +43,14 @@
 
     @QtCore.pyqtSlot()
     def deactivateView(self):
         self.main_widget.deactivatePlot()
 
 
 class QQuadLeaf(QtCore.QRectF):
-
     leaf_outline = pg.mkPen((255, 255, 255), width=1)
     leaf_fill = pg.mkBrush(0, 0, 0, 0)
 
     def __init__(self, leaf):
         self.id = leaf.id
         QtCore.QRectF.__init__(
             self,
@@ -71,15 +69,14 @@
 class QQuadSelectedLeaf(QQuadLeaf):
     leaf_outline = pg.mkPen((202, 60, 60), width=1)
     leaf_fill = pg.mkBrush(202, 60, 60, 120)
 
 
 class KiteQuadtreePlot(KitePlot):
     def __init__(self, model):
-
         self.components_available = {
             "mean": [
                 "Node.mean displacement",
                 lambda sp: sp.quadtree.leaf_matrix_means,
             ],
             "median": [
                 "Node.median displacement",
```

### Comparing `kite-1.5.5/kite/spool/tab_scene.py` & `kite-1.5.6/kite/spool/tab_scene.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/__main__.py` & `kite-1.5.6/kite/talpa/__main__.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/config.py` & `kite-1.5.6/kite/talpa/config.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import logging
 import os
 from os import path
 
 from PyQt5 import QtCore, QtGui, QtWidgets
-from pyrocko.guts import Bool, Float, Int, List, Object, String, Tuple, load
+from pyrocko.guts import Bool, Float, Int, Object, String, Tuple, load
 
 from kite.qt_utils import loadUi
 
 from .util import get_resource
 
 config_file = path.expanduser("~/.config/kite/talpa_config.yml")
 logger = logging.getLogger("TalpaConfig")
@@ -83,15 +83,14 @@
             createDefaultConfig()
             config_instance = TalpaConfig()
 
     return config_instance
 
 
 class ConfigDialog(QtWidgets.QDialog):
-
     attributes = [
         "show_cursor",
         "default_gf_dir",
         "nvectors",
         "vector_color",
         "vector_relative_length",
         "vector_pen_thickness",
@@ -101,15 +100,15 @@
         "view_los",
     ]
 
     def __init__(self, *args, **kwargs):
         QtWidgets.QDialog.__init__(self, *args, **kwargs)
 
         self.completer = QtWidgets.QCompleter()
-        self.completer_model = QtWidgets.QFileSystemModel(self.completer)
+        self.completer_model = QtGui.QFileSystemModel(self.completer)
         self.completer.setModel(self.completer_model)
         self.completer.setMaxVisibleItems(8)
 
         loadUi(get_resource("dialog_config.ui"), self)
 
         self.ok_button.released.connect(self.setAttributes)
         self.ok_button.released.connect(self.close)
```

### Comparing `kite-1.5.5/kite/talpa/multiplot.py` & `kite-1.5.6/kite/talpa/multiplot.py`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 from .config import getConfig
 from .util import SourceROI
 
 d2r = np.pi / 180.0
 
 
 class SandboxSceneLayout(pg.GraphicsLayoutWidget):
-
     PLOT_VIEWS = ["north", "east", "down", "los"]
 
     def __init__(self, sandbox, *args, **kwargs):
         pg.GraphicsLayoutWidget.__init__(self, **kwargs)
         self.sandbox = sandbox
 
         self.plots = [
@@ -44,15 +43,15 @@
             getConfig().__getattribute__(cfg)
             for cfg in ("view_north", "view_east", "view_down", "view_los")
         ]
 
         visible_plots = [plt for ip, plt in enumerate(self.plots) if config_mask[ip]]
 
         for ip, plt in enumerate(visible_plots):
-            row = ip / 2
+            row = ip // 2
             col = ip % 2 + 1
 
             self.addItem(plt, row=row, col=col)
             plt.showGrid(x=True, y=True)
             plt.hideAxis("bottom")
             plt.hideAxis("left")
             plt.vb.border = pg.mkPen(50, 50, 50)
@@ -211,15 +210,14 @@
     def addCursor(self):
         self.sandbox.cursor_tracker.sigCursorMoved.connect(self.drawCursor)
         self.sandbox.cursor_tracker.sigMouseMoved.connect(self.mouseMoved)
         self.addItem(self.cursor)
 
     @QtCore.pyqtSlot(object)
     def mouseMoved(self, event):
-
         if self.vb.sceneBoundingRect().contains(event[0]):
             map_pos = self.vb.mapSceneToView(event[0])
 
             img_pos = self.image.mapFromScene(event[0])
             pE, pN = img_pos.x(), img_pos.y()
             if (pE < 0 or pN < 0) or (
                 pE > self.image.image.shape[0] or pN > self.image.image.shape[1]
@@ -373,15 +371,14 @@
             self.vectors[ivec].hide()
             ivec += 1
 
         QtWidgets.QGraphicsItemGroup.paint(self, painter, option, parent)
 
 
 class Vector(QtWidgets.QGraphicsItem):
-
     arrow_color = QtGui.QColor(*getConfig().vector_color)
     arrow_brush = QtGui.QBrush(arrow_color, QtCore.Qt.SolidPattern)
     arrow_pen = QtGui.QPen(
         arrow_brush, 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin
     )
 
     relative_length = getConfig().vector_relative_length
```

### Comparing `kite-1.5.5/kite/talpa/res/about.ui` & `kite-1.5.6/kite/talpa/res/about.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/dialog_config.ui` & `kite-1.5.6/kite/talpa/res/dialog_config.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/dialog_extent.ui` & `kite-1.5.6/kite/talpa/res/dialog_extent.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/dialog_los.ui` & `kite-1.5.6/kite/talpa/res/dialog_los.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/ellipsoid_source.ui` & `kite-1.5.6/kite/talpa/res/ellipsoid_source.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/okada_source.ui` & `kite-1.5.6/kite/talpa/res/okada_source.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pCDM_source.ui` & `kite-1.5.6/kite/talpa/res/pCDM_source.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pyrocko_double_couple.ui` & `kite-1.5.6/kite/talpa/res/pyrocko_double_couple.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pyrocko_moment_tensor.ui` & `kite-1.5.6/kite/talpa/res/pyrocko_moment_tensor.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pyrocko_rectangular_source.ui` & `kite-1.5.6/kite/talpa/res/pyrocko_rectangular_source.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pyrocko_ringfault.ui` & `kite-1.5.6/kite/talpa/res/pyrocko_ringfault.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/pyrocko_vlvd_source.ui` & `kite-1.5.6/kite/talpa/res/pyrocko_vlvd_source.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/spin_widget.ui` & `kite-1.5.6/kite/talpa/res/spin_widget.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/talpa-splash-full.png` & `kite-1.5.6/kite/talpa/res/talpa-splash-full.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/talpa.ui` & `kite-1.5.6/kite/talpa/res/talpa.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/talpa_splash.png` & `kite-1.5.6/kite/talpa/res/talpa_splash.png`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/res/window_reference.ui` & `kite-1.5.6/kite/talpa/res/window_reference.ui`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/sandbox_model.py` & `kite-1.5.6/kite/talpa/sandbox_model.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,14 @@
 
 class CursorTracker(QtCore.QObject):
     sigCursorMoved = QtCore.pyqtSignal(object)
     sigMouseMoved = QtCore.pyqtSignal(object)
 
 
 class SandboxModel(QtCore.QObject):
-
     sigModelUpdated = QtCore.pyqtSignal()
     sigModelChanged = QtCore.pyqtSignal()
     sigLogRecord = QtCore.pyqtSignal(object)
 
     sigProcessingFinished = QtCore.pyqtSignal()
     sigProcessingStarted = QtCore.pyqtSignal(str)
 
@@ -108,15 +107,14 @@
 
         sandbox = cls(parent=parent)
         sandbox.setModel(SandboxScene())
         return sandbox
 
 
 class SourceModel(QtCore.QAbstractTableModel):
-
     selectionModelChanged = QtCore.pyqtSignal()
 
     def __init__(self, sandbox, *args, **kwargs):
         QtCore.QAbstractTableModel.__init__(self, *args, **kwargs)
 
         self.sandbox = sandbox
         self.selection_model = None
```

### Comparing `kite-1.5.5/kite/talpa/sources/__init__.py` & `kite-1.5.6/kite/talpa/sources/__init__.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite/talpa/sources/base.py` & `kite-1.5.6/kite/talpa/sources/base.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 from ..util import get_resource
 
 d2r = np.pi / 180.0
 r2d = 180.0 / np.pi
 
 
 class RectangularSourceROI(pg.ROI):
-
     newSourceParameters = QtCore.pyqtSignal(object)
 
     pen_outline = pg.mkPen((46, 125, 50, 100), width=1.25)
     pen_handle = pg.mkPen(((38, 50, 56, 100)), width=1.25)
     pen_highlight = pg.mkPen((52, 175, 60), width=2.5)
 
     def __init__(self, delegate):
@@ -44,15 +43,14 @@
         self.sigRegionChangeFinished.connect(self.setSourceParametersFromROI)
 
         self.setAcceptedMouseButtons(QtCore.Qt.RightButton)
         self.sigClicked.connect(self.showEditingDialog)
 
     @QtCore.pyqtSlot()
     def setSourceParametersFromROI(self):
-
         strike = float((-self.angle()) % 360)
         width = float(self.size().x())
         length = float(self.size().y())
 
         northing = float(self.pos().y() + np.cos(strike * d2r) * length / 2)
         easting = float(self.pos().x() + np.sin(strike * d2r) * length / 2)
 
@@ -92,15 +90,14 @@
         if self.mouseHovering:
             return self.pen_highlight
         else:
             return self.pen
 
 
 class PointSourceROI(pg.EllipseROI):
-
     newSourceParameters = QtCore.pyqtSignal(object)
 
     pen_outline = pg.mkPen((46, 125, 50, 100), width=1.25)
     pen_handle = pg.mkPen(((38, 50, 56, 100)), width=1.25)
     pen_highlight = pg.mkPen((52, 175, 60), width=2.5)
 
     def __init__(self, delegate):
@@ -168,15 +165,14 @@
         if self.mouseHovering:
             return self.pen_highlight
         else:
             return self.pen
 
 
 class SourceDelegate(QtCore.QObject):
-
     __represents__ = "SourceToImplement"
 
     sourceParametersChanged = QtCore.pyqtSignal()
     highlightROI = QtCore.pyqtSignal(bool)
 
     parameters = ["List", "of", "parameters", "from", "kite.source"]
     ro_parameters = ["Read-Only", "parameters"]
@@ -272,15 +268,15 @@
         self.applyButton.released.connect(self.setSourceParameters)
         self.okButton.released.connect(self.setSourceParameters)
         self.okButton.released.connect(self.close)
 
     @QtCore.pyqtSlot()
     def getSourceParameters(self):
         for param, value in self.delegate.getSourceParameters().items():
-            self.__getattribute__(param).setValue(value)
+            self.__getattribute__(param).setValue(int(value))
 
     @QtCore.pyqtSlot()
     def setSourceParameters(self):
         params = {}
         for param in self.delegate.parameters:
             params[param] = self.__getattribute__(param).value()
         self.delegate.updateModelParameters(params)
```

### Comparing `kite-1.5.5/kite/talpa/sources/compound_models.py` & `kite-1.5.6/kite/talpa/sources/compound_models.py`

 * *Files 0% similar despite different names*

```diff
@@ -5,15 +5,14 @@
 from .base import PointSourceROI, SourceDelegate, SourceEditDialog
 
 d2r = np.pi / 180.0
 r2d = 180.0 / np.pi
 
 
 class EllipsoidSourceDelegate(SourceDelegate):
-
     __represents__ = "EllipsoidSource"
 
     display_backend = "Compound Model"
     display_name = "EllipsoidSource"
 
     parameters = [
         "easting",
@@ -80,15 +79,14 @@
     <td>Volume:</td><td>{source.volume:.2e} m<sup>3</sup></td>
 </tr></table>
 """
         return item.format(idx=self.index.row() + 1, delegate=self, source=self.source)
 
 
 class PointCompoundSourceDelegate(SourceDelegate):
-
     __represents__ = "PointCompoundSource"
 
     display_backend = "Compound Model"
     display_name = "PointCompoundSource"
 
     parameters = [
         "easting",
```

### Comparing `kite-1.5.5/kite/talpa/sources/okada.py` & `kite-1.5.6/kite/talpa/sources/okada.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,14 @@
 from .base import RectangularSourceROI, SourceDelegate, SourceEditDialog
 
 d2r = np.pi / 180.0
 r2d = 180.0 / np.pi
 
 
 class OkadaSourceDelegate(SourceDelegate):
-
     __represents__ = "OkadaSource"
 
     display_backend = "Okada"
     display_name = "OkadaSource"
 
     parameters = [
         "easting",
```

### Comparing `kite-1.5.5/kite/talpa/sources/pyrocko.py` & `kite-1.5.6/kite/talpa/sources/pyrocko.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import os
 
 import numpy as np
-from PyQt5 import QtCore, QtGui
+from PyQt5 import QtCore, QtGui, QtWidgets
 
 from kite.sources import (
     PyrockoDoubleCouple,
     PyrockoMomentTensor,
     PyrockoRectangularSource,
     PyrockoRingfaultSource,
     PyrockoVLVDSource,
@@ -18,15 +18,15 @@
 r2d = 180.0 / np.pi
 
 
 class PyrockoSourceDialog(SourceEditDialog):
     def __init__(self, delegate, ui_file, *args, **kwargs):
         SourceEditDialog.__init__(self, delegate, ui_file, *args, **kwargs)
 
-        self.completer = QtGui.QCompleter()
+        self.completer = QtWidgets.QCompleter()
         self.completer_model = QtGui.QFileSystemModel(self.completer)
         self.completer.setModel(self.completer_model)
         self.completer.setMaxVisibleItems(8)
 
         self.chooseStoreDirButton.released.connect(self.chooseStoreDir)
 
         self.completer_model.setRootPath("")
@@ -44,15 +44,14 @@
             self, "Open Pyrocko GF Store", os.getcwd()
         )
         if folder != "":
             self.store_dir.setText(folder)
 
 
 class PyrockoRectangularSourceDelegate(SourceDelegate):
-
     __represents__ = "PyrockoRectangularSource"
 
     display_backend = "pyrocko"
     display_name = "RectangularSource"
 
     parameters = [
         "easting",
@@ -116,15 +115,14 @@
     <td>Slip:</td><td>{source.slip:.2f} m</td>
 </tr></table>
 """
         return item.format(idx=self.index.row() + 1, delegate=self, source=self.source)
 
 
 class PyrockoMomentTensorDelegate(SourceDelegate):
-
     __represents__ = "PyrockoMomentTensor"
 
     display_backend = "pyrocko"
     display_name = "MomentTensor"
 
     parameters = [
         "easting",
@@ -137,15 +135,14 @@
         "mne",
         "mnd",
         "med",
     ]
     ro_parameters = []
 
     class MomentTensorDialog(PyrockoSourceDialog):
-
         scaling_params = ["mnn", "mee", "mdd", "mne", "mnd", "med"]
 
         def __init__(self, *args, **kwargs):
             PyrockoSourceDialog.__init__(
                 self, ui_file="pyrocko_moment_tensor.ui", *args, **kwargs
             )
 
@@ -206,15 +203,14 @@
 </tr>
 </table>
 """
         return item.format(idx=self.index.row() + 1, delegate=self, source=self.source)
 
 
 class PyrockoDoubleCoupleDelegate(SourceDelegate):
-
     __represents__ = "PyrockoDoubleCouple"
 
     display_backend = "pyrocko"
     display_name = "DoubleCouple"
 
     parameters = [
         "easting",
@@ -443,15 +439,14 @@
 </tr>
 </table>
 """
         return item.format(idx=self.index.row() + 1, delegate=self, source=self.source)
 
 
 class PyrockoVLVDSourceDelegate(SourceDelegate):
-
     __represents__ = "PyrockoVLVDSource"
 
     display_backend = "pyrocko"
     display_name = "VLVDSource"
 
     parameters = [
         "easting",
@@ -462,15 +457,14 @@
         "azimuth",
         "dip",
         "clvd_moment",
     ]
     ro_parameters = []
 
     class VLVDSourceDialog(PyrockoSourceDialog):
-
         scaling_params = ["clvd_moment"]
 
         def __init__(self, *args, **kwargs):
             PyrockoSourceDialog.__init__(
                 self, ui_file="pyrocko_vlvd_source.ui", *args, **kwargs
             )
```

### Comparing `kite-1.5.5/kite/talpa/sources_dock.py` & `kite-1.5.6/kite/talpa/sources_dock.py`

 * *Files 1% similar despite different names*

```diff
@@ -129,15 +129,15 @@
             options = QtWidgets.QStyleOptionViewItem(option)
             self.initStyleOption(options, index)
 
             doc = QtGui.QTextDocument()
             doc.setHtml(options.text)
             doc.setTextWidth(options.rect.width())
 
-            return QtCore.QSize(doc.idealWidth(), doc.size().height())
+            return QtCore.QSize(int(doc.idealWidth()), int(doc.size().height()))
 
     class SourceContextMenu(QtWidgets.QMenu):
         def __init__(self, parent, idx, *args, **kwargs):
             QtWidgets.QMenu.__init__(self, parent, *args, **kwargs)
             self.parent = parent
             self.sandbox = parent.sandbox
             self.idx = idx
```

### Comparing `kite-1.5.5/kite/talpa/talpa.py` & `kite-1.5.6/kite/talpa/talpa.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,7 @@
-import sys
-
 from PyQt5 import QtCore, QtGui, QtWidgets
 
 from kite.qt_utils import SceneLog, loadUi, validateFilename
 from kite.sandbox_scene import SandboxScene
 
 from .config import ConfigDialog
 from .multiplot import ModelReferenceDockarea, SandboxSceneDockarea
```

### Comparing `kite-1.5.5/kite/talpa/tool_dialogs.py` & `kite-1.5.6/kite/talpa/tool_dialogs.py`

 * *Files 5% similar despite different names*

```diff
@@ -63,24 +63,24 @@
 
         self.move(
             self.parent().window().mapToGlobal(self.parent().window().rect().center())
             - self.mapToGlobal(self.rect().center())
         )
 
         self.sandbox = sandbox
-        model = self.sandbox.model
+        self.sandbox.model
         self.applyButton.released.connect(self.updateValues)
         self.okButton.released.connect(self.updateValues)
         self.okButton.released.connect(self.close)
 
         self.setValues()
 
     def setValues(self):
-        model = self.sandbox.model
-        phi = np.deg2rad(self.spinlos_phi.value())
-        theta = np.deg2rad(self.spinlos_theta.value())
+        self.sandbox.model
+        np.deg2rad(self.spinlos_phi.value())
+        np.deg2rad(self.spinlos_theta.value())
 
     @QtCore.pyqtSlot()
     def updateValues(self):
         print("updated los!")
         self.sandbox.model.setLOS(self.spinlos_phi.value(), self.spinlos_theta.value())
         self.setValues()
```

### Comparing `kite-1.5.5/kite/util/__init__.py` & `kite-1.5.6/kite/util/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -213,23 +213,23 @@
         """
         try:
             self._listeners.remove(listener)
         except Exception:
             raise AttributeError("%s was not subscribed!", listener.__name__)
 
     def unsubscribeAll(self):
-        for l in self._listeners:
-            self.unsubscribe(l)
+        for listener in self._listeners:
+            self.unsubscribe(listener)
 
     def notify(self, *args, **kwargs):
         if self._mute:
             return
-        for l in self._listeners:
-            if callable(l):
-                self._call(l, *args, **kwargs)
+        for listener in self._listeners:
+            if callable(listener):
+                self._call(listener, *args, **kwargs)
 
     @staticmethod
     def _call(func, *args, **kwargs):
         try:
             for k in kwargs.keys():
                 if k not in func.__code__.co_varnames:
                     k.pop(k)
```

### Comparing `kite-1.5.5/kite/util/bbd2kite.py` & `kite-1.5.6/kite/util/bbd2kite.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import logging
 import os.path as op
 import re
 
 import numpy as np
-import pyrocko.orthodrome as od
 import shapefile
 import utm
 from scipy import stats
 
 from kite.scene import Scene, SceneConfig
 
 log = logging.getLogger("bbd2kite")
```

### Comparing `kite-1.5.5/kite/util/stamps2kite.py` & `kite-1.5.6/kite/util/stamps2kite.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/kite.egg-info/PKG-INFO` & `kite-1.5.6/kite.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kite
-Version: 1.5.5
+Version: 1.5.6
 Summary: InSAR unwrapped surface displacement processing for earthquake modelling.
 Author-email: Marius Paul Isken <mi@gfz-potsdam.de>, Henriette Sudhaus <hsudhaus@ifg.uni-kiel.de>
 Maintainer-email: Marius Paul Isken <mi@gfz-potsdam.de>
 License: GPLv3
 Project-URL: Home, https://pyrocko.org
 Project-URL: GitHub, https://github.com/pyrocko/kite
 Project-URL: Issues, https://github.com/pyrocko/kite/issues
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: kite Version: 1.5.5 Summary: InSAR unwrapped
+Metadata-Version: 2.1 Name: kite Version: 1.5.6 Summary: InSAR unwrapped
 surface displacement processing for earthquake modelling. Author-email: Marius
 Paul Isken
 gfz-potsdam.de>, Henriette Sudhaus
 ifg.uni-kiel.de> Maintainer-email: Marius Paul Isken
 gfz-potsdam.de> License: GPLv3 Project-URL: Home, https://pyrocko.org Project-
 URL: GitHub, https://github.com/pyrocko/kite Project-URL: Issues, https://
 github.com/pyrocko/kite/issues Keywords:
```

### Comparing `kite-1.5.5/kite.egg-info/SOURCES.txt` & `kite-1.5.6/kite.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/maintenance/deploy-docs.sh` & `kite-1.5.6/maintenance/deploy-docs.sh`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/pyproject.toml` & `kite-1.5.6/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,46 +1,49 @@
 [build-system]
-requires = ["wheel", "setuptools >= 61.0.0", "oldest-supported-numpy", "setuptools_scm[toml]>=6.2"]
+requires = [
+  "wheel",
+  "setuptools >= 61.0.0",
+  "oldest-supported-numpy",
+  "setuptools_scm[toml]>=6.2",
+]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "kite"
 requires-python = ">=3.7"
-license = {text = "GPLv3"}
+license = { text = "GPLv3" }
 dynamic = ["version"]
 description = "InSAR unwrapped surface displacement processing for earthquake modelling."
 readme = "README.md"
 authors = [
-  {name = "Marius Paul Isken", email = "mi@gfz-potsdam.de"},
-  {name = "Henriette Sudhaus", email = "hsudhaus@ifg.uni-kiel.de"}
-]
-maintainers = [
-  {name = "Marius Paul Isken", email = "mi@gfz-potsdam.de"}
+  { name = "Marius Paul Isken", email = "mi@gfz-potsdam.de" },
+  { name = "Henriette Sudhaus", email = "hsudhaus@ifg.uni-kiel.de" },
 ]
+maintainers = [{ name = "Marius Paul Isken", email = "mi@gfz-potsdam.de" }]
 keywords = ["InSAR", "satellite", "radar", "earthquake", "optimization"]
 classifiers = [
-    "Intended Audience :: Science/Research",
-    "Topic :: Scientific/Engineering",
-    "Topic :: Scientific/Engineering :: Atmospheric Science",
-    "Topic :: Scientific/Engineering :: Image Recognition",
-    "Topic :: Scientific/Engineering :: Physics",
-    "Topic :: Scientific/Engineering :: Visualization",
-    "Programming Language :: Python :: 3.7",
-    "Programming Language :: C",
-    "Operating System :: POSIX",
-    "Operating System :: MacOS"
+  "Intended Audience :: Science/Research",
+  "Topic :: Scientific/Engineering",
+  "Topic :: Scientific/Engineering :: Atmospheric Science",
+  "Topic :: Scientific/Engineering :: Image Recognition",
+  "Topic :: Scientific/Engineering :: Physics",
+  "Topic :: Scientific/Engineering :: Visualization",
+  "Programming Language :: Python :: 3.7",
+  "Programming Language :: C",
+  "Operating System :: POSIX",
+  "Operating System :: MacOS",
 ]
 dependencies = [
-    "numpy>=1.17.3",
-    "scipy>=1.8.0",
-    "PyQt5>=5.15.7",
-    "pyqtgraph==0.12.4",
-    "pyrocko>=2022.06.10",
-    "utm>=0.7.0",
-    "geojson>=2.5.0"
+  "numpy>=1.17.3",
+  "scipy>=1.8.0",
+  "PyQt5>=5.15.7",
+  "pyqtgraph==0.12.4",
+  "pyrocko>=2022.06.10",
+  "utm>=0.7.0",
+  "geojson>=2.5.0",
 ]
 
 [project.urls]
 Home = "https://pyrocko.org"
 GitHub = "https://github.com/pyrocko/kite"
 Issues = "https://github.com/pyrocko/kite/issues"
 
@@ -54,23 +57,27 @@
 bbd2kite = "kite.util.bbd2kite:main"
 
 [project.gui-scripts]
 spool = "kite.spool.__main__:main"
 talpa = "kite.talpa.__main__:main"
 
 [tool.setuptools]
-packages=[
-    "kite",
-    "kite.util",
-    "kite.sources",
-    "kite.spool",
-    "kite.spool.res",
-    "kite.talpa",
-    "kite.talpa.res",
-    "kite.talpa.sources"
+packages = [
+  "kite",
+  "kite.util",
+  "kite.sources",
+  "kite.spool",
+  "kite.spool.res",
+  "kite.talpa",
+  "kite.talpa.res",
+  "kite.talpa.sources",
 ]
 
 [tool.setuptools.package-data]
 "kite.spool.res" = ["*.ui", "*.jpg", "*.png"]
 "kite.talpa.res" = ["*.ui", "*.jpg", "*.png"]
 
 [tool.setuptools_scm]
+
+[tool.ruff]
+select = ["E", "F", "I"]
+exclude = ["docs/**.py"]
```

### Comparing `kite-1.5.5/setup.py` & `kite-1.5.6/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -89,15 +89,14 @@
 """
             )
     print("Continuing your build without OpenMP...\n")
     return False
 
 
 if _have_openmp():
-
     omp_arg = ["-fopenmp"]
     omp_lib = ["-lgomp"]
 
     if platform.uname()[0] == "Darwin":
         gomp_lib = os.environ.get("GOMPLIB", None)
         if gomp_lib:
             omp_lib.insert(0, "-L{}".format(gomp_lib))
```

### Comparing `kite-1.5.5/test/common.py` & `kite-1.5.6/test/common.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/covariance_ref.npy` & `kite-1.5.6/test/covariance_ref.npy`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_covariance.py` & `kite-1.5.6/test/test_covariance.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_gacos.py` & `kite-1.5.6/test/test_gacos.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_io.py` & `kite-1.5.6/test/test_io.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_scene.py` & `kite-1.5.6/test/test_scene.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_scene_stack.py` & `kite-1.5.6/test/test_scene_stack.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,13 @@
 import logging
 import time
 
-import numpy as np
-
 from kite.quadtree import QuadNode
 from kite.scene import TestScene
 from kite.scene_stack import SceneStack, TSScene
-from kite.spool import spool
 
 logging.basicConfig(level=logging.DEBUG)
 QuadNode.MIN_PIXEL_LENGTH_NODE = 32
 
 t0 = time.time()
 dt = 60 * 60 * 24 * 365.25 / 2
```

### Comparing `kite-1.5.5/test/test_source_compound_models.py` & `kite-1.5.6/test/test_source_compound_models.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_source_okada.py` & `kite-1.5.6/test/test_source_okada.py`

 * *Files identical despite different names*

### Comparing `kite-1.5.5/test/test_source_pyrocko.py` & `kite-1.5.6/test/test_source_pyrocko.py`

 * *Files identical despite different names*

